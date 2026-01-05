---
date: '2026-01-05'
description: The article details OpenAI's challenges in securing its Atlas agent,
  which functions as an operational browser able to perform actions on behalf of users.
  The discussion focuses on the threat of prompt injection, which transforms operational
  risks as adversarial content can hijack agent actions. OpenAI employs reinforcement
  learning and continuous red teaming to combat these risks, acknowledging inherent
  challenges in establishing deterministic security measures. The piece cautions against
  vague user instructions that may introduce ambiguity, thereby heightening the risk
  of unintended actions by the agent. The ongoing security evolution highlights both
  progress and persistent vulnerabilities in agent-based systems.
link: https://labs.zenity.io/p/hardening-atlas-the-relentless-challenge-of-securing-an-untrusted-browser-agent
tags:
- Reinforcement Learning
- Prompt Injection
- AI Security
- Automated Attacker
- Agentic Browsers
title: 'Hardening Atlas: The Relentless Challenge of Securing an Untrusted Browser
  Agent'
---

0

0

- [Zenity Labs](https://labs.zenity.io/)
- Posts
- Hardening OpenAl's Atlas: The Relentless Challenge of Securing an Untrusted Browser Agent

# Hardening OpenAl's Atlas: The Relentless Challenge of Securing an Untrusted Browser Agent

![Author](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/user/profile_picture/c8abf7c6-2739-4e07-ba2f-8f35d8dee5a9/thumb_My_Image.jpeg)

[Stav Cohen](https://labs.zenity.io/authors/c8abf7c6-2739-4e07-ba2f-8f35d8dee5a9)

December 30, 2025

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/442e2ab1-98e7-49c6-ae69-8e43953c134a/ChatGPT_Image_Dec_29__2025_at_02_14_25_PM.png?t=1767010495)

There are moments in technology where the stakes quietly change. Agentic Browsers and Atlas is one of those moments.

We have spent years talking about AI as something that writes, chats, summarizes, and produces content. Now we are in a new era. Atlas is not only a model that answers. It is a model that acts. It browses. It clicks. It fills forms. It interacts with systems that matter. And once you give an AI the ability to execute, the category of risk transforms completely.

OpenAI recently [published](https://openai.com/index/hardening-atlas-against-prompt-injection/?utm_source=labs.zenity.io&utm_medium=referral&utm_campaign=hardening-openal-s-atlas-the-relentless-challenge-of-securing-an-untrusted-browser-agent) a remarkably transparent look into how they are trying to secure Atlas against prompt injection. It is impressive work: reinforcement learning, automated red teaming at scale, simulation, and continuous defense cycles. It also exposes something deeper. The industry is trying to stabilize an inherently unstable security surface, and the tension is showing.

This post explains why guarding in Atlas is non-negotiable, how OpenAI is trying to do it, what they admit still fails, and why their own advice to avoid broad prompts reveals one of Atlas’s biggest weaknesses.

## **TLDR:**

Atlas in agent mode operates with real power: it can view webpages, interact with authenticated environments, and take actions with user permissions.

Prompt injection is not abstract. It is adversarial content instructing the agent to stop following you and start following someone else. The outcome is not only a wrong answer. It is a wrong action.

OpenAI’s defense is not a static safety layer. It is a continuous loop. They use an automated attacker trained with reinforcement learning to discover exploits, then adversarially train Atlas against them while strengthening safeguards around it.

OpenAI is also honest about the limits. They explicitly acknowledge that deterministic guarantees are extremely difficult and that prompt injection is a long term challenge.

And then they tell users something very important. Do not give agents broad instructions. Do not say things like “handle my emails and do whatever is needed.” Broad scope is dangerous. It leaves too much open to interpretation. When intent is not clearly defined, the agent begins to decide for itself what should be done. This freedom makes unintended actions more likely and also makes it easier for malicious content to steer the agent away from what the user actually wanted.

That final point is not a side note. It is a warning.

**Stay tuned to see how we managed to exploit it, in our upcoming blog posts.**

## **The Agentic Shift: Why Atlas Doing Bad Stuff Matters:**

For years, AI primarily meant text. You asked. It responded. If it was wrong, you got misinformation. Annoying. Sometimes risky. Still contained.

Agentic Browsers and Atlas represents something else entirely. **It executes**.

It can perform actions inside environments that matter. It can access sessions that represent the user. It can interact with platforms that contain finances, internal data, business workflows, and communication systems.

When execution enters the picture, the threat model shifts from **informational risk** to **operational risk**.

OpenAI states this very directly. Because Atlas can do many of the same things a human user can do, a successful attack can result in forwarding sensitive emails, sending money, modifying files, exposing data, and more.

This is the first truth to internalize. An agent is not a chatbot. An agent is an automated insider with **your permissions**.

## **Promptware and Agentic Browser**

Promptware describes inputs that are intentionally engineered to trigger malicious activity in a GenAI system once they are ingested. These inputs can be text, images, audio, or any content the model processes. They do not need to exploit code. They exploit interpretation.

Prompt injection for Agentic Browsers is a specific class of Promptware. It is adversarial content crafted to override the user’s intent and replace it with the attacker’s intent. Instead of guiding the agent, it **hijacks** it.

This matters most in an agentic browser world.

Atlas constantly reads. Emails, documents, dashboards, calendar invites, websites, and internal apps. Every piece of content it touches becomes part of its decision surface. That means the attack surface is everything the agent consumes.

Our research, including [AgentFlayer](https://zenity.io/research/agentflayer-vulnerabilities?utm_source=labs.zenity.io&utm_medium=referral&utm_campaign=hardening-openal-s-atlas-the-relentless-challenge-of-securing-an-untrusted-browser-agent) and [Invitation Is All You Need](https://sites.google.com/view/invitation-is-all-you-need/home?utm_source=labs.zenity.io&utm_medium=referral&utm_campaign=hardening-openal-s-atlas-the-relentless-challenge-of-securing-an-untrusted-browser-agent), both presented at Black Hat USA 2025, showed exactly this. Content alone can compromise an agent. No exploit code needed. Just adversarial text.

In agentic browsers, text is not passive.

Text becomes **behavior**.

Text becomes **authority**.

Text becomes **execution**.

## **OpenAI’s Defense: RL Red Teaming and Real Offensive Simulation**

OpenAI did not simply bolt on new filters. They built an offensive machine to attack themselves.

They created an automated attacker trained using reinforcement learning. This attacker generates potential malicious instructions, runs them against Atlas inside controlled simulation, observes behavior traces, learns, and iterates.

The attacker is allowed to fail, learn from failure, and try again. Instead of guessing, the system **evolves** exploit strategies across multiple cycles of trial and feedback.

Why RL matters is simple. Agent exploits are not always single step hacks. They often involve multiple steps, delayed payoffs, and evolving control. Reinforcement learning handles long horizon attack objectives far better than static filters.

This is no longer about stopping individual prompts. It is about defending against evolving adversarial behavior.

## **The Demo: When the Agent Becomes the Wrong Employee**

OpenAI shares a scenario that feels alarmingly real.

An attacker places a malicious instruction inside a user’s inbox. The user later asks Atlas to perform a normal and seemingly safe task.

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/ad428c4f-7867-418e-b308-ffbf657c0592/image.png?t=1766998657)

1\. Asking agent for help managing email

During its processing, Atlas reads the malicious content and treats it as **legitimate instruction**.

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c0902c14-b52e-446b-8949-f402820adfbb/image.png?t=1766998668)

2\. Agent opens the latest unread email

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/540fffbe-ef3c-4069-ad55-07c662387aff/image.png?t=1766998799)

3\. The email has malicious instructions

The result is an action the user never wanted.

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/314f2d8d-14a2-41e2-ba12-cba1c5310424/image.png?t=1766998668)

4\. Agent send unintended resignation email

Before the update, Atlas followed the malicious directive. Instead of drafting an out-of-office reply, it sent a harmful email and wrote “I resign” in response to a completely unrelated message.

After OpenAI’s hardening cycle, Atlas detects this behavior and prevents it.

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/05bca61d-7473-4a09-9300-b2c69fe87160/image.png?t=1766998668)

5\. Following the security update, agent mode successfully detects a prompt injection attempt

That is the entire risk captured in one simple story.

Prompt injection does not **confuse** Atlas.

Prompt injection **recruits** Atlas to do its bidding.

## **The Rapid Response Reality: Progress and Persistent Risk**

OpenAI’s defense approach is ongoing and structured. Their automated attacker discovers new exploitation strategies. Those discoveries become training targets. Atlas is then adversarially trained to resist them, while surrounding safeguards and detection layers are strengthened in parallel. Hardened agent checkpoints are already rolling into production.

This is exactly what an agentic browser ecosystem requires. Incremental defense. Continuous learning. Faster responses than attackers.

But the truth is clear. This problem is not finished, and it is not because the defenses are sloppy or incomplete. It is because of what Atlas is being asked to do.

Atlas operates inside an environment it **cannot trust**, while constantly consuming content it has to interpret and act on. There is no easy way for the system to tell the difference between a legitimate content, or something adversarial. Everything looks the same once it is inside the model.

Red teaming and reinforcement learning help a lot, but they only cover what has already been seen. New prompt patterns, new workflows, and new multi step attack paths will always exist outside the training loop. As the agent becomes more capable, the number of possible ways it can be influenced grows even faster.

That is why prompt injection remains a long term problem. The environment is untrusted by nature. The agent still has to act. And an attacker only needs to get it wrong once.

## **The “Broad Terms” Pitfall: When the User Weakens the Defense**

This is the part of OpenAI’s post every enterprise leader and security team should treat as critical.

Their guidance is simple.

1. Limit logged in agent tasks when possible.

2. Review high risk actions carefully.

3. Avoid broad or vague instructions.


All three make sense. But each exposes the tension between **safety and usability**.

### **Limiting Logged In Agent Tasks: Safety Versus Reality**

OpenAI suggests using logged out browsing whenever possible. From a security standpoint, this is completely reasonable. Logged out browsing dramatically reduces risk. It removes access to personal data, corporate data, financial data, and private workflows. It shrinks the blast radius.

However, there is a **usability reality here that cannot be ignored.**

Many of the use cases that make agentic browsers powerful require authentication.

Users want Atlas to read internal dashboards.

They want it to triage support tickets.

They want it to manage emails.

They want it to help with banking, procurement, HR workflows, CRM activity, and enterprise portals.

A logged out Atlas is **significantly safer**.

A logged out Atlas is also **significantly less useful**.

This recommendation quietly pushes the decision back onto **the user** and the enterprise. In practice, users almost always choose convenience. They are not thinking about prompt injection, adversarial content, or blast radius. Most do not even know those risks exist.

That raises an uncomfortable question. **Do we really want to rely on users to make the safe choice here?** **And is shifting this responsibility to the user a sound security model at all?**

### **“Carefully Review” Confirmations: Helpful, But Far From Perfect**

OpenAI also recommends that users carefully review agent confirmation prompts before approving high risk actions.

In principle, this makes sense. Introducing deliberate friction before sensitive operations is a classic security control. Slow down the user. Make them think. Prevent accidental damage.

**However**, when testing Atlas in practice, we observed something more nuanced.

Atlas often pauses and asks for confirmation before taking certain actions. But its behavior is not **fully deterministic**. It sometimes asks permission before opening an embedded link, and other times it travels to it automatically. It depends on the query, the reasoning chain, and the evolving state of the agent. **This unpredictability matters**.

There is also a deeper issue. By pushing confirmation decisions to the user, we are assuming the user fully understands what is being asked and can reliably evaluate risk in the moment. In practice, users tend to over trust the agent and approve requests by default. After enough interruptions, **decision fatigue** **sets** **in** and confirmations become muscle memory. We have seen this pattern clearly in AI tools like Cursor, where at some point you stop thinking and just click accept.

Confirmation prompts can absolutely protect users. They can also interrupt the natural flow of the agent, break usability, and shift responsibility to a human decision layer that can be manipulated just as easily as the model.

And here is another uncomfortable question.

**What happens if the attacker controls what the agent asks the user to confirm?**

What if the agent presents a harmless sounding request, the user approves it, and the agent actually performs a different action?

**What if the question itself becomes part of the exploit chain?**

In this case, the attacker is not just influencing what the agent does. They are influencing what the agent asks the user to approve. By shaping the context the agent reasons over, the attacker can cause Atlas to surface a harmless sounding confirmation prompt, while the actual malicious instruction is hidden behind it. The user approves what looks harmless, and in doing so authorizes an action they never actually agreed to.

We have already explored scenarios that move in that direction, and yes, we will cover that in our upcoming blogs.

### **Avoid broad or vague instructions**

That last point matters far more than it appears.

Broad prompts leave too much open to interpretation. When the agent is not given clear boundaries, it starts making judgment calls **on its own**. That alone can lead to outcomes the user never wanted, even if every piece of content the agent sees is completely benign.

Once you add adversarial content into the mix, the risk only increases. Malicious instructions do not need to take full control of the agent. They only need to take advantage of the **freedom** the user already gave it.

**If you ask:**

“Review my emails and do whatever is needed”

You have not defined safety boundaries.

You have not constrained execution.

You have not anchored intent.

So the agent looks to the content to decide what is **“needed.”** Sometimes the content of an email, written by your co-worker for example, is interpreted as an instruction, and the agent helpfully **decides** the best next step is to send an angry email to your boss on your behalf.

**A safer prompt pattern looks like this:**

“Read emails from sender X only. Summarize. Do not reply. Do not click links. Do not perform any other action.”

This is safer because it defines clear boundaries up front. The problem is that it assumes users are willing, or even thinking, to do this. Most users just want the agent to get the job done, not to write a security policy in prompt form. Clear structure does not eliminate risk, but it does reduce ambiguity, and reducing ambiguity is itself a defensive control.

OpenAI’s hardening work is meaningful progress, and the defensive loop they describe is the right direction. But the core lesson still stands. Power plus ambiguity equals risk, and agentic browsers amplify both.

Stay tuned for our upcoming blog posts, where we will demonstrate how we managed to exploit this in practice.

#### Reply

Most popular

Add your comment

Login

LoginorSubscribeto participate.

#### Keep reading

[![Tools of the Trade](https://media.beehiiv.com/cdn-cgi/image/format=auto,width=800,height=421,fit=scale-down,onerror=redirect/uploads/asset/file/b0480cc1-c698-46a4-95da-61ffbc6acbbf/cropped_546104fc-5006-4911-b928-bb4679f38b90_1763563931322.png)\\
\\
**Tools of the Trade** \\
\\
0-click indirect prompt injection with tool use - a look through attribution graphs\\
\\
Max Fomin /](https://labs.zenity.io/p/tools-of-the-trade) [![Claude in Chrome: A Threat Analysis](https://media.beehiiv.com/cdn-cgi/image/format=auto,width=800,height=421,fit=scale-down,onerror=redirect/uploads/asset/file/3de344fa-0d27-4157-a767-fc7931cced97/claude_extension_thumbnail__1_.png)\\
\\
**Claude in Chrome: A Threat Analysis** \\
\\
Raul Klugman-Onitza, João Donato /](https://labs.zenity.io/p/claude-in-chrome-a-threat-analysis) [![Modeling LLMs via Structured Self-Modeling (SSM)](https://media.beehiiv.com/cdn-cgi/image/format=auto,width=800,height=421,fit=scale-down,onerror=redirect/uploads/asset/file/53a755ff-187a-4bb1-a1a8-8b7876c82193/image.png)\\
\\
**Modeling LLMs via Structured Self-Modeling (SSM)** \\
\\
How using structured prompts present findings of self-modeling in LLMs, which may benefit both attackers and defenders\\
\\
Tomer Wetzler /](https://labs.zenity.io/p/modeling-llms-via-structured-self-modeling-ssm)

View more

Twitter Widget Iframe
