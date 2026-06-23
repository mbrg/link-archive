---
date: '2026-06-23'
description: Daniel Miessler outlines strategic META-prompts for leveraging the anticipated
  return of the AI model Fable, focusing on system optimization rather than task execution.
  Key areas include harness optimization by aligning system goals, auditing self-models
  against current behaviors, and enhancing memory retention. Security measures are
  escalated through robust prompt injection defenses and infrastructure audits. Additionally,
  prompts aim for holistic life optimization, addressing major life decisions and
  identifying potential constraints. This approach emphasizes iterative system improvement,
  strategic decision-making, and long-term resilience against emerging AI advancements.
link: https://danielmiessler.com/blog/prompts-to-run-when-fable-comes-back
tags:
- AI
- system optimization
- development workflows
- META-prompts
- security upgrades
title: 10 Prompts to Run When Fable Comes Back ◆ Daniel Miessler
---

# 10 Prompts to Run When Fable Comes Back

Tactical META-prompts that benefit from maximum intelligence to upgrade your entire system

June 18, 2026

[#ai](https://danielmiessler.com/archives/?tag=ai) [#harness](https://danielmiessler.com/archives/?tag=harness) [#meta-work](https://danielmiessler.com/archives/?tag=meta-work)

 Glanding-slumber…

28 reading now

![A runner coiled in the starting blocks, looking down a glowing purple lane](https://danielmiessler.com/images/things-to-do-when-fable-comes-back.webp)

Now that people have tasted Fable and [had it pulled away](https://www.anthropic.com/news/fable-mythos-access), many of us are queueing up work to have it do when it comes back.

I think the key is to focus on META-work, i.e., work that helps other work. Or, _system_ upgrades vs. task upgrades.

Here are the ones I have planned and/or that I recommend:

# 10 Prompts That Benefit from the Smartest Models [​](https://danielmiessler.com/blog/prompts-to-run-when-fable-comes-back\#_10-prompts-that-benefit-from-the-smartest-models)

## Harness optimization [​](https://danielmiessler.com/blog/prompts-to-run-when-fable-comes-back\#harness-optimization)

These prompts are related to improving our AI harness at a deep level across different dimensions.

### Goal orientation [​](https://danielmiessler.com/blog/prompts-to-run-when-fable-comes-back\#goal-orientation)

- Look at our overall harness. I need you to:
  - Characterize what I'm ultimately trying to accomplish with it
  - Then look at what parts of the system — such as our system prompt, AGENTS/CLAUDE.md files, hooks, skills, etc. — are working against that overall goal
  - And if you don't see a clear goal in our harness, interview me about it so we can get the system working cohesively in a single direction
  - ultracode

### Bitter lesson optimization [​](https://danielmiessler.com/blog/prompts-to-run-when-fable-comes-back\#bitter-lesson-optimization)

- Deeply study Richard Sutton's Bitter Lesson essay and how it applies to overengineering, specifically for AI / Coding harnesses. Then I need you to:
  - Do a full analysis of our AI harness in its entirety
  - Look for places where we're violating Bitter Lesson Engineering
  - Give me a comprehensive plan for upgrading our system to be more flexible to future improvements in the models we use
  - ultracode

### Self-model audit [​](https://danielmiessler.com/blog/prompts-to-run-when-fable-comes-back\#self-model-audit)

- Read everything my harness believes about me — identity, goals, voice, preferences — and find where it's modeling a version of me that's stale, aspirational, or just wrong. I need you to:
  - Compare what my files say I am against what my recent behavior and work actually reveal
  - Flag every place the system is optimizing for who I said I was, not who I am now
  - Propose the specific edits that close the gap
  - ultracode

### Memory that compounds [​](https://danielmiessler.com/blog/prompts-to-run-when-fable-comes-back\#memory-that-compounds)

- Look at everything my harness remembers and how it learns across sessions. I need you to:
  - Find where knowledge goes to die — captured but never resurfaced, or never captured at all
  - Tell me whether it's actually getting smarter about me or just accumulating
  - Design the retention, decay, and promotion rules that make every session compound into the next
  - ultracode

### What does "better" even mean [​](https://danielmiessler.com/blog/prompts-to-run-when-fable-comes-back\#what-does-better-even-mean)

- I can't improve what I can't measure. I need you to:
  - Define what "better" actually means for my harness — not vanity metrics, the thing I care about
  - Build the evals and regression checks that catch it getting worse before I feel it
  - Find where I'm already optimizing a proxy that's drifting from what I really want
  - ultracode

### The autonomy ladder [​](https://danielmiessler.com/blog/prompts-to-run-when-fable-comes-back\#the-autonomy-ladder)

- Map what my harness does on its own versus what it asks me to approve. I need you to:
  - Find where I've handed an agent authority I shouldn't have, and where I'm withholding it out of fear and paying for it
  - Calibrate each action by risk against leverage, not habit
  - Redesign the trust boundary so it's neither reckless nor asking permission for everything
  - ultracode

## Security upgrades [​](https://danielmiessler.com/blog/prompts-to-run-when-fable-comes-back\#security-upgrades)

These prompts involve upgrading how the harness handles security at multiple levels.

### Prompt injection handling [​](https://danielmiessler.com/blog/prompts-to-run-when-fable-comes-back\#prompt-injection-handling)

- Do deep analysis of our overall AI harness and imagine and model how vulnerable it is to various levels of Prompt Injection. I need you to:
  - Map out all the different inputs to the harness
  - How the different input avenues are handled from a Prompt Injection standpoint using which models
  - Based on the data that we have access to and the tools that we have access to, figure out what our Prompt Injection defense should be
  - Research the best tools available
  - And then finally give a full plan and recommendation on how to upgrade our harness in the long term so that it is less vulnerable to Prompt Injection overall
  - ultracode

### Deployed infrastructure audit [​](https://danielmiessler.com/blog/prompts-to-run-when-fable-comes-back\#deployed-infrastructure-audit)

Go look at everything I have deployed across all my various projects, across all hosts, vendors, sites, and technologies and come up with a comprehensive list which we'll add to attacksurface.md.

This will be a running list of things we need to keep updated and assessed continuously. I want to understand and constantly audit things like:

- What tech do they use?
- Self-hosted or third-party?
- How do we auth into that service
- What are common security issues and misconfigurations for that platform / tech
- What all do we have deployed there?
- Is it a web property? Databases? APIs? What is the total attack surface for that system?
- What are the security mechanisms we've defended that infra with? What exposure does each of those services have to different audiences, e.g., public, internal, behind VPN, token required, OAuth, etc?

Build an AttackSurface Skill that maintains this attacksurface.ai file as a resource, plus an AssessAttackSurface workflow that can assess any of our attack surfaces thoroughly and efficiently, and come up with a recommended frequency for continuous testing based on criticality and cost.

## Overall life and work optimization [​](https://danielmiessler.com/blog/prompts-to-run-when-fable-comes-back\#overall-life-and-work-optimization)

These are massive scope prompts that basically help you sort out your priorities, your projects, and come up with a plan for maximizing the next crucial few years.

### Big picture [​](https://danielmiessler.com/blog/prompts-to-run-when-fable-comes-back\#big-picture)

I need you to take a look at all my various projects and writing online and all the different activities we've been doing in our harness here, and what you know about me from web search and such, and then deeply analyze that.

Then I want you to take a look at what is going on in my field, what's going on with AI, what's going on with society and the future in general, and tell me what you think solves the Japanese Ikigai for me. What do you think I should be working on that will give me fulfillment but also be lucrative doing it for myself or with other collaborators or working for a corporation?

Make a number of concrete recommendations if you have them, and feel free to interview me to ask for additional context before creating the output. The goal is to clear up the chaos and chaotic nature of my different projects and help me get focused in a single direction. I could come up with:

- A domain
- A plan for how to publish my different projects
- How to explain them to others at parties or work events, et cetera.

Basically I'm confused about what all I'm doing and how I should focus it given all the change in the world.

### Where am I most wrong [​](https://danielmiessler.com/blog/prompts-to-run-when-fable-comes-back\#where-am-i-most-wrong)

- Take everything you know about me, my plans, and my biggest current bets, and turn on me. I need you to:
  - Steelman the case that my largest bet is wrong
  - Surface the load-bearing beliefs my decisions rest on that I've never actually checked
  - Tell me what evidence would change my mind, and whether I'd even notice it
  - ultracode

### What 10×s and what dies [​](https://danielmiessler.com/blog/prompts-to-run-when-fable-comes-back\#what-10%C3%97s-and-what-dies)

- Given where frontier AI is actually heading, I need you to:
  - Tell me which parts of my work and life are about to go obsolete, and which are about to 10×
  - Separate what I should stop investing in now from what I should pour into
  - Give me the specific changes to make this year, not someday
  - ultracode

### Decisions into policy [​](https://danielmiessler.com/blog/prompts-to-run-when-fable-comes-back\#decisions-into-policy)

- Find the decisions I make over and over and stop re-litigating them. I need you to:
  - Surface the choices I remake from scratch every time, and the latent rule behind each
  - Sort them by reversibility and stakes — where I'm slow on cheap reversible calls and reckless on expensive irreversible ones
  - Turn each into a standing policy I can run on autopilot
  - ultracode

### The one real constraint [​](https://danielmiessler.com/blog/prompts-to-run-when-fable-comes-back\#the-one-real-constraint)

- Out of everything limiting my life and work, I need you to:
  - Find the single binding constraint — the actual bottleneck, not the loudest problem
  - Show me where I'm pouring effort into things that aren't the constraint
  - Tell me the one move that relieves it, and what becomes possible once it's gone
  - ultracode

### The bus-factor audit [​](https://danielmiessler.com/blog/prompts-to-run-when-fable-comes-back\#the-bus-factor-audit)

- If I vanished for 30 days, I need you to tell me:
  - What breaks, and what only keeps running because it's in my head and never in the system
  - Every undocumented dependency and you-shaped hole in how my life and work run
  - The plan to get the load-bearing stuff out of my head and into something durable
  - ultracode

## Development [​](https://danielmiessler.com/blog/prompts-to-run-when-fable-comes-back\#development)

Loops that help you code better.

### Peter Steinberger's loop prompt [​](https://danielmiessler.com/blog/prompts-to-run-when-fable-comes-back\#peter-steinberger-s-loop-prompt)

- While repository maintenance is active, wake every five minutes.

- Triage \[repositories\] and read each repository thread's latest state.

- Reuse one thread per repository; assign its highest-value bounded task only within granted permissions, and do not interrupt coherent active work.

- Require tests, live proof, autoreview, and green CI before work can land.

- Escalate product, access, security, or irreversible decisions. Record meaningful changes and stop when every item is landed, decision-ready, blocked, or has no work.


## Public presence [​](https://danielmiessler.com/blog/prompts-to-run-when-fable-comes-back\#public-presence)

Getting your public presence unified in the right place online.

### Blog consolidation [​](https://danielmiessler.com/blog/prompts-to-run-when-fable-comes-back\#blog-consolidation)

Go and find everything I've written online since I've been writing on the internet across all different platforms, social media accounts, et cetera, and unify them into my permanent blog under my permanent domain which is \_\_\_\_\_\_\_\_\_\_\_\_. Look at that domain, and if you think it's a good one for a permanent location, let's keep it. If you think I should use a different one, then recommend some others.

But take a look at everything in my content and everything I've done recently, and everything you know about me from my harness and all contacts you have about me, and figure out what the best domain name should be. It's most likely going to be some variation of first name, last name, but maybe that doesn't make sense.

Ultimately, I need to get everything consolidated into a single location so I don't have all my different ideas and projects and content spread out to places where it will disappear over time as different platforms come in and out of style. Let's get it all unified into a single location with a single host at our single domain.

Share

[Post](https://ul.live/share-x?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fprompts-to-run-when-fable-comes-back&title=10%20Prompts%20to%20Run%20When%20Fable%20Comes%20Back "Share on X") [LinkedIn](https://ul.live/share-linkedin?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fprompts-to-run-when-fable-comes-back&title=10%20Prompts%20to%20Run%20When%20Fable%20Comes%20Back "Share on LinkedIn") [HN Hacker News](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fprompts-to-run-when-fable-comes-back&title=10%20Prompts%20to%20Run%20When%20Fable%20Comes%20Back "Share on Hacker News") [Reddit](https://ul.live/share-reddit?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fprompts-to-run-when-fable-comes-back&title=10%20Prompts%20to%20Run%20When%20Fable%20Comes%20Back "Share on Reddit") [Facebook](https://ul.live/share-facebook?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fprompts-to-run-when-fable-comes-back&title=10%20Prompts%20to%20Run%20When%20Fable%20Comes%20Back "Share on Facebook") [Forward](https://ul.live/share-email?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fprompts-to-run-when-fable-comes-back&title=10%20Prompts%20to%20Run%20When%20Fable%20Comes%20Back "Share via Email")

Follow

[Get The Newsletter](https://ul.live/nlpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fprompts-to-run-when-fable-comes-back&title=10%20Prompts%20to%20Run%20When%20Fable%20Comes%20Back) [Follow On X](https://ul.live/xpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fprompts-to-run-when-fable-comes-back&title=10%20Prompts%20to%20Run%20When%20Fable%20Comes%20Back) [Subscribe On YouTube](https://ul.live/ytpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fprompts-to-run-when-fable-comes-back&title=10%20Prompts%20to%20Run%20When%20Fable%20Comes%20Back) [Follow On LinkedIn](https://ul.live/lipostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fprompts-to-run-when-fable-comes-back&title=10%20Prompts%20to%20Run%20When%20Fable%20Comes%20Back)

## supporting = loving

For 29.6672 years I've been creating ad-free technical tutorials and essays here. 3,060 pieces and counting.

It's a one-person effort that's also my livelihood. If it makes your day easier or more pleasant in any way, please consider supporting the work with a monthly or one-time donation.

It helps me make more content, and is deeply appreciated as well. 🫶🏼

### Monthly Support

[♥ $5](https://buy.stripe.com/7sY14g3Ne7qq3ybeV20x20m) [♥ $10](https://buy.stripe.com/eVq00c2Jah10gkX9AI0x20n) [♥ $25](https://buy.stripe.com/3cI14gdnO9yy2u714c0x20o) [♥ $50](https://buy.stripe.com/6oUdR2erS9yy5Gj14c0x20p) [♥ $100](https://buy.stripe.com/4gMbIU97y9yy0lZ9AI0x20q)

### One-Time Support

[♥ $5](https://buy.stripe.com/3cIeV66Zq7qq3yb4go0x20r) [♥ $10](https://buy.stripe.com/dRmdR2cjK5ii5Gj14c0x20s) [♥ $25](https://buy.stripe.com/eVq14gabCcKK1q37sA0x20t) [♥ $50](https://buy.stripe.com/14AcMY2Ja8uub0D28g0x20u) [♥ $100](https://buy.stripe.com/28E9AM5Vm1220lZfZ60x20v)

Search

This post was tagged with:

aiharnessmetawork

[HOME](https://danielmiessler.com/)· [BLOG](https://danielmiessler.com/blog)· [ARCHIVES](https://danielmiessler.com/archives)· [ABOUT](https://danielmiessler.com/about)
