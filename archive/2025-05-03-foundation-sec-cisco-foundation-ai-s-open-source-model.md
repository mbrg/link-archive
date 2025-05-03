---
title: "Foundation-sec: Cisco Foundation AI's Open-Source Model"
tags:
   - Open Source
   - Large Language Model
   - Threat Intelligence
   - Cybersecurity Infrastructure
   - AI Cybersecurity
link: https://blogs.cisco.com/security/foundation-sec-cisco-foundation-ai-first-open-source-security-model
date: 2025-05-03
summary: "Cisco's Foundation AI has unveiled Foundation-sec-8b, an 8-billion parameter open-weight LLM specifically designed for cybersecurity. This model addresses the limitations of traditional AI in security applications, offering enhanced precision, reduced response times, and deeper insights with domain-specific training data. It outperforms larger models on critical security benchmarks while maintaining flexibility for customization and deployment in diverse environments. Foundation-sec-8b is tailored for tasks like threat analysis and SOC operations, promoting accelerated defense mechanisms. The release underscores Cisco's commitment to embedding AI deeply within security frameworks, with future tools and enhancements anticipated."
---

[Skip to content](https://blogs.cisco.com/security/foundation-sec-cisco-foundation-ai-first-open-source-security-model#content)

![Avatar](https://storage.googleapis.com/blogs-images-new/ciscoblogs/1/2025/04/IL20250423200708-ysinger-150x150.jpeg)

[**Security**](https://blogs.cisco.com/security)

# Foundation-sec-8b: Cisco Foundation AI’s First Open-Source Security Model

4 min read

[Yaron Singer](https://blogs.cisco.com/author/ysinger "Posts by Yaron Singer")

Cisco is proud to mark a major milestone in its AI journey. Our newly launched **Foundation AI** group—formed to bring world-class, domain-specific AI infrastructure to the cybersecurity space—is proud to introduce its first release: **Llama-3.1-FoundationAI-SecurityLLM-base-8B (Foundation-sec-8b)**, an **8-billion parameter**, open-weight Large Language Model (LLM) purpose-built for security.

This model combines deep domain expertise with the flexibility and control needed for secure, real-world deployment. With Foundation-sec-8B, teams can build, fine-tune, and deploy AI-native workflows across the security lifecycle. This model is designed to help security teams think faster, act with precision, and scale operations without compromise.

## Cybersecurity Applications Require Purpose-Built, open, Small Models

Security teams today face unprecedented pressure. Threats are growing faster, attacks are more complex, and traditional tools aren’t enough. AI is emerging as a critical force multiplier—but general-purpose models often fall short for real-world security workflows.

Prompting and retrieval pipelines can’t meet the precision, consistency, and quality demands of security operations. Fine-tuning closed models brings its own challenges: high costs, limited control, and deployment barriers—especially where data privacy, regulatory compliance, and in-environment hosting are non-negotiable. Meanwhile, most open models lack the domain-specific knowledge security teams need.

> “Foundation-sec-8b is a foundational step toward building AI-native security systems—tools that don’t just process data but truly understand the security domain. This model gives security teams everywhere a powerful building block to accelerate defense, reduce fatigue, and gain clarity in complex threat environments.”
>
> Jeetu Patel, Chief Product Officer, Cisco

## A Purpose-Built Model for Security

Foundation-sec-8b isn’t a general-purpose model retrofitted for security. It was designed from the ground up to understand the language, logic, and workflows of cybersecurity.

Built with Llama, using the **Llama 3.1 8B framework**, foundation-sec-8b has been pre-trained on a dataset meticulously built in-house by Cisco Foundation AI. This dataset was curated specifically to capture the real-world knowledge and context that security professionals work with every day. It includes, but is not limited to:

- Vulnerability databases and threat behavior mappings (e.g., CVEs, CWEs, MITRE ATT&CK)
- Threat intelligence reports, red team playbooks, and real-world incident summaries
- Security tooling documentation across cloud, identity, and infrastructure domains
- Compliance references and secure development practices (e.g., NIST, OWASP, secure coding guides)

This domain alignment makes foundation-sec-8b immediately effective across analyst workflows—delivering **deeper insights, fewer hallucinations, and dramatically lower response times** compared to generalist models.

## Performance That Punches Above Its Weight

Despite its **8B parameter size**, foundation-sec-8b results are comparable with models nearly 10x larger. On core cybersecurity benchmarks, it **outperforms Llama 3.1 8B** and even **matches or exceeds Llama 3.1 70B**, offering powerful inference at a fraction of the cost and infrastructure burden.

| Benchmark | Model<br>Foundation-sec-8b | Model<br>Llama-3.1-8b | Model<br>Llama-3.1 70B |
| --- | --- | --- | --- |
| [CTI-MCQA](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5acd3c628aa1819fbf07c39ef73e7285-Abstract-Datasets_and_Benchmarks_Track.html) | 67.39 | 64.14 | 68.23 |
| [CTI-RCM](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5acd3c628aa1819fbf07c39ef73e7285-Abstract-Datasets_and_Benchmarks_Track.html) | 75.26 | 66.43 | 72.66 |

Importantly, foundation-sec-8b maintains strong general language performance, staying on par with Llama models on MMLU benchmarks. This means it can fluidly explain threat behavior, support long-form investigation narratives, and respond naturally in chat-based workflows—without compromising its security focus.

Its advantages grow even more apparent with fine-tuning. In downstream security tasks—such as extracting MITRE ATT&CK techniques from unstructured threat reports—a fine-tuned foundation-sec-8b model significantly outperformed fine-tuning the same-sized Llama model. This reinforces the value of foundation-sec-8b as both a foundational model and a high-impact component for embedded security workflows.

## Practical Applications—and Built to Fit Your Environment

Foundation-sec-8b isn’t just performant—it’s versatile. **Being open-weight and built on the Llama framework** makes it easy to fine-tune or extend with your own telemetry, detection rules, or threat intel. Whether you’re embedding it into existing tools or building entirely new workflows, foundation-sec-8b adapts to your organization’s unique needs.

Security teams can apply foundation-sec-8b across the security lifecycle:

- **SOC acceleration** – Automate alert triage, summarize incidents, and assist with investigations
- **Proactive threat defense** – Simulate attacks, prioritize vulnerabilities, and model threats tailored to your infrastructure
- **Engineering enablement** – Deliver AI-assisted code reviews, validate configurations, and assess compliance evidence with context from your environment
- **Custom integration** – Fine-tune the model to reflect your security posture, language, and detection strategies—ensuring precision in real-world deployments

> “We have been working with the Cisco Foundation AI team exploring how to embed foundation-sec-8b across Cisco’s internal security stack. We are very excited about the capabilities of an AI model that truly understands our domain and can scale across use cases.”
>
> Omar Santos, Distinguished Engineer, Cisco Security & Trust Organization (S&TO)

From powering agentic assistant workflows to assisting developers in writing secure-by-default code, foundation-sec-8b is a foundation you can build on.

## Publicly Available, With Privacy and Control in Mind

In cybersecurity, trust is non-negotiable. That’s why foundation-sec-8b is open-weight, with weights and tokenizer released under a permissive license.

This gives organizations:

- **Full control over deployment** – Run the model on-prem, in air-gapped environments, or within secure cloud enclaves
- **Compliance confidence** – Keep sensitive data local; no forced inference APIs or third-party sharing
- **Customization freedom** – Adapt and extend the model architecture or training pipeline to meet unique security and privacy needs

Foundation-sec-8b is now available for download on [Hugging Face](https://huggingface.co/fdtn-ai/Foundation-Sec-8B).

You can also read the full technical details in our [research paper](https://huggingface.co/fdtn-ai/Foundation-Sec-8B/blob/main/Technical_Report.pdf).

In the near future, we also plan to open source the training pipeline used to build the model. For more on the data construction and training process, refer to the research paper.

## Just the Beginning

Foundation-sec-8b is the **first release** from **Cisco Foundation AI**, a dedicated group building the infrastructure that will drive the next decade of cybersecurity innovation. This model lays the groundwork for a future where AI isn’t just a bolt-on feature—but **a foundational capability** embedded across the entire security lifecycle.

And we’re just getting started.

Over the coming months, Cisco Foundation AI will be releasing:

- A **cybersecurity reasoning model** that brings explainability and deeper analysis to complex security workflows
- A new **benchmark suite** designed to evaluate AI models on real-world, practitioner-defined security tasks
- Additional tools and components that help teams fine-tune, operationalize, and embed AI safely and effectively into their security stacks

Foundation-sec-8b opens the door. What comes next will reshape how defenders build, respond, and lead with AI.

**Foundation-sec-8b is live. It’s open. And it’s ready to defend.**

Explore the model, join the community, and help shape the next generation of AI-powered cybersecurity.

* * *

We’d love to hear what you think. Ask a Question, Comment Below, and Stay Connected with Cisco Security on social!

**Cisco Security Social Handles**

[LinkedIn](https://www.linkedin.com/showcase/cisco-security)

[Facebook](https://www.facebook.com/ciscosecurity)

[Instagram](https://www.instagram.com/ciscosecurity/)

[X](https://x.com/CiscoSecure)

Share

Share:

## Authors

[![Avatar](https://storage.googleapis.com/blogs-images-new/ciscoblogs/1/2025/04/IL20250423200708-ysinger-150x150.jpeg)](https://blogs.cisco.com/author/ysinger)

### [Yaron Singer](https://blogs.cisco.com/author/ysinger)

#### VP of AI and Security at Foundation

#### Foundation AI

Tags: [AI Cybersecurity](https://blogs.cisco.com/tag/ai-cybersecurity) [Artificial Intelligence (AI)](https://blogs.cisco.com/tag/artificial-intelligence) [Foundation AI](https://blogs.cisco.com/tag/foundation-ai) [Security for AI](https://blogs.cisco.com/tag/security-for-ai)

* * *

### Leave a Comment [Cancel reply](https://blogs.cisco.com/security/foundation-sec-cisco-foundation-ai-first-open-source-security-model\#respond)

We'd love to hear from you! Your comment(s) will appear instantly on the live site. Spam, promotional and derogatory comments will be removed and HTML formatting will not appear.

Comment \*

Name

Δ

## 3 Comments

- I’m absolutely thrilled about this new model and the possibilities it brings. I can’t wait to dive in and get hands-on experience with a network-centric model!





[Reply](https://blogs.cisco.com/security/foundation-sec-cisco-foundation-ai-first-open-source-security-model#comment-2584837)

- Nazeey





[Reply](https://blogs.cisco.com/security/foundation-sec-cisco-foundation-ai-first-open-source-security-model#comment-2584845)

- If you can also show a real world example on how to use it that would add more sense rather than such theory . What we see and experience helps us to trust that a lot . Till now whatever you suggested can be done by a normal AI model as well nothing so different





[Reply](https://blogs.cisco.com/security/foundation-sec-cisco-foundation-ai-first-open-source-security-model#comment-2584865)


![](https://storage.googleapis.com/blogs-images-new/ciscoblogs/1/2023/07/IL20230719143932-Cybersecurity-Expert-graphic-marquee-3-scaled-150x150.jpg)

## Cisco Cybersecurity Viewpoints

Where security insights and innovation meet. Read the e-book, see the video, dive into the infographic and more...

Get expert perspectives now

![](https://alln-extcloud-storage.cisco.com/Cisco_Blogs:blogs/1/2020/01/IL20200117171458-Screen-Shot-2020-01-17-at-12.13.39-PM-150x150.png)

## Why Cisco Security?

Explore our Products & Services

Learn More

##### CONNECT WITH US
