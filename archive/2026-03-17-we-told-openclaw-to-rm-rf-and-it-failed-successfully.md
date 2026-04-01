---
date: '2026-03-17'
description: Sondera's extension for OpenClaw introduces "policy as code" guardrails,
  enhancing security for AI agents with tool access. This solution enforces predefined
  rules, preventing destructive commands like `rm -rf` and unauthorized access to
  sensitive data, including AWS credentials. Utilizing Cedar language for policy definition,
  the system ensures consistent and auditable enforcement of permissions. The extension
  intercepts tool calls pre- and post-execution, providing structured feedback on
  blocked actions. This deterministic approach mitigates risks inherent in prompt-based
  compliance, positioning agents for safer and more effective operation in production
  environments.
link: https://blog.sondera.ai/p/openclaw-rm-rf-policy-as-code
tags:
- AI Safety
- Guardrails
- Policy as Code
- Cedar Policy Language
- OpenClaw
title: We Told OpenClaw to rm -rf and It Failed Successfully
---

[![Secure Trajectories by Sondera](https://substackcdn.com/image/fetch/$s_!Xvym!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2836c431-33d7-4987-a9a0-91fd619ed98c_1000x1000.png)](https://blog.sondera.ai/)

# [Secure Trajectories by Sondera](https://blog.sondera.ai/)

SubscribeSign in

![User's avatar](https://substackcdn.com/image/fetch/$s_!g1FG!,w_64,h_64,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F53e4a43b-ed02-4d69-b364-c4f05b3c082c_1117x1117.jpeg)

Discover more from Secure Trajectories by Sondera

The Sondera team’s research and analysis on the systems and mechanics of agent control.

Subscribe

By subscribing, you agree Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

Already have an account? Sign in

# We Told OpenClaw to rm -rf and It Failed Successfully

### Policy as code guardrails for AI agents

[![Josh Devon's avatar](https://substackcdn.com/image/fetch/$s_!g1FG!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F53e4a43b-ed02-4d69-b364-c4f05b3c082c_1117x1117.jpeg)](https://substack.com/@joshdevon)

[Josh Devon](https://substack.com/@joshdevon)

Feb 03, 2026

17

2

5

Share

[![](https://substackcdn.com/image/fetch/$s_!jiGs!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5be23339-eecd-436c-9fa0-621b495e8fbe_1280x720.gif)](https://substackcdn.com/image/fetch/$s_!jiGs!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5be23339-eecd-436c-9fa0-621b495e8fbe_1280x720.gif)

**[OpenClaw](https://openclaw.ai/)** is an open-source personal AI assistant with over 160,000 [GitHub](https://github.com/openclaw/openclaw) stars. Full tool access: bash, browser control, file system, arbitrary API calls. It’s an “AI that actually does things.” It also has what Simon Willison calls the **[lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)**: tool access, sensitive data, autonomous execution. **The risk and the utility come from the same source.**

One response to this risk has been sandboxing. [Trail of Bits](https://github.com/trailofbits/claude-code-devcontainer) released an isolation framework. [Cloudflare built Moltworker](https://github.com/cloudflare/Moltworker). Sandboxes are an important foundation, but alone they force a binary choice: total restriction or total access. An agent in a full sandbox can’t help with your actual projects unless you mount them in, and then you’re back to worrying about what it can do.

We built a different approach. The **Sondera extension** adds policy as code guardrails to OpenClaw. Instead of blocking all tool access, it governs what the agent can actually do. The agent can run bash, but not `sudo`. It can read files, but not `~/.aws/credentials`. It can execute commands, but not `rm -rf`. Define what’s allowed. The rules enforce it every time.

**Ready to try it?** Check out the [installation guide](https://docs.sondera.ai/integrations/openclaw/) or the [GitHub repo](https://github.com/sondera-ai/openclaw/tree/sondera-pr/extensions/sondera).

## **From Polite Requests to Hard Rules**

System prompts are **polite requests**. You can tell an agent “never run `sudo` commands” and hope it complies, but you are relying on probabilistic compliance from a system designed to be helpful. The agent might decide that `sudo` is necessary to complete your task. The agent might be manipulated through prompt injection. The agent might simply hallucinate that you gave permission.

**Policy as code** is a different approach. Instead of asking the agent to follow rules, you define rules that the infrastructure enforces. The agent doesn’t get to decide whether to comply. [Cedar](https://www.cedarpolicy.com/) is the policy language we use, developed by AWS and battle-tested at scale through Amazon Verified Permissions.

**Cedar policies are hard blocks.** When a tool call violates a policy, the infrastructure intercepts it before execution. Same input, same verdict, every time. These are **deterministic lanes**: defined boundaries that the agent can’t cross regardless of its reasoning.

Cedar is designed for authorization decisions. The syntax is declarative and readable by humans, not just machines. Evaluation is deterministic. And like any code, policies are auditable, versionable, and testable.

For OpenClaw users, the goal is to grant your agent real capabilities without constant supervision. Define what’s allowed once, and the policies check every tool call.

## **The Sondera Extension for OpenClaw**

The extension intercepts every tool call at two stages:

- **PRE\_TOOL:** Evaluates policies before execution. Blocked actions never run.

- **POST\_TOOL:** Inspects results after execution. Sensitive data is redacted from the transcript.


When a tool call is blocked, the agent receives structured feedback: `"Blocked by Sondera policy (sondera-block-rm)"`. The agent sees why it was blocked rather than failing opaquely. Be aware that OpenClaw may retry with alternative approaches, sometimes finding creative workarounds like using `find -delete` or `mv` to trash instead of `rm`. The policy packs include overlapping rules to catch common alternatives.

### **Policy Packs**

The extension comes with built-in policy packs to experiment with. You can toggle them on or off, add your own custom rules, or create your own policy pack. To learn more about reading and writing policies, see the [writing policies guide](https://docs.sondera.ai/writing-policies/).

Sondera Extension OpenClaw Policy Packs

### Sondera Extension OpenClaw Policy Packs

| Pack | **Sondera Base Pack** |
| Rules | 41 |
| Purpose | Core protections: sudo, rm, credentials, config files |
|  |
| Pack | **OpenClaw System Protection** |
| Rules | 24 |
| Purpose | Protect SOUL.md, extension configs, system prompts |
|  |
| Pack | **OWASP Agentic Pack** |
| Rules | 38 |
| Purpose | OWASP Top 10 for Agentic Applications controls |
|  |
| Pack | **Lockdown Mode** |
| Rules | — |
| Purpose | Deny-all tool calling with explicit allowlisting |

| Pack | Rules | Purpose |
| --- | --- | --- |
| **Sondera Base Pack** | 41 | Core protections: sudo, rm, credentials, config files |
| **OpenClaw System Protection** | 24 | Protect SOUL.md, extension configs, system prompts |
| **OWASP Agentic Pack** | 38 | OWASP Top 10 for Agentic Applications controls |
| **Lockdown Mode** | — | Deny-all tool calling with explicit allowlisting |

Table with 3 columns and 4 rows. (column headers with buttons are sortable)

[Embed](https://datawrapper.dwcdn.net/O820b/2/#embed) Created with [Datawrapper](https://www.datawrapper.de/_/O820b)

These packs can be combined and customized. The Base Pack provides sensible defaults. The OWASP Agentic Pack maps directly to the control recommendations in the framework. Lockdown Mode inverts the model entirely: deny all tool calls by default, then add permit rules for specific tools you want to allow. This default-deny pattern gives you maximum control over exactly what the agent can do. See the [full policy reference](https://docs.sondera.ai/integrations/openclaw-policies/) for details on every rule.

[![](https://substackcdn.com/image/fetch/$s_!TqUU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3605e38e-edf8-4bc6-842d-a7d812a443a2_1376x2540.png)](https://substackcdn.com/image/fetch/$s_!TqUU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3605e38e-edf8-4bc6-842d-a7d812a443a2_1376x2540.png) Configuration panel for the Sondera extension showing policy pack toggles

Subscribe

## **Policy Enforcement in Action**

### **Blocking Privilege Escalation**

`sudo` commands let users execute operations with root privileges. An agent with `sudo` access can install packages, modify system files, create users, or disable security controls. A prompt telling the agent “never use `sudo`“ is a suggestion. Fine-tuning and training are also suggestions. The agent might decide `sudo` is necessary to complete your task, or an attacker might inject instructions that override the original guidance. Prompt-based guardrails fail because they operate at the same layer as the attack.

Here’s what happens when OpenClaw tries to run `sudo` with Sondera enabled:

[![](https://substackcdn.com/image/fetch/$s_!r3gc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a421ac7-c005-45b8-beec-a34d6a1709f7_2082x2546.png)](https://substackcdn.com/image/fetch/$s_!r3gc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a421ac7-c005-45b8-beec-a34d6a1709f7_2082x2546.png) Sudo command blocked by policy sondera-block-sudo

The command was blocked before it could execute. OpenClaw received the message `"Blocked by Sondera policy (sondera-block-sudo)"` and told the user: _“I can’t run_`sudo` _commands. It’s a security thing. I can run regular commands for you, though.”_

Here’s the policy that made this happen:

```
// Policy: sondera-block-sudo
@id("sondera-block-sudo")
forbid(principal, action, resource)
when {
  action == Sondera::Action::"exec" &&
  context has params && context.params has command &&
  context.params.command like "*sudo *"
};
```

The policy checks every `exec` action (bash commands) and blocks any command containing `sudo`. The `like "*sudo *"` pattern matches `sudo` followed by a space anywhere in the command string. The trailing space avoids false positives on words like `pseudocode`. No prompt needed. No training required. The infrastructure enforces the rule.

### **Blocking Destructive Commands**

The `rm -rf` command recursively deletes files without confirmation. One misplaced path and your codebase, documents, or entire home directory is gone. Agents can hallucinate paths, misinterpret instructions, or be manipulated into cleanup operations that destroy data. Prompt guardrails fail here because the agent genuinely believes it is following instructions. The reasoning that led to the destructive command looks legitimate from inside the model.

Here’s what happens when OpenClaw tries to run `rm -rf` with Sondera enabled:

[![](https://substackcdn.com/image/fetch/$s_!5aDq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F63b5caca-6c09-4e62-9f3f-68fb1d558269_2082x2546.png)](https://substackcdn.com/image/fetch/$s_!5aDq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F63b5caca-6c09-4e62-9f3f-68fb1d558269_2082x2546.png) Destructive rm command blocked by policies sondera-block-rm and sondera-block-rf-flags

The command was blocked before it could execute. OpenClaw received the message `"Blocked by Sondera policy (sondera-block-rm)"` and told the user: _“I am not able to execute that command. It is blocked by a safety policy. Is there something else I can help with?”_

Here’s the policy that made this happen:

```
// Policy: sondera-block-rm
@id("sondera-block-rm")
forbid(principal, action, resource)
when {
  action == Sondera::Action::"exec" &&
  context has params && context.params has command &&
  context.params.command like "*rm *"
};

// Policy: sondera-block-rf-flags
@id("sondera-block-rf-flags")
forbid(principal, action, resource)
when {
  action == Sondera::Action::"exec" &&
  context has params && context.params has command &&
  (
    context.params.command like "*-rf*" ||
    context.params.command like "*-fr*"
  )
};
```

Two overlapping policies catch this threat. The second blocks `-rf` and `-fr` flags, but an agent could try `-r -f` or `-f -r` as separate flags. That’s why the first policy blocks any command containing `rm` entirely. The trade-off: the agent loses the ability to delete files with `rm`.

### **Protecting Cloud Credentials**

AWS credentials in `~/.aws/credentials` provide access to your entire cloud infrastructure. An agent that reads this file can exfiltrate the keys, and those keys can provision resources, access S3 buckets, or pivot to other services. Prompt instructions like “do not read sensitive files” fail because the agent does not reliably know which files are sensitive. It might read the credentials while debugging an AWS CLI issue, or an attacker might ask it to “check the AWS configuration” without mentioning credentials.

Here’s what happens when OpenClaw tries to read `~/.aws/credentials` with Sondera enabled:

[![](https://substackcdn.com/image/fetch/$s_!HPX0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc8dc00ef-05f9-4143-84f7-cd4b9f3e5a06_2082x2546.png)](https://substackcdn.com/image/fetch/$s_!HPX0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc8dc00ef-05f9-4143-84f7-cd4b9f3e5a06_2082x2546.png) Access to ~/.aws/credentials blocked by multiple policies

The read was blocked before the file contents were returned. OpenClaw also attempted `~/.aws/config` as a fallback. Also blocked.

Here’s the policy that made this happen:

```
// Policy: sondera-block-read-cloud-creds
@id("sondera-block-read-cloud-creds")
forbid(principal, action, resource)
when {
  action == Sondera::Action::"read" &&
  context has params && context.params has path &&
  (context.params.path like "*/.aws/*" ||
   context.params.path like "*/.gcloud/*" ||
   context.params.path like "*/.azure/*" ||
   context.params.path like "*/.kube/config*")
};
```

The policy checks every `read` action and blocks any path matching cloud credential directories. One policy covers AWS, GCP, Azure, and Kubernetes. The agent never sees the file contents.

### **Redacting Secrets from Output**

Sometimes blocking the read is too restrictive. The agent needs to read a config file to help you debug, but that file contains an API key. PRE\_TOOL blocking would prevent the read entirely. POST\_TOOL redaction is a different approach: let the agent read the file, but strip sensitive patterns from the output before they are saved to the conversation transcript.

**Important limitation:** Due to OpenClaw’s current hook architecture, POST\_TOOL redaction cleans what gets persisted, not what the agent sees in the current session. The agent may still see and respond with sensitive content on screen. The value is that secrets are not saved to session transcripts where they could be exposed later.

Here’s what happens when OpenClaw reads a file containing API keys with Sondera enabled:

[![](https://substackcdn.com/image/fetch/$s_!QO9u!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37baf9f2-a973-40cd-ae32-3f1ea292fe36_2082x2546.png)](https://substackcdn.com/image/fetch/$s_!QO9u!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37baf9f2-a973-40cd-ae32-3f1ea292fe36_2082x2546.png) File read succeeds but API keys are redacted from the transcript

The file was read successfully. Sensitive content is stripped before saving to the transcript, but the agent may have seen it during the session.

Here’s the policy that made this happen:

```
// Policy: sondera-redact-api-keys
@id("sondera-redact-api-keys")
forbid(principal, action, resource)
when {
  action == Sondera::Action::"read_result" &&
  context has response &&
  context.response like "*_API_KEY=*"
};

// Policy: sondera-redact-anthropic-keys
@id("sondera-redact-anthropic-keys")
forbid(principal, action, resource)
when {
  action == Sondera::Action::"read_result" &&
  context has response &&
  context.response like "*sk-ant-*"
};
```

These policies check the `read_result` action (the output after a tool runs) and redact any content matching API key patterns. The first catches environment variable style keys (`_API_KEY=`). The second catches Anthropic API keys (`sk-ant-`). PRE\_TOOL blocks actions before they execute. POST\_TOOL cleans what gets persisted. Even if the agent sees a secret during the session, POST\_TOOL ensures it’s not saved to session transcripts where it could be exposed through exports, shared history, or other agents reading the session later.

### **Preventing Persistence Attacks**

`Crontab` lets users schedule commands to run automatically. An attacker who compromises an agent session can use `crontab` to establish persistence: schedule a script that runs every hour, exfiltrates data, or re-establishes access even after the original session ends. This maps to ASI02 (Tool Misuse & Exploitation) in the [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/). Prompt guardrails fail here because the request to “set up a scheduled task” sounds legitimate. The agent has no way to distinguish between a user setting up a backup script and an attacker establishing a foothold.

Here’s what happens when OpenClaw tries to access `crontab` with Sondera enabled:

[![](https://substackcdn.com/image/fetch/$s_!FkSa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9333ac87-1216-4995-b08a-250bc5426c96_2082x2546.png)](https://substackcdn.com/image/fetch/$s_!FkSa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9333ac87-1216-4995-b08a-250bc5426c96_2082x2546.png) Crontab access blocked, mapping to ASI02 (Tool Misuse & Exploitation) persistence prevention

The command was blocked before it could execute. This policy comes from the OWASP Agentic Pack, which maps controls to the OWASP Top 10 for Agentic Applications framework.

Here’s the policy that made this happen:

```
// Policy: owasp-block-crontab (ASI02)
@id("owasp-block-crontab")
forbid(principal, action, resource)
when {
  action == Sondera::Action::"exec" &&
  context has params && context.params has command &&
  (context.params.command like "*crontab*-e*" ||
   context.params.command like "*crontab*-r*" ||
   context.params.command like "*crontab*-l*|*" ||
   context.params.command like "*/etc/cron*")
};
```

The policy blocks `crontab` editing (`-e`), removal (`-r`), listing piped to other commands (`-l|`), and direct access to `/etc/cron*` directories. The OWASP Agentic Pack includes similar rules for `systemctl`, `launchd`, and other scheduling mechanisms.

## **Try the Sondera Extension**

### Experimental Release

> This is a research release. The hooks architecture in OpenClaw is an active area of development, and the policies have not been rigorously tested. Use at your own risk, not in production environments.
>
> The current state requires transparency. The `before_tool_call` and `after_tool_call` hooks are documented in [OpenClaw’s agent loop documentation](https://docs.openclaw.ai/concepts/agent-loop) but **not fully wired in the current release**. There is active work to address this, with multiple PRs in flight. We’ve submitted [PR #8448](https://github.com/openclaw/openclaw/pull/8448) to upstream these changes.
>
> The Sondera fork below includes the necessary hook wiring. Install from there until these changes land in mainline OpenClaw.

### Requirements

**OpenClaw 2026.2.0 or later** with plugin hook support.

If the extension installs but doesn’t block anything, your OpenClaw version may not have the required hooks yet. Check for updates or [join the OpenClaw Discord](https://discord.gg/clawd) for the latest compatibility info.

> The OpenClaw plugin hooks are not fully wired in the current release. Until the hooks land in mainline, install from the Sondera fork using the instructions below.
>
> Test in an isolated environment before running with access to production systems or sensitive data. We recommend the [Trail of Bits devcontainer](https://github.com/trailofbits/claude-code-devcontainer) for sandboxed testing.

```
# Clone the Sondera fork
# (Once PR is merged, use: git clone https://github.com/openclaw/openclaw.git)
git clone https://github.com/sondera-ai/openclaw.git
cd openclaw
git checkout sondera-pr

# Install and build
npm install -g pnpm
pnpm install
pnpm ui:build
pnpm build
pnpm openclaw onboard --install-daemon

# Start the gateway
pnpm openclaw gateway
# Dashboard: http://localhost:18789

# Dev container users (e.g. Trail of Bits devcontainer):
# Add to .devcontainer/devcontainer.json:
#   "forwardPorts": [18789],
#   "appPort": [18789]
# Then rebuild. Before pnpm install, run:
#   pnpm config set store-dir ~/.pnpm-store
# To start the gateway, use:
#   pnpm openclaw gateway --bind lan
```

This installs OpenClaw from the Sondera fork with the hook wiring needed for policy enforcement. Once OpenClaw merges the hook fixes into mainline, you’ll be able to install directly.

See the [full installation guide](https://docs.sondera.ai/integrations/openclaw/) for detailed setup instructions and configuration options.

### **Feedback Welcome!**

This project is experimental. We want to hear what works, what breaks, and what policies you need. Open an issue on [OpenClaw GitHub](https://github.com/openclaw/openclaw/issues) or join the [OpenClaw Discord](https://discord.gg/clawd) to share your experience.

## **Community Effort**

### **Related Security Work**

Other contributors are working on OpenClaw security. Here’s what’s in flight:

**[@Reapor-Yurnero](https://github.com/Reapor-Yurnero)**, **[@Scrattlebeard](https://github.com/Scrattlebeard)**, and **[@nwinter](https://github.com/nwinter)** — [PR #6095: Modular Guardrails Extensions](https://github.com/openclaw/openclaw/pull/6095)

- Adds `before_request` and `after_response` message-stage hooks

- Extends `before_tool_call`/`after_tool_call` with richer context

- Includes example guardrails: Gray Swan Cygnal, Command-Safety-Guard, Security-Audit

- Closes multiple security issues (#4011, #4840, #5155, #5513, #5943, #6459, #6613, #6823, #7597)


**[@pauloportella](https://github.com/pauloportella)** — [PR #6569: Interceptor Pipeline](https://github.com/openclaw/openclaw/pull/6569)

- Typed, priority-sorted interceptor system

- `tool.before`, `tool.after`, `message.before`, `params.before` hooks

- Built-in `command-safety-guard` and `security-audit` interceptors

- Regex-based tool matching and observability


**[@msl2246](https://github.com/msl2246)** — [Issue #5513: Plugin hooks are never invoked](https://github.com/openclaw/openclaw/issues/5513) (root cause analysis that identified the timing bug)

These approaches complement each other. Model-based guardrails (like Gray Swan Cygnal) use AI to detect novel prompt injection attempts. Rule-based validators use regex for known patterns. Policy as code with Cedar sits between: deterministic like regex, but more expressive. You can compose rules, define permit/deny logic, and enable lockdown mode with explicit allowlists. Defense in depth means combining these layers.

## **Beyond Pattern Matching: What Comes Next**

The current implementation has clear limitations. These rules are **signature and pattern-based**. Agents will search for workarounds. In our testing, we observed agents blocked from `rm -rf` attempt `find -delete` instead. The Sondera packs include overlapping rules to catch common alternatives, but determined agents will probe for gaps. Single-turn evaluation also can’t capture cross-session state or behavioral patterns.

Deterministic lanes unlock capabilities that prompt-based governance can’t achieve:

- **Trajectory-aware state:** If an agent touches sensitive data in Step 1, block external API calls in Step 10, even across sessions

- **Behavioral circuit breakers:** Detect when an agent’s search throughput shifts from mission completion to boundary probing

- **Policy generation:** Auto-generate Cedar policies from your agent’s actual behavior. Baseline what is normal, flag what is anomalous

- **Compliance mapping:** Generate audit trails for teams that need them


The bigger picture extends beyond OpenClaw. The same pattern (infrastructure-level policy enforcement on tool calls) works with Claude Code, Cursor, LangGraph agents, Google ADK, and custom implementations. Any system where an agent makes tool calls can benefit from deterministic policy guardrails.

## **The Path to Meaningful Autonomy**

The goal is not to block agents. The goal is to let them do more, safely. The more control you have, the more autonomy you can grant. **Constraints enable capability.**

Sandboxes provide isolation. Policy as code adds finer-grained governance. Together, they transform the binary choice into a spectrum of precisely-defined permissions. You can accept the lethal trifecta and mitigate its risks rather than eliminating its power.

OpenClaw represents what we all want: AI agents capable enough to be genuinely useful. The security challenge is not whether to allow this future. The challenge is building the infrastructure that makes it trustworthy.

Secure Trajectories helps you move agents from YOLO to production.

Subscribe

[Share](https://blog.sondera.ai/p/openclaw-rm-rf-policy-as-code?utm_source=substack&utm_medium=email&utm_content=share&action=share)

[![Secure By Design llc's avatar](https://substackcdn.com/image/fetch/$s_!hl_l!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa524cb5a-d3db-4cc3-a7be-fd200904111a_727x1080.jpeg)](https://substack.com/profile/4083872-secure-by-design-llc)[![Sumant Thakur's avatar](https://substackcdn.com/image/fetch/$s_!Ou--!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F037dea85-ff8b-4a96-bc36-55519cbbeb8f_1179x1179.jpeg)](https://substack.com/profile/73575842-sumant-thakur)[![Nicholas Wagner's avatar](https://substackcdn.com/image/fetch/$s_!cs7O!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F231c5227-3559-4fc5-81ac-78207b4e2a55_848x871.jpeg)](https://substack.com/profile/1510719-nicholas-wagner)[![Andrea Politano's avatar](https://substackcdn.com/image/fetch/$s_!8KMp!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82454e75-7319-40b1-8403-b96579d4d8da_1366x1366.jpeg)](https://substack.com/profile/126188014-andrea-politano)[![Matt Maisel's avatar](https://substackcdn.com/image/fetch/$s_!Dl3t!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffa454c10-f74d-4f8d-b3c5-a5de46287be7_800x800.jpeg)](https://substack.com/profile/349931863-matt-maisel)

17 Likes∙

[5 Restacks](https://substack.com/note/p-186803965/restacks?utm_source=substack&utm_content=facepile-restacks)

17

2

5

Share

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

[![The AI Architect's avatar](https://substackcdn.com/image/fetch/$s_!Hsg8!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F558d3d2d-6947-42ce-a62f-3c7c1c5d2ca3_2048x2048.png)](https://substack.com/profile/40266909-the-ai-architect?utm_source=comment)

[The AI Architect](https://substack.com/profile/40266909-the-ai-architect?utm_source=substack-feed-item)

[Feb 4](https://blog.sondera.ai/p/openclaw-rm-rf-policy-as-code/comment/209784673 "Feb 4, 2026, 8:43 AM")

Liked by Josh Devon, Matt Maisel, Tyler Predale

Impressive work on the deterministic enforcement layer. The policy-as-code approch solves what prompt guardrails fundamentally can't, which is adversarial compliance. Seen too many "just tell the agent not to" solutions fail in prod when someone crafts the right jailbreak. The cross-session state idea for trajectory-aware blocking is where this gets realy powerful though.

Like (3)

Reply

Share

[![Sumant Thakur's avatar](https://substackcdn.com/image/fetch/$s_!Ou--!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F037dea85-ff8b-4a96-bc36-55519cbbeb8f_1179x1179.jpeg)](https://substack.com/profile/73575842-sumant-thakur?utm_source=comment)

[Sumant Thakur](https://substack.com/profile/73575842-sumant-thakur?utm_source=substack-feed-item)

[Feb 4](https://blog.sondera.ai/p/openclaw-rm-rf-policy-as-code/comment/210142092 "Feb 4, 2026, 10:41 PM")

Great post, policy-as-code have been out there for long but with Agentic AI it is more relevant and required!

Like

Reply

Share

TopLatestDiscussions

[How We Hijacked a Claude Skill with an Invisible Sentence](https://blog.sondera.ai/p/claude-skill-hijack-invisible-sentence)

[A logic-based attack bypasses both the human eyeball test and the platform's own prompt guardrails, revealing a critical flaw in today's agent security…](https://blog.sondera.ai/p/claude-skill-hijack-invisible-sentence)

Oct 20, 2025•[Josh Devon](https://substack.com/@joshdevon)

33

10

5

![](https://substackcdn.com/image/fetch/$s_!Bc6B!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F282542ab-c1fc-4e51-849a-c4aa3c7196cc_1024x1024.jpeg)

[Your AI Agent Just Got Pwned](https://blog.sondera.ai/p/your-ai-agent-just-got-pwned)

[A Security Engineer's Guide to Building Trustworthy Autonomous Systems](https://blog.sondera.ai/p/your-ai-agent-just-got-pwned)

Dec 8, 2025•[Matt Maisel](https://substack.com/@mattmaisel)

30

2

6

![](https://substackcdn.com/image/fetch/$s_!m8f5!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9dec8e8f-5558-4ed2-9dab-451029a60875_1920x1080.png)

[Hooking Coding Agents with the Cedar Policy Language](https://blog.sondera.ai/p/hooking-coding-agents-with-the-cedar)

[A reference monitor built on the trajectory event model.](https://blog.sondera.ai/p/hooking-coding-agents-with-the-cedar)

Mar 5•[Matt Maisel](https://substack.com/@mattmaisel)

17

2

4

![](https://substackcdn.com/image/fetch/$s_!36YS!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F27525a7d-47cd-4386-a59f-d72ce3b36bd5_1233x707.png)

See all

### Ready for more?

Subscribe
