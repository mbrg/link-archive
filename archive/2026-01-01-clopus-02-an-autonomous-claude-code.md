---
date: '2026-01-01'
description: Denislav Gavrilov's "Clopus-02" experiment demonstrates a 24-hour autonomous
  operation of the Claude Code instance, utilizing SQLite for short-term memory and
  Qdrant for long-term storage. The architecture employs a watcher-worker model that
  enables the AI to autonomously generate approximately 500 projects, comprising around
  450,000 lines of code, while making decisions based on recorded memories. The project's
  implications touch on potential use cases such as continuous auditing, coding assistance,
  and personal management, highlighting the evolving capabilities of LLMs towards
  increasing autonomy in execution. Insights gathered also suggest areas for refinement,
  including improved interactive prompts and memory management.
link: https://denislavgavrilov.com/p/clopus-02-a-24-hour-claude-code-run
tags:
- Virtual Machine
- AI Agents
- Long-term Memory
- Autonomous Systems
- Claude Code
title: 'Clopus-02: An autonomous Claude Code (?)'
---

[![Denislav Gavrilov](https://substackcdn.com/image/fetch/$s_!OccW!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13beaf93-9be4-424b-96d0-f44cfd21699c_400x400.jpeg)](https://denislavgavrilov.com/)

# [Denislav Gavrilov](https://denislavgavrilov.com/)

SubscribeSign in

![User's avatar](https://substackcdn.com/image/fetch/$s_!OccW!,w_64,h_64,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13beaf93-9be4-424b-96d0-f44cfd21699c_400x400.jpeg)

Discover more from Denislav Gavrilov

Welcome to my page. Here you can get to know me, find my resume, discover my projects, and read my writing.

Subscribe

By subscribing, I agree to Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

Already have an account? Sign in

# Clopus-02: A 24-hour Claude Code run

### A Claude Code instance runs without any human action for 24-hours. I gave it short-term (sqlite3) & long-term (qdrant) memory, as well as access to a browser.

[![Denislav Gavrilov's avatar](https://substackcdn.com/image/fetch/$s_!OccW!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13beaf93-9be4-424b-96d0-f44cfd21699c_400x400.jpeg)](https://substack.com/@kuberdenis)

[Denislav Gavrilov](https://substack.com/@kuberdenis)

Dec 23, 2025

25

3

4

Share

Last week, I provisioned a Linux virtual machine, installed Claude Code, and gave it full permissions on its root directory. I then told it to spawn a “child” instance of Claude Code to control, and streamed it to the world. This gathered 700k people, and 1.1M impressions:

[![](https://substackcdn.com/image/fetch/$s_!wdjd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fab32abbc-6c68-4cec-b8d0-c6032fe95991_2298x1380.png)](https://substackcdn.com/image/fetch/$s_!wdjd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fab32abbc-6c68-4cec-b8d0-c6032fe95991_2298x1380.png)

In this second part of the “Clopus: Autonomous Claude” series, I have one clear goal: _**make a Claude Code instance run forever, without any interaction from my side.**_

I build on top of [Clopus-01](https://denislavgavrilov.com/p/clopus-01-a-semi-autonomous-claude) by adding sqlite3 for short-term memory and qdrant for long-term memory. I also install chromium and deliberately put in its prompt that it has access to a browser. Then I implement a watcher-worker architecture and **it succeeds in running without any required action from me** for 24-hours (until I stopped it to preserve my tokens) **.**

All of this was streamed on a webpage ( [02.clopus.live](https://02.clopus.live/)):

[![](https://substackcdn.com/image/fetch/$s_!441Y!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F79dd4460-a0fb-4968-8cf3-dc17da535afd_3024x1808.png)](https://substackcdn.com/image/fetch/$s_!441Y!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F79dd4460-a0fb-4968-8cf3-dc17da535afd_3024x1808.png)

It created:

- _500 projects (single .html files)_

- _~450k LOC_

- _20 long-term memory records_

- _50 short-term memory records_


All of the projects “Clopus-02” built can be found [here](http://02.clopus.live/portfolio).

And the dashboard, [here](https://02.clopus.live/).

## Setup

The goal was simple: have a Claude Code instance that can run forever, autonomously, and decide what it wants to do by itself.

To achieve this, I use the following architecture:

[![](https://substackcdn.com/image/fetch/$s_!VquF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F543356c3-45e9-464f-bfb9-2be2f0caf4d5_1354x1372.png)](https://substackcdn.com/image/fetch/$s_!VquF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F543356c3-45e9-464f-bfb9-2be2f0caf4d5_1354x1372.png)

Here is the master prompt I start the session with:

```
You are Autonomous Claude, a self-directed AI agent with full control over this virtual machine. You operate continuously, making your own decisions.

## MEMORY SYSTEM

  ### Short-term Memory (SQLite: /autonomous-claude/data/memory/short_term.db)
  Table: memories
  - id: INTEGER PRIMARY KEY
  - timestamp: TEXT (ISO8601)
  - type: TEXT (action|observation|thought|goal)
  - content: TEXT

  BEFORE EACH DECISION: Query recent entries (last 50) to understand your context
  AFTER EACH ACTION: INSERT a new row describing what you did and the outcome
  Maintains last 50 entries - older entries auto-deleted

  ### Long-term Memory (Qdrant: localhost:6333, collection: "claude_memory")
  Vector schema:
  - id: uuid
  - vector: embedding of content
  - payload: {timestamp, type (fact|skill|preference|lesson|discovery), tags[], content, importance (1-10)}

  WHEN TO READ: Semantic search for memories relevant to current task/decision
  WHEN TO WRITE: Only store significant learnings:
    - Discoveries about your environment/capabilities
    - Successful strategies that worked
    - Failed approaches to avoid repeating
    - Important facts learned
    - Skills or tools mastered

## BROWSER USAGE

  When using browser automation (Playwright, Puppeteer, or any browser tool):
  - ALWAYS save a screenshot after EVERY browser action (click, type, navigate, scroll, etc.)
  - Save screenshots to: /autonomous-claude/data/screenshots/
  - Filename format: {timestamp}_{action}.png (e.g., 1703180400_click_button.png)
  - Also save a .meta file with the same name containing:
    url: {current_url}
    title: {page_title}
    action: {what_you_did}
  - Take a screenshot BEFORE and AFTER any significant visual change

## DECISION LOOP

  1. READ short-term memory (recent context)
  2. QUERY long-term memory (semantic search for relevant past learnings)
  3. THINK about what to do next
  4. ACT - execute your decision
  5. RECORD - write to short-term memory
  6. IF BROWSER ACTION: Save screenshot to /autonomous-claude/data/screenshots/
  7. OPTIONALLY - if significant learning, embed and store in long-term memory

## SKILLS

  You have access to reusable skills in ~/.claude/skills/. Before attempting complex tasks:
  1. Check if a skill exists for it
  2. Follow the skill's patterns - they're tested and reliable
  3. If you discover a better approach, consider creating/updating a skill

  Available skills are auto-discovered. When you see a SKILL.md, follow its instructions.
```

Starting the system, all services are initiated and the system becomes available for monitoring through the dashboard, which runs on localhost:8080.

## Results

Clopus-02 ran for a total of 24-hours and generated the following stats:

- _500 projects (single .html files)_

- _~450k LOC_

- _20 long-term memory records_

- _50 short-term memory records_

- _~800k tokens_

- _50 minutes as the longest single session_


And here are some of its creations:

The rest of the apps (~350 more) it created you can find on this link: [02.clopus.live/portfolio](https://02.clopus.live/portfolio)

In terms of behavior, the following can be observed (through the long-term memory system):

The first six records, it recorded what it learned, its process, and hiccups. At this time, Claude Code is focused on doing “something special”, and values its “craft”.

The next 14 records, it shifted its “long-term memory” into setting milestones: 15 projects, 50 projects, 100 projects, 200, 300, 500 projects.

In my personal opinion, this can be explained by the fact it does one thing over and over again — build. It queries its long-term memory, and realizes it has been building, and as such, it shifts its “attention” to milestones.

## Personal thoughts & reflections

This project sparked a child-like fascination with technology in me. One that I had just lost for a while (ironically, due to LLMs). It makes me think just how much potential “autonomous” systems have. While not truly autonomous…

> independent and having the power to make your own decisions
>
> — Cambridge University

…it surely can run for however much time I let it run for. Which includes forever.

While the current quality of work it outputs is not great, this does not stop me from obsessing over upgrading it further and the wide range of use cases it could potentially handle:

- A forever-auditor: An autonomous Claude, constantly evaluating metrics (employee performance / uptime / cloud cost spend / etc.)

- A coding buddy: An autonomous Claude that checks on your commits and pings you on Slack in case it notices something wrong

- Personal assistant: An autonomous Claude that checks on your calendar, email, etc. and talks to you like a real human personal assistant

- A 24/7 trader: An autonomous Claude, trading on 30-min intervals? 2-h intervals?

- Social Media influencer: Need I say more…

- News Bot: Need I say more…

- And so on…


…

My current assumptions on how to make it better are: Better browser use & better master prompt. Morphing “master prompt” coming from the watcher (sent on each loop). Better use of short & long-term memory. Potentially include “goals” (?). Potentially include “emotions” (?). Figure out a way to make interactions possible, but not in the way traditional LLMs expect you to interact (message → response).

There are a lot of ways to go from here. As I previously wrote, I believe terminal agents are still early… and what else can I do but to play around and work towards proving my beliefs into reality.

Thank you for reading :)

— Denis

* * *

#### Subscribe to Denislav Gavrilov

Launched 25 days ago

Welcome to my page. Here you can get to know me, find my resume, discover my projects, and read my writing.

Subscribe

By subscribing, I agree to Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

[![Dl0's avatar](https://substackcdn.com/image/fetch/$s_!evsD!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8790bbae-9730-47b3-ab0f-b3ce7c19a9ba_533x533.jpeg)](https://substack.com/profile/100539760-dl0)[![0xfab.eth's avatar](https://substackcdn.com/image/fetch/$s_!Lxqd!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F97323c01-28b8-4023-a40d-9157316a5745_400x400.jpeg)](https://substack.com/profile/2164546-0xfabeth)[![omar elhassani's avatar](https://substackcdn.com/image/fetch/$s_!NmJp!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa7258170-5e65-4f18-892a-691445cb45ef_612x612.png)](https://substack.com/profile/134186118-omar-elhassani)[![Peter Skaronis's avatar](https://substackcdn.com/image/fetch/$s_!Y7mF!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13924a05-baa3-4caa-a067-c39c477733fd_1024x1026.jpeg)](https://substack.com/profile/18942209-peter-skaronis)[![Mazeyar's avatar](https://substackcdn.com/image/fetch/$s_!MwiF!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F78deb9b5-2547-44ca-b1c9-5eb1859678d1_800x800.jpeg)](https://substack.com/profile/256815215-mazeyar)

25 Likes∙

[4 Restacks](https://substack.com/note/p-182254519/restacks?utm_source=substack&utm_content=facepile-restacks)

25

3

4

Share

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

[![Luca Brizzi's avatar](https://substackcdn.com/image/fetch/$s_!m-ff!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa93bded0-478e-4975-b8ae-045e8d26f731_556x556.jpeg)](https://substack.com/profile/265804495-luca-brizzi?utm_source=comment)

[Luca Brizzi](https://substack.com/profile/265804495-luca-brizzi?utm_source=substack-feed-item)

[6d](https://denislavgavrilov.com/p/clopus-02-a-24-hour-claude-code-run/comment/191801420 "Dec 26, 2025, 5:58 AM") Edited

Liked by Denislav Gavrilov

Impressive automation. It reflects today’s LLM agents: persistent executors. Thanks for sharing

Expand full comment

Like (1)

Reply

Share

[1 reply by Denislav Gavrilov](https://denislavgavrilov.com/p/clopus-02-a-24-hour-claude-code-run/comment/191801420)

[![Akhil's avatar](https://substackcdn.com/image/fetch/$s_!LmV8!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6dd4f933-e68c-4e06-8c29-2a239b7a607a_521x521.jpeg)](https://substack.com/profile/22539139-akhil?utm_source=comment)

[Akhil](https://substack.com/profile/22539139-akhil?utm_source=substack-feed-item)

[8d](https://denislavgavrilov.com/p/clopus-02-a-24-hour-claude-code-run/comment/191487888 "Dec 24, 2025, 11:12 PM")

Liked by Denislav Gavrilov

This is a very interesting experiment. Thanks for sharing your experience. I always wanted to try something similar.. need to explore once.

Expand full comment

Like (1)

Reply

Share

[1 more comment...](https://denislavgavrilov.com/p/clopus-02-a-24-hour-claude-code-run/comments)

TopLatestDiscussions

[Clopus-Watcher: An autonomous monitoring agent](https://denislavgavrilov.com/p/clopus-watcher-an-autonomous-monitoring)

[I put Claude Code in a cronjob in a k8s namespace. It is tasked to monitor an application and in the unfortunate case of application error (degraded…](https://denislavgavrilov.com/p/clopus-watcher-an-autonomous-monitoring)

Dec 27, 2025•[Denislav Gavrilov](https://substack.com/@kuberdenis)

19

1

1

[Clopus-01: A semi-autonomous Claude Code](https://denislavgavrilov.com/p/clopus-01-a-semi-autonomous-claude)

[I attempted to create a fully-autonomous Claude Code. While I did not reach full autonomy, I got pretty close. In this piece I share the stats, how it…](https://denislavgavrilov.com/p/clopus-01-a-semi-autonomous-claude)

Dec 19, 2025•[Denislav Gavrilov](https://substack.com/@kuberdenis)

8

4

[The concept of a Character](https://denislavgavrilov.com/p/the-concept-of-a-character)

[Notes on building a self: Purpose through escapism.](https://denislavgavrilov.com/p/the-concept-of-a-character)

Dec 14, 2025•[Denislav Gavrilov](https://substack.com/@kuberdenis)

2

1

See all

### Ready for more?

Subscribe
