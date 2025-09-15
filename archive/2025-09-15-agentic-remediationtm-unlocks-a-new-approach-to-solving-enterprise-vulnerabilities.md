---
date: '2025-09-15'
description: Zafran Labs introduces Agentic Remediation™, an AI-driven approach to
  tackle enterprise vulnerabilities. It automates vulnerability assessment and remediation,
  addressing the rise of AI-enhanced cyber threats. The system integrates real-time
  data access, enabling dynamic querying of vulnerability contexts while eliminating
  false positives through detailed asset analysis. The architecture emphasizes a closed-loop
  system with human oversight for trust validation. As enterprises largely operate
  in a hybrid environment with a shift-right remediation strategy, this solution proposes
  a scalable framework to enhance cybersecurity resilience against AI-fueled exploitation
  efforts. Future developments will focus on refining agentic capabilities for broader
  application.
link: https://www.zafran.io/resources/agentic-remediation-unlocks-a-new-approach-to-solving-enterprise-vulnerabilities
tags:
- Automated Patching
- Vulnerability Management
- Enterprise Security
- AI in Cybersecurity
- Agentic Remediation
title: Agentic Remediation™ Unlocks A New Approach To Solving Enterprise Vulnerabilities
---

## Get a Demo

Required fields are marked with an asterisk \*

[Skip to main content](https://www.zafran.io/#main)

[Zafran Unveils Agentic Remediation™ to Solve Enterprise Vulnerabilities in the Age of AI\\
\\
Read More](https://www.zafran.io/resources/agentic-remediation-unlocks-a-new-approach-to-solving-enterprise-vulnerabilities)

Close Announcement Banner

[Home Page](https://www.zafran.io/)

[Home Page](https://www.zafran.io/)

# Agentic Remediation™ Unlocks A New Approach To Solving Enterprise Vulnerabilities

### Zafran Labs reveals a blueprint for agentic remediation

Author:

Ben Seri

,

CTO & Co-Founder

Published on

September 15, 2025

Blog

![](https://cdn.prod.website-files.com/680f77e95243e1c8f6ae6792/68c45e820c538d9e9c639939_Active%20-%20Vibe%20Patching%20-%20Banner%20V6.png)

AI hype is all around - AI is the new ‘digital’, the new ‘cloud’, the new ‘mobile’, the new **new**. And while a lot of it is just hot air, some real opportunities are emerging - from fast coding, to smarter searches, to better planning, and a tidal wave of summarized content in every corner of our digital lives (‘agentic’ lives, come to think of it 🙄).

Unfortunately, attackers are also adopting the trend. In a recent [blog](https://blog.checkpoint.com/executive-insights/hexstrike-ai-when-llms-meet-zero-day-exploitation/?utm_source=chatgpt.com), Check Point detailed how hackers used the newly released HexStrike-AI framework to exploit fresh NetScaler zero-days - compressing the time-to-exploit window to unprecedented levels. [Anthropic](https://www.bbc.com/news/articles/crr24eqnnq9o?utm_source=chatgpt.com) has reported that its Claude model was weaponized in real-world breaches, helping attackers write code that exfiltrated data from at least 17 organizations. And the Chinese group [Aquatic Panda](https://openai.com/index/disrupting-malicious-uses-of-ai-by-state-affiliated-threat-actors/) has been observed using LLMs to debug exploit code, refine evasion scripts, perform reconnaissance, and achieve persistence. These examples illustrate how AI is not only accelerating the speed of attacks but also enhancing their sophistication and stealth, creating serious challenges for defenders.

So can AI also help counter these AI‑driven advances? Are today’s LLMs, and their emerging "agentic" capabilities, mature enough to investigate impact, assess dependencies, and generate ready‑to‑use remediation scripts for a large portion of enterprise vulnerabilities?

Zafran Labs – the research team at Zafran dedicated to dissecting vulnerabilities, assessing exposures, and continuously developing the Zafran Exposure Graph – set out to answer this question. In this blog, we’ll present a sneak peek into the development of Zafran’s own Agentic AI tool, aimed at investigating, assessing and remediating enterprise vulnerabilities.

## End-to-End Remediation

The following video demonstrates the potential of agentic technology in solving the above questions. A day in the life of a vulnerability management analyst starts by hunting for a critical exposure (a privilege-escalation vulnerability, on a mail server, in this example), and uncovering the exact steps to fix it. These manual steps are automated in the following video:

- The agent is able to translate a freetext description of the exposure the user is looking for, into queries in Zafran’s platform data warehouse, identify the vulnerable asset, and focus on the most exploitable vulnerability.
- It leverages Zafran’s context on **runtime, reachability** and **security controls**, and provides a detailed report.
- It then goes a step further: With the approval of the user, it creates an interactive session with the affected asset, and runs read-only commands on it.
- These commands are used to assess the impact, verify a patch is available, simulate the effects of installing it - and provide ready-to-use instructions on performing the patch.
- For most organizations - applying a fix to an endpoint or a production server would be done by a separate user (IT / engineering) - and not by a vulnerability management analyst. Despite this, the POC goes a step further and demonstrates the last mile of remediation, where the user asks the agent to perform the patch itself. The agent installs the patch, and also **validates** that it was successfully installed, and the underlying component continues to work.

‍

![Zafran Agentic Remediation Demo Thumbnail](https://cdn.prod.website-files.com/680f7748aeaac0c97e4b1a7b/68c7e341d72a489a86f33ea1_Zafran-Agentic-Remediation.png)

‍

## Elimination of False Positives

The above demo shows an end-to-end remediation scenario, however - it is well known that most vulnerabilities identified by scanners are actually false-positive detections. There are infinite amounts of conditions for a vulnerability to be unexploitable in a certain environment, and scanners are unable to reliably account for these conditions. The following demo shows such a case:

- The user asks the agent to generate remediation steps for a vulnerability in OpenSSL.
- The agent researches the relevant CVE online, and finds that it is only exploitable on assets that use a PowerPC CPU.
- By leveraging the real-time access to the impacted asset, the agent runs commands on it, and finds the asset is running a x86 CPU.
- The above conditions lead the agent to definitively assess that the vulnerability on the impacted asset is in fact a false positive detection.
- This leads the agent to produce a false-positive report, and deduce that patching the OpenSSL component is not required.

‍

![Vulnerability Validation Thumbnail](https://cdn.prod.website-files.com/680f7748aeaac0c97e4b1a7b/68c45c6601f0f50e3a6db11e_Vulnerability%20Validation.png)

‍

## Shift-Right Remediation vs Shift-Left Remediation

While the demos above look promising, we need to go back to understand how this agent was constructed, but more importantly how this approach may scale for the enterprise.

Most enterprises today operate in a hybrid approach, certain applications are developed and deployed to containerized environments, with CI/CD processes that allow organizations to fix images in a build process (a shift-left remediation strategy) - while other enterprise assets (endpoints, servers, unmanaged devices) receive software updates in-place, in a shift-right remediation strategy.

According to Zafran’s stats (tracking many large enterprises, with millions of assets), while most enterprises have embraced the cloud, the majority of assets - 72% in our data - are still on-prem (endpoints, servers, unmanaged devices). Only 14% are container images. In practice, this means most enterprise assets are maintained and patched with a shift-right approach. The reality: enterprises, by and large, have not yet shifted left.

![](https://cdn.prod.website-files.com/680f77e95243e1c8f6ae6792/68c2cfdf9da428eb2de0875b_Active%20-%20Vibe%20Patching%20graphic%201%20v2.png)

The stats above mean that assessing impact, preparing a fix, and ultimately applying it on an asset in-place (“shift-right”) - is a required strategy for most enterprises today. Moreover, even for applications that adopted a shift-left remediation process, assessment of vulnerabilities - and the specific conditions that might deem them unexploitable, is best done in shift-right, where these conditions fully manifest.

The process of applying the patch may differ greatly from one organization to the next (via various change-management procedures, and by utilizing various patch management tools) but the assessment, impact analysis and preparations of a patch are tedious, manual and universal procedures performed today by vulnerability analysts in every security organization.

The nature of software vulnerabilities makes these steps inherently non-deterministic - each vulnerability may require a different validation approach, each patch may need to be simulated differently. And, as it turns out, non-determinism is at the heart of agentic AI - for better, or for worse. Let’s see how we tame the beast.

Our initial POCs show promising results: when current agentic models are paired with a rich vulnerability data warehouse and a secure, real-time way to interact with affected assets, they can fundamentally change the **remediation game**\- a shift that defenders urgently need as attackers gain AI-powered momentum.

## A Closed-Loop System

Developers who have used Cursor, Claude‑Code, or other AI coding tools know how they succeed: they read existing code, write a change, compile and test it, analyze failures, and iterate. Any effective AI agent today requires a closed-loop system, to move from ‘maybe works’ to ‘works’. The same applies to **Agentic Remediation.**

Four ingredients for making an effective Remediation Agent:

1. Great exposure context **data**
2. A **scalable** and efficient way to query that data
3. **Real-time interface** to run (read-only) commands on vulnerable assets, validate assumptions, and generate ready-to-use remediation scripts
4. Lastly, but most importantly - a **User**; A human-in-the-loop, to approve execution of commands, and ask the right questions

‍

![](https://cdn.prod.website-files.com/680f77e95243e1c8f6ae6792/68c2d6e49223b802660b64c7_Active%20-%20Vibe%20Patching%20graphic%202%20v3.png)

‍ **Data:** AI agents are only as effective as the data they have access to. Leveraging the rich context and detailed knowledge graph within the Zafran platform, an AI agent can hunt for the most exploitable vulnerabilities that are found **in-runtime**, understand business-context, validate reachability risk (e.g., **Internet-facing** exposures), and identify the underlying components that need fixing.

**Scale:** Exposure management is fundamentally a data problem - and therefore also a scale problem. A mid-sized enterprise typically manages ~100,000 assets, each with ~1,000 vulnerabilities spread across ~1,000 unique software components. These numbers compound quickly: the result is roughly 100 million vulnerability findings at any given time. Humans simply cannot sift through this volume, and AI models face context limitations as well. Solving this challenge requires two elements: a scalable and reliable data warehouse, and an efficient method to query it. In our lab, we paired our agent with the MCP server of our platform’s data warehouse for our Zafran tenant. The agent quickly learned the warehouse’s data structures and effectively queried the most relevant data. Many “agentic” solutions are merely strapped onto existing APIs, which are often slow and inefficient. With query-level access, an agent can leverage the full power of a high-performance analytical database to locate the information it needs.

**Real-time interface:** Once an agent identifies a critical exposure, gathers context, and obtains initial guidance from vulnerability scanners, it must investigate the issue live. Using Zafran’s patented technology to run inspection scripts through existing agents (tools, that is - not ‘agentic’ agents), the closed-loop system allows the AI to assess and test potential fixes. Through iterative exploration, the agent reaches a conclusion: a detailed report explaining whether a vulnerability can be patched, and, when possible, a ready-to-use remediation script. A security guardrail, that ensures that only read-only commands are executed, will likely be a requirement for initial releases of an agentic remediator. However, to apply the patch in-place (as demonstrated above), certain write-commands will be required as well.

**User:** A user, to guide and authorize actions is an integral part of an agentic remediator - required to both audit the commands that the remediator is attempting to execute on endpoints (as an additional security measure), but also to guide the agent via questions that are of particular interest and significant to the enterprise. A human-in-the-loop provides an essential element for the agent: trust.

The architecture below summarizes the 4 ingredients for creating an Agentic Remediator:

![](https://cdn.prod.website-files.com/680f77e95243e1c8f6ae6792/68c2d726837cf35545559e7a_Active%20-%20Vibe%20Patching%20graphic%203%20v1.png)

Agentic Remediation Architecture (click to enlarge image)

## Looking Ahead

While these demos above focused on Linux-based findings, we believe the approach demonstrated above can expand across other remediation “classes” - fixing a 3rd party dependency, updating a Windows application, or even safely assessing the impact and applying an OS upgrade. Yes, every vulnerability, and every patch is a snowflake, but recognizable patterns do emerge. Over time, these patterns could enable remediation agents to automate much of the work vulnerability analysts perform today - who may soon find themselves “vibe-patching” with AI assistance.

Scaling this approach, and connecting the dots between AI-generated remediation scripts, with automated patching solutions - would bring us one step closer to real-world automated remediation. In the above demo, the agent safely remediated 1 vulnerability on 1 asset - but there’s no reason to believe the agent won’t be able to replicate this action on a fleet of similarly impacted servers.

Similarly - when considering modern applications that are built from code (shift-left) - the solution could include a code-to-cloud agent, that will connect the dots from shift-right back to shift-left, and offer to apply a fix in infra-as-code, or other type of image dependencies.

Our next step at Zafran is taking this approach from blueprint to production. The key challenge: evolving a non-deterministic agent into an enterprise-ready system. This requires strict security and safety guardrails - principles we embed into every technology we develop. That’s even more critical as we explore solutions that not only leverage AI, but give it (some) agency in service of enterprise defense.

We must conclude by acknowledging the proverbial elephant in the room: **trust**. Can I trust Agentic Remediation to not take down critical systems? Can I trust my data won’t be exposed to a new attack surface? How will I be able to validate an agent is not hallucinating, or producing a faulty analysis?

It’s natural to have doubts at this stage, in the evolution of a disruptive technology. Trust will be built in small and gradual steps - and then, once it gains a footing - in a large leap of faith.

This piece was intended to start a conversation. If you’re interested in shaping the future of agentic remediation, or exploring early use cases, I’d love to hear from you.

Ben Seri

CTO and Co-Founder, Zafran

[ben@zafran.io](mailto:ben@zafran.io)

Discover how Zafran Security can streamline your vulnerability management processes.

Request a demo today and secure your organization’s digital infrastructure.

Discover how Zafran Security can streamline your vulnerability management processes.

Request a demo today and secure your organization’s digital infrastructure.

Request Demo

On This Page

- [End-to-End Remediation](https://www.zafran.io/resources/agentic-remediation-unlocks-a-new-approach-to-solving-enterprise-vulnerabilities#end-to-end-remediation)

[Elimination of False Positives](https://www.zafran.io/resources/agentic-remediation-unlocks-a-new-approach-to-solving-enterprise-vulnerabilities#elimination-of-false-positives)

[Shift-Right Remediation vs Shift-Left Remediation](https://www.zafran.io/resources/agentic-remediation-unlocks-a-new-approach-to-solving-enterprise-vulnerabilities#shift-right-remediation-vs-shift-left-remediation)

[A Closed-Loop System](https://www.zafran.io/resources/agentic-remediation-unlocks-a-new-approach-to-solving-enterprise-vulnerabilities#a-closed-loop-system)

[Looking Ahead](https://www.zafran.io/resources/agentic-remediation-unlocks-a-new-approach-to-solving-enterprise-vulnerabilities#looking-ahead)


Share this article:

[copy url](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.zafran.io%2Fresources%2Fagentic-remediation-unlocks-a-new-approach-to-solving-enterprise-vulnerabilities&title=Agentic+Remediation%E2%84%A2+Unlocks+A+New+Approach+To+Solving+Enterprise+Vulnerabilities&summary=)[share](https://www.zafran.io/resources/agentic-remediation-unlocks-a-new-approach-to-solving-enterprise-vulnerabilities#)

[![A black and white logo for a company.](https://cdn.prod.website-files.com/680f7748aeaac0c97e4b1a7b/68122a4da278ac463a8a9db5_zafran-logo.png)](https://www.zafran.io/)

[Platform](https://www.zafran.io/platform) [Careers](https://www.zafran.io/careers) [Resources](https://www.zafran.io/learn) [Trust Center](https://trust.zafran.io/?__hstc=17958374.fa313179e6967d027776ed95f8800f83.1731412408262.1748424978459.1748428967045.69&__hssc=17958374.3.1748428967045&__hsfp=2189040166) [Company](https://www.zafran.io/about) [Get a Demo](https://www.zafran.io/resources/agentic-remediation-unlocks-a-new-approach-to-solving-enterprise-vulnerabilities#)

© 2025 Zafran. All rights reserved.

[Privacy Policy](https://www.zafran.io/legal/privacy-policy) [Terms of Service](https://www.zafran.io/legal/terms-of-use)

© 2025 Zafran. All rights reserved.
