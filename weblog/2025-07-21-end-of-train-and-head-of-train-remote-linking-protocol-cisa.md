---
date: '2025-07-21'
description: CISA has issued an advisory (ICSA-25-191-10) regarding a vulnerability
  in the End-of-Train (EoT) and Head-of-Train (HoT) remote linking protocol, with
  a CVSS v4 score of 7.2. The issue, classified as weak authentication, allows attackers
  to potentially command brake systems remotely using software-defined radios, risking
  train operation stability. While exploitation requires physical proximity, CISA
  urges organizations to enhance cybersecurity measures, such as isolating control
  networks and employing VPNs. The Association of American Railroads (AAR) is developing
  standardized solutions to mitigate this risk.
link: /archive/2025-07-21-end-of-train-and-head-of-train-remote-linking-protocol-cisa.md
tags:
- Industrial Control Systems
- Remote Device Security
- Transportation Safety
- Vulnerability Management
- Cybersecurity
- weblog
title: End-of-Train and Head-of-Train Remote Linking Protocol ◆ CISA
type: weblog
---

CISA is still kicking. They stand behind the researchers doing old-school full disclosure when all else fails. This is actually pretty great of them.

---

> [CVE-2025-1727(link is external)](https://www.cve.org/CVERecord?id=CVE-2025-1727) has been assigned to this vulnerability. A CVSS v3 base score of 8.1 has been calculated; the CVSS vector string is ( [AV:A/AC:L/PR:N/UI:N/S:C/C:L/I:H/A:H(link is external)](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:H)).

Attack vector = adjacent is of course doing the heavy lifting in reducing CVSS scores. It's almost like CVSS wasn't designed for ICS..

---

> The Association of American Railroads (AAR) is pursuing new equipment and protocols which should replace traditional End-of-Train and Head-of-Train devices. The standards committees involved in these updates are aware of the vulnerability and are investigating mitigating solutions.

This investigation must be pretty thorough if it's still ongoing after 12 years.

---

> - Minimize network exposure for all control system devices and/or systems, ensuring they are [not accessible from the internet](https://www.cisa.gov/uscert/ics/alerts/ICS-ALERT-10-301-01). - Locate control system networks and remote devices behind firewalls and isolating them from business networks. - When remote access is required, use more secure methods, such as Virtual Private Networks (VPNs), recognizing VPNs may have vulnerabilities and should be updated to the most current version available. Also recognize VPN is only as secure as the connected devices.

If you somehow put this on the Internet too then (1) it's time to hire security folks, (2) you are absolutely already owned.

For everyone else -- why is this useful advice? This is exploited via RF, no?

---

> No known public exploitation specifically targeting this vulnerability has been reported to CISA at this time. This vulnerability is not exploitable remotely.

500 meters away is remote exploitation when you're talking about a vuln that will probably be used by nation states only.
