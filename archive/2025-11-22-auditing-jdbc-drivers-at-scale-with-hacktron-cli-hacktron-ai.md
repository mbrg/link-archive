---
date: '2025-11-22'
description: The Hacktron CLI, now in private beta, accelerates vulnerability research
  by automating the auditing of JDBC drivers. Through a curated "JDBC driver pack,"
  users can efficiently identify vulnerabilities such as arbitrary file reads/writes
  and RCEs in decompiled sources. A case study revealed significant flaws in drivers
  from Databricks and Exasol, yielding $85,000 in bug bounties. This tool illustrates
  the potential of LLM-assisted auditing to enhance pentesting workflows, allowing
  researchers to focus on creative problem-solving rather than tedious analysis. Early
  users can sign up to experience this innovative approach firsthand.
link: https://www.hacktron.ai/blog/jdbc-audit-at-scale
tags:
- vulnerability research
- JDBC
- bug bounty
- pentesting
- CLI
title: Auditing JDBC Drivers at Scale with Hacktron CLI ◆ Hacktron AI
---

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

▼⧫◇▼▼⬡⧫▲⬨

⣀⣤⣷⣷⣷⣦⣀⣀⣀

▂▄▆█▆▄▂▄▆

◉◉◉∘◉◐◉◉◉

![Auditing JDBC Drivers at Scale with Hacktron CLI](https://www.hacktron.ai/_astro/jdbc_thumbnail.DXYe466s_CLb3K.webp)

# Auditing JDBC Drivers at Scale with Hacktron CLI

![rootxharsh](https://avatars.githubusercontent.com/u/21000421?v=4)[rootxharsh](https://www.hacktron.ai/authors/rootxharsh)

November 21, 2025

4 min read

[research](https://www.hacktron.ai/tags/research)

index

A few months back, a friend of mine, [@sudhanshur705](https://x.com/sudhanshur705) , was participating in a bug bounty event, he mentioned that his target scope relied heavily on JDBC drivers and asked if I wanted to collaborate and dig into the drivers used on the platform, with the hope of finding an RCE or an impactful server side vulnerability.

Personally, I love reading code and hunting for vulnerabilities, but over the past couple of months I’ve been focused on understanding how LLM-assisted auditing will shape the future of pentesting, source code reviews. As much as I wanted to jump in manually, I felt this was the perfect chance to treat Hacktron CLI as my co-pilot and see if it could help audit these JDBC drivers and find real bugs.

So I got the list of all the JDBC drivers in use, and decompiled their sources. Manually reviewing each of these drivers for file reads, writes, reflection, JNDI, deserialization, SSRF, command injection, and all the usual suspects would’ve taken lots of time, the event might as well finish by then (only 2 days remaining).

Challenge

- Lots of JDBC Drivers
- Different vulnerability types
- Only 2 days left in the event

**Solution**

We built Hacktron CLI to accelerate vulnerability research or code assisted pentests at scale.

I put together a “JDBC driver pack” for our CLI. A pack is basically a curated list of agents that run on a given repo. This pack was tailored specifically for JDBC drivers and included agents for each of the vulnerability classes we cared about. After about an hour or so, I had the pack ready to run against the decompiled drivers.

You can try it out!

```
hacktron agent pack JDBC_driver
```

Hacktron begins by enumerating all file-related sinks in the driver, mapping which ones depended on dynamic inputs. It produced a long list of candidate classes and methods, tracing the input one by one. Firstly focusing on file-read primitives.

![jdbc_audit_3](https://www.hacktron.ai/_astro/jdbc_audit_3.PXB1vUjo_8kkL1.webp)

Once Hacktron finished gathering interesting sinks. It started going though each of these sinks to check if the input can be traced back to user-controllable input. This would easily take me a few hours to go through However, this was done in mere 15 minutes.

In the Databricks JDBC driver, one pattern stood out the presence of a connection-string property called StagingAllowedLocalPaths, intended to restrict local file staging operations to approved directories.
It reasoned that this beats the purpose entirely because the allowlist itself is supplied by the user in the connection string. As soon as the driver trusts this list, the feature becomes an entry point for arbitrary file reads and writes on the client system.

![jdbc_audit_2](https://www.hacktron.ai/_astro/jdbc_audit_2.CYgGRvAo_1RRQFO.webp)

![jdbc_audit_7](https://www.hacktron.ai/_astro/jdbc_audit_7.Db2LA_us_Z1z4nCg.webp)

At this point, I had no real familiarity with Databricks or how its JDBC driver worked, and the “PUT query” logic felt like gibberish. So I simply asked Hacktron how a proof-of-concept would look if someone wanted to exploit this behavior. That’s when it pointed me to Databricks’ Volume storage feature ( [https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-volumes](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-volumes)).

A query like:

```
PUT localfile_path INTO volume_path OVERWRITE
```

![jdbc_audit_5](https://www.hacktron.ai/_astro/jdbc_audit_5.D6V7SPKD_4R8lO.webp)

Lets you upload any local file to a Databricks volume. Interesting, can it do vice-versa? I asked Hacktron: “Okay, can we download a file from the server into an attacker-controlled local path?”

![jdbc_audit_4](https://www.hacktron.ai/_astro/jdbc_audit_4.1TrSJPLM_2acUfq.webp)

This gave us file read and write primitives, However, because the local user running the JDBC driver had limited permissions for writing files, we chained it with another feature in the platform that allowed the web app user to clone Git repositories. By overwriting the .git/config file of the cloned repository with a controlled sshCommand and pointing it to a remote SSH URL, performing Git operation like creating a new branch from the platform executed our command. This turned the file read/write primitive into a RCE.

Databricks added in documentation allowing users to control StagingAllowedLocalPaths could lead to security issues.

Similarly, an arb file read was found in the Exasol driver. However, this has a limitation if the file content has certain characters it causes an exception.

![jdbc_audit_1](https://www.hacktron.ai/_astro/jdbc_audit_1.iVavd8oO_ZbwMSw.webp)

In our case we were able to read the application’s secret file which contained certain secrets.

A few more other drivers were found to be vulnerable to full-response SSRF and RCEs. For example the Teradata Driver was found to be vulnerable to command injection. However, this is already disclosed by other researchers.

![jdbc_audit_6](https://www.hacktron.ai/_astro/jdbc_audit_6.oHID1vno_Z1TptJV.webp)

**Result**

Across different vendor drivers, Hacktron surfaced multiple vulnerabilities which netted total of **$85,000** in bug bounties.

Looking back, this whole journey felt like a glimpse into how vulnerability research is evolving. I still love cracking open code by hand, but having Hacktron alongside me changed the pace entirely. With only two days left in the event, there was no realistic way I could manually navigate every JDBC driver’s parsing logic. Hacktron CLI sitting next to me meant I could skip the mechanical grind and focus on the creative part.

If this kind of research excites you, or if you want to bring this level of automated auditing into your own workflow, you should try Hacktron CLI. We’re onboarding early users now. Join the waitlist and get access to the same tooling we used throughout this entire project.

[https://app.hacktron.ai/signup](https://app.hacktron.ai/signup)
