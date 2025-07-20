---
title: "2024 Malicious Infrastructure Insights: Key Trends and Threats"
tags:
   - malware-as-a-service
   - malware
   - threat intelligence
   - remote access trojans
   - cybersecurity
link: https://www.recordedfuture.com/research/2024-malicious-infrastructure-report
date: 2025-05-05
description: "The 2024 Malicious Infrastructure Report by Insikt Group documents a notable evolution in malware trends, emphasizing the rise of Malware-as-a-Service (MaaS) infostealers, particularly LummaC2, amidst law enforcement disruptions to rival threats. Key findings include continued dominance of AsyncRAT and QuasarRAT, significant shifts in relay network usage by state-sponsored actors, and an increase in malicious infrastructure tracked. Key recommendations for defenders involve leveraging threat intelligence, improving detection methodologies, and adapting strategies to confrontation evolving cyber threats, particularly those utilizing legitimate services and targeting mobile platforms."
---

Research (Insikt)

# 2024 Malicious Infrastructure Report

Posted: 25th February 2025

By: Insikt Group®

![2024 Malicious Infrastructure Report](https://cms.recordedfuture.com/uploads/format_webp/large_2024_malicious_infrastructure_report_95f6761bdf.png)

![insikt group logo](https://cms.recordedfuture.com/uploads/insikt_group_logo_updated_3_300x48_b5390f4ff2.png)

## Executive Summary

In 2024, Insikt Group significantly expanded its tracking of malicious infrastructure by covering more malware families and categories, additional infrastructure types such as staging servers, and integrating data sources like Recorded Future® Network Intelligence, enhancing threat detection, higher-tier infrastructure insights, and victimology analysis. While many key 2023 trends persisted — such as Cobalt Strike dominating offensive security tools (OSTs), AsyncRAT and QuasarRAT leading among remote access trojans (RATs), China and the United States (US) being the top hosting locations, and law enforcement actions having often only temporary impact — Insikt Group identified several emerging trends in 2024.

Notably, malware-as-a-service (MaaS) infostealers, led by LummaC2, grew in prevalence, likely driven by law enforcement actions against competitor infostealers and rapid innovation by LummaC2. Additionally, Android remained the primary target for mobile malware, with Hook leading. While Latrodectus dominated droppers and loaders despite law enforcement disruptions in the loader ecosystem, traffic distribution systems (TDSs) continued to enhance cybercrime efficiency, as seen with TAG-124, and the abuse of content delivery networks (CDNs) like Cloudflare surged. In regards to state-sponsored groups, China notably increased its use of relay networks such as ArcSilt, while Russia continued its abuse of a wide range of [legitimate internet services (LIS)](https://www.recordedfuture.com/research/threat-actors-leverage-internet-services-to-enhance-data-theft-and-weaken-security-defenses).

Defenders should leverage this report's insights to strengthen security controls by prioritizing top malware and infrastructure techniques, and thereby enhance network monitoring and deploy relevant detections like YARA, Sigma, and Snort. This should be complemented by investments in tracking evolving malicious infrastructure dynamics, conducting threat simulations to test defenses, and effectively monitoring the broader threat landscape. Regarding LIS, defenders must balance blocking, flagging, or allowing high-risk services based on their assessed criticality and risk level.

As malicious infrastructure evolves and detection improves, Insikt Group expects existing trends to persist in 2025, driven by continuous threat actor innovation rather than drastic shifts. For example, the "as-a-service" ecosystem will likely expand, and threat actors will increasingly rely on legitimate tools, services, and CDNs to evade detection. Furthermore, with growing mobile reliance, Insikt Group expects mobile-based threats to continue to rise. Relay networks, primarily used by Chinese state-sponsored groups up until now, may see broader adoption by cybercriminals and other state-sponsored groups. Lastly, law enforcement actions are expected to have a greater impact due to enhanced international cooperation and accrued expertise in large-scale cybercrime takedowns.

## Key Findings

- MaaS infostealers led in infections in 2024, with LummaC2 dominating command-and-control (C2) servers as continuous innovation and law enforcement actions against rivals like RedLine Stealer reshaped the cybercrime ecosystem.
- AsyncRAT and Quasar RAT remained the top remote access tools (RATs), while MaaS-based malware like DcRAT continued widespread use.
- The US (North America), Brazil (South America), Angola (Africa), France (Europe), India (Asia), and Australia (Oceania) recorded the highest number of victims in their respective regions based on Recorded Future Network Intelligence, with AsyncRAT emerging as the most prevalent malware in most cases. Other significant threats included QuasarRAT and Cobalt Strike.
- Android remained the primary target for mobile malware, with nine of the top ten families focusing on it, alongside the rise of mercenary spyware and potentially unwanted programs (PUPs) like stalkerware.
- Cobalt Strike accounted for two-thirds of offensive security tool command-and-control (C2) servers, with jQuery as the most popular malleable profile and cs2modrewrite targeting the most victim countries. Cobalt Strike is followed by Metasploit, with detections of Sliver and Brute Ratel C4 rising significantly.
- Mozi Botnet was the largest tracked botnet in 2024 based on the number of identified bots, while older botnets remained active, being primarily used for distributed denial-of-service (DDoS) attacks, as well as credential theft and localized attacks, as seen with Fenix Botnet.
- Latrodectus dominated all droppers and loaders in 2024, accounting for 33% of detections, likely driven by law enforcement disruptions in the loader ecosystem, while most top families emerged post-2021, indicating shorter lifespans.
- TDS continued to play a crucial role in cybercrime by improving efficiency, targeting, and profitability while evading detection, exemplified by TAG-124, which served a broad user base, including ransomware groups like Rhysida.
- The US and China dominated malicious hosting, while bulletproof hosting providers like Stark Industries played a growing role in cybercrime infrastructure.
- Chinese state-sponsored groups expanded their use of anonymization networks in 2024 to target entities worldwide, enabling them to blend with legitimate traffic and complicate victim identification, while RedDelta used Cloudflare to proxy C2 traffic and geo-fence malicious files.
- Russian state-sponsored groups increasingly relied on legitimate services like Ngrok, Cloudflare, and Telegram to evade detection, with BlueDelta shifting to Ngrok after takedown efforts and BlueAlpha using Cloudflare Tunnels to stage GammaDrop malware.

## Introduction

Insikt Group proactively identifies and monitors infrastructure associated with hundreds of malware families, threat actors, and other artifacts, including phishing kits, scanners, and relay networks. By automatically validating malicious infrastructure through various proprietary methods on a daily basis, Insikt Group provides accurate risk representation, enabling Recorded Future customers to enhance their detection and defense capabilities.

Building on Insikt Group's annual adversary infrastructure reports from [2022](https://www.recordedfuture.com/research/2022-adversary-infrastructure-report) and [2023](https://go.recordedfuture.com/hubfs/reports/cta-2024-1209.pdf), the 2024 Malicious Infrastructure Report provides a concise, data-based overview of malicious infrastructure observed throughout 2024. This year, it specifically emphasizes the synergy among passive infrastructure detection, higher-tier infrastructure insights powered by Recorded Future Network Intelligence, and victim identification. Overall, this report is for anyone interested in malicious infrastructure, offering a high-level overview of its current state as well as summaries of key findings to inform decision-making and provide a broad perspective in this highly dynamic environment.

Recognizing the challenge of categorizing malware types in a mutually exclusive manner due to their overlapping functionalities, this report establishes a set of malware categories to facilitate analysis, as detailed in **Appendix A**, with brief definitions for each. Notably, certain malware categories, such as crypters, have been intentionally excluded due to the usual absence of network artifacts.

Beyond examining malicious infrastructure through the lens of malware categories, Insikt Group also monitors it by type, with each type assigned a distinct risk scoring within the Recorded Future Intelligence Cloud. This differentiation reflects varying levels of severity — for instance, network traffic to or from a C2 server in a corporate network may indicate higher risk compared to a management panel, as it typically implies active malicious activity. The infrastructure types defined by Insikt Group are detailed in **Appendix B**.

## 2024 Malicious Infrastructure Insights by the Numbers

Proactively identifying malicious infrastructure is a complex task shaped by various factors. In addition to the vast volume of data, each malware family, version, or infrastructure linked to specific threat actors often employs entirely unique setups. Detection becomes even more challenging due to factors such as hosting behind CDNs like Cloudflare, the use of high or random ports, reliance on [legitimate internet services](https://www.recordedfuture.com/research/threat-actors-leverage-internet-services-to-enhance-data-theft-and-weaken-security-defenses) such as Discord or Telegram, or the exploitation of compromised infrastructure.

These setups also evolve continuously, demanding that Insikt Group constantly innovate and refine its tracking methodologies. Considering all these factors, this report examines malicious infrastructure across multiple categories, including infostealers, backdoors and RATs, mobile malware, OSTs, botnets, droppers and loaders, phishing kits, web shells, and ransomware.

Overall, in 2024, there has been a significant rise in identified malicious infrastructure, driven by an evolving threat landscape and advancements in detection methodologies by Insikt Group. For instance, the number of unique, validated C2 servers doubled from 2023 to 2024, while unique, validated management panels saw a 69% increase over the same period.

In addition, using Recorded Future Network Intelligence, Insikt Group identified victims in approximately 200 countries worldwide in 2024 based on victim IP address geolocation. Countries in **Figure 1** were categorized into five groups based on the number of unique victims detected, with those showing high exposure being geographically dispersed worldwide. Notably, accurately measuring malware impact across countries is challenging due to variations in population size, digital footprint, analytical biases (for example, the types of malware tracked), internet infrastructure (such as proxies), and the geographical hosting choices of victim organizations.

![Malware impact by country](https://cms.recordedfuture.com/uploads/Fig_1_86418b387b.png)_**Figure 1:** Malware impact by country based on Recorded Future Network Intelligence (Source: Recorded Future)_

**Figure 2** shows the distribution of victims by country across different continents. In North America, the US is the most targeted country, accounting for around 87% of unique victims in the region despite making up only about half of its population. The high victim count in the US is likely driven by factors such as its large population, extensive digital footprint, widespread English use (exploited in phishing campaigns), and economics, while also being influenced by the country's role as a global infrastructure hub, providing hosting and digital services to organizations worldwide. Most victims are linked to AsyncRAT, followed by SolarMarker RAT and QuasarRAT (see **Table 1**). Notably, unlike AsyncRAT and QuasarRAT, SolarMarker RAT is [believed](https://www.recordedfuture.com/research/exploring-the-depths-of-solarmarkers-multi-tiered-infrastructure) to be operated by a single threat actor and has previously been observed predominantly targeting the US.

![victim by country](https://cms.recordedfuture.com/uploads/Fig_2_529f459d62.png)_**Figure 2:** Shares of unique victim by country and continent (Source: Recorded Future)_

In South America, Brazil recorded the highest number of unique victims, accounting for 86% of the region’s total, while also only making up around half of the continent’s population. Previously [identified](https://www.forbes.com/sites/angelicamarideoliveira/2023/09/27/brazil-is-the-worlds-second-most-vulnerable-country-to-cyberattacks/) as one of the countries most vulnerable to cyberattacks, Brazil has long been a hotspot for both global and local cyber threats, [ranking](https://www.ox.ac.uk/news/2024-04-10-world-first-cybercrime-index-ranks-countries-cybercrime-threat-level) high in cybercrime activity, with groups like Grandoreiro operating almost exclusively within its borders. In 2024, QuasarRAT infections were the most prevalent among Brazilian victims, followed by infections linked to AsyncRAT and SectopRAT.

In Africa, Angola recorded the highest number of unique victims, followed by Ghana, South Africa, the Republic of the Congo, and the Democratic Republic of the Congo. Notably, in two of the five most targeted African countries, PlugX, a malware linked to multiple Chinese state-sponsored groups, ranked among the most prevalent malware.

In Europe, France had the highest number of unique victims, followed by Germany, the United Kingdom, the Netherlands, and Poland. AsyncRAT was the most prevalent malware across all five countries, with Cobalt Strike ranking second in three of them. The distribution of victims in these top five countries closely aligns with their population sizes. Notably, in the Netherlands, GobRAT — a backdoor targeting Linux routers with malware written in Go — ranked among the top three malware families.

In Asia, India recorded the highest number of unique victims, followed by China, Indonesia, Thailand, and Hong Kong. Approximately 73% of all victims in these countries were linked to AsyncRAT, QuasarRAT, and Cobalt Strike infections. Notably, Brute Ratel C4 ranked among the top three malware in Hong Kong, highlighting its growing significance.

In Oceania, Australia accounted for 87% of all unique victims despite making up only 60% of the region's population. AsyncRAT was the most prevalent malware, linked to over half of Australia's victims, while in New Zealand, 67% of victims were associated with AsyncRAT infections.

**Table 1** presents the full list of the top three malware families for each of the five leading countries in each continent, based on the number of unique victims observed by Insikt Group in those countries.

| Continent | Country | Top 1 | Top 2 | Top 3 |
| --- | --- | --- | --- | --- |
| North America | United States | AsyncRAT | SolarMarker RAT | QuasarRAT |
| Canada | SolarMarker RAT | AsyncRAT | DcRAT |
| Cuba | Rhadamanthys Stealer | AsyncRAT | PrivateLoader |
| Mexico | AsyncRAT | DanaBot | Rhadamanthys Stealer |
| Bahamas | Spylix | AsyncRAT | QuasarRAT |
| Europe | France | AsyncRAT | Cobalt Strike | PrivateLoader |
| Germany | AsyncRAT | DcRAT | Cobalt Strike |
| United Kingdom | AsyncRAT | Cobalt Strike | DcRAT |
| Netherlands | AsyncRAT | Cobalt Strike | GobRAT |
| Poland | AsyncRAT | DcRAT | Cobalt Strike |
| South America | Brazil | QuasarRAT | AsyncRAT | SectopRAT |
| Colombia | AsyncRAT | Rhadamanthys Stealer | DcRAT |
| Peru | Rhadamanthys Stealer | AsyncRAT | PrivateLoader |
| Argentina | AsyncRAT | QuasarRAT | Rhadamanthys Stealer |
| Venezuela | QuasarRAT | Rhadamanthys Stealer | AsyncRAT |
| Asia | India | AsyncRAT | Cobalt Strike | Mythic |
| China | Cobalt Strike | AsyncRAT | QuasarRAT |
| Indonesia | AsyncRAT | QuasarRAT | DcRAT |
| Thailand | AsyncRAT | QuasarRAT | Cobalt Strike |
| Hong Kong | QuasarRAT | Cobalt Strike | Brute Ratel C4 |
| Africa | Angola | QuasarRAT | AsyncRAT | Gh0st RAT |
| Ghana | AsyncRAT | Spylix | QuasarRAT |
| South Africa | AsyncRAT | PrivateLoader | QuasarRAT |
| Republic of the Congo | AsyncRAT | PlugX | QuasarRAT |
| Democratic Republic of Congo | AsyncRAT | PlugX | MoqHao |
| Oceania | Australia | AsyncRAT | Cobalt Strike | DcRAT |
| New Zealand | AsyncRAT | DcRAT | Rhadamanthys Stealer |
| Fiji | AsyncRAT | Stealc | N/A |
| New Caledonia | AsyncRAT | N/A | N/A |
| French Polynesia | AsyncRAT | N/A | N/A |

_**Table 1:** Top three families for the top five countries of each continent (Source: Recorded Future)_

To read the entire analysis, [click here](https://go.recordedfuture.com/hubfs/reports/cta-2025-0228.pdf) to download the report as a PDF.

Related Research (Insikt)

[![TerraStealerV2 and TerraLogger: Golden Chickens' New Malware Families Discovered](https://cms.recordedfuture.com/uploads/format_webp/medium_cta_2025_0501_Blog_Main_Feature_55a0e64897.jpg)\\
\\
Research (Insikt)\\
\\
**TerraStealerV2 and TerraLogger: Golden Chickens' New Malware Families Discovered** \\
\\
Insikt Group reveals two emerging malware strains—TerraStealerV2 and TerraLogger—linked to Golden Chickens, a threat actor behind credential theft and keylogging MaaS platforms. Learn how these tools operate and evolve.\\
\\
View Research (Insikt)](https://www.recordedfuture.com/research/terrastealerv2-and-terralogger)

[![Uncovering MintsLoader With Recorded Future Malware Intelligence Hunting](https://cms.recordedfuture.com/uploads/format_webp/medium_BLOG_cta_2025_0429_Main_Feature_e924c36cbd.jpg)\\
\\
Research (Insikt)\\
\\
**Uncovering MintsLoader With Recorded Future Malware Intelligence Hunting** \\
\\
Discover how MintsLoader operates as a stealthy, obfuscated malware loader distributing GhostWeaver, StealC, and BOINC. Read Recorded Future’s in-depth analysis of its evasion tactics, DGA-based C2s, and use in phishing and drive-by campaigns.\\
\\
View Research (Insikt)](https://www.recordedfuture.com/research/uncovering-mintsloader-with-recorded-future-malware-intelligence-hunting)

[![Iran’s AI Ambitions: Balancing Economic Isolation with National Security Imperatives](https://cms.recordedfuture.com/uploads/format_webp/medium_irans_ai_ambitions_balancing_economic_isolation_national_security_imperatives_151fba814d.png)\\
\\
Research (Insikt)\\
\\
**Iran’s AI Ambitions: Balancing Economic Isolation with National Security Imperatives** \\
\\
Explore how Iran is leveraging AI for cyberwarfare, influence ops, military tech, and domestic surveillance. A deep dive into Tehran’s top-down AI strategy, partnerships with China and Russia, and implications for global security. \\
\\
View Research (Insikt)](https://www.recordedfuture.com/research/irans-ai-ambitions-balancing-economic-isolation-national-security-imperatives)
