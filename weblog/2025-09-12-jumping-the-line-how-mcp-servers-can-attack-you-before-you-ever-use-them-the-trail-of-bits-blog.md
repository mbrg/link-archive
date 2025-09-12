---
date: '2025-09-12'
description: This article presents a critical vulnerability in the Model Context Protocol
  (MCP), termed "line jumping," which enables malicious servers to manipulate models
  without explicit tool invocation. This circumvents MCP's security promises, such
  as invocation controls and connection isolation, exposing clients to threats like
  code exfiltration and vulnerability insertion. The authors recommend immediate defensive
  measures, including vetting sources, implementing automated scans, and disabling
  unnecessary MCP servers. The vulnerability highlights significant architectural
  flaws in MCP, necessitating heightened awareness and caution as this protocol evolves.
link: /archive/2025-09-12-jumping-the-line-how-mcp-servers-can-attack-you-before-you-ever-use-them-the-trail-of-bits-blog
tags:
- Prompt Injection
- MCP Security
- Line Jumping
- Vulnerability
- AI Security
- weblog
title: 'Jumping the line: How MCP servers can attack you before you ever use them
  -The Trail of Bits Blog'
type: weblog
---

Don't let others decide what goes into YOUR system instructions. That includes your MCP servers. 
Trail Of Bits have a unique style in the AI security blogs. Feels very structured and methodological.

---

> Let’s cut to the chase: MCP servers can manipulate model behavior _without ever being invoked_. This attack vector, which we call “line jumping” and [other researchers have called tool poisoning](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks), fundamentally undermines MCP’s core security principles.

I don't get the name "line jumping". This seems to hint at line breakers, but that's just one technique in which tool descriptions can introduce instructions. Which lines are we jumping?
Tool poisoning or description poisoning seem easier and more intuitive.

---

> When a client application connects to an MCP server, it must ask the server what tools it offers via the `tools/list` method. The server responds with tool descriptions that the client adds to the model’s context to let it know what tools are available.

Even worse. Tool descriptions are typically placed right into the system instructions. So they can easily manipulate LLM behavior.


