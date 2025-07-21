---
date: 2023-07-14
description: A new vulnerability reported by Michael Bargury at Black Hat USA reveals
  how improperly configured Azure AD guest accounts and over-permissive Power Apps
  connections can lead to unauthorized data access. By manipulating default settings,
  malicious actors can access sensitive corporate applications and data sources. Bargury's
  two-step attack demonstrates how guest accounts can leverage undocumented APIs to
  bypass Standard Data Loss Prevention mechanisms. To defend against these risks,
  he recommends auditing guest access configurations and using the newly introduced
  PowerGuest tool to limit exposure and detect misconfigurations effectively.
link: https://www.darkreading.com/black-hat/azure-ad-guests-steal-data-microsoft-power-apps
tags:
- Azure AD
- Data Protection
- Power Apps
- Cybersecurity Risks
- Application Security
title: Rogue Azure AD Guests Can Steal Data via Power Apps
---

- [Application Security](https://www.darkreading.com/application-security)
- [News](https://www.darkreading.com/latest-news)

# Rogue Azure AD Guests Can Steal Data via Power Apps

A few default guest setting manipulations in Azure AD and over-promiscuous low-code app developer connections can upend data protections.

[![Picture of Ericka Chickowski, Contributing Writer](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt53e8e9e7fdab1946/64f178f5e0ecf1629365e905/ErickaC.jpg?width=100&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/author/ericka-chickowski)

[Ericka Chickowski, Contributing Writer](https://www.darkreading.com/author/ericka-chickowski)

July 14, 2023

5 Min Read

![Rusty lock cut open and hanging on an open, rusty gate](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt13ba927313096dd1/64f1792e789972596e832b06/opengate_marreston_AdobeStock.jpeg?width=1280&auto=webp&quality=80&format=jpg&disable=upscale)

marreston via AdobeStock

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/application-security/azure-ad-guests-steal-data-microsoft-power-apps)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/application-security/azure-ad-guests-steal-data-microsoft-power-apps)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/application-security/azure-ad-guests-steal-data-microsoft-power-apps)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/application-security/azure-ad-guests-steal-data-microsoft-power-apps&title=Rogue%20Azure%20AD%20Guests%20Can%20Steal%20Data%20via%20Power%20Apps)[Email](mailto:?subject=Rogue%20Azure%20AD%20Guests%20Can%20Steal%20Data%20via%20Power%20Apps&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Rogue%20Azure%20AD%20Guests%20Can%20Steal%20Data%20via%20Power%20Apps%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fapplication-security%2Fazure-ad-guests-steal-data-microsoft-power-apps)

Guest accounts in Azure AD (AAD) are meant to provide limited access to corporate resources for external third parties — the idea is to enable collaboration without risking too much exposure. But enterprises may be unknowingly oversharing access to sensitive resources and applications with guests in Azure AD, paving the way for data theft and more.

An upcoming presentation at [Black Hat USA](https://www.blackhat.com/us-23/briefings/schedule/index.html) in August will detail how a toxic combination of easily manipulated default guest account settings and promiscuous connections within Microsoft's low-code development platform [known as Power Apps](https://learn.microsoft.com/en-us/power-apps/powerapps-overview) can kick open the door to giving guest accounts wide-open access to the corporate jewels. [Power Apps provides a rapid development environment](https://www.darkreading.com/application-security/38m-records-exposed-via-microsoft-power-apps-misconfiguration)for businesses to build custom apps that connect various online and on-premises data sources (such as SharePoint, Microsoft 365, Dynamics 365, SQL Server, and so on).

Researcher Michael Bargury, CTO of Zenity, will present his findings in a session on Thursday, Aug. 10, entitled, "[All You Need is Guest](https://www.blackhat.com/us-23/briefings/schedule/index.html#all-you-need-is-guest-32647)." He noted in the session writeup that guests can use undocumented APIs to gain access to corporate SQL servers, SharePoint sites, KeyVault secrets, and more; they can also create and control internal business applications to move laterally within the organization.

"From the perspective of the blue team defending an organization, I'm hoping to show that inviting guests carries a lot more risk than they might think," he says. "This is the first research that I'm aware of that shows that guests can actually gain access to data, not just gain an understanding of your directory or something like that."

## A Two-Step Path to Malicious Azure AD Access

Bargury says the potential exposure can be achieved through a two-step process. The first part of his demonstration at Black Hat USA will show how easy it is to take a guest account with default settings — ones that essentially show access to no applications — and, by using a few cheap manipulations that include creating trial licenses and canceling them, give a guest user visibility into the default environment for Power Apps, which exists in that AAD tenant.

Once that visibility is established, guest users will then be able to see all of the application connections created in Power Apps that have been marked as "shared with everyone" by developers.

"The root cause of the problem I'm showing comes when somebody has created or shared an application using something that Microsoft calls 'share with everyone,'" Bargury notes. "And when you share with everyone, you might think that it's shared with everybody in your org, but essentially it means everyone in your AAD tenant, which includes guests."

In turn, those apps connect to data in the background that could be sensitive.

"These are [resources in Azure AD](https://www.darkreading.com/cloud-security/azure-ad-log-in-with-microsoft-authentication-bypass-affects-thousands). They can be in on-prem, they could be people's own personal accounts that have been overshared across the organization," he says.

By default, just because a guest account could see those connections doesn't necessarily mean they could use them to get at data, thanks to limitations that Microsoft has created through protections like its Power Platform DLP controls. However, Bargury will demonstrate how he's able to get around those protections as the second step of the attack process.

"Once you are in and you can see the things that have been overshared, you need to be able to use them," he says. "I'm using research that has been done by others that allows me to basically reach out to internal Microsoft APIs with existing user authentication. The reason why I'm able to go through each of these connections and dump the data behind them is because I was able to peel off the front-end APIs for Power Platform and figure out the infrastructure behind them. And I'm essentially just reaching out directly to the infrastructure in terms of the front-end APIs, which means that I can a) circumvent defenses; and b) leave no logs."

## Limiting Cyber Risk From Promiscuous Oversharing

Bargury says his talk will sound the alarm on how severe this problem is and also provide the audience with the tools to get a handle on the risk posed by this exposure. He'll also walk the audience through configurations that they can change to limit the scope of guest access in their AAD environment, and he'll talk about how to detect the manipulations that could lead to this toxic oversharing to guest accounts.

"One of the key things that I'm doing here is using research to gain authentication tokens to those internal APIs," he says. "And that's an event that you can configure AAD to log. If you find that the user, especially guest user, has provisioned for themselves an authentication token to an internal Microsoft API that should not be exposed, then this should be a red flag."

As a part of the talk Bargury is going to drop a new tool called PowerGuest, an exploratory auditing tool that will help both blue and red teamers understand the true scope of guest access within an AAD tenant.

The other important point he'll focus on is that defenders really should start to gain a better understanding of the connections and credentials opened up in their AAD environments through Power Apps.

"If you are building things on top of low-code platforms, you need to understand that it's very easy for you to share credentials and identities across different users. When you create an application and you share it with other people, then they end up getting access to the underlying connection, the underlying data source," says Bargury, who tackled this concept in a different piece of research [presented earlier this year at RSA Conference](https://www.darkreading.com/identity-access-management-security/are-low-code-apps-a-ticking-access-control-time-bomb-).

Read more about:

[Black Hat News](https://www.darkreading.com/keyword/black-hat-news)

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/application-security/azure-ad-guests-steal-data-microsoft-power-apps)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/application-security/azure-ad-guests-steal-data-microsoft-power-apps)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/application-security/azure-ad-guests-steal-data-microsoft-power-apps)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/application-security/azure-ad-guests-steal-data-microsoft-power-apps&title=Rogue%20Azure%20AD%20Guests%20Can%20Steal%20Data%20via%20Power%20Apps)[Email](mailto:?subject=Rogue%20Azure%20AD%20Guests%20Can%20Steal%20Data%20via%20Power%20Apps&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Rogue%20Azure%20AD%20Guests%20Can%20Steal%20Data%20via%20Power%20Apps%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fapplication-security%2Fazure-ad-guests-steal-data-microsoft-power-apps)

## About the Author

[![Ericka Chickowski, Contributing Writer](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt53e8e9e7fdab1946/64f178f5e0ecf1629365e905/ErickaC.jpg?width=400&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/author/ericka-chickowski)

[Ericka Chickowski, Contributing Writer](https://www.darkreading.com/author/ericka-chickowski)

Ericka Chickowski specializes in coverage of information technology and business innovation. She has focused on information security for the better part of a decade and regularly writes about the security industry as a contributor to Dark Reading.

[See more from Ericka Chickowski, Contributing Writer](https://www.darkreading.com/author/ericka-chickowski)

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

### Editor's Choice

[Source circles of services available![](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt8b429372f211b1ae/6638d53305cfba61114b4398/Mikko_Lemola-security-services-shutterstock.jpg?width=700&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/cybersecurity-operations/levelblue-trustwave-forms-largest-independent-mssp) [Cybersecurity Operations](https://www.darkreading.com/cybersecurity-operations)

[LevelBlue Acquires Trustwave, Forms World's Largest Independent MSSP](https://www.darkreading.com/cybersecurity-operations/levelblue-trustwave-forms-largest-independent-mssp) [LevelBlue Acquires Trustwave, Forms World's Largest Independent MSSP](https://www.darkreading.com/cybersecurity-operations/levelblue-trustwave-forms-largest-independent-mssp)

by [Jeffrey Schwartz](https://www.darkreading.com/author/jeffrey-schwartz)

Jul 1, 2025

3 Min Read

[Man speaking into a mobile device displaying voice generating app ![](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt5ff5db734c332a51/68642c60bcd8a1819b3deb30/voice_genertator_Tero_Vesalainen_Alamy.jpg?width=700&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/cyberattacks-data-breaches/scope-scale-spurious-north-korean-it-workers) [Cyberattacks & Data Breaches](https://www.darkreading.com/cyberattacks-data-breaches)

[Scope, Scale of Spurious North Korean IT Workers Emerges](https://www.darkreading.com/cyberattacks-data-breaches/scope-scale-spurious-north-korean-it-workers) [Scope, Scale of Spurious North Korean IT Workers Emerges](https://www.darkreading.com/cyberattacks-data-breaches/scope-scale-spurious-north-korean-it-workers)

by [Becky Bracken](https://www.darkreading.com/author/becky-bracken)

Jul 1, 2025

6 Min Read

[A Yes/No questionnaire about spear phishing![](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt3962b0eb0e6077ca/6862a9327a618d39aea36ec8/Spear_phishing_question-Yee_Xin_Tan-Alamy.jpg?width=700&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/endpoint-security/phishing-training-doesnt-work) [Endpoint Security](https://www.darkreading.com/endpoint-security)

[We've All Been Wrong: Phishing Training Doesn't Work](https://www.darkreading.com/endpoint-security/phishing-training-doesnt-work) [We've All Been Wrong: Phishing Training Doesn't Work](https://www.darkreading.com/endpoint-security/phishing-training-doesnt-work)

by [Nate Nelson, Contributing Writer](https://www.darkreading.com/author/nate-nelson)

Jul 1, 2025

6 Min Read

Webinars

- [Think Like a Cybercriminal to Stop the Next Potential Attack](https://dr-resources.darkreading.com/c/pubRD.mpl?secure=1&sr=pp&_t=pp:&qf=w_cmdc03&ch=SBX&cid=_upcoming_webinars_8.500001572&_mc=_upcoming_webinars_8.500001572) Jul 22, 2025
- [Elevating Database Security: Harnessing Data Threat Analytics and Security Posture](https://dr-resources.darkreading.com/c/pubRD.mpl?secure=1&sr=pp&_t=pp:&qf=w_rubr156&ch=SBX&cid=_upcoming_webinars_8.500001574&_mc=_upcoming_webinars_8.500001574) Jul 23, 2025
- [The DOGE-effect on Cyber: What's happened and what's next?](https://www.brighttalk.com/webcast/18975/628444?utm_source=brighttalk-darkreading&utm_medium=web&utm_campaign=curation04242025&cid=_upcoming_webinars_8.500001554&_mc=_upcoming_webinars_8.500001554) Jul 24, 2025
- [Solving ICS/OT Patching and Vulnerability Management Conundrum](https://dr-resources.darkreading.com/c/pubRD.mpl?secure=1&sr=pp&_t=pp:&qf=w_txon82&ch=SBX&cid=_upcoming_webinars_8.500001577&_mc=_upcoming_webinars_8.500001577) Jul 30, 2025
- [Creating a Roadmap for More Effective Security Partnerships](https://dr-resources.darkreading.com/c/pubRD.mpl?secure=1&sr=pp&_t=pp:&qf=w_defa8838&ch=SBX&cid=_upcoming_webinars_8.500001578&_mc=_upcoming_webinars_8.500001578) Aug 14, 2025

[More Webinars](https://www.darkreading.com/resources?types=Webinar)

White Papers

- [XSIAM Buyer's Guide: How to Transform Your SOC for the AI Era](https://dr-resources.darkreading.com/c/pubRD.mpl?secure=1&sr=pp&_t=pp:&qf=w_palo294&ch=SBX&cid=_whitepaper_14.500005977&_mc=_whitepaper_14.500005977)
- [XSIAM Infographic: Talking About a Revolution](https://dr-resources.darkreading.com/c/pubRD.mpl?secure=1&sr=pp&_t=pp:&qf=w_palo292&ch=SBX&cid=_whitepaper_14.500005975&_mc=_whitepaper_14.500005975)
- [Omdia Universe: Selecting a Next-Generation Security Information and Event Management Solution, 2024-25](https://dr-resources.darkreading.com/c/pubRD.mpl?secure=1&sr=pp&_t=pp:&qf=w_palo291&ch=SBX&cid=_whitepaper_14.500005974&_mc=_whitepaper_14.500005974)
- [The State of Workforce Security: Key Insights for IT and Security Leaders](https://dr-resources.darkreading.com/c/pubRD.mpl?secure=1&sr=pp&_t=pp:&qf=w_palo308&ch=SBX&cid=_whitepaper_14.500005966&_mc=_whitepaper_14.500005966)
- [Cortex XSIAM: The Machine-Led, Human-Empowered Security Platform](https://dr-resources.darkreading.com/c/pubRD.mpl?secure=1&sr=pp&_t=pp:&qf=w_palo295&ch=SBX&cid=_whitepaper_14.500005962&_mc=_whitepaper_14.500005962)

[More Whitepapers](https://www.darkreading.com/resources?types=Whitepaper)

Events

- [\[Virtual Event\] Strategic Security for the Modern Enterprise](https://ve.informaengage.com/virtual-events/strategic-security-for-the-modern-enterprise/?ch=sbx&cid=_session_16.500334&_mc=_session_16.500334) Jun 26, 2025
- [\[Virtual Event\] Anatomy of a Data Breach](https://ve.informaengage.com/virtual-events/an-anatomy-of-a-data-breach-and-what-to-do-if-it-happens-to-you/?ch=sbx&cid=_session_16.500333&_mc=_session_16.500333) Jun 18, 2025
- [\[Conference\] Black Hat USA - August 2-7 - Learn More](https://www.blackhat.com/us-25/?_mc=we_bhas25_drcuration&cid=_session_16.500330) Aug 2, 2025

[More Events](https://www.darkreading.com/events)

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
