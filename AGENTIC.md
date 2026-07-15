<a id="top"></a>

<div align="center">
  <h1>Agentic AI OSINT</h1>
  <p>An automatically updated radar of open-source skills, plugins, MCP servers, and AI agent integrations for efficiently monitoring the agentic OSINT, research, reconnaissance, and threat-intelligence market.</p>
  <p>
    <a href="#osint-investigation-and-intelligence"><img alt="OSINT integrations: 48" src="https://img.shields.io/badge/OSINT_integrations-48-0969da?style=flat-square"></a>
    <a href="#reconnaissance-and-threat-intelligence"><img alt="Recon and CTI: 30" src="https://img.shields.io/badge/recon_and_CTI-30-d1242f?style=flat-square"></a>
    <a href="#web-research-and-source-discovery"><img alt="Research integrations: 30" src="https://img.shields.io/badge/research_integrations-30-8250df?style=flat-square"></a>
    <img alt="Total projects: 108" src="https://img.shields.io/badge/total_projects-108-bf8700?style=flat-square">
    <img alt="Last verified: 2026-07-15" src="https://img.shields.io/badge/last_verified-2026--07--15-1f883d?style=flat-square">
  </p>
  <p><strong><a href="README.md">OSINT Tools Radar</a> · <a href="EMERGING.md">Emerging Projects</a> · <a href="AGENTIC.md">Agentic AI OSINT</a> · <a href="osint-repositories.csv">Repository Database</a></strong></p>
</div>

## About this catalogue

This file tracks public repositories that extend AI agents with investigative workflows or data access. Automated metadata refreshes and review-gated discovery expose new integrations and changing adoption signals without publishing unverified candidates. It covers native agent skills, plugins, MCP servers, research systems, and mixed integrations with practical OSINT, recon, CTI, source discovery, or evidence-analysis capabilities.

> [!IMPORTANT]
> Only repositories with public source code and identifiable implementation are included. Prompt lists, link-only collections, closed services, and repository stubs are excluded.

> [!NOTE]
> This is a young and fast-moving ecosystem. Low or zero star counts do not disqualify a project when its repository already contains a meaningful implementation. Metadata and compatibility claims were last verified on **2026-07-15**.

<a id="contents"></a>

## Contents

- [Compatibility labels](#compatibility-labels)
- [OSINT investigation and intelligence](#osint-investigation-and-intelligence) <sup>48 projects</sup>
- [Reconnaissance and threat intelligence](#reconnaissance-and-threat-intelligence) <sup>30 projects</sup>
- [Web research and source discovery](#web-research-and-source-discovery) <sup>24 projects</sup>
- [Academic and structured research](#academic-and-structured-research) <sup>6 projects</sup>
- [Metadata conventions](#metadata-conventions)
- [Complete CSV database](osint-repositories.csv) <sup>394 unique repositories</sup>

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

## 🔎 OSINT investigation and intelligence <sup>48 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [last30days](https://github.com/mvanhorn/last30days-skill) | Skill + plugin | Multi-model | Researches recent discussion across social platforms, communities, prediction markets, and the web. | 2026-01-23 | 2026-07-13 | 52,226 |
| [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Skill library | Multi-model | Provides reusable scientific research workflows and access patterns for public databases. | 2025-10-19 | 2026-07-14 | 30,916 |
| [Claude Skills](https://github.com/alirezarezvani/claude-skills) | Skills + plugins | Multi-model | Includes research, security, market analysis, compliance, and evidence-oriented agent skills. | 2025-10-19 | 2026-07-14 | 22,588 |
| [notebooklm-py](https://github.com/teng-lin/notebooklm-py) | Library + skill + MCP | Multi-model | Gives agents programmatic, source-grounded access to NotebookLM research workflows. | 2026-01-07 | 2026-07-15 | 17,786 |
| [ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | Research skill system | Multi-model | Orchestrates long-running research, cross-model review, experiments, and evidence capture. | 2026-03-10 | 2026-07-14 | 13,400 |
| [NotebookLM CLI and MCP](https://github.com/jacob-bd/notebooklm-mcp-cli) | CLI + skill + MCP | Multi-model | Connects AI agents to NotebookLM for cited source ingestion, querying, and synthesis. | 2025-12-23 | 2026-07-15 | 5,461 |
| [CTF Skills](https://github.com/ljagiello/ctf-skills) | Skill pack | Agent Skills standard | Supplies agent workflows for CTF categories including OSINT, forensics, and web investigation. | 2026-02-01 | 2026-07-10 | 2,715 |
| [Claude OSINT](https://github.com/elementalsouls/Claude-OSINT) | Skill pack | Claude Code | Adds structured external reconnaissance methods, dorks, validators, and reporting guidance. | 2026-04-26 | 2026-06-08 | 1,943 |
| [OpenOSINT](https://github.com/OpenOSINT/OpenOSINT) | Agent + CLI + MCP | Multi-model | Combines OSINT tools in an interactive agent, command-line interface, and MCP server. | 2026-05-06 | 2026-07-14 | 983 |
| [Claude Skills for Journalism](https://github.com/jamditis/claude-skills-journalism) | Skills + plugins | Claude Code | Covers source verification, public records, FOIA work, scraping, and newsroom research. | 2025-12-25 | 2026-07-14 | 324 |
| [MCP Maigret](https://github.com/w0h1v/mcp-maigret) | MCP server | Model-agnostic (MCP) | Exposes Maigret username searches and public account discovery through MCP. | 2024-12-13 | 2026-01-27 | 250 |
| [CTI Expert](https://github.com/7onez/cti-expert) | Skill | Claude Code + Codex | Guides structured cyber threat intelligence and OSINT collection with confidence scoring. | 2026-04-06 | 2026-06-30 | 249 |
| [OSINT Tools MCP Server](https://github.com/frishtik/osint-tools-mcp-server) | MCP server | Model-agnostic (MCP) | Wraps several public OSINT utilities for use by MCP-compatible assistants. | 2025-08-07 | 2025-08-07 | 220 |
| [xint](https://github.com/0xNyk/xint) | CLI + skill + MCP | X / Twitter; Multi-model | Searches, monitors, and exports public X data for agent-assisted investigations. | 2026-02-14 | 2026-07-04 | 215 |
| [OSINT360 GPT](https://github.com/oryon-osint/OSINT360-GPT) | Custom GPT configuration | ChatGPT | Provides a public OSINT-oriented custom GPT configuration and supporting instructions. | 2024-05-23 | 2024-05-23 | 107 |
| [OSINT Skill](https://github.com/smixs/osint-skill) | Skill | Multi-model | Runs phased people research with source grading, correlation, and report generation. | 2026-03-10 | 2026-03-10 | 80 |
| [OnionClaw](https://github.com/JacobJandon/OnionClaw) | Skill + CLI | OpenClaw | Adds Tor search, hidden-service retrieval, crawling, and export workflows to OpenClaw. | 2026-03-14 | 2026-07-01 | 62 |
| [MCP dnstwist](https://github.com/w0h1v/mcp-dnstwist) | MCP server | Model-agnostic (MCP) | Exposes look-alike domain discovery for phishing and impersonation investigations. | 2024-12-19 | 2025-03-03 | 51 |
| [OSINT AI](https://github.com/dkyazzentwatwa/osint-ai) | Skill pack | Generic AI agents | Provides guided people, domain, organization, breach, and evidence-analysis workflows. | 2026-02-27 | 2026-03-07 | 44 |
| [MCP OSINT Server](https://github.com/himanshusanecha/mcp-osint-server) | MCP server | Model-agnostic (MCP) | Offers MCP tools for public intelligence lookups and investigative pivots. | 2025-03-12 | 2025-03-12 | 44 |
| [deep-recon](https://github.com/kvarnelis/deep-recon) | Skill | Claude Code + Obsidian | Coordinates multi-agent research and stores reconnaissance findings in Obsidian. | 2026-02-18 | 2026-02-21 | 40 |
| [OSINT Agent Skills](https://github.com/frangelbarrera/osint-agent-skills) | Skills + MCP | Multi-model | Combines OSINT playbooks, agent instructions, report templates, and MCP tool definitions. | 2026-06-27 | 2026-07-01 | 11 |
| [OSINT AI Agent](https://github.com/sumba101/OSINT-AI-Agent) | Agent + skills | Claude | Orchestrates Holehe, Sherlock, and GHunt for person-focused investigations. | 2026-01-11 | 2026-01-11 | 7 |
| [Newsroom Extension](https://github.com/ehurrn/newsroom-extension) | Skill pack | Multi-model | Supports investigative journalism, FOIA work, corporate research, verification, and editorial review. | 2026-04-06 | 2026-06-22 | 6 |
| [Hermes OSINT Skill](https://github.com/mtjikuzu/hermes-osint-skill) | Skill | Hermes Agent | Structures company due diligence, background checks, vendor risk, and privacy review. | 2026-05-22 | 2026-05-22 | 6 |
| [OSINT Investigation](https://github.com/reichaves/osint-investigation) | Skill | Claude Code | Guides geolocation, source verification, entity profiling, and social-media investigation. | 2026-05-02 | 2026-05-03 | 6 |
| [Recon](https://github.com/g-baskin/recon) | Skill | Claude Code | Performs competitive intelligence across products, infrastructure, APIs, and communities. | 2026-02-25 | 2026-04-04 | 5 |
| [Outrider Recon](https://github.com/Ap6pack/outrider-recon) | Skills + MCP | Claude Code | Runs evidence-backed external reconnaissance with policy controls and optional MCP enrichment. | 2026-04-29 | 2026-07-14 | 4 |
| [Deep Research Ladder](https://github.com/hint-shu/deep-research) | Skills + plugin | Claude Code | Scales from fact checks to long-form research and OSINT entity reconnaissance. | 2026-04-17 | 2026-05-03 | 3 |
| [Geo Trajectory Analysis](https://github.com/eyal-weiss/geo-trajectory-analysis) | Skill | Claude | Applies a documented video-geolocation method to estimate missile launch origins. | 2026-03-23 | 2026-03-23 | 3 |
| [Infringement Information Collector](https://github.com/11murmur/infringement-information-collector) | Skill | Claude Code | Collects public leads about counterfeits, private servers, and piracy into auditable reports. | 2026-05-31 | 2026-06-01 | 2 |
| [OSINT Investigator](https://github.com/TNeagle/osint-investigator) | Skill | Claude Code | Coordinates multi-domain investigations, public-record research, geolocation, and intelligence reports. | 2026-03-18 | 2026-03-20 | 2 |
| [OpenProbe](https://github.com/hxd0818/openprobe) | Skill | OpenClaw | Investigates companies, competitors, supply chains, capital links, and key people. | 2026-04-12 | 2026-05-08 | 2 |
| [Email Finder Batch](https://github.com/yoitsyoung/email-finder-batch) | Skill | Claude Code | Coordinates public-source email discovery, pattern generation, and verification agents. | 2026-03-22 | 2026-03-22 | 2 |
| [Company Recon Skill](https://github.com/zoharbabin/company-recon-skill) | Skill | Claude Code | Identifies websites using a company's technology and classifies the resulting evidence. | 2026-03-04 | 2026-03-04 | 2 |
| [Agent Toolkit](https://github.com/000001000000/agent-toolkit) | Skill pack | Agent Skills standard | Includes an OSINT dorking workflow with search tooling and evaluation assets. | 2026-04-11 | 2026-06-08 | 1 |
| [Maltego MCP](https://github.com/schwarztim/sec-maltego-mcp) | MCP server (archived) | Model-agnostic (MCP) | Exposes Maltego transforms, entities, graph operations, and machines through MCP. | 2026-01-29 | 2026-05-09 | 1 |
| [OSINT Investigator for OpenClaw](https://github.com/Elyasuuuuu/osint-investigator) | Skill | OpenClaw | Correlates usernames, emails, domains, IPs, organizations, and public profile evidence. | 2026-03-16 | 2026-03-16 | 1 |
| [OSINT Social](https://github.com/guleguleguru/osint-social) | Skill | OpenClaw | Wraps broad username discovery with additional coverage for major Chinese platforms. | 2026-02-28 | 2026-02-28 | 1 |
| [Scout](https://github.com/indigokarasu/scout) | Skill pack | Agent Skills standard | Structures lawful people and company research with provenance, source tiers, and refresh workflows. | 2026-03-10 | 2026-07-07 | 1 |
| [LinkedIn Recon Skill](https://github.com/Kewanvk/linkedin-recon-skill) | Skill | LinkedIn; Claude Code + Codex | Maps public hiring networks and organizational relationships from LinkedIn evidence. | 2026-05-08 | 2026-05-25 | 0 |
| [Bellingcat OSINT Toolkit Skills](https://github.com/CasualSecurityInc/Bellingcat-OSINT-Toolkit) | Skill pack | Agent Skills standard | Packages hundreds of investigation resources by geolocation, media, identity, transport, and conflict use case. | 2026-07-12 | 2026-07-12 | 0 |
| [Claude OSINT Plugin](https://github.com/lawriec/claude-osint-plugin) | Plugin + skills + MCP | Claude Code | Adds an intelligence-cycle methodology and configured search, media, archive, and analysis MCP servers. | 2026-04-09 | 2026-05-10 | 0 |
| [Sherlock Skill](https://github.com/ImL1s/sherlock-skill) | Skill | Multi-model | Wraps Sherlock username searches with a portable skill and structured dossier output. | 2026-04-22 | 2026-04-22 | 0 |
| [Norteia Lead Recon](https://github.com/Luispitik/norteia-lead-recon) | Skill | Claude Code | Researches Spanish companies and leads through official open registers and geodata. | 2026-04-29 | 2026-05-01 | 0 |
| [OSINT Researcher](https://github.com/MrBridgeHQ/osint-researcher-claude) | Skill | Claude Code | Provides scoped OSINT, CTI, due diligence, and evidence-reporting procedures. | 2026-07-01 | 2026-07-06 | 0 |
| [Chinese OSINT Skills](https://github.com/zomin/chinese-osint-skills) | Skill pack | Multi-model | Supplies Chinese-platform research methods and scripts for cross-platform identity pivots. | 2026-04-30 | 2026-04-30 | 0 |
| [Geolocation Skill](https://github.com/zuocharles/geolocation-skill) | Skill | Agent Skills standard | Guides photo geolocation with visual clues, map queries, and source references. | 2026-03-30 | 2026-03-31 | 0 |

<a id="reconnaissance-and-threat-intelligence"></a>

## 🛡️ Reconnaissance and threat intelligence <sup>30 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [Anthropic Cybersecurity Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | Skill library | Multi-model | Packages extensive offensive, defensive, CTI, forensics, and reconnaissance procedures. | 2026-02-25 | 2026-06-26 | 25,580 |
| [HexStrike AI](https://github.com/0x4m4/hexstrike-ai) | MCP server | Model-agnostic (MCP) | Connects agents to a large collection of security and reconnaissance tools. | 2025-07-10 | 2026-04-27 | 10,311 |
| [Claude Bug Bounty](https://github.com/shuvonsec/claude-bug-bounty) | Skills + agents | Claude Code | Organizes authorized bug-bounty reconnaissance, testing, validation, and reporting. | 2026-03-08 | 2026-07-09 | 3,962 |
| [Claude BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | Skill pack | Claude Code | Adds structured web reconnaissance and vulnerability-hunting methodology. | 2026-05-05 | 2026-07-01 | 2,969 |
| [Claude Red](https://github.com/SnailSploit/Claude-Red) | Skill pack | Claude Code | Provides red-team and security research playbooks for Claude-based workflows. | 2026-03-04 | 2026-05-08 | 2,701 |
| [VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | Agent + skills + MCP | Multi-model | Orchestrates information gathering, vulnerability analysis, exploitation, and reporting. | 2026-04-18 | 2026-07-13 | 2,078 |
| [Pentest AI Agents](https://github.com/0xSteph/pentest-ai-agents) | Agent pack | Claude Code | Supplies specialized subagents for recon analysis, exploit research, detection, and reporting. | 2026-03-28 | 2026-06-22 | 1,995 |
| [Hack Skills](https://github.com/yaklang/hack-skills) | Skill library | Agent Skills standard | Covers reconnaissance, web and network security, forensics, reversing, and authorized research. | 2026-04-07 | 2026-06-16 | 1,365 |
| [Pentest AI](https://github.com/0xSteph/pentest-ai) | CLI + MCP | Multi-model | Exposes security tools, specialist agents, and deterministic probes through CLI and MCP. | 2026-04-04 | 2026-07-05 | 1,290 |
| [CyberStrike](https://github.com/CyberStrikeus/CyberStrike) | Agent + MCP | Multi-model | Runs agent-assisted offensive security with recon, testing, and evidence workflows. | 2026-02-14 | 2026-07-14 | 1,203 |
| [CVE MCP Server](https://github.com/mukul975/cve-mcp-server) | MCP server | Model-agnostic (MCP) | Correlates CVE, EPSS, KEV, Shodan, VirusTotal, and related security intelligence. | 2026-04-14 | 2026-06-22 | 1,082 |
| [Hackingtool Plugin](https://github.com/AKCodez/hackingtool-plugin) | Plugin + skill | Claude Code | Makes a large catalogue of pentest and OSINT tools discoverable and runnable by Claude. | 2026-04-23 | 2026-04-25 | 848 |
| [Recon Skills](https://github.com/uphiago/recon-skills) | Skill pack | Agent Skills standard | Provides field-oriented recon, dorking, secret discovery, asset mapping, and testing playbooks. | 2026-06-24 | 2026-07-08 | 754 |
| [MCP Security Hub](https://github.com/FuzzingLabs/mcp-security-hub) | MCP collection | Model-agnostic (MCP) | Exposes containerized security tools for recon, threat intelligence, code, and binary analysis. | 2026-01-06 | 2026-04-08 | 728 |
| [Transilience Community Tools](https://github.com/transilienceai/communitytools) | Skills + agents | Claude Code | Covers security reconnaissance, bug bounty, AI threat testing, validation, and reporting. | 2025-11-21 | 2026-07-13 | 409 |
| [Darknet MCP Server](https://github.com/badchars/darknet-mcp-server) | MCP server | Model-agnostic (MCP) | Unifies dark-web, breach, ransomware, malware, and blockchain intelligence tools. | 2026-06-23 | 2026-07-14 | 206 |
| [Reversecore MCP](https://github.com/sjkim1127/Reversecore_MCP) | MCP server | Model-agnostic (MCP) | Connects agents to reverse engineering, malware, forensics, and vulnerability research tools. | 2025-11-10 | 2026-07-13 | 180 |
| [Shodan MCP](https://github.com/w0h1v/mcp-shodan) | MCP server | Model-agnostic (MCP) | Provides device search, IP reconnaissance, DNS, CPE, and CVE intelligence. | 2024-12-12 | 2026-03-31 | 144 |
| [VirusTotal MCP](https://github.com/w0h1v/mcp-virustotal) | MCP server | Model-agnostic (MCP) | Queries files, URLs, domains, IPs, and related security-analysis records. | 2024-12-13 | 2026-05-24 | 138 |
| [ThreatSwarm](https://github.com/mukul975/Threatswarm) | Plugin + agents | Claude Code | Coordinates scope-aware agents across recon, exploitation, DFIR, and final reporting. | 2026-04-29 | 2026-04-29 | 59 |
| [ZettelForge](https://github.com/ThreatRecall/zettelforge) | CTI system + MCP | Multi-model | Extracts IOCs and threat entities into a local STIX knowledge graph with agent access. | 2026-04-06 | 2026-07-11 | 55 |
| [OSINT MCP Server](https://github.com/badchars/osint-mcp-server) | MCP server | Model-agnostic (MCP) | Correlates infrastructure and threat data from Shodan, Censys, DNS, BGP, archives, and more. | 2026-03-17 | 2026-03-17 | 35 |
| [Shodan MCP by Vorota](https://github.com/Vorota-ai/shodan-mcp) | MCP server | Model-agnostic (MCP) | Adds passive asset discovery, DNS analysis, and vulnerability intelligence from Shodan. | 2026-02-12 | 2026-02-12 | 21 |
| [Claude Code Pentest](https://github.com/Orizon-eu/claude-code-pentest) | Skill pack | Claude Code | Automates the authorized pentest lifecycle from initial recon to exploit-chain reports. | 2026-03-11 | 2026-03-11 | 19 |
| [Malware Sandbox MCP](https://github.com/mukul975/Malware-Sandbox-mcp) | MCP server | Model-agnostic (MCP) | Normalizes malware sandbox verdicts, IOCs, artifacts, and ATT&CK mappings. | 2026-06-11 | 2026-06-23 | 14 |
| [BBOT OSINT MCP](https://github.com/dn9uy3n/bbot-osint-mcp) | MCP server | Model-agnostic (MCP) | Connects BBOT asset discovery to Neo4j storage and MCP-based investigation workflows. | 2025-10-27 | 2025-11-07 | 8 |
| [MISP MCP](https://github.com/MISP/misp-mcp) | MCP server | Model-agnostic (MCP) | Provides read-only access to MISP threat intelligence events and attributes. | 2026-04-01 | 2026-06-26 | 8 |
| [Offensive Recon](https://github.com/mahuttha/offensive-recon) | Plugin + skills | Claude Code | Packages multi-phase reconnaissance skills and agents around common security tools. | 2026-03-01 | 2026-03-01 | 4 |
| [OSINT MCP Gateway](https://github.com/bonetrees/osint-mcp-gateway) | MCP server | Model-agnostic (MCP) | Routes agent queries across VirusTotal, Shodan, DNS, WHOIS, RIPEstat, and OTX. | 2025-11-23 | 2026-06-10 | 0 |
| [Bounty Recon Pro](https://github.com/synicalkid/bounty-recon-pro) | Skill | Claude Code | Runs scoped passive OSINT and active bug-bounty recon with evidence-oriented reports. | 2026-07-11 | 2026-07-11 | 0 |

<a id="web-research-and-source-discovery"></a>

## 🌐 Web research and source discovery <sup>24 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [Firecrawl MCP Server](https://github.com/firecrawl/firecrawl-mcp-server) | MCP server | Model-agnostic (MCP) | Gives agents web search, crawling, scraping, extraction, and structured research tools. | 2024-12-06 | 2026-07-14 | 6,955 |
| [Exa MCP Server](https://github.com/exa-labs/exa-mcp-server) | MCP server | Model-agnostic (MCP) | Provides semantic web search, content retrieval, and research discovery through Exa. | 2024-11-27 | 2026-07-14 | 4,720 |
| [Deep Research](https://github.com/u14app/deep-research) | Research system + MCP | Multi-model | Runs iterative web research and synthesis with configurable models and MCP access. | 2025-02-22 | 2026-06-18 | 4,632 |
| [Bright Data MCP](https://github.com/brightdata/brightdata-mcp) | MCP server | Model-agnostic (MCP) | Connects agents to search, browsing, scraping, and public web datasets. | 2025-04-15 | 2026-06-21 | 2,497 |
| [Tavily MCP](https://github.com/tavily-ai/tavily-mcp) | MCP server | Model-agnostic (MCP) | Exposes search, extraction, crawling, mapping, and research functions from Tavily. | 2025-01-27 | 2026-07-10 | 2,218 |
| [Apify MCP Server](https://github.com/apify/apify-mcp-server) | MCP server | Model-agnostic (MCP) | Makes Apify Actors and public web data collection available to compatible agents. | 2025-01-02 | 2026-07-14 | 1,916 |
| [Brave Search MCP Server](https://github.com/brave/brave-search-mcp-server) | MCP server | Model-agnostic (MCP) | Adds Brave web, news, image, video, and local search to MCP clients. | 2025-06-12 | 2026-07-12 | 1,297 |
| [De-Anthropocentric Research Engine](https://github.com/yogsoth-ai/de-anthropocentric-research-engine) | Research skill system | Multi-model | Organizes autonomous research into composable campaigns, strategies, tactics, and procedures. | 2026-02-10 | 2026-07-09 | 384 |
| [Kindly Web Search MCP](https://github.com/Shelpuk-AI-Technology-Consulting/kindly-web-search-mcp-server) | MCP server | Model-agnostic (MCP) | Aggregates web search, extraction, crawling, and browser automation for many clients. | 2026-01-02 | 2026-07-14 | 357 |
| [NotebookLM Skill](https://github.com/claude-world/notebooklm-skill) | Skill + MCP | Claude Code | Uses NotebookLM for source-grounded research, synthesis, and content preparation. | 2026-03-13 | 2026-04-14 | 338 |
| [MCP Omnisearch](https://github.com/spences10/mcp-omnisearch) | MCP server | Model-agnostic (MCP) | Combines multiple search, AI search, and content-processing providers behind MCP. | 2025-03-08 | 2026-07-13 | 333 |
| [Google Research MCP](https://github.com/mixelpixx/Google-Research-MCP) | MCP server | Model-agnostic (MCP) | Uses Google Search and browser automation for multi-step cited research. | 2024-12-19 | 2026-06-27 | 249 |
| [Reddit Research MCP](https://github.com/king-of-the-grackles/reddit-research-mcp) | MCP server | Reddit; Model-agnostic (MCP) | Supports structured Reddit discovery, thread collection, and community research. | 2025-08-12 | 2026-07-02 | 216 |
| [Octagon MCP Server](https://github.com/OctagonAI/octagon-mcp-server) | MCP server | Model-agnostic (MCP) | Provides public company, market, investor, private-market, and crypto research data. | 2025-03-12 | 2026-07-09 | 143 |
| [RivalSearch MCP](https://github.com/damionrashford/RivalSearchMCP) | MCP server | Model-agnostic (MCP) | Unifies web, social, news, academic, and entity-search sources behind MCP. | 2025-08-03 | 2026-07-14 | 113 |
| [Deep Research MCP](https://github.com/pminervini/deep-research-mcp) | MCP server | Multi-model | Connects several deep-research agents and model providers through one MCP interface. | 2025-08-07 | 2026-06-10 | 92 |
| [Deep Web Research MCP](https://github.com/qpd-v/mcp-DEEPwebresearch) | MCP server | Model-agnostic (MCP) | Coordinates recursive web search and page analysis for deeper topic coverage. | 2025-01-13 | 2025-03-05 | 86 |
| [Agent Search](https://github.com/brcrusoe72/agent-search) | MCP server | Model-agnostic (MCP) | Provides privacy-oriented search and browser retrieval for AI agents. | 2026-02-18 | 2026-07-13 | 57 |
| [OpenRouter Deep Research MCP](https://github.com/wheattoast11/openrouter-deep-research-mcp) | MCP server | Model-agnostic (MCP) | Orchestrates parallel research agents and consensus-backed synthesis through OpenRouter. | 2025-03-28 | 2026-03-29 | 54 |
| [Web Researcher MCP](https://github.com/zoharbabin/web-researcher-mcp) | MCP server | Model-agnostic (MCP) | Searches the web, extracts sources, and produces citation-aware research results. | 2026-05-18 | 2026-07-13 | 42 |
| [Helium MCP](https://github.com/connerlambden/helium-mcp) | MCP server | Model-agnostic (MCP) | Provides news discovery, bias scoring, market data, and multi-source synthesis. | 2026-04-10 | 2026-06-15 | 11 |
| [GiaSip Skills](https://github.com/GiaSip/giasip-skills) | Skills + plugin | Claude Code + Codex | Provides quick recon, fact-checking, research orchestration, and multi-model dispatch. | 2026-05-30 | 2026-07-15 | 11 |
| [Web Multi Search](https://github.com/soxoj/web-multi-search-skill) | Skill + script | OpenClaw | Searches several web engines in parallel and exports deduplicated results. | 2026-02-08 | 2026-02-08 | 7 |
| [Digital Research Skills](https://github.com/smarks26/digital-research-skills) | Research skill system | Multi-model | Plans evidence-driven research waves for OSINT, due diligence, trends, and long-form analysis. | 2026-05-29 | 2026-05-16 | 2 |

<a id="academic-and-structured-research"></a>

## 🎓 Academic and structured research <sup>6 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [Simple PubMed MCP](https://github.com/andybrandt/mcp-simple-pubmed) | MCP server | Model-agnostic (MCP) | Searches PubMed and retrieves biomedical article metadata and abstracts. | 2024-12-11 | 2026-03-19 | 169 |
| [mcp.science](https://github.com/pathintegral-institute/mcp.science) | MCP server | Model-agnostic (MCP) | Connects agents to scientific literature search and research data services. | 2025-03-27 | 2026-02-27 | 145 |
| [Academia MCP](https://github.com/IlyaGusev/academia_mcp) | MCP server | Model-agnostic (MCP) | Searches academic sources and retrieves papers for agent-assisted literature research. | 2025-01-24 | 2026-01-25 | 90 |
| [ZotPilot](https://github.com/xunhe730/ZotPilot) | Skill + MCP | Model-agnostic (MCP) | Connects Zotero collections to source-grounded research and agent workflows. | 2026-03-16 | 2026-06-28 | 66 |
| [OpenAlex Research MCP](https://github.com/oksure/openalex-research-mcp) | MCP server | Model-agnostic (MCP) | Queries OpenAlex works, authors, institutions, concepts, and citation relationships. | 2025-10-05 | 2026-06-22 | 36 |
| [Semantic Scholar Skills](https://github.com/zongmin-yu/semantic-scholar-skills) | Skills + MCP | Claude Code | Supports literature discovery, citation expansion, and structured Semantic Scholar research. | 2026-03-10 | 2026-03-16 | 19 |

---

<a id="metadata-conventions"></a>

## Metadata conventions

- **Project** links to the canonical public source repository.
- **Type** describes the repository's primary integration surface, not every component it contains.
- **Compatibility** names platforms and standards explicitly documented by the repository; `-` means it does not apply.
- **Description** summarizes the project's primary capability in neutral language.
- **Created** is the public repository creation date.
- **Last Update** is the latest recorded repository push date.
- **Stars ⭐** is a point-in-time snapshot captured on **2026-07-15**.
- Star counts are exact at verification time and may change afterward.
- Archived repositories are identified in the **Type** column.
- Inclusion indicates practical relevance, not a security audit, endorsement, or guarantee of maintenance.

> [!TIP]
> For standalone OSINT software, use [OSINT Tools Radar](README.md). For new standalone tools, see [emerging projects](EMERGING.md). For one searchable dataset, use [osint-repositories.csv](osint-repositories.csv).

<p align="right"><a href="#top">Back to top ↑</a></p>
