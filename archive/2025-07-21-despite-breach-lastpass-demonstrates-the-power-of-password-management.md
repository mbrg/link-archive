---
date: '2025-07-21'
description: The LastPass breach underscores critical vulnerabilities in password
  management systems. Despite hackers accessing source code and user data, the architecture’s
  reliance on strong master passwords and endpoint MFA mitigates threat severity.
  However, the incident raises concerns around implicit user responsibility in selecting
  and recommending password managers. The balance of convenience versus the potential
  for catastrophic breaches remains tenuous. Users must reinforce security protocols,
  such as rotating sensitive passwords, and question the robustness of their chosen
  vault providers. The systemic design flaws must prompt introspection into the shared
  security paradigm of password management tools.
link: https://www.darkreading.com/edge-articles/despite-breach-lastpass-demonstrates-the-power-of-password-management
tags:
- Cybersecurity
- Password Management
- Data Breaches
- MFA
- LastPass
title: Despite Breach, LastPass Demonstrates the Power of Password Management
---

- [Cyberattacks & Data Breaches](https://www.darkreading.com/cyberattacks-data-breaches)

[![The Edge Logo](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt530eb1f4e672eb44/653a71690e92cc040a3e9d6d/Dark_Reading_Logo_TheEdge_0.png?width=700&auto=webp&quality=80&disable=upscale)\\
\\
Cybersecurity In-Depth: Feature articles on security strategy, latest trends, and people to know.](https://www.darkreading.com/program/the-edge)

# Despite Breach, LastPass Demonstrates the Power of Password Management

What's scarier than keeping all of your passwords in one place and having that place raided by hackers? Maybe reusing insecure passwords.

[![Picture of Michael Bargury](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltbd8a249d11a28466/64f150aad5f7ca2f7665bf81/Michael_Bargury_zenity.jpg?width=100&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/author/michael-bargury)

[Michael Bargury](https://www.darkreading.com/author/michael-bargury), CTO & Co-Founder, Zenity

February 20, 2023

5 Min Read

![Photo of the aftermath of a car burglary, with the passenger side window smashed and safety glass pieces everywhere](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt43d1e6a0c2e0dabb/64f1651611a9e52894193259/carburglary-Jeffrey_Isaac_Greenberg_16_-alamy.jpg?width=1280&auto=webp&quality=80&format=jpg&disable=upscale)

Source: Jeffrey Isaac Greenberg 16+ via Alamy Stock Photo

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyberattacks-data-breaches/despite-breach-lastpass-demonstrates-the-power-of-password-management)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyberattacks-data-breaches/despite-breach-lastpass-demonstrates-the-power-of-password-management)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyberattacks-data-breaches/despite-breach-lastpass-demonstrates-the-power-of-password-management)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyberattacks-data-breaches/despite-breach-lastpass-demonstrates-the-power-of-password-management&title=Despite%20Breach%2C%20LastPass%20Demonstrates%20the%20Power%20of%20Password%20Management)[Email](mailto:?subject=Despite%20Breach,%20LastPass%20Demonstrates%20the%20Power%20of%20Password%20Management&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Despite%20Breach%2C%20LastPass%20Demonstrates%20the%20Power%20of%20Password%20Management%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyberattacks-data-breaches%2Fdespite-breach-lastpass-demonstrates-the-power-of-password-management)

A few months ago, LastPass [suffered a significant breach](https://blog.lastpass.com/2022/12/notice-of-recent-security-incident/). Hackers got both the source code and user data, including encrypted secret vaults and plaintext metadata. This [is not](https://www.darkreading.com/cloud-security/lastpass-data-breach-source-code-stolen) the first breach LastPass had suffered.

[This breach](https://www.darkreading.com/application-security/lastpass-discloses-second-breach-in-three-months) put me in a weird situation. I'd been a champion of using secret vaults for a few years now. After a brief period of trial and examination, I chose LastPass even though it [had been breached before](https://blog.lastpass.com/2015/06/lastpass-security-notice/). Being happy with the experience despite its quirks and a trying onboarding, I recommended its use to anyone I cared about — my family, friends, and colleagues. I helped them onboard and generate random passwords, install the app everywhere, and come up with a really good master password. In some cases, this wasn't easy and took a lot of guidance and convincing on my part.

The obvious fact I had failed to realize at the time was that a recommendation as strong as that comes with an implicit responsibility. When those people see a major news article about their passwords belonging to hackers now, they reach out to me for questions. They are right — I got them into this mess, didn't I?

## Why Evangelize Secret Managers?

I was not always convinced secret managers were a good idea, especially commercial ones with their own cloud infra. As a teen, I started off where more people do, using one "good password" for everything, appending a service-specific prefix or suffix to avoid straight password duplication. I also had the unfortunate experience of working in an enterprise that forced me to change my password every 30 days. The number appended to the end of your password was a token of seniority in that org. I reached some number in the 40s and was really proud of myself and how experienced I was. Of course, when you're proud of something, you really want to share it. And so we did.

I always knew that sharing the chunky part of my password across services was a bad idea. That knowledge became a reality when I started to understand [how hackers leverage these common yet faulty tactics](https://www.darkreading.com/remote-workforce/norton-lifelock-warns-on-password-manager-account-compromises) to their advantage. Appending two letters to your "good password" does nothing to stop an attacker from compromising one service based on a compromised password for the other. It only makes you feel good about complying with a bad policy. Fortunately, monthly password changes are now passe.

But my first attempt at solving my password problem was using my dad's custom-built bare C based password manager. It was very basic: encrypt and decrypt a text file. You pop the encrypted file on a shared drive and congrats, you have a secret manager! Of course, this has clear downsides, like no mobile support, auto-fill, or password generation. I also wrote [my own cli-based interface](https://github.com/mbrg/crd) on top of cloud and native keyvaults. It was great, but still, no utilities. I used these two options for a long while. I was still looking for solutions with those utility features, but anything with the word "cloud" in it was denied at the doorstep.

Then I took an advanced crypto course as part of a masters in computer science. The beauty of Merkel trees and zero knowledge proofs excited my imagination and made me devour the Web in search of real-world applications. I encountered a scientific paper describing secret vaults, and the idea just clicked. Of course, it makes perfect sense! The only way for my passwords to be truly secure is to assume the vault provider is malicious and still be confident that they can't accomplish anything significant. I had reached the conclusion that a password manager that follows the theory would be safe to use.

The other threat vector to get my password is a malicious vendor or party within that vendor. They could, for example, steal my master password from the client application, making the theorized protections irrelevant. After reading through reviews putting different password manager clients under scrutiny, I became convinced that the implementations are up to standards and it's time to migrate.

Several years afterwards, I found myself with hundreds of auto-generated passwords managed by my password manager. I had also been able to convince the people I care about to go through that journey too. I was really happy about it.

## What If My Vault Gets Breached?

If hackers actually get access to my plaintext passwords, I will be in a world of hurt. I do have MFA enabled on anything important, but MFA-anyway is notoriously hard to pull off. Just thinking about rolling all those passwords manually gives me a headache. I don't see myself being able to convince my family to do it for their accounts too.

In short, this scenario would be catastrophic.

Wait, Didn't Your Password Manager Just Get Breached?

Well yes, most definitely. One colleague who chose LastPass on my advice recently asked me two questions after reading a concerning article. What happened? and How should he react?

My answer for the first question couldn't be worse. Hackers compromised both code and data. Data contains our vaults, with plaintext metadata including email addresses and our encrypted passwords.

My answer to the second question was very different. There is no indication of the hackers stealing master passwords by abusing the client. We can assume that didn't happen or we would see a whole host of reproductions across the industry. So if your master password is strong enough not to be cracked and you have MFA on everything that matters, you are fine. If you still feel iffy, roll your important passwords.

Concrete steps to take if you were affected by the breach:

- Roll your master password.

- Enable MFA and roll passwords everywhere that matters.

- If your master password was weak, I strongly advise you to roll all of your passwords.


How Can That Be? Aren't Those Answers Contradictory?

The seemingly contradictory nature of these two answers shows just how powerful avoiding storage of sensitive data is.

LastPass got breached. Repeatedly. Attackers took everything there is to take. The impact is severe, but not catastrophic at least given what we know now. That's a brilliant property of the system's design.

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyberattacks-data-breaches/despite-breach-lastpass-demonstrates-the-power-of-password-management)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyberattacks-data-breaches/despite-breach-lastpass-demonstrates-the-power-of-password-management)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyberattacks-data-breaches/despite-breach-lastpass-demonstrates-the-power-of-password-management)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyberattacks-data-breaches/despite-breach-lastpass-demonstrates-the-power-of-password-management&title=Despite%20Breach%2C%20LastPass%20Demonstrates%20the%20Power%20of%20Password%20Management)[Email](mailto:?subject=Despite%20Breach,%20LastPass%20Demonstrates%20the%20Power%20of%20Password%20Management&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Despite%20Breach%2C%20LastPass%20Demonstrates%20the%20Power%20of%20Password%20Management%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyberattacks-data-breaches%2Fdespite-breach-lastpass-demonstrates-the-power-of-password-management)

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
