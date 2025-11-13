---
date: '2025-11-13'
description: Christophe Parisel's exploration of the "Pensieve Parasite" malware highlights
  critical vulnerabilities in Microsoft Copilot Chat's design. This in-memory, semantic
  virus exploits user memories to execute malicious commands without user consent,
  leveraging functionalities like file uploads. It underscores significant architectural
  flaws, particularly poor isolation between chat and file upload channels, and unregulated
  memory modifications. Proposed mitigations include restricting data flow into memory
  and enhancing monitoring. The implications extend beyond traditional malware, suggesting
  potential risk in legitimate business processes, challenging organizations to reconsider
  LLM integration within security frameworks.
link: https://www.linkedin.com/pulse/planting-virus-copilot-chats-memory-christophe-parisel-uysqe/
tags:
- prompt injection
- Copilot Chat
- in-memory virus
- AI security
- malware
title: Planting a virus in Copilot Chat's memory
---

Agree & Join LinkedIn


By clicking Continue to join or sign in, you agree to LinkedIn’s [User Agreement](https://www.linkedin.com/legal/user-agreement?trk=linkedin-tc_auth-button_user-agreement), [Privacy Policy](https://www.linkedin.com/legal/privacy-policy?trk=linkedin-tc_auth-button_privacy-policy), and [Cookie Policy](https://www.linkedin.com/legal/cookie-policy?trk=linkedin-tc_auth-button_cookie-policy).


``````[Skip to main content](https://www.linkedin.com/pulse/planting-virus-copilot-chats-memory-christophe-parisel-uysqe/#main-content)

``````

![Planting a virus in Copilot Chat's memory](https://media.licdn.com/dms/image/v2/D4E12AQFtuI8HSPgnLw/article-cover_image-shrink_720_1280/B4EZlI4vxYIwAM-/0/1757864462713?e=2147483647&v=beta&t=Q8P_P2c2d5TNkSBkFxQW8ItjivBT0EZel_DkSzXF26Q)

A Pensieve, parasitized

I crafted a malware for research purposes, the "Pensieve Parasite", targeting Microsoft Copilot Chat. It leverages two common capabilities: files exchange (uploads & downloads), and user memories. These capabilities are widely available, even in enterprises enforcing hardened/enclaved deployments.

Although the virus was specifically built with Copilot Chat in mind, the simplicity of its design, its modest prerequisites, and the low technical expertise required make it quite generic, even vendor agnostic.

That said, LLM-powered chat viruses have no reason to exist, much less to be universal. We believe the major reason they can contaminate information systems is two simple design errors.

### Overview

Before we give more details and propose a fix, let's give this attack technique a clear characterization: simply put, the Pensieve Parasite is a semantic, in-memory virus. It belongs to the large family of prompt injections, but it is the first of its kind. Let me explain why.

By "in-memory virus," we mean a non-self-replicating form of malware hosted in conversational memory.

By "semantic," we mean two things:

1. Its execution is entirely based on natural language. This is very different from usual IT viruses, which use programming languages, and very similar to classical prompt injections.
2. Instructions are not obfuscated. This is very different from classical prompt injection attacks, where the intent is always hidden, making natural language instructions not so natural: they are indeed heavily re-engineered and look quite outlandish to a native speaker.

### Operating model

The operating model of the Pensieve Parasite is straightforward: conversational memory is used as a persistent pivot to execute arbitrary instructions from an upstream compromised file to many downstream, chat-generated, files. Using memory for pivoting is not only useful for spacial contamination (north-south across datastores, east-west across users), but also, and that's the novelty, for temporal contamination (maintaining the attack across different conversation sessions over time).

In our design, "conversation 0" is where a malevolent instruction is initially uploaded from an adversary-controlled file, and implanted in a user's conversational memory. All future conversations have the potential to trigger forward contamination to downstream chat-generated files.

![Article content](https://media.licdn.com/dms/image/v2/D4E12AQE-Cumm6mPaXA/article-inline_image-shrink_1500_2232/B4EZlSb0eXKcAc-/0/1758024649734?e=2147483647&v=beta&t=oq1miC7l0_jatgoU_PttCoNWx4eX4ijPylul0X3_c0c)Temporal (cross-conversational) persistence and spatial contamination sequence

To make the virus really efficient, the trigger must have good chances to fire. In my exploit, it was: "whenever the user requests to download a text file." A common, innocuous action that ensures frequent activation :-)

It must also be stealthy: tampering with user memory should be done without explicit user consent.

![Article content](https://media.licdn.com/dms/image/v2/D4E12AQEZPT0VyAfAxQ/article-inline_image-shrink_400_744/B4EZoMeEttGcAc-/0/1761145808140?e=2147483647&v=beta&t=LhQjNJBFo8reGL5YdRxLFJQzmgSMzjMU2XU2dfWUT7Y)Memory implants

### Replication and contamination

The Pensieve Parasite is not a worm, but a virus: it relies on user interaction to copy itself into memory in a stealthy way. As said before, it is not self-replicating, and this is a relief. Still, the more users who read the compromised file, the more opportunities the parasite has to spread to different users' memories.

The parasite doesn't copy itself into contaminated files, only into user memories. These compromised memories then serve as persistent injection points, contaminating all future downstream files indefinitely.

### Exploiting two design errors

Error #1: Channels porosity

The fundamental flaw in Copilot's design is insufficient isolation between "chat" and "upload" channels. Information from uploaded files has no reason to automatically populate user memory. Only information coming from chat interactions should, by default.

Error #2: Implicit memory modifications

What I've found particularly concerning is the possibility to create new memories (or alter existing ones) from uploaded files without explicit consent from the user.

In my proof-of-concept, the user asks Copilot to generate a calendar invite using a template file in TXT format. What Copilot does under the hood, however, is to update user memory with malevolent instructions executed from the template.

> Ultimately, users should have explicit control over their chat memories.

### Possible fixes

We can think of three possible fixes: one preventive (works all the time), the two others detective & responsive (works "most of the time").

- The preventive fix should simply prevent information flow from data uploads to memory. It should be hardwired into the bot architecture. This architectural change would require uploaded content to remain in session-scoped context only.
- A detective approach could deploy an independent LLM to analyze memory write requests, flagging instructions that contain conditional triggers or unusual directives.
- Manual user review of all memory writes would provide another detection approach, but is impractical at scale and would likely degrade user experience significantly.

### Microsoft's response

11 Sep 2025: Submitted PoC to MSRC.

16 Sep 2025: MSRC closed the case because the PoC included explicit user consent.

19 Sep 2025: Submitted a second PoC to MSRC demonstrating a fraud (modification of banking transaction amount and beneficiary) without user consent.

15 Oct 2025: MSRC closed the case because "Existing prompt injection defenses block broad attacks; this approach only works under extremely targeted conditions, which significantly limits feasibility and impact."

21 Oct 2025: Shared draft of this document with MSRC.

3 Nov 2025: Public disclosure.

### Security implications of semantic in-memory viruses

So far, LLM malware has been almost entirely focused on prompt injection. This is quite understandable, since as of today this technique remains almost impossible to prevent in real life, production environments.

But... consider the next iteration of malicious capability: an attack that distorts business processes by biasing LLM reasoning through seemingly legitimate natural language instructions.

> No IT security system can detect a prompt that appears perfectly legitimate but yields catastrophic business decisions.

I've shared a practical example of reality distortion: the malevolent payload contained in the text template which I mentioned earlier, updates Copilot memory. It changes the banking account receiving commission fees. The only visual cue that something went wrong is the small "memory update' message showing up in the conversation.

No security tool is going to detect reality distortion because, without understanding the business at hand, it is completely legitimate to use IBAN XXX or IBAN YYY for sending fees.

This context-dependency makes semantic viruses particularly insidious: the same instruction could be benign in one domain, and devastating in another.

````````

``

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fplanting-virus-copilot-chats-memory-christophe-parisel-uysqe%2F&trk=article-ssr-frontend-pulse_x-social-details_like-toggle_like-cta)

Like

Celebrate

Support

Love

Insightful

Funny

[Comment](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fplanting-virus-copilot-chats-memory-christophe-parisel-uysqe%2F&trk=article-ssr-frontend-pulse_comment-cta)

````

- Copy
- LinkedIn
- Facebook
- X

Share


````

[![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/a0e8rff6djeoq8iympcysuqfu)![](https://static.licdn.com/aero-v1/sc/h/2tzoeodxy0zug4455msr0oq0v)\\
55](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fplanting-virus-copilot-chats-memory-christophe-parisel-uysqe%2F&trk=article-ssr-frontend-pulse_x-social-details_likes-count_social-actions-reactions)`````````````` [26 Comments](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fplanting-virus-copilot-chats-memory-christophe-parisel-uysqe%2F&trk=article-ssr-frontend-pulse_x-social-details_likes-count_social-actions-comments)

[![Marlon Caraan, graphic](https://static.licdn.com/aero-v1/sc/h/9c8pery4andzj6ohjkjp54ma2)](https://ph.linkedin.com/in/marlon-caraan-184555227?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_actor-image)

[Marlon Caraan](https://ph.linkedin.com/in/marlon-caraan-184555227?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_actor-name)

Technology Specialist



































1w



- [Report this comment](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fpulse%2Fplanting-virus-copilot-chats-memory-christophe-parisel-uysqe&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=COMMENT&_f=guest-reporting)

Thanks for flagging this, [Christophe](https://fr.linkedin.com/in/parisel?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment-text). Definitely something to keep an eye on as Copilot gets deeper into workflows.

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fplanting-virus-copilot-chats-memory-christophe-parisel-uysqe%2F&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_like) [Reply](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fplanting-virus-copilot-chats-memory-christophe-parisel-uysqe%2F&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_reply) [1 Reaction](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fplanting-virus-copilot-chats-memory-christophe-parisel-uysqe%2F&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_reactions)
2 Reactions


[![Francesco Faenzi, graphic](https://static.licdn.com/aero-v1/sc/h/9c8pery4andzj6ohjkjp54ma2)](https://it.linkedin.com/in/francescofaenzi?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_actor-image)

[Francesco Faenzi](https://it.linkedin.com/in/francescofaenzi?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_actor-name)

#TrustEverybodyButCutTheCards



































1w



- [Report this comment](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fpulse%2Fplanting-virus-copilot-chats-memory-christophe-parisel-uysqe&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=COMMENT&_f=guest-reporting)

Memory poisoning attacks on AI copilots expose a fundamental architectural flaw: stateful LLMs inherit traditional session hijacking risks without the decades of defensive patterns we've built for web applications.

The stealth factor is particularly concerning from a cybersecurity posture perspective. Unlike traditional malware, poisoned memories don't trigger EDR alerts or network anomalies. They manipulate AI output silently, creating a perfect vector for fraud, data exfiltration, or supply chain compromise through developer tools.

TCO implications are significant: organizations deploying GitHub Copilot, Cursor, or similar tools must now add "AI memory hygiene" to security operations. This includes: 1) Regular memory audit trails, 2) Context isolation between projects/users, 3) Cryptographic integrity checks on stored memories.

The economic feasibility of these attacks is worrying - low technical barrier, high impact. As for adoption barriers: most orgs haven't updated threat models to include LLM context poisoning. We need "memory firewalls" - verification layers that validate memory integrity before feeding context to LLMs. Without this, every AI assistant becomes a persistent backdoor.

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fplanting-virus-copilot-chats-memory-christophe-parisel-uysqe%2F&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_like) [Reply](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fplanting-virus-copilot-chats-memory-christophe-parisel-uysqe%2F&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_reply) [1 Reaction](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fplanting-virus-copilot-chats-memory-christophe-parisel-uysqe%2F&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_reactions)
2 Reactions


[![Jeff van Eek, graphic](https://static.licdn.com/aero-v1/sc/h/9c8pery4andzj6ohjkjp54ma2)](https://nl.linkedin.com/in/jeffvaneek?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_actor-image)

[Jeff van Eek](https://nl.linkedin.com/in/jeffvaneek?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_actor-name)

Adverum Consulting - AWS Architect, Engineer, Consultant - AWS certified , 🇺🇸🇳🇱 Solutions not Platforms. (opinions are my own).



































1w



- [Report this comment](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fpulse%2Fplanting-virus-copilot-chats-memory-christophe-parisel-uysqe&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=COMMENT&_f=guest-reporting)

Certainly a new frontier for psy-ops and counter intelligence.

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fplanting-virus-copilot-chats-memory-christophe-parisel-uysqe%2F&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_like) [Reply](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fplanting-virus-copilot-chats-memory-christophe-parisel-uysqe%2F&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_reply) [1 Reaction](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fplanting-virus-copilot-chats-memory-christophe-parisel-uysqe%2F&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_reactions)
2 Reactions


[![Tarak ☁️, graphic](https://static.licdn.com/aero-v1/sc/h/9c8pery4andzj6ohjkjp54ma2)](https://fr.linkedin.com/in/tarak-bach-hamba/en?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_actor-image)

[Tarak ☁️](https://fr.linkedin.com/in/tarak-bach-hamba/en?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_actor-name)

building infracodebase.com - AI that learns from your docs, diagrams & codebase to help teams manage and scale infrastructure with context and security in mind.



































1w



- [Report this comment](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fpulse%2Fplanting-virus-copilot-chats-memory-christophe-parisel-uysqe&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=COMMENT&_f=guest-reporting)

Really interesting, the idea of memory-layer poisoning as a silent persistence vector is both clever and unsettling.

It really highlights how LLM-integrated tools are drifting closer to the “stateful agent” model which means memory integrity now needs the same threat modeling we’d apply to session storage or API tokens.

Curious if you’ve seen any effective mitigation patterns beyond memory sanitization or scoped recall? Feels like we’ll soon need a full “memory firewall” layer for AI copilots.

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fplanting-virus-copilot-chats-memory-christophe-parisel-uysqe%2F&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_like) [Reply](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fplanting-virus-copilot-chats-memory-christophe-parisel-uysqe%2F&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_reply) [3 Reactions](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fplanting-virus-copilot-chats-memory-christophe-parisel-uysqe%2F&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_reactions)
4 Reactions


[See more comments](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fplanting-virus-copilot-chats-memory-christophe-parisel-uysqe%2F&trk=article-ssr-frontend-pulse_x-social-details_comments_comment-see-more)

To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fplanting-virus-copilot-chats-memory-christophe-parisel-uysqe%2F&trk=article-ssr-frontend-pulse_x-social-details_feed-cta-banner-cta)

## More articles by Christophe Parisel

- [A fragility in Terraform actions](https://www.linkedin.com/pulse/fragility-terraform-actions-christophe-parisel-kuiye)

![](https://media.licdn.com/dms/image/v2/D4E12AQFQXq3hrs13FQ/article-cover_image-shrink_720_1280/B4EZmvmKKmKYAI-/0/1759587646798?e=2147483647&v=beta&t=T4s-LZnZX1JITy_MwJOFvwGYXFmTp2rLBHaOvb3Wcy0)





Oct 4, 2025



### A fragility in Terraform actions





Terraform 1.14 (currently in beta) introduces Actions as a first-class feature for running custom operations during…



````



![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/a0e8rff6djeoq8iympcysuqfu)
51


``````````````



5 Comments



- [Thinking the unthinkable](https://www.linkedin.com/pulse/thinking-unthinkable-christophe-parisel-imphe)

![](https://media.licdn.com/dms/image/v2/D4E12AQGDcXXKZmKHHw/article-cover_image-shrink_720_1280/B4EZmBekgOHEAI-/0/1758813901456?e=2147483647&v=beta&t=6g6S9N9PRO_wpEHCbisBrlEjrYGEcb_rPddMPYREorw)





Sep 25, 2025



### Thinking the unthinkable





Black Swans are the worst nightmare of risk managers, because they are both unexpected and disastrous. But we should be…



````



![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/a0e8rff6djeoq8iympcysuqfu)![](https://static.licdn.com/aero-v1/sc/h/cyfai5zw4nrqhyyhl0p7so58v)
27


``````````````



8 Comments



- [Business meets security with Azure Service Groups](https://www.linkedin.com/pulse/business-meets-security-azure-service-groups-christophe-parisel-e3mse)

![](https://media.licdn.com/dms/image/v2/D4E12AQHYzLdvI2zAZQ/article-cover_image-shrink_720_1280/B4EZlI4YqbK0AI-/0/1757864368451?e=2147483647&v=beta&t=rCFL5z5nFmG2bZ6Vo3JdpPCvFQjdAKgW72CiiJNGgSE)





Sep 15, 2025



### Business meets security with Azure Service Groups





Which CISO hasn't dreamt of a security strategy wholly driven by the business? There are opportunities, of course, and…



````



![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/a0e8rff6djeoq8iympcysuqfu)![](https://static.licdn.com/aero-v1/sc/h/asiqslyf4ooq7ggllg4fyo4o2)
46


``````````````



5 Comments



- [A zero-hallucination AI](https://www.linkedin.com/pulse/zero-hallucination-ai-christophe-parisel-l47qf)

![](https://media.licdn.com/dms/image/v2/D4E12AQHhL49WDkc3Pg/article-cover_image-shrink_720_1280/B4EZjLwCucHgAQ-/0/1755765029657?e=2147483647&v=beta&t=77UNX_c_tJuXm2E2YxfaNQoU9gRF278p_5Ob3ldKQQg)





Aug 26, 2025



### A zero-hallucination AI





Now that we are three years into the generative AI revolution, some patterns are emerging around how to approach AI…



````



![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/a0e8rff6djeoq8iympcysuqfu)![](https://static.licdn.com/aero-v1/sc/h/2tzoeodxy0zug4455msr0oq0v)
60


``````````````



25 Comments



- [Managed Identities 2.0 From Tokens To Circuits](https://www.linkedin.com/pulse/managed-identities-20-from-tokens-circuits-christophe-parisel-3ucyf)

![](https://media.licdn.com/dms/image/v2/D4E12AQGPlgqvYhzD7g/article-cover_image-shrink_720_1280/B4EZifr3zKGUAM-/0/1755025738349?e=2147483647&v=beta&t=iawZ8Uknl_JzAHJo5p563o0ZbpKpC-9BQA-mMLEySWE)





Aug 19, 2025



### Managed Identities 2.0 From Tokens To Circuits





Managed identities (MIs) were the single best thing to happen to cloud authentication in years: no secret vaults in…



````



![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/a0e8rff6djeoq8iympcysuqfu)![](https://static.licdn.com/aero-v1/sc/h/asiqslyf4ooq7ggllg4fyo4o2)
54


``````````````



22 Comments



- [When naming is a sin: Azure’s Achilles Heel](https://www.linkedin.com/pulse/when-naming-sin-azures-achilles-heel-christophe-parisel-2fade)

![](https://media.licdn.com/dms/image/v2/D4E12AQGpwY7v5ZU-kw/article-cover_image-shrink_720_1280/B4EZeb4lG4GwAI-/0/1750666993995?e=2147483647&v=beta&t=kdRqfWT5fucSgaJJIUzEMCnRNk2Vh25uT-fI0ktsniE)





Jun 23, 2025



### When naming is a sin: Azure’s Achilles Heel





In our recent research, we uncovered a structural weakness in the organization of Azure RBAC permissions of Custom and…



````



![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/a0e8rff6djeoq8iympcysuqfu)![](https://static.licdn.com/aero-v1/sc/h/cyfai5zw4nrqhyyhl0p7so58v)
39


``````````````



9 Comments



- [Taming NHIs in Azure and AWS (part 2: foundations)](https://www.linkedin.com/pulse/taming-nhis-azure-aws-part-2-foundations-christophe-parisel-r6dfe)

![](https://media.licdn.com/dms/image/v2/D4E12AQESw_ET9Jos0g/article-cover_image-shrink_720_1280/B4EZcMwBLXHYAI-/0/1748265609363?e=2147483647&v=beta&t=bkKZ4Om6MaCpHWzGPXEuk_Bt_n_kLvo-owT8cwSz-MU)





Jun 4, 2025



### Taming NHIs in Azure and AWS (part 2: foundations)





In part 1, we explained how the IAM schemas of our mainstream Cloud providers (Azure, AWS and Google) were almost…



````



![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/asiqslyf4ooq7ggllg4fyo4o2)![](https://static.licdn.com/aero-v1/sc/h/a0e8rff6djeoq8iympcysuqfu)
13


``````````````



4 Comments



- [Evading multimodal AI firewalls](https://www.linkedin.com/pulse/evading-multimodal-ai-firewalls-christophe-parisel-edace)

![](https://media.licdn.com/dms/image/v2/D4E12AQE4ZoDSYnJB9g/article-cover_image-shrink_600_2000/B4EZX2kj9JHgAU-/0/1743598535237?e=2147483647&v=beta&t=tK8Hq0iSgaXtF-Ckkmwpn_OuBuBUxCmr-Ng3EnR8M6w)





May 12, 2025



### Evading multimodal AI firewalls





In a previous article, we saw how multimodal AI opens up brand new attack paths against applications. But for those…



````



![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/a0e8rff6djeoq8iympcysuqfu)![](https://static.licdn.com/aero-v1/sc/h/cyfai5zw4nrqhyyhl0p7so58v)
20


``````````````



7 Comments



- [Taming NHIs in AWS and Azure (part 1: a visual tour)](https://www.linkedin.com/pulse/taming-nhis-aws-azure-part-1-visual-tour-christophe-parisel-f9tpe)

![](https://media.licdn.com/dms/image/v2/D4E12AQH7D2iU9PMriw/article-cover_image-shrink_600_2000/B4EZYevew7GgAQ-/0/1744272488585?e=2147483647&v=beta&t=mRr7MRA9HqVuy9GBys3SrivOdivYqaKunSAqfW970cM)





Apr 28, 2025



### Taming NHIs in AWS and Azure (part 1: a visual tour)





In a series of articles, I will explain how I overcome the challenge of managing Non Human Identities (NHIs) at scale…



````



![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/a0e8rff6djeoq8iympcysuqfu)![](https://static.licdn.com/aero-v1/sc/h/2tzoeodxy0zug4455msr0oq0v)
45


``````````````



10 Comments



- [Engineering multimodal AI attacks](https://www.linkedin.com/pulse/ultimate-weapon-against-your-ai-powered-apps-christophe-parisel-wmmre)

![](https://media.licdn.com/dms/image/v2/D4E12AQHfWenOlhSMnw/article-cover_image-shrink_600_2000/B4EZXhZ9weHMAU-/0/1743243435264?e=2147483647&v=beta&t=VX7rbWun2mtbc5v4YkSJZ8geHikuLwdD9wzJq0waSAs)





Mar 31, 2025



### Engineering multimodal AI attacks





What will kill your AI apps? A design error..



````



![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/a0e8rff6djeoq8iympcysuqfu)![](https://static.licdn.com/aero-v1/sc/h/asiqslyf4ooq7ggllg4fyo4o2)
36


``````````````



8 Comments




Show more


[See all articles](https://fr.linkedin.com/in/parisel/recent-activity/articles/)

## Explore content categories

- [Career](https://www.linkedin.com/top-content/career/)
- [Productivity](https://www.linkedin.com/top-content/productivity/)
- [Finance](https://www.linkedin.com/top-content/finance/)
- [Soft Skills & Emotional Intelligence](https://www.linkedin.com/top-content/soft-skills-emotional-intelligence/)
- [Project Management](https://www.linkedin.com/top-content/project-management/)
- [Education](https://www.linkedin.com/top-content/education/)
- [Technology](https://www.linkedin.com/top-content/technology/)
- [Leadership](https://www.linkedin.com/top-content/leadership/)
- [Ecommerce](https://www.linkedin.com/top-content/ecommerce/)
- [User Experience](https://www.linkedin.com/top-content/user-experience/)
- [Recruitment & HR](https://www.linkedin.com/top-content/recruitment-hr/)
- [Customer Experience](https://www.linkedin.com/top-content/customer-experience/)
- [Real Estate](https://www.linkedin.com/top-content/real-estate/)
- [Marketing](https://www.linkedin.com/top-content/marketing/)
- [Sales](https://www.linkedin.com/top-content/sales/)
- [Retail & Merchandising](https://www.linkedin.com/top-content/retail-merchandising/)
- [Science](https://www.linkedin.com/top-content/science/)
- [Supply Chain Management](https://www.linkedin.com/top-content/supply-chain-management/)
- [Future Of Work](https://www.linkedin.com/top-content/future-of-work/)
- [Consulting](https://www.linkedin.com/top-content/consulting/)
- [Writing](https://www.linkedin.com/top-content/writing/)
- [Economics](https://www.linkedin.com/top-content/economics/)
- [Artificial Intelligence](https://www.linkedin.com/top-content/artificial-intelligence/)
- [Employee Experience](https://www.linkedin.com/top-content/employee-experience/)
- [Workplace Trends](https://www.linkedin.com/top-content/workplace-trends/)
- [Fundraising](https://www.linkedin.com/top-content/fundraising/)
- [Networking](https://www.linkedin.com/top-content/networking/)
- [Corporate Social Responsibility](https://www.linkedin.com/top-content/corporate-social-responsibility/)
- [Negotiation](https://www.linkedin.com/top-content/negotiation/)
- [Communication](https://www.linkedin.com/top-content/communication/)
- [Engineering](https://www.linkedin.com/top-content/engineering/)
- [Hospitality & Tourism](https://www.linkedin.com/top-content/hospitality-tourism/)
- [Business Strategy](https://www.linkedin.com/top-content/business-strategy/)
- [Change Management](https://www.linkedin.com/top-content/change-management/)
- [Organizational Culture](https://www.linkedin.com/top-content/organizational-culture/)
- [Design](https://www.linkedin.com/top-content/design/)
- [Innovation](https://www.linkedin.com/top-content/innovation/)
- [Event Planning](https://www.linkedin.com/top-content/event-planning/)
- [Training & Development](https://www.linkedin.com/top-content/training-development/)

Show more

Show less


``
