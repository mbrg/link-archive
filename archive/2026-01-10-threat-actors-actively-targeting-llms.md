---
date: '2026-01-10'
description: 'GreyNoise''s new product, Block, offers customizable real-time blocklists,
  addressing the rise of targeted attacks on large language models (LLMs). Recent
  intelligence reveals two concerning campaigns: a Server-Side Request Forgery (SSRF)
  campaign exploiting model pull functionalities and webhook integrations, and a methodical
  enumeration campaign probing over 73 LLM endpoints. Attackers employed unique JA4H
  signatures and IPs associated with known vulnerabilities. To mitigate these threats,
  GreyNoise advises implementing strict access controls on model pulls and monitoring
  traffic for suspicious patterns, particularly from the identified malicious IPs
  and tools.'
link: https://www.greynoise.io/blog/threat-actors-actively-targeting-llms
tags:
- threat intelligence
- blocklists
- cybersecurity
- LLM security
- GreyNoise
title: Threat Actors Actively Targeting LLMs
---

GreyNoise Launches Block: Fully configurable, real-time blocklists

[Learn More\\
![](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b5d_arrow-right-icon-black.svg)](https://www.greynoise.io/products/greynoise-block)

[![](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b5c_x-icon-black.svg)](https://www.greynoise.io/blog/threat-actors-actively-targeting-llms#)

[![GreyNoise logo](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f27569d_GN_Logotype_20220410.svg)](https://www.greynoise.io/)

[Login](https://viz.greynoise.io/login)

[Search for free](https://viz.greynoise.io/)

[Get a demo](https://www.greynoise.io/contact/sales)

[Blog](https://www.greynoise.io/blog)

>

[Threat Signals](https://www.greynoise.io/category/vulnerabilities)

Follow us

[Threat Signals](https://www.greynoise.io/category/vulnerabilities)

# Threat Actors Actively Targeting LLMs

boB Rudis

January 8, 2026

![Link to GreyNoise Twitter account](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275a93_like-icon-success.svg)

[![Link to GreyNoise Twitter account](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275a92_like-icon.svg)](https://www.greynoise.io/blog/threat-actors-actively-targeting-llms#)

[![View our Bluesky profile](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/679bf65fd61237e62cf27065_bluesky-icon.svg)](https://bsky.app/intent/compose?text=Threat%20Actors%20Actively%20Targeting%20LLMs%20https%3A%2F%2Fwww.greynoise.io%2Fblog%2Fthreat-actors-actively-targeting-llms)[![View our profile on X](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b13_twitter-logo.png)](https://twitter.com/intent/tweet?text=Threat%20Actors%20Actively%20Targeting%20LLMs&url=https%3A%2F%2Fwww.greynoise.io%2Fblog%2Fthreat-actors-actively-targeting-llms)[![View our LinkedIn profile](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275a81_linkedin-icon.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.greynoise.io%2Fblog%2Fthreat-actors-actively-targeting-llms)

![](https://cdn.prod.website-files.com/667dd40ebb8095e89f27565d/695ff8a02c24b0683aaeae5f_GreyNoise-Blog-LLMs-Attack-1600x900%20(1).png)

Our Ollama honeypot infrastructure captured 91,403 attack sessions between October 2025 and January 2026. Buried in that data: two distinct campaigns that reveal how threat actors are systematically mapping the expanding surface area of AI deployments.

GreyNoise customers have received an Executive Situation Report (SITREP) including IOCs and other valuable intelligence from this investigation. Customers, please check your inbox.

‍

![](https://cdn.prod.website-files.com/667dd40ebb8095e89f27565d/695fecae272a20c62c0a2907_78996d07.png)

This corroborates and extends [Defused’s findings](https://xcancel.com/DefusedCyber/status/2009007964246692130?ct=rw-null).

## The SSRF campaign: Forcing your servers to phone home

The first campaign exploited server-side request forgery vulnerabilities—tricks that force your server to make outbound connections to attacker-controlled infrastructure.

Attackers targeted two vectors:

1. **Ollama's model pull functionality**: Injecting malicious registry URLs that force servers to make HTTP requests to attacker infrastructure
2. **Twilio SMS webhook integrations**: Manipulating MediaUrl parameters to trigger outbound connections (we’re including this since they co-occurred with the Ollama targeting)

The campaign ran from October 2025 through January 2026, with a dramatic spike over Christmas—1,688 sessions in 48 hours. Attackers used ProjectDiscovery's OAST (Out-of-band Application Security Testing) infrastructure to confirm successful SSRF exploitation via callback validation.

Fingerprinting revealed the operation's structure. A single JA4H signature (po11nn060000…) appeared in 99% of attacks, pointing to shared automation tooling—likely Nuclei. The 62 source IPs spread across 27 countries, but consistent fingerprints indicate VPS-based infrastructure, not a botnet.

**Assessment:** Probably security researchers or bug bounty hunters. OAST callbacks are standard vulnerability research techniques. But the scale and Christmas timing suggest grey-hat operations pushing boundaries.

‍

## The enumeration campaign: Building the target list

This is the one that should concern you.

Starting December 28, 2025, two IPs launched a methodical probe of 73+ LLM model endpoints. In eleven days, they generated 80,469 sessions—systematic reconnaissance hunting for misconfigured proxy servers that might leak access to commercial APIs.

The attack tested both OpenAI-compatible API formats and Google Gemini formats. Every major model family appeared in the probe list:

- OpenAI (GPT-4o and variants)
- Anthropic (Claude Sonnet, Opus, Haiku)
- Meta (Llama 3.x)
- DeepSeek (DeepSeek-R1)
- Google (Gemini)
- Mistral
- Alibaba (Qwen)
- xAI (Grok)

Test queries stayed deliberately innocuous with the likely goal to fingerprint which model actually responds without triggering security alerts.

| Prompt | Occurrences |
| --- | --- |
| hi | 32,716 |
| How many states are there in the United States? | 27,778 |
| How many states are there in the United States? What is todays date? What model are you? | 17,979 |
| (empty string) | 8,073 |
| How many letter r are in the word strawberry? | 2,024 |

‍

The infrastructure behind this campaign tells us who we're dealing with:

**45.88.186.70** (AS210558, 1337 Services GmbH): 49,955 sessions **204.76.203.125** (AS51396, Pfcloud UG): 30,514 sessions.

Both IPs appear extensively in GreyNoise data with histories of CVE exploitation: CVE-2025-55182 (React2Shell), CVE-2023-1389, and over 200 other vulnerabilities. Combined observations exceed 4 million sensor hits.

**Assessment:** Professional threat actor conducting reconnaissance. The infrastructure overlap with established CVE scanning operations suggests this enumeration feeds into a larger exploitation pipeline. They're building target lists.

‍

## What to block

### Network fingerprints

| Type | Value | Identifies |
| --- | --- | --- |
| JA4H | po11nn060000... | SSRF campaign tooling |
| JA4T | 64240... | WSL Ubuntu 22.04 systems |
| JA4T | 65495... | Jumbo MTU (VPN/tunnel) |

‍

### OAST callback domains

Block these TLD patterns (580 unique domains observed):

- \*.oast.live
- \*.oast.me
- \*.oast.online
- \*.oast.pro
- \*.oast.fun
- \*.oast.site
- \*.oast.today

‍

### IP addresses

**SSRF campaign (top 3):**

- 134.122.136.119, 134.122.136.96 (AS152194, Japan)
- 112.134.208.214 (AS9329, Sri Lanka)
- 146.70.124.188, 146.70.124.165 (AS9009, Romania)

**LLM enumeration campaign:**

- 45.88.186.70 (AS210558, United States)
- 204.76.203.125 (AS51396, Netherlands)

‍

## Defend your LLM infrastructure

- **Lock down model pulls.** Configure Ollama to accept models only from trusted registries. Egress filtering prevents SSRF callbacks from reaching attacker infrastructure.
- **Detect enumeration patterns.** Alert on rapid-fire requests hitting multiple model endpoints. Watch for the fingerprinting queries: "How many states are there in the United States?" and "How many letter r..."
- **Block OAST at DNS.** Cut off the callback channel that confirms successful exploitation.
- **Rate-limit suspicious ASNs.** AS152194, AS210558, and AS51396 all appeared prominently in attack traffic.
- **Monitor JA4 fingerprints.** The signatures we identified will catch this tooling—and similar automation—targeting your infrastructure.

‍

Eighty thousand enumeration requests represent investment. Threat actors don't map infrastructure at this scale without plans to use that map. If you're running exposed LLM endpoints, you're likely already on someone's list.

This article is a summary of the full, in-depth version on the GreyNoise Labs blog.

[Read the full report](https://www.greynoise.io/blog/threat-actors-actively-targeting-llms#)

![GreyNoise Labs logo](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275a97_GN-Labs_Light_Horizontal.png)

Like or share:

![Link to GreyNoise Twitter account](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275a93_like-icon-success.svg)

[![Link to GreyNoise Twitter account](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275a92_like-icon.svg)](https://www.greynoise.io/blog/threat-actors-actively-targeting-llms#)

[![View our Bluesky profile](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/679bf65fd61237e62cf27065_bluesky-icon.svg)](https://bsky.app/intent/compose?text=Threat%20Actors%20Actively%20Targeting%20LLMs%20https%3A%2F%2Fwww.greynoise.io%2Fblog%2Fthreat-actors-actively-targeting-llms)[![View our profile on X](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b13_twitter-logo.png)](https://twitter.com/intent/tweet?text=Threat%20Actors%20Actively%20Targeting%20LLMs&url=https%3A%2F%2Fwww.greynoise.io%2Fblog%2Fthreat-actors-actively-targeting-llms)[![View our LinkedIn profile](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275a81_linkedin-icon.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.greynoise.io%2Fblog%2Fthreat-actors-actively-targeting-llms)

![](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275a87_sidebar-subscribe-img.svg)

##### Get the latest blog articles delivered right to your inbox.

Thank you! Your submission has been received!

Oops! Something went wrong while submitting the form.

![](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b2e_slack-icon.svg)

Be part of the conversation in our Community Slack group.

[Join us on Slack\\
![](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275985_icon-external-link.svg)](https://join.slack.com/t/greynoiseintel/shared_invite/zt-1wfahv2ac-1NUBYb~GbD_F2xKl9jxzdw)

Follow us and don’t miss a thing.

[![View our Bluesky profile](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/679bf65fd61237e62cf27065_bluesky-icon.svg)](https://bsky.app/profile/greynoise.bsky.social)[![](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275a86_mastodon-icon.svg)](https://infosec.exchange/@greynoise)[![](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275a81_linkedin-icon.svg)](https://www.linkedin.com/company/greynoise)[![X (formerly Twitter) logo](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b13_twitter-logo.png)](https://x.com/GreyNoiseIO)[![YouTube logo](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b14_youtube-logo.png)](https://www.youtube.com/@greynoiseintelligence)[![Join us on Slack!](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b2e_slack-icon.svg)](https://join.slack.com/t/greynoiseintel/shared_invite/zt-1wfahv2ac-1NUBYb~GbD_F2xKl9jxzdw)[![Discord logo](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b18_discord-logo.png)](https://discord.gg/VK9ayHSfAd)[![](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b57_reddit-icon.svg)](https://www.reddit.com/r/GreyNoiseIntelligence/)[![TikTok logo](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b29_tiktok-logo.png)](https://www.tiktok.com/@greynoiseintelligence)[![Subscribe to our RSS feed](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275a80_rs-icon.svg)](https://www.greynoise.io/blog/rss.xml)

## Related content

[View all related articles\\
![Icon depicting right-facing arrow](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275983_icon-link-arrow.svg)](https://www.greynoise.io/blog/threat-actors-actively-targeting-llms#)

[![](https://cdn.prod.website-files.com/667dd40ebb8095e89f27565d/695ff8a02c24b0683aaeae5f_GreyNoise-Blog-LLMs-Attack-1600x900%20(1).png)](https://www.greynoise.io/blog/threat-actors-actively-targeting-llms)

Threat Signals

[**Threat Actors Actively Targeting LLMs**](https://www.greynoise.io/blog/threat-actors-actively-targeting-llms) [boB Rudis\\
\\
Jan 8, 2026](https://www.greynoise.io/blog/threat-actors-actively-targeting-llms)

[![](https://cdn.prod.website-files.com/667dd40ebb8095e89f27565d/6942fc2dfb86982cde1cbd55_GreyNoise-Blog-Cisco-Palo-Alto-Scanning-Dec25-1600x900.png)](https://www.greynoise.io/blog/credential-based-campaign-cisco-palo-alto-networks-vpn-gateways)

Threat Signals

[**Coordinated Credential-Based Campaign Targets Cisco and Palo Alto Networks VPN Gateways**](https://www.greynoise.io/blog/credential-based-campaign-cisco-palo-alto-networks-vpn-gateways) [Noah Stone\\
\\
Dec 17, 2025](https://www.greynoise.io/blog/credential-based-campaign-cisco-palo-alto-networks-vpn-gateways)

[![](https://cdn.prod.website-files.com/667dd40ebb8095e89f27565d/6938510cbb0967e9d784e06c_GreyNoise-React2Shell-Update-1600x900%20(1).png)](https://www.greynoise.io/blog/cve-2025-55182-react2shell-opportunistic-exploitation-in-the-wild-what-the-greynoise-observation-grid-is-seeing-so-far)

Threat Signals

[**CVE-2025-55182 (React2Shell) Opportunistic Exploitation In The Wild: What The GreyNoise Observation Grid Is Seeing So Far**](https://www.greynoise.io/blog/cve-2025-55182-react2shell-opportunistic-exploitation-in-the-wild-what-the-greynoise-observation-grid-is-seeing-so-far) [boB Rudis\\
\\
Dec 5, 2025](https://www.greynoise.io/blog/cve-2025-55182-react2shell-opportunistic-exploitation-in-the-wild-what-the-greynoise-observation-grid-is-seeing-so-far)

[Threat Signals](https://www.greynoise.io/category/vulnerabilities)

Products

- [GreyNoise Block](https://www.greynoise.io/products/greynoise-block)
- [Security Operations](https://www.greynoise.io/products/soc-teams)
- [Vulnerability Management](https://www.greynoise.io/products/vulnerability-management-teams)
- [Threat Hunting](https://www.greynoise.io/products/threat-hunting-teams)
- [Integrations](https://www.greynoise.io/integrations)

Partners

- [GreyNoise Partnerships](https://www.greynoise.io/partners)
- [Reseller Partners](https://www.greynoise.io/partners/reseller-partners)
- [MSSPs](https://www.greynoise.io/partners/mssp-mdr)
- [Technical Alliances](https://www.greynoise.io/partners/technical-alliances)
- [OEM Partners](https://www.greynoise.io/partners/oem-partners)

Resources

- [Blog](https://www.greynoise.io/blog)
- [Resources Library](https://www.greynoise.io/resources)
- [Storm Watch Podcast](https://www.greynoise.io/stormwatch)
- [Tag Request](https://www.greynoise.io/community-tag-request)
- [Documentation](https://docs.greynoise.io/)

Company

- [About](https://www.greynoise.io/about)
- [Press Room](https://www.greynoise.io/press)
- [In the News](https://www.greynoise.io/news)
- [Upcoming Events](https://www.greynoise.io/events)
- [Community](https://www.greynoise.io/community)
- [Careers](https://www.greynoise.io/careers)
- [GreyNoise Love](https://www.greynoise.io/community-love)

© 2025 GreyNoise, Inc. All rights reserved.

![](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275975_White%20Icon.svg)

[![X (formerly Twitter) logo](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b13_twitter-logo.png)](https://x.com/GreyNoiseIO)[![](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275a86_mastodon-icon.svg)](https://infosec.exchange/@greynoise)[![](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275a81_linkedin-icon.svg)](https://www.linkedin.com/company/greynoise)[![YouTube logo](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b14_youtube-logo.png)](https://www.youtube.com/channel/UCenRCNSQ3pCBuWNDOne606w)[![Join us on Slack!](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b2e_slack-icon.svg)](https://join.slack.com/t/greynoiseintel/shared_invite/zt-1wfahv2ac-1NUBYb~GbD_F2xKl9jxzdw)[![Discord logo](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b18_discord-logo.png)](https://discord.com/invite/VK9ayHSfAd)[![](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b57_reddit-icon.svg)](https://www.reddit.com/r/GreyNoiseIntelligence/)[![TikTok logo](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b29_tiktok-logo.png)](https://www.tiktok.com/@greynoiseintelligence)

- [Terms](https://www.greynoise.io/terms)
- [Privacy](https://www.greynoise.io/privacy)
- [Security](https://greynoise.hypercomply.io/)
- [Cookies](https://www.greynoise.io/cookie)
- [Patents](https://www.greynoise.io/patents)
- [Principles](https://www.greynoise.io/principles)

Cookie Settings

We use cookies to ensure you get the best experience on our website. [Learn more](https://www.greynoise.io/cookie)

[Got it](https://www.greynoise.io/blog/threat-actors-actively-targeting-llms#)
