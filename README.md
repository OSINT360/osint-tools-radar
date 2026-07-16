<a id="top"></a>

<div align="center">
  <h1>OSINT Tools Radar</h1>
  <p>A catalogue of open-source OSINT tools organized by investigation target, platform, and emerging capability.</p>
  <p>
    <a href="EMERGING.md"><img alt="Emerging projects: 87" src="https://img.shields.io/badge/emerging-87-bf8700?style=flat-square"></a>
    <a href="#social-platforms"><img alt="Social platform entries: 73" src="https://img.shields.io/badge/social_platforms-73-8250df?style=flat-square"></a>
    <a href="AGENTIC.md"><img alt="Agentic integrations: 124" src="https://img.shields.io/badge/agentic_integrations-124-d1242f?style=flat-square"></a>
    <img alt="Catalogue entries: 484" src="https://img.shields.io/badge/catalogue_entries-484-8250df?style=flat-square">
    <img alt="Last update: 2026-07-16" src="https://img.shields.io/badge/last_update-2026--07--16-1f883d?style=flat-square">
  </p>
  <p><a href="README.md">OSINT Tools Radar</a> · <a href="EMERGING.md">Emerging Projects</a> · <strong><a href="AGENTIC.md">Agentic AI OSINT</a></strong> · <a href="TIMELINE.md">Added Timeline</a> · <a href="osint-repositories.csv">Repository Database CSV</a></p>
</div>

## About this catalogue

OSINT Tools Radar is a repository-first catalogue of open-source OSINT software. Every published entry represents a public source-code repository containing an identifiable tool or integration with a practical investigative use case. Project names link directly to the repositories that contain their implementations.

> [!IMPORTANT]
> Only implementation-bearing repositories with publicly accessible source code are included. Closed-source services, commercial tools without public code, link collections, prompt-only lists, datasets, and repository stubs are excluded.

> <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> marks projects added to the catalogue within the last 14 days.

<a id="table-of-contents"></a>

## Table of contents

- **Identity**
  - [Person](#person) <sup>2 projects</sup>
  - [Username](#username) <sup>2 projects</sup>
  - [Email](#email) <sup>7 projects</sup>
  - [Phone](#phone) <sup>3 projects</sup>
- **Infrastructure**
  - [Domain](#domain) <sup>17 projects</sup>
  - [IP Address](#ip-address) <sup>9 projects</sup>
  - [URL](#url) <sup>43 projects</sup>
  - [Dark Web](#dark-web) <sup>15 projects</sup>
- **Media and geography**
  - [Image](#image) <sup>34 projects</sup>
  - [Location](#location) <sup>16 projects</sup>
- **Organizations and assets**
  - [Company](#company) <sup>5 projects</sup>
  - [Cryptocurrency](#cryptocurrency) <sup>4 projects</sup>
- **Cross-target tooling**
  - [General](#general) <sup>43 projects</sup>
- **Social platforms**
  - [Cross-platform](#cross-platform) <sup>14 projects</sup>
  - [X and Twitter](#x-and-twitter) <sup>6 projects</sup>
  - [Facebook](#facebook) <sup>0 projects</sup>
  - [Instagram](#instagram) <sup>6 projects</sup>
  - [LinkedIn](#linkedin) <sup>5 projects</sup>
  - [Reddit](#reddit) <sup>3 projects</sup>
  - [Telegram](#telegram) <sup>13 projects</sup>
  - [TikTok](#tiktok) <sup>0 projects</sup>
  - [YouTube](#youtube) <sup>4 projects</sup>
  - [Snapchat](#snapchat) <sup>1 project</sup>
  - [WhatsApp](#whatsapp) <sup>1 project</sup>
  - [Steam](#steam) <sup>3 projects</sup>
  - [GitHub](#github) <sup>13 projects</sup>
  - [Discord](#discord) <sup>4 projects</sup>
- [Emerging projects](EMERGING.md) <sup>87 projects</sup>
- [Agentic AI OSINT](AGENTIC.md) <sup>124 projects</sup>
- [Added timeline](TIMELINE.md)
- [Complete repository database](osint-repositories.csv) <sup>439 unique repositories</sup>

---

<a id="person"></a>

## 👤 Person <sup>2 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [GHunt](https://github.com/mxrch/GHunt) | Python | - | Collects public information associated with Google accounts and identifiers. | 2020-10-02 | 2026-04-10 | 19,220 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Bellingcat Name Variant Search](https://github.com/bellingcat/name-variant-search) | Python | - | Generates and searches spelling and transliteration variants of personal names. | 2023-07-18 | 2026-06-25 | 53 |

<a id="username"></a>

## 🪪 Username <sup>2 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [username-anarchy](https://github.com/urbanadventurer/username-anarchy) | Ruby | - | Generates likely username permutations from names and naming patterns. | 2012-11-07 | 2024-09-20 | 1,431 |
| [vesper](https://github.com/krishpranav/vesper) | Rust | - | Performs lightweight username checks across online services. | 2021-06-20 | 2026-06-15 | 322 |

<a id="email"></a>

## ✉️ Email <sup>7 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [Holehe](https://github.com/megadose/holehe) | Python | - | Checks whether an email address is registered with supported online services. | 2020-06-25 | 2024-09-10 | 11,699 |
| [h8mail](https://github.com/khast3x/h8mail) | Python | - | Searches breach sources and local datasets for email-related records. | 2018-06-15 | 2022-06-25 | 5,098 |
| [pwnedOrNot](https://github.com/thewhiteh4t/pwnedOrNot) | Python | - | Searches breach data for passwords associated with an email address. | 2018-05-25 | 2026-03-28 | 2,598 |
| [Zehef](https://github.com/N0rz3/Zehef) | Python | - | Aggregates public information associated with an email address. | 2023-06-13 | 2024-11-13 | 1,042 |
| [iKy](https://github.com/kennbroorg/iKy) | Python | - | Builds profiles and timelines from email-based investigation modules. | 2018-12-14 | 2026-07-16 | 963 |
| [mailcat](https://github.com/sharsil/mailcat) | Python | - | Finds existing email addresses derived from a nickname. | 2021-08-20 | 2026-05-24 | 910 |
| [glit](https://github.com/shadawck/glit) | Rust | - | Extracts contributor email addresses from Git repositories and organizations. | 2022-11-14 | 2024-05-01 | 58 |

<a id="phone"></a>

## 📞 Phone <sup>3 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [PhoneInfoga](https://github.com/sundowndev/phoneinfoga) | Go | - | Collects and correlates publicly available information about phone numbers. | 2018-10-25 | 2026-01-06 | 17,032 |
| [Phunter](https://github.com/N0rz3/Phunter) | Python | - | Aggregates several public phone number investigation methods. | 2023-12-30 | 2024-04-06 | 1,089 |
| [odnoklassniki-checker](https://github.com/OSINT-mindset/odnoklassniki-checker) | Python | - | Looks for public OK.ru account data using a phone number or email. | 2022-10-15 | 2024-10-02 | 20 |

<a id="domain"></a>

## 🌐 Domain <sup>17 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [theHarvester](https://github.com/laramies/theHarvester) | Python | - | Collects names, email addresses, subdomains, and hosts from public sources. | 2011-01-01 | 2026-07-06 | 16,810 |
| [Amass](https://github.com/owasp-amass/amass) | Go | - | Maps external assets and discovers domains from multiple data sources. | 2018-07-10 | 2026-04-07 | 14,844 |
| [Subfinder](https://github.com/projectdiscovery/subfinder) | Go | - | Enumerates subdomains using passive online sources. | 2018-03-31 | 2026-07-02 | 14,021 |
| [BBOT](https://github.com/blacklanternsecurity/bbot) | Python | - | Recursively discovers internet-facing assets through modular scan events. | 2022-03-12 | 2026-07-08 | 10,159 |
| [OneForAll](https://github.com/shmilylty/OneForAll) | Python | - | Combines numerous sources and methods for subdomain discovery. | 2018-12-10 | 2026-05-11 | 9,927 |
| [reconFTW](https://github.com/six2dez/reconftw) | Shell | - | Orchestrates domain reconnaissance, asset collection, and follow-up checks. | 2020-12-30 | 2026-06-29 | 7,849 |
| [dnstwist](https://github.com/elceef/dnstwist) | Python | - | Generates and evaluates look-alike domains for phishing and impersonation research. | 2015-06-11 | 2025-04-15 | 5,707 |
| [Knockpy](https://github.com/guelfoweb/knockpy) | Python | - | Enumerates subdomains and resolves related DNS information. | 2014-02-11 | 2026-02-19 | 4,171 |
| [Findomain](https://github.com/Findomain/Findomain) | Rust | - | Discovers and monitors domains and subdomains from multiple sources. | 2019-04-14 | 2026-02-03 | 3,770 |
| [FinalRecon](https://github.com/thewhiteh4t/FinalRecon) | Python | - | Collects headers, DNS records, subdomains, and related web intelligence. | 2019-03-28 | 2026-06-01 | 2,845 |
| [dnsx](https://github.com/projectdiscovery/dnsx) | Go | - | Runs high-volume DNS queries and filters resolved records. | 2020-11-12 | 2026-07-16 | 2,808 |
| [SubDomainizer](https://github.com/nsonaniya2010/SubDomainizer) | Python | - | Finds subdomains and exposed data referenced in JavaScript files. | 2018-11-19 | 2026-07-14 | 1,875 |
| [domain-digger](https://github.com/wotschofsky/domain-digger) | TypeScript | - | Provides a web toolkit for DNS, certificate, hosting, and domain analysis. | 2021-07-29 | 2026-07-10 | 1,181 |
| [dnsgen](https://github.com/AlephNullSK/dnsgen) | Python | - | Generates likely DNS name permutations for further discovery. | 2019-09-24 | 2025-01-03 | 1,074 |
| [openSquat](https://github.com/atenreiro/opensquat) | Python | - | Detects newly registered look-alike domains associated with brands. | 2020-05-04 | 2026-04-27 | 977 |
| [subscraper](https://github.com/m8sec/subscraper) | Python | - | Enumerates subdomains and related targets from public sources. | 2018-09-27 | 2024-06-19 | 969 |
| [Subdominator](https://github.com/RevoltSecurities/Subdominator) | Python | - | Performs low-impact subdomain discovery across multiple sources. | 2023-07-24 | 2026-06-21 | 793 |

<a id="ip-address"></a>

## 🖧 IP Address <sup>9 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [IVRE](https://github.com/ivre/ivre) | Python | - | Builds searchable network intelligence from active and passive observations. | 2014-09-12 | 2026-07-05 | 4,086 |
| [Uncover](https://github.com/projectdiscovery/uncover) | Go | - | Queries internet search engines for exposed hosts matching a search. | 2022-03-02 | 2026-05-19 | 3,017 |
| [IPinfo CLI](https://github.com/ipinfo/cli) | Go | - | Queries IP geolocation, ASN, privacy, and network data from the command line. | 2020-10-23 | 2026-04-28 | 2,033 |
| [asn](https://github.com/nitefood/asn) | Shell | - | Reports ASN, BGP, geolocation, reputation, and routing information for IPs. | 2020-07-22 | 2026-06-22 | 1,911 |
| [Metabigor](https://github.com/j3ssie/metabigor) | Go | - | Correlates IP, ASN, domain, and network data without mandatory API keys. | 2019-05-24 | 2026-02-15 | 1,631 |
| [Harpoon](https://github.com/Te-k/harpoon) | Python | - | Provides command-line queries for open-source and threat intelligence indicators. | 2017-09-25 | 2026-05-18 | 1,288 |
| [HostHunter](https://github.com/SpiderLabs/HostHunter) | Python | - | Discovers hostnames associated with supplied IP addresses. | 2018-05-17 | 2023-03-30 | 1,168 |
| [asnmap](https://github.com/projectdiscovery/asnmap) | Go | - | Maps organizations and ASNs to their advertised network ranges. | 2022-09-29 | 2026-05-19 | 1,095 |
| [pygreynoise](https://github.com/GreyNoise-Intelligence/pygreynoise) | Python | - | Queries GreyNoise observations and classifications for internet-scanning IPs. | 2017-12-07 | 2026-07-09 | 177 |

<a id="url"></a>

## 🔗 URL <sup>43 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Firecrawl](https://github.com/firecrawl/firecrawl) | TypeScript | - | Provides APIs for web search, scraping, crawling, and structured extraction. | 2024-04-15 | 2026-07-16 | 151,931 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Browser Use](https://github.com/browser-use/browser-use) | Agent framework | Multi-model | Lets AI agents navigate websites, interact with pages, and extract information. | 2024-10-31 | 2026-07-14 | 105,083 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Crawl4AI](https://github.com/unclecode/crawl4ai) | Python | - | Crawls websites and produces structured, LLM-ready content and metadata. | 2024-05-09 | 2026-07-15 | 72,960 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Scrapling](https://github.com/D4Vinci/Scrapling) | Python | Agent Skills standard; Model-agnostic (MCP) | Provides adaptive web scraping, crawling, browser automation, and structured extraction. | 2024-10-13 | 2026-07-15 | 69,773 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Scrapy](https://github.com/scrapy/scrapy) | Python | - | Implements a mature Python framework for crawling and extracting structured web data. | 2010-02-22 | 2026-07-13 | 63,186 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [EasySpider](https://github.com/NaiboWang/EasySpider) | JavaScript | - | Creates and runs visual no-code web crawling and data extraction tasks. | 2020-07-18 | 2026-07-03 | 44,244 |
| [Web-Check](https://github.com/lissy93/web-check) | TypeScript | - | Produces a broad technical and open-source intelligence report for a website. | 2023-06-25 | 2026-07-11 | 34,168 |
| [changedetection.io](https://github.com/dgtlmoon/changedetection.io) | Python | - | Monitors web pages and records content changes over time. | 2021-01-27 | 2026-07-16 | 32,340 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [ScrapeGraphAI](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | Python | - | Builds scraping pipelines that use language models to extract structured information. | 2024-01-27 | 2026-07-15 | 28,409 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [ArchiveBox](https://github.com/ArchiveBox/ArchiveBox) | Python | - | Creates self-hosted, durable archives of web pages and linked online material. | 2017-05-05 | 2026-07-15 | 27,940 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Crawlee](https://github.com/apify/crawlee) | TypeScript | - | Provides a scalable SDK for HTTP crawling and browser automation. | 2016-08-26 | 2026-07-16 | 24,754 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Stagehand](https://github.com/browserbase/stagehand) | Agent SDK | Multi-model | Provides an SDK for agent-driven browser automation and page extraction. | 2024-03-24 | 2026-07-16 | 23,530 |
| [SingleFile](https://github.com/gildas-lormeau/SingleFile) | JavaScript | - | Saves a complete web page as one file for preservation and later analysis. | 2010-09-12 | 2026-02-24 | 21,836 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Linkwarden](https://github.com/linkwarden/linkwarden) | TypeScript | - | Preserves bookmarked pages and stored copies for later reference and collaboration. | 2022-04-09 | 2026-07-11 | 18,969 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Maxun](https://github.com/getmaxun/maxun) | TypeScript | - | Builds reusable web robots and structured data APIs through a visual interface. | 2023-10-23 | 2026-07-15 | 16,529 |
| [Photon](https://github.com/s0md3v/Photon) | Python | - | Crawls a supplied URL to collect links and related open-source data. | 2018-03-30 | 2026-02-10 | 13,040 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [httpx](https://github.com/projectdiscovery/httpx) | Go | - | Probes web targets at scale and reports HTTP, TLS, technology, and response metadata. | 2020-05-28 | 2026-07-16 | 10,174 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Steel Browser](https://github.com/steel-dev/steel-browser) | TypeScript | - | Runs a self-hosted browser API and sandbox for automated web operations. | 2024-11-01 | 2026-07-06 | 7,342 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Trafilatura](https://github.com/adbar/trafilatura) | Python | - | Extracts main text, metadata, links, and document structure from web pages. | 2019-04-08 | 2026-07-09 | 6,301 |
| [hakrawler](https://github.com/hakluke/hakrawler) | Go | - | Crawls web applications to discover endpoints, assets, and linked resources. | 2019-12-15 | 2024-12-21 | 5,091 |
| [gau](https://github.com/lc/gau) | Go | - | Collects known URLs from public archives and threat intelligence sources. | 2020-02-25 | 2026-03-20 | 5,036 |
| [Cariddi](https://github.com/edoardottt/cariddi) | Go | - | Crawls domains and extracts endpoints, secrets, tokens, and file references. | 2021-04-27 | 2026-07-15 | 3,456 |
| [pagodo](https://github.com/opsdisk/pagodo) | Python | - | Automates Google dork collection and searches against a target. | 2016-08-19 | 2025-08-30 | 3,365 |
| [waybackpack](https://github.com/jsvine/waybackpack) | Python | - | Downloads archived versions of a URL from the Wayback Machine. | 2016-04-11 | 2025-04-21 | 3,215 |
| [ParamSpider](https://github.com/devanshbatham/ParamSpider) | Python | - | Mines web archives for URLs containing useful parameters. | 2020-04-12 | 2026-03-07 | 3,135 |
| [waymore](https://github.com/xnl-h4ck3r/waymore) | Python | - | Collects archived URLs and responses from several public sources. | 2022-06-24 | 2026-06-11 | 2,691 |
| [Mitaka](https://github.com/ninoseki/mitaka) | TypeScript | - | Adds browser searches for URLs, hashes, IP addresses, and other indicators. | 2018-02-09 | 2026-06-14 | 1,822 |
| [BlackWidow](https://github.com/1N3/BlackWidow) | Python | - | Crawls a web application to collect intelligence and identify reachable paths. | 2018-01-06 | 2026-04-17 | 1,812 |
| [urlhunter](https://github.com/utkusen/urlhunter) | Go | - | Finds URLs exposed through public URL-shortening services. | 2020-11-21 | 2025-01-23 | 1,684 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [pywb](https://github.com/webrecorder/pywb) | Python | - | Indexes, serves, and replays WARC web archives. | 2013-12-09 | 2026-04-10 | 1,680 |
| [GooFuzz](https://github.com/m3n0sd0n4ld/GooFuzz) | Shell | - | Uses search-engine results to enumerate web paths, files, and parameters. | 2022-06-17 | 2025-12-21 | 1,577 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [ArchiveWeb.page](https://github.com/webrecorder/archiveweb.page) | TypeScript | - | Captures selected web pages and browsing sessions into portable web archives. | 2020-02-10 | 2026-04-30 | 1,521 |
| [FavFreak](https://github.com/devanshbatham/FavFreak) | Python | - | Creates favicon hashes for finding related websites through internet search engines. | 2020-07-03 | 2023-08-29 | 1,294 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Bellingcat Auto Archiver](https://github.com/bellingcat/auto-archiver) | Python | - | Archives web pages, social posts, images, and videos from queued URLs. | 2021-01-15 | 2026-04-27 | 1,095 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Browsertrix Crawler](https://github.com/webrecorder/browsertrix-crawler) | TypeScript | - | Captures interactive websites as WARC and WACZ archives with replay quality checks. | 2020-11-02 | 2026-07-16 | 1,081 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [ReplayWeb.page](https://github.com/webrecorder/replayweb.page) | TypeScript | - | Replays WARC and WACZ web archives locally in a browser. | 2019-12-09 | 2026-07-06 | 964 |
| [xurlfind3r](https://github.com/hueristiq/xurlfind3r) | Go | - | Discovers URLs for a domain through passive public sources. | 2021-05-13 | 2025-11-17 | 710 |
| [waybackpy](https://github.com/akamhy/waybackpy) | Python | - | Provides a command-line and library interface to Wayback Machine APIs. | 2020-05-02 | 2022-11-17 | 596 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Browsertrix](https://github.com/webrecorder/browsertrix) | TypeScript | - | Provides a collaborative platform for browser-based web archiving and replay. | 2021-06-28 | 2026-07-16 | 438 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [TheScrapper](https://github.com/champmq/TheScrapper) | Python | - | Crawls websites to extract email addresses, phone numbers, and social profile links. | 2021-05-07 | 2026-05-29 | 363 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Memorious4](https://github.com/dataresearchcenter/memorious) | Python | - | Runs maintained configurable crawlers for investigative documents and structured public data. | 2025-01-21 | 2026-06-09 | 3 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [openParlData.ch Web Archive](https://gitlab.com/opendata.ch/openparldatach/web-archive) | Web archive pipeline | - | Archives Swiss parliamentary websites with Browsertrix and serves them through pywb. | 2026-04-02 | 2026-05-04 | 0 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [ConsentTheater Playbill](https://codeberg.org/ConsentTheater/playbill) | TypeScript | - | Maintains a queryable knowledge base of trackers, cookies, domains, and responsible companies. | 2026-05-31 | 2026-07-15 | 0 |

<a id="dark-web"></a>

## 🕸️ Dark Web <sup>15 projects</sup>

Use this category as a layered collection workflow: **darkdump** for first-pass keyword discovery and saved result sets, **Sicry** for Tor health, identity rotation, multi-engine search, and targeted fetching, and **TorBot** only after a relevant onion service has been identified and needs link-tree or structure mapping.

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [Robin](https://github.com/apurvsinghgautam/robin) | Python | Tor; OpenAI, Claude, Gemini, Ollama, and compatible APIs | Refines queries, filters dark-web search results, and saves assisted investigation summaries. | 2025-04-08 | 2026-07-15 | 5,945 |
| [TorBot](https://github.com/DedSecInside/TorBot) | Python | Tor / .onion | Crawls a known onion service and exports its link tree for structure mapping. | 2017-05-17 | 2025-10-29 | 4,350 |
| [darkdump](https://github.com/josh0xA/darkdump) | Python | Tor and clearnet search engines | Runs first-pass keyword discovery across dark-web search engines and saves result sets for later review. | 2021-02-11 | 2026-04-08 | 1,642 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [AIL Framework](https://github.com/ail-project/ail-framework) | Python | Tor, I2P, chats, files, and feeds | Collects, crawls, processes, correlates, and analyzes unstructured information from Tor and other sources. | 2020-04-20 | 2026-07-15 | 980 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Ahmia](https://github.com/ahmia/ahmia-site) | Python | Tor, Django, and Elasticsearch | Provides an open-source search application and interface for indexed onion services. | 2016-05-23 | 2026-07-09 | 747 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Darkus](https://github.com/Lucksi/Darkus) | Python | Tor / .onion search engines | Queries multiple onion search engines for keyword-matched hidden services. | 2023-10-27 | 2026-02-21 | 683 |
| [VoidAccess](https://github.com/KatrielMoses/voidaccess) | Python | Tor / .onion | Runs a self-hosted pipeline for dark-web collection, extraction, correlation, and graph analysis. | 2026-04-29 | 2026-07-08 | 289 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [darc](https://github.com/JarryShaw/darc) | Python | Tor and proxy-based dark-web services | Crawls dark-web services, stores link and host data, and supports distributed collection workflows. | 2019-09-28 | 2026-07-11 | 225 |
| [Darknet MCP Server](https://github.com/badchars/darknet-mcp-server) | MCP server | Tor / .onion; Model-agnostic (MCP) | Unifies dark-web search, breach, ransomware, malware, and blockchain intelligence tools for MCP clients. | 2026-06-23 | 2026-06-24 | 221 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [onion-lookup](https://github.com/ail-project/onion-lookup) | Python | Tor / .onion; AIL | Checks onion-service availability and retrieves associated metadata from an AIL instance. | 2024-10-03 | 2026-01-05 | 64 |
| [OnionClaw](https://github.com/JacobJandon/OnionClaw) | Skill + CLI | Tor / .onion; OpenClaw | Adds Tor search, hidden-service retrieval, crawling, and export workflows to OpenClaw. | 2026-03-14 | 2026-05-28 | 61 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [DarkSpider](https://github.com/PROxZIMA/DarkSpider) | Python | Tor / .onion | Crawls onion services through Tor and visualizes extracted link relationships. | 2022-07-31 | 2024-07-27 | 45 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Sicry](https://github.com/JacobJandon/Sicry) | Python + MCP | Tor / .onion; MCP and AI agents | Checks Tor health, rotates identity, searches onion engines, fetches known services, and exposes optional agent-assisted analysis. | 2026-03-14 | 2026-05-28 | 16 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [PyAhmia](https://github.com/rly0nheart/pyahmia) | Python | Tor | Provides programmatic search access to Ahmia-indexed Tor hidden services. | 2025-09-26 | 2026-06-01 | 16 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [LeakRecon](https://github.com/egnake/LeakRecon) | Python | Tor / SOCKS5 | Runs Tor-routed leak reconnaissance with local history, change tracking, and report export. | 2026-05-18 | 2026-06-04 | 10 |

<a id="image"></a>

## 🖼️ Image <sup>34 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [face_recognition](https://github.com/ageitgey/face_recognition) | Python | Python and CLI | Recognizes and compares faces through a Python API and command-line interface. | 2017-03-03 | 2026-06-25 | 56,586 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Frigate](https://github.com/blakeblackshear/frigate) | TypeScript | IP and RTSP cameras | Records and analyzes local IP-camera streams with real-time object detection, tracking, and search. | 2019-01-26 | 2026-07-16 | 34,378 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [InsightFace](https://github.com/deepinsight/insightface) | Python | Python, C++, and desktop GUI | Performs face detection, alignment, recognition, and embedding analysis across multiple runtimes. | 2017-09-01 | 2026-05-23 | 29,263 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [DeepFace](https://github.com/serengil/deepface) | Python | - | Performs face verification, recognition, search, and facial attribute analysis. | 2020-02-08 | 2026-06-29 | 23,110 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [CompreFace](https://github.com/exadel-inc/CompreFace) | Java | Self-hosted REST API | Provides self-hosted face detection, recognition, verification, and similarity search through a REST API. | 2020-07-06 | 2023-11-14 | 8,138 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [ZoneMinder](https://github.com/ZoneMinder/zoneminder) | PHP | IP, USB, and analog cameras | Monitors, records, and reviews IP, USB, and analog camera feeds. | 2013-04-12 | 2026-07-15 | 5,882 |
| [ExifTool](https://github.com/exiftool/exiftool) | Perl | - | Reads and writes metadata embedded in images and other file formats. | 2018-05-09 | 2026-05-27 | 4,875 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Torchreid](https://github.com/KaiyangZhou/deep-person-reid) | Python | Images and camera footage | Re-identifies people across images and camera views with pretrained models and training tools. | 2018-03-11 | 2026-01-09 | 4,868 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [motionEye](https://github.com/motioneye-project/motioneye) | Python | IP and local cameras | Provides web-based multi-camera monitoring, motion detection, recording, and review. | 2015-08-30 | 2026-06-20 | 4,635 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [ImageHash](https://github.com/JohannesBuchner/imagehash) | Python | - | Calculates perceptual image hashes for similarity and duplicate-image comparison. | 2013-03-02 | 2025-04-17 | 3,852 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Search by Image](https://github.com/dessant/search-by-image) | JavaScript | Chrome, Edge, and Safari | Sends images to multiple reverse-image search engines from Chrome, Edge, and Safari. | 2017-06-17 | 2026-06-27 | 3,597 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Viseron](https://github.com/roflcoopter/viseron) | Python | CCTV and IP cameras | Analyzes local camera feeds with motion, object, face, and license-plate detection. | 2020-08-30 | 2026-07-15 | 3,284 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Human](https://github.com/vladmandic/human) | TypeScript | Browser and Node.js | Performs face detection, recognition, matching, and broader human analysis in browsers and Node.js. | 2020-10-11 | 2025-12-13 | 3,209 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Sherloq](https://github.com/GuidoBartoli/sherloq) | Python | - | Combines metadata, error-level, noise, clone, splice, and resampling analysis for images. | 2017-06-24 | 2026-07-16 | 3,167 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [DeepCamera](https://github.com/SharpAI/DeepCamera) | JavaScript | CCTV and IP cameras | Analyzes camera feeds with local vision models, face recognition, re-identification, and configurable AI skills. | 2019-03-05 | 2026-04-21 | 2,908 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [RetinaFace](https://github.com/serengil/retinaface) | Python | - | Detects, aligns, and extracts faces from images for downstream comparison workflows. | 2021-04-25 | 2026-06-01 | 2,012 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Photonix](https://github.com/photonixapp/photonix) | Python | - | Organizes and searches local photo collections using faces, objects, locations, and visual attributes. | 2017-03-07 | 2026-07-07 | 1,953 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [unblink](https://github.com/zapdos-labs/unblink) | Go | RTSP and MJPEG cameras | Uses vision-language models to monitor camera feeds and search recorded frames with natural language. | 2025-11-05 | 2026-03-09 | 1,471 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [HomeGallery](https://github.com/xemle/home-gallery) | JavaScript | Self-hosted photo and video collections | Indexes local photos and videos for reverse-image lookup, face search, and semantic discovery. | 2020-12-22 | 2026-06-22 | 1,169 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Kerberos Agent](https://github.com/kerberos-io/agent) | Go | RTSP cameras | Runs local video monitoring, recording, motion analysis, and event capture for RTSP camera streams. | 2020-08-12 | 2026-07-16 | 1,073 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [camera.ui](https://github.com/cameraui/camera.ui) | TypeScript | CCTV and IP cameras | Records, monitors, and searches local camera feeds with on-device detection workflows. | 2021-10-27 | 2026-07-16 | 1,063 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [clearcam](https://github.com/roryclear/clearcam) | Python | RTSP and HLS cameras | Adds object detection, tracking, notifications, summaries, and search to security-camera feeds. | 2025-01-04 | 2026-07-15 | 949 |
| [ExifLooter](https://github.com/aydinnyunus/exifLooter) | Go | - | Finds geolocation metadata in local and remote images and maps the results. | 2022-07-30 | 2026-01-16 | 494 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [gallery-dl](https://codeberg.org/mikf/gallery-dl) | Python | Cross-platform image sites | Downloads image galleries and media collections from supported websites. | 2026-03-24 | 2026-07-15 | 380 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [SentryShot](https://github.com/SentryShot/sentryshot) | Rust | IP and RTSP cameras | Records camera streams and applies local object detection through a web video-management interface. | 2023-10-29 | 2026-04-27 | 357 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [VibeNVR](https://github.com/spupuz/VibeNVR) | JavaScript | IP and RTSP cameras | Provides privacy-focused local camera recording and monitoring without a cloud dependency. | 2026-01-15 | 2026-07-16 | 326 |
| [GVision](https://github.com/GONZOsint/gvision) | Python | - | Uses image analysis to detect landmarks and related web entities. | 2023-03-29 | 2024-12-08 | 272 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [goris](https://github.com/tanaikech/goris) | Go | Google Images | Runs Google reverse-image searches from the command line. | 2017-04-26 | 2026-07-07 | 124 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Project Eyes On](https://github.com/Y0oshi/Project-Eyes-On) | Python | Public camera directories and web search | Finds publicly accessible IP-camera streams through public directories and web-search queries. | 2026-01-10 | 2026-01-12 | 120 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [EfficientIR](https://github.com/Sg4Dylan/EfficientIR) | Python | Local image collections | Finds similar and duplicate images in local collections using visual embeddings. | 2020-03-30 | 2024-07-22 | 112 |
| [lingolens](https://github.com/OSINT-mindset/lingolens) | HTML | - | Runs multilingual Google Lens searches and exports the results. | 2023-03-10 | 2026-05-29 | 85 |
| [PhotOSINT](https://github.com/Haris87/photosint) | JavaScript | - | Extracts image metadata and adds reverse-image search actions to the browser. | 2019-09-15 | 2021-07-13 | 60 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [OpenArchive Save](https://github.com/OpenArchive/Save-app-ios) | Swift | iOS | Captures and preserves mobile media with secure storage and provenance-oriented workflows. | 2018-06-06 | 2026-05-10 | 20 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [ProofMode](https://gitlab.com/guardianproject/proofmode/proofmode-android) | Kotlin | Android | Adds hashes, signatures, sensor data, and C2PA provenance to captured mobile media. | 2022-01-10 | 2026-07-15 | 18 |

<a id="location"></a>

## 📍 Location <sup>16 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [QGIS](https://github.com/qgis/QGIS) | C++ | - | Provides a complete desktop environment for geospatial data analysis and mapping. | 2011-05-02 | 2026-07-16 | 14,092 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [OSMnx](https://github.com/gboeing/osmnx) | Python | OpenStreetMap | Downloads, models, and analyzes street networks and other OpenStreetMap features. | 2016-07-24 | 2026-07-16 | 5,781 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Google Maps Scraper by gosom](https://github.com/gosom/google-maps-scraper) | Go | Google Maps | Collects structured place and business information from Google Maps. | 2023-04-22 | 2026-07-13 | 4,987 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [GeoAI](https://github.com/opengeos/geoai) | Python | - | Applies machine-learning and computer-vision workflows to geospatial data. | 2023-08-11 | 2026-07-16 | 3,186 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Google Maps Scraper by omkarcloud](https://github.com/omkarcloud/google-maps-scraper) | Python | Google Maps | Provides an alternative workflow for extracting business and place data from Google Maps. | 2023-05-19 | 2026-07-04 | 2,897 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [GeoLibre](https://github.com/opengeos/GeoLibre) | Python | - | Provides open geospatial and remote-sensing analysis workflows. | 2026-05-27 | 2026-07-16 | 1,745 |
| [GeoWiFi](https://github.com/GONZOsint/geowifi) | Python | - | Queries public Wi-Fi geolocation sources using BSSIDs and SSIDs. | 2022-02-05 | 2024-12-21 | 1,372 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Satpy](https://github.com/pytroll/satpy) | Python | - | Loads, transforms, composites, and exports meteorological satellite observations. | 2016-02-09 | 2026-07-08 | 1,200 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [CoastSat](https://github.com/kvos/CoastSat) | Python | - | Extracts and analyzes shoreline change from public satellite imagery. | 2018-09-28 | 2026-05-29 | 885 |
| [ShadowFinder](https://github.com/bellingcat/ShadowFinder) | Python | - | Estimates possible locations from the geometry of shadows in an image. | 2024-05-01 | 2026-02-13 | 593 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [EODAG](https://github.com/CS-SI/eodag) | Python | - | Searches and downloads Earth observation products from multiple data providers. | 2019-08-22 | 2026-07-10 | 424 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Bellingcat OSM Search](https://github.com/bellingcat/osm-search) | TypeScript | OpenStreetMap | Finds combinations of OpenStreetMap features based on their geographic proximity. | 2022-10-05 | 2026-07-07 | 207 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Bellingcat ADS-B History](https://github.com/bellingcat/adsb-history) | TypeScript | ADS-B | Stores historical ADS-B observations and supports spatial, temporal, and aircraft filtering. | 2025-08-22 | 2026-03-05 | 87 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Copernicus Browser](https://github.com/eu-cdse/copernicus-browser) | JavaScript | Copernicus Data Space | Searches, visualizes, and compares Earth observation data from Copernicus services. | 2023-08-08 | 2026-07-09 | 81 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Bellingcat Geoclustering](https://github.com/bellingcat/geoclustering) | Python | - | Groups and explores geographic observations to identify spatial patterns. | 2022-06-29 | 2026-07-07 | 45 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Bellingcat CouncilSearcher](https://github.com/bellingcat/CouncilSearcher) | Python | - | Searches local-government documents and records across supported council websites. | 2025-05-07 | 2026-01-07 | 16 |

<a id="company"></a>

## 🏢 Company <sup>5 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [Aleph](https://github.com/alephdata/aleph) | JavaScript | - | Lets investigators search documents and structured data for people and companies. | 2014-08-27 | 2025-12-19 | 2,398 |
| [cloud_enum](https://github.com/initstring/cloud_enum) | Python | - | Enumerates public cloud resources associated with organization keywords. | 2019-05-31 | 2026-07-09 | 2,115 |
| [emploleaks](https://github.com/infobyte/emploleaks) | Python | - | Identifies company employees appearing in credential leak data. | 2023-04-21 | 2026-05-19 | 786 |
| [OpenSanctions](https://github.com/opensanctions/opensanctions) | Python | - | Builds searchable data on sanctions, entities, and persons of interest. | 2015-12-05 | 2026-07-16 | 768 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Bellingcat Sugartrail](https://github.com/bellingcat/sugartrail) | Python | - | Builds relationship graphs from UK companies, officers, and registered addresses. | 2022-09-04 | 2026-02-20 | 78 |

<a id="cryptocurrency"></a>

## ₿ Cryptocurrency <sup>4 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [Bitcoin ETL](https://github.com/blockchain-etl/bitcoin-etl) | Python | - | Exports Bitcoin-family blockchain data into analysis-friendly formats. | 2018-09-13 | 2025-05-02 | 458 |
| [all-in-one-bot](https://github.com/uerax/all-in-one-bot) | Go | - | Tracks on-chain activity and market signals through a Telegram interface. | 2023-03-28 | 2026-06-12 | 180 |
| [GraphSense Dashboard](https://github.com/graphsense/graphsense-dashboard) | Elm | - | Provides interactive exploration of cryptocurrency transactions and entities. | 2017-10-18 | 2026-07-14 | 135 |
| [GraphSense Library](https://github.com/graphsense/graphsense-lib) | Python | - | Supplies CLI and backend utilities for cryptocurrency analytics workflows. | 2022-10-11 | 2026-07-14 | 17 |

<a id="general"></a>

## 🧰 General <sup>43 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [MarkItDown](https://github.com/microsoft/markitdown) | Python | - | Converts common document and media formats into Markdown for analysis. | 2024-11-13 | 2026-05-26 | 166,632 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Whisper](https://github.com/openai/whisper) | Python | - | Runs multilingual speech recognition, translation, and language identification locally. | 2022-09-16 | 2026-04-15 | 105,066 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | Python | - | Performs multilingual OCR, document layout analysis, and structured text extraction. | 2020-05-08 | 2026-06-26 | 85,633 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Tesseract](https://github.com/tesseract-ocr/tesseract) | C++ | - | Provides a multilingual optical character recognition engine. | 2014-08-12 | 2026-07-16 | 75,383 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Docling](https://github.com/docling-project/docling) | Python | - | Parses PDFs, office files, HTML, images, and audio into structured document representations. | 2024-07-09 | 2026-07-14 | 63,295 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | C++ | - | Provides an efficient C and C++ implementation for local Whisper transcription. | 2022-09-25 | 2026-07-11 | 51,792 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Marker](https://github.com/datalab-to/marker) | Python | - | Converts PDFs and other documents into Markdown, JSON, tables, and structured text. | 2023-10-30 | 2026-06-29 | 37,565 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) | Python | - | Adds searchable OCR text layers to scanned PDF documents. | 2013-12-20 | 2026-07-16 | 34,201 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [SearXNG](https://github.com/searxng/searxng) | Python | - | Aggregates results from multiple search services in a self-hosted metasearch engine. | 2021-04-12 | 2026-07-16 | 33,983 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [OpenDataLoader PDF](https://github.com/opendataloader-project/opendataloader-pdf) | Java | - | Extracts text, tables, layout, and structured content from PDF documents. | 2025-05-13 | 2026-07-14 | 27,372 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [WhisperX](https://github.com/m-bain/whisperX) | Python | - | Adds word-level timestamps and speaker diarization to speech transcription. | 2022-12-09 | 2026-07-13 | 23,103 |
| [SpiderFoot](https://github.com/smicallef/spiderfoot) | Python | - | Automates multi-source OSINT collection and attack-surface mapping. | 2012-04-28 | 2023-11-05 | 19,711 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Unstructured](https://github.com/Unstructured-IO/unstructured) | Python | - | Normalizes documents and extracts elements for search, analytics, and RAG pipelines. | 2022-09-26 | 2026-07-15 | 15,145 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [OpenRefine](https://github.com/OpenRefine/OpenRefine) | Java | - | Cleans, transforms, reconciles, and links inconsistent structured data. | 2012-10-15 | 2026-07-16 | 11,909 |
| [OpenCTI](https://github.com/OpenCTI-Platform/opencti) | TypeScript | - | Organizes cyber threat intelligence in a graph-based analysis platform. | 2018-12-17 | 2026-07-16 | 9,690 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [MISP](https://github.com/MISP/MISP) | PHP | - | Stores, correlates, analyzes, and shares structured threat intelligence and indicators. | 2013-02-07 | 2026-07-13 | 6,418 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [docTR](https://github.com/mindee/doctr) | Python | - | Detects and recognizes text in document images using deep-learning models. | 2021-01-08 | 2026-07-15 | 6,182 |
| [Recon-ng](https://github.com/lanmaster53/recon-ng) | Python | - | Organizes modular open-source intelligence collection in a command-line framework. | 2019-03-28 | 2024-11-01 | 5,782 |
| [IntelOwl](https://github.com/intelowlproject/IntelOwl) | Python | - | Orchestrates threat intelligence analyzers and connectors at scale. | 2019-12-31 | 2026-07-02 | 4,624 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Apache Tika](https://github.com/apache/tika) | Java | - | Detects file types and extracts text and metadata from many document formats. | 2009-05-21 | 2026-07-16 | 3,870 |
| [Mr.Holmes](https://github.com/Lucksi/Mr.Holmes) | Python | - | Combines multiple identity, domain, phone, and social investigation modules. | 2021-06-23 | 2026-02-21 | 3,857 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [GLiNER](https://github.com/urchade/GLiNER) | Python | - | Recognizes user-defined entity types in unstructured text without task-specific retraining. | 2023-11-14 | 2026-07-06 | 3,395 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Timesketch](https://github.com/google/timesketch) | Python | - | Supports collaborative search, annotation, and analysis across multiple event timelines. | 2014-06-19 | 2026-07-10 | 3,376 |
| [X-osint](https://github.com/TermuxHackz/X-osint) | Python | - | Runs phone, email, domain, VIN, and identity-oriented lookup modules. | 2023-03-11 | 2026-07-12 | 2,490 |
| [sn0int](https://github.com/kpcyrd/sn0int) | Rust | - | Provides a semi-automatic OSINT framework with installable modules. | 2018-10-05 | 2025-01-31 | 2,485 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Splink](https://github.com/moj-analytical-services/splink) | Python | - | Performs probabilistic entity resolution and deduplication across imperfect records. | 2019-11-22 | 2026-07-07 | 2,264 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [MediaInfo](https://github.com/MediaArea/MediaInfo) | C++ | - | Extracts technical metadata from audio, video, image, and container formats. | 2014-06-10 | 2026-06-15 | 1,966 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [OpenOCR](https://github.com/Topdu/OpenOCR) | Python | - | Provides an open toolkit for text detection and recognition in images and documents. | 2024-05-31 | 2026-05-20 | 1,409 |
| [Watcher](https://github.com/thalesgroup-cert/Watcher) | JavaScript | - | Collects, enriches, and searches cyber threat intelligence with assisted analysis. | 2020-09-01 | 2026-07-08 | 1,337 |
| [Open Semantic Search](https://github.com/opensemanticsearch/open-semantic-search) | Shell | - | Searches, extracts, and links entities across large document collections. | 2016-03-30 | 2025-04-19 | 1,189 |
| [Taranis AI](https://github.com/taranis-ai/taranis-ai) | Python | - | Collects and analyzes open-source information for situational awareness. | 2023-10-05 | 2026-07-15 | 1,179 |
| [Mihari](https://github.com/ninoseki/mihari) | Ruby | - | Aggregates search queries across threat intelligence services. | 2019-04-15 | 2026-07-04 | 939 |
| [ThreatIngestor](https://github.com/pedramamini/ThreatIngestor) | Python | - | Extracts and routes threat indicators from public information feeds. | 2017-08-31 | 2026-05-26 | 922 |
| [Seekr](https://github.com/seekr-osint/seekr) | Go | - | Offers a multi-purpose OSINT toolkit through a web interface. | 2022-12-06 | 2026-06-16 | 834 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [ICIJ Datashare](https://github.com/ICIJ/datashare) | Java | - | Indexes investigative documents, runs OCR, and extracts people, organizations, and locations. | 2016-04-20 | 2026-07-16 | 744 |
| [LinkScope Client](https://github.com/AccentuSoft/LinkScope_Client) | Python | - | Represents investigation entities and relationships in an extensible visual workspace. | 2021-09-15 | 2025-02-06 | 474 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [FollowTheMoney](https://github.com/alephdata/followthemoney) | Python | - | Defines an investigative data model for entities, assets, documents, and relationships. | 2017-10-20 | 2025-06-27 | 278 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [ICIJ Extract](https://github.com/ICIJ/extract) | Python | - | Extracts searchable text and metadata from investigative document collections. | 2015-05-07 | 2026-07-16 | 256 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [MalwareDB](https://github.com/malwaredb/malwaredb-rs) | Rust | - | Stores, indexes, and analyzes malware samples and associated metadata. | 2023-02-19 | 2026-07-15 | 59 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [DocumentCloud](https://github.com/MuckRock/documentcloud) | Python | - | Provides the backend for uploading, processing, searching, and publishing source documents. | 2019-09-09 | 2026-07-13 | 49 |
| [Ronin Recon](https://github.com/ronin-rb/ronin-recon) | Ruby | - | Provides a modular reconnaissance framework and command-line interface. | 2023-04-11 | 2026-01-15 | 42 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [StratIntel](https://codeberg.org/martinsnygg/stratintel) | Python | - | Monitors RSS sources, scores items, learns from feedback, and produces strategic reports. | 2025-12-18 | 2026-07-14 | 3 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Amanu](https://gitlab.com/varg.alejandro25/amanu) | Python | - | Runs local speech transcription and assigns timestamped passages to detected speakers. | 2026-07-09 | 2026-07-16 | 1 |

---

<a id="social-platforms"></a>

## Social platforms

The following sections separate tools by the social, community, messaging, video, gaming, or code-hosting platform they primarily investigate. The **Compatibility** column identifies the supported platform or cross-platform scope; agentic tools retain their AI-client compatibility after the platform name.

> [!NOTE]
> Some legacy projects remain useful for research or reference even when the platform behavior they relied on has changed; their age is visible in the update date.

<a id="cross-platform"></a>

## Cross-platform <sup>14 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [Sherlock](https://github.com/sherlock-project/sherlock) | Python | Cross-platform (400+) | Checks a username across many social networks. | 2018-12-24 | 2026-05-09 | 86,672 |
| [Maigret](https://github.com/soxoj/maigret) | Python | Cross-platform (3,000+) | Builds username-based account reports across thousands of sites. | 2020-06-27 | 2026-07-16 | 35,451 |
| [Social Analyzer](https://github.com/qeeqbox/social-analyzer) | JavaScript | Cross-platform (1,000+) | Searches and analyzes profiles across numerous social platforms. | 2020-11-30 | 2026-01-12 | 23,482 |
| [Blackbird](https://github.com/p1ngul1n0/blackbird) | Python | Cross-platform (600+) | Searches social platforms for accounts linked to a username or email. | 2022-05-06 | 2025-07-13 | 7,035 |
| [Snoop](https://github.com/snooppr/snoop) | Python | Cross-platform (5,400+) | Searches for username usage across a large collection of websites. | 2020-02-14 | 2026-07-15 | 3,963 |
| [gosearch](https://github.com/ibnaleem/gosearch) | Go | Cross-platform (300+) | Searches for a person's digital footprint across hundreds of websites. | 2024-11-09 | 2026-07-08 | 3,505 |
| [user-scanner](https://github.com/kaifcodec/user-scanner) | Python | Cross-platform (310+ vectors) | Runs username and email discovery checks across many services. | 2025-10-19 | 2026-07-16 | 2,736 |
| [WhatsMyName](https://github.com/WebBreacher/WhatsMyName) | Python | Cross-platform (700+) | Checks usernames using community-maintained site definitions and scripts. | 2015-10-02 | 2026-06-24 | 2,673 |
| [Aliens Eye](https://github.com/arxhr007/Aliens_eye) | Python | Cross-platform (840+) | Searches for accounts associated with a username across hundreds of platforms. | 2021-09-22 | 2026-07-03 | 2,629 |
| [Tookie](https://github.com/Alfredredbird/tookie-osint) | Python | Cross-platform | Provides a multi-target information gathering toolkit. | 2023-08-22 | 2026-07-07 | 2,598 |
| [socid-extractor](https://github.com/soxoj/socid-extractor) | Python | Cross-platform (130+) | Converts profile URLs into structured identity records across many platforms. | 2019-11-17 | 2026-07-14 | 1,037 |
| [Linkook](https://github.com/JackJuly/linkook) | Python | Cross-platform | Discovers linked social accounts and email clues from a username. | 2025-01-30 | 2026-02-28 | 993 |
| [Marple](https://github.com/soxoj/marple) | Python | Cross-platform via search engines | Finds profile links through search engines and extensible analysis plugins. | 2021-11-16 | 2026-07-14 | 313 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Social OSINT](https://github.com/krishpranav/socialosint) | Rust | Instagram, LinkedIn, X / Twitter | Collects exposed email addresses from supported social platforms and checks related leak data. | 2021-07-02 | 2026-02-10 | 93 |

<a id="x-and-twitter"></a>

## X and Twitter <sup>6 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [Nitter](https://github.com/zedeus/nitter) | Nim | X / Twitter | Provides a privacy-oriented front end for viewing public X content. | 2019-06-20 | 2026-07-11 | 13,267 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [twikit](https://github.com/d60/twikit) | Python | X / Twitter | Provides an alternative Python client for collecting and interacting with public X data. | 2024-01-20 | 2026-03-10 | 4,559 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [twscrape](https://github.com/vladkens/twscrape) | Python | X / Twitter | Collects public X data through supported GraphQL endpoints with account-pool rotation. | 2023-05-05 | 2026-06-26 | 2,584 |
| [X Tweet Fetcher](https://github.com/ythx-101/x-tweet-fetcher) | Python | X / Twitter | Retrieves public X posts, replies, timelines, and articles without login. | 2026-02-14 | 2026-07-05 | 901 |
| [xint](https://github.com/0xNyk/xint) | CLI + skill + MCP | X / Twitter; Multi-model | Searches, monitors, and exports public X data for agent-assisted investigations. | 2026-02-14 | 2026-07-16 | 216 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [X Archive RAG](https://github.com/mameshivaa/x-archive-rag) | RAG system | X / Twitter; Generic AI agents | Indexes exported X data for local semantic search and retrieval-augmented analysis. | 2026-05-26 | 2026-06-18 | 0 |

<a id="facebook"></a>

## Facebook <sup>0 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|

<a id="instagram"></a>

## Instagram <sup>6 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [Osintgram](https://github.com/Datalux/Osintgram) | Python | Instagram | Provides an interactive interface for collecting information from Instagram profiles. | 2019-06-07 | 2025-08-25 | 13,572 |
| [Instaloader](https://github.com/instaloader/instaloader) | Python | Instagram | Downloads Instagram posts, captions, profile data, and related metadata. | 2016-06-15 | 2026-07-13 | 12,890 |
| [Instagram Monitor](https://github.com/misiektoja/instagram_monitor) | Python | Instagram | Tracks public Instagram profile changes, activity, and captured content. | 2024-04-25 | 2026-07-01 | 1,112 |
| [Osintgraph](https://github.com/XD-MHLOO/Osintgraph) | Python | Instagram | Maps Instagram followers and relationships in Neo4j for network analysis. | 2025-04-30 | 2026-05-10 | 803 |
| [SoIG](https://github.com/yezz123/SoIG) | Python | Instagram | Retrieves selected public information associated with an Instagram account. | 2020-06-08 | 2026-06-28 | 382 |
| [insto](https://github.com/subzeroid/insto) | Python | Instagram | Collects Instagram profile, media, relationship, and timeline data through interchangeable backends. | 2026-04-26 | 2026-06-20 | 54 |

<a id="linkedin"></a>

## LinkedIn <sup>5 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [linkedin2username](https://github.com/initstring/linkedin2username) | Python | LinkedIn | Generates possible corporate usernames from public LinkedIn employee data. | 2018-02-22 | 2026-05-20 | 1,770 |
| [CrossLinked](https://github.com/m8sec/CrossLinked) | Python | LinkedIn | Extracts employee names from public LinkedIn search results. | 2019-05-16 | 2024-11-26 | 1,572 |
| [LinkedInDumper](https://github.com/l4rm4nd/LinkedInDumper) | Python | LinkedIn | Extracts company employee records through LinkedIn endpoints. | 2022-10-17 | 2026-07-15 | 602 |
| [LinkedIn OSINT Toolkit](https://github.com/michaelelizarov/linkedin-osint-toolkit) | Python | LinkedIn | Discovers companies and employees, classifies roles, and builds organization views. | 2026-02-16 | 2026-02-16 | 34 |
| [LinkedIn Recon Skill](https://github.com/Kewanvk/linkedin-recon-skill) | Skill | LinkedIn; Claude Code + Codex | Maps public hiring networks and organizational relationships from LinkedIn evidence. | 2026-05-08 | 2026-05-25 | 0 |

<a id="reddit"></a>

## Reddit <sup>3 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [Arctic Shift](https://github.com/ArthurHeitmann/arctic_shift) | TypeScript | Reddit | Provides searchable Reddit archives through data dumps, an API, and a web interface. | 2023-08-03 | 2026-07-12 | 1,240 |
| [Universal Reddit Scraper](https://github.com/JosephLai241/URS) | Python | Reddit | Scrapes and archives Reddit submissions, comments, and user activity. | 2019-03-20 | 2026-07-11 | 1,008 |
| [Reddit Research MCP](https://github.com/king-of-the-grackles/reddit-research-mcp) | MCP server | Reddit; Model-agnostic (MCP) | Supports structured Reddit discovery, thread collection, and community research. | 2025-08-12 | 2026-07-02 | 219 |

<a id="telegram"></a>

## Telegram <sup>13 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [Telegram Phone Number Checker](https://github.com/bellingcat/telegram-phone-number-checker) | Python | Telegram | Checks whether supplied phone numbers are connected to Telegram accounts. | 2021-02-17 | 2026-01-06 | 1,743 |
| [Informer](https://github.com/paulpierre/informer) | Python | Telegram | Collects and indexes Telegram channel and group activity. | 2019-12-09 | 2025-10-20 | 1,639 |
| [Telerecon](https://github.com/sockysec/Telerecon) | Python | Telegram | Provides a modular framework for researching Telegram entities. | 2023-08-30 | 2024-04-22 | 1,311 |
| [Telepathy Community](https://github.com/prose-intelligence-ltd/Telepathy-Community) | Python | Telegram | Collects and analyzes public Telegram chat data. | 2022-01-17 | 2024-07-12 | 1,228 |
| [Tosint](https://github.com/drego85/tosint) | Python | Telegram | Extracts Telegram bot, chat, and user information from tokens and identifiers. | 2021-07-26 | 2026-03-25 | 837 |
| [TeleTracker](https://github.com/tsale/TeleTracker) | Python | Telegram | Collects Telegram channel information and supports repeatable investigation tasks. | 2024-01-15 | 2024-04-29 | 535 |
| [Maltego Telegram](https://github.com/vognik/maltego-telegram) | Python | Telegram | Adds Maltego transforms for Telegram channels, groups, users, and messages. | 2024-11-04 | 2026-01-27 | 515 |
| [telegram-tracker](https://github.com/estebanpdl/telegram-tracker) | Python | Telegram | Exports channel details and posts from selected Telegram channels. | 2022-04-06 | 2026-04-20 | 381 |
| [TeleGraphite](https://github.com/hamodywe/telegram-scraper-TeleGraphite) | Python | Telegram | Collects Telegram channel posts and exports them as JSON. | 2025-04-12 | 2025-04-15 | 274 |
| [Telegram Similar Channels](https://github.com/SocialLinks-IO/telegram-similar-channels) | Python | Telegram | Finds related Telegram channels through CLI and Maltego interfaces. | 2023-12-07 | 2024-04-10 | 190 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Telegram Archive](https://github.com/GeiserX/Telegram-Archive) | Python | Telegram | Creates incremental local archives of Telegram chats, media, and message history. | 2025-11-25 | 2026-07-15 | 158 |
| [Telegram OSINT Polo](https://github.com/Ironship/TelegramOSINTPolo) | Python | Telegram | Downloads Telegram feed posts for local review and assisted analysis. | 2025-03-04 | 2026-03-12 | 55 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Telegram MCP TDLib](https://github.com/tolboy/telegram-mcp-tdlib) | MCP server | Telegram; Model-agnostic (MCP) | Exposes Telegram searches, chats, messages, and public content to MCP clients through TDLib. | 2026-07-04 | 2026-07-15 | 0 |

<a id="tiktok"></a>

## TikTok <sup>0 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|

<a id="youtube"></a>

## YouTube <sup>4 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | Python | YouTube + other video sites | Downloads public video, audio, subtitles, comments, and metadata from supported platforms. | 2020-10-26 | 2026-07-14 | 178,311 |
| [Yark](https://github.com/Owez/yark) | Python | YouTube | Archives public YouTube channels, videos, and metadata for local analysis. | 2022-08-16 | 2025-12-17 | 2,180 |
| [tubeup](https://github.com/bibanon/tubeup) | Python | YouTube + yt-dlp-supported sites | Archives online video and metadata to the Internet Archive through yt-dlp. | 2016-02-05 | 2026-05-08 | 509 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [YouTube Research MCP](https://github.com/coyaSONG/youtube-mcp-server) | MCP server | YouTube; Model-agnostic (MCP) | Exposes YouTube videos, channels, search results, comments, and transcripts through MCP. | 2025-03-31 | 2026-07-14 | 15 |

<a id="snapchat"></a>

## Snapchat <sup>1 project</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [SnapIntel](https://github.com/Kr0wZ/SnapIntel) | Python | Snapchat | Retrieves public account details associated with Snapchat usernames. | 2021-03-02 | 2026-03-24 | 325 |

<a id="whatsapp"></a>

## WhatsApp <sup>1 project</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [WhatsOSINT](https://github.com/HackUnderway/WhatsOSINT) | Python | WhatsApp | Retrieves public WhatsApp account details associated with a number. | 2024-11-19 | 2026-07-10 | 310 |

<a id="steam"></a>

## Steam <sup>3 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [steam-osint](https://github.com/matiash26/steam-osint) | Python | Steam | Finds mutual friends between public Steam profiles. | 2022-03-12 | 2026-07-01 | 92 |
| [Steam Monitor](https://github.com/misiektoja/steam_monitor) | Python | Steam | Tracks public Steam player activity, game sessions, and status changes. | 2024-04-25 | 2026-06-26 | 50 |
| [SteamReveal](https://github.com/Berchez/SteamReveal) | TypeScript | Steam | Analyzes Steam profiles for close contacts and possible location clues. | 2024-02-20 | 2026-05-06 | 25 |

<a id="github"></a>

## GitHub <sup>13 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Gitleaks](https://github.com/gitleaks/gitleaks) | Go | Git, GitHub | Scans Git repositories and other inputs for hardcoded secrets and credentials. | 2018-01-27 | 2026-07-01 | 28,170 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [TruffleHog](https://github.com/trufflesecurity/trufflehog) | Go | GitHub, GitLab, Git and other sources | Finds, verifies, and analyzes exposed credentials across supported code and storage sources. | 2016-12-31 | 2026-07-16 | 27,074 |
| [github-dorks](https://github.com/techgaun/github-dorks) | Python | GitHub | Runs GitHub search queries intended to locate exposed sensitive data. | 2015-10-11 | 2025-10-05 | 3,243 |
| [gitGraber](https://github.com/hisxo/gitGraber) | Python | GitHub | Monitors public GitHub activity for exposed credentials and service tokens. | 2019-09-04 | 2024-07-19 | 2,316 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Bellingcat Octosuite](https://github.com/bellingcat/octosuite) | Python | GitHub | Collects and analyzes public GitHub repository, user, organization, and activity data. | 2022-02-24 | 2026-02-28 | 1,891 |
| [GitGot](https://github.com/BishopFox/GitGot) | Python | GitHub | Searches public GitHub data for exposed secrets using feedback-driven queries. | 2019-06-14 | 2024-03-07 | 1,567 |
| [git-hound](https://github.com/tillson/git-hound) | Go | GitHub | Searches GitHub at scale for exposed secrets and dork matches. | 2019-07-16 | 2025-11-20 | 1,441 |
| [GitFive](https://github.com/mxrch/GitFive) | Python | GitHub | Correlates public GitHub account data for identity-focused investigations. | 2022-10-05 | 2025-10-04 | 1,004 |
| [GitSint](https://github.com/N0rz3/GitSint) | Python | GitHub | Collects public intelligence about GitHub users and repositories. | 2023-04-26 | 2026-06-28 | 243 |
| [Gitxray](https://github.com/kulkansecurity/gitxray) | Python | GitHub | Uses public GitHub APIs for account, repository, and contribution analysis. | 2024-08-06 | 2026-01-09 | 182 |
| [Shotstars](https://github.com/snooppr/shotstars) | Python | GitHub | Analyzes repository star history and indicators of artificial activity. | 2024-05-25 | 2026-06-04 | 111 |
| [GitRecon](https://github.com/atiilla/gitrecon) | JavaScript | GitHub | Scans a GitHub user's repositories for exposed names and email addresses. | 2023-09-03 | 2025-12-29 | 55 |
| [GitHub Monitor](https://github.com/misiektoja/github_monitor) | Python | GitHub | Tracks GitHub profile and repository activity with change notifications. | 2024-05-11 | 2026-05-26 | 52 |

<a id="discord"></a>

## Discord <sup>4 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter) | C# | Discord | Exports accessible Discord message history and rich media to local files. | 2017-07-12 | 2026-07-14 | 11,594 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Discord History Tracker](https://github.com/chylex/Discord-History-Tracker) | C# | Discord | Saves accessible Discord chat history for offline preservation and review. | 2016-10-22 | 2026-01-29 | 579 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [discord-urls-extractor](https://github.com/TheTechRobo/discord-urls-extractor) | Rust | Discord | Extracts URLs and media references from supported Discord archive formats. | 2021-11-21 | 2024-12-19 | 21 |
| <img src=".github/assets/new-dot.svg" width="6" height="6" alt=""> [Discord Inspector](https://github.com/Euronymou5/Discord-Inspector) | Python | Discord | Retrieves public user, server, and application metadata from Discord identifiers. | 2024-12-03 | 2024-12-05 | 6 |

---

<p align="right"><a href="#top">Back to top ↑</a></p>
