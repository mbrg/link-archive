---
date: '2025-11-30'
description: Amazon Threat Intelligence reveals an emergent trend in warfare termed
  "cyber-enabled kinetic targeting," where nation-state actors integrate cyber operations
  to facilitate physical attacks. Recent case studies illustrate how actors like Imperial
  Kitten and MuddyWater use cyber reconnaissance to inform real-time military operations
  on critical infrastructure, highlighting the need to re-evaluate traditional cybersecurity
  frameworks that separate digital and physical threats. This paradigm shift demands
  enhanced threat modeling, critical infrastructure protection, and collaborative
  intelligence sharing among organizations and governmental bodies, acknowledging
  the evolving nature of adversarial tactics in modern conflict.
link: https://aws.amazon.com/blogs/security/new-amazon-threat-intelligence-findings-nation-state-actors-bridging-cyber-and-kinetic-warfare/
tags:
- threat intelligence
- cyber warfare
- cybersecurity
- nation-state actors
- AWS security
title: 'New Amazon Threat Intelligence findings: Nation-state actors bridging cyber
  and kinetic warfare ◆ AWS Security Blog'
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

 [Skip to Main Content](https://aws.amazon.com/blogs/security/new-amazon-threat-intelligence-findings-nation-state-actors-bridging-cyber-and-kinetic-warfare/#aws-page-content-main)

## [AWS Security Blog](https://aws.amazon.com/blogs/security/)

# New Amazon Threat Intelligence findings: Nation-state actors bridging cyber and kinetic warfare

## The new threat landscape

The line between cyber warfare and traditional kinetic operations is rapidly blurring. Recent investigations by Amazon threat intelligence teams have uncovered a new trend that they’re calling _cyber-enabled kinetic targeting_ in which nation-state threat actors systematically use cyber operations to enable and enhance physical operations. Traditional cybersecurity frameworks often treat digital and physical threats as separate domains. However, research by Amazon demonstrates that this separation is increasingly artificial. Multiple nation-state threat groups are pioneering a new operational model where cyber reconnaissance directly enables kinetic targeting.

We’re seeing a fundamental shift in how nation-state actors approach warfare. These aren’t just cyber attacks that happen to cause physical damage; they are coordinated campaigns where digital operations are specifically designed to support physical military objectives.

## Unique visibility at Amazon

The ability of Amazon Threat Intelligence to identify these campaigns stems from their unique position in the global threat landscape:

- **Threat intelligence telemetry**: Amazon global cloud operations provide visibility into threats across diverse environments, including intelligence from Amazon [MadPot](https://aws.amazon.com/blogs/security/how-aws-tracks-the-clouds-biggest-security-threats-and-helps-shut-them-down/) honeypot systems, which enable the detection of suspicious patterns, actor infrastructure, and the network pathways used in these cyber-enabled kinetic targeting campaigns.
- **Opt-in customer data**: Real-world data about attempted threat actor activities provided on an opt-in basis from enterprise environments.
- **Industry partner collaboration**: Threat intelligence sharing with leading security organizations and government agencies provides additional context and validation for observed activities.

Through this multi-source approach, Amazon can connect dots that might otherwise remain invisible to individual organizations or even government agencies operating in isolation.

## Case study 1: Imperial Kitten’s maritime campaign

The first case study involves Imperial Kitten, a threat group suspected of operating on behalf of Iran’s Islamic Revolutionary Guard Corps (IRGC). The timeline reveals the progression from digital reconnaissance to physical attack:

- **December 4, 2021**: Imperial Kitten compromises a maritime vessel’s Automatic Identification System (AIS) platform, gaining access to critical shipping infrastructure. The Amazon Threat Intelligence team identifies the compromise and works with the affected organization to remediate the security event.
- **August 14, 2022**: The threat actor expands their maritime targeting of additional vessel platforms. In one incident, they gained access to CCTV cameras aboard a maritime vessel, which provided real-time visual intelligence.
- **January 27, 2024**: Imperial Kitten conducts targeted searches for AIS location data for a specific shipping vessel. This represents a clear shift from broad reconnaissance to targeted intelligence gathering.
- **February 1, 2024**: US Central Command reports a missile strike by Houthi forces against the exact vessel that Imperial Kitten had been tracking. While the missile strike was ultimately ineffective, the correlation between the cyber reconnaissance and kinetic strike is unmistakable.

This case demonstrates how cyber operations can provide adversaries with the precise intelligence needed to conduct targeted physical attacks against maritime infrastructure—a critical component of global commerce and military logistics.

## Case study 2: MuddyWater’s Jerusalem operations

The second case study involves MuddyWater, a threat group attributed by the US government to Rana Intelligence Computer Company, operating at the behest of Iran’s Ministry of Intelligence and Security (MOIS). This case reveals an even more direct connection between cyber operations and kinetic targeting.

- **May 13, 2025**: MuddyWater provisions a server specifically for cyber network operations, establishing the infrastructure needed for their campaign.
- **June 17, 2025**: The threat actor uses their server infrastructure to access another compromised server containing live CCTV streams from Jerusalem. This provides real-time visual intelligence of potential targets within the city.
- **June 23, 2025**: Iran launches widespread missile attacks against Jerusalem. On the same day, Israeli authorities report that Iranian forces were exploiting compromised security cameras to gather real-time intelligence and adjust missile targeting.

The timing is not coincidental. As reported by [The Record](https://therecord.media/iran-espionage-israeli-security-cameras-missile-attacks), Israeli officials urged citizens to disconnect internet-connected security cameras, warning that Iran was exploiting them to “gather real-time intelligence and adjust missile targeting.”

## Technical infrastructure and methods

Research by Amazon reveals the sophisticated technical infrastructure supporting these operations. The threat actors employ a multi-layered approach:

1. **Anonymizing VPN networks**: Threat actors route their traffic through anonymizing VPN services to obscure their true origins and make attribution more difficult.
2. **Actor-controlled servers**: Dedicated infrastructure provides persistent access and command-and-control capabilities for ongoing operations.
3. **Compromised enterprise systems**: The ultimate targets—enterprise servers hosting critical infrastructure like CCTV systems, maritime platforms, and other intelligence-rich environments.
4. **Real-time data streaming**: Live feeds from compromised cameras and sensors provide actionable intelligence that can be used to adjust targeting in near real time.

## Defining a new category of warfare

The research team proposes new terminology to describe these hybrid operations. Traditional frameworks fall short:

- **Cyber-kinetic operations** typically refer to cyber attacks that cause physical damage to systems
- **Hybrid warfare** is too broad, encompassing multiple types of warfare without specific focus on the cyber-physical integration

Amazon researchers suggest _cyber-enabled kinetic targeting_ as a more precise term for campaigns where cyber operations are specifically designed to enable and enhance kinetic military operations.

## Implications for defenders

For the cybersecurity community, this research serves as both a warning and a call to action. Defenders must adapt their strategies to address threats that span both digital and physical domains. Organizations that historically believed they weren’t of interest to threat actors could now be targeted for tactical intelligence. We must expand our threat models, enhance our intelligence sharing, and develop new defensive strategies that account for the reality of cyber-enabled kinetic targeting across diverse adversaries.

- **Expanded threat modeling**: Organizations must consider not just the direct impact of cyberattacks, but how compromised systems might be used to support physical attacks against themselves or others.
- **Critical infrastructure protection**: Operators of maritime systems, urban surveillance networks, and other infrastructure must recognize that their systems might be valuable not just for espionage, but as targeting aids for kinetic operations.
- **Intelligence sharing**: The cases demonstrate the critical importance of threat intelligence sharing between private sector organizations, government agencies, and international partners.
- **Attribution challenges**: When cyber operations directly enable kinetic attacks, the attribution and response frameworks become more complex, potentially requiring coordination between cybersecurity, military, and diplomatic channels.

## Looking forward

We believe that cyber-enabled kinetic targeting will become increasingly common across multiple adversaries. Nation-state actors are recognizing the force multiplier effect of combining digital reconnaissance with physical attacks. This trend represents a fundamental evolution in warfare, where the traditional boundaries between cyber and kinetic operations are dissolving.

### Indicators of Compromise

IOC Value, IOC Type, First Seen, Last Seen, Annotation


18\[.\]219.14.54, IPv4, 2025-05-13, 2025-06-17, MuddyWater Command and Control IP address


85\[.\]239.63.179, IPv4, 2023-08-13, 2025-09-19, Imperial Kitten proxy IP address


37\[.\]120.233.84, IPv4, 2021-01-01, 2022-11-01, Imperial Kitten proxy IP address


95\[.\]179.207.105, IPv4, 2020-11-11, 2022-04-09, Imperial Kitten proxy IP address

_This blog post is based on research presented at CYBERWARCON by David Magnotti, Principal Engineer, and Dlshad Othman, Senior Threat Intelligence Engineer, both of Amazon Threat Intelligence. The authors thank US Central Command for their transparency in reporting military activities and acknowledge the ongoing support of customers and partners in these critical investigations._

If you have feedback about this post, submit comments in the **Comments** section below. If you have questions about this post, [contact AWS Support](https://console.aws.amazon.com/support/home).

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
