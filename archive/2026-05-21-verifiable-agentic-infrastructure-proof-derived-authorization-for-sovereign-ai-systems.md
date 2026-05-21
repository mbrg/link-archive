---
date: '2026-05-21'
description: The paper presents a Distributed Trust Framework (DTF) for managing authorization
  in sovereign AI systems. DTF transitions from traditional identity-centric models
  to proof-derived authority, addressing the risks posed by autonomous AI agents creating
  unsafe actions. Key features include Justification Proofs for intent, context, and
  policy evaluation; consensus validation mechanisms involving independent evaluators;
  ephemeral execution identities; and an Evidence Chain for capturing the authorization
  lifecycle. This framework enhances governance, auditability, and operational safety
  in cloud-native environments, crucial for ensuring controlled execution within high-stakes
  automated settings.
link: https://arxiv.org/html/2605.15228v1
tags:
- AI
- evidence chain
- authorization
- distributed trust framework
- cloud infrastructure
title: 'Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign
  AI Systems'
---

Title:

Content selection saved. Describe the issue below:

Description:

[License: CC BY 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2605.15228v1 \[cs.AI\] 13 May 2026

# Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems

Jun He

OpenKedge.io

junhe@openkedge.io

Deying Yu

OpenKedge.io

deying@openkedge.io

###### Abstract

Modern cloud and enterprise systems rely on identity-centric authorization, assuming that callers possessing valid credentials are safe to execute commands. The emergence of autonomous AI agents invalidates this assumption: agents can generate syntactically valid but semantically unsafe actions, making standing privileges a significant operational risk. This risk becomes especially acute in sovereign AI systems, where autonomous agents may interact with cloud infrastructure, regulated data, financial workflows, and national-scale digital services. Governed mutation substrates reduce this risk by interposing on agent actions: agents submit intents, infrastructure evaluates context and policy, and execution is mediated. However, this shifts the trust boundary: how can the decision to authorize an intent be made verifiable, distributed, and replayable?

We introduce a Distributed Trust Framework (DTF), a verification framework for governed mutation systems that computes execution authority from structured, verifiable artifacts. DTF introduces a Justification Proof to encode the admissibility basis of an action, a consensus model for independent evaluation, an ephemeral Execution Identity derived from the approved proof, and an append-only Evidence Chain that preserves the authorization lifecycle. Under stated substrate assumptions, this architecture enforces a compact authorization invariant: no high-stakes execution without a proof object, no derived authority without consensus, and no valid mutation detached from evidence.

We define the model, instantiate it over an OpenKedge-based governed mutation substrate, and show how it maps onto cloud-native environments. By shifting authorization from standing identity to proof-derived authority, DTF provides an infrastructure foundation for making agentic execution governable, auditable, and bounded in sovereign AI deployments.

## 1 Introduction

Modern cloud and enterprise systems rely on identity and access management models that assume callers are rational and trustworthy. In these systems, authorization is fundamentally identity-centric: if a service account possesses sufficient permissions, its requested actions are admitted. This model breaks down when applied to autonomous AI agents. Agents generate actions non-deterministically; they can produce API calls that are syntactically valid but semantically unsafe. Granting them broad, standing permissions creates operational risk.

OpenKedge addresses part of this risk by reframing agent-driven mutation as an intent-governed process \[ [9](https://arxiv.org/html/2605.15228v1#bib.bib13 "OpenKedge: governing agentic mutation with execution-bound safety and evidence chains")\]. Instead of mutating state directly, agents submit proposals. The infrastructure evaluates these proposals against context and policy before allowing execution. OpenKedge is the motivating and concrete substrate in this paper, but the verification problem is broader than any single substrate.

Intent governance leaves a second authorization question: what makes the authorization decision itself verifiable, distributed, and replayable? If the system simply intercepts requests, runs a policy check, and issues a token, it leaves a single point of failure and an unauditable decision gap. What is the stable object that evaluators approve? How is temporary authority derived from the approval record rather than from the caller’s standing role? What must be persisted so that an auditor can later reconstruct why execution authority existed at all?

We answer these questions with a _Distributed Trust Framework_ (DTF) for proof-derived execution. DTF is a verification layer for governed mutation substrates: it assumes that a system already interposes on mutation attempts, and supplies the authorization semantics needed to make approval proof-bound, consensus-gated, and replayable. It adds four verification constructs:

- •


Justification Proofs, structured artifacts that bind intent, context, policy basis, risk, and execution boundary.

- •


Consensus validation, in which independent evaluators attest to the same proof object under explicit governance rules.

- •


Execution Identity, an ephemeral authority token derived from the approved proof rather than from ambient caller privilege.

- •


Evidence Chains, append-only lifecycle records that preserve proof, attestations, authority, execution, and outcome.


DTF has a more specific authorization invariant than ordinary access control: a high-stakes mutation is valid only if its authority can be replayed from recorded proof and approval. In conventional identity and access management, authorization is primarily a property of a principal \[ [15](https://arxiv.org/html/2605.15228v1#bib.bib1 "Role-based access control models"), [11](https://arxiv.org/html/2605.15228v1#bib.bib8 "Guide to attribute based access control (abac) definition and considerations")\]. In zero-trust systems, that principal and its context are checked continuously \[ [14](https://arxiv.org/html/2605.15228v1#bib.bib2 "Zero trust architecture")\]. In DTF, the principal is no longer the main object of trust. The decision lifecycle is.

The paper keeps mechanisms already covered by OpenKedge brief. Section [3.5](https://arxiv.org/html/2605.15228v1#S3.SS5 "3.5 What this paper adds beyond OpenKedge ‣ 3 Distributed Trust Framework ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems") states the boundary precisely: we instantiate DTF over an OpenKedge-based governed mutation substrate while defining a general authorization-verification model for such substrates.

Our contributions are:

- •


a proof-derived authority model for governed agentic mutation;

- •


a consensus semantics for independent approval of authorization artifacts;

- •


a definition of Execution Identity as computed, ephemeral authority;

- •


safety and audit properties for proof-bound, consensus-gated, evidence-preserved execution;

- •


a practical cloud mapping that uses existing temporary credential and audit primitives.


## 2 Related Work

#### Access control and zero trust.

Role-based and attribute-based access control decide whether a principal may perform an action \[ [15](https://arxiv.org/html/2605.15228v1#bib.bib1 "Role-based access control models"), [11](https://arxiv.org/html/2605.15228v1#bib.bib8 "Guide to attribute based access control (abac) definition and considerations")\]. Zero-trust architecture improves this model through continuous verification of requester and context \[ [14](https://arxiv.org/html/2605.15228v1#bib.bib2 "Zero trust architecture")\]. DTF shifts the verification target from the requester to the mutation lifecycle: authority is valid only if it is derived from an approved proof.

#### Automated Reasoning and Verified Permissions.

Modern authorization systems increasingly rely on automated reasoning and formal methods to analyze access invariants. For example, recent frameworks like AWS Cedar encode authorization policies into SMT-solvable formulas to check security properties and use mechanized proofs in Lean to establish properties of the policy engine \[ [5](https://arxiv.org/html/2605.15228v1#bib.bib18 "Cedar: a new language for expressive, fast, safe, and analyzable authorization"), [6](https://arxiv.org/html/2605.15228v1#bib.bib19 "How we built cedar: a verification-guided approach")\]. These systems primarily reason about policy semantics and static authorization decisions. DTF addresses a complementary problem: it structures the runtime authorization lifecycle of autonomous agents so that transient authority is derived from a recorded proof object, checked by independent evaluators, and bounded under stated substrate assumptions before mutation occurs.

#### LLM Agent Safety and Tool-Use Authorization.

The adoption of Large Language Models (LLMs) as autonomous agents has exposed security vulnerabilities, including indirect prompt injection \[ [8](https://arxiv.org/html/2605.15228v1#bib.bib16 "Not what you’ve signed up for: compromising real-world llm-integrated applications with indirect prompt injection")\] and the ability of agents to exploit systems when granted unchecked tool access \[ [7](https://arxiv.org/html/2605.15228v1#bib.bib15 "LLM agents can autonomously hack websites")\]. Recent surveys describe the growing architecture of agent tool-use \[ [16](https://arxiv.org/html/2605.15228v1#bib.bib17 "A survey on large language model based autonomous agents")\]; governing those tools remains unsettled. Early mitigation strategies focused on prompt-level guardrails or strict "human-in-the-loop" approvals for every action. At scale, continuous human oversight becomes a bottleneck. DTF shifts the safety boundary from the prompt to the execution infrastructure. It provides a structured "human-on-the-loop" alternative where independent evaluators—rather than the proposing agent—derive execution authority from structured proof artifacts.

#### Distributed trust.

Consensus and Byzantine fault-tolerant systems study agreement under faulty participants \[ [13](https://arxiv.org/html/2605.15228v1#bib.bib5 "The byzantine generals problem"), [4](https://arxiv.org/html/2605.15228v1#bib.bib6 "Practical byzantine fault tolerance")\]. We do not run consensus over replicated application state. Instead, we use explicit multi-evaluator agreement to decide whether a proof is sufficient to derive execution authority.

#### Provenance and accountability.

Provenance, event sourcing, and accountability systems preserve causal history and support replay or audit \[ [3](https://arxiv.org/html/2605.15228v1#bib.bib7 "Why and where: a characterization of data provenance"), [17](https://arxiv.org/html/2605.15228v1#bib.bib10 "Information accountability"), [12](https://arxiv.org/html/2605.15228v1#bib.bib9 "Designing data-intensive applications")\]. The DTF Evidence Chain—an append-only lifecycle record introduced earlier—specializes this lineage for authorization-bearing mutations by recording not only effects, but the proof object and approval path that produced authority.

#### OpenKedge and Sovereign Agentic Loops.

OpenKedge provides the concrete intent-governed mutation substrate used in this paper’s instantiation \[ [9](https://arxiv.org/html/2605.15228v1#bib.bib13 "OpenKedge: governing agentic mutation with execution-bound safety and evidence chains")\]. The Sovereign Agentic Loops architecture separately develops the decoupling of reasoning from direct execution \[ [10](https://arxiv.org/html/2605.15228v1#bib.bib14 "Sovereign agentic loops: decoupling ai reasoning from execution in real-world systems")\]. DTF is a substrate-agnostic verification layer that formalizes proof construction, consensus-backed approval, and execution identity semantics rather than a replacement for these systems.

## 3 Distributed Trust Framework

In traditional architectures, authorization is largely a static property of a principal: an agent or service account acts under a standing role, and requests are granted if they fall within the permissions of that role. This model breaks down when applied to autonomous AI agents. Because an agent’s behavior is non-deterministic and its reasoning is prone to error or manipulation, granting it broad standing authority creates operational risk.

DTF is a general verification model for intent-governed mutation systems. It assumes a substrate that already interposes on mutation attempts: agents propose intents, the infrastructure binds context and policy, and execution is mediated rather than direct. Any substrate with this interposition point can adopt DTF’s authorization semantics. OpenKedge is the concrete governed mutation substrate used for the implementation and examples in this paper \[ [9](https://arxiv.org/html/2605.15228v1#bib.bib13 "OpenKedge: governing agentic mutation with execution-bound safety and evidence chains")\].

Moving from direct execution to intent governance raises a subsequent verification problem. If intent governance simply means a central policy engine says “yes” or “no” and issues an API key, the system still has a single point of failure and an unauditable decision gap. How is the decision to authorize a mutation made verifiable? What is the stable object that evaluators approve? How is authority bounded to the approved intent, and how is the authorization basis reconstructed after the fact?

The Distributed Trust Framework provides the verification layer above such governed mutation substrates. It models authority not as a standing permission, but as a _derived state_. A proposed mutation does not execute because an agent or service account already has broad permission. It executes only if a recorded proof is approved by independent evaluators and converted into a bounded execution identity.

### 3.1 Model Formulation

We define the Distributed Trust Framework using a formal state-transition model. Let tt denote logical time.

#### Sets and Spaces:

- •


ℐ\\mathcal{I}: Space of canonical intents.

- •


𝒞\\mathcal{C}: Space of authorization-relevant context snapshots.

- •


𝒫\\mathcal{P}: Space of policy bundles.

- •


𝒥\\mathcal{J}: Space of Justification Proofs.

- •


𝒜\\mathcal{A}: Space of attestations.

- •


𝒢\\mathcal{G}: Space of governance metadata.

- •


𝒟={𝖺𝗉𝗉𝗋𝗈𝗏𝖾,𝗋𝖾𝗃𝖾𝖼𝗍,𝖾𝗌𝖼𝖺𝗅𝖺𝗍𝖾}\\mathcal{D}=\\{\\mathsf{approve},\\mathsf{reject},\\mathsf{escalate}\\}: The decision space.

- •


ℰ\\mathcal{E}: Space of Execution Identities.

- •


𝒳,𝒪\\mathcal{X},\\mathcal{O}: Spaces of mutation attempts and observed outcomes, respectively.


#### State Variables:

At any time tt, the system processes an intent It∈ℐI\_{t}\\in\\mathcal{I} against context Ct∈𝒞C\_{t}\\in\\mathcal{C} and policy Pt∈𝒫P\_{t}\\in\\mathcal{P}. This produces a Justification Proof 𝖩𝖯t∈𝒥\\mathsf{JP}\_{t}\\in\\mathcal{J}, a vector of attestations At∈𝒜nA\_{t}\\in\\mathcal{A}^{n} from evaluator set Vt={v1,…,vn}V\_{t}=\\{v\_{1},\\dots,v\_{n}\\}, and a decision Dt∈𝒟D\_{t}\\in\\mathcal{D} using metadata Γt∈𝒢\\Gamma\_{t}\\in\\mathcal{G}. A successful decision materializes an Execution Identity 𝖤𝖨t∈ℰ\\mathsf{EI}\_{t}\\in\\mathcal{E}, leading to an attempt Xt∈𝒳X\_{t}\\in\\mathcal{X} and outcome Ot∈𝒪O\_{t}\\in\\mathcal{O}, durably recorded in an Evidence Chain 𝖤𝖢t\\mathsf{EC}\_{t}.

#### Core Functions:

- •


Proof Construction:f:ℐ×𝒞×𝒫→𝒥f:\\mathcal{I}\\times\\mathcal{C}\\times\\mathcal{P}\\rightarrow\\mathcal{J} generates the proof 𝖩𝖯t=f​(It,Ct,Pt)\\mathsf{JP}\_{t}=f(I\_{t},C\_{t},P\_{t}).

- •


Attestation:vi:𝒥→𝒜v\_{i}:\\mathcal{J}\\rightarrow\\mathcal{A} generates an independent attestation ait=vi​(𝖩𝖯t)a\_{i}^{t}=v\_{i}(\\mathsf{JP}\_{t}).

- •


Consensus Rule:q:𝒜n×𝒢→𝒟q:\\mathcal{A}^{n}\\times\\mathcal{G}\\rightarrow\\mathcal{D} computes the decision Dt=q​(At,Γt)D\_{t}=q(A\_{t},\\Gamma\_{t}).

- •


Authority Derivation:h:𝒥×𝒜n×𝒢→ℰh:\\mathcal{J}\\times\\mathcal{A}^{n}\\times\\mathcal{G}\\rightarrow\\mathcal{E} materializes the bounded identity 𝖤𝖨t=h​(𝖩𝖯t,At,Γt)\\mathsf{EI}\_{t}=h(\\mathsf{JP}\_{t},A\_{t},\\Gamma\_{t}) if Dt=𝖺𝗉𝗉𝗋𝗈𝗏𝖾D\_{t}=\\mathsf{approve}.


### 3.2 Execution Pipeline

The authorization pipeline transforms an intent into a governed execution record. Algorithm [1](https://arxiv.org/html/2605.15228v1#alg1 "Algorithm 1 ‣ 3.2 Execution Pipeline ‣ 3 Distributed Trust Framework ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems") gives the ordered path. The central requirement is causal ordering: proof precedes approval, approval precedes authority, and execution is incomplete until evidence is durably recorded.

Algorithm 1 DTF Authorization and Execution Pipeline

1:Input: Intent ItI\_{t}, Context CtC\_{t}, Policy PtP\_{t}, Evaluator set VtV\_{t}, Metadata Γt\\Gamma\_{t}

2:Output: Evidence Chain 𝖤𝖢t\\mathsf{EC}\_{t}

3:𝖩𝖯t←f​(It,Ct,Pt)\\mathsf{JP}\_{t}\\leftarrow f(I\_{t},C\_{t},P\_{t})⊳\\triangleright Construct Justification Proof

4:for each evaluator vi∈Vtv\_{i}\\in V\_{t}do

5:ait←vi​(𝖩𝖯t)a\_{i}^{t}\\leftarrow v\_{i}(\\mathsf{JP}\_{t})⊳\\triangleright Generate independent attestations

6:endfor

7:At←(a1t,…,ant)A\_{t}\\leftarrow(a\_{1}^{t},\\dots,a\_{n}^{t})

8:Dt←q​(At,Γt)D\_{t}\\leftarrow q(A\_{t},\\Gamma\_{t})⊳\\triangleright Evaluate consensus rule

9:ifDt=𝖺𝗉𝗉𝗋𝗈𝗏𝖾D\_{t}=\\mathsf{approve}then

10:𝖤𝖨t←h​(𝖩𝖯t,At,Γt)\\mathsf{EI}\_{t}\\leftarrow h(\\mathsf{JP}\_{t},A\_{t},\\Gamma\_{t})⊳\\triangleright Derive bounded Execution Identity

11:Bt←𝖡𝗈𝗎𝗇𝖽𝖺𝗋𝗒​(𝖩𝖯t)B\_{t}\\leftarrow\\mathsf{Boundary}(\\mathsf{JP}\_{t})

12:if𝖲𝖼𝗈𝗉𝖾​(𝖤𝖨t)⪯Bt\\mathsf{Scope}(\\mathsf{EI}\_{t})\\preceq B\_{t}then

13:Xt,Ot←Execute​(𝖤𝖨t)X\_{t},O\_{t}\\leftarrow\\text{Execute}(\\mathsf{EI}\_{t})

14:else

15:Xt,Ot←∅,Escalated (Boundary Violation)X\_{t},O\_{t}\\leftarrow\\emptyset,\\text{Escalated (Boundary Violation)}

16:endif

17:else

18:𝖤𝖨t←∅\\mathsf{EI}\_{t}\\leftarrow\\emptyset

19:Xt,Ot←∅,Rejected or EscalatedX\_{t},O\_{t}\\leftarrow\\emptyset,\\text{Rejected or Escalated}

20:endif

21:𝖤𝖢t←(It,Ct,Pt,𝖩𝖯t,At,Γt,Dt,𝖤𝖨t,Xt,Ot)\\mathsf{EC}\_{t}\\leftarrow(I\_{t},C\_{t},P\_{t},\\mathsf{JP}\_{t},A\_{t},\\Gamma\_{t},D\_{t},\\mathsf{EI}\_{t},X\_{t},O\_{t})

22:return𝖤𝖢t\\mathsf{EC}\_{t}

### 3.3 Threat Model and Assumptions

We assume the autonomous agent proposing intents is untrusted. Its internal reasoning, prompts, and local state may be non-deterministic, hallucinated, or compromised by prompt injection. The Trusted Computing Base (TCB) consists of the DTF verification layer (Justification Engine, Evaluation Swarm, Execution Broker, Evidence Store) and the underlying governed mutation substrate (e.g., OpenKedge). We assume the TCB is uncompromised and the substrate correctly interposes on execution. The framework defends against rogue or unsafe agent actions, not against total compromise of the verification infrastructure itself.

### 3.4 System Invariants

To make governance verifiable, DTF enforces four lifecycle invariants. Let Ωt\\Omega\_{t} denote the execution obligations, and Bt=(μt,ρt,τt,Ωt)B\_{t}=(\\mu\_{t},\\rho\_{t},\\tau\_{t},\\Omega\_{t}) be the maximum authority boundary derived from the proof.

#### Constraint 1: Proof-bound Execution.

No governed high-stakes mutation XtX\_{t} may execute without a corresponding valid proof.

|     |     |     |
| --- | --- | --- |
|  | ∀Xt≠∅,∃𝖩𝖯t∈𝒥​ s.t. ​𝖩𝖯t=f​(It,Ct,Pt)\\forall X\_{t}\\neq\\emptyset,\\quad\\exists\\mathsf{JP}\_{t}\\in\\mathcal{J}\\text{ s.t. }\\mathsf{JP}\_{t}=f(I\_{t},C\_{t},P\_{t}) |  |

#### Constraint 2: Consensus-gated Authority.

No valid Execution Identity may be issued unless the consensus explicitly approves the proof.

|     |     |     |
| --- | --- | --- |
|  | 𝖤𝖨t≠∅⟹q​(At,Γt)=𝖺𝗉𝗉𝗋𝗈𝗏𝖾\\mathsf{EI}\_{t}\\neq\\emptyset\\implies q(A\_{t},\\Gamma\_{t})=\\mathsf{approve} |  |

#### Constraint 3: Non-escalation.

The effective authority scope of 𝖤𝖨t\\mathsf{EI}\_{t}, extracted via 𝖲𝖼𝗈𝗉𝖾​(⋅)\\mathsf{Scope}(\\cdot), must be contained within the proof-derived boundary.

|     |     |     |
| --- | --- | --- |
|  | ∀𝖤𝖨t≠∅,𝖲𝖼𝗈𝗉𝖾​(𝖤𝖨t)⪯Bt\\forall\\mathsf{EI}\_{t}\\neq\\emptyset,\\quad\\mathsf{Scope}(\\mathsf{EI}\_{t})\\preceq B\_{t} |  |

#### Constraint 4: Evidence Completeness.

Every intent proposal, regardless of decision outcome, must map to exactly one structurally complete Evidence Chain.

|     |     |     |
| --- | --- | --- |
|  | ∀It∈ℐ,\|𝖤𝖢t\|=1​ where ​𝖤𝖢t​ captures ​(Dt,𝖤𝖨t,Xt,Ot)\\forall I\_{t}\\in\\mathcal{I},\\quad\|\\mathsf{EC}\_{t}\|=1\\text{ where }\\mathsf{EC}\_{t}\\text{ captures }(D\_{t},\\mathsf{EI}\_{t},X\_{t},O\_{t}) |  |

### 3.5 What this paper adds beyond OpenKedge

OpenKedge contributes one governed mutation substrate: intent-governed mutation, context-aware policy evaluation, execution contracts and task-oriented identities, and lineage through the Intent-to-Execution Evidence Chain (IEEC) \[ [9](https://arxiv.org/html/2605.15228v1#bib.bib13 "OpenKedge: governing agentic mutation with execution-bound safety and evidence chains")\]. DTF does not replace that substrate. It is a general authorization-verification layer for governed mutation systems, and OpenKedge is the substrate through which we instantiate and evaluate it.

The delta is the object of authorization. OpenKedge governs whether and how an intent may mutate state. DTF defines the stable object that independent evaluators approve (𝖩𝖯\\mathsf{JP}), the consensus semantics over that object (q​(At,Γt)q(A\_{t},\\Gamma\_{t})), the proof-derived authority that reaches the execution substrate (𝖤𝖨\\mathsf{EI}), and the authorization lifecycle evidence required for later replay (𝖤𝖢\\mathsf{EC}). In the OpenKedge instantiation, a task-oriented identity becomes an Execution Identity only when its authority is derived from a Justification Proof and consensus record; an IEEC becomes a DTF Evidence Chain only when it preserves proof, attestations, issuance, execution, and outcome as a replayable authorization lifecycle.

| Concern | OpenKedge-based substrate | DTF layer in this paper |
| --- | --- | --- |
| Mutation unit | Intent-governed mutation proposal | Justification Proof as stable authorization object |
| Policy path | Context-aware policy evaluation | Consensus validation semantics over proof attestations |
| Execution authority | Contracts and task-oriented identities | Proof-derived Execution Identity |
| Lineage | IEEC records intent-to-execution lineage | Evidence Chain records replayable authorization lifecycle |

The upper path in Figure [1](https://arxiv.org/html/2605.15228v1#S3.F1 "Figure 1 ‣ 3.5 What this paper adds beyond OpenKedge ‣ 3 Distributed Trust Framework ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems") is the generic DTF authorization pipeline; the OpenKedge row is one concrete substrate mapping used in this paper.

IntentGatewayPolicy Engine(Arbiter)ExecutionContractExecutionSubstrateIEEC(Audit Log)JustificationProof 𝖩𝖯t\\mathsf{JP}\_{t}EvaluationSwarm AtA\_{t}ExecutionIdentity 𝖤𝖨t\\mathsf{EI}\_{t}EvidenceChain 𝖤𝖢t\\mathsf{EC}\_{t}constructvalidateapproveauthorizerecordmapsmapsmapsExample Substrate (OpenKedge)DTF Verification PipelineFigure 1: Generic DTF verification pipeline with OpenKedge shown as one substrate mapping. DTF defines proof, evaluator attestations, proof-derived Execution Identity, and Evidence Chain; the OpenKedge row shows the corresponding intent governance, execution contract, task identity, and lineage hooks.

## 4 Justification Proof

A Justification Proof (𝖩𝖯\\mathsf{JP}) is the stable authorization object inspected by evaluators and preserved for replay. It is not a natural-language explanation and not a transcript of the agent’s reasoning. It is a structured decision artifact whose contents are sufficient to determine whether a specific mutation can receive bounded authority.

These properties distinguish Justification Proofs from ordinary audit messages or human-readable explanations. Audit messages are typically post-hoc; they record what happened after the fact. Explanations may be persuasive but are often unverifiable. By contrast, a Justification Proof is an authorization artifact whose role is to make the basis and boundary of execution explicit before authority is issued.

### 4.1 Structure

We represent a proof as

|     |     |     |
| --- | --- | --- |
|  | 𝖩𝖯t=(Mt,St,Πt,Rt,Bt)∈𝒥,\\mathsf{JP}\_{t}=(M\_{t},S\_{t},\\Pi\_{t},R\_{t},B\_{t})\\in\\mathcal{J}, |  |

where MtM\_{t} is the mutation specification, StS\_{t} the bound state and context snapshot, Πt\\Pi\_{t} the policy basis, RtR\_{t} the risk and admissibility assessment, and BtB\_{t} the maximum execution boundary.

Each field has a narrow role:

- •


MtM\_{t} states what mutation is proposed.

- •


StS\_{t} records the authorization-relevant context used at decision time.

- •


Πt\\Pi\_{t} identifies the policies, versions, and constraints applied.

- •


RtR\_{t} classifies risk and required approval strength.

- •


Bt=(μt,ρt,τt,Ωt)B\_{t}=(\\mu\_{t},\\rho\_{t},\\tau\_{t},\\Omega\_{t}) defines the action (μt\\mu\_{t}), resource (ρt\\rho\_{t}), time (τt\\tau\_{t}), and obligation (Ωt\\Omega\_{t}) limits that may be issued if approval succeeds.


The proof may reference richer artifacts such as dependency snapshots, simulation results, or model-generated plans, but its authorization-relevant content must be explicit and machine-inspectable.

### 4.2 Semantics

A valid 𝖩𝖯\\mathsf{JP} satisfies three properties.

#### Explicitness.

Authorization-relevant assumptions must appear in the proof or in referenced immutable artifacts. Hidden model state or informal operator memory is not part of the proof.

#### Re-evaluability.

Given the stored proof, evaluators and auditors can revisit the admissibility judgment without reconstructing the proposing agent’s internal reasoning.

#### Boundary derivation.

The proof determines the maximal authority that could be issued, extracted via the boundary function 𝖡𝗈𝗎𝗇𝖽𝖺𝗋𝗒\\mathsf{Boundary}:

|     |     |     |
| --- | --- | --- |
|  | 𝖡𝗈𝗎𝗇𝖽𝖺𝗋𝗒​(𝖩𝖯t)=Bt.\\mathsf{Boundary}(\\mathsf{JP}\_{t})=B\_{t}. |  |

Approval may narrow this boundary, but issuance may not expand it.

### 4.3 Construction

Proof construction follows four structured steps. Let 𝖭𝗈𝗋𝗆𝖺𝗅𝗂𝗓𝖾\\mathsf{Normalize}, 𝖡𝗂𝗇𝖽𝖢𝗈𝗇𝗍𝖾𝗑𝗍\\mathsf{BindContext}, 𝖤𝗏𝖺𝗅𝗎𝖺𝗍𝖾𝖯𝗈𝗅𝗂𝖼𝗒\\mathsf{EvaluatePolicy}, and 𝖣𝖾𝗋𝗂𝗏𝖾𝖡𝗈𝗎𝗇𝖽𝖺𝗋𝗒\\mathsf{DeriveBoundary} be state-transition functions governing intent processing. The construction of 𝖩𝖯t\\mathsf{JP}\_{t} proceeds as follows:

|     |     |     |     |
| --- | --- | --- | --- |
|  | It′\\displaystyle I^{\\prime}\_{t} | =𝖭𝗈𝗋𝗆𝖺𝗅𝗂𝗓𝖾​(It)\\displaystyle=\\mathsf{Normalize}(I\_{t}) |  |
|  | St\\displaystyle S\_{t} | =𝖡𝗂𝗇𝖽𝖢𝗈𝗇𝗍𝖾𝗑𝗍​(It′,Ct)\\displaystyle=\\mathsf{BindContext}(I^{\\prime}\_{t},C\_{t}) |  |
|  | (Πt,Rt)\\displaystyle(\\Pi\_{t},R\_{t}) | =𝖤𝗏𝖺𝗅𝗎𝖺𝗍𝖾𝖯𝗈𝗅𝗂𝖼𝗒​(St,Pt)\\displaystyle=\\mathsf{EvaluatePolicy}(S\_{t},P\_{t}) |  |
|  | Bt\\displaystyle B\_{t} | =𝖣𝖾𝗋𝗂𝗏𝖾𝖡𝗈𝗎𝗇𝖽𝖺𝗋𝗒​(Πt,Rt)\\displaystyle=\\mathsf{DeriveBoundary}(\\Pi\_{t},R\_{t}) |  |

The proof-construction function ff from our model is defined as the composition of these steps:

|     |     |     |
| --- | --- | --- |
|  | f​(It,Ct,Pt)≜(Mt,St,Πt,Rt,Bt)=𝖩𝖯t,f(I\_{t},C\_{t},P\_{t})\\triangleq(M\_{t},S\_{t},\\Pi\_{t},R\_{t},B\_{t})=\\mathsf{JP}\_{t}, |  |

where the normalized intent It′I^{\\prime}\_{t} serves as the mutation specification MtM\_{t}. In the OpenKedge substrate, this mirrors the intent-governed pipeline but changes the authorization artifact produced by the pipeline. The output is a durable proof object, not a transient “approve” or “deny” token; independent validators can agree, disagree, or escalate over the same artifact.

### 4.4 Example

For a proposed TerminateInstance mutation, MtM\_{t} identifies the action and target instance. StS\_{t} records relevant topology, traffic, ownership, protection tags, and incident state. Πt\\Pi\_{t} identifies policies governing destructive actions and protected resources. RtR\_{t} may mark the action as critical if the instance is on a dependency path. BtB\_{t} either permits no issuance or restricts authority to exactly that instance, action, and time window, possibly with an execution-time obligation to re-check traffic.

The proof replaces a vague claim such as “the instance appears unused” with a replayable authorization object.

## 5 Consensus Validation

A proof alone is a claim. Consensus validation turns that claim into an authorization decision. DTF does not run full Byzantine consensus over replicated application state; it distributes trust over authorization. The question is whether a proof is sufficient to derive bounded execution authority, and the answer must come from an explicit evaluator set rather than one unchecked component.

One evaluator is insufficient because authorization failures are heterogeneous. A policy evaluator may apply the written rule correctly while missing stale topology. A dependency checker may see current state but lack business-risk context. A simulator may model the ordinary case while missing protected-resource policy. A human reviewer may notice operational intent but miss a malformed proof field. Consensus validation is not decorative voting; it prevents any one failure mode from becoming execution authority.

### 5.1 Evaluator Model

Each evaluator vi∈Vtv\_{i}\\in V\_{t} receives the same 𝖩𝖯t\\mathsf{JP}\_{t} and emits an attestation

|     |     |     |
| --- | --- | --- |
|  | ait=vi​(𝖩𝖯t)∈𝒜,a\_{i}^{t}=v\_{i}(\\mathsf{JP}\_{t})\\in\\mathcal{A}, |  |

where 𝒜\\mathcal{A} includes 𝖺𝗉𝗉𝗋𝗈𝗏𝖾\\mathsf{approve}, 𝗋𝖾𝗃𝖾𝖼𝗍\\mathsf{reject}, and 𝖺𝖻𝗌𝗍𝖺𝗂𝗇\\mathsf{abstain}, plus optional structured objections or obligations. For example, an attestation may be represented as

|     |     |     |
| --- | --- | --- |
|  | ait=(vi,dit,ωit),dit∈{𝖺𝗉𝗉𝗋𝗈𝗏𝖾,𝗋𝖾𝗃𝖾𝖼𝗍,𝖺𝖻𝗌𝗍𝖺𝗂𝗇},a\_{i}^{t}=(v\_{i},d\_{i}^{t},\\omega\_{i}^{t}),\\qquad d\_{i}^{t}\\in\\{\\mathsf{approve},\\mathsf{reject},\\mathsf{abstain}\\}, |  |

where ωit\\omega\_{i}^{t} records evaluator-specific annotations such as objections, obligations, or confidence metadata.

Practical deployments should use heterogeneous evaluator classes:

- •


policy evaluators for explicit governance rules;

- •


state evaluators for topology, dependency, and freshness checks;

- •


risk evaluators for blast radius and reversibility;

- •


simulation evaluators for predicted effects;

- •


human-supervised evaluators for elevated or exceptional cases.


Heterogeneity matters only if the consensus rule can observe it. DTF records evaluator class, proof hash, decision, objections, and obligations in AtA\_{t}, and lets Γt\\Gamma\_{t} require specific classes, veto rights, quorum thresholds, or escalation on disagreement.

### 5.2 Consensus Rule

The consensus rule encodes quorum thresholds, required evaluator diversity, veto rights, and risk-sensitive escalation. Let 𝒜+\\mathcal{A}^{+} and 𝒜−\\mathcal{A}^{-} denote the sets of approving and rejecting evaluators, respectively:

|     |     |     |     |
| --- | --- | --- | --- |
|  | 𝒜+\\displaystyle\\mathcal{A}^{+} | ={vi∈Vt∣dit=𝖺𝗉𝗉𝗋𝗈𝗏𝖾}\\displaystyle=\\{v\_{i}\\in V\_{t}\\mid d\_{i}^{t}=\\mathsf{approve}\\} |  |
|  | 𝒜−\\displaystyle\\mathcal{A}^{-} | ={vi∈Vt∣dit=𝗋𝖾𝗃𝖾𝖼𝗍}\\displaystyle=\\{v\_{i}\\in V\_{t}\\mid d\_{i}^{t}=\\mathsf{reject}\\} |  |

Let Vveto⊆VtV\_{\\text{veto}}\\subseteq V\_{t} represent the subset of evaluators granted veto authority for the specific mutation class. The governance metadata Γt\\Gamma\_{t} supplies the risk-adjusted quorum threshold kΓk\_{\\Gamma} and rejection threshold rΓr\_{\\Gamma}. We define the consensus function q:𝒜n×𝒢→𝒟q:\\mathcal{A}^{n}\\times\\mathcal{G}\\rightarrow\\mathcal{D} as:

|     |     |     |
| --- | --- | --- |
|  | q​(At,Γt)={𝗋𝖾𝗃𝖾𝖼𝗍if ​∃vi∈Vveto:dit=𝗋𝖾𝗃𝖾𝖼𝗍​ or ​\|𝒜−\|≥rΓ𝖺𝗉𝗉𝗋𝗈𝗏𝖾if (∄vi∈Vveto:dit=𝗋𝖾𝗃𝖾𝖼𝗍) and \|𝒜−\|<rΓ and \|𝒜+\|≥kΓ𝖾𝗌𝖼𝖺𝗅𝖺𝗍𝖾otherwiseq(A\_{t},\\Gamma\_{t})=\\begin{cases}\\mathsf{reject}&\\text{if }\\exists v\_{i}\\in V\_{\\text{veto}}:d\_{i}^{t}=\\mathsf{reject}\\text{ or }\|\\mathcal{A}^{-}\|\\geq r\_{\\Gamma}\\\<br>\\mathsf{approve}&\\text{if }\\left(\\nexists v\_{i}\\in V\_{\\text{veto}}:d\_{i}^{t}=\\mathsf{reject}\\right)\\text{ and }\|\\mathcal{A}^{-}\|<r\_{\\Gamma}\\text{ and }\|\\mathcal{A}^{+}\|\\geq k\_{\\Gamma}\\\<br>\\mathsf{escalate}&\\text{otherwise}\\end{cases} |  |

Higher-risk mutations require stronger quorum limits kΓk\_{\\Gamma}, greater evaluator diversity within 𝒜+\\mathcal{A}^{+}, explicit veto handling, or human review.

Equivalently, issuance readiness is the predicate

|     |     |     |
| --- | --- | --- |
|  | 𝖱𝖾𝖺𝖽𝗒​(𝖩𝖯t,At,Γt)⇔q​(At,Γt)=𝖺𝗉𝗉𝗋𝗈𝗏𝖾.\\mathsf{Ready}(\\mathsf{JP}\_{t},A\_{t},\\Gamma\_{t})\\iff q(A\_{t},\\Gamma\_{t})=\\mathsf{approve}. |  |

Approval means the proof is authorization-ready under recorded inputs. It does not mean the action is globally optimal. The semantics are deliberately limited: DTF requires authority to come through a checked path; it does not claim complete world knowledge.

### 5.3 Failure Handling

Consensus validation rejects or escalates when quorum is missing, required evaluator classes are absent, the proof becomes stale, evaluator outputs are malformed, the derived boundary is ambiguous, or disagreement itself indicates unsafe uncertainty. Disagreement is not treated as an implementation inconvenience; it is a signal about authorization risk. Emergency handling is modeled as a governed break-glass policy, not a bypass: consensus requirements may change, but proof, narrowed identity, evidence, and post-event review remain mandatory.

### 5.4 Audit Value

Evaluator disagreement is evidence. DTF therefore preserves all attestations, not only the aggregate decision. Later review can distinguish clear approval, contested approval, rejection, escalation, and malformed evaluation. The record also makes the consensus layer accountable: reviewers can see which failure modes were checked, which objections were raised, and whether the configured rule converted that evidence into the appropriate authorization outcome.

## 6 Execution Identity

Execution Identity (𝖤𝖨\\mathsf{EI}) is the concrete authority produced by an approved proof. It is the main difference between merely deciding that a mutation is allowed and giving the execution substrate an enforceable, proof-derived scope for that mutation.

Execution Identity changes the locus of authorization from a durable role to a recorded decision. In role-based or attribute-based systems, an agent is assigned an identity (e.g., AgentServiceAccount) and granted broad permissions (e.g., TerminateInstance). When the agent acts, the system checks if the identity has the permission. This assumes the identity is a stable locus of trust.

DTF avoids this assumption. The proposing agent’s identity is metadata for the decision, not the source of authority. Trust is placed in the Justification Proof and its validation.

### 6.1 Definition

If Dt=q​(At,Γt)=𝖺𝗉𝗉𝗋𝗈𝗏𝖾D\_{t}=q(A\_{t},\\Gamma\_{t})=\\mathsf{approve}, the system derives

|     |     |     |
| --- | --- | --- |
|  | 𝖤𝖨t=h​(𝖩𝖯t,At,Γt)∈ℰ.\\mathsf{EI}\_{t}=h(\\mathsf{JP}\_{t},A\_{t},\\Gamma\_{t})\\in\\mathcal{E}. |  |

An 𝖤𝖨\\mathsf{EI} is ephemeral, non-transferable, and scoped to the proof-derived boundary BtB\_{t}. It contains or references:

- •


the permitted action class;

- •


the authorized resource set;

- •


temporal validity bounds;

- •


execution-time obligations;

- •


lineage to 𝖩𝖯t\\mathsf{JP}\_{t}, AtA\_{t}, Γt\\Gamma\_{t}, and DtD\_{t}.


An 𝖤𝖨\\mathsf{EI} is not a durable role. It is a per-decision capability whose existence is justified by the recorded proof and approval set.

### 6.2 Scope Relation

Let 𝖲𝖼𝗈𝗉𝖾:ℰ→ℬ\\mathsf{Scope}:\\mathcal{E}\\rightarrow\\mathcal{B} map an identity to its effective authority boundary. Valid issuance requires

|     |     |     |
| --- | --- | --- |
|  | 𝖲𝖼𝗈𝗉𝖾​(𝖤𝖨t)⪯Bt,\\mathsf{Scope}(\\mathsf{EI}\_{t})\\preceq B\_{t}, |  |

where ⪯\\preceq is the partial order over boundaries: action classes, resource sets, validity intervals, and obligations must be no broader than those encoded in BtB\_{t}. The execution broker may further narrow the scope, for example by reducing lifetime or requiring an additional final precondition check. It may not widen the scope beyond the proof boundary.

### 6.3 Enforcement

The execution substrate must admit a governed mutation XtX\_{t} only when

|     |     |     |
| --- | --- | --- |
|  | 𝖵𝖺𝗅𝗂𝖽​(𝖤𝖨t,Xt)=1.\\mathsf{Valid}(\\mathsf{EI}\_{t},X\_{t})=1. |  |

This predicate checks action, resource, time, and obligations. If the target platform cannot enforce a boundary precisely, the broker must add a mediation layer or refuse issuance for that mutation class.

### 6.4 Cloud Mapping

In cloud infrastructure, 𝖤𝖨\\mathsf{EI} can be implemented using short-lived credentials such as AWS STS sessions with restrictive session policies and resource conditions \[ [2](https://arxiv.org/html/2605.15228v1#bib.bib12 "AWS security token service api reference")\]. The credential format is secondary to lineage and containment: the issued authority must be traceable to 𝖩𝖯t\\mathsf{JP}\_{t} and incapable of authorizing actions outside BtB\_{t}.

### 6.5 Contrast with OpenKedge Task-Oriented Identity

OpenKedge introduces task-oriented identities as the execution-bound mechanism for approved intents \[ [9](https://arxiv.org/html/2605.15228v1#bib.bib13 "OpenKedge: governing agentic mutation with execution-bound safety and evidence chains")\]. 𝖤𝖨\\mathsf{EI} gives that mechanism explicit authorization semantics. A task-oriented identity becomes an Execution Identity when its scope is derived from a Justification Proof, issued only after consensus, and preserved as evidence.

## 7 Evidence Chain

The Evidence Chain is the durable record that makes proof-derived authority replayable. Conventional audit logs can show that an API call occurred. An Evidence Chain must also show why authority was issued, who or what approved it, what boundary was encoded, and whether execution stayed within that boundary.

Logging execution events is insufficient for verifiable infrastructure. If a system logs that an instance was terminated by an agent, an auditor knows _what_ happened, but not _why_ it was authorized. Did the agent hallucinate the context? Did a policy engine fail? Was the mutation escalated to a human who incorrectly approved it? To answer these questions, the system must record the entire authorization lifecycle. The Evidence Chain records that lifecycle.

### 7.1 Record

For each governed mutation attempt,

|     |     |     |
| --- | --- | --- |
|  | 𝖤𝖢t=(It,Ct,Pt,𝖩𝖯t,At,Γt,Dt,𝖤𝖨t,Xt,Ot).\\mathsf{EC}\_{t}=(I\_{t},C\_{t},P\_{t},\\mathsf{JP}\_{t},A\_{t},\\Gamma\_{t},D\_{t},\\mathsf{EI}\_{t},X\_{t},O\_{t}). |  |

Implementations may add timestamps, policy versions, hashes, signatures, evaluator identities, state digests, and substrate receipts. These enrich integrity and attribution but do not change the core requirement: authorization and execution must remain in the same lifecycle record.

### 7.2 Completeness

Evidence completeness requires that every governed execution have a record linking proof, approval, derived identity, mutation, and outcome. Rejected and escalated attempts should also be recorded because they explain what the system refused and why. Missing evidence is not an observability gap; it is an authorization failure.

### 7.3 Replay

A complete evidence record should let an auditor answer:

- •


what mutation was proposed;

- •


what context and policy were used;

- •


which evaluators approved, rejected, or abstained;

- •


what boundary was issued;

- •


what execution occurred and what outcome resulted.


Replay does not require reconstructing the entire external world. It requires preserving enough authorization-relevant state to re-check the decision under its recorded inputs.

### 7.4 Integrity

The chain should be append-only and tamper-evident. Hash linking, signatures, immutable storage, and correlation with substrate audit systems such as CloudTrail can strengthen the implementation \[ [1](https://arxiv.org/html/2605.15228v1#bib.bib11 "AWS cloudtrail user guide")\]. DTF does not mandate one cryptographic construction; it mandates that proof, approval, identity, and outcome cannot silently drift apart.

### 7.5 Relation to IEEC

OpenKedge’s IEEC records the intent-to-execution lineage of governed mutation \[ [9](https://arxiv.org/html/2605.15228v1#bib.bib13 "OpenKedge: governing agentic mutation with execution-bound safety and evidence chains")\]. DTF refines the evidence requirements for replayable authorization by requiring explicit storage of the Justification Proof, evaluator attestations, governance metadata, and Execution Identity linkage.

## 8 Safety and Audit Properties

This section states system properties of the composed DTF pipeline. The claims below are not properties of any component in isolation, and they should not be read as claims of semantic correctness for every approved action. They hold under the assumptions stated below, when Justification Proofs, consensus validation, Execution Identity, and Evidence Chains are implemented as the ordered authorization path.

These properties are architectural rather than component-local. Traditional systems trust principals and then constrain their actions through policy and logging. DTF makes the decision lifecycle the object of trust: authority emerges from explicit proof, distributed validation, bounded issuance, and durable evidence. This matters in agentic infrastructure, where the initiating reasoning process may be non-deterministic, partially observed, or unreliable.

### 8.1 Assumptions

#### A1: Enforcement fidelity.

The execution substrate enforces the action, resource, time, and obligation limits encoded in a valid 𝖤𝖨\\mathsf{EI}.

#### A2: Evidence integrity.

Evidence records cannot be silently modified or deleted after append.

#### A3: Consensus enforcement.

The consensus rule approves only when its configured quorum, veto, diversity, and escalation requirements are satisfied.

#### A4: Proof correspondence.

The stored proof and context correspond to the mutation attempt being evaluated with the fidelity captured in evidence.

### 8.2 System Invariants

#### Proof-bound execution.

Under A1 and A3, any admitted governed mutation XtX\_{t} has a corresponding 𝖩𝖯t\\mathsf{JP}\_{t}, AtA\_{t}, and Dt=𝖺𝗉𝗉𝗋𝗈𝗏𝖾D\_{t}=\\mathsf{approve} from which a valid 𝖤𝖨t\\mathsf{EI}\_{t} was derived. The substrate admits execution only through 𝖤𝖨\\mathsf{EI}, and 𝖤𝖨\\mathsf{EI} is issued only after proof approval.

#### Consensus-gated authority.

Under A3, no valid 𝖤𝖨t\\mathsf{EI}\_{t} is issued unless Dt=q​(At,Γt)=𝖺𝗉𝗉𝗋𝗈𝗏𝖾D\_{t}=q(A\_{t},\\Gamma\_{t})=\\mathsf{approve}. A single evaluator cannot create authority unless the governance rule explicitly defines that as sufficient.

#### Non-escalation.

Under A1, if XtX\_{t} executes through 𝖤𝖨t\\mathsf{EI}\_{t}, then its effective scope is contained within BtB\_{t}. This follows from 𝖲𝖼𝗈𝗉𝖾​(𝖤𝖨t)⪯Bt\\mathsf{Scope}(\\mathsf{EI}\_{t})\\preceq B\_{t} and substrate enforcement.

#### Evidence completeness.

Under A2, each admitted governed mutation remains attached to an evidence record containing intent, context, proof, attestations, governance metadata, identity, execution, and outcome.

#### Replayable verification.

Under A2 and A4, the authorization basis of each complete record can be re-examined from stored artifacts. Replayability is about the decision lifecycle, not perfect reconstruction of all external state.

### 8.3 Composed Pipeline Property

Under A1–A4, every admitted governed high-stakes mutation is proof-bound, consensus-gated, scope-bounded, evidence-preserved, and replayable from its lifecycle record.

#### Proof sketch.

The DTF pipeline constrains each stage by the previous one:

|     |     |     |
| --- | --- | --- |
|  | (It,Ct,Pt)→𝖩𝖯t→At→Dt→𝖤𝖨t→Xt→Ot→𝖤𝖢t.(I\_{t},C\_{t},P\_{t})\\rightarrow\\mathsf{JP}\_{t}\\rightarrow A\_{t}\\rightarrow D\_{t}\\rightarrow\\mathsf{EI}\_{t}\\rightarrow X\_{t}\\rightarrow O\_{t}\\rightarrow\\mathsf{EC}\_{t}. |  |

Approval requires the proof and attestation set; issuance requires approval; execution requires a valid identity; identity scope is contained in the proof boundary; evidence stores the lifecycle. The listed properties follow by composition.

### 8.4 Limits

This composed property does not imply semantic optimality, correct policy design, complete world knowledge, or resilience to total compromise of all evaluators and stores. It establishes a narrower infrastructure property: high-stakes authority cannot be legitimately materialized without recorded proof, recorded approval, bounded issuance, and durable evidence.

## 9 Implementation

DTF is implemented as a verification layer over the OpenKedge-based governed mutation substrate used in our prototype. The prototype binds the abstract functions to this substrate and to AWS primitives, but the decomposition into proof construction, validation, authority derivation, and evidence persistence is substrate-agnostic. Our prototype consists of approximately 4,500 lines of Go and is deployed as a suite of highly available microservices. It interposes on destructive infrastructure operations, privilege changes, and production configuration updates. The implementation materializes the model functions as explicit service boundaries and persisted artifacts rather than as implicit checks inside a single policy engine.

#### Prototype footprint.

| Module | LOC | Replicas | Primary model function |
| --- | --- | --- | --- |
| Intent Gateway | 650 | 3 | 𝖭𝗈𝗋𝗆𝖺𝗅𝗂𝗓𝖾\\mathsf{Normalize} |
| Justification Engine | 1,200 | 3 | ff, 𝖡𝗂𝗇𝖽𝖢𝗈𝗇𝗍𝖾𝗑𝗍\\mathsf{BindContext}, 𝖣𝖾𝗋𝗂𝗏𝖾𝖡𝗈𝗎𝗇𝖽𝖺𝗋𝗒\\mathsf{DeriveBoundary} |
| Swarm Coordinator | 700 | 3 | q​(At,Γt)q(A\_{t},\\Gamma\_{t}) |
| Execution Broker | 900 | 3 | hh, 𝖲𝖼𝗈𝗉𝖾\\mathsf{Scope}, 𝖵𝖺𝗅𝗂𝖽\\mathsf{Valid} |
| Evidence Store Adapter | 500 | 3 | 𝖤𝖢t\\mathsf{EC}\_{t} persistence |
| Evaluation Harness | 550 | 1 | workload generation and replay |

_Replicas are deployed across three availability zones for the online control path._

### 9.1 Function Realization

The runtime path implements the functions from Section 3 as follows.

- •


f​(It,Ct,Pt)f(I\_{t},C\_{t},P\_{t}) is implemented by the Intent Gateway and Justification Engine. The gateway canonicalizes ItI\_{t} into It′I^{\\prime}\_{t}, binds the request to a context snapshot CtC\_{t}, evaluates the applicable policy bundle PtP\_{t}, derives BtB\_{t}, and emits the structured proof 𝖩𝖯t=(Mt,St,Πt,Rt,Bt)\\mathsf{JP}\_{t}=(M\_{t},S\_{t},\\Pi\_{t},R\_{t},B\_{t}).

- •


Each evaluator function vi​(𝖩𝖯t)v\_{i}(\\mathsf{JP}\_{t}) is implemented as an isolated worker that consumes the same serialized proof and emits an attributed attestation ait=(vi,dit,ωit)a\_{i}^{t}=(v\_{i},d\_{i}^{t},\\omega\_{i}^{t}). Attestations are signed and include evaluator class, input proof hash, decision, objections, and obligations.

- •


The consensus function q​(At,Γt)q(A\_{t},\\Gamma\_{t}) is implemented by the swarm coordinator. It verifies attestation signatures, checks evaluator diversity and freshness, applies veto rules, computes the risk-adjusted quorum from Γt\\Gamma\_{t}, and returns 𝖺𝗉𝗉𝗋𝗈𝗏𝖾\\mathsf{approve}, 𝗋𝖾𝗃𝖾𝖼𝗍\\mathsf{reject}, or 𝖾𝗌𝖼𝖺𝗅𝖺𝗍𝖾\\mathsf{escalate}.

- •


𝖡𝗈𝗎𝗇𝖽𝖺𝗋𝗒​(𝖩𝖯t)\\mathsf{Boundary}(\\mathsf{JP}\_{t}) is materialized as the boundary field Bt=(μt,ρt,τt,Ωt)B\_{t}=(\\mu\_{t},\\rho\_{t},\\tau\_{t},\\Omega\_{t}) embedded in the proof. The broker treats this field as the maximum issuable authority.

- •


h​(𝖩𝖯t,At,Γt)h(\\mathsf{JP}\_{t},A\_{t},\\Gamma\_{t}) is implemented by the Execution Broker. It runs only after q​(At,Γt)=𝖺𝗉𝗉𝗋𝗈𝗏𝖾q(A\_{t},\\Gamma\_{t})=\\mathsf{approve}, converts the approved boundary into a substrate-specific temporary credential, and records lineage to the proof, attestation set, governance metadata, and decision.

- •


𝖲𝖼𝗈𝗉𝖾​(𝖤𝖨t)\\mathsf{Scope}(\\mathsf{EI}\_{t}) and 𝖵𝖺𝗅𝗂𝖽​(𝖤𝖨t,Xt)\\mathsf{Valid}(\\mathsf{EI}\_{t},X\_{t}) are implemented by broker-side admission checks. Before forwarding a mutation, the broker verifies that the effective action, resource, time window, and obligations of the credential are no broader than BtB\_{t} and that the concrete mutation attempt is authorized by the issued identity.

- •


𝖤𝖢t\\mathsf{EC}\_{t} is implemented by the Evidence Store as one append-only lifecycle record containing the intent, bound context digest, policy version, proof, attestations, governance metadata, decision, issued identity reference, attempted mutation, and observed outcome.


### 9.2 Components

#### Intent Gateway and Justification Engine.

The gateway receives proposed mutations via gRPC and implements 𝖭𝗈𝗋𝗆𝖺𝗅𝗂𝗓𝖾\\mathsf{Normalize} by resolving aliases, validating schemas, and converting tool-specific calls into canonical mutation specifications. The Justification Engine (approx. 1,200 LOC) implements 𝖡𝗂𝗇𝖽𝖢𝗈𝗇𝗍𝖾𝗑𝗍\\mathsf{BindContext} through concurrent state collection from Redis, inventory services, incident state, ownership metadata, and an internal graph database for dependency resolution. It then implements 𝖤𝗏𝖺𝗅𝗎𝖺𝗍𝖾𝖯𝗈𝗅𝗂𝖼𝗒\\mathsf{EvaluatePolicy} and 𝖣𝖾𝗋𝗂𝗏𝖾𝖡𝗈𝗎𝗇𝖽𝖺𝗋𝗒\\mathsf{DeriveBoundary} by loading a versioned policy bundle, assigning risk class and required governance metadata, and computing the maximum boundary BtB\_{t}. In our deployment, context gathering typically completes in under 20 ms, issuing 9 parallel reads per proof at the median and 17 at the 95th percentile. Serialized proofs have a median size of 6.4 KB and a 95th percentile size of 18.7 KB.

#### Evaluation Swarm.

The swarm runs independent evaluators over the same proof and applies Dt=q​(At,Γt)D\_{t}=q(A\_{t},\\Gamma\_{t}). Evaluators are implemented as stateless AWS Lambda functions to ensure parallel execution and strict isolation. The deployed evaluator set contains 7 functions across 5 classes: 2 policy evaluators, 2 dependency-state evaluators, 1 risk evaluator, 1 simulation evaluator, and 1 human-escalation adapter. Low-risk mutations require 3 approvals from at least 2 classes; high-risk mutations require 4 approvals from at least 3 classes; protected-resource mutations additionally grant veto authority to the dependency-state and human-escalation classes. Attestations are compact, with a median serialized size of 0.9 KB. The coordinator rejects malformed attestations, escalates missing required evaluator classes, honors veto-capable evaluators for protected mutation classes, and requires risk-sensitive mm-of-nn cryptographic signatures before progressing.

#### Execution Broker and Evidence Store.

The Execution Broker derives 𝖤𝖨t\\mathsf{EI}\_{t} by exchanging the consensus-approved 𝖩𝖯t\\mathsf{JP}\_{t} for temporary credentials. It translates BtB\_{t} into substrate-specific action, resource, validity, and obligation constraints, then performs a final 𝖲𝖼𝗈𝗉𝖾​(𝖤𝖨t)⪯Bt\\mathsf{Scope}(\\mathsf{EI}\_{t})\\preceq B\_{t} check before exposing the credential to the execution path. During execution, the broker evaluates 𝖵𝖺𝗅𝗂𝖽​(𝖤𝖨t,Xt)\\mathsf{Valid}(\\mathsf{EI}\_{t},X\_{t}) and refuses calls that drift from the approved action, resource, time window, or required obligations. The median identity lifetime is 300 s for destructive actions and 120 s for emergency break-glass actions. The Evidence Store persists 𝖤𝖢t\\mathsf{EC}\_{t} as an append-only ledger using Amazon QLDB (Quantum Ledger Database) to provide tamper-evident persistence, optionally linking to substrate audit receipts. Each logical lifecycle record is represented by 4 append events on average: proof creation, attestation closure, identity issuance or refusal, and substrate outcome. The median complete evidence record is 11.2 KB.

### 9.3 AWS Instantiation

Our cloud deployment relies heavily on native AWS primitives. The broker implements hh by assuming short-lived sessions via AWS Security Token Service (STS), constrained by inline session policies and resource conditions generated from BtB\_{t}\[ [2](https://arxiv.org/html/2605.15228v1#bib.bib12 "AWS security token service api reference")\]. The generated session policies contain a median of 3 allow statements and 2 explicit resource conditions; no generated policy in the evaluation exceeds 1.8 KB. Temporal scope is enforced through short session duration and broker-side expiry checks. Obligation checks, such as verifying that a target is no longer receiving production traffic, are performed immediately before the substrate call. Evidence records are continuously correlated with CloudTrail logs \[ [1](https://arxiv.org/html/2605.15228v1#bib.bib11 "AWS cloudtrail user guide")\]. In the evaluated workload, this mapping provides containment without requiring custom substrate modifications.

### 9.4 Instance Termination Path

For TerminateInstance(r), the gateway normalizes the request into Mt=(TerminateInstance,r)M\_{t}=(\\texttt{TerminateInstance},r). The Justification Engine binds dependency context, traffic state, ownership, protection tags, and incident state into StS\_{t}; records the governing destructive-action policy in Πt\\Pi\_{t}; assigns the risk and admissibility assessment RtR\_{t}; and derives BtB\_{t} as a single-action boundary over resource rr with a strict 5-minute validity window and a no-active-traffic obligation. Policy, state, simulation, and risk evaluators attest to this proof in parallel. If Dt=𝖺𝗉𝗉𝗋𝗈𝗏𝖾D\_{t}=\\mathsf{approve}, the broker derives an 𝖤𝖨t\\mathsf{EI}\_{t} scoped to exactly that termination action on rr. Before execution, the broker re-checks the obligation and evaluates 𝖵𝖺𝗅𝗂𝖽​(𝖤𝖨t,Xt)\\mathsf{Valid}(\\mathsf{EI}\_{t},X\_{t}). The Evidence Store records both success and refusal paths with tamper-evident linkage.

## 10 Evaluation

The evaluation is a mechanism validation of DTF in a governed synthetic workload. It asks whether the implementation realizes the model functions—proof construction, independent attestation, consensus, authority derivation, boundary enforcement, execution validity, evidence completeness, and overhead—for high-stakes cloud mutations. Our testbed consists of a simulated environment mimicking a multi-region cloud deployment handling 10,000 synthetic agent mutations over 50 independent runs. Each run contains 200 mutations and replays the same workload against DTF, standing IAM, and policy-only precheck baselines.

Several metrics below are invariant-oriented. A 100% result for boundary refusal or evidence completeness means that the implementation enforced the designed containment or recording invariant in this controlled workload; it does not imply open-world semantic correctness or universally correct policy. We separate containment metrics, replayability metrics, and policy-quality questions. The evaluation supports claims about proof-derived authority and replayable enforcement under controlled scenarios, not unconstrained internet-scale agent behavior.

### 10.1 Questions

- •


EQ1: Proof construction. Does f​(It,Ct,Pt)f(I\_{t},C\_{t},P\_{t}) produce a proof containing the mutation, context, policy, risk assessment, and boundary fields needed for independent review?

- •


EQ2: Independent validation. Do evaluator functions vi​(𝖩𝖯t)v\_{i}(\\mathsf{JP}\_{t}) produce attributable attestations, and does q​(At,Γt)q(A\_{t},\\Gamma\_{t}) prevent unilateral unsafe authority derivation?

- •


EQ3: Authority containment. Does h​(𝖩𝖯t,At,Γt)h(\\mathsf{JP}\_{t},A\_{t},\\Gamma\_{t}) produce an 𝖤𝖨t\\mathsf{EI}\_{t} whose effective scope satisfies 𝖲𝖼𝗈𝗉𝖾​(𝖤𝖨t)⪯Bt\\mathsf{Scope}(\\mathsf{EI}\_{t})\\preceq B\_{t} and reduces authority compared with standing credentials?

- •


EQ4: Execution validity and replayability. Does the broker enforce 𝖵𝖺𝗅𝗂𝖽​(𝖤𝖨t,Xt)\\mathsf{Valid}(\\mathsf{EI}\_{t},X\_{t}), and can 𝖤𝖢t\\mathsf{EC}\_{t} reconstruct the authorization lifecycle?

- •


EQ5: Overhead. Is the added latency acceptable for high-risk operations?


### 10.2 Scenarios

We evaluate three representative workloads: destructive resource termination (3,500 requests), production configuration mutation during partial degradation (4,500 requests), and emergency break-glass execution (2,000 requests). The workload includes 7,600 admissible requests and 2,400 unsafe or adversarial variants. Unsafe variants include missing dependency context (900), stale state (650), protected-resource targeting (350), post-approval boundary drift (300), and malformed evaluator outputs (200). Baselines are (B1) standing IAM credentials with standard audit logs and (B2) a policy-only precheck that still executes with standing authority. We exclude standard "human-in-the-loop" approval workflows from the latency baselines because human review introduces O​(minutes)O(\\text{minutes}) of latency, which strictly dominates infrastructure overhead and is not directly comparable to automated swarm consensus.

### 10.3 Metrics

The metrics are proof completeness rate, attestation coverage, unsafe mutation block or escalation rate, authority reduction factor, boundary-violation refusal rate, evidence completeness rate, replay success rate, decision latency, and broker overhead. Proof completeness checks whether all fields of 𝖩𝖯t=(Mt,St,Πt,Rt,Bt)\\mathsf{JP}\_{t}=(M\_{t},S\_{t},\\Pi\_{t},R\_{t},B\_{t}) are populated and hash-linked to their source artifacts. Attestation coverage checks that required evaluator classes emit well-formed attestations over the same proof hash. Boundary-violation refusal injects attempted action, resource, and time-window drift after approval and measures whether 𝖵𝖺𝗅𝗂𝖽​(𝖤𝖨t,Xt)\\mathsf{Valid}(\\mathsf{EI}\_{t},X\_{t}) refuses execution.

#### Aggregate results.

| Metric | DTF | B1 | B2 |
| --- | --- | --- | --- |
| Complete proof records | 100.0% | 0.0% | 72.4% |
| Required attestation coverage | 100.0% | – | – |
| Unsafe block or escalation | 100.0% | 0.0% | 86.0% |
| Boundary-drift refusal | 100.0% | 0.0% | 0.0% |
| Mean mutable resources per approval | 1.0 | 450.0 | 450.0 |
| Evidence completeness | 100.0% | 41.8% | 64.6% |
| Replay success | 99.9% | 23.0% | 58.7% |

#### Latency breakdown.

| Stage | Mean | p50 | p95 | p99 |
| --- | --- | --- | --- | --- |
| Proof construction and context binding | 18.5 | 16.8 | 34.7 | 48.9 |
| Parallel evaluator processing | 24.3 | 21.1 | 52.8 | 79.4 |
| Consensus aggregation | 3.1 | 2.7 | 7.6 | 11.8 |
| Broker issuance and STS exchange | 12.4 | 10.9 | 26.5 | 41.2 |
| End-to-end decision latency | 58.3 | 52.6 | 112.4 | 171.3 |

### 10.4 Findings

#### Safety.

DTF achieved a 100% block or escalation rate across all 2,400 unsafe variants in the governed workload. In contrast, B2 (policy-only precheck) allowed 336 unsafe mutations through, corresponding to the 14% unsafe pass-through rate caused by stale local state or missing dependency context. This result measures enforcement of the configured proof, consensus, and veto rules, not correctness of every possible real-world policy. No single evaluator was able to derive authority without a consensus decision: all 200 malformed evaluator-output cases and all 350 protected-resource veto cases were rejected or escalated by q​(At,Γt)q(A\_{t},\\Gamma\_{t}). In emergency scenarios, DTF successfully processed all 2,000 break-glass requests while constraining the authority to the exact target rather than relying on broad administrative override.

#### Authority containment.

𝖤𝖨\\mathsf{EI} reduced the effective execution scope. While standing credentials (B1) exposed an average of 450 resources and a 95th percentile of 1,120 resources to potential mutation per role, DTF constrained authority to exactly 1 approved resource per request, yielding a 99.7% authority reduction factor at the mean and 99.9% at the 95th percentile. In 300 boundary-drift tests, attempts to reuse an approved identity for a different action, resource, or expired time window were refused by the broker. For destructive actions, this prevents the tested class of post-approval blast-radius expansion.

#### Auditability.

The Evidence Chain achieved a 100% completeness rate for the DTF lifecycle fields, persisting proof, attestations, governance metadata, decision, issuance reference, attempted mutation, and outcome for all 10,000 attempts. The 10,000 logical records produced 39,812 append events and 10,000 terminal outcome entries. In replay testing, auditors successfully reconstructed the authorization lifecycle for 9,991 events without manual log correlation, compared to 2,300 events under B1 standard audit logs and 5,870 events under B2. Replay failures were attributable to deliberately injected external receipt loss rather than missing DTF lifecycle records.

#### Overhead.

The governed path added acceptable latency for high-stakes operations. Proof construction and context gathering averaged 18.5 ms. Evaluator processing via parallel Lambda execution averaged 24.3 ms. Consensus aggregation, signature verification, and quorum evaluation averaged 3.1 ms. Broker execution and STS credential issuance added an overhead of 12.4 ms. The total end-to-end decision latency averaged 58.3 ms, with a median of 52.6 ms, 95th percentile of 112.4 ms, and 99th percentile of 171.3 ms. Even at the 99th percentile, the added delay remains small relative to destructive infrastructure workflows, which are typically dominated by substrate operation latency and human review time.

### 10.5 Ablations

Removing consensus leaves a proof object but reintroduces unilateral evaluator failure: in the malformed-output workload, single-evaluator approval would have allowed 61 of 200 malformed cases to proceed. This matches the swarm design rationale: heterogeneous evaluator disagreement matters only if it can block or escalate authority derivation. Removing 𝖤𝖨\\mathsf{EI} preserves decision records but loses execution containment: all 300 post-approval boundary-drift attempts become executable because the substrate still sees broad standing authority. Removing the Evidence Chain preserves runtime gating but reduces replay success from 99.9% to 52.1% because auditors must reconstruct proof, approval, and outcome from separate logs. The mechanisms are complementary rather than interchangeable.

### 10.6 Limitations

The prototype evaluation tests high-risk mutations rather than benchmarking every possible agent action. Its containment and replayability results reflect architecture-controlled scenarios with known mutation classes, explicit policies, and injected failure modes; they should not be read as unconstrained internet-scale benchmarks. Results depend on the fidelity of captured context, the correctness of policy, the quality and independence of evaluator classes, and the granularity with which the substrate can enforce 𝖤𝖨\\mathsf{EI} boundaries. We do not claim resilience to total compromise of all evaluators, broker, and evidence storage. The evidence supports the narrower claim that proof-derived authority is practical and improves containment and replayability for governed infrastructure mutations.

## 11 Discussion and Future Work

DTF changes the object of authorization from a durable principal to a recorded decision lifecycle. That shift matters because agentic systems are non-deterministic and partially observed: the system need not trust the agent’s internal reasoning if execution authority can be derived only from explicit proof, independent approval, and bounded issuance.

### 11.1 Tradeoffs

DTF adds latency, storage, and operational complexity. These costs are justified for high-stakes mutations but should not be imposed indiscriminately on routine reads or low-risk operations. Evidence fidelity also creates a storage tradeoff: richer context improves replay, while compact records reduce operational burden. Evaluator diversity improves resilience but increases governance design work.

### 11.2 Limitations

DTF does not synthesize correct policy, guarantee globally optimal decisions, or solve prompt injection inside the proposing agent. Its value depends on context fidelity: if dependency state, ownership metadata, incident state, or policy versions are stale or incomplete, the proof may faithfully encode the wrong basis for authorization. It also depends on evaluator diversity quality. A nominal swarm whose evaluators share the same data source, model failure mode, or operational blind spot provides less protection than its quorum size suggests.

DTF also assumes that the governed path is actually interposed, that 𝖤𝖨\\mathsf{EI} boundaries are enforceable at the substrate granularity required by the mutation, and that evidence integrity is maintained. Some substrates expose coarse permissions that may require a broker or mediation layer before DTF can enforce narrow scopes. DTF is not designed to survive total compromise of the evaluator set, broker, and evidence store. These are infrastructure and governance assumptions, not model capabilities.

### 11.3 Future Work

Future work includes typed proof languages for 𝖩𝖯\\mathsf{JP}, adaptive evaluator selection based on risk and historical disagreement, stronger cross-domain Evidence Chains for workflows spanning organizations, simulation-backed approval for irreversible operations, and structured human review for high-assurance escalation.

## 12 Conclusion

OpenKedge motivates and instantiates the governed mutation substrate used in this paper: intent, context, policy, bounded execution, and lineage. The paper’s contribution is DTF, a verification model for making authorization proof-bound, consensus-gated, scope-bounded, and replayable across governed agentic infrastructure. It introduces Justification Proofs, consensus validation, Execution Identity, and Evidence Chains as the mechanisms that turn an approved mutation into replayable authority.

The invariant can be stated compactly: no high-stakes execution without proof, no authority without consensus, and no valid mutation detached from evidence. DTF makes that invariant an executable authorization lifecycle for agentic infrastructure, rather than an audit aspiration after the fact.

## References

- \[1\]Amazon Web Services (2024)AWS cloudtrail user guide.
Note: [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/ "") Documentation referenceCited by: [§7.4](https://arxiv.org/html/2605.15228v1#S7.SS4.p1.1 "7.4 Integrity ‣ 7 Evidence Chain ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems"),
[§9.3](https://arxiv.org/html/2605.15228v1#S9.SS3.p1.2 "9.3 AWS Instantiation ‣ 9 Implementation ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems").

- \[2\]Amazon Web Services (2024)AWS security token service api reference.
Note: [https://docs.aws.amazon.com/STS/latest/APIReference/](https://docs.aws.amazon.com/STS/latest/APIReference/ "") Documentation referenceCited by: [§6.4](https://arxiv.org/html/2605.15228v1#S6.SS4.p1.3 "6.4 Cloud Mapping ‣ 6 Execution Identity ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems"),
[§9.3](https://arxiv.org/html/2605.15228v1#S9.SS3.p1.2 "9.3 AWS Instantiation ‣ 9 Implementation ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems").

- \[3\]P. Buneman, S. Khanna, and W. Tan (2001)Why and where: a characterization of data provenance.
Lecture Notes in Computer Science1973,  pp. 316–330.
Cited by: [§2](https://arxiv.org/html/2605.15228v1#S2.SS0.SSS0.Px5.p1.1 "Provenance and accountability. ‣ 2 Related Work ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems").

- \[4\]M. Castro and B. Liskov (1999)Practical byzantine fault tolerance.
In Proceedings of the 3rd Symposium on Operating Systems Design
and Implementation,
pp. 173–186.
Cited by: [§2](https://arxiv.org/html/2605.15228v1#S2.SS0.SSS0.Px4.p1.1 "Distributed trust. ‣ 2 Related Work ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems").

- \[5\]J. W. Cutler, C. Disselkoen, A. Eline, S. He, K. Headley, M. Hicks, K. Hietala, E. Ioannidis, J. Kastner, A. Mamat, et al. (2024)Cedar: a new language for expressive, fast, safe, and analyzable authorization.
Proceedings of the ACM on Programming Languages8 (OOPSLA1),  pp. 670–697.
Cited by: [§2](https://arxiv.org/html/2605.15228v1#S2.SS0.SSS0.Px2.p1.1 "Automated Reasoning and Verified Permissions. ‣ 2 Related Work ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems").

- \[6\]C. Disselkoen, A. Eline, S. He, K. Headley, M. Hicks, K. Hietala, J. Kastner, A. Mamat, M. McCutchen, N. Rungta, et al. (2024)How we built cedar: a verification-guided approach.
In Companion Proceedings of the 32nd ACM International Conference
on the Foundations of Software Engineering,
pp. 351–357.
Cited by: [§2](https://arxiv.org/html/2605.15228v1#S2.SS0.SSS0.Px2.p1.1 "Automated Reasoning and Verified Permissions. ‣ 2 Related Work ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems").

- \[7\]R. Fang, R. Binder, J. Zou, T. Burgess, and D. Wagner (2024)LLM agents can autonomously hack websites.
arXiv preprint arXiv:2402.06664.
Cited by: [§2](https://arxiv.org/html/2605.15228v1#S2.SS0.SSS0.Px3.p1.1 "LLM Agent Safety and Tool-Use Authorization. ‣ 2 Related Work ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems").

- \[8\]K. Greshake, S. Abdelnabi, S. Mishra, C. Endres, T. Holz, and M. Fritz (2023)Not what you’ve signed up for: compromising real-world llm-integrated applications with indirect prompt injection.
In Proceedings of the 16th ACM Workshop on Artificial Intelligence
and Security,
Cited by: [§2](https://arxiv.org/html/2605.15228v1#S2.SS0.SSS0.Px3.p1.1 "LLM Agent Safety and Tool-Use Authorization. ‣ 2 Related Work ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems").

- \[9\]J. He and D. Yu (2026)OpenKedge: governing agentic mutation with execution-bound safety and evidence chains.
arXiv preprint arXiv:2604.08601.
Cited by: [§1](https://arxiv.org/html/2605.15228v1#S1.p2.1 "1 Introduction ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems"),
[§2](https://arxiv.org/html/2605.15228v1#S2.SS0.SSS0.Px6.p1.1 "OpenKedge and Sovereign Agentic Loops. ‣ 2 Related Work ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems"),
[§3.5](https://arxiv.org/html/2605.15228v1#S3.SS5.p1.1 "3.5 What this paper adds beyond OpenKedge ‣ 3 Distributed Trust Framework ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems"),
[§3](https://arxiv.org/html/2605.15228v1#S3.p2.1 "3 Distributed Trust Framework ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems"),
[§6.5](https://arxiv.org/html/2605.15228v1#S6.SS5.p1.1 "6.5 Contrast with OpenKedge Task-Oriented Identity ‣ 6 Execution Identity ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems"),
[§7.5](https://arxiv.org/html/2605.15228v1#S7.SS5.p1.1 "7.5 Relation to IEEC ‣ 7 Evidence Chain ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems").

- \[10\]J. He and D. Yu (2026)Sovereign agentic loops: decoupling ai reasoning from execution in real-world systems.
arXiv preprint arXiv:2604.22136.
Cited by: [§2](https://arxiv.org/html/2605.15228v1#S2.SS0.SSS0.Px6.p1.1 "OpenKedge and Sovereign Agentic Loops. ‣ 2 Related Work ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems").

- \[11\]V. C. Hu, D. Ferraiolo, R. Kuhn, A. R. Friedman, A. J. Lang, M. M. Cogdell, A. Schnitzer, K. Sandlin, R. Miller, and K. Scarfone (2015)Guide to attribute based access control (abac) definition and considerations.
NIST Special Publication 800-162.
Cited by: [§1](https://arxiv.org/html/2605.15228v1#S1.p5.1 "1 Introduction ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems"),
[§2](https://arxiv.org/html/2605.15228v1#S2.SS0.SSS0.Px1.p1.1 "Access control and zero trust. ‣ 2 Related Work ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems").

- \[12\]M. Kleppmann (2017)Designing data-intensive applications.
O’Reilly Media.
Cited by: [§2](https://arxiv.org/html/2605.15228v1#S2.SS0.SSS0.Px5.p1.1 "Provenance and accountability. ‣ 2 Related Work ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems").

- \[13\]L. Lamport, R. Shostak, and M. Pease (1982)The byzantine generals problem.
ACM Transactions on Programming Languages and Systems4 (3),  pp. 382–401.
Cited by: [§2](https://arxiv.org/html/2605.15228v1#S2.SS0.SSS0.Px4.p1.1 "Distributed trust. ‣ 2 Related Work ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems").

- \[14\]S. Rose, O. Borchert, S. Mitchell, and S. Connelly (2020)Zero trust architecture.
Technical reportTechnical Report NIST Special Publication 800-207, National Institute of Standards and Technology.
Cited by: [§1](https://arxiv.org/html/2605.15228v1#S1.p5.1 "1 Introduction ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems"),
[§2](https://arxiv.org/html/2605.15228v1#S2.SS0.SSS0.Px1.p1.1 "Access control and zero trust. ‣ 2 Related Work ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems").

- \[15\]R. S. Sandhu, E. J. Coyne, H. L. Feinstein, and C. E. Youman (1992)Role-based access control models.
In Proceedings of the 15th National Computer Security Conference,
Cited by: [§1](https://arxiv.org/html/2605.15228v1#S1.p5.1 "1 Introduction ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems"),
[§2](https://arxiv.org/html/2605.15228v1#S2.SS0.SSS0.Px1.p1.1 "Access control and zero trust. ‣ 2 Related Work ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems").

- \[16\]L. Wang, C. Ma, X. Feng, Z. Zhang, H. Yang, J. Zhang, Z. Chen, J. Tang, X. Chen, Y. Lin, et al. (2024)A survey on large language model based autonomous agents.
Frontiers of Computer Science18 (6).
Cited by: [§2](https://arxiv.org/html/2605.15228v1#S2.SS0.SSS0.Px3.p1.1 "LLM Agent Safety and Tool-Use Authorization. ‣ 2 Related Work ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems").

- \[17\]D. J. Weitzner, H. Abelson, T. Berners-Lee, J. Feigenbaum, J. A. Hendler, and G. J. Sussman (2008)Information accountability.
Communications of the ACM51 (6),  pp. 82–87.
Cited by: [§2](https://arxiv.org/html/2605.15228v1#S2.SS0.SSS0.Px5.p1.1 "Provenance and accountability. ‣ 2 Related Work ‣ Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems").


## Appendix A Notation

| Symbol | Meaning |
| --- | --- |
| ℐ,𝒞,𝒫\\mathcal{I},\\mathcal{C},\\mathcal{P} | Intent, context, and policy spaces. |
| 𝒥,𝒜,𝒢\\mathcal{J},\\mathcal{A},\\mathcal{G} | Proof, attestation, and governance-metadata spaces. |
| ℬ,ℰ\\mathcal{B},\\mathcal{E} | Execution-boundary and Execution Identity spaces. |
| 𝒳,𝒪\\mathcal{X},\\mathcal{O} | Mutation-attempt and execution-outcome spaces. |
| It∈ℐI\_{t}\\in\\mathcal{I} | Canonical mutation intent at logical time tt. |
| Ct∈𝒞C\_{t}\\in\\mathcal{C} | Bound context snapshot used for authorization. |
| Pt∈𝒫P\_{t}\\in\\mathcal{P} | Applicable policy bundle and version. |
| f:ℐ×𝒞×𝒫→𝒥f:\\mathcal{I}\\times\\mathcal{C}\\times\\mathcal{P}\\to\\mathcal{J} | Proof-construction function. |
| 𝖩𝖯t∈𝒥\\mathsf{JP}\_{t}\\in\\mathcal{J} | Justification Proof derived from (It,Ct,Pt)(I\_{t},C\_{t},P\_{t}). |
| Vt={v1,…,vn}V\_{t}=\\{v\_{1},\\ldots,v\_{n}\\} | Evaluator set selected for the mutation at time tt. |
| ait∈𝒜a\_{i}^{t}\\in\\mathcal{A} | Attestation emitted by evaluator viv\_{i} over 𝖩𝖯t\\mathsf{JP}\_{t}. |
| At=(a1t,…,ant)A\_{t}=(a\_{1}^{t},\\ldots,a\_{n}^{t}) | Ordered attestation record. |
| Γt∈𝒢\\Gamma\_{t}\\in\\mathcal{G} | Governance metadata, including quorum, veto, and escalation rules. |
| q:𝒜n×𝒢→𝒟q:\\mathcal{A}^{n}\\times\\mathcal{G}\\to\\mathcal{D} | Consensus function. |
| Dt∈𝒟D\_{t}\\in\\mathcal{D} | Consensus decision, where 𝒟={𝖺𝗉𝗉𝗋𝗈𝗏𝖾,𝗋𝖾𝗃𝖾𝖼𝗍,𝖾𝗌𝖼𝖺𝗅𝖺𝗍𝖾}\\mathcal{D}=\\{\\mathsf{approve},\\mathsf{reject},\\mathsf{escalate}\\}. |
| Bt=(μt,ρt,τt,Ωt)B\_{t}=(\\mu\_{t},\\rho\_{t},\\tau\_{t},\\Omega\_{t}) | Proof-derived execution boundary: action, resources, time, obligations. |
| 𝖡𝗈𝗎𝗇𝖽𝖺𝗋𝗒:𝒥→ℬ\\mathsf{Boundary}:\\mathcal{J}\\to\\mathcal{B} | Map from a proof to its maximal execution boundary. |
| h:𝒥×𝒜n×𝒢→ℰh:\\mathcal{J}\\times\\mathcal{A}^{n}\\times\\mathcal{G}\\to\\mathcal{E} | Authority-derivation function. |
| 𝖤𝖨t∈ℰ\\mathsf{EI}\_{t}\\in\\mathcal{E} | Execution Identity derived from an approved proof. |
| ⪯\\preceq | Componentwise containment order over execution boundaries. |
| 𝖲𝖼𝗈𝗉𝖾:ℰ→ℬ\\mathsf{Scope}:\\mathcal{E}\\to\\mathcal{B} | Map from an identity to its effective authority boundary. |
| 𝖲𝖼𝗈𝗉𝖾​(𝖤𝖨t)⪯Bt\\mathsf{Scope}(\\mathsf{EI}\_{t})\\preceq B\_{t} | Issued identity scope is no broader than the approved boundary. |
| 𝖵𝖺𝗅𝗂𝖽:ℰ×𝒳→{0,1}\\mathsf{Valid}:\\mathcal{E}\\times\\mathcal{X}\\to\\{0,1\\} | Predicate deciding whether an identity authorizes a mutation attempt. |
| Xt∈𝒳X\_{t}\\in\\mathcal{X} | Attempted or executed mutation. |
| Ot∈𝒪O\_{t}\\in\\mathcal{O} | Observed execution outcome. |
| 𝖤𝖢t\\mathsf{EC}\_{t} | Evidence record linking proof, approval, authority, execution, and outcome. |

Table 1: Core notation. Authority is modeled as a computed state derived from proof and consensus, not as a standing property of a caller.

BETA
