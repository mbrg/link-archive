---
title: "Understanding Tokens in Microsoft Entra ID - Microsoft Entra ID ◆ Microsoft Learn"
tags:
   - cybersecurity
   - conditional access
   - authentication
   - token security
   - Microsoft Entra ID
link: https://learn.microsoft.com/en-us/entra/identity/devices/concept-tokens-microsoft-entra-id
date: 2025-05-03
description: "Microsoft Entra ID outlines critical strategies to mitigate token theft risks as sophisticated attack vectors evolve. Key recommendations include deploying phishing-resistant MFA, hardening devices against malware, and enforcing device-bound tokens. Tokens, essential for authentication, must be managed with a defense-in-depth approach, prioritizing the protection of sign-in session tokens due to their longevity. The increased occurrence of adversary-in-the-middle (AiTM) attacks underscores the necessity for organizations to secure token management practices. Continuous access evaluation and minimized token exposure are imperative to thwart unauthorized access and data exfiltration."
---

Table of contents Exit focus mode

Ask LearnAsk Learn[Read in English](https://learn.microsoft.com/en-us/entra/identity/devices/concept-tokens-microsoft-entra-id "Read in English")Save

- Add to Collections
- Add to plan

[Edit This Document](https://github.com/MicrosoftDocs/entra-docs/blob/main/docs/identity/devices/concept-tokens-microsoft-entra-id.md "Edit This Document")

Table of contents[Read in English](https://learn.microsoft.com/en-us/entra/identity/devices/concept-tokens-microsoft-entra-id "Read in English")Add to CollectionsAdd to plan[Edit](https://github.com/MicrosoftDocs/entra-docs/blob/main/docs/identity/devices/concept-tokens-microsoft-entra-id.md "Edit This Document")

* * *

#### Share via

[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fentra%2Fidentity%2Fdevices%2Fconcept-tokens-microsoft-entra-id%3FWT.mc_id%3Dfacebook) [x.com](https://twitter.com/intent/tweet?original_referer=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fentra%2Fidentity%2Fdevices%2Fconcept-tokens-microsoft-entra-id%3FWT.mc_id%3Dtwitter&text=Today%20I%20completed%20%22Understanding%20Tokens%20in%20Microsoft%20Entra%20ID%20-%20Microsoft%20Entra%20ID%20%7C%20Microsoft%20Learn%22!%20I%27m%20so%20proud%20to%20be%20celebrating%20this%20achievement%20and%20hope%20this%20inspires%20you%20to%20start%20your%20own%20%40MicrosoftLearn%20journey!&tw_p=tweetbutton&url=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fentra%2Fidentity%2Fdevices%2Fconcept-tokens-microsoft-entra-id%3FWT.mc_id%3Dtwitter) [LinkedIn](https://www.linkedin.com/feed/?shareActive=true&text=Today%20I%20completed%20%22Understanding%20Tokens%20in%20Microsoft%20Entra%20ID%20-%20Microsoft%20Entra%20ID%20%7C%20Microsoft%20Learn%22!%20I%27m%20so%20proud%20to%20be%20celebrating%20this%20achievement%20and%20hope%20this%20inspires%20you%20to%20start%20your%20own%20%40MicrosoftLearn%20journey!%0A%0D%0Ahttps%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fentra%2Fidentity%2Fdevices%2Fconcept-tokens-microsoft-entra-id%3FWT.mc_id%3Dlinkedin) [Email](mailto:?subject=%5BShared%20Article%5D%20Understanding%20Tokens%20in%20Microsoft%20Entra%20ID%20-%20Microsoft%20Entra%20ID%20%7C%20Microsoft%20Learn&body=Today%20I%20completed%20%22Understanding%20Tokens%20in%20Microsoft%20Entra%20ID%20-%20Microsoft%20Entra%20ID%20%7C%20Microsoft%20Learn%22!%20I'm%20so%20proud%20to%20be%20celebrating%20this%20achievement%20and%20hope%20this%20inspires%20you%20to%20start%20your%20own%20%40MicrosoftLearn%20journey!%0A%0D%0Ahttps%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fentra%2Fidentity%2Fdevices%2Fconcept-tokens-microsoft-entra-id%3FWT.mc_id%3Demail)

* * *

Print

* * *

Note

Access to this page requires authorization. You can try [signing in](https://learn.microsoft.com/en-us/entra/identity/devices/concept-tokens-microsoft-entra-id#) or changing directories.


Access to this page requires authorization. You can try changing directories.


# Understanding tokens in Microsoft Entra ID

- Article
- 04/30/2025
- 2 contributors


Feedback

As attackers increasingly use sophisticated attacks, it's crucial to guard against data exfiltration by hardening your environment against token theft and token replay. Although challenging, there are simple steps you can take to reduce your attack surface and increase the cost for attackers to successfully steal and replay tokens. A robust strategy to protect your tokens requires a multi-layered defense-in-depth approach, which should include:

- Deploying phishing-resistant credentials
- Hardening your devices against malware-based attacks
- Using Device-based and Risk-based Conditional Access
- Enforcing device-bound tokens where possible
- Implementing network-based enforcements

This document summarizes the basics of what tokens are, how tokens are stolen, and provide concrete steps you can take to mitigate the risk of successful attacks in your environment. Due to the complexity and wide variety of tokens in Microsoft Entra, some topics are generalized for simplicity and may not cover all edge cases. However, this guidance covers most scenarios for public clients. [Confidential client](https://learn.microsoft.com/en-us/entra/identity-platform/msal-client-applications#public-client-and-confidential-client-authorization) scenarios aren't in scope.

Password-based attacks still comprise over 99% of attacks seen by Microsoft and are the root cause of most compromised identities. Organizations should deploy phishing-resistant MFA as a frontline of defense for their identities. Doing so forces adversaries to adjust their tactics, moving to the next logical attack vector, which is likely token theft. “Although token theft results in far fewer identity compromises than password attacks, our detections indicate incidents have grown to an estimated 39,000 per day. Moreover, over the last year we’ve seen a 146% rise in AiTM phishing attacks, which occur when attackers trick users into clicking a link and completing MFA on the attacker’s behalf.”\* While the deployment of phishing-resistant MFA should be a top priority, organizations should also begin preparing a token theft mitigation strategy as token theft attack vectors continue to increase over time. Protecting against token theft becomes more important as password-based attacks become less viable.

_\\* From [2024 Microsoft Digital Defense Report](https://aka.ms/mddr) (page 40)_

[Section titled: What is a token?](https://learn.microsoft.com/en-us/entra/identity/devices/concept-tokens-microsoft-entra-id#what-is-a-token)

## What is a token?

Tokens are digital objects used in various authentication and authorization processes to grant access to resources. They verify the identity of a user or a workload and grant access to resources without requiring the transmission of a password or credential for each transaction. Tokens encapsulate information about the user's identity and their permissions in a secure format, ensuring that sensitive information remains protected during the authentication process.

In digital environments, tokens play a critical role in enhancing security by enabling secure and efficient authentication mechanisms. They help reduce the risk of credential theft by minimizing the exposure of credentials over the network. However, they have the characteristic that if the device or network is compromised, they can be exfiltrated by an attacker. The attacker can then use these tokens to gain access to resources as the signed-in user.

[Section titled: Summary of the kinds of tokens](https://learn.microsoft.com/en-us/entra/identity/devices/concept-tokens-microsoft-entra-id#summary-of-the-kinds-of-tokens)

## Summary of the kinds of tokens

There are many kinds of tokens, but they generally fall into one of two categories:

- **Sign-in sessions** – These tokens maintain the signed-in state of a user, allowing the user to access resources without the need for frequent reauthentication. They're passed to the identity provider to request tokens that are in the app session category. They're also known as Refresh Tokens in the OAuth 2.0 standard.
- **App sessions** – These tokens authorize access to specific applications. They're short-lived and are played between the client and the application. They're also known as Access Tokens in the OAuth 2.0 standard.

Tokens may also vary depending on the client application. Web applications accessed via browsers sometimes use different kinds of tokens compared with native apps such as Outlook and Teams.

![Screenshot of tokens evaluated by Microsoft Entra ID and other applications and services.](https://learn.microsoft.com/en-us/entra/identity/devices/media/concept-tokens-microsoft-entra-id/tokens-evaluated-by-microsoft-entra-id.png)

As a best practice, you want to prioritize protecting your sign-in session tokens first as these tokens can last for weeks or months, potentially enabling persistent unauthorized access if stolen.

Another difference between the two token families: Sign-in session tokens are revocable by design while app sessions are typically not. For example, Entra ID Access Tokens can only be revoked if the application has integrated Continuous Access Evaluation.

Expand table

| Token Type | Issued by | Purpose | Scoped to Resource | Lifetime | Revocable | Renewable |
| --- | --- | --- | --- | --- | --- | --- |
| Primary Refresh Token (PRT) | Entra ID | Request Access Tokens | No – Can request an access token for any resource | 14 days\* | Yes | Yes |
| Refresh Token | Entra ID | Request Access Tokens | Yes | 90 days\* | Yes | Yes |
| Access Token | Entra ID | Access the resource | Yes | Variable 60-90 minutes | Yes, if CAE capable | No |
| App auth cookie | Web app | Access the resource | Yes | Determined by application | Depends on application | No |

\*Rolling window – Lifetime is restarted with every use of the token.

[Section titled: Token theft attack vectors](https://learn.microsoft.com/en-us/entra/identity/devices/concept-tokens-microsoft-entra-id#token-theft-attack-vectors)

## Token theft attack vectors

Adversaries can employ many different attack vectors to steal tokens. Once a token is stolen, the adversary can then impersonate the user, gaining unauthorized access and even exfiltrating sensitive data.
Some examples of these attack vectors include:

- **Adversary-in-the-middle**: A sophisticated form of a Man-in-the-Middle (MitM) attack. In this scenario, an attacker positions themselves between two communicating parties, intercepting and potentially altering the communication without either party's knowledge. This scenario allows the attacker to capture sensitive information such as credentials, session cookies, and other data, even bypassing security measures like multifactor authentication. Learn more about [Adversary-in-the-middle phishing attacks](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/defeating-adversary-in-the-middle-phishing-attacks/1751777).
- **Malware**: Malware can steal tokens from a device by infiltrating the system and monitoring network traffic or accessing stored data. Once installed, the malware can capture authentication tokens, session cookies, or other credentials by intercepting communications between the device and legitimate services. It can also exploit vulnerabilities to extract tokens directly from memory or storage.

In this article, we focus primarily on how to defeat attacks that are directed towards end users, such as those previously listed. Attack vectors such as server-side or application compromise are out of scope for this article. To mitigate these kinds of attacks, organizations should follow the general best practices of:

- Secure your application’s authentication
- Ensure application permissions are least privileged
- Avoid capture and retention of tokens in server-side logs
- Monitor OAuth applications with permissions to other resources for compromise

[Section titled: Next steps](https://learn.microsoft.com/en-us/entra/identity/devices/concept-tokens-microsoft-entra-id#next-steps)

## Next steps

To understand how to protect tokens in Microsoft Entra ID, continue to [Protecting tokens in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/devices/protecting-tokens-microsoft-entra-id).

* * *

## Feedback

Was this page helpful?


YesNo

[Provide product feedback](https://feedback.azure.com/d365community/forum/22920db1-ad25-ec11-b6e6-000d3a4f0789)

* * *

## Additional resources

* * *

Events


[Join AI Skills Fest Challenge](https://aka.ms/AISkillsFest_LearnT2_TechChallenges)

Apr 8, 6 AM - May 27, 10 PM


Sharpen your AI skills and enter the sweepstakes to win a free Certification exam


[Register now!](https://aka.ms/AISkillsFest_LearnT2_TechChallenges)
