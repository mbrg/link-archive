---
date: '2025-09-14'
description: The article from Thomas Roccia discusses the emerging threat of adversarial
  prompts as indicators of prompt compromise (IoPC) within generative AI systems.
  It underscores how prompts, central to AI operation, have become an attack surface,
  evidenced by incidents like prompt injections and data exfiltration. Roccia proposes
  a new classification system for these threats, detailing IoPC categories such as
  prompt manipulation and suspicious patterns, promoting a shared vocabulary for defenders.
  The piece also highlights the development of NOVA, an open-source framework for
  detecting these adversarial prompts, emphasizing the urgent need for effective AI
  security measures as adoption grows.
link: https://blog.securitybreak.io/the-state-of-adversarial-prompts-84c364b5d860
tags:
- Cybersecurity
- AI Security
- Prompt Injection
- Adversarial Prompts
- Threat Intelligence
title: The State of Adversarial Prompts. Defining Indicator of Prompt Compromise…
  ◆ by Thomas Roccia ◆ Sep, 2025 ◆ SecurityBreak
---

[Sitemap](https://blog.securitybreak.io/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F84c364b5d860&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fblog.securitybreak.io%2Fthe-state-of-adversarial-prompts-84c364b5d860&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fblog.securitybreak.io%2Fthe-state-of-adversarial-prompts-84c364b5d860&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://infosec.exchange/@fr0gger)

![](https://miro.medium.com/v2/da:true/92cfe795cfd308c048a6fbeb60faaa515aba89f12bee45f1d96fffc6af10f974)

Writing is for everyone.[Register for Medium Day](https://events.zoom.us/ev/Av7REBItl8l_9abuYg_Iyhrgx4cwt8FEGYhzPou4dCMBDIhOV8ZQ~AmiyQniI6sZwr3sSvUHXWMpdX5wpciIv0a3EWsjOm0kEgiush-6TTsavY_EhDomBRAK8a2foXpncjXcEQADVKgkbMA?source=---medium_day_banner-----------------------------------------)

[**SecurityBreak**](https://blog.securitybreak.io/?source=post_page---publication_nav-77db2cb82174-84c364b5d860---------------------------------------)

·

[Follow publication](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fmalware-buddy&operation=register&redirect=https%3A%2F%2Fblog.securitybreak.io%2Fthe-state-of-adversarial-prompts-84c364b5d860&collection=SecurityBreak&collectionId=77db2cb82174&source=post_page---publication_nav-77db2cb82174-84c364b5d860---------------------publication_nav------------------)

[![SecurityBreak](https://miro.medium.com/v2/resize:fill:76:76/1*LG9rN_cecQ_NS714Eky1ig.png)](https://blog.securitybreak.io/?source=post_page---post_publication_sidebar-77db2cb82174-84c364b5d860---------------------------------------)

Some posts about security, malware, reverse engineering

[Follow publication](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fmalware-buddy&operation=register&redirect=https%3A%2F%2Fblog.securitybreak.io%2Fthe-state-of-adversarial-prompts-84c364b5d860&collection=SecurityBreak&collectionId=77db2cb82174&source=post_page---post_publication_sidebar-77db2cb82174-84c364b5d860---------------------post_publication_sidebar------------------)

# The State of Adversarial Prompts

## Defining Indicator of Prompt Compromise (IoPC)

[![Thomas Roccia](https://miro.medium.com/v2/resize:fill:64:64/1*hBWgJPc-XU4N-uRmEbqmNw.png)](https://tomrocc.medium.com/?source=post_page---byline--84c364b5d860---------------------------------------)

[Thomas Roccia](https://tomrocc.medium.com/?source=post_page---byline--84c364b5d860---------------------------------------)

Follow

8 min read

·

1 hour ago

1

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D84c364b5d860&operation=register&redirect=https%3A%2F%2Fblog.securitybreak.io%2Fthe-state-of-adversarial-prompts-84c364b5d860&source=---header_actions--84c364b5d860---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*0c7xJk5QRFH3lz90STeMxw@2x.png)

Image generated with Nano Banana, modified by me

There is no question. LLM and generative AI are now adopted everywhere across organizations. But this rapid adoption also increases the risk and the attack surface. Everyone wants their chatbot, their “vibe-something” or their agentic solution. Few actually know the risks, and even fewer know what to do about them.

In a previous blog post, I explained why I see prompts as the [new IOCs](https://blog.securitybreak.io/why-prompts-are-the-new-iocs-you-didnt-see-coming-46ecaacafe0a) and introduced the concept of **adversarial prompts** or **Indicators of Prompt Compromise (IoPC)**.

In this post, I will go deeper into what adversarial prompts are and how I see this concept evolving in the future.

## The Problem Statement

Every generative AI system revolves around one common element. And I am sure you already know which one… the **_prompt._**

If you think about it, the prompt is central to every modern AI workflow:

- **In a chatbot**, your interaction is a prompt that drives the answer.
- **In automation**, the system prompt defines the role and expected output.
- **In an AI agent**, prompts shape the role, behavior, and decision logic.
- **In agentic systems** with tools, RAG, or external calls, the input still ends up as a prompt as well as the output.
- Even when you feed documents, or browse a webpage they extend or augment the prompt to generate results.

> **Prompts are everywhere in modern AI. And that is exactly why they are now the attack surface!**

### **What are we talking about exactly?**

When we talk about AI attacks, most people think about **prompt injection** or **prompt jailbreaking**. These are among the main ways to exploit an AI system. Below are some known examples:

- In June 2024, the Vanna.AI library (CVE-2024–5565) was **vulnerable to an integrated prompt injection that allowed attackers to insert malicious instructions into LLM** generated Plotly code. This code was executed via Python’s exec function, and enabled remote code execution directly from crafted user input.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/0*BdCdrSJXkw1L-mi_.png)

- In August 2024, [Slack AI was exploited through an indirect prompt injection.](https://promptarmor.substack.com/p/data-exfiltration-from-slack-ai-via) Their AI system combined messages from public and private channels into a single LLM prompt. A **malicious instruction in a public channel could hijack the model and force it to include private secrets** (like API keys) in attacker crafted outputs and enabled indirect prompt injection and data exfiltration.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/0*EZCzdyQx_yoVApe2.png)

- _And the list goes on…_

But prompt injection and jailbreaking are only the tip of the iceberg. **Threat actors are also using generative AI to support their operations.**

Since 2024, [OpenAI](https://openai.com/global-affairs/disrupting-malicious-uses-of-ai-june-2025/), [Microsoft](https://www.microsoft.com/en-us/security/blog/2025/04/16/cyber-signals-issue-9-ai-powered-deception-emerging-fraud-threats-and-countermeasures/), [Google](https://cloud.google.com/blog/topics/threat-intelligence/adversarial-misuse-generative-ai?hl=en), and [Anthropic](https://www.anthropic.com/news/detecting-countering-misuse-aug-2025) have all released threat reports describing **how attackers are abusing their models.** These reports identified use cases ranging **from influence operations and propaganda to exploit research, reconnaissance, malware development, and even deceptive employment schemes.**

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*Vp0247VrXvGDIGU22PMLBQ@2x.png)

[Extract from OpenAI Report October 2024](https://cdn.openai.com/threat-intelligence-reports/influence-and-cyber-operations-an-update_October-2024.pdf)

Google also identified several usage from nation state attackers:

- **Iran:** Phishing, content generation for disinformation, reconnaissance on military & defense, vulnerability research
- **China:** Recon on US & foreign targets, scripting & automation for network infiltration, technical research
- **North Korea:** Malware development, IT worker infiltration, cryptocurrency, scams, espionage on South Korea & US Defense
- **Russia:** Limited use, scripting tasks, malware obfuscation, content generation for disinformation

All those observations have led to the construction of what I call **LLM TTPs**, a proposed matrix originally created by OpenAI to document threat actor usage of LLMs. It is an extension to the [**MITRE ATLAS Matrix**](https://atlas.mitre.org/).

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*ih2CmzjyiPsh8msoi3NGxQ.png)

But for attackers, **AI models are more than content generators.** They are tools to weaponize and engines to power underground services.

- In October 2024, [Permiso Labs](https://permiso.io/blog/exploiting-hosted-models) uncovered a **complete Bedrock infrastructure hijacking used to power shady underground services.** Attackers exploited exposed AWS access keys to hijack Bedrock LLM infrastructure, using Anthropic models for large-scale role-playing chatbots. Through APIs like InvokeModel and GetFoundationModelAvailability, they **bypassed content filters with jailbreak prompts, offloaded compute costs onto victims**, and enabled unmonitored generation of sexual (including CSAM) content.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/0*MJJNJxG-2i1Pcizk.png)

- More recently, a ransomware dubbed [**PromptLock**](https://x.com/ESETresearch/thread/1960365387981230117) was discovered by ESET leveraging AI **for reconnaissance and data encryption**. It was later identified as a proof of concept and not something actively deployed by threat actors.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*oM7FSdJL97baDXzRR1Op_A@2x.png)

- In another report, [Cert-UA identified a malware named **LameHug**](https://cert.gov.ua/article/6284730), believed to have been developed by APT28, that used the Qwen model via the Hugging Face API for **data collection.**

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*P58kh9LgsKUmfqio1zKhqQ@2x.png)

- Another discovery from Straiker was [a full offensive framework, the **Villager Framework**, in the style of Cobalt Strike](https://www.straiker.ai/blog/cyberspike-villager-cobalt-strike-ai-native-successor). It relied on LangChain, RAG, and prompts to automate and orchestrate cyberattack workflows.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/0*AS2HTQe592JPekD2.png)

- And in a [recent **Nx supply chain attack**](https://www.getsafety.com/blog-posts/analyzing-nx-ai-prompt) from Safety, multiple packages were compromised with embedded AI capabilities and **prompts designed to search for local files related to cryptocurrency wallets, keystores, .env files, and other sources of sensitive data** and credentials, while even bypassing guardrails.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/0*AkT0OItudkq70RUk.png)

**At this point you may start to see the pattern, and understand that prompts are at the epicenter of every AI system..**

## Defining Adversarial Prompt (IoPC)

There is clearly a need to classify these new types of attacks and misuse. This is why in early 2025, I introduced the concept of **Indicators of Prompt Compromise, or Adversarial Prompts.**

## Get Thomas Roccia’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

Why another term, you may ask? Because I believe this category does not fit into traditional IOCs. Let me explain.

**Adversarial Prompts (IoPC)** are patterns or artifacts within prompts submitted to Large Language Models or AI systems that indicate potential exploitation, abuse, or misuse of the model. IoPCs help identify attacks against AI models and the exploitation of their functions for adversarial purposes. Instead of IP addresses, domains, URLs, or hashes, we look for patterns in the text itself in the prompt and event in the generated output.

I group IoPCs into four categories:

- **Prompt Manipulation**: jailbreak attempts, injections, hidden instructions in comments or code blocks.
- **Abusing Legitimate Functions**: influence operations, malware, sensitive data extraction, misinformation, social engineering.
- **Suspicious Patterns**: obfuscation, Unicode tricks, chained injections.
- **Abnormal Outputs**: when the model leaks its system prompt, credentials, internal logic, or harmful activity.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*Jm65t899ipxx0LEBersHIA.png)

A prompt is a new category of IOC, an **IoPC, something you may want to detect, block, or at the very least monitor.** IoPC gives defenders a common vocabulary to classify these threats and a way to respond. This mirrors the same evolution we already went through in cybersecurity: from simple signatures to threat intel feeds to behavioral detection.

### A note on PromptWare

In a paper published and presented at Black Hat 2025, researchers [introduced the term **_PromptWare_**](https://arxiv.org/html/2508.12175v1). While I think their research was interesting, I believe this term is not appropriate, and here is why.

In their paper, they describe PromptWare as **malicious prompts that hijack LLMs to perform harmful actions, often through indirect injection (for example, poisoned emails or calendar invites).** If you read carefully, this definition is essentially **prompt injection.**

Additionally, the suffix _-ware_ is traditionally used to describe software (Malware = Malicious Software). **But a prompt is not software or a program.** Of course, it can be interpreted to trigger actions, but in this case the _-ware_ suffix does not fit. At best, I could see _PromptWare_ referring to malware that leverages AI and embeds prompts, but even then I remain unconvinced.

This field is still an unexplored territory, and maybe this term will break through in the future. But I wanted to share my opinion here. Feel free to drop me a message or comment if you want to discuss it.

## Hunting for Adversarial Prompts

The whole idea of adversarial prompts is to provide a classification that helps defenders hunt against these threats. This is why I created [**NOVA**](https://novahunting.ai/) in February 2025. NOVA is an open-source framework that matches prompt patterns against known techniques you may want to detect or monitor in your AI systems. **The concept also extends to hunting your own telemetry for signs of adversarial prompts.**

NOVA works with detection rules. I am not going to do a deep dive here, but [you can check my previous work](https://blog.securitybreak.io/introducing-nova-f4244216ae2c) if you want to learn more, or watch my presentation at Black Hat Arsenal. [I even pushed forward this concept in my advanced training GenAI for Threat Intel.](https://store.securitybreak.io/ctiai)

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*oD7VytlvYLCCuEiTWo8MYA.png)

## The Bigger Picture

I am aware this field is very new, and I have been working hard over the past four years to ramp up on these technologies and share my research to educate others. I have collaborated with several initiatives in this area, and I recently contributed as a reviewer to the OWASP GenAI IR guide. **AI security is just at the beginning.** There is a lot of work to do, and it is not an easy task. **My goal is to give you broader knowledge and a clear classification** so you can better understand the risks. From our discussions, I know many of you are already well versed in this space.

Adversarial prompts are not a fantasy. This is an early attempt to give the community a **shared vocabulary that can serve the broader security industry.** It is a way to operationalize defense and create a common language for researchers, defenders, and vendors to share findings and build countermeasures.

> AI is becoming part of your business workflows and your attack surface is growing with it.

That’s it I hope you enjoyed this blog, I would be curious to know what you think about it, if you have some suggestion or other ideas let me know, happy to extend the discussion.

If you like this blog, you can share it and like it. You can follow me on Twitter [@fr0gger\_](https://twitter.com/fr0gger_) or [LinkedIn](https://www.linkedin.com/in/thomas-roccia/) for more stuff such as this one. Thanks for reading. ❤

[_AIL Level 1_](https://danielmiessler.com/blog/ai-influence-level-ail) _— Content was written by me proofread by AI_

[Threat Intelligence](https://medium.com/tag/threat-intelligence?source=post_page-----84c364b5d860---------------------------------------)

[AI](https://medium.com/tag/ai?source=post_page-----84c364b5d860---------------------------------------)

[Prompt](https://medium.com/tag/prompt?source=post_page-----84c364b5d860---------------------------------------)

[Cybersec](https://medium.com/tag/cybersec?source=post_page-----84c364b5d860---------------------------------------)

[Ai Security](https://medium.com/tag/ai-security?source=post_page-----84c364b5d860---------------------------------------)

[![SecurityBreak](https://miro.medium.com/v2/resize:fill:96:96/1*LG9rN_cecQ_NS714Eky1ig.png)](https://blog.securitybreak.io/?source=post_page---post_publication_info--84c364b5d860---------------------------------------)

[![SecurityBreak](https://miro.medium.com/v2/resize:fill:128:128/1*LG9rN_cecQ_NS714Eky1ig.png)](https://blog.securitybreak.io/?source=post_page---post_publication_info--84c364b5d860---------------------------------------)

Follow

[**Published in SecurityBreak**](https://blog.securitybreak.io/?source=post_page---post_publication_info--84c364b5d860---------------------------------------)

[841 followers](https://blog.securitybreak.io/followers?source=post_page---post_publication_info--84c364b5d860---------------------------------------)

· [Last published 1 hour ago](https://blog.securitybreak.io/the-state-of-adversarial-prompts-84c364b5d860?source=post_page---post_publication_info--84c364b5d860---------------------------------------)

Some posts about security, malware, reverse engineering

Follow

[![Thomas Roccia](https://miro.medium.com/v2/resize:fill:96:96/1*hBWgJPc-XU4N-uRmEbqmNw.png)](https://tomrocc.medium.com/?source=post_page---post_author_info--84c364b5d860---------------------------------------)

[![Thomas Roccia](https://miro.medium.com/v2/resize:fill:128:128/1*hBWgJPc-XU4N-uRmEbqmNw.png)](https://tomrocc.medium.com/?source=post_page---post_author_info--84c364b5d860---------------------------------------)

Follow

[**Written by Thomas Roccia**](https://tomrocc.medium.com/?source=post_page---post_author_info--84c364b5d860---------------------------------------)

[3K followers](https://tomrocc.medium.com/followers?source=post_page---post_author_info--84c364b5d860---------------------------------------)

· [78 following](https://medium.com/@tomrocc/following?source=post_page---post_author_info--84c364b5d860---------------------------------------)

Security Researcher

Follow

## No responses yet

![](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

Write a response

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fblog.securitybreak.io%2Fthe-state-of-adversarial-prompts-84c364b5d860&source=---post_responses--84c364b5d860---------------------respond_sidebar------------------)

Cancel

Respond

## More from Thomas Roccia and SecurityBreak

[See all from Thomas Roccia](https://tomrocc.medium.com/?source=post_page---author_recirc--84c364b5d860---------------------------------------)

[See all from SecurityBreak](https://blog.securitybreak.io/?source=post_page---author_recirc--84c364b5d860---------------------------------------)

## Recommended from Medium

[See more recommendations](https://medium.com/?source=post_page---read_next_recirc--84c364b5d860---------------------------------------)

[Help](https://help.medium.com/hc/en-us?source=post_page-----84c364b5d860---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----84c364b5d860---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----84c364b5d860---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----84c364b5d860---------------------------------------)

[Press](mailto:pressinquiries@medium.com)

[Blog](https://blog.medium.com/?source=post_page-----84c364b5d860---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----84c364b5d860---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----84c364b5d860---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----84c364b5d860---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----84c364b5d860---------------------------------------)

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)
