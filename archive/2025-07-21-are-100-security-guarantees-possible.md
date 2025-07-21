---
date: '2025-07-21'
description: The article examines the feasibility of attaining 100% security guarantees
  through formal verification methods. Major cloud providers like Amazon and Microsoft
  have begun commoditizing these capabilities in response to persistent issues like
  IAM misconfigurations. Formal methods utilize mathematical proofs to assert bug-free
  code, yet their implementation is complex and resource-intensive, often limited
  to critical software. The implications for organizations include a potential paradigm
  shift in evaluating security solutions but caution against over-reliance on absolute
  claims due to coverage and definition challenges. This could drive innovation but
  necessitates careful consideration of risk management strategies.
link: https://www.darkreading.com/edge-articles/are-100-security-guarantees-possible-
tags:
- Cybersecurity
- Cloud Security
- Identity and Access Management
- Software Quality Assurance
- Formal Verification
title: Are 100% Security Guarantees Possible?
---

- [Cyber Risk](https://www.darkreading.com/cyber-risk)

[![The Edge Logo](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt530eb1f4e672eb44/653a71690e92cc040a3e9d6d/Dark_Reading_Logo_TheEdge_0.png?width=700&auto=webp&quality=80&disable=upscale)\\
\\
Cybersecurity In-Depth: Feature articles on security strategy, latest trends, and people to know.](https://www.darkreading.com/program/the-edge)

# Are 100% Security Guarantees Possible?

Large vendors are commoditizing capabilities that claim to provide absolute security guarantees backed up by formal verification. How significant are these promises?

[![Picture of Michael Bargury](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltbd8a249d11a28466/64f150aad5f7ca2f7665bf81/Michael_Bargury_zenity.jpg?width=100&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/author/michael-bargury)

[Michael Bargury](https://www.darkreading.com/author/michael-bargury), CTO & Co-Founder, Zenity

December 19, 2022

7 Min Read

![Photo illustration of a businessman surrounded by a protective dome as rain and lightning rage](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltf2fe5d5a5bb38e69/64f15681a282586cf933289f/protectivedome-alphaspirit-AdobeStock.jpg?width=1280&auto=webp&quality=80&format=jpg&disable=upscale)

Source: alphaspirit via Adobe Stock

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyber-risk/are-100-security-guarantees-possible-)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyber-risk/are-100-security-guarantees-possible-)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyber-risk/are-100-security-guarantees-possible-)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyber-risk/are-100-security-guarantees-possible-&title=Are%20100%25%20Security%20Guarantees%20Possible%3F)[Email](mailto:?subject=Are%20100%%20Security%20Guarantees%20Possible?&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Are%20100%25%20Security%20Guarantees%20Possible%3F%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyber-risk%2Fare-100-security-guarantees-possible-)

There is no software without bugs, right? While this is a common sentiment, we make assumptions that rely on the premise that software has no bugs in our day-to-day digital life. We trust identity providers (IDPs) to get authentication right, operating systems to perfectly comply with their specs, and financial transactions to always perform as intended. Even more vividly, we trust software with our physical safety by [going on planes](https://xkcd.com/2030/), driving a car that actively corrects our adherence to traffic lanes, or undergoing certain surgeries. What makes this possible? Or to put it another way, why aren't planes falling out of the sky due to bad software?

Software quality assurance borrows from scientific and engineering disciplines. Akin to reproducibility in science, one way to ensure and improve software quality is to publicize it and give as many people as possible an incentive to try to break it.

Another is using design patterns or well-architecture frameworks rooted in engineering. For example, while not every software project can be put under the same level of scrutiny as the Linux kernel, which has been under scrutiny for decades, software projects can leverage proven design patterns borrowed from the Linux kernel in hopes of gaining some of the security guarantees.

And of course, there's testing. Whether static, dynamic, or real-time, done by the developer or by a dedicated team, testing is a major part of software development. With critical software, testing is usually an entirely separate project handled by a separate team with specific expertise.

All these methods are good, but they don't claim to be comprehensive, and history suggests they aren't. There are no guarantees we found all the bugs because we don't know which bugs we don't know about (i.e., false negatives). Did we already find 99% of Linux kernel bugs out there? 50%? 10%?

## The 'Absolute' Claim

The research field of formal methods is looking at ways to assure you that there are no bugs in a certain piece of software, such as your stockbroker or certificate authority. The basic idea is to translate software into math, where everything is well-defined, and then create an actual proof that the software works with no bugs. That way, you can be sure that your software is bug-free in the same way you can be sure that every number can be decomposed to a multiplication of prime numbers. (Note that I don't define what a bug is. This will prove to be a problem, as we will later see.)

Formal method techniques have long been used for critical software, but they were extremely compute- and effort-intensive and so applied only to small pieces of software, such as a limited part of chip firmware or an authentication protocol. In recent years, advanced theorem provers like [Z3](https://en.wikipedia.org/wiki/Z3_Theorem_Prover) and [Coq](https://en.wikipedia.org/wiki/Coq) have made it possible to apply this technology in a larger context. There are now formally verified [programming languages](https://circuitcellar.com/insights/tech-the-future/the-future-of-safe-programming/), [operating systems](https://sel4.systems/About/), and [compilers](https://compcert.org/) that are 100% guaranteed to work according to their specifications. Applying these technologies still requires both advanced expertise and a ton of computing power, which make them prohibitively expensive to most organizations.

Major cloud providers are performing formal verification of their fundamental stacks to reach high levels of security assurance. [Amazon](https://www.amazon.science/research-areas/automated-reasoning) and [Microsoft](https://www.microsoft.com/en-us/research/research-area/programming-languages-software-engineering/) have dedicated research groups that work with engineering teams to incorporate formal verification methods into critical infrastructure, such as [AWS S3 and EBS](https://cslab.pepperdine.edu/warford/math221/How-Amazon-Web-Services-Uses-Formal-Methods.pdf) and [Azure Blockchain](https://www.microsoft.com/en-us/research/blog/researchers-work-to-secure-azure-blockchain-smart-contracts-with-formal-verification/?ocid=msr_blog_verisol_car). But the really interesting fact is that in the past few years, cloud providers have been [trying to](https://aws.amazon.com/security/provable-security/)[commoditize](https://www.microsoft.com/en-us/research/project/network-verification/microsoft-research-blog/) formal verification to sell to their customers.

## Decisively Solving Misconfiguration?

Last year, AWS released two features that leverage formal verification to address issues that have long plagued their customers, namely network and [identity and access management (IAM) misconfiguration](https://www.darkreading.com/cloud-security/cloud-misconfiguration-mishaps-businesses-must-watch)s. Network access and IAM configurations are complex, and that complexity grows drastically in a large organization with distributed decision-making and governance. AWS addresses it by giving its customers simple controls — such as "S3 buckets should not be exposed to the Internet" or "Internet traffic to EC2 instances must go through a firewall" — and guaranteeing to apply them in every possible configuration scenario.

AWS is not the first to address the misconfiguration problem, even for AWS-specific issues such as [open S3 buckets](https://www.darkreading.com/application-security/cloud-misconfig-exposes-3tb-sensitive-airport-data-amazon-s3-bucket). Cloud security posture management (CSPM) vendors have been addressing this issue for a while now, analyzing AWS virtual port channel (VPC) configuration and IAM roles and identifying cases where privileges are too lax, security features are not properly used, and data can be exposed to the Internet. So what's new?

Well, this is where the absolute guarantee comes in. A [CSPM solution](https://www.darkreading.com/cloud-security/what-lurks-in-the-shadows-of-cloud-security) works by creating a known-bad or known-good list of misconfigurations, sometimes adding context from your environment, and producing results accordingly. Network and IAM analyzers work by examining every potential IAM or network request and guaranteeing that they will not result in unwanted access according to your specification (such as "no Internet access"). The difference is in the guarantees about false negatives.

While AWS claims that there is no way it has missed anything, CSPM vendors say they are always on the lookout for new misconfigurations to catalog and detect, which is an admission that they did not detect these misconfigurations previously.

## What Is a Bug, Anyway?

Formal verification is great for finding well-defined issues, such as memory security issues. However, things become difficult when trying to find logical bugs because those require specifying what the code is actually supposed to do, which is exactly what the code itself does.

For one thing, formal verification requires specifying well-defined goals. While some goals, like preventing access to the Internet, seem simple enough, in reality they are not. The AWS IAM analyzer documentation has [an entire section](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html#access-control-block-public-access-policy-status) defining what "public" means, and it's full of caveats. The guarantees it provides are only as good as the mathematical claims that it has coded.

There's also the question of coverage. AWS analyzers cover only a few major AWS services. If you route traffic into your network through an outbound connection channel, or grant a service access to two separate IAM roles which can be combined to write confidential data to a public bucket, the analyzer wouldn't know. Nevertheless, on some well-defined subset of the misconfiguration problem, formal verification provides stronger guarantees than ever before.

Getting back to the relative advantage question posed above, the difference is that the IAM and network analyzer claims that its list of issues detected is comprehensive, while CSPM claims that its list covers every misconfiguration known today. Here's the key question: Should you care?

## Should We Care About Absolute Guarantees?

Consider the following scenario. You own a CSPM and look at the AWS network and IAM analyzer. Comparing the results of the two, you realize that they've identified the exact same problems. After some effort, you fix every single problem on that list. Relying only on your CSPM, you would feel you are in a good place now and could dedicate security resources elsewhere. By adding AWS analyzers to the mix, you now know — with an AWS guarantee — that you are in a good place. Are these the same results?

Even if we neglect the caveat of formal verification and assume that it catches 100% of issues, measuring the benefits over detection-based services like CSPM would be an exercise for every individual organization with its own security risk appetite. Some would find these absolute guarantees groundbreaking, while others would probably stick to existing controls.

These questions are not unique to CSPM. The same comparisons could be made for SAST/DAST/IAST web application security testing tools and formally verified software, to name one example.

Regardless of individual organization choices, one exciting side effect of this new technology would be an independent way to start measuring security solutions' false negative rates, pushing vendors to be better and providing them with clear evidence where they need to improve. This in and of itself is a tremendous contribution to the cybersecurity industry.

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyber-risk/are-100-security-guarantees-possible-)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyber-risk/are-100-security-guarantees-possible-)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyber-risk/are-100-security-guarantees-possible-)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyber-risk/are-100-security-guarantees-possible-&title=Are%20100%25%20Security%20Guarantees%20Possible%3F)[Email](mailto:?subject=Are%20100%%20Security%20Guarantees%20Possible?&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Are%20100%25%20Security%20Guarantees%20Possible%3F%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyber-risk%2Fare-100-security-guarantees-possible-)

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

Cookies Button

## About Cookies On This Site

We and our partners use cookies to enhance your website experience, learn how our site is used, offer personalised features, measure the effectiveness of our services, and tailor content and ads to your interests while you navigate on the web or interact with us across devices. By clicking "Continue" or continuing to browse our site you are agreeing to our and our partners use of cookies. For more information see [Privacy Policy](https://www.informa.com/privacy-policy/)

CONTINUE

![Company Logo](https://cdn.cookielaw.org/logos/c1f53e84-9f05-4169-a854-85052b63c50b/2ffb64fa-e393-483d-84e2-2a331bb9122e/6e7e0837-5d54-4f8b-ad38-2515147bf672/Informa_Logo_1Line_Indigo_Grad_RGB_(1)_(1).jpg)

## Cookie Policy

When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer.


[More information](https://www.informa.com/privacy-policy/)

Allow All

### Manage Consent Preferences

#### Strictly Necessary Cookies

Always Active

These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms.    You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.

#### Performance Cookies

Always Active

These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site.    All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.

#### Functional Cookies

Always Active

These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages.    If you do not allow these cookies then some or all of these services may not function properly.

#### Targeting Cookies

Always Active

These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites.    They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.

Back Button

### Cookie List

Search Icon

Filter Icon

Clear

checkbox labellabel

ApplyCancel

ConsentLeg.Interest

checkbox labellabel

checkbox labellabel

checkbox labellabel

Confirm My Choices

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)
