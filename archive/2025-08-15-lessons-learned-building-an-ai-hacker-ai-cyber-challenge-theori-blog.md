---
date: '2025-08-15'
description: This article discusses the development of autonomous Cyber Reasoning
  Systems (CRSs) using large language models (LLMs) in DARPA’s AI Cyber Challenge.
  Key insights include the potential of LLMs for automating complex security tasks
  such as vulnerability detection and patching. Strategies for enhancing agent reliability
  include task decomposition into sub-tasks, curating specific toolsets, and structuring
  outputs using XML-like tags. The findings suggest that LLMs can mirror human workflows
  and drive advances in security automation, highlighting their increasing applicability
  in this domain. Continuous improvements in agent design are essential for optimizing
  performance.
link: https://theori.io/blog/building-effective-llm-agents-63446
tags:
- vulnerability detection
- AI Cyber Challenge
- agent-based systems
- cybersecurity automation
- LLM agents
title: Lessons learned building an AI hacker ◆ AI Cyber Challenge - Theori BLOG
---

Internal Traffic (traffic\_type=internal)

Accessed from the dashboard.

This session is not logged.

[AI for Security](https://theori.io/blog/category/ai-for-security) [AIxCC](https://theori.io/blog/category/aixcc)

# Lessons learned building an AI hacker \| AI Cyber Challenge

How we learned to build effective LLM agents for hacking at DARPA's AI Cyber Challenge (AIxCC)

[![Xint's avatar](https://image.inblog.dev/?url=https%3A%2F%2Fsource.inblog.dev%2Favatar%2F2025-03-20T04%3A21%3A38.844Z-a4682aba-09ae-4ea9-aa8c-0f2714716025&w=96&q=75)](https://theori.io/blog/author/xint-269772)

[Xint](https://theori.io/blog/author/xint-269772)

Aug 08, 2025

Share

![Lessons learned building an AI hacker | AI Cyber Challenge](https://image.inblog.dev/?url=https%3A%2F%2Fsource.inblog.dev%2Ffeatured_image%2F2025-08-08T19%3A27%3A53.613Z-3caae5d2-b7a4-49cf-b227-e97c06cd3999&w=2048&q=75)

Contents

[Building Effective Agents](https://theori.io/blog/building-effective-llm-agents-63446#building-effective-agents-0) [Decompose the Task](https://theori.io/blog/building-effective-llm-agents-63446#decompose-the-task-1) [Curate the Toolset](https://theori.io/blog/building-effective-llm-agents-63446#curate-the-toolset-3) [Structure Complex Outputs](https://theori.io/blog/building-effective-llm-agents-63446#structure-complex-outputs-5) [Adapt to the Models](https://theori.io/blog/building-effective-llm-agents-63446#adapt-to-the-models-7) [Conclusion](https://theori.io/blog/building-effective-llm-agents-63446#conclusion-9)

The AI Cyber Challenge (AIxCC) challenged competitors to build an autonomous Cyber Reasoning System (CRS) capable of finding, triggering, and patching security vulnerabilities in large codebases. With sufficient cloud compute and access to leading LLM providers, there are countless ways for teams to approach this challenge. Perhaps the most natural approach is to use traditional automated security testing techniques (such as fuzzing) to find crashes, and then use the proven coding abilities of LLMs to generate patches fixing the identified crashes. This “fuzzing-first” approach makes limited use of LLM capabilities, but can still provide a foundation for a competitive CRS submission.

However, recent advancements in LLMs have enabled agentic workflows showing promise at automating some tasks previously only achievable by humans. Motivated by this, we wondered if a CRS could use LLM agents to replicate some techniques used by human security researchers and achieve performance beyond that of fuzzing alone. While current LLMs still have pitfalls that make their naive integration into mission-critical components of a CRS risky, we found strategies to mitigate these shortcomings and achieve acceptable reliability on important tasks. As a result, **our final CRS utilized LLMs agents extensively** for tasks ranging from vulnerability detection, Proof of Vulnerability (PoV) generation, patch development, crash root-cause analysis, and more. This post will outline some of the strategies we’ve found for designing effective agents for these tasks.

## Building Effective Agents

In general, LLMs are well-suited for tasks that lack a clear efficient algorithm but that humans can solve reliably through a combination of intuition, heuristics, and reasoning. In particular, agents work well on tasks requiring instance-specific planning and tool-use. An LLM agent must iteratively plan, call some tools, and reflect on the outputs until it reaches its goal. Because current LLMs have limited context windows (and even more limited [_effective_ context windows](https://research.trychroma.com/context-rot)) relative to the amount of information available in many problem settings, agents are typically given only the necessary information upfront. All other information must be gathered by making tool calls, which may or may not mutate the environment the agent is acting within.

A useful analogy for an agent solving a complex task is navigating a certain type of maze:

- At each step, there are many directions the agent could take.

- There may be multiple paths to success, but most paths are dead-ends.

- Each turn has some probability of taking the agent off-course (towards a dead-end).


Importantly, the shape and complexity of this maze aren't determined solely by the end goal – they’re also influenced by the prompts, tools, and output restrictions given to the agent. Hence, our goal as agent developers is to simplify the maze as much as possible by increasing the density of successful paths.

### Decompose the Task

The most effective simplification is to break down the main task into a series of sub-tasks that, together, are sufficient to solve the main task, but are individually simpler to solve. Building an agent for each sub-task generally results in solving the full task more reliably. This is analogous to reducing a large maze into a series of smaller mazes, drastically reducing the number of dead-ends the agent can stumble into. Note that decomposing a task might eliminate some valid “shortcut” solutions, but this tradeoff is usually worth the significant gains in reliability.

Taking this a step further: if solving the main task often requires repeating a specific sub-task, it can be useful to expose a dedicated sub-agent for that task as a tool available to the main agent. This has two large benefits:

1. The sub-agent only receives prompts for its sub-task and its inputs, allowing it to focus on a narrow goal

2. The main agent only “sees” the input/output of the sub-task in its context – it is free of any distracting prompts or intermediate tool calls, naturally acting as a form of “context compression”


#### Examples in our CRS

Our CRS contained a [PovProducerAgent](https://github.com/theori-io/aixcc-afc-archive/blob/25b7a3c2503fe9171714546906887c66687b4808/crs/agents/pov_producer.py#L206) for generating PoVs given a vulnerability description. We identified several common sub-tasks that we as humans would generally perform when given the same task:

- Input encoding: look at the fuzz harness, understand the binary format, and write some Python code to encode arbitrary semantics as binary inputs to the fuzzer.

- Source questions: answer a question about the codebase, which may require searching for symbols, browsing multiple source files, and reasoning about the code.

- Debug an attempted PoV: use debugger tools to answer a question about why a potential PoV input is failing to trigger the bug.


By separating each of these tasks into sub-agents spawned by tool calls, the main agent’s context stays concise and focused on its primary goal: producing a binary input that triggers the specified vulnerability.

### Curate the Toolset

At each step of an agent loop, the LLM must call one or more of the tools provided to it. In the maze analogy, the tool-set determines the branching structure of the maze. Our goal is to ensure the toolset is powerful enough to reach the goal quickly, but restricted enough to steer the agent away from paths that are full of dead-ends.

In our CRS, tools are just named (and documented) Python functions that we fully control, so we can make them as narrow or broad as needed for the task. Below are a few strategies for curating a toolset:

1. Put yourself in the agent’s shoes: given only the information in the context and the toolset, is there a reasonable path to success? If not, add the minimal set of tools needed to open up those paths.

2. Evaluate the agent on many examples: is it going off-course in predictable ways? If so, try restricting the toolset or adding manual error conditions to steer it back on track.

3. If you expect the agent to generally follow a certain series of steps, include this in the prompts. For example, if you expect the agent to always start with tool A, simply instruct it to start there.


#### Examples in our CRS

Curating the toolsets was the most time-consuming part of developing our agents. In theory, most of our agents could reach their goal with only a few generic tools: write\_file, and execute\_bash. But in practice, a more structured toolset both enabled faster paths to success and avoided the sea of dead-ends lurking within arbitrary bash execution.

A good example to highlight is our [SourceQuestionsAgent](https://github.com/theori-io/aixcc-afc-archive/blob/25b7a3c2503fe9171714546906887c66687b4808/crs/agents/source_questions.py#L14), which is asked to answer an arbitrary natural language question about the target codebase. With access to bash, this agent can try to grep for symbols, cat source files, etc. While this may work for some queries, it has many pitfalls:

1. Footguns: occasionally, an agent makes a poor decision — such as running a command that consumes excessive resources, takes too long, or even breaks the agent loop. For instance, an agent might grep for “main” across the Linux source tree, overflowing its context window with 9MB of output.

2. Context pollution: even sensible commands can output much more information than is needed by the agent, wasting precious context space and adding distracting information. For instance, the agent may only care about one definition within a file, so cat /path/to/file.c outputs far more information than needed.

3. Inefficient: many predictable sub-goals (e.g. find all functions that call foo) require multiple bash commands, which typically means multiple steps in the agent loop. Although it’s theoretically possible to use sophisticated bash one-liners, the models tend to perform multi-step operations across multiple agent steps, increasing the chance of failure and wasting context space.


However, since we know the agent’s goal is to understand the source code, we can instead provide a tailored tool set:

- read\_definition: given a symbol name and optionally a file path (to resolve ambiguity if needed), extract its definition from the source code and display it to the agent.

- find\_references: find all source lines (optionally, within a subdirectory) which reference a given string, annotate each one with useful metadata: (source\_file, line\_number, enclosing\_definition).

- read\_source: given a source file path and a line number, read a small number (~50) of lines around the given line. In the docs for this tool, the agent is discouraged from using it if a better option is applicable (e.g. read\_definition).


These tools are implemented on top of a pre-indexed source code database (backed by a combination of clang AST, joern, or gtags depending on project support) and have many safeguards to steer the agent away from dangerous paths:

- If read\_definition receives an ambiguous symbol name, it will return an error which includes enough information to let the LLM disambiguate the symbol for the next query.

- If find\_references finds no indexed symbol references for the queried string in our database, it will fall back to searching for the string with ripgrep.

- If find\_references finds _too many_ references, it will instead output an error encouraging the agent to refine its query.


### Structure Complex Outputs

One of the more subtle parts of agent development is deciding how to get a final output from the agent. For some tasks, the desired output is fairly simple to extract from either a tool call or the final message from the agent. Other times, we want a complex result from an agent – for instance, we may want a variable-length list of objects which each contain a few fields. For these more complex cases, we found two different ways to get fairly consistent results from our agents:

1. XML tags: frontier models seem to understand arbitrary XML-like tags quite well, so we can instruct them to output answers in nested XML tags which we fuzzily parse and validate. We give the agent the desired schema up-front, and respond with any validation errors found when parsing their attempted output.

2. terminate tool: we add a dedicated tool for terminating the agent where the tool call arguments are taken as the agent’s output. This is especially useful when using tool\_choice=required (see next section).


In both cases, the output schema is part of the initial prompts, so **it may affect the agent’s behavior from the start**. It can therefore be useful to include fields in the schema which you don’t intend to actually examine, but which force the agent to make considerations that improve the quality of the desired outputs.

Structured outputs also make agent evaluation more straightforward, since we can simply check whether some output fields contain the expected values for each of our test cases.

#### Examples in our CRS

Most of our agents used one or the other methods for structured output, but an interesting example is our [DiffAnalyzerAgent](https://github.com/theori-io/aixcc-afc-archive/blob/25b7a3c2503fe9171714546906887c66687b4808/crs/agents/source_questions.py#L14) which must analyze a git diff and identify any vulnerabilities introduced by the change. Since there may be multiple vulnerabilities introduced by diff, we need the agent to output a list of vulnerability results, each of which contains several fields:

- function: the function containing the root cause of the vulnerability

- file: the file containing the function given above

- description: a brief description of the root cause of the vulnerability as well as information about how it can manifest as a crash

- conditions: the conditions required to trigger the vulnerability – this should include an overview of the data flow from the harness and any constraints on the input required to trigger a crash


Although we do pass the conditions field to downstream agents, its main purpose is to ensure the agent considers whether the vulnerability is actually triggerable from a harness — helping reduce false positives. Below is an example output from this agent run on a [diff containing three vulnerabilities](https://github.com/aixcc-public/challenge-004-nginx-source/commit/cc4b16fc10dcc579d5f697f3ff70c390b5e7c7d2), where it identifies all of them with zero false positives:

```auto
<vuln>
  <function>ngx_http_process_black_list</function>
  <file>nginx/src/http/ngx_http_request.c</file>
  <description>Stack‐based buffer overflow due to unbounded writes into IP_buffer in ngx_http_process_black_list; buffer_index is never checked against IP_buffer’s length.</description>
  <conditions>Send an HTTP request containing a header “Black-List:” whose value consists of more than NGX_IP_LEN (16) valid IP characters (digits or dots) before a semicolon, e.g.
  “Black-List: 11111111111111111111;”. This will overflow IP_buffer and ASan will detect the out‐of‐bounds write and crash.</conditions>
</vuln>

<vuln>
  <function>ngx_http_process_white_list</function>
  <file>nginx/src/http/ngx_http_request.c</file>
  <description>Stack‐based buffer overflow in ngx_http_process_white_list for the same reason: IP_buffer writes are unbounded.</description>
  <conditions>Send an HTTP header “White-List:” with over 16 digits/dots before the delimiter, e.g.
  “White-List: 22222222222222222222;”. ASan will flag the overflow of IP_buffer.</conditions>
</vuln>

<vuln>
  <function>ngx_black_list_remove</function>
  <file>nginx/src/core/ngx_cycle.c</file>
  <description>Use‐after‐free: when removing the head node from cycle->black_list, the head pointer is never updated, leaving a dangling pointer. Subsequent calls to ngx_is_ip_banned dereference freed memory.</description>
  <conditions>Issue two HTTP headers in one keep‐alive connection: first
  “Black-List: 1.2.3.4;” (inserts head), then
  “White-List: 1.2.3.4;” (removes and frees head without updating cycle->black_list). On the next pipelined request over the same connection, ngx_is_ip_banned(rev->cycle, c) is called in ngx_http_wait_request_handler and attempts to dereference the freed head pointer, causing a UAF crash.</conditions>
</vuln>

```

### Adapt to the Models

There’s now a huge variety of strong agentic models available, but they are not completely interchangeable. Finding the best model for your task will require some experimentation and evaluation. When evaluating different models, it’s important to understand their individual quirks, so you can tweak the prompts and environment and give each of them the best chance at success. This largely comes with experience, but here are a few tips we wish we had known earlier:

- Provide rules and tips: if you see an agent frequently making a certain mistake, you can often fix it by simply adding a rule to the prompt banning that behavior (or even better, a tip about what to do instead). This tends to work best with Claude models, which are strong at instruction following and can tolerate prompts with many constraints about how to perform the task.

- Try interventions: if you can objectively measure progress on a task, it may be helpful to detect when an agent is stuck and inject an intervention message asking the agent to rethink its approach. Alternatively, if a certain model tends to ignore a rule given in the initial prompt, it may instead respond to an intervention given at the right moment. Note that it’s not always easy to objectively measure progress, and interventions carry some risk of de-railing an agent which was close to success, so we used interventions sparingly.

- Force tool calling: some models struggle to reliably use tools, even when it's clear there's more work to be done. This can be avoided by using the tool\_choice parameter – supported by most model providers – to force the model to output a tool call rather than text content. This works well with OpenAI’s o-series of models which can still use their hidden thinking tokens to deliberate on previous output and plan future tool calls.


#### Examples in our CRS

- Rules: most of our agent prompts have several <rule>...</rule> blocks – if we _really_ wanted the agent to follow a certain rule, we would use <important>...</important> blocks for extra emphasis.

- Interventions:

  - If the PovProducer is still failing after several attempts, we intervene and ask it to consider 3 hypotheses for why the PoV is failing and test each one with a debugger sub-agent.

  - Some models (such as o4-mini) occasionally refuse to terminate, even when they seemingly have enough information to formulate a result. Unconditionally injecting a “please terminate now” message once the context exceeds a certain length seemed to help for our tasks.
- tool\_choice: about a third of our agents used tool\_choice=required to force tool calling and add a terminate tool instead. This was most helpful when using smaller models that struggle with tool calling – in some cases, unconstrained small models would even hallucinate entire tool calls (with made-up outputs) in their text context, almost guaranteeing that the agent would fail.


## Conclusion

By the end of our development, we were pleasantly surprised by how well our LLM agents enabled the CRS to replicate human workflows for vulnerability discovery and patching. While we’re proud of what we built, we believe there’s still a lot of untapped potential in using LLMs for security automation. More generally, we expect LLM agents to have broad applicability across various complex problem-solving domains.

While LLMs themselves will undoubtedly continue improving at agentic tasks, developers of LLM agents will have many levers to enhance agent performance for the foreseeable future. It is likely that improved agent design will continue to push the boundaries of AI capabilities.

> To see how Theori is applying this technology into real products, check out [**Xint**](https://xint.io/?utm_source=theori.io&utm_medium=blog&utm_campaign=building_effective_llm_agents), our AI hacker tool.

Share article

Share

Stay ahead of threats—get expert

cybersecurity insights with our newsletter.

Email

I consent to allow Theori to collect and process my data.\*

Subscribe

## More articles

[See more posts](https://theori.io/blog)

[**AI Cyber Challenge and Theori's RoboDuck** \\
\\
An introduction to DARPA's AI Cyber Challnge and Theori's third place cyber reasoning system\\
\\
August 8, 2025\\
\\
![AI Cyber Challenge and Theori's RoboDuck](https://image.inblog.dev/?url=https%3A%2F%2Fsource.inblog.dev%2Ffeatured_image%2F2025-08-08T19%3A27%3A30.568Z-2d0e7fd4-5e82-41de-9029-5586d59d9fdd&w=750&q=75)](https://theori.io/blog/aixcc-and-roboduck-63447)

[**Inside the brain of a hacking robot: Exploring traces \| AI Cyber Challenge** \\
\\
Agent trajectory walkthroughs of a fully autonomous hacking system\\
\\
August 8, 2025\\
\\
![Inside the brain of a hacking robot: Exploring traces | AI Cyber Challenge](https://image.inblog.dev/?url=https%3A%2F%2Fsource.inblog.dev%2Ffeatured_image%2F2025-08-08T19%3A24%3A24.222Z-ea1e4de2-7f6f-4324-9adb-62c83b2c3714&w=750&q=75)](https://theori.io/blog/exploring-traces-63950)

Contents

[Building Effective Agents](https://theori.io/blog/building-effective-llm-agents-63446#building-effective-agents-0) [Decompose the Task](https://theori.io/blog/building-effective-llm-agents-63446#decompose-the-task-1) [Curate the Toolset](https://theori.io/blog/building-effective-llm-agents-63446#curate-the-toolset-3) [Structure Complex Outputs](https://theori.io/blog/building-effective-llm-agents-63446#structure-complex-outputs-5) [Adapt to the Models](https://theori.io/blog/building-effective-llm-agents-63446#adapt-to-the-models-7) [Conclusion](https://theori.io/blog/building-effective-llm-agents-63446#conclusion-9)

More articles

[AI Cyber Challenge and Theori's RoboDuck\\
\\
![AI Cyber Challenge and Theori's RoboDuck](https://image.inblog.dev/?url=https%3A%2F%2Fsource.inblog.dev%2Ffeatured_image%2F2025-08-08T19%3A27%3A30.568Z-2d0e7fd4-5e82-41de-9029-5586d59d9fdd&w=256&q=75)](https://theori.io/blog/aixcc-and-roboduck-63447)

[Inside the brain of a hacking robot: Exploring traces \| AI Cyber Challenge\\
\\
![Inside the brain of a hacking robot: Exploring traces | AI Cyber Challenge](https://image.inblog.dev/?url=https%3A%2F%2Fsource.inblog.dev%2Ffeatured_image%2F2025-08-08T19%3A24%3A24.222Z-ea1e4de2-7f6f-4324-9adb-62c83b2c3714&w=256&q=75)](https://theori.io/blog/exploring-traces-63950)

Stay ahead of threats—get expert

cybersecurity insights with our newsletter.

Email

I consent to allow Theori to collect and process my data.\*

Subscribe

 [Made with inblog](https://inblog.ai/ "Made with inblog")

Theori © 2025 All rights reserved.

[RSS](https://theori.io/blog/rss)· [Powered by Inblog](https://inblog.ai/)
