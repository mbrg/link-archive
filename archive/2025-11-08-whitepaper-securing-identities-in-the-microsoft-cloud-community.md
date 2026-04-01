---
date: '2025-11-08'
description: The whitepaper outlines a Risk-based Privilege Framework designed to
  secure identities within Microsoft Entra ID and Azure. It categorizes roles into
  High, Medium, and Low risk based on their potential impact on the organization's
  security. Critical roles, like Global Administrator, are prioritized for stringent
  protections such as phishing-resistant MFA and dedicated workstations. The framework
  addresses challenges in privilege sprawl, hidden escalation paths, and inefficient
  controls, advocating for strategic allocation of security resources. This model
  facilitates tailored security measures, enhancing operational efficiency while mitigating
  complexities associated with hybrid identity environments.
link: https://security.googlecloudcommunity.com/community-blog-42/whitepaper-securing-identities-in-the-microsoft-cloud-6077
tags:
- Identity Management
- Microsoft Azure
- Cloud Security
- Access Control
- Risk Management
title: 'Whitepaper: Securing Identities in the Microsoft Cloud ◆ Community'
---

[Skip to main content](https://security.googlecloudcommunity.com/community-blog-42/whitepaper-securing-identities-in-the-microsoft-cloud-6077#breadcrumbs-target)

[![Google Cloud Security Logo](https://uploads-us-west-2.insided.com/securitygooglecloud-en/attachment/d62c88eb-93ce-4e42-b40a-0fa2d44267da_thumb.png)](https://security.googlecloudcommunity.com/)

[![Google Cloud Security Logo](https://uploads-us-west-2.insided.com/securitygooglecloud-en/attachment/d62c88eb-93ce-4e42-b40a-0fa2d44267da_thumb.png)](https://security.googlecloudcommunity.com/)

Search

- [Create topic](https://security.googlecloudcommunity.com/topic/new "Create topic")
- [Login](https://security.googlecloudcommunity.com/community-blog-42/whitepaper-securing-identities-in-the-microsoft-cloud-6077#)

Search

Community Webinar: IaC For Threat Detection: Operationalizing OSINT Into Google SecOps Rules

(Tue, Nov 11, 12:00 PM)

- [Home](https://security.googlecloudcommunity.com/)
- [Knowledge base overview](https://security.googlecloudcommunity.com/knowledge-base)
- [Resource Center](https://security.googlecloudcommunity.com/resource-center-23)
- [Community Blog](https://security.googlecloudcommunity.com/community-blog-42)
- Whitepaper: Securing Identities in the Microsoft Cloud

* * *

[![yuri](https://uploads-us-west-2.insided.com/securitygooglecloud-en/icon/200x200/84c1506d-3536-4ad6-ad18-66219024e41c.png)\\
![Staff](https://uploads-us-west-2.insided.com/securitygooglecloud-en/attachment/2eaec9f5-7193-4586-856c-becc368c1691_thumb.png)](https://security.googlecloudcommunity.com/members/yuri-422761)

![Forum|alt.badge.img](https://uploads-us-west-2.insided.com/securitygooglecloud-en/attachment/2048c00f-c388-495f-a136-aa03e1d5c3ac_thumb.png)

- [yuri](https://security.googlecloudcommunity.com/members/yuri-422761)

- Staff

_Co-Authors: [Razvan Buliga](https://security.googlecloudcommunity.com/members/razvanb-422717), [Ischa Rijff](https://security.googlecloudcommunity.com/members/ischa-rijff-422978)_

## Executive Summary

As organizations migrate to the cloud, identity has become the primary security perimeter. The proliferation of roles and permissions across two distinct but interconnected RBAC systems in Microsoft Entra ID and Microsoft Azure creates a complex and often misunderstood attack surface. A single compromised account with excessive privileges can lead to a full tenant takeover, data exfiltration, or catastrophic service disruption.

This whitepaper presents a unified, risk-based privilege framework for securing identities and roles in Microsoft Entra ID and Azure. It is designed for large organizations with a need to balance security controls with administrative usability and operational efficiency. By classifying roles into distinct **High, Medium and Low** risk categories based on their potential impact and known attack paths, organizations can prioritize and systematically apply proportionate security controls to reduce their attack surface.

The core of this framework is a three-level risk-based privilege model with explicit security requirements:

- **High-risk Roles:** High privilege roles with direct or indirect paths to complete control over the environment. These are the "keys to the kingdom" and require the most stringent protections, including **phishing-resistant MFA** and dedicated **physical Privileged Admin Workstation (PAW)** for human identities and short-lived token based authentication using Managed or Federated Identities with location restrictions for machine identities.
- **Medium-risk Roles:** Medium risk roles with extensive administrative rights over specific services or large segments of the environment (e.g., Exchange Online, critical subscriptions). These require strong protections like **phishing-resistant MFA** and isolated **Secure Admin Workstation (SAW)** for human identities and authentication with short-lived secrets using Managed or Federated Identities with location restrictions for machine identities.
- **Low-risk Roles:** Roles with narrowly scoped permissions that pose little to no systemic security risk. These can be managed with standard corporate security controls.

Implementing this risk-based privilege framework enables organizations to move beyond a one-size-fits-all security posture, focusing their most robust defenses on the roles that pose the greatest risk.

## 1\. The Challenge: Privilege Sprawl in the Cloud

Unlike on-premises environments, the cloud control plane is directly accessible from the internet making it a globally accessible target for attacks. The distinction between roles that manage identity (Entra ID), Microsoft 365 (e.g., SharePoint Online, Exchange Online) services and roles that manage infrastructure (Azure) is getting more blurred. This is magnified by machine identities (e.g., service principals) that can be impersonated by other identities creating a complex and interconnected web of permissions that obscures the true scope of access and creates hidden privilege escalation paths.

For instance, a role in Entra ID, such as Application Administrator, can be leveraged to compromise Azure resources as exemplified in the case study below. This convergence of identity and infrastructure management planes creates a multi-layered attack surface that is often poorly understood.

Especially for larger organizations where management and budget become strong factors in securing cloud identities, a one-size-fits-all approach to privileged identities does not provide enough flexibility and control.

### **Key Security Challenges**

This complexity leads to several significant challenges:

- **Default Over-Privileging:** For convenience, organizations often grant broad roles like Global Administrator or Contributor across large scopes, providing excessive permissions.
- **Hidden Escalation Paths:** Not all privilege is obvious. Research on [Entra ID attack paths](https://cloud.google.com/blog/topics/threat-intelligence/abusing-intune-permissions-entra-id-environments?e=48754805) demonstrates that many roles can be abused in non-intuitive ways to escalate to higher levels of access.
- **Inefficient Security Controls:** Applying the same level of protection (e.g., MFA, session monitoring) to all administrative roles—such as treating a lower risk Global Reader the same as a high-risk Global Administrator—is an inefficient allocation of resources and creates a false sense of security.

### **A Case Study in Hidden Risk: The Application Administrator role**

The "Application Administrator" role perfectly illustrates these interconnected risks.

1. **The Perceived Role:** The name suggests the role can manage enterprise applications, such as adding, configuring, or removing applications.
2. **The Hidden Path:** This role grants the ability to add a new credential (client secret or certificate) to any existing application or service principal in the tenant, including those that have been granted Admin Consent for high-privilege API permissions (e.g., RoleManagement.ReadWrite.Directory) or have been directly assigned a highly privileged directory role (e.g., Global Administrator, Privileged Role Administrator).
3. **The Escalation:** By authenticating as the compromised application using the new credential, the user effectively inherits the application's permissions. This can lead to a full privilege escalation to a Global Administrator or other high-impact roles, resulting in complete tenant compromise and long-term persistence.
4. **The Full Environment Compromise**: Once an attacker has achieved Global Administrator, they can elevate their own access to manage all Azure resources by granting themselves the User Access Administrator role at the Azure Root Management Group scope. This role gives them full control over all Azure subscriptions and the infrastructure they contain.

This hidden potential for escalation means the Application Administrator role, while seemingly scoped to application management, must be secured with the vigilance typically reserved for high-privilege roles, as it provides an indirect path to compromise the entire directory.

### **The Solution: The Risk-based Privilege Framework**

The solution is a structured approach we call the Risk-based Privilege Framework.This framework, based on a risk classification model (see Section 2), provides a set of rules and guidelines that allow an organization to focus your most robust security controls on the assets that matter most: high-privileged administrative accounts.

## 2\. Risk-based Privilege Model

This model categorizes roles into **High, Medium and Low risk**, based on the amount of control they grant to a given scope. Each category is aligned with specific security controls.

It is of note to mention that this goes beyond the standard “privileged” classification given by [Microsoft to Entra ID roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference), which does not take scope into account or a possibility for a privileged elevation path.

### **High-Risk Roles**

- **Definition:** Roles that grant ultimate control over the identity and/or infrastructure environment, or provide a direct path to roles that do so. A compromise in this tier is catastrophic, leading to full tenant takeover.
- **Scope:** Tenant-wide, root management groups (MG) or the entire environment.
- **Guiding Principle:** Identities assigned these roles are the highest value targets. Compromise can lead to full tenant takeover, data exfiltration, or catastrophic service disruption.
- **Security Controls:** Complete isolation. Activities must be done on dedicated PAW and be completely isolated from lower-tier administrative activities and general user productivity (e.g., email, web browsing).
- **Examples:**
  - **Entra ID:** Global Administrator, Privileged Role Administrator, Domain Name Administrator.
  - **Azure:** Owner or User Access Administrator at the Root Management Group scope.
- See **Table 3** below for a list of high-risk roles in Entra ID
- See **Table 7** below for a list of high-risk roles in Azure

### **Medium-Risk Roles**

- **Definition:** Roles with broad administrative access to specific Microsoft 365 services, Azure subscriptions, or resource groups. These roles are highly privileged within their domain, granting significant control over specific workloads and data. While these roles do not have a known direct path to compromise the entire environment, they still pose a substantial risk. Depending on the environment's configuration, these roles can still be used for privilege escalation. Therefore, a thorough risk assessment must consider potential indirect paths based on dependencies in the environment that could elevate the risk associated with these roles.
- **Scope:** Specific M365 services (e.g., Exchange, SharePoint, Teams), critical Azure subscriptions, or management groups containing production workloads.
- **Guiding Principle:** Identities assigned these roles are high-value targets. While they don't control the entire environment, compromise can lead to significant disruption or data loss within the associated services.
- **Security controls:** Session isolation; Activities must be done on dedicated SAW and be isolated from lower-tier administrative activities and general user productivity (e.g., email, web browsing).
- **Examples of roles:**
  - **Entra ID:** Application Administrator, Exchange Administrator, SharePoint Administrator, User Administrator, Helpdesk Administrator.
  - **Azure:** Owner or Contributor scoped to a business-critical subscription or resource group.
- See **Table 4** below for a list of medium-risk roles in Entra ID
- See **Table 7** below for a list of medium-risk roles in Azure

### **Low-Risk Roles**

- **Definition:** Roles with limited, read-only, or narrowly scoped administrative permissions. A compromise of these accounts has a low impact on the overall security of the environment.
- **Scope:** A single resource, read-only access across a service, or a specific, non-critical operational function/workload.
- **Guiding Principle:** Identities assigned these roles pose a low risk to the overall environment; however, enforcing least privilege and limiting potential impact are essential to prevent unintended privilege escalation.
- **Security Controls:** Less stringent than for high and medium-risk roles. Standard user security hygiene is often sufficient.
- **Examples:**
  - **Entra ID:** Directory Readers, Reports Reader, Application Developer.
  - **Azure:** Reader at any scope, Contributor scoped to a single, isolated, or non-critical resource.
- See **Table 5** below for a list of low-risk roles in Entra ID
- See **Table 7** below for a list of low-risk roles in Azure

## 3\. Required Security Controls

With roles divided into **High, Medium and Low risk** categories based on the principles outlined above (level of control and scope), we have defined mandated security controls. These controls should be directly proportional to the level of risk associated with the role. Additionally, human identities (users) need different controls than machine identities (e.g. service principals).

Controls are defined for the following aspects associated with the role and identity:

- **Authentication**
- **Account type**
- **Access device**
- **Privileged Identity Management (PIM) Configuration**
- **Session Duration**
- **Monitoring and Alerting**

![](https://uploads-us-west-2.insided.com/securitygooglecloud-en/attachment/940a0f2d-2bc1-4be9-98e7-426b3933bf59.png)Figure 1: Overview of Required Security Controls for Human Identities by Risk Privilege Level![](https://uploads-us-west-2.insided.com/securitygooglecloud-en/attachment/c6deadc1-9173-4be5-bf75-6b74e06c35de.png)Figure 2: Overview of Required Security Controls for Machine Identities by Risk Privilege Level

## 3.1 Required Security Controls for Human Identities by Risk Privilege Level

Applying security controls should be directly proportional to the risk of the role. The following table outlines the minimum required controls for each privilege level.

|     |     |     |     |
| --- | --- | --- | --- |
| **Security Control** | **High-Risk Roles** | **Medium-Risk Roles** | **Low-Risk Roles** |
| **Account type** | **Cloud-only account**<br>Created directly in Entra ID, not synchronized from on-premises Active Directory. Must be used for administrative tasks only. | **Cloud-only account**<br>Created directly in Entra ID, not synchronized from on-premises Active Directory. Must be used for administrative tasks only. | **Regular account**<br>Regular day-to-day account, may be synchronized from on-premises Active Directory. Can be used for productivity tasks (email, collaboration, etc.). |
| **Access Device** | **Physical Privileged Access Workstation (PAW)**. A dedicated, locked-down physical device used _only_ for privileged tasks. Managed and compliant endpoint. | **Secure Admin Workstation (SAW)**. A dedicated, locked-down (virtual) machine (e.g., via Azure Virtual Desktop) used for admin tasks. Managed and compliant endpoint. | **Standard Corporate Device**. A managed and compliant endpoint. |
| **Authentication** | **Phishing-Resistant MFA Required** (e.g., FIDO2 Security Keys, Windows Hello for Business). | **Phishing-Resistant MFA Required** (e.g., FIDO2 Security Keys, Windows Hello for Business). | **Strong MFA Required** (e.g., Number Matching in Microsoft Authenticator app). |
| **Session Duration** | **Time-bound to shorter periods (e.g., 4 hours)** | **Limited to a standard workday (e.g., 8 hours)** | **Follow standard user session policies.** |
| **Access Provisioning** | **Just-in-Time only. Security team approval required**with justification. Short, time-bound access (e.g., < 4 hours). <br>Role activation must request the required MFA strength. | **Just-in-Time only.**<br>**Manager approval required**with justification.Time-bound access limited to standard workday duration.<br>Role activation must request the required MFA strength. | **Automatic grants**allowed. Default activation duration and optional justification if PIM is used.<br>Role activation must request the required MFA strength. |
| **Additional Access Conditions** | Implement [Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection) risk-based policies to block access on medium- or high-risk detections. | Implement [Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection) risk-based policies to block access on high-risk detections. | Implement [Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection) risk-based policies to block access on high-risk detections. |
| **Monitoring & Alerting** | **Highest priority alerts** should be configured to trigger on any anomalous or suspicious behavior. | **High-priority alerts** should be configured to trigger on any anomalous or suspicious behavior. | **Standard Logging.** Activities are logged for audit and forensic purposes. |

_Table 1: Required Security Controls for Human Identities by Risk Privilege Level_

## 3.2 Required Security Controls for Machine Identities by Risk Privilege Level

Just as with human identities, a risk-based approach to securing machine identities based on their privilege level is essential. The following table outlines the mandated security controls for **High, Medium, and Low-Risk** machine identities.

|     |     |     |     |
| --- | --- | --- | --- |
| **Security Control** | **High-Risk Roles** | **Medium-Risk Roles** | **Low-Risk Roles** |
| **Identity type** | **Federated or Managed Identities.** | **Federated or Managed Identities recommended.**<br>Service principals preferably with certificates. | **Federated or Managed Identities are highly recommended.**<br>Service principals preferably with certificates. |
| **Authentication** | **Short lived token based**. | **Short lived token or certificate based.**<br>Client secrets only with short expiration and automated rotation. | **Short lived token or certificate based.**<br>Client secrets only with short expiration and automated rotation. |
| **Additional Access Conditions** | Limit access to only trusted networks. <br>Implement [Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection) risk-based policies to block access on medium- or high-risk detections. | Limit access to only trusted networks. <br>Implement [Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection) risk-based policies to block access on high-risk detections. | Preferably limit access to only trusted networks.<br>Implement [Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection) risk-based policies to block access on high-risk detections. |
| **Monitoring & Alerting** | **Highest priority alerts** should be configured to trigger on any anomalous or suspicious behavior. | **High-priority alerts** should be configured to trigger on any anomalous or suspicious behavior. | **Standard Logging.** All activities are logged for routine audit and forensic purposes. Alerts should be configured for significant deviations from normal activity. |

_Table 2: Required Security Controls for Machine Identities by Risk Privilege Level_

## 4\. Comprehensive Role Classification Reference

The following tables provide a detailed, non-exhaustive classification of Entra ID and Azure roles based on a synthesis of the attack-path-focused tiering model and the risk-based Mandiant framework. Organizations must perform their own analysis, but this serves as a strong baseline for prioritizing security efforts.

## 4.1 Entra ID Role Classifications

### **High-Risk Roles**

|     |     |
| --- | --- |
| **Entra Role** | **Justification / Key Risk** |
| **Global Administrator** | The ultimate authority. Can manage all aspects of Entra ID and services that use Entra identities such as Azure. |
| **Privileged Role Administrator** | Can manage role assignments in Entra ID and PIM. Can assign any role, including Global Admin, to itself or others. |
| **Conditional Access Administrator** | Can create, modify, and delete Conditional Access and per-user MFA settings. Can be used to disable security policies, removing protection for all accounts, including Global Administrators, can block access to the tenant. |
| **Hybrid Identity Administrator** | Can manage federation settings, Entra Connect, and password hash sync. Can be abused to forge tokens for a federated domain and authenticate as a Global Admin. |
| **Partner Tier2 Support** | Can reset passwords for all users including administrators |
| **Security Administrator** | Can manage security features and read all tenant information. Has permissions equivalent to Conditional Access Admin, Domain Name Administrator, providing multiple paths to compromise. |
| **Domain Name Administrator** | Can manage domain names. Can add a new federated domain and forge SAML tokens to impersonate any user, including a Global Admin. |
| **Intune Administrator** | Can run scripts on managed devices. If a Global Administrator or other high-privilege admin is using an Intune-managed device, their tokens can be extracted. |
| **Privileged Authentication Admin** | Can view, set, and reset authentication methods for any user, including Global Administrators. |

_Table 3: High-Risk Roles in Entra ID_

### **Medium-Risk Roles**

|     |     |
| --- | --- |
| **Entra Role** | **Justification / Key Risk** |
| **Authentication Administrator** | Can view, set, and reset authentication methods (password and MFA) for any non-admin and some admin users. Can be used in a chain attack to take over a higher-privileged role. |
| **User Administrator** | Can manage all aspects of users and groups, including resetting passwords for most roles below Global Administrator. Can be used in a chain attack to take over a higher-privileged role. |
| **SharePoint Administrator** | Full control over a critical data repository (SharePoint and OneDrive) and manage Microsoft 365 groups. Can access sensitive data and impersonate users within the service. Indirect attack paths: can be used to add a compromised user to a non-role-assignable group with elevated permissions (e.g., groups assigned roles  on critical Azure resources, groups exempted from Conditional Access policies, or groups with high-privilege app permissions). |
| **Teams Administrator** | Full control over a critical communication and data service. |
| **Authentication Policy Admin** | Can configure authentication methods policy, MFA settings, and password protection policies tenant-wide. Can weaken security posture if misused. |
| **Azure Information Protection Admin** | Can manage protection policies in AIP. Can decrypt sensitive documents. |
| **Compliance Administrator** | Can manage compliance settings in the Purview portal, granting broad access to data and eDiscovery. |
| **Directory Synchronization Accounts** | Service account for Entra Connect. Can reset passwords for hybrid users, though recent controls have limited this risk. This is a high-value target. |
| **Global Reader** | Read-only access to everything a Global Administrator can see. Invaluable for reconnaissance and finding misconfigurations to exploit. |
| **Security Operator** | Read-only access to security services (Defender, Sentinel). Can manage security alerts. Essential for reconnaissance. |
| **License Administrator** | Can manage licenses. Can cause denial of service by unassigning business critical licenses from users. |
| **Password Administrator** | Same as Helpdesk Administrator. Can reset passwords for non-admins and some limited admins. |
| **Power Platform Administrator** | Can manage all aspects of Power Platform. Can create flows/apps that access sensitive data sources. |
| **Directory Writers** | Can read and write basic directory information and manage group memberships. Indirect attack paths: can be used to add a compromised user to a non-role-assignable group with elevated permissions (e.g., groups assigned roles  on critical Azure resources, groups exempted from Conditional Access policies, or groups with high-privilege app permissions). |
| **Groups Administrator** | Can manage all groups and their membership. Indirect attack paths: can be used to add a compromised user to a non-role-assignable group with elevated permissions (e.g., groups assigned roles  on critical Azure resources, groups exempted from Conditional Access policies, or groups with high-privilege app permissions). |
| **Exchange Administrator** | Full control over Exchange Online service. Additionally shares Directory Writers risk through the ability to manage distribution groups and mail-enabled security groups, which can be assigned Azure roles or used in access control policies. Can also access all mailboxes, read sensitive communications, and configure mail flow rules for data exfiltration. |
| **Helpdesk Administrator** | Can reset passwords for non-administrators and Helpdesk Administrators. Can be used in a chain attack to take over a higher-privileged role. |
| **Partner Tier1 Support** | Can reset passwords for non-administrators and update application credentials. |
| **Application Administrator** | Can register and manage all aspects of applications, including adding new credentials. Can be abused to add credentials to a highly privileged Service Principal (e.g., one with RoleManagement.ReadWrite.All) and escalate to Global Admin. |
| **Cloud Application Administrator** | Same risk path as Application Administrator. Can manage application credentials, leading to potential takeover of privileged applications. |
| **Windows 365 Administrator** | Can provision and manage all aspects of Windows 365 resources and manage security groups. Can deploy scripts to Cloud PCs to extract credentials or tokens, or be used to add a compromised user to a non-role-assignable group with elevated permissions (e.g., groups assigned roles  on critical Azure resources, groups exempted from Conditional Access policies, or groups with high-privilege app permissions). |
| **Yammer Administrator** | Manage all aspects of the Yammer service and manage Microsoft 365 groups. Indirect privileged escalation path: can be used to add a compromised user to a non-role-assignable group with elevated permissions (e.g., groups assigned roles  on critical Azure resources, groups exempted from Conditional Access policies, or groups with high-privilege app permissions). |
| **Password Administrator** | Can reset passwords for non-administrators and Password Administrators. Can be used in a chain attack to take over a higher-privileged role. |
| **Power Platform Administrator** | Can create and manage all aspects of Dynamics 365, Power Apps and Power Automate. |
| **Lifecycle Workflows Administrator** | Create and manage all aspects of workflows and tasks associated with Lifecycle Workflows in Entra ID. |
| **Identity Governance Administrator** | Manage access using Entra ID for identity governance scenarios. Can be used in a chain attack to take over a higher-privileged role. |

_Table 4: Medium-Risk Roles in Entra ID_

|     |     |
| --- | --- |
| **Other identities** | **Justification / Key Risk** |
| **Application Owner (only for privileged applications)** | This is not an Entra ID role, this is an identity assigned as owner of an application in Entra ID. Can manage application credentials. Same risk as Application Administrator (scoped to specific application). |
| **Azure DevOps Administrator** | Can manage all projects in Azure DevOps organization. Can impersonate pipelines that use privilege identities. |
| **Group Owner** | Can manage owned groups and their membership. Indirect attack paths: can be used to add a compromised user to the owned group with elevated permissions (e.g., groups assigned roles  on critical Azure resources, groups exempted from Conditional Access policies, or groups with high-privilege app permissions). |

_Table 5: Other Medium-Risk Roles_

### Low-Risk Roles

|     |     |
| --- | --- |
| **Entra Role** | **Justification / Key Risk** |
| **Application Developer** | Can create application registrations when users are not allowed to. Cannot grant consent or add credentials. |
| **Attribute Definition/Assignment/Log Reader/Admin** | Manages custom security attributes. Low risk unless these attributes are used for critical security decisions. |
| **Billing Administrator** | Manages billing and subscriptions. No access to data or resources. |
| **Cloud Device Administrator** | Can enable, disable, and delete devices in Entra ID but cannot manage their properties. |
| **Directory Readers** | Read basic directory info. Default permission for all member users. |
| **Message Center Reader** | Can read Message Center notifications, which may contain sensitive service change information. |
| **Reports Reader** | Can read sign-in and audit reports. Useful for reconnaissance but read-only. |
| **Teams Devices Administrator** | Manages Teams-certified devices. |
| **Viva Goals Administrator** | Manages Viva Goals. May have access to sensitive strategic information but not platform controls. |
| **Guest Inviter** | Can invite external users. Can be abused to invite malicious actors or exploit vulnerable dynamic groups. |
| **Security Reader** | Read-only access to security services (Defender, Sentinel). Can manage security alerts. Essential for reconnaissance. |
| **All other roles not listed** | This includes many service-specific or feature-specific roles with limited permissions (e.g., Attack Payload Author, Printer Technician, Teams Communications Support Engineer, User Experience Success Manager). |

_Table 6: Low-Risk Roles in Entra ID_

### 4.2 Azure Role Classification Matrix

The privilege of an Azure role is inseparable from its **scope**. An Owner of a single, non-critical VM is far less powerful than an Owner of the Root MG.

Any role with write/assignment permissions at the Root MG is high-risk because it controls the entire Azure resource hierarchy. An identity with Contributor role at this scope could destroy all resources.

Highly privileged roles (Owner, Contributor) on critical production assets are classified as medium-risk.

The same roles on isolated or non-critical business assets could be considered low-risk.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Azure Role** | **Tenant Root or equivalent MG** | **Business****-critical assets** | **Non-critical assets** | **Limited scope** |
| **Owner** | **High risk** | **Medium risk** | **Low risk** | **Low risk** |
| **Contributor** | **High risk** | **Medium risk** | **Low risk** | **Low risk** |
| **User Access Administrator** | **High risk** | **Medium risk** | **Low risk** | **Low risk** |
| **Role Based Access Control Administrator** | **High risk** | **Medium risk** | **Low risk** | **Low risk** |
| **Reader** | **Low risk** | **Low risk** | **Low risk** | **Low risk** |

_Table 7: Azure Role Classification Matrix_

For other Azure built-in roles that are specific to individual services, risk assessment based on criticality, scope and privilege is needed. For a full listing of available roles, refer to the official documentation available at: [https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles)

## 5\. Conclusion

This risk-based privileged framework is not a project; it is a foundational component of a continuous cloud security program. By moving from a flat security model to a risk-based hierarchy of **High, Medium, and Low** **risk**, organizations can apply the right level of protection to the right roles.

To ensure effective resource allocation and immediate risk reduction, organizations should prioritize the implementation of security controls starting with High-Risk roles, then proceeding to Medium-Risk roles, and finally addressing Low-Risk roles. This strategic, phased approach ensures that the most powerful identities are protected from abuse first, while not impeding the productivity of administrators with less critical roles. This proactive, defense-in-depth stance is an organization's strongest defense against the evolving landscape of identity-based attacks.

The cloud identity landscape is constantly changing, new roles are added and associated permissions are subject to evolve. This requires a periodic reassessment of the associated risks for the organization, and appropriate adjustment of security controls applied to the identities.

## Appendix - Glossary

**PAW (Privileged Access Workstation)**: A dedicated, physically isolated and locked-down physical device exclusively used for high-privilege administrative tasks. It should not be used for email, web browsing, or general productivity tasks.

**SAW (Secure Admin Workstation)**: A dedicated and locked-down virtual machine (e.g., using Azure Virtual Desktop) used for medium-risk administrative tasks. It provides session isolation to protect administrative activities.

**Phishing-resistant MFA**: A multi-factor authentication method that cannot be bypassed through  credential phishing attacks. Examples include FIDO2 Security Keys and Windows Hello for Business.

**Break-glass account:** A break-glass account is a highly privileged user account used only in critical emergencies when standard administrative access is unavailable. It serves as a last-resort method to regain control of a system, for instance, during a major outage, security incident, or if other admin accounts are locked out. Due to its powerful permissions, its use is heavily monitored, audited, and triggers immediate alerts.

**Workload Identity Federation:** A modern method for allowing a software workload, like an application in one cloud, to access resources in another cloud or on-premise system without using long-lived secret keys. It works by establishing a trust relationship between two identity providers, allowing the workload to exchange a short-lived token from its native environment for temporary credentials in the target environment. This keyless approach significantly improves security by eliminating the risk of static credentials being stolen or leaked.

- [Cloud Security](https://security.googlecloudcommunity.com/search?q=Cloud%20Security&search_type=tag)
- [Identity](https://security.googlecloudcommunity.com/search?q=Identity&search_type=tag)
- [Identity & Access Management](https://security.googlecloudcommunity.com/search?q=Identity%20%26%20Access%20Management&search_type=tag)

[![yuri](https://uploads-us-west-2.insided.com/securitygooglecloud-en/icon/200x200/84c1506d-3536-4ad6-ad18-66219024e41c.png)](https://security.googlecloudcommunity.com/members/yuri-422761)

[![Corne](https://uploads-us-west-2.insided.com/securitygooglecloud-en/icon/200x200/e29f30d0-c52e-4dba-849a-b24569764cfc.png)](https://security.googlecloudcommunity.com/members/corne-423148)

[![jupave](https://uploads-us-west-2.insided.com/securitygooglecloud-en/icon/200x200/d24a9dde-9fb8-4093-8baf-308af4e99240.png)](https://security.googlecloudcommunity.com/members/jupave-423282)

4 people like this

- [![yuri](https://uploads-us-west-2.insided.com/securitygooglecloud-en/icon/200x200/84c1506d-3536-4ad6-ad18-66219024e41c.png)](https://security.googlecloudcommunity.com/members/yuri-422761)


yuri
- [![Corne](https://uploads-us-west-2.insided.com/securitygooglecloud-en/icon/200x200/e29f30d0-c52e-4dba-849a-b24569764cfc.png)](https://security.googlecloudcommunity.com/members/corne-423148)


Corne
- [![jupave](https://uploads-us-west-2.insided.com/securitygooglecloud-en/icon/200x200/d24a9dde-9fb8-4093-8baf-308af4e99240.png)](https://security.googlecloudcommunity.com/members/jupave-423282)


jupave
- [![Wally.Hass](https://uploads-us-west-2.insided.com/securitygooglecloud-en/icon/200x200/7859313f-daca-4dbd-9aa9-30f3d6f328a5.png)](https://security.googlecloudcommunity.com/members/wally-hass-423284)


Wally.Hass

- [Like](https://security.googlecloudcommunity.com/community-blog-42/whitepaper-securing-identities-in-the-microsoft-cloud-6077#)
- [Quote](https://security.googlecloudcommunity.com/community-blog-42/whitepaper-securing-identities-in-the-microsoft-cloud-6077#)
- Subscribe
- Share


Did this topic help you find an answer to your question?

Be the first to reply!

### Reply

Rich Text Editor, editor1

Editor toolbarsStylesStylesStylesBoldKeyboard shortcut Ctrl+BItalicKeyboard shortcut Ctrl+IUnderlineKeyboard shortcut Ctrl+UStrikethroughKeyboard shortcut Ctrl+Shift+XText ColorBackground ColorBullet listNumbered listAlign LeftCenterAlign RightEmojiInsert linkKeyboard shortcut Ctrl+KInsert imageQuoteInsert Media EmbedInsert Code SnippetSpoilerInsertTableMore

Press ALT 0 for help

Rich Text Editor, editor1Add as many details as possible, by providing details you’ll make it easier for others to reply

Send

[Powered by Gainsight](https://www.gainsight.com/customer-communities/ "Visit Gainsight.com")

[Terms & Conditions](https://security.googlecloudcommunity.com/site/terms) [Cookie settings](https://security.googlecloudcommunity.com/community-blog-42/whitepaper-securing-identities-in-the-microsoft-cloud-6077#) [Accessibility statement](https://www.gainsight.com/policy/accessibility-cc/)

[Create topic](https://security.googlecloudcommunity.com/topic/new)

## Sign up

Already have an account? Login

#### Login with SSO

[![](https://dowpznhhyvkm4.cloudfront.net/2025-11-07-18-05-27-ff3b54926a/dist/images/g-logo.png)\\
\\
Google login](https://security.googlecloudcommunity.com/ssoproxy/login?ssoType=google)

or

Username


\\*

E-mail address


\\*

First Name




Last Name




Company


\\*

Job Title




Product of Interest




SecOps



Google Threat Intelligence



Security Command Center



reCAPTCHA



Other




Country




Password


\\*

I accept the [terms of use](https://policies.google.com/terms)

loginBox.register.email\_repeat




Register


## Login to the community

No account yet? Create an account

#### Login with SSO

[![](https://dowpznhhyvkm4.cloudfront.net/2025-11-07-18-05-27-ff3b54926a/dist/images/g-logo.png)\\
\\
Google login](https://security.googlecloudcommunity.com/ssoproxy/login?ssoType=google)

or

Username or Email




Password




Remember me


Log in


[Forgot password?](https://security.googlecloudcommunity.com/community-blog-42/whitepaper-securing-identities-in-the-microsoft-cloud-6077#)

Enter your E-mail address. We'll send you an e-mail with instructions to reset your password.

Enter your e-mail address




Send


[Back to overview](https://security.googlecloudcommunity.com/community-blog-42/whitepaper-securing-identities-in-the-microsoft-cloud-6077#)

## Scanning file for viruses.

Sorry, we're still checking this file's contents to make sure it's safe to download. Please try again in a few minutes.

[OK](https://security.googlecloudcommunity.com/community-blog-42/whitepaper-securing-identities-in-the-microsoft-cloud-6077#)

## This file cannot be downloaded

Sorry, our virus scanner detected that this file isn't safe to download.

[OK](https://security.googlecloudcommunity.com/community-blog-42/whitepaper-securing-identities-in-the-microsoft-cloud-6077#)

### Cookie Policy

This site uses [cookies](https://policies.google.com/technologies/cookies) to deliver and enhance the quality of its services and to analyze traffic. If you agree, cookies are also used to serve advertising and to personalize the content and advertisements that you see.

Accept cookiesDeny All

Cookie settings

×

### Cookie settings

When you visit any website, your information is stored or retrieved on the browser, through cookies. The website uses this information to give you a personalized experience. You could choose not to store certain information. Blocking some types of cookies might impact your site experience and the services we offer. Click the different category headings to learn more. We need basic cookies to make this site work, therefore these are the minimum you can select. [Learn more about our cookies.](https://policies.google.com/technologies/cookies)

Strictly Necessary Cookies (Always Active)

Performance Cookies

Functional Cookies

Accept cookies

[Privacy Policy](https://policies.google.com/privacy) [Terms of Service](https://policies.google.com/terms) [Gen AI Policy](https://policies.google.com/terms/generative-ai/use-policy) [Community Guidelines](https://security.googlecloudcommunity.com/p/community-guidelines) [Cookie Settings](https://security.googlecloudcommunity.com/community-blog-42/whitepaper-securing-identities-in-the-microsoft-cloud-6077#)

© 2025 Google. All rights reserved.
