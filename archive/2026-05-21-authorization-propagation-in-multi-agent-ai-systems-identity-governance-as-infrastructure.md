---
date: '2026-05-21'
description: This paper introduces the concept of *authorization propagation* in multi-agent
  AI systems, identifying it as critical to maintaining authorization invariants during
  autonomous data handling and task delegation. Distinct from prompt injection vulnerabilities,
  authorization propagation addresses workflow-level challenges including transitive
  delegation, aggregation inference, and temporal validity. Existing access control
  models (RBAC, ABAC, ReBAC) inadequately address these requirements. The paper outlines
  seven essential architectural needs for robust authorization frameworks, advocating
  that identity governance should be treated as foundational infrastructure. Preliminary
  evidence from enterprise AI deployments highlights the prevalence of authorization
  failures during normal operations, underscoring the urgency for structured solutions.
link: https://arxiv.org/html/2605.05440v1
tags:
- Identity Governance
- Access Control Models
- Multi-Agent Systems
- Authorization Propagation
- AI Security
title: 'Authorization Propagation in Multi-Agent AI Systems: Identity Governance as
  Infrastructure'
---

Title:

Content selection saved. Describe the issue below:

Description:

[License: arXiv.org perpetual non-exclusive license](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2605.05440v1 \[cs.AI\] 06 May 2026

# Authorization Propagation in Multi-Agent AI Systems:   Identity Governance as Infrastructure

Krti Tallam

Kamiwaza AI

krti@kamiwaza.ai

(May 2026)

###### Abstract

The security discussion around agentic AI focuses heavily on prompt injection. This paper argues that multi-agent systems also create a distinct authorization problem: maintaining authorization invariants as non-human principals retrieve data, delegate tasks, and synthesize results across changing boundaries. We call this problem _authorization propagation_. It is not reducible to prompt injection and is not fully addressed by classical access-control models such as RBAC, ABAC, or ReBAC. The paper formalizes authorization propagation as a workflow-level property, identifies three sub-problems (transitive delegation, aggregation inference, and temporal validity), and derives seven structural requirements for authorization architectures in multi-agent AI systems. Recent work on invocation-bound capability tokens (Prakash, [2026](https://arxiv.org/html/2605.05440v1#bib.bib13 "AIP: invocation-bound capability tokens with Biscuit and Datalog")), task-scoped authorization envelopes (Sharma et al., [2026](https://arxiv.org/html/2605.05440v1#bib.bib14 "PAuth: precise task-scoped authorization for AI agents")), dependency-graph policy enforcement (Palumbo et al., [2026](https://arxiv.org/html/2605.05440v1#bib.bib16 "PCAS: policy compiler for agentic systems")), and execution-count revocation (Parakhin, [2026](https://arxiv.org/html/2605.05440v1#bib.bib15 "The bureaucracy of speed: capability coherence systems for agent authorization")) demonstrates that the field is converging on the problem, but not yet on a complete architecture. The central claim is that identity governance must be treated as infrastructure: evaluated continuously, enforced at every interaction boundary, and designed into the system before orchestration logic is allowed to scale. Preliminary implementation evidence from a production enterprise AI platform shows that ordinary system behavior, not only adversarial action, already produces the failures this model predicts.

Keywords: agentic AI, authorization, access control, delegation, aggregation inference, identity governance

## 1 Introduction

As AI systems evolve from single-model inference to multi-agent orchestration, the security discourse has concentrated heavily on prompt injection. This is understandable. Prompt injection is the mechanism by which an adversary subverts an agent’s behavior by manipulating the content it processes. It is well-documented, broadly applicable, and — as of this writing — not fully solved at the model level.

The resulting industry posture treats prompt injection as the central, sometimes only, novel security problem in agentic AI. A common argument, articulated informally but widely held, runs approximately as follows: prompt injection is to agentic AI what SQL injection was to web applications. Fix it architecturally — separate data from instructions, as parameterized queries separated data from SQL — and the remaining security problems reduce to known primitives: authentication, authorization, network isolation, secrets management. Nothing novel.

This paper argues that the analogy is partially correct but materially incomplete. Prompt injection is the novel _attack vector_. But there is a distinct novel _architectural problem_ that persists even under the assumption that prompt injection is fully solved: the problem of maintaining authorization invariants as non-human principals make chains of autonomous decisions.

We call this problem _authorization propagation_.

Consider a concrete scenario. An orchestrating agent receives a user query. It decomposes the task and delegates sub-tasks to specialized agents. Agent A retrieves data from Dataset X. Agent B retrieves data from Dataset Y. Agent C synthesizes the results from A and B into a response for the user. Even with perfect prompt injection defense — no agent can be tricked by the content it processes — the system must answer:

- •


Did Agent A have the right to access Dataset X?

- •


Did Agent B have the right to access Dataset Y?

- •


Does Agent C have the right to see the combined results?

- •


Does the user have the right to see the synthesized output?

- •


Does the _combination_ of X and Y reveal information that neither dataset alone would expose?


These are authorization questions, not prompt injection questions. They arise from the structure of the system, not from adversarial content. And they have no established equivalent of “parameterized queries” — no single architectural primitive that resolves them.

Why this matters now is that enterprise agents no longer merely retrieve documents on behalf of a visible human operator. They increasingly mediate the entire evidentiary path: decomposition, retrieval, tool invocation, synthesis, and delivery. In that setting, authorization is no longer just a question of whether an individual access is permitted. It is a question of whether the full delegated workflow preserves the authority, scope, and boundary conditions that make the final result governable.

This paper formalizes authorization propagation, distinguishes it from prompt injection, and identifies what it demands of authorization architectures.

## 2 Background and Related Work

### 2.1 Prompt Injection and Agent Security

Prompt injection was first characterized as a distinct vulnerability class in 2022 (Gruskovnjak, [2023](https://arxiv.org/html/2605.05440v1#bib.bib11 "Indirect prompt injection via web search")) and has since been the subject of extensive research (Greshake et al., [2023](https://arxiv.org/html/2605.05440v1#bib.bib12 "Not what you’ve signed up for: compromising real-world LLM-integrated applications with indirect prompt injection")). Google DeepMind’s “AI Agent Traps” taxonomy (Google DeepMind, [2026](https://arxiv.org/html/2605.05440v1#bib.bib7 "AI Agent Traps: a taxonomy of attacks on AI agents")) identifies six categories of agent-directed attacks: content injection, semantic manipulation, cognitive state attacks, tool misuse induction, goal hijacking, and multi-agent collusion. These categories are useful but share a common structure: an adversary manipulates the content, context, or memory that an agent processes in order to alter its behavior.

The defense literature has correspondingly focused on content-level mitigations: input filtering, output validation, trusted/untrusted content separation, and instruction hierarchy enforcement.

What this literature does not address in depth is the authorization architecture that determines what data and actions are available to agents in the first place. The implicit assumption is that if agents can be made robust to adversarial content, the remaining security properties can be handled by conventional access control.

Recent empirical work challenges this assumption. Anonymous ( [2026](https://arxiv.org/html/2605.05440v1#bib.bib28 "Claude Code permission system evaluation")) evaluate the Claude Code permission system and find an 81.0% false negative rate on deliberately ambiguous authorization scenarios, with 36.8% of state-changing actions bypassing the classifier entirely via file edits. Debenedetti and others ( [2026](https://arxiv.org/html/2605.05440v1#bib.bib27 "Prompt injection as role confusion")) demonstrate that prompt injection can be reframed as role confusion, with 60% attack success on StrongREJECT via spoofed reasoning — arguing that “security is defined at the interface but authority is assigned in latent space.” These results suggest that even well-resourced content-level defenses are insufficient, reinforcing the need for architectural authorization enforcement.

### 2.2 Classical Access Control Models

The access control literature provides foundational models that inform but do not fully address authorization propagation. Bell and LaPadula ( [1973](https://arxiv.org/html/2605.05440v1#bib.bib32 "Secure computer systems: mathematical foundations")) formalize mandatory access control with the ⋆\\star-property (no write-down) and simple security property (no read-up), preventing information flow from high-classification to low-classification subjects. Biba ( [1977](https://arxiv.org/html/2605.05440v1#bib.bib33 "Integrity considerations for secure computer systems")) provides the dual integrity model: no read-down, no write-up. Clark and Wilson ( [1987](https://arxiv.org/html/2605.05440v1#bib.bib34 "A comparison of commercial and military computer security policies")) shift focus to well-formed transactions and separation of duty, requiring that data modifications pass through certified transformation procedures.

Sandhu et al. ( [1996](https://arxiv.org/html/2605.05440v1#bib.bib35 "Role-based access control models")) formalize role-based access control (RBAC), which assigns permissions to roles rather than directly to subjects. XACML (OASIS, [2013](https://arxiv.org/html/2605.05440v1#bib.bib36 "eXtensible access control markup language (XACML) version 3.0")) extends attribute-based access control with obligation policies — actions that must be performed upon access denial or grant.

These models address important properties: confidentiality (Bell-LaPadula), integrity (Biba), transaction correctness (Clark-Wilson), administrative scalability (RBAC), and policy expressiveness (XACML). Contemporary risk frameworks (National Institute of Standards and Technology, [2023](https://arxiv.org/html/2605.05440v1#bib.bib9 "Artificial intelligence risk management framework (AI RMF 1.0)"); International Organization for Standardization, [2023](https://arxiv.org/html/2605.05440v1#bib.bib10 "ISO/IEC 42001:2023 information technology — artificial intelligence — management system")) acknowledge that AI systems introduce novel authorization challenges, but delegate the specifics to implementation standards that do not yet exist for multi-agent architectures. The classical models share assumptions that do not hold in multi-agent AI systems: human principals, static resources, synchronous access decisions, and well-defined trust boundaries. The authorization propagation problem arises precisely where these assumptions break down.

### 2.3 Relationship-Based Access Control

Relationship-based access control (ReBAC) originates from Google’s Zanzibar system (Pang et al., [2019](https://arxiv.org/html/2605.05440v1#bib.bib8 "Zanzibar: google’s consistent, global authorization system")), which models authorization as a graph of typed relationships between subjects and objects. A subject’s permissions are determined not by static role assignments (as in RBAC) or attribute predicates (as in ABAC), but by the existence and type of relationships in a tuple store. This enables fine-grained, context-sensitive authorization that can express ownership, delegation, group membership, and organizational hierarchy.

ReBAC has been implemented in several open systems (SpiceDB, OpenFGA, Authzed) and is well-suited to multi-tenant enterprise environments where access patterns are relational rather than role-based.

However, the Zanzibar model and its descendants were designed for human principals interacting with static resources through well-defined API surfaces. They do not natively address:

- •


non-human principals that autonomously chain authorization decisions

- •


transitive delegation where one agent acts on behalf of another

- •


synthesized outputs where the result is derived from multiple authorized sources but the combination may not itself be authorized

- •


temporal validity where authorization state may change between the start and end of a multi-step agent workflow


### 2.4 Emerging Agent Authorization Frameworks

The period from late 2025 through early 2026 has seen a rapid emergence of authorization frameworks specifically designed for agentic AI systems. We survey the most architecturally significant.

##### Invocation-bound capability tokens.

Prakash ( [2026](https://arxiv.org/html/2605.05440v1#bib.bib13 "AIP: invocation-bound capability tokens with Biscuit and Datalog")) proposes Invocation-Bound Capability Tokens (IBCTs) that fuse identity, attenuated authorization, and provenance binding into an append-only token chain. Two wire formats are specified: compact JWT for single-hop and Biscuit tokens with Datalog policies for multi-hop delegation. Reference implementations in Python and Rust demonstrate 0.049ms verification latency and 100% adversarial rejection across 600 attack attempts. IBCTs address R2 (explicit, bounded, auditable delegation) and partially address R5 (self-contained authorization traces), but do not address aggregation inference (R4).

##### Task-scoped authorization envelopes.

Sharma et al. ( [2026](https://arxiv.org/html/2605.05440v1#bib.bib14 "PAuth: precise task-scoped authorization for AI agents")) propose PAuth, which challenges OAuth’s operator-scoped authorization model. PAuth introduces “NL slices” — symbolic specifications of expected tool calls per service derived from natural language task descriptions — and “envelopes” that bind operand values to symbolic provenance. The system achieves 100% success on benign tasks and 100% warning rate on injected attacks. The envelope concept is architecturally adjacent to the execution envelope pattern described in the companion fail-and-report paper, and the NL-slice concept provides a mechanism for deriving per-task authorization scope.

##### Capability coherence via execution counting.

Parakhin ( [2026](https://arxiv.org/html/2605.05440v1#bib.bib15 "The bureaucracy of speed: capability coherence systems for agent authorization")) provides formal proof that TTL-based token revocation fails at agent execution speeds. Mapping CPU cache coherence protocols (MESI) to agent authorization revocation, the paper demonstrates that execution-count-based Release Consistency bounds unauthorized operations at Dr​c​c≤nD\_{rcc}\\leq n _independent of agent velocity_, versus O​(v⋅T​T​L)O(v\\cdot TTL) scaling for time-based approaches — a 120×\\times reduction in unauthorized operations. This directly addresses the temporal validity sub-problem (Section [5.2.3](https://arxiv.org/html/2605.05440v1#S5.SS2.SSS3 "5.2.3 Temporal Validity ‣ 5.2 The Three Sub-Problems ‣ 5 Authorization Propagation: The Formal Problem ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure")) by demonstrating that time-based revocation is architecturally wrong for autonomous agents.

##### Dependency-graph policy enforcement.

Palumbo et al. ( [2026](https://arxiv.org/html/2605.05440v1#bib.bib16 "PCAS: policy compiler for agentic systems")) propose PCAS, which models agent state as a dependency graph capturing causal relationships among tool calls, results, and messages. Datalog-derived policies are enforced by a reference monitor. The system improves policy compliance from 48% to 93% across frontier models with zero policy violations under deterministic enforcement independent of model reasoning. The dependency graph approach provides a concrete mechanism for R3 (authorization at every retrieval boundary) and R5 (workflow-scoped traces).

##### Standards-track proposals.

The OpenID Foundation ( [2025](https://arxiv.org/html/2605.05440v1#bib.bib20 "Agentic identity whitepaper")) has published a consensus whitepaper on agentic identity, and Benameur and others ( [2025](https://arxiv.org/html/2605.05440v1#bib.bib21 "OIDC-A: openid connect for agents 1.0")) propose OIDC-A (OpenID Connect for Agents 1.0), extending OIDC with agent identity, delegation chain validation, attestation verification, and capability-based authorization. Together with the IETF AIP track (Prakash, [2026](https://arxiv.org/html/2605.05440v1#bib.bib13 "AIP: invocation-bound capability tokens with Biscuit and Datalog")), these represent the two major standards efforts.

### 2.5 Formal Methods for Agent Security

Several recent works provide formal foundations relevant to authorization propagation.

Chen ( [2026](https://arxiv.org/html/2605.05440v1#bib.bib17 "AITH: post-quantum continuous delegation for AI agents")) proposes AITH, a post-quantum continuous delegation protocol for AI agents. Its six-check Boundary Engine implements push-based revocation within one second. All five security theorems are machine-verified via the Tamarin Prover under the Dolev-Yao model. Notably, the protocol achieves 79.5% autonomous execution with 6.1% human escalation and 14.4% blocked — the escalation rate representing an implementation of the fail-and-report pattern where the system halts and reports rather than proceeding under uncertain authorization.

Garby et al. ( [2026](https://arxiv.org/html/2605.05440v1#bib.bib18 "LLMbda calculus: dynamic information-flow control for agentic programming")) present the LLMbda Calculus, a lambda calculus enriched with dynamic information-flow control and LLM invocation primitives. Their termination-insensitive noninterference theorem establishes integrity and confidentiality guarantees for agentic programming. Noninterference — the property that low-integrity inputs cannot influence high-integrity actions — is the formal analogue of the authorization propagation guarantee: information flow through the agent chain preserves authorization boundaries.

Song and others ( [2026](https://arxiv.org/html/2605.05440v1#bib.bib19 "Formalizing LLM agent security")) (UC Berkeley / ETH Zurich) propose four contextual security properties for LLM agents: task alignment, action alignment, source authorization, and data isolation. Source authorization maps directly to authorization propagation; data isolation maps to the anti-aggregation-inference requirement. The formalization provides an independent validation of the problem decomposition presented in this paper.

### 2.6 Empirical Evidence of Authorization Failures

The authorization propagation problem is not merely theoretical. Recent empirical work demonstrates that it produces real, exploitable failures.

##### Semantic intent fragmentation.

The SIF attack (Anonymous, [2026](https://arxiv.org/html/2605.05440v1#bib.bib22 "Semantic intent fragmentation: aggregation attacks on agentic AI systems")), accepted at the AAAI 2026 Summer Symposium, decomposes a legitimate request into individually benign subtasks that jointly violate security policy through four mechanisms: bulk scope escalation, silent data exfiltration, embedded trigger deployment, and quasi-identifier aggregation. A 71% success rate across 14 enterprise scenarios provides direct empirical evidence that aggregation inference (Section [5.2.2](https://arxiv.org/html/2605.05440v1#S5.SS2.SSS2 "5.2.2 Aggregation Inference ‣ 5.2 The Three Sub-Problems ‣ 5 Authorization Propagation: The Formal Problem ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure")) is a real, exploitable attack vector, not a theoretical concern.

##### Agentic deanonymization.

Li ( [2026](https://arxiv.org/html/2605.05440v1#bib.bib23 "Agentic deanonymization")) demonstrates that LLM agents with web search can link anonymized interview data to specific individuals by decomposing re-identification into individually benign sub-tasks that bypass safeguards. This is aggregation inference in practice: each individual data access is authorized, but their composition violates privacy policy.

##### Production deployment evidence.

Maiti ( [2026](https://arxiv.org/html/2605.05440v1#bib.bib24 "Healthcare zero trust: production deployment of autonomous AI agents")) reports on 9 autonomous AI agents deployed in a healthcare production environment for 90 days under zero-trust constraints. The deployment uses gVisor isolation, credential proxy sidecars, egress allowlisting, and structured metadata envelopes. Four HIGH severity findings from automated security testing were identified, providing rare production-scale evidence that authorization architecture matters in practice. The credential proxy sidecar pattern implements authorization propagation at the container layer.

##### MCP threat landscape.

Anonymous ( [2026](https://arxiv.org/html/2605.05440v1#bib.bib25 "MCPSHIELD: threat analysis of MCP tool ecosystem")) identifies 7 threat categories, 23 attack vectors, and 4 attack surfaces across 177,000+ MCP tools, finding that no single defense covers more than 34% of threats. An integrated architecture achieves 91%, providing quantitative evidence for the defense-in-depth argument and against the notion that any single authorization mechanism is sufficient.

### 2.7 The Companion Governance Framework

The companion paper, _Machine-Speed Accountability_(Tallam, [2026e](https://arxiv.org/html/2605.05440v1#bib.bib1 "Machine-speed accountability: a constraint-aware reference model for oversight-heavy ai")), provides a governance operating model for oversight-heavy AI environments. It defines four constraints — traceability, auditability, controllability, and recovery — and argues that accountability must be treated as a system constraint rather than a reporting layer. Its control layer identifies the seams where controls must exist: between data and retrieval, model and context, model and tools, tools and systems of record, and human operators and delegated agents.

This paper provides the technical depth for the last of those seams — the boundary between human operators and delegated agents, and between agents themselves — which is where authorization propagation occurs.

## 3 A Taxonomy: Attack Vectors and Architectural Problems

The current AI security discourse conflates two categories of challenge that have different structures, different solutions, and different implications for system design.

### 3.1 Attack Vectors

Attack vectors are mechanisms by which an adversary subverts system behavior. In agentic AI, the primary attack vectors are:

- •


Content injection: adversarial instructions embedded in data that an agent processes (e.g., hidden text in HTML, manipulated documents)

- •


Semantic manipulation: authoritative-sounding content that causes an agent to override its instructions

- •


Cognitive state attacks: poisoning an agent’s memory, context, or learned state

- •


Tool misuse induction: manipulating an agent into invoking tools in unintended ways


These share a common property: they require an adversary to introduce malicious content into the agent’s processing path. Defense is a content-integrity problem.

### 3.2 Architectural Problems

Architectural problems are structural challenges that arise from the design of the system itself, independent of adversarial action. In multi-agent AI, the primary architectural problems are:

- •


Authorization propagation: maintaining access control invariants as agents delegate tasks, retrieve data, and synthesize results across multiple authorization boundaries

- •


Transitive delegation: determining what authority an agent inherits when acting on behalf of another agent or a human principal

- •


Aggregation inference: determining whether a synthesized result derived from individually authorized data sources is itself authorized for the requesting principal

- •


Temporal validity: ensuring that authorization decisions remain valid across the duration of a multi-step autonomous workflow


A recent systematization of knowledge (Anonymous, [2026](https://arxiv.org/html/2605.05440v1#bib.bib31 "SoK: attack surface of agentic AI")) introduces the Privilege Escalation Distance metric for quantifying authorization gaps across agentic attack surfaces. These architectural problems do not require an adversary. They arise from normal system operation. A misconfigured agent chain, a stale relationship tuple, a workroom membership change that propagates too slowly — any of these can produce unauthorized data exposure without a traditional breach.

### 3.3 Why the Distinction Matters

Solving prompt injection does not solve authorization propagation. Even in a system with perfect content integrity — where no agent can be tricked by anything it reads — the authorization questions remain:

- •


Which data sources is each agent permitted to access?

- •


Does delegation from Agent A to Agent B carry A’s authority, B’s authority, or neither?

- •


When Agent C synthesizes results from multiple sources, does the user have authorization for the synthesis?

- •


If a relationship tuple is revoked mid-workflow, what happens to results already derived from data accessed under that tuple?


Conversely, solving authorization propagation does not solve prompt injection. A system with perfect authorization architecture can still be subverted by an adversary who manipulates agent behavior through content injection.

The two problems are complementary, not reducible. Treating them as a single problem — or treating one as a subset of the other — leads to architectures that are robust against attacks but structurally unsound, or structurally sound but vulnerable to adversarial content.

Bhattarai and Vu ( [2026](https://arxiv.org/html/2605.05440v1#bib.bib29 "Deterministic architectural boundaries for agentic AI")) independently arrive at a compatible conclusion, identifying the “Lethal Trifecta” — untrusted inputs, privileged data access, and external action capability — and arguing that alignment is insufficient; architectural mediation is required. Their finite action calculus formalizes monotonic permissions, complementing the structural requirements presented in Section [8](https://arxiv.org/html/2605.05440v1#S8 "8 Structural Requirements ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

## 4 Identity Governance as Infrastructure

### 4.1 The Convergence Thesis

We observe that the authorization challenges in multi-agent AI systems converge from two independent directions:

##### Internal drift.

Multi-agent systems accumulate authorization inconsistencies through normal operation. Ontologies evolve. Relationship tuples go stale. Workroom or team membership changes. Agent configurations are updated without corresponding authorization reviews. The system drifts into a state where its actual data access patterns no longer match its intended authorization posture. No attacker is required.

##### External attack.

The DeepMind Agent Traps taxonomy (Google DeepMind, [2026](https://arxiv.org/html/2605.05440v1#bib.bib7 "AI Agent Traps: a taxonomy of attacks on AI agents")) demonstrates that the same system layers that drift internally — context, memory, tool interfaces, data retrieval paths — are also the attack surface for external adversaries. An attacker who can manipulate an agent’s context can alter what data it retrieves. An attacker who can poison an agent’s memory can alter what it considers authorized.

Both vectors produce the same outcome: unauthorized data exposure without a traditional perimeter breach. The convergence of internal drift and external attack on the same system layers is what elevates identity governance from a policy concern to an infrastructure requirement.

### 4.2 What “Infrastructure” Means Here

To say identity governance is infrastructure is to make a specific architectural claim: authorization state must be evaluated continuously and enforced at every interaction boundary in the system, not checked periodically or applied as a middleware layer.

The analogy is to encryption in transit. Early web architectures treated TLS as optional, applied selectively to “sensitive” endpoints. Modern architectures treat it as infrastructure — always on, not a decision point. The reason is that the cost of deciding “does this particular request need encryption?” exceeded the cost of encrypting everything, and the consequences of deciding wrong were unacceptable.

Identity governance in multi-agent AI is at an analogous inflection. The cost of deciding “does this particular agent interaction need authorization checking?” exceeds the cost of checking everything, and the consequences of deciding wrong — data leakage through an unchecked agent hop — are unacceptable in oversight-heavy environments.

This means authorization evaluation cannot be a gateway that agents pass through once. It must be a property of every data retrieval, every delegation, and every result synthesis in the system.

## 5 Authorization Propagation: The Formal Problem

### 5.1 System Model

Consider a multi-agent system with the following components:

- •


A set of human principalsH={h1,h2,…,hm}H=\\{h\_{1},h\_{2},\\ldots,h\_{m}\\}

- •


A set of agent principalsA={a1,a2,…,an}A=\\{a\_{1},a\_{2},\\ldots,a\_{n}\\}

- •


A set of data resourcesD={d1,d2,…,dk}D=\\{d\_{1},d\_{2},\\ldots,d\_{k}\\}

- •


An authorization functionauth​(s,r,t)→{allow,deny}\\mathrm{auth}(s,r,t)\\rightarrow\\{\\mathrm{allow},\\mathrm{deny}\\} that determines whether subject ss may access resource rr at time tt

- •


A delegation functiondelegate​(s1,s2,t)→P\\mathrm{delegate}(s\_{1},s\_{2},t)\\rightarrow P that determines what permissions principal s1s\_{1} transfers to principal s2s\_{2} at time tt


A workflow execution is a directed acyclic graph W=(V,E)W=(V,E) where each vertex v∈Vv\\in V is an agent action (retrieve, transform, synthesize, or return) and each edge (vi,vj)(v\_{i},v\_{j}) represents data flow from action viv\_{i} to action vjv\_{j}.

### 5.2 The Three Sub-Problems

#### 5.2.1 Transitive Delegation

When a human principal hh initiates a workflow that involves agents a1,a2,…,ana\_{1},a\_{2},\\ldots,a\_{n}, the system must determine the effective authority at each agent. The naive approach — each agent inherits the initiating human’s full authority — violates least privilege. The conservative approach — each agent operates only under its own service identity — may be insufficient to complete the workflow.

The problem is to define a delegation model where:

- •


Each agent’s effective authority is bounded and auditable

- •


Authority does not accumulate through delegation chains (no privilege escalation)

- •


The initiating principal’s authorization is necessary but not sufficient for downstream access

- •


Delegation can be revoked at any point in the chain


No widely deployed authorization system provides a complete solution to this in the context of autonomous agent-to-agent delegation. The confused deputy problem — where an agent is tricked into misusing its authority on behalf of an unauthorized principal — is a classical formulation of this failure mode, and has been identified in multi-agent LLM systems specifically (Anonymous, [2026](https://arxiv.org/html/2605.05440v1#bib.bib26 "SEAgent: mandatory access control for multi-agent LLM systems")). However, emerging work on invocation-bound capability tokens (Prakash, [2026](https://arxiv.org/html/2605.05440v1#bib.bib13 "AIP: invocation-bound capability tokens with Biscuit and Datalog")) and post-quantum delegation chains (Chen, [2026](https://arxiv.org/html/2605.05440v1#bib.bib17 "AITH: post-quantum continuous delegation for AI agents")) demonstrates that the token-level mechanisms are feasible. Prakash ( [2026](https://arxiv.org/html/2605.05440v1#bib.bib13 "AIP: invocation-bound capability tokens with Biscuit and Datalog")) achieves 0.049ms per-boundary verification with append-only attenuation, and Chen ( [2026](https://arxiv.org/html/2605.05440v1#bib.bib17 "AITH: post-quantum continuous delegation for AI agents")) provides Tamarin-verified revocation within one second. What remains is integration into a workflow-scoped authorization architecture.

#### 5.2.2 Aggregation Inference

Even when each individual data access in a workflow is independently authorized, the synthesis of results may produce information that no individual access would expose. This is the aggregation inference problem.

Formally: given authorized accesses to resources d1,d2,…,djd\_{1},d\_{2},\\ldots,d\_{j} and a synthesis function

|     |     |     |
| --- | --- | --- |
|  | f​(d1,d2,…,dj)→r,f(d\_{1},d\_{2},\\ldots,d\_{j})\\rightarrow r, |  |

is the result rr authorized for the requesting principal?

This problem is not new — it appears in statistical database security and classified information handling (the “mosaic effect”). But it takes on new dimensions in agentic AI because:

- •


The synthesis function ff is a neural network whose behavior is not formally specified

- •


The set of accessed resources may not be known in advance (agents may discover and access resources dynamically)

- •


The requesting principal may not know what resources contributed to the result


Recent empirical work confirms that aggregation inference is not merely theoretical. The Semantic Intent Fragmentation attack (Anonymous, [2026](https://arxiv.org/html/2605.05440v1#bib.bib22 "Semantic intent fragmentation: aggregation attacks on agentic AI systems")) achieves a 71% success rate across 14 enterprise scenarios by decomposing legitimate requests into individually benign subtasks that jointly violate security policy. Li ( [2026](https://arxiv.org/html/2605.05440v1#bib.bib23 "Agentic deanonymization")) demonstrates that LLM agents can link anonymized interview data to specific individuals through individually authorized web searches, establishing aggregation inference as a practical privacy attack. These results elevate aggregation inference from a known theoretical concern to a demonstrated exploitation technique.

The aggregation inference problem is genuinely unsolved in the general case. What can be addressed architecturally is (a) making the set of contributing resources inspectable after the fact, (b) defining policy boundaries that limit which resource combinations are permitted, and (c) tracking causal dependencies through the synthesis graph — an approach demonstrated by the PCAS dependency-graph monitor (Palumbo et al., [2026](https://arxiv.org/html/2605.05440v1#bib.bib16 "PCAS: policy compiler for agentic systems")), which improves policy compliance from 48% to 93%.

#### 5.2.3 Temporal Validity

Multi-agent workflows execute over time. A workflow initiated at time t0t\_{0} may not complete until tnt\_{n}. Authorization state may change during execution: a relationship tuple may be revoked, a principal’s role may change, a data resource may be reclassified.

The question is: at what time is authorization evaluated?

- •


Initiation-time: authorization is checked when the workflow starts and assumed valid throughout. This is simple but may permit access to data that was subsequently restricted.

- •


Access-time: authorization is checked at each data retrieval. This is correct but may cause workflows to fail mid-execution, requiring partial rollback.

- •


Completion-time: authorization is checked before results are returned to the initiating principal. This prevents unauthorized delivery but may waste compute on workflows whose results cannot be disclosed.


Each policy has different failure modes and different implications for the recovery constraint defined in (Tallam, [2026e](https://arxiv.org/html/2605.05440v1#bib.bib1 "Machine-speed accountability: a constraint-aware reference model for oversight-heavy ai")). The choice is a governance decision, not a purely technical one.

Parakhin ( [2026](https://arxiv.org/html/2605.05440v1#bib.bib15 "The bureaucracy of speed: capability coherence systems for agent authorization")) demonstrates quantitatively why time-based revocation (the JWT TTL model) fails at agent execution speeds. Mapping CPU cache coherence protocols to authorization revocation, the analysis shows that TTL-based approaches produce unauthorized operations scaling as O​(v⋅T​T​L)O(v\\cdot TTL) where vv is agent velocity, while execution-count-based Release Consistency bounds violations at Dr​c​c≤nD\_{rcc}\\leq n independent of velocity — a 120×\\times reduction. This argues strongly against initiation-time evaluation for any system where agents operate at machine speed, and suggests that access-time evaluation with execution-count-based validity checks is the architecturally sound default.

### 5.3 A Worked Authorization Chain

Consider a due-diligence workflow with four principals: a human analyst, an orchestrating agent, a retrieval agent, and a synthesis agent.

1. 1.


The analyst asks for a summary of liabilities that could materially change valuation.

2. 2.


The orchestrator decomposes the request into financial retrieval, legal-annex retrieval, and review-committee memo retrieval.

3. 3.


The retrieval agent has access to the deal room, but not to the restricted review-committee workspace that contains a contingent-liability memo.

4. 4.


A synthesis agent combines the retrieved materials and returns a valuation-risk summary to the analyst.


Every stage raises a different authorization question. The orchestrator may be allowed to delegate the legal-annex retrieval but not the restricted memo retrieval. The retrieval agent may be allowed to access each visible corpus independently while still lacking authority to create a cross-boundary synthesis context. The synthesis agent may be permitted to read both outputs only if the delegated scope remains intact and no boundary has been crossed under stale authority. The analyst may be authorized to receive a partial result, but not a result presented as complete when a material source was excluded.

This is the core reason authorization propagation is not reducible to per-request authentication or per-access policy checks. The governable object is the chain itself: who initiated it, which authority was delegated, what data crossed which boundaries, what was combined, and under what validity regime that combination remained authorized.

## 6 Why Existing Authorization Models Are Insufficient

### 6.1 RBAC (Role-Based Access Control)

RBAC (Sandhu et al., [1996](https://arxiv.org/html/2605.05440v1#bib.bib35 "Role-based access control models")) assigns permissions to roles, and roles to users. It does not model relationships between resources, does not support transitive delegation natively, and cannot express “this agent may access this dataset only when acting on behalf of a specific user within a specific workflow.” The granularity is wrong for multi-agent authorization.

### 6.2 ABAC (Attribute-Based Access Control)

ABAC evaluates access decisions based on attributes of the subject, resource, action, and environment. It is more expressive than RBAC but treats each access decision independently. It does not model the _chain_ of accesses that constitutes a multi-agent workflow, and cannot express constraints on the aggregation of individually authorized accesses. XACML obligation policies (OASIS, [2013](https://arxiv.org/html/2605.05440v1#bib.bib36 "eXtensible access control markup language (XACML) version 3.0")) can trigger actions upon access denial, but obligations are evaluated per-access, not per-workflow — they cannot enforce constraints that span the full delegation and synthesis graph.

### 6.3 ReBAC (Relationship-Based Access Control)

ReBAC is the closest existing model to what multi-agent authorization requires. Its graph-based relationship model can express delegation, group membership, and hierarchical access. However, as currently specified and implemented:

- •


Relationships are between human principals and static resources. Non-human agent principals are not first-class entities in most ReBAC schemas.

- •


Delegation is modeled as a static relationship, not as a dynamic, workflow-scoped authority transfer.

- •


There is no native concept of workflow-scoped authorization that binds a set of accesses together and constrains their aggregation.

- •


Temporal validity is handled through tuple creation and deletion, not through workflow-aware authorization epochs.


ReBAC provides the right _primitives_ — relationship tuples, graph-based permission evaluation, fine-grained resource binding — but requires extension to address authorization propagation in multi-agent contexts.

### 6.4 Emerging Models and Remaining Gaps

The frameworks surveyed in Section 2.4 address fragments of the problem space. IBCTs (Prakash, [2026](https://arxiv.org/html/2605.05440v1#bib.bib13 "AIP: invocation-bound capability tokens with Biscuit and Datalog")) solve per-boundary delegation with attenuation. PAuth (Sharma et al., [2026](https://arxiv.org/html/2605.05440v1#bib.bib14 "PAuth: precise task-scoped authorization for AI agents")) solves task-scoped authorization derivation. PCAS (Palumbo et al., [2026](https://arxiv.org/html/2605.05440v1#bib.bib16 "PCAS: policy compiler for agentic systems")) solves causal dependency tracking. AITH (Chen, [2026](https://arxiv.org/html/2605.05440v1#bib.bib17 "AITH: post-quantum continuous delegation for AI agents")) solves post-quantum revocation. No single framework satisfies all seven structural requirements (Section [8](https://arxiv.org/html/2605.05440v1#S8 "8 Structural Requirements ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure")).

The gap is integration. A sufficient authorization architecture for multi-agent AI must compose: (a) append-only delegated authority (IBCTs), (b) task-scoped authorization derivation (PAuth/NL-slices), (c) causal dependency tracking for aggregation (PCAS), (d) execution-count-based temporal validity (Parakhin, [2026](https://arxiv.org/html/2605.05440v1#bib.bib15 "The bureaucracy of speed: capability coherence systems for agent authorization")), and (e) workflow-scoped traces (R5). Whether these mechanisms can be composed without introducing new failure modes is an open architectural question.

## 7 Instantiating the Accountability Constraints

The companion paper (Tallam, [2026e](https://arxiv.org/html/2605.05440v1#bib.bib1 "Machine-speed accountability: a constraint-aware reference model for oversight-heavy ai")) defines four constraints for oversight-heavy AI: traceability, auditability, controllability, and recovery. Authorization propagation provides a specific, technically demanding instantiation of each.

### 7.1 Traceability

For authorization propagation, traceability requires that the system can reconstruct:

- •


The initiating principal and their authorization state at workflow initiation

- •


The delegation chain: which agent delegated to which, with what authority transfer

- •


The data access chain: which agent accessed which resource, under what authorization, at what time

- •


The synthesis chain: which results were combined, by which agent, to produce the final output


This is more demanding than logging individual API calls. It requires a _workflow-scoped authorization trace_ that links the initiating authority to every downstream access and synthesis.

### 7.2 Auditability

An independent reviewer must be able to inspect the authorization trace and determine:

- •


Whether each individual access was authorized at the time it occurred

- •


Whether the delegation chain was valid (no privilege escalation, no stale authority)

- •


Whether the aggregation of accesses was within policy bounds

- •


Whether the final result was authorized for delivery to the requesting principal


This requires that the authorization trace is self-contained — the reviewer should not need to replay the workflow or query live authorization state to reach a conclusion. Tamper-evident receipts (Anonymous, [2026](https://arxiv.org/html/2605.05440v1#bib.bib30 "AARM: action classification with tamper-evident receipts")) provide one mechanism for ensuring trace integrity.

### 7.3 Controllability

The system must be able to:

- •


Deny a downstream agent access even if the upstream agent was authorized (least privilege at each hop, not inherited privilege)

- •


Pause or terminate a workflow when an authorization boundary is crossed mid-execution

- •


Degrade gracefully: return partial results from authorized sources rather than failing entirely or returning unauthorized results


### 7.4 Recovery

When an authorization violation is discovered retroactively:

- •


The system must be able to identify all downstream results that were derived from the unauthorized access

- •


Results that were delivered to principals must be flaggable for review

- •


Authorization tuples must be correctable, and the correction must propagate to prevent recurrence


The difficulty of recovery scales with the depth and breadth of the agent chain. A single unauthorized access at an early hop may taint every downstream result. This is why authorization propagation must be treated as a design-time architectural concern, not a runtime patching exercise.

## 8 Structural Requirements

We do not propose a specific authorization architecture. We identify the structural requirements that any sufficient architecture must satisfy.

R1. Agent principals must be first-class authorization subjects. Agents must have scoped identities with explicit, bounded permissions. Service accounts with broad access are insufficient.

R2. Delegation must be explicit, bounded, and auditable. When an agent delegates to another agent, the authority transfer must be recorded, scoped to the workflow, and subject to policy constraints. Implicit authority inheritance through shared credentials or ambient permissions violates least privilege.

R3. Authorization must be evaluated at every data retrieval boundary. Not once at workflow initiation, but at every point where an agent accesses a data resource. The evaluation must be against the agent’s effective authority in the context of the current workflow, not against a static permission set.

R4. Aggregation policies must be expressible and enforceable. The system must be able to define constraints on which resource combinations are permitted for a given principal, and enforce those constraints before synthesized results are returned.

R5. Authorization traces must be workflow-scoped and self-contained. The complete authorization history of a workflow — from initiation through every delegation, access, and synthesis — must be capturable as a single, inspectable artifact.

R6. Temporal validity must be a policy decision, not an implementation default. The system must support configurable authorization evaluation policies (initiation-time, access-time, completion-time) with explicit tradeoff documentation.

R7. Recovery must be traceable through the synthesis graph. When an authorization violation is discovered, the system must be able to identify all results derived from the violated access, across all downstream agents and synthesis steps.

## 9 Discussion

### 9.1 The SQL Injection Analogy, Revisited

The informal argument that prompt injection is to agentic AI what SQL injection was to web applications has real merit. SQL injection was solved architecturally by separating data from instructions (parameterized queries), not by trying to sanitize inputs. Prompt injection likely requires an analogous architectural separation — perhaps explicit trust boundary tokens in the model’s input processing, or formal separation of instruction and data channels.

But SQL injection was not the only security problem in web applications. Authentication, authorization, session management, and access control remained hard problems even after parameterized queries were universally adopted. The existence of an architectural fix for the injection vector did not eliminate the need for authorization architecture.

The same applies here. An architectural fix for prompt injection — if achieved — would eliminate one important attack vector. It would not address authorization propagation, because authorization propagation is not caused by adversarial content. It is caused by the structure of multi-agent systems themselves.

### 9.2 The Governance Implication

The companion paper (Tallam, [2026e](https://arxiv.org/html/2605.05440v1#bib.bib1 "Machine-speed accountability: a constraint-aware reference model for oversight-heavy ai")) argues that accountability is a system constraint, not a reporting layer. Authorization propagation provides the clearest illustration of why.

In a single-agent system, authorization is a boundary check. The user is authorized (or not) to access a resource. In a multi-agent system, authorization is a _flow property_ — it must hold at every point in a directed graph of delegations, accesses, and syntheses. Boundary checks are necessary but insufficient. The system must reason about authorization as a property of the workflow, not just of individual accesses.

This is why identity governance is infrastructure. It cannot be added after the agent orchestration architecture is designed. It must be a first-class design constraint, co-equal with the functional requirements of the system. Attempting to retrofit authorization propagation onto an existing multi-agent architecture is analogous to attempting to retrofit encryption into a protocol designed without it — technically possible, but the resulting system is fragile, auditable only with difficulty, and prone to subtle failures.

### 9.3 What Current Platforms Need

For current agentic platforms, the paper’s thesis cashes out into a small set of concrete requirements.

First-class non-human identity and delegation artifacts. Agent identity cannot remain an ambient service-account property. Systems need explicit delegation artifacts that preserve requester identity, delegated scope, and attenuation across hops (Prakash, [2026](https://arxiv.org/html/2605.05440v1#bib.bib13 "AIP: invocation-bound capability tokens with Biscuit and Datalog"); Tallam, [2026c](https://arxiv.org/html/2605.05440v1#bib.bib5 "From can to would: identity-conditioned authorization for delegated agentic action")).

Stable workflow receipts and admission surfaces. If a later reviewer cannot reconstruct which execution path was admitted, narrowed, redirected, or denied, then authorization propagation collapses into guesswork. Shared admission or receipt-bearing surfaces are therefore not mere observability conveniences; they are part of the authorization substrate (Tallam, [2026a](https://arxiv.org/html/2605.05440v1#bib.bib4 "Execution envelopes: a shared admission contract for backend ai execution requests"); Anonymous, [2026](https://arxiv.org/html/2605.05440v1#bib.bib30 "AARM: action classification with tamper-evident receipts")).

A measurable surface for unsafe completeness. One reason authorization failures are under-specified is that many evaluation stacks do not measure them directly. Benchmark work on authorization-limited evidence provides an empirical surface for whether systems silently overclaim completeness, conservatively underclaim, or surface insufficiency in an operationally usable way (Tallam, [2026f](https://arxiv.org/html/2605.05440v1#bib.bib3 "Partial evidence bench: benchmarking authorization-limited evidence in agentic systems"), [b](https://arxiv.org/html/2605.05440v1#bib.bib2 "Fail-and-report: a missing authorization primitive for agentic ai systems")).

A disciplined degraded path. Not every authorization shortfall should become a hard stop, and not every system can tolerate one. But if a platform chooses degradation, it needs a principled degraded path with explicit accountability semantics rather than ambient narrowing and implicit trust transfer (Tallam, [2026b](https://arxiv.org/html/2605.05440v1#bib.bib2 "Fail-and-report: a missing authorization primitive for agentic ai systems")).

### 9.4 What Remains Unsolved

This paper identifies the problem and the structural requirements. It does not claim to solve the aggregation inference problem in the general case — this is an open research question with roots in statistical disclosure control and classified information handling that predates AI systems. Nor does it claim that the temporal validity problem has a single correct policy — the right choice depends on the risk tolerance, operational requirements, and regulatory context of the deploying organization.

The rapid emergence of frameworks surveyed in Section 2.4 demonstrates that the community is converging on the problem. IBCTs (Prakash, [2026](https://arxiv.org/html/2605.05440v1#bib.bib13 "AIP: invocation-bound capability tokens with Biscuit and Datalog")), PAuth (Sharma et al., [2026](https://arxiv.org/html/2605.05440v1#bib.bib14 "PAuth: precise task-scoped authorization for AI agents")), PCAS (Palumbo et al., [2026](https://arxiv.org/html/2605.05440v1#bib.bib16 "PCAS: policy compiler for agentic systems")), and AITH (Chen, [2026](https://arxiv.org/html/2605.05440v1#bib.bib17 "AITH: post-quantum continuous delegation for AI agents")) each solve fragments. But the gap between fragment solutions and a unified authorization propagation architecture is substantial. The MCPSHIELD finding (Anonymous, [2026](https://arxiv.org/html/2605.05440v1#bib.bib25 "MCPSHIELD: threat analysis of MCP tool ecosystem")) — that no single defense covers more than 34% of threats — applies by analogy: no single authorization mechanism addresses all seven structural requirements.

The LLMbda Calculus (Garby et al., [2026](https://arxiv.org/html/2605.05440v1#bib.bib18 "LLMbda calculus: dynamic information-flow control for agentic programming")) offers the most promising formal foundation, with its termination-insensitive noninterference theorem providing the theoretical basis for provable authorization flow guarantees. Whether the formal model can be operationalized into a practical authorization architecture at production scale remains an open question.

What this paper does claim is that these problems must be _named_, _distinguished from prompt injection_, and _addressed architecturally_ rather than assumed away.

### 9.5 Limits and Non-Goals

This paper does not present a complete deployment architecture, and its claims are narrower than they may first appear.

- •


It does not solve aggregation inference in the general case. It identifies why it becomes unavoidable in multi-agent systems and what a sufficient architecture must make inspectable.

- •


It does not replace prompt-injection defenses. A system may solve authorization propagation badly, well, or not at all independently of its content-integrity posture.

- •


It does not propose a final policy language. The paper is about architectural requirements, not about a complete syntax or theorem of authorization composition.

- •


It does not assume agents are stable units. In practice, mutable orchestration, runtime rebinding, and self-modifying agents complicate identity continuity further (Tallam, [2026d](https://arxiv.org/html/2605.05440v1#bib.bib6 "Layered mutability: identity drift and governance in self-modifying ai agents")). That complication is acknowledged here, not solved here.


### 9.6 Preliminary Evidence from Implementation

While this paper does not propose a specific authorization architecture, we have observed the structural requirements articulated in Section [8](https://arxiv.org/html/2605.05440v1#S8 "8 Structural Requirements ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure") being violated in a production enterprise AI platform during a stabilization cycle. These violations were not the result of adversarial action. They arose from normal system operation — configuration, integration, and error-handling decisions made by competent engineers under ordinary conditions. The bugs were identified and fixed through standard development process. We report them here not as failures of engineering quality but as empirical evidence that the authorization propagation problem produces real, observable consequences in real systems.

#### 9.6.1 Silent Scope Widening Under Session Failure

A reverse-proxy gateway delegated authentication to an external auth service via a ForwardAuth mechanism. When session binding to a specific collaboration workspace failed, the middleware silently fell back from workspace-scoped authentication to a global authentication context.

This is a temporal validity violation (Section [5.2.3](https://arxiv.org/html/2605.05440v1#S5.SS2.SSS3 "5.2.3 Temporal Validity ‣ 5.2 The Three Sub-Problems ‣ 5 Authorization Propagation: The Formal Problem ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure")). The authorization scope established at session initiation became invalid when the binding failed, but the system continued operating under a wider scope. The user was authenticated but not scoped. Subsequent requests accessed resources outside the user’s intended authorization boundary.

The fix required fail-closed behavior at the middleware layer: if workspace session binding fails, the request fails. The system must not continue under a wider scope.

Structural requirement violated: R3 (authorization at every data retrieval boundary) and R6 (temporal validity as policy decision). The middleware defaulted to a permissive fallback rather than treating scope loss as an authorization failure.

#### 9.6.2 Delegation Binding Reported as Successful When It Was Not

A collaboration workspace entry API returned HTTP 200 (success) even when the session binding that should establish workspace-scoped authorization context failed to complete. Subsequent user actions proceeded without workspace-scoped authorization, operating in an unscoped context while the user believed workspace isolation was active.

This is a transitive delegation failure (Section [5.2.1](https://arxiv.org/html/2605.05440v1#S5.SS2.SSS1 "5.2.1 Transitive Delegation ‣ 5.2 The Three Sub-Problems ‣ 5 Authorization Propagation: The Formal Problem ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure")). The user delegates authority to the workspace context. If the delegation binding fails but the system reports success, every subsequent action carries authority that was never properly established. The delegation is nominal but not actual.

The fix required treating session binding as a precondition, not an optimization. If the binding fails, the entry fails.

Structural requirement violated: R2 (delegation must be explicit, bounded, and auditable). The system reported successful delegation when no delegation had occurred. The audit record showed a delegation that did not exist in practice.

#### 9.6.3 Infrastructure Identity Gap

Extension components (agent containers that operate within the platform) were not built through an attested build pipeline. The platform’s application-layer identity mechanism (trusted requester context) verified the caller’s identity at the service layer, but the infrastructure layer — the container image itself — was not attested. An extension container could be built from an unverified image while still presenting valid application-layer credentials.

This is an identity integrity gap. R2 requires that delegation is auditable and bounded; a delegation chain that includes an unattested container has a gap in the identity proof. The application layer says “this request comes from Extension X.” But the infrastructure layer cannot attest that Extension X is the genuine, unmodified extension.

The fix adopted a dual-build pattern using attested base images, closing the identity chain from application layer to infrastructure layer.

Structural requirement implicated: R2 (delegation auditable) and R5 (authorization traces self-contained). The trace was incomplete because it could not prove the infrastructure-layer identity of the delegating component.

#### 9.6.4 Observations

Three observations emerge from these cases:

First, all three violations arose from normal system operation, not from adversarial action. This confirms the paper’s argument that authorization propagation is an architectural problem, not an attack-vector problem. No adversary was involved. The system drifted into authorization-violating states through reasonable engineering decisions (graceful degradation under failure, optimistic success reporting, independent build pipelines).

Second, all three violations produced the same class of outcome: a principal operated with authorization broader than intended, without visibility into the discrepancy. This is the unauthorized-data-exposure-without-breach scenario described in Section 4.1. It supports the convergence thesis: whether the cause is internal drift or external attack, the failure presents identically at the authorization layer.

Third, the fixes all converged on the same pattern: fail closed at the boundary, treat authorization preconditions as preconditions rather than optimizations, and close identity gaps in the enforcement chain. This is consistent with the paper’s argument that authorization propagation demands infrastructure-grade enforcement, not policy-layer mitigation.

We note that three cases from a single system do not constitute proof of the formal model. But they demonstrate that the structural requirements (R1–R7) identify real failure modes in production systems, and that violations of these requirements produce the authorization-boundary failures the model predicts.

## 10 Future Work

Several next steps would make the paper’s argument more operational and more falsifiable.

Interoperable delegation carriers. The field needs delegation artifacts that survive across model, tool, service, and container boundaries without collapsing back into ambient credentials. Existing token and envelope proposals point in that direction, but interoperability remains open (Prakash, [2026](https://arxiv.org/html/2605.05440v1#bib.bib13 "AIP: invocation-bound capability tokens with Biscuit and Datalog"); Sharma et al., [2026](https://arxiv.org/html/2605.05440v1#bib.bib14 "PAuth: precise task-scoped authorization for AI agents"); Tallam, [2026a](https://arxiv.org/html/2605.05440v1#bib.bib4 "Execution envelopes: a shared admission contract for backend ai execution requests")).

Authorization-aware evaluation. Current agent benchmarks over-index on capability and under-specify governance failures. A more complete evaluation program should measure silent narrowing, unsafe completeness, delegation drift, and stale-authority behavior under realistic task decompositions (Tallam, [2026f](https://arxiv.org/html/2605.05440v1#bib.bib3 "Partial evidence bench: benchmarking authorization-limited evidence in agentic systems")).

Mutable-agent identity. As agents become more stateful, updatable, and self-modifying, the question “what is the same principal over time?” becomes materially harder. Authorization propagation and identity drift should be studied together rather than treated as separate concerns (Tallam, [2026d](https://arxiv.org/html/2605.05440v1#bib.bib6 "Layered mutability: identity drift and governance in self-modifying ai agents")).

Delegated intent models. Multi-agent systems increasingly need to distinguish what an agent technically can do from what it is conditionally authorized to do on behalf of a specific requester. That suggests deeper integration between propagation models and identity-conditioned delegation work (Tallam, [2026c](https://arxiv.org/html/2605.05440v1#bib.bib5 "From can to would: identity-conditioned authorization for delegated agentic action")).

## 11 Conclusion

The security discourse around multi-agent AI systems has concentrated on prompt injection as the singular novel challenge. This paper argues that authorization propagation is a distinct, complementary problem that persists even under the assumption of perfect prompt injection defense. It arises not from adversarial content but from the structure of multi-agent systems: non-human principals making chains of autonomous decisions involving data retrieval, delegation, and synthesis across authorization boundaries.

We have presented a taxonomy distinguishing attack vectors from architectural problems, formalized authorization propagation and its three sub-problems (transitive delegation, aggregation inference, and temporal validity), shown where existing authorization models are insufficient, and identified seven structural requirements for authorization architectures in multi-agent AI systems. Preliminary implementation evidence from a production platform confirms that these requirements identify real failure modes, and that violations produce the authorization-boundary failures the model predicts.

The rapid emergence of fragment solutions demonstrates that the community is converging on the problem. Recent examples include invocation-bound capability tokens (Prakash, [2026](https://arxiv.org/html/2605.05440v1#bib.bib13 "AIP: invocation-bound capability tokens with Biscuit and Datalog")), task-scoped authorization envelopes (Sharma et al., [2026](https://arxiv.org/html/2605.05440v1#bib.bib14 "PAuth: precise task-scoped authorization for AI agents")), execution-count revocation (Parakhin, [2026](https://arxiv.org/html/2605.05440v1#bib.bib15 "The bureaucracy of speed: capability coherence systems for agent authorization")), dependency-graph enforcement (Palumbo et al., [2026](https://arxiv.org/html/2605.05440v1#bib.bib16 "PCAS: policy compiler for agentic systems")), and formally verified delegation protocols (Chen, [2026](https://arxiv.org/html/2605.05440v1#bib.bib17 "AITH: post-quantum continuous delegation for AI agents")). The gap between these fragments and a unified authorization propagation architecture is the central open challenge.

The central claim is that identity governance must be treated as infrastructure — evaluated continuously, enforced at every interaction boundary, and designed into the system from the start. Companion work on machine-speed accountability (Tallam, [2026e](https://arxiv.org/html/2605.05440v1#bib.bib1 "Machine-speed accountability: a constraint-aware reference model for oversight-heavy ai")), fail-and-report (Tallam, [2026b](https://arxiv.org/html/2605.05440v1#bib.bib2 "Fail-and-report: a missing authorization primitive for agentic ai systems")), execution envelopes (Tallam, [2026a](https://arxiv.org/html/2605.05440v1#bib.bib4 "Execution envelopes: a shared admission contract for backend ai execution requests")), and authorization-limited evidence evaluation (Tallam, [2026f](https://arxiv.org/html/2605.05440v1#bib.bib3 "Partial evidence bench: benchmarking authorization-limited evidence in agentic systems")) sketches adjacent pieces of that infrastructure. The alternative — treating authorization as a policy layer applied after the agent architecture is built — produces systems that are structurally prone to unauthorized data exposure through normal operation, independent of any adversarial action.

## Acknowledgments

This paper benefited from informal discussions with colleagues working on agentic AI security, model evaluation, and enterprise authorization systems. The SQL injection analogy in Section 8.1 was crystallized in a particularly heated conversation about whether prompt injection is the only novel security problem in agentic AI. The answer, as this paper argues, is: it is the only novel _attack vector_. It is not the only novel _problem_.

## References

- Anonymous (2026)AARM: action classification with tamper-evident receipts.
External Links: 2602.09433Cited by: [§7.2](https://arxiv.org/html/2605.05440v1#S7.SS2.p3.1 "7.2 Auditability ‣ 7 Instantiating the Accountability Constraints ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§9.3](https://arxiv.org/html/2605.05440v1#S9.SS3.p3.1 "9.3 What Current Platforms Need ‣ 9 Discussion ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- D. E. Bell and L. J. LaPadula (1973)Secure computer systems: mathematical foundations.
Technical reportTechnical Report MTR-2547, MITRE Corporation.
Cited by: [§2.2](https://arxiv.org/html/2605.05440v1#S2.SS2.p1.1 "2.2 Classical Access Control Models ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- A. Benameur et al. (2025)OIDC-A: openid connect for agents 1.0.
External Links: 2509.25974Cited by: [§2.4](https://arxiv.org/html/2605.05440v1#S2.SS4.SSS0.Px5.p1.1 "Standards-track proposals. ‣ 2.4 Emerging Agent Authorization Frameworks ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- P. Bhattarai and T. Vu (2026)Deterministic architectural boundaries for agentic AI.
External Links: 2602.09947Cited by: [§3.3](https://arxiv.org/html/2605.05440v1#S3.SS3.p5.1 "3.3 Why the Distinction Matters ‣ 3 A Taxonomy: Attack Vectors and Architectural Problems ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- K. J. Biba (1977)Integrity considerations for secure computer systems.
Technical reportTechnical Report MTR-3153, MITRE Corporation.
Cited by: [§2.2](https://arxiv.org/html/2605.05440v1#S2.SS2.p1.1 "2.2 Classical Access Control Models ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- Z. Chen (2026)AITH: post-quantum continuous delegation for AI agents.
External Links: 2604.07695Cited by: [§11](https://arxiv.org/html/2605.05440v1#S11.p3.1 "11 Conclusion ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§2.5](https://arxiv.org/html/2605.05440v1#S2.SS5.p2.1 "2.5 Formal Methods for Agent Security ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§5.2.1](https://arxiv.org/html/2605.05440v1#S5.SS2.SSS1.p4.1 "5.2.1 Transitive Delegation ‣ 5.2 The Three Sub-Problems ‣ 5 Authorization Propagation: The Formal Problem ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§6.4](https://arxiv.org/html/2605.05440v1#S6.SS4.p1.1 "6.4 Emerging Models and Remaining Gaps ‣ 6 Why Existing Authorization Models Are Insufficient ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§9.4](https://arxiv.org/html/2605.05440v1#S9.SS4.p2.1 "9.4 What Remains Unsolved ‣ 9 Discussion ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- D. D. Clark and D. R. Wilson (1987)A comparison of commercial and military computer security policies.
In Proc. IEEE Symposium on Security and Privacy,
Cited by: [§2.2](https://arxiv.org/html/2605.05440v1#S2.SS2.p1.1 "2.2 Classical Access Control Models ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- Anonymous (2026)Claude Code permission system evaluation.
External Links: 2604.04978Cited by: [§2.1](https://arxiv.org/html/2605.05440v1#S2.SS1.p4.1 "2.1 Prompt Injection and Agent Security ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- G. Debenedetti et al. (2026)Prompt injection as role confusion.
Note: MITExternal Links: 2603.12277Cited by: [§2.1](https://arxiv.org/html/2605.05440v1#S2.SS1.p4.1 "2.1 Prompt Injection and Agent Security ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- Google DeepMind (2026)AI Agent Traps: a taxonomy of attacks on AI agents.
Note: Technical reportCited by: [§2.1](https://arxiv.org/html/2605.05440v1#S2.SS1.p1.1 "2.1 Prompt Injection and Agent Security ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§4.1](https://arxiv.org/html/2605.05440v1#S4.SS1.SSS0.Px2.p1.1 "External attack. ‣ 4.1 The Convergence Thesis ‣ 4 Identity Governance as Infrastructure ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- S. Garby, A. D. Gordon, and D. Sands (2026)LLMbda calculus: dynamic information-flow control for agentic programming.
External Links: 2602.20064Cited by: [§2.5](https://arxiv.org/html/2605.05440v1#S2.SS5.p3.1 "2.5 Formal Methods for Agent Security ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§9.4](https://arxiv.org/html/2605.05440v1#S9.SS4.p3.1 "9.4 What Remains Unsolved ‣ 9 Discussion ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- K. Greshake, S. Abdelnabi, S. Mishra, C. Endres, T. Holz, and M. Fritz (2023)Not what you’ve signed up for: compromising real-world LLM-integrated applications with indirect prompt injection.
In Proc. 16th ACM Workshop on Artificial Intelligence and Security (AISec),
Cited by: [§2.1](https://arxiv.org/html/2605.05440v1#S2.SS1.p1.1 "2.1 Prompt Injection and Agent Security ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- S. Gruskovnjak (2023)Indirect prompt injection via web search.
Note: Technical writeupCited by: [§2.1](https://arxiv.org/html/2605.05440v1#S2.SS1.p1.1 "2.1 Prompt Injection and Agent Security ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- International Organization for Standardization (2023)ISO/IEC 42001:2023 information technology — artificial intelligence — management system.
Technical reportISO/IEC.
Cited by: [§2.2](https://arxiv.org/html/2605.05440v1#S2.SS2.p3.1 "2.2 Classical Access Control Models ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- T. Li (2026)Agentic deanonymization.
External Links: 2601.05918Cited by: [§2.6](https://arxiv.org/html/2605.05440v1#S2.SS6.SSS0.Px2.p1.1 "Agentic deanonymization. ‣ 2.6 Empirical Evidence of Authorization Failures ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§5.2.2](https://arxiv.org/html/2605.05440v1#S5.SS2.SSS2.p5.1 "5.2.2 Aggregation Inference ‣ 5.2 The Three Sub-Problems ‣ 5 Authorization Propagation: The Formal Problem ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- S. Maiti (2026)Healthcare zero trust: production deployment of autonomous AI agents.
External Links: 2603.17419Cited by: [§2.6](https://arxiv.org/html/2605.05440v1#S2.SS6.SSS0.Px3.p1.1 "Production deployment evidence. ‣ 2.6 Empirical Evidence of Authorization Failures ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- Anonymous (2026)MCPSHIELD: threat analysis of MCP tool ecosystem.
External Links: 2604.05969Cited by: [§2.6](https://arxiv.org/html/2605.05440v1#S2.SS6.SSS0.Px4.p1.1 "MCP threat landscape. ‣ 2.6 Empirical Evidence of Authorization Failures ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§9.4](https://arxiv.org/html/2605.05440v1#S9.SS4.p2.1 "9.4 What Remains Unsolved ‣ 9 Discussion ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- National Institute of Standards and Technology (2023)Artificial intelligence risk management framework (AI RMF 1.0).
Technical reportTechnical Report AI 100-1, NIST.
Cited by: [§2.2](https://arxiv.org/html/2605.05440v1#S2.SS2.p3.1 "2.2 Classical Access Control Models ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- OpenID Foundation (2025)Agentic identity whitepaper.
External Links: 2510.25819Cited by: [§2.4](https://arxiv.org/html/2605.05440v1#S2.SS4.SSS0.Px5.p1.1 "Standards-track proposals. ‣ 2.4 Emerging Agent Authorization Frameworks ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- A. Palumbo, S. Jha, et al. (2026)PCAS: policy compiler for agentic systems.
External Links: 2602.16708Cited by: [§11](https://arxiv.org/html/2605.05440v1#S11.p3.1 "11 Conclusion ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§2.4](https://arxiv.org/html/2605.05440v1#S2.SS4.SSS0.Px4.p1.1 "Dependency-graph policy enforcement. ‣ 2.4 Emerging Agent Authorization Frameworks ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§5.2.2](https://arxiv.org/html/2605.05440v1#S5.SS2.SSS2.p6.1 "5.2.2 Aggregation Inference ‣ 5.2 The Three Sub-Problems ‣ 5 Authorization Propagation: The Formal Problem ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§6.4](https://arxiv.org/html/2605.05440v1#S6.SS4.p1.1 "6.4 Emerging Models and Remaining Gaps ‣ 6 Why Existing Authorization Models Are Insufficient ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§9.4](https://arxiv.org/html/2605.05440v1#S9.SS4.p2.1 "9.4 What Remains Unsolved ‣ 9 Discussion ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- R. Pang, R. Caceres, M. Burrows, Z. Chen, P. Dave, N. Germer, A. Golynski, K. Graney, N. Kang, L. Kissner, et al. (2019)Zanzibar: google’s consistent, global authorization system.
In USENIX Annual Technical Conference (ATC),
Cited by: [§2.3](https://arxiv.org/html/2605.05440v1#S2.SS3.p1.1 "2.3 Relationship-Based Access Control ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- V. Parakhin (2026)The bureaucracy of speed: capability coherence systems for agent authorization.
External Links: 2603.09875Cited by: [§11](https://arxiv.org/html/2605.05440v1#S11.p3.1 "11 Conclusion ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§2.4](https://arxiv.org/html/2605.05440v1#S2.SS4.SSS0.Px3.p1.3 "Capability coherence via execution counting. ‣ 2.4 Emerging Agent Authorization Frameworks ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§5.2.3](https://arxiv.org/html/2605.05440v1#S5.SS2.SSS3.p5.4 "5.2.3 Temporal Validity ‣ 5.2 The Three Sub-Problems ‣ 5 Authorization Propagation: The Formal Problem ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§6.4](https://arxiv.org/html/2605.05440v1#S6.SS4.p2.1 "6.4 Emerging Models and Remaining Gaps ‣ 6 Why Existing Authorization Models Are Insufficient ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- S. Prakash (2026)AIP: invocation-bound capability tokens with Biscuit and Datalog.
External Links: 2603.24775Cited by: [§10](https://arxiv.org/html/2605.05440v1#S10.p2.1 "10 Future Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§11](https://arxiv.org/html/2605.05440v1#S11.p3.1 "11 Conclusion ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§2.4](https://arxiv.org/html/2605.05440v1#S2.SS4.SSS0.Px1.p1.1 "Invocation-bound capability tokens. ‣ 2.4 Emerging Agent Authorization Frameworks ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§2.4](https://arxiv.org/html/2605.05440v1#S2.SS4.SSS0.Px5.p1.1 "Standards-track proposals. ‣ 2.4 Emerging Agent Authorization Frameworks ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§5.2.1](https://arxiv.org/html/2605.05440v1#S5.SS2.SSS1.p4.1 "5.2.1 Transitive Delegation ‣ 5.2 The Three Sub-Problems ‣ 5 Authorization Propagation: The Formal Problem ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§6.4](https://arxiv.org/html/2605.05440v1#S6.SS4.p1.1 "6.4 Emerging Models and Remaining Gaps ‣ 6 Why Existing Authorization Models Are Insufficient ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§9.3](https://arxiv.org/html/2605.05440v1#S9.SS3.p2.1 "9.3 What Current Platforms Need ‣ 9 Discussion ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§9.4](https://arxiv.org/html/2605.05440v1#S9.SS4.p2.1 "9.4 What Remains Unsolved ‣ 9 Discussion ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- R. S. Sandhu, E. J. Coyne, H. L. Feinstein, and C. E. Youman (1996)Role-based access control models.
IEEE Computer29 (2),  pp. 38–47.
Cited by: [§2.2](https://arxiv.org/html/2605.05440v1#S2.SS2.p2.1 "2.2 Classical Access Control Models ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§6.1](https://arxiv.org/html/2605.05440v1#S6.SS1.p1.1 "6.1 RBAC (Role-Based Access Control) ‣ 6 Why Existing Authorization Models Are Insufficient ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- Anonymous (2026)SEAgent: mandatory access control for multi-agent LLM systems.
External Links: 2601.11893Cited by: [§5.2.1](https://arxiv.org/html/2605.05440v1#S5.SS2.SSS1.p4.1 "5.2.1 Transitive Delegation ‣ 5.2 The Three Sub-Problems ‣ 5 Authorization Propagation: The Formal Problem ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- A. Sharma, R. Jiang, Z. Lin, and L. Chen (2026)PAuth: precise task-scoped authorization for AI agents.
External Links: 2603.17170Cited by: [§10](https://arxiv.org/html/2605.05440v1#S10.p2.1 "10 Future Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§11](https://arxiv.org/html/2605.05440v1#S11.p3.1 "11 Conclusion ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§2.4](https://arxiv.org/html/2605.05440v1#S2.SS4.SSS0.Px2.p1.1 "Task-scoped authorization envelopes. ‣ 2.4 Emerging Agent Authorization Frameworks ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§6.4](https://arxiv.org/html/2605.05440v1#S6.SS4.p1.1 "6.4 Emerging Models and Remaining Gaps ‣ 6 Why Existing Authorization Models Are Insufficient ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§9.4](https://arxiv.org/html/2605.05440v1#S9.SS4.p2.1 "9.4 What Remains Unsolved ‣ 9 Discussion ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- Anonymous (2026)Semantic intent fragmentation: aggregation attacks on agentic AI systems.
Note: Accepted AAAI 2026 Summer SymposiumExternal Links: 2604.08608Cited by: [§2.6](https://arxiv.org/html/2605.05440v1#S2.SS6.SSS0.Px1.p1.1 "Semantic intent fragmentation. ‣ 2.6 Empirical Evidence of Authorization Failures ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§5.2.2](https://arxiv.org/html/2605.05440v1#S5.SS2.SSS2.p5.1 "5.2.2 Aggregation Inference ‣ 5.2 The Three Sub-Problems ‣ 5 Authorization Propagation: The Formal Problem ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- Anonymous (2026)SoK: attack surface of agentic AI.
External Links: 2603.22928Cited by: [§3.2](https://arxiv.org/html/2605.05440v1#S3.SS2.p3.1 "3.2 Architectural Problems ‣ 3 A Taxonomy: Attack Vectors and Architectural Problems ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- D. Song et al. (2026)Formalizing LLM agent security.
Note: UC Berkeley / ETH ZurichExternal Links: 2603.19469Cited by: [§2.5](https://arxiv.org/html/2605.05440v1#S2.SS5.p4.1 "2.5 Formal Methods for Agent Security ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- K. Tallam (2026a)Execution envelopes: a shared admission contract for backend ai execution requests.
Note: Working draftCited by: [§10](https://arxiv.org/html/2605.05440v1#S10.p2.1 "10 Future Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§11](https://arxiv.org/html/2605.05440v1#S11.p4.1 "11 Conclusion ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§9.3](https://arxiv.org/html/2605.05440v1#S9.SS3.p3.1 "9.3 What Current Platforms Need ‣ 9 Discussion ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- K. Tallam (2026b)Fail-and-report: a missing authorization primitive for agentic ai systems.
Note: Working draftCited by: [§11](https://arxiv.org/html/2605.05440v1#S11.p4.1 "11 Conclusion ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§9.3](https://arxiv.org/html/2605.05440v1#S9.SS3.p4.1 "9.3 What Current Platforms Need ‣ 9 Discussion ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§9.3](https://arxiv.org/html/2605.05440v1#S9.SS3.p5.1 "9.3 What Current Platforms Need ‣ 9 Discussion ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- K. Tallam (2026c)From can to would: identity-conditioned authorization for delegated agentic action.
Note: Working draftCited by: [§10](https://arxiv.org/html/2605.05440v1#S10.p5.1 "10 Future Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§9.3](https://arxiv.org/html/2605.05440v1#S9.SS3.p2.1 "9.3 What Current Platforms Need ‣ 9 Discussion ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- K. Tallam (2026d)Layered mutability: identity drift and governance in self-modifying ai agents.
Note: Working draftCited by: [§10](https://arxiv.org/html/2605.05440v1#S10.p4.1 "10 Future Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[4th item](https://arxiv.org/html/2605.05440v1#S9.I1.i4.p1.1 "In 9.5 Limits and Non-Goals ‣ 9 Discussion ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- K. Tallam (2026e)Machine-speed accountability: a constraint-aware reference model for oversight-heavy ai.
Note: Working draftCited by: [§11](https://arxiv.org/html/2605.05440v1#S11.p4.1 "11 Conclusion ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§2.7](https://arxiv.org/html/2605.05440v1#S2.SS7.p1.1 "2.7 The Companion Governance Framework ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§5.2.3](https://arxiv.org/html/2605.05440v1#S5.SS2.SSS3.p4.1 "5.2.3 Temporal Validity ‣ 5.2 The Three Sub-Problems ‣ 5 Authorization Propagation: The Formal Problem ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§7](https://arxiv.org/html/2605.05440v1#S7.p1.1 "7 Instantiating the Accountability Constraints ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§9.2](https://arxiv.org/html/2605.05440v1#S9.SS2.p1.1 "9.2 The Governance Implication ‣ 9 Discussion ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- K. Tallam (2026f)Partial evidence bench: benchmarking authorization-limited evidence in agentic systems.
Note: Working draftCited by: [§10](https://arxiv.org/html/2605.05440v1#S10.p3.1 "10 Future Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§11](https://arxiv.org/html/2605.05440v1#S11.p4.1 "11 Conclusion ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§9.3](https://arxiv.org/html/2605.05440v1#S9.SS3.p4.1 "9.3 What Current Platforms Need ‣ 9 Discussion ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").

- OASIS (2013)eXtensible access control markup language (XACML) version 3.0.
Technical reportOASIS Standard.
Cited by: [§2.2](https://arxiv.org/html/2605.05440v1#S2.SS2.p2.1 "2.2 Classical Access Control Models ‣ 2 Background and Related Work ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"),
[§6.2](https://arxiv.org/html/2605.05440v1#S6.SS2.p1.1 "6.2 ABAC (Attribute-Based Access Control) ‣ 6 Why Existing Authorization Models Are Insufficient ‣ Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure").


BETA
