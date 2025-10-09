---
date: '2025-10-09'
description: At the Zenity AI Agent Security Summit, CTO Michael Bargury acknowledged
  the nascent field of AI security, highlighting the necessity of collaboration in
  risk management as AI agents pose significant security threats. Key insights included
  treating AI agents akin to malicious insiders and adopting strict limitations on
  their operational capabilities. Presenters underscored the growing prevalence of
  AI-targeted attacks and the importance of minimizing agent access to critical systems
  to mitigate risks. As security flaws are increasingly exploited via prompt injection,
  implementing robust control mechanisms is essential to enhance AI safety and prevent
  unauthorized actions.
link: https://www.theregister.com/2025/10/09/zenity_ai_agent_security_summit_recap/
tags:
- AI Security
- Cybersecurity
- Prompt Injection
- Risk Management
- AI Agents
title: Zenity AI Agent Security Summit focuses on risk mitigation • The Register
---

[![](https://www.theregister.com/design_picker/ae01b183a707a7db8cd5f2c947715ed56d335138/graphics/std/user_icon_white_extents_16x16.png)![](https://www.theregister.com/design_picker/ae01b183a707a7db8cd5f2c947715ed56d335138/graphics/std/user_icon_white_filled_extents_16x16.png)Sign in / up](https://account.theregister.com/login?r=https%3A//www.theregister.com/2025/10/09/zenity_ai_agent_security_summit_recap/ "Sign in / up")

[The Register](https://www.theregister.com/)

[![](https://www.theregister.com/design_picker/ae01b183a707a7db8cd5f2c947715ed56d335138/graphics/std/magnifying_glass_white_extents_16x16.png)](https://search.theregister.com/)

![](https://www.theregister.com/design_picker/ae01b183a707a7db8cd5f2c947715ed56d335138/graphics/icon/burger_menu_white_16x16.png)![](https://www.theregister.com/design_picker/ae01b183a707a7db8cd5f2c947715ed56d335138/graphics/icon/burger_menu_white_close_16x16.png)

## Topics

[Special Features](https://www.theregister.com/2025/10/09/zenity_ai_agent_security_summit_recap/#subnav-box-nav-special_features)

## Special Features

## Vendor Voice

[Resources](https://www.theregister.com/2025/10/09/zenity_ai_agent_security_summit_recap/#subnav-box-nav-resources)

## Resources

#### [Cybersecurity Month](https://www.theregister.com/special_features/cybersecurity_month/)

[**2**![comment bubble on white](https://www.theregister.com/design_picker/f5daacc84b9722c1e31ba85f836c37e4ad993fc4/graphics/icons/bubble_comment_white.png)](https://forums.theregister.com/forum/all/2025/10/09/zenity_ai_agent_security_summit_recap/ "View comments on this article")

# Hobble your AI agents to prevent them from hurting you too badly

[**2**![comment bubble on white](https://www.theregister.com/design_picker/f5daacc84b9722c1e31ba85f836c37e4ad993fc4/graphics/icons/bubble_comment_white.png)](https://forums.theregister.com/forum/all/2025/10/09/zenity_ai_agent_security_summit_recap/ "View comments on this article")

## That's the main takeaway from the Zenity AI Agent Security Summit

![icon](https://www.theregister.com/design_picker/d518b499f8a6e2c65d4d8c49aca8299d54b03012/graphics/icon/vulture_red.svg)[Thomas Claburn](https://www.theregister.com/Author/Thomas-Claburn "Read more by this author")

Thu 9 Oct 2025  //
07:27 UTC

![](https://www.theregister.com/design_picker/d2e337b97204af4aa34dda04c4e5d56d954b216f/graphics/icons/social_share_icon.svg)

Michael Bargury, CTO of AI security company Zenity, welcomed attendees to the company's AI Agent Security Summit on Wednesday with an unexpected admission.

"This is a new space and we – frankly – don't really know what we're doing," he said at San Francisco's Commonwealth Club. "But we're trying ... We need to face things as they are. And the only way to do it is together."

Zenity's marketing graphic for its AI Agent Security Summit inadvertently made that point by mixing Marvel and DC Comics motifs. The conference graphic read, "The League Assembles," applying Marvel's "Avengers, assemble!" catchphrase and font styling to what DC fans might read as a reference to The Justice League.

The brand mashup nonetheless struck an appropriately aspirational tone, even if its evocation of heroism overstates the tech industry's present capacity to safeguard the public from AI agents. The conference was ostensibly about security, but the presenters focused on risk management – limiting the damage rather than precluding it.

Johann Rehberger, an independent security researcher and red team director at Electronic Arts, agreed with Bargury's assessment in an interview with _The Register_ following his keynote presentation. He should know, having recently published an AI security flaw write-up [every day during the month of August](https://embracethered.com/blog/).

"For many, security is an afterthought," he said. "A lot of AI labs, and vendors, they focus on content safety, so the model doesn't swear at you."

Security, particularly when an AI agent can control your computer, is different, he said.

Ryan Ray, regional director of Slalom's cybersecurity and privacy consulting practice, defined AI agents in a presentation as "systems that pursue complex goals with limited supervision." You may also know them by developer Simon Willison's formulation, " [AI models using tools in a loop](https://simonwillison.net/2025/May/22/tools-in-a-loop/)." They are, by any definition, a security risk.

Rehberger proposed another description during his presentation: "Think about agents as malicious insiders. But they're potentially faster."

"When I started my research about two and a half years ago, looking at LLMs, nobody was really looking at it from this perspective," he told _The Register_. "And I think now we see a lot of security researchers looking at it more."

- [Google declares AI bug hunting season open, sets a $30K max reward](https://www.theregister.com/2025/10/07/google_ai_bug_bounty/)
- [Cisco's new router unites disparate datacenters into AI training behemoths](https://www.theregister.com/2025/10/08/cisco_multi_datacenter/)
- [IBM's big iron to get Spyre AI accelerator upgrade this month](https://www.theregister.com/2025/10/08/ibm_z17_spyre_accelerator/)
- [AI companion bots use emotional manipulation to boost usage](https://www.theregister.com/2025/10/08/ai_bots_use_emotional_manipulation/)

Rehberger pointed to the recent [compromise of the Amazon Q extension](https://www.theregister.com/2025/07/24/amazon_q_ai_prompt/) for Visual Studio Code and said that people are starting to see attacks that specifically target AI agents and associated coding tools, based on the assumption that many developers are using these tools and have them installed on their local machines.

Attackers, he said, are now looking to invoke code agents and put them into YOLO mode – so they execute commands without human approval – to hijack machines and steal data.

During his keynote, Rehberger discussed how this can be done in VS Code by applying the [configuration setting](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode) `chat.tools.autoApprove` to direct the associated model to operate autonomously.

"We will see many compromised computers in the future," he said.

Others speaking at Zenity's conference endorsed that proposition, citing a variety of security shortcomings in AI agents, MCP servers, and LLMs. And the answers they provided to IT professionals struggling to manage the risk of AI agents tended toward finding ways to limit what AI agents can do.

Asked by a conference attendee to share some thoughts on how to prevent agents from taking action on their own, Jack Cable, CEO and co-founder of AI security startup Corridor and a former senior tech advisor at CISA, said, "There are a couple of classes of mitigations. I think the best is something that isn't relying on AI to address it."

In contrast to what some companies are trying to do with AI guardrails, Cable said, "I think what actually is the best approach is having some sort of controls in place. One option is for that to be through just limitations on what tools you can use."

As an example, he cited how Anthropic prevented its browser use extension from connecting to banks and financial sites, to mitigate the risk of an AI-based attack that empties bank accounts.

In short, to reduce the risk of AI agent exploitation, hobble your AI agents. Don't give them access to file deletion commands. Don't let them open arbitrary network ports.

Nate Lee, founder of Trustmind and Cloudsec.ai, observed during his presentation how the fundamental problem with AI agents is that they're non-deterministic, so we don't know exactly what they're going to do.

"With all of the talks around agent security, really 98 percent of it is going to boil down to the fact that prompt injection is a real thing," he said. "And we don't have a really great way to protect against it. And because of that, you need to be extremely mindful of these trade-offs as you're building the systems. Because when you give it more context, when you give it more tools, you're also increasing that attack surface."

With AI agents, less is more security. ®

![](https://www.theregister.com/design_picker/d2e337b97204af4aa34dda04c4e5d56d954b216f/graphics/icons/social_share_icon.svg)Share

#### More about

- [AI](https://www.theregister.com/Tag/AI/)
- [Cybersecurity](https://www.theregister.com/Tag/Cybersecurity/)

More like these

×

### More about

- [AI](https://www.theregister.com/Tag/AI/)
- [Cybersecurity](https://www.theregister.com/Tag/Cybersecurity/)

### Narrower topics

- [AIOps](https://www.theregister.com/Tag/AIOps/)
- [Center for Internet Security](https://www.theregister.com/Tag/Center%20for%20Internet%20Security/)
- [DeepSeek](https://www.theregister.com/Tag/DeepSeek/)
- [Gemini](https://www.theregister.com/Tag/Gemini/)
- [Google AI](https://www.theregister.com/Tag/Google%20AI/)
- [GPT-3](https://www.theregister.com/Tag/GPT-3/)
- [GPT-4](https://www.theregister.com/Tag/GPT-4/)
- [Large Language Model](https://www.theregister.com/Tag/Large%20Language%20Model/)
- [Machine Learning](https://www.theregister.com/Tag/Machine%20Learning/)
- [MCubed](https://www.theregister.com/Tag/MCubed/)
- [Neural Networks](https://www.theregister.com/Tag/Neural%20Networks/)
- [NLP](https://www.theregister.com/Tag/NLP/)
- [Retrieval Augmented Generation](https://www.theregister.com/Tag/Retrieval%20Augmented%20Generation/)
- [RSA Conference](https://www.theregister.com/Tag/RSA%20Conference/)
- [Star Wars](https://www.theregister.com/Tag/Star%20Wars/)
- [Tensor Processing Unit](https://www.theregister.com/Tag/Tensor%20Processing%20Unit/)
- [TOPS](https://www.theregister.com/Tag/TOPS/)
- [Zero trust](https://www.theregister.com/Tag/Zero%20trust/)

### Broader topics

- [Security](https://www.theregister.com/Tag/Security/)
- [Self-driving Car](https://www.theregister.com/Tag/Self-driving%20Car/)

#### More about

![](https://www.theregister.com/design_picker/d2e337b97204af4aa34dda04c4e5d56d954b216f/graphics/icons/social_share_icon.svg)Share

[**2**![comment bubble on white](https://www.theregister.com/design_picker/f5daacc84b9722c1e31ba85f836c37e4ad993fc4/graphics/icons/bubble_comment_white.png)\\
COMMENTS](https://forums.theregister.com/forum/all/2025/10/09/zenity_ai_agent_security_summit_recap/ "View comments on this article")

#### More about

- [AI](https://www.theregister.com/Tag/AI/)
- [Cybersecurity](https://www.theregister.com/Tag/Cybersecurity/)

More like these

×

### More about

- [AI](https://www.theregister.com/Tag/AI/)
- [Cybersecurity](https://www.theregister.com/Tag/Cybersecurity/)

### Narrower topics

- [AIOps](https://www.theregister.com/Tag/AIOps/)
- [Center for Internet Security](https://www.theregister.com/Tag/Center%20for%20Internet%20Security/)
- [DeepSeek](https://www.theregister.com/Tag/DeepSeek/)
- [Gemini](https://www.theregister.com/Tag/Gemini/)
- [Google AI](https://www.theregister.com/Tag/Google%20AI/)
- [GPT-3](https://www.theregister.com/Tag/GPT-3/)
- [GPT-4](https://www.theregister.com/Tag/GPT-4/)
- [Large Language Model](https://www.theregister.com/Tag/Large%20Language%20Model/)
- [Machine Learning](https://www.theregister.com/Tag/Machine%20Learning/)
- [MCubed](https://www.theregister.com/Tag/MCubed/)
- [Neural Networks](https://www.theregister.com/Tag/Neural%20Networks/)
- [NLP](https://www.theregister.com/Tag/NLP/)
- [Retrieval Augmented Generation](https://www.theregister.com/Tag/Retrieval%20Augmented%20Generation/)
- [RSA Conference](https://www.theregister.com/Tag/RSA%20Conference/)
- [Star Wars](https://www.theregister.com/Tag/Star%20Wars/)
- [Tensor Processing Unit](https://www.theregister.com/Tag/Tensor%20Processing%20Unit/)
- [TOPS](https://www.theregister.com/Tag/TOPS/)
- [Zero trust](https://www.theregister.com/Tag/Zero%20trust/)

### Broader topics

- [Security](https://www.theregister.com/Tag/Security/)
- [Self-driving Car](https://www.theregister.com/Tag/Self-driving%20Car/)

#### TIP US OFF

[Send us news](https://www.theregister.com/Profile/contact/)

* * *

### Other stories you might like

[![](https://regmedia.co.uk/2022/10/10/brain_shutterstock.jpg?x=150&y=100&crop=1)\\
\\
**Curl project, swamped with AI slop, finds not all AI is bad** \\
\\
Artificial intelligence works when humans use it wisely\\
\\
AI + ML7 days \| 7](https://www.theregister.com/2025/10/02/curl_project_swamped_with_ai/?td=keepreading)[![](https://regmedia.co.uk/2025/09/26/slop_tank.jpg?x=150&y=100&crop=1)\\
\\
**Many employees are using AI to create 'workslop,' Stanford study says**\\
\\
ai-pocalypse Remember when AI was supposed to make us more productive, not hate each other?\\
\\
AI + ML13 days \| 86](https://www.theregister.com/2025/09/26/ai_workslop_productivity/?td=keepreading)[![](https://regmedia.co.uk/2018/02/20/skeptical.jpg?x=150&y=100&crop=1)\\
\\
**AI gets more 'meh' as you get to know it better, researchers discover** \\
\\
Most scientists now use the tech in their work, but still question its usefulness\\
\\
AI + ML19 hrs \| 30](https://www.theregister.com/2025/10/08/more_researchers_use_ai_few_confident/?td=keepreading)[![](https://regmedia.co.uk/2017/09/07/shutterstock_cat_bye.jpg?x=150&y=100&crop=1)\\
\\
**VMware customers say bye-bye Broadcom and vote for Nutanix** \\
\\
Many seeking a replacement for VMware are turning to Nutanix as a strategic choice\\
\\
Sponsored feature](https://www.theregister.com/2025/08/26/vmware_customers_say_byebye/?td=keepreading)

[![](https://regmedia.co.uk/2023/03/26/aitraining.jpg?x=150&y=100&crop=1)\\
\\
**How chatbots are coaching vulnerable users into crisis**\\
\\
Feature From homework helper to psychological hazard in 300 hours of sycophantic validation\\
\\
AI + ML1 day \| 21](https://www.theregister.com/2025/10/08/ai_psychosis/?td=keepreading)[![](https://regmedia.co.uk/2023/11/15/china.jpg?x=150&y=100&crop=1)\\
\\
**Export controls now a key factor in AI chip development – adding risk for the whole industry**\\
\\
Analysis The physics of transistors and politics of trading licenses are colliding on the AI frontier\\
\\
Systems8 days \| 7](https://www.theregister.com/2025/10/01/the_risks_of_export_controls/?td=keepreading)[![](https://regmedia.co.uk/2025/10/03/shutterstock_2582185805.jpg?x=150&y=100&crop=1)\\
\\
**Startups binge on AI while big firms sip cautiously, study shows** \\
\\
Better hope that bubble doesn't pop\\
\\
AI + ML6 days \| 8](https://www.theregister.com/2025/10/03/startups_binge_on_ai/?td=keepreading)[![](https://regmedia.co.uk/2025/09/25/harness-unscripted.jpg?x=150&y=100&crop=1)\\
\\
**Harness pitches AI agents as your new DevOps taskmasters** \\
\\
Productivity gains promised, but humans still expected to audit the bots\\
\\
AI + ML14 days \| 2](https://www.theregister.com/2025/09/25/harness_agentic_ai_devops/?td=keepreading)

[![](https://regmedia.co.uk/2025/10/07/shutterstock_1619490175.jpg?x=150&y=100&crop=1)\\
\\
**Employees regularly paste company secrets into ChatGPT** \\
\\
Microsoft Copilot, not so much\\
\\
AI + ML2 days \| 42](https://www.theregister.com/2025/10/07/gen_ai_shadow_it_secrets/?td=keepreading)[![](https://regmedia.co.uk/2024/11/20/shutterstock_aidissapointment.jpg?x=150&y=100&crop=1)\\
\\
**McKinsey wonders how to sell AI apps with no measurable benefits** \\
\\
Consultant says software vendors risk hiking prices without cutting costs or boosting productivity\\
\\
AI + ML5 hrs \| 16](https://www.theregister.com/2025/10/09/mckinsey_ai_monetization/?td=keepreading)[![](https://regmedia.co.uk/2022/05/25/meta_facebook_logo.jpg?x=150&y=100&crop=1)\\
\\
**Meta will listen into AI conversations to personalize ads** \\
\\
Religion, race, health and other dicey topics supposedly exempt\\
\\
AI + ML8 days \| 16](https://www.theregister.com/2025/10/01/meta_ai_use_informs_ads/?td=keepreading)[![](https://regmedia.co.uk/2017/05/23/puppet-master.jpg?x=150&y=100&crop=1)\\
\\
**AI companion bots use emotional manipulation to boost usage** \\
\\
Researchers argue that this dark pattern poses a legal risk\\
\\
AI + ML1 day \| 17](https://www.theregister.com/2025/10/08/ai_bots_use_emotional_manipulation/?td=keepreading)
