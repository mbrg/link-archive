---
date: '2025-11-08'
description: "Anthropic's latest blog post details the implementation of the Model\
  \ Context Protocol (MCP) to enhance AI agent efficiency through code execution.\
  \ By allowing agents to treat MCP servers as code APIs, developers can avoid excessive\
  \ token consumption tied to direct tool calls and overload on context windows. This\
  \ approach utilizes filesystem-like navigation to dynamically load only necessary\
  \ tools and process results in code, resulting in significant reductions in token\
  \ count\u2014up to 98.7% in some cases. Additionally, this method facilitates better\
  \ state persistence, data privacy, and effective use of advanced control flows,\
  \ though it requires secure execution environments to manage complexity and safeguard\
  \ operational integrity."
link: /archive/2025-11-08-code-execution-with-mcp-building-more-efficient-ai-agents-anthropic
tags:
- AI Agents
- Token Management
- Efficient APIs
- Code Execution
- MCP
- weblog
title: 'Code execution with MCP: building more efficient AI agents \ Anthropic'
type: weblog
---

MCP requires agents to manipulate data. But at scale LLMs are lossy data manipulators. Code is great at copying data and mutating it with precision.

This is great real-world engineering around LLMs. I wish they would take it a step further. When LLMs write their own tools (out if provided building blocks), why do we immediately need to let them execute them? Instead, new tools can go through review. Approved tools can be used however they want (under boundaries). I do wonder what this does to caching. And if it is applicable to simple 2-3 tool call agents, which are the most prolific.

---

> Today developers routinely build agents with access to hundreds or thousands of tools across dozens of MCP servers. However, as the number of connected tools grows, loading all tool definitions upfront and passing intermediate results through the context window slows down agents and increases costs.

These numbers are crazy. They represent cutting edge agents, not the 99% of simple agents being built in the enterprise. This feels like a very biased view towards these apex agents.

---

> Every intermediate result must pass through the model. In this example, the full call transcript flows through twice. For a 2-hour sales meeting, that could mean processing an additional 50,000 tokens. Even larger documents may exceed context window limits, breaking the workflow.

If you need to pass 50k tokens from one tool to another this is definitely work for deterministic code not a generative model.

---

> With code execution environments becoming more common for agents, a solution is to present MCP servers as code APIs rather than direct tool calls. The agent can then write code to interact with MCP servers. This approach addresses both challenges: agents can load only the tools they need and process data in the execution environment before passing results back to the model.

Essentially: force the model to commit to how it would process the results. Instead of putting results in context and just figuring out the next step on the fly. We should distinguish between data the model needs to manipulate (with code, out of context) and data it needs to analyze (with llm, within context).

---

> The agent discovers tools by exploring the filesystem: listing the `./servers/`directory to find available servers (like `google-drive` and `salesforce`), then reading the specific tool files it needs (like `getDocument.ts` and `updateRecord.ts`) to understand each tool's interface. This lets the agent load only the definitions it needs for the current task. This reduces the token usage from 150,000 tokens to 2,000 tokens—a time and cost saving of 98.7% **.**

Another benefit is that this equates tool call with code understanding which is something the labs are pushing real strong for, for obvious reasons.

---

> Code execution with MCP enables agents to use context more efficiently by loading tools on demand, filtering data before it reaches the model, and executing complex logic in a single step. There are also security and state management benefits to using this approach.

This is great. BUT: we are losing the cached checkpoint with all tools loaded up. 

---

> Loops, conditionals, and error handling can be done with familiar code patterns rather than chaining individual tool calls. For example, if you need a deployment notification in Slack, the agent can write:

This requires strong tests/compiler to catch and hint at programming mistakes early.

---

> Then, when the data is shared in another MCP tool call, it is untokenized via a lookup in the MCP client. The real email addresses, phone numbers, and names flow from Google Sheets to Salesforce, but never through the model. This prevents the agent from accidentally logging or processing sensitive data. You can also use this to define deterministic security rules, choosing where data can flow to and from.

Huge benefit. This introduces a hard boundary where injections can't get to the actual sensitive content.

---

> Code execution with filesystem access allows agents to maintain state across operations. Agents can write intermediate results to files, enabling them to resume work and track progress:

It also allows us to review these "generated tool compositions" for security vulns.

