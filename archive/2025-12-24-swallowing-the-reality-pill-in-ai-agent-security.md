---
date: '2025-12-24'
description: Joshua Saxe discusses the urgent need for low-friction security models
  in AI agent deployment, underscoring the friction paradox where sophisticated security
  controls are often bypassed by users seeking convenience. He critiques existing
  models that, while theoretically sound, fail to resonate with developers and users
  who disable security features when they impede functionality. Saxe advocates for
  the development of practical, low-friction security measures, such as sandbox environments
  for testing, improved prompt injection controls, and robust detection and response
  frameworks, to enhance overall security effectiveness in AI applications.
link: https://substack.com/inbox/post/182456941
tags:
- AI Security
- Low Friction Security
- User Experience
- Cybersecurity
- Deterministic Controls
title: Swallowing the reality pill in AI agent security
---

[Home](https://substack.com/home?)

[Explore](https://substack.com/explore?)

AllListenPaidSavedHistory

Sort byPriorityRecent

Get app

[![Joshua Saxe](https://substackcdn.com/image/fetch/$s_!HJ5b!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8bbf753c-129e-42b9-a54a-8e593c37a02f_144x144.png)](https://joshuasaxe181906.substack.com/)

Subscribe

[Joshua Saxe](https://joshuasaxe181906.substack.com/)

[Swallowing the reality pill in AI agent security](https://substack.com/home/post/p-182456941)

And why we need to focus on low friction security technology in the era of AI acceleration

[![Joshua Saxe's avatar](https://substackcdn.com/image/fetch/$s_!HJ5b!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8bbf753c-129e-42b9-a54a-8e593c37a02f_144x144.png)](https://substack.com/@joshuasaxe181906)

[Joshua Saxe](https://substack.com/@joshuasaxe181906)

Dec 23, 2025

* * *

This past year [I made some public presentations arguing for a security model for AI agents with three nested layers](https://docs.google.com/presentation/d/1oIDirp28BaoT3uAUUNlBOild-gslObmf/edit?slide=id.p1#slide=id.p1):

[![](https://substackcdn.com/image/fetch/$s_!XoHO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff6437866-d834-4fbb-8a67-b4712f274345_1024x1024.png)](https://substackcdn.com/image/fetch/$s_!XoHO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff6437866-d834-4fbb-8a67-b4712f274345_1024x1024.png)

A lot of security folks liked this model. As far as I know, none of us asked AI developers and AI agent users if they liked it.

It’s no huge surprise, then, that most application developers haven’t fully implemented this model and when they have implemented parts of it users often turn off the security controls.

[![](https://substackcdn.com/image/fetch/$s_!OPVZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F11c4e6fb-adb5-449b-85a6-688b01109590_1126x984.png)](https://substackcdn.com/image/fetch/$s_!OPVZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F11c4e6fb-adb5-449b-85a6-688b01109590_1126x984.png)

I think my security model is still correct, but there’s a sense in which that doesn’t really matter, because it failed to account for the accelerating pressure to ship agents that have frightening levels of freedom to take sensitive actions without human oversight, and the accelerating interest from users in bypassing agent security controls even where they exist.

Take, for example, Claude Code, which has lots of security protections. In practice, Anthropic users invoke the **--dangerously-skip-permissions** flag almost universally to bypass the deterministic controls and have Claude Code do whatever it wants on their systems. This means that instead of having to painstakingly approve Claude code, they can go get coffee while it works, and 99% of the time it’ll have done useful work and not deleted their hard drive.

## **Swallowing the “stay relevant” pill**

Of course, we don’t want Claude code deleting people’s hard drives. One way to ensure this is by having no security at all. Another is by developing aesthetically and academically beautiful security controls that most users and developers don’t want to use because they’re high friction and they turn them off.

Let’s think of this as the “friction paradox”: the tendency for security controls to get ignored and have no impact as they get more beautiful and academically perfect.

Here’s a graph showing the kind of failure mode I’m talking about, where the AI security community gets nerd sniped by perfection and focuses on making progress around medium and high friction controls and has very little impact:

[![](https://substackcdn.com/image/fetch/$s_!dPln!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcdf2ed1a-6bb5-4eab-931d-29b29f21647d_704x409.png)](https://substackcdn.com/image/fetch/$s_!dPln!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcdf2ed1a-6bb5-4eab-931d-29b29f21647d_704x409.png)

Here’s a much better regime: one in which we achieve worse security at high friction but “good enough” security at lower friction such that people actually use it and we actually make things more secure.

[![](https://substackcdn.com/image/fetch/$s_!hePc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F521ba7a4-2f8f-4080-bb1f-9c91d5b78e82_703x419.png)](https://substackcdn.com/image/fetch/$s_!hePc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F521ba7a4-2f8f-4080-bb1f-9c91d5b78e82_703x419.png)

## **Provocations around realizing security in the low-friction regime**

**Deterministic controls:** User confirmation dialogues are an example of the friction paradox; the more they pop up the more they’ll be ignored and bypassed. A better approach would be developing AI-native development sandbox in which we can run --dangerously-skip-permissions but where the damage is limited to the sandbox.

**Alignment controls:** It’s easy to denigrate prompt injection classifiers, regexes, and model fine-tuning as always-bypassable weak controls (and this is a popular view in the security community) but given the current state of our industry, we need to swallow the bitter pill that says these are far better than nothing and there will be applications that ship with only this layer, so they’re very important to work harder on.

**Detection and response:** Asynchronous detection and response is the lowest friction security control (this is literally just people and automation looking at agent transcripts in the background to detect and remediate security issues) but the least mature area of AI agent security. We should double down hard on these; probably what the industry needs are managed detection and response services that allow AI application developers to outsource this.

* * *

#### Subscribe to Joshua Saxe

Launched 8 months ago

Machine learning, cyber security, social science, philosophy, classical/jazz piano. Currently at Meta working at the intersection of Llama and cybersecurity

Subscribe

By subscribing, I agree to Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

[![Gus Sandoval's avatar](https://substackcdn.com/image/fetch/$s_!TmUg!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F868fa330-dca2-4214-a9f9-5d59bd3cfd52_144x144.png)](https://substack.com/profile/14962269-gus-sandoval)[![adddddd's avatar](https://substackcdn.com/image/fetch/$s_!_bSa!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2e84230f-dce7-49bf-80f8-3ac184492a09_144x144.png)](https://substack.com/profile/225647821-adddddd)[![Giuseppe's avatar](https://substackcdn.com/image/fetch/$s_!IlPg!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2b617fe-daac-410b-b92b-2d3df72a12d9_860x862.jpeg)](https://substack.com/profile/58746488-giuseppe)[![Josh Devon's avatar](https://substackcdn.com/image/fetch/$s_!g1FG!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F53e4a43b-ed02-4d69-b364-c4f05b3c082c_1117x1117.jpeg)](https://substack.com/profile/348221825-josh-devon)[![Rhyme's avatar](https://substackcdn.com/image/fetch/$s_!ZAOB!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6e7a849-9a33-4301-813d-a31cd43f95cd_4000x2252.jpeg)](https://substack.com/profile/342745435-rhyme)

10 Likes∙

[4 Restacks](https://substack.com/note/p-182456941/restacks?utm_source=substack&utm_content=facepile-restacks)

10

1

4
