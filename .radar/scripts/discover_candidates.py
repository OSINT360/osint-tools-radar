#!/usr/bin/env python3
"""Discover repository candidates from configured public hosting and MCP sources."""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import time
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode, urlparse
from urllib.request import Request, urlopen

from catalog_common import DATA_ROOT, load_catalog, repository_key, write_csv


CANDIDATE_PATH = DATA_ROOT / "candidates.csv"
SOURCE_PATH = DATA_ROOT / "sources.csv"
CANDIDATE_FIELDS = [
    "Project", "Repository", "Hosting", "Discovered", "Discovery Source", "Query",
    "Suggested Target", "Suggested Category", "Description", "Created", "Last Update",
    "Stars", "Language", "License", "Archived", "Fork", "Score", "Confidence",
    "Evidence", "Review Status", "Notes",
]

RELEVANCE_TERMS = {
    "osint", "socmint", "geoint", "recon", "reconnaissance", "intelligence",
    "investigation", "forensics", "threat-intelligence", "username", "geolocation",
}


class HttpClient:
    def __init__(self, github_token: str = "", delay: float = 0.0) -> None:
        self.github_token = github_token
        self.delay = delay

    def get(self, url: str, github: bool = False) -> Any:
        headers = {"User-Agent": "osint-tools-radar", "Accept": "application/json"}
        if github:
            headers.update({"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"})
            if self.github_token:
                headers["Authorization"] = f"Bearer {self.github_token}"
        for attempt in range(3):
            if self.delay:
                time.sleep(self.delay)
            try:
                with urlopen(Request(url, headers=headers), timeout=45) as response:
                    return json.load(response)
            except HTTPError as error:
                if error.code in {403, 429, 500, 502, 503, 504} and attempt < 2:
                    retry_after = int(error.headers.get("Retry-After", "0") or "0")
                    time.sleep(max(retry_after, 2 ** (attempt + 1)))
                    continue
                raise
            except (URLError, TimeoutError) as error:
                if attempt == 2:
                    raise RuntimeError(str(error)) from error
                time.sleep(2 ** (attempt + 1))
        raise RuntimeError(f"Unable to fetch {url}")


def clean_text(value: object) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def iso_date(value: object) -> str:
    text = str(value or "")
    return text[:10] if re.match(r"\d{4}-\d{2}-\d{2}", text) else ""


def bool_text(value: object) -> str:
    return "true" if bool(value) else "false"


def candidate_score(item: dict[str, Any]) -> int:
    text = " ".join(
        [clean_text(item.get("name")), clean_text(item.get("description")), " ".join(item.get("topics") or [])]
    ).casefold()
    topics = {str(topic).casefold() for topic in item.get("topics") or []}
    score = 0
    if "osint" in topics or "open-source-intelligence" in topics:
        score += 4
    score += min(3, sum(1 for term in RELEVANCE_TERMS if term in text))
    if item.get("language"):
        score += 1
    if int(item.get("size") or 0) >= 20:
        score += 1
    if item.get("license"):
        score += 1
    if int(item.get("stars") or 0) > 0:
        score += 1
    if item.get("archived"):
        score -= 5
    if item.get("fork"):
        score -= 5
    return score


def confidence(score: int) -> str:
    if score >= 8:
        return "high"
    if score >= 5:
        return "medium"
    return "low"


def github_items(client: HttpClient, source: dict[str, str], since: str, limit: int) -> list[dict[str, Any]]:
    query = source["Query"]
    window = source["Window"]
    if window in {"created", "pushed"}:
        query += f" {window}:>={since}"
    query += " archived:false fork:false"
    params = urlencode({"q": query, "sort": "updated", "order": "desc", "per_page": limit})
    payload = client.get(f"https://api.github.com/search/repositories?{params}", github=True)
    results = []
    for item in payload.get("items", []):
        license_data = item.get("license") or {}
        results.append(
            {
                "name": item.get("name"),
                "url": item.get("html_url"),
                "hosting": "GitHub",
                "description": item.get("description"),
                "created": item.get("created_at"),
                "updated": item.get("pushed_at"),
                "stars": item.get("stargazers_count"),
                "language": item.get("language"),
                "license": license_data.get("spdx_id") if isinstance(license_data, dict) else "",
                "archived": item.get("archived"),
                "fork": item.get("fork"),
                "topics": item.get("topics") or [],
                "size": item.get("size") or 0,
            }
        )
    return results


def gitlab_items(client: HttpClient, source: dict[str, str], since: str, limit: int) -> list[dict[str, Any]]:
    params = urlencode(
        {
            "search": source["Query"], "visibility": "public", "active": "true",
            "last_activity_after": f"{since}T00:00:00Z", "order_by": "last_activity_at",
            "sort": "desc", "per_page": limit,
        }
    )
    payload = client.get(f"https://gitlab.com/api/v4/projects?{params}")
    return [
        {
            "name": item.get("name"), "url": item.get("web_url"), "hosting": "GitLab",
            "description": item.get("description"), "created": item.get("created_at"),
            "updated": item.get("last_activity_at"), "stars": item.get("star_count"),
            "language": "", "license": "", "archived": item.get("archived"),
            "fork": bool(item.get("forked_from_project")), "topics": item.get("topics") or [],
            "size": 0,
        }
        for item in payload
    ]


def codeberg_items(client: HttpClient, source: dict[str, str], since: str, limit: int) -> list[dict[str, Any]]:
    params = urlencode({"q": source["Query"], "limit": min(limit, 50), "sort": "updated", "order": "desc"})
    payload = client.get(f"https://codeberg.org/api/v1/repos/search?{params}")
    results = []
    for item in payload.get("data", []):
        if iso_date(item.get("created_at")) < since and source["Window"] == "created":
            continue
        results.append(
            {
                "name": item.get("name"), "url": item.get("html_url"), "hosting": "Codeberg",
                "description": item.get("description"), "created": item.get("created_at"),
                "updated": item.get("updated_at"), "stars": item.get("stars_count"),
                "language": item.get("language"), "license": "", "archived": item.get("archived"),
                "fork": item.get("fork"), "topics": item.get("topics") or [], "size": item.get("size") or 0,
            }
        )
    return results


def find_repository_url(value: object) -> str:
    if isinstance(value, str) and re.match(r"https://(?:github\.com|gitlab\.com|codeberg\.org)/[^/]+/[^/]+", value):
        return value.split("#", 1)[0].removesuffix(".git")
    if isinstance(value, dict):
        for key in ("repository", "url", "source", "homepage"):
            if key in value:
                found = find_repository_url(value[key])
                if found:
                    return found
        for nested in value.values():
            found = find_repository_url(nested)
            if found:
                return found
    if isinstance(value, list):
        for nested in value:
            found = find_repository_url(nested)
            if found:
                return found
    return ""


def mcp_items(client: HttpClient, source: dict[str, str], since: str, limit: int) -> list[dict[str, Any]]:
    params = urlencode({"search": source["Query"], "limit": min(limit, 100), "updated_since": f"{since}T00:00:00.000Z"})
    payload = client.get(f"https://registry.modelcontextprotocol.io/v0.1/servers?{params}")
    results = []
    for entry in payload.get("servers", []):
        server = entry.get("server", entry)
        url = find_repository_url(server)
        if not url:
            continue
        results.append(
            {
                "name": server.get("name") or url.rstrip("/").rsplit("/", 1)[-1],
                "url": url, "hosting": urlparse(url).netloc, "description": server.get("description"),
                "created": entry.get("publishedAt") or entry.get("createdAt"),
                "updated": entry.get("updatedAt") or entry.get("publishedAt"),
                "stars": 0, "language": "", "license": "", "archived": False,
                "fork": False, "topics": ["mcp"], "size": 1,
            }
        )
    return results


ADAPTERS = {
    "GitHub": github_items,
    "GitLab": gitlab_items,
    "Codeberg": codeberg_items,
    "MCP Registry": mcp_items,
}


def load_sources() -> list[dict[str, str]]:
    with SOURCE_PATH.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def load_candidates(path: Path = CANDIDATE_PATH) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or CANDIDATE_FIELDS), list(reader)


def report_text(new_rows: list[dict[str, str]], errors: list[str], since: str) -> str:
    lines = [
        "# OSINT Tools Radar Candidate Discovery",
        "",
        f"- Scan date: {date.today().isoformat()}",
        f"- Window start: {since}",
        f"- New candidates: {len(new_rows)}",
        f"- Source errors: {len(errors)}",
        "",
    ]
    if new_rows:
        lines.extend(["| Project | Source | Suggested category | Score | Repository |", "|---|---|---|---:|---|"])
        for row in sorted(new_rows, key=lambda item: (-int(item["Score"]), item["Project"].casefold())):
            lines.append(
                f"| {row['Project']} | {row['Discovery Source']} | {row['Suggested Category']} "
                f"| {row['Score']} | [Review]({row['Repository']}) |"
            )
        lines.append("")
    if errors:
        lines.extend(["## Source errors", ""] + [f"- {error}" for error in errors] + [""])
    lines.append("Candidates remain excluded from the public catalogue until their review status is accepted.")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Write .radar/data/candidates.csv")
    parser.add_argument("--lookback-days", type=int, default=14)
    parser.add_argument("--max-per-source", type=int, default=100)
    parser.add_argument("--provider", action="append", default=[], help="Limit providers")
    parser.add_argument("--source", action="append", default=[], help="Limit exact configured source names")
    parser.add_argument("--seed-candidates", type=Path, help="Merge candidates from an existing review branch")
    parser.add_argument("--delay", type=float, default=2.1, help="Delay between source requests")
    parser.add_argument("--report", type=Path, help="Write a Markdown discovery report")
    args = parser.parse_args()

    since = (datetime.now(timezone.utc) - timedelta(days=args.lookback_days)).date().isoformat()
    _, catalog_rows = load_catalog()
    fields, existing_candidates = load_candidates()
    if args.seed_candidates and args.seed_candidates.exists():
        seed_fields, seed_candidates = load_candidates(args.seed_candidates)
        if seed_fields != CANDIDATE_FIELDS:
            print(f"Invalid candidate seed schema: {args.seed_candidates}", file=sys.stderr)
            return 2
        existing_keys = {repository_key(row["Repository"]) for row in existing_candidates}
        for row in seed_candidates:
            key = repository_key(row["Repository"])
            if key not in existing_keys:
                existing_candidates.append(row)
                existing_keys.add(key)
    known = {repository_key(row["Repository"]) for row in catalog_rows}
    known.update(repository_key(row["Repository"]) for row in existing_candidates)
    providers = set(args.provider)
    source_names = set(args.source)
    sources = [
        source for source in load_sources()
        if source.get("Enabled", "").casefold() == "true"
        and (not providers or source["Provider"] in providers)
        and (not source_names or source["Name"] in source_names)
    ]

    client = HttpClient(os.environ.get("GITHUB_TOKEN", ""), args.delay)
    new_rows: list[dict[str, str]] = []
    errors: list[str] = []
    for index, source in enumerate(sources, 1):
        adapter = ADAPTERS.get(source["Provider"])
        if adapter is None:
            errors.append(f"{source['Name']}: unsupported provider {source['Provider']}")
            continue
        try:
            items = adapter(client, source, since, args.max_per_source)
        except Exception as error:
            errors.append(f"{source['Name']}: {error}")
            continue
        added = 0
        for item in items:
            url = clean_text(item.get("url"))
            if not url or repository_key(url) in known:
                continue
            score = candidate_score(item)
            row = {
                "Project": clean_text(item.get("name")) or url.rstrip("/").rsplit("/", 1)[-1],
                "Repository": url, "Hosting": clean_text(item.get("hosting")),
                "Discovered": date.today().isoformat(), "Discovery Source": source["Name"],
                "Query": source["Query"], "Suggested Target": source["Suggested Target"],
                "Suggested Category": source["Suggested Category"],
                "Description": clean_text(item.get("description")), "Created": iso_date(item.get("created")),
                "Last Update": iso_date(item.get("updated")), "Stars": str(item.get("stars") or 0),
                "Language": clean_text(item.get("language")), "License": clean_text(item.get("license")),
                "Archived": bool_text(item.get("archived")), "Fork": bool_text(item.get("fork")),
                "Score": str(score), "Confidence": confidence(score), "Evidence": url,
                "Review Status": "review", "Notes": "",
            }
            new_rows.append(row)
            known.add(repository_key(url))
            added += 1
        print(f"[{index}/{len(sources)}] {source['Name']}: found={len(items)} new={added}")

    all_candidates = existing_candidates + new_rows
    all_candidates.sort(key=lambda row: (row["Review Status"], -int(row["Score"] or 0), row["Project"].casefold()))
    if args.write:
        write_csv(CANDIDATE_PATH, fields or CANDIDATE_FIELDS, all_candidates)
    report = report_text(new_rows, errors, since)
    if args.report:
        args.report.write_text(report, encoding="utf-8")
    else:
        print(report)
    print(f"sources={len(sources)} new_candidates={len(new_rows)} errors={len(errors)}")
    return 1 if errors and not new_rows else 0


if __name__ == "__main__":
    raise SystemExit(main())
