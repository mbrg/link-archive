---
date: 2024-01-23
description: 'Michael Bargury''s article discusses the disruptive potential of AI
  in enterprise environments, highlighting the rapid deployment of AI solutions like
  Microsoft 365 Copilot across major companies. Key risks include: 1. **Permission
  Management:** AI models may retain access to outdated data after personnel changes,
  complicating security protocols. 2. **Data Boundary Erosion:** AI''s ability to
  aggregate and access vast datasets challenges traditional data segregation principles.
  3. **Activity Monitoring Dilemmas:** AI impersonation blurs the lines for monitoring
  suspicious activities, complicating anomaly detection. These factors signal a need
  for reevaluated security frameworks amidst fast-paced AI integration, emphasizing
  innovation over static practices.'
link: https://www.darkreading.com/cyber-risk/move-fast-and-break-the-enterprise-with-ai
tags:
- Cybersecurity
- Artificial Intelligence
- Machine Learning
- Enterprise Security
- Data Privacy
title: Move Fast and Break the Enterprise With AI
---

- [Cyber Risk](https://www.darkreading.com/cyber-risk)

[![The Edge Logo](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt530eb1f4e672eb44/653a71690e92cc040a3e9d6d/Dark_Reading_Logo_TheEdge_0.png?width=700&auto=webp&quality=80&disable=upscale)\\
\\
Cybersecurity In-Depth: Feature articles on security strategy, latest trends, and people to know.](https://www.darkreading.com/program/the-edge)

# Move Fast and Break the Enterprise With AI

The tantalizing promise of true artificial intelligence, or at least decent machine learning, has whipped into a gallop large organizations not built for speed.

[![Picture of Michael Bargury](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltbd8a249d11a28466/64f150aad5f7ca2f7665bf81/Michael_Bargury_zenity.jpg?width=100&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/author/michael-bargury)

[Michael Bargury](https://www.darkreading.com/author/michael-bargury), CTO & Co-Founder, Zenity

January 23, 2024

4 Min Read

![Jockeys race four horses down a racetrack, crops raised](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltf90b5e2bcc0f7e30/65af52aa45b4a8040a1f810b/horserace-Michael_Turner-alamy.jpg?width=1280&auto=webp&quality=80&format=jpg&disable=upscale)

Source: Michael Turner via Alamy Stock Photo

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyber-risk/move-fast-and-break-the-enterprise-with-ai)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyber-risk/move-fast-and-break-the-enterprise-with-ai)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyber-risk/move-fast-and-break-the-enterprise-with-ai)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyber-risk/move-fast-and-break-the-enterprise-with-ai&title=Move%20Fast%20and%20Break%20the%20Enterprise%20With%20AI)[Email](mailto:?subject=Move%20Fast%20and%20Break%20the%20Enterprise%20With%20AI&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Move%20Fast%20and%20Break%20the%20Enterprise%20With%20AI%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyber-risk%2Fmove-fast-and-break-the-enterprise-with-ai)

COMMENTARY

Working for a large enterprise for many years often leaves you with a strong feeling that everything will forever stay the same. Sure, some things change, even drastically. There are ups and downs, reorgs on a regular cadence, and sometimes companies even reinvent and rejuvenate themselves like Satya Nadella's Microsoft did in recent years. But most things stay the same, and culture runs deep. There is an inherent unwillingness to change; after all, these are large, successful enterprises — why change?

Security professionals often reach a point in their careers where they look back and ask: Have we made any progress? Are organizations really more secure today than they were 20 years ago? Sure, the threat landscape is different, but so is the amount of money and, more importantly, mindshare being spent on security throughout the industry. Even with all of that, some things never change. We have evergreen sayings, like "developers don't care about security," "you can't secure the perimeter," "x is the new perimeter," and my personal (un)favorite, "users are the weakest link."

Securing a large enterprise means having to deal with the problems of a large enterprise, which, as stated above, has a basic unwillingness to change.

Until it does.

## Changing at the Speed of AI

Enter artificial intelligence (AI). Emboldened by the technology's promise of changing all industries, large enterprises are mobilizing their AI initiatives at lightning speed. It's been incredible (and frightening) to see how fast Microsoft and others, including Salesforce, Google, and Amazon, have pushed AI directly into their core enterprise offerings. They do this despite knowing that AI has serious problems that no one can really solve yet, like [alignment](https://openai.com/blog/our-approach-to-alignment-research) with human values and [safety](https://www.safe.ai/statement-on-ai-risk) risks. They do this because their customers — the entire enterprise market — are eager to adopt the bleeding edge to get one up on their competition.

Whether you are an AI enthusiast or an AI skeptic doesn't matter at this point. The winds of change are blowing, and an opportunity has opened up in which enterprises are willing to risk their core competencies to reap the rewards of AI before their competitors do.

## Breaking the Enterprise

The most significant advancement in enterprise AI is business Copilots. Every large Microsoft shop is looking into [Microsoft 365 Copilot](https://www.microsoft.com/en-us/microsoft-365/microsoft-copilot) to seek fulfillment of the promise of a huge productivity boost. [Google](https://workspace.google.com/solutions/ai/), [AWS](https://aws.amazon.com/blogs/aws/introducing-amazon-q-a-new-generative-ai-powered-assistant-preview/), and [Salesforce](https://www.salesforce.com/news/press-releases/2023/09/12/ai-einstein-news-dreamforce/) have released their own versions: Duet AI, Amazon Q, and Einstein, respectively. They're doing this because they see a huge value to be gained. This idea of a Copilot also [completely breaks](https://www.zenity.io/microsoft-copilot-studio-vulnerabilities-explained/)[key assumptions](https://www.darkreading.com/cybersecurity-analytics/generative-ai-empowers-users-but-challenges-security) about how an enterprise operates.

- Breaking permissions. To service my requests, my personal corporate AI needs to munch through all of the data I can access in order to index it so that it's available for query. Pretty soon we can expect it to train on the previous conversation I had with it. Now let's consider what happens when I move to a different role in the company or somebody removes my access. Can we remove that knowledge from the AI's neural network? That does not seem to be an existing capability of models today. Maybe tomorrow?

- Breaking data boundaries. If a single AI can answer questions across all of my corporate data access, it is difficult to see how data boundaries could be maintained. Every control we put in front of data becomes meaningless, when the AI can read the data and write it infinite times from its "memory."

- Breaking activity monitoring. We're used to monitoring user activity to find snooping employees or distinguish between human and scripted behavior. When AI works by user impersonation and has to touch every piece of data to which I have access to build an index, does [anomalous access](https://www.darkreading.com/vulnerabilities-threats/are-ai-engineered-threats-fud-or-reality-) mean anything anymore?


These problems might have solutions right around the corner, or they might be insurmountable in AI's current form and require a fundamental rethink. But one thing is clear: The problems have not been solved, yet we're moving forward anyway. And that is bound to be interesting.

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyber-risk/move-fast-and-break-the-enterprise-with-ai)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyber-risk/move-fast-and-break-the-enterprise-with-ai)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyber-risk/move-fast-and-break-the-enterprise-with-ai)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyber-risk/move-fast-and-break-the-enterprise-with-ai&title=Move%20Fast%20and%20Break%20the%20Enterprise%20With%20AI)[Email](mailto:?subject=Move%20Fast%20and%20Break%20the%20Enterprise%20With%20AI&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Move%20Fast%20and%20Break%20the%20Enterprise%20With%20AI%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyber-risk%2Fmove-fast-and-break-the-enterprise-with-ai)

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
