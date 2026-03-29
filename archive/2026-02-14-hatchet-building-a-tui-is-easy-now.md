---
date: '2026-02-14'
description: Hatchet co-founder Alexander Belanger shares insights on an accelerated
  process for developing terminal-based user interfaces (TUIs) using Claude Code,
  a terminal coding agent. Key takeaways include the advantages of TUIs in enhancing
  developer workflows by reducing context-switching and leveraging existing APIs.
  The development utilized the Charm stack, specifically Bubble Tea and Lip Gloss
  for styling. Belanger's approach involved iterative testing with Claude Code, illustrating
  the effectiveness of AI in rapid development cycles. This methodology enabled the
  successful creation of a TUI in just two days, showcasing both the potential of
  coding agents and the simplicity of TUI frameworks. [Live demo here](https://tui.hatchet.run).
link: https://hatchet.run/blog/tuis-are-easy-now
tags:
- developer experience
- terminal-based tools
- coding agents
- TUI
- Charm stack
title: Hatchet · Building a TUI is easy now
---

[Hatchet is hiring! See open roles →](https://www.ycombinator.com/companies/hatchet-run/jobs)

## Building a TUI is easy now

![Alexander Belanger](<Base64-Image-Removed>)Alexander BelangerCo-Founder  · Hatchet

When I first booted up Claude Code in May 2025, I thought: _huh, this is cute. A terminal-based coding agent...they must be pandering to developers._

Within the first 30 minutes, I was convinced: this was going to be huge. So huge that we at Hatchet discussed whether we should build a new product line around terminal-based coding agents.

Ultimately, we decided against it, but that first experience with Claude Code stuck with me. It seems so simple and obvious in hindsight that a terminal-based agent would have a incredibly fast adoption curve among developers.

Perhaps you have a similar feeling that the tool you're working on should have a TUI. Perhaps you've always wanted to build a TUI yourself. Or perhaps you just like saying too-ee.

I say: go for it. It's much easier than I was expecting, using a few neat tricks with Claude Code. This is coming from a skeptic. We had previously attempted an aggressive, agent-first refactor of our frontend which was built in a week, bug-bashed for five, then abandoned.

In comparison, this TUI was mostly driven by Claude Code, but was built and shipped in a few days. You can check it out a live demo here:

🔔

Live demo: [https://tui.hatchet.run](https://tui.hatchet.run/)

For all you budding TUI developers, I wanted to write out some of the decisions that made this significantly easier than similar projects of mine: a “happy path” to building a successful TUI application.

### [Why build a TUI?](https://hatchet.run/blog/tuis-are-easy-now\#why-build-a-tui)

I've always wanted a TUI for Hatchet. Something like [k9s](https://k9scli.io/), but for tasks and workflow runs. I wasn't sure anyone else would find it useful, and we didn't even really announce it to our community, but within a few days we got some very positive, unsolicited feedback from our users. For example:

> Guys great work on the Hatchet CLI (especially the TUI!) It feels so \[much more\] performant than the UI.

I love this comment, because it gets at the heart of why I love TUIs - they just _feel_ easier to use, even though it uses the exact same API as the UI. They're also the opposite of how web applications have been trending the past few years: TUIs are text-first, information-dense, and most importantly, they live inline to your code, preventing constant tab switching. And since our users are primarily developing Hatchet tasks and durable workflows in their IDE, we wanted to provide an experience where workflows could be visualized and run from a terminal, instead of constantly switching between your code and your browser.

### [The stack](https://hatchet.run/blog/tuis-are-easy-now\#the-stack)

Let's get into the details. Every frontend application starts with a stack: A typical one these days might be React, `react-query`, Tailwind, ShadCN, and some additional Tanstack libraries.

There's an equivalent of these libraries for TUI development — and they're all maintained by the same company! I'm referring to the [Charm stack](https://github.com/charmbracelet): if you're unfamiliar, the team at Charm has been building out a set of TUI libraries which are incredibly delightful to use. I primarily used Bubble Tea, Lip Gloss, and Huh. Don't let the cutesy nature of these libraries fool you — they're incredibly well-documented and have tons of examples.

And while I found it slightly more difficult to build anything custom outside of Bubble Tea and Bubbles, it's certainly easier than building a React-based rendering engine [like the one that Claude Code uses internally](https://x.com/trq212/status/2014051501786931427).

One of my favorite bits was the ease at which I could apply a style to any TUI element in a way that felt cohesive using [Lip Gloss](https://github.com/charmbracelet/lipgloss) and [Huh themes](https://pkg.go.dev/github.com/charmbracelet/huh#readme-themes). I then reused this style throughout the Hatchet CLI, instead of just with the TUI. For example, most commands in the Hatchet CLI are interactive by default, with forms that use the Lip Gloss theme:

### [Testing](https://hatchet.run/blog/tuis-are-easy-now\#testing)

The most important piece of testing was Claude Code: it turns out that a terminal-based coding agent is exceptionally good at driving other terminal-based tools. This means that the development process looks something like: build a component or view, compile your TUI, and have Claude Code drive the first pass of testing for it.

I had seen [a comment on Hacker News](https://news.ycombinator.com/item?id=46570397) about using Claude Code to drive a tmux session which uses `tmux capture-pane` to store rendered views and test to make sure they seem correct. This was remarkably effective at driving a first pass of testing, and also ensuring that the proliferation of views continued to render properly (even the Hatchet TUI, which is a relatively simple set of 4 primary views, but contains at least 6 other modals which replace the viewport). Here's what Claude Code "sees" when driving a tmux session:

Historically, my biggest frustration with coding agents for features that involve e2e or frontend testing is the feedback loop. Not in this case: LLMs are built to iterate in ASCII-based environments. After Claude Code drove the first pass of testing, I then manually tested each view along with writing unit tests for anything critical. After a few iterations of this, the TUI ended up in a surprisingly stable place. Iterations felt convergent instead of divergent.

### [Playing on easy mode](https://hatchet.run/blog/tuis-are-easy-now\#playing-on-easy-mode)

Claude Code is much more effective when using a reference implementation. Our reference implementation is our [existing frontend](https://github.com/hatchet-dev/hatchet/tree/main/frontend/app). So most of my instructions for Claude Code referenced an existing and very specific set of frontend views, components or hooks. We don't do anything too crazy in our frontend, and we try to keep our components and views as simple as possible, with business logic and API calls offloaded to various React hooks. This gave Claude Code a very clear boundary of separation to build out each view with business logic first, views second.

We also benefited massively from using an OpenAPI spec to generate our server interfaces and REST API clients, which gave Claude Code a simple reference and auto-generated client to interface with our API.

I initially suspected that the hardest component to build would be the DAG-based renderer. For context, Hatchet is unique in the space of orchestrators in that it supports single tasks, durable execution via durable tasks, _and_ DAG-based execution. Rendering DAGs is a tough problem abstracted for us in our frontend by the fantastic [React Flow](https://reactflow.dev/) which handles a bunch of the complexity around rendering DAGs and graphs properly:

![DAG view in the Hatchet UI](https://hatchet.run/assets/dag_ui-BsvOigmG.png)

DAG view in the Hatchet UI

It didn't seem tractable to transpile the React Flow internals to the TUI, so I tried a different approach. I went through a few failed iterations of prompting Claude Code to build this before I decided to dig into it. I searched online for existing implementations of ASCII-based graph renderers and stumbled upon [https://github.com/AlexanderGrooff/mermaid-ascii](https://github.com/AlexanderGrooff/mermaid-ascii). I cloned this repository, pointed Claude Code at it, wrote several paragraphs of a prompt, and got it to render a _working_ DAG renderer within the first try.

It's not quite pixel-perfect, but it's getting there.

### [The result](https://hatchet.run/blog/tuis-are-easy-now\#the-result)

All told, this took about 2 days of effort. Notably this was the first time I felt that using Claude Code for something non-arbitrary was significantly faster than doing it myself. The aforementioned frontend refactor fiasco bore all the hallmarks of agentic antipattern: incredibly fast to get something extremely promising working, then losing the plot in a wave of complexity and bugs caused by subtle bugs upon subtle bugs. A house of cards. We reverted the frontend changes after a difficult pre-turned-postmortem.

This was a big shift for me: releasing a major feature, which has been working reliably for me with aggressive usage over the past few weeks, driven by a coding agent. While we're not going full [yolo mode](https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/) with our agents any time soon, we're gradually using them more and more, particularly for less-critical paths (if your TUI crashes, it hopefully doesn't bring down your production. This is not true of your queueing system).

Perhaps the lessons are a little boring and intuitive to more experienced engineers: building an environment with a tight feedback loop, modular design, proper specifications, continuous testing and deployment, yada yada. But I finally feel like I'm in the loop.

Linking the live demo again here, would love to hear your feedback!

🔔

Live demo: [https://tui.hatchet.run](https://tui.hatchet.run/)

#### Subscribe for more technical deep dives

Stay updated with our latest work on distributed systems, workflow engines, and developer tools.

Subscribe
