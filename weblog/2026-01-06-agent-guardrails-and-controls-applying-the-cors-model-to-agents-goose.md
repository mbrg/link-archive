---
date: '2026-01-06'
description: This article presents a novel approach to mitigate content injection
  vulnerabilities in Large Language Models (LLMs) leveraging insights from browser
  security, specifically Cross-Site Request Forgery (CSRF) protections. It proposes
  adopting a verification mechanism akin to CORS to ensure tool executions are authorized
  and originate from valid user interactions. Key strategies include tracking tool
  invocation history and flushing tool output from the context window between user
  prompts to reduce exploitation risks. While the framework offers substantial improvements
  over existing security measures, it emphasizes the reliance on trusted agent codebases
  and acknowledges limitations regarding second-order injection attacks.
link: /archive/2026-01-06-agent-guardrails-and-controls-applying-the-cors-model-to-agents-goose
tags:
- LLM Security
- Cross-Site Request Forgery (CSRF)
- Model Context Protocol (MCP)
- CORS Mitigations
- Content Injection
- weblog
title: "Agent Guardrails and Controls: Applying the CORS Model to Agents \u25C6 goose"
type: weblog
---

---

> To handle these threats we propose **removing** **all tool-call responses from the context window in-between user turns**. This significantly increases the difficulty of performing “inter-turn” manipulation at the cost of occasionally forcing it to re-run tool-calls if it requires more precise historical values.

This is new (to me). The reduction of tool outputs on the next user turn.. is this feasible? i mean, it kills state cache so its very costly.

