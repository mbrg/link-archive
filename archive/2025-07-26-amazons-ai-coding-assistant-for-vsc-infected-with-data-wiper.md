---
date: '2025-07-26'
description: Amazon's AI coding assistant for Visual Studio Code experienced a security
  breach where a data-wiping payload was injected into version 1.84.0 of the Amazon
  Q Developer Extension. The attacker submitted malicious code that could have deleted
  local files and AWS resources, disguising it as a system maintenance directive.
  AWS responded promptly, releasing an updated version (1.85.0) and urging users to
  upgrade. Key technical implications include concerns over software supply chain
  security and repository governance, highlighting vulnerabilities in access controls
  within open-source environments.
link: https://cyberinsider.com/amazons-ai-coding-assistant-for-vsc-infected-with-data-wiper/
tags:
- Visual Studio Code
- data wiper
- AI security
- software supply chain
- coding assistant
title: Amazon’s AI Coding Assistant for VSC Infected With Data Wiper
---

- [Skip to main content](https://cyberinsider.com/amazons-ai-coding-assistant-for-vsc-infected-with-data-wiper/#genesis-content)
- [Skip to after header navigation](https://cyberinsider.com/amazons-ai-coding-assistant-for-vsc-infected-with-data-wiper/#nav-after-header)
- [Skip to site footer](https://cyberinsider.com/amazons-ai-coding-assistant-for-vsc-infected-with-data-wiper/#site-footer)

# Amazon’s AI Coding Assistant for VSC Infected With Data Wiper

**July 25, 2025** _By_ [Bill Mann](https://cyberinsider.com/author/billmann/) — [Leave a Comment](https://cyberinsider.com/amazons-ai-coding-assistant-for-vsc-infected-with-data-wiper/#respond)

[X](https://x.com/intent/tweet?text=Amazon%E2%80%99s%20AI%20Coding%20Assistant%20for%20VSC%20Infected%20With%20Data%20Wiper&url=https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F) [LinkedIn](https://www.linkedin.com/shareArticle?title=Amazon%E2%80%99s%20AI%20Coding%20Assistant%20for%20VSC%20Infected%20With%20Data%20Wiper&url=https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F&mini=true) [Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F&title=Amazon%E2%80%99s%20AI%20Coding%20Assistant%20for%20VSC%20Infected%20With%20Data%20Wiper) [Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F)

![](https://cyberinsider.com/wp-content/uploads/2025/07/Amazons-AI-Coding-Assistant-for-VSC-Infected-With-Data-Wiper.png)

A hacker infiltrated Amazon’s AI-powered coding assistant for Visual Studio Code, injecting a destructive system-wiping prompt into version 1.84.0 of the Amazon Q Developer Extension.

Although the payload was ultimately non-functional due to formatting errors, the breach exposes serious lapses in Amazon’s software supply chain security.

The incident was [first reported by 404 Media](https://www.404media.co/hacker-plants-computer-wiping-commands-in-amazons-ai-coding-agent/). AWS [published a security advisory](https://aws.amazon.com/security/security-bulletins/AWS-2025-015/) shortly afterward, confirming the compromise and urging users to update to version 1.85.0 of the extension. The attacker, who claimed the goal was to expose “AI security theater,” submitted the malicious code directly to Amazon’s open-source GitHub repository, exploiting inadequate access controls.

Security researcher [Michael Bargury reconstructed the incident timeline](https://www.mbgsec.com/posts/2025-07-24-constructing-a-timeline-for-amazon-q-prompt-infection/) through GitHub Archive logs. The attack appears to have begun on July 13, 2025, when a user under the handle lkmanka58 submitted a commit that embedded a prompt instructing Amazon Q to delete local files and cloud infrastructure, posing as a system cleaning operation. This malicious payload was included in the scripts/extensionNode.bk file and funneled into production via a downloader script that triggered only in production environments, evading automated testing.

The hacker’s prompt included commands instructing the AI to:

- Wipe the local home directory.
- Delete AWS cloud resources using AWS CLI commands (e.g., ec2 terminate-instances, s3 rm, iam delete-user).
- Log deletions to /tmp/CLEANER.LOG.

![](https://cyberinsider.com/wp-content/uploads/2025/07/commit-1-1024x784.jpg)Prompt injection in the extension's code

**Bargury**

The prompt was framed as a system maintenance directive, but would have initiated data destruction had it been successfully executed. AWS states the code was malformed and therefore did not pose an active threat, but it was nevertheless published in a signed release and downloaded by thousands of users. The malicious version 1.84.0 was released on July 17, 2025, and remained available for at least 48 hours before being pulled and replaced with version 1.85.0 on July 19.

Amazon Q is Amazon Web Services’ generative AI assistant designed to help developers code faster through natural language interactions, code generation, and explanation features. Integrated into Visual Studio Code, the extension has over 950,000 installations and is a core part of Amazon’s push into developer-facing AI tools, similar in intent to Microsoft’s GitHub Copilot.

According to 404 Media’s review, the attacker claimed they were granted administrative permissions through a pull request from a newly created account, implying an alarming breakdown in repository governance. However, Bargury’s search of GitHub’s event logs found no trace of this PR, leaving some questions unresolved about the attacker’s precise access pathway. Git commits show the attacker leveraged Amazon’s automation tooling and reused benign commit messages to obfuscate their actions.

Amazon did not publicly acknowledge the compromised release until after 404 Media’s reporting, and the company has since removed all traces of version 1.84.0 from GitHub. In its security bulletin, AWS emphasized that no customer environments or cloud resources were affected. The malicious code was “incorrectly formatted,” preventing execution, and all credentials involved in the tampering have been revoked.

Developers using Amazon Q should immediately upgrade to version 1.85.0, and any local or forked copies of version 1.84.0 should be deleted.

If you liked this article, be sure to follow us on **[X/Twitter](https://twitter.com/CyberInsidercom)** and also **[LinkedIn](https://www.linkedin.com/company/cyberinsider/)** for more exclusive content.

* * *

## More from CyberInsider

[![Tea App Suffers Data Breach Exposing 72,000 Users' Photos and Private Messages](https://cyberinsider.com/wp-content/uploads/2025/07/Tea-App-Suffers-Data-Breach-Exposing-72000-Users-Photos-and-Private-Messages-950-x-520-px-80x80.png)](https://cyberinsider.com/tea-app-suffers-data-breach-exposing-72000-users-photos-and-private-messages/)

### [Tea App Suffers Data Breach Exposing 72,000 Users’ Photos and Private Messages](https://cyberinsider.com/tea-app-suffers-data-breach-exposing-72000-users-photos-and-private-messages/)

[![Proton VPN Signups in UK Surge 1,400% After Online Safety Act Comes Into Force](https://cyberinsider.com/wp-content/uploads/2025/07/Proton-VPN-Signups-in-UK-Surge-1400-After-Online-Safety-Act-Comes-Into-Force-80x80.jpg)](https://cyberinsider.com/proton-vpn-signups-in-uk-surge-1400-after-online-safety-act-comes-into-force/)

### [Proton VPN Signups in UK Surge 1,400% After Online Safety Act Comes Into Force](https://cyberinsider.com/proton-vpn-signups-in-uk-surge-1400-after-online-safety-act-comes-into-force/)

[![Android Hacking Services Enable Mobile Malware Attacks for $300/Month](https://cyberinsider.com/wp-content/uploads/2025/07/417-80x80.jpg)](https://cyberinsider.com/android-hacking-services-enable-mobile-malware-attacks-for-300-month/)

### [Android Hacking Services Enable Mobile Malware Attacks for $300/Month](https://cyberinsider.com/android-hacking-services-enable-mobile-malware-attacks-for-300-month/)

[![Hacking Forum Leakzone Exposed User IPs via Unsecured Database](https://cyberinsider.com/wp-content/uploads/2025/07/Hacking-Forum-Leakzone-Exposed-User-IPs-via-Unsecured-Database-80x80.jpg)](https://cyberinsider.com/hacking-forum-leakzone-exposed-user-ip-s-via-unsecured-database/)

### [Hacking Forum Leakzone Exposed User IPs via Unsecured Database](https://cyberinsider.com/hacking-forum-leakzone-exposed-user-ip-s-via-unsecured-database/)

[![Emergency Zoom meeting invites target corporate account credentials](https://cyberinsider.com/wp-content/uploads/2025/07/IMG_1906-80x80.jpeg)](https://cyberinsider.com/emergency-zoom-meeting-invites-target-corporate-account-credentials/)

### [Emergency Zoom meeting invites target corporate account credentials](https://cyberinsider.com/emergency-zoom-meeting-invites-target-corporate-account-credentials/)

[![Novel AI System ‘WhoFi’ Identifies People Using Only Wi-Fi Signals](https://cyberinsider.com/wp-content/uploads/2025/07/IMG_1904-80x80.jpeg)](https://cyberinsider.com/novel-ai-system-whofi-identifies-people-using-only-wi-fi-signals/)

### [Novel AI System ‘WhoFi’ Identifies People Using Only Wi-Fi Signals](https://cyberinsider.com/novel-ai-system-whofi-identifies-people-using-only-wi-fi-signals/)

* * *

![](https://cyberinsider.com/wp-content/themes/mai-exclusive/images/Bill-Mann-200.jpg)

#### About Bill Mann

Bill specializes in explaining complex technical topics to a non-technical audience. In his 30+ year career, he has covered many of the technological advances that shape our lives. Today, Bill uses those skills to help people protect their privacy and security against the ever-growing assaults on both.

## Reader Interactions

### Leave a Reply [Cancel reply](https://cyberinsider.com/amazons-ai-coding-assistant-for-vsc-infected-with-data-wiper/\#respond)

Your email address will not be published.Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Amazon%E2%80%99s%20AI%20Coding%20Assistant%20for%20VSC%20Infected%20With%20Data%20Wiper%20https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F) [Buffer](https://buffer.com/add?url=https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F&text=Amazon%E2%80%99s%20AI%20Coding%20Assistant%20for%20VSC%20Infected%20With%20Data%20Wiper) [Copy](https://cyberinsider.com/amazons-ai-coding-assistant-for-vsc-infected-with-data-wiper/#) [Email](mailto:?subject=Amazon%E2%80%99s%20AI%20Coding%20Assistant%20for%20VSC%20Infected%20With%20Data%20Wiper&body=https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F) [Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F) [Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F&title=Amazon%E2%80%99s%20AI%20Coding%20Assistant%20for%20VSC%20Infected%20With%20Data%20Wiper) [Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F&t=Amazon%E2%80%99s%20AI%20Coding%20Assistant%20for%20VSC%20Infected%20With%20Data%20Wiper) [Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F&text=Amazon%E2%80%99s%20AI%20Coding%20Assistant%20for%20VSC%20Infected%20With%20Data%20Wiper) [LinkedIn](https://www.linkedin.com/shareArticle?title=Amazon%E2%80%99s%20AI%20Coding%20Assistant%20for%20VSC%20Infected%20With%20Data%20Wiper&url=https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F&mini=true) [Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F&title=Amazon%E2%80%99s%20AI%20Coding%20Assistant%20for%20VSC%20Infected%20With%20Data%20Wiper) [Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F) [Mix](https://mix.com/add?url=https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F) [Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Amazon%E2%80%99s%20AI%20Coding%20Assistant%20for%20VSC%20Infected%20With%20Data%20Wiper%20https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F) [Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F&media=https://cyberinsider.com/wp-content/uploads/2025/07/Amazons-AI-Coding-Assistant-for-VSC-Infected-With-Data-Wiper.png&description=Amazon%E2%80%99s%20AI%20Coding%20Assistant%20for%20VSC%20Infected%20With%20Data%20Wiper) [Pocket](https://getpocket.com/edit?url=https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F) [Print](https://cyberinsider.com/amazons-ai-coding-assistant-for-vsc-infected-with-data-wiper/#) [Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F&title=Amazon%E2%80%99s%20AI%20Coding%20Assistant%20for%20VSC%20Infected%20With%20Data%20Wiper) [SMS](sms:?&body=Amazon%E2%80%99s%20AI%20Coding%20Assistant%20for%20VSC%20Infected%20With%20Data%20Wiper%20https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F) [Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F&text=Amazon%E2%80%99s%20AI%20Coding%20Assistant%20for%20VSC%20Infected%20With%20Data%20Wiper) [Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F) [Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F) [X](https://x.com/intent/tweet?text=Amazon%E2%80%99s%20AI%20Coding%20Assistant%20for%20VSC%20Infected%20With%20Data%20Wiper&url=https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F) [VK](https://vk.com/share.php?url=https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F) [WhatsApp](https://api.whatsapp.com/send?text=Amazon%E2%80%99s%20AI%20Coding%20Assistant%20for%20VSC%20Infected%20With%20Data%20Wiper+https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F) [Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F) [Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fcyberinsider.com%2Famazons-ai-coding-assistant-for-vsc-infected-with-data-wiper%2F&title=Amazon%E2%80%99s%20AI%20Coding%20Assistant%20for%20VSC%20Infected%20With%20Data%20Wiper&image=https://cyberinsider.com/wp-content/uploads/2025/07/Amazons-AI-Coding-Assistant-for-VSC-Infected-With-Data-Wiper.png&yumtype=button)
