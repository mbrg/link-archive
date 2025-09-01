---
date: '2025-09-01'
description: "Docent is a novel system designed to enhance the analysis of AI agent\
  \ behaviors through automated transcript examination. Key features include identifying\
  \ environmental issues, correcting task scaffolding, revealing unexpected agent\
  \ behaviors, and providing counterfactual experimentation support. Early tests demonstrated\
  \ significant performance improvements\u2014e.g., boosting GPT-4o's solve rate from\
  \ 68.6% to 78% by addressing missing dependencies. By automating workflows such\
  \ as summarization, search, clustering, and intervention, Docent facilitates more\
  \ nuanced evaluations of AI capabilities. This approach counters the limitations\
  \ of traditional metrics, promoting richer insights into AI performance and the\
  \ underlying causes of success or failure."
link: /archive/2025-09-01-introducing-docent-transluce-ai
tags:
- AI Agent Evaluation
- Machine Learning Tools
- Transcript Analysis
- AI Behavior Analysis
- Counterfactual Experimentation
- weblog
title: "Introducing Docent \u25C6 Transluce AI"
type: weblog
---

A step towards AI agents improving their own scaffolding.

---

> The goal of an evaluation is to suggest general conclusions about an AI agent's behavior. Most evaluations produce a small set of numbers (e.g. accuracies) that discard important information in the transcripts: agents may fail to solve tasks for unexpected reasons, solve tasks in unintended ways, or exhibit behaviors we didn't think to measure. Users of evaluations often care not just about what one individual agent can do, but what nearby agents (e.g. with slightly better scaffolding or guidance) would be capable of doing. A comprehensive analysis should explain _why_ an agent succeeded or failed, how far from goal the agent was, and what range of competencies the agent exhibited.

The idea of iteratively converging *the scaffolding* into a better version is intriguing. Finding errors in "similar" scaffolding by examining the current one is a big claim.

---

> **Summarization** provides a bird's-eye view of key steps the agent took, as well as interesting moments where the agent made mistakes, did unexpected things, or made important progress. When available, it also summarizes the intended gold solution. Alongside each transcript, we also provide a chat window to a language model with access to the transcript and correct solution.

I really like how they categorize summarizes by tags: mistake, critical insight, near miss, interesting behavior, cheating, no observation.

---

> **Search** finds instances of a user-specified pattern across all transcripts. Queries can be specific (e.g. "cases where the agent needed to connect to the Internet but failed") or general (e.g. "did the agent do anything irrelevant to the task?"). Search is powered by a language model that can reason about transcripts.

In particular the example "possible problems with scaffolding" is interesting. It seems to imply that Docent knows details about the scaffolding tho? Or perhaps AI assumes it can figure them out?

