---
date: '2025-09-12'
description: Trail of Bits has launched the beta version of [`mcp-context-protector`](https://github.com/trailofbits/mcp-context-protector)
  to enhance security in LLM applications leveraging the Model Context Protocol (MCP).
  The tool addresses vulnerabilities such as line jumping and prompt injection attacks
  by employing trust-on-first-use server pinning, LLM guardrail integration for response
  verification, and ANSI character sanitization. Functioning as a wrapper between
  LLM apps and MCP servers, it ensures compatibility without requiring upstream modifications.
  While it improves upon security, it mandates manual configuration reviews, raising
  potential alert fatigue concerns. Feedback is encouraged via their GitHub repository.
link: /archive/2025-09-05-we-built-the-security-layer-mcp-always-needed-the-trail-of-bits-blog
tags:
- mcp-context-protector
- prompt-injection
- security-wrappers
- LLM-security
- ANSI-sanitization
- weblog
title: We built the security layer MCP always needed -The Trail of Bits Blog
type: weblog
---

Cool OSS implementation of an MCP security gateway.

I have two concerns with this approach.

1. Devs need to configure MCP through your tool rather than the environment they are already using. So they can't leverage the inevitable MCP stores that Claude, ChatGPT, Cursor and others and creating and are bound to continue to invest in.

2. Chaining MCP gateways isn't really feasible, which means dev can only have one gateway. Would they really choose one that only provides security guarantees? What about observability, tracing, caching? I think devs are much more likely to use an MCP gateway with security features than an MCP security gateway. Just like they did with API gateways.

---

> If the downstream server’s configuration ever changes, such as by the addition of a new tool, a change to a tool’s description, or a change to the server instructions, each modified field is a new potential prompt injection vector. Thus, when `mcp-context-protector` detects a configuration change, it blocks access to any features that the user has not manually pre-approved. Specifically, if a new tool is introduced, or the description or parameters to a tool have been changed, that tool is blocked and never sent to the downstream LLM app. If the server’s instructions change, the entire server is blocked. That way, it is impossible for an MCP server configuration change to introduce new text (and, therefore, new prompt injection attacks) into the LLM’s context window without a manual approval step.

That's cool, but isn't comprehensive. Injections could easily be introduced dynamically at runtime via tool results. Scanning tool definitions even dynamically is not enough. Edit: these are covered on a separate module.

---

> As [one of our recent posts on MCP](https://blog.trailofbits.com/2025/04/29/deceiving-users-with-ansi-terminal-codes-in-mcp/) discussed, ANSI control characters can be used to conceal prompt injection attacks and otherwise obfuscate malicious output that is displayed in a terminal. Users of Claude Code and other shell-based LLM apps can turn on `mcp-context-protector`’s ANSI control character sanitization feature. Instead of stripping out ANSI control sequences, this feature replaces the escape character (a byte with the hex value `1b`) with the ASCII string `ESC`. That way, the output is rendered harmless, but visible. This feature is turned on automatically when a user is reviewing a server configuration through the CLI app:

Love this. Default on policy that has little to no operational downside but a lot of security upside.

---

> There is one conspicuous downside to using MCP itself to insert `mcp-context-protector` between an LLM app and an MCP server: `mcp-context-protector` does not have full access to the conversation history, so it cannot use that data in deciding whether a tool call is safe or aligns with the user’s intentions. An example of an AI guardrail that performs exactly that type of analysis is AlignmentCheck, which is integrated into LlamaFirewall. AlignmentCheck uses a fine-tuned model to evaluate the entire message history of an agentic workflow for signs that the agent has deviated from the user’s stated objectives. If a misalignment is detected, the workflow can be aborted.

More than being blind to intent breaking, this limitation also means that you can't dynamically adjust defenses based on existing context. For example, change AI firewall thresholds if the context has sensitive data.
It's really cool of Trail Of Bits to state this limitation clearly.

---

> Since `mcp-context-protector` is itself an MCP server, by design, it lacks the information necessary to holistically evaluate an entire chain of thought, and it cannot leverage AlignmentCheck. Admittedly, we demonstrated in [the second post in this series](https://blog.trailofbits.com/2025/04/23/how-mcp-servers-can-steal-your-conversation-history/) that malicious MCP servers _can_ steal a user’s conversation history. But it is a bad idea in principle to build security controls that intentionally breach other security controls. We don’t recommend writing MCP tools that rely on the LLM disclosing the user’s conversation history in spite of [the protocol’s admonitions](https://modelcontextprotocol.io/specification/2025-03-26/architecture#design-principles).

It's an MCP gateway.

