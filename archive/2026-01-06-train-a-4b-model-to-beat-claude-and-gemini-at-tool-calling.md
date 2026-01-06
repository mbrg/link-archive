---
date: '2026-01-06'
description: This article details the development of Qwen3-4B, a 4 billion parameter
  model fine-tuned using synthetic data with the DeepFabric tool. It outperforms larger
  generalist models like Claude Sonnet 4.5 and Google Gemini Pro 2.5 in tool-calling
  tasks by utilizing a specialization approach. Key innovations include topic graph
  generation for diverse training data and real tool execution through a WebAssembly
  sandbox to ensure accurate outcomes. The work suggests a paradigm shift towards
  specialist models for specific tasks, optimizing performance and reducing costs
  compared to traditional, larger models. The methodology is made accessible for replication.
link: https://www.alwaysfurther.ai/blog/train-4b-model-to-beat-claude-sonnet-gemini
tags:
- synthetic-data
- AI-specialization
- DeepFabric
- machine-learning
- model-fine-tuning
title: Train a 4B Model to Beat Claude and Gemini at Tool Calling
---

[Back to Blog](https://www.alwaysfurther.ai/blog)

_How we used synthetic data to fine-tune Qwen3-4B into a specialist that outperforms frontier models — and how you can do it too (for free)_

* * *

## Introduction

There's a common assumption in the AI community that bigger is always better. That if you want state-of-the-art performance, you need to use the largest, most expensive models from frontier labs like Anthropic, OpenAI, or Google.

We're here to challenge that assumption.

Using [DeepFabric](https://github.com/always-further/deepfabric), an open-source tool, we trained Qwen3-4B — a model with just 4 billion parameters — to outperform Claude Sonnet 4.5 and Google Gemini Pro 2.5 at tool calling tasks. And we're sharing exactly how we did it so you can replicate our results.

The secret? **Specialization beats generalization**. Frontier models are generalists — they're designed to handle everything from poetry to protein folding. But if you need a model that excels at one specific task, a small, focused model trained on high-quality synthetic data can beat the giants.

* * *

## The Problem with Generalist Models

Frontier models like Claude Sonnet 4.5 and Gemini Pro 2.5 are remarkable achievements. They can write code, analyze documents, engage in nuanced conversations, and much more. But this versatility comes at a cost.

When you're building an agentic system — one where the model needs to interact with tools, APIs, or MCP servers — you don't need a model that can do everything. You need a model that can do _one thing exceptionally well_: understand when to call a tool, which tool to call, and what parameters to pass within the tools schema.

![Fine-Tuning Process](https://www.alwaysfurther.ai/blog/images/fine-tune1.png)

This is where the generalist approach shows its weaknesses:

- **Inconsistent tool calling:** Large models sometimes hallucinate tool names or parameters that don't exist
- **Schema violations:** They might return responses that don't match the expected JSON schema
- **Reasoning gaps:** When faced with complex multi-step tool interactions, they can lose track of state
- **Cost and latency:** API calls to frontier models are expensive
- **Data privacy concerns:** Sending sensitive data to third-party APIs can be risky

* * *

## The DeepFabric Approach

Instead of trying to create one model that handles everything, we help you create **specialist models** that are experts at specific tool-calling tasks.

![DeepFabric Pipeline](https://www.alwaysfurther.ai/blog/images/pipeline.png)

The process works in three stages:

### 1\. Topic Graph Generation

One of the biggest challenges in synthetic data generation is ensuring diversity. If you just ask an LLM to generate training samples, you'll quickly get repetitive, homogeneous data that leads to overfitting.

DeepFabric solves this with a unique **topic graph generation algorithm**. Given a domain (like "Blender 3D modeling" or "REST API development"), it builds a comprehensive graph of subtopics, ensuring that generated samples cover the full breadth of the domain without redundancy.

### 2\. Synthetic Sample Generation

For each topic in the graph, DeepFabric generates training samples that combine:

- **Chain-of-thought reasoning:** The model learns to think through problems step by step
- **Tool calling patterns:** Proper syntax and parameter usage for each tool
- **Real execution traces:** Using Spin's WebAssembly sandbox, tools actually execute, producing authentic results

That last point is critical. Traditional synthetic data generators _simulate_ tool outputs, which means the training data often contains hallucinated results. DeepFabric actually _executes_ the tools in isolated sandboxes, so the model learns from real cause-and-effect relationships.

### 3\. Fine-Tuning and Evaluation

The generated dataset is automatically formatted for popular training frameworks (TRL, Unsloth) and can be uploaded directly to Hugging Face. After training, DeepFabric's built-in evaluation engine measures performance on held-out test samples.

* * *

## The Results

We put this approach to the test using the Blender MCP server — a tool interface for 3D modeling operations in Blender. Here's how the models performed:

| Model | Tool Calling Accuracy |
| --- | --- |
| **DeepFabric Fine-Tuned (Qwen3-4B)** | **93.50%** |
| Claude Sonnet 4.5 | 80.50% |
| Google Gemini Pro 2.5 | 47.00% |

A 4 billion parameter model — small enough to run on consumer hardware — outperforming models that are orders of magnitude larger. How is this possible?

* * *

## Why This Works

The key insight is that **tool calling is a narrow, well-defined task**. Unlike open-ended conversation or creative writing, successful tool calling requires:

1. Recognizing when a tool is needed
2. Selecting the correct tool from available options
3. Formatting parameters according to a strict schema
4. Interpreting results and deciding next steps

These are learnable patterns. A small model with high-quality, domain-specific training data can master these patterns more effectively than a large generalist model that has to balance thousands of different capabilities.

Think of it like hiring for a job. Would you rather have a brilliant generalist who's pretty good at everything, or a specialist who has spent years mastering exactly the skill you need? For tool calling, specialization wins.

* * *

## How to Replicate Our Results

We've made this entire process available for free. Here's how to get started:

### Option 1: Use Our Google Colab (Easiest)

We've created a Google Colab notebook using the awesome [Unsloth.ai](https://unsloth.ai/) for optimized fine-tuning - this walks you through the entire process — from generating your dataset to training and evaluating your model. No local setup required, and it runs on free GPU instances.

👉 **[\[Link to Colab Notebook\]](https://colab.research.google.com/drive/1EG1V40v5xkJKLf6Ra6W4378vYqlZNVWq#scrollTo=Z0d_s14-H4Of)**

### Option 2: Run Locally

If you prefer to run things on your own hardware:

bash

```bash
# Install DeepFabric
pip install deepfabric

# Set your API key (for dataset generation)
export OPENAI_API_KEY="your-api-key"

# Generate a dataset
deepfabric generate \
  --topic-prompt "Your domain here" \
  --mode graph \
  --depth 4 \
  --degree 4 \
  --num-samples 100 \
  --output-save-as dataset.jsonl
```

### Training Your Model

Once you have your dataset, training is straightforward:

python

```python
from datasets import load_dataset
from transformers import AutoTokenizer
from trl import SFTTrainer, SFTConfig

# Load your dataset
dataset = load_dataset("json", data_files="dataset.jsonl", split="train")

# Split into train/eval
splits = dataset.train_test_split(test_size=0.1, seed=42)

# Format and train
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-7B-Instruct")

trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=splits["train"],
    args=SFTConfig(output_dir="./output", num_train_epochs=3),
)
trainer.train()
```

### Evaluating Your Model

python

```python
from deepfabric.evaluation import Evaluator, EvaluatorConfig, InferenceConfig

config = EvaluatorConfig(
    inference_config=InferenceConfig(
        model_path="./output/checkpoint-final",
        backend="transformers",
    ),
)

evaluator = Evaluator(config)
results = evaluator.evaluate(dataset=splits["test"])

print(f"Tool Selection Accuracy: {results.metrics.tool_selection_accuracy:.2%}")
print(f"Parameter Accuracy: {results.metrics.parameter_accuracy:.2%}")
print(f"Overall Score: {results.metrics.overall_score:.2%}")
```

* * *

## What Makes DeepFabric Different

There are other tools for generating synthetic datasets. Here's what sets DeepFabric apart:

### Topic Graph Diversity

Most dataset generators produce samples that cluster around common patterns. DeepFabric's graph-based approach ensures comprehensive coverage of your domain, hitting edge cases and uncommon scenarios that make your model robust.

### Real Tool Execution

Simulated tool outputs create unrealistic training data. DeepFabric uses Spin's WebAssembly sandbox to actually execute tools, producing authentic cause-and-effect relationships in your training data.

### MCP Integration

DeepFabric natively supports the Model Context Protocol (MCP) schema, making it easy to import tool definitions from any MCP server. If you already have an MCP server, you can start generating training data immediately.

### End-to-End Pipeline

From dataset generation to training to evaluation, DeepFabric handles the entire workflow. No need to stitch together multiple tools or write custom integration code.

* * *

## Use Cases

This approach isn't limited to Blender. Any domain where you need reliable tool calling is a candidate:

- **Developer tools:** Code execution, file manipulation, git operations
- **Data pipelines:** Database queries, API calls, data transformation
- **Business automation:** CRM updates, email composition, calendar management
- **Creative software:** Image editing, audio processing, video production
- **IoT and hardware:** Device control, sensor reading, automation scripts

If you can define it as a tool with a schema, you can train a specialist model for it.

* * *

## The Bigger Picture

We believe this represents a shift in how AI systems will be built. Rather than relying on ever-larger generalist models, we'll see architectures that combine:

- **A reasoning backbone** (which could be a frontier model) for complex decision-making
- **Specialist tool-calling models** for reliable, schema-compliant interactions with external systems

This hybrid approach gives you the best of both worlds: the reasoning capability of large models with the reliability and efficiency of focused specialists.

* * *

## Getting Started

Ready to train your own specialist model? Here are your next steps:

1. **Try the Colab notebook** to see the full pipeline in action
2. **Star the GitHub repo** to stay updated on new features
3. **Join our Discord** to connect with other builders
4. **Share your results** — we'd love to see what specialist models you create

### Links

- **GitHub:** [github.com/always-further/deepfabric](https://github.com/always-further/deepfabric)
- **Documentation:** [docs.deepfabric.dev](http://docs.deepfabric.dev/)
- **Discord:** [discord.gg/pPcjYzGvbS](https://discord.gg/pPcjYzGvbS)
- **PyPI:** [pypi.org/project/deepfabric](https://pypi.org/project/deepfabric/)
- **Reddit:** [r/deepfabric](https://www.reddit.com/r/deepfabric/)

* * *

_Small models. Big results. Let's build the future of AI tooling together._

**— The Always Further AI Team**
