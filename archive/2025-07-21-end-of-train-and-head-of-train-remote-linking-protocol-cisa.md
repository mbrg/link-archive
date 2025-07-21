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
link: https://www.cisa.gov/news-events/ics-advisories/icsa-25-191-10
tags:
- Industrial Control Systems
- Remote Device Security
- Transportation Safety
- Vulnerability Management
- Cybersecurity
title: End-of-Train and Head-of-Train Remote Linking Protocol | CISA
---

[Skip to main content](https://www.cisa.gov/news-events/ics-advisories/icsa-25-191-10#main)

[Free Cyber Services](https://www.cisa.gov/resources-tools/resources/free-cybersecurity-services-and-tools "Free Cyber Services") [Secure by design](https://www.cisa.gov/securebydesign) [Secure Our World](https://www.cisa.gov/node/18883) [Shields Up](https://www.cisa.gov/node/8056) [Report A Cyber Issue](https://www.cisa.gov/report)

Share:

[Share to Facebook](https://www.facebook.com/sharer/sharer.php?u=https://www.cisa.gov/news-events/ics-advisories/icsa-25-191-10&title=End-of-Train%20and%20Head-of-Train%20Remote%20Linking%20Protocol "Share to Facebook")[Share to X](https://twitter.com/intent/tweet?text=End-of-Train%20and%20Head-of-Train%20Remote%20Linking%20Protocol+https://www.cisa.gov/news-events/ics-advisories/icsa-25-191-10 "Share to X")[Share to Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.cisa.gov/news-events/ics-advisories/icsa-25-191-10 "Share to Linkedin")[Share to Email](mailto:?subject=End-of-Train%20and%20Head-of-Train%20Remote%20Linking%20Protocol&body=https://www.cisa.gov/news-events/ics-advisories/icsa-25-191-10 "Share to Email")

ICS Advisory

# End-of-Train and Head-of-Train Remote Linking Protocol

Release Date

July 10, 2025

Alert Code

ICSA-25-191-10

Related topics:

[Industrial Control System Vulnerabilities](https://www.cisa.gov/topics/industrial-control-systems/industrial-control-system-vulnerabilities), [Industrial Control Systems](https://www.cisa.gov/topics/industrial-control-systems)

[**View CSAF**(link is external)](https://github.com/cisagov/CSAF)

## 1\. EXECUTIVE SUMMARY

- **CVSS v4 7.2**
- **ATTENTION:** Low attack complexity
- **Standard:** End-of-Train and Head-of-Train remote linking protocol
- **Equipment:** End-of-Train and Head-of-Train devices
- **Vulnerability:** Weak Authentication

## 2\. RISK EVALUATION

Successful exploitation of this vulnerability could allow an attacker to send their own brake control commands to the end-of-train device, causing a sudden stoppage of the train which may lead to a disruption of operations, or induce brake failure.

## 3\. TECHNICAL DETAILS

### 3.1 AFFECTED PRODUCTS

The following version of End-of-Train and Head-of-Train remote linking protocol is affected:

- End-of-Train and Head-of-Train remote linking protocol: All versions

### 3.2 VULNERABILITY OVERVIEW

#### **3.2.1** [**WEAK AUTHENTICATION CWE-1390**(link is external)](https://cwe.mitre.org/data/definitions/1390.html)

The protocol used for remote linking over RF for End-of-Train and Head-of-Train (also known as a FRED) relies on a BCH checksum for packet creation. It is possible to create these EoT and HoT packets with a software defined radio and issue brake control commands to the EoT device, disrupting operations or potentially overwhelming the brake systems.

[CVE-2025-1727(link is external)](https://www.cve.org/CVERecord?id=CVE-2025-1727) has been assigned to this vulnerability. A CVSS v3 base score of 8.1 has been calculated; the CVSS vector string is ( [AV:A/AC:L/PR:N/UI:N/S:C/C:L/I:H/A:H(link is external)](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:H)).

A CVSS v4 score has also been calculated for [CVE-2025-1727(link is external)](https://www.cve.org/CVERecord?id=CVE-2025-1727). A base score of 7.2 has been calculated; the CVSS vector string is ( [AV:A/AC:L/AT:N/PR:N/UI:N/VC:L/VI:H/VA:H/SC:N/SI:H/SA:H(link is external)](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:A/AC:L/AT:N/PR:N/UI:N/VC:N/VI:H/VA:H/SC:N/SI:N/SA:N)).

### 3.3 BACKGROUND

- **CRITICAL INFRASTRUCTURE SECTORS:** Transportation Systems
- **COUNTRIES/AREAS DEPLOYED:** United States
- **COMPANY HEADQUARTERS LOCATION:** United States

### 3.4 RESEARCHER

Neil Smith and Eric Reuter reported this vulnerability to CISA.

## 4\. MITIGATIONS

The Association of American Railroads (AAR) is pursuing new equipment and protocols which should replace traditional End-of-Train and Head-of-Train devices. The standards committees involved in these updates are aware of the vulnerability and are investigating mitigating solutions.

The AAR Railroad Electronics Standards Committee (RESC) maintains this protocol which is used by multiple manufacturers across the industry, including Hitachi Rail STS USA, Wabtec, Siemens, and others. Users of EoT/HoT devices are recommended to contact their own device manufacturers with questions.

CISA recommends users take defensive measures to minimize the risk of exploitation of this vulnerability, such as:

- Minimize network exposure for all control system devices and/or systems, ensuring they are [not accessible from the internet](https://www.cisa.gov/uscert/ics/alerts/ICS-ALERT-10-301-01).
- Locate control system networks and remote devices behind firewalls and isolating them from business networks.
- When remote access is required, use more secure methods, such as Virtual Private Networks (VPNs), recognizing VPNs may have vulnerabilities and should be updated to the most current version available. Also recognize VPN is only as secure as the connected devices.

CISA reminds organizations to perform proper impact analysis and risk assessment prior to deploying defensive measures.

CISA also provides a section for [control systems security recommended practices](https://www.cisa.gov/resources-tools/resources/ics-recommended-practices) on the ICS webpage on [cisa.gov/ics](https://www.cisa.gov/topics/industrial-control-systems). Several CISA products detailing cyber defense best practices are available for reading and download, including [Improving Industrial Control Systems Cybersecurity with Defense-in-Depth Strategies](https://us-cert.cisa.gov/sites/default/files/recommended_practices/NCCIC_ICS-CERT_Defense_in_Depth_2016_S508C.pdf).

CISA encourages organizations to implement recommended cybersecurity strategies for [proactive defense of ICS assets](https://www.cisa.gov/sites/default/files/publications/Cybersecurity_Best_Practices_for_Industrial_Control_Systems.pdf).

Additional mitigation guidance and recommended practices are publicly available on the ICS webpage at [cisa.gov/ics](https://www.cisa.gov/topics/industrial-control-systems) in the technical information paper, [ICS-TIP-12-146-01B--Targeted Cyber Intrusion Detection and Mitigation Strategies](https://www.cisa.gov/uscert/ics/tips/ICS-TIP-12-146-01B).

Organizations observing suspected malicious activity should follow established internal procedures and report findings to CISA for tracking and correlation against other incidents.

No known public exploitation specifically targeting this vulnerability has been reported to CISA at this time. This vulnerability is not exploitable remotely.

## 5\. UPDATE HISTORY

- July 10, 2025: Initial Publication

This product is provided subject to this [Notification](https://www.cisa.gov/notification "Follow link") and this [Privacy & Use](https://www.cisa.gov/privacy-policy "Follow link") policy.

### Tags

**Sector**:
[Transportation Systems Sector](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors/transportation-systems-sector)

**Topics**:
[Industrial Control System Vulnerabilities](https://www.cisa.gov/topics/industrial-control-systems/industrial-control-system-vulnerabilities),
[Industrial Control Systems](https://www.cisa.gov/topics/industrial-control-systems)

## Please share your thoughts

We recently updated our anonymous [product survey](https://cisasurvey.gov1.qualtrics.com/jfe/form/SV_9n4TtB8uttUPaM6?product=https://www.cisa.gov/news-events/ics-advisories/icsa-25-191-10); we welcome your feedback.

## Related Advisories

Jul 17, 2025

ICS Advisory \| ICSA-25-198-01

### [Leviton AcquiSuite and Energy Monitoring Hub](https://www.cisa.gov/news-events/ics-advisories/icsa-25-198-01)

Jul 15, 2025

ICS Advisory \| ICSA-25-196-02

### [ABB RMC-100](https://www.cisa.gov/news-events/ics-advisories/icsa-25-196-02)

Jul 15, 2025

ICS Advisory \| ICSA-25-196-01

### [Hitachi Energy Asset Suite](https://www.cisa.gov/news-events/ics-advisories/icsa-25-196-01)

Jul 15, 2025

ICS Advisory \| ICSA-25-196-03

### [LITEON IC48A and IC80A EV Chargers](https://www.cisa.gov/news-events/ics-advisories/icsa-25-196-03)

|     |     |
| --- | --- |
|  |  |

|     |     |
| --- | --- |
|  |  |
