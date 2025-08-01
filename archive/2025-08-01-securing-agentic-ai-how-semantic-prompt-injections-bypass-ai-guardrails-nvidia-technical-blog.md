---
date: '2025-08-01'
description: NVIDIA's latest blog highlights the evolving threat of semantic prompt
  injections targeting multimodal AI. As models like Llama 4 implement early fusion
  architectures, integrating text and visual data, traditional input-based security
  measures fail to mitigate risks. Attackers can exploit visual semantics, manipulating
  sequences of images to execute commands or generate code without textual prompts.
  This underscores the urgency for adaptive output filtering and multilayered defenses
  to enhance AI security. Future strategies must focus on understanding cross-modal
  implications and refining defenses to maintain integrity in increasingly autonomous
  AI systems.
link: https://developer.nvidia.com/blog/securing-agentic-ai-how-semantic-prompt-injections-bypass-ai-guardrails/
tags:
- Semantic Prompt Injection
- Agentic AI
- Cybersecurity
- Large Language Models
- Multimodal AI
title: 'Securing Agentic AI: How Semantic Prompt Injections Bypass AI Guardrails ◆
  NVIDIA Technical Blog'
---

[Technical Blog](https://developer.nvidia.com/blog)

[Subscribe](https://developer.nvidia.com/email-signup)

[Related Resources](https://developer.nvidia.com/blog/securing-agentic-ai-how-semantic-prompt-injections-bypass-ai-guardrails/#main-content-end)

[Cybersecurity](https://developer.nvidia.com/blog/category/cybersecurity/)

# Securing Agentic AI: How Semantic Prompt Injections Bypass AI Guardrails

Jul 31, 2025


By [Daniel Teixeira](https://developer.nvidia.com/blog/author/dteixeira/ "Posts by Daniel Teixeira")

+7

Like

[Discuss (0)](https://developer.nvidia.com/blog/securing-agentic-ai-how-semantic-prompt-injections-bypass-ai-guardrails/#entry-content-comments)

![Decorative image.](https://developer-blogs.nvidia.com/wp-content/uploads/2025/07/llm-prompt-injection-1024x576-png.webp)

- [L](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fsecuring-agentic-ai-how-semantic-prompt-injections-bypass-ai-guardrails%2F)
- [T](https://twitter.com/intent/tweet?text=Securing+Agentic+AI%3A+How+Semantic+Prompt+Injections+Bypass+AI+Guardrails+%7C+NVIDIA+Technical+Blog+https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fsecuring-agentic-ai-how-semantic-prompt-injections-bypass-ai-guardrails%2F)
- [F](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fsecuring-agentic-ai-how-semantic-prompt-injections-bypass-ai-guardrails%2F)
- [R](https://www.reddit.com/submit?url=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fsecuring-agentic-ai-how-semantic-prompt-injections-bypass-ai-guardrails%2F&title=Securing+Agentic+AI%3A+How+Semantic+Prompt+Injections+Bypass+AI+Guardrails+%7C+NVIDIA+Technical+Blog)
- [E](mailto:?subject=I%27d%20like%20to%20share%20a%20link%20with%20you&body=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fsecuring-agentic-ai-how-semantic-prompt-injections-bypass-ai-guardrails%2F)

Prompt injection, where adversaries manipulate inputs to make large language models behave in unintended ways, has long posed a threat to AI systems since the earliest days of LLM deployment. While defenders have made progress securing models against text-based attacks, the shift to multimodal and agentic AI is rapidly expanding the attack surface.

This is where red teaming plays a vital role. The NVIDIA [AI Red Team](https://developer.nvidia.com/blog/nvidia-ai-red-team-an-introduction/) proactively simulates real-world attacks to uncover emerging threats in production-grade systems. Their work doesn’t aim to present finalized fixes; rather, it highlights vulnerabilities that require cross-functional solutions, especially in fast-evolving areas like generative and multimodal AI.

In this post, we introduce a new category of multimodal prompt injection that doesn’t rely on natural language. We show how adversaries can use symbolic visual inputs, like emoji-like sequences or rebus puzzles, to compromise agentic systems and evade existing guardrails. These findings underscore the need to shift from input filtering to output-level defenses when securing advanced AI workflows.

## **Introduction: beyond traditional prompt injection**

Since the debut of multimodal models, researchers have experimented with prompt injection techniques targeting external audio or vision modules, often exploiting implementations that convert images to text using optical character recognition (OCR). A common tactic was to embed malicious prompts as text within images, manipulating systems through the text processing pipeline.

Our research takes a different direction, inspired by OpenAI’s [Thinking with images](https://openai.com/index/thinking-with-images/) announcement for the o3 and o4-mini models. OpenAI’s new architecture marked a significant shift: instead of translating images or audio to text, these models convert each modality into fixed-size embedding vectors, concatenate them, and process the sequence in a unified decoder. Audio and visual tokens are handled directly within the model’s core reasoning layers, enabling true cross-modal reasoning without separate audio-to-text or image-to-text pipelines.

This architectural change prompted us to explore new avenues for multimodal prompt injection techniques that don’t depend on hidden textual payloads, but instead use the direct integration of multimodal inputs within the model’s reasoning process.

## **Traditional multimodal prompt injection techniques**

Historically, multimodal prompt injection attacks have exploited the way models process images containing text. Adversaries insert malicious prompts into visual elements, like t-shirts or signage, so that the model interprets this embedded text as executable instructions.

For example, an image of a person wearing a shirt with the text print(“Hello, World”) can be processed by a model, which extracts the text and interprets it as a programming instruction, generating a “Hello, World” program.

_Video 1. A model interprets text on a t-shirt to generate “Hello, World” code_

Guardrails using OCR to find malicious text in images are becoming ineffective. Advanced models, like OpenAI’s o-series, Google Gemini, and Meta Llama 4, now have native visual reasoning, enabling stealthier attacks that bypass text-based detection and require updated defense strategies.

## **Multimodal model evolution: early fusion in Llama 4**

While robust guardrails are reducing the success of traditional prompt injections, our novel approach targets new early fusion architectures. For example, Meta Llama 4 natively integrates text and vision tokens from the input stage, unlike older models. This creates shared representations and enables more natural cross-modal reasoning.

### **How early fusion works**

1. **Parallel input processing**
   - **Text processing**: The user prompt “Describe this image” is tokenized into a sequence of token IDs.
   - **Image processing**: The image is preprocessed (resized, tiled, normalized), passed through a vision encoder, divided into patches, and each patch is embedded and projected into the language model’s embedding space, resulting in continuous image embeddings.
2. **Sequence construction**
   - **A unified sequence is constructed**: tokenized text interleaved with image placeholder tokens (e.g., <\|image\_start\|>, <\|patch\|>, <\|image\_end\|>).
3. **Embedding and fusion**
   - Placeholders are replaced with actual image embeddings; special tokens retain learned embeddings.
4. **Fused sequence**
   - Text and image patch embeddings coexist in a single sequence, mapped to the same dimensional space.
5. **Unified processing**
   - The transformer backbone processes the entire fused sequence, enabling cross-modal attention and reasoning from the earliest layers.

![Pipeline flow includes separate text tokenization and image embedding, followed by sequence construction, where tokens and image patches are merged into a unified sequence. This sequence is jointly embedded and passed to a transformer for multimodal reasoning.](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20210%20140%22%3E%3C/svg%3E)_Figure 1. Llama 4 early fusion pipeline_

This process creates a truly multimodal latent space, where visual and textual semantics are intertwined. For example, an image patch with “STOP” on a sign aligns closely in latent space with the text token “STOP,” allowing the model to reason fluidly across modalities.

Early fusion architectures, such as Llama 4, enabled seamless integration and reasoning across text and images by aligning them in a shared latent space. This opens up new opportunities for cross-modal attacks that do not rely on explicit text.

## **New multimodal prompt injections**

Early fusion enables models to process and interpret both images and text by mapping them into a shared latent space. This creates a novel attack surface where adversaries can now craft sequences of images (e.g., a printer, a person waving, and a globe) to visually encode instructions like “print hello world.”

### **Code injections**

By using semantic alignment between image and text embeddings, attackers can bypass traditional text-based security filters and exploit non-textual inputs to control agentic systems.

#### **“Print Hello World” Image Payload**

![Illustration of a printer, a person waving, and a globe arranged left to right. When interpreted semantically by a multimodal model, this image sequence forms the phrase “print Hello, World” and triggers the generation of the corresponding code without using any textual input.](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201536%201024%22%3E%3C/svg%3E)_Figure 2. Rebus-style visual prompt_

A sequence of images—such as a printer, a person waving, and a globe—can be interpreted by the model as a rebus: “print ‘Hello, world’.” The model deduces the intended meaning and generates the corresponding code, even without explicit text instructions.

_Video 2. Code from semantic image input_

**“Sleep Timer” image payload**

A sequence of images depicting a person sleeping, a dot, and a stopwatch might suggest “sleep timer,” indicating a function to pause execution for a duration.

_Video 3. Model interprets sleep timer prompt_

### **Command injections**

Visual semantics can also be harnessed to execute commands. For example, a cat icon followed by a document icon can be interpreted as the Unix cat command to read a file. Similarly, a trash can and document icon can be interpreted as a file deletion command.

**“Cat File” image payload**

Following the pattern of our previous examples, this payload demonstrates how visual semantics can be harnessed to execute a terminal command to cat (read) a file. The image sequence contains a cat (representing the Unix cat command), a document or file icon.

_Video 4. Visual prompt for cat command_

**“Delete File” image payload**

_Video 5. Model executes file deletion command_

These examples show how models naturally interpret visual semantics and convert them into functional code, even without explicit text instructions. The model’s reasoning steps (“Deciphering image puzzles”) underscore how current architectures are trained to solve such puzzles, as described in OpenAI’s [Thinking with images](https://openai.com/index/thinking-with-images/) post. This drive to excel at reasoning and puzzle solving not only makes these attacks practical but also substantially expands the native multimodal attack surface.

## **Conclusion**

The shift to natively multimodal LLMs marks a major advance in AI capabilities, but also introduces new security challenges. These models reason across text, images, and other modalities in a shared latent space, creating novel opportunities for adversarial manipulation. Semantic prompt injection via symbolic or visual inputs exposes critical gaps in traditional safeguards like OCR, keyword filtering, and content moderation.

To defend against these threats, AI security must evolve. Input filtering alone can’t keep up with the complexity of cross-modal attacks. The focus must move downstream toward output-level controls that rigorously filter, monitor, and, when needed, require explicit confirmation before executing sensitive actions.

**How to Defend Against Multimodal Prompt Injections:**

- **Deploy adaptive output filters:** Evaluate model responses for safety, intent, and downstream impact, especially before they trigger code execution, file access, or system changes.
- **Build layered defenses:** Combine output filtering with runtime monitoring, rate limiting, and rollback mechanisms to detect and contain emerging attacks.
- **Use semantic and cross-modal analysis:** Move beyond static keyword checks. Interpret output meaning across modalities to detect rebus-style or symbolic prompt injections.
- **Continuously tune defenses:** Use red teaming, telemetry, and feedback loops to adapt guardrails as models and attack techniques evolve.

These attacks, from rebus-style “Hello, World” programs to visual file deletion payloads, aren’t theoretical. They’re live demonstrations of how the multimodal attack surface is expanding, especially in agentic systems with tool access or autonomy. Prioritizing output-centric mitigations now is essential to building AI systems that are safe, resilient, and production-ready. For a hands-on look at these and related threats, explore the [Exploring Adversarial Machine Learning](https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-DS-03+V1) NVIDIA Deep Learning Institute course. To dive deeper into real-world red teaming insights and techniques for AI systems, check out the [related NVIDIA Technical Blog posts](https://developer.nvidia.com/blog/tag/ai-red-team/).

## Related resources

- GTC session: [Bypassing LLM Security and Safety Guardrails](https://www.nvidia.com/gtc/session-catalog/?tab.catalogallsessionstab=1700692987788001F1cG&search=P73562&ncid=em-even-124008-vt33-23spring#/)
- GTC session: [Advanced LLM App Evaluation: Building Real-Time Guardrails for Real-World LLM Risk Mitigation](https://www.nvidia.com/gtc/session-catalog/?tab.catalogallsessionstab=1700692987788001F1cG&search=S71692&ncid=em-even-124008-vt33-23spring#/)
- GTC session: [Embeddings are Limiting AI Agents: How Codeium used NVIDIA GPUs at Scale During Inference to Improve Retrieval Current](https://www.nvidia.com/gtc/session-catalog/?tab.catalogallsessionstab=1700692987788001F1cG&search=S71317&ncid=em-even-124008-vt33-23spring#/)
- NGC Containers: [NVIDIA Retrieval QA E5 Embedding v5](https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nv-embedqa-e5-v5?ncid=em-nurt-245273-vt33)
- NGC Containers: [NVIDIA Retrieval QA Mistral 7B Embedding v2](https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nv-embedqa-mistral-7b-v2?ncid=em-nurt-245273-vt33)
- Webinar: [Accelerating Contact Center AI Workflows with NVIDIA AI Enterprise](https://gateway.on24.com/wcc/eh/1407606/lp/5008538/?embedUrl=https://www.nvidia.com/en-us/about-nvidia/webinar-portal/)

[Discuss (0)](https://developer.nvidia.com/blog/securing-agentic-ai-how-semantic-prompt-injections-bypass-ai-guardrails/#entry-content-comments)

+7

Like

## Tags

[Cybersecurity](https://developer.nvidia.com/blog/category/cybersecurity/) \| [Generative AI](https://developer.nvidia.com/blog/category/generative-ai/) \| [General](https://developer.nvidia.com/blog/recent-posts/?industry=General) \| [Intermediate Technical](https://developer.nvidia.com/blog/recent-posts/?learning_levels=Intermediate+Technical) \| [Deep dive](https://developer.nvidia.com/blog/recent-posts/?content_types=Deep+dive) \| [AI Red Team](https://developer.nvidia.com/blog/tag/ai-red-team/) \| [DLI](https://developer.nvidia.com/blog/tag/dli/)

## About the Authors

![Avatar photo](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20131%20131%22%3E%3C/svg%3E)

**About Daniel Teixeira**


Daniel Teixeira is a senior offensive security researcher and Red Team operator at NVIDIA, bringing over a decade of experience in penetration testing, vulnerability research, and red teaming. His research interests include adversary simulation, adversarial machine learning, agentic AI systems, MLOps, and LLMOps.




[View all posts by Daniel Teixeira](https://developer.nvidia.com/blog/author/dteixeira/)

## Comments

- [![](https://developer-blogs.nvidia.com/wp-content/uploads/2025/07/siggraph25-special-address-email-banner-1360x180-1.png)](https://www.nvidia.com/en-us/events/siggraph/?nvid=nv-int-bnr-463583)

- [L](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fsecuring-agentic-ai-how-semantic-prompt-injections-bypass-ai-guardrails%2F)
- [T](https://twitter.com/intent/tweet?text=Securing+Agentic+AI%3A+How+Semantic+Prompt+Injections+Bypass+AI+Guardrails+%7C+NVIDIA+Technical+Blog+https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fsecuring-agentic-ai-how-semantic-prompt-injections-bypass-ai-guardrails%2F)
- [F](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fsecuring-agentic-ai-how-semantic-prompt-injections-bypass-ai-guardrails%2F)
- [R](https://www.reddit.com/submit?url=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fsecuring-agentic-ai-how-semantic-prompt-injections-bypass-ai-guardrails%2F&title=Securing+Agentic+AI%3A+How+Semantic+Prompt+Injections+Bypass+AI+Guardrails+%7C+NVIDIA+Technical+Blog)
- [E](mailto:?subject=I%27d%20like%20to%20share%20a%20link%20with%20you&body=https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fsecuring-agentic-ai-how-semantic-prompt-injections-bypass-ai-guardrails%2F)

- [Join](https://developer.nvidia.com/login)
