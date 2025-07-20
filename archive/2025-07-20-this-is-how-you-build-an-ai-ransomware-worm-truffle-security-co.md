---
title: "This is how you build an AI Ransomware Worm ◆ Truffle Security Co."
tags:
   - Ransomware
   - AI Security
   - Hacking Techniques
   - Malware Development
   - Large Language Models
link: https://trufflesecurity.com/blog/this-is-how-you-build-an-ai-ransomware-worm
date: 2025-07-20
summary: "A demonstration of an AI-powered ransomware worm highlights significant security risks as smaller LLMs become capable of running on consumer devices. The worm utilizes techniques like RLHF and vector search to execute hacking operations autonomously, with a Python supervisor managing tasks from reconnaissance to exploitation. Notably, the model can bypass refusal vectors that prevent it from facilitating hacking activities. The potential for AI-assisted malware development raises alarm over accelerated financial incentives, indicating a looming threat where sophisticated worms could manifest independently and challenge current cybersecurity defenses."
---

[Learn how AI coding assistants can introduce security risks—register for the webinar](https://trufflesecurity.com/webinars/are-llms-teaching-developers-to-hardcode-api-keys)

TRUFFLEHOG

[CUSTOMERS](https://trufflesecurity.com/customers)

COMPANY

RESOURCES

[LOG IN](https://trufflehog.org/)

[Contact Us](https://trufflesecurity.com/contact)

Dylan Ayrey

[**The Dig**](https://trufflesecurity.com/blog)

May 9, 2025

# This is how you build an AI Ransomware Worm

![](https://framerusercontent.com/images/QaJr85hoCYMZZeUSiV7HloTxelY.png?scale-down-to=512)

![](https://framerusercontent.com/images/QaJr85hoCYMZZeUSiV7HloTxelY.png?scale-down-to=512)

A little while ago when I saw how capable smaller LLM were becoming (the kind that can run on a smart phone), I became increasingly concerned someone might be able to package one into malware.

I started to worry that the next generation of ransomware worms were going to have LLMs embedded into them, helping them troubleshoot, capable of exceeding (or augmenting) the ~$10 billion dollar price the [NotPetya non-AI worm cost the world](https://www.wired.com/story/notpetya-cyberattack-ukraine-russia-code-crashed-the-world/).

So I went ahead and built one, a hacking LLM capable of self replication, and presented it at BsidesSF. You can view this presentation here:

This menacing hacking bot had several alignment techniques to get it to cooperate well, including:

- RLHF (Reinforcement Learning from Human Feedback)

- Fine tuning

- Vector search for relevant hacking guides


In the end, the worm had no external dependancies, was capable of full self propagation weights and all, and I estimate had hacking capabilities about on par with a teenager.

This is discernibly different from many claims floating around about existing AI worms that rely on OpenAI or other 3rd party services. Those worms can easily be shut down centrally by the 3rd party they depend on. This worm cannot be centrally shut down.

# Why on earth did you do this?

To show everyone it's coming. The financial incentives for this type of worm make it inevitable. NotPetya authors made tens of millions from their ransoms; if you buy that a similar worm could be made more infectious with AI, even by a small amount, the exponential nature of worms puts hundreds of millions of dollars up for the taking. It's not a matter of if one gets released into the wild, it's when and by who.

# But what about…?

I mentioned LLM's were getting capable of running on a smart phone, here's a 3b parameter model:

That being said, you still get refusals by most of the popular LLM's when asking to hack things:

![](https://framerusercontent.com/images/dzrxsW4KvN4ASDbrKmYigyWZk.png)

To bypass this refusal, I was forwarded (by the author!) a very interesting white paper on how refusals are stored in LLMs: [https://arxiv.org/abs/2406.11717](https://arxiv.org/abs/2406.11717)

To understand what the paper means when it says Refusal Is Mediated by a Single Direction, you have to understand all facts or ideas in LLM's are stored in vector space as coordinates. Typically when LLM's are trained, they pack all these facts into vector space, and then they undergo a series of alignment steps to get them to behave well. The last step is typically safety alignment.

This step makes the models do things like refuse to hack, or refuse to build nuclear weapons.

As it turns out, there is a single vector in this space that's moderating whether or not the model returns facts about hacking or refuses to do so. This means a lot of the hacking we want to do may already be in its head.

To demonstrate this, I used a method of RLHF to remove this refusal vector, without actually teaching the model anything about hacking. This took less than 30 minutes on a gaming rig, of me simply selecting which output I liked best, A or B, and poof, the model now knew how to hack things.

![](https://framerusercontent.com/images/I0Ln8jnAT7Y0ON9Mimvv0FWAn7Q.png)

So now we have 2 key ingredients to make our worm, small powerful models that take up only 5-15gb of storage, and the ability to get those models to help hack things without refusing.

# The rest of the worm

The LLM able to help us hack things is great and all, but something needs to keep the model on task, instructing it which host to hack, providing it tools like code execution, out of the box scripts for self propagation and ransomware, etc…

This is where I'll introduce the idea of a supervisor. The supervisor starts and stops the LLM, and monitors its output. The supervisor is a python script.

![](https://framerusercontent.com/images/DAGVEguYJX5Fl4DdJGStk2DGAs.png)

The supervisor controls if the LLM is in pre-exploit or post-exploit mode. In pre-exploit mode it picks a host at random from all the network interfaces the infected machine sits on, recons it with tools like NMAP, and then feeds that recon into the LLM with instructions to hack the chosen host.

In post exploit mode it uses tools like TruffleHog to look for credentials such as SSH, NTLM, Browser session keys, API keys, etc… then feed them into the LLM to leverage for spreading.

The supervisor waits until the LLM outputs <code>code</code> and then it breaks the flow, runs the code, and returns that code output back into the LLM.

![](https://framerusercontent.com/images/6yJu6oD8j8OhUcUDgfveFOa8Tg.png)

The supervisor provides the exploitation script to spread once the LLM gets code execution.

# The fine tuning step

One thing I noticed is the LLM I had originally chosen ( [Llama advanced reasoning 8b](https://deepseek-ai/DeepSeek-R1-Distill-Llama-8B)) after the refusal had been removed still struggled to use the <code> blocks I had instructed it to use.

To fix this, I added an additional alignment step through the use of fine tuning, to condition the LLM how to use <code> blocks.

I also took this opportunity to try and reinforce a few thousand CVE's in the model, to increase it's abilities to hack things, and I through in a few troubleshooting steps like adding the -k flag to curl if there's a self signed certificate, etc..

I used a more powerful LLM both to transform existing guides I found [on the internet](https://huggingface.co/datasets/WhiteRabbitNeo/Code-Functions-Level-Cyber), and to build new ones based on CVE's and CVE POC data I could find..

![](https://framerusercontent.com/images/dqnTZWuLMfoGxXhXvUzezkieE.png)

All and all this was the most expensive part of the worm. It cost about $1000 in cloud compute.

![](https://framerusercontent.com/images/tWaoUsDwXOIGGllOMu4tlquWDFM.png)

You can see the before and after of the supervisor instructing it to hack a host with SSH exposed. Night and day. Pre-training it didn't even use <code>, after training it tried SSHing in, recognized a brute force attack was the way to go, tried to run one with metasploit, saw metasploit wasn't installed (whoops I meant to have it there…) and went on to try and install it…

![](https://framerusercontent.com/images/Pz8eVsOd1UNysmpUhraJxEYXsuE.png)

What about a CVE though? Something more complex than brute forcing SSH. Something that might require specific knowledge of an exploit, and a sequence of specially crafted payloads…

I tasked it to go after Elasticsearch with a known CVE and well… to be frank, it fell on its face. It didn't know the right CVE, didn't know which requests to send. Here's a snippet of its thinking step:

![](https://framerusercontent.com/images/a1PaoVzQInPVYppzgcHothrncuY.png)

This should make some sense… the guides that I fed it, only one of them contained this specific CVE.

![](https://framerusercontent.com/images/xdMhIWQbVNFoF4zgsYAWoKBjz4w.png)

I likely would have needed to include hundreds of examples of each CVE, to really reinforce them, and I wasn't gonna spend $100k on this thing…

# I fixed it with RAG

At this point I realized, the answer was staring me in the face. I already generated all these hacking guides… All I needed to do was have the supervisor implement a simple vector search against the guides based on the recon data. If nmap found Elasticsearch is exposed, search for guides on hacking elastic search.

![](https://framerusercontent.com/images/B82vqeQsftzhmaXlFFYM3Ukg1hU.png)

Then we can feed each guide into the LLM, one at a time, monitor the output a certain number of tokens, reset and have it work on the next guide, repeat over and over until we get execution.

![](https://framerusercontent.com/images/9CMF64WSeQdoAJlENDeuxjxURI.png)

It was surprising how good the model got at hacking CVE's at this point… I would put it at a host with a CVE, and as long as there was a guide for it, the supervisor was pretty good at getting the model to pop the host…

![](https://framerusercontent.com/images/GDSJ9jlHkcViezrf5xWD5yO62SY.png)

Then I just repeated the process for post exploitation.

![](https://framerusercontent.com/images/sydSGlzX29cBrzKbnWz3urC12g.png)

Assemble hundreds of guides for how to hack every credential type you can imagine. For example, a guide for a GitHub browser session token, would include pushing evil code to GitHub. A guide for an SSH key would include checking known\_hosts, and SSHing into stuff, etc… the supervisor would look for credentials using a number of tools, find the right guide for the credential, feed it into the model.

Once it exhausted all the post exploitation credentials it could find, the supervisor puts the model back into pre-exploitation mode hunting for CVEs with recon data.

# Did you really do it?

Yes and no. I did write the supervisor, I did do all the alignment steps, I did prove out it could both do pre-exploitation and post exploitation. I stopped short when it came to writing the replication code. It wasn’t that it would have been difficult, actually I independently validated the worm could run on almost any target system, but the fact that this thing existed, even in a lab setting, was becoming dangerous.

Morris's worm in 1988 that infected 20% of the internet, was an accident. Robert Morris didn't mean to take down the internet. Samy Kamkar's worm in 2005 was also an accident. Samy didn't mean to take down MySpace. I wasn't looking to cause a lab leak in 2025.

One of the main take aways I want people to get from reading this is that AI safety teams [putting out blogs](https://www.anthropic.com/news/anthropics-responsible-scaling-policy) claiming current-generation models are capable of unsafe behavior, are categorically wrong. The disconnect likely comes from AI safety teams lacking required knowledge of modern hacking and red teaming techniques.

I think it's actually a good thing we have access to some of these open source models so we can run these lab experiments and do our best to prepare for what's coming.

The truth is, if you graph worm costs over time, we were already on track for a 100 billion dollar worm, with our without AI, AI is just going to accelerate us there a lot faster.

![](https://framerusercontent.com/images/NrpfAfas4BPI9o41MjSUBgeXUs.png)

All that said, I stongly recommend watching [the video I put up on youtube](https://www.youtube.com/watch?v=s4RKXTC8iuM), it goes into a lot more detail

## [More from THE DIG](https://trufflesecurity.com/blog)

Thoughts, research findings, reports, and more from Truffle Security Co.

[![](https://framerusercontent.com/images/BCjuoyGZuvI6gtpfhAB6bZ8KVs.png)\\
\\
Jul 18, 2025\\
\\
**Guest Post: GCP CloudQuarry: Searching for Secrets in Public GCP Images**](https://trufflesecurity.com/blog/guest-post-gcp-cloudquarry-searching-for-secrets-in-public-gcp-images) [![](https://framerusercontent.com/images/BjTcuiTOBzjGW9YlfBj0vYivUs.png)\\
\\
Jul 11, 2025\\
\\
**How to Scan Force Pushed Commits for Secrets**](https://trufflesecurity.com/blog/how-to-scan-force-pushed-commits-for-secrets) [![](https://framerusercontent.com/images/HGNIfDeHr823mfdZmv9gZM1Bok.png)\\
\\
**Guest Post: How I Scanned all of GitHub’s “Oops Commits” for Leaked Secrets**](https://trufflesecurity.com/blog/guest-post-how-i-scanned-all-of-github-s-oops-commits-for-leaked-secrets)

STAY STRONG

DIG DEEP

TRUFFLEHOG

[Open-source](https://trufflesecurity.com/trufflehog)

[Enterprise](https://trufflesecurity.com/trufflehog-enterprise)

[Analyze](https://trufflesecurity.com/trufflehog-analyze)

NEW!

[Forager](https://trufflesecurity.com/security)

[Security](https://trufflesecurity.com/security)

[Integrations](https://trufflesecurity.com/integrations)

[Pricing](https://trufflesecurity.com/pricing)

[CUSTOMERS](https://trufflesecurity.com/customers)

COMPANY

[About](https://trufflesecurity.com/about)

[Careers](https://trufflesecurity.com/careers)

[Press](https://trufflesecurity.com/press)

[FAQ](https://trufflesecurity.com/faq)

[Contact us](https://trufflesecurity.com/contact)

RESOURCES

[Blog](https://trufflesecurity.com/blog)

[Newsletter](https://trufflesecurity.com/newsletter)

[Library](https://trufflesecurity.com/library)

[Events](https://trufflesecurity.com/events)

[Videos](https://trufflesecurity.com/videos)

[GitHub](https://github.com/trufflesecurity)

[Enterprise docs](https://docs.trufflesecurity.com/)

[Open-source docs](https://github.com/trufflesecurity/trufflehog#trufflehog)

[How to rotate](https://howtorotate.com/)

[Brand assets](https://trufflesecurity.com/branding)

NEW!

DOING IT THE RIGHT WAY

SINCE 2021

[#trufflehog-community](https://join.slack.com/t/trufflehog-community/shared_invite/zt-pw2qbi43-Aa86hkiimstfdKH9UCpPzQ) [#Secret Scanning](https://discord.gg/8Hzbrnkr7E)

© 2025 Truffle Security Co.

[Privacy policy](https://trufflesecurity.com/privacy-policy)

[Terms and conditions](https://trufflesecurity.com/terms-conditions)

[Data processing agreement](https://trufflesecurity.com/data-processing-agreement)

[Acceptable use policy](https://trufflesecurity.com/acceptable-use-policy)
