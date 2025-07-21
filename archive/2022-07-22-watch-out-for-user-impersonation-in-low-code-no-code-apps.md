---
date: 2022-07-22
description: A recent article highlights significant cybersecurity risks associated
  with user impersonation in low-code/no-code applications. As employees bypass security
  protocols by sharing credentials for convenience, organizations face compromised
  user identities, undermining access control and compliance frameworks. A case study
  illustrates how such credential sharing led to security incidents, prompting a reevaluation
  of application design to safeguard user identities. This trend underscores the necessity
  for security teams to engage in the development of low-code applications, as they
  present unique risks that could exacerbate existing vulnerabilities within enterprise
  IT infrastructures.
link: https://www.darkreading.com/edge-articles/watch-out-for-user-impersonation-in-low-code-no-code-apps
tags:
- Identity Management
- Credential Sharing
- User Impersonation
- Low-Code Development
- Cybersecurity
title: Watch Out for User Impersonation in Low-Code/No-Code Apps
---

- [Cyber Risk](https://www.darkreading.com/cyber-risk)

[![The Edge Logo](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt530eb1f4e672eb44/653a71690e92cc040a3e9d6d/Dark_Reading_Logo_TheEdge_0.png?width=700&auto=webp&quality=80&disable=upscale)\\
\\
Cybersecurity In-Depth: Feature articles on security strategy, latest trends, and people to know.](https://www.darkreading.com/program/the-edge)

# Watch Out for User Impersonation in Low-Code/No-Code Apps

How a well-meaning employee could unwittingly share their identity with other users, causing a whole range of problems across IT, security, and the business.

[![Picture of Michael Bargury](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltbd8a249d11a28466/64f150aad5f7ca2f7665bf81/Michael_Bargury_zenity.jpg?width=100&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/author/michael-bargury)

[Michael Bargury](https://www.darkreading.com/author/michael-bargury), CTO & Co-Founder, Zenity

July 18, 2022

7 Min Read

![Photo of two young white men wearing identical red and white fox masks and patterned blue shirts on a yellow background](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltdeeffb6cf9d2216e/64f152bdec1d256ed9a6a839/identicalmasks-nito-alamy.jpg?width=1280&auto=webp&quality=80&format=jpg&disable=upscale)

Source: nito via Alamy Stock Photo

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyber-risk/watch-out-for-user-impersonation-in-low-code-no-code-apps)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyber-risk/watch-out-for-user-impersonation-in-low-code-no-code-apps)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyber-risk/watch-out-for-user-impersonation-in-low-code-no-code-apps)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyber-risk/watch-out-for-user-impersonation-in-low-code-no-code-apps&title=Watch%20Out%20for%20User%20Impersonation%20in%20Low-Code%2FNo-Code%20Apps)[Email](mailto:?subject=Watch%20Out%20for%20User%20Impersonation%20in%20Low-Code/No-Code%20Apps&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Watch%20Out%20for%20User%20Impersonation%20in%20Low-Code%2FNo-Code%20Apps%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyber-risk%2Fwatch-out-for-user-impersonation-in-low-code-no-code-apps)

Last month I wrote [an article](https://www.darkreading.com/cyber-risk/credential-sharing-as-a-service-hidden-risk-of-low-code-no-code) about the way low-code/no-code platforms are offering credential-sharing as a service, why they are doing it, and how this looks from [an attacker's perspective](https://www.zenity.io/blog/why-are-low-code-platforms-becoming-the-new-holy-grail-of-cyberattackers/). In this article, I'll focus on the implications of that compromise and how it affects enterprises today.

Here's why sharing your enterprise credentials with somebody else is bad practice. Say I want to pass my credentials to a colleague in order to query production logs for some one-off user-behavior analysis. In a typical enterprise, granting someone permissions to query a new data source could mean a long access review process, especially when it comes to production or sensitive data. My colleague could easily get frustrated. "All I wanted is to do this tiny one-off query, and I've already been waiting for a month!" they could say. I could just run the query for them, but I'm swamped with my own day-to-day tasks, and one-off queries tend to get complicated.

I am left with one quick solution: I could just share my username/password with my colleague. If they get an MFA challenge, I'll gladly approve. I don't have to spend the time running the query, and my colleague gets unblocked. Everybody wins! Right?

Well, you would be right in your analysis, but you are missing the bigger picture. While it's important for the enterprise that your colleague gets their user behavior analysis done, it is equally, if not more, important that your enterprise remains compliant with a whole host of privacy and security standards and maintains customer trust by upkeeping the company's commitment to security.

If high-level enterprise goals do not convince you, consider the central management teams in IT or security. Those teams base their operations and security strategies on the fact that each user has their own unique identity. IT teams are setting up networking and access policies that assume each user would be logged in from one corporate IP or corporate laptop at once; security teams are correlating events based on user ID; finance teams could be aggregating cost reports per user and their personal cloud environment. Credential sharing undermines all of those assumptions, among others. It strips away the basic meaning of an online identity.

## A Real-World Example

Let's turn to the world of low-code/no-code and examine a real-world scenario. In a large enterprise, Jane, an inspired employee from the customer care team, realized that when employees across the organization take part in a customer case, they are usually missing key information about the customer, such as their support case history and latest purchases. This degrades the customer's experience, since they have to explain their issue again and again while the case gets routed to the right employee who can address the issue.

To improve this, Jane created an app that allows company employees to view this key information about customers when those employees are part of the team responsible for addressing the customer's support case. First, let's take a moment to acknowledge the power of low-code/no-code, which allows Jane to identify a need and address it on her own, without asking for a budget or waiting for IT resource allocations.

While building the application, Jane had to work around multiple issues, the biggest one being permissions. Employees across the organization don't have direct access to query the customer database to get the information they need. If they did, then Jane wouldn't have to build this application. To overcome this issue, Jane logged into the database and embedded her authenticated session directly in the application. When the application receives a request from one user, it will use Jane's identity to execute that query and then return the results to the user. This credential-embedding feature, [as we explored last month](https://www.darkreading.com/cyber-risk/credential-sharing-as-a-service-hidden-risk-of-low-code-no-code), is a key feature of low-code/no-code platforms. Jane made sure to set up role-based access control (RBAC) in the application such that every user can only access customer cases they are assigned to.

The application solved an important business problem, and so it quickly gained user adoption across the enterprise. People were happy that they could provide better service to their customers by having the right context for the conversation. Customers were happy, too. A month after Jane created the application, it was already used by hundreds of users across the organization, with customer satisfaction rates rising.

Meanwhile at the SOC, a high-severity alert showing abnormal activity around the production customer database was triggered and assigned to Amy, an experienced security analyst. Amy's initial investigation showed an internal user was trying to scrape the entire database, querying information about multiple customers from multiple IP addresses across the organization. The query pattern was very complex; instead of a simple enumeration pattern you would expect to see when a database is being scraped, the same customer's data was queried multiple times, sometimes through different IP addresses and on different dates. Could this be an attacker trying to confuse the security monitoring systems?

After a quick investigation, Amy uncovered a crucial piece of information: All of those queries across all IP addresses and dates were using a single user identity, someone named Jane from the customer care team.

Amy reached out to Jane to ask her what's going on. At first, Jane didn't know. Were her credentials stolen? Did she click on the wrong link or trust the wrong incoming email? But when Jane told Amy about the application she recently built, they both realized there might be a connection. Amy, the SOC analyst, wasn't familiar with low-code/no-code, so they reached out to the AppSec team. With Jane's help, the team figured out that Jane's application had Jane's credentials embedded within it. From the database's perspective, there was no application — there was just Jane, executing a whole lot of queries.

Jane, Amy, and the AppSec team decided to shut down the application until a solution was found. Application users across the organization were frustrated since they had come to rely on it, and customers were feeling it, too.

While Amy closed the issue and documented their findings, the VP of customer care was not happy seeing customer satisfaction rate drop, so they asked Jane to look for a permanent solution. With the help of the platform's documentation and the organization's Center of Excellence team, Jane removed her embedded identity from the application, changed the app to use each user's identity to query the database, and ensured users gain permissions only to customer cases they are associated with. In its new and improved version, the application used each user's identity to query the customer database. Jane and the application users were happy that the application is back online, Amy and the AppSec team were happy that Jane's identity is no longer shared, and the enterprise saw customer satisfaction rate starting to climb up again. All was well.

Two weeks later, the SOC received another alert on abnormal access to the production customer database. It looked suspiciously similar to the previous alert on that same database. Again, IP addresses from across the organization were using a single user's identity to query the database. Again, that user was Jane. But this time, the security team and Jane knew that the app uses its user's identities. What's going on?

The investigation revealed that the original app had [implicitly shared](https://docs.microsoft.com/en-us/power-apps/maker/canvas-apps/share-app-resources#implicit-sharing) Jane's authenticated database session with the app's users. By sharing the app with a user, that user got direct access to the connection, a wrapper around an authenticated database session provided by the low-code/no-code's platform. Using that connection, users could leverage the authenticated session directly — they no longer had to go through the app. It turns out that several users had found this out and, thinking that this was the intended behavior, were using Jane's authenticated database session to run their queries. They loved this solution, since using the connection directly gave them full access to the database, not just for customer cases that they are assigned to.

The connection was deleted, and the incident was over. The SOC analyst reached out to users who had used Jane's connection to ensure they discarded any customer data they have stored.

## Addressing the Low-Code/No-Code Security Challenge

The story above is a real-life scenario from a multinational B2C company. Some details were omitted or adjusted to protect privacy. We've seen how a well-meaning employee could unwittingly share their identity with other users, causing a whole range of problems across IT, security, and the business. As we explored last month, credential-sharing is a key feature of low-code/no-code. It's the norm, not the exception.

As [low-code/no-code continues to bloom in the enterprise, consciously or not](https://www.darkreading.com/cyber-risk/you-can-t-opt-out-of-citizen-development), it is crucial for security and IT teams to join the business development conversation. Low-code/no-code apps come with a [unique set of security challenges](https://owasp.org/www-project-top-10-low-code-no-code-security-risks/), and their prolific nature means those challenges become acute faster than ever before.

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/cyber-risk/watch-out-for-user-impersonation-in-low-code-no-code-apps)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/cyber-risk/watch-out-for-user-impersonation-in-low-code-no-code-apps)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/cyber-risk/watch-out-for-user-impersonation-in-low-code-no-code-apps)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/cyber-risk/watch-out-for-user-impersonation-in-low-code-no-code-apps&title=Watch%20Out%20for%20User%20Impersonation%20in%20Low-Code%2FNo-Code%20Apps)[Email](mailto:?subject=Watch%20Out%20for%20User%20Impersonation%20in%20Low-Code/No-Code%20Apps&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20Watch%20Out%20for%20User%20Impersonation%20in%20Low-Code%2FNo-Code%20Apps%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fcyber-risk%2Fwatch-out-for-user-impersonation-in-low-code-no-code-apps)

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
