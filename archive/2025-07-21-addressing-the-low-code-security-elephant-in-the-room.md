---
date: '2025-07-21'
description: The article addresses the critical security implications of low-code/no-code
  applications, emphasizing that security is a shared responsibility among all stakeholders.
  It delineates four operational layers—infrastructure, runtime, application, and
  data—each requiring distinct security considerations. As users can launch applications
  without deep technical knowledge, the risk of vulnerabilities increases. Emphasizing
  a proactive security governance approach is essential, especially regarding third-party
  components and the integration of these applications with existing cloud and on-premises
  systems. Organizations must ensure comprehensive visibility and adherence to security
  best practices to mitigate potential risks.
link: https://www.darkreading.com/edge-articles/addressing-the-low-code-security-elephant-in-the-room
tags:
- cloud security
- application security
- software development security
- shared responsibility model
- low-code security
title: Addressing the Low-Code Security Elephant in the Room
---

- [Cyber Risk](https://www.darkreading.com/cyber-risk)

[![The Edge Logo](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt530eb1f4e672eb44/653a71690e92cc040a3e9d6d/Dark_Reading_Logo_TheEdge_0.png?width=700&auto=webp&quality=80&disable=upscale)\\
\\
Cybersecurity In-Depth: Feature articles on security strategy, latest trends, and people to know.](https://www.darkreading.com/program/the-edge)

# Addressing the Low-Code Security Elephant in the Room

The danger of anyone being able to spin up new applications is that few are thinking about security. Here's why everyone is responsible for the security of low-code/no-code applications.

[![Picture of Michael Bargury](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltbd8a249d11a28466/64f150aad5f7ca2f7665bf81/Michael_Bargury_zenity.jpg?width=100&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/author/michael-bargury)

[Michael Bargury](https://www.darkreading.com/author/michael-bargury), CTO & Co-Founder, Zenity

November 18, 2021

8 Min Read

![Multi-colored blocks of different shapes put together to create a wall.](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt8b402bceebefbeb5/64f151e70b661a6928407866/buildingblocks-radachynskyi-adobe.jpg?width=1280&auto=webp&quality=80&format=jpg&disable=upscale)

Source: Radachynskyi via Adobe Stock

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyber-risk/addressing-the-low-code-security-elephant-in-the-room)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyber-risk/addressing-the-low-code-security-elephant-in-the-room)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyber-risk/addressing-the-low-code-security-elephant-in-the-room)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyber-risk/addressing-the-low-code-security-elephant-in-the-room&title=Addressing%20the%20Low-Code%20Security%20Elephant%20in%20the%20Room)[Email](mailto:?subject=Addressing%20the%20Low-Code%20Security%20Elephant%20in%20the%20Room&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Addressing%20the%20Low-Code%20Security%20Elephant%20in%20the%20Room%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyber-risk%2Faddressing-the-low-code-security-elephant-in-the-room)

With all the hype around low-code/no-code platforms, many are now touting the benefits of adopting low-code/no-code development. Let’s address the (security) elephant in the room: Anyone can spin up applications using these tools, but who is responsible for the security of these applications?

If, similar to cloud computing, it is a shared-responsibility model, then where do we draw the lines of responsibility among the different parties involved?

One Size Does Not Fit All

Low-code applications are diverse: They come in different forms, vary in how they are deployed, and solve a broad range of problems. When discussing the security responsibility model for low-code applications, we have to first understand the different layers of a low-code application. Here is a brief summary:

- Layer 1: The infrastructure on which the low-code application is running on, which includes the servers running the operating system, the network in which the servers are deployed, the underlying operating system(s), and virtualization layers, containers, and container orchestration being used.

- Layer 2: The runtime environment used for running the low-code application.

- Layer 3: The application itself, which includes the business logic of the application; any widgets, components, and connectors provided by the low-code platform; custom widgets/components created by the app owner’s organization; third-party widgets, components, and connectors, such as those available through the different public marketplaces; any ancillary services being used by the low-code application, such as public cloud services (e.g., storage buckets, message queues, IoT devices) and SaaS instances (e.g., Salesforce, ServiceNow, Slack); and identity and access management tools being used.

- Layer 4: The data being used by the application. Data can be stored in different locations — sometimes in the cloud and sometimes on-premise.


We can also consider the low-code platform development environment used to develop the application as Layer 0. Even if you do everything necessary to rigorously secure your application, if a malicious user gets access to your development console — that’s just as bad.

Security Is a Shared Responsibility

Cloud computing’s approach to the shared-responsibility model is straightforward: As you advance in your cloud journey and adopt higher levels of abstraction, the security responsibility shifts away from you and toward the cloud provider.

![Responsibility for security is split between cloud providers and application owners.](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltacac6cf773912de8/64f152d5e8ab153cf61fb14a/SharedModelEvolution-Zenity.jpg/?width=700&auto=webp&quality=80&disable=upscale)

The Shared Responsibility Model as it evolves in cloud computing. Grey boxes reflect the application owner's responsibility. (Source: Zenity)

Should we consider low-code/no-code applications as yet another step in this evolution?

It depends. Where the responsibility lies depends on the choices you make when adopting low-code development. For example, with the infrastructure layer, are you planning on hosting your application in a private cloud or a public data center? Some low-code/no-code platforms are designed specifically for on-premises or hybrid cloud/on-premises deployments. If you decide to host your own applications, you will have full control over the underlying infrastructure, but that also means you are responsible for securing every aspect of the environment.

Application-Layer Choices

What are some development choices about the application layer that affect the security responsibility?

If the low-code application is strictly made up of low-code platform native capabilities or services, you only have to worry about the basics. That includes application design and business logic flaws, securing your data in transit and at rest, security misconfigurations, authentication, authorizing and adhering to the principle of least-privilege, providing security training for your citizen developers, and maintaining a secure deployment environment. These are the same elements any developer — low-code or traditional — would need to think about in order to secure the application. Everything else is handled by the low-code platform itself.

That is as basic as it gets.

But what if you are making use of additional widgets, components, or connectors provided by the low-code platform? Those components — and the code used to build them — are definitely out of your jurisdiction of responsibility. You may need to consider how they are configured or used in your application, though. It’s possible that an incorrectly used component may lead to a potential vulnerability in your application.

For example, most low-code platforms provide a SQL database connector, which enables low-code app developers to run SQL queries to access the data stored in the databases. In some common SQL connectors that we looked at, we saw several methods for interacting with databases: Some provided strict security and allowed less flexibility to developers, while others were more flexible. If used incorrectly, those connectors with flexible methods could lead to a disastrous SQL injection (SQLi) vulnerability. For example, a successful SQLi attack against a low-code application can result in unauthorized access to the data. The attacker may be able to manipulate the data or even execute shell commands on the database server.

The third choice is to extend the components library with custom components because the low-code/no-code platform of choice does not provide all the needed (or desired) functionality. For example, you may create Mendix custom widgets to create dynamic menus in your application, Appian custom plug-in components to render a Google Maps object, or Canvas Apps in Microsoft Power Apps to integrate data from other Microsoft applications.

While custom built components provide extensibility and the freedom to create functionality as you see fit, they also introduce more code and logic to your application. Just like with traditionally developed software, more code and logic means a greater chance of introducing defects, design flaws, and security vulnerabilities. When developing custom components, even in the low-code/no-code world, make sure you have the proper SDLC and security processes in place. Developers should follow your organization’s security policy and guidelines for developing and deploying applications.

Finally, you may have to rely on third-party components because the functionality you are looking for does not exist as a native service or is offered as an add-on component by your low-code platform. In this case, you will be responsible for vetting and choosing third-party components based on several factors:

1. Is the source code available for review?

2. How often is the component updated?

3. Does the component come from a reputable author or organization?

4. Is the component connected to a third-party service, and, if so, is it secure?

5. Does the low-code platform provider perform any kind of security validation on components in the marketplace?


Similar to vetting third-party open source packages, you must have a process in place to make sure you are not turning these components into the weakest link of your application security chain.

Choosing Between the Cloud and On-Premises

It’s quite common to integrate low-code applications with existing public cloud accounts in order to consume public cloud services, such as storage buckets, message queues, databases, and so forth. If that is the case, you have to add cloud security as an additional factor to the overall security posture of your application. You should make sure you are adopting a mature cloud security posture management approach.

Many low-code/no-code platforms offer connectivity to on-premises data and applications. As an example, organizations that use the Microsoft Power Apps low-code platform have the option to use an on-premises data gateway, which acts as a bridge to provide quick and secure data transfer between on-premises data (data not in the cloud) and several Microsoft cloud services. Another example is when using the Appian low-code platform with robotic process automation (RPA), which supports a hybrid cloud/on-premises deployment model.

When creating a bridge between the cloud and your organization’s on-premises infrastructure, data, and applications, you are essentially opening up your private assets to access from the public Internet. Needless to say, in such cases security and privacy should be top-of-mind, and access should be as restricted as possible — encrypted and monitored at all times.

Who Is Responsible? The Verdict

Given all the different options for low-code application development, there’s really no simple answer. Neither is there a straight line we can draw in some low-code stack security chart that would be clear-cut. Low-code/no-code is a paradigm shift in the way software is developed, from monolithic, to microservices, and now — low-code/no-code. It should not be viewed as a way to abstract away hardware and deployment models as part of the next phase in the evolution of cloud computing.

The bottom line is that low-code/no-code applications are another form of software. It is inevitable they will contain bugs, design flaws, vulnerabilities, and misconfigurations that will introduce risk. Even if you are giving away some of the control and responsibility to a low-code/no-code platform provider or other supplier, you are still the owner of your application and its data. You remain responsible for making sure the applications are secure and adhere to your corporate security policies and standards.

Regardless of how much abstraction you use, and how much control you are giving up, always keep in mind the following two aspects: know your apps, and secure your business logic. You need to fully understand how your low-code applications are developed, deployed and maintained. Always make sure you have full visibility to your low-code applications, and address any security concerns raised here. And regardless of how your application is developed, you should always make sure that you applied secure design, development and application security best practices. A simple flaw in business logic can make the most resilient application vulnerable.

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyber-risk/addressing-the-low-code-security-elephant-in-the-room)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyber-risk/addressing-the-low-code-security-elephant-in-the-room)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyber-risk/addressing-the-low-code-security-elephant-in-the-room)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyber-risk/addressing-the-low-code-security-elephant-in-the-room&title=Addressing%20the%20Low-Code%20Security%20Elephant%20in%20the%20Room)[Email](mailto:?subject=Addressing%20the%20Low-Code%20Security%20Elephant%20in%20the%20Room&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Addressing%20the%20Low-Code%20Security%20Elephant%20in%20the%20Room%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyber-risk%2Faddressing-the-low-code-security-elephant-in-the-room)

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
