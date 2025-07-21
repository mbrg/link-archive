---
date: 2022-08-29
description: 'The rise of no-code/low-code platforms affords business users significant
  autonomy but introduces critical cybersecurity risks. This article highlights three
  scenarios that demonstrate potential pitfalls: unauthorized data sharing with vendors,
  mishandling of sensitive information (e.g., credit card details), and evasion of
  corporate email security through automation. These examples underscore the necessity
  for organizations to implement robust security frameworks, educate users about their
  responsibilities, and monitor developments to mitigate risks associated with citizen
  development. Without proper oversight, enterprises risk severe compliance violations
  and data breaches, necessitating a proactive security posture.'
link: https://www.darkreading.com/dr-tech/3-ways-no-code-developers-can-shoot-themselves-in-the-foot
tags:
- data privacy
- SaaS security
- cybersecurity risks
- no-code development
- application security
title: 3 Ways No-Code Developers Can Shoot Themselves in the Foot
---

- [Cyber Risk](https://www.darkreading.com/cyber-risk)

[![DR Technology Logo](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt4c091cd3ac9935ea/653a71456ad0f6040a6f71bd/Dark_Reading_Logo_Technology_0.png?width=700&auto=webp&quality=80&disable=upscale)\\
\\
News, news analysis, and commentary on the latest trends in cybersecurity technology.](https://www.darkreading.com/program/dr-technology)

# 3 Ways No-Code Developers Can Shoot Themselves in the Foot

Low/no-code tools allow citizen developers to design creative solutions to address immediate problems, but without sufficient training and oversight, the technology can make it easy to make security mistakes.

[![Picture of Michael Bargury](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltbd8a249d11a28466/64f150aad5f7ca2f7665bf81/Michael_Bargury_zenity.jpg?width=100&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/author/michael-bargury)

[Michael Bargury](https://www.darkreading.com/author/michael-bargury), CTO & Co-Founder, Zenity

August 29, 2022

6 Min Read

![A blond, blue-eyed child covers his mouth with both hands in an expression of dismay](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt5890cb462abb07b8/64f171005694095f13849643/oops-Roman_Yanushevsky-AdobeStock.jpeg?width=1280&auto=webp&quality=80&format=jpg&disable=upscale)

Source: Roman Yanushevsky via Adobe Stock Photo

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyber-risk/3-ways-no-code-developers-can-shoot-themselves-in-the-foot)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyber-risk/3-ways-no-code-developers-can-shoot-themselves-in-the-foot)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyber-risk/3-ways-no-code-developers-can-shoot-themselves-in-the-foot)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyber-risk/3-ways-no-code-developers-can-shoot-themselves-in-the-foot&title=3%20Ways%20No-Code%20Developers%20Can%20Shoot%20Themselves%20in%20the%20Foot)[Email](mailto:?subject=3%20Ways%20No-Code%20Developers%20Can%20Shoot%20Themselves%20in%20the%20Foot&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%203%20Ways%20No-Code%20Developers%20Can%20Shoot%20Themselves%20in%20the%20Foot%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyber-risk%2F3-ways-no-code-developers-can-shoot-themselves-in-the-foot)

There used to be a time where risk-averse organizations could severely limit their business users' ability to make costly mistakes. With limited technical know-how, strict permissions, and lack of tailwind, the worst thing a business user could do was download malware or fall for a phishing campaign. Those days are now gone.

Nowadays, [every major software-as-a-service (SaaS) platform comes bundled](https://www.darkreading.com/cyber-risk/you-can-t-opt-out-of-citizen-development) with automation and application-building capabilities that are designed for and marketed directly to business users. SaaS platforms like Microsoft 365, Salesforce, and ServiceNow are embedding [no-code/low-code platforms](https://www.darkreading.com/cyber-risk/credential-sharing-as-a-service-hidden-risk-of-low-code-no-code) into their existing offerings, placing them directly in the hands of business users without asking for corporate approval. Capabilities that were once available only to the IT and development teams are now available throughout the organization.

Power Platform, Microsoft's low-code platform, is built into Office 365 and is a great example due to Microsoft's strong foothold in the enterprise and the rate in which it is adopted by business users. Perhaps without realizing it, enterprises are placing developer-level power in the hands of more people than ever before, with far less security or technical savvy. What could possibly go wrong?

Quite a lot, actually. Let's examine a few real-world examples from my experience. The information has been anonymized, and business-specific processes were omitted.

## Situation 1: New Vendor? Just Do It

The customer care team at a multinational retail company wanted to enrich their customer data with consumer insights. In particular, they were hoping to find more information about new customers so that they could better serve them, even during their initial purchase. The customer care team decided on a vendor they would like to work with. The vendor required data to be sent to them for enrichment, which would then be pulled back by their services.

Normally, this is where IT comes into the picture. IT would need to build some sort of integration to get data to and from the vendor. The IT security team would obviously need to be involved, too, to ensure this vendor can be trusted with customer data and approve the purchase. Procurement and legal would have taken a key part, as well. In this case, however, things went in a different direction.

This particular customer care team were Microsoft Power Platform experts. Instead of waiting around for resources or approval, they just went ahead and built the integration themselves: collecting customer data from SQL servers in production, forwarding it all to an FTP server provided by the vendor, and fetching enriched data back from the FTP server to the production database. The entire process was automatically executed every time a new customer was added to the database. This was all done through drag-and-drop interfaces, hosted on Office 365, and using their personal accounts. The license was paid out-of-pocket, which kept procurement out of the loop.

Imagine the CISO's surprise when they found a bunch of business automations moving customer data to a hard-coded IP address on AWS. Being an Azure-only customer, this raised a giant red flag. Furthermore, the data was being sent and received with an insecure FTP connection, creating a security and compliance risk. When the security team found this through a dedicated security tool, data had been moving in and out of the organization for almost a year.

## Situation 2: Ohh, Is It Wrong to Collect Credit Cards?

The HR team at a large IT vendor was preparing for a once-a-year "Give Away" campaign, where employees are encouraged to donate to their favorite charity, with the company pitching in by matching every dollar donated by employees. The previous year's campaign was a massive success, so expectations were through the roof. To power the campaign and alleviate manual processes, a creative HR employee used Microsoft's Power Platform to create an app that facilitated the entire process. To register, an employee would log in to the application with their corporate account, submit their donation amount, select a charity, and provide their credit card details for payment.

The campaign was a huge success, with record-breaking participation by employees and little manual work required from HR employees. For some reason, though, the security team was not happy with the way things turned out. While registering to the campaign, an employee from the security team realized that credit cards were being collected in an app that did not look like it should be doing so. Upon investigation, they found that those credit card details were indeed improperly handled. Credit card details were stored in the default Power Platform environment, which means they were available to the entire Azure AD tenant, including all employees, vendors, and contractors. Furthermore, they were stored as simple plaintext string fields.

Fortunately, the data-processing violation was discovered by the security team before malicious actors — or compliance auditors — spotted it. The database was cleaned up, and the application was patched to properly handle financial information according to regulation.

## Situation 3: Why Can't I Just Use Gmail?

As a user, nobody likes enterprise data loss prevention controls. Even when necessary, they introduce annoying friction to the day-to-day operations. As a result, users have always tried to circumvent them. One perennial tug-of-war between creative business users and the security team is corporate email. Syncing corporate email to a personal email account or corporate calendar to a personal calendar: Security teams have a solution for that. Namely, they put email security and DLP solutions in place to block email forwarding and ensure data governance. This solves the problem, right?

Well, no. [A repeated finding](https://www.zenity.io/blog/low-code-security-and-business-email-compromise-via-email-auto-forwarding/) across large enterprises and small businesses finds that users are creating automations that bypass email controls to forward their corporate email and calendar to their personal accounts. Instead of forwarding emails, they copy and paste data from one service to another. By logging into each service with a separate identity and automating the copy-paste process with no-code, business users bypass security controls with ease — and with no easy way for security teams to find out.

The Power Platform community has even developed [templates](https://powerautomate.microsoft.com/en-us/templates/details/b1dab790d27011e6a4d6dd74e8f2382f/daily-copy-all-outlook-contacts-to-google-contacts/) that any Office 365 user can pick up and use.

## With Great Power Comes Great Responsibility

Business user empowerment is great. Business lines should not be waiting for IT or fighting for development resources. However, we can't just give business users developer-level power with no guidance or guardrails and expect that everything will be alright.

Security teams need to educate business users and make them aware of their new responsibilities as application developers, even if those applications were built using "no code." Security teams should also put guardrails and monitoring in place to ensure that when business users make a mistake, like we all do, it will not snowball into full-blown data leaks or compliance audit incidents.

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyber-risk/3-ways-no-code-developers-can-shoot-themselves-in-the-foot)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyber-risk/3-ways-no-code-developers-can-shoot-themselves-in-the-foot)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyber-risk/3-ways-no-code-developers-can-shoot-themselves-in-the-foot)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyber-risk/3-ways-no-code-developers-can-shoot-themselves-in-the-foot&title=3%20Ways%20No-Code%20Developers%20Can%20Shoot%20Themselves%20in%20the%20Foot)[Email](mailto:?subject=3%20Ways%20No-Code%20Developers%20Can%20Shoot%20Themselves%20in%20the%20Foot&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%203%20Ways%20No-Code%20Developers%20Can%20Shoot%20Themselves%20in%20the%20Foot%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyber-risk%2F3-ways-no-code-developers-can-shoot-themselves-in-the-foot)

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
