---
date: '2026-05-02'
description: Harvey's platform focuses on securing sensitive legal data while leveraging
  AI. The embedding reversal threat, wherein an attacker reconstructs original data
  from embeddings, is central to their security model. Harvey employs strict database
  isolation, short retention policies, and strong access controls to mitigate risks.
  They emphasize a secure-by-design architecture that adapts to evolving security
  threats, ensuring embeddings are handled with the same caution as raw data. This
  approach positions Harvey as a robust solution for legal professionals who require
  both advanced AI capabilities and stringent data protection, addressing increasing
  cybersecurity concerns in the legal sector.
link: https://www.harvey.ai/blog/how-harvey-secures-embeddings-at-scale
tags:
- AI Security
- Data Privacy
- Legal Technology
- Embedding Reversal
- Vector Database
title: How Harvey Secures Embeddings at Scale ◆ Harvey
---

Platform

  - [Overview\\
    \\
    A unified view of how Harvey's products work together to support your entire practice.](https://www.harvey.ai/platform)
  - [Assistant\\
    \\
    Ask questions, analyze documents, and draft faster with domain-specific AI.](https://www.harvey.ai/platform/assistant)
  - [Vault\\
    \\
    Securely store, organize, and bulk-analyze legal documents.](https://www.harvey.ai/platform/vault)
  - [Knowledge\\
    \\
    Research complex legal, regulatory, and tax questions across domains.](https://www.harvey.ai/platform/knowledge)
  - [Workflow Agents\\
    \\
    Run pre-built Workflow agents or build your own, tailored to your firm's needs.](https://www.harvey.ai/platform/workflow-agents)
  - [Harvey Mobile\\
    \\
    Get up to speed, capture new information, and keep work moving from anywhere.](https://www.harvey.ai/platform/harvey-mobile)
  - [Ecosystem\\
    \\
    Access Harvey where you already work and ground every answer in sources you trust.](https://www.harvey.ai/platform/ecosystem)
  - [![Harvey Agents](https://www.harvey.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F07s0r5r6%2Fproduction%2Fd3dcef152521107b64a52cf8dcd6dbe2e8481d92-2400x1260.png%3Fauto%3Dformat&w=3840&q=80)**Harvey Agents** \\
    Harvey Agents execute legal work end-to-end, so you can focus on what only lawyers can do.](https://harvey.ai/agents)

Solutions

  - [Innovation\\
    \\
    Scale expertise and impact to drive firmwide transformation.](https://www.harvey.ai/solutions/innovation)
  - [In-House\\
    \\
    Streamline work and shift focus to strategy and speed.](https://www.harvey.ai/solutions/in-house)
  - [Transactional\\
    \\
    Accelerate due diligence, contract analysis, and review with precision and control.](https://www.harvey.ai/solutions/transactional)
  - [Litigation\\
    \\
    Reduce manual effort, prioritize strategy, and drive stronger outcomes in litigation.](https://www.harvey.ai/solutions/litigation)
  - [Mid-Sized Firms\\
    \\
    Drive outsize impact with tools built for lean teams.](https://www.harvey.ai/solutions/mid-sized-firms)
  - [Collaboration\\
    \\
    Work with legal teams across organizations in secure, shared spaces.](https://www.harvey.ai/solutions/collaboration)
  - [![A New Era of Collaboration for Legal and Professional Services](https://cdn.sanity.io/images/07s0r5r6/production/6d697d9a97bf529af75a9380d4de4b99e101c77e-2740x1542.svg)**A New Era of Collaboration for Legal and Professional Services** \\
    Law firms and professional service networks have been using Harvey to build new service models and add value collaboratively.](https://www.harvey.ai/blog/a-new-era-of-collaboration-for-legal-and-professional-services)

- [Customers](https://www.harvey.ai/customers)
- [Security](https://www.harvey.ai/security)

Resources

  - [Blog\\
    \\
    Product updates, insights, and behind-the-scenes from the Harvey team.](https://www.harvey.ai/blog)
  - [Resources Hub\\
    \\
    The latest videos, webinars, guides, and reports from Harvey.](https://www.harvey.ai/resources)
  - [Press Kit\\
    \\
    Resources for maintaining a uniform and professional presentation of the Harvey brand.](https://www.harvey.ai/press)
  - [ROI Calculator Law Firm\\
    \\
    See Harvey's Impact on Your Firm.](https://www.harvey.ai/roi-calculator/law-firm)
  - [ROI Calculator In House\\
    \\
    See Harvey's Impact on Your Business.](https://www.harvey.ai/roi-calculator/in-house)
  - [![Harvey Academy](https://www.harvey.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F07s0r5r6%2Fproduction%2Fda591a03f44c5e7ba5f094e088c681f76cb17f20-2400x1260.png%3Fauto%3Dformat&w=3840&q=80)**Harvey Academy** \\
    Introducing Harvey Academy: on-demand training, expert workflows, and step-by-step guidance to help legal teams get the most out of Harvey.](https://academy.harvey.ai/)

About

  - [Company\\
    \\
    About Harvey, our leadership, and career opportunities.](https://www.harvey.ai/company)
  - [Newsroom\\
    \\
    Press releases and partnership announcements.](https://www.harvey.ai/newsroom)
  - [![2025 Year in Review](https://www.harvey.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F07s0r5r6%2Fproduction%2F8f29fcfce7a2b69616005ef38dd6edaa20613c6e-5760x3240.png%3Fauto%3Dformat&w=3840&q=80)**2025 Year in Review** \\
    In 2025, we celebrated major customer wins, introduced product breakthroughs, and expanded our global presence. Most importantly, we continued to deepen our commitment to building the best AI solutions for our customers.](https://www.harvey.ai/year-in-review/2025)

[Request a Demo](https://www.harvey.ai/contact-sales)

Login

[US](https://app.harvey.ai/)
[EU](https://eu.app.harvey.ai/)
[AU](https://au.app.harvey.ai/)

Technical

# How :Harvey: Secures Embeddings at Scale

Protecting sensitive data from embedding reversal through secure-by-design architecture.

by[Suha Sabi Hussain](https://www.harvey.ai/blog/author/suha-sabi-hussain)•Apr 30, 2026

Helping legal and professional service teams leverage AI effectively and securely means that we deal with some of the most sensitive data in the world. Much of this sensitive data powers our enterprise-grade RAG systems.

Previously, we discussed how we build these systems at scale by [choosing a vector database that prioritizes security, performance, and reliability](https://www.harvey.ai/blog/enterprise-grade-rag-systems) and [establishing strong management of customer data](https://www.harvey.ai/blog/how-harvey-manages-customer-data). Embeddings are the foundation of our enterprise-grade RAG systems, but they come with an emerging security threat: embedding reversal.

At Harvey, we're building a platform that is secure by design and stays secure as our product and the industry evolve. In this post, we describe how we’ve applied that approach to embedding reversal: what recent research has shown is possible, why it matters for the sensitive work our customers bring to us, and the architectural controls we've designed as a result.

## Why Embeddings?

To understand why we care about embedding reversal, it’s important to understand the role embeddings play at Harvey. When a user uploads a file to [Assistant](https://www.harvey.ai/platform/assistant), adds a document to a [Vault](https://www.harvey.ai/platform/vault) project, or even adds a new knowledge source, the data uploaded is converted and stored inside of our vector databases as an embedding. Semantic and [agentic search](https://www.harvey.ai/blog/how-agentic-search-unlocks-legal-research-intelligence) is then performed upon these embeddings to establish our RAG systems. Without embeddings, retrieval in Harvey would be limited to textual search mapping, rather than the semantic (i.e., meanings-based) search capabilities that powers retrieval across our application.

An **embedding** is a learned numerical representation mapping complex, multimodal inputs into vectors that are easier for algorithmic processing. Conceptually, embedding is compression. We’re taking messy, diverse, high-dimensional raw data and turning into a standardized, fixed-length array that preserves the most important features.

![Embeddings Chart](https://www.harvey.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F07s0r5r6%2Fproduction%2F1ff2d81accd50ada524204db50f892b41be3fd34-1920x1080.jpg%3Fauto%3Dformat&w=3840&q=80)An embedding represents items as points in a space where distance captures conceptual similarity. Here, cases plotted by "criminalness" and "civilness" place securities fraud beside tax evasion and far from breach of contract.

When doing this, the embedding model preserves important features with respect to what is known as an embedding space. The geometry of this embedding space encodes meaning, so words closer together are closer in meaning. For example, the words "king" and "queen" sit closer together than "king" and "quark,” which means they likely share the same embedding space.

This makes embeddings embody richer relationships than raw categories and identifiers. Downstream models consume these embeddings as static inputs rather than learning from them, so instead of each model learning its notion of similarity from scratch, they can plug into the same embedding space. This means our retrieval process can be model-agnostic, efficient, and powerful [without training on customer data](https://www.harvey.ai/blog/how-harvey-manages-customer-data).

## What is Embedding Reversal?

What if an attacker somehow obtains access to an embedding? Can they recover the underlying data?

This attack, known as **embedding reversal** or embedding inversion, has been heavily researched. A common assumption is that embeddings cannot be reversed in practice. But that assumption underestimates what genuine non-reversibility actually requires. Cryptographic hash functions are actual objects purpose-built to be non-reversible (among other objectives). These have demanded decades of dedicated research, and even these purpose-built constructions require ongoing scrutiny.

Embeddings were never designed with non-reversibility in mind. They are built for the opposite: preserving as much semantic structure as possible so downstream models can reason over it. If a cryptographic hash is an object that tries to erase structure, an embedding is an object that tries to expose it. **Embeddings should therefore be handled with the same care as the raw text they encode**.

Recently, [Jha et al.](https://arxiv.org/abs/2505.12540) demonstrated that an attacker can reverse any embedding model by using an unsupervised learning approach. This technique substantiates what the researchers deem the Strong Platonic Representation Hypothesis: “the universal latent structure of text representations can be learned and, furthermore, harnessed to translate representations from one space to another without any paired data or encoders.” In simpler terms, these researchers demonstrated that embeddings can be easily reversed as these models converge onto a shared embedding space.

This trend is worth paying close attention to: as embedding methods and techniques improve, so too will the sophistication of these attacks. For instance, newer techniques like [Matryoshka embeddings](https://huggingface.co/blog/matryoshka) pack more semantic information into their outputs, a property that likely inadvertently makes them easier to reverse-engineer. Earlier approaches (preceding Jha et al.) required [training a dedicated model](https://arxiv.org/abs/2310.06816) or [access to specialized paired data or encoders](https://arxiv.org/abs/2504.00147), raising the bar for attackers. That bar is falling. Future attacks will likely be faster, more accurate, and more broadly applicable, extending to specialized domains and a wider range of embedding architectures.

## Why Does This Matter?

Access to even a small amount of customer data can result in serious violations of [contextual privacy](https://nissenbaum.tech.cornell.edu/papers/Privacy%20and%20Contextual%20Integrity%20-%20Frameworks%20and%20Applications.pdf) norms. A single clause, email snippet, or header can reveal who is talking to whom, about what, and in what role, thereby exposing strategy, counterparties, or the existence of a dispute. Once such fragments leak, they can be linked with other data to reconstruct identities, timelines, and intentions far beyond what any one snippet suggests. **That’s why Harvey treats every piece of customer data as highly sensitive and designs our systems so that even limited exposure cannot cascade into a broader privacy failure**.

How bad would it be for embedding reversal to succeed? On its own, reversal can already reconstruct sensitive context from what should have been an opaque, blackbox vector. Now, it can potentially be chained to other attacks such as [context-aware tool abuse](https://arxiv.org/abs/2410.14923), [side channels](https://arxiv.org/html/2411.18191v1), [poisoning](https://arxiv.org/abs/2410.06628), [attribute inference, and membership inference](https://arxiv.org/abs/2509.20324). Even if Harvey’s current architecture prevents many of these attacks in practice, we design knowing that our product will evolve over time and that these attacks will become cheaper, more general, and more automated over time. **The security guarantees we offer today must remain true as the AI ecosystem evolves and novel AI security issues emerge**.

## Our Defense Philosophy

Harvey’s strategy does not depend on embeddings being "hard to reverse," but instead on making it extremely difficult for an attacker to obtain them in the first place, and limiting the damage even if they did.

We know that our defense must be:

- **Robust**: We want to be secure against new attacks and improvements in attacker capabilities.

- **Future-proof**: Adopting new techniques and paradigms should not quietly erode our security .

- **Secure-by-default**: A misconfiguration or dependency bug should not undermine our guarantees.

- **Enterprise-grade**: We have to be scalable and compose with your existing security controls.


### How we Protect Against Embedding Reversal

We've previously written about how we [manage customer data](https://www.harvey.ai/blog/how-harvey-manages-customer-data) at Harvey. Here, we'll focus specifically on how those principles apply to embeddings.

We start with isolation at the database layer. **Harvey stores embeddings in a vector database, and we partition that storage so that each workspace has its own dedicated, isolated footprint, backed by separate collections and storage.** A query issued on behalf of one customer cannot see or reference another customer’s vectors, because the database itself is segmented along tenant boundaries and tenant IDs rather than filtered after the fact.

Even if two organizations use Harvey in the same region and on the same underlying cloud provider, their embedding data sits in distinct, non-overlapping namespaces. That separation is a foundational control: it prevents cross-tenant bleed-through even before you consider model behavior or application logic.

We also understand that legal work is inherently collaborative. At Harvey, we’ve introduced [Shared Spaces](https://help.harvey.ai/release-notes/shared-spaces) and we’ll continue to build multi-party features, making it even more important for these workspace separation controls to be strong and robust.

Next, when we generate vectors from your documents, we do so to **support retrieval and search for your workspace only.** To that end, we treat embeddings as an extension of your source data such as vault documents, queries, and responses, rather than a separate, less sensitive artifact. From there, we layer several controls:

- **Embeddings are never retained for any longer than necessary**. Embeddings generated for a single query exist only for the duration of that request. Embeddings tied to stored documents follow the same customer-defined retention policies as the source (rather than being kept indefinitely as a separate corpus).

- **Access to embeddings is governed by the same disciplined engineering practices as the rest of our infrastructure.** All paths into our vector database are declared through infrastructure-as-code, so permissions, network rules, and service identities are version-controlled and reviewed rather than tweaked ad hoc. Embeddings are encrypted under the same cryptographic controls as source documents. Application services use short-lived credentials refreshed programmatically, avoiding long-lived secrets that can be exfiltrated. The result: we can reason about who can touch embeddings, audit that access, and roll back any unexpected change.

- **The working set for each request is minimized to limit the blast radius**. The system retrieves only the most relevant vectors for a workspace and assembles them into a narrow context window scoped to that interaction only. Performance caches are tenant-bound and encrypted under keys with limited lifetimes. By limiting how much data is ever "in play" at once, we reduce potential impact even if an internal component were compromised.

- **Embedding access is part of the same monitoring fabric as the rest of our data plane.** Requests are logged, correlated, and checked for anomalies in who is accessing what, when, and how. These boundaries are continuously verified to ensure our controls remain effective.


![Embeddings Diagram](https://www.harvey.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F07s0r5r6%2Fproduction%2Feafa8b2230a357c53f5e22f972574dd361ba509f-1920x1080.jpg%3Fauto%3Dformat&w=3840&q=80)

Isolation, strict access control, strong encryption, tight retention, and active verification give us a defense that is robust, future-proof, secure-by-default, and enterprise-grade.

### Why Popular Defenses Fall Short

We evaluated and rejected several common alternatives. Each fails on at least one critical dimension: fragility, operational cost, or incomplete guarantees.

- **Transforming and obfuscating embeddings in the pursuit of security is fragile**. This includes noise addition, random projections, and compression. Often, these approaches are extremely sensitive to implementation details, make incorrect assumptions of an attacker, greatly degrade retrieval quality of embeddings, or are [outright broken](https://arxiv.org/abs/2505.13758).

- **Practical cryptographic solutions are necessary but not sufficient**. They can protect embeddings at rest and in transit, but enterprise-grade retrieval systems ultimately need to compare them in the clear even if you’re relying on secure enclaves or encrypting vectors. This means a bug or side channel in the component handling decrypted embeddings can undermine the entire construction.

- **Private RAG based on PIR doesn't scale to entire enterprise-grade systems**. Private Information Retrieval (PIR) aims to hide which documents you're querying, but current approaches are typically heavy, specialized, and tailored to simple key-value access patterns. They frequently address narrow slices of a larger threat model, and they introduce significant latency without eliminating the need for architectural controls.

- **"Approximate privacy" guarantees don't meet legal expectations.** While these mechanisms are academically sound since they are tied to a specific bounded leakage (given a certain degree of leakage is permissible), legal teams expect a clear binary, not a probability: privileged material is either protected or not. These techniques are also [hard to build robustly](https://arxiv.org/abs/2112.05307) in practice.

- **Post-filtering reduces defense-in-depth to a single point of failure**. Some systems retrieve across all data and then filter results based on access permissions. This approach can introduce a [side channel to leak membership](https://arxiv.org/abs/2511.12043): an attacker may infer that certain documents exist even without seeing their contents. A bug or misconfiguration in the filter logic becomes a complete breach. We enforce access at the database layer so that unauthorized vectors are never retrieved in the first place.


We continue to track these approaches and may incorporate elements where they can be made robust and auditable. But our core strategy remains: **protect embeddings with the same trusted, well-understood mechanisms that already govern your source data**.

## From Research to Defense

Embedding reversal is just one class of attacks we secure ourselves against at Harvey. We treat embeddings as the highly sensitive customer data they are, and we've invested in strong architectural controls so that security and privacy are engineered in from the ground up, not layered on afterward.

New AI security threats will emerge. Attacker capabilities, tools, and techniques will proliferate and improve. Our promise is simple: if you bring your most sensitive work to Harvey, we engineer our systems to withstand the next breakthrough attack, not just the last one. Embeddings make our systems powerful and flexible, but never at the expense of control and security.

Stay tuned for additional research from the Harvey security team. If you want to learn more about how Harvey protects sensitive data through secure-by-design architecture, reach out to us:

## Request a Demo

Unable to load form. Please try again.

Try Again

### Thank you!

We'll be in touch shortly.

## Next Up

[![Rebuilding Review Algorithm](https://www.harvey.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F07s0r5r6%2Fproduction%2F0afeece1616ee3e756d0092d16f3500da76c0cb5-3600x2025.png%3Fauto%3Dformat&w=3840&q=80)\\
\\
****Rebuilding the Review Algorithm to Increase Accuracy and Speed****](https://www.harvey.ai/blog/rebuilding-harveys-review-algorithm) [![Building Spectre](https://www.harvey.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F07s0r5r6%2Fproduction%2F4d35c810f5439edd7ce2d98ee455309256e0977b-2400x1350.png%3Fauto%3Dformat&w=3840&q=80)\\
\\
****Building Spectre****](https://www.harvey.ai/blog/building-spectre-internal-collaborative-cloud-agent-platform) [![Harvey for Word Add-In](https://www.harvey.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F07s0r5r6%2Fproduction%2F44ea8e66c3962585156969f863084923df6f47de-2400x1350.png%3Fauto%3Dformat&w=3840&q=80)\\
\\
****Building an Agent for Complex Document Drafting and Editing****](https://www.harvey.ai/blog/building-an-agent-for-complex-document-drafting-and-editing)

Qualified
