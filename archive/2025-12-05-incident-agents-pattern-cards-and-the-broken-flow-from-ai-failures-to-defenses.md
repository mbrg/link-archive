---
date: '2025-12-05'
description: Jason Stanley discusses the evolution of incident response in AI systems,
  emphasizing the need for a structured flow from incident detection to pattern formation
  and defense mechanisms. Central to his argument is the introduction of incident
  agents like Zenity's, which correlate and contextualize incidents, transforming
  them into narratives. This approach aims to move beyond reactive measures, fostering
  a robust learning loop that connects incidents, patterns, and automated testing
  to enhance AI resilience. The implication is a shift towards treating AI behaviors
  as trajectories, enabling organizations to fortify defenses more proactively while
  improving overall security posture.
link: https://jasonstanley.substack.com/p/incident-agents-pattern-cards-and
tags:
- Incident Agents
- Security Operations
- Automated Testing
- Pattern Recognition
- AI Incident Management
title: Incident Agents, Pattern Cards, and the Broken Flow from AI Failures to Defenses
---

[![Jason Stanley](https://substackcdn.com/image/fetch/$s_!WPry!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F255c8f5b-e7e6-4fe8-9439-59976d63edb8_336x336.png)](https://jasonstanley.substack.com/)

# [Jason Stanley](https://jasonstanley.substack.com/)

SubscribeSign in

![User's avatar](https://substackcdn.com/image/fetch/$s_!n5O6!,w_64,h_64,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2062ce0c-c956-4be6-8e0c-2ff8bb616838_198x198.png)

Discover more from Jason Stanley

Writings on technology

Subscribe

By subscribing, I agree to Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

Already have an account? Sign in

# Incident Agents, Pattern Cards, and the Broken Flow from AI Failures to Defenses

### Building a flow from AI incidents to pattern cards to test harnesses, so defences evolve with how agents actually fail

[![Jason Stanley's avatar](https://substackcdn.com/image/fetch/$s_!n5O6!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2062ce0c-c956-4be6-8e0c-2ff8bb616838_198x198.png)](https://substack.com/@jasonstanley)

[Jason Stanley](https://substack.com/@jasonstanley)

Dec 05, 2025

Share

[![](https://substackcdn.com/image/fetch/$s_!q5Ir!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7acedbcb-1d14-4acf-82bf-3fbf84188c96_2560x2564.jpeg)](https://substackcdn.com/image/fetch/$s_!q5Ir!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7acedbcb-1d14-4acf-82bf-3fbf84188c96_2560x2564.jpeg) Piet Mondrian’s _Broadway Boogie Woogie_, a city of signals and intersecting flows, a visual echo of incident rivers, agent trajectories, and the structure we’re trying to build on top of them.

In most large organizations, inbound security incidents take river-like form, the volume and power of current almost overwhelming.

Alerts arrive from log pipelines, cloud platforms, security tools, application health checks, and increasingly AI systems. Analysts sit at the bank of that river grabbing whatever floats closest: an unusual sequence of tool calls from a support copilot, a burst of failed authentications, a spike in file access from a new agent. Each item is handled locally. Today, little of that work accumulates into a broader view of how the river itself is changing.

[Zenity’s recent Incident Intelligence Agent release](https://zenity.io/company-overview/newsroom/company-news/zenity-expands-ai-security-with-incident-intelligence-agentic-browser-support-and-new-open) is aimed at this seam. Their incident agent sits between raw AI-related detections and the people who have to make sense of them. It correlates posture findings, runtime anomalies, identity relationships and agent telemetry, then presents ‘Issues’ that tell a story: what happened, why, and what was affected.

That is interesting on its own. But what matters more for me is the class of problem it points at: the flow from noisy incidents to durable defences. And, increasingly, what it means to reason not just about single incidents but about agent trajectories, the full sequences of steps agents take as they reason, call tools, move data, and act on our behalf.

Nothing here is an assessment of how security work happens inside any particular company. It’s a synthesis of what I see across the field.

In this piece I want to:

1. Describe what incident agents, including Zenity’s, are actually trying to do.

2. Put that work into a broader flow from one-off failure to generalized pattern and defense, and talk about why trajectories matter.

3. Sketch what it would take for incident agents to become engines for that flow (especially when paired with automated testing) rather than just slightly smarter inboxes.


* * *

## The seam we keep struggling to see clearly

In [earlier writing](https://jasonstanley.substack.com/p/sensing-and-intervening-on-systemic) I argued that we need to see AI deployments not just as individual agents, but as portfolios and ecosystems whose risks can become correlated through shared components and architectures. That was a vantage-point argument.

Here, I want to zoom in on a particular seam in the middle of the system: the place where incidents are observed, triaged and ‘fixed’, and where in theory we should also be learning general lessons.

In AI-heavy systems, that seam lies roughly between:

- the **left-hand side**, where AI workflows run, log, and occasionally fail; and

- the **right-hand side**, where guardrails, evaluation suites, and platform policies are defined and updated.


Between these two sits a noisy, human-intensive layer: incident response desks, security operations teams, reliability engineers on call.

When an AI incident comes in today, say a support agent exfiltrates more data than intended or an internal coding assistant is tricked into pulling secrets from a tool, the flow often looks like this:

1. **We see a specific incident.** Someone raises a ticket, or an alert crosses a threshold.

2. **We apply an immediate patch.** A rule is added, a prompt is tightened, a tool is temporarily disabled, a user is blocked. The patch is narrow and brittle.

3. **We notice similar incidents.** Over time, a cluster of issues starts to look like a structural weakness: a class of prompt-injection, a recurring tool misuse, a recurring data-path problem.

4. **We design a broader fix.** Engineers and safety teams propose a more general change: new tool constraints, a new review step, a stronger safety layer.

5. **We write down the pattern.** Ideally, we turn this into a reusable object: a **pattern card**, a structured description of the failure mode, triggering conditions, example traces, hypotheses about root cause, and how to test for it.

6. **We harden defences and monitoring.** Guardrails, policies, and monitors are updated so the structural issue becomes part of standard protection and evaluation.


Call this the 1 → 6 flow: from incident, to local patch, to structural pattern, to generalized defence and regression testing.

A pattern card is not just a one-off attack prompt or a script used to validate a patch. Those artefacts are local and ephemeral: they live in one sprint, in one team’s repo, pointed at one fix. A pattern card is meant to be durable and shareable. It connects:

- multiple real incidents that instantiate the same underlying pattern,

- a family of test cases, not just one prompt, and

- one or more defences that claim to address it.


If we get them right, pattern cards become the currency that connects incident handling, evaluation, and defence. Today, most organizations stop short of this. They accumulate prompts and test scripts and attack cards in ad hoc ways, but not pattern cards as first-class, reusable objects.

The result is a familiar dynamic: we get good at swatting individual incidents, but the underlying structure of risk remains hard to see and hard to act on.

* * *

## Incidents, trajectories, and why agents change the picture

There’s another dimension that makes this harder in AI systems: **agents are trajectories**.

Traditional monitoring and incident pipelines are built around relatively narrow actuators. A “thing that can go wrong” is often well-located: a packet crossing a boundary, a process spawning, a privileged API being called. The incident stream is a view of discrete events at known seams.

Agents blur this. An agent:

- reads and writes over many channels (email, documents, tickets, chats, APIs);

- chains model calls and tools together in long sequences;

- carries state and goals forward across steps;

- sometimes reflects on its own behaviour.


That sequence (the **trajectory**) is itself a form of actuation. It’s how the system does things in the world.

Most monitoring today looks at **traffic through specific openings on that trajectory**:

- input prompts at the beginning;

- tool calls in the middle;

- outputs back to users or systems at the end.


Each seam is important. But crucial information often lives in the shape of the trajectory itself: the order in which tools are called, repeated attempts to cross a policy boundary, the way an agent keeps revisiting a particular data source, the fact that a seemingly harmless instruction early in the sequence unlocks something dangerous downstream.

Incident streams are, by construction, about events. They tell us when a particular step crosses a line. In an agentic setting, what we often need to understand is the **vector**: the path through state space an agent is following. Two trajectories can pass through the same incident point (e.g., a DLP alert) with very different risk profiles because one is part of a broader pattern of probing and escalation and the other is a one-off mistake.

That means incident synthesis in AI systems has to work on **trajectories**, not just isolated detections. Clustering similar incidents is useful, but there is something novel and dangerous about the _sequences_ of activities and incidents that agents generate. Those sequences can signal risk in ways that don’t show up when we only look at single events or simple clusters.

Zenity’s incident agent is interesting partly because it is explicitly agent-centric: it treats agents, their tools, and their flows as first-class objects. That is the right direction. The harder question is whether we can extend this to the full 1 → 6 flow, where trajectories and clusters of incidents give rise to pattern cards, and pattern cards feed back into defences and automated testing.

* * *

## What incident agents are really trying to do

Zenity’s incident agent is one of several attempts to staff this seam with software, not just people.

Instead of showing analysts a raw feed of AI-related alerts, it tries to:

- **Correlate signals** that involve the same agents, tools, users or data.

- **Reconstruct narratives** of agent behaviour: what the agent was trying to do, which tools it called, how it was influenced by content or prompts.

- **Enrich context** with identity and posture information: which environment this ran in, which policies applied, which data sources were touched.

- **Surface ‘Issues’** that describe the incident in human-readable terms and support prioritization.


It’s a move from alert-as-atomic-event to incident-as-story about behaviour and intent.

Other companies are working in adjacent directions. Microsoft’s security copilots try to read across signals in their defender products and turn them into coherent investigations. Google’s security workbench does something similar on top of Chronicle and related telemetry. CrowdStrike’s assistants watch endpoint traces and identity events and propose ranked investigations. These efforts grew out of traditional security problems, but share the same mental model: the bottleneck is less about logs, more about structured stories.

Zenity’s contribution is to cast this storytelling explicitly in terms of AI agents as the primary objects: the system cares about which agents acted, how they were steered, and which shared components (models, tools, safety layers) tie multiple incidents together.

That focus matters, because AI incidents are about **behavioural patterns in high-dimensional systems**: sequences of messages, tools, context windows and partial failures. Without some way to turn those sequences into interpretable objects, the flow past step 2 (beyond local fixes) is very hard to achieve.

* * *

## The broken flow in more detail

If we zoom in on the typical flow today, a few structural breaks show up.

### From incident to structural issue

First, **incidents are not represented in a way that is easy to generalize from**.

They live as tickets, chat transcripts, terminal captures, and short internal write-ups. These artefacts are rich in local detail but poor in machine-readable structure. They rarely say, in a standardized way:

- which model or model family was involved;

- which tools and data sources were used;

- which guardrail or policy layers were in play;

- what the user or upstream system was trying to achieve;

- how the full trajectory unfolded.


Without that structure, it’s hard to see that five apparently different incidents are the same pattern expressed through different tools or workflows, or that multiple incidents are fragments of the same trajectory behaviour.

Second, **there is often no consistent owner for step 3,** the work of noticing that a cluster of incidents points to a structural issue. Sometimes this happens informally in a security operations team. Sometimes it happens in an AI platform team after a particularly painful incident. It is rarely systematic.

### From structural issue to pattern card

Even when a structural issue is recognized, the translation into reusable pattern descriptions is manual and fragile.

Teams may create:

- a one-off red-teaming scenario used in a particular evaluation sprint;

- a small internal attack card that lives in a deck or document;

- a prompt script or harness used to validate a patch in one service.


These are all valuable. But they tend to be _local_ to a team, a moment, and a system.

A **pattern card** is a step beyond that:

- It is written to be reused across systems and teams, not just in one sprint.

- It connects multiple incidents and multiple test cases that instantiate the same underlying pattern.

- It records hypotheses about mechanism and relevant surfaces, not just example prompts.

- It is structured enough that automated testing engines and guardrail systems can plug into it.


Most organizations have ingredients that _could_ be pattern cards, but they are scattered and inconsistent. So even when people do the work of recognizing a structural issue, we stop short of capturing the value in a way that future testing and defence can actually use.

### From pattern to defence

Finally, the connection between pattern and defence is often **weak in both directions**.

On one side:

- Guardrail and policy teams maintain their own configuration stores and evaluation harnesses.

- When they respond to a pattern, they might change a safety prompt, add rules to a policy engine, or extend a regression suite.


On the other side:

- Incident and IR teams often lack visibility into which structural issues are already accounted for (at some acceptable level of confidence) in defences, and which are not.

- The same pattern may be rediscovered multiple times as different teams run into it.


Part of the weakness is organizational: different teams, different tools. Cut part is representational. Without pattern cards as shared objects, ‘pattern’ lives mostly in people’s heads, and ‘defense’ lives mostly in code and configuration. The flow from incident to defense is therefore patchy and brittle.

* * *

## Incident agents as pattern distillers

If we take the 1 → 6 flow seriously, what would it mean for incident agents to play a central role?

Think of an incident agent sitting on top of three broad kinds of input:

1. **Telemetry from AI workflows** – traces of model calls, tool invocations, context windows, outcomes, and full trajectories.

2. **Signals from existing controls** – guardrail blocks, policy decisions, abuse detection, data loss alerts.

3. **Human annotations** – tickets, analyst notes, thumbs up/down, after-action reviews.


From this, it tries to produce at least three distinct outputs:

- **Incidents-as-stories** for human responders.

- **Incidents-as-structures** for pattern mining.

- **Incidents-as-training-data** for future judgment models.


Zenity’s incident agent, and similar systems, are starting to tackle the first of these. The interesting question is how to push them along the other two axes.

### 1\. From story to structure

The same machinery that builds human-readable narratives can also produce structured representations:

> Agent A, using model family M and tools T1/T2, accepted input of type X from source Y, followed trajectory τ, and produced action Z that violated policy P under conditions C.

This doesn’t require particularly difficult or novel methods. It requires discipline about **schemas** and **vocabularies** for agents, tools, policies, contexts, and trajectories that are:

- rich enough to be useful;

- stable enough to aggregate over; and

- simple enough for analysts to correct.


Once incidents have this structure, the incident agent can search for recurring shapes:

- repeated tool misuse tied to a particular data source;

- recurring failures when agents operate in a certain identity context;

- trajectories that repeatedly push against the same boundary before triggering a detection;

- patterns of manipulation coming from specific channels.


These clusters and trajectory-shapes are candidates for step 3: this is not just a one-off, this is a structural issue.

### 2\. From clusters to pattern cards

The next move is to turn these clusters into **pattern cards**, records that describe:

- the nature of the pattern (e.g., multi-step prompt injection via embedded instructions in internal docs consumed by an agentic browser);

- concrete examples (prompts, traces, configuration snippets, trajectories);

- hypotheses about underlying causes (weak separation between tool outputs and model instructions, over-broad tool scopes, missing checks);

- the surfaces where it’s likely to appear (which agents, tools, data domains, identity roles).


To be useful beyond human reading, pattern cards also need testing-specific elements:

- **Verifier or judge spec** – how we know when the pattern has succeeded in a test (rubric for a model judge, log predicates, deterministic checks).

- **Variation seeds** – templates and examples an automated engine can use to generate many concrete test instances (prompt variations, tool-call permutations, environment tweaks).

- **Target and scope metadata** – which systems, policies, and environments the pattern should be tested against.

- **Budget and metrics** – how many trials we want, which metrics matter (bypass rate, data volume, time-to-detection), and what success/failure looks like.


Now the pattern card is not just a write-up; it’s a **recipe for automated exploration**.

Given a cluster of similar incidents and trajectories, an incident agent can:

- summarize the pattern;

- extract candidate triggers and traces;

- propose initial judge criteria (e.g., this is bad if the agent returns un-redacted internal doc X to caller Y);

- suggest where in the system the pattern is likely to recur.


Humans refine the card, but the cost of going from cluster-of-incidents to machine-consumable-pattern-card drops significantly.

### 3\. From pattern cards to defences and monitors

Once we have pattern cards with this richer structure, they can drive more than manual red teaming.

We can imagine a pipeline where pattern cards are:

1. **Registered** in a patterns library, with ownership and lifecycle (draft, active, retired).

2. **Consumed by automated testing engines**, which:

   - generate variations from the pattern’s seeds;

   - run tests against target systems and environments;

   - apply the associated judge to score outcomes;

   - produce structured metrics.
3. **Summarized back to defence and monitoring teams** in terms they can act on:

   - which systems are vulnerable and how badly;

   - which monitors and guards are catching the behaviour;

   - where blind spots remain.

Only at that point, ideally, does something show up as a candidate structural issue on a defence roadmap. The value to those teams is far beyond what they get from a pile of incidents, or even from a well-written ‘Issue.’ They receive:

- quantified signal about vulnerability;

- clarity about which layers of monitoring see the problem;

- a ready-made harness they can re-run after changes.


Incident agents are natural upstream producers here. They see incidents and trajectories; they have hooks into the agent graph; they already know how to tell stories. The opportunity is to push them into structured pattern distillation and testing.

* * *

## Other shapes this could take

It’s tempting to think of an incident agent as a single assistant that reads logs and writes tickets. But, as with agents in critical systems more broadly, the architecture matters as much as the model.

A few patterns are worth calling out.

### Watchdog around legacy cores

One pattern is to treat the incident agent as a **watchdog around existing monitoring stacks**.

Traditional observability tools continue to generate alerts. The incident agent watches these alerts, plus AI telemetry, and focuses on:

- clustering them into episodes and trajectories;

- spotting inconsistencies between what different monitoring systems believe;

- proposing where human attention is most needed.


Here, the agent does not change defences directly. Its power lies in shaping attention and generating better raw material for pattern cards.

### Planner behind hard gates

Another pattern is to give the incident agent limited powers to **propose changes** (e.g., temporary policy adjustments or kill switches for specific tools) while keeping these behind hard gates.

Any action the agent proposes is checked against non-negotiable constraints:

- it cannot disable critical logging;

- it cannot relax certain access controls;

- it cannot make irreversible changes without human review.


Pattern cards and automated test results can be part of the evidence presented at those gates.

### Parallel lenses and structured disagreement

A third pattern is to run multiple lenses in parallel:

- a rule-based system grounded in known indicators;

- a statistics-heavy system focused on unusual behaviour;

- a language-heavy system (the incident agent) focused on narratives, semantics, and trajectories.


Instead of merging them into a single view, the system treats **disagreement between lenses as a primary signal**: if one layer sees a serious story and the others are quiet, that is a reason to slow down and look carefully.

This can make the seam more robust, especially while we’re still learning where AI incidents will cluster.

* * *

## Where should we go from here?

Zenity’s incident agent, and its peers in other ecosystems, already improve the **front end** of the flow: they reduce noise, enrich context, and make incidents more legible.

The question is how to extend this into a **full loop**:

1. **Incidents → structured trajectories**

   - Invest in schemas and vocabularies that let incident agents represent agent trajectories and contexts in machine-readable form.

   - Treat the trajectory, not just the alert, as a first-class object.
2. **Trajectories → pattern cards**

   - Use incident agents to propose draft pattern cards tying together clusters of incidents and trajectory shapes.

   - Standardize what a pattern card must contain for humans and automated testing: description, examples, surfaces, judge spec, variation seeds, targets, budgets, metrics.
3. **Pattern cards → automated testing**

   - Build or adopt engines that ingest pattern cards and turn them into structured test campaigns, with clear metrics and budget control.

   - Before anything goes to defence and monitoring teams for fixing, run at least a lightweight automated test pass to understand how vulnerable systems and monitors really are.
4. **Testing → defences and monitors**

   - Present defence teams not just with observed incidents, but with structured inputs and insights on system and monitor behaviour under this pattern.

   - Capture resulting changes (e.g., new guardrails, policies, monitors) as linked artefacts in the same pattern card.
5. **Defenses → incident understanding**

   - Feed defence changes back into the incident agent’s view: it should know which patterns are known, which mitigations exist, and where to look for residual risk (though obviously without assuming that ‘known’ issues are in fact solved).

   - Use gaps between what should be mitigated, on the one hand, and what we still see in the river, on the other hand, as drivers for further investigation.

Incident agents, in this picture, aren’t just summarizers. They are **pattern distillers** at the center of a loop that runs from real-world failures through testing into defences, and back again.

* * *

We are in an awkward phase. Enterprises are deploying AI agents faster than they can fully see them. Guardrail teams are working hard on policy and evaluation, often a couple of organizational hops away from the desks where the most interesting failures appear. Incident response teams are dealing with noisy rivers of events and have limited time to turn local firefighting into structural learning.

Incident agents like Zenity’s don’t solve this on their own. But they gesture at a useful re-framing:

- Incidents are not just items to be closed. They are raw material for patterns.

- Patterns are not just curiosities. They are the backbone of evaluation and defence.

- Agents are trajectories, not just endpoints, and trajectories carry signals we can’t see if we only look at seams.

- The seam between incident handling and guardrail and defence design needs its own tools, schemas, and architectures.


If we design incident agents as pattern distillers and flow enablers and pair them with automated testing pipelines, we get closer to a world where AI systems move beyond graceful failure in the moment to helping us harden the structures they depend on. And hopefully soon learning to do this hardening on their own.

* * *

#### Subscribe to Jason Stanley

Launched 7 days ago

Writings on technology

Subscribe

By subscribing, I agree to Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

Share

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

TopLatest

[Internal Representations as a Governance Surface for AI](https://jasonstanley.substack.com/p/internal-representations-as-a-governance)

[Logit Steering, Sparse Autoencoders, and the Future of Enterprise AI Control](https://jasonstanley.substack.com/p/internal-representations-as-a-governance)

Nov 28•
[Jason Stanley](https://substack.com/@jasonstanley)

2

![](https://substackcdn.com/image/fetch/$s_!_kGt!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8892d2e2-986d-4a27-aedb-e61f81891f9e_894x524.jpeg)

[Sensing and Intervening on Systemic Risk in AI](https://jasonstanley.substack.com/p/sensing-and-intervening-on-systemic)

[How finance, aviation and cyber manage correlated exposures and what that implies for AI control planes and oversight](https://jasonstanley.substack.com/p/sensing-and-intervening-on-systemic)

Nov 30•
[Jason Stanley](https://substack.com/@jasonstanley)

2

![](https://substackcdn.com/image/fetch/$s_!D8h_!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fffdae530-218b-4873-a2ac-84804704044a_2560x2023.jpeg)

[Patterns for Agents in Critical Systems](https://jasonstanley.substack.com/p/patterns-for-agents-in-critical-systems)

[Design patterns for mixing deterministic cores, surrogate engines, and reasoning models. And how each shifts governance and security.](https://jasonstanley.substack.com/p/patterns-for-agents-in-critical-systems)

Dec 3•
[Jason Stanley](https://substack.com/@jasonstanley)

![](https://substackcdn.com/image/fetch/$s_!8xQ6!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F625af912-16bd-4139-8bc3-9c5ebbc9ee78_1060x754.jpeg)

See all

### Ready for more?

Subscribe
