---
date: '2025-11-14'
description: OpenAI's research on sparse neural circuits seeks to enhance interpretability
  in AI models by training them with significantly constrained connections, allowing
  clearer comprehension of internal operations. Mechanistic interpretability, focusing
  on low-level explanations, is emphasized over traditional dense networks, which
  present complex dependencies. Initial findings suggest that sparse models successfully
  execute simple tasks with disentangled circuits, potentially paving the way for
  scalable interpretability in larger systems. Future work aims to optimize the efficiency
  of training sparse models and extract interpretable features from dense counterparts,
  enhancing the ability to analyze and debug advanced AI systems.
link: https://openai.com/index/understanding-neural-networks-through-sparse-circuits/
tags:
- Sparse Circuits
- Neural Networks
- AI Safety
- Mechanistic Interpretability
- Interpretability
title: Understanding neural networks through sparse circuits ◆ OpenAI
---

Switch to

- [ChatGPT(opens in a new window)](https://chatgpt.com/?openaicom-did=dc8856cd-5140-4e79-bc5b-11034550af92&openaicom_referred=true)
- [Sora(opens in a new window)](https://sora.com/)
- [API Platform(opens in a new window)](https://platform.openai.com/)

Understanding neural networks through sparse circuits \| OpenAI

November 13, 2025

[Research](https://openai.com/news/research/) [Publication](https://openai.com/research/index/publication/)

# Understanding neural networks through sparse circuits

We trained models to think in simpler, more traceable steps—so we can better understand how they work.

[Read the paper(opens in a new window)](https://cdn.openai.com/pdf/41df8f28-d4ef-43e9-aed2-823f9393e470/circuit-sparsity-paper.pdf)

Listen to article

Share

​​Neural networks power today’s most capable AI systems, but they remain difficult to understand. We don’t write these models with explicit, step-by-step instructions. Instead, they learn by adjusting billions of internal connections, or “weights,” until they master a task. We design the rules of training, but not the specific behaviors that emerge, and the result is a dense web of connections that no human can easily decipher.

## How we view interpretability

As AI systems become more capable and have real-world impact on decisions in science, education, and healthcare, understanding how they work is essential. **Interpretability** refers to methods that help us understand why a model produced a given output. There are many ways we might achieve this.

For example, reasoning models are incentivized to explain their work on the way to a final answer. **Chain of thought interpretability** leverages these explanations to monitor the model’s behavior. This is immediately useful: current reasoning models’ chains of thought seem to be informative with respect to concerning behaviors like deception. However, fully relying on this property is a brittle strategy, and this may break down over time.

On the other hand, **mechanistic interpretability**, which is the focus of this work, seeks to completely reverse engineer a model’s computations. It has so far been less immediately useful, but in principle, could offer a more complete explanation of the model’s behavior. By seeking to explain model behavior at the most granular level, mechanistic interpretability can make fewer assumptions and give us more confidence. But the path from low-level details to explanations of complex behaviors is much longer and more difficult.

Interpretability supports several key goals, for example enabling better oversight and providing early warning signs of unsafe or strategically misaligned behavior. It also complements our other safety efforts, such as scalable oversight, adversarial training, and red-teaming.

In this work, we show that we can often train models in ways that make them easier to interpret. We see our work as a promising complement to post-hoc analysis of dense networks.

This is a very ambitious bet; there is a long path from our work to fully understanding the complex behaviors of our most powerful models. Still, for simple behaviors, we find that sparse models trained with our method contain small, disentangled circuits that are both understandable and sufficient to perform the behavior. This suggests there may be a tractable path toward training larger systems whose mechanisms we can understand.

## A new approach: learning sparse models

Previous mechanistic interpretability work has started from dense, tangled networks, and tried to untangle them. In these networks, each individual neuron is connected to thousands of other neurons. Most neurons seem to perform many distinct functions, making it seemingly impossible to understand.

But what if we trained untangled neural networks, with many more neurons, but where each neuron has only a few dozen connections? Then maybe the resulting network will be simpler, and easier to understand. This is the central research bet of our work.

With this principle in mind, we trained language models with a very similar architecture to existing language models like GPT‑2, with one small modification: we force the vast majority of the model’s weights to be zeros. This constrained the model to use only very few of the possible connections between its neurons. This is a simple change which we argue substantially disentangles the model’s internal computations.

![Diagram comparing dense circuits and sparse circuits. The dense version shows two rows of nodes with many interconnecting lines, while the sparse version shows the same layout but with fewer, more selective connections.](https://images.ctfassets.net/kftzwdyauwt9/3IgwdnCJRjTjCJIliNOIub/b1f0a6ec3fae173a75723de47fb67614/IT_Blog_Static01_Desktop_Light__2_.svg?w=3840&q=90)

In normal dense neural networks, each neuron is connected to every neuron in the next layer. In our sparse models, each neuron only connects to a few neurons in the next layer. We hope that this makes the neurons, and the network as a whole, easier to understand.

## Evaluating interpretability

We wish to measure the extent to which our sparse models’ computations are disentangled. We considered various simple model behaviors, and checked whether we could isolate the parts of the model responsible for each behavior—which we term circuits.

We hand-curated a suite of simple algorithmic tasks. For each, we pruned the model down to the smallest circuit that can still perform the task, and examined how simple that circuit is. (For details, see our [paper⁠(opens in a new window)](https://cdn.openai.com/pdf/41df8f28-d4ef-43e9-aed2-823f9393e470/circuit-sparsity-paper.pdf).) We found that by training bigger and sparser models, we could produce increasingly capable models with increasingly simple circuits.

![Scatter plot showing model capability (pretraining loss) on the x-axis against interpretability (pruned circuit size) on the y-axis. Points represent models of different sizes and sparsity levels, with color indicating total parameters and marker size indicating number of nonzero parameters. Arrows label the upper-right direction as “better.”](https://images.ctfassets.net/kftzwdyauwt9/1FZ239wOAcW45PdiS7URYr/20fa2c3f1eea7f422fbc7768015e6171/IT_Blog_Static02_Desktop_Light__2_.svg?w=3840&q=90)

We plot interpretability versus capability across models (lower-left is better). For a fixed sparse model size, increasing sparsity—setting more weights to zero—reduces capability but increases interpretability. Scaling up model size shifts this frontier outward, suggesting we can build larger models that are both capable and interpretable.

To make this concrete, consider a task where a model trained on Python code has to complete a string with the correct type of quote. In Python, ‘hello’ must end with a single quote, and “hello” must end with a double quote. The model can solve this by remembering which quote type opened the string and reproducing it at the end.

Our most interpretable models appear to contain disentangled circuits which implement exactly that algorithm.

![Diagram illustrating an example circuit in a sparse transformer. It shows how specific neurons and attention heads activate in response to input tokens like “(” and “circuits,” with labeled pathways for positive and negative weights, multiplications, nonlinearities, and connections between MLP and attention layers, culminating in output token probabilities.](https://images.ctfassets.net/kftzwdyauwt9/1pKKMlQPqjkLSuP3nv2bSu/9cd54cd1beb6525693c75e14df905512/IT_Blog_Static03_Desktop_Light__2_.svg?w=3840&q=90)

Example circuit in a sparse transformer that predicts whether to end a string in a single or double quote. This circuit uses just five residual channels (vertical gray lines), two MLP neurons in layer 0, and one attention query-key channel and one value channel in layer 10. The model (1) encodes single quotes in one residual channel and double quotes in another; (2) uses an MLP layer to convert this into one channel that detects any quote and another that classifies between single and double quotes; (3) uses an attention operation to ignore intervening tokens, find the previous quote, and copy its type to the final token; and (4) predicts the matching closing quote.

In our definition, the exact connections shown above are sufficient to perform the task—if we remove the rest of the model, this small circuit still works. They are also necessary–deleting these few edges causes the model to fail.

We also looked at some more complicated behaviors. Our circuits for these behaviors (for example variable binding shown below) are harder to explain completely. Even then, we can still achieve relatively simple partial explanations which are predictive of model behavior.

![Diagram highlighting an example sparse-transformer circuit within the Python function get_neighbors. Two assignments to current = set() are boxed, with colored arrows showing which attention heads (labeled with Q/K/V indices) activate to connect each occurrence of the variable current to its usage in the loop.](https://images.ctfassets.net/kftzwdyauwt9/QlxzFQmEJ6KxzbxKessr6/89f5d4968c671183cbeae30ada19af39/IT_Blog_Static04_Desktop_Light__1_.svg?w=3840&q=90)

Another example circuit, in less detail. To determine the type of a variable called `current`, one attention operation copies the variable name into the `set()` token when it’s defined, and another later operation copies the type from the `set()` token into a subsequent use of the variable, allowing the model to infer the correct next token.

## The road ahead

This work is an early step toward a larger goal: making model computations easier to understand. But, there’s still a long way to go. Our sparse models are much smaller than frontier models, and large parts of their computation remain uninterpreted.

Next, we hope to scale our techniques to larger models, and to explain more of the models’ behavior. By enumerating circuit motifs underlying more complex reasoning in capable sparse models, we could develop an understanding that helps us better target investigations of frontier models.

To overcome the inefficiency of training sparse models, we see two paths forward. One is to extract sparse circuits from existing dense models, rather than training sparse models from scratch. Dense models are fundamentally more efficient to deploy than sparse models. The other path is to develop more efficient techniques to train models for interpretability, which might be easier to put in production.

Note that our findings here are no guarantee that this approach will extend to more capable systems, but these early results are promising. Our aim is to gradually expand how much of a model we can reliably interpret, and to build tools that make future systems easier to analyze, debug, and evaluate.

- [2025](https://openai.com/news/?tags=2025)
- [Ethics & Safety](https://openai.com/news/?tags=ethics-safety)
- [Transformers](https://openai.com/news/?tags=transformers)

## Authors

Leo Gao, Achyuta Rajaram, Jacob Coxon, Soham V. Govande, Bowen Baker, Dan Mossing

## Keep reading

[View all](https://openai.com/news/research/)

![5-1 SystemCard ArtCard 1x1](https://images.ctfassets.net/kftzwdyauwt9/6yB8QrkjEuIj8mS0RaKpzL/b57140fc567f52715ac1fcf251692a3e/5-1_SystemCard_ArtCard_1x1.png?w=3840&q=90&fm=webp)

[GPT-5.1 Instant and GPT-5.1 Thinking System Card Addendum\\
\\
PublicationNov 12, 2025](https://openai.com/index/gpt-5-system-card-addendum-gpt-5-1/)

![IndQA > Cover Image](https://images.ctfassets.net/kftzwdyauwt9/5tudNlgnPnUpQULfzVyNjz/b2783e0e63c398de66282e824d98de9e/oai_IndQA_1.1.png?w=3840&q=90&fm=webp)

[Introducing IndQA\\
\\
ResearchNov 3, 2025](https://openai.com/index/introducing-indqa/)

![Introducing Aardvark > Cover Image](https://images.ctfassets.net/kftzwdyauwt9/9nWk5GVnxe20BUU12vsk4/b9822a77ac99d7cd57c4f01e8bb76e80/Aardvark_SEO_Card_1x1.png?w=3840&q=90&fm=webp)

[Introducing Aardvark: OpenAI’s agentic security researcher\\
\\
SecurityOct 30, 2025](https://openai.com/index/introducing-aardvark/)
