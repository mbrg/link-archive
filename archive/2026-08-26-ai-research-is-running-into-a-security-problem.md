---
date: '2026-08-26'
description: OpenAI is decelerating frontier model development to enhance security
  amid rising risks linked to advanced AI capabilities. This shift responds to recent
  incidents showcasing vulnerabilities and emphasizes the need for integrated cybersecurity
  within the AI research lifecycle. As AI models gain capabilities like executing
  code and interacting with networks, proactive security measures—such as sandboxing
  and access control—are crucial. The line between AI research and cybersecurity is
  increasingly blurred, necessitating a collaborative approach to mitigate risks while
  advancing AI functionalities essential for real-world applications.
link: https://www.groundlevel-ai.com/p/ai-research-is-running-into-a-security
tags:
- OpenAI
- machine learning
- AI research
- safety measures
- cybersecurity
title: AI research is running into a security problem
---

[![Ground Level AI](https://substackcdn.com/image/fetch/$s_!WzLV!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2fbef887-7f45-43d6-bf60-cfd47d23f6a2_256x256.png)](https://www.groundlevel-ai.com/)

# [![Ground Level AI](https://substackcdn.com/image/fetch/$s_!ZOqj!,e_trim:10:white/e_trim:10:transparent/h_72,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F542d8a81-96ed-45dd-86a2-a70f40c5b4a1_1500x500.png)](https://www.groundlevel-ai.com/)

SubscribeSign in

# AI research is running into a security problem

### OpenAI has slowed frontier model development as it hardens the environments where increasingly capable agents are trained, raising new questions about where AI research ends and cybersecurity begins.

[![Sharon Goldman's avatar](https://substackcdn.com/image/fetch/$s_!TgyN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46567afe-42bd-4d56-ac9a-3579582e6c22_2002x2002.jpeg)](https://substack.com/@sharongoldman)

[Sharon Goldman](https://substack.com/@sharongoldman)

Aug 20, 2026

∙ Paid

10

2

Share

[![](https://substackcdn.com/image/fetch/$s_!NsWA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7d97392-92d7-4edb-9c05-6b6c1530605a_1844x244.png)](http://www.codestrap.com/)

[![](https://substackcdn.com/image/fetch/$s_!hQZv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9c7d33bc-4373-4223-923e-fd019426ef8e_1672x941.png)](https://substackcdn.com/image/fetch/$s_!hQZv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9c7d33bc-4373-4223-923e-fd019426ef8e_1672x941.png)

At an OpenAI press briefing for dozens of reporters on Tuesday, right before the company announced it was [slowing its frontier model training](https://openai.com/index/pacing-model-development-cyber-capabilities/), vice president of research Mia Glaese and chief scientist Jakub Pachocki said the company was strengthening safety across three areas: monitoring, alignment, and “security and containment measures.”

They explained that the move was the result of three urgent developments — the [OpenAI-Hugging Face incident](https://www.groundlevel-ai.com/p/openai-gives-first-detailed-debrief); preliminary evidence that the company’s upcoming Astra model may meet the [Critical cybersecurity capability](https://openai.com/index/responding-next-frontier-critical-cyber-capabilities/?utm_source=chatgpt.com) threshold under its [Preparedness Framework](https://openai.com/index/updating-our-preparedness-framework/?utm_source=chatgpt.com); and the rapid pace of internal progress at OpenAI.

That made me wonder why there were no OpenAI security staff on the briefing? Where was the CISO, for example? In a call with an OpenAI spokesperson, I was told that that the reason was that the briefing was about research. “It was Jakob and Mia, this was ultimately a research call that was made,” she said. “Obviously security is a very important stakeholder who feeds into decisions that are made, but this is ultimately a research call to put on a pause.”

### The line between AI research and security is disappearing

But the distinction between AI research and security is becoming more and more blurred after the OpenAI-Hugging Face incident. After all, OpenAI is slowing frontier AI research in part because the security controls surrounding increasingly capable models need to catch up. As AI agents gain the ability to write and execute code, use tools and interact with real-world systems, cybersecurity is no longer simply about securing models after they are developed. It is becoming part of the research process itself and also a constraint on whether that research can proceed.

#### A message from our sponsor

##### [Codestrap](http://www.codestrap.com/)’s AI Value Factory delivers value-generating assets from repeatable factory-grade workflows. (A factory was always necessary to garner value from AI.)

Joshua Saxe, cofounder and CTO of Abundant Security and the former engineering lead for Llama security at Meta (check out our [GLAI podcast episode](https://www.groundlevel-ai.com/p/ground-level-ai-podcast-joshua-saxe)), told me the training slowdown makes “perfect sense” and hardening the research environments does too. But, he warned that it also exposes a fundamental tension: Frontier labs want to train agents to complete long, complicated tasks involving code execution, internet access, and external software. Those capabilities are essential to making agents genuinely useful in the real world, especially for software engineering and cybersecurity.

But the same access, he argued, also gives a misbehaving agent opportunities to go beyond its intended task, attack infrastructure, steal information, or interact with systems it was never supposed to reach.

“OpenAI is trying to preserve enough realism for agents to learn useful real-world behavior while preventing that realism from becoming a dangerous attack surface,” he said. “Stronger sandboxing, network isolation, access controls and reduced privileges are all sensible responses.”

This will require security to become more interwoven with AI research, he added. “LLMs under training are now writing and executing code and manipulating computers and network services,” he said. “This is how the Hugging Face incident started; agents just hacking their training infrastructure during normal training.” Going forward, he explained, training infrastructure “will need to be much more heavily secured or you can’t really train at scale.”

### A quick favor before you keep reading

I know how many of you are reading GLAI, but I’d love to know a little more about **who** you are. I’ve put together a very short reader survey to help me better understand the GLAI community.

It should take about two minutes, and every question is optional. I’d really appreciate it if you’d take a moment to fill it out. Thanks so much in advance!

[Start Survey](https://www.groundlevel-ai.com/survey/69392?token=)

![User's avatar](https://substackcdn.com/image/fetch/$s_!TgyN!,w_64,h_64,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46567afe-42bd-4d56-ac9a-3579582e6c22_2002x2002.jpeg)

## Continue reading this post for free, courtesy of Sharon Goldman.

Claim my free post

[Or purchase a paid subscription.](https://www.groundlevel-ai.com/subscribe?simple=true&next=https%3A%2F%2Fwww.groundlevel-ai.com%2Fp%2Fai-research-is-running-into-a-security&utm_source=paywall&utm_medium=web&utm_content=211914856&just_signed_up=falsesimple=true&utm_source=paywall&utm_medium=email&utm_content=211914856&next=https://www.groundlevel-ai.com/p/ai-research-is-running-into-a-security)

PreviousNext
