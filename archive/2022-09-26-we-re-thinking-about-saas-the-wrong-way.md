---
date: 2022-09-26
description: Michael Bargury argues that the traditional separation of SaaS and public
  cloud security hinders effective risk management as low-code SaaS platforms evolve
  into business-centric application development solutions. With business users increasingly
  acting as developers, applications built on these platforms require the same rigorous
  security measures applied to cloud-hosted applications. This shift necessitates
  a reevaluation of security strategies to include the myriad applications stemming
  from enterprise SaaS, which currently lack adequate visibility and governance, thus
  exposing organizations to heightened cyber risks.
link: https://www.darkreading.com/edge-articles/we-re-thinking-about-saas-the-wrong-way
tags:
- Cyber Risk Management
- Cloud Computing
- Application Development
- SaaS Security
- Low Code
title: We're Thinking About SaaS the Wrong Way
---

- [Cyber Risk](https://www.darkreading.com/cyber-risk)

[![The Edge Logo](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt530eb1f4e672eb44/653a71690e92cc040a3e9d6d/Dark_Reading_Logo_TheEdge_0.png?width=700&auto=webp&quality=80&disable=upscale)\\
\\
Cybersecurity In-Depth: Feature articles on security strategy, latest trends, and people to know.](https://www.darkreading.com/program/the-edge)

# We're Thinking About SaaS the Wrong Way

Many enterprise applications are built outside of IT, but we still treat the platforms they're built with as point solutions.

[![Picture of Michael Bargury](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltbd8a249d11a28466/64f150aad5f7ca2f7665bf81/Michael_Bargury_zenity.jpg?width=100&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/author/michael-bargury)

[Michael Bargury](https://www.darkreading.com/author/michael-bargury), CTO & Co-Founder, Zenity

September 26, 2022

6 Min Read

![Businessman reaches out to touch Low Code button on a screen full of icons](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltf3dd13eae8ac4e0b/64f161946ec0b12a4f30f592/lowcode-photon_photo-AdobeStock.jpeg?width=1280&auto=webp&quality=80&format=jpg&disable=upscale)

Source: photon\_photo via Adobe Stock

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyber-risk/we-re-thinking-about-saas-the-wrong-way)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyber-risk/we-re-thinking-about-saas-the-wrong-way)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyber-risk/we-re-thinking-about-saas-the-wrong-way)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyber-risk/we-re-thinking-about-saas-the-wrong-way&title=We%27re%20Thinking%20About%20SaaS%20the%20Wrong%20Way)[Email](mailto:?subject=We%27re%20Thinking%20About%20SaaS%20the%20Wrong%20Way&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20We%27re%20Thinking%20About%20SaaS%20the%20Wrong%20Way%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyber-risk%2Fwe-re-thinking-about-saas-the-wrong-way)

We're used to thinking about securing software-as-a-service (SaaS) platforms and the cloud as two separate beasts. This separation stems from the way SaaS and the public cloud first emerged as small point solutions and an extension of the traditional data center, respectively. Today, due to the advent of low code, this separation is wrong, and it's holding us back from seeing what's right in front of our eyes. Low code makes SaaS platforms a part of the public cloud, a place where developers build multiple applications rather than consuming a single one: a cloud platform.

Failing to shift our mindset leads to where we are today, with those applications being left up for grabs with no security visibility. And to make matters worse, low-code applications are embedded right into platforms like Salesforce and Microsoft Dynamics, which we all use and that hold our most sensitive business data.

## How Did We Get Here?

Origin stories are always interesting because they explain something fundamental about the way we perceive the hero of the story. While SaaS started as an extension of the corporate network, the public cloud started as an extension of the data center. Those very different starting points explain why securing SaaS started with shadow IT (protecting the perimeter) and securing the public cloud started with workload protection (lift-and-shift servers and their network/host agents). This also meant that different security teams were tasked with securing SaaS and the cloud, which of course led to a separation of tools, different threat modeling, and, most importantly, the formation of different security mindsets.

Both SaaS and the public cloud have drastically evolved from those early days. Public cloud vendors introduced ever more granular compute paradigms, gradually introducing infrastructure as a service (IaaS), platform as a service (PaaS), and serverless to help developers focus on the business problem at hand. They also built an entire ecosystem of ready-made solutions for complex yet common problems — identity, permissions, logging, configuration, and deployment, to name a few.

SaaS used to mean a point solution for a specific problem. Salesforce started as a CRM, ServiceNow as a ticketing system, and Office365 as email, spreadsheets, docs, and slides. (While this is more than one solution, these are very specific ones.) Contrast that with today: Salesforce Developers are building apps for [just about any business need](https://www.salesforce.com/products/platform/app-gallery/) on top of the Salesforce Platform, ServiceNow low-code apps are [handling just about anything](https://www.servicenow.com/customers.html#filterTag1=servicenow%3Aproducts-and-solutions%2Fservicenow-platform) from HR to health and finance processes, and Power Platform, Microsoft's low-code platform embedded into Office365, is being used by more than [20 million users](https://news.microsoft.com/wp-content/uploads/prod/2022/07/07192022_Inspire_Satya_Nadella.pdf) across the industry [to solve every business need](https://powerapps.microsoft.com/en-us/blog/power-platform-stories/), from productivity through procurement and COVID-related processes.

Clearly, these have become enterprise-grade application development platforms, not point solutions to specific business problems. Many developers today choose to build their applications on platform-provided abstractions, whether those are serverless functions on the public cloud or extendable building blocks on SaaS low-code platforms.

## The Introduction of Business Developers

Comparing how SaaS platforms started and where they are now clearly shows how far these have come from their earlier versions. But there's still a major shift we haven't mentioned yet: the introduction of business developers.

SaaS low-code platforms draw their power from the data they maintain and their existing users. Those are both not limited to IT but rather skew heavily toward the business. Having access to both business data and business users means that SaaS is in the perfect position to tackle the most pressing issue many enterprises face today — digital transformation.

With a global shortage of developers and the difficulty of streamlining a business process with so many stakeholders, low-code platforms introduce a shortcut, letting the business users streamline their processes themselves without waiting for IT.

Low code is taking off with business users, so much so that in his 2019 Inspire keynote, Microsoft CEO Satya Nadella [discussed the opportunity](https://qz.com/1740052/microsoft-shares-plan-to-make-anyone-a-software-developer/) of low code to empower people and to create new white-collar jobs just like Excel did.

Just like the public cloud is an application development platform enabling developers to focus on their business logic, SaaS platforms have become application development platforms using low code to empower business users to become developers and address any business need.

SaaS is now focused on new types of developers addressing a whole range of unmet business needs with dedicated applications, creating a new type of cloud: the business cloud.

## Securing Low Code as an Extension of Cloud

With the realization that some SaaS platforms are now application development platforms and an extension of the cloud, we should re-examine the [responsibilities](https://www.darkreading.com/cyber-risk/addressing-the-low-code-security-elephant-in-the-room) for securing those applications and bringing them under the security team's umbrella.

We should treat platforms like Salesforce, ServiceNow, and Office365 the same way we treat AWS, Azure, and GCP, where we focus on the applications that were built and are hosted in these application development platforms rather than treating the whole platform as a single application.

Shadow IT, for example, remains an issue with smaller and an ever-growing number of point-solution SaaS. But it doesn't make sense to treat any single platform mentioned above as a single app to discover and catalog. Instead, we should discover and catalog the applications built with those platforms — and there are tens of thousands of those. In most organizations, this enormous complexity is hidden behind a single line in an application inventory.

Applications built with SaaS low-code platforms should be [examined](https://owasp.org/www-project-top-10-low-code-no-code-security-risks/) with the same security rigor we use for those built on the cloud because, at the end of the day, an application is an application, no matter where it was built and hosted.

What does matter for the security of our business applications is the people, process, and tools that are involved in making, maintaining, and protecting those applications. For applications built in the cloud, we have professional developers, automated CI/CD processes, and various security tools from code scanning and dynamic analysis through runtime monitoring and prevention. For applications built on SaaS low-code platforms, we have some professional developers but also business users who are [not security-savvy](https://www.darkreading.com/cyber-risk/3-ways-no-code-developers-can-shoot-themselves-in-the-foot), with [few to no deployment processes](https://www.zenity.io/blog/low-code-sdlc-build-fast-stay-secure/) and no security controls or guarantees.

Thinking about low-code platforms as part of SaaS makes it difficult for us to see that a [huge](https://www.techrepublic.com/article/report-60-of-apps-are-built-outside-of-it-and-thats-a-good-thing/)[portion](https://www.gartner.com/en/newsroom/press-releases/2021-11-10-gartner-says-cloud-will-be-the-centerpiece-of-new-digital-experiences) of our business applications are now being built by the business, outside of IT and outside of security control. To begin seeing the problem and figuring out our approach to it, we must shift our mindset to acknowledge low-code platforms as a part of the cloud and treat the applications on those platforms like we do any other application.

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyber-risk/we-re-thinking-about-saas-the-wrong-way)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyber-risk/we-re-thinking-about-saas-the-wrong-way)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyber-risk/we-re-thinking-about-saas-the-wrong-way)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyber-risk/we-re-thinking-about-saas-the-wrong-way&title=We%27re%20Thinking%20About%20SaaS%20the%20Wrong%20Way)[Email](mailto:?subject=We%27re%20Thinking%20About%20SaaS%20the%20Wrong%20Way&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20We%27re%20Thinking%20About%20SaaS%20the%20Wrong%20Way%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyber-risk%2Fwe-re-thinking-about-saas-the-wrong-way)

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
