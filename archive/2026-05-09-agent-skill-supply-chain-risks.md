---
date: '2026-05-09'
description: The content outlines significant risks associated with Agent Skills,
  modular enhancements for AI agents like Claude. Key insights include the potential
  for deception (e.g., impersonating trusted sources), content manipulation (e.g.,
  code poisoning), and unregulated code execution (e.g., running shell scripts or
  Python code). The risks extend to integration vulnerabilities, allowing malicious
  skills to execute commands upon loading or create persistent hooks for data exfiltration.
  Moreover, evasion tactics like employing unicode or HTML comments may conceal harmful
  intents. Emphasizing trust and source validation is critical to mitigate these threats
  in AI skill deployment.
link: https://ramimac.me/spooky-skills/list/
tags:
- Malware Analysis
- Agent Skills
- Cybersecurity Risks
- Code Execution Vulnerabilities
- AI Security
title: Agent Skill Supply Chain Risks
---

# Agent Skill Supply Chain Risks

19 attack vectors. [See interactive version](https://ramimac.me/spooky-skills/)

[Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) are modular capabilities that extend AI agents. They package instructions, metadata, and code that agents execute automatically when triggered.

**From Anthropic's docs:** "We strongly recommend using Skills only from trusted sources. A malicious Skill can direct Claude to invoke tools or execute code in ways that don't match the Skill's stated purpose."

## Deception

Skills can lie to you.Skill metadata is just a label. The contents are what actually matters.

Skills can impersonate trusted sources.Anyone can claim their skill is "verified" or "official". Enforcement is marketplace specific.

Skills can shadow other skills.Skill names aren't namespaced. A malicious skill can impersonate a legitimate one.

Skills can create fake urgency.Skill content loads into the agent's context. Urgent framing influences how it prioritizes actions.

## Content Poisoning

Skills can poison context with examples.Code examples in skill docs get reproduced by agents. Malicious patterns become "best practices."

## Agent Integration

Skills can create commands.A skill's `name` becomes a slash command. The body controls what happens.

Skills can auto-execute on load.The ``!`command``` syntax executes immediately when a skill loads.

## Code Execution

Skills can run shell scripts.Skills can bundle shell scripts. The agent runs them without seeing the contents.

Skills can run Python code.Skills can embed Python scripts with full system access.

Skills can fetch remote content.Skills can fetch from external URLs. The payload can change after installation.

Skills can pipe to bash.`curl | bash` downloads and executes in one step. No chance to inspect first.

Skills can install packages.Postinstall scripts run automatically with your permissions.

## Hooks & Persistence

Skills can create HTTP hooks.HTTP hooks POST data to external servers on every tool use or session event.

Skills can create command hooks.Command hooks run shell commands before or after every tool use.

Skills can background command hooks.Async hooks fire and forget. No slowdown, no indication data is being sent.

Skills can write to CLAUDE.md.Malicious rules persist across ALL future sessions.

## Evasion

Skills can hide in unicode.Unicode Tag codepoints (U+E0000) are invisible to humans but readable by models.

Skills can hide in HTML comments.HTML comments are stripped from rendered markdown but may still be parsed by the agent.

Skills can hide in subagents.Subagent tool calls aren't shown in your main conversation. You only see the summary.
