---
date: '2025-10-21'
description: 'In "Follow the SCRIPT," Tal Be''ery analyzes how AI disproportionately
  benefits attackers in cybersecurity due to two key asymmetries: contextual understanding
  and permissible failure. The SCRIPT framework highlights that attackers leverage
  automated, low-context tasks while defenders rely on comprehensive, context-dependent
  analysis. This inherent structural imbalance is exacerbated by AI. Solutions include
  architectural changes like implementing MFA to complicate attacker automation and
  employing honeypots to heighten costs for attackers. Ultimately, defenders must
  innovate not merely through AI tools but by restructuring their environments to
  mitigate these asymmetries for improved resilience.'
link: https://medium.com/@TalBeerySec/follow-the-script-why-attackers-are-winning-the-ai-arms-race-39de80748d09
tags:
- Automation
- AI
- SCRIPT Framework
- Information Security
- Cybersecurity
title: 'Follow the SCRIPT: Why Attackers are Winning the AI Arms Race ◆ by Tal Be''ery
  ◆ Oct, 2025 ◆ Medium'
---

[Sitemap](https://medium.com/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F39de80748d09&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40TalBeerySec%2Ffollow-the-script-why-attackers-are-winning-the-ai-arms-race-39de80748d09&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40TalBeerySec%2Ffollow-the-script-why-attackers-are-winning-the-ai-arms-race-39de80748d09&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

# Follow the SCRIPT: Why Attackers are Winning the AI Arms Race

[![Tal Be'ery](https://miro.medium.com/v2/resize:fill:64:64/0*xv5INqVj65wt8lER.jpeg)](https://medium.com/@TalBeerySec?source=post_page---byline--39de80748d09---------------------------------------)

[Tal Be'ery](https://medium.com/@TalBeerySec?source=post_page---byline--39de80748d09---------------------------------------)

Follow

9 min read

·

1 hour ago

Listen

Share

**TL;DR: Attackers can automate perfectly with AI, while defenders can’t. This gap stems not from AI limitations but from fundamental asymmetries in how security tasks are structured. We formalize Karpathy’s heuristic into the SCRIPT framework to explain why, then show how defenders can turn the tables through architectural changes.**

AI promises to reshape many, if not all, aspects of our lives. In this post, we examine how it changes the balance of power in information security.

Information security (InfoSec) is an adversarial field where attackers and defenders engage in constant battle. The AI revolution provides new tools for both sides: for example, attackers can use AI agents to find vulnerabilities faster, while defenders can deploy AI agents to patch them. This raises a critical question: does AI favor one side over the other, or do the benefits cancel out if both sides adopt AI equally?

## Introducing the SCRIPT framework for AI’s impact evaluation

Estimating AI’s impact is notoriously difficult. In 2016, AI pioneer Geoffrey Hinton made a bold prediction:

> _We should stop training radiologists now. It’s just completely obvious that within five years, deep learning is going to do better than radiologists._

Nine years later, Hinton [admitted](https://www.nytimes.com/2025/05/14/technology/ai-jobs-radiologists-mayo-clinic.html) he was wrong, at least on the timing. AI did not replace human radiologists but instead became their assistant, making them more efficient and accurate.

### Why Hinton Was Wrong: Enter SCRIPT Framework

AI researcher [Andrej Karpathy](https://en.wikipedia.org/wiki/Andrej_Karpathy) analyzed why Hinton’s prediction failed and identified characteristics that determine whether AI will thrive in a field.

Karpathy’s tweet: The source of the SCRIPT Framework

> When looking for jobs that will change a lot due to AI on shorter time scales, I’d look in other places — jobs that look like repetition of one rote task, each task being relatively independent, closed (not requiring too much context), short (in time), forgiving (the cost of mistake is low), and of course automatable giving current (and digital) capability.

Distilling and formalizing Karpathy’s heuristic into its principal components yields the SCRIPT Framework for evaluating tasks’ suitability for AI automation:

- **Short**:brief in time
- **Closed**:requireslimited context
- **Repetitive**: repetition of one rote task
- **Independent**: standalone
- **Permissive:** forgiving of mistakes
- **Tech-ready**: digitally automatable

### **The Two Dimensions of SCRIPT**

SCRIPT’s six elements measure two fundamentally different aspects of AI automation feasibility:

**1\. Automation Readiness** (R, P, T): Is this task suitable for automation at all?

- **Repetitive**: Enables pattern learning
- **Permissive**: Tolerates trial-and-error
- **Tech-ready**: Digitally automatable

Tasks that are unique, require perfect accuracy, or involve physical components resist all automation, AI-based or others.

**2\. Context Window Fit** (S, C, I): Can this fit in an AI’s limited memory?

- **Short**: Minimal data volume
- **Closed**: Little background needed
- **Independent**: No accumulated state

Tasks requiring extensive history, correlating thousands of events, or building context over time will overflow AI’s constraints.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*fnUMo1SlUIlE1Kkgk8Rn1A.png)

## Applying the SCRIPT Framework to Information Security

### Methodology

To ensure consistent evaluation across security domains, we used Claude Sonnet 4.5 to generate SCRIPT scorecards based on structured prompts and framework definitions. We’ve made these prompts public so readers can recreate our analysis or evaluate their own security domains.

[**GitHub — talbeerysec/SCRIPT-AI-Framework: Framework for Assessing AI Automation Potential in Any…** \\
\\
**Framework for Assessing AI Automation Potential in Any Domain — talbeerysec/SCRIPT-AI-Framework**\\
\\
github.com](https://github.com/talbeerysec/SCRIPT-AI-Framework?source=post_page-----39de80748d09---------------------------------------)

### Security Domain 1: Lateral Movement

Authentication and Access Control is a fundamental pillar of information security that ensures only authorized individuals can access specific resources and data within a system. Authentication verifies a user’s identity. Access control then determines what that authenticated user is permitted to do. Together, these mechanisms form the first line of defense against unauthorized access, protecting sensitive information from breaches while enabling legitimate users to perform their necessary functions.

From attackers’ perspective, Authentication and Access Control is a challenge they need to overcome during Lateral Movement. Lateral Movement is a critical, time-consuming phase of the cyber kill-chain where attackers propagate from their initial foothold in the network periphery into the heart of the network where the victim’s high-value assets are located.

![](https://miro.medium.com/v2/resize:fit:595/0*JeLGlw23ZBgkLci7.jpg)

The Lateral movement cycle within the Cyber Kill-chain model (source: [microsoft](https://www.microsoftpressstore.com/articles/article.aspx?p=2992603&seqNum=2))

### Lateral Movement AI Automation for Attackers

Recent research demonstrates AI agents can solve Lateral Movement challenges (like the [GOAD benchmark)](https://orange-cyberdefense.github.io/GOAD/) significantly faster than skilled security professionals.

According to this tweet, AI agents solved Lateral Movement challenges in 14 minutes, compared to 12+ hours of focused work by a human red team, or >50x improvement.

This should not surprise us. We demonstrated nearly a decade ago that basic Lateral Movement in Active Directory-based networks was highly automatable using deterministic tools — long before AI entered the picture.

Our 2017 BlackHat Talk: The Industrial Revolution of Lateral Movement

Looking at the SCRIPT scorecard for attackers performing Lateral Movement, it becomes obvious why AI is highly useful for this task. Lateral Movement is ripe for automation with minimal context requirements, making AI a perfect candidate to deliver this automation.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*ioMBYtDiS2eqPhkqBNgkVQ.png)

Attackers’ Lateral Movement SCRIPT Scorecard (Graded by Claude Sonnet 4.5)

### Lateral Movement AI Automation for Defenders

Detecting and responding to Lateral Movement requires defenders to continuously monitor authentication patterns across the entire network, distinguishing legitimate administrative activity from malicious credential abuse. Analysts must correlate events across multiple systems and timeframes, building behavioral baselines that account for organizational context — user roles, current projects, business cycles, and infrastructure changes. Each suspicious authentication event demands investigation: Is this admin accessing the finance server for legitimate maintenance or using a compromised credential? The answer requires deep organizational knowledge accumulated over weeks or months. When lateral movement is detected, defenders must rapidly assess scope (which systems are compromised?), make high-stakes containment decisions (isolate systems without disrupting business?), and reconstruct attack timelines by correlating logs from dozens of sources. Throughout this process, defenders face a challenging balance: aggressive detection may generate overwhelming false positives and alert fatigue, while conservative detection risks missing more subtle attacks.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*A8Xh03gZZ-2HqN_6URwP3g.png)

Defenders’ Lateral Movement SCRIPT Scorecard (Graded by Claude Sonnet 4.5)

### The Inherent Asymmetries

Inspecting the Lateral Movement use case through the SCRIPT Framework prism reveals two fundamental asymmetries that structurally favor attackers over defenders in the AI automation era:

- **Contextual Asymmetry**: Attackers need only minimal context to execute lateral movement across hundreds of systems, easily fitting within any LLM’s context window, while defenders require rich organizational-specific contextual knowledge — user baselines, role histories, current projects, business calendars, infrastructure changes — that far exceeds context window limits and must be rebuilt continuously as organizations evolve.
- **Permissiveness Asymmetry**: Attackers can sustain many failures, needing only a single success to advance further within the victim’s network, while defenders can tolerate very few failures — missing attacks results in breaches, while excessive false positives cause alert fatigue and operational disruption.

**These asymmetries compound devastatingly and are reflected in SCRIPT scorecards.** While the exact scores might be debatable, the trend is undeniable. Attackers score perfectly on the SCRIPT framework — their tasks are repetitive, error-tolerant, brief, context-light, and independent — making them perfectly suited for AI automation at machine speed.

In contrast, defenders score moderately — their tasks demand unique contextual judgment, low-tolerance accuracy, extended investigation timelines, massive organizational context, and correlation across interdependent systems — rendering them fundamentally resistant to full AI automation.

### **The Pattern Repeats Across Information Security**

Lateral Movement isn’t an isolated case. The same asymmetries appear across information security domains:

- **Phishing**: Attackers can use AI to generate thousands of personalized, convincing phishing emails in seconds, achieving success even if only one tricks the victim. On the other hand, defenders require deep context to detect them, and blocking legitimate messages due to false positives is costly. (See full [attackers](https://htmlpreview.github.io/?https%3A%2F%2Fgithub.com%2Ftalbeerysec%2FSCRIPT-AI-Framework%2Fblob%2Fmain%2FScorecards%2Fphishing_attacker_scorecard.html=) and [defenders](https://htmlpreview.github.io/?https%3A%2F%2Fgithub.com%2Ftalbeerysec%2FSCRIPT-AI-Framework%2Fblob%2Fmain%2FScorecards%2Fphishing_defender_scorecard.html=) scorecards)
- **Vulnerability management**: While attackers and defenders can leverage similar AI tools to identify vulnerabilities, defenders then need to follow up with a context-heavy remediation process where each patch requires understanding system dependencies, business impact, compatibility matrices, maintenance windows, and rollback plans. The permissiveness asymmetry is stark too: attackers can probe everything indiscriminately, while defenders face catastrophic consequences for both poor prioritization leaving critical vulnerabilities unpatched and poor execution causing downtime.(See full [attackers](https://htmlpreview.github.io/?https%3A%2F%2Fgithub.com%2Ftalbeerysec%2FSCRIPT-AI-Framework%2Fblob%2Fmain%2FScorecards%2Fvuln_attacker_scorecard.html=) and [defenders](https://htmlpreview.github.io/?https%3A%2F%2Fgithub.com%2Ftalbeerysec%2FSCRIPT-AI-Framework%2Fblob%2Fmain%2FScorecards%2Fvuln_defender_scorecard.html=) scorecards)

**These asymmetries surely predate AI automation. Defenders always required more context and their mistakes were much more costly. However, AI automation greatly amplifies this gap thus making it unbearable for defenders.**

### **This Isn’t Temporary — It’s Structural**

The asymmetry isn’t a limitation of current AI technology — it’s a fundamental feature of the tasks themselves. Attacker tasks align with AI’s strengths: pattern matching with incomplete context and error tolerance. Defender tasks require AI’s weaknesses: contextual judgment requiring comprehensive organizational context and very high accuracy.

**This means that while defenders must invest in AI tools to improve their defenses, these tools alone cannot close the security gap that AI has widened.**

## Rewriting the terrain: How Defenders can win

We’ve shown that AI amplifies attackers’ existing advantages. However, defenders aren’t limited to merely responding to attacks. Since the battlefield exists within defenders’ own networks and systems, they can reshape its architecture to eliminate the asymmetries that empower attackers.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/0*IDqd1o5-GrBdDvVL.jpg)

Defenders need to apply architectural changes to their networks and systems to eliminate the Contextual and Permissiveness asymmetries.

Applying this insight to the Authentication and Access Control use case and its abuse by attackers during lateral movement we explored above, defenders can:

**1\. Reduce Attacker Automation**

Implement Multi-Factor Authentication (MFA) that requires human intervention, preventing attackers from automating lateral movement. Hardware tokens or biometrics break the **_Tech-Ready_** element (SCRIPT’s T) that makes attacks so automatable.

**2\. Reduce Attacker Permissiveness**

Deploy deception elements such as honeypots and honeytokens throughout the network. Access to these decoys can alert defenders with minimal context requirements. Combined with an ‘Impose Cost’ approach that eliminates attackers’ assets after detection, this significantly raises the cost of attackers’ mistakes, reduces **_Permissiveness_**(SCRIPT’s P) and turns their trial-and-error strategy into a liability.

**3\. Increase Defender Permissiveness**

Instead of blocking suspicious access outright (causing business disruption), require step-up authentication with an additional factor. This allows defenders to challenge suspicious activity aggressively without the high cost of false positives, thus reducing the problem’s **_Permissiveness_**(SCRIPT’s P) and enabling more aggressive detection.

**4\. Reduce Required Context**

Apply Least Privilege principles to eliminate unnecessary user access rights, and implement network micro-segmentation to restrict lateral movement paths. This transforms complex contextual detection questions (“Is this access legitimate?”) into simple architectural prevention rules (“Nobody should access X from Y”) and increases the problem’s **_closeness_**(SCRIPT’s C).

All of these suggested solutions existed long before AI was introduced, as the contextual and permissiveness asymmetries were not created by AI, only amplified by it. However, this new AI amplification makes applying such architectural changes much more urgent.

## Summing Up

Automation is an amplifier. When the information security battlefield favors attackers over defenders, AI automation amplifies that advantage.

The SCRIPT framework reveals how this happens: two structural asymmetries — contextual and permissiveness — align attacker tasks with AI’s strengths while defender tasks require AI’s weaknesses. Therefore, AI automation fundamentally favors attackers over defenders in information security.

The key for defenders is not adding more AI tools to match attackers’ capabilities. Instead, defenders must make architectural changes that eliminate the asymmetries themselves: break attackers’ automation, punish their trial-and-error approaches, reduce defenders’ false positive costs, and simplify detection through least privilege and segmentation. While some advanced defenders may have already reached this point, they seem to be more the exception than the rule.

**The battlefield may favor attackers today, but defenders control the terrain. By reshaping the architecture, defenders can turn AI’s own strengths against the attackers.**

## Acknowledgements

Thanks to Claude Sonnet 4.5 for multiple reviews and discussions throughout the development of this framework.

Special thanks to [@thegrugq](https://x.com/thegrugq), Dr. [Ana Polterovich](https://www.linkedin.com/in/ana-polterovich/), the Be’ery family ( [Tasfi](https://www.linkedin.com/in/tsafi-tsur-be-ery-1312123/), [Gilad](https://www.linkedin.com/in/gilad-be-ery-86b15885/)), [@ace\_\_pace](https://x.com/ace__pace), and several anonymous reviewers for their thoughtful feedback. Additional review and analysis support provided by ChatGPT and Perplexity.

[AI](https://medium.com/tag/ai?source=post_page-----39de80748d09---------------------------------------)

[Information Security](https://medium.com/tag/information-security?source=post_page-----39de80748d09---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----39de80748d09---------------------------------------)

[Automation](https://medium.com/tag/automation?source=post_page-----39de80748d09---------------------------------------)

[![Tal Be'ery](https://miro.medium.com/v2/resize:fill:96:96/0*xv5INqVj65wt8lER.jpeg)](https://medium.com/@TalBeerySec?source=post_page---post_author_info--39de80748d09---------------------------------------)

[![Tal Be'ery](https://miro.medium.com/v2/resize:fill:128:128/0*xv5INqVj65wt8lER.jpeg)](https://medium.com/@TalBeerySec?source=post_page---post_author_info--39de80748d09---------------------------------------)

Follow

[**Written by Tal Be'ery**](https://medium.com/@TalBeerySec?source=post_page---post_author_info--39de80748d09---------------------------------------)

[1K followers](https://medium.com/@TalBeerySec/followers?source=post_page---post_author_info--39de80748d09---------------------------------------)

· [130 following](https://medium.com/@TalBeerySec/following?source=post_page---post_author_info--39de80748d09---------------------------------------)

All things CyberSecurity. Security Research Manager. Co-Founder @ZenGo (KZen). Formerly, VP of Research @ Aorato acquired by @Microsoft ( MicrosoftATA)

Follow

## No responses yet

![](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

Write a response

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40TalBeerySec%2Ffollow-the-script-why-attackers-are-winning-the-ai-arms-race-39de80748d09&source=---post_responses--39de80748d09---------------------respond_sidebar------------------)

Cancel

Respond

[Help](https://help.medium.com/hc/en-us?source=post_page-----39de80748d09---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----39de80748d09---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----39de80748d09---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----39de80748d09---------------------------------------)

[Press](mailto:pressinquiries@medium.com)

[Blog](https://blog.medium.com/?source=post_page-----39de80748d09---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----39de80748d09---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----39de80748d09---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----39de80748d09---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----39de80748d09---------------------------------------)

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)
