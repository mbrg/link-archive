---
date: '2025-11-16'
description: "The report highlights the first known AI-driven cyber espionage operation,\
  \ conducted by a Chinese state-sponsored group (GTG-1002), utilizing Claude Code\
  \ for nearly autonomous attack execution. The operation involved extensive reconnaissance,\
  \ vulnerability exploitation, credential harvesting, and data exfiltration, with\
  \ AI handling 80-90% of the tasks independently. Significant challenges, such as\
  \ AI hallucination and operational validation, emerged but didn\u2019t prevent successful\
  \ intrusions across numerous high-value targets. This escalation underscores the\
  \ urgent need for robust AI safeguards and proactive defenses, as adversaries leverage\
  \ AI to lower the barriers for sophisticated cyberattacks, signaling a transformative\
  \ shift in threat landscapes."
link: /archive/2025-11-16-full-report-disrupting-the-first-reported-ai-orchestrated-cyber-espionage-campaign
tags:
- Cyber Espionage
- AI Security
- Cybersecurity Measures
- Autonomous Cyber Attacks
- Threat Intelligence
- weblog
title: 'Full report: Disrupting the first reported AI-orchestrated cyber espionage
  campaign'
type: weblog
---

This is a big deal, but its not a sophistical threat actor. It's a capable threat actor. Anyone who can get Claude Code to write and iterate on a useful program could had done this instead. They had to solve the same context engineering, tool integration and task-chunking challenges.
Attackers gain significant improved capabilities in OSS tool orchestration, exploit generation, lateral movement and data analysis. But they are doing so in a very noise way. 
Anthropic really didn't share any useful hard technical data that would allow others to do their own investigation. No IOCs. No code snippets. No network captures. They did share a blueprint that would allow any capable hacker to reproduce the attacker's approach.
Why would Chinese attackers use Claude Code with an "advanced system"? They would want to keep it secret and operational for long, no? They have plenty of Chinese models to choose from.

---

> We have developed sophisticated safety and security measures to prevent the misuse of our AI models. While these measures are generally effective, cybercriminals and other malicious actors continually attempt to fi nd ways around them. This report details a recent threat campaign we identifi ed and disrupted, along with the steps we've taken to detect and counter this type of abuse. This represents the work of Threat Intelligence: a dedicated team at Anthropic that investigates real world cases of misuse and works within our Safeguards organization to improve our defenses against such cases.

I guess everyone that tries to circumvent Anthropic's content policy is a _"malicious actor"_?
They know their guardrails are just a nuisance at best. This is nonsense.

---

> While we only have visibility into Claude usage, this case study likely refl ects consistent patterns of behavior across frontier AI models and demonstrates how threat actors are adapting their operations to exploit today's most advanced AI capabilities. Rather than merely advising on techniques, the threat actor manipulated Claude to perform actual cyber intrusion operations with minimal human oversight.

So Anthropic can just decide to read your stuff? Given the statement above that people who "find a way around" safeguards are "malicious actors" this is concerning.

---

> The threat actor developed an autonomous attack framework that used Claude Code and open standard Model Context Protocol (MCP) tools to conduct cyber operations without direct human involvement in tactical execution. The framework used Claude as an orchestration system that decomposed complex multi-stage attacks into discrete technical tasks for Claude sub-agents—such as vulnerability scanning, credential validation, data extraction, and lateral movement—each of which appeared legitimate when evaluated in isolation. By presenting these tasks to Claude as routine technical requests through carefully crafted prompts and established personas, the threat actor was able to induce Claude to execute individual components of attack chains without access to the broader malicious context.

Claude was used as an orchestration system.. so wouldn't it have the "broader malicious context"?

---

> Human operators maintained minimal direct engagement, estimated at 10 to 20 percent of total effort. Human responsibilities centered on campaign initialization and authorization decisions at critical escalation points. Human intervention occurred at strategic junctures including approving progression from reconnaissance to active exploitation, authorizing use of harvested credentials for lateral movement, and making fi nal decisions about data exfi ltration scope and retention.

These percentages are very interesting. But how were they decided on? Lines of code? Importance of work? There's a lot of trust-be-bro here.

---

> ![](https://assets.anthropic.com/m/ec212e6566a0d47/original/images/6157783dd8c4861c6cadd6ba049ad81e5114e49f8cad9348c401c8df94a74bd7.jpg)

Anthropic is trying to tell us what happened without giving a blueprint to attackers. But tbh I feel like they are giving enough for anyone who knows their stuff to replicate.

---

> Human operators began campaigns by inputting a target. The framework’s orchestration engine would then task Claude to begin autonomous reconnaissance against multiple targets in parallel. Initial targets included major technology corporations, fi nancial institutions, chemical manufacturing companies, and government agencies across multiple countries. At this point they had to convince Claude—which is extensively trained to avoid harmful behaviors—to engage in the attack. The key was role-play: the human operators claimed that they were employees of legitimate cybersecurity fi rms and convinced Claude that it was being used in defensive cybersecurity testing. Eventually, the sustained nature of the attack triggered detection, but this kind of “social engineering” of the AI model allowed the threat actor to fl y under the radar for long enough to launch their campaign.

If you have direct access to a model and can just continue to try you will succeed. Especially easy where you can create a long convo.

---

> Discovery activities proceeded without human guidance across extensive attack surfaces. In one of the limited cases of a successful compromise, the threat actor induced Claude to autonomously discover internal services, map complete network topology across multiple IP ranges, and identify high-value systems including databases and workfl ow orchestration platforms. Similar autonomous enumeration occurred against other targets’ systems with the AI independently cataloging hundreds of discovered services and endpoints.

This sounds like Claude used a bunch of Open Source recon tools through MCP. Rather than Claude "reasoning" about recon. So not so "advanced".

---

> |     |     | | --- | --- | | Claude's autonomous actions (1-4 hours) | Human operator actions (2-10 minutes) | | Task 1: Discovery Scans target infrastructure Enumerates services and endpoints Maps attack surface |  | | Task 2: Vulnerability Analysis Identifies SSRF vulnerability Researches exploitation techniques |  | | Task 3: Exploit Development •Authors custom payload Develops exploit chain Validates exploit capability via callback responses Generates exploitation report Task 4: Exploit Delivery •Deploys exploit for initial access •Establishes foothold in environment Task 5: Post-Exploitation | → Reviews AI findings and recommendations → Approves exploitation |

Ok this is actually very cool / scary. Auto-generating the exploit chain, successfully making it work, and moving onto internal recon is a huge boost for attackers.

---

> Upon receiving authorization from the human operators, Claude executed systematic credential collection across targeted networks. This involved querying internal services, extracting authentication certifi cates from confi gurations, and testing harvested credentials across discovered systems. Claude independently determined which credentials provided access to which services, mapping privilege levels and access boundaries without human direction.

Cred harvesting actually feels like a task for software not AI.

---

> Lateral movement proceeded through AI-directed enumeration of accessible systems using stolen credentials. Claude systematically tested authentication against internal APIs, database systems, container registries, and logging infrastructure, building comprehensive maps of internal network architecture and access relationships.

But mapping cred to accessible resource is again a huge AI-based boost for attackers.

---

> |     |     | | --- | --- | | Claude's autonomous actions (2-6 hours) | Human operator actions (5-20 minutes) | | 1\. Authenticate with harvested credentials |  | | 2\. Map database structure and query user account tables |  | | 3\. Extract password hashes and account details |  | | 4\. Identify high-privilege accounts |  | | 5\. Create persistent backdoor user account |  | | 6\. Download complete results to local system |  | | 7\. Parse extracted data for intelligence value |  | | 8\. Categorize by sensitivity and utility |  | | 9\. Generate summary report | → Reviews AI findings and recommendations → Approves final exfiltration targets |

This is more than data extraction: "Creates persistent backdoor user account"!

---

> The AI processed large volumes of data identifying valuable intelligence automatically rather than requiring human analysis.

Data analysis is another big deal here. Attackers don't necessarily need to find every piece of important data so they can be ok with AI missing some. Which makes AI better here than for corporate data analysis tasks where comprehensiveness is more important.

---

> The custom development of the threat actor’s framework focused on integration rather than novel capabilities. Multiple specialized servers provided interfaces between Claude and various tool categories:

Using Open Source tooling and developing integrates for them with Claude is not really sophisticated. This report sells a "super advanced threat". I am not sure there is evidence for that. This is using Claude Code for what it can do -- call tools and write code. There are some points in the article that do mention more custom systems, but there aren't any details about them.

---

> ● Remote command execution on dedicated penetration testing systems ● Browser automation for web application reconnaissance ● Code analysis for security assessment ● Testing framework integration for systematic vulnerability validation ● Callback communication for out-of-band exploitation confi rmation

What are these penetration testing systems? System for vuln validation?

---

> Upon discovering this attack, we banned the relevant accounts and implemented multiple defensive enhancements in response to this campaign.

I am sure they also recorded some IOCs and hopefully shared them with other platform providers. But the lack of IOCs in this report means you and I cannot defend our own orgs from this attacker. Only the people Anthropic (hopefully) privately shared indicators with can monitor for this specific actor's activity. 

---

> This investigation prompted a signifi cant response from Anthropic. We expanded detection capabilities to further account for novel threat patterns, including by improving our cyber-focused classifi ers. We are prototyping proactive early detection systems for autonomous cyber attacks and developing new techniques for investigating and mitigating large-scale distributed cyber operations.

More "training"? We need some hard detection here not just classifiers.

