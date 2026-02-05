---
date: '2026-02-05'
description: Introducing Julius, an open-source LLM service fingerprinting tool by
  Praetorian, targets the growing concern of shadow AI by actively probing over 17
  AI platforms, including Ollama and vLLM, for unauthorized access. Its unique probe-and-match
  architecture enables quick identification during assessments, outperforming traditional
  detection methods that rely on manual checks or Shodan queries. Notably, Julius
  excels in specificity scoring to minimize false positives and supports custom probe
  extensions with minimal YAML configuration. Its integration into existing security
  toolchains enhances reconnaissance efficiency in detecting exposed AI services across
  enterprise environments.
link: https://www.praetorian.com/blog/introducing-julius-open-source-llm-service-fingerprinting/
tags:
- Network Security
- Penetration Testing
- LLM fingerprinting
- AI Security
- Open Source Tools
title: 'Introducing Julius: Open Source LLM Service Fingerprinting ◆ Praetorian'
---

[Skip to content](https://www.praetorian.com/blog/introducing-julius-open-source-llm-service-fingerprinting/#content)

- [AI Security](https://www.praetorian.com/category/ai-security/), [Open Source Tools](https://www.praetorian.com/category/open-source-tools/)

# Introducing Julius: Open Source LLM Service Fingerprinting

- [Evan Leleux](https://www.praetorian.com/author/evan-leleux/)
- [January 30, 2026](https://www.praetorian.com/blog/2026/01/30/)

![](<Base64-Image-Removed>)

## The Growing Shadow AI Problem

Over 14,000 Ollama server instances are publicly accessible on the internet right now. A recent [Cisco analysis](https://blogs.cisco.com/security/detecting-exposed-llm-servers-shodan-case-study-on-ollama) found that 20% of these actively host models susceptible to unauthorized access. Separately, [BankInfoSecurity](https://www.bankinfosecurity.com/exposed-llm-servers-expose-ollama-risks-a-29354) reported discovering more than 10,000 Ollama servers with no authentication layer—the result of hurried AI deployments by developers under pressure.

This is the new shadow IT: developers spinning up local LLM servers for productivity, unaware they’ve exposed sensitive infrastructure to the internet. And Ollama is just one of dozens of AI serving platforms proliferating across enterprise networks.

The security question is no longer “are we running AI?” but “where is AI running that we don’t know about?”

## What is LLM Service Fingerprinting?

LLM service fingerprinting identifies what **\*\*server software\*\*** is running on a network endpoint—not which AI model generated text, butwhich infrastructure is serving it.

The LLM security space spans multiple tool categories, each answering a different question:

| Question | Tool Category |
| --- | --- |
| "What ports are open?" | [Nmap](https://github.com/nmap/nmap) |
| "What service is on this port?" | [Praetorian Nerva](https://github.com/praetorian-inc/nerva) (will be open-sourced) |
| "Is this HTTP service an LLM?" | [Praetorian Julius](https://github.com/praetorian-inc/julius) |
| "Which LLM wrote this text?" | [Model fingerprinting](https://arxiv.org/html/2407.15847v3) |
| "Is this prompt malicious?" | [Input guardrails](https://protectai.com/llm-guard) |
| "Can this model be jailbroken?" | [Nvidia Garak](https://github.com/NVIDIA/garak)<br>[Praetorian Augustus](https://github.com/praetorian-inc/augustus) (will be open-sourced) |

Julius answers the third question: during a penetration test or attack surface assessment, you’ve found an open port. Is it Ollama? vLLM? A Hugging Face deployment? Some enterprise AI gateway? Julius tells you in seconds.

Julius follows the Unix philosophy: do one thing and do it well. It doesn’t port scan. It doesn’t vulnerability scan. It identifies LLM services—nothing more, nothing less.

This design enables Julius to slot into existing security toolchains rather than replace them.  The Praetorian Guard Security Pipeline. In [Praetorian’s continuous offensive security platform](https://www.praetorian.com/guard), Julius occupies a critical position in the  multi-stage scanning pipeline:

```
---
config:
  layout: elk
  theme: dark
  themeVariables:
    primaryColor: '#270A0C'
    primaryTextColor: '#ffffff'
    primaryBorderColor: '#535B61'
    lineColor: '#535B61'
    background: '#0D0D0D'
---
flowchart LR
 subgraph subGraph0["Asset Discovery"]
        A["🌱 Seed"]
  end
 subgraph subGraph1["LLM Reconnaissance"]
        B["🔍 Portscan\
Nmap"]
        C["🏷️ Fingerprint\
Nerva"]
        D["🤖 LLM Detection\
Julius"]
  end
 subgraph subGraph2["LLM Attack"]
        E["⚔️ Augustus\
Syntactic Probes\
46+ patterns"]
        F["🧠 Aurelius\
Semantic Reasoning\
AI-driven attacks"]
  end
    A --> B
    B --> C
    C --> D
    D --> E
    E -- Static probes
exhausted --> F
    F -- Adaptive
exploitation --> G["📋 Confirmed Compromise"]
    E --> G

    style C fill:#FFCDD2,stroke:#D50000,color:#000000
    style D fill:#D50000,color:#FFFFFF
    style E fill:#FFCDD2,stroke:#D50000,color:#000000
    style F fill:#FFCDD2,stroke:#D50000,stroke-width:2px,color:#000000
```

## Why Existing Detection Methods Fall Short

### Manual Detection is Slow and Error-Prone

Each LLM platform has different API signatures, default ports, and response patterns:

- Ollama: port 11434, /api/tags returns {“models”: \[…\]}
- vLLM: port 8000, OpenAI-compatible /v1/models
- LiteLLM: port 4000, proxies to multiple backends
- LocalAI: port 8080, /models endpoint

Manually checking each possibility during an assessment wastes time and risks missing services.

### Shodan Queries Have Limitations

[A Cisco’s Study](https://blogs.cisco.com/security/detecting-exposed-llm-servers-shodan-case-study-on-ollama) found ~1,100 Ollama instances were indexed on Shodan. While interesting, replicating the research requires a Shodan license.

| Limitation | Impact |
| --- | --- |
| Ollama-only detection | Misses vLLM, LiteLLM, and 15+ other platforms |
| Passive database queries | Data lags behind real-time deployments |
| Requires Shodan subscription | Cost barrier for some teams |
| No model enumeration | Can't identify what's deployed |

## Introducing Julius

Julius is an open-source LLM service fingerprinting tool that detects 17+ AI platforms through active HTTP probing. Built in Go, it  compiles to a single binary with no external dependencies.

```bash
# Installation
go install github.com/praetorian-inc/julius/cmd/julius@latest

# Basic usage
julius probe https://target.example.com:11434

# Output
```

| TARGET | SERVICE | SPECIFICITY | CATEGORY | MODELS |
| --- | --- | --- | --- | --- |
| https://target.example.com | ollama | 100 | self-hosted | llama2, mistral |

### Julius vs Alternatives

| Capability | Julius | Shodan Queries | Manual Discovery |
| --- | --- | --- | --- |
| Services detected | 17+ | Comprehensive | Unreliable and varied |
| External dependencies | None | Shodan API and License | None |
| Offline operation | Yes | No | Yes |
| Real-time detection | Yes | Delayed (index lag) | Yes |
| Model enumeration | Yes | No | Manual |
| Custom probe extension | Yes (YAML) | No | Not Applicable |
| Time per target | Seconds | Seconds | Minutes, Hours, Days |

## How Julius Works

Julius uses a probe-and-match architecture optimized for speed and accuracy:

```
%%{init: {'theme': 'dark', 'themeVariables': { 'primaryColor': '#270A0C', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#535B61', 'lineColor':
  '#535B61', 'background': '#0D0D0D'}}}%%
  flowchart LR
      A[Target URL] --> B[Load Probes]
      B --> C[HTTP Probes]
      C --> D[Rule Match]
      D --> E[Specificity\
Scoring]
      E --> F[Report\
Service]

      style A fill:#1a1a1a,stroke:#535B61,color:#ffffff
      style B fill:#1a1a1a,stroke:#535B61,color:#ffffff
      style C fill:#1a1a1a,stroke:#535B61,color:#ffffff
      style D fill:#270A0C,stroke:#E63948,color:#ffffff
      style E fill:#E63948,stroke:#535B61,color:#ffffff
      style F fill:#270A0C,stroke:#E63948,color:#ffffff
```

### Architectural Decisions

Julius is designed for performance in large-scale assessments:

| Design Decision | Purpose |
| --- | --- |
| Concurrent scanning with errgroup | Scan 50+ targets in parallel without race conditions |
| Response caching with singleflight | Multiple probes hitting /api/models trigger only one HTTP request |
| Embedded probes compiled into binary | True single-binary distribution—no external files |
| Port-based probe prioritization | Target on :11434 runs Ollama probes first for faster identification |
| MD5 response deduplication | Identical responses across targets are processed once |

```bash
  cmd/julius/          CLI entrypoint
  pkg/
    runner/            Command execution (probe, list, validate)
    scanner/           HTTP client, response caching, model extraction
    rules/             Match rule engine (status, body, header pattern)
    output/            Formatters (table, JSON, JSONL)
    probe/             Probe loader (embedded YAML + filesystem)
    types/             Core data structures
  probes/              YAML probe definitions (one per service)
```

### Detection Process

1. Target Normalization: Validates and normalizes input URLs
2. Probe Selection: Prioritizes probes matching the target’s port (if :11434, Ollama probes run first)
3. HTTP Probing: Sends requests to service-specific endpoints
4. Rule Matching: Compares responses against signature patterns
5. Specificity Scoring: Ranks results 1-100 by most specific match
6. Model Extraction: Optionally retrieves deployed models via JQ expressions

Specificity Scoring: Eliminating False Positives

Many LLM platforms implement OpenAI-compatible APIs. If Julius detects both “OpenAI-compatible” (specificity: 30) and “LiteLLM” (specificity: 85) on the same endpoint, it reports LiteLLM first.

This prevents the generic “OpenAI-compatible” match from obscuring the actual service identity.

### Match Rule Engine

Julius uses six rule types for fingerprinting:

| Rule Type | Purpose | Example |
| --- | --- | --- |
| status | HTTP status code | 200 confirms endpoint exists |
| body.contains | JSON structure detection | "models": identifies list responses |
| body.prefix | Response format identification | {"object": matches OpenAI-style |
| content-type | API vs HTML differentiation | application/json |
| header.contains | Service-specific headers | X-Ollama-Version |
| header.prefix | Server identification | uvicorn ASGI fingerprint |

All rules support negation with not: true—crucial for distinguishing similar services. For example: “has /api/tags endpoint” AND “does NOT contain LiteLLM” ensures Ollama detection doesn’t match LiteLLM proxies.

Julius also caches HTTP responses during a scan, so multiple probes targeting the same endpoint don’t result in duplicate requests. You can write 100 probes that check `/` for different signatures without overloading the target. Julius fetches the page once and evaluates all matching rules against the cached response.

Julius prioritizes precision over breadth. Each probe includes specificity scoring to avoid false positives. An Ollama instance should be identified as Ollama, not just “something OpenAI-compatible.” The generic OpenAI-compatible probe exists as a fallback, but specific service detection always takes precedence.

### Probes Included in Initial Release

#### Self-Hosted LLM Servers

| Services | Port | Detection Method |
| --- | --- | --- |
| [ollama](https://ollama.ai/) | 11434 | api/tags JSON response + "Ollama is running" banner |
| [vllm](https://github.com/vllm-project/vllm) | 8000 | /v1/models with Server: uvicorn header + /version endpoint |
| [local.ai](https://localai.io/) | 8080 | /metrics endpoint containing "LocalAI" markers |
| [llama](https://github.com/ggerganov/llama.cpp) | 8080 | /v1/models with owned\_by: llamacpp OR Server: llama.cpp header |
| [Hugging Face](https://huggingface.co/docs/text-generation-inference) | 3000 | /info endpoint with model\_id field |
| [lm studio](https://lmstudio.ai/) | 1234 | /api/v0/models endpoint (LM Studio-specific) |
| [Nvidia nim](https://developer.nvidia.com/nim) | 8000 | /v1/metadata with modelInfo + /v1/health/ready |

#### Proxy & Gateway Services

| Services | Port | Detection Method |
| --- | --- | --- |
| [LiteLLM](https://github.com/BerriAI/litellm) | 4000 | /health with healthy\_endpoints or litellm\_metadata JSON |
| [Kong](https://konghq.com/) | 8000 | Server: kong header + /status endpoint |

#### Enterprise Cloud Platforms

| Services | Port | Detection Method |
| --- | --- | --- |
| [salesforce einstein](https://www.salesforce.com/einstein/) | 443 | Messaging API auth endpoint error response |

#### ML Demo Platforms

| Services | Port | Detection Method |
| --- | --- | --- |
| [Gradio](https://gradio.app/) | 7860 | /config with mode and components |

#### RAG Platforms

| Services | Port | Detection Method |
| --- | --- | --- |
| [AnythingLLM](https://anythingllm.com/) | 3001 | HTML containing "AnythingLLM" |

#### Chat Frontends

| Services | Port | Detection Method |
| --- | --- | --- |
| [Open WebUI](https://github.com/open-webui/open-webui) | 3000 | /api/config with "name":"Open WebUI" |
| [LibreChat](https://librechat.ai/) | 3080 | HTML containing "LibreChat" |
| [SillyTavern](https://sillytavernai.com/) | 8000 | HTML containing "SillyTavern" |
| [Better ChatGPT](https://github.com/ztjhz/BetterChatGPT) | 3000 | HTML containing "Better ChatGPT" |

#### Generic Detection

| Services | Port | Detection Method |
| --- | --- | --- |
| OpenAI-compatible | Varied | /v1/models with standard response structure |

### Extending Julius with Custom Probes

Adding support for a new LLM service requires ~20 lines of YAML— no code changes:

```yml
# probes/my-service.yaml
name: my-llm-service
description: Custom LLM service detection
category: self-hosted
port_hint: 8080
specificity: 75
api_docs: https://example.com/api-docs

requests:
  - type: http
    path: /health
    method: GET
    match:
      - type: status
        value: 200
      - type: body.contains
        value: '"service":"my-llm"'

  - type: http
    path: /api/version
    method: GET
    match:
      - type: status
        value: 200
      - type: content-type
        value: application/json

models:
  path: /api/models
  method: GET
  extract: ".models[].name"
```

Validate your probe:

```bash
julius validate ./probes
```

## Real World Usage

### Single Target Assessment

```bash
julius probe https://target.example.com

julius probe https://target.example.com:11434

julius probe 192.168.1.100:8080
```

### Scan Multiple Targets From a File

```bash
julius probe -f targets.txt
```

### JSON output for automation:

```bash
Table (default) - human readable
julius probe https://target.example.com

# JSON - structured for parsing
julius probe -o json https://target.example.com

# JSONL - streaming for large scans
julius probe -o jsonl -f targets.txt | jq '.service'
```

## What's Next

Julius is the first tool release of our “The 12 Caesars” open source tool campaign where we will be releasing one open source tool per week for the next 12 weeks. Julius focuses on HTTP-based fingerprinting of known LLM services. We’re already working on expanding its capabilities while maintaining the lightweight, fast execution that makes it practical for large-scale reconnaissance.

On our roadmap: additional probes for cloud-hosted LLM services, smarter detection of custom integrations, and the ability to analyze HTTP traffic patterns to identify LLM usage that doesn’t follow standard API conventions. We’re also exploring how Julius can work alongside AI agents to autonomously discover LLM infrastructure across complex environments.

## Contributing & Community

Julius is available now under the Apache 2.0 license at **[https://github.com/praetorian-inc/julius](https://github.com/praetorian-inc/julius)**

We welcome contributions from the community. Whether you’re adding probes for services we haven’t covered, reporting bugs, or suggesting new features, check the repository’s CONTRIBUTING.md for guidance on probe definitions and development workflow.

Ready to start? Clone the repository, experiment with Julius in your environment, and join the discussion on GitHub. We’re excited to see how the security community uses this tool in real-world reconnaissance workflows. Star the project if you find it useful, and let us know what LLM services you’d like to see supported next.

## About the Authors

![Evan Leleux](<Base64-Image-Removed>)

### [Evan Leleux](https://www.praetorian.com/author/evan-leleux/)

Evan Leleux is a Software Engineer at Praetorian focused on building scalable, distributed systems for enterprise security operations. He loves challenging problems and is always eager to learn. Evan is a Georgia Tech alumni.

## Catch the Latest

Catch our latest exploits, news, articles, and events.

- [Vulnerability Research](https://www.praetorian.com/category/vulnerability-research/)

- [February 4, 2026](https://www.praetorian.com/blog/2026/02/04/)

## [Gone Phishing, Got a Token: When Separate Flaws Combine](https://www.praetorian.com/blog/gone-phishing-got-a-token-when-separate-flaws-combine/)

[Read More](https://www.praetorian.com/blog/gone-phishing-got-a-token-when-separate-flaws-combine/)

- [AI Security](https://www.praetorian.com/category/ai-security/), [Open Source Tools](https://www.praetorian.com/category/open-source-tools/)

- [January 30, 2026](https://www.praetorian.com/blog/2026/01/30/)

## [Introducing Julius: Open Source LLM Service Fingerprinting](https://www.praetorian.com/blog/introducing-julius-open-source-llm-service-fingerprinting/)

[Read More](https://www.praetorian.com/blog/introducing-julius-open-source-llm-service-fingerprinting/)

- [Vulnerability Research](https://www.praetorian.com/category/vulnerability-research/)

- [January 26, 2026](https://www.praetorian.com/blog/2026/01/26/)

## [Corrupting the Hive Mind: Persistence Through Forgotten Windows Internals](https://www.praetorian.com/blog/corrupting-the-hive-mind-persistence-through-forgotten-windows-internals/)

[Read More](https://www.praetorian.com/blog/corrupting-the-hive-mind-persistence-through-forgotten-windows-internals/)

## Ready to Discuss Your Next Continuous Threat Exposure Management Initiative?

Praetorian’s Offense Security Experts are Ready to Answer Your Questions

[Get Started](https://www.praetorian.com/contact-us/)
