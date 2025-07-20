---
title: "Building, launching, and scaling ChatGPT Images"
tags:
   - scalability
   - OpenAI
   - ChatGPT
   - engineering challenges
   - image generation
link: https://newsletter.pragmaticengineer.com/p/chatgpt-images
date: 2025-07-20
summary: "OpenAI's launch of ChatGPT Images achieved unprecedented scale, attracting 100 million new users and generating 700 million images within its first week. The team utilized Python, FastAPI, C, and Temporal for a robust tech stack. Faced with higher-than-expected demand, they transitioned from synchronous to asynchronous processing to enhance system resilience and manage workloads. The architecture effectively isolated ChatGPT Images traffic from other services to mitigate outages. This rapid adaptation exemplifies best practices in scaling AI services while addressing reliability and performance challenges amid explosive user growth."
---

[![The Pragmatic Engineer](https://substackcdn.com/image/fetch/$s_!6TJt!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5ecbf7ac-260b-423b-8493-26783bf01f06_600x600.png)](https://newsletter.pragmaticengineer.com/)

# [The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/)

SubscribeSign in

[Deepdives](https://newsletter.pragmaticengineer.com/s/deepdives/?utm_source=substack&utm_medium=menu)

# Building, launching, and scaling ChatGPT Images

### ChatGPT Images is OpenAI’s biggest launch yet, with 100 million NEW users generating 700 million images in the first week. But how was it built? A deepdive with OpenAI’s engineering team

[![Gergely Orosz's avatar](https://substackcdn.com/image/fetch/$s_!CPFa!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F58fed27c-f331-4ff3-ba47-135c5a0be0ba_400x400.png)](https://substack.com/@pragmaticengineer)

[Gergely Orosz](https://substack.com/@pragmaticengineer)

May 13, 2025

∙ Paid

212

[6](https://newsletter.pragmaticengineer.com/p/chatgpt-images/comments)

15

Share

ChatGPT is the fastest-growing app of all time: from its launch in November 2022, it took the AI chat assistant only 12 months to hit 100M weekly active users. And new figures show that growth is speeding up. ChatGPT Images released at the end of March, and an incredible 100 million _new_ users signed up in the first week. This load was far higher than OpenAI had expected and prepared for, but the launch passed with no major outages.

Afterwards, I sat down with two engineering leaders deeply involved in ChatGPT Images: [Sulman Choudhry](https://www.linkedin.com/in/sulmanc/) (Head of Engineering, ChatGPT) and [Srinivas Narayanan](https://www.linkedin.com/in/srinivasnarayanan/) (VP of Engineering, OpenAI). In this article, they share previously-unreleased details about the Images project, and behind-the-scenes details of how the team pulled the launch off.

For extra context, check out a previous deepdive with the ChatGPT team, including [how OpenAI ships so fast](https://newsletter.pragmaticengineer.com/p/inside-openai-how-does-chatgpt-ship), and [the real-world scaling challenges they solved](https://newsletter.pragmaticengineer.com/p/scaling-chatgpt?utm_source=publication-search).

Today, we cover:

1. **Launch.** Higher-than-expected load from the start, going viral in India, and getting up to 1 million new users _per hour_ signing up.

2. **How ChatGPT Images works.** Image tokens, a decoder, multiple passes to generate an image, and also the tech stack: Python, FastAPI, C, and Temporal.

3. **Changing the engine while speeding on the highway.** What to do when your system struggles under rising load. The ChatGPT team rewrote image generation on-the-fly from synchronous to asynchronous, with users noticing none of this effort.

4. **Reliability challenges.** The load on ChatGPT Images overwhelmed other OpenAI systems, and was higher than the team had expected. Major outages were avoided thanks to months spent isolating systems, doing regular load testing, and ongoing efforts to monitor and alert for reliability.

5. **Extra engineering challenges.** Third-party dependencies, an unbelievable “vertical growth spike”, and new users adding unexpected load by hanging around.

6. **From “GPU constrained” to “everything constrained.”** A year ago, ChatGPT was heavily GPU constrained. Having solved that bottleneck, the new bottleneck is “everything constrained”.

7. **How does OpenAI keep shipping so rapidly?** Infra teams’ #1 focus is on shipping fast, blurred roles across engineers/researchers/PMs/designers, the heavily used DRI role, and more.


_As every deepdive, this one also reveals new details about how OpenAI’s engineering team operates and on engineering challenges in building and operating ChatGPT. Other related deepdives from last year:_

- [Inside OpenAI: how does ChatGPT ship so quickly?](https://newsletter.pragmaticengineer.com/p/inside-openai-how-does-chatgpt-ship)

- [Scaling ChatGPT: five real-world engineering challenges](https://newsletter.pragmaticengineer.com/p/scaling-chatgpt)


_This article is from the [Real-world engineering challenges series](https://newsletter.pragmaticengineer.com/t/real-world-engineering-challenges). See [all others here](https://newsletter.pragmaticengineer.com/t/real-world-engineering-challenges)._

## 1\. Launch

OpenAI keeps launching new features at a rapid pace. In one month, they launched:

- 5 March: [ChatGPT 4.5](https://x.com/OpenAI/status/1897346510821711959) – a new model

- 6 March: ChatGPT for MacOS [code editing abilities](https://x.com/OpenAIDevs/status/1897700857833193955) within IDEs

- 11 March: [Agent Tools](https://x.com/OpenAI/status/1899501967946465637) for developers

- 13 March: Python-powered [data analysis](https://x.com/OpenAI/status/1900308446211432484) – allowing things like running regressions on test data

- 20 March: voice agents with new audio models launched [in the API](https://x.com/OpenAI/status/1902763432300122450)


Then, on Tuesday, 25 March 2025, OpenAI released Image Generation using the 4o model:

[![](https://substackcdn.com/image/fetch/$s_!-s59!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d4a8ee0-e2b9-42b5-8f92-1956e36e819d_1172x1304.png)](https://substackcdn.com/image/fetch/$s_!-s59!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d4a8ee0-e2b9-42b5-8f92-1956e36e819d_1172x1304.png) _Announcement of ChatGPT’s image generation feature was an AI image. Source: [X](https://x.com/OpenAI/status/1904602845221187829)_

It’s hard to predict if a launch will achieve “cut through” by becoming an event in itself. ChatGPT’s head of engineering, Sulman Choudhry, reveals this wasn’t widely expected of ChatGPT Images, internally:

> “At the scale that we're at now with ChatGPT, we thought we were as ready as can be for any launch. After all, we've done dozens of launches – including some very massive ones – in the past several months. However, the Images launch turned out to be orders of magnitude larger than anything we've seen so far.
>
> It was also the first massive launch that happened after we’d scaled out already. It’s of an unexpected scale which I was surprised we had to deal with.”

Sulman calls the launch the craziest of his entire career – and this from someone who scaled Facebook Video to 5 billion _daily_ views back in 2014. The team designed ChatGPT Images expecting to drive meaningful growth similar to the [DALL-E 3 images feature](https://openai.com/index/dall-e-3/) launched in October 2023. _But they simply did not expect as much growth as what happened._

The plan was to initially release ChatGPT Images to paying subscribers, and then free users later on the same day. However, as things unfolded it was decided to postpone launching to free users:

[![](https://substackcdn.com/image/fetch/$s_!MkAz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcf414edc-6c32-4f92-9bcd-2cacfc5080e8_1192x316.png)](https://substackcdn.com/image/fetch/$s_!MkAz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcf414edc-6c32-4f92-9bcd-2cacfc5080e8_1192x316.png) _ChatGPT Images’ rollout to free users was delayed by huge demand from paid users. Source: Sam Altman [on X](https://x.com/sama/status/1905000759336620238)_

But the OpenAI team wanted to get Images in front of free users, so despite the high ongoing load, a day later (on 27 March) they started a gradual rollout to free users. At this point, traffic ratched up, big time.

#### Viral in India

As soon as free users got access to ChatGPT Images, usage in India blew up: celebrities in the country shared images created by ChatGPT in the Ghibli animation style, such as India’s most famous cricketer, Sachin Tendulkar:

[![](https://substackcdn.com/image/fetch/$s_!raU1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4bf9d144-4f35-4ab6-a159-bb7f79f14ae2_1182x1002.png)](https://substackcdn.com/image/fetch/$s_!raU1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4bf9d144-4f35-4ab6-a159-bb7f79f14ae2_1182x1002.png) _Translation: “I heard this is trending. So I thought, what if Ghibli made cricket?” Source: Sachin Tendulkar [on X](https://x.com/sachin_rt/status/1905227258564124710)_

The Prime Minister of India, Narendra Modi, was depicted in images recreated in Ghibli style:

[![](https://substackcdn.com/image/fetch/$s_!CG-E!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fab0f0a25-f0dc-40f5-9dbd-86a8dd750ec9_1180x1246.png)](https://substackcdn.com/image/fetch/$s_!CG-E!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fab0f0a25-f0dc-40f5-9dbd-86a8dd750ec9_1180x1246.png) _Graphics of the Indian Prime Minister generated by ChatGPT Images. Source: MyGovIndia [on X](https://x.com/mygovindia/status/1905563843364790471)_

Srinivas told me:

> “This launch quickly became really special for me: my entire family was in India and they also started sharing old pictures recreated with ChatGPT, just like the rest of the country. The feature really hit big in India.”

Ghibli-style generation has remained one of the most common use cases – and one I’ve played around with by turning existing photos into cheerful, anime-style images.

#### Launch stats

The team worked around the clock to ensure paying users could keep generating images, and preparing for the launch to free users. Five days after everyone got access, the load was still high enough that additional work was needed to keep things up and running:

[![](https://substackcdn.com/image/fetch/$s_!zBXo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6e704fee-6a0a-4c2e-90e9-a292073ac676_1182x236.png)](https://substackcdn.com/image/fetch/$s_!zBXo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6e704fee-6a0a-4c2e-90e9-a292073ac676_1182x236.png) _Load higher than expected, five days post launch. Source: Sam Altman [on X](https://x.com/sama/status/1906210479695126886)_

On day six, 31 March, yet another viral spike added one million users in just one hour:

[![](https://substackcdn.com/image/fetch/$s_!u_fd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb57e70cc-1ee8-45cd-ad86-853dbb316cbc_1190x324.png)](https://substackcdn.com/image/fetch/$s_!u_fd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb57e70cc-1ee8-45cd-ad86-853dbb316cbc_1190x324.png) _Source: Sam Altman [on X](https://x.com/sama/status/1906771292390666325)_

Launch stats:

- **100 million:** new users signing up in the first week of the feature’s release

- **700 million**: images generated in the first week

- **1 million:** _new_ users signing up during a one-hour period on day six of the launch


Despite unexpectedly high traffic, ChatGPT avoided hard outages like the site going down, and maintained availability for existing users. At peak load, latency did regress, but the team prioritized keeping the service accessible. They kept the site responsive by applying rate limits and increasing compute allocations to stabilize performance. Shortly after the peak, they returned to normal rate limits and brought latency back to acceptable levels.

A rule of thumb the ChatGPT engineering team uses is to intentionally prioritize access over latency. So, at times of unexpected growth, latency is often the first tradeoff made to keep the platform up.

## 2\. How ChatGPT Images works

Here’s how image generation works, as described by Sulman:

> You ask ChatGPT to draw something, and then:
>
> 1. **Image tokens** convert the description into a grid of discrete image tokens. These tokens natively encode image content.
>
> 2. **Decoder** progressively renders image tokens into an image.
>
> 3. **Rinse and repeat for multiple passes:** when you generate an image, it is very blurry to start with and then gradually becomes clearer. This is the decoder refining the tokens into a crisp image through multiple passes.
>
> 4. **Integrity and safety:** throughout rendering, there are processes to ensure the image adheres to content and community standards. If not, rendering is aborted.
>
> 5. **Finishing rendering**: after several passes, the image starts to crispen up, and then is rendered to the user.

Here’s an image generated by these steps:

[![](https://substackcdn.com/image/fetch/$s_!N_CU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff87b5823-2482-466c-be94-d519d1b8aca0_1398x1036.png)](https://substackcdn.com/image/fetch/$s_!N_CU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff87b5823-2482-466c-be94-d519d1b8aca0_1398x1036.png) _How ChatGPT Images work, generated as a flow chart by ChatGPT Images. The first image shows the image generation in progress. Note how the model mis-spelled “description” in the final image: this is part of the non-deterministic nature!_

Another feature of ChatGPT images is that you can iterate on a generated image with new prompts. This operation takes the existing image (with tokens) and applies a new prompt on top, meaning it’s possible to tweak an image:

[![](https://substackcdn.com/image/fetch/$s_!TY0z!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F965abddf-c188-4abb-80bc-8b25265fd540_1312x1006.png)](https://substackcdn.com/image/fetch/$s_!TY0z!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F965abddf-c188-4abb-80bc-8b25265fd540_1312x1006.png) _A tweaked image using grey arrows and a globe background. Left: the image being generated. Right: the final image_

“Tweaking” an existing image is a practical feature, but it involves a lot more resource usage because the same compute operations execute each time a “tweaked” image is generated.

#### Tech stack

The technology choices behind the product are surprisingly simple; dare I say, pragmatic!

- **Python:** most of the product’s code is written in this language.

- **[FastAPI](https://fastapi.tiangolo.com/):** the Pythonframeworkused for building APIs quickly, using standard Python type hints. As the name suggests, FastAPI’s strength is that it takes less effort to create functional, production-ready APIs to be consumed by other services.

- **C:** for parts of the code that need to be highly optimized, the team uses the lower-level C programming language

- **[Temporal](https://temporal.io/)**: used for asynchronous workflows and operations inside OpenAI. _Temporal is a neat workflow solution that makes multi-step workflows reliable even when individual steps crash, without much effort by developers. It’s particularly useful for longer-running workflows like image generation at scale_


## 3\. Changing the engine while speeding on the highway

The ChatGPT team designed Images to be a synchronous product: when an image starts rendering, it needs to finish in a synchronous way. If the process is interrupted, there is no way to restart it, and while an image is rendering, it continues using GPU and memory resources.

The problem with this setup is that it can’t handle peak load by taking advantage of excess capacity at non-peak times. Sulman recounts how the team decided to rewrite image generation engine, while dealing with rapidly-rising load:

> “It was the first or second night after Images launch, and demand was bigger than we’d expected. The team got together and we decided that to keep the product available and keep the service up and running for all users, we needed to have something _asynchronous_ – and fast!
>
> **Over a few days and nights, we built an entirely asynchronous Images product.** It was a bunch of engineers rolling their sleeves up – and we kicked off a parallel workstream to get this new implementation ready. All the while, a bunch of us worked on keeping the site up and running under the intense load.
>
> Once the asynchronous product was ready, we were able to “defer” the load on our systems: for free users, we would route that traffic to an asynchronous system when load was too high. These requests would get queued up and once our system had extra cycles to spare, we got to generating those images.
>
> This meant that we traded off latency (time to generate free images) for availability (being able to generate images)”.

#### Isolating other OpenAI systems

A viral launch is usually great news, except when it takes down other parts of the system! In the case of ChatGPT, the product is used by paying users (many of whom are developers), as well as larger enterprises on enterprise plans. Ideally, ChatGPT Images’ unprecedented load should not impact other systems. But due to the increased load, several underlying infrastructure systems were impacted:

- **File systems** storing storing images hit rate limits

- **Databases**: OpenAI’s database infrastructure got overloaded because the rapid growth was unexpected.

- **Authentication and onboarding:** the authentication and new user signup systems got so much load that they came close to tipping over


OpenAI has always had strict reliability standards for the OpenAI API, and many systems were isolated from ChatGPT traffic.

However, there were still some shared components for which there was a plan to isolate, which hadn’t happened yet; such as a couple of compute clusters, and a shared database instance. Seeing the sudden surge and impact on otherwise independent systems made the team speed up their isolation work. They decoupled non-ChatGPT systems from the ChatGPT infrastructure, and most OpenAI API endpoints stayed stable during the Images-related spike, thanks to prior work on isolation. They also wrapped up the work of isolating non-ChatGPT endpoints from ChatGPT infra.

#### Improving performance while finding new capacity

Images encountered a compute bottleneck, so the team started to push changes that improved performance and they sought quick performance wins, even before capacity was increased. Srinivas (head of engineering, OpenAI) recalls:

> “When you're moving quickly, you can easily have too much tech debt accumulated, including code that is not particularly optimized. One of our bottlenecks was our database, so our team started to look for database queries that were taking too many resources. Looking closer, it was clear that some of these were doing unnecessary things.
>
> So, on the spot, we had a spontaneous workstream form of people working through the night to figure out how to make our existing code more efficient. We made changes to existing systems to use fewer resources. At the same time, we had other teams working hard to bring up new capacity across systems like filesystems and databases.”

## 4\. Reliability challenge

ChatGPT working reliably with higher-than-expected load was key to the successful launch. Here’s how the team prioritized this non-functional requirement.

## This post is for paid subscribers

[Subscribe](https://newsletter.pragmaticengineer.com/subscribe?simple=true&next=https%3A%2F%2Fnewsletter.pragmaticengineer.com%2Fp%2Fchatgpt-images&utm_source=paywall&utm_medium=web&utm_content=163483933)

[Already a paid subscriber? **Sign in**](https://substack.com/sign-in?redirect=%2Fp%2Fchatgpt-images&for_pub=pragmaticengineer&change_user=false)
