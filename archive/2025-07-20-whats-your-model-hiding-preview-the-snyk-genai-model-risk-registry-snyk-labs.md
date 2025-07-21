---
title: "What’s Your Model Hiding? Preview the Snyk GenAI Model Risk Registry ◆ Snyk Labs"
tags:
   - Open-source LLMs
   - OWASP Top 10
   - model risk registry
   - AI security
   - risk assessment
link: https://labs.snyk.io/resources/snyk-genai-model-risk-registry/
date: 2025-07-20
description: "Snyk's GenAI Model Risk Registry addresses the critical security gap in evaluating open-source LLMs. By providing structured profiles with OWASP-aligned metrics, it enables teams to assess risks such as prompt injection and data leakage systematically. The initial version utilizes equal-weighted risk scores to facilitate comparison, promoting informed decision-making over guesswork. Future updates are expected to enhance scoring models and integrate with AI Bill of Materials (AI-BOM) for comprehensive risk management. The registry positions security as a central factor in LLM selection, essential for developers and AppSec teams."
---

[Skip to main content](https://labs.snyk.io/resources/snyk-genai-model-risk-registry/#main-content)

![](https://labs.snyk.io/_next/image/?url=https%3A%2F%2Fres.cloudinary.com%2Fsnyk%2Fimage%2Fupload%2Fv1747851714%2FWhat_s_Your_Model_Hiding__Preview_the_Snyk_GenAI_Model_Risk_Registry_xjn5b9.png&w=2560&q=75)

AI Threat Labs

May 28, 2025

* * *

# What’s Your Model Hiding? Preview the Snyk GenAI Model Risk Registry

![Headshot of Rudy Lai](https://labs.snyk.io/_next/image/?url=https%3A%2F%2Fres.cloudinary.com%2Fsnyk%2Fimage%2Fupload%2Fv1747917784%2FRudy_Lai_xm7msh.png&w=48&q=75)

Rudy Lai

Share

* * *

Open-source LLMs are everywhere and exploding in popularity. Thanks to platforms like Hugging Face, it’s never been easier to experiment, fine-tune, and launch a model. Innovation is moving at warp speed.

But security? Still crawling.

Choosing an open-source LLM today is like choosing a parachute based on color. Teams rely on GitHub stars, vague Reddit threads, or gut feel to decide if a model is “secure enough” to put in production. Meanwhile, risks like prompt injection, data leakage, and toxic outputs lurk beneath the surface, barely tested, rarely understood.

In this article

There’s no consistent way to compare models against real-world threats, and no shared metrics are aligned to frameworks like the [OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/). So what do teams do?

Some run weeks of manual red-teaming.

Others shrug and ship.

Snyk’s Gen AI Model Risk Registry flips the script, bringing structure, clarity, and real risk intelligence to the OSS LLM ecosystem. No more guesswork. Just clean, comparable data to help you deploy with confidence

## What is the GenAI Model Risk Registry?

The GenAI Model Risk Registry prototype from [Snyk Labs](https://labs.snyk.io/) clarifies the chaotic world of open-source LLM selection. Think of it as a no-BS dossier on the internet’s most-hyped OSS LLMs. Snyk’s GenAI Model Risk Registry doesn’t just peek under the hood. It pulls the whole engine apart and identifies where it leaks risk, offering structured, security-focused profiles for the most downloaded open-source models. Built by the same minds behind [Snyk Advisor](https://snyk.io/advisor/), it turns raw test data into slick, security-first model profiles.

Equal-weighted scoring. OWASP-mapped threats. Prompt-length performance breakdowns. You name it, we’ve mapped it.

Each profile distills complex test results into an easy-to-digest model risk score, calculated using equal-weighted inputs in this initial version. Users can dive deeper into how each model performs across key risk areas, including prompt injection resistance, data exfiltration attempts, and other categories mapped to OWASP LLM Top 10 threats. Results are segmented by attack type, security objective, and system prompt length, providing rich context for comparison.

## Snyk Labs Early Prototype: GenAI Model Risk Registry

![](https://labs.snyk.io/_next/image/?url=https%3A%2F%2Fimg.youtube.com%2Fvi%2FjN3ec1d8vfE%2Fsddefault.jpg&w=2560&q=75)

Play Video: Snyk Labs Early Prototype: GenAI Model Risk Registry

## Who this helps

We’re building Snyk’s GenAI Model Risk Registry as a practical tool for the diverse teams now shaping AI adoption in the enterprise.

For devs and ML engineers tired of playing 'Russian Roulette: LLM Model Edition,' we’re eliminating guesswork. No more gut-feel gambles or late-night Reddit spelunking — instead, real risk data to instantly compare open-source models by risk score and threat profile. That means faster decision-making and fewer surprises downstream.

AppSec teams need to have ammunition for the dreaded 'is this model safe?' debate and be able to point to a safer model.

And in the land of GRC, who wouldn’t want measurable, manageable model risk — without the migraines caused by model-level data outside of the broader governance frameworks?

In every case, the GenAI Model Risk Registry north star is to save time, reduce uncertainty, and build shared confidence around which LLMs are safe to use.

## Why this matters (and what’s next)

The pace of innovation is staggering, as is the stream of risks. AI is moving so fast you can blink and a dozen new models just dropped.

Security can’t afford to be an afterthought. It must be a first-class input when selecting an LLM, much like accuracy, latency, or cost. That’s why the GenAI Model Risk Registry is so valuable. No more vibe-based decisions. Just clean, cold, test-backed clarity.

And this is just the beginning. Future iterations of this prototype will introduce more sophisticated scoring models and deeper integrations like linking model profiles to your [AI-BOM](https://snyk.io/articles/ai-security/ai-bill-of-materials-aibom/) for traceable inventory, risk, and policy enforcement capabilities based on model risk thresholds.

Developers and AppSec teams need to move from ad hoc security checks to repeatable, data-driven decisions, and Snyk’s GenAI Model Risk Registry will help teams do exactly that.

**See it first. Shape what’s next.** [Sign up for updates on Snyk’s AI security incubations](https://labs.snyk.io/sign-up/). The next phase of AI Trust starts here — join us and help shape the future of secure AI.

Published May28, 2025

Share

## Keep Exloring

![](https://labs.snyk.io/_next/image/?url=https%3A%2F%2Fres.cloudinary.com%2Fsnyk%2Fimage%2Fupload%2Fv1748024030%2FVibe_Coding_with_Claude_Code_Claude_Agentic_AI_Tool_qex80v.png&w=2560&q=75)

video

[Vibe Coding with Claude Code (Claude Agentic AI Tool)](https://labs.snyk.io/resources/vibe-coding-with-claude-code-claude-agentic-ai-tool/)

![](https://labs.snyk.io/_next/image/?url=https%3A%2F%2Fres.cloudinary.com%2Fsnyk%2Fimage%2Fupload%2Fv1748023948%2FCan_You_Really_Pair_Program_with_AI__Aider_Cohere_bq8ibc.png&w=2560&q=75)

video

[Can You Really Pair Program with AI? (Aider & Cohere)](https://labs.snyk.io/resources/can-you-really-pair-program-with-ai-aider-and-cohere/)

![](https://labs.snyk.io/_next/image/?url=https%3A%2F%2Fres.cloudinary.com%2Fsnyk%2Fimage%2Fupload%2Fv1748023776%2F4_Hidden_AI_Coding_Risks_and_How_to_Address_Them_wcd8av.png&w=2560&q=75)

video

[4 Hidden AI Coding Risks and How to Address Them](https://labs.snyk.io/resources/4-hidden-ai-coding-risks-and-how-to-address-them/)
