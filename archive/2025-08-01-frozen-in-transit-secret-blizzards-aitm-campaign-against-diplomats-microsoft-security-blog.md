---
date: '2025-08-01'
description: Microsoft's Threat Intelligence has revealed a cyberespionage campaign
  by Russian actor Secret Blizzard, targeting foreign embassies in Moscow through
  an adversary-in-the-middle (AiTM) technique. The campaign utilizes ApolloShadow
  malware to install a trusted root certificate, allowing the actor to intercept sensitive
  data from compromised devices. The attack leverages local ISPs for access, raising
  substantial risks for diplomatic entities. Defensive recommendations include encrypting
  traffic and employing robust access controls. This underscores the growing sophistication
  of state-sponsored threats, emphasizing the need for heightened vigilance and adaptive
  cybersecurity measures within sensitive environments.
link: https://www.microsoft.com/en-us/security/blog/2025/07/31/frozen-in-transit-secret-blizzards-aitm-campaign-against-diplomats/
tags:
- network defense
- cybersecurity
- adversary-in-the-middle
- threat intelligence
- malware analysis
title: 'Frozen in transit: Secret Blizzard’s AiTM campaign against diplomats ◆ Microsoft
  Security Blog'
---

[Skip to main content](javascript:void(0))

![](https://www.microsoft.com/en-us/security/blog/wp-content/themes/security-blog-2025/dist/images/single-bg.jpg)

![](https://www.microsoft.com/en-us/security/blog/wp-content/themes/security-blog-2025/dist/images/single-bg-dark.jpg)

* * *

## Share

- [Link copied to clipboard!](https://www.microsoft.com/en-us/security/blog/2025/07/31/frozen-in-transit-secret-blizzards-aitm-campaign-against-diplomats/)
- [Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https://www.microsoft.com/en-us/security/blog/2025/07/31/frozen-in-transit-secret-blizzards-aitm-campaign-against-diplomats/)
- [Share on X](https://twitter.com/intent/tweet?url=https://www.microsoft.com/en-us/security/blog/2025/07/31/frozen-in-transit-secret-blizzards-aitm-campaign-against-diplomats/&text=Frozen+in+transit%3A+Secret+Blizzard%E2%80%99s+AiTM+campaign+against+diplomats)
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https://www.microsoft.com/en-us/security/blog/2025/07/31/frozen-in-transit-secret-blizzards-aitm-campaign-against-diplomats/)

## Content types

- [Research](https://www.microsoft.com/en-us/security/blog/content-type/research/)

## Products and services

- [Microsoft Defender](https://www.microsoft.com/en-us/security/blog/product/microsoft-defender/)
- [Microsoft Defender for Endpoint](https://www.microsoft.com/en-us/security/blog/product/microsoft-defender-for-endpoint/)
- [Microsoft Defender XDR](https://www.microsoft.com/en-us/security/blog/product/microsoft-defender-xdr/)

## Topics

- [Threat intelligence](https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/)

Microsoft Threat Intelligence has uncovered a cyberespionage campaign by the Russian state actor we track as Secret Blizzard that has been targeting embassies located in Moscow using an adversary-in-the-middle (AiTM) position to deploy their custom ApolloShadow malware. ApolloShadow has the capability to install a trusted root certificate to trick devices into trusting malicious actor-controlled sites, enabling Secret Blizzard to maintain persistence on diplomatic devices, likely for intelligence collection. This campaign, which has been ongoing since at least 2024, poses a high risk to foreign embassies, diplomatic entities, and other sensitive organizations operating in Moscow, particularly to those entities who rely on local internet providers.

While we previously assessed with low confidence that the actor conducts cyberespionage activities within Russian borders against foreign and domestic entities, this is the first time we can confirm that they have the capability to do so at the Internet Service Provider (ISP) level. This means that diplomatic personnel using local ISP or telecommunications services in Russia are highly likely targets of Secret Blizzard’s AiTM position within those services. In our previous [blog](https://www.microsoft.com/security/blog/2024/12/04/frequent-freeloader-part-i-secret-blizzard-compromising-storm-0156-infrastructure-for-espionage/), we reported the actor likely leverages Russia’s domestic intercept systems such as the [System for Operative Investigative Activities](https://www.welivesecurity.com/2018/01/09/turlas-backdoor-laced-flash-player-installer/) (SORM), which we assess may be integral in facilitating the actor’s current AiTM activity, judging from the large-scale nature of these operations.

This blog provides guidance on how organizations can protect against Secret Blizzard’s AiTM ApolloShadow campaign, including forcing or routing all traffic through an encrypted tunnel to a trusted network or using an alternative provider—such as a satellite-based connection—hosted within a country that does not control or influence the provider’s infrastructure. The blog also provides additional information on network defense, such as recommendations, indicators of compromise (IOCs), and detection details.

Secret Blizzard is [attributed](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-129a) by the United States Cybersecurity and Infrastructure Agency (CISA) as Russian Federal Security Service (Center 16). Secret Blizzard further overlaps with threat actors [tracked by other security vendors](https://learn.microsoft.com/en-us/unified-secops-platform/microsoft-threat-actor-naming) by names such as VENOMOUS BEAR, Uroburos, Snake, Blue Python, Turla, Wraith, ATG26, and Waterbug.

As part of our continuous monitoring, analysis, and reporting of the threat landscape, we are sharing our observations on Secret Blizzard’s latest activity to raise awareness of this actor’s tradecraft and educate organizations on how to harden their attack surface against this and similar activity. Although this activity poses a high risk to entities within Russia, the defense measures included in this blog are broadly applicable and can help organizations in any region reduce their risk from similar threats. Microsoft is also tracking other groups using similar techniques, including those documented by ESET in a previous [publication](https://www.eset.com/us/about/newsroom/press-releases/eset-research-discovers-moustachedbouncer/).

## AiTM and ApolloShadow deployment

In February 2025, Microsoft Threat Intelligence observed Secret Blizzard conducting a cyberespionage campaign against foreign embassies located in Moscow, Russia, using an AiTM position to deploy the ApolloShadow malware to maintain persistence and collect intelligence from diplomatic entities. An [adversary-in-the-middle](https://attack.mitre.org/techniques/T1557/) technique is when an adversary positions themself between two or more networks to support follow-on activity. The Secret Blizzard AiTM position is likely facilitated by lawful intercept and notably includes the installation of root certificates under the guise of Kaspersky Anti-Virus (AV). We assess this allows for TLS/SSL stripping from the Secret Blizzard AiTM position, rendering the majority of the target’s browsing in clear text including the delivery of certain tokens and credentials. Secret Blizzard has exhibited similar techniques in past cyberespionage [campaigns](https://web-assets.esetstatic.com/wls/2018/01/ESET_Turla_Mosquito.pdf) to infect foreign ministries in Eastern Europe by tricking users to download a trojanized Flash installer from an AiTM position.

### Initial access

In this most recent campaign, the initial access mechanism used by Secret Blizzard is facilitated by an AiTM position at the ISP/Telco level inside Russia, in which the actor redirects target devices by putting them behind a captive portal. Captive portals are legitimate web pages designed to manage network access, such as those encountered when connecting to the internet at a hotel or airport. Once behind a captive portal, the [Windows Test Connectivity Status Indicator](https://learn.microsoft.com/troubleshoot/windows-client/networking/internet-explorer-edge-open-connect-corporate-public-network) is initiated—a legitimate service that determines whether a device has internet access by sending an HTTP GET request to _hxxp://www.msftconnecttest\[.\]_ _com/redirect_ which should direct to _msn\[.\]com_.

### Delivery and installation

Once the system opens the browser window to this address, the system is redirected to a separate actor-controlled domain that likely displays a certificate validation error which prompts the target to download and execute ApolloShadow. Following execution, ApolloShadow checks for the privilege level of the _ProcessToken_ and if the device is not running on default administrative settings, then the malware displays the user access control (UAC) pop-up window to prompt the user to install certificates with the file name _CertificateDB.exe_, which masquerades as a Kaspersky installer to install root certificates and allow the actor to gain elevated privileges in the system.

![The infect chain displays the back and forth between the unknowing target and Secret Blizzard, with the target first getting an unexpected response to a connection, leading the attacker to redirecting the target to their domain. The target downloads and executes the malware, which ultimately beacons the attacker's server at their attacker-controlled IP address to deliver a secondary payload. ](https://www.microsoft.com/en-us/security/blog/2025/07/31/frozen-in-transit-secret-blizzards-aitm-campaign-against-diplomats/)_Figure 1. Secret Blizzard AiTM infection chain_

### ApolloShadow malware

ApolloShadow uses two execution paths depending on the privilege level of the running process. The token of the running process is retrieved using the API _GetTokenInformationType_ and the value of _TokenInformation_ is checked to see if the token contains the _TokenElevationTypeFull_ type **.** If it does not have that privilege level, ApolloShadow executes a low privilege execution path **.**

![Diagram of the ApolloShadow execution flow starting with CertificateDB.exe checking token access, using a GET request to receive and execute the VB Script. At the same time, it installs the certificate to elevate privileges, ultimately installing root certificates. changing the connected networks to private, and adding an admin user.](https://www.microsoft.com/en-us/security/blog/2025/07/31/frozen-in-transit-secret-blizzards-aitm-campaign-against-diplomats/)_Figure 2. ApolloShadow execution flow_

## Low privilege execution

When executing the low privilege path, the first action is to collect information about the host to send back to the AiTM controlled command and control (C2). First, the host’s IP information is collected using the API _GetIpAddrTable_, which collects information from the _IpAddrTable_. Each entry is individually Base64-encoded and delineated by a pipe character with _\\r\\n_ appended, then combined into one string. For example:

- 172.29.162\[.\]128 00-15-5D-04-04-1C
- 127.0.0\[.\]1

` "|MTcyLjI5LjE2Mi4xMjggMDAtMTUtNUQtMDQtMDQtMUM=|\r\n|MTI3LjAuMC4xIA==|\r\n"`

Then the entire string is Base64-encoded once again in preparation for exfiltration to the C2 host:

`"fE1UY3lMakk1TGpFMk1pNHhNamdnTURBdE1UVXROVVF0TURRdE1EUXRNVU09fA0KfE1USTNMakF1TUM0eElBPT18DQo="`

The encoded network information is added as a query string to a GET request with the destination URL _hxxp_ _://timestamp.digicert\[.\]com/registered_. Two query parameters are included with the request, _code_ and _t_.  The _Code_ parameters contains a hardcoded set of characters and the _t_ variable has the encoded IP address information, as shown below:

`code=DQBBBBBBBBBOBBBBBBBBBBgBBBBBBBBBny_t???????t=fE1UY3lMakk1TGpFMk1pNHhNamdnTURBdE1UVXROVVF0TURRdE1EUXRNVU09fA0KfE1USTNMakF1TUM0eElBPT18DQo=`

While the timestamp subdomain does exist for Digicert, the / _registered_ resource does not. Due to the AiTM position of the actor, Secret Blizzard can use DNS manipulation to redirect legitimate-looking communication to the actor-controlled C2 and return an encoded VBScript as the second-stage payload.

When the response comes back from the redirected Digicert request, the file name that is used to write the script to disk is decoded for use. ApolloShadow uses string obfuscation in several places throughout the binary to hide critical strings. These strings are blocks of encoded characters that are encoded using XOR with a separate set of hardcoded constants. While this is not a particularly sophisticated technique, it is enough to obscure the strings from view at first glance. The strings are decoded as they are used and then re-encoded after use to remove traces of the strings from memory.

![Screenshot of code depicting the string decoding operation for the VB script name](https://www.microsoft.com/en-us/security/blog/2025/07/31/frozen-in-transit-secret-blizzards-aitm-campaign-against-diplomats/)_Figure 2. String decoding operation for VB script name_

The decoded file name is _edgB4ACD.vbs_ and the file name string is concatenated by the malware with the results of querying the environment variable for the _TEMP_ directory to create the path for the target script. We were unable to recover the script, but the header of the response is checked for the first 12 characters to see if it matches the string _MDERPWSAB64B_. Once ApolloShadow has properly decoded the script, it executes the script using the Windows API call _CreateProcessW_ with the command line to launch _wscript_ and the path to _edgB4ACD.vbs_.

Finally, the ApolloShadow process launches itself again using _ShellExecuteA,_ which presents the user with an UAC window to bypass UAC mechanisms and prompt the user to grant the malware the highest privileges available to the user.

![Screenshot of the UAC popup which asks the user if they want to allow this app from an unknown publisher to make changes to their device. The file is called CertificateDB.exe and the user can click Yes or No.](https://www.microsoft.com/en-us/security/blog/2025/07/31/frozen-in-transit-secret-blizzards-aitm-campaign-against-diplomats/)_Figure 3. UAC popup to request elevated privileges from the user_

## Elevated privilege execution

When the process is executed with sufficient elevated privileges, ApolloShadow alters the host by setting all networks to _Private_. This induces several changes including allowing the host device to become discoverable, and relaxing firewall rules to enable file sharing. While we did not see any direct attempts for lateral movement, the main reason for these modifications is likely to reduce the difficulty of lateral movement on the network. ApolloShadow uses two different methods to perform this change.

The first method is through the registry settings for _NetworkProfiles: SOFTWARE\\\Microsoft\\\Windows NT\\\CurrentVersion\\\NetworkList\\\Profiles_. The network’s globally unique identifiers (GUIDs) are parsed for each connected network, and the malware modifies the value _Category_ by setting it to 0. This change sets the profile of the network to _Private_ after the host has been rebooted.

![Screenshot of the registry settings for network profiles](https://www.microsoft.com/en-us/security/blog/2025/07/31/frozen-in-transit-secret-blizzards-aitm-campaign-against-diplomats/)_Figure 4. Registry settings for network profiles_

The second method directly sets firewall rules using Component Object Model (COM) objects that enable file sharing and turn on network discovery. Several strings are decoded using the same method as above and concatenated to create the firewall rules they want to modify.

- `FirewallAPI.dll,-32752`
  - This command enables the **Network Discovery** rule group
- `FirewallAPI.dll,-28502`
  - This command enables all rules in the **File and Printer Sharing** group

The strings are passed to the COM objects to enable the rules if they are not already enabled.

![Screenshot of code depicting COM objects that were used to modify firewall rules](https://www.microsoft.com/en-us/security/blog/2025/07/31/frozen-in-transit-secret-blizzards-aitm-campaign-against-diplomats/)_Figure 5. COM objects used to modify firewall rules_

Both techniques have some crossover, but the following table provides a comparison overview of each method.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Technique** | **Purpose** | **Timing** | **Stealth** | **Effect** |
| Registry profile change | Sets network to _Private_ | Requires reboot | High | Broadly relaxes firewall posture |
| COM-based rule enablement | Activates specific rules | Immediate | Moderate | Opens precise ports for discovery and sharing |

From here, ApolloShadow presents the user with a window showing that the certificates are being installed.

![A screenshot of the window displayed to the user which shows a loading bar called K Certificate Installation](https://www.microsoft.com/en-us/security/blog/2025/07/31/frozen-in-transit-secret-blizzards-aitm-campaign-against-diplomats/)_Figure 6. Window displayed to the user during execution_

A new thread performs the remainder of the functionality. The two root certificates being installed are written to the _%TEMP%_ directory with a temporary name and the extension _crt_. The certificate installation is performed by using the Windows certutil utility and the temporary files are deleted following the execution of the commands.

- `certutil.exe -f -Enterprise -addstore root "C:\Users\<username>\AppData\Local\Temp\crt3C5C.tmp"`
- ` certutil.exe -f -Enterprise -addstore ca "C:\Users\<username>\AppData\Local\Temp\crt53FF.tmp"`

The malware must add a preference file to the Firefox preference directory because Firefox uses different certificate stores than browsers such as Chromium, which results in Firefox not trusting the root and enterprise store by default. ApolloShadow reads the registry key that points to the installation of the application and builds a path to the preference directory from there. A file is written to disk called _wincert.js_ containing a preference modification for Firefox browsers, allowing Firefox to trust the root certificates added to the operating system’s certificate store.

- `pref("security.enterprise_roots.enabled", true);" privilege`

The final step is to create an administrative user with the username _UpdatusUser_ and a hardcoded password on the infected system using the Windows API _NetUserAdd_. The password is also set to never expire.

![Screenshot of an admin user being added to an infected system with the username UpdatusUser](https://www.microsoft.com/en-us/security/blog/2025/07/31/frozen-in-transit-secret-blizzards-aitm-campaign-against-diplomats/)_Figure 7. Administrator user added to infected system_

ApolloShadow has successfully installed itself on the infected host and has persistent access using the new local administrator user.

## Defending against Secret Blizzard activity

Microsoft recommends that all customers, but especially sensitive organizations operating in Moscow, should implement the following recommendations to mitigate against Secret Blizzard activity.

- Route all traffic through an encrypted tunnel to a trusted network or use a virtual private network (VPN) service provider, such as a satellite-based provider, whose infrastructure is not controlled or influenced by outside parties.

Microsoft also recommends the following guidance to enhance protection and mitigate potential threats:

- Practice the [principle of least privilege](https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/implementing-least-privilege-administrative-models), use multifactor authentication (MFA), and audit privileged account activity in your environments to slow and stop attackers. Avoid the use of domain-wide, admin-level service accounts and restrict local administrative privileges. These mitigation steps reduce the paths that attackers have available to them to accomplish their goals and lower the risk of the compromise spreading in your environment.
- Regularly review highly privileged groups like Administrators, Remote Desktop Users, and Enterprise Admins. Threat actors may add accounts to these groups to maintain persistence and disguise their activity.
- Turn on [cloud-delivered protection](https://learn.microsoft.com/defender-endpoint/configure-block-at-first-sight-microsoft-defender-antivirus) in Microsoft Defender Antivirus or the equivalent for your antivirus product to cover rapidly evolving attacker tools and techniques.
- Run [endpoint detection and response (EDR) in block mode](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/edr-in-block-mode?ocid=magicti%3Cem%3Eta%3C/em%3Elearndoc), so that Defender for Endpoint can block malicious artifacts, even when your non-Microsoft antivirus doesn’t detect the threat or when Microsoft Defender Antivirus is running in passive mode. EDR in block mode works behind the scenes to remediate malicious artifacts detected post-breach.
- Turn on [attack surface reduction rules](https://learn.microsoft.com/defender-endpoint/attack-surface-reduction-rules-reference?ocid=magicti_ta_learndoc) to prevent common attack techniques. These rules, which can be configured by all Microsoft Defender Antivirus customers and not just those using the EDR solution, offer significant hardening against common attack vectors.
- [Block executable files from running unless they meet a prevalence, age, or trusted list criterion](https://learn.microsoft.com/defender-endpoint/attack-surface-reduction-rules-reference#block-executable-files-from-running-unless-they-meet-a-prevalence-age-or-trusted-list-criterion)
- [Block execution of potentially obfuscated scripts](https://learn.microsoft.com/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)

## Microsoft Defender XDR detections

Microsoft Defender XDR customers can refer to the list of applicable detections below. Microsoft Defender XDR coordinates detection, prevention, investigation, and response across endpoints, identities, email, apps to provide integrated protection against attacks like the threat discussed in this blog.

Customers with provisioned access can also use [Microsoft Security Copilot in Microsoft Defender](https://learn.microsoft.com/defender-xdr/security-copilot-in-microsoft-365-defender) to investigate and respond to incidents, hunt for threats, and protect their organization with relevant threat intelligence.

### Microsoft Defender Antivirus

Microsoft Defender Antivirus detects this threat as the following malware:

- [Trojan:Win64/ApolloShadow](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Trojan:Win64/ApolloShadow!dha)

### Microsoft Defender for Endpoint

The following alerts might indicate threat activity related to this threat. Note, however, that these alerts can be also triggered by unrelated threat activity.

- Secret Blizzard Actor activity detected
- Suspicious root certificate installation
- Suspicious certutil activity
- User account created under suspicious circumstances
- A script with suspicious content was observed

## Microsoft Security Copilot

Security Copilot customers can use the standalone experience to [create their own prompts](https://learn.microsoft.com/copilot/security/prompting-security-copilot#create-your-own-prompts) or run the following [pre-built promptbooks](https://learn.microsoft.com/copilot/security/using-promptbooks) to automate incident response or investigation tasks related to this threat:

- Incident investigation
- Microsoft User analysis
- Threat actor profile
- Threat Intelligence 360 report based on MDTI article
- Vulnerability impact assessment

Note that some promptbooks require access to plugins for Microsoft products such as Microsoft Defender XDR or Microsoft Sentinel.

## Threat intelligence reports

Microsoft customers can use the following reports in Microsoft products to get the most up-to-date information about the threat actor, malicious activity, and techniques discussed in this blog. These reports provide the intelligence, protection information, and recommended actions to prevent, mitigate, or respond to associated threats found in customer environments.

### Microsoft Defender Threat Intelligence

- [Actor profile: Secret Blizzard](https://security.microsoft.com/intel-profiles/01d15f655c45c517f52235d63932fb377c319176239426681412afb01bf39dcc)

Microsoft Security Copilot customers can also use the [Microsoft Security Copilot integration](https://learn.microsoft.com/defender/threat-intelligence/security-copilot-and-defender-threat-intelligence?bc=%2Fsecurity-copilot%2Fbreadcrumb%2Ftoc.json&toc=%2Fsecurity-copilot%2Ftoc.json#turn-on-the-security-copilot-integration-in-defender-ti) in Microsoft Defender Threat Intelligence, either in the Security Copilot standalone portal or in the [embedded experience](https://learn.microsoft.com/defender/threat-intelligence/using-copilot-threat-intelligence-defender-xdr) in the Microsoft Defender portal to get more information about this threat actor.

## Hunting queries

### Microsoft Defender XDR

Microsoft Defender XDR customers can run the following query to find related activity in their networks:

Surface devices that attempt to download a file within two minutes after captive portal redirection. This activity may indicate a first stage AiTM attack—such as the one utilized by Secret Blizzard—against a device.

```
let CaptiveRedirectEvents = DeviceNetworkEvents
| where RemoteUrl contains "msftconnecttest.com/redirect"
| project DeviceId, RedirectTimestamp = Timestamp, RemoteUrl;
let FileDownloadEvents = DeviceFileEvents
| where ActionType == "FileDownloaded"
| project DeviceId, DownloadTimestamp = Timestamp, FileName, FolderPath; CaptiveRedirectEvents
| join kind=inner (FileDownloadEvents) on DeviceId
| where DownloadTimestamp between (RedirectTimestamp .. (RedirectTimestamp + 2m))
| project DeviceId, RedirectTimestamp, RemoteUrl, DownloadTimestamp, FileName, FolderPath

```

### Microsoft Sentinel

Microsoft Sentinel customers can use the TI Mapping analytics (a series of analytics all prefixed with ‘TI map’) to automatically match the malicious domain indicators mentioned in this blog post with data in their workspace. If the TI Map analytics are not currently deployed, customers can install the Threat Intelligence solution from the [Microsoft Sentinel Content Hub](https://learn.microsoft.com/azure/sentinel/sentinel-solutions-deploy) to have the analytics rule deployed in their Sentinel workspace.

Below are the queries using Sentinel Advanced Security Information Model (ASIM) functions to hunt threats across both Microsoft first party and third-party data sources. ASIM also supports deploying parsers to specific workspaces from GitHub, using an ARM template or manually.

**Detect network IP and domain indicators of compromise using ASIM**

The below query checks IP addresses and domain indicators of compromise (IOCs) across data sources supported by ASIM Network session parser.

```
//IP list and domain list- _Im_NetworkSession
let lookback = 30d;
let ioc_ip_addr = dynamic(["45.61.149.109"]);
let ioc_domains = dynamic(["kav-certificates.info"]);
_Im_NetworkSession(starttime=todatetime(ago(lookback)), endtime=now())
| where DstIpAddr in (ioc_ip_addr) or DstDomain has_any (ioc_domains)
| summarize imNWS_mintime=min(TimeGenerated), imNWS_maxtime=max(TimeGenerated),
  EventCount=count() by SrcIpAddr, DstIpAddr, DstDomain, Dvc, EventProduct, EventVendor

```

**Detect network and files hashes indicators of compromise using ASIM**

The below queries will check IP addresses and file hash IOCs across data sources supported by ASIM Web session parser.

Detect network indicators of compromise and domains using ASIM

```
//IP list - _Im_WebSession
let lookback = 30d;
let ioc_ip_addr = dynamic(["45.61.149.109"]);
let ioc_sha_hashes =dynamic(["13fafb1ae2d5de024e68f2e2fc820bc79ef0690c40dbfd70246bcc394c52ea20"]);
_Im_WebSession(starttime=todatetime(ago(lookback)), endtime=now())
| where DstIpAddr in (ioc_ip_addr) or FileSHA256 in (ioc_sha_hashes)
| summarize imWS_mintime=min(TimeGenerated), imWS_maxtime=max(TimeGenerated),
  EventCount=count() by SrcIpAddr, DstIpAddr, Url, Dvc, EventProduct, EventVendor

```

```
// Domain list - _Im_WebSession
let ioc_domains = dynamic(["kav-certificates.info"]);
_Im_WebSession (url_has_any = ioc_domains)

```

**Detect files hashes indicators of compromise using ASIM**

The below query will check IP addresses and file hash IOCs across data sources supported by ASIM FileEvent parser.

Detect network and files hashes indicators of compromise using ASIM

```
// file hash list - imFileEvent
let ioc_sha_hashes =dynamic(["13fafb1ae2d5de024e68f2e2fc820bc79ef0690c40dbfd70246bcc394c52ea20"]);
imFileEvent
| where SrcFileSHA256 in (ioc_sha_hashes) or
TargetFileSHA256 in (ioc_sha_hashes)
| extend AccountName = tostring(split(User, @'')[1]),
  AccountNTDomain = tostring(split(User, @'')[0])
| extend AlgorithmType = "SHA256"

```

### Indicators of compromise

|     |     |     |
| --- | --- | --- |
| **Indicator** | **Type** | **Description** |
| _kav-certificates\[.\]info_ | Domain | Actor-controlled domain that downloads the malware |
| 45.61.149\[.\]109 | IP address | Actor-controlled IP address |
| 13fafb1ae2d5de024e68f2e2fc820bc79ef0690c40dbfd70246bcc394c52ea20 | SHA256 | ApolloShadow malware |
| _CertificateDB.exe_ | File name | File name associated with ApolloShadow sample |

## References

- [https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-129a](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-129a)
- [https://www.welivesecurity.com/2018/01/09/turlas-backdoor-laced-flash-player-installer/](https://www.welivesecurity.com/2018/01/09/turlas-backdoor-laced-flash-player-installer/)
- [https://attack.mitre.org/techniques/T1557/](https://attack.mitre.org/techniques/T1557/)
- [https://web-assets.esetstatic.com/wls/2018/01/ESET\_Turla\_Mosquito.pdf](https://web-assets.esetstatic.com/wls/2018/01/ESET_Turla_Mosquito.pdf)

## Acknowledgments

- [https://securelist.com/compfun-successor-reductor/93633/](https://securelist.com/compfun-successor-reductor/93633/)

## Learn more

Meet the experts behind Microsoft Threat Intelligence, Incident Response, and the Microsoft Security Response Center at our [VIP Mixer at Black Hat 2025](https://microsoftsecurityevents.eventbuilder.com/events/11f048838dabd650892acff3dd777035?ref=blog). Discover how our end-to-end platform can help you strengthen resilience and elevate your security posture.

For the latest security research from the Microsoft Threat Intelligence community, check out the [Microsoft Threat Intelligence Blog](https://aka.ms/threatintelblog).

To get notified about new publications and to join discussions on social media, follow us on [LinkedIn](https://www.linkedin.com/showcase/microsoft-threat-intelligence), [X (formerly Twitter)](https://x.com/MsftSecIntel), and [Bluesky](https://bsky.app/profile/threatintel.microsoft.com).

To hear stories and insights from the Microsoft Threat Intelligence community about the ever-evolving threat landscape, listen to the [Microsoft Threat Intelligence podcast](https://thecyberwire.com/podcasts/microsoft-threat-intelligence).

![](https://www.microsoft.com/en-us/security/blog/wp-content/themes/blog-in-a-box/dist/images/default-avatar.png)

- [Follow on X](https://x.com/MsftSecIntel)
- [Follow on LinkedIn](https://www.linkedin.com/showcase/microsoft-threat-intelligence/)

## Microsoft Threat Intelligence

[See Microsoft Threat Intelligence posts](https://www.microsoft.com/en-us/security/blog/author/microsoft-security-threat-intelligence/)

## Related posts

- ![A woman pointing at a computer.](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2025/07/Security_TBD_Blog_250725-809x455.webp)









- July 31
- 5 min read

### [Modernize your identity defense with Microsoft Identity Threat Detection and Response](https://www.microsoft.com/en-us/security/blog/2025/07/31/modernize-your-identity-defense-with-microsoft-identity-threat-detection-and-response/)

Microsoft’s Identity Threat Detection and Response solution integrates identity and security operations to provide proactive, real-time protection against sophisticated identity-based cyberthreats.

- ![A woman sitting on a couch using a laptop](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2025/07/Screenshot-2025-07-21-131220-809x455.webp)









- July 28
- 9 min read

### [Sploitlight: Analyzing a Spotlight-based macOS TCC vulnerability](https://www.microsoft.com/en-us/security/blog/2025/07/28/sploitlight-analyzing-a-spotlight-based-macos-tcc-vulnerability/)

Microsoft Threat Intelligence has discovered a macOS vulnerability, tracked as CVE-2025-31199, that could allow attackers to steal private data of files normally protected by Transparency, Consent, and Control (TCC), including the ability to extract and leak sensitive information cached by Apple Intelligence.

- ![A blue background with a logo](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2025/07/Security-Blog-hero-1260x708_Revised0714-809x455.webp)









- July 22
- 6 min read

### [Microsoft Sentinel data lake: Unify signals, cut costs, and power agentic AI](https://www.microsoft.com/en-us/security/blog/2025/07/22/microsoft-sentinel-data-lake-unify-signals-cut-costs-and-power-agentic-ai/)

We’re evolving our industry-leading Security Incidents and Event Management solution (SIEM), Microsoft Sentinel, to include a modern, cost-effective data lake.

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
