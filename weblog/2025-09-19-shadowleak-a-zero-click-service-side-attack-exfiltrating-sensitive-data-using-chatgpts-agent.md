---
date: '2025-09-25'
description: "**Title: ShadowLeak: Zero-Click Service-Side Data Exfiltration via ChatGPT**\
  \ Research reveals a zero-click vulnerability in ChatGPT\u2019s Deep Research function,\
  \ enabling sensitive data exfiltration from linked Gmail accounts without user interaction.\
  \ The exploit relies on sophisticated social engineering, utilizing hidden prompt\
  \ injections within email HTML to bypass safety protocols. This service-side attack\
  \ operates undetected within OpenAI's cloud infrastructure, evading traditional\
  \ security measures. Mitigation strategies include email sanitization and continuous\
  \ monitoring of agent behavior to prevent malicious intent from guiding operations.\
  \ This vulnerability underscores the need for enhanced security in AI integrations\
  \ across various data access points."
link: /archive/2025-09-19-shadowleak-a-zero-click-service-side-attack-exfiltrating-sensitive-data-using-chatgpts-agent
tags:
- Data Exfiltration
- Cybersecurity
- Prompt Injection
- Social Engineering
- Zero-Click Attack
- weblog
title: "ShadowLeak: A Zero-Click, Service-Side Attack Exfiltrating Sensitive Data\
  \ Using ChatGPT\u2019s Agent"
type: weblog
---

Cool research showing (1) hijacking of Deep Research agent, (2) exfil via gmail write actions.

---

> _“Do deep research on my emails from today … collect everything about …”_

The "collect everything about" reduces the bar for the injection to work. We spent some time going around these specific terms with AgentFlayer. After fiddling around, you can get the injection to work without it.

---

> **Full Name:** _Zvika Rosenberg_

Choice of info to exfil is also really important. ChatGPT is especially reluctant to do anything around secrets. If the data seems benign it would be more willing to exfil it.

---

> In the following we share our research process to craft the prompt injection that pushes the agent to do exactly what we want. This process was a rollercoaster of failed attempts, frustrating roadblocks, and, finally, a breakthrough!

Prompt injection is very much an annoying process of getting the thing to work. The "solution" is to use AI to do it. We typically use Grok or Claude.

---

> **Attempt 3 - Forcing Tool Use:** We crafted a new prompt that explicitly instructed the agent to use the `browser.open()` tool with the malicious URL. This led to **partial success**. The agent would sometimes attempt to use the tool, but the request often failed, likely due to additional security restrictions on suspicious URLs.

This TTP: recon for tools and then invoking tools, is a repeated theme. Works every time.

---

> **Attempt 4 - Adding Persistence:** To overcome this, we added instructions for the agent to "retry several times" and framed the failures as standard network connectivity issues. This improved the success rate, with the agent sometimes performing the HTTP request correctly. However, in other cases, it would call the attacker's URL without attaching the necessary PII parameters.

I wouldn't call this persistence as it doesn't stick around between sessions. But this is a cool new detail, getting the agent to retry in case of failures. 

---

> The agent accepted this reasoning, encoded the PII as a string and transmitted it. This method achieved a **100% success rate** in repeated tests, demonstrating a reliable method for indirect prompt injection and data exfiltration.

This is cool. Getting to a consistent payload is not easy.

---

> The leak is Service-side, occurring entirely from within OpenAI’s cloud environment. The agent’s built-in browsing tool performs the exfiltration autonomously, without any client involvement. Prior research—such as [AgentFlayer](https://labs.zenity.io/p/agentflayer-chatgpt-connectors-0click-attack-5b41?) by Zenity and [EchoLeak](https://www.aim.security/aim-labs/aim-labs-echoleak-blogpost) by Aim Security—demonstrated client-side leaks, where exfiltration was triggered when the agent rendered attacker-controlled content (such as images) in the user’s interface. Our attack broadens the threat surface: instead of relying on what the client displays, it exploits what the backend agent is induced to execute.

Appreciate the shout out. AgentFlayer demonstrates server-side exfil for Copilot Studio, but not for ChatGPT. This is a cool new find by the team at Radware.

