---
date: '2026-01-06'
description: 'Jason Stanley''s recent analysis reveals critical insights regarding
  the assessment of AI systems in enterprises, emphasizing the need for dual scorecards:
  one for value and another for resilience under stress. Recent artifacts, IDEsaster
  and OpenAI''s Atlas, highlight vulnerabilities in AI-augmented tools stemming from
  auto-approved actions and untrusted inputs. Stanley advocates for structured evaluation
  of failure pathways (S3/S4) to effectively manage risk while leveraging AI''s capabilities.
  Key recommendations include continuous discovery for risk mitigation and establishing
  comprehensive testing protocols to ensure the functionality and security of autonomous
  systems.'
link: https://jasonstanley.substack.com/p/what-idesaster-and-atlas-reveal-about
tags:
- AI risk management
- enterprise AI
- security assessments
- performance evaluation
- continuous improvement
title: What IDEsaster and Atlas reveal about tail risks, autonomy creep, and risk
  budgets
---

[![Jason Stanley](https://substackcdn.com/image/fetch/$s_!WBso!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1162034d-20cd-4661-9ea0-ecbacfa986ba_1251x1251.png)](https://jasonstanley.substack.com/)

# [Jason Stanley](https://jasonstanley.substack.com/)

SubscribeSign in

![User's avatar](https://substackcdn.com/image/fetch/$s_!n5O6!,w_64,h_64,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2062ce0c-c956-4be6-8e0c-2ff8bb616838_198x198.png)

Discover more from Jason Stanley

Deep, practical writing on agent security, system-level evaluation, and portfolio/systemic risk from real deployments — patterns, failures, and architectures that actually hold up in real organizations. New writing several times per week.

Subscribe

By subscribing, I agree to Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

Already have an account? Sign in

# What IDEsaster and Atlas reveal about tail risks, autonomy creep, and risk budgets

### Continuous hardening, loss evidence, and why average-case eval no longer explains risk

[![Jason Stanley's avatar](https://substackcdn.com/image/fetch/$s_!n5O6!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2062ce0c-c956-4be6-8e0c-2ff8bb616838_198x198.png)](https://substack.com/@jasonstanley)

[Jason Stanley](https://substack.com/@jasonstanley)

Jan 05, 2026

1

1

Share

[![A lone figure stands on a rocky peak looking over a fog-filled landscape.](https://substackcdn.com/image/fetch/$s_!lMP6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd351ec34-7a2c-4ae6-9674-f7ba53131974_1280x1642.jpeg)](https://substackcdn.com/image/fetch/$s_!lMP6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd351ec34-7a2c-4ae6-9674-f7ba53131974_1280x1642.jpeg) Caspar David Friedrich, _Wanderer above the Sea of Fog_, 1818\. One of the most emblematic works of the Romantic era. Landscape as sublime; but what lurks below in that fog?

In December, two evaluation artifacts were released that should change how enterprise leaders think about marshalling information about performance and risk. [IDEsaster](https://maccarita.com/posts/idesaster/) documented a wide set of vulnerabilities across popular AI-augmented developer tools, showing how prompt injection can chain with ordinary IDE capabilities and auto-approved agent behaviors into high-impact outcomes. At the same time, OpenAI described how it is [continuously hardening its Atlas browser agent against prompt injection](https://openai.com/index/hardening-atlas-against-prompt-injection/), explicitly treating it as an ongoing operational problem rather than a punctual exercise.

The point here is not that security matters. Of course it does. Instead, it is that both stories are about the same systems pattern: a model that **ingests untrusted content** as part of normal operation and has the ability to **take actions that matter**. In that world, evaluation has two jobs. Yes, you need to prove that the system is useful on intended workflows; but you also need to prove that the high-severity failure modes are bounded, detectable, and survivable.

Recently, a friend who works in large-scale credit investing gave me a useful way to describe the structure. In credit, base-case analysis is necessary, but it isn’t sufficient. You can’t make a serious risk-acceptance decision if you don’t understand the tails: pathways to default, size of losses when things go wrong, the conditions under which failures become correlated. The discipline here is in separating the work that estimates value from the work that characterizes loss, and in making the tradeoff explicit.

Enterprise AI needs an equivalent split because agents force us to decide what we are willing to tolerate once the system can read untrusted content and change states in consequential ways.

I’ll ground my discussion here in two common enterprise deployments:

1. An internal RAG-based AI assistant working over sensitive HR/legal/engineering documents; and

2. A tool-use agent that can write to a system-of-record.


My goal is to highlight the need for a distinct second evaluation scorecard built around high-severity tails, plus a method for deciding which tails are worth testing in the first place.

* * *

## What IDEsaster and Atlas actually taught us

#### IDEsaster: auto-approved actions plus platform side effects

IDEsaster is best read as a systems paper disguised as a roundup of vulnerabilities. Its core message isn’t really that any specific vendors are sloppy. Instead, it is that when you add an agent to a platform that was designed for humans, new exploit chains can be created.

Two patterns are especially relevant to enterprise agents.

**1) Auto-approved writes are a privileged channel.**

Many AI-enhanced IDE workflows auto-approve certain actions for usability (e.g., edits inside the workspace). IDEsaster shows how an attacker can exploit that design choice by injecting instructions that cause the agent to write to sensitive configuration surfaces (workspace settings, task definitions, metadata) or to modify files whose execution is triggered by normal IDE behavior. The important takeaway is not the exact file type, but the principle that, if an agent can write without a human decision point, the write path becomes a privileged control plane.

**2) Normal platform behavior becomes an exfiltration primitive.**

IDEsaster also highlights cases where seemingly benign platform behaviors (e.g., automatically fetching a referenced schema) become outbound channels when an agent can generate the inputs that trigger those behaviors. Again, don’t fixate on schemas here. Instead, look at the pattern: the agent doesn’t need an explicit tool designed to send data to attacker if the surrounding platform can be induced to do it indirectly.

Enterprises have the same class of side effects all over the place: previewers that fetch remote resources, link unfurlers, webhook retries, connectors that enrich data by calling third-party endpoints, audit pipelines that export traces, and so on. Agents increase the chance that you’ll accidentally wire those side effects into a chain.

#### Atlas: untrusted content as permanent condition

OpenAI’s Atlas hardening post is valuable because it is explicit about the operating environment. A browser agent lives in an untrusted world by default. It reads pages, emails, shared docs, and attachments that can contain adversarial instructions. In that environment, prompt injection isn’t a bug you remove but instead a pressure you continuously manage.

More important than the threat model is the posture: OpenAI describes automated red teaming uncovering new injection strategies, shipping mitigations, and using training approaches to strengthen the agent against those attacks over time. The defense strategy is continuous discovery feeding continuous hardening.

Put the two artifacts together and you get a concrete enterprise lesson:

- IDEsaster shows how auto-approved actions and platform side effects create exploit chains when an agent is present.

- Atlas shows that once untrusted content is part of the environment, the only stable posture is continuous discovery and hardening.


That combination is the practical justification for a second scorecard. It’s not enough to ask whether an agent is good enough at a task or family of tasks. We also need to ask whether the agent holds under the kinds of stresses that can emerge at the boundary between untrusted inputs, agentic interpretation, and privileged actions.

* * *

## From one scorecard to two

Most enterprise AI programs already run a ‘value’ scorecard. They test functional performance on representative workflows: accuracy, completeness, hallucination rates, retrieval relevance, latency, cost. They run regressions across model and prompt changes. They do staged rollouts. They measure satisfaction and productivity outcomes. This work is essential. It’s how product progress is made visible.

The gap is that value evidence and loss evidence are often mixed implicitly rather than organized explicitly. Teams do some security testing, some safety checks, and some incident review, but the evidence is not consistently built to answer the question decision makers actually face: given this blast radius, what are the high-severity failure pathways we care about, how often do they appear under stress, and what controls bound them?

At some level, value and risk can be traded off. Organizations do this all the time. The problem is not that you can’t or shouldn’t do this kind of trade off or summary evaluation. The problem is that you can’t make a serious risk-acceptance decision if your evaluation mostly describes the middle of the distribution while leaving the tails vague, or if the implemented mitigations are mere promises rather than verifiable properties. You cannot decide what you are willing to tolerate if you cannot see what you are tolerating.

So we should run two scorecards that answer different questions:

- **Scorecard 1 (Prove value)** asks: when used as intended, does the system deliver the promised productivity and quality gains?

- **Scorecard 2 (Prove it holds under stress)** asks: under attack, under ambiguity, and under degraded dependencies, do the worst failures stay inside an acceptable blast radius. Can we detect and recover when they do not?


To keep this legible across product, engineering, security, and risk leadership, it helps to use a simple severity ladder:

- **S4:** security/compliance breach, unauthorized data access or exfiltration, irreversible harmful action

- **S3:** corruption of a system-of-record, materially wrong action with substantial customer/financial impact

- **S2:** repeated workflow failure causing operational disruption and escalations

- **S1:** low-impact errors caught by users


This ladder helps make the problem discussable. It allows different stakeholders and teams to align on which failure types are more critical than others, what testing should exist for different types of failure modes, and what trade offs are acceptable for different kinds of failure types.

* * *

## Example 1: internal RAG over sensitive documents

Consider an internal retrieval-augmented assistant that answers questions over HR policies, legal guidance, engineering runbooks, and incident postmortems.

Scorecard 1 (Prove value) is fairly straightforward: build a representative query set, measure retrieval coverage and citation correctness, assess answer accuracy and completeness, track latency and cost, iterate.

Scorecard 2 (Prove it holds under stress) pushes us to evaluate different seams. A few illustrative failure modes worth testing (not exhaustive):

1. **Boundary-crossing exposure (S4).**

The assistant reveals restricted content, discloses the existence of confidential documents, or reconstructs sensitive information across user or role boundaries.

2. **Mis-evidencing via citations (S3–S4 depending on domain).**

The assistant cites something that looks authoritative but is out of date, mis-scoped, or irrelevant, producing a confident answer that sounds authoritative while being wrong in a consequential way.

3. **Confident synthesis under high-stakes ambiguity (often S3).**

Questions like ‘Can I share this data externally?’ or ‘Does this exception apply?’ are conditional and context-sensitive. Optimizing on known-answer queries trains the system toward fluency, not toward safe abstention and escalation when qualifiers are missing.

4. **Untrusted-content injection inside the corpus (S4).**

Untrusted content isn’t only external web pages. It includes vendor documents, pasted logs, shared wikis, or compromised internal content. If injected instructions can influence retrieval or synthesis behavior, you have a tail pathway that typical functional benchmarks won’t expose.

5. **Access control implemented at the wrong layer (S4).**

If permissions are not enforced below retrieval (if you effectively ask the model to behave like an ACL) you will get a system that is usually fine but is not bounded.


These are just a starting set. A serious evaluation would go deeper: identity lifecycle edge cases (role changes, termination), retention/deletion behavior, multi-tenant boundaries, audit and forensics, incident response drills, and systematic measurement of reconstruction risk. The point here is methodological: Scorecard 2 (Holds under stress) evaluation is about seams (boundaries, ambiguity, untrusted content), and seams are rarely captured by representative test sets.

* * *

## Example 2: a tool-using agent that writes to a system-of-record

Now consider an agent that can create or modify records in a system-of-record: open and close tickets, update fields, trigger refunds, change entitlements, launch workflows through tools and APIs.

Scorecard 1 (Prove value) is again approachable: measure end-to-end task success on typical cases, correct routing and extraction, time-to-resolution improvements, human-assist rate, cost, and satisfaction.

Scorecard 2 (Holds under stress) is where enterprise risk concentrates. A few illustrative failure modes worth testing (again, not exhaustive):

1. **Degraded dependencies causing unsafe writes (S3).**

Timeouts, partial writes, state drift, retries, race conditions, and backpressure can cause duplicate actions or inconsistent records (double refund, wrong closure, incorrect entitlement). These are distributed-systems realities, not adversarial edge cases.

2. **Policy violations under pressure (S3–S4).**

Users request exceptions; some are benign, some manipulative. The evaluation question is not whether the agent follows policy when asked in a standard way. It is whether the agent (including the enforcement layer, which could even include human intervention) holds the line when pressured, confused, or adversarially phrased.

3. **Injection through untrusted user text and tool outputs (S4).**

Tickets, emails, and chat transcripts are untrusted inputs. Tool responses can also be a channel. The key question is whether injected instructions can influence the agent’s action selection in ways that bypass controls.

4. **Auto-approved actions and chainability (S4).**

IDEsaster’s lesson generalizes: when you combine auto-approved actions, untrusted inputs, and platform side effects, you create exploit chains. In enterprise terms: auto-approved writes with broad tool scopes and connectors that amplify side effects are a recipe for tail risk.

5. **Control-plane failure: least privilege and approvals are advisory (S4).**

If approval gates can be bypassed by prompt manipulation, or if tool scopes are broad for convenience, you do not have a bounded system, even if the agent performs well in typical cases.


A serious evaluation for this use case would be more comprehensive: auditability and reversibility guarantees, compensating transactions, multi-step workflows with interruption, cross-system invariants (e.g., ticket state must match entitlement state), abuse-rate estimation, and fleet-level anomaly detection. The point is the same: once the system can write, you need evidence about tails and controls, not only about median task quality.

* * *

## How do we decide what failures are worth testing?

Test the tails is easy to say and hard to execute because the space is enormous. The hard question is not whether we can think up bad cases worth testing, but how to identify the most important failure modes worth spending our limited testing and monitoring budget on to get the right information for decision makers?

Security has a mature answer here: threat modeling. You identify assets, trust boundaries, entry points, attacker capabilities, and plausible goals; you prioritize scenarios by impact and feasibility. You don’t get completeness, but you do get a defensible selection of high-value tests.

For non-adversarial robustness (ambiguity, messy inputs, degraded dependencies) most organizations lack an equivalent practice. Teams often rely on informal brainstorming or ad hoc bug lists. That helps, but it won’t reliably surface the failure modes that dominate enterprise pain: cascade conditions, state inconsistencies, data lifecycle edge cases, and failure correlations across shared infrastructure.

A practical path forward is to treat non-adversarial robustness as a hazards discipline: systematic identification of where ambiguity and partial failure can create high-severity outcomes. In practice, that usually means combining three inputs:

- **System decomposition:** enumerate interfaces where partial failure, ambiguity, and state drift can arise (retrieval, identity, tool gateways, state transitions, human approval loops).

- **Operational learning:** mine near-misses and incidents for recurring patterns and precursors; treat almost-happened as first-class signal.

- **Stress design:** deliberately simulate degradations you know will occur (timeouts, partial writes, stale state, rate limits, corrupted inputs) and ask which could plausibly drive S3/S4 outcomes at your current blast radius.


This won’t produce a perfect taxonomy. But it produces something many teams lack today: a repeatable method for deciding what goes into the holds-under-stress scorecard, and a defensible story for risk leaders about why you’re testing what you’re testing.

* * *

## How to operationalize two scorecards

The fix is not to simply do more red teaming, but to connect value evidence and failure evidence to explicit shipping and scaling decisions, and to make the process cumulative and repeatable.

### Step 1: Name the blast radius

A read-only assistant over non-sensitive content is not the same risk object as a write-capable agent touching systems-of-record. A pilot is not the same as broad rollout. Define posture in plain terms: what can it read, what can it write, and how many users or records are in scope.

### Step 2: Adopt a decision rule with constraints

Maximize utility subject to constraints on high-severity loss. You can accept some S1/S2 failure if it is bounded and improves quickly, but you should not expand blast radius with uncontrolled S3/S4 pathways just because the median is impressive.

Use the severity ladder as a shared language:

- **S4:** security/compliance breach, unauthorized data access or exfiltration, irreversible harmful action

- **S3:** corruption of a system-of-record, materially wrong action with substantial customer/financial impact

- **S2:** repeated workflow failure causing operational disruption and escalations

- **S1:** low-impact errors caught by users


### Step 3: Build a cumulative loss suite

Keep the base-case suite. Add a loss suite designed specifically to find S3/S4 pathways. Every discovered failure mode becomes a regression test that runs on every meaningful change (model updates, prompt changes, retrieval changes, tool changes).

For RAG systems, loss suites include cross-boundary probes, adversarial content in the corpus, reconstruction attempts, and “should refuse / should escalate” ambiguity cases. For write-capable agents, loss suites include degraded-tool simulations (timeouts, retries, partial writes), state drift, boundary-pressure prompts, and tests that validate approvals cannot be bypassed.

The other ingredient is to make the downside program living rather than episodic. Atlas is instructive here: OpenAI describes a compounding loop of automated attack discovery, rapid mitigations, and continuously tightening defenses. Enterprises do not need to copy the exact methods to copy the posture: exploratory discovery should continuously feed regression testing, and telemetry should continuously generate new test cases.

Here’s a starter list for how to move towards a living eval suite:

1. Seed the suite with known high-severity families: injection/exfil chains, ambiguity in high-stakes decisions, tool degradation and partial failure.

2. Generate variants automatically (paraphrases, tool-output poisoning, multi-step chains) so the suite does not overfit to a single phrasing.

3. Run it continuously across meaningful changes: model updates, prompt changes, retrieval changes, tool/connector changes.

4. Promote every real incident and near-miss into regression with clear reproduction steps.

5. Score outcomes by severity, detectability, and recoverability, not only pass/fail accuracy.

6. Tie rollout scope and autonomy to holds-under-stress results through explicit gates, like the risk-budget rule above.

7. Refresh deliberately: periodic reviews plus telemetry-driven additions, because attackers and environments evolve.


### Step 4: Test controls as properties, not promises

Guardrails and many defense-in-depth measures can be helpful, but they can’t be confused with controls. Controls are verifiable mechanisms: scoped privileges, tool-gateway enforcement, approvals, fail-closed defaults, logging, rollback paths. Build tests that prove these mechanisms do what they claim under adversarial conditions, degradations, environment shifts, and so on.

### Step 5: Treat fleet behavior like a portfolio

Shared infrastructure creates correlated risk. Centralize the things that reduce correlation: policy enforcement at tool gateways, anomaly detection for high-risk actions, rollout controls, and kill switches. This is the AI analogue of portfolio constraints: you are reducing the chance that one misconfiguration becomes an organization-wide incident.

### Step 6: Use an autonomy ladder and climb it deliberately

A practical way to keep the two scorecards honest is to define an autonomy ladder and require holds-under-stress evidence before you move up a rung:

- **Rung 0 (Read-only):** answer questions, retrieve documents, no side effects

- **Rung 1 (Suggest):** propose actions, human executes

- **Rung 2 (Execute with approval):** agent executes only after explicit approval for each high-impact action

- **Rung 3 (Execute within a tight envelope):** auto-execute low-impact actions inside strictly bounded privileges; escalate the rest

- **Rung 4 (Broad autonomy):** rare in enterprise; requires exceptional containment and monitoring maturity


The point is not to slow teams down. It is to make blast radius an explicit product decision and to prevent accidental autonomy creep where convenience features quietly push you up the ladder without the corresponding evidence that the system holds.

This is where the risk budget idea becomes concrete. For example:

> We will not move from Rung 2 → Rung 3 until (a) we observe zero S4 outcomes in 10,000 stress episodes, (b) approvals cannot be bypassed under adversarial prompting, (c) near-misses are explainable and trending down over successive releases, and (d) rollback paths are exercised quarterly in drills.

That doesn’t guarantee security or non-adversarial robustness, but it does put the right information on the table before autonomy is expanded.

### Step 7: Measure holds-under-stress with operational signals

You don’t need perfect probability estimates of tail events to run a serious program, but you do need repeatable signals. Examples that can to matter in enterprise settings:

- **S3/S4 rate in simulation:** how often do high-severity outcomes occur per 1,000 adversarial or stress-test episodes?

- **Near-miss rate:** how often did a control (approval gate, policy engine, tool scope) prevent a high-impact action?

- **Uncertainty behavior:** when evidence is insufficient, how often does the system abstain or escalate versus confidently acting?

- **Duplicate/unsafe action under degradation:** what happens under injected latency, timeouts, partial failures, and stale state?

- **Forensic completeness:** can you reconstruct the decision and tool sequence end-to-end for sampled episodes and real incidents?


These signals don’t replace qualitative review. They make it possible to set and enforce a risk budget (e.g., we will not expand rollout if S4 events appear in the loss suite; we will not auto-execute this class of actions until near-misses are rare and fully explained).

One small artifact ties this all together: a standardized ship memo that forces the value story and the holds-under-stress story to coexist as equals. A good memo can fit on two pages:

- **Value evidence:** what it does, where it works, what it replaces, expected benefit and cost

- **High-severity loss evidence:** what you tested in S3/S4, what failed, what remains uncertain

- **Control verification:** least privilege, approvals, fail-closed behavior, auditability, rollback

- **Rollout posture:** blast radius, monitoring signals, and explicit triggers for reducing autonomy


This format does two things. It makes it harder to ship high-autonomy systems with weak containment just because the median is impressive. And it makes it easier to scale systems that are not perfect, because leadership can see what is bounded, what is monitored, and what happens when assumptions break.

* * *

Enterprises should pursue large upside from AI. The organizations that scale that upside will be the ones that can put downside information in front of decision makers in a disciplined way, identifying the failure modes that matter, keeping the evaluation system adaptive, and expanding autonomy only when the evidence supports it.

* * *

#### Subscribe to Jason Stanley

Launched a month ago

Deep, practical writing on agent security, system-level evaluation, and portfolio/systemic risk from real deployments — patterns, failures, and architectures that actually hold up in real organizations. New writing several times per week.

Subscribe

By subscribing, I agree to Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

[![Jason Stanley's avatar](https://substackcdn.com/image/fetch/$s_!n5O6!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2062ce0c-c956-4be6-8e0c-2ff8bb616838_198x198.png)](https://substack.com/profile/8866899-jason-stanley)[![Navdeep Gill's avatar](https://substackcdn.com/image/fetch/$s_!sSJi!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F42499736-3457-42c9-9823-7daea69ca76f_496x496.jpeg)](https://substack.com/profile/2259770-navdeep-gill)

1 Like∙

[1 Restack](https://substack.com/note/p-183552148/restacks?utm_source=substack&utm_content=facepile-restacks)

1

1

Share

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

TopLatestDiscussions

[Anthropic’s Activation Oracles: Better Introspection, New Failure Modes](https://jasonstanley.substack.com/p/anthropics-activation-oracles-better)

[How to use activation narratives without mistaking legibility for causality](https://jasonstanley.substack.com/p/anthropics-activation-oracles-better)

Dec 24, 2025•[Jason Stanley](https://substack.com/@jasonstanley)

3

2

![](https://substackcdn.com/image/fetch/$s_!HVaS!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F00a295b2-d27e-4ab9-a364-a1c78b830d06_1200x900.jpeg)

[Incident Agents, Pattern Cards, and the Broken Flow from AI Failures to Defenses](https://jasonstanley.substack.com/p/incident-agents-pattern-cards-and)

[Building a flow from AI incidents to pattern cards to test harnesses, so defences evolve with how agents actually fail](https://jasonstanley.substack.com/p/incident-agents-pattern-cards-and)

Dec 5, 2025•[Jason Stanley](https://substack.com/@jasonstanley)

2

![](https://substackcdn.com/image/fetch/$s_!q5Ir!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7acedbcb-1d14-4acf-82bf-3fbf84188c96_2560x2564.jpeg)

[Internal Representations as a Governance Surface for AI](https://jasonstanley.substack.com/p/internal-representations-as-a-governance)

[Logit Steering, Sparse Autoencoders, and the Future of Enterprise AI Control](https://jasonstanley.substack.com/p/internal-representations-as-a-governance)

Nov 28, 2025•[Jason Stanley](https://substack.com/@jasonstanley)

3

![](https://substackcdn.com/image/fetch/$s_!_kGt!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8892d2e2-986d-4a27-aedb-e61f81891f9e_894x524.jpeg)

See all

### Ready for more?

Subscribe
