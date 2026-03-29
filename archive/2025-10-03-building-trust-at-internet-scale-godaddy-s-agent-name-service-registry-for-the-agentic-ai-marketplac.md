---
date: '2025-10-03'
description: GoDaddy introduces an enhanced Agent Name Service (ANS) Registry aimed
  at establishing trust and identity verification for AI agents in a rapidly developing
  market. Utilizing IETF and OWASP standards, the system enables secure agent discovery
  via DNS and cryptographic trust through public key infrastructure (PKI). The architecture
  features a Registration Authority (RA) for agent lifecycle management and immutable
  transparency logging, preventing impersonation and ensuring tamper-proof identity.
  This infrastructure facilitates a marketplace for AI capabilities, enhancing operational
  scalability and security for future multi-agent interactions. Insights suggest that
  integration with existing frameworks may drive broader adoption across AI systems.
link: https://www.godaddy.com/resources/news/building-trust-at-internet-scale-godaddys-agent-name-service-registry-for-the-agentic-ai-marketplace
tags:
- AI agents
- Agent Name Service
- cryptographic security
- identity verification
- trust infrastructure
title: 'Building Trust at Internet Scale: GoDaddy''s Agent Name Service Registry for
  the Agentic AI Marketplace - GoDaddy Blog'
---

[Skip to main content](https://www.godaddy.com/resources/news/building-trust-at-internet-scale-godaddys-agent-name-service-registry-for-the-agentic-ai-marketplace#root)

Popular Search Terms

website builder

* * *

whois

* * *

email

* * *

domain

* * *

payments

Quick Links

- [Domain Search](https://www.godaddy.com/domains)
- [Help Center](https://www.godaddy.com/help)
- [Plans & Pricing](https://www.godaddy.com/pricing)
- [Account Sign-In](https://sso.godaddy.com/?realm=idp&app=dashboard.api&path=%2fvh-login-redirect&marketid=en-US)
- [Hire an Expert](https://www.godaddy.com/hire-an-expert)

[Deals](https://www.godaddy.com/great-deals)Help

- [Getting Started](https://godaddy.com/help/get-started-with-godaddy-products-1000077)
- [Contact Us](https://www.godaddy.com/help/contact-us)

[Help Center](https://godaddy.com/help)

Sign In

Registered Users

Have an account? Sign in now.

[Sign In](https://sso.godaddy.com/?realm=idp&app=venture-redirector&path=%2F)

New Customer

New to GoDaddy? Create an account to get started today.

[Create an Account](https://sso.godaddy.com/account/create?realm=idp&app=venture-redirector&path=%2F)

INBOX LINKS

- [Sign in to Office 365 Email](https://sso.godaddy.com/?app=o365&realm=pass&marketid=en-US)
- [Sign in to GoDaddy Webmail](https://email.godaddy.com/?target=blank)

![graphical user interface](https://www.godaddy.com/resources/wp-content/uploads/2025/10/cover-1.png?size=3840x0)

- Copy link
- Share "Building Trust at Internet Scale: GoDaddy’s Agent Name Service Registry for the Agentic AI Marketplace" on Facebook
- Share "Building Trust at Internet Scale: GoDaddy’s Agent Name Service Registry for the Agentic AI Marketplace" on X
- Share "Building Trust at Internet Scale: GoDaddy’s Agent Name Service Registry for the Agentic AI Marketplace" on LinkedIn
- Share "Building Trust at Internet Scale: GoDaddy’s Agent Name Service Registry for the Agentic AI Marketplace" on Pinterest

As AI agents proliferate across the internet, a critical question emerges: how do agents discover and trust each other at scale? At GoDaddy, we're addressing this challenge by developing an enhanced Agent Name Service (ANS) Registry with a Registration Authority (RA) that builds on emerging IETF, OWASP, and agent communication protocol standards while adding the operational automation and cryptographic rigidity needed for real-world deployment. In this blog post, we provide a proof-of-concept demonstrating how to create a verifiable trust chain from customers and their agents through the DNS, certificate authorities (CAs), and transparency logs.

## The challenge of agent identity and discovery

Picture this: You've built an AI agent that analyzes customer sentiment in real-time. And it detects a customer complaint written in Spanish! But to resolve that complaint, your agent needs to collaborate ... and it immediately runs into a series of roadblocks:

First, it needs to translate the complaint. It searches for an agent with a translation capability, and finds multiple options. Which one is trustworthy? Which one is cost-effective? There's no "phone book" to check.

After guessing at a translation agent, it needs to route the complaint. It looks for a customer-service-triage agent for the user's account. It finds one, but how can it be sure it's the legitimate agent and not a malicious imposter trying to intercept customer data? There's no way to verify its identity.

Finally, the triage agent decides to issue a small refund and needs to call a billing agent. How can it securely authorize a payment transaction? Without a trusted identity infrastructure, it's too risky.

The task fails. Your agent is an island. The current landscape resembles the early web: functional protocols exist, but with no trusted directory, no identity verification, and no secure way to transact, scalable collaboration is impossible.

The AI ecosystem is experiencing explosive, if nascent, growth. Industry analysts project billions of agents operating by 2030, yet fundamental infrastructure challenges remain unsolved across the internet:

- **Discovery**: How does an agent find other agents with specific capabilities?
- **Identity**: How can agents verify they're communicating with legitimate entities?
- **Immutability**: How do we ensure agent identity is tamper-proof and traceable over time?

Emerging standards address pieces of this puzzle; however, they lack the operational automation and trust mechanisms needed for sustained internet-scale deployment.

## GoDaddy's enhanced ANS Registry: bridging concept to reality

Our enhanced ANS Registry introduces a registration authority as the central orchestrator. In leveraging GoDaddy's existing infrastructure, we've created a system that makes agent registration as straightforward as domain registration, with absolute identity integrity as the core principle.

### `ANSName` immutability

In our enhanced design, the full `ANSName` is treated as a primary key. Any change to any of its components, even a minor version increment, forces the creation of a new, unique, `ANSName`. The identity certificate for the former name is immediately revoked, and a new entry is sealed in the transparency log, creating a permanent, auditable record of the version change.

The structured ANS Name format is composed of six distinct parts: `Protocol://AgentID.Capability.Provider.vX.Y.Z.Extension`

This builds from the [IETF narajala-draft document](https://datatracker.ietf.org/doc/draft-narajala-ans/). Our format strictly defines the agent's communication protocol, its unique hostname ( `AgentID`), its primary function ( `Capability`), its verified owner ( `ProviderID`), its software version, and the DNS domain zone ( `Extension`) that acts as its trust anchor. Any change to these components requires a new registration.

## The architecture: familiar patterns, new purpose

The breakthrough came when we realized we didn't need to reinvent the internet's infrastructure; we simply needed to extend it. The internet already has two massive, battle-tested hierarchies that handle identity and discovery at a global scale: the Domain Name System for organizing resources hierarchically and the CA system for establishing cryptographic trust.

We asked: what if agent identity could work just like web server identity? Instead of creating new protocols from scratch, we could build agent discovery on DNS, the same system that currently handles more than one hundred million requests each second, and we could establish trust through the same PKI infrastructure that secures every HTTPS connection. The enhanced ANS/RA architecture deliberately integrates with these proven systems: DNS provides scalable, hierarchical discovery while CAs establish cryptographic trust.

The following diagram illustrates complete ANS registration flow showing the new orchestration role provided by the RA:

![diagram](https://www.godaddy.com/resources/wp-content/uploads/2025/10/registration-flow-1.png?size=3840x0)

### The trust chain: cryptography at every link

Our implementation creates a comprehensive trust chain that is verifiable at each step:

1. **Customer verification**: Know-your-customer processes validate the agent provider's identity.
2. **Domain validation**: ACME DNS-01 challenges prove domain ownership.
3. **Hybrid certificates**: Public CA issues standard TLS certificates; private CA issues identity certificates with custom ANS extensions.
4. **DNS provisioning**: DNSSEC validation ensures the entire trust chain for the agent's domain is cryptographically secured against hijacking.
5. **Transparency logging**: Merkle tree-based attestation provides an immutable audit trail, sealing the identity and attestation results.

Each link uses established cryptographic standards, creating defense in depth against impersonation and tampering. The following diagram illustrates the evolution from basic validation to comprehensive cryptographic trust chain:

![diagram of trust chain](https://www.godaddy.com/resources/wp-content/uploads/2025/10/trust-chain-1.png?size=3840x0)

## Agent registration in practice

Imagine you've built a sentiment analysis service and want other AI agents to discover and use it. Here's how our ANS Registry transforms this from a manual, error-prone process into something as simple as registering a domain using the ANS format and lifecycle rules.

### Step 1: Submission

An agent provider submits their registration with an ANS name following our structured format:

`mcp://sentimentAnalyzer.textAnalysis.AcmeCorp.v1.0.example.com`

This strictly encodes the protocol ( `MCP`), AgentID ( `sentimentAnalyzer`), capability ( `textAnalysis`), provider ( `AcmeCorp`), version ( `v1.0.0`), and extension ( `example.com`).

## Step 2: Validation and certificate issuance

The RA validates the provider's identity and domain control. It then orchestrates the issuance of two certificates as defined in our hybrid model: a public server certificate for the agent's endpoint (this is the standard TLS certificate used to secure its public HTTPS traffic), and a private identity certificate that cryptographically binds the agent's key to its full, immutable `ANSName`, which is used for secure agent-to-agent signing.

## Step 3: DNS provisioning

The system provisions multiple DNS record types for comprehensive discovery:

```hljs kotlin
; Points to the Agent Card, a metadata file hosted by the agent provider
_ans.sentiment       IN TXT "url=https://sentiment.example.com/agent-card.json"

; Service endpoint
_mcp._tcp.sentiment   IN HTTPS 1 . alpn=h2 port=443

; Certificate pinning for additional security
_443._tcp.sentiment   IN TLSA 3 1 1 [cert_hash]

; RA attestation badge dynamically hosted at the RA
_ra-badge.sentiment   IN TXT "v=ra-badge1; url=https://transparency.example.com/reg-abc123"
```

### Step 4: Transparency and attestation

Every successful registration or status change creates a new, immutable log entry. This record explicitly includes the cryptographic fingerprints and the hash of the agent's configuration.

```hljs json
{
  "log_id": "reg-abc123",
  "ans_name": "mcp://sentimentAnalyzer.textAnalysis.PID-1234.v1.0.0.example.com",
  "timestamp": "2025-01-24T10:00:00Z",
  "status": "VERIFIED",
  "validation_summary": {
    "domainControl": "success",
    "organizationIdentity": "success",
    "dnssec": "success"
  }
}
```

The following image depicts the RA Attestation Badge, which visualizes the cryptographic proof and validation checks from the transparency log:

![Attestation badge](https://www.godaddy.com/resources/wp-content/uploads/2025/10/attestation-badge-1.png?size=3840x0)

## Lessons from the POC

Our proof-of-concept implementation demonstrates several key architectural decisions that any organization building similar infrastructure would need to consider:

- **Domain-driven design for complex business logic** \- We structured our code using domain-driven design principles to manage the system's complexity, ensuring a clear separation between business rules and technical infrastructure.
- Functional **error handling** \- Our implementation uses functional programming concepts to handle errors gracefully and predictably, avoiding unexpected exceptions and making the system more robust.
- **Idempotent operations at scale**\- Every core operation is designed to be idempotent, meaning API requests can be safely retried without creating duplicate registrations or causing unintended side effects.

## Enabling the agentic marketplace

The following diagram illustrates the circular economy of AI agents enabled by the ANS Registry:

![Illustration of the market ecosystem](https://www.godaddy.com/resources/wp-content/uploads/2025/10/market-ecosystem-1.png?size=3840x0)

Beyond technical infrastructure, our ANS Registry enables new economic models for AI agents:

### Discovery markets

Agents can advertise their capabilities through the registry, and independent discovery services subscribe to the registry's public pub/sub feed to build their own searchable indexes. For example, an LLM-powered discovery chatbot constantly indexes this feed. A user or agent can then find other agents through a simple, natural language conversation:

> User: Find me an agent with sentiment analysis capabilities.
>
> Discovery Bot: I found two registered agents. Agent A offers pay-per-request, and Agent B offers a monthly subscription. Here are their details:

```hljs json
[\
  {\
    "ansName": "mcp://sentiment.analytics.PID-1234.v2.0.0.provider1.com",\
    "endpoint": "https://sentiment.provider1.com",\
    "pricing": "0.001 USD per request"\
  },\
  {\
    "ansName": "a2a://emotions.analysis.PID-5678.v1.5.0.provider2.com",\
    "endpoint": "https://emotions.provider2.com",\
    "pricing": "subscription: 100 USD/month"\
  }\
]
```

### Monetization through cryptographic attribution

The system enables secure, attributable billing for agent services. By using its private Identity Certificate to cryptographically sign requests, an agent can prove its identity to another agent. This allows the receiving agent to confidently bill for services, for example by responding with a standard HTTP 402 (Payment Required) status to initiate a transaction.

### Platform opportunities

While any of these can be offered by independent providers in the market, GoDaddy is creating each of the service streams:

1. **Agent hosting**: Managed infrastructure for agent deployment.
2. **Registration services**: ANS registration analogous to domain registration.
3. **Certificate management**: Automated renewal and lifecycle management.
4. **Discovery marketplace**: Commission-based agent marketplace.
5. **Analytics and monitoring**: Insights into agent interactions and performance.

## Defense in depth

Our implementation addresses the following threat vectors:

- **Domain hijacking prevention** \- ACME DNS-01 validation ensures only legitimate domain owners can register agents. This prevents a malicious actor from registering an agent for a domain they do not actually control, thwarting impersonation at the domain level. We already use it in several parts of our business.
- **Certificate pinning via DANE** \- TLSA records in DNS provide out-of-band certificate verification. This allows a client to verify an agent's certificate directly against DNS, even in the unlikely event of a CA compromise.
- **Transparency for accountability** \- Every action is logged with cryptographic proof. This creates a public, tamper-evident audit trail, allowing any third party to independently verify an agent's registration history and confirm that the log has not been secretly altered.

### Differences from emerging standards

Our implementation makes deliberate choices that differ from nascent standards. The following table illustrates the key differences and our rationale for each divergence:

| Standard | Changes Made | Rationale |
| --- | --- | --- |
| **IETF ANS draft** | **Added**: RA orchestration, automated lifecycle management, transparency logs | The RA's role is precisely to add the operationalization that moves the IETF standard from a naming convention draft into a deployable, auditable system |
| **OWASP GenAI ANS** | **Added**: Hybrid certificates, Domain Connect integration | Our system emphasizes public TLS + private identity and automated DNS provisioning as core differentiators enabling robust trust models |
| **A2A/MCP protocols** | **Added**: DNS-based discovery layer | These protocols focus on agent-to-agent communication after discovery. Our ANS/RA provides the DNS-based discovery layer that acts as the missing foundational infrastructure |
| **Blockchain approaches** | **Different**: Uses DNS instead of blockchain | The explicit choice to use DNS, PKI, and Merkle Logs over a fully distributed blockchain ledger is an architectural distinction to leverage existing, scalable internet infrastructure |

## Infrastructure for the agentic future

The enhanced ANS Registry with RA represents more than a technical implementation. It is foundational infrastructure for the emerging agentic economy. By building on proven internet standards while adding necessary automation and trust mechanisms, we're creating the conditions for AI agents to discover, verify, and transact with each other at internet scale.

Just as GoDaddy has been instrumental in making domain registration accessible to our 20 million customers, we're now working to make agent registration equally straightforward. The trust chain we've built ensures that the agentic marketplace can grow securely and reliably by integrating:

1. Customer Verification
2. Domain Validation
3. Hybrid Certificate Issuance
4. DNSSEC-signed DNS Provisioning
5. Immutable Transparency Logging

As we move toward a future where billions of agents coordinate to solve complex problems, the infrastructure we build today will determine whether that future is secure, scalable, and accessible to all. At GoDaddy, we're committed to making that vision a reality.

We're actively seeking feedback from the developer community. If you're building AI agents or multi-agent systems, we'd love to hear about your challenges and use cases. We're also launching a developer preview in the coming weeks. If you have feedback or are interested in the being a part of the developer preview, contact us at [GDANS@godaddy.com](mailto:GDANS@godaddy.com).

## More articles like this

[![](https://www.godaddy.com/resources//_next/static/media/godaddy-article-default.desktop.d615e0d9.png)](https://www.godaddy.com/resources/skills/5-tried-and-true-tips-for-buying-and-selling-domain-names-for-profit)

[Domains](https://www.godaddy.com/resources/category/domains)

Sep 22, 2025

[7 expert tips for buying and selling domain names for profit](https://www.godaddy.com/resources/skills/5-tried-and-true-tips-for-buying-and-selling-domain-names-for-profit) Learn more

[![](https://www.godaddy.com/resources//_next/static/media/godaddy-article-default.desktop.d615e0d9.png)](https://www.godaddy.com/resources/skills/what-is-a-domain-name)

[Domains](https://www.godaddy.com/resources/category/domains)

Aug 25, 2025

[What is a domain name? Domains vs URLs — Your ultimate guide](https://www.godaddy.com/resources/skills/what-is-a-domain-name) Learn more

[![](https://www.godaddy.com/resources//_next/static/media/godaddy-article-default.desktop.d615e0d9.png)](https://www.godaddy.com/resources/skills/company-naming-seo-strategies)

[Business](https://www.godaddy.com/resources/category/business)

Aug 20, 2025

[Strategies for how to select an SEO-friendly business name](https://www.godaddy.com/resources/skills/company-naming-seo-strategies) Learn more

[![](https://www.godaddy.com/resources//_next/static/media/godaddy-article-default.desktop.d615e0d9.png)](https://www.godaddy.com/resources/skills/move-llc-to-another-state)

[Business](https://www.godaddy.com/resources/category/business)

Aug 17, 2025

[How to transfer an LLC to another state](https://www.godaddy.com/resources/skills/move-llc-to-another-state) Learn more

[![](https://www.godaddy.com/resources//_next/static/media/godaddy-article-default.desktop.d615e0d9.png)](https://www.godaddy.com/resources/skills/how-to-start-an-llc-in-pennsylvania)

[Business](https://www.godaddy.com/resources/category/business)

Aug 5, 2025

[How to start an LLC in Pennsylvania in 2025](https://www.godaddy.com/resources/skills/how-to-start-an-llc-in-pennsylvania) Learn more

## Related Articles

[![](https://www.godaddy.com/resources/wp-content/uploads/2019/09/buying-and-selling-domains-for-profit-featured-nHLvAa.tmp_.jpeg?size=3840x0)](https://www.godaddy.com/resources/skills/5-tried-and-true-tips-for-buying-and-selling-domain-names-for-profit)

[Domains](https://www.godaddy.com/resources/category/domains)

September 22, 2025

[7 expert tips for buying and selling domain names for profit](https://www.godaddy.com/resources/skills/5-tried-and-true-tips-for-buying-and-selling-domain-names-for-profit) [Learn more](https://www.godaddy.com/resources/skills/5-tried-and-true-tips-for-buying-and-selling-domain-names-for-profit)

[![](https://www.godaddy.com/resources/wp-content/uploads/2023/03/what-is-a-domain-name-featured-min.png?size=3840x0)](https://www.godaddy.com/resources/skills/what-is-a-domain-name)

[Domains](https://www.godaddy.com/resources/category/domains)

Aug 25, 2025

[What is a domain name? Domains vs URLs — Your ultimate guide](https://www.godaddy.com/resources/skills/what-is-a-domain-name) Learn more

[![Illustration of a person standing thoughtfully outdoors with a large orange speech bubble containing a question mark above their head, representing curiosity or decision-making. The image symbolizes the process of brainstorming or choosing SEO company names, with the individual contemplating different options and ideas.](https://www.godaddy.com/resources/wp-content/uploads/2025/08/seo-company-names-featured-vvyfoC.tmp_.jpeg?size=3840x0)](https://www.godaddy.com/resources/skills/company-naming-seo-strategies)

[Business](https://www.godaddy.com/resources/category/business)

Aug 20, 2025

[Strategies for how to select an SEO-friendly business name](https://www.godaddy.com/resources/skills/company-naming-seo-strategies) Learn more

[![Map of the United States with three large, colorful arrows showing movement between different states, illustrating the concept of how to transfer an LLC to another state](https://www.godaddy.com/resources/wp-content/uploads/2025/08/how-to-transfer-an-llc-featured-D6jNZ3.tmp_.jpeg?size=3840x0)](https://www.godaddy.com/resources/skills/move-llc-to-another-state)

[Business](https://www.godaddy.com/resources/category/business)

Aug 17, 2025

[How to transfer an LLC to another state](https://www.godaddy.com/resources/skills/move-llc-to-another-state) Learn more

[![a sign in front of a building - The Pennsylvania State Capitol](https://www.godaddy.com/resources/wp-content/uploads/2025/08/llc-in-pa-featured-IRWGcg.tmp_.jpeg?size=3840x0)](https://www.godaddy.com/resources/skills/how-to-start-an-llc-in-pennsylvania)

[Business](https://www.godaddy.com/resources/category/business)

Aug 5, 2025

[How to start an LLC in Pennsylvania in 2025](https://www.godaddy.com/resources/skills/how-to-start-an-llc-in-pennsylvania) Learn more

[Skip to main content](https://www.godaddy.com/resources/news/building-trust-at-internet-scale-godaddys-agent-name-service-registry-for-the-agentic-ai-marketplace#root)

[GoDaddy Home Page](https://www.godaddy.com/)

* * *

United States - English

Choose your Country/Region

- [**Argentina** \- Español](https://www.godaddy.com/es)
- [**Australia** \- English](https://www.godaddy.com/en-au)
- [**België** \- Nederlands](https://www.godaddy.com/nl)
- [**Belgique** \- Français](https://www.godaddy.com/fr)
- [**Brasil** \- Português](https://www.godaddy.com/pt-br)
- [**Canada** \- English](https://www.godaddy.com/en-ca)
- [**Canada** \- Français](https://www.godaddy.com/fr-ca)
- [**Chile** \- Español](https://www.godaddy.com/es)
- [**Colombia** \- Español](https://www.godaddy.com/es)
- [**Danmark** \- Dansk](https://dk.godaddy.com/)
- [**Deutschland** \- Deutsch](https://www.godaddy.com/de)
- [**España** \- Español](https://www.godaddy.com/es-es)
- [**Estados Unidos** \- Español](https://www.godaddy.com/es)
- [**France** \- Français](https://www.godaddy.com/fr)
- [**Hong Kong** \- English](https://www.godaddy.com/en)
- [**India** \- English](https://www.godaddy.com/en-in)
- [**India** \- हिंदी](https://www.godaddy.com/hi-in)
- [**Indonesia** \- Bahasa Indonesia](https://www.godaddy.com/id-id)
- [**Ireland** \- English](https://www.godaddy.com/en)
- [**Israel** \- English](https://www.godaddy.com/en)
- [**Italia** \- Italiano](https://www.godaddy.com/it)
- [**Malaysia** \- English](https://www.godaddy.com/en-ph)
- [**México** \- Español](https://www.godaddy.com/es)
- [**Nederland** \- Nederlands](https://www.godaddy.com/nl)
- [**New Zealand** \- English](https://www.godaddy.com/en)
- [**Norge** \- Bokmål](https://no.godaddy.com/)
- [**Österreich** \- Deutsch](https://www.godaddy.com/de)
- [**Pakistan** \- English](https://www.godaddy.com/en-ph)
- [**Perú** \- Español](https://www.godaddy.com/es)
- [**Philippines** \- English](https://www.godaddy.com/en-ph)
- [**Polska** \- Polski](https://www.godaddy.com/pl-pl)
- [**Portugal** \- Português](https://www.godaddy.com/pt-pt)
- [**Schweiz** \- Deutsch](https://www.godaddy.com/de)
- [**Singapore** \- English](https://www.godaddy.com/en)
- [**South Africa** \- English](https://www.godaddy.com/en-ph)
- [**Suisse** \- Français](https://www.godaddy.com/fr)
- [**Sverige** \- Svenska](https://se.godaddy.com/)
- [**Svizzera** \- Italiano](https://www.godaddy.com/it)
- [**Türkiye** \- Türkçe](https://www.godaddy.com/tr-tr)
- [**United Arab Emirates** \- English](https://www.godaddy.com/en)
- [**United Kingdom** \- English](https://www.godaddy.com/en-uk)
- [**United States** \- English](https://www.godaddy.com/)
- [**Việt Nam** \- Tiếng Việt](https://www.godaddy.com/vi-vn)
- [**Україна** \- Українська](https://www.godaddy.com/uk-ua)
- [**الإمارات العربية المتحدة** \- اللغة العربية](https://ae.godaddy.com/ar)
- [**ไทย** \- ไทย](https://www.godaddy.com/th-th)
- [**대한민국** \- 한국어](https://kr.godaddy.com/)
- [**台灣** \- 繁體中文](https://www.godaddy.com/zh)
- [**新加坡** \- 简体中文](https://www.godaddy.com/zh-sg)
- [**日本** \- 日本語](https://jp.godaddy.com/)
- [**香港** \- 繁體中文](https://www.godaddy.com/zh)

USD $

USD $

AED AEDAUD $CAD C$CHF CHFCLP $CNY ¥COP $DKK krEUR €GBP £HKD HK$IDR RpILS ₪INR ₹JPY ¥KRW ₩MXN MXNMYR RMNZD $PEN S/PHP ₱PKR ₨PLN złSAR SARSEK krSGD SG$THB ฿TWD NT$UAH ₴VND ₫ZAR R

- [GoDaddy on Facebook](https://www.facebook.com/godaddy)
- [GoDaddy on Instagram](https://www.instagram.com/godaddy)
- [GoDaddy on TikTok](https://www.tiktok.com/@godaddy?lang=en)
- [GoDaddy on Twitter](https://www.twitter.com/godaddy)
- [GoDaddy on Youtube](https://www.youtube.com/channel/UCgH_SmWw9WianYyOB5Y6tEA)

[Do not sell my personal information](https://www.godaddy.com/legal/agreements/cookie-policy)

Copyright © 1999 - 2025 GoDaddy Operating Company, LLC. All Rights Reserved. The GoDaddy word mark is a registered trademark of GoDaddy Operating Company, LLC in the US and other countries. The “GO” logo is a registered trademark of GoDaddy.com, LLC in the US.

Use of this Site is subject to express terms of use. By using this site, you signify that you agree to be bound by these [Universal Terms of Service](https://www.godaddy.com/legal/agreements/universal-terms-of-service-agreement).
