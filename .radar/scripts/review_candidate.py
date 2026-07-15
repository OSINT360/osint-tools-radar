#!/usr/bin/env python3
"""Accept or reject one discovered candidate without editing CSV files by hand."""

from __future__ import annotations

import argparse
import csv
import sys
from datetime import date

from catalog_common import (
    ALL_CATEGORIES,
    ALL_COLUMNS,
    ROOT,
    categories,
    load_catalog,
    repository_key,
    source_files_for_categories,
    split_values,
    write_csv,
)
from discover_candidates import CANDIDATE_FIELDS, CANDIDATE_PATH


def load_candidates() -> list[dict[str, str]]:
    with CANDIDATE_PATH.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


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
            "Created": candidate["Created"],
            "Last Update": candidate["Last Update"],
            "Stars": candidate["Stars"] or "0",
            "Source Files": "; ".join(source_files),
            "Categories": "; ".join(final_categories),
            "Hosting": candidate["Hosting"],
            "Repository ID": "",
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
