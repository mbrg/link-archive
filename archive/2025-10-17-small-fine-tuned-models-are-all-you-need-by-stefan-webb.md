---
date: '2025-10-17'
description: Oumi’s latest blog post highlights the effectiveness of small fine-tuned
  models compared to larger general-purpose models like GPT-4. A study showed that
  six out of ten small models outperformed GPT-4 across 31 diverse tasks, emphasizing
  their potential for task-specific applications with lower compute costs and faster
  inference times. The article suggests that the adoption of these models is hindered
  by perceived development complexities and misconceptions regarding training data
  needs. Oumi aims to streamline this process, advocating for small, efficiently fine-tuned
  models as viable alternatives in generative AI deployments.
link: https://blog.oumi.ai/p/small-fine-tuned-models-are-all-you
tags:
- Generative AI
- NLP
- machine learning
- small models
- fine-tuning
title: Small Fine-tuned Models are All You Need - by Stefan Webb
---

[![Oumi's Blog](https://substackcdn.com/image/fetch/$s_!wxdl!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa9c5c922-6d4a-4d95-badf-73c60185188b_1010x1010.png)](https://blog.oumi.ai/)

# [Oumi's Blog](https://blog.oumi.ai/)

SubscribeSign in

![User's avatar](https://substackcdn.com/image/fetch/$s_!ctPE!,w_64,h_64,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc4eeb722-8810-421b-96da-68a5782d2d55_800x800.jpeg)

Discover more from Oumi's Blog

Oumi's blog and newsletter offering insights on the latest developments in Generative AI with a focus on Agents, plus tips on what you can build with Oumi, the community-driven open-source library for foundation model development.

Subscribe

By subscribing, I agree to Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

Already have an account? Sign in

# Small Fine-tuned Models are All You Need

### But the devil is in the details—how can you get them right?

[![Stefan Webb's avatar](https://substackcdn.com/image/fetch/$s_!ctPE!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc4eeb722-8810-421b-96da-68a5782d2d55_800x800.jpeg)](https://substack.com/@stefanoumi)

[Stefan Webb](https://substack.com/@stefanoumi)

Oct 16, 2025

7

[1](https://blog.oumi.ai/p/small-fine-tuned-models-are-all-you/comments)

Share

[![](https://substackcdn.com/image/fetch/$s_!RSKq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84ee70a7-9414-4536-9b11-5fdc41f3951c_1536x1024.png)](https://substackcdn.com/image/fetch/$s_!RSKq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84ee70a7-9414-4536-9b11-5fdc41f3951c_1536x1024.png) Our 7B contender lands a left jab on hapless ChatGPT

_The evidence is overwhelming._ Small fine-tuned models can outperform large general-purpose models like GPT-5 at tasks for which they have been specialized. And by a huge margin! Since small models require far less compute, they save on inference costs and reduce latency to users, as well.

_But what exactly is the evidence?_ And is it all sunshine and rainbows?In this post, we’ll discuss a case-study from mid-2024 comparing the performance of small fine-tuned models to ChatGPT on a variety of real-world tasks, including:

- **Biomedical**: Recognizing chemicals and diseases.

- **Natural language**: Writing an apt headline for a given article.

- **Coding**: Generating an SQL query for a given table and question.

- **Reasoning**: Deciding whether a hypothesis follows from a given set of premises.

- **Mathematics**: Solving high-school math problems.


Also, we’ll scrutinize why small models may not yet be used ubiquitously across GenAI development, and investigate some of the finer points of when and how our claim is true.

## 📊 A large-scale empirical study of fine-tuned models

### Overview

But first, what exactly do we mean by a small foundation model? As always, the size is in the eye of the beholder. An informal definition, however, is that a small model is two orders-of-magnitude smaller than the largest state-of-the-art model in a given domain. For example, DeepSeek-R1 contains 671 billion parameters, so we could define a small model as having around 7 billion parameters.

In mid-2024, an applied AI research team conducted one of the first large-scale empirical studies on fine-tuning small models (Zhao et al., 2024). The researchers chose 31 tasks across a wide range of domains (see above), and fine-tuned 10 small base models on each task.

The questions being investigated included:

- How does task-specific performance compare between a small base-model and its fine-tuned variant?

- How does task-specific performance compare between small fine-tuned models and large general purpose ones?

- Does the difference in performance between small fine-tune models and large general purpose ones vary between tasks?


### Models

The small base models were versions of Llama, Mistral, Zephyr (from Hugging Face), Phi, and Gemma released prior to February 2024. They all have less than 8 billion parameters, a permission license like Apache 2.0, and can be fine-tuned on consumer-grade GPUs. For the strong model baseline, GPT-4 and GPT-3.5-Turbo were used.

### Metrics

The metrics used to evaluate each task varied depending on the nature of the task. For example, the authors used accuracy for classification tasks, (1 - mean average error) for regression tasks, and a metric comparing n-grams for generation tasks. If we were to re-run this experiment today, we might wish to use LLM-as-a-Judge for the generation tasks.

### Training

The method of fine-tuning used was LoRA (Low Rank-Adaption), which, at a high-level, works by freezing the base model weights and training a much smaller set of parameters expressing divergence from the base model. This contrasts with fine-tuning all weights and is a type of parameter-efficient fine-tuning.

For the more technically minded, the models were trained for 2,500 steps of batch size 16 (taking into account gradient accumulation) on a rank-8 LoRA using 4-bit precision without optimizing for the training hyperparameters. In layman’s terms, what this means is that each model could be fine-tuned on a single consumer-grade GPU card with less than 24 GB memory using the same configuration file.

### Results

[![](https://substackcdn.com/image/fetch/$s_!E6M3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e13ef99-3c55-4e94-9ffb-edc660614916_2048x1116.png)](https://substackcdn.com/image/fetch/$s_!E6M3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e13ef99-3c55-4e94-9ffb-edc660614916_2048x1116.png)

The main finding from the study (see above figure) was that, for the tasks considered, 6 of the 10 small models outperformed GPT-4 on average after fine-tuning. And all 10 smaller models outperformed GPT-3.5-Turbo. We see significant improvements from fine-tuning small base models relative to the base model (i.e., the length of the red bars).

Another interesting finding was that the improvement in performance from fine-tuning and the gap between GPT-4 and the fine-tuned model was largest for tasks in the GLUE benchmark, which are primarily traditional NLP problems. The fine-tuned models didn’t do as well when compared to GPT-4 on coding and math reasoning problems. This might not be so surprising given that the small base models capture fine-grained statistics from a large corpus of text, or rather, natural language, and these pre-February 2024 models weren’t pretrained explicitly for coding and math reasoning.

One thing to keep in mind is that there have been many advances in open-source LLMs since the release of this study. Think of the recent advancements in dealing with long context lengths, more efficiently using a model’s parameters, and training for coding and reasoning with Reinforcement Learning, to name a few. On the other hand, strong base models have gotten stronger - think GPT-5. It would be interesting to repeat this study with the resources of late-2025 and I posit that fine-tuning on more recently released base models such as Qwen3-4B-Instruct would close the gap on coding and reasoning performance.

## 💬 Discussion

So, why then aren’t small LLMs and VLMs ubiquitous? Why aren’t they used in the majority of GenAI applications and products built in late-2025? I’d like to put forward some hypotheses:

### Extra development costs over an out-of-the-box LLM

Anecdotal reports from our industry partners have been that earlier attempts at productionizing smaller fine-tuned floundered on long and costly development cycles, especially when compared to an out-of-the-box strong LLM. This has been one of the main motivations for the development of Oumi’s Enterprise Platform, in that we solve this problem with clever automation and recent research. We can eliminate custom AI development costs so the development cycle takes mere hours, rather than months, and you can enjoy the benefits of smaller models without the downsides. We’ll elaborate in the coming weeks.

### Lack of training data or misconceptions about the scale required

There may be a misconception that big data is required for successful fine-tuning or that it is too difficult to obtain training data for a custom task. In fact, as we’ll investigate in upcoming posts, a small model can be successfully fine-tuned with as little as 1000 samples, and in many cases the performance is actually better training on small, carefully curated data. Also, it is possible to synthesize data for custom tasks so this doesn’t require masses of human labor. We’ll examine both of these points in upcoming articles.

### Fear of catastrophic forgetting or loss of generalization

Another common concern for fine-tuning is that the model will experience what is known as “catastrophic forgetting”, where it loses knowledge and task performance that it had prior to fine-tuning, overfitting to the new training data. This is one area where it matters to get the details right. Catastrophic forgetting is not generally a problem for parameter efficient fine-tuning methods, like LoRA, and recent research has shown how RL avoids the loss of generalization that a fine-tuned model experiences on other tasks. Similarly, we’ll go into more depth on these points in an upcoming post.

### Misunderstanding about the role of fine-tuning

A common misunderstanding is that the main reason to fine-tune a model is to impart domain specific knowledge. Then—as the argument goes—you shouldn’t fine-tune because RAG (Retrieval Augmented Generation) can do this more efficiently and performantly. We agree: RAG is a much better way to bring new _knowledge_ into your system. Where fine-tuning really shines is for teaching the model _capabilities_, examples of which are classification, reasoning, coding, and general tool usage.

Does this agree with your experience? Why or why not, and is there something you think I’ve missed? I welcome your comments below.

[Leave a comment](https://blog.oumi.ai/p/small-fine-tuned-models-are-all-you/comments)

## → What’s next?

[![](https://substackcdn.com/image/fetch/$s_!yPlN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5b35482-2539-40fe-8ae0-3e138d1976e2_2459x1351.png)](https://substackcdn.com/image/fetch/$s_!yPlN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5b35482-2539-40fe-8ae0-3e138d1976e2_2459x1351.png)

In this post, we’ve examined a single piece from the mountain of empirical evidence that small fine-tuned foundation models can outperform large general-purpose ones. They have higher task-specific performance, faster and more economical inference, to name a few. We touched upon some of the nuances in this claim and in future posts, we’ll dive deeper into the details, looking at more recent work.

Notwithstanding, a key takeaway from our discussion on why small foundation models haven’t been universally adopted is that you need to get the details right to enjoy their cost and performance benefits, and it requires technical expertise and intelligently designed infrastructure to get the details correct.

> Here at Oumi, we’re specialists in the art of fine-tuning custom AI models for your application. _And we do it in hours, not months._

Oumi’s platform can quickly and cheaply build a smaller fine-tuned model for your application outperforming GPT-5, and we’d love to hear from you if you’re interested; why not set up a time to chat?

[Schedule a video call with Oumi](https://calendly.com/d/ctcx-nps-47m/chat-with-us-get-early-access-to-the-oumi-platform)

We’re also providing early access to Oumi’s Enterprise Platform for select industry partners. So pick up the metaphorical phone and let’s start the non-metaphorical conversation!

_As Always, Stay Hungry and Happy Hacking!_ 🧑‍💻🤖🚀

**[Stefan Webb, Lead Developer Relations Engineer, Oumi](https://www.linkedin.com/in/stefan-webb/)**

## Resources

- [Oumi homepage](https://oumi.ai/)

- [Oumi open-source quickstart](https://oumi.ai/docs/en/latest/index.html)

- [Zhao et al.](https://arxiv.org/pdf/2405.00732) _[LoRA Land: 310 Fine-tuned LLMs that Rival GPT-4, A Technical Report.](https://arxiv.org/pdf/2405.00732)_ [arxiv.org. 2024.](https://arxiv.org/pdf/2405.00732)

- [Hu et al. LoRA:](https://arxiv.org/abs/2106.09685) _[Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)_ [.](https://arxiv.org/abs/2106.09685) [arxiv.org](http://arxiv.org/) [. 2021.](https://arxiv.org/abs/2106.09685)


Thanks for reading Oumi's Blog! Subscribe for free to receive new posts and support my work.

Subscribe

[![Min's avatar](https://substackcdn.com/image/fetch/$s_!I0gZ!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffc26194f-e0c9-4818-92e4-16aee8e16f2a_144x144.png)](https://substack.com/profile/393159843-min)

[![Jeremy Greer's avatar](https://substackcdn.com/image/fetch/$s_!AOFH!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0817a203-c325-4a3c-a822-9df017a9528a_144x144.png)](https://substack.com/profile/392761758-jeremy-greer)

[![Stefan Webb's avatar](https://substackcdn.com/image/fetch/$s_!ctPE!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc4eeb722-8810-421b-96da-68a5782d2d55_800x800.jpeg)](https://substack.com/profile/363147405-stefan-webb)

[![Michael Schuler's avatar](https://substackcdn.com/image/fetch/$s_!YZBo!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3533d52f-85a4-48e8-834c-10e4dbbd6b3b_144x144.png)](https://substack.com/profile/392763689-michael-schuler)

7 Likes

7

[1](https://blog.oumi.ai/p/small-fine-tuned-models-are-all-you/comments)

Share

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

[![Jeremy Greer's avatar](https://substackcdn.com/image/fetch/$s_!AOFH!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0817a203-c325-4a3c-a822-9df017a9528a_144x144.png)](https://substack.com/profile/392761758-jeremy-greer?utm_source=comment)

[Jeremy Greer](https://substack.com/profile/392761758-jeremy-greer?utm_source=substack-feed-item)

[19h](https://blog.oumi.ai/p/small-fine-tuned-models-are-all-you/comment/167030862 "Oct 16, 2025, 1:42 PM")

Liked by Stefan Webb

The ability to match or exceed GPT-4 performance on a 7B cannot be overstated - something that also tends to help is a fine-tuned models ability to consistently produce outputs in the correct format. System instructions only do so much...

Expand full comment

Like (2)

Reply

Share

TopLatestDiscussions

[Hours, Not Months – The Custom AI Era is Now](https://blog.oumi.ai/p/hours-not-months-the-custom-ai-era)

[When we started Oumi, we set out to build a better future for AI – grounded in the benefits of open source.](https://blog.oumi.ai/p/hours-not-months-the-custom-ai-era)

Oct 9•
[Manos Koukoumidis](https://substack.com/@mkoukoumidis)

9

[5](https://blog.oumi.ai/p/hours-not-months-the-custom-ai-era/comments)

![](https://substackcdn.com/image/fetch/$s_!ef02!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67b283c0-7fea-4460-940e-d8034b47372a_2459x1351.png)

[Compete to Curate Smarter Vision-Language Data—And Win Big at NeurIPS 2025](https://blog.oumi.ai/p/compete-to-curate-smarter-vision)

[Originally posted June 18, 2025](https://blog.oumi.ai/p/compete-to-curate-smarter-vision)

Sep 14•
[Stefan Webb](https://substack.com/@stefanoumi)

1

[View comments (0)](https://blog.oumi.ai/p/compete-to-curate-smarter-vision/comments)

![](https://substackcdn.com/image/fetch/$s_!8pWI!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5057534f-e5b3-40a9-82e2-68e76b45af04.tif)

[Training Frontier Reasoning VLMs for the 2025 NeurIPS DCVLR Workshop with Oumi](https://blog.oumi.ai/p/training-frontier-reasoning-vlms)

[Originally published July 31, 2025](https://blog.oumi.ai/p/training-frontier-reasoning-vlms)

Sep 14•
[Stefan Webb](https://substack.com/@stefanoumi)

1

[View comments (0)](https://blog.oumi.ai/p/training-frontier-reasoning-vlms/comments)

![](https://substackcdn.com/image/fetch/$s_!YI_8!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F09e9ea21-c722-41ba-8201-1b0c9270208c.tif)

See all

Ready for more?

Subscribe
