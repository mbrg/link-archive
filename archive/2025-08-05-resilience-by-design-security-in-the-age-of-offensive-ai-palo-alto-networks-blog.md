---
date: '2025-08-05'
description: The era of Offensive AI challenges traditional cybersecurity strategies.
  Current defensive measures, reliant on manual processes, are outpaced by AI-driven
  attacks that can exfiltrate data in as little as 25 minutes. Adopting a "Resilience
  by Design" approach emphasizes layered defenses, employing the Swiss cheese model
  to minimize risk. Key strategies include aggressive containment using least-privileged
  IAM roles, real-time visibility through runtime security agents, immediate automated
  responses, and ensuring operational continuity. Organizations must pivot from perfect
  security to enduring capability, prioritizing resilience to withstand sophisticated,
  rapid cyber threats.
link: https://www.paloaltonetworks.com/blog/cloud-security/resilence-by-design/
tags:
- Cloud Security
- Data Protection
- Resilience by Design
- Cybersecurity
- AI Security
title: 'Resilience by Design: Security in the Age of Offensive AI - Palo Alto Networks
  Blog'
---

# Resilience by Design: Security in the Age of Offensive AI

[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.paloaltonetworks.com%2Fblog%2Fcloud-security%2Fresilence-by-design%2F)

[Twitter](https://twitter.com/share?text=Resilience+by+Design%3A+Security+in+the+Age+of+Offensive+AI&url=https%3A%2F%2Fwww.paloaltonetworks.com%2Fblog%2Fcloud-security%2Fresilence-by-design%2F)

[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.paloaltonetworks.com%2Fblog%2Fcloud-security%2Fresilence-by-design%2F&title=Resilience+by+Design%3A+Security+in+the+Age+of+Offensive+AI&summary=&source=)

[Reddit](https://www.reddit.com/submit?url=https://www.paloaltonetworks.com/blog/cloud-security/resilence-by-design/)

[mail](mailto:?subject=Resilience%20by%20Design:%20Security%20in%20the%20Age%20of%20Offensive%20AI)

[CopyLink](https://www.paloaltonetworks.com/blog/cloud-security/resilence-by-design/#)

Link copied


By [Ory Segal](https://www.paloaltonetworks.com/blog/author/ory-segal/ "Posts by Ory Segal")

Aug 01, 2025

6 minutes

25 views

[AI Security](https://www.paloaltonetworks.com/blog/category/ai-security/)

[Cloud Runtime Security](https://www.paloaltonetworks.com/blog/cloud-security/category/cloud-runtime-security/)

[Cloud Security](https://www.paloaltonetworks.com/blog/cloud-security/category/cloud-security/)

Last week I had a moment of clarity while studying the HackerOne leaderboard. An AI agent named XBOW claimed the top spot and now sits at number twelve. I reviewed its attack traces. I saw it chain together a sophisticated padding oracle attack on a custom crypto CAPTCHA. I also watched it dissect a GraphQL API and uncover a critical insecure direct object reference flaw. (It's worth noting that our own Unit 42 team recently published an article detailing [the use of LLMs for detecting broken object level authorization (BOLA) attacks](https://unit42.paloaltonetworks.com/automated-bola-detection-and-ai/)).

Exploits at this level go beyond mere scanner findings. They demonstrate genuine, machine-speed logic targeting complex business processes.

My realization mirrors wider industry anxiety. A recent Palo Alto Networks study found that [61% of organizations fear AI-powered attacks](https://www.paloaltonetworks.com/resources/research/state-of-cloud-native-security-2024) will compromise sensitive data. They’re right to be concerned. With nearly one in five cyberattacks, data exfiltration now happens within the first hour of compromise. Unit 42 testing shows [AI assistance cuts time to exfiltration](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report) from days to just 25 minutes. Meanwhile security teams still require an average of [145 hours to resolve a single alert](https://www.paloaltonetworks.com/prisma/unit42-cloud-threat-research). Our defensive timeline remains hopelessly mismatched with offensive reality.

Defenders once counted on grace periods. Those days have ended.

## Cybersecurity’s Machine-Gun Moment

We’re living in cybersecurity’s machine-gun moment. We run a defensive playbook of methodical, human-driven operations while adversaries unleash automated, overwhelming attacks.

Relying on a "scan-and-patch" cycle is like planning a week-long fortification project in the middle of an ambush.

Our industry has poured immense resources into building an impenetrable fortress. We shifted left, armed developers with static application security testing (SAST) tools and hunted for every flaw. The _secure by design_ philosophy, for all its good intentions, is predicated on achieving a state of near-perfect invulnerability. The pursuit of perfection, of course, becomes a fool’s errand when an adversary can find and exploit an unknown flaw in the time it takes you to read this sentence. The wall will fail. The defining question is what will happen in the five minutes after that.

## The Pivot to Engineering for Resilience

Since we can’t guarantee perfect prevention, we need to shift our strategy from chasing invulnerability to engineering for security synergy. The new mandate is _resilience by design_.

Visualize this approach using the [swiss cheese model](https://en.wikipedia.org/wiki/Swiss_cheese_model). Every defensive layer in our security stack, including code scanning, IAM policies, network segmentation and runtime protection, is a slice of cheese with unavoidable holes. An attacker succeeds only when holes in every layer align to create a direct path.

A resilient architecture based on the Swiss cheese model relies on multiple, diverse defense layers. A vulnerability missed by a static application security testing scanner becomes useless under a least-privilege IAM role. A misconfigured IAM role receives neutralization from a runtime agent that detects and blocks anomalous behavior. Layer synergy prevents hole alignment.

![Swiss cheese model for cloud-native security](https://www.paloaltonetworks.com/blog/wp-content/uploads/2025/08/word-image-342823-1.png)

Figure 1: The swiss cheese model for cloud-native security

A resilient architecture built according to this principle requires a fundamental change in how we build software and measure security success. It stands on four critical concepts.

### Aggressive Containment

Modern cloud-native systems must be architected as a series of segmented, isolated compartments to prevent a breach in one microservice or container from cascading.

The most effective way to achieve isolation is by assigning each workload a strictly scoped, least-privileged IAM role. A compromised container then becomes a dead end for the attacker. Imagine a service whose IAM role grants only read access to a single S3 bucket. A breach of that service remains instantly contained. The attacker can’t access other databases, spin up new VMs or retrieve secrets. Lateral movement stops before it starts. I demonstrated this principle years ago in a Dark Reading article, detailing how a [compromised Lambda function becomes neutralized by a minimal IAM role](https://www.darkreading.com/cloud-security/securing-serverless-attacking-an-aws-account-via-a-lambda-function).

### Real-Time Visibility

Runtime security agents deployed directly on workloads provide the intelligence required for resilience. They detect attacks in real time.

Organizations relying solely on agentless scanning measure mean-time-to-detect in days. Those deploying a runtime agent directly on workloads achieve continuous detection within minutes.

A resilient system depends on a single source of truth. It must correlate application vulnerabilities with runtime exploit attempts and cloud misconfigurations with lateral movement. Unified telemetry enables the split-second decisions resilience demands.

Consider a typical cloud breach. An attacker exploits a container vulnerability, escalates privileges using leaked IAM credentials and moves laterally. A [unified platform](https://www.paloaltonetworks.com/cortex/cloud) sees the entire attack path unfold in real time.

### Immediate Response

Detection alone holds no value if response lags behind an attack. Manual investigation workflows collapse under machine-speed attacks. Resilient applications must use real-time defenses. When runtime agents detect the exploitation of a known vulnerability, the system must instantly map the attack path and execute containment. The precision required for automated containment, where a false positive could disrupt business, demands the highest degree of detection accuracy.

We need to remove the bottleneck. Imagine an API protected by a runtime agent. Having detected an exploit, the agent alerts the security platform, which instantly severs the malicious connection, freezes the compromised process for forensic analysis and quarantines the container from the network — all before a human analyst is even aware of the event.

### Guarantee Operational Survival

An automated response is powerful, but only if the cure isn't worse than the disease. The final pillar of resilience ensures the business survives its own defenses.

A resilient system must ensure core business functions persist even when defenses isolate components. A financial trading platform, for example, should continue processing transactions if an auxiliary market data analysis service becomes quarantined.

Designing for graceful degradation goes beyond high availability. It ensures business continuity in a hostile digital environment and validates the resilience strategy’s ultimate goal — operational survival.

## Resilience by Design: Beyond the First 5 Minutes

To answer the defining question — _what happens in the five minutes after breach?_ — we must redefine success. Security no longer means preventing every compromise. It means ensuring that even at machine speed, attackers can’t achieve their objectives.

Resilience by design represents an evolution in strategic thinking. Organizations adopting this mindset will set the new standard in cybersecurity, prevailing not by the perfection of defenses, but by their power to endure.

To learn more about a unified approach to security, read [Breaking Barriers in Enterprise Security: An Executive Guide to Cloud Security and SOC Convergence](https://www.paloaltonetworks.com/resources/guides/cortex-cloud-executive-guide).

* * *

## Related Blogs

### [AI Security](https://www.paloaltonetworks.com/blog/category/ai-security/), [AI Security Posture Management](https://www.paloaltonetworks.com/blog/cloud-security/category/ai-security-posture-management/), [Artificial Intelligence](https://www.paloaltonetworks.com/blog/cloud-security/category/artificial-intelligence/), [Cloud Security](https://www.paloaltonetworks.com/blog/cloud-security/category/cloud-security/), [CSPM](https://www.paloaltonetworks.com/blog/cloud-security/category/cspm/)

[**The Rise of AI-Powered IDEs: What the Windsurf Acquisition News Mean for Security Teams**](https://www.paloaltonetworks.com/blog/cloud-security/windsurf-openai-acquisition/)

### [AI Governance](https://www.paloaltonetworks.com/blog/category/ai-governance/), [AI Security](https://www.paloaltonetworks.com/blog/category/ai-security/), [Announcement](https://www.paloaltonetworks.com/blog/category/announcement/), [Government](https://www.paloaltonetworks.com/blog/category/government/), [Points of View](https://www.paloaltonetworks.com/blog/category/points-of-view/), [Public Sector](https://www.paloaltonetworks.com/blog/category/public-sector/)

[**A Secure Vision for Our AI-Driven Future**](https://www.paloaltonetworks.com/blog/2025/07/secure-vision-ai-driven-future/)

### [AI Security](https://www.paloaltonetworks.com/blog/category/ai-security/), [Interview](https://www.paloaltonetworks.com/blog/category/interview/)

[**Security by Design — UX and AI in Modern Cybersecurity**](https://www.paloaltonetworks.com/blog/2025/07/security-by-design-ux-ai-modern-cybersecurity/)

### [Announcement](https://www.paloaltonetworks.com/blog/category/announcement/), [Cloud ASM](https://www.paloaltonetworks.com/blog/cloud-security/category/cloud-asm/), [Cloud Security](https://www.paloaltonetworks.com/blog/cloud-security/category/cloud-security/), [CNAPP](https://www.paloaltonetworks.com/blog/cloud-security/category/cnapp/)

[**What’s New in Cortex Cloud**](https://www.paloaltonetworks.com/blog/cloud-security/attack-surface-dspm-fim/)

### [AI Security](https://www.paloaltonetworks.com/blog/category/ai-security/), [Application Security](https://www.paloaltonetworks.com/blog/cloud-security/category/application-security/), [ASPM](https://www.paloaltonetworks.com/blog/cloud-security/category/aspm/)

[**AI's Hidden Security Debt**](https://www.paloaltonetworks.com/blog/cloud-security/ai-security-debt/)

### [AI Security](https://www.paloaltonetworks.com/blog/category/ai-security/), [AI Security Posture Management](https://www.paloaltonetworks.com/blog/cloud-security/category/ai-security-posture-management/)

[**Implementing AI Security with Cortex Cloud AI-SPM**](https://www.paloaltonetworks.com/blog/cloud-security/implementing-ai-security-with-cortex-cloud-ai-spm/)

### Subscribe to Cloud Security Blogs!

Sign up to receive must-read articles, Playbooks of the Week, new feature announcements, and more.

![spinner](https://www.paloaltonetworks.com/blog/wp-content/themes/panwblog2023/dist/images/ajax-loader.gif)
Sign up


Please enter a valid email.

By submitting this form, you agree to our [Terms of Use](https://www.paloaltonetworks.com/legal-notices/terms-of-use) and acknowledge our [Privacy Statement](https://www.paloaltonetworks.com/legal-notices/privacy). Please look for a confirmation email from us. If you don't receive it in the next 10 minutes, please check your spam folder.

## Get the latest news, invites to events, and threat alerts

Enter your email now to subscribe!

Sign up

By submitting this form, you agree to our
[Terms of Use](https://www.paloaltonetworks.com/legal-notices/terms-of-use)
and acknowledge our
[Privacy Statement](https://www.paloaltonetworks.com/legal-notices/privacy).


Sign up

## Products and Services

- [AI-Powered Network Security Platform](https://www.paloaltonetworks.com/network-security)
- [Secure AI by Design](https://www.paloaltonetworks.com/precision-ai-security/secure-ai-by-design)
- [Prisma AIRS](https://www.paloaltonetworks.com/prisma/prisma-ai-runtime-security)
- [AI Access Security](https://www.paloaltonetworks.com/sase/ai-access-security)
- [Cloud Delivered Security Services](https://www.paloaltonetworks.com/network-security/security-subscriptions)
- [Advanced Threat Prevention](https://www.paloaltonetworks.com/network-security/advanced-threat-prevention)
- [Advanced URL Filtering](https://www.paloaltonetworks.com/network-security/advanced-url-filtering)
- [Advanced WildFire](https://www.paloaltonetworks.com/network-security/advanced-wildfire)
- [Advanced DNS Security](https://www.paloaltonetworks.com/network-security/advanced-dns-security)
- [Enterprise Data Loss Prevention](https://www.paloaltonetworks.com/sase/enterprise-data-loss-prevention)
- [Enterprise IoT Security](https://www.paloaltonetworks.com/network-security/enterprise-iot-security)
- [Medical IoT Security](https://www.paloaltonetworks.com/network-security/medical-iot-security)
- [Industrial OT Security](https://www.paloaltonetworks.com/network-security/industrial-ot-security)
- [SaaS Security](https://www.paloaltonetworks.com/sase/saas-security)

- [Next-Generation Firewalls](https://www.paloaltonetworks.com/network-security/next-generation-firewall)
- [Hardware Firewalls](https://www.paloaltonetworks.com/network-security/hardware-firewall-innovations)
- [Software Firewalls](https://www.paloaltonetworks.com/network-security/software-firewalls)
- [Strata Cloud Manager](https://www.paloaltonetworks.com/network-security/strata-cloud-manager)
- [SD-WAN for NGFW](https://www.paloaltonetworks.com/network-security/sd-wan-subscription)
- [PAN-OS](https://www.paloaltonetworks.com/network-security/pan-os)
- [Panorama](https://www.paloaltonetworks.com/network-security/panorama)
- [Secure Access Service Edge](https://www.paloaltonetworks.com/sase)
- [Prisma SASE](https://www.paloaltonetworks.com/sase)
- [Application Acceleration](https://www.paloaltonetworks.com/sase/app-acceleration)
- [Autonomous Digital Experience Management](https://www.paloaltonetworks.com/sase/adem)
- [Enterprise DLP](https://www.paloaltonetworks.com/sase/enterprise-data-loss-prevention)
- [Prisma Access](https://www.paloaltonetworks.com/sase/access)
- [Prisma Access Browser](https://www.paloaltonetworks.com/sase/prisma-access-browser)
- [Prisma SD-WAN](https://www.paloaltonetworks.com/sase/sd-wan)
- [Remote Browser Isolation](https://www.paloaltonetworks.com/sase/remote-browser-isolation)
- [SaaS Security](https://www.paloaltonetworks.com/sase/saas-security)

- [AI-Driven Security Operations Platform](https://www.paloaltonetworks.com/cortex)
- [Cloud Security](https://www.paloaltonetworks.com/cortex/cloud)
- [Cortex Cloud](https://www.paloaltonetworks.com/cortex/cloud)
- [Application Security](https://www.paloaltonetworks.com/cortex/cloud/application-security)
- [Cloud Posture Security](https://www.paloaltonetworks.com/cortex/cloud/cloud-posture-security)
- [Cloud Runtime Security](https://www.paloaltonetworks.com/cortex/cloud/runtime-security)
- [Prisma Cloud](https://www.paloaltonetworks.com/prisma/cloud)
- [AI-Driven SOC](https://www.paloaltonetworks.com/cortex)
- [Cortex XSIAM](https://www.paloaltonetworks.com/cortex/cortex-xsiam)
- [Cortex XDR](https://www.paloaltonetworks.com/cortex/cortex-xdr)
- [Cortex XSOAR](https://www.paloaltonetworks.com/cortex/cortex-xsoar)
- [Cortex Xpanse](https://www.paloaltonetworks.com/cortex/cortex-xpanse)
- [Unit 42 Managed Detection & Response](https://www.paloaltonetworks.com/cortex/managed-detection-and-response)
- [Managed XSIAM](https://www.paloaltonetworks.com/cortex/managed-xsiam)

- [Threat Intel and Incident Response Services](https://www.paloaltonetworks.com/unit42)
- [Proactive Assessments](https://www.paloaltonetworks.com/unit42/assess)
- [Incident Response](https://www.paloaltonetworks.com/unit42/respond)
- [Transform Your Security Strategy](https://www.paloaltonetworks.com/unit42/transform)
- [Discover Threat Intelligence](https://www.paloaltonetworks.com/unit42/threat-intelligence-partners)

## Company

- [About Us](https://www.paloaltonetworks.com/about-us)
- [Careers](https://jobs.paloaltonetworks.com/en/)
- [Contact Us](https://www.paloaltonetworks.com/company/contact-sales)
- [Corporate Responsibility](https://www.paloaltonetworks.com/about-us/corporate-responsibility)
- [Customers](https://www.paloaltonetworks.com/customers)
- [Investor Relations](https://investors.paloaltonetworks.com/)
- [Location](https://www.paloaltonetworks.com/about-us/locations)
- [Newsroom](https://www.paloaltonetworks.com/company/newsroom)

## Popular Links

- [Blog](https://www.paloaltonetworks.com/blog/)
- [Communities](https://www.paloaltonetworks.com/communities)
- [Content Library](https://www.paloaltonetworks.com/resources)
- [Cyberpedia](https://www.paloaltonetworks.com/cyberpedia)
- [Event Center](https://events.paloaltonetworks.com/)
- [Manage Email Preferences](https://start.paloaltonetworks.com/preference-center)
- [Products A-Z](https://www.paloaltonetworks.com/products/products-a-z)
- [Product Certifications](https://www.paloaltonetworks.com/legal-notices/trust-center/compliance)
- [Report a Vulnerability](https://www.paloaltonetworks.com/security-disclosure)
- [Sitemap](https://www.paloaltonetworks.com/sitemap)
- [Tech Docs](https://docs.paloaltonetworks.com/)
- [Unit 42](https://unit42.paloaltonetworks.com/)
- [Do Not Sell or Share My Personal Information](https://panwedd.exterro.net/portal/dsar.htm?target=panwedd)
