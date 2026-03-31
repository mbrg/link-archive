---
date: '2025-12-13'
description: Halvar Flake's blog post explores enhancing crash triage in C++ using
  Claude, a language model trained to analyze code failures. Initial attempts yielded
  inaccurate results due to LLM hallucinations, but refining the approach led to useful
  insights. The methodology incorporates a dual-agent system where one LLM generates
  hypotheses and another verifies them, emphasizing the importance of detailed documentation
  at each step ("receipts"). This structured approach not only improves accuracy but
  also mitigates the risk of erroneous output, suggesting potential applications for
  complex tasks lacking straightforward validation. For detailed implementation, see
  the GitHub contributions.
link: https://addxorrol.blogspot.com/2025/12/ask-your-llm-for-receipts-what-i.html
tags:
- automated analysis
- reverse engineering
- LLM
- C++
- crash triage
title: 'ADD / XOR / ROL: Ask your LLM for receipts: What I learned teaching Claude
  C++ crash triage'
---

|     |     |     |     |
| --- | --- | --- | --- |
| [Go to Blogger.com](https://draft.blogger.com/ "Go to Blogger.com") | |     |     |
| --- | --- |
|  |  | | MoreShare by emailShare with FacebookShare with TwitterReport Abuse | [Create Blog](https://draft.blogger.com/onboarding) [Sign In](https://draft.blogger.com/) |

# [ADD / XOR / ROL](https://addxorrol.blogspot.com/)

A blog about reverse engineering, mathematics, politics, economics and more ...

## Friday, December 12, 2025

### Ask your LLM for receipts: What I learned teaching Claude C++ crash triage

I recently embarked on a small toy project/experiment: How well can I equip Claude Code to automatically analyze and triage crashes in a C++ code base?

For the experimentation, I worked on a small number of crashes in the ffmpeg bug tracker. The initial results were very discouraging, Claude hallucinated all sorts of implausible root causes and tended to write typical "AI slop" -- things that follow the form of a well-written report, but that had no bearing on reality.

I iterated for a few days, but ultimately I got things to work reasonably well, at least to the point where I was happy with the result.

The result of this little diversion are a bunch of .md files (subagents and skills) that I contributed to [https://github.com/gadievron/raptor](https://github.com/gadievron/raptor) \- specifically the following parts:

[https://github.com/gadievron/raptor/blob/main/.claude/agents/crash-analysis-agent.md](https://addxorrol.blogspot.com/2025/12/goog_336902655)

[https://github.com/gadievron/raptor/blob/main/.claude/agents/coverage-analysis-generator-agent.md](https://addxorrol.blogspot.com/2025/12/goog_336902655)

[https://github.com/gadievron/raptor/blob/main/.claude/agents/function-trace-generator-agent.md](https://addxorrol.blogspot.com/2025/12/goog_336902655)

[https://github.com/gadievron/raptor/blob/main/.claude/agents/crash-analyzer-agent.md](https://addxorrol.blogspot.com/2025/12/goog_336902655)

[https://github.com/gadievron/raptor/blob/main/.claude/agents/crash-analyzer-checker-agent.md](https://github.com/gadievron/raptor/blob/main/.claude/agents/crash-analyzer-checker-agent.md)

and the skills under [https://github.com/gadievron/raptor/tree/main/.claude/skills/crash-analysis](https://github.com/gadievron/raptor/tree/main/.claude/skills/crash-analysis)

The task itself is not necessarily a natural fit for an LLM: I find that LLMs tend to perform better in situations where their results can be immediately verified. This is not the case here - crash triage fundamentally includes a component of "narrative building", and it is not super clear how to validate such a narrative.

There are a few things that I took from my experience in using Claude Code for C++ development in the last year which I applied:

- Since LLMs only perceive the world through text, but their context is a scarce resource, it makes sense to provide them with effective ways of gathering extra data without wasting too much context.
- LLMs will hallucinate arbitrary things but tend to course-correct if their context includes too much data that is obviously in contradiction with their current trajectory.

In my C++ development, I learnt to provide the LLMs with copious amount of conditionally-compiled logging, and ways of running granular tests, so gathering information about what is happening without totally swamping the context window was possible.

Anyhow, what does the crash-analysis-agent end up doing?

1. It gathers a lot of stuff that provides text-level data about what is going on in the program that crashes: A function-level execution trace, gcov data, an ASAN build, and an rr recording that allows deterministic replay of a particular crashing execution.
2. It launches a subagent to then formulate a hypothesis of what is going on. This subagent is instructed to "provide receipts" for each step in the reasoning: Show the precise place where the pointer that ultimately leads to the crashing deref is allocated, show all the modifications, both in the source code **and** in the rr trace. Show all modifications to it, including the pointer values pre/post modification in the rr trace.
3. This hypothesis document is then validated by a separate subagent that is instructed to carefully vet each of the steps in the first document, and reject the file if any evidence is missing. On rejection, a rebuttal is written. This rebuttal is then passed to the previous agent again, until a report is generated that the validator accepts.
4. The final output is a report that includes specific breakpoints, pointer values, pointer modifications etc. that can be manually verified by a human by stepping through the provided rr trace.

In some sense, this is "LLM as a judge", but it appears to me that the usual problem ("generating LLM is convincing enough that the judge LLM waves everything through") is side-stepped by making the judging LLM focus on the formal correctness of the individual steps.

I didn't think much of this, but when I presented this to an audience during the last week, some of the feedback I got was that the technique of "ask the LLM for detailed receipts & have a second LLM validate the receipts" was not necessarily widely known.

So here we are. If you have a task that is perhaps not verifiable on it's final output, but involves verifiable substeps, you can greatly boost performance by providing the LLM with tools/skills to "provide receipts" for the substeps - the final output might still be wrong, but it is so with a much decreased probability.

Posted by
[halvar.flake](https://draft.blogger.com/profile/12486016980670992738 "author profile")
at

[3:17 AM](https://addxorrol.blogspot.com/2025/12/ask-your-llm-for-receipts-what-i.html "permanent link")[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://draft.blogger.com/post-edit.g?blogID=14114712&postID=1848391930076815546&from=pencil "Edit Post")

#### No comments:

[Post a Comment](https://draft.blogger.com/comment/fullpage/post/14114712/1848391930076815546)

[Older Post](https://addxorrol.blogspot.com/2025/07/understand-neural-nets-better-post-5-of.html "Older Post")[Home](https://addxorrol.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://addxorrol.blogspot.com/feeds/1848391930076815546/comments/default)

## Blog Archive

- ▼

[2025](https://addxorrol.blogspot.com/2025/)(7)

  - ▼

     [December](https://addxorrol.blogspot.com/2025/12/)(1)    - [Ask your LLM for receipts: What I learned teaching...](https://addxorrol.blogspot.com/2025/12/ask-your-llm-for-receipts-what-i.html)

  - ►

     [July](https://addxorrol.blogspot.com/2025/07/)(2)

  - ►

     [May](https://addxorrol.blogspot.com/2025/05/)(1)

  - ►

     [April](https://addxorrol.blogspot.com/2025/04/)(2)

  - ►

     [March](https://addxorrol.blogspot.com/2025/03/)(1)

- ►

[2024](https://addxorrol.blogspot.com/2024/)(4)

  - ►

     [December](https://addxorrol.blogspot.com/2024/12/)(1)

  - ►

     [July](https://addxorrol.blogspot.com/2024/07/)(2)

  - ►

     [January](https://addxorrol.blogspot.com/2024/01/)(1)

- ►

[2023](https://addxorrol.blogspot.com/2023/)(1)  - ►

       [December](https://addxorrol.blogspot.com/2023/12/)(1)

- ►

[2021](https://addxorrol.blogspot.com/2021/)(1)  - ►

       [February](https://addxorrol.blogspot.com/2021/02/)(1)

- ►

[2020](https://addxorrol.blogspot.com/2020/)(4)

  - ►

     [September](https://addxorrol.blogspot.com/2020/09/)(1)

  - ►

     [August](https://addxorrol.blogspot.com/2020/08/)(1)

  - ►

     [May](https://addxorrol.blogspot.com/2020/05/)(1)

  - ►

     [March](https://addxorrol.blogspot.com/2020/03/)(1)

- ►

[2019](https://addxorrol.blogspot.com/2019/)(1)  - ►

       [August](https://addxorrol.blogspot.com/2019/08/)(1)

- ►

[2018](https://addxorrol.blogspot.com/2018/)(3)

  - ►

     [October](https://addxorrol.blogspot.com/2018/10/)(1)

  - ►

     [March](https://addxorrol.blogspot.com/2018/03/)(1)

  - ►

     [February](https://addxorrol.blogspot.com/2018/02/)(1)

- ►

[2017](https://addxorrol.blogspot.com/2017/)(1)  - ►

       [August](https://addxorrol.blogspot.com/2017/08/)(1)

- ►

[2016](https://addxorrol.blogspot.com/2016/)(3)

  - ►

     [October](https://addxorrol.blogspot.com/2016/10/)(1)

  - ►

     [September](https://addxorrol.blogspot.com/2016/09/)(1)

  - ►

     [January](https://addxorrol.blogspot.com/2016/01/)(1)

- ►

[2015](https://addxorrol.blogspot.com/2015/)(3)

  - ►

     [December](https://addxorrol.blogspot.com/2015/12/)(2)

  - ►

     [May](https://addxorrol.blogspot.com/2015/05/)(1)

- ►

[2014](https://addxorrol.blogspot.com/2014/)(2)  - ►

       [January](https://addxorrol.blogspot.com/2014/01/)(2)

- ►

[2013](https://addxorrol.blogspot.com/2013/)(3)

  - ►

     [June](https://addxorrol.blogspot.com/2013/06/)(1)

  - ►

     [March](https://addxorrol.blogspot.com/2013/03/)(1)

  - ►

     [January](https://addxorrol.blogspot.com/2013/01/)(1)

- ►

[2012](https://addxorrol.blogspot.com/2012/)(1)  - ►

       [July](https://addxorrol.blogspot.com/2012/07/)(1)

- ►

[2011](https://addxorrol.blogspot.com/2011/)(2)

  - ►

     [September](https://addxorrol.blogspot.com/2011/09/)(1)

  - ►

     [March](https://addxorrol.blogspot.com/2011/03/)(1)

- ►

[2010](https://addxorrol.blogspot.com/2010/)(3)

  - ►

     [March](https://addxorrol.blogspot.com/2010/03/)(1)

  - ►

     [February](https://addxorrol.blogspot.com/2010/02/)(1)

  - ►

     [January](https://addxorrol.blogspot.com/2010/01/)(1)

- ►

[2009](https://addxorrol.blogspot.com/2009/)(17)

  - ►

     [December](https://addxorrol.blogspot.com/2009/12/)(1)

  - ►

     [November](https://addxorrol.blogspot.com/2009/11/)(3)

  - ►

     [October](https://addxorrol.blogspot.com/2009/10/)(1)

  - ►

     [September](https://addxorrol.blogspot.com/2009/09/)(2)

  - ►

     [August](https://addxorrol.blogspot.com/2009/08/)(1)

  - ►

     [July](https://addxorrol.blogspot.com/2009/07/)(4)

  - ►

     [March](https://addxorrol.blogspot.com/2009/03/)(2)

  - ►

     [February](https://addxorrol.blogspot.com/2009/02/)(1)

  - ►

     [January](https://addxorrol.blogspot.com/2009/01/)(2)

- ►

[2008](https://addxorrol.blogspot.com/2008/)(34)

  - ►

     [December](https://addxorrol.blogspot.com/2008/12/)(2)

  - ►

     [November](https://addxorrol.blogspot.com/2008/11/)(5)

  - ►

     [October](https://addxorrol.blogspot.com/2008/10/)(4)

  - ►

     [September](https://addxorrol.blogspot.com/2008/09/)(1)

  - ►

     [July](https://addxorrol.blogspot.com/2008/07/)(8)

  - ►

     [June](https://addxorrol.blogspot.com/2008/06/)(4)

  - ►

     [April](https://addxorrol.blogspot.com/2008/04/)(6)

  - ►

     [March](https://addxorrol.blogspot.com/2008/03/)(2)

  - ►

     [February](https://addxorrol.blogspot.com/2008/02/)(1)

  - ►

     [January](https://addxorrol.blogspot.com/2008/01/)(1)

- ►

[2007](https://addxorrol.blogspot.com/2007/)(17)

  - ►

     [October](https://addxorrol.blogspot.com/2007/10/)(1)

  - ►

     [September](https://addxorrol.blogspot.com/2007/09/)(2)

  - ►

     [August](https://addxorrol.blogspot.com/2007/08/)(3)

  - ►

     [July](https://addxorrol.blogspot.com/2007/07/)(5)

  - ►

     [June](https://addxorrol.blogspot.com/2007/06/)(1)

  - ►

     [April](https://addxorrol.blogspot.com/2007/04/)(1)

  - ►

     [March](https://addxorrol.blogspot.com/2007/03/)(1)

  - ►

     [February](https://addxorrol.blogspot.com/2007/02/)(2)

  - ►

     [January](https://addxorrol.blogspot.com/2007/01/)(1)

- ►

[2006](https://addxorrol.blogspot.com/2006/)(47)

  - ►

     [December](https://addxorrol.blogspot.com/2006/12/)(1)

  - ►

     [November](https://addxorrol.blogspot.com/2006/11/)(4)

  - ►

     [October](https://addxorrol.blogspot.com/2006/10/)(2)

  - ►

     [September](https://addxorrol.blogspot.com/2006/09/)(2)

  - ►

     [August](https://addxorrol.blogspot.com/2006/08/)(3)

  - ►

     [July](https://addxorrol.blogspot.com/2006/07/)(7)

  - ►

     [June](https://addxorrol.blogspot.com/2006/06/)(5)

  - ►

     [May](https://addxorrol.blogspot.com/2006/05/)(8)

  - ►

     [April](https://addxorrol.blogspot.com/2006/04/)(8)

  - ►

     [March](https://addxorrol.blogspot.com/2006/03/)(2)

  - ►

     [February](https://addxorrol.blogspot.com/2006/02/)(4)

  - ►

     [January](https://addxorrol.blogspot.com/2006/01/)(1)

- ►

[2005](https://addxorrol.blogspot.com/2005/)(10)

  - ►

     [December](https://addxorrol.blogspot.com/2005/12/)(4)

  - ►

     [November](https://addxorrol.blogspot.com/2005/11/)(1)

  - ►

     [September](https://addxorrol.blogspot.com/2005/09/)(1)

  - ►

     [August](https://addxorrol.blogspot.com/2005/08/)(4)

|     |     |
| --- | --- |
| ## About Me<br>[halvar.flake](https://draft.blogger.com/profile/12486016980670992738)[View my complete profile](https://draft.blogger.com/profile/12486016980670992738) | ## Links<br>- [Off Convex](https://www.offconvex.org/) |

|     |     |
| --- | --- |
|  |  |

Powered by [Blogger](https://draft.blogger.com/).
