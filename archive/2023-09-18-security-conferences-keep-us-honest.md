---
date: 2023-09-18
description: Michael Bargury highlights the duality of cybersecurity research and
  responsible disclosure at security conferences, using his Black Hat USA presentation
  as a case study. He divulged vulnerabilities in Microsoft’s Azure environment, emphasizing
  that the shared responsibility model leaves customers needing to secure their own
  systems. Bargury notes a shift from zero-day revelations to fostering vendor accountability
  and transparency. He argues that public discourse can compel organizations to prioritize
  security over public relations. This evolution in vulnerability reporting underscores
  an ongoing need for collaboration between researchers and vendors to enhance overall
  cybersecurity resilience.
link: https://www.darkreading.com/cyber-risk/security-conferences-keep-us-honest
tags:
- Vulnerability Disclosure
- Information Security
- Cybersecurity
- Security Conferences
- Risk Management
title: Security Conferences Keep Us Honest
---

- [Cyber Risk](https://www.darkreading.com/cyber-risk)
- [Commentary](https://www.darkreading.com/latest-commentary)

[![The Edge Logo](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt530eb1f4e672eb44/653a71690e92cc040a3e9d6d/Dark_Reading_Logo_TheEdge_0.png?width=700&auto=webp&quality=80&disable=upscale)\\
\\
Cybersecurity In-Depth: Feature articles on security strategy, latest trends, and people to know.](https://www.darkreading.com/program/the-edge)

# Security Conferences Keep Us Honest

Conferences are where vendors and security researchers meet face to face to address problems and discuss solutions — despite the risks associated with public disclosure.

[![Picture of Michael Bargury](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltbd8a249d11a28466/64f150aad5f7ca2f7665bf81/Michael_Bargury_zenity.jpg?width=100&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/author/michael-bargury)

[Michael Bargury](https://www.darkreading.com/author/michael-bargury), CTO & Co-Founder, Zenity

September 18, 2023

4 Min Read

![Photo of an audience member taking a photo of a conference presentation with their cell phone](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltbfe19b843f56c5ca/654e398658cf9d040abf76a2/audience-PG_Arphexad-alamy.jpg?width=1280&auto=webp&quality=80&format=jpg&disable=upscale)

Source: PG Arphexad via Alamy Stock Photo

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyber-risk/security-conferences-keep-us-honest)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyber-risk/security-conferences-keep-us-honest)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyber-risk/security-conferences-keep-us-honest)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyber-risk/security-conferences-keep-us-honest&title=Security%20Conferences%20Keep%20Us%20Honest)[Email](mailto:?subject=Security%20Conferences%20Keep%20Us%20Honest&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Security%20Conferences%20Keep%20Us%20Honest%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyber-risk%2Fsecurity-conferences-keep-us-honest)

In August on a stage at [Black Hat USA](https://www.blackhat.com/us-23/briefings/schedule/index.html#all-you-need-is-guest-32647), I described in detail how [Microsoft guest accounts could gain access to view and manipulate sensitive corporate data](https://www.darkreading.com/application-security/azure-ad-guests-steal-data-microsoft-power-apps), including SQL servers and Azure resources. On top of that, I showed how Power Platform could be leveraged by a hacker to [create internal phishing applications](https://www.blackhat.com/us-23/arsenal/schedule/index.html#powerguest-aad-guest-exploitation-beyond-enumeration-33687) that automatically authenticate their victims and create a backdoor that persists even if the hacked user is deleted. These are still open issues today, as mitigation falls in the customer's side of the shared responsibility model — meaning every Microsoft customer would have to monitor and harden their own environments to mitigate these security holes.

Preparing for the talk, I thought long and hard about what information to share, well aware of the double-edged sword that security research can be. How can I share enough to raise awareness and drive people to action while not making the problem worse by putting it on hackers' radar? After considering that we've already observed all of these issues being exploited in the wild, I decided to share the information; it was important that we leveled the playing field and gave security teams the knowledge and tools they need to keep their organizations secure.

This security researcher's dilemma is not new, and I'm definitely not the first or only one to have to deal with it. I could point to [a few](https://media.defcon.org/DEF%20CON%2031/DEF%20CON%2031%20presentations/nyxgeek%20-%20Track%20the%20Planet%20Mapping%20Identities%20Monitoring%20Presence%20and%20Decoding%20Business%20Alliances%20in%20the%20Azure%20Ecosystem.pdf)[other](https://media.defcon.org/DEF%20CON%2031/DEF%20CON%2031%20presentations/byt3bl33d3r%20-%20SpamChannel%20Spoofing%20Emails%20From%202%20Million%2B%20Domains%20and%20Virtually%20Becoming%20Satan.pdf)[researchers](https://www.tenable.com/security/research/tra-2023-25) who were in a similar position, where they could either remain silent or educate everyone about an [unsolved security issue](https://www.darkreading.com/cyber-risk/a-fintech-horror-story-how-one-company-prioritizes-cybersecurity).

## The Bad Ol' Days

Gone are the days when security researchers used to drop zero-day vulnerabilities on the Black Hat or DEF CON stages. That is, of course, a very good thing — although we did lose something as a security community (but more on that later). In conjunction, most vendors realize that security researchers are acting to keep them honest and improve the security state of the entire community. [As cybersecurity executive Kymberlee Price put it](https://securityconversations.com/episode/kymberlee-price-reflects-on-life-at-the-msrc-hacker-vendor-engagement-bug-bounties/) in a recent interview with Ryan Naraine, just because security researchers are publishing vulnerabilities, it doesn't make them the enemy; if they were the bad guys, they would be using the vulnerability — they wouldn't tell you about them at all.

Admittedly, we do still get zero-day drops now and again, with the pain of recent example Log4Shell being a fresh memory. But it feels like the average researcher, especially one who works for a respectable security vendor or consultancy, goes the vulnerability disclosure route first.

It is important to remember why people are sharing this information publicly. It is because they don't feel like they can get the vendor to fix the problem within a reasonable time frame. In the bad ol' days, security researchers essentially lit fires that forced vendors to fix things right away.

## Where We Are Today

We're mostly in a whole different ballpark today. Most security researchers I know engage with the vendor, wait around for a reply, and then wait some more before they go out and expose things publicly.

It is important to notice the balance of power here. As a researcher, you typically find yourself facing a giant enterprise with endless resources, a strong media presence, and a whole bunch of lawyers. In many cases, you can get the feeling that those endless resources are used to avoid a PR crisis and nullify the issue rather than face it and actually make customers more secure. While [some organizations do help researchers](https://www.eff.org/) through those challenges, it always feels like David vs. Goliath.

The main issue with responsible disclosure, coordinated disclosure, and the popular vulnerability disclosure platforms today is that they put all of the decision at the sole discretion of the organization whose vulnerability is being reported, without any transparency. Sure, we have the CVE system. But issuing those is mostly at the vendor's discretion. For the cloud services we all rely on today, the situation is even worse, with many vendors refusing to issue a CVE and having no transparency for security issues discovered and fixed on their services.

## Keeping Ourselves Honest

We've long known that discussing problems out in the open is the best way to push ourselves to do the right thing. We seem to rediscover this fact again and again in different contexts, be it developing open source software, challenging security by obscurity, or launching initiatives for open government. In today's state of vulnerability disclosure, many feel the pendulum has swung too much to one side, pushing vendors to make choices that minimize short-term visibility concerns at the cost of long-term customer trust and the security of the ecosystem.

Vendor security teams that receive vulnerability reports are doing incredible jobs trying to get their organizations to fix the issues and build strong relationships with researchers. But they too need help. Creating urgency to fix an issue is difficult when the organization feels they control the situation, even while their customers might be at risk.

Security conferences are where security researchers can help vendors make the right choices. They provide a tiny stick a security researcher can poke the vendor with, in hopes of spurring them into action. Information is put out there for the entire community to see and decide whether they accept the current state of things. In public.

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyber-risk/security-conferences-keep-us-honest)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyber-risk/security-conferences-keep-us-honest)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyber-risk/security-conferences-keep-us-honest)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyber-risk/security-conferences-keep-us-honest&title=Security%20Conferences%20Keep%20Us%20Honest)[Email](mailto:?subject=Security%20Conferences%20Keep%20Us%20Honest&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Security%20Conferences%20Keep%20Us%20Honest%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyber-risk%2Fsecurity-conferences-keep-us-honest)

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
