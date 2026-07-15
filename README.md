<a id="top"></a>

<div align="center">
  <h1>OSINT Tools Radar</h1>
  <p>An automatically updated catalogue of open-source OSINT tools and the public source-code repositories that maintain them, organized by investigation target, platform, and emerging capability.</p>
  <p>
    <a href="#table-of-contents"><img alt="Open-source tools: 256" src="https://img.shields.io/badge/open--source_tools-256-0969da?style=flat-square"></a>
    <a href="EMERGING.md"><img alt="Emerging projects: 74" src="https://img.shields.io/badge/emerging-74-bf8700?style=flat-square"></a>
    <a href="#social-platforms"><img alt="Social platform entries: 104" src="https://img.shields.io/badge/social_platforms-104-8250df?style=flat-square"></a>
    <a href="AGENTIC.md"><img alt="Agentic integrations: 108" src="https://img.shields.io/badge/agentic_integrations-108-d1242f?style=flat-square"></a>
    <a href="osint-repositories.csv"><img alt="Source repositories: 420" src="https://img.shields.io/badge/source_repositories-420-1f883d?style=flat-square"></a>
    <img alt="Catalogue entries: 438" src="https://img.shields.io/badge/catalogue_entries-438-8250df?style=flat-square">
    <img alt="Last verified: 2026-07-15" src="https://img.shields.io/badge/last_verified-2026--07--15-1f883d?style=flat-square">
  </p>
  <p><strong><a href="README.md">OSINT Tools Radar</a> · <a href="EMERGING.md">Emerging Projects</a> · <a href="AGENTIC.md">Agentic AI OSINT</a> · <a href="osint-repositories.csv">Open-source Repository Database</a></strong></p>
</div>

## About this catalogue

OSINT Tools Radar is a repository-first catalogue of open-source OSINT software. Every published entry represents a public source-code repository containing an identifiable tool or integration with a practical investigative use case. Project names link directly to the repositories that contain their implementations.

> [!IMPORTANT]
> Only implementation-bearing repositories with publicly accessible source code are included. Closed-source services, commercial tools without public code, link collections, prompt-only lists, datasets, and repository stubs are excluded.

> [!NOTE]
> Public source-code access and open-source licensing are separate checks. License metadata is recorded in the repository database when verified; blank, missing, or `NOASSERTION` values require manual review and do not by themselves prove open-source status.

> [!NOTE]
> Repository metadata was last verified on **2026-07-15**. Star counts are a point-in-time snapshot and may change after verification.

<a id="table-of-contents"></a>

## Table of contents

- **Identity**
  - [Person](#person) <sup>2 projects</sup>
  - [Username](#username) <sup>2 projects</sup>
  - [Email](#email) <sup>13 projects</sup>
  - [Phone](#phone) <sup>6 projects</sup>
- **Infrastructure**
  - [Domain](#domain) <sup>22 projects</sup>
  - [IP Address](#ip-address) <sup>11 projects</sup>
  - [URL](#url) <sup>24 projects</sup>
- **Media and geography**
  - [Image](#image) <sup>36 projects</sup>
  - [Location](#location) <sup>5 projects</sup>
- **Organizations and assets**
  - [Company](#company) <sup>4 projects</sup>
  - [Cryptocurrency](#cryptocurrency) <sup>6 projects</sup>
- **Cross-target tooling**
  - [General](#general) <sup>21 projects</sup>
- **Social platforms**
  - [Cross-platform](#cross-platform) <sup>19 projects</sup>
  - [X and Twitter](#x-and-twitter) <sup>7 projects</sup>
  - [Facebook](#facebook) <sup>2 projects</sup>
  - [Instagram](#instagram) <sup>9 projects</sup>
  - [LinkedIn](#linkedin) <sup>8 projects</sup>
  - [Reddit](#reddit) <sup>5 projects</sup>
  - [Telegram](#telegram) <sup>20 projects</sup>
  - [TikTok](#tiktok) <sup>2 projects</sup>
  - [YouTube](#youtube) <sup>3 projects</sup>
  - [Snapchat](#snapchat) <sup>2 projects</sup>
  - [WhatsApp](#whatsapp) <sup>2 projects</sup>
  - [Steam](#steam) <sup>3 projects</sup>
  - [GitHub](#github) <sup>16 projects</sup>
  - [Discord](#discord) <sup>6 projects</sup>
- [Catalogue automation](#catalogue-automation)
- [Reviewed source collections](#reviewed-source-collections)
- [Metadata conventions](#metadata-conventions)
- [Emerging projects](EMERGING.md) <sup>74 projects</sup>
- [Agentic AI OSINT](AGENTIC.md) <sup>108 projects</sup>
- [Complete repository database](osint-repositories.csv) <sup>420 unique repositories</sup>

---

<a id="person"></a>

## 👤 Person <sup>2 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [GHunt](https://github.com/mxrch/GHunt) | Python | - | Collects public information associated with Google accounts and identifiers. | 2020-10-02 | 2026-04-10 | 19,216 |
| [Trape](https://github.com/jofpin/trape) | Python | - | Correlates browser session details for people-focused online investigations. | 2017-10-31 | 2024-06-20 | 8,870 |

<a id="username"></a>

## 🪪 Username <sup>2 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [username-anarchy](https://github.com/urbanadventurer/username-anarchy) | Ruby | - | Generates likely username permutations from names and naming patterns. | 2012-11-07 | 2024-09-20 | 1,431 |
| [vesper](https://github.com/krishpranav/vesper) | Rust | - | Performs lightweight username checks across online services. | 2021-06-20 | 2026-06-15 | 321 |

<a id="email"></a>

## ✉️ Email <sup>13 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [Holehe](https://github.com/megadose/holehe) | Python | - | Checks whether an email address is registered with supported online services. | 2020-06-25 | 2024-09-10 | 11,687 |
| [Mosint](https://github.com/alpkeskin/mosint) | Go | - | Automates multiple public checks for an email address. | 2020-09-27 | 2024-02-02 | 5,938 |
| [h8mail](https://github.com/khast3x/h8mail) | Python | - | Searches breach sources and local datasets for email-related records. | 2018-06-15 | 2023-08-15 | 5,091 |
| [pwnedOrNot](https://github.com/thewhiteh4t/pwnedOrNot) | Python | - | Searches breach data for passwords associated with an email address. | 2018-05-25 | 2026-03-28 | 2,597 |
| [WhatBreach](https://github.com/Ekultek/WhatBreach) | Python | - | Finds breach, paste, and database references linked to an email address. | 2019-04-19 | 2025-08-14 | 1,620 |
| [Buster](https://github.com/sham00n/buster) | Python | - | Runs multiple email reconnaissance and account discovery checks. | 2019-06-03 | 2020-03-26 | 1,352 |
| [Zehef](https://github.com/N0rz3/Zehef) | Python | - | Aggregates public information associated with an email address. | 2023-06-13 | 2024-11-13 | 1,039 |
| [iKy](https://github.com/kennbroorg/iKy) | Python | - | Builds profiles and timelines from email-based investigation modules. | 2018-12-14 | 2026-07-14 | 963 |
| [mailcat](https://github.com/sharsil/mailcat) | Python | - | Finds existing email addresses derived from a nickname. | 2021-08-20 | 2026-05-24 | 910 |
| [Poastal](https://github.com/jakecreps/poastal) | Python | - | Combines email validation, enrichment, and account discovery checks. | 2023-03-24 | 2024-04-08 | 600 |
| [MailFinder](https://github.com/mishakorzik/MailFinder) | Python | - | Generates and checks candidate email addresses from a person's name. | 2021-11-07 | 2025-11-16 | 571 |
| [Email-Osint](https://github.com/KanekiWeb/Email-Osint) | Python | - | Collects basic public information associated with an email address. | 2021-03-12 | 2022-11-14 | 130 |
| [glit](https://github.com/shadawck/glit) | Rust | - | Extracts contributor email addresses from Git repositories and organizations. | 2022-11-14 | 2024-05-01 | 58 |

<a id="phone"></a>

## 📞 Phone <sup>6 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [PhoneInfoga](https://github.com/sundowndev/phoneinfoga) | Go | - | Collects and correlates publicly available information about phone numbers. | 2018-10-25 | 2026-01-06 | 17,010 |
| [email2phonenumber](https://github.com/martinvigo/email2phonenumber) | Python | - | Uses account recovery workflows to derive phone number clues from an email. | 2019-03-17 | 2024-07-26 | 2,703 |
| [Moriarty Project](https://github.com/AzizKpln/Moriarty-Project) | Python | - | Collects carrier, region, and public search information for phone numbers. | 2020-05-08 | 2024-07-13 | 2,023 |
| [Ignorant](https://github.com/megadose/ignorant) | Python | - | Checks whether a phone number is registered with supported online services. | 2021-03-24 | 2024-07-27 | 1,920 |
| [Phunter](https://github.com/N0rz3/Phunter) | Python | - | Aggregates several public phone number investigation methods. | 2023-12-30 | 2024-04-06 | 1,089 |
| [odnoklassniki-checker](https://github.com/OSINT-mindset/odnoklassniki-checker) | Python | - | Looks for public OK.ru account data using a phone number or email. | 2022-10-15 | 2024-10-02 | 20 |

<a id="domain"></a>

## 🌐 Domain <sup>22 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [theHarvester](https://github.com/laramies/theHarvester) | Python | - | Collects names, email addresses, subdomains, and hosts from public sources. | 2011-01-01 | 2026-07-06 | 16,792 |
| [Amass](https://github.com/owasp-amass/amass) | Go | - | Maps external assets and discovers domains from multiple data sources. | 2018-07-10 | 2026-04-17 | 14,836 |
| [Subfinder](https://github.com/projectdiscovery/subfinder) | Go | - | Enumerates subdomains using passive online sources. | 2018-03-31 | 2026-07-10 | 14,010 |
| [BBOT](https://github.com/blacklanternsecurity/bbot) | Python | - | Recursively discovers internet-facing assets through modular scan events. | 2022-03-12 | 2026-07-15 | 10,153 |
| [OneForAll](https://github.com/shmilylty/OneForAll) | Python | - | Combines numerous sources and methods for subdomain discovery. | 2018-12-10 | 2026-05-11 | 9,922 |
| [reconFTW](https://github.com/six2dez/reconftw) | Shell | - | Orchestrates domain reconnaissance, asset collection, and follow-up checks. | 2020-12-30 | 2026-06-29 | 7,842 |
| [dnstwist](https://github.com/elceef/dnstwist) | Python | - | Generates and evaluates look-alike domains for phishing and impersonation research. | 2015-06-11 | 2025-04-15 | 5,706 |
| [Knockpy](https://github.com/guelfoweb/knockpy) | Python | - | Enumerates subdomains and resolves related DNS information. | 2014-02-11 | 2026-02-19 | 4,171 |
| [Findomain](https://github.com/Findomain/Findomain) | Rust | - | Discovers and monitors domains and subdomains from multiple sources. | 2019-04-14 | 2026-05-06 | 3,769 |
| [assetfinder](https://github.com/tomnomnom/assetfinder) | Go | - | Finds domains and subdomains related to a supplied domain. | 2019-06-23 | 2024-06-07 | 3,638 |
| [FinalRecon](https://github.com/thewhiteh4t/FinalRecon) | Python | - | Collects headers, DNS records, subdomains, and related web intelligence. | 2019-03-28 | 2026-06-01 | 2,842 |
| [dnsx](https://github.com/projectdiscovery/dnsx) | Go | - | Runs high-volume DNS queries and filters resolved records. | 2020-11-12 | 2026-07-13 | 2,807 |
| [Sudomy](https://github.com/screetsec/Sudomy) | Shell | - | Automates subdomain enumeration and supporting domain reconnaissance tasks. | 2019-07-26 | 2024-06-27 | 2,414 |
| [SubDomainizer](https://github.com/nsonaniya2010/SubDomainizer) | Python | - | Finds subdomains and exposed data referenced in JavaScript files. | 2018-11-19 | 2026-07-14 | 1,875 |
| [domain-digger](https://github.com/wotschofsky/domain-digger) | TypeScript | - | Provides a web toolkit for DNS, certificate, hosting, and domain analysis. | 2021-07-29 | 2026-07-15 | 1,178 |
| [dnsgen](https://github.com/AlephNullSK/dnsgen) | Python | - | Generates likely DNS name permutations for further discovery. | 2019-09-24 | 2025-01-03 | 1,074 |
| [openSquat](https://github.com/atenreiro/opensquat) | Python | - | Detects newly registered look-alike domains associated with brands. | 2020-05-04 | 2026-04-27 | 977 |
| [subscraper](https://github.com/m8sec/subscraper) | Python | - | Enumerates subdomains and related targets from public sources. | 2018-09-27 | 2024-06-19 | 969 |
| [censys-subdomain-finder](https://github.com/christophetd/censys-subdomain-finder) | Python | - | Uses Censys certificate data to identify subdomains. | 2018-01-15 | 2025-05-01 | 842 |
| [Subdominator](https://github.com/RevoltSecurities/Subdominator) | Python | - | Performs low-impact subdomain discovery across multiple sources. | 2023-07-24 | 2026-06-21 | 791 |
| [ct-exposer](https://github.com/chris408/ct-exposer) | Python | - | Extracts subdomains from public Certificate Transparency logs. | 2018-09-04 | 2022-08-16 | 486 |
| [Columbus](https://github.com/elmasy-com/columbus) | Go | - | Provides subdomain discovery, an API, and historical DNS results. | 2022-08-23 | 2023-08-18 | 34 |

<a id="ip-address"></a>

## 🖧 IP Address <sup>11 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [IVRE](https://github.com/ivre/ivre) | Python | - | Builds searchable network intelligence from active and passive observations. | 2014-09-12 | 2026-07-05 | 4,083 |
| [Uncover](https://github.com/projectdiscovery/uncover) | Go | - | Queries internet search engines for exposed hosts matching a search. | 2022-03-02 | 2026-07-10 | 3,016 |
| [reconspider](https://github.com/bhavsec/reconspider) | Python | - | Collects information about IP addresses, websites, emails, and organizations. | 2018-12-15 | 2023-09-26 | 2,734 |
| [IPinfo CLI](https://github.com/ipinfo/cli) | Go | - | Queries IP geolocation, ASN, privacy, and network data from the command line. | 2020-10-23 | 2026-04-28 | 2,033 |
| [asn](https://github.com/nitefood/asn) | Shell | - | Reports ASN, BGP, geolocation, reputation, and routing information for IPs. | 2020-07-22 | 2026-06-22 | 1,909 |
| [Metabigor](https://github.com/j3ssie/metabigor) | Go | - | Correlates IP, ASN, domain, and network data without mandatory API keys. | 2019-05-24 | 2026-07-03 | 1,630 |
| [OSINT-SPY](https://github.com/SharadKumar97/OSINT-SPY) | Python | - | Runs public intelligence checks for IPs, domains, emails, and organizations. | 2017-08-02 | 2023-10-23 | 1,532 |
| [Harpoon](https://github.com/Te-k/harpoon) | Python | - | Provides command-line queries for open-source and threat intelligence indicators. | 2017-09-25 | 2026-05-18 | 1,288 |
| [HostHunter](https://github.com/SpiderLabs/HostHunter) | Python | - | Discovers hostnames associated with supplied IP addresses. | 2018-05-17 | 2023-03-30 | 1,168 |
| [asnmap](https://github.com/projectdiscovery/asnmap) | Go | - | Maps organizations and ASNs to their advertised network ranges. | 2022-09-29 | 2026-07-13 | 1,094 |
| [pygreynoise](https://github.com/GreyNoise-Intelligence/pygreynoise) | Python | - | Queries GreyNoise observations and classifications for internet-scanning IPs. | 2017-12-07 | 2026-07-09 | 177 |

<a id="url"></a>

## 🔗 URL <sup>24 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [Web-Check](https://github.com/lissy93/web-check) | TypeScript | - | Produces a broad technical and open-source intelligence report for a website. | 2023-06-25 | 2026-07-11 | 34,152 |
| [changedetection.io](https://github.com/dgtlmoon/changedetection.io) | Python | - | Monitors web pages and records content changes over time. | 2021-01-27 | 2026-07-13 | 32,316 |
| [SingleFile](https://github.com/gildas-lormeau/SingleFile) | JavaScript | - | Saves a complete web page as one file for preservation and later analysis. | 2010-09-12 | 2026-02-24 | 21,818 |
| [Photon](https://github.com/s0md3v/Photon) | Python | - | Crawls a supplied URL to collect links and related open-source data. | 2018-03-30 | 2026-02-10 | 13,036 |
| [httpx](https://github.com/projectdiscovery/httpx) | Go | - | Probes web targets at scale and reports HTTP, TLS, technology, and response metadata. | 2020-05-28 | 2026-07-13 | 10,169 |
| [hakrawler](https://github.com/hakluke/hakrawler) | Go | - | Crawls web applications to discover endpoints, assets, and linked resources. | 2019-12-15 | 2024-12-21 | 5,090 |
| [gau](https://github.com/lc/gau) | Go | - | Collects known URLs from public archives and threat intelligence sources. | 2020-02-25 | 2024-10-28 | 5,033 |
| [TorBot](https://github.com/DedSecInside/TorBot) | Python | - | Crawls and indexes links discovered across Tor services. | 2017-05-17 | 2026-01-08 | 4,348 |
| [Cariddi](https://github.com/edoardottt/cariddi) | Go | - | Crawls domains and extracts endpoints, secrets, tokens, and file references. | 2021-04-27 | 2026-07-03 | 3,456 |
| [pagodo](https://github.com/opsdisk/pagodo) | Python | - | Automates Google dork collection and searches against a target. | 2016-08-19 | 2025-12-01 | 3,363 |
| [waybackpack](https://github.com/jsvine/waybackpack) | Python | - | Downloads archived versions of a URL from the Wayback Machine. | 2016-04-11 | 2024-05-15 | 3,214 |
| [ParamSpider](https://github.com/devanshbatham/ParamSpider) | Python | - | Mines web archives for URLs containing useful parameters. | 2020-04-12 | 2026-03-07 | 3,131 |
| [waymore](https://github.com/xnl-h4ck3r/waymore) | Python | - | Collects archived URLs and responses from several public sources. | 2022-06-24 | 2026-06-11 | 2,690 |
| [Mitaka](https://github.com/ninoseki/mitaka) | TypeScript | - | Adds browser searches for URLs, hashes, IP addresses, and other indicators. | 2018-02-09 | 2026-06-16 | 1,821 |
| [BlackWidow](https://github.com/1N3/BlackWidow) | Python | - | Crawls a web application to collect intelligence and identify reachable paths. | 2018-01-06 | 2026-04-17 | 1,811 |
| [OnionSearch](https://github.com/megadose/OnionSearch) | Python | - | Queries several Tor search engines and collects matching onion URLs. | 2020-03-18 | 2024-08-08 | 1,734 |
| [urlhunter](https://github.com/utkusen/urlhunter) | Go | - | Finds URLs exposed through public URL-shortening services. | 2020-11-21 | 2025-01-23 | 1,684 |
| [darkdump](https://github.com/josh0xA/darkdump) | Python | - | Searches and collects public results from dark web sources. | 2021-02-11 | 2026-04-08 | 1,640 |
| [GooFuzz](https://github.com/m3n0sd0n4ld/GooFuzz) | Shell | - | Uses search-engine results to enumerate web paths, files, and parameters. | 2022-06-17 | 2025-12-21 | 1,577 |
| [FavFreak](https://github.com/devanshbatham/FavFreak) | Python | - | Creates favicon hashes for finding related websites through internet search engines. | 2020-07-03 | 2023-08-29 | 1,293 |
| [uDork](https://github.com/m3n0sd0n4ld/uDork) | Shell | - | Automates advanced search queries for exposed web information. | 2019-09-09 | 2022-06-20 | 849 |
| [xurlfind3r](https://github.com/hueristiq/xurlfind3r) | Go | - | Discovers URLs for a domain through passive public sources. | 2021-05-13 | 2026-02-23 | 708 |
| [waybackpy](https://github.com/akamhy/waybackpy) | Python | - | Provides a command-line and library interface to Wayback Machine APIs. | 2020-05-02 | 2022-03-15 | 594 |
| [TheScrapper](https://github.com/champmq/TheScrapper) | Python | - | Crawls websites to extract email addresses, phone numbers, and social profile links. | 2021-05-07 | 2026-05-29 | 364 |

<a id="image"></a>

## 🖼️ Image <sup>36 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [face_recognition](https://github.com/ageitgey/face_recognition) | Python | Python and CLI | Recognizes and compares faces through a Python API and command-line interface. | 2017-03-03 | 2026-06-25 | 56,581 |
| [Frigate](https://github.com/blakeblackshear/frigate) | TypeScript | IP and RTSP cameras | Records and analyzes local IP-camera streams with real-time object detection, tracking, and search. | 2019-01-26 | 2026-07-15 | 34,355 |
| [InsightFace](https://github.com/deepinsight/insightface) | Python | Python, C++, and desktop GUI | Performs face detection, alignment, recognition, and embedding analysis across multiple runtimes. | 2017-09-01 | 2026-05-23 | 29,249 |
| [DeepFace](https://github.com/serengil/deepface) | Python | - | Performs face verification, recognition, search, and facial attribute analysis. | 2020-02-08 | 2026-06-29 | 23,109 |
| [CompreFace](https://github.com/exadel-inc/CompreFace) | Java | Self-hosted REST API | Provides self-hosted face detection, recognition, verification, and similarity search through a REST API. | 2020-07-06 | 2024-10-05 | 8,135 |
| [ZoneMinder](https://github.com/ZoneMinder/zoneminder) | PHP | IP, USB, and analog cameras | Monitors, records, and reviews IP, USB, and analog camera feeds. | 2013-04-12 | 2026-07-14 | 5,882 |
| [EagleEye](https://github.com/ThoughtfulDev/EagleEye) | Python | Instagram, Facebook, YouTube, and X/Twitter | Uses face recognition and reverse-image search to locate potentially related social profiles. | 2018-02-17 | 2024-04-25 | 5,144 |
| [ExifTool](https://github.com/exiftool/exiftool) | Perl | - | Reads and writes metadata embedded in images and other file formats. | 2018-05-09 | 2026-05-27 | 4,871 |
| [Torchreid](https://github.com/KaiyangZhou/deep-person-reid) | Python | Images and camera footage | Re-identifies people across images and camera views with pretrained models and training tools. | 2018-03-11 | 2026-01-09 | 4,867 |
| [motionEye](https://github.com/motioneye-project/motioneye) | Python | IP and local cameras | Provides web-based multi-camera monitoring, motion detection, recording, and review. | 2015-08-30 | 2026-07-14 | 4,633 |
| [FastReID](https://github.com/JDAI-CV/fast-reid) | Python | Images and camera footage | Provides models and inference tooling for person re-identification across camera imagery. | 2018-06-06 | 2024-07-30 | 3,966 |
| [ImageHash](https://github.com/JohannesBuchner/imagehash) | Python | - | Calculates perceptual image hashes for similarity and duplicate-image comparison. | 2013-03-02 | 2025-04-17 | 3,852 |
| [Search by Image](https://github.com/dessant/search-by-image) | JavaScript | Chrome, Edge, and Safari | Sends images to multiple reverse-image search engines from Chrome, Edge, and Safari. | 2017-06-17 | 2026-06-27 | 3,595 |
| [Viseron](https://github.com/roflcoopter/viseron) | Python | CCTV and IP cameras | Analyzes local camera feeds with motion, object, face, and license-plate detection. | 2020-08-30 | 2026-07-15 | 3,281 |
| [Human](https://github.com/vladmandic/human) | TypeScript | Browser and Node.js | Performs face detection, recognition, matching, and broader human analysis in browsers and Node.js. | 2020-10-11 | 2025-12-13 | 3,207 |
| [image-match](https://github.com/rhsimplex/image-match) | Python | - | Performs scalable perceptual image matching against indexed images. | 2016-03-08 | 2022-12-06 | 2,976 |
| [DeepCamera](https://github.com/SharpAI/DeepCamera) | JavaScript | CCTV and IP cameras | Analyzes camera feeds with local vision models, face recognition, re-identification, and configurable AI skills. | 2019-03-05 | 2026-06-18 | 2,908 |
| [RetinaFace](https://github.com/serengil/retinaface) | Python | - | Detects, aligns, and extracts faces from images for downstream comparison workflows. | 2021-04-25 | 2026-06-01 | 2,011 |
| [Photonix](https://github.com/photonixapp/photonix) | Python | - | Organizes and searches local photo collections using faces, objects, locations, and visual attributes. | 2017-03-07 | 2026-07-14 | 1,953 |
| [unblink](https://github.com/zapdos-labs/unblink) | Go | RTSP and MJPEG cameras | Uses vision-language models to monitor camera feeds and search recorded frames with natural language. | 2025-11-05 | 2026-03-09 | 1,469 |
| [HomeGallery](https://github.com/xemle/home-gallery) | JavaScript | Self-hosted photo and video collections | Indexes local photos and videos for reverse-image lookup, face search, and semantic discovery. | 2020-12-22 | 2026-06-25 | 1,169 |
| [FaceAPI](https://github.com/vladmandic/face-api) | TypeScript (archived) | Browser and Node.js | Provides browser and Node.js face detection, recognition, description, and attribute analysis. | 2020-08-18 | 2025-02-05 | 1,079 |
| [Kerberos Agent](https://github.com/kerberos-io/agent) | Go | RTSP cameras | Runs local video monitoring, recording, motion analysis, and event capture for RTSP camera streams. | 2020-08-12 | 2026-07-15 | 1,073 |
| [camera.ui](https://github.com/cameraui/camera.ui) | TypeScript | CCTV and IP cameras | Records, monitors, and searches local camera feeds with on-device detection workflows. | 2021-10-27 | 2026-07-15 | 1,063 |
| [clearcam](https://github.com/roryclear/clearcam) | Python | RTSP and HLS cameras | Adds object detection, tracking, notifications, summaries, and search to security-camera feeds. | 2025-01-04 | 2026-07-15 | 947 |
| [ExifLooter](https://github.com/aydinnyunus/exiflooter) | Go | - | Finds geolocation metadata in local and remote images and maps the results. | 2022-07-30 | 2023-12-28 | 494 |
| [gallery-dl](https://codeberg.org/mikf/gallery-dl) | Python | Cross-platform image sites | Downloads image galleries and media collections from supported websites. | 2026-03-24 | 2026-07-15 | 380 |
| [SentryShot](https://github.com/SentryShot/sentryshot) | Rust | IP and RTSP cameras | Records camera streams and applies local object detection through a web video-management interface. | 2023-10-29 | 2026-04-27 | 356 |
| [VibeNVR](https://github.com/spupuz/VibeNVR) | JavaScript | IP and RTSP cameras | Provides privacy-focused local camera recording and monitoring without a cloud dependency. | 2026-01-15 | 2026-07-15 | 325 |
| [GVision](https://github.com/GONZOsint/gvision) | Python | - | Uses image analysis to detect landmarks and related web entities. | 2023-03-29 | 2024-12-08 | 271 |
| [clip-image-search](https://github.com/kingyiusuen/clip-image-search) | Python | Local image collections | Searches local image collections by reference image or text using CLIP embeddings. | 2021-08-24 | 2022-01-15 | 268 |
| [goris](https://github.com/tanaikech/goris) | Go | Google Images | Runs Google reverse-image searches from the command line. | 2017-04-26 | 2026-07-07 | 124 |
| [Project Eyes On](https://github.com/Y0oshi/Project-Eyes-On) | Python | Public camera directories and web search | Finds publicly accessible IP-camera streams through public directories and web-search queries. | 2026-01-10 | 2026-01-12 | 120 |
| [EfficientIR](https://github.com/Sg4Dylan/EfficientIR) | Python | Local image collections | Finds similar and duplicate images in local collections using visual embeddings. | 2020-03-30 | 2025-06-25 | 112 |
| [lingolens](https://github.com/OSINT-mindset/lingolens) | HTML | - | Runs multilingual Google Lens searches and exports the results. | 2023-03-10 | 2026-05-29 | 85 |
| [PhotOSINT](https://github.com/Haris87/photosint) | JavaScript | - | Extracts image metadata and adds reverse-image search actions to the browser. | 2019-09-15 | 2021-07-15 | 60 |

<a id="location"></a>

## 📍 Location <sup>5 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [GhostTrack](https://github.com/HunxByts/GhostTrack) | Python | - | Combines phone, IP, and username lookups with geolocation modules. | 2023-04-15 | 2024-01-11 | 14,478 |
| [Creepy](https://github.com/ilektrojohn/creepy) | Python | - | Collects geolocation information exposed through social networking platforms. | 2011-02-03 | 2016-01-07 | 1,459 |
| [GeoWiFi](https://github.com/GONZOsint/geowifi) | Python | - | Queries public Wi-Fi geolocation sources using BSSIDs and SSIDs. | 2022-02-05 | 2024-12-21 | 1,370 |
| [SatIntel](https://github.com/ANG13T/SatIntel) | Go | - | Retrieves satellite telemetry, orbital predictions, and TLE data. | 2023-05-03 | 2024-03-15 | 893 |
| [ShadowFinder](https://github.com/bellingcat/ShadowFinder) | Python | - | Estimates possible locations from the geometry of shadows in an image. | 2024-05-01 | 2026-02-13 | 591 |

<a id="company"></a>

## 🏢 Company <sup>4 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [Aleph](https://github.com/alephdata/aleph) | JavaScript | - | Lets investigators search documents and structured data for people and companies. | 2014-08-27 | 2026-02-20 | 2,397 |
| [cloud_enum](https://github.com/initstring/cloud_enum) | Python | - | Enumerates public cloud resources associated with organization keywords. | 2019-05-31 | 2026-07-09 | 2,114 |
| [emploleaks](https://github.com/infobyte/emploleaks) | Python | - | Identifies company employees appearing in credential leak data. | 2023-04-21 | 2026-05-19 | 786 |
| [OpenSanctions](https://github.com/opensanctions/opensanctions) | Python | - | Builds searchable data on sanctions, entities, and persons of interest. | 2015-12-05 | 2026-07-14 | 768 |

<a id="cryptocurrency"></a>

## ₿ Cryptocurrency <sup>6 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [BlockSci](https://github.com/citp/BlockSci) | C++ | - | Provides high-performance analysis and exploration of blockchain data. | 2017-09-02 | 2021-12-13 | 1,394 |
| [Bitcoin ETL](https://github.com/blockchain-etl/bitcoin-etl) | Python | - | Exports Bitcoin-family blockchain data into analysis-friendly formats. | 2018-09-13 | 2025-05-02 | 458 |
| [all-in-one-bot](https://github.com/uerax/all-in-one-bot) | Go | - | Tracks on-chain activity and market signals through a Telegram interface. | 2023-03-28 | 2026-06-12 | 180 |
| [GraphSense Dashboard](https://github.com/graphsense/graphsense-dashboard) | Elm | - | Provides interactive exploration of cryptocurrency transactions and entities. | 2017-10-18 | 2026-07-14 | 135 |
| [Mars](https://github.com/deepeth/mars) | Rust | - | Explores and visualizes structured blockchain data. | 2022-07-05 | 2023-06-20 | 119 |
| [GraphSense Library](https://github.com/graphsense/graphsense-lib) | Python | - | Supplies CLI and backend utilities for cryptocurrency analytics workflows. | 2022-10-11 | 2026-07-14 | 17 |

<a id="general"></a>

## 🧰 General <sup>21 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [SearXNG](https://github.com/searxng/searxng) | Python | - | Aggregates results from multiple search services in a self-hosted metasearch engine. | 2021-04-12 | 2026-07-15 | 33,933 |
| [SpiderFoot](https://github.com/smicallef/spiderfoot) | Python | - | Automates multi-source OSINT collection and attack-surface mapping. | 2012-04-28 | 2026-04-13 | 19,658 |
| [OpenCTI](https://github.com/OpenCTI-Platform/opencti) | TypeScript | - | Organizes cyber threat intelligence in a graph-based analysis platform. | 2018-12-17 | 2026-07-14 | 9,682 |
| [Recon-ng](https://github.com/lanmaster53/recon-ng) | Python | - | Organizes modular open-source intelligence collection in a command-line framework. | 2019-03-28 | 2024-11-01 | 5,774 |
| [IntelOwl](https://github.com/intelowlproject/IntelOwl) | Python | - | Orchestrates threat intelligence analyzers and connectors at scale. | 2019-12-31 | 2026-07-14 | 4,622 |
| [Mr.Holmes](https://github.com/Lucksi/Mr.Holmes) | Python | - | Combines multiple identity, domain, phone, and social investigation modules. | 2021-06-23 | 2026-02-21 | 3,844 |
| [FOCA](https://github.com/ElevenPaths/FOCA) | C# | - | Extracts metadata and hidden information from public documents. | 2017-10-02 | 2022-12-08 | 3,588 |
| [Datasploit](https://github.com/DataSploit/datasploit) | Python | - | Correlates OSINT findings across people, companies, domains, phones, and cryptocurrency. | 2016-05-23 | 2017-12-20 | 3,307 |
| [OnionScan](https://github.com/s-rah/onionscan) | Go | - | Investigates operational security issues and relationships in Tor hidden services. | 2016-04-08 | 2016-10-30 | 3,267 |
| [X-osint](https://github.com/TermuxHackz/X-osint) | Python | - | Runs phone, email, domain, VIN, and identity-oriented lookup modules. | 2023-03-11 | 2026-07-12 | 2,483 |
| [sn0int](https://github.com/kpcyrd/sn0int) | Rust | - | Provides a semi-automatic OSINT framework with installable modules. | 2018-10-05 | 2026-05-15 | 2,482 |
| [Watcher](https://github.com/thalesgroup-cert/Watcher) | JavaScript | - | Collects, enriches, and searches cyber threat intelligence with assisted analysis. | 2020-09-01 | 2026-07-13 | 1,336 |
| [Open Semantic Search](https://github.com/opensemanticsearch/open-semantic-search) | Shell | - | Searches, extracts, and links entities across large document collections. | 2016-03-30 | 2025-04-19 | 1,189 |
| [Taranis AI](https://github.com/taranis-ai/taranis-ai) | Python | - | Collects and analyzes open-source information for situational awareness. | 2023-10-05 | 2026-07-14 | 1,178 |
| [Mihari](https://github.com/ninoseki/mihari) | Ruby | - | Aggregates search queries across threat intelligence services. | 2019-04-15 | 2026-07-04 | 939 |
| [ThreatIngestor](https://github.com/pedramamini/ThreatIngestor) | Python | - | Extracts and routes threat indicators from public information feeds. | 2017-08-31 | 2026-05-26 | 921 |
| [Seekr](https://github.com/seekr-osint/seekr) | Go | - | Offers a multi-purpose OSINT toolkit through a web interface. | 2022-12-06 | 2026-06-16 | 834 |
| [Operative Framework](https://github.com/graniet/operative-framework) | Rust | - | Manages targets, investigation modules, links, notes, and reports. | 2017-01-03 | 2025-05-17 | 746 |
| [LinkScope Client](https://github.com/AccentuSoft/LinkScope_Client) | Python | - | Represents investigation entities and relationships in an extensible visual workspace. | 2021-09-15 | 2024-08-12 | 473 |
| [TIGMINT](https://github.com/TIGMINT/TIGMINT) | JavaScript | - | Provides a graphical framework for running modular OSINT tasks. | 2020-09-05 | 2021-07-29 | 258 |
| [Ronin Recon](https://github.com/ronin-rb/ronin-recon) | Ruby | - | Provides a modular reconnaissance framework and command-line interface. | 2023-04-11 | 2026-01-12 | 42 |

---

<a id="social-platforms"></a>

## Social platforms

The following sections separate tools by the social, community, messaging, video, gaming, or code-hosting platform they primarily investigate. The **Compatibility** column identifies the supported platform or cross-platform scope; agentic tools retain their AI-client compatibility after the platform name.

> [!NOTE]
> Some legacy projects remain useful for research or reference even when the platform behavior they relied on has changed; their age is visible in the update date.

<a id="cross-platform"></a>

## Cross-platform <sup>19 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [Sherlock](https://github.com/sherlock-project/sherlock) | Python | Cross-platform (400+) | Checks a username across many social networks. | 2018-12-24 | 2026-07-14 | 86,582 |
| [Maigret](https://github.com/soxoj/maigret) | Python | Cross-platform (3,000+) | Builds username-based account reports across thousands of sites. | 2020-06-27 | 2026-07-14 | 35,386 |
| [Social Analyzer](https://github.com/qeeqbox/social-analyzer) | JavaScript | Cross-platform (1,000+) | Searches and analyzes profiles across numerous social platforms. | 2020-11-30 | 2026-01-12 | 23,456 |
| [Blackbird](https://github.com/p1ngul1n0/blackbird) | Python | Cross-platform (600+) | Searches social platforms for accounts linked to a username or email. | 2022-05-06 | 2025-07-13 | 7,007 |
| [Snoop](https://github.com/snooppr/snoop) | Python | Cross-platform (5,400+) | Searches for username usage across a large collection of websites. | 2020-02-14 | 2026-06-30 | 3,962 |
| [gosearch](https://github.com/ibnaleem/gosearch) | Go | Cross-platform (300+) | Searches for a person's digital footprint across hundreds of websites. | 2024-11-09 | 2026-07-08 | 3,503 |
| [user-scanner](https://github.com/kaifcodec/user-scanner) | Python | Cross-platform (310+ vectors) | Runs username and email discovery checks across many services. | 2025-10-19 | 2026-07-14 | 2,687 |
| [WhatsMyName](https://github.com/WebBreacher/WhatsMyName) | Python | Cross-platform (700+) | Checks usernames using community-maintained site definitions and scripts. | 2015-10-02 | 2026-06-24 | 2,666 |
| [Tookie](https://github.com/Alfredredbird/tookie-osint) | Python | Cross-platform | Provides a multi-target information gathering toolkit. | 2023-08-22 | 2026-07-07 | 2,590 |
| [Nexfil](https://github.com/thewhiteh4t/nexfil) | Python | Cross-platform (350+) | Finds profiles associated with a username across online services. | 2021-05-21 | 2023-09-30 | 2,582 |
| [Aliens Eye](https://github.com/arxhr007/Aliens_eye) | Python | Cross-platform (840+) | Searches for accounts associated with a username across hundreds of platforms. | 2021-09-22 | 2026-07-03 | 2,511 |
| [socialscan](https://github.com/iojw/socialscan) | Python | Instagram, X / Twitter, GitHub, Tumblr, Last.fm, Snapchat, GitLab, Reddit, Yahoo, Pinterest, Firefox | Queries username and email registration status on supported platforms. | 2019-02-17 | 2026-04-27 | 1,791 |
| [DetectDee](https://github.com/Yvesssn/DetectDee) | Go | Cross-platform | Searches social networks using usernames, email addresses, and phone numbers. | 2023-04-29 | 2023-08-26 | 1,786 |
| [UserFinder](https://github.com/mishakorzik/UserFinder) | Shell | Cross-platform | Checks whether a username appears on supported websites. | 2021-07-19 | 2025-11-16 | 1,320 |
| [socid-extractor](https://github.com/soxoj/socid-extractor) | Python | Cross-platform (130+) | Converts profile URLs into structured identity records across many platforms. | 2019-11-17 | 2026-07-14 | 1,038 |
| [Linkook](https://github.com/JackJuly/linkook) | Python | Cross-platform | Discovers linked social accounts and email clues from a username. | 2025-01-30 | 2026-02-28 | 993 |
| [Marple](https://github.com/soxoj/marple) | Python | Cross-platform via search engines | Finds profile links through search engines and extensible analysis plugins. | 2021-11-16 | 2026-07-14 | 312 |
| [SocialPath](https://github.com/woj-ciech/SocialPath) | CSS | Facebook, X / Twitter, Stack Overflow, Instagram, Reddit, Steam, Pinterest, Tumblr, Pastebin, GitHub | Correlates usernames and profile links across supported social platforms. | 2020-09-05 | 2020-09-05 | 169 |
| [Social OSINT](https://github.com/krishpranav/socialosint) | Rust | Instagram, LinkedIn, X / Twitter | Collects exposed email addresses from supported social platforms and checks related leak data. | 2021-07-02 | 2026-02-10 | 93 |

<a id="x-and-twitter"></a>

## X and Twitter <sup>7 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [Twint](https://github.com/twintproject/twint) | Python (archived) | X / Twitter | Collects public Twitter posts, profiles, and account relationships without the official API. | 2017-06-10 | 2023-02-23 | 16,394 |
| [Nitter](https://github.com/zedeus/nitter) | Nim | X / Twitter | Provides a privacy-oriented front end for viewing public X content. | 2019-06-20 | 2026-06-26 | 13,258 |
| [twitter-scraper](https://github.com/bisguzar/twitter-scraper) | Python (archived) | X / Twitter | Collects public Twitter data through the frontend API without official API authentication. | 2018-02-22 | 2023-10-30 | 4,013 |
| [tinfoleak](https://github.com/vaguileradiaz/tinfoleak) | Python | X / Twitter | Analyzes public Twitter account activity and associated metadata. | 2018-01-27 | 2019-02-06 | 1,978 |
| [X Tweet Fetcher](https://github.com/ythx-101/x-tweet-fetcher) | Python | X / Twitter | Retrieves public X posts, replies, timelines, and articles without login. | 2026-02-14 | 2026-07-05 | 901 |
| [stweet](https://github.com/markowanga/stweet) | Python | X / Twitter | Provides an unofficial Python library for collecting Twitter posts and user records. | 2020-11-16 | 2023-07-25 | 623 |
| [xint](https://github.com/0xNyk/xint) | CLI + skill + MCP | X / Twitter; Multi-model | Searches, monitors, and exports public X data for agent-assisted investigations. | 2026-02-14 | 2026-07-04 | 215 |

<a id="facebook"></a>

## Facebook <sup>2 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [Facebook Sleep Stats](https://github.com/sorenlouv/fb-sleep-stats) | JavaScript | Facebook | Infers activity and sleep patterns from observed Facebook online status. | 2015-12-30 | 2020-08-25 | 1,699 |
| [Facebook Friend List Scraper](https://github.com/n0kovo/fb_friend_list_scraper) | Python | Facebook | Extracts names and usernames from large Facebook friend lists. | 2021-11-21 | 2022-04-21 | 325 |

<a id="instagram"></a>

## Instagram <sup>9 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [Osintgram](https://github.com/Datalux/Osintgram) | Python | Instagram | Provides an interactive interface for collecting information from Instagram profiles. | 2019-06-07 | 2025-08-25 | 13,529 |
| [Instaloader](https://github.com/instaloader/instaloader) | Python | Instagram | Downloads Instagram posts, captions, profile data, and related metadata. | 2016-06-15 | 2026-07-13 | 12,854 |
| [Toutatis](https://github.com/megadose/toutatis) | Python | Instagram | Extracts public account details from Instagram profiles. | 2020-02-03 | 2024-12-05 | 4,087 |
| [yesitsme](https://github.com/0x0be/yesitsme) | Python | Instagram | Finds possible Instagram profiles from a name, email address, or phone number. | 2021-12-23 | 2024-08-17 | 2,871 |
| [osi.ig](https://github.com/th3unkn0n/osi.ig) | Python | Instagram | Collects publicly accessible information from Instagram profiles. | 2019-11-04 | 2022-12-08 | 1,529 |
| [Instagram Monitor](https://github.com/misiektoja/instagram_monitor) | Python | Instagram | Tracks public Instagram profile changes, activity, and captured content. | 2024-04-25 | 2026-07-06 | 1,111 |
| [Osintgraph](https://github.com/XD-MHLOO/Osintgraph) | Python | Instagram | Maps Instagram followers and relationships in Neo4j for network analysis. | 2025-04-30 | 2025-09-06 | 803 |
| [SoIG](https://github.com/yezz123/SoIG) | Python | Instagram | Retrieves selected public information associated with an Instagram account. | 2020-06-08 | 2023-07-25 | 382 |
| [insto](https://github.com/subzeroid/insto) | Python | Instagram | Collects Instagram profile, media, relationship, and timeline data through interchangeable backends. | 2026-04-26 | 2026-06-20 | 52 |

<a id="linkedin"></a>

## LinkedIn <sup>8 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [linkedin2username](https://github.com/initstring/linkedin2username) | Python | LinkedIn | Generates possible corporate usernames from public LinkedIn employee data. | 2018-02-22 | 2026-05-20 | 1,765 |
| [CrossLinked](https://github.com/m8sec/CrossLinked) | Python | LinkedIn | Extracts employee names from public LinkedIn search results. | 2019-05-16 | 2024-11-26 | 1,568 |
| [LinkedInt](https://github.com/vysecurity/LinkedInt) | Python | LinkedIn | Performs legacy LinkedIn account and company reconnaissance. | 2018-03-08 | 2022-12-08 | 1,207 |
| [LinkedInDumper](https://github.com/l4rm4nd/LinkedInDumper) | Python | LinkedIn | Extracts company employee records through LinkedIn endpoints. | 2022-10-17 | 2026-04-18 | 601 |
| [InSpy](https://github.com/jobroche/InSpy) | Python | LinkedIn | Enumerates LinkedIn employees by company and job title. | 2016-02-14 | 2016-02-14 | 573 |
| [the-endorser](https://github.com/eth0izzle/the-endorser) | Python | LinkedIn | Maps relationships between LinkedIn profiles using endorsements and skills. | 2017-11-24 | 2021-03-25 | 353 |
| [LinkedIn OSINT Toolkit](https://github.com/michaelelizarov/linkedin-osint-toolkit) | Python | LinkedIn | Discovers companies and employees, classifies roles, and builds organization views. | 2026-02-16 | 2026-02-16 | 34 |
| [LinkedIn Recon Skill](https://github.com/Kewanvk/linkedin-recon-skill) | Skill | LinkedIn; Claude Code + Codex | Maps public hiring networks and organizational relationships from LinkedIn evidence. | 2026-05-08 | 2026-05-25 | 0 |

<a id="reddit"></a>

## Reddit <sup>5 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [Pushshift API](https://github.com/pushshift/api) | Python | Reddit | Implements an API for searching archived Reddit submissions and comments. | 2017-08-17 | 2017-12-06 | 1,424 |
| [Arctic Shift](https://github.com/ArthurHeitmann/arctic_shift) | TypeScript | Reddit | Provides searchable Reddit archives through data dumps, an API, and a web interface. | 2023-08-03 | 2026-07-12 | 1,235 |
| [Universal Reddit Scraper](https://github.com/JosephLai241/URS) | Python | Reddit | Scrapes and archives Reddit submissions, comments, and user activity. | 2019-03-20 | 2026-07-11 | 1,007 |
| [Reddit Research MCP](https://github.com/king-of-the-grackles/reddit-research-mcp) | MCP server | Reddit; Model-agnostic (MCP) | Supports structured Reddit discovery, thread collection, and community research. | 2025-08-12 | 2026-07-02 | 216 |
| [Reddit Persona](https://github.com/n2itn/reddit_persona) | Python | Reddit | Extracts sentiment, keywords, and personality indicators from Reddit accounts. | 2016-08-02 | 2017-07-19 | 24 |

<a id="telegram"></a>

## Telegram <sup>20 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [CCTV](https://github.com/IvanGlinkin/CCTV) | JavaScript | Telegram | Demonstrates location mapping through Telegram's former nearby-user behavior. | 2024-04-26 | 2024-05-02 | 2,470 |
| [Telegram Phone Number Checker](https://github.com/bellingcat/telegram-phone-number-checker) | Python | Telegram | Checks whether supplied phone numbers are connected to Telegram accounts. | 2021-02-17 | 2024-06-24 | 1,743 |
| [Telegram Scraper](https://github.com/th3unkn0n/TeleGram-Scraper) | Python | Telegram | Exports Telegram group member information through a legacy scraper. | 2019-12-03 | 2019-12-03 | 1,659 |
| [Informer](https://github.com/paulpierre/informer) | Python | Telegram | Collects and indexes Telegram channel and group activity. | 2019-12-09 | 2025-10-20 | 1,639 |
| [Telerecon](https://github.com/sockysec/Telerecon) | Python | Telegram | Provides a modular framework for researching Telegram entities. | 2023-08-30 | 2024-07-11 | 1,309 |
| [Telepathy Community](https://github.com/prose-intelligence-ltd/Telepathy-Community) | Python | Telegram | Collects and analyzes public Telegram chat data. | 2022-01-17 | 2026-06-01 | 1,228 |
| [Telegram Nearby Map](https://github.com/tejado/telegram-nearby-map) | JavaScript | Telegram | Maps nearby Telegram users through a legacy location feature. | 2021-01-14 | 2022-03-02 | 1,188 |
| [Tosint](https://github.com/drego85/tosint) | Python | Telegram | Extracts Telegram bot, chat, and user information from tokens and identifiers. | 2021-07-26 | 2026-03-10 | 835 |
| [Geogramint](https://github.com/Alb-310/Geogramint) | Python | Telegram | Implements a legacy workflow for locating nearby Telegram users and groups. | 2022-07-16 | 2023-10-25 | 731 |
| [Telegram History Dump](https://github.com/tvdstaaij/telegram-history-dump) | Ruby | Telegram | Backs up Telegram chat logs through telegram-cli. | 2015-10-18 | 2017-03-02 | 677 |
| [TeleTracker](https://github.com/tsale/TeleTracker) | Python | Telegram | Collects Telegram channel information and supports repeatable investigation tasks. | 2024-01-15 | 2024-04-29 | 535 |
| [Maltego Telegram](https://github.com/vognik/maltego-telegram) | Python | Telegram | Adds Maltego transforms for Telegram channels, groups, users, and messages. | 2024-11-04 | 2026-01-27 | 515 |
| [telegram-tracker](https://github.com/estebanpdl/telegram-tracker) | Python | Telegram | Exports channel details and posts from selected Telegram channels. | 2022-04-06 | 2024-07-26 | 381 |
| [Telegram OSINT Library](https://github.com/Postuf/telegram-osint-lib) | PHP | Telegram | Provides scenario-based Telegram API operations for investigations. | 2019-12-23 | 2024-03-16 | 314 |
| [TeleGraphite](https://github.com/hamodywe/telegram-scraper-TeleGraphite) | Python | Telegram | Collects Telegram channel posts and exports them as JSON. | 2025-04-12 | 2025-04-12 | 275 |
| [Telegram Similar Channels](https://github.com/SocialLinks-IO/telegram-similar-channels) | Python | Telegram | Finds related Telegram channels through CLI and Maltego interfaces. | 2023-12-07 | 2023-12-07 | 190 |
| [Save Telegram Chat History](https://github.com/pigpagnet/save-telegram-chat-history) | JavaScript | Telegram | Exports Telegram chat history for local preservation. | 2016-02-01 | 2016-02-01 | 169 |
| [Telegram Message Analyzer](https://github.com/zqtay/Telegram-Message-Analyzer) | Python | Telegram | Summarizes exported Telegram chats by date, message volume, and word frequency. | 2018-12-31 | 2018-12-31 | 61 |
| [Telegram OSINT Polo](https://github.com/Ironship/TelegramOSINTPolo) | Python | Telegram | Downloads Telegram feed posts for local review and assisted analysis. | 2025-03-04 | 2026-03-12 | 55 |
| [TGeocoder](https://github.com/MJCruickshank/TGeocoder) | Jupyter Notebook | Telegram | Parses and geocodes location references from Telegram news channels. | 2025-01-08 | 2025-01-08 | 43 |

<a id="tiktok"></a>

## TikTok <sup>2 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [TikTok Hashtag Analysis](https://github.com/bellingcat/tiktok-hashtag-analysis) | Python | TikTok | Collects and analyzes TikTok posts associated with selected hashtags. | 2021-08-11 | 2024-06-20 | 367 |
| [TikTok-OSINT](https://github.com/T1erno/TikTok-OSINT) | Python | TikTok | Collects public TikTok profile metadata and profile images from a username. | 2021-07-23 | 2022-11-02 | 3 |

<a id="youtube"></a>

## YouTube <sup>3 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | Python | YouTube + other video sites | Downloads public video, audio, subtitles, comments, and metadata from supported platforms. | 2020-10-26 | 2026-07-04 | 178,063 |
| [Yark](https://github.com/Owez/yark) | Python | YouTube | Archives public YouTube channels, videos, and metadata for local analysis. | 2022-08-16 | 2026-06-07 | 2,179 |
| [tubeup](https://github.com/bibanon/tubeup) | Python | YouTube + yt-dlp-supported sites | Archives online video and metadata to the Internet Archive through yt-dlp. | 2016-02-05 | 2026-05-08 | 509 |

<a id="snapchat"></a>

## Snapchat <sup>2 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [SnapIntel](https://github.com/Kr0wZ/SnapIntel) | Python | Snapchat | Retrieves public account details associated with Snapchat usernames. | 2021-03-02 | 2023-12-17 | 325 |
| [Snap Map Scraper](https://github.com/nemec/snapchat-map-scraper) | Python | Snapchat | Collects public Snapchat stories and location metadata from Snap Map. | 2020-06-01 | 2023-07-25 | 195 |

<a id="whatsapp"></a>

## WhatsApp <sup>2 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [WhatsOSINT](https://github.com/HackUnderway/WhatsOSINT) | Python | WhatsApp | Retrieves public WhatsApp account details associated with a number. | 2024-11-19 | 2026-07-10 | 309 |
| [whatsfoto](https://github.com/zoutepopcorn/whatsfoto) | JavaScript | WhatsApp | Retrieves WhatsApp profile pictures for supplied phone numbers. | 2017-05-31 | 2018-04-13 | 20 |

<a id="steam"></a>

## Steam <sup>3 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [steam-osint](https://github.com/matiash26/steam-osint) | Python | Steam | Finds mutual friends between public Steam profiles. | 2022-03-12 | 2022-04-10 | 92 |
| [Steam Monitor](https://github.com/misiektoja/steam_monitor) | Python | Steam | Tracks public Steam player activity, game sessions, and status changes. | 2024-04-25 | 2026-06-26 | 50 |
| [SteamReveal](https://github.com/Berchez/SteamReveal) | TypeScript | Steam | Analyzes Steam profiles for close contacts and possible location clues. | 2024-02-20 | 2026-05-01 | 25 |

<a id="github"></a>

## GitHub <sup>16 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Go | Git, GitHub | Scans Git repositories and other inputs for hardcoded secrets and credentials. | 2018-01-27 | 2026-07-15 | 28,153 |
| [TruffleHog](https://github.com/trufflesecurity/trufflehog) | Go | GitHub, GitLab, Git and other sources | Finds, verifies, and analyzes exposed credentials across supported code and storage sources. | 2016-12-31 | 2026-07-15 | 27,053 |
| [shhgit](https://github.com/eth0izzle/shhgit) | JavaScript | GitHub, GitLab, Bitbucket | Monitors public code platforms for newly exposed secrets. | 2019-09-06 | 2023-08-30 | 3,971 |
| [github-dorks](https://github.com/techgaun/github-dorks) | Python | GitHub | Runs GitHub search queries intended to locate exposed sensitive data. | 2015-10-11 | 2021-01-18 | 3,241 |
| [GitDorker](https://github.com/obheda12/GitDorker) | Python | GitHub | Automates GitHub dork searches for exposed secrets. | 2020-07-13 | 2020-07-13 | 2,567 |
| [gitGraber](https://github.com/hisxo/gitGraber) | Python | GitHub | Monitors public GitHub activity for exposed credentials and service tokens. | 2019-09-04 | 2026-03-26 | 2,316 |
| [GitGot](https://github.com/BishopFox/GitGot) | Python | GitHub | Searches public GitHub data for exposed secrets using feedback-driven queries. | 2019-06-14 | 2019-07-30 | 1,567 |
| [git-hound](https://github.com/tillson/git-hound) | Go | GitHub | Searches GitHub at scale for exposed secrets and dork matches. | 2019-07-16 | 2026-02-10 | 1,441 |
| [GitFive](https://github.com/mxrch/GitFive) | Python | GitHub | Correlates public GitHub account data for identity-focused investigations. | 2022-10-05 | 2025-10-04 | 1,004 |
| [Zen](https://github.com/s0md3v/Zen) | Python | GitHub | Finds email addresses associated with GitHub users. | 2018-10-15 | 2018-10-17 | 595 |
| [gitrecon](https://github.com/GONZOsint/gitrecon) | Python | GitHub, GitLab | Extracts public profile and email evidence from GitHub and GitLab. | 2021-03-19 | 2021-03-25 | 322 |
| [GitSint](https://github.com/N0rz3/GitSint) | Python | GitHub | Collects public intelligence about GitHub users and repositories. | 2023-04-26 | 2026-06-28 | 243 |
| [Gitxray](https://github.com/kulkansecurity/gitxray) | Python | GitHub | Uses public GitHub APIs for account, repository, and contribution analysis. | 2024-08-06 | 2026-01-09 | 182 |
| [Shotstars](https://github.com/snooppr/shotstars) | Python | GitHub | Analyzes repository star history and indicators of artificial activity. | 2024-05-25 | 2026-06-04 | 111 |
| [GitRecon](https://github.com/atiilla/gitrecon) | JavaScript | GitHub | Scans a GitHub user's repositories for exposed names and email addresses. | 2023-09-03 | 2025-06-09 | 55 |
| [GitHub Monitor](https://github.com/misiektoja/github_monitor) | Python | GitHub | Tracks GitHub profile and repository activity with change notifications. | 2024-05-11 | 2026-05-26 | 51 |

<a id="discord"></a>

## Discord <sup>6 projects</sup>

| Project | Type | Compatibility | Description | Created | Last Update | Stars ⭐ |
|:---|:---:|:---:|:---|:---:|:---:|---:|
| [DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter) | C# | Discord | Exports accessible Discord message history and rich media to local files. | 2017-07-12 | 2026-07-14 | 11,583 |
| [Discord History Tracker](https://github.com/chylex/Discord-History-Tracker) | C# | Discord | Saves accessible Discord chat history for offline preservation and review. | 2016-10-22 | 2026-01-29 | 579 |
| [DiscordLookup](https://github.com/discordlookup/discordlookup) | PHP (archived) | Discord | Provides user, guild, application, invite, and snowflake lookup functions. | 2021-09-28 | 2025-10-21 | 254 |
| [discard2](https://github.com/Sanqui/discard2) | TypeScript (archived) | Discord | Creates high-fidelity local archives of accessible Discord content. | 2022-03-15 | 2025-07-21 | 39 |
| [discord-urls-extractor](https://github.com/TheTechRobo/discord-urls-extractor) | Rust | Discord | Extracts URLs and media references from supported Discord archive formats. | 2021-11-21 | 2024-12-19 | 21 |
| [Discord Inspector](https://github.com/Euronymou5/Discord-Inspector) | Python | Discord | Retrieves public user, server, and application metadata from Discord identifiers. | 2024-12-03 | 2024-12-05 | 6 |

---

<a id="catalogue-automation"></a>

## Catalogue automation

The catalogue uses a review-gated monitor to refresh exact repository metadata, preserve historical snapshots, discover candidates across GitHub and other public sources, and regenerate every published table from one canonical repository database.

> [!TIP]
> Maintainer documentation and automation internals are kept in the [hidden radar workspace](.radar/README.md).

---

<a id="reviewed-source-collections"></a>

## Reviewed source collections

All tracked text and configuration files in these source repositories were scanned for repository links. The collections themselves are not catalogued as tools.

- [jivoi/awesome-osint](https://github.com/jivoi/awesome-osint)
- [wddadk/Offensive-OSINT-Tools](https://github.com/wddadk/Offensive-OSINT-Tools)
- [Astrosp/Awesome-OSINT-List](https://github.com/Astrosp/Awesome-OSINT-List)
- [osintambition/Social-Media-OSINT-Tools-Collection](https://github.com/osintambition/Social-Media-OSINT-Tools-Collection)
- [The-Osint-Toolbox/Telegram-OSINT](https://github.com/The-Osint-Toolbox/Telegram-OSINT)
- [ubikron/Awesome-AI-OSINT](https://github.com/ubikron/Awesome-AI-OSINT)

---

<a id="metadata-conventions"></a>

## Metadata conventions

- **Project** links to the canonical public source-code repository containing the implementation.
- **Type** is the repository's primary implementation language for standalone tools, or its integration type for skills, plugins, and MCP projects.
- **Compatibility** names the investigated platform for platform-specific tools, summarizes the scope for cross-platform tools, and names a documented AI client or standard for agentic integrations. When both apply, values are separated with a semicolon; `-` means the field does not apply.
- **Description** summarizes the project's primary capability in neutral language.
- **Created** is the public repository creation date.
- **Last Update** is the date of the repository's latest recorded push in `YYYY-MM-DD` format.
- **Stars ⭐** is the repository star count captured during the latest metadata verification.
- **License** in the repository database records the open-source license declared by the project. Blank, missing, or `NOASSERTION` values require manual verification.
- Each project appears only once, under its primary investigation target or platform.

> [!TIP]
> New standalone tools are maintained in [Emerging OSINT Projects](EMERGING.md). Agent skills, plugins, and MCP servers are listed in [Agentic AI OSINT](AGENTIC.md). The deduplicated [open-source repository database](osint-repositories.csv) combines all catalogue views.

<p align="right"><a href="#top">Back to top ↑</a></p>
