#!/usr/bin/env python3
"""Shared catalogue parsing and formatting helpers."""

from __future__ import annotations

import csv
import re
from datetime import date, timedelta
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[2]
RADAR_ROOT = ROOT / ".radar"
DATA_ROOT = RADAR_ROOT / "data"
CATALOG_PATH = ROOT / "osint-repositories.csv"
MIN_LAST_UPDATE = "2020-01-01"
NEW_PROJECT_WINDOW_DAYS = 14
NEW_PROJECT_MARKER = (
    '<img src=".github/assets/new-dot.svg" width="6" height="6" alt="">'
)
NEW_PROJECT_LEGEND = (
    f"{NEW_PROJECT_MARKER} marks projects added to the catalogue within the last 14 days."
)

PUBLIC_COLUMNS = [
    "Project",
    "Repository",
    "Target",
    "Type",
    "Compatibility",
    "Description",
    "Added",
    "Created",
    "Last Update",
    "Stars",
    "Source Files",
    "Categories",
]

MONITOR_COLUMNS = [
    "Hosting",
    "Repository ID",
    "Platforms",
    "Agent Compatibility",
    "License",
    "Archived",
    "Fork",
    "Repository Status",
    "Verified",
    "Discovery Source",
    "Review Status",
]

ALL_COLUMNS = PUBLIC_COLUMNS + MONITOR_COLUMNS

TABLE_HEADER = (
    "| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |"
)
TABLE_ALIGNMENT = "|:---|:---:|:---:|:---|:---:|:---:|---:|"

README_SECTIONS = [
    ("Person", "Person"),
    ("Username", "Username"),
    ("Email", "Email"),
    ("Phone", "Phone"),
    ("Domain", "Domain"),
    ("IP Address", "IP Address"),
    ("URL", "URL"),
    ("Dark Web", "Dark Web"),
    ("Image", "Image"),
    ("Location", "Location"),
    ("Company", "Company"),
    ("Cryptocurrency", "Cryptocurrency"),
    ("General", "General"),
    ("Cross-platform", "Social platforms / Cross-platform"),
    ("X and Twitter", "Social platforms / X and Twitter"),
    ("Facebook", "Social platforms / Facebook"),
    ("Instagram", "Social platforms / Instagram"),
    ("LinkedIn", "Social platforms / LinkedIn"),
    ("Reddit", "Social platforms / Reddit"),
    ("Telegram", "Social platforms / Telegram"),
    ("TikTok", "Social platforms / TikTok"),
    ("YouTube", "Social platforms / YouTube"),
    ("Snapchat", "Social platforms / Snapchat"),
    ("WhatsApp", "Social platforms / WhatsApp"),
    ("Steam", "Social platforms / Steam"),
    ("GitHub", "Social platforms / GitHub"),
    ("Discord", "Social platforms / Discord"),
]

AGENTIC_SECTIONS = [
    (
        "OSINT investigation and intelligence",
        "Agentic / OSINT investigation and intelligence",
    ),
    (
        "Reconnaissance and threat intelligence",
        "Agentic / Reconnaissance and threat intelligence",
    ),
    (
        "Web research and source discovery",
        "Agentic / Web research and source discovery",
    ),
    (
        "Academic and structured research",
        "Agentic / Academic and structured research",
    ),
]

ALL_CATEGORIES = {
    category for _, category in README_SECTIONS + AGENTIC_SECTIONS
} | {"Emerging"}


def split_values(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def load_catalog(path: Path = CATALOG_PATH) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"Missing CSV header: {path}")
        rows = [{key: value or "" for key, value in row.items()} for row in reader]
        return list(reader.fieldnames), rows


def write_csv(path: Path, fieldnames: list[str], rows: Iterable[dict[str, str]]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fieldnames,
            extrasaction="ignore",
            quoting=csv.QUOTE_ALL,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)
    temporary.replace(path)


def categories(row: dict[str, str]) -> list[str]:
    return split_values(row.get("Categories", ""))


def source_files_for_categories(values: Iterable[str]) -> list[str]:
    files: list[str] = []
    for category in values:
        if category == "Emerging" and "EMERGING.md" not in files:
            files.append("EMERGING.md")
        elif category.startswith("Agentic / ") and "AGENTIC.md" not in files:
            files.append("AGENTIC.md")
        elif (
            category != "Emerging"
            and not category.startswith("Agentic / ")
            and "README.md" not in files
        ):
            files.append("README.md")
    order = {"README.md": 0, "EMERGING.md": 1, "AGENTIC.md": 2}
    return sorted(files, key=order.__getitem__)


def rows_for_category(rows: Iterable[dict[str, str]], category: str) -> list[dict[str, str]]:
    selected = [
        row
        for row in rows
        if category in categories(row) and row.get("Review Status", "accepted") == "accepted"
    ]
    # CSV order is the deterministic tiebreaker so equal-star projects do not
    # jump around when the renderer runs.
    return sorted(selected, key=lambda row: -stars_as_int(row.get("Stars", "0")))


def stars_as_int(value: str) -> int:
    cleaned = value.replace(",", "").strip()
    return int(cleaned or "0")


def markdown_text(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def format_markdown_row(row: dict[str, str], is_new: bool = False) -> str:
    marker = f"{NEW_PROJECT_MARKER} " if is_new else ""
    project = f"{marker}[{markdown_text(row['Project'])}]({row['Repository']})"
    return (
        f"| {project} "
        f"| {markdown_text(row['Type']) or '-'} "
        f"| {markdown_text(row['Compatibility']) or '-'} "
        f"| {markdown_text(row['Description'])} "
        f"| {row['Created']} | {row['Last Update']} "
        f"| {stars_as_int(row['Stars']):,} |"
    )


def verified_date(rows: Iterable[dict[str, str]]) -> str:
    values = [row.get("Verified", "") for row in rows]
    valid = sorted(value for value in values if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value))
    if valid:
        return valid[-1]
    return ""


def repository_key(url: str) -> str:
    return url.strip().lower().removesuffix("/").removesuffix(".git")


def recent_repository_keys(
    rows: Iterable[dict[str, str]],
    reference_date: str,
    window_days: int = NEW_PROJECT_WINDOW_DAYS,
) -> set[str]:
    if not reference_date:
        return set()

    current = date.fromisoformat(reference_date)
    earliest = current - timedelta(days=window_days - 1)
    return {
        repository_key(row.get("Repository", ""))
        for row in rows
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", row.get("Added", ""))
        and earliest <= date.fromisoformat(row["Added"]) <= current
    }
