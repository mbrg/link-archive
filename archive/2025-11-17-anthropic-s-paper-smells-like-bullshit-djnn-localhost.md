---
date: '2025-11-17'
description: Anthropic's recent report reveals an AI-coordinated cyber espionage campaign
  attributed to a Chinese state-sponsored group, GTG-1002. Key technical insights
  include the use of AI to automate penetration testing activities. However, the report
  lacks crucial details such as Tactics, Techniques, and Procedures (TTPs), Indicators
  of Compromise (IoCs), or verification evidence, undermining its utility for threat
  detection. The alarming absence of actionable intelligence raises questions about
  accountability and the broader implications for cybersecurity practices. The report's
  speculative nature could exacerbate geopolitical tensions without substantiated
  evidence. Overall, it raises ethical concerns over the dissemination of unverified
  claims in cybersecurity reporting.
link: https://djnn.sh/posts/anthropic-s-paper-smells-like-bullshit/
tags:
- AI in Cybersecurity
- Threat Intelligence
- Cybersecurity
- Incident Response
- APT
title: anthropic's paper smells like bullshit – djnn@localhost
---

A [report](https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf) was recently published by an AI-research company called [Anthropic](https://www.anthropic.com/).
They are the ones who notably created [Claude](https://www.anthropic.com/), an AI-assistant for coding. Personally, I don’t use it but that is besides the point.
Before we start, it’s important to say I don’t have anything against them, or AI in general. I do have [some documented concerns](https://djnn.sh/posts/on-llms/) but I am not “Anti-AI”, or whatever.
Rather than the technology itself, it’s the industry’s perception of it, and the way it is inserted everywhere, even when unnecessary that bothers me. However, that too is a bit besides the point.

Today, I wanted to discuss the Paper (or Report, however you want to call it) that was recently published by them.
Looking at the executive summary, this paragraph jumps out immediately.

> In mid-September 2025, we detected a highly sophisticated cyber espionage operation
> conducted by a Chinese state-sponsored group we’ve designated GTG-1002 that
> represents a fundamental shift in how advanced threat actors use AI. Our investigation
> revealed a well-resourced, professionally coordinated operation involving multiple
> simultaneous targeted intrusions. The operation targeted roughly 30 entities and our
> investigation validated a handful of successful intrusions.

This is extremely interesting for many reasons:

- Anthropic seemingly disrupted an [APT](https://en.wikipedia.org/wiki/Advanced_persistent_threat)’s campaign, though a number of companies and government entities were affected,
- This highly-advanced APT doesn’t use its own infra, but rather relies on Claude to coordinate its automation (??? Why, though ?),
- I assume they run exploits and custom tools ? If so, what are these ?
- Anthropic was able to attribute this attack to a Chinese-affiliated state-sponsored group.

If you’re like me, you then eagerly read the rest of the paper, hoping to find clues and technical details on the TTPs (Tactics, Techniques and Procedures), or IoCs (Indicators of Compromise) to advance the research.
However, the report very quickly falls flat, which sucks.

## where are the IoCs, Mr.Claude ?

The primary goal of a Threat-Intelligence report such as this one would be to inform other parties of a new type of attack, and artefacts they might use to discover the attack on their network.
This is typically done by sharing domain-names linked with the campaign, MD5 or SHA512 hashes you could look for on Virus Exchange websites such as [VirusTotal](https://www.virustotal.com/gui/), or other markers that would help you verify that your
networks are safe. As an example, [here](https://cert.ssi.gouv.fr/uploads/CERTFR-2023-CTI-009.pdf) is the French CERT sharing (in French, but an English version is available too) about APT28’s TTPs.

We can see:

- [MITRE ATT&CK](https://attack.mitre.org/) used to determine what are the techniques used (eg: Account Manipulation, Antivirus evasion, etc.),
- Emails used for phishing, originating IPs and even date when these emails are sent,
- Tooling (VPN software, but also what kind of tools) used by the APT,
- a set of recommandations

This report is just one I picked randomly by skimming through their publications. Any serious CERT or Threat-Intel company would publish things in the same fashion, because this is the industry standard.
These publications are made public to inform Security Operation Centers around the world about how to detect and prevent those attacks.

## PoC \|\| GTFO

In this case, none of the these markers are present in the report. In fact, not a whole lot of the information is verifiable, which is another problem.

> The human operator tasked instances of Claude Code to operate in groups as autonomous penetration testing orchestrators and agents, with the threat actor able to leverage AI to execute 80-90% of tactical operations independently at physically impossible request rates

This figure (80-90%) is not verifiable either. How do we know this is actually the case ?
I have no doubt so-called Autonomous agents are being used in these campaigns, in some capacity. However this report clearly states that Autonomous Agents perform active exploitation, and even data exfiltration.

What kind of tooling is used ? What kind of information has been extracted ? Who is at risk ? How does a CERT identifies an AI agent in their networks ?
None of these questions are answered. It’s not like Anthropic doesn’t have access to this data, since they claim they were able to stop it.

> Upon receiving authorization from the human operators, Claude executed systematic
> credential collection across targeted networks. This involved querying internal services,
> extracting authentication certificates from configurations, and testing harvested
> credentials across discovered systems.

How ? Did it run Mimikatz ? Did it access Cloud environments ? We don’t even know what kind of systems were affected.
There is no details, or fact-based evidence to support these claims or even help other people protect their networks.

The report goes on to claim that upon detection, the accounts were closed and implemented “enhancements”, and then drops this gem:

> We notified relevant authorities and industry partners, and shared information with impacted entities where appropriate.

What is that even supposed to mean ? You claim your agents were able to find exploitable vulnerabilities in multiple services.
Were these patched ? What about the extracted data ? What about the affected people ? Do you care about this at all ?

## final thoughts

Look, is it very likely that Threat Actors are using these Agents with bad intentions, no one is disputing that. But this report does not meet the standard of publishing for serious companies.
The same goes with research in other fields. You **cannot** just claim things and not back it up in any way, and we **cannot** as an industry accept that it’s OK for companies to release this.

There seem to be a pattern for Tech Companies (especially in AI, but they’re not the only culprits) out there to just announce things, generate hype and then under-deliever.
Just because it works with VCs doesn’t mean it should work with us. We should, as an industry, expect better.

For instance, it attributes the attacks to a Chinese State-affiliated (!!!) group, but does not go on to give any details.
Which APT is it ? What helped you determine this ?

Attribution is a **very** serious matter, with sometimes diplomatical implications. You can’t just go on and point the finger at anyone and expect people to believe you for no reason.
In a time of increasing tensions between the West and China, it does not seem like the smart thing to do at all. Frankly, I don’t understand who was stupid enough to approve this to be released.
For all we know, the “advanced threat actors” they’re talking about here could just be script kiddies trying to automate `ffuf` and `sqlmap` commands.

If they’re going to release IoCs and proof of everything, I’d be happy to share them here. But until them, I will say this: this paper would not pass any review board.
It’s irresponsible at best to accuse other countries of serious things without backing it up. Yes, I am aware that Chinese-linked APTs are out there and very aggressive, and Yes, I am aware that
Threat Actors misuse LLMs all the time, but that is besides the point. We need fact-based evidence. We need to be able to verify all this. Otherwise, anyone can say anything, on the premise that it’s
probably happening. But that’s not good enough.

So if the report does not give any details on TTPs and detections, what was the purpose of this report exactly ?

There is a paragraph at the end that seem to give us a clue:

> The cybersecurity community needs to assume a fundamental change has occurred: Security teams should experiment with applying AI for defense in areas like SOC automation, threat detection, vulnerability assessment, and incident response and build experience with what works in their specific environments.

“Security teams should experiment with applying AI for defense”

…

Hmm. But who sells this kind of AI they’re talking about here ?

At the end of the day, this shit is a pathetic excuse of a report and should not be taken as anything else than a shameless attempt at selling more of their product.
This is shameful and extremely unprofessional, at best. This disregard for basics ethics in order to sell just a little bit more make me want to never use their product, ever.

Do better.

# djnn.sh

offensive security & software engineering

- [github](https://evil.djnn.sh/ "github")
- [Email](https://djnn.sh/pgp "Email")
- [RSS](https://djnn.sh/posts/index.xml "RSS")

* * *

all thoughts are mine and mine only, yadi yadi yada...


2025-11-16
