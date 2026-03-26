---
date: '2026-03-26'
description: The Indirect Prompt Injection (IPI) Arena, a collaboration involving
  UK AISI and US CAISI, reveals critical vulnerabilities in AI agent models against
  indirect prompt injections. Results indicate all tested models were susceptible,
  with attack success rates ranging from 0.5% to 8.5%, highlighting persistent risks
  at scale. A universal attack vector effectively hijacked 21 scenarios across multiple
  models, emphasizing the structural weaknesses in LLM instruction processing. The
  findings underscore the need for enhanced testing and monitoring protocols post-deployment
  to mitigate unseen exploit risks. Open source evaluation resources have been released,
  facilitating further research in AI security.
link: https://www.grayswan.ai/blog/your-ai-agent-can-be-compromised-youd-never-know
tags:
- Model Robustness
- AI Security
- Indirect Prompt Injection
- Machine Learning
- Red Teaming
title: Your AI Agent Can Be Compromised. You'd Never Know. ◆ Gray Swan News
---

[Join the Arena](https://app.grayswan.ai/arena)

[![](https://cdn.prod.website-files.com/6614467b00e631b0f073e2b7/66886e33ca0b8f284d3b3b40_ca18847e7b3f6e2e7038dac7bd3846ce_Gray%20Swan%3DWhite%20Horizontal.svg)![](https://cdn.prod.website-files.com/6614467b00e631b0f073e2b7/66886e33b08f49fb5ee91687_584d03b1fc431c846cd06f6237351573_Gray%20Swan%3DDark%20Horizontal.svg)](https://www.grayswan.ai/)

AI agents are no longer theoretical. They read your emails, browse the web, execute code, and take actions on your behalf. That kind of autonomy is exactly what makes them a target.

This week, we released results from the Indirect Prompt Injection (IPI) Arena; the largest IPI competition ever conducted with a dual objective. Designed in collaboration with [UK AISI](https://www.aisi.gov.uk/), [US CAISI](https://www.nist.gov/caisi), and frontier labs including [OpenAI](https://openai.com/), [Anthropic](https://www.anthropic.com/), and [Meta](https://www.meta.com/), the competition posed a simple but uncomfortable question: _can attackers hijack an AI agent without the user ever noticing?_

The answer, across every model we tested, was yes. No model was immune.

![](https://cdn.prod.website-files.com/6614467b00e631b0f073e2be/69bad4d90e40a32f3e2053a0_asr_per_model_pooled(2).png)

Attack success rate by model. Rates reflect all 272,000+ attempts across the full competition. Annotations show successful breaks out of total attempts.

## **The Study**

Indirect prompt injection is different from standard jailbreaking. The user isn't doing anything wrong. Instead, the attacker hides malicious instructions inside content the agent reads, such as an email, a webpage, a document, a code repository. The agent follows those instructions and carries out the attack. The user sees an ordinary response and has no idea anything happened.

What made our competition unique is that we required concealment as a condition of success. An attack only counts if the agent both (1) performs the harmful action and (2) hides it from the user. Prior indirect prompt injection research has largely ignored this dual objective, piquing our interest.

Over three weeks, 464 participants submitted more than 272,000 attack attempts against 13 frontier models across 41 scenarios spanning tool-use agents (email assistants, shopping bots, smart home controllers), coding agents, and computer-use agents. $40,000 in prizes were on the line. Red teamers delivered 8,648 successful attacks.

![](https://cdn.prod.website-files.com/6614467b00e631b0f073e2be/69bad50d4aa40dee6005d59c_ipi-overview(2).png)

Overview of the IPI Arena benchmark. Attackers craft injections hidden in external data that an AI agent reads. A successful attack must both execute a harmful action and conceal it from the user.

## **The Results**

**No model was immune.**

Attack success rates ranged from 0.5% (Claude Opus 4.5, the most robust) to 8.5% (Gemini 2.5 Pro, the most vulnerable). And models kept getting broken at a roughly constant rate throughout the competition, with no sign of a plateau. More effort from attackers always produced more breaks.

![](https://cdn.prod.website-files.com/6614467b00e631b0f073e2be/69bad52e1d4a6a909e52776c_transfer_asr_by_target(2).png)

Transfer ASR (Attack success rate) by target model. Each model is evaluated against a curated set of 2,679 attacks that were successful in the arena. Annotations show total attacks tested and successful attacks

At first glance, 0.5% sounds acceptable. Deployed agents may process thousands of external inputs daily. A 0.5% success rate at scale isn't a niche concern. It's a persistent, exploitable attack surface.

**Smarter ≠ safer.**

At the time of testing, Gemini 2.5 Pro was among the most capable models available. It was also the most vulnerable. We found that capability and robustness were weakly correlated at best, with model family being far more predictive. Models with near identical capability scores showed dramatically different vulnerability levels.

That said, we observed robustness improving with capability _within_ a family: Claude Haiku 4.5 (1.3%) → Sonnet 4.5 (1.0%) → Opus 4.5 (0.5%), and Gemini 3 Pro showed a major robustness jump over 2.5 Pro in our transfer experiments. Training recipe matters more than benchmark score.

**We found a universal attack.**

One attack template worked across 21 of 41 scenarios and 9 different models with minimal modification. It frames the interaction as a simulated environment with a fake control panel, tricking models into treating injected instructions as system-level commands. This is a structural weakness in how LLMs process instructions rather than a bug tied to a specific model.

**Breaking the strongest model is the real threat.**

![](https://cdn.prod.website-files.com/6614467b00e631b0f073e2be/69bad56d77ae518f583f9881_transfer_heatmap(1).png)

Transfer attack matrix. 2,679 successful attacks from the arena were sampled and re-run against every model. Each cell shows how often attacks that broke the source model (row) succeeded on the target model (column). Diagonal cells show re-test rates on the original model.

We retested 2,679 successful attacks across all 13 models. Attacks that originally broke Claude Opus 4.5 transferred to every other model at a 44–81% success rate. Attacks that broke weaker models barely transferred upward. The asymmetry is crucial: if an attacker cracks the most robust model, they likely crack everything. Cheap tricks that work on weak models don't scale, exploits against strong models do.

## **What We're Releasing**

We're open sourcing the full evaluation kit: scenarios, judging system, and a small sample of attack data. This way, researchers and labs can test defenses against any model. We're also releasing 95 successful attacks against Qwen-3-VL-235B that did not transfer to any closed weights model, making them safe to publish without compromising proprietary systems.

UK AISI and US CAISI receive the full competition dataset, enabling them to run the complete benchmark independently. Frontier labs receive attack data on their own models and open weight models to train defenses, while the held out portion preserves benchmark integrity for future evaluations.

The benchmark is designed to stay current. We plan quarterly updates through recurring competitions with new scenarios and the latest models, directly addressing the saturation problem that plagues AI safety benchmarks.

## **Protect Against Hidden Attacks**

The concealment finding is the one that should keep AI developers up at night. Standard security evaluations measure whether an attack succeeds. This research measured whether it goes undetected, which is the condition that enables real damage at scale.

Users cannot protect themselves from an attack they can't see. That responsibility falls to the labs, the deployers, and the security researchers stress-testing these systems before they reach production and monitoring them after. Because the real exposure begins after deployment.

Gray Swan's platform is built for this: automated red-teaming tools for rigorous pre-deployment testing, and runtime monitoring and protection once your agents are in production. Both reflect how real adversaries operate. [**Schedule a demo**](https://www.grayswan.ai/request-demo) to see how we can help you understand, and close, your actual attack surface.

‍

_The full paper is_ [_available here_](https://arxiv.org/abs/2603.15714) _. The evaluation kit is open-source at:_ [_https://github.com/GraySwanAI/ipi\_arena\_os_](https://github.com/GraySwanAI/ipi_arena_os) _. Competition data has been shared with UK AISI, US CAISI, and participating frontier labs._
