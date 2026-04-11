---
date: '2026-04-11'
description: Costin Raiu's analysis outlines the transformative impact of AI on zero-day
  vulnerability research. With models like Anthropic's Mythos, the cost of discovering
  exploits is decreasing, leading to a surge in targets previously deemed secure.
  This will usher in a new era characterized as the "Zero-Day Economic Arc," transitioning
  from a flood of low-cost exploits to the need for advanced defenses, where human-machine
  collaboration will be essential. Ultimately, the risk lies in undertraining the
  next generation due to automation, emphasizing the necessity for a balance between
  leveraging AI and maintaining critical cybersecurity skills.
link: https://medium.com/@costin.raiu/the-ai-0-day-economic-arc-from-the-flood-to-the-10x-spike-9b9ed6f256c6
tags:
- cybersecurity
- vulnerability research
- machine learning
- AI
- zero-day
title: 'The AI 0-Day Economic Arc: From the Flood to the 10x Spike ◆ by Costin Raiu
  ◆ Apr, 2026 ◆ Medium'
---

[Sitemap](https://medium.com/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40costin.raiu%2Fthe-ai-0-day-economic-arc-from-the-flood-to-the-10x-spike-9b9ed6f256c6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40costin.raiu%2Fthe-ai-0-day-economic-arc-from-the-flood-to-the-10x-spike-9b9ed6f256c6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

# The AI 0-Day Economic Arc: From the Flood to the 10x Spike

[![Costin Raiu](https://miro.medium.com/v2/resize:fill:32:32/1*dsFfGfTrcZ2XH6clqwiw_A.jpeg)](https://medium.com/@costin.raiu?source=post_page---byline--9b9ed6f256c6---------------------------------------)

[Costin Raiu](https://medium.com/@costin.raiu?source=post_page---byline--9b9ed6f256c6---------------------------------------)

Follow

4 min read

·

2 days ago

2

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D9b9ed6f256c6&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40costin.raiu%2Fthe-ai-0-day-economic-arc-from-the-flood-to-the-10x-spike-9b9ed6f256c6&source=---header_actions--9b9ed6f256c6---------------------post_audio_button------------------)

Share

A year in AI is essentially a decade in “traditional” cybersecurity. When people ask me if our [Three Buddy Problem](https://podcasts.apple.com/us/podcast/three-buddy-problem/id1414525622) conversations from twelve months ago are still relevant, the answer is usually: _partially, but the dam has since broken._

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*TsX1M6UMAh-d6YoBKxveEw.png)

Mythos Preview

This week, Anthropic’s new [**Mythos**](https://www-cdn.anthropic.com/8b8380204f74670be75e81c820ca8dda846ab289.pdf) model and **Project** [**Glasswing**](https://www.anthropic.com/project/glasswing) took the news. Many want to know if vulnerability research is, as some say, “cooked.” Here is how I’m looking at the landscape today.

## The End of the “Elite” Barrier

For decades, zero-day research was a high-stakes, high-cost game played by a tiny circle of elite researchers. If you wanted a zero-click chain for iOS, you needed millions of dollars and months of manual labor.

Models like **Mythos** and initiatives like [**Glasswing**](https://www.anthropic.com/project/glasswing) are changing the physics of this market. We are moving from “AI as an assistant” to “AI as the lead researcher.” You can now point an agentic model at a massive codebase, give it a goal, and let it hunt. It doesn’t get tired, and it doesn’t miss the “boring” bugs that humans overlook. If it’s good enough, it might even find stuff.

This leads to what I call the **Zero-Day Economic Arc**:

> _“There will be a period of time where the cost of exploits goes down dramatically then a sharp slope where security goes up and prices reach 10x of what they used to be.” — Costin Raiu_

### Phase 1: The Flood (Short-Term)

Right now, we are entering the “Flood.” Because the cost of finding vulnerabilities is dropping toward zero, we are seeing a massive **target expansion**. Attackers are no longer just focused on browsers and mobile kernels; they are hitting routers, printers, and critical infrastructure that was previously “secure” simply because it wasn’t worth the manual effort to audit. This is the “commodity zero-day” era.

### Phase 2: The 10x Spike (Long-Term)

As the market becomes saturated with bugs, the defensive side will finally leverage AI to do what humans couldn’t: **patch at scale.** We’ll see AI rewriting legacy C++ into memory-safe Rust, Golang or [Swift](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/memorysafety/) and deploying real-time fixes across entire ecosystems.

When the “easy” bugs are gone, the remaining vulnerabilities will be so deep and complex that only a “Cyborg” (a human expert paired with a frontier model) can find them. This is when prices will skyrocket. We are looking at a future where an iOS zero-click chain might command **$50 million or $100 million**.

## The “Cyborg” Reality: Intuition vs. Processing

I often cite [Garry Kasparov’s idea of “Cyborg Chess.”](https://en.wikipedia.org/wiki/Advanced_chess) His argument is that it no longer makes sense for a human to play a machine, but a human _plus_ a machine is a formidable force. The [human-machine team](https://www.amazon.com/Human-Machine-Team-Artificial-Intelligence-Revolutionize-ebook/dp/B09472K2YZ) always wins.

## Get Costin Raiu’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

Remember me for faster sign in

In cybersecurity, AI provides the **data processing and scale**, but humans still provide the **adversarial intuition**. The machines are excellent at finding the flaw, but they don’t always understand the “why” or the broader architectural implications.

However, there is a risk I worry about. Our friend Chris St. Meyers wrote about it in an amazing blog entitled: [**The Cognitive Rust Belt**](https://www.sentinelone.com/blog/the-implementation-blind-spot-why-organizations-are-confusing-temporary-friction-with-permanent-safety/) **.** If we automate all the “grunt work” — the tedious log analysis and manual debugging — how do we train the next generation of experts? If you don’t sweat over the small stuff, you never develop the intuition needed to guide the AI. There is no good answer. This needs to be fixed with education and in schools we still punish kids for using ChatGPT to do their homeworks when in reality, at work, people who don’t use AI fall behind.

## From Reactive to Generative

The ultimate end-state isn’t just better patching; it’s a fundamental redesign of how we handle code.

Currently, our digital world is built on a “shared needle” model — we download packages (NPM, Cargo, etc.) from people we don’t know and run them on our machines. It’s a supply chain nightmare.

JAGS has an interesting solution: the “Generative OS” thesis. Eventually, we might end up using models like **Mythos** to **generate our own software locally**.

Why run someone else’s potentially backdoored browser when your local “code factory” can generate a secure, audited version of a browser tailored specifically to your needs?

## Final Thoughts

To answer the question: Is Mythos a threat? **Yes.** It lowers the floor for attackers. But it also raises the ceiling for defenders.

We are currently in the messy middle — the “Flood.” It’s going to be a chaotic few years of high-volume attacks and “vibe-coded” exploits. But on the other side of that sharp slope, we might finally reach a level of security that was previously impossible.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*PBxghbMnc5iT-Jz_e1FPvw.png)

**Bojumeok** (보주먹, often written as **bojumeok-junbi** or **covered fist ready stance/posture**) is a specific **ready posture** we use in Taekwondo. It symbolizes **control and readiness**: the strong hand (the right fist) is “covered” and protected by the other hand, representing that you have the power to strike but choose to remain calm and controlled until necessary.

If we let AI run wild without the **Bojumeok** philosophy, we end up in that “Flood” I talked about — where everything is broken and nobody knows how to fix it. We need to stop being impressed by how hard the “AI fist” can hit and start focusing on how well we can “cover” it.

The goal of security shouldn’t be to have the biggest weapon; it should be to reach a state of **controlled readiness** — where we have the power to strike any vulnerability, but we choose to remain calm, focused, and secure.

**Stay calm, keep your fist covered, and update your iOS.**

**— Costin**

[![Costin Raiu](https://miro.medium.com/v2/resize:fill:48:48/1*dsFfGfTrcZ2XH6clqwiw_A.jpeg)](https://medium.com/@costin.raiu?source=post_page---post_author_info--9b9ed6f256c6---------------------------------------)

[![Costin Raiu](https://miro.medium.com/v2/resize:fill:64:64/1*dsFfGfTrcZ2XH6clqwiw_A.jpeg)](https://medium.com/@costin.raiu?source=post_page---post_author_info--9b9ed6f256c6---------------------------------------)

Follow

[**Written by Costin Raiu**](https://medium.com/@costin.raiu?source=post_page---post_author_info--9b9ed6f256c6---------------------------------------)

[84 followers](https://medium.com/@costin.raiu/followers?source=post_page---post_author_info--9b9ed6f256c6---------------------------------------)

· [21 following](https://medium.com/@costin.raiu/following?source=post_page---post_author_info--9b9ed6f256c6---------------------------------------)

Cybersecurity researcher focused on threat intel & APTs. Breaking down attacks and hunting threats. Buddy @ Three Buddy Problem & TLPBLACK

Follow

## No responses yet

![](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

Write a response

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40costin.raiu%2Fthe-ai-0-day-economic-arc-from-the-flood-to-the-10x-spike-9b9ed6f256c6&source=---post_responses--9b9ed6f256c6---------------------respond_sidebar------------------)

Cancel

Respond

## More from Costin Raiu

![Alice left the Wonderland](https://miro.medium.com/v2/resize:fit:679/format:webp/1*rWNSxFsgWjdKGO6XZJHUrw.png)

[![Costin Raiu](https://miro.medium.com/v2/resize:fill:20:20/1*dsFfGfTrcZ2XH6clqwiw_A.jpeg)](https://medium.com/@costin.raiu?source=post_page---author_recirc--9b9ed6f256c6----0---------------------68b940be_d0a9_48b1_b899_b6f5c6272625--------------)

[Costin Raiu](https://medium.com/@costin.raiu?source=post_page---author_recirc--9b9ed6f256c6----0---------------------68b940be_d0a9_48b1_b899_b6f5c6272625--------------)

Mar 17

[A clap icon55\\
\\
A response icon1](https://medium.com/@costin.raiu/alice-left-the-wonderland-41f3988aedb8?source=post_page---author_recirc--9b9ed6f256c6----0---------------------68b940be_d0a9_48b1_b899_b6f5c6272625--------------)

![The Cybersecurity Booklist: 11 Must-Reads for 2026 from The Three Buddy Problem Podcast](https://miro.medium.com/v2/resize:fit:679/format:webp/0*tvh9CtJS4oLC6ou4.jpg)

[![Costin Raiu](https://miro.medium.com/v2/resize:fill:20:20/1*dsFfGfTrcZ2XH6clqwiw_A.jpeg)](https://medium.com/@costin.raiu?source=post_page---author_recirc--9b9ed6f256c6----1---------------------68b940be_d0a9_48b1_b899_b6f5c6272625--------------)

[Costin Raiu](https://medium.com/@costin.raiu?source=post_page---author_recirc--9b9ed6f256c6----1---------------------68b940be_d0a9_48b1_b899_b6f5c6272625--------------)

[**In a recent episode of The Three Buddy Problem podcast, together with my buddies Ryan and Jags we discussed some of the reads that shaped…**](https://medium.com/@costin.raiu/the-cybersecurity-booklist-11-must-reads-for-2026-from-the-three-buddy-problem-podcast-ef8216958bd3?source=post_page---author_recirc--9b9ed6f256c6----1---------------------68b940be_d0a9_48b1_b899_b6f5c6272625--------------)

Jan 9

[A clap icon73](https://medium.com/@costin.raiu/the-cybersecurity-booklist-11-must-reads-for-2026-from-the-three-buddy-problem-podcast-ef8216958bd3?source=post_page---author_recirc--9b9ed6f256c6----1---------------------68b940be_d0a9_48b1_b899_b6f5c6272625--------------)

![What we know about the Notepad++ supply chain attack](https://miro.medium.com/v2/resize:fit:679/format:webp/1*sEdlgw7Pl9pOAU8oQ6HSTQ.png)

[![Costin Raiu](https://miro.medium.com/v2/resize:fill:20:20/1*dsFfGfTrcZ2XH6clqwiw_A.jpeg)](https://medium.com/@costin.raiu?source=post_page---author_recirc--9b9ed6f256c6----2---------------------68b940be_d0a9_48b1_b899_b6f5c6272625--------------)

[Costin Raiu](https://medium.com/@costin.raiu?source=post_page---author_recirc--9b9ed6f256c6----2---------------------68b940be_d0a9_48b1_b899_b6f5c6272625--------------)

[**(updated 4-Feb-2026 with information from Hostinger and Validin)**](https://medium.com/@costin.raiu/what-we-know-about-the-notepad-supply-chain-attack-0f428b4aee08?source=post_page---author_recirc--9b9ed6f256c6----2---------------------68b940be_d0a9_48b1_b899_b6f5c6272625--------------)

Feb 3

[A clap icon64](https://medium.com/@costin.raiu/what-we-know-about-the-notepad-supply-chain-attack-0f428b4aee08?source=post_page---author_recirc--9b9ed6f256c6----2---------------------68b940be_d0a9_48b1_b899_b6f5c6272625--------------)

![An analysis of the BreachForums leak(s)](https://miro.medium.com/v2/resize:fit:679/format:webp/1*sWDvniA7X6rGajox1Q3lCg.png)

[![Costin Raiu](https://miro.medium.com/v2/resize:fill:20:20/1*dsFfGfTrcZ2XH6clqwiw_A.jpeg)](https://medium.com/@costin.raiu?source=post_page---author_recirc--9b9ed6f256c6----3---------------------68b940be_d0a9_48b1_b899_b6f5c6272625--------------)

[Costin Raiu](https://medium.com/@costin.raiu?source=post_page---author_recirc--9b9ed6f256c6----3---------------------68b940be_d0a9_48b1_b899_b6f5c6272625--------------)

[**BreachForums is a notorious dark web marketplace for stolen data that appeared in 2022. Because the forum has been shut down and rebooted…**](https://medium.com/@costin.raiu/an-analysis-of-the-breachforums-leak-s-55539f6c18df?source=post_page---author_recirc--9b9ed6f256c6----3---------------------68b940be_d0a9_48b1_b899_b6f5c6272625--------------)

Jan 12

[See all from Costin Raiu](https://medium.com/@costin.raiu?source=post_page---author_recirc--9b9ed6f256c6---------------------------------------)

## Recommended from Medium

![If You Understand These 5 AI Terms, You’re Ahead of 90% of People](https://miro.medium.com/v2/resize:fit:679/format:webp/1*qbVrf-wO9PYtthAj6E4RYQ.png)

[![Towards AI](https://miro.medium.com/v2/resize:fill:20:20/1*JyIThO-cLjlChQLb6kSlVQ.png)](https://medium.com/towards-artificial-intelligence?source=post_page---read_next_recirc--9b9ed6f256c6----0---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

In

[Towards AI](https://medium.com/towards-artificial-intelligence?source=post_page---read_next_recirc--9b9ed6f256c6----0---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

by

[Shreyas Naphad](https://medium.com/@shreyasnaphad?source=post_page---read_next_recirc--9b9ed6f256c6----0---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

[**Master the core ideas behind AI without getting lost**](https://medium.com/towards-artificial-intelligence/if-you-understand-these-5-ai-terms-youre-ahead-of-90-of-people-c7622d353319?source=post_page---read_next_recirc--9b9ed6f256c6----0---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

Mar 29

[A clap icon8.2K\\
\\
A response icon166](https://medium.com/towards-artificial-intelligence/if-you-understand-these-5-ai-terms-youre-ahead-of-90-of-people-c7622d353319?source=post_page---read_next_recirc--9b9ed6f256c6----0---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

![Palantir CEO Says Only Two Types Will Survive AI (And Elite Degrees Aren’t One of Them)!](https://miro.medium.com/v2/resize:fit:679/format:webp/0*l4NiCXObZ9VFewv8)

[![Predict](https://miro.medium.com/v2/resize:fill:20:20/1*EetZyjDw-19wRRBzc6fSMA.png)](https://medium.com/predict?source=post_page---read_next_recirc--9b9ed6f256c6----1---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

In

[Predict](https://medium.com/predict?source=post_page---read_next_recirc--9b9ed6f256c6----1---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

by

[Tasmia Sharmin](https://medium.com/@tasmiasharmin7?source=post_page---read_next_recirc--9b9ed6f256c6----1---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

[**Alex Karp told Gen Z there are “basically two ways to know you have a future.” Vocational training or neurodivergence. Philosophy degrees…**](https://medium.com/predict/palantir-ceo-says-only-two-types-will-survive-ai-and-elite-degrees-arent-one-of-them-341c222044e0?source=post_page---read_next_recirc--9b9ed6f256c6----1---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

Mar 26

[A clap icon3.3K\\
\\
A response icon253](https://medium.com/predict/palantir-ceo-says-only-two-types-will-survive-ai-and-elite-degrees-arent-one-of-them-341c222044e0?source=post_page---read_next_recirc--9b9ed6f256c6----1---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

![A quiet shift in power: Qwen’s open-source AI core emerges from the shadows, challenging the dominance of closed corporate models.](https://miro.medium.com/v2/resize:fit:679/format:webp/1*Xi5NxKh9VaV79bx6OyJ6dg.png)

[![Suleiman Tawil](https://miro.medium.com/v2/resize:fill:20:20/1*oej3hyYVseQigyP7zGqFAQ.png)](https://medium.com/@stawils?source=post_page---read_next_recirc--9b9ed6f256c6----0---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

[Suleiman Tawil](https://medium.com/@stawils?source=post_page---read_next_recirc--9b9ed6f256c6----0---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

[**The most-downloaded AI model family on Earth was built by a small team with fewer resources than its competitors. Then Alibaba restructured…**](https://medium.com/@stawils/qwen-just-quietly-became-the-most-dangerous-open-source-ai-model-b5bcf7b2743c?source=post_page---read_next_recirc--9b9ed6f256c6----0---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

Mar 31

[A clap icon1.6K\\
\\
A response icon43](https://medium.com/@stawils/qwen-just-quietly-became-the-most-dangerous-open-source-ai-model-b5bcf7b2743c?source=post_page---read_next_recirc--9b9ed6f256c6----0---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

![6 brain images](https://miro.medium.com/v2/resize:fit:679/format:webp/1*Q-mzQNzJSVYkVGgsmHVjfw.png)

[![Write A Catalyst](https://miro.medium.com/v2/resize:fill:20:20/1*KCHN5TM3Ga2PqZHA4hNbaw.png)](https://medium.com/write-a-catalyst?source=post_page---read_next_recirc--9b9ed6f256c6----1---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

In

[Write A Catalyst](https://medium.com/write-a-catalyst?source=post_page---read_next_recirc--9b9ed6f256c6----1---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

by

[Dr. Patricia Schmidt](https://medium.com/@creatorschmidt?source=post_page---read_next_recirc--9b9ed6f256c6----1---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

[**Most people do \#1 within 10 minutes of waking (and it sabotages your entire day)**](https://medium.com/write-a-catalyst/as-a-neuroscientist-i-quit-these-5-morning-habits-that-destroy-your-brain-3efe1f410226?source=post_page---read_next_recirc--9b9ed6f256c6----1---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

Jan 14

[A clap icon46K\\
\\
A response icon938](https://medium.com/write-a-catalyst/as-a-neuroscientist-i-quit-these-5-morning-habits-that-destroy-your-brain-3efe1f410226?source=post_page---read_next_recirc--9b9ed6f256c6----1---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

![Vibe Coding is Over illustration of three ai generated landing pages with the words IT’S OVER written at the top in large text](https://miro.medium.com/v2/resize:fit:679/format:webp/1*1OGKfKCooEZbKCSoSXXY8g.png)

[![Michal Malewicz](https://miro.medium.com/v2/resize:fill:20:20/1*149zXrb2FXvS_mctL4NKSg.png)](https://medium.com/@michalmalewicz?source=post_page---read_next_recirc--9b9ed6f256c6----2---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

[Michal Malewicz](https://medium.com/@michalmalewicz?source=post_page---read_next_recirc--9b9ed6f256c6----2---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

[**Here’s What Comes Next.**](https://medium.com/@michalmalewicz/vibe-coding-is-over-5a84da799e0d?source=post_page---read_next_recirc--9b9ed6f256c6----2---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

Mar 24

[A clap icon4.8K\\
\\
A response icon184](https://medium.com/@michalmalewicz/vibe-coding-is-over-5a84da799e0d?source=post_page---read_next_recirc--9b9ed6f256c6----2---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

![I Woke Up at 4:30 AM Every Day for 30 Days — Here Is What Nobody Tells You](https://miro.medium.com/v2/resize:fit:679/format:webp/1*0XnPmr19m6XJf9vZ9ojJ-Q.png)

[![ILLUMINATION](https://miro.medium.com/v2/resize:fill:20:20/1*AZxiin1Cvws3J0TwNUP2sQ.png)](https://medium.com/illumination?source=post_page---read_next_recirc--9b9ed6f256c6----3---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

In

[ILLUMINATION](https://medium.com/illumination?source=post_page---read_next_recirc--9b9ed6f256c6----3---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

by

[Sufyan Maan, M.Eng](https://medium.com/@sufyanmaan?source=post_page---read_next_recirc--9b9ed6f256c6----3---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

[**Here is what actually happened, from someone who did it & tracked everything.**](https://medium.com/illumination/i-woke-up-at-4-30-am-every-day-for-30-days-here-is-what-nobody-tells-you-054bf0160903?source=post_page---read_next_recirc--9b9ed6f256c6----3---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

Apr 3

[A clap icon7.4K\\
\\
A response icon323](https://medium.com/illumination/i-woke-up-at-4-30-am-every-day-for-30-days-here-is-what-nobody-tells-you-054bf0160903?source=post_page---read_next_recirc--9b9ed6f256c6----3---------------------aafe11ae_5816_4467_9937_62ce87ee6282--------------)

[See more recommendations](https://medium.com/?source=post_page---read_next_recirc--9b9ed6f256c6---------------------------------------)

[Help](https://help.medium.com/hc/en-us?source=post_page-----9b9ed6f256c6---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----9b9ed6f256c6---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----9b9ed6f256c6---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----9b9ed6f256c6---------------------------------------)

[Press](mailto:pressinquiries@medium.com)

[Blog](https://blog.medium.com/?source=post_page-----9b9ed6f256c6---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----9b9ed6f256c6---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----9b9ed6f256c6---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----9b9ed6f256c6---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----9b9ed6f256c6---------------------------------------)

reCAPTCHA

Recaptcha requires verification.

protected by **reCAPTCHA**
