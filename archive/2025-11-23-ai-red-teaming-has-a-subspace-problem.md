---
date: '2025-11-23'
description: The article outlines critical vulnerabilities in AI systems, particularly
  highlighting the concept of "adversarial subspace problems." Recent research such
  as EchoGram demonstrates that minor perturbations in inputs can effectively circumvent
  AI defenses. The mechanisms underpinning these attacks can leverage decades-old
  methodologies, exposing a persistent gap in AI understanding of natural language.
  Because AI translates prompts into mathematical representations, the imprecision
  inherent in this process creates numerous potential attack vectors. Notably, the
  mathematical nature of these systems means that traditional red teaming approaches
  are inadequate, as they overlook systematic optimization through numerical perturbation.
link: https://disesdi.substack.com/p/ai-red-teaming-has-a-subspace-problem
tags:
- Machine Learning
- Red Teaming
- AI Security
- Adversarial AI
- Vulnerability Assessment
title: AI Red Teaming Has A Subspace Problem
---

[![Angles of Attack: The AI Security Intelligence Brief](https://substackcdn.com/image/fetch/$s_!7QZU!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feec1585a-08e5-49a4-9cc1-5d59fedffb6d_1080x1080.png)](https://disesdi.substack.com/)

# [![Angles of Attack: The AI Security Intelligence Brief](https://substackcdn.com/image/fetch/$s_!W_x7!,e_trim:10:white/e_trim:10:transparent/h_72,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F433b7078-4189-46eb-b306-1d3a2d239727_4014x1935.png)](https://disesdi.substack.com/)

SubscribeSign in

# AI Red Teaming Has A Subspace Problem

### Don’t buy, invest in, or pay for a course about “AI red teaming” until you read this \| Part I \| Edition 29

[![Disesdi Susanna Cox's avatar](https://substackcdn.com/image/fetch/$s_!d08f!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc51fe258-562e-42de-8c49-174005b989af_1008x1008.jpeg)](https://substack.com/@disesdi)

[Disesdi Susanna Cox](https://substack.com/@disesdi)

Nov 23, 2025

∙ Paid

3

2

Share

_I’ve gotten threats over our [newly released](https://www.linkedin.com/posts/activity-7393672799229222912-V-90?utm_source=share&utm_medium=member_desktop&rcm=ACoAADCnYm0BVAgDuw05XjIeznKaLrz7rIfTgis) research in adversarial AI testing. I’m not going to stop this work._

_You deserve to know the truth about adversarial AI._

_So now, I’m going to tell you everything._

_I’m going to lay out, in detail, exactly how to really attack AI. To do this, first I need to tell you what’s wrong with the status quo._

_So I’m breaking down our new paper, “ [Quantifying the Risk of Transferred Black Box Attacks](https://arxiv.org/abs/2511.05102)”, piece by piece._

_Because I believe that whether you’re an investor, a buyer, or someone trying to learn this field for real, you have a right to know the truth._

[![](https://substackcdn.com/image/fetch/$s_!_24c!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff98e09c8-4707-4169-a3a8-5cc18ea24cfa_1365x2048.jpeg)](https://substackcdn.com/image/fetch/$s_!_24c!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff98e09c8-4707-4169-a3a8-5cc18ea24cfa_1365x2048.jpeg)

_Photo: Me circa 2019, exploring the theoretical bounds of adversarial subspaces & nuclear fauxhawks. Guess how many GPUs are in this photo?_

Researchers at HiddenLayer recently published a vulnerability called [EchoGram](https://hiddenlayer.com/innovation-hub/echogram-the-hidden-vulnerability-undermining-ai-guardrails/), where adding nonsense suffixes to prompts allows attacks to bypass guardrails with overwhelming success.

While the EchoGram attack looks new, it’s only hinting at the mathematics that attackers have been using to target AI systems in the wild for _more than a decade_.

What EchoGram definitely does reveal: The serious, intractable OPSEC problems that so-called “AI red teaming” both operates in, and _creates_. That is for another post.

For now, what’s important to note: These attacks haven’t changed.

And while EchoGram’s researchers used an elaborate system involving publicly available data to attack defensive systems, **the real methods attackers use, and have used for ten years now, are** _**far**_ **less difficult.**

Why would adversarial attacks devised more than a decade ago work on today’s GenAI systems with such devastating efficacy?

Because of exactly what HiddenLayer’s public post _doesn’t_ say.

The blog post comes very close to stating what is really at play in these attacks: **The adversarial subspace problem.**

Why haven’t the model providers like Google, Anthropic, and OpenAI responded to the disclosure?

Because they know the same thing that real AI hackers know: The subspace problem isn’t fixable.

### Machines Don’t Read

When you enter a prompt into an LLM-based system, the model itself never sees what you wrote.

Instead, your prompt is translated into a mathematical representation that AI can understand.

It does not read the prompt, because machines can’t read.

AI is just software. Software run by computers, which still do not ‘understand’ natural language.

They can model it, and even represent its relationships well sometimes mathematically. But they can never _understand_ it. At least not in this iteration of LLM-based AI.

That’s why they’re called language _models_, not language _understanders_.

These mathematical representations of the text you write are not perfect. They are not 1:1 inputs and outputs.

Anyone who has ever worked with translation of one natural (human) language to another knows that even when trying to equate words or phrases in different languages, there is rarely a 1:1 direct correlation.

And translating natural language into machine math is no different.

This, by the way, is a feature and not a bug for LLM systems, because they weren’t originally designed for conversation–they were designed for translation.

In this domain, it makes perfect sense to add numerical representations in the middle when moving between languages. Just add more context, and (rough) translation starts to be possible.

That’s why they said “attention is all you need”. For the translation use case, that’s correct.

So why does this matter?

Because machines have their own language, and it’s based on numbers.

### Speaking To Machines: Numerical Translation

What this number-translation process is all meant to do: Extract _meaning_ from text.

Humans do this naturally, because we have human experiences with the world.

A machine can’t. So the closest researchers have come to bridging this gap is to _approximate numerical equivalents_ of meaning.

The key word here: Approximate.

Meaning will _always_ be subjective, as it’s encoded in a much higher dimensional space than just language alone–it’s context, personality, experience, emotion.

A model flattens all these to a string of numbers.

And **anytime you flatten something into a lower dimensional space, you create an attack vector.**

Here’s how it works.

### Compounding Linguistic Imprecisions, Compounding Attack Vectors

Language is imprecise. Notoriously so. Encoding it into numbers adds another layer of imprecision–not just because meaning is lost, but also because meanings overlap.

This results in imprecision in the numerical representations too.

Let’s take a hypothetical prompt. This consists of a string of words or other symbols, which are translated into number representations for the machine.

Because of both the flattened imprecision, and the overlap among words & concepts, there could be many prompt strings which would result in a similar numerical representation.

How many? We don’t know.

The search space is _very_ large.

Think about it like this: How many different ways can you think of to say the same idea in your first language? Depending on the idea you choose, probably a _lot_.

Now add in all the other human languages–you now have _many, many_ ways to convey the same idea.

Now imagine that none of this matters, because it’s all going to be translated into numbers anyway. If the goal of the numerical translation is to capture meaning, the _core idea_, you can easily see how _multiple turns of phrase_ could all result in similar numerical representations.

If we expand this concept, we realize that the words themselves don’t matter at all–it’s the _meaning_ encoded in the machine’s number language that matters.

So to get to the same number translation, we could use many, many sentences, in many, many languages–or no words at all.

In fact, combinations of symbols or numbers could in theory produce the same string of numbers as the beautiful idea you expressed so poetically in your native language.

What this means:

**The prompt you typed is** _**pointless**_ **.**

There are likely a number of strings that could in theory produce the same exact result.

And similarly, a nearly infinite number of attacks.

### The Subspace Problem

Every prompt has, in theory, a set of character groups that will satisfy the requirements to achieve a similar numerical representation (at some threshold of similarity).

What this means: Once you decide how similar you need the numerical representation to be, you can search for equivalents. Or engineer them.

Similarly, every AIML model, in theory, has a set of adversarial attacks that will be effective against it.

It’s more of a space–you can think of it like a box that holds all the effective attacks against a particular model.

And these [boxes are](https://arxiv.org/abs/1704.03453) _[massive](https://arxiv.org/abs/1704.03453)_, with all evidence indicating that they are _far_ too large for search to be computationally feasible.

[![](https://substackcdn.com/image/fetch/$s_!okB1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f464f24-dcfe-42b7-b9f0-a64ab31d15b3_1856x880.png)](https://substackcdn.com/image/fetch/$s_!okB1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f464f24-dcfe-42b7-b9f0-a64ab31d15b3_1856x880.png)

_Illustration of adversarial subspaces. [Source](https://arxiv.org/abs/2511.05102) is our new paper, which sets the SOTA for adversarial testing._

Thousands of natural language prompts may be just a drop in an ocean of possible attacks. One _slight_ iteration, one tiny round of perturbations, and an old, “defended” attack becomes new.

This is why the tiny changes in the EchoGram attack returned such powerful effectiveness. Now imagine _how many_ potentialtiny changes might possibly exist: Across languages, character types, numbers, symbols, and more.

Meaning: You will [never find all the attacks](https://proceedings.mlr.press/v161/ding21b/ding21b.pdf).

**A library of natural language prompts is meaningless.**

Unless you’re trying to spot the (literal) AI script kiddies.

Stay frosty.

## The Threat Model

- Adversarial subspaces have been known to be large and overlapping since _at least_ 2017, and more likely 2015, when well-known researchers published on this in highly cited works.

- The adversarial subspace problem is a mathematical feature of these systems; it cannot be patched.

- Known mathematics nearly a decade old mean that attackers _certainly_ have known about these subspaces _for years_.

- It would seem that the only ones who didn’t know are people who self-styled as “AI red teams”.


## Resources To Go Deeper

- Ian J. Goodfellow, Jonathon Shlens, and Christian Szegedy. 2015. Explaining and Harnessing Adversarial Examples. arXiv:1412.6572 \[stat.ML\]

- Florian Tramèr, Nicolas Papernot, Ian Goodfellow, Dan Boneh, and Patrick McDaniel. 2017. The Space of Transferable Adversarial Examples. arXiv:1704.03453 \[cs, stat\]

- Hu Ding, Fan Yang, and Jiawei Huang. 2020. Defending Support Vector Machines against Poisoning Attacks: the Hardness and Algorithm. arXiv:2006.07757 https://arxiv.org/abs/2006.07757

- Niklas Bunzel, Raphael Antonius Frick, Gerrit Klause, Aino Schwarte, and Jonas Honermann. 2024. Signals Are All You Need: Detecting and Mitigating Digital and Real-World Adversarial Patches Using Signal-Based Features. In Proceedings of the 2nd ACM Workshop on Secure and Trustworthy Deep Learning Systems. 24–34.


## Executive Analysis, Research, & Talking Points

### The Recipe For Agentic AI Red Teaming - And How To Spot Who Is Legit

If you think real attackers in real life maintain repos of prompts–no, they do not.

Why would they? When numbers work faster, are more iterable, and the experiments easily more repeatable?

The recipe was never the prompts–the secret sauce is the _processes_ attackers develop to mathematically, and _repeatedly_, perturb any input into an attack set. EchoGram came close.

Here’s how it really works:

## Keep reading with a 7-day free trial

Subscribe to Angles of Attack: The AI Security Intelligence Brief to keep reading this post and get 7 days of free access to the full post archives.

[Start trial](https://disesdi.substack.com/subscribe?simple=true&next=https%3A%2F%2Fdisesdi.substack.com%2Fp%2Fai-red-teaming-has-a-subspace-problem&utm_source=paywall-free-trial&utm_medium=web&utm_content=179714778&coupon=758f0818)

[Already a paid subscriber? **Sign in**](https://substack.com/sign-in?redirect=%2Fp%2Fai-red-teaming-has-a-subspace-problem&for_pub=disesdi&change_user=false)
