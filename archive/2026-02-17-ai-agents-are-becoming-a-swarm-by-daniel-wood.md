---
date: '2026-02-17'
description: The article discusses a paradigm shift in AI security as multi-agent
  systems become prevalent. Key insights include the transition from isolated AI models
  to coordinated swarms, necessitating a focus on intent governance rather than traditional
  model risks. New vulnerabilities arise, such as intent laundering and permission
  drift, complicating accountability in automated decision-making processes. Organizations
  must adapt by establishing robust controls like AI action ledgers and treating agents
  as new actors within security frameworks. The overarching challenge is managing
  coordination risks that exceed legacy governance capabilities, emphasizing the need
  for proactive oversight at the board level.
link: https://dwsec.substack.com/p/ai-agents-are-becoming-a-swarm
tags:
- AI Agents
- Automation Risks
- Intent Management
- Security Governance
- Adversarial Mindset
title: AI Agents Are Becoming a Swarm - by Daniel Wood
---

# [The Adversarial Mindset](https://dwsec.substack.com/)

SubscribeSign in

![User's avatar](https://substackcdn.com/image/fetch/$s_!04ZB!,w_64,h_64,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b5ca424-e7a8-4530-bafa-af38fe5c6837_644x644.jpeg)

Discover more from The Adversarial Mindset

Most security commentary reacts to tools and headlines.
This newsletter focuses on leverage.

I write about security as a system of control — how organizations shape adversary decisions, manage tempo, and translate technical exposure into executive action

Subscribe

By subscribing, you agree Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

Already have an account? Sign in

# AI Agents Are Becoming a Swarm

### The Next Security Perimeter Is Coordination

[![Daniel Wood's avatar](https://substackcdn.com/image/fetch/$s_!04ZB!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b5ca424-e7a8-4530-bafa-af38fe5c6837_644x644.jpeg)](https://substack.com/@dwsec)

[Daniel Wood](https://substack.com/@dwsec)

Feb 16, 2026

1

1

Share

[![](https://substackcdn.com/image/fetch/$s_!Bksd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbba4eb9e-8fec-4ac4-b316-65d846cdb918_1536x1024.png)](https://substackcdn.com/image/fetch/$s_!Bksd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbba4eb9e-8fec-4ac4-b316-65d846cdb918_1536x1024.png)

Over the last few days, the signal is getting louder: we’re moving from “LLMs that answer” to **agents that act**, and from “one agent” to **many agents operating concurrently**. We are seeing a complete _control-plane_ shift.

If you’re a CIO/CTO/CISO, the question isn’t “will agents be useful?” The question is: **what happens when your organization’s work is executed by a swarm of semi-autonomous systems that can coordinate faster than your governance can reason?**

## What changed in the last few days…

### 1) Safety UI is moving _up the stack_

OpenAI’s “Lockdown Mode” and “Elevated Risk labels” are a notable tell. It implies a product reality: **the model is now a decision surface**. We’re not just securing infrastructure; we’re securing the _interaction layer where intent is expressed_. If you need “Lockdown Mode,” it means:

- some prompts and workflows are inherently high-risk,

- users will push models into privileged workflows,

- and the vendor expects real-world abuse modes to be frequent enough to warrant UX-level controls.


This isn’t really a surprise, when looking at the [news](https://steipete.me/posts/2026/openclaw) that Peter Steinberger, the creator behind Clawdbot/Moltbot/OpenClaw, is joining OpenAI. Autonomous agents, and securing the execution environment they exist in will be the talk for weeks to come.

### 2) Agent “swarming” is now a mainstream security concern

Dark Reading explicitly [framed](https://www.darkreading.com/cloud-security/ai-agents-swarm-security-complexity) the emerging problem: AI agents can “swarm,” and security complexity follows. The key word is _swarm_.

- A single agent is a feature. A swarm is a system. Systems create:

  - emergent behavior,

  - unintended coupling,

  - cascading failure (think upstream/downstream systems),

  - and adversarial surface area.

### 3) “Scale” is the product, not an engineering detail

- OpenAI’s [note](https://openai.com/index/beyond-rate-limits/) about scaling access to Codex and Sora is another tell: the unit of value is shifting from “try a model” to “run it constantly.” When usage becomes continuous, security needs to move from:


  - “review the output”


…to:

  - “govern the actions.”

### 4) The broader security ecosystem is already responding to AI abuse & browser-layer risk

Google’s [research](https://cloud.google.com/blog/topics/threat-intelligence/distillation-experimentation-integration-ai-adversarial-use) “GTIG AI Threat Tracker: Distillation, Experimentation, and (Continued) Integration of AI for Adversarial Use” and separate reporting on malicious browser extensions point at the same future: the front door is increasingly **browser + identity + automation**. Agents will live there.

Thanks for reading The Adversarial Mindset! Subscribe for free to receive new posts and support my work.

Subscribe

## The real shift: from model risk to coordination risk

Most AI security talk is still model-shaped:

- prompt injection

- data leakage

- model jailbreaks

- hallucinations


These matter of course, however, they’re not where AI risk is expanding. The increasing risk is **delegated execution at scale.** When agents can do work, your new risks are:

### 1) Intent laundering

- If a human clicks “approve,” who owns the intent?

  - the user?

  - the agent?

  - the tool that suggested the action?

In traditional systems, intent is attributable. A person decides, and ownership is clear.

In agentic workflows, approval often becomes confirmation of framing, not independent judgment. The human sees a distilled rationale generated by a system optimized for efficiency, resolution speed, or acceptance rates. The path to approval is friction-minimized by design.

So, back to the question, who owns intent? The user who clicked? The model that structured the recommendation? The product team that tuned the optimization loop? The data inputs that shaped the output? _Responsibility becomes structurally ambiguous._

**This is where adversarial dynamics enter.**

Attackers do not need to “hack” the model. They do not need jailbreaks or prompt injection. They only need to **shape the decision context** so the model persuades a human to authorize a harmful action. This is classic adversarial deception—reflexive control—applied to software:

- Manipulate telemetry.

- Seed misleading signals.

- Trigger urgency.

- Exploit automation bias.


The system generates a reasonable recommendation.

- The human approves.

- The action executes.

- The logs read: “User authorized.”


Instead of compromising systems directly, an adversary engineers the perception layer so the system recommends the action they want taken. The human believes they are in control, _but the context has already been engineered with intent._

As AI agents gain tool-use autonomy and multi-step planning capabilities, this risk compounds. The more work systems can do, the more valuable it becomes to shape what they decide to do.

We are no longer defending code paths. We are defending intent pathways.

The danger is not runaway intelligence. It is scaled delegation without clear intent governance. Automation compresses friction, distributes responsibility, and optimizes for throughput. But **accountability models have not evolved at the same speed**.

Intent laundering is the governance blind spot of agentic AI. Not because the systems are malicious. But because authority, persuasion, and execution now flow across layers faster than ownership can be cleanly assigned.

That is where the real expansion of AI risk is occurring.

### 2) Permission drift (the silent killer)

- Agents will accrete permissions the way SaaS integrations do:

  - “just give it access to my Drive/Slack/Jira/GitHub”
- “just let it manage my cloud resources”


Then you wake up with a non-human identity that is:

- long-lived,

- broadly scoped,

- poorly monitored,

- and socially normalized.


### 3) Toolchain ambiguity

Security teams will struggle to answer:

- What actions did the agent take?

- Which tool executed it?

- Under what identity?

- Was the decision deterministic or model-influenced?


### 4) Swarm amplification

If you have 50 agents operating:

- one compromised instruction path can replicate 50x faster than a human can intervene,

- and the blast radius becomes “everything the swarm can touch,” not “one endpoint.”


* * *

## Probabilistic forecast (12–24 months)

Based on what we’ve all seen in the last two years regarding technological advancement of artificial intelligence, coupled with just how fast innovation is moving, these are my forecasts over the next two years (barring any additional groundbreaking work).

### High probability (70–90%)

- Agents become the default UI for knowledge work workflows.

- Identity becomes the control plane for AI risk.

- “Lockdown modes” expand across vendors.


### Medium probability (40–70%)

- Agent-to-agent communication becomes a blind spot.

- A new class of incidents emerges: “approved bad actions.”


### Low probability, high impact (10–30%)

- A major breach is primarily a coordination failure, not a technical failure.


* * *

## What to do now (or the timeless “what’s old is new” playbook)

- Treat agents as NHIs (least privilege, time-bound tokens, kill switches)

- Build an “AI action ledger” (intent, context, tool, identity, approval)

- Add approvals only for high-risk actions

- Red team agent workflows (decision points + belief formation)

- **Make coordination risk a board-level concept**


The unifying principle behind these controls is simple: agents are new actors in your system, even if they are not legal persons. They aggregate perception, recommendation, and execution into a single coordination node. That means they must be governed like any other high-impact actor — with constrained authority, observable intent, and reversible power. Least privilege is not an AI feature; it is an accountability mechanism. An AI action ledger is not logging for forensics; it is provenance for intent. Red teaming workflows is not about breaking the model; it is about **breaking the decision chain before an adversary does**.

Most importantly, coordination risk must move out of engineering and into governance. When agents compress multi-step processes into single approvals, they collapse separation-of-duties by design. That is not a bug — it is the value proposition. But value without oversight becomes fragility and is contrarian to resilience engineering. Boards and executive teams need to understand that AI deployment is not merely a tooling decision; it is a reallocation of authority inside the enterprise. The organizations that survive this transition will not be the ones with the smartest models, but the ones with the clearest ownership of intent.

[Leave a comment](https://dwsec.substack.com/p/ai-agents-are-becoming-a-swarm/comments)

1

1

Share

Previous

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

[![Coconut Snowshoe's avatar](https://substackcdn.com/image/fetch/$s_!DBay!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F75e57526-75b6-452d-b131-6ad29083deb4_600x600.png)](https://substack.com/profile/345611120-coconut-snowshoe?utm_source=comment)

[Coconut Snowshoe](https://substack.com/profile/345611120-coconut-snowshoe?utm_source=substack-feed-item)

[18h](https://dwsec.substack.com/p/ai-agents-are-becoming-a-swarm/comment/215380171 "Feb 16, 2026, 1:12 PM")

Liked by Daniel Wood

Once again, great article!

Like (1)

Reply

Share

TopLatestDiscussions

[Deception as a System](https://dwsec.substack.com/p/deception-as-a-system)

[How to Red Team Adversarial Intent (Not Just TTPs)](https://dwsec.substack.com/p/deception-as-a-system)

Feb 6•[Daniel Wood](https://substack.com/@dwsec)

2

2

![](https://substackcdn.com/image/fetch/$s_!wX5e!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F920ae435-6232-4d04-9e52-986e7496df27_1536x1024.png)

[Rethinking Security](https://dwsec.substack.com/p/rethinking-security)

[As security practitioners, we face an uphill challenge, not just with defending our organization, customers, and data; but we often struggle with…](https://dwsec.substack.com/p/rethinking-security)

May 15, 2025•[Daniel Wood](https://substack.com/@dwsec)

1

![](https://substackcdn.com/image/fetch/$s_!X5yf!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e350729-ddf3-4532-8d02-7f66a52626a1_1024x1024.png)

[Deception as Control](https://dwsec.substack.com/p/deception-as-control)

[The Red Teamer’s Missing Discipline](https://dwsec.substack.com/p/deception-as-control)

Feb 12•[Daniel Wood](https://substack.com/@dwsec)

2

![](https://substackcdn.com/image/fetch/$s_!9fGM!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2159fdcc-8f76-41dc-be41-af939c4e8a25_1536x1024.png)

See all

### Ready for more?

Subscribe
