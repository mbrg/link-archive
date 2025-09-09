---
date: '2025-09-09'
description: Microsoft's Active Protections Program (MAPP) faces escalating risks
  associated with Chinese company participation due to conflicting domestic security
  regulations. MAPP is designed for swift vulnerability patching, but several Chinese
  firms must report zero-days to state authorities within 48 hours, creating potential
  leaks to threat actors. The recent "ToolShell" campaign illustrates these vulnerabilities,
  leading to significant global cybersecurity threats. Continued involvement of Chinese
  firms in MAPP must be scrutinized to mitigate insider risks and prevent exploitation,
  challenging Microsoft’s operational integrity and user security amidst systemic
  governmental pressures.
link: https://nattothoughts.substack.com/p/when-privileged-access-falls-into
tags:
- Microsoft MAPP
- China cyber threats
- information security
- vulnerability disclosure
- cybersecurity
title: 'When Privileged Access Falls into the Wrong Hands: Chinese Companies in Microsoft’s
  MAPP Program'
---

[![Natto Thoughts](https://substackcdn.com/image/fetch/$s_!1RVv!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F129a6344-5848-4177-b035-86464e1bdfb7_334x334.png)](https://nattothoughts.substack.com/)

# [Natto Thoughts](https://nattothoughts.substack.com/)

SubscribeSign in

![User's avatar](https://substackcdn.com/image/fetch/$s_!7NwJ!,w_64,h_64,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F89cc96e8-a290-4e80-8425-e183892d1f15_500x334.webp)

Discover more from Natto Thoughts

Stories, analysis and insights from the intersection of culture, technology, and security.

Over 1,000 subscribers

Subscribe

By subscribing, I agree to Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

Already have an account? Sign in

# When Privileged Access Falls into the Wrong Hands: Chinese Companies in Microsoft’s MAPP Program

### Chinese companies face conflicting pressures between MAPP’s non-disclosure requirements and domestic policies that incentivize or mandate vulnerability disclosure to the state.

[![Eugenio Benincasa's avatar](https://substackcdn.com/image/fetch/$s_!-Wtv!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F09a1f79e-07d1-4938-9147-e0df8440802f_800x800.jpeg)](https://substack.com/@eubenincasa)

[![Dakota Cary's avatar](https://substackcdn.com/image/fetch/$s_!D_sy!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff14100c6-832f-4739-84c8-88b8137c5382_400x400.jpeg)](https://substack.com/@dakotaksg)

[![Natto Team's avatar](https://substackcdn.com/image/fetch/$s_!7NwJ!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F89cc96e8-a290-4e80-8425-e183892d1f15_500x334.webp)](https://substack.com/@nattothoughts)

[Eugenio Benincasa](https://substack.com/@eubenincasa)

,

[Dakota Cary](https://substack.com/@dakotaksg)

, and

[Natto Team](https://substack.com/@nattothoughts)

Jul 31, 2025

17

[2](https://nattothoughts.substack.com/p/when-privileged-access-falls-into/comments)
8

Share

On July 25, 2025, Bloomberg [reported](https://www.bloomberg.com/news/articles/2025-07-25/microsoft-sharepoint-hack-probe-on-whether-chinese-hackers-found-flaw-via-alert?srnd=undefined) that Microsoft is investigating whether a leak from its Microsoft Active Protections Program (MAPP) allowed Chinese hackers to exploit a SharePoint vulnerability before a patch was released. Microsoft attributed the campaign – dubbed “ToolShell” after the custom remote access trojan used – to three China-linked threat actors: Linen Typhoon, Violet Typhoon, and Storm-2603. The attackers reportedly compromised over 400 organizations worldwide, including the U.S. National Nuclear Security Administration.

Launched in 2008, MAPP is designed to reduce the time between the discovery of a vulnerability and the deployment of patches. By giving trusted security vendors early access to technical details about upcoming patches, Microsoft enables them to release protections (such as antivirus signatures and intrusion detection rules) in sync with its monthly updates. The program, however, relies on strict compliance with non-disclosure agreements and the secure handling of pre-release data.

Concerns about some Chinese companies violating MAPP requirements are longstanding. In 2012, Microsoft [removed](https://msrc.microsoft.com/blog/2012/05/mapp-update-taking-action-to-decrease-risk-of-information-disclosure/) Chinese company Hangzhou DPTech Technologies Co., Ltd. (杭州迪普科技股份有限公司) from the program for violating its nondisclosure agreement (NDA). According to Bloomberg, in 2021, Microsoft [suspected](https://www.bloomberg.com/news/articles/2025-07-25/microsoft-sharepoint-hack-probe-on-whether-chinese-hackers-found-flaw-via-alert?srnd=undefined) that at least two other Chinese MAPP partners leaked details of unpatched Exchange server vulnerabilities, enabling a global cyber espionage campaign linked to the Chinese threat group Hafnium. The Microsoft Exchange hack affected tens of thousands of servers, including systems at the European Banking Authority and the Norwegian Parliament, and [was met with](https://www.sentinelone.com/labs/chinas-covert-capabilities-silk-spun-from-hafnium/) global condemnation. Although [Microsoft said](https://www.bloomberg.com/news/articles/2021-04-27/microsoft-weighs-revamping-flaw-disclosures-after-suspected-leak) it would review MAPP following the incident, it remains unclear whether any reforms were implemented, or whether a leak was ever confirmed.

In light of the SharePoint case, this piece examines how MAPP operates, the risks posed by Chinese firms in the program, and which companies are currently involved.

Subscribe

## **MAPP Seeks to Reduce Risk Through Early Disclosure**

The core purpose of MAPP is to minimize the window of risk between patch rollout and deployment. Simply releasing a patch doesn't mean systems are protected: many organizations delay patching, and attackers often exploit known vulnerabilities during this lag. By giving trusted vendors early access to vulnerability details, Microsoft ensures they can build and distribute detection signatures and other defensive measures in advance, so these protections are already active when the patch is published. Without MAPP, vendors would only begin creating protections after public disclosure, leaving many systems globally, including in China, exposed for critical hours or days.

To participate in MAPP, security vendors must meet criteria that demonstrate their ability to protect a broad customer base. Applicants must be willing to sign a non-disclosure agreement, commit to coordinated vulnerability disclosure practices, share threat information, and actively create in-house security protections such as signatures or indicators of compromise based on Microsoft's data. Microsoft retains discretion over admission and may suspend or expel members who fail to meet participation standards.

According to the MAPP website, members are divided into three tiers based on the amount of time they receive vulnerability information before public release and other criteria: Entry (24 hours in advance), ANS (up to 5 days in advance), and Validate (invite-only, focused on testing detection guidance). However, [recently admitted MAPP partners](https://stellarcyber.ai/news/press-releases/stellar-cyber-joins-microsoft-active-protections-program-mapp-to-deliver-proactive-threat-defense/) and [recognized experts](https://www.theregister.com/2025/07/26/microsoft_sharepoint_attacks_leak/) have observed that Microsoft may provide critical vulnerability and threat intelligence as early as two weeks prior to public disclosure. Criteria for determining the criticality which warrants such early releases and to whom the intelligence flows is unclear.

## Risks of Chinese Participation in MAPP

Chinese companies operating within MAPP present a unique risk due to national regulations mandating the disclosure of vulnerabilities to the state. In September 2021, China implemented the Regulations on the Management of Network Product Security Vulnerabilities (RMSV), which require any organization doing business in China to report newly discovered zero-day vulnerabilities to government authorities within 48 hours. This gives Chinese state agencies early access to high-impact vulnerabilities – often before patches are available. Microsoft itself acknowledged the implications of this policy in its [2022 Digital Defense Report](https://blogs.microsoft.com/on-the-issues/2022/11/04/microsoft-digital-defense-report-2022-ukraine/), noting that “this new regulation might enable elements in the Chinese government to stockpile reported vulnerabilities toward weaponizing them.”

While the RMSV serves as the primary legal pathway for the state to acquire zero-days, it is not the only mechanism. In 2023, cybersecurity analysts Dakota Cary and Kristin Del Rosso uncovered a parallel, more opaque process involving the China National Vulnerability Database of Information Security (CNNVD), which is overseen by the Ministry of State Security (MSS). Under this framework, Chinese cybersecurity firms voluntarily partner with CNNVD to report vulnerabilities, [in exchange for financial compensation](https://archive.ph/Ano99) and prestige. These firms, known as technical support units (TSUs), are stratified into three tiers based on the number of vulnerabilities they submit each year. Tier 1 TSUs must submit at least 20 “common” vulnerabilities annually, including a minimum of 3 classified as “critical risk.”

[![](https://substackcdn.com/image/fetch/$s_!EhC1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F382de5ac-b4cf-41b4-aa5e-e9346bc1ee80_973x768.jpeg)](https://substackcdn.com/image/fetch/$s_!EhC1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F382de5ac-b4cf-41b4-aa5e-e9346bc1ee80_973x768.jpeg) Requirements for companies applying to join the CNNVD’s Technical Support Units. Source: [CNNVD Handbook](https://archive.ph/CvOL7), Translation by Dakota Cary

As early as 2017, the U.S. threat intelligence firm Recorded Future [demonstrated](https://www.recordedfuture.com/blog/chinese-vulnerability-data-altered) that vulnerabilities reported to CNNVD are assessed by the MSS for their potential use in intelligence operations. As of this writing, 38 companies are classified as Tier 1 contributors to CNNVD, 61 as Tier 2, and 247 as Tier 3. Of these, ten Tier 1 companies, one Tier 2, and one Tier 3 company are currently MAPP members.

In addition to providing new vulnerabilities to the CNNVD, TSUs are also required to provide “vulnerability early warning support” to the MSS: at least five “critical alerts” annually for Tiers 1 and 2, and at least three for Tier 3. As cybersecurity and tech companies, many TSUs likely provide this early warning support by reporting newly observed attacks on their customers or systems. Nothing beyond the Microsoft NDA precludes TSUs from sharing MAPP data with CNNVD, which may view such submissions as fulfilling this vulnerability early warning support requirement.

[Share](https://nattothoughts.substack.com/p/when-privileged-access-falls-into?utm_source=substack&utm_medium=email&utm_content=share&action=share)

## **Chinese MAPP Participants Dominated by CNNVD Tier 1 Companies**

Our analysis of the MAPP [main page](https://www.microsoft.com/en-us/msrc/mapp) via the Wayback Machine shows that the number of Chinese companies listed in MAPP increased from 13 in [December 2018](https://web.archive.org/web/20181214185855/https://www.microsoft.com/en-us/msrc/mapp) (the earliest available snapshot) to 19 out of a total of 104 member companies globally as of this writing – the second-largest national representation after the US.

[![](https://substackcdn.com/image/fetch/$s_!JlLx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d1189b0-0edf-49a2-850e-efa1ee86bf08_1060x838.jpeg)](https://substackcdn.com/image/fetch/$s_!JlLx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d1189b0-0edf-49a2-850e-efa1ee86bf08_1060x838.jpeg) Current MAPP Partners (as of July 2025); Chinese companies highlighted in red. Source: [Microsoft MAPP website](https://www.microsoft.com/en-us/msrc/mapp)

Since 2018, several Chinese companies have appeared and disappeared from the MAPP list. Companies that have since disappeared include Beijing Leadsec (北京网御星云技术有限公司), Huawei, and Neusoft (东软集团) (removed between [December 2018 and November 2019](https://web.archive.org/web/20191108214204/https://www.microsoft.com/en-us/msrc/mapp)), Qihoo 360 (奇虎360) (between [November 2019 and October 2020](https://web.archive.org/web/20201020234619/https://www.microsoft.com/en-us/msrc/mapp)), Hangzhou H3C Technology (between [December 2021 and October 2022](https://web.archive.org/web/20220930222141/https://www.microsoft.com/en-us/msrc/mapp)), and Sangfor (between [October 2022 and September 2023](https://web.archive.org/web/20230922084021/https://www.microsoft.com/en-us/msrc/mapp)). Newly added companies between 2018 and today can be seen in the table below. The reasons for a company's removal from the MAPP list are not always clear. In the case of Huawei and Qihoo 360, the timing aligns with their addition to the U.S. Entity List in [2019](https://www.federalregister.gov/documents/2019/05/21/2019-10616/addition-of-entities-to-the-entity-list) and [2020](https://www.federalregister.gov/documents/2020/06/05/2020-10869/addition-of-entities-to-the-entity-list-revision-of-certain-entries-on-the-entity-list), respectively. For others, we could not locate any public explanation from Microsoft, unlike the 2012 public notice from the Microsoft Security Response Center regarding DPTech’s removal for [violating](https://msrc.microsoft.com/blog/2012/05/mapp-update-taking-action-to-decrease-risk-of-information-disclosure/) MAPP’s NDA requirements.

Of the 19 Chinese companies currently participating in MAPP, 12 are classified as CNNVD TSUs (see table below). Based on previous research into their vulnerability submissions to Microsoft’s bug bounty program, Tier 1 TSUs such as Tencent (腾讯), Cyber Kunlun (赛博昆仑), Sangfor (深信服科技), QiAnXin (奇安信), and Venustech (启明星辰) [operate dedicated labs](https://ethz.ch/content/dam/ethz/special-interest/gess/cis/center-for-securities-studies/pdfs/cyber-report-2024-from-vegas-to-chengdu.pdf) – with varying levels of focus – on identifying vulnerabilities in Microsoft software products.

[![](https://substackcdn.com/image/fetch/$s_!8klO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2e0c3ee4-3c48-449c-a385-ce656fe59d53_614x837.png)](https://substackcdn.com/image/fetch/$s_!8klO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2e0c3ee4-3c48-449c-a385-ce656fe59d53_614x837.png) Side-by-side comparison of Chinese companies in MAPP in 2018 and 2025, indicating current CNNVD TSU status. Source: Created by the Authors

It is also possible that individuals working at MAPP companies in China individually decide to pass along or sell such information to offensive teams. With access to valuable information and a clear market of buyers, insider risk at MAPP partners themselves cannot be ruled out.

Regardless of the specific mechanism for information diffusion, it is clear that China’s incentives for reporting such vulnerabilities – both economic and reputational, as companies seek to meet CNNVD quotas and maintain TSU status for potential business opportunities – create an environment which incentivizes abuse.

## China’s Vulnerability Ecosystem Enables Rapid Exploitation and Cross-Group Sharing

Vulnerabilities reported to the MSS-run CNNVD may be evaluated for potential operational use before being disclosed to the public. Chinese APT groups are known for their speed and coordination in exploiting such vulnerabilities. According to advisories from multiple [national cybersecurity agencies](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-190a) and [threat intelligence firms](https://cloud.google.com/blog/topics/threat-intelligence/apt41-us-state-governments?utm_source=chatgpt.com), groups such as APT40 and APT41 have exploited vulnerabilities within hours or days of public disclosure. Chinese APTs are also effective at sharing exploits across groups. Once a vulnerability has been successfully weaponized, it often [circulates rapidly](https://www.atlanticcouncil.org/in-depth-research-reports/report/crash-exploit-and-burn/) among operators.

Both of these dynamics were on display during the 2021 Microsoft Exchange campaign. On [February 23, 2021](https://www.zdnet.com/article/microsoft-investigates-potential-tie-between-partner-firm-and-potential-exchange-bug-leak/), MAPP distributed proof-of-concept (POC) code to its members so they could engineer detections. [Five days later](https://www.theguardian.com/world/2021/jul/19/what-is-the-hafnium-microsoft-hack-and-why-has-the-uk-linked-it-to-china), mass exploitation of the vulnerabilities with similar code to that distributed via MAPP blanketed the web. [According to](https://www.welivesecurity.com/2021/03/10/exchange-servers-under-siege-10-apt-groups/) threat intelligence firm ESET, exploitation began with the China-linked threat group Tick and was quickly followed by other China-linked groups, including LuckyMouse, Calypso and the Winnti Group. Microsoft made patches publicly available for customers shortly thereafter on March 2, 2021–seven days after distributing POC code to MAPP members.

A similar pattern emerged in 2025 with the exploitation of SharePoint vulnerabilities [first disclosed](https://news.sophos.com/en-us/2025/07/21/sharepoint-toolshell-vulnerabilities-being-exploited-in-the-wild/) at Pwn2Own Berlin in May. The winning submission was reported to Microsoft shortly after the event. As per standard MAPP procedures, Microsoft distributed vulnerability details to selected partners [up to two weeks](https://www.theregister.com/2025/07/26/microsoft_sharepoint_attacks_leak/) before the public patch, scheduled for July 9. Yet CrowdStrike [observed exploitation](https://www.bloomberg.com/news/articles/2025-07-22/microsoft-says-chinese-hackers-exploiting-sharepoint-flaws) as early as July 7, again suggesting that threat groups may have gained access to vulnerability details before protections were made widely available. Microsoft [attributed](https://www.microsoft.com/en-us/security/blog/2025/07/22/disrupting-active-exploitation-of-on-premises-sharepoint-vulnerabilities/) the activity to no fewer than three China-linked groups on July 22.

## **Mission or Mission Impossible?**

Microsoft’s [stated mission](https://www.microsoft.com/en-us/about) is to “empower every person and every organization on the planet to achieve more.” In line with this mission – and given Microsoft’s strong global presence, including a [vast userbase in China](https://news.microsoft.com/about-microsofts-presence-in-china/) – initiatives like MAPP play a critical role in protecting users from malicious actors. However, such programs require strong safeguards and clear accountability, and ensuring full compliance can be difficult. In unique contexts such as China’s centralized vulnerability disclosure system, the inclusion of Chinese companies warrants special scrutiny, especially those participating in domestic programs that incentivize reporting vulnerabilities to the state.

Unfortunately for Microsoft’s userbase in China, the government incentivizes behavior which should jeopardize the continuing participation of legitimately defensive companies in MAPP. It is the role of the PRC government to enforce laws on companies operating within its jurisdiction and responding to its policies. In consideration of Microsoft’s pursuit of adequate defense and support of its users, and in line with the company’s mission statement, it may be appropriate for Microsoft to temporarily suspend PRC-based companies from MAPP pending an investigation by the PRC government into the potential violation of Microsoft’s NDA with local companies. Microsoft has the systemic importance to request such an investigation, as the behavior clearly jeopardizes the safe operation of Critical Information Infrastructure under the PRC Cyber Security Law.

_Natto Thoughts is a reader-supported publication. Your paid subscription supports access for all and serves as a token of appreciation for the efforts of the Natto Team._

Subscribe

[![Deanna Hodgin's avatar](https://substackcdn.com/image/fetch/$s_!4s6Z!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd00376ed-12b8-4a8b-baea-a9a45eff861d_144x144.png)](https://substack.com/profile/13991025-deanna-hodgin)

[![Dakota's avatar](https://substackcdn.com/image/fetch/$s_!vioL!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf7de472-977a-48d8-b2e8-96f3bfa933bc_88x88.jpeg)](https://substack.com/profile/24245255-dakota)

[![Jamie Williams's avatar](https://substackcdn.com/image/fetch/$s_!HXmo!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3c6ff9d5-41a6-44ef-b7f2-939decab31cc_3464x3464.png)](https://substack.com/profile/317244637-jamie-williams)

[![Eugenio Benincasa's avatar](https://substackcdn.com/image/fetch/$s_!-Wtv!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F09a1f79e-07d1-4938-9147-e0df8440802f_800x800.jpeg)](https://substack.com/profile/5401290-eugenio-benincasa)

[![NetAskari's avatar](https://substackcdn.com/image/fetch/$s_!BsZQ!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fda139f3d-df22-454a-b176-0da7a3c2cc34_1328x1328.png)](https://substack.com/profile/43092822-netaskari)

17 Likes∙

[8 Restacks](https://substack.com/note/p-169760037/restacks?utm_source=substack&utm_content=facepile-restacks)

17

[2](https://nattothoughts.substack.com/p/when-privileged-access-falls-into/comments)
8

Share

PreviousNext

|     |     |
| --- | --- |
| [![Dakota Cary's avatar](https://substackcdn.com/image/fetch/$s_!D_sy!,w_52,h_52,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff14100c6-832f-4739-84c8-88b8137c5382_400x400.jpeg)](https://substack.com/@dakotaksg) | A guest post by

|     |     |
| --- | --- |
| [Dakota Cary](https://substack.com/@dakotaksg?utm_campaign=guest_post_bio&utm_medium=web)<br>Dakota provides insights to clients on China's hacking teams, their capabilities and research, and the industrial policies that drive their behavior. | [Subscribe to Dakota](https://intel.ks.group/subscribe?) | |

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

[![Mary Jo's avatar](https://substackcdn.com/image/fetch/$s_!xsBt!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbbc6e9c1-b64a-4c0a-9a72-f5abd4c7fba0_144x144.png)](https://substack.com/profile/298741713-mary-jo?utm_source=comment)

[Mary Jo](https://substack.com/profile/298741713-mary-jo?utm_source=substack-feed-item)

[Aug 3](https://nattothoughts.substack.com/p/when-privileged-access-falls-into/comment/141673560 "Aug 3, 2025, 3:42 AM")

Liked by Natto Team

Concise and clear. Well done

Expand full comment

Like (1)

Reply

Share

[![Franco Magno's avatar](https://substackcdn.com/image/fetch/$s_!Tjml!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F33163c87-4ebb-44cf-aaaf-ca3289aa6e8c_144x144.png)](https://substack.com/profile/12785859-franco-magno?utm_source=comment)

[Franco Magno](https://substack.com/profile/12785859-franco-magno?utm_source=substack-feed-item)

[Aug 3](https://nattothoughts.substack.com/p/when-privileged-access-falls-into/comment/141669780 "Aug 3, 2025, 3:07 AM")

Liked by Eugenio Benincasa

Top

Expand full comment

Like (1)

Reply

Share

TopLatestDiscussions

[i-SOON: Another Company in the APT41 Network](https://nattothoughts.substack.com/p/i-soon-another-company-in-the-apt41)

[A lawsuit casts light on the ecosystem of IT companies related to Chengdu 404, the company allegedly behind Chinese state-sponsored hacking group APT41.](https://nattothoughts.substack.com/p/i-soon-another-company-in-the-apt41)

Oct 26, 2023•
[Natto Team](https://substack.com/@nattothoughts)

15

[2](https://nattothoughts.substack.com/p/i-soon-another-company-in-the-apt41/comments)

![](https://substackcdn.com/image/fetch/$s_!4WzG!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa8b88094-6521-4bac-9ac4-1e77907bc727_925x354.png)

[Troll Humor](https://nattothoughts.substack.com/p/troll-humor)

[Tongue in cheek, divisive online personas pursue Russian disinformation goals](https://nattothoughts.substack.com/p/troll-humor)

Apr 21, 2023•
[Natto Team](https://substack.com/@nattothoughts)

[View comments (0)](https://nattothoughts.substack.com/p/troll-humor/comments)

![](https://substackcdn.com/image/fetch/$s_!PK25!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0a5146fc-8bd0-4755-81df-228153d92901_1415x823.png)

[Salt Typhoon: the Other Shoe Has Dropped, but Consternation Continues](https://nattothoughts.substack.com/p/salt-typhoon-the-other-shoe-dropped)

[Sichuan Juxinhe, directly involved in the Salt Typhoon cyber operations, resembles a front company of the Chinese Ministry of State Security](https://nattothoughts.substack.com/p/salt-typhoon-the-other-shoe-dropped)

Jan 22•
[Natto Team](https://substack.com/@nattothoughts)

19

[View comments (0)](https://nattothoughts.substack.com/p/salt-typhoon-the-other-shoe-dropped/comments)

![](https://substackcdn.com/image/fetch/$s_!rXx1!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5ae93815-675b-4259-b8a8-ada48009435f_550x405.jpeg)

See all

Ready for more?

Subscribe
