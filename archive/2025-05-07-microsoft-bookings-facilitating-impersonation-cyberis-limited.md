---
title: "Microsoft Bookings – Facilitating Impersonation | Cyberis Limited"
tags:
   - accountimpersonation
   - securitybestpractices
   - MicrosoftBookings
   - phishing
   - cybersecurity
link: https://www.cyberis.com/article/microsoft-bookings-facilitating-impersonation
date: 2025-05-07
description: "Microsoft Bookings allows end users to create accounts in Entra, introducing significant security vulnerabilities. Attackers can leverage this feature to produce impersonation email accounts, allowing for phishing attacks under the guise of legitimate users, potentially even mimicking high-profile executives. They can also hijack dormant accounts linked to ex-employees, create functional mailboxes without consuming licenses, and exploit these for malicious purposes like domain validation. To mitigate these risks, organizations are advised to audit shared Bookings pages, disable user access unless necessary, and monitor account creation activities within Entra."
---

[Skip to main content](https://www.cyberis.com/article/microsoft-bookings-facilitating-impersonation#main-content)

**TL;DR:** Allowing end users to create accounts in Entra, as Microsoft Bookings does by default, poses significant security risks. An attacker could potentially:

- Purchase TLS certificates or transfer domain names and services relying on email verification (e.g., [AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/email-validation.html), Facebook/Meta Business Manager, [Cloudflare](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/email/)).
- Impersonate high-profile individuals to conduct phishing attacks on internal and external users.
- Hijack dormant accounts previously associated with former employees.

* * *

## The Issue

Microsoft Bookings includes a feature to create “ [Shared Booking Pages](https://learn.microsoft.com/en-us/microsoft-365/bookings/bookings-faq),” enabled by default for users assigned an appropriate Microsoft 365 licence. To check if you’re licensed, visit [Bookings in Outlook](https://outlook.office.com/bookings/).

![Bookings page](https://www.cyberis.com/files/inline-images/image_2.png)_Figure 1 - The option to create a shared Bookings page_

Behind the scenes, the feature operates in a way that could make it very useful for adversaries who have compromised the Microsoft 365 account of a user in an organisation.

Imagine a scenario where an adversary has phished a Microsoft 365 user and gained access to their account.  In most business email compromise situations, the attacker may well communicate with internal and external parties using the identity of the compromised user, and will use information from existing email communications to try to gain financial advantage or improve their positioning on the network.  Depending on which user has been compromised, this can be impactful, but often the compromised user may have limited rights or power in the business.

Where Shared Bookings pages are enabled, the adversary suddenly has better options available to them.  Using the features in the Shared Bookings pages, the attacker can create a very convincing impersonation of another identity in the compromised tenant and use this to good effect.  For example, having compromised a low privileged worker, they may be able to create an internal email address that convincingly impersonates the CEO and can then email other members of staff passing instructions for the transfer of funds, bypassing impersonation filters.  There's also the potential for an adversary to create "special" email addresses inside the domain (think "admin@" or "hostmaster@") which might allow for very convincing social engineering of external parties aimed at the transfer of infrastructure control.

The impact of misuse of these features is difficult to quantify and will depend on circumstances, but as with all features, leaving this functionality enabled when it's not required expands your attack surface area; if you're not using Shared Bookings, disabling this feature is recommended.

For a step-by-step breakdown of the "weaknesses" see below.

## Security Weaknesses

#### 1\. Unauthorised Account Creation

When a user creates a shared Booking page, it generates a fully-fledged account in Entra—created by an end user without administrative permissions.

The account:

- **Display Name**: Matches the Booking page name.
- **Email Address**: Formed by removing spaces (e.g., a page named "Firstname Surname" creates `FirstnameSurname@<tenantdefaultmaildomain>`).
- The account can **send and receive emails**, regardless of sharing settings.

An attacker could impersonate legitimate users by:

1. Creating a Booking page named after a target (e.g., "Geoff Jones").
2. This automatically creates a mailbox with the space removed - `geoffjones@cyberis.com` \- that mimics the legitimate address `geoff.jones@cyberis.com`.
3. Adding a profile image or email signature identical to the target (referred to as a 'logo' when creating the page).

This makes internal phishing (i.e. from an account that has been compromised) and lateral movement attacks significantly easier and harder to detect.  These attacks would bypass Microsoft's impersonation detection mechanisms, as they would be coming from a legitimate Exchange mailbox.

![Side by side comparison of a genuine email vs an impersonated email](https://www.cyberis.com/files/inline-images/sidebyside.png)_Figure 2 - Side by side comparison of a genuine email vs an impersonated email from a shared Bookings page_

#### 2\. Mailbox Access and Delegation

The mailbox associated with the Booking page:

- Is fully functional, allowing the user to **send emails internally and externally**.
- Automatically forwards emails to the creator of the page (but this can be turned off in the mailbox).
- Can be accessed by the user that created the shared Bookings page (or anybody with access to that shared Bookings page) via Outlook Web App (OWA) under "Open another mailbox".

![Open mailbox function](https://www.cyberis.com/files/inline-images/openmailbox.png)_Figure 3 - 'Opening another mailbox'_

An attacker could exploit this to impersonate a CEO, manager, or finance department and send outbound emails.  An attacker for example could target customers to redirect payments to their own bank account by impersonating legitimate businesses invoices.

#### 3\. Email Address Hijacking

It is possible to create Booking pages matching email addresses of former employees.

For instance:

- A malicious user could create a Booking page for "Joe Bloggs" (a former employee).
- They would then receive all inbound mail for `joebloggs@cyberis.com`.
- This could allow:
  - Resetting passwords for external services tied to the email.
  - Verifying domain ownership for SSL certificates ( [AWS ACM email validation](https://docs.aws.amazon.com/acm/latest/userguide/email-validation.html)).

#### 4\. Licence-Free Mailboxes

Creating shared Booking pages provides a hidden, fully functional mailbox that does not consume a Microsoft 365 licence.

Steps:

1. Create a Booking page and reset the associated password in Entra (would require admin privileges).
2. Sign in at [Outlook Web](https://outlook.office.com/).

The mailbox:

- Functions like a standard 50GB Exchange Online mailbox.
- Remains invisible in the Exchange Admin Center but detectable via PowerShell modules.

* * *

## How to Detect and Mitigate

We recommend the following steps to identify and address the issue:

#### 1\. Audit Shared Bookings Pages

Use ExchangeOnline PowerShell to identify hidden mailboxes created by shared Booking pages.

```plaintext hljs plaintext
PS C:\Users\user> Get-Mailbox
```

![](https://www.cyberis.com/files/inline-images/image_1.png)

#### 2\. Restrict Bookings Access

Disable the ability for end users to create shared Booking pages unless absolutely necessary.

```plaintext hljs plaintext
PS C:\Users\user> Connect-ExchangeOnline
PS C:\Users\user> set-OrganizationConfig -BookingsEnabled $false
```

#### 3\. Monitor Entra Accounts

Set up alerts for unusual account creation activity.

#### 4\. Review and Revoke Permissions

Regularly audit mailbox permissions for and remove unnecessary delegate access.

#### 5\. Ensure High-Value Email Addresses are Secured

To mitigate risks of email impersonation and hijacking, ensure that high-value email addresses commonly used for domain or service validation are claimed and associated with an administrator-controlled account in your tenant. Examples of these addresses include:

```plaintext hljs plaintext
administrator@your_domain_name
hostmaster@your_domain_name
postmaster@your_domain_name
webmaster@your_domain_name
admin@your_domain_name
root@your_domain_name
```

## Disclosure

At Cyberis, we take a proactive approach to identifying security vulnerabilities that could impact organisations using widely adopted tools like Microsoft Bookings. These findings highlight the importance of rigorous security configuration and monitoring within your Microsoft 365 environment.

If you need assistance mitigating risks or enhancing your organisation's security posture, please get in touch with our team.

## Improve your security

Our experienced team will identify and address your most critical information security concerns.

[Contact us](https://www.cyberis.com/contact-us "") [About Cyberis](https://www.cyberis.com/about-us "")
