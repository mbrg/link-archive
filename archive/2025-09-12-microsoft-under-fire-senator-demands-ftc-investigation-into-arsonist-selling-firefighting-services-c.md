---
date: '2025-09-12'
description: Senator Ron Wyden has called for an FTC investigation into Microsoft,
  labeling it "gross cybersecurity negligence" related to ransomware attacks exploiting
  long-known Windows vulnerabilities. Wyden's critique centers on Microsoft's continued
  use of outdated RC4 encryption in Active Directory, which facilitates attacks like
  Kerberoasting. This has enabled widespread breaches, notably the Ascension Health
  incident, which compromised 5.6 million records. With Microsoft's security division
  generating over $20 billion, concerns arise over its dual approach—selling add-on
  cybersecurity services while neglecting core product security. The implications
  could reshape industry standards for secure software development.
link: https://www.csoonline.com/article/4055697/microsoft-under-fire-senator-demands-ftc-investigation-into-arsonist-selling-firefighting-services.html
tags:
- Microsoft
- FTC investigation
- ransomware
- vulnerabilities
- cybersecurity
title: 'Microsoft under fire: Senator demands FTC investigation into ‘arsonist selling
  firefighting services’ ◆ CSO Online'
---

by [Gyana Swain](https://www.csoonline.com/profile/gyana-swain-2/)

# Microsoft under fire: Senator demands FTC investigation into ‘arsonist selling firefighting services’

News

Sep 11, 20256 mins

[Security](https://www.csoonline.com/security/)[Vulnerabilities](https://www.csoonline.com/vulnerabilities/)

## US Senator Ron Wyden has called for accountability after healthcare ransomware attacks exposed Windows vulnerabilities that Microsoft had known about for over a decade.

![Auckland / New Zealand - November 7 2019: View of Microsoft office building](https://www.csoonline.com/wp-content/uploads/2025/09/4055697-0-18903900-1757595834-shutterstock_1555135388.jpg?quality=50&strip=all&w=1024)

Credit: Emagnetic / Shutterstock

US Senator Ron Wyden has formally requested that the Federal Trade Commission investigate Microsoft for what he characterized as “gross cybersecurity negligence” that had enabled widespread ransomware attacks against critical infrastructure, including healthcare organizations.

In a four-page letter to FTC Chair Andrew Ferguson, the Oregon Democrat documented how Microsoft’s software engineering decisions had enabled ransomware attacks.

“Microsoft has become like an arsonist selling firefighting services to their victims,” Wyden wrote in the [letter](https://www.wyden.senate.gov/imo/media/doc/wyden_letter_to_ftc_on_microsoft_kerberoasting_ransomwarepdf.pdf), arguing that the company had built a profitable cybersecurity business while simultaneously leaving its core products vulnerable to attack.

The letter presented a detailed case study of the February 2024 ransomware attack against [Ascension Health](https://www.csoonline.com/article/3480397/how-cyber-insurance-shapes-risk-ascension-and-the-limits-of-lessons-learned.html) that compromised 5.6 million patient records, demonstrating how Microsoft’s default security configurations enabled hackers to move from a single infected laptop to an organization-wide breach.

## When one click brought down a hospital system

The [Ascension attack](https://www.csoonline.com/article/3480397/how-cyber-insurance-shapes-risk-ascension-and-the-limits-of-lessons-learned.html?utm=hybrid_search) began when a contractor using an Ascension laptop clicked on a malicious link from a Microsoft Bing search result. The malware spread laterally through Ascension’s network, eventually compromising administrative accounts on the organization’s Microsoft Active Directory server.

The hackers exploited a technique called Kerberoasting, which leveraged Microsoft’s continued default support for RC4 encryption — a technology from the 1980s that federal agencies had warned against for more than a decade.

“That’s exactly what played out in the Ascension case, where one weak default snowballed into a ransomware disaster,” said Sanchit Vir Gogia, chief analyst and CEO at Greyhound Research.

“Because of dangerous software engineering decisions by Microsoft, which the company has largely hidden from its corporate and government customers, a single individual at a hospital or other organization clicking on the wrong link can quickly result in an organization-wide ransomware infection,” Wyden wrote in the letter.

## The technical reality behind the failures

Security experts have long criticized Microsoft’s reliance on outdated encryption standards. “RC4 should have been retired long ago, yet it still lurks in Active Directory and continues to enable attacks like Kerberoasting,” Gogia noted.

Microsoft’s justification centered on backward compatibility concerns. “Microsoft’s line has been that switching it off overnight could break older systems,” Gogia explained. “That may be true, but after more than a decade of warnings, the argument has become increasingly difficult to sustain.”

Wyden detailed how “Microsoft’s continued support for the ancient, insecure RC4 encryption technology needlessly exposes its customers to ransomware and other cyber threats by enabling hackers that have gained access to any computer on a corporate network to crack the passwords of privileged accounts used by administrators.”

## The $20 billion security business

Microsoft’s security division now generates more than $20 billion annually, much of it from features that addressed gaps in the company’s core products. “Features such as advanced logging, which many assumed were part of the core product, sat behind premium licenses until the Exchange Online hack forced Microsoft to expand access,” Gogia observed.

Wyden argued that “instead of delivering secure software to its customers, Microsoft has built a multibillion-dollar secondary business selling cybersecurity add-on services to those organizations that can afford it.”

This created what enterprise customers described as a double-billing problem. “That’s why CIOs describe the feeling as being billed twice — once for the platform, and again for the peace of mind,” Gogia said.

Wyden captured this dynamic with his pointed criticism: “At this point, Microsoft has become like an arsonist selling firefighting services to their victims.”

## Broken promises and regulatory pressure

When Wyden’s staff briefed senior Microsoft officials about the Kerberoasting threat in July 2024, the letter added, they “specifically requested that Microsoft publish and publicize clear guidance in plain English so that senior executives would understand this serious, avoidable cyber risk.”

Microsoft’s response fell short, publishing guidance as “a highly technical blog post on an obscure area of the company’s website on a Friday afternoon.” The company also promised to release a software update disabling RC4 encryption, but eleven months later, “Microsoft has yet to release that promised security update,” Wyden noted.

The regulatory implications remained uncertain. “A full-blown FTC case against Microsoft on the basis of weak defaults still feels unlikely,” Gogia said. However, he noted that “the Cyber Safety Review Board’s report from last year complicates the picture. It concluded Microsoft’s security culture was inadequate and accused the company of avoidable mistakes in a government email breach.”

## What CISOs are doing now

Enterprise security leaders weren’t waiting for Microsoft or regulators to act. “CISOs are already acting as though Wyden’s points are proven,” Gogia said. “They’re disabling RC4 manually, mandating longer passwords for service accounts, and pushing multi-factor authentication across the board.”

Organizations were increasingly using procurement contracts as leverage. “Contracts are starting to include clauses demanding configuration reports and baseline protections,” Gogia noted. “In some cases, workloads are being threatened with migration unless these terms are met.”

## Industry-wide implications

The implications of Wyden’s investigation could reshape how the entire software industry approaches security. “If Wyden’s concerns gain ground, the implications stretch beyond Microsoft,” Gogia said. “Treating insecure defaults as negligence would change how software is built and sold.”

Wyden concluded with a stark warning: “Microsoft has utterly failed to stop or even slow down the scourge of ransomware enabled by its dangerous software,” and warned that “Microsoft’s culture of negligent cybersecurity, combined with its de facto monopolization of the enterprise operating system market, poses a serious national security threat and makes additional hacks inevitable.”

As Gogia summarized: “The Ascension breach has become a rallying point: one overlooked setting can take down an entire industry, so defaults are no longer trusted.”

Microsoft did not immediately respond to a request for comment.

SUBSCRIBE TO OUR NEWSLETTER

### From our editors straight to your inbox

Get started by entering your email address below.

Please enter a valid email address

Subscribe

by [Gyana Swain](https://www.csoonline.com/profile/gyana-swain-2/)

Gyana Swain is a seasoned technology journalist with over 20 years' experience covering the telecom and IT space. He is a consulting editor with VARINDIA and earlier in his career, he held editorial positions at CyberMedia, PTI, 9dot9 Media, and Dennis Publishing. A published author of two books, he combines industry insight with narrative depth. Outside of work, he’s a keen traveler and cricket enthusiast. He earned a B.S. degree from Utkal University.

## More from this author

- [news\\
**Massive npm supply chain attack hits 18 popular packages with 2B weekly downloads** \\
Sep 9, 2025 6 mins](https://www.csoonline.com/article/4053725/massive-npm-supply-chain-attack-hits-18-popular-packages-with-2b-weekly-downloads.html)
- [news\\
**Wave of npm supply chain attacks exposes thousands of enterprise developer credentials** \\
Aug 28, 2025 1 min](https://www.infoworld.com/article/4047739/wave-of-npm-supply-chain-attacks-exposes-thousands-of-enterprise-developer-credentials.html)
- [news\\
**Russian hackers exploit old Cisco flaw to target global enterprise networks** \\
Aug 21, 2025 5 mins](https://www.csoonline.com/article/4043721/russian-hackers-exploit-old-cisco-flaw-to-target-global-enterprise-networks.html)
- [news\\
**Lenovo chatbot breach highlights AI security blind spots in customer-facing systems** \\
Aug 20, 2025 6 mins](https://www.csoonline.com/article/4043005/lenovo-chatbot-breach-highlights-ai-security-blind-spots-in-customer-facing-systems.html)
- [news\\
**Silicon under siege: Nation-state hackers target semiconductor supply chains** \\
Aug 13, 2025 6 mins](https://www.csoonline.com/article/4038979/silicon-under-siege-nation-state-hackers-target-semiconductor-supply-chains.html)
- [news\\
**‘EDR-on-EDR Violence’: Hackers turn security tools against each other** \\
Jul 31, 2025 5 mins](https://www.csoonline.com/article/4032009/edr-on-edr-violence-hackers-turn-security-tools-against-each-other.html)
- [news\\
**Palo Alto Networks to buy CyberArk for $25B as identity security takes center stage** \\
Jul 30, 2025 5 mins](https://www.csoonline.com/article/4031259/palo-alto-networks-to-buy-cyberark-for-25b-as-identity-security-takes-center-stage.html)
- [news\\
**Clorox sues Cognizant for $380M over alleged helpdesk failures in cyberattack** \\
Jul 23, 2025 6 mins](https://www.csoonline.com/article/4027266/clorox-sues-cognizant-for-380m-over-alleged-helpdesk-failures-in-cyberattack.html)

## Show me more

PopularArticlesPodcastsVideos

[opinion\\
\\
**Why domain-based attacks will continue to wreak havoc** \\
\\
By Yash Mehta\\
\\
Sep 12, 202512 mins\\
\\
CyberattacksCybercrimePhishing\\
\\
![Image](https://www.csoonline.com/wp-content/uploads/2025/09/4055796-0-51560400-1757675090-domain-name-system_dns-security_data-center_lock_icann-100789391-orig.jpg?quality=50&strip=all&w=375)](https://www.csoonline.com/article/4055796/why-domain-based-attacks-will-continue-to-wreak-havoc.html)

[feature\\
\\
**12 digital forensics certifications to accelerate your cyber career** \\
\\
By Eric Frank\\
\\
Sep 12, 202513 mins\\
\\
CertificationsIT Training Investigation and Forensics\\
\\
![Image](https://www.csoonline.com/wp-content/uploads/2025/09/4054289-0-00574100-1757660502-shutterstock_1590824884.jpg?quality=50&strip=all&w=444)](https://www.csoonline.com/article/4054289/12-digital-forensics-certifications-to-accelerate-your-cyber-career.html)

[news\\
\\
**Microsoft under fire: Senator demands FTC investigation into ‘arsonist selling firefighting services’** \\
\\
By Gyana Swain\\
\\
Sep 11, 20256 mins\\
\\
SecurityVulnerabilities\\
\\
![Image](https://www.csoonline.com/wp-content/uploads/2025/09/4055697-0-18903900-1757595834-shutterstock_1555135388.jpg?quality=50&strip=all&w=375)](https://www.csoonline.com/article/4055697/microsoft-under-fire-senator-demands-ftc-investigation-into-arsonist-selling-firefighting-services.html)

[podcast\\
\\
**Navigating ransomware attacks while proactively managing cyber risks** \\
\\
Jun 20, 202517 mins\\
\\
CybercrimeRansomware\\
\\
![Image](https://www.csoonline.com/wp-content/uploads/2025/06/0-84732300-1750955491-jason-thumb-16x9-1.jpg?quality=50&strip=all&w=444)](https://www.csoonline.com/podcast/4010157/navigating-ransomware-attacks-while-proactively-managing-cyber-risks.html)

[podcast\\
\\
**CSO Executive Sessions: How AI and LLMs are affecting security in the financial services industry** \\
\\
Mar 20, 202513 mins\\
\\
CSO and CISOFinancial Services IndustrySecurity Operations Center\\
\\
![Image](https://www.csoonline.com/wp-content/uploads/2025/08/0-65286700-1754656177-Mandy-Thumb-16x9-1.jpg?quality=50&strip=all&w=444)](https://www.csoonline.com/podcast/3849977/cso-executive-sessions-how-ai-and-llms-are-affecting-security-in-the-financial-services-industry.html)

[podcast\\
\\
**CSO Executive Sessions: How cybersecurity impacts company ratings - A fey factor for investors and consumers** \\
\\
Feb 12, 202527 mins\\
\\
Security\\
\\
![Image](https://www.csoonline.com/wp-content/uploads/2025/02/0-79893900-1739420575-martin-thumb-16x9-1.jpg?quality=50&strip=all&w=444)](https://www.csoonline.com/podcast/3823540/cso-executive-sessions-how-cybersecurity-impacts-company-ratings-a-fey-factor-for-investors-and-consumers.html)

[video\\
\\
**Navigating ransomware attacks while proactively managing cyber risks** \\
\\
Jun 20, 202517 mins\\
\\
CybercrimeRansomware\\
\\
![Image](https://www.csoonline.com/wp-content/uploads/2025/06/4010153-0-09450800-1750950215-youtube-thumbnail-hKXaofSGoL0.jpg?quality=50&strip=all&w=444)](https://www.csoonline.com/video/4010153/navigating-ransomware-attacks-while-proactively-managing-cyber-risks.html)

[video\\
\\
**CSO30 winner Vishwanath Nair on balancing the tech and human element of cyber defence** \\
\\
Jun 17, 202540 mins\\
\\
CSO and CISOGovernment ITHealthcare Industry\\
\\
![Image](https://www.csoonline.com/wp-content/uploads/2025/06/4007981-0-09616200-1750133914-vish-nair-thumb-16x9-V2.jpg?quality=50&strip=all&w=444)](https://www.csoonline.com/video/4007981/cso30-winner-vishwanath-nair-on-balancing-the-tech-and-human-element-of-cyber-defence.html)

[video\\
\\
**Standard Chartered’s Alvaro Garrido on AI threats and what CIOs/CISOs must know in their AI journey** \\
\\
Apr 10, 202514 mins\\
\\
CIOCSO and CISOFinancial Services Industry\\
\\
![Image](https://www.csoonline.com/wp-content/uploads/2025/04/3958918-0-38315100-1744270897-youtube-thumbnail-JENruhTNWh0.jpg?quality=50&strip=all&w=444)](https://www.csoonline.com/video/3958918/standard-chartereds-alvaro-garrido-on-ai-threats-and-what-cios-cisos-must-know-in-their-ai-journey.html)

Sponsored Links

- [Solve your most complex IT challenges with solutions that simplify your modernization journey.](http://pubads.g.doubleclick.net/gampad/clk?id=7038222634&iu=/8456/IDG.G_B2B_CIO.com)
- [Secure AI by Design: Unleash the power of AI and keep applications, usage and data secure.](http://pubads.g.doubleclick.net/gampad/clk?id=6856108221&iu=/8456/IDG.G_B2B_CSOOnline.com)
