---
date: '2026-05-23'
description: Uber's recent advancements in AI agent identity management address critical
  issues in accountability and oversight for agentic tasks. Their internal platform
  utilizes a refined identity model that supports cryptographic agent identities and
  propagates execution context across automations. This architecture employs a centralized
  Security Token Service (STS) for short-lived JWT tokens, enhancing traceability
  and auditing across multi-agent workflows. Key implications include improved compliance,
  reduced incident response times, and a foundation for dynamic access control in
  AI ecosystems. As AI adoption accelerates, Uber’s architecture sets a precedent
  for integrating robust security measures into agent-driven environments.
link: https://www.uber.com/us/en/blog/solving-the-agent-identity-crisis/
tags:
- Identity Management
- Microservices
- AI Agents
- Zero Trust Security
- Kubernetes
title: Solving the Identity Crisis for AI Agents
---

[Skip to main content](https://www.uber.com/us/en/blog/solving-the-agent-identity-crisis/#main)

May 21, 2026

# Solving the Identity Crisis for AI Agents

![Matt Mathew](https://cn-geo1.uber.com/image-proc/crop/resizecrop/udam/format=auto/width=40/height=40/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy8yZTI4ZDgzMS04MGZmLTU3ZjEtOWU3MS1jYjI1OTFjNGUxNWIuanBlZw==)

MM

Matt Mathew

Sr Staff Engineer

![Prasad Borole](https://cn-geo1.uber.com/image-proc/crop/resizecrop/udam/format=auto/width=40/height=40/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy8xZDc2YTRkMi02YzI1LTU4YjctOGJiMS1lOTU1MzZmYjcwYTkucG5n)

PB

Prasad Borole

Staff Software Engineer

![Meng Huang](https://cn-geo1.uber.com/image-proc/crop/resizecrop/udam/format=auto/width=40/height=40/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy9iYWZlODk3MS00ZWUwLTRlOWItODEyMi1jNjE3MTdkYTZkOWMucG5n)

MH

Meng Huang

Engineering Manager

3+

![](https://cn-geo1.uber.com/image-proc/crop/resizecrop/udam/format=auto/width=552/height=0/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy9mNTAxNTRjMy1hNjU4LTQ2YTQtODQ1Yi01ZTk4YTA4ZGE4MmYucG5n)

Share this article

FacebookLinkedinX socialLink

# Introduction

Uber is at the forefront of leveraging AI, empowering engineers to build AI solutions to improve productivity. In early 2025, the company built an internal Agent platform that allows teams to compose, deploy, and operate production-grade agents at scale. Additionally, Uber’s microservices tech stack comprising thousands of services was made AI-ready by enabling MCP® (Model Context Protocol) support over existing service APIs.

Increasing agentic autonomy necessitates strict oversight of the agents and the actions they execute. Accountability, the ability to answer “who did what, when and why” is critical for auditing, compliance, and executive trust. Without clear attribution, security controls can be harder to enforce, incident response may slow, and trust may be impacted.

This blog outlines the major updates to Uber’s identity and access technology stack in 2025 to accommodate AI agents. To maintain a proactive stance as AI adoption accelerates, we also offer a glimpse into our strategic roadmap for 2026 within this technical area.

The systems and approaches described reflect Uber’s internal architecture and controlled production environments. Design choices, performance characteristics, and security controls may vary across organizations, use cases, and deployment contexts.

### Motivation

Imagine an on-call engineer using an Oncall Agent to manage and resolve a system alert. In this scenario, the Investigation Agent determined the system was functioning correctly and the alert itself was misconfigured. The Investigation Agent then seamlessly passed the task to the Monitoring Agent to adjust the alert's threshold through a PR (pull request). The pull request shows a Monitoring Agent introducing the change, but the identity of the on-call engineer responsible remains untraceable.

![Workflow diagram showing an Oncall Engineer interacting with an Oncall Agent, which connects to both an Investigation Agent and a Monitoring Agent. Both agents feed into an MCP Tool Gateway (handling tool authorization and redaction), which then connects to Observability Systems and Source Control/CI (pull requests and tests).](https://cn-geo1.uber.com/image-proc/resize/udam/format=auto/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy80MzEyNTEzZC0yYzAzLTQwMTgtOTAzZi01OGJlN2Q1MWU3ZmYucG5n)

Figure 1: Agentic AI example.

We started observing this pattern across multiple use cases: an agent would take a multi-step path to get work done, but the systems it interacted with could only see a generic service identity at each hop. And the tool invocation appeared to downstream systems as “some service called an API,” even though the real actor was a specific agent acting on behalf of a specific user.

As agentic workflows expand to encompass more agents, tools, and systems, this challenge becomes increasingly pronounced. We distilled this into the following two core problems.

#### Problem 1: Current Identity Model Doesn’t Describe Agency

Today’s identity models are built around humans and workloads (often called non-human identity, or NHI, supported through credentials such as service account or API keys). An agent is best defined as an entity that is authorized to act for or in the place of another.  AI agents often run as workloads performing tasks on behalf of a human. In the above example, the Oncall Agent started a session on behalf of the on-call engineer to investigate and fix a specific issue.

#### Problem 2: Original Provenance Isn’t Effectively Carried Forward Across Agents to Systems

Execution context (originating user, intermediate agents) is dropped across agent hops. This leads to incomplete audits across the system and limits our ability to consistently leverage the fine-grained access policies already configured by downstream systems. In the absence of complete audit trails, incident response would require stitching partial audit logs across systems together. The PR opened by the Monitoring Agent should indicate that the on-call engineer requested solving a specific issue and some context around prior agent decisions that led to the PR.

It’s clear that agentic workflows behave differently than traditional automation:

- Delegation is the default mode - agents work on behalf of others
- Workflows are compositional - agents call other agents, tools, and systems
- Behavior is dynamic - plans evolve based on intermediate results as a session progresses

This defined the direction for what we had to build: foundations for agent identity and its propagation across agents that address the above problems.

### Architecture

As AI workflows scale, the interactions between autonomous agents and internal systems become deeply complex. To secure this ecosystem without stifling developer velocity, we decided to extend our existing Zero Trust Architecture for AI agents. Our architecture focuses on establishing verifiable cryptographic identity within the agent ecosystem and enforcing authorization for accessing downstream systems.

![Flowchart depicting an AI agent mesh architecture. The Michelangelo Platform registers agents with the Agent Registry, which interacts with the Security Token Service for JWTs. The AI Agent Mesh contains Oncall, Investigation, and Monitoring Agents. These agents connect to AI Gateway and MCP Gateway via AI Guard, which handles redaction. The AI Gateway communicates with an LLM, while the MCP Gateway connects to Downstream Systems. Control and data planes are labeled, and arrows indicate data flow and interactions between components.](https://cn-geo1.uber.com/image-proc/resize/udam/format=auto/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy8xZTFmOTM0Ni00MTZlLTQwODEtOGI2Ny00MDVjM2U0MWIyMWMucG5n)

Figure 2: Architecture.

The architecture comprises the following core components.

#### Agent Registry

At Uber, AI agents are often deployed as workloads, often managed by Kubernetes®. The [Michelangelo](https://www.uber.com/us/en/blog/from-predictive-to-generative-ai/) platform associates an AI agent to a workload. The Agent Registry serves as the source of truth, storing this registration. This is later used by the Security Token Service to verify the agent.

#### AI Agent Mesh

Analogous to the popular term [service mesh](https://en.wikipedia.org/wiki/Service_mesh), the AI Agent Mesh is the data plane where AI agents communicate with each other to complete tasks assigned to them. Within the Agent Mesh and for outbound calls (such as to MCP tools), AI agents rely on JWT tokens minted by the Security Token Service for authentication.

#### STS (Security Token Service)

Token minting for AI agents is handled by STS. Rather than relying on broad, long-lived service credentials, the STS acts as a dynamic trust broker that issues short-lived, scoped tokens for every hop.

#### MCP Gateway

MCP Gateway is a central system that mediates calls from the AI Agent Mesh to Uber’s systems. This design enables MCP Gateway to be a policy enforcement point for MCP tool invocations.

#### Downstream Systems

Once the MCP Gateway successfully authenticates the caller and authorizes the tool call, it securely proxies the request to the respective downstream services. These are primarily microservice APIs and datastores that execute the actual mutation or data retrieval.

#### AI Gateway

Beyond these components, an AI Gateway mediates all calls outbound from AI agents to AI models. This serves as the central point of integration for Uber with external APIs such as OpenAI®, Anthropic®, and others.  The AI Gateway is integrated with security guardrails to detect and handle prompt injection, jailbreaks, content safety, PII redaction, and more. Learn more about Uber’s AI Guard from our recent conference presentation [here](https://cfe5ada20.lwcdn.com/hls/4e490060-3632-4408-9e39-c9565b1768d7/playlist.m3u8).

To empower engineers and operational teams to build agentic solutions, the Michelangelo AI platform provides two options:

- **Code:** Write agents in Python using Uber’s internal production SDK. The SDK is orchestration-framework agnostic and supports common agent programming patterns (planning loops, tool use, state and memory), while providing standardized scaffolding, middleware hooks, observability, and evaluation tooling for production deployments.
- **No-code:** Author agents through the UI without writing any code. This lowers the barrier to entry and opens up the ability to build agents to the entire company beyond engineers.

Regardless of the options, the resulting AI agent gets deployed within Uber’s Kubernetes infrastructure.

Initially we considered building/adopting [agentgateway](https://github.com/agentgateway/agentgateway) that can proxy calls between AI agents. As Uber’s agentic AI ecosystem standardized heavily around the SDK, we instead integrated the solution directly into the SDK. We also found that fully addressing Problem 2 required support in the agent application layer, where execution context is created and propagated end-to-end, rather than relying only on an external proxy.

### Providing Agent Identities

Similar to microservices, AI agents run within workloads. The fundamental challenge to address was how to assign each individual agent a verifiable identity. Figure 3 shows our agent identity model and the process to mint a JWT token for the agent:

![Flowchart illustrating the process of Agent-1 in Workload-1 fetching an SVID from SPIRE, requesting a JWT from the Security Token Service, which verifies Agent-1's registration in the Agent Registry, and then returns the JWT to Agent-1. Each step is labeled and arrows indicate the direction of communication between components.](https://cn-geo1.uber.com/image-proc/resize/udam/format=auto/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy83Y2U2MDllNy02YzkyLTQzNzMtOWZmZi0zZjM4MDU3ZjM4YWQucG5n)

Figure 3: Providing an agent it’s identity.

We updated the SDK to add code to fetch the AI agent identity during runtime.

1. Every workload first fetches its own cryptographically signed workload SVID (SPIFFE Verifiable ID) from [SPIRE](https://www.uber.com/blog/our-journey-adopting-spiffe-spire). This proves the legitimacy of the underlying compute environment but doesn’t yet identify the agent.
2. The SDK uses its metadata available locally (like agent config), JWT from inbound calls and outbound destination audience to request a new JWT token from STS authenticated with the workload SVID. Only the STS is permitted to mint tokens for AI agents. By centralizing this process, we ensure that the actor chain carries the cryptographic record of every entity involved in the request.
3. STS integrates with the Agent Registry to verify that the requesting _agent\_id_ is explicitly authorized to run on that specific workload (from step 1). This prevents a workload from attempting to impersonate an agent that it isn’t authorized to host.
4. STS mints a JWT token and returns it to the requesting agent. This JWT is used for requests for the next hop of the agentic flow.

Here are some key features of this design:

- **Single-hop, short-lived tokens.** Every JWT minted by the STS is intended for a single hop, with a specific Audience claim and a short time-to-live in the order of minutes. A token issued for Agent A to call Agent B can’t be intercepted and replayed to call a database or another service; it’s valid only for that specific destination.
- **Full contextual attribution.** STS manages the token exchange at every step and embeds the fully attested actor chain into the token. This allows the MCP Gateway or downstream system to have the full context of the request; we see every participant in the lineage (e.g. engineer to Oncall Agent to Investigation Agent …) rather than just the immediate caller. This visibility allows for comprehensive audit logs and advanced workflow authorization that accounts for the full request lineage.
- **Extensible context.** JWT structure is designed to be extensible; we can seamlessly add additional claims in the future, such as session identifiers and request intent related claims, to provide richer context for policy decisions. This high-fidelity visibility ensures that a tool's execution can be authorized not just by the last hop, but by the verified intent of the entire chain.

By anchoring every agent identity in a SPIRE-backed workload credential and centralizing token exchange, we’re able to provide short-lived tokens while maintaining end-to-end traceability.

### Agent Identities in Action

To understand how agent identity manifests in a real-world workflow, let’s trace a typical request path. As agentic AI workflows involve calling multiple specialized agents to fulfill a complex user request, the identity must evolve at every boundary without losing its original context. Figure 4 shows a multi-hop investigation flow, from an initial user query to the final secure tool invocation:

![A flowchart showing an Oncall Engineer interacting with an Oncall Agent in Workload-1, which fetches a JWT from a Security Token Service. The Oncall Agent communicates with an Investigation Agent in Workload-2, which also fetches a JWT from the Security Token Service. The Investigation Agent then interacts with the MCP Gateway, passing along a JWT with an actor chain that includes the user, Oncall Agent, and Investigation Agent.](https://cn-geo1.uber.com/image-proc/resize/udam/format=auto/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy9kODRlMzQ5Mi00ZDYyLTRhZGItODEwMi1jZDFhNGFjYmFmNDcucG5n)

Figure 4: Agentic AI session life cycle.

1. An on-call engineer (user1) initiates a session with the Oncall Agent. At this entry point, the request is anchored by the user’s own personnel identity.
2. The Oncall Agent can’t reuse the user’s raw credentials to call downstream services. Instead, it contacts the Security Token Service. It presents its SPIRE-issued identity (Workload-1) and the user’s context to request a new JWT specifically scoped for the next-hop audience as Investigation Agent. STS responds with a JWT to the Oncall Agent. This per-hop mechanism for exchanging tokens is conceptually based on OAuth 2.0 Token Exchange ( [RFC 8693](https://datatracker.ietf.org/doc/html/rfc8693)) but is customized to transmit agent identity and provenance in a streamlined way that integrates with Uber's internal auditing and performance requirements.

![A JSON Web Token (JWT) payload with fields for issuer, subject, audience, issued at, expiration, agent ID, and an act_chain containing a chain of subjects and issued-at timestamps. Some numeric values are highlighted in red.](https://cn-geo1.uber.com/image-proc/resize/udam/format=auto/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy8zMDViZDI1ZC1mNmE0LTQ1MjAtODVlNi05YzMxYmI1OTNkNDYucG5n)

Figure 5: JWT for oncall agent about to call Workload-2.

3. The Oncall Agent sends the above JWT to the Investigation Agent (hosted within Workload-2).
4. The Investigation Agent verifies the signature and the audience. To call MCP Gateway, Investigation Agent performs its own token exchange with STS audience as MCP Gateway. This step is the same as step 2 above. The newly minted JWT carries a verifiable history of everyone involved: \[user1, oncall-agent, investigation-agent\].








![A JSON Web Token (JWT) payload with fields for issuer, subject, audience, issued at, expiration, agent ID, and an act_chain containing a chain of subjects and agent IDs, with timestamps highlighted in red.](https://cn-geo1.uber.com/image-proc/resize/udam/format=auto/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy81NWQxNTY0NS1jMzNiLTQ5ZTQtYjBhOS1hNzVkYmQzNDZjZDEucG5n)

Figure 6: JWT for investigation agent to MCP Gateway.

5. The MCP Gateway receives and verifies the JWT. Once verified, the Gateway enforces tool-level policies, which involves tool access checks and redaction of sensitive data if needed (also powered by AI Guard that we mentioned in the Architecture section). Policies are defined based on internal risk classification, and mandated for systems that we consider ‌high risk.

Having identity across the entire call chain of the request enables the system to enforce policies that are flexible enough to evaluate both the personnel identity (the human initiator) and the agent identity (the acting logic) simultaneously. As we evolve our IAM systems to support AI agents, we’re closely tracking emerging standards, particularly the IETF [WIMSE working group drafts](https://datatracker.ietf.org/wg/wimse/about/), along with relevant individual drafts such as “AI Agent Authentication and Authorization” ( [draft-klrc-aiagent-auth-01](https://datatracker.ietf.org/doc/draft-klrc-aiagent-auth/)), to stay aligned with the broader direction of the industry.

### Establishing a Paved Path

Several agents were built before the architecture was implemented. This posed a challenge: ensuring every agent consistently performs STS token exchanges and preserves the actor chain. To eliminate these gaps, we shifted from manual compliance to an automated, secure-by-default developer experience.

We developed a Standardized A2A (Agent-to-Agent) Client on top of the [A2A protocol](https://github.com/langchain-ai/agent-protocol). This client automates the STS JWT exchange and propagation of the actor chain, ensuring the secure path is also the easiest path for developers to implement A2A calls.

![Python code defining an abstract base class 'BaseAgentProtocolClient' for an agent-to-agent protocol client, including asynchronous methods for building authentication context, calling agents, and abstract methods for running and streaming operations.](https://cn-geo1.uber.com/image-proc/resize/udam/format=auto/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy85YWFkYmE5YS1iN2U3LTQxZjUtYTgwOS0xNGFhOGM4NTkzYWYucG5n)

Figure 7: A2A client requesting JWT token.

Additionally, we’re working with stakeholders to migrate existing use cases to use A2A clients. This involves a phased approach to identify legacy agent-to-agent calls and refactor them to use the standard A2A client. By providing dedicated support and testing guidelines, we ensure these existing agents get full lineage attribution and centralized auditability without disrupting their current functionality.

### Observability & Adoption

Our observability system provides a real-time, end-to-end view into agentic traffic, making complex multi-agent workflows transparent and auditable. By capturing each hop in the actor chain from the originating user through multiple agents and downstream tool invocations, it enables precise attribution of actions, along with associated authorization decisions and security context. This level of visibility is a top priority in a Zero Trust environment, where every interaction should be authenticated, authorized, and continuously monitored.

![Dark-themed dashboard titled 'Agent IAM Observability' displaying a session trace with multiple agents and MCP tools, showing user and agent identities, tool actions like reading logs, metrics, alerts, and source control, each marked as 'ALLOWED' with color-coded steps and a search/filter bar at the top.](https://cn-geo1.uber.com/image-proc/resize/udam/format=auto/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy8wZjEwYzlhMi1iNDFmLTRjMjMtYTFmZi03MDY0N2MxOWRmZjgucG5n)

Figure 8: Actor chain trace observability.

The system has been adopted by thousands of internal agents. A common concern when introducing per-hop token exchange is the potential for increased latency. In a high-scale environment like Uber, where a single agentic task might involve dozens of tool calls and agent delegations, even a few milliseconds of overhead can compound rapidly. Our production metrics show that this security model maintains low latency under current load conditions. The graph below showcases that P99 latency for the STS Token Exchange API is consistently _below 40 milliseconds_. We intend to keep scaling this system as agentic AI adoption grows at Uber.

![Yellow line graph displaying P99 latency for security-token-service endpoints over several days, with latency values mostly below 10 ms but occasional spikes reaching up to 40 ms. Time range spans from March 30 to April 2.](https://cn-geo1.uber.com/image-proc/resize/udam/format=auto/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy9jNTIwNjM1My03ZDZjLTRlOTItYWMxNC0zNjEwMGE4ZWE3NDkucG5n)

Figure 9: Agent token exchange p99 latency.

In production environments, agent interactions are subject to standard security and governance controls, including policy enforcement, monitoring, and audit logging to ensure safe and compliant operation.

# Conclusion

As we think about the future of AI identity and access, we frame our direction in the 3 layers shown in Figure 10.

![Three stacked boxes describe components of agentic AI security: Unified Enforcement Plane (policy decisions, features: observability, audit, governance, central policy), Dynamic Access Control (context-based permissions, features: adaptive access, human-in-the-loop, workflow authorization), and Identity & Trust Foundation (agent identity and context, features: agent identity, context propagation, trust definition).](https://cn-geo1.uber.com/image-proc/resize/udam/format=auto/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy82MTg2ZjllNi01NWI0LTQyOWEtYWExZi1iNzUzMjNjNGYwMjQucG5n)

Figure 10: Agentic IAM direction.

The first is the Identity & Trust Foundation - establishing a verifiable, cryptographic identity for every agent and preserving the full chain of delegation from user to agent to tool. This is the layer we’ve primarily focused on in this blog.

On top of that foundation sits Dynamic Access Control, followed by a Unified Policy Enforcement Plane that enables observability and expresses business-level controls consistently across tools, sessions, and protocols. In an agent-driven world, static human-managed permissions and fragmented enforcements don’t scale.

Our long-term vision is a cohesive architecture where identity, risk, and policy work together seamlessly - so humans and AI agents can collaborate at machine speed while maintaining strong trust and security controls.

## Acknowledgments

_Anthropic is a registered trademark of Anthropic, PBC._

_Kubernetes®, Model Context Protocol (MCP)  and its logo are registered trademarks of The Linux Foundation® in the United States and other countries. No endorsement by The Linux Foundation is implied by the use of these marks._

_OpenAI® and its logos are registered trademarks of OpenAI®._

Cover Photo Attribution: Image created by ChatGPT

Stay up to date with the latest from Uber Engineering - follow us on [LinkedIn](https://p.uber.com/eng-linkedin) for our newest blog posts and insights.

Written by

![Matt Mathew](https://cn-geo1.uber.com/image-proc/crop/resizecrop/udam/format=auto/width=64/height=64/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy8yZTI4ZDgzMS04MGZmLTU3ZjEtOWU3MS1jYjI1OTFjNGUxNWIuanBlZw==)

MM

Matt Mathew

Sr Staff Engineer

Matt is a Sr. Staff Engineer on the Engineering Security team at Uber. He currently works on various projects in the security domain. Previously, he led the initiative to containerize and automate Data infrastructure at Uber.

![Prasad Borole](https://cn-geo1.uber.com/image-proc/crop/resizecrop/udam/format=auto/width=64/height=64/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy8xZDc2YTRkMi02YzI1LTU4YjctOGJiMS1lOTU1MzZmYjcwYTkucG5n)

PB

Prasad Borole

Staff Software Engineer

Prasad is a Staff Software Engineer on the AI Security team within Core Security Engineering at Uber. He leads initiatives in the areas of agent security and risk-adaptive access control.

![Meng Huang](https://cn-geo1.uber.com/image-proc/crop/resizecrop/udam/format=auto/width=64/height=64/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy9iYWZlODk3MS00ZWUwLTRlOWItODEyMi1jNjE3MTdkYTZkOWMucG5n)

MH

Meng Huang

Engineering Manager

Meng leads teams within Engineering Security at Uber focused on identity, access control, and infrastructure for securing agentic systems at scale. Previously, he led several 0-to-1 platform initiatives across customer data, sign-up and login, and account management.

![Sergey Burykin](https://cn-geo1.uber.com/image-proc/crop/resizecrop/udam/format=auto/width=64/height=64/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy9hNzQ5YTdhZC04OWExLTRjNzMtODBhNi0xNWI4ZWI5ZWZjZjMuanBlZw==)

SB

Sergey Burykin

Sr Software Engineer

Sergey is on the AI Security team within Core Security Engineering at Uber. He leads the design and development of Uber’s agent security platform, including Agent Identity framework, and MCP Gateway security, establishing secure identity propagation and standardized access for AI agents.

![Gaurav Goel](https://cn-geo1.uber.com/image-proc/crop/resizecrop/udam/format=auto/width=64/height=64/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy8zZjg0NTczMi00Y2NmLTQwM2UtOWMyNy02YjUwYmEzMmY5OWQuanBlZw==)

GG

Gaurav Goel

Software Engineer II

Gaurav is a Software Engineer on the AI Security team within Core Security Engineering at Uber. He focuses on the design and development of the Agent Identity framework, ensuring secure and seamless integrations across the Uber ecosystem.

![Bayard Walsh](https://cn-geo1.uber.com/image-proc/crop/resizecrop/udam/format=auto/width=64/height=64/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy9hYjI1Y2I3Yi1hYTY1LTRlMWMtYTFjNi02MmE2YjQyODBhNTIuanBlZw==)

BW

Bayard Walsh

Software Engineer I

Bayard is a Software Engineer on the AI Security team within Core Security Engineering at Uber. He designs and develops Uber’s agent security platform, including Agent Identity framework, MCP Gateway security, and secure third-party MCP access.

Category

[Engineering](https://www.uber.com/us/en/blog/engineering/) [Uber AI](https://www.uber.com/us/en/blog/engineering/uber-ai/) [Security](https://www.uber.com/us/en/blog/engineering/security/)

Related articles

6 articles

![](https://cn-geo1.uber.com/image-proc/crop/resizecrop/udam/format=auto/width=407/height=0/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy80ZWRlMzQ1OS1lNGE2LTRlNWYtYWExOC00YWE5M2UwMWEzNGIucG5n)

Engineering

Uber AI

[Scaling Real-Time Traffic Forecasting with a Graph-Aware Transformer](https://www.uber.com/us/en/blog/scaling-real-time-traffic/)

May 19, 2026

![](https://cn-geo1.uber.com/image-proc/crop/resizecrop/udam/format=auto/width=407/height=0/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy80NjdiZmE2Mi1jNDMzLTQ4NzMtYTU0OC04MjQ3YjI3ODdhMzYuanBlZw==)

Backend

Data / ML

Engineering

[Beyond Prediction: Solving the Multiple Knapsack Problem at Scale: How Uber Optimizes Incentives](https://www.uber.com/us/en/blog/solving-multiple-knapsack/)

May 14, 2026

![](https://cn-geo1.uber.com/image-proc/crop/resizecrop/udam/format=auto/width=407/height=0/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy9mY2MwOGExMy0xNmM1LTQwZmEtYTQ2ZC02NzlkYzY5YzQ3YzEucG5n)

Engineering

Uber AI

[Lessons from Building a First-Pass AI PRD Reviewer at Uber](https://www.uber.com/us/en/blog/first-pass-prd/)

May 12, 2026

![](https://cn-geo1.uber.com/image-proc/crop/resizecrop/udam/format=auto/width=407/height=0/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy9hOTc0M2Q4Ni1kNzhmLTQ1OTUtODY5MC04NDkxNzM3MzAxYWQuanBlZw==)

Backend

Engineering

[Zero-Growth Stack, Real Gains: How Stack Allocation Can Save 10% CPU in Go](https://www.uber.com/us/en/blog/zero-growth-stack/)

May 7, 2026

![](https://cn-geo1.uber.com/image-proc/crop/resizecrop/udam/format=auto/width=407/height=0/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy9lYTYzOGFiMC0yOGRhLTQwNWYtYWYwMy1hNTAyMTk3MDNlY2YucG5n)

Engineering

Uber AI

[The 5 Layers Every Cloud Commitment Depends On](https://www.uber.com/us/en/blog/five-layers-cloud/)

May 4, 2026

![](https://cn-geo1.uber.com/image-proc/crop/resizecrop/udam/format=auto/width=407/height=0/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy9iYzA2ZWY4Yy1kYjg1LTRjN2QtOTk4YS0zYmY5M2JlOGZmYzkuanBlZw==)

Backend

Engineering

[How Ansible® Automation Powers the Uber Corporate Network at a Global Scale](https://www.uber.com/us/en/blog/ansible-automation-powers/)

April 30, 2026

## Select your preferred language

[English](https://www.uber.com/us/en/blog/solving-the-agent-identity-crisis/)

- ![](https://tb-static.uber.com/prod/udam-assets/b13c9264-0416-4e8f-bb02-737a108f36ae.svg)



### Products









  - [Advertising\\
    \\
    Learn more about advertising on Uber. Reach consumers as they go anywhere and get anything.](https://www.uber.com/us/en/blog/advertising/)

  - [Earn\\
    \\
    Resources for driving and delivering with Uber](https://www.uber.com/us/en/blog/earn/)

  - [Ride\\
    \\
    Experiences and information for people on the move](https://www.uber.com/us/en/blog/ride/)

  - [Eat\\
    \\
    Ordering meals for delivery is just the beginning with Uber Eats](https://www.uber.com/us/en/blog/eat/)

  - [Merchants\\
    \\
    Putting stores within reach of a world of customers](https://www.uber.com/us/en/blog/merchants/)

  - [Business\\
    \\
    Transforming the way companies move and feed their people](https://www.uber.com/us/en/blog/business/)

  - [Freight\\
    \\
    Taking shipping logistics in a new direction](https://www.uber.com/us/en/blog/freight/)

  - [Health\\
    \\
    Moving care forward together with medical providers](https://www.uber.com/us/en/blog/health/)

  - [Higher Education\\
    \\
    Enhancing campus transportation](https://www.uber.com/us/en/blog/higher-education/)

  - [Transit\\
    \\
    Expanding the reach of public transportation](https://www.uber.com/us/en/blog/transit/)
- ![](https://cn-geo1.uber.com/image-proc/crop/resizecrop/udam/format=auto/width=0/height=0/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy8yNzk4ODM0OC0wY2JkLTRjNWMtYmUzYS1mNTMzZjQ4ZDAwNDcucG5n)



### Company









  - [Engineering\\
    \\
    The technology behind Uber Engineering](https://www.uber.com/us/en/blog/engineering/)

  - [Community support\\
    \\
    Doing the right thing for cities and communities globally](https://www.uber.com/us/en/blog/community-support/)

  - [Newsroom\\
    \\
    Uber news and updates in your country](https://www.uber.com/us/en/newsroom/)

  - [Uber.com\\
    \\
    Product, how-to, and policy content—and more](https://www.uber.com/)
- [Help](https://help.uber.com/)


EN

## Select your preferred language

[English](https://www.uber.com/us/en/blog/solving-the-agent-identity-crisis/)

[![](https://tb-static.uber.com/prod/udam-assets/80bb7bdd-6cf4-4053-94c5-2e4e53d9d5f6.svg)\\
\\
**Ride**](https://m.uber.com/looking/)

[![](https://tb-static.uber.com/prod/udam-assets/d4ca3837-f9df-473b-9099-85505187cb2a.svg)\\
\\
**Drive & deliver**](https://drivers.uber.com/)

[![](https://tb-static.uber.com/prod/udam-assets/839bd4f4-306c-4b1b-b0e8-ab9cc8fd65c7.svg)\\
\\
**Uber Eats**](https://ubereats.com/login-redirect/)

[![](https://tb-static.uber.com/prod/udam-assets/0d73ead7-7739-4bb3-b79b-ded048dba1e1.svg)\\
\\
**Business**](https://business.uber.com/)

[![](https://tb-static.uber.com/prod/udam-assets/e3f56da1-d0d0-4ddb-a97a-62451d4164ef.svg)\\
\\
**Drive & deliver**](https://drivers.uber.com/)

[![](https://tb-static.uber.com/prod/udam-assets/ccb36d13-2a48-47a7-a01a-2b5f78973293.svg)\\
\\
**Ride**](https://m.uber.com/login-redirect)

[![](https://tb-static.uber.com/prod/udam-assets/aeaa8bd6-4051-4372-bcc5-a8631cfbbcaa.svg)\\
\\
**Uber Eats**](https://ubereats.com/login-redirect/)

[![](https://tb-static.uber.com/prod/udam-assets/2a2a1bb3-c25a-4b46-b64d-b8b1ec5e6969.svg)\\
\\
**Uber for Business**](https://business.uber.com/)

[![](https://tb-static.uber.com/prod/udam-assets/33188c4f-3728-4287-9447-50da6f123c2f.svg)\\
\\
**Manage account**](https://account.uber.com/)

[**Sign out**](https://auth.uber.com/login/logout)
