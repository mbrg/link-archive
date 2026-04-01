---
date: '2025-09-23'
description: Microsoft's security findings highlight critical vulnerabilities in Active
  Directory setups. Estimated attacks often stem from initial compromise of non-privileged
  users, leading to full control via misconfigurations and accessible tools like BloodHound.
  Key recommendations include implementing passwordless authentication, reducing excessive
  privileges, and tightening security on sensitive accounts. Effective tools like
  Defender for Identity can aid in monitoring privileged credential exposure and misconfigured
  access control lists (ACLs), promoting a proactive security posture. Continuous
  review and adjustment of identity controls are essential to mitigate risks posed
  by evolving threat landscapes.
link: https://techcommunity.microsoft.com/blog/microsoftsecurityexperts/total-identity-compromise-microsoft-incident-response-lessons-on-securing-active/3753391
tags:
- Identity Management
- Active Directory
- Incident Response
- Credential Security
- Cybersecurity
title: 'Total Identity Compromise: Microsoft Incident Response lessons on securing
  Active Directory ◆ Microsoft Community Hub'
---

## Blog Post

Microsoft Security Experts Blog

18 MIN READ

# Total Identity Compromise: Microsoft Incident Response lessons on securing Active Directory

[![matthewzorich's avatar](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/dS0xNzA2NjgyLTQ0MDE5MWkyODZFQTIxQ0ZFN0VCQTAz?image-dimensions=50x50)](https://techcommunity.microsoft.com/users/matthewzorich/1706682)

[matthewzorich](https://techcommunity.microsoft.com/users/matthewzorich/1706682)

![Icon for Microsoft rank](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/cmstNC05WEo0blc?image-dimensions=100x16&constrain-image=true)Microsoft

Feb 28, 2023

**Total Identity Compromise: Microsoft Incident Response lessons on securing Active Directory**

When Microsoft Incident Response (formerly DART/CRSP) is engaged during an incident, almost all environments include an on-premises Active Directory component. In most of these engagements, threat actors have taken full control of Active Directory –i.e., total domain compromise.

Total domain compromise often starts with the compromise of a regular non-privileged user rather than a domain admin. Threat actors can use that account to discover misconfiguration and attack paths in Active Directory that lead to full domain control. Oftentimes, threat actors leverage freely available tools such as AdFind, AD Explorer, or BloodHound to find attack paths through Active Directory environments. After total domain compromise, restoring trust back into Active Directory can take significant time and investment.

To aid in our investigations, Microsoft Incident Response leverages a custom-built Active Directory enumeration tool to retrieve metadata about users, groups, permissions, group policies and more. Microsoft Incident Response uses this data to not only aid in the investigation, but also to shape [attacker eviction and compromise recovery plans](https://www.microsoft.com/en-us/security/blog/2021/06/09/crsp-the-emergency-team-fighting-cyber-attacks-beside-customers/) and to provide best practice recommendations on taking back and maintaining positive identity control. In addition to the Microsoft Incident Response custom tool, there are other tools, such as [Defender for Identity](https://learn.microsoft.com/en-us/defender-for-identity/what-is), and open-source tools such as [BloodHound](https://github.com/BloodHoundAD/BloodHound) and [PingCastle](https://www.pingcastle.com/), that you can use to secure Active Directory in your own environment.

Across all industry verticals, Microsoft Incident Response often finds similar issues within Active Directory environments. In this blog, we will be highlighting some of the most common issues seen in on-premises Active Directory environments and provide guidance on how to secure those weaknesses. These include:

Initial Access – Weak password policies, excessive privilege and poor credential hygiene, insecure account configuration

Credential Access – Privileged credential exposure, Kerberoasting, insecure delegation configuration, Local Administrator Password Solution (LAPS) misconfiguration, excessive privilege via built-in groups

Privilege Escalation – Access control list (ACL) abuse, escalation via Exchange permissions, Group Policy abuse, insecure trust configuration, compromise of other Tier 0 assets

**Initial Access**

**Weak Password Policies**

It is not uncommon for Microsoft Incident Response to engage with customers where accounts have weak or easy to guess credentials, including those of privileged users such as Domain Admins. Simple password spray attacks can lead to the compromise of such accounts. If these standard user accounts are provided VPN or remote access without multi-factor authentication, the risk is increased: threat actors can connect to the VPN via devices in their control and begin reconnaissance of the environment remotely. From here, a threat actor can then attempt to escalate to Domain Admin privileges via weaknesses in Active Directory.

**Recommendation**

Where possible, Microsoft Incident Response recommends deploying [passwordless authentication](https://www.microsoft.com/en-us/security/business/solutions/passwordless-authentication) technology, such as Windows Hello for Business (which uses biometrics such as facial recognition or fingerprints) or FIDO2 security keys. Fully deploying passwordless authentication allows you to [disallow password authentication](https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/passwordless-strategy#configure-user-accounts-to-disallow-password-authentication), which eliminates password-based attack vectors (such as password sprays and phishing) for those users. If you are not yet ready to begin deploying passwordless solutions, you can increase the strength of your on-premises password policy through group policy and [fine-grained password policies](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/introduction-to-active-directory-administrative-center-enhancements--level-100-#fine_grained_pswd_policy_mgmt). Current guidance recommends longer (14 or more characters) but less complex passwords (no special characters or similar required), with users having to change them much less frequently. This discourages users from cycling through easy-to-guess passwords to satisfy complexity and rotation requirements, such as changing their password from ‘ _Monday10_’ to ‘ _Monday11’_.

If you are licensed for Azure Active Directory P1 or higher, you can also deploy [Azure Active Directory Password Protection](https://learn.microsoft.com/en-us/azure/active-directory/authentication/concept-password-ban-bad-on-premises), which can disallow your users from using easy to guess passwords [even in on-premises Active Directory](https://learn.microsoft.com/en-us/azure/active-directory/authentication/concept-password-ban-bad-on-premises). You can also ban custom words unique to your business, such as the name of your company or the city in which you operate.

For both passwordless and stronger password policies, if you work in a complex environment where the rollout of those solutions may take some time, start by targeting your Domain Admins and other privileged users. Your Tier 0 accounts can, and should, be held to a higher security standard.

**Excessive Privilege and Poor Credential Hygiene**

One of the most common issues found in Active Directory is accounts, particularly service accounts, being assigned too much privilege. In Microsoft Incident Response engagements, it is not uncommon to find multiple service accounts and named user accounts to be granted Domain Admin privileges. Additionally, service accounts used for applications or scripts are often granted local administrative access over all workstations and servers. Though this is an easy way to allow a product or script to function, these accounts then become a weak point in your security.

Service accounts are attractive targets because the passwords are rarely rotated. Security controls for them are often weaker, and they can’t be protected by MFA. Furthermore, the passwords for these accounts are often stored in clear text, whether that be sent in email, saved to text files on devices, or used in clear text in command line arguments. The combination of many Domain Admin accounts and poor technical controls over those accounts increase the risk for credential theft.

This excessive privilege also extends to too many users having local administrative rights on their own devices. If a compromised user does not have local administrative rights on their device, it is harder for a threat actor to continue to move laterally in the environment from that device.

**Recommendation**

There is no specific guidance on how many Domain Admin accounts should exist in each environment, as the requirements for privileged accounts will be unique for each environment. With that said, any requests to have additional Domain Admins should be scrutinized closely, with the preference always being to grant a lower level of privilege, particularly to service accounts. Even though adding service accounts to Domain Admins is an easy way to ensure an application works, most of these accounts can be assigned much less privilege and still function correctly. They can also often be granted access to only a subset of devices rather than all workstations and servers.

If you don’t have strong controls to govern secure credential practice for your most important accounts, then the more Domain Admin level accounts you add, the more risk you incur. For service accounts, investigate whether [Group Managed Service Accounts](https://learn.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/group-managed-service-accounts-overview) (gMSA), which can provide automatic password management, would be suitable for the workload.

**Insecure Account Configuration**

In Active Directory, misconfiguration can be a reason the security of individual user accounts is weaker than it could be. Some of the settings to scrutinize for proper configuration include:

- Do not require Kerberos pre-authentication.
- Store password using reversible encryption.
- Password not required.
- Password stored with weak encryption.

Enabling any of these settings drastically reduces the security of an account. An adversary can enumerate a directory with relative ease to find any accounts that have these flags. The credentials for these accounts may then be easier for a threat actor to retrieve.

**Recommendation**

Defender for Identity, via the Secure Score portal, provides an excellent summary of these risky account flags. For each configuration item, it lists which accounts are affected and how to remediate the issue. Other tooling such as BloodHound or PingCastle can also flag these account issues.

**Credential Access**

**Privileged Credential Exposure**

During cyber-attacks, adversaries often seek to obtain privileged credentials. These credentials are viewed as ‘crown jewels’ because they allow threat actors to complete their objectives. Once privileged credentials are obtained, they can be used to:

- Add additional persistence mechanisms, such as scheduled tasks, installing services, or creating additional user accounts.
- Disable or bypass endpoint antivirus or other security controls.
- Deploy malware or ransomware.
- Exfiltrate sensitive data.

As administrators log on to devices directly or connect to devices remotely to complete their day-to-day work, they may leave behind privileged credentials. Threat actors can leverage tools such as Mimikatz or secretsdump (part of the Impacket framework) to retrieve those credentials. As privileged users log on to more and more machines, attackers have additional opportunities to locate and extract those credentials. For example, if members of the Domain Admins group regularly log on to end user workstations to troubleshoot issues, then Domain Admin credentials may be exposed on each device, increasing a threat actor’s chances of locating and extracting them.

To help customers understand this privileged credential spread, Microsoft Incident Response collects logon telemetry from the event logs on devices, signals from Microsoft Defender for Endpoint, or both. From that data, a map is created of Tier 0 accounts, such as Domain Admins, logging onto devices that are not considered Tier 0, such as member servers and workstations.

![mzorich_5-1677476139108.png](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNzUzMzkxLTQ0NTYwOWlCRTJGQzIzNEE0MTQ3NTk5?image-dimensions=984x541&revision=5)

_Figure 1: Map of Domain Admin login paths to non-Tier 0 servers._

In this visual, the green circles represent Domain Admins. The red dotted lines represent RDP logons to devices, while the black dotted lines represent network logons. In this example, we can see two domain admins that have logged onto three different servers. Should a threat actor compromise one of these three servers, there is potential for theft of a Domain Admin level credential. The larger the environment, the more this issue becomes apparent. If we add additional admins and other non-Tier 0 devices, we can see the immediate impact on our footprint.

![mzorich_6-1677476230313.png](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNzUzMzkxLTQ0NTYxMGk4NTVCODQ3Mzg0ODZERDJC?image-dimensions=931x737&revision=5)

_Figure 2: Map of Domain Admin login paths to non-Tier 0 servers and other devices._

With additional Domain Admins and those admins logging onto other non-tier 0 devices, credential exposure has increased significantly.

The goal of these diagrams is to help customers visualize where privileged credentials are being left on their network and to start thinking from the mindset of a threat actor. In large and complex Active Directory environments, these diagrams can become immense, and the number of endpoints climbs into the thousands.

**Recommendation**

Microsoft’s solution to reduce privileged credential exposure is to implement the [enterprise access model](http://aka.ms/tier0). This administration model seeks to reduce the spread of privileged credentials by restricting the devices that Domain Admins (and similar accounts) can log on to. In large and complex environments, it is safe to assume that some users and devices will be compromised. Your most privileged accounts should only access Tier 0 assets from hardened devices, known as privileged access workstations (PAWs). Using least-privileged access is a key part of [Zero Trust principals](https://www.microsoft.com/en-us/security/business/zero-trust). By reducing the opportunity to extract privileged credentials, we reduce the impact of compromise on a single device or user.

Deploying the enterprise access model is a journey, and every organization is at a different stage of that journey. Regardless of your current posture, you can always reduce privilege credential spread, both through technical controls and changes to the way staff work. This [table](https://learn.microsoft.com/en-us/windows-server/identity/securing-privileged-access/reference-tools-logon-types) [in the Microsoft Learn documentation](https://learn.microsoft.com/en-us/windows-server/identity/securing-privileged-access/reference-tools-logon-types) lists various logon types and whether credentials are left on the destination device. When administering remote systems, Microsoft Incident Response recommends using methods that do not leave credentials behind wherever possible.

Defender for Identity also maps these lateral movement paths, showing paths where compromise of a regular user can lead to domain compromise. These are [integrated directly within user and computer objects in the Microsoft 365 Defender portal](https://learn.microsoft.com/en-us/defender-for-identity/understand-lateral-movement-paths#where-can-i-find-defender-for-identity-lmps).

![mzorich_1-1677549966901.png](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNzUzMzkxLTQ0NTkzM2lGNjk1MzgyN0E0NzM2QkRC?image-dimensions=826x388&revision=5)

_Figure 3: Defender for Identity page_ _for mapping a user’s lateral movement paths._

The highest risk users and computers are also shown in the [Secure Score](https://learn.microsoft.com/en-us/defender-for-identity/security-assessment-riskiest-lmp) portal, allowing you to remediate objects most at risk.

**Kerberoasting**

Kerberoasting is a technique used by threat actors to crack the passwords of accounts, generally service accounts, that have [service principal names](https://learn.microsoft.com/en-us/windows/win32/ad/service-principal-names) (SPNs) associated with them. If a regular user in Active Directory is compromised, they can request a ticket (which includes the hashed password) via tools such as Rubeus for **any** account with an SPN configured. The threat actor can then extract this hash from memory and attempt to crack the password offline. If they can crack the password, they can then authenticate as and assume the privileges of that service account.

It is also not uncommon for Microsoft Incident Response to detect SPNs registered to privileged admin accounts or service accounts that have been added to privileged groups. Often these SPNs are configured for testing and then never removed, leaving them vulnerable to Kerberoasting.

**Recommendation**

Microsoft Incident Response recommends that you review all accounts configured with SPNs to ensure they are still required. For those that are actively in use, ensure the passwords associated for those accounts are extremely complex and rotated where practical.

Defender for Identity includes logic to detect Kerberoasting activity in your environment. By taking signals from your domain controllers, Defender for Identity can help detect users enumerating your domain looking for Kerberoast-able accounts or attempts to actively exploit those accounts.

**Insecure Delegation Configuration**

Unconstrained Kerberos delegation provides the ability for an entity to impersonate other users. This helps with authentication through multi-tier applications. For example, a web server running IIS may have delegation configured to access an SQL server, which stores the data for the web site. When you log onto the web server, the web server then uses delegation to authenticate on behalf of you to SQL. In doing this, the user’s Kerberos Ticket Granting Ticket (TGT) is stored in memory on the web server. If a threat actor compromises that web server, they could retrieve those tickets and impersonate any users that had logged on. If a Domain Admin happened to log on, then the threat actor would have access to a Domain Admin TGT and could assume full control of Active Directory.

**Recommendation**

Review all the users and devices that are enabled for delegation. These are available in the [Defender for Identity section of Secure Score](https://learn.microsoft.com/en-us/defender-for-identity/security-assessment-unconstrained-kerberos). If delegation is required it should be restricted to only the required services, not fully unconstrained.

Administrative accounts should never be enabled for delegation. You can prevent these privileged accounts from being targeted by enabling the ‘Account is sensitive and cannot be delegated’ flag on them. You can optionally add these accounts to the ‘ [Protected Users’ group](https://learn.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group). This group provides protections over and above just preventing delegation and makes them even more secure; however, it may cause operational issues, so it is worth testing in your environment.

**Local Administrator Password Solution (LAPS)**

Microsoft Incident Response often encounters situations where [LAPS](https://learn.microsoft.com/en-us/windows-server/identity/laps/laps-overview) has not been deployed to an environment. LAPS is the Microsoft solution to automatically manage the password for the built-in Administrator account on Windows devices. When machines are built or imaged, they often have the same password for the built-in Administrator account. If this is never changed, a single password can give local administrative rights to all machines and may provide opportunities for lateral movement. LAPS solves this problem by ensuring each device has a unique local administrator password and rotates it regularly.

Additionally, even in cases where LAPS has been deployed, sometimes it has not been fully operationalized by the business. As a result, despite LAPS managing the local administrator account on these devices, there are still user groups that have local administrative rights over all the workstations or all the servers, or both. These groups can contain numerous users, generally belonging to the service desk or other operations staff. These operational staff then use their own accounts to administer those devices, rather than the LAPS credentials. IT configurations can also exist where a secondary, non-LAPS managed account still exists with an easy to guess password, defeating the benefit gained by deploying LAPS.

As noted earlier, groups with broad administrative access give threat actors additional opportunity to compromise privileged credentials. Should an endpoint where one of these accounts has logged onto become compromised, a threat actor could have credentials to compromise all the devices in the network.

**Recommendation**

It is important to not only deploy LAPS to endpoints, but to ensure that IT standard operating procedures are updated to ensure LAPS is used. This allows companies to remove privilege from administrative accounts and reduce credential theft risk across the business Additionally, it is crucial to understand which users can retrieve the LAPS password for use, since the ability to retrieve this password grants local administrative access to that device. The ability to read the LAPS password is controlled via the ‘ms-Mcs-AdmPwd’ attribute and should be audited to ensure access is only granted to users that require it.

**Excessive Privilege via Built-In Groups**

During incident response, companies often have alerting and monitoring in place for changes to groups like Domain and Enterprise Admins. These groups are widely known to hold the highest level of privilege in Active Directory. However, there are other privileged built-in groups that are attractive to threat actors and are often not held to the same level of scrutiny. Groups such as Account and Server Operators have wide ranging privilege over your Active Directory. For example, by default Server Operators can log on to Domain Controllers, restart services, backup and restore files, and more.

**Recommendation**

It is recommended that, where possible, privileged built-in groups not contain any users. Instead, the appropriate privilege should be granted specifically to users that require it. Additionally, Microsoft Incident Response recommends reviewing the current membership of those [groups](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory#table-b-1-built-in-and-default-accounts-and-groups-in-active-directory) and adding additional alerting to changes to them in the same way you would alert on Domain or Enterprise admin changes.

**Privilege Escalation**

**Access Control List Abuse**

Access Control Lists (ACL) misconfiguration is one of the most common issues Microsoft Incident Response finds in Active Directory environments. Active Directory ACLs are exceptionally granular, complex, and easy to configure incorrectly. It is easy to reduce the security posture of your Active Directory environment without having any operational impact on your users. As ACLs are configured in your environment through business-as-usual activities, attack paths start to form. These attack paths create an escalation path from a low privileged user to total domain control. A threat actor can take advantage of the paths created by the combination of excessive privilege and scope on ACLs. A threat actor can take advantage of the paths created by the combination of excessive privilege and scope on ACLs.

Two common ACLs that Microsoft Incident Response sees regularly in Active Directory are:

- GenericAll – this privilege is the same as Full Control access. If a user was compromised and that user had GenericAll over a highly privileged group, then the threat actor could add additional members to that group.
- WriteDacl – this privilege allows manipulation of the ACL on an object. With this privilege a threat actor can change the ACL on an object such as a group. If a user was compromised and that user had WriteDacl over a highly privileged group, the threat actor could add a new ACL to that group. That new ACL could then give them access to add additional members to the group, such as themselves.

These permissions are often set at the top of the Active Directory hierarchy. They are also often applied to users and groups that do not require those permissions, effectively granting those group members full domain control. The members of these groups are very rarely secured in the same way that Domain and Enterprise Admins are.

In addition, Microsoft Incident Response often detects insecure ACLs on the [AdminSdHolder](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/appendix-c--protected-accounts-and-groups-in-active-directory#adminsdholder) object, which is responsible for managing permissions on protected users and groups. If an adversary can manipulate the ACL on AdminSdHolder, it will be propagated on to those protected users and groups when the SDProp process runs. The adversary will then have rights to change membership of protected groups such as Domain Admins, allowing them to add themselves. The documentation for [BloodHound](https://bloodhound.readthedocs.io/en/latest/data-analysis/edges.html) describes these and several other ACL ‘edges’ that can be abused for privilege escalation.

**Recommendation**

Microsoft Incident Response recommends auditing permissions through your Active Directory environment using tools such as Defender for Identity and running sanctioned audits of attack paths using BloodHound and remediating paths that can lead to domain compromise.

**Escalation via Exchange Permissions**

Prior to the use of corporate cloud email services such as Office 365, customers ran their own on-premises Exchange environments. Many customers still maintain a complete on-premises Exchange environment. On-premises Exchange and Active Directory have always been tied closely together, with Exchange maintaining high privilege through Active Directory. Even in environments that have migrated user mailboxes to Office 365, an on-premises Exchange footprint often remains. It may exist to manage users not yet migrated, for legacy applications that are not able to integrate with Office 365, or to service non-internet connected workloads.

These on-premises Exchange environments often retain high privilege through Active Directory, and groups such as ‘Exchange Trusted Subsystem’ and ‘Exchange Servers’ can have a direct path to total domain control.

On-premises Exchange is also often internet-facing to allow users to access resources such as Outlook Web Access. Like any internet facing service, this increases the surface area for attack. If a threat actor can obtain SYSTEM privilege on an Exchange server and Exchange still retains excessive permissions in Active Directory, then it can lead to complete domain compromise.

**Recommendation**

It is possible to decouple the privilege held by Exchange in Active Directory by deploying the [split permissions model for Exchange](https://learn.microsoft.com/en-us/exchange/permissions/split-permissions/configure-exchange-for-split-permissions?view=exchserver-2019). By deploying this model, permissions for Active Directory and Exchange are separated.

After deploying the Exchange split permissions model, there are [operational changes](https://learn.microsoft.com/en-us/exchange/permissions/split-permissions/split-permissions?view=exchserver-2019) required by staff who administer both Exchange and Active Directory. If you don’t want to deploy the entire split permissions model, you can still reduce the permissions Exchange has in Active Directory by implementing the changes in the following Microsoft [guidance](https://support.microsoft.com/en-us/topic/reducing-permissions-required-to-run-exchange-server-when-you-use-the-shared-permissions-model-e1972d47-d714-fd76-1fd5-7cdcb85408ed).

If you have completely migrated to Office 365 but maintain on-premises Exchange servers for ease of management, you may now be able to [turn off those on-premises servers](https://learn.microsoft.com/en-us/exchange/manage-hybrid-exchange-recipients-with-management-tools).

**Group Policy ACL Abuse**

Group Policy is often a tool used by threat actors to establish persistence (via the creation of scheduled tasks), create additional accounts, or deploy malware. It is also used as a ransomware deployment mechanism. If a threat actor has not yet compromised a Domain Admin, they may have been able to compromise an account that maintains permissions over Group Policy Objects. For instance, the ability to create, update, or even link policies may have been delegated to other groups.

If an existing Group Policy is configured to run a startup script, a threat actor can change the path of that script to then have it execute a malicious payload. If a group policy exists to disable endpoint security tooling as an exemption, a threat actor could leverage the permissions to link policy by applying that policy to all devices in the environment. This would not require the threat actor to update the policy, just change the scope of it.  Additionally, regular users can be given additional privileges via [User Rights Assignments](https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/user-rights-assignment). These privileges are often not required by the users and are granted accidentally.

**Recommendation**

The ability to manipulate Group Policy is a highly privileged action and users and groups with delegated responsibility to manage it should be held to the same standards as Domain Admins or similar. Ensure that permissions to create, update, and link group policies are in line with least privilege principles.

In large and complex environments, the number of Group Policies in use can be overwhelming and it is not clear what policies apply to which users and devices. Using tools such as [Resultant Set of Policy](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn789183(v=ws.11)) (RSoP), you can model your Group Policy objects to see the overall effect on your users and devices.

**Insecure Trust Configuration**

SID history is a capability in Active Directory to aid in domain migration. It allows Domain Admins to simplify migration by applying the SID history (in simple terms, a list of permissions) from the old account to the new account. This helps the user retain access to resources once they are migrated. An adversary can target this capability by inserting the SIDs of groups such as Domain Admins into the SID history of an account in the trusted forest and using that account to [take control of the trusting forest](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc755321(v=ws.10)?redirectedfrom=MSDN#how-sid-history-can-be-used-to-elevate-privileges). This can be especially relevant during [mergers and acquisitions](https://www.microsoft.com/en-us/security/blog/2022/11/02/microsoft-security-tips-for-mitigating-risk-in-mergers-and-acquisitions/), where trusts between Active Directory environments are configured to allow migrations.

**Recommendation**

Active Directory trusts should only be configured when absolutely required. If they are part of an acquisition or migration, then they should be decommissioned once migration is complete. For trusts that need to remain for operational reasons, [SID filtering](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc755321(v=ws.10)?redirectedfrom=MSDN#sid-filtering) and [Selective Authentication](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc755321(v=ws.10)?redirectedfrom=MSDN#selective-authentication) should be configured to reduce the attack path from other domains and forests.

**Compromise of other Tier 0 assets**

Historically, domain controllers have been at the center of Tier 0 infrastructure. While that is still true, Tier 0 has now expanded to include several interconnected systems. As ways of working have evolved, so has the underlying technology required to drive modern identity systems. In line with that, your Tier 0 footprint has also evolved and may now include systems such as:

- Active Directory Federation Services
- Azure Active Directory Connect
- Active Directory Certificate Services

It also includes any other services or infrastructure, including 3rd party providers, that form part of your identity trust chain, such as privileged access management and identity governance systems.

![mzorich_12-1677477076646.png](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNzUzMzkxLTQ0NTYxNmlDNEI4MDVDODREMTk5QjY0?image-dimensions=896x558&revision=5)

_Figure 4: Example of how Tier 0 assets connect to an identity trust chain._

It is important that all systems that form part of your end-to-end identity chain are included in Tier 0, and the security controls you apply to domain controllers also apply to these systems. Due to the interconnected nature of these systems, compromise of any one of them could lead to complete domain compromise. Only Tier 0 accounts should retain local administrative privileges over these systems and, where practical, access to them should be via a privileged access workstation.

**Summary**

In large and complex environments, Microsoft Incident Response often sees combinations of the above issues that reduce identity security posture significantly. These misconfigurations allow threat actors to elevate from a single non privileged user all the way to your crown jewel Domain Admin accounts.

![mzorich_0-1677549706251.png](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNzUzMzkxLTQ0NTkzMmlDOERGQzEyQ0JGQjEyRkY3?image-dimensions=929x237&revision=5)

_Figure 5: Kill chain showing how domain compromise can start from a single compromised user._

For example, in the above kill chain, the first user was compromised due to a weak password policy. Through the initial poor password policy, additional bad credential hygiene, and ACL misconfiguration, the domain was compromised. When you multiply all the combinations of user accounts, group access, and permissions in Active Directory, many paths can exist to Domain Admin.

Attacks on Active Directory are ever evolving, and this blog covers only some of the more common issues Microsoft Incident Response observes in customer environments. Ultimately, any changes made to Active Directory can either increase or decrease the risk that a threat actor can take control of your environment. To ensure that risk is consistently decreasing, Microsoft Incident Response recommends a constant cycle of the below:

- Reduce Privilege – assign all access according to the principle of least privilege. Additionally, deploy the enterprise access model to reduce privileged credential exposure. Combined, these will reduce the likelihood that a single device or user compromise leads to total domain compromise.
- Audit Current Posture – use tools such as Defender for Identity and sanctioned use of BloodHound and PingCastle to audit your current Active Directory security posture and remediate the issues both surfaced through those tools and described in this blog.
- Monitor Changes – monitor for changes to your Active Directory environment that can reduce your security posture or expose additional attack paths to domain compromise.

- Actively Detect – alert on potential signs of compromise using Defender for Identity or custom detection rules.


A message that Microsoft Incident Response often leaves customers with is that securing Active Directory requires continued governance. You can’t ‘deploy’ Active Directory security and never have to look at it again. Active Directory security is about constant improvement and ensuring those misconfigurations and attack paths are mitigated before an adversary finds them.

Updated May 22, 2023

Version 4.0

[microsoft detection and response team (dart)](https://techcommunity.microsoft.com/tag/microsoft%20detection%20and%20response%20team%20(dart)?nodeId=board%3AMicrosoftSecurityExperts)

LikeLike

18

CommentComment

[![matthewzorich's avatar](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/dS0xNzA2NjgyLTQ0MDE5MWkyODZFQTIxQ0ZFN0VCQTAz?image-dimensions=80x80)](https://techcommunity.microsoft.com/users/matthewzorich/1706682)

[matthewzorich](https://techcommunity.microsoft.com/users/matthewzorich/1706682)

![Icon for Microsoft rank](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/cmstNC05WEo0blc?image-dimensions=100x16&constrain-image=true)Microsoft

Joined January 27, 2023

Send Message

[View Profile](https://techcommunity.microsoft.com/users/matthewzorich/1706682)

[Go to Microsoft Security Experts Blog board](https://techcommunity.microsoft.com/category/microsoft-security-product/blog/microsoftsecurityexperts)

[Microsoft Security Experts Blog](https://techcommunity.microsoft.com/category/microsoft-security-product/blog/microsoftsecurityexperts)

Follow this blog board to get notified when there's new activity

 "}},"componentScriptGroups({\\"componentId\\":\\"custom.widget.MicrosoftFooter\\"})":{"\_\_typename":"ComponentScriptGroups","scriptGroups":{"\_\_typename":"ComponentScriptGroupsDefinition","afterInteractive":{"\_\_typename":"PageScriptGroupDefinition","group":"AFTER\_INTERACTIVE","scriptIds":\[\]},"lazyOnLoad":{"\_\_typename":"PageScriptGroupDefinition","group":"LAZY\_ON\_LOAD","scriptIds":\[\]}},"componentScripts":\[\]},"cachedText({\\"lastModified\\":\\"1758304526186\\",\\"locale\\":\\"en-US\\",\\"namespaces\\":\[\\"components/community/NavbarDropdownToggle\\"\]})":\[{"\_\_ref":"CachedAsset:text:en\_US-components/community/NavbarDropdownToggle-1758304526186"}\],"cachedText({\\"lastModified\\":\\"1758304526186\\",\\"locale\\":\\"en-US\\",\\"namespaces\\":\[\\"components/messages/MessageCoverImage\\"\]})":\[{"\_\_ref":"CachedAsset:text:en\_US-components/messages/MessageCoverImage-1758304526186"}\],"cachedText({\\"lastModified\\":\\"1758304526186\\",\\"locale\\":\\"en-US\\",\\"namespaces\\":\[\\"shared/client/components/nodes/NodeTitle\\"\]})":\[{"\_\_ref":"CachedAsset:text:en\_US-shared/client/components/nodes/NodeTitle-1758304526186"}\],"cachedText({\\"lastModified\\":\\"1758304526186\\",\\"locale\\":\\"en-US\\",\\"namespaces\\":\[\\"components/messages/MessageTimeToRead\\"\]})":\[{"\_\_ref":"CachedAsset:text:en\_US-components/messages/MessageTimeToRead-1758304526186"}\],"cachedText({\\"lastModified\\":\\"1758304526186\\",\\"locale\\":\\"en-US\\",\\"namespaces\\":\[\\"components/messages/MessageSubject\\"\]})":\[{"\_\_ref":"CachedAsset:text:en\_US-components/messages/MessageSubject-1758304526186"}\],"cachedText({\\"lastModified\\":\\"1758304526186\\",\\"locale\\":\\"en-US\\",\\"namespaces\\":\[\\"components/users/UserLink\\"\]})":\[{"\_\_ref":"CachedAsset:text:en\_US-components/users/UserLink-1758304526186"}\],"cachedText({\\"lastModified\\":\\"1758304526186\\",\\"locale\\":\\"en-US\\",\\"namespaces\\":\[\\"shared/client/components/users/UserRank\\"\]})":\[{"\_\_ref":"CachedAsset:text:en\_US-shared/client/components/users/UserRank-1758304526186"}\],"cachedText({\\"lastModified\\":\\"1758304526186\\",\\"locale\\":\\"en-US\\",\\"namespaces\\":\[\\"components/messages/MessageTime\\"\]})":\[{"\_\_ref":"CachedAsset:text:en\_US-components/messages/MessageTime-1758304526186"}\],"cachedText({\\"lastModified\\":\\"1758304526186\\",\\"locale\\":\\"en-US\\",\\"namespaces\\":\[\\"components/messages/MessageBody\\"\]})":\[{"\_\_ref":"CachedAsset:text:en\_US-components/messages/MessageBody-1758304526186"}\],"cachedText({\\"lastModified\\":\\"1758304526186\\",\\"locale\\":\\"en-US\\",\\"namespaces\\":\[\\"components/messages/MessageCustomFields\\"\]})":\[{"\_\_ref":"CachedAsset:text:en\_US-components/messages/MessageCustomFields-1758304526186"}\],"cachedText({\\"lastModified\\":\\"1758304526186\\",\\"locale\\":\\"en-US\\",\\"namespaces\\":\[\\"components/messages/MessageRevision\\"\]})":\[{"\_\_ref":"CachedAsset:text:en\_US-components/messages/MessageRevision-1758304526186"}\],"cachedText({\\"lastModified\\":\\"1758304526186\\",\\"locale\\":\\"en-US\\",\\"namespaces\\":\[\\"shared/client/components/common/QueryHandler\\"\]})":\[{"\_\_ref":"CachedAsset:text:en\_US-shared/client/components/common/QueryHandler-1758304526186"}\],"cachedText({\\"lastModified\\":\\"1758304526186\\",\\"locale\\":\\"en-US\\",\\"namespaces\\":\[\\"components/messages/MessageReplyButton\\"\]})":\[{"\_\_ref":"CachedAsset:text:en\_US-components/messages/MessageReplyButton-1758304526186"}\],"cachedText({\\"lastModified\\":\\"1758304526186\\",\\"locale\\":\\"en-US\\",\\"namespaces\\":\[\\"components/messages/MessageAuthorBio\\"\]})":\[{"\_\_ref":"CachedAsset:text:en\_US-components/messages/MessageAuthorBio-1758304526186"}\],"cachedText({\\"lastModified\\":\\"1758304526186\\",\\"locale\\":\\"en-US\\",\\"namespaces\\":\[\\"shared/client/components/users/UserAvatar\\"\]})":\[{"\_\_ref":"CachedAsset:text:en\_US-shared/client/components/users/UserAvatar-1758304526186"}\],"cachedText({\\"lastModified\\":\\"1758304526186\\",\\"locale\\":\\"en-US\\",\\"namespaces\\":\[\\"shared/client/components/ranks/UserRankLabel\\"\]})":\[{"\_\_ref":"CachedAsset:text:en\_US-shared/client/components/ranks/UserRankLabel-1758304526186"}\],"cachedText({\\"lastModified\\":\\"1758304526186\\",\\"locale\\":\\"en-US\\",\\"namespaces\\":\[\\"components/common/ExternalLinkWarningModal\\"\]})":\[{"\_\_ref":"CachedAsset:text:en\_US-components/common/ExternalLinkWarningModal-1758304526186"}\],"cachedText({\\"lastModified\\":\\"1758304526186\\",\\"locale\\":\\"en-US\\",\\"namespaces\\":\[\\"components/tags/TagView/TagViewChip\\"\]})":\[{"\_\_ref":"CachedAsset:text:en\_US-components/tags/TagView/TagViewChip-1758304526186"}\],"cachedText({\\"lastModified\\":\\"1758304526186\\",\\"locale\\":\\"en-US\\",\\"namespaces\\":\[\\"components/users/UserRegistrationDate\\"\]})":\[{"\_\_ref":"CachedAsset:text:en\_US-components/users/UserRegistrationDate-1758304526186"}\],"cachedText({\\"lastModified\\":\\"1758304526186\\",\\"locale\\":\\"en-US\\",\\"namespaces\\":\[\\"shared/client/components/nodes/NodeAvatar\\"\]})":\[{"\_\_ref":"CachedAsset:text:en\_US-shared/client/components/nodes/NodeAvatar-1758304526186"}\],"cachedText({\\"lastModified\\":\\"1758304526186\\",\\"locale\\":\\"en-US\\",\\"namespaces\\":\[\\"shared/client/components/nodes/NodeDescription\\"\]})":\[{"\_\_ref":"CachedAsset:text:en\_US-shared/client/components/nodes/NodeDescription-1758304526186"}\],"cachedText({\\"lastModified\\":\\"1758304526186\\",\\"locale\\":\\"en-US\\",\\"namespaces\\":\[\\"shared/client/components/nodes/NodeIcon\\"\]})":\[{"\_\_ref":"CachedAsset:text:en\_US-shared/client/components/nodes/NodeIcon-1758304526186"}\]},"Theme:customTheme1":{"\_\_typename":"Theme","id":"customTheme1"},"User:user:-1":{"\_\_typename":"User","id":"user:-1","entityType":"USER","eventPath":"community:gxcuf89792/user:-1","uid":-1,"login":"Deleted","email":"","avatar":null,"rank":null,"kudosWeight":1,"registrationData":{"\_\_typename":"RegistrationData","status":"ANONYMOUS","registrationTime":null,"confirmEmailStatus":false,"registrationAccessLevel":"VIEW","ssoRegistrationFields":\[\]},"ssoId":null,"profileSettings":{"\_\_typename":"ProfileSettings","dateDisplayStyle":{"\_\_typename":"InheritableStringSettingWithPossibleValues","key":"layout.friendly\_dates\_enabled","value":"false","localValue":"true","possibleValues":\["true","false"\]},"dateDisplayFormat":{"\_\_typename":"InheritableStringSetting","key":"layout.format\_pattern\_date","value":"MMM dd yyyy","localValue":"MM-dd-yyyy"},"language":{"\_\_typename":"InheritableStringSettingWithPossibleValues","key":"profile.language","value":"en-US","localValue":null,"possibleValues":\["en-US","es-ES"\]},"repliesSortOrder":{"\_\_typename":"InheritableStringSettingWithPossibleValues","key":"config.user\_replies\_sort\_order","value":"DEFAULT","localValue":"DEFAULT","possibleValues":\["DEFAULT","LIKES","PUBLISH\_TIME","REVERSE\_PUBLISH\_TIME"\]}},"deleted":false},"CachedAsset:pages-1758304527927":{"\_\_typename":"CachedAsset","id":"pages-1758304527927","value":\[{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"BlogViewAllPostsPage","type":"BLOG","urlPath":"/category/:categoryId/blog/:boardId/all-posts/(/:after\|/:before)?","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"CasePortalPage","type":"CASE\_PORTAL","urlPath":"/caseportal","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"CreateGroupHubPage","type":"GROUP\_HUB","urlPath":"/groups/create","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"CaseViewPage","type":"CASE\_DETAILS","urlPath":"/case/:caseId/:caseNumber","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"InboxPage","type":"COMMUNITY","urlPath":"/inbox","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"HelpFAQPage","type":"COMMUNITY","urlPath":"/help","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"IdeaMessagePage","type":"IDEA\_POST","urlPath":"/idea/:boardId/:messageSubject/:messageId","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"IdeaViewAllIdeasPage","type":"IDEA","urlPath":"/category/:categoryId/ideas/:boardId/all-ideas/(/:after\|/:before)?","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"LoginPage","type":"USER","urlPath":"/signin","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"WorkstreamsPage","type":"COMMUNITY","urlPath":"/workstreams","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"BlogPostPage","type":"BLOG","urlPath":"/category/:categoryId/blogs/:boardId/create","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"UserBlogPermissions.Page","type":"COMMUNITY","urlPath":"/c/user-blog-permissions/page","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"ThemeEditorPage","type":"COMMUNITY","urlPath":"/designer/themes","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"TkbViewAllArticlesPage","type":"TKB","urlPath":"/category/:categoryId/kb/:boardId/all-articles/(/:after\|/:before)?","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1730819800000,"localOverride":null,"page":{"id":"AllEvents","type":"CUSTOM","urlPath":"/Events","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"OccasionEditPage","type":"EVENT","urlPath":"/event/:boardId/:messageSubject/:messageId/edit","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"OAuthAuthorizationAllowPage","type":"USER","urlPath":"/auth/authorize/allow","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"PageEditorPage","type":"COMMUNITY","urlPath":"/designer/pages","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"PostPage","type":"COMMUNITY","urlPath":"/category/:categoryId/:boardId/create","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"CreateUserGroup.Page","type":"COMMUNITY","urlPath":"/c/create-user-group/page","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"ForumBoardPage","type":"FORUM","urlPath":"/category/:categoryId/discussions/:boardId","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"TkbBoardPage","type":"TKB","urlPath":"/category/:categoryId/kb/:boardId","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"EventPostPage","type":"EVENT","urlPath":"/category/:categoryId/events/:boardId/create","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"UserBadgesPage","type":"COMMUNITY","urlPath":"/users/:login/:userId/badges","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"GroupHubMembershipAction","type":"GROUP\_HUB","urlPath":"/membership/join/:nodeId/:membershipType","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"MaintenancePage","type":"COMMUNITY","urlPath":"/maintenance","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"IdeaReplyPage","type":"IDEA\_REPLY","urlPath":"/idea/:boardId/:messageSubject/:messageId/comments/:replyId","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"UserSettingsPage","type":"USER","urlPath":"/mysettings/:userSettingsTab","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"GroupHubsPage","type":"GROUP\_HUB","urlPath":"/groups","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"ForumPostPage","type":"FORUM","urlPath":"/category/:categoryId/discussions/:boardId/create","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"OccasionRsvpActionPage","type":"OCCASION","urlPath":"/event/:boardId/:messageSubject/:messageId/rsvp/:responseType","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"VerifyUserEmailPage","type":"USER","urlPath":"/verifyemail/:userId/:verifyEmailToken","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"AllOccasionsPage","type":"OCCASION","urlPath":"/category/:categoryId/events/:boardId/all-events/(/:after\|/:before)?","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"EventBoardPage","type":"EVENT","urlPath":"/category/:categoryId/events/:boardId","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"TkbReplyPage","type":"TKB\_REPLY","urlPath":"/kb/:boardId/:messageSubject/:messageId/comments/:replyId","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"IdeaBoardPage","type":"IDEA","urlPath":"/category/:categoryId/ideas/:boardId","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"CommunityGuideLinesPage","type":"COMMUNITY","urlPath":"/communityguidelines","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"CaseCreatePage","type":"SALESFORCE\_CASE\_CREATION","urlPath":"/caseportal/create","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"TkbEditPage","type":"TKB","urlPath":"/kb/:boardId/:messageSubject/:messageId/edit","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"ForgotPasswordPage","type":"USER","urlPath":"/forgotpassword","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"IdeaEditPage","type":"IDEA","urlPath":"/idea/:boardId/:messageSubject/:messageId/edit","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"TagPage","type":"COMMUNITY","urlPath":"/tag/:tagName","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"BlogBoardPage","type":"BLOG","urlPath":"/category/:categoryId/blog/:boardId","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"OccasionMessagePage","type":"OCCASION\_TOPIC","urlPath":"/event/:boardId/:messageSubject/:messageId","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"ManageContentPage","type":"COMMUNITY","urlPath":"/managecontent","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"ClosedMembershipNodeNonMembersPage","type":"GROUP\_HUB","urlPath":"/closedgroup/:groupHubId","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"CommunityPage","type":"COMMUNITY","urlPath":"/","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"ForumMessagePage","type":"FORUM\_TOPIC","urlPath":"/discussions/:boardId/:messageSubject/:messageId","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"IdeaPostPage","type":"IDEA","urlPath":"/category/:categoryId/ideas/:boardId/create","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1730819800000,"localOverride":null,"page":{"id":"CommunityHub.Page","type":"CUSTOM","urlPath":"/Directory","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"BlogMessagePage","type":"BLOG\_ARTICLE","urlPath":"/blog/:boardId/:messageSubject/:messageId","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"RegistrationPage","type":"USER","urlPath":"/register","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"EditGroupHubPage","type":"GROUP\_HUB","urlPath":"/group/:groupHubId/edit","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"ForumEditPage","type":"FORUM","urlPath":"/discussions/:boardId/:messageSubject/:messageId/edit","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"ResetPasswordPage","type":"USER","urlPath":"/resetpassword/:userId/:resetPasswordToken","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1730819800000,"localOverride":null,"page":{"id":"AllBlogs.Page","type":"CUSTOM","urlPath":"/blogs","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"TkbMessagePage","type":"TKB\_ARTICLE","urlPath":"/kb/:boardId/:messageSubject/:messageId","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"BlogEditPage","type":"BLOG","urlPath":"/blog/:boardId/:messageSubject/:messageId/edit","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"ManageUsersPage","type":"USER","urlPath":"/users/manage/:tab?/:manageUsersTab?","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"ForumReplyPage","type":"FORUM\_REPLY","urlPath":"/discussions/:boardId/:messageSubject/:messageId/replies/:replyId","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"PrivacyPolicyPage","type":"COMMUNITY","urlPath":"/privacypolicy","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"NotificationPage","type":"COMMUNITY","urlPath":"/notifications","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"UserPage","type":"USER","urlPath":"/users/:login/:userId","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"HealthCheckPage","type":"COMMUNITY","urlPath":"/health","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"OccasionReplyPage","type":"OCCASION\_REPLY","urlPath":"/event/:boardId/:messageSubject/:messageId/comments/:replyId","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"ManageMembersPage","type":"GROUP\_HUB","urlPath":"/group/:groupHubId/manage/:tab?","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"SearchResultsPage","type":"COMMUNITY","urlPath":"/search","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"BlogReplyPage","type":"BLOG\_REPLY","urlPath":"/blog/:boardId/:messageSubject/:messageId/replies/:replyId","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"GroupHubPage","type":"GROUP\_HUB","urlPath":"/group/:groupHubId","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"TermsOfServicePage","type":"COMMUNITY","urlPath":"/termsofservice","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"CategoryPage","type":"CATEGORY","urlPath":"/category/:categoryId","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"ForumViewAllTopicsPage","type":"FORUM","urlPath":"/category/:categoryId/discussions/:boardId/all-topics/(/:after\|/:before)?","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"TkbPostPage","type":"TKB","urlPath":"/category/:categoryId/kbs/:boardId/create","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"},{"lastUpdatedTime":1758304527927,"localOverride":null,"page":{"id":"GroupHubPostPage","type":"GROUP\_HUB","urlPath":"/group/:groupHubId/:boardId/create","\_\_typename":"PageDescriptor"},"\_\_typename":"PageResource"}\],"localOverride":false},"CachedAsset:text:en\_US-components/context/AppContext/AppContextProvider-0":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/context/AppContext/AppContextProvider-0","value":{"noCommunity":"Cannot find community","noUser":"Cannot find current user","noNode":"Cannot find node with id {nodeId}","noMessage":"Cannot find message with id {messageId}","userBanned":"We're sorry, but you have been banned from using this site.","userBannedReason":"You have been banned for the following reason: {reason}"},"localOverride":false},"CachedAsset:text:en\_US-shared/client/components/common/Loading/LoadingDot-0":{"\_\_typename":"CachedAsset","id":"text:en\_US-shared/client/components/common/Loading/LoadingDot-0","value":{"title":"Loading..."},"localOverride":false},"AssociatedImage:{\\"url\\":\\"https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/cmstNC05WEo0blc\\"}":{"\_\_typename":"AssociatedImage","url":"https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/cmstNC05WEo0blc","height":512,"width":512,"mimeType":"image/png"},"Rank:rank:4":{"\_\_typename":"Rank","id":"rank:4","position":4,"name":"Microsoft","color":"333333","icon":{"\_\_ref":"AssociatedImage:{\\"url\\":\\"https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/cmstNC05WEo0blc\\"}"},"rankStyle":"OUTLINE"},"User:user:1706682":{"\_\_typename":"User","id":"user:1706682","uid":1706682,"login":"matthewzorich","deleted":false,"avatar":{"\_\_typename":"UserAvatar","url":"https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/dS0xNzA2NjgyLTQ0MDE5MWkyODZFQTIxQ0ZFN0VCQTAz"},"rank":{"\_\_ref":"Rank:rank:4"},"email":"","messagesCount":3,"biography":null,"topicsCount":2,"kudosReceivedCount":20,"kudosGivenCount":4,"kudosWeight":1,"registrationData":{"\_\_typename":"RegistrationData","status":null,"registrationTime":"2023-01-26T23:38:53.596-08:00","confirmEmailStatus":null},"followersCount":null,"solutionsCount":0},"Category:category:microsoft-security-product":{"\_\_typename":"Category","id":"category:microsoft-security-product","entityType":"CATEGORY","displayId":"microsoft-security-product","nodeType":"category","depth":4,"title":"Microsoft Security","shortTitle":"Microsoft Security","parent":{"\_\_ref":"Category:category:microsoft-security"}},"Category:category:top":{"\_\_typename":"Category","id":"category:top","entityType":"CATEGORY","displayId":"top","nodeType":"category","depth":0,"title":"Top","shortTitle":"Top"},"Category:category:communities":{"\_\_typename":"Category","id":"category:communities","entityType":"CATEGORY","displayId":"communities","nodeType":"category","depth":1,"parent":{"\_\_ref":"Category:category:top"},"title":"Communities","shortTitle":"Communities"},"Category:category:products-services":{"\_\_typename":"Category","id":"category:products-services","entityType":"CATEGORY","displayId":"products-services","nodeType":"category","depth":2,"parent":{"\_\_ref":"Category:category:communities"},"title":"Products","shortTitle":"Products"},"Category:category:microsoft-security":{"\_\_typename":"Category","id":"category:microsoft-security","entityType":"CATEGORY","displayId":"microsoft-security","nodeType":"category","depth":3,"parent":{"\_\_ref":"Category:category:products-services"},"title":"Microsoft Security","shortTitle":"Microsoft Security","categoryPolicies":{"\_\_typename":"CategoryPolicies","canReadNode":{"\_\_typename":"PolicyResult","failureReason":null}}},"Blog:board:MicrosoftSecurityExperts":{"\_\_typename":"Blog","id":"board:MicrosoftSecurityExperts","entityType":"BLOG","displayId":"MicrosoftSecurityExperts","nodeType":"board","depth":5,"conversationStyle":"BLOG","repliesProperties":{"\_\_typename":"RepliesProperties","sortOrder":"REVERSE\_PUBLISH\_TIME","repliesFormat":"threaded"},"tagProperties":{"\_\_typename":"TagNodeProperties","tagsEnabled":{"\_\_typename":"PolicyResult","failureReason":null}},"requireTags":true,"tagType":"PRESET\_ONLY","description":"","title":"Microsoft Security Experts Blog","shortTitle":"Microsoft Security Experts Blog","parent":{"\_\_ref":"Category:category:microsoft-security-product"},"ancestors":{"\_\_typename":"CoreNodeConnection","edges":\[{"\_\_typename":"CoreNodeEdge","node":{"\_\_ref":"Community:community:gxcuf89792"}},{"\_\_typename":"CoreNodeEdge","node":{"\_\_ref":"Category:category:communities"}},{"\_\_typename":"CoreNodeEdge","node":{"\_\_ref":"Category:category:products-services"}},{"\_\_typename":"CoreNodeEdge","node":{"\_\_ref":"Category:category:microsoft-security"}},{"\_\_typename":"CoreNodeEdge","node":{"\_\_ref":"Category:category:microsoft-security-product"}}\]},"userContext":{"\_\_typename":"NodeUserContext","canAddAttachments":false,"canUpdateNode":false,"canPostMessages":false,"isSubscribed":false},"theme":{"\_\_ref":"Theme:customTheme1"},"boardPolicies":{"\_\_typename":"BoardPolicies","canViewSpamDashBoard":{"\_\_typename":"PolicyResult","failureReason":{"\_\_typename":"FailureReason","message":"error.lithium.policies.feature.moderation\_spam.action.access\_spam\_quarantine.allowed.accessDenied","key":"error.lithium.policies.feature.moderation\_spam.action.access\_spam\_quarantine.allowed.accessDenied","args":\[\]}},"canArchiveMessage":{"\_\_typename":"PolicyResult","failureReason":{"\_\_typename":"FailureReason","message":"error.lithium.policies.content\_archivals.enable\_content\_archival\_settings.accessDenied","key":"error.lithium.policies.content\_archivals.enable\_content\_archival\_settings.accessDenied","args":\[\]}},"canPublishArticleOnCreate":{"\_\_typename":"PolicyResult","failureReason":{"\_\_typename":"FailureReason","message":"error.lithium.policies.forums.policy\_can\_publish\_on\_create\_workflow\_action.accessDenied","key":"error.lithium.policies.forums.policy\_can\_publish\_on\_create\_workflow\_action.accessDenied","args":\[\]}}},"linkProperties":{"\_\_typename":"LinkProperties","isExternalLinkWarningEnabled":true}},"BlogTopicMessage:message:3753391":{"\_\_typename":"BlogTopicMessage","uid":3753391,"subject":"Total Identity Compromise: Microsoft Incident Response lessons on securing Active Directory","id":"message:3753391","entityType":"BLOG\_ARTICLE","eventPath":"category:microsoft-security-product/category:microsoft-security/category:products-services/category:communities/community:gxcuf89792board:MicrosoftSecurityExperts/message:3753391","revisionNum":5,"repliesCount":6,"author":{"\_\_ref":"User:user:1706682"},"depth":0,"hasGivenKudo":false,"board":{"\_\_ref":"Blog:board:MicrosoftSecurityExperts"},"conversation":{"\_\_ref":"Conversation:conversation:3753391"},"messagePolicies":{"\_\_typename":"MessagePolicies","canPublishArticleOnEdit":{"\_\_typename":"PolicyResult","failureReason":{"\_\_typename":"FailureReason","message":"error.lithium.policies.forums.policy\_can\_publish\_on\_edit\_workflow\_action.accessDenied","key":"error.lithium.policies.forums.policy\_can\_publish\_on\_edit\_workflow\_action.accessDenied","args":\[\]}},"canModerateSpamMessage":{"\_\_typename":"PolicyResult","failureReason":{"\_\_typename":"FailureReason","message":"error.lithium.policies.feature.moderation\_spam.action.moderate\_entity.allowed.accessDenied","key":"error.lithium.policies.feature.moderation\_spam.action.moderate\_entity.allowed.accessDenied","args":\[\]}}},"contentWorkflow":{"\_\_typename":"ContentWorkflow","state":"PUBLISH","scheduledPublishTime":null,"scheduledTimezone":null,"userContext":{"\_\_typename":"MessageWorkflowContext","canSubmitForReview":null,"canEdit":false,"canRecall":null,"canSubmitForPublication":null,"canReturnToAuthor":null,"canPublish":null,"canReturnToReview":null,"canSchedule":false},"shortScheduledTimezone":null},"readOnly":false,"editFrozen":false,"showMoveIndicator":false,"moderationData":{"\_\_ref":"ModerationData:moderation\_data:3753391"},"teaser":"","body":"

**Total Identity Compromise: Microsoft Incident Response lessons on securing Active Directory**

\\n

\\n

When Microsoft Incident Response (formerly DART/CRSP) is engaged during an incident, almost all environments include an on-premises Active Directory component. In most of these engagements, threat actors have taken full control of Active Directory –i.e., total domain compromise.

\\n

\\n

Total domain compromise often starts with the compromise of a regular non-privileged user rather than a domain admin. Threat actors can use that account to discover misconfiguration and attack paths in Active Directory that lead to full domain control. Oftentimes, threat actors leverage freely available tools such as AdFind, AD Explorer, or BloodHound to find attack paths through Active Directory environments. After total domain compromise, restoring trust back into Active Directory can take significant time and investment.

\\n

\\n

To aid in our investigations, Microsoft Incident Response leverages a custom-built Active Directory enumeration tool to retrieve metadata about users, groups, permissions, group policies and more. Microsoft Incident Response uses this data to not only aid in the investigation, but also to shape [attacker eviction and compromise recovery plans](https://techcommunity.microsoft.com/%22https://www.microsoft.com/en-us/security/blog/2021/06/09/crsp-the-emergency-team-fighting-cyber-attacks-beside-customers//%22) and to provide best practice recommendations on taking back and maintaining positive identity control. In addition to the Microsoft Incident Response custom tool, there are other tools, such as [Defender for Identity](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/defender-for-identity/what-is/%22), and open-source tools such as [BloodHound](https://techcommunity.microsoft.com/%22https://github.com/BloodHoundAD/BloodHound/%22) and [PingCastle](https://techcommunity.microsoft.com/%22https://www.pingcastle.com//%22), that you can use to secure Active Directory in your own environment.

\\n

\\n

Across all industry verticals, Microsoft Incident Response often finds similar issues within Active Directory environments. In this blog, we will be highlighting some of the most common issues seen in on-premises Active Directory environments and provide guidance on how to secure those weaknesses. These include:

\\n

\\n

Initial Access – Weak password policies, excessive privilege and poor credential hygiene, insecure account configuration

\\n

Credential Access – Privileged credential exposure, Kerberoasting, insecure delegation configuration, Local Administrator Password Solution (LAPS) misconfiguration, excessive privilege via built-in groups

\\n

Privilege Escalation – Access control list (ACL) abuse, escalation via Exchange permissions, Group Policy abuse, insecure trust configuration, compromise of other Tier 0 assets

\\n

\\n

**Initial Access**

\\n

**Weak Password Policies**

\\n

It is not uncommon for Microsoft Incident Response to engage with customers where accounts have weak or easy to guess credentials, including those of privileged users such as Domain Admins. Simple password spray attacks can lead to the compromise of such accounts. If these standard user accounts are provided VPN or remote access without multi-factor authentication, the risk is increased: threat actors can connect to the VPN via devices in their control and begin reconnaissance of the environment remotely. From here, a threat actor can then attempt to escalate to Domain Admin privileges via weaknesses in Active Directory.

\\n

\\n

**Recommendation**

\\n

Where possible, Microsoft Incident Response recommends deploying [passwordless authentication](https://techcommunity.microsoft.com/%22https://www.microsoft.com/en-us/security/business/solutions/passwordless-authentication/%22) technology, such as Windows Hello for Business (which uses biometrics such as facial recognition or fingerprints) or FIDO2 security keys. Fully deploying passwordless authentication allows you to [disallow password authentication](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/passwordless-strategy#configure-user-accounts-to-disallow-password-authentication\%22), which eliminates password-based attack vectors (such as password sprays and phishing) for those users. If you are not yet ready to begin deploying passwordless solutions, you can increase the strength of your on-premises password policy through group policy and [fine-grained password policies](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/introduction-to-active-directory-administrative-center-enhancements--level-100-#fine_grained_pswd_policy_mgmt\%22). Current guidance recommends longer (14 or more characters) but less complex passwords (no special characters or similar required), with users having to change them much less frequently. This discourages users from cycling through easy-to-guess passwords to satisfy complexity and rotation requirements, such as changing their password from ‘ _Monday10_’ to ‘ _Monday11’_.

\\n

\\n

If you are licensed for Azure Active Directory P1 or higher, you can also deploy [Azure Active Directory Password Protection](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/azure/active-directory/authentication/concept-password-ban-bad-on-premises/%22), which can disallow your users from using easy to guess passwords [even in on-premises Active Directory](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/azure/active-directory/authentication/concept-password-ban-bad-on-premises/%22). You can also ban custom words unique to your business, such as the name of your company or the city in which you operate.

\\n

\\n

For both passwordless and stronger password policies, if you work in a complex environment where the rollout of those solutions may take some time, start by targeting your Domain Admins and other privileged users. Your Tier 0 accounts can, and should, be held to a higher security standard.

\\n

\\n

**Excessive Privilege and Poor Credential Hygiene**

\\n

One of the most common issues found in Active Directory is accounts, particularly service accounts, being assigned too much privilege. In Microsoft Incident Response engagements, it is not uncommon to find multiple service accounts and named user accounts to be granted Domain Admin privileges. Additionally, service accounts used for applications or scripts are often granted local administrative access over all workstations and servers. Though this is an easy way to allow a product or script to function, these accounts then become a weak point in your security.

\\n

\\n

Service accounts are attractive targets because the passwords are rarely rotated. Security controls for them are often weaker, and they can’t be protected by MFA. Furthermore, the passwords for these accounts are often stored in clear text, whether that be sent in email, saved to text files on devices, or used in clear text in command line arguments. The combination of many Domain Admin accounts and poor technical controls over those accounts increase the risk for credential theft.

\\n

\\n

This excessive privilege also extends to too many users having local administrative rights on their own devices. If a compromised user does not have local administrative rights on their device, it is harder for a threat actor to continue to move laterally in the environment from that device.

\\n

\\n

**Recommendation**

\\n

There is no specific guidance on how many Domain Admin accounts should exist in each environment, as the requirements for privileged accounts will be unique for each environment. With that said, any requests to have additional Domain Admins should be scrutinized closely, with the preference always being to grant a lower level of privilege, particularly to service accounts. Even though adding service accounts to Domain Admins is an easy way to ensure an application works, most of these accounts can be assigned much less privilege and still function correctly. They can also often be granted access to only a subset of devices rather than all workstations and servers.

\\n

\\n

If you don’t have strong controls to govern secure credential practice for your most important accounts, then the more Domain Admin level accounts you add, the more risk you incur. For service accounts, investigate whether [Group Managed Service Accounts](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/group-managed-service-accounts-overview/%22) (gMSA), which can provide automatic password management, would be suitable for the workload.

\\n

\\n

**Insecure Account Configuration**

\\n

In Active Directory, misconfiguration can be a reason the security of individual user accounts is weaker than it could be. Some of the settings to scrutinize for proper configuration include:

\\n

\\n

\\n- Do not require Kerberos pre-authentication.
\\n- Store password using reversible encryption.
\\n- Password not required.
\\n- Password stored with weak encryption.
\\n

\\n

Enabling any of these settings drastically reduces the security of an account. An adversary can enumerate a directory with relative ease to find any accounts that have these flags. The credentials for these accounts may then be easier for a threat actor to retrieve.

\\n

\\n

**Recommendation**

\\n

Defender for Identity, via the Secure Score portal, provides an excellent summary of these risky account flags. For each configuration item, it lists which accounts are affected and how to remediate the issue. Other tooling such as BloodHound or PingCastle can also flag these account issues.

\\n

\\n

**Credential Access**

\\n

**Privileged Credential Exposure**

\\n

During cyber-attacks, adversaries often seek to obtain privileged credentials. These credentials are viewed as ‘crown jewels’ because they allow threat actors to complete their objectives. Once privileged credentials are obtained, they can be used to:

\\n

\\n

\\n- Add additional persistence mechanisms, such as scheduled tasks, installing services, or creating additional user accounts.
\\n- Disable or bypass endpoint antivirus or other security controls.
\\n- Deploy malware or ransomware.
\\n- Exfiltrate sensitive data.
\\n

\\n

As administrators log on to devices directly or connect to devices remotely to complete their day-to-day work, they may leave behind privileged credentials. Threat actors can leverage tools such as Mimikatz or secretsdump (part of the Impacket framework) to retrieve those credentials. As privileged users log on to more and more machines, attackers have additional opportunities to locate and extract those credentials. For example, if members of the Domain Admins group regularly log on to end user workstations to troubleshoot issues, then Domain Admin credentials may be exposed on each device, increasing a threat actor’s chances of locating and extracting them.

\\n

\\n

To help customers understand this privileged credential spread, Microsoft Incident Response collects logon telemetry from the event logs on devices, signals from Microsoft Defender for Endpoint, or both. From that data, a map is created of Tier 0 accounts, such as Domain Admins, logging onto devices that are not considered Tier 0, such as member servers and workstations.

\\n

\\n

![\"mzorich_5-1677476139108.png\"](https://techcommunity.microsoft.com/%22https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNzUzMzkxLTQ0NTYwOWlCRTJGQzIzNEE0MTQ3NTk5?image-dimensions=984x541&revision=5\%22)

\\n

_Figure 1: Map of Domain Admin login paths to non-Tier 0 servers._

\\n

\\n

In this visual, the green circles represent Domain Admins. The red dotted lines represent RDP logons to devices, while the black dotted lines represent network logons. In this example, we can see two domain admins that have logged onto three different servers. Should a threat actor compromise one of these three servers, there is potential for theft of a Domain Admin level credential. The larger the environment, the more this issue becomes apparent. If we add additional admins and other non-Tier 0 devices, we can see the immediate impact on our footprint.

\\n

\\n

![\"mzorich_6-1677476230313.png\"](https://techcommunity.microsoft.com/%22https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNzUzMzkxLTQ0NTYxMGk4NTVCODQ3Mzg0ODZERDJC?image-dimensions=931x737&revision=5\%22)

\\n

_Figure 2: Map of Domain Admin login paths to non-Tier 0 servers and other devices._

\\n

\\n

With additional Domain Admins and those admins logging onto other non-tier 0 devices, credential exposure has increased significantly.

\\n

The goal of these diagrams is to help customers visualize where privileged credentials are being left on their network and to start thinking from the mindset of a threat actor. In large and complex Active Directory environments, these diagrams can become immense, and the number of endpoints climbs into the thousands.

\\n

\\n

**Recommendation**

\\n

Microsoft’s solution to reduce privileged credential exposure is to implement the [enterprise access model](https://techcommunity.microsoft.com/%22http://aka.ms/tier0/%22). This administration model seeks to reduce the spread of privileged credentials by restricting the devices that Domain Admins (and similar accounts) can log on to. In large and complex environments, it is safe to assume that some users and devices will be compromised. Your most privileged accounts should only access Tier 0 assets from hardened devices, known as privileged access workstations (PAWs). Using least-privileged access is a key part of [Zero Trust principals](https://techcommunity.microsoft.com/%22https://www.microsoft.com/en-us/security/business/zero-trust/%22). By reducing the opportunity to extract privileged credentials, we reduce the impact of compromise on a single device or user.

\\n

\\n

Deploying the enterprise access model is a journey, and every organization is at a different stage of that journey. Regardless of your current posture, you can always reduce privilege credential spread, both through technical controls and changes to the way staff work. This [table](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/windows-server/identity/securing-privileged-access/reference-tools-logon-types/%22) [in the Microsoft Learn documentation](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/windows-server/identity/securing-privileged-access/reference-tools-logon-types/%22) lists various logon types and whether credentials are left on the destination device. When administering remote systems, Microsoft Incident Response recommends using methods that do not leave credentials behind wherever possible.

\\n

\\n

Defender for Identity also maps these lateral movement paths, showing paths where compromise of a regular user can lead to domain compromise. These are [integrated directly within user and computer objects in the Microsoft 365 Defender portal](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/defender-for-identity/understand-lateral-movement-paths#where-can-i-find-defender-for-identity-lmps\%22).

\\n

\\n

![\"mzorich_1-1677549966901.png\"](https://techcommunity.microsoft.com/%22https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNzUzMzkxLTQ0NTkzM2lGNjk1MzgyN0E0NzM2QkRC?image-dimensions=826x388&revision=5\%22)

\\n

\\n

_Figure 3: Defender for Identity page_ _for mapping a user’s lateral movement paths._

\\n

\\n

The highest risk users and computers are also shown in the [Secure Score](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/defender-for-identity/security-assessment-riskiest-lmp/%22) portal, allowing you to remediate objects most at risk.

\\n

\\n

**Kerberoasting**

\\n

Kerberoasting is a technique used by threat actors to crack the passwords of accounts, generally service accounts, that have [service principal names](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/windows/win32/ad/service-principal-names/%22) (SPNs) associated with them. If a regular user in Active Directory is compromised, they can request a ticket (which includes the hashed password) via tools such as Rubeus for **any** account with an SPN configured. The threat actor can then extract this hash from memory and attempt to crack the password offline. If they can crack the password, they can then authenticate as and assume the privileges of that service account.

\\n

\\n

It is also not uncommon for Microsoft Incident Response to detect SPNs registered to privileged admin accounts or service accounts that have been added to privileged groups. Often these SPNs are configured for testing and then never removed, leaving them vulnerable to Kerberoasting.

\\n

\\n

**Recommendation**

\\n

Microsoft Incident Response recommends that you review all accounts configured with SPNs to ensure they are still required. For those that are actively in use, ensure the passwords associated for those accounts are extremely complex and rotated where practical.

\\n

\\n

Defender for Identity includes logic to detect Kerberoasting activity in your environment. By taking signals from your domain controllers, Defender for Identity can help detect users enumerating your domain looking for Kerberoast-able accounts or attempts to actively exploit those accounts.

\\n

\\n

**Insecure Delegation Configuration**

\\n

Unconstrained Kerberos delegation provides the ability for an entity to impersonate other users. This helps with authentication through multi-tier applications. For example, a web server running IIS may have delegation configured to access an SQL server, which stores the data for the web site. When you log onto the web server, the web server then uses delegation to authenticate on behalf of you to SQL. In doing this, the user’s Kerberos Ticket Granting Ticket (TGT) is stored in memory on the web server. If a threat actor compromises that web server, they could retrieve those tickets and impersonate any users that had logged on. If a Domain Admin happened to log on, then the threat actor would have access to a Domain Admin TGT and could assume full control of Active Directory.

\\n

\\n

**Recommendation**

\\n

Review all the users and devices that are enabled for delegation. These are available in the [Defender for Identity section of Secure Score](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/defender-for-identity/security-assessment-unconstrained-kerberos/%22). If delegation is required it should be restricted to only the required services, not fully unconstrained.

\\n

\\n

Administrative accounts should never be enabled for delegation. You can prevent these privileged accounts from being targeted by enabling the ‘Account is sensitive and cannot be delegated’ flag on them. You can optionally add these accounts to the ‘ [Protected Users’ group](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group/%22). This group provides protections over and above just preventing delegation and makes them even more secure; however, it may cause operational issues, so it is worth testing in your environment.

\\n

\\n

**Local Administrator Password Solution (LAPS)**

\\n

Microsoft Incident Response often encounters situations where [LAPS](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/windows-server/identity/laps/laps-overview/%22) has not been deployed to an environment. LAPS is the Microsoft solution to automatically manage the password for the built-in Administrator account on Windows devices. When machines are built or imaged, they often have the same password for the built-in Administrator account. If this is never changed, a single password can give local administrative rights to all machines and may provide opportunities for lateral movement. LAPS solves this problem by ensuring each device has a unique local administrator password and rotates it regularly.

\\n

\\n

Additionally, even in cases where LAPS has been deployed, sometimes it has not been fully operationalized by the business. As a result, despite LAPS managing the local administrator account on these devices, there are still user groups that have local administrative rights over all the workstations or all the servers, or both. These groups can contain numerous users, generally belonging to the service desk or other operations staff. These operational staff then use their own accounts to administer those devices, rather than the LAPS credentials. IT configurations can also exist where a secondary, non-LAPS managed account still exists with an easy to guess password, defeating the benefit gained by deploying LAPS.

\\n

\\n

As noted earlier, groups with broad administrative access give threat actors additional opportunity to compromise privileged credentials. Should an endpoint where one of these accounts has logged onto become compromised, a threat actor could have credentials to compromise all the devices in the network.

\\n

\\n

**Recommendation**

\\n

It is important to not only deploy LAPS to endpoints, but to ensure that IT standard operating procedures are updated to ensure LAPS is used. This allows companies to remove privilege from administrative accounts and reduce credential theft risk across the business Additionally, it is crucial to understand which users can retrieve the LAPS password for use, since the ability to retrieve this password grants local administrative access to that device. The ability to read the LAPS password is controlled via the ‘ms-Mcs-AdmPwd’ attribute and should be audited to ensure access is only granted to users that require it.

\\n

\\n

**Excessive Privilege via Built-In Groups**

\\n

During incident response, companies often have alerting and monitoring in place for changes to groups like Domain and Enterprise Admins. These groups are widely known to hold the highest level of privilege in Active Directory. However, there are other privileged built-in groups that are attractive to threat actors and are often not held to the same level of scrutiny. Groups such as Account and Server Operators have wide ranging privilege over your Active Directory. For example, by default Server Operators can log on to Domain Controllers, restart services, backup and restore files, and more.

\\n

\\n

**Recommendation**

\\n

It is recommended that, where possible, privileged built-in groups not contain any users. Instead, the appropriate privilege should be granted specifically to users that require it. Additionally, Microsoft Incident Response recommends reviewing the current membership of those [groups](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory#table-b-1-built-in-and-default-accounts-and-groups-in-active-directory\%22) and adding additional alerting to changes to them in the same way you would alert on Domain or Enterprise admin changes.

\\n

\\n

**Privilege Escalation**

\\n

**Access Control List Abuse**

\\n

Access Control Lists (ACL) misconfiguration is one of the most common issues Microsoft Incident Response finds in Active Directory environments. Active Directory ACLs are exceptionally granular, complex, and easy to configure incorrectly. It is easy to reduce the security posture of your Active Directory environment without having any operational impact on your users. As ACLs are configured in your environment through business-as-usual activities, attack paths start to form. These attack paths create an escalation path from a low privileged user to total domain control. A threat actor can take advantage of the paths created by the combination of excessive privilege and scope on ACLs. A threat actor can take advantage of the paths created by the combination of excessive privilege and scope on ACLs.

\\n

\\n

Two common ACLs that Microsoft Incident Response sees regularly in Active Directory are:

\\n

\\n- GenericAll – this privilege is the same as Full Control access. If a user was compromised and that user had GenericAll over a highly privileged group, then the threat actor could add additional members to that group.
\\n- WriteDacl – this privilege allows manipulation of the ACL on an object. With this privilege a threat actor can change the ACL on an object such as a group. If a user was compromised and that user had WriteDacl over a highly privileged group, the threat actor could add a new ACL to that group. That new ACL could then give them access to add additional members to the group, such as themselves.
\\n

\\n

These permissions are often set at the top of the Active Directory hierarchy. They are also often applied to users and groups that do not require those permissions, effectively granting those group members full domain control. The members of these groups are very rarely secured in the same way that Domain and Enterprise Admins are.

\\n

\\n

In addition, Microsoft Incident Response often detects insecure ACLs on the [AdminSdHolder](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/appendix-c--protected-accounts-and-groups-in-active-directory#adminsdholder\%22) object, which is responsible for managing permissions on protected users and groups. If an adversary can manipulate the ACL on AdminSdHolder, it will be propagated on to those protected users and groups when the SDProp process runs. The adversary will then have rights to change membership of protected groups such as Domain Admins, allowing them to add themselves. The documentation for [BloodHound](https://techcommunity.microsoft.com/%22https://bloodhound.readthedocs.io/en/latest/data-analysis/edges.html/%22) describes these and several other ACL ‘edges’ that can be abused for privilege escalation.

\\n

\\n

**Recommendation**

\\n

Microsoft Incident Response recommends auditing permissions through your Active Directory environment using tools such as Defender for Identity and running sanctioned audits of attack paths using BloodHound and remediating paths that can lead to domain compromise.

\\n

\\n

**Escalation via Exchange Permissions**

\\n

Prior to the use of corporate cloud email services such as Office 365, customers ran their own on-premises Exchange environments. Many customers still maintain a complete on-premises Exchange environment. On-premises Exchange and Active Directory have always been tied closely together, with Exchange maintaining high privilege through Active Directory. Even in environments that have migrated user mailboxes to Office 365, an on-premises Exchange footprint often remains. It may exist to manage users not yet migrated, for legacy applications that are not able to integrate with Office 365, or to service non-internet connected workloads.

\\n

\\n

These on-premises Exchange environments often retain high privilege through Active Directory, and groups such as ‘Exchange Trusted Subsystem’ and ‘Exchange Servers’ can have a direct path to total domain control.

\\n

\\n

On-premises Exchange is also often internet-facing to allow users to access resources such as Outlook Web Access. Like any internet facing service, this increases the surface area for attack. If a threat actor can obtain SYSTEM privilege on an Exchange server and Exchange still retains excessive permissions in Active Directory, then it can lead to complete domain compromise.

\\n

\\n

**Recommendation**

\\n

It is possible to decouple the privilege held by Exchange in Active Directory by deploying the [split permissions model for Exchange](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/exchange/permissions/split-permissions/configure-exchange-for-split-permissions?view=exchserver-2019\%22). By deploying this model, permissions for Active Directory and Exchange are separated.

\\n

\\n

After deploying the Exchange split permissions model, there are [operational changes](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/exchange/permissions/split-permissions/split-permissions?view=exchserver-2019\%22) required by staff who administer both Exchange and Active Directory. If you don’t want to deploy the entire split permissions model, you can still reduce the permissions Exchange has in Active Directory by implementing the changes in the following Microsoft [guidance](https://techcommunity.microsoft.com/%22https://support.microsoft.com/en-us/topic/reducing-permissions-required-to-run-exchange-server-when-you-use-the-shared-permissions-model-e1972d47-d714-fd76-1fd5-7cdcb85408ed/%22).

\\n

\\n

If you have completely migrated to Office 365 but maintain on-premises Exchange servers for ease of management, you may now be able to [turn off those on-premises servers](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/exchange/manage-hybrid-exchange-recipients-with-management-tools/%22).

\\n

\\n

**Group Policy ACL Abuse**

\\n

Group Policy is often a tool used by threat actors to establish persistence (via the creation of scheduled tasks), create additional accounts, or deploy malware. It is also used as a ransomware deployment mechanism. If a threat actor has not yet compromised a Domain Admin, they may have been able to compromise an account that maintains permissions over Group Policy Objects. For instance, the ability to create, update, or even link policies may have been delegated to other groups.

\\n

\\n

If an existing Group Policy is configured to run a startup script, a threat actor can change the path of that script to then have it execute a malicious payload. If a group policy exists to disable endpoint security tooling as an exemption, a threat actor could leverage the permissions to link policy by applying that policy to all devices in the environment. This would not require the threat actor to update the policy, just change the scope of it.  Additionally, regular users can be given additional privileges via [User Rights Assignments](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/user-rights-assignment/%22). These privileges are often not required by the users and are granted accidentally.

\\n

\\n

**Recommendation**

\\n

The ability to manipulate Group Policy is a highly privileged action and users and groups with delegated responsibility to manage it should be held to the same standards as Domain Admins or similar. Ensure that permissions to create, update, and link group policies are in line with least privilege principles.

\\n

\\n

In large and complex environments, the number of Group Policies in use can be overwhelming and it is not clear what policies apply to which users and devices. Using tools such as [Resultant Set of Policy](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn789183(v=ws.11)/%22) (RSoP), you can model your Group Policy objects to see the overall effect on your users and devices.

\\n

\\n

**Insecure Trust Configuration**

\\n

SID history is a capability in Active Directory to aid in domain migration. It allows Domain Admins to simplify migration by applying the SID history (in simple terms, a list of permissions) from the old account to the new account. This helps the user retain access to resources once they are migrated. An adversary can target this capability by inserting the SIDs of groups such as Domain Admins into the SID history of an account in the trusted forest and using that account to [take control of the trusting forest](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc755321(v=ws.10)?redirectedfrom=MSDN#how-sid-history-can-be-used-to-elevate-privileges\%22). This can be especially relevant during [mergers and acquisitions](https://techcommunity.microsoft.com/%22https://www.microsoft.com/en-us/security/blog/2022/11/02/microsoft-security-tips-for-mitigating-risk-in-mergers-and-acquisitions//%22), where trusts between Active Directory environments are configured to allow migrations.

\\n

\\n

**Recommendation**

\\n

Active Directory trusts should only be configured when absolutely required. If they are part of an acquisition or migration, then they should be decommissioned once migration is complete. For trusts that need to remain for operational reasons, [SID filtering](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc755321(v=ws.10)?redirectedfrom=MSDN#sid-filtering\%22) and [Selective Authentication](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc755321(v=ws.10)?redirectedfrom=MSDN#selective-authentication\%22) should be configured to reduce the attack path from other domains and forests.

\\n

\\n

**Compromise of other Tier 0 assets**

\\n

Historically, domain controllers have been at the center of Tier 0 infrastructure. While that is still true, Tier 0 has now expanded to include several interconnected systems. As ways of working have evolved, so has the underlying technology required to drive modern identity systems. In line with that, your Tier 0 footprint has also evolved and may now include systems such as:

\\n

\\n

\\n- Active Directory Federation Services
\\n- Azure Active Directory Connect
\\n- Active Directory Certificate Services
\\n

\\n

It also includes any other services or infrastructure, including 3rd party providers, that form part of your identity trust chain, such as privileged access management and identity governance systems.

\\n

\\n

\\n

![\"mzorich_12-1677477076646.png\"](https://techcommunity.microsoft.com/%22https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNzUzMzkxLTQ0NTYxNmlDNEI4MDVDODREMTk5QjY0?image-dimensions=896x558&revision=5\%22)

\\n

_Figure 4: Example of how Tier 0 assets connect to an identity trust chain._

\\n

\\n

It is important that all systems that form part of your end-to-end identity chain are included in Tier 0, and the security controls you apply to domain controllers also apply to these systems. Due to the interconnected nature of these systems, compromise of any one of them could lead to complete domain compromise. Only Tier 0 accounts should retain local administrative privileges over these systems and, where practical, access to them should be via a privileged access workstation.

\\n

\\n

**Summary**

\\n

In large and complex environments, Microsoft Incident Response often sees combinations of the above issues that reduce identity security posture significantly. These misconfigurations allow threat actors to elevate from a single non privileged user all the way to your crown jewel Domain Admin accounts.

\\n

\\n

![\"mzorich_0-1677549706251.png\"](https://techcommunity.microsoft.com/%22https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNzUzMzkxLTQ0NTkzMmlDOERGQzEyQ0JGQjEyRkY3?image-dimensions=929x237&revision=5\%22)

\\n

_Figure 5: Kill chain showing how domain compromise can start from a single compromised user._

\\n

\\n

For example, in the above kill chain, the first user was compromised due to a weak password policy. Through the initial poor password policy, additional bad credential hygiene, and ACL misconfiguration, the domain was compromised. When you multiply all the combinations of user accounts, group access, and permissions in Active Directory, many paths can exist to Domain Admin.

\\n

\\n

Attacks on Active Directory are ever evolving, and this blog covers only some of the more common issues Microsoft Incident Response observes in customer environments. Ultimately, any changes made to Active Directory can either increase or decrease the risk that a threat actor can take control of your environment. To ensure that risk is consistently decreasing, Microsoft Incident Response recommends a constant cycle of the below:

\\n

\\n

\\n- Reduce Privilege – assign all access according to the principle of least privilege. Additionally, deploy the enterprise access model to reduce privileged credential exposure. Combined, these will reduce the likelihood that a single device or user compromise leads to total domain compromise.
\\n- Audit Current Posture – use tools such as Defender for Identity and sanctioned use of BloodHound and PingCastle to audit your current Active Directory security posture and remediate the issues both surfaced through those tools and described in this blog.
\\n- Monitor Changes – monitor for changes to your Active Directory environment that can reduce your security posture or expose additional attack paths to domain compromise.

\\n- Actively Detect – alert on potential signs of compromise using Defender for Identity or custom detection rules.

\\n

\\n

A message that Microsoft Incident Response often leaves customers with is that securing Active Directory requires continued governance. You can’t ‘deploy’ Active Directory security and never have to look at it again. Active Directory security is about constant improvement and ensuring those misconfigurations and attack paths are mitigated before an adversary finds them.

\\n

","body@stringLength":"43396","rawBody":"

**Total Identity Compromise: Microsoft Incident Response lessons on securing Active Directory**

\\n

\\n

When Microsoft Incident Response (formerly DART/CRSP) is engaged during an incident, almost all environments include an on-premises Active Directory component. In most of these engagements, threat actors have taken full control of Active Directory –i.e., total domain compromise.

\\n

\\n

Total domain compromise often starts with the compromise of a regular non-privileged user rather than a domain admin. Threat actors can use that account to discover misconfiguration and attack paths in Active Directory that lead to full domain control. Oftentimes, threat actors leverage freely available tools such as AdFind, AD Explorer, or BloodHound to find attack paths through Active Directory environments. After total domain compromise, restoring trust back into Active Directory can take significant time and investment.

\\n

\\n

To aid in our investigations, Microsoft Incident Response leverages a custom-built Active Directory enumeration tool to retrieve metadata about users, groups, permissions, group policies and more. Microsoft Incident Response uses this data to not only aid in the investigation, but also to shape [attacker eviction and compromise recovery plans](https://techcommunity.microsoft.com/%22https://www.microsoft.com/en-us/security/blog/2021/06/09/crsp-the-emergency-team-fighting-cyber-attacks-beside-customers//%22) and to provide best practice recommendations on taking back and maintaining positive identity control. In addition to the Microsoft Incident Response custom tool, there are other tools, such as [Defender for Identity](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/defender-for-identity/what-is/%22), and open-source tools such as [BloodHound](https://techcommunity.microsoft.com/%22https://github.com/BloodHoundAD/BloodHound/%22) and [PingCastle](https://techcommunity.microsoft.com/%22https://www.pingcastle.com//%22), that you can use to secure Active Directory in your own environment.

\\n

\\n

Across all industry verticals, Microsoft Incident Response often finds similar issues within Active Directory environments. In this blog, we will be highlighting some of the most common issues seen in on-premises Active Directory environments and provide guidance on how to secure those weaknesses. These include:

\\n

\\n

Initial Access – Weak password policies, excessive privilege and poor credential hygiene, insecure account configuration

\\n

Credential Access – Privileged credential exposure, Kerberoasting, insecure delegation configuration, Local Administrator Password Solution (LAPS) misconfiguration, excessive privilege via built-in groups

\\n

Privilege Escalation – Access control list (ACL) abuse, escalation via Exchange permissions, Group Policy abuse, insecure trust configuration, compromise of other Tier 0 assets

\\n

\\n

**Initial Access**

\\n

**Weak Password Policies**

\\n

It is not uncommon for Microsoft Incident Response to engage with customers where accounts have weak or easy to guess credentials, including those of privileged users such as Domain Admins. Simple password spray attacks can lead to the compromise of such accounts. If these standard user accounts are provided VPN or remote access without multi-factor authentication, the risk is increased: threat actors can connect to the VPN via devices in their control and begin reconnaissance of the environment remotely. From here, a threat actor can then attempt to escalate to Domain Admin privileges via weaknesses in Active Directory.

\\n

\\n

**Recommendation**

\\n

Where possible, Microsoft Incident Response recommends deploying [passwordless authentication](https://techcommunity.microsoft.com/%22https://www.microsoft.com/en-us/security/business/solutions/passwordless-authentication/%22) technology, such as Windows Hello for Business (which uses biometrics such as facial recognition or fingerprints) or FIDO2 security keys. Fully deploying passwordless authentication allows you to [disallow password authentication](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/passwordless-strategy#configure-user-accounts-to-disallow-password-authentication\%22), which eliminates password-based attack vectors (such as password sprays and phishing) for those users. If you are not yet ready to begin deploying passwordless solutions, you can increase the strength of your on-premises password policy through group policy and [fine-grained password policies](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/introduction-to-active-directory-administrative-center-enhancements--level-100-#fine_grained_pswd_policy_mgmt\%22). Current guidance recommends longer (14 or more characters) but less complex passwords (no special characters or similar required), with users having to change them much less frequently. This discourages users from cycling through easy-to-guess passwords to satisfy complexity and rotation requirements, such as changing their password from ‘ _Monday10_’ to ‘ _Monday11’_.

\\n

\\n

If you are licensed for Azure Active Directory P1 or higher, you can also deploy [Azure Active Directory Password Protection](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/azure/active-directory/authentication/concept-password-ban-bad-on-premises/%22), which can disallow your users from using easy to guess passwords [even in on-premises Active Directory](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/azure/active-directory/authentication/concept-password-ban-bad-on-premises/%22). You can also ban custom words unique to your business, such as the name of your company or the city in which you operate.

\\n

\\n

For both passwordless and stronger password policies, if you work in a complex environment where the rollout of those solutions may take some time, start by targeting your Domain Admins and other privileged users. Your Tier 0 accounts can, and should, be held to a higher security standard.

\\n

\\n

**Excessive Privilege and Poor Credential Hygiene**

\\n

One of the most common issues found in Active Directory is accounts, particularly service accounts, being assigned too much privilege. In Microsoft Incident Response engagements, it is not uncommon to find multiple service accounts and named user accounts to be granted Domain Admin privileges. Additionally, service accounts used for applications or scripts are often granted local administrative access over all workstations and servers. Though this is an easy way to allow a product or script to function, these accounts then become a weak point in your security.

\\n

\\n

Service accounts are attractive targets because the passwords are rarely rotated. Security controls for them are often weaker, and they can’t be protected by MFA. Furthermore, the passwords for these accounts are often stored in clear text, whether that be sent in email, saved to text files on devices, or used in clear text in command line arguments. The combination of many Domain Admin accounts and poor technical controls over those accounts increase the risk for credential theft.

\\n

\\n

This excessive privilege also extends to too many users having local administrative rights on their own devices. If a compromised user does not have local administrative rights on their device, it is harder for a threat actor to continue to move laterally in the environment from that device.

\\n

\\n

**Recommendation**

\\n

There is no specific guidance on how many Domain Admin accounts should exist in each environment, as the requirements for privileged accounts will be unique for each environment. With that said, any requests to have additional Domain Admins should be scrutinized closely, with the preference always being to grant a lower level of privilege, particularly to service accounts. Even though adding service accounts to Domain Admins is an easy way to ensure an application works, most of these accounts can be assigned much less privilege and still function correctly. They can also often be granted access to only a subset of devices rather than all workstations and servers.

\\n

\\n

If you don’t have strong controls to govern secure credential practice for your most important accounts, then the more Domain Admin level accounts you add, the more risk you incur. For service accounts, investigate whether [Group Managed Service Accounts](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/group-managed-service-accounts-overview/%22) (gMSA), which can provide automatic password management, would be suitable for the workload.

\\n

\\n

**Insecure Account Configuration**

\\n

In Active Directory, misconfiguration can be a reason the security of individual user accounts is weaker than it could be. Some of the settings to scrutinize for proper configuration include:

\\n

\\n

\\n- Do not require Kerberos pre-authentication.
\\n- Store password using reversible encryption.
\\n- Password not required.
\\n- Password stored with weak encryption.
\\n

\\n

Enabling any of these settings drastically reduces the security of an account. An adversary can enumerate a directory with relative ease to find any accounts that have these flags. The credentials for these accounts may then be easier for a threat actor to retrieve.

\\n

\\n

**Recommendation**

\\n

Defender for Identity, via the Secure Score portal, provides an excellent summary of these risky account flags. For each configuration item, it lists which accounts are affected and how to remediate the issue. Other tooling such as BloodHound or PingCastle can also flag these account issues.

\\n

\\n

**Credential Access**

\\n

**Privileged Credential Exposure**

\\n

During cyber-attacks, adversaries often seek to obtain privileged credentials. These credentials are viewed as ‘crown jewels’ because they allow threat actors to complete their objectives. Once privileged credentials are obtained, they can be used to:

\\n

\\n

\\n- Add additional persistence mechanisms, such as scheduled tasks, installing services, or creating additional user accounts.
\\n- Disable or bypass endpoint antivirus or other security controls.
\\n- Deploy malware or ransomware.
\\n- Exfiltrate sensitive data.
\\n

\\n

As administrators log on to devices directly or connect to devices remotely to complete their day-to-day work, they may leave behind privileged credentials. Threat actors can leverage tools such as Mimikatz or secretsdump (part of the Impacket framework) to retrieve those credentials. As privileged users log on to more and more machines, attackers have additional opportunities to locate and extract those credentials. For example, if members of the Domain Admins group regularly log on to end user workstations to troubleshoot issues, then Domain Admin credentials may be exposed on each device, increasing a threat actor’s chances of locating and extracting them.

\\n

\\n

To help customers understand this privileged credential spread, Microsoft Incident Response collects logon telemetry from the event logs on devices, signals from Microsoft Defender for Endpoint, or both. From that data, a map is created of Tier 0 accounts, such as Domain Admins, logging onto devices that are not considered Tier 0, such as member servers and workstations.

\\n

\\n

\\n

_Figure 1: Map of Domain Admin login paths to non-Tier 0 servers._

\\n

\\n

In this visual, the green circles represent Domain Admins. The red dotted lines represent RDP logons to devices, while the black dotted lines represent network logons. In this example, we can see two domain admins that have logged onto three different servers. Should a threat actor compromise one of these three servers, there is potential for theft of a Domain Admin level credential. The larger the environment, the more this issue becomes apparent. If we add additional admins and other non-Tier 0 devices, we can see the immediate impact on our footprint.

\\n

\\n

\\n

_Figure 2: Map of Domain Admin login paths to non-Tier 0 servers and other devices._

\\n

\\n

With additional Domain Admins and those admins logging onto other non-tier 0 devices, credential exposure has increased significantly.

\\n

The goal of these diagrams is to help customers visualize where privileged credentials are being left on their network and to start thinking from the mindset of a threat actor. In large and complex Active Directory environments, these diagrams can become immense, and the number of endpoints climbs into the thousands.

\\n

\\n

**Recommendation**

\\n

Microsoft’s solution to reduce privileged credential exposure is to implement the [enterprise access model](https://techcommunity.microsoft.com/%22http://aka.ms/tier0/%22). This administration model seeks to reduce the spread of privileged credentials by restricting the devices that Domain Admins (and similar accounts) can log on to. In large and complex environments, it is safe to assume that some users and devices will be compromised. Your most privileged accounts should only access Tier 0 assets from hardened devices, known as privileged access workstations (PAWs). Using least-privileged access is a key part of [Zero Trust principals](https://techcommunity.microsoft.com/%22https://www.microsoft.com/en-us/security/business/zero-trust/%22). By reducing the opportunity to extract privileged credentials, we reduce the impact of compromise on a single device or user.

\\n

\\n

Deploying the enterprise access model is a journey, and every organization is at a different stage of that journey. Regardless of your current posture, you can always reduce privilege credential spread, both through technical controls and changes to the way staff work. This [table](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/windows-server/identity/securing-privileged-access/reference-tools-logon-types/%22) [in the Microsoft Learn documentation](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/windows-server/identity/securing-privileged-access/reference-tools-logon-types/%22) lists various logon types and whether credentials are left on the destination device. When administering remote systems, Microsoft Incident Response recommends using methods that do not leave credentials behind wherever possible.

\\n

\\n

Defender for Identity also maps these lateral movement paths, showing paths where compromise of a regular user can lead to domain compromise. These are [integrated directly within user and computer objects in the Microsoft 365 Defender portal](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/defender-for-identity/understand-lateral-movement-paths#where-can-i-find-defender-for-identity-lmps\%22).

\\n

\\n

\\n

\\n

_Figure 3: Defender for Identity page_ _for mapping a user’s lateral movement paths._

\\n

\\n

The highest risk users and computers are also shown in the [Secure Score](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/defender-for-identity/security-assessment-riskiest-lmp/%22) portal, allowing you to remediate objects most at risk.

\\n

\\n

**Kerberoasting**

\\n

Kerberoasting is a technique used by threat actors to crack the passwords of accounts, generally service accounts, that have [service principal names](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/windows/win32/ad/service-principal-names/%22) (SPNs) associated with them. If a regular user in Active Directory is compromised, they can request a ticket (which includes the hashed password) via tools such as Rubeus for **any** account with an SPN configured. The threat actor can then extract this hash from memory and attempt to crack the password offline. If they can crack the password, they can then authenticate as and assume the privileges of that service account.

\\n

\\n

It is also not uncommon for Microsoft Incident Response to detect SPNs registered to privileged admin accounts or service accounts that have been added to privileged groups. Often these SPNs are configured for testing and then never removed, leaving them vulnerable to Kerberoasting.

\\n

\\n

**Recommendation**

\\n

Microsoft Incident Response recommends that you review all accounts configured with SPNs to ensure they are still required. For those that are actively in use, ensure the passwords associated for those accounts are extremely complex and rotated where practical.

\\n

\\n

Defender for Identity includes logic to detect Kerberoasting activity in your environment. By taking signals from your domain controllers, Defender for Identity can help detect users enumerating your domain looking for Kerberoast-able accounts or attempts to actively exploit those accounts.

\\n

\\n

**Insecure Delegation Configuration**

\\n

Unconstrained Kerberos delegation provides the ability for an entity to impersonate other users. This helps with authentication through multi-tier applications. For example, a web server running IIS may have delegation configured to access an SQL server, which stores the data for the web site. When you log onto the web server, the web server then uses delegation to authenticate on behalf of you to SQL. In doing this, the user’s Kerberos Ticket Granting Ticket (TGT) is stored in memory on the web server. If a threat actor compromises that web server, they could retrieve those tickets and impersonate any users that had logged on. If a Domain Admin happened to log on, then the threat actor would have access to a Domain Admin TGT and could assume full control of Active Directory.

\\n

\\n

**Recommendation**

\\n

Review all the users and devices that are enabled for delegation. These are available in the [Defender for Identity section of Secure Score](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/defender-for-identity/security-assessment-unconstrained-kerberos/%22). If delegation is required it should be restricted to only the required services, not fully unconstrained.

\\n

\\n

Administrative accounts should never be enabled for delegation. You can prevent these privileged accounts from being targeted by enabling the ‘Account is sensitive and cannot be delegated’ flag on them. You can optionally add these accounts to the ‘ [Protected Users’ group](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group/%22). This group provides protections over and above just preventing delegation and makes them even more secure; however, it may cause operational issues, so it is worth testing in your environment.

\\n

\\n

**Local Administrator Password Solution (LAPS)**

\\n

Microsoft Incident Response often encounters situations where [LAPS](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/windows-server/identity/laps/laps-overview/%22) has not been deployed to an environment. LAPS is the Microsoft solution to automatically manage the password for the built-in Administrator account on Windows devices. When machines are built or imaged, they often have the same password for the built-in Administrator account. If this is never changed, a single password can give local administrative rights to all machines and may provide opportunities for lateral movement. LAPS solves this problem by ensuring each device has a unique local administrator password and rotates it regularly.

\\n

\\n

Additionally, even in cases where LAPS has been deployed, sometimes it has not been fully operationalized by the business. As a result, despite LAPS managing the local administrator account on these devices, there are still user groups that have local administrative rights over all the workstations or all the servers, or both. These groups can contain numerous users, generally belonging to the service desk or other operations staff. These operational staff then use their own accounts to administer those devices, rather than the LAPS credentials. IT configurations can also exist where a secondary, non-LAPS managed account still exists with an easy to guess password, defeating the benefit gained by deploying LAPS.

\\n

\\n

As noted earlier, groups with broad administrative access give threat actors additional opportunity to compromise privileged credentials. Should an endpoint where one of these accounts has logged onto become compromised, a threat actor could have credentials to compromise all the devices in the network.

\\n

\\n

**Recommendation**

\\n

It is important to not only deploy LAPS to endpoints, but to ensure that IT standard operating procedures are updated to ensure LAPS is used. This allows companies to remove privilege from administrative accounts and reduce credential theft risk across the business Additionally, it is crucial to understand which users can retrieve the LAPS password for use, since the ability to retrieve this password grants local administrative access to that device. The ability to read the LAPS password is controlled via the ‘ms-Mcs-AdmPwd’ attribute and should be audited to ensure access is only granted to users that require it.

\\n

\\n

**Excessive Privilege via Built-In Groups**

\\n

During incident response, companies often have alerting and monitoring in place for changes to groups like Domain and Enterprise Admins. These groups are widely known to hold the highest level of privilege in Active Directory. However, there are other privileged built-in groups that are attractive to threat actors and are often not held to the same level of scrutiny. Groups such as Account and Server Operators have wide ranging privilege over your Active Directory. For example, by default Server Operators can log on to Domain Controllers, restart services, backup and restore files, and more.

\\n

\\n

**Recommendation**

\\n

It is recommended that, where possible, privileged built-in groups not contain any users. Instead, the appropriate privilege should be granted specifically to users that require it. Additionally, Microsoft Incident Response recommends reviewing the current membership of those [groups](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory#table-b-1-built-in-and-default-accounts-and-groups-in-active-directory\%22) and adding additional alerting to changes to them in the same way you would alert on Domain or Enterprise admin changes.

\\n

\\n

**Privilege Escalation**

\\n

**Access Control List Abuse**

\\n

Access Control Lists (ACL) misconfiguration is one of the most common issues Microsoft Incident Response finds in Active Directory environments. Active Directory ACLs are exceptionally granular, complex, and easy to configure incorrectly. It is easy to reduce the security posture of your Active Directory environment without having any operational impact on your users. As ACLs are configured in your environment through business-as-usual activities, attack paths start to form. These attack paths create an escalation path from a low privileged user to total domain control. A threat actor can take advantage of the paths created by the combination of excessive privilege and scope on ACLs. A threat actor can take advantage of the paths created by the combination of excessive privilege and scope on ACLs.

\\n

\\n

Two common ACLs that Microsoft Incident Response sees regularly in Active Directory are:

\\n

\\n- GenericAll – this privilege is the same as Full Control access. If a user was compromised and that user had GenericAll over a highly privileged group, then the threat actor could add additional members to that group.
\\n- WriteDacl – this privilege allows manipulation of the ACL on an object. With this privilege a threat actor can change the ACL on an object such as a group. If a user was compromised and that user had WriteDacl over a highly privileged group, the threat actor could add a new ACL to that group. That new ACL could then give them access to add additional members to the group, such as themselves.
\\n

\\n

These permissions are often set at the top of the Active Directory hierarchy. They are also often applied to users and groups that do not require those permissions, effectively granting those group members full domain control. The members of these groups are very rarely secured in the same way that Domain and Enterprise Admins are.

\\n

\\n

In addition, Microsoft Incident Response often detects insecure ACLs on the [AdminSdHolder](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/appendix-c--protected-accounts-and-groups-in-active-directory#adminsdholder\%22) object, which is responsible for managing permissions on protected users and groups. If an adversary can manipulate the ACL on AdminSdHolder, it will be propagated on to those protected users and groups when the SDProp process runs. The adversary will then have rights to change membership of protected groups such as Domain Admins, allowing them to add themselves. The documentation for [BloodHound](https://techcommunity.microsoft.com/%22https://bloodhound.readthedocs.io/en/latest/data-analysis/edges.html/%22) describes these and several other ACL ‘edges’ that can be abused for privilege escalation.

\\n

\\n

**Recommendation**

\\n

Microsoft Incident Response recommends auditing permissions through your Active Directory environment using tools such as Defender for Identity and running sanctioned audits of attack paths using BloodHound and remediating paths that can lead to domain compromise.

\\n

\\n

**Escalation via Exchange Permissions**

\\n

Prior to the use of corporate cloud email services such as Office 365, customers ran their own on-premises Exchange environments. Many customers still maintain a complete on-premises Exchange environment. On-premises Exchange and Active Directory have always been tied closely together, with Exchange maintaining high privilege through Active Directory. Even in environments that have migrated user mailboxes to Office 365, an on-premises Exchange footprint often remains. It may exist to manage users not yet migrated, for legacy applications that are not able to integrate with Office 365, or to service non-internet connected workloads.

\\n

\\n

These on-premises Exchange environments often retain high privilege through Active Directory, and groups such as ‘Exchange Trusted Subsystem’ and ‘Exchange Servers’ can have a direct path to total domain control.

\\n

\\n

On-premises Exchange is also often internet-facing to allow users to access resources such as Outlook Web Access. Like any internet facing service, this increases the surface area for attack. If a threat actor can obtain SYSTEM privilege on an Exchange server and Exchange still retains excessive permissions in Active Directory, then it can lead to complete domain compromise.

\\n

\\n

**Recommendation**

\\n

It is possible to decouple the privilege held by Exchange in Active Directory by deploying the [split permissions model for Exchange](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/exchange/permissions/split-permissions/configure-exchange-for-split-permissions?view=exchserver-2019\%22). By deploying this model, permissions for Active Directory and Exchange are separated.

\\n

\\n

After deploying the Exchange split permissions model, there are [operational changes](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/exchange/permissions/split-permissions/split-permissions?view=exchserver-2019\%22) required by staff who administer both Exchange and Active Directory. If you don’t want to deploy the entire split permissions model, you can still reduce the permissions Exchange has in Active Directory by implementing the changes in the following Microsoft [guidance](https://techcommunity.microsoft.com/%22https://support.microsoft.com/en-us/topic/reducing-permissions-required-to-run-exchange-server-when-you-use-the-shared-permissions-model-e1972d47-d714-fd76-1fd5-7cdcb85408ed/%22).

\\n

\\n

If you have completely migrated to Office 365 but maintain on-premises Exchange servers for ease of management, you may now be able to [turn off those on-premises servers](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/exchange/manage-hybrid-exchange-recipients-with-management-tools/%22).

\\n

\\n

**Group Policy ACL Abuse**

\\n

Group Policy is often a tool used by threat actors to establish persistence (via the creation of scheduled tasks), create additional accounts, or deploy malware. It is also used as a ransomware deployment mechanism. If a threat actor has not yet compromised a Domain Admin, they may have been able to compromise an account that maintains permissions over Group Policy Objects. For instance, the ability to create, update, or even link policies may have been delegated to other groups.

\\n

\\n

If an existing Group Policy is configured to run a startup script, a threat actor can change the path of that script to then have it execute a malicious payload. If a group policy exists to disable endpoint security tooling as an exemption, a threat actor could leverage the permissions to link policy by applying that policy to all devices in the environment. This would not require the threat actor to update the policy, just change the scope of it.  Additionally, regular users can be given additional privileges via [User Rights Assignments](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/user-rights-assignment/%22). These privileges are often not required by the users and are granted accidentally.

\\n

\\n

**Recommendation**

\\n

The ability to manipulate Group Policy is a highly privileged action and users and groups with delegated responsibility to manage it should be held to the same standards as Domain Admins or similar. Ensure that permissions to create, update, and link group policies are in line with least privilege principles.

\\n

\\n

In large and complex environments, the number of Group Policies in use can be overwhelming and it is not clear what policies apply to which users and devices. Using tools such as [Resultant Set of Policy](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn789183(v=ws.11)/%22) (RSoP), you can model your Group Policy objects to see the overall effect on your users and devices.

\\n

\\n

**Insecure Trust Configuration**

\\n

SID history is a capability in Active Directory to aid in domain migration. It allows Domain Admins to simplify migration by applying the SID history (in simple terms, a list of permissions) from the old account to the new account. This helps the user retain access to resources once they are migrated. An adversary can target this capability by inserting the SIDs of groups such as Domain Admins into the SID history of an account in the trusted forest and using that account to [take control of the trusting forest](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc755321(v=ws.10)?redirectedfrom=MSDN#how-sid-history-can-be-used-to-elevate-privileges\%22). This can be especially relevant during [mergers and acquisitions](https://techcommunity.microsoft.com/%22https://www.microsoft.com/en-us/security/blog/2022/11/02/microsoft-security-tips-for-mitigating-risk-in-mergers-and-acquisitions//%22), where trusts between Active Directory environments are configured to allow migrations.

\\n

\\n

**Recommendation**

\\n

Active Directory trusts should only be configured when absolutely required. If they are part of an acquisition or migration, then they should be decommissioned once migration is complete. For trusts that need to remain for operational reasons, [SID filtering](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc755321(v=ws.10)?redirectedfrom=MSDN#sid-filtering\%22) and [Selective Authentication](https://techcommunity.microsoft.com/%22https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc755321(v=ws.10)?redirectedfrom=MSDN#selective-authentication\%22) should be configured to reduce the attack path from other domains and forests.

\\n

\\n

**Compromise of other Tier 0 assets**

\\n

Historically, domain controllers have been at the center of Tier 0 infrastructure. While that is still true, Tier 0 has now expanded to include several interconnected systems. As ways of working have evolved, so has the underlying technology required to drive modern identity systems. In line with that, your Tier 0 footprint has also evolved and may now include systems such as:

\\n

\\n

\\n- Active Directory Federation Services
\\n- Azure Active Directory Connect
\\n- Active Directory Certificate Services
\\n

\\n

It also includes any other services or infrastructure, including 3rd party providers, that form part of your identity trust chain, such as privileged access management and identity governance systems.

\\n

\\n

\\n

\\n

_Figure 4: Example of how Tier 0 assets connect to an identity trust chain._

\\n

\\n

It is important that all systems that form part of your end-to-end identity chain are included in Tier 0, and the security controls you apply to domain controllers also apply to these systems. Due to the interconnected nature of these systems, compromise of any one of them could lead to complete domain compromise. Only Tier 0 accounts should retain local administrative privileges over these systems and, where practical, access to them should be via a privileged access workstation.

\\n

\\n

**Summary**

\\n

In large and complex environments, Microsoft Incident Response often sees combinations of the above issues that reduce identity security posture significantly. These misconfigurations allow threat actors to elevate from a single non privileged user all the way to your crown jewel Domain Admin accounts.

\\n

\\n

\\n

_Figure 5: Kill chain showing how domain compromise can start from a single compromised user._

\\n

\\n

For example, in the above kill chain, the first user was compromised due to a weak password policy. Through the initial poor password policy, additional bad credential hygiene, and ACL misconfiguration, the domain was compromised. When you multiply all the combinations of user accounts, group access, and permissions in Active Directory, many paths can exist to Domain Admin.

\\n

\\n

Attacks on Active Directory are ever evolving, and this blog covers only some of the more common issues Microsoft Incident Response observes in customer environments. Ultimately, any changes made to Active Directory can either increase or decrease the risk that a threat actor can take control of your environment. To ensure that risk is consistently decreasing, Microsoft Incident Response recommends a constant cycle of the below:

\\n

\\n

\\n- Reduce Privilege – assign all access according to the principle of least privilege. Additionally, deploy the enterprise access model to reduce privileged credential exposure. Combined, these will reduce the likelihood that a single device or user compromise leads to total domain compromise.
\\n- Audit Current Posture – use tools such as Defender for Identity and sanctioned use of BloodHound and PingCastle to audit your current Active Directory security posture and remediate the issues both surfaced through those tools and described in this blog.
\\n- Monitor Changes – monitor for changes to your Active Directory environment that can reduce your security posture or expose additional attack paths to domain compromise.

\\n- Actively Detect – alert on potential signs of compromise using Defender for Identity or custom detection rules.

\\n

\\n

A message that Microsoft Incident Response often leaves customers with is that securing Active Directory requires continued governance. You can’t ‘deploy’ Active Directory security and never have to look at it again. Active Directory security is about constant improvement and ensuring those misconfigurations and attack paths are mitigated before an adversary finds them.

\\n

","kudosSumWeight":18,"postTime":"2023-02-28T13:22:43.717-08:00","images":{"\_\_typename":"AssociatedImageConnection","edges":\[{"\_\_typename":"AssociatedImageEdge","cursor":"MjUuOHwyLjF8b3wyNXxfTlZffDE","node":{"\_\_ref":"AssociatedImage:{\\"url\\":\\"https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNzUzMzkxLTQ0NTYwOWlCRTJGQzIzNEE0MTQ3NTk5?revision=5\\"}"}},{"\_\_typename":"AssociatedImageEdge","cursor":"MjUuOHwyLjF8b3wyNXxfTlZffDI","node":{"\_\_ref":"AssociatedImage:{\\"url\\":\\"https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNzUzMzkxLTQ0NTYxMGk4NTVCODQ3Mzg0ODZERDJC?revision=5\\"}"}},{"\_\_typename":"AssociatedImageEdge","cursor":"MjUuOHwyLjF8b3wyNXxfTlZffDM","node":{"\_\_ref":"AssociatedImage:{\\"url\\":\\"https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNzUzMzkxLTQ0NTkzM2lGNjk1MzgyN0E0NzM2QkRC?revision=5\\"}"}},{"\_\_typename":"AssociatedImageEdge","cursor":"MjUuOHwyLjF8b3wyNXxfTlZffDQ","node":{"\_\_ref":"AssociatedImage:{\\"url\\":\\"https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNzUzMzkxLTQ0NTYxNmlDNEI4MDVDODREMTk5QjY0?revision=5\\"}"}},{"\_\_typename":"AssociatedImageEdge","cursor":"MjUuOHwyLjF8b3wyNXxfTlZffDU","node":{"\_\_ref":"AssociatedImage:{\\"url\\":\\"https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNzUzMzkxLTQ0NTkzMmlDOERGQzEyQ0JGQjEyRkY3?revision=5\\"}"}}\],"totalCount":5,"pageInfo":{"\_\_typename":"PageInfo","hasNextPage":false,"endCursor":null,"hasPreviousPage":false,"startCursor":null}},"attachments":{"\_\_typename":"AttachmentConnection","pageInfo":{"\_\_typename":"PageInfo","hasNextPage":false,"endCursor":null,"hasPreviousPage":false,"startCursor":null},"edges":\[\]},"tags":{"\_\_typename":"TagConnection","pageInfo":{"\_\_typename":"PageInfo","hasNextPage":false,"endCursor":null,"hasPreviousPage":false,"startCursor":null},"edges":\[{"\_\_typename":"TagEdge","cursor":"MjUuOHwyLjF8b3wxMHxfTlZffDE","node":{"\_\_typename":"Tag","id":"tag:microsoft detection and response team (dart)","text":"microsoft detection and response team (dart)","time":"2022-01-04T09:00:00.029-08:00","lastActivityTime":null,"messagesCount":null,"followersCount":null}}\]},"timeToRead":18,"rawTeaser":"","introduction":"","coverImage":null,"coverImageProperties":{"\_\_typename":"CoverImageProperties","style":"STANDARD","titlePosition":"BOTTOM","altText":""},"currentRevision":{"\_\_ref":"Revision:revision:3753391\_5"},"latestVersion":{"\_\_typename":"FriendlyVersion","major":"4","minor":"0"},"metrics":{"\_\_typename":"MessageMetrics","views":82145},"read":false,"visibilityScope":"PUBLIC","canonicalUrl":null,"seoTitle":null,"seoDescription":null,"placeholder":false,"originalMessageForPlaceholder":null,"contributors":{"\_\_typename":"UserConnection","edges":\[\]},"nonCoAuthorContributors":{"\_\_typename":"UserConnection","edges":\[\]},"coAuthors":{"\_\_typename":"UserConnection","edges":\[\]},"blogMessagePolicies":{"\_\_typename":"BlogMessagePolicies","canDoAuthoringActionsOnBlog":{"\_\_typename":"PolicyResult","failureReason":{"\_\_typename":"FailureReason","message":"error.lithium.policies.blog.action\_can\_do\_authoring\_action.accessDenied","key":"error.lithium.policies.blog.action\_can\_do\_authoring\_action.accessDenied","args":\[\]}}},"archivalData":null,"customFields":\[\],"revisions({\\"constraints\\":{\\"isPublished\\":{\\"eq\\":true}}})":{"\_\_typename":"RevisionConnection","totalCount":5}},"Conversation:conversation:3753391":{"\_\_typename":"Conversation","id":"conversation:3753391","solved":false,"topic":{"\_\_ref":"BlogTopicMessage:message:3753391"},"lastPostingActivityTime":"2025-03-05T16:33:05.788-08:00","lastPostTime":"2025-03-05T16:33:05.788-08:00","unreadReplyCount":6,"isSubscribed":false},"ModerationData:moderation\_data:3753391":{"\_\_typename":"ModerationData","id":"moderation\_data:3753391","status":"APPROVED","rejectReason":null,"isReportedAbuse":false,"rejectUser":null,"rejectTime":null,"rejectActorType":null},"AssociatedImage:{\\"url\\":\\"https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNzUzMzkxLTQ0NTYwOWlCRTJGQzIzNEE0MTQ3NTk5?revision=5\\"}":{"\_\_typename":"AssociatedImage","url":"https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNzUzMzkxLTQ0NTYwOWlCRTJGQzIzNEE0MTQ3NTk5?revision=5","title":"mzorich\_5-1677476139108.png","associationType":"BODY","width":984,"height":541,"altText":null},"AssociatedImage:{\\"url\\":\\"https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNzUzMzkxLTQ0NTYxMGk4NTVCODQ3Mzg0ODZERDJC?revision=5\\"}":{"\_\_typename":"AssociatedImage","url":"https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNzUzMzkxLTQ0NTYxMGk4NTVCODQ3Mzg0ODZERDJC?revision=5","title":"mzorich\_6-1677476230313.png","associationType":"BODY","width":984,"height":779,"altText":null},"AssociatedImage:{\\"url\\":\\"https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNzUzMzkxLTQ0NTkzM2lGNjk1MzgyN0E0NzM2QkRC?revision=5\\"}":{"\_\_typename":"AssociatedImage","url":"https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNzUzMzkxLTQ0NTkzM2lGNjk1MzgyN0E0NzM2QkRC?revision=5","title":"mzorich\_1-1677549966901.png","associationType":"BODY","width":2382,"height":1119,"altText":null},"AssociatedImage:{\\"url\\":\\"https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNzUzMzkxLTQ0NTYxNmlDNEI4MDVDODREMTk5QjY0?revision=5\\"}":{"\_\_typename":"AssociatedImage","url":"https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNzUzMzkxLTQ0NTYxNmlDNEI4MDVDODREMTk5QjY0?revision=5","title":"mzorich\_12-1677477076646.png","associationType":"BODY","width":980,"height":609,"altText":null},"AssociatedImage:{\\"url\\":\\"https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNzUzMzkxLTQ0NTkzMmlDOERGQzEyQ0JGQjEyRkY3?revision=5\\"}":{"\_\_typename":"AssociatedImage","url":"https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNzUzMzkxLTQ0NTkzMmlDOERGQzEyQ0JGQjEyRkY3?revision=5","title":"mzorich\_0-1677549706251.png","associationType":"BODY","width":2588,"height":659,"altText":null},"Revision:revision:3753391\_5":{"\_\_typename":"Revision","id":"revision:3753391\_5","lastEditTime":"2023-05-22T13:37:11.901-07:00"},"CachedAsset:theme:customTheme1-1758304527221":{"\_\_typename":"CachedAsset","id":"theme:customTheme1-1758304527221","value":{"id":"customTheme1","animation":{"fast":"150ms","normal":"250ms","slow":"500ms","slowest":"750ms","function":"cubic-bezier(0.07, 0.91, 0.51, 1)","\_\_typename":"AnimationThemeSettings"},"avatar":{"borderRadius":"50%","collections":\["default"\],"\_\_typename":"AvatarThemeSettings"},"basics":{"browserIcon":{"imageAssetName":"favicon-1730836283320.png","imageLastModified":"1730836286415","\_\_typename":"ThemeAsset"},"customerLogo":{"imageAssetName":"favicon-1730836271365.png","imageLastModified":"1730836274203","\_\_typename":"ThemeAsset"},"maximumWidthOfPageContent":"1300px","oneColumnNarrowWidth":"1200px","gridGutterWidthMd":"30px","gridGutterWidthXs":"10px","pageWidthStyle":"WIDTH\_OF\_BROWSER","\_\_typename":"BasicsThemeSettings"},"buttons":{"borderRadiusSm":"3px","borderRadius":"3px","borderRadiusLg":"5px","paddingY":"5px","paddingYLg":"7px","paddingYHero":"var(--lia-bs-btn-padding-y-lg)","paddingX":"12px","paddingXLg":"16px","paddingXHero":"60px","fontStyle":"NORMAL","fontWeight":"700","textTransform":"NONE","disabledOpacity":0.5,"primaryTextColor":"var(--lia-bs-white)","primaryTextHoverColor":"var(--lia-bs-white)","primaryTextActiveColor":"var(--lia-bs-white)","primaryBgColor":"var(--lia-bs-primary)","primaryBgHoverColor":"hsl(var(--lia-bs-primary-h), var(--lia-bs-primary-s), calc(var(--lia-bs-primary-l) \* 0.85))","primaryBgActiveColor":"hsl(var(--lia-bs-primary-h), var(--lia-bs-primary-s), calc(var(--lia-bs-primary-l) \* 0.7))","primaryBorder":"1px solid transparent","primaryBorderHover":"1px solid transparent","primaryBorderActive":"1px solid transparent","primaryBorderFocus":"1px solid var(--lia-bs-white)","primaryBoxShadowFocus":"0 0 0 1px var(--lia-bs-primary), 0 0 0 4px hsla(var(--lia-bs-primary-h), var(--lia-bs-primary-s), var(--lia-bs-primary-l), 0.2)","secondaryTextColor":"var(--lia-bs-gray-900)","secondaryTextHoverColor":"hsl(var(--lia-bs-gray-900-h), var(--lia-bs-gray-900-s), calc(var(--lia-bs-gray-900-l) \* 0.95))","secondaryTextActiveColor":"hsl(var(--lia-bs-gray-900-h), var(--lia-bs-gray-900-s), calc(var(--lia-bs-gray-900-l) \* 0.9))","secondaryBgColor":"var(--lia-bs-gray-200)","secondaryBgHoverColor":"hsl(var(--lia-bs-gray-200-h), var(--lia-bs-gray-200-s), calc(var(--lia-bs-gray-200-l) \* 0.96))","secondaryBgActiveColor":"hsl(var(--lia-bs-gray-200-h), var(--lia-bs-gray-200-s), calc(var(--lia-bs-gray-200-l) \* 0.92))","secondaryBorder":"1px solid transparent","secondaryBorderHover":"1px solid transparent","secondaryBorderActive":"1px solid transparent","secondaryBorderFocus":"1px solid transparent","secondaryBoxShadowFocus":"0 0 0 1px var(--lia-bs-primary), 0 0 0 4px hsla(var(--lia-bs-primary-h), var(--lia-bs-primary-s), var(--lia-bs-primary-l), 0.2)","tertiaryTextColor":"var(--lia-bs-gray-900)","tertiaryTextHoverColor":"hsl(var(--lia-bs-gray-900-h), var(--lia-bs-gray-900-s), calc(var(--lia-bs-gray-900-l) \* 0.95))","tertiaryTextActiveColor":"hsl(var(--lia-bs-gray-900-h), var(--lia-bs-gray-900-s), calc(var(--lia-bs-gray-900-l) \* 0.9))","tertiaryBgColor":"transparent","tertiaryBgHoverColor":"transparent","tertiaryBgActiveColor":"hsla(var(--lia-bs-black-h), var(--lia-bs-black-s), var(--lia-bs-black-l), 0.04)","tertiaryBorder":"1px solid transparent","tertiaryBorderHover":"1px solid hsla(var(--lia-bs-black-h), var(--lia-bs-black-s), var(--lia-bs-black-l), 0.08)","tertiaryBorderActive":"1px solid transparent","tertiaryBorderFocus":"1px solid transparent","tertiaryBoxShadowFocus":"0 0 0 1px var(--lia-bs-primary), 0 0 0 4px hsla(var(--lia-bs-primary-h), var(--lia-bs-primary-s), var(--lia-bs-primary-l), 0.2)","destructiveTextColor":"var(--lia-bs-danger)","destructiveTextHoverColor":"hsl(var(--lia-bs-danger-h), var(--lia-bs-danger-s), calc(var(--lia-bs-danger-l) \* 0.95))","destructiveTextActiveColor":"hsl(var(--lia-bs-danger-h), var(--lia-bs-danger-s), calc(var(--lia-bs-danger-l) \* 0.9))","destructiveBgColor":"var(--lia-bs-gray-200)","destructiveBgHoverColor":"hsl(var(--lia-bs-gray-200-h), var(--lia-bs-gray-200-s), calc(var(--lia-bs-gray-200-l) \* 0.96))","destructiveBgActiveColor":"hsl(var(--lia-bs-gray-200-h), var(--lia-bs-gray-200-s), calc(var(--lia-bs-gray-200-l) \* 0.92))","destructiveBorder":"1px solid transparent","destructiveBorderHover":"1px solid transparent","destructiveBorderActive":"1px solid transparent","destructiveBorderFocus":"1px solid transparent","destructiveBoxShadowFocus":"0 0 0 1px var(--lia-bs-primary), 0 0 0 4px hsla(var(--lia-bs-primary-h), var(--lia-bs-primary-s), var(--lia-bs-primary-l), 0.2)","\_\_typename":"ButtonsThemeSettings"},"border":{"color":"hsla(var(--lia-bs-black-h), var(--lia-bs-black-s), var(--lia-bs-black-l), 0.08)","mainContent":"NONE","sideContent":"LIGHT","radiusSm":"3px","radius":"5px","radiusLg":"9px","radius50":"100vw","\_\_typename":"BorderThemeSettings"},"boxShadow":{"xs":"0 0 0 1px hsla(var(--lia-bs-gray-900-h), var(--lia-bs-gray-900-s), var(--lia-bs-gray-900-l), 0.08), 0 3px 0 -1px hsla(var(--lia-bs-gray-900-h), var(--lia-bs-gray-900-s), var(--lia-bs-gray-900-l), 0.16)","sm":"0 2px 4px hsla(var(--lia-bs-gray-900-h), var(--lia-bs-gray-900-s), var(--lia-bs-gray-900-l), 0.12)","md":"0 5px 15px hsla(var(--lia-bs-gray-900-h), var(--lia-bs-gray-900-s), var(--lia-bs-gray-900-l), 0.3)","lg":"0 10px 30px hsla(var(--lia-bs-gray-900-h), var(--lia-bs-gray-900-s), var(--lia-bs-gray-900-l), 0.3)","\_\_typename":"BoxShadowThemeSettings"},"cards":{"bgColor":"var(--lia-panel-bg-color)","borderRadius":"var(--lia-panel-border-radius)","boxShadow":"var(--lia-box-shadow-xs)","\_\_typename":"CardsThemeSettings"},"chip":{"maxWidth":"300px","height":"30px","\_\_typename":"ChipThemeSettings"},"coreTypes":{"defaultMessageLinkColor":"var(--lia-bs-link-color)","defaultMessageLinkDecoration":"none","defaultMessageLinkFontStyle":"NORMAL","defaultMessageLinkFontWeight":"400","defaultMessageFontStyle":"NORMAL","defaultMessageFontWeight":"400","defaultMessageFontFamily":"var(--lia-bs-font-family-base)","forumColor":"#4099E2","forumFontFamily":"var(--lia-bs-font-family-base)","forumFontWeight":"var(--lia-default-message-font-weight)","forumLineHeight":"var(--lia-bs-line-height-base)","forumFontStyle":"var(--lia-default-message-font-style)","forumMessageLinkColor":"var(--lia-default-message-link-color)","forumMessageLinkDecoration":"var(--lia-default-message-link-decoration)","forumMessageLinkFontStyle":"var(--lia-default-message-link-font-style)","forumMessageLinkFontWeight":"var(--lia-default-message-link-font-weight)","forumSolvedColor":"#148563","blogColor":"#1CBAA0","blogFontFamily":"var(--lia-bs-font-family-base)","blogFontWeight":"var(--lia-default-message-font-weight)","blogLineHeight":"1.75","blogFontStyle":"var(--lia-default-message-font-style)","blogMessageLinkColor":"var(--lia-default-message-link-color)","blogMessageLinkDecoration":"var(--lia-default-message-link-decoration)","blogMessageLinkFontStyle":"var(--lia-default-message-link-font-style)","blogMessageLinkFontWeight":"var(--lia-default-message-link-font-weight)","tkbColor":"#4C6B90","tkbFontFamily":"var(--lia-bs-font-family-base)","tkbFontWeight":"var(--lia-default-message-font-weight)","tkbLineHeight":"1.75","tkbFontStyle":"var(--lia-default-message-font-style)","tkbMessageLinkColor":"var(--lia-default-message-link-color)","tkbMessageLinkDecoration":"var(--lia-default-message-link-decoration)","tkbMessageLinkFontStyle":"var(--lia-default-message-link-font-style)","tkbMessageLinkFontWeight":"var(--lia-default-message-link-font-weight)","qandaColor":"#4099E2","qandaFontFamily":"var(--lia-bs-font-family-base)","qandaFontWeight":"var(--lia-default-message-font-weight)","qandaLineHeight":"var(--lia-bs-line-height-base)","qandaFontStyle":"var(--lia-default-message-link-font-style)","qandaMessageLinkColor":"var(--lia-default-message-link-color)","qandaMessageLinkDecoration":"var(--lia-default-message-link-decoration)","qandaMessageLinkFontStyle":"var(--lia-default-message-link-font-style)","qandaMessageLinkFontWeight":"var(--lia-default-message-link-font-weight)","qandaSolvedColor":"#3FA023","ideaColor":"#FF8000","ideaFontFamily":"var(--lia-bs-font-family-base)","ideaFontWeight":"var(--lia-default-message-font-weight)","ideaLineHeight":"var(--lia-bs-line-height-base)","ideaFontStyle":"var(--lia-default-message-font-style)","ideaMessageLinkColor":"var(--lia-default-message-link-color)","ideaMessageLinkDecoration":"var(--lia-default-message-link-decoration)","ideaMessageLinkFontStyle":"var(--lia-default-message-link-font-style)","ideaMessageLinkFontWeight":"var(--lia-default-message-link-font-weight)","contestColor":"#FCC845","contestFontFamily":"var(--lia-bs-font-family-base)","contestFontWeight":"var(--lia-default-message-font-weight)","contestLineHeight":"var(--lia-bs-line-height-base)","contestFontStyle":"var(--lia-default-message-link-font-style)","contestMessageLinkColor":"var(--lia-default-message-link-color)","contestMessageLinkDecoration":"var(--lia-default-message-link-decoration)","contestMessageLinkFontStyle":"ITALIC","contestMessageLinkFontWeight":"var(--lia-default-message-link-font-weight)","occasionColor":"#D13A1F","occasionFontFamily":"var(--lia-bs-font-family-base)","occasionFontWeight":"var(--lia-default-message-font-weight)","occasionLineHeight":"var(--lia-bs-line-height-base)","occasionFontStyle":"var(--lia-default-message-font-style)","occasionMessageLinkColor":"var(--lia-default-message-link-color)","occasionMessageLinkDecoration":"var(--lia-default-message-link-decoration)","occasionMessageLinkFontStyle":"var(--lia-default-message-link-font-style)","occasionMessageLinkFontWeight":"var(--lia-default-message-link-font-weight)","grouphubColor":"#333333","categoryColor":"#949494","communityColor":"#FFFFFF","productColor":"#949494","\_\_typename":"CoreTypesThemeSettings"},"colors":{"black":"#000000","white":"#FFFFFF","gray100":"#F7F7F7","gray200":"#F7F7F7","gray300":"#E8E8E8","gray400":"#D9D9D9","gray500":"#CCCCCC","gray600":"#717171","gray700":"#707070","gray800":"#545454","gray900":"#333333","dark":"#545454","light":"#F7F7F7","primary":"#0069D4","secondary":"#333333","bodyText":"#1E1E1E","bodyBg":"#FFFFFF","info":"#409AE2","success":"#41C5AE","warning":"#FCC844","danger":"#BC341B","alertSystem":"#FF6600","textMuted":"#707070","highlight":"#FFFCAD","outline":"var(--lia-bs-primary)","custom":\["#D3F5A4","#243A5E"\],"\_\_typename":"ColorsThemeSettings"},"divider":{"size":"3px","marginLeft":"4px","marginRight":"4px","borderRadius":"50%","bgColor":"var(--lia-bs-gray-600)","bgColorActive":"var(--lia-bs-gray-600)","\_\_typename":"DividerThemeSettings"},"dropdown":{"fontSize":"var(--lia-bs-font-size-sm)","borderColor":"var(--lia-bs-border-color)","borderRadius":"var(--lia-bs-border-radius-sm)","dividerBg":"var(--lia-bs-gray-300)","itemPaddingY":"5px","itemPaddingX":"20px","headerColor":"var(--lia-bs-gray-700)","\_\_typename":"DropdownThemeSettings"},"email":{"link":{"color":"#0069D4","hoverColor":"#0061c2","decoration":"none","hoverDecoration":"underline","\_\_typename":"EmailLinkSettings"},"border":{"color":"#e4e4e4","\_\_typename":"EmailBorderSettings"},"buttons":{"borderRadiusLg":"5px","paddingXLg":"16px","paddingYLg":"7px","fontWeight":"700","primaryTextColor":"#ffffff","primaryTextHoverColor":"#ffffff","primaryBgColor":"#0069D4","primaryBgHoverColor":"#005cb8","primaryBorder":"1px solid transparent","primaryBorderHover":"1px solid transparent","\_\_typename":"EmailButtonsSettings"},"panel":{"borderRadius":"5px","borderColor":"#e4e4e4","\_\_typename":"EmailPanelSettings"},"\_\_typename":"EmailThemeSettings"},"emoji":{"skinToneDefault":"#ffcd43","skinToneLight":"#fae3c5","skinToneMediumLight":"#e2cfa5","skinToneMedium":"#daa478","skinToneMediumDark":"#a78058","skinToneDark":"#5e4d43","\_\_typename":"EmojiThemeSettings"},"heading":{"color":"var(--lia-bs-body-color)","fontFamily":"Segoe UI","fontStyle":"NORMAL","fontWeight":"400","h1FontSize":"34px","h2FontSize":"32px","h3FontSize":"28px","h4FontSize":"24px","h5FontSize":"20px","h6FontSize":"16px","lineHeight":"1.3","subHeaderFontSize":"11px","subHeaderFontWeight":"500","h1LetterSpacing":"normal","h2LetterSpacing":"normal","h3LetterSpacing":"normal","h4LetterSpacing":"normal","h5LetterSpacing":"normal","h6LetterSpacing":"normal","subHeaderLetterSpacing":"2px","h1FontWeight":"var(--lia-bs-headings-font-weight)","h2FontWeight":"var(--lia-bs-headings-font-weight)","h3FontWeight":"var(--lia-bs-headings-font-weight)","h4FontWeight":"var(--lia-bs-headings-font-weight)","h5FontWeight":"var(--lia-bs-headings-font-weight)","h6FontWeight":"var(--lia-bs-headings-font-weight)","\_\_typename":"HeadingThemeSettings"},"icons":{"size10":"10px","size12":"12px","size14":"14px","size16":"16px","size20":"20px","size24":"24px","size30":"30px","size40":"40px","size50":"50px","size60":"60px","size80":"80px","size120":"120px","size160":"160px","\_\_typename":"IconsThemeSettings"},"imagePreview":{"bgColor":"var(--lia-bs-gray-900)","titleColor":"var(--lia-bs-white)","controlColor":"var(--lia-bs-white)","controlBgColor":"var(--lia-bs-gray-800)","\_\_typename":"ImagePreviewThemeSettings"},"input":{"borderColor":"var(--lia-bs-gray-600)","disabledColor":"var(--lia-bs-gray-600)","focusBorderColor":"var(--lia-bs-primary)","labelMarginBottom":"10px","btnFontSize":"var(--lia-bs-font-size-sm)","focusBoxShadow":"0 0 0 3px hsla(var(--lia-bs-primary-h), var(--lia-bs-primary-s), var(--lia-bs-primary-l), 0.2)","checkLabelMarginBottom":"2px","checkboxBorderRadius":"3px","borderRadiusSm":"var(--lia-bs-border-radius-sm)","borderRadius":"var(--lia-bs-border-radius)","borderRadiusLg":"var(--lia-bs-border-radius-lg)","formTextMarginTop":"4px","textAreaBorderRadius":"var(--lia-bs-border-radius)","activeFillColor":"var(--lia-bs-primary)","\_\_typename":"InputThemeSettings"},"loading":{"dotDarkColor":"hsla(var(--lia-bs-black-h), var(--lia-bs-black-s), var(--lia-bs-black-l), 0.2)","dotLightColor":"hsla(var(--lia-bs-white-h), var(--lia-bs-white-s), var(--lia-bs-white-l), 0.5)","barDarkColor":"hsla(var(--lia-bs-black-h), var(--lia-bs-black-s), var(--lia-bs-black-l), 0.06)","barLightColor":"hsla(var(--lia-bs-white-h), var(--lia-bs-white-s), var(--lia-bs-white-l), 0.4)","\_\_typename":"LoadingThemeSettings"},"link":{"color":"var(--lia-bs-primary)","hoverColor":"hsl(var(--lia-bs-primary-h), var(--lia-bs-primary-s), calc(var(--lia-bs-primary-l) - 10%))","decoration":"none","hoverDecoration":"underline","\_\_typename":"LinkThemeSettings"},"listGroup":{"itemPaddingY":"15px","itemPaddingX":"15px","borderColor":"var(--lia-bs-gray-300)","\_\_typename":"ListGroupThemeSettings"},"modal":{"contentTextColor":"var(--lia-bs-body-color)","contentBg":"var(--lia-bs-white)","backgroundBg":"var(--lia-bs-black)","smSize":"440px","mdSize":"760px","lgSize":"1080px","backdropOpacity":0.3,"contentBoxShadowXs":"var(--lia-bs-box-shadow-sm)","contentBoxShadow":"var(--lia-bs-box-shadow)","headerFontWeight":"700","\_\_typename":"ModalThemeSettings"},"navbar":{"position":"FIXED","background":{"attachment":null,"clip":null,"color":"var(--lia-bs-white)","imageAssetName":"","imageLastModified":"0","origin":null,"position":"CENTER\_CENTER","repeat":"NO\_REPEAT","size":"COVER","\_\_typename":"BackgroundProps"},"backgroundOpacity":0.8,"paddingTop":"15px","paddingBottom":"15px","borderBottom":"1px solid var(--lia-bs-border-color)","boxShadow":"var(--lia-bs-box-shadow-sm)","brandMarginRight":"30px","brandMarginRightSm":"10px","brandLogoHeight":"30px","linkGap":"10px","linkJustifyContent":"flex-start","linkPaddingY":"5px","linkPaddingX":"10px","linkDropdownPaddingY":"9px","linkDropdownPaddingX":"var(--lia-nav-link-px)","linkColor":"var(--lia-bs-body-color)","linkHoverColor":"var(--lia-bs-primary)","linkFontSize":"var(--lia-bs-font-size-sm)","linkFontStyle":"NORMAL","linkFontWeight":"400","linkTextTransform":"NONE","linkLetterSpacing":"normal","linkBorderRadius":"var(--lia-bs-border-radius-sm)","linkBgColor":"transparent","linkBgHoverColor":"transparent","linkBorder":"none","linkBorderHover":"none","linkBoxShadow":"none","linkBoxShadowHover":"none","linkTextBorderBottom":"none","linkTextBorderBottomHover":"none","dropdownPaddingTop":"10px","dropdownPaddingBottom":"15px","dropdownPaddingX":"10px","dropdownMenuOffset":"2px","dropdownDividerMarginTop":"10px","dropdownDividerMarginBottom":"10px","dropdownBorderColor":"hsla(var(--lia-bs-black-h), var(--lia-bs-black-s), var(--lia-bs-black-l), 0.08)","controllerBgHoverColor":"hsla(var(--lia-bs-black-h), var(--lia-bs-black-s), var(--lia-bs-black-l), 0.1)","controllerIconColor":"var(--lia-bs-body-color)","controllerIconHoverColor":"var(--lia-bs-body-color)","controllerTextColor":"var(--lia-nav-controller-icon-color)","controllerTextHoverColor":"var(--lia-nav-controller-icon-hover-color)","controllerHighlightColor":"hsla(30, 100%, 50%)","controllerHighlightTextColor":"var(--lia-yiq-light)","controllerBorderRadius":"var(--lia-border-radius-50)","hamburgerColor":"var(--lia-nav-controller-icon-color)","hamburgerHoverColor":"var(--lia-nav-controller-icon-color)","hamburgerBgColor":"transparent","hamburgerBgHoverColor":"transparent","hamburgerBorder":"none","hamburgerBorderHover":"none","collapseMenuMarginLeft":"20px","collapseMenuDividerBg":"var(--lia-nav-link-color)","collapseMenuDividerOpacity":0.16,"\_\_typename":"NavbarThemeSettings"},"pager":{"textColor":"var(--lia-bs-link-color)","textFontWeight":"var(--lia-font-weight-md)","textFontSize":"var(--lia-bs-font-size-sm)","\_\_typename":"PagerThemeSettings"},"panel":{"bgColor":"var(--lia-bs-white)","borderRadius":"var(--lia-bs-border-radius)","borderColor":"var(--lia-bs-border-color)","boxShadow":"none","\_\_typename":"PanelThemeSettings"},"popover":{"arrowHeight":"8px","arrowWidth":"16px","maxWidth":"300px","minWidth":"100px","headerBg":"var(--lia-bs-white)","borderColor":"var(--lia-bs-border-color)","borderRadius":"var(--lia-bs-border-radius)","boxShadow":"0 0.5rem 1rem hsla(var(--lia-bs-black-h), var(--lia-bs-black-s), var(--lia-bs-black-l), 0.15)","\_\_typename":"PopoverThemeSettings"},"prism":{"color":"#000000","bgColor":"#f5f2f0","fontFamily":"var(--font-family-monospace)","fontSize":"var(--lia-bs-font-size-base)","fontWeightBold":"var(--lia-bs-font-weight-bold)","fontStyleItalic":"italic","tabSize":2,"highlightColor":"#b3d4fc","commentColor":"#62707e","punctuationColor":"#6f6f6f","namespaceOpacity":"0.7","propColor":"#990055","selectorColor":"#517a00","operatorColor":"#906736","operatorBgColor":"hsla(0, 0%, 100%, 0.5)","keywordColor":"#0076a9","functionColor":"#d3284b","variableColor":"#c14700","\_\_typename":"PrismThemeSettings"},"rte":{"bgColor":"var(--lia-bs-white)","borderRadius":"var(--lia-panel-border-radius)","boxShadow":" var(--lia-panel-box-shadow)","customColor1":"#bfedd2","customColor2":"#fbeeb8","customColor3":"#f8cac6","customColor4":"#eccafa","customColor5":"#c2e0f4","customColor6":"#2dc26b","customColor7":"#f1c40f","customColor8":"#e03e2d","customColor9":"#b96ad9","customColor10":"#3598db","customColor11":"#169179","customColor12":"#e67e23","customColor13":"#ba372a","customColor14":"#843fa1","customColor15":"#236fa1","customColor16":"#ecf0f1","customColor17":"#ced4d9","customColor18":"#95a5a6","customColor19":"#7e8c8d","customColor20":"#34495e","customColor21":"#000000","customColor22":"#ffffff","defaultMessageHeaderMarginTop":"40px","defaultMessageHeaderMarginBottom":"20px","defaultMessageItemMarginTop":"0","defaultMessageItemMarginBottom":"10px","diffAddedColor":"hsla(170, 53%, 51%, 0.4)","diffChangedColor":"hsla(43, 97%, 63%, 0.4)","diffNoneColor":"hsla(0, 0%, 80%, 0.4)","diffRemovedColor":"hsla(9, 74%, 47%, 0.4)","specialMessageHeaderMarginTop":"40px","specialMessageHeaderMarginBottom":"20px","specialMessageItemMarginTop":"0","specialMessageItemMarginBottom":"10px","tableBgColor":"transparent","tableBorderColor":"var(--lia-bs-gray-700)","tableBorderStyle":"solid","tableCellPaddingX":"5px","tableCellPaddingY":"5px","tableTextColor":"var(--lia-bs-body-color)","tableVerticalAlign":"middle","\_\_typename":"RteThemeSettings"},"tags":{"bgColor":"var(--lia-bs-gray-200)","bgHoverColor":"var(--lia-bs-gray-400)","borderRadius":"var(--lia-bs-border-radius-sm)","color":"var(--lia-bs-body-color)","hoverColor":"var(--lia-bs-body-color)","fontWeight":"var(--lia-font-weight-md)","fontSize":"var(--lia-font-size-xxs)","textTransform":"UPPERCASE","letterSpacing":"0.5px","\_\_typename":"TagsThemeSettings"},"toasts":{"borderRadius":"var(--lia-bs-border-radius)","paddingX":"12px","\_\_typename":"ToastsThemeSettings"},"typography":{"fontFamilyBase":"Segoe UI","fontStyleBase":"NORMAL","fontWeightBase":"400","fontWeightLight":"300","fontWeightNormal":"400","fontWeightMd":"500","fontWeightBold":"700","letterSpacingSm":"normal","letterSpacingXs":"normal","lineHeightBase":"1.5","fontSizeBase":"16px","fontSizeXxs":"11px","fontSizeXs":"12px","fontSizeSm":"14px","fontSizeLg":"20px","fontSizeXl":"24px","smallFontSize":"14px","customFonts":\[{"source":"SERVER","name":"Segoe UI","styles":\[{"style":"NORMAL","weight":"400","\_\_typename":"FontStyleData"},{"style":"NORMAL","weight":"300","\_\_typename":"FontStyleData"},{"style":"NORMAL","weight":"600","\_\_typename":"FontStyleData"},{"style":"NORMAL","weight":"700","\_\_typename":"FontStyleData"},{"style":"ITALIC","weight":"400","\_\_typename":"FontStyleData"}\],"assetNames":\["SegoeUI-normal-400.woff2","SegoeUI-normal-300.woff2","SegoeUI-normal-600.woff2","SegoeUI-normal-700.woff2","SegoeUI-italic-400.woff2"\],"\_\_typename":"CustomFont"},{"source":"SERVER","name":"MWF Fluent Icons","styles":\[{"style":"NORMAL","weight":"400","\_\_typename":"FontStyleData"}\],"assetNames":\["MWFFluentIcons-normal-400.woff2"\],"\_\_typename":"CustomFont"}\],"\_\_typename":"TypographyThemeSettings"},"unstyledListItem":{"marginBottomSm":"5px","marginBottomMd":"10px","marginBottomLg":"15px","marginBottomXl":"20px","marginBottomXxl":"25px","\_\_typename":"UnstyledListItemThemeSettings"},"yiq":{"light":"#ffffff","dark":"#000000","\_\_typename":"YiqThemeSettings"},"colorLightness":{"primaryDark":0.36,"primaryLight":0.74,"primaryLighter":0.89,"primaryLightest":0.95,"infoDark":0.39,"infoLight":0.72,"infoLighter":0.85,"infoLightest":0.93,"successDark":0.24,"successLight":0.62,"successLighter":0.8,"successLightest":0.91,"warningDark":0.39,"warningLight":0.68,"warningLighter":0.84,"warningLightest":0.93,"dangerDark":0.41,"dangerLight":0.72,"dangerLighter":0.89,"dangerLightest":0.95,"\_\_typename":"ColorLightnessThemeSettings"},"localOverride":false,"\_\_typename":"Theme"},"localOverride":false},"CachedAsset:text:en\_US-shared/client/components/common/Loading/LoadingDot-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-shared/client/components/common/Loading/LoadingDot-1758304526186","value":{"title":"Loading..."},"localOverride":false},"CachedAsset:quilt:o365.prod:pages/blogs/BlogMessagePage:board:MicrosoftSecurityExperts-1758304525115":{"\_\_typename":"CachedAsset","id":"quilt:o365.prod:pages/blogs/BlogMessagePage:board:MicrosoftSecurityExperts-1758304525115","value":{"id":"BlogMessagePage","container":{"id":"Common","headerProps":{"backgroundImageProps":null,"backgroundColor":null,"addComponents":null,"removeComponents":\["community.widget.bannerWidget"\],"componentOrder":null,"\_\_typename":"QuiltContainerSectionProps"},"headerComponentProps":{"community.widget.breadcrumbWidget":{"disableLastCrumbForDesktop":false}},"footerProps":null,"footerComponentProps":null,"items":\[{"id":"blog-article","layout":"ONE\_COLUMN","bgColor":null,"showTitle":null,"showDescription":null,"textPosition":null,"textColor":null,"sectionEditLevel":"LOCKED","bgImage":null,"disableSpacing":null,"edgeToEdgeDisplay":null,"fullHeight":null,"showBorder":null,"\_\_typename":"OneColumnQuiltSection","columnMap":{"main":\[{"id":"blogs.widget.blogArticleWidget","className":"lia-blog-container","props":null,"\_\_typename":"QuiltComponent"}\],"\_\_typename":"OneSectionColumns"}},{"id":"section-1729184836777","layout":"MAIN\_SIDE","bgColor":"transparent","showTitle":false,"showDescription":false,"textPosition":"CENTER","textColor":"var(--lia-bs-body-color)","sectionEditLevel":null,"bgImage":null,"disableSpacing":null,"edgeToEdgeDisplay":null,"fullHeight":null,"showBorder":null,"\_\_typename":"MainSideQuiltSection","columnMap":{"main":\[\],"side":\[\],"\_\_typename":"MainSideSectionColumns"}}\],"\_\_typename":"QuiltContainer"},"\_\_typename":"Quilt","localOverride":false},"localOverride":false},"CachedAsset:text:en\_US-components/common/EmailVerification-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/common/EmailVerification-1758304526186","value":{"email.verification.title":"Email Verification Required","email.verification.message.update.email":"To participate in the community, you must first verify your email address. The verification email was sent to {email}. To change your email, visit My Settings.","email.verification.message.resend.email":"To participate in the community, you must first verify your email address. The verification email was sent to {email}. Resend email."},"localOverride":false},"CachedAsset:text:en\_US-pages/blogs/BlogMessagePage-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-pages/blogs/BlogMessagePage-1758304526186","value":{"title":"{contextMessageSubject} \| {communityTitle}","errorMissing":"This blog post cannot be found","name":"Blog Message Page","section.blog-article.title":"Blog Post","archivedMessageTitle":"This Content Has Been Archived","section.section-1729184836777.title":"","section.section-1729184836777.description":"","section.CncIde.title":"Blog Post","section.tifEmD.description":"","section.tifEmD.title":""},"localOverride":false},"CachedAsset:quiltWrapper:o365.prod:Common:1758304525640":{"\_\_typename":"CachedAsset","id":"quiltWrapper:o365.prod:Common:1758304525640","value":{"id":"Common","header":{"backgroundImageProps":{"assetName":null,"backgroundSize":"COVER","backgroundRepeat":"NO\_REPEAT","backgroundPosition":"CENTER\_CENTER","lastModified":null,"\_\_typename":"BackgroundImageProps"},"backgroundColor":"transparent","items":\[{"id":"community.widget.navbarWidget","props":{"showUserName":true,"showRegisterLink":true,"useIconLanguagePicker":true,"useLabelLanguagePicker":true,"className":"QuiltComponent\_lia-component-edit-mode\_\_0nCcm","links":{"sideLinks":\[\],"mainLinks":\[{"children":\[\],"linkType":"INTERNAL","id":"gxcuf89792","params":{},"routeName":"CommunityPage"},{"children":\[\],"linkType":"EXTERNAL","id":"external-link","url":"/Directory","target":"SELF"},{"children":\[{"linkType":"INTERNAL","id":"microsoft365","params":{"categoryId":"microsoft365"},"routeName":"CategoryPage"},{"linkType":"INTERNAL","id":"windows","params":{"categoryId":"Windows"},"routeName":"CategoryPage"},{"linkType":"INTERNAL","id":"Common-microsoft365-copilot-link","params":{"categoryId":"Microsoft365Copilot"},"routeName":"CategoryPage"},{"linkType":"INTERNAL","id":"microsoft-teams","params":{"categoryId":"MicrosoftTeams"},"routeName":"CategoryPage"},{"linkType":"INTERNAL","id":"microsoft-securityand-compliance","params":{"categoryId":"microsoft-security"},"routeName":"CategoryPage"},{"linkType":"INTERNAL","id":"azure","params":{"categoryId":"Azure"},"routeName":"CategoryPage"},{"linkType":"INTERNAL","id":"Common-content\_management-link","params":{"categoryId":"Content\_Management"},"routeName":"CategoryPage"},{"linkType":"INTERNAL","id":"exchange","params":{"categoryId":"Exchange"},"routeName":"CategoryPage"},{"linkType":"INTERNAL","id":"windows-server","params":{"categoryId":"Windows-Server"},"routeName":"CategoryPage"},{"linkType":"INTERNAL","id":"outlook","params":{"categoryId":"Outlook"},"routeName":"CategoryPage"},{"linkType":"INTERNAL","id":"microsoft-endpoint-manager","params":{"categoryId":"microsoftintune"},"routeName":"CategoryPage"},{"linkType":"EXTERNAL","id":"external-link-2","url":"/Directory","target":"SELF"}\],"linkType":"EXTERNAL","id":"communities","url":"/","target":"BLANK"},{"children":\[{"linkType":"INTERNAL","id":"a-i","params":{"categoryId":"AI"},"routeName":"CategoryPage"},{"linkType":"INTERNAL","id":"education-sector","params":{"categoryId":"EducationSector"},"routeName":"CategoryPage"},{"linkType":"INTERNAL","id":"partner-community","params":{"categoryId":"PartnerCommunity"},"routeName":"CategoryPage"},{"linkType":"INTERNAL","id":"i-t-ops-talk","params":{"categoryId":"ITOpsTalk"},"routeName":"CategoryPage"},{"linkType":"INTERNAL","id":"healthcare-and-life-sciences","params":{"categoryId":"HealthcareAndLifeSciences"},"routeName":"CategoryPage"},{"linkType":"INTERNAL","id":"microsoft-mechanics","params":{"categoryId":"MicrosoftMechanics"},"routeName":"CategoryPage"},{"linkType":"INTERNAL","id":"public-sector","params":{"categoryId":"PublicSector"},"routeName":"CategoryPage"},{"linkType":"INTERNAL","id":"s-m-b","params":{"categoryId":"MicrosoftforNonprofits"},"routeName":"CategoryPage"},{"linkType":"INTERNAL","id":"io-t","params":{"categoryId":"IoT"},"routeName":"CategoryPage"},{"linkType":"INTERNAL","id":"startupsat-microsoft","params":{"categoryId":"StartupsatMicrosoft"},"routeName":"CategoryPage"},{"linkType":"INTERNAL","id":"driving-adoption","params":{"categoryId":"DrivingAdoption"},"routeName":"CategoryPage"},{"linkType":"EXTERNAL","id":"external-link-1","url":"/Directory","target":"SELF"}\],"linkType":"EXTERNAL","id":"communities-1","url":"/","target":"SELF"},{"children":\[\],"linkType":"EXTERNAL","id":"external","url":"/Blogs","target":"SELF"},{"children":\[\],"linkType":"EXTERNAL","id":"external-1","url":"/Events","target":"SELF"},{"children":\[{"linkType":"INTERNAL","id":"microsoft-learn-1","params":{"categoryId":"MicrosoftLearn"},"routeName":"CategoryPage"},{"linkType":"INTERNAL","id":"microsoft-learn-blog","params":{"boardId":"MicrosoftLearnBlog","categoryId":"MicrosoftLearn"},"routeName":"BlogBoardPage"},{"linkType":"EXTERNAL","id":"external-10","url":"/category/MicrosoftLearn?tab=grouphub","target":"BLANK"},{"linkType":"EXTERNAL","id":"external-3","url":"https://docs.microsoft.com/learn/dynamics365/?WT.mc\_id=techcom\_header-webpage-m365","target":"BLANK"},{"linkType":"EXTERNAL","id":"external-4","url":"https://docs.microsoft.com/learn/m365/?wt.mc\_id=techcom\_header-webpage-m365","target":"BLANK"},{"linkType":"EXTERNAL","id":"external-5","url":"https://docs.microsoft.com/learn/topics/sci/?wt.mc\_id=techcom\_header-webpage-m365","target":"BLANK"},{"linkType":"EXTERNAL","id":"external-6","url":"https://docs.microsoft.com/learn/powerplatform/?wt.mc\_id=techcom\_header-webpage-powerplatform","target":"BLANK"},{"linkType":"EXTERNAL","id":"external-7","url":"https://docs.microsoft.com/learn/github/?wt.mc\_id=techcom\_header-webpage-github","target":"BLANK"},{"linkType":"EXTERNAL","id":"external-8","url":"https://docs.microsoft.com/learn/teams/?wt.mc\_id=techcom\_header-webpage-teams","target":"BLANK"},{"linkType":"EXTERNAL","id":"external-9","url":"https://docs.microsoft.com/learn/dotnet/?wt.mc\_id=techcom\_header-webpage-dotnet","target":"BLANK"},{"linkType":"EXTERNAL","id":"external-2","url":"https://docs.microsoft.com/learn/azure/?WT.mc\_id=techcom\_header-webpage-m365","target":"BLANK"}\],"linkType":"INTERNAL","id":"microsoft-learn","params":{"categoryId":"MicrosoftLearn"},"routeName":"CategoryPage"},{"children":\[\],"linkType":"INTERNAL","id":"community-info-center","params":{"categoryId":"Community-Info-Center"},"routeName":"CategoryPage"}\]},"style":{"boxShadow":"var(--lia-bs-box-shadow-sm)","controllerHighlightColor":"hsla(30, 100%, 50%)","linkFontWeight":"400","dropdownDividerMarginBottom":"10px","hamburgerBorderHover":"none","linkBoxShadowHover":"none","linkFontSize":"14px","backgroundOpacity":0.8,"controllerBorderRadius":"var(--lia-border-radius-50)","hamburgerBgColor":"transparent","hamburgerColor":"var(--lia-nav-controller-icon-color)","linkTextBorderBottom":"none","brandLogoHeight":"30px","linkBgHoverColor":"transparent","linkLetterSpacing":"normal","collapseMenuDividerOpacity":0.16,"dropdownPaddingBottom":"15px","paddingBottom":"15px","dropdownMenuOffset":"2px","hamburgerBgHoverColor":"transparent","borderBottom":"1px solid var(--lia-bs-border-color)","hamburgerBorder":"none","dropdownPaddingX":"10px","brandMarginRightSm":"10px","linkBoxShadow":"none","collapseMenuDividerBg":"var(--lia-nav-link-color)","linkColor":"var(--lia-bs-body-color)","linkJustifyContent":"flex-start","dropdownPaddingTop":"10px","controllerHighlightTextColor":"var(--lia-yiq-dark)","controllerTextColor":"var(--lia-nav-controller-icon-color)","background":{"imageAssetName":"","color":"var(--lia-bs-white)","size":"COVER","repeat":"NO\_REPEAT","position":"CENTER\_CENTER","imageLastModified":""},"linkBorderRadius":"var(--lia-bs-border-radius-sm)","linkHoverColor":"var(--lia-bs-body-color)","position":"FIXED","linkBorder":"none","linkTextBorderBottomHover":"2px solid var(--lia-bs-body-color)","brandMarginRight":"30px","hamburgerHoverColor":"var(--lia-nav-controller-icon-color)","linkBorderHover":"none","collapseMenuMarginLeft":"20px","linkFontStyle":"NORMAL","controllerTextHoverColor":"var(--lia-nav-controller-icon-hover-color)","linkPaddingX":"10px","linkPaddingY":"5px","paddingTop":"15px","linkTextTransform":"NONE","dropdownBorderColor":"hsla(var(--lia-bs-black-h), var(--lia-bs-black-s), var(--lia-bs-black-l), 0.08)","controllerBgHoverColor":"hsla(var(--lia-bs-black-h), var(--lia-bs-black-s), var(--lia-bs-black-l), 0.1)","linkBgColor":"transparent","linkDropdownPaddingX":"var(--lia-nav-link-px)","linkDropdownPaddingY":"9px","controllerIconColor":"var(--lia-bs-body-color)","dropdownDividerMarginTop":"10px","linkGap":"10px","controllerIconHoverColor":"var(--lia-bs-body-color)"},"showSearchIcon":false,"languagePickerStyle":"iconAndLabel"},"\_\_typename":"QuiltComponent"},{"id":"community.widget.breadcrumbWidget","props":{"backgroundColor":"transparent","linkHighlightColor":"var(--lia-bs-primary)","visualEffects":{"showBottomBorder":true},"linkTextColor":"var(--lia-bs-gray-700)"},"\_\_typename":"QuiltComponent"},{"id":"custom.widget.CommunityBanner","props":{"widgetVisibility":"signedInOrAnonymous","useTitle":true,"usePageWidth":false,"useBackground":false,"title":"","lazyLoad":false},"\_\_typename":"QuiltComponent"},{"id":"custom.widget.HeroBanner","props":{"widgetVisibility":"signedInOrAnonymous","usePageWidth":false,"useTitle":true,"cMax\_items":3,"useBackground":false,"title":"","lazyLoad":false,"widgetChooser":"custom.widget.HeroBanner"},"\_\_typename":"QuiltComponent"}\],"\_\_typename":"QuiltWrapperSection"},"footer":{"backgroundImageProps":{"assetName":null,"backgroundSize":"COVER","backgroundRepeat":"NO\_REPEAT","backgroundPosition":"CENTER\_CENTER","lastModified":null,"\_\_typename":"BackgroundImageProps"},"backgroundColor":"transparent","items":\[{"id":"custom.widget.MicrosoftFooter","props":{"widgetVisibility":"signedInOrAnonymous","useTitle":true,"useBackground":false,"title":"","lazyLoad":false},"\_\_typename":"QuiltComponent"}\],"\_\_typename":"QuiltWrapperSection"},"\_\_typename":"QuiltWrapper","localOverride":false},"localOverride":false},"CachedAsset:text:en\_US-components/common/ActionFeedback-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/common/ActionFeedback-1758304526186","value":{"joinedGroupHub.title":"Welcome","joinedGroupHub.message":"You are now a member of this group and are subscribed to updates.","groupHubInviteNotFound.title":"Invitation Not Found","groupHubInviteNotFound.message":"Sorry, we could not find your invitation to the group. The owner may have canceled the invite.","groupHubNotFound.title":"Group Not Found","groupHubNotFound.message":"The grouphub you tried to join does not exist. It may have been deleted.","existingGroupHubMember.title":"Already Joined","existingGroupHubMember.message":"You are already a member of this group.","accountLocked.title":"Account Locked","accountLocked.message":"Your account has been locked due to multiple failed attempts. Try again in {lockoutTime} minutes.","editedGroupHub.title":"Changes Saved","editedGroupHub.message":"Your group has been updated.","leftGroupHub.title":"Goodbye","leftGroupHub.message":"You are no longer a member of this group and will not receive future updates.","deletedGroupHub.title":"Deleted","deletedGroupHub.message":"The group has been deleted.","groupHubCreated.title":"Group Created","groupHubCreated.message":"{groupHubName} is ready to use","accountClosed.title":"Account Closed","accountClosed.message":"The account has been closed and you will now be redirected to the homepage","resetTokenExpired.title":"Reset Password Link has Expired","resetTokenExpired.message":"Try resetting your password again","invalidUrl.title":"Invalid URL","invalidUrl.message":"The URL you're using is not recognized. Verify your URL and try again.","accountClosedForUser.title":"Account Closed","accountClosedForUser.message":"{userName}'s account is closed","inviteTokenInvalid.title":"Invitation Invalid","inviteTokenInvalid.message":"Your invitation to the community has been canceled or expired.","inviteTokenError.title":"Invitation Verification Failed","inviteTokenError.message":"The url you are utilizing is not recognized. Verify your URL and try again","pageNotFound.title":"Access Denied","pageNotFound.message":"You do not have access to this area of the community or it doesn't exist","eventAttending.title":"Responded as Attending","eventAttending.message":"You'll be notified when there's new activity and reminded as the event approaches","eventInterested.title":"Responded as Interested","eventInterested.message":"You'll be notified when there's new activity and reminded as the event approaches","eventNotFound.title":"Event Not Found","eventNotFound.message":"The event you tried to respond to does not exist.","redirectToRelatedPage.title":"Showing Related Content","redirectToRelatedPageForBaseUsers.title":"Showing Related Content","redirectToRelatedPageForBaseUsers.message":"The content you are trying to access is archived","redirectToRelatedPage.message":"The content you are trying to access is archived","relatedUrl.archivalLink.flyoutMessage":"The content you are trying to access is archived View Archived Content"},"localOverride":false},"CachedAsset:component:custom.widget.CommunityBanner-en-us-1758304579146":{"\_\_typename":"CachedAsset","id":"component:custom.widget.CommunityBanner-en-us-1758304579146","value":{"component":{"id":"custom.widget.CommunityBanner","template":{"id":"CommunityBanner","markupLanguage":"REACT","style":null,"texts":{},"defaults":{"config":{"applicablePages":\[\],"description":null,"fetchedContent":null,"\_\_typename":"ComponentConfiguration"},"props":\[\],"\_\_typename":"ComponentProperties"},"components":\[{"id":"custom.widget.CommunityBanner","form":null,"config":null,"props":\[\],"\_\_typename":"Component"}\],"grouping":"CUSTOM","\_\_typename":"ComponentTemplate"},"properties":{"config":{"applicablePages":\[\],"description":null,"fetchedContent":null,"\_\_typename":"ComponentConfiguration"},"props":\[\],"\_\_typename":"ComponentProperties"},"form":null,"\_\_typename":"Component","localOverride":false},"globalCss":null,"form":null},"localOverride":false},"CachedAsset:component:custom.widget.HeroBanner-en-us-1758304579146":{"\_\_typename":"CachedAsset","id":"component:custom.widget.HeroBanner-en-us-1758304579146","value":{"component":{"id":"custom.widget.HeroBanner","template":{"id":"HeroBanner","markupLanguage":"REACT","style":null,"texts":{"searchPlaceholderText":"Search this community","followActionText":"Follow","unfollowActionText":"Following","searchOnHoverText":"Please enter your search term(s) and then press return key to complete a search.","blogs.sidebar.pagetitle":"Latest Blogs \| Microsoft Tech Community","followThisNode":"Follow this node","unfollowThisNode":"Unfollow this node"},"defaults":{"config":{"applicablePages":\[\],"description":null,"fetchedContent":null,"\_\_typename":"ComponentConfiguration"},"props":\[{"id":"max\_items","dataType":"NUMBER","list":false,"defaultValue":"3","label":"Max Items","description":"The maximum number of items to display in the carousel","possibleValues":null,"control":"INPUT","\_\_typename":"PropDefinition"}\],"\_\_typename":"ComponentProperties"},"components":\[{"id":"custom.widget.HeroBanner","form":{"fields":\[{"id":"widgetChooser","validation":null,"noValidation":null,"dataType":"STRING","list":null,"control":null,"defaultValue":null,"label":null,"description":null,"possibleValues":null,"\_\_typename":"FormField"},{"id":"title","validation":null,"noValidation":null,"dataType":"STRING","list":null,"control":null,"defaultValue":null,"label":null,"description":null,"possibleValues":null,"\_\_typename":"FormField"},{"id":"useTitle","validation":null,"noValidation":null,"dataType":"BOOLEAN","list":null,"control":null,"defaultValue":null,"label":null,"description":null,"possibleValues":null,"\_\_typename":"FormField"},{"id":"useBackground","validation":null,"noValidation":null,"dataType":"BOOLEAN","list":null,"control":null,"defaultValue":null,"label":null,"description":null,"possibleValues":null,"\_\_typename":"FormField"},{"id":"widgetVisibility","validation":null,"noValidation":null,"dataType":"STRING","list":null,"control":null,"defaultValue":null,"label":null,"description":null,"possibleValues":null,"\_\_typename":"FormField"},{"id":"moreOptions","validation":null,"noValidation":null,"dataType":"STRING","list":null,"control":null,"defaultValue":null,"label":null,"description":null,"possibleValues":null,"\_\_typename":"FormField"},{"id":"cMax\_items","validation":null,"noValidation":null,"dataType":"NUMBER","list":false,"control":"INPUT","defaultValue":"3","label":"Max Items","description":"The maximum number of items to display in the carousel","possibleValues":null,"\_\_typename":"FormField"}\],"layout":{"rows":\[{"id":"widgetChooserGroup","type":"fieldset","as":null,"items":\[{"id":"widgetChooser","className":null,"\_\_typename":"FormFieldRef"}\],"props":null,"legend":null,"description":null,"className":null,"viewVariant":null,"toggleState":null,"\_\_typename":"FormFieldset"},{"id":"titleGroup","type":"fieldset","as":null,"items":\[{"id":"title","className":null,"\_\_typename":"FormFieldRef"},{"id":"useTitle","className":null,"\_\_typename":"FormFieldRef"}\],"props":null,"legend":null,"description":null,"className":null,"viewVariant":null,"toggleState":null,"\_\_typename":"FormFieldset"},{"id":"useBackground","type":"fieldset","as":null,"items":\[{"id":"useBackground","className":null,"\_\_typename":"FormFieldRef"}\],"props":null,"legend":null,"description":null,"className":null,"viewVariant":null,"toggleState":null,"\_\_typename":"FormFieldset"},{"id":"widgetVisibility","type":"fieldset","as":null,"items":\[{"id":"widgetVisibility","className":null,"\_\_typename":"FormFieldRef"}\],"props":null,"legend":null,"description":null,"className":null,"viewVariant":null,"toggleState":null,"\_\_typename":"FormFieldset"},{"id":"moreOptionsGroup","type":"fieldset","as":null,"items":\[{"id":"moreOptions","className":null,"\_\_typename":"FormFieldRef"}\],"props":null,"legend":null,"description":null,"className":null,"viewVariant":null,"toggleState":null,"\_\_typename":"FormFieldset"},{"id":"componentPropsGroup","type":"fieldset","as":null,"items":\[{"id":"cMax\_items","className":null,"\_\_typename":"FormFieldRef"}\],"props":null,"legend":null,"description":null,"className":null,"viewVariant":null,"toggleState":null,"\_\_typename":"FormFieldset"}\],"actionButtons":null,"className":"custom\_widget\_HeroBanner\_form","formGroupFieldSeparator":"divider","\_\_typename":"FormLayout"},"\_\_typename":"Form"},"config":null,"props":\[\],"\_\_typename":"Component"}\],"grouping":"CUSTOM","\_\_typename":"ComponentTemplate"},"properties":{"config":{"applicablePages":\[\],"description":null,"fetchedContent":null,"\_\_typename":"ComponentConfiguration"},"props":\[{"id":"max\_items","dataType":"NUMBER","list":false,"defaultValue":"3","label":"Max Items","description":"The maximum number of items to display in the carousel","possibleValues":null,"control":"INPUT","\_\_typename":"PropDefinition"}\],"\_\_typename":"ComponentProperties"},"form":{"fields":\[{"id":"widgetChooser","validation":null,"noValidation":null,"dataType":"STRING","list":null,"control":null,"defaultValue":null,"label":null,"description":null,"possibleValues":null,"\_\_typename":"FormField"},{"id":"title","validation":null,"noValidation":null,"dataType":"STRING","list":null,"control":null,"defaultValue":null,"label":null,"description":null,"possibleValues":null,"\_\_typename":"FormField"},{"id":"useTitle","validation":null,"noValidation":null,"dataType":"BOOLEAN","list":null,"control":null,"defaultValue":null,"label":null,"description":null,"possibleValues":null,"\_\_typename":"FormField"},{"id":"useBackground","validation":null,"noValidation":null,"dataType":"BOOLEAN","list":null,"control":null,"defaultValue":null,"label":null,"description":null,"possibleValues":null,"\_\_typename":"FormField"},{"id":"widgetVisibility","validation":null,"noValidation":null,"dataType":"STRING","list":null,"control":null,"defaultValue":null,"label":null,"description":null,"possibleValues":null,"\_\_typename":"FormField"},{"id":"moreOptions","validation":null,"noValidation":null,"dataType":"STRING","list":null,"control":null,"defaultValue":null,"label":null,"description":null,"possibleValues":null,"\_\_typename":"FormField"},{"id":"cMax\_items","validation":null,"noValidation":null,"dataType":"NUMBER","list":false,"control":"INPUT","defaultValue":"3","label":"Max Items","description":"The maximum number of items to display in the carousel","possibleValues":null,"\_\_typename":"FormField"}\],"layout":{"rows":\[{"id":"widgetChooserGroup","type":"fieldset","as":null,"items":\[{"id":"widgetChooser","className":null,"\_\_typename":"FormFieldRef"}\],"props":null,"legend":null,"description":null,"className":null,"viewVariant":null,"toggleState":null,"\_\_typename":"FormFieldset"},{"id":"titleGroup","type":"fieldset","as":null,"items":\[{"id":"title","className":null,"\_\_typename":"FormFieldRef"},{"id":"useTitle","className":null,"\_\_typename":"FormFieldRef"}\],"props":null,"legend":null,"description":null,"className":null,"viewVariant":null,"toggleState":null,"\_\_typename":"FormFieldset"},{"id":"useBackground","type":"fieldset","as":null,"items":\[{"id":"useBackground","className":null,"\_\_typename":"FormFieldRef"}\],"props":null,"legend":null,"description":null,"className":null,"viewVariant":null,"toggleState":null,"\_\_typename":"FormFieldset"},{"id":"widgetVisibility","type":"fieldset","as":null,"items":\[{"id":"widgetVisibility","className":null,"\_\_typename":"FormFieldRef"}\],"props":null,"legend":null,"description":null,"className":null,"viewVariant":null,"toggleState":null,"\_\_typename":"FormFieldset"},{"id":"moreOptionsGroup","type":"fieldset","as":null,"items":\[{"id":"moreOptions","className":null,"\_\_typename":"FormFieldRef"}\],"props":null,"legend":null,"description":null,"className":null,"viewVariant":null,"toggleState":null,"\_\_typename":"FormFieldset"},{"id":"componentPropsGroup","type":"fieldset","as":null,"items":\[{"id":"cMax\_items","className":null,"\_\_typename":"FormFieldRef"}\],"props":null,"legend":null,"description":null,"className":null,"viewVariant":null,"toggleState":null,"\_\_typename":"FormFieldset"}\],"actionButtons":null,"className":"custom\_widget\_HeroBanner\_form","formGroupFieldSeparator":"divider","\_\_typename":"FormLayout"},"\_\_typename":"Form"},"\_\_typename":"Component","localOverride":false},"globalCss":null,"form":{"fields":\[{"id":"widgetChooser","validation":null,"noValidation":null,"dataType":"STRING","list":null,"control":null,"defaultValue":null,"label":null,"description":null,"possibleValues":null,"\_\_typename":"FormField"},{"id":"title","validation":null,"noValidation":null,"dataType":"STRING","list":null,"control":null,"defaultValue":null,"label":null,"description":null,"possibleValues":null,"\_\_typename":"FormField"},{"id":"useTitle","validation":null,"noValidation":null,"dataType":"BOOLEAN","list":null,"control":null,"defaultValue":null,"label":null,"description":null,"possibleValues":null,"\_\_typename":"FormField"},{"id":"useBackground","validation":null,"noValidation":null,"dataType":"BOOLEAN","list":null,"control":null,"defaultValue":null,"label":null,"description":null,"possibleValues":null,"\_\_typename":"FormField"},{"id":"widgetVisibility","validation":null,"noValidation":null,"dataType":"STRING","list":null,"control":null,"defaultValue":null,"label":null,"description":null,"possibleValues":null,"\_\_typename":"FormField"},{"id":"moreOptions","validation":null,"noValidation":null,"dataType":"STRING","list":null,"control":null,"defaultValue":null,"label":null,"description":null,"possibleValues":null,"\_\_typename":"FormField"},{"id":"cMax\_items","validation":null,"noValidation":null,"dataType":"NUMBER","list":false,"control":"INPUT","defaultValue":"3","label":"Max Items","description":"The maximum number of items to display in the carousel","possibleValues":null,"\_\_typename":"FormField"}\],"layout":{"rows":\[{"id":"widgetChooserGroup","type":"fieldset","as":null,"items":\[{"id":"widgetChooser","className":null,"\_\_typename":"FormFieldRef"}\],"props":null,"legend":null,"description":null,"className":null,"viewVariant":null,"toggleState":null,"\_\_typename":"FormFieldset"},{"id":"titleGroup","type":"fieldset","as":null,"items":\[{"id":"title","className":null,"\_\_typename":"FormFieldRef"},{"id":"useTitle","className":null,"\_\_typename":"FormFieldRef"}\],"props":null,"legend":null,"description":null,"className":null,"viewVariant":null,"toggleState":null,"\_\_typename":"FormFieldset"},{"id":"useBackground","type":"fieldset","as":null,"items":\[{"id":"useBackground","className":null,"\_\_typename":"FormFieldRef"}\],"props":null,"legend":null,"description":null,"className":null,"viewVariant":null,"toggleState":null,"\_\_typename":"FormFieldset"},{"id":"widgetVisibility","type":"fieldset","as":null,"items":\[{"id":"widgetVisibility","className":null,"\_\_typename":"FormFieldRef"}\],"props":null,"legend":null,"description":null,"className":null,"viewVariant":null,"toggleState":null,"\_\_typename":"FormFieldset"},{"id":"moreOptionsGroup","type":"fieldset","as":null,"items":\[{"id":"moreOptions","className":null,"\_\_typename":"FormFieldRef"}\],"props":null,"legend":null,"description":null,"className":null,"viewVariant":null,"toggleState":null,"\_\_typename":"FormFieldset"},{"id":"componentPropsGroup","type":"fieldset","as":null,"items":\[{"id":"cMax\_items","className":null,"\_\_typename":"FormFieldRef"}\],"props":null,"legend":null,"description":null,"className":null,"viewVariant":null,"toggleState":null,"\_\_typename":"FormFieldset"}\],"actionButtons":null,"className":"custom\_widget\_HeroBanner\_form","formGroupFieldSeparator":"divider","\_\_typename":"FormLayout"},"\_\_typename":"Form"}},"localOverride":false},"CachedAsset:component:custom.widget.MicrosoftFooter-en-us-1758304579146":{"\_\_typename":"CachedAsset","id":"component:custom.widget.MicrosoftFooter-en-us-1758304579146","value":{"component":{"id":"custom.widget.MicrosoftFooter","template":{"id":"MicrosoftFooter","markupLanguage":"HANDLEBARS","style":".context-uhf {\\r\\n min-width: 280px;\\r\\n font-size: 15px;\\r\\n box-sizing: border-box;\\r\\n -ms-text-size-adjust: 100%;\\r\\n -webkit-text-size-adjust: 100%;\\r\\n & \*,\\r\\n & \*:before,\\r\\n & \*:after {\\r\\n box-sizing: inherit;\\r\\n }\\r\\n a.c-uhff-link {\\r\\n color: #616161;\\r\\n word-break: break-word;\\r\\n text-decoration: none;\\r\\n }\\r\\n &a:link,\\r\\n &a:focus,\\r\\n &a:hover,\\r\\n &a:active,\\r\\n &a:visited {\\r\\n text-decoration: none;\\r\\n color: inherit;\\r\\n }\\r\\n & div {\\r\\n font-family: 'Segoe UI', SegoeUI, 'Helvetica Neue', Helvetica, Arial, sans-serif;\\r\\n }\\r\\n}\\r\\n.c-uhff {\\r\\n background: #f2f2f2;\\r\\n margin: -1.5625;\\r\\n width: auto;\\r\\n height: auto;\\r\\n}\\r\\n.c-uhff-nav {\\r\\n margin: 0 auto;\\r\\n max-width: calc(1600px + 10%);\\r\\n padding: 0 5%;\\r\\n box-sizing: inherit;\\r\\n &:before,\\r\\n &:after {\\r\\n content: ' ';\\r\\n display: table;\\r\\n clear: left;\\r\\n }\\r\\n @media only screen and (max-width: 1083px) {\\r\\n padding-left: 12px;\\r\\n }\\r\\n .c-heading-4 {\\r\\n color: #616161;\\r\\n word-break: break-word;\\r\\n font-size: 15px;\\r\\n line-height: 20px;\\r\\n padding: 36px 0 4px;\\r\\n font-weight: 600;\\r\\n }\\r\\n .c-uhff-nav-row {\\r\\n .c-uhff-nav-group {\\r\\n display: block;\\r\\n float: left;\\r\\n min-height: 1px;\\r\\n vertical-align: text-top;\\r\\n padding: 0 12px;\\r\\n width: 100%;\\r\\n zoom: 1;\\r\\n &:first-child {\\r\\n padding-left: 0;\\r\\n @media only screen and (max-width: 1083px) {\\r\\n padding-left: 12px;\\r\\n }\\r\\n }\\r\\n @media only screen and (min-width: 540px) and (max-width: 1082px) {\\r\\n width: 33.33333%;\\r\\n }\\r\\n @media only screen and (min-width: 1083px) {\\r\\n width: 16.6666666667%;\\r\\n }\\r\\n ul.c-list.f-bare {\\r\\n font-size: 11px;\\r\\n line-height: 16px;\\r\\n margin-top: 0;\\r\\n margin-bottom: 0;\\r\\n padding-left: 0;\\r\\n list-style-type: none;\\r\\n li {\\r\\n word-break: break-word;\\r\\n padding: 8px 0;\\r\\n margin: 0;\\r\\n }\\r\\n }\\r\\n }\\r\\n }\\r\\n}\\r\\n.c-uhff-base {\\r\\n background: #f2f2f2;\\r\\n margin: 0 auto;\\r\\n max-width: calc(1600px + 10%);\\r\\n padding: 30px 5% 16px;\\r\\n &:before,\\r\\n &:after {\\r\\n content: ' ';\\r\\n display: table;\\r\\n }\\r\\n &:after {\\r\\n clear: both;\\r\\n }\\r\\n a.c-uhff-ccpa {\\r\\n font-size: 11px;\\r\\n line-height: 16px;\\r\\n float: left;\\r\\n margin: 3px 0;\\r\\n }\\r\\n a.c-uhff-ccpa:hover {\\r\\n text-decoration: underline;\\r\\n }\\r\\n ul.c-list {\\r\\n font-size: 11px;\\r\\n line-height: 16px;\\r\\n float: right;\\r\\n margin: 3px 0;\\r\\n color: #616161;\\r\\n li {\\r\\n padding: 0 24px 4px 0;\\r\\n display: inline-block;\\r\\n }\\r\\n }\\r\\n .c-list.f-bare {\\r\\n padding-left: 0;\\r\\n list-style-type: none;\\r\\n }\\r\\n @media only screen and (max-width: 1083px) {\\r\\n display: flex;\\r\\n flex-wrap: wrap;\\r\\n padding: 30px 24px 16px;\\r\\n }\\r\\n}\\r\\n\\r\\n.social-share {\\r\\n position: fixed;\\r\\n top: 60%;\\r\\n transform: translateY(-50%);\\r\\n left: 0;\\r\\n z-index: 1000;\\r\\n}\\r\\n\\r\\n.sharing-options {\\r\\n list-style: none;\\r\\n padding: 0;\\r\\n margin: 0;\\r\\n display: block;\\r\\n flex-direction: column;\\r\\n background-color: white;\\r\\n width: 50px;\\r\\n border-radius: 0px 7px 7px 0px;\\r\\n}\\r\\n.linkedin-icon {\\r\\n border-top-right-radius: 7px;\\r\\n}\\r\\n.linkedin-icon:hover {\\r\\n border-radius: 0;\\r\\n}\\r\\n\\r\\n.social-share-email-image:hover {\\r\\n border-radius: 0;\\r\\n}\\r\\n\\r\\n.social-link-footer:hover .linkedin-icon {\\r\\n border-radius: 0;\\r\\n}\\r\\n.social-link-footer:hover .social-share-email-image {\\r\\n border-radius: 0;\\r\\n}\\r\\n\\r\\n.social-link-footer img {\\r\\n width: 30px;\\r\\n height: auto;\\r\\n transition: filter 0.3s ease;\\r\\n}\\r\\n\\r\\n.social-share-list {\\r\\n width: 50px;\\r\\n}\\r\\n.social-share-rss-image {\\r\\n width: 30px;\\r\\n height: auto;\\r\\n transition: filter 0.3s ease;\\r\\n}\\r\\n.sharing-options li {\\r\\n width: 50px;\\r\\n height: 50px;\\r\\n padding: 8px;\\r\\n box-sizing: border-box;\\r\\n border: 2px solid white;\\r\\n display: inline-block;\\r\\n text-align: center;\\r\\n opacity: 1;\\r\\n visibility: visible;\\r\\n transition: border 0.3s ease; /\* Smooth transition effect \*/\\r\\n border-left: none;\\r\\n border-bottom: none; /\* Apply bottom border to only last item \*/\\r\\n}\\r\\n\\r\\n.social-share-list-linkedin {\\r\\n background-color: #0474b4;\\r\\n border-top-right-radius: 5px; /\* Rounded top right corner of first item\*/\\r\\n}\\r\\n.social-share-list-facebook {\\r\\n background-color: #3c5c9c;\\r\\n}\\r\\n.social-share-list-xicon {\\r\\n background-color: #000;\\r\\n}\\r\\n.social-share-list-reddit {\\r\\n background-color: #fc4404;\\r\\n}\\r\\n.social-share-list-bluesky {\\r\\n background-color: #f0f2f5;\\r\\n}\\r\\n.social-share-list-rss {\\r\\n background-color: #ec7b1c;\\r\\n}\\r\\n.social-share-list-mail {\\r\\n background-color: #848484;\\r\\n border-bottom-right-radius: 5px; /\* Rounded bottom right corner of last item\*/\\r\\n}\\r\\n.sharing-options li.social-share-list-mail {\\r\\n border-bottom: 2px solid white; /\* Add bottom border only to the last item \*/\\r\\n height: 52px; /\* Increase last child height to make in align with the hover label \*/\\r\\n}\\r\\n.x-icon {\\r\\n filter: invert(100%);\\r\\n transition: filter 0.3s ease;\\r\\n width: 20px !important;\\r\\n height: auto;\\r\\n padding-top: 5px !important;\\r\\n}\\r\\n.bluesky-icon {\\r\\n filter: invert(20%) sepia(100%) saturate(3000%) hue-rotate(180deg);\\r\\n transition: filter 0.3s ease;\\r\\n padding-top: 5px !important;\\r\\n width: 25px !important;\\r\\n}\\r\\n\\r\\n.share-icon {\\r\\n border: 2px solid transparent;\\r\\n display: inline-block;\\r\\n position: relative;\\r\\n}\\r\\n\\r\\n.sharing-options li:hover {\\r\\n border: 2px solid white;\\r\\n border-left: none;\\r\\n border-bottom: none;\\r\\n border-radius: 0px;\\r\\n}\\r\\n.sharing-options li.social-share-list-mail:hover {\\r\\n border-bottom: 2px solid white; /\* Add bottom border only to the last item \*/\\r\\n}\\r\\n\\r\\n.sharing-options li:hover .label {\\r\\n opacity: 1;\\r\\n visibility: visible;\\r\\n border: 2px solid white;\\r\\n box-sizing: border-box;\\r\\n border-left: none;\\r\\n}\\r\\n\\r\\n.label {\\r\\n position: absolute;\\r\\n left: 100%;\\r\\n white-space: nowrap;\\r\\n opacity: 0;\\r\\n visibility: hidden;\\r\\n transition: all 0.2s ease;\\r\\n color: white;\\r\\n border-radius: 0 10 0 10px;\\r\\n top: 50%;\\r\\n transform: translateY(-50%);\\r\\n height: 52px;\\r\\n display: flex;\\r\\n align-items: center;\\r\\n justify-content: center;\\r\\n padding: 10px 12px 15px 8px;\\r\\n border: 2px solid white;\\r\\n}\\r\\n.linkedin {\\r\\n background-color: #0474b4;\\r\\n border-top-right-radius: 5px; /\* Rounded top right corner of first item\*/\\r\\n}\\r\\n.facebook {\\r\\n background-color: #3c5c9c;\\r\\n}\\r\\n.twitter {\\r\\n background-color: black;\\r\\n color: white;\\r\\n}\\r\\n.reddit {\\r\\n background-color: #fc4404;\\r\\n}\\r\\n.mail {\\r\\n background-color: #848484;\\r\\n border-bottom-right-radius: 5px; /\* Rounded bottom right corner of last item\*/\\r\\n}\\r\\n.bluesky {\\r\\n background-color: #f0f2f5;\\r\\n color: black;\\r\\n}\\r\\n.rss {\\r\\n background-color: #ec7b1c;\\r\\n}\\r\\n\\r\\n@media (max-width: 991px) {\\r\\n .social-share {\\r\\n display: none;\\r\\n }\\r\\n}\\r\\n","texts":{"New tab":"What's New","New 1":"Surface Laptop Studio 2","New 2":"Surface Laptop Go 3","New 3":"Surface Pro 9","New 4":"Surface Laptop 5","New 5":"Surface Studio 2+","New 6":"Copilot in Windows","New 7":"Microsoft 365","New 8":"Windows 11 apps","Store tab":"Microsoft Store","Store 1":"Account Profile","Store 2":"Download Center","Store 3":"Microsoft Store Support","Store 4":"Returns","Store 5":"Order tracking","Store 6":"Certified Refurbished","Store 7":"Microsoft Store Promise","Store 8":"Flexible Payments","Education tab":"Education","Edu 1":"Microsoft in education","Edu 2":"Devices for education","Edu 3":"Microsoft Teams for Education","Edu 4":"Microsoft 365 Education","Edu 5":"How to buy for your school","Edu 6":"Educator Training and development","Edu 7":"Deals for students and parents","Edu 8":"Azure for students","Business tab":"Business","Bus 1":"Microsoft Cloud","Bus 2":"Microsoft Security","Bus 3":"Dynamics 365","Bus 4":"Microsoft 365","Bus 5":"Microsoft Power Platform","Bus 6":"Microsoft Teams","Bus 7":"Microsoft Industry","Bus 8":"Small Business","Developer tab":"Developer & IT","Dev 1":"Azure","Dev 2":"Developer Center","Dev 3":"Documentation","Dev 4":"Microsoft Learn","Dev 5":"Microsoft Tech Community","Dev 6":"Azure Marketplace","Dev 7":"AppSource","Dev 8":"Visual Studio","Company tab":"Company","Com 1":"Careers","Com 2":"About Microsoft","Com 3":"Company News","Com 4":"Privacy at Microsoft","Com 5":"Investors","Com 6":"Diversity and inclusion","Com 7":"Accessiblity","Com 8":"Sustainibility"},"defaults":{"config":{"applicablePages":\[\],"description":"The Microsoft Footer","fetchedContent":null,"\_\_typename":"ComponentConfiguration"},"props":\[\],"\_\_typename":"ComponentProperties"},"components":\[{"id":"custom.widget.MicrosoftFooter","form":null,"config":null,"props":\[\],"\_\_typename":"Component"}\],"grouping":"CUSTOM","\_\_typename":"ComponentTemplate"},"properties":{"config":{"applicablePages":\[\],"description":"The Microsoft Footer","fetchedContent":null,"\_\_typename":"ComponentConfiguration"},"props":\[\],"\_\_typename":"ComponentProperties"},"form":null,"\_\_typename":"Component","localOverride":false},"globalCss":{"css":".custom\_widget\_MicrosoftFooter\_context-uhf\_1w55e\_1 {\\r\\n min-width: 17.5rem;\\r\\n font-size: 0.9375rem;\\r\\n box-sizing: border-box;\\r\\n -ms-text-size-adjust: 100%;\\r\\n -webkit-text-size-adjust: 100%;\\r\\n & \*,\\r\\n & \*:before,\\r\\n & \*:after {\\r\\n box-sizing: inherit;\\r\\n }\\r\\n a.custom\_widget\_MicrosoftFooter\_c-uhff-link\_1w55e\_23 {\\r\\n color: #616161;\\r\\n word-break: break-word;\\r\\n text-decoration: none;\\r\\n }\\r\\n &a:link,\\r\\n &a:focus,\\r\\n &a:hover,\\r\\n &a:active,\\r\\n &a:visited {\\r\\n text-decoration: none;\\r\\n color: inherit;\\r\\n }\\r\\n & div {\\r\\n font-family: 'Segoe UI', SegoeUI, 'Helvetica Neue', Helvetica, Arial, sans-serif;\\r\\n }\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_c-uhff\_1w55e\_23 {\\r\\n background: #f2f2f2;\\r\\n margin: -1.5625;\\r\\n width: auto;\\r\\n height: auto;\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_c-uhff-nav\_1w55e\_69 {\\r\\n margin: 0 auto;\\r\\n max-width: calc(100rem + 10%);\\r\\n padding: 0 5%;\\r\\n box-sizing: inherit;\\r\\n &:before,\\r\\n &:after {\\r\\n content: ' ';\\r\\n display: table;\\r\\n clear: left;\\r\\n }\\r\\n @media only screen and (max-width: 1083px) {\\r\\n padding-left: 0.75rem;\\r\\n }\\r\\n .custom\_widget\_MicrosoftFooter\_c-heading-4\_1w55e\_97 {\\r\\n color: #616161;\\r\\n word-break: break-word;\\r\\n font-size: 0.9375rem;\\r\\n line-height: 1.25rem;\\r\\n padding: 2.25rem 0 0.25rem;\\r\\n font-weight: 600;\\r\\n }\\r\\n .custom\_widget\_MicrosoftFooter\_c-uhff-nav-row\_1w55e\_113 {\\r\\n .custom\_widget\_MicrosoftFooter\_c-uhff-nav-group\_1w55e\_115 {\\r\\n display: block;\\r\\n float: left;\\r\\n min-height: 0.0625rem;\\r\\n vertical-align: text-top;\\r\\n padding: 0 0.75rem;\\r\\n width: 100%;\\r\\n zoom: 1;\\r\\n &:first-child {\\r\\n padding-left: 0;\\r\\n @media only screen and (max-width: 1083px) {\\r\\n padding-left: 0.75rem;\\r\\n }\\r\\n }\\r\\n @media only screen and (min-width: 540px) and (max-width: 1082px) {\\r\\n width: 33.33333%;\\r\\n }\\r\\n @media only screen and (min-width: 1083px) {\\r\\n width: 16.6666666667%;\\r\\n }\\r\\n ul.custom\_widget\_MicrosoftFooter\_c-list\_1w55e\_155.custom\_widget\_MicrosoftFooter\_f-bare\_1w55e\_155 {\\r\\n font-size: 0.6875rem;\\r\\n line-height: 1rem;\\r\\n margin-top: 0;\\r\\n margin-bottom: 0;\\r\\n padding-left: 0;\\r\\n list-style-type: none;\\r\\n li {\\r\\n word-break: break-word;\\r\\n padding: 0.5rem 0;\\r\\n margin: 0;\\r\\n }\\r\\n }\\r\\n }\\r\\n }\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_c-uhff-base\_1w55e\_187 {\\r\\n background: #f2f2f2;\\r\\n margin: 0 auto;\\r\\n max-width: calc(100rem + 10%);\\r\\n padding: 1.875rem 5% 1rem;\\r\\n &:before,\\r\\n &:after {\\r\\n content: ' ';\\r\\n display: table;\\r\\n }\\r\\n &:after {\\r\\n clear: both;\\r\\n }\\r\\n a.custom\_widget\_MicrosoftFooter\_c-uhff-ccpa\_1w55e\_213 {\\r\\n font-size: 0.6875rem;\\r\\n line-height: 1rem;\\r\\n float: left;\\r\\n margin: 0.1875rem 0;\\r\\n }\\r\\n a.custom\_widget\_MicrosoftFooter\_c-uhff-ccpa\_1w55e\_213:hover {\\r\\n text-decoration: underline;\\r\\n }\\r\\n ul.custom\_widget\_MicrosoftFooter\_c-list\_1w55e\_155 {\\r\\n font-size: 0.6875rem;\\r\\n line-height: 1rem;\\r\\n float: right;\\r\\n margin: 0.1875rem 0;\\r\\n color: #616161;\\r\\n li {\\r\\n padding: 0 1.5rem 0.25rem 0;\\r\\n display: inline-block;\\r\\n }\\r\\n }\\r\\n .custom\_widget\_MicrosoftFooter\_c-list\_1w55e\_155.custom\_widget\_MicrosoftFooter\_f-bare\_1w55e\_155 {\\r\\n padding-left: 0;\\r\\n list-style-type: none;\\r\\n }\\r\\n @media only screen and (max-width: 1083px) {\\r\\n display: flex;\\r\\n flex-wrap: wrap;\\r\\n padding: 1.875rem 1.5rem 1rem;\\r\\n }\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_social-share\_1w55e\_275 {\\r\\n position: fixed;\\r\\n top: 60%;\\r\\n transform: translateY(-50%);\\r\\n left: 0;\\r\\n z-index: 1000;\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_sharing-options\_1w55e\_291 {\\r\\n list-style: none;\\r\\n padding: 0;\\r\\n margin: 0;\\r\\n display: block;\\r\\n flex-direction: column;\\r\\n background-color: white;\\r\\n width: 3.125rem;\\r\\n border-radius: 0 0.4375rem 0.4375rem 0;\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_linkedin-icon\_1w55e\_311 {\\r\\n border-top-right-radius: 7px;\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_linkedin-icon\_1w55e\_311:hover {\\r\\n border-radius: 0;\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_social-share-email-image\_1w55e\_325:hover {\\r\\n border-radius: 0;\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_social-link-footer\_1w55e\_333:hover .custom\_widget\_MicrosoftFooter\_linkedin-icon\_1w55e\_311 {\\r\\n border-radius: 0;\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_social-link-footer\_1w55e\_333:hover .custom\_widget\_MicrosoftFooter\_social-share-email-image\_1w55e\_325 {\\r\\n border-radius: 0;\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_social-link-footer\_1w55e\_333 img {\\r\\n width: 1.875rem;\\r\\n height: auto;\\r\\n transition: filter 0.3s ease;\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_social-share-list\_1w55e\_359 {\\r\\n width: 3.125rem;\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_social-share-rss-image\_1w55e\_365 {\\r\\n width: 1.875rem;\\r\\n height: auto;\\r\\n transition: filter 0.3s ease;\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_sharing-options\_1w55e\_291 li {\\r\\n width: 3.125rem;\\r\\n height: 3.125rem;\\r\\n padding: 0.5rem;\\r\\n box-sizing: border-box;\\r\\n border: 2px solid white;\\r\\n display: inline-block;\\r\\n text-align: center;\\r\\n opacity: 1;\\r\\n visibility: visible;\\r\\n transition: border 0.3s ease; /\* Smooth transition effect \*/\\r\\n border-left: none;\\r\\n border-bottom: none; /\* Apply bottom border to only last item \*/\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_social-share-list-linkedin\_1w55e\_405 {\\r\\n background-color: #0474b4;\\r\\n border-top-right-radius: 5px; /\* Rounded top right corner of first item\*/\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_social-share-list-facebook\_1w55e\_413 {\\r\\n background-color: #3c5c9c;\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_social-share-list-xicon\_1w55e\_419 {\\r\\n background-color: #000;\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_social-share-list-reddit\_1w55e\_425 {\\r\\n background-color: #fc4404;\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_social-share-list-bluesky\_1w55e\_431 {\\r\\n background-color: #f0f2f5;\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_social-share-list-rss\_1w55e\_437 {\\r\\n background-color: #ec7b1c;\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_social-share-list-mail\_1w55e\_443 {\\r\\n background-color: #848484;\\r\\n border-bottom-right-radius: 5px; /\* Rounded bottom right corner of last item\*/\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_sharing-options\_1w55e\_291 li.custom\_widget\_MicrosoftFooter\_social-share-list-mail\_1w55e\_443 {\\r\\n border-bottom: 2px solid white; /\* Add bottom border only to the last item \*/\\r\\n height: 3.25rem; /\* Increase last child height to make in align with the hover label \*/\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_x-icon\_1w55e\_459 {\\r\\n filter: invert(100%);\\r\\n transition: filter 0.3s ease;\\r\\n width: 1.25rem !important;\\r\\n height: auto;\\r\\n padding-top: 0.3125rem !important;\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_bluesky-icon\_1w55e\_473 {\\r\\n filter: invert(20%) sepia(100%) saturate(3000%) hue-rotate(180deg);\\r\\n transition: filter 0.3s ease;\\r\\n padding-top: 0.3125rem !important;\\r\\n width: 1.5625rem !important;\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_share-icon\_1w55e\_487 {\\r\\n border: 2px solid transparent;\\r\\n display: inline-block;\\r\\n position: relative;\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_sharing-options\_1w55e\_291 li:hover {\\r\\n border: 2px solid white;\\r\\n border-left: none;\\r\\n border-bottom: none;\\r\\n border-radius: 0;\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_sharing-options\_1w55e\_291 li.custom\_widget\_MicrosoftFooter\_social-share-list-mail\_1w55e\_443:hover {\\r\\n border-bottom: 2px solid white; /\* Add bottom border only to the last item \*/\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_sharing-options\_1w55e\_291 li:hover .custom\_widget\_MicrosoftFooter\_label\_1w55e\_519 {\\r\\n opacity: 1;\\r\\n visibility: visible;\\r\\n border: 2px solid white;\\r\\n box-sizing: border-box;\\r\\n border-left: none;\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_label\_1w55e\_519 {\\r\\n position: absolute;\\r\\n left: 100%;\\r\\n white-space: nowrap;\\r\\n opacity: 0;\\r\\n visibility: hidden;\\r\\n transition: all 0.2s ease;\\r\\n color: white;\\r\\n border-radius: 0 10 0 0.625rem;\\r\\n top: 50%;\\r\\n transform: translateY(-50%);\\r\\n height: 3.25rem;\\r\\n display: flex;\\r\\n align-items: center;\\r\\n justify-content: center;\\r\\n padding: 0.625rem 0.75rem 0.9375rem 0.5rem;\\r\\n border: 2px solid white;\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_linkedin\_1w55e\_311 {\\r\\n background-color: #0474b4;\\r\\n border-top-right-radius: 5px; /\* Rounded top right corner of first item\*/\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_facebook\_1w55e\_579 {\\r\\n background-color: #3c5c9c;\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_twitter\_1w55e\_585 {\\r\\n background-color: black;\\r\\n color: white;\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_reddit\_1w55e\_593 {\\r\\n background-color: #fc4404;\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_mail\_1w55e\_599 {\\r\\n background-color: #848484;\\r\\n border-bottom-right-radius: 5px; /\* Rounded bottom right corner of last item\*/\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_bluesky\_1w55e\_473 {\\r\\n background-color: #f0f2f5;\\r\\n color: black;\\r\\n}\\r\\n.custom\_widget\_MicrosoftFooter\_rss\_1w55e\_615 {\\r\\n background-color: #ec7b1c;\\r\\n}\\r\\n@media (max-width: 991px) {\\r\\n .custom\_widget\_MicrosoftFooter\_social-share\_1w55e\_275 {\\r\\n display: none;\\r\\n }\\r\\n}\\r\\n","tokens":{"context-uhf":"custom\_widget\_MicrosoftFooter\_context-uhf\_1w55e\_1","c-uhff-link":"custom\_widget\_MicrosoftFooter\_c-uhff-link\_1w55e\_23","c-uhff":"custom\_widget\_MicrosoftFooter\_c-uhff\_1w55e\_23","c-uhff-nav":"custom\_widget\_MicrosoftFooter\_c-uhff-nav\_1w55e\_69","c-heading-4":"custom\_widget\_MicrosoftFooter\_c-heading-4\_1w55e\_97","c-uhff-nav-row":"custom\_widget\_MicrosoftFooter\_c-uhff-nav-row\_1w55e\_113","c-uhff-nav-group":"custom\_widget\_MicrosoftFooter\_c-uhff-nav-group\_1w55e\_115","c-list":"custom\_widget\_MicrosoftFooter\_c-list\_1w55e\_155","f-bare":"custom\_widget\_MicrosoftFooter\_f-bare\_1w55e\_155","c-uhff-base":"custom\_widget\_MicrosoftFooter\_c-uhff-base\_1w55e\_187","c-uhff-ccpa":"custom\_widget\_MicrosoftFooter\_c-uhff-ccpa\_1w55e\_213","social-share":"custom\_widget\_MicrosoftFooter\_social-share\_1w55e\_275","sharing-options":"custom\_widget\_MicrosoftFooter\_sharing-options\_1w55e\_291","linkedin-icon":"custom\_widget\_MicrosoftFooter\_linkedin-icon\_1w55e\_311","social-share-email-image":"custom\_widget\_MicrosoftFooter\_social-share-email-image\_1w55e\_325","social-link-footer":"custom\_widget\_MicrosoftFooter\_social-link-footer\_1w55e\_333","social-share-list":"custom\_widget\_MicrosoftFooter\_social-share-list\_1w55e\_359","social-share-rss-image":"custom\_widget\_MicrosoftFooter\_social-share-rss-image\_1w55e\_365","social-share-list-linkedin":"custom\_widget\_MicrosoftFooter\_social-share-list-linkedin\_1w55e\_405","social-share-list-facebook":"custom\_widget\_MicrosoftFooter\_social-share-list-facebook\_1w55e\_413","social-share-list-xicon":"custom\_widget\_MicrosoftFooter\_social-share-list-xicon\_1w55e\_419","social-share-list-reddit":"custom\_widget\_MicrosoftFooter\_social-share-list-reddit\_1w55e\_425","social-share-list-bluesky":"custom\_widget\_MicrosoftFooter\_social-share-list-bluesky\_1w55e\_431","social-share-list-rss":"custom\_widget\_MicrosoftFooter\_social-share-list-rss\_1w55e\_437","social-share-list-mail":"custom\_widget\_MicrosoftFooter\_social-share-list-mail\_1w55e\_443","x-icon":"custom\_widget\_MicrosoftFooter\_x-icon\_1w55e\_459","bluesky-icon":"custom\_widget\_MicrosoftFooter\_bluesky-icon\_1w55e\_473","share-icon":"custom\_widget\_MicrosoftFooter\_share-icon\_1w55e\_487","label":"custom\_widget\_MicrosoftFooter\_label\_1w55e\_519","linkedin":"custom\_widget\_MicrosoftFooter\_linkedin\_1w55e\_311","facebook":"custom\_widget\_MicrosoftFooter\_facebook\_1w55e\_579","twitter":"custom\_widget\_MicrosoftFooter\_twitter\_1w55e\_585","reddit":"custom\_widget\_MicrosoftFooter\_reddit\_1w55e\_593","mail":"custom\_widget\_MicrosoftFooter\_mail\_1w55e\_599","bluesky":"custom\_widget\_MicrosoftFooter\_bluesky\_1w55e\_473","rss":"custom\_widget\_MicrosoftFooter\_rss\_1w55e\_615"}},"form":null},"localOverride":false},"CachedAsset:text:en\_US-components/community/Breadcrumb-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/community/Breadcrumb-1758304526186","value":{"navLabel":"Breadcrumbs","dropdown":"Additional parent page navigation"},"localOverride":false},"CachedAsset:text:en\_US-components/messages/MessageBanner-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/messages/MessageBanner-1758304526186","value":{"messageMarkedAsSpam":"This post has been marked as spam","messageMarkedAsSpam@board:TKB":"This article has been marked as spam","messageMarkedAsSpam@board:BLOG":"This post has been marked as spam","messageMarkedAsSpam@board:FORUM":"This discussion has been marked as spam","messageMarkedAsSpam@board:OCCASION":"This event has been marked as spam","messageMarkedAsSpam@board:IDEA":"This idea has been marked as spam","manageSpam":"Manage Spam","messageMarkedAsAbuse":"This post has been marked as abuse","messageMarkedAsAbuse@board:TKB":"This article has been marked as abuse","messageMarkedAsAbuse@board:BLOG":"This post has been marked as abuse","messageMarkedAsAbuse@board:FORUM":"This discussion has been marked as abuse","messageMarkedAsAbuse@board:OCCASION":"This event has been marked as abuse","messageMarkedAsAbuse@board:IDEA":"This idea has been marked as abuse","preModCommentAuthorText":"This comment will be published as soon as it is approved","preModCommentModeratorText":"This comment is awaiting moderation","messageMarkedAsOther":"This post has been rejected due to other reasons","messageMarkedAsOther@board:TKB":"This article has been rejected due to other reasons","messageMarkedAsOther@board:BLOG":"This post has been rejected due to other reasons","messageMarkedAsOther@board:FORUM":"This discussion has been rejected due to other reasons","messageMarkedAsOther@board:OCCASION":"This event has been rejected due to other reasons","messageMarkedAsOther@board:IDEA":"This idea has been rejected due to other reasons","messageArchived":"This post was archived on {date}","relatedUrl":"View Related Content","relatedContentText":"Showing related content","archivedContentLink":"View Archived Content"},"localOverride":false},"Category:category:Exchange":{"\_\_typename":"Category","id":"category:Exchange","categoryPolicies":{"\_\_typename":"CategoryPolicies","canReadNode":{"\_\_typename":"PolicyResult","failureReason":null}}},"Category:category:Outlook":{"\_\_typename":"Category","id":"category:Outlook","categoryPolicies":{"\_\_typename":"CategoryPolicies","canReadNode":{"\_\_typename":"PolicyResult","failureReason":null}}},"Category:category:Community-Info-Center":{"\_\_typename":"Category","id":"category:Community-Info-Center","categoryPolicies":{"\_\_typename":"CategoryPolicies","canReadNode":{"\_\_typename":"PolicyResult","failureReason":null}}},"Category:category:EducationSector":{"\_\_typename":"Category","id":"category:EducationSector","categoryPolicies":{"\_\_typename":"CategoryPolicies","canReadNode":{"\_\_typename":"PolicyResult","failureReason":null}}},"Category:category:DrivingAdoption":{"\_\_typename":"Category","id":"category:DrivingAdoption","categoryPolicies":{"\_\_typename":"CategoryPolicies","canReadNode":{"\_\_typename":"PolicyResult","failureReason":null}}},"Category:category:Azure":{"\_\_typename":"Category","id":"category:Azure","categoryPolicies":{"\_\_typename":"CategoryPolicies","canReadNode":{"\_\_typename":"PolicyResult","failureReason":null}}},"Category:category:Windows-Server":{"\_\_typename":"Category","id":"category:Windows-Server","categoryPolicies":{"\_\_typename":"CategoryPolicies","canReadNode":{"\_\_typename":"PolicyResult","failureReason":null}}},"Category:category:MicrosoftTeams":{"\_\_typename":"Category","id":"category:MicrosoftTeams","categoryPolicies":{"\_\_typename":"CategoryPolicies","canReadNode":{"\_\_typename":"PolicyResult","failureReason":null}}},"Category:category:PublicSector":{"\_\_typename":"Category","id":"category:PublicSector","categoryPolicies":{"\_\_typename":"CategoryPolicies","canReadNode":{"\_\_typename":"PolicyResult","failureReason":null}}},"Category:category:microsoft365":{"\_\_typename":"Category","id":"category:microsoft365","categoryPolicies":{"\_\_typename":"CategoryPolicies","canReadNode":{"\_\_typename":"PolicyResult","failureReason":null}}},"Category:category:IoT":{"\_\_typename":"Category","id":"category:IoT","categoryPolicies":{"\_\_typename":"CategoryPolicies","canReadNode":{"\_\_typename":"PolicyResult","failureReason":null}}},"Category:category:HealthcareAndLifeSciences":{"\_\_typename":"Category","id":"category:HealthcareAndLifeSciences","categoryPolicies":{"\_\_typename":"CategoryPolicies","canReadNode":{"\_\_typename":"PolicyResult","failureReason":null}}},"Category:category:ITOpsTalk":{"\_\_typename":"Category","id":"category:ITOpsTalk","categoryPolicies":{"\_\_typename":"CategoryPolicies","canReadNode":{"\_\_typename":"PolicyResult","failureReason":null}}},"Category:category:MicrosoftLearn":{"\_\_typename":"Category","id":"category:MicrosoftLearn","categoryPolicies":{"\_\_typename":"CategoryPolicies","canReadNode":{"\_\_typename":"PolicyResult","failureReason":null}}},"Blog:board:MicrosoftLearnBlog":{"\_\_typename":"Blog","id":"board:MicrosoftLearnBlog","blogPolicies":{"\_\_typename":"BlogPolicies","canReadNode":{"\_\_typename":"PolicyResult","failureReason":null}},"boardPolicies":{"\_\_typename":"BoardPolicies","canReadNode":{"\_\_typename":"PolicyResult","failureReason":null}}},"Category:category:MicrosoftMechanics":{"\_\_typename":"Category","id":"category:MicrosoftMechanics","categoryPolicies":{"\_\_typename":"CategoryPolicies","canReadNode":{"\_\_typename":"PolicyResult","failureReason":null}}},"Category:category:MicrosoftforNonprofits":{"\_\_typename":"Category","id":"category:MicrosoftforNonprofits","categoryPolicies":{"\_\_typename":"CategoryPolicies","canReadNode":{"\_\_typename":"PolicyResult","failureReason":null}}},"Category:category:StartupsatMicrosoft":{"\_\_typename":"Category","id":"category:StartupsatMicrosoft","categoryPolicies":{"\_\_typename":"CategoryPolicies","canReadNode":{"\_\_typename":"PolicyResult","failureReason":null}}},"Category:category:PartnerCommunity":{"\_\_typename":"Category","id":"category:PartnerCommunity","categoryPolicies":{"\_\_typename":"CategoryPolicies","canReadNode":{"\_\_typename":"PolicyResult","failureReason":null}}},"Category:category:Microsoft365Copilot":{"\_\_typename":"Category","id":"category:Microsoft365Copilot","categoryPolicies":{"\_\_typename":"CategoryPolicies","canReadNode":{"\_\_typename":"PolicyResult","failureReason":null}}},"Category:category:Windows":{"\_\_typename":"Category","id":"category:Windows","categoryPolicies":{"\_\_typename":"CategoryPolicies","canReadNode":{"\_\_typename":"PolicyResult","failureReason":null}}},"Category:category:Content\_Management":{"\_\_typename":"Category","id":"category:Content\_Management","categoryPolicies":{"\_\_typename":"CategoryPolicies","canReadNode":{"\_\_typename":"PolicyResult","failureReason":null}}},"Category:category:microsoftintune":{"\_\_typename":"Category","id":"category:microsoftintune","categoryPolicies":{"\_\_typename":"CategoryPolicies","canReadNode":{"\_\_typename":"PolicyResult","failureReason":null}}},"CachedAsset:text:en\_US-components/community/Navbar-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/community/Navbar-1758304526186","value":{"community":"Community Home","inbox":"Inbox","manageContent":"Manage Content","tos":"Terms of Service","forgotPassword":"Forgot Password","themeEditor":"Theme Editor","edit":"Edit Navigation Bar","skipContent":"Skip to content","gxcuf89792":"Tech Community","external-1":"Events","s-m-b":"Nonprofit Community","windows-server":"Windows Server","education-sector":"Education Sector","driving-adoption":"Driving Adoption","Common-content\_management-link":"Content Management","microsoft-learn":"Microsoft Learn","s-q-l-server":"Content Management","partner-community":"Microsoft Partner Community","microsoft365":"Microsoft 365","external-9":".NET","external-8":"Teams","external-7":"Github","products-services":"Products","external-6":"Power Platform","communities-1":"Topics","external-5":"Microsoft Security","planner":"Outlook","external-4":"Microsoft 365","external-3":"Dynamics 365","azure":"Azure","healthcare-and-life-sciences":"Healthcare and Life Sciences","external-2":"Azure","microsoft-mechanics":"Microsoft Mechanics","microsoft-learn-1":"Community","external-10":"Learning Room Directory","microsoft-learn-blog":"Blog","windows":"Windows","i-t-ops-talk":"ITOps Talk","external-link-1":"View All","microsoft-securityand-compliance":"Microsoft Security","public-sector":"Public Sector","community-info-center":"Lounge","external-link-2":"View All","microsoft-teams":"Microsoft Teams","external":"Blogs","microsoft-endpoint-manager":"Microsoft Intune","startupsat-microsoft":"Startups at Microsoft","exchange":"Exchange","a-i":"AI and Machine Learning","io-t":"Internet of Things (IoT)","Common-microsoft365-copilot-link":"Microsoft 365 Copilot","outlook":"Microsoft 365 Copilot","external-link":"Community Hubs","communities":"Products"},"localOverride":false},"CachedAsset:text:en\_US-components/community/NavbarHamburgerDropdown-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/community/NavbarHamburgerDropdown-1758304526186","value":{"hamburgerLabel":"Side Menu"},"localOverride":false},"CachedAsset:text:en\_US-components/community/BrandLogo-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/community/BrandLogo-1758304526186","value":{"logoAlt":"Khoros","themeLogoAlt":"Brand Logo"},"localOverride":false},"CachedAsset:text:en\_US-components/community/NavbarTextLinks-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/community/NavbarTextLinks-1758304526186","value":{"more":"More"},"localOverride":false},"CachedAsset:text:en\_US-components/authentication/AuthenticationLink-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/authentication/AuthenticationLink-1758304526186","value":{"title.login":"Sign In","title.registration":"Register","title.forgotPassword":"Forgot Password","title.multiAuthLogin":"Sign In"},"localOverride":false},"CachedAsset:text:en\_US-components/nodes/NodeLink-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/nodes/NodeLink-1758304526186","value":{"place":"Place {name}"},"localOverride":false},"CachedAsset:text:en\_US-components/messages/MessageView/MessageViewStandard-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/messages/MessageView/MessageViewStandard-1758304526186","value":{"anonymous":"Anonymous","author":"{messageAuthorLogin}","authorBy":"{messageAuthorLogin}","board":"{messageBoardTitle}","replyToUser":" to {parentAuthor}","showMoreReplies":"Show More","replyText":"Reply","repliesText":"Replies","markedAsSolved":"Marked as Solution","messageStatus":"Status: ","statusChanged":"Status changed: {previousStatus} to {currentStatus}","statusAdded":"Status added: {status}","statusRemoved":"Status removed: {status}","labelExpand":"expand replies","labelCollapse":"collapse replies","unhelpfulReason.reason1":"Content is outdated","unhelpfulReason.reason2":"Article is missing information","unhelpfulReason.reason3":"Content is for a different Product","unhelpfulReason.reason4":"Doesn't match what I was searching for"},"localOverride":false},"CachedAsset:text:en\_US-components/messages/MessageReplyCallToAction-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/messages/MessageReplyCallToAction-1758304526186","value":{"leaveReply":"Leave a reply...","leaveReply@board:BLOG@message:root":"Leave a comment...","leaveReply@board:TKB@message:root":"Leave a comment...","leaveReply@board:IDEA@message:root":"Leave a comment...","leaveReply@board:OCCASION@message:root":"Leave a comment...","repliesTurnedOff.FORUM":"Replies are turned off for this topic","repliesTurnedOff.BLOG":"Comments are turned off for this topic","repliesTurnedOff.TKB":"Comments are turned off for this topic","repliesTurnedOff.IDEA":"Comments are turned off for this topic","repliesTurnedOff.OCCASION":"Comments are turned off for this topic","infoText":"Stop poking me!"},"localOverride":false},"CachedAsset:text:en\_US-components/community/NavbarDropdownToggle-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/community/NavbarDropdownToggle-1758304526186","value":{"ariaLabelClosed":"Press the down arrow to open the menu"},"localOverride":false},"CachedAsset:text:en\_US-components/messages/MessageCoverImage-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/messages/MessageCoverImage-1758304526186","value":{"coverImageTitle":"Cover Image"},"localOverride":false},"CachedAsset:text:en\_US-shared/client/components/nodes/NodeTitle-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-shared/client/components/nodes/NodeTitle-1758304526186","value":{"nodeTitle":"{nodeTitle, select, community {Community} other {{nodeTitle}}} "},"localOverride":false},"CachedAsset:text:en\_US-components/messages/MessageTimeToRead-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/messages/MessageTimeToRead-1758304526186","value":{"minReadText":"{min} MIN READ"},"localOverride":false},"CachedAsset:text:en\_US-components/messages/MessageSubject-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/messages/MessageSubject-1758304526186","value":{"noSubject":"(no subject)"},"localOverride":false},"CachedAsset:text:en\_US-components/users/UserLink-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/users/UserLink-1758304526186","value":{"authorName":"View Profile: {author}","anonymous":"Anonymous"},"localOverride":false},"CachedAsset:text:en\_US-shared/client/components/users/UserRank-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-shared/client/components/users/UserRank-1758304526186","value":{"rankName":"{rankName}","userRank":"Author rank {rankName}"},"localOverride":false},"CachedAsset:text:en\_US-components/messages/MessageTime-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/messages/MessageTime-1758304526186","value":{"postTime":"Published: {time}","lastPublishTime":"Last Update: {time}","conversation.lastPostingActivityTime":"Last posting activity time: {time}","conversation.lastPostTime":"Last post time: {time}","moderationData.rejectTime":"Rejected time: {time}"},"localOverride":false},"CachedAsset:text:en\_US-components/messages/MessageBody-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/messages/MessageBody-1758304526186","value":{"showMessageBody":"Show More","mentionsErrorTitle":"{mentionsType, select, board {Board} user {User} message {Message} other {}} No Longer Available","mentionsErrorMessage":"The {mentionsType} you are trying to view has been removed from the community.","videoProcessing":"Video is being processed. Please try again in a few minutes.","bannerTitle":"Video provider requires cookies to play the video. Accept to continue or {url} it directly on the provider's site.","buttonTitle":"Accept","urlText":"watch"},"localOverride":false},"CachedAsset:text:en\_US-components/messages/MessageCustomFields-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/messages/MessageCustomFields-1758304526186","value":{"CustomField.default.label":"Value of {name}"},"localOverride":false},"CachedAsset:text:en\_US-components/messages/MessageRevision-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/messages/MessageRevision-1758304526186","value":{"lastUpdatedDatePublished":"{publishCount, plural, one{Published} other{Updated}} {date}","lastUpdatedDateDraft":"Created {date}","version":"Version {major}.{minor}"},"localOverride":false},"CachedAsset:text:en\_US-shared/client/components/common/QueryHandler-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-shared/client/components/common/QueryHandler-1758304526186","value":{"title":"Query Handler"},"localOverride":false},"CachedAsset:text:en\_US-components/messages/MessageReplyButton-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/messages/MessageReplyButton-1758304526186","value":{"repliesCount":"{count}","title":"Reply","title@board:BLOG@message:root":"Comment","title@board:TKB@message:root":"Comment","title@board:IDEA@message:root":"Comment","title@board:OCCASION@message:root":"Comment"},"localOverride":false},"CachedAsset:text:en\_US-components/messages/MessageAuthorBio-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/messages/MessageAuthorBio-1758304526186","value":{"sendMessage":"Send Message","actionMessage":"Follow this blog board to get notified when there's new activity","coAuthor":"CO-PUBLISHER","contributor":"CONTRIBUTOR","userProfile":"View Profile","iconlink":"Go to {name} {type}"},"localOverride":false},"CachedAsset:text:en\_US-shared/client/components/users/UserAvatar-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-shared/client/components/users/UserAvatar-1758304526186","value":{"altText":"{login}'s avatar","altTextGeneric":"User's avatar"},"localOverride":false},"CachedAsset:text:en\_US-shared/client/components/ranks/UserRankLabel-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-shared/client/components/ranks/UserRankLabel-1758304526186","value":{"altTitle":"Icon for {rankName} rank"},"localOverride":false},"CachedAsset:text:en\_US-components/common/ExternalLinkWarningModal-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/common/ExternalLinkWarningModal-1758304526186","value":{"title":"Leaving the Community","description":"You're about to leave this site and navigate to an external domain. Are you sure you want to continue?","action.submit":"Continue","action.cancel":"Go Back"},"localOverride":false},"CachedAsset:text:en\_US-components/tags/TagView/TagViewChip-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/tags/TagView/TagViewChip-1758304526186","value":{"tagLabelName":"Tag name {tagName}"},"localOverride":false},"CachedAsset:text:en\_US-components/users/UserRegistrationDate-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-components/users/UserRegistrationDate-1758304526186","value":{"noPrefix":"{date}","withPrefix":"Joined {date}"},"localOverride":false},"CachedAsset:text:en\_US-shared/client/components/nodes/NodeAvatar-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-shared/client/components/nodes/NodeAvatar-1758304526186","value":{"altTitle":"Node avatar for {nodeTitle}"},"localOverride":false},"CachedAsset:text:en\_US-shared/client/components/nodes/NodeDescription-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-shared/client/components/nodes/NodeDescription-1758304526186","value":{"description":"{description}"},"localOverride":false},"CachedAsset:text:en\_US-shared/client/components/nodes/NodeIcon-1758304526186":{"\_\_typename":"CachedAsset","id":"text:en\_US-shared/client/components/nodes/NodeIcon-1758304526186","value":{"contentType":"Content Type {style, select, FORUM {Forum} BLOG {Blog} TKB {Knowledge Base} IDEA {Ideas} OCCASION {Events} other {}} icon"},"localOverride":false}}}},"page":"/blogs/BlogMessagePage/BlogMessagePage","query":{"boardId":"microsoftsecurityexperts","messageSubject":"total-identity-compromise-microsoft-incident-response-lessons-on-securing-active","messageId":"3753391"},"buildId":"WM9SdYbkBOUO6CupNKc\_7","runtimeConfig":{"buildInformationVisible":false,"logLevelApp":"info","logLevelMetrics":"info","surveysEnabled":true,"openTelemetry":{"clientEnabled":false,"configName":"o365","serviceVersion":"25.8.0","universe":"prod","collector":"http://localhost:4318","logLevel":"error","routeChangeAllowedTime":"5000","headers":"","enableDiagnostic":"false","maxAttributeValueLength":"4095"},"apolloDevToolsEnabled":false,"quiltLazyLoadThreshold":"3"},"isFallback":false,"isExperimentalCompile":false,"dynamicIds":\["components\_community\_Navbar\_NavbarWidget","components\_community\_Breadcrumb\_BreadcrumbWidget","components\_customComponent\_CustomComponent","components\_blogs\_BlogArticleWidget","components\_external\_components\_ExternalComponent","components\_messages\_MessageView\_MessageViewStandard","shared\_client\_components\_common\_List\_UnwrappedList","components\_tags\_TagView","components\_tags\_TagView\_TagViewChip","components\_customComponent\_CustomComponentContent\_TemplateContent"\],"appGip":true,"scriptLoader":\[{"id":"analytics","src":"https://techcommunity.microsoft.com/t5/s/gxcuf89792/pagescripts/1750802071000/analytics.js?page.id=BlogMessagePage&entity.id=board%3Amicrosoftsecurityexperts&entity.id=message%3A3753391","strategy":"afterInteractive"}\]}
