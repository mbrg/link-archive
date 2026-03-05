---
date: '2026-03-05'
description: The cybersecurity landscape is undergoing a dramatic shift as AI-driven
  exploit generation accelerates time-to-exploit (TTE) dramatically, dropping from
  a median of 771 days in 2018 to just 4 hours in 2024, and expected to reach zero
  in 2025. The patch paradox compounds this crisis; as vulnerabilities are disclosed,
  AI can weaponize fixes almost instantaneously, leaving organizations vulnerable
  for 99.9% of a vulnerability's lifecycle. This systemic failure, rooted in misaligned
  economic incentives, necessitates urgent re-evaluation of cybersecurity strategies
  for businesses and governments. Immediate, real-time vulnerability response is now
  essential to mitigate existential risks to critical digital infrastructure.
link: https://zerodayclock.com/collapse
tags:
- exploit development
- software vulnerabilities
- cybersecurity
- AI and hacking
- economic incentives in tech
title: The Collapse — Zero Day Clock
---

# The Collapse

Twenty years of warnings. Every one ignored.

2001

## The Economics Problem

Cambridge professor Ross Anderson published a paper that should have changed everything. Cybersecurity isn't failing because of bad technology. It's failing because of bad incentives.

The people who build insecure software don't pay when it gets hacked. The costs land on the wrong people — a textbook economic externality, no different from a factory polluting a river it doesn't drink from.

An attacker only needs to find one way in. A defender must guard every possible entry. The search space is simply too vast for any defender to cover completely.

> “Information insecurity is at least as much due to perverse incentives as it is due to technical problems.”
>
> — Ross Anderson, University of Cambridge

[Read the paper →](https://www.acsac.org/2001/papers/110.pdf)

2004

## The Patch Paradox

Halvar Flake built BinDiff — a tool that could compare a program before and after a security fix and automatically reveal how to exploit the flaw. Every security patch was simultaneously an exploit blueprint.

The entire model of "responsible disclosure" contained a fatal contradiction. The fix itself told attackers exactly where to look.

When AI enters this equation — able to read, compare, and weaponize a patch in minutes — the disclosure model doesn't just weaken. It inverts.

> “The patch is the advisory.”
>
> — Thomas Dullien (Halvar Flake)

2007

## Market for Lemons

Bruce Schneier connected cybersecurity to Nobel Prize-winning economics. When buyers can't judge quality, bad products drive good ones out. The less-secure product is always cheaper, ships faster, and has more features. The insecure product wins. Every time.

No industry in 150 years — not aviation, not automotive, not pharmaceuticals — has fixed this voluntarily. It took regulation and liability.

> “The more-secure product will be more expensive, later to market, and have fewer features. It's going to lose.”
>
> — Bruce Schneier, Harvard Kennedy School

[Read the essay →](https://www.schneier.com/blog/archives/2007/04/a_security_mark.html)

2016

## Machines Start Hacking

DARPA staged the first all-machine hacking tournament. Seven autonomous systems attacked and defended simultaneously — finding flaws, writing exploits, and generating patches in real time. No humans touching keyboards.

The winner, Mayhem, then competed against human hackers at DEF CON. The first time a machine had ever played.

> “This first step is about lighting a spark, igniting an automation revolution.”
>
> — Mike Walker, DARPA Program Manager

2018Median TTE: 771 days

## AI Village

Ariel Herbert-Voss co-founded the AI Village at DEF CON — the first permanent community dedicated to studying how AI and hacking would converge. At the time, the intersection of machine learning and cybersecurity was a niche curiosity. Most researchers worked on one or the other, never both.

The AI Village gave offensive security researchers and AI researchers a shared space for the first time. Within years it would become the proving ground for every major AI-security development — from adversarial attacks on ML models to autonomous exploit generation.

Our data begins here. The median time from CVE disclosure to first observed exploit: 771 days. Over two years. Defenders had time. But the clock was already accelerating.

2021Median TTE: 84 days

## The Acceleration

By 2021, the median time-to-exploit had collapsed from 771 days to 84 days — a 9x compression in three years. The exponential decay was unmistakable.

Log4Shell hit in December: a critical flaw in a Java logging library used by hundreds of millions of systems. Exploitation began within hours of disclosure. Patch deployment took months. The gap between attack speed and defense speed was widening, not narrowing.

2023Median TTE: 6 days

## Five Days

The median time-to-exploit collapsed to 6.36 days. Down from 771 days in just five years. Over 70% of exploited flaws were now zero-days — weaponized before or on the day of disclosure.

Palo Alto Networks discovered the disclosure system itself had inverted: 80% of public exploits appeared before the official advisory was published. On average, 23 days before.

The system designed to warn defenders was arriving after the attack.

[Unit 42 research →](https://unit42.paloaltonetworks.com/state-of-exploit-development/)

2024Median TTE: 4 hours

## AI Writes Exploits

Daniel Kang gave GPT-4 real descriptions of known software flaws and told it to exploit them autonomously. Success rate: 87%. Cost per exploit: $8.80. Every other AI model scored zero. Every commercial security scanner scored zero.

He then showed AI agent teams could discover and exploit previously unknown flaws — zero-days — working collaboratively without human guidance.

> “Many people underestimate the trends in AI — both in terms of ability and cost.”
>
> — Daniel Kang, University of Illinois

[Read the paper →](https://arxiv.org/abs/2404.08144)

2024Median TTE: 4 hours

## First AI Zero-Day

Google's Big Sleep — Project Zero and DeepMind combined — independently discovered a critical flaw in SQLite, one of the most widely deployed databases in the world. An AI found it before any human defender did.

> “This is the first public example of an AI agent finding a previously unknown exploitable memory-safety issue in widely used real-world software.”
>
> — Google Project Zero, November 2024

[Read the blog post →](https://googleprojectzero.blogspot.com/2024/10/from-naptime-to-big-sleep.html)

2025Median TTE: zero-day

## Singularity Warning

Three of the most respected voices in cybersecurity — Bruce Schneier of Harvard, Heather Adkins of Google, and Gadi Evron of Knostic — arrived at the same conclusion independently, from different vantage points, and published a joint essay with an unprecedented warning.

Their argument was precise: AI systems can now discover vulnerabilities, write exploits, and launch attacks faster than any human defender can respond. The feedback loop that makes AI effective — try, fail, learn, try again — is orders of magnitude cheaper and faster in offense than in defense. An attacker gets instant, binary feedback: did the exploit work? A defender gets noise, ambiguity, and months of uncertainty.

This asymmetry means the gap between offense and defense isn't closing. It's accelerating. AI makes attackers better, faster, and cheaper at a rate that defenders cannot match with the same technology. The two sides are not on equal footing — and they never will be, as long as the economics of software remain unchanged.

Months earlier, Adkins and Evron had put it more bluntly: the attackers have already entered their AI singularity moment. The defenders' hasn't begun. VulnCheck reported that 28.3% of exploited vulnerabilities were now weaponized within 24 hours of disclosure. Nearly one in three.

> “We're potentially looking at a singularity event for cyber attackers.”
>
> — Schneier, Adkins & Evron, October 2025

> “The attackers' AI singularity has arrived. Ours has not yet begun.”
>
> — Adkins & Evron, August 2025

[Read the essay →](https://www.schneier.com/essays/archives/2025/10/autonomous-ai-hacking-and-the-future-of-cybersecurity.html)

2025Median TTE: zero-day

## Verifier's Law

Sergej Epp explained why AI accelerates offense faster than defense. The answer: verification asymmetry.

In offense, feedback is binary and instant: did the exploit succeed? The AI learns at machine speed. In defense, feedback is ambiguous, slow, expensive. Is this alert real? Is this system secure? The signal is noisy. The learning loop is broken.

> “AI capability scales with the cheapness of verification. Offense has the cheapest verifier in cybersecurity.”
>
> — Sergej Epp (Sysdig)

[Read the framework →](https://sergejepp.substack.com/p/winning-the-ai-cyber-race-verifiability)

2025Median TTE: zero-day

## AI Beats Professionals

Stanford and Carnegie Mellon ran the first rigorous head-to-head: AI agents versus certified human penetration testers on a live enterprise network — 8,000 machines, 12 subnets, real defenses.

ARTEMIS placed second overall, outperforming 9 of 10 human professionals. Cost: $18/hour vs $60/hour for a human. The AI never sleeps.

[Read the paper →](https://arxiv.org/abs/2512.09882)

2026Median TTE: zero-day

## 500 Bugs. Decades Undetected.

Anthropic announced that its AI system Claude had found over 500 high-severity vulnerabilities in widely used open-source software — bugs that had survived decades of expert human review and millions of hours of automated testing.

The standard industry practice gives vendors 90 days to fix a reported flaw before it's made public. Anthropic's red team warned this timeline may not survive the speed and volume of AI-discovered bugs. When a single AI can find hundreds of critical flaws in a matter of days, the entire coordinated disclosure model begins to break.

> “Industry-standard 90-day disclosure windows may not hold up against the speed and volume of LLM-discovered bugs.”
>
> — Anthropic Frontier Red Team, February 2026

[Read the announcement →](https://www.anthropic.com/news/claude-code-security)

2026Median TTE: zero-day

## Industrialization

Sean Heelan built AI agents that generated over 40 working exploits for a single flaw — bypassing address randomization, control-flow protection, hardware security, and sandboxes. Cost: $50.

Yaron Dinkin and Eyal Kraft unleashed AI agent swarms on Windows kernel drivers. In 30 days, for $600 total, they found over 100 exploitable vulnerabilities across AMD, Intel, NVIDIA, Dell, Lenovo, and IBM. Cost per bug: $4.

> “The limiting factor on a state's ability to develop exploits is going to be their token throughput — not the number of hackers they employ.”
>
> — Sean Heelan, January 2026

[Read the full post →](https://sean.heelan.io/2026/01/18/on-the-coming-industrialisation-of-exploit-generation-with-llms/)

Now

## The Math

The data tells a simple story. In 2018, the median time from a vulnerability being disclosed to the first observed exploit was 771 days. Organizations had over two years to patch. By 2023 that window was 6 days. By 2024 it was 4 hours. In 2025, the majority of exploited vulnerabilities were weaponized before they were even publicly disclosed.

The data fits an exponential decay curve. This is not a trend that stabilizes. It is a collapse.

771 d

Median TTE in 2018

4 h

Median TTE in 2024

0 d

Median TTE in 2025

majority exploited before disclosure

Here is the systemic problem. When a software vendor releases a security patch, AI can now reverse-engineer that patch, identify the vulnerability it fixes, and generate a working weaponized exploit in minutes. Attacks can begin propagating across the world within hours. But organizations need an average of 20 days to test and deploy that same patch.

The act of fixing a vulnerability now accelerates its exploitation. The defense creates the offense. And the offense arrives weeks before the defense can finish deploying.

< 1h

Exploit created

< 24h

Attacks begin

~20 d

Median patch time

Organizations are exposed for 99.9% of the vulnerability lifecycle. Monthly patch cycles become theater.

This is not a technical problem that better tools can solve. It is a structural failure that affects every layer of modern society.

#### For Organizations

Every software update is now a race against automated exploit generation. Patch windows measured in days are obsolete. Real-time vulnerability response becomes a survival requirement, not a luxury.

#### For Governments

Critical infrastructure — power grids, water systems, hospitals — runs on software with known flaws that take weeks to patch. State-sponsored attackers with AI can weaponize any disclosed vulnerability faster than any government can deploy a fix.

#### For Society

The economic incentives that made software insecure for 25 years now compound with AI that makes exploitation instant and free. This is a systemic risk to the digital infrastructure civilization depends on.

[Read the Call to Action →](https://zerodayclock.com/call-to-action)
