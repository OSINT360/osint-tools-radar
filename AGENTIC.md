<a id="top"></a>

<div align="center">
  <h1>Agentic AI OSINT</h1>
  <p>A catalogue of open-source skills, plugins, MCP servers, and AI-agent integrations, linked to the public source-code repositories that contain their implementations.</p>
  <p>
    <a href="#osint-investigation-and-intelligence"><img alt="OSINT integrations: 51" src="https://img.shields.io/badge/OSINT_integrations-51-0969da?style=flat-square"></a>
    <a href="#reconnaissance-and-threat-intelligence"><img alt="Recon and CTI: 30" src="https://img.shields.io/badge/recon_and_CTI-30-d1242f?style=flat-square"></a>
    <a href="#web-research-and-source-discovery"><img alt="Research integrations: 43" src="https://img.shields.io/badge/research_integrations-43-8250df?style=flat-square"></a>
    <img alt="Total projects: 124" src="https://img.shields.io/badge/total_projects-124-bf8700?style=flat-square">
    <img alt="Last update: 2026-07-16" src="https://img.shields.io/badge/last_update-2026--07--16-1f883d?style=flat-square">
  </p>
  <p><strong><a href="AGENTIC.md">Agentic AI OSINT</a></strong> · <a href="README.md">OSINT Tools Radar</a> · <a href="EMERGING.md">Emerging Projects</a> · <a href="TIMELINE.md">Catalogue Timeline</a> · <a href="osint-repositories.csv">Repository Database CSV</a></p>
</div>

## About this catalogue

This file indexes open-source integrations that extend AI agents with investigative workflows or data access. It covers native agent skills, plugins, MCP servers, research systems, and mixed integrations with practical OSINT, reconnaissance, CTI, source-discovery, or evidence-analysis capabilities.

> [!IMPORTANT]
> Only implementation-bearing repositories with public source code are included. Prompt lists, link-only collections, closed services, commercial integrations without public code, and repository stubs are excluded.

> [!NOTE]
> This is a young and fast-moving ecosystem. Low or zero star counts do not disqualify a project when its repository already contains a meaningful implementation.

> <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> marks projects added to the catalogue within the last 14 days.

<a id="contents"></a>

## Contents

- [Compatibility labels](#compatibility-labels)
- [OSINT investigation and intelligence](#osint-investigation-and-intelligence) <sup>51 projects</sup>
- [Reconnaissance and threat intelligence](#reconnaissance-and-threat-intelligence) <sup>30 projects</sup>
- [Web research and source discovery](#web-research-and-source-discovery) <sup>33 projects</sup>
- [Academic and structured research](#academic-and-structured-research) <sup>10 projects</sup>
- [Catalogue timeline](TIMELINE.md)
- [Complete repository database](osint-repositories.csv) <sup>439 unique repositories</sup>

<a id="compatibility-labels"></a>

## Compatibility labels

- **Named product:** The repository explicitly targets or documents that product, such as Claude Code, Codex, Gemini CLI, OpenClaw, or Hermes Agent.
- **Multi-model:** The repository explicitly supports several model providers, agent runtimes, or AI clients.
- **Agent Skills standard:** The integration uses the portable `SKILL.md` or Agent Skills format without requiring one named model.
- **Model-agnostic (MCP):** The server uses MCP and can be connected to compatible clients; external APIs, credentials, and client-specific configuration may still be required.
- **Generic AI agents:** The repository provides agent instructions or tooling but does not claim a specific runtime.

> [!TIP]
> Compatibility describes the repository's documented integration surface. It does not imply that every feature was tested with every model or client.

---

<a id="osint-investigation-and-intelligence"></a>

## 🔎 OSINT investigation and intelligence <sup>51 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Agent Reach](https://github.com/Panniantong/Agent-Reach) | CLI + skill | Multi-model | Gives agents collection workflows for public content across multiple social and developer platforms. | 2026-02-24 | 2026-07-03 | 57,123 |
| [last30days](https://github.com/mvanhorn/last30days-skill) | Skill + plugin | Multi-model | Researches recent discussion across social platforms, communities, prediction markets, and the web. | 2026-01-23 | 2026-07-16 | 52,363 |
| [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Skill library | Multi-model | Provides reusable scientific research workflows and access patterns for public databases. | 2025-10-19 | 2026-07-15 | 31,020 |
| [Claude Skills](https://github.com/alirezarezvani/claude-skills) | Skills + plugins | Multi-model | Includes research, security, market analysis, compliance, and evidence-oriented agent skills. | 2025-10-19 | 2026-07-14 | 22,623 |
| [notebooklm-py](https://github.com/teng-lin/notebooklm-py) | Library + skill + MCP | Multi-model | Gives agents programmatic, source-grounded access to NotebookLM research workflows. | 2026-01-07 | 2026-07-16 | 17,852 |
| [ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | Research skill system | Multi-model | Orchestrates long-running research, cross-model review, experiments, and evidence capture. | 2026-03-10 | 2026-07-14 | 13,487 |
| [NotebookLM CLI and MCP](https://github.com/jacob-bd/notebooklm-mcp-cli) | CLI + skill + MCP | Multi-model | Connects AI agents to NotebookLM for cited source ingestion, querying, and synthesis. | 2025-12-23 | 2026-07-16 | 5,479 |
| [CTF Skills](https://github.com/ljagiello/ctf-skills) | Skill pack | Agent Skills standard | Supplies agent workflows for CTF categories including OSINT, forensics, and web investigation. | 2026-02-01 | 2026-07-10 | 2,726 |
| [Claude OSINT](https://github.com/elementalsouls/Claude-OSINT) | Skill pack | Claude Code | Adds structured external reconnaissance methods, dorks, validators, and reporting guidance. | 2026-04-26 | 2026-06-08 | 1,947 |
| [OpenOSINT](https://github.com/OpenOSINT/OpenOSINT) | Agent + CLI + MCP | Multi-model | Combines OSINT tools in an interactive agent, command-line interface, and MCP server. | 2026-05-06 | 2026-07-14 | 1,016 |
| [Claude Skills for Journalism](https://github.com/jamditis/claude-skills-journalism) | Skills + plugins | Claude Code | Covers source verification, public records, FOIA work, scraping, and newsroom research. | 2025-12-25 | 2026-07-16 | 326 |
| [CTI Expert](https://github.com/7onez/cti-expert) | Skill | Claude Code + Codex | Guides structured cyber threat intelligence and OSINT collection with confidence scoring. | 2026-04-06 | 2026-06-30 | 251 |
| [MCP Maigret](https://github.com/w0h1v/mcp-maigret) | MCP server | Model-agnostic (MCP) | Exposes Maigret username searches and public account discovery through MCP. | 2024-12-13 | 2026-01-27 | 250 |
| [xint](https://github.com/0xNyk/xint) | CLI + skill + MCP | X / Twitter; Multi-model | Searches, monitors, and exports public X data for agent-assisted investigations. | 2026-02-14 | 2026-07-16 | 216 |
| [OSINT Skill](https://github.com/smixs/osint-skill) | Skill | Multi-model | Runs phased people research with source grading, correlation, and report generation. | 2026-03-10 | 2026-03-10 | 82 |
| [OnionClaw](https://github.com/JacobJandon/OnionClaw) | Skill + CLI | Tor / .onion; OpenClaw | Adds Tor search, hidden-service retrieval, crawling, and export workflows to OpenClaw. | 2026-03-14 | 2026-05-28 | 61 |
| [MCP dnstwist](https://github.com/w0h1v/mcp-dnstwist) | MCP server | Model-agnostic (MCP) | Exposes look-alike domain discovery for phishing and impersonation investigations. | 2024-12-19 | 2025-03-03 | 51 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Huntkit](https://github.com/assafkip/huntkit) | Skills + MCP | Claude Code | Organizes cases, targets, findings, timelines, evidence hashes, and chain-of-custody records. | 2026-04-15 | 2026-07-06 | 46 |
| [OSINT AI](https://github.com/dkyazzentwatwa/osint-ai) | Skill pack | Generic AI agents | Provides guided people, domain, organization, breach, and evidence-analysis workflows. | 2026-02-27 | 2026-03-07 | 44 |
| [deep-recon](https://github.com/kvarnelis/deep-recon) | Skill | Claude Code + Obsidian | Coordinates multi-agent research and stores reconnaissance findings in Obsidian. | 2026-02-18 | 2026-02-21 | 41 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [European Parliament MCP](https://github.com/Hack23/European-Parliament-MCP-Server) | MCP server | Model-agnostic (MCP) | Provides agent access to European Parliament members, committees, votes, documents, and questions. | 2026-02-16 | 2026-07-16 | 20 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Sicry](https://github.com/JacobJandon/Sicry) | Python + MCP | Tor / .onion; MCP and AI agents | Checks Tor health, rotates identity, searches onion engines, fetches known services, and exposes optional agent-assisted analysis. | 2026-03-14 | 2026-05-28 | 16 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [YouTube Research MCP](https://github.com/coyaSONG/youtube-mcp-server) | MCP server | YouTube; Model-agnostic (MCP) | Exposes YouTube videos, channels, search results, comments, and transcripts through MCP. | 2025-03-31 | 2026-07-14 | 15 |
| [OSINT Agent Skills](https://github.com/frangelbarrera/osint-agent-skills) | Skills + MCP | Multi-model | Combines OSINT playbooks, agent instructions, report templates, and MCP tool definitions. | 2026-06-27 | 2026-07-01 | 12 |
| [OSINT AI Agent](https://github.com/sumba101/OSINT-AI-Agent) | Agent + skills | Claude | Orchestrates Holehe, Sherlock, and GHunt for person-focused investigations. | 2026-01-11 | 2026-01-11 | 7 |
| [Newsroom Extension](https://github.com/ehurrn/newsroom-extension) | Skill pack | Multi-model | Supports investigative journalism, FOIA work, corporate research, verification, and editorial review. | 2026-04-06 | 2026-06-22 | 6 |
| [Hermes OSINT Skill](https://github.com/mtjikuzu/hermes-osint-skill) | Skill | Hermes Agent | Structures company due diligence, background checks, vendor risk, and privacy review. | 2026-05-22 | 2026-05-22 | 6 |
| [OSINT Investigation](https://github.com/reichaves/osint-investigation) | Skill | Claude Code | Guides geolocation, source verification, entity profiling, and social-media investigation. | 2026-05-02 | 2026-05-03 | 6 |
| [Recon](https://github.com/g-baskin/recon) | Skill | Claude Code | Performs competitive intelligence across products, infrastructure, APIs, and communities. | 2026-02-25 | 2026-04-04 | 5 |
| [Outrider Recon](https://github.com/Ap6pack/outrider-recon) | Skills + MCP | Claude Code | Runs evidence-backed external reconnaissance with policy controls and optional MCP enrichment. | 2026-04-29 | 2026-07-15 | 4 |
| [Deep Research Ladder](https://github.com/hint-shu/deep-research) | Skills + plugin | Claude Code | Scales from fact checks to long-form research and OSINT entity reconnaissance. | 2026-04-17 | 2026-04-29 | 3 |
| [Geo Trajectory Analysis](https://github.com/eyal-weiss/geo-trajectory-analysis) | Skill | Claude | Applies a documented video-geolocation method to estimate missile launch origins. | 2026-03-23 | 2026-03-23 | 3 |
| [Infringement Information Collector](https://github.com/11murmur/infringement-information-collector) | Skill | Claude Code | Collects public leads about counterfeits, private servers, and piracy into auditable reports. | 2026-05-31 | 2026-06-01 | 2 |
| [OSINT Investigator](https://github.com/TNeagle/osint-investigator) | Skill | Claude Code | Coordinates multi-domain investigations, public-record research, geolocation, and intelligence reports. | 2026-03-18 | 2026-03-20 | 2 |
| [OpenProbe](https://github.com/hxd0818/openprobe) | Skill | OpenClaw | Investigates companies, competitors, supply chains, capital links, and key people. | 2026-04-12 | 2026-05-08 | 2 |
| [Email Finder Batch](https://github.com/yoitsyoung/email-finder-batch) | Skill | Claude Code | Coordinates public-source email discovery, pattern generation, and verification agents. | 2026-03-22 | 2026-03-22 | 2 |
| [Company Recon Skill](https://github.com/zoharbabin/company-recon-skill) | Skill | Claude Code | Identifies websites using a company's technology and classifies the resulting evidence. | 2026-03-04 | 2026-03-04 | 2 |
| [Agent Toolkit](https://github.com/000001000000/agent-toolkit) | Skill pack | Agent Skills standard | Includes an OSINT dorking workflow with search tooling and evaluation assets. | 2026-04-11 | 2026-06-08 | 1 |
| [OSINT Investigator for OpenClaw](https://github.com/Elyasuuuuu/osint-investigator) | Skill | OpenClaw | Correlates usernames, emails, domains, IPs, organizations, and public profile evidence. | 2026-03-16 | 2026-03-16 | 1 |
| [OSINT Social](https://github.com/guleguleguru/osint-social) | Skill | OpenClaw | Wraps broad username discovery with additional coverage for major Chinese platforms. | 2026-02-28 | 2026-02-28 | 1 |
| [Scout](https://github.com/indigokarasu/scout) | Skill pack | Agent Skills standard | Structures lawful people and company research with provenance, source tiers, and refresh workflows. | 2026-03-10 | 2026-07-16 | 1 |
| [Claude OSINT Plugin](https://github.com/lawriec/claude-osint-plugin) | Plugin + skills + MCP | Claude Code | Adds an intelligence-cycle methodology and configured search, media, archive, and analysis MCP servers. | 2026-04-09 | 2026-05-10 | 1 |
| [LinkedIn Recon Skill](https://github.com/Kewanvk/linkedin-recon-skill) | Skill | LinkedIn; Claude Code + Codex | Maps public hiring networks and organizational relationships from LinkedIn evidence. | 2026-05-08 | 2026-05-25 | 0 |
| [Bellingcat OSINT Toolkit Skills](https://github.com/CasualSecurityInc/Bellingcat-OSINT-Toolkit) | Skill pack | Agent Skills standard | Packages hundreds of investigation resources by geolocation, media, identity, transport, and conflict use case. | 2026-07-12 | 2026-07-12 | 0 |
| [Sherlock Skill](https://github.com/ImL1s/sherlock-skill) | Skill | Multi-model | Wraps Sherlock username searches with a portable skill and structured dossier output. | 2026-04-22 | 2026-04-22 | 0 |
| [Norteia Lead Recon](https://github.com/Luispitik/norteia-lead-recon) | Skill | Claude Code | Researches Spanish companies and leads through official open registers and geodata. | 2026-04-29 | 2026-04-29 | 0 |
| [OSINT Researcher](https://github.com/MrBridgeHQ/osint-researcher-claude) | Skill | Claude Code | Provides scoped OSINT, CTI, due diligence, and evidence-reporting procedures. | 2026-07-01 | 2026-07-06 | 0 |
| [Chinese OSINT Skills](https://github.com/zomin/chinese-osint-skills) | Skill pack | Multi-model | Supplies Chinese-platform research methods and scripts for cross-platform identity pivots. | 2026-04-30 | 2026-04-30 | 0 |
| [Geolocation Skill](https://github.com/zuocharles/geolocation-skill) | Skill | Agent Skills standard | Guides photo geolocation with visual clues, map queries, and source references. | 2026-03-30 | 2026-03-31 | 0 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [X Archive RAG](https://github.com/mameshivaa/x-archive-rag) | RAG system | X / Twitter; Generic AI agents | Indexes exported X data for local semantic search and retrieval-augmented analysis. | 2026-05-26 | 2026-06-18 | 0 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Telegram MCP TDLib](https://github.com/tolboy/telegram-mcp-tdlib) | MCP server | Telegram; Model-agnostic (MCP) | Exposes Telegram searches, chats, messages, and public content to MCP clients through TDLib. | 2026-07-04 | 2026-07-15 | 0 |

<a id="reconnaissance-and-threat-intelligence"></a>

## 🛡️ Reconnaissance and threat intelligence <sup>30 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [Anthropic Cybersecurity Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | Skill library | Multi-model | Packages extensive offensive, defensive, CTI, forensics, and reconnaissance procedures. | 2026-02-25 | 2026-06-26 | 25,629 |
| [HexStrike AI](https://github.com/0x4m4/hexstrike-ai) | MCP server | Model-agnostic (MCP) | Connects agents to a large collection of security and reconnaissance tools. | 2025-07-10 | 2026-04-27 | 10,347 |
| [Claude Bug Bounty](https://github.com/shuvonsec/claude-bug-bounty) | Skills + agents | Claude Code | Organizes authorized bug-bounty reconnaissance, testing, validation, and reporting. | 2026-03-08 | 2026-07-09 | 3,974 |
| [Claude BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | Skill pack | Claude Code | Adds structured web reconnaissance and vulnerability-hunting methodology. | 2026-05-05 | 2026-07-01 | 2,978 |
| [Claude Red](https://github.com/SnailSploit/Claude-Red) | Skill pack | Claude Code | Provides red-team and security research playbooks for Claude-based workflows. | 2026-03-04 | 2026-05-08 | 2,706 |
| [VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | Agent + skills + MCP | Multi-model | Orchestrates information gathering, vulnerability analysis, exploitation, and reporting. | 2026-04-18 | 2026-07-10 | 2,101 |
| [Pentest AI Agents](https://github.com/0xSteph/pentest-ai-agents) | Agent pack | Claude Code | Supplies specialized subagents for recon analysis, exploit research, detection, and reporting. | 2026-03-28 | 2026-06-19 | 2,004 |
| [Hack Skills](https://github.com/yaklang/hack-skills) | Skill library | Agent Skills standard | Covers reconnaissance, web and network security, forensics, reversing, and authorized research. | 2026-04-07 | 2026-06-16 | 1,380 |
| [Pentest AI](https://github.com/0xSteph/pentest-ai) | CLI + MCP | Multi-model | Exposes security tools, specialist agents, and deterministic probes through CLI and MCP. | 2026-04-04 | 2026-06-30 | 1,297 |
| [CyberStrike](https://github.com/CyberStrikeus/CyberStrike) | Agent + MCP | Multi-model | Runs agent-assisted offensive security with recon, testing, and evidence workflows. | 2026-02-14 | 2026-07-16 | 1,218 |
| [CVE MCP Server](https://github.com/mukul975/cve-mcp-server) | MCP server | Model-agnostic (MCP) | Correlates CVE, EPSS, KEV, Shodan, VirusTotal, and related security intelligence. | 2026-04-14 | 2026-06-22 | 1,085 |
| [Hackingtool Plugin](https://github.com/AKCodez/hackingtool-plugin) | Plugin + skill | Claude Code | Makes a large catalogue of pentest and OSINT tools discoverable and runnable by Claude. | 2026-04-23 | 2026-04-25 | 852 |
| [Recon Skills](https://github.com/uphiago/recon-skills) | Skill pack | Agent Skills standard | Provides field-oriented recon, dorking, secret discovery, asset mapping, and testing playbooks. | 2026-06-24 | 2026-07-08 | 756 |
| [MCP Security Hub](https://github.com/FuzzingLabs/mcp-security-hub) | MCP collection | Model-agnostic (MCP) | Exposes containerized security tools for recon, threat intelligence, code, and binary analysis. | 2026-01-06 | 2026-04-08 | 732 |
| [Transilience Community Tools](https://github.com/transilienceai/communitytools) | Skills + agents | Claude Code | Covers security reconnaissance, bug bounty, AI threat testing, validation, and reporting. | 2025-11-21 | 2026-07-13 | 413 |
| [Darknet MCP Server](https://github.com/badchars/darknet-mcp-server) | MCP server | Tor / .onion; Model-agnostic (MCP) | Unifies dark-web search, breach, ransomware, malware, and blockchain intelligence tools for MCP clients. | 2026-06-23 | 2026-06-24 | 221 |
| [Reversecore MCP](https://github.com/sjkim1127/Reversecore_MCP) | MCP server | Model-agnostic (MCP) | Connects agents to reverse engineering, malware, forensics, and vulnerability research tools. | 2025-11-10 | 2026-07-16 | 182 |
| [Shodan MCP](https://github.com/w0h1v/mcp-shodan) | MCP server | Model-agnostic (MCP) | Provides device search, IP reconnaissance, DNS, CPE, and CVE intelligence. | 2024-12-12 | 2026-03-31 | 144 |
| [VirusTotal MCP](https://github.com/w0h1v/mcp-virustotal) | MCP server | Model-agnostic (MCP) | Queries files, URLs, domains, IPs, and related security-analysis records. | 2024-12-13 | 2026-05-24 | 138 |
| [ThreatSwarm](https://github.com/mukul975/Threatswarm) | Plugin + agents | Claude Code | Coordinates scope-aware agents across recon, exploitation, DFIR, and final reporting. | 2026-04-29 | 2026-04-29 | 59 |
| [ZettelForge](https://github.com/ThreatRecall/zettelforge) | CTI system + MCP | Multi-model | Extracts IOCs and threat entities into a local STIX knowledge graph with agent access. | 2026-04-06 | 2026-07-10 | 55 |
| [OSINT MCP Server](https://github.com/badchars/osint-mcp-server) | MCP server | Model-agnostic (MCP) | Correlates infrastructure and threat data from Shodan, Censys, DNS, BGP, archives, and more. | 2026-03-17 | 2026-03-17 | 36 |
| [Shodan MCP by Vorota](https://github.com/Vorota-ai/shodan-mcp) | MCP server | Model-agnostic (MCP) | Adds passive asset discovery, DNS analysis, and vulnerability intelligence from Shodan. | 2026-02-12 | 2026-02-12 | 21 |
| [Claude Code Pentest](https://github.com/Orizon-eu/claude-code-pentest) | Skill pack | Claude Code | Automates the authorized pentest lifecycle from initial recon to exploit-chain reports. | 2026-03-11 | 2026-03-11 | 19 |
| [Malware Sandbox MCP](https://github.com/mukul975/Malware-Sandbox-mcp) | MCP server | Model-agnostic (MCP) | Normalizes malware sandbox verdicts, IOCs, artifacts, and ATT&CK mappings. | 2026-06-11 | 2026-06-11 | 14 |
| [MISP MCP](https://github.com/MISP/misp-mcp) | MCP server | Model-agnostic (MCP) | Provides read-only access to MISP threat intelligence events and attributes. | 2026-04-01 | 2026-04-05 | 8 |
| [Offensive Recon](https://github.com/mahuttha/offensive-recon) | Plugin + skills | Claude Code | Packages multi-phase reconnaissance skills and agents around common security tools. | 2026-03-01 | 2026-03-01 | 4 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [LeakIX MCP](https://github.com/LeakIX/leakix-mcp) | MCP server | Model-agnostic (MCP) | Exposes LeakIX searches for internet services, leaks, domains, and IP addresses through MCP. | 2026-01-27 | 2026-07-14 | 2 |
| [OSINT MCP Gateway](https://github.com/bonetrees/osint-mcp-gateway) | MCP server | Model-agnostic (MCP) | Routes agent queries across VirusTotal, Shodan, DNS, WHOIS, RIPEstat, and OTX. | 2025-11-23 | 2026-06-10 | 0 |
| [Bounty Recon Pro](https://github.com/synicalkid/bounty-recon-pro) | Skill | Claude Code | Runs scoped passive OSINT and active bug-bounty recon with evidence-oriented reports. | 2026-07-11 | 2026-07-11 | 0 |

<a id="web-research-and-source-discovery"></a>

## 🌐 Web research and source discovery <sup>33 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Browser Use](https://github.com/browser-use/browser-use) | Agent framework | Multi-model | Lets AI agents navigate websites, interact with pages, and extract information. | 2024-10-31 | 2026-07-14 | 105,083 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Scrapling](https://github.com/D4Vinci/Scrapling) | Python | Agent Skills standard; Model-agnostic (MCP) | Provides adaptive web scraping, crawling, browser automation, and structured extraction. | 2024-10-13 | 2026-07-15 | 69,773 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [TrendRadar](https://github.com/sansan0/TrendRadar) | Monitoring platform + MCP | Model-agnostic (MCP) | Monitors news and RSS sources, tracks trends, stores history, and exposes MCP access. | 2025-04-28 | 2026-07-08 | 60,612 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Vane](https://github.com/ItzCrazyKns/Vane) | Research agent | Multi-model | Provides a self-hosted research interface that answers questions with linked sources. | 2024-04-09 | 2026-04-11 | 35,682 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [GPT Researcher](https://github.com/assafelovic/gpt-researcher) | Research agent | Multi-model | Runs multi-agent web research and produces source-grounded reports with citations. | 2023-05-12 | 2026-07-14 | 28,343 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Stagehand](https://github.com/browserbase/stagehand) | Agent SDK | Multi-model | Provides an SDK for agent-driven browser automation and page extraction. | 2024-03-24 | 2026-07-16 | 23,530 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [deep-research](https://github.com/dzhng/deep-research) | Research agent | Multi-model | Runs iterative web searches, evaluates findings, and builds source-grounded research answers. | 2025-02-04 | 2026-04-11 | 19,367 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Open Deep Research](https://github.com/langchain-ai/open_deep_research) | Research agent | Multi-model | Implements a configurable deep-research agent with pluggable search and model providers. | 2024-11-20 | 2026-07-15 | 12,026 |
| [Firecrawl MCP Server](https://github.com/firecrawl/firecrawl-mcp-server) | MCP server | Model-agnostic (MCP) | Gives agents web search, crawling, scraping, extraction, and structured research tools. | 2024-12-06 | 2026-07-08 | 6,969 |
| [Exa MCP Server](https://github.com/exa-labs/exa-mcp-server) | MCP server | Model-agnostic (MCP) | Provides semantic web search, content retrieval, and research discovery through Exa. | 2024-11-27 | 2026-07-15 | 4,729 |
| [Deep Research](https://github.com/u14app/deep-research) | Research system + MCP | Multi-model | Runs iterative web research and synthesis with configurable models and MCP access. | 2025-02-22 | 2026-06-18 | 4,634 |
| [Bright Data MCP](https://github.com/brightdata/brightdata-mcp) | MCP server | Model-agnostic (MCP) | Connects agents to search, browsing, scraping, and public web datasets. | 2025-04-15 | 2026-06-14 | 2,501 |
| [Tavily MCP](https://github.com/tavily-ai/tavily-mcp) | MCP server | Model-agnostic (MCP) | Exposes search, extraction, crawling, mapping, and research functions from Tavily. | 2025-01-27 | 2026-07-10 | 2,223 |
| [Apify MCP Server](https://github.com/apify/apify-mcp-server) | MCP server | Model-agnostic (MCP) | Makes Apify Actors and public web data collection available to compatible agents. | 2025-01-02 | 2026-07-16 | 1,975 |
| [Brave Search MCP Server](https://github.com/brave/brave-search-mcp-server) | MCP server | Model-agnostic (MCP) | Adds Brave web, news, image, video, and local search to MCP clients. | 2025-06-12 | 2026-06-24 | 1,304 |
| [De-Anthropocentric Research Engine](https://github.com/yogsoth-ai/de-anthropocentric-research-engine) | Research skill system | Multi-model | Organizes autonomous research into composable campaigns, strategies, tactics, and procedures. | 2026-02-10 | 2026-07-09 | 386 |
| [Kindly Web Search MCP](https://github.com/Shelpuk-AI-Technology-Consulting/kindly-web-search-mcp-server) | MCP server | Model-agnostic (MCP) | Aggregates web search, extraction, crawling, and browser automation for many clients. | 2026-01-02 | 2026-07-14 | 358 |
| [NotebookLM Skill](https://github.com/claude-world/notebooklm-skill) | Skill + MCP | Claude Code | Uses NotebookLM for source-grounded research, synthesis, and content preparation. | 2026-03-13 | 2026-03-24 | 355 |
| [MCP Omnisearch](https://github.com/spences10/mcp-omnisearch) | MCP server | Model-agnostic (MCP) | Combines multiple search, AI search, and content-processing providers behind MCP. | 2025-03-08 | 2026-07-02 | 333 |
| [Google Research MCP](https://github.com/mixelpixx/Google-Research-MCP) | MCP server | Model-agnostic (MCP) | Uses Google Search and browser automation for multi-step cited research. | 2024-12-19 | 2026-06-27 | 249 |
| [Reddit Research MCP](https://github.com/king-of-the-grackles/reddit-research-mcp) | MCP server | Reddit; Model-agnostic (MCP) | Supports structured Reddit discovery, thread collection, and community research. | 2025-08-12 | 2026-07-02 | 219 |
| [Octagon MCP Server](https://github.com/OctagonAI/octagon-mcp-server) | MCP server | Model-agnostic (MCP) | Provides public company, market, investor, private-market, and crypto research data. | 2025-03-12 | 2026-07-09 | 143 |
| [RivalSearch MCP](https://github.com/damionrashford/RivalSearchMCP) | MCP server | Model-agnostic (MCP) | Unifies web, social, news, academic, and entity-search sources behind MCP. | 2025-08-03 | 2026-05-31 | 114 |
| [Deep Research MCP](https://github.com/pminervini/deep-research-mcp) | MCP server | Multi-model | Connects several deep-research agents and model providers through one MCP interface. | 2025-08-07 | 2026-06-10 | 93 |
| [Deep Web Research MCP](https://github.com/qpd-v/mcp-DEEPwebresearch) | MCP server | Model-agnostic (MCP) | Coordinates recursive web search and page analysis for deeper topic coverage. | 2025-01-13 | 2025-03-05 | 86 |
| [Agent Search](https://github.com/brcrusoe72/agent-search) | MCP server | Model-agnostic (MCP) | Provides privacy-oriented search and browser retrieval for AI agents. | 2026-02-18 | 2026-07-07 | 58 |
| [OpenRouter Deep Research MCP](https://github.com/wheattoast11/openrouter-deep-research-mcp) | MCP server | Model-agnostic (MCP) | Orchestrates parallel research agents and consensus-backed synthesis through OpenRouter. | 2025-03-28 | 2026-03-04 | 54 |
| [Web Researcher MCP](https://github.com/zoharbabin/web-researcher-mcp) | MCP server | Model-agnostic (MCP) | Searches the web, extracts sources, and produces citation-aware research results. | 2026-05-18 | 2026-07-16 | 42 |
| [Helium MCP](https://github.com/connerlambden/helium-mcp) | MCP server | Model-agnostic (MCP) | Provides news discovery, bias scoring, market data, and multi-source synthesis. | 2026-04-10 | 2026-07-06 | 11 |
| [GiaSip Skills](https://github.com/GiaSip/giasip-skills) | Skills + plugin | Claude Code + Codex | Provides quick recon, fact-checking, research orchestration, and multi-model dispatch. | 2026-05-30 | 2026-07-15 | 11 |
| [Web Multi Search](https://github.com/soxoj/web-multi-search-skill) | Skill + script | OpenClaw | Searches several web engines in parallel and exports deduplicated results. | 2026-02-08 | 2026-02-08 | 7 |
| [Digital Research Skills](https://github.com/smarks26/digital-research-skills) | Research skill system | Multi-model | Plans evidence-driven research waves for OSINT, due diligence, trends, and long-form analysis. | 2026-05-29 | 2026-05-16 | 2 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Internet Archive MCP](https://github.com/cyanheads/internet-archive-mcp-server) | MCP server | Model-agnostic (MCP) | Provides agent access to Internet Archive search, metadata, files, and preserved resources. | 2026-06-05 | 2026-07-03 | 1 |

<a id="academic-and-structured-research"></a>

## 🎓 Academic and structured research <sup>10 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Agentset](https://github.com/agentset-ai/agentset) | Research system + MCP | Model-agnostic (MCP) | Provides document ingestion, agentic search, ranking, citations, RAG, and MCP access. | 2025-03-10 | 2026-07-04 | 2,031 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [PDF Reader MCP](https://github.com/SylphxAI/pdf-reader-mcp) | MCP server + CLI | Model-agnostic (MCP) | Analyzes PDFs through MCP while retaining page references, visual crops, and OCR provenance. | 2025-04-04 | 2026-07-16 | 827 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Docling MCP](https://github.com/docling-project/docling-mcp) | MCP server | Model-agnostic (MCP) | Exposes document conversion and structured extraction from files and URLs through MCP. | 2025-03-14 | 2026-07-16 | 686 |
| [Simple PubMed MCP](https://github.com/andybrandt/mcp-simple-pubmed) | MCP server | Model-agnostic (MCP) | Searches PubMed and retrieves biomedical article metadata and abstracts. | 2024-12-11 | 2026-03-19 | 169 |
| [mcp.science](https://github.com/pathintegral-institute/mcp.science) | MCP server | Model-agnostic (MCP) | Connects agents to scientific literature search and research data services. | 2025-03-27 | 2025-09-02 | 145 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Data Commons Agent Toolkit](https://github.com/datacommonsorg/agent-toolkit) | MCP toolkit | Model-agnostic (MCP) | Connects agents and MCP clients to the public Data Commons knowledge graph. | 2025-06-26 | 2026-07-15 | 137 |
| [Academia MCP](https://github.com/IlyaGusev/academia_mcp) | MCP server | Model-agnostic (MCP) | Searches academic sources and retrieves papers for agent-assisted literature research. | 2025-01-24 | 2026-01-24 | 90 |
| [ZotPilot](https://github.com/xunhe730/ZotPilot) | Skill + MCP | Model-agnostic (MCP) | Connects Zotero collections to source-grounded research and agent workflows. | 2026-03-16 | 2026-06-16 | 67 |
| [OpenAlex Research MCP](https://github.com/oksure/openalex-research-mcp) | MCP server | Model-agnostic (MCP) | Queries OpenAlex works, authors, institutions, concepts, and citation relationships. | 2025-10-05 | 2026-06-22 | 36 |
| [Semantic Scholar Skills](https://github.com/zongmin-yu/semantic-scholar-skills) | Skills + MCP | Claude Code | Supports literature discovery, citation expansion, and structured Semantic Scholar research. | 2026-03-10 | 2026-03-16 | 19 |

---

<p align="right"><a href="#top">Back to top ↑</a></p>
