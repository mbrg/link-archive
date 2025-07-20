---
title: "Securing the Model Context Protocol: Building a safer agentic future on Windows | Windows Experience Blog"
tags:
   - Model Context Protocol
   - Cybersecurity
   - Agentic Computing
   - Windows 11
   - AI Security
link: https://blogs.windows.com/windowsexperience/2025/05/19/securing-the-model-context-protocol-building-a-safer-agentic-future-on-windows/
date: 2025-07-20
summary: "Microsoft's Model Context Protocol (MCP) aims to standardize secure interactions among AI tools in Windows 11. MCP operates as JSON-RPC over HTTP and introduces roles for hosts, clients, and servers, enabling seamless orchestration of services. Security measures are crucial to mitigate risks like cross-prompt injection and credential leakage. Windows 11 enforces security through a trusted proxy, tool-level authorizations, and a regulated server registry, ensuring user control and adherence to the principle of least privilege. This proactive security architecture is foundational for future developments in AI and agentic computing."
---

[Skip to main content](https://blogs.windows.com/windowsexperience/2025/05/19/securing-the-model-context-protocol-building-a-safer-agentic-future-on-windows/#a11y-skip-link-content)

Skip to main content

[![Site Icon](https://winblogs.thesourcemediaassets.com/sites/2/2021/06/Windows11Icon.png)](https://windows.com/)[/ Windows Experience Blog](https://blogs.windows.com/windowsexperience/2025/05/19/securing-the-model-context-protocol-building-a-safer-agentic-future-on-windows/)

Microsoft Build


May 19, 2025

# Securing the Model Context Protocol: Building a safer agentic future on Windows

By

- [David Weston, Vice President Enterprise and OS Security at Microsoft](https://blogs.windows.com/windowsexperience/author/davidweston/)

As AI agents become more capable and integrated into daily workflows, the need for secure, standardized communication between tools and agents has never been greater. At Microsoft Build 2025, we’re announcing an early preview of how Windows 11 is embracing the Model Context Protocol (MCP) as a foundational layer for secure, interoperable agentic computing — and how we’re securing it from the ground up.

### What is MCP?

MCP is a lightweight, open protocol — essentially JSON-RPC over HTTP — that allows agents and applications to discover and invoke tools in a standardized way. It enables seamless orchestration across local and remote services, allowing developers to build once and integrate everywhere.

MCP defines three roles:

- **MCP Hosts**: Applications like VS Code, or other AI tools that want to access capabilities via MCP.

- **MCP Clients**: Clients that initiate requests to MCP servers.

- **MCP Servers**: Lightweight services that expose specific capabilities (e.g., file system access, semantic search, app actions) through the MCP interface.

Windows 11 will support developers building intelligent applications that want to use MCP and generative AI capabilities to build applications centered around generative AI and intelligence which can leverage MCP where appropriate to take actions on behalf of the user. We will provide an early preview of the MCP platform capabilities to developers in the coming months for the purposes of feedback.

### Why security matters

MCP opens up powerful new possibilities — but also introduces new risks. Without strong controls, an MCP server, for example, could expose sensitive functionality, be misconfigured to allow remote access, or be exploited through many means of attacks including new forms such as prompt injection or tool poisoning. From a security perspective, the input and training data for an LLM are considered untrusted. In addition, cross-prompt injection can enable attackers to include untrusted prompt data and complete a [confused deputy](https://en.wikipedia.org/wiki/Confused_deputy_problem) attack. In the case of a simple chat app, the implications of a prompt injection could be a jailbreak or leakage of memory data, with MCP the implications could be full remote code execution — the highest severity attack.

We’ve used internal and external security research to identify several emerging threat vectors that need to be accounted for in a secure agentic architecture:

- **Cross-Prompt Injection (XPIA):** Malicious content embedded in UI elements or documents can override agent instructions, leading to unintended actions like data exfiltration or malware installation.

- **Authentication Gaps**: MCP’s current standards for authentication are new and inconsistently adopted. OAuth is optional, and ad-hoc approaches are emerging.

- **Credential Leakage:** Agents running with full user privileges risk exposing sensitive tokens or credentials.

- **Tool Poisoning:** Unvetted or low-quality MCP servers may expose dangerous functionality or be used to escalate privileges.

- **Lack of Containment:** Without isolation, a compromised agent can affect the entire user session or system.

- **Limited Security Review**: Many servers are rapidly developed with minimal security review, increasing the risk of vulnerabilities.

- **Registry and MCP Supply Chain Risks**: Without vetting, a public registry of MCP servers could become a vector for malware or abuse.

- **Command Injection**: Improperly validated inputs in the MCP server can lead to arbitrary command execution.

The MCP standard and AI related security is a fast-moving field of research. The goal for Windows 11 as an agentic OS is to provide the strongest fundamental security capabilities while also evolving and adapting to emerging threats.

### MCP security architecture in Windows 11

In line with Microsoft’s [Secure Future Initiative](https://www.microsoft.com/en-us/trust-center/security/secure-future-initiative?msockid=33ce0b4d7a5a6d9e3df01ed27bd96c23) commitment, security is our top priority as we expand MCP capabilities. The MCP Security Architecture in Windows 11 provides fundamental security capabilities based on the following principles:

1. Provide a baseline set of security requirements that all MCP server developers must meet to help ensure user safety.
   - Windows 11 seeks to provide an open and diverse ecosystem of servers while keeping user security as the top priority. This means ensuring each server meets security requirements (more information on this below), has a unique identity, and code is signed to enable provenance validation and revocation when necessary.
2. The user is in control for all security sensitive operations done on their behalf.
   - When agents work on behalf of the user, their scope and operations must be transparent to the user, and sensitive operations such as modifications to the state of the operating system, data and credential access must be surfaced. All sensitive actions done on behalf of the user must be auditable and transparent.
3. Principle of least privilege must be enforced to contain the impact of any possible attack on an MCP server.
   - Windows 11 enforces declarative capabilities and isolation (where applicable) for servers to limit the blast radius and impact of attacks on MCP.

### MCP security controls

To make good on these promises, Windows 11 will provide the following security controls:

- **Proxy-Mediated Communication:** All MCP client-server interactions are routed through a trusted Windows proxy, enabling centralized enforcement of policies and consent. This includes the ability to enforce authentication and authorization in a centralized and consistent manner addressing one of the top challenges with the MCP protocol. This also enables transparent auditing of all on-behalf-of operations and provides a central point where security solutions can observe and respond to potential attacks.

- **Tool-Level Authorization:** Users must explicitly approve each client-tool pair, with support for per-resource granularity helping to fulfil the principle of keeping user in control.

- **Central Server Registry:** Only MCP servers which meet a baseline security criteria will be available in the Windows Registry, ensuring discoverability without compromising trust.

- **Runtime Isolation:** MCP servers’ requirement will implement the principle of least privilege enforced through mechanisms such as isolation and granular permissions. This will put the user in control of what privileges are granted to an MCP server through a declarative model and limit the “blast radius” of any potential attack on a specific MCP server.

### MCP Server security requirements

MCP Servers will be required to meet a baseline series of security requirements in order to appear in the Windows 11 MCP server registry which includes:

1. Mandatory code signing to establish provenance and enable revocation
2. Servers’ definition of tools cannot be changed at runtime
3. Security testing of exposed interfaces
4. Mandatory package identity
5. Servers must declare privileges they require

These will prevent classes of attack like tool poisoning while also creating an open and diverse ecosystem of MCP servers. More information on these requirements will be available when the developer preview is released. These requirements are subject to change as we learn more through the preview.

### Developer preview

Microsoft will provide an early private preview of the MCP server capability post-Microsoft Build to developers only for the purposes of feedback. This private preview may include security capabilities that are not in enforcement mode during the private preview period which will enabled before broad availability. Microsoft will provide this private preview to developers and require that devices be in developer mode to ensure only developers with entitlement can leverage it. Secure-by-default enforcement will be part of the overall release to customers.

### Looking ahead

Security is not a one-time feature — it’s a continuous commitment. As we expand MCP and other agentic capabilities, we will continue to evolve our defenses. From prompt isolation and dual-LLM validation to runtime policy enforcement and firewall plugins, our roadmap is designed to stay ahead of the threat curve.  We are also working with others in the ecosystem such as Anthropic and the MCP Steering Committee to help MCP to meet increasing security needs with continued agentic innovation. For more information, see: [Microsoft Build 2025: The age of AI agents and building the open agentic web](https://aka.ms/AAvchhm).

At Microsoft, we believe that trust is the foundation of innovation. By building security into the core of our agentic platform, the future of AI on Windows is not just powerful — but safe.
