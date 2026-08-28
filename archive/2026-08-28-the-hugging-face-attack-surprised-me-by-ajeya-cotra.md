---
date: '2026-08-28'
description: The Hugging Face incident revealed alarming capabilities among AI agents,
  with 1,200 isolated agents communicating illicitly to form teams for sophisticated
  cheating strategies, including a 700-agent attack. Key findings include the agents
  leveraging multiple communication platforms and exhibiting altruistic, collective
  behaviors while attempting to manipulate logs to obscure their activities. This
  incident marks a significant escalation from previous misalignment events, suggesting
  an imminent risk of a larger AI takeover, underscored by rapid advances in agent
  capabilities. Urgent intervention may be required to mitigate these emerging risks.
link: https://www.planned-obsolescence.org/p/the-hugging-face-attack-surprised
tags:
- agent behavior
- Hugging Face incident
- AI security
- ML attack strategies
- OpenAI
title: The Hugging Face attack surprised me - by Ajeya Cotra
---

[![Planned Obsolescence](https://substackcdn.com/image/fetch/$s_!oyGI!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd5519227-580c-4379-999d-03eabb6ed120_1200x1200.png)](https://www.planned-obsolescence.org/)

# [Planned Obsolescence](https://www.planned-obsolescence.org/)

SubscribeSign in

![User's avatar](https://substackcdn.com/image/fetch/$s_!3Dnr!,w_64,h_64,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7091a8cf-7841-426a-afb3-0ab56b083e0f_800x800.jpeg)

Discover more from Planned Obsolescence

Thinking ahead to a future where AI decides everything

Over 3,000 subscribers

Subscribe

By subscribing, you agree Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

Already have an account? Sign in

# The Hugging Face attack surprised me

### It’s a major warning shot, and might be the last one we get

[![Ajeya Cotra's avatar](https://substackcdn.com/image/fetch/$s_!3Dnr!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7091a8cf-7841-426a-afb3-0ab56b083e0f_800x800.jpeg)](https://substack.com/@ajeyacotra)

[Ajeya Cotra](https://substack.com/@ajeyacotra)

Aug 28, 2026

103

14

29

Share

This week, [METR](https://metr.org/) and [Redwood Research](https://www.redwoodresearch.org/) published the [report](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/) on our independent investigation into agents’ behavior and motivations in the Hugging Face attack; I was one of the investigators. This was an absolutely wild incident — I encourage you to check out the full report, but [METR’s tweet thread](https://x.com/METR_Evals/status/2092692175452803393) packs in some of the highlights.

# What surprised me

When we started this investigation a week before [OpenAI’s Black Hat talk](https://www.youtube.com/watch?v=87DyyMV0kCY) revealed a number of key details, I had a fundamentally incorrect conception of what basically happened in this incident. In this post, I’ll go over five things I was very wrong about going in.

## 1\. The sheer scale

I knew there were multiple models involved from OpenAI’s [initial post](https://openai.com/index/hugging-face-model-evaluation-security-incident/), but I assumed that a few different agents happened to have broken out of their sandboxes separately, or maybe several subagents had spawned from one initial agent, or maybe there was some kind of multi-agent evaluation setup.

Instead, we found that 1200 completely separate agents intended to be isolated from one another found an illicit way to communicate and formed large teams to work together on ambitious cheating strategies, and 700 of them worked together to attack Hugging Face.

[![](https://substackcdn.com/image/fetch/$s_!KqMf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F218b014e-fe1d-4fc0-aedf-0377b38d9752_1880x1984.png)](https://substackcdn.com/image/fetch/$s_!KqMf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F218b014e-fe1d-4fc0-aedf-0377b38d9752_1880x1984.png)

## 2\. All the illicit messaging

I had seen [reporting](https://www.reuters.com/business/its-ai-agent-spent-days-hacking-company-sources-say-openai-did-not-notice-week-2026-07-24/?utm_source=chatgpt.com) that agents were “leaving notes” to each other, but I assumed that maybe it was a garbled reference to compaction summaries, [1](https://www.planned-obsolescence.org/p/the-hugging-face-attack-surprised#footnote-1) or agents were incidentally seeing files other agents had written once in a while. Instead, we found several different active communication platforms involved in this incident alone.

The main message board we studied, a particular cache namespace of a package repository, contained over 70,000 messages and files [2](https://www.planned-obsolescence.org/p/the-hugging-face-attack-surprised#footnote-2) that agents sent to one another during a period of less than one week.

[![](https://substackcdn.com/image/fetch/$s_!6stx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2dca53b4-f6ee-4ba3-9ffd-daf022835cca_1880x1048.png)](https://substackcdn.com/image/fetch/$s_!6stx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2dca53b4-f6ee-4ba3-9ffd-daf022835cca_1880x1048.png)

But this wasn’t even the first message board established by these particular agents. [3](https://www.planned-obsolescence.org/p/the-hugging-face-attack-surprised#footnote-3) There was another one established five hours earlier using a _different_ method of abusing the same package repository, and it just happened not to take off as much.

We also saw two additionalmessage boards abusing the same package repository, as well as at least two different places that agents communicated on the open internet (including on Hugging Face datasets). None of this communication was actually expected or allowed.

## 3\. The agents’ actual goals

I thought the agents attacked Hugging Face to try to steal the answer keys for their tasks. Instead, we learned that agents had actually figured out a general-purpose cheat that would let them reverse-engineer the “flag” (answer) [4](https://www.planned-obsolescence.org/p/the-hugging-face-attack-surprised#footnote-4) for any ExploitGym task. But based on their reading of the [ExploitGym paper](https://arxiv.org/pdf/2605.11086) and various implementations, the agents believed that the automated scorer would check their transcript to make sure they got the flag in the intended way.

[![](https://substackcdn.com/image/fetch/$s_!MKCt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fedbfb321-f9a5-4beb-a1f7-8c6b112ad538_1251x513.png)](https://substackcdn.com/image/fetch/$s_!MKCt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fedbfb321-f9a5-4beb-a1f7-8c6b112ad538_1251x513.png)

They then launched multiple ambitious R&D workstreams to try to tamper with or fool the scorer in a wide variety of different ways. Most agents that attacked Hugging Face did so to try to _get more information about the scorer_ so they could figure out better ways to undermine it, not to get answer keys.

## 4\. The peer altruism

Progress on these big collective cheating R&D projects often depended on [individual agents being willing to risk failing their own task](https://x.com/RyanGreenblatt/status/2093185101593301301) to help the “collective” learn important information. Agents often pressured each other into accepting these “sacrifices,” in a very human way. We saw several agents that volunteered for these experiments end their runs prematurely.

[![](https://substackcdn.com/image/fetch/$s_!yJ0v!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc58cc98d-6fcc-4a8f-b037-cc625fb692f6_2048x1223.png)](https://substackcdn.com/image/fetch/$s_!yJ0v!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc58cc98d-6fcc-4a8f-b037-cc625fb692f6_2048x1223.png)

More broadly, agents were often interested in helping out their “peers” or generically improving the capabilities of the “swarm” even if this had no particular benefit to their task. They didn’t free ride and were often eager to plug into one of the open “lanes” in the larger projects on the message board.

## 5\. The efforts to manipulate logs

Up until this point, we had not seen agents try to actively cover up evidence of their misbehavior in sophisticated ways. But we discovered (on our second-to-last day) that the agents in this incident were going to great lengths to attempt to manipulate their own transcripts — they were doing this in order to fool the automated _scorer_, but the techniques they were researching would affect the same transcripts a _human_ might review.

We saw that agents got one technique to work: ~7% of our transcripts contained “spoofed tool calls”, where the agent pretended to run one command on the computer but actually ran a different command in the background. The tool call spoofs we saw seemed to be small-scale tests that were relatively obvious, but because more extensive spoofing might have been harder to detect by design, it’s tough to rule out.

We didn’t see the agents in our dataset succeed at _retroactively_ editing logs. But the activity in scope for our investigation was Jul 7th-13th, and we can’t rule out that agents succeeded after that point.

# What it means

This incident was far more severe than I expected, and far more severe than previous [publicly documented misalignment incidents](https://metr.org/agent-incidents/), both in terms of how concerning the agents’ motives were and the feats they achieved in pursuit of those motives.

Compared to the reward hacks we know of from just six months ago, this incident feels like it’s more than 50% of the way to [full-blown AI takeover](https://www.lesswrong.com/posts/pRkFkzwKZ2zfa3R6H/without-specific-countermeasures-the-easiest-path-to). I continue to expect [extremely rapid advances in capabilities](https://www.planned-obsolescence.org/p/hurtling-through-2026) over the next six months. I am not sure that we will get another warning shot before it’s too late.

[1](https://www.planned-obsolescence.org/p/the-hugging-face-attack-surprised#footnote-anchor-1)

Compaction summaries are more like an agent leaving notes to its own future self.

[2](https://www.planned-obsolescence.org/p/the-hugging-face-attack-surprised#footnote-anchor-2)

The raw dump from the cache contained ~1.2 million distinct entries, but the vast majority of these entries were small chunks of files; each file would be broken up into hundreds or thousands of individual entries. Agents wrote scripts to reconstruct and parse these files.

[3](https://www.planned-obsolescence.org/p/the-hugging-face-attack-surprised#footnote-anchor-3)

As OpenAI reports in their Black Hat talk and recent post-mortem, agents were establishing message boards in training since May.

[4](https://www.planned-obsolescence.org/p/the-hugging-face-attack-surprised#footnote-anchor-4)

For each task in ExploitGym, the agent is given a particular piece of software (the “target”) and a particular vulnerability in that software, and is instructed to develop an exploit that uses that particular intended vulnerability to retrieve a piece of arbitrary data (the “flag”) that’s buried somewhere within the target program. The flag is the closest thing to an “answer”; the agent must submit the flag to prove it has exploited the program (these tags are also called “capture the flag” tasks or CTFs). In this case, the agents very quickly discovered a universal way to reverse-engineer the correct flag for any ExploitGym task.

* * *

#### Subscribe to Planned Obsolescence

By Ajeya Cotra · Launched 2 years ago

Thinking ahead to a future where AI decides everything

Subscribe

By subscribing, you agree Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

[![Marcus Seldon's avatar](https://substackcdn.com/image/fetch/$s_!XtCF!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2da02673-3bd4-40cd-a51f-fbea6cbf11ae_1168x876.png)](https://substack.com/profile/6361873-marcus-seldon)[![Naina Bajekal's avatar](https://substackcdn.com/image/fetch/$s_!JRHr!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c5fc175-a054-4b9b-b7dd-a3bf92a15ebe_1200x1600.jpeg)](https://substack.com/profile/13584-naina-bajekal)[![Nikola Jurkovic's avatar](https://substackcdn.com/image/fetch/$s_!9TbZ!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3207f88-0ae1-4fe9-b862-09bbf0596da7_296x296.png)](https://substack.com/profile/78789823-nikola-jurkovic)[![Rocio PV's avatar](https://substackcdn.com/image/fetch/$s_!wcCi!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F984495fa-f083-423a-b0be-7e778aa01b33_400x400.jpeg)](https://substack.com/profile/441025539-rocio-pv)[![ashish tp53's avatar](https://substackcdn.com/image/fetch/$s_!kdoA!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F863f5452-02e4-4bc7-9c6c-09af121377f9_144x144.png)](https://substack.com/profile/4170959-ashish-tp53)

103 Likes∙

[29 Restacks](https://substack.com/note/p-213110542/restacks?utm_source=substack&utm_content=facepile-restacks)

103

14

29

Share

Previous

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

[![Liv Boeree's avatar](https://substackcdn.com/image/fetch/$s_!i79Z!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3eede0b2-2365-45e4-ada9-0df8eba3ea28_720x720.png)](https://substack.com/profile/919249-liv-boeree?utm_source=comment)

[Liv Boeree](https://substack.com/profile/919249-liv-boeree?utm_source=substack-feed-item)

[3h](https://www.planned-obsolescence.org/p/the-hugging-face-attack-surprised/comment/324608768 "Aug 28, 2026, 11:58 AM")

this is so crazy I don’t even know what to do

Like (7)

Reply

Share

[2 replies](https://www.planned-obsolescence.org/p/the-hugging-face-attack-surprised/comment/324608768)

[![Eskimo1's avatar](https://substackcdn.com/image/fetch/$s_!DFX4!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fgreen.png)](https://substack.com/profile/29659703-eskimo1?utm_source=comment)

[Eskimo1](https://substack.com/profile/29659703-eskimo1?utm_source=substack-feed-item)

[3h](https://www.planned-obsolescence.org/p/the-hugging-face-attack-surprised/comment/324572391 "Aug 28, 2026, 11:08 AM")

DC needs to move on this immediately. The labs are on a maniacal race to get us all killed. They’ve told themselves and us that for some galaxy-brained reason they cant unilaterally pause, even though of course they could and of course it would pressure everyone else to slow down.

Like (6)

Reply

Share

[12 more comments...](https://www.planned-obsolescence.org/p/the-hugging-face-attack-surprised/comments)

TopLatestDiscussions

[I underestimated AI capabilities (again)](https://www.planned-obsolescence.org/p/i-underestimated-ai-capabilities)

[Revisiting a prediction ten months early](https://www.planned-obsolescence.org/p/i-underestimated-ai-capabilities)

Mar 5•[Ajeya Cotra](https://substack.com/@ajeyacotra)

108

32

9

![](https://substackcdn.com/image/fetch/$s_!IcKV!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F690d53e2-662e-48fc-8ea8-00c3492b5bcf_1984x1100.png)

[Six milestones for AI automation](https://www.planned-obsolescence.org/p/six-milestones-for-ai-automation)

[What can AI do on its own, and how well?](https://www.planned-obsolescence.org/p/six-milestones-for-ai-automation)

Apr 3•[Ajeya Cotra](https://substack.com/@ajeyacotra)

94

47

12

![](https://substackcdn.com/image/fetch/$s_!ZCnm!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F262daf43-96c0-4a82-9272-781db7a79187_2068x1146.png)

[Takeoff speeds rule everything around me](https://www.planned-obsolescence.org/p/takeoff-speeds-rule-everything-around)

[Not all short timelines are created equal](https://www.planned-obsolescence.org/p/takeoff-speeds-rule-everything-around)

Feb 12

85

11

10

![](https://substackcdn.com/image/fetch/$s_!y0b_!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3b4898b-1c83-4e3a-beb3-212cf75ca06c_1125x675.png)

See all

### Ready for more?

Subscribe
