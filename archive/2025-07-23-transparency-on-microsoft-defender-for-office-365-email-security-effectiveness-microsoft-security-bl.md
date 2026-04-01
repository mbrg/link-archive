---
date: '2025-07-23'
description: Microsoft announces enhanced transparency for Defender for Office 365,
  launching a customer dashboard to illustrate email security efficacy and two comparative
  benchmarking reports. These initiatives aim to empower organizations with data on
  threat detection capabilities—one report evaluates Integrated Cloud Email Security
  (ICES) solutions that operate post-Defender, while the other assesses Secure Email
  Gateways (SEGs) filtering pre-delivery. Utilizing real-world data, Microsoft highlights
  effectiveness variances, revealing Defender for Office 365 as superior in threat
  detection. This commitment to transparent metrics aids CISOs in informed decision-making
  amidst evolving cyber threats.
link: https://www.microsoft.com/en-us/security/blog/2025/07/17/transparency-on-microsoft-defender-for-office-365-email-security-effectiveness/
tags:
- Transparency in Security
- Microsoft Defender
- Benchmarking
- Email Security
- Cybersecurity
title: Transparency on Microsoft Defender for Office 365 email security effectiveness
  ◆ Microsoft Security Blog
---

[Skip to content](https://www.microsoft.com/en-us/security/blog/2025/07/17/transparency-on-microsoft-defender-for-office-365-email-security-effectiveness/#wp--skip-link--target)

Skip to main content

![](https://www.microsoft.com/en-us/security/blog/wp-content/themes/security-blog-2025/dist/images/single-bg.jpg)

![](https://www.microsoft.com/en-us/security/blog/wp-content/themes/security-blog-2025/dist/images/single-bg-dark.jpg)

* * *

## Share

- [Link copied to clipboard!](https://www.microsoft.com/en-us/security/blog/2025/07/17/transparency-on-microsoft-defender-for-office-365-email-security-effectiveness/)
- [Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https://www.microsoft.com/en-us/security/blog/2025/07/17/transparency-on-microsoft-defender-for-office-365-email-security-effectiveness/)
- [Share on X](https://twitter.com/intent/tweet?url=https://www.microsoft.com/en-us/security/blog/2025/07/17/transparency-on-microsoft-defender-for-office-365-email-security-effectiveness/&text=Transparency+on+Microsoft+Defender+for+Office+365+email+security+effectiveness)
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https://www.microsoft.com/en-us/security/blog/2025/07/17/transparency-on-microsoft-defender-for-office-365-email-security-effectiveness/)

## Content types

- [News](https://www.microsoft.com/en-us/security/blog/content-type/news/)

## Products and services

- [Microsoft Defender](https://www.microsoft.com/en-us/security/blog/product/microsoft-defender/)
- [Microsoft Defender for Office 365](https://www.microsoft.com/en-us/security/blog/product/microsoft-defender-for-office-365/)

## Topics

- [Email security](https://www.microsoft.com/en-us/security/blog/topic/email-security/)

more

In today’s world, cyberattackers are relentless. They are often well-resourced, highly sophisticated, and constantly innovating, which means the effectiveness of cybersecurity solutions must be continuously evaluated, not assumed. Yet, despite the critical role email security plays in protecting organizations, there is limited transparency and standardization in how email security effectiveness is measured and communicated. This makes it challenging for chief information security officers (CISOs) and security architects to make decisions based on data.

At Microsoft, we believe that transparency is foundational to trust. As both an email platform and a security provider, we want to work together with our ecosystem and do more to empower customers to understand email security effectiveness. Today, we’re announcing two initiatives to support that objective.

First, to provide [Microsoft Defender for Office 365](https://www.microsoft.com/security/business/siem-and-xdr/microsoft-defender-office-365) customers with richer data on its efficacy, we are releasing a new customer-facing dashboard that will provide visibility on our effectiveness across a range of threat vectors.

Second, we are releasing two comparative benchmarking reports designed to assist customers in evaluating the benefits of integrating multiple email security solutions. The first describes the protection value added by Integrated Cloud Email Security (ICES) vendors, which detect and remediate threats after Microsoft Defender for Office 365. The second describes the value of Secure Email Gateways (SEGs), which filter emails before they reach Microsoft Defender for Office 365. These reports are based on real-world threat data rather than synthetic tests to provide an objective basis for comparison at scale.

Security is a team sport, and we are grateful to our entire ecosystem for working together on protecting our customers. We encourage customers to see how the solutions deployed in their tenants are collectively performing for their needs.

## Introducing the Defender for Office 365 overview dashboard

The new customer overview dashboard allows security teams to track efficacy across cyberthreats blocked pre-delivery, threats mitigated post-delivery, and even “missed” threats. It includes details on how Microsoft Defender for Office 365 capabilities like Safe link, Safe attachments, and Zero-hour Auto Purge contribute to threat protection across an organization. Our goal is simple: to help you confidently answer the question “How are my organization’s users being protected from malicious content and cyberattacks when using email and other collaboration surfaces like Microsoft Teams?”

![A screenshot of the new Defender for Office 365 overview dashboard.](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2025/07/Picture1-3.webp)

_Figure 1. Transparent Reporting Overview Dashboard_.

## Benchmarking

Transparency on effectiveness of Microsoft products alone isn’t enough. We know customers need data to evaluate effectiveness across the entire ecosystem, and our benchmarking research is intended to help you plan your cybersecurity solutions end to end.

Unlike traditional benchmarks that rely on synthetic tests or artificial environments, our reports use real email threats observed in the Microsoft ecosystem. We specifically compared environments protected solely by Microsoft Defender for Office 365 with those where an SEG was deployed in front of Defender, and with those where additional protection was provided by ICES vendors layered after Defender for Office 365. Throughout this process, we adhered to our strict security and privacy principles; all data presented in this report is aggregated and anonymized similar to data published in the Microsoft Digital Defense Report.

![A screenshot of a computer screen.](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2025/07/photo-1024x553.webp)

_Figure 2. Secure Email Gateway and Integrated Cloud Email Security vendors landscape_.

### Benchmarking SEG vendors

SEGs continue to play an important role in many organizations’ security architectures, offering additional layers of protection. Microsoft benchmarked seven SEG vendors and Microsoft Defender for Office 365.

#### **Methodology**

Microsoft analyzed aggregated threat signals from environments using specific SEGs with Defender for Office 365, then normalized the results per 1,000 protected users to measure missed threats.

For SEG vendors, a threat was considered “missed” if it was not detected pre-delivery, or if it was not removed shortly after delivery (post-delivery). However, for Microsoft Defender for Office 365, we applied a stricter standard; even if the threat was removed post-delivery, it was considered as missed.

#### **Results**

This analysis showed that, when baselined against Defender for Office, Defender for Office missed the least threats.

![A chart that shows how many email threats are missed by other secure email gateway vendors. ](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2025/07/Picture2-1-1024x578.webp)

_Figure 3. Secure Email Gateway (SEG) Vendor Benchmark Data_.

### ICES vendors

As organizations adopt layered security strategies, ICES products execute after Microsoft Defender for Office 365 and act as a secondary filter. These solutions offer additional detection layers focusing on specific threat types or user behavior patterns.

#### **Methodology**

ICES vendors use the [Microsoft Graph API](https://learn.microsoft.com/en-us/graph/use-the-api) to move emails to folders such as junk, promotional, or deleted items.   Messages can be moved from any delivery location, like the Inbox or even the Junk folder. In this data study, a message moved by an ICES vendor is counted as a catch. Messages marked as spam or malicious by Microsoft Defender for Office 365 _before_ the ICES vendor moved them, are counted as duplicate catch. Generally, messages classified as spam by Microsoft Defender for Office 365 are delivered to the Junk folder and those classified as malicious go to Quarantine. However, some customer configurations can override message delivery. The ICES vendor catch is normalized by Microsoft Defender for Office 365’s overall catch to make it simple to see the value added by ICES vendor.

![A chart that summarizes the incremental detection contributions from ICES vendors across several categories.](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2025/07/Picture3-1.webp)

_Figure 4. Integrated Cloud Email Security Vendor Benchmark Data_.

Definitions for the categories used are:

- **Marketing and bulk**—Promotional offers or newsletters from known senders (for example, a coupon from a food delivery app) that are not malicious but may affect productivity.
- **Spam**—Nuisance emails from unsolicited or disreputable senders that are not malicious but may affect productivity.
- **Malicious**—Messages containing harmful content such as phishing links, malware, or other security threats.
- **Non-malicious**—Benign messages that could be false positives or may have been moved due to customer preferences.

Our analysis shows that combining ICES products with Defender for Office 365 yields the greatest impact in enhancing detection of promotional or bulk email, with an average improvement of 20%. These enhancements can help reduce inbox clutter to improve user experience, particularly in environments where marketing noise is a concern, and offer valuable insight for us as we consider continued investment in enabling roadmap capabilities that benefit our customers. For malicious messages and spam, across all vendors analyzed, the average improvement was 0.30% for malicious catch and 0.51% for spam catch. Look for details on each vendor on the [benchmarking website](https://www.microsoft.com/en-us/security/business/siem-and-xdr/microsoft-defender-office-365/performance-benchmarking).

## Empowering security through transparency and data

In keeping with our commitment to transparency and data-driven rigor, we reached out to SE Labs, recognized experts in email security testing, to independently review our benchmarking methodology, ensuring we hold ourselves to the highest quality standards.

> “Businesses need to choose the best security that they can afford. Showing the additional benefit vendors provide using real threats, as Microsoft has done here, can help with this important decision.
>
> While traditional comparative tests with synthetic threats allow for testing that targets certain features in a product, using specific, advanced, or novel attack techniques, real-world data exposes how products perform against the full spectrum of threats encountered day to day.
>
> Both types of testing provide valuable insights that together give a more complete picture of security effectiveness. We hope Microsoft’s data inspires additional comparative testing for better customer decision-making.
>
> —Simon Edwards, Founder and Chief Executive Officer, SE Labs

In the face of increasingly complex email threats where cybersecurity decisions carry profound consequences, clarity and transparency are indispensable. To support data-driven decisions for our customers, we plan to provide [quarterly updates for these benchmarks](https://www.microsoft.com/en-us/security/business/siem-and-xdr/microsoft-defender-office-365/performance-benchmarking) and we will continue to take feedback and refine our approach working together with our ecosystem.

Microsoft remains steadfast in its commitment not only to securing organizations but also to providing reliable tools and actionable transparent data to help you evaluate efficacy and keep your organization safe.

## Learn more

Learn more about [Microsoft Defender for Office 365](https://www.microsoft.com/en-us/security/business/siem-and-xdr/microsoft-defender-office-365?msockid=3793858bb492626d36189079b50d634e)

To learn more about Microsoft Security solutions, visit our [website.](https://www.microsoft.com/en-us/security/business) Bookmark the [Security blog](https://www.microsoft.com/security/blog/) to keep up with our expert coverage on security matters. Also, follow us on LinkedIn ( [Microsoft Security](https://www.linkedin.com/showcase/microsoft-security/)) and X ( [@MSFTSecurity](https://twitter.com/@MSFTSecurity)) for the latest news and updates on cybersecurity.

## Related posts

- ![A blue background with a logo](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2025/07/Security-Blog-hero-1260x708_Revised0714-809x455.webp)









- July 22
- 6 min read

### [Microsoft Sentinel data lake: Unify signals, cut costs, and power agentic AI](https://www.microsoft.com/en-us/security/blog/2025/07/22/microsoft-sentinel-data-lake-unify-signals-cut-costs-and-power-agentic-ai/)

We’re evolving our industry-leading Security Incidents and Event Management solution (SIEM), Microsoft Sentinel, to include a modern, cost-effective data lake.

- ![A woman standing in front of a computer](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2025/07/Security_1071272_Blog_250701-809x455.webp)









- July 16
- 5 min read

### [Microsoft is named a Leader in the 2025 Gartner® Magic Quadrant™ for Endpoint Protection Platforms](https://www.microsoft.com/en-us/security/blog/2025/07/16/microsoft-is-named-a-leader-in-the-2025-gartner-magic-quadrant-for-endpoint-protection-platforms/)

We are honored to be recognized once again as a Leader in the 2025 Gartner® Magic Quadrant™ for Endpoint Protection Platforms—our sixth consecutive time.

- ![CISO (chief information security officer) collaborating with practitioners in a security operations center.](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2025/07/CLO22_SecOps_014-809x455.jpg)









- July 16
- 7 min read

### [Protecting customers from Octo Tempest attacks across multiple industries](https://www.microsoft.com/en-us/security/blog/2025/07/16/protecting-customers-from-octo-tempest-attacks-across-multiple-industries/)

To help protect and inform customers, Microsoft highlights protection coverage across the Microsoft Defender security ecosystem to protect against threat actors like Octo Tempest.

![](https://www.microsoft.com/en-us/security/blog/wp-content/themes/security-blog-2025/dist/images/bg-footer.png)

![](https://www.microsoft.com/en-us/security/blog/wp-content/themes/security-blog-2025/dist/images/bg-footer.png)

## Get started with Microsoft Security

Protect your people, data, and infrastructure with AI-powered, end-to-end security from Microsoft.

[Learn how](https://www.microsoft.com/en-us/security?wt.mc_id=AID730391_QSG_BLOG_319247&ocid=AID730391_QSG_BLOG_319247)

![](https://www.microsoft.com/en-us/security/blog/wp-content/themes/security-blog-2025/dist/images/footer-promotional.jpg)

Connect with us on social

- [X](https://twitter.com/msftsecurity)
- [YouTube](https://www.youtube.com/channel/UC4s3tv0Qq_OSUBfR735Jc6A)
- [LinkedIn](https://www.linkedin.com/showcase/microsoft-security/)
