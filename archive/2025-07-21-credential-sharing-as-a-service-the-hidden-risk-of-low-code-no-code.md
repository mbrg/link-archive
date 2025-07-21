---
date: '2025-07-21'
description: The article emphasizes the security vulnerabilities associated with low-code/no-code
  platforms, particularly regarding credential sharing and identity management. It
  highlights that these platforms facilitate embedding user identities in applications,
  thereby increasing the risk of credential leakage—often the primary entry point
  for cyberattacks. The authors argue that this circumvention of traditional identity
  models compromises security oversight, leading to issues like impersonation and
  unauthorized access. Consequently, organizations must adapt their security frameworks
  to address these emergent risks, balancing rapid application development with strategic
  identity governance.
link: https://www.darkreading.com/dr-tech/credential-sharing-as-a-service-hidden-risk-of-low-code-no-code
tags:
- Application Security
- Credential Leakage
- Low-Code/No-Code
- Identity Management
- Cybersecurity
title: 'Credential Sharing as a Service: The Hidden Risk of Low-Code/No-Code'
---

- [Cyber Risk](https://www.darkreading.com/cyber-risk)

[![DR Technology Logo](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt4c091cd3ac9935ea/653a71456ad0f6040a6f71bd/Dark_Reading_Logo_Technology_0.png?width=700&auto=webp&quality=80&disable=upscale)\\
\\
News, news analysis, and commentary on the latest trends in cybersecurity technology.](https://www.darkreading.com/program/dr-technology)

# Credential Sharing as a Service: The Hidden Risk of Low-Code/No-Code

Low-code/no-code platforms allow users to embed their existing user identities within an application, increasing the risk of credentials leakage.

[![Picture of Michael Bargury](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltbd8a249d11a28466/64f150aad5f7ca2f7665bf81/Michael_Bargury_zenity.jpg?width=100&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/author/michael-bargury)

[Michael Bargury](https://www.darkreading.com/author/michael-bargury), CTO & Co-Founder, Zenity

June 20, 2022

8 Min Read

![Illustration of two hands typing on a laptop with floating screen display of profile login information](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt097d7736537417aa/64f153edb87aa7d03b15b08e/credentials-NicoElNino-AdobeStock.jpeg?width=1280&auto=webp&quality=80&format=jpg&disable=upscale)

Source: NicoElNino via Adobe Stock

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyber-risk/credential-sharing-as-a-service-hidden-risk-of-low-code-no-code)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyber-risk/credential-sharing-as-a-service-hidden-risk-of-low-code-no-code)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyber-risk/credential-sharing-as-a-service-hidden-risk-of-low-code-no-code)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyber-risk/credential-sharing-as-a-service-hidden-risk-of-low-code-no-code&title=Credential%20Sharing%20as%20a%20Service%3A%20The%20Hidden%20Risk%20of%20Low-Code%2FNo-Code)[Email](mailto:?subject=Credential%20Sharing%20as%20a%20Service:%20The%20Hidden%20Risk%20of%20Low-Code/No-Code&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Credential%20Sharing%20as%20a%20Service%3A%20The%20Hidden%20Risk%20of%20Low-Code%2FNo-Code%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyber-risk%2Fcredential-sharing-as-a-service-hidden-risk-of-low-code-no-code)

According to the "[2022 Verizon Data Breach Investigations Report](https://www.verizon.com/business/resources/reports/dbir/)," stolen credentials were the top path leading to data breaches. More often than phishing or exploiting vulnerabilities, attackers gain direct access to credentials, letting them virtually walk into victim organizations using the front door.

Low-code/no-code platforms make it extremely easy for users to share their credentials and embed their credentials into applications, thus drastically increasing the risk that employee mistakes will result in credentials leakage. Unintentionally, low-code/no-code development makes the No. 1 resource for attackers easier to obtain.

## How Low-Code/No-Code Platforms Sacrifice Security For Productivity

Getting the required permissions to do your job in an enterprise can be very frustrating. It's not uncommon for new employees to wait more than a month before they have the full scope of permissions they need to access business data, review KPI dashboards, or join an internal communication channel.

The same thing is true, maybe even worse, for setting up a new application in the enterprise. Permissions requests typically need to be approved by your direct manager, their manager, and the team who owns the data/service. Some of the approvers might be in another continent with a time zone difference. It's next to impossible to start building an application without the required access to data/services, and so you end up waiting.

After you manage to get the right access for your application, you are finally ready to start building. A few months go by. Suddenly, you get a notification that your application has failed. A quick analysis shows that its permissions have been revoked. Enterprises typically set up an automated process that revokes access every few months, unless permissions are explicitly asked for by the application maker. This process is necessary to comply with regulations and reduce over-permissions, but it has its downsides — namely a periodic manual process that could hinder productivity.

Low-code/no-code is an attempt to empower every employee, especially business professionals, to address their own issues with custom-built applications and automations. Vendors do this by systematically identifying and removing roadblocks for building applications. Is learning to code challenging or scary? A drag-and-drop interface can help lower the barrier to entry. Is integration difficult? A wide range of managed connectors will remove the need to know what an application programming interface (API) is or how to interact with it. Is asking for permissions slowing you down? Sharing identities and leveraging existing user access can provide a quick alternative.

To boost innovation, low-code/no-code platforms allow their users to leverage their existing user identity, embed it within an application, and by doing so circumvent the enterprise permissions model entirely. For an outside viewer in security or IT, the application doesn't exist, and everyone using it is actually running it on its maker's account.

## Wait, But How?

If you're thinking that there are better solutions out there than letting the application impersonate its maker, you are partially right.

In recent years, OAuth has been the de-facto standard for granting application access. Any time you go to a software-as-a-service (SaaS) marketplace, pick up a third-party integration, and get prompted with a small login and consent pop-up, you're most likely using OAuth. OAuth has many different consent flows, all resulting in the familiar pop-up experience. A key distinction is whether consent is granted to the application directly or on behalf of its currently signed-in user. Although this might sound like a minor detail, it is actually the root cause of the low-code/no-code identity problem.

When an application is granted consent directly, it is issued its own identity, separate from that of the user who granted the consent. The application identity can be monitored for suspicious authentication or access patterns, and its permissions can be revoked at any time by a security or IT admin. Controls like IP restriction can be put in place to take advantage of the static nature of the infrastructure that the application runs on. Every application can have a separate identity, with separate access restrictions, and can be monitored and acted up--on separately. Another useful implication of application identity is admin control.

Granting consent on behalf of the currently signed-in application user, however, has very different implications. The application gains access to resources using its user's identity for the limited time when the user uses the app. On-behalf access means that the application is actually using its user's identity directly when querying external resources. Moreover, using multiple applications will result in all of them using the same identity: the user's identity. IT or security admins looking at logs will not be able to easily distinguish between the user or any application used by the user. Granting application access on behalf of users was originally designed to allow temporary access only while a user is actively using the application.

In many cases, services allow applications to gain access on behalf of users but deny applications direct access to service APIs. This raises an interesting question: If an application can only gain access to data on behalf of a user, how can it access data when no user is interacting with it? Creative engineers have come up with a solution. The application logs in as a user once, then records its authentication token and keeps on using it even after the user has logged off the application. In the case of low-code/no-code applications, that user is typically the application's creator. User authentication tokens are supposed to be short-lived in order to prevent this workaround. In practice, however, most services issue tokens that are valid for 12 months.

Let's say a business professional creates an application. Instead of having to wait for approval of an application identity or permissions, they use access on behalf of a user — in this case, their own. The application requires them to log in once (say to Salesforce or SharePoint), records their own private authentication token, and reuses it at will. Even if another user is using the application, it will still use its maker's identity.

There are ways to build low-code/no-code applications with dedicated identities — for example, by using service accounts. However, the methods are not very widely used.

Recall the positive properties of application identity stated above: The application can be monitored, its access to data can be controlled, and its privileges can be revoked. None of this is true when low-code/no-code platforms are embedded with their creator's identity. Every application a business professional makes might have their user identity built into it. Security and IT teams analyzing access logs will have no way to know that these applications even exist.

## Impersonation-as-a-Service

Recording and replaying user authentication tokens as a way to grant applications access to resources has another implication: They open the door to simple and easy identity sharing among users. This manifests in a common low-code/no-code feature typically referred to as connections. Connections are how low-code/no-code applications gain access to resources like Slack, NetSuite, or BambooHR. They allow read operations, like reading employee HR data; write operations, like the ERP on recent sales; and delete operations, like permanently deleting a Slack channel. Connections are first-class objects, which means they can be created by one user and shared with another user, an entire team, or even an entire organization. Technically speaking, these are wrappers around user authentication tokens or hard-coded credentials.

When a user creates and shares a connection to Microsoft Office, for example, it is akin to them sharing their password. However, if a team of developers is collaborating on a project, they often need to be able to share an application identity with each other. Connection sharing enables working together in a team on a shared project, but unfortunately it can also enable users to share their identities with each other. Since many low-code/no-code applications are built with the creator's identity embedded within, identity sharing is [a common risk low-code/no-code platforms introduce](https://owasp.org/www-project-top-10-low-code-no-code-security-risks/).

To make matters worse, credential sharing is just way too easy on many platforms. A single checkbox stands between you and sharing your identity — for example, your ServiceNow or Salesforce account — with your entire organization. In some cases, sharing an application with other users implicitly shares its underlying connections too.

This is a crucial point. Under certain circumstances, users who gain access to a business application will gain direct access to its underlying database implicitly, without direct consent or knowledge. Take an expense management application, for example. There's a big difference between letting people use the application to submit their expense reports and giving them access to the underlying database with everyone's expense reports within it.

Unintentionally, low-code/no-code applications make credentials — the No. 1 resource that attackers are after — [easier to obtain](https://www.zenity.io/blog/why-are-low-code-platforms-becoming-the-new-holy-grail-of-cyberattackers/).

## Where Do We Go From Here?

As we've seen, low-code/no-code platforms had to overcome many challenges in making enterprise applications easy to build for everyone from professional to business developers. Sometimes, the solutions come at a cost. In the case of credentials, the ability to move fast is unfortunately coupled with the ability to break things — namely, the enterprise identity model.

It is important to mention here the immense value that low-code/no-code platforms create for the enterprise: reducing the time between idea and execution, lowering the bar for application development, and increasing business velocity.

Platforms cannot be expected to resolve security concerns on their own; it is [a responsibility shared](https://www.darkreading.com/cyber-risk/addressing-the-low-code-security-elephant-in-the-room) between the platform and its customers. To reduce the risk, security teams should familiarize themselves with the ways identities are treated as part of the low-code/no-code platforms their organizations use. Most platforms can be configured to reduce the level of credential sharing and turn off implicit sharing.

More importantly, security teams must realize that [low-code/no-code platforms introduce an inherent new risk into the enterprise](https://www.darkreading.com/cyber-risk/why-so-many-security-experts-are-concerned-about-low-code-no-code-apps) that cannot be mitigated by traditional monitoring approaches because of the confusion between application and user identities. Therefore, security teams should invest in guiding business developers, reviewing potentially risky applications, and taking action to mitigate risk.

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyber-risk/credential-sharing-as-a-service-hidden-risk-of-low-code-no-code)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyber-risk/credential-sharing-as-a-service-hidden-risk-of-low-code-no-code)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyber-risk/credential-sharing-as-a-service-hidden-risk-of-low-code-no-code)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyber-risk/credential-sharing-as-a-service-hidden-risk-of-low-code-no-code&title=Credential%20Sharing%20as%20a%20Service%3A%20The%20Hidden%20Risk%20of%20Low-Code%2FNo-Code)[Email](mailto:?subject=Credential%20Sharing%20as%20a%20Service:%20The%20Hidden%20Risk%20of%20Low-Code/No-Code&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Credential%20Sharing%20as%20a%20Service%3A%20The%20Hidden%20Risk%20of%20Low-Code%2FNo-Code%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyber-risk%2Fcredential-sharing-as-a-service-hidden-risk-of-low-code-no-code)

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
