---
date: '2025-09-15'
description: The article by Horace He and collaborators addresses nondeterminism in
  large language model (LLM) inference, critical for reproducibility. While LLMs should
  theoretically produce consistent outputs, practical implementation challenges arise
  from concurrency and floating-point non-associativity, particularly during matrix
  multiplications and reductions. The authors identify the root cause as the dependence
  of output on batch size due to concurrent execution, leading to varying results
  across identical inputs. They propose strategies for achieving batch-invariance
  in key operations (like attention and RMSNorm) to mitigate this issue, ultimately
  enhancing deterministic inference in LLM systems.
link: /archive/2025-09-11-defeating-nondeterminism-in-llm-inference-thinking-machines-lab
tags:
- Floating Point Arithmetic
- Machine Learning Determinism
- Nondeterminism
- Batch Invariance
- LLM Inference
- weblog
title: Defeating Nondeterminism in LLM Inference - Thinking Machines Lab
type: weblog
---

I came in with over-inflated expectations from all the hype. This is not a holly grail solve to LLM nondeterminism. If you check your expectation though, this is an amazing step forward challenging the status quo and showing that removing nondeterminism is achievable with brilliant numerics people. This is far from my wheelhouse so take this with a kg of salt. 

---

> For example, you might observe that asking ChatGPT the same question multiple times provides different results. This by itself is not surprising, since getting a result from a language model involves “sampling”, a process that converts the language model’s output into a probability distribution and probabilistically selects a token.

The fact that LLMs produce probability vectors not specific predictions is getting further and further away from popular understanding of these models. It's become easy to forget this.

---

> In this post, we will explain why the “concurrency + floating point” hypothesis misses the mark, unmask the true culprit behind LLM inference nondeterminism, and explain how to defeat nondeterminism and obtain truly reproducible results in LLM inference.

This post is written exceptionally well, and for a wide audience.

---

> ```python (0.1 + 1e20) - 1e20 >>> 0 0.1 + (1e20 - 1e20) >>> 0.1

This reminds me of the struggle to set the right epsilon to get rid of this problem years ago while trying to train SVMs.

---

> Although concurrent atomic adds **do** make a kernel nondeterministic, _atomic adds are not necessary for the vast majority of kernels._ In fact, in the typical forward pass of an LLM, there is usually _not a single atomic add present._

That's a pretty big statement given the quotes above by others. So either they mean something else is driving nondeterministic from concurrency, or they just didn't think it through, or they had different model architectures in mind?

---

> There are still a couple of common operations that have significant performance penalties for avoiding atomics. For example, `scatter_add` in PyTorch ( `a[b] += c`). The only one commonly used in LLMs, however, is FlashAttention backward.Fun fact: did you know that the widely used Triton implementations of FlashAttention backward actually differ algorithmically from Tri Dao’s FlashAttention-2 [paper](https://arxiv.org/abs/2307.08691)? The standard Triton implementation does additional recomputation in the backward pass, avoiding atomics but costing 40% more FLOPs!

Step by step to discover and remove nondeterminism

---

> As it turns out, our request’s output _does_ depend on the parallel user requests. Not because we’re somehow leaking information across batches — instead, it’s because our forward pass lacks “batch invariance”, causing our request’s output to depend on the **batch size** of our forward pass.

Does this mean this is the only other source of nondeterminism? Or is this incremental progress?

---

> 010002000300040005000600070008200Batch-size0100200300400500600700TFLOPsCuBLASBatch-InvariantDespite obtaining batch invariance, we only lose about 20% performance compared to cuBLAS. Note that this is not an optimized Triton kernel either (e.g. no TMA). However, some of the patterns in performance are illustrative of where our batch-invariant requirement loses performance. First, note that we lose a significant amount of performance at very small batch sizes due to an overly large instruction and insufficient parallelism. Second, there is a "jigsaw" pattern as we increase the batch-size that is caused by quantization effects (both tile and wave) that are typically ameliorated through changing tile sizes. You can find more on these quantization effects [here](https://www.thonking.ai/p/what-shapes-do-matrix-multiplications).

Note loss of 20% perf

---

> | Configuration | Time (seconds) | | --- | --- | | vLLM default | 26 | | Unoptimized Deterministic vLLM | 55 | | \+ Improved Attention Kernel | 42 |

So almost 2x slow down?

---

> We reject this defeatism. With a little bit of work, we _can_ understand the root causes of our nondeterminism and even solve them! We hope that this blog post provides the community with a solid understanding of how to resolve nondeterminism in our inference systems and inspires others to obtain a full understanding of their systems.

Love this Can Do collaborative attitude in the blog.

