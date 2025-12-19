---
date: '2025-12-19'
description: The concept of trustworthy AI agents is critically examined, emphasizing
  the lack of integrity in current systems, which can mislead users and fail to maintain
  accuracy. The proposed solution involves decoupling personal data stores from AI
  systems to enhance security independently of AI performance, thus enabling users
  to manage data access and maintain accurate records. Key requirements for such systems
  include accessibility, accuracy verification, user control, security against attacks,
  and ease of use. This approach aims to mitigate manipulation risks and foster trust
  in AI technologies, addressing the existing integrity gap in data security practices.
link: https://www.schneier.com/blog/archives/2025/12/building-trustworthy-ai-agents.html
tags:
- data integrity
- data privacy
- AI security
- personal data management
- trustworthy AI
title: Building Trustworthy AI Agents - Schneier on Security
---

## Building Trustworthy AI Agents

The promise of personal AI assistants rests on a dangerous assumption: that we can trust systems we haven’t made trustworthy. We can’t. And today’s versions are failing us in predictable ways: pushing us to do things against our own best interests, gaslighting us with doubt about things we are or that we know, and being unable to distinguish between who we are and who we have been. They struggle with incomplete, inaccurate, and partial context: with no standard way to move toward accuracy, no mechanism to correct sources of error, and no accountability when wrong information leads to bad decisions.

These aren’t edge cases. They’re the result of building AI systems without basic integrity controls. We’re in the third leg of data security—the old CIA triad. We’re good at availability and working on confidentiality, but we’ve never properly solved integrity. Now AI personalization has exposed the gap by accelerating the harms.

The scope of the problem is large. A good AI assistant will need to be trained on everything we do and will need access to our most intimate personal interactions. This means an intimacy greater than your relationship with your email provider, your social media account, your cloud storage, or your phone. It requires an AI system that is both discreet and trustworthy when provided with that data. The system needs to be accurate and complete, but it also needs to be able to keep data private: to selectively disclose pieces of it when required, and to keep it secret otherwise. No current AI system is even close to meeting this.

To further development along these lines, I and others have proposed separating users’ personal data stores from the AI systems that will use them. It makes sense; the engineering expertise that designs and develops AI systems is completely orthogonal to the security expertise that ensures the confidentiality and integrity of data. And by separating them, advances in security can proceed independently from advances in AI.

What would this sort of personal data store look like? Confidentiality without integrity gives you access to wrong data. Availability without integrity gives you reliable access to corrupted data. Integrity enables the other two to be meaningful. Here are six requirements. They emerge from treating integrity as the organizing principle of security to make AI trustworthy.

First, it would be broadly accessible as a data repository. We each want this data to include personal data about ourselves, as well as transaction data from our interactions. It would include data we create when interacting with others—emails, texts, social media posts—and revealed preference data as inferred by other systems. Some of it would be raw data, and some of it would be processed data: revealed preferences, conclusions inferred by other systems, maybe even raw weights in a personal LLM.

Second, it would be broadly accessible as a source of data. This data would need to be made accessible to different LLM systems. This can’t be tied to a single AI model. Our AI future will include many different models—some of them chosen by us for particular tasks, and some thrust upon us by others. We would want the ability for any of those models to use our data.

Third, it would need to be able to prove the accuracy of data. Imagine one of these systems being used to negotiate a bank loan, or participate in a first-round job interview with an AI recruiter. In these instances, the other party will want both relevant data and some sort of proof that the data are complete and accurate.

Fourth, it would be under the user’s fine-grained control and audit. This is a deeply detailed personal dossier, and the user would need to have the final say in who could access it, what portions they could access, and under what circumstances. Users would need to be able to grant and revoke this access quickly and easily, and be able to go back in time and see who has accessed it.

Fifth, it would be secure. The attacks against this system are numerous. There are the obvious read attacks, where an adversary attempts to learn a person’s data. And there are also write attacks, where adversaries add to or change a user’s data. Defending against both is critical; this all implies a complex and robust authentication system.

Sixth, and finally, it must be easy to use. If we’re envisioning digital personal assistants for everybody, it can’t require specialized security training to use properly.

I’m not the first to suggest something like this. Researchers have proposed a “Human Context Protocol” (https://papers.ssrn.com/sol3/ papers.cfm?abstract\_id=5403981) that would serve as a neutral interface for personal data of this type. And in my capacity at a company called Inrupt, Inc., I have been working on an extension of Tim Berners-Lee’s Solid protocol for distributed data ownership.

The engineering expertise to build AI systems is orthogonal to the security expertise needed to protect personal data. AI companies optimize for model performance, but data security requires cryptographic verification, access control, and auditable systems. Separating the two makes sense; you can’t ignore one or the other.

Fortunately, decoupling personal data stores from AI systems means security can advance independently from performance (https:// ieeexplore.ieee.org/document/ 10352412). When you own and control your data store with high integrity, AI can’t easily manipulate you because you see what data it’s using and can correct it. It can’t easily gaslight you because you control the authoritative record of your context. And you determine which historical data are relevant or obsolete. Making this all work is a challenge, but it’s the only way we can have trustworthy AI assistants.

This essay was originally published in _IEEE Security & Privacy_.

Tags: [AI](https://www.schneier.com/tag/ai/), [data privacy](https://www.schneier.com/tag/data-privacy/), [LLM](https://www.schneier.com/tag/llm/), [privacy](https://www.schneier.com/tag/privacy/), [trust](https://www.schneier.com/tag/trust/)

[Posted on December 12, 2025 at 7:00 AM](https://www.schneier.com/blog/archives/2025/12/building-trustworthy-ai-agents.html) •
[11 Comments](https://www.schneier.com/blog/archives/2025/12/building-trustworthy-ai-agents.html#comments)

### Comments

Rontea •

[December 12, 2025 9:08 AM](https://www.schneier.com/blog/archives/2025/12/building-trustworthy-ai-agents.html/#comment-450602)

By empowering individuals to manage their own data, AI systems can operate with greater integrity and transparency, fostering trust and reliable collaboration between humans and machines.

Anonymous •

[December 12, 2025 9:32 AM](https://www.schneier.com/blog/archives/2025/12/building-trustworthy-ai-agents.html/#comment-450604)

“There is no trust without security, and yet it seems to be an afterthought in ai development today.”

Clive Robinson •

[December 12, 2025 9:52 AM](https://www.schneier.com/blog/archives/2025/12/building-trustworthy-ai-agents.html/#comment-450605)

@ Bruce, ALL,

With regards,

> “The system needs to be accurate and complete, but it also needs to be able to keep data private: to selectively disclose pieces of it when required, and to keep it secret otherwise. No current AI system is even close to meeting this.”

There is a very real issue that can be summed up as,

**“Of accurate, complete, and private, you can have any two but not all three.”**

Because of the various “Observer effects”.

The reason for this, I’ve known since the 1990’s and it apparently cannot be solved.

Put simply to increase accuracy or completeness, you have to “ask highly specific questions” the number of questions goes also goes up as a power law.

The thing is every question leaks data thus privacy diminishes quite rapidly.

To increase privacy you have to cut down the information leaked.

There are two basic ways,

1, Reduce the specificity of the questions.

2, Reduce the number of questions.

The results are broadly the same you loose a significant amount of accuracy or completeness, as you would expect.

But it gets worse, nearly all attempts to increase privacy of the data it’s self is by “anonymizing” which not only reduces the specificity significantly, but is usually easily stripped away with another source of data, even though it to has been “anonymized”.

Call it the “Data uncertainty principle” but as you get more fine grained in measurement, privacy is lost significantly to even a passive observer watching only “traffic”, not message content.

Morley •

[December 12, 2025 10:42 AM](https://www.schneier.com/blog/archives/2025/12/building-trustworthy-ai-agents.html/#comment-450606)

How is securing my personal data going to keep my assistant from manipulating me?

KC •

[December 12, 2025 10:52 AM](https://www.schneier.com/blog/archives/2025/12/building-trustworthy-ai-agents.html/#comment-450607)

There is a [helpful illustration](https://hcp.loyalagents.org/hcp-paper.pdf) of Human Context Protocol in the AI personalization paper on page 5. You can see how user data may flow and filter to personalized agents.

Bruce and Barath also have several [very nice graphics](https://spectrum.ieee.org/data-privacy) in their IEEE paper illustrating data decoupling.

I’m finding these enlightening in the exploration of personalized AI agents and articulated safeguards.

Bilateralrope •

[December 12, 2025 11:24 AM](https://www.schneier.com/blog/archives/2025/12/building-trustworthy-ai-agents.html/#comment-450608)

Are any of the AI companies even trying to build agents like this ?

If not, how do you propose making them ?

ResearcherZero •

[December 13, 2025 12:13 AM](https://www.schneier.com/blog/archives/2025/12/building-trustworthy-ai-agents.html/#comment-450613)

@Morley

Just give me your credentials and I will do it for you? Treat it as an untrustworthy adversary. Much like warez, a phishing attempt, a scam or any other kind of nasty rash.

Expect agentic AI to be compromised at the time of interaction, or at a later date. Always think carefully about how you interact with them and how you can eliminate sharing personal information or reduce the exposure of behavioral patterns. Limit the use of agentic AI where the same task can be accomplished via other means. Break up information and subjects entered into AI prompts into separate sessions, use aliasing or remove any personally relevant information or identifiers.

Data segregation and segmentation, with a strict rule set and strict personal security policy. Treat it like public WIFI or anything else that can result in data compromise or a source of malicious payload delivery through having any interaction with it. Use a separate device that does not contain personal information and treat that device with caution.

ResearcherZero •

[December 13, 2025 12:30 AM](https://www.schneier.com/blog/archives/2025/12/building-trustworthy-ai-agents.html/#comment-450614)

@Bilateralrope

Given they operate these models on a subscription basis the companies care little for the personal privacy or anonymity of their customers. These systems have been poked in with little thought of how to limit sensitive data exposure, or of the vulnerabilities that are created by having connectable automated interfaces which can trigger a range of actions.

Gen AI is insecure by design. Preventing prompt injection attacks is likely impossible.

Given the lack of regulation to create more secure models, this seems unlikely to change.

Bilateralrope •

[December 13, 2025 12:52 AM](https://www.schneier.com/blog/archives/2025/12/building-trustworthy-ai-agents.html/#comment-450616)

@ResearcherZero

Which makes articles like this seem pointless without a plan to get lawmakers involved.

Morley •

[December 13, 2025 10:54 AM](https://www.schneier.com/blog/archives/2025/12/building-trustworthy-ai-agents.html/#comment-450627)

AI can manipulate pretty strongly even without personal info. And once the info is in a date breach, the cat’s out of the bag. That’s not to say we shouldn’t safeguard personal data. I just wish it solved more than it does.

Mark Thompson •

[December 18, 2025 2:31 AM](https://www.schneier.com/blog/archives/2025/12/building-trustworthy-ai-agents.html/#comment-450717)

Bruce, the proposal to decouple the data store is the correct architectural move, but it highlights a secondary failure mode we are seeing: the “Authorization Blind Spot.”

Even if the data is stored securely in a separate pod, if the AI Agent acts as the retrieval interface, we are still trusting a probabilistic model to enforce deterministic access controls (ACLs). We’ve found that LLMs are notoriously bad at context-switching between “User A” and “User B” permissions when they share a context window.

We need to decouple not just the storage of data, but the logic that authorizes access to it. We analyzed this specific “agent authorization” gap recently: [https://protectifyai.com/blog/ai-agents-authorization](https://protectifyai.com/blog/ai-agents-authorization)

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)\\
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2025/12/building-trustworthy-ai-agents.html/feed/)

## Leave a comment [Cancel reply](https://www.schneier.com/blog/archives/2025/12/building-trustworthy-ai-agents.html\#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2025%2F12%2Fbuilding-trustworthy-ai-agents.html "Login")

Name

Email

URL:

Remember personal info?

Fill in the blank: the name of this blog is Schneier on \_\_\_\_\_\_\_\_\_\_\_ (required):

Comments:

![](https://www.schneier.com/wp-content/themes/schneier/assets/images/loader.gif)

**Allowed HTML**
<a href="URL"> • <em> <cite> <i> • <strong> <b> • <sub> <sup> • <ul> <ol> <li> • <blockquote> <pre>
**Markdown Extra** syntax via [https://michelf.ca/projects/php-markdown/extra/](https://michelf.ca/projects/php-markdown/extra/)

Δ

[← AIs Exploiting Smart Contracts](https://www.schneier.com/blog/archives/2025/12/ais-exploiting-smart-contracts.html) [Friday Squid Blogging: Giant Squid Eating a Diamondback Squid →](https://www.schneier.com/blog/archives/2025/12/friday-squid-blogging-giant-squid-eating-a-diamondback-squid.html)

Sidebar photo of Bruce Schneier by Joe MacInnis.

[Powered by WordPress](https://wordpress.com/wp/?partner_domain=www.schneier.com&utm_source=Automattic&utm_medium=colophon&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com) [Hosted by Pressable](https://pressable.com/?utm_source=Automattic&utm_medium=rpc&utm_campaign=Concierge%20Referral&utm_term=concierge)

# Search results

Magnifying Glass
Search

Close search results

FiltersShow filters

Sort:RelevanceNewestOldestPrice: low to highPrice: high to lowRating

## No results found

## Filter options

Close Search

[Search powered by Jetpack](https://jetpack.com/upgrade/search/?utm_source=poweredby)
