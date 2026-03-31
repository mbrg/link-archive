---
date: '2025-12-26'
description: The integration of AI agents in cybersecurity presents both opportunities
  and threats, as noted in a Microsoft blog by Charlie Bell. With a projected 1.3
  billion AI agents by 2028, organizations must adapt to a new threat landscape characterized
  by autonomous, dynamic attackers. Key strategies include adopting "Agentic Zero
  Trust" principles through containment and alignment, ensuring least privilege access
  and monitoring agent activities. Additionally, fostering a culture of secure innovation
  is crucial for effective risk management. Organizations are urged to establish clear
  governance frameworks to enhance accountability and traceability of AI agents, thereby
  mitigating potential security risks.
link: https://blogs.microsoft.com/blog/2025/11/05/beware-of-double-agents-how-ai-can-fortify-or-fracture-your-cybersecurity/
tags:
- AI Governance
- Zero Trust
- AI Security
- Cybersecurity
- Microsoft Entra
title: 'Beware of double agents: How AI can fortify — or fracture — your cybersecurity
  - The Official Microsoft Blog'
---

[Skip to content](https://blogs.microsoft.com/blog/2025/11/05/beware-of-double-agents-how-ai-can-fortify-or-fracture-your-cybersecurity/#content)

Skip to main content

![Eight people gathered around a long table in a conference room with two large screens on two walls and digital clocks above one of the screens on the wall. The meeting is visible through a wall of glass.](https://blogs.microsoft.com/wp-content/uploads/2025/11/OMB-Security-11-5-Hero_Final.jpg)

AI is rapidly becoming the backbone of our world, promising unprecedented productivity and innovation. But as organizations deploy AI agents to unlock new opportunities and drive growth, they also face a new breed of cybersecurity threats.

There are a lot of _Star Trek_ fans here at Microsoft, including me. One of our engineering leaders gifted me a life-size cardboard standee of [Data](https://www.startrek.com/news/top-10-data-moments) that lurks next to my office door. So, as I look at that cutout, I think about the Great AI Security Dilemma: Is AI going to be our best friend or our worst nightmare? Drawing inspiration from the duality of the android officer [Data](https://www.startrek.com/news/top-10-data-moments), and his evil twin [Lore](https://www.startrek.com/news/remembering-datalore-26-years-later) in the _Star Trek_ universe, today’s AI agents can either fortify your cybersecurity defenses — or, if mismanaged — fracture them.

The influx of agents is real. IDC research [\[1\]](https://blogs.microsoft.com/blog/2025/11/05/beware-of-double-agents-how-ai-can-fortify-or-fracture-your-cybersecurity/#_ftn1) predicts there will be 1.3 billion agents in circulation by 2028. When we think about our agentic future in AI, the duality of Data and Lore seems like a great way to think about what we’ll face with AI agents and how to avoid double agents that upend control and trust. Leaders should consider three principles and tailor them to fit the specific needs of their organizations.

### **1\. Recognize the new attack landscape**

Security is not just an IT issue — it’s a board-level priority. Unlike traditional software, AI agents are even more dynamic, adaptive and likely to operate autonomously. This creates unique risks.

We must accept that AI can be abused in ways beyond what we’ve experienced with traditional software. We employ AI agents to perform well-meaning tasks, but those with broad privileges can be manipulated by bad actors to misuse their access, such as leaking sensitive data via automated actions. We call this the “Confused Deputy” problem. AI Agents “think” in terms of natural language where instructions and data are tightly intertwined, much more than in typical software we interact with. The generative models agents depend on dynamically analyze the entire soup of human (or even non-human) languages, making it hard to distinguish well-known safe operations from new instructions introduced through malicious manipulation. The risk grows even more when shadow agents — unapproved or orphaned — enter the picture. And as we saw in Bring Your Own Device (BYOD) and other tech waves, anything you cannot inventory and account for magnifies blind spots and drives risk ever upward.

### **2\. Practice Agentic Zero Trust**

AI agents may be new as productivity drivers, but they can still be managed effectively using established security principles. I’ve had great conversations about this here at Microsoft with leaders like Mustafa Suleyman, cofounder of DeepMind and now Executive Vice President and CEO of Microsoft AI. Mustafa frequently shares a way to think about this, which he outlined in his book _The Coming Wave,_ in terms of Containment and Alignment.

Containment simply means we do not blindly trust our AI Agents, and we significantly box every aspect of what they do. For example, we cannot let any agent’s access privileges exceed its role and purpose — it’s the same security approach we take to employee accounts, software and devices, what we refer to as “least privilege.” Similarly, we contain by never implicitly trusting what an agent does or how it communicates — everything must be monitored — and when this isn’t possible, agents simply are not permitted to operate in our environment.

Alignment is all about infusing positive control of an AI agent’s intended purpose, through its prompts and the models it uses. We must only use AI agents trained to resist attempts at corruption, with standard and _mission-specific_ safety protections built into both the model itself and the prompts used to invoke the model. AI agents must resist attempts to divert them from their approved uses. They must execute in a Containment environment that watches closely for deviation from their intended purpose. All this requires strong AI agent identity and clear accountable ownership within the organization. As part of AI governance, every agent must have an identity, and we must know who in the organization is accountable for its _aligned_ behavior.

Containment (least privilege) and Alignment will sound familiar to enterprise security teams, because they align with some of the basic principles of [Zero Trust](https://learn.microsoft.com/en-us/security/zero-trust/zero-trust-overview). Agentic Zero Trust includes “assuming breach,” or never implicitly trusting anything, making humans, devices and agents verify who they are explicitly before they gain access and limiting their access to only what’s needed to perform a task. While Agentic Zero Trust ultimately includes deeper security capabilities, discussing Containment and Alignment is a good shorthand in security-in-AI strategy conversations with senior stakeholders to keep everyone grounded in managing the new risk. Agents will keep joining and adapting at work — some may become double agents. With proper controls, we can protect ourselves.

### **3\. Foster a culture of secure innovation**

Technology alone won’t solve AI security. Culture is the real superpower in managing cyber risk — and leaders have the unique ability to shape it. Start with open dialogue: make AI risks and responsible use part of everyday conversations. Keep it cross-functional: legal, compliance, HR and others should have a seat at the table. Invest in continuous education: train teams on AI security fundamentals and clarify policies to cut through noise. Finally, embrace safe experimentation: give people approved spaces to learn and innovate without creating risk.

Organizations that thrive will treat AI as a teammate, not a threat — building trust through communication, learning and continuous improvement.

### **The path forward: What every company should do**

AI isn’t just another chapter — it’s a plot twist that changes everything. The opportunities are huge, but so are the risks. The rise of AI requires ambient security, which executives create by making cybersecurity a daily priority. This means blending robust technical measures with ongoing education and clear leadership so that security awareness influences every choice made. Organizations maintain ambient security when they:

- Make AI security a strategic priority.
- Insist on Containment and Alignment for every agent.
- Mandate identity, ownership and data governance.
- Build a culture that champions secure innovation.

**And it will be important to take a set of practical steps:**

- Assign every AI agent an ID and owner — just like employees need badges. This ensures traceability and control.
- Document each agent’s intent and scope.
- Monitor actions, inputs and outputs. Map data flows early to set compliance benchmarks.
- Keep agents in secure, sanctioned environments — no rogue “agent factories.”

**The call to action for every business is:** Review your AI governance framework now. Demand clarity, accountability and continuous improvement. The future of cybersecurity is human plus machine — lead with purpose and make AI your strongest ally.

At Microsoft, we know we have a huge role to play in empowering our customers in this new era. In May, we introduced [Microsoft Entra Agent ID](https://www.microsoft.com/en-us/security/blog/2025/05/19/microsoft-extends-zero-trust-to-secure-the-agentic-workforce/) as a way to help customers place unique identities to agents from the moment they are created in Microsoft Copilot Studio and Azure AI Foundry. We leverage AI in Defender and Security Copilot, combined with the massive security signals we collect, to [expose and defeat phishing campaigns](https://www.microsoft.com/en-us/security/blog/2025/09/24/ai-vs-ai-detecting-an-ai-obfuscated-phishing-campaign/) and other attacks that cybercriminals may use as entry points to compromise AI agents. We’ve also been committed to a platform approach with AI agents, to help customers safely use both Microsoft and third-party agents on their journey, avoiding complexity and risk that come from needing to juggle excessive dashboards and management consoles.

I’m excited by several other innovations we will be sharing at [Microsoft Ignite](https://ignite.microsoft.com/en-US/home) later this month, alongside customers and partners.

We may not be conversing with Data on the bridge of the [USS Enterprise](https://www.startrek.com/news/enterprise-starfleets-finest-flagships) quite yet, but as a technologist, it’s never been more exciting than watching this stage of AI’s trajectory in our workplaces and lives. As leaders, understanding the core opportunities and risks helps create a safer world for humans and agents working together.

_Charlie Bell is executive vice president of Microsoft Security, leading teams advancing cybersecurity, compliance, identity and management. With more than 40 years in technology, he’s held leadership roles at Oracle, founded Server Technologies Group and unified engineering at AWS before joining Microsoft, driving innovation and protection for global digital systems._

**NOTE**

[\[1\]](https://blogs.microsoft.com/blog/2025/11/05/beware-of-double-agents-how-ai-can-fortify-or-fracture-your-cybersecurity/#_ftnref1) IDC Info Snapshot, sponsored by Microsoft, 1.3 Billion AI Agents by 2028, May 2025 #US53361825

Tags: [AI](https://blogs.microsoft.com/blog/tag/ai/), [Azure AI Foundry](https://blogs.microsoft.com/blog/tag/azure-ai-foundry/), [Entra Agent ID](https://blogs.microsoft.com/blog/tag/entra-agent-id/), [Microsoft Copilot Studio](https://blogs.microsoft.com/blog/tag/microsoft-copilot-studio/), [Microsoft Defender](https://blogs.microsoft.com/blog/tag/microsoft-defender/), [Security Copilot](https://blogs.microsoft.com/blog/tag/security-copilot/)

Follow us:

- [Check us out on RSS](https://blogs.microsoft.com/?feed=rss2 "RSS Subscription")
