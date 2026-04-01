---
date: '2025-08-08'
description: Zenity researchers revealed at Black Hat that widely adopted enterprise
  AI assistants, including ChatGPT and Microsoft Copilot, can be exploited for data
  theft and manipulation through prompt injection attacks. For instance, attackers
  can craft malicious files or messages that the AI processes autonomously, retrieving
  sensitive data like API keys or modifying customer records. Though vulnerabilities
  in ChatGPT and Copilot have been patched, similar weaknesses in other tools remain
  unaddressed. This showcases the growing security risks associated with integrating
  generative AI into enterprise applications, necessitating robust defenses against
  evolving threat vectors.
link: https://www.securityweek.com/major-enterprise-ai-assistants-abused-for-data-theft-manipulation/
tags:
- prompt injection
- data theft
- enterprise tools
- AI security
- cybersecurity
title: Major Enterprise AI Assistants Can Be Abused for Data Theft, Manipulation -
  SecurityWeek
---

### SECURITYWEEK NETWORK:

### ICS:

[![SecurityWeek](https://www.securityweek.com/wp-content/uploads/2022/04/SecurityWeek-Small-Dark.png)](https://www.securityweek.com/)

Connect with us

Hi, what are you looking for?

![Enterprise AI data theft](https://www.securityweek.com/wp-content/uploads/2025/08/AI-assistant-chatbot-artificial-intelligence.jpg)

**Researchers at AI security startup Zenity demonstrated how several widely used enterprise AI assistants can be abused by threat actors to steal or manipulate data.**

The [Zenity](https://www.securityweek.com/zenity-raises-38-million-to-secure-agentic-ai/) researchers showcased their findings on Wednesday at the Black Hat conference. They shared several examples of how AI assistants can be leveraged — in some cases without any user interaction — to do the attacker’s bidding.

Enterprise tools are increasingly integrated with generative AI to boost productivity, but this also opens cybersecurity holes that could be highly valuable to threat actors.

For instance, security experts demonstrated in the past how the integration between Google’s Gemini gen-AI and Google Workspace productivity tools can be [abused](https://www.securityweek.com/ai-security-firm-shows-how-threat-actors-could-abuse-google-gemini-for-workspace/) through prompt injection attacks for [phishing](https://www.securityweek.com/google-gemini-tricked-into-showing-phishing-message-hidden-in-email/).

Researchers at Zenity showed last year how they could [hijack Microsoft Copilot for M365](https://labs.zenity.io/p/rce) by planting specially crafted instructions in emails, Teams messages or calendar invites that the attacker assumed would get processed by the chatbot.

This year, Zenity’s experts disclosed similar [attack methods](https://labs.zenity.io/p/hsc25) targeting ChatGPT, Copilot, Cursor, Gemini, and Salesforce Einstein.

In the case of ChatGPT, the researchers targeted its integration with Google Drive, which enables users to query and analyze files stored on Drive. The attack involved sharing a specially crafted file — one containing hidden instructions for ChatGPT — with the targeted user (this requires only knowing the victim’s email address).

When the AI assistant was instructed by the victim to process the malicious file, the attacker’s instructions would be executed, without any interaction from the victim. Zenity demonstrated the risks by getting ChatGPT to search the victim’s Google Drive for API keys and exfiltrate them.

Advertisement. Scroll to continue reading.

In the case of Copilot Studio agents that engage with the internet — over 3,000 instances have been found — the researchers showed how an agent could be hijacked to exfiltrate information that is available to it. Copilot Studio is used by some organizations for customer service, and Zenity showed how it can be abused to obtain a company’s entire CRM.

When Cursor is integrated with Jira MCP, an attacker can create malicious Jira tickets that instruct the AI agent to harvest credentials and send them to the attacker. This is dangerous in the case of email systems that automatically open Jira tickets — hundreds of such instances have been found by Zenity.

In a demonstration targeting Salesforce’s Einstein, the attacker can target instances with case-to-case automations — again hundreds of instances have been found. The threat actor can create malicious cases on the targeted Salesforce instance that hijack Einstein when they are processed by it. The researchers showed how an attacker could update the email addresses for all cases, effectively rerouting customer communication through a server they control.

In a Gemini attack demo, the experts showed how prompt injection can be leveraged to get the gen-AI tool to display incorrect information. In Zenity’s example, the attacker got Gemini to provide a bank account owned by the attacker when the victim requested a certain customer’s account.

The ChatGPT and Copilot Studio weaknesses have been patched, but the rest have been flagged as ‘won’t fix’ by vendors, according to Zenity.

**UPDATE:** “We have recently deployed new, layered defenses that fix this type of issue. Having a layered defense strategy against prompt injection attacks is crucial – see our recent [blog post](https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html) with detail on the protections we’ve deployed to keep our users safe.” – a Google spokesperson told _SecurityWeek_.

Google also said it takes prompt injection attack defenses seriously, but pointed out that currently this is largely an area of intensive academic research involving hypothetical attacks, and the technique is rarely seen in the wild as adversarial activity.

Salesforce also told _SecurityWeek_ that it has patched the flaw. A Salesforce spokesperson said, “Salesforce is aware of the vulnerability reported by Zenity and fixed the specific issue on July 11, 2025. The fix has been tested and this issue is no longer exploitable. The security landscape for prompt injection remains a complex and evolving area, and we will continue to invest in strong security controls and work closely with the research community to help protect our customers as these types of issues surface. For more details on how to maintain trust and security with Agentforce actions, see \[ [help page](https://help.salesforce.com/s/articleView?id=ai.service_agent_secure_actions.htm&type=5)\].”

**Related**: [Vibe Coding: When Everyone’s a Developer, Who Secures the Code?](https://www.securityweek.com/vibe-coding-when-everyones-a-developer-who-secures-the-code/)

**Related**: [AI Guardrails Under Fire: Cisco’s Jailbreak Demo Exposes AI Weak Points](https://www.securityweek.com/ai-guardrails-under-fire-ciscos-jailbreak-demo-exposes-ai-weak-points/)

**Related**: [Google Gemini Tricked Into Showing Phishing Message Hidden in Email](https://www.securityweek.com/google-gemini-tricked-into-showing-phishing-message-hidden-in-email/)

![](https://www.securityweek.com/wp-content/uploads/2023/11/Ed-Kovacs.jpg)

Written By[Eduard Kovacs](https://www.securityweek.com/contributors/eduard-kovacs/ "Posts by Eduard Kovacs")

Eduard Kovacs (@EduardKovacs) is a managing editor at SecurityWeek. He worked as a high school IT teacher for two years before starting a career in journalism as Softpedia’s security news reporter. Eduard holds a bachelor’s degree in industrial informatics and a master’s degree in computer techniques applied in electrical engineering.

## More from [Eduard Kovacs](https://www.securityweek.com/contributors/eduard-kovacs/ "Posts by Eduard Kovacs")

- [Trend Micro Warns of Apex One Vulnerabilities Exploited in Wild](https://www.securityweek.com/trend-micro-patches-apex-one-vulnerabilities-exploited-in-wild/)
- [Microsoft’s Project Ire Autonomously Reverse Engineers Software to Find Malware](https://www.securityweek.com/microsofts-project-ire-autonomously-reverse-engineers-software-to-find-malware/)
- [Cisco Says User Data Stolen in CRM Hack](https://www.securityweek.com/cisco-says-user-data-stolen-in-crm-hack/)
- [Nvidia Triton Vulnerabilities Pose Big Risk to AI Models](https://www.securityweek.com/nvidia-triton-vulnerabilities-pose-big-risk-to-ai-models/)
- [Cybersecurity M&A Roundup: 44 Deals Announced in July 2025](https://www.securityweek.com/cybersecurity-ma-roundup-44-deals-announced-in-july-2025/)
- [Gene Sequencing Giant Illumina Settles for $9.8M Over Product Vulnerabilities](https://www.securityweek.com/gene-sequencing-giant-illumina-settles-for-9-8m-over-product-vulnerabilities/)
- [Echo Raises $15M in Seed Funding for Vulnerability-Free Container Images](https://www.securityweek.com/echo-raises-15m-in-seed-funding-for-vulnerability-free-container-images/)
- [$1 Million Offered for WhatsApp Exploit at Pwn2Own Ireland 2025](https://www.securityweek.com/1-million-offered-for-whatsapp-exploit-at-pwn2own-ireland-2025/)

## Latest News

- [SonicWall Says Recent Attacks Don’t Involve Zero-Day Vulnerability](https://www.securityweek.com/sonicwall-says-recent-attacks-dont-involve-zero-day-vulnerability/)
- [Black Hat USA 2025 – Summary of Vendor Announcements (Part 3)](https://www.securityweek.com/black-hat-usa-2025-summary-of-vendor-announcements-part-3/)
- [Air France, KLM Say Hackers Accessed Customer Data](https://www.securityweek.com/air-france-klm-say-hackers-accessed-customer-data/)
- [Organizations Warned of Vulnerability in Microsoft Exchange Hybrid Deployment](https://www.securityweek.com/organizations-warned-of-vulnerability-in-microsoft-exchange-hybrid-deployment/)
- [New HTTP Request Smuggling Attacks Impacted CDNs, Major Orgs, Millions of Websites](https://www.securityweek.com/new-http-request-smuggling-attacks-impacted-cdns-major-orgs-millions-of-websites/)
- [Enterprise Secrets Exposed by CyberArk Conjur Vulnerabilities](https://www.securityweek.com/enterprise-secrets-exposed-by-cyberark-conjur-vulnerabilities/)
- [Google Discloses Data Breach via Salesforce Hack](https://www.securityweek.com/google-discloses-salesforce-hack/)
- [PLoB: A Behavioral Fingerprinting Framework to Hunt for Malicious Logins](https://www.securityweek.com/plob-a-behavioral-fingerprinting-framework-to-hunt-for-malicious-logins/)

![](https://www.securityweek.com/wp-content/uploads/2022/04/SecurityWeek-Small-Dark.png)

#### Trending

## Daily Briefing Newsletter

Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insightful columns from industry experts.

[**Event: AI Risk Summit at the Ritz-Carlton, Half Moon Bay**](https://www.airisksummit.com/)

August 19-20, 2025


The AI Risk Summit brings together security and risk management executives, AI researchers, policy makers, software developers and influential business and government stakeholders.

[Learn More](https://www.airisksummit.com/)

[**Virtual Event: CodeSecCon**](https://register.securityweek.com/codeseccon)

August 12-13, 2025


CodeSecCon is the premier virtual event bringing together developers and cybersecurity professionals to revolutionize the way applications are built, secured, and maintained.

[Register](https://register.securityweek.com/codeseccon)

#### People on the Move

Huntress has appointed former CISA Director Jen Easterly to its Strategic Advisory Board.

Bugcrowd has appointed CISO Trey Ford as its Chief Strategy and Trust Officer.

Agentic AI security company Noma Security has appointed Diana Kelley as CISO and Mavi Grizer as VP of Customer Success.

[More People On The Move](https://www.securityweek.com/industry-moves)

#### Expert Insights

[**Who’s Really Behind the Mask? Combatting Identity Fraud**](https://www.securityweek.com/whos-really-behind-the-mask-combatting-identity-fraud/)

![](https://www.securityweek.com/wp-content/uploads/2024/07/Etay_Maor-Cado-Networks.jpg)Why context, behavioral baselines, and multi-source visibility are the new pillars of identity security in a world where credentials alone no longer cut it. [(Etay Maor)](https://www.securityweek.com/contributors/etay-maor/)

[**From Ex Machina to Exfiltration: When AI Gets Too Curious**](https://www.securityweek.com/from-ex-machina-to-exfiltration-when-ai-gets-too-curious/)

![](https://www.securityweek.com/wp-content/uploads/2023/09/Danelle-Au.jpeg)From prompt injection to emergent behavior, today’s curious AI models are quietly breaching trust boundaries. [(Danelle Au)](https://www.securityweek.com/contributors/danelle-au/)

[**Reclaiming Control: How Enterprises Can Fix Broken Security Operations**](https://www.securityweek.com/reclaiming-control-how-enterprises-can-fix-broken-security-operations/)

![](https://www.securityweek.com/wp-content/uploads/2022/04/Josh-Goldfarb-F5.jpeg)Once a manageable function, security operations has become a battlefield of complexity. [(Joshua Goldfarb)](https://www.securityweek.com/contributors/joshua-goldfarb/)

[**What Can Businesses Do About Ethical Dilemmas Posed by AI?**](https://www.securityweek.com/what-can-businesses-do-about-ethical-dilemmas-posed-by-ai/)

![](https://www.securityweek.com/wp-content/uploads/2024/07/Stu-Sjouwerman-KnowBe4.jpg)AI-made decisions are in many ways shaping and governing human lives. Companies have a moral, social, and fiduciary duty to responsibly lead its take-up. [(Stu Sjouwerman)](https://www.securityweek.com/contributors/stu-sjouwerman/)

[**Like Ransoming a Bike: Organizational Muscle Memory Drives the Most Effective Response**](https://www.securityweek.com/like-ransoming-a-bike-organizational-muscle-memory-drives-the-most-effective-response/)

![](https://www.securityweek.com/wp-content/uploads/2025/01/Trevin-Edgeworth.jpg)Ransomware is a major threat to the enterprise. Tools and training help, but survival depends on one thing: your organization’s muscle memory to respond fast and recover stronger. [(Trevin Edgeworth)](https://www.securityweek.com/contributors/trevin-edgeworth/)

[Share on Facebook](https://www.securityweek.com/major-enterprise-ai-assistants-abused-for-data-theft-manipulation/# "Share on Facebook")[Tweet This Post](https://www.securityweek.com/major-enterprise-ai-assistants-abused-for-data-theft-manipulation/# "Tweet This Post")- [Flipboard](https://www.securityweek.com/major-enterprise-ai-assistants-abused-for-data-theft-manipulation/# "Share on Flipboard") [Reddit](https://www.securityweek.com/major-enterprise-ai-assistants-abused-for-data-theft-manipulation/# "Share on Reddit") [Whatsapp](https://web.whatsapp.com/send?text=Major%20Enterprise%20AI%20Assistants%20Can%20Be%20Abused%20for%20Data%20Theft,%20Manipulation%20https://www.securityweek.com/major-enterprise-ai-assistants-abused-for-data-theft-manipulation/) [Whatsapp](whatsapp://send?text=Major%20Enterprise%20AI%20Assistants%20Can%20Be%20Abused%20for%20Data%20Theft,%20Manipulation%20https://www.securityweek.com/major-enterprise-ai-assistants-abused-for-data-theft-manipulation/) [Email](mailto:?subject=Major%20Enterprise%20AI%20Assistants%20Can%20Be%20Abused%20for%20Data%20Theft,%20Manipulation&BODY=I%20found%20this%20article%20interesting%20and%20thought%20of%20sharing%20it%20with%20you.%20Check%20it%20out:%20https://www.securityweek.com/major-enterprise-ai-assistants-abused-for-data-theft-manipulation/)

## Daily Briefing Newsletter

Subscribe to the SecurityWeek Email Briefing to stay informed on the latest cybersecurity
news, threats, and expert insights. Unsubscribe at any time.


Close
