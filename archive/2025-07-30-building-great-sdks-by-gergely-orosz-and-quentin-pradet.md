---
date: '2025-07-30'
description: Quentin Pradet's deep dive into SDK development highlights best practices
  for creating user-friendly software development kits, especially relevant in the
  context of LLMs. Key insights include the distinctions between SDKs and APIs, the
  importance of simplifying API usage and robust documentation, and strategies for
  building versatile SDKs—from manual coding to leveraging generators. He also emphasizes
  the critical role of SDK maintainers in ensuring backward compatibility, configurability,
  and effective error handling. As SDKs gain prominence with AI integrations, organizations
  can capitalize on this trend by providing high-quality, open-source SDKs that enhance
  developer experiences.
link: https://newsletter.pragmaticengineer.com/p/building-great-sdks
tags:
- Open Source
- SDK
- Software Development
- API
- Documentation
title: Building great SDKs - by Gergely Orosz and Quentin Pradet
---

[![The Pragmatic Engineer](https://substackcdn.com/image/fetch/$s_!6TJt!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5ecbf7ac-260b-423b-8493-26783bf01f06_600x600.png)](https://newsletter.pragmaticengineer.com/)

# [The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/)

SubscribeSign in

[Deepdives](https://newsletter.pragmaticengineer.com/s/deepdives/?utm_source=substack&utm_medium=menu)

# Building great SDKs

### A guide to creating SDKs that devs – and LLMs – will find a breeze to use, plus an overview of modern approaches for building and maintaining SDKs. By veteran SDK engineer, Quentin Pradet

[![Gergely Orosz's avatar](https://substackcdn.com/image/fetch/$s_!CPFa!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F58fed27c-f331-4ff3-ba47-135c5a0be0ba_400x400.png)](https://substack.com/@pragmaticengineer)

[![Quentin Pradet's avatar](https://substackcdn.com/image/fetch/$s_!BF9y!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6288b4ed-0618-4eb0-84dc-e398297ca9df_1280x1280.jpeg)](https://substack.com/@quentinpradet)

[Gergely Orosz](https://substack.com/@pragmaticengineer)

and

[Quentin Pradet](https://substack.com/@quentinpradet)

Jul 29, 2025

∙ Paid

100

[1](https://newsletter.pragmaticengineer.com/p/building-great-sdks/comments)

3

Share

_Scheduling note: following this deepdive, The Pragmatic Engineer team is off on [summer break](https://newsletter.pragmaticengineer.com/about#%C2%A7publishing-schedule-and-holidays). There will be no articles for the next week and a half, and one podcast episode will be published next week. Normal service resumes on Tuesday, 11 August. Taking an occasional break helps me research and write better during the rest of the year. Thank you for your understanding and ongoing support! Now, on with the latest deepdive:_

As devs, we use software development kits (SDKs) to build any and all functionality for apps. Want to build a cloud service on AWS? You’ll use the AWS SDK. Integrating Stripe to an app? It will be the Stripe SDK. Doing something with Slack? You might reach for the Slack SDK.

Today, SDKs are especially relevant with AI tooling spreading across the industry, since SDKs that are easy to use are more likely to be employed by LLMs, which is an opportunity for companies offering high-quality SDKs to benefit from the “LLM wave.”

But how are great SDKs built, how much work does it take to maintain them – and why not just use an API? For answers to these questions and others, I sought out someone whose bread-and-butter is building SDKs.

[Quentin Pradet](https://www.linkedin.com/in/quentin-pradet/) is a software engineer at Elastic who maintains the Python SDKs, and has spent a decade building and maintaining SDKs. He has been the maintainer of [Apache Libcloud](https://libcloud.apache.org/) (for interacting with cloud providers using a unified API), [urllib3](https://pypi.org/project/urllib3/) (a Python library for HTTP requests), [Rally](https://github.com/elastic/rally) (a Python benchmarking tool), and is currently the maintainer of the Python [Elastisearch client](https://www.elastic.co/docs/reference/elasticsearch/clients/python).

Today, we cover:

1. **What is an SDK?** The name has stuck since SDKs were shipped on physical CD-ROMs in the 1990s.

2. **Why build one?** To simplify API usage, improve documentation, have robust error handling, and more.

3. **How to build an SDK.** The “SDK ladder”: manually-written SDKs, in-house generators, general purpose generators like AWS Smithy, Microsoft TypeSpec, and OpenAPI. As a follow-up, see the article [How Elastisearch and OpenSearch built their SDKs](https://quentin.pradet.me/blog/how-elastisearch-and-opensearch-built-their-sdks.html).

4. **API-first design process.** Instead of writing code first and then creating an API for it, start with the API. It’s easy to do for new codebases / APIs, but can be tricky to retro-fit.

5. **Can we use LLMs to generate SDKs?** You might assume LLMs would shine at generating a Rust SDK based on a Java one, but the reality is different.

6. **The day-to-day of an SDK maintainer.** Answering questions, communicating with users, writing and generating documentation, and more.

7. **SDK engineers: how many are needed?** The rule of thumb used to be that one engineer can maintain one SDK. But with SDK generators, a single engineer can support SDKs written in 4-5 languages. There are limitations to take into account, though.


_With that, it’s over to Quentin:_

* * *

## 1\. What is an SDK?

Historically, an SDK was a collection of development tools: documentation, libraries, frameworks, and even debuggers, which were usually distributed in CD-ROMs, back in the day:

[![](https://substackcdn.com/image/fetch/$s_!mGVW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd022982-77b6-4ecd-9bac-982d5891d9b8_1527x1600.jpeg)](https://substackcdn.com/image/fetch/$s_!mGVW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd022982-77b6-4ecd-9bac-982d5891d9b8_1527x1600.jpeg) _Windows CE Platform SDK on a CD-ROM. Source: [Internet Archive](https://archive.org/details/MPLATSDK.20)_

But today, these tools are obviously no longer bundled in physical form; the software is distributed from package registries, and users – and LLMs – read their docs online. The name SDK has stuck and today refers to libraries that enable third-party developers to use a specific technology, directly. This article focuses on a specific subset: SDKs for HTTP APIs.

**SDKs are different from frameworks.** You can _invoke them_ from the code you write, whereas frameworks _invoke the code_ you write. Therefore, frameworks enforce a specific, opinionated code architecture which SDKs do not.

[![](https://substackcdn.com/image/fetch/$s_!FZNw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F19a30fc3-cd74-4182-9f9d-48a46d9432f1_1456x1086.png)](https://substackcdn.com/image/fetch/$s_!FZNw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F19a30fc3-cd74-4182-9f9d-48a46d9432f1_1456x1086.png) _Difference between an SDK and a framework_

### Why build an SDK for an API when there’s already an API?

The standard way to allow software engineers to integrate products is to offer an HTTP API. However, you’ll notice that some popular consumer companies provide an API without an SDK, such as the social media platform Bluesky, previously covered in the deep dive, [Inside Bluesky’s engineering culture](https://newsletter.pragmaticengineer.com/p/bluesky-engineering-culture). Other companies consider an SDK so valuable that it’s built for internal-only APIs. So, what are its benefits?

Let’s take an Elasticsearch query with a few filters as an example. Without an SDK:

[![](https://substackcdn.com/image/fetch/$s_!l6Dt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe08008e8-084b-4296-8aa0-5f44915cc83f_1826x1444.png)](https://substackcdn.com/image/fetch/$s_!l6Dt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe08008e8-084b-4296-8aa0-5f44915cc83f_1826x1444.png)

Below is the same query with the Elasticsearch Python client, which handles authentication, headers, and error handling. This allows you to think more about queries, and less about how to send them:

[![](https://substackcdn.com/image/fetch/$s_!J5VE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2021c13-1e12-4c3a-8363-03e2c95ea6cf_1838x1164.png)](https://substackcdn.com/image/fetch/$s_!J5VE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2021c13-1e12-4c3a-8363-03e2c95ea6cf_1838x1164.png)

While I like the above because it hits a sweet spot between conciseness and readability for larger codebases, many of our users love the domain-specific language (DSL) module, which is even more concise and Python-like:

[![](https://substackcdn.com/image/fetch/$s_!vTPh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77ebf848-243a-439b-b536-fde1a20a8519_1826x918.png)](https://substackcdn.com/image/fetch/$s_!vTPh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77ebf848-243a-439b-b536-fde1a20a8519_1826x918.png)

## 2\. Why build an SDK?

Conciseness is one reason to build SDKs, as shown in the above example. But there are others:

**Simplify API usage**. Developers can explore the complete API surface from the comfort of their IDE, using autocompletion to see the options. Also, precise types give instant feedback, eliminating an entire class of errors. For example, all Elasticsearch Inference APIs are available under [client.inference](https://elasticsearch-py.readthedocs.io/en/v9.0.2/api/inference.html), and each parameter has a description and type hint. Since SDKs abstract away many concerns in calling an API, this can be done with a few simple lines of code, which helps users and LLMs.

**Improve documentation**. Good SDKs also include documentation tailored to the programming language, such as:

- Reference documentation

- Code examples

- Tutorials

- How-to guides

- Explanations


The [Diátaxis documentation framework](https://diataxis.fr/) is a good way to think about useful documentation:

[![](https://substackcdn.com/image/fetch/$s_!jvGW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37e977da-1919-4b15-8407-105cf3f53071_1600x885.png)](https://substackcdn.com/image/fetch/$s_!jvGW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37e977da-1919-4b15-8407-105cf3f53071_1600x885.png) _The [Diátaxis documentation framework](https://diataxis.fr/) is a good starting point for creating documentation_

Code examples should be available in all languages, so that users and LLMs don’t have to come up with them based on generic API documentation.

Note that your docs will likely [get more visits from LLMs than from people](https://bsky.app/profile/gergely.pragmaticengineer.com/post/3lugdgl4ghc2w), which can be a [challenge for some websites](https://lwn.net/Articles/1008897/). Everything that helps users – such as code samples – will also help LLMs, but you can go one step further and provide Markdown files. Adding \`.md\` to any Elastic doc page will get you the [Markdown source code](https://www.elastic.co/docs/explore-analyze/elastic-inference/inference-api.md). You can also provide a [/llms.txt](https://llmstxt.org/) file to aid LLMs even more.

**Robuster error handling**. SDKs should raise specific exceptions/errors, allowing users to handle errors in fine-grain detail. For example, CouchDB replies to conflicts with an [HTTP 409 Conflict status code](https://docs.couchdb.org/en/stable/replication/conflicts.html), and one third-party Python SDK [provides a ResourceConflict exception](https://github.com/djc/couchdb-python/blob/459bb1ef24587eef2577ad414e1c070e8b0eaff5/couchdb/http.py#L99-L102), which allows applications to react to conflicts easily. Additionally, for idempotent operations, SDKs can be configured to retry automatically on HTTP 429 Too Many Requests status codes, ideally using [exponential backoff and jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/).

**Take more advantage of language features**. Maintainers with intimate knowledge of a language and its ecosystem can improve their SDK in ways that are unique to each language:

- The Elasticsearch Python client supports async/await through [unasync](https://github.com/python-trio/unasync), a library that I maintain, which codegens the sync code from the async code. This is (objectively!) the best way to support async/await in Python.

- JavaScript SDKs should support CommonJS / ES Modules and alternate runtimes such as Deno or Cloudflare workers.

- C# database SDKs could support expression trees for [strongly-typed](https://en.wikipedia.org/wiki/Strong_and_weak_typing) field name access, or LINQ for simple queries.


**Take care of authentication**. Users only have to think of authentication as providing an API key or username/password credentials. SDKs will map this to the correct header or API call, giving clear errors on failures, and differentiating 401 and 403 status codes. For more complex cases, such as Kerberos, the Python Elasticsearch client can also [delegate authentication to the Requests library](https://requests.readthedocs.io/en/latest/user/authentication/).

**Ensure backward compatibility**. Users like nothing less than changing their code to upgrade to a newer version of an SDK: they use an SDK to make their lives easier, not harder! Keeping backward compatibility helps users to upgrade or, put differently, to avoid churn.

Backward compatibility also helps LLMs. For example, in 2021 the Python Elasticsearch client started mandating a URL scheme (http:// or https://) on instantiation, instead of just the hostname. While Claude 3.5 Sonnet always used the newer form in my tests, GPT-4o had an earlier cutoff date, and only caught up in early 2025. For this reason, software engineer Simon Willison [suggests](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#account-for-training-cut-off-dates) favoring popular libraries without significant changes since the training cut-off date, which differs by LLM provider.

If you need to break backward compatibility because you believe it will ultimately help users despite the short-term pain, then it’s ideal to use a long deprecation period, measured in months or years.

**Better configurability support**. SDKs need to adapt to user needs. After years of evolution, the Elasticsearch Python client supports nearly 50 parameters. They configure:

- Authentication using 4 parameters

- SSL using 9 parameters

- Timeouts with 3 params

- Retries with 5

- Serialization with 3

- Node sniffing with 10 ( [node sniffing](https://www.elastic.co/blog/elasticsearch-sniffing-best-practices-what-when-why-how) is specific to Elastisearch: it’s about discovering nodes on startup and not sending requests to dead nodes

- … and a few more!


All these parameters were added to help users achieve their goals. Removing them would also break backward compatibility, so needs to be done carefully. For example, Version 9 of the SDK [removes](https://www.elastic.co/docs/release-notes/elasticsearch/clients/python#elasticsearch-python-client-900-release-notes) parameters which had been marked for deprecation for more than 3 years.

**Measure performance with built-in observability**. Which of your API calls are slow? To answer this question, you should offer observability in your SDKs. While Prometheus is so widely used that you could target it directly, I recommend OpenTelemetry, which is a vendor-neutral standard, and its tooling can export metrics to Prometheus, Datadog, Honeycomb, Elastic APM, etc. Interestingly, the Python [aiohttp](https://docs.aiohttp.org/en/stable/) client goes for a third approach by offering [generic tracing](https://docs.aiohttp.org/en/stable/tracing_reference.html), which grants complete control to the user, but requires custom code and is more complex to adopt.

Other reasons:

- **Provide helpers**. These make users’ lives easier, and can add support for operations when several API calls need to be orchestrated. Examples of helpers include [streaming chat completions](https://github.com/openai/openai-python/blob/e502d3014d8520ce3b29c59abf0fe4a27d447163/helpers.md#streaming-helpers) (in the OpenAI SDK), [auto-pagination](https://docs.stripe.com/api/pagination/auto?lang=node&api-version=2025-01-27.acacia) (in Stripe SDKs), and [bulk inserts](https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html#orm-bulk-insert-statements) (in the SQLAlchemy SDK).

- **Better serialization/deserialization**. The [orjson](https://github.com/ijl/orjson) Python is an example that shines here: it encodes [NumPy arrays](https://numpy.org/doc/stable/reference/generated/numpy.array.html) into JSON [10x faster](https://github.com/ijl/orjson?tab=readme-ov-file#numpy) than the Python standard library. For best performance, you may also need to support protocols other than JSON, such as Apache Arrow.

- **… and more!** Better integration into the ecosystem (e.g., adding LangChain integration to a vector database), supporting lower-level details (e.g. adding compression to reduce bandwidth), or domain-specific features (e.g., an Elastisearch SDK offering better node discovery with node sniffing).


### Reusing an existing SDK

Sometimes, the work involved in creating an SDK can be avoided by making your API compatible with an existing one. Two typical cases are [OpenAI](https://platform.openai.com/docs/libraries) and [AWS S3](https://aws.amazon.com/s3/getting-started/), which offer SDKs in multiple languages.

Most LLM providers develop their own SDK that can utilize the full breadth of their capabilities. However, since OpenAI was the first entrant in this market, many existing applications use the OpenAI SDK, which allows targeting of any base URL. Therefore, many LLM providers support the OpenAI API in addition to their own, so customers can try models without having to rewrite their code. As a result, the OpenAI API is now a standard, supported by LLM providers such as [Google Vertex,](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/call-vertex-using-openai-library) [Amazon Bedrock](https://github.com/aws-samples/bedrock-access-gateway), [Ollama](https://ollama.com/blog/openai-compatibility), and [DeepSeek](https://api-docs.deepseek.com/). These companies compete on model quality, without having to convince developers to adopt a different SDK.

Another example is AWS S3, first introduced in March 2006 – 19 years ago! Today, many storage providers claim to support the S3 API, including MinIO, Backblaze B2, Cloudflare R2, Synology, and more. However, the S3 API continues to evolve.

- Recently, [default data integrity protections](https://aws.amazon.com/blogs/aws/introducing-default-data-integrity-protections-for-new-objects-in-amazon-s3/) added in their SDKs [broke most S3 compatible services](https://xuanwo.io/links/2025/02/aws_s3_sdk_breaks_its_compatible_services/).

- Features such as [read-after-write consistency](https://aws.amazon.com/blogs/aws/amazon-s3-update-strong-read-after-write-consistency/) (2020), and [compare-and-swap](https://aws.amazon.com/about-aws/whats-new/2024/11/amazon-s3-functionality-conditional-writes/) (2024) can be difficult to mimic.


As mentioned in the [Elasticsearch docs](https://www.elastic.co/guide/en/elasticsearch/reference/current/repository-s3.html#repository-s3-compatible-services), many systems claim to offer an S3-compatible API, despite [failing](https://mastodon.online/@davecturner/111336442716327822) to emulate S3’s behavior in full, which has led to some interesting Elasticsearch support cases.

### Should SDKs be open source?

Yes! Simply put, this offers the best developer experience. Using only open source dependencies is a given across many platforms and industries. Nothing would be more frustrating than trying to debug an API call, then realizing you can’t see exactly what the SDK is doing, or being unable to step into a debugger. Open-sourcing an SDK can also help LLMs use it, for example by looking at integration tests. Additionally, since SDKs are aimed at developers, they’re often technical enough to be improved when needed, and to submit a change as a pull request when relevant. This is a great way to grow a community while making users happy.

What about competition, then? Even if AWS S3 and OpenAPI SDKs invite competition, making the SDKs private would hurt them more. However, anything that isn’t published to users can be kept private, as we did at Elastic with the client generators, which are not trivial to replicate.

Finally, are closed source SDKs essential [to fight ad fraud](https://www.appsflyer.com/blog/mobile-fraud/closed-source-sdk-is-essential/)? No! It’s easy to observe requests made by the SDK itself, and the intelligence of an anti-fraud system should be in the API, not the SDK.

In my opinion, SDKs should always be open source.

## 3\. How to build an SDK

When starting an SDK, you need to decide how to build it. I like to think of the options as an “SDK ladder.” Each step requires less work to scale, at the cost of giving up some of your control:

- #1: Manually-written SDKs

- #2: In-house generators

- #3: General-purpose generators

- #4: OpenAPI generators


[![](https://substackcdn.com/image/fetch/$s_!pI98!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e5e3583-7133-4539-97b5-e954169cf2ef_1226x1182.png)](https://substackcdn.com/image/fetch/$s_!pI98!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e5e3583-7133-4539-97b5-e954169cf2ef_1226x1182.png)“SDK ladder:” every step up brings more generalized tooling

### \#1: Manually-written SDKs

For open source projects, the first SDKs are often built by community members and written manually. Since they are independent efforts, they can be incomplete, fragmented, and inconsistent with each other. This happened to Elasticsearch, and users complained about those issues, after which official clients were started [in 2013](https://av.tib.eu/media/19982).

The first version of an SDK often starts with manual coding, where an engineer writes code they think is needed to use a few APIs. They have a problem to solve and throw together a solution, and because the API surface used is small, it’s easy enough to create a high-quality SDK with high-quality code.

**As the SDK grows, the limits of manually coding start to show**. For example:

- It becomes harder to keep up with the evolution of the APIs as engineers add more endpoints, data types, query parameters, and possible responses

- Each SDK has a different level of API coverage (e.g. one SDK could lack accessing an endpoint that is exposed via the API, or support fewer query parameters than what the API exposes)

- SDKs written in different languages need to be kept up-to-date with one another


### \#2: Custom generators

The biggest problem with manually writing code is the lack of consistency, so how can you keep several SDK clients consistent with each other? The most straightforward way is to generate all SDKs from one specification.

This is the approach Elastic took for Elasticsearch, whose SDKs are generated from the [Elasticsearch specification](https://github.com/elastic/elasticsearch-specification). This specification defines more than 500 APIs, and each API specification is written declaratively in TypeScript. Here is an example:

[![](https://substackcdn.com/image/fetch/$s_!UviK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff9195ab0-fda3-4291-89c4-0a55eb8392f5_1652x1320.png)](https://substackcdn.com/image/fetch/$s_!UviK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff9195ab0-fda3-4291-89c4-0a55eb8392f5_1652x1320.png) _Request definition of the [“Create or update a synonym set” API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-synonyms-put-synonym)_

From this specification, we generate a JSON file for all endpoints. This JSON file is then used by each client generator (we have one per language) to produce language-specific SDKs: eight in total.

[![](https://substackcdn.com/image/fetch/$s_!ubXT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa7545f4d-0379-4fd1-9697-e5a1056fd08b_1358x1534.png)](https://substackcdn.com/image/fetch/$s_!ubXT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa7545f4d-0379-4fd1-9697-e5a1056fd08b_1358x1534.png) Generating the Elasticsearch SDKs using a custom generator

There are two big downsides to this approach:

- **A lot of custom code!** We need to write and maintain the compiler from TypeScript to JSON, unlike with an off-the-shelf solution. Plus, we also need to maintain a custom code generator for each language. Back when building this solution, we decided that developing our own tooling was the best way to go. Companies like Stripe and Twilio also follow the custom SDK generator route, likely because suitable open source tools did not exist when they started working on their first SDKs.

- **The declarative TypeScript specification is maintained separately from the product.** The API specification needs to be updated any time a part of the Elasticsearch API changes. _Once we move over to an API-first approach (discussed below), we can discard this step._


### \#3: General-purpose generators: Smithy and TypeSpec

## This post is for paid subscribers

[Subscribe](https://newsletter.pragmaticengineer.com/subscribe?simple=true&next=https%3A%2F%2Fnewsletter.pragmaticengineer.com%2Fp%2Fbuilding-great-sdks&utm_source=paywall&utm_medium=web&utm_content=169288209)

[Already a paid subscriber? **Sign in**](https://substack.com/sign-in?redirect=%2Fp%2Fbuilding-great-sdks&for_pub=pragmaticengineer&change_user=false)

|     |     |
| --- | --- |
| [![](https://substackcdn.com/image/fetch/$s_!BF9y!,w_104,h_104,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6288b4ed-0618-4eb0-84dc-e398297ca9df_1280x1280.jpeg)](https://substack.com/profile/18226609-quentin-pradet) | |     |     |
| --- | --- |
| A guest post by<br>[Quentin Pradet](https://substack.com/@quentinpradet?utm_campaign=guest_post_bio&utm_medium=web) |  | |
