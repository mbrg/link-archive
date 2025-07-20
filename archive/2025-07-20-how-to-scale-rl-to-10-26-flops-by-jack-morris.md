---
title: "How to scale RL to 10^26 FLOPs - by Jack Morris"
tags:
   - next-token-prediction
   - machine-learning
   - language-models
   - AI-training
   - reinforcement-learning
link: https://blog.jxmo.io/p/how-to-scale-rl-to-1026-flops
date: 2025-07-20
description: "The concept of scaling reinforcement learning (RL) to 10^26 FLOPs focuses on leveraging web-scale data for training large language models (LLMs). Current RL methodologies, which utilize reward systems predominantly based on verifiable tasks, have foundational limitations in generalizing across diverse problem sets. A proposed approach suggests combining next-token prediction with RL to teach models to reason. This hybrid framework aims to utilize the expansive knowledge base of the internet while making reasoning learning more scalable and efficient. The engineering challenges remain, particularly in optimizing computational resources for reward verification in various domains, notably code and math."
---

[![Token for Token](https://substackcdn.com/image/fetch/$s_!ySE4!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b4d4a83-97c1-455a-a39b-46563262fcdb_1024x1024.png)](https://blog.jxmo.io/)

# [Token for Token](https://blog.jxmo.io/)

SubscribeSign in

![User's avatar](https://substackcdn.com/image/fetch/$s_!QCZr!,w_64,h_64,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9bb7f676-fa98-45ab-9564-23bfec7fef26_1241x1241.png)

Discover more from Token for Token

language models and the future of AI

Over 1,000 subscribers

Subscribe

By subscribing, I agree to Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

Already have an account? Sign in

# How to scale RL to 10^26 FLOPs

### A roadmap for RL-ing LLMs on the entire Internet

[![Jack Morris's avatar](https://substackcdn.com/image/fetch/$s_!QCZr!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9bb7f676-fa98-45ab-9564-23bfec7fef26_1241x1241.png)](https://substack.com/@jxmnop)

[Jack Morris](https://substack.com/@jxmnop)

Jul 10, 2025

42

[11](https://blog.jxmo.io/p/how-to-scale-rl-to-1026-flops/comments)

4

Share

_TLDR: Reinforcement learning (RL) is the next training technique for building frontier-level AI models. To make it better, we need to train on more data. The current approach of scaling many environments simultaneously is messy and complicated. Instead, I propose we find a way to do next-token prediction on the Web using RL. This way, we learn to reason from general web data, instead of just math and code._

* * *

I’ve spent a good part of the past year in denial.

Thanks for reading! Subscribe for free to receive new posts and support my work.

Subscribe

I was in denial because when [OpenAI released o1](https://openai.com/index/learning-to-reason-with-llms/), and explained their paradigm of _test-time compute_, I thought it was a good idea but mostly a way to get better performance out of models of fixed size. After all, letting models ‘think for longer’ by generating more tokens lets them do more internal computation.

[![](https://substackcdn.com/image/fetch/$s_!Dxsi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdbe8a574-8953-446a-b6fc-dc3fb43915f0_1980x1113.png)](https://substackcdn.com/image/fetch/$s_!Dxsi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdbe8a574-8953-446a-b6fc-dc3fb43915f0_1980x1113.png) [The o1 release](https://openai.com/index/learning-to-reason-with-llms/) from OpenAI was the first demonstration of a new type of language model, one that could think for longer to generate better answers.

So I wasn’t that surprised that these new models, termed _reasoning models_, gave better answers. And I especially wasn’t surprised when I found out these answers mostly came on problems that inherently require lots of computation, like difficult math and engineering test questions.

Don’t get me wrong: I always thought reasoning models were _interesting_. It’s cool to me that they generate “thinking traces” before giving answers (although the thinking traces might not be very reliable). And it’s amazing that the models were trained with reinforcement learning, a foundational technique in machine learning that was generally understood to be difficult to use effectively for real problems.

But I still thought of myself as a scale maximalist: all that really mattered, I thought, was training bigger models on more data. Anything else (read: reasoning models) appeared to be a coping mechanism, just a way to get by while we wait for the hardware needed to train bigger models.

I’ve spent the past few months working on RL research at Meta. It took a bit of time but I’ve come full-circle: something far more nuanced is happening with reasoning models. RL isn’t just a way to give models more compute. **RL training really is teaching models something** _**different**_ **, a way to use compute to generate better answers** given finite model capacity. Through RL, models are clearly learning something that they’re not getting from pretraining.

### Two waves of AI scaling

The AI research-into-production cycle moves through a few distinct phases. First, we as a community identify a new learning paradigm. Second, we find the correct datasets for training and design evaluations to know when our models are getting better, and by how much. And third, we scale it to all hell.

This cycle has happened already, exactly once. Pretraining. It started with the innocuous observation that models can learn quite a lot when trained on internet text data using next-token prediction. We realized that this gives intelligence improvements in just about every domain. And then we scaled.

[![](https://substackcdn.com/image/fetch/$s_!6hjW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F23e84ae2-5f9b-4748-aa99-11200f2ea70b_1536x1024.png)](https://substackcdn.com/image/fetch/$s_!6hjW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F23e84ae2-5f9b-4748-aa99-11200f2ea70b_1536x1024.png) We spent 2022–2024 scaling language model pretraining: first making models bigger, and now working to pack as much knowledge we could into models of various scales. We’ll spend the next several years scaling post-training using RL.

And to be clear, pretraining research is ongoing. We’re still figuring out how to scale our models via bigger datacenters and better hardware and more efficient algorithms. And we’re gathering more and better data every year. But the upper bound of pretraining performance is really clear. To build better models, we need to give them more parameters and train them on bigger datasets. This is what the AI labs have been working on for three years or so now.

But as the dust settles on the pretraining frenzy, reasoning models are showing us a new way to scale. We’ve found a way to make models better that’s independent of the number of training tokens or model size.

### The murky path to RL scaling starts with _data_

We’ve identified a new paradigm: learning to _reason_. But reasoning models are [in their GPT-3 era](https://www.mechanize.work/blog/the-upcoming-gpt-3-moment-for-rl/): they’re trained on small datasets to do a narrow selection of tasks. We have a brittle proof-of-concept in the reasoning models of 2025. These models have achieved state-of-the-art scores on a small number of tasks, mostly expert-level math and coding questions.

In the case of pretraining, the path to progress was very clear. Models can learn via next-token prediction on just about _any_ data, so we could simply scrape the entire Web and feed it to the models. And once we’d done that it became clear that our models were too small and we needed to make them much, much bigger.

But RL training is different. Let’s briefly remind ourselves how RL works:

Models like o1 are trained with _verifiable rewards_, meaning that after thinking and generating answers, we teach models by encouraging them to think more of the thoughts that led to correct answers, and less of the thoughts that led to incorrect answers. This is how RL algorithms like [PPO](https://arxiv.org/abs/1707.06347) (what o1 probably uses) and [GRPO](https://arxiv.org/abs/2402.03300) (the algorithm behind DeepSeek R1) work. They don’t teach, they incentivize.

So clearly we can only train RL models on tasks where we can score answers based on correctness. This is the idea behind _verifiability_, an RL buzzword used to describe tasks with a well-defined automatic scoring function. (The o1-style RL training paradigm is usually called _RLVR_, reinforcement learning with verifiable rewards, as to be distinguished from _RLHF_, or reinforcement learning from human feedback.)

Unfortunately, most things aren’t automatically verifiable. There aren’t perfect computer programs that can tell you whether an essay is good, for example, or an explanation.

In fact, things that we know how to automatically verify tend to be in the scientific domain. For example, [OpenThoughts](https://huggingface.co/datasets/open-thoughts/OpenThoughts-114k), a recently-released dataset of training data for reasoning models, contains four categories, Code, Math, Science, and ‘Puzzle’:

[![](https://substackcdn.com/image/fetch/$s_!CQ0O!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8df13457-bc45-4202-a49a-d524523416be_1174x1296.png)](https://substackcdn.com/image/fetch/$s_!CQ0O!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8df13457-bc45-4202-a49a-d524523416be_1174x1296.png) The recent [OpenThoughts dataset](https://huggingface.co/datasets/open-thoughts/OpenThoughts-114k) contains verifiable tasks in Math, Science, Coding, as well as a small dataset of puzzles. (What is the Puzzle task, I wonder?)

Ok, so we can see that there are at least four domains that contain verifiable problems that we can train on. But there are many open problems here. Are those all the verifiable things that exist? Are they equally valuable? During training should we randomly alternate between them or [train separate models and then average](https://arxiv.org/abs/2203.05482)?

In fact, in typical RL setups, we don’t even understand the marginal value of a _single_ training example. One recent paper, [Reinforcement Learning for Reasoning in Large Language Models with One Training Example](https://arxiv.org/abs/2504.20571), demonstrated that training on just a single example with thousands of different attempts of reasoning can actually produce a very good model:

[![](https://substackcdn.com/image/fetch/$s_!p87E!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F22ce64ec-421f-4564-873e-6e813b016a59_1364x400.png)](https://substackcdn.com/image/fetch/$s_!p87E!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F22ce64ec-421f-4564-873e-6e813b016a59_1364x400.png) [A recent paper](https://arxiv.org/abs/2504.20571) showed close to on-par reasoning performance from just learning a reasoning process from a _single training example_.

It’s also interesting to note the x-axis in the above graph: training only runs for 2000 steps. And that’s typical. Right now, these models are typically only trained for a few hundred or at most a few thousand steps. In the pretraining era, we often trained models on _trillions_ of tokens, which meant millions of training steps.

This is mostly a compute issue: each step of RL requires _sampling reasoning tokens_, which is expensive and just difficult from a software perspective. The infrastructure to do this sort of thing is challenging and requires a lot of new engineering, since we aren’t used to doing generation at all during training, let alone at each step.

Mark my words: before we know it we’ll be running millions of steps of RLVR too.

### RL compute scales unevenly

There are many practical engineering problems that need to be solved to scale RL.

In the pretraining days, training was a very homogenous workload, a very real-time continuous process. Batch of text passes through the model, we compute losses and backpropagate once. Queue the next back of text. This was simple and straightforward to optimize.

When we do RL, training infrastructure has to get more complicated. Gradient steps happen much less frequently and (depending on our chosen hyperparameters) we spend a lot more time generating thinking tokens.

Luckily, we’ve spent the last year or two making LLM inference super fast, and we can take advantage of these improvements here. In particular there are two really good libraries for doing inference ( [SGLang](https://github.com/sgl-project/sglang) and [vLLM](https://github.com/vllm-project/vllm)) that make this part ~10x faster than naive python inference code. That helps a lot.

Another systems problem arises when we actually compute verifiable rewards. In the case of math problems this is usually pretty easy. Most datasets have answers computed ahead of time, so we can simply check if the final answer is correct and score accordingly (In practice, [formatting makes this process slightly more complicated](https://gist.github.com/willccbb/4676755236bb08cab5f4e54a0475d6fb).)

But in domains besides math, verification quickly becomes expensive. This is especially noticeable in the code domain, which is where a lot of AI labs are focusing their efforts right now.

Remember that each domain needs a domain-specific “verifier”, a system that provides rewards that guide LLMs to generate better outputs. In the case of code, this usually involves running some code and scoring based on the code’s output. Given an LLM-generated answer to a coding problem, we may need to run a bunch of unit tests and count the number of ones that pass to provide a reward.

There are a lot of people working on this right now. Doing better and faster verification, running it in parallel, scaling it properly. In some cases, the training bottleneck isn’t anything related to the model – it’s not inference or backpropagation that slows things down, but the time it takes to compile and execute model code.

[![](https://substackcdn.com/image/fetch/$s_!YfNa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7fe7d41-0a9c-4de0-a97e-58631aaa0576_1445x1182.png)](https://substackcdn.com/image/fetch/$s_!YfNa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7fe7d41-0a9c-4de0-a97e-58631aaa0576_1445x1182.png) The new [DGX B200 GPU servers from NVIDIA](https://www.nvidia.com/en-us/data-center/dgx-b200/) cost $500K a pop and provide around 10^17 FLOPS for training or inference. Unfortunately, our systems for doing RL on LLMs are pretty primitive and can’t get anywhere near this level of performance yet.

Since [a single B200 costs over $500K](https://wccftech.com/nvidia-blackwell-dgx-b200-price-half-a-million-dollars-top-of-the-line-ai-hardware/), any time training spends bottlenecked by CPU execution is a big waste of money.

One path to scaling RL is optimizing this kind of system: making verifiers faster and more reliable, optimizing the new generate-before-backprop [training pipeline](https://github.com/volcengine/verl), and designing [clever systems](https://arxiv.org/html/2412.01152v1) that let us scale RL across datacenters.

In addition to all these systems-level improvements, we’ll need to build [lots of new environments](https://github.com/open-thought/reasoning-gym) to try and learn diverse skills via RL training. Oh, and no one really knows what the right skills are to learn via RL, or how to combine them. So we’ll have to try lots of different combinations and train many models. And we can try averaging them in different ways via some kind of [model souping](https://arxiv.org/abs/2203.05482) (also known as model merging). We’ll just run lots of evaluations to find which combination of environments and souping produces the best model. This sounds difficult, doesn’t it? And quite messy.

What if I told you there was another way?

### What does it mean to be verifiable?

If we want to scale RL in verifiable settings, we should probably start by figuring out which things are verifiable in the first place. It’s my feeling that people have been throwing this word around a lot, but there’s no clear definition.

It all comes down to what we can train into the models. If we can check a model output and provide a score, that’s good enough.

Wait– but isn’t this how language modeling works _already_?

### Pretraining for reasoning with next-token prediction

Before making my proposal, let me start with listing a few core tenets that I believe about the current state of AI:

1. **The only data we’ve found that really “works” (i.e. helps us build more intelligent models) is web-scale pretraining data**. Ilya Sutskever famously compared all the human text on the internet to [a reserve of fossil fuel](https://www.youtube.com/watch?v=YD-9NG1Ke5Y): it’s exceptionally useful, but finite.

2. Reasoning, at its core, is a way to get better performance out of smaller models. It’s not doing anything more magical. Crucially, we’re getting limited new signal from the verifier itself; RL with verification is just a way to elicit capabilities that already exist within models. ( [This is a common belief about RL.](https://limit-of-rlvr.github.io/))

3. **There is nothing special about math and code**. These modalities happen to lie in a space that’s difficult to model with a reward model (so prior approaches didn’t work super well) but easy to verify. And we happen to care about them ( [automating coding seems especially valuable)](https://cursor.com/en/blog/series-c). But we should be able to learn to reason from any type of data.

4. And finally, **we haven’t fully saturated models with Internet data**. Today’s models don’t seem to [have enough capacity](https://arxiv.org/abs/2505.24832) to memorize the entire Internet. Additional pretraining on Web data should still give us a performance boost – and might be enough to learn to reason.

5. **Next-token prediction is verifiable.** This is perhaps the central argument I’m making. The current strategy of checking if a math problem has been answered correctly is spiritually no different than confirming whether a model has outputted the proper next tokens.


Putting all this together, I’m betting that the “right way” to scale RL is by unifying it with next-token prediction. We should teach models to reason by practicing reasoning at scale on the vast diversity of data available on the Web.

Learning to reason via next-token prediction.

[![](https://substackcdn.com/image/fetch/$s_!tZ5F!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb827aab5-7961-4e9b-ab48-5b666a8553ae_1744x1288.png)](https://substackcdn.com/image/fetch/$s_!tZ5F!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb827aab5-7961-4e9b-ab48-5b666a8553ae_1744x1288.png) The proposed framework of learning to reason via next-token prediction.

This shows a comparison of the new paradigm demonstrated on a math problem. Normal next-token prediction is guessing which tokens come next. Typical RLVR allows the model to ‘think’ for a few tokens and then rewards it for outputting the right thing. Our idea of reasoning with next-token prediction (RNTP) would allow the model to think and then reward it based on the next-token prediction loss of the outputs in the <answer> tag. It’s a hybrid between traditional language model pretraining and the new reasoning model RL training.

[![](https://substackcdn.com/image/fetch/$s_!hhru!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F56425c6f-5cab-4cad-ae74-4749561d227c_800x404.png)](https://substackcdn.com/image/fetch/$s_!hhru!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F56425c6f-5cab-4cad-ae74-4749561d227c_800x404.png)

Grok 2 was trained on more FLOPs than GPT-4. Apparently Grok 3, which came out later, was trained on around 10^26 FLOPs, which would put it above the top of this graph. But that was all supervised learning. How do we scale RL to use this much compute?

### What do we even need RL for?

Now that we’ve stripped things down to their base components, it might not be obvious what benefit we get from doing reinforcement learning, if any.

The answer lies in the <think> tokens. In the picture above, we generated everything between <thinks> directly from the model. _There’s no supervision for this_.

In other words, we’re trying to get the model to learn to reason without knowing what reasoning should look like. We just sample lots of things from the model and encourage it to do the things that get rewards. If there was ground-truth reasoning, we could use the typical supervised training techniques to train the model to output the proper reasoning chains.

But in the real world, there’s no ground-truth for reasoning, so we can’t do supervised learning. And in fact we want it this way – this is the magic of reinforcement learning. We’re _hoping_ that the model will discover reasoning chains that are more useful than anything we could ever write ourselves.

### Scaling reasoning via next-token prediction

If you’ve read this far, and you agree this idea makes sense, you might be thinking about how it could be tricky to implement.

And in fact, you’re right. This is where the research comes in. Almost all research that matters comes from figuring out how to implement and scale ideas that make sense from first principles.

For example: what exactly is the reward? Do we give the model a point for guessing a token correctly? Should we reward it more for multiple tokens in a row? Perhaps we use a string-similarity reward like BLEU score, [as was common in machine translation in 2018](https://arxiv.org/abs/1808.08866). We could do some kind of [self-evaluation](https://arxiv.org/abs/2506.18254), where a decent model can look at its own outputs and decide which ones should get rewards. Perhaps we filter tokens by [entropy](https://arxiv.org/pdf/2506.08007) and use that to determine which to reason about. Or maybe we want to [account for confidence in the reward](https://arxiv.org/abs/2505.19590), and give the model more points for being confidently correct.

Another question: how many times should you “reason” within a single text chunk? One approach is to insert reasoning tokens at a random position per-chunk. Or perhaps we allow models to reason multiple times throughout each chunk. But then we’d have to figure out whether how many times can learn from a given text chunk with different reasoning patterns before memorization starts to occur.

There are additional difficulties that arise when switching from math and code to _general_ reasoning. One reason we like math and code is because they’re difficult for base models to do “from scratch” but often easy to learn via reasoning. This won’t be the case with general text: some tokens are already extremely low-entropy, and therefore easy to predict; other tokens are nearly impossible, and will never be guessed correctly with any amount of reasoning.

[![](https://substackcdn.com/image/fetch/$s_!AwyA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05d693ef-e1b1-4a78-afde-1983105526ac_1196x992.png)](https://substackcdn.com/image/fetch/$s_!AwyA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05d693ef-e1b1-4a78-afde-1983105526ac_1196x992.png) Even the best pretraining datasets are still a long way from perfect.

Andrej Karpathy recently noted that if you [actually look at samples from a typical pretraining dataset](https://huggingface.co/datasets/HuggingFaceFW/fineweb), they’re quite ugly, and there is a lot of obvious noise. One benefit of scale is that it irons out many of these low-level idiosyncrasies: after a lot of training, much of this noise gets averaged away. It’s possible that this would happen with my proposed RL training scheme. **If we train for long enough, on enough tokens, we might not even care what the exact reward or reasoning schema looks like.**

### But wait, didn’t somebody try this already?

Those among us who diligently troll ArXiv for the latest nuggets of progress might recognize that someone recently proposed something like this in a recently released preprint ( [\*Reinforcement Pre-Training](https://arxiv.org/abs/2506.08007)).\\* This research was praised on twitter (the title sounds important, and the figure is funny!) but disappointed a lot of researchers:

[![](https://substackcdn.com/image/fetch/$s_!e2No!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc8f12234-e78c-47fd-b0cd-9afbff8145f0_1126x726.png)](https://substackcdn.com/image/fetch/$s_!e2No!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc8f12234-e78c-47fd-b0cd-9afbff8145f0_1126x726.png) Headlining figure from the recent ‘Reinforcement Pre-Training’ paper, which also proposes the idea of pretraining for RL via next-token prediction.

Headliner figure from the recent ‘Reinforcement Pre-Training’ paper, which also proposes the idea of pretraining for RL via next-token prediction.

To be more specific, this paper proposed something similar to what I’m advocating for: using large unlabeled text datasets and next-token prediction to scale RL! And it has pretraining in the name, just like I was describing.

Alas, it turns out to be a classic case of academic titlegrabbing. What the paper actually does is very specific: they finetune a single model with chain-of-thought to improve single-token outputs for some multiple-choice questions. They’re not actually doing pretraining–just finetuning!– and train on a small subset of questions from [a single math dataset](https://omni-math.github.io/). There aren’t a lot of comparisons to any of the other RLVR papers, so it’s hard to tell whether this thing even works, and if so, when and how well.

Normally I’d file this type of work away as a sort of negative result – if a simpler and more general setting worked, they surely would have tried it in this paper, right? But that’s exactly what I don’t think we should do. My overall point in this piece is that **if something makes sense from first principles, we should keep working on it until we work out all the kinks.**

Making good ideas work often turns out to require significantly more labor than academic researchers expect from a single project. But this is is the price of progress.

### What’s next?

It’s very exciting to me that (a) RL works and (b) no one knows the right way to do it. There is so much opportunity here. One way or another, we will have much better reasoning models in a year or two; it’s just that the path is unclear. Before we can see with clarity, we have a lot to learn. If reasoning next-token prediction turns out to really be the right way to scale RL, we’re going to need to answer all these questions and many more.

* * *

Thanks to my friends Wenting Zhao, Will Brown, and Nishanth Kumar for reading this blog post early and providing helpful feedback.

Thanks for reading! Subscribe for free to receive new posts and support my work.

Subscribe

[![Motoki Wu's avatar](https://substackcdn.com/image/fetch/$s_!ktgL!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F08bbb3b1-3439-40cd-a103-a1a4622bc274_144x144.png)](https://substack.com/profile/866457-motoki-wu)

[![Leo Benaharon's avatar](https://substackcdn.com/image/fetch/$s_!l79E!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6eb78471-0a08-48bb-892f-91bc4d6b9c4d_96x96.jpeg)](https://substack.com/profile/36452329-leo-benaharon)

[![Akhilesh Kumawat's avatar](https://substackcdn.com/image/fetch/$s_!YCNO!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F723b789f-6285-486a-b0bb-9f748caf03d5_144x144.png)](https://substack.com/profile/269088971-akhilesh-kumawat)

[![Vincent Weisser's avatar](https://substackcdn.com/image/fetch/$s_!oqK1!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff08bf3ed-d1ea-421c-9da8-2dab9396e13a_400x400.jpeg)](https://substack.com/profile/757328-vincent-weisser)

[![Samyak Datta's avatar](https://substackcdn.com/image/fetch/$s_!PoVh!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f946e3b-b6e6-45fc-adf3-ca51dca81ec9_460x460.jpeg)](https://substack.com/profile/17665861-samyak-datta)

42 Likes∙

[4 Restacks](https://substack.com/note/p-168023871/restacks?utm_source=substack&utm_content=facepile-restacks)

42

[11](https://blog.jxmo.io/p/how-to-scale-rl-to-1026-flops/comments)

4

Share

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

[![Douglas Summers-Stay's avatar](https://substackcdn.com/image/fetch/$s_!t6Zq!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd6415a1-a3d1-41a3-a735-8f557136a7e6_144x144.png)](https://substack.com/profile/131028757-douglas-summers-stay?utm_source=comment)

[Douglas Summers-Stay](https://substack.com/profile/131028757-douglas-summers-stay?utm_source=substack-feed-item)

[8d](https://blog.jxmo.io/p/how-to-scale-rl-to-1026-flops/comment/134663438 "Jul 12, 2025, 5:36 PM")

Liked by Jack Morris

It's funny, I had the exact same reaction to that cherry cake paper. What I thought it was about before I read it closely is almost exactly the same as your post.

Expand full comment

Like (1)

Reply

Share

[![Thomas DeWitt's avatar](https://substackcdn.com/image/fetch/$s_!Wobr!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9c198e8e-7863-4fd4-b520-e2cd64454c9a_2139x2139.jpeg)](https://substack.com/profile/320886778-thomas-dewitt?utm_source=comment)

[Thomas DeWitt](https://substack.com/profile/320886778-thomas-dewitt?utm_source=substack-feed-item)

[7d](https://blog.jxmo.io/p/how-to-scale-rl-to-1026-flops/comment/134929060 "Jul 13, 2025, 3:38 PM")

Really interesting! This makes a lot of sense to me. It feels closer to how humans learn than pretraining (even if its still a bit different). When I’m learning a difficult thing in a textbook, I spend a lot of time thinking in between reading sentences, and I feel like the models need that too. The current RL paradigm feels more similar to skimming and then repeatedly trying the problems at the end of the chapter.

Expand full comment

Like (1)

Reply

Share

[9 more comments...](https://blog.jxmo.io/p/how-to-scale-rl-to-1026-flops/comments)

TopLatestDiscussions

[There Are No New Ideas in AI… Only New Datasets](https://blog.jxmo.io/p/there-are-no-new-ideas-in-ai-only)

[LLMs were invented in four major developments... all of which were datasets](https://blog.jxmo.io/p/there-are-no-new-ideas-in-ai-only)

Apr 9•
[Jack Morris](https://substack.com/@jxmnop)

245

[20](https://blog.jxmo.io/p/there-are-no-new-ideas-in-ai-only/comments)

![](https://substackcdn.com/image/fetch/$s_!56cS!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6c8b571-bdbe-46cc-aa5c-8fd5e5555b01_720x430.png)

[All AI Models Might Be The Same](https://blog.jxmo.io/p/there-is-only-one-model)

[what can language model embeddings tell us about whales speech, and decoding ancient texts? (on The Platonic Representation Hypothesis and the idea of…](https://blog.jxmo.io/p/there-is-only-one-model)

Jul 17•
[Jack Morris](https://substack.com/@jxmnop)

70

[6](https://blog.jxmo.io/p/there-is-only-one-model/comments)

![](https://substackcdn.com/image/fetch/$s_!X8H_!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F08727245-d2dc-4d17-84d9-258d335e27bb_1024x1024.png)

[Please Stop Talking About AGI](https://blog.jxmo.io/p/we-should-stop-talking-about-agi)

[Why I think Yann Lecun was right about LLMs (but perhaps only by accident)](https://blog.jxmo.io/p/we-should-stop-talking-about-agi)

Feb 21•
[Jack Morris](https://substack.com/@jxmnop)

53

[6](https://blog.jxmo.io/p/we-should-stop-talking-about-agi/comments)

![](https://substackcdn.com/image/fetch/$s_!N3r5!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F295078c0-2a16-4d53-8ba7-0d9cb5ce4fb5_1224x702.png)

See all

Ready for more?

Subscribe
