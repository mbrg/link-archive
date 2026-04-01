---
date: '2026-01-03'
description: By 2026, cybersecurity is poised to undergo significant transformation
  driven by AI advancements. Organizations will prioritize the efficacy of their defensive
  AI against adversarial AI capabilities, resulting in a critical shift in resource
  allocation towards agentic security platforms. Asset management will improve dramatically
  through AI automation, enabling consistent oversight against sophisticated threats.
  Concurrently, security education may evolve to support AI systems rather than human
  developers directly. As reliance on agent-driven tools increases, traditional security
  roles will change, accelerating demand for top-tier security professionals adept
  in AI. Certifications may decline in value as immediate effectiveness becomes paramount
  in hiring.
link: https://danielmiessler.com/blog/cybersecurity-ai-changes-2026
tags:
- security management
- AI
- asset management
- cybersecurity
- future
title: Cybersecurity Changes I Expect in 2026 ◆ Daniel Miessler
---

# Cybersecurity Changes I Expect in 2026

My thoughts on what's coming for Cybersecurity in 2026

December 30, 2025

[#cybersecurity](https://danielmiessler.com/archives/?tag=cybersecurity) [#ai](https://danielmiessler.com/archives/?tag=ai) [#future](https://danielmiessler.com/archives/?tag=future)

[![Cybersecurity Changes I Expect in 2026](https://danielmiessler.com/images/cybersecurity-changes-2026.webp)](https://danielmiessler.com/images/cybersecurity-changes-2026.webp)

Here are the major changes I see coming for Cybersecurity in 2026.

## **It becomes very clear that the primary security question for a company is how good their attackers' AI is vs. their own** [​](https://danielmiessler.com/blog/cybersecurity-ai-changes-2026\#it-becomes-very-clear-that-the-primary-security-question-for-a-company-is-how-good-their-attackers-ai-is-vs-their-own)

- CISOs increasingly realize that there is no way to scale their human team to deal with how constant, continuous, and increasingly effective their attackers are becoming at attacking them
- It becomes a competition with how fast you can perform asset management, attack surface management, and vulnerability management on your company, but especially on your perimeter (which includes email and phishing/social engineering)

## More spend on Agentic security platforms as a way to augment security teams and sidestep the continued challenge of hiring and onboarding good security people [​](https://danielmiessler.com/blog/cybersecurity-ai-changes-2026\#more-spend-on-agentic-security-platforms-as-a-way-to-augment-security-teams-and-sidestep-the-continued-challenge-of-hiring-and-onboarding-good-security-people)

- It's not that there aren't good security people out there. It's that it's hard to find them and even harder to vet them, go through the entire interview process, and get them onboarded and spun up. The friction of hiring and onboarding is extremely nasty, and that friction gets dramatically worse when compared to agents once the agents start getting good enough to do decent, verifiable work (which my guess is mid-2026-2027)
- Hiring agents to start doing security work on the team will be seen as a way to avoid the friction of hiring, even if agents won't be able to match the quality of a solid, experienced security person anytime in 2026 (and possibly 2027 either)
- Keep in mind that this will largely happen on accident, not consciously

## Security coding training actually becomes useful for once because it will be turned into just-in-time context aimed at the AIs writing and checking the code instead of humans [​](https://danielmiessler.com/blog/cybersecurity-ai-changes-2026\#security-coding-training-actually-becomes-useful-for-once-because-it-will-be-turned-into-just-in-time-context-aimed-at-the-ais-writing-and-checking-the-code-instead-of-humans)

- Secure code training has had very little stickiness and overall effectiveness because of the human limitation of being primarily driven by the incentive structures in companies that drive their promotions and pay
- The currency of engineering teams is features, not security. Most companies don't give any thought (which is to say virtually zero) for paying developers more because they are producing more secure code, and because humans can mostly focus on only one incentive system at once, they ignore security advice even if the training was good (which it often isn't)
- AI doesn't have this problem because if you tell it that security is a critical priority, and that they need to fight the urge to prioritize other things over it, this is something that AI can actually follow because it can keep multiple things in its mind at once, and with proper scaffolding it can be encouraged to never let this drop out of its mind, and to have multiple layered defenses to make sure that the controls are checked over and over repeatedly

## Asset Management becomes possible for the first time because of Agents [​](https://danielmiessler.com/blog/cybersecurity-ai-changes-2026\#asset-management-becomes-possible-for-the-first-time-because-of-agents)

- Asset Management should have been an IT function all along, but the responsibility always fell to security because they're the ones who had to clean up the messes
- It's an untenable problem with human teams because there's too much to watch and it changes too often
- Agents in 2025 and 2026 are just now becoming competent and dependable. But it's extraordinarily easy to improve on asset management because we suck so bad at it
- This is also absolutely critical because asset management needs to be part of our AI automation stack for attack surface management and vulnerability management in the constant cat-and-mouse game against attackers who are doing the same thing against us
- Another way to say this is that attackers are about to get really good at asset management, but unfortunately they are doing it on our infrastructure, not their own. So we better get real good at it really fast as well

## Significantly more in-house building of security tools [​](https://danielmiessler.com/blog/cybersecurity-ai-changes-2026\#significantly-more-in-house-building-of-security-tools)

- Double-edged sword because it'll be very easy to produce something useful, and quickly, due to AI, and some security management will reward this, which will incentivize it
- But a large percentage of these will become abandoned and security technical debt because there's a big difference between an MVP and something that scales in production and is properly maintained

## CISOs learn that with proper scaffolding of an agentic platform, many (most?) security products can be replaced by AI prompts [​](https://danielmiessler.com/blog/cybersecurity-ai-changes-2026\#cisos-learn-that-with-proper-scaffolding-of-an-agentic-platform-many-most-security-products-can-be-replaced-by-ai-prompts)

There are tons of decent security tools on the market, but they tend to be full products that cost a lot of money, need to go through procurement, and need to be installed and maintained. That's a lot of friction.

The difference with Agent-based security is that the use cases for those projects become prompts to a waiting swarm of eager interns with very low marginal cost.

> Spin up 128 agents and have them go through every line of code in all of our repos and report on every place we're using hardcoded credentials.

This is especially true of "many eyes" types of security problems where there are millions of places to look, and by the time you get done looking, they've already changed.

- **Asset management**
- Configuration management
- Secrets cleanup

A swarm of hundreds or thousands of agents checking continuously really is the only solution for a lot of security problems like these. If we could do it with people, we would have already. But it's not really possible due to the difficulty of hiring and training and managing all those people, and (most importantly) the fact that it would cost too much money even if we could.

## Just as with asset management and security training, the concept of Security ROI becomes (more) tractable for the first time because of AI [​](https://danielmiessler.com/blog/cybersecurity-ai-changes-2026\#just-as-with-asset-management-and-security-training-the-concept-of-security-roi-becomes-more-tractable-for-the-first-time-because-of-ai)

- The reason we could never do ROI well as an industry before is because there are too many moving parts, and it's too hard to agree on a framework
- With a properly built AI security management system, we now have the ability to say, "This is how we're calculating ROI, show a basic algorithm, monitor the budget at the same time as we monitor our projects, our staff and compensation, new security features being deployed, what our attackers are doing, how many of their attacks we have stopped, and the average cost of all those attacks becoming successful vs. our spend on the budget. I have been doing this kind of consulting for over 15 years and I'm now using AI to do this for customers in a way that was not possible before. It seriously feels really good to be able to show your management/CFO the actual value of their work. Still not perfect, but tractable for the first time in our industry's lifespan
- This will be a massive improvement through 26 and 27 for security teams needing to communicate their value to the company

## Top security talent who have organizational knowledge, coding skills, AI skills, and great communication will be in extreme demand [​](https://danielmiessler.com/blog/cybersecurity-ai-changes-2026\#top-security-talent-who-have-organizational-knowledge-coding-skills-ai-skills-and-great-communication-will-be-in-extreme-demand)

- The next two tiers of talent below that which are either: more moderately talented, more moderately experienced, or more moderately broad-skilled, will face massively more pressure because the top tier will be so much more effective.

## Junior security talent becomes (even more) non-valuable to security teams [​](https://danielmiessler.com/blog/cybersecurity-ai-changes-2026\#junior-security-talent-becomes-even-more-non-valuable-to-security-teams)

Many teams will no longer have any bandwidth or tolerance for needing to train anyone because they are under pressure from attackers and from management on budget and speed of execution.

- Just like hiring, training will become something that security teams can no longer afford to do, just because of the increased pressure from multiple angles
- The only attractive candidates are those who don't need anything to get going
- This not only hurts new graduates and new holders of security certifications, but it also massively harms the pipeline for new people entering the field and forces us to ask the question of where intermediate and expert people are going to come from if we don't have any new people learning on the job

## Security degrees and certifications plummet in value to security teams [​](https://danielmiessler.com/blog/cybersecurity-ai-changes-2026\#security-degrees-and-certifications-plummet-in-value-to-security-teams)

- Security certifications massively drop in value
- Information security degrees massively drop in value
- The main thing that matters now is: Can you start immediately and be effective basically on day one, are you extremely good at using AI to multiply yourself and the rest of the team to take problems proactively and deliver solutions end to end

## AI security vendors consolidate and generalize to being more general agent platforms instead of specific point solutions like automated SOC or automated GRC [​](https://danielmiessler.com/blog/cybersecurity-ai-changes-2026\#ai-security-vendors-consolidate-and-generalize-to-being-more-general-agent-platforms-instead-of-specific-point-solutions-like-automated-soc-or-automated-grc)

- As CISOs start to trust agents more, they will realize how general they are and that they shouldn't be limited to specific tasks when they could largely be handled by many different types of tasks, especially as AI improves throughout the year and into next year

## More and more of traditional CI/CD security tooling and SAST / DAST starts to get eaten by Agentic workflows that happen at various stages, from the increasingly voice-controlled and Agent controlled IDE to GitHub integrations [​](https://danielmiessler.com/blog/cybersecurity-ai-changes-2026\#more-and-more-of-traditional-ci-cd-security-tooling-and-sast-dast-starts-to-get-eaten-by-agentic-workflows-that-happen-at-various-stages-from-the-increasingly-voice-controlled-and-agent-controlled-ide-to-github-integrations)

- Traditional security tools like scanners, CI/CD security, etc. are heavy, expensive, and require management overhead, and they can can increasingly be replaced by prompts and custom-written command-line tools that scale well and can be controlled by agents where the work is actually being done and committed

## Dramatic increase in the use of AI to inject granular, time-sensitive, and contextually relevant security advice at the moment that security decisions are being made, such as during writing of code and testing of code. [​](https://danielmiessler.com/blog/cybersecurity-ai-changes-2026\#dramatic-increase-in-the-use-of-ai-to-inject-granular-time-sensitive-and-contextually-relevant-security-advice-at-the-moment-that-security-decisions-are-being-made-such-as-during-writing-of-code-and-testing-of-code)

- Developers rarely stop what they're doing to go and look up their security training or the security best practice. But now they won't have to because Klippi will offer to use the paved road option instead of what they were planning to do
- Secure implementations can be recommended when somebody is trying to hardcode a secret or build a custom encryption algorithm, or use local API keys instead of a secure vault

Share

[Post](https://ul.live/share-x?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fcybersecurity-ai-changes-2026&title=Cybersecurity%20Changes%20I%20Expect%20in%202026 "Share on X") [LinkedIn](https://ul.live/share-linkedin?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fcybersecurity-ai-changes-2026&title=Cybersecurity%20Changes%20I%20Expect%20in%202026 "Share on LinkedIn") [HN Hacker News](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fcybersecurity-ai-changes-2026&title=Cybersecurity%20Changes%20I%20Expect%20in%202026 "Share on Hacker News") [Reddit](https://ul.live/share-reddit?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fcybersecurity-ai-changes-2026&title=Cybersecurity%20Changes%20I%20Expect%20in%202026 "Share on Reddit") [Facebook](https://ul.live/share-facebook?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fcybersecurity-ai-changes-2026&title=Cybersecurity%20Changes%20I%20Expect%20in%202026 "Share on Facebook") [Forward](https://ul.live/share-email?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fcybersecurity-ai-changes-2026&title=Cybersecurity%20Changes%20I%20Expect%20in%202026 "Share via Email")

Follow

[Get The Newsletter](https://ul.live/nlpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fcybersecurity-ai-changes-2026&title=Cybersecurity%20Changes%20I%20Expect%20in%202026) [Follow On X](https://ul.live/xpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fcybersecurity-ai-changes-2026&title=Cybersecurity%20Changes%20I%20Expect%20in%202026) [Subscribe On YouTube](https://ul.live/ytpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fcybersecurity-ai-changes-2026&title=Cybersecurity%20Changes%20I%20Expect%20in%202026) [Follow On LinkedIn](https://ul.live/lipostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fcybersecurity-ai-changes-2026&title=Cybersecurity%20Changes%20I%20Expect%20in%202026)

Search

This post was tagged with:

cybersecurityaifuture

[HOME](https://danielmiessler.com/)· [BLOG](https://danielmiessler.com/blog)· [ARCHIVES](https://danielmiessler.com/archives)· [ABOUT](https://danielmiessler.com/about)
