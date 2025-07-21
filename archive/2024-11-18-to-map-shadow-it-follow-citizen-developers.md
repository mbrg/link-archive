---
date: 2024-11-18
description: In "To Map Shadow IT, Follow Citizen Developers," Michael Bargury discusses
  the pervasive issue of shadow IT, where employees use unauthorized tools to meet
  business needs. He emphasizes the dual role of citizen development—allowing users
  to create apps with low-code/no-code platforms while exposing potential security
  risks. By tracing user-built applications and their integrations with existing systems,
  organizations can better understand their shadow IT landscape. This approach fosters
  a proactive stance in governance, balancing efficiency with security, albeit requiring
  careful risk management to mitigate vulnerabilities.
link: https://www.darkreading.com/cyber-risk/to-map-shadow-it-follow-citizen-developers
tags:
- SaaS Security
- Low-Code Development
- Cybersecurity
- Shadow IT
- Citizen Development
title: To Map Shadow IT, Follow Citizen Developers
---

- [Cyber Risk](https://www.darkreading.com/cyber-risk)
- [Insider Threats](https://www.darkreading.com/vulnerabilities-threats/insider-threats)

[![The Edge Logo](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt530eb1f4e672eb44/653a71690e92cc040a3e9d6d/Dark_Reading_Logo_TheEdge_0.png?width=700&auto=webp&quality=80&disable=upscale)\\
\\
Cybersecurity In-Depth: Feature articles on security strategy, latest trends, and people to know.](https://www.darkreading.com/program/the-edge)

# To Map Shadow IT, Follow Citizen Developers

The tangle of user-built tools is formidable to manage, but it can lead to a greater understanding of real-world business needs.

[![Picture of Michael Bargury](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltbd8a249d11a28466/64f150aad5f7ca2f7665bf81/Michael_Bargury_zenity.jpg?width=100&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/author/michael-bargury)

[Michael Bargury](https://www.darkreading.com/author/michael-bargury), CTO & Co-Founder, Zenity

November 18, 2024

4 Min Read

![Shadow of hot-air balloon over the Namib desert. Namib-Naukluft Park, Namibia](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt5de5c92bd6a90dcd/673682a6897306f6b9292ba6/balloonshadow-Martin_Harvey-alamy.jpg?width=1280&auto=webp&quality=80&format=jpg&disable=upscale)

Source: Martin Harvey via Alamy Stock Photo

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyber-risk/to-map-shadow-it-follow-citizen-developers)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyber-risk/to-map-shadow-it-follow-citizen-developers)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyber-risk/to-map-shadow-it-follow-citizen-developers)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyber-risk/to-map-shadow-it-follow-citizen-developers&title=To%20Map%20Shadow%20IT%2C%20Follow%20Citizen%20Developers)[Email](mailto:?subject=To%20Map%20Shadow%20IT,%20Follow%20Citizen%20Developers&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20To%20Map%20Shadow%20IT%2C%20Follow%20Citizen%20Developers%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyber-risk%2Fto-map-shadow-it-follow-citizen-developers)

COMMENTARY

Shadow IT is what your business runs on while waiting for IT to provide an enterprise solution. It's your sales team buying licenses to an obscure software-as-a-service (SaaS) because it helps them get the job done. Or it's your finance team using an unapproved tool because the approved one is too clunky. Sometimes shadow IT exists specifically to bypass an overly annoying security mechanism — figuring out a way to forward business emails to your personal Gmail account because it's easier to view on mobile, for example.

You might hope shadow IT is a problem only for large enterprises, too big to centrally manage. My experience running a small startup suggests otherwise. We agonized over our choice of a productivity tools suite — considering pros and cons and balancing user experience with governability. And people are happy to use our tool of choice; they just also use other tools in parallel. We run on Google Workspace, but many of our employees use Office because they're used to it. We use Google Drive for file sharing, but we quickly learned some people prefer iCloud.

People's personal preferences play a significant role here. They want to get their jobs done, not worry about learning a new tool. Platforms make this tendency even worse. Many try to get you to use and rely on them for a long time before asking for added licensing. Consider local file saves on Windows or Mac. By default, every local file save actually gets saved in a directory backed up into Microsoft's or Apple's cloud.

A large enterprise might have more mature security controls to prevent use of unauthorized software, but it also has much more variety in the software people would like to use. The sheer size of an enterprise and the independence of different business units exacerbate the software spread even further. The standard industry security practice for controlling software usage combines bringing in security on every license purchase and restricting software and SaaS usage on the endpoint. While those tactics are useful, they are limited in scope. Paying out of pocket, which some users will do to get the software they want, bypasses enterprise procurement.

## Approved Apps Lead to Building Unapproved Apps

Expanding the use of existing platforms into new and unapproved feature sets is even more pervasive. Did you purchase Office 365 for productivity or Salesforce for your sales reps? Congrats. You've now empowered your business users to build their own apps [with the no-code/low-code platform bundled in](https://www.darkreading.com/cyber-risk/you-can-t-opt-out-of-citizen-development). Unapproved uses of enterprise platforms also bypass SaaS usage controls. Enterprises can't block access to Microsoft or Salesforce, but through them users can send corporate data to unapproved systems.

With each new discovery of an unapproved system, the security team can either try to block it or bring it under their umbrella. Either way, it's an endless game of whack-a-mole. Some tools can help with this discovery, but they often lack context about how these systems are used and which are actually important to business functions.

What if we could ask every business user what systems they use in their day-to-day, regardless of corporate policies? And ask which of those are truly vital for the business? That could give us the ultimate list: a full mapping of shadow IT, coupled with its business importance. Unfortunately, that doesn't work — simply asking people likely won't result in a full list, and what end users find vital may be different from what management does.

## User-Built Tools Expose Shadow IT Network

Enter [citizen development](https://www.darkreading.com/application-security/building-application-security-into-shadow-it), in which business users leverage low-code/no-code tools to streamline their processes, analyze their data, and build custom business applications for their use cases. To be relevant, these apps must connect to the data and processes that the business uses in practice. A citizen developer is not going to call IT to integrate their app with the approved corporate service; instead, they'll connect directly to what we call shadow IT.

Here's an example. Consider a sales team using an unapproved tool for lead tracking. To sync it with the approved CRM, they use no-code automation. By finding automations that connect to the CRM and following the data flow, we can easily find the unapproved tool and what type of data it holds.

Embracing citizen development can leave security teams at a much better spot — having visibility into what software the business actually runs on — if used right.

That "if" is very important. Citizen development [introduces its fair share of security risks](https://www.darkreading.com/cyber-risk/3-ways-no-code-developers-can-shoot-themselves-in-the-foot), which must be mitigated to avoid adverse effects. But by embracing citizen development, we're letting business users codify what used to be a copy-paste data integration. Following these processes will lead us directly to the most important elements of shadow IT.

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyber-risk/to-map-shadow-it-follow-citizen-developers)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyber-risk/to-map-shadow-it-follow-citizen-developers)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyber-risk/to-map-shadow-it-follow-citizen-developers)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyber-risk/to-map-shadow-it-follow-citizen-developers&title=To%20Map%20Shadow%20IT%2C%20Follow%20Citizen%20Developers)[Email](mailto:?subject=To%20Map%20Shadow%20IT,%20Follow%20Citizen%20Developers&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20To%20Map%20Shadow%20IT%2C%20Follow%20Citizen%20Developers%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyber-risk%2Fto-map-shadow-it-follow-citizen-developers)

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

[Cyber Risk\\
\\
How CISOs Can Effectively Communicate Cyber-Risk](https://www.darkreading.com/cyber-risk/how-cisos-can-effectively-communicate-cyber-risk)

[Cyber Risk\\
\\
Ransomware Gangs Pummel Southeast Asia](https://www.darkreading.com/cyber-risk/ransomware-gangs-pummel-southeast-asia)

[Cyber Risk\\
\\
India's Critical Infrastructure Suffers Spike in Cyberattacks](https://www.darkreading.com/cyber-risk/india-s-critical-infrastructure-suffers-spike-in-cyberattacks)

[Cyber Risk\\
\\
NIST Hands Off Post-Quantum Cryptography Work to Cyber Teams](https://www.darkreading.com/cyber-risk/nist-post-quantum-cryptography-work-cyber-teams)

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
