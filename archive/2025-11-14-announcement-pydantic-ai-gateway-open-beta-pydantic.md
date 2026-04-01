---
date: '2025-11-14'
description: Pydantic has launched the open beta of the Pydantic AI Gateway (PAIG),
  streamlining LLM governance. PAIG enables direct API access to various LLM providers
  (OpenAI, Anthropic, Google, etc.) with a single key, eliminating inefficiencies
  associated with traditional gateways. Key features include advanced cost controls,
  built-in observability through Pydantic Logfire, automatic failover, and options
  for on-premises deployment. PAIG operates on Cloudflare’s edge network, ensuring
  low latency. The core is open source under AGPL-3.0, with additional enterprise
  features available in a managed service. Feedback is encouraged during the beta
  phase.
link: https://pydantic.dev/articles/gateway-open-beta
tags:
- Open Source
- Cost Management
- Pydantic
- API Gateway
- LLM Governance
title: 'Announcement: Pydantic AI Gateway Open Beta ◆ Pydantic'
---

/PydanticAI

# Announcement: Pydantic AI Gateway Open Beta

![Samuel Colvin avatar](https://pydantic.dev/cdn-cgi/image/width=96,quality=75,format=auto/https://avatars.githubusercontent.com/u/4039449)

Samuel Colvin

7 mins

2025/11/13

If you've built anything serious with LLMs, you've probably seen it:
a tangled mess of API keys, rate limits, and one unexpected Slack message:

> Why did we spend $10,000 last night?

Once you get beyond toy usage, LLM governance is a pain. That's exactly why we built [Pydantic AI Gateway](https://pydantic.dev/ai-gateway) (PAIG),
and today, we're opening the beta to everyone.

Sign up now at [gateway.pydantic.dev](https://gateway.pydantic.dev/). Docs at [ai.pydantic.dev/gateway](https://ai.pydantic.dev/gateway)
The beta is **free** while we gather feedback.

* * *

## [\#](https://pydantic.dev/articles/gateway-open-beta\#why-another-gateway) Why another gateway?

1. We could see it was a pain point for our customers.
2. We knew we could build something with higher engineering quality and better chosen abstractions.
3. We are uniquely positioned to offer a better developer experience via integrations with the existing Pydantic stack (specifically [Pydantic AI](https://ai.pydantic.dev/) and [Logfire](https://logfire.pydantic.dev/)).

Most "AI gateways" are the wrong kind of abstraction.

They try to wrap every provider in a single "universal schema" that slows you down.
Every time a model adds a feature: tool calling, image input, JSON mode - you wait weeks for the gateway to catch up.

PAIG takes a different approach:
**one key, zero translation.**

Your requests go straight through in the provider's native format.
That means when OpenAI, Anthropic, Google, Groq or any other provider ship something new, you can use it immediately. No adapters, no waiting.

Added to that, you get superb observability via the Gateway's (optional) integration with [Pydantic Logfire](https://logfire.pydantic.dev/).

* * *

## [\#](https://pydantic.dev/articles/gateway-open-beta\#whats-included) What's included

- **One key, many models:** talk to [OpenAI](https://platform.openai.com/docs/models), [Anthropic](https://docs.claude.com/en/docs/about-claude/models/overview), [Google Vertex](https://docs.claude.com/en/docs/about-claude/models/overview), [Groq](https://console.groq.com/docs/models), or [AWS Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) with the same key. More
providers (notably [Azure](https://azure.microsoft.com/en-us/products/ai-foundry/models#Models)) are on the way.
- **Cost limits that stop spend:** set daily, weekly, monthly and total caps at project, user, and key levels.
- **Built-in observability:** every request can be logged to [Pydantic Logfire](https://logfire.pydantic.dev/)
or any OpenTelemetry backend.
- **Failover:** route around provider outages automatically.
- **Open source & self-hostable:** [AGPL-3.0 core](https://github.com/pydantic/pydantic-ai-gateway), file-based
config, deploy anywhere. Console and UI are closed source.
- **Enterprise-ready:** SSO via OIDC, granular permissions, and Cloudflare or on-prem deployment options.
- **Low latency:** Finally, and perhaps most importantly, PAIG runs on Cloudflare's globally distributed edge compute [network](https://www.cloudflare.com/network/), meaning absolutely minimal latency. If you're sitting in Berlin making a request to a model near Frankfurt, you'll connect to a PAIG service running in Berlin. After the first request, it won't need to call back to our central database, so using the gateway will add single-digit milliseconds to your response time. It might even be faster, as the request will run through Cloudflare's backbone to the model provider.

This isn't "one schema to rule them all." It's a thin layer that gives you control without hiding power.
If PAIG ever slows you down, we've failed.

* * *

## [\#](https://pydantic.dev/articles/gateway-open-beta\#using-paig-with-pydantic-ai) Using PAIG with Pydantic AI

If you already use [Pydantic AI](https://ai.pydantic.dev/), switching takes one line:

```python
from pydantic_ai import Agent

agent = Agent(
    'gateway/openai:gpt-5',
    instructions='Be concise, reply with one sentence.',
)
print(agent.run_sync('Hello World').output)
```

To switch models, just change the string:

```
gateway/<api_format>:<model_name>
```

For example:

- `gateway/openai:gpt-5`
- `gateway/anthropic:claude-sonnet-4-5`
- `gateway/google-vertex:gemini-2.5-flash`
- `gateway/groq:openai/gpt-oss-120b`

* * *

## [\#](https://pydantic.dev/articles/gateway-open-beta\#using-paig-with-provider-sdks) Using PAIG with provider SDKs

You don't have to use Pydantic AI at all, you can point any supported SDK at PAIG and keep your existing code.

### [\#](https://pydantic.dev/articles/gateway-open-beta\#openai-sdk) OpenAI SDK

```python
import openai

client = openai.Client(
    base_url='https://gateway.pydantic.dev/proxy/openai/',
    api_key='paig_...',
)

response = client.chat.completions.create(
    model='gpt-4o',
    messages=[{'role': 'user', 'content': 'Hello world'}],
)

print(response.choices[0].message.content)
```

### [\#](https://pydantic.dev/articles/gateway-open-beta\#anthropic-sdk) Anthropic SDK

```python
import anthropic

client = anthropic.Anthropic(
    base_url='https://gateway.pydantic.dev/proxy/anthropic/',
    auth_token='paig_...',
)

response = client.messages.create(
    model='claude-3-haiku-20240307',
    max_tokens=1000,
    messages=[{'role': 'user', 'content': 'Hello world'}],
)

print(response.content[0].text)
```

You can even route **Claude Code** through PAIG by setting:

```bash
export ANTHROPIC_AUTH_TOKEN="paig_..."
export ANTHROPIC_BASE_URL="https://gateway.pydantic.dev/proxy/anthropic"
```

Then launch Claude Code as normal — now with real cost limits and logs.

* * *

## [\#](https://pydantic.dev/articles/gateway-open-beta\#our-philosophy) Our philosophy

- **Abstractions should be honest.**
We won't "normalize" APIs into a pretend universal schema. That only hides power and delays progress.
- **Observability is not optional.**
Shared keys without logs are accidents waiting to happen. With PAIG + Logfire (or any inferior OTel-compatible backend), you always know who spent what.
- **Control beats ceremony.**
Budgets should live in your gateway, not in a Notion doc.

We want PAIG to be the boring, reliable layer you don't think about — until you realize how much time and cost it's saved you.

* * *

## [\#](https://pydantic.dev/articles/gateway-open-beta\#frequently-asked-questions) Frequently Asked Questions

1. Why did you build a gateway?
It's a pain point for a lot of our customers, and we think that it integrates nicely with Pydantic AI and Pydantic Logfire (but those are not required to use it).
2. Is it open-source?
The core gateway is open source and available on [GitHub](https://github.com/pydantic/pydantic-ai-gateway). However, some features, like the hosted UI and SSO support are closed source and part of the managed service.
3. How long will the beta last?
Until early December (roughly).
4. How much will it cost after the beta?
Pricing will be announced closer to general availability. During the open beta, the gateway is completely free to use (we’ll eat the card fee for now). We roughly expect to charge competitive markup fee on LLM inference credits if you are using our built-in models, and a base fee for enterprise features (e.g. SSO).
5. What's the difference between this and other gateways?
Similar purpose, pricing and features - just built with higher engineering quality and richer observability via [Pydantic Logfire](https://pydantic.dev/logfire).

* * *

## [\#](https://pydantic.dev/articles/gateway-open-beta\#try-it-today) Try it today

You can:

1. [Create an org](https://gateway.pydantic.dev/) with GitHub or Google login.
2. Add provider credentials (BYOK).
3. Set project, user, and key-level caps.
4. Drop the gateway key into your code.
5. Watch usage and costs in Logfire.

The **open beta starts today — November 13, 2025**.
PAIG is **free** during beta while we gather feedback.
Go to [gateway.pydantic.dev](https://gateway.pydantic.dev/) and tell us what works, and what sucks.

* * *

_PAIG is built with the same philosophy as the Pydantic stack: developer-first, transparent and fast._
_If that sounds like your kind of infrastructure, we think you'll love it._

## Related content

[View all articles](https://pydantic.dev/articles)

[/Open Source\\
\\
**Pydantic Open Source Fund**\\
\\
![Samuel Colvin](https://pydantic.dev/cdn-cgi/image/width=64,quality=75,format=auto/https://avatars.githubusercontent.com/u/4039449)\\
\\
Samuel Colvin\\
\\
2025/10/07](https://pydantic.dev/articles/pydantic-oss-fund-2025) [/Company\\
\\
**Introducing Pydantic’s New Brand Identity**\\
\\
![Laura Summers](https://pydantic.dev/cdn-cgi/image/width=64,quality=75,format=auto/https://avatars.githubusercontent.com/u/6570564)\\
\\
Laura Summers\\
\\
2025/08/29](https://pydantic.dev/articles/pydantic-rebranding)

### Explore Logfire

[Get started\\
\\
Get started](https://pydantic.dev/contact)

[Explore ouropen sourcepackages\\
![Product shot](https://pydantic.dev/cdn-cgi/image/width=750,quality=75,format=auto/https://pydantic.dev/assets/footer/cta.svg)](https://github.com/pydantic)
