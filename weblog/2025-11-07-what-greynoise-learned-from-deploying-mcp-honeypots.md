---
date: '2025-11-07'
description: GreyNoise has introduced GreyNoise Block, a customizable real-time blocklist
  service, paralleling their recent deployment of Model Context Protocol (MCP) honeypots.
  The honeypots revealed that no targeted attacks on MCPs occurred, although they
  were quickly discovered by automated scanning. This highlights a current lack of
  deliberate threats but underscores the importance of monitoring baseline traffic
  patterns for anomalies. As advanced attackers leverage AI for operational speed,
  GreyNoise's new tools suggest organizations can enhance defensive capabilities and
  automate threat response. Establishing AI SOCs combining dependable data and AI
  reasoning is crucial to bridge the offense-defense gap.
link: /archive/2025-11-07-what-greynoise-learned-from-deploying-mcp-honeypots
tags:
- GreyNoise
- MCP
- blocklists
- cybersecurity
- AI security
- weblog
title: What GreyNoise Learned from Deploying MCP Honeypots
type: weblog
---

Cool project by GrayNoise. The fact that they didn't find any meaningful scanning shows the immaturity of the AI security market.

---

> To find out, **GreyNoise deployed a series of MCP honeypots to observe what actually happens when AI middleware meets the open internet.**

Great idea

---

> - **Unauthenticated endpoint** to capture background scanning. - **Authenticated endpoint** requiring an API key to detect credential probing. - **Simulated developer instance** with a deliberately exposed key to see whether anyone followed it.

Good coverage. One missing use case is MCP server code published on GitHub.

---

> Across the deployment, **no MCP-specific payload or exploitation attempts appeared.**

Strange they did not observe security vendors running internet-wide scanning. Vendors did publish one-off research pieces. But given the fact that MCP servers are very well positioned for rug pull attacks (instructions are fetched by agents on the fly), these leave plenty of room to hide in.

---

> In October 2025, independent researchers [demonstrated](https://www.theregister.com/2025/10/21/mcp_prompt_hijacking_attack/) a prompt-hijacking flaw in a custom MCP build that used a deprecated protocol handler. It was a contained proof-of-concept, not an attack in the wild — and it supports the same conclusion: present-day MCP exposure risk lies in implementation errors, not in deliberate targeting of MCPs as a class.

Deprecated protocol makes it sound like a patched vulnerability. Plenty of case studies were demonstrated by the hacker community. MCP is literally using prompt injection as a feature..

