---
date: '2025-12-13'
description: OpenAI's development of the Sora Android app demonstrates the effective
  use of Codex in software engineering. Built in just 28 days with a lean team, Sora
  showcases a crash-free rate of 99.9%. The process emphasized nimble collaboration,
  avoiding the pitfalls of scaling teams, and instead leveraging Codex like a senior
  engineer. Codex excelled in code generation, testing coverage, and rapid comprehension
  of large codebases. This highlights a shift towards AI-assisted development, necessitating
  human oversight to ensure architectural integrity. The project suggests future engineering
  will blend human intuition with AI capability for enhanced efficiency and creativity.
link: https://openai.com/index/shipping-sora-for-android-with-codex/
tags:
- Software Engineering
- Codex
- Cross-Platform Development
- AI Development
- Android App Development
title: How we used Codex to build Sora for Android in 28 days ◆ OpenAI
---

Switch to

- [ChatGPT(opens in a new window)](https://chatgpt.com/?openaicom-did=ed69b6ac-6e17-4ba9-b606-b69fb160b9a8&openaicom_referred=true)
- [Sora(opens in a new window)](https://sora.com/)
- [API Platform(opens in a new window)](https://platform.openai.com/)

OpenAI

December 12, 2025

[Engineering](https://openai.com/news/engineering/)

# How we used Codex to build Sora for Android in 28 days

By Patrick Hum and RJ Marsan, Members of the Technical Staff

Loading…

Share

In November, we launched the Sora Android app to the world, giving anyone with an Android device the ability to turn a short prompt into a vivid video. On launch day, the app reached #1 in the Play Store. Android users generated more than a million videos in the first 24 hours.

Behind the launch is a story: the initial version of Sora’s production Android app was built in 28 days, thanks to the same agent that’s available to any team or developer: Codex.

From October 8 to November 5, 2025, a lean engineering team working alongside Codex and consuming roughly 5 billion tokens, shipped Sora for Android from prototype to global launch. Despite its scale, the app has a crash-free rate of 99.9 percent and an architecture we’re proud of. If you’re wondering whether we used a secret model, we used an early version of the GPT‑5.1-Codex model – the same version that any developer or business can use today via CLI, IDE extension, or web app.

Prompt: figure skater performs a triple axle with a cat on her head

#### Embracing Brooks’ Law: Staying nimble to move fast

When Sora launched on iOS, usage exploded. People immediately began generating a stream of videos. On Android, by contrast, we had only a small internal prototype and a mounting number of pre-registered users on Google Play.

A common response to a high stakes, time-pressured launch is to pile on resources and add process. A production app of this scope and quality would typically involve many engineers working for months, slowed down by coordination.

American computer architect Fred Brooks famously warned that “adding more people to a late software project makes it later.” In other words, when trying to ship a complex project quickly, adding more engineers can often slow down efficiency by adding to communication overhead, task fragmentation, and integration costs. We leaned into this insight instead of ignoring it; we assembled a strong team of four engineers – all equipped with Codex to drastically increase each engineer’s impact.

Working this way, we shipped an internal build of Sora for Android to employees in 18 days and launched publicly 10 days later. We maintained a high bar on Android engineering practices, invested in maintainability, and held the app to the same reliability bar we would expect from a more traditional project. (We also continue to use Codex extensively today to evolve and bring new features to the app).

#### Onboarding a new senior engineer

To make sense of how we worked with Codex, it helps to know where it shines and where it needs direction. Treating it like a newly hired senior engineer was a good approach. Codex’s ability meant we could spend more time directing and reviewing code than writing it ourselves.

**Where Codex needs guidance**

1. Codex isn’t yet great at inferring what it hasn’t been told (e.g., your preferred architecture patterns, product strategy, real user behavior, and internal norms or shortcuts).
2. Similarly, Codex couldn’t see the app actually run: It couldn’t open Sora on a device, notice that a scroll felt off, or sense that a flow was confusing. Only our team could cover these experiential tasks.
3. Each instance requires onboarding. Sharing context with clear goals, constraints, and guidance on “how we do things” was essential to making Codex execute well.
4. In the same vein, Codex struggled with deep architectural judgment: Left on its own, it might introduce an extra view model where we really wanted to extend an existing one or push logic into the UI layer that clearly belonged in a repository. Its instinct is to get something working, not to prioritize long‑term cleanliness.

We found it useful to have Codex create and maintain a generous amount of AGENT.md files throughout the codebase. This made it easy to apply the same guidance and best practices across sessions. For example, to ensure Codex wrote code in our style guidelines, we added the following to our top-level AGENTS.md:

#### Plain Text

``1## Formatting and static checks

2- **Always run** `./gradlew detektFix` (or for the affected modules) **before committing**. CI will fail if formatting or detekt issues are present.

``

**Where Codex excels**

1. Reading and understanding large codebases rapidly: Codex knows essentially all major programming languages, which makes it easier to leverage the same concepts across many platforms without complex abstractions.
2. Testing coverage: Codex is (uniquely) enthusiastic about writing unit tests to cover a broad variety of cases. Not every test was deep, but having breadth of coverage was helpful in preventing regressions.
3. Applying feedback: In a similar vein, Codex is good at reacting to feedback. When CI failed, we could paste log output into a prompt and ask Codex to propose fixes.
4. Massively parallel, disposable execution: Most won’t push the limits of the number of sessions they could actually run at any one time. It’s highly feasible to test multiple ideas in parallel and view code as disposable.
5. Offering new perspective: In design discussions, we used Codex as a generative tool to explore potential failure points and discover new ways to solve a problem. For example, while we designed video player memory optimizations, Codex sifted through multiple SDKs to propose approaches we wouldn’t have had time to parse. The insights from Codex’s research proved invaluable in minimizing memory footprint in the final app.
6. Enabling higher‑leverage work: In practice, we ended up spending more time reviewing and directing code than writing it ourselves. That said, Codex is very good at code review, too, often catching bugs before they’re merged, improving reliability.

Once we acknowledged these characteristics, our working model became more straightforward. We leaned on Codex to do a huge amount of heavy lifting inside well‑understood patterns and well‑bounded scopes, while our team focused on architecture, user experience, systemic changes, and final quality.

#### Laying the foundation by hand

Even the best new, senior hire doesn’t have the right vantage point for making long-term trade-offs right away. To leverage Codex and ensure its work was robust and maintainable, it was key that we oversaw the app’s systems design and key trade-offs ourselves. These included shaping the app’s architecture, modularization, dependency injection, and navigation; we also implemented authentication and base networking flows.

From this foundation, we wrote a few representative features end‑to‑end. We used the rules we wanted the entire codebase to follow and documented project‑wide patterns as we went. By pointing Codex to representative features, it was able to work more independently within our standards. For a project that we estimate was 85% written by Codex, a carefully planned foundation avoided costly backtracking and refactoring. It was one of the most important decisions we made.

The idea was not to make “something that works” as quickly as possible, rather to make “something that gets how we want things to work.” There are many “correct” ways to write code. We didn’t need to tell Codex exactly what to do; we needed to show Codex what’s “correct” on our team. Once we had established our starting point and how we liked to build, Codex was ready to start.

To see what would happen, we did try prompting: “Build the Sora Android app based on the iOS code. Go,” but quickly aborted that path. While what Codex created technically worked, the product experience was sub-par. And without a clear understanding of endpoints, data, and user flows, Codex’s single-shot code was unreliable (Even without using an agent, it’s risky to merge thousands of lines of code.)

We hypothesized Codex would thrive in a sandbox of well-written examples; and we were right. Asking Codex to “build this settings screen” with almost no context was unreliable. Asking Codex to “build this settings screen using the same architecture and patterns as this other screen you just saw” worked far better. Humans made the structural decisions and set the invariants; Codex then filled in large amounts of code inside that structure.

#### Planning with Codex before coding

Our next step in maximizing Codex’s potential was figuring out how to enable Codex to work for long periods of time (recently, [more than 24 hours⁠](https://openai.com/index/gpt-5-1-codex-max/)), unsupervised.

Early on in using Codex, we jumped to prompts like, “Here is the feature. Here are some files. Please build it.” That sometimes worked, but mostly produced code that technically compiled, while straying from our architecture and goals.

So we changed the workflow. For any non‑trivial change, we first asked Codex to help us understand how the system and code work. For example, we’d ask it to read a set of related files and summarize how that feature works; for example, how data flows from the API through the repository layer, the view model, and into the UI. Then we would correct or refine its understanding. (For example, we’d point out that a particular abstraction really belongs in a different layer or that a given class exists only for offline mode and should not be extended.)

Similarly to how you might engage a new, highly capable teammate, we worked with Codex to create a solid implementation plan. That plan often looked like a miniature design document directing which files should change, what new states should be introduced, and how logic should flow. Only then did we ask Codex to start applying the plan, one step at a time. One helpful tip: for very long tasks, where we hit the limit of our context window, we’d ask Codex to save its plan to a file, allowing us to apply the same direction across instances.

This extra planning loop turned out to be worth the time. It allowed us to let Codex run “unsupervised” for long stretches, because we knew its plans. It made code review easier, because we could check the implementation against our plan rather than reading a diff without context. And when something went wrong, we could debug the plan first and the code second.

The dynamic felt similar to the way a good design document gives a tech lead confidence in a project. We weren’t just generating code: we were producing code that supported a shared roadmap.

#### Distributed engineering

At the peak of the project, we were often running multiple Codex sessions in parallel. One was working on playback, another on search, another on error handling, and sometimes another on tests or refactors. It felt less like using a tool and more like managing a team.

Each session would periodically report back to us with progress. One might say, “I’m done planning out this module; here’s what I propose,” while another would offer a large diff for a new feature. Each required attention, feedback, and review. It was uncannily similar to being a tech lead with several new engineers, all making progress, all needing guidance.

The result was a collaborative flow. Codex’s raw coding capability freed us from a lot of manual typing. We had more time to think about architecture, read pull requests carefully, and test out the app.

At the same time, that extra speed meant we always had something waiting in our review queue. Codex didn’t get blocked by context switching, but we did. Our bottleneck in development shifted from writing code to making decisions, giving feedback, and integrating changes.

This is where Brooks’s insights land in a new way. You can’t simply add Codex sessions and expect linear speedups any more than you can keep adding engineers to a project and expect the schedule to shrink linearly. Each additional “pair of hands,” even virtual ones, adds coordination overhead. We had become the conductor of an orchestra versus simply faster solo players.

#### Codex as a cross‑platform superpower

We started our project with a huge stepping stone: Sora had already shipped on iOS. We frequently pointed Codex at the iOS and backend codebases to help it understand key requirements and constraints. Throughout the project we joked that we had reinvented the idea of a cross‑platform framework. Forget React Native or Flutter; _the future of cross‑platform is just Codex._

Beneath the quip are two principles:.

1. Logic is portable. Whether the code is written in Swift or Kotlin, the underlying application logic – data models, network calls, validation rules, business logic – are the same. Codex is very good at reading a Swift implementation and producing an equivalent in Kotlin that preserves semantics.
2. Concrete examples provide powerful context. A fresh Codex session that can see “here is exactly how this works on iOS” and “here is the Android architecture” is far more effective than one that’s only working from natural language descriptions.

Putting these principles to work, we made the iOS, backend and Android repos available in the same environment. We gave Codex prompts like:

“Read these models and endpoints in the iOS code and then propose a plan to implement the equivalent behavior on Android using our existing API client and model classes.”

One small but useful trick was to detail in  `~/.codex/AGENTS.md` where local repos lived and what they contained. That made it easier for Codex to discover and navigate relevant code.

We were effectively doing cross-platform development through translation instead of shared abstraction. Because Codex handled most of the translation, we avoided doubling implementation costs.

The broader lesson is that for Codex, context is everything. Codex did its best work when it understood how the feature already worked in iOS, paired with an understanding of how our Android app was structured. When Codex lacked that context, it wasn’t “refusing to cooperate”; it was guessing. The more we treated it like a new teammate and invested in giving it the right inputs, the better it performed.

#### The software engineering of tomorrow, today

By the end of our four‑week sprint, using Codex stopped feeling like an experiment and became our default development loop. We used it to understand existing code, plan changes, and implement features. We reviewed its output the same way we’d review a teammate’s. It was simply how we shipped software.

It became clear that AI‑assisted development does not reduce the need for rigor; it increases it. As capable as Codex is, its objective is to get from A to B, now. This is why AI-assisted coding doesn’t work without humans. Software engineers can understand and apply the real-world constraints of systems, the best ways to architect software, and how to build with future development and product plans in mind. The super powers of tomorrow’s software engineer will be deep systems understanding and the ability to work collaboratively with AI over long time horizons.

The most interesting parts of software engineering are building compelling products, designing scalable systems, writing complex algorithms, and experimenting with data, patterns, and code. However, the realities of software engineering of the past and present often lean more mundane: centering buttons, wiring endpoints, and writing boilerplate. Now, Codex makes it possible to focus on the most meaningful parts of software engineering and the reasons we love our craft.

Once Codex is set up in a context-rich environment where it understands your goals and how you like to build, any team can multiply its capabilities. Our launch retro isn’t a one‑size‑fits‑all recipe, and we're not claiming to have solved AI‑assisted development. But we hope our experience makes it easier to find the best ways to empower Codex to empower you.

When Codex launched in a research preview seven months ago, software engineering looked very different. Through Sora, we got to explore the next chapter of engineering. As our models and harness keep improving, AI will become an increasingly indispensable part of building.

What will you make with your own team of Codex?

- [Sora](https://openai.com/news/?tags=sora)
- [2025](https://openai.com/news/?tags=2025)

## Acknowledgements

_Special thanks to the entire team that helped build Sora for Android._

## Authors

[Patrick Hum](https://openai.com/news/?author=patrick-hum#results), [RJ Marsan](https://openai.com/news/?author=rj-marsan#results)

## Keep reading

[View all](https://openai.com/news/engineering/)

![AtlasBlog Art Card SEO 1x1](https://images.ctfassets.net/kftzwdyauwt9/6g2Y2DIZG548CNl02tzjIz/ab8e6edb0c34b4965b363652878fe50a/AtlasBlog_Art_Card___SEO_1x1.png?w=3840&q=90&fm=webp)

[How we built OWL, the new architecture behind our ChatGPT-based browser, Atlas\\
\\
EngineeringOct 30, 2025](https://openai.com/index/building-chatgpt-atlas/)
