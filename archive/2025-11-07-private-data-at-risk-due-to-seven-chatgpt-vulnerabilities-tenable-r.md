---
date: '2025-11-07'
description: Tenable Research identifies seven critical vulnerabilities in OpenAI's
  ChatGPT, including advanced indirect prompt injections that can exfiltrate user
  data. The discovery highlights the AI's susceptibility to attacks via manipulated
  inputs, utilizing features like user memories and browsing capabilities. Key findings
  include successful 0-click and 1-click injection attacks that exploit external web
  content and URL safety checks, allowing attackers to manipulate responses and access
  sensitive information. These vulnerabilities pose significant risks to millions
  of users and demonstrate the need for enhanced security mechanisms in AI applications.
  Continuous oversight and updates are vital to mitigate these risks effectively.
link: https://www.tenable.com/blog/hackedgpt-novel-ai-vulnerabilities-open-the-door-for-private-data-leakage
tags:
- Prompt Injection
- Data Exfiltration
- AI Security
- Vulnerabilities
- ChatGPT
title: Private data at risk due to seven ChatGPT vulnerabilities ◆ Tenable®
---

- [Skip to Main Navigation](https://www.tenable.com/blog/hackedgpt-novel-ai-vulnerabilities-open-the-door-for-private-data-leakage#site-nav)
- [Skip to Main Content](https://www.tenable.com/blog/hackedgpt-novel-ai-vulnerabilities-open-the-door-for-private-data-leakage#block-tenable-content)
- [Skip to Footer](https://www.tenable.com/blog/hackedgpt-novel-ai-vulnerabilities-open-the-door-for-private-data-leakage#site-footer)

FacebookGoogle PlusTwitterLinkedInYouTubeRSSMenuSearchResource - BlogResource - WebinarResource - ReportResource - Eventicons\_066icons\_067icons\_068icons\_069icons\_070

[Blog](https://www.tenable.com/blog) / [AI Security](https://www.tenable.com/blog/search?field_blog_section_tid=1985)

[Subscribe](https://www.tenable.com/blog/hackedgpt-novel-ai-vulnerabilities-open-the-door-for-private-data-leakage#blog-subscribe)

# HackedGPT: Novel AI Vulnerabilities Open the Door for Private Data Leakage

* * *

![Moshe Bernstein](https://www.tenable.com/sites/default/files/pictures/2025-10/Moshe-Bernstein.jpg)[Moshe Bernstein](https://www.tenable.com/profile/moshe-bernstein)

![Liv Matan](https://www.tenable.com/sites/default/files/pictures/2024-03/Liv-Matan.jpg)[Liv Matan](https://www.tenable.com/profile/liv-matan)

November 5, 2025

13 Min Read

- [![X logo](https://static.tenable.com/marketing/icons/social/SVG/footer-icon-twitter.svg)](https://x.com/intent/post?text=HackedGPT%3A%20Novel%20AI%20Vulnerabilities%20Open%20the%20Door%20for%20Private%20Data%20Leakage%20https://www.tenable.com/blog/hackedgpt-novel-ai-vulnerabilities-open-the-door-for-private-data-leakage)
- [![Facebook logo](https://static.tenable.com/marketing/icons/social/SVG/footer-icon-facebook.svg)](https://www.facebook.com/sharer/sharer.php?u=https://www.tenable.com/blog/hackedgpt-novel-ai-vulnerabilities-open-the-door-for-private-data-leakage)
- [![LinkedIn logo](https://static.tenable.com/marketing/icons/social/SVG/footer-icon-linkedin.svg)](https://www.linkedin.com/shareArticle?mini=true&url=https://www.tenable.com/blog/hackedgpt-novel-ai-vulnerabilities-open-the-door-for-private-data-leakage&title=HackedGPT%3A%20Novel%20AI%20Vulnerabilities%20Open%20the%20Door%20for%20Private%20Data%20Leakage&summary=&source=)

* * *

Tenable Research has discovered seven vulnerabilities and attack techniques in ChatGPT, including unique indirect prompt injections, exfiltration of personal user information, persistence, evasion, and bypass of safety mechanisms.

![abstract image on blue background with the words HackedGPT: Novel AI Vulnerabilities Lead to Private Data Leakage](https://www.tenable.com/sites/default/files/images/articles/Hacked%20GPT_MAIN.jpg)

## Key takeaways:

1. Tenable Research has discovered multiple new and persistent vulnerabilities in OpenAI's ChatGPT that could allow an attacker to exfiltrate private information from users' memories and chat history.

2. These vulnerabilities, present in the latest GPT-5 model, could allow attackers to exploit users without their knowledge through several likely victim use cases, including simply asking ChatGPT a question.

3. The discoveries include a vulnerability bypassing ChatGPT's safety features, meant to protect users from such attacks, and could lead to the theft of private ChatGPT user data.

4. Hundreds of millions of users interact with LLMs on a daily basis, and could be vulnerable to these attacks.

## Architecture

Prompt injections are a weakness in how large language models (LLMs) process input data. An attacker can manipulate the LLM by injecting instructions into any data it ingests, which can cause the LLM to ignore the original instructions and perform unintended or malicious actions instead. Specifically, indirect prompt injection occurs when an LLM finds unexpected instructions in an external source, such as a document or website, rather than a direct prompt from the user. Since prompt injection is a well-known issue with LLMs, many AI vendors create safeguards to help mitigate and protect against it. Nevertheless, we discovered several vulnerabilities and techniques that significantly increase the potential impact of indirect prompt injection attacks. To better understand the discoveries, we will first cover some technical details about how ChatGPT works. (To get right to the discoveries, click [here](https://www.tenable.com/blog/hackedgpt-novel-ai-vulnerabilities-open-the-door-for-private-data-leakage#here).)

### System prompt

Every ChatGPT model has a set of instructions created by OpenAI that outline the capabilities and context of the model before its conversation with the user. This is called a System Prompt. Researchers often use techniques for extracting the System Prompt from ChatGPT (as can be seen [here](https://gist.github.com/maoxiaoke/f6d5b28f9104cd856a2622a084f46fd7)), giving insight into how the LLM works. When looking at the System Prompt, we can see that ChatGPT has the capability to retain information across conversations using the _bio_ tool, or, as ChatGPT users may know it, [memories](https://openai.com/index/memory-and-new-controls-for-chatgpt/). The context from the user’s memories is appended to the System Prompt, giving the model access to any (potentially private) information deemed important in previous conversations. Additionally, we can see that ChatGPT has access to a _web_ tool, allowing it to access up-to-date information from the internet based on two commands: _search_ and _open\_url_.

### The _bio_ tool, aka memories

The ChatGPT memory feature mentioned above is enabled by default. If the user asks it to remember something, or if there is some information that the engine deems important even without an explicit request, it can be remembered using memories. As is seen in the System Prompt, the memories are invoked internally using the _bio_ tool and sent as a static context along with it. It is important to note that memories could contain private information about the user. Memories are shared between conversations and considered by the LLM before each response. It is also possible to have a memory about the type of response you want, which will be taken into account whenever ChatGPT responds.

In addition to its long-term memory feature, ChatGPT considers the current conversation and context when responding. It can refer to previous requests and messages or follow a line of thinking. To avoid confusion, we will refer to this type of memory as Conversational Context.

### The web tool

While researching ChatGPT, we discovered some information about how the _web_ tool works. If ChatGPT gets a URL directly from the user or decides it needs to visit a specific URL, it will do so with the _web_ tool's _open\_url_ functionality, which we will refer to as Browsing Context. When doing so, it will usually use the _ChatGPT-User_ user agent. It quickly became clear to us that there is some kind of cache mechanism for such browsing, since when we asked about a URL that was already opened, ChatGPT would respond without browsing again.

Based on our experimentation, ChatGPT is extremely susceptible to prompt injection while browsing, but we concluded that _open\_url_ actually hands the responsibility of browsing to an alternative LLM named SearchGPT, which has significantly fewer capabilities and understanding of the user context. Sometimes ChatGPT will respond with the output of SearchGPT’s browsing results as-is, and sometimes it will take the full output and modify its reply based on the question. As a method of isolation, SearchGPT has no access to the user’s memories or context. Therefore, despite being susceptible to prompt injection in the Browsing Context, the user should, theoretically, be safe, as SearchGPT is doing the browsing.

![As a method of isolation, SearchGPT has no access to the user’s memories or context.](https://www.tenable.com/sites/default/files/inline/images/blog_tenable-HackedGPT-02.png)![ID instructions in ChatGPT](https://www.tenable.com/sites/default/files/inline/images/ID%20Instuctions.png)![open_url hands the responsibility of browsing to an alternative LLM named SearchGPT](https://www.tenable.com/sites/default/files/inline/images/searchgpt_vs_chatgpt2.png)

_The AI identifies as SearchGPT when browsing, and as ChatGPT when interacting with the user_

![In this example, the user has a memory stating that responses should include emojis. Since SearchGPT doesn’t have access to memories, they are not addressed when it responds ](https://www.tenable.com/sites/default/files/inline/images/Prefers%20Emojis.png)

_In this example, the user has a memory stating that responses should include emojis. Source: Tenable, November 2025_

![In this example, the user has a memory stating that responses should include emojis. Since SearchGPT doesn’t have access to memories, they are not addressed when it responds ](https://www.tenable.com/sites/default/files/inline/images/Search%20vs%20Chat%20Emojis.png)

_Since SearchGPT doesn’t have access to memories, they are not addressed when it responds. Source: Tenable, November 2025._

The other end of the _web_ tool is the _search_ command, used by ChatGPT to invoke an internet search whenever a user enters a prompt that requires it. ChatGPT uses a proprietary search engine to find and return results based on up-to-date information that may have been published after the model’s training cutoff date. A user can choose this feature with the dedicated “Web search” button; if the user doesn’t select this feature, a search is conducted at the LLM’s discretion. ChatGPT might send a few queries or change the wording of the search in an attempt to optimize the results, which are returned as a list of websites and snippets. If possible, it will respond solely based on the information in the result snippets, but if that information is insufficient, it might browse using the _open\_url_ command to some of the sites in order to investigate further. It seems that part of the indexing is done by Bing, and part is done by OpenAI using their crawler with _OAI-Search_ as its user agent. We don’t know the distinction in the responsibilities of OpenAI and Bing. We will refer to this usage of the _search_ command as Search Context.

![An example of a web search and its results. Source: Tenable, November 2025.](https://www.tenable.com/sites/default/files/inline/images/Search%20President%20GPT5.png)

_An example of a web search and its results. Source: Tenable, November 2025._

### **The** _**url\_safe**_ **endpoint**

Since prompt injection is such a prevalent issue, AI vendors are constantly trying to mitigate the potential impact of these attacks by developing safety features to protect user data. Much of the potential impact of prompt injection stems from having the AI respond with URLs, which could be used to direct the user to a malicious website or exfiltrate information with [image markdown rendering](https://atlas.mitre.org/techniques/AML.T0077). OpenAI has attempted to address this issue with an endpoint named [_url\_safe_](https://embracethered.com/blog/posts/2023/openai-data-exfiltration-first-mitigations-implemented/), which checks most URLs before they are shown to the user and uses proprietary logic to decide whether the URL is safe or not. If it is deemed unsafe, the link is omitted from the output.

Based on our research, some of the parameters that are checked include:

- Domain trust (e.g., [openai.com](http://openai.com/))
- Existence and trust of a subdomain
- Existence and trust of parameters
- Conversational Context

## 7 new vulnerabilities and techniques in ChatGPT

### 1\. Indirect prompt injection vulnerability via trusted sites in Browsing Context

When diving into ChatGPT’s Browsing Context, we wondered how malicious actors could exploit ChatGPT’s susceptibility to indirect prompt injection in a way that would align with a legitimate use case. Since one of the primary use cases for the Browsing Context is summarizing blogs and articles, our idea was to inject instructions in the comment section. We created our own blogs with dummy content and then left a message for SearchGPT in the comments section. When asked to summarize the contents of the blog, SearchGPT follows the malicious instructions from the comment, compromising the user. (We elaborate on the specific impact to the user in the Full Attack Vector PoCs section below.) The potential reach of this vulnerability is tremendous, since attackers could spray malicious prompts in comment sections on popular blogs and news sites, compromising countless ChatGPT users.

### 2\. 0-click indirect prompt injection vulnerability in Search Context

We’ve proven that we can inject a prompt when the user asks ChatGPT to browse to a specific website, but what about attacking a user just for asking a question? We know that ChatGPT’s web search results are based on Bing and OpenAI’s crawler, so we wondered: What would happen if a site with a prompt injection were to be indexed? In order to prove our theory, we created some websites about niche topics with specific names in order to narrow down our results, such as a site containing some humorous information about our team with the domain [llmninjas.com](http://llmninjas.com/). We then asked ChatGPT for information about the LLM Ninjas team and were pleased to see that our site was sourced in the response.

Having only a prompt injection on your site would make it much less likely to be indexed by Bing, so we created a fingerprint for SearchGPT based on the headers and user agent it uses to browse, and only served the prompt injection when SearchGPT was the one browsing. _Voila!_ After the change we made was indexed by OpenAI’s crawler, we were able to achieve the final level of prompt injection and inject a prompt just by the victim asking a simple question!

Hundreds of millions of users ask LLMs questions that require searching the web, and it seems that LLMs will eventually [replace classic search engines](https://www.forbes.com/councils/forbesagencycouncil/2024/12/27/will-llms-lead-to-the-demise-of-google-search/). This unprecedented 0-click vulnerability opens a whole new attack vector that could target anyone who relies on AI search for information. AI vendors are relying on metrics like SEO scores, which are not security boundaries, to choose which sources to trust. By hiding the prompt in tailor-made sites, attackers could directly target users based on specific topics or political and social trends.

![The output of the LLM is manipulated (as noted by “TCS Research POC Success!”), compromising the user for asking an innocent question](https://www.tenable.com/sites/default/files/inline/images/llmninjas.png)_The output of the LLM is manipulated (as noted by “TCS Research POC Success!”), compromising the user for asking an innocent question. Source: Tenable, November 2025_

### 3\. Prompt injection vulnerability via 1-click

The final and simplest method of prompt injection is through a feature that OpenAI created, which allows users to prompt ChatGPT by browsing to _https://chatgpt.com/?q={Prompt}_. We found that ChatGPT will automatically submit the query in the _q=_ parameter, leaving anyone who clicks that link vulnerable to a prompt injection attack.

07 URL Prompt Injection New

Play Video

![HackedGPT prompt injection example](https://play.vidyard.com/oX93yCSyZBnDMF6ypuyBNr.jpg)

### 4\. Safety mechanism bypass vulnerability

During our research of the _url\_safe_ endpoint, we noticed that [bing.com](https://bing.com/) was a whitelisted domain, and always passed the _url\_safe_ check. It turns out that search results on Bing are served through a wrapped tracking link that redirects the user from a static bing.com/ck/a link to the requested website. That means that any website that is indexed on Bing has a bing.com URL that will redirect to it.

![When searching using Bing, if we hover over the results, we can see that they redirect to bing.com/ck/a links. Source: Tenable, November 2025.](https://www.tenable.com/sites/default/files/inline/images/bing.png)_When searching using Bing, if we hover over the results, we can see that they redirect to bing.com/ck/a links. Source: Tenable, November 2025._

By indexing some test websites to Bing, we were able to extract their static tracking links and use them to bypass the _url\_safe_ check, allowing our links to be fully rendered. The Bing tracking links cannot be altered, so a single link cannot extract information that we did not know in advance. Our solution was to index a page for every letter in the alphabet and then use those links to exfiltrate information one letter at a time. For example, if we want to exfiltrate the word “Hello”, ChatGPT would render the Bing links for H, E, L, L, and O sequentially in its response.

### 5\. Conversation Injection technique

Even with the _url\_safe_ bypass above, we cannot use prompt injection alone to exfiltrate anything of value, since SearchGPT has no access to user data. We wondered: How could we get control over ChatGPT’s output when we only have direct access to SearchGPT’s output? Then we remembered Conversational Context. ChatGPT remembers the entire conversation when responding to user prompts. If it were to find a prompt on its “side” of the conversation, would it still listen? So we used our SearchGPT prompt injection to ensure the response ends with another prompt for ChatGPT in a novel technique we dubbed **Conversation Injection**. When responding to the following prompts, ChatGPT will go over the Conversational Context, see, and listen to the instructions we injected, not realizing that SearchGPT wrote them. Essentially, ChatGPT is prompt-injecting itself.

![We inject a prompt to SearchGPT, which in turn injects a prompt to ChatGPT within its response](https://www.tenable.com/sites/default/files/inline/images/blog_tenable-HackedGPT-03%20%281%29.png)![We inject a prompt to SearchGPT, which in turn injects a prompt to ChatGPT within its response. Source: Tenable, November 2025.](https://www.tenable.com/sites/default/files/inline/images/convo_injection.png)_We inject a prompt to SearchGPT, which in turn injects a prompt to ChatGPT within its response. Source: Tenable, November 2025._

### 6\. Malicious content hiding technique

One of the issues with the Conversation Injection technique is that the output from SearchGPT appears clearly to the user, which will raise a lot of suspicion. We discovered a bug with how the ChatGPT website renders markdown that can allow us to hide the malicious content. When rendering code blocks, any data that appears on the same line as the code block opening (past the first word) does not get rendered. This means that unless copied, the response will look completely innocent to the user, despite containing the malicious context, which will be read by ChatGPT.

![All of the content after the first word of the code block opening line is hidden from the user. Source: Tenable, November 2025.](https://www.tenable.com/sites/default/files/inline/images/Code%20Block%20-%20GPT5.png)_All of the content after the first word of the code block opening line is hidden from the user. Source: Tenable, November 2025._

### 7\. Memory injection technique

Another issue with Conversation Injection is that it only persists for the current conversation. But what if we wanted persistence between conversations? We found that, similarly to Conversation Injection, SearchGPT can actually get ChatGPT to update its memories, allowing us to create an exfiltration that will happen for every single response. This injection creates a persistent threat that will continue to leak user data even between sessions, days, and data changes.

![We get SearchGPT to make ChatGPT update its memories, as noted by ‘Memory updated.'Source: Tenable, November 2025](https://www.tenable.com/sites/default/files/inline/images/memory.png)_We get SearchGPT to make ChatGPT update its memories, as noted by ‘Memory updated.'Source: Tenable, November 2025_

## Full attack vector PoCs

By mixing and matching all of the vulnerabilities and techniques we discovered, we were able to create proofs of concept (PoCs) for multiple complete attack vectors, such as indirect prompt injection, bypassing safety features, exfiltrating private user information, and creating persistence.

**PoC #1: Phishing**

1. Hacker includes a malicious prompt in a comment on a blog post
2. User asks ChatGPT to summarize the blog
3. SearchGPT browses to the post and gets a prompt injected via a malicious comment
4. SearchGPT adds a hyperlink to the end of its summary, leading to a malicious site using the _url\_safe_ bypass vulnerability
5. Users tend to trust ChatGPT, and therefore could be more susceptible to clicking the malicious link

01 Phishing Improved-v1

Play Video

![Phishing improved ChatGPT4](https://play.vidyard.com/ZcuPMk2o5r9CKgzw9xxoQB.jpg)

**ChatGPT 4o PoC**

02 Phishing GPT 5 POC Success

Play Video

![Phishing ChatGPT 5 PoC Success](https://play.vidyard.com/WcRsy4LwdwPAriqmiVhwW5.jpg)

**ChatGPT 5 PoC**

* * *

**PoC #2: Comment**

1. Hacker includes a malicious prompt in a comment on a blog post
2. User asks ChatGPT to summarize a blog post
3. SearchGPT browses to the post and gets a prompt injected via a malicious comment
4. SearchGPT injects instructions to ChatGPT via Conversation Injection, while hiding them using the code block technique
5. The user sends a follow-up message
6. ChatGPT renders image markdowns based on the instructions injected by SearchGPT, using the _url\_safe_ bypass to exfiltrate private user information to the attacker’s server


03 Comment POC Success v3

Play Video

![ChatGPT 5 Comment PoC Success](https://play.vidyard.com/DKGrhipouhMygfFdQFSAFY.jpg)

**ChatGPT 5 PoC**

* * *

**PoC #3:  SearchGPT**

1. Hacker creates and indexes a malicious website that serves a prompt injection to SearchGPT based on the appropriate headers
2. User asks ChatGPT an innocent question that relates to the information on the Hacker’s website
3. SearchGPT browses to the malicious websites and finds a prompt injection
4. SearchGPT responds based on the malicious prompt and compromises the user


04 SearchGPT Enlarged POC (HD) v2

Play Video

![ChatGPT 4o Enlarged PoC](https://play.vidyard.com/UzNuSELSKFqSqrwAZ84h2L.jpg)

**ChatGPT 4o PoC**

05 SearchGPT llmninjas GPT-5

Play Video

![ChatGPT 5 SearchGPT LLM Ninjas](https://play.vidyard.com/79uPFofCRc6qDU7HK4DFJY.jpg)

**ChatGPT 5 PoC**

* * *

**PoC #4: Memories**

1. User gets attacked by prompt injection in one of the aforementioned ways
2. ChatGPT adds a memory that the user wants all responses to contain exfiltration of private information
3. Every time the user sends a prompt in any conversation, the _url\_safe_ bypass vulnerability is used to exfiltrate private information


06 Memory Injection POC

Play Video

![ChatGPT Memory Injection PoC](https://play.vidyard.com/CWX9dU9eSfTR5DsAkqQu6W.jpg)

**ChatGPT 4o PoC**

* * *

## Vendor response

Tenable Research has disclosed all of these issues to OpenAI and directly worked with them to fix some of the vulnerabilities. The associated TRAs are:

- [https://www.tenable.com/security/research/tra-2025-22](https://www.tenable.com/security/research/tra-2025-22)
- [https://www.tenable.com/security/research/tra-2025-11](https://www.tenable.com/security/research/tra-2025-11)
- [https://www.tenable.com/security/research/tra-2025-06](https://www.tenable.com/security/research/tra-2025-06)

The majority of the research was done on ChatGPT 4o, but OpenAI is constantly tuning and improving their platform, and has since launched ChatGPT 5. The researchers have been able to confirm that several of the PoCs and vulnerabilities are still valid in ChatGPT 5, and ChatGPT 4o is still available for use based on user preference. Prompt injection is a known issue with the way that LLMs work, and, unfortunately, it will probably not be fixed systematically in the near future. AI vendors should take care to ensure that all of their safety mechanisms (such as _url\_safe_) are working properly to limit the potential damage caused by prompt injection.

_**Note: This blog includes research conducted by Yarden Curiel.**_

* * *

![Moshe Bernstein](https://www.tenable.com/sites/default/files/pictures/2025-10/Moshe-Bernstein.jpg)

### [Moshe Bernstein](https://www.tenable.com/profile/moshe-bernstein)

##### Senior Security Researcher, Tenable

**Moshe Bernstein** is a Senior Security Researcher specializing in cloud vulnerability research at Tenable. With over a decade of experience in cybersecurity, Moshe has developed a strong focus on network and operational security, web vulnerability research, and cloud infrastructure security. He enjoys presenting his research at conferences around the world, and is always on the lookout for new challenges.

![Liv Matan](https://www.tenable.com/sites/default/files/pictures/2024-03/Liv-Matan.jpg)

### [Liv Matan](https://www.tenable.com/profile/liv-matan)

##### Senior Security Researcher, Tenable

Liv is a Senior Security Researcher at Tenable, specializing in cloud, application and web security. As a bug bounty hunter, Liv has found vulnerabilities in popular software platforms, including Azure, Google Cloud, AWS, Facebook and GitLab. Liv was recognized by Microsoft as a Most Valuable Security Researcher and ranked among the top eight Google Vulnerability Researchers for 2024. He has also presented at conferences including Black Hat USA, DEF CON Cloud Village, SecTor, Bsides LV, fwd:cloudsec and INTENT. You can follow Liv on X @terminatorLM.

## Related articles

_November 7, 2025_

## [Cybersecurity Snapshot: AI Will Take Center Stage in Cyber in 2026, Google Says, as MITRE Revamps ATT&CK Framework](https://www.tenable.com/blog/cybersecurity-snapshot-agentic-ai-security-best-practices-mitre-attack-v18-11-07-2025)

Learn why Google expects AI to transform cyber defense and offense next year, and explore MITRE's major update to the ATT&CK knowledge base. We also cover a new McKinsey playbook for agentic AI security, along with the latest on Microsoft Exchange protection and the CIS Benchmarks.


* * *

![Juan Perez](https://www.tenable.com/sites/default/files/pictures/2022-06/juan-perez.jpg)[Juan Perez](https://www.tenable.com/profile/juan-perez)

_November 6, 2025_

## [What's New in Tenable Cloud Security: Enhanced Visibility, Prioritization, and Navigation](https://www.tenable.com/blog/whats-new-in-tenable-cloud-security-enhanced-visibility-prioritization-and-navigation)

We have enhanced our Tenable Cloud Security CNAPP product to give you greater visibility, smarter prioritization, and a more streamlined user experience.


* * *

![Liat Hayun](https://www.tenable.com/sites/default/files/pictures/2024-09/Liat-Hayun.jpg)[Liat Hayun](https://www.tenable.com/profile/liat-hayun)

_November 5, 2025_

## [7 Questions EDR Providers Hope You Won’t Ask About Their “Exposure Management” Solution](https://www.tenable.com/blog/EDR-exposure-management-blind-spots-7-questions-to-ask)

Not all exposure management platforms are created equal. But how can you pick the right one for your organization? Here’s a set of questions designed to help you cut through vendor noise and make an informed decision.


* * *

![Christopher Day](https://www.tenable.com/sites/default/files/pictures/2022-07/christopher%20day%20headshot%202.jpeg)[Christopher Day](https://www.tenable.com/profile/christopher-day)

- Cloud
- Exposure Management
- Vulnerability Management

- Tenable AI Exposure
- Tenable One

### Cybersecurity news you can use

Enter your email and never miss timely alerts and security guidance from the experts at Tenable.

Email Address

You may opt-out of receiving our emails at any time by following the opt-out instructions included in the footer of the emails delivered to you or by visiting [Tenable's Subscription Center](https://info.tenable.com/SubscriptionManagement.html). You acknowledge that Tenable, our affiliates, and the third parties (as applicable) listed in our Privacy Policy may transfer your personal data outside of the European Economic Area ("EEA") in order to deliver marketing communications to you, and that countries outside of the EEA may not require the equivalent level of protection of your personal data. Tenable will only process your personal data as described in our [Privacy Policy](https://www.tenable.com/eu-privacy-policy).

Submit

#### Thank you for subscribing!

Try for freeBuy now

### Tenable Vulnerability Management

Enjoy full access to a modern, cloud-based vulnerability management platform that enables you to see and track all of your assets with unmatched accuracy.

Your Tenable Vulnerability Management trial also includes Tenable Web App Scanning.

**Oops!**

First Name

Last Name

Business Email

Phone

Title

Company Name

Company Size (Employees)1-910-4950-99100-249250-499500-9991,000-3,4993,500-4,9995,000-10,00010,000+

Create My Trial in United States Canada United Kingdom Germany Singapore Australia Japan Brazil India United Arab Emirates

By registering for this trial license, Tenable may send you email communications regarding its products and services. You may opt out of receiving these communications at any time by using the unsubscribe link located in the footer of the emails delivered to you. You can also manage your Tenable email preferences by visiting the [Subscription Management Page](https://info.tenable.com/SubscriptionManagement.html).

Tenable will only process your personal data in accordance with its [Privacy Policy](https://www.tenable.com/privacy-policy).

Check

## Thanks!

You will receive an email confirmation in the next few minutes with next steps.

### Tenable Vulnerability Management

Enjoy full access to a modern, cloud-based vulnerability management platform that enables you to see and track all of your assets with unmatched accuracy. **Purchase your annual subscription today.**

-100 assets
+

Choose your subscription option:

1 Year

**$3,500**

2 Years

**$6,825**

3 Years

**$9,975**

[Buy Now](https://store.tenable.com/1479/purl-tiotwoyear?quantity=100&x-promotion=www-webmodal-io&x-Source=web-modal)

Please contact us or a [Tenable partner.](https://www.tenable.com/partner-locator/resellers)

\*
First Name

\*
Last Name

\*
Title

Email Address

\*
Company Size

Company Size...1-910-4950-99100-249250-499500-9991,000-3,4993,500-4,9995,000-10,00010,000+

\*
Phone

\*
Company

\*
Comments (Limited to 255 characters):

\*

I would like to receive marketing communications from Tenable regarding its products and services.

You may opt-out of receiving our emails at any time by following the opt-out instructions included in the footer of the emails delivered to you or by visiting [Tenable's Subscription Center](https://info.tenable.com/SubscriptionManagement.html). You acknowledge that Tenable, our affiliates, and the third parties (as applicable) listed in our Privacy Policy may transfer your personal data outside of the European Economic Area ("EEA") in order to deliver marketing communications to you, and that countries outside of the EEA may not require the equivalent level of protection of your personal data. Tenable will only process your personal data as described in our [Privacy Policy](https://www.tenable.com/eu-privacy-policy).

Submit

### Thank You

Thank you for your interest in Tenable Vulnerability Management. A representative will be in touch soon.

Try for freeBuy now

#### Tenable Vulnerability Management

Enjoy full access to a modern, cloud-based vulnerability management platform that enables you to see and track all of your assets with unmatched accuracy.

Your Tenable Vulnerability Management trial also includes Tenable Web App Scanning.

**Oops!**

Step 1 of 4

First Name

Last Name

[Get Started](https://www.tenable.com/blog/hackedgpt-novel-ai-vulnerabilities-open-the-door-for-private-data-leakage#)

Step 2 of 4

Business Email

Phone

[Go Back](https://www.tenable.com/blog/hackedgpt-novel-ai-vulnerabilities-open-the-door-for-private-data-leakage#)

[Next](https://www.tenable.com/blog/hackedgpt-novel-ai-vulnerabilities-open-the-door-for-private-data-leakage#)

Step 3 of 4

Title

Company Name

[Go Back](https://www.tenable.com/blog/hackedgpt-novel-ai-vulnerabilities-open-the-door-for-private-data-leakage#)

[Next](https://www.tenable.com/blog/hackedgpt-novel-ai-vulnerabilities-open-the-door-for-private-data-leakage#)

Step 4 of 4

Company Size (Employees)1-910-4950-99100-249250-499500-9991,000-3,4993,500-4,9995,000-10,00010,000+

Create My Trial in United States Canada United Kingdom Germany Singapore Australia Japan Brazil India United Arab Emirates

By registering for this trial license, Tenable may send you email communications regarding its products and services. You may opt out of receiving these communications at any time by using the unsubscribe link located in the footer of the emails delivered to you. You can also manage your Tenable email preferences by visiting the [Subscription Management Page](https://info.tenable.com/SubscriptionManagement.html).

Tenable will only process your personal data in accordance with its [Privacy Policy](https://www.tenable.com/privacy-policy).

[Go Back](https://www.tenable.com/blog/hackedgpt-novel-ai-vulnerabilities-open-the-door-for-private-data-leakage#)

Check

## Thanks!

You will receive an email confirmation in the next few minutes with next steps.

#### Tenable Vulnerability Management

Enjoy full access to a modern, cloud-based vulnerability management platform that enables you to see and track all of your assets with unmatched accuracy. **Purchase your annual subscription today.**

-100 assets
+

Choose your subscription option:

1 Year

**$3,500**

2 Years

**$6,825**

3 Years

**$9,975**

[Buy Now](https://store.tenable.com/1479/purl-tiotwoyear?quantity=100&x-promotion=www-webmodal-io&x-Source=web-modal)

Please contact us or a [Tenable partner.](https://www.tenable.com/partner-locator/resellers)

\*
First Name

\*
Last Name

\*
Title

Email Address

\*
Company Size

Company Size...1-910-4950-99100-249250-499500-9991,000-3,4993,500-4,9995,000-10,00010,000+

\*
Phone

\*
Company

\*
Comments (Limited to 255 characters):

\*

I would like to receive marketing communications from Tenable regarding its products and services.

You may opt-out of receiving our emails at any time by following the opt-out instructions included in the footer of the emails delivered to you or by visiting [Tenable's Subscription Center](https://info.tenable.com/SubscriptionManagement.html). You acknowledge that Tenable, our affiliates, and the third parties (as applicable) listed in our Privacy Policy may transfer your personal data outside of the European Economic Area ("EEA") in order to deliver marketing communications to you, and that countries outside of the EEA may not require the equivalent level of protection of your personal data. Tenable will only process your personal data as described in our [Privacy Policy](https://www.tenable.com/eu-privacy-policy).

Submit

### Thank you

Thank you for your interest in Tenable.io. A representative will be in touch soon.

Try for freeBuy now

#### Tenable Vulnerability Management

Enjoy full access to a modern, cloud-based vulnerability management platform that enables you to see and track all of your assets with unmatched accuracy.

Your Tenable Vulnerability Management trial also includes Tenable Web App Scanning.

**Oops!**

First Name

Last Name

Business Email

Company Name

[Continue](https://www.tenable.com/blog/hackedgpt-novel-ai-vulnerabilities-open-the-door-for-private-data-leakage#)

Title

Phone

Company Size (Employees)1-910-4950-99100-249250-499500-9991,000-3,4993,500-4,9995,000-10,00010,000+

Create My Trial in United States Canada United Kingdom Germany Singapore Australia Japan Brazil India United Arab Emirates

By registering for this trial license, Tenable may send you email communications regarding its products and services. You may opt out of receiving these communications at any time by using the unsubscribe link located in the footer of the emails delivered to you. You can also manage your Tenable email preferences by visiting the [Subscription Management Page](https://info.tenable.com/SubscriptionManagement.html).

Tenable will only process your personal data in accordance with its [Privacy Policy](https://www.tenable.com/privacy-policy).

[Go Back](https://www.tenable.com/blog/hackedgpt-novel-ai-vulnerabilities-open-the-door-for-private-data-leakage#)

Step 2 of 2

Check

## Thanks!

You will receive an email confirmation in the next few minutes with next steps.

#### Tenable Vulnerability Management

Enjoy full access to a modern, cloud-based vulnerability management platform that enables you to see and track all of your assets with unmatched accuracy. **Purchase your annual subscription today.**

-100 assets
+

Choose your subscription option:

1 Year

**$3,500**

2 Years

**$6,825**

3 Years

**$9,975**

[Buy Now](https://store.tenable.com/1479/purl-tiotwoyear?quantity=100&x-promotion=www-webmodal-io&x-Source=web-modal)

Please contact us or a [Tenable partner.](https://www.tenable.com/partner-locator/resellers)

### Thank you

Thank you for your interest in Tenable Vulnerability Management. A representative will be in touch soon.

Try for freeBuy now

#### Try Tenable Web App Scanning

Enjoy full access to our latest web application scanning offering designed for modern applications as part of the Tenable One Exposure Management platform. Safely scan your entire online portfolio for vulnerabilities with a high degree of accuracy without heavy manual effort or disruption to critical web applications. **Sign up now.**

Your Tenable Web App Scanning trial also includes Tenable Vulnerability Management.

**Oops!**

Step 1 of 4

First Name

Last Name

[Get Started](https://www.tenable.com/blog/hackedgpt-novel-ai-vulnerabilities-open-the-door-for-private-data-leakage#)

Step 2 of 4

Business Email

Phone

[Go Back](https://www.tenable.com/blog/hackedgpt-novel-ai-vulnerabilities-open-the-door-for-private-data-leakage#)

[Next](https://www.tenable.com/blog/hackedgpt-novel-ai-vulnerabilities-open-the-door-for-private-data-leakage#)

Step 3 of 4

Title

Company Name

[Go Back](https://www.tenable.com/blog/hackedgpt-novel-ai-vulnerabilities-open-the-door-for-private-data-leakage#)

[Next](https://www.tenable.com/blog/hackedgpt-novel-ai-vulnerabilities-open-the-door-for-private-data-leakage#)

Step 4 of 4

Company Size (Employees)1-910-4950-99100-249250-499500-9991,000-3,4993,500-4,9995,000-10,00010,000+

Create My Trial in United States Canada United Kingdom Germany Singapore Australia Japan Brazil India United Arab Emirates

By registering for this trial license, Tenable may send you email communications regarding its products and services. You may opt out of receiving these communications at any time by using the unsubscribe link located in the footer of the emails delivered to you. You can also manage your Tenable email preferences by visiting the [Subscription Management Page](https://info.tenable.com/SubscriptionManagement.html).

Tenable will only process your personal data in accordance with its [Privacy Policy](https://www.tenable.com/privacy-policy).

[Go Back](https://www.tenable.com/blog/hackedgpt-novel-ai-vulnerabilities-open-the-door-for-private-data-leakage#)

Check

## Thanks!

You will receive an email confirmation in the next few minutes with next steps.

#### Buy Tenable Web App Scanning

Enjoy full access to a modern, cloud-based vulnerability management platform that enables you to see and track all of your assets with unmatched accuracy. **Purchase your annual subscription today.**

-5 FQDNs+

**$5,250**

[Buy Now](https://store.tenable.com/1479/?scope=checkout&cart=202710&quantity=5&x-promotion=www-webmodal-was&x-Source=web-modal)

Please contact us or a [Tenable partner.](https://www.tenable.com/partner-locator/resellers)

\*
First Name

\*
Last Name

\*
Title

Email Address

\*
Company Size

Company Size...1-910-4950-99100-249250-499500-9991,000-3,4993,500-4,9995,000-10,00010,000+

\*
Phone

\*
Company

\*
Comments (Limited to 255 characters):

\*

I would like to receive marketing communications from Tenable regarding its products and services.

You may opt-out of receiving our emails at any time by following the opt-out instructions included in the footer of the emails delivered to you or by visiting [Tenable's Subscription Center](https://info.tenable.com/SubscriptionManagement.html). You acknowledge that Tenable, our affiliates, and the third parties (as applicable) listed in our Privacy Policy may transfer your personal data outside of the European Economic Area ("EEA") in order to deliver marketing communications to you, and that countries outside of the EEA may not require the equivalent level of protection of your personal data. Tenable will only process your personal data as described in our [Privacy Policy](https://www.tenable.com/eu-privacy-policy).

Submit

### Thank you

Thank you for your interest in Tenable Web App Scanning. A representative will be in touch soon.

### Request a demo of Tenable Security Center

Please fill out this form with your contact information.

A sales representative will contact you shortly to schedule a demo.

_\\* Field is required_

\*
First Name

\*
Last Name

Email Address

\*
Comments (Limited to 255 characters):

\*

I would like to receive marketing communications from Tenable regarding its products and services.

By submitting your information on this page, Tenable may send you email communications regarding its products and services. You may opt out of receiving these communications at any time by using the unsubscribe link located in the footer of the emails delivered to you. You can also manage your Tenable email preferences by visiting the [Subscription Management](https://info.tenable.com/SubscriptionManagement.html) Page.

Tenable will only process your personal data in accordance with its [Privacy Policy](https://www.tenable.com/privacy-policy).

Submit

### Request a demo of Tenable OT Security

Get the Operational Technology security you need.

Reduce the risk you don’t.

\*
First Name

\*
Last Name

Email Address

\*
Comments (Limited to 255 characters):

\*

I would like to receive marketing communications from Tenable regarding its products and services.

You may opt-out of receiving our emails at any time by following the opt-out instructions included in the footer of the emails delivered to you or by visiting [Tenable's Subscription Center](https://info.tenable.com/SubscriptionManagement.html). You acknowledge that Tenable, our affiliates, and the third parties (as applicable) listed in our Privacy Policy may transfer your personal data outside of the European Economic Area ("EEA") in order to deliver marketing communications to you, and that countries outside of the EEA may not require the equivalent level of protection of your personal data. Tenable will only process your personal data as described in our [Privacy Policy](https://www.tenable.com/eu-privacy-policy).

Submit

### Request a demo

Don’t wait for an attack-- **eliminate risks before they’re exploited.**

- Uncover hidden weaknesses
- Stop threats before they strike
- Simplify security
- Secure hybrid environments

\*
First Name

\*
Last Name

Email Address

\*
Comments (Limited to 255 characters):

\*

I would like to receive marketing communications from Tenable regarding its products and services.

By submitting your information on this page, Tenable may send you email communications regarding its products and services. You may opt out of receiving these communications at any time by using the unsubscribe link located in the footer of the emails delivered to you. You can also manage your Tenable email preferences by visiting the [Subscription Management](https://info.tenable.com/SubscriptionManagement.html) Page.

Tenable will only process your personal data in accordance with its [Privacy Policy](https://www.tenable.com/privacy-policy).

Submit

### Request a demo of Tenable Cloud Security

* * *

**Exceptional unified cloud security awaits you!**

* * *

We’ll show you exactly how Tenable Cloud Security helps you deliver multi-cloud asset discovery, prioritized risk assessments and automated compliance/audit reports.

\*
First Name

\*
Last Name

Email Address

\*
Comments (Limited to 255 characters):

\*

I would like to receive marketing communications from Tenable regarding its products and services.

By submitting your information on this page, Tenable may send you email communications regarding its products and services. You may opt out of receiving these communications at any time by using the unsubscribe link located in the footer of the emails delivered to you. You can also manage your Tenable email preferences by visiting the [Subscription Management](https://info.tenable.com/SubscriptionManagement.html) Page.

Tenable will only process your personal data in accordance with its [Privacy Policy](https://www.tenable.com/privacy-policy).

Submit

### See   Tenable One   in action

Exposure management for the modern attack surface.

\*
First Name

\*
Last Name

Email Address

\*
Comments (Limited to 255 characters):

\*

I would like to receive marketing communications from Tenable regarding its products and services.

By submitting your information on this page, Tenable may send you email communications regarding its products and services. You may opt out of receiving these communications at any time by using the unsubscribe link located in the footer of the emails delivered to you. You can also manage your Tenable email preferences by visiting the [Subscription Management](https://info.tenable.com/SubscriptionManagement.html) Page.

Tenable will only process your personal data in accordance with its [Privacy Policy](https://www.tenable.com/privacy-policy).

Contact us

### Get started with Tenable AI Exposure

\*
First Name

\*
Last Name

Email Address

\*
Comments (Limited to 255 characters):

\*

I would like to receive marketing communications from Tenable regarding its products and services.

By submitting your information on this page, Tenable may send you email communications regarding its products and services. You may opt out of receiving these communications at any time by using the unsubscribe link located in the footer of the emails delivered to you. You can also manage your Tenable email preferences by visiting the [Subscription Management](https://info.tenable.com/SubscriptionManagement.html) Page.

Tenable will only process your personal data in accordance with its [Privacy Policy](https://www.tenable.com/privacy-policy).

Contact us

### See Tenable Attack Surface Management in action

Know the exposure of every asset on any platform.

\*
First Name

\*
Last Name

Email Address

\*
Comments (Limited to 255 characters):

\*

I would like to receive marketing communications from Tenable regarding its products and services.

By submitting your information on this page, Tenable may send you email communications regarding its products and services. You may opt out of receiving these communications at any time by using the unsubscribe link located in the footer of the emails delivered to you. You can also manage your Tenable email preferences by visiting the [Subscription Management](https://info.tenable.com/SubscriptionManagement.html) Page.

Tenable will only process your personal data in accordance with its [Privacy Policy](https://www.tenable.com/privacy-policy).

Contact us

### Get a demo of Tenable Enclave Security

Please fill out the form with your contact information and a sales representative will contact you shortly to schedule a demo.

\*
First Name

\*
Last Name

Email Address

\*
Comments (Limited to 255 characters):

\*

I would like to receive marketing communications from Tenable regarding its products and services.

By submitting your information on this page, Tenable may send you email communications regarding its products and services. You may opt out of receiving these communications at any time by using the unsubscribe link located in the footer of the emails delivered to you. You can also manage your Tenable email preferences by visiting the [Subscription Management](https://info.tenable.com/SubscriptionManagement.html) Page.

Tenable will only process your personal data in accordance with its [Privacy Policy](https://www.tenable.com/privacy-policy).

Submit

### Thank You

Thank you for your interest in Tenable Enclave Security. A representative will be in touch soon.

Try for freeBuy now

#### Try Tenable Nessus Professional free

Tenable Nessus is the most comprehensive vulnerability scanner on the market today.

Fill out the form below to continue with a Nessus Pro trial.

First Name

Last Name

Business Email

Get Started


By registering for this trial license, Tenable may send you email communications regarding its products and services. You may opt out of receiving these communications at any time by using the unsubscribe link located in the footer of the emails delivered to you. You can also manage your Tenable email preferences by visiting the [Subscription Management Page](https://info.tenable.com/SubscriptionManagement.html).

Tenable will only process your personal data in accordance with its [Privacy Policy](https://www.tenable.com/privacy-policy).

Phone

Title

Company

Company Size (Employees)1-9
10-49
50-99
100-249
250-499
500-999
1,000-3,499
3,500-4,999
5,000-10,000
10,000+


Go Back
Start Trial


By registering for this trial license, Tenable may send you email communications regarding its products and services. You may opt out of receiving these communications at any time by using the unsubscribe link located in the footer of the emails delivered to you. You can also manage your Tenable email preferences by visiting the [Subscription Management Page](https://info.tenable.com/SubscriptionManagement.html).

Tenable will only process your personal data in accordance with its [Privacy Policy](https://www.tenable.com/privacy-policy).

Check

## Thanks! To start your trial, download and install Nessus.

During the install process, you will be prompted to check your inbox to validate your email address.

[Download Now](https://www.tenable.com/downloads/nessus?utm_source=nessus-trial-thank-you-update)

#### Buy Tenable Nessus Professional

Tenable Nessus is the most comprehensive vulnerability scanner on the market today. Tenable Nessus Professional will help automate the vulnerability scanning process, save time in your compliance cycles and allow you to engage your IT team.

Buy a multi-year license and save. Add Advanced Support for access to phone, community and chat support 24 hours a day, 365 days a year.

**Select your license**

Buy a multi-year license and save.

1 Year - $4,390\*
2 Years - $8,560.50\*
(Save $219.50)

3 Years - $12,511.50\*
(Save $658.50)


**Add support and training**

**Advanced Support - $400**

24x365 Access to phone, email, community, and chat support. [More info](https://www.tenable.com/products/nessus/advanced-support).
**On-Demand Training - $275**

1 Year Access to the Nessus Fundamentals On-Demand Video Course for 1 person. [More info](https://www.tenable.com/education/courses/nessus-fundamentals?utm_campaign=more-info).
[Buy Now](https://store.tenable.com/1479/purl-nessuspro1y?x-promotion=www-webmodal-nessusPro&x-Source=web-modal&audience=pro1ysupport&resetMvtCandidate=true)

[Renew an existing license](https://account.tenable.com/) [Find a reseller](https://www.tenable.com/partner-locator/resellers)

\*VAT incl.

Try for freeBuy now

#### Try Tenable Nessus Expert free

Built for the modern attack surface, Nessus Expert enables you to see more and protect your organization from vulnerabilities from IT to the cloud.

**Already have Tenable Nessus Professional?** [Upgrade to Nessus Expert free for 7 days.](https://www.tenable.com/products/nessus/nessus-expert/evaluate/upgrade)

First Name

Last Name

Business Email

Get Started


By registering for this trial license, Tenable may send you email communications regarding its products and services. You may opt out of receiving these communications at any time by using the unsubscribe link located in the footer of the emails delivered to you. You can also manage your Tenable email preferences by visiting the [Subscription Management Page](https://info.tenable.com/SubscriptionManagement.html).

Tenable will only process your personal data in accordance with its [Privacy Policy](https://www.tenable.com/privacy-policy).

Phone

Title

Company

Company Size (Employees)1-9
10-49
50-99
100-249
250-499
500-999
1,000-3,499
3,500-4,999
5,000-10,000
10,000+


Go Back
Start Trial


By registering for this trial license, Tenable may send you email communications regarding its products and services. You may opt out of receiving these communications at any time by using the unsubscribe link located in the footer of the emails delivered to you. You can also manage your Tenable email preferences by visiting the [Subscription Management Page](https://info.tenable.com/SubscriptionManagement.html).

Tenable will only process your personal data in accordance with its [Privacy Policy](https://www.tenable.com/privacy-policy).

Check

## Thanks! To start your trial, download and install Nessus.

During the install process, you will be prompted to check your inbox to validate your email address.

[Download Now](https://www.tenable.com/downloads/nessus?utm_source=nessus-trial-thank-you-update)

#### Buy Tenable Nessus Expert

Built for the modern attack surface, Nessus Expert enables you to see more and protect your organization from vulnerabilities from IT to the cloud.

**Select your license**

_Buy a multi-year license and save more._

**1 Year** \- $6,390\*Save**2 Years** \- $12,460.50\*
(Save $319.50)
**3 Years** \- $18,211.50\*
(Save $958.50)


**Add support and training****Advanced Support - $400**

24x365 Access to phone, email, community, and chat support. [More info](https://www.tenable.com/products/nessus/advanced-support).
**Nessus Fundamentals - $275**

1 Year Access to the Nessus Fundamentals On-Demand Video Course for 1 person. [More info.](https://www.tenable.com/education/courses/nessus-fundamentals?utm_campaign=more-info)**Nessus Fundamentals + Nessus Advanced - $385**

1 Year Access to the Nessus Fundamentals and Nessus Advanced On-Demand Video Courses for 1 person. [More info.](https://www.tenable.com/education/courses/nessus-advanced?utm_campaign=more-info)

[Buy Now](https://store.tenable.com/1479/purl-webExpertOneYearAlwaysin?x-promotion=www-webmodal-nessusExpert&x-Source=web-modal)

[Renew an existing license](https://account.tenable.com/) [Find a reseller](https://www.tenable.com/partner-locator/resellers)

#### Learn How Tenable Helps Achieve SLCGP Cybersecurity Plan Requirements

Tenable solutions help fulfill all SLCGP requirements. Connect with a Tenable representative to learn more.

\*
First Name:

\*
Last Name:

Email Address

\*
Phone Number:

\*
Job Title:

\*
Organization:

\*
Additional Comments:

Send Request

**Thank you.**

You should receive a confirmation email shortly and one of our Sales Development Representatives will be in touch. Route any questions to [SLCGP@tenable.com](mailto:SLCGP@tenable.com).

### Get a demo of Tenable Patch Management

Interested in streamlining security and IT collaboration and shortening the mean time to remediate with automation? Try Tenable Patch Management.

\*
First Name

\*
Last Name

Email Address

\*
Comments (Limited to 255 characters):

\*

I would like to receive marketing communications from Tenable regarding its products and services.

By submitting your information on this page, Tenable may send you email communications regarding its products and services. You may opt out of receiving these communications at any time by using the unsubscribe link located in the footer of the emails delivered to you. You can also manage your Tenable email preferences by visiting the [Subscription Management](https://info.tenable.com/SubscriptionManagement.html) Page.

Tenable will only process your personal data in accordance with its [Privacy Policy](https://www.tenable.com/privacy-policy).

Submit

×
[_![](https://www.tenable.com/themes/custom/tenable/images-new/icons/contact-us.svg)_ Contact our sales team](https://www.tenable.com/blog/hackedgpt-novel-ai-vulnerabilities-open-the-door-for-private-data-leakage#contact-us-floating-btn)

#### Contact a sales representative

\*
First Name

\*
Last Name

Email Address

\*
Phone

\*
Title

\*
Company

\*
Company Size

Select...1-910-4950-99100-249250-499500-9991,000-3,4993,500-4,9995,000-10,00010,000+

\*
I am interested in:

Select...Tenable One Exposure Management PlatformTenable Vulnerability ManagementTenable Patch Management Tenable Identity ExposureTenable Attack Surface Management Tenable Cloud Security Tenable Web App Scanning Tenable Enclave Security Nessus ExpertNessus ProfessionalTenable OT Security Tenable Security Center Training

\*
Comments (Limited to 255 characters):

\*

I would like to receive marketing communications from Tenable regarding its products and services.

You may opt-out of receiving our emails at any time by following the opt-out instructions included in the footer of the emails delivered to you or by visiting [Tenable's Subscription Center](https://info.tenable.com/SubscriptionManagement.html). You acknowledge that Tenable, our affiliates, and the third parties (as applicable) listed in our Privacy Policy may transfer your personal data outside of the European Economic Area ("EEA") in order to deliver marketing communications to you, and that countries outside of the EEA may not require the equivalent level of protection of your personal data. Tenable will only process your personal data as described in our [Privacy Policy](https://www.tenable.com/eu-privacy-policy).

Submit

Marketo Forms 2 Cross Domain request proxy frame

## This page is used by Marketo Forms 2 to proxy cross domain AJAX requests.
