---
date: 2024-08-19
description: In "Assume Breach When Building AI Apps," Michael Bargury emphasizes
  the inevitability of AI jailbreaks, urging developers to design applications with
  the understanding that such exploits are a matter of context, not mere vulnerabilities.
  The rise of AI jailbreaking communities highlights the ease with which these bypasses
  can be discovered, outpacing defensive strategies. Bargury advocates for proactive
  oversight rather than reliance on perimeter defenses, suggesting monitoring systems
  capable of rapid response to potential exploits, framing AI as an unpredictable
  asset that requires diligent governance. This perspective is crucial for developers
  and security professionals adapting to AI's growing role in enterprise applications.
link: https://www.darkreading.com/application-security/assume-breach-when-building-ai-apps
tags:
- application security
- jailbreaking
- cybersecurity
- AI security
- vulnerability management
title: Assume Breach When Building AI Apps
---

- [Application Security](https://www.darkreading.com/application-security)

[![The Edge Logo](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt530eb1f4e672eb44/653a71690e92cc040a3e9d6d/Dark_Reading_Logo_TheEdge_0.png?width=700&auto=webp&quality=80&disable=upscale)\\
\\
Cybersecurity In-Depth: Feature articles on security strategy, latest trends, and people to know.](https://www.darkreading.com/program/the-edge)

# Assume Breach When Building AI Apps

AI jailbreaks are not vulnerabilities; they are expected behavior.

[![Picture of Michael Bargury](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltbd8a249d11a28466/64f150aad5f7ca2f7665bf81/Michael_Bargury_zenity.jpg?width=100&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/author/michael-bargury)

[Michael Bargury](https://www.darkreading.com/author/michael-bargury), CTO & Co-Founder, Zenity

August 19, 2024

4 Min Read

![person in a dark suit and beard breaking out of a white wall](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltd42c317460171325/66bfe2c2473f2f75eb0c2115/Break-it-iStock_000047114688_Medium.jpg?width=1280&auto=webp&quality=80&format=jpg&disable=upscale)

Source: Pinkypills via iStock

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/application-security/assume-breach-when-building-ai-apps)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/application-security/assume-breach-when-building-ai-apps)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/application-security/assume-breach-when-building-ai-apps)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/application-security/assume-breach-when-building-ai-apps&title=Assume%20Breach%20When%20Building%20AI%20Apps)[Email](mailto:?subject=Assume%20Breach%20When%20Building%20AI%20Apps&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Assume%20Breach%20When%20Building%20AI%20Apps%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fapplication-security%2Fassume-breach-when-building-ai-apps)

COMMENTARY

If you are still a skeptic about artificial intelligence (AI), you won't be for long. I was recently using Claude.ai to model security data I had at hand into a graph for attack path analysis. While I can do this myself, Claude took care of the task in minutes. More importantly, Claude was just as quick to adapt the script when significant changes were made to the initial requirements. Instead of me having to switch between being a security researcher and data engineer — exploring the graph, identifying a missing property or relation, and adapting the script — I could keep on my researcher hat while Claude played the engineer.

These are moments of clarity, when you realize your toolbox has been upgraded, saving you hours or days of work. It seems like many people have been having those moments, becoming more convinced of the impact AI is going to have in the enterprise.

But AI isn't infallible. There have been a number of public examples of AI jailbreaking, where the generative AI model was fed carefully crafted prompts to do or say unintended things. It can mean bypassing built-in safety features and guardrails or accessing capabilities that are supposed to be restricted. AI companies are trying to solve jailbreaking; some say they have either done so or are making significant progress. Jailbreaking is treated as a fixable problem — a quirk we'll soon get rid of.

As part of that mindset, AI vendors are treating jailbreaks as vulnerabilities. They expect researchers to submit their latest prompts to a bug-bounty program instead of publishing them on social media for laughs. Some security leaders are [talking about AI jailbreaks in terms of responsible disclosure](https://twitter.com/markrussinovich/status/1806036596556476852), creating a clear contrast with those supposedly irresponsible people who disclose jailbreaks publicly.

## Reality Sees Things Differently

Meanwhile, AI jailbreaking communities are popping up on social media and community platforms, such as Discord and Reddit, like mushrooms after the rain. These communities are more akin to gaming speedrunners than to security researchers. Whenever a new generative AI model is released, these communities race to see who can find a jailbreak first. It usually takes minutes, and they never fail. These communities do not know about, of care about, responsible disclosure.

[To quote an X post from Pliny the Prompter](https://x.com/i/web/status/1807105884381978700), a popular social media account from the AI breaking community: "circumventing AI 'safety' measures is getting easier as they become more powerful, not harder. this may seem counterintuitive but it's all about the surface area of attack, which seems to be expanding much faster than anyone on defense can keep up with."

Let's imagine for a second that vulnerability disclosure could work — that we can get every person on the planet to submit their evil prompts to a National Vulnerability Database-style repository before sharing it with their friends. Would that actually help? Last year at DEF CON, the AI village hosted the largest public AI red-teaming event, where they [reportedly collected over 17,000 jailbreaking conversations](https://www.humane-intelligence.org/grt). This was an incredible effort with huge benefits to our understanding of securing AI, but it did not make any significant change to the rate at which AI jailbreaks are discovered.

Vulnerabilities are quirks of the application in which they were found. If the application is complex, it has more surface for vulnerabilities. AI captures human languages so well, but can we really hope to enumerate all quirks of the human experience?

## Stop Worrying About Jailbreaks

We need to operate under the assumption that AI jailbreaks are trivial. Don't give your AI application capabilities it should not be using. If the AI application can perform actions and relies on people not knowing those prompts as a defense mechanism, expect those actions to be eventually exploited by a persistent user.

AI startups are suggesting we think of AI agents as employees who know a lot of facts but need guidance on applying their knowledge to the real world. As security professionals, I believe we need a different analogy: I suggest you think of an AI agent as an expert you want to hire, even though that expert defrauded their previous employer. You really need this employee, so you put a bunch of guardrails in place to ensure this employee won't defraud you as well. But at the end of the day, every data and access you give this problematic employee exposes your organization and is risky. Instead of trying to create systems that can't be jailbroken, let's focus on applications that are easy to monitor for when they inevitably are, so we can quickly respond and limit the impact.

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/application-security/assume-breach-when-building-ai-apps)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/application-security/assume-breach-when-building-ai-apps)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/application-security/assume-breach-when-building-ai-apps)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/application-security/assume-breach-when-building-ai-apps&title=Assume%20Breach%20When%20Building%20AI%20Apps)[Email](mailto:?subject=Assume%20Breach%20When%20Building%20AI%20Apps&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Assume%20Breach%20When%20Building%20AI%20Apps%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fapplication-security%2Fassume-breach-when-building-ai-apps)

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
