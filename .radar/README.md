<a id="top"></a>

<div align="center">
  <h1>OSINT Tools Radar Monitoring</h1>
  <p>Automation and review guide for maintaining a verified catalogue of open-source OSINT tools and the public source-code repositories that contain their implementations.</p>
  <p>
    <img alt="Publication policy: review gated" src="https://img.shields.io/badge/publication-review_gated-bf8700?style=flat-square">
    <img alt="Metadata refresh: weekly" src="https://img.shields.io/badge/metadata-weekly-0969da?style=flat-square">
    <img alt="Candidate discovery: daily" src="https://img.shields.io/badge/discovery-daily-8250df?style=flat-square">
    <img alt="Third-party code execution: disabled" src="https://img.shields.io/badge/third--party_code-not_executed-1f883d?style=flat-square">
  </p>
  <p><strong><a href="../README.md">OSINT Tools Radar</a> · <a href="../EMERGING.md">Emerging Projects</a> · <a href="../AGENTIC.md">Agentic AI OSINT</a> · <a href="../osint-repositories.csv">Open-source Repository Database</a> · <a href="README.md">Monitoring</a></strong></p>
</div>

## Operating model

`../osint-repositories.csv` is the canonical, deduplicated repository database. The Markdown tables are generated views of accepted open-source tool and integration records. Candidate discovery is intentionally separate from publication.

```text
.radar/data/sources.csv -> discover_candidates.py -> .radar/data/candidates.csv -> human review
                                                                           -> osint-repositories.csv
GitHub API -> refresh_metadata.py -> osint-repositories.csv + .radar/data/snapshots.csv
osint-repositories.csv -> render_catalog.py -> README.md + EMERGING.md + AGENTIC.md
all catalogue files -> validate_catalog.py -> pass or fail
```

The monitor never clones, imports, installs, or executes code from catalogued repositories. It reads public repository metadata and registry records only.

## Files

| File | Purpose |
|---|---|
| `../osint-repositories.csv` | Canonical accepted open-source tool records and current repository metadata. |
| `data/candidates.csv` | Automatically discovered repositories awaiting an explicit decision. |
| `data/sources.csv` | Enabled discovery queries, providers, windows, and suggested classifications. |
| `data/snapshots.csv` | Point-in-time metadata used for trend and change reporting. |
| `../README.md` | Generated main and social-platform catalogue views. |
| `../EMERGING.md` | Generated early-stage project view. |
| `../AGENTIC.md` | Generated skills, plugins, MCP, and agent integration views. |

## Local commands

The scripts use the Python standard library and require Python 3.11 or newer.

Validate the canonical data and every generated table:

```bash
python3 -m py_compile .radar/scripts/*.py
python3 .radar/scripts/render_catalog.py --check
python3 .radar/scripts/validate_catalog.py
```

Refresh GitHub metadata and save a daily snapshot. A token is recommended for sufficient API quota:

```bash
GITHUB_TOKEN=github_token python3 .radar/scripts/refresh_metadata.py --write --snapshot --delay 0.1
python3 .radar/scripts/render_catalog.py --write
python3 .radar/scripts/validate_catalog.py
```

Run discovery against all enabled providers without changing files:

```bash
GITHUB_TOKEN=github_token python3 .radar/scripts/discover_candidates.py --lookback-days 14 --report discovery-report.md
```

Limit a diagnostic run to one configured source with `--source "GitHub OSINT topic"`, or repeat `--provider` to select one or more providers.

Persist newly found candidates:

```bash
GITHUB_TOKEN=github_token python3 .radar/scripts/discover_candidates.py --write --lookback-days 14 --report discovery-report.md
```

Generate a market-watch summary from candidates and snapshots:

```bash
python3 .radar/scripts/market_report.py --output market-watch.md
```

Reports are operational artifacts and are not committed by the scheduled workflows.

## Candidate review

Automated discovery provides suggestions, not final classifications. Before accepting a repository, verify that it:

- contains meaningful, publicly accessible source code;
- declares an open-source software license, or has its license status explicitly flagged for manual verification;
- has a practical OSINT, SOCMINT, GEOINT, recon, CTI, research, or evidence-analysis use case;
- is not merely a link collection, product landing page, prompt stub, or duplicate;
- has a neutral description supported by its implementation and documentation;
- is assigned to the most specific target and catalogue category;
- documents any claimed platform or agent compatibility.

Reject a candidate:

```bash
python3 .radar/scripts/review_candidate.py https://github.com/owner/repository --reject --notes "Not an implementation-bearing OSINT project"
```

Accept a standalone project:

```bash
python3 .radar/scripts/review_candidate.py https://github.com/owner/repository \
  --accept \
  --target Domain \
  --category Domain \
  --type Python \
  --description "Discovers public infrastructure associated with a domain."
python3 .radar/scripts/render_catalog.py --write
python3 .radar/scripts/validate_catalog.py
```

Accept a project into more than one generated view by repeating `--category`. Compatibility values use semicolons when both an investigated platform and an agent runtime apply.

## Discovery sources

`.radar/data/sources.csv` currently supports these adapters:

| Provider | Coverage | Authentication |
|---|---|---|
| GitHub Search | Topics and targeted repository queries | `GITHUB_TOKEN` recommended |
| GitLab Projects API | Public OSINT and recon project search | None for public results |
| Codeberg API | Public repository search | None for public results |
| Official MCP Registry | OSINT, recon, and research server search | None for public results |

Edit `.radar/data/sources.csv` to add, disable, or narrow a query. A new provider requires a corresponding adapter in `.radar/scripts/discover_candidates.py`. Keep queries focused enough to make manual review practical.

## Scheduled workflows

- `validate.yml` checks Python syntax, generated Markdown drift, CSV integrity, links between local files, duplicate repositories, table schemas, and category mappings on every push and pull request.
- `refresh.yml` runs weekly, refreshes GitHub metadata, appends a snapshot, regenerates all catalogue tables, opens or updates a review pull request, and creates a dated market-watch issue.
- `discover.yml` runs daily, scans configured sources, and opens or updates a review pull request when `.radar/data/candidates.csv` changes.

Scheduled workflows use the repository-provided `GITHUB_TOKEN`. The repository must allow GitHub Actions to create pull requests and grant workflows read and write permissions under **Settings -> Actions -> General**. GitHub may disable scheduled workflows in inactive public repositories, so the manual `workflow_dispatch` trigger remains available.

## Metadata and lifecycle policy

- `Last Update` records the latest repository push date reported by the hosting platform.
- `Stars` records an exact point-in-time value, never an approximation.
- `Verified` records the last successful metadata check.
- `License` records the declared open-source license; blank, missing, or `NOASSERTION` values require manual review and do not prove open-source status.
- Renamed or transferred GitHub repositories are replaced with the canonical API URL.
- Archived repositories remain visible and are marked as archived until a review decides whether historical value justifies retention.
- A confirmed `404` marks a repository as unavailable. Transient network and API failures do not change repository status.
- Descriptions, targets, categories, types, and compatibility labels are never overwritten by metadata refreshes.

## Recommended review rhythm

| Frequency | Review |
|---|---|
| Daily | Triage new high-confidence candidates and obvious false positives. |
| Weekly | Review metadata pull request, star movement, archival changes, and unavailable repositories. |
| Monthly | Audit low-activity projects, category balance, source quality, and repeated discovery noise. |
| Quarterly | Revisit inclusion rules, providers, target taxonomy, and agent compatibility labels. |

<p align="right"><a href="#top">Back to top ↑</a></p>
