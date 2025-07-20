---
title: "Building A Secure Agentic AI Application Leveraging Google’s A2A Protocol"
tags:
   - A2A Protocol
   - Agentic AI
   - Interoperability
   - Threat Modeling
   - Security Analysis
link: https://arxiv.org/html/2504.16902v1
date: 2025-05-04
description: "The paper thoroughly examines the security framework of Google’s Agent-to-Agent (A2A) protocol, emphasizing its importance as multi-agent AI systems evolve. It employs the MAESTRO threat modeling framework to identify vulnerabilities, including impersonation, replay attacks, and artifact tampering. Recommendations include robust digital signature protocols, session management, idempotency in tasks, and enhanced input validation. Moreover, the paper advocates for secure development practices, such as implementing Zero Trust principles and continuous monitoring. This comprehensive analysis equips developers with actionable strategies to ensure resilient A2A applications in increasingly complex operational landscapes."
---

[License: CC BY 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2504.16902v1 \[cs.CR\] 23 Apr 2025

# Building A Secure Agentic AI Application Leveraging Google’s A2A Protocol

Report issue for preceding element

Idan Habler121These authors contributed equally to this work.2This work is not related to the author’s position at Intuit
Adversarial AI Security reSearch (A2RS)

Intuit

idan\_habler@intuit.com [![[Uncaptioned image]](https://arxiv.org/html/extracted/6381309/orcid_logo.png)](https://orcid.org/0000-0003-3423-5927 "")Ken Huang13

Prashant Kulkarni153This work is not related to the author’s position at DistributedApp.ai5This work is not related to the author’s position at Google
Agentic AI Security

DistributedApps.ai

ken.huang@distributedapps.ai [![[Uncaptioned image]](https://arxiv.org/html/extracted/6381309/orcid_logo.png)](https://orcid.org/0009-0004-6502-3673 "")Google Cloud

Google

pskulkarni@google.com [![[Uncaptioned image]](https://arxiv.org/html/extracted/6381309/orcid_logo.png)](https://orcid.org/0009-0004-2344-4840 "")Vineeth Sai Narajala144This work is not related to the author’s position at Amazon Web Services.
Proactive Security

Amazon Web Services

vineesa@amazon.com [![[Uncaptioned image]](https://arxiv.org/html/extracted/6381309/orcid_logo.png)](https://orcid.org/0009-0007-4553-9930 "")

Report issue for preceding element

###### Abstract

Report issue for preceding element

As Agentic AI systems evolve from basic workflows to complex multi-agent collaboration, robust protocols such as Google’s Agent2Agent (A2A) become essential enablers. To foster secure adoption and ensure the reliability of these complex interactions, understanding the secure implementation of A2A is essential. This paper addresses this goal by providing a comprehensive security analysis centered on the A2A protocol. We examine its fundamental elements and operational dynamics, situating it within the framework of agent communication development. Utilizing the MAESTRO framework, specifically designed for AI risks, we apply proactive threat modeling to assess potential security issues in A2A deployments, focusing on aspects such as Agent Card management, task execution integrity, and authentication methodologies.

Report issue for preceding element

Based on these insights, we recommend practical secure development methodologies and architectural best practices designed to build resilient and effective A2A systems. Our analysis also explores how the synergy between A2A and the Model Context Protocol (MCP) can further enhance secure interoperability. This paper equips developers and architects with the knowledge and practical guidance needed to confidently leverage the A2A protocol for building robust and secure next-generation agentic applications.

Report issue for preceding element

###### Index Terms:

Report issue for preceding element
Agentic AI, Google Agent2Agent, Agent-to-Agent Communication, A2A Protocol, Security, Threat Modeling, MAESTRO, MCP, Interoperability, Secure Development

## I Introduction

Report issue for preceding element

The emergence of intelligent, autonomous agents marks a pivotal shift in how AI systems are developed, deployed, and scaled. As these agents increasingly interact across organizational and technological boundaries, the need for secure, interoperable communication becomes critical. This paper begins by exploring the foundation of this transformation: the rise of Agentic AI and the protocols that enable it.

Report issue for preceding element

### I-AThe Rise of Agentic AI and the Need for Secure Interoperability

Report issue for preceding element

As artificial intelligence systems evolve from isolated, task-specific models to dynamic, multi-agent ecosystems, we are witnessing the emergence of Agentic AI—intelligent agents capable of autonomous decision-making, tool use, and collaboration with other agents and humans. These agents do not merely respond to prompts; they initiate actions, delegate subtasks, coordinate with peers, and adapt to new goals in real time. From AI research assistants that plan literature reviews to supply chain agents negotiating logistics across organizations, agentic AI is rapidly becoming the backbone of next-generation intelligent applications.
However, as these agents interact and compose workflows across organizational, geographical, and trust boundaries, the need for secure, standardized interoperability becomes paramount. Without a shared protocol for identity, authentication, task exchange, and auditability, agent interactions are prone to fragmentation, redundancy, and most critically—security vulnerabilities. Threats such as impersonation, data exfiltration, task tampering, and unauthorized privilege escalation can quickly arise in loosely governed agent ecosystems.
To address this, secure interoperability protocols like Google’s Agent-to-Agent (A2A) specification offer a promising foundation. A2A provides a declarative, identity-aware framework for enabling structured, secure communication between agents—whether human-authored or AI-powered.
Such protocols enable agents to share descriptive information about their capabilities, which is essential for facilitating effective interaction, discovery, and interoperability. This exchanged information, especially when received from potentially untrusted peers, must be handled with care and rigorously validated to prevent manipulation techniques like prompt injections.
Realizing the full potential of agentic AI will depend not only on such protocol standards, but on robust implementations, rigorous threat modeling, and continuous security adaptation. To aid developers in building secure systems, we also offer a repository containing secure A2A coding examples 111 [https://github.com/kenhuangus/a2a-secure-coding-examples](https://github.com/kenhuangus/a2a-secure-coding-examples "").

Report issue for preceding element

This paper explores the security architecture of A2A, identifies critical risks through the MAESTRO threat modeling lens  \[ [1](https://arxiv.org/html/2504.16902v1#bib.bib1 ""), [2](https://arxiv.org/html/2504.16902v1#bib.bib2 "")\] and proposes mitigation strategies and implementation best practices to ensure that agentic systems remain not just intelligent—but trustworthy by design.

Report issue for preceding element

### I-BGoogle A2A: A Foundational Protocol and its Context

Report issue for preceding element

The Agent-to-Agent (A2A) protocol, introduced by Google, represents a significant step forward in enabling structured, secure, and interoperable communication between autonomous agents. Designed with composability and trust in mind, A2A allows agents to discover each other via standardized AgentCards, authenticate using modern cryptographic protocols, and exchange tasks in a declarative, auditable manner. Its architecture reflects the growing demand for modular AI systems that can scale across organizations, tools, and domains—while remaining adaptable to both human and machine-driven workflows. A2A’s emergence is timely, as the AI ecosystem increasingly shifts toward open-ended, agent-driven applications in areas like research, enterprise automation, cybersecurity, and scientific collaboration. Positioned at the intersection of protocol engineering and AI orchestration, A2A provides the plumbing needed to build reliable, multi-agent ecosystems—where interoperability and security are not afterthoughts, but built-in foundations.

Report issue for preceding element

### I-CPaper Objectives: Analyzing A2A, Proposing Enhancements, and Guiding Secure Implementation

Report issue for preceding element

This paper sets out to examine the Agent-to-Agent (A2A) protocol in both its theoretical design and practical deployment, with the overarching goal of enabling secure and trustworthy agentic AI systems. First, we analyze the A2A protocol through the lens of the MAESTRO threat modeling framework, identifying a comprehensive set of risks that emerge in multi-agent environments—including spoofing, task replay, privilege escalation, and prompt injection. Building on this analysis, we propose targeted security enhancements to strengthen the protocol and its implementations, ranging from cryptographic controls and schema enforcement to secure session handling and fine-grained authorization. Finally, the paper outlines a set of implementation best practices for building hardened A2A servers and clients, offering guidance on secure communication, authentication workflows, logging, and abuse prevention. By bridging the gap between protocol specification and real-world deployment, this paper aims to equip developers, researchers, and architects with actionable insights for designing secure-by-default agentic ecosystems.

Report issue for preceding element

## II Literature Review

Report issue for preceding element

### II-AAgent to Agent Communication Literature Review

Report issue for preceding element

Agent-to-agent communication is fundamental to multi-agent systems (MAS), enabling autonomous entities to coordinate and collaborate to solve complex problems \[ [3](https://arxiv.org/html/2504.16902v1#bib.bib3 "")\]. Efficient and secure communication protocols are critical for sophisticated agent interactions across heterogeneous platforms. This review synthesizes the historical development, protocols, theoretical foundations, applications, challenges, and future directions of agent communication, with a focus on secure A2A multi-agent systems.

Report issue for preceding element

Early agent communication languages (ACLs) emerged from the Knowledge Sharing Effort (KSE) in the early 1990s \[ [4](https://arxiv.org/html/2504.16902v1#bib.bib4 "")\]. KQML, the pioneering ACL, defined a multi-layered architecture including content, message, and communication layers using speech act theory through performatives to specify message intentions \[ [3](https://arxiv.org/html/2504.16902v1#bib.bib3 "")\]. Building upon KQML, the FIPA ACL sought more rigor with a semantic framework based on modal logic, feasibility preconditions, and rational effects \[ [5](https://arxiv.org/html/2504.16902v1#bib.bib5 ""), [6](https://arxiv.org/html/2504.16902v1#bib.bib6 "")\]. These ACLs are based on speech act theory, formal semantics, and the Belief-Desire-Intention (BDI) model \[ [7](https://arxiv.org/html/2504.16902v1#bib.bib7 "")\].

Report issue for preceding element

Key protocols include KQML with its LISP-like syntax, and FIPA ACL which refines message structure and semantics with defined preconditions and outcomes \[ [3](https://arxiv.org/html/2504.16902v1#bib.bib3 "")\]. Protocols define interaction sequences between agents, including request, query, contract net, auction, and subscription \[ [5](https://arxiv.org/html/2504.16902v1#bib.bib5 "")\]. Recent efforts like Google’s A2A protocol aim to enable seamless interoperability between AI agents across different frameworks by standardizing task negotiation, capability sharing, and secure communication \[ [8](https://arxiv.org/html/2504.16902v1#bib.bib8 "")\].

Report issue for preceding element

Communication architectures in MAS can be direct (full, partial, or dynamic networks) or mediated (facilitator-based, blackboard systems, or global control) \[ [9](https://arxiv.org/html/2504.16902v1#bib.bib9 "")\]. Multi-agent reinforcement learning (MARL) allows agents to learn when, how, and what to communicate using differentiable, reinforcement, supervised, or regularized communication learning methods \[ [10](https://arxiv.org/html/2504.16902v1#bib.bib10 "")\].

Report issue for preceding element

Applications of agent communication range across enterprise knowledge management, customer service, supply chain management, healthcare, smart grids, autonomous vehicles, e-commerce, and disaster response \[ [9](https://arxiv.org/html/2504.16902v1#bib.bib9 ""), [5](https://arxiv.org/html/2504.16902v1#bib.bib5 "")\]. Security, trust, and the potential manipulation of feedback loops present inherent challenges. Integration with existing standards, scaling communication for efficiency, and handling non-stationarity in learning processes are open research areas \[ [4](https://arxiv.org/html/2504.16902v1#bib.bib4 ""), [11](https://arxiv.org/html/2504.16902v1#bib.bib11 ""), [5](https://arxiv.org/html/2504.16902v1#bib.bib5 "")\].

Report issue for preceding element

Future research should focus on multimodal communication, structured communication networks, robust centralized components, interpretable emergent languages, and integration with LLMs. Initiatives like A2A and MCP are aiming for protocol convergence for standardized agent communication, although many questions regarding how this may emerge are still unanswered. Effective communication remains crucial for the success of agent systems. Security must be considered throughout their evolution.

Report issue for preceding element

### II-BTraditional PKI and Transport Security

Report issue for preceding element

Early implementations of secure agentic systems leveraged public key infrastructure (PKI), with each agent provisioned a certificate and private key signed by a trusted certificate authority. This approach, frequently combined with SSL/TLS at the transport layer, guaranteed encrypted channels for agent communication \[ [12](https://arxiv.org/html/2504.16902v1#bib.bib12 "")\]. While PKI solutions remain fundamental to securing multi-agent messages, they often required complex certificate management, especially as agent populations grew or changed dynamically. Agent platforms such as JADE (Java Agent DEvelopment Framework) attempted to simplify this via security extensions that integrated PKI-based authentication \[ [13](https://arxiv.org/html/2504.16902v1#bib.bib13 "")\].

Report issue for preceding element

### II-CSOAP, WS-Security, and Enterprise Service Buses

Report issue for preceding element

Prior to the widespread adoption of RESTful services, enterprise-grade agentic applications often employed SOAP as the foundational protocol. The WS-Security suite \[ [14](https://arxiv.org/html/2504.16902v1#bib.bib14 "")\] provided message-level encryption, signatures, and token-based authentication for agent-to-service or agent-to-agent interactions. These frameworks were robust but verbose; they were well-suited to closed enterprise environments yet burdensome for lightweight agentic systems or real-time AI workflows. Still, they established fundamental principles of end-to-end message confidentiality, integrity, and non-repudiation at a time when microservices and ephemeral containers were not standard practice.

Report issue for preceding element

### II-DOAuth 2.0, JSON Web Tokens (JWT), and Service Accounts

Report issue for preceding element

With the shift to cloud and user-centric web applications, OAuth 2.0 became the de facto framework for delegated authorization \[ [15](https://arxiv.org/html/2504.16902v1#bib.bib15 "")\]. However, OAuth 2.0’s flows primarily focus on interactive user login. This made it challenging for autonomous agents to securely obtain and renew tokens without user intervention. JSON Web Tokens (JWT) \[ [16](https://arxiv.org/html/2504.16902v1#bib.bib16 "")\] introduced a lightweight format for securely transmitting agent identity and privileges. Many practitioners adopted service accounts or “robot accounts” with static credentials to simulate user roles in an agent scenario, though this introduced key-rotation and secret-management complexities.

Report issue for preceding element

### II-EZero-Trust Architectures and BeyondCorp

Report issue for preceding element

As multi-agent systems expanded across hybrid cloud environments, Zero-Trust principles emphasized continuous validation of identity and authorization, even for internal requests \[ [17](https://arxiv.org/html/2504.16902v1#bib.bib17 "")\]. Solutions like Google’s BeyondCorp architecture applied these principles, requiring every agent or service to authenticate with strong, verifiable credentials irrespective of network location \[ [18](https://arxiv.org/html/2504.16902v1#bib.bib18 "")\]. This paved the way for “never trust, always verify” policies, which align closely with the needs of autonomous AI agents that may operate across heterogeneous network boundaries.

Report issue for preceding element

### II-FLimitations of Historical Approaches

Report issue for preceding element

The historical approaches to securing agentic AI systems shared several common limitations:

Report issue for preceding element

- •


Manual Credential Management: Significant manual effort was required to provision, rotate, and revoke agent credentials.

Report issue for preceding element

- •


Adapting User-Centric Models: Substantial work was needed to adapt inherently user-centric security workflows to machine-only environments.

Report issue for preceding element

- •


Fragmented Implementations: The lack of uniform standards or cloud-native support for fully autonomous agents resulted in inconsistent security implementations.

Report issue for preceding element

- •


Scaling Challenges: As agent populations grew, the operational complexity of maintaining secure communication increased exponentially.

Report issue for preceding element


These early innovations and their limitations highlighted the fundamental importance of establishing robust identity and trust mechanisms for distributed AI, while also underscoring the need for simpler, more automated credential exchange processes specifically designed for autonomous agent interactions.

Report issue for preceding element

## III Understanding Google’s A2A Protocol

Report issue for preceding element

### III-AProtocol Overview

Report issue for preceding element

The A2A protocol facilitates communication between two primary types of agents:

Report issue for preceding element

- •


Client Agent: Responsible for formulating and communicating tasks.

Report issue for preceding element

- •


Remote Agent: Responsible for acting on those tasks to provide information or take action.

Report issue for preceding element


Built on established web standards including HTTP, JSON-RPC, and Server-Sent Events (SSE), A2A prioritizes compatibility with existing systems while maintaining a security-first approach. Its design follows several key principles:

Report issue for preceding element

- •


Agentic-first: Agents operate independently and communicate explicitly to exchange information, without shared memory or tools by default.

Report issue for preceding element

- •


Standards-compliant: Utilization of widely adopted web technologies minimizes developer friction.

Report issue for preceding element

- •


Secure by default: Integrated authentication and authorization measures safeguard sensitive data and transactions.

Report issue for preceding element


### III-BCommunication Flow

Report issue for preceding element

The A2A protocol defines a structured communication flow between agents that consists of several stages:

Report issue for preceding element

1. 1.


Discovery: The client fetches the target agent’s Agent Card (from /.well-known/agent.json) via HTTPS to learn about its capabilities, endpoint, and authentication requirements.

Report issue for preceding element

2. 2.


Initiation: After authenticating using a method specified in the Agent Card, the client sends a JSON-RPC request over HTTPS to the server’s a2aEndpointUrl using one of two methods:

Report issue for preceding element

- •


tasks.send: Used for potentially synchronous tasks or initiating tasks where immediate streaming isn’t required.

Report issue for preceding element

- •


tasks.sendSubscribe: Used for long-running tasks requiring streaming updates, establishing a persistent HTTPS connection for Server-Sent Events (SSE).

Report issue for preceding element


3. 3.


Processing & Interaction:

Report issue for preceding element

- •


Non-Streaming (tasks.send): The server processes the task and returns the final Task object in the HTTP response.

Report issue for preceding element

- •


Streaming (tasks.sendSubscribe): The server sends SSE messages over the persistent connection, including TaskStatusUpdateEvent (containing the updated Task object) and TaskArtifactUpdateEvent (containing generated Artifact objects).

Report issue for preceding element


4. 4.


Input Required: If additional input is needed, the server signals this via the response or an SSE event, and the client sends subsequent input using the same taskId.

Report issue for preceding element

5. 5.


Completion: The task transitions to a terminal state (completed, failed, or canceled), communicated via the final response or an SSE event.

Report issue for preceding element

6. 6.


Push Notifications (Optional): Servers supporting the pushNotifications capability can send asynchronous updates to a client-provided webhook URL, registered using tasks.pushNotification.set.

Report issue for preceding element


### III-CDiscoverability Mechanism

Report issue for preceding element

A central innovation of the A2A protocol is its robust discoverability mechanism, which enables agents to efficiently locate and leverage each other’s capabilities.

Report issue for preceding element

#### III-C1 AgentCard Structure

Report issue for preceding element

The AgentCard serves as the foundation of the A2A protocol’s discoverability mechanism. This structured JSON metadata file, located at the standardized path /.well-known/agent.json, functions as a machine-readable ”business card” describing an agent’s capabilities and interfaces. The AgentCard contains:

Report issue for preceding element

- •


Basic agent identification (name, version, provider).

Report issue for preceding element

- •


HTTPS endpoint URL for A2A communication (a2aEndpointUrl).

Report issue for preceding element

- •


Detailed function catalogs with parameter schemas.

Report issue for preceding element

- •


Required authentication methods using OpenAPI 3.x Security Scheme objects (e.g., apiKey, http bearer, oauth2, openIdConnect).

Report issue for preceding element

- •


Capability descriptions that define available functions.

Report issue for preceding element

- •


Hosted/DNS information detailing accessibility.

Report issue for preceding element


This standardized location creates a predictable discovery pattern across the entire A2A ecosystem, similar to how robots.txt and sitemap.xml function for web crawlers. The AgentCard’s JSON structure ensures both human readability and machine parsability, facilitating seamless integration between disparate agent systems.

Report issue for preceding element

### III-DCore Concepts

Report issue for preceding element

The A2A protocol is built around several fundamental concepts that structure agent interactions:

Report issue for preceding element

#### III-D1 AgentCard

Report issue for preceding element

As described earlier, the Agent Card is a public JSON metadata file that acts as a machine-readable business card. The quality and accuracy of Agent Cards can vary, which directly impacts discovery reliability and security posture advertisement.

Report issue for preceding element

#### III-D2 A2A Server

Report issue for preceding element

An agent exposing an HTTPS endpoint that implements the A2A JSON-RPC methods. It receives requests, manages task execution, and sends responses/updates.

Report issue for preceding element

#### III-D3 A2A Client

Report issue for preceding element

An application or another agent that consumes A2A services by sending JSON-RPC requests to a server’s a2aEndpointUrl. Clients can dynamically add and remove servers after launch, offering flexibility in how capabilities are discovered and utilized during runtime.

Report issue for preceding element

#### III-D4 Task

Report issue for preceding element

The fundamental unit of work in the A2A protocol, identified by a unique taskId provided by the client. Tasks progress through a defined lifecycle represented by TaskStatus values:

Report issue for preceding element

- •


TASK\_STATUS\_SUBMITTED

Report issue for preceding element

- •


TASK\_STATUS\_WORKING

Report issue for preceding element

- •


TASK\_STATUS\_INPUT\_REQUIRED

Report issue for preceding element

- •


TASK\_STATUS\_COMPLETED

Report issue for preceding element

- •


TASK\_STATUS\_FAILED

Report issue for preceding element

- •


TASK\_STATUS\_CANCELED

Report issue for preceding element


The protocol supports both short-lived request/response style interactions and long-running asynchronous tasks, making it suitable for complex workflows that may extend over days or weeks.

Report issue for preceding element

#### III-D5 Message

Report issue for preceding element

Represents a turn in the communication dialogue, containing a role (”user” for client-originated, ”agent” for server-originated) and one or more Parts.

Report issue for preceding element

#### III-D6 Part

Report issue for preceding element

The basic unit of content within a Message or Artifact. Defined types include:

Report issue for preceding element

- •


TextPart: For unstructured plain text communication.

Report issue for preceding element

- •


FilePart: For transferring files, either via inline Base64 encoded bytesContent or a URI reference.

Report issue for preceding element

- •


DataPart: For structured JSON data, identified by a mimeType (e.g., application/json).

Report issue for preceding element


#### III-D7 Artifact

Report issue for preceding element

Represents outputs generated by the agent during task execution (e.g., files, reports, structured data), also containing Parts.

Report issue for preceding element

## IV Threat Modeling Google A2A based Agentic AI Apps with MAESTRO

Report issue for preceding element

This section will focus on typical agentic AI applications built using Google A2A Applications. We will use the MAESTRO threat modeling framework \[ [1](https://arxiv.org/html/2504.16902v1#bib.bib1 "")\] and the work documented in \[ [2](https://arxiv.org/html/2504.16902v1#bib.bib2 "")\] to build application-specific threats for Agentic AI applications built using the Google A2A protocol. The next section will dive deep into strategies to mitigate the threats.

Report issue for preceding element

### IV-ARecap of MAESTRO Threat Modeling Methodology

Report issue for preceding element

Traditional threat modeling frameworks often fall short when applied to agentic AI systems. These systems can autonomously make decisions, interact with external tools, and learn over time – capabilities that introduce unique security risks. That’s why we’ll use the MAESTRO framework, a seven-layer threat modeling approach specifically designed for agentic AI. MAESTRO offers a more granular and proactive methodology uniquely suited for the complexities of agentic systems like those built using A2A.
MAESTRO (Multi-Agent Environment, Security, Threat, Risk, and Outcome) provides a structured, granular, and proactive methodology for identifying, assessing, and mitigating threats across the entire agentic AI lifecycle.

Report issue for preceding element

MAESTRO in a Nutshell:

Report issue for preceding element

- •


Extends Existing Frameworks: Builds upon established security frameworks like STRIDE, PASTA, and LINDDUN, but adds AI-specific considerations.

Report issue for preceding element

- •


Layered Security: Recognizes that security must be addressed at every layer of the agentic architecture.

Report issue for preceding element

- •


AI-Specific Threats: Focuses on the unique threats arising from AI, such as adversarial machine learning and the risks of autonomous decision-making.

Report issue for preceding element

- •


Risk-Based Approach: Prioritizes threats based on their likelihood and potential impact.

Report issue for preceding element

- •


Continuous Monitoring: Emphasizes the need for ongoing monitoring and adaptation.

Report issue for preceding element


The Seven Layers of MAESTRO (See Figure 1):

Report issue for preceding element

1. 1.


Foundation Models: The core AI models (e.g., LLMs) used by the agents.

Report issue for preceding element

2. 2.


Data Operations: The data used by the agents, including storage, processing, and vector embeddings.

Report issue for preceding element

3. 3.


Agent Frameworks: The software frameworks and APIs that enable agent creation and interaction (like the A2A protocol).

Report issue for preceding element

4. 4.


Deployment and Infrastructure: The underlying infrastructure (servers, networks, containers) that hosts the agents and API.

Report issue for preceding element

5. 5.


Evaluation and Observability: The systems used to monitor, evaluate, and debug agent behavior.

Report issue for preceding element

6. 6.


Security and Compliance: The security controls and compliance measures that protect the entire system.

Report issue for preceding element

7. 7.


Agent Ecosystem: The environment where multiple agents interact, including marketplaces, collaborations, and potential conflicts.

Report issue for preceding element


![Refer to caption](https://arxiv.org/html/extracted/6381309/figure-1-maestro.png)Figure 1: Maestro Architecture - 7 LayersReport issue for preceding element

### IV-BCommon A2A Multi-Agent System Threats

Report issue for preceding element![Refer to caption](https://arxiv.org/html/extracted/6381309/commonthreats.png)Figure 2: List of Common A2A Multi-Agent System Threats Identified by MAESTRO Threat Modeling MethodologyReport issue for preceding element

Leveraging MAESTRO threat modeling methodology, we identified potential threats for A2A multi-agent systems, which are illustrated in Figure [2](https://arxiv.org/html/2504.16902v1#S4.F2 "Figure 2 ‣ IV-B Common A2A Multi-Agent System Threats ‣ IV Threat Modeling Google A2A based Agentic AI Apps with MAESTRO ‣ Building A Secure Agentic AI Application Leveraging Google’s A2A Protocol") and detailed below:

Report issue for preceding element

#### IV-B1 Agent Card Spoofing

Report issue for preceding element

MAESTRO Layers: 3 (Agent Frameworks), 4 (Deployment & Infrastructure)

An attacker publishes a forged /.well-known/agent.json (Agent Card) at a malicious or typosquatting domain. When an A2A Client performs agent discovery, it may trust this fake card and send sensitive A2A Tasks to a rogue A2A Server. This can result in task hijacking, data exfiltration, and agent impersonation.

Report issue for preceding element

#### IV-B2 A2A Task Replay

Report issue for preceding element

MAESTRO Layers: 3 (Agent Frameworks), 2 (Data Operations)
If an attacker captures a valid tasks/send request and replays it to the A2A Server, the same A2A Task may be executed multiple times. Without replay protection, this leads to duplicate or unauthorized actions.

Report issue for preceding element

#### IV-B3 A2A Message Schema Violation

Report issue for preceding element

MAESTRO Layer: 2 (Data Operations)
A malicious A2A Client may craft malformed A2A Messages or Parts to exploit weak schema validation in the A2A Server, potentially causing code injection, privilege escalation, or denial of service.

Report issue for preceding element

#### IV-B4 A2A Server Impersonation

Report issue for preceding element

MAESTRO Layer: 4 (Deployment & Infrastructure)
Through DNS spoofing or network attacks, an adversary redirects A2A Client traffic to a fake A2A Server. The attacker can serve forged Agent Cards and Task results, undermining trust and stealing data.

Report issue for preceding element

#### IV-B5 Cross-Agent Task Escalation

Report issue for preceding element

MAESTRO Layers: 7 (Agent Ecosystem), 3 (Agent Frameworks)
A malicious agent enumerates available Agent Cards and attempts to escalate privileges by submitting A2A Tasks with forged credentials, breaching trust boundaries and accessing unauthorized data.

Report issue for preceding element

#### IV-B6 Artifact Tampering via A2A Artifacts

Report issue for preceding element

MAESTRO Layers: 2 (Data Operations), 3 (Agent Frameworks)
Attackers intercept or modify Artifacts exchanged during A2A Task execution, injecting malicious content or corrupting results.

Report issue for preceding element

#### IV-B7 Insider Threat/Logging Evasion via A2A Task Manipulation

Report issue for preceding element

MAESTRO Layers: 6 (Security & Compliance), 3 (Agent Frameworks)
A privileged user or agent manipulates Task state transitions or disables logging on the A2A Server, concealing unauthorized actions.

Report issue for preceding element

#### IV-B8 Supply Chain Attack via A2A Dependencies

Report issue for preceding element

MAESTRO Layers: 4 (Deployment & Infrastructure), 6 (Security & Compliance)
A compromised or vulnerable dependency in the A2A Server or Client can enable remote code execution or credential theft.

Report issue for preceding element

#### IV-B9 Authentication & Identity Threats

Report issue for preceding element

MAESTRO Layers: 3 (Agent Frameworks), 4 (Deployment & Infrastructure), 6 (Security & Compliance), 7 (Agent Ecosystem)
A2A-based systems use OAuth/OIDC with JWT tokens for identity validation. Threats include:

Report issue for preceding element

- •


Forged or stolen JWT tokens allowing unauthorized access to A2A Tasks or Agent Cards.

Report issue for preceding element

- •


Weak JWT validation (e.g., missing signature check, improper audience/issuer claims).

Report issue for preceding element

- •


Token replay or use of expired tokens.

Report issue for preceding element

- •


Insecure storage or transmission of tokens.

Report issue for preceding element


#### IV-B10 Poisoned AgentCard

Report issue for preceding element

MAESTRO Layers: 1 (Foundation Model), 2 (Data Operations)
An attacker embeds malicious instructions using prompt injection techniques within the fields of an AgentCard (e.g., AgentSkill id, name, descriptions, tags or examples). When another agent automatically ingests and processes this AgentCard data as part of its discovery or interaction flow, it may execute these hidden instructions.
This exploits the trust placed in AgentCard content (Data Operations) and the automated processing of this content using the foundation model during its planning. As a result, the agent’s goals being hijacked, sensitive data being revealed, or internal security protocols being bypassed, highlighting the need to treat AgentCard content as untrusted input requiring careful validation and sanitization.

Report issue for preceding element

### IV-CAdditional Security Considerations

Report issue for preceding element

In addition to the above specific controls, we think following additional security aspects should be considered:

Report issue for preceding element

- •


Supply chain dependencies must be scanned and verified. (Layers 4, 6)

Report issue for preceding element

- •


Incident response and recovery plans must be in place. (Layers 6, 7)

Report issue for preceding element

- •


Use open-source libraries for validation, authentication, and monitoring. (Layers 2, 3, 6)

Report issue for preceding element

- •


Prefer declarative security configurations (YAML/JSON) for infrastructure. (Layer 4)

Report issue for preceding element

- •


Integrate security testing (unit, integration, adversarial) into CI/CD pipelines. (Layers 3, 6)

Report issue for preceding element

- •


Document all agent capabilities and trust boundaries in the Agent Card. (Layers 3, 7)

Report issue for preceding element


## V Case Study

Report issue for preceding element

We will consider two case studies to understand the threat modeling of the agentic system.

Report issue for preceding element

### V-ACase Study 1: Collaborative Document Processing

Report issue for preceding element

In this scenario, multiple A2A Clients (from different vendors) discover and interact with an enterprise A2A Server to co-edit, summarize, and review documents. Each client retrieves the Agent Card, authenticates, and launches A2A Tasks via tasks/send.

Report issue for preceding element

1. 1.


Layer 1: Foundation Models — Prompt injection attacks can occur when adversarial input is embedded in A2A Message Parts, causing the LLM to behave unexpectedly.

Report issue for preceding element

2. 2.


Layer 2: Data Operations — Attackers may leak sensitive data through A2A Artifacts or tamper with A2A Task state.

Report issue for preceding element

3. 3.


Layer 3: Agent Frameworks — Vulnerable to Agent Card spoofing and replayed tasks/send requests, especially if malformed Agent Cards are accepted.

Report issue for preceding element

4. 4.


Layer 4: Deployment & Infrastructure — Risks include denial-of-service attacks via flooding the A2A Server with tasks, or lateral movement using compromised Agent Cards.

Report issue for preceding element

5. 5.


Layer 5: Evaluation & Observability — Log tampering or insufficient auditing of A2A Task transitions can let attacks go undetected.

Report issue for preceding element

6. 6.


Layer 6: Security & Compliance — Credential theft from Agent Cards or bypassing policies via misconfigured fields.

Report issue for preceding element

7. 7.


Layer 7: Agent Ecosystem — Enumeration of Agent Cards and Sybil attacks with fake cards can undermine trust in federated A2A deployments.

Report issue for preceding element


#### V-A1 Cross-Layer Vulnerabilities

Report issue for preceding element

- •


Compromised Agent Card enables attacker to hijack Task execution (Layer 3 →→\\rightarrow→ Layer 2).

Report issue for preceding element

- •


Weak authentication on A2A Server allows replayed Task requests (Layer 3 →→\\rightarrow→ Layer 6).

Report issue for preceding element

- •


Insufficient logging of Task state changes enables undetected attacks (Layer 5 →→\\rightarrow→ Layer 7).

Report issue for preceding element


#### V-A2 Risk Assessment

Report issue for preceding element

- •


Likelihood: High (open Agent Card discovery, multi-vendor federation)

Report issue for preceding element

- •


Impact: High (data loss, compliance breach, reputational damage)

Report issue for preceding element


### V-BCase Study 2: Distributed Data Analysis

Report issue for preceding element

Here, A2A Clients in different departments analyze sensitive datasets by launching A2A Tasks to a central A2A Server, aggregating results via Artifacts.

Report issue for preceding element

1. 1.


Layer 1: Foundation Models — Model inversion attacks may occur when adversarial input is embedded in A2A Message Parts, allowing attackers to extract sensitive data from LLMs.

Report issue for preceding element

2. 2.


Layer 2: Data Operations — Data poisoning in A2A Artifacts, unauthorized aggregation of Task results, tool poisoning, agent card poisoning, or tampering with distributed Task state are key threats.

Report issue for preceding element

3. 3.


Layer 3: Agent Frameworks — Susceptible to Task replay via tasks/send, Agent Card spoofing, and schema violations in Task or Message objects.

Report issue for preceding element

4. 4.


Layer 4: Deployment & Infrastructure — Risks include network eavesdropping on A2A Task traffic and A2A Server compromise.

Report issue for preceding element

5. 5.


Layer 5: Evaluation & Observability — Insufficient anomaly detection in Task audit logs or log forgery in Task status events can enable undetected attacks.

Report issue for preceding element

6. 6.


Layer 6: Security & Compliance — Data privacy violations due to misconfigured Agent Cards or weak encryption of Task data.

Report issue for preceding element

7. 7.


Layer 7: Agent Ecosystem — Data silo bridging via Agent Card enumeration and policy conflicts between federated A2A Servers can lead to unauthorized data flows.

Report issue for preceding element


#### V-B1 Cross-Layer Vulnerabilities:

Report issue for preceding element

- •


Poisoned A2A Artifacts corrupting analytics (Layer 2 →→\\rightarrow→ Layer 1)

Report issue for preceding element

- •


Weak Task orchestration enabling replay or hijacking (Layer 3 →→\\rightarrow→ Layer 4)

Report issue for preceding element

- •


Cross-department Agent Card trust failures (Layer 7 →→\\rightarrow→ Layer 6)

Report issue for preceding element


#### V-B2 Risk Assessment

Report issue for preceding element

- •


Likelihood: Medium-High (complexity, distributed trust)

Report issue for preceding element

- •


Impact: High (business intelligence compromise, regulatory risk)

Report issue for preceding element


### V-CThreat Evolution

Report issue for preceding element

Threats to A2A-based multi-agent systems evolve as the protocol, Agent Card registry, and deployment patterns change. Regular threat modeling via the MAESTRO methodology, and updates to identified threats, are essential to address new attack techniques and changes in the A2A ecosystem.

Report issue for preceding element

## VI Mitigating Security Threats in A2A-Based Multi-Agent Systems

Report issue for preceding element

Drawing from the MAESTRO threat modeling methodology, Section- [IV-B](https://arxiv.org/html/2504.16902v1#S4.SS2 "IV-B Common A2A Multi-Agent System Threats ‣ IV Threat Modeling Google A2A based Agentic AI Apps with MAESTRO ‣ Building A Secure Agentic AI Application Leveraging Google’s A2A Protocol") outlined several potential threats facing A2A-based MAS. This section delves into specific security controls and best practices to address these threats, as well as additional security considerations from Section- [IV-C](https://arxiv.org/html/2504.16902v1#S4.SS3 "IV-C Additional Security Considerations ‣ IV Threat Modeling Google A2A based Agentic AI Apps with MAESTRO ‣ Building A Secure Agentic AI Application Leveraging Google’s A2A Protocol"). Moreover, it re-contextualizes the case studies of Sections- [V-A](https://arxiv.org/html/2504.16902v1#S5.SS1 "V-A Case Study 1: Collaborative Document Processing ‣ V Case Study ‣ Building A Secure Agentic AI Application Leveraging Google’s A2A Protocol") and [V-B](https://arxiv.org/html/2504.16902v1#S5.SS2 "V-B Case Study 2: Distributed Data Analysis ‣ V Case Study ‣ Building A Secure Agentic AI Application Leveraging Google’s A2A Protocol") in light of those mitigations.

Report issue for preceding element

### VI-AAddressing Specific Threats and Enhancing Security

Report issue for preceding element

The following subsections detail mitigation strategies for each threat identified in Section- [IV-B](https://arxiv.org/html/2504.16902v1#S4.SS2 "IV-B Common A2A Multi-Agent System Threats ‣ IV Threat Modeling Google A2A based Agentic AI Apps with MAESTRO ‣ Building A Secure Agentic AI Application Leveraging Google’s A2A Protocol"), incorporating the additional considerations of Section- [IV-C](https://arxiv.org/html/2504.16902v1#S4.SS3 "IV-C Additional Security Considerations ‣ IV Threat Modeling Google A2A based Agentic AI Apps with MAESTRO ‣ Building A Secure Agentic AI Application Leveraging Google’s A2A Protocol"):

Report issue for preceding element

#### VI-A1 Addressing Agent Card Spoofing

Report issue for preceding element

Addressing Section- [IV-B1](https://arxiv.org/html/2504.16902v1#S4.SS2.SSS1 "IV-B1 Agent Card Spoofing ‣ IV-B Common A2A Multi-Agent System Threats ‣ IV Threat Modeling Google A2A based Agentic AI Apps with MAESTRO ‣ Building A Secure Agentic AI Application Leveraging Google’s A2A Protocol")
Agent Card Spoofing, where an attacker publishes a forged /.well-known/agent.json (Agent Card) at a malicious domain, poses a significant risk of task hijacking, data exfiltration, and agent impersonation.

Report issue for preceding element

Mitigation Strategies:

Report issue for preceding element

- •


Digital Signatures on Agent Cards: Use digital signatures via a trusted Certificate Authority (CA) to ensure authenticity and integrity.

Report issue for preceding element

- •


Secure Agent Card Resolution: Use HTTPS with certificate validation and optionally, certificate pinning.

Report issue for preceding element

- •


Agent Card Registry and Validation: Use a trusted registry or directory for validation.

Report issue for preceding element

- •


Reputation-Based Trust: Implement a reputation system for rating Agent Cards.

Report issue for preceding element

- •


Agent Card Sanitization: Sanitize AgentCard content before using it with Foundational Models.

Report issue for preceding element


#### VI-A2 Preventing A2A Task Replay

Report issue for preceding element

Addressing Section- [IV-B2](https://arxiv.org/html/2504.16902v1#S4.SS2.SSS2 "IV-B2 A2A Task Replay ‣ IV-B Common A2A Multi-Agent System Threats ‣ IV Threat Modeling Google A2A based Agentic AI Apps with MAESTRO ‣ Building A Secure Agentic AI Application Leveraging Google’s A2A Protocol")

Report issue for preceding element

Mitigation Strategies:

Report issue for preceding element

- •


Include a unique nonce in each tasks/send request.

Report issue for preceding element

- •


Use timestamp verification with an acceptable time window.

Report issue for preceding element

- •


Use Message Authentication Codes (MACs).

Report issue for preceding element

- •


Design tasks to be idempotent.

Report issue for preceding element

- •


Implement session management to track tasks.

Report issue for preceding element


#### VI-A3 Preventing A2A Message Schema Violations

Report issue for preceding element

Addressing Section- [IV-B3](https://arxiv.org/html/2504.16902v1#S4.SS2.SSS3 "IV-B3 A2A Message Schema Violation ‣ IV-B Common A2A Multi-Agent System Threats ‣ IV Threat Modeling Google A2A based Agentic AI Apps with MAESTRO ‣ Building A Secure Agentic AI Application Leveraging Google’s A2A Protocol")

Report issue for preceding element

Mitigation Strategies:

Report issue for preceding element

- •


Enforce strict schema validation.

Report issue for preceding element

- •


Sanitize all input from clients.

Report issue for preceding element

- •


Use Content Security Policies (CSP).

Report issue for preceding element

- •


Execute tasks with least privilege.

Report issue for preceding element


#### VI-A4 Preventing A2A Server Impersonation

Report issue for preceding element

Addressing Section- [IV-B4](https://arxiv.org/html/2504.16902v1#S4.SS2.SSS4 "IV-B4 A2A Server Impersonation ‣ IV-B Common A2A Multi-Agent System Threats ‣ IV Threat Modeling Google A2A based Agentic AI Apps with MAESTRO ‣ Building A Secure Agentic AI Application Leveraging Google’s A2A Protocol")

Report issue for preceding element

Mitigation Strategies:

Report issue for preceding element

- •


Use Mutual TLS (mTLS).

Report issue for preceding element

- •


Use DNSSEC to protect against spoofing.

Report issue for preceding element

- •


Implement certificate pinning.

Report issue for preceding element

- •


Apply monitoring and intrusion detection.

Report issue for preceding element


#### VI-A5 Preventing Cross-Agent Task Escalation

Report issue for preceding element

Addressing Section- [IV-B5](https://arxiv.org/html/2504.16902v1#S4.SS2.SSS5 "IV-B5 Cross-Agent Task Escalation ‣ IV-B Common A2A Multi-Agent System Threats ‣ IV Threat Modeling Google A2A based Agentic AI Apps with MAESTRO ‣ Building A Secure Agentic AI Application Leveraging Google’s A2A Protocol")

Report issue for preceding element

Mitigation Strategies:

Report issue for preceding element

- •


Enforce strict authentication and authorization.

Report issue for preceding element

- •


Validate credentials for every task.

Report issue for preceding element

- •


Implement audit logging.

Report issue for preceding element

- •


Follow least privilege principles.

Report issue for preceding element

- •


Use secure discovery for Agent Cards.

Report issue for preceding element


#### VI-A6 Mitigating Artifact Tampering via A2A Artifacts

Report issue for preceding element

Addressing Section- [IV-B6](https://arxiv.org/html/2504.16902v1#S4.SS2.SSS6 "IV-B6 Artifact Tampering via A2A Artifacts ‣ IV-B Common A2A Multi-Agent System Threats ‣ IV Threat Modeling Google A2A based Agentic AI Apps with MAESTRO ‣ Building A Secure Agentic AI Application Leveraging Google’s A2A Protocol")

Report issue for preceding element

Mitigation Strategies:

Report issue for preceding element

- •


Use digital signatures on artifacts.

Report issue for preceding element

- •


Apply hashing and checksums.

Report issue for preceding element

- •


Use encryption.

Report issue for preceding element

- •


Ensure secure storage and transmission.

Report issue for preceding element


#### VI-A7 Preventing Insider Threat/Logging Evasion via A2A Task Manipulation

Report issue for preceding element

Addressing Section- [IV-B7](https://arxiv.org/html/2504.16902v1#S4.SS2.SSS7 "IV-B7 Insider Threat/Logging Evasion via A2A Task Manipulation ‣ IV-B Common A2A Multi-Agent System Threats ‣ IV Threat Modeling Google A2A based Agentic AI Apps with MAESTRO ‣ Building A Secure Agentic AI Application Leveraging Google’s A2A Protocol")

Report issue for preceding element

Mitigation Strategies:

Report issue for preceding element

- •


Implement RBAC.

Report issue for preceding element

- •


Apply audit logging with integrity checks.

Report issue for preceding element

- •


Ensure separation of duties.

Report issue for preceding element

- •


Conduct security audits.

Report issue for preceding element

- •


Require MFA for privileged roles.

Report issue for preceding element


#### VI-A8 Addressing Supply Chain Attacks via A2A Dependencies

Report issue for preceding element

Addressing Section- [IV-B8](https://arxiv.org/html/2504.16902v1#S4.SS2.SSS8 "IV-B8 Supply Chain Attack via A2A Dependencies ‣ IV-B Common A2A Multi-Agent System Threats ‣ IV Threat Modeling Google A2A based Agentic AI Apps with MAESTRO ‣ Building A Secure Agentic AI Application Leveraging Google’s A2A Protocol")

Report issue for preceding element

Mitigation Strategies:

Report issue for preceding element

- •


Use dependency scanning.

Report issue for preceding element

- •


Apply dependency pinning.

Report issue for preceding element

- •


Generate and maintain a Software Bill of Materials (SBOM).

Report issue for preceding element

- •


Conduct vendor security assessments.

Report issue for preceding element

- •


Follow secure development practices.

Report issue for preceding element


#### VI-A9 Mitigating Authentication & Identity Threats

Report issue for preceding element

Addressing Section- [IV-B9](https://arxiv.org/html/2504.16902v1#S4.SS2.SSS9 "IV-B9 Authentication & Identity Threats ‣ IV-B Common A2A Multi-Agent System Threats ‣ IV Threat Modeling Google A2A based Agentic AI Apps with MAESTRO ‣ Building A Secure Agentic AI Application Leveraging Google’s A2A Protocol")

Report issue for preceding element

Mitigation Strategies:

Report issue for preceding element

- •


Apply strong JWT validation.

Report issue for preceding element

- •


Use secure token storage.

Report issue for preceding element

- •


Implement token rotation.

Report issue for preceding element

- •


Use mTLS for API access.

Report issue for preceding element

- •


Follow OAuth 2.0 best practices, including PKCE.

Report issue for preceding element


#### VI-A10 Mitigating Poisoned AgentCard

Report issue for preceding element

Addressing Section [IV-B10](https://arxiv.org/html/2504.16902v1#S4.SS2.SSS10 "IV-B10 Poisoned AgentCard ‣ IV-B Common A2A Multi-Agent System Threats ‣ IV Threat Modeling Google A2A based Agentic AI Apps with MAESTRO ‣ Building A Secure Agentic AI Application Leveraging Google’s A2A Protocol")

Report issue for preceding element

Mitigation Strategies:

Report issue for preceding element

- •


Apply input sanitization to all AgentCard content.

Report issue for preceding element

- •


Use a whitelist of allowed characters.

Report issue for preceding element

- •


Implement escaping/encoding of special characters.

Report issue for preceding element

- •


Enforce Content Security Policy (CSP).

Report issue for preceding element

- •


Validate structure with schema checks and type constraints.

Report issue for preceding element


### VI-BAdditional Security Considerations

Report issue for preceding element

Addressing Section- [IV-C](https://arxiv.org/html/2504.16902v1#S4.SS3 "IV-C Additional Security Considerations ‣ IV Threat Modeling Google A2A based Agentic AI Apps with MAESTRO ‣ Building A Secure Agentic AI Application Leveraging Google’s A2A Protocol")

Report issue for preceding element

- •


Continuously scan and verify supply chain dependencies.

Report issue for preceding element

- •


Develop and maintain incident response and recovery plans.

Report issue for preceding element

- •


Evaluate security posture of open-source libraries.

Report issue for preceding element

- •


Use declarative security configurations (YAML/JSON).

Report issue for preceding element

- •


Integrate security testing into CI/CD pipelines.

Report issue for preceding element

- •


Document capabilities and trust boundaries in Agent Cards.

Report issue for preceding element


### VI-CApplying Mitigations to Case Studies (Sections [V-A](https://arxiv.org/html/2504.16902v1\#S5.SS1 "V-A Case Study 1: Collaborative Document Processing ‣ V Case Study ‣ Building A Secure Agentic AI Application Leveraging Google’s A2A Protocol") and [V-B](https://arxiv.org/html/2504.16902v1\#S5.SS2 "V-B Case Study 2: Distributed Data Analysis ‣ V Case Study ‣ Building A Secure Agentic AI Application Leveraging Google’s A2A Protocol"))

Report issue for preceding element

#### VI-C1 Case Study 1: Collaborative Document Processing

Report issue for preceding element

- •


Digitally sign all documents.

Report issue for preceding element

- •


Enforce granular access control.

Report issue for preceding element

- •


Apply DLP techniques.

Report issue for preceding element

- •


Sanitize Agent Cards before using with FMs.

Report issue for preceding element

- •


Validate and authenticate all task submissions.

Report issue for preceding element


#### VI-C2 Case Study 2: Distributed Data Analysis

Report issue for preceding element

- •


Implement differential privacy.

Report issue for preceding element

- •


Use federated learning.

Report issue for preceding element

- •


Apply secure multi-party computation (SMPC).

Report issue for preceding element

- •


Sanitize Agent Cards before use.

Report issue for preceding element

- •


Apply strict audit controls on artifact aggregation.

Report issue for preceding element


## VII Secure Application Development Strategies

Report issue for preceding element

### VII-ASecurely Implementing with Current A2A Features

Report issue for preceding element

This involves endpoint hardening, augmenting authentication mechanisms beyond the basic requirements if necessary, and rigorous input/output validation.

Report issue for preceding element

### VII-BLeveraging Enhanced A2A Features for Advanced Security

Report issue for preceding element

Future enhancements or complementary technologies could include DID-based authentication, granular policy enforcement frameworks, and mechanisms for establishing data provenance.

Report issue for preceding element

## VIII Key Control Measures for Safe A2A Deployment

Report issue for preceding element

This section covers essential controls for deploying A2A-based applications securely:

Report issue for preceding element

- •


Endpoint security (TLS, network controls).

Report issue for preceding element

- •


Strong authentication and authorization.

Report issue for preceding element

- •


Comprehensive input validation and sanitization.

Report issue for preceding element

- •


Principle of least privilege for agent capabilities and data access.

Report issue for preceding element

- •


Robust monitoring, logging, and alerting.

Report issue for preceding element

- •


Secure software development lifecycle (SSDLC) practices.

Report issue for preceding element

- •


Incident response planning and execution.

Report issue for preceding element


For secure A2A coding examples, please refer to the Github repository 222 [https://github.com/kenhuangus/a2a-secure-coding-examples](https://github.com/kenhuangus/a2a-secure-coding-examples "").

Report issue for preceding element

## IX Implementing A2A Server Securely

Report issue for preceding element![Refer to caption](https://arxiv.org/html/extracted/6381309/a2aserver.png)Figure 3: Best Practices For Secured A2A ServerReport issue for preceding element

In this section, we will focus on suggesting specific security controls to implement for the A2A Server deployment, aiming to enhance its resilience against potential threats. A high-level overview of these threats is illustrated in Figure [3](https://arxiv.org/html/2504.16902v1#S9.F3 "Figure 3 ‣ IX Implementing A2A Server Securely ‣ Building A Secure Agentic AI Application Leveraging Google’s A2A Protocol").

Report issue for preceding element

### IX-ASecuring the AgentCard

Report issue for preceding element

The AgentCard (/.well-known/agent.json) is a critical security element as it exposes information about your agent’s capabilities and authentication requirements.

Report issue for preceding element

### IX-BSecuring the AgentCard

Report issue for preceding element

The AgentCard is a critical security element in the A2A protocol as it exposes information about an agent’s capabilities and authentication requirements.

Report issue for preceding element

1. 1.


AgentCard Location and Access Controls

Report issue for preceding element

- •


Host the AgentCard file (/.well-known/agent.json) with appropriate access controls.

Report issue for preceding element

- •


Implement rate limiting to prevent enumeration attacks.

Report issue for preceding element

- •


Consider using content security headers to prevent unauthorized embedding or framing.

Report issue for preceding element


2. 2.


AgentCard Content Security

Report issue for preceding element

- •


Include only necessary information about your agent’s capabilities.

Report issue for preceding element

- •


Specify detailed authentication requirements using OpenAPI 3.x Security Scheme objects.

Report issue for preceding element

- •


Validate the AgentCard content regularly to ensure it doesn’t expose sensitive information.

Report issue for preceding element

- •


Keep authentication details accurate and up to date.

Report issue for preceding element


### IX-CAuthentication and Authorization

Report issue for preceding element

- •


Establish Server Identity: Authenticate the server’s identity via digital certificates provided by trustworthy Certificate Authorities. Employ TLS to secure connections, enabling clients to authenticate the server’s authenticity during the handshake and mitigate man-in-the-middle attacks.

Report issue for preceding element

- •


Declare Authentication Protocols: Explicitly declare the supported authentication methods (e.g., OAuth, OIDC, API Keys) in the Agent Card.

Report issue for preceding element

- •


Authenticate Each Request: Require authentication for each incoming HTTP request. Ensure that every request has proper credentials (e.g., tokens, certificates). Reject requests that lack the valid credentials by utilizing suitable HTTP status codes (e.g., 401 Unauthorized, 403 Forbidden).

Report issue for preceding element


1. 1.


Protecting Sensitive Actions and Data

It is recommended that A2A server will protect sensitive information by managing authorization to both ‘skills’ and ‘tools’:

Report issue for preceding element

- •


Skills: Agents are required to advertise their skills through an Agent Card, showcasing their expertise. It is recommended for agents to grant permission for each skill or grant permission on a per-skill basis using specific scopes, enabling different access levels (e.g., read-only skills).

Report issue for preceding element

- •


Tools: Agents are required to limit access to sensitive data and actions by securing using controlled tools. Therefore, when agentic flow requests data, the agent will grant permissions based on this.

Report issue for preceding element


2. 2.


API Keys

For simpler implementations, API keys may be used:

Report issue for preceding element

- •


Generate strong, random API keys following cryptographic best practices.

Report issue for preceding element

- •


Implement key rotation policies to regularly update API keys.

Report issue for preceding element

- •


Store API keys securely and never expose them in client-side code.

Report issue for preceding element


3. 3.


JWT Authentication

For stateless authentication:

Report issue for preceding element

- •


Implement robust JWT validation including signature verification.

Report issue for preceding element

- •


Set appropriate token expiration times to limit the impact of token theft.

Report issue for preceding element

- •


Include only necessary claims in the JWT payload.

Report issue for preceding element


### IX-DSecure Communication

Report issue for preceding element

1. 1.


Transport Layer Security (TLS)

Report issue for preceding element

- •


Enforce HTTPS for all A2A communications with proper TLS configuration (TLS1.3).

Report issue for preceding element

- •


Regularly renew TLS certificates and disable insecure ciphers.

Report issue for preceding element


2. 2.


Data Protection in Transit

Report issue for preceding element

- •


Ensure all A2A messages are encrypted during transmission.

Report issue for preceding element

- •


Validate certificate chains to prevent man-in-the-middle attacks.

Report issue for preceding element

- •


Consider implementing certificate pinning for critical connections.

Report issue for preceding element


3. 3.


Data Protection at Rest

Report issue for preceding element

- •


Encrypt sensitive data stored by your A2A server.

Report issue for preceding element

- •


Secure storage of any persistent data from agent interactions.

Report issue for preceding element

- •


Implement proper key management for encryption keys.

Report issue for preceding element


### IX-EInput Validation and Request Processing

Report issue for preceding element

1. 1.


Message Validation

Report issue for preceding element

- •


Validate all incoming messages against the A2A protocol schema.

Report issue for preceding element

- •


Implement robust input sanitization to prevent injection attacks.

Report issue for preceding element

- •


Verify message formats, sizes, and content types before processing.

Report issue for preceding element


2. 2.


URI Validation

Report issue for preceding element

- •


Strictly validate any URIs included in messages to prevent Server-Side Request Forgery (SSRF) attacks.

Report issue for preceding element

- •


Implement allow-lists for acceptable URI schemes and domains.

Report issue for preceding element

- •


Avoid fetching content from untrusted or user-supplied URIs.

Report issue for preceding element


3. 3.


Processing File Parts

When handling FilePart content in A2A messages:

Report issue for preceding element

- •


Scan all uploaded files for malware.

Report issue for preceding element

- •


Validate file types and enforce size limits.

Report issue for preceding element

- •


Store uploaded files securely with appropriate access controls.

Report issue for preceding element


### IX-FServer Implementation Best Practices

Report issue for preceding element

1. 1.


Error Handling and Logging

Report issue for preceding element

- •


Implement comprehensive error handling that doesn’t expose sensitive information.

Report issue for preceding element

- •


Maintain detailed security logs for authentication attempts, authorization decisions, and security events.

Report issue for preceding element

- •


Ensure logs are protected and cannot be tampered with.

Report issue for preceding element

- •


Implement monitoring and alerting for suspicious activities.

Report issue for preceding element


2. 2.


Rate Limiting and DoS Protection

Report issue for preceding element

- •


Implement rate limiting on all A2A endpoints to prevent abuse.

Report issue for preceding element

- •


Consider using exponential backoff for failed authentication attempts.

Report issue for preceding element

- •


Monitor for and mitigate denial of service attacks targeting your A2A server.

Report issue for preceding element


3. 3.


Secure Development Practices

Report issue for preceding element

- •


Follow secure coding guidelines specific to your implementation language.

Report issue for preceding element

- •


Conduct regular security code reviews.

Report issue for preceding element

- •


Implement application security testing as part of your development workflow.

Report issue for preceding element

- •


Keep all dependencies updated to address security vulnerabilities.

Report issue for preceding element


TABLE I: Comparative Analysis of A2A and MCP

|     |     |     |
| --- | --- | --- |
| Feature | Google Agent2Agent (A2A) | Anthropic Model Context Protocol (MCP) |
| Purpose | Enable interoperability between diverse AI agents | Standardize connection between AI models/agentsand external tools/data |
| Focus | Agent-to-Agent collaboration, delegation,messaging | Agent-to-Tool/Resource access, contextprovisioning |
| Primary Interaction | Client Agent ↔↔\\leftrightarrow↔ Remote Agent | MCP Client (Agent/Host) ↔↔\\leftrightarrow↔ MCP Server(Tool/Data) |
| Key Mechanisms | Agent Cards (discovery), Task object (lifecycle),Messages, Artifacts | Tools, Resources, Prompts (exposed by server),Client-Server requests |
| Ecosystem Role | Horizontal Integration(Agent Network Communication) | Vertical Integration(Agent Capability Enhancement) |

Report issue for preceding element

### IX-GProtocol-Specific Security Considerations

Report issue for preceding element

1. 1.


Streaming and SSE (Server-Sent Events)

For implementations using tasks/sendSubscribe and Server-Sent Events (SSE):

Report issue for preceding element

- •


Implement proper authentication for SSE connections.

Report issue for preceding element

- •


Maintain secure state management for long-lived connections.

Report issue for preceding element

- •


Monitor for and mitigate resource exhaustion attacks.

Report issue for preceding element


2. 2.


Push Notifications

When implementing the optional push notifications capability:

Report issue for preceding element

- •


Validate webhook URLs rigorously to prevent SSRF attacks.

Report issue for preceding element

- •


Implement signature verification for webhook payloads.

Report issue for preceding element

- •


Use HTTPS for all webhook communications.

Report issue for preceding element

- •


Implement retry policies with appropriate backoff.

Report issue for preceding element


3. 3.


Connection Management and Abuse Prevention

Effective connection management is essential to ensure the scalability and resilience of A2A Server streaming features such as tasks/sendSubscribe and Server-Sent Events (SSE). To prevent abuse and resource exhaustion, the server should enforce various strategies depicted below.

Report issue for preceding element

4. 4.


Connection Quotas: connection quotas per client or IP, close idle connections through timeout mechanisms, and use periodic keep-alive pings to detect and clean up stale sessions.

Report issue for preceding element

5. 5.


Connection limits: Set hard limits on the number of active SSE connections per client ID/IP to prevent resource exhaustion.

Report issue for preceding element

6. 6.


Idle Timeout & Keep-Alive Pings: Enforce connection idle timeouts. Use periodic keep-alive pings and terminate stale sessions.

Report issue for preceding element

7. 7.


Backpressure-Aware Streaming: Drop non-critical event messages for lagging clients or apply backoff strategies to prevent memory build-up.

Report issue for preceding element


### IX-HServer Hardening

Report issue for preceding element

When deploying A2A server, it is essential to use a hardened environment following security best practices.

Report issue for preceding element

- •


Implement network segmentation to isolate the A2A server.

Report issue for preceding element

- •


Use Web Application Firewalls (WAF) to protect against common web attacks.

Report issue for preceding element

- •


Regularly apply security updates to server components.

Report issue for preceding element

- •


Implement comprehensive monitoring of your A2A server.

Report issue for preceding element

- •


Develop incident response procedures for security breaches.

Report issue for preceding element

- •


Conduct regular security assessments and penetration tests.

Report issue for preceding element

- •


Establish a security incident management process.

Report issue for preceding element


![Refer to caption](https://arxiv.org/html/extracted/6381309/sequence-diag.png)Figure 4: End to End Agents collaboration utilizing A2A and MCPReport issue for preceding element

## X MCP and A2A: A Synergy

Report issue for preceding element

The Agent-to-Agent (A2A) protocol and Model Context Protocol (MCP) represent complementary frameworks that together create a robust foundation for sophisticated agentic systems. Rather than competing standards, these protocols operate at different layers of the AI interaction stack, enabling both horizontal coordination between peer agents and vertical integration with specialized tools and data sources. Table [I](https://arxiv.org/html/2504.16902v1#S9.T1 "TABLE I ‣ IX-F Server Implementation Best Practices ‣ IX Implementing A2A Server Securely ‣ Building A Secure Agentic AI Application Leveraging Google’s A2A Protocol") presents a comparative analysis of these two critical protocols in Agentic AI.

Report issue for preceding element

When deployed together, these protocols create an efficient hierarchical workflow system. An agent initially receives a complex task from either a human user or another agent through A2A protocols. To successfully complete this assignment, the agent often needs specialized capabilities beyond its own scope. Using A2A’s discovery mechanism, it identifies and delegates specific subtasks to purpose-built agents with relevant expertise, such as Claim Agents or Rental Car Agents. These specialized agents then leverage MCP to connect with structured data sources, computational tools, or external systems required to fulfill their assigned responsibilities. The completed work flows back through the agent hierarchy via A2A’s structured task management framework, enabling seamless integration of results from multiple specialized systems into a cohesive solution delivered to the original requestor. Figure [4](https://arxiv.org/html/2504.16902v1#S9.F4 "Figure 4 ‣ IX-H Server Hardening ‣ IX Implementing A2A Server Securely ‣ Building A Secure Agentic AI Application Leveraging Google’s A2A Protocol") illustrates the steps in such a use case.

Report issue for preceding element

The flow between a Claim Agent and Rental Car Agent would utilize the A2A protocol for agent-to-agent coordination and task management, where the Claim Agent (acting as the Main A2A Client) would discover the Rental Car Agent’s capabilities through the well-known agent registry, authenticate, and delegate specific rental-related tasks with unique taskIds. Meanwhile, the MCP framework enables each specialized agent to extend its capabilities by connecting to external tools and databases - the Claim Agent might access policy databases while the Rental Car Agent connects to vehicle availability systems. These frameworks complement each other by allowing the Claim Agent to maintain high-level coordination of the insurance claim process (tracking status updates and compiling final results for the user) while the Rental Car Agent uses MCP to perform specialized functions like querying vehicle inventories and processing rental agreements, ultimately delivering an integrated solution where claim processing and rental car arrangements happen seamlessly within a unified workflow.

Report issue for preceding element

This architectural approach promotes several key design principles. It enables functional modularity, allowing organizations to develop specialized agents with deep domain expertise. It supports compositional flexibility, as different agent combinations can be assembled to address diverse problems. It maintains clear separation of concerns between peer-level agent coordination and tool-level resource access. Most importantly, it creates an extensible ecosystem where new capabilities can be added incrementally without redesigning the entire system.

Report issue for preceding element

The multi-protocol architecture introduces important security considerations at integration boundaries. Potential attack vectors may cross protocol boundaries—for example, an authentication vulnerability in the A2A layer could be exploited to gain unauthorized MCP access, while sensitive information exposed through inadequately protected MCP connections might enable subsequent A2A-based compromises. Therefore, robust security strategies must address not only each protocol individually but also the critical interfaces where they interconnect. This comprehensive approach ensures continuous protection throughout the entire agent workflow chain, with special attention to authentication token handling, task delegation permissions, and secure data transmission between the Claim Agent, Rental Car Agent, and their respective external systems. \[ [19](https://arxiv.org/html/2504.16902v1#bib.bib19 "")\]

Report issue for preceding element

## XI Conclusion

Report issue for preceding element

### XI-ARecap of A2A’s Role, Security Challenges, and Enhancement Potential

Report issue for preceding element

The Agent-to-Agent (A2A) protocol plays a foundational role in enabling secure, composable, and scalable multi-agent systems. By standardizing how agents discover, authenticate, and communicate with one another, A2A facilitates a new paradigm of autonomous collaboration—ranging from document co-authoring agents to federated analytics across distributed datasets. Its declarative nature and emphasis on explicit capabilities (via AgentCards) empower developers to build trust-aware, modular workflows that reflect real-world boundaries and roles.
However, with these capabilities come significant security challenges. The distributed and dynamic nature of multi-agent systems introduces threats. Furthermore, novel risks such as prompt injection into AgentCards and cross-agent escalation highlight the need for context-aware threat modeling—such as that provided by the MAESTRO framework.
To realize the full potential of A2A-based systems, security must be deeply integrated into both protocol design and server implementation. From strong cryptographic controls and zero-trust agent authentication to schema validation, logging integrity, and resilient streaming protocols, robust security controls are essential. As multi-agent ecosystems grow in complexity, future enhancements to A2A should emphasize adaptive trust, continuous policy enforcement, and secure-by-default configurations. By proactively addressing today’s threats and anticipating tomorrow’s, A2A can serve as a resilient backbone for intelligent, secure, and trustworthy agentic AI applications.

Report issue for preceding element

### XI-BFuture Directions for Secure Agent Collaboration

Report issue for preceding element

Looking ahead, the secure collaboration of autonomous agents hinges on continued progress in protocol standardization and the widespread adoption of security best practices. Initiatives like A2A and MCP are crucial, but their evolution must prioritize security considerations, potentially incorporating lessons from Zero Trust architectures adapted for agent-specific contexts. Future work should focus on developing standardized methods for expressing and enforcing complex authorization policies between agents, establishing robust mechanisms for agent identity verification and reputation management, and creating frameworks for secure multi-agent coordination, especially when crossing administrative or trust boundaries. Furthermore, addressing the security implications of integrating Large Language Models within agentic workflows and ensuring the resilience of agent communication against sophisticated attacks will be paramount for building trustworthy and reliable multi-agent systems. The development of comprehensive threat models, like MAESTRO \[ [1](https://arxiv.org/html/2504.16902v1#bib.bib1 "")\], and shared security implementation guidelines will be vital for guiding developers in building the next generation of secure agentic AI applications.

Report issue for preceding element

## References

Report issue for preceding element

- \[1\]↑
K. Huang, “Agentic AI threat modeling framework: MAESTRO,” [https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro ""), Cloud Security Alliance, feb 2025.

- \[2\]↑
K. Huang and I. Habler, “Threat modeling Google’s A2A protocol,” [https://kenhuangus.substack.com/p/threat-modeling-googles-a2a-protocol](https://kenhuangus.substack.com/p/threat-modeling-googles-a2a-protocol ""), 2025.

- \[3\]↑
T. Finin, R. Fritzson, D. McKay, and R. McEntire, “KQML as an agent communication language,” in _Proceedings of the Third International Conference on Information and Knowledge Management_.   ACM, 1994, pp. 456–463. \[Online\]. Available: [https://dl.acm.org/doi/10.1145/191246.191322](https://dl.acm.org/doi/10.1145/191246.191322 "")
- \[4\]↑
Y. Labrou and T. Finin, “History, state of the art and challenges for agent communication languages,” _Informatik/Informatique_, 2000\. \[Online\]. Available: [https://ebiquity.umbc.edu/paper/html/id/231/History-State-of-the-Art-and-Challenges-for-Agent-Communication-Languages](https://ebiquity.umbc.edu/paper/html/id/231/History-State-of-the-Art-and-Challenges-for-Agent-Communication-Languages "")
- \[5\]↑
FIPA.org, “FIPA agent communication language specifications,” [http://www.fipa.org/repository/aclspecs.html](http://www.fipa.org/repository/aclspecs.html ""), n.d.

- \[6\]↑
B. Chaib-draa and F. Dignum, “Trends in agent communication language,” _Computational Intelligence_, vol. 18, no. 2, pp. 89–101, 2002. \[Online\]. Available: [https://onlinelibrary.wiley.com/doi/abs/10.1111/1467-8640.00184](https://onlinelibrary.wiley.com/doi/abs/10.1111/1467-8640.00184 "")
- \[7\]↑
B. Gaudou, A. Herzig, D. Longin, and M. Nickles, “A new semantics for the FIPA agent communication language based on social attitudes,” in _ECAI 2006: 17th European Conference on Artificial Intelligence_.   IOS Press, 2006, pp. 245–249. \[Online\]. Available: [https://www.irit.fr/publis/LILAC/Conf\_internationales/2006\_Gaudou\_et\_al\_ECAI.pdf](https://www.irit.fr/publis/LILAC/Conf_internationales/2006_Gaudou_et_al_ECAI.pdf "")
- \[8\]↑
Google Developer Blog, “Announcing the agent2agent protocol (A2A),” [https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/ ""), 2025.

- \[9\]↑
A. Dorri, S. S. Kanhere, and R. Jurdak, “Multi-agent systems: A survey,” _IEEE Access_, vol. 6, pp. 28 573–28 593, 2018. \[Online\]. Available: [https://ieeexplore.ieee.org/document/8352646/](https://ieeexplore.ieee.org/document/8352646/ "")
- \[10\]↑
C. Zhu, M. Dastani, and S. Wang, “A survey of multi-agent deep reinforcement learning with communication,” _Autonomous Agents and Multi-Agent Systems_, vol. 38, no. 1, 2024. \[Online\]. Available: [https://link.springer.com/article/10.1007/s10458-023-09633-6](https://link.springer.com/article/10.1007/s10458-023-09633-6 "")
- \[11\]↑
Google Developer Blog, “\[specific blog post title - placeholder\],” \[Specific URL - Placeholder\], 2024.

- \[12\]↑
M. Bellare and P. Rogaway, “Optimal asymmetric encryption,” _Journal of Cryptology_, vol. 9, no. 2, pp. 137–159, 1995.

- \[13\]↑
JADE Documentation, “Security extensions,” TILab, Telecom Italia.

- \[14\]↑
OASIS, “Web services security: SOAP message security 1.0 (WS-Security 2004),” 2004.

- \[15\]↑
D. Hardt, “The OAuth 2.0 authorization framework,” IETF, RFC 6749, October 2012. \[Online\]. Available: [https://tools.ietf.org/html/rfc6749](https://tools.ietf.org/html/rfc6749 "")
- \[16\]↑
M. B. Jones, J. Bradley, and N. Sakimura, “JSON web token (JWT),” IETF, RFC 7519, May 2015. \[Online\]. Available: [https://tools.ietf.org/html/rfc7519](https://tools.ietf.org/html/rfc7519 "")
- \[17\]↑
S. Rose, O. Borchert, S. Mitchell, and S. Connelly, “Zero trust architecture,” National Institute of Standards and Technology, NIST Special Publication 800-207, August 2020. \[Online\]. Available: [https://doi.org/10.6028/NIST.SP.800-207](https://doi.org/10.6028/NIST.SP.800-207 "")
- \[18\]↑
N. Ward and Y. He, “Adopting BeyondCorp for multi-agent AI in enterprise networks,” 2019.

- \[19\]↑
V. S. Narajala and I. Habler, “Enterprise-Grade Security for the Model Context Protocol (MCP): Frameworks and Mitigation Strategies,” _arXiv preprint arXiv:2504.08623_, 2025\. \[Online\]. Available: [https://arxiv.org/abs/2504.08623](https://arxiv.org/abs/2504.08623 "")

Report IssueReport Issue for Selection

Generated by
[L\\
A\\
T\\
Exml![[LOGO]](<Base64-Image-Removed>)](https://math.nist.gov/~BMiller/LaTeXML/)
