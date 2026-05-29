---
date: '2026-05-29'
description: A misconfigured Grafana instance on a public Meta IP unveiled a five-hop
  vulnerability chain leading to access to 507 private Meta repositories, exploiting
  a wildcard SAN TLS certificate. Using an AI-driven framework, the team identified
  and leveraged an unauthenticated GCP API endpoint to harvest sensitive tokens, culminating
  in potential full repository access. This incident highlights critical misconfigurations
  in cloud security, emphasizing the interconnectedness of identity and access management
  within cloud infrastructures. Meta addressed the issue within two days, awarding
  $157K for the responsible disclosure.
link: https://sectricity.com/blog/misconfigured-grafana-507-private-meta-repos/
tags:
- Grafana
- Red Teaming
- Bug Bounty
- Penetration Testing
- GCP
title: 'Grafana to 507 Meta Repos: A $157K Bug Chain ◆ Sectricity'
---

[Back to blog](https://sectricity.com/blog/)

Pentesting

# From a Misconfigured Grafana to 507 Private Meta Repos: A Bug Worth $157K

Sectricity Security TeamMay 28, 2026

A routine recon flag on a public Meta IP running an open Grafana grew into a five-hop chain that ended at 507 private Meta repositories. We proved impact without cloning a single file. Meta awarded $157K.

MetaBug BountyAI SecurityReconOSINTCloud SecurityPenetration TestingRed TeamingGrafanaGCPVercelGitHub

# From a Misconfigured Grafana to 507 Private Meta Repos: A Bug Worth $157K

## TL;DR

- A public Meta IP running an open Grafana grew into a five-hop chain into Meta's source code estate.
- The pivot was a wildcard SAN on the TLS certificate: \*.llm-playground.aws.metafb.cloud, which exposed a quiet shadow estate behind metafb.cloud.
- By parsing JavaScript bundles across that estate, we uncovered references to a previously unseen domain: api.haloworld.xyz, which became the next pivot point.
- Slight (AI built wordlist given JS bundles, context, etc) fuzzing against api.haloworld.xyz then exposed /\_api/gcp-token, an unauthenticated endpoint that handed out a valid GCP OAuth2 token.
- The chain went GCP token, Secret Manager, Vercel token, 85 environment variables, GitHub tokens, 507 private repositories with read/write access.
- We proved blast radius without cloning a single file. Meta awarded Preben $157K; report filed 21 March 2026, mitigated by 23 March 2026.

A few times a year we hack on Meta out of curiosity. It is one of the hardest scopes in bug bounty and we are nowhere near as sharp as the full-time Meta hunters. What we do have is an AI framework at Sectricity, doing most of the heavy lifting while we steer. We use the same approach in our [penetration testing](https://sectricity.com/services/pentesting/) and [red teaming](https://sectricity.com/services/red-team/) engagements: human judgement on top of agentic recon. By the end of the chain we were looking at 507 private Meta repositories with read/write access.

## Step 1: our AI framework, pointed at anomalies

Over the last year we have built our own agentic frameworks and custom models for the recon work we actually do. We do not point them at Meta and ask "find bugs." We ask for anomalies: things that look out of place against a baseline.

On this hunt, the framework did what would have taken a human team weeks. It chewed through Meta's public-facing infrastructure, built a baseline of what normal looked like, and handed us a short list of hosts that did not fit. One of those flags is where the chain starts.

## Step 2: a boring Grafana

One of the flagged hosts was an IP running an open Grafana. No auth, just sitting there on the public internet.

First reaction: nice. Second reaction, after poking around: boring. Dev metrics, nothing sensitive. The kind of finding most researchers file as a low-severity misconfig and move on from.

The framework did not move on. It had flagged the host for a reason and kept it on the shortlist regardless of how unimpressive the surface looked. We were ready to drop it; the framework was not. That is the part a human almost certainly gets wrong.

![](https://cdn.sanity.io/images/m7cnrai7/production/ab5705c3c79e3d442f2b8d3456b1152927964ccd-1040x1190.png?w=1200&q=85&auto=format)

_The open Grafana instance, sitting on one of the hosts our pipeline had flagged as out of place. Dev metrics, nothing sensitive, but the existence of a public Meta IP running it was the real signal._

## Step 3: the TLS cert

The Grafana itself was boring. The existence of the Grafana, on a host Meta clearly was running, was the weird part. Meta is network-strict; internal services do not leak onto the public internet without something underneath the leak. The real question was not "what is in this Grafana?" It was "why is this IP exposed at all?"

The framework pulled the TLS certificate on the IP and surfaced the SANs. The CN: \*.llm-playground.aws.metafb.cloud

![](https://cdn.sanity.io/images/m7cnrai7/production/92fc711f43cdf1943b42463439dd69035f6ae902-1199x293.png?w=1200&q=85&auto=format)

_The TLS certificate pulled from the IP. The wildcard SAN \*.llm-playground.aws.metafb.cloud was the pivot point, a domain almost nobody had heard of._

metafb.cloud was a domain almost nobody had heard of. llm-playground was an internal AI experimentation environment, exposed enough to have a public cert.

A wildcard SAN tells you whoever provisioned the cert was thinking about a whole family of hosts. We took the fingerprint to crt.sh and pulled 20 to 30 reachable subdomains off that one cert.

![](https://cdn.sanity.io/images/m7cnrai7/production/a18b9c2249c9e77a24a3009450125444df0db51f-1198x459.png?w=1200&q=85&auto=format)

_Pivoting the cert on crt.sh surfaced 20 to 30 reachable subdomains sharing the same wildcard, mapping out the shadow estate behind metafb.cloud._

## Step 4a: AI builds the wordlist

Most of the metafb.cloud subdomains were boring. To find anything interesting we needed a smart wordlist, not a generic one. And we needed somewhere to point it.

The framework had been parsing JavaScript bundles from the subdomains we could reach, extracting every URL and hostname it found. One of those references pointed at a domain we had not seen anywhere else: api.haloworld.xyz. Not on metafb.cloud, not in the cert, not in any of Meta's public surface. Just a quiet reference buried in JS.

With a new target in hand, we put the orchestration back to work. Build a context-aware wordlist for this host, grounded in what we had already seen during the recon: routes from the JavaScript bundles, words and tokens from pages we had crawled, naming patterns from sibling subdomains. The kind of list a human could assemble, but not in any reasonable time.

## Step 4b: humans (actually, tools) fuzz

We fed the wordlist into our fuzzer and walked the subdomains one by one. A few low and medium severity findings dropped out. Then we hit one that changed everything: GET https://api.haloworld.xyz/\_api/gcp-token

![](https://cdn.sanity.io/images/m7cnrai7/production/39c70e4fd8a46aaf00642b3c80263a11cb71f077-1600x900.png?w=1200&q=85&auto=format)

_The unauthenticated endpoint that handed out a valid GCP OAuth2 token to anyone who asked. No auth, no rate limit._

Unauthenticated. The endpoint returned a valid GCP OAuth2 access token to anyone who asked. A GCP access token is a key, and what it unlocks depends entirely on which identity it represents. This one represented the wrong identity.

## Step 5: the chain

We checked what the token could do, one read-only call at a time.

![](https://cdn.sanity.io/images/m7cnrai7/production/947cc1d01452313f308349904487ea4bb17d7390-1600x900.png?w=1200&q=85&auto=format)

_The five-hop chain. GCP token, Secret Manager, Vercel token, 85 env vars, GitHub tokens, 507 private repos._

The token had read access to GCP Secret Manager. Inside Secret Manager: a Vercel API token. The Vercel token exposed 85 environment variables across the org's projects. Among those env vars: multiple GitHub personal access tokens. One of those GitHub tokens had read/write access to 507 private repositories.

## Step 6: stop

When the GitHub token enumerated 507 private repos we ran one careful query, confirmed the count, and closed the tab. We did not clone anything, did not search the code, did not browse a single file tree.

The job is to prove impact, not extract it. The moment you can demonstrate blast radius, you write it up. We reported the chain; Meta's security team rotated credentials and investigated. Meta eventually rewarded Preben Ver Eecke $157K.

![](https://cdn.sanity.io/images/m7cnrai7/production/0922a8418cdaef1d97559f53cc865b6384445e89-1600x900.png?w=1200&q=85&auto=format)

_507 private repositories enumerated, zero accessed. The report was the win._

## What we would take away from this

The hard part is not the model or the bug itself. It is the scaffolding, the prompts, the feedback loops, the chaining of smaller bugs and the judgement to know which flags deserve a closer look. We have been heads-down on that for a while, and this finding is part of why.

The human-led, AI-powered pipeline that surfaced this chain is available for Sectricity clients.

## Meta's response

After reviewing this issue, we have decided to award you a bounty of $150000. Below is an explanation of the bounty amount. Meta fulfills its bounty awards through Bugcrowd.

Your report demonstrated a chain of vulnerabilities that granted access to a set of secrets that enabled you to access services with privileged access.

Following a comprehensive investigation we have decided to award you a $150.000 bounty. We have mitigated the vulnerabilities and found no evidence of abuse. Thank you for your continued efforts in helping us secure our services and protect the people that use them, we look forward to collaborating with you again in the future.

Thank you again for your report. We look forward to receiving more reports from you in the future!

**and a 5% patience bonus**

Thank you for your patience while we investigated this report. As the payment is being issued 37 days from your message with the last details required for us to reproduce the bug, we are awarding you with 5% bonus of the original payout amount.

### Timeline

- 21 March 2026: reported
- 23 March 2026: triaged and mitigated
- 29 April 2026: reward


It has been almost exactly ten years since our first Meta finding, a boring IDOR that ended up on Belgian national news. Standing on a stage in Taipei a decade later, talking about a chain that started with an open Grafana and ended at 507 private repos, feels like a decent way to mark the anniversary.

![](https://cdn.sanity.io/images/m7cnrai7/production/62235038baa4c257d11825e3a92331900c450b3c-1200x798.png?w=1200&q=85&auto=format)

_The 2016 IDOR that ended up on Belgian national news. The original Meta (Facebook then) finding, almost exactly ten years before this chain._

## Frequently Asked Questions

### Why did the chain start with an open Grafana?

The Grafana itself was not the vulnerability. It was a signal. A network-strict company like Meta does not usually leak internal services to the public internet. An open Grafana on a public Meta IP was an anomaly worth investigating, even though the dashboard content itself was boring dev metrics.

### What is a wildcard SAN and why was it the pivot in this case?

A wildcard SAN is a Subject Alternative Name on a TLS certificate that covers a whole family of hostnames, like \*.example.com. In this chain, the wildcard \*.llm-playground.aws.metafb.cloud revealed that an entire shadow estate existed behind a domain almost nobody had heard of, and the certificate fingerprint let us pull 20 to 30 reachable subdomains from public Certificate Transparency logs.

### How can an unauthenticated GCP token expose private source code?

A GCP OAuth2 access token represents an identity inside Google Cloud. If that identity has read access to Secret Manager, anyone holding the token can read every secret the identity is allowed to see. In this case those secrets included a Vercel API token, which in turn exposed 85 environment variables, which in turn contained GitHub personal access tokens with read/write access to 507 private repositories. The lesson is that secrets in cloud storage are only as protected as the weakest identity that can read them. This is one of the core failure modes we test for during a [penetration test](https://sectricity.com/services/pentesting/).

### Did Sectricity access any of the 507 private repositories?

No. We enumerated the count with a single read-only query and stopped. We did not clone, browse, or search any repository. The objective in responsible disclosure is to prove impact, not to extract data.

### How long did Meta take to fix the chain?

Two days. The chain was reported on 21 March 2026 and triaged and mitigated on 23 March 2026.

### Is this kind of approach something companies can use during pentests?

Yes. The same agentic reasoning that surfaced this chain applies to any external attack surface: shadow domains, forgotten certificates, exposed dev environments, and leaked credentials. Sectricity uses this approach in external pentests for both existing and new clients.

## Related services and resources

If your organisation runs cloud workloads on GCP, AWS, or Vercel, the failure mode in this story is not exotic; it is a chain of small misconfigurations that individually look harmless. Sectricity tests for exactly this kind of chain during a [penetration test](https://sectricity.com/services/pentesting/) and goes deeper during a [red team engagement](https://sectricity.com/services/red-team/), where we combine external recon with goal-based attacks against your real environment. For organisations exposing AI experimentation environments and LLM playgrounds to the internet, our [AI systems pentest](https://sectricity.com/services/pentesting/ai-systems/) covers the specific attack surface that LLM-adjacent infrastructure introduces. Further reading: [OWASP on common web attack surfaces](https://owasp.org/www-community/attacks/xss/) and the [MITRE ATT&CK framework](https://attack.mitre.org/) for mapping post-exploitation behaviour.
