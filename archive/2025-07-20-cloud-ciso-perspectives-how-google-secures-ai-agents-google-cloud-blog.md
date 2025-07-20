---
title: "Cloud CISO Perspectives: How Google secures AI Agents | Google Cloud Blog"
tags:
   - Agent Security
   - Cybersecurity
   - AI Security
   - Cloud Security
   - Identity and Access Management
link: https://cloud.google.com/blog/products/identity-security/cloud-ciso-perspectives-how-google-secures-ai-agents
date: 2025-07-20
description: "In \"How Google Secures AI Agents,\" Anton Chuvakin from Google Cloud outlines a hybrid security paradigm to address the unique challenges of AI agents. Key strategies include enforcing well-defined human controller roles, limiting agent powers for adherence to least-privilege principles, and ensuring observability of agent actions through rigorous logging. Google's multi-layered approach blends traditional deterministic controls with dynamic reasoning-based defenses, such as adversarial training to minimize risks from rogue actions and data disclosures. This framework emphasizes continuous assurance to adapt to evolving threats while maintaining agent utility. Comprehensive insights can be found in Google’s detailed guidelines on securing AI agents."
---

Security & Identity

# Cloud CISO Perspectives: How Google secures AI Agents

June 12, 2025

![https://storage.googleapis.com/gweb-cloudblog-publish/images/Cloud_CISO_Perspectives_header_4_Blue.max-2500x2500.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/Cloud_CISO_Perspectives_header_4_Blue.max-2500x2500.png)

##### Anton Chuvakin

Security Advisor, Office of the CISO

##### Get original CISO insights in your inbox

The latest on security from Google Cloud's Office of the CISO, twice a month.

[Subscribe](https://go.chronicle.security/cloudciso-newsletter-signup?utm_source=cgc-blog&utm_medium=blog&utm_campaign=FY23-Cloud-CISO-Perspectives-newsletter-blog-rail-CTA&utm_content=-&utm_term=-)

Welcome to the first Cloud CISO Perspectives for June 2025. Today, Anton Chuvakin, security advisor for Google Cloud’s Office of the CISO, discusses a new Google report on securing AI agents, and the new security paradigm they demand.

As with all Cloud CISO Perspectives, the contents of this newsletter are posted to the [Google Cloud blog](https://cloud.google.com/blog/products/identity-security/). If you’re reading this on the website and you’d like to receive the email version, you can [subscribe here](https://cloud.google.com/resources/google-cloud-ciso-newsletter-signup).

### How Google secures AI Agents

_By Anton Chuvakin, security advisor, Office of the CISO_

![https://storage.googleapis.com/gweb-cloudblog-publish/images/Anton_Chuvakin_Headshot_18L8044_SQ1_Hi_Res.max-2200x2200.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Anton_Chuvakin_Headshot_18L8044_SQ1_Hi_Res.max-2200x2200.jpg)![https://storage.googleapis.com/gweb-cloudblog-publish/images/Anton_Chuvakin_Headshot_18L8044_SQ1_Hi_Res.max-2200x2200.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Anton_Chuvakin_Headshot_18L8044_SQ1_Hi_Res.max-2200x2200.jpg)

The emergence of AI agents promises to reshape our interactions with information systems — and ultimately with the real world, too. These systems, distinct from the foundation models they’re built on, possess the unique ability to act on information they’ve been given to achieve user-defined goals. However, this newfound capability introduces a critical challenge: agent security.

Agents strive to be more autonomous. They can take information and use it in conjunction with tools to devise and execute complex plans, so it’s critical that developers align agent behavior with user intent to prevent unintended and harmful actions.

With this great power comes a great responsibility for agent developers. To help mitigate the potential risks posed by rogue agent actions, we should invest in a new field of study focused specifically on securing agent systems.

While there are similarities to [securing AI](https://cloud.google.com/blog/products/identity-security/cloud-ciso-perspectives-5-tips-secure-ai-success), securing AI agents is distinct and evolving, and demands a new security paradigm.

#### Google advocates for a hybrid defense-in-depth approach that combines the strengths of both traditional (deterministic) and reasoning-based (dynamic) security measures. This creates layered defenses that can help prevent catastrophic outcomes while preserving agent usefulness.

[Tweet this quote](https://x.com/intent/tweet?text=Google%20advocates%20for%20a%20hybrid%20defense-in-depth%20approach%20that%20combines%20the%20strengths%20of%20both%20traditional%20%28deterministic%29%20and%20reasoning-based%20%28dynamic%29%20security%20measures.%20This%20creates%20layered%20defenses%20that%20can%20help%20prevent%20catastrophic%20outcomes%20while%20preserving%20agent%20usefulness.%20-%20https%3A%2F%2Fcloud.google.com%2Fblog%2Fproducts%2Fidentity-security%2Fcloud-ciso-perspectives-how-google-secures-ai-agents)

To help detail what we believe are the core issues, we’ve published a comprehensive guide covering [our approach to securing AI agents](https://research.google/pubs/an-introduction-to-googles-approach-for-secure-ai-agents/) that addresses concerns for both AI agent developers and security practitioners. Our goal is to provide a clear and actionable foundation for building secure and trustworthy AI agent systems that benefit society.

We cover the security challenges of agent architecture, the specific risks of rogue actions and sensitive data disclosure, and detail the three fundamental agent security principles: well-defined human controllers, limited agent powers, and observable agent actions.

1. **Agents must have well-defined human controllers**: Agents must operate under clear human oversight, with the ability to distinguish authorized user instructions from other inputs.
2. **Agent powers must have limitations**: Agent actions and resource access must be carefully limited and dynamically aligned with their intended purpose and user risk tolerance. This emphasizes the least-privilege principle.
3. **Agent actions and planning must be observable**: Agent activities must be transparent and auditable through robust logging and clear action characterization.

**Google's hybrid approach: Agentic defense-in-depth**

Google advocates for a hybrid defense-in-depth approach that combines the strengths of both traditional (deterministic) and reasoning-based (dynamic) security measures. This creates layered defenses that can help prevent catastrophic outcomes while preserving agent usefulness.

We believe that the most effective and efficient defense-in-depth path forward secures agents with both classic and AI controls. Our approach advocates for two distinct layers:

- **Layer 1: Use traditional, deterministic measures**, such as runtime policy enforcement. Runtime policy engines act as external guardrails, monitoring and controlling agent actions _before_ execution based on predefined rules. These engines use action manifests to capture the security properties of agent actions, such as dependency types, effects, authentication, and data types.
- **Layer 2: Deploy reasoning-based defense strategies**. This layer uses the AI model's own reasoning to enhance security. Techniques such as adversarial training and using specialized models as security analysts can help the agent distinguish legitimate commands from malicious ones, making it more resilient against attacks, data theft, and even model theft.

Of course, each of the above two layers should have their own layers of defense. For example, model-based input filtering coupled with adversarial training and other techniques can help reduce the risk of prompt injection, but not completely eliminate it. Similarly, these defense measures would make data theft more difficult, but would also need to be enhanced by traditional controls such as rule-based and algorithmic threat detection.

**Key risks, limitations, and challenges**

Traditional security paradigms, designed for [static software or general AI](https://www.googlecloudcommunity.com/gc/Community-Blog/Securing-AI-Supply-Chain-Like-Software-Only-Not/ba-p/867409), are insufficient for AI agents. They often lack the contextual awareness needed to know what the agent is reasoning about and can overly restrict an agent's utility.

Similarly, relying solely on a model’s judgment for security is also inadequate because of the risk posed by vulnerabilities such as [prompt injection](https://cloud.google.com/transform/5-gen-ai-security-terms-busy-business-leaders-should-know?e=48754805), which can compromise the integrity and functionality of an agent over time.

In the [wide universe of risks to AI](https://saif.google/secure-ai-framework/risks), two risks associated with AI agents stand out from the crowd by being both more likely to manifest and more damaging if ignored.

**Rogue actions** are unintended, harmful, and policy-violating behaviors an agent might exhibit. They can stem from several factors, including the stochastic nature of underlying models, the emergence of unexpected behaviors, and challenges in aligning agent actions with user intent. Prompt injections are a significant vector for inducing rogue actions.

For example, imagine an agent designed to automate tasks in a cloud environment. A user intends to use the agent to deploy a virtual machine. However, due to a prompt injection attack, the agent instead attempts to delete all databases. A runtime policy engine, acting as a guardrail, would detect the "delete all databases" action (from its action manifest) and block it because it violates predefined rules.

**Sensitive data disclosure** involves the unauthorized revelation of private or confidential information by agents. Security measures would help ensure that access to sensitive data is strictly controlled.

For example, an agent in the cloud might have access to customer data to generate reports. If not secured, the agent might retain this sensitive data and then be coaxed to expose it. A malicious user could then ask a follow-up question that triggers the agent to inadvertently disclose some of that retained data.

However, securing AI agents is inherently challenging due to four factors:

- Unpredictability (non-deterministic nature)
- Emergent behaviors
- Autonomy in decision-making
- Alignment issues (ensuring actions match user intent)

**Practical security considerations**

Our recommended hybrid approach addresses several critical areas.

- **Agent/plugin user controls**: Emphasizes human confirmation for critical and irreversible actions, clear distinction between user input and other data, and verifiable sharing of agent configurations.
- **Agent permissions**: Adherence to the least-privilege principle, confining agent actions to its domain, limiting permissions, and allowing for user authority revocation. This level of granular control often surprises security leaders because such a traditional 1980s-style security control delivers high value for securing 2020s AI agents.
- **Orchestration and tool calls:** The intricate relationship between AI agents and external tools and services they use for orchestration can present unique security risks, especially with "Actions as Code." Robust authentication, authorization, and semantic tool definitions are crucial risk mitigations here.
- **Agent memory**: Data stored in an agent's memory can lead to persistent prompt injections and information leakage.
- **Response rendering:** Safely rendering AI agent outputs into user-readable content is vital to prevent classic web vulnerabilities.

**Assurance and future directions**

Continuous assurance efforts are essential to validate agent security. This includes regression testing, variant analysis, [red teaming](https://cloud.google.com/transform/how-google-does-it-red-teaming-at-scale), user feedback, and external research programs to ensure security measures remain effective against evolving threats.

Securing AI agents requires a multi-faceted, hybrid approach that carefully balances the utility of these systems with the imperative to mitigate their inherent risks. Google Cloud offers controls in Agentspace that follow these guidelines, such as authentication and authorization, model safeguards, posture assessment, and of course logging and detection.

To learn more about how Google is approaching securing AI agents, please read [our research paper](https://research.google/pubs/an-introduction-to-googles-approach-for-secure-ai-agents/).

### **In case you missed it**

Here are the latest updates, products, services, and resources from our security teams so far this month:

- **Project Shield blocked a massive recent DDoS attack. Here’s how**: Project Shield, Google’s free service that protects at-risk sites against DDoS attacks, kept KrebsOnSecurity up during a recent, massive one. Here’s what happened. [**Read more**](https://cloud.google.com/blog/products/identity-security/project-shield-blocked-a-massive-recent-ddos-attack-heres-how).
- **Don’t test in prod. Use digital twins for safer, smarter resilience**: Digital twins are replicas of physical systems using real-time data to create a safe test environment. Here’s how they can help business and security leaders. [**Read more**](https://cloud.google.com/transform/dont-test-in-prod-use-digital-twins-safer-smarter-resilience).
- **How to build a digital twin with Google Cloud**: Digital twins are essentially IT stunt doubles, cloud-based replicas of physical systems for testing. Learn how to build them on Google Cloud. [**Read more**](https://cloud.google.com/blog/products/identity-security/how-to-build-a-digital-twin-to-boost-resilience).
- **Enhancing protection: 4 new Security Command Center capabilities**: Security Command Center has a unique vantage point to protect Google Cloud environments. Here are four new SCC capabilities. [**Read more**](https://cloud.google.com/blog/products/identity-security/enhancing-protection-4-new-security-command-center-capabilities).

Please visit the Google Cloud blog for more security stories [published this month](https://cloud.google.com/blog/products/identity-security).

### **Threat Intelligence news**

- **The cost of a call, from voice phishing to data extortion**: Google Threat Intelligence Group (GTIG) is tracking threat actors who specialize in voice phishing (vishing) campaigns designed to compromise Salesforce instances for large-scale data theft and subsequent extortion. Here’s several defensive measures you can take. [**Read more**](https://cloud.google.com/blog/topics/threat-intelligence/voice-phishing-data-extortion?e=48754805) **.**
- **A technical analysis of vishing threats:** Financially motivated threat actors have increasingly adopted voice-based social engineering, or "vishing," as a primary vector for initial access, though their specific methods and end goals can vary significantly. Here’s how they do it — and what you can do to stop them. [**Read more**](https://cloud.google.com/blog/topics/threat-intelligence/coldriver-steal-documents-western-targets-ngos?e=48754805) **.**

Please visit the Google Cloud blog for more threat intelligence stories [published this month](https://cloud.google.com/blog/topics/threat-intelligence/).

### **Now hear this: Podcasts from Google Cloud**

- **Debunking cloud breach myths (and what DBIR says now)**: Everything (and we mean _everything_) you wanted to know about cloud breaches, but were (legitimately, of course) afraid to ask. Verizon Data Breach Report lead Alex Pinto joins hosts Anton Chuvakin and Tim Peacock for a lively chat on breaching clouds. [**Listen here**](https://cloud.withgoogle.com/cloudsecurity/podcast/ep229-beyond-the-hype-debunking-cloud-breach-myths-and-what-dbir-says-now/).
- **Is SIEM in 2025 still too hard**: Alan Braithwaite, co-founder and CTO, RunReveal, discusses the future of SIEM and security telemetry data with Anton and Tim. [**Listen here**](https://cloud.withgoogle.com/cloudsecurity/podcast/ep228-siem-in-2025-still-hard-reimagining-detection-at-cloud-scale-and-with-more-pipelines/).
- **Cyber-Savvy Boardroom: Jamie Collier on today’s threat landscape**: Jamie Collier, lead Europe advisor, GTIG, joins Office of the CISO’s David Homovich and Anton Chuvakin to talk about what boards need to know about today’s threat actors. [**Listen here**](https://cybersavvyboardroom.libsyn.com/ep4-jamie-collier-on-the-current-threat-landscape).
- **Defender’s Advantage: Confronting a North Korean IT worker incident**: Mandiant Consulting's Nick Guttilla and Emily Astranova join Luke McNamara for an episode on the AI-driven use of voice-based phishing, or "vishing," and how they use it during red team engagements. [**Listen here**](https://www.youtube.com/watch?v=t_roGtOtlDE&list=PLjiTz6DAEpuINUjE8zp5bAFAKtyGJvnew&index=1).
- **Behind the Binary: Protecting software intellectual property**: Tim Blazytko, chief scientist and head of engineering, Emproof, talks with host Josh Stroschein about the essential strategies for protecting software intellectual property. [**Listen here**](https://www.youtube.com/watch?v=ZrME6aUqybY&list=PLjiTz6DAEpuLAykjYGpAUDL-tCrmTpXTf&index=1).

To have our Cloud CISO Perspectives post delivered twice a month to your inbox, [sign up for our newsletter](https://cloud.google.com/resources/google-cloud-ciso-newsletter-signup). We’ll be back in a few weeks with more security-related updates from Google Cloud.

Posted in

- [Security & Identity](https://cloud.google.com/blog/products/identity-security)
- [Cloud CISO](https://cloud.google.com/blog/topics/cloud-ciso)
- [AI & Machine Learning](https://cloud.google.com/blog/products/ai-machine-learning)

##### Related articles

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/17_-_Security__Identity_NrORvDT.max-700x700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/17_-_Security__Identity_NrORvDT.max-700x700.jpg)\\
\\
Security & Identity\\
\\
**How to enable Secure Boot for your AI workloads** \\
\\
By Maciej Strzelczyk • 5-minute read](https://cloud.google.com/blog/products/identity-security/how-to-enable-secure-boot-for-your-ai-workloads)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/Cloud_CISO_Perspectives_header_4_Blue.max-700x700.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/Cloud_CISO_Perspectives_header_4_Blue.max-700x700.png)\\
\\
Security & Identity\\
\\
**Cloud CISO Perspectives: Our Big Sleep agent makes a big leap, and other AI news** \\
\\
By Sandra Joyce • 6-minute read](https://cloud.google.com/blog/products/identity-security/cloud-ciso-perspectives-our-big-sleep-agent-makes-big-leap)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/49_-_Customers_YsP9mBg.max-700x700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/49_-_Customers_YsP9mBg.max-700x700.jpg)\\
\\
Customers\\
\\
**Engineering Deutsche Telekom's sovereign data platform** \\
\\
By Ashutosh Mishra • 5-minute read](https://cloud.google.com/blog/topics/customers/engineering-deutsche-telekoms-sovereign-data-platform)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/image1_LxY1x34.max-700x700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/image1_LxY1x34.max-700x700.jpg)\\
\\
Inside Google Cloud\\
\\
**London Summit: agentic AI leaders, training 100,000 civil servants, AI sovereignty, and more** \\
\\
By Maureen Costello • 5-minute read](https://cloud.google.com/blog/topics/inside-google-cloud/london-summit-2025-gen-ai-agents-transforming-business-civil-service)
