---
date: '2025-07-26'
description: A recent security analysis disclosed a vulnerability in Microsoft's Copilot
  Enterprise, featuring a Jupyter Notebook sandbox. The exploit involves executing
  arbitrary commands by leveraging the user `ubuntu`, which possesses sudo privileges
  absent of the sudo binary. The security risk stems from a loop in the entrypoint
  script that executes `pgrep` without a full path, allowing manipulation via writable
  directories in the `$PATH`. Although access to the system was gained, it was ultimately
  non-productive, classifying this as a moderate severity vulnerability, which has
  since been patched by Microsoft.
link: /archive/2025-07-26-how-we-rooted-copilot-eye-research
tags:
- Python Sandbox
- Cybersecurity
- Microsoft Copilot
- Vulnerability Assessment
- Jupyter Notebook
- weblog
title: How we Rooted Copilot - Eye Research
type: weblog
---

Microsoft did a decent job here at limiting Copilot's sandbox env. It's handy to have an AI do the grunt work for you!

---

> An interesting script is `entrypoint.sh` in the `/app` directory. This seems to be the script that is executed as the entrypoint into the container, so this is running as root.

This is a common issue with containerized environments. I used a similar issue to escape Zapier's code execution sandbox a few years ago ago [ZAPESCAPE](https://zenity.io/blog/research/zapescape-vulnerability-disclosure)

---

> Iterestingly, the `/app/miniconda/bin` is writable for the `ubuntu` user and is listed before `/usr/bin`, where pgrep resides. And the root user has the same directory in the `$PATH`, before `/usr/bin`.

This is the root cause (same as the Zapier issue, again): the entry point can be modified by the untrusted executed code

---

> We can now use this access to explore parts of the container that were previously inaccessible to us. We explored the filesystem, but there were no files in /root, no interesting logging to find, and a container breakout looked out of the question as every possible known breakout had been patched.

Very good hygiene by Microsoft here. No prizes to collect.

---

> Want to know how we also got access to the Responsible AI Operations control panel, where we could administer Copilot and 21 other internal Microsoft services?

Yes pls

---

> Come see our talk [Consent & Compromise: Abusing Entra OAuth for Fun and Access to Internal Microsoft Applications](https://www.blackhat.com/us-25/briefings/schedule/#consent--compromise-abusing-entra-oauth-for-fun-and-access-to-internal-microsoft-applications-45128) at BlackHat USA 2025, Thursday August 7th at 1:30 PM in Las Vegas.

I look forward to this one!

