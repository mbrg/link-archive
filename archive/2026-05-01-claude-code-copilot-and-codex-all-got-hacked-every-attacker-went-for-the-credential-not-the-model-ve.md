---
date: '2026-05-01'
description: Recent findings highlight critical vulnerabilities across AI coding agents,
  exposing enterprise OAuth tokens to exploitation. Research teams revealed six exploits
  impacting Claude Code, Copilot, Codex, and Vertex AI, primarily targeting runtime
  credentials rather than model outputs. Key issues include inadequate input sanitization
  and excessive permissions, leading to unauthorized access. A governance gap exists,
  with enterprises poorly managing AI agent identities and their associated credentials.
  Effective security measures must prioritize credential inventory, OAuth scope audits,
  and enhanced identity validation protocols to mitigate these risks and bolster overall
  system integrity.
link: https://venturebeat.com/security/six-exploits-broke-ai-coding-agents-iam-never-saw-them
tags:
- Identity Governance
- Credential Management
- AI Security
- Vulnerability Exploits
- Threat Intelligence
title: Claude Code, Copilot and Codex all got hacked. Every attacker went for the
  credential, not the model. ◆ VentureBeat
---

[Louis Columbus](https://venturebeat.com/author/louis-columbus)

9:30 am, PT, April 30, 2026


![Six exploits broke Claude Code, Copilot, Codex, and Vertex AI. Your IAM never saw any of them.](https://venturebeat.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fjdtwqhzvc2n1%2F2KikESFD5r42LAO66sAKSK%2F0505660b31c83a54c4701cfcd1cc6ff1%2FSix_exploits_broke_Claude_Code__Copilot__Codex__and_Vertex_AI_Your_IAM_never_saw_them_coming.png%3Fw%3D1000%26q%3D100&w=3840&q=85)

VentureBeat created with Imagen

[Add to Google Preferred Source](https://www.google.com/preferences/source?q=venturebeat.com "Add to Google Preferred Source")

On March 30, [BeyondTrust](https://www.beyondtrust.com/blog/entry/openai-codex-command-injection-vulnerability-github-token) proved that a crafted GitHub branch name could steal Codex’s OAuth token in cleartext. OpenAI classified it Critical P1. Two days later, Anthropic’s Claude Code source code [spilled onto the public npm registry](https://venturebeat.com/technology/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know), and within hours, [Adversa](https://adversa.ai/blog/claude-code-security-bypass-deny-rules-disabled/) found Claude Code silently ignored its own deny rules once a command exceeded 50 subcommands. These were not isolated bugs. They were the latest in a nine-month run: six research teams disclosed exploits against Codex, Claude Code, Copilot, and Vertex AI, and every exploit followed the same pattern. An AI coding agent held a credential, executed an action, and authenticated to a production system without a human session anchoring the request.

The attack surface was first demonstrated at Black Hat USA 2025, when Zenity CTO [Michael Bargury hijacked](https://labs.zenity.io/p/hsc25) ChatGPT, Microsoft Copilot Studio, Google Gemini, Salesforce Einstein and Cursor with Jira MCP on stage with zero clicks. Nine months later, those credentials are what attackers reached.

Merritt Baer, CSO at Enkrypt AI and former Deputy CISO at AWS, named the failure in an exclusive VentureBeat interview. “Enterprises believe they’ve ‘approved’ AI vendors, but what they’ve actually approved is an interface, not the underlying system.” The credentials underneath the interface are the breach.

## Codex, where a branch name stole GitHub tokens

[BeyondTrust](https://www.beyondtrust.com/blog/entry/openai-codex-command-injection-vulnerability-github-token) researcher Tyler Jespersen, with Fletcher Davis and Simon Stewart, found Codex cloned repositories using a GitHub OAuth token embedded in the git remote URL. During cloning, the branch name parameter flowed unsanitized into the setup script. A semicolon and a backtick subshell turned the branch name into an exfiltration payload.

Stewart added the stealth. By appending 94 Ideographic Space characters (Unicode U+3000) after “main,” the malicious branch looked identical to the standard main branch in the Codex web portal. A developer sees “main.” The shell sees curl exfiltrating their token. OpenAI classified it Critical P1 and shipped full remediation by February 5, 2026.

## Claude Code, where two CVEs and a 50-subcommand bypass broke the sandbox

[CVE-2026-25723](https://www.sentinelone.com/vulnerability-database/cve-2026-25723/) hit Claude Code’s file-write restrictions. Piped sed and echo commands escaped the project sandbox because command chaining was not validated. Patched in 2.0.55. [CVE-2026-33068](https://www.sentinelone.com/vulnerability-database/cve-2026-33068/) was subtler. Claude Code resolved permission modes from .claude/settings.json before showing the workspace trust dialog. A malicious repo set permissions.defaultMode to bypassPermissions. The trust prompt never appeared. Patched in 2.1.53.

The 50-subcommand bypass landed last. Adversa found that Claude Code silently dropped deny-rule enforcement once a command exceeded 50 subcommands. Anthropic’s engineers had traded security for speed and stopped checking after the fiftieth. Patched in 2.1.90.

“A significant vulnerability in enterprise AI is broken access control, where the flat authorization plane of an LLM fails to respect user permissions,” wrote Carter Rees, VP of AI and Machine Learning at [Reputation](https://reputation.com/) and a member of the Utah AI Commission. The repository decided what permissions the agent had. The token budget decided which deny rules survived.

## Copilot, where a pull request description and a GitHub issue both became root

[Johann Rehberger](https://embracethered.com/blog/posts/2025/github-copilot-remote-code-execution-via-prompt-injection/) demonstrated [CVE-2025-53773](https://embracethered.com/blog/posts/2025/github-copilot-remote-code-execution-via-prompt-injection/) against GitHub Copilot with [Markus Vervier of Persistent Security](https://www.persistent-security.net/post/part-iii-vscode-copilot-wormable-command-execution-via-prompt-injection) as co-discoverer. Hidden instructions in PR descriptions triggered Copilot to flip auto-approve mode in .vscode/settings.json. That disabled all confirmations and granted unrestricted shell execution across Windows, macOS, and Linux. Microsoft patched it in the August 2025 Patch Tuesday release.

Then, [Orca Security](https://orca.security/resources/blog/roguepilot-github-copilot-vulnerability/) cracked Copilot inside GitHub Codespaces. Hidden instructions in a GitHub issue manipulated Copilot into checking out a malicious PR with a symbolic link to /workspaces/.codespaces/shared/user-secrets-envs.json. A crafted JSON $schema URL exfiltrated the privileged GITHUB\_TOKEN. Full repository takeover. Zero user interaction beyond opening the issue.

Mike Riemer, CTO at Ivanti, framed the speed dimension in a VentureBeat interview: “Threat actors are reverse engineering patches within 72 hours. If a customer doesn’t patch within 72 hours of release, they’re open to exploit.” Agents compress that window to seconds.

## Vertex AI, where default scopes reached Gmail, Drive and Google’s own supply chain

[Unit 42](https://unit42.paloaltonetworks.com/double-agents-vertex-ai/) researcher Ofir Shaty found that the default Google service identity attached to every Vertex AI agent had excessive permissions. Stolen P4SA credentials granted unrestricted read access to every Cloud Storage bucket in the project and reached restricted, Google-owned Artifact Registry repositories at the core of the Vertex AI Reasoning Engine. Shaty described the compromised P4SA as functioning like a "double agent," with access to both user data and Google's own infrastructure.

## VentureBeat defense grid

|     |     |     |     |
| --- | --- | --- | --- |
| **Security requirement** | **Defense shipped** | **Exploit path** | **The gap** |
| Sandbox AI agent execution | Codex runs tasks in cloud containers; token scrubbed during agent runtime. | Token present during cloning. Branch-name command injection executed before cleanup. | No input sanitization on container setup parameters. |
| Restrict file system access | Claude Code sandboxes writes via accept-edits mode. | Piped sed/echo escaped sandbox (CVE-2026-25723). Settings.json bypassed trust dialog (CVE-2026-33068). 50-subcommand chain dropped deny-rule enforcement. | Command chaining not validated. Settings loaded before trust. Deny rules truncated for performance. |
| Block prompt injection in code context | Copilot filters PR descriptions for known injection patterns. | Hidden injections in PRs, README files, and GitHub issues triggered RCE (CVE-2025-53773 + Orca RoguePilot). | Static pattern matching loses to embedded prompts in legitimate review and Codespaces flows. |
| Scope agent credentials to least privilege | Vertex AI Agent Engine uses P4SA service agent with OAuth scopes. | Default scopes reached Gmail, Calendar, Drive. P4SA credentials read every Cloud Storage bucket and Google’s Artifact Registry. | OAuth scopes non-editable by default. Least privilege violated by design. |
| Inventory and govern agent identities | No major AI coding agent vendor ships agent identity discovery or lifecycle management. | Not attempted. Enterprises do not inventory AI coding agents, their credentials, or their permission scopes. | AI coding agents are invisible to IAM, CMDB, and asset inventory. Zero governance exists. |
| Detect credential exfiltration from agent runtime | Codex obscures tokens in web portal view. Claude Code logs subcommands. | Tokens visible in cleartext inside containers. Unicode obfuscation hid exfil payloads. Subcommand chaining hid intent. | No runtime monitoring of agent network calls. Log truncation hid the bypass. |
| Audit AI-generated code for security flaws | Anthropic launched [Claude Code Security](https://www.anthropic.com/news/claude-code-security) (Feb 2026). OpenAI launched [Codex Security](https://www.axios.com/2026/03/06/openai-codex-security-ai-cyber) (March 2026). | Both scan generated code. Neither scans the agent’s own execution environment or credential handling. | Code-output security is not agent-runtime security. The agent itself is the attack surface. |

## Every exploit targeted runtime credentials, not model output

Every vendor shipped a defense. Every defense was bypassed.

The [Sonar 2026 State of Code Developer Survey](https://www.sonarsource.com/resources/developer-survey-report/) found 25% of developers use AI agents regularly, and 64% have started using them. [Veracode](https://www.veracode.com/blog/genai-code-security-report/) tested more than 100 LLMs and found 45% of generated code samples introduced OWASP Top 10 flaws, a separate failure that compounds the runtime credential gap.

CrowdStrike CTO Elia Zaitsev framed the rule in an exclusive VentureBeat interview at RSAC 2026: [collapse agent identities back to the human](https://venturebeat.com/security/rsac-2026-agent-identity-frameworks-three-gaps), because an agent acting on your behalf should never have more privileges than you do. Codex held a GitHub OAuth token scoped to every repository the developer authorized. Vertex AI’s P4SA read every Cloud Storage bucket in the project. Claude Code traded deny-rule enforcement for token budget.

Kayne McGladrey, an IEEE Senior Member who advises enterprises on identity risk, made the same diagnosis in an exclusive interview with VentureBeat. " [It uses far more permissions than it should have](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook), more than a human would, because of the speed of scale and intent."

Riemer drew the operational line in an exclusive VentureBeat interview. "It becomes, I don't know you until I validate you." The branch name talked to the shell before validation. The GitHub issue talked to Copilot before anyone read it.

## Security director action plan

1. **Inventory every AI coding agent (CIEM).** Codex, Claude Code, Copilot, Cursor, Gemini Code Assist, Windsurf. List the credentials and OAuth scopes each received at setup. If your CMDB has no category for AI agent identities, create one.

2. **Audit OAuth scopes and patch levels.** Upgrade Claude Code to 2.1.90 or later. Verify Copilot's August 2025 patch. Migrate Vertex AI to the bring-your-own-service-account model.

3. **Treat branch names, pull request descriptions, GitHub issues, and repo configuration as untrusted input.** Monitor for Unicode obfuscation (U+3000), command chaining over 50 subcommands, and changes to .vscode/settings.json or .claude/settings.json that flip permission modes.

4. **Govern agent identities the way you govern human privileged identities (PAM/IGA).** Credential rotation. Least-privilege scoping. Separation of duties between the agent that writes code and the agent that deploys it. CyberArk, Delinea, and any PAM platform that accepts non-human identities can onboard agent OAuth credentials today; [Gravitee's 2026 survey](https://www.gravitee.io/blog/state-of-ai-agent-security-2026-report-when-adoption-outpaces-control) found only 21.9% of teams have done it.

5. **Validate before you communicate.** "As long as we trust and we check and we validate, I'm fine with letting AI maintain it," Riemer said. Before any AI coding agent authenticates to GitHub, Gmail, or an internal repository, verify the agent's identity, scope, and the human session it is bound to.

6. **Ask each vendor in writing before your next renewal.** "Show me the identity lifecycle management controls for the AI agent running in my environment, including credential scope, rotation policy, and permission audit trail." If the vendor cannot answer, that is the audit finding.


## **The governance gap in three sentences**

Most CISOs inventory every human identity and have zero inventory of the AI agents running with equivalent credentials. No IAM framework governs human privilege escalation and agent privilege escalation with the same rigor. Most scanners track every CVE but cannot alert when a branch name exfiltrates a GitHub token through a container that developers trust by default.

Zaitsev's advice to RSAC 2026 attendees was blunt: you already know what to do. Agents just made the cost of not doing it catastrophic.

## More

[![Security Teams Deprioritized Both Palo Alto CVEs as Non-Critical. Chained Together, They Were a Kill Shot](https://venturebeat.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fjdtwqhzvc2n1%2FhjtJE1itxnyTrftv5Ef7a%2Fa57e3655e1b832acec36c5ab10a47dc5%2Fmeyers_hero.png%3Fw%3D1000%26q%3D100&w=3840&q=50)\\
\\
VentureBeat created with Imagen](https://venturebeat.com/security/cvss-triage-failure-chained-vulnerability-audit-security-directors)

Five ways CVSS vulnerability triage misses the kill chain — and the specific actions security directors can take this month.

[Louis Columbus](https://venturebeat.com/author/louis-columbus)
April 24, 2026


[![Cisco's Jeetu Patel says trusted delegation is the line between bankruptcy and market dominance. Only 5% of enterprises crossed it](https://venturebeat.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fjdtwqhzvc2n1%2F673zAlj9W9yRILFBZOklRb%2Fb0ca2015b9f2e63e50a691f182097932%2Fkeynote_with_jeetu_hero.png%3Fw%3D1000%26q%3D100&w=3840&q=50)\\
\\
Source: Cisco Video Portal (https://video.cisco.com/detail/video/6391539167112)](https://venturebeat.com/security/85-of-enterprises-are-running-ai-agents-only-5-trust-them-enough-to-ship)

An 80-point gap separates AI agent pilots from production. Patel's RSAC interview reveals why trust — not technology — is what's keeping enterprises stuck.

[Louis Columbus](https://venturebeat.com/author/louis-columbus)
April 24, 2026


[![One Employee's AI Tool Just Opened the Door to Vercel's Internal Systems. Here's the OAuth Scoping Audit Every Security Director Needs Now](https://venturebeat.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fjdtwqhzvc2n1%2F6wgHVXn6N3biFNjGQrW3dM%2F05683cce2c54c5658a779c71e09887df%2FVercel_breach.png%3Fw%3D1000%26q%3D100&w=3840&q=50)\\
\\
VentureBeat made with Imagen](https://venturebeat.com/security/vercel-breach-exposes-the-oauth-gap-most-security-teams-cannot-detect-scope-or-contain)

One AI tool OAuth grant. Four organizational boundaries. No zero-day required. How the Vercel breach exposed a detection gap most security programs can't close.

[Louis Columbus](https://venturebeat.com/author/louis-columbus)
April 21, 2026


[![Three frontier AI system cards promise safety. None quantifies agent-runtime resistance](https://venturebeat.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fjdtwqhzvc2n1%2F338TKAZmGg0eamRggz05Kq%2Ffdc8465b217fab704067d122300d6da7%2Fhero_model_comparison.png%3Fw%3D1000%26q%3D100&w=3840&q=50)\\
\\
VentureBeat created with Imagen](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)

A researcher typed one malicious PR title and exfiltrated API keys from three AI coding agents. One vendor's system card warned it was possible.

[Louis Columbus](https://venturebeat.com/author/louis-columbus)
April 21, 2026


[![Adversaries hijacked AI security tools at 90+ organizations. The next wave has write access to your firewall](https://venturebeat.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fjdtwqhzvc2n1%2F46SzboB6NVjamCROg8pfcE%2Fa20c84d337fb68ef55e801810cab5308%2Fhero.png%3Fw%3D1000%26q%3D100&w=3840&q=50)\\
\\
VentureBeat created with Imagen](https://venturebeat.com/security/adversaries-hijacked-ai-security-tools-at-90-organizations-the-next-wave-has-write-access-to-the-firewall)

The AI tools attackers hijacked in 2025 could only read data. The autonomous SOC agents shipping now can rewrite infrastructure.

[Louis Columbus](https://venturebeat.com/author/louis-columbus)
April 21, 2026


[![Enterprises funded stage-one security for their AI agents. Stage-three threats arrived anyway. Here is the maturity audit that closes the gap](https://venturebeat.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fjdtwqhzvc2n1%2F2oq4gxUSORHuJY6GKHVxQ1%2F1ff08d293fe4d0c43df9f5c7a1893344%2Fhero_survey.png%3Fw%3D1000%26q%3D100&w=3840&q=50)\\
\\
VentureBeat created with Imagen](https://venturebeat.com/security/most-enterprises-cant-stop-stage-three-ai-agent-threats-venturebeat-survey-finds)

A rogue Meta agent and a Mercor supply-chain breach expose the same gap: enterprises fund monitoring, not isolation. VentureBeat's maturity audit maps the fix.

[Louis Columbus](https://venturebeat.com/author/louis-columbus)
April 17, 2026


[![Microsoft Copilot Studio and Salesforce Agentforce both fell to the same attack class. Here is the enterprise agent remediation playbook](https://venturebeat.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fjdtwqhzvc2n1%2F6QO34Fn3Ix5qFbnemAM3a5%2F6cf10a1a9ecd680e39c790c0733d16fd%2FHERO_CAPSULE.png%3Fw%3D1000%26q%3D100&w=3840&q=50)](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook)

Safety mechanisms flagged the attack. DLP never fired. A new CVE class for agentic AI is exposing what patches alone can't fix.

[Louis Columbus](https://venturebeat.com/author/louis-columbus)
April 15, 2026


[![AI question](https://venturebeat.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fjdtwqhzvc2n1%2F4z68iLEpqAtIY5EAKVlov3%2Feda1e72826a8322c9042c0c5f1fe7726%2FAI_question.png%3Fw%3D1000%26q%3D100&w=3840&q=50)\\
\\
CleoP made with Midjourney](https://venturebeat.com/security/frontier-models-are-failing-one-in-three-production-attempts-and-getting-harder-to-audit)

Capability is no longer the constraint. Reliability, transparency and benchmark validity are — and all three are getting worse.

[Taryn Plumb](https://venturebeat.com/author/taryn-plumb)
April 15, 2026


[![nuneybits Vector art of developer mopping code spill dbcceaac-fb6e-4e63-90cf-5774d34a0f44](https://venturebeat.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fjdtwqhzvc2n1%2F5nAHuSU7TlSixVhQbV3Zpy%2Ff97f9591cd1d877db961dac2be53b6cc%2Fnuneybits_Vector_art_of_developer_mopping_code_spill_dbcceaac-fb6e-4e63-90cf-5774d34a0f44.webp%3Fw%3D1000%26q%3D100&w=3840&q=50)\\
\\
Credit: VentureBeat made with Midjourney](https://venturebeat.com/technology/43-of-ai-generated-code-changes-need-debugging-in-production-survey-finds)

The software industry is racing to write code with artificial intelligence. It is struggling, badly, to make sure that code holds up once it ships.

[Michael Nuñez](https://venturebeat.com/author/michael_nunez)
April 14, 2026


[![AI drift](https://venturebeat.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fjdtwqhzvc2n1%2FerAw6FrOeAX9eZJqeF2Dx%2F3a759d02f32a698bdc815c787701a17a%2FAI_drift.png%3Fw%3D1000%26q%3D100&w=3840&q=50)\\
\\
CleoP made with Midjourney](https://venturebeat.com/security/five-signs-data-drift-is-already-undermining-your-security-models)

Data drift happens when the statistical properties of a machine learning (ML) model's input data change over time, eventually rendering its predictions less accurate. [Cybersecurity professionals](https://venturebeat.com/security/ocsf-explained-the-shared-data-language-security-teams-have-been-missing?_gl=1*yt0z35*_up*MQ..*_ga*MTcxNTczODYxLjE3NzYwMDUzOTE.*_ga_B8TDS1LEXQ*czE3NzYwMDUzODkkbzEkZzAkdDE3NzYwMDUzODkkajYwJGwwJGgw*_ga_SCH1J7LNKY*czE3NzYwMDUzODkkbzEkZzAkdDE3NzYwMDUzODkkajYwJGwwJGgw) who rely on ML for tasks like malware detection and network threat analysis find that undetected data drift can create vulnerabilities. A model trained on old attack patterns may fail to see today's sophisticated threats. Recognizing the early signs of data drift is the first step in maintaining reliable and efficient security systems.

[Zac Amos, ReHack](https://venturebeat.com/author/zac-amos-rehack)
April 12, 2026


[![AI perimeter](https://venturebeat.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fjdtwqhzvc2n1%2FpAoHef9hMVI3aHoyHfluC%2Ff410fef5dc2a910939184a98db76eec4%2FAI_perimeter.png%3Fw%3D1000%26q%3D100&w=3840&q=50)\\
\\
CleoP made with Midjourney](https://venturebeat.com/security/your-developers-are-already-running-ai-locally-why-on-device-inference-is)

For the last 18 months, the CISO playbook for generative AI has been relatively simple: Control the browser.

[Jayachander Reddy Kandakatla](https://venturebeat.com/author/jayachander-reddy-kandakatla)
April 12, 2026


[![AI Agent Credentials Live in the Same Box as Untrusted Code. Here's the Zero-Trust Architecture Audit That Shows What to Fix.](https://venturebeat.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fjdtwqhzvc2n1%2F35u1BcqPcGPsUcDOjxBtIh%2Ffb7d22c10100687068f227c644d2e297%2Fzero_trust_hero.png%3Fw%3D1000%26q%3D100&w=3840&q=50)\\
\\
Created by VentureBeat with Imagen](https://venturebeat.com/security/ai-agent-zero-trust-architecture-audit-credential-isolation-anthropic-nvidia-nemoclaw)

79% of enterprises run AI agents. 86% deployed without security approval. Two new architectures reveal how far credentials actually are from untrusted code.

[Louis Columbus](https://venturebeat.com/author/louis-columbus)
April 10, 2026
