---
date: '2025-07-29'
description: Invariant Labs introduces "toxic flow analysis" (TFA) to address prompt
  injection vulnerabilities in AI agent systems and MCP servers. This framework models
  tool flows and predicts security risks, focusing on dynamic attack surfaces inherent
  in AI applications. Current security solutions fall short against these evolving
  threats, necessitating a shift from traditional prompt-level defenses to comprehensive
  flow analysis. TFA is integrated into the MCP-scan tool, offering automation in
  vulnerability detection. As AI systems become more integrated with user workflows,
  TFA's predictive capabilities are crucial for safeguarding against malicious exploitation
  and data exfiltration. [GitHub](https://github.com/invariantlabs-ai/mcp-scan) [Try
  MCP-Scan](https://invariantlabs.ai/blog/toxic-flow-analysis#try)
link: https://invariantlabs.ai/blog/toxic-flow-analysis
tags:
- Dynamic Systems
- Malware Threats
- Prompt Injection
- Security Vulnerabilities
- AI Security
title: Invariant Labs Exposes Novel Prompt Injection Attack Vulnerabilities, “Toxic
  Flows,” in Agentic Systems & MCP Servers
---

#### 2025-07-29

# Invariant Labs Exposes Novel Prompt Injection Attack Vulnerabilities, “Toxic Flows,” in Agentic Systems & MCP Servers

### We present the toxic flow analysis (TFA) framework to detect and mitigate security vulnerabilities in agent systems before they are exploited. Toxic flow analysis is the first principled approach to reduce the attack surface of AI applications, mitigating indirect prompt injections and other MCP attack vectors. We are sharing a preview of toxic flow analysis in our MCP-scan tool.

[GitHub](https://github.com/invariantlabs-ai/mcp-scan) [Try MCP-Scan](https://invariantlabs.ai/blog/toxic-flow-analysis#try)

![](https://invariantlabs.ai/images/toxicflows/tfa-header.svg)

The rise of MCP-enabled AI applications and agent systems has significantly increased the attack surface of AI-powered applications, compared to traditional software systems. Novel kinds of security vulnerabilities first uncovered by Invariant Labs, the research division of Snyk, have enabled prompt-injection-based attacks like the [GitHub MCP exploit](https://invariantlabs.ai/blog/mcp-github-vulnerability) and [tool poisoning attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks), allowing for severe forms of data exfiltration. To date, these vulnerabilities remain largely unmitigated, as existing AI security solutions lack the capabilities to effectively safeguard against them. This puts the users and enterprises relying on AI-powered tools like Cursor, Claude, or ChatGPT at an immense risk of malicious exploitation and data exfiltration.

Current security solutions are unable to mitigate these attacks, as they cannot adapt to the nature of current AI systems like agents that dynamically change their behavior based on user input, the connected data sources, and models. To address this, we showcase a novel security analysis framework designed to detect so-called toxic flows in AI systems. Instead of focusing on just prompt-level security, toxic flow analysis pre-emptively predicts the risk of attacks in an AI system by constructing potential attack scenarios leveraging deep understanding of an AI system’s capabilities and potential for misconfiguration.

## Securing A New Kind Of Software

AI-powered software like the Cursor IDE, Claude Desktop, or ChatGPT can use MCP to connect to tools, allowing them to interact with APIs, services, and databases on behalf of the user.
In contrast to traditional, deterministic software systems, this enables such agents to dynamically adapt and perform user-specific workflows as required. However, it also makes these systems notoriously hard to secure, validate, and test before deployment. After all, any possible combination of available tools may be employed at runtime, making it hard to anticipate all possible security failures and vulnerabilities.

Given a set of tools, to properly secure an agent system, we must thus consider the power set, i.e. all possible combinations of tools, to accurately profile the security risks of the system. The figure below demonstrates this difference. While traditional software allows us to make strong assumptions about the use of data and APIs, AI-powered systems are opaque and less predictable.

![](https://invariantlabs.ai/images/toxicflows/figure-1-traditional%20vs%20agent.svg)**Figure 1.** Traditional software follows predictable execution paths, while agent systems can dynamically combine tools in unpredictable ways, creating a much larger attack surface.

## Agentic Threats

Given this inherently dynamic nature of agent systems, agent security breaches typically occur at runtime: While an agent system may appear safe and benign before deployment, a malicious prompt injection as well as the handling of sensitive data, can create novel security vulnerabilities entirely at runtime. One particular instance of this, is the notion of the so-called [lethal trifecta for AI agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/): If an agent is exposed both to untrusted instructions, sensitive data as well as a way to leak or exfiltrate arbitrary data, attackers can easily exploit the AI system to their advantage.

An example of such an attack was recently demonstrated by the GitHub MCP exploit, where a malicious actor is able to exfiltrate sensitive data from a GitHub repository by injecting a prompt into an AI agent that was able to access the repository. This attack exploited the dynamic nature of agent systems, where the agent's behavior could change based on the input it received, leading to unintended data exposure.

![](https://invariantlabs.ai/images/toxicflows/figure-2-gh-issue.svg)**Figure 2.** A malicious GitHub issue containing prompt injection triggers data exfiltration.

## Securing Flows, not just Prompts and Code

While basic prompt security solutions (e.g. LLM firewalls) as well as secure implementation of agent systems (e.g. code scanning) are relevant, we need to look further if we are serious about truly mitigating agentic AI vulnerabilities.

To do so, toxic flow analysis (TFA) first instantiates the flow graph of an agent system, modelling all tool flows, i.e. the potential sequences of tool uses together with relevant properties like the level of trust, sensitiveness or e.g. whether a tool could be used as an exfiltration sink. Based on this graph, TFA can then instantiate and score potential toxic flows, i.e. tool sequences that would lead to security violations at runtime, as illustrated below.

This automatically uncovers and notifies users about attack vectors. It can detect and warn about lethal-trifectas scenarios like the recent GitHub MCP exploit and other potential
vulnerabilities in your agent systems.

TFA is a hybrid security analysis framework, which can incorporate both static information about an agent system, its toolsets, and MCP servers, as well as dynamic runtime data, captured while monitoring agents in production.

![](https://invariantlabs.ai/images/toxicflows/figure-3-flow-to-toxic.svg)**Figure 3.** Toxic Flow Analysis analyzes agent tool flows to identify toxic flows that could lead to security vulnerabilities.

## Toxic Flow Analysis in Action

Today, we are releasing an early preview of toxic flow analysis as part of the MCP-scan security scanning tool, which allows you to analyze your agent systems for potential toxic flows. The tool automatically identifies potential toxic flows in the agent systems on your machine by scanning MCP servers and toolsets installed in your environment (e.g. Cursor IDE, ChatGPT, Claude Desktop, etc.).

To use MCP-scan, run the following command (requires [uv to be installed](https://docs.astral.sh/uv/#highlights)):

```
  Copyuvx mcp-scan@latest

```

This will automatically run the MCP-scan tool and analyze AI-powered applications like Cursor and Claude Desktop for potential toxic flows. The tool will provide you with a report of any potential vulnerabilities it finds, allowing you to take action to mitigate them:

![](https://invariantlabs.ai/images/toxicflows/mcp-scan-tfa-silent-short.gif)

## Conclusion

Toxic flow analysis is a powerful new framework for securing AI agent systems, allowing developers to proactively identify and mitigate security vulnerabilities before they can be exploited. By modeling the flow of data and tool usage in agent systems, TFA can uncover potential attack vectors and help developers build more secure AI applications.

Want to learn more? Please attend Snyk’s webinar on Monday, August 18, at noon ET. See [registration details here](https://go.snyk.io/the-future-of-agentic-ai-security.html).

Authors:

Luca Beurer-Kellner

Marco Milanta

Marc Fischer

[See all blog posts →](https://invariantlabs.ai/blog)
