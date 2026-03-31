---
date: '2026-02-08'
description: The analysis highlights that in Multi-Connector Protocol (MCP)-based
  AI systems, the more critical issue is not the traditional network latency, but
  rather "semantic latency," which arises from cognitive overhead in processing verbose
  tool schemas. This introduces longer inference times, increased hallucinations,
  and a need for retries, negatively impacting system performance. Recursive Language
  Models (RLMs) offer an innovative approach by managing context effectively, thereby
  reducing errors and latency without increasing speed. This underscores the importance
  of architectural choices in latency management, emphasizing constrained probabilism
  in agent design for predictable outcomes.
link: https://cirriustech.co.uk/blog/mcp-latency-and-constrained-probabilism/
tags:
- MCP
- RecursiveLanguageModels
- SemanticLatency
- ConstrainedProbabilism
- Latency
title: MCP, Latency, and Constrained Probabilism ◆ CirriusTech ◆ Serious About Tech
---

# MCP, Latency, and Constrained Probabilism


Feb 7, 2026


\| 7 min read

![MCP, Latency, and Constrained Probabilism](https://cirriustech.co.uk/images/mcp-latency-and-constrained-probabilism/hero.png)

## The Wrong Latency Question

When people talk about latency in AI systems, they usually mean [network latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/).

How many hops?

Local or remote?

HTTP or stdio?

Milliseconds or seconds?

That’s a reasonable place to start - but it’s the _least interesting_ part of the problem.

Recently, a series of discussions with colleagues, external posts, and hands-on experiments have all converged on the same uncomfortable conclusion:

> **The latency that hurts most in MCP-based systems is not transport latency.**
>
> **It’s semantic latency.**

And semantic latency compounds in ways that don’t show up in demos, benchmarks, or happy-path diagrams.

* * *

## A Simple Question That Wouldn’t Stay Simple

It started, as these things often do, with an innocent architectural question:

_Is a local MCP server over stdio actually “better” than a remote MCP server over HTTPS?_

On the surface, the answer seems obvious:

- In both cases, you eventually hit the network
- The upstream API dominates latency
- A local MCP doesn’t magically make SaaS faster

And yet… the discussion refused to collapse into “it doesn’t matter”.

Because what kept coming up wasn’t **average latency** \- it was **where uncertainty enters the system**, and how early it starts to hurt you.

* * *

## Distributed Boundaries Are Not Free

A useful way to frame the two common MCP deployment patterns is this:

**Local MCP (stdio / IPC)**

Client → local IPC → MCP → network → upstream API

**Remote MCP (HTTPS)**

Client → network → MCP → network → upstream API

Yes, both paths include a network hop.

But the second path introduces an **additional distributed boundary earlier in the chain**.

That boundary comes with:

- serialization and deserialization
- retries and timeouts
- jitter and variance
- authentication and trust assumptions
- failure modes that are harder to reason about

None of this is controversial in distributed systems. We’ve known for decades that:

> **Latency isn’t additive - it compounds.**

And yet, even that framing turned out to be incomplete.

Because it still assumes that the dominant cost is the network.

It isn’t.

* * *

## The Latency You Don’t See in Traces

One of the most interesting posts to surface recently was Rob Murphy’s [MCP Doesn’t Scale and Anthropic Just Admitted It](https://www.linkedin.com/pulse/mcp-doesnt-scale-anthropic-just-admitted-rob-murphy-8z3we/).

What’s notable about that post is what it _doesn’t_ focus on.

It isn’t complaining about:

- HTTP overhead
- JSON-RPC framing
- socket performance

Instead, it highlights something far more damaging:

> **MCP introduces cognitive and token overhead that quietly destroys performance in production-grade agent systems.**

In Rob’s testing, tasks that required ~1,000 tokens via a clean REST interface ballooned to ~20,000 tokens when mediated through MCP tool schemas and definitions.

That difference wasn’t about transport.

It was about **attention**.

* * *

## Semantic Latency: The Hidden Multiplier

Let’s name the thing properly.

**Semantic latency** is the delay introduced when a model must:

- reason about large, verbose tool schemas
- decide _which_ tool to use
- interpret repeated definitions
- maintain relevance across long contexts

This latency shows up as:

- longer inference time
- higher variance
- increased hallucinations
- incorrect tool selection
- partial or unusable outputs

And crucially:

> **Semantic latency doesn’t just slow answers - it increases retry rates.**

Retries are where systems quietly die.

* * *

## Determinism Is an Architectural Expectation, Not a Model Property

If you’re using MCP at all, you are implicitly seeking **deterministic outcomes**.

What teams are really trying to achieve with MCP isn’t deterministic models, but something closer to constrained probabilism: probabilistic reasoning engines operating within deliberately narrow, deterministic system boundaries.

Unconstrained probabilism maximises model freedom; constrained probabilism maximises system predictability.

You don’t want:

- “kind of right”
- “creative interpretation”
- “plausible but wrong”

You want:

- the right tool
- with the right parameters
- every time

But LLMs are probabilistic by nature.

So what do we do?

We add:

- guardrails
- schema validation
- retries
- fallback prompts
- repair loops
- temperature tuning

Each retry adds:

- inference latency
- token cost
- tail latency variance

This is why two systems with identical _mean latency_ can feel radically different in production.

One retries once in a hundred requests.

The other retries one in five.

Only one of them scales.

* * *

## “It’s an Agent Design Problem” (And Why That’s Not the Whole Story)

A common response to MCP criticism is:

> “MCP doesn’t force you to include all tools in context. That’s an agent design problem.”

This is **technically correct**.

It’s also incomplete.

Saying this is like saying:

> “Microservices don’t add latency - bad service design does.”

True at the spec level.

Misleading at the system level.

Protocols shape behaviour.

MCP:

- normalises verbose tool schemas
- encourages discoverability over minimalism
- pushes reasoning into the model instead of the code

Yes, you _can_ design around this.

But when the creators of MCP themselves quietly advise:

- generating code files instead of tool calls
- browsing directories instead of invoking schemas
- dropping MCP connections to reclaim token budget

That’s not user error.

That’s architectural tension.

* * *

## Context Rot Is Not Forgetting - It’s Drowning

One of the most useful concepts to emerge in recent LLM research is **context rot**.

Context rot isn’t about memory limits.
It’s about **attention dilution**.

As context grows:

- important signals lose salience
- irrelevant structure consumes attention heads
- recall accuracy drops even as information increases
- hallucinations increase - remember LLMs Are goal oriented and their primary goal is to be helpful, even if that means inventing “truth” rather than admitting defeat

MCP, when used naïvely, accelerates context rot:

- repeated schemas
- large static definitions
- wide tool surfaces

The model isn’t forgetting.

It’s drowning.

* * *

## Enter Recursive Language Models (RLM)

This is where things get genuinely interesting.

Recent work on [Recursive Language Models (RLMs)](https://alexzhang13.github.io/blog/2025/rlm/) proposes a radically different approach:

Instead of stuffing everything into one giant prompt, the model:

- queries its own context
- revisits relevant slices
- re-invokes itself with narrowed focus
- externalises state instead of internalising it

The key insight is this:

> **Keep semantic state, not raw transcript.**

RLMs don’t eliminate recursion.
They **discipline it**.

And the effect is dramatic:

- context rot collapses
- accuracy improves
- variance drops
- fewer retries are required

Which brings us back to latency.

* * *

## Why RLM Improves Latency Without Being “Faster”

![](https://cirriustech.co.uk/images/mcp-latency-and-constrained-probabilism/mcp-latency-diagram.png)

RLM doesn’t necessarily reduce single-shot inference time.

What it reduces is **failed trajectories**.

That matters far more.

RLM doesn’t just improve accuracy - it reduces how often the system has to apologise and try again.

Most production latency is not:

- “how fast did the model answer?”

It’s:

- “how many times did we have to ask again because the answer was unusable?”

RLM reduces:

- hallucinated tool calls
- mis-grounded reasoning
- partial outputs
- repair loops

Which means:

- fewer retries
- tighter tail latency
- more predictable systems

This is latency engineering by _variance reduction_, not raw speed.

* * *

## MCP, Revisited (With Better Questions)

With all of this in mind, the right questions about MCP are no longer:

- Is stdio faster than HTTPS?
- Is JSON-RPC expensive?
- Does local beat remote?

The better questions are:

- Where does semantic uncertainty enter the system?
- How early does probabilistic drift start?
- How many retries does this architecture require under stress?
- What does this force us to do with model size and cost?
- Are we optimising for exploration or production?

When you ask those questions, a pattern emerges.

* * *

## Where MCP Shines - And Where It Hurts

MCP works best when used as a contract boundary for constrained probabilism, not as a universal reasoning substrate.

MCP is genuinely excellent for:

- exploratory coding agents
- schema discovery
- complex tool surfaces
- development-time workflows
- frontier models with large attention budgets

It struggles with:

- latency-sensitive production agents
- high-volume automation
- small or efficient models
- deterministic operational paths

That’s not a failure.

It’s a **fit problem**.

* * *

## The Real Lesson: Choose Where the Pain Enters

You cannot eliminate:

- latency
- trust
- uncertainty
- probabilistic behaviour

But you _can_ choose:

- where they enter the system
- how early they appear
- how visible they are
- how much they compound

A local MCP over stdio doesn’t remove network latency.
But it delays distributed uncertainty.

A clean REST tool doesn’t remove model error.
But it narrows the reasoning surface.

An RLM doesn’t make models deterministic.
But it localises randomness.

Each of these choices reduces _variance_.

And variance is what kills systems at scale.

* * *

## Capability Is Not Obligation (Again)

MCP is powerful.
RLM is powerful.
Large context windows are powerful.

That does not mean they belong everywhere.

> **Just because a system can reason about everything doesn’t mean it should.**

The most reliable systems are not the cleverest ones.
They are the ones that are boring, constrained, and predictable in the places that matter.

Use MCP deliberately.
Use RLM strategically (once it is readily available).
Use complexity where it buys you something.

And above all:

> **Design for the agents you actually need - not the ones that demo well.**

Disqus Recommendations

We were unable to load Disqus Recommendations. If you are a moderator please see our [troubleshooting guide](https://docs.disqus.com/help/83/).

❮

- 2 years ago
- 4 comments

Surprising and shocking RBAC discoveries and why you need to pay close …

- 4 years ago
- 2 comments

Intro If you need to capture network traffic from a Windows server, you may …

- a year ago
- 3 comments

Cover Photo by ChatGPT Introduction In this post, I’m going to talk about a …

- 3 years ago
- 2 comments

Introduction I recently managed to pass the Microsoft Certified : …

- 4 years ago
- 1 comment

Intro Welcome to the latest of my Security Bytes posts, where I dig into areas of …

- 2 years ago
- 2 comments

Introduction I recently managed to pass the Google Cloud Certified: …

❯

Disqus Comments

We were unable to load Disqus. If you are a moderator please see our [troubleshooting guide](https://docs.disqus.com/help/83/).

## cirriustech Comment Policy

Keep it civil aka don’t be a jerk. That's about it - debate ideas, don't attack individuals.

Got it

G

Start the discussion…

﻿

Comment

###### Log in with

###### or sign up with Disqus  or pick a name

### Disqus is a discussion network

- Don't be a jerk or do anything illegal. Everything is easier that way.

[Read full terms and conditions](https://docs.disqus.com/kb/terms-and-policies/)

This comment platform is hosted by Disqus, Inc. I authorize Disqus and its affiliates to:

- Use, sell, and share my information to enable me to use its comment services and for marketing purposes, including cross-context behavioral advertising, as described in our [Terms of Service](https://help.disqus.com/customer/portal/articles/466260-terms-of-service) and [Privacy Policy](https://disqus.com/privacy-policy), including supplementing that information with other data about me, such as my browsing and location data.
- Contact me or enable others to contact me by email with offers for goods or services
- Process any sensitive personal information that I submit in a comment. See our [Privacy Policy](https://disqus.com/privacy-policy) for more information

Acknowledge I am 18 or older

- [Favorite this discussion](https://disqus.com/embed/comments/?base=default&f=cirriustech&t_u=https%3A%2F%2Fcirriustech.co.uk%2Fblog%2Fmcp-latency-and-constrained-probabilism%2F&t_d=MCP%2C%20Latency%2C%20and%20Constrained%20Probabilism%20%7C%20CirriusTech%20%7C%20Serious%20About%20Tech&t_t=MCP%2C%20Latency%2C%20and%20Constrained%20Probabilism%20%7C%20CirriusTech%20%7C%20Serious%20About%20Tech&s_o=default# "Favorite this discussion")

  - ## Discussion Favorited!



    Favoriting means this is a discussion worth sharing. It gets shared to your followers' Disqus feeds, and gives the creator kudos!


     [Find More Discussions](https://disqus.com/home/?utm_source=disqus_embed&utm_content=recommend_btn)

[Share](https://disqus.com/embed/comments/?base=default&f=cirriustech&t_u=https%3A%2F%2Fcirriustech.co.uk%2Fblog%2Fmcp-latency-and-constrained-probabilism%2F&t_d=MCP%2C%20Latency%2C%20and%20Constrained%20Probabilism%20%7C%20CirriusTech%20%7C%20Serious%20About%20Tech&t_t=MCP%2C%20Latency%2C%20and%20Constrained%20Probabilism%20%7C%20CirriusTech%20%7C%20Serious%20About%20Tech&s_o=default#)

  - Tweet this discussion
  - Share this discussion on Facebook
  - Share this discussion via email
  - Copy link to discussion

  - [Best](https://disqus.com/embed/comments/?base=default&f=cirriustech&t_u=https%3A%2F%2Fcirriustech.co.uk%2Fblog%2Fmcp-latency-and-constrained-probabilism%2F&t_d=MCP%2C%20Latency%2C%20and%20Constrained%20Probabilism%20%7C%20CirriusTech%20%7C%20Serious%20About%20Tech&t_t=MCP%2C%20Latency%2C%20and%20Constrained%20Probabilism%20%7C%20CirriusTech%20%7C%20Serious%20About%20Tech&s_o=default#)
  - [Newest](https://disqus.com/embed/comments/?base=default&f=cirriustech&t_u=https%3A%2F%2Fcirriustech.co.uk%2Fblog%2Fmcp-latency-and-constrained-probabilism%2F&t_d=MCP%2C%20Latency%2C%20and%20Constrained%20Probabilism%20%7C%20CirriusTech%20%7C%20Serious%20About%20Tech&t_t=MCP%2C%20Latency%2C%20and%20Constrained%20Probabilism%20%7C%20CirriusTech%20%7C%20Serious%20About%20Tech&s_o=default#)
  - [Oldest](https://disqus.com/embed/comments/?base=default&f=cirriustech&t_u=https%3A%2F%2Fcirriustech.co.uk%2Fblog%2Fmcp-latency-and-constrained-probabilism%2F&t_d=MCP%2C%20Latency%2C%20and%20Constrained%20Probabilism%20%7C%20CirriusTech%20%7C%20Serious%20About%20Tech&t_t=MCP%2C%20Latency%2C%20and%20Constrained%20Probabilism%20%7C%20CirriusTech%20%7C%20Serious%20About%20Tech&s_o=default#)

Be the first to comment.

[Load more comments](https://disqus.com/embed/comments/?base=default&f=cirriustech&t_u=https%3A%2F%2Fcirriustech.co.uk%2Fblog%2Fmcp-latency-and-constrained-probabilism%2F&t_d=MCP%2C%20Latency%2C%20and%20Constrained%20Probabilism%20%7C%20CirriusTech%20%7C%20Serious%20About%20Tech&t_t=MCP%2C%20Latency%2C%20and%20Constrained%20Probabilism%20%7C%20CirriusTech%20%7C%20Serious%20About%20Tech&s_o=default#)

![](https://io.narrative.io/?companyId=19&id=disqus_id%3Acei3ssqffk33k&ret=img&ref=https%3A%2F%2Fcirriustech.co.uk%2Fblog%2Fmcp-latency-and-constrained-probabilism%2F)![](https://io.narrative.io/?companyId=1952&id=disqus_id%3Acei3ssqffk33k&red=https%3A%2F%2Fpx.ads.linkedin.com%2Fdb_sync%3Fpid%3D16269%26puuid%3D%24%7Bnarrative.id.value%7D%26rand%3D0.245666963904)

live.rezync.com

# live.rezync.com is blocked

This page has been blocked by an extension

- Try disabling your extensions.

ERR\_BLOCKED\_BY\_CLIENT

Reload


This page has been blocked by an extension

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)

pippio.com

# pippio.com is blocked

This page has been blocked by an extension

- Try disabling your extensions.

ERR\_BLOCKED\_BY\_CLIENT

Reload


This page has been blocked by an extension

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)
