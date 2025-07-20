---
title: "New Threat Vector: Prompt Injection at the Raw Signal Level "
tags:
   - Deepfake Detection
   - Cybersecurity
   - Machine Learning
   - Voice AI
   - Speech Processing
link: https://gradientflow.substack.com/p/new-threat-vector-prompt-injection
date: 2025-07-20
summary: "The Rise of Voice AI presents new security challenges, notably with prompt injection attacks at the signal level, as voice synthesis technologies advance. Current systems predominantly use a cascading model for speech generation, leading to vulnerabilities such as impersonation and social engineering. Attack vectors will evolve as the industry shifts to end-to-end audio models, necessitating an innovative approach to security. Enterprises must integrate defenses during design phases, focusing on continuous updates and audio-specific protections to mitigate threats posed by increasingly sophisticated voice agents. Voice security is critical even for organizations not utilizing voice technology internally."
---

[![Gradient Flow](https://substackcdn.com/image/fetch/$s_!JgYc!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F42dc987e-4b38-4003-b259-4283ad63d445_256x256.png)](https://gradientflow.substack.com/)

# [![Gradient Flow](https://substackcdn.com/image/fetch/$s_!Khuo!,e_trim:10:white/e_trim:10:transparent/h_72,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa19659ab-55ef-4ffb-bc23-0c552391257a_953x185.jpeg)](https://gradientflow.substack.com/)

SubscribeSign in

![User's avatar](https://substackcdn.com/image/fetch/$s_!HMMg!,w_64,h_64,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe5db607c-0a85-4d98-8f35-7aada811bc0c_253x115.jpeg)

Discover more from Gradient Flow

Put data, machine learning, and AI to work.

Subscribe

By subscribing, I agree to Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

Already have an account? Sign in

# New Threat Vector: Prompt Injection at the Raw Signal Level

[Ben Lorica 罗瑞卡](https://substack.com/@gradientflow)

Jun 24, 2025

3

[View comments (0)](https://gradientflow.substack.com/p/new-threat-vector-prompt-injection/comments)

3

Share

[![](https://substackcdn.com/image/fetch/$s_!Qpug!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F0f732fb8-bcb3-47bb-93e0-cf2c6c0653c5_1100x220.png)](https://gradientflow.com/newsletter/)

**[Subscribe](https://gradientflow.substack.com/subscribe) • [Previous Issues](https://gradientflow.substack.com/)**

# **The Enterprise Guide to Voice AI Threat Modeling and Defense**

Voice interfaces have become a routine feature of modern life, from home assistants to automotive controls and automated customer service. Yet, within the AI community, the focus on large language and visual models has overshadowed the field of voice. In my experience, for every AI team experimenting with voice or audio models, there are dozens focused on computer vision and hundreds building apps that rely on text-based LLMs. Consequently, the rapid advances in core voice technologies—such as speech-to-text, text-to-speech, and generative audio—have largely gone underappreciated, creating a significant and growing vulnerability.

That complacency is costly. Fraudsters have already used synthetic voices to [trick a British engineering firm](https://www.weforum.org/stories/2025/02/deepfake-ai-cybercrime-arup/) into wiring away tens of millions, to [impersonate a cybersecurity chief executive](https://techcrunch.com/2024/10/28/wiz-ceo-says-company-was-targeted-with-deepfake-attack-that-used-his-voice/), and even to [spoof a senior White House adviser](https://www.theguardian.com/us-news/2025/may/30/susie-wiles-trump-chief-of-staff-impersonation). As voice synthesis approaches real-time fidelity, every new customer-service bot or multilingual meeting assistant widens the attack surface. The heavily edited conversation that follows with [Yishay Carmiel](https://www.linkedin.com/in/yishay-carmiel-6469482/) and [Roy Zanbel](https://www.linkedin.com/in/royzanbel/) of **[Apollo Defend](https://www.apollodefend.com/)**, provides a map of the technology's capabilities, the threats it poses, and the urgent need for a new class of defenses.

* * *

**Gradient Flow is a reader-supported publication. To receive new posts and support our work, consider becoming a free or paid subscriber ⭐️**

Subscribe

* * *

#### **The State of Voice AI and Foundation Models**

**How does the current state of voice foundation models compare to the large language model (LLM) space?**

Voice AI is not yet as mature as the LLM space, where a few dominant foundation models are used off-the-shelf. However, the industry is moving in that direction. Currently, most voice applications use a "cascading model" with three separate steps:

1. **Speech-to-Text (ASR):** OpenAI's [Whisper](https://github.com/openai/whisper) is the de facto open-source foundation model that most developers use or build upon

2. **Language Processing:** An LLM processes the transcribed text

3. **Text-to-Speech (TTS):** The LLM's text output is converted back into speech


The TTS space is more fragmented, with commercial options like ElevenLabs and various open-source models. The next evolution is the move to end-to-end "speech-to-speech" or "audio LLM" models that treat speech as both input and output, using internal token representations instead of converting to text.

**What foundation models are available from major players and international sources?**

Beyond Whisper, the landscape includes:

- **Amazon:** Recently released [Amazon Nova](https://aws.amazon.com/ai/generative-ai/nova/speech/) for speech-to-speech

- **Meta:** Working on [VoiceBox](https://ai.meta.com/blog/voicebox-generative-ai-model-speech/) and [AudioBox](https://ai.meta.com/blog/audiobox-generating-audio-voice-natural-language-prompts/) for speech synthesis; rumors suggest an upcoming "Voice Llama" for speech-to-speech tasks

- **Google:** Demonstrated [near real-time translation systems](https://www.youtube.com/watch?v=ujjAplVydhg)

- **Chinese companies:** Models like [CosyVoice](https://github.com/FunAudioLLM/CosyVoice) for speech synthesis and voice conversion, AudioLabs from StepFunction, and initiatives from [Alibaba](https://www.alibabacloud.com/en/product/intelligent-speech-interaction?_p_lc=1) and [Baidu](https://intl.cloud.baidu.com/product/speech.html)


While these indicate rapid global innovation, most are not yet widely available to general developers like LLMs are.

[![](https://substackcdn.com/image/fetch/$s_!GQta!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd04802c-9e81-4ed0-a875-90b1c42676c8_1796x916.jpeg)](https://substackcdn.com/image/fetch/$s_!GQta!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd04802c-9e81-4ed0-a875-90b1c42676c8_1796x916.jpeg)

**Is real-time** _**speech-to-speech**_ **(speech-in, speech-out) technology generally available to developers?**

Not yet. While companies like [Apollo Defend](https://www.apollodefend.com/) have demonstrated this capability, it remains largely proprietary. Most current architectures still rely on cascading through text. The "holy grail" of pure speech-to-speech processing is coming but isn't generally available to developers today in the way LLMs are.

#### **Technical Breakthroughs and Capabilities**

**What technical advances have enabled current voice AI applications?**

Major improvements include:

- **Hyper-realistic speech synthesis:** Modern TTS can generate highly realistic, expressive, and conversational human-like speech, moving far beyond robotic voices

- **Near real-time processing capabilities:** Essential for creating seamless conversational agents

- **Broad language support:** While English leads, foundation models are rapidly improving support for many languages

- **Few-shot voice cloning:** Creating high-quality voice clones with [just 5-10 seconds](https://www.resemble.ai/voice-cloning/#:~:text=Rapid%20Voice%20Cloning,that's%20immediately%20ready%20to%20use.) of clean audio


**How close are we to fully human-like AI speech synthesis?**

For simple reading tasks (like article summarization), current models perform excellently. Complex, fully conversational, multi-turn dialogue remains more challenging but is improving rapidly. The technology can now capture subtle nuances of a person's accent and tone, even for non-native speakers.

#### **Voice Security Threats and Attack Vectors**

**What makes voice a unique attack vector compared to text?**

Voice carries a unique biometric fingerprint. Unlike writing style which can be mimicked, your voice is uniquely yours. This enables:

- Bypassing voice-based biometric security systems

- Highly convincing impersonation attacks

- Real-time voice agents that can interact via phone or video calls

- Advanced social engineering and identity theft at scale


**How accessible are voice cloning tools to non-experts?**

The barrier to entry is practically zero. Anyone with a computer and internet access can find YouTube tutorials using open-source tools or readily available services. All that's needed is a short, clean audio sample—often easily found on YouTube, podcasts, or social media—to create a functional clone. Even "script kiddies" can generate convincing clones.

**What are the main threat vectors developers need to consider?**

Attack vectors can be categorized by attacker knowledge:

- **White-box attacks:** Attacker knows the model architecture and weights (highly vulnerable)

- **Gray-box attacks:** Attacker has partial knowledge, like assuming a Conformer-based architecture

- **Black-box attacks:** No knowledge of internal workings (most difficult to execute)


Attack methods include:

- **Text-to-speech attacks:** Generating synthetic speech using cloned voices

- **Voice conversion attacks:** Real-time transformation of one voice to another

- **Voice agents:** Autonomous agents conducting conversations while impersonating individuals


[![](https://substackcdn.com/image/fetch/$s_!XoMY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F925c9029-18ed-4415-b0f8-1deb8ac325a8_1684x984.jpeg)](https://substackcdn.com/image/fetch/$s_!XoMY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F925c9029-18ed-4415-b0f8-1deb8ac325a8_1684x984.jpeg)

**How sophisticated are voice-based attacks becoming?**

Attackers can now deploy voice agents at scale to perform automated attacks on large numbers of people. These agents can make fake calls, impersonate specific individuals, and conduct social engineering attacks without human intervention—potentially extracting credentials, social security numbers, or other sensitive information.

#### **Defense Mechanisms and Detection**

**How effective are current deepfake voice detectors?**

It's a constant cat-and-mouse game. Effectiveness depends on:

- Whether the detector has been trained on recent synthesis models

- The type of attack (text-to-speech vs. voice conversion)

- The sophistication of the attacker


Detectors trained on older synthetic voices may not catch content from the latest models. A detection model even 12-18 months old may be easily bypassed, making continuous adaptation essential.

**How does anti-voice-cloning technology work?**

Advanced anti-cloning involves real-time voice anonymization. These systems process speech and output a new audio stream that:

- Preserves key characteristics (cadence, intonation) for natural human perception

- Alters the underlying biometric fingerprint

- Cannot be reverse-engineered to identify the original speaker

- Makes the audio useless for training cloning models


This is a proactive defense and cannot retroactively protect already-public audio.

**Can these protections help public figures with existing recordings?**

Unfortunately, no. Existing recordings can't be retroactively protected. For public figures with extensive audio exposure, deepfake detection becomes the more viable defense mechanism rather than prevention.

#### **Enterprise Adoption and Implementation**

**Who is currently adopting voice security technologies?**

Early adopters are primarily in defense sectors and government agencies with mission-critical applications. These organizations face sophisticated adversaries and have more to lose from voice-based attacks. They're implementing capabilities like real-time voice protection, deepfake detection, and anti-voice-cloning safeguards.

**When will mainstream enterprises need voice security?**

The timeline has accelerated from 12-18 months to 6-12 months due to rapid AI innovation. Currently, most CISOs are focused on LLM security and haven't fully addressed voice threats. As high-profile attacks increase and companies deploy their own voice agents, CISOs will be forced to prioritize it.

[![](https://substackcdn.com/image/fetch/$s_!4csy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b1e6b2a-c8ee-4d96-a78e-9a6f267a0e96_1052x1028.jpeg)](https://substackcdn.com/image/fetch/$s_!4csy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b1e6b2a-c8ee-4d96-a78e-9a6f267a0e96_1052x1028.jpeg)

**Do companies need voice security even if they're not using voice AI?**

Absolutely. Voice AI can be weaponized against organizations through social engineering attacks regardless of whether the company uses voice technology internally. The risk exists for any organization whose employees or customers might receive phone calls. Protection is needed against external threats, not just for securing internal voice applications.

**What lessons can be drawn from email security evolution?**

Just as email introduced new attack surfaces like phishing, voice AI will require layered defenses including:

- Spam filtering equivalents for voice

- Verification protocols adapted for voice interactions

- Anomaly detection systems

- User education about voice-based threats


#### **Future Outlook and Implications**

**What's the next major shift in voice AI foundation models?**

The industry is moving toward end-to-end speech-to-speech models (audio LLMs) where everything happens through tokens rather than text. This eliminates the intermediate text step, enabling more fluid and natural voice AI capabilities while introducing entirely new security challenges.

[![](https://substackcdn.com/image/fetch/$s_!S7DG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F11c32fec-3ba3-416e-b76e-ce05b7a6ec2a_1780x754.jpeg)](https://substackcdn.com/image/fetch/$s_!S7DG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F11c32fec-3ba3-416e-b76e-ce05b7a6ec2a_1780x754.jpeg)

**How will this shift impact security requirements for AI development teams?**

Every attack vector currently used against text-based LLMs—prompt injection, jailbreaking, privacy attacks—will migrate directly to the audio layer. **Since there's no accessible text layer to inspect, these attacks must be executed and defended against at the raw signal level**. This means:

- Security must be designed in from the start, not added as an afterthought

- Teams need audio-specific defenses against prompt injection at the signal level

- A new field of "audio LLM security" will become critical

- Traditional text-based security tools won't be sufficient


**How real is the threat of malicious voice agents today?**

The threat is immediate and happening now. The building blocks are all commercially available:

- High-quality text-to-speech

- Powerful LLMs for conversational logic

- Scalable infrastructure for deployment


Companies already deploy voice agents for customer service, sales, and recruiting. Attackers can repurpose this exact same technology to create agents that impersonate trusted individuals and conduct sophisticated attacks at scale. This makes it an urgent threat for all enterprises, not just those building with voice AI.

* * *

Subscribe

* * *

**What should AI development teams prioritize when building voice applications?**

Teams should:

- Implement voice security from the design phase, not as an afterthought

- Consider both internal use cases and external threat vectors

- Prepare for the transition to speech-to-speech architectures

- Understand that voice AI introduces unique biometric risks beyond traditional cybersecurity

- Plan for continuous updates to detection systems as offensive capabilities evolve

- Consider voice anonymization for sensitive applications

- Build in authentication mechanisms that don't rely solely on voice recognition


* * *

_**[Ben Lorica](https://gradientflow.com/disclosure/)** edits the [Gradient Flow newsletter](https://gradientflow.substack.com/). He helps organize the **[AI Conference](https://aiconference.com/?utm_source=gradientflow&utm_medium=newsletter)**, the **[AI Agent Conference](https://agentconference.com/?utm_source=gradientflow&utm_medium=newsletter)**, the **[Applied AI Summit](https://appliedaisummit.org/)**, while also serving as the Strategic Content Chair for AI at the **[Linux Foundation](https://events.linuxfoundation.org/)**. He is the host of [the Data Exchange podcast](https://thedataexchange.media/). You can follow him on [Linkedin](https://www.linkedin.com/in/benlorica/), [Mastodon](https://indieweb.social/@bigdata), [Reddit](https://www.reddit.com/r/GradientFlow/), [Bluesky](https://bsky.app/profile/gradientflow.com), [YouTube](https://www.youtube.com/c/GradientFlow), or [TikTok](https://www.tiktok.com/@gradientflow). This newsletter is produced by [Gradient Flow](https://gradientflow.com/blog/)._

* * *

#### Subscribe to Gradient Flow

By Ben Lorica 罗瑞卡

Put data, machine learning, and AI to work.

Subscribe

By subscribing, I agree to Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

[![Jeff's avatar](https://substackcdn.com/image/fetch/$s_!HVcF!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4ff80399-b831-4fe6-b77b-0fbabb269a16_144x144.png)](https://substack.com/profile/18454268-jeff)

[![Ben Lorica 罗瑞卡's avatar](https://substackcdn.com/image/fetch/$s_!HMMg!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe5db607c-0a85-4d98-8f35-7aada811bc0c_253x115.jpeg)](https://substack.com/profile/969577-ben-lorica)

3 Likes∙

[3 Restacks](https://substack.com/note/p-165967174/restacks?utm_source=substack&utm_content=facepile-restacks)

3

[View comments (0)](https://gradientflow.substack.com/p/new-threat-vector-prompt-injection/comments)

3

Share

PreviousNext

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

TopLatestDiscussions

[Best Practices in Retrieval Augmented Generation](https://gradientflow.substack.com/p/best-practices-in-retrieval-augmented)

[Subscribe • Previous Issues](https://gradientflow.substack.com/p/best-practices-in-retrieval-augmented)

Oct 19, 2023•
[Ben Lorica 罗瑞卡](https://substack.com/@gradientflow)

31

[View comments (0)](https://gradientflow.substack.com/p/best-practices-in-retrieval-augmented/comments)

![](https://substackcdn.com/image/fetch/$s_!T1R_!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe9ee6310-47da-4661-958c-a2bdc069c2b7_1464x855.png)

[Building LLM-powered Apps: What You Need to Know](https://gradientflow.substack.com/p/building-llm-powered-apps-what-you)

[Subscribe • Previous Issues](https://gradientflow.substack.com/p/building-llm-powered-apps-what-you)

Apr 6, 2023•
[Ben Lorica 罗瑞卡](https://substack.com/@gradientflow)

29

[View comments (0)](https://gradientflow.substack.com/p/building-llm-powered-apps-what-you/comments)

![](https://substackcdn.com/image/fetch/$s_!ak-7!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa31b9678-ad7e-49db-a78b-1e3291f7a340_2501x1886.png)

[LLM Inference Hardware: Emerging from Nvidia's Shadow](https://gradientflow.substack.com/p/llm-inference-hardware-emerging-from)

[Subscribe • Previous Issues](https://gradientflow.substack.com/p/llm-inference-hardware-emerging-from)

Jan 11, 2024•
[Ben Lorica 罗瑞卡](https://substack.com/@gradientflow)

58

[View comments (0)](https://gradientflow.substack.com/p/llm-inference-hardware-emerging-from/comments)

![](https://substackcdn.com/image/fetch/$s_!szu-!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff94258e-b231-4bc8-9fc8-941652579e24_1920x1080.jpeg)

See all

Ready for more?

Subscribe
