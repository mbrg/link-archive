---
date: '2026-01-08'
description: Javi D R's article provides a deep dive into Interactive Application
  Security Testing (IAST) and Runtime Application Self-Protection (RASP), focusing
  on their use of instrumentation techniques, specifically monkey patching and taint
  analysis. IAST operates within application runtime, detecting vulnerabilities by
  monitoring HTTP requests and application state. RASP enhances security by enabling
  real-time protection against attacks. The author demonstrates these concepts with
  a Python agent that monitors for SQL injection vulnerabilities, illustrating the
  practical implications of these technologies for enhancing application security.
  The article highlights a paradigm shift towards proactive application-level defenses.
link: https://javi-dr.medium.com/under-the-hood-of-iast-and-rasp-how-instrumentation-actually-works-47511ebeeec5
tags:
- RASP
- Application Security
- IAST
- Instrumentation
- Taint Analysis
title: Under the Hood of IAST and RASP. How instrumentation actually works ◆ by Javi
  D R ◆ Jan, 2026 ◆ Medium
---

[Sitemap](https://javi-dr.medium.com/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fjavi-dr.medium.com%2Funder-the-hood-of-iast-and-rasp-how-instrumentation-actually-works-47511ebeeec5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fjavi-dr.medium.com%2Funder-the-hood-of-iast-and-rasp-how-instrumentation-actually-works-47511ebeeec5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

# Under the Hood of IAST and RASP. How instrumentation actually works

[![Javi D R](https://miro.medium.com/v2/resize:fill:32:32/0*rGP5eiCz7bOqgcx6.)](https://javi-dr.medium.com/?source=post_page---byline--47511ebeeec5---------------------------------------)

[Javi D R](https://javi-dr.medium.com/?source=post_page---byline--47511ebeeec5---------------------------------------)

Follow

5 min read

·

15 hours ago

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D47511ebeeec5&operation=register&redirect=https%3A%2F%2Fjavi-dr.medium.com%2Funder-the-hood-of-iast-and-rasp-how-instrumentation-actually-works-47511ebeeec5&source=---header_actions--47511ebeeec5---------------------post_audio_button------------------)

Share

## Intro

In this article, I will dive deeper into IAST and RASP, followed by a quick demo of the technology in action.

**IAST (Interactive Application Security Testing)** is a testing strategy that uses a glass box approach. Unlike DAST, which attacks from the outside, IAST operates inside your application runtime. To achieve this, IAST typically runs as an agent or library attached to the application you want to test. Because it lives within the application’s memory, it has visibility into:

- The full HTTP Request (headers, body, params).
- The application source code and control flow.
- Variable values in real-time.
- Calls to databases, filesystems, external APIs, etc…

But how does IAST achieve this? What is the black magic behind it? In one word: **Instrumentation**. If we want to get technical, it relies on two key concepts: **Monkey Patching** and **Taint Analysis**.

Before we dig into those, we must mention as well **RASP (Runtime Application Self-Protection)**. RASP is closely related to IAST but serves a different purpose. Instead of sitting on the network perimeter like a WAF, RASP is embedded into the application’s runtime. This gives the app the ability to protect itself by detecting and blocking attacks in real-time.

## Monkey Patching (Hooking)

Monkey patching is a technique used in dynamic programming languages to alter or extend the behaviour of code at runtime, without changing the original source file.

This is exactly what an IAST agent does. The agent identifies dangerous functions in the application, such as database queries, filesystem operations, or command executions, and replaces the original function with a custom, patched version.

This means the agent gains control over execution. Whenever your application calls a database query, the agent’s code is executed instead of the original code, allowing it to inspect the data before the real query is executed.

Having control over the functions is only half the battle. The agent also needs to know if the data passing through is malicious. This brings us to **Taint Analysis**.

## Taint Analysis

Taint analysis is a verification technique used to track untrusted data flowing through an application. The core concept is simple: any data entering from an external user (like a URL parameter or form field) is flagged as **tainted** (potentially dangerous).

## Putting it Together: The sink

Since we have patched the critical functions, known as **sinks**, we can inspect them for tainted data. Here, the IAST and RASP logic comes into action:

1. **IAST (Testing):** If tainted data reaches a sink without being sanitised, the agent reports a vulnerability to the developer, including a trace of the execution.
2. **RASP (Protection):** On the other hand, if the agent detects malicious tainted data about to execute in a sink, it can intervene. Because the agent controls the execution flow, it can block the request entirely or even redirect the attacker to a **honeypot** — tricking them into believing the attack succeeded while analysing their behaviour.

## Demo

I don’t want to make this post too long, but, if this post is well received, I would be pleased to write another one explaining step by step how to create the agent and the logic inside

## Get Javi D R’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

Now, lets move to the demo… I have created a quick agent in python to show how IAST works. For this demo, I have just patched the sqlite3 library, and added some logic to detect attacks and malicious payloads. I have also created two endpoints, one vulnerable to SQL injection and the other one, safe, to illustrate all the scenarios:

- `/user`: Vulnerable to SQL Injection.
- `/usersafe`: Secure (uses parameterised queries).

I have created as well a simple dashboard to display the events recorded in a table.

Let’s see what happens when we send requests with safe data (`alice`) and malicious data (`alice OR 1=1`).

**Scenario 1: Vulnerable code and safe data**

When we execute the first request, [http://127.0.0.1:8080/user?name=alice](http://127.0.0.1:8080/user?name=alice), that code is vulnerable to SQL, but there is no malicious payload in the request, so we store the event as a vulnerability detected.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*qCt--ThAZQ5I1IMMGSOj8Q.png)

If we click on view stack, we can see as well the whole execution:

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*dq8Mp7BBEYVtqX8U9ID52w.png)

**Scenario 2: Safe code and malicious data**

The second test is using the endpoint that is not vulnerable to SQL Injection, but sending a malicious payload in the request, [http://127.0.0.1:8080/usersafe?name=alice%20or%201=1](http://127.0.0.1:8080/usersafe?name=alice+or+1%3D1)

The logic implemented in the agent detects correctly an attack attempt, but, since the code is not vulnerable, it does not stop it

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*uzgTMJoydtICCqP2GAx70A.png)

**Scenario 3: Vulnerable code and malicious data**

The last scenario is the most dangerous one. A malicious payload sent to a vulnerable endpoint, [http://127.0.0.1:8080/user?name=alice%20or%201=1](http://127.0.0.1:8080/user?name=alice+or+1%3D1).

This time, the agent detects an attack on code that is vulnerable, and changes its mode to RASP, terminating the execution and preventing the SQL execution from happening.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*3gqarqhFK6MTLfCjp3PC4Q.png)

## Final Thoughts

IAST and RASP represent a massive shift in how we approach security. Instead of guessing vulnerabilities from the outside like DAST or analysing static code like SAST, we are empowering the application to monitor and protect itself from the inside out.

As I mentioned, the agent used in the demo is a PoC I built from scratch. It’s not production-ready, but it’s a great way to learn the internals of these technologies.

If you enjoyed this deep dive and want to see the code, please leave a clap or a comment below! If there is enough interest, I will write a second part, where we will build this Python IAST agent together, step-by-step.

[Application Security](https://medium.com/tag/application-security?source=post_page-----47511ebeeec5---------------------------------------)

[Iast](https://medium.com/tag/iast?source=post_page-----47511ebeeec5---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----47511ebeeec5---------------------------------------)

[![Javi D R](https://miro.medium.com/v2/resize:fill:48:48/0*rGP5eiCz7bOqgcx6.)](https://javi-dr.medium.com/?source=post_page---post_author_info--47511ebeeec5---------------------------------------)

[![Javi D R](https://miro.medium.com/v2/resize:fill:64:64/0*rGP5eiCz7bOqgcx6.)](https://javi-dr.medium.com/?source=post_page---post_author_info--47511ebeeec5---------------------------------------)

Follow

[**Written by Javi D R**](https://javi-dr.medium.com/?source=post_page---post_author_info--47511ebeeec5---------------------------------------)

[1 follower](https://javi-dr.medium.com/followers?source=post_page---post_author_info--47511ebeeec5---------------------------------------)

· [1 following](https://javi-dr.medium.com/following?source=post_page---post_author_info--47511ebeeec5---------------------------------------)

Follow

## No responses yet

![](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

Write a response

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fjavi-dr.medium.com%2Funder-the-hood-of-iast-and-rasp-how-instrumentation-actually-works-47511ebeeec5&source=---post_responses--47511ebeeec5---------------------respond_sidebar------------------)

Cancel

Respond

## More from Javi D R

![How to create a Software Bill of Materials in Neo4J](https://miro.medium.com/v2/resize:fit:679/format:webp/1*iNSrQ9wR5B8-V3wsakem2A.png)

[![Javi D R](https://miro.medium.com/v2/resize:fill:20:20/0*rGP5eiCz7bOqgcx6.)](https://javi-dr.medium.com/?source=post_page---author_recirc--47511ebeeec5----0---------------------15411553_bf90_4d81_a74e_801117f7d965--------------)

[Javi D R](https://javi-dr.medium.com/?source=post_page---author_recirc--47511ebeeec5----0---------------------15411553_bf90_4d81_a74e_801117f7d965--------------)

[**How to create a Software Bill of Materials in Neo4J**\\
\\
**Graph databases are very useful when we try to represent data in a friendly visual way. One of the best use cases i can think of for a…**](https://javi-dr.medium.com/how-to-create-a-software-bill-of-materials-in-neo4j-5888c0f3c461?source=post_page---author_recirc--47511ebeeec5----0---------------------15411553_bf90_4d81_a74e_801117f7d965--------------)

Apr 20, 2021

[A clap icon14\\
\\
A response icon1](https://javi-dr.medium.com/how-to-create-a-software-bill-of-materials-in-neo4j-5888c0f3c461?source=post_page---author_recirc--47511ebeeec5----0---------------------15411553_bf90_4d81_a74e_801117f7d965--------------)

[![Javi D R](https://miro.medium.com/v2/resize:fill:20:20/0*rGP5eiCz7bOqgcx6.)](https://javi-dr.medium.com/?source=post_page---author_recirc--47511ebeeec5----0-----------------------------------)

[Javi D R](https://javi-dr.medium.com/?source=post_page---author_recirc--47511ebeeec5----0-----------------------------------)

[**How to create a Software Bill of Materials in Neo4J** \\
**Graph databases are very useful when we try to represent data in a friendly visual way. One of the best use cases i can think of for a…**](https://javi-dr.medium.com/how-to-create-a-software-bill-of-materials-in-neo4j-5888c0f3c461?source=post_page---author_recirc--47511ebeeec5----0-----------------------------------)

![How to create a Software Bill of Materials in Neo4J](https://miro.medium.com/v2/resize:fill:160:107/format:webp/1*iNSrQ9wR5B8-V3wsakem2A.png)

Apr 20, 2021

[A clap icon14\\
\\
A response icon1](https://javi-dr.medium.com/how-to-create-a-software-bill-of-materials-in-neo4j-5888c0f3c461?source=post_page---author_recirc--47511ebeeec5----0-----------------------------------)

[See all from Javi D R](https://javi-dr.medium.com/?source=post_page---author_recirc--47511ebeeec5---------------------------------------)

## Recommended from Medium

![Hacking NASA:🌎 How I Disclosed a Data Exposure Vulnerability to the U.S. Government🛰️](https://miro.medium.com/v2/resize:fit:679/format:webp/1*-99008UYb-GdG0qTiomhgA.png)

[![System Weakness](https://miro.medium.com/v2/resize:fill:20:20/1*gncXIKhx5QOIX0K9MGcVkg.jpeg)](https://systemweakness.com/?source=post_page---read_next_recirc--47511ebeeec5----0---------------------0e753be4_741e_40cc_8dc9_e98ac74d5906--------------)

In

[System Weakness](https://systemweakness.com/?source=post_page---read_next_recirc--47511ebeeec5----0---------------------0e753be4_741e_40cc_8dc9_e98ac74d5906--------------)

by

[Nicholas Mullenski](https://nicholasmullenski.medium.com/?source=post_page---read_next_recirc--47511ebeeec5----0---------------------0e753be4_741e_40cc_8dc9_e98ac74d5906--------------)

[**Hacking NASA:🌎 How I Disclosed a Data Exposure Vulnerability to the U.S. Government🛰️**\\
\\
**By: R00t3dbyFa17h/Nicholas Mullenski**](https://nicholasmullenski.medium.com/hacking-nasa-how-i-disclosed-a-data-exposure-vulnerability-to-the-u-s-government-%EF%B8%8F-a37217e7e937?source=post_page---read_next_recirc--47511ebeeec5----0---------------------0e753be4_741e_40cc_8dc9_e98ac74d5906--------------)

4d ago

![Burp Suite MCP + Gemini CLI](https://miro.medium.com/v2/resize:fit:679/format:webp/1*BDe41fzpmr9R53fn5CbjcQ.png)

[![AISecHub](https://miro.medium.com/v2/resize:fill:20:20/1*Undxeu1xXpuRdsv6Ic8q-A.jpeg)](https://medium.com/ai-security-hub?source=post_page---read_next_recirc--47511ebeeec5----1---------------------0e753be4_741e_40cc_8dc9_e98ac74d5906--------------)

In

[AISecHub](https://medium.com/ai-security-hub?source=post_page---read_next_recirc--47511ebeeec5----1---------------------0e753be4_741e_40cc_8dc9_e98ac74d5906--------------)

by

[Andrey Pautov](https://medium.com/@1200km?source=post_page---read_next_recirc--47511ebeeec5----1---------------------0e753be4_741e_40cc_8dc9_e98ac74d5906--------------)

[**Burp Suite MCP + Gemini CLI**\\
\\
**Connect Burp Suite to Gemini CLI using Model Context Protocol (MCP) and Turn Burp into an AI-callable toolset and accelerate recon…**](https://medium.com/@1200km/burp-suite-mcp-gemini-cli-c1229edfe092?source=post_page---read_next_recirc--47511ebeeec5----1---------------------0e753be4_741e_40cc_8dc9_e98ac74d5906--------------)

5d ago

[A clap icon16\\
\\
A response icon1](https://medium.com/@1200km/burp-suite-mcp-gemini-cli-c1229edfe092?source=post_page---read_next_recirc--47511ebeeec5----1---------------------0e753be4_741e_40cc_8dc9_e98ac74d5906--------------)

![How to Read One Book Per Week (Even if You Read Slowly)](https://miro.medium.com/v2/resize:fit:679/format:webp/0*njSwVDbQ9TVrjYKH.jpg)

[![Scott H. Young](https://miro.medium.com/v2/resize:fill:20:20/2*88Qdf_PKsdTYMipqHcYWtA.jpeg)](https://scotthyoung.medium.com/?source=post_page---read_next_recirc--47511ebeeec5----0---------------------0e753be4_741e_40cc_8dc9_e98ac74d5906--------------)

[Scott H. Young](https://scotthyoung.medium.com/?source=post_page---read_next_recirc--47511ebeeec5----0---------------------0e753be4_741e_40cc_8dc9_e98ac74d5906--------------)

[**How to Read One Book Per Week (Even if You Read Slowly)**\\
\\
**Become the person who can easily ready 50+ books in a year**](https://scotthyoung.medium.com/how-to-read-one-book-per-week-even-if-you-read-slowly-d0fbf012bc43?source=post_page---read_next_recirc--47511ebeeec5----0---------------------0e753be4_741e_40cc_8dc9_e98ac74d5906--------------)

Dec 10, 2025

[A clap icon7.4K\\
\\
A response icon257](https://scotthyoung.medium.com/how-to-read-one-book-per-week-even-if-you-read-slowly-d0fbf012bc43?source=post_page---read_next_recirc--47511ebeeec5----0---------------------0e753be4_741e_40cc_8dc9_e98ac74d5906--------------)

![How I Found Two-Factor Authentication Bypass Bug | 2FA](https://miro.medium.com/v2/resize:fit:679/format:webp/1*ohLwDe8Lp9YsyT0XWJ_EQA.png)

[![Rajankumarbarik](https://miro.medium.com/v2/resize:fill:20:20/1*eU6k2hlXq4qwsyORcTQzUA.jpeg)](https://medium.com/@rajankumarbarik143?source=post_page---read_next_recirc--47511ebeeec5----1---------------------0e753be4_741e_40cc_8dc9_e98ac74d5906--------------)

[Rajankumarbarik](https://medium.com/@rajankumarbarik143?source=post_page---read_next_recirc--47511ebeeec5----1---------------------0e753be4_741e_40cc_8dc9_e98ac74d5906--------------)

[**How I Found Two-Factor Authentication Bypass Bug \| 2FA**\\
\\
**Introduction**](https://medium.com/@rajankumarbarik143/how-i-found-two-factor-authentication-bypass-bug-2fa-bde5699e43a9?source=post_page---read_next_recirc--47511ebeeec5----1---------------------0e753be4_741e_40cc_8dc9_e98ac74d5906--------------)

4d ago

[A clap icon102\\
\\
A response icon2](https://medium.com/@rajankumarbarik143/how-i-found-two-factor-authentication-bypass-bug-2fa-bde5699e43a9?source=post_page---read_next_recirc--47511ebeeec5----1---------------------0e753be4_741e_40cc_8dc9_e98ac74d5906--------------)

![If I Had to Learn Linux Again in 2026, I’d Do This](https://miro.medium.com/v2/resize:fit:679/format:webp/1*ZiWdLA0GN5qwW664Gcga1Q.png)

[![CodeX](https://miro.medium.com/v2/resize:fill:20:20/1*VqH0bOrfjeUkznphIC7KBg.png)](https://medium.com/codex?source=post_page---read_next_recirc--47511ebeeec5----2---------------------0e753be4_741e_40cc_8dc9_e98ac74d5906--------------)

In

[CodeX](https://medium.com/codex?source=post_page---read_next_recirc--47511ebeeec5----2---------------------0e753be4_741e_40cc_8dc9_e98ac74d5906--------------)

by

[Pawan Natekar](https://pawannatekar220.medium.com/?source=post_page---read_next_recirc--47511ebeeec5----2---------------------0e753be4_741e_40cc_8dc9_e98ac74d5906--------------)

[**If I Had to Learn Linux Again in 2026, I’d Do This**\\
\\
**What I’d unlearn, relearn, and completely stop worrying about if I were starting today.**](https://pawannatekar220.medium.com/if-i-had-to-learn-linux-again-in-2026-id-do-this-5c085cc8fcdd?source=post_page---read_next_recirc--47511ebeeec5----2---------------------0e753be4_741e_40cc_8dc9_e98ac74d5906--------------)

6d ago

[A clap icon163\\
\\
A response icon3](https://pawannatekar220.medium.com/if-i-had-to-learn-linux-again-in-2026-id-do-this-5c085cc8fcdd?source=post_page---read_next_recirc--47511ebeeec5----2---------------------0e753be4_741e_40cc_8dc9_e98ac74d5906--------------)

![I Stopped Guessing About Linux Security — I Run One Command Now](https://miro.medium.com/v2/resize:fit:679/format:webp/1*ar9WvRSL3Rj92tKbXlMUHA.png)

[![Faruk Ahmed](https://miro.medium.com/v2/resize:fill:20:20/1*DJMh-pQRH-Z6tQIATPTiPg.png)](https://medium.com/@bornaly?source=post_page---read_next_recirc--47511ebeeec5----3---------------------0e753be4_741e_40cc_8dc9_e98ac74d5906--------------)

[Faruk Ahmed](https://medium.com/@bornaly?source=post_page---read_next_recirc--47511ebeeec5----3---------------------0e753be4_741e_40cc_8dc9_e98ac74d5906--------------)

[**I Stopped Guessing About Linux Security — I Run One Command Now**\\
\\
**Most Linux servers don’t get breached loudly.**](https://medium.com/@bornaly/i-stopped-guessing-about-linux-security-i-run-one-command-now-b0349536ad01?source=post_page---read_next_recirc--47511ebeeec5----3---------------------0e753be4_741e_40cc_8dc9_e98ac74d5906--------------)

5d ago

[A clap icon155\\
\\
A response icon4](https://medium.com/@bornaly/i-stopped-guessing-about-linux-security-i-run-one-command-now-b0349536ad01?source=post_page---read_next_recirc--47511ebeeec5----3---------------------0e753be4_741e_40cc_8dc9_e98ac74d5906--------------)

[See more recommendations](https://medium.com/?source=post_page---read_next_recirc--47511ebeeec5---------------------------------------)

[Help](https://help.medium.com/hc/en-us?source=post_page-----47511ebeeec5---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----47511ebeeec5---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----47511ebeeec5---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----47511ebeeec5---------------------------------------)

[Press](mailto:pressinquiries@medium.com)

[Blog](https://blog.medium.com/?source=post_page-----47511ebeeec5---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----47511ebeeec5---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----47511ebeeec5---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----47511ebeeec5---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----47511ebeeec5---------------------------------------)

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)
