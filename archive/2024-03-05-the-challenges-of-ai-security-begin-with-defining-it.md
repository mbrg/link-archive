---
date: 2024-03-05
description: Michael Bargury discusses the evolving landscape of AI security, highlighting
  the lack of consensus on definitions and practices. Key challenges include achieving
  visibility over AI applications, preventing data leaks, controlling AI models, and
  ensuring the security of AI systems. Current security frameworks may struggle to
  address these issues, as AI's dynamic nature complicates traditional prevention
  methods. The article emphasizes the necessity for organizations to adapt security
  strategies to accommodate AI, underscoring the need for further development in this
  domain. This evolving threat landscape calls for ongoing discussion and innovation
  in AI security methodologies.
link: https://www.darkreading.com/application-security/the-challenges-of-ai-security-begin-with-defining-it
tags:
- Data Protection
- AI Security
- Data Leak Prevention
- Application Security
- Cybersecurity Trends
title: The Challenges of AI Security Begin With Defining It
---

- [Application Security](https://www.darkreading.com/application-security)
- [Cyber Risk](https://www.darkreading.com/cyber-risk)
- [Data Privacy](https://www.darkreading.com/cyber-risk/data-privacy)

[![DR Technology Logo](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt4c091cd3ac9935ea/653a71456ad0f6040a6f71bd/Dark_Reading_Logo_Technology_0.png?width=700&auto=webp&quality=80&disable=upscale)\\
\\
News, news analysis, and commentary on the latest trends in cybersecurity technology.](https://www.darkreading.com/program/dr-technology)

# The Challenges of AI Security Begin With Defining It

Security for AI is the Next Big Thing! Too bad no one knows what any of that really means.

[![Picture of Michael Bargury](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltbd8a249d11a28466/64f150aad5f7ca2f7665bf81/Michael_Bargury_zenity.jpg?width=100&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/author/michael-bargury)

[Michael Bargury](https://www.darkreading.com/author/michael-bargury), CTO & Co-Founder, Zenity

March 5, 2024

4 Min Read

![A fully automated police robot stands at a charging station in Terminal T4 at Singapore Changi International Airport](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt521637665481bcc9/65dfe9cfea879b040a14fbb9/policerobot-Agencja_Fotograficzna_Caro-alamy.jpg?width=1280&auto=webp&quality=80&format=jpg&disable=upscale)

Source: Agencja Fotograficzna Caro via Alamy Stock Photo

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/application-security/the-challenges-of-ai-security-begin-with-defining-it)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/application-security/the-challenges-of-ai-security-begin-with-defining-it)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/application-security/the-challenges-of-ai-security-begin-with-defining-it)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/application-security/the-challenges-of-ai-security-begin-with-defining-it&title=The%20Challenges%20of%20AI%20Security%20Begin%20With%20Defining%20It)[Email](mailto:?subject=The%20Challenges%20of%20AI%20Security%20Begin%20With%20Defining%20It&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20The%20Challenges%20of%20AI%20Security%20Begin%20With%20Defining%20It%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fapplication-security%2Fthe-challenges-of-ai-security-begin-with-defining-it)

As artificial intelligence (AI) continues to grab everyone's attention, security for AI has become a popular topic in the marketplace of ideas. Security for AI is capturing the media cycle, AI security startups are coming out of stealth left and right, and incumbents are scrambling to release AI-relevant security features. It is clear security teams are concerned about AI.

But what does "AI security" mean, exactly?

Frankly, we don't really know what security for AI means yet because we still don't know what AI development means. "Security for X" typically arrives after X has matured — think cloud, network, Web apps — but AI remains a moving target.

Still, there are a few distinct problem categories emerging as a part of AI security. These line up with the concerns of different roles within an organization, so it is unclear whether they easily merge, though of course they do have some overlap.

These problems are:

1. Visibility

2. Data leak prevention

3. AI model control

4. Building secure AI applications


Let's tackle them one at a time.

## 1\. Visibility

Security always starts with visibility, and securing AI applications is no different. Chances are many teams in your organization are using and building AI applications right now. Some might have the knowledge, resources, and security savviness to do it right, but others probably don't. Each team could be using a different technology to build their applications and applying different standards to ensure they work correctly. To standardize practices, some organizations create specialized teams to [inventory and review all AI applications](https://www.darkreading.com/application-security/security-must-empower-ai-developers-now). While that is not an easy task in the enterprise, visibility is important enough to begin this process.

## 2\. Data Leak Prevention

When ChatGPT was first launched, many enterprises went down the same route of desperately trying to block it. Every week new headlines emerged about companies losing their intellectual property to AI because an employee copy-pasted highly confidential data to the chat so they could ask for a summary or a funny poem about it. This was really all anybody could talk about for a few weeks.

Since you cannot control ChatGPT or any of the other AIs that appear on the consumer market, this has become a sprawling challenge. Enterprises issue acceptable use policies with approved enterprise AI services, but those are not easy to enforce. This problem got so much attention that OpenAI, which caused the scare in the first place, changed its policies to allow [users to opt out](https://techcrunch.com/2023/03/01/addressing-criticism-openai-will-no-longer-use-customer-data-to-train-its-models-by-default/) of being included in the training set and for [organizations to pay](https://openai.com/chatgpt/enterprise) to opt out on behalf of all their users.

This issue — users pasting the wrong information into an app it does not belong to — seems similar to what [data loss prevention (DLP)](https://www.darkreading.com/endpoint-security/infosec-101-why-data-loss-prevention-important-enterprise-defense) and [cloud access security broker (CASB)](https://www.darkreading.com/cloud-security/designing-a-security-strategy-for-defending-multicloud-architectures) solutions were created to solve. Whether enterprises can use these tools created for conventional data to protect data within AI remains to be discovered.

## 3\. AI Model Control

Think about SQL injection, which boosted the [application security testing](https://www.darkreading.com/vulnerabilities-threats/continuous-scanning-is-imperative-for-effective-web-application-security) industry. It arises when data is translated as instructions, resulting in allowing people who manipulate application data (i.e., users) to manipulate application instruction (i.e., its behavior). With years of severe issues wreaking havoc on Web applications, application development frameworks have risen to the challenge and now safely handle user input. If you're using a modern framework and going through its paved road, SQL injection is for all practical purposes a solved problem.

One of the weird things about AI from an engineer's perspective is that it mixes instructions and data. You tell the AI what you want it to do with text, and then you let your users add some more text into essentially the same input. As you would expect, this results in users being able to change the instructions. Using clever prompts lets you do that even if the application builder really tried to prevent it, a problem we all know today as [prompt injection](https://simonwillison.net/series/prompt-injection/).

For AI application developers, trying to control these uncontrollable models is a real challenge. This is a security concern, but it is also a predictability and usability concern.

## 4\. Building Secure AI Applications

Once you allow AI to act on the user's behalf and chain those actions one after the other, you’ve reached uncharted territory. Can you really tell whether the AI is doing things it should be doing to meet its goal? If you could think of and list everything the AI might need to do, then you arguably wouldn't need AI in the first place.

Importantly, this problem is about [how AI interacts with the world](https://www.zenity.io/microsoft-copilot-studio-vulnerabilities-explained/), and so it is as much about the world as it is about the AI. Most Copilot apps are proud to inherit existing security controls by impersonating users, but are user security controls really all that strict? Can we really count on user-assigned and managed permissions to protect sensitive data from a curious AI?

## A Finishing Thought

Trying to say anything about where AI or by extension AI security will end up is trying to predict the future. As the Danish proverb says, it's difficult to make predictions, especially about the future. As AI development and usage continue to evolve, the security landscape [is bound to evolve with them](https://www.darkreading.com/cyber-risk/move-fast-and-break-the-enterprise-with-ai).

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/application-security/the-challenges-of-ai-security-begin-with-defining-it)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/application-security/the-challenges-of-ai-security-begin-with-defining-it)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/application-security/the-challenges-of-ai-security-begin-with-defining-it)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/application-security/the-challenges-of-ai-security-begin-with-defining-it&title=The%20Challenges%20of%20AI%20Security%20Begin%20With%20Defining%20It)[Email](mailto:?subject=The%20Challenges%20of%20AI%20Security%20Begin%20With%20Defining%20It&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20The%20Challenges%20of%20AI%20Security%20Begin%20With%20Defining%20It%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fapplication-security%2Fthe-challenges-of-ai-security-begin-with-defining-it)

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
