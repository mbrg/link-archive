---
date: 2024-05-23
description: The article highlights the critical role of secure configuration management
  in cloud and SaaS environments, likening current practices to an unregulated cockpit.
  Misconfiguration remains a key cause of security vulnerabilities, exacerbated by
  fluid user interfaces and the decentralized nature of decision-making. The piece
  advocates for standardized practices to consolidate disparate efforts in mitigating
  these risks, suggesting that aligned industry standards could significantly reduce
  misconfiguration incidents. Continuous change in service functionalities adds complexity,
  necessitating robust security governance frameworks to handle evolving threats and
  configurations effectively.
link: https://www.darkreading.com/cloud-security/seizing-control-cloud-security-configuration-cockpit
tags:
- configuration-management
- cloud-security
- misconfiguration
- SaaS-security
- cybersecurity-strategy
title: Seizing Control of the Cloud Security Cockpit
---

- [Сloud Security](https://www.darkreading.com/cloud-security)

[![The Edge Logo](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt530eb1f4e672eb44/653a71690e92cc040a3e9d6d/Dark_Reading_Logo_TheEdge_0.png?width=700&auto=webp&quality=80&disable=upscale)\\
\\
Cybersecurity In-Depth: Feature articles on security strategy, latest trends, and people to know.](https://www.darkreading.com/program/the-edge)

# Seizing Control of the Cloud Security Cockpit

Much like an airplane's dashboard, configurations are the way we control cloud applications and SaaS tools. It's also the entry point for too many security threats. Here are some ideas for making the configuration process more secure.

[![Picture of Michael Bargury](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltbd8a249d11a28466/64f150aad5f7ca2f7665bf81/Michael_Bargury_zenity.jpg?width=100&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/author/michael-bargury)

[Michael Bargury](https://www.darkreading.com/author/michael-bargury), CTO & Co-Founder, Zenity

May 23, 2024

3 Min Read

![Airbus A380 cockpit, full of dials and controls and computers and joysticks](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt4ef53068f6e61e95/664e5067e0559141b7072b54/cockpit-JLBvdWOLF-alamy.jpg?width=1280&auto=webp&quality=80&format=jpg&disable=upscale)

Source: JLBvdWOLF via Alamy Stock Photo

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cloud-security/seizing-control-cloud-security-configuration-cockpit)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cloud-security/seizing-control-cloud-security-configuration-cockpit)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cloud-security/seizing-control-cloud-security-configuration-cockpit)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cloud-security/seizing-control-cloud-security-configuration-cockpit&title=Seizing%20Control%20of%20the%20Cloud%20Security%20Cockpit)[Email](mailto:?subject=Seizing%20Control%20of%20the%20Cloud%20Security%20Cockpit&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Seizing%20Control%20of%20the%20Cloud%20Security%20Cockpit%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcloud-security%2Fseizing-control-cloud-security-configuration-cockpit)

The image of a cockpit always struck me as overwhelming. So many knobs and whistles of different shapes and sizes. Do pilots really need all those options at arm's length? On every flight? And how do they verify that they're all in the right position before takeoff?

Today's enterprises have tens of millions of these — or, rather, their digital equivalent: configuration. The cloud and software as a service (SaaS) are now ubiquitous, and they brought with them countless choices to make. Unlike aircraft, we do not have standards and procedures to ensure each and every toggle is switched to the right position. It is no wonder that misconfiguration continues to be the most dominant reason for [cloud security issues](https://www.darkreading.com/cyber-risk/10-essential-processes-for-reducing-top-11-cloud-risks).

## Opaque Configurations

Commercial aircraft have thorough manuals that detail the function and implications of each and every toggle in that cockpit. For cloud and SaaS, you'll typically find a one-line explanation hidden on an obscure documentation page. If you're lucky, that short snippet is meaningful and still up to date. In most cases, however, you aren't that lucky — the docs were written three years ago and the service is now widely different. Entire companies are built on the premise of having a team of experts to figure out what these toggles do. They reverse-engineer, poke around, and brute-force their way to capture the meaning of each configuration.

In the SaaS and platform-as-a-service (PaaS) worlds, things become even worse. You never really have a full understanding of how things are built under the hood, so building an intuition about which knob does what becomes a guessing game.

## Distributed Choice

A cockpit is managed by the captain and first officer, two highly trained professionals with well-defined responsibilities. They are sometimes backed up by the flight engineer, a well-oiled human machine who triple-checks that everything is in order. For cloud and SaaS, it's the Wild West. People across the enterprise make configuration choices every day — or, worse, fail to make them and leave an insecure default on.

It's not just your cloud developers and SaaS admins, even though they have received most of the attention. Business users are making those choices, too. [They leverage low-code/no-code](https://www.darkreading.com/cyber-risk/embracing-the-next-generation-of-business-developers) to build and customize their business processes, making configuration choices by the dozens as they go.

Security teams have this problem, too. Can you really say your security stack is 100% optimized and correctly configured? How many incidents could have been prevented by a technology deployed in audit mode rather than enforcement mode?

## Constant Change

Imagine what would happen if the cockpit changed its toggles — their functionality, their implications, or just their appearance — every quarter. Now imagine it changes multiple times a day.

[Continuous delivery](https://www.darkreading.com/cyber-risk/where-there-s-no-code-there-s-no-sdlc) is the holy grail of enterprise cloud and SaaS companies hoping to move fast. We have given permission to vendors to change their offerings under the hood as much and as fast as they can. This is a good thing, mostly, because this is how excellent software gets built. However, applying that same principle to the user interface means configuration can change at an alarming rate. The meaning of an existing configuration could change as well, making it much more difficult to understand what's going on.

Even if configuration options are the same, the enterprise environment is ever-evolving. SaaS and cloud resources are connected in different ways. They hold different data subject to different sets of regulations. Risk decisions adapt as the threat landscape changes.

## It's Time for Standards

Public pressure in recent years has forced big vendors to change their insecure default, which helps put us all in a better position. S3 buckets are now [shut off from the Internet](https://aws.amazon.com/blogs/aws/heads-up-amazon-s3-security-changes-are-coming-in-april-of-2023/) by default. [So are Copilot bots](https://www.zenity.io/blog/security/microsoft-copilot-studio-vulnerabilities-explained/) built with Microsoft's Copilot Studio.

Some cloud and SaaS platforms have started publishing recommended configurations for a secure deployment. CISA and other organizations have [put out excellent recommendations](https://www.cisa.gov/resources-tools/services/secure-cloud-business-applications-scuba-project) to follow.

These are, however, all dispersed efforts. Working together through industry standards might be what is needed to finally make a real impact in reducing the ever-growing risk of misconfiguration.

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cloud-security/seizing-control-cloud-security-configuration-cockpit)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cloud-security/seizing-control-cloud-security-configuration-cockpit)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cloud-security/seizing-control-cloud-security-configuration-cockpit)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cloud-security/seizing-control-cloud-security-configuration-cockpit&title=Seizing%20Control%20of%20the%20Cloud%20Security%20Cockpit)[Email](mailto:?subject=Seizing%20Control%20of%20the%20Cloud%20Security%20Cockpit&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Seizing%20Control%20of%20the%20Cloud%20Security%20Cockpit%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcloud-security%2Fseizing-control-cloud-security-configuration-cockpit)

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
