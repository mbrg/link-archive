---
date: '2025-07-21'
description: The rise of low-code/no-code development poses significant challenges
  to traditional software development life cycle (SDLC) security practices. This paradigm
  shift enables business users to rapidly build applications without formal coding,
  bypassing critical security gates established in SDLCs. To mitigate risks, organizations
  must adapt by embedding security directly within these platforms, ensuring ease
  of use for non-technical users while upholding security and compliance standards.
  Cross-industry frameworks are emerging to address these new dynamics, highlighting
  the necessity of guiding citizen developers in secure application creation to maintain
  effective governance without stifling productivity.
link: https://www.darkreading.com/edge-articles/where-there-s-no-code-there-s-no-sdlc
tags:
- No-Code
- Low-Code
- Cybersecurity
- Application Security
- SDLC
title: Where There's No Code, There's No SDLC
---

- [Cyber Risk](https://www.darkreading.com/cyber-risk)

[![The Edge Logo](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt530eb1f4e672eb44/653a71690e92cc040a3e9d6d/Dark_Reading_Logo_TheEdge_0.png?width=700&auto=webp&quality=80&disable=upscale)\\
\\
Cybersecurity In-Depth: Feature articles on security strategy, latest trends, and people to know.](https://www.darkreading.com/program/the-edge)

# Where There's No Code, There's No SDLC

How can we build security back into software development in a low-code/no-code environment?

[![Picture of Michael Bargury](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltbd8a249d11a28466/64f150aad5f7ca2f7665bf81/Michael_Bargury_zenity.jpg?width=100&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/author/michael-bargury)

[Michael Bargury](https://www.darkreading.com/author/michael-bargury), CTO & Co-Founder, Zenity

April 18, 2023

3 Min Read

![Conceptual Illustration of Low Code and No Code Development Platforms](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blta0a80d39808fdd66/64f17366018a7cb872822f51/nocode-ArtemisDiana-AdobeStock.jpg?width=1280&auto=webp&quality=80&format=jpg&disable=upscale)

Source: ArtemisDiana via Adobe Stock

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyber-risk/where-there-s-no-code-there-s-no-sdlc)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyber-risk/where-there-s-no-code-there-s-no-sdlc)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyber-risk/where-there-s-no-code-there-s-no-sdlc)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyber-risk/where-there-s-no-code-there-s-no-sdlc&title=Where%20There%27s%20No%20Code%2C%20There%27s%20No%20SDLC)[Email](mailto:?subject=Where%20There%27s%20No%20Code,%20There%27s%20No%20SDLC&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Where%20There%27s%20No%20Code%2C%20There%27s%20No%20SDLC%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyber-risk%2Fwhere-there-s-no-code-there-s-no-sdlc)

We’ve come to rely heavily on the software development life cycle (SDLC) as the go-to method for getting security ingrained into development processes. In fact, the assumption of a comprehensive continuous integration/continuous delivery (CI/CD) has become so fundamental that we as an industry spent most of last year focused on addressing one of its derivatives: security of the CI/CD pipeline as the centerpiece of the software supply chain. This is good news, of course. A proper SDLC and its operational manifestation, the CI/CD, has allowed us to embed security controls where they are most useful — while developers are building and testing their software.

With the continued soar of low-code/no-code and citizen development in the enterprise, many AppSec teams have been occupied with creating secure development guidelines for these new business applications. [Cross-industry collaborations](https://owasp.org/www-project-top-10-low-code-no-code-security-risks/) have emerged to provide a security risk framework. The real challenge, however, is bringing this new wave of [business users becoming developers](https://www.darkreading.com/cyber-risk/embracing-the-next-generation-of-business-developers) under the security umbrella.

Business users are best at knowing what the business needs, and so they are best positioned to address those needs when empowered with low-code/no-code tools that allow them to build their own applications. On the other hand, trying to discuss security risks or development practices with business users can prove challenging.

Embedding security in the SDLC works because it is where it is more comfortable for developers to consume it, making it less costly to fix a security vulnerability. In order to do the same for business users, we must understand how their process for building applications works.

## R.I.P. to the SDLC

A boilerplate version of the SDLC shows how software goes from articulating a need by the business; to planning, development, and testing by engineering and Q&A teams; to deployment, monitoring, and management by the operations teams. This, of course, varies widely across organizations. The important point for our discussion is that the responsibility is shifted among different teams and perhaps different departments throughout the development life cycle. Every transition can also be harnessed as a quality or security assurance gate, whether automated, like SAST/DAST/IAST tools, or manually, like threat modeling or security review.

In contrast, consider the low-code/no-code development process. A business user articulates their needs, moves on to creating their application or automation with an intuitive drag and drop interface, clicks save, and ... that’s it! Sometimes even the save step is skipped with a helpful autosave. Although not all low-code/no-code applications are built this way by the person who envisioned them, many are. Note how much faster the development process can be now — no exchange of responsibility or convincing someone else to align with your goals, and everyone can address their own business needs as they are spotted, on their own. This is the power of business-led development and mature citizen-development initiatives.

Unfortunately, it comes at the cost of skipping those security and quality gates we’ve baked into the development life cycle. These gates were critical, especially in an enterprise that needs to enforce values that are just as important as business productivity: security, compliance, and privacy, to name a few.

## Meeting Developers Where They Are

Business users [are building and will continue to build](https://www.darkreading.com/cyber-risk/you-can-t-opt-out-of-citizen-development) more applications than we’ve ever seen before. To bring them under the security umbrella, we must meet them where they are and speak their language. Instead of relying on the existence of a CI/CD pipeline and introducing business users to concepts like production versus test environments, we should accept reality and focus on making it easy to create secure applications and difficult to create risky ones.

To do this, we must understand the low-code/no-code platforms they use to build applications and the ways in which these applications are built and adopted by others. We must embrace our responsibility to guide these new developers, apply security best practices to the applications they create according to our organization's risk appetite, and take a retroactive approach to address critical issues swiftly.

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyber-risk/where-there-s-no-code-there-s-no-sdlc)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyber-risk/where-there-s-no-code-there-s-no-sdlc)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyber-risk/where-there-s-no-code-there-s-no-sdlc)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyber-risk/where-there-s-no-code-there-s-no-sdlc&title=Where%20There%27s%20No%20Code%2C%20There%27s%20No%20SDLC)[Email](mailto:?subject=Where%20There%27s%20No%20Code,%20There%27s%20No%20SDLC&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Where%20There%27s%20No%20Code%2C%20There%27s%20No%20SDLC%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyber-risk%2Fwhere-there-s-no-code-there-s-no-sdlc)

## About the Author

[![Michael Bargury](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltbd8a249d11a28466/64f150aad5f7ca2f7665bf81/Michael_Bargury_zenity.jpg?width=400&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/author/michael-bargury)

[Michael Bargury](https://www.darkreading.com/author/michael-bargury)

CTO & Co-Founder, Zenity

Michael Bargury is an industry expert in cybersecurity focused on cloud security, SaaS security, and AppSec. Michael is the CTO and co-founder of Zenity.io, a startup that enables security governance for low-code/no-code enterprise applications without disrupting business. Prior to Zenity, Michael was a senior architect at Microsoft Cloud Security CTO Office, where he founded and headed security product efforts for IoT, APIs, IaC, Dynamics, and confidential computing. Michael holds 15 patents in the field of cybersecurity and a BSc in Mathematics and Computer Science from Tel Aviv University. Michael is leading the OWASP community effort on low-code/no-code security.

[See more from Michael Bargury](https://www.darkreading.com/author/michael-bargury)

Keep up with the latest cybersecurity threats, newly discovered vulnerabilities, data breach information, and emerging trends. Delivered daily or weekly right to your email inbox.

[Subscribe](https://dr-resources.darkreading.com/c/pubRD.mpl?secure=1&sr=pp&_t=pp:&qf=w_defa3135&ch=drwebbutton)

More Insights

Webinars

- [Think Like a Cybercriminal to Stop the Next Potential Attack](https://dr-resources.darkreading.com/c/pubRD.mpl?secure=1&sr=pp&_t=pp:&qf=w_cmdc03&ch=SBX&cid=_upcoming_webinars_8.500001572&_mc=_upcoming_webinars_8.500001572) Jul 22, 2025
- [Elevating Database Security: Harnessing Data Threat Analytics and Security Posture](https://dr-resources.darkreading.com/c/pubRD.mpl?secure=1&sr=pp&_t=pp:&qf=w_rubr156&ch=SBX&cid=_upcoming_webinars_8.500001574&_mc=_upcoming_webinars_8.500001574) Jul 23, 2025
- [The DOGE-effect on Cyber: What's happened and what's next?](https://www.brighttalk.com/webcast/18975/628444?utm_source=brighttalk-darkreading&utm_medium=web&utm_campaign=curation04242025&cid=_upcoming_webinars_8.500001554&_mc=_upcoming_webinars_8.500001554) Jul 24, 2025
- [Solving ICS/OT Patching and Vulnerability Management Conundrum](https://dr-resources.darkreading.com/c/pubRD.mpl?secure=1&sr=pp&_t=pp:&qf=w_txon82&ch=SBX&cid=_upcoming_webinars_8.500001577&_mc=_upcoming_webinars_8.500001577) Jul 30, 2025
- [Creating a Roadmap for More Effective Security Partnerships](https://dr-resources.darkreading.com/c/pubRD.mpl?secure=1&sr=pp&_t=pp:&qf=w_defa8838&ch=SBX&cid=_upcoming_webinars_8.500001578&_mc=_upcoming_webinars_8.500001578) Aug 14, 2025

[More Webinars](https://www.darkreading.com/resources?types=Webinar)

Events

- [\[Virtual Event\] Strategic Security for the Modern Enterprise](https://ve.informaengage.com/virtual-events/strategic-security-for-the-modern-enterprise/?ch=sbx&cid=_session_16.500334&_mc=_session_16.500334) Jun 26, 2025
- [\[Virtual Event\] Anatomy of a Data Breach](https://ve.informaengage.com/virtual-events/an-anatomy-of-a-data-breach-and-what-to-do-if-it-happens-to-you/?ch=sbx&cid=_session_16.500333&_mc=_session_16.500333) Jun 18, 2025
- [\[Conference\] Black Hat USA - August 2-7 - Learn More](https://www.blackhat.com/us-25/?_mc=we_bhas25_drcuration&cid=_session_16.500330) Aug 2, 2025

[More Events](https://www.darkreading.com/events)

You May Also Like

* * *

### Edge Picks

[thumbnail![](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltffc178dab705140f/684c22b62ecd3f8eb7f9a606/ad-blocker-tofino-alamy.jpg?width=700&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/cyber-risk/browser-extensions-heightened-manageable-security-risks) [Cyber Risk](https://www.darkreading.com/cyber-risk)

[Browser Extensions Pose Heightened, but Manageable, Security Risks](https://www.darkreading.com/cyber-risk/browser-extensions-heightened-manageable-security-risks) [Browser Extensions Pose Heightened, but Manageable, Security Risks](https://www.darkreading.com/cyber-risk/browser-extensions-heightened-manageable-security-risks)

[URL bar of a browser showing part of a website address![](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt516ba50b3094017d/6849369a2e0a1044ba06abb3/Browser-creativep-alamy.jpg?width=700&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/endpoint-security/gartner-secure-enterprise-browser-adoption-25-by-2028) [Endpoint Security](https://www.darkreading.com/endpoint-security)

[Gartner: Secure Enterprise Browser Adoption to Hit 25% by 2028](https://www.darkreading.com/endpoint-security/gartner-secure-enterprise-browser-adoption-25-by-2028) [Gartner: Secure Enterprise Browser Adoption to Hit 25% by 2028](https://www.darkreading.com/endpoint-security/gartner-secure-enterprise-browser-adoption-25-by-2028)

[Icons for Chrome, Edge, and Firefox browsers on a screen![](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt01b9c36c6effed9b/68654f0eaa6325395eb4af3a/browser_Tada_Images_shutterstock.png?width=700&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/endpoint-security/clickfix-spin-off-bypassing-key-browser-safeguards) [Endpoint Security](https://www.darkreading.com/endpoint-security)

[ClickFix Spin-Off Attack Bypasses Key Browser Safeguards](https://www.darkreading.com/endpoint-security/clickfix-spin-off-bypassing-key-browser-safeguards) [ClickFix Spin-Off Attack Bypasses Key Browser Safeguards](https://www.darkreading.com/endpoint-security/clickfix-spin-off-bypassing-key-browser-safeguards)

[Stream of 0s and 1s running alongside padlock icons![](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt528f12d2e4d4e3c3/672cf7b054a4f4676ff70996/vs148-software-security-debt-shutterstock.jpg?width=700&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/endpoint-security/extension-poisoning-campaign-gaps-browser-security) [Endpoint Security](https://www.darkreading.com/endpoint-security)

[Extension Poisoning Campaign Highlights Gaps in Browser Security](https://www.darkreading.com/endpoint-security/extension-poisoning-campaign-gaps-browser-security) [Extension Poisoning Campaign Highlights Gaps in Browser Security](https://www.darkreading.com/endpoint-security/extension-poisoning-campaign-gaps-browser-security)

Latest Articles in The Edge

- [Women Who 'Hacked the Status Quo' Aim to Inspire Cybersecurity Careers](https://www.darkreading.com/cybersecurity-operations/women-hacked-status-quo-cybersecurity-careers) Jul 16, 2025
\|

5 Min Read

- [AI Is Reshaping How Attorneys Practice Law](https://www.darkreading.com/cyber-risk/ai-is-reshaping-how-attorneys-practice-law) Jul 15, 2025
\|

5 Min Read

- [Browser Exploits Wane as Users Become the Attack Surface](https://www.darkreading.com/vulnerabilities-threats/browser-exploits-wane-users-become-attack-surface) Jul 9, 2025
\|

6 Min Read

- [Unlock Security Operations Success With Data Analysis](https://www.darkreading.com/cybersecurity-analytics/unlock-security-operations-success-data-analysis) Jul 8, 2025
\|

2 Min Read


[Read More The Edge](https://www.darkreading.com/program/the-edge)
