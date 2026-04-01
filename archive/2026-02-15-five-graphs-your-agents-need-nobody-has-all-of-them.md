---
date: '2026-02-15'
description: 'Jason Stanley outlines a critical approach to agent governance as a
  graph composition challenge. He identifies five essential graph types: Access, Security,
  Context, Action, and Knowledge graphs, each answering specific governance questions
  but insufficient individually. The composition of these graphs is necessary for
  coherent governance, addressing the complexities of control within agent operations.
  Key insights include the need for real-time data freshness, comprehensive failure
  coverage, and effective approximation strategies for complexity management. Organizations
  should evaluate their governance landscape, enhance visibility into tool impact,
  and methodically scope agent capabilities to ensure robust governance frameworks.'
link: https://jasonstanley.substack.com/p/five-graphs-your-agents-need-and
tags:
- Security Graphs
- Graph Composition
- Agent Governance
- Access Control
- Contextual Decision Making
title: Five Graphs Your Agents Need (Nobody Has All of Them)
---

[![Jason Stanley](https://substackcdn.com/image/fetch/$s_!WBso!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1162034d-20cd-4661-9ea0-ecbacfa986ba_1251x1251.png)](https://jasonstanley.substack.com/)

# [Jason Stanley](https://jasonstanley.substack.com/)

SubscribeSign in

# Five Graphs Your Agents Need (Nobody Has All of Them)

### Agent control is a graph composition problem. Each layer answers a necessary control question. None is sufficient alone. Composing across them is hard.

[![Jason Stanley's avatar](https://substackcdn.com/image/fetch/$s_!n5O6!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2062ce0c-c956-4be6-8e0c-2ff8bb616838_198x198.png)](https://substack.com/@jasonstanley)

[Jason Stanley](https://substack.com/@jasonstanley)

Feb 15, 2026

Share

[![A 17th-century engraving by Athanasius Kircher depicting the Kabbalistic Tree of Life as ten labeled circular nodes connected by twenty-two labeled edges arranged in a layered vertical structure with cross-connections between layers.](https://substackcdn.com/image/fetch/$s_!62rY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb525672d-9448-4f01-9d21-6a4fa46ad8e5_500x739.png)](https://substackcdn.com/image/fetch/$s_!62rY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb525672d-9448-4f01-9d21-6a4fa46ad8e5_500x739.png) Athanasius Kircher's Sephirotic Tree of Life, from _Oedipus Aegyptiacus_ (1652). Ten nodes, twenty-two edges, multiple layers of connection. Governance is a graph problem.

Five different kinds of graph are converging on agent governance from different directions. Access graphs map who can reach what. Security graphs map what is exploitable and what the blast radius looks like. Context graphs capture decision trajectories so agents can act on precedent. Action graphs model what operations are legal on what objects under what rules. Knowledge graphs represent entities and relationships across the enterprise.

Each answers a real control question. Each is being built, bought, or proposed by serious teams. Yet each alone is insufficient. The governance gap in agentic systems lives in the questions that only a composed view can answer. Right now almost nobody is composing.

This essay maps the layers, identifies what each contributes and where each falls short, and argues that the central design challenge for agent governance is graph composition: getting coherent governance answers from structures built by different teams, in different products, on different refresh cycles, for different purposes.

## The landscape: four graphs, four control questions

**Access graphs** answer the question of who can reach what resource through what chain of delegations, and whether that access is appropriate. Veza has built an Access Graph that ingests permissions metadata from SaaS applications, cloud platforms, data systems, and custom apps, normalizing different permission models into a single queryable structure. The graph captures delegation chains: user A has role B, which inherits permission C on resource D, which is federated through identity provider E. It refreshes on change rather than continuously, producing a near-static map of reachability. For agent governance, this answers the threshold question of whether the agent’s credentials allow it to touch a given resource. What it does not capture is behavioral context, temporal patterns, or what happens after the agent gets there.

**Security graphs** answer the question of what is exploitable and what the blast radius would be. Wiz is the clearest example. Their Security Graph is a digital twin of cloud infrastructure that composes risk factors across dimensions: vulnerabilities, network exposure, identity paths, data sensitivity, and runtime signals. Risk engines traverse the graph in seconds, surfacing attack paths and toxic combinations no single scanner would catch. The architectural insight matters: composing risk factors across dimensions requires a graph. Tables and dashboards cannot express the combinatorial nature of risk; you need traversal. For agent governance, security graphs show whether the infrastructure underneath an agent’s actions carries unpatched vulnerabilities or lateral movement risks. The limitation is that they were built for infrastructure, not agent action spaces. They model what exists, not what an agent might do next.

**Context graphs** answer the question of what happened before and why. [Foundation Capital’s widely shared thesis](https://foundationcapital.com/context-graphs-ais-trillion-dollar-opportunity/) captures the shift: if agents are going to do real work, they need more than current state. They need rich histories of decision trajectories, including what context was consulted, what constraints applied, and what exceptions were granted, so future actions can be grounded in how work actually happened. The limitation, which I explored in an [earlier essay on making context graphs failure-aware](https://jasonstanley.substack.com/p/making-context-graphs-failure-aware), is that decision traces optimized for precedent tend to under-specify what matters for reliability and security. Knowing that a similar transaction was approved last quarter is useful. Knowing why a similar transaction failed, what boundary was crossed, what control did not fire, requires richer capture and deliberate investment in failure-related primitives.

**Action graphs** model what operations are legal on what objects under what rules, and what those operations do to the world. Palantir’s Ontology is the strongest current example. It treats operations as first-class citizens alongside data, modeling an operation like approving a purchase order not just as a permission to check but as a governed procedure with preconditions (budget check, three-way match, vendor approval status), state transitions (pending to approved), downstream triggers (payment workflow, general ledger update, vendor notification), and rollback logic. For agents that can only read, an action graph is basically an access graph: the distinction does not matter much. Once agents can write in consequential ways, the gap opens up. An access graph tells you the agent can reach the payment system. An action graph tells you what executing a payment means: what validates, what changes state, what cascades, and what can be undone. Palantir’s approach embeds governance into the data model itself, policy-as-structure rather than policy-as-bolt-on. The tradeoff is tight coupling and portability risk.

Beneath all four sits the broader category of **knowledge graphs**: the entity-relationship structures that power enterprise search (Glean, Microsoft Graph, various GraphRAG implementations). Several of the layers above are technically knowledge graphs with specialized schemas and operational hooks. The distinction worth preserving is that a general knowledge graph tells you what exists and how things relate, while each of the four layers above adds a specific operational question on top of that structure.

## Keeping graphs honest: freshness, failure coverage, and active enrichment

Graphs are only as useful as the data that populates them. Access graphs are notoriously stale; permissions drift is one of the oldest problems in identity and access management. Security graphs depend on scan freshness. Context graphs accumulate errors and gaps over time. Action graphs fall behind the systems they model as configurations change. If the composed view depends on four inputs and two of them are stale, the governance decision is unreliable regardless of how sophisticated the composition logic is.

The industry is moving toward event-driven freshness for the layers where it matters most. Palantir’s Ontology objects are backed by streaming data pipelines that use change data capture to sync source-system changes in seconds rather than waiting for nightly ETL. Wiz recently shipped real-time CSPM that triggers security graph updates off cloud events (resource provisioned, configuration changed) rather than relying solely on periodic scans, updating graph objects within minutes. These are meaningful improvements over batch refresh, but they also create freshness asymmetries across the composed view. If your security graph is near-real-time but your access graph refreshes daily, the composition is only as current as its stalest input. Runtime governance logic needs to account for this, treating stale layers with appropriate caution or flagging them in audit trails.

Failure coverage deserves particular attention beyond freshness. Context graphs populated only by production data will reflect the distribution of ordinary operations, which systematically under-samples the failure state space. The failures that matter most tend to live in rare contexts: cross-boundary situations, partial outages, ambiguous instructions, novel combinations of tools and permissions. Production never visits these regions.

I have argued in [earlier work](https://jasonstanley.substack.com/p/making-context-graphs-failure-aware) that this gap requires two deliberate investments. The first is capturing richer failure primitives in traces: not just what happened and what the outcome was, but where instruction-like content entered, how it flowed into action, what separators existed between retrieved text and planner directives, which controls fired and which did not, and where the breakpoints are. The second is exploratory testing as a deliberate practice for growing the failure side of graph coverage. Production traces tell you what happened. Exploratory traces tell you what could happen. Together they give the graphs the coverage they need to support governance decisions in the regions where risk actually concentrates.

This is the least mature of the three freshness patterns (batch refresh, event-driven CDC, active enrichment through testing) and the one where the most governance work remains. Pattern cards, which I have described in several earlier posts ( [like this one](https://jasonstanley.substack.com/p/incident-agents-pattern-cards-and)), are one way to compress the resulting failure lessons into reusable, executable structure: a named mechanism tied to representative traces, detection methods, test recipes, and mitigation hooks.

## The composition problem

Each of these graphs answers a necessary question. None answers the compound question that agent governance actually requires.

Consider an agent that processes vendor invoices: receiving them, matching against purchase orders, routing approvals, triggering payments. The governance question at any decision point is a composition across all four layers plus the knowledge graph underneath them.

Is the delegation chain from the initiating user through the agent to the payment system valid? Is the infrastructure path carrying known vulnerabilities or lateral movement risks? Is there precedent for this vendor, this amount range, this approval pattern? Is the payment operation modeled with the right validation rules and downstream consequence tracking?

The governance decision requires all of these answers together. Today, these live in separate products, maintained by separate teams, refreshing on separate cycles, using separate data models. IAM owns the access graph. SecOps owns the security graph. The AI platform team might own context and action layers. The organizational composition problem, who owns the composed view, is at least as hard as the technical one.

When the graphs give conflicting signals, something needs to arbitrate. The access graph says the agent can reach the payment system. The security graph says the path carries an unpatched vulnerability. The context graph says there is precedent. A known failure pattern matches the current scenario. Is every layer a hard gate? Are some advisory? Is there a hierarchy? These are design decisions most organizations have not yet made, because until recently the graphs did not exist in forms that could be queried together.

## Tractability: approximation strategies for graphs too large to exhaust

There is a harder problem underneath the composition question. Wiz’s Security Graph works because cloud infrastructure, while large, is finite and relatively static. Agent action spaces are different. They are non-deterministic and grow combinatorially with planning horizon. An agent with access to twenty tools, each with conditional effects on shared state, produces an action space that expands exponentially with the number of steps. Exact blast-radius computation becomes infeasible beyond trivially short horizons.

This is a basic complexity-theory observation applied to a new domain. The practical question is what approximations are good enough to support governance decisions. Several strategies are available, and they work best in combination.

**Bounded-horizon reachability** limits computation to N steps out from the current action. You compute the reachable subgraph within a fixed lookahead window and treat everything beyond it conservatively. This is the simplest approach and the most immediately implementable.

**Risk-weighted pruning** traverses high-consequence edges preferentially and drops low-risk branches early. If a downstream path only touches read-only resources, you deprioritize it relative to a path leading to a production write endpoint. This turns exhaustive search into guided exploration of the risk-relevant subgraph.

**Probabilistic cascade estimation**, borrowed from network science, replaces exhaustive enumeration with distributional bounds. The social graph literature has mature, well-validated models for how effects propagate through networks. The Independent Cascade and Linear Threshold models, validated in contexts from epidemiology to infrastructure failure analysis, model propagation probabilistically: given that the agent acted on node X, what is the expected propagation depth and breadth given graph topology and edge weights (where weights encode write-access, data sensitivity, or irreversibility)? This scales to large graphs and provides exactly the kind of approximation the tractability problem demands. As far as I can tell, nobody in the agent governance conversation is applying these models to agent infrastructure graphs, despite decades of validation in adjacent domains.

**Centrality-based monitoring prioritization**, also from network science, helps when you cannot monitor everything. Computing betweenness centrality across the composed graph produces a ranked list of which components, if compromised or degraded, would disrupt the most agent workflows. These high-centrality components are where blast-radius propagation concentrates and where governance attention should concentrate too. There is a subtler insight from research on structural holes in networks: the most dangerous paths may not be the heavily-trafficked, well-monitored ones but the rarely-used tool connections and legacy connectors that nobody watches. Production under-samples these paths, reinforcing the earlier point about exploratory testing.

**Conservative scoping under uncertainty** is the fallback: if the reachable subgraph exceeds your ability to assess, narrow the agent’s tool set or permissions until it does not. The least sophisticated approach but the most defensible when better approximations are not yet available.

## What this looks like in practice: design time and runtime

The four-layer composition plays out very differently depending on whether you are making a pre-deployment decision or a runtime governance call. The difference is latency, and latency determines what is feasible.

**Design-time readiness.** Before deployment, the question is whether the agent is ready: correctly scoped, adequately tested, and well-understood in terms of what it can reach and what could go wrong. You can take days. Graph traversals can be thorough.

You map the full reachable subgraph from the access graph and discover the agent has write access to the payment system, read access to the vendor master, and the ability to create new vendor records, an unexpected permission inherited from a broad service account. You tighten the credential. You check the action graph and find that the payment operation has validation rules modeled, but modifying payment terms does not. You model it or block it. You run the security graph and find the payment connector sits on infrastructure with an unpatched vulnerability creating a lateral movement path to the ERP admin interface. You patch or restrict network exposure. You query known failure patterns and find a pattern card for duplicate invoice processing due to an idempotency gap. You add the check as a pre-deployment test. You use centrality analysis to identify the highest-betweenness components in the reachable subgraph and ensure each has monitoring in place. You run exploratory tests exercising boundary conditions and unusual tool combinations that production will never produce on its own.

Readiness is not a single check. It is the compound result of scoping, testing, infrastructure assessment, and failure-pattern review, each drawing on different graph layers.

**Runtime governance.** In production, the question is whether a specific action should be allowed right now, and the latency budget is tight.

The agent receives an invoice for $47,000 from a known vendor and is about to trigger payment approval. The access graph (cached, sub-second) confirms the delegation chain is valid for this amount. The context graph (retrieval, low hundreds of milliseconds) shows three prior clean payments to this vendor in similar ranges. The security graph (last scan twelve hours ago) shows no new critical findings; a note goes to the audit log that the scan is not fresh. Pre-compiled pattern matching (sub-second) finds no match to active failure patterns. A pre-computed cascade estimate shows bounded blast radius: one payment of $47K to a verified vendor. Decision: allow, with full audit trail.

Now change the scenario. The vendor was added two days ago. There is no precedent in the context graph. The amount sits just under the $50,000 threshold requiring additional approval. Pre-compiled pattern matching flags this combination: threshold-adjacent payments from recently onboarded vendors. The cascade estimate still shows bounded financial exposure, but the combination of no precedent, a new vendor, and a threshold-adjacent amount triggers escalation. Decision: route to a human reviewer, surfacing the specific graph-based evidence for why.

Different graph layers operate at different speeds. Some can be queried in real time; others must be pre-computed and cached. A runtime governance architecture needs to account for this, and needs a clear policy for what happens when a layer is stale or unavailable.

## The channels you cannot graph

Tool calls are the most governable channel for agent impact because they are explicit, loggable, and interruptible. Graph-based governance applies well here: if you can map an agent’s tools and their downstream write paths, you can estimate blast radius and enforce scoping.

But state changes also flow through channels harder to represent as graph edges. Data pulled from internal systems into a prompt changes agent behavior without any tool invocation. Goal drift accumulates through context over multi-step plans. Reasoning errors compound. Correct actions on stale or corrupted data produce wrong outcomes no tool-graph would flag.

Graph-based composition gives you strong leverage over the explicit, structured surfaces of agent behavior. On the surfaces where you lack graph visibility, the appropriate response is greater conservatism: shorter planning horizons, more frequent human checkpoints, tighter output constraints. Governance confidence should be calibrated to the surfaces you can actually see.

## Three priorities

If the composition thesis holds, three things are worth doing now.

1. **Inventory your graph coverage.** Audit which of the four layers you currently have, even partially. Most organizations will find some access-graph coverage through IAM tooling, maybe some security-graph coverage through a CSPM, and very little of the other two. Identifying what is missing tells you which control questions you cannot currently answer.

2. **Map tool-to-impact subgraphs.** For every tool an agent can invoke, trace its downstream write paths: what systems it can mutate, what data it can expose, what workflows it can trigger. This is a tractable subset of the full composition problem, and it directly informs capability contracts and least-agency scoping. Compute centrality on this subgraph to know where monitoring should concentrate. But keep in mind that tool calls are one channel among several, and be more conservative on the channels you cannot graph.

3. **Scope agents to the graph you can reason about.** If the reachable subgraph from an agent’s credentials and tools exceeds your ability to assess blast radius, narrow the permissions, restrict the tool set, or shorten the planning horizon until it does not. This is least agency expressed as a function of graph visibility. Do not grant autonomy over territory you cannot see. As graph coverage and composition capabilities improve, agents can safely do more. That is the feedback loop worth building.


* * *

_This essay builds on several earlier pieces: [Making Context Graphs Failure-Aware](https://jasonstanley.substack.com/p/making-context-graphs-failure-aware), [Beyond Permissions: Least Agency as Architecture for Agentic Systems](https://jasonstanley.substack.com/p/beyond-permissions-least-agency-as), and [Incident Agents, Pattern Cards, and the Broken Flow from AI Failures to Defenses](https://jasonstanley.substack.com/p/incident-agents-pattern-cards-and)._

Share

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

TopLatestDiscussions

No posts

### Ready for more?

Subscribe
