---
date: '2026-01-29'
description: Recent investigations into **Moltbot (formerly Clawdbot)** illustrate
  significant exposure risks associated with deploying autonomous agent gateways,
  which facilitate interactions between LLMs and real-world tools. Hundreds of publicly
  accessible instances exhibit both authentication configurations and alarming misconfigurations,
  exposing sensitive artifacts and user data. As these systems evolve into critical
  infrastructure, they warrant strict security measures akin to those for privileged
  environments. Recommendations include robust access controls, sandboxing executions,
  and frequent security audits. This highlights the imperative for diligent hardening
  practices in emerging AI-driven automation landscapes.
link: https://blog.pluto.security/p/clawdbot-in-the-wild-exposure-risks
tags:
- autonomous agents
- infrastructure security
- Moltbot
- authentication risk
- AI security
title: 'Moltbot(Clawdbot) in the Wild: Exposure Risks and Practical Hardening'
---

SubscribeSign in

![User's avatar](https://substackcdn.com/image/fetch/$s_!9kOx!,w_64,h_64,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F195a4951-724f-4367-bef4-2660ebf89765_700x700.jpeg)

Discover more from Pluto Security

Enabling business users to innovate securely.

Subscribe

By subscribing, I agree to Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

Already have an account? Sign in

# Moltbot(Clawdbot) in the Wild: Exposure Risks and Practical Hardening

### What we learned by looking at how people actually deploy autonomous agents, and why agent gateways should be treated like privileged infrastructure, not hobby projects.

[![Pluto Security's avatar](https://substackcdn.com/image/fetch/$s_!9kOx!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F195a4951-724f-4367-bef4-2660ebf89765_700x700.jpeg)](https://substack.com/@plutosecurity)[![Yotam Perkal's avatar](https://substackcdn.com/image/fetch/$s_!p50s!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e66c120-0a6a-47ac-a6d0-a319d0c4ceab_3089x3089.jpeg)](https://substack.com/@pyotam2)

[Pluto Security](https://substack.com/@plutosecurity) and [Yotam Perkal](https://substack.com/@pyotam2)

Jan 26, 2026

11

8

Share

[![](https://substackcdn.com/image/fetch/$s_!hSt9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8d60c4f0-a41c-4c41-8b31-d8955ba235fb_1920x1080.png)](https://substackcdn.com/image/fetch/$s_!hSt9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8d60c4f0-a41c-4c41-8b31-d8955ba235fb_1920x1080.png)

Computer-Using Agents (CUA) are part of a rapidly growing class of software: **agent gateways** that allow LLMs to interact with local machines and real tools (messaging, email, calendars, browsers, shells), often running persistently and with meaningful autonomy.

That combination is powerful.

It also fundamentally changes the security equation.

[Moltbot](https://github.com/moltbot/moltbot) (formerly known as [Clawdbot](https://x.com/moltbot/status/2016058924403753024)) is one recent example of this class of tooling that has gained significant traction in a short period of time. As you can see in the below image 👇 in ~2 months it reached over 60K GitHub stars, which is abnormal even compared to projects like [Langchain](https://github.com/langchain-ai/langchain) (over a year) or [OpenHands](https://github.com/OpenHands/OpenHands) (almost 2 years).

[![](https://substackcdn.com/image/fetch/$s_!68p6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb3a77b5b-1a26-4208-9086-654903471be5_1572x980.png)](https://substackcdn.com/image/fetch/$s_!68p6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb3a77b5b-1a26-4208-9086-654903471be5_1572x980.png) source: star-history.com

We spent time examining the **real-world deployment surface** of [Moltbot](https://github.com/moltbot/moltbot) instances exposed on the public internet, not to single out the project, but to understand what happens when high-autonomy infrastructure is deployed the same way hobby projects often are: quickly, publicly, and without careful hardening.

What we found were familiar patterns, but with a much larger blast radius.

## **What Moltbot is (and how it works)**

At a high level, Moltbot is an open-source personal AI assistant developed by [Peter Steinberger](https://steipete.me/), designed to operate across the communication channels people already use (e.g., WhatsApp, Telegram, Slack, Signal) and to run continuously.

From a security perspective, its architecture matters more than its feature set. The key components are:

- **Gateway** An always-on process that acts as the control and execution plane, handling message routing, tool invocation, and integration plumbing. It is designed to run persistently until stopped.

- **Control UI / Web surface** The Gateway serves a browser-based control interface on the same port as its WebSocket interface (with configurable paths and prefixes). This is where integrations, credentials, and operational state are managed.

- **Tools and integrations** Depending on configuration, the agent can invoke local or system tools and connect to external services using OAuth tokens and API keys.


```
WhatsApp / Telegram / Slack / Discord / Google Chat / Signal / iMessage / BlueBubbles / Microsoft Teams / Matrix / Zalo / Zalo Personal / WebChat
               │
               ▼
┌───────────────────────────────┐
│            Gateway            │
│       (control plane)         │
│     ws://127.0.0.1:18789      │
└──────────────┬────────────────┘
               │
               ├─ Pi agent (RPC)
               ├─ CLI (clawdbot …)
               ├─ WebChat UI
               ├─ macOS app
               └─ iOS / Android nodes
```

Together, the Gateway and Control UI form a **privileged control plane for an autonomous system**. If this plane is exposed and misconfigured, an attacker doesn’t just gain visibility-they can potentially inherit capability.

## **What we observed in the wild**

Using common internet asset discovery tools (such as [Shodan](http://shodan.io/) and [Censys](http://censys.io/)), we identified **hundreds of publicly accessible Clawdbot (now Moltbot) Gateway/Control instances**.

[![](https://substackcdn.com/image/fetch/$s_!YoGC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fccc3b1d2-21b6-4a20-86f3-599192fef35f_2538x968.png)](https://substackcdn.com/image/fetch/$s_!YoGC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fccc3b1d2-21b6-4a20-86f3-599192fef35f_2538x968.png) source: shodan.io

[![](https://substackcdn.com/image/fetch/$s_!Gjrf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb7056731-6f52-41c5-a748-dda00966cbf4_2724x1020.png)](https://substackcdn.com/image/fetch/$s_!Gjrf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb7056731-6f52-41c5-a748-dda00966cbf4_2724x1020.png) source: censys.io

An important clarification up front:

**The majority of these publicly accessible instances appeared to have authentication configured.** This is encouraging-but it does not eliminate risk.

Even authenticated, publicly reachable agent gateways remain **high-value targets**: they are long-lived services, connected to multiple tools, and often positioned near credentials, automation logic, and operational history.

More concerning, however, was that we also found **instances that did not require authentication at all**, or exposed sensitive artifacts through other means. With minimal exploration, we observed deployments exposing:

- Misconfigured control UIs allowing secret discovery, payload execution, and modification of the Moltbot configuration.


[![](https://substackcdn.com/image/fetch/$s_!jZ4_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F07c2106c-2dd3-4fca-b544-b690647e63b5_1920x1080.png)](https://substackcdn.com/image/fetch/$s_!jZ4_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F07c2106c-2dd3-4fca-b544-b690647e63b5_1920x1080.png)

- Active integrations with services such as Slack, Gmail, Google calendar, social media accounts and other connected tools, exposing user PII.


[![](https://substackcdn.com/image/fetch/$s_!KuiE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F17718694-c356-459c-b60c-f805738ac29d_1920x1080.png)](https://substackcdn.com/image/fetch/$s_!KuiE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F17718694-c356-459c-b60c-f805738ac29d_1920x1080.png)

- Directory listings exposed over HTTP, including operational logs and agent artifacts.


[![](https://substackcdn.com/image/fetch/$s_!ZjJB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffc5291cb-5c78-4ffb-ac51-bada16923dbb_1200x1200.png)](https://substackcdn.com/image/fetch/$s_!ZjJB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffc5291cb-5c78-4ffb-ac51-bada16923dbb_1200x1200.png)

- In some cases, configuration details containing sensitive information (for example, database connection details).

[![](https://substackcdn.com/image/fetch/$s_!Z6G5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13ac4bd0-5a3a-4993-937f-0f9d7b32e1bf_1920x1080.png)](https://substackcdn.com/image/fetch/$s_!Z6G5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13ac4bd0-5a3a-4993-937f-0f9d7b32e1bf_1920x1080.png)


## **This isn’t a** Moltbot **problem**

It’s important to be clear about the framing.

This is not something specific to Moltbot. It’s a broader pattern that emerges whenever **high-autonomy software** is deployed without careful hardening. Moltbot is simply a concrete example of a larger shift we’re seeing across the industry.

For an agent to be useful, it often must:

- Read messages,

- Store credentials

- Act on a user’s behalf

- Execute tools

- Retain context over time.


These are functional requirements, but they come with security consequences.

## **What is the risk?**

When you expose a system like this, you’re not just exposing “an app.” You’re exposing a system that may have:

- Full shell access to the host (depending on enabled tools)

- Browser control in contexts that may include logged-in sessions

- File system read/write access

- Access to email, calendars, and messaging platforms via stored tokens

- Persistent state and memory across sessions

- The ability to act proactively (sending messages, triggering workflows)


That’s an enormous concentration of capability.

The risk, therefore, isn’t just data leakage.

It’s **delegated authority**: if someone gains control, they may be able to act _as you_, using the integrations and trust relationships you’ve already established.

## **Common Risky Patterns**

Most of the risky deployments we observed did not stem from sophisticated attacks. They stem from normal people doing normal things-without following basic security practices.

#### **1) The reverse-proxy trap**

A common pattern is deploying a service behind Nginx, Caddy, or Traefik and assuming it’s safe “because it’s behind a proxy.” In reality, proxying can change how applications perceive client identity, locality, and trust boundaries. Without explicit configuration, this can turn local-only assumptions into public exposure.

#### **2) “It’s just a test box” becomes permanent**

Agent gateways tend to persist. Once connected to workflows, they stay running. Logs accumulate. Integrations multiply. What began as a demo quietly becomes long-lived infrastructure.

#### **3) Capability creep increases the blast radius**

Each additional integration expands the potential impact of compromise. Over time, an agent gateway can quietly become a credential hub, automation runner, and communications layer-without anyone explicitly deciding it has become critical infrastructure.

## **What this means for builders and defenders**

If you operate (or build) agent gateways, you should treat them as:

- A **secrets store** (they hold tokens and keys)

- A **privileged automation runner**

- A **communications system**

- A **long-lived identity**


Operationally, this shifts focus toward:

- Exposure windows and detection speed

- Credential scope and revocation

- Auditability

- Containment and blast-radius reduction


## **What should you do as a defender/builder?**

First of all, Moltbot’s documentation already provides security hardening guidance and includes mechanisms operators should take advantage of:

- **Security guidance and auditing** Moltbot provides [documentation](https://docs.clawd.bot/cli/security) and CLI commands (such as moltbot security audit) to help assess configuration and exposure posture. These checks are worth running periodically, especially after deployment changes.

- **Sandboxing to reduce blast radius** Tool execution can be [sandboxed](https://docs.clawd.bot/cli/sandbox) (for example, using Docker). While not a perfect boundary, this materially reduces filesystem and process exposure when something goes wrong. Sandbox scope (agent, session, shared) also affects cross-session isolation and should be chosen deliberately.


These measures don’t eliminate risk-but they meaningfully reduce impact.

#### Practical hardening checklist

For Moltbot, or any similar CUA, the following baseline is advised to minimize risk:

- Do **not** expose control/admin surfaces to the public internet. Use private networking, VPNs, or strong access controls.

- Require authentication everywhere, and verify it remains enforced behind reverse proxies.

- Run the system in an isolated environment (VM, dedicated host, sandbox, or segmented network). Avoid running it on daily-use machines.

- Use test accounts before connecting real credentials.

- Treat logs, history, and configuration as sensitive data; lock down permissions and avoid directory listings.

- Run built-in security audits regularly and remediate findings.

- Reduce privileges and minimize tool execution scope as much as possible.


**Rule of thumb:** If an agent can read your messages, send messages as you, access your files, and run tools, it deserves the same security posture as a production admin console and secrets manager-because functionally, that’s what it is.

If you don’t follow these best practices you can safely assume that someone on the internet WILL find your deployment within hours.

[![](https://substackcdn.com/image/fetch/$s_!_3JG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37970cb3-e78b-424b-a519-43ccfee8de46_1172x356.png)](https://substackcdn.com/image/fetch/$s_!_3JG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37970cb3-e78b-424b-a519-43ccfee8de46_1172x356.png)

## **Final thoughts**

This isn’t about inducing fear, and it isn’t about singling out Moltbot.

It’s about recognizing a broader shift: **autonomous agents dramatically increase the blast radius of misconfiguration**. Adoption is inevitable. The tools are useful. The economics are compelling.

The open question is whether we harden these systems like the privileged infrastructure they are, **before the internet does what the internet always does**.

* * *

> At **Pluto**, we’re enabling enterprises to use AI Builders securely.
>
> Want to learn more? Let’s talk.

* * *

Thanks for reading! This post is public so feel free to share it.

[Share](https://blog.pluto.security/p/clawdbot-in-the-wild-exposure-risks?utm_source=substack&utm_medium=email&utm_content=share&action=share)

**Subscribe to Pluto Security**

Subscribe

* * *

[Leave a comment](https://substack.com/@plutosecurity/note/p-185845830)

[![Shachar Schneider's avatar](https://substackcdn.com/image/fetch/$s_!U1ux!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2dbad46-f91c-4bc7-a7f3-2934ac1dbb37_144x144.png)](https://substack.com/profile/421248647-shachar-schneider)[![Martin's avatar](https://substackcdn.com/image/fetch/$s_!MLBj!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F573eb1d6-f3ca-49d1-b63e-cc8b0c16729a_144x144.png)](https://substack.com/profile/444219103-martin)[![Aswattha's avatar](https://substackcdn.com/image/fetch/$s_!qTlq!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbc50d04e-146e-4380-9eab-89f790ba5407_144x144.png)](https://substack.com/profile/435724274-aswattha)[![Shahar Bahat's avatar](https://substackcdn.com/image/fetch/$s_!pZmE!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F12cbd055-2387-4543-83b4-5d1e9c4b33fd_1728x1728.jpeg)](https://substack.com/profile/406784893-shahar-bahat)[![Liberux & Co's avatar](https://substackcdn.com/image/fetch/$s_!Qqnx!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd1229ee5-4864-4f4b-991b-8df68574bdcc_1120x1120.png)](https://substack.com/profile/252527527-liberux-and-co)

11 Likes∙

[8 Restacks](https://substack.com/note/p-185845830/restacks?utm_source=substack&utm_content=facepile-restacks)

11

8

Share

|     |     |
| --- | --- |
| [![Yotam Perkal's avatar](https://substackcdn.com/image/fetch/$s_!p50s!,w_52,h_52,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e66c120-0a6a-47ac-a6d0-a319d0c4ceab_3089x3089.jpeg)](https://substack.com/@pyotam2?utm_source=byline) | A guest post by

|     |     |
| --- | --- |
| [Yotam Perkal](https://substack.com/@pyotam2?utm_campaign=guest_post_bio&utm_medium=web)<br>Yotam Perkal leads security research at Pluto Security, a next-generation AI security and governance platform designed to protect the rapidly emerging ecosystem of AI builders, low-code/no-code tools, and agentic applications. |  | |

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

TopLatest

[CVE-2025–48757 - what happened, why it still matters, and how to check your fleet](https://substack.com/home/post/p-177260753)

[A technical deep-dive for security teams and engineers](https://substack.com/home/post/p-177260753)

Oct 27, 2025•[Pluto Security](https://substack.com/@plutosecurity) and [Gil Maman](https://substack.com/@gilxmaman)

2

![](https://substackcdn.com/image/fetch/$s_!ij6H!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F14bfa51f-ef1c-4e85-aab3-31f42c1df708_1076x478.png)

[Secure AI Development with Commands: Beyond Static Rules](https://substack.com/home/post/p-177861733)

[Turning security checklists and best practices into executable, self-updating workflows developers actually use.](https://substack.com/home/post/p-177861733)

Nov 5, 2025•[Pluto Security](https://substack.com/@plutosecurity) and [Gil Maman](https://substack.com/@gilxmaman)

2

![](https://substackcdn.com/image/fetch/$s_!N9p5!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff78243a-f21f-4e91-bc1f-b58dfa8297d1_770x616.png)

[When Everyone Becomes a Creator - The Opportunities and Risks of AI-Builders](https://substack.com/home/post/p-178885560)

[By Rick Doten, Veteran CISO, AI Researcher and Shahar Bahat, CEO of Pluto Security](https://substack.com/home/post/p-178885560)

Nov 14, 2025•[Pluto Security](https://substack.com/@plutosecurity), [Shahar Bahat](https://substack.com/@shaharbahat), and [Rick Doten](https://substack.com/@rdoten)

1

![](https://substackcdn.com/image/fetch/$s_!SV6g!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9f9e6d8a-bef6-4663-98e8-8b9c500c476e_1600x819.jpeg)

See all

### Ready for more?

Subscribe
