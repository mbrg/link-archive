---
date: '2025-10-15'
description: OpenAI's recent release of ChatGPT Agent significantly escalates the
  risk profile in AI security by enabling direct manipulation of web tools. While
  the adoption of AI guardrails has become commonplace, these soft boundaries are
  proving inadequate against sophisticated threats. Historical parallels to web hacking
  underscore vulnerabilities, as hackers rapidly circumvent both hard and soft protections.
  The reliance on fine-tuning and statistical models for security is insufficient;
  robust data flow controls are essential. As AI evolves, integrating hard boundaries
  within ecosystems can potentially mitigate abuse, but challenges remain in reconciling
  usability and security.
link: https://www.mbgsec.com/posts/2025-07-19-data-flow-controls-wont-save-us/
tags:
- AI Security
- Data Flow Controls
- Soft Boundaries
- Guardrails
- Hard Boundaries
title: Why Aren’t We Making Any Progress In Security From AI - Michael Bargury
---

# Guardrails Are Soft Boundaries. Hard Boundaries Do Exist. [Permalink](https://www.mbgsec.com/posts/2025-07-19-data-flow-controls-wont-save-us/\#guardrails-are-soft-boundaries-hard-boundaries-do-exist "Permalink")

Yesterday OpenAI released [Agent mode](https://openai.com/index/introducing-chatgpt-agent/).
ChatGPT now wields a general purpose tool – its own web browser.
It manipulates the mouse and keyboard directly.
It can use any web tool, like we do.

Any AI security researcher will tell you that this is 100x uptake on risk.
Heck, even Sam Altman dedicated half his [launch post](https://x.com/sama/status/1945900345378697650) warning that this is unsafe for sensitive use.

Meanwhile AI guardrails are The leading idea in AI security.
It’s safe to say they’ve been commoditized.
You can get yours from your AI provider, hordes of Open Source projects, or buy a commercial one.

Yet hackers are having a ball.
Jason Haddix sums it up best:

Twitter Embed

[Visit this post on X](https://twitter.com/Jhaddix/status/1944835174878859680?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1944835174878859680%7Ctwgr%5Ea9fe584d444f1afc2c1ff9f7189436c9bcc9e9e7%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.mbgsec.com%2Fposts%2F2025-07-19-data-flow-controls-wont-save-us%2F)

[![](https://pbs.twimg.com/profile_images/1762218547185364992/1FuX7tkQ_normal.jpg)](https://twitter.com/Jhaddix?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1944835174878859680%7Ctwgr%5Ea9fe584d444f1afc2c1ff9f7189436c9bcc9e9e7%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.mbgsec.com%2Fposts%2F2025-07-19-data-flow-controls-wont-save-us%2F)

[JS0N Haddix](https://twitter.com/Jhaddix?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1944835174878859680%7Ctwgr%5Ea9fe584d444f1afc2c1ff9f7189436c9bcc9e9e7%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.mbgsec.com%2Fposts%2F2025-07-19-data-flow-controls-wont-save-us%2F)

[@Jhaddix](https://twitter.com/Jhaddix?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1944835174878859680%7Ctwgr%5Ea9fe584d444f1afc2c1ff9f7189436c9bcc9e9e7%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.mbgsec.com%2Fposts%2F2025-07-19-data-flow-controls-wont-save-us%2F)

·

[Follow](https://twitter.com/intent/follow?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1944835174878859680%7Ctwgr%5Ea9fe584d444f1afc2c1ff9f7189436c9bcc9e9e7%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.mbgsec.com%2Fposts%2F2025-07-19-data-flow-controls-wont-save-us%2F&screen_name=Jhaddix)

[View on X](https://twitter.com/Jhaddix/status/1944835174878859680?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1944835174878859680%7Ctwgr%5Ea9fe584d444f1afc2c1ff9f7189436c9bcc9e9e7%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.mbgsec.com%2Fposts%2F2025-07-19-data-flow-controls-wont-save-us%2F)

AI Pentest: A client pays an exorbitant amount of money for guardrail and implementation consulting services from a defensive AI Security vendor.

Bypassed in 20 minutes.

It really does feel like the dawn of web hacking all over again.

[7:03 PM · Jul 14, 2025](https://twitter.com/Jhaddix/status/1944835174878859680?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1944835174878859680%7Ctwgr%5Ea9fe584d444f1afc2c1ff9f7189436c9bcc9e9e7%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.mbgsec.com%2Fposts%2F2025-07-19-data-flow-controls-wont-save-us%2F)

[X Ads info and privacy](https://help.twitter.com/en/twitter-for-websites-ads-info-and-privacy)

[377](https://twitter.com/intent/like?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1944835174878859680%7Ctwgr%5Ea9fe584d444f1afc2c1ff9f7189436c9bcc9e9e7%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.mbgsec.com%2Fposts%2F2025-07-19-data-flow-controls-wont-save-us%2F&tweet_id=1944835174878859680) [Reply](https://twitter.com/intent/tweet?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1944835174878859680%7Ctwgr%5Ea9fe584d444f1afc2c1ff9f7189436c9bcc9e9e7%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.mbgsec.com%2Fposts%2F2025-07-19-data-flow-controls-wont-save-us%2F&in_reply_to=1944835174878859680)

Copy link

[Read 22 replies](https://twitter.com/Jhaddix/status/1944835174878859680?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1944835174878859680%7Ctwgr%5Ea9fe584d444f1afc2c1ff9f7189436c9bcc9e9e7%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.mbgsec.com%2Fposts%2F2025-07-19-data-flow-controls-wont-save-us%2F)

## In Hard Boundaries We Trust [Permalink](https://www.mbgsec.com/posts/2025-07-19-data-flow-controls-wont-save-us/\#in-hard-boundaries-we-trust "Permalink")

SQLi attacks were all the rage back in the 90s.
[Taint-analysis](https://en.wikipedia.org/wiki/Taint_checking) was invented to detect vulnerable data flow paths.
Define user inputs as sources, special character escaping-function as sanitizers, and database queries as sinks.
Static analysis tools analyze the software to find any route from source to sink that doesn’t go through a sanitizer.
This is [still the core](https://codeql.github.com/docs/writing-codeql-queries/creating-path-queries/) of static analysis tools.

Formal verification take this a step further and actually allow you to **prove** that there is no unsanitized path between source and sink.
[AWS Network Analyzer enables](https://aws.amazon.com/blogs/aws/new-amazon-vpc-network-access-analyzer/) policies like _“S3 bucket cannot be exposed to the public internet”_.
No matter how many gateways and load balancers you place in-between.

ORM libraries have sanitization [built-in](https://docs.djangoproject.com/en/5.2/topics/security/) to enforce boundaries.
Preventing XSS and SQLi.
SQLi is solved as a technical problem (the operational problem remains, of course).

**With software you can create hard boundaries.**
**You CANNOT get there from here.**

Hard boundaries [cannot be applied](https://www.darkreading.com/cyber-risk/are-100-security-guarantees-possible-) anywhere–they require full knowledge of the environment.
They shine when you go all-in on one ecosystem.
In one ecosystem you can codify the entire environment state into a formula.
AWS Networking Analyzer.
Django ORM.
Virtual machines.
These are illustrative examples of strong guarantees you can get out of buying-into one ecosystem.

**It’s enticing to think that hard boundaries will solve our AI security problems.**
**With hard boundaries, instructions hidden in a document simply CANNOT trigger additional tool calls.**

Meanwhile we can’t even tell if an LLM hallucinated.
Even when we feed in an authoritative document and ask for citation.
We can’t generate a data flow graph for LLMs.

Sure, you can say the LLM fetched a document and then searched the web.
But you CANNOT know whether elements of that file were incorporated into web search query parameters.
Or whether the LLM chose to do the web search query because it was instructed to by the document.
LLMs mix and match data.
Instructions are data.

## Hackers Don’t Care About Your Soft Boundaries [Permalink](https://www.mbgsec.com/posts/2025-07-19-data-flow-controls-wont-save-us/\#hackers-dont-care-about-your-soft-boundaries "Permalink")

AI labs invented a new type of guardrail based on fine-tuning LLMs–a soft boundary.
**Soft boundaries are created by training AI real hard not to violate control flow, and hope that it doesn’t.**
**Sometimes we don’t even train for it.**
**We ask it nicely to apply a boundary through _“system instructions”_.**

System instructions themselves are a soft boundary.
An imaginary boundary.
AI labs [train models to follow instructions](https://openai.com/index/the-instruction-hierarchy/).
Security researchers [pass right through](https://embracethered.com/blog/posts/2024/chatgpt-gpt-4o-mini-instruction-hierarchie-bypasses/) these soft boundaries.

Sam Altman on the [announcement](https://x.com/sama/status/1945900345378697650) of ChatGPT Agent:

> We have built a lot of safeguards and warnings into it, and broader mitigations than we’ve ever developed before from robust training to system safeguards to user controls

Robust training.
Soft boundaries.
Hackers are [happy](https://embracethered.com/blog/posts/2025/chatgpt-operator-prompt-injection-exploits/).

This isn’t to say that soft boundaries aren’t useful.
Here is ChatGPT with GPT 4o refusing to store a malicious memory based on instructions I placed in a Google Drive document.

![ChatGPT 4o refuses to store a memory based on instructions in a Google Drive document](https://www.mbgsec.com/assets/images/2025-07-19-data-flow-controls-wont-save-us/chatgpt_memory_refusal.png)

Check out the conversation [transcript](https://chatgpt.com/share/e/687a40e8-25bc-8002-ba2a-b86b4727c1f0).
More on this at [BHUSA 2025](https://www.blackhat.com/us-25/briefings/schedule/index.html#ai-enterprise-compromise---0click-exploit-methods-46442) _“AI Enterprise Compromise - 0click Exploit Methods”_.

LLM Guardrails addressing Indirect Prompt Injection are another type of soft boundary.
You pass a fetched document through an LLM or classifier and ask it to clean out any instructions.
It’s a sanitizer, the equivalent of backslashing notorious escape characters that lead to injections.
But unlike software sanitizer, it’s based on statistical models.

**Soft boundaries rely on training AI to identify and enforce them.**
**They work most of the time.**
**Hackers don’t care about what happens most of the time.**

Relying on AI makes soft boundaries easy to apply.
They work when hard boundaries are not feasible.
You don’t have to limit yourself to one ecosystem.
They apply in an open environment that spans multiple ecosystems.

\\* The steelman argument for soft boundaries is that AI labs are building AGI.
And AGI can solve anything, including strictly enforcing a soft boundary.
Indeed, soft boundary benchmarks are [going up](https://arxiv.org/abs/2312.14197).
Do you _feel the AGI_?

## Every Boundary Has Its Bypass [Permalink](https://www.mbgsec.com/posts/2025-07-19-data-flow-controls-wont-save-us/\#every-boundary-has-its-bypass "Permalink")

Both hard and soft boundaries can be bypassed.
But they are not the same.
Hard boundaries are bypassed via software bugs.
You could write bug-free software (I definitely can’t, but YOU can).
You can prove correctness for some software.
Soft boundaries are stochastic.
There will always be a counter-example.
A bypass isn’t a bug–it’s the system working as intended.

Summing it up:

| Boundary | Based on | Applies best | Examples | Bypass |
| --- | --- | --- | --- | --- |
| Hard boundary | Software | Within walled ecosystems | VM; Django ORM; | Software bug |
| Soft boundary | AI/ML | Anywhere | AI Guardrails; System instructions | There will always be a counter-examples |

## Hard Boundaries Do Apply To AI Systems [Permalink](https://www.mbgsec.com/posts/2025-07-19-data-flow-controls-wont-save-us/\#hard-boundaries-do-apply-to-ai-systems "Permalink")

Hard boundaries are not applicable to probabilistic AI models.
But they are applicable to AI systems.

Strict control of data flow has been the only thing that has prevented our red team to attain 0click exploits.
Last year we reverse engineered Microsoft Copilot at [BHUSA 2024](https://www.youtube.com/watch?v=FH6P288i2PE).
We spent a long time figuring out if a RAG query results can initiate a new tool invocation like a web search.
It could.
But Microsoft could have built it a different way.
Perform RAG queries by an agent who simply cannot decide to run a web search.

Salesforce Einstein simply [does not read](https://labs.zenity.io/p/inside-salesforce-einstein-a-technical-background) its own tool outputs.
Here is Einstein querying CRM records.
Results are presented in a structured UI component, not summarized by an LLM.
You CANNOT inject instructions through CRM results.
Until someone finds a bypass. More on this at [BHUSA 2025](https://www.blackhat.com/us-25/briefings/schedule/index.html#ai-enterprise-compromise---0click-exploit-methods-46442) _“AI Enterprise Compromise - 0click Exploit Methods”_.

![Salesforce Einstein does not read its own tool outputs. Image by Tamir Ishay Sharbat.](https://www.mbgsec.com/assets/images/2025-07-19-data-flow-controls-wont-save-us/salesforce_crm_result.png)

Microsoft Copilot simply does not render markdown images.
You CANNOT [exfiltrate data through image](https://atlas.mitre.org/techniques/AML.T0077) parameters if there’s no image.
Until someone [finds a bypass](https://labs.zenity.io/p/echoleak-a-reminder-that-ai-agent-risks-are-here-to-stay-3cf3).

ChatGPT validates image URL before rendering them using an API endpoint called `/url_safe`.
[This mechanism](https://embracethered.com/blog/posts/2023/openai-data-exfiltration-first-mitigations-implemented/) ensures that image URLs were not dynamically generated.
They must explicitly be provided by the user.
Until someone [finds a bypass](https://youtu.be/84NVG1c5LRI?si=6sxgefcXoKQAZuC6&t=808).

**The main issue with hard boundaries is that they nerf the agent.**
They make agents less useful.
Like a surgeon removing an entire organ out of abundance of caution.

With market pressure for adoption, AI vendors are removing these one by one.
Anthropic was reluctant to let Claude browse the web.
Microsoft removed Copilot-generated URLs.
OpenAI hid Operator in a separate experimental UI.
These hard boundaries are all gone by now.

## The Solution [Permalink](https://www.mbgsec.com/posts/2025-07-19-data-flow-controls-wont-save-us/\#the-solution "Permalink")

This piece is too long already.
Fortunately the solution is simple.

Here’s what we should

![Claude says bye bye](https://www.mbgsec.com/assets/images/2025-07-19-data-flow-controls-wont-save-us/claude_refusal.png)

#### Share on

[X](https://x.com/intent/tweet?via=mbrg0&text=Why+Aren%27t+We+Making+Any+Progress+In+Security+From+AI%20https%3A%2F%2Fwww.mbgsec.com%2Fposts%2F2025-07-19-data-flow-controls-wont-save-us%2F "Share on X") [Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.mbgsec.com%2Fposts%2F2025-07-19-data-flow-controls-wont-save-us%2F "Share on Facebook") [LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://www.mbgsec.com/posts/2025-07-19-data-flow-controls-wont-save-us/ "Share on LinkedIn") [Bluesky](https://bsky.app/intent/compose?text=Why+Aren%27t+We+Making+Any+Progress+In+Security+From+AI%20https%3A%2F%2Fwww.mbgsec.com%2Fposts%2F2025-07-19-data-flow-controls-wont-save-us%2F "Share on Bluesky")

## You May Also Enjoy

![](https://www.mbgsec.com/assets/images/2025-10-08-making-real-progress-in-security-from-ai/AIAgentSummit.png)

## [Make Real Progress In Security From AI](https://www.mbgsec.com/posts/2025-10-08-making-real-progress-in-security-from-ai/)


1 minute read



I gave a talk at the AI Agent Security Summit by Zenity Labs on October 8th in San Francisco.
I’ll post a blog version of that talk here shortly.

![](https://www.mbgsec.com/assets/images/2025-08-28-human-machine-interface-role-reversal/second.png)

## [How Should AI Ask for Our Input?](https://www.mbgsec.com/posts/2025-08-28-human-machine-interface-role-reversal/)


2 minute read



Enterprise systems provide a terrible user experience.
That’s common knowledge.
Check out one of the flash keynotes about the latest flagship AI product by ...

![](https://www.mbgsec.com/assets/images/2025-08-08-enterprise-ai-compromise-0click-exploit-methods-sneak-peek/talk_cover2.png)

## [Pwn the Enterprise - thank you AI! Slides, Demos and Techniques](https://www.mbgsec.com/posts/2025-08-08-enterprise-ai-compromise-0click-exploit-methods-sneak-peek/)


6 minute read



We’re getting asks for more info about the 0click AI exploits we dropped this week at DEFCON / BHUSA.
We gave a talk at BlackHat, but it’ll take time bef...

![](https://www.mbgsec.com/assets/images/2025-07-26-tracking-down-the-amazon-q-attacker-through-deleted-prs/devcontainer.png)

## [Someone Is Cleaning Up Evidence](https://www.mbgsec.com/posts/2025-07-26-tracking-down-the-amazon-q-attacker-through-deleted-prs/)


1 minute read



AWS security blog confirms the attacker gained access to a write token and abused it to inject the malicious prompt.
This confirms our earlier findings.

Enter your search term...


Twitter Widget Iframe
