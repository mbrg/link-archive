---
title: "Sharing new open source protection tools and advancements in AI privacy and security"
tags:
   - Open Source
   - Cybersecurity Tools
   - Meta AI
   - AI Security
   - Llama Model
link: https://ai.meta.com/blog/ai-defenders-program-llama-protection-tools/
date: 2025-05-04
description: "Meta has launched new Llama protection tools aimed at improving AI security and privacy for developers. Key advancements include Llama Guard 4, which enhances protection across modalities, and LlamaFirewall, designed to mitigate risks from AI prompt injection and insecure interactions. The updated CyberSecEval 4 benchmark will assess AI defense capabilities in the security operations context. Additionally, Meta's Private Processing technology aims to keep AI request processing private while enhancing user functionalities like message summarization in WhatsApp. These resources aim to bolster security frameworks within the open-source AI community."
---

[Go up one level](https://ai.meta.com/blog/ai-defenders-program-llama-protection-tools/# "Go up one level") [![Meta](https://scontent.xx.fbcdn.net/v/t39.8562-6/252294889_575082167077436_6034106545912333281_n.svg/meta-logo-primary_standardsize.svg?_nc_cat=1&ccb=1-7&_nc_sid=e280be&_nc_ohc=1UXmLCmJXR0Q7kNvwGdg4Lk&_nc_oc=AdkJsgAQfDzZD2YtpVD53fSV8z_b9_zGYes6aSZ-OiSAscCQZPK4u1XV_EIRVrEvxQc&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfFLQa1N6ol-hMivOEilZxc37-CUiuIsjLqwLod4pAgrtA&oe=681CE079)](https://ai.meta.com/)

- [Our approach](https://ai.meta.com/blog/ai-defenders-program-llama-protection-tools/#)

- [Research](https://ai.meta.com/blog/ai-defenders-program-llama-protection-tools/#)

- [Meta AI](https://ai.meta.com/blog/ai-defenders-program-llama-protection-tools/#)

- [Llama](https://www.llama.com/)

- [Blog](https://ai.meta.com/blog/)


- [Try Meta AI](https://www.meta.ai/?utm_source=ai_meta_site&utm_medium=web&utm_content=AI_nav&utm_campaign=04292025_moment)
- [Toggle site search](https://ai.meta.com/blog/ai-defenders-program-llama-protection-tools/# "Toggle site search")


[Close submenu](https://ai.meta.com/blog/ai-defenders-program-llama-protection-tools/# "Close submenu") [Main menu](https://ai.meta.com/blog/ai-defenders-program-llama-protection-tools/# "Main menu")

[BACK](https://ai.meta.com/blog/ai-defenders-program-llama-protection-tools/# "Go up one level")

- [About us](https://ai.meta.com/about/)
- [People](https://ai.meta.com/results/?content_types[0]=person)
- [Careers](https://www.metacareers.com/)

- [Overview](https://ai.meta.com/research/)
- [Infrastructure](https://ai.meta.com/infrastructure/)
- [Resources](https://ai.meta.com/resources/)
- [Demos](https://aidemos.meta.com/)

- [Explore Meta AI](https://ai.meta.com/meta-ai/)
- [Get Meta AI](https://ai.meta.com/get-meta-ai/)
- [AI Studio](https://ai.meta.com/ai-studio/)

Clear

- Clear

- [Our approach\\
\\
>](https://ai.meta.com/blog/ai-defenders-program-llama-protection-tools/#)

- [Research\\
\\
>](https://ai.meta.com/blog/ai-defenders-program-llama-protection-tools/#)

- [Meta AI\\
\\
>](https://ai.meta.com/blog/ai-defenders-program-llama-protection-tools/#)

- [Llama](https://www.llama.com/)
- [Blog](https://ai.meta.com/blog/)

[Try Meta AI](https://www.meta.ai/?utm_source=ai_meta_site&utm_medium=web&utm_content=AI_nav&utm_campaign=04292025_moment)

FEATURED

Open Source

# Sharing new open source protection tools and advancements in AI privacy and security

April 29, 2025•

![](https://static.xx.fbcdn.net/rsrc.php/v4/yA/r/I5sXYV5XfVd.png)6 minute read

![](https://scontent.xx.fbcdn.net/v/t39.2365-6/490414961_1240604227411923_2781313039051156303_n.png?_nc_cat=110&ccb=1-7&_nc_sid=e280be&_nc_ohc=FcJ_qtTY2WIQ7kNvwFkDjpP&_nc_oc=AdnL5xnZGwPqkDoRs1pFdPZ-rGPyL5Y_JSGKUC3Mm-XAmHWcQrn8IwXR7Noa-t6D9KM&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfH_ZTaOKiabZquvtQV8xgdgLEMXzgfsyb0fZ2DDzKZsIQ&oe=683131F5)

## Takeaways

- Today, we’re releasing new [Llama](https://www.llama.com/) protection tools for the open source AI community.
- We’re providing new AI-enabled solutions to help the defender community proactively detect and secure critical infrastructure, systems, and services against active attacks.
- We’re also previewing our new technology that allows AI-related requests to be processed privately.

## The latest Llama protection tools for the open source community

We’re committed to providing developers with the best possible tools and resources to build secure AI applications. Developers can access our latest Llama Protection tools to be used when building with Llama by visiting Meta’s [Llama Protections page](https://www.llama.com/llama-protections/), [Hugging Face](https://huggingface.co/meta-llama), or [GitHub](https://github.com/meta-llama/PurpleLlama).

- Llama Guard 4: The new Llama Guard 4 is an update to our customizable Llama Guard tool, acting as a unified safeguard across modalities, supporting protections for text and image understanding. Llama Guard 4 is also available on our new Llama API, which we’re launching as a limited preview.
- LlamaFirewall: We’re introducing LlamaFirewall, a security guardrail tool to help build secure AI systems. LlamaFirewall can orchestrate across guard models and work with our suite of protection tools to detect and prevent AI system risks such as prompt injection, insecure code, and risky LLM plug-in interactions. For more details on the tool, please refer to the [LlamaFirewall research paper](https://ai.meta.com/research/publications/llamafirewall-an-open-source-guardrail-system-for-building-secure-ai-agents/).
- Llama Prompt Guard 2: Prompt Guard 2 86M, an update to our Llama Prompt Guard classifier model, improves on its performance in jailbreak and prompt injection detection. We’re also introducing Prompt Guard 2 22M, a smaller, faster version that can reduce latency and compute costs with minimal performance trade-offs by up to 75% compared to our 86M model.

Helping the defender community leverage AI in security operations

At Meta, we use AI to strengthen our security systems and defend against potential cyber attacks. We’ve heard from the community that they want access to AI-enabled tools that will help them do the same. That’s why we’re sharing updates to help organizations evaluate the efficacy of AI systems in security operations and announcing the [Llama Defenders Program](https://www.llama.com/llama-protections/ai-defenders) for select partners. We believe this is an important effort to improve the robustness of software systems as more capable AI models become available.

- CyberSec Eval 4: Our updated open source cybersecurity benchmark suite, [CyberSecEval 4](https://github.com/meta-llama/PurpleLlama/tree/main/CybersecurityBenchmarks/benchmark) includes new tools—CyberSOC Eval and AutoPatchBench—to assess AI systems’ defense capabilities.
  - CyberSOC Eval: Developed with CrowdStrike, this framework measures AI systems’ efficacy in security operation centers. Today, we’re announcing this benchmark, and will be releasing it soon.
  - AutoPatchBench: A new benchmark that evaluates the ability of Llama and other AI systems to automatically patch security vulnerabilities in native code before they can be exploited. [Learn more](https://engineering.fb.com/2025/04/29/ai-research/autopatchbench-benchmark-ai-powered-security-fixes) on the Engineering at Meta Blog.
- Llama Defenders Program: We’re launching the Llama Defenders Program to help partner organizations and developers access a variety of open, early-access, and closed AI solutions to address different security needs.
  - Automated Sensitive Doc Classification Tool: A tool we use internally at Meta, this automatically applies security classification labels to an organization’s internal documents to help prevent unauthorized access and distribution, or to filter out sensitive documents from an AI system’s RAG implementation. Learn more on [GitHub](https://github.com/meta-llama/PurpleLlama/tree/main/SensitiveDocClassification).
  - Llama Generated Audio Detector & Llama Audio Watermark Detector: Designed to detect AI-generated content, these tools will help organizations detect AI-generated threats, such as scams, fraud, and phishing attempts. At launch, we’re working with ZenDesk, Bell Canada, and AT&T to integrate these into their systems. If interested in learning more, other organizations can request information by visiting the [Llama Defenders Program website](https://www.llama.com/llama-protections/ai-defenders).

Building new technology to enable private processing for AI requests

We’re sharing the first look into Private Processing, our new technology that will help WhatsApp users leverage AI capabilities for things like summarizing unread messages or refining them, while keeping messages private so that Meta or WhatsApp cannot access them. More information on our security approach to building this technology, including the threat model that guides how we identify and defend against potential attack vectors, can be found on our [Engineering blog](https://engineering.fb.com/2025/04/29/security/whatsapp-private-processing-ai-tools/). We’re working with the security community to audit and improve our architecture and will continue to build and strengthen Private Processing in the open, in collaboration with researchers, before we launch it in product.

Looking ahead

We hope that the set of AI updates shared here will make it even easier for developers to build with Llama, help organizations enhance their security operations, and enable stronger privacy guarantees for certain AI use cases. We look forward to continuing this work and sharing more in the future.

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

![](https://scontent.xx.fbcdn.net/v/t39.2365-6/87524316_2677189655726266_6338721200264445952_n.svg?_nc_cat=103&ccb=1-7&_nc_sid=e280be&_nc_ohc=zRFrWECnUesQ7kNvwEtCcN2&_nc_oc=AdnAqbvmCoZWAKp1B7nYaIDwhzOfZK5HrMhCF9gsL9fM0gHRlOEjDkPO9yB3qXJvloQ&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfF8DAnNEQTxORCPrf6HVMPNawD0vOFX0-Zdw7XyPSZG5w&oe=68314A38)

![](https://scontent.xx.fbcdn.net/v/t39.2365-6/85559716_2814260008668824_1992323131183726592_n.svg?_nc_cat=103&ccb=1-7&_nc_sid=e280be&_nc_ohc=a7XzDKqkv70Q7kNvwEAq7gi&_nc_oc=Adm6186nAALtxkC3Kb4VzUkuRTMfGztriSbmKKmzj3i8mpKndWIJXsmZSi10RtKZi7g&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfHbeAc-wKB9IpCkYkT2IILPMSshC-bJC7vXAGzhCZQT4g&oe=68314F0F)

[![](https://scontent.xx.fbcdn.net/v/t39.8562-6/335682312_964107378293184_3093631164486164913_n.svg?_nc_cat=100&ccb=1-7&_nc_sid=e280be&_nc_ohc=fMdxsXTscrgQ7kNvwGDKRQ8&_nc_oc=AdmFxNXIyghcbfJteQChZQbyMss7509qy1Zvsltxmx7zCuzRPOK4nHQZ93Dc7o15Ptw&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfE_zZHO8x37v8LNF6BxNzuRHGxAWm7coP7iYfWMALXzsA&oe=681CD0A7)\\
\\
![](https://scontent.xx.fbcdn.net/v/t39.8562-6/335682312_964107378293184_3093631164486164913_n.svg?_nc_cat=100&ccb=1-7&_nc_sid=e280be&_nc_ohc=fMdxsXTscrgQ7kNvwGDKRQ8&_nc_oc=AdmFxNXIyghcbfJteQChZQbyMss7509qy1Zvsltxmx7zCuzRPOK4nHQZ93Dc7o15Ptw&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfE_zZHO8x37v8LNF6BxNzuRHGxAWm7coP7iYfWMALXzsA&oe=681CD0A7)](https://www.facebook.com/aiatmeta/)

[![](https://scontent.xx.fbcdn.net/v/t39.8562-6/336009607_1870102080040414_6753977241281150924_n.svg?_nc_cat=103&ccb=1-7&_nc_sid=e280be&_nc_ohc=ZtW4P3kEIE0Q7kNvwGgLPZo&_nc_oc=AdkJC30ShLlYRieGi7gOfmhwEqzpa9eMH3e0gPvO3U1Pb42N59ZoZreVwvG3DSM0nSo&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfEi1rZwbat_eetCl1g1e2IbLEEaWSjK3-BO_WkMJLM-Rw&oe=681CC8E2)\\
\\
![](https://scontent.xx.fbcdn.net/v/t39.8562-6/336009607_1870102080040414_6753977241281150924_n.svg?_nc_cat=103&ccb=1-7&_nc_sid=e280be&_nc_ohc=ZtW4P3kEIE0Q7kNvwGgLPZo&_nc_oc=AdkJC30ShLlYRieGi7gOfmhwEqzpa9eMH3e0gPvO3U1Pb42N59ZoZreVwvG3DSM0nSo&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfEi1rZwbat_eetCl1g1e2IbLEEaWSjK3-BO_WkMJLM-Rw&oe=681CC8E2)](https://twitter.com/aiatmeta/)

[![](https://scontent.xx.fbcdn.net/v/t39.8562-6/336289415_1541032296405649_2165099305308791297_n.svg?_nc_cat=109&ccb=1-7&_nc_sid=e280be&_nc_ohc=eeYi5emVeWgQ7kNvwFRs0-W&_nc_oc=Adn09xeUeFBqi4pwjszCbrueXxFaMX-bkKGW0u7aeV_8cooUeBrnG2xs-ca76NIlsOs&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfGtIPqhBwk3O0xSicEhETbdhdLkWX6M7WYoFDdS2SfqoA&oe=681CF4BB)\\
\\
![](https://scontent.xx.fbcdn.net/v/t39.8562-6/336289415_1541032296405649_2165099305308791297_n.svg?_nc_cat=109&ccb=1-7&_nc_sid=e280be&_nc_ohc=eeYi5emVeWgQ7kNvwFRs0-W&_nc_oc=Adn09xeUeFBqi4pwjszCbrueXxFaMX-bkKGW0u7aeV_8cooUeBrnG2xs-ca76NIlsOs&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfGtIPqhBwk3O0xSicEhETbdhdLkWX6M7WYoFDdS2SfqoA&oe=681CF4BB)](https://www.linkedin.com/showcase/aiatmeta)

[![](https://scontent.xx.fbcdn.net/v/t39.8562-6/335648731_142576991793348_7786819189843639239_n.svg?_nc_cat=108&ccb=1-7&_nc_sid=e280be&_nc_ohc=t6wPNAM7D4sQ7kNvwGlWyB7&_nc_oc=AdnPOBpFgF_Q9smDcLO-AdAodES7ozBYtyw9AgqIqE2zHXSRh6CnY8OfkRincAftHW8&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfHBKuGgd4A1Hwe8mr2zY7kYIqOpzagoNbTBrZFAl5q7sQ&oe=681CD5EE)\\
\\
![](https://scontent.xx.fbcdn.net/v/t39.8562-6/335648731_142576991793348_7786819189843639239_n.svg?_nc_cat=108&ccb=1-7&_nc_sid=e280be&_nc_ohc=t6wPNAM7D4sQ7kNvwGlWyB7&_nc_oc=AdnPOBpFgF_Q9smDcLO-AdAodES7ozBYtyw9AgqIqE2zHXSRh6CnY8OfkRincAftHW8&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfHBKuGgd4A1Hwe8mr2zY7kYIqOpzagoNbTBrZFAl5q7sQ&oe=681CD5EE)](https://www.youtube.com/@aiatmeta)

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

[![](https://scontent.xx.fbcdn.net/v/t39.8562-6/335682312_964107378293184_3093631164486164913_n.svg?_nc_cat=100&ccb=1-7&_nc_sid=e280be&_nc_ohc=fMdxsXTscrgQ7kNvwGDKRQ8&_nc_oc=AdmFxNXIyghcbfJteQChZQbyMss7509qy1Zvsltxmx7zCuzRPOK4nHQZ93Dc7o15Ptw&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfE_zZHO8x37v8LNF6BxNzuRHGxAWm7coP7iYfWMALXzsA&oe=681CD0A7)\\
\\
![](https://scontent.xx.fbcdn.net/v/t39.8562-6/335682312_964107378293184_3093631164486164913_n.svg?_nc_cat=100&ccb=1-7&_nc_sid=e280be&_nc_ohc=fMdxsXTscrgQ7kNvwGDKRQ8&_nc_oc=AdmFxNXIyghcbfJteQChZQbyMss7509qy1Zvsltxmx7zCuzRPOK4nHQZ93Dc7o15Ptw&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfE_zZHO8x37v8LNF6BxNzuRHGxAWm7coP7iYfWMALXzsA&oe=681CD0A7)](https://www.facebook.com/aiatmeta/)

[![](https://scontent.xx.fbcdn.net/v/t39.8562-6/336009607_1870102080040414_6753977241281150924_n.svg?_nc_cat=103&ccb=1-7&_nc_sid=e280be&_nc_ohc=ZtW4P3kEIE0Q7kNvwGgLPZo&_nc_oc=AdkJC30ShLlYRieGi7gOfmhwEqzpa9eMH3e0gPvO3U1Pb42N59ZoZreVwvG3DSM0nSo&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfEi1rZwbat_eetCl1g1e2IbLEEaWSjK3-BO_WkMJLM-Rw&oe=681CC8E2)\\
\\
![](https://scontent.xx.fbcdn.net/v/t39.8562-6/336009607_1870102080040414_6753977241281150924_n.svg?_nc_cat=103&ccb=1-7&_nc_sid=e280be&_nc_ohc=ZtW4P3kEIE0Q7kNvwGgLPZo&_nc_oc=AdkJC30ShLlYRieGi7gOfmhwEqzpa9eMH3e0gPvO3U1Pb42N59ZoZreVwvG3DSM0nSo&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfEi1rZwbat_eetCl1g1e2IbLEEaWSjK3-BO_WkMJLM-Rw&oe=681CC8E2)](https://twitter.com/aiatmeta/)

[![](https://scontent.xx.fbcdn.net/v/t39.8562-6/336289415_1541032296405649_2165099305308791297_n.svg?_nc_cat=109&ccb=1-7&_nc_sid=e280be&_nc_ohc=eeYi5emVeWgQ7kNvwFRs0-W&_nc_oc=Adn09xeUeFBqi4pwjszCbrueXxFaMX-bkKGW0u7aeV_8cooUeBrnG2xs-ca76NIlsOs&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfGtIPqhBwk3O0xSicEhETbdhdLkWX6M7WYoFDdS2SfqoA&oe=681CF4BB)\\
\\
![](https://scontent.xx.fbcdn.net/v/t39.8562-6/336289415_1541032296405649_2165099305308791297_n.svg?_nc_cat=109&ccb=1-7&_nc_sid=e280be&_nc_ohc=eeYi5emVeWgQ7kNvwFRs0-W&_nc_oc=Adn09xeUeFBqi4pwjszCbrueXxFaMX-bkKGW0u7aeV_8cooUeBrnG2xs-ca76NIlsOs&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfGtIPqhBwk3O0xSicEhETbdhdLkWX6M7WYoFDdS2SfqoA&oe=681CF4BB)](https://www.linkedin.com/showcase/aiatmeta)

[![](https://scontent.xx.fbcdn.net/v/t39.8562-6/335648731_142576991793348_7786819189843639239_n.svg?_nc_cat=108&ccb=1-7&_nc_sid=e280be&_nc_ohc=t6wPNAM7D4sQ7kNvwGlWyB7&_nc_oc=AdnPOBpFgF_Q9smDcLO-AdAodES7ozBYtyw9AgqIqE2zHXSRh6CnY8OfkRincAftHW8&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfHBKuGgd4A1Hwe8mr2zY7kYIqOpzagoNbTBrZFAl5q7sQ&oe=681CD5EE)\\
\\
![](https://scontent.xx.fbcdn.net/v/t39.8562-6/335648731_142576991793348_7786819189843639239_n.svg?_nc_cat=108&ccb=1-7&_nc_sid=e280be&_nc_ohc=t6wPNAM7D4sQ7kNvwGlWyB7&_nc_oc=AdnPOBpFgF_Q9smDcLO-AdAodES7ozBYtyw9AgqIqE2zHXSRh6CnY8OfkRincAftHW8&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfHBKuGgd4A1Hwe8mr2zY7kYIqOpzagoNbTBrZFAl5q7sQ&oe=681CD5EE)](https://www.youtube.com/@aiatmeta)

[Privacy Policy](https://www.facebook.com/about/privacy/)

[Terms](https://www.facebook.com/policies/)

[Cookies](https://www.facebook.com/policies/cookies/)

Meta © 2025

[![](https://scontent.xx.fbcdn.net/v/t39.8562-6/335682312_964107378293184_3093631164486164913_n.svg?_nc_cat=100&ccb=1-7&_nc_sid=e280be&_nc_ohc=fMdxsXTscrgQ7kNvwGDKRQ8&_nc_oc=AdmFxNXIyghcbfJteQChZQbyMss7509qy1Zvsltxmx7zCuzRPOK4nHQZ93Dc7o15Ptw&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfE_zZHO8x37v8LNF6BxNzuRHGxAWm7coP7iYfWMALXzsA&oe=681CD0A7)\\
\\
![](https://scontent.xx.fbcdn.net/v/t39.8562-6/335682312_964107378293184_3093631164486164913_n.svg?_nc_cat=100&ccb=1-7&_nc_sid=e280be&_nc_ohc=fMdxsXTscrgQ7kNvwGDKRQ8&_nc_oc=AdmFxNXIyghcbfJteQChZQbyMss7509qy1Zvsltxmx7zCuzRPOK4nHQZ93Dc7o15Ptw&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfE_zZHO8x37v8LNF6BxNzuRHGxAWm7coP7iYfWMALXzsA&oe=681CD0A7)](https://www.facebook.com/aiatmeta/)

[![](https://scontent.xx.fbcdn.net/v/t39.8562-6/336009607_1870102080040414_6753977241281150924_n.svg?_nc_cat=103&ccb=1-7&_nc_sid=e280be&_nc_ohc=ZtW4P3kEIE0Q7kNvwGgLPZo&_nc_oc=AdkJC30ShLlYRieGi7gOfmhwEqzpa9eMH3e0gPvO3U1Pb42N59ZoZreVwvG3DSM0nSo&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfEi1rZwbat_eetCl1g1e2IbLEEaWSjK3-BO_WkMJLM-Rw&oe=681CC8E2)\\
\\
![](https://scontent.xx.fbcdn.net/v/t39.8562-6/336009607_1870102080040414_6753977241281150924_n.svg?_nc_cat=103&ccb=1-7&_nc_sid=e280be&_nc_ohc=ZtW4P3kEIE0Q7kNvwGgLPZo&_nc_oc=AdkJC30ShLlYRieGi7gOfmhwEqzpa9eMH3e0gPvO3U1Pb42N59ZoZreVwvG3DSM0nSo&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfEi1rZwbat_eetCl1g1e2IbLEEaWSjK3-BO_WkMJLM-Rw&oe=681CC8E2)](https://twitter.com/aiatmeta/)

[![](https://scontent.xx.fbcdn.net/v/t39.8562-6/336289415_1541032296405649_2165099305308791297_n.svg?_nc_cat=109&ccb=1-7&_nc_sid=e280be&_nc_ohc=eeYi5emVeWgQ7kNvwFRs0-W&_nc_oc=Adn09xeUeFBqi4pwjszCbrueXxFaMX-bkKGW0u7aeV_8cooUeBrnG2xs-ca76NIlsOs&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfGtIPqhBwk3O0xSicEhETbdhdLkWX6M7WYoFDdS2SfqoA&oe=681CF4BB)\\
\\
![](https://scontent.xx.fbcdn.net/v/t39.8562-6/336289415_1541032296405649_2165099305308791297_n.svg?_nc_cat=109&ccb=1-7&_nc_sid=e280be&_nc_ohc=eeYi5emVeWgQ7kNvwFRs0-W&_nc_oc=Adn09xeUeFBqi4pwjszCbrueXxFaMX-bkKGW0u7aeV_8cooUeBrnG2xs-ca76NIlsOs&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfGtIPqhBwk3O0xSicEhETbdhdLkWX6M7WYoFDdS2SfqoA&oe=681CF4BB)](https://www.linkedin.com/showcase/aiatmeta)

[![](https://scontent.xx.fbcdn.net/v/t39.8562-6/335648731_142576991793348_7786819189843639239_n.svg?_nc_cat=108&ccb=1-7&_nc_sid=e280be&_nc_ohc=t6wPNAM7D4sQ7kNvwGlWyB7&_nc_oc=AdnPOBpFgF_Q9smDcLO-AdAodES7ozBYtyw9AgqIqE2zHXSRh6CnY8OfkRincAftHW8&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfHBKuGgd4A1Hwe8mr2zY7kYIqOpzagoNbTBrZFAl5q7sQ&oe=681CD5EE)\\
\\
![](https://scontent.xx.fbcdn.net/v/t39.8562-6/335648731_142576991793348_7786819189843639239_n.svg?_nc_cat=108&ccb=1-7&_nc_sid=e280be&_nc_ohc=t6wPNAM7D4sQ7kNvwGlWyB7&_nc_oc=AdnPOBpFgF_Q9smDcLO-AdAodES7ozBYtyw9AgqIqE2zHXSRh6CnY8OfkRincAftHW8&_nc_zt=14&_nc_ht=scontent.xx&_nc_gid=VUox-ohuYz-2sVjygkJHbQ&oh=00_AfHBKuGgd4A1Hwe8mr2zY7kYIqOpzagoNbTBrZFAl5q7sQ&oe=681CD5EE)](https://www.youtube.com/@aiatmeta)

[iframe](https://fbthirdpartypixel.com/ga-tag/?pixel=G-R3P89RH1FB&__cci=FQAREiIVABkFGAthaS5tZXRhLmNvbQA%3D.ARZs86xMjDauvlqrTAF82dmFsWgBVJTh2rLrYs6i02odylzL)
