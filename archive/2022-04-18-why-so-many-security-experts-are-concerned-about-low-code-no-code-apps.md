---
date: 2022-04-18
description: Recent concerns about low-code/no-code applications highlight significant
  security vulnerabilities in enterprise environments. Key issues include the lack
  of governance regarding data access (32%), trust in platform security (26%), inadequate
  application security knowledge (26%), and poor visibility into created applications
  (25%). IT security teams struggle with manual processes for monitoring and protecting
  these tools, which are often developed outside their purview. As enterprises adopt
  these platforms, an urgent need arises for tailored security solutions that align
  with low-code/no-code architectures, emphasizing the necessity for robust governance
  and proactive security measures.
link: https://www.darkreading.com/dr-tech/why-so-many-security-experts-are-concerned-about-low-code-no-code-apps
tags:
- Low-Code Applications
- Application Security
- No-Code Applications
- Cybersecurity Risks
- Data Governance
title: Why So Many Security Experts Are Concerned About Low-Code/No-Code Apps
---

- [Cyber Risk](https://www.darkreading.com/cyber-risk)

[![DR Technology Logo](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt4c091cd3ac9935ea/653a71456ad0f6040a6f71bd/Dark_Reading_Logo_Technology_0.png?width=700&auto=webp&quality=80&disable=upscale)\\
\\
News, news analysis, and commentary on the latest trends in cybersecurity technology.](https://www.darkreading.com/program/dr-technology)

# Why So Many Security Experts Are Concerned About Low-Code/No-Code Apps

IT departments must account for the business impact and security risks such applications introduce.

[![Picture of Michael Bargury](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltbd8a249d11a28466/64f150aad5f7ca2f7665bf81/Michael_Bargury_zenity.jpg?width=100&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/author/michael-bargury)

[Michael Bargury](https://www.darkreading.com/author/michael-bargury), CTO & Co-Founder, Zenity

April 18, 2022

7 Min Read

![Visualization of low-code/no-code development, with a human hand touching a screen and generating a stream of app logos](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blta11753225eddf0ba/64f1098747a6e39c1de3438f/Low-code_maxsattana_iStock_47622152_LARGE.png?width=1280&auto=webp&quality=80&format=jpg&disable=upscale)

Source: maxsattana via iStock

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyber-risk/why-so-many-security-experts-are-concerned-about-low-code-no-code-apps)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyber-risk/why-so-many-security-experts-are-concerned-about-low-code-no-code-apps)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyber-risk/why-so-many-security-experts-are-concerned-about-low-code-no-code-apps)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyber-risk/why-so-many-security-experts-are-concerned-about-low-code-no-code-apps&title=Why%20So%20Many%20Security%20Experts%20Are%20Concerned%20About%20Low-Code%2FNo-Code%20Apps)[Email](mailto:?subject=Why%20So%20Many%20Security%20Experts%20Are%20Concerned%20About%20Low-Code/No-Code%20Apps&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Why%20So%20Many%20Security%20Experts%20Are%20Concerned%20About%20Low-Code%2FNo-Code%20Apps%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyber-risk%2Fwhy-so-many-security-experts-are-concerned-about-low-code-no-code-apps)

Last month, Dark Reading released an [enterprise application security survey](https://www.informationweek.com/whitepaper/cybersecurity/cloud-security/how-enterprises-are-securing-the-application-environment/437083?gset=yes&_sp=74170523-4e1c-48d8-80b0-b05f6918b6f0.1650040431642&_ga=2.77744852.1325979760.1649694450-2130966764.1641840616) that raised serious concerns by IT and security teams about the state of low-code/no-code applications. The survey exposed a deep lack of visibility, control, and knowledge necessary to maintain the level of security maturity expected in the enterprise. Here we will look at concrete concerns raised by the survey, examine their root causes, and offer recommendations on ways to address them today.

The following concerns were raised under the question, "[What security concerns do you have regarding low-code/no-code applications?](https://www.darkreading.com/cyberattacks-data-breaches/low-code-no-code-tools-are-popular-but-untrusted)"

Concern No. 1: Governance

According to 32% of respondents, "There is no governance over how these applications are accessing and using our data."

Indeed, many useful low-code/no-code applications rely on storing data either in managed storage provided by the platform or in another platform via a connector. The tricky part is that low-code/no-code platforms make it extremely easy for makers to essentially bake their identity into the applications, so that every application user ends up triggering operations on behalf of the maker. Within enterprise environments, it is not uncommon for useful business applications to store their data in the maker's Dropbox or OneDrive account. Baked-in accounts can become an even bigger issue when an honest mistake causes data to be stored in a personal rather than business account.

Another popular use of low-code/no-code are data-movers or operation-stitchers. They connect source and destination, either by moving data between multiple points or by linking together an operation in one system to another in a different system.

As an example, a popular automation flow in enterprise scenarios is email forwarding. Users build an application that monitors their professional inbox for new emails, copies their content, and pastes it in their personal email for various reasons. Note that by copying the data, users are easily able to [bypass DLP controls](https://www.zenity.io/blog/low-code-security-and-business-email-compromise-via-email-auto-forwarding/) that would have prevented email forwarding.

Concern No. 2: Trust

According to 26% of respondents, "I don't trust the platforms used to create the applications."

Low-code/no-code platform vendors are increasingly directing their attention to provide strong security assurance for their platforms, but there is a long way to go. While enterprise customers have become used to the security benefits provided by public cloud vendors, with their mature security teams, vulnerability disclosure programs, and state-of-the-art SOCs, low-code/no-code platforms are just getting used to the fact that they are now business-critical systems.

Of course, vendors investing in the security of their platform is not enough. Customers have to hold their part of the [shared responsibility model](https://www.darkreading.com/cyber-risk/addressing-the-low-code-security-elephant-in-the-room), too. While platform vendors are improving their security posture, enterprises using low-code/no-code platforms must figure out how to approach these applications with the same level of security vigor as they would their pro-code applications. After all, the impact of both types of applications on data, identity, and the enterprise as a whole is the same.

Take security testing, for example. To catch security issues early, pro-code applications are typically built with code and configuration scanning tools in place, as part of the CI/CD. There are a host of tools to help detect issues throughout the SDLC, including SAST, DAST, and SCA, which has become very popular in recent years with the rise in open source security issues. Low-code/no-code applications are prone to the same problems that these tools detect, such as injection-based attacks, security misconfiguration, and untrusted dependencies. However, these applications typically rely on manual processes for security assurance or try to use pro-code tools to scan artifacts generated with low-code; unfortunately, pro-code tools fail to understand the business logic of low-code/no-code applications and therefore provide little value.

Concern No. 3: AppSec

According to 26% of respondents, "I don't know how to check for security vulnerabilities in these applications."

How do I make sure my code makes sense, and that it is secure and robust, without access to that code? This point is tricky, and new solutions are required to tackle it.

When public cloud providers started introducing the concept of platform-as-a-service for compute services such as managed virtual machines (VMs), managed Kubernetes clusters, or serverless functions, the same kind of concerns were raised. Our entire strategy, as a security community, to secure compute instances was based on our ability to observe and leverage the host machine running our applications. While stripping away the complexities of managing VMs, cloud providers also stripped away the ability of security teams to observe and protect them. As a result, novel solutions had to be introduced to provide the same level of security assurance with cloud-native building blocks.

The same approach is desperately needed in low-code/no-code applications. Instead of trying to apply existing tools like code scanning or web security monitoring to artifacts generated by low-code/no-code, security teams should adopt solutions that understand the language of low-code/no-code in order to [identify logical vulnerabilities in those applications](https://owasp.org/www-project-top-10-low-code-no-code-security-risks/).

Concern No. 4: Visibility

According to 25% of respondents, "The security team doesn't know what applications are being created."

This point is particularly important because you can't protect what you can't see. Most low-code/no-code platforms have little to no capabilities for allowing admins to view applications built on these platforms. Basic questions like, "How many applications do we have?" are simply unanswerable without pervasive measures. For example, some platforms allow admins to make themselves the owners of every application separately but do not allow them to see the application otherwise. So admins must resort to an active change on the platform to take a look at the application.

Other platforms go even further, allowing business users to create applications in a private folder that administrators cannot review, other than knowing the number of applications that exist in them. A maker could be exfiltrating data through a private application, and the admin is left with no way to even know anything besides the fact that the application exists.

Visibility becomes even trickier once companies realize that they are using more than one low-code/no-code platform. In fact, most large enterprises are already using multiple platforms. With low-code/no-code platforms becoming more popular, citizen development tools being introduced bottom-up, and software-as-a-service (SaaS) vendors becoming platforms themselves, it's clear why enterprises are suddenly finding themselves using several different platforms.

Concern No. 5: Knowledge and Awareness

According to 33% of respondents, "I don't have any security concerns," "Other," or "Don't know."

Since low-code/no-code platforms often find their way into the enterprise through business units rather than top-down through IT, they can easily slip through the cracks and be missed by security and IT teams. While security teams are in most cases part of the procurement process, it's easy to treat a low-code/no-code platform as just another SaaS application used by the business, not realizing that the result of adopting this platform would be empowering a whole array of new citizen-developers in the business.

In one large organization, citizen-developers in the finance team built an expense management application to replace a manual process filled with back-and-forth emails. Employees quickly adopted the application since it made it easier for them to get reimbursed. The finance team was happy because it automated part of its repetitive work. But IT and security were not in the loop. It took some time for them to notice the application, understand that it was built outside of IT, and reach out to the finance team to bring the app under the IT umbrella.

Security and IT teams are always in a state where the backlog of concerns is much larger than their ability to invest. To make sure resources are allocated to the most critical security risks, teams must first be aware of the criticality of low-code/no-code applications to the business and the security risks that they introduce. For the former, this means that low-code/no-code applications' impact on the enterprise must be demonstrated and clear. Security teams must be part of the discussion when thinking about adopting citizen development.

For the latter, we as a community have to research, categorize, and share concrete security risks we identify to help others to build more secure applications. Bringing IT and security into the low-code/no-code conversation would allow the adoption of these technologies to accelerate, unleashing their full potential to increase business velocity and productivity.

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyber-risk/why-so-many-security-experts-are-concerned-about-low-code-no-code-apps)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyber-risk/why-so-many-security-experts-are-concerned-about-low-code-no-code-apps)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyber-risk/why-so-many-security-experts-are-concerned-about-low-code-no-code-apps)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyber-risk/why-so-many-security-experts-are-concerned-about-low-code-no-code-apps&title=Why%20So%20Many%20Security%20Experts%20Are%20Concerned%20About%20Low-Code%2FNo-Code%20Apps)[Email](mailto:?subject=Why%20So%20Many%20Security%20Experts%20Are%20Concerned%20About%20Low-Code/No-Code%20Apps&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Why%20So%20Many%20Security%20Experts%20Are%20Concerned%20About%20Low-Code%2FNo-Code%20Apps%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyber-risk%2Fwhy-so-many-security-experts-are-concerned-about-low-code-no-code-apps)

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

Latest Articles in DR Technology

- [AI Driving the Adoption of Confidential Computing](https://www.darkreading.com/cyber-risk/ai-driving-adoption-confidential-computing) Jul 16, 2025
\|

4 Min Read

- [Cognida.ai Launches Codien: An AI Agent to Modernize Legacy Test Automation and Fast-Track Test Creation](https://www.darkreading.com/application-security/cognida-ai-launches-codien) Jul 16, 2025
\|

3 Min Read

- [MITRE Launches AADAPT Framework for Financial Systems](https://www.darkreading.com/vulnerabilities-threats/mitre-aadapt-framework-financial-systems) Jul 15, 2025
\|

1 Min Read

- [Digital Fingerprints Test Privacy Concerns in 2025](https://www.darkreading.com/data-privacy/digital-fingerprints-tests-privacy-concerns-2025) Jul 10, 2025
\|

4 Min Read


[Read More DR Technology](https://www.darkreading.com/program/dr-technology)

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
