#!/usr/bin/env python3
"""Accept or reject one discovered candidate without editing CSV files by hand."""

from __future__ import annotations

import argparse
import csv
import os
import sys
from datetime import date
from urllib.parse import quote, urlparse

from catalog_common import (
    ALL_CATEGORIES,
    ALL_COLUMNS,
    MIN_LAST_UPDATE,
    ROOT,
    categories,
    load_catalog,
    repository_key,
    source_files_for_categories,
    split_values,
    write_csv,
)
from discover_candidates import CANDIDATE_FIELDS, CANDIDATE_PATH, HttpClient
from refresh_metadata import GitHubClient, bool_text, github_coordinates


def load_candidates() -> list[dict[str, str]]:
    with CANDIDATE_PATH.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def refresh_github_candidate(candidate: dict[str, str]) -> str:
    coordinates = github_coordinates(candidate["Repository"])
    if coordinates is None:
        return ""
    owner, repository = coordinates
    client = GitHubClient(os.environ.get("GITHUB_TOKEN", ""))
    status, metadata = client.get_repository(owner, repository)
    if status == 404 or metadata is None:
        raise RuntimeError("repository is unavailable")
    if metadata.get("archived"):
        candidate["Archived"] = "true"
        raise RuntimeError("repository is archived")

    default_branch = str(metadata.get("default_branch") or "")
    if not default_branch:
        raise RuntimeError("repository has no default branch")
    _, branch_commit = client.get_default_branch_commit(owner, repository, default_branch)
    if branch_commit is None:
        raise RuntimeError("default branch commit could not be verified")
    commit_data = branch_commit.get("commit") or {}
    committer_data = commit_data.get("committer") if isinstance(commit_data, dict) else {}
    author_data = commit_data.get("author") if isinstance(commit_data, dict) else {}
    committed_at = ""
    if isinstance(committer_data, dict):
        committed_at = str(committer_data.get("date") or "")
    if not committed_at and isinstance(author_data, dict):
        committed_at = str(author_data.get("date") or "")
    if not committed_at:
        raise RuntimeError("default branch commit date could not be verified")

    license_data = metadata.get("license") or {}
    license_id = license_data.get("spdx_id") if isinstance(license_data, dict) else ""
    if license_id == "NOASSERTION":
        license_id = ""
    candidate.update(
        {
            "Repository": str(metadata.get("html_url") or candidate["Repository"]),
            "Hosting": "GitHub",
            "Created": str(metadata.get("created_at") or "")[:10],
            "Last Update": committed_at[:10],
            "Stars": str(metadata.get("stargazers_count") or 0),
            "Language": str(metadata.get("language") or candidate.get("Language") or ""),
            "License": str(license_id or ""),
            "Archived": "false",
            "Fork": bool_text(metadata.get("fork")),
        }
    )
    return str(metadata.get("id") or "")


def refresh_gitlab_candidate(candidate: dict[str, str]) -> str:
    parsed = urlparse(candidate["Repository"])
    project_path = parsed.path.strip("/")
    if parsed.netloc.casefold() != "gitlab.com" or not project_path:
        raise RuntimeError("invalid GitLab repository URL")
    client = HttpClient()
    metadata = client.get(
        f"https://gitlab.com/api/v4/projects/{quote(project_path, safe='')}"
    )
    if not isinstance(metadata, dict):
        raise RuntimeError("GitLab returned invalid repository metadata")
    if metadata.get("archived"):
        raise RuntimeError("repository is archived")
    default_branch = str(metadata.get("default_branch") or "")
    if not default_branch:
        raise RuntimeError("repository has no default branch")
    commits = client.get(
        f"https://gitlab.com/api/v4/projects/{metadata['id']}/repository/commits"
        f"?ref_name={quote(default_branch, safe='')}&per_page=1"
    )
    if not isinstance(commits, list) or not commits:
        raise RuntimeError("default branch commit could not be verified")
    committed_at = str(commits[0].get("committed_date") or "")
    if not committed_at:
        raise RuntimeError("default branch commit date could not be verified")
    candidate.update(
        {
            "Repository": str(metadata.get("web_url") or candidate["Repository"]),
            "Hosting": "GitLab",
            "Created": str(metadata.get("created_at") or "")[:10],
            "Last Update": committed_at[:10],
            "Stars": str(metadata.get("star_count") or 0),
            "Archived": "false",
            "Fork": bool_text(metadata.get("forked_from_project")),
        }
    )
    return str(metadata.get("id") or "")


def refresh_codeberg_candidate(candidate: dict[str, str]) -> str:
    parsed = urlparse(candidate["Repository"])
    parts = [part for part in parsed.path.strip("/").split("/") if part]
    if parsed.netloc.casefold() != "codeberg.org" or len(parts) < 2:
        raise RuntimeError("invalid Codeberg repository URL")
    owner, repository = parts[:2]
    client = HttpClient()
    metadata = client.get(
        f"https://codeberg.org/api/v1/repos/{quote(owner)}/{quote(repository)}"
    )
    if not isinstance(metadata, dict):
        raise RuntimeError("Codeberg returned invalid repository metadata")
    if metadata.get("archived"):
        raise RuntimeError("repository is archived")
    default_branch = str(metadata.get("default_branch") or "")
    if not default_branch:
        raise RuntimeError("repository has no default branch")
    branch = client.get(
        f"https://codeberg.org/api/v1/repos/{quote(owner)}/{quote(repository)}"
        f"/branches/{quote(default_branch, safe='')}"
    )
    commit = branch.get("commit") if isinstance(branch, dict) else {}
    committed_at = str(commit.get("timestamp") or "") if isinstance(commit, dict) else ""
    if not committed_at:
        raise RuntimeError("default branch commit date could not be verified")
    candidate.update(
        {
            "Repository": str(metadata.get("html_url") or candidate["Repository"]),
            "Hosting": "Codeberg",
            "Created": str(metadata.get("created_at") or "")[:10],
            "Last Update": committed_at[:10],
            "Stars": str(metadata.get("stars_count") or 0),
            "Language": str(metadata.get("language") or candidate.get("Language") or ""),
            "Archived": "false",
            "Fork": bool_text(metadata.get("fork")),
        }
    )
    return str(metadata.get("id") or "")


def refresh_candidate_metadata(candidate: dict[str, str]) -> str:
    host = urlparse(candidate["Repository"]).netloc.casefold()
    if host == "github.com":
        return refresh_github_candidate(candidate)
    if host == "gitlab.com":
        return refresh_gitlab_candidate(candidate)
    if host == "codeberg.org":
        return refresh_codeberg_candidate(candidate)
    raise RuntimeError(f"unsupported repository host: {host or 'missing'}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository", help="Candidate repository URL")
    decision = parser.add_mutually_exclusive_group(required=True)
    decision.add_argument("--accept", action="store_true")
    decision.add_argument("--reject", action="store_true")
    parser.add_argument("--project", help="Override project name")
    parser.add_argument("--target", help="Final target")
    parser.add_argument("--category", action="append", default=[], help="Final category; may be repeated")
    parser.add_argument("--type", dest="project_type", help="Language or integration type")
    parser.add_argument("--compatibility", default="-", help="Published compatibility value")
    parser.add_argument("--description", help="Curated neutral description")
    parser.add_argument("--notes", default="")
    args = parser.parse_args()

    candidates = load_candidates()
    key = repository_key(args.repository)
    candidate = next((row for row in candidates if repository_key(row["Repository"]) == key), None)
    if candidate is None:
        print(f"Candidate not found: {args.repository}", file=sys.stderr)
        return 1

    if args.reject:
        candidate["Review Status"] = "rejected"
        candidate["Notes"] = args.notes
        write_csv(CANDIDATE_PATH, CANDIDATE_FIELDS, candidates)
        print(f"rejected {candidate['Repository']}")
        return 0

    repository_id = ""
    try:
        repository_id = refresh_candidate_metadata(candidate)
    except Exception as error:
        print(
            f"Candidate metadata verification failed: {candidate['Repository']}: {error}",
            file=sys.stderr,
        )
        return 1
    key = repository_key(candidate["Repository"])

    if candidate.get("Archived") == "true":
        print(
            f"Archived repositories cannot be accepted: {candidate['Repository']}",
            file=sys.stderr,
        )
        return 1

    if candidate.get("Last Update", "") < MIN_LAST_UPDATE:
        print(
            f"Repositories inactive since before {MIN_LAST_UPDATE} cannot be accepted: "
            f"{candidate['Repository']}",
            file=sys.stderr,
        )
        return 1

    required = {
        "target": args.target,
        "category": args.category,
        "type": args.project_type,
        "description": args.description,
    }
    missing = [name for name, value in required.items() if not value]
    if missing:
        print(f"Acceptance requires: {', '.join('--' + name for name in missing)}", file=sys.stderr)
        return 2

    fields, catalogue = load_catalog()
    if any(repository_key(row["Repository"]) == key for row in catalogue):
        print(f"Repository is already catalogued: {candidate['Repository']}", file=sys.stderr)
        return 1
    for field in ALL_COLUMNS:
        if field not in fields:
            fields.append(field)

    final_categories: list[str] = []
    for value in args.category:
        final_categories.extend(split_values(value))
    final_categories = list(dict.fromkeys(final_categories))
    invalid_categories = [value for value in final_categories if value not in ALL_CATEGORIES]
    if invalid_categories:
        print(f"Unknown category: {', '.join(invalid_categories)}", file=sys.stderr)
        return 2
    source_files = source_files_for_categories(final_categories)
    social_category = next(
        (value.split(" / ", 1)[1] for value in final_categories if value.startswith("Social platforms / ")),
        "",
    )
    agentic = any(value.startswith("Agentic / ") for value in final_categories)
    compatibility_parts = split_values(args.compatibility)

    catalogue.append(
        {
            "Project": args.project or candidate["Project"],
            "Repository": candidate["Repository"],
            "Target": args.target or candidate["Suggested Target"],
            "Type": args.project_type or candidate["Language"] or "Unknown",
            "Compatibility": args.compatibility,
            "Description": args.description or candidate["Description"],
            "Added": date.today().isoformat(),
            "Created": candidate["Created"],
            "Last Update": candidate["Last Update"],
            "Stars": candidate["Stars"] or "0",
            "Source Files": "; ".join(source_files),
            "Categories": "; ".join(final_categories),
            "Hosting": candidate["Hosting"],
            "Repository ID": repository_id,
            "Platforms": (
                compatibility_parts[0]
                if social_category and args.compatibility != "-" and compatibility_parts
                else social_category
            ),
            "Agent Compatibility": (
                "; ".join(compatibility_parts[1:])
                if social_category and agentic and len(compatibility_parts) > 1
                else (args.compatibility if agentic and not social_category and args.compatibility != "-" else "")
            ),
            "License": candidate["License"],
            "Archived": candidate["Archived"],
            "Fork": candidate["Fork"],
            "Repository Status": "archived" if candidate["Archived"] == "true" else "active",
            "Verified": date.today().isoformat(),
            "Discovery Source": candidate["Discovery Source"],
            "Review Status": "accepted",
        }
    )
    candidate["Review Status"] = "accepted"
    candidate["Notes"] = args.notes
    write_csv(ROOT / "osint-repositories.csv", fields, catalogue)
    write_csv(CANDIDATE_PATH, CANDIDATE_FIELDS, candidates)
    print(f"accepted {candidate['Repository']}; run render_catalog.py --write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
