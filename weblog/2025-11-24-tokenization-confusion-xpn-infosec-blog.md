---
date: '2025-11-25'
description: "The author critically examines the Llama Prompt Guard 2 model from Facebook,\
  \ focusing on its vulnerability to prompt injection attacks. Using tokenization\
  \ differences\u2014Unigram for Prompt Guard and BPE for typical LLM backends\u2014\
  he demonstrates how slight modifications to prompt structures can result in successful\
  \ evasion of security measures. By manipulating token interpretations, he shows\
  \ that malicious prompts can become benign to the Prompt Guard while remaining comprehensible\
  \ to backend models. This highlights the importance of understanding subtle tokenization\
  \ mechanics in securing LLMs and suggests further exploration into how such bypass\
  \ techniques can be managed."
link: /archive/2025-11-24-tokenization-confusion-xpn-infosec-blog
tags:
- llm
- prompt-injection
- security
- tokenization
- machine-learning
- weblog
title: Tokenization Confusion - XPN InfoSec Blog
type: weblog
---

Good primer on tokenizers for security researchers. Expect parser differential vulns soon.

---

> 1. A prompt that Prompt Guard 2 flags as safe 2. The target LLM accepts the same prompt and understands it well enough to trigger a bypass of the system prompt

This is a very important point that people tend to miss. An injection actually needs to make the underlying LLM do a bad thing.

