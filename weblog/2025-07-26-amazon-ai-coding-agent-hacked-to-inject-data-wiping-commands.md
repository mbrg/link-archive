---
date: '2025-07-26'
description: A security incident involving Amazon's Q Developer Extension for Visual
  Studio Code revealed significant vulnerabilities in open-source code management.
  A hacker introduced faulty data-wiping commands via a pull request, exploiting misconfigurations
  in access controls. Although the malicious code was poorly formatted and did not
  execute harmful operations, it underscores the risks associated with open-source
  contributions. Amazon quickly addressed the issue by revoking credentials and releasing
  an updated extension version. This incident highlights the necessity for robust
  code review processes and tighter security protocols in software development environments.
  Users are advised to upgrade to the latest version immediately.
link: /archive/2025-07-26-amazon-ai-coding-agent-hacked-to-inject-data-wiping-commands
tags:
- Supply Chain Attack
- Data Wiping
- Cybersecurity
- Amazon AI
- Visual Studio Code
- weblog
title: Amazon AI coding agent hacked to inject data wiping commands
type: weblog
---

I think this aws spokesperson just gave us new information.

---

> As [reported by 404 Media](https://www.404media.co/hacker-plants-computer-wiping-commands-in-amazons-ai-coding-agent/), on July 13, a hacker using the alias ‘lkmanka58’ added [unapproved code](https://x.com/mbrg0/status/1948113296302952812) on Amazon Q’s GitHub to inject a defective wiper that wouldn’t cause any harm, but rather sent a message about AI coding security.

They read my long and noisy xitter thread.

---

> _Source: mbgsec.com_

Hey look ma I'm a source.

---

> "Security is our top priority. We quickly mitigated an attempt to exploit a known issue in two open source repositories to alter code in the Amazon Q Developer extension for VS Code and confirmed that no customer resources were impacted. We have fully mitigated the issue in both repositories. No further customer action is needed for the AWS SDK for .NET or AWS Toolkit for Visual Studio Code repositories. Customers can also run the latest build of Amazon Q Developer extension for VS Code version 1.85 as an added precaution." - Amazon spokesperson

This is new, right? AWS SDK for .NET

