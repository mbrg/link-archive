---
date: '2026-03-26'
description: A recent investigation into Iranian cyber operations reveals a sophisticated
  landscape of state-aligned threat actors leveraging obfuscated infrastructure, often
  utilizing Cloudflare for masking origins. Tools like PowerShell dropper scripts
  and blockchain communications were identified among the campaigns, notably within
  the MuddyWater and Dark Scepter APT groups. The study underscores the importance
  of infrastructure-level intelligence, highlighting systemic patterns in ASNs, domain
  usage, and behaviors that allow for early detection and proactive defense against
  future intrusions. Critical sectors, particularly in the U.S. and Israel, must enhance
  monitoring of remote access technologies and spoofed domains.
link: https://hunt.io/blog/iranian-apt-infrastructure-state-aligned-clusters
tags:
- Iranian cyber threats
- cybersecurity
- infrastructure analysis
- ransomware
- APT
title: 'Iranian APT Infrastructure in Focus: Mapping State-Aligned Clusters During
  Geopolitical Escalation'
---

[TheGentlemen Ransomware Exposed on Russian Proton66 Server: Complete Toolkit, Victim Credentials, and Ngrok Tokens](https://hunt.io/blog/thegentlemen-ransomware-toolkit-russian-proton66-server)

[Learn More](https://hunt.io/blog/thegentlemen-ransomware-toolkit-russian-proton66-server)

[Hunt.io](https://hunt.io/)

[Product](https://hunt.io/products)

[Features](https://hunt.io/features)

[OEM](https://hunt.io/oem)

[Pricing](https://hunt.io/pricing)

[About](https://hunt.io/about)

[Blog](https://hunt.io/blog)

[Login](https://app.hunt.io/login)

[Get a Demo](https://hunt.io/get-started)

To embed a website or widget, add it to the properties panel.

[Home](https://hunt.io/)

[Blog](https://hunt.io/blog)

Iranian APT Infrastructure in Focus: Mapping State-Aligned Clusters During Geopolitical Escalation

# Iranian APT Infrastructure in Focus: Mapping State-Aligned Clusters During Geopolitical Escalation

Published on

Mar 4, 2026

![Iranian APT Infrastructure in Focus:  Mapping State-Aligned Clusters During Geopolitical Escalation](https://framerusercontent.com/images/Oqi8bQwplQgryBuVlzAtxHeelEE.png?width=1440&height=540)

TABLE OF CONTENTS

[Iranian Threat Actors Currently Tracked in Hunt.io](https://hunt.io/blog/iranian-apt-infrastructure-state-aligned-clusters#Iranian_Threat_Actors_Currently_Tracked_in_Huntio) [Infrastructure Patterns Observed](https://hunt.io/blog/iranian-apt-infrastructure-state-aligned-clusters#Infrastructure_Patterns_Observed) [How to Track These Actors with Hunt.io](https://hunt.io/blog/iranian-apt-infrastructure-state-aligned-clusters#How_to_Track_These_Actors_with_Huntio) [What U.S. and Israeli Organizations Should Monitor](https://hunt.io/blog/iranian-apt-infrastructure-state-aligned-clusters#What_US_and_Israeli_Organizations_Should_Monitor) [Indicators of Compromise (IOCs)](https://hunt.io/blog/iranian-apt-infrastructure-state-aligned-clusters#Indicators_of_Compromise_IOCs) [Conclusion](https://hunt.io/blog/iranian-apt-infrastructure-state-aligned-clusters#Conclusion)

Tensions between the United States, Israel, and Iran have reached a critical point following a series of diplomatic breakdowns, which led to [escalating](https://www.state.gov/releases/office-of-the-spokesperson/2026/03/secretary-of-state-marco-rubio-remarks-to-press-6) military exchanges and proxy engagements across the Middle East. History has shown that when hostilities rise to this degree, cyber operations do not lag far behind kinetic activity. They precede it.

These operations, whether infrastructure reconnaissance, pre-positioning, or network intrusion, are part of the operational groundwork of modern conflict. Disrupting communications and compromising critical systems can weaken response capabilities long before physical engagement begins. Iranian state-aligned actors have [historically](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4229506/nsa-cisa-fbi-and-dc3-warn-iranian-cyber-actors-may-target-vulnerable-us-network/) targeted energy, financial services, government networks, and defense-related organizations across the U.S., Israel, and allied regions.

This post does not attempt to assess the political dimensions of the conflict. Instead, it focuses on infrastructure-level intelligence such as ASN patterns, TLS fingerprints, and hosting clusters derived from Hunt.io. While many indicators originate from public reporting, infrastructure scanning and behavioral clustering can expand them into wider operational patterns.

Understanding these patterns is what enables proactive defense to see the threat coming before it hits. To illustrate how this plays out in real operations, we first examine several Iranian-linked threat actors currently tracked within Hunt.io.

## Iranian Threat Actors Currently Tracked in Hunt.io

Hunt.io continuously extracts high-value IOCs such as IP addresses, hosts, and SHA-256 hashes from a wide range of OSINT sources and consolidates them into a single, structured view. [19 threat groups linked to Iran](https://app.hunt.io/threat-actors/listing?country=IR&page=1) are currently tracked by Hunt.

By normalizing and linking this data at the threat actor level, analysts can quickly pivot between infrastructure, artifacts, and campaigns, reducing the time needed to move from attribution to actionable hunting and detection.

![Figure 1](https://public-hunt-static-blog-assets.s3.us-east-1.amazonaws.com/3-2026/Iranian+APT+Infrastructure+in+Focus+Mapping+State-Aligned+Clusters+During+Geopolitical+Escalation+-+figure+1.png)Figure 1: Overview of Iranian threat actor profiles containing IPs, hosts, and sample hashes

These actors represent a mix of state-aligned and hacktivist-motivated operations, with campaigns ranging from espionage and credential harvesting to ransomware and attacks targeting critical infrastructure.

![Figure 2](https://public-hunt-static-blog-assets.s3.us-east-1.amazonaws.com/3-2026/Iranian+APT+Infrastructure+in+Focus++Mapping+State-Aligned+Clusters+During+Geopolitical+Escalation+-+figure+2.png)Figure 2: Profile for MuddyWater APT group

Current infrastructure intelligence identifies **264 total IPs**, **432 hosts**, and **128 related SHA-256 hashes** attributed to [MuddyWater](https://app.hunt.io/threat-actors/MuddyWater). Activity observed as recently as the end of January highlighted a persistent campaign targeting organizations in the Middle East and North Africa (MENA). Research also suggested domain reuse dating back to October 2025.

![Figure 3](https://public-hunt-static-blog-assets.s3.us-east-1.amazonaws.com/3-2026/Iranian+APT+Infrastructure+in+Focus++Mapping+State-Aligned+Clusters+During+Geopolitical+Escalation+-+figure+3.png)Figure 3: VoidManticore profile showing the most recent IPs and hosts

[VoidManticore](https://app.hunt.io/threat-actors/Void%20Manticore) includes a footprint of **13 tracked IPs**, **1 associated host**, and **91 SHA-256 hashes**. Recent reporting involves the exploitation of an **Omani government mailbox** to facilitate the delivery of malicious Microsoft Word documents focusing on critical infrastructure and government entities worldwide.

![Figure 4](https://public-hunt-static-blog-assets.s3.us-east-1.amazonaws.com/3-2026/Iranian+APT+Infrastructure+in+Focus++Mapping+State-Aligned+Clusters+During+Geopolitical+Escalation+-+figure+4.png)Figure 4: Screenshot of APT42 profile page

[APT42](https://app.hunt.io/threat-actors/APT42), also known as Charming Cypress or Mint Sandstorm, links to **54 IPs**, **233 total hosts**, and **44 SHA-256 hashes**. Analysis of recent campaigns introduces TameCat, a modular, PowerShell-based backdoor used to target **senior defense and government officials**.

![Figure 5](https://public-hunt-static-blog-assets.s3.us-east-1.amazonaws.com/3-2026/Iranian+APT+Infrastructure+in+Focus++Mapping+State-Aligned+Clusters+During+Geopolitical+Escalation+-+figure+5.png)Figure 5: Most recent activity linked to APT35 as identified by Hunt

High-value IOCs revealed **79 IPs**, **2,211 hosts**, and **67 SHA-256 hashes** attributed to [APT35](https://app.hunt.io/threat-actors/APT35). This threat actor has used WhatsApp to distribute spear-phishing messages using spoofed websites to steal the credentials of security and defense-related individuals. In late 2025, a trove of documents and information linked to APT35 was leaked, including C2 infrastructure IPs, usernames, and passwords, and more.

![Figure 6](https://public-hunt-static-blog-assets.s3.us-east-1.amazonaws.com/3-2026/Iranian+APT+Infrastructure+in+Focus++Mapping+State-Aligned+Clusters+During+Geopolitical+Escalation+-+figure+6.png)Figure 6: Infy group actor profile page

[Infy](https://app.hunt.io/threat-actors/Infy) has a footprint of **18 IPs**, **53 associated hosts**, and **58 SHA-256 hashes**. Following recent campaign shifts, the group has been observed using updated Foudre and Tonnerre variants to target **Iranian dissidents** and **regional government entities**, leveraging Telegram-based C2 to bypass defenses.

![Figure 7](https://public-hunt-static-blog-assets.s3.us-east-1.amazonaws.com/3-2026/Article_img_Infrastructure+Pattern+Comparison+Across+Iranian-Linked+Actors.png)Figure 7: Infrastructure Pattern Comparison Across Iranian-Linked Actors

## Infrastructure Patterns Observed

Across intrusion campaigns, network infrastructure is an operational requirement for any threat actor communicating with target systems. While provisioning that infrastructure, actors frequently, sometimes unknowingly, leave behind patterns that defenders can fingerprint and track in real-time.

Clustering on behaviors such as repeated use of specific autonomous systems (AS), hosting providers, certificate authorities, and domain registrars can enable C2/threat group tracking well beyond reported indicators of compromise.

The following examines these patterns as observed through Hunt.io's [Attack Capture](https://hunt.io/features/attackcapture) feature, beginning with a known MuddyWater IP identified in the above threat actor profile page.

Also referred to as Mango Sandstorm, [MuddyWater APT](https://hunt.io/malware-families/muddywater-apt), and other Iranian state-linked groups have displayed a preference for including NameCheap and Hosterdaddy Private Limited (AS136557).

Although additional ASNs have appeared in historical reporting, these two providers recur with enough frequency to serve as high-confidence infrastructure clustering pivots. This is particularly valuable when combined with recurring use of offensive tools unique to Iranian APTs like remote monitoring and management (RMM), PowerShell scripts, etc.

[Open directory](https://hunt.io/glossary/open-directories) listings are among the highest-value findings in infrastructure hunting. A misconfigured server offers not only an inventory of attacker tooling, but a window into the mindset of how network intrusions are conducted. In Attack Capture, file hashes can be pivoted to find if any other servers are hosting the same file.

Hosted on NameCheap, [209.74.87\[.\]100](https://app.hunt.io/file-manager?host=http://209.74.87.100:8000) is present in the MuddyWater threat actor profile page on 20 February.

![Figure 8](https://public-hunt-static-blog-assets.s3.us-east-1.amazonaws.com/3-2026/Iranian+APT+Infrastructure+in+Focus++Mapping+State-Aligned+Clusters+During+Geopolitical+Escalation+-+figure+7.png)Figure 8: Attack Capture file manager for open directory hosted at 209.74.87\[.\]100

Among the thousands of exposed artifacts on the server was FMAPP.exe, a proxy binary used as a tunneling component.

Pivoting on the file hash (SHA-256: e25892603c42e34bd7ba0d8ea73be600d898cadc290e3417a82c04d6281b743b) resulted in a single IP not previously reported, [157.20.182\[.\]49](https://app.hunt.io/file-manager?host=http://157.20.182.49:8000).

![Figure 9](https://public-hunt-static-blog-assets.s3.us-east-1.amazonaws.com/3-2026/Iranian+APT+Infrastructure+in+Focus++Mapping+State-Aligned+Clusters+During+Geopolitical+Escalation+-+figure+8.png)Figure 9: SHA-256 hash pivot result on FMAPP.exe, showing an additional IP

Consistent with MuddyWater's established AS pattern, the above IP is hosted on the Hosterdaddy Private Limited network and is another server within this wider cluster. Similar to the initial directory, many of the exposed files consisted of offensive tooling.

![Figure 10](https://public-hunt-static-blog-assets.s3.us-east-1.amazonaws.com/3-2026/Iranian+APT+Infrastructure+in+Focus++Mapping+State-Aligned+Clusters+During+Geopolitical+Escalation+-+figure+9.png)Figure 10: Snippet of the files available for download from 157.20.182\[.\]49

The directory remained accessible until February 26. Several days later, on March 2, our network scans identified a [Sliver C2](https://hunt.io/malware-families/sliver) server on port 31337. The C2's presence was only captured for a single day. It remains unclear whether MuddyWater is actively operating the Sliver C2 instance, but as the below will explain, it appears the group may be using openly available tooling to blend in with cybercriminals and other actors.

![Figure 11](https://public-hunt-static-blog-assets.s3.us-east-1.amazonaws.com/3-2026/Iranian+APT+Infrastructure+in+Focus++Mapping+State-Aligned+Clusters+During+Geopolitical+Escalation+-+figure+10.png)Figure 11: Identification of Sliver C2 on port 31337 on [157.20.182\[.\]49](https://app.hunt.io/ip/157.20.182.49)

Of note, two files from the directory jumped out as interesting/suspicious and required further analysis:

- udp\_3.0.py: A custom Python-based UDP command and control server using a lightweight symmetric cipher for communications over port 1269.

- reset.ps1: Multi-stage PowerShell dropper and installer, responsible for downloading JavaScript payloads, including Node.js runtime dependencies.


Particularly interesting was the dropper's explicit dependency on ethers.js and the WebSocket library, indicating Ethereum-based infrastructure as a communications component. Upon execution, reset.ps1 communicates with [185.236.25\[.\]119:3001](https://app.hunt.io/ip/185.236.25.119) using websockets. This IP is identified as high risk in Hunt due to login to Tsundere botnet panels on ports 80 and 3000.

![Figure 12](https://public-hunt-static-blog-assets.s3.us-east-1.amazonaws.com/3-2026/Iranian+APT+Infrastructure+in+Focus++Mapping+State-Aligned+Clusters+During+Geopolitical+Escalation+-+figure+11.png)Figure 12: C2 is linked to reset.ps1 is also identified as hosting Tsundere botnet panels

Starting with a single IP address, infrastructure pivoting uncovered two additional servers within the same hosting cluster, including a node potentially leveraging blockchain-related libraries for command-and-control communications.

Additionally, it appears MuddyWater is using publicly available malware likely to blend in with cybercriminals. Target-referenced files related to a UAE engineering company found within the .49 directory further strengthened the assessment of campaign alignment.

This activity is consistent with previously documented MuddyWater infrastructure patterns and overlaps known hosting and tooling behaviors attributed to the group.

## How to Track These Actors with Hunt.io

The earlier MuddyWater example demonstrated how pivoting from IP to hash to ASN can expose wider infrastructure clusters tied to an actor. The same clustering logic applies across other Iranian-linked groups.

In this section, we extend that approach using [HuntSQL](https://hunt.io/features/hunt-sql) and examine Dark Scepter, a recently identified actor overlapping APT34 (OilRig).

Reviewing C2 domains linked to Dark Scepter showed Cloudflare being used to proxy infrastructure and obscure origin IP addresses. Cloudflare fronting is common among Iranian-aligned operators, which makes certificate Subject Alternative Name (SAN) pivoting especially valuable for revealing backend servers.

While CDN fronting can delay direct attribution, the underlying domain frequently appears as a SAN entry on certificates issued elsewhere. Pivoting on certificate hostnames often exposes the real infrastructure behind the proxy.

Using the C2 domain web14\[.\]info as an example, we pivot on certificate hostnames to identify the likely backend server.

Example Query:

```sql
SELECT
  ip,
  port,
  hostnames
FROM
  certificates
WHERE
  hostnames RLIKE 'web[0-9]{2}.info[^a-zA-Z0-9.]'
  AND timestamp > '2026-02-01'
group by
  ip,
  port,
  hostnames

                Copy
```

Example Output:

![Figure 13](https://public-hunt-static-blog-assets.s3.us-east-1.amazonaws.com/3-2026/Iranian+APT+Infrastructure+in+Focus++Mapping+State-Aligned+Clusters+During+Geopolitical+Escalation+-+figure+12.png)Figure 13: HuntSQL [query](https://app.hunt.io/sql?page=1&pageSize=100&query=SELECT%0A%20%20ip%2C%0A%20%20port%2C%0A%20%20hostnames%0AFROM%0A%20%20certificates%0AWHERE%0A%20%20hostnames%20RLIKE%20%27web%5B0-9%5D%7B2%7D.info%5B%5Ea-zA-Z0-9.%5D%27%0A%20%20AND%20timestamp%20%3E%20%272026-02-01%27%0Agroup%20by%0Aip%2C%0Aport%2C%0Ahostnames%0A) to locate the real IP used by Dark Scepter

The query, which uses regex to look for all occurrences of web\*.info, identifies actor-controlled infrastructure hosted on M247 Europe SRL at [38.180.239\[.\]161](https://app.hunt.io/ip/38.180.239.161). From the results, we also see several domains listed as hostnames. Some of these domains have previously appeared in public reporting, including [Maltrail](https://github.com/stamparm/maltrail/commit/b1746197022348b4cbbdacbc3271f1620f737d0b).

- anythingshere\[.\]shop

- cside\[.\]site

- footballfans\[.\]asia

- menclub\[.\]lt

- musiclivetrack\[.\]website

- stone110\[.\]store

- web14\[.\]info


A review of the webpage details on [38.180.239\[.\]161](https://app.hunt.io/ip/38.180.239.161) reveals a unique title, "Wonders Above". To further pivot on these new findings, we can build an additional HuntSQL query to determine how prevalent this title is across the internet and whether it is a solid hunting query.

![Figure 14](https://public-hunt-static-blog-assets.s3.us-east-1.amazonaws.com/3-2026/Iranian+APT+Infrastructure+in+Focus++Mapping+State-Aligned+Clusters+During+Geopolitical+Escalation+-+figure+13.png)Figure 14: Example webpage when making a GET request to the attacker-controlled IP, 38.180.239\[.\]161

Example Query:

```sql
SELECT
  ip,
  port
FROM
  httpv2
WHERE
  html.head.title LIKE '%Wonders Above%'
group by
  ip,
  port

                Copy
```

Example Output:

![Figure 15](https://public-hunt-static-blog-assets.s3.us-east-1.amazonaws.com/3-2026/Iranian+APT+Infrastructure+in+Focus++Mapping+State-Aligned+Clusters+During+Geopolitical+Escalation+-+figure+14.png)Figure 15: HuntSQL [query](https://app.hunt.io/sql?page=1&pageSize=100&query=SELECT%0A%20%20ip%2C%0A%20%20port%0AFROM%0A%20%20httpv2%0AWHERE%0A%20%20html.head.title%20LIKE%20%27%25Wonders%20Above%25%27%0Agroup%20by%0Aip%2C%0Aport%0A) results for servers hosting the 'Wonders Above' page

The results returned two additional IP addresses using either port 443, 2053, 2083, or 2096, plus the server we started with in the previous query. The new servers share the same webpage and Let's Encrypt certificates with multiple hostnames as seen below:

- [92.243.65\[.\]243](https://app.hunt.io/ip/92.243.65.243)

- [185.76.79\[.\]125](https://app.hunt.io/ip/185.76.79.125)


The virtual servers are hosted on Akton d.o.o. (AS25467), and EDIS GmbH (AS57169), respectively. Observed domain names: justweb\[.\]click, girlsbags\[.\]shop, lecturegenieltd\[.\]pro, ntcx\[.\]pro, and retseptik\[.\]info.

Pivoting on reused webpages and certificate hostnames is a reliable way to track not only Dark Scepter and other Iranian groups, but a majority of threat actors who think simply moving their C2 infrastructure behind Cloudflare will deter defenders.

## What U.S. and Israeli Organizations Should Monitor

Iranian state-linked actors have consistently targeted organizations aligned with national intelligence priorities and those deemed as a threat. For U.S. and Israeli entities, the sectors of greatest exposure are government agencies, defense contractors, energy and utilities operators, university and policy institutions, and financial services.

### Monitoring Recommendations

Defenders should prioritize monitoring the following:

- VPN and remote access appliances: Monitor for anomalous geolocation shifts, ASN changes, and authentication attempts tied to high-risk hosting networks.

- Suspicious emails: Enforce MFA across all users and monitor for OAuth abuse, token replay, and credential harvesting patterns.

- Spoofed domains: Continuously scan for typosquatting domains and certificate reuse tied to defense, energy, and government keywords.

- ASN-based monitoring: Track infrastructure originating from repeatedly observed Iranian-linked ASNs such as Hosterdaddy Private Limited (AS136557).

- TLS fingerprinting: Leverage JARM and [JA4x fingerprint](https://hunt.io/glossary/ja4-fingerprinting) clustering within HuntSQL to detect backend infrastructure reuse behind CDN proxies.


## Indicators of Compromise (IOCs)

The infrastructure uncovered throughout this investigation reveals several previously unreported hosts, domains, and servers linked to Iranian-aligned operations.

The indicators below represent a subset of the infrastructure identified during this analysis. Additional indicators and actor infrastructure can be explored directly through Hunt.io threat actor profiles.

| IP addresses | Details |
| --- | --- |
| 209.74.87\[.\]100 | Open directory IP found in MuddyWater threat actor profile |
| 157.20.182\[.\]49 | Additional IP/open directory sharing the same file (FMAPP.exe) as 209.74.87\[.\]100 |
| 185.236.25\[.\]119 | C2 for reset.ps1, a PowerShell loader found in 157.20.182\[.\]49 |
| 38.180.239\[.\]161 | Attacker-controlled IP linked to Dark Scepter hidden behind Cloudflare |
| 92.243.65\[.\]243 | Secondary IP linked to 38.180.239\[.\]161 when pivoting on web page titles. |
| 185.76.79\[.\]125 | Tertiary IP linked to the two above sharing the same web titles and TLS certificates |

| Domains | Details |
| --- | --- |
| anythingshere\[.\]shop | Dark Scepter C2 domain |
| cside\[.\]site | Dark Scepter C2 domain |
| footballfans\[.\]asia | Dark Scepter C2 domain |
| menclub\[.\]lt | Dark Scepter C2 domain |
| musiclivetrack\[.\]website | Dark Scepter C2 domain |
| stone110\[.\]store | Dark Scepter C2 domain |
| web14\[.\]info | Initial C2 domain linked to Dark Scepter |
| justweb\[.\]click | Dark Scepter C2 domain |
| girlsbags\[.\]shop | Dark Scepter C2 domain |
| lecturegenieltd\[.\]pro | Dark Scepter C2 domain |
| ntcx\[.\]pro | Dark Scepter C2 domain |
| retseptik\[.\]info | Dark Scepter C2 domain |

## Conclusion

Network intrusions rarely begin with exploitation. They begin with infrastructure provisioning, staging, and reconnaissance that often occurs weeks before any direct interaction with a target. The indicators documented in this assessment surfaced through proactive infrastructure clustering and behavioral pivoting, not reactive post-incident reporting.

Once an IP address or domain becomes widely published, operators have typically already rotated infrastructure. Monitoring ASN patterns, certificate reuse, hosting clusters, and hash overlaps shifts detection earlier in the intrusion lifecycle, where disruption is still possible. Infrastructure intelligence is not about reacting faster. It is about seeing earlier.

**If your organization, industry, or national infrastructure is exposed to these types of campaigns, Hunt.io can help you identify and track the infrastructure behind them.**

**[Get in touch](https://hunt.io/get-started) with our team to learn how Hunt.io supports proactive threat hunting and infrastructure monitoring.**

Related Posts

[Threat Research\\
\\
![](https://framerusercontent.com/images/E0b6Kg54NokYFQzb7rI7GCb02kY.png?width=961&height=540)](https://hunt.io/blog/apt-muddywater-deploys-multi-stage-phishing-to-target-cfos)

Aug 20, 2025

•

16

min read

### [APT MuddyWater Deploys Multi-Stage Phishing to Target CFOs](https://hunt.io/blog/apt-muddywater-deploys-multi-stage-phishing-to-target-cfos)

[Read Article](https://hunt.io/blog/apt-muddywater-deploys-multi-stage-phishing-to-target-cfos)

Threat Research

[Threat Research\\
\\
![](https://framerusercontent.com/images/J5gYF4NCcr0kmuZkJXcOw8u7QRs.png?width=961&height=540)](https://hunt.io/blog/practical-guide-unconvering-malicious-infrastructure)

Mar 9, 2026

•

16

min read

### [A Practical Guide to Uncovering Malicious Infrastructure With Hunt.io](https://hunt.io/blog/practical-guide-unconvering-malicious-infrastructure)

[Read Article](https://hunt.io/blog/practical-guide-unconvering-malicious-infrastructure)

Threat Research

[Threat Research\\
\\
![](https://framerusercontent.com/images/nFO1imdvlzD60VbaFyt5XANMOLM.png?width=961&height=540)](https://hunt.io/blog/china-hosting-malware-c2-infrastructure)

Jan 14, 2026

•

15

min read

### [Inside China’s Hosting Ecosystem: 18,000+ Malware C2 Servers Mapped Across Major ISPs](https://hunt.io/blog/china-hosting-malware-c2-infrastructure)

[Read Article](https://hunt.io/blog/china-hosting-malware-c2-infrastructure)

Threat Research

[Threat Hunting Platform](https://hunt.io/)

©2026 Hunt Intelligence, Inc.

Explore

[Product](https://hunt.io/products)

[Features](https://hunt.io/features)

[OEM Partners](https://hunt.io/oem)

[Pricing](https://hunt.io/pricing)

[Integrations](https://hunt.io/integrations)

Resources

[Blog](https://hunt.io/blog)

[Change log](https://hunt.io/changelog)

[Support Docs](https://hunt.io/support)

[Service Status](https://status.hunt.io/)

[Malware Families](https://hunt.io/malware-families)

[Glossary](https://hunt.io/glossary)

Company

[About Us](https://hunt.io/about)

[Use Cases](https://hunt.io/use-cases)

[Testimonials](https://hunt.io/reviews)

[Branding](https://hunt.io/logo-and-branding)

[Contact Us](https://hunt.io/contact-us)

[Terms and conditions](https://hunt.io/terms-of-service)

[Privacy Policy](https://hunt.io/privacy-policy)
