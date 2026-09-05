---
date: '2026-09-05'
description: The article discusses the development of "FORENSIA," a local LLM framework
  for AI-assisted forensic investigations, emphasizing a human-in-the-loop approach.
  It argues against fully autonomous forensic AI due to concerns about accuracy and
  reliability, advocating instead for "AI-assisted Forensic Scribing." The framework
  divides tasks, enabling human analysts to lead while AI organizes and verifies information.
  The author introduces a prototype named "Lepisma," built on Pi Coding Agent, which
  automates record handling without replacing the investigator's critical insights.
  This method uses local models to enhance efficiency in forensic contexts, highlighting
  a practical, cost-effective strategy for forensic analysis.
link: https://sumeshi.github.io/posts/works/dont-make-ai-your-forensic-analyst-en
tags:
- Human-in-the-loop
- AI-assisted Forensics
- Local LLMs
- Digital Investigation
- Forensic Analysis
title: Don't Make AI Your Forensic Analyst ◆ SIPDEP
---

# Don't Make AI Your Forensic Analyst

On the idea of AI-assisted Forensic Scribing, and one way to implement it.

## Introduction

A while ago, I wrote an article titled [Do Local LLMs Dream of Becoming Forensic Investigators?](https://sumeshi.github.io/posts/works/do-localllms-dream-of-forensic-investigator-en). It was about [FORENSIA](https://github.com/sumeshi/forensia), a project I built to let AI conduct forensic investigations autonomously.

FORENSIA ingests different forensic artifacts into a unified format, uses rules to generate investigation starting points, generates hypotheses, checks them against actual evidence, and feeds the results into subsequent hypothesis and report generation. In other words, it is a harness built around an investigation loop.

The basic architecture was simple in principle: **Do not let the LLM handle everything. Break work into small tasks and give the LLM only the parts it actually needs to do. Anything that does not require an LLM should be handled mechanically.**

Why did I build it this way? Back around April 2026, there simply were not many strong LLMs that could run locally. At best, the newly released [Gemma 4](https://deepmind.google/models/gemma/gemma-4/) — released on March 31, 2026 — was just barely reaching the point where I felt it might be usable.

So I ended up exploring what could be done with what I like to call a **poor man's LLM strategy**: making the most of limited hardware. In fact, I run it on a used GPU that cost me around USD 150.

I still think the original idea behind FORENSIA is interesting, but I also built it more as a PoC chasing a dream than as something I expected to immediately use in real investigations. Recently, though, I feel like local LLMs have clearly entered a different stage.

The model that personally surprised me the most was [Ornith-1.5](https://ornith.ai/ornith_1_5.html). Even the 9B version runs comfortably, and more importantly, I can leave it working for a long time without it getting stuck in reasoning loops or spiraling off in increasingly bizarre directions. It just keeps working. In that sense, I find its **agentic capability extremely impressive**.

[Ornith-1.5](https://ornith.ai/ornith_1_5.html) 9B is based on the Qwen3.5 family with additional training, so its language ability and general knowledge are not as strong as vanilla [Gemma 4](https://deepmind.google/models/gemma/gemma-4/). But honestly, I do not expect those things from a local LLM in the first place. In fact, I probably should not.

What I need is much simpler: **Give it the necessary information and instructions, and have it reliably do what I ask.** That is enough.

## The Problem with Making AI Do Forensics

Obviously, I am not the only person thinking about this. I regularly see systems that promise something along the lines of: **Feed all your forensic artifacts into AI and get a complete report at the other end!**

Most of them, however, tend to use the **WORLD'S STRONGEST MODEL** from a managed service and throw a lot of compute at the problem to maximize accuracy. And to be clear, I think that is extremely interesting too. But once confidentiality and evidence handling come into the picture, I keep coming back to local models.

![localllm](https://github.com/user-attachments/assets/e0e3e714-e83f-4166-9aff-3009736f530b)

> [FORENSIA: Local LLM Forensic Harness](https://speakerdeck.com/sumeshi/forensia-local-llm-forensic-harness?slide=3)

The problem is that on hardware an individual can realistically afford, local LLMs are still not at the point where I want to hand the entire forensic investigation over to them. I was thinking about what to do with that limitation when something occurred to me: **Maybe I do not need to make the AI do forensics at all.**

The truly painful part of forensic work is not always the investigation itself. It is continuously organizing everything into a consistent representation that lets you understand the incident as a whole.

During an investigation, you look at all kinds of artifacts and logs. There are countless tools for parsing them, and every artifact exposes different information at a different level of granularity. Of course, there are analysis products bundled with EDR platforms, as well as integrated forensic suites. But even then, you eventually have to incorporate things like:

- some mysterious cave painting that supposedly represents the network topology,
- statements from operations staff,
- actions taken by the incident response team,
- investigation results produced by somebody else,
- and all kinds of other information that never existed inside your forensic tool in the first place.

Keeping all of that organized in a single timeline is painful. And if the tool you are using to assemble it all is Excel or PowerPoint, that is enough to drive me insane.

## Choosing Not to Make AI Do Forensics

Also, the most fun part of forensic work is **discovering something that looks bad**. Why would I give that part to the AI? And if I do hand it over to the AI and the result is mediocre, that is even worse. Sometimes I end up thinking: **Wouldn't this have been faster if I had just done it myself?**

So I will.

For example, I might discover things like:

> "According to the event log, there was a logon from this IP address at 04:56 on January 12."
>
> "PowerShell ran immediately afterward."
>
> "The firewall log also shows outbound traffic around the same time."

The human analyst can simply send observations like these to the AI as they discover them. The AI then searches for the relevant source records and organizes them while retaining references to the original data. That kind of division of labor sounds much more useful to me.

This is a fully **human-in-the-loop** approach to using local LLMs. In this post, I will call this approach **AI-assisted Forensic Scribing**.

~~Surely nobody is making a junior analyst do all of this by hand... right?~~

## Starting My Forensic Life with Pi Coding Agent

As mentioned earlier, [FORENSIA](https://github.com/sumeshi/forensia) contains quite a lot of machinery just to keep an LLM behaving reasonably inside an investigation loop.

~~Evidence normalization, investigation starting points generated by detection rules, hypothesis generation, investigation coverage management, context management, validation to avoid blindly trusting model output...~~ If you want autonomous investigation to work with even halfway decent reliability, you end up needing at least that much machinery.

But with this new idea, we can start much more casually. Instead of building another investigation loop, we can reuse the loop that already exists in a coding-agent harness and simply add the domain-specific layers on top — a bit like adding the synths and melodic parts over an existing rhythm section.

I chose [Pi Coding Agent](https://pi.dev/) as the base. Pi is a minimal coding-agent harness. By default, its core toolset is basically just: `read``write``edit``bash`.

And apparently there is a whole group of people who see that minimalism and immediately think: **Nice. Time to build my own harness on top of this.** They are the kind of people who mix their own BBQ rub instead of buying one from the store. I understand them. I am one of them.

## Let's Actually Build It

Since we are already here, let's build a quick prototype and see what it can do. I named the project [Lepisma](https://github.com/sumeshi/lepisma). The name comes from **Lepisma**, the genus that includes the common silverfish.

### Preparing Pi

See the official [Pi](https://pi.dev/) website for installation instructions. Install it with npm or whatever the current recommended method happens to be.

Then configure the model you want to use. Set the API server URL in `baseUrl`, and adjust `contextWindow` and `maxTokens` according to your available VRAM.

The configuration below is almost identical to what I use. My setup is nothing special:

- a desktop PC assembled from assorted spare parts,
- an RTX 2070 SUPER that cost around USD 150,
- and [llama-server](https://github.com/ggml-org/llama.cpp/tree/master/tools/server).

That is enough.

`~/.pi/agent/models.json`

```
{
    "providers": {
        "ornith": {
            "baseUrl": "http://192.168.1.123:8080/v1",
            "api": "openai-completions",
            "apiKey": "none",
            "compat": {
                "supportsDeveloperRole": false,
                "supportsReasoningEffort": false
            },
            "models": [\
                {\
                    "id": "Ornith-1.5-9B",\
                    "name": "Ornith-1.5-9B",\
                    "reasoning": true,\
                    "contextWindow": 131072,\
                    "maxTokens": 16384\
                }\
            ]
        }
    }
}
```

### Structure

I use two main mechanisms to control how Pi Coding Agent behaves:

- `AGENTS.md`
- `.pi/skills/<skill_name>/SKILL.md`

The project structure looks like this:

```
lepisma/
 ├── AGENTS.md
 ├── timeline.csv
 ├── sources/
 └── .pi/
    └── skills/
        ├── lepisma-search/
        │   └── SKILL.md
        ├── lepisma-summarize/
        │   └── SKILL.md
        ├── lepisma-tag/
        │   └── SKILL.md
        └── lepisma-timeline/
            └── SKILL.md
```

Let's go through them one by one.

### AGENTS.md

`AGENTS.md` is loaded throughout the session. I use it for project-wide policies and general behavior. Ornith-1.5 is Qwen-based, so English tends to work better than Japanese, but if I am going to keep modifying the instructions while actually using the system, writing them in whatever language is easiest for me may be more practical.

```
# Lepisma

You are an assistant that supports digital forensic investigations.

The human analyst leads the investigation. Do not autonomously decide the direction of the investigation.

Treat information provided by the analyst as investigation anchors and use the following skills when appropriate:

- `lepisma-search`: Search for relevant source records.
- `lepisma-summarize`: Summarize source records concisely and objectively.
- `lepisma-tag`: Assign consistent `event_type` values and `tags`.
- `lepisma-timeline`: Verify source records and update `timeline.csv`.

## General Policy

When the analyst provides a timestamp, IP address, hostname, username, process name, filename, or other investigative information, use it as the starting point for the task.

Whenever possible, verify factual information against source data under `sources/`.

Do not record unverified information as fact solely because the analyst said it.

Do not infer or invent information that does not exist in the source records.

Do not expand the investigation in directions that were not explicitly requested.

## timeline.csv

Store the chronological investigation record in `timeline.csv`.

Before adding new information, inspect the existing `timeline.csv`.

Do not add duplicate events.

Inspect existing `event_type` values and `tags`, and reuse existing values when they express the same meaning.

Do not create new classifications or tags that differ only in wording or formatting.

Preserve `source_record` and `source_file` so that the basis for each entry can be reviewed later.

## sources/

Treat files under `sources/` as analysis source data extracted or parsed from original evidence.

Do not treat them as identical to the original evidence itself.

Do not modify them unless explicitly instructed.

Use them only for search, reference, and reading.

## Division of Responsibilities

The analyst decides what to examine, what matters, and where to investigate next.

Lepisma takes investigation anchors provided by the analyst, searches for relevant source records, verifies them, summarizes them, classifies them, and organizes them chronologically.

Do not behave as an autonomous investigator.

Behave as an assistant that records and organizes an investigation led by a human analyst.
```

### SKILL.md

Skills are loaded when needed. I use them for procedures that are clear, repetitive, and easy to standardize. I think of them almost like small, task-specific functions.

#### lepisma-search/SKILL.md

```
---
name: lepisma-search
description: Search source files for records related to analyst-provided investigation anchors.
---

Use analyst-provided timestamps, IP addresses, hostnames, usernames, process names, filenames, and other identifiers as search anchors.

Search relevant records under `sources/`.

Also search for keywords directly derived from the analyst-provided information to reduce missed relevant records.

For each result, preserve the complete source record and its source file.

Do not infer or invent information that cannot be verified from the source data.
```

#### lepisma-summarize/SKILL.md

```
---
name: lepisma-summarize
description: Summarize a source record into a short and objective timeline entry.
---

Summarize the provided source record in roughly 10 to 20 words.

The summary must allow a human reader to quickly understand what happened.

Do not add information that does not exist in the source record.

Do not include speculation, interpretation, or evaluation.
```

#### lepisma-tag/SKILL.md

```
---
name: lepisma-tag
description: Assign consistent event types and tags to timeline events.
---

Assign `event_type` and `tags` to an event.

Before assigning values, inspect the existing `timeline.csv`.

Reuse an existing value when the same or a sufficiently similar value already exists.

Do not create new values that differ only in spelling, capitalization, wording, or formatting.

Create a new value only when the existing values cannot appropriately describe the event.

Use `event_type` to describe the type of event itself.

Use `tags` to provide keywords that help identify, search, and correlate related events later.
```

#### lepisma-timeline/SKILL.md

```
---
name: lepisma-timeline
description: Search source records and update the investigation timeline based on analyst-provided information.
---

Use the `lepisma-search` skill to search for source records related to the information provided by the analyst.

Use the search results to update `timeline.csv`.

Do not add an event if the same event already exists in the timeline.

Use the following columns:

- `timestamp`: Original timestamp recorded in the source data.
- `timestamp_utc`: Timestamp normalized to UTC (`UTC+00:00`).
- `event_type`: Event classification such as `Logon`, `Logoff`, or `UserAdd`. Use the `lepisma-tag` skill.
- `summary`: Short and objective description of the event. Use the `lepisma-summarize` skill.
- `source_record`: Complete source record used to support this timeline entry.
- `source_file`: Source file containing the source record.
- `note`: Additional notes or analyst-provided context.
- `tags`: Keywords used to search and correlate related events. Use the `lepisma-tag` skill.

When the timezone can be determined, normalize the timestamp to UTC and store it in `timestamp_utc`.

Always preserve `source_record` and `source_file`.

Use `-` when a value cannot be determined.
```

#### sources

This is where I put the source data used during the investigation. Plain text works well enough for this PoC. For testing, I parsed Windows Event Logs from the [CFReDS Data Leakage Case](https://cfreds-archive.nist.gov/data_leakage_case/data-leakage-case.html) using [EvtxECmd](https://github.com/EricZimmerman/evtx) and placed the resulting data here.

#### timeline.csv

This is where the investigation timeline is stored. For this prototype, I intentionally kept the schema small.

| Column | Description |
| --- | --- |
| `timestamp` | Original timestamp recorded in the source data |
| `timestamp_utc` | Timestamp normalized to UTC (`UTC+00:00`) |
| `event_type` | Event classification such as `Logon`, `Logoff`, or `UserAdd`, defined as needed |
| `summary` | Concise description of the event |
| `source_record` | Complete source record supporting the entry |
| `source_file` | File containing the source record |
| `note` | Additional notes or comments from the analyst |
| `tags` | Tags used to search for and correlate related events later |

#### Results

![lepisma-en](https://github.com/user-attachments/assets/64b94186-2b21-4ac2-85c5-7fcfd8ad7060)

Even with just this, it is already starting to look reasonably useful. The LLM also seems capable of deciding when to invoke the appropriate skills on its own.

One issue I noticed is that whenever it needs to edit the CSV, it tends to generate small Python scripts and fiddle with the file that way. That costs a bit of time and tokens. It may be better to prepare utility scripts or additional skills in advance, or simply move the timeline into [SQLite](https://www.sqlite.org/) or [DuckDB](https://duckdb.org/).

Ideally, I would also like to keep dropping findings into it as I discover them and then let it organize everything while I take a break. So queueing and parallel execution may be worth exploring as well. Adding retrieval mechanisms such as RAG could probably make the whole thing reasonably practical too.

## Conclusion

During forensic work, I rarely max out the machine with analysis software alone. There is usually some compute sitting idle, and computers are meant to be used.

So maybe a loose workflow like this is good enough: **I keep investigating while I throw all the annoying organizational work at the AI running beside me.** That feels like a perfectly reasonable way to use local AI.

Right, Hamtaro?

The end.
