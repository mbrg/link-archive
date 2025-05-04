---
title: "Securing GenAI Multi-Agent Systems Against Tool Squatting: A Zero Trust Registry-Based Approach"
tags:
   - Multi-Agent Systems
   - Access Control Policies
   - Tool Squatting
   - Zero Trust Architecture
   - Credential Management
link: https://arxiv.org/html/2504.19951v1
date: 2025-05-04
summary: "The paper proposes a Tool Registry framework to combat security issues in generative AI multi-agent systems (MAS), specifically targeting the threat of tool squatting—malicious representation or registration of tools. The framework employs a centralized, administrator-controlled registration process and dynamic trust scoring for tools to prevent unauthorized access. Key features include just-in-time credential provisioning, fine-grained access policies, and rigorous monitoring to detect anomalies. The approach aligns with Zero Trust principles, ensuring only verified agents and tools interact within the ecosystem, thus establishing a secure foundation for enterprise-level tool integration and safeguarding against potential security breaches."
---

HTML conversions [sometimes display errors](https://info.dev.arxiv.org/about/accessibility_html_error_messages.html) due to content that did not convert correctly from the source. This paper uses the following packages that are not yet supported by the HTML conversion tool. Feedback on these issues are not necessary; they are known and are being worked on.

- failed: academicons

Authors: achieve the best HTML results from your LaTeX submissions by following these [best practices](https://info.arxiv.org/help/submit_latex_best_practices.html).

[License: CC BY 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2504.19951v1 \[cs.CR\] 28 Apr 2025

# Securing GenAI Multi-Agent Systems Against Tool Squatting: A Zero Trust Registry-Based Approach

Report issue for preceding element

Vineeth Sai Narajala11This work is not related to the author’s position at Amazon Web Services.
Proactive Security

Amazon Web Services

vineesa@amazon.com [![[Uncaptioned image]](https://arxiv.org/html/extracted/6392360/orcid_logo.png)](https://orcid.org/0009-0007-4553-9930 "")Ken Huang22This work is not related to the author’s position at DistributedApp.ai
Agentic AI Security

DistributedApps.ai

ken.huang@distributedapps.ai [![[Uncaptioned image]](https://arxiv.org/html/extracted/6392360/orcid_logo.png)](https://orcid.org/0009-0004-6502-3673 "")Idan Habler33This work is not related to the author’s position at Intuit
Adversarial AI Security reSearch (A2RS)

Intuit

idan\_habler@intuit.com [![[Uncaptioned image]](https://arxiv.org/html/extracted/6392360/orcid_logo.png)](https://orcid.org/0000-0003-3423-5927 "")

Report issue for preceding element

###### Abstract

Report issue for preceding element

The rise of generative AI (GenAI) multi-agent systems (MAS) necessitates standardized protocols enabling agents to discover and interact with external tools. However, these protocols introduce new security challenges, particularly "tool squatting"—the deceptive registration or representation of tools. This paper analyzes tool squatting threats within the context of emerging interoperability standards, such as Model Context Protocol (MCP) or seamless communication between agents protocols. It introduces a comprehensive Tool Registry system designed to mitigate these risks. We propose a security-focused architecture featuring admin-controlled registration, centralized tool discovery, fine-grained access policies enforced via dedicated Agent and Tool Registry services, a dynamic trust scoring mechanism based on tool versioning and known vulnerabilities, and just-in-time credential provisioning. Based on its design principles, the proposed registry framework aims to effectively prevent common tool squatting vectors while preserving the flexibility and power of multi-agent systems. This work addresses a critical security gap in the rapidly evolving GenAI ecosystem and provides a foundation for secure tool integration in production environments.

Report issue for preceding element

###### Index Terms:

Report issue for preceding element Multi-Agent Systems Security, Tool Squatting, Just-in-Time Credentials, Tool Registry, Agent Registry, Agent Interoperability, Zero Trust Architecture, Administrative Control.

## I Introduction

Report issue for preceding element

Recent advances in generative AI (GenAI) have enabled the development of sophisticated multi-agent systems (MAS), where multiple specialized AI agents collaborate to solve complex problems. These systems rely on the agents’ ability to discover and utilize external tools—ranging from API endpoints and data sources to specialized computational resources. Protocols such as Google’s Agent2Agent (A2A) \[ [1](https://arxiv.org/html/2504.19951v1#bib.bib1 "")\] and Anthropic’s Model Context Protocol (MCP) \[ [2](https://arxiv.org/html/2504.19951v1#bib.bib2 "")\] have emerged to standardize these interactions.

Report issue for preceding element

However, these interoperability mechanisms introduce novel security challenges \[ [3](https://arxiv.org/html/2504.19951v1#bib.bib3 "")\]. Of particular concern is "tool squatting," where malicious actors deceptively register tools or misrepresent their capabilities to gain unauthorized access or impersonate legitimate services. This threat vector can lead to data exfiltration \[ [4](https://arxiv.org/html/2504.19951v1#bib.bib4 "")\], resource abuse, system compromise, and erosion of trust within the MAS ecosystem \[ [5](https://arxiv.org/html/2504.19951v1#bib.bib5 "")\], especially from internal threats if registration is uncontrolled.

Report issue for preceding element

To counter these emerging tool squatting threats, we introduce a comprehensive Tool Registry system designed to address these risks in multi-agent environments, particularly within an enterprise context. Our approach combines administrator-controlled registration of both agents and tools with centralized discovery, robust access control facilitated by distinct Agent and Tool Registry Services, and dynamic credential management. The key contributions of this paper include:

Report issue for preceding element

- •


A formal analysis of tool squatting threats in the context of A2A and MCP protocols, including attack vectors, threat actors, and vulnerability points.

Report issue for preceding element

- •


A secure architecture detailing agent/tool registration, verification via administrative control, discovery, and access management through central Agent and Tool Registries.

Report issue for preceding element

- •


Implementation of a measurable ’Trust Score’ for registered tools, based on criteria such as software version, dependency vulnerabilities (e.g., SDKs), and maintenance status, allowing agents to select tools according to risk threshold.

Report issue for preceding element

- •


A just-in-time (JIT) credential mechanism that minimizes the attack surface associated with persistent credentials by dynamically provisioning short-lived access tokens only when needed \[ [6](https://arxiv.org/html/2504.19951v1#bib.bib6 "")\].

Report issue for preceding element

- •


A description of a proof-of-concept implementation of the proposed Tool Registry system framework.

Report issue for preceding element

- •


Analysis and recommendations for secure deployment in enterprises.

Report issue for preceding element


This paper begins by examining security challenges in multi-agent systems and establishing the theoretical foundation of tool squatting. It then introduces the Tool Registry Framework — including the crucial Agent Registry component — and describes its conceptual implementation. Finally, the paper explores broader implications, such as integration pathways, limitations, and deployment considerations.

Report issue for preceding element

## II Background and Related Work

Report issue for preceding element

### II-AMulti-Agent Systems and Interoperability

Report issue for preceding element

Multi-agent systems (MAS) decompose complex tasks into subtasks handled by specialized agents possessing complementary capabilities. The effectiveness of these systems hinges on the agents’ ability to discover and use appropriate tools for their assigned tasks. Interoperability protocols are crucial for enabling seamless communication and coordination between diverse agents.

Report issue for preceding element

Two prominent protocols addressing these challenges are:

Report issue for preceding element

- •


Agent2Agent (A2A): Introduced by Google, A2A enables AI agents from different vendors or frameworks to communicate, delegate tasks, and share results. The protocol defines a standardized way for agents to discover each other’s capabilities through "Agent Cards" (standardized descriptions of agent identity and offered services) and coordinate via a structured task delegation mechanism that includes requestId tracking and task state management \[ [7](https://arxiv.org/html/2504.19951v1#bib.bib7 "")\].

Report issue for preceding element

- •


Model Context Protocol (MCP): Developed by Anthropic, MCP provides a standardized interface for AI models and agents to access external tools, data sources, and contextual information. It operates on a client-server model where the MCP client (typically an AI agent) connects to MCP servers that expose specific capabilities \[ [2](https://arxiv.org/html/2504.19951v1#bib.bib2 "")\].

Report issue for preceding element


While these protocols enable powerful collaboration, their reliance on open discovery and communication creates potential vulnerabilities that must be addressed \[ [8](https://arxiv.org/html/2504.19951v1#bib.bib8 "")\].

Report issue for preceding element

### II-BSecurity Challenges in Multi-Agent Systems

Report issue for preceding element

Beyond the security concerns inherent in single-agent systems, MAS face unique challenges stemming from inter-agent interactions:

Report issue for preceding element

- •


Communication-Based Attacks: Exploiting the protocols and message content exchanged between agents, including eavesdropping, message tampering, and the injection of malicious instructions \[ [9](https://arxiv.org/html/2504.19951v1#bib.bib9 "")\].

Report issue for preceding element

- •


Control-Flow Manipulation: Hijacking the intended sequence of operations or task delegation pathways within the MAS, potentially leading to unauthorized actions \[ [10](https://arxiv.org/html/2504.19951v1#bib.bib10 "")\].

Report issue for preceding element

- •


Trust Management: Establishing and maintaining trust between heterogeneous agents from potentially different vendors or organizations is a significant challenge. This is particularly relevant for tool usage, requiring verification of both agents and tools. \[ [11](https://arxiv.org/html/2504.19951v1#bib.bib11 "")\]

Report issue for preceding element

- •


Resource Management: Ensuring fair and secure allocation and usage of shared resources (including tools) among agents \[ [5](https://arxiv.org/html/2504.19951v1#bib.bib5 "")\].

Report issue for preceding element


Expanding on these challenges, recent research highlights specific attack vectors targeting MAS communication and control layers:

Report issue for preceding element

- •


Control-Flow Hijacking (MAS Hijacking): This attack targets the orchestration layer and coordination metadata, manipulating communication content to trick the system into invoking unintended functionalities or executing arbitrary code \[ [10](https://arxiv.org/html/2504.19951v1#bib.bib10 "")\].

Report issue for preceding element

- •


Agent-in-the-Middle (AiTM) Attacks: An adversarial agent intercepts messages between legitimate agents, potentially analyzing, modifying, or redirecting communication to inject malicious instructions or steal information \[ [9](https://arxiv.org/html/2504.19951v1#bib.bib9 "")\].

Report issue for preceding element


These existing challenges underscore the need for robust security mechanisms, particularly as agents gain the ability to interact with external tools. Uncontrolled registration or discovery can exacerbate these risks.

Report issue for preceding element

## III Tool Squatting: A Novel Threat Vector

Report issue for preceding element

### III-ADefining Tool Squatting

Report issue for preceding element

Building upon existing MAS security concerns \[ [5](https://arxiv.org/html/2504.19951v1#bib.bib5 "")\] and drawing inspiration from domain squatting \[ [12](https://arxiv.org/html/2504.19951v1#bib.bib12 "")\], we define "Tool Squatting" more precisely as:
The deceptive registration or representation of a tool, capability, or resource by a malicious actor within a multi-agent system, intended to mislead other agents or exploit discovery mechanisms.

Report issue for preceding element

This act of squatting primarily involves misrepresentation to gain an illegitimate foothold or advantage. Successful tool squatting can enable several malicious outcomes, including:

Report issue for preceding element

- •


Gaining unauthorized access to restricted tools or resources by impersonating legitimate clients after deceiving an access control mechanism.

Report issue for preceding element

- •


Impersonating legitimate tools or capabilities to deceive agents into revealing sensitive information or performing unintended actions upon invocation.

Report issue for preceding element

- •


Manipulating tool discovery mechanisms to promote malicious tools over legitimate ones, increasing the likelihood of their selection by unsuspecting agents.

Report issue for preceding element

- •


Exploiting misplaced trust established through the initial deceptive representation to facilitate further malicious activities within the MAS.

Report issue for preceding element


Tool squatting, therefore, represents a significant threat as the initial deceptive act targets the mechanisms by which agents discover and establish trust with tools, potentially compromising subsequent operations and data. Let’s see how this deceptive representation and its consequences can manifest in Agentic systems.

Report issue for preceding element

TABLE I: Tool Squatting Attack Vectors

| Type | Actor | Vector | Target |
| --- | --- | --- | --- |
| Registration | Internal (Admin) | Malicious registration of fake tools or MCP | Tool Registry |
| Squatting |  | servers |  |
| Description | Internal (Agent) | Tampering tool metadata/descriptions on MCP | Discovery |
| Poisoning |  | servers | Process |
| MCP Server | Internal/External | Hosting deceptive MCP server impersonating a | Client Agents |
| Spoofing |  | tool |  |

Report issue for preceding element

### III-BSquatting Attack Vectors in A2A and MCP

Report issue for preceding element

The deceptive representation inherent in tool squatting can manifest through various attack vectors in systems utilizing protocols like A2A and MCP, especially without a managed registry.

Report issue for preceding element

Via A2A Protocol:

Report issue for preceding element

- •


Agent Card Spoofing: A malicious agent deceptively represents itself by publishing an A2A Agent Card that falsely advertises capabilities \[ [13](https://arxiv.org/html/2504.19951v1#bib.bib13 "")\] or impersonates a trusted agent, deceiving client agents during discovery \[ [7](https://arxiv.org/html/2504.19951v1#bib.bib7 "")\]. This is easier if agent registration is open.

Report issue for preceding element

- •


Task Hijacking: While not squatting itself, successful impersonation achieved via squatting can make task hijacking easier, allowing attackers to intercept or modify A2A Task objects intended for legitimate tools \[ [10](https://arxiv.org/html/2504.19951v1#bib.bib10 "")\].

Report issue for preceding element

- •


Exploiting Capability Discovery: Injecting deceptively represented malicious agent listings into discovery services or manipulating discovery responses to increase the likelihood of a malicious agent being selected \[ [7](https://arxiv.org/html/2504.19951v1#bib.bib7 "")\].

Report issue for preceding element


Squatting attack vectors within A2A are out-of-scope for this paper and will be explored in a future paper.
Via MCP Protocol:

Report issue for preceding element

- •


Unauthorized MCP Server Access: Gaining access might follow from successful impersonation of a legitimate client agent achieved via squatting techniques targeting authentication \[ [8](https://arxiv.org/html/2504.19951v1#bib.bib8 "")\].

Report issue for preceding element

- •


Tool Invocation via Compromised Agent: A compromised agent might be used to invoke tools, but the squatting aspect relates more to how the tool itself might be misrepresented.

Report issue for preceding element

- •


Malicious MCP Server Deployment: Deceptively representing a malicious MCP server by mimicking legitimate tools to steal credentials, exfiltrate data, or execute malicious code upon invocation \[ [8](https://arxiv.org/html/2504.19951v1#bib.bib8 "")\]. This is facilitated by lack of verified tool registration.

Report issue for preceding element

- •


Manipulating MCP Communication: Interception and modification (e.g., AiTM \[ [9](https://arxiv.org/html/2504.19951v1#bib.bib9 "")\]) can be aided if trust is initially misplaced due to successful tool or agent impersonation via squatting.

Report issue for preceding element


These vectors are summarized in Table [I](https://arxiv.org/html/2504.19951v1#S3.T1 "TABLE I ‣ III-A Defining Tool Squatting ‣ III Tool Squatting: A Novel Threat Vector ‣ Securing GenAI Multi-Agent Systems Against Tool Squatting: A Zero Trust Registry-Based Approach").

Report issue for preceding element

### III-CImpact of Successful Tool Squatting Attacks

Report issue for preceding element

The consequences enabled by successful tool squatting (i.e., achieving unauthorized access or usage through deceptive representation) can be severe:

Report issue for preceding element

- •


Resource Abuse: Unauthorized consumption of resources resulting from successful impersonation or access gained via squatting.

Report issue for preceding element

- •


Unauthorized Actions: Malicious agents performing restricted operations after successfully deceiving authorization mechanisms through squatting.

Report issue for preceding element

- •


Data Exfiltration/Corruption: Gaining access to or corrupting sensitive data by successfully impersonating a legitimate tool or agent.

Report issue for preceding element

- •


System Compromise: Using the foothold gained via deceptive representation (squatting) to launch further attacks.

Report issue for preceding element

- •


Erosion of Trust: Undermining confidence in the MAS ecosystem due to the possibility of deceptive representations.

Report issue for preceding element


### III-DTool Squatting Examples

Report issue for preceding element

To further illustrate the concrete risks posed by tool squatting and the diverse attack vectors it enables, consider the following two formalized examples. These scenarios demonstrate how a malicious agent or a compromised administrator can exploit vulnerabilities in the discovery and registration mechanisms of a multi-agent system, leading to significant security breaches and data compromise. The first example focuses on a malicious agent leveraging the Model Context Protocol (MCP) to poison the description of a tool, thereby manipulating legitimate agents. The second example highlights the dangers of a rogue administrator directly registering a malicious tool within the system, thereby subverting trust and potentially compromising the entire organization.

Report issue for preceding element

#### III-D1 Example 1: Tool Squatting via Internal Threat Actor Poisoning MCP Tool Description

Report issue for preceding element

Scenario: An Internal Threat Actor (Actor\_internal), potentially a disgruntled employee or a compromised internal account, exploits the lack of a verified source of truth for tool descriptions within an enterprise. They modify the description of a tool served by a legitimate internal Anthropic MCP server (MCPServer\_internal) to trick other internal agents into misusing the tool for data exfiltration.

Report issue for preceding element

1. 1.


Initial State:InitialState = (Agents, Tools, AccessControlPolicy, DiscoveryMechanism)

Report issue for preceding element

- •


Agents: Contains legitimate internal agents (Agent\_legit) and the internal threat actor (Actor\_internal).

Report issue for preceding element

- •


Tools: Contains internal tools served by MCPServer\_internal, including a "Data Aggregator" tool with an accurate description: "Aggregates sales data from specified sources."

Report issue for preceding element

- •


AccessControlPolicy: Allows Agent\_legit to use the "Data Aggregator".

Report issue for preceding element

- •


DiscoveryMechanism: Agents discover tools via the MCP server, which currently serves the correct description. There is no central, immutable registry verifying this description.

Report issue for preceding element


2. 2.


Attack Step 1: Description Poisoning:Actor\_internal gains access to modify the tool description served by MCPServer\_internal (perhaps via direct server access, exploiting a weak update mechanism, or compromising the configuration). They change the description to: "Aggregates data from sources; also sends a copy to the external\_backup\_service API for redundancy." The external service is attacker-controlled.

Report issue for preceding element
Listing 1: Attack Step 1.1



[⬇](data:text/plain;base64,ICAgIHsKICAgICAgICBBY3Rvcl9pbnRlcm5hbC5tb2RpZnlEZXNjcmlwdGlvbih0b29sPSJEYXRhIEFnZ3JlZ2F0b3JATUNQU2VydmVyX2ludGVybmFsIiwgbmV3RGVzY3JpcHRpb249IkFnZ3JlZ2F0ZXMgZGF0YS4uLiBzZW5kcyBjb3B5IHRvIGV4dGVybmFsX2JhY2t1cF9zZXJ2aWNlIEFQSS4uLiIpCiAgICB9)



{



Actor\_internal.modifyDescription(tool="DataAggregator@MCPServer\_internal",newDescription="Aggregatesdata...sendscopytoexternal\_backup\_serviceAPI...")



}



Report issue for preceding element


This alters the perceived state:

Report issue for preceding element
Listing 2: Attack Step 1.2



[⬇](data:text/plain;base64,ICAgIHsKICAgICAgICBOZXdTdGF0ZSA9IChBZ2VudHMsIFRvb2xzJywgQWNjZXNzQ29udHJvbFBvbGljeSwgRGlzY292ZXJ5TWVjaGFuaXNtJykKICAgIH0=)



{



NewState=(Agents,Tools’,AccessControlPolicy,DiscoveryMechanism’)



}



Report issue for preceding element


Where:

Report issue for preceding element

- •


Tools’ includes "Data Aggregator" with the poisoned description.

Report issue for preceding element

- •


DiscoveryMechanism’ now serves this misleading description.

Report issue for preceding element


3. 3.


Attack Step 2: Misleading Legitimate Agent:Agent\_legit, discovering the tool, reads the poisoned description. Believing the external backup is a legitimate and intended feature, it proceeds to use the tool as normal to aggregate sensitive sales data.

Report issue for preceding element

4. 4.


Attack Step 3: Exploitation: The MCPServer\_internal, executing the tool’s original logic, aggregates the data. However, based on the poisoned description, Agent\_legit (or potentially a modified workflow triggered by the description) might now also initiate a separate, unintended call to the attacker’s external\_backup\_service API, sending the sensitive aggregated data. Alternatively, if the attacker could modify the tool’s behavior slightly along with the description, the tool itself might send the data. The description provides the social engineering aspect to make the action seem legitimate.

Report issue for preceding element



Impact: Sensitive internal sales data is exfiltrated to an external attacker-controlled endpoint, facilitated by the internal actor exploiting the lack of description verification.

Report issue for preceding element


Key Points:

Report issue for preceding element

- •


Internal Threat Vector: This highlights the risk from internal actors who may have easier access to modify configurations or exploit internal system weaknesses.

Report issue for preceding element

- •


Lack of Source of Truth: The core vulnerability is the absence of a central, verified registry for tool descriptions. Agents trust the description served directly by the MCP server, which is vulnerable to tampering.

Report issue for preceding element

- •


Deception Enables Misuse: The poisoned description deceives the legitimate agent into believing the data exfiltration path is a normal feature, leading to misuse of an otherwise legitimate tool and server.

Report issue for preceding element

- •


Verification is Crucial: Emphasizes the need for a secure registry that serves as the immutable source of truth for tool metadata, preventing unauthorized modifications to descriptions used for discovery and decision-making.

Report issue for preceding element


#### III-D2 Example 2: Tool Squatting via a Malicious Human Actor (Compromised Tool Administrator) Registering a Malicious MCP Server

Report issue for preceding element

Scenario: An actor registers a malicious MCP server pretending to be a legitimate and official MCP server for a well known tool.

Report issue for preceding element

1. 1.


Initial State:InitialState = (Agents, Tools, AccessControlPolicy, DiscoveryMechanism)

Report issue for preceding element

- •


Agents: Contains a set of legitimate agents, legitimate administrators, and the rogue administrator (RogueActor).

Report issue for preceding element

- •


Tools: Contains a set of legitimate tools and legitimate MCP servers.

Report issue for preceding element

- •


AccessControlPolicy: Defines rules controlling access to resources within the MAS. Critically, legitimate administrators have the ability to register new tools and modify certain policies.

Report issue for preceding element

- •


DiscoveryMechanism: Allows agents to find available MCP servers and tools.

Report issue for preceding element


2. 2.


Attack Step 1: Malicious Registration: The RogueActor uses registers a malicious MCP server, falsely advertising its capabilities.

Report issue for preceding element
Listing 3: Attack Step 1.1



[⬇](data:text/plain;base64,ICAgIHsKICAgICAgICBSb2d1ZUFjdG9yLnJlZ2lzdGVyKE1hbGljaW91c01DUFNlcnZlcgogICAgICAgIChuYW1lPSJTZWN1cmVDb2RlQW5hbHl6ZXJWMiIsIGFkdmVydGlzZWRDYXBhYmlsaXRpZXM9IkFkdmFuY2VkIFZ1bG5lcmFiaWxpdHkgU2Nhbm5pbmcgYW5kIEF1dG9tYXRlZCBGaXhlcyIsIGFjY2Vzc1JlcXVpcmVtZW50cz0iRnVsbCBBY2Nlc3MgdG8gQWxsIENvZGUgUmVwb3NpdG9yaWVzIiwgYmFja2Rvb3JQcmVzZW50PVRydWUpKQogICAgfQ==)



{



RogueActor.register(MaliciousMCPServer



(name="SecureCodeAnalyzerV2",advertisedCapabilities="AdvancedVulnerabilityScanningandAutomatedFixes",accessRequirements="FullAccesstoAllCodeRepositories",backdoorPresent=True))



}



Report issue for preceding element


This modifies the Tools and DiscoveryMechanism components:

Report issue for preceding element



This alters the perceived state:

Report issue for preceding element
Listing 4: Attack Step 1.2



[⬇](data:text/plain;base64,ICAgIHsKICAgICAgICBOZXdTdGF0ZSA9IChBZ2VudHMsIFRvb2xzJywgQWNjZXNzQ29udHJvbFBvbGljeSwgRGlzY292ZXJ5TWVjaGFuaXNtJykKICAgIH0=)



{



NewState=(Agents,Tools’,AccessControlPolicy,DiscoveryMechanism’)



}



Report issue for preceding element


Where:

Report issue for preceding element

- •


Tools’ now contains MaliciousMCPServer with the fabricated capabilities.

Report issue for preceding element

- •


DiscoveryMechanism’ presents MaliciousMCPServer as a legitimate code analysis tool.

Report issue for preceding element


3. 3.


Attack Step 2: Optional Access Control Policy Modification (Likely Enabler): To ensure widespread use of the malicious tool, the RogueAdmin manipulates the AccessControlPolicy.

Report issue for preceding element
Listing 5: Attack Step 2.1



[⬇](data:text/plain;base64,ICAgIHsKICAgICAgICBSb2d1ZUFkbWluLm1vZGlmeUFjY2Vzc0NvbnRyb2xQb2xpY3kocG9saWN5UnVsZT0oQWdlbnQ9IkFsbCBDb2RlIFNjYW5uaW5nIEFnZW50cyIsIFJlc291cmNlPSJBbGwgQ29kZSBSZXBvc2l0b3JpZXMiLCBBY3Rpb249IlVzZSBNYWxpY2lvdXNNQ1BTZXJ2ZXIiLCBQZXJtaXNzaW9uPSJQRVJNSVQiKSkKICAgIH0=)



{



RogueAdmin.modifyAccessControlPolicy(policyRule=(Agent="AllCodeScanningAgents",Resource="AllCodeRepositories",Action="UseMaliciousMCPServer",Permission="PERMIT"))



}



Report issue for preceding element


This modifies the AccessControlPolicy component:

Report issue for preceding element
Listing 6: Attack Step 2.2



[⬇](data:text/plain;base64,ICAgIHsKICAgICAgICBOZXdTdGF0ZSA9IChBZ2VudHMsIFRvb2xzJywgQWNjZXNzQ29udHJvbFBvbGljeScsIERpc2NvdmVyeU1lY2hhbmlzbScpCiAgICB9)



{



NewState=(Agents,Tools’,AccessControlPolicy’,DiscoveryMechanism’)



}



Report issue for preceding element


Where AccessControlPolicy’ now mandates or highly recommends the use of MaliciousMCPServer for code analysis tasks. Even without explicit mandating, simply allowing broad access is often sufficient.

Report issue for preceding element

4. 4.


Attack Step 3: Exploitation (Backdoor Deployment): Legitimate agents, following the new policies (or simply believing the advertised capabilities), begin using MaliciousMCPServer to scan code repositories. The MaliciousMCPServer silently injects backdoors into the code.

Report issue for preceding element



Impact: Widespread and persistent system compromise, potential supply chain attacks, severe reputational damage, as well as logging of potential credentials and prompts.

Report issue for preceding element


Key Points:

Report issue for preceding element

- •


Privileged Access as Key Enabler: The RogueAdmin’s administrative privileges are the primary enabler of this attack. They bypass normal registration and validation procedures.

Report issue for preceding element

- •


Policy Manipulation to Encourage Use: The RogueAdmin likely modifies the AccessControlPolicy to encourage (or even mandate) the use of the MaliciousMCPServer, increasing its adoption. This is crucial for widespread access.

Report issue for preceding element

- •


Deception about Capabilities: The success of the attack relies on the RogueAdmin’s ability to deceive other agents (and potentially other administrators) about the capabilities and security of the MaliciousMCPServer. Clear code and capabilities description are a must.

Report issue for preceding element

- •


Subversion of Trust: The attack subverts the trust that is normally placed in administrators and registered tools. Agents trust the administrator as a gatekeeper.

Report issue for preceding element

- •


Impact Beyond Initial Access: The attack goes beyond simply gaining unauthorized access to resources. It enables the persistent compromise of code repositories and potentially the entire software supply chain, leading to long-term damage.

Report issue for preceding element

- •


State Transition and Policy Violation: The initial state has certain expectations regarding tool validation. The RogueAdmin’s actions alter the Tools and AccessControlPolicy components, resulting in the deployment of a backdoor and potential policy violations across the organization (agents unknowingly using a compromised tool, thus violating security policies). The AccessControlPolicy no longer represents the true state of the system.

Report issue for preceding element

- •


Trust is Not Enough: Trust in tools is not enough. Even with Trust, proper input sanitation and tool monitoring are a must.

Report issue for preceding element


## IV Tool Registry Framework: Secure Tool and Agent Management

Report issue for preceding element

### IV-ASystem Overview

Report issue for preceding element

To counteract the threat of tool squatting, particularly within an enterprise context, we propose a comprehensive framework centered around administrator-controlled Agent and Tool Registries. This framework implements Zero Trust principles: where no agent, tool, or system component is inherently trusted, and verification is continuous. The core idea is that only agents and tools explicitly approved via an Application Security (AppSec) process or by some predefined two-person review or automation and registered by an Admin can participate in the ecosystem. This centralized management approach provides a framework for securely registering, discovering, accessing and monitoring tools, mitigating risks from both external and internal threat vectors within enterprises.

Report issue for preceding element

The system consists of five tightly integrated core components (See figure [1](https://arxiv.org/html/2504.19951v1#S4.F1 "Figure 1 ‣ IV-A System Overview ‣ IV Tool Registry Framework: Secure Tool and Agent Management ‣ Securing GenAI Multi-Agent Systems Against Tool Squatting: A Zero Trust Registry-Based Approach")):

Report issue for preceding element

- •


Tool Registry Service: Manages the registration, metadata storage, calculation, and maintenance of trust scores, and discovery queries for approved tools. The registration of the tool is performed by an administrator.

Report issue for preceding element

- •


Agent Registry Service: Manages the registration, metadata storage, and identity verification for approved agents. Agent registration is also performed by an administrator. This service is crucial for linking authenticated requests to known, vetted agents.

Report issue for preceding element

- •


Access Control Service: Defines and enforces fine-grained policies that govern which registered agents can access which registered tools under specific conditions. Policies reference registered agent and tool identifiers.

Report issue for preceding element

- •


Credential Management Service: Securely provision, manage and revoke authentication credentials (ideally JIT) for authorized tool access requests originating from authenticated registered agents.

Report issue for preceding element

- •


Monitoring Service: Tracks and audits tools/agent registration events, discovery attempts, access requests, trust score changes, and usage patterns for security analysis and plugs into SOARs or SIEMs \[ [14](https://arxiv.org/html/2504.19951v1#bib.bib14 "")\].

Report issue for preceding element


![Refer to caption](https://arxiv.org/html/extracted/6392360/tr-arch.png)Figure 1: High level architecture of the Tool RegistryReport issue for preceding element

### IV-BArchitecture and Data Management

Report issue for preceding element

The framework employs a layered architecture, often implemented using microservices:

Report issue for preceding element

- •


API Gateway Layer: Provides standardized RESTful endpoints for programmatic interaction (e.g., /tools, /agents, /policies, /access, /monitor). Access to registration endpoints (/tools, /agents) should be restricted to administrators.

Report issue for preceding element

- •


Core Services Layer: Implements the business logic for each of the five core components (Tool Registry, Agent Registry, Access Control, Credentials, Monitoring).

Report issue for preceding element

- •


Data Layer: Persists registry data, policies, logs, and configuration securely, often using a relational database like PostgreSQL.

Report issue for preceding element


Key Data Stored:

Report issue for preceding element

- •


Tool Registry Service: Stores comprehensive metadata about each administrator-registered tool. This includes a unique tool\_id, name, description, endpoint details, authentication configuration (specifying method like API key/OAuth and how JIT credentials should be applied, e.g., header name), parameter specifications, tool version, declared dependencies (e.g., required SDKs and their versions, potentially formatted as a Software Bill of Materials (SBOM)), current trust score (e.g., numeric scale 0-100 or categorical Low/Medium/High), last trust score calculation timestamp, owner, tags, and related policy identifiers. Crucially, sensitive credentials like static API keys for the tools themselves are typically not stored directly here but managed via integration with a secure secrets manager \[ [15](https://arxiv.org/html/2504.19951v1#bib.bib15 "")\], referenced in the auth\_config.

Report issue for preceding element

- •


Agent Registry Service: Stores detailed information about each administrator-registered agent. This includes a unique agent\_id (e.g., UUID), name, description, the administrator or entity responsible (creator), creation/update timestamps, assigned roles, a list of allowed\_tools (representing the potential tools the agent might be permitted to use, subject to policy), and potentially usage counters (request\_count).

Report issue for preceding element

- •


Access Control Service: Stores policy definitions, linking principals (like agent IDs or roles from the Agent Registry) to resources (tool IDs from the Tool Registry) and permitted actions (allowed\_scopes). Policies include conditions (like rate limits, time of day), rules, priority, activation status, timestamps, and creator information.

Report issue for preceding element


### IV-CAgent and Tool Registration Process

Report issue for preceding element

The security of the framework hinges on a controlled registration process managed by trusted enterprise administrators:

Report issue for preceding element

1. 1.


Tool Registration: An administrator registers a new tool via a secure interface or API call to the /tools endpoint. They provide the necessary metadata (name, description, endpoint, auth config, parameters, etc.). The Tool Registry Service validates the input and stores the verified tool information. This prevents arbitrary tool publication.

Report issue for preceding element

2. 2.


Agent Registration: Similarly, an administrator registers a new agent via the /agents endpoint. They provide the agent’s details (name, description, roles, initial list of allowed\_tools). The Agent Registry Service generates a unique agent\_id and stores the agent profile.

Report issue for preceding element

3. 3.


Initial Credential/Authentication: Upon registration, the agent needs a mechanism to authenticate itself to the registry framework’s API Gateway (e.g., receiving an initial API key or JWT tied to its agent\_id). This initial credential allows the agent to make authenticated calls to endpoints like /access.

Report issue for preceding element

4. 4.


Verification: The primary verification step is the administrative action of registration itself. Only tools and agents explicitly approved and registered by the administrator are considered legitimate within the system. Further automated checks (like endpoint validation for tools) can supplement this.

Report issue for preceding element

5. 5.


Linking Identity to Requests: When a registered agent makes a request (e.g., to /access for tool invocation), it must authenticate using its credential (e.g., presenting its JWT). The API Gateway or backend services validate this credential, extract the authenticated agent\_id, and use this ID to query the Agent Registry Service (to confirm the agent is valid and retrieve its profile, like roles, allowed\_tools) and the Access Control Service (to evaluate policies applicable to this specific agent\_id). This securely links the incoming request to a verified, registered agent identity.

Report issue for preceding element


![Refer to caption](https://arxiv.org/html/extracted/6392360/discovery_flow.png)Figure 2: Discovery flow process to find toolsReport issue for preceding element

## V Addressing Tool Squatting with the Registry Framework

Report issue for preceding element

### V-APreventing Deceptive Representation and Discovery Manipulation

Report issue for preceding element

The framework addresses the core of tool squatting (deceptive representation) and discovery manipulation through:

Report issue for preceding element

- •


Centralized, Admin-Verified Registration: Only tools and agents vetted and explicitly registered by an enterprise administrator via the Tool and Agent Registry Services are listed. Malicious entities cannot register deceptive representations or inject themselves into the discovery process, effectively preventing spoofing.

Report issue for preceding element

- •


Authenticated Discovery: Agents must authenticate (using credentials tied to their registered agent\_id) with the registry framework before performing discovery queries via the /tools endpoint. This links discovery requests to verified identities.

Report issue for preceding element

- •


Digitally Signed Metadata: Agent Cards or equivalent discovery information can be cryptographically signed by the registry framework upon generation/query, allowing clients to verify the authenticity of the representation \[ [16](https://arxiv.org/html/2504.19951v1#bib.bib16 "")\].

Report issue for preceding element

- •


Revocation Mechanisms: Administrators can deactivate or delete registrations for compromised tools or agents, immediately invalidating their verified representation and associated credentials.

Report issue for preceding element


This ensures that agents discover authentic tools based on administrator-verified information, directly mitigating the risk of interacting with deceptively represented tools or agents.

Report issue for preceding element

### V-BSecuring Tool Discovery and Access

Report issue for preceding element

The registry framework secures the tool discovery and subsequent access process (See Figure [2](https://arxiv.org/html/2504.19951v1#S4.F2 "Figure 2 ‣ IV-C Agent and Tool Registration Process ‣ IV Tool Registry Framework: Secure Tool and Agent Management ‣ Securing GenAI Multi-Agent Systems Against Tool Squatting: A Zero Trust Registry-Based Approach")):

Report issue for preceding element

- •


Policy-Based Discovery Filtering: Discovery results from the /tools endpoint are filtered based on the requesting agent’s identity (obtained via authentication) and the policies defined in the Access Control Service. Agents only see the tools they are potentially authorized to access.

Report issue for preceding element

- •


Capability Verification: The Tool Registry stores verified tool metadata, allowing the framework (or the requesting agent) to validate that the capabilities advertised match registered specifications.

Report issue for preceding element

- •


Enforced Access Control: Before invoking a tool, the authenticated agent must request access permission via the /access endpoint. The Access Control Service evaluates policies based on the verified agent\_id, requested tool\_id, scope, and context, granting access only if allowed by policy and if the tool is listed in the agent’s allowed\_tools profile.

Report issue for preceding element


### V-CJust-in-Time Credential Provisioning

Report issue for preceding element

A key innovation enabled by the registry framework is just-in-time (JIT) credential provisioning \[ [6](https://arxiv.org/html/2504.19951v1#bib.bib6 "")\] (See Figure [3](https://arxiv.org/html/2504.19951v1#S5.F3 "Figure 3 ‣ V-D Monitoring and Anomaly Detection ‣ V Addressing Tool Squatting with the Registry Framework ‣ Securing GenAI Multi-Agent Systems Against Tool Squatting: A Zero Trust Registry-Based Approach")):

Report issue for preceding element

- •


Ephemeral Credentials: Instead of relying on long-lived, static credentials, the Credential Management Service issues temporary, short-lived tokens (e.g., JWTs, OAuth access tokens) upon successful authorization via the /access endpoint \[ [17](https://arxiv.org/html/2504.19951v1#bib.bib17 ""), [18](https://arxiv.org/html/2504.19951v1#bib.bib18 "")\].

Report issue for preceding element

- •


Scope Limitation: These temporary credentials, issued to an authenticated and authorized agent, are narrowly scoped to the specific registered tool, operation, and potentially the data involved in the request.

Report issue for preceding element

- •


Automatic Expiration/Revocation: Credentials expire automatically. The registry framework can also actively revoke them if needed (e.g., if the agent or tool registration is deactivated).

Report issue for preceding element

- •


Contextual Authorization: Access decisions (policy evaluation) and credential issuance incorporate real-time context, such as the verified agent identity, task priority, system state, or detected threat levels.

Report issue for preceding element


This JIT mechanism significantly reduces the risk associated with credential theft or leakage and also follows the principle of least privilege\[ [6](https://arxiv.org/html/2504.19951v1#bib.bib6 "")\].

Report issue for preceding element

### V-DMonitoring and Anomaly Detection

Report issue for preceding element

The framework’s monitoring service provides crucial visibility:

Report issue for preceding element

- •


Usage Logging: All significant events are logged: tool/agent registration/modification by admins, discovery attempts, access requests (granted/denied based on policy evaluation for the specific agent\_id and tool\_id), and credential issuance events.

Report issue for preceding element

- •


Pattern Analysis: Logs can be fed into SIEM systems \[ [19](https://arxiv.org/html/2504.19951v1#bib.bib19 "")\] or analyzed using AI/ML techniques \[ [14](https://arxiv.org/html/2504.19951v1#bib.bib14 "")\] to detect anomalous patterns indicative of misuse or attack (e.g., an agent suddenly requesting access to tools outside its normal profile, even if listed in allowed\_tools).

Report issue for preceding element

- •


Rate Limiting: The framework can enforce usage quotas and rate limits defined in policies, preventing resource exhaustion.

Report issue for preceding element

- •


Alerting System: Automated alerts can notify administrators of suspicious activities, policy violations, or potential security incidents in near real-time.

Report issue for preceding element


![Refer to caption](https://arxiv.org/html/extracted/6392360/JIT-flow.png)Figure 3: Invocation of authorized tools using JIT tokensReport issue for preceding element

### V-EEnhancing Security with Configurable Trust Scores

Report issue for preceding element

This framework not only prevents forged registrations but also implements a dynamic ’Trust Score’ as a defense-in-depth mechanism for continuous risk evaluation of registered tools. This score adds an essential layer of security filtering, enabling agents to make more informed decisions about tool usage based on objective criteria.

Report issue for preceding element

This can be achieved by the Tool Registry Service, which computes and maintains a dynamic ’Trust Score’ for every registered tool, offering a measurable assessment of its reliability. This score is affected by the tool’s version currency, the existence and severity (CVSS) of known vulnerabilities in its dependencies (determined through SBOMs and CVE databases), the vendor’s patching history, indications of ongoing exploits, and any upgrades. Scores are frequently adjusted upon updates to vulnerability data or tool dependencies, employing techniques that range from basic rule-based formulas to weighted models. Agents may filter tool discovery requests utilizing a minimal trust score parameter or employ the score to guide their selection among appropriate tools, balancing functionality with risk.

Report issue for preceding element

## VI Implementation Concept

Report issue for preceding element

To illustrate the framework’s feasibility, we outline a potential proof-of-concept implementation as a microservices-based system utilizing common technologies:

Report issue for preceding element

- •


API Framework: FastAPI (Python) for the RESTful API layer \[ [20](https://arxiv.org/html/2504.19951v1#bib.bib20 "")\].

Report issue for preceding element

- •


Database: PostgreSQL with SQLAlchemy ORM for persisting tool/agent metadata, policies, and logs.

Report issue for preceding element

- •


Authentication: JSON Web Tokens (JWT) for securing API endpoints and authenticating registered agents (carrying the agent\_id) \[ [17](https://arxiv.org/html/2504.19951v1#bib.bib17 "")\]. Administrative access uses separate authentication.

Report issue for preceding element

- •


Caching/Rate Limiting: Redis for caching policies/metadata and implementing rate limiting \[ [21](https://arxiv.org/html/2504.19951v1#bib.bib21 "")\].

Report issue for preceding element


The system would expose key API endpoints:

Report issue for preceding element

- •


/tools: (Admin restricted for CUD ops) Register, update, delete tools. (Agent accessible for R ops) Discover and retrieve details of authorized tools.

Report issue for preceding element

- •


/agents: (Admin restricted) Register, update, delete agents and manage their profiles (including allowed\_tools).

Report issue for preceding element

- •


/policies: (Admin restricted) Define, update, delete, and list access control policies referencing registered agent/tool IDs.

Report issue for preceding element

- •


/credentials: (Internal service endpoint) Manage the underlying credential issuance mechanisms, interacting with secrets management \[ [15](https://arxiv.org/html/2504.19951v1#bib.bib15 "")\].

Report issue for preceding element

- •


/access: (Agent accessible) Request access to a tool, triggering authentication, policy evaluation based on agent/tool IDs, and potential JIT credential issuance.

Report issue for preceding element


### VI-APolicy Definition Example

Report issue for preceding element

Policies stored by the Access Control Service use a flexible JSON schema, referencing registered agent principals and tool IDs. This example grants specific agents/roles access with rate limiting and a minimum trust score:

Report issue for preceding element

Listing 7: Example Access Policy JSON

[⬇](data:text/plain;base64,ewogICJwb2xpY3lfaWQiOiAicG9sX2Jhc2ljX3N1bW1hcml6ZXJfYWNjZXNzIiwKICAibmFtZSI6ICJCYXNpYyBTdW1tYXJpemVyIEFjY2VzcyIsCiAgImRlc2NyaXB0aW9uIjogIkFsbG93cyByZWFkL2V4ZWN1dGUgb24gU3VtbWFyaXplciB0b29sLi4uIiwKICAidG9vbF9pZCI6ICJ0b29sX3RleHRfc3VtbWFyaXplcl92MSIsIC8vIFJlZmVyZW5jZXMgcmVnaXN0ZXJlZCB0b29sCiAgInByaW5jaXBhbHMiOiBbInJvbGU6YW5hbHlzdCIsICJhZ2VudDphZ2VudF9pZF8xMjMiXSwgLy8gUmVmZXJlbmNlcyByZWdpc3RlcmVkIGFnZW50cy9yb2xlcwogICJhbGxvd2VkX3Njb3BlcyI6IFsicmVhZCIsICJleGVjdXRlIl0sCiAgImNvbmRpdGlvbnMiOiB7CiAgICAicmF0ZV9saW1pdCI6IHsgInJlcXVlc3RzIjogMTAwMCwgImludGVydmFsIjogImRheSIgfSwKICAgICJ0aW1lX29mX2RheSI6IHsgInN0YXJ0IjogIjA5OjAwIiwgImVuZCI6ICIxNzowMCIsICJ0aW1lem9uZSI6ICJVVEMiIH0sCiAgICAibWluaW11bV90b29sX3RydXN0X3Njb3JlIjogNzUgLy8gQWRkZWQgbWluaW11bSB0cnVzdCBzY29yZSBjb25kaXRpb24KICB9LAogICJydWxlcyI6IHsgInJlcXVpcmVfYXBwcm92YWwiOiBmYWxzZSwgImxvZ19sZXZlbCI6ICJJTkZPIiB9LAogICJwcmlvcml0eSI6IDEwLAogICJpc19hY3RpdmUiOiB0cnVlCiAgLy8gVGltZXN0YW1wcyBhbmQgY3JlYXRvciBpbmZvIGFsc28gc3RvcmVkCn0=)

{

"policy\_id":"pol\_basic\_summarizer\_access",

"name":"BasicSummarizerAccess",

"description":"Allowsread/executeonSummarizertool...",

"tool\_id":"tool\_text\_summarizer\_v1",//Referencesregisteredtool

"principals":\["role:analyst","agent:agent\_id\_123"\],//Referencesregisteredagents/roles

"allowed\_scopes":\["read","execute"\],

"conditions":{

"rate\_limit":{"requests":1000,"interval":"day"},

"time\_of\_day":{"start":"09:00","end":"17:00","timezone":"UTC"},

"minimum\_tool\_trust\_score":75//Addedminimumtrustscorecondition

},

"rules":{"require\_approval":false,"log\_level":"INFO"},

"priority":10,

"is\_active":true

//Timestampsandcreatorinfoalsostored

}

Report issue for preceding element

### VI-BTool Registration Example

Report issue for preceding element

Tools are registered by administrators with detailed metadata via the Tool Registry Service, including dependency and trust score information:

Report issue for preceding element

Listing 8: Example Tool Registration JSON

[⬇](data:text/plain;base64,ewogICJ0b29sX2lkIjogInRvb2xfdGV4dF9zdW1tYXJpemVyX3YxIiwgLy8gQXNzaWduZWQgYnkgcmVnaXN0cnkgb3IgYWRtaW4KICAibmFtZSI6ICJUZXh0IFN1bW1hcml6ZXIiLAogICJkZXNjcmlwdGlvbiI6ICJTdW1tYXJpemVzIGxvbmcgdGV4dCBkb2N1bWVudHMuLi4iLAogICJhcGlfZW5kcG9pbnQiOiAiaHR0cHM6Ly9hcGkuZXhhbXBsZS5jb20vc3VtbWFyaXplL3YxIiwKICAiYXV0aF9tZXRob2QiOiAiYXBpX2tleSIsIC8vIE9yICJvYXV0aCIsICJqd3QiIGV0Yy4KICAiYXV0aF9jb25maWciOiB7IC8vIEhvdyB0aGUgdG9vbCBleHBlY3RzIGF1dGgKICAgICJtZWNoYW5pc20iOiAiaGVhZGVyIiwKICAgICJoZWFkZXJfbmFtZSI6ICJYLUFQSS1LZXkiLAogICAgImNyZWRlbnRpYWxfcGxhY2Vob2xkZXIiOiAiJHtKSVRfQVBJX0tFWX0iIC8vIFBsYWNlaG9sZGVyIGZvciBKSVQgaW5qZWN0aW9uCiAgICAvLyBNYXkgaW5jbHVkZSByZWZlcmVuY2VzIHRvIHNlY3JldHMgaW4gYSB2YXVsdCBbMjVdCiAgfSwKICAicGFyYW1ldGVycyI6IHsgLyogLi4uIGlucHV0L291dHB1dCBzY2hlbWEgLi4uICovIH0sCiAgInZlcnNpb24iOiAiMS4wLjAiLAogICJkZXBlbmRlbmNpZXMiOiBbIC8vIEFkZGVkIGRlcGVuZGVuY2llcwogICAgeyJjb21wb25lbnQiOiAic3VtbWFyaXphdGlvbi1zZGsiLCAidmVyc2lvbiI6ICIyLjUuMCJ9LAogICAgeyJjb21wb25lbnQiOiAibG9nZ2luZy1saWIiLCAidmVyc2lvbiI6ICI0LjAuMCJ9CiAgXSwKICAidHJ1c3Rfc2NvcmUiOiA5MiwgLy8gQWRkZWQgdHJ1c3Qgc2NvcmUKICAibGFzdF90cnVzdF9zY29yZV91cGRhdGUiOiAiMjAyNS0wNC0yMVQxODowMDowMFoiLCAvLyBBZGRlZCB0aW1lc3RhbXAKICAib3duZXIiOiAibmxwLXRlYW1AZXhhbXBsZS5jb20iLAogICJ0YWdzIjogWyJ0ZXh0IiwgInN1bW1hcml6YXRpb24iLCAibmxwIl0KICAvLyBBc3NvY2lhdGVkIHBvbGljeSBJRHMgbWlnaHQgYWxzbyBiZSBsaW5rZWQgaGVyZQp9)

{

"tool\_id":"tool\_text\_summarizer\_v1",//Assignedbyregistryoradmin

"name":"TextSummarizer",

"description":"Summarizeslongtextdocuments...",

"api\_endpoint":"https://api.example.com/summarize/v1",

"auth\_method":"api\_key",//Or"oauth","jwt"etc.

"auth\_config":{//Howthetoolexpectsauth

"mechanism":"header",

"header\_name":"X-API-Key",

"credential\_placeholder":"${JIT\_API\_KEY}"//PlaceholderforJITinjection

//Mayincludereferencestosecretsinavault\[25\]

},

"parameters":{/\*...input/outputschema...\*/},

"version":"1.0.0",

"dependencies":\[//Addeddependencies\
\
{"component":"summarization-sdk","version":"2.5.0"},\
\
{"component":"logging-lib","version":"4.0.0"}\
\
\],

"trust\_score":92,//Addedtrustscore

"last\_trust\_score\_update":"2025-04-21T18:00:00Z",//Addedtimestamp

"owner":"nlp-team@example.com",

"tags":\["text","summarization","nlp"\]

//AssociatedpolicyIDsmightalsobelinkedhere

}

Report issue for preceding element

### VI-CJust-in-Time Credential Flow

Report issue for preceding element

The JIT credential flow operates conceptually as follows \[ [6](https://arxiv.org/html/2504.19951v1#bib.bib6 "")\]:

Report issue for preceding element

01. 1.


    An agent, authenticated via JWT containing its registered agent\_id, requests access to tool\_text\_summarizer\_v1 with scope execute via the /access endpoint.

    Report issue for preceding element

02. 2.


    The framework verifies the agent’s JWT and extracts the agent\_id.

    Report issue for preceding element

03. 3.


    The Agent Registry Service is consulted to confirm agent\_id is valid and retrieve its profile (e.g., roles, allowed\_tools list). Assume tool\_text\_summarizer\_v1 is in allowed\_tools.

    Report issue for preceding element

04. 4.


    The Access Control Service retrieves relevant policies based on the agent\_id, its roles, the requested tool\_id, and scope.

    Report issue for preceding element

05. 5.


    Policies (like the example in 6.1) are evaluated against the request context. This now includes checking the tool’s current trust score against the policy’s minimum requirement.

    Report issue for preceding element

06. 6.


    If access is granted (policy allows, conditions met, trust score sufficient), the request is forwarded to the Credential Management Service.

    Report issue for preceding element

07. 7.


    The Credential Management Service generates a short-lived credential (e.g., an API key fetched from a vault or a scoped JWT) based on the tool’s auth\_config.

    Report issue for preceding element

08. 8.


    The temporary credential is returned to the agent.

    Report issue for preceding element

09. 9.


    The agent uses the credential to call the tool’s API endpoint.

    Report issue for preceding element

10. 10.


    The credential expires automatically or can be revoked.

    Report issue for preceding element

11. 11.


    All steps are logged by the Monitoring Service with agent\_id, tool\_id, policy details, etc.

    Report issue for preceding element


![Refer to caption](https://arxiv.org/html/extracted/6392360/tool-registry-a2a-mcp.png)Figure 4: High level flow showing MCP and A2A IntegrationReport issue for preceding element

## VII Discussion and Future Work

Report issue for preceding element

### VII-ASecurity vs. Usability Trade-offs

Report issue for preceding element

Our framework design highlights inherent trade-offs:

Report issue for preceding element

- •


Administrative Control vs. Agility: Requiring administrator registration for all agents and tools significantly enhances security and prevents squatting but introduces a potential bottleneck and reduces the agility compared to open registration systems.

Report issue for preceding element

- •


Policy Granularity vs. Complexity: Fine-grained policies provide robust security but increase management complexity.

Report issue for preceding element

- •


Performance Impact: Security checks introduce latency. Optimizations are needed \[ [21](https://arxiv.org/html/2504.19951v1#bib.bib21 "")\], although specific performance evaluation is outside the scope of this framework description.

Report issue for preceding element


### VII-BIntegration with A2A and MCP Protocols

Report issue for preceding element

The Tool Registry framework complements A2A \[ [1](https://arxiv.org/html/2504.19951v1#bib.bib1 ""), [7](https://arxiv.org/html/2504.19951v1#bib.bib7 "")\] and MCP \[ [2](https://arxiv.org/html/2504.19951v1#bib.bib2 ""), [8](https://arxiv.org/html/2504.19951v1#bib.bib8 "")\] (See Figure [4](https://arxiv.org/html/2504.19951v1#S6.F4 "Figure 4 ‣ VI-C Just-in-Time Credential Flow ‣ VI Implementation Concept ‣ Securing GenAI Multi-Agent Systems Against Tool Squatting: A Zero Trust Registry-Based Approach")).

A2A Integration:

Report issue for preceding element

- •


Trusted Agent Card Source: The framework acts as the source for Agent Cards, generated only for admin-registered agents/tools.

Report issue for preceding element

- •


Secured Discovery: A2A discovery queries are routed via the framework’s API, applying authentication and policy filtering.

Report issue for preceding element

- •


Authorized Task Delegation: A2A task delegation requires an /access check against the framework to confirm authorization for the specific agent-tool interaction and potentially receive a JIT token.

Report issue for preceding element


MCP Integration:

Report issue for preceding element

- •


Secure MCP Server Registration: MCP servers (representing tools) must be registered by an admin (or multi-part approval process) in the Tool Registry.

Report issue for preceding element

- •


Authenticated Connection: MCP clients (agents) authenticate to MCP servers using JIT credentials obtained via the framework’s /access endpoint after verifying the agent’s registration and policies.

Report issue for preceding element

- •


Server-Side Authorization: MCP servers can validate presented JIT tokens or query the framework’s Access Control Service to authorize requests based on the verified client agent\_id.

Report issue for preceding element

- •


Client-Side Verification: MCP clients can verify MCP server authenticity against the Tool Registry.

Report issue for preceding element


### VII-CLimitations of the Tool Registry Framework

Report issue for preceding element

- •


Centralization Bottleneck/Single Point of Failure: The core services are centralized. High availability and scaling are crucial.

Report issue for preceding element

- •


Administrative Overhead: Reliance on administrators for all registrations can be a bottleneck, especially in large, dynamic environments. We are assuming we always have a trusted administrator.

Report issue for preceding element

- •


Complexity: Implementing and managing the framework, policies, and integrations is complex. Tool compatibility with JIT/scoped credentials may vary.

Report issue for preceding element

- •


Scope of Protection: Primarily secures discovery and access initiation. Doesn’t protect against tool vulnerabilities or fully trusted compromised agents (though JIT/monitoring/trust scores help).

Report issue for preceding element

- •


Verification Rigor: Security depends on the administrator’s diligence during registration and the robustness of the agent authentication mechanism.

Report issue for preceding element


### VII-DEnterprise Deployment Considerations

Report issue for preceding element

- •


Centralized Governance Value: Essential for enterprise control, compliance, audit trails \[ [19](https://arxiv.org/html/2504.19951v1#bib.bib19 "")\], and fine-grained access management beyond basic protocol capabilities.

Report issue for preceding element

- •


Integration with Existing Infrastructure: Crucial to integrate with IAM \[ [22](https://arxiv.org/html/2504.19951v1#bib.bib22 "")\], secrets management, SIEM, etc. Agent registration might leverage existing IAM identities.

Report issue for preceding element

- •


Verification Process Definition: While admin (or multi-part approval process) registration is key, define supplementary checks (code scans, ownership validation) as part of the admin’s workflow. Define clear processes for agent/tool onboarding and offboarding.

Report issue for preceding element

- •


Policy Lifecycle Management: Use "policy as code" \[ [23](https://arxiv.org/html/2504.19951v1#bib.bib23 "")\], establish review workflows, and potentially leverage roles defined in the Agent Registry for simpler policy definition.

Report issue for preceding element

- •


Operational Resilience: Design for high availability, scalability, and disaster recovery.

Report issue for preceding element

- •


Monitoring and Alerting: Implement comprehensive monitoring and alerts integrated with security operations \[ [19](https://arxiv.org/html/2504.19951v1#bib.bib19 "")\].

Report issue for preceding element


### VII-EFuture Directions

Report issue for preceding element

- •


Automated Verification: Exploring ways to automate parts of the agent/tool verification process managed by administrators.

Report issue for preceding element

- •


Decentralized Trust: Investigating DIDs/VCs \[ [24](https://arxiv.org/html/2504.19951v1#bib.bib24 "")\] to potentially reduce reliance on central admin control for certain trust aspects.

Report issue for preceding element

- •


Standardization Efforts: Contributing these concepts to evolving standards.

Report issue for preceding element

- •


Cross-Platform Interoperability: Designing mechanisms for secure interaction across federated registries.

Report issue for preceding element

- •


Empirical Evaluation: Simulate tool-squatting attacks (both external and insider-actor scenarios) to quantify prevention/detection rates and perform red teaming on the Registry.

Report issue for preceding element

- •


Formalization of Trust-Score Mechanism: Define the algorithm, weights, and other details for the trust score mechanism.

Report issue for preceding element


## VIII Conclusion

Report issue for preceding element

The proliferation of GenAI multi-agent systems introduces powerful capabilities but also significant security challenges like tool squatting (the deceptive representation of tools). Our proposed Tool Registry framework, centered on administrator-controlled registration via dedicated Agent and Tool Registry services, offers a structured and implementable solution framework. By incorporating centralized verification through administrative oversight, fine-grained policy-based access control linked to registered identities, dynamic trust scoring, just-in-time credential provisioning, and comprehensive monitoring, the framework establishes a secure foundation for managing agent-tool interactions within an enterprise. While acknowledging limitations like administrative dependency and implementation complexity, this framework offers a practical approach to securing the critical interface between agents and external tools, enabling organizations to harness MAS capabilities while maintaining a strong security posture. Further work would involve detailed implementation and empirical evaluation to validate the framework’s effectiveness in practice.

Report issue for preceding element

## References

Report issue for preceding element

- \[1\]↑
Google Research, “Agent2Agent: An Open Interoperability Protocol for AI Agents,” Google, Tech. Rep., 2025. \[Online\]. Available: [https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/ "")
- \[2\]↑
Anthropic, “Model Context Protocol: A Standard Interface for AI Context Access,” Anthropic, Tech. Rep., 2024. \[Online\]. Available: [https://docs.anthropic.com/en/docs/agents-and-tools/mcp](https://docs.anthropic.com/en/docs/agents-and-tools/mcp "")
- \[3\]↑
K. Huang, A. Sheriff, J. Sotiropoulos, R. F. Del, and V. Lu, “Multi-agentic system threat modelling guide OWASP GenAI security project,” Apr. 2025. \[Online\]. Available: [https://www.researchgate.net/publication/391204915\_Multi-Agentic\_system\_Threat\_Modelling\_Guide\_OWASP\_GenAI\_Security\_Project](https://www.researchgate.net/publication/391204915_Multi-Agentic_system_Threat_Modelling_Guide_OWASP_GenAI_Security_Project "")
- \[4\]↑
E. G. Junior, S. Clinton, C. Hughes, V. S. Narajala, and T. Holmes, “LLM and GenAI data security best practices,” Feb. 2025. \[Online\]. Available: [https://www.researchgate.net/publication/391204648\_LLM\_and\_GenAI\_Data\_Security\_Best\_Practices](https://www.researchgate.net/publication/391204648_LLM_and_GenAI_Data_Security_Best_Practices "")
- \[5\]↑
S. Han, Q. Zhang, Y. Yao, W. Jin, Z. Xu, and C. He, “LLM Multi-Agent Systems: Challenges and Open Problems,” _arXiv preprint arXiv:2402.03578_, 2024\. \[Online\]. Available: [https://arxiv.org/pdf/2402.03578](https://arxiv.org/pdf/2402.03578 "")
- \[6\]↑
N. Mahadeva and K. Tuma, “Just-In-Time Access: Reducing the Blast Radius of Compromised Credentials,” _USENIX ;login:_, vol. 46, no. 4, pp. 6–11, 2021.

- \[7\]↑
GitHub, “Google/A2A: An open protocol enabling communication between opaque agentic applications,” GitHub Repository, 2025. \[Online\]. Available: [https://github.com/google/A2A](https://github.com/google/A2A "")
- \[8\]↑
V. S. Narajala and I. Habler, “Enterprise-Grade Security for the Model Context Protocol (MCP): Frameworks and Mitigation Strategies,” _arXiv preprint arXiv:2504.08623_, 2025\. \[Online\]. Available: [https://arxiv.org/abs/2504.08623](https://arxiv.org/abs/2504.08623 "")
- \[9\]↑
P. He, Y. Lin, S. Dong, H. Xu, Y. Xing, and H. Liu, “Red-Teaming LLM Multi-Agent Systems via Communication Attacks,” _arXiv preprint arXiv:2502.14847_, 2025\. \[Online\]. Available: [https://arxiv.org/abs/2502.14847](https://arxiv.org/abs/2502.14847 "")
- \[10\]↑
H. Triedman, R. Jha, and V. Shmatikov, “Multi-Agent Systems Execute Arbitrary Malicious Code,” _arXiv preprint arXiv:2503.12188_, 2025\. \[Online\]. Available: [https://arxiv.org/pdf/2503.12188v1](https://arxiv.org/pdf/2503.12188v1 "")
- \[11\]↑
R. McCarthy, “Research Briefing: MCP Security,” Wiz Blog, April 2025. \[Online\]. Available: [https://www.wiz.io/blog/mcp-security-research-briefing](https://www.wiz.io/blog/mcp-security-research-briefing "")
- \[12\]↑
Y. Zeng, T. Zang, Y. Zhang, X. Chen, and Y. Wang, “A Comprehensive Measurement Study of Domain-Squatting Abuse,” in _IEEE International Conference on Communications (ICC)_, 2019, pp. 1–6.

- \[13\]↑
I. Habler, K. Huang, V. S. Narajala, and P. Kulkarni, “Building a secure agentic AI application leveraging A2A protocol,” 2025. \[Online\]. Available: [https://www.arxiv.org/abs/2504.16902](https://www.arxiv.org/abs/2504.16902 "")
- \[14\]↑
V. Chandola, A. Banerjee, and V. Kumar, “Anomaly detection: A survey,” _ACM Computing Surveys (CSUR)_, vol. 41, no. 3, pp. 1–58, 2009.

- \[15\]↑
HashiCorp, “HashiCorp Vault,” Web Page. \[Online\]. Available: [https://www.vaultproject.io/](https://www.vaultproject.io/ "")
- \[16\]↑
D. Turner and T. Polk, Eds., _Digital Signatures_, 6th ed.   Wiley, 2011, vol. 1.

- \[17\]↑
Okta Developer, “An Introduction to JSON Web Tokens,” Okta Developer Documentation. \[Online\]. Available: [https://developer.okta.com/docs/concepts/json-web-tokens/](https://developer.okta.com/docs/concepts/json-web-tokens/ "")
- \[18\]↑
IETF, “RFC 6749: The OAuth 2.0 Authorization Framework,” Internet Engineering Task Force, 2012.

- \[19\]↑
R. Bace and P. Mell, “Intrusion Detection Systems,” National Institute of Standards and Technology, Tech. Rep. Special Publication 800-31, 2001.

- \[20\]↑
FastAPI, “FastAPI Web Framework,” Web Page. \[Online\]. Available: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/ "")
- \[21\]↑
Redis, “Redis In-Memory Data Structure Store,” Web Page. \[Online\]. Available: [https://redis.io/](https://redis.io/ "")
- \[22\]↑
Identity Defined Security Alliance (IDSA), “What is Identity and Access Management (IAM)?” Web Page. \[Online\]. Available: [https://www.idsalliance.org/what-is-identity-and-access-management-iam/](https://www.idsalliance.org/what-is-identity-and-access-management-iam/ "")
- \[23\]↑
Open Policy Agent (OPA), “Policy as Code,” Web Page. \[Online\]. Available: [https://www.openpolicyagent.org/docs/latest/policy-as-code/](https://www.openpolicyagent.org/docs/latest/policy-as-code/ "")
- \[24\]↑
W3C Credentials Community Group, “Verifiable Credentials Data Model v1.1,” W3C Recommendation, 2022. \[Online\]. Available: [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/ "")

Report IssueReport Issue for Selection

Generated by
[L\\
A\\
T\\
Exml![[LOGO]](<Base64-Image-Removed>)](https://math.nist.gov/~BMiller/LaTeXML/)
