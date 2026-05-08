---
date: '2026-05-08'
description: In a recent analysis of coding-agent behaviors, team at Entire examined
  search efficiency using traces from real-world agent interactions. They compared
  `ripgrep`, `fff`, and `pgr` across benchmarks to assess the impact on agentic code
  search. They found that while improving search speed (as seen with `fff`) led to
  modest gains, better-ranked results (via `pgr`) significantly enhanced first-query
  relevance. This indicates that improved ranking is crucial for rapid code discovery
  but that overall efficiency gains may not manifest uniformly across tasks. Future
  work aims to expand benchmarks and explore advanced retrieval models.
link: https://entire.io/blog/improving-agentic-search-in-coding-agents
tags:
- search_efficiency
- ranking_systems
- AI_agents
- code_search
- benchmarking
title: How We Improved Agentic Search · Entire
---

## TL;DR

We analyzed real coding-agent traces, built public benchmarks, and compared `ripgrep`, [`fff`](https://github.com/dmtrKovalenko/fff), and [`pgr`](https://github.com/entireio/pgr) to see what actually improves agentic code search. The clearest result was that faster search alone only modestly helps, while better-ranked results improve first-query retrieval and help agents find the right code sooner.

## How Do Agents Search?

If you watch a coding agent work, one thing becomes obvious very quickly: it spends a lot of time searching for files, symbols, definitions, references, test cases, imports, call sites, and more. Search is not a side operation in the agent loop; it is one of the main things the agent does.

![Agent trace animation](https://entire.io/blog/improving-agentic-search-in-coding-agents/agent_trace_animation.svg)

At [Entire](https://www.entire.io/), we capture AI agent traces and make them searchable and shareable across agents and teammates. We call each trace a **checkpoint**. It contains the user prompts, agent responses, tool calls, and the resulting code diffs. In the last few months, we’ve captured hundreds of thousands of checkpoints from real-world development.

We are building code and semantic search infrastructure that will be capable of efficiently searching billions of checkpoints. Search itself is not a new problem. Tools like `grep`, `ripgrep`, `fzf`, and `fff` are already quite fast locally. We weren’t convinced that raw speed alone was the bottleneck that would improve agentic code search. So we set out to test it.

To figure out what did matter, we pulled checkpoints that were generated during real-world development from our open source [Entire CLI](https://github.com/entireio/cli) repo for analysis. No customer data was used. You can find the source data [here](https://github.com/entireio/pgr/blob/main/public_release/data/entireio_cli_checkpoints_2026_04_15/summary.json).

Here’s what that public dataset looks like:

- **Total checkpoints analyzed:**`1,983`
- **Total tool calls analyzed:**`202,142`
- **Search-related tool calls:**`98,555` (`48.8%` of all tool calls)

Diving deeper on the search-related tool calls:

![Agent tool call breakdown](https://entire.io/blog/improving-agentic-search-in-coding-agents/tool_calls_breakdown.svg)

| Category | Count | Percentage |
| --- | --- | --- |
| Read / file retrieval | 48,322 | 49.0% |
| Bash search fallback | 23,180 | 23.5% |
| Grep / content search | 23,136 | 23.5% |
| Other | 3,917 | 4.0% |

In the **Grep / content search** category, the agent used a dedicated content-search tool like grep to search file contents directly, usually for symbols, strings, or regex patterns. In the **Bash search fallback** category, the agent used general shell commands to do search-like work such as `grep`, `find`, `ls`, shell pipelines, existence checks, and file discovery commands.

In other words, Bash search fallback is broader and messier. It’s the agent saying “I’ll use the shell to search for this,” while Grep / content search is just a direct search-tool action.

This initial analysis told us two things immediately:

1. **Search is a first-order operation of agent behavior.** Nearly half of all tool calls were search-related.
2. **The search workflow is fragmented.** Agents bounce between file reads, bash-based search, and grep-style content search, which suggests there is room for a better default search surface than raw `ripgrep` output in whatever order it happens to come back.

After the initial analysis, it was time to dig in deeper.

## Faster Search Wasn’t the Bottleneck

Before trying to improve search quality, we tested a simpler hypothesis: maybe coding agents just needed faster search execution.

So we tested it directly, with a dedicated public benchmark around a 60-task search-sensitive suite pulled from real public `entireio/cli` checkpoints. The [benchmark package](https://github.com/entireio/pgr/blob/main/public_release/benchmarks/entireio_cli_fff_vs_baseline_public60/README.md) is here.

These were not handwritten eval prompts. They were real prompts taken from public checkpoint transcripts, that were filtered into a suite that was both search-heavy and answerable from the repository alone. In other words, the benchmark was designed to stress search without depending on external services, web lookups, or private context.

We evaluated two conditions:

- **baseline:** raw `ripgrep`
- **fff:** a stateful MCP search server built around a bigram index, `mmap`, SIMD-accelerated scanning, and frecency ranking

`fff` is much faster than `ripgrep`, so if raw search latency were the real bottleneck, that should have translated into dramatically faster end-to-end agent runs.

It only translated into a modest improvement.

On this 60-task public benchmark, `fff` drove median `search_code` latency from `14.7ms` down to `1.7ms`, but end-to-end wall clock only moved from `38.57s` to `36.99s`. The full [summary](https://github.com/entireio/pgr/blob/main/public_release/benchmarks/entireio_cli_fff_vs_baseline_public60/SUMMARY.md) is here.

| Metric | Baseline (`ripgrep`) | `fff` |
| --- | --- | --- |
| Avg wall clock per run | 38.57s | 36.99s |
| Avg tool calls | 19.12 | 17.90 |
| Avg total tool execution time per run | 0.140s | 0.055s |
| Tool execution share of wall clock | 0.4% | 0.1% |
| Avg `search_code` duration | 15.5ms | 5.7ms |
| Median `search_code` duration | 14.7ms | 1.7ms |

![Speed benchmark comparison](https://entire.io/blog/improving-agentic-search-in-coding-agents/speed_benchmark.svg)

Yes, faster search helped a little. But even with a large tool-level speedup, the end-to-end effect was modest because tool execution was only a tiny fraction of total runtime to begin with. On this benchmark, actual tool execution accounted for just `0.4%` of wall clock for baseline and `0.1%` for `fff`.

The agent was not spending most of its time waiting for `ripgrep`. It was spending most of its time in the much slower loop around the tools:

![Agent loop bottleneck](https://entire.io/blog/improving-agentic-search-in-coding-agents/agent_loop_bottleneck.svg)

Once you look at the system that way, the result becomes much less surprising. Driving a search call from tens of milliseconds down to sub-millisecond latency is progress at the tool layer, but it barely matters if each call still sits inside seconds of model inference, result interpretation, and next-step planning.

In order to have the same effect as removing one inference step, let’s estimate that at a 2-second roundtrip, you would have to shave roughly `330ms` off each of six search calls, or drive on the order of `130` baseline-latency searches all the way to zero.

So then the question became:

> How do we make each search result more useful to the agent so it stops thrashing and moves into reading code sooner?

To test this question, we built our own local search tool called `pgr`.

![Search surface comparison](https://entire.io/blog/improving-agentic-search-in-coding-agents/search_surface_comparison.svg)

## The Systems We Tested

We ended up comparing three systems.

### 1\. Baseline: raw `ripgrep`

This was the control. The agent used the same four-tool interface we defined for the benchmark, but `search_code` was backed by plain `ripgrep` with minimal post-processing. Results came back in roughly the order `ripgrep` produced them, with no ranking layer on top.

This condition answers the simplest question:

> What does agent search behavior look like with a strong, standard local search tool and no extra intelligence?

### 2\. `fff`: faster indexed search

`fff` is a stateful MCP search server built around a bigram index, `mmap`, SIMD-accelerated scanning, and frecency ranking. It is engineered for raw speed. If raw search speed were the main bottleneck, `fff` should have produced a dramatically better end-to-end result.

It was useful in the study for exactly that reason: it gave us a way to separate scan speed from search usefulness.

### 3\. `pgr`: ranked, agent-oriented search

`pgr` is the search tool we built for agents.

It keeps the simplicity of local code search, but changes what the agent sees first:

- definitions first
- source files before tests and vendor
- grouped and trimmed output
- richer result presentation designed to make the next step clearer

![pgr demo animation](https://entire.io/blog/improving-agentic-search-in-coding-agents/pgr_demo_animation.svg)

If you want to see what `pgr` actually looks like as an MCP server, the interface is deliberately simple. It speaks JSON-RPC over stdio: initialize the server, list the available tools, and then call `search_code`.

```
$printf '%s\n' \
  '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{}}' \
  '{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}' \
  '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"search_code","arguments":{"query":"CheckpointStore","max_files":5}}}' \
  | ~/.cargo/bin/pgr
```

During development, we iterated on both ranking and output formatting. The public benchmarks below report the final `pgr` configuration rather than a version-by-version ablation.

## Why These Conditions Mattered

Taken together, these systems let us test a few different hypotheses:

- Does faster search help?
- Does better ranking help?
- Does agent-oriented result presentation help?

That is why the benchmark stack ended up being so important. Different systems were improving different parts of the loop, and a single aggregate metric was not enough to tell them apart.

## The Benchmark Stack

Once we had multiple systems to compare, the next question was how to evaluate them. At first, we expected a single end-to-end benchmark to be enough: give the agent the same tasks, swap out the search backend, and measure tool calls, cost, and wall clock. In principle, that is exactly the metric we want. In practice, it was not enough on its own.

One quick note: In our benchmark harness, the agent searches the repository through a single tool interface called `search_code`, which we back with different search systems.

```
{
  "name": "search_code",
  "arguments": {
    "query": "CheckpointStore",
    "max_files": 5
  }
}
```

So when we talk about “first search\_code queries” or “search\_code latency,” we mean the same abstract code-search tool call evaluated under different backends, not a separate product or model capability.

For this public release, the benchmark stack ended up with three layers:

1. **Speed benchmark**

Measure whether dramatically faster search execution translates into faster end-to-end runs.

2. **Broad mixed-workload benchmark**

Run the full agent loop end-to-end across many prompts, then measure tool calls, cost, and wall clock.

3. **Offline retrieval benchmark**

Replay real `search_code` queries from agent traces against different backends and score retrieval quality directly, without letting the agent continue.


Each layer answers a different question, and together they tell a much clearer story than any one metric on its own.

## Starting Simple

We started by predicting that if we gave the agent a search tool that returned better-ranked results, we could see downstream improvements resulting in better search results, fewer searches, fewer tool calls and lower cost.

So we started with a smaller end-to-end pilot before scaling up. The benchmark package is [here](https://github.com/entireio/pgr/blob/main/public_release/benchmarks/entireio_cli_ranking_public60/README.md).

### Early Pilot

The pilot used the first 25 tasks from the public `entireio/cli` suite. We tested `baseline`, `fff`, `pgr` on the same 4-tool interface for each condition using Claude Sonnet as the agent.

The full pilot results are [here](https://github.com/entireio/pgr/blob/main/public_release/benchmarks/entireio_cli_ranking_public60/pilot25/SUMMARY.md).

| Metric | Baseline | `fff` | `pgr` |
| --- | --- | --- | --- |
| Avg wall clock | 38.21s | 36.25s (-5.1%) | 36.88s (-3.5%) |
| Avg tool calls | 20.20 | 20.00 (-1.0%) | 20.92 (+3.6%) |
| Avg cost | $0.5581 | $0.4161 (-25.4%) | $0.4824 (-13.6%) |
| Avg search calls | 8.04 | 7.64 (-5.0%) | 6.56 (-18.4%) |

That was encouraging, but not definitive. Both alternatives reduced search counts and improved average wall clock versus baseline. `fff` showed the largest cost drop, while `pgr` reduced search calls the most. But neither variant reduced the total tool calls.

So we scaled it up.

## Study 1: Broad Mixed-Workload Benchmark

The larger public benchmark expanded the same setup to the full public suite of 60-tasks:

- **60 tasks total**
- **1 public repository:**`entireio/cli`
- **4 prompt categories:**`code_understanding`, `debug_or_validation`, `implementation`, `repo_task`
- **same 4-tool interface for each condition**
- **Claude Sonnet as the agent**

The conditions were:

- **baseline:** raw `ripgrep`
- **fff:** a stateful indexed MCP search server optimized for speed
- **pgr:** Rust MCP search tool

Full results [here](https://github.com/entireio/pgr/blob/main/public_release/benchmarks/entireio_cli_ranking_public60/full60/SUMMARY.md):

| Metric | Baseline | `fff` | `pgr` |
| --- | --- | --- | --- |
| Avg wall clock | 34.98s | 34.97s (-0.0%) | 33.67s (-3.8%) |
| Avg tool calls | 18.45 | 18.72 (+1.4%) | 18.90 (+2.4%) |
| Median tool calls | 21.0 | 21.0 | 22.0 |
| Avg cost | $0.4030 | $0.3797 (-5.8%) | $0.3698 (-8.2%) |
| Avg search calls | 6.12 | 5.70 (-6.8%) | 5.53 (-9.5%) |

`fff` slightly reduced search calls but left wall clock essentially flat and slightly increased tool calls. `pgr` was the most promising of the group, with fewer searches and modest improvements in both wall clock and cost, but even there the total tool-call count did not go down.

The larger benchmark told us something more nuanced:

1. Better search was probably changing some local agent decisions.
2. Those changes were not large or stable enough to produce a single clean aggregate headline across all end-to-end metrics.

### Why the Broad Benchmark Washed Out

Task variance was still high. Some prompts produced a short, direct search-read-answer path. Others branched into much longer exploratory trajectories with extra searches, extra reads, or more backtracking. That variance was often large enough to distort or erase a clean aggregate signal.

In other words, the broad benchmark still answered an important question:

> Does this intervention survive realistic end-to-end workloads?

But it still did not answer the more diagnostic question:

> What part of the agent loop is this intervention actually improving?

That distinction ended up mattering a lot.

The broad benchmark did not prove that search quality was irrelevant. It proved that aggregate agent behavior is noisy enough that local improvements can disappear, or show up only partially, if you only measure the final total.

That is what led to the next benchmark layer.

## Experiment 1: Offline Retrieval Quality

After the broad benchmark turned out to be mixed, we still had a strong intuition that ranking could help. The problem was that the full end-to-end metric was too noisy to isolate what the search layer itself was doing.

So the next step was to remove the agent from the loop and evaluate retrieval directly.

We built an offline replay benchmark from the baseline runs of the `entireio/cli` suite. The benchmark package is [here](https://github.com/entireio/pgr/blob/main/public_release/benchmarks/entireio_cli_offline_ir_public60/README.md):

The method was:

1. Extract real `search_code` queries from the baseline agent traces
2. Replay those same queries against different search backends
3. Score the returned files against a public relevance signal

We used the files the baseline agent actually opened with `read_code` in that run as a relevance label. This benchmark is much narrower than the broad mixed-workload study, but it answers a more precise question:

> For the exact same query, which backend returned better candidates?

![Retrieval example](https://entire.io/blog/improving-agentic-search-in-coding-agents/retrieval_example.svg)

We ran two versions:

- **first-search replay:** only the first `search_code` query from each run
- **pre-read replay:** all `search_code` queries before the baseline agent first opened code

### Experiment 1A: First-Search Replay

This was the cleanest retrieval benchmark in the study.

- **Query set:** 50 first-search queries
- **Groups:** 50 runs from 50 tasks
- **Conditions:**`baseline`, `fff`, `pgr`
- **Source files:** [first\_search/SUMMARY.md](https://github.com/entireio/pgr/blob/main/public_release/benchmarks/entireio_cli_offline_ir_public60/first_search/SUMMARY.md), [first\_search/results.json](https://github.com/entireio/pgr/blob/main/public_release/benchmarks/entireio_cli_offline_ir_public60/first_search/results.json)

We measured four things:

- **MRR (Mean Reciprocal Rank):** how high the first relevant file appears in the result list, with earlier hits rewarded much more heavily
- **Hit@1:** how often the top result is relevant
- **Hit@3:** how often a relevant result appears in the top 3
- **Avg output chars:** how much search output was returned, which acts as a rough proxy for response size and token burden

| Metric | Baseline | `fff` | `pgr` |
| --- | --- | --- | --- |
| MRR | 0.3177 | 0.3059 | 0.4053 |
| Hit@1 | 26.0% | 18.0% | 34.0% |
| Hit@3 | 34.0% | 42.0% | 42.0% |
| Avg output chars | 6565.9 | 1427.0 | 1587.1 |

![First-search retrieval metrics](https://entire.io/blog/improving-agentic-search-in-coding-agents/first_search_metrics.svg)

Paired by task (`N = 50`):

- **MRR `fff` vs baseline:**`-0.012`, 95% CI `[-0.089, +0.066]`
- **MRR `pgr` vs baseline:**`+0.088`, 95% CI `[-0.007, +0.182]`
- **Hit@1 `fff` vs baseline:**`-8.0` points, 95% CI `[-17.7, +1.7]`
- **Hit@1 `pgr` vs baseline:**`+8.0` points, 95% CI `[-4.7, +20.7]`

`fff` is the useful contrast case. It was the fastest search system we tested, but it did not improve first-result relevance in the way `pgr` did. It still often surfaced a relevant file somewhere near the top of the list, but it was less likely to put that file first.

This is one of the clearest results in the project:

**Definition-first, path-aware ranking improved the quality of the first search result the agent saw.**

### Where the Gain Was Strongest

The gains were larger on prompts where the agent had to navigate uncertainty rather than simply confirm a single obvious definition.

The strongest first-search gains showed up on **implementation** prompts, where the agent is usually trying to find the main file or code path to inspect next:

- **MRR:**`0.3061 -> 0.5000`
- **Hit@1:**`14.3% -> 42.9%`

Those prompts tend to leave a lot of room for better ranking to matter, because the right file is often buried among helpers, tests, or neighboring implementations.

On **code\_understanding** prompts, the gain was smaller but still directionally positive:

- **MRR:**`0.2760 -> 0.3260`
- **Hit@1:**`20.0% -> 24.0%`

That makes intuitive sense. Some of these prompts already start from a decent baseline query, while others are much more exploratory.

![Gains by task type](https://entire.io/blog/improving-agentic-search-in-coding-agents/gains_by_task_type.svg)

### Experiment 1B: Pre-Read Replay

The broader replay benchmark used every `search_code` query the baseline agent issued before it first opened code.

In other words, instead of measuring only the first search, this benchmark measured the unresolved search phase: all the queries the agent tried while it was still looking for the right place to read.

- **Query set:** 132 searches before first read
- **Groups:** 42 runs from 42 tasks
- **Conditions:**`baseline`, `fff`, `pgr`
- **Source files:** [pre\_read/SUMMARY.md](https://github.com/entireio/pgr/blob/main/public_release/benchmarks/entireio_cli_offline_ir_public60/pre_read/SUMMARY.md), [pre\_read/results.json](https://github.com/entireio/pgr/blob/main/public_release/benchmarks/entireio_cli_offline_ir_public60/pre_read/results.json)

| Metric | Baseline | `fff` | `pgr` |
| --- | --- | --- | --- |
| MRR | 0.2271 | 0.1764 | 0.2640 |
| Hit@1 | 17.4% | 10.6% | 22.0% |
| Hit@3 | 24.2% | 23.5% | 28.8% |
| Avg output chars | 2225.7 | 978.7 | 1449.4 |

![Pre-read retrieval metrics](https://entire.io/blog/improving-agentic-search-in-coding-agents/pre_read_metrics.svg)

Paired by task (`N = 42`):

- **MRR `fff` vs baseline:**`-0.048`, 95% CI `[-0.115, +0.019]`
- **MRR `pgr` vs baseline:**`+0.067`, 95% CI `[-0.007, +0.141]`
- **Hit@1 `fff` vs baseline:**`-11.6` points, 95% CI `[-21.5, -1.7]`
- **Hit@1 `pgr` vs baseline:**`+5.1` points, 95% CI `[-4.1, +14.4]`
- **Hit@3 `pgr` vs baseline:**`+10.4` points, 95% CI `[+0.8, +20.0]`

The trend stayed positive for `pgr`, but the confidence intervals widened.

That told us something useful:

- first-search gains are strongest and easiest to measure
- later reformulations are noisier
- search quality matters most when the agent is deciding where to go first

So this benchmark reinforced the same basic lesson:

**Ranking helps most at the beginning of the search process, when the agent is deciding what to inspect next.**

## What Actually Held Up

Across all of the benchmarks, three things held up.

1. Faster search was not the main bottleneck. `fff` was dramatically faster at the tool layer, but that only translated into a modest end-to-end improvement because tool execution was a tiny fraction of total wall-clock time.

2. Ranking clearly improved retrieval quality. On real first-search queries, `pgr` consistently outperformed baseline on first-result relevance, while `fff` did not.

3. The strongest behavioral effect was local improvement, not a broad universal efficiency win. Better search helped agents find better candidates earlier, especially on tasks where search quality actually mattered.


## What Did Not Hold Up

The data does not support a universal claim like:

> Better code search reliably means fewer tool calls and lower cost across all coding-agent tasks.

On broad mixed workloads, task variance was large enough to swamp small local improvements. Even when search behavior got better, total tool calls and total cost stayed noisy. Those are still useful downstream metrics, but they are not the most sensitive way to evaluate a search intervention.

## Future Work

This study held the language model fixed and focused on the search systems surrounding the agent loop. That choice made it easier to isolate the effects of retrieval quality, result presentation, and tool behavior, but it leaves several important questions open.

First, these benchmarks should be repeated across multiple frontier models to test whether the observed effects are model-specific or general across different planners. Some models may be more sensitive to ranking quality, while others may benefit more from richer result formatting or clearer empty-state handling.

Second, the benchmark suite should be extended to include modern retrieval models and retrieval-augmented search systems that optimize semantic matching rather than lexical ranking alone. A useful next step would be to compare those approaches against `ripgrep`, `fff`, and `pgr` on the same benchmark stack, using both retrieval and end-to-end metrics.

Finally, future work should expand the public benchmark set, improve relevance labeling, and test whether the local gains observed here persist under larger and more diverse workloads. The central methodological question is not only whether search improves, but which benchmark layer is most sensitive to which kind of search improvement.
