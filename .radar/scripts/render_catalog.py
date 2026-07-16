#!/usr/bin/env python3
"""Render Markdown catalogue tables and counters from osint-repositories.csv."""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path

from catalog_common import (
    AGENTIC_SECTIONS,
    NEW_PROJECT_MARKER,
    README_SECTIONS,
    ROOT,
    TABLE_HEADER,
    format_markdown_row,
    load_catalog,
    markdown_text,
    recent_repository_keys,
    repository_key,
    rows_for_category,
    split_values,
    stars_as_int,
    verified_date,
)

TIMELINE_HEADER = "| Project | Target | Categories | Description | Stars |"
TIMELINE_ALIGNMENT = "|:---|:---|:---|:---|---:|"
LEGACY_TABLE_HEADER = (
    "| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |"
)


def count_label(count: int) -> str:
    return "project" if count == 1 else "projects"


def heading_matches(line: str, label: str) -> bool:
    if not line.startswith("## "):
        return False
    title = re.sub(r"\s*<sup>.*?</sup>\s*$", "", line[3:]).strip()
    return title == label or title.endswith(f" {label}")


def replace_section_table(text: str, label: str, rendered_rows: list[str]) -> str:
    lines = text.splitlines()
    heading_index = next(
        (index for index, line in enumerate(lines) if heading_matches(line, label)),
        None,
    )
    if heading_index is None:
        raise ValueError(f"Cannot find Markdown section: {label}")

    count = len(rendered_rows)
    clean_heading = re.sub(r"\s*<sup>.*?</sup>\s*$", "", lines[heading_index]).rstrip()
    lines[heading_index] = f"{clean_heading} <sup>{count} {count_label(count)}</sup>"

    header_index = next(
        (
            index
            for index in range(heading_index + 1, min(len(lines), heading_index + 12))
            if lines[index] in {TABLE_HEADER, LEGACY_TABLE_HEADER}
        ),
        None,
    )
    if header_index is None:
        raise ValueError(f"Cannot find table below section: {label}")
    lines[header_index] = TABLE_HEADER

    first_row = header_index + 2
    last_row = first_row
    marker_pattern = (
        r'(?:<img src="\.github/assets/new-dot\.svg"[^>]*>'
        r"|<sup>🟢</sup>|🟢) "
    )
    while last_row < len(lines) and re.match(
        rf"^\| (?:{marker_pattern})?\[",
        lines[last_row],
    ):
        last_row += 1
    lines[first_row:last_row] = rendered_rows
    return "\n".join(lines) + "\n"


def replace_toc_count(text: str, label: str, count: int) -> str:
    anchor = re.sub(r"[^a-z0-9 -]", "", label.casefold()).replace(" ", "-")
    pattern = re.compile(
        rf"(\[{re.escape(label)}\]\(#{re.escape(anchor)}\)\s*<sup>)\d+\s+projects?(</sup>)"
    )
    return pattern.sub(rf"\g<1>{count} {count_label(count)}\2", text)


def replace_number_badge(text: str, alt_label: str, slug: str, value: int) -> str:
    text = re.sub(
        rf'alt="{re.escape(alt_label)}: \d+"',
        f'alt="{alt_label}: {value}"',
        text,
    )
    return re.sub(
        rf"(badge/{re.escape(slug)}-)\d+(-)",
        rf"\g<1>{value}\2",
        text,
    )


def replace_update_date(text: str, date: str) -> str:
    if not date:
        return text
    badge_date = date.replace("-", "--")
    text = re.sub(r'alt="Last update: \d{4}-\d{2}-\d{2}"', f'alt="Last update: {date}"', text)
    return re.sub(
        r"(badge/last_update-)\d{4}--\d{2}--\d{2}(-)",
        rf"\g<1>{badge_date}\2",
        text,
    )


def replace_discord_empty_state(text: str, count: int) -> str:
    note = "No implementation-bearing public repository from the reviewed sources passed the inclusion criteria."
    pattern = re.compile(
        rf"(## Discord <sup>\d+\s+projects?</sup>\n\n)(?:{re.escape(note)}\n\n)?(?={re.escape(TABLE_HEADER)})"
    )
    replacement = rf"\g<1>{note}\n\n" if count == 0 else r"\g<1>"
    return pattern.sub(replacement, text)


def rendered_rows(
    rows: list[dict[str, str]],
    recent_keys: set[str],
) -> list[str]:
    return [
        format_markdown_row(row, repository_key(row["Repository"]) in recent_keys)
        for row in rows
    ]


def render_readme(
    text: str,
    rows: list[dict[str, str]],
    date: str,
    recent_keys: set[str],
) -> str:
    counts: dict[str, int] = {}
    for label, category in README_SECTIONS:
        selected = rows_for_category(rows, category)
        counts[label] = len(selected)
        text = replace_section_table(text, label, rendered_rows(selected, recent_keys))
        text = replace_toc_count(text, label, len(selected))

    readme_count = sum(counts.values())
    social_labels = {
        label for label, category in README_SECTIONS if category.startswith("Social platforms / ")
    }
    social_count = sum(count for label, count in counts.items() if label in social_labels)
    emerging_count = len(rows_for_category(rows, "Emerging"))
    agentic_count = sum(len(rows_for_category(rows, category)) for _, category in AGENTIC_SECTIONS)
    total_entries = readme_count + emerging_count + agentic_count

    text = replace_number_badge(text, "Emerging projects", "emerging", emerging_count)
    text = replace_number_badge(text, "Social platform entries", "social_platforms", social_count)
    text = replace_number_badge(text, "Agentic integrations", "agentic_integrations", agentic_count)
    text = replace_number_badge(text, "Catalogue entries", "catalogue_entries", total_entries)
    text = re.sub(
        r"(\[Emerging projects\]\(EMERGING\.md\) <sup>)\d+\s+projects?(</sup>)",
        rf"\g<1>{emerging_count} {count_label(emerging_count)}\2",
        text,
    )
    text = re.sub(
        r"(\[Agentic AI OSINT\]\(AGENTIC\.md\) <sup>)\d+\s+projects?(</sup>)",
        rf"\g<1>{agentic_count} {count_label(agentic_count)}\2",
        text,
    )
    text = replace_discord_empty_state(text, counts["Discord"])
    text = re.sub(r"(Complete repository database\]\(osint-repositories\.csv\) <sup>)\d+", rf"\g<1>{len(rows)}", text)
    return replace_update_date(text, date)


def render_emerging(
    text: str,
    rows: list[dict[str, str]],
    date: str,
    recent_keys: set[str],
) -> str:
    selected = rows_for_category(rows, "Emerging")
    text = replace_section_table(text, "Projects", rendered_rows(selected, recent_keys))
    text = replace_number_badge(text, "Emerging projects", "emerging_projects", len(selected))
    text = re.sub(r"(Complete repository database\]\(osint-repositories\.csv\) <sup>)\d+", rf"\g<1>{len(rows)}", text)
    return replace_update_date(text, date)


def render_agentic(
    text: str,
    rows: list[dict[str, str]],
    date: str,
    recent_keys: set[str],
) -> str:
    counts: dict[str, int] = {}
    for label, category in AGENTIC_SECTIONS:
        selected = rows_for_category(rows, category)
        counts[label] = len(selected)
        text = replace_section_table(text, label, rendered_rows(selected, recent_keys))
        text = replace_toc_count(text, label, len(selected))

    research_count = counts["Web research and source discovery"] + counts["Academic and structured research"]
    total = sum(counts.values())
    text = replace_number_badge(text, "OSINT integrations", "OSINT_integrations", counts["OSINT investigation and intelligence"])
    text = replace_number_badge(text, "Recon and CTI", "recon_and_CTI", counts["Reconnaissance and threat intelligence"])
    text = replace_number_badge(text, "Research integrations", "research_integrations", research_count)
    text = replace_number_badge(text, "Total projects", "total_projects", total)
    text = re.sub(r"(Complete repository database\]\(osint-repositories\.csv\) <sup>)\d+", rf"\g<1>{len(rows)}", text)
    return replace_update_date(text, date)


def render_monitoring(
    text: str,
    rows: list[dict[str, str]],
    date: str,
    recent_keys: set[str],
) -> str:
    return replace_update_date(text, date)


def timeline_row(row: dict[str, str]) -> str:
    project = f"[{markdown_text(row['Project'])}]({row['Repository']})"
    targets = "<br>".join(markdown_text(value) for value in split_values(row["Target"])) or "-"
    categories = (
        "<br>".join(markdown_text(value) for value in split_values(row["Categories"]))
        or "-"
    )
    return (
        f"| {project} "
        f"| {targets} "
        f"| {categories} "
        f"| {markdown_text(row['Description'])} "
        f"| {stars_as_int(row['Stars']):,} ⭐ |"
    )


def render_timeline(
    text: str,
    rows: list[dict[str, str]],
    date: str,
    recent_keys: set[str],
) -> str:
    del text, recent_keys
    dated: dict[str, list[dict[str, str]]] = {}
    legacy: list[dict[str, str]] = []
    for row in rows:
        added = row.get("Added", "")
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", added):
            dated.setdefault(added, []).append(row)
        else:
            legacy.append(row)

    dated_count = sum(len(group) for group in dated.values())
    badge_date = date.replace("-", "--")
    lines = [
        '<a id="top"></a>',
        "",
        '<div align="center">',
        "  <h1>OSINT Tools Radar Timeline</h1>",
        "  <p>A chronological view of projects added to the catalogue.</p>",
        "  <p>",
        (
            f'    <img alt="Dated additions: {dated_count}" '
            f'src="https://img.shields.io/badge/dated_additions-'
            f'{dated_count}-0969da?style=flat-square">'
        ),
        (
            f'    <img alt="Catalogue projects: {len(rows)}" '
            f'src="https://img.shields.io/badge/catalogue_projects-'
            f'{len(rows)}-8250df?style=flat-square">'
        ),
        (
            f'    <img alt="Last update: {date}" '
            f'src="https://img.shields.io/badge/last_update-'
            f'{badge_date}-1f883d?style=flat-square">'
        ),
        "  </p>",
        (
            '  <p><strong><a href="TIMELINE.md">Catalogue Timeline</a></strong> · '
            '<a href="README.md">OSINT Tools Radar</a> · '
            '<a href="EMERGING.md">Emerging Projects</a> · '
            '<a href="AGENTIC.md">Agentic AI OSINT</a> · '
            '<a href="osint-repositories.csv">Repository Database CSV</a></p>'
        ),
        "</div>",
        "",
        (
            "> Projects are grouped by the date stored in the canonical `Added` "
            "column. Newest catalogue entries appear first."
        ),
        "",
    ]

    for added in sorted(dated, reverse=True):
        group = sorted(dated[added], key=lambda row: row["Project"].casefold())
        count = len(group)
        lines.extend(
            [
                f"## {added} <sup>{count} {count_label(count)}</sup>",
                "",
                TIMELINE_HEADER,
                TIMELINE_ALIGNMENT,
                *(timeline_row(row) for row in group),
                "",
                '<p align="right"><a href="#top">Back to top ↑</a></p>',
                "",
            ]
        )

    legacy = sorted(legacy, key=lambda row: row["Project"].casefold())
    legacy_count = len(legacy)
    lines.extend(
        [
            "<details>",
            (
                "<summary><strong>Legacy entries without a catalogue date</strong> "
                f"<sup>{legacy_count} {count_label(legacy_count)}</sup></summary>"
            ),
            "",
            (
                "These projects predate reliable per-entry addition tracking. "
                "They are listed alphabetically without an invented date."
            ),
            "",
            TIMELINE_HEADER,
            TIMELINE_ALIGNMENT,
            *(timeline_row(row) for row in legacy),
            "",
            "</details>",
            "",
            '<p align="right"><a href="#top">Back to top ↑</a></p>',
            "",
        ]
    )
    return "\n".join(lines)


def rendered_documents() -> dict[Path, str]:
    _, rows = load_catalog()
    date = verified_date(rows)
    recent_keys = recent_repository_keys(rows, date)
    renderers = {
        ROOT / "README.md": render_readme,
        ROOT / "EMERGING.md": render_emerging,
        ROOT / "AGENTIC.md": render_agentic,
        ROOT / "TIMELINE.md": render_timeline,
        ROOT / ".radar" / "README.md": render_monitoring,
    }
    rendered: dict[Path, str] = {}
    for path, renderer in renderers.items():
        rendered[path] = renderer(
            path.read_text(encoding="utf-8"),
            rows,
            date,
            recent_keys,
        )
    return rendered


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Fail if generated documents differ")
    mode.add_argument("--write", action="store_true", help="Write generated documents")
    args = parser.parse_args()

    changed = 0
    for path, rendered in rendered_documents().items():
        current = path.read_text(encoding="utf-8")
        if current == rendered:
            continue
        changed += 1
        if args.write:
            path.write_text(rendered, encoding="utf-8")
            print(f"updated {path.relative_to(ROOT)}")
        else:
            diff = difflib.unified_diff(
                current.splitlines(),
                rendered.splitlines(),
                fromfile=str(path.relative_to(ROOT)),
                tofile=f"generated/{path.relative_to(ROOT)}",
                lineterm="",
            )
            print("\n".join(diff))

    if args.check and changed:
        print(f"{changed} generated document(s) are out of date", file=sys.stderr)
        return 1
    print("catalogue rendering is current" if not changed else f"updated {changed} document(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
