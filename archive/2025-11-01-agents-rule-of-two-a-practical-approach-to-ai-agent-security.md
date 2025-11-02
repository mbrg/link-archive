---
date: '2025-11-01'
description: 'Meta introduces the "Agents Rule of Two" to enhance AI agent security,
  particularly against prompt injection vulnerabilities. This framework allows AI
  agents to only satisfy two out of three properties in a session: processing untrustworthy
  inputs, accessing sensitive data, or communicating externally. This minimizes risks
  such as unauthorized data exfiltration or harmful actions. The strategy emphasizes
  a balance between functionality and security, requiring human oversight for actions
  needing all three properties. As agents gain more capabilities, developers must
  adapt this framework to ensure safety while fulfilling user needs, highlighting
  an evolving landscape in AI security.'
link: https://ai.meta.com/blog/practical-ai-agent-security/
tags:
- Meta AI
- Prompt Injection
- AI Security
- Agent Frameworks
- Software Security
title: 'Agents Rule of Two: A Practical Approach to AI Agent Security'
---

[Go up one level](https://ai.meta.com/blog/practical-ai-agent-security/# "Go up one level") [![Meta](https://scontent.xx.fbcdn.net/v/t39.8562-6/252294889_575082167077436_6034106545912333281_n.svg/meta-logo-primary_standardsize.svg?_nc_cat=108&ccb=1-7&_nc_sid=e280be&_nc_ohc=Uv5iG90FGMEQ7kNvwE0Cjw4&_nc_oc=AdnLctoM2iCaVkNE6cPGmrCm0eYT2enj0fZMHQKuXEltOYsWQUJfM4ncHwUIz90bNfc&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_AfdLv12JTn6iNZ6ADHIa67DMs8AtQEWYkqhZnYwQesaMeA&oe=690B7FF9)](https://ai.meta.com/)

- [Meta AI](https://ai.meta.com/blog/practical-ai-agent-security/#)

- [AI Research](https://ai.meta.com/blog/practical-ai-agent-security/#)

- [The Latest](https://ai.meta.com/blog/)

- [About](https://ai.meta.com/blog/practical-ai-agent-security/#)

- [Get Llama](https://www.llama.com/?utm_source=ai_meta_site&utm_medium=web&utm_content=AI_nav&utm_campaign=09252025_moment)


- [Try Meta AI](https://www.meta.ai/?utm_source=ai_meta_site&utm_medium=web&utm_content=AI_nav&utm_campaign=09252025_moment)
- [Toggle site search](https://ai.meta.com/blog/practical-ai-agent-security/# "Toggle site search")


[Close submenu](https://ai.meta.com/blog/practical-ai-agent-security/# "Close submenu") [Main menu](https://ai.meta.com/blog/practical-ai-agent-security/# "Main menu")

[BACK](https://ai.meta.com/blog/practical-ai-agent-security/# "Go up one level")

- [Explore Meta AI](https://ai.meta.com/meta-ai/)
- [Get Meta AI](https://ai.meta.com/get-meta-ai/)
- [Meta AI Studio](https://ai.meta.com/ai-studio/)

- [Overview](https://ai.meta.com/research/)
- [Projects](https://ai.meta.com/research/#projects)
- [Research Areas](https://ai.meta.com/research/#research-areas)
- [People](https://ai.meta.com/results/?content_types[0]=person)

- [Overview](https://ai.meta.com/about/)
- [Open Source](https://ai.meta.com/opensourceai/)
- [Careers](https://www.metacareers.com/)

Clear

- Clear

- [Meta AI\\
\\
>](https://ai.meta.com/blog/practical-ai-agent-security/#)

- [AI Research\\
\\
>](https://ai.meta.com/blog/practical-ai-agent-security/#)

- [The Latest](https://ai.meta.com/blog/)
- [About\\
\\
>](https://ai.meta.com/blog/practical-ai-agent-security/#)

- [Get Llama](https://www.llama.com/?utm_source=ai_meta_site&utm_medium=web&utm_content=AI_nav&utm_campaign=09252025_moment)

[Try Meta AI](https://www.meta.ai/?utm_source=ai_meta_site&utm_medium=web&utm_content=AI_nav&utm_campaign=09252025_moment)

FEATURED

# Agents Rule of Two: A Practical Approach to AI Agent Security

October 31, 2025•

14 minute read

![](https://scontent.xx.fbcdn.net/v/t39.2365-6/569630476_853480637349455_6406966111987148057_n.png?_nc_cat=101&ccb=1-7&_nc_sid=e280be&_nc_ohc=DWiUu9ko2RgQ7kNvwHs_Qiu&_nc_oc=Admbat1Qrj2EWrjg2_i3V0pw23hyDQYiaRg9P6FBjy4TJDd8OSQm6komx4t6WtdRJmI&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_Afen1aBYD-rOyxImyf7kWx_YA4Qs1vp937sx7VyHQfXh_Q&oe=6920003B)

Imagine a personal AI agent, Email-Bot, that’s designed to help you manage your inbox. In order to provide value and operate effectively, Email-Bot might need to:

- Access unread email contents from various senders to provide helpful summaries
- Read through your existing email inbox to keep track of any important updates, reminders, or context
- Send replies or follow-up emails on your behalf

While the automated email assistant can be of great help, this hypothetical bot can also demonstrate how AI agents are introducing novel risks. Notably, one of the biggest challenges for the industry is that of agents’ susceptibility to [prompt injection](https://en.wikipedia.org/wiki/Prompt_injection).

Prompt injection is a fundamental, unsolved weakness in all LLMs. With prompt injection, certain types of untrustworthy strings or pieces of data — when passed into an AI agent’s context window — can cause unintended consequences, such as ignoring the instructions and safety guidelines provided by the developer or executing unauthorized tasks. This vulnerability could be enough for an attacker to take control of the agent and cause harm to the AI agent’s user.

Using our Email-Bot example, if an attacker puts a prompt injection string in an email to the targeted user, they might be able to hijack the AI agent once that email is processed. Example attacks could include exfiltrating sensitive data, such as private email contents, or taking unwanted actions, such as sending phishing messages to the target’s friends.

Like many of our industry peers, we’re excited by the potential for agentic AI to improve people’s lives and enhance productivity. The path to reach this vision involves granting AI agents like Email-Bot more capabilities, including access to:

- Data sources authored by unknown parties, such as inbound emails or content queried from the internet
- Private or sensitive data that an agent is permitted to use to inform planning and enable higher personalization
- Tools that can be called autonomously to get stuff done on a user’s behalf

At Meta, we’re thinking deeply about how agents can be most useful to people by balancing the utility and flexibility needed for this product vision while minimizing bad outcomes from prompt injection, such as exfiltration of private data, forcing actions to be taken on a user’s behalf, or system disruption. To best protect people and our systems from this known risk, we’ve developed the Agents Rule of Two. When this framework is followed, the severity of security risks is deterministically reduced.

Inspired by the similarly named policy [developed for Chromium](https://chromium.googlesource.com/chromium/src/+/main/docs/security/rule-of-2.md), as well as [Simon Willison’s “lethal trifecta,](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) [”](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) our framework aims to help developers understand and navigate the tradeoffs that exist today with these new powerful agent frameworks.

## Agents Rule of Two

At a high level, the Agents Rule of Two states that until robustness research allows us to reliably detect and refuse prompt injection, agents **must satisfy no more than two** of the following three properties within a session to avoid the highest impact consequences of prompt injection.

**\[A\]** An agent can process untrustworthy inputs

**\[B\]** An agent can have access to sensitive systems or private data

**\[C\]** An agent can change state or communicate externally

It’s still possible that all three properties are necessary to carry out a request. If an agent requires all three without starting a new session (i.e., with a fresh context window), then the agent should not be permitted to operate autonomously and at a minimum requires supervision — via human-in-the-loop approval or another reliable means of validation.

![](https://scontent.xx.fbcdn.net/v/t39.8562-6/574406069_795364830030580_7993774635627241814_n.png?_nc_cat=100&ccb=1-7&_nc_sid=f537c7&_nc_ohc=cbMu9XJUr08Q7kNvwHJ_NZ4&_nc_oc=AdmsKuhdZa5jITPGfIrb4SY51_dxANds8aW8huPXhThJfYZyl2cHuYYOit1PO_Ity2s&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_Affqs4798NDBlWdkks9qVeXD9TXz5x66t1GLhq_qAHoT4g&oe=690B8226)

## How the Agents Rule of Two Stops Exploitation

Let’s return to our example Email-Bot to see how applying the Agents Rule of Two can prevent a data exfiltration attack.

**Attack Scenario:** Prompt injection within a spam email contains a string that instructs a user’s Email-Bot to gather the private contents of the user’s inbox and forward them to the attacker by calling a Send-New-Email tool.

This attack is successful because:

- **\[A\]** The agent has access to untrusted data (spam emails)
- **\[B\]** The agent can access a user’s private data (inbox)
- **\[C\]** The agent can communicate externally (through sending new emails)

With the Agents Rule of Two, this attack can be prevented in a few different ways:

- In a **\[BC\]** configuration, the agent may only process emails from trustworthy senders, such as close friends, preventing the initial prompt injection payload from ever reaching the agent’s context window.
- In an **\[AC\]** configuration, the agent won’t have access to any sensitive data or systems (for instance operating in a test environment for training), so any prompt injection that reaches the agent will result in no meaningful impact.
- In an **\[AB\]** configuration, the agent can only send new emails to trusted recipients or once a human has validated the contents of the draft message, preventing the attacker from ultimately completing their attack chain.

With the Agents Rule of Two, agent developers can compare different designs and their associated tradeoffs (such as user friction or limits on capabilities) to determine which option makes the most sense for their users’ needs.

## Hypothetical Examples and Implementations of the Agents Rule of Two

Let’s look at three other hypothetical agent use cases to see how they might choose to satisfy the framework.

**Travel Agent Assistant \[AB\]**

- This is a public-facing travel assistant that can answer questions and act on a user’s behalf.
- It needs to search the web to get up-to-date information about travel destinations \[A\] and has access to a user’s private info to enable booking and purchasing experiences \[B\].
- To satisfy the Agents Rule of Two, we place preventative controls on its tools and communication \[C\] by:
  - Requesting a human confirmation of any action, like making a reservation or paying a deposit
  - Limiting web requests to URLs exclusively returned from trusted sources like not visiting URLs constructed by the agent

**Web Browsing Research Assistant \[AC\]**

- This agent can interact with a web browser to perform research on a user’s behalf.
- It needs to fill out forms and send a larger number of requests to arbitrary URLs \[C\] and must process the results \[A\] to replan as needed.
- To satisfy the Agents Rule of Two, we place preventative controls around its access to sensitive systems and private data \[B\] by:
  - Running the browser in a restrictive sandbox without preloaded session data
  - Limiting the agent’s access to private information (beyond the initial prompt) and informing the user of how their data might be shared

**High-Velocity Internal Coder \[BC\]**

- This agent can solve engineering problems by generating and executing code across an organization’s internal infrastructure.
- To solve meaningful problems, it must have access to a subset of production systems \[B\] and have the ability to make stateful changes to these systems \[C\]. While human-in-the-loop can be a valuable defense-in-depth, developers aim to unlock operation at scale by minimizing human interventions.
- To satisfy the Agents Rule of Two, we place preventive controls around any sources of untrustworthy data \[A\] by:
  - Using author-lineage to filter all data sources processed within the agent’s context window
  - Providing a human-review process for marking false positives and enabling agents access to data

As is common for general frameworks, the devil is ultimately in the details. In order to enable additional use cases, it can be safe for an agent to transition from one configuration of the Agents Rule of Two to another within the same session. One concrete example would be starting in \[AC\] to access the internet and completing a one-way switch to \[B\] by disabling communication when accessing internal systems.

While all of the specific ways this can be done have been omitted for brevity, readers can infer when this can be safely accomplished through focus on disrupting the exploit path — namely preventing an attack from completing the full chain from \[A\] → \[B\] → \[C\].

Limitations

It’s important to note that satisfying the Agents Rule of Two should not be viewed as sufficient for protecting against other threat vectors common to agents (e.g., attacker uplift, proliferation of spam, agent mistakes, hallucinations, excessive privileges, etc.) or lower consequence outcomes of prompt injection (e.g., misinformation in the agent’s response).

Similarly, applying the Agents Rule of Two should not be viewed as a finish line for mitigating risk. Designs that satisfy the Agents Rule of Two can still be prone to failure (e.g., a user blindly confirming a warning interstitial), and [defense in depth](https://about.fb.com/news/2019/01/designing-security-for-billions/) is a critical component towards mitigating the highest risk scenarios when the failure of a single layer may be likely. The Agents Rule of Two is a supplement — and not a substitute — for common security principles such as least-privilege.

## Existing Solutions

For further AI protection solutions that complement the Agents Rule of Two, read more about our [Llama Protections](https://www.llama.com/llama-protections/). Offerings include Llama Firewall for orchestrating agent protections, Prompt Guard for classifying potential prompt injections, Code Shield to reduce insecure code suggestions, and Llama Guard for classifying potentially harmful content.

## What’s Next

We believe the Agents Rule of Two is a useful framework for developers today. We’re also excited by its potential to enable secure development at scale.

With the adoption of plug-and-play agentic tool-calling through protocols such as Model Context Protocol (MCP), we see both emerging novel risks and opportunities. While blindly connecting agents to new tools can be a recipe for disaster, there’s potential for enabling security-by-default with built-in Rule of Two awareness. For example, by declaring an Agents Rule of Two configuration in supporting tool calls, developers can have increased confidence that an action will succeed, fail, or request additional approval in accordance with their policy.

We also know that as agents become more useful and capabilities grow, some highly sought-after use cases will be difficult to fit cleanly into the Agents Rule of Two, such as a background process where human-in-the-loop is disruptive or ineffective. While we believe that traditional software guardrails and human approvals continue to be the preferred method of satisfying the Agents Rule of Two in present use cases, we’ll continue to pursue research towards satisfying the Agents Rule of Two’s supervisory approval checks via alignment controls, such as oversight agents and the open source LlamaFirewall platform. We look forward to sharing more in the future.

* * *

Share:

* * *

Our latest updates delivered to your inbox

[Subscribe](https://ai.facebook.com/subscribe/) to our newsletter to keep up with Meta AI news, events, research breakthroughs, and more.

## Join us in the pursuit of what’s possible with AI.

[See all open positions](https://www.metacareers.com/jobs/?is_leadership=0&sub_teams%5B0%5D=Artificial+Intelligence&is_in_page=0&fbclid=IwAR0O8BF7opOj5gASJmwYVGalPPXTLu-6xrl9w00eC7Rarp2HQ9uEH8tERFw)

[Our approach](https://ai.meta.com/about)

[About AI at Meta](https://ai.meta.com/about)

[People](https://ai.meta.com/results/?content_types%5B0%5D=person&sort_by=random)

[Careers](https://www.metacareers.com/jobs/?is_leadership=0&sub_teams[0]=Artificial%20Intelligence&is_in_page=0)

[Research](https://ai.meta.com/research)

[Infrastructure](https://ai.meta.com/infrastructure)

[Resources](https://ai.meta.com/resources)

[Demos](https://aidemos.meta.com/)

[Meta AI](https://ai.meta.com/meta-ai/)

[Explore Meta AI](https://ai.meta.com/meta-ai/)

[Get Meta AI](https://ai.meta.com/get-meta-ai/)

[AI Studio](https://ai.meta.com/ai-studio/)

[Latest news](https://ai.meta.com/blog)

[Blog](https://ai.meta.com/blog)

[Newsletter](https://ai.meta.com/subscribe)

Foundational models

[Llama](https://www.llama.com/)

![](https://scontent.xx.fbcdn.net/v/t39.2365-6/87524316_2677189655726266_6338721200264445952_n.svg?_nc_cat=103&ccb=1-7&_nc_sid=e280be&_nc_ohc=WHtvBAeUADkQ7kNvwHuJhaN&_nc_oc=Adll1W86ct3dpkoRbg2WPctcKBlh4BcwFH6gi-K_lEDNlZDZG7BGmDwzh-Y98DjfaEU&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_Afe_NT-TpP5HEx5jCZe_UvrsvaHbNMGtCLiIlnQVcZc0LA&oe=692021F8)

![](https://scontent.xx.fbcdn.net/v/t39.2365-6/85559716_2814260008668824_1992323131183726592_n.svg?_nc_cat=103&ccb=1-7&_nc_sid=e280be&_nc_ohc=c_TnyCiqnWQQ7kNvwGyXzT4&_nc_oc=AdlG68to4UVJhXckCOAsjkym1BK45D902wqEt3-VSD6MbZVpB6EDdAmvrcNFx98hIYM&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_AfdzvV_Ff5sdsHhaKplMrGlQqY4uA9R8_EzWCRQZ2j9zVA&oe=691FEE8F)

[![](https://scontent.xx.fbcdn.net/v/t39.8562-6/335682312_964107378293184_3093631164486164913_n.svg?_nc_cat=100&ccb=1-7&_nc_sid=e280be&_nc_ohc=nxweIh-GeFIQ7kNvwGq_nlr&_nc_oc=AdkQrfEEJSozqvIwzmRc84omolUd76SgaBAqlP_fLCiIFexma3DS9uugVAH_gab3rME&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_Afd8azs6kNlFKsTVLWPWrqPW3_QSKdbvGChRB9aD50LsRw&oe=690BA867)\\
\\
![](https://scontent.xx.fbcdn.net/v/t39.8562-6/335682312_964107378293184_3093631164486164913_n.svg?_nc_cat=100&ccb=1-7&_nc_sid=e280be&_nc_ohc=nxweIh-GeFIQ7kNvwGq_nlr&_nc_oc=AdkQrfEEJSozqvIwzmRc84omolUd76SgaBAqlP_fLCiIFexma3DS9uugVAH_gab3rME&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_Afd8azs6kNlFKsTVLWPWrqPW3_QSKdbvGChRB9aD50LsRw&oe=690BA867)](https://www.facebook.com/aiatmeta/)

[![](https://scontent.xx.fbcdn.net/v/t39.8562-6/336009607_1870102080040414_6753977241281150924_n.svg?_nc_cat=103&ccb=1-7&_nc_sid=e280be&_nc_ohc=uTr1eQWF2QMQ7kNvwGygmm0&_nc_oc=AdliXbYTbaLAzqjTQ7672ycoQzN_RWaX8RQjQsO368EAlKz_kgwHEDTaZI-OKmKKdAw&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_AfegRs0SIb_xpJnjNAf1BzfRM5b8qtWOcyTKCuo_g7cqsA&oe=690BA0A2)\\
\\
![](https://scontent.xx.fbcdn.net/v/t39.8562-6/336009607_1870102080040414_6753977241281150924_n.svg?_nc_cat=103&ccb=1-7&_nc_sid=e280be&_nc_ohc=uTr1eQWF2QMQ7kNvwGygmm0&_nc_oc=AdliXbYTbaLAzqjTQ7672ycoQzN_RWaX8RQjQsO368EAlKz_kgwHEDTaZI-OKmKKdAw&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_AfegRs0SIb_xpJnjNAf1BzfRM5b8qtWOcyTKCuo_g7cqsA&oe=690BA0A2)](https://twitter.com/aiatmeta/)

[![](https://scontent.xx.fbcdn.net/v/t39.8562-6/336289415_1541032296405649_2165099305308791297_n.svg?_nc_cat=109&ccb=1-7&_nc_sid=e280be&_nc_ohc=nwo--MEYb4MQ7kNvwF8aB6c&_nc_oc=AdlnWXO7hw3lOvuaBNYn5lADvIWKIK-hq7MtA5DH5zmJ07PIy8VJN5Rj9RpDtGDwRmM&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_AfdQQH4DOtxGsycixHPJeTN36ZI96DgK4ScFR-9l9O9saQ&oe=690B943B)\\
\\
![](https://scontent.xx.fbcdn.net/v/t39.8562-6/336289415_1541032296405649_2165099305308791297_n.svg?_nc_cat=109&ccb=1-7&_nc_sid=e280be&_nc_ohc=nwo--MEYb4MQ7kNvwF8aB6c&_nc_oc=AdlnWXO7hw3lOvuaBNYn5lADvIWKIK-hq7MtA5DH5zmJ07PIy8VJN5Rj9RpDtGDwRmM&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_AfdQQH4DOtxGsycixHPJeTN36ZI96DgK4ScFR-9l9O9saQ&oe=690B943B)](https://www.linkedin.com/showcase/aiatmeta)

[![](https://scontent.xx.fbcdn.net/v/t39.8562-6/335648731_142576991793348_7786819189843639239_n.svg?_nc_cat=108&ccb=1-7&_nc_sid=e280be&_nc_ohc=dofCodi2jaoQ7kNvwEvC7up&_nc_oc=AdlO6ml629dRhRfgREbGQ5h61xhEvijf7DTcB-YkHdjqKuoaDa9lVSd9yyPOTVjRy4M&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_Afda1XTGfEgKGGEVySZ4Y6ARMDhtXVAhJ3czdd9OhwDxJg&oe=690BADAE)\\
\\
![](https://scontent.xx.fbcdn.net/v/t39.8562-6/335648731_142576991793348_7786819189843639239_n.svg?_nc_cat=108&ccb=1-7&_nc_sid=e280be&_nc_ohc=dofCodi2jaoQ7kNvwEvC7up&_nc_oc=AdlO6ml629dRhRfgREbGQ5h61xhEvijf7DTcB-YkHdjqKuoaDa9lVSd9yyPOTVjRy4M&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_Afda1XTGfEgKGGEVySZ4Y6ARMDhtXVAhJ3czdd9OhwDxJg&oe=690BADAE)](https://www.youtube.com/@aiatmeta)

Our approach

[Our approach](https://ai.meta.com/about) [About AI at Meta](https://ai.meta.com/about) [People](https://ai.meta.com/results/?content_types%5B0%5D=person&sort_by=random) [Careers](https://www.metacareers.com/jobs/?is_leadership=0&sub_teams[0]=Artificial%20Intelligence&is_in_page=0)

Research

[Research](https://ai.meta.com/research) [Infrastructure](https://ai.meta.com/infrastructure) [Resources](https://ai.meta.com/resources) [Demos](https://aidemos.meta.com/)

Meta AI

[Meta AI](https://ai.meta.com/meta-ai/) [Explore Meta AI](https://ai.meta.com/meta-ai/) [Get Meta AI](https://ai.meta.com/get-meta-ai/) [AI Studio](https://ai.meta.com/ai-studio/)

Latest news

[Latest news](https://ai.meta.com/blog) [Blog](https://ai.meta.com/blog) [Newsletter](https://ai.meta.com/subscribe)

Foundational models

[Llama](https://www.llama.com/)

[![](https://scontent.xx.fbcdn.net/v/t39.8562-6/335682312_964107378293184_3093631164486164913_n.svg?_nc_cat=100&ccb=1-7&_nc_sid=e280be&_nc_ohc=nxweIh-GeFIQ7kNvwGq_nlr&_nc_oc=AdkQrfEEJSozqvIwzmRc84omolUd76SgaBAqlP_fLCiIFexma3DS9uugVAH_gab3rME&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_Afd8azs6kNlFKsTVLWPWrqPW3_QSKdbvGChRB9aD50LsRw&oe=690BA867)\\
\\
![](https://scontent.xx.fbcdn.net/v/t39.8562-6/335682312_964107378293184_3093631164486164913_n.svg?_nc_cat=100&ccb=1-7&_nc_sid=e280be&_nc_ohc=nxweIh-GeFIQ7kNvwGq_nlr&_nc_oc=AdkQrfEEJSozqvIwzmRc84omolUd76SgaBAqlP_fLCiIFexma3DS9uugVAH_gab3rME&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_Afd8azs6kNlFKsTVLWPWrqPW3_QSKdbvGChRB9aD50LsRw&oe=690BA867)](https://www.facebook.com/aiatmeta/)

[![](https://scontent.xx.fbcdn.net/v/t39.8562-6/336009607_1870102080040414_6753977241281150924_n.svg?_nc_cat=103&ccb=1-7&_nc_sid=e280be&_nc_ohc=uTr1eQWF2QMQ7kNvwGygmm0&_nc_oc=AdliXbYTbaLAzqjTQ7672ycoQzN_RWaX8RQjQsO368EAlKz_kgwHEDTaZI-OKmKKdAw&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_AfegRs0SIb_xpJnjNAf1BzfRM5b8qtWOcyTKCuo_g7cqsA&oe=690BA0A2)\\
\\
![](https://scontent.xx.fbcdn.net/v/t39.8562-6/336009607_1870102080040414_6753977241281150924_n.svg?_nc_cat=103&ccb=1-7&_nc_sid=e280be&_nc_ohc=uTr1eQWF2QMQ7kNvwGygmm0&_nc_oc=AdliXbYTbaLAzqjTQ7672ycoQzN_RWaX8RQjQsO368EAlKz_kgwHEDTaZI-OKmKKdAw&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_AfegRs0SIb_xpJnjNAf1BzfRM5b8qtWOcyTKCuo_g7cqsA&oe=690BA0A2)](https://twitter.com/aiatmeta/)

[![](https://scontent.xx.fbcdn.net/v/t39.8562-6/336289415_1541032296405649_2165099305308791297_n.svg?_nc_cat=109&ccb=1-7&_nc_sid=e280be&_nc_ohc=nwo--MEYb4MQ7kNvwF8aB6c&_nc_oc=AdlnWXO7hw3lOvuaBNYn5lADvIWKIK-hq7MtA5DH5zmJ07PIy8VJN5Rj9RpDtGDwRmM&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_AfdQQH4DOtxGsycixHPJeTN36ZI96DgK4ScFR-9l9O9saQ&oe=690B943B)\\
\\
![](https://scontent.xx.fbcdn.net/v/t39.8562-6/336289415_1541032296405649_2165099305308791297_n.svg?_nc_cat=109&ccb=1-7&_nc_sid=e280be&_nc_ohc=nwo--MEYb4MQ7kNvwF8aB6c&_nc_oc=AdlnWXO7hw3lOvuaBNYn5lADvIWKIK-hq7MtA5DH5zmJ07PIy8VJN5Rj9RpDtGDwRmM&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_AfdQQH4DOtxGsycixHPJeTN36ZI96DgK4ScFR-9l9O9saQ&oe=690B943B)](https://www.linkedin.com/showcase/aiatmeta)

[![](https://scontent.xx.fbcdn.net/v/t39.8562-6/335648731_142576991793348_7786819189843639239_n.svg?_nc_cat=108&ccb=1-7&_nc_sid=e280be&_nc_ohc=dofCodi2jaoQ7kNvwEvC7up&_nc_oc=AdlO6ml629dRhRfgREbGQ5h61xhEvijf7DTcB-YkHdjqKuoaDa9lVSd9yyPOTVjRy4M&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_Afda1XTGfEgKGGEVySZ4Y6ARMDhtXVAhJ3czdd9OhwDxJg&oe=690BADAE)\\
\\
![](https://scontent.xx.fbcdn.net/v/t39.8562-6/335648731_142576991793348_7786819189843639239_n.svg?_nc_cat=108&ccb=1-7&_nc_sid=e280be&_nc_ohc=dofCodi2jaoQ7kNvwEvC7up&_nc_oc=AdlO6ml629dRhRfgREbGQ5h61xhEvijf7DTcB-YkHdjqKuoaDa9lVSd9yyPOTVjRy4M&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_Afda1XTGfEgKGGEVySZ4Y6ARMDhtXVAhJ3czdd9OhwDxJg&oe=690BADAE)](https://www.youtube.com/@aiatmeta)

[Privacy Policy](https://www.facebook.com/about/privacy/)

[Terms](https://www.facebook.com/policies/)

[Cookies](https://www.facebook.com/policies/cookies/)

Meta © 2025

[![](https://scontent.xx.fbcdn.net/v/t39.8562-6/335682312_964107378293184_3093631164486164913_n.svg?_nc_cat=100&ccb=1-7&_nc_sid=e280be&_nc_ohc=nxweIh-GeFIQ7kNvwGq_nlr&_nc_oc=AdkQrfEEJSozqvIwzmRc84omolUd76SgaBAqlP_fLCiIFexma3DS9uugVAH_gab3rME&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_Afd8azs6kNlFKsTVLWPWrqPW3_QSKdbvGChRB9aD50LsRw&oe=690BA867)\\
\\
![](https://scontent.xx.fbcdn.net/v/t39.8562-6/335682312_964107378293184_3093631164486164913_n.svg?_nc_cat=100&ccb=1-7&_nc_sid=e280be&_nc_ohc=nxweIh-GeFIQ7kNvwGq_nlr&_nc_oc=AdkQrfEEJSozqvIwzmRc84omolUd76SgaBAqlP_fLCiIFexma3DS9uugVAH_gab3rME&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_Afd8azs6kNlFKsTVLWPWrqPW3_QSKdbvGChRB9aD50LsRw&oe=690BA867)](https://www.facebook.com/aiatmeta/)

[![](https://scontent.xx.fbcdn.net/v/t39.8562-6/336009607_1870102080040414_6753977241281150924_n.svg?_nc_cat=103&ccb=1-7&_nc_sid=e280be&_nc_ohc=uTr1eQWF2QMQ7kNvwGygmm0&_nc_oc=AdliXbYTbaLAzqjTQ7672ycoQzN_RWaX8RQjQsO368EAlKz_kgwHEDTaZI-OKmKKdAw&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_AfegRs0SIb_xpJnjNAf1BzfRM5b8qtWOcyTKCuo_g7cqsA&oe=690BA0A2)\\
\\
![](https://scontent.xx.fbcdn.net/v/t39.8562-6/336009607_1870102080040414_6753977241281150924_n.svg?_nc_cat=103&ccb=1-7&_nc_sid=e280be&_nc_ohc=uTr1eQWF2QMQ7kNvwGygmm0&_nc_oc=AdliXbYTbaLAzqjTQ7672ycoQzN_RWaX8RQjQsO368EAlKz_kgwHEDTaZI-OKmKKdAw&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_AfegRs0SIb_xpJnjNAf1BzfRM5b8qtWOcyTKCuo_g7cqsA&oe=690BA0A2)](https://twitter.com/aiatmeta/)

[![](https://scontent.xx.fbcdn.net/v/t39.8562-6/336289415_1541032296405649_2165099305308791297_n.svg?_nc_cat=109&ccb=1-7&_nc_sid=e280be&_nc_ohc=nwo--MEYb4MQ7kNvwF8aB6c&_nc_oc=AdlnWXO7hw3lOvuaBNYn5lADvIWKIK-hq7MtA5DH5zmJ07PIy8VJN5Rj9RpDtGDwRmM&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_AfdQQH4DOtxGsycixHPJeTN36ZI96DgK4ScFR-9l9O9saQ&oe=690B943B)\\
\\
![](https://scontent.xx.fbcdn.net/v/t39.8562-6/336289415_1541032296405649_2165099305308791297_n.svg?_nc_cat=109&ccb=1-7&_nc_sid=e280be&_nc_ohc=nwo--MEYb4MQ7kNvwF8aB6c&_nc_oc=AdlnWXO7hw3lOvuaBNYn5lADvIWKIK-hq7MtA5DH5zmJ07PIy8VJN5Rj9RpDtGDwRmM&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_AfdQQH4DOtxGsycixHPJeTN36ZI96DgK4ScFR-9l9O9saQ&oe=690B943B)](https://www.linkedin.com/showcase/aiatmeta)

[![](https://scontent.xx.fbcdn.net/v/t39.8562-6/335648731_142576991793348_7786819189843639239_n.svg?_nc_cat=108&ccb=1-7&_nc_sid=e280be&_nc_ohc=dofCodi2jaoQ7kNvwEvC7up&_nc_oc=AdlO6ml629dRhRfgREbGQ5h61xhEvijf7DTcB-YkHdjqKuoaDa9lVSd9yyPOTVjRy4M&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_Afda1XTGfEgKGGEVySZ4Y6ARMDhtXVAhJ3czdd9OhwDxJg&oe=690BADAE)\\
\\
![](https://scontent.xx.fbcdn.net/v/t39.8562-6/335648731_142576991793348_7786819189843639239_n.svg?_nc_cat=108&ccb=1-7&_nc_sid=e280be&_nc_ohc=dofCodi2jaoQ7kNvwEvC7up&_nc_oc=AdlO6ml629dRhRfgREbGQ5h61xhEvijf7DTcB-YkHdjqKuoaDa9lVSd9yyPOTVjRy4M&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=8o7n7oJtzLiGltDHrDz9jA&oh=00_Afda1XTGfEgKGGEVySZ4Y6ARMDhtXVAhJ3czdd9OhwDxJg&oe=690BADAE)](https://www.youtube.com/@aiatmeta)

Facebook
