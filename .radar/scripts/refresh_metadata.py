#!/usr/bin/env python3
"""Refresh tracked GitHub repository metadata and append point-in-time snapshots."""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import time
from datetime import date
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlparse
from urllib.request import Request, urlopen

from catalog_common import ALL_COLUMNS, DATA_ROOT, ROOT, load_catalog, repository_key, write_csv


SNAPSHOT_PATH = DATA_ROOT / "snapshots.csv"
SNAPSHOT_FIELDS = [
    "Date", "Repository ID", "Repository", "Stars", "Forks", "Open Issues",
    "Last Update", "Archived",
]


class GitHubClient:
    def __init__(self, token: str = "", delay: float = 0.0) -> None:
        self.token = token
        self.delay = delay

    def get_repository(self, owner: str, repository: str) -> tuple[int, dict[str, object] | None]:
        url = f"https://api.github.com/repos/{quote(owner)}/{quote(repository)}"
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "osint-tools-radar",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        for attempt in range(3):
            if self.delay:
                time.sleep(self.delay)
            try:
                with urlopen(Request(url, headers=headers), timeout=30) as response:
                    return response.status, json.load(response)
            except HTTPError as error:
                if error.code == 404:
                    return 404, None
                if error.code in {403, 429, 500, 502, 503, 504} and attempt < 2:
                    retry_after = int(error.headers.get("Retry-After", "0") or "0")
                    time.sleep(max(retry_after, 2 ** (attempt + 1)))
                    continue
                raise
            except (URLError, TimeoutError) as error:
                if attempt == 2:
                    raise RuntimeError(str(error)) from error
                time.sleep(2 ** (attempt + 1))
        raise RuntimeError(f"Unable to fetch {owner}/{repository}")


def github_coordinates(url: str) -> tuple[str, str] | None:
    parsed = urlparse(url)
    if parsed.netloc.casefold() != "github.com":
        return None
    parts = [part for part in parsed.path.strip("/").split("/") if part]
    if len(parts) < 2:
        return None
    return parts[0], parts[1].removesuffix(".git")


def bool_text(value: object) -> str:
    return "true" if bool(value) else "false"


def load_snapshots() -> list[dict[str, str]]:
    if not SNAPSHOT_PATH.exists():
        return []
    with SNAPSHOT_PATH.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def update_snapshot(rows: list[dict[str, str]], snapshot: dict[str, str]) -> None:
    key = (snapshot["Date"], snapshot["Repository ID"] or repository_key(snapshot["Repository"]))
    for index, row in enumerate(rows):
        existing = (row["Date"], row["Repository ID"] or repository_key(row["Repository"]))
        if existing == key:
            rows[index] = snapshot
            return
    rows.append(snapshot)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Write refreshed metadata")
    parser.add_argument("--snapshot", action="store_true", help="Append or update today's snapshot")
    parser.add_argument("--limit", type=int, default=0, help="Process at most this many repositories")
    parser.add_argument("--repository", action="append", default=[], help="Process only matching repository URL")
    parser.add_argument("--delay", type=float, default=0.0, help="Delay between API requests")
    args = parser.parse_args()

    fields, rows = load_catalog()
    for field in ALL_COLUMNS:
        if field not in fields:
            fields.append(field)

    requested = {repository_key(value) for value in args.repository}
    selected = [
        row for row in rows
        if (not requested or repository_key(row["Repository"]) in requested)
        and github_coordinates(row["Repository"])
    ]
    if args.limit:
        selected = selected[: args.limit]

    client = GitHubClient(os.environ.get("GITHUB_TOKEN", ""), args.delay)
    snapshots = load_snapshots()
    today = date.today().isoformat()
    changed_fields = 0
    unavailable = 0
    failures: list[str] = []

    for index, row in enumerate(selected, 1):
        coordinates = github_coordinates(row["Repository"])
        assert coordinates is not None
        owner, repository = coordinates
        try:
            status, metadata = client.get_repository(owner, repository)
        except Exception as error:  # network and API failures must not mark a repository unavailable
            failures.append(f"{row['Repository']}: {error}")
            continue

        if status == 404 or metadata is None:
            unavailable += 1
            if row.get("Repository Status") != "unavailable":
                row["Repository Status"] = "unavailable"
                changed_fields += 1
            row["Verified"] = today
            print(f"[{index}/{len(selected)}] unavailable {row['Repository']}")
            continue

        license_data = metadata.get("license") or {}
        license_id = license_data.get("spdx_id") if isinstance(license_data, dict) else ""
        if license_id == "NOASSERTION":
            license_id = ""
        pushed_at = str(metadata.get("pushed_at") or "")[:10]
        canonical_url = str(metadata.get("html_url") or row["Repository"])
        archived = bool(metadata.get("archived"))
        updates = {
            "Repository": canonical_url,
            "Hosting": "GitHub",
            "Repository ID": str(metadata.get("id") or ""),
            "Created": str(metadata.get("created_at") or "")[:10],
            "Last Update": pushed_at,
            "Stars": str(metadata.get("stargazers_count") or 0),
            "License": str(license_id or ""),
            "Archived": bool_text(archived),
            "Fork": bool_text(metadata.get("fork")),
            "Repository Status": "archived" if archived else "active",
            "Verified": today,
        }
        for field, value in updates.items():
            if row.get(field, "") != value:
                row[field] = value
                changed_fields += 1

        if args.snapshot:
            update_snapshot(
                snapshots,
                {
                    "Date": today,
                    "Repository ID": str(metadata.get("id") or ""),
                    "Repository": canonical_url,
                    "Stars": str(metadata.get("stargazers_count") or 0),
                    "Forks": str(metadata.get("forks_count") or 0),
                    "Open Issues": str(metadata.get("open_issues_count") or 0),
                    "Last Update": pushed_at,
                    "Archived": bool_text(archived),
                },
            )
        print(f"[{index}/{len(selected)}] refreshed {owner}/{repository}")

    if failures:
        print("Metadata refresh failed without writing partial results:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    canonical = [repository_key(row["Repository"]) for row in rows]
    if len(canonical) != len(set(canonical)):
        print("Metadata refresh produced duplicate canonical URLs; no files were written", file=sys.stderr)
        return 1

    if args.write:
        write_csv(ROOT / "osint-repositories.csv", fields, rows)
        if args.snapshot:
            snapshots.sort(key=lambda row: (row["Date"], repository_key(row["Repository"])))
            write_csv(SNAPSHOT_PATH, SNAPSHOT_FIELDS, snapshots)
    print(
        f"processed={len(selected)} changed_fields={changed_fields} "
        f"unavailable={unavailable} mode={'write' if args.write else 'dry-run'}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
