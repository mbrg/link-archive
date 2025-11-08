---
date: '2025-11-08'
description: Thomas Ptacek's exploration of LLM agents emphasizes their straightforward
  implementation and potential for innovation in computing. He highlights how the
  simplicity of coding an agent (using minimal code to interface with the OpenAI API)
  can lead to surprising functionalities, such as multi-personality responses and
  tool interactions. The piece also critiques the reliance on MCP for agent functionality,
  suggesting that security and agent architecture can be improved through thoughtful
  context engineering. Ptacek encourages experimentation, noting that designing agents
  opens avenues for solving significant problems within security and software engineering.
link: /archive/2025-11-07-you-should-write-an-agent-the-fly-blog
tags:
- vulnerability assessment
- Python programming
- LLM agents
- context engineering
- OpenAI API
- weblog
title: "You Should Write An Agent \xB7 The Fly Blog"
type: weblog
---

Write your own coding agent. It isn't that big of a lift (yet).

---

> You can see now how hyperfixated people are on Claude Code and Cursor. They’re fine, even good. But here’s the thing: you couldn’t replicate Claude Sonnet 4.5 on your own. Claude Code, though? The TUI agent? Completely in your grasp. Build your own light saber. Give it 19 spinning blades if you like. And stop using [coding agents as database clients](https://simonwillison.net/2025/Aug/9/ "").

Strongly agree with this point. Coding agents are at the point where a single person can still understand everything important about how they are built. This won't be the case in the future. Now is the time to build your own coding agent, to understand the tools of the (new) eng craft.

---

> When you read a security horror story about MCP your first question should be why MCP showed up at all. By helping you dragoon a naive, single-context-window coding agent into doing customer service queries, MCP saved you a couple dozen lines of code, tops, while robbing you of any ability to finesse your agent architecture.

MCP helps labs turn general purpose assistants into customized agents. On the fly. It wasn't designed for *your* agent.

---

> You don’t know what works best until you try to write the agent.

This is an important point. Tests with agents aren't coding tests. They are data science tests--evals.

