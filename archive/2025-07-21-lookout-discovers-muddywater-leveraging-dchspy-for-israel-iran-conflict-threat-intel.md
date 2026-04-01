---
date: '2025-07-21'
description: Lookout has detected new instances of DCHSpy, an Android surveillanceware
  utilized by the Iranian APT MuddyWater amid rising tensions in the Israel-Iran conflict.
  This malware, aimed at government and private sector targets, captures extensive
  data—WhatsApp messages, files, location—exploiting social engineering tactics via
  lures related to Starlink internet service. Notably, DCHSpy shares infrastructure
  with SandStrike and employs malicious VPN apps promoted over Telegram. The rapid
  evolution of this malware underscores ongoing risks to digital sovereignty, particularly
  for activists, as nation-state surveillance intensifies during geopolitical crises.
  Continuous monitoring of MuddyWater’s activities is imperative.
link: https://www.lookout.com/threat-intelligence/article/lookout-discovers-iranian-dchsy-surveillanceware
tags:
- MuddyWater
- DCHSpy
- Android
- Cybersecurity
- Spyware
title: Lookout Discovers MuddyWater Leveraging DCHSpy For Israel-Iran Conflict ◆ Threat
  Intel
---

[![Lookout Logo](https://cdn.prod.website-files.com/64ad8cecda5417d65d91a876/64ad8cecda5417d65d91a893_logo-footer.svg)](https://www.lookout.com/)

In-Depth Analysis

Android

Spyware

July 21, 2025

# Lookout Discovers Iranian APT MuddyWater Leveraging DCHSpy During Israel-Iran Conflict

![](https://cdn.prod.website-files.com/64ad8cecda5417d65d91a876/6538402be65965bcc1d1df4c_threat-gradient.webp)

![A spy dressed in a trench coat printed with the Iranian flag](https://cdn.prod.website-files.com/64ad8cecda5417d65d91a8b7/687a4b10d3e24ab489160c1d_DCHSpy.png)

- Lookout discovered four new samples of DCHSpy one week after the start of the Israel-Iran conflict.
- DCHSpy is an Android surveillanceware tool leveraged by Iranian cyber espionage group MuddyWater.
- DCHSpy collects WhatsApp data, accounts, contacts, SMS, files, location, and call logs, and can record audio and take photos.
- It appears that new targeting could be using lures centered around StarLink, which offered internet access to Iranians during the imposed internet outage.

DCHSpy is an Android surveillanceware family that Lookout customers have been protected from since 2024. It is likely developed and maintained by MuddyWater, which is a cyber espionage group believed to be affiliated with Iran's Ministry of Intelligence and Security (MOIS). This group targets diverse government and private entities in various sectors, such as telecommunications, local government, defense, and oil and natural gas, across the Middle East, Asia, Africa, Europe, and North America.

In light of the recent conflict in Iran, it appears that new versions of DCHSpy are being deployed against adversaries. It uses political lures and disguises as legitimate apps like VPNs or banking applications. This modular malware collects the following data:

- Accounts logged into on the device
- Contacts
- SMS messages
- Files stored on the device
- Location data
- Call logs
- Audio by taking control of the microphone
- Photos by taking control of the camera
- WhatsApp data

DCHSpy shares infrastructure with another Android malware known as SandStrike, an Android surveillanceware targeting Baháʼí practitioners originally reported publicly by Kaspersky in 2022. Lookout researchers discovered that the hardcoded command and control (C2) IP address in the SandStrike sample was also used multiple times to deploy a PowerShell RAT attributed to MuddyWater. Notably, the SandStrike sample also contained a malicious VPN configuration file tied to threat actor controlled infrastructure.

DCHSpy uses similar tactics and infrastructure as SandStrike. It is distributed to targeted groups and individuals by leveraging malicious URLs shared directly over messaging apps such as Telegram.

### New Capabilities, Targeting, and StarLink Lures

About a week after Israel launched its initial strikes on Iranian nuclear infrastructure, Lookout acquired four new samples of DCHSpy. These new samples show that MuddyWater has continued to develop the surveillanceware with new capabilities - this time exhibiting the ability to identify and exfiltrate data from files of interest on the device as well as WhatsApp data.

‍

![](https://cdn.prod.website-files.com/64ad8cecda5417d65d91a8b7/687a4bffe513f916403f3884_AD_4nXcO3s7HAVJ9JID5QhXm2lzoTNGL-mSqAtyArNipr2LqXWeQcajvIulWzDSlMZgWRSixAMiXs_PqRk9Sow3yhxbTNT4x-AfsJ4LssX6bvqFwHcH_L7HQzdVUPL5q2f9Ekbse6pNZ.png)

![](https://cdn.prod.website-files.com/64ad8cecda5417d65d91a8b7/687a4c6fbabe81f9d275df72_Screenshot%202025-07-18%20at%2009.29.20.png)

One of the Earth VPN samples, SHA1:9dec46d71289710cd09582d84017718e0547f438, was uploaded with an APK filename of starlink\_vpn(1.3.0)-3012 (1).apk. This may indicate that DCHSpy VPN samples are also being spread with Starlink lures, especially given recent reports of Starlink offering internet services to the Iranian population during the internet outage imposed by the Iranian government following hostilities between Israel and Iran.

Once data is collected off of an infected device, it is compressed and encrypted with a password it receives from the command and control (C2) server. Following additional commands from the C2 server, the data is uploaded to the destination Secure File Transfer Protocol (SFTP) server.

### Parallel Tactics

When Lookout first disclosed research on DCHSpy to its Threat Advisory Service customers, we highlighted that MuddyWater leveraged a malicious VPN app that was distributed via Telegram as these new samples are. The Telegram channels advertise the malicious VPN applications to English and Farsi speakers, and feature themes and language consistent with views contrary to the Iranian regime. In previous reporting, the threat actor advertised _HideVPN_ and led victims to the following webpage:

![](https://cdn.prod.website-files.com/64ad8cecda5417d65d91a8b7/687a4fff69372b8269cfaa56_AD_4nXeml-5GVVH8h53NGOt-dVjEoyqhh3tdyMI4zpvlP5otIC-3xq4aq_vMx1GnFR6PPm7WlGHm37RlruzOyNVjjelbMQzkCdKpgl0lKgdLG8ld6jAgzmvxBnJ0RHuBVLGV25Zg53avjQ.png)

_The malicious VPN distribution page from July 2024_

In the discovery of this most recent version of DCHSpy, the actor is now advertising two malicious VPN services called _EarthVPN_ and _ComodoVPN_. Below is an example of the ComodoVPN distribution page, which is a similarly simple webpage as we saw with the _Hide VPN_ page above. Comodo VPN claims to be located in Canada and Earth VPN claims to be located in Romania. They list addresses and contact numbers from these countries which actually belong to random businesses in those respective countries.

![](https://cdn.prod.website-files.com/64ad8cecda5417d65d91a8b7/687a4fff69372b8269cfaa61_AD_4nXeUPRGVctjRzfwTDO9T7AAb13nBiM2VbFPIVW6sGdmD9TH-DtC8FvQ4FKATpYIH7y4g7NJP2lSav_S8GcW9UNnlYIZ4zCjibHzjnsgPY3UPDvQ9dxp8mem_OzsxQ0s5mdDPHqrc.png)

_The malicious VPN distribution page from June 2025, which is notably targeted at activists and journalists globally._

‍

### Continued Observation and Research

Threat actors tied to the Iranian government are no strangers in the mobile surveillanceware landscape. Lookout’s research team tracks 17 unique mobile malware families tied to at least 10 Iranian APTs with activity spanning over a decade, along with multiple campaigns conducted with commodity spyware such as Metasploit, AndroRat and AhMyth. In addition to this continued activity around DCHSpy, Lookout researchers also disclosed [BouldSpy](https://www.lookout.com/threat-intelligence/article/iranian-spyware-bouldspy) in 2023. At the time, BouldSpy was a novel Android surveillanceware tool used by the Law Enforcement Command of the Islamic Republic of Iran (FARAJA).

These most recent samples of DCHSpy indicate continued development and usage of the surveillanceware as the situation in the Middle East evolves, especially as Iran cracks down on its citizens following the ceasefire with Israel. Lookout researchers have observed countless instances of nation-states monitoring threats to their authority and spying on enemy soldiers during times of conflict by quietly delivering malicious apps to their mobile devices through social engineering. Recent examples include the [GuardZoo surveillanceware](https://www.lookout.com/threat-intelligence/article/guardzoo-houthi-android-surveillanceware) tied to the Houthis, an Iranian proxy, and campaigns [targeting Assad’s forces](https://newlinesmag.com/reportage/how-a-spyware-app-compromised-assads-army/) in Syria using the commodity malware SpyMax.

Lookout will continue to track MuddyWater’s activity and inform our threat intelligence customers of any relevant updates.

‍

### Indicators of Compromise (IoCs)

**SHA1s**

556d7ac665fa3cc6e56070641d4f0f5c36670d38

7010e2b424eadfa261483ebb8d2cca4aac34670c

8f37a3e2017d543f4a788de3b05889e5e0bc4b06

9dec46d71289710cd09582d84017718e0547f438

6c291b3e90325bea8e64a82742747d6cdce22e5b

7267f796581e4786dbc715c6d62747d27df09c61

67ab474e08890c266d242edaca7fab1b958d21d4

f194259e435ff6f099557bb9675771470ab2a7e3

cb2ffe5accc89608828f5c1cd960d660aac2971d

‍

**Command and Control:**

https://it1\[.\]comodo-vpn\[.\]com:1953

https://it1\[.\]comodo-vpn\[.\]com:1950

https://r1\[.\]earthvpn\[.\]org:3413

https://r2\[.\]earthvpn\[.\]org:3413

http://192.121.113\[.\]60/dev/run.php

http://79.132.128\[.\]81/dev/run.php

n14mit69company\[.\]top

https://hs1.iphide\[.\]net:751

https://hs2.iphide\[.\]net:751

https://hs3.iphide\[.\]net:751

https://hs4.iphide\[.\]net:751

http://194.26.213\[.\]176/class/mcrypt.php

http://45.86.163\[.\]10/class/mcrypt.php

http://46.30.188\[.\]243/class/mcrypt.php

http://77.75.230\[.\]135/class/mcrypt.php

http://185.203.119\[.\]134/DP/dl.php

### Authors

![](https://cdn.prod.website-files.com/64ad8cecda5417d65d91a8b7/64ad8cecda5417d65d91d4da_icons8-article-50%20(1).png)

Entry Type

In-Depth Analysis

![](https://cdn.prod.website-files.com/64ad8cecda5417d65d91a8b7/64ad8cecda5417d65d91d4d7_icons8-android-50.png)

Platform(s) Affected

Android

![](https://cdn.prod.website-files.com/64ad8cecda5417d65d91a8b7/64ad8cecda5417d65d91d4dc_icons8-spy-50.png)

Threat Type

Spyware

![](https://cdn.prod.website-files.com/64ad8cecda5417d65d91a876/64b7175a82e0c534d8aa1f53_platform-40x40.png)

Platform(s) Affected

In-Depth Analysis

Android

Spyware

## Related Content

[**Lookout Discovers Iranian APT MuddyWater Leveraging DCHSpy During Israel-Iran Conflict** \\
\\
Lookout discovered four new samples of DCHSpy one week after the start of the Israel-Iran conflict. It is likely developed and maintained by MuddyWater, part of Iran's MOIS\\
\\
Read Threat Article](https://www.lookout.com/threat-intelligence/article/lookout-discovers-iranian-dchsy-surveillanceware)

[**Lookout Discovers Massistant Chinese Mobile Forensic Tooling** \\
\\
Massistant is a mobile forensics application used by law enforcement in China to collect extensive information from mobile devices.\\
\\
Read Threat Article](https://www.lookout.com/threat-intelligence/article/massistant-chinese-mobile-forensics)

[**MultiApp-MultiCVE-2025-4609-4664** \\
\\
Google disclosed two vulnerabilities in Chrome, while a new zero-day was discovered in versions of Microsoft Edge\\
\\
Read Threat Article](https://www.lookout.com/threat-intelligence/article/multiapp-multicve-2025-4609-4664)

![A person with a prosthetic arm working on a computer](https://cdn.prod.website-files.com/64ad8cecda5417d65d91a8b7/64ad8cecda5417d65d91d334_lookout-threat-intelligence.jpg)![](https://cdn.prod.website-files.com/64ad8cecda5417d65d91a876/653fd7d50c8fbec5baf3bb6d_bottom-cta.png)

### Identify and Prevent Threats with Lookout Threat Advisory

### Stop Cyberattacks Before They Start With Industry-Leading Threat Intelligence.

Lookout Threat Advisory offers advanced mobile threat intelligence, leveraging millions of devices in our global network and top security research insights to protect your organization.

[![](https://cdn.prod.website-files.com/64ad8cecda5417d65d91a876/64ad8cecda5417d65d91a8dd_dark-green.svg)\\
\\
Learn More Today](https://www.lookout.com/products/endpoint-security/threat-intelligence) [![](https://cdn.prod.website-files.com/64ad8cecda5417d65d91a876/64ad8cecda5417d65d91a8dd_dark-green.svg)\\
\\
Schedule Demo](https://www.lookout.com/contact/request-a-demo)

| Header | Header | Header | Header |
| --- | --- | --- | --- |
| Cell | Cell | Cell | Cell |
| Cell | Cell | Cell | Cell |
| Cell | Cell | Cell | Cell |
| Cell | Cell | Cell | Cell |
