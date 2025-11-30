---
date: '2025-11-30'
description: AWS leverages its vast infrastructure for high-fidelity threat intelligence,
  detecting and mitigating cyber threats in real-time through advanced systems such
  as MadPot and Mithra. MadPot analyzes over 100 million potential threats daily,
  while Mithra's neural network evaluates 3.5 billion nodes for domain reputability.
  This dual approach reduces false positives and allows proactive customer notifications
  of vulnerabilities. AWS also shares actionable insights and threat indicators, enhancing
  overall security posture and collaboration in the cybersecurity landscape. Such
  capabilities underline AWS’s leadership in cloud security by fostering resilience
  across its global network.
link: https://aws.amazon.com/blogs/security/how-aws-tracks-the-clouds-biggest-security-threats-and-helps-shut-them-down/
tags:
- Cybersecurity
- Threat Intelligence
- Cloud Security
- AWS
- Machine Learning
title: How AWS tracks the cloud’s biggest security threats and helps shut them down
  ◆ AWS Security Blog
---

## Select your cookie preferences

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies.

If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

AcceptDeclineCustomize

## Customize cookie preferences

We use cookies and similar tools (collectively, "cookies") for the following purposes.

### Essential

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

### Performance

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Allowed

### Functional

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Allowed

### Advertising

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Allowed

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the [AWS Cookie Notice](https://aws.amazon.com/legal/cookies/).

CancelSave preferences

## Your privacy choices

We and our advertising partners (“we”) may use information we collect from or about you to show you ads on other websites and online services. Under certain laws, this activity is referred to as “cross-context behavioral advertising” or “targeted advertising.”

To opt out of our use of cookies or similar technologies to engage in these activities, select “Opt out of cross-context behavioral ads” and “Save preferences” below. If you clear your browser cookies or visit this site from a different device or browser, you will need to make your selection again. For more information about cookies and how we use them, read our [Cookie Notice](https://aws.amazon.com/legal/cookies/).

Allow cross-context behavioral adsOpt out of cross-context behavioral ads

To opt out of the use of other identifiers, such as contact information, for these activities, fill out the form [here](https://pulse.aws/application/ZRPLWLL6?p=0).

For more information about how AWS handles your information, read the [AWS Privacy Notice](https://aws.amazon.com/privacy/).

CancelSave preferences

## Unable to save cookie preferences

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

Dismiss

 [Skip to Main Content](https://aws.amazon.com/blogs/security/how-aws-tracks-the-clouds-biggest-security-threats-and-helps-shut-them-down/#aws-page-content-main)

## [AWS Security Blog](https://aws.amazon.com/blogs/security/)

# How AWS tracks the cloud’s biggest security threats and helps shut them down

_Threat intelligence that can fend off security threats before they happen requires not just smarts, but the speed and worldwide scale that only AWS can offer._

Organizations around the world trust [Amazon Web Services (AWS)](https://aws.amazon.com/) with their most sensitive data. One of the ways we help secure data on AWS is with an industry-leading threat intelligence program where we identify and stop many kinds of malicious online activities that could harm or disrupt our customers or our infrastructure. Producing accurate, timely, actionable, and scalable threat intelligence is a responsibility we take very seriously, and is something we invest significant resources in.

Customers increasingly ask us where our threat intelligence comes from, what types of threats we see, how we act on what we observe, and what they need to do to protect themselves. Questions like these indicate that Chief Information Security Officers (CISOs)—whose roles have evolved from being primarily technical to now being a strategic, business-oriented function—understand that effective threat intelligence is critical to their organizations’ success and resilience. This blog post is the first of a series that begins to answer these questions and provides examples of how AWS threat intelligence protects our customers, partners, and other organizations.

## High-fidelity threat intelligence that can only be achieved at the global scale of AWS

Every day across AWS infrastructure, we detect and thwart cyberattacks. With the largest public network footprint of any cloud provider, AWS has unparalleled insight into certain activities on the internet, in real time. For threat intelligence to have meaningful impact on security, large amounts of raw data from across the internet must be gathered and quickly analyzed. In addition, false positives must be purged. For example, threat intelligence findings could erroneously indicate an insider threat when an employee is logged accessing sensitive data after working hours, when in reality, that employee may have been tasked with a last-minute project and had to work overnight. Producing threat intelligence is very time consuming and requires substantial human and digital resources. Artificial intelligence (AI) and machine learning can help analysts sift through and analyze vast amounts of data. However, without the ability to collect and analyze relevant information across the entire internet, threat intelligence is not very useful. Even for organizations that are able to gather actionable threat intelligence on their own, without the reach of global-scale cloud infrastructure, it’s difficult or impossible for time-sensitive information to be collectively shared with others at a meaningful scale.

The AWS infrastructure radically transforms threat intelligence because we can significantly boost threat intelligence accuracy—what we refer to as high fidelity—because of the sheer number of intelligence signals (notifications generated by our security tools) we can observe. And we constantly improve our ability to observe and react to threat actors’ evolving tactics, techniques, and procedures (TTPs) as we discover and monitor potentially harmful activities through [MadPot](https://aws.amazon.com/blogs/security/how-aws-threat-intelligence-deters-threat-actors/), our sophisticated globally-distributed network of honeypot threat sensors with automated response capabilities.

With our global network and internal tools such as [MadPot](https://aws.amazon.com/blogs/security/how-aws-threat-intelligence-deters-threat-actors/), we receive and analyze thousands of different kinds of event signals in real time. For example, MadPot observes more than 100 million potential threats every day around the world, with approximately 500,000 of those observed activities classified as malicious. This means high-fidelity findings (pieces of relevant information) produce valuable threat intelligence that can be acted on quickly to protect customers around the world from harmful and malicious online activities. Our high-fidelity intelligence also generates real-time findings that are ingested into our intelligent threat detection security service [Amazon GuardDuty](https://aws.amazon.com/guardduty/), which automatically detects threats for millions of AWS accounts.

## AWS’s Mithra ranks domain trustworthiness to help protect customers from threats

Let’s dive deeper. Identification of malicious domains (physical IP addresses on the internet) is crucial to effective threat intelligence. GuardDuty generates various kinds of [findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-active.html) (potential security issues such as anomalous behaviors) when AWS customers interact with domains, with each domain being assigned a reputation score derived from a variety of metrics that rank trustworthiness. Why this ranking? Because maintaining a high-quality list of malicious domain names is crucial to monitoring cybercriminal behavior so that we can protect customers. How do we accomplish the huge task of ranking? First, imagine a graph so large (perhaps one of the largest in existence) that it’s impossible for a human to view and comprehend the entirety of its contents, let alone derive usable insights.

Meet Mithra. Named after a mythological rising sun, Mithra is a massive internal neural network graph model, developed by AWS, that uses algorithms for threat intelligence. With its 3.5 billion nodes and 48 billion edges, Mithra’s reputation scoring system is tailored to identify malicious domains that customers come in contact with, so the domains can be ranked accordingly. We observe a significant number of [DNS requests](https://aws.amazon.com/route53/what-is-dns/) per day—up to 200 trillion in a single AWS Region alone—and Mithra detects an average of 182,000 new malicious domains daily. By assigning a reputation score that ranks every domain name queried within AWS on a daily basis, Mithra’s algorithms help AWS rely less on third parties for detecting emerging threats, and instead generate better knowledge, produced more quickly than would be possible if we used a third party.

Mithra is not only able to detect malicious domains with remarkable accuracy and fewer false positives, but this super graph is also capable of predicting malicious domains days, weeks, and sometimes even months before they show up on threat intel feeds from third parties. This world-class capability means that we can see and act on millions of security events and potential threats every day.

By scoring domain names, Mithra can be used in the following ways:

- A high-confidence list of previously unknown malicious domain names can be used in security services like GuardDuty to help protect our customers. GuardDuty also allows customers to block malicious domains and get alerts for potential threats.
- Services that use third-party threat feeds can use Mithra’s scores to significantly reduce false positives.
- AWS security analysts can use scores for additional context as part of security investigations.

## Sharing our high-fidelity threat intelligence with customers so they can protect themselves

Not only is our threat intelligence used to seamlessly enrich security services that AWS and our customers rely on, we also proactively reach out to share critical information with customers and other organizations that we believe may be targeted or potentially compromised by malicious actors. Sharing our threat intelligence enables recipients to assess information we provide, take steps to reduce their risk, and help prevent disruptions to their business.

For example, using our threat intelligence, we notify organizations around the world if we identify that their systems are potentially compromised by threat actors or appear to be running misconfigured systems vulnerable to exploits or abuse, such as open databases. Cybercriminals are constantly scanning the internet for exposed databases and other vulnerabilities, and the longer a database remains exposed, the higher the risk that malicious actors will discover and exploit it. In certain circumstances when we receive signals that suggest a third-party (non-customer) organization may be compromised by a threat actor, we also notify them because doing so can help head off further exploitation, which promotes a safer internet at large.

Often, when we alert customers and others to these kinds of issues, it’s the first time they become aware that they are potentially compromised. After we notify organizations, they can investigate and determine the steps they need to take to protect themselves and help prevent incidents that could cause disruptions to their organization or allow further exploitation. Our notifications often also include recommendations for actions organizations can take, such as to review security logs for specific domains and block them, implement mitigations, change configurations, conduct a forensic investigation, install the latest patches, or move infrastructure behind a network firewall. These proactive actions help organizations to get ahead of potential threats, rather than just reacting after an incident occurs.

Sometimes, the customers and other organizations we notify contribute information that in turn helps us assist others. After an investigation, if an affected organization provides us with related indicators of compromise (IOCs), this information can be used to improve our understanding of how a compromise occurred. This understanding can lead to critical insights we may be able to share with others, who can use it to take action to improve their security posture—a virtuous cycle that helps promote collaboration aimed at improving security. For example, information we receive may help us learn how a social engineering attack or particular phishing campaign was used to compromise an organization’s security to install malware on a victim’s system. Or, we may receive information about a zero-day vulnerability that was used to perpetrate an intrusion, or learn how a remote code execution (RCE) attack was used to run malicious code and other malware to steal an organization’s data. We can then use and share this intelligence to protect customers and other third parties. This type of collaboration and coordinated response is more effective when organizations work together and share resources, intelligence, and expertise.

## Three examples of AWS high-fidelity threat intelligence in action

**Example 1:** We became aware of suspicious activity when our [MadPot](https://aws.amazon.com/blogs/security/how-aws-threat-intelligence-deters-threat-actors/) sensors indicated unusual network traffic known as backscatter (potentially unwanted or unintended network traffic that is often associated with a cyberattack) that contained known IOCs associated with a specific threat attempting to move across our infrastructure. The network traffic appeared to be originating from the IP space of a large multinational food service industry organization and flowing to Eastern Europe, suggesting potential malicious data exfiltration. Our threat intelligence team promptly contacted the security team at the affected organization, which wasn’t an AWS customer. They were already aware of the issue but believed they had successfully addressed and removed the threat from their IT environment. However, our sensors indicated that the threat was continuing and not resolved, showing that a persistent threat was ongoing. We requested an immediate escalation, and during a late-night phone call, the AWS CISO shared real-time security logs with the CISO of the impacted organization to show that large amounts of data were still being suspiciously exfiltrated and that urgent action was necessary. The CISO of the affected company agreed and engaged their Incident Response (IR) team, which we worked with to successfully stop the threat.

**Example 2:** Earlier this year, Volexity published [research](https://www.volexity.com/blog/2024/01/10/active-exploitation-of-two-zero-day-vulnerabilities-in-ivanti-connect-secure-vpn/) detailing two zero-day vulnerabilities in the Ivanti Connect Secure VPN, resulting in the publication of [CVE-2023-46805](https://nvd.nist.gov/vuln/detail/CVE-2023-46805) (an authentication-bypass vulnerability) and [CVE-2024-21887](https://nvd.nist.gov/vuln/detail/CVE-2023-21887) (a command-injection vulnerability found in multiple web components). The U.S. Cybersecurity and Infrastructure Security Agency (CISA) issued a cybersecurity [advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060b) on February 29, 2024 on this issue. Earlier this year, Amazon security teams enhanced our MadPot sensors to detect attempts by malicious actors to exploit these vulnerabilities. Using information obtained by the MadPot sensors, Amazon identified multiple active exploitation campaigns targeting vulnerable Ivanti Connect Secure VPNs. We also published related intelligence in the GuardDuty common vulnerabilities and exposures (CVE) feed, enabling our customers who use this service to detect and stop this activity if it is present in their environment. (For more on CVSS metrics, see the [National Institute of Standards and Technology (NIST) Vulnerability Metrics](https://nvd.nist.gov/vuln-metrics/cvss).)

**Example 3:** Around the time Russia began its invasion of Ukraine in 2022, Amazon proactively identified infrastructure that Russian threat groups were creating to use for phishing campaigns against Ukrainian government services. Our intelligence findings were integrated into GuardDuty to automatically protect AWS customers while also providing the information to the Ukrainian government for their own protection. After the invasion, Amazon identified IOCs and TTPs of Russian cyber threat actors that appeared to target certain technology supply chains that could adversely affect Western businesses opposed to Russia’s actions. We worked with the targeted AWS customers to thwart potentially harmful activities and help prevent supply chain disruption from taking place.

AWS operates the most trusted cloud infrastructure on the planet, which gives us a unique view of the security landscape and the threats our customers face every day. We are encouraged by how our efforts to share our threat intelligence have helped customers and other organizations be more secure, and we are committed to finding even more ways to help. Upcoming posts in this series will include other threat intelligence topics such as mean time to defend, our internal tool [Sonaris](https://www.aboutamazon.com/news/aws/aws-security-cloud-generative-ai-customer-data), and more.

If you have feedback about this post, submit comments in the **Comments** section below. If you have questions about this post, [contact AWS Support](https://console.aws.amazon.com/support/home).

[![](https://d1.awsstatic.com/Digital%20Marketing/House/Editorial/other/SiteMerch-3066-Podcast_Editorial.65839609a8dda387937ed07dc8dc4f3c3b870546.png)\\
\\
AWS Podcast \\
\\
\\
Subscribe for weekly AWS news and interviews \\
\\
\\
Learn more](https://aws.amazon.com/podcasts/aws-podcast/?sc_icampaign=aware_aws-podcast&sc_ichannel=ha&sc_icontent=awssm-2021&sc_iplace=blog_tile&trk=ha_awssm-2021)

[![](https://d1.awsstatic.com/webteam/homepage/editorials/Site-Merch_APN_Editorial.12df33fb7e0299389b086fb48dba7b9deeef07df.png)\\
\\
AWS Partner Network \\
\\
\\
Find an APN member to support your cloud business needs \\
\\
\\
Learn more](https://aws.amazon.com/partners/find/?sc_icampaign=aware_apn_recruit&sc_ichannel=ha&sc_icontent=awssm-2021&sc_iplace=blog_tile&trk=ha_awssm-2021)

[![](https://d1.awsstatic.com/webteam/homepage/editorials/Site-Merch_Training_Editorial.5cc72ab0552ba66ef4e36a1a60ee742bc31113c7.png)\\
\\
AWS Training & Certifications \\
\\
\\
Free digital courses to help you develop your skills \\
\\
\\
Learn more](https://aws.amazon.com/training/?sc_icampaign=aware_aws-training_blog&sc_ichannel=ha&sc_icontent=awssm-2021&sc_iplace=blog_tile&trk=ha_awssm-2021)

### Resources

- [AWS Cloud Security](https://aws.amazon.com/security?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=security-resources)
- [AWS Compliance](https://aws.amazon.com/compliance?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=security-resources)
- [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html?secd_ip5)
- [Best Practices](https://aws.amazon.com/architecture/security-identity-compliance)
- [Data Protection at AWS](https://aws.amazon.com/compliance/data-protection/)
- [Zero Trust on AWS](https://aws.amazon.com/security/zero-trust/)
- [Cryptographic Computing](https://aws.amazon.com/security/cryptographic-computing/)

* * *

### Follow

- [Twitter](https://twitter.com/AWSsecurityinfo)
- [Facebook](https://www.facebook.com/amazonwebservices)
- [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
- [Twitch](https://www.twitch.tv/aws)
- [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=security-social)

[![](https://d1.awsstatic.com/webteam/homepage/editorials/Site-Merch_Events_Editorial.5418337af87bf455c2d1528c064688a6d4b4f04c.png)\\
\\
AWS Events \\
\\
\\
Discover the latest AWS events in your region \\
\\
\\
Learn more](https://aws.amazon.com/events/?sc_icampaign=aware_aws-events&sc_ichannel=ha&sc_icontent=awssm-2021_event&sc_iplace=blog-sidebar&trk=ha_awssm-2021_event)
