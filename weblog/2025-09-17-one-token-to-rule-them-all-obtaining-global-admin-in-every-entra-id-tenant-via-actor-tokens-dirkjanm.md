---
date: '2025-09-17'
description: A critical vulnerability in Microsoft Entra ID (CVE-2025-55241) leveraged
  undocumented Actor tokens, allowing attackers to impersonate users across tenants
  due to inadequate validation in the Azure AD Graph API. This flaw permitted complete
  access to all Entra ID tenant data, including global admin functionality, without
  generating logs. Mitigations have been implemented to restrict Actor token use for
  external applications, but the legacy design raises ongoing security concerns. Attackers
  could exploit this to access or modify tenant settings seamlessly, underscoring
  the urgency for enhanced security controls and logging mechanisms in identity management
  systems.
link: /archive/2025-09-17-one-token-to-rule-them-all-obtaining-global-admin-in-every-entra-id-tenant-via-actor-tokens-dirkjanm
tags:
- actor tokens
- Azure AD Graph API
- Entra ID
- vulnerability disclosure
- cross-tenant access
- weblog
title: One Token to rule them all - obtaining Global Admin in every Entra ID tenant
  via Actor tokens - dirkjanm.io
type: weblog
---

This goes to show that a single person can do APT-level stuff with talent and dedicated. This mist be investigated further, this entire hidden mechanism still exists and is putting us all at a huge risk.

---

> Effectively this means that with a token I requested in my lab tenant I could authenticate as _any user_, including Global Admins, in _any other tenant_. Because of the nature of these Actor tokens, they are not subject to security policies like Conditional Access, which means there was no setting that could have mitigated this for specific hardened tenants. Since the Azure AD Graph API is an older API for managing the core Azure AD / Entra ID service, access to this API could have been used to make any modification in the tenant that Global Admins can do, including taking over or creating new identities and granting them any permission in the tenant. With these compromised identities the access could also be extended to Microsoft 365 and Azure.

APT-level results.

---

> These tokens allowed full access to the Azure AD Graph API in any tenant. Requesting Actor tokens does not generate logs. Even if it did they would be generated in my tenant instead of in the victim tenant, which means there is no record of the existence of these tokens.

No logs when random Microsoft internal services auth to your tenant.

---

> Based on Microsoft’s internal telemetry, they did not detect any abuse of this vulnerability. If you want to search for possible abuse artifacts in your own environment, a KQL detection is included at the end of this post.

I'd argue that the fact that this mechanism *exists* as it is is in and off itself an abuse. By Microsoft.

---

> When using this Actor token, Exchange would embed this in an **unsigned** JWT that is then sent to the resource provider, in this case the Azure AD graph. In the rest of the blog I call these **impersonation tokens** since they are used to impersonate users.

Unsigned???

---

> The `sip`, `smtp`, `upn` fields are used when accessing resources in Exchange online or SharePoint, but are ignored when talking to the Azure AD Graph, which only cares about the `nameid`. This `nameid` originates from an attribute of the user that is called the `netId` on the Azure AD Graph. You will also see it reflected in tokens issued to users, in the `puid` claim, which stands for Passport UID. I believe these identifiers are an artifact from the original codebase which Microsoft used for its Microsoft Accounts (consumer accounts or MSA). They are still used in Entra ID, for example to map guest users to the original identity in their home tenant.

This blend of corp and personal identity is the source of many evils with AAD

---

> - There are no logs when Actor tokens are issued. - Since these services can craft the unsigned impersonation tokens without talking to Entra ID, there are also no logs when they are created or used. - They cannot be revoked within their 24 hours validity. - They completely bypass any restrictions configured in Conditional Access. - We have to rely on logging from the resource provider to even know these tokens were used in the tenant.

More work for the CSRB right here

