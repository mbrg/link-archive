---
date: '2025-11-03'
description: "OpenAI\u2019s CISO, Dane Stuckey, addresses prompt injection risks associated\
  \ with the ChatGPT Atlas browser. He outlines ongoing efforts to mitigate these\
  \ attacks, which involve hiding malicious instructions within digital content. While\
  \ promising measures like \u201Clogged out mode\u201D and \u201CWatch Mode\u201D\
  \ for sensitive sites are in place, the persistence of prompt injection as a significant\
  \ risk remains concerning. As adversaries evolve their tactics, reliance on overlapping\
  \ guardrails may propagate a false sense of security. The evolution of user awareness\
  \ and AI's accountability in security contexts will be crucial for future developments."
link: /archive/2025-10-23-dane-stuckey-openai-ciso-on-prompt-injection-risks-for-chatgpt-atlas
tags:
- openai
- browser-agents
- security
- ai-agents
- prompt-injection
- weblog
title: Dane Stuckey (OpenAI CISO) on prompt injection risks for ChatGPT Atlas
type: weblog
---

Great to see OpenAI's new CISO engage directly with the community. I agree with more of the viewpoint: prompt injection is malware. But not the implications: more training and giant lists of bad prompts won't help.

---

> OpenAI’s Chief Information Security Officer Dane Stuckey just posted the most detail I’ve seen yet in [a lengthy Twitter post](https://twitter.com/cryps1s/status/1981037851279278414).

It is really awesome of Dane  to openly engage the community and acknowledge the issue.

---

> > One emerging risk we are very thoughtfully researching and mitigating is **prompt injections, where attackers hide malicious instructions in websites, emails, or other sources, to try to trick the agent into behaving in unintended ways**. The objective for attackers can be as simple as trying to bias the agent’s opinion while shopping, or as consequential as an attacker **trying to get the agent to fetch and leak private data**, such as sensitive information from your email, or credentials.

Good to see a callout for more than data exfil. Getting the agent to make bad decisions, in this case recommending the wrong product.

---

> > Our long-term goal is that you should be able to trust ChatGPT agent to use your browser, **the same way you’d trust your most competent, trustworthy, and security-aware colleague** or friend.

This sounds like "one day we'll have AGI and this will no longer be a problem". There is a lot we can do today with engineering, not more training.

---

> > We’re working hard to achieve that. For this launch, we’ve performed extensive red-teaming, implemented novel model training techniques to reward the model for ignoring malicious instructions, **implemented overlapping guardrails and safety measures**, and added new systems to detect and block such attacks. However, **prompt injection remains a frontier, unsolved security problem, and our adversaries will spend significant time and resources to find ways to make ChatGPT agent fall for these attacks**.

Remember about the 18 months ago when OpenAI announced Instruction Hierarchy as the end of most prompt injection attacks? That had no impact on attackers..
"We trained the model real hard not to follow instructions" is mostly wasted effort.
But I'd love to learn more about those overlapping guardrails and safety measures!

---

> > To protect our users, and to help improve our models against these attacks: > > 1. We’ve prioritized rapid response systems to help us quickly identify block attack campaigns as we become aware of them.

This sounds like fast response to bug submissions. Which is nice but irrelevant. Blocking yet another prompt is not a defense strategy it's a PR strategy.

---

> It’s still bad news for users that get caught out by a zero-day prompt injection, but it does at least mean that successful new attack patterns should have a small window of opportunity.

I don't like this term zero-day prompt. Folks, we now auto-generate those prompts. We always have infinite prompts that work. Stop trying to build a perimeter it isn't working.

---

> > 3. We’ve designed Atlas to give you controls to help protect yourself. **We have added a feature to allow ChatGPT agent to take action on your behalf, but without access to your credentials called “logged out mode”**. We recommend this mode when you don’t need to take action within your accounts. **Today, we think “logged in mode” is most appropriate for well-scoped actions on very trusted sites, where the risks of prompt injection are lower**. Asking it to add ingredients to a shopping cart is generally safer than a broad or vague request like “review my emails and take whatever actions are needed.”

Logged out mode is indeed very cool. But will people use it when logged in mode is right there?

---

> > 4. **When agent is operating on sensitive sites, we have also implemented a “Watch Mode” that alerts you to the sensitive nature of the site and requires you have the tab active to watch the agent do its work**. Agent will pause if you move away from the tab with sensitive information. This ensures you stay aware—and in control—of what agent actions the agent is performing. \[...\]

So if the agent is hijacked we home the AI that triggers the watch mode isn't?

---

> I tried just now using both GitHub and an online banking site and neither of them seemed to trigger “watch mode”—Atlas continued to navigate even when I had switched to another application.

Simon is right to expect that whole sites would need watch mode. This is exactly what's needed: hard boundaries. You cannot interact with GitHub without a human in the loop. But domains are way too broad.  They will restrict the utility of the agent and will tire users making them complacent.

---

> > New levels of intelligence and capability require the technology, society, the risk mitigation strategy to co-evolve. **And as with computer viruses in the early 2000s, we think it’s important for everyone to understand responsible usage**, including thinking about prompt injection attacks, so we can all learn to benefit from this technology safely.

Strong agree on this comparison between prompt injection and malware. In fact I've been using this analogy for almost two years now, see my BlackHat USA 2024 talks. But the implications are also clear: giant lists of bad prompts will fail, exactly like AVs did. Even if LLMs hide those lists behind obscure model weights.

