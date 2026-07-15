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
    README_SECTIONS,
    ROOT,
    TABLE_HEADER,
    format_markdown_row,
    load_catalog,
    rows_for_category,
    split_values,
    verified_date,
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
            if lines[index] == TABLE_HEADER
        ),
        None,
    )
    if header_index is None:
        raise ValueError(f"Cannot find table below section: {label}")

    first_row = header_index + 2
    last_row = first_row
    while last_row < len(lines) and lines[last_row].startswith("| ["):
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


def replace_verified_date(text: str, date: str) -> str:
    if not date:
        return text
    badge_date = date.replace("-", "--")
    text = re.sub(r'alt="Last verified: \d{4}-\d{2}-\d{2}"', f'alt="Last verified: {date}"', text)
    text = re.sub(r"(badge/last_verified-)\d{4}--\d{2}--\d{2}(-)", rf"\g<1>{badge_date}\2", text)
    text = re.sub(r"(last verified on \*\*)\d{4}-\d{2}-\d{2}(\*\*)", rf"\g<1>{date}\2", text, flags=re.IGNORECASE)
    text = re.sub(r"(captured on \*\*)\d{4}-\d{2}-\d{2}(\*\*)", rf"\g<1>{date}\2", text, flags=re.IGNORECASE)
    return text


def replace_discord_empty_state(text: str, count: int) -> str:
    note = "No implementation-bearing public repository from the reviewed sources passed the inclusion criteria."
    pattern = re.compile(
        rf"(## Discord <sup>\d+\s+projects?</sup>\n\n)(?:{re.escape(note)}\n\n)?(?={re.escape(TABLE_HEADER)})"
    )
    replacement = rf"\g<1>{note}\n\n" if count == 0 else r"\g<1>"
    return pattern.sub(replacement, text)


def render_readme(text: str, rows: list[dict[str, str]], date: str) -> str:
    counts: dict[str, int] = {}
    for label, category in README_SECTIONS:
        selected = rows_for_category(rows, category)
        counts[label] = len(selected)
        text = replace_section_table(text, label, [format_markdown_row(row) for row in selected])
        text = replace_toc_count(text, label, len(selected))

    readme_count = sum(counts.values())
    social_count = sum(count for label, count in counts.items() if label in {item[0] for item in README_SECTIONS[12:]})
    emerging_count = len(rows_for_category(rows, "Emerging"))
    agentic_count = sum(len(rows_for_category(rows, category)) for _, category in AGENTIC_SECTIONS)
    total_entries = readme_count + emerging_count + agentic_count

    text = replace_number_badge(text, "Open-source tools", "open--source_tools", readme_count)
    text = replace_number_badge(text, "Emerging projects", "emerging", emerging_count)
    text = replace_number_badge(text, "Social platform entries", "social_platforms", social_count)
    text = replace_number_badge(text, "Agentic integrations", "agentic_integrations", agentic_count)
    text = replace_number_badge(text, "Source repositories", "source_repositories", len(rows))
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
    return replace_verified_date(text, date)


def render_emerging(text: str, rows: list[dict[str, str]], date: str) -> str:
    selected = rows_for_category(rows, "Emerging")
    text = replace_section_table(text, "Projects", [format_markdown_row(row) for row in selected])
    text = replace_number_badge(text, "Emerging projects", "emerging_projects", len(selected))
    text = re.sub(r"(Complete repository database\]\(osint-repositories\.csv\) <sup>)\d+", rf"\g<1>{len(rows)}", text)
    return replace_verified_date(text, date)


def render_agentic(text: str, rows: list[dict[str, str]], date: str) -> str:
    counts: dict[str, int] = {}
    for label, category in AGENTIC_SECTIONS:
        selected = rows_for_category(rows, category)
        counts[label] = len(selected)
        text = replace_section_table(text, label, [format_markdown_row(row) for row in selected])
        text = replace_toc_count(text, label, len(selected))

    research_count = counts["Web research and source discovery"] + counts["Academic and structured research"]
    total = sum(counts.values())
    text = replace_number_badge(text, "OSINT integrations", "OSINT_integrations", counts["OSINT investigation and intelligence"])
    text = replace_number_badge(text, "Recon and CTI", "recon_and_CTI", counts["Reconnaissance and threat intelligence"])
    text = replace_number_badge(text, "Research integrations", "research_integrations", research_count)
    text = replace_number_badge(text, "Total projects", "total_projects", total)
    text = re.sub(r"(Complete repository database\]\(osint-repositories\.csv\) <sup>)\d+", rf"\g<1>{len(rows)}", text)
    return replace_verified_date(text, date)


def rendered_documents() -> dict[Path, str]:
    _, rows = load_catalog()
    date = verified_date(rows)
    renderers = {
        ROOT / "README.md": render_readme,
        ROOT / "EMERGING.md": render_emerging,
        ROOT / "AGENTIC.md": render_agentic,
    }
    rendered: dict[Path, str] = {}
    for path, renderer in renderers.items():
        rendered[path] = renderer(path.read_text(encoding="utf-8"), rows, date)
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
