---
title: "3rd party authorizations/oAuth/NHI/Agents"
tags:
   - Security Protocols
   - Third-Party Authorization
   - Machine-to-Machine Security
   - Identity Management
   - OAuth 2.0
link: https://www.linkedin.com/pulse/3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac/
date: 2025-07-20
summary: "JPMC's recent CISO letter emphasizes the critical security gaps within third-party authentication protocols, highlighting the vulnerabilities of long-lived OAuth 2.0 tokens in machine-to-machine integrations. These unmanaged tokens present significant risks, including lateral movement opportunities for attackers. Okta's proposed IPSIE standard aims to centralize authorization management across applications, improving visibility and governance. The call for a unified identity ecosystem is further underscored by the rise of AI agents, necessitating robust security practices surrounding machine identities. Okta's efforts catalyze an industry shift towards standardized, central control of identity and access management."
---

Agree & Join LinkedIn


By clicking Continue to join or sign in, you agree to LinkedIn’s [User Agreement](https://www.linkedin.com/legal/user-agreement?trk=linkedin-tc_auth-button_user-agreement), [Privacy Policy](https://www.linkedin.com/legal/privacy-policy?trk=linkedin-tc_auth-button_privacy-policy), and [Cookie Policy](https://www.linkedin.com/legal/cookie-policy?trk=linkedin-tc_auth-button_cookie-policy).


``````[Skip to main content](https://www.linkedin.com/pulse/3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac/#main-content)

``````

![3rd party authorizations/oAuth/NHI/Agents](https://media.licdn.com/dms/image/v2/D5612AQF4T8kIHZlmRQ/article-cover_image-shrink_720_1280/B56Zay7gsZGsAI-/0/1746758667457?e=2147483647&v=beta&t=WVVWCoQHiwFUc151g0KNr1rZ0zA0v9h9vBejBAXWH6Q)

Video: [https://youtu.be/xzr\_z\_rx\_Mw](https://youtu.be/xzr_z_rx_Mw)

Overview:

1.    The JPMC CISO Letter as a Catalyst:

- The conversation is framed around a recent letter from the CISO of JPMC, described by Harish Peri as a "bomb in industry."
- The letter validates Okta's existing concerns regarding third-party supplier security and authentication protocols, particularly as digital chains become "more and more expansive."
- The letter highlights a "big problem" related to authentication protocols in third-party supply chains.
- Peri states, "I loved it... because it was great to hear, you know, the CISO of one of the world's largest and probably one of the most complex organizations... really echo back the thing that's been top of mind for us."

2.    Identity as an Integration and Orchestration Issue:

- Identity is fundamentally an integration issue, orchestrating identities across various systems (e.g., Microsoft AD).
- The ideal state involves a "one golden record" for identity that is then orchestrated, avoiding "multiple silos, multiple ids."
- Okta's initial focus on single sign-on (SSO) is described as a form of orchestration, connecting an identity source like AD to a SAS app.
- The current challenge involves orchestrating identities and access between multiple apps ("going from like a SAS to another apps").

3.    The Critical Difference Between OAuth 1.0 and OAuth 2.0 and Associated Risks:

- OAuth 1.0: Designed for human authentication into an app ("basically between a person and a technology"). Simple and focused on user access grants.
- OAuth 2.0: A framework for machine-to-machine authorization ("authorizing another app to access another app or resource on my behalf"). This can also include "AI agents."
- The Problem: The machine-to-machine nature of OAuth 2.0, while enabling seamless integration, can lead to significant security risks:
- Long-lived, unmanaged tokens: These tokens are essentially "the master key to every part of the organization."
- Improper token management: Tokens can be "hardcoded or put into configuration files or something in plain text even that can be accessed."
- Lateral Movement: Attackers seek to gain access, "escalate privilege," and then "laterally mov\[e\] around the organization." Long-lived, unmanaged tokens are a "gold mine" for this.
- The drive for ease of customer experience and rapid innovation in app development has often led to security being overlooked in the implementation of machine-to-machine access.
- The JPMC letter highlights the lack of visibility into "what level of privilege that connection allows," "how long that token is living," and "who has access to it." This bypasses traditional security controls like "access management, identity governance and privilege access."
- Harish Peri states: "That right there is what we believe is probably the biggest security gap in our industry right now."
- He adds: "the security side of it is not being thought of with as much diligence as it should."

4.    The Importance of Authorization and Cross-App Authorization:

- Beyond authentication (logging in), authorization (what you can do) is a significant challenge, particularly in third-party applications.
- Different apps have different controls and authorization models, making it difficult to consistently manage access.
- There is a tendency for authorization logic to be implemented directly within individual SaaS applications.
- Okta's Vision (IPS): Okta is working with the Open ID Foundation and other identity providers on a future standard called IPSIE (Interoperable Profile for Secure Identity in the Enterprise).
- The core idea of IPSIE is that no SaaS application should directly implement authorization or authentication logic. Instead, they should "expos\[e\] capabilities such that a platform like Okta can handle that."
- This is because authorization is a "very specialized function" that most app builders lack the expertise to do comprehensively and securely.
- IPSIE will encapsulate SSO, MFA, exposing entitlements and life cycle management, sharing risk signals, and supporting session termination.
- This standard will provide CISOs with "complete visibility" and the ability to take actions like "terminating the session to prevent lateral movement."
- Cross-App Authorization: A key emerging pattern where authorization logic is outsourced to a centralized identity provider. This provides a "single control plane" to manage access across applications.
- Harish Peri emphasizes: "as a security professional, you have a single control plane to see everything. Who's logging in? How are they logging in? What do they have access to? Is that access happening the right way? Are they breaking authorization patterns?"
- This becomes even more critical with the deployment of "enterprise AI agents."

5.    Timeline and Adoption of IPSIE:

- Okta is actively building tooling for both ISVs (app builders) to adopt the standard and for Okta's platform to consume it.
- For Okta customers, the ability to consume the standard and gain visibility/control across apps is being built into the platform.
- The longer-term challenge is getting ISVs to adopt the standard, which is an "industry transformation" requiring "behavior change" and "code change."
- Okta is pursuing a "two-pronged approach": pushing the open standard (IPSIE) and working with major SAS ISVs to have "secure identity integrations pre-built into their applications." This aims to provide an "adrenaline boost to the whole ecosystem."
- This echoes Okta's efforts in driving industry adoption of SAML 15 years ago.
- Okta is actively working to convince SAS builders (e.g., at events like SaaStr) that adopting identity security standards is essential for their long-term viability.

6.    Addressing Current State Issues (Visibility and Control):

## Recommended by LinkedIn

[![How to Leverage Microsoft Purview Data Loss Prevention for Improved Compliance ](https://media.licdn.com/dms/image/v2/D5612AQFeiJE1gUixuQ/article-cover_image-shrink_720_1280/B56ZZzR0fqHsAI-/0/1745690776645?e=2147483647&v=beta&t=AVWg8l97KA6AEqaDykilNjrW2ASt3B_8jFQkx8vAmHM)\\
How to Leverage Microsoft Purview Data Loss Prevention…\\
\\
Kanerika Inc\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
2 months ago](https://www.linkedin.com/pulse/how-leverage-microsoft-purview-data-loss-prevention-improved-gdk4c)

[![Why JPMorgan Chase's CISOs Warning Demands Industry-Wide Action](https://media.licdn.com/dms/image/v2/D4E12AQFCgsT1aRRD3w/article-cover_image-shrink_720_1280/B4EZai634dHoAM-/0/1746490067156?e=2147483647&v=beta&t=8a5I4_0izewCdnasxDVFjb4k3A0j7LS8DKeAPpAe4-E)\\
Why JPMorgan Chase's CISOs Warning Demands…\\
\\
Dr. Erdal Ozkaya\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
2 months ago](https://www.linkedin.com/pulse/why-jpmorgan-chases-cisos-warning-demands-action-dr-erdal-ozkaya-hurke)

[![An Introduction to Keycloak: Simplifying Authentication & Identity Management](https://media.licdn.com/dms/image/v2/D4D12AQFgyUYCYwBgwg/article-cover_image-shrink_720_1280/B4DZVdNrURHwAI-/0/1741025621714?e=2147483647&v=beta&t=meUaoyRcp48-ZgNRdWEfltuQAeMHgAqS8bimUpPxFN0)\\
An Introduction to Keycloak: Simplifying…\\
\\
Ricardo M.\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
4 months ago](https://www.linkedin.com/pulse/introduction-keycloak-simplifying-authentication-identity-morales-h9rif)

- Even in the absence of widespread IPSIE adoption, Okta offers capabilities for visibility and management.
- Using the example of Calendly accessing Google Calendar, Harish Peri notes that while a future state should involve centralized authorization, current capabilities exist.
- Okta's platform, with its deep integrations across thousands of applications, can detect "misconfigured accounts, overprivileged accounts, excessive authorization."
- Okta's ISPM (Identity Security Posture Management) product provides visibility into "all of your risks in one place."
- ISPM is integrated with governance and privilege management capabilities, allowing for "remediative actions all in one place."
- Okta's approach is summarized as "see it, control it and then ongoing manage it from a governance perspective." This includes detecting and managing "overprivileged misconfigured accounts orphan accounts... non-human service accounts, keys."

7.    Activity Monitoring and Blind Spots:

- Pramod Gosavi raises the issue of monitoring app-to-app activity and potential blind spots (e.g., a third-party app misbehaving or being compromised and performing malicious actions on behalf of a user).
- Harish Peri states that monitoring granular activity and taking action requires "depth of integration into the application to be able to see the fine grain entitlements."
- Okta has had "fine grain entitlements for about a year now" allowing visibility into authorization details.
- The ability to "write into that and take action in case there is overprivileged" is also powered by Okta's integration depth.
- He reiterates the need for integrations "almost into that config screen that's saying like what authorizations I have."

8.    Non-Human Identity (Machine-to-Machine) and Privilege Access Management (PAM):

- Machine-to-machine identity is acknowledged as a distinct challenge.
- Vendors are emerging focusing on visibility or separate orchestration for machine identities.
- Harish Peri connects this to the issue of AI agents, which will "exacerbate" bad behavior around service accounts, tokens, and keys.
- The core issue is "discipline" in development practices to avoid exposing tokens (e.g., hardcoding, plain text in config files).
- He highlights the risk of AI-generated code inadvertently introducing exposed tokens.
- Machine-to-machine access patterns often relate to privileged access.
- It's acceptable for tokens to be long-lived or have excessive privilege if they are properly managed.
- The solution lies in introducing "discipline" through PAM practices: "access control around privilege, timebound checkouts, rotations, vaulting."
- "There's nothing inherently wrong with the tokens. It's the discipline around that."

9.    AI Agents and the Future of Identity:

- AI agents will amplify existing security problems.
- The complexity increases with autonomous agents and MCP (Multi-Component Systems) servers that can dynamically assemble tools and connect to systems in real-time.
- Okta's approach to "Author NAI" (Authoring AI) involves four principles dictating the discipline needed to build AI securely.
- Key principles include:
- Agent should not directly access API keys (should be vaulted).
- Fine-grained authorization must be baked in to act on behalf of the user (relationship-based access control).
- Following SSO/MFA protocols.
- The concept of cross-app authorization extends to AI agents: agents should not have direct access but be brokered through a standard identity platform.
- The need is to "outsource the authorization authentication logic to someone who knows what they're doing like us."
- Okta is working on an identity spec for agents, viewing it as an evolution of IPSIE.
- The vision is a "Lego plate" metaphor: a standard connecting every "Lego" (app, agent, resource) to a "unified identity security platform" for visibility and control.
- The standard acts as a "manifesto" ensuring adherence to core identity security principles ("Do not hard code anything. Make sure you're exposing yourself to a central platform.").

10.    Orchestration, Scalability, and Reliability:

- Orchestration of identities across dynamic, short-lived agents (like microservices) is a challenge.
- Harish Peri argues that with standards and discipline, the central platform can orchestrate actions based on policy violations or anomalous activity (e.g., universal logout).
- Orchestration is "a byproduct of having everything built to a standard sitting on top of a single platform."
- Okta emphasizes its existing high availability and scalability, stating they are "mission critical" and already have the infrastructure to handle high demands ("99... four five times up time").

1.    Okta's Response and Future Focus:

- Okta is actively promoting the adoption of identity security standards among SAS builders.
- They are preparing to release information on cross-app capabilities and updated standards/specs in the June-July timeframe (relative to the recording date).
- The JPMC letter has provided "more fuel to the fire" for these existing initiatives.
- Okta's goal is to create a "utopia" for CISOs where they have visibility and control over their entire application ecosystem, ensuring no direct app-to-app access bypasses identity controls.

Key Quotes:

- Harish Peri: "this letter was sort of a bomb in industry. I loved it... because it was great to hear, you know, the CISO of one of the world's largest and probably one of the most complex organizations... really echo back the thing that's been top of mind for us."
- Harish Peri: "identity at its core is the integration issue."
- Harish Peri: "with O 2.0 is it's really a framework to say I'm authorizing another app to access another app or resource on my behalf."
- Harish Peri: "you end up with essentially a token that is long lived, that is not proper managed that sometimes can get hardcoded or put into configuration files or something in plain text even that can be accessed. And that right there is what we believe is probably the biggest security gap in our industry right now."
- Harish Peri: "Every hacker is trying to do one thing. They're trying to get in get escalate privilege... And once they do that, they can start laterally moving around the organization."
- Harish Peri: "the security side of it is not being thought of with as much diligence as it should."
- Harish Peri: "we imagine a world where no SAS application is directly implementing authorization or authentication logic. What it's doing is it's exposing capabilities such that a platform like Okta can handle that."
- Harish Peri: "as a security professional, you have a single control plane to to see everything. Who's logging in? How are they logging in? What do they have access to? Is that access happening the right way? Are they breaking authorization patterns?"
- Harish Peri: "IPSIE, which it's a very long name for those that don't know. It's interoperable. profile for secure identity in the enterprise."
- Harish Peri: "see it, control it and then ongoing manage it from a governance perspective."

````````

``

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac%2F&trk=article-ssr-frontend-pulse_x-social-details_like-toggle_like-cta)

[Comment](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac%2F&trk=article-ssr-frontend-pulse_comment-cta)

````

- Copy
- LinkedIn
- Facebook
- Twitter

Share


````

[![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/asiqslyf4ooq7ggllg4fyo4o2)![](https://static.licdn.com/aero-v1/sc/h/a0e8rff6djeoq8iympcysuqfu)\\
100](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac%2F&trk=article-ssr-frontend-pulse_x-social-details_likes-count_social-actions-reactions) `` `` `` `` `` `` `` [14 Comments](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac%2F&trk=article-ssr-frontend-pulse_x-social-details_likes-count_social-actions-comments)

[![Brendan Booth, graphic](https://media.licdn.com/dms/image/v2/D5603AQHJor-zXS6-3w/profile-displayphoto-shrink_400_400/B56ZcxO7X5HgAg-/0/1748877686537?e=2147483647&v=beta&t=SY00GWNDx_jNNSRcwYzLsZTnxuop5kQLTnxWT3F0kTg)](https://www.linkedin.com/in/brendan-booth-48b8167?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_actor-image)

[Brendan Booth](https://www.linkedin.com/in/brendan-booth-48b8167?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_actor-name)

AI SOC Analyst



































2mo



- [Report this comment](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=COMMENT&_f=guest-reporting)

[Pramod Gosavi](https://www.linkedin.com/in/pramod-gosavi-b32a71?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment-text) What are your thoughts on using a solution like [vorlon.io](http://vorlon.io/?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment-text) to solve this problem? Do you think there is demand for this before there is a real standard like IPSIE rolled out and adopted by the market?

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac%2F&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_like) [Reply](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac%2F&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_reply)
1 Reaction


[![Nico Popp, graphic](https://media.licdn.com/dms/image/v2/C4E03AQEK03cujh0tCw/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1516164941515?e=2147483647&v=beta&t=WIa01cYKDRZiwjrUjBxSNyhEzD2EQeLCEXJhp0tU9MI)](https://www.linkedin.com/in/nicopopp?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_actor-image)

[Nico Popp](https://www.linkedin.com/in/nicopopp?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_actor-name)



































2mo



- [Report this comment](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=COMMENT&_f=guest-reporting)

I especially like session termination. FInally a real 'R' in ITDR...After device containment, identity containment.

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac%2F&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_like) [Reply](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac%2F&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_reply) [1 Reaction](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac%2F&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_reactions)
2 Reactions


[![Harish Peri, graphic](https://media.licdn.com/dms/image/v2/D4E03AQH202dTrW59PA/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1681744637962?e=2147483647&v=beta&t=CYRyMPGcC6lHCNk9JcOcLRvKCGj-UpJf1tnUV-fkrR4)](https://www.linkedin.com/in/harishperi?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_actor-image)

[Harish Peri](https://www.linkedin.com/in/harishperi?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_actor-name)

SVP Product Marketing, Okta



































2mo



- [Report this comment](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=COMMENT&_f=guest-reporting)

[Okta](https://www.linkedin.com/company/okta-inc-?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment-text) 👆🏽

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac%2F&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_like) [Reply](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac%2F&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_reply) [2 Reactions](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac%2F&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_reactions)
3 Reactions


[![Harish Peri, graphic](https://media.licdn.com/dms/image/v2/D4E03AQH202dTrW59PA/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1681744637962?e=2147483647&v=beta&t=CYRyMPGcC6lHCNk9JcOcLRvKCGj-UpJf1tnUV-fkrR4)](https://www.linkedin.com/in/harishperi?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_actor-image)

[Harish Peri](https://www.linkedin.com/in/harishperi?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_actor-name)

SVP Product Marketing, Okta



































2mo



- [Report this comment](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=COMMENT&_f=guest-reporting)

[Arnab Bose](https://www.linkedin.com/in/abosesf?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment-text) 👆🏽

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac%2F&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_like) [Reply](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac%2F&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_reply) [2 Reactions](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac%2F&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_reactions)
3 Reactions


[![Lokesh Koli, graphic](https://media.licdn.com/dms/image/v2/D4E03AQE202qof2XZDw/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1667238488596?e=2147483647&v=beta&t=5dV5HOYSVqnNYwLcCIOgDI0b56IEn6gyKrRrjkfzH7w)](https://www.linkedin.com/in/lokeshkoli?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_actor-image)

[Lokesh Koli](https://www.linkedin.com/in/lokeshkoli?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_actor-name)

Vectoredge's AI Powered Data Security platform mitigates AI Data Security risks by enhancing protection measures, enabling secure data sharing, and reducing costs and processing time.



































2mo



- [Report this comment](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=COMMENT&_f=guest-reporting)

Next Gen AI Identity protocol will be quite interesting space to look fwd to

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac%2F&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_like) [Reply](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac%2F&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_reply) [2 Reactions](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac%2F&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_reactions)
3 Reactions


[See more comments](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac%2F&trk=article-ssr-frontend-pulse_x-social-details_comments_comment-see-more)

To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac%2F&trk=article-ssr-frontend-pulse_x-social-details_feed-cta-banner-cta)

## More articles by Pramod Gosavi

- [NHI with Clutch Security](https://www.linkedin.com/pulse/nhi-clutch-security-pramod-gosavi-ayahc)

![](https://static.licdn.com/scds/common/u/img/pic/pic_pulse_stock_article_1.jpg)





Jun 30, 2025



### NHI with Clutch Security





Video: https://youtu.be/81M86g-Cje0 Key Themes and Most Important Ideas/Facts 1.



````



![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/a0e8rff6djeoq8iympcysuqfu)![](https://static.licdn.com/aero-v1/sc/h/asiqslyf4ooq7ggllg4fyo4o2)
42


``````````````



2 Comments



- [Future of SaaS platforms](https://www.linkedin.com/pulse/future-saas-platforms-pramod-gosavi-gd8fc)

![](https://media.licdn.com/dms/image/v2/D5612AQGQfhMTAfSBQQ/article-cover_image-shrink_720_1280/B56ZcScjl3GsAI-/0/1748361168639?e=2147483647&v=beta&t=qFzu2-KxNMjMOZbS_8PDAxI9DrTiMSF1VNrkP48_ABQ)





May 27, 2025



### Future of SaaS platforms





Video: https://www.youtube.



````



![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/asiqslyf4ooq7ggllg4fyo4o2)![](https://static.licdn.com/aero-v1/sc/h/a0e8rff6djeoq8iympcysuqfu)
68


``````````````



7 Comments



- [To MCP or not to MCP](https://www.linkedin.com/pulse/mcp-pramod-gosavi-rgqbc)

![](https://media.licdn.com/dms/image/v2/D5612AQEhQ6010S-p7A/article-cover_image-shrink_720_1280/B56ZZE_T52GsAI-/0/1744914170278?e=2147483647&v=beta&t=l8VQgX6fzwsyB32DSlQ53RMPiuALFl-ZxoOx4HlW54s)





Apr 17, 2025



### To MCP or not to MCP





Video link: https://youtu.be/Xw4AQlI1IKg Main Themes and Important Ideas: The "Pre-MCP" State: API-Centric Integration:…



````



![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/a0e8rff6djeoq8iympcysuqfu)![](https://static.licdn.com/aero-v1/sc/h/asiqslyf4ooq7ggllg4fyo4o2)
75


``````````````



14 Comments



- [AI in SOC with DropZone Security](https://www.linkedin.com/pulse/ai-soc-dropzone-security-pramod-gosavi-mo8zc)

![](https://media.licdn.com/dms/image/v2/D5612AQEGsw5tjwzR3w/article-cover_image-shrink_720_1280/B56ZX6TEh8HQAI-/0/1743661060535?e=2147483647&v=beta&t=nrJPppAhTfa7AsDStkPym91PD3ut--7xpBLjLC4izN4)





Apr 10, 2025



### AI in SOC with DropZone Security





Video: https://www.youtube.



````



![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/cyfai5zw4nrqhyyhl0p7so58v)![](https://static.licdn.com/aero-v1/sc/h/asiqslyf4ooq7ggllg4fyo4o2)
70


``````````````



3 Comments



- [AI in SOC with BrickLayer AI](https://www.linkedin.com/pulse/ai-soc-bricklayer-pramod-gosavi-xmfoc)

![](https://media.licdn.com/dms/image/v2/D5612AQEu1_hk46z2NA/article-cover_image-shrink_720_1280/B56ZWSl61mGUAI-/0/1741921172512?e=2147483647&v=beta&t=ju7IVw40_A4Bjmu7Ag6eQIHDH7upCvnTGyzPbi2srSs)





Mar 14, 2025



### AI in SOC with BrickLayer AI





Video: https://youtu.be/sHmUaoDj64o 1.



````



![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/a0e8rff6djeoq8iympcysuqfu)![](https://static.licdn.com/aero-v1/sc/h/asiqslyf4ooq7ggllg4fyo4o2)
31


``````````````



2 Comments



- [AI SOC with Simbian Security](https://www.linkedin.com/pulse/ai-soc-simbian-security-pramod-gosavi-omjfc)

![](https://media.licdn.com/dms/image/v2/D4E12AQFDc-fWFR6eRw/article-cover_image-shrink_720_1280/B4EZWDgDBaH0AM-/0/1741667972741?e=2147483647&v=beta&t=a3uX9qgCzKmTTkkMaFvhWkK43_6uYb4F88cl_Skgj-M)





Mar 11, 2025



### AI SOC with Simbian Security





Video link: https://www.youtube.



````



![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/asiqslyf4ooq7ggllg4fyo4o2)![](https://static.licdn.com/aero-v1/sc/h/2tzoeodxy0zug4455msr0oq0v)
42


``````````````



9 Comments



- [AI SOC with Ozan Unlu, CEO of Edge Delta](https://www.linkedin.com/pulse/ai-soc-ozan-unlu-ceo-edge-delta-pramod-gosavi-goamc)

![](https://media.licdn.com/dms/image/v2/D5612AQG5V1jTJDdtwQ/article-cover_image-shrink_720_1280/B56ZVuA5piGUAI-/0/1741307486380?e=2147483647&v=beta&t=hi3kcmlpb6CWpqt8eVw-WfLH5JKfJMnMsj6qFm8DsYo)





Mar 7, 2025



### AI SOC with Ozan Unlu, CEO of Edge Delta





Video Link: https://youtu.be/yd-ytREnq54 Main Themes and Important Ideas: 1.



````



![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/a0e8rff6djeoq8iympcysuqfu)![](https://static.licdn.com/aero-v1/sc/h/2tzoeodxy0zug4455msr0oq0v)
45


``````````````



4 Comments



- [AI in SOC with Kamal Shah and Vibhav Sreekanti, founders of Prophet Security](https://www.linkedin.com/pulse/ai-soc-kamal-shah-vibhav-sreekanti-founders-prophet-security-gosavi-ojijc)

![](https://media.licdn.com/dms/image/v2/D5612AQFSicUpy_5_tg/article-cover_image-shrink_720_1280/B56ZUr4mXAHsAQ-/0/1740198013455?e=2147483647&v=beta&t=Ege7IHUYONXZFaRJjN62NiZOt9dGYxrN0BtNDTSIraE)





Feb 27, 2025



### AI in SOC with Kamal Shah and Vibhav Sreekanti, founders of Prophet Security





Video: https://youtu.be/jITyJ446xNc Main Themes: Agentic AI Revolutionizing Security Operations: Prophet Security…



````



![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/2tzoeodxy0zug4455msr0oq0v)![](https://static.licdn.com/aero-v1/sc/h/asiqslyf4ooq7ggllg4fyo4o2)
49


``````````````



3 Comments



- [AI SOC with Kumar Saurabh, founder AirMDR](https://www.linkedin.com/pulse/ai-soc-kumar-saurabh-founder-airmdr-pramod-gosavi-5qctc)

![](https://media.licdn.com/dms/image/v2/D5612AQE7ltCXTCLoqg/article-cover_image-shrink_720_1280/B56ZUrz5IPGQAI-/0/1740196779603?e=2147483647&v=beta&t=RRGzrgr4br0Ut0bF9mvJN7Ez_nUHgJI8kgcR52v-J00)





Feb 22, 2025



### AI SOC with Kumar Saurabh, founder AirMDR





The State of SOCs and the Talent Gap: · Kumar highlights the cybersecurity talent shortage, emphasizing that it's not…



````



![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/a0e8rff6djeoq8iympcysuqfu)![](https://static.licdn.com/aero-v1/sc/h/asiqslyf4ooq7ggllg4fyo4o2)
70


``````````````



9 Comments



- [Will GenAI app vendors win even the Gen AI infra market](https://www.linkedin.com/pulse/genai-app-vendors-win-even-gen-ai-infra-market-pramod-gosavi-wnb6c)

![](https://media.licdn.com/dms/image/v2/D5612AQEviM7hdoWBuA/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1725214141354?e=2147483647&v=beta&t=9mplKzL4aMEaimTam87gAFCmkR4BfE9k3yGgKEczN5Q)





Sep 1, 2024



### Will GenAI app vendors win even the Gen AI infra market





I published this article (https://www.linkedin.



````



![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/a0e8rff6djeoq8iympcysuqfu)![](https://static.licdn.com/aero-v1/sc/h/asiqslyf4ooq7ggllg4fyo4o2)
72


``````````````



17 Comments




Show more


[See all articles](https://www.linkedin.com/in/pramod-gosavi-b32a71/recent-activity/articles/)

## Sign in

Stay updated on your professional world

[Sign in](https://www.linkedin.com/uas/login?session_redirect=%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac%2F&trk=article-ssr-frontend-pulse_xandr-ad-fallback_signin)

By clicking Continue to join or sign in, you agree to LinkedIn’s [User Agreement](https://www.linkedin.com/legal/user-agreement?trk=article-ssr-frontend-pulse_auth-button_user-agreement), [Privacy Policy](https://www.linkedin.com/legal/privacy-policy?trk=article-ssr-frontend-pulse_auth-button_privacy-policy), and [Cookie Policy](https://www.linkedin.com/legal/cookie-policy?trk=article-ssr-frontend-pulse_auth-button_cookie-policy).


Sign In - Google Accounts

Continue with GoogleContinue with Google. Opens in new tab

New to LinkedIn? [Join now](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2F3rd-party-authorizationsoauthnhiagents-pramod-gosavi-a54ac%2F&trk=article-ssr-frontend-pulse_xandr-ad-fallback_join-link)

## Others also viewed

- [![](https://media.licdn.com/dms/image/v2/D5612AQEbiA8zMeYl_w/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1738190984341?e=2147483647&v=beta&t=9X9boEob38qfzU42c-yEXo_YVZPZIWBRkW9r_-vhoiU)\\
\\
**Kerberos III - User Impersonation**\\
\\
Lares, a Damovo Company\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
4mo](https://www.linkedin.com/pulse/kerberos-iii-user-impersonation-lares-consulting-mk3ic)
- [![](https://media.licdn.com/dms/image/v2/D4D12AQGZdFXAOvsJEg/article-cover_image-shrink_600_2000/B4DZZJE_jHG4AQ-/0/1744982771270?e=2147483647&v=beta&t=nGNAk66EJ2DzXp8pRxo9tuW2LsFDz7nyQaMEAzR9GS8)\\
\\
**April 18, 2025**\\
\\
Kannan Subbiah\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
3mo](https://www.linkedin.com/pulse/april-18-2025-kannan-subbiah-m55ff)
- [![](https://media.licdn.com/dms/image/v2/D5612AQFyEpHUKWJKQw/article-cover_image-shrink_720_1280/B56Za2v68xGsAI-/0/1746822739009?e=2147483647&v=beta&t=GnO_ltiY2hx5s1czXa2frsX5VslLfc8CoNxKTCkUbmw)\\
\\
**The Importance of Demanding Data Governance Transparency from Your Software Vendors**\\
\\
Drummond Group, LLC\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
2mo](https://www.linkedin.com/pulse/importance-demanding-data-governance-transparency-from-j2pdc)
- [![](https://media.licdn.com/dms/image/v2/D4E12AQGGNQDF-IORNQ/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1707585790675?e=2147483647&v=beta&t=ayCsOIWg7BRT_1k_1Yst-igCw33Ah0jGkuw81veZYbQ)\\
\\
**Escaping The Gray Area Of Tier Zero: Part 1 - Why Definitional Debates Can Paralyze Enterprise Security**\\
\\
Kay Daskalakis\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
1y](https://www.linkedin.com/pulse/escaping-gray-area-tier-zero-part-1-why-debates-can-kay-daskalakis-n9wke)
- [![](https://media.licdn.com/dms/image/v2/D5612AQGW1DuraYnDWw/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1681829686617?e=2147483647&v=beta&t=j5lyI_GBUI96euebbJ7S1ezeozhw8f6qVM2pwWUDnSo)\\
\\
**Balancing Security and User Adoption on Salesforce for Enterprise Success: A Comprehensive Guide for Salesforce Architects**\\
\\
Shivanath Devinarayanan\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
2y](https://www.linkedin.com/pulse/balancing-security-user-adoption-salesforce-success-devinarayanan)
- [![](https://media.licdn.com/dms/image/v2/D4E12AQGg86ESVWtmLg/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1720513061704?e=2147483647&v=beta&t=aCujwO0CEDtHn1KZdWGHob7Ii-K9TGGMqVO3OqjAhTQ)\\
\\
**Understanding the Implementing Acts for EU Regulation 2024/1183 (eIDAS 2.0)**\\
\\
Joerg Lenz\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
1y](https://www.linkedin.com/pulse/understanding-implementing-acts-eu-regulation-20241183-joerg-lenz-gbwee)
- [![](https://media.licdn.com/dms/image/v2/D5612AQHg9jxwsKM1Dw/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1732310287800?e=2147483647&v=beta&t=TvAvY7WCOt3RI_E6OmgQTauP45sjHpIcoRx8-o24NWE)\\
\\
**It's a new world and giving 3rd party software vendors and others access to ERP systems requires a new way of thinking**\\
\\
Richard Duffy\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
7mo](https://www.linkedin.com/pulse/its-new-world-giving-3rd-party-software-vendors-others-richard-duffy-2lfxc)
- [![](https://media.licdn.com/dms/image/v2/D4E12AQEAlv7Pj98QqQ/article-cover_image-shrink_720_1280/B4EZaQTOOrHYAI-/0/1746177681899?e=2147483647&v=beta&t=QbPo4GmjOMDgeia0mJDWRoumv41FRD2oF-30SvMumVA)\\
\\
**Why Workload Identity Federation matters?**\\
\\
Badr Nasslahsen, CISSP\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
2mo](https://www.linkedin.com/pulse/why-workload-identity-federation-matters-badr-nasslahsen-cissp-o0cyc)
- [![](https://media.licdn.com/dms/image/v2/D5612AQE1MeaFMc56IA/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1656238642861?e=2147483647&v=beta&t=eS-zHBmSu6wa-1LtMe-NHcrGagM5ZGg1X5Qs1pTceU0)\\
\\
**Is passwordless the future of authentication and authorization?**\\
\\
Subbu Rama\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
3y](https://www.linkedin.com/pulse/passwordless-future-authentication-authorization-subbu-rama)
- [![](https://media.licdn.com/dms/image/v2/D5612AQHu4LTZSmJOng/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1672490567048?e=2147483647&v=beta&t=r8qWQ37FDqfuQVXemAyB9CKU0AWfp4IjrZp_5IGpkZE)\\
\\
**Why Do We Need Authorization and Authentication? 🔑**\\
\\
Gokulakkannan AK\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
2y](https://www.linkedin.com/pulse/why-do-we-need-authorization-authentication-gokulakkannan-ak)

Show more

Show less


## Explore topics

- [Sales](https://www.linkedin.com/pulse/topics/sales-s5/)
- [Marketing](https://www.linkedin.com/pulse/topics/marketing-s2461/)
- [IT Services](https://www.linkedin.com/pulse/topics/it-services-s57547/)
- [Business Administration](https://www.linkedin.com/pulse/topics/business-administration-s50111/)
- [HR Management](https://www.linkedin.com/pulse/topics/hr-management-s50359/)
- [Engineering](https://www.linkedin.com/pulse/topics/engineering-s166/)
- [Soft Skills](https://www.linkedin.com/pulse/topics/soft-skills-s2976/)
- [See All](https://www.linkedin.com/pulse/topics/home/)

``
