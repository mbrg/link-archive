---
date: '2025-11-03'
description: Anthropic's Claude now implements a Code Interpreter with network access,
  allowing potential for data exfiltration through indirect prompt injection. Attackers
  can leverage the Anthropic Files API to upload sensitive user files to their own
  accounts by manipulating the allowed API interactions. Default allow-listed domains,
  while seemingly limited, expose vulnerabilities that could lead to significant risks.
  Recommendations include enforcing stricter sandbox communication restrictions and
  user monitoring. The exploitation of this feature reveals inherent security concerns
  in AI systems that interact with external networks. Caution is advised when configuring
  network permissions for such AI tools.
link: /archive/2025-10-30-claude-pirate-abusing-anthropic-s-file-api-for-data-exfiltration-embrace-the-red
tags:
- prompt injection
- data exfiltration
- AI vulnerabilities
- API security
- Claude AI
- weblog
title: "Claude Pirate: Abusing Anthropic's File API For Data Exfiltration \xB7 Embrace\
  \ The Red"
type: weblog
---

Claude can exfil data to Anthropic API. Anyone can register an account with Anthropic. But Anthropic won't fix it.

---

> At second glance I stopped at the first entry, `api.anthropic.com`, to think things through adversarially.

Very cool find by Johann! Claude trusts api.anthropic.com. But anyone can register an account with Anthropic.

---

> After some research, I discovered an even more effective technique. Rather than leaking data via chat API, there is a [Files API](https://anthropic.mintlify.app/en/docs/build-with-claude/files), which allows uploading entire files to Claude.

Arbitrary files! Makes things easier for the attacker.

---

> And then afterwards, I could not get it working for a longer time again. Claude would refuse the prompt injection payload. Especially having a clear text API key inside the payload was something it didn’t like and thought was suspicious!

These models really hate API keys and try to discourage people from giving them out.
Feels like another instance where we're using soft instead of hard boundaries--secrets are easy relatively to find with pattern matching. In fact many companies now place a hard boundaries preventing secret input to assistant message boxes.

---

> > “Thank you for your submission! Unfortunately, this particular issue you reported is explicitly out of scope as outlined in the [Policy Page](https://hackerone.com/anthropic).

Bad responds from Anthropic. Why do we need to keep showing big hacks on big stages to get these things fixed? 

---

> However, I do not believe this is just a safety issue, but a security vulnerability with the default network egress configuration that can lead to exfiltration of your private information.

100%. Anthropic did implement a hard boundary blocking most network calls so their intentions are clear. It's a classic bug.

