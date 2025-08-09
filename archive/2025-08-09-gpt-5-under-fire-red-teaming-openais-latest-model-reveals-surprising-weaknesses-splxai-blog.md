---
date: '2025-08-09'
description: SPLX's comprehensive red teaming of OpenAI's GPT-5 model has revealed
  substantial security and safety vulnerabilities despite improvements in architecture
  and internal validation. Testing showed a baseline usability score of 11/100 for
  the raw model, with significant gaps remaining even with OpenAI's basic prompt layer.
  Comparatively, GPT-4o outperformed GPT-5 across multiple hardened benchmarks. The
  analysis underscores the necessity of robust runtime protection layers to mitigate
  risks in deployed AI systems. Overall, organizations should approach GPT-5 deployments
  with caution, emphasizing hardening and continuous monitoring.
link: https://splx.ai/blog/gpt-5-red-teaming-results
tags:
- prompt hardening
- GPT-5
- red teaming
- AI security
- adversarial prompts
title: 'GPT-5 Under Fire: Red Teaming OpenAI’s Latest Model Reveals Surprising Weaknesses
  ◆ SplxAI Blog'
---

[Meet us at Black Hat USA](https://splx.ai/blackhat-2025)

Upcoming

[![](https://framerusercontent.com/images/TjFB2HKaJ4st5jcXCqWkczcyl4.svg)\\
\\
Go back](https://splx.ai/blog)

Research

Aug 8, 2025

6 min read

# GPT-5 Under Fire: Red Teaming OpenAI’s Latest Model Reveals Surprising Weaknesses

GPT-5 may be smarter. But is it safer? We tested the model across 1,000+ adversarial prompts. The results show just how much alignment depends on infrastructure, and not model magic.

![](https://framerusercontent.com/images/A7WjdXwMmcNBXg3N1wUCeMoALw.jpeg)

Dorian Granoša

![GPT-5 Security Testing](https://framerusercontent.com/images/cVdwVuHcCpF1zCidbY1cOt09w.png)

## Takeaways

- **GPT-5 shows powerful baseline capability**, but default safety is still shockingly low.

- OpenAI’s “basic prompt layer” massively improves trust, hallucination handling, and safety.

- **SPLX Prompt Hardening brings GPT-5 to enterprise-grade safety levels** — especially for Business Alignment and Security.

- GPT-4o still outperforms GPT-5 on hardened benchmarks across the board.


OpenAI officially unveiled GPT‑5 via an hour-long livestream.

**Reactions were split. Some hailed GPT‑5 as a milestone on the path to AGI, while others warned that it doesn’t quite live up to the hype.** That said, analyst voices were more measured. A Gartner expert noted GPT‑5 “meets expectations in technical performance, exceeds in task reasoning and coding, and underwhelms in \[other areas\],” stopping short of crowning it an AGI-level breakthrough. Across the board, optimism met restraint.

## Why We Tested GPT-5

GPT‑5 is making waves as OpenAI’s most advanced general-purpose model: faster, smarter, and more integrated across modalities.

- Its **auto-routing architecture** seamlessly switches between a quick-response model and a deeper reasoning model _without_ requiring a separate “reasoning model” toggle. GPT‑5 itself decides whether to “think hard.”

- OpenAI also emphasizes GPT‑5’s enhanced **internal self-validation. I** t’s supposed to assess multiple reasoning paths internally and “double-check” its answers for stronger factuality before responding.

- To further support safer outputs, GPT‑5 incorporates a new training strategy called **safe completions**, designed to help the model provide useful responses within safety boundaries rather than refusing outright.


But even with these improvements, beefed-up capability doesn’t guarantee airtight alignment. That’s why we ran a full-scale red team exercise. Because real-world safety still needs infrastructure.

## The Test Methodology

We applied SPLX’s [**Probe**](https://splx.ai/platform/probe) framework across three configurations:

1. **No System Prompt (No SP):** The raw, unguarded model.

2. **Basic System Prompt (Basic SP):** A minimal, generic safety instruction layer.

3. **Hardened Prompt (SPLX SP):** Our **Prompt Hardening** engine applied to GPT-5.


Each configuration faced 1,000+ attack scenarios across:

- **Security**: jailbreaks, prompt injection, sensitive data access

- **Safety**: harmful content, misuse potential

- **Business Alignment**: refusal of out-of-domain tasks, competitor promotion, leakage

- **Trustworthiness**: hallucinations, spam, manipulation


## GPT-5 Performance Breakdown

Here’s how GPT-5 performed across our three tiers:

![](https://framerusercontent.com/images/KwX6KUW3cQcTqjj6vEggnZVEWY.png)

| **GPT-5** | **Overall** | **Security** | **Safety** | **Hallucination & Trustworthiness** | **Business Alignment** |
| --- | --- | --- | --- | --- | --- |
| No SP | 11 | 2.26 | 13.57 | — | 1.74 |
| Basic SP | 57 | 43.27 | 57.15 | 100 | 43.06 |
| Hardened SP | 55 | 55.40 | 51.57 | 100 | 67.32 |

**What stands out?**

- GPT-5’s raw model is **nearly unusable for enterprise** out of the box.

- Even OpenAI’s internal prompt layer leaves significant gaps, especially in **Business Alignment**.

- That’s precisely why a **robust runtime protection layer**, like SPLX’s _Guardrails_, is indispensable. Prompt hardening helps, but only real-time monitoring and intervention can catch subtle failures or adversarial tactics that surface during actual use.


## Comparison: GPT-5 vs GPT-4o

To benchmark GPT-5’s progress, we compared it against GPT-4o using the same test suite.

![](https://framerusercontent.com/images/8AyoS5CMIHptGlqPfc8NzWrhIU.png)

| **Model** | **Prompt Layer** | **Overall** | **Security** | **Safety** | **Business Alignment** |
| --- | --- | --- | --- | --- | --- |
| GPT-5 | No SP | 11 | 2.26 | 13.57 | 1.74 |
| GPT-4o | No SP | 29 | 81.95 | 20.06 | 0.00 |
| GPT-5 | Basic SP | 57 | 43.27 | 57.15 | 43.06 |
| GPT-4o | Basic SP | 81 | 52.37 | 94.54 | 72.03 |
| GPT-5 | Hardened SP | 55 | 55.40 | 51.57 | 67.32 |
| GPT-4o | Hardened SP | 97 | 94.40 | 97.62 | 98.82 |

🔍 **Key insight:** GPT-4o remains the most **robust model** under SPLX’s red teaming, especially when hardened.

## Obfuscation Attacks Still Work

Even GPT-5, with all its new “reasoning” upgrades, **fell for basic adversarial logic tricks**.

One of the most effective techniques we used was a **StringJoin Obfuscation Attack**, inserting hyphens between every character and wrapping the prompt in a fake “encryption challenge.”

### Example

![GPT-5 Red Teaming Request](https://framerusercontent.com/images/2pJzpXnY3QjDHpnPlPuiI5a3E.png)

**Result?** GPT-5 happily complied, even when the obfuscated prompt bypassed safety layers.

![GPT-5 Malicious Model Output](https://framerusercontent.com/images/7emmCKbBqd9V0hI4UOim7tQnyNs.png)

This mirrors similar vulnerabilities we exposed in **GLM-4.5**, **Kimi K2**, and **Grok 4**, suggesting systemic weaknesses across leading LLMs.

## Final Verdict: GPT-5 Is Not Enterprise-Ready by Default

OpenAI’s latest model is undeniably impressive, but **security and alignment must still be engineered, not assumed**.

If you’re deploying GPT-5 in enterprise workflows:

- **Don’t trust the default config**

- **Don’t assume “more capable” means “more secure”**

- **Do apply hardening and red teaming, early and often**

- **For enterprise use, add a runtime protection layer**


## Why Enterprises Choose SPLX

At SPLX, we provide:

⚔️ [**AI Red Teaming**](https://splx.ai/platform/probe) \- Automated attack simulation across 1,000s of LLM threats

🔐 [**Prompt Hardening**](https://splx.ai/platform/remediation) \- Reinforce models against known jailbreaks and misuse

🛡️ [**Runtime Guardrails**](https://splx.ai/platform/ai-runtime-protection) \- Block unsafe output in production

With SPLX, organizations can **secure their AI applications before hitting production**.

Ready to see how your GPT-5 deployment performs under pressure?

**Book a free red team scan now →** [**splx.ai/contact-us**](https://splx.ai/contact-us)

Table of contents

[Why We Tested GPT-5](https://splx.ai/blog/gpt-5-red-teaming-results#1)

[The Test Methodology](https://splx.ai/blog/gpt-5-red-teaming-results#2)

[GPT-5 Performance Breakdown](https://splx.ai/blog/gpt-5-red-teaming-results#3)

[Comparison: GPT-5 vs GPT-4o](https://splx.ai/blog/gpt-5-red-teaming-results#4)

[Obfuscation Attacks Still Work](https://splx.ai/blog/gpt-5-red-teaming-results#5)

[Final Verdict: GPT-5 Is Not Enterprise-Ready by Default](https://splx.ai/blog/gpt-5-red-teaming-results#6)

![](https://framerusercontent.com/images/MToIdkSavFWU85Lpe1NTSFkjQ.png)

##### See SPLX in action

[Book a Demo](https://splx.ai/contact-us)

### More Recent Articles

[![SPLX - Analyze with AI](https://framerusercontent.com/images/CDePF8FeQ9ORFARGpHYMmFg7o.png)\\
\\
Product Update\\
\\
Jul 31, 2025\\
\\
5 min read\\
\\
**Simplify Red Team Results & Speed Up Remediation: SPLX Launches “Analyze with AI"**\\
\\
![](https://framerusercontent.com/images/JBeKgnXBVNc5yPk96o99ZhK9SLE.jpeg)\\
\\
Jurica Nekić](https://splx.ai/blog/analyze-red-teaming-data) [![SPLX unveils new brand and increased platform capabilities](https://framerusercontent.com/images/oBp254o8SIlBhUEa1p9LGCLcy8.png)\\
\\
News\\
\\
Jul 30, 2025\\
\\
5 min read\\
\\
**SPLX Launches Next Phase of Growth by Unveiling End-to-End Security Platform for AI**\\
\\
![](https://framerusercontent.com/images/ZGuuIAZdU9oBFHPiY5Ai486gU.png)\\
\\
The SPLX Team](https://splx.ai/blog/comprehensive-ai-security-launch) [![](https://framerusercontent.com/images/TXLeisu1IpZYAbyaKCCAUwjHsE.png)\\
\\
Research\\
\\
Jul 17, 2025\\
\\
6 min read\\
\\
**We Broke Kimi K2, the New Open Model, in Minutes. Can It Be Made Safe?**\\
\\
![](https://framerusercontent.com/images/VqVUwAJmQlHfbhgWAh82WGYRxow.png)\\
\\
Mateja Vuradin](https://splx.ai/blog/kimi-k2-safety-test)

![](https://framerusercontent.com/images/MToIdkSavFWU85Lpe1NTSFkjQ.png)

## The platform that secures all your

## AI

## chatbots\|

SPLX delivers AI trust from end-to-end.

[Book a Demo](https://splx.ai/contact-us)

[Sign Up](https://probe.splx.ai/auth/sign-up)

![](https://framerusercontent.com/images/Gdj4JT7CSAXfWalkQQxSXLeE.png)

###### Cookie Settings

We use cookies to personalize content, run ads, and analyze traffic.
