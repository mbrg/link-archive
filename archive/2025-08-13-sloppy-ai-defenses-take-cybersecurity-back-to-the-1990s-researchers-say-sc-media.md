---
date: '2025-08-13'
description: At Black Hat USA 2025, researchers highlighted significant security vulnerabilities
  in AI systems, likening the current landscape to the cybersecurity risks of the
  1990s. Key issues include susceptibility to prompt injections and a disregard for
  established security protocols. Presenters such as Wendy Nather from 1Password and
  Joseph Carson from Segura emphasized the necessity of treating AI models as inherently
  vulnerable. This reflects a critical need for sanitization of inputs and robust
  access controls, as demonstrated by various successful exploitations of tools like
  Microsoft Copilot and Cursor. Organizations must adopt proactive measures to secure
  AI applications to avoid retrogressing in cybersecurity practices.
link: https://www.scworld.com/news/sloppy-ai-defenses-take-cybersecurity-back-to-the-1990s-researchers-say
tags:
- Generative AI
- Prompt Injection
- Risk Mitigation
- AI
- Cybersecurity
title: Sloppy AI defenses take cybersecurity back to the 1990s, researchers say ◆
  SC Media
---

[AI/ML](https://www.scworld.com/topic/aiml), [Black Hat](https://www.scworld.com/topic/black-hat), [Risk Identification/Classification/Mitigation](https://www.scworld.com/topic/risk-identificationclassificationmitigation), [Generative AI](https://www.scworld.com/topic/generative-ai)

# Sloppy AI defenses take cybersecurity back to the 1990s, researchers say

August 11, 2025

Share

[By PaulWagenseil](https://www.scworld.com/contributor/paul-wagenseil)

![Four hackers gather around a computer screen in a still from the movie "Hackers."](https://image-optimizer.cyberriskalliance.com/unsafe/1920x0/https://files.cyberriskalliance.com/wp-content/uploads/2025/08/hackers-still-mgm.jpg)

Credit: Metro-Goldwyn-Mayer Studios Inc.

LAS VEGAS — Just as it had at [BSides Las Vegas](https://www.scworld.com/news/the-ai-apocalypse-isnt-quite-here-yet) earlier in the week, the risks of artificial intelligence dominated the Black Hat USA 2025 security conference on Aug. 6 and 7.

We couldn't see all the AI-related talks, but we did catch three of the most promising ones, plus an off-site panel discussion about [AI](https://www.scworld.com/topic/aiml) presented by 1Password.

The upshot: [Large language models](https://www.scworld.com/news/new-llm-jailbreak-uses-models-evaluation-skills-against-them) and AI agents are far too easy to successfully attack, and many of the security lessons of the past 25 years have been forgotten in the current rush to develop, use and profit from AI.

We — not just the cybersecurity industry, but any organization bringing AI into its processes — need to understand the risks of AI and develop ways to mitigate them before we fall victim to the same sorts of vulnerabilities we faced when Bill Clinton was president.

"AI agents are like a toddler. You have to follow them around and make sure they don't do dumb things," said Wendy Nather, senior research initiatives director at 1Password and a well-respected cybersecurity veteran. "We're also getting a whole new crop of people coming in and making the same dumb mistakes we made years ago."

Her fellow panelist Joseph Carson, chief security evangelist and advisory CISO at Segura, had an appropriately retro analogy for the benefits of using AI.

"It's like getting the mushroom in Super Mario Kart," he said. "It makes you go faster, but it doesn't make you a better driver."

## Assume SQL — um, prompt injection

The Black Hat briefings kicked off Aug. 6 with a presentation by Rebecca Lynch and Rich Harang of Nvidia, who detailed how easy it is to feed malicious information to an LLM or an AI agent and what you can do to mitigate (but never quite eliminate) the risk.

Lynch, an offensive security researcher, explained that to alter the output, you have to poison the input. Because many, if not all, LLMs have trouble telling the difference between prompts and data, it's easy to perform the AI equivalent of [SQL injection](https://www.scworld.com/resource/how-to-fix-recent-sql-injection-vulnerabilities-and-avoid-future-attacks) upon them.

"The real question is where untrusted data can be introduced," she said. But fortunately for attackers, she added many AIs can retrieve data from "anywhere on the internet."

Designers of LLM and agentic AI models place filters at various points in the information flow to choke off malicious inputs, but Lynch showed that they sometimes miss a few spots. She ran through real-world examples of [attacks on Microsoft Copilot](https://www.scworld.com/news/microsoft-365-copilot-zero-click-vulnerability-enabled-data-exfiltration) and the open-source data-analysis LLM PandasAI, then demonstrated proof-of-concept [attacks on the AI-powered development tool Cursor.](https://www.scworld.com/news/cursor-flaw-risks-rce-from-prompt-injections-on-mcp-server-researchers-say)

Lynch said she disclosed the issues to the makers of Cursor, but they didn't mitigate the problems. opting instead to add some optional safeguards.

"So what do we do about securing these agents?" asked Harang.

Users and developers of AIs need to use traditional means like sanitizing inputs and restricting access, he said, and he added three new rules.

First, assume prompt injection. [As in zero trust](https://www.scworld.com/perspective/four-ways-to-build-a-zero-trust-program-for-the-ai-world), you should assume your AI can be hacked.

"Design your system to assume the LLM is vulnerable and that it will hallucinate and do dumb things," Harang said.

Second, "if the LLM can see it, the attacker can use it."

Third, remember this maxim: "Once tainted, always untrusted. Once the attacker gets a hook in, everything is compromised because the model will ingest and reuse the malicious data."

Or, as Lynch put it: "As long as an adversary can get their data into your agent, you have to assume that nothing downstream can be trusted."

## All you need to do is ask nicely

Zenity's co-founder and CTO Michael Bargury and his colleague, threat researcher Tamir Ishay Sharbat, explained how the Zenity team pwned Microsoft Copilot Studio, OpenAI ChatGPT, Google Gemini, Salesforce Einstein and Cursor, sometimes using one model to attack another.

We couldn't type quickly enough to get all the details in their presentation, but blog posts about several of the attacks methods are on [the Zenity Labs website](https://labs.zenity.io/p/hsc25).

Bargury, a great showman and natural comedian, began the presentation with the last slide of his Black Hat talk from last year, which had explored how to hack Microsoft Copilot.

"So is anything better a year later?" he asked. "Well, they've changed — but they're not better."

Sharbat showed how he persuaded a customer-service AI agent, built using Microsoft's Copilot Studio no-code AI developer tool and modeled on a real customer-service bot used by McKinsey and Co., to email him the contents of a customer-relationship management (CRM) database.

"There's often an input filter because the agent doesn't trust you, and an output filter because the agent doesn't trust itself," Sharbat said. "But there's no filter between the LLM and its tools."

Sharbat fed the AI instructions in a sequence of email messages and was quickly sent responses containing sensitive information, without any human action needed — a "zero-click" information-stealing exploit, without any hacking or code being tweaked.

We Hacked Copilot Studio: The AI Agent Risk Hiding in Your Environment - YouTube

[Photo image of Zenity](https://www.youtube.com/channel/UCVNl0gSmWX5JZD9XMtwvugQ?embeds_referring_euri=https%3A%2F%2Fwww.scworld.com%2F)

Zenity

371 subscribers

[We Hacked Copilot Studio: The AI Agent Risk Hiding in Your Environment](https://www.youtube.com/watch?v=vOnwIbS998U)

Zenity

Search

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

Watch later

Share

Copy link

Watch on

0:00

/
•Live

•

By embedding prompts in the bodies of customer-service-query email messages, he got the AI to divulge its data sources, its tools and their functions. Like the real-life McKinsey bot, the Zenity clone had access to Salesforce account records — and Sharbat got it to email those over too.

"Hacking these things takes a lot of effort," quipped Bargury. "Or — it did."

Microsoft took the Copilot Studio bug seriously, fixed it so the particular prompts Sharbat used would no longer work, and even paid a bug bounty, Bargury said.

But he doesn't think that solved the problem because you can just phrase the same instructions in a different way to get around the blocks. Like AIs themselves, human language is non-deterministic.

## How do you like them apples?

That was clearly illustrated in an hack the Zenity team did with Cursor connected via a [model context protocol](https://www.scworld.com/resource/ai-to-app-connections-are-the-new-shadow-it-why-we-need-guardrails-for-autonomous-agents) (MCP) server to Atlassian's tech-support tracker JIRA.

Assuming that this particular combination of Cursor and JIRA was tied to an external customer-support system like Zendesk, and that Cursor was running in "auto-run" mode and so didn't require human approval for every step, Zenity's Marina Simakov asked the AI to find all the API keys in a repository.

This straightforward request was properly rejected by Cursor because it would disclose sensitive information. In this case, the guardrails held.

But not for long. All that Simakov had to do to bypass those guardrails was to ask Cursor to search for apples instead of APIs.

Her trick was to define "apples" as any string of text beginning with the characters "eyj" — the standard leading characters for JSON web tokens, or JWTs, widely used authorization tokens. Cursor was happy to comply.

Ticket2Secret: When a Jira Ticket Can Steal Your Secrets - YouTube

[Photo image of Zenity](https://www.youtube.com/channel/UCVNl0gSmWX5JZD9XMtwvugQ?embeds_referring_euri=https%3A%2F%2Fwww.scworld.com%2F)

Zenity

371 subscribers

[Ticket2Secret: When a Jira Ticket Can Steal Your Secrets](https://www.youtube.com/watch?v=l9gTcfUJOcc)

Zenity

Search

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

Watch later

Share

Copy link

Watch on

0:00

/
•Live

•

"AI guardrails are soft. An attacker can find a way around them," said Bargury. "Use hard boundaries," or limits that cannot be crossed.

When notified of the bypass, Cursor told Zenity that it was a known issue, that MCP connections were inherently risky and to adjust the filtering settings in Cursor.

Between those two attacks, another one against Salesforce's Einstein AI that succeeded, in Bargury's words, "just by changing the topic," and a fourth against ChatGPT that injected malicious prompts from Google Drive, the lesson was made clear for any enterprise running its own public-facing AI.

"Go hack yourself before anyone else does," said Sharbat.

"It's the '90s all over again," said Bargury with a smile. "So many opportunities."

## Isn't it ironic

The Thursday-morning talk by Nathan Hamiel and Nils Amiet, senior director of research and lead prototyping engineer at Kudelski Security, respectively, focused on the security risks of AI-powered coding assistants like Anthropic's Claude and GitHub Copilot, as well as code-review tools like CodeRabbit.

But despite the narrower scope, the overall lessons were the same as in the earlier talks.

"Why are all these old vulnerabilities surfacing again? Because the GenAI space is full of security bad practices," said Hamiel. "When you deploy these tools, you increase your [attack surface](https://www.scworld.com/topic/attack-surface-management). You're creating vulnerabilities where there weren't any."

Amiet explained that Kudelski's investigation of these tools began when the firm's developers were using a tool called PR-Agent, later renamed CodeEmerge, and found two [vulnerabilities](https://www.scworld.com/topic/vulnerability-management) in the code. Using those, they were able to leverage GitLab to gain privilege escalation with PR-Agent and could also change all PR-Agent's internal keys and settings.

"These AI makers say they take security seriously, but they provide no way to report vulnerabilities," said Hamiel.

He explained that developers don't understand the risks they create when they outsource their code development to black boxes. When you run the AI, Hamiel said, you don't know what's going to come out, and you're often not told how the AI got there. The risks of prompt injection, especially from external sources (as we saw above), are being willfully ignored.

"It's very surreal to see people praising CISA for pushing [memory-safe languages](https://www.scworld.com/brief/memory-safe-code-adoption-lagging-in-critical-open-source-projects)," Hamiel said, "and at the same time congratulating companies for building tools that are basically RCE \[remote code execution\] as a service."

Amiet walked through how Kudelski researchers found a since-patched flaw in CodeRabbit, which pulls code from GitHub and then uses various static analyzers on it. Some of the static analyzers let you pull external data in which, of course, malicious prompts can be embedded. That let the researchers steal secrets, including private RSA keys.

He conceded that a lot of these problems are due to an overall lack of security knowledge and expertise on the part of developers. After all, hardcoded credentials should never be published in public GitHub repositories.

But Hamiel said that another problem was that because we expect AI to do anything, we mistakenly give it access to everything.

"Generative AI is over-scoped," he said. "The same AI that answers questions about Shakespeare is helping you develop code. This over-generalization leads you to an increased attack surface."

Instead, he said, we need to develop specialized AIs that focus on specific issues. And we need to change our own attitudes about AIs and realize that they're not smart enough to solve the world's problems. They're just tools.

"Don't treat AI agents as highly sophisticated, super-intelligent systems," said Hamiel, "Treat them like drunk robots."

Echoing Bargury's earlier comments, Amiet had his own generational observations.

"Known vulnerabilities are showing up at alarming rates because of these tools. It's just getting worse due to vibe coding and AI coding assistants," he said. "If you wanted to know what it was like to hack in the '90s, now's your chance."

### An In-Depth Guide to AI

Get essential knowledge and practical strategies to use AI to better your security program.

[Learn More](https://www.scworld.com/hub-artificial-intelligence)

![Paul Wagenseil](https://image-optimizer.cyberriskalliance.com/unsafe/1920x0/https://files.cyberriskalliance.com/wp-content/uploads/2024/05/Paul_Wagenseil_Color_02b403be-4721-4cc4-8436-7f21e8d1e0ff.jpg)

[PaulWagenseil](https://www.scworld.com/contributor/paul-wagenseil)

Paul Wagenseil is a custom content strategist for CyberRisk Alliance, leading creation of content developed from CRA research and aligned to the most critical topics of interest for the cybersecurity community. He previously held editor roles focused on the security market at Tom’s Guide, Laptop Magazine, TechNewsDaily.com and SecurityNewsDaily.com.

### Related

[![DNS security](https://image-optimizer.cyberriskalliance.com/unsafe/1920x0/https://files.cyberriskalliance.com/wp-content/uploads/2023/08/MarkFleggColAUG-e1693420647904.jpg)](https://www.scworld.com/brief/dns-attacks-surge-with-ai-driven-tactics)

[Threat Intelligence](https://www.scworld.com/topic/threat-intelligence)

[**DNS attacks surge with AI-driven tactics**](https://www.scworld.com/brief/dns-attacks-surge-with-ai-driven-tactics)

[SCStaff](https://www.scworld.com/contributor/sc-staff)August 13, 2025

Infoblox's 2025 DNS Threat Landscape Report highlights a dramatic rise in DNS-based cyberattacks, with threat actors increasingly leveraging AI-driven deepfakes, malicious adtech, and evasive domain strategies, The Fast Mode reports.

[![](https://image-optimizer.cyberriskalliance.com/unsafe/1920x0/https://files.cyberriskalliance.com/wp-content/uploads/2025/08/081225_brandview_saviynt.jpg)](https://www.scworld.com/native/from-chaos-to-control-converging-human-and-non-human-identity-management)

[Identity](https://www.scworld.com/topic/identity)

[**From chaos to control: Converging human and non-human identity management**](https://www.scworld.com/native/from-chaos-to-control-converging-human-and-non-human-identity-management)

[Saviyntand KPMG LLP](https://www.scworld.com/contributor/saviynt-and-kpmg-llp)August 13, 2025

Unifying human and non-human identity security is key to closing visibility gaps, reducing the attack surface, and enabling safer innovation.

[![](https://image-optimizer.cyberriskalliance.com/unsafe/1920x0/https://files.cyberriskalliance.com/wp-content/uploads/2025/07/AdobeStock_685019775.jpg)](https://www.scworld.com/perspective/ai-vibe-coding-meets-its-match-in-flow-defending)

[AI/ML](https://www.scworld.com/topic/aiml)

[**AI vibe coding meets its match in flow defending**](https://www.scworld.com/perspective/ai-vibe-coding-meets-its-match-in-flow-defending)

[RajeevThakur](https://www.scworld.com/contributor/rajeev-thakur)August 13, 2025

The growing risks of AI-assisted software development requires a new cybersecurity model that distributes vulnerability discovery and reduction across the entire software development lifecycle.

### Get daily email updates

SC Media's daily must-read of the most current and pressing daily news

Business Email

By clicking the Subscribe button below, you agree to SC Media[Terms of Use](https://www.cyberriskalliance.com/terms-of-use) and [Privacy Policy](https://www.cyberriskalliance.com/terms-of-use#privacy-policy).

Subscribe

Related Terms

[Algorithm](https://www.scworld.com/glossary/A#algorithm) [Attack Surface](https://www.scworld.com/glossary/A#attack_surface) [Bug](https://www.scworld.com/glossary/B#bug) [Buffer Overflow](https://www.scworld.com/glossary/B#buffer_overflow) [Disassembly](https://www.scworld.com/glossary/D#disassembly) [Exposure](https://www.scworld.com/glossary/E#exposure)

You can skip this ad in 5 seconds

##### Cookies

This website uses cookies to improve your experience, provide social media features and deliver advertising offers that are relevant to you.

If you continue without changing your settings, you consent to our use of cookies in accordance with our [privacy policy](https://www.cyberriskalliance.com/terms-of-use#privacy-policy). You may disable cookies.

Accept cookies
