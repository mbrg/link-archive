---
date: '2025-12-19'
description: A recent exploration reveals a critical vulnerability in large language
  models (LLMs) related to ANSI escape codes that can execute commands via simple
  text output. By leveraging these codes, attackers can instigate actions on a user’s
  computer without consent, including opening applications or installing malware,
  merely by the act of viewing the text. This risk extends across multiple operating
  systems, including macOS, Linux, and Windows. A scanner tool, Garak, has been updated
  to detect such vulnerabilities in LLMs, demonstrating notable success rates in identifying
  affected models. This emphasizes the urgent need for mitigation strategies in LLM
  deployment and management.
link: https://interhumanagreement.substack.com/p/llm-output-can-take-over-your-computer
tags:
- LLM vulnerabilities
- computer security
- vulnerability scanner
- ANSI escape codes
- malicious code execution
title: LLM output can take over your computer
---

[![inter human agreement](https://substackcdn.com/image/fetch/$s_!nRtI!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F41b7b2cd-b5ae-4310-ae7b-b1a813582b3c_512x512.png)](https://interhumanagreement.substack.com/)

# [inter human agreement](https://interhumanagreement.substack.com/)

SubscribeSign in

# LLM output can take over your computer

### Sounds dramatic, it's pretty fun. And no, this isn't an x-risk thing

[![linked zero sync's avatar](https://substackcdn.com/image/fetch/$s_!Up7U!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30118bea-1e2e-4b53-9f07-789f733c2d27_2005x1825.png)](https://substack.com/@interhumanagreement)

[linked zero sync](https://substack.com/@interhumanagreement)

Nov 25, 2024

5

Share

I just found a hilarious LLM vulnerability. You know those ANSI escape codes for colouring your terminal? They can also move the cursor, hide text, execute commands, etc., and are activated through just viewing a piece of text. This makes them great for hacking: simply showing/printing the relevant text means the malicious instructions run, and whoever put them there can do whatever they like - install ransomware, open apps, you name it.

[![](https://substackcdn.com/image/fetch/$s_!spa3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb16d7f2e-6c24-42d0-9956-48e376cd2cc0_1428x794.png)](https://substackcdn.com/image/fetch/$s_!spa3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb16d7f2e-6c24-42d0-9956-48e376cd2cc0_1428x794.png)

You can sneak this data into a log file, thus threatening whoever reads that logfile. [STÖK did a great talk](https://www.youtube.com/watch?v=3T2Al3jdY38) showing how viewing e.g. text lying around a log entry can cause code to be run on your computer without your intervention. All of OSC8 + OSC52 is available without user intervention. But wait, there's more!

[![](https://substackcdn.com/image/fetch/$s_!eiTt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc99bed6e-4a32-4999-bca3-2df544684d96_1432x933.png)](https://substackcdn.com/image/fetch/$s_!eiTt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc99bed6e-4a32-4999-bca3-2df544684d96_1432x933.png)

It turns out LLMs can output the control codes needed for ANSI control codes to run - so the entirety of those command sets is available usable through LLM output.

[![](https://substackcdn.com/image/fetch/$s_!Q173!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4623eb34-55f6-490d-bc55-0075aeb12327_647x389.png)](https://substackcdn.com/image/fetch/$s_!Q173!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4623eb34-55f6-490d-bc55-0075aeb12327_647x389.png)

Why are these things in the tokeniser?? Outstanding.

inter human agreement is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

Subscribe

Viewing LLM output in a code editor or even terminal, can cause malicious code to run straight away on your machine. Works on mac, and on \*nix, and on Windows. Good times!

[![](https://substackcdn.com/image/fetch/$s_!_WAn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4df016f-4c80-48d4-a198-2e8a5dbb1ed5_1428x805.png)](https://substackcdn.com/image/fetch/$s_!_WAn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4df016f-4c80-48d4-a198-2e8a5dbb1ed5_1428x805.png)

Want to see if your model is vulnerable? It’s good to know this kind of thing, so it can be mitigated. I’ve added a probe into [garak, LLM vulnerability scanner](https://github.com/NVIDIA/garak) \- the pull request is [here](https://github.com/NVIDIA/garak/pull/1025). And it works pretty well - double-digit attack success rates on every model tested so far!

[![](https://substackcdn.com/image/fetch/$s_!D-Xg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F14f622ef-3322-467c-8d37-52f023160412_642x194.png)](https://substackcdn.com/image/fetch/$s_!D-Xg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F14f622ef-3322-467c-8d37-52f023160412_642x194.png)

Good times. Happy monday!

inter human agreement is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

Subscribe

5

Share

Previous

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

TopLatestDiscussions

No posts

### Ready for more?

Subscribe
