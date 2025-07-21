---
date: '2025-07-21'
description: The emergence of enterprise-level generative AI tools, such as OpenAI's
  custom GPTs and Microsoft's Copilot Studio, enables business users to easily create
  AI applications using organizational data. These tools facilitate user impersonation,
  complicating security oversight, as AI actions become indistinguishable from legitimate
  user activities. Security teams must shift focus from traditional monitoring to
  integrating strategies that account for citizen-developed applications, particularly
  as low-code/no-code platforms proliferate. Adopting industry standards for assessing
  risks associated with these applications will be crucial for maintaining security
  in an evolving landscape dominated by agile AI development.
link: https://www.darkreading.com/cyber-risk/enterprise-generative-ai-enters-its-citizen-development-era
tags:
- Generative AI
- No-Code Development
- Cybersecurity
- Citizen Development
- Enterprise Security
title: Enterprise Generative AI Enters Its Citizen Development Era
---

- [Cyber Risk](https://www.darkreading.com/cyber-risk)

[![The Edge Logo](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt530eb1f4e672eb44/653a71690e92cc040a3e9d6d/Dark_Reading_Logo_TheEdge_0.png?width=700&auto=webp&quality=80&disable=upscale)\\
\\
Cybersecurity In-Depth: Feature articles on security strategy, latest trends, and people to know.](https://www.darkreading.com/program/the-edge)

# Enterprise Generative AI Enters Its Citizen Development Era

Business users are building Copilots and GPTs with enterprise data. What can security teams do about it?

[![Picture of Michael Bargury](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltbd8a249d11a28466/64f150aad5f7ca2f7665bf81/Michael_Bargury_zenity.jpg?width=100&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/author/michael-bargury)

[Michael Bargury](https://www.darkreading.com/author/michael-bargury), CTO & Co-Founder, Zenity

November 19, 2023

4 Min Read

![Robot version of a human hand hangs in a display case in Dortmund art exhibition; photo by Bernd Thissen](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt5fefa7b26ae3cb5b/655f4a4b71d6b8040a39617b/robothand-dpa_picture_alliance-alamy.jpg?width=1280&auto=webp&quality=80&format=jpg&disable=upscale)

Source: dpa picture alliance via Alamy Stock Photo

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyber-risk/enterprise-generative-ai-enters-its-citizen-development-era)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyber-risk/enterprise-generative-ai-enters-its-citizen-development-era)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyber-risk/enterprise-generative-ai-enters-its-citizen-development-era)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyber-risk/enterprise-generative-ai-enters-its-citizen-development-era&title=Enterprise%20Generative%20AI%20Enters%20Its%20Citizen%20Development%20Era)[Email](mailto:?subject=Enterprise%20Generative%20AI%20Enters%20Its%20Citizen%20Development%20Era&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Enterprise%20Generative%20AI%20Enters%20Its%20Citizen%20Development%20Era%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyber-risk%2Fenterprise-generative-ai-enters-its-citizen-development-era)

There are times where we get a clear before-and-after moment that demands a reevaluation of our most basic assumptions. This month, [OpenAI announced custom GPTs](https://openai.com/blog/introducing-gpts), a no-code tool for people to create their own Generative Pre-trained Transformer (GPT) models based on their own data and using their own plug-ins. What used to be a tight mandate for a team inside a large R&D group or a chatbot startup can now be accomplished by my grandfather in five minutes while using a couple of wiki links as a knowledge base. Security leaders need to recognize that artificial intelligence (AI) tools are not something that is coming in the nebulous future; they are here.

More importantly, these GPTs can act on the user's behalf. [OpenAI's tight integration with Zapier](https://zapier.com/blog/gpt-assistant/) means thousands of connectors are at your disposal, letting the AI query your CRM, update your ERP, or monitor your servers with a few clicks. How does the AI authenticate to all these services, you might ask? Great question, but more on that later.

Another thought you might have is, well, this is amazing and all, but we will never allow this to happen in our highly regulated security-focused enterprise. You might have even blocked ChatGPT on the network level long ago and are now constantly monitoring for more bots to add to that deny list — which is annoying, but you can manage.

Enter Microsoft. Last week at its Ignite conference, [Microsoft announced Copilot Studio](https://www.microsoft.com/en-us/microsoft-365/blog/2023/11/15/introducing-microsoft-copilot-studio-and-new-features-in-copilot-for-microsoft-365/), its own no-code GPT creator. It has everything the OpenAI tool has, from uploading files to use as a knowledge base to a chat interface for configuration and click-to-add integrations called plug-ins. Copilot Studio allows users to integrate their Copilots with Microsoft 365, Azure SaaS, and hundreds of other enterprise systems. This integration is done via user impersonation, meaning the Copilot acts on behalf of users.

Here's the thing about these Microsoft-generated user impersonation bots: You can't block them. You have no way to distinguish between an AI-generated operation and a user-triggered operation because they look exactly alike in the logs. Copilots are hosted as applications inside your M365 environment, so forget about network-level blocks. Users log into these Copilots with their corporate credentials. The bottom line is that while GPTs live in the consumer world, Copilots live in the enterprise world.

## How Did This Happen So Quickly?

Well, it didn't. Microsoft and other major vendors — such as Salesforce, UiPath, and ServiceNow — have been building low-code/no-code platforms that [lowered the bar to building enterprise applications](https://www.darkreading.com/cyber-risk/you-can-t-opt-out-of-citizen-development) for years now. These companies have been building out hundreds of integrations, visual builders, automated production deployments, and [credential-sharing-as-a-service](https://www.darkreading.com/cyber-risk/credential-sharing-as-a-service-hidden-risk-of-low-code-no-code).

Chatbots are the killer app for low-code/no-code platforms. Who needs to code when you can leverage a platform that out of the box gives you everything you need to create, share, monitor, upgrade, and embed your bot within minutes inside the enterprise, directly on top of business data?

A crucial point here is just how easy it now is to build no-code apps. In recent years, professional developers and business users alike have used platforms, like the Power Platform, to build millions of new business applications, including some that handle sensitive data and facilitate business-critical processes. While some companies have started to [centralize the GenAI apps](https://www.darkreading.com/application-security/security-must-empower-ai-developers-now) being created by the engineering teams, this won't be enough. Security teams have to look at what business users are building as well. In fact, the sheer number of business users, combined with the ease of creating bots, suggests that security teams should, in fact, focus more on what business users are building.

## Where Do We Even Begin?

Luckily, a growing number of organizations have already integrated citizen development (business users building apps) into their application security programs, and some of their insights have been [publicly](https://www.youtube.com/watch?v=nHDUVzrpZEk&t=23971s)[shared](https://www.zenity.io/securing-my-lcnc-where-to-start/). [Industry standards](https://owasp.org/www-project-top-10-low-code-no-code-security-risks/) that categorize, explain, and suggest remediation for security risks of low-code/no-code apps have emerged.

Not using code doesn't mean no vulnerabilities, especially logical ones. However, it typically does mean the [lack of a software development life cycle (SDLC)](https://www.darkreading.com/cyber-risk/where-there-s-no-code-there-s-no-sdlc), [visibility](https://www.zenity.io/unlocking-supply-chain-transparency-for-low-code-no-code-apps-with-sbom/), and controls. Whether our users are creating a GPT or a Copilot, they are doing so today and in large quantities. For security leaders, it's either get on board now and bring these new developers under the security umbrella — or miss the train and hope for the best.

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyber-risk/enterprise-generative-ai-enters-its-citizen-development-era)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyber-risk/enterprise-generative-ai-enters-its-citizen-development-era)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyber-risk/enterprise-generative-ai-enters-its-citizen-development-era)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyber-risk/enterprise-generative-ai-enters-its-citizen-development-era&title=Enterprise%20Generative%20AI%20Enters%20Its%20Citizen%20Development%20Era)[Email](mailto:?subject=Enterprise%20Generative%20AI%20Enters%20Its%20Citizen%20Development%20Era&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Enterprise%20Generative%20AI%20Enters%20Its%20Citizen%20Development%20Era%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyber-risk%2Fenterprise-generative-ai-enters-its-citizen-development-era)

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
