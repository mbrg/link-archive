---
date: '2025-08-08'
description: Recent findings by security researchers Michael Bargury and Tamir Ishay
  Sharbat reveal a vulnerability in OpenAI’s Connectors that enables indirect prompt
  injection attacks. The attack, demonstrated as "AgentFlayer," involves a poisoned
  document to extract sensitive data, such as API keys, from a Google Drive account
  with zero user interaction required. This highlights the risks of connecting generative
  AI models to external data sources, potentially increasing the attack surface for
  malicious actors. The findings emphasize the urgent need for robust protections
  against such injection attacks as AI integration expands in organizational systems.
link: https://www.wired.com/story/poisoned-document-could-leak-secret-data-chatgpt/
tags:
- ChatGPT
- AI security
- prompt injection
- OpenAI
- cybersecurity
title: A Single Poisoned Document Could Leak ‘Secret’ Data Via ChatGPT ◆ WIRED
---

[Skip to main content](https://www.wired.com/story/poisoned-document-could-leak-secret-data-chatgpt/#main-content)

Save StorySave this story

Save StorySave this story

The latest generative AI models are not just stand-alone [text-generating chatbots](https://www.wired.com/story/openai-chatgpt-agent-launch/)—instead, they can easily be hooked up to your data to give personalized answers to your questions. OpenAI’s [ChatGPT can be linked](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt) to your Gmail inbox, allowed to inspect your GitHub code, or find appointments in your Microsoft calendar. But these connections have the potential to be abused—and researchers have shown it can take just a single “poisoned” document to do so.

New findings from security researchers Michael Bargury and Tamir Ishay Sharbat, revealed at the Black Hat hacker conference in Las Vegas today, show how a weakness in OpenAI’s Connectors allowed sensitive information to be extracted from a Google Drive account using an [indirect prompt injection attack](https://www.wired.com/story/generative-ai-prompt-injection-hacking/). In a demonstration of the attack, [dubbed AgentFlayer](https://labs.zenity.io/p/agentflayer-chatgpt-connectors-0click-attack-5b41?), Bargury shows how it was possible to extract developer secrets, in the form of API keys, that were stored in a demonstration Drive account.

The vulnerability highlights how connecting AI models to external systems and sharing more data across them increases the potential attack surface for malicious hackers and potentially multiplies the ways where vulnerabilities may be introduced.

“There is nothing the user needs to do to be compromised, and there is nothing the user needs to do for the data to go out,” Bargury, the CTO at security firm Zenity, tells WIRED. “We’ve shown this is completely zero-click; we just need your email, we share the document with you, and that’s it. So yes, this is very, very bad,” Bargury says.

OpenAI did not immediately respond to WIRED’s request for comment about the vulnerability in Connectors. The company introduced Connectors for ChatGPT as a beta feature earlier this year, and its [website lists](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt) at least 17 different services that can be linked up with its accounts. It says the system allows you to “bring your tools and data into ChatGPT” and “search files, pull live data, and reference content right in the chat.”

Bargury says he reported the findings to OpenAI earlier this year and that the company quickly introduced mitigations to prevent the technique he used to extract data via Connectors. The way the attack works means only a limited amount of data could be extracted at once—full documents could not be removed as part of the attack.

“While this issue isn’t specific to Google, it illustrates why developing robust protections against prompt injection attacks is important,” says Andy Wen, senior director of security product management at Google Workspace, pointing to the company’s [recently enhanced AI security measures](https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html).

Bargury’s attack starts with a poisoned document, which is [shared](https://support.google.com/drive/answer/2375057?hl=en-GB&co=GENIE.Platform%3DDesktop) to a potential victim’s Google Drive. (Bargury says a victim could have also uploaded a compromised file to their own account.) Inside the document, which for the demonstration is a fictitious set of notes from a nonexistent meeting with OpenAI CEO Sam Altman, Bargury hid a 300-word malicious prompt that contains instructions for ChatGPT. The prompt is written in white text in a size-one font, something that a human is unlikely to see but a machine will still read.

In a [proof of concept video of the attack](https://www.youtube.com/watch?v=JNHpZUpeOCg), Bargury shows the victim asking ChatGPT to “summarize my last meeting with Sam,” although he says any user query related to a meeting summary will do. Instead, the hidden prompt tells the LLM that there was a “mistake” and the document doesn’t actually need to be summarized. The prompt says the person is actually a “developer racing against a deadline” and they need the AI to search Google Drive for API keys and attach them to the end of a URL that is provided in the prompt.

That URL is actually a command in the [Markdown language](https://www.wired.com/story/the-eternal-truth-of-markdown/) to connect to an external server and pull in the image that is stored there. But as per the prompt’s instructions, the URL now also contains the API keys the AI has found in the Google Drive account.

Using Markdown to extract data from ChatGPT is not new. Independent security researcher Johann Rehberger has [shown how data](https://embracethered.com/blog/posts/2023/openai-custom-malware-gpt/) [could be extracted](https://embracethered.com/blog/posts/2025/chatgpt-chat-history-data-exfiltration/) this way, and [described how OpenAI previously introduced a feature](https://embracethered.com/blog/posts/2023/openai-data-exfiltration-first-mitigations-implemented/) called “url\_safe” to detect if URLs were malicious and stop image rendering if they are dangerous. To get around this, Sharbat, an AI researcher at Zenity, [writes in a blog post](https://labs.zenity.io/p/agentflayer-chatgpt-connectors-0click-attack-5b41) detailing the work, that the researchers used URLs from Microsoft’s Azure Blob cloud storage. “Our image has been successfully rendered, and we also get a very nice request log in our Azure Log Analytics which contains the victim’s API keys,” the researcher writes.

The attack is the latest demonstration of how [indirect prompt injections](https://www.wired.com/story/generative-ai-prompt-injection-hacking/) can impact generative AI systems. Indirect prompt injections involve attackers feeding an LLM poisoned data that can tell the system to complete malicious actions. This week, a group of researchers showed how indirect prompt injections could be used to hijack a smart home system, [activating a smart home’s lights and boiler remotely](https://www.wired.com/story/google-gemini-calendar-invite-hijack-smart-home/).

While indirect prompt injections have been around almost as long as ChatGPT has, security researchers worry that as more and more systems are connected to LLMs, there is an increased risk of attackers inserting “untrusted” data into them. Getting access to sensitive data could also allow malicious hackers a way into an organization's other systems. Bargury says that hooking up LLMs to external data sources means they will be more capable and increase their utility, but that comes with challenges. “It’s incredibly powerful, but as usual with AI, more power comes with more risk,” Bargury says.

## You Might Also Like …

- **In your inbox:** [Five new newsletters](https://www.wired.com/newsletter?sourceCode=BottomStories) by deeply sourced experts

- Interview: [Bryan Johnson is going to die](https://www.wired.com/story/big-interview-bryan-johnson/)

- **Big Story:** [The enshittification of American power](https://www.wired.com/story/enshittification-of-american-power/)

- This is [DOGE 2.0](https://www.wired.com/story/next-stage-doge-elon-musk/)

- **Special Edition:** [Are we healthy yet?](https://www.wired.com/beyond-wellness/)


[![](https://media.wired.com/photos/65e713244d9f150f523145c2/1:1/w_270%2Cc_limit/undefined)](https://www.wired.com/author/matt-burgess/)

[Matt Burgess](https://www.wired.com/author/matt-burgess/) is a senior writer at WIRED focused on information security, privacy, and data regulation in Europe. He graduated from the University of Sheffield with a degree in journalism and now lives in London. Send tips to Matt\_Burgess@wired.com. ... [Read More](https://www.wired.com/author/matt-burgess)

Senior writer

- [X](https://www.twitter.com/mattburgess1)

Topics [artificial intelligence](https://www.wired.com/tag/artificial-intelligence/) [cybersecurity](https://www.wired.com/tag/cybersecurity/) [hacking](https://www.wired.com/tag/hacking/) [security](https://www.wired.com/tag/security/) [vulnerabilities](https://www.wired.com/tag/vulnerabilities/) [Google](https://www.wired.com/tag/google/) [OpenAI](https://www.wired.com/tag/openai/) [ChatGPT](https://www.wired.com/tag/chatgpt/) [black hat](https://www.wired.com/tag/black-hat/) [DefCon](https://www.wired.com/tag/defcon/)

[Leak Reveals the Workaday Lives of North Korean IT Scammers](https://www.wired.com/story/leaked-data-reveals-the-workaday-lives-of-north-korean-it-scammers/#intcid=_wired-article-bottom-recirc_f3315436-7ce1-4d71-be47-0a836f62bd5d_roberta-similarity1_fallback_cral-top2-2)

Spreadsheets, Slack messages, and files linked to an alleged group of North Korean IT workers expose their meticulous job-planning and targeting—and the constant surveillance they're under.

Matt Burgess

[The Best Colored Noise for Sleep](https://www.wired.com/story/best-noise-for-sleep/#intcid=_wired-article-bottom-recirc_f3315436-7ce1-4d71-be47-0a836f62bd5d_roberta-similarity1_fallback_cral-top2-2)

You may be familiar with white noise, but what about pink noise, or brown noise? WIRED’s sleep expert walks you through the rainbow of benefits for bedtime.

Julia Forbes

[The 35 Best Movies on HBO Max Right Now](https://www.wired.com/story/best-movies-hbo-max-right-now/#intcid=_wired-article-bottom-recirc_f3315436-7ce1-4d71-be47-0a836f62bd5d_roberta-similarity1_fallback_cral-top2-2)

_Final Destination Bloodlines_, _Sinners_, and _Get Out_ are just a few of the movies you should be watching on HBO Max this month.

WIRED Staff

[Mysterious Crime Spree Targeted National Guard Equipment Stashes](https://www.wired.com/story/mysterious-crime-spree-targeted-national-guard-equipment-stashes/#intcid=_wired-article-bottom-recirc_f3315436-7ce1-4d71-be47-0a836f62bd5d_roberta-similarity1_fallback_cral-top2-2)

A string of US armory break-ins, kept quiet by authorities for months, points to a growing security crisis—and signs of an inside job.

Dell Cameron

[Encryption Made for Police and Military Radios May Be Easily Cracked](https://www.wired.com/story/encryption-made-for-police-and-military-radios-may-be-easily-cracked-researchers-find/#intcid=_wired-article-bottom-recirc_f3315436-7ce1-4d71-be47-0a836f62bd5d_roberta-similarity1_fallback_cral-top2-2)

Researchers found that an encryption algorithm likely used by law enforcement and special forces can have weaknesses that could allow an attacker to listen in.

Kim Zetter

[OpenAI Finally Launched GPT-5. Here's Everything You Need to Know](https://www.wired.com/story/openais-gpt-5-is-here/#intcid=_wired-article-bottom-recirc_f3315436-7ce1-4d71-be47-0a836f62bd5d_roberta-similarity1_fallback_cral-top2-2)

OpenAI released GPT-5 on Thursday to both free users of ChatGPT and paying subscribers.

Kylie Robison

[Why the US Is Racing to Build a Nuclear Reactor on the Moon](https://www.wired.com/story/why-the-us-is-racing-to-build-a-nuclear-reactor-on-the-moon/#intcid=_wired-article-bottom-recirc_f3315436-7ce1-4d71-be47-0a836f62bd5d_roberta-similarity1_fallback_cral-top2-2)

NASA has set a 2030 deadline to build a 100-kilowatt nuclear reactor on the moon. It’s an ambitious but potentially achievable goal that could transform space exploration, experts tell WIRED.

Becky Ferreira

[Age Verification Is Sweeping Gaming. Is It Ready for the Age of AI Fakes?](https://www.wired.com/story/age-verification-is-sweeping-gaming-is-it-ready-for-the-age-of-ai-fakes/#intcid=_wired-article-bottom-recirc_f3315436-7ce1-4d71-be47-0a836f62bd5d_roberta-similarity1_fallback_cral-top2-2)

Discord users are already using video game characters to bypass the UK’s age-check laws. AI deepfakes could make things even more complicated.

Megan Farokhmanesh

[Trump Is Undermining Trust in Official Economic Statistics. China Shows Where That Path Can Lead](https://www.wired.com/story/trump-labor-statistics-china-comparison-gdp-unemployment/#intcid=_wired-article-bottom-recirc_f3315436-7ce1-4d71-be47-0a836f62bd5d_roberta-similarity1_fallback_cral-top2-2)

China demonstrates how manipulating economic data can ultimately erode government credibility.

Louise Matsakis

[The Best Walking Pads for Hitting Your Daily Step Goals](https://www.wired.com/story/best-walking-pads/#intcid=_wired-article-bottom-recirc_f3315436-7ce1-4d71-be47-0a836f62bd5d_roberta-similarity1_fallback_cral-top2-2)

These compact walking pads fit under your desk and make staying active so much easier.

Kristin Canning

[Eli Lilly’s Obesity Pill Shows Promising Weight Loss in New Results](https://www.wired.com/story/eli-lillys-obesity-pill-shows-promising-weight-loss-in-new-results/#intcid=_wired-article-bottom-recirc_f3315436-7ce1-4d71-be47-0a836f62bd5d_roberta-similarity1_fallback_cral-top2-2)

In an 18-month clinical trial of the experimental GLP-1 pill orforglipron, about 60 percent of people lost at least 10 percent of their body weight.

Emily Mullin

[NASA Rewrites the Rules for Developers of Private Space Stations](https://www.wired.com/story/nasas-new-chief-has-radically-rewritten-the-rules-for-private-space-stations/#intcid=_wired-article-bottom-recirc_f3315436-7ce1-4d71-be47-0a836f62bd5d_roberta-similarity1_fallback_cral-top2-2)

In the face of budget cuts, NASA has issued a new directive on how it will procure replacements for the International Space Station.

Eric Berger, Ars Technica
