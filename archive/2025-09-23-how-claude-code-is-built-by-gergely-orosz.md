---
date: '2025-09-23'
description: Claude Code, an AI-driven development tool by Anthropic, has rapidly
  gained traction, achieving over $500M in annual revenue since its release. Built
  using TypeScript, React, and a streamlined architecture leveraging the Claude AI
  model, Claude Code enables quick prototyping, releasing around five features daily.
  Key innovations include a redefined command-line interface and an advanced permission
  system, allowing secure local file interaction. The tool empowers engineers by increasing
  productivity, evident from a 67% improvement in pull request throughput as team
  size doubled. Claude Code exemplifies the shift towards AI-first development workflows,
  fundamentally changing software engineering practices.
link: https://newsletter.pragmaticengineer.com/p/how-claude-code-is-built
tags:
- Software Development
- Machine Learning
- Code Prototyping
- Tech Stack
- AI
title: How Claude Code is built - by Gergely Orosz
---

[![The Pragmatic Engineer](https://substackcdn.com/image/fetch/$s_!6TJt!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5ecbf7ac-260b-423b-8493-26783bf01f06_600x600.png)](https://newsletter.pragmaticengineer.com/)

# [The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/)

SubscribeSign in

[Deepdives](https://newsletter.pragmaticengineer.com/s/deepdives/?utm_source=substack&utm_medium=menu)

# How Claude Code is built

### A rare look into how the new, popular dev tool is built, and what it might mean for the future of software building with AI. Exclusive.

[![Gergely Orosz's avatar](https://substackcdn.com/image/fetch/$s_!CPFa!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F58fed27c-f331-4ff3-ba47-135c5a0be0ba_400x400.png)](https://substack.com/@pragmaticengineer)

[Gergely Orosz](https://substack.com/@pragmaticengineer)

Sep 23, 2025

∙ Paid

1

[View comments (0)](https://newsletter.pragmaticengineer.com/p/how-claude-code-is-built/comments)

Share

Claude Code has taken the developer world by storm since being made generally available in May. The tool is currently generating more than $500M in annual run-rate revenue, and usage has exploded by more than 10x in the three months since that May release.

I recently sat down with two of the founding engineers behind Claude Code: [Boris Cherny](https://www.threads.com/@boris_cherny) (the engineer who came up with the original prototype, and the founding engineer of the project), [Sid Bidasaria](https://x.com/sidbidasaria) (engineer #2 of Claude Code, and creator of Claude Code subagents), and founding product manager [Cat Wu](https://x.com/_catwu).

I learned how Claude Code is built, and got insights into how a successful “AI-first engineering team” operates; it was a bit like a peek into a crystal ball and a potential future of how fast-moving startups will operate. The good news is that software engineers appear _very much_ in demand in it…

Today, we cover:

1. **How it all began.** The idea for Claude Code came from a command-line tool using Claude to state what music an engineer was listening to at work. It spread like wildfire at Anthropic after being given access to the filesystem. Today, Claude Code has its own fully-fledged team.

2. **Tech stack and architecture.** TypeScript, React, Ink, Yoga, and Bun. The tech stack was chosen to be “on distribution” and to play to the strengths of the model. Fun fact: 90% of code in Claude Code is written by itself!

3. **Building and shipping features in days – not weeks**. The team is working at rapid pace, with around 5 releases per engineer each day. Prototyping is done surprisingly quickly: we go through 10+ actual prototypes for a new feature. _It looks like AI agents really speed up iteration._

4. **Redesigning the terminal UX.** Claude Code brings a lot of innovative features to the terminal user experience that weren’t needed before we could interact with terminals powered by LLMs. A look at some of them.

5. **What “AI-first” software engineering looks like.** Using AI agents for code reviews and tests, test-driven development’s (TDD) renaissance, automating incident response, and cautious use of feature flags. Does this presage how “AI-first” engineering teams will work in the future?

6. **Building subagents.** A walk through how the subagents feature was built in just three days, of which two days’ work was thrown away.

7. **Future of AI-assisted engineering teams?** What engineering teams can learn from how Anthropic operates, and things to keep in mind about what makes it unique, that might be less transferable.


_Other, related deepdives from the [real-world engineering challenges series](https://newsletter.pragmaticengineer.com/t/real-world-engineering-challenges):_

- _[Real-world engineering challenges: building Cursor](https://newsletter.pragmaticengineer.com/p/cursor)_

- _[How Anthropic built Artifacts](https://newsletter.pragmaticengineer.com/p/how-anthropic-built-artifacts)_

- _[Scaling ChatGPT: five real-world engineering challenges](https://newsletter.pragmaticengineer.com/p/scaling-chatgpt)_


## 1\. How it all began

Boris Cherny joined Anthropic in September 2024, and began building a bunch of different prototypes with the Claude 3.6 model. At the time, he wanted to get more familiar with Anthropic’s public API. Boris recalls that period:

> “I started hacking around using Claude in the terminal. The first version was barebones: it couldn't read files, nor could it use [bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)), and couldn’t do any engineering stuff at all. But it could interact with the computer.
>
> **I hooked up this prototype to AppleScript**: it could tell me what music I was listening to while working. And then it could also change the music playing, based on my input.
>
> This was a cool demo, but wasn’t that interesting”.

Meanwhile, Cat Wu was researching the computer usage of AI agents, and new capabilities that arose from agents using them. Following a conversation with Cat, Boris had the idea to give the terminal more capabilities than just using AppleScript. He says:

> “I tried giving it some tools to interact with the filesystem and to interact with the batch; it could read files, write files, and run batch commands.
>
> Suddenly, this agent was _really_ interesting. I ran it in our codebase, and just started asking questions about it. Claude then started exploring the filesystem and reading files. So, it would read one file, look at the imports, then read the files that were defined in the imports! It went on, until it found a good answer. Claude exploring the filesystem was mindblowing to me because I’d never used any tool like this before.
>
> **In AI, we talk about “product overhang”, and this is what we discovered with the prototype.** Product overhang means that a model is able to do a specific thing, but the product that the AI runs in isn’t built in a way that captures this capability. What I discovered about Claude exploring the filesystem was pure product overhang. The model could already do this, but there wasn’t a product built around this capability!”

### Product-market fit

Boris started to use his prototype every day at work. He then shared it with what would become the core Claude Code team, and fellow devs started to use it daily, too.

Boris and the Claude Code team released a dogfooding-ready version in November 2024 – two months after the first prototype. On the first day, around 20% of the Engineering team used it, and by day five, 50% of Engineering was using Claude Code. At that point, Boris felt pretty confident Claude Code could be a hit in the outside world.

**But there was internal debate about whether to even release the tool**, or to keep it for internal use. Boris recounts:

> “We actually weren't even sure if we wanted to launch Claude Code publicly because we were thinking it could be a competitive advantage for us, like our “secret sauce”: if it gives us an advantage, why launch it?
>
> In the end, this is the position we landed on:
>
> - Anthropic, at its core, is a model safety company
>
> - The way we learn about model safety and capabilities is that we make tools people use
>
> - Claude Code would _almost certainly_ be a tool people use because all of Anthropic got hooked on it
>
>
> So by releasing this tool, we learn a lot more about model safety and capabilities.”

### Assembling the Claude Code engineering team

Initially, the team was just Boris until in November, Sid Bidasaria joined Anthropic and came across the early version of Claude Code. He liked the idea and joined Boris on the project.

There was a lot of freedom in how their two-person team worked. Sid told me:

> “Most of what we did was prototype _really_ quickly and build products that showcase how strong the underlying model is. We didn’t have formal processes inside the team: it was all super fluid. We could work on pretty much whatever we wanted, and so we just kept choosing the most promising ideas."

The team grew to around 10 engineers by July, and hiring has continued since. Today, it’s a full-fledged product team with engineers, Product Management, Design, and Data Science folks – and they’re [still hiring](https://www.anthropic.com/jobs).

### Claude Code not only for coders

Today, more than 80% of Anthropic’s engineers who write code use Claude Code day-to-day, but it’s not only them. Boris:

> “I was walking into the office and glanced at the screen of a data scientist. He had Claude Code running. I was like, “hold on, why do you have Claude Code running?” He says: “I figured out how to get this thing running and write queries for me.”
>
> These days when I walk by the row of data scientists, they all have Claude Code running – many of them have several instances– running queries, creating visualizations, and doing other types of helpful work”.

An interesting point is that Boris only ever had software engineers in mind for Claude Code – hence the name! – but the product has shown it has further utility in other areas.

### More engineering output while doubling team size

If we take the metric of pull requests per engineer; when an engineering team doubles in size quickly this process usually pulls down the metric. This is because existing engineers spend more time onboarding new colleagues and less time coding, and new joiners need to get the hang of things at first. _Like any metric, pull requests (PR) per engineer are not a perfect metric, but it does give a sense of the pace of iteration. PR throughput is [measured by companies](https://newsletter.pragmaticengineer.com/p/how-tech-companies-measure-the-impact-of-ai) including GitHub, Dropbox, Monzo, Adyen, and others._

**But Anthropic saw a 67% increase in PR throughput as their team size doubled – thanks to Claude Code.** It would have been normal for the average-PRs-merged metric to drop, but it actually went up! The credit for this is given to Claude Code: engineers get PRs done faster with it. In what might have been a lucky constellation of events, Anthropic doubled its engineering headcount at around the time that Claude Code was adopted across all of engineering.

I’ve also noticed that finishing a piece of work with Claude Code is considerably faster, and that I make better progress on my coding tasks with the tool. It also helps when I build stuff for which Claude Code can verify the correctness of the code, by running the program and checking outputs or running tests.

## 2\. Tech stack and architecture

Claude Code’s tech stack:

- **TypeScript**: Claude Code is built on this language

- **React with Ink:** the UI is written in React, using the [Ink](https://github.com/vadimdemedes/ink) framework for interactive command-line elements

- **[Yoga](https://www.yogalayout.dev/):** the layout system, open sourced by Meta. It’s a constraints-based layout that works nicely. Terminal-based applications have the disadvantage of needing to support all sizes of terminals, so you need a layout system to do this pragmatically

- **[Bun](https://bun.com/)**: for building and packaging. The team chose it for speed compared to other build systems like Webpack, Vite, and others.


The Ink framework is a neat component that allows for creating pleasant-looking UIs in the terminal. For example, to create this UI:

[![](https://substackcdn.com/image/fetch/$s_!C9m-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8add9d90-de56-4efd-b755-f483d61cfb10_538x228.gif)](https://substackcdn.com/image/fetch/$s_!C9m-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8add9d90-de56-4efd-b755-f483d61cfb10_538x228.gif)

You can write the code in React:

[![](https://substackcdn.com/image/fetch/$s_!rEIp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2cf6d0b7-3d0f-4e8a-9c9a-f8f3b62f0712_1024x748.png)](https://substackcdn.com/image/fetch/$s_!rEIp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2cf6d0b7-3d0f-4e8a-9c9a-f8f3b62f0712_1024x748.png) _The code for a counter that updates in the console. Source: [Ink on GitHub](https://github.com/vadimdemedes/ink)_

**npm** is used for distributing Claude Code. It’s the most popular package manager in the Node ecosystem. To get started with Claude Code, you need to have Node 18-or-above installed, then run:

npm install -g @anthropic-ai/claude-code

Once that’s done, you can start the tool with the _Claude_ command.

**The tech stack was chosen to be “on distribution” for the Claude model.** In AI, there are the terms “on distribution” and “off distribution.” “On distribution” means the model already knows how to do it, and “off distribution” means it’s not good at it.

The team wanted an “on distribution” tech stack for Claude that it was already good at. TypeScript and React are two technologies the model is very capable with, so were a logical choice. However, if the team had chosen a more exotic stack Claude isn’t that great with, then it would be an “off distribution” stack. Boris sums it up:

> “With an off-distribution stack, the model can still learn it. But you have to show it the ropes and put in the work. We wanted a tech stack which we didn't need to teach: one where Claude Code could build itself. And it’s working great; around 90% of Claude Code is written with Claude Code”.

### Architecture: choose the simplest option

Interestingly, there’s not all that much to Claude Code in terms of modules, components, and complex business logic on the client side. For a tool that does pretty complex things like traversing filesystems and codebases, this is somewhat surprising! But Claude Code is just a lightweight shell on top of the Claude model. This is because the model does almost all of the work:

- Defines the UI, and exposes hooks for the model to modify it

- Exposes tools for the models to use

- … then gets out of the way


**The Claude Code team tries to write as little business logic as possible.** Boris tells me:

> “This might sound weird, but the way we build this is we want people to _feel_ the model as _raw_ as possible. We have this belief the model can do much more than products today enable it to do.
>
> When you look at a lot of coding products, they get in the way of the model; they add scaffolding by adding UI elements and other parts that clutter things, so that the model running in those tools feels like it’s hobbling on one foot. Features that are meant to be helpful for users end up limiting the model. So, we try to make the UI as minimal as possible.
>
> **Every time there’s a new model release, we delete a bunch of code.** For example, with the 4.0 models, we deleted around half the system prompt because we no longer needed it. We try to put as little code as possible around the model, and this includes minimizing prompting and minimizing the number of tools. We constantly delete tools and experiment with new ones”.

**Claude Code does not use virtualization – it runs locally.** A major design decision was whether to run Claude Code in a virtual machine – like on a Docker container, or in the cloud – and thereby create a sandbox environment. But the team decided to go with a version that runs locally because: simplicity! From Boris:

> “With every design decision, we almost always pick the simplest possible option. What are the simplest answers to the questions: “where do you run batch commands?” and “where do you read from the filesystem?” It’s to do it locally.
>
> So we went with this: Claude Code runs batch commands locally, and reads and writes to the filesystem. There’s no virtualization”.

### The permissions system

The most complex part of Claude Code is the permissions system. The risk of running Claude Code locally is that an agent may do irreversible things that it shouldn’t, such as deleting files. But how can this be done securely?

Again, the team has opted for simplicity and built a permissions system that seeks permission before executing an action. The user can then decide to:

- Grant the permission once

- Grant the permission for future sessions, as well

- Reject the permission


[![](https://substackcdn.com/image/fetch/$s_!YlQN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4baf7543-7874-4fee-9d6b-1569af794535_1310x472.png)](https://substackcdn.com/image/fetch/$s_!YlQN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4baf7543-7874-4fee-9d6b-1569af794535_1310x472.png) _Claude Code seeking permission before deleting a file_

Boris tells me that getting permissions right took effort:

> “Our most important principle is this: if you start running Claude Code, it shouldn't change things on your system without permission. That could be dangerous.
>
> However, we should also give ways for people to opt out and say things like “actually, in the context I’m working in, I’d like to not give permission every time.”
>
> There’s a lot of nuance in the permissions system, though. For example, when a command comes in, we do static analysis on them to check if this is something already allowed in the settings file (in the settings.json file).
>
> **The settings system is a multi-tiered system that can be configured per project, per user, and per company.** You can also share settings with your team. We are observing teams share settings files that whitelists commands so that Claude Code won’t ask for permission, such as checking into source control”.

### Other features

Claude Code is simple in some ways, but has dozens of features which add to its complexity. Several are [documented](https://docs.claude.com/en/docs/claude-code/quickstart). Some to note:

- [Hooks](https://docs.claude.com/en/docs/claude-code/hooks-guide): create custom shell commands for Claude Code to use

- [MCP support](https://docs.claude.com/en/docs/claude-code/mcp): give Claude Code more capabilities by connecting it to MCP servers. See our deepdive on the Model Context Protocol (MCP)

- [GitHub](https://docs.claude.com/en/docs/claude-code/github-actions) and [GitLab](https://docs.claude.com/en/docs/claude-code/gitlab-ci-cd) support: use GitHub Actions and integrate Claude Code into GitLab CI/CD.

- [Output styles](https://docs.claude.com/en/docs/claude-code/output-styles): the ability to switch to output styles, or define your own. Built-in output styles you can switch to include:

  - Explanatory: educating you about implementation choices

  - Learning: a collaborative style where Claude asks you to do small tasks yourself. A very clever approach to stay in the loop, hands-on, and learn! It could be a great way for less experienced engineers to learn, or for those unfamiliar
- [Configuration](https://docs.claude.com/en/docs/claude-code/settings): use a variety of config files and settings to configure your terminal, model, status line, and many more

- [Subagents](https://docs.claude.com/en/docs/claude-code/sub-agents): covered below

- Enterprise features: [set up](https://docs.claude.com/en/docs/claude-code/iam) Identity and Access Management (IAM) to use Claude Code across an organization, and access [org-wide analytic](https://docs.claude.com/en/docs/claude-code/analytics) s to track usage

- [Claude Code SDK](https://docs.claude.com/en/docs/claude-code/sdk/sdk-overview): build custom AI agents, using the agent harness that powers Claude Code

- … and see this roundup of [recent new features in Claude Code](https://x.com/claudeai/status/1967998397136408954)


## 3\. Building and shipping features in days, not weeks

For a team of around a dozen engineers, they work _really_ fast:

**~60-100 internal releases/day.** Any time an engineer makes a change to Claude Code, they release a new npm package internally. Everyone at Anthropic uses the internal version and the dev team gets rapid feedback.

Over the summer, engineers pushed around 5 pull requests per day – a much faster pace than at most tech companies where 1-2 pull requests per day are often the norm.

**1 external release/day.** Almost every day, a new version of the package is released as part of a deployment.

### 20 prototypes in 2 days: building todo lists

What surprises me about this development is that the team does a lot more prototyping with Claude Code than I’m used to seeing. As an example, Boris walked me through how he built around 20 prototypes of the new feature, todo lists, in a few hours over two days.

He was kind enough to share the actual prompts he used for the various iterations. After each one, Boris:

- Sometimes tweaked the result

- Played around with it

- If it felt good, shared it with colleagues for feedback

- When something felt off, he built a new prototype with a new prompt


#### Prototype \#1: showing todos as they are completed

Idea: todo lists are one of the easiest ways to keep track of how Claude is doing, so they tried having the list just below the most-recent tool call.

Prompt:

> \> make it so instead of todos showing up as they come in, we hide the tool use and result for todos, and render a fixed todo list above the input. title it "/todo (1 of 3)" in grey

How it looked:

[![](https://substackcdn.com/image/fetch/$s_!y-m6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F534bd2bd-b75c-4fdf-92cb-cafec6896142_1600x963.png)](https://substackcdn.com/image/fetch/$s_!y-m6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F534bd2bd-b75c-4fdf-92cb-cafec6896142_1600x963.png) _Prototype #1_

#### Prototype \#2: showing progress at the bottom

Another variation was showing each todo update in line.

Prompt:

> \> actually don't show a todo list at all, and instead render the tool used inline, as bold headings when the model starts working on a todo. keep the "step 2 of 4" or whatever, and add middot /todo to see after in grey

How it looked:

[![](https://substackcdn.com/image/fetch/$s_!ii2j!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6e5cc77-f18b-4caa-9332-0010a088e06d_1600x1047.png)](https://substackcdn.com/image/fetch/$s_!ii2j!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6e5cc77-f18b-4caa-9332-0010a088e06d_1600x1047.png) _Prototype #2_

#### Prototypes \#3 and \#4: an “interactive pill”

What if the todos were an interactive pill (a rectangle at the bottom of the console) that you could pull up to see progress on, just like background tasks?

Prompts and outputs:

> \> also add a todo pill under the text input, similar to bg tasks. it should render "todos: 1 of 3" or whatever

[![](https://substackcdn.com/image/fetch/$s_!P6K-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff30813e3-2f45-4db5-8e18-80248e1e2b42_1600x887.png)](https://substackcdn.com/image/fetch/$s_!P6K-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff30813e3-2f45-4db5-8e18-80248e1e2b42_1600x887.png) _Prototype #3_

> \> make the pill interactive, like the bg tasks pill

[![](https://substackcdn.com/image/fetch/$s_!k0dz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F47388481-89df-4a5b-ab92-0fca56c3c031_1600x970.png)](https://substackcdn.com/image/fetch/$s_!k0dz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F47388481-89df-4a5b-ab92-0fca56c3c031_1600x970.png) _Prototype #4_

#### Prototypes \#5 and \#6: using a “drawer”

What if we had a ‘drawer’ that slid in with the todos on the side?

Prompts and outputs:

> \> actually undo both the pill and headings. instead, make the todo list render to the right of the input, vertically centered with a grey divider. show it when todos are active, hide it when it's done

[![](https://substackcdn.com/image/fetch/$s_!uJwE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc384016f-5a99-44d6-807a-1366b0da73e8_1600x689.png)](https://substackcdn.com/image/fetch/$s_!uJwE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc384016f-5a99-44d6-807a-1366b0da73e8_1600x689.png) _Prototype #5, with todos as a “drawer” on the right. See [the animated version](https://www.threads.com/@boris_cherny/post/DOJ7j1yEinY?xmt=AQF0ng_THawLvtKm-2ybaug10RNNwXP8l8I2TfS20BW2Vg)_

> \> it's a little jumpy, can you also animate it like a drawer

[![](https://substackcdn.com/image/fetch/$s_!2dM2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13423c9d-49fd-4cf8-b3ec-e63fd8d564bb_1600x597.png)](https://substackcdn.com/image/fetch/$s_!2dM2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13423c9d-49fd-4cf8-b3ec-e63fd8d564bb_1600x597.png) _Prototype #6. See [the animated version](https://www.threads.com/@boris_cherny/post/DOJ7j1yEinY?xmt=AQF0ng_THawLvtKm-2ybaug10RNNwXP8l8I2TfS20BW2Vg)_

#### Prototypes \#7, \#8 and \#9: experiments on visibility

To make the todo list as visible as possible, Boris tried making it always show above the input.

Prompts and outputs:

> \> actually what if you show the todo list above the input instead

[![](https://substackcdn.com/image/fetch/$s_!QWzS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1291426d-a32a-410f-9ae1-4f0c234c7863_1600x988.png)](https://substackcdn.com/image/fetch/$s_!QWzS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1291426d-a32a-410f-9ae1-4f0c234c7863_1600x988.png) _Prototype #7_

> \> truncate at 5 and show "... and 4 more" or whatever

[![](https://substackcdn.com/image/fetch/$s_!xBeu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcfe013cf-c070-416d-8e19-86f152dddf37_1600x884.png)](https://substackcdn.com/image/fetch/$s_!xBeu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcfe013cf-c070-416d-8e19-86f152dddf37_1600x884.png) _Prototype #8_

> \> add a heading "Todo:" in grey text

[![](https://substackcdn.com/image/fetch/$s_!3n7F!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f16c120-a1e1-435f-8724-b7a970bd9376_1600x967.png)](https://substackcdn.com/image/fetch/$s_!3n7F!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f16c120-a1e1-435f-8724-b7a970bd9376_1600x967.png) _Prototype #9_

#### Prototypes \#10-20: moving the spinner UI element

Boris kept playing with where the todo list visibility should live, and after several more prototypes. In the end, Boris moved the to-do lists to the spinner which maximized visibility, and started to feel good. After a few iterations, they had the version that they ended up shipping in public.

[![](https://substackcdn.com/image/fetch/$s_!CKPP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa61e4589-1063-4582-b3df-2e0c4d5c3721_1600x793.png)](https://substackcdn.com/image/fetch/$s_!CKPP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa61e4589-1063-4582-b3df-2e0c4d5c3721_1600x793.png) _At around prototype #20, after playing with visibility and the spinner_

#### One more iteration

The team got a lot of feedback from the community that they wanted to be able to see all the todos. So the team added the ability to toggle them with CTRL + T. And this is what’s live today!

[![](https://substackcdn.com/image/fetch/$s_!czTW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F15b62a32-6063-4073-81df-cf11b0db85bb_1600x782.png)](https://substackcdn.com/image/fetch/$s_!czTW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F15b62a32-6063-4073-81df-cf11b0db85bb_1600x782.png) This iteration (around #21 or so) is currently in production – pressing Tab toggles the list of steps executing

**Building and testing 5-10 prototype ideas in a day is possible with AI agents.** Prototyping used to be so time consuming that if there were two days to prototype, it was lucky to have two distinct prototypes built by the end. But now, agents can build prototypes very quickly, so tests of 5-10 prototypes per day are easily done, as the Claude Code team did.

I don’t suggest everyone can build that many prototypes so quickly, but I think it’s sensible to forget about how long prototyping used to take: these tools change how fast prototyping can be!

_A lot of this prototyping was about making the UI “feel good:” You can see the animated prototypes [in this thread](https://www.threads.com/@boris_cherny/post/DOJ5SiCkxG1). I suggest watching the videos of the prototype steps for a sense of how the feature evolved, and how Boris kept trying new ideas to narrow it down to how the todo list looks inside the tool today._

## 4\. Redesigning the terminal UX

Claude Code has a lot of fresh ideas from the team because this is the first time the terminal is really interactive, thanks to an LLM responding to each command. A few examples:

## This post is for paid subscribers

[Subscribe](https://newsletter.pragmaticengineer.com/subscribe?simple=true&next=https%3A%2F%2Fnewsletter.pragmaticengineer.com%2Fp%2Fhow-claude-code-is-built&utm_source=paywall&utm_medium=web&utm_content=174356873)

[Already a paid subscriber? **Sign in**](https://substack.com/sign-in?redirect=%2Fp%2Fhow-claude-code-is-built&for_pub=pragmaticengineer&change_user=false)
