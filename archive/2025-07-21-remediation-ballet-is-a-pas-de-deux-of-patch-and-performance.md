---
date: '2025-07-21'
description: The article discusses the evolving landscape of vulnerability remediation,
  emphasizing the integration of AI in code generation. While tools like GitHub Copilot
  enhance efficiency, developers and security teams must navigate the complexities
  of applying patches without disrupting existing functionality. The balance between
  security patch implementation and software performance is crucial, particularly
  in large enterprises with divided responsibilities. The article advocates for recognizing
  both mitigation risks and vulnerability threats, suggesting a measured approach
  to remediation that acknowledges the inherent challenges of both realms.
link: https://www.darkreading.com/edge/remediation-ballet-is-a-pas-de-deux-of-patch-and-performance
tags:
- Application Security
- AI in Security
- Vulnerability Management
- Patch Management
- Cybersecurity
title: Remediation Ballet Is a Pas de Deux of Patch and Performance
---

- [Cyber Risk](https://www.darkreading.com/cyber-risk)

[![The Edge Logo](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt530eb1f4e672eb44/653a71690e92cc040a3e9d6d/Dark_Reading_Logo_TheEdge_0.png?width=700&auto=webp&quality=80&disable=upscale)\\
\\
Cybersecurity In-Depth: Feature articles on security strategy, latest trends, and people to know.](https://www.darkreading.com/program/the-edge)

# Remediation Ballet Is a Pas de Deux of Patch and Performance

AI-generated code promises quicker fixes for vulnerabilities, but ultimately developers and security teams must balance competing interests.

[![Picture of Michael Bargury](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltbd8a249d11a28466/64f150aad5f7ca2f7665bf81/Michael_Bargury_zenity.jpg?width=100&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/author/michael-bargury)

[Michael Bargury](https://www.darkreading.com/author/michael-bargury), CTO & Co-Founder, Zenity

June 26, 2023

4 Min Read

![Ballerina Polina Semionova and male dancer Jason Reilly in passionate Ballet pas de deux taken from the wings](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt8100003ea6f7ff0e/64f176317de67f334000e4e1/pasdedeux-Sian_Trenberth-alamy.jpg?width=1280&auto=webp&quality=80&format=jpg&disable=upscale)

Source: Sian Trenberth via Alamy Stock Photo

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyber-risk/remediation-ballet-is-a-pas-de-deux-of-patch-and-performance)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyber-risk/remediation-ballet-is-a-pas-de-deux-of-patch-and-performance)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyber-risk/remediation-ballet-is-a-pas-de-deux-of-patch-and-performance)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyber-risk/remediation-ballet-is-a-pas-de-deux-of-patch-and-performance&title=Remediation%20Ballet%20Is%20a%20Pas%20de%20Deux%20of%20Patch%20and%20Performance)[Email](mailto:?subject=Remediation%20Ballet%20Is%20a%20Pas%20de%20Deux%20of%20Patch%20and%20Performance&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Remediation%20Ballet%20Is%20a%20Pas%20de%20Deux%20of%20Patch%20and%20Performance%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyber-risk%2Fremediation-ballet-is-a-pas-de-deux-of-patch-and-performance)

Recent advancements in artificial intelligence (AI) have rekindled the spirit of fully automated vulnerability remediation. The industry is booming with attempts to provide tailored remediation that works in your code base, taking into account your unique environment and circumstances, powered by generative AI. The tech is incredible and is already showing signs of success. The big question remains: Are we ready to embrace it?

Ask any developer using [GitHub Copilot](https://www.darkreading.com/cybersecurity-analytics/generative-ai-empowers-users-but-challenges-security) or one of the alternatives, and you will find wonderful examples of how AI can generate context-aware code completion suggestions that save a ton of time. You'll also find examples of irrelevant, overly complex, or flat-out-wrong suggestions generated at bulk.

There's no doubt we're witnessing a breakthrough in technology that will produce automated code generation far better than everything we've seen before. However, tech is only one piece in the remediation puzzle, with significant weight falling on process and people.

## New Tech, Old Challenges

Every change to an application is a balancing act between introducing improvements and protecting existing functionality. Urgent changes, including security fixes, take this problem to the extreme by introducing tight schedule constraints and a strong pressure to get things right. Applying [patches can have unexpected consequences](https://www.darkreading.com/vulnerabilities-threats/patching-poses-security-problems-with-move-to-more-remote-work), which in the worst case can mean an outage.

Ask any IT manager who handles patching, and you will hear a never-ending list of horror stories where users were unable to go about their day-to-day work because of a [seemingly benign patch](https://www.darkreading.com/vulnerabilities-threats/mcafee-offers-compensation-to-enterprise-customers-hit-by-faulty-av-update). But [failing to apply a patch](https://www.darkreading.com/vulnerabilities-threats/firms-still-struggle-to-prioritize-security-vulnerabilities), only to have the [vulnerability exploited as part of a breach](https://www.darkreading.com/cyberattacks-data-breaches/accellion-data-breach-resulted-in-extortion-attempts-against-multiple-victims), can also have devastating consequences for the entire organization, as readers of this column are acutely aware.

Good software engineering is focused on finding a balance that maintains the ability to apply changes to the application at a fast pace while [protecting the application](https://www.darkreading.com/cyber-risk/where-there-s-no-code-there-s-no-sdlc) and its maintainers from bad changes. There are plenty of challenges in achieving this goal, including legacy software that cannot be easily changed and ever-changing system requirements, to name just a couple.

In reality, maintaining the ability to change software is a difficult goal that cannot always be attained, and teams have to accept the risk of some changes resulting in unexpected consequences that need more remediation. The main challenge for engineers lies in ensuring that the proposed change would produce expected results, not in writing the actual code change, which generative AI can now do for us. Security fixes are no different.

## Overlapping Responsibility for Application Security

Another major challenge that becomes acute in large enterprises is the fractioning of responsibility. A central AppSec team in charge of reducing risk across the organization cannot be expected to understand the potential consequences of applying a specific fix to a particular application. Some solutions, such as virtual patching and network controls, allow security teams to fix problems without relying on development teams, which could simplify mitigation, reduce required engineering resources, or eliminate buy-in.

Politics aside, solutions like these are blunt tools that are bound to cause friction. Network controls, such as firewalls and Web application firewalls (WAFs), are an area where IT and security traditionally have much autonomy, and developers just have to deal with it. They represent a clear choice to put control before productivity and to accept the added friction for developers.

For application vulnerabilities, fixes require changing either the application's code or the application's environment. While changing the application's code is within the scope of responsibility of a development team, changing the environment has always been a way for security teams to intervene and might present a better path for AI-generated remediations to be applied.

In the on-premises world, this usually meant security agents managing workloads and infrastructure. In managed environments, like a public cloud provider or low-code/no-code platform, security teams could fully understand and examine changes to the environment, which allowed deeper intervention in application behavior.

Configuration, for example, can change the behavior of an application without changing its code, thus applying a security mitigation while limiting consequences. A good example of this is enabling built-in encryption-at-rest for databases, [preventing public data access](https://www.zenity.io/microsoft-power-pages-low-code-misconfiguration-remains-a-top-security-risk/), or masking sensitive data handled by a low-code app.

## Striking the Right Balance

It is important to note that environment changes can have adverse effects on the application. Encryption comes at a performance cost, and masking makes debugging more difficult. However, these are risks more and more organizations are willing to take for the benefit of increasing security mitigation at lower engineering cost.

At the end of the day, even once a mitigation is available, organizations have to balance the risk of security vulnerabilities with the risk of applying mitigations. It is clear that AI-generated mitigations reduce the cost of remediation, but the risk of applying them will always exist. However, failing to remediate for fear of consequences puts us on one end of the spectrum between those two risks, which is far away from a perfect balance. Applying any auto-generated remediation automatically would be the other end of the spectrum.

Instead of choosing either extreme, we should acknowledge both the vulnerability risks and the mitigation risks and find a balance between the two. Mitigations will sometimes break applications. But choosing not to accept this risk means, by default, choosing to accept the risk of security breach due to lack of mitigation.

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyber-risk/remediation-ballet-is-a-pas-de-deux-of-patch-and-performance)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyber-risk/remediation-ballet-is-a-pas-de-deux-of-patch-and-performance)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyber-risk/remediation-ballet-is-a-pas-de-deux-of-patch-and-performance)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyber-risk/remediation-ballet-is-a-pas-de-deux-of-patch-and-performance&title=Remediation%20Ballet%20Is%20a%20Pas%20de%20Deux%20of%20Patch%20and%20Performance)[Email](mailto:?subject=Remediation%20Ballet%20Is%20a%20Pas%20de%20Deux%20of%20Patch%20and%20Performance&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Remediation%20Ballet%20Is%20a%20Pas%20de%20Deux%20of%20Patch%20and%20Performance%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyber-risk%2Fremediation-ballet-is-a-pas-de-deux-of-patch-and-performance)

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
