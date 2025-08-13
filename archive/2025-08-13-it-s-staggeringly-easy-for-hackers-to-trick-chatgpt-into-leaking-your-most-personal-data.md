---
date: '2025-08-13'
description: At Black Hat 2025, researchers revealed a critical vulnerability in OpenAI's
  ChatGPT that allows indirect prompt injection attacks via "poisoned" documents.
  By embedding malicious prompts in overlooked document formats, attackers can exploit
  the AI's access to Google accounts, extracting sensitive data with no user interaction
  required. This incident underscores deficiencies in AI security, particularly with
  broader integrations, as seen with ChatGPT's Connectors feature. While OpenAI swiftly
  patched the exploit, the incident highlights significant risks in using AI tools
  across diverse applications, necessitating stringent security reviews prior to deployment
  in sensitive environments.
link: https://futurism.com/hackers-trick-chatgpt-personal-data
tags:
- Vulnerabilities
- AI Security
- Prompt Injection
- Data Privacy
- Cybersecurity
title: It's Staggeringly Easy for Hackers to Trick ChatGPT Into Leaking Your Most
  Personal Data
---

![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271024%27%20height=%27536.1256544502618%27/%3e)![Futurism](https://futurism.com/_next/image?url=https%3A%2F%2Fwordpress-assets.futurism.com%2F2025%2F08%2Fhackers-trick-chatgpt-personal-data.jpg&w=2048&q=75)

![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271024%27%20height=%27682.6666666666666%27/%3e)![Futurism](https://futurism.com/_next/image?url=https%3A%2F%2Fwordpress-assets.futurism.com%2F2025%2F08%2Fhackers-trick-chatgpt-personal-data.jpg&w=2048&q=75)

Image byFuturism

OpenAI's ChatGPT can easily be coaxed into leaking your personal data — with just a single "poisoned" document.

As [_Wired_ reports](https://www.wired.com/story/poisoned-document-could-leak-secret-data-chatgpt/), security researchers revealed at this year's Black Hat hacker conference that highly sensitive information can be stolen from a Google Drive account with an indirect prompt injection attack. In other words, hackers feed a document with hidden, malicious prompts to an AI that controls your data instead of manipulating it directly with a prompt injection, one of the [most serious types of security flaws](https://www.wired.com/story/generative-ai-prompt-injection-hacking/) threatening the safety of user-facing AI systems.

ChatGPT's ability to be linked to a Gmail account allows it to rifle through your files, which could easily expose you to simple hacks.

This latest glaring lapse in cybersecurity highlights the tech's enormous shortcomings, and raises concerns that your personal data simply isn't safe with these types of tools.

"There is nothing the user needs to do to be compromised, and there is nothing the user needs to do for the data to go out," security firm Zenity CTO Michael Bargury, who discovered the vulnerability with his colleagues, told _Wired_. "We’ve shown this is completely zero-click; we just need your email, we share the document with you, and that’s it. So yes, this is very, very bad."

Earlier this year, OpenAI launched its Connectors for ChatGPT feature in the form of a beta, giving the chatbot access to Google accounts that allow it to "search files, pull live data, and reference content right in the chat."

The way the exploit works is by hiding a 300-word malicious prompt in a document in white text and size-one font — something that's easily overlooked by a human, but not a chatbot like ChatGPT.

In a proof of concept, Bargury and his colleagues showed how the hidden prompt flagged a "mistake" to ChatGPT, instructing it that it doesn't actually need a document to be summarized. Instead, it calls for the chatbot to extract Google Drive API keys and share them with the attackers.

Bargury already flagged the exploit to OpenAI, which acted quickly enough to plug the hole. The exploit also didn't allow hackers to extract full documents due to how it works, _Wired_ points out. Still, the incident shows that even ChatGPT, with all the staggering resources of OpenAI behind it, is a leaky tub of potential security vulnerabilities even as it's being pushed to institutions ranging [from colleges](https://www.nytimes.com/2025/06/07/technology/chatgpt-openai-colleges.html) to the [federal government](https://www.cnbc.com/2025/08/06/openai-is-giving-chatgpt-to-the-government-for-1-.html).

It's not just Google, either — Connectors allows users to connect up to 17 different services, raising the possibility that other personal information could be extracted as well.

It's far from the first time security researchers have flagged glaring cybersecurity gaps in AI systems. There have been [numerous other instances](https://thehackernews.com/2025/06/google-adds-multi-layered-defenses-to.html) of how [indirect prompt injections](https://futurism.com/the-byte/ai-microsoft-windows-incredibly-hackable) can extract personal data.

The same day _Wired_ published its piece, the outlet also reported on a separate indirect prompt injection attack that [allowed hackers to hijack a smart home system](https://www.wired.com/story/google-gemini-calendar-invite-hijack-smart-home/), enabling them to turn off the lights, open and close smart shutters, and even turn on a boiler.

Researchers at Tel Aviv University found that Google's Gemini AI chatbot could be manipulated to figuratively give up the keys to a smart home by feeding it a poisoned Google Calendar invite. A later prompt to summarize calendar events triggers hidden instructions inside the poisoned invite, causing the smart home products to jump into action, _Wired_ reports — only one of 14 different indirect prompt injection attacks aimed at the AI.

"LLMs are about to be integrated into physical humanoids, into semi- and fully autonomous cars, and we need to truly understand how to secure LLMs before we integrate them with these kinds of machines, where in some cases the outcomes will be safety and not privacy," Tel Aviv University researcher Ben Nassi told the publication.

We've known about indirect prompt injection attacks for several years now, but given the latest news, companies still have a lot of work to do to mitigate the substantial risks. By giving tools like ChatGPT more and more access to our personal lives, security researchers warn of many more lapses in cybersecurity that could leave our data exposed to hackers.

"It’s incredibly powerful, but as usual with AI, more power comes with more risk," Bargury told _Wired_.

**More on AI hijacking:** _[The Copilot AI Microsoft Built Into Windows Makes It Incredibly Hackable, Research Shows](https://futurism.com/the-byte/ai-microsoft-windows-incredibly-hackable)_

Share This Article
