---
date: '2025-11-07'
description: GreyNoise has introduced GreyNoise Block, a customizable real-time blocklist
  service, paralleling their recent deployment of Model Context Protocol (MCP) honeypots.
  The honeypots revealed that no targeted attacks on MCPs occurred, although they
  were quickly discovered by automated scanning. This highlights a current lack of
  deliberate threats but underscores the importance of monitoring baseline traffic
  patterns for anomalies. As advanced attackers leverage AI for operational speed,
  GreyNoise's new tools suggest organizations can enhance defensive capabilities and
  automate threat response. Establishing AI SOCs combining dependable data and AI
  reasoning is crucial to bridge the offense-defense gap.
link: https://www.greynoise.io/blog/deploying-mcp-honeypots
tags:
- GreyNoise
- MCP
- blocklists
- cybersecurity
- AI security
title: What GreyNoise Learned from Deploying MCP Honeypots
---

# What GreyNoise Learned from Deploying MCP Honeypots

Noah Stone

November 5, 2025

![Link to GreyNoise Twitter account](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275a93_like-icon-success.svg)

[![Link to GreyNoise Twitter account](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275a92_like-icon.svg)](https://www.greynoise.io/blog/deploying-mcp-honeypots#)

[![View our Bluesky profile](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/679bf65fd61237e62cf27065_bluesky-icon.svg)](https://bsky.app/intent/compose?text=What%20GreyNoise%20Learned%20from%20Deploying%20MCP%20Honeypots%20https%3A%2F%2Fwww.greynoise.io%2Fblog%2Fdeploying-mcp-honeypots)[![View our profile on X](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b13_twitter-logo.png)](https://twitter.com/intent/tweet?text=What%20GreyNoise%20Learned%20from%20Deploying%20MCP%20Honeypots&url=https%3A%2F%2Fwww.greynoise.io%2Fblog%2Fdeploying-mcp-honeypots)[![View our LinkedIn profile](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275a81_linkedin-icon.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.greynoise.io%2Fblog%2Fdeploying-mcp-honeypots)

![](https://cdn.prod.website-files.com/667dd40ebb8095e89f27565d/6905335bb5a4365c300b0444_GreyNoise-MCP-Honeypot-insights-blog-1600x900.png)

The Model Context Protocol (MCP) lets AI systems securely connect to external data and tools — a key building block for emerging AI-driven operations. It’s also a new piece of internet-facing infrastructure, which means defenders are asking the same question they ask of anything exposed online: _is anyone attacking it yet?_

To find out, **GreyNoise deployed a series of MCP honeypots to observe what actually happens when AI middleware meets the open internet.**

‍

## Testing the Exposure

Each honeypot mimicked a plausible MCP deployment, instrumented for full packet-level visibility. We built three configurations:

- **Unauthenticated endpoint** to capture background scanning.
- **Authenticated endpoint** requiring an API key to detect credential probing.
- **Simulated developer instance** with a deliberately exposed key to see whether anyone followed it.

All were isolated from production systems.

**Every instance was discovered within days** — proof that anything listening on the internet will be found quickly. After that, activity leveled off. We saw the usual: HTTP probes, SSH touches, and other one-shot scans indistinguishable from the constant hum that hits everything else online.

Across the deployment, **no MCP-specific payload or exploitation attempts appeared.**

GreyNoise’s broader MCP Scanner tag, which tracks reconnaissance against MCP endpoints, shows that threat actors are indeed discovering exposed MCP servers — and increasingly so.

‍

## A Controlled Exception

In October 2025, independent researchers [demonstrated](https://www.theregister.com/2025/10/21/mcp_prompt_hijacking_attack/) a prompt-hijacking flaw in a custom MCP build that used a deprecated protocol handler. It was a contained proof-of-concept, not an attack in the wild — and it supports the same conclusion: present-day MCP exposure risk lies in implementation errors, not in deliberate targeting of MCPs as a class.

‍

## Why “Nothing Happened” Still Matters

**Sometimes the absence of activity is the signal.** Knowing what “normal” internet noise looks like gives defenders a baseline to detect the first real deviation — the point where interest becomes intent. Today, MCP traffic sits squarely within that background noise. When that changes, we’ll see it.

‍

## AI, Asymmetry, and the Modern SOC

While defenders experiment with AI-enabled workflows, advanced adversaries are doing the same. **Some threat actors are reportedly using MCP-style architectures to process stolen telemetry and correlate infrastructure, perhaps faster than human analysts could.**

That marks a growing asymmetry: machine-speed offense versus human-speed defense. **Bridging that gap requires AI SOCs** — operations centers where AI agents assist analysts using verified, transparent data rather than opaque automation.

MCP offers one path to that balance: a structured, auditable way for both humans and AI systems to access and reason over trustworthy intelligence. **Defensive AI only works when its data can be traced and its reasoning explained, and findings evidenced.**

‍

## The Takeaway

**GreyNoise’s MCP honeypot experiment found no evidence of targeted attacks on AI middleware.** MCPs are being noticed, but not pursued — yet.

This quiet defines the current baseline for AI middleware exposure. For defenders building toward AI-assisted operations, that baseline is the starting point.

‍

## Use GreyNoise’s MCP Server

**GreyNoise recently** [**launched**](https://www.labs.greynoise.io/mcp/) **its own MCP server**, intentionally connected only to our API to ensure sound security. Human analysts and AI agents alike can use our MCP server to explore GreyNoise’s telemetry, automate jobs, and more.

Pair GreyNoise’s MCP server with our new offering, [GreyNoise Block](https://www.greynoise.io/products/greynoise-block), to **automate dynamic IP blocking based on custom deviations from baseline threat activity.**

This article is a summary of the full, in-depth version on the GreyNoise Labs blog.

[Read the full report](https://www.greynoise.io/blog/deploying-mcp-honeypots#)

![GreyNoise Labs logo](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275a97_GN-Labs_Light_Horizontal.png)

Like or share:

![Link to GreyNoise Twitter account](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275a93_like-icon-success.svg)

[![Link to GreyNoise Twitter account](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275a92_like-icon.svg)](https://www.greynoise.io/blog/deploying-mcp-honeypots#)

[![View our Bluesky profile](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/679bf65fd61237e62cf27065_bluesky-icon.svg)](https://bsky.app/intent/compose?text=What%20GreyNoise%20Learned%20from%20Deploying%20MCP%20Honeypots%20https%3A%2F%2Fwww.greynoise.io%2Fblog%2Fdeploying-mcp-honeypots)[![View our profile on X](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b13_twitter-logo.png)](https://twitter.com/intent/tweet?text=What%20GreyNoise%20Learned%20from%20Deploying%20MCP%20Honeypots&url=https%3A%2F%2Fwww.greynoise.io%2Fblog%2Fdeploying-mcp-honeypots)[![View our LinkedIn profile](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275a81_linkedin-icon.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.greynoise.io%2Fblog%2Fdeploying-mcp-honeypots)

![](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275a87_sidebar-subscribe-img.svg)

##### Get the latest blog articles delivered right to your inbox.

Thank you! Your submission has been received!

Oops! Something went wrong while submitting the form.

![](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b2e_slack-icon.svg)

Be part of the conversation in our Community Slack group.

[Join us on Slack\\
![](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275985_icon-external-link.svg)](https://join.slack.com/t/greynoiseintel/shared_invite/zt-1pz66753m-gakjNlolL6bbPuqfjnm3pg)

Follow us and don’t miss a thing.

[![View our Bluesky profile](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/679bf65fd61237e62cf27065_bluesky-icon.svg)](https://bsky.app/profile/greynoise.bsky.social)[![](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275a86_mastodon-icon.svg)](https://infosec.exchange/@greynoise)[![](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275a81_linkedin-icon.svg)](https://www.linkedin.com/company/greynoise)[![X (formerly Twitter) logo](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b13_twitter-logo.png)](https://x.com/GreyNoiseIO)[![YouTube logo](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b14_youtube-logo.png)](https://www.youtube.com/@greynoiseintelligence)[![Join us on Slack!](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b2e_slack-icon.svg)](https://join.slack.com/t/greynoiseintel/shared_invite/zt-1pz66753m-gakjNlolL6bbPuqfjnm3pg)[![Discord logo](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b18_discord-logo.png)](https://discord.gg/VK9ayHSfAd)[![](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b57_reddit-icon.svg)](https://www.reddit.com/r/GreyNoiseIntelligence/)[![TikTok logo](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b29_tiktok-logo.png)](https://www.tiktok.com/@greynoiseintelligence)[![Subscribe to our RSS feed](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275a80_rs-icon.svg)](https://www.greynoise.io/blog/rss.xml)

## Related content

[View all related articles\\
![Icon depicting right-facing arrow](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275983_icon-link-arrow.svg)](https://www.greynoise.io/blog/deploying-mcp-honeypots#)

[![](https://cdn.prod.website-files.com/667dd40ebb8095e89f27565d/6905335bb5a4365c300b0444_GreyNoise-MCP-Honeypot-insights-blog-1600x900.png)](https://www.greynoise.io/blog/deploying-mcp-honeypots)

Insights

[**What GreyNoise Learned from Deploying MCP Honeypots**](https://www.greynoise.io/blog/deploying-mcp-honeypots) [Noah Stone\\
\\
Nov 5, 2025](https://www.greynoise.io/blog/deploying-mcp-honeypots)

[![](https://cdn.prod.website-files.com/667dd40ebb8095e89f27565d/67697664ffcfd0b6b8b75c42_twice.png)](https://www.greynoise.io/blog/checking-it-twice-profiling-benign-internet-scanners----2024-edition)

Insights

[**Checking It Twice: Profiling Benign Internet Scanners — 2024 Edition**](https://www.greynoise.io/blog/checking-it-twice-profiling-benign-internet-scanners----2024-edition) [boB Rudis\\
\\
Dec 23, 2024](https://www.greynoise.io/blog/checking-it-twice-profiling-benign-internet-scanners----2024-edition)

[![](https://cdn.prod.website-files.com/667dd40ebb8095e89f27565d/67463ba3ee993327b386fc69_blog_comms-1.png)](https://www.greynoise.io/blog/from-help-desk-to-ciso-how-communication-shapes-security-success)

Insights

[**From Help Desk to CISO: How Communication Shapes Security Success**](https://www.greynoise.io/blog/from-help-desk-to-ciso-how-communication-shapes-security-success) [boB Rudis\\
\\
Nov 27, 2024](https://www.greynoise.io/blog/from-help-desk-to-ciso-how-communication-shapes-security-success)

[Insights](https://www.greynoise.io/category/insights)

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

[![X (formerly Twitter) logo](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b13_twitter-logo.png)](https://x.com/GreyNoiseIO)[![](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275a86_mastodon-icon.svg)](https://infosec.exchange/@greynoise)[![](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275a81_linkedin-icon.svg)](https://www.linkedin.com/company/greynoise)[![YouTube logo](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b14_youtube-logo.png)](https://www.youtube.com/channel/UCenRCNSQ3pCBuWNDOne606w)[![Join us on Slack!](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b2e_slack-icon.svg)](https://join.slack.com/t/greynoiseintel/shared_invite/zt-1pz66753m-gakjNlolL6bbPuqfjnm3pg)[![Discord logo](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b18_discord-logo.png)](https://discord.com/invite/VK9ayHSfAd)[![](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b57_reddit-icon.svg)](https://www.reddit.com/r/GreyNoiseIntelligence/)[![TikTok logo](https://cdn.prod.website-files.com/667dd40ebb8095e89f275639/667dd40ebb8095e89f275b29_tiktok-logo.png)](https://www.tiktok.com/@greynoiseintelligence)

- [Terms](https://www.greynoise.io/terms)
- [Privacy](https://www.greynoise.io/privacy)
- [Security](https://greynoise.hypercomply.io/)
- [Cookies](https://www.greynoise.io/cookie)
- [Patents](https://www.greynoise.io/patents)
- [Principles](https://www.greynoise.io/principles)

Cookie Settings

We use cookies to ensure you get the best experience on our website. [Learn more](https://www.greynoise.io/cookie)

[Got it](https://www.greynoise.io/blog/deploying-mcp-honeypots#)
