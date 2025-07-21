---
date: 2024-06-24
description: 'Michael Bargury highlights the necessity of integrating application
  security (AppSec) within the burgeoning field of citizen development, particularly
  given the dramatic rise of shadow IT. A case study reveals two developers addressed
  70,000 vulnerabilities in three months, underscoring key strategies: thorough inventory
  management, clear policy frameworks, automated risk assessments, and an emphasis
  on self-service documentation. The challenge lies in harnessing non-security-savvy
  business users while fostering a security-first culture. As citizen development
  proliferates, effective AppSec solutions will increasingly rely on innovative automation
  and collaborative governance to mitigate risks without hindering business agility.'
link: https://www.darkreading.com/application-security/building-application-security-into-shadow-it
tags:
- Vulnerabilities
- Citizen Development
- Automation in Security
- Shadow IT
- Application Security
title: What Application Security Within Shadow IT Looks Like
---

- [Application Security](https://www.darkreading.com/application-security)
- [Insider Threats](https://www.darkreading.com/vulnerabilities-threats/insider-threats)

[![DR Technology Logo](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt4c091cd3ac9935ea/653a71456ad0f6040a6f71bd/Dark_Reading_Logo_Technology_0.png?width=700&auto=webp&quality=80&disable=upscale)\\
\\
News, news analysis, and commentary on the latest trends in cybersecurity technology.](https://www.darkreading.com/program/dr-technology)

# What Building Application Security Into Shadow IT Looks Like

AppSec is hard for traditional software development, let alone citizen developers. So how did two people resolve 70,000 vulnerabilities in three months?

[![Picture of Michael Bargury](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltbd8a249d11a28466/64f150aad5f7ca2f7665bf81/Michael_Bargury_zenity.jpg?width=100&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/author/michael-bargury)

[Michael Bargury](https://www.darkreading.com/author/michael-bargury), CTO & Co-Founder, Zenity

June 24, 2024

4 Min Read

![Businesspeople cast long shadows during morning rush hour inside Grand Central Station](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blte060f517bef7733d/6674aacc827832101a9c62ee/bizshadows-David_Grossman-alamy.jpg?width=1280&auto=webp&quality=80&format=jpg&disable=upscale)

Source: David Grossman / Alamy Stock Photo

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/application-security/building-application-security-into-shadow-it)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/application-security/building-application-security-into-shadow-it)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/application-security/building-application-security-into-shadow-it)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/application-security/building-application-security-into-shadow-it&title=What%20Building%20Application%20Security%20Into%20Shadow%20IT%20Looks%20Like)[Email](mailto:?subject=What%20Building%20Application%20Security%20Into%20Shadow%20IT%20Looks%20Like&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20What%20Building%20Application%20Security%20Into%20Shadow%20IT%20Looks%20Like%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fapplication-security%2Fbuilding-application-security-into-shadow-it)

Application security (AppSec) programs are difficult to use and filled with vulnerabilities. Overloaded staff face an inadequate budget. Communication with developers is challenging. These sayings are so true, so ubiquitous, that they've become tropes. This is why meeting a team of two who managed to resolve 70,000 security vulnerabilities in three months made me gasp.

## 70,000 Vulnerabilities? Really?

Actually, they found 80,000, 70,000 of which they were able to fix within 90 days. These numbers do not indicate particularly vulnerable applications. They indicate taking a real look in the mirror, beyond the usual lines drawn in the sand between professional development and citizen development, which we sometimes call shadow IT.

Citizen developers are now embedded in every part of large enterprises. [Yes, that includes yours.](https://www.darkreading.com/cyber-risk/you-can-t-opt-out-of-citizen-development) Last year, Microsoft [announced](https://www.microsoft.com/en-us/investor/events/fy-2023/earnings-fy-2023-q3.aspx) that Power Platform, its popular low-code/no-code platform built into M365, had surpassed 33 million users, growing 50% year over year. These users work for the enterprise — your enterprise. They build critical applications, from finance to risk and customer care. It's a real boost to digital transformation, for the business and by the business (user).

## Citizen Development Security Challenges

A few aspects of citizen development make building an AppSec program around it particularly challenging:

- The scale of citizen development is between 10x and 100x that of professional development, whether you measure it in terms of numbers of developers, number of applications, or any other metric.

- The variance of business units can be so big that it is easier to think of some business units as separate entities. Indeed, in a large enough corporation, some business units fall under different laws and regulation and have a different risk appetite.

- Citizen developers, as business users, are not security-savvy. If you try to explain injection attacks to a business user, it would probably not be a fruitful conversation or a good use of anyone's time. Citizen developers should do what they do best: move the business forward.

- Finally, the lack of process can be tricky — citizen development is all about moving fast. [You edit right in production](https://www.darkreading.com/cyber-risk/where-there-s-no-code-there-s-no-sdlc), adapt quickly, and move forward.


Fortunately, some [standards have emerged](https://owasp.org/www-project-top-10-low-code-no-code-security-risks/) that document and categorize the security vulnerabilities in low-code/no-code apps built by citizen developers.

## AppSec for Citizen Development

The good news is that the unique challenges of citizen development force us to think outside of the box. Any manual review or process goes out the window. Blocking business users from developing software is never a real option, even when we pretend it is.

Building a successful AppSec program for citizen developers requires heavy reliance on automation and self-service. We need to design a process, think about the edge cases, and automate it completely. For example, when a developer says they have fixed an issue, can you retest to confirm? Is there a clear route for escalation and asking for exemptions? What happens when service-level agreements (SLAs) aren't met? We have answers to all of these questions for traditional AppSec, relying on the software development life cycle and years of working with developers. Though none of the established processes work as is with citizen development, we can use our learnings from pro developers to design a solution that does.

To build your program, start with the basics:

1. Inventory. Know what you have, but don't stop there. Ask: Who is the owner for each app?

2. Policy. Clarify your risk appetite. Which applications are outside of your accepted use cases? Which should never have been built?

3. Security assessment and retesting. Know your risk, and have a way to automatically test whether this risk has been mitigated.

4. Self-service. Provide clear documentation. Create a self-service portal where citizen developers can learn about issues and how to fix them, where they can ask for clarification or exemptions.

5. Enforce SLAs. What happens if a vulnerability isn't fixed under an SLA? Take preventive action where possible.

6. Track and report. Ensure you get and maintain executive tailwinds by keeping everything informed on progress.

7. Management buy-in. Making progress at a fast pace requires strong tailwind from management. Clarify the security risk you are mitigating, and tell [an enablement story rather than a blocking story](https://www.darkreading.com/cyber-risk/no-one-wants-to-be-governed-everyone-wants-to-be-helped).


The team I mentioned at the beginning of this article followed all of these points and more. They invested time in designing the process, down to its nooks and crannies. This gave them the confidence to hit "play" on the campaign and drastically reduce the security risk in their environment.

It's an incredible success — two employees, three months, 70,000 vulnerabilities, no business disruption. Those results may be exceptional, but you can achieve incredible results at your business as well.

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/application-security/building-application-security-into-shadow-it)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/application-security/building-application-security-into-shadow-it)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/application-security/building-application-security-into-shadow-it)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/application-security/building-application-security-into-shadow-it&title=What%20Building%20Application%20Security%20Into%20Shadow%20IT%20Looks%20Like)[Email](mailto:?subject=What%20Building%20Application%20Security%20Into%20Shadow%20IT%20Looks%20Like&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20What%20Building%20Application%20Security%20Into%20Shadow%20IT%20Looks%20Like%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fapplication-security%2Fbuilding-application-security-into-shadow-it)

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

[Application Security\\
\\
'Void Banshee' Exploits Second Microsoft Zero-Day](https://www.darkreading.com/application-security/void-banshee-exploits-second-microsoft-zero-day)

[Application Security\\
\\
Microsoft VS Code Undermined in Asian Spy Attack](https://www.darkreading.com/application-security/microsoft-vs-code-undermined-in-asian-spy-attack)

[Application Security\\
\\
Hackers Use Rare Stealth Techniques to Down Asian Military, Gov't Orgs](https://www.darkreading.com/application-security/hackers-use-rare-stealth-techniques-to-down-asian-military-govt-orgs)

[Application Security\\
\\
Microsoft Talks Kernel Drivers Post CrowdStrike Outage](https://www.darkreading.com/application-security/microsoft-lowballs-crowdstrike-outage-impact)

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
