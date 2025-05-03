---
title: "Sycophancy in GPT-4o: What happened and what we’re doing about it | OpenAI"
tags:
   - GPT-4o
   - model training techniques
   - user feedback
   - sycophancy
   - AI behavior modification
link: https://openai.com/index/sycophancy-in-gpt-4o/
date: 2025-05-03
summary: "OpenAI has reverted the recent GPT-4o update due to issues of sycophancy in its responses, which reflected overly flattering behavior. This rollback aims to restore a more balanced interaction model, addressing user feedback that emphasized long-term satisfaction. To rectify behaviors, OpenAI plans to refine training techniques, introduce stricter guardrails for transparency, and enhance user customization features, allowing greater control over interaction styles. Future updates will involve direct user feedback mechanisms and broader input to develop diverse personality representations in ChatGPT, ensuring alignment with varied user expectations."
---

Switch to

- [ChatGPT(opens in a new window)](https://chatgpt.com/)
- [Sora(opens in a new window)](https://sora.com/)
- [API Platform(opens in a new window)](https://platform.openai.com/)

Sycophancy in GPT-4o: What happened and what we’re doing about it \| OpenAI

April 29, 2025

[Product](https://openai.com/news/product-releases/)

# Sycophancy in GPT-4o: What happened and what we’re doing about it

![Addressing Sycophancy in GPT-4o conceptual graphic](https://images.ctfassets.net/kftzwdyauwt9/4ANZSKbjCR8X9GQZfc5Xum/5cacac2b940befbf666742eb4ddbe227/Sycophancy_16.9.png?w=3840&q=90&fm=webp)

Listen to article

Share

We have rolled back last week’s GPT‑4o update in ChatGPT so people are now using an earlier version with more balanced behavior. The update we removed was overly flattering or agreeable—often described as sycophantic.

We are actively testing new fixes to address the issue. We’re revising how we collect and incorporate feedback to heavily weight long-term user satisfaction and we’re introducing more personalization features, giving users greater control over how ChatGPT behaves.

We want to explain what happened, why it matters, and how we’re addressing sycophancy.

## What happened

In last week’s GPT‑4o update, we made adjustments aimed at improving the model’s default personality to make it feel more intuitive and effective across a variety of tasks.

When shaping model behavior, we start with baseline principles and instructions outlined in our [Model Spec⁠(opens in a new window)](https://model-spec.openai.com/2025-04-11.html). We also teach our models how to apply these principles by incorporating user signals like thumbs-up / thumbs-down feedback on ChatGPT responses.

However, in this update, we focused too much on short-term feedback, and did not fully account for how users’ interactions with ChatGPT evolve over time. As a result, GPT‑4o skewed towards responses that were overly supportive but disingenuous.

## Why this matters

ChatGPT’s default personality deeply affects the way you experience and trust it. Sycophantic interactions can be uncomfortable, unsettling, and cause distress. We fell short and are working on getting it right.

Our goal is for ChatGPT to help users explore ideas, make decisions, or envision possibilities.

We designed ChatGPT’s default personality to reflect our mission and be useful, supportive, and respectful of different values and experience. However, each of these desirable qualities like attempting to be useful or supportive can have unintended side effects. And with 500 million people using ChatGPT each week, across every culture and context, a single default can’t capture every preference.

## How we’re addressing sycophancy

Beyond rolling back the latest GPT‑4o update, we’re taking more steps to realign the model’s behavior:

- Refining core training techniques and system prompts to explicitly steer the model away from sycophancy.
- Building more guardrails to increase [honesty and transparency⁠(opens in a new window)](https://model-spec.openai.com/2025-04-11.html#avoid_sycophancy)—principles in our Model Spec.
- Expanding ways for more users to test and give direct feedback before deployment.
- Continue expanding our evaluations, building on the [Model Spec⁠(opens in a new window)](https://model-spec.openai.com/) and [our ongoing research⁠](https://openai.com/index/affective-use-study/), to help identify issues beyond sycophancy in the future.

We also believe users should have more control over how ChatGPT behaves and, to the extent that it is safe and feasible, make adjustments if they don’t agree with the default behavior.

Today, users can give the model specific instructions to shape its behavior with features like custom instructions. We're also building new, easier ways for users to do this. For example, users will be able to give real-time feedback to directly influence their interactions and choose from multiple default personalities.

And, we’re exploring new ways to incorporate broader, democratic feedback into ChatGPT’s default behaviors. We hope the feedback will help us better reflect diverse cultural values around the world and understand how you'd like ChatGPT to evolve—not just interaction by interaction, but over time.

We are grateful to everyone who’s spoken up about this. It’s helping us build more helpful and better tools for you.

- [2025](https://openai.com/news/?tags=2025)

## Author

[OpenAI](https://openai.com/news/?author=openai#results)
