---
date: '2025-08-13'
description: At Black Hat 2025, significant advancements in AI utilization for cybersecurity
  were confirmed. Key discussions highlighted robust AI applications like Sublime
  Security's Autonomous Detection Engineer, streamlining SOC operations by reducing
  alert handling time significantly. The transition to offensive security models through
  AI was underscored, marking a paradigm shift from detection-focused strategies to
  proactive offensive capabilities. Additionally, the exploration of digital twins
  for security simulations demonstrated potential for real-time, dynamic vulnerability
  assessments. The conference emphasized the maturation of AI in operational security,
  potentially accelerating the adoption of further AI use cases in the sector.
link: https://dannguyenhuu.substack.com/p/black-hat-2025-security-catalyst
tags:
- BlackHat2025
- AI
- digitaltwins
- cloudcomputing
- cybersecurity
title: 'Black Hat 2025: Security Catalyst Recap - by Dan Nguyen-Huu'
---

[![Founder Catalyst](https://substackcdn.com/image/fetch/$s_!-96Q!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F53ccedcc-7db7-45b4-a945-e215df8f5d19_800x800.png)](https://dannguyenhuu.substack.com/)

# [![Founder Catalyst](https://substackcdn.com/image/fetch/$s_!JsI8!,e_trim:10:white/e_trim:10:transparent/h_72,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7232d5c-f6b7-49e7-8ae3-5bda499e86ce_500x96.gif)](https://dannguyenhuu.substack.com/)

SubscribeSign in

![User's avatar](https://substackcdn.com/image/fetch/$s_!iGor!,w_64,h_64,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F401c2fc7-08e7-4291-b79a-7f67d68440b6_1044x1218.jpeg)

Discover more from Founder Catalyst

Seeding ideas, startup concepts, and compelling events for founders and future founders in cloud, AI, and cybersecurity.

Over 1,000 subscribers

Subscribe

By subscribing, I agree to Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

Already have an account? Sign in

[Security Catalyst](https://dannguyenhuu.substack.com/s/security-catalyst/?utm_source=substack&utm_medium=menu)

# Black Hat 2025: Security Catalyst Recap

### In Las Vegas, GPUs are not the only thing overheating. So are its hackers.

[![Dan Nguyen-Huu's avatar](https://substackcdn.com/image/fetch/$s_!iGor!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F401c2fc7-08e7-4291-b79a-7f67d68440b6_1044x1218.jpeg)](https://substack.com/@dannguyenhuu)

[Dan Nguyen-Huu](https://substack.com/@dannguyenhuu)

Aug 13, 2025

7

[2](https://dannguyenhuu.substack.com/p/black-hat-2025-security-catalyst/comments)

Share

[![](https://substackcdn.com/image/fetch/$s_!4Eyq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe6885239-5843-46fc-b33d-dcc86dddf1a4_2048x1536.jpeg)](https://substackcdn.com/image/fetch/$s_!4Eyq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe6885239-5843-46fc-b33d-dcc86dddf1a4_2048x1536.jpeg) Decibel Vibes and Cocktails Happy Hour

Las Vegas in August is always intense, but this year the real heat came from breakthroughs not just in cyber tools, but in how we think about offense, defense, simulation, identity, and human sustainability under pressure all under the large cloud cover of AI (obviously). The [Decibel](http://decibel.vc/) team was out in full force hosting a series of events from the [Vibes & Cocktails happy hour](https://www.linkedin.com/posts/jonsakoda_it-was-great-to-take-a-break-from-the-109-activity-7359601490073698306-jT9x?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAO9oeEBhUic4AhdPOZY6irsjPr5IOduplc) with the awesome [Mike Privette](https://www.linkedin.com/in/mikeprivette/) from [Return on Security](https://www.returnonsecurity.com/), a [Women in Cyber brunch](https://www.linkedin.com/posts/lauren-ipsen-6a5a84113_blackhat2025-ugcPost-7359669353866301440-Qpez?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAO9oeEBhUic4AhdPOZY6irsjPr5IOduplc) and our usual Founder Oasis suite where founders can hang out and take a breather from the craziness of the BlackHat Expo. Over these glorious few days inside the Mandalay Bay hotel, here are some of the biggest topics and themes that were discussed:

* * *

### **The First AI-in-Cyber Use Case has matured: Toil Reduction**

It's taken a lot of hype cycles, but we've finally hit a clear, repeatable AI use case in cybersecurity: getting rid of soul-crushing toil. [Sublime Security's ADE](https://docs.sublime.security/docs/ade-autonomous-detection-engineer) (Autonomous Detection Engineer) is a prime example: automating the grunt work of detection engineering so humans can focus on higher-order problems. Dropzone AI is doing the same for the SOC, taking Tier-1 alert handling and triage from hours to minutes without sacrificing quality. The value is obvious because the before/after delta is so stark. No philosophical debates about "will it work". It's already working.

The timeline tells an important story about enterprise AI adoption. [Edward Wu](https://www.linkedin.com/in/edwardxwu/), founder of [Dropzone AI](https://www.dropzone.ai/), first introduced the concept of investigating alerts using LLMs at our Founder Oasis at RSA in March of 2023, only a few months after ChatGPT was released. Dropzone was born in August 2023, and while he long proved that its AI was effective for alert investigations, the human acceptance, trust, and willingness to delegate alerts and reduce toil took until recently to fully materialize. AI SOC dominated every conversation on the expo floor at Black Hat 2025. For me, this marks the moment we can officially declare victory on AI-powered toil reduction in security. What was once a pilot in many enterprises has become a mainstream operational reality.

This raises a critical question for the broader AI-in-security landscape: now that we've moved past the foundational debate of whether AI works in security contexts, **how much faster will we adopt other AI use cases?** The answer likely depends on whether those use cases can demonstrate the same stark before/after delta that made toil reduction so compelling. With trust barriers lowered and operational patterns established, I think the adoption curve for subsequent AI security applications should accelerate significantly

[![](https://substackcdn.com/image/fetch/$s_!PXQt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5b9b549-d334-4b0e-a630-7be0fe2585cc_879x434.png)](https://substackcdn.com/image/fetch/$s_!PXQt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5b9b549-d334-4b0e-a630-7be0fe2585cc_879x434.png)

### **Proudly Offensive — Deterrence in the AI Era**

After this year’s RSA, I wrote an article about "Proudly Offensive", an idea on how in an AI world, security insights increasingly come from offense, not just from watching and waiting. Historically, security posture leaned heavily on detection, with just enough response to feel proactive. Organizations built their security programs around the assumption that visibility and monitoring would give them the edge they needed.

But AI fundamentally changes this calculus. We're already seeing operational proof: startups using AI agents to dominate bug bounty programs, and more concerning, full end-to-end data exfiltrations that run autonomously from initial access to final payload delivery. The offensive capabilities of AI have moved from theoretical to operational.

Bug bounties are a useful proving ground. They demonstrate that AI can find vulnerabilities faster than humans and execute complex attack chains with minimal human oversight. But the real question is whether we can build offensive cyber capabilities that matter when geopolitical tensions escalate. What happens when the call comes in: "We need you to help"?

This is where deterrence becomes front and center. The organizations and nations that figure out how to weaponize AI for cyber operations will have strategic leverage. We're seeing early signals in American defense investments: companies like Palantir and Anduril building AI-powered capabilities at scale, not for corporate penetration testing, but for real-world adversarial engagement.

This shift is technical, political, and extisential. In an AI-driven threat landscape, deterrence requires demonstrable offensive capability. The willingness to develop, deploy, and when necessary, unleash AI-powered cyber operations will define which nations maintain strategic advantage in the coming decade. American dynamism built the internet, scaled cloud computing, and created the AI models powering this revolution.

The next chapter won't just reward those who can defend better, it will reward those who can project power through AI when called upon to do so.

[![](https://substackcdn.com/image/fetch/$s_!jsDl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d046f1f-b58e-433c-b98a-177b5ee4b1d1_889x669.png)](https://substackcdn.com/image/fetch/$s_!jsDl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d046f1f-b58e-433c-b98a-177b5ee4b1d1_889x669.png)

### **Simulation Is All You Need (…Almost)**

One of the more interesting threads was the growing role of digital twins in cyber. Enterprises are interested in building high-fidelity replicas of systems and networks to safely run security experiments, train AI models, and test defenses. [This Dark Reading piece on this is worth a read.](https://www.darkreading.com/endpoint-security/digital-twins-bring-simulated-security-real-world) Today, these simulations excel at controlled, discrete scenarios perfect for training or red-team-blue-team exercises. But the leap to truly continuous, real-time "mirror worlds" of live enterprise environments is still constrained by data freshness, fidelity, and cost.

The most compelling advancement is how these twins are evolving beyond simple network topology modeling to capture dynamic interactions between applications, cascading effects of component failures, and environmental factors that influence security posture. [Google shared the actual complexity required in their approach](https://cloud.google.com/blog/products/identity-security/how-to-build-a-digital-twin-to-boost-resilience): real-time data streams, comprehensive monitoring capabilities, and computational power to model both normal operations and adversarial scenarios simultaneously.

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/GC---Chart---Digital-twin_1.max-2200x2200.jpg](https://substackcdn.com/image/fetch/$s_!HHLx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3075793f-d624-47d7-ab23-826fd34554d3_2200x963.jpeg)](https://substackcdn.com/image/fetch/$s_!HHLx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3075793f-d624-47d7-ab23-826fd34554d3_2200x963.jpeg) https://cloud.google.com/blog/products/identity-security/how-to-build-a-digital-twin-to-boost-resilience

The next evolution will likely involve AI agents operating within these simulated environments. While today's digital twins rely on human red teams manually probing for weaknesses, the future points toward autonomous agents that could continuously explore attack paths, test defensive responses, and discover novel vulnerability combinations at machine speed. We're not there yet, but the foundation is being built.

This sort of rehearsal logic combined with operationalized threat intel (like GLACIAL PANDA's long-duration persistence) can let defenders explore edge cases and policy effectiveness before reality does. It's a cyber range that no longer approximates, but lets you fight today's adversary with your own specific blueprint.

* * *

### Other Blackhat Thoughts

**Social Engineering - Phishing, Vishing, really all the -ishings**

The narrative is changing from phishing campaigns to quantifying and modeling human risk in real-time. The old security awareness training model of quarterly compliance checkboxes is dead. In its place, we're seeing human risk management emerge as a control layer that feeds behavioral telemetry into identity systems, conditional access policies, and even insurance underwriting ( [I wrote about this recently!](https://dannguyenhuu.substack.com/p/welcome-to-human-risk-university)). According to Crowdstrike, “Vishing attacks increased 442% from the first to the second half of 2024 and the number of vishing attacks in the first half of 2025 have already exceeded the total number seen in 2024.”

This means that authentication must evolve beyond static credentials to dynamic behavioral baselines and step-up validation that adapts to the sophistication of AI-driven social engineering. The threat is substantial and requires a different approach ( [See Push’s Phishing Detection Evasion Techniques Matrix](https://pushsecurity.com/news/pr-20250806-push-security-launches-phishing-detection-evasion-techniques-matrix)) now that adversaries can clone voices or generate convincing deepfakes in real-time that adapt mid-conversation to bypass detection systems and human intuition alike.

[![](https://substackcdn.com/image/fetch/$s_!md3o!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd1fb8918-8bbb-48f8-ad88-a0022597ccb8_624x637.png)](https://substackcdn.com/image/fetch/$s_!md3o!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd1fb8918-8bbb-48f8-ad88-a0022597ccb8_624x637.png)

**Security for AI**

Acquisitions continued this year. [Protect AI’s acquisition](https://www.paloaltonetworks.com/company/press/2025/palo-alto-networks-completes-acquisition-of-protect-ai) was announced during RSA and SentinelOne announced its intent to [acquire Prompt Security](https://www.sentinelone.com/press/sentinelone-to-acquire-prompt-security-to-advance-genai-security/) at the start of Black Hat. This reminds me of [Evident.io’s acquisition](https://investors.paloaltonetworks.com/news-releases/news-release-details/palo-alto-networks-announces-intent-acquire-evidentio) in the early cloud days. The vendors getting acquired today are the ones creating the security controls that make AI deployment viable at enterprise scale. In the past year, solutions have moved from simple model governance to AI security platforms that can detect prompt injection, monitor model behavior drift, and protect training data pipelines. But the question is whether or not this is the end game solution to Security for AI since we don’t even know the full attack surface yet.

**From Application Security to Product Security**

There's a subtle but important shift happening in how organizations think about security ownership. Traditional AppSec focused on finding vulnerabilities in code. Product Security embeds security thinking into the entire product lifecycle: from design decisions to feature rollouts to customer-facing security controls. This isn't just semantic evolution; it's organizational. Product Security teams report to product leadership, not just security leadership, and they're measured on customer outcomes, not just vulnerability counts. AI companies are attacking this problem at different stages: [Prime Security](https://www.primesec.ai/) (this year's Black Hat Startup Champion) focuses on design-stage risk analysis before code is written, making the call that security needs to be woven into the product development process itself.

### **Final Thought**

Black Hat 2025 made it clear: AI in security is no longer just a thought experiment, it’s operational, shaping how we reduce toil, test defenses, and even think about deterrence. From the expo floor to our own events, the energy, ideas, and debates reminded me why this community is so special. Huge thanks to all the security practitioners who joined us, and to our friends across the Decibel family and beyond; it was truly great to catch up! Looking forward to seeing you all again soon…ideally somewhere with a milder climate.

* * *

[![](https://substackcdn.com/image/fetch/$s_!WhdE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2d7c4c8-4be2-4df2-a833-546fdbeccaeb_831x532.png)](https://substackcdn.com/image/fetch/$s_!WhdE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2d7c4c8-4be2-4df2-a833-546fdbeccaeb_831x532.png)

PS: A big shoutout to my good friend [Sean Sun](https://www.linkedin.com/in/seanqsun/) (founder of [Miscreants](https://www.miscreants.com/)) for hosting an incredible (and much needed off strip) dinner with so many friends, teachers and creators in the security community that I have admired for a long time as I have been a student of the security industry.

* * *

#### Subscribe to Founder Catalyst

By Dan Nguyen-Huu · Launched 2 years ago

Seeding ideas, startup concepts, and compelling events for founders and future founders in cloud, AI, and cybersecurity.

Subscribe

By subscribing, I agree to Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

[![Tanya D's avatar](https://substackcdn.com/image/fetch/$s_!moEJ!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc0ad0f67-1bf9-40ea-8f5d-f1318de22b00_1178x1179.jpeg)](https://substack.com/profile/6568381-tanya-d)

[![Robby's avatar](https://substackcdn.com/image/fetch/$s_!RTI8!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd343fdeb-02ca-49c1-8dce-debf5aa07e38_966x966.png)](https://substack.com/profile/101020040-robby)

[![Jess Leão's avatar](https://substackcdn.com/image/fetch/$s_!Q3Ax!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a85e302-c2d3-4bee-a3fb-c230924fc243_4275x4275.jpeg)](https://substack.com/profile/172537544-jess-leao)

[![Damien Lewke's avatar](https://substackcdn.com/image/fetch/$s_!YSdF!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a437d7f-474e-4e6e-863a-4d7d91885fd9_800x800.jpeg)](https://substack.com/profile/248623304-damien-lewke)

7 Likes

7

[2](https://dannguyenhuu.substack.com/p/black-hat-2025-security-catalyst/comments)

Share

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

[![Robby's avatar](https://substackcdn.com/image/fetch/$s_!RTI8!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd343fdeb-02ca-49c1-8dce-debf5aa07e38_966x966.png)](https://substack.com/profile/101020040-robby?utm_source=comment)

[Robby](https://substack.com/profile/101020040-robby?utm_source=substack-feed-item)

[2h](https://dannguyenhuu.substack.com/p/black-hat-2025-security-catalyst/comment/145091344 "Aug 13, 2025, 1:58 PM")

Liked by Dan Nguyen-Huu

Love it! Great summary!

Expand full comment

Like (1)

Reply

Share

[1 reply by Dan Nguyen-Huu](https://dannguyenhuu.substack.com/p/black-hat-2025-security-catalyst/comment/145091344)

[1 more comment...](https://dannguyenhuu.substack.com/p/black-hat-2025-security-catalyst/comments)

TopLatestDiscussions

[Introducing: The Managed-Service-as-Software (M-SaS) Startup](https://dannguyenhuu.substack.com/p/introducing-the-managed-service-as)

[A technology disruption like AI is especially powerful for startups when paired with a business model disruption.](https://dannguyenhuu.substack.com/p/introducing-the-managed-service-as)

Jun 28, 2024•
[Dan Nguyen-Huu](https://substack.com/@dannguyenhuu)

22

[6](https://dannguyenhuu.substack.com/p/introducing-the-managed-service-as/comments)

![](https://substackcdn.com/image/fetch/$s_!Acfl!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1beb0529-45f3-4038-a635-78947f62147d_1792x1024.webp)

[A New Frontier: Service-as-Software, powered by AI Agents](https://dannguyenhuu.substack.com/p/a-new-frontier-service-as-software)

[Agen(t)cy for everyone to build the next generation of IT & Cybersecurity Applications](https://dannguyenhuu.substack.com/p/a-new-frontier-service-as-software)

Nov 7, 2023•
[Dan Nguyen-Huu](https://substack.com/@dannguyenhuu)

24

[4](https://dannguyenhuu.substack.com/p/a-new-frontier-service-as-software/comments)

![](https://substackcdn.com/image/fetch/$s_!fAVq!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feee40e40-f0eb-4040-8029-bfc2f854fb73_1920x1080.png)

[The Price is AI-ght? A Short Discussion on Pricing Models for AI Startups](https://dannguyenhuu.substack.com/p/the-price-is-ai-ght-a-short-discussion)

[In the ever-changing world of software pricing, the rise of AI agent applications could lead to a significant change in how companies determine the…](https://dannguyenhuu.substack.com/p/the-price-is-ai-ght-a-short-discussion)

Dec 15, 2023•
[Dan Nguyen-Huu](https://substack.com/@dannguyenhuu)

9

[2](https://dannguyenhuu.substack.com/p/the-price-is-ai-ght-a-short-discussion/comments)

![](https://substackcdn.com/image/fetch/$s_!gVki!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3a24d5fe-2cd9-4494-bf04-3a3f5d31a647_815x400.png)

See all

Ready for more?

Subscribe
