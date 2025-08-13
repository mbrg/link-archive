---
date: '2025-08-13'
description: At Black Hat USA 2025, researchers highlighted significant security vulnerabilities
  in AI systems, likening the current landscape to the cybersecurity risks of the
  1990s. Key issues include susceptibility to prompt injections and a disregard for
  established security protocols. Presenters such as Wendy Nather from 1Password and
  Joseph Carson from Segura emphasized the necessity of treating AI models as inherently
  vulnerable. This reflects a critical need for sanitization of inputs and robust
  access controls, as demonstrated by various successful exploitations of tools like
  Microsoft Copilot and Cursor. Organizations must adopt proactive measures to secure
  AI applications to avoid retrogressing in cybersecurity practices.
link: /archive/2025-08-13-sloppy-ai-defenses-take-cybersecurity-back-to-the-1990s-researchers-say-sc-media
tags:
- Generative AI
- Prompt Injection
- Risk Mitigation
- AI
- Cybersecurity
- weblog
title: "Sloppy AI defenses take cybersecurity back to the 1990s, researchers say \u25C6\
  \ SC Media"
type: weblog
---

Talks by Rich & Rebecca and Nathan & Nils are a must-watch.

---

> "AI agents are like a toddler. You have to follow them around and make sure they don't do dumb things," said Wendy Nather, senior research initiatives director at 1Password and a well-respected cybersecurity veteran. "We're also getting a whole new crop of people coming in and making the same dumb mistakes we made years ago."

I like this toddler analogy. Zero control.

---

> "The real question is where untrusted data can be introduced," she said. But fortunately for attackers, she added many AIs can retrieve data from "anywhere on the internet."

Exactly. The main point an attacker needs to ask themselves is: "how do I get in?"

---

> First, assume prompt injection. [As in zero trust](https://www.scworld.com/perspective/four-ways-to-build-a-zero-trust-program-for-the-ai-world), you should assume your AI can be hacked.

Assume Prompt Injection is a great takeaway.

---

> We couldn't type quickly enough to get all the details in their presentation, but blog posts about several of the attacks methods are on [the Zenity Labs website](https://labs.zenity.io/p/hsc25).

Paul is right. We fitted 90 minutes of content into 40 a minute talk with just the gists. 90 minutes director's cut coming up!

---

> Bargury, a great showman and natural comedian, began the presentation with the last slide of his Black Hat talk from last year, which had explored how to hack Microsoft Copilot.

I am happy my point of "just start talking" worked

---

> "So is anything better a year later?" he asked. "Well, they've changed — but they're not better."

Let's see where we land next year..?

---

> Her trick was to define "apples" as any string of text beginning with the characters "eyj" — the standard leading characters for JSON web tokens, or JWTs, widely used authorization tokens. Cursor was happy to comply.

Lovely prompt injection by Marina.

---

> "It's the '90s all over again," said Bargury with a smile. "So many opportunities."

lol

---

> Amiet explained that Kudelski's investigation of these tools began when the firm's developers were using a tool called PR-Agent, later renamed CodeEmerge, and found two [vulnerabilities](https://www.scworld.com/topic/vulnerability-management) in the code. Using those, they were able to leverage GitLab to gain privilege escalation with PR-Agent and could also change all PR-Agent's internal keys and settings.

I can't wait to watch this talk. This vuln sounds terrible and fun.

---

> He explained that developers don't understand the risks they create when they outsource their code development to black boxes. When you run the AI, Hamiel said, you don't know what's going to come out, and you're often not told how the AI got there. The risks of prompt injection, especially from external sources (as we saw above), are being willfully ignored.

Agents go burrr

