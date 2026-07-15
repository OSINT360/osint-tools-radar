#!/usr/bin/env python3
"""Validate catalogue CSV data and generated Markdown tables."""

from __future__ import annotations

import csv
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse

from catalog_common import (
    AGENTIC_SECTIONS,
    ALL_CATEGORIES,
    ALL_COLUMNS,
    DATA_ROOT,
    RADAR_ROOT,
    README_SECTIONS,
    ROOT,
    TABLE_ALIGNMENT,
    TABLE_HEADER,
    categories,
    format_markdown_row,
    load_catalog,
    repository_key,
    rows_for_category,
    source_files_for_categories,
    split_values,
    stars_as_int,
)


DATE_PATTERN = re.compile(r"\d{4}-\d{2}-\d{2}")
MARKDOWN_LINK_PATTERN = re.compile(r"\[([^]]+)\]\(([^)]+)\)")


class Validation:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def check(self, condition: bool, message: str) -> None:
        if not condition:
            self.errors.append(message)


def parse_markdown_tables(path: Path, validation: Validation) -> dict[str, list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    tables: dict[str, list[str]] = {}
    current_heading = ""
    for index, line in enumerate(lines):
        if line.startswith("## "):
            current_heading = re.sub(r"\s*<sup>.*?</sup>\s*$", "", line[3:]).strip()
            current_heading = re.sub(r"^[^\w]+", "", current_heading)
        if line != TABLE_HEADER:
            continue
        validation.check(
            index + 1 < len(lines) and lines[index + 1] == TABLE_ALIGNMENT,
            f"{path.name}:{index + 1}: invalid table alignment row",
        )
        rows: list[str] = []
        cursor = index + 2
        while cursor < len(lines) and lines[cursor].startswith("| ["):
            cells = [cell.strip() for cell in lines[cursor].strip().strip("|").split("|")]
            validation.check(
                len(cells) == 7,
                f"{path.name}:{cursor + 1}: expected 7 table cells, found {len(cells)}",
            )
            rows.append(lines[cursor])
            cursor += 1
        tables[current_heading] = rows
    return tables


def find_heading_table(tables: dict[str, list[str]], label: str) -> list[str] | None:
    for heading, rows in tables.items():
        if heading == label or heading.endswith(f" {label}"):
            return rows
    return None


def validate_catalog(validation: Validation) -> tuple[list[str], list[dict[str, str]]]:
    fields, rows = load_catalog()
    missing = [field for field in ALL_COLUMNS if field not in fields]
    validation.check(not missing, f"osint-repositories.csv: missing columns: {', '.join(missing)}")

    seen_urls: dict[str, int] = {}
    seen_ids: dict[str, int] = {}
    allowed_status = {"active", "archived", "unavailable", "unknown"}
    for line_number, row in enumerate(rows, 2):
        for field in ("Project", "Target", "Type", "Description", "Hosting"):
            validation.check(bool(row.get(field, "").strip()), f"osint-repositories.csv:{line_number}: missing {field}")
        key = repository_key(row.get("Repository", ""))
        validation.check(bool(key), f"osint-repositories.csv:{line_number}: missing Repository")
        if key:
            validation.check(key not in seen_urls, f"osint-repositories.csv:{line_number}: duplicate Repository: {row['Repository']}")
            seen_urls[key] = line_number
        parsed = urlparse(row.get("Repository", ""))
        validation.check(parsed.scheme == "https" and bool(parsed.netloc), f"osint-repositories.csv:{line_number}: invalid Repository URL")

        repo_id = row.get("Repository ID", "").strip()
        if repo_id:
            identity = f"{row.get('Hosting', '').casefold()}:{repo_id}"
            validation.check(identity not in seen_ids, f"osint-repositories.csv:{line_number}: duplicate Repository ID: {identity}")
            seen_ids[identity] = line_number

        for field in ("Created", "Last Update", "Verified"):
            value = row.get(field, "")
            validation.check(bool(DATE_PATTERN.fullmatch(value)), f"osint-repositories.csv:{line_number}: invalid {field}: {value!r}")
        try:
            stars_as_int(row.get("Stars", ""))
        except ValueError:
            validation.errors.append(f"osint-repositories.csv:{line_number}: invalid Stars: {row.get('Stars')!r}")

        row_categories = categories(row)
        validation.check(bool(row_categories), f"osint-repositories.csv:{line_number}: missing Categories")
        unknown_categories = [value for value in row_categories if value not in ALL_CATEGORIES]
        validation.check(
            not unknown_categories,
            f"osint-repositories.csv:{line_number}: unknown Categories: {', '.join(unknown_categories)}",
        )
        expected_sources = source_files_for_categories(row_categories)
        actual_sources = split_values(row.get("Source Files", ""))
        validation.check(actual_sources == expected_sources, f"osint-repositories.csv:{line_number}: Source Files do not match Categories")
        validation.check(row.get("Repository Status", "") in allowed_status, f"osint-repositories.csv:{line_number}: invalid Repository Status")
        validation.check(row.get("Review Status", "") == "accepted", f"osint-repositories.csv:{line_number}: canonical records must be accepted")
        validation.check(row.get("Archived", "") in {"true", "false"}, f"osint-repositories.csv:{line_number}: invalid Archived")
        validation.check(row.get("Fork", "") in {"", "true", "false"}, f"osint-repositories.csv:{line_number}: invalid Fork")
        if row.get("Repository Status") == "archived":
            validation.check(row.get("Archived") == "true", f"osint-repositories.csv:{line_number}: archived status disagrees with metadata")

    validation.check(len(rows) == len(seen_urls), "osint-repositories.csv: repository uniqueness check failed")
    return fields, rows


def validate_markdown(validation: Validation, rows: list[dict[str, str]]) -> None:
    specifications = {
        ROOT / "README.md": README_SECTIONS,
        ROOT / "EMERGING.md": [("Projects", "Emerging")],
        ROOT / "AGENTIC.md": AGENTIC_SECTIONS,
    }
    for path, sections in specifications.items():
        tables = parse_markdown_tables(path, validation)
        for label, category in sections:
            actual = find_heading_table(tables, label)
            validation.check(actual is not None, f"{path.name}: missing table for {label}")
            if actual is None:
                continue
            expected = [format_markdown_row(row) for row in rows_for_category(rows, category)]
            validation.check(actual == expected, f"{path.name}: generated rows differ in {label}")

        urls: list[str] = []
        for table_rows in tables.values():
            for line in table_rows:
                match = re.search(r"\]\((https://[^)]+)\)", line)
                if match:
                    urls.append(repository_key(match.group(1)))
        validation.check(len(urls) == len(set(urls)), f"{path.name}: duplicate repository rows")


def validate_local_links(validation: Validation) -> None:
    for path in (ROOT / "README.md", ROOT / "EMERGING.md", ROOT / "AGENTIC.md", RADAR_ROOT / "README.md"):
        text = path.read_text(encoding="utf-8")
        for _, target in MARKDOWN_LINK_PATTERN.findall(text):
            if target.startswith(("http://", "https://", "#")):
                continue
            local_path = path.parent / target.split("#", 1)[0]
            validation.check(local_path.exists(), f"{path.name}: missing local link target: {target}")


def validate_auxiliary_csv(validation: Validation) -> None:
    schemas = {
        DATA_ROOT / "candidates.csv": [
            "Project", "Repository", "Hosting", "Discovered", "Discovery Source", "Query",
            "Suggested Target", "Suggested Category", "Description", "Created", "Last Update",
            "Stars", "Language", "License", "Archived", "Fork", "Score", "Confidence",
            "Evidence", "Review Status", "Notes",
        ],
        DATA_ROOT / "snapshots.csv": [
            "Date", "Repository ID", "Repository", "Stars", "Forks", "Open Issues",
            "Last Update", "Archived",
        ],
        DATA_ROOT / "sources.csv": [
            "Name", "Provider", "Query", "Window", "Suggested Target", "Suggested Category", "Enabled",
        ],
    }
    for path, expected in schemas.items():
        validation.check(path.exists(), f"missing automation data file: {path.name}")
        if not path.exists():
            continue
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            header = list(reader.fieldnames or [])
            rows = list(reader)
        validation.check(header == expected, f"{path.name}: invalid header")
        if path.name == "candidates.csv":
            seen: set[str] = set()
            for line_number, row in enumerate(rows, 2):
                key = repository_key(row.get("Repository", ""))
                validation.check(bool(key) and key not in seen, f"candidates.csv:{line_number}: invalid or duplicate Repository")
                seen.add(key)
                validation.check(bool(DATE_PATTERN.fullmatch(row.get("Discovered", ""))), f"candidates.csv:{line_number}: invalid Discovered")
                validation.check(row.get("Review Status") in {"review", "accepted", "rejected"}, f"candidates.csv:{line_number}: invalid Review Status")
                try:
                    stars_as_int(row.get("Stars", ""))
                    int(row.get("Score", ""))
                except ValueError:
                    validation.errors.append(f"candidates.csv:{line_number}: invalid numeric value")
        elif path.name == "snapshots.csv":
            seen_snapshots: set[tuple[str, str]] = set()
            for line_number, row in enumerate(rows, 2):
                identity = row.get("Repository ID") or repository_key(row.get("Repository", ""))
                snapshot_key = (row.get("Date", ""), identity)
                validation.check(
                    bool(identity) and snapshot_key not in seen_snapshots,
                    f"snapshots.csv:{line_number}: invalid or duplicate snapshot",
                )
                seen_snapshots.add(snapshot_key)
                validation.check(bool(DATE_PATTERN.fullmatch(row.get("Date", ""))), f"snapshots.csv:{line_number}: invalid Date")
                validation.check(bool(DATE_PATTERN.fullmatch(row.get("Last Update", ""))), f"snapshots.csv:{line_number}: invalid Last Update")
                try:
                    stars_as_int(row.get("Stars", ""))
                except ValueError:
                    validation.errors.append(f"snapshots.csv:{line_number}: invalid Stars")
        elif path.name == "sources.csv":
            seen_names: set[str] = set()
            for line_number, row in enumerate(rows, 2):
                name = row.get("Name", "")
                validation.check(bool(name) and name not in seen_names, f"sources.csv:{line_number}: missing or duplicate Name")
                seen_names.add(name)
                validation.check(row.get("Provider") in {"GitHub", "GitLab", "Codeberg", "MCP Registry"}, f"sources.csv:{line_number}: unsupported Provider")
                validation.check(bool(row.get("Query", "")), f"sources.csv:{line_number}: missing Query")
                validation.check(row.get("Window") in {"created", "pushed", "updated"}, f"sources.csv:{line_number}: invalid Window")
                validation.check(row.get("Suggested Category") in ALL_CATEGORIES, f"sources.csv:{line_number}: unknown Suggested Category")
                validation.check(row.get("Enabled", "").casefold() in {"true", "false"}, f"sources.csv:{line_number}: invalid Enabled")


def main() -> int:
    validation = Validation()
    _, rows = validate_catalog(validation)
    validate_markdown(validation, rows)
    validate_local_links(validation)
    validate_auxiliary_csv(validation)
    validation.check(not (ROOT / "SOCIAL.md").exists(), "SOCIAL.md must remain merged into README.md")

    if validation.errors:
        print("Catalogue validation failed:", file=sys.stderr)
        for error in validation.errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Catalogue validation passed: {len(rows)} unique repositories")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
