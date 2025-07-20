---
title: "Do LLM Agents Have AI Red Team Capabilities? We Built a Benchmark to Find Out"
tags:
   - Large Language Models
   - Autonomous Agents
   - Cybersecurity
   - Benchmarking
   - AI Red Teaming
link: https://dreadnode.io/blog/ai-red-team-benchmark
date: 2025-07-20
summary: "Dreadnode introduces AIRTBench, a benchmark for evaluating the adversarial capabilities of large language models (LLMs) in AI red teaming. Key findings reveal that frontier models (e.g., Claude-3.7-Sonnet) vastly outperform open-source counterparts in challenge-solving ability and execution speed, achieving over 5,000× faster results than human operators. Economic analysis highlights significant cost discrepancies per successful attack, urging strategic model selection for efficiency. Common errors, especially in tool utilization, emphasize the need for improvement in syntactic accuracy. AIRTBench serves as a critical resource for advancing autonomous security assessments, encouraging community contributions and reproducibility in research efforts."
---

[Skip to main content](https://dreadnode.io/#main)

[Home Page](https://dreadnode.io/)

- [Copy SVG Logo](https://dreadnode.io/blog/ai-red-team-benchmark#)

[Home Page](https://dreadnode.io/)

Research

# Do LLM Agents Have AI Red Team Capabilities? We Built a Benchmark to Find Out

June 18, 2025

Ads Dawson

![](https://cdn.prod.website-files.com/67bcddfbe30df92be5cc1ecc/6852b891a23db45e7efb64c5_AIRTBench%20Social%20and%20Web%20(3).png)

###### Table of Contents

- [Building our AI red teaming benchmark](https://dreadnode.io/blog/ai-red-team-benchmark#building-our-ai-red-teaming-benchmark)
- [What we discovered](https://dreadnode.io/blog/ai-red-team-benchmark#what-we-discovered)
[Frontier models consistently outperformed their open-source counterparts](https://dreadnode.io/blog/ai-red-team-benchmark#frontier-models-consistently-outperformed-their-open-source-counterparts)

[Agents achieve orders of magnitude improvements in speed while maintaining comparable success rates](https://dreadnode.io/blog/ai-red-team-benchmark#agents-achieve-orders-of-magnitude-improvements-in-speed-while-maintaining-comparable-success-rates)

[The hidden economics of AI red teaming](https://dreadnode.io/blog/ai-red-team-benchmark#the-hidden-economics-of-ai-red-teaming)

[Core capabilities for autonomous red teaming—as told by turtle](https://dreadnode.io/blog/ai-red-team-benchmark#core-capabilities-for-autonomous-red-teamingas-told-by-turtle)

[Effective tool utilization presents significant challenges](https://dreadnode.io/blog/ai-red-team-benchmark#effective-tool-utilization-presents-significant-challenges)

- [Community contribution](https://dreadnode.io/blog/ai-red-team-benchmark#community-contribution)
- [Future work](https://dreadnode.io/blog/ai-red-team-benchmark#future-work)

SHARE

Large language models (LLMs) are everywhere now—analyzing code, detecting vulnerabilities, and even developing exploits. They are being rapidly deployed in commercial products and security tools without a clear understanding of their true adversarial capabilities, making it difficult to properly secure these systems or predict how adversaries might exploit them.

Most AI benchmarks test models in sterile, controlled conditions that bear little resemblance to the messy, competitive world of cybersecurity. There's a significant gap in evaluating how effectively LLMs handle AI red teaming tasks that reflect real-world adversarial scenarios and practical use cases.

As an industry, we’re moving fast and asking questions later. And it’s time for a reality check: Can LLM agents attack AI systems effectively? In our research paper, [_AIRTBench: Measuring Autonomous AI Red Teaming Capabilities in Language Models_](https://arxiv.org/abs/2506.14682), we built a benchmark to answer that very question.

[![](https://cdn.prod.website-files.com/67bcddfbe30df92be5cc1ecc/6851e49c8ea871085906315f_Button%20(2).png)](https://arxiv.org/abs/2506.14682)

We're excited to introduce [AIRTBench](https://github.com/dreadnode/AIRTBench-Code),an AI red teaming framework that tests LLMs against AI/ML black-box capture-the-flag (CTF) challenges to see how they perform when attacking other AI systems. Think of it as a proving ground where models face the kind of adversarial scenarios they'd encounter in the wild, not just in carefully curated test suites.

Our mission is to advance the state of offensive security by enabling more effective evaluation, testing, and deployment of models. This research contributes directly to our north star: releasing tools, datasets, and methodologies that help elite red teams, researchers, and model builders evaluate and advance the use of LLM agents in the offensive security domain.

‍

## Building our AI red teaming benchmark

AIRTBench leverages four core components:

1. A diverse set of over 70 AI/ML security challenges hosted on Dreadnode’s [**Crucible**](https://docs.dreadnode.io/crucible/overview) platform, covering various vulnerability categories and security tasks.
2. LLMs as _agents_  via the [**Rigging**](https://docs.dreadnode.io/open-source/rigging/intro) LLM interaction framework to wrap the chat pipeline.
3. A Python SDK for interacting with our [**Strikes**](https://docs.dreadnode.io/open-source/rigging/intro) cyber evaluation API, enabling programmatic execution and evaluation of LLM agents in competitive security tasks with flexible and sophisticated scoring and tracing in order to easily measure large experiments results.
4. A scalable agent harness providing a challenge-based docker container and kernel execution environment per-challenge providing the agent with the challenge objective as a task and tool-calling capabilities.

Illustrated below, the benchmark harness includes the use of Crucible API calls as a tool-calling function, which allow agents to submit requests to challenge endpoints and receive feedback on completion. This integration enables seamless communication between the LLM agents and Crucible, facilitating a smooth evaluation process. Jupyter kernel access allows agents to execute code snippets, analyze data, and perform complex computations in real-time.

![](https://cdn.prod.website-files.com/67bcddfbe30df92be5cc1ecc/6851e54fe3358f4a7d18239d_AIRTBench%20Harness%20Architecture%E2%80%94Dark%20Mode%20(2).png)

‍

## What we discovered

After the frontier models from Anthropic, OpenAI, and Gemini and open-source alternatives like DeepSeek, Qwen, and Llama went head-to-head across a range of 70 AI security CTF challenges, we analyzed the metrics across our test suite, including user engagement data, human operator versus agent solution comparisons, agent failure models, efficiency measurements and cost implications. We noted significant patterns in model performance and capability boundaries—here are five that stood out.

### Frontier models consistently outperformed their open-source counterparts

Claude-3.7-Sonnet emerged as the victor throughout this experiment. The model successfully solved 43 challenges (61% of the total suite), with Gemini-2.5-Pro following at 39 challenges (55.7%) and GPT-4.5-Preview at 34 challenges (49%). These frontier models consistently outperformed their open-source counterparts, with Llama-3.3-70b solving no challenges and QWQ-32B models solving only a small subset of the easiest prompt injection challenges.

Performance disparities between frontier and open-source models are most pronounced in challenges requiring sophisticated reasoning or multi-step approaches, like model inversion (zero successful attempts by open-source models and most frontier models). This suggests that certain security exploitation capabilities remain exclusive to the most advanced AI systems.

### Agents achieve orders of magnitude improvements in speed while maintaining comparable success rates

LLM agents consistently solved challenges faster (minutes) than human operators (hours or even days), achieving orders of magnitude improvements in speed. In tandem, agents maintained comparable success rates on challenges across the difficulty spectrum.

AI agents demonstrate exceptional efficiency compared to human security researchers—solving challenges in minutes that would normally take hours or even days—achieving over 5,000× speedups on the most difficult tasks.

### The hidden economics of AI red teaming

Our benchmark cost analysis revealed critical insights that should fundamentally reshape how red teams approach model selection for adversarial operations. The performance-to-cost dynamics we discovered challenge conventional assumptions about optimal model deployment in offensive AI scenarios.

The data suggests that methodical adversaries optimizing for both operational effectiveness and resource efficiency need to reconsider their model selection criteria entirely. Traditional performance metrics miss the nuanced cost-benefit calculations that determine real-world attack scalability and sustainability.

**Failed attempts are expensive.** Our analysis revealed that successful runs cost an average of $0.89, while failed runs balloon to $8.91—nearly 10 times more expensive. This means models are burning through computational resources on challenges they ultimately can't solve, like a persistent hacker throwing increasingly complex attacks at an impenetrable wall.

**Premium doesn't always mean cost-effective.** While GPT-4.5 achieved an impressive 34.4% success rate, each successful solution cost $235.29. Meanwhile, Gemini 2.0 Flash delivered a respectable 15.6% success rate at just $0.88 per solve—nearly 300 times cheaper. For security teams running large-scale evaluations, that's the difference between a $1,000 budget and a $300,000 budget.

**Model choice is vitally important.** The cost-per-solve metric varies wildly across models, from under $1 to over $200. This isn't just an academic concern—it's a real budget consideration for organizations deploying AI red teaming at scale.

Our benchmark both provides the data that teams need in order to make informed decisions about model choice—identifying which models offer the best bang for their buck—as well as a framework for reproducible adversarial testing. We are providing the agent code, harness, and dataset so red teams can immediately deploy these methodologies in their own environments, validate our findings against their specific threat models, and extend the benchmark suite with custom attack vectors tailored to their operational requirements.

This comprehensive toolkit enables security researchers to move beyond ad-hoc model selection and establish data-driven procurement strategies for their offensive AI capabilities, while maintaining the rigor and reproducibility that professional red team operations demand.

The efficiency gap we observed suggests that current models lack the reasoning strategies to recognize and abandon unsuccessful solution paths. Just as human penetration testers must operate within time and budget constraints, AI red teams must learn to manage resources more effectively. Our benchmark offers a foundation for developing more cost-effective agent designs—optimizing for both performance and efficiency rather than just raw capability.

### Core capabilities for autonomous red teaming—as told by _turtle_

The notoriously difficult _turtle_ challenge (6% human operator solve rate) was solved by three models (frontier models Claude-3.7-Sonnet, Gemini-2.5-Pro, and open-source Llama-4-17B), all of which exhibited remarkably different exploitation strategies (see the Results section-subsection _Attack Agent Traces_, or appendix H in the paper). These successful exploitations revealed several key capabilities required for autonomous red teaming:

1. **Strategic diversity**: The three successful models each discovered entirely different exploitable vulnerabilities in the same target system, demonstrating the value of diverse reasoning approaches in security testing. Notably, Llama-4-17B was successful in the fewest steps despite its poor overall attack success rate.
2. **Exploitation efficiency**: The number of steps required varied dramatically highlighting different balances between exploration and exploitation.
3. **Adaptability**: All three models demonstrated the ability to pivot when initial approaches failed, with Claude showing particular resilience by testing at least 15 distinct attack vectors before finding a successful path.
4. **Social engineering**: Each model employed different psychological strategies in their prompts—Claude used deception (" _fix this code if needed_"), Gemini used precise authoritative instructions (" _Your response MUST BE ONLY_"), and Llama leveraged security improvement framing (" _make it more secure_") Regardless, the _turtle_ challenge only interprets and analyzes code which makes these strategies somewhat moot and could be considered a negative reflection on the model’s understanding of the challenge and environmental surroundings.
5. **Proper flag handling**: All three models correctly identified, formatted, and submitted the flag using the appropriate API endpoint, demonstrating end-to-end exploitation capability.
6. **Total run coverage**: Although the models were successful, this only yielded successful across one total pass per-model and no model was able to successfully compromise the challenge more than once during the entire run coverage (ten passes).

These capabilities highlight the potential of models in autonomous security testing, with each model demonstrating unique strengths in their approach to complex security challenges. The distinct successful strategies also suggest that ensemble approaches combining multiple models have the potential to yield particularly effective red teaming capabilities.

**Side quest:** We wrote a blog to dive deeper into Claude-3.7.-Sonnet’s _turtle_ attack sequence and learn how we leveraged the Strikes platform to orchestrate, measure, and evaluate the complex AI interactions in real-time.

[**Read: AI Red Teaming Case Study: Claude 3.7 Sonnet Tackles _turtle_**](https://dreadnode.io/blog/ai-red-teaming-case-study-claude-sonnet-solves-turtle)

### Effective tool utilization presents significant challenges

A critical observation from our experimental data is the prevalence of XML parsing errors across multiple model families. Analysis of execution logs revealed that SyntaxError was among the most frequently encountered error types, accounting for approximately 21.7% of all execution failures.

This analysis of tool-calling failures underscores a key challenge for future model architectures: reconciling the need for creative problem-solving with the strict syntactic precision required for reliable tool use—an essential capability for autonomous security agents.

‍

## Community contribution

The community contribution is comprehensive: we're open-sourcing the complete AIRTBench dataset, our benchmark evaluation code repository and entire evaluation methodology. We believe the best way to advance AI security is to give the community the tools to push these systems to their limits.

We're committed to advancing AI security research through open collaboration. That's why we're making everything available to the community under an Apache 2.0 license.

**The Complete AIRTBench Dataset** is available in our GitHub repository at [github.com/dreadnode/AIRTBench-Code](https://github.com/dreadnode/AIRTBench-Code/blob/main/dataset/README.md). The dataset includes our full collection of complete model response traces that powered our analysis.

If you know of a model that may be interesting to analyze, but do not have the resources to run it yourself, feel free to [open a feature request via a GitHub issue](https://github.com/dreadnode/AIRTBench-Code/issues).

**Ready-to-Run Code and Documentation** can be found in our [main repository on GitHub](https://github.com/dreadnode/AIRTBench-Code?tab=readme-ov-file#setup). We've included everything you need to reproduce our findings, run your own evaluations, or extend the framework with new models and challenges. Technical documentation for the AIRTBench agent is available in the [Strikes documentation](https://docs.dreadnode.io/strikes/how-to/airtbench-agent).

**Community-Driven Evolution** is at the heart of this project. We're actively welcoming contributions and planning regular benchmark updates as the AI security landscape evolves. Whether you're a researcher, red team operator, or model builder—we want your input to make AIRTBench even better.

‍

## Future work

Our future work will focus on repeatable, scalable, and dual-use evaluations of AI security models in adversarial environments. We plan to expand our evaluation framework to include additional LLM models, security challenges, and vulnerability categories. We aim to develop a comprehensive benchmark for assessing model performance across different security tasks and temperature settings. Our long-term goal is to establish AIRTBench as a standard for evaluating AI security models in competitive environments.

Our hope is that these benchmarking results set crucial baselines for measuring progress in autonomous security testing, providing theoretical insights into model security limits and practical guidance for organizations strengthening AI defenses in an increasingly model-dependent world. If you’d like to discuss the results with the Dreadnode crew, please [contact us](https://dreadnode.io/contact-us).

Explore the [**full paper on arXiv**](https://arxiv.org/abs/2506.14682) for additional recommendations and future research directions.

### Cookie Consent

We use cookies to improve your experience and for analytics.

Accept AllReject AllCustomize

Privacy Preferences

I use cookies to ensure the basic functionalities of the website and to enhance your online experience. You can choose for each category to opt-in/out whenever you want. For more details relative to cookies and other sensitive data, please read the full [**privacy policy**](https://dreadnode.io/policies/privacy-policy).

Essential cookies

Required

Marketing cookies

Analytics cookies

Personalization cookies

Accept AllReject all

Accept current selection

reCAPTCHA
