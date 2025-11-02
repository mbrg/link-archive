---
date: '2025-11-02'
description: 'Meta introduces the "Agents Rule of Two" to enhance AI agent security,
  particularly against prompt injection vulnerabilities. This framework allows AI
  agents to only satisfy two out of three properties in a session: processing untrustworthy
  inputs, accessing sensitive data, or communicating externally. This minimizes risks
  such as unauthorized data exfiltration or harmful actions. The strategy emphasizes
  a balance between functionality and security, requiring human oversight for actions
  needing all three properties. As agents gain more capabilities, developers must
  adapt this framework to ensure safety while fulfilling user needs, highlighting
  an evolving landscape in AI security.'
link: /archive/2025-11-01-agents-rule-of-two-a-practical-approach-to-ai-agent-security
tags:
- Meta AI
- Prompt Injection
- AI Security
- Agent Frameworks
- Software Security
- weblog
title: 'Agents Rule of Two: A Practical Approach to AI Agent Security'
type: weblog
---

Hard boundaries becoming popular!

---

> Prompt injection is a fundamental, unsolved weakness in all LLMs. With prompt injection, certain types of untrustworthy strings or pieces of data — when passed into an AI agent’s context window — can cause unintended consequences, such as ignoring the instructions and safety guidelines provided by the developer or executing unauthorized tasks. This vulnerability could be enough for an attacker to take control of the agent and cause harm to the AI agent’s user.

Great to see this written out explicitly. Just a few months ago labs and app devs were still trying to say that prompt injection can be fixed. Some at Anthropic and OAI still do.

---

> Inspired by the similarly named policy [developed for Chromium](https://chromium.googlesource.com/chromium/src/+/main/docs/security/rule-of-2.md), as well as [Simon Willison’s “lethal trifecta,](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) [”](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) our framework aims to help developers understand and navigate the tradeoffs that exist today with these new powerful agent frameworks.

I like this name and the analog to Chromium's rule of two. It's more down to earth than Lethal Trifecta.

---

> **\[C\]** An agent can change state or communicate externally

Does this include the agent's internal state? Or just any mutative action? I guess the latter. But the former would be crucial moving forward with agents that have a persistent scratch pad.

---

> - **\[A\]** The agent has access to untrusted data (spam emails) - **\[B\]** The agent can access a user’s private data (inbox) - **\[C\]** The agent can communicate externally (through sending new emails)

Here lies the BIG problem: how do you distinguish spam emails (untrusted data) from private emails (sensitive data)? 

---

> - This is a public-facing travel assistant that can answer questions and act on a user’s behalf. - It needs to search the web to get up-to-date information about travel destinations \[A\] and has access to a user’s private info to enable booking and purchasing experiences \[B\]. - To satisfy the Agents Rule of Two, we place preventative controls on its tools and communication \[C\] by: - Requesting a human confirmation of any action, like making a reservation or paying a deposit - Limiting web requests to URLs exclusively returned from trusted sources like not visiting URLs constructed by the agent

This is cool. Instead of blocking the "third leg" as suggest by Simon Willison's Lethal Trifecta, the authors here suggest limiting the input parameter space.

---

> - This agent can interact with a web browser to perform research on a user’s behalf. - It needs to fill out forms and send a larger number of requests to arbitrary URLs \[C\] and must process the results \[A\] to replan as needed. - To satisfy the Agents Rule of Two, we place preventative controls around its access to sensitive systems and private data \[B\] by: - Running the browser in a restrictive sandbox without preloaded session data - Limiting the agent’s access to private information (beyond the initial prompt) and informing the user of how their data might be shared

Cool mitigation for browser agents (removing session data)

---

> - This agent can solve engineering problems by generating and executing code across an organization’s internal infrastructure. - To solve meaningful problems, it must have access to a subset of production systems \[B\] and have the ability to make stateful changes to these systems \[C\]. While human-in-the-loop can be a valuable defense-in-depth, developers aim to unlock operation at scale by minimizing human interventions. - To satisfy the Agents Rule of Two, we place preventive controls around any sources of untrustworthy data \[A\] by: - Using author-lineage to filter all data sources processed within the agent’s context window - Providing a human-review process for marking false positives and enabling agents access to data

Author lineage as a way to filter out untrusted data from code sounds very difficult. Most commits aren't signed anyways.

