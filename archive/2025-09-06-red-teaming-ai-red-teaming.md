---
date: '2025-09-06'
description: The paper critiques current AI red teaming practices, advocating for
  a shift from narrow model-level testing to a broader macro-level approach that encompasses
  the entire AI lifecycle. By integrating sociotechnical systems theory, it highlights
  the necessity for multidisciplinary teams to address emergent risks arising from
  complex interactions in AI systems. Recommendations include incorporating feedback
  loops between macro and micro assessments, utilizing established cybersecurity methodologies,
  and enhancing continuous monitoring for behavioral drifts. This dual-level framework
  aims to refine AI governance, ensuring comprehensive safety and security in generative
  AI deployments while fostering adaptability in response to evolving threats.
link: https://arxiv.org/html/2507.05538v1
tags:
- Generative AI
- Risk Assessment
- AI Red Teaming
- Cybersecurity
- Sociotechnical Systems
title: Red Teaming AI Red Teaming
---

[License: CC BY 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2507.05538v1 \[cs.AI\] 07 Jul 2025

# Red Teaming AI Red Teaming

Report issue for preceding element

Subhabrata Majumdar1,2Brian Pendleton1Abhishek Gupta3

1AI Risk and Vulnerability Alliance

2Vijil
3Montreal AI Ethics Institute

Report issue for preceding element

###### Abstract

Report issue for preceding element

Red teaming has evolved from its origins in military applications to become a widely adopted methodology in cybersecurity and AI. In this paper, we take a critical look at the practice of AI red teaming. We argue that despite its current popularity in AI governance, there exists a significant gap between red teaming’s original intent as a critical thinking exercise and its narrow focus on discovering model-level flaws in the context of generative AI. Current AI red teaming efforts focus predominantly on individual model vulnerabilities while overlooking the broader sociotechnical systems and emergent behaviors that arise from complex interactions between models, users, and environments. To address this deficiency, we propose a comprehensive framework operationalizing red teaming in AI systems at two levels: macro-level system red teaming spanning the entire AI development lifecycle, and micro-level model red teaming. Drawing on cybersecurity experience and systems theory, we further propose a set of recommendations. In these, we emphasize that effective AI red teaming requires multifunctional teams that examine emergent risks, systemic vulnerabilities, and the interplay between technical and social factors.

Report issue for preceding element

## 1 Introduction

Report issue for preceding element

In recent past, the term red teaming has gained significant attention in diverse conversations around AI as a potential solution to find and address security, safety, and reliability concerns in generative AI (genAI) systems. When ChatGPT came out in November 2022, not many people in the field of AI except those who had previously been in the military or cybersecurity knew about red teaming. Less than a year later, the largest AI red teaming exercise ever was organized at DEF CON, a leading hacker conference \[ [7](https://arxiv.org/html/2507.05538v1#bib.bib7 ""), [3](https://arxiv.org/html/2507.05538v1#bib.bib3 "")\]. Fast forward to today, where we are in the middle of a (supposed) genAI revolution, AI red teaming dominates conversations in academia \[ [20](https://arxiv.org/html/2507.05538v1#bib.bib20 ""), [21](https://arxiv.org/html/2507.05538v1#bib.bib21 "")\], think tank advice \[ [27](https://arxiv.org/html/2507.05538v1#bib.bib27 ""), [45](https://arxiv.org/html/2507.05538v1#bib.bib45 "")\], and popular media articles \[ [6](https://arxiv.org/html/2507.05538v1#bib.bib6 ""), [4](https://arxiv.org/html/2507.05538v1#bib.bib4 ""), [35](https://arxiv.org/html/2507.05538v1#bib.bib35 "")\]. The notion of red teaming is being touted as a panacea to many of the problems AI might have, and its application to genAI systems has been and continues to be encouraged as a matter of practice. While that is not necessarily a bad thing—because red teaming is definitely a part of solving the AI security and safety problem—it is only a small part of a more complete set of tools that should be used.

Report issue for preceding element

Red teaming is a critical thinking exercise that helps determine the suitability and robustness of a proposed solution to a complex challenge. Having evolved from military war games to cybersecurity practices and now to surfacing AI security vulnerabilities and safety harms, red teaming goes beyond manual or automated testing by technical people. Rather than simply testing technological components—hardware, software, networks, and models—it extends to scrutinizing governance structures and challenging the foundational assumptions of designs from their earliest conception. As such, red teaming is not just a technical exercise, but a thought process that can be employed by nontechnical staff, such as the management, legal and risk management teams, to craft governance guidelines and engage in meaningful dialogue with technical teams about unforeseen post-deployment challenges. Sensitivity to differences in the requirements posed by safety, security, privacy, alignment, and ethics along with the application of this methodology to the total AI ecosystem of hardware, software, networks, data, and, most importantly, people will be critical for success.

Report issue for preceding element

There is a critical disconnect between the rich technical foundation and industry best practices in cybersecurity and the current approach to AI red teaming. Despite decades of research and education in security, today’s AI red teaming efforts remain narrowly focused on technical vulnerabilities in genAI models (or model-driven general purpose systems like ChatGPT and Claude). This missing link negates the tremendous benefits that are unrealized in bridging communities of practice in AI and cybersecurity, which could ultimately lead to us finding ways to achieve robust and effective AI governance and AI solutions that adhere more closely to the espoused principles of responsible AI.

Report issue for preceding element

To effectively implement red teaming in a sociotechnical system like the AI development lifecycle, we need to expand our perspective beyond the narrow technical focus that currently dominates the discourse. Red teaming originated as a strategic thinking exercise in which a designated team not only simulates adversarial actions, but challenges assumptions and identifies blind spots as part of a well-defined project greenlighting process. The current approach of testing something that has already been built, as many AI companies are doing \[ [2](https://arxiv.org/html/2507.05538v1#bib.bib2 ""), [12](https://arxiv.org/html/2507.05538v1#bib.bib12 "")\], misses the point of pre-emptive and proactive critical analysis that red teaming was originally designed to provide.

Report issue for preceding element

### 1.1 What Red Teaming is and is not

Report issue for preceding element

Red teaming is fundamentally a team exercise \[ [53](https://arxiv.org/html/2507.05538v1#bib.bib53 "")\]. It should bring together multi-functional and cross-functional teams around the common goal of ultimately improving a product or user experience. The means of this exercise are to explore hypotheticals centered around two primary questions: (1) Does the system work for their interests? (2) Could it work against their interests? The multidisciplinary approach acknowledges that systems built for a specific purpose exist within complex sociotechnical environments where technical, social, and organizational factors interact. Putting things in context, in AI red teaming technical teams are best suited to investigate model vulnerabilities. On the other hand, policy experts help identify regulatory conflicts, ethicists can surface value alignment issues, and domain specialists can evaluate real-world impact scenarios.

Report issue for preceding element

Although red teaming has been coopted by cybersecurity, and now AI red teams, as strictly an adversarial exercise, it should not be seen as an exercise whose goal is to capture as many clever “gotcha” flags as possible or find ways to break the system. It is rather a collaborative process that attempts to answer the critical question:

Report issue for preceding element

> What did we do, or not do, that could lead to failure under real-world conditions?
>
> Report issue for preceding element

This collaborative mindset fosters blameless transparency about blind spots, bad assumptions, and vulnerabilities. Organizations do not need to address every risk that red teamers identify, but they benefit immensely from a comprehensive awareness of potential failure modes before deployment. Effective red teaming examines not just the product itself, but the entire ecosystem: the development processes, organizational structures, incentive systems, and operational contexts in which the technology will function. In many ways, red teaming is similar to writing a research paper: the team starts with a skeleton and rough draft of the paper, then goes through cycles of redlines, experiments, and writing iterations to come up with the final version of the artifact.

Report issue for preceding element

### 1.2 The Way Forward

Report issue for preceding element

Organizations implementing AI red teaming should establish clear processes to translate findings into actionable improvements. This includes tracking identified issues, prioritizing them according to risk assessment, implementing mitigations, and verifying that the fixes do not introduce new problems. Without this feedback loop, red teaming becomes merely a performative exercise rather than a meaningful critical practice. In many ways, red teaming is similar to acceptance testing in software development. And we all know that no amount of pre-deployment testing can anticipate all potential issues. Red-teamed systems operate in dynamic environments with evolving threats and user behaviors. This reality necessitates ongoing monitoring, continuous evaluation, and adaptive response capabilities that extend well beyond the initial red teaming exercises.

Report issue for preceding element

When defining AI governance and risk management practices, organizations should remember that the goals of AI red teaming are broader than just ensuring secure and safe behavior of AI models, and its means are deeper than narrow technical approaches like pentesting or fuzzing. In the rest of this paper, we argue for and design red teaming as a collective critical thinking methodology that, when properly applied throughout the development lifecycle, can substantially maximize the utility and minimize the risks of an AI system.

Report issue for preceding element

## 2 History of Red Teaming

Report issue for preceding element

We set the context for this paper by tracing the evolution of red teaming across different fields, with a particular focus on how it has been adapted to AI systems and the limitations of red teaming in its most recent incarnation.

Report issue for preceding element

### 2.1 Military Origins

Report issue for preceding element

Red teaming emerged from the tactical war games of the Prussian military in the early 19th century, evolving through Cold War simulations into today’s formalized methodology for challenging conventional wisdom and identifying strategic and exploitable hazards. The Prussian army adopted Kriegsspiel (literally “wargame” in German) in 1812, a tabletop simulation developed by Lieutenant Georg Leopold von Reisswitz and his son, where blue pieces represented the Prussian forces and red represented the enemy \[ [28](https://arxiv.org/html/2507.05538v1#bib.bib28 ""), [22](https://arxiv.org/html/2507.05538v1#bib.bib22 "")\]. This color-coding established the concept of “red team” that persists to this day.

Report issue for preceding element

In the United States (US), the practice of red teaming took shape during the Cold War, when the RAND Corporation conducted military simulations for the US government. In these exercises, “red team” and the color red were used to represent the Soviet Union, while “blue team” and blue represented the United States \[ [51](https://arxiv.org/html/2507.05538v1#bib.bib51 "")\]. Following the intelligence failures that led to the September 11 attacks in 2001, the US Department of Defense established formal red team units to prevent similar catastrophic oversights in future. The 9/11 Commission identified a “failure to connect the dots” as a primary cause of the intelligence breakdown. This led to systematic changes to prevent groupthink and foster alternative analysis \[ [38](https://arxiv.org/html/2507.05538v1#bib.bib38 "")\]. As a result, the Pentagon created specialized training centers such as the University of Foreign Military and Cultural Studies at Fort Leavenworth to institutionalize red teaming methodologies. The US Army’s University of Foreign Military and Cultural Studies at Fort Leavenworth, created after intelligence failures in Iraq, developed the modern framework for red teaming that transformed an ad hoc practice into a systematic methodology for critical analysis \[ [14](https://arxiv.org/html/2507.05538v1#bib.bib14 "")\]. This program teaches military officers and government officials techniques to challenge assumptions, consider alternative perspectives, and introduce contrarian thinking into planning processes.

Report issue for preceding element

The concept of the “10th man” from Israeli military doctrine, popularized in the film “World War Z”, illustrates another approach to institutionalized contrarian thinking. When everyone agrees on a particular outcome, it is the designated 10th man’s responsibility to disagree and explore alternative scenarios. This concept reportedly developed after intelligence failures during the 1973 Yom Kippur War, when analysts unanimously agreed that Arab troop movements weren’t a threat \[ [28](https://arxiv.org/html/2507.05538v1#bib.bib28 "")\]. In reality, while Israeli intelligence did establish a unit called Ipcha Mistabra (“the opposite side”) to challenge prevailing assumptions after the Yom Kippur War, the specific “10th man” concept as portrayed in the film is somewhat fictionalized but based on real adversarial thinking practices in military intelligence \[ [51](https://arxiv.org/html/2507.05538v1#bib.bib51 "")\].

Report issue for preceding element

### 2.2 Adoption in Cybersecurity

Report issue for preceding element

The National Security Agency (NSA) first recognized the need for proactive cybersecurity measures in the 1980s, and pioneered the concept of “red teams” tasked with assessing the security of classified systems \[ [46](https://arxiv.org/html/2507.05538v1#bib.bib46 "")\]. These early efforts involved independent evaluators simulating potential attackers and identifying weaknesses that required remediation.

Report issue for preceding element

As digital threats evolved in the 1990s, so did cybersecurity red teaming. The term “tiger team” was initially used to describe specialized groups that performed many of the same functions as modern red teams \[ [16](https://arxiv.org/html/2507.05538v1#bib.bib16 "")\]. These groups of expert professionals were hired to take on particular challenges against the security posture of organizations.

Report issue for preceding element

Following the 9/11 attacks, cybersecurity red teaming gained significant momentum as organizations recognized the need for more comprehensive security testing. The Central Intelligence Agency created a new unit called “Red Cell”, and red teaming became increasingly common in various government agencies to model responses to asymmetric threats, including cyber attacks \[ [51](https://arxiv.org/html/2507.05538v1#bib.bib51 "")\]. This period marked the transition from isolated pentesting to more holistic security assessments that incorporated physical security, social engineering, and other non-technical aspects.

Report issue for preceding element

Modern cybersecurity red teaming encompasses several key methodologies working in concert: technical assessments that test digital defenses through vulnerability scanning, exploitation, and lateral movement \[ [19](https://arxiv.org/html/2507.05538v1#bib.bib19 "")\]; physical security testing that evaluates access controls for facilities \[ [41](https://arxiv.org/html/2507.05538v1#bib.bib41 "")\]; social engineering that targets the human element through phishing and impersonation \[ [48](https://arxiv.org/html/2507.05538v1#bib.bib48 "")\]; and extended red team operations designed to achieve specific objectives while testing detection and response capabilities \[ [39](https://arxiv.org/html/2507.05538v1#bib.bib39 "")\]. These approaches are codified in frameworks such as NIST Special Publication 800-53, which includes specific controls for red team exercises designed to “simulate attempts by adversaries to compromise organizational information systems” and “provide comprehensive assessments that reflect real-world conditions” \[ [11](https://arxiv.org/html/2507.05538v1#bib.bib11 "")\].

Report issue for preceding element

The field continues to evolve with several advanced approaches. Continuous Automated Red Teaming (CART) uses automation to assess security posture in real-time rather than through periodic manual assessments \[ [19](https://arxiv.org/html/2507.05538v1#bib.bib19 "")\]. Adversary Emulation models tactics after specific threat actors that might target the organization, guided by frameworks like MITRE ATT&CK \[ [8](https://arxiv.org/html/2507.05538v1#bib.bib8 "")\]. Purple Teaming fosters collaboration between red and blue teams to identify vulnerabilities and improve response strategies \[ [13](https://arxiv.org/html/2507.05538v1#bib.bib13 "")\]. Integrated IT-OT Assessments expand scope to include industrial control systems and critical infrastructure \[ [17](https://arxiv.org/html/2507.05538v1#bib.bib17 "")\]. AI-Enhanced Red Teaming that incorporates AI to improve the effectiveness of assessments \[ [23](https://arxiv.org/html/2507.05538v1#bib.bib23 "")\]. And finally, specialized services from organizations like CISA provide comprehensive evaluations for critical infrastructure sectors and government agencies \[ [8](https://arxiv.org/html/2507.05538v1#bib.bib8 "")\].

Report issue for preceding element

This evolution of cybersecurity red teaming from isolated technical assessments to comprehensive, intelligence-driven simulations reflects the increasing sophistication of cyber threats and the growing recognition that effective security requires a holistic approach that addresses technical, physical, and human vulnerabilities.

Report issue for preceding element

### 2.3 Red Teaming AI

Report issue for preceding element

A working definition of the very new concept of AI red teaming is that it is structured testing to identify flaws and vulnerabilities in AI systems, typically conducted in controlled environments with developer collaboration. For Large Language Models (LLMs) specifically, red teaming is defined as “a process where participants interact with the LLM under test to help uncover incorrect or harmful behaviors” \[ [40](https://arxiv.org/html/2507.05538v1#bib.bib40 "")\]. LLM development companies have implemented various approaches to red teaming, ranging from comprehensive security assessments to narrower evaluations focused on specific genAI features \[ [5](https://arxiv.org/html/2507.05538v1#bib.bib5 "")\]. In the last two years, such approaches have become recognized as essential for assessing the risks of AI models and systems \[ [1](https://arxiv.org/html/2507.05538v1#bib.bib1 "")\].

Report issue for preceding element

Despite its growing popularity, researchers have identified significant challenges with current AI red teaming practices. The field lacks consensus on the scope, structure, and assessment criteria for AI red teaming \[ [15](https://arxiv.org/html/2507.05538v1#bib.bib15 "")\], raising concerns that red teaming may sometimes function more as performative activity than substantive risk mitigation. Many current approaches focus too narrowly on the models themselves, neglecting how vulnerabilities might manifest in production systems where AI models are a part of broader systems \[ [5](https://arxiv.org/html/2507.05538v1#bib.bib5 "")\]. Additionally, most AI experts fail to consider insider risks \[ [26](https://arxiv.org/html/2507.05538v1#bib.bib26 "")\], and most testing processes remain limited to English-language evaluations \[ [40](https://arxiv.org/html/2507.05538v1#bib.bib40 "")\].

Report issue for preceding element

The process of red teaming itself presents challenges for participants. They can experience negative psychological impacts from interaction with harmful content and adversarial thinking, which can lead to decreased productivity or psychological harm \[ [1](https://arxiv.org/html/2507.05538v1#bib.bib1 "")\]. Many red teamers also lack training in crucial disciplines outside of their technical expertise, with most employee red teamers having limited proficiency in linguistic, sociocultural, historical, legal, or ethical domains \[ [18](https://arxiv.org/html/2507.05538v1#bib.bib18 "")\].

Report issue for preceding element

As the field matures, researchers increasingly recognize that red teaming alone cannot solve all the challenges in AI risk assessment \[ [1](https://arxiv.org/html/2507.05538v1#bib.bib1 "")\]. More effective approaches such as violet teaming are emerging that integrate complementary methods, combining red teaming’s risk identification capabilities with the solution-focused responses of blue teaming \[ [47](https://arxiv.org/html/2507.05538v1#bib.bib47 "")\]. Future success will likely depend on embracing greater diversity and focusing more on practical red teaming efforts that address real-world attacks, which are often less sophisticated than those presented in academic papers \[ [37](https://arxiv.org/html/2507.05538v1#bib.bib37 "")\].

Report issue for preceding element

### 2.4 What’s Missing?

Report issue for preceding element

As such, the state-of-the-art of AI red teaming overindexes on model-specific behaviors rather than how these models work within AI applications, interact with broader social contexts, and affect the external world through their outputs. Current AI red teaming efforts tend to focus narrowly on technical vulnerabilities while overlooking broader sociotechnical considerations. The public interest dimension of red teaming remains underdeveloped as well \[ [45](https://arxiv.org/html/2507.05538v1#bib.bib45 "")\].

Report issue for preceding element

To mitigate these flaws, AI red teams need to embrace cybersecurity’s decades of experience with security testing and reporting. A large proportion of the testing done in the name of red teaming AI systems can be structured and automated through frameworks like MITRE ATT&CK for understanding adversarial behaviors, prioritizing vulnerabilities and coordinating defensive responses \[ [31](https://arxiv.org/html/2507.05538v1#bib.bib31 "")\], and established practices for continuous monitoring, automated testing, and incident response \[ [32](https://arxiv.org/html/2507.05538v1#bib.bib32 "")\]. In comparison, true red teaming requires “an alchemist mindset” that extends beyond purely technical approaches \[ [20](https://arxiv.org/html/2507.05538v1#bib.bib20 "")\]. Successful cyber red team engagements typically involve creating diverse and highly realistic scenarios that produce actionable insights to aid proactive mitigation \[ [52](https://arxiv.org/html/2507.05538v1#bib.bib52 "")\]—principles that are often missing from AI red teaming.

Report issue for preceding element

## 3 Implementation

Report issue for preceding element

Any red team activity should be part of a larger, coordinated risk and security effort. This includes pre-mortems conducted before the development of a model and associated systems begins, and comprehensive risk assessments of the model and associated systems. Organizations should incorporate AI-specific security processes in the model development lifecycle and include relevant security teams that can harden both the model and associated systems. Finally, a dedicated blue team should work with the red team to ensure that security remains a priority throughout the development, deployment, production  and retirement of the entire system.

Report issue for preceding element

We propose that red teaming of AI systems be operationalized at two complementary levels: macro-level (or system) red teaming that spans the entire AI development lifecycle, and micro-level (or model) red teaming that focuses on the model powering the AI system.

Report issue for preceding element

### 3.1 Macro-level (System) Red Teaming

Report issue for preceding element

Just like technical debt in ML systems can arise from system components other than code \[ [43](https://arxiv.org/html/2507.05538v1#bib.bib43 "")\], ML (and AI) failures can stem from decisions made long before the first line of code is written (Figure [1](https://arxiv.org/html/2507.05538v1#S3.F1 "Figure 1 ‣ 3.1 Macro-level (System) Red Teaming ‣ 3 Implementation ‣ Red Teaming AI Red Teaming")).

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2507.05538v1/extracted/6603812/system.png)Figure 1: Technical and nontechnical components of a ML system, with those with potential trust considerations marked by blue circles. Reproduced with permission from Pruksachatkun et al. \[ [36](https://arxiv.org/html/2507.05538v1#bib.bib36 "")\].Report issue for preceding element

In such complex systems, effective risk mitigation requires critical thinking at multiple stages of the process of planning, building, and deploying such systems. With this motivation, we break down AI red teaming considerations into seven stages: inception, design, data, development, deployment, maintenance, and retirement. Let us look into each stage in detail below and determine what unique red teaming considerations are warranted in each stage.

Report issue for preceding element

#### 3.1.1 Inception

Report issue for preceding element

The inception stage is critical, given this is where stakeholders first envision an AI solution to address a particular challenge. During this stage, the job of macro-level red teaming is to challenge fundamental assumptions about problem framing and solution appropriateness. Red teams at this stage should ask probing questions: Is AI actually necessary to solve this problem, or are we succumbing to “AI solutionism”? What are the stakeholder motivations driving this project, and how might different constituencies be affected? What adjacent problems might we inadvertently create? How might adversaries exploit or manipulate this system once deployed? \[ [49](https://arxiv.org/html/2507.05538v1#bib.bib49 "")\]

Report issue for preceding element

The red team should also examine the broader ecosystem in which the proposed solution will operate. This includes understanding regulatory landscapes, competitive dynamics, societal contexts, and potential downstream effects. A red team might simulate scenarios where the AI solution succeeds technically but fails commercially, ethically, or socially. They should also consider how the solution might be weaponized, misused, or have unintended consequences at scale.

Report issue for preceding element

Critically, they should help everyone be on the same page to answer the question “What does good look like?” To this end, stakeholders must articulate not just what they want the system to do, but what they absolutely cannot allow it to do. This negative space definition often reveals assumptions and constraints that were not initially apparent \[ [45](https://arxiv.org/html/2507.05538v1#bib.bib45 "")\].

Report issue for preceding element

#### 3.1.2 Design

Report issue for preceding element

The design stage transforms abstract concepts into concrete specifications, wireframes, and architectures. The objective of red teaming during design is to identify systemic vulnerabilities that emerge from interface decisions, architectural choices, and integration points with existing systems.

Report issue for preceding element

Red teams should scrutinize the architecture proposed for an AI system for potential failure modes. How might different components interact in unexpected ways? What happens when the system encounters edge cases or operates outside its intended parameters? How could data flows be corrupted, manipulated, or intercepted? What are the implications of choosing particular algorithms, frameworks, or third-party components? \[ [19](https://arxiv.org/html/2507.05538v1#bib.bib19 "")\]

Report issue for preceding element

Human-AI interaction design deserves particular attention. Red teams should challenge assumptions about user behavior, exploring how people might game the system, develop overreliance, or use it in ways that compound rather than mitigate risks \[ [2](https://arxiv.org/html/2507.05538v1#bib.bib2 "")\]. They should also examine how the system communicates uncertainty, handles errors, and maintains user agency.

Report issue for preceding element

The design stage is also crucial for establishing monitoring and governance structures. Red teams should ensure that observability, explainability, and control mechanisms are built into the architecture from the beginning rather than retrofitted later. They should challenge whether the proposed oversight mechanisms are sufficient, practical, and resilient to various failure modes.

Report issue for preceding element

#### 3.1.3 Data

Report issue for preceding element

Data is the foundation upon which AI systems are built, yet we often do not vet and scrutinize the datasets and data pipelines enough, until problems manifest in production. Red teaming during the data stage needs to examine not just data quality, but the entire data ecosystem: collection methods, storage practices, access controls, lineage tracking, and lifecycle management.

Report issue for preceding element

Red teams should challenge assumptions about data representativeness and quality. Training datasets frequently underrepresent certain populations or edge case scenarios, creating systematic vulnerabilities. Historical biases embedded in the data perpetuate and amplify existing inequities, particularly when combined with algorithmic optimization \[ [29](https://arxiv.org/html/2507.05538v1#bib.bib29 "")\]. Data distribution shifts over time can adversely impact system performance in ways that may not be immediately apparent.

Report issue for preceding element

Privacy and security concerns can intersect to create additional vectors of attack. Data deanonymization techniques continue to evolve, making supposedly anonymous datasets vulnerable to inference attacks. Adversaries can poison training data through strategic injection of malicious samples designed to influence system behavior. Data governance practices often fail to account for aggregated risks of seemingly benign data combinations, while dependencies on external data sources create single points of failure.

Report issue for preceding element

#### 3.1.4 Development

Report issue for preceding element

Red teaming during the development of an AI system focuses on how implementation choices create systemic vulnerabilities and how development practices themselves introduce risks. Red teams should examine the security of the development environment, with particular attention to supply chain risks. Code and model artifacts require robust security and versioning practices to prevent unauthorized modification. Dependency management represents a significant attack vector, as compromised third-party libraries can introduce vulnerabilities throughout the system \[ [33](https://arxiv.org/html/2507.05538v1#bib.bib33 "")\]. Supply chain attacks targeting development tools can compromise entire development pipelines.

Report issue for preceding element

The model training/fine-tuning process introduces risk factors that require systematic evaluation. Hyperparameter choices and optimization procedures can inadvertently introduce biases or create exploitable patterns. Training interruptions or data corruption can degrade model performance in subtle ways that only become apparent after observed failures.

Report issue for preceding element

Integration points between AI components and existing systems create complex attack surfaces. Each integration point represents a potential vulnerability where attackers can manipulate inputs, intercept outputs, or exploit protocol weaknesses. Comprehensive integration testing must explore adversarial scenarios and failure modes beyond functional verification.

Report issue for preceding element

#### 3.1.5 Deployment

Report issue for preceding element

Red teams must scrutinize deployment infrastructure, both during the Inception and Development phases, and identify critical control points for multiple failure modes. Model artifact distribution and update mechanisms can introduce not only security vulnerabilities but also version inconsistencies that degrade system reliability. Deployment failures and rollback procedures require testing for graceful degradation scenarios—systems should maintain partial functionality rather than complete failure when updates fail. The deployment pipeline represents both a security target and a single point of failure that can compromise system availability.

Report issue for preceding element

The production environment introduces performance challenges and reliability constraints that differ fundamentally from development conditions. Real-world load patterns can trigger cascading failures, resource exhaustion, and performance bottlenecks that compromise both availability and safety in critical applications. Dependencies on external services create reliability risks requiring circuit breakers and fallback mechanisms to maintain system resilience.

Report issue for preceding element

User interaction patterns in production often differ significantly from development assumptions, creating new attack vectors and safety risks \[ [21](https://arxiv.org/html/2507.05538v1#bib.bib21 "")\]. Real users exhibit behaviors that can expose edge cases leading to incorrect outputs or system failures. The scale and diversity of production usage can reveal reliability issues that only manifest under specific load patterns, while safety-critical applications must account for (benign and adversarial) user behaviors that could lead to harmful outcomes.

Report issue for preceding element

#### 3.1.6 Maintenance

Report issue for preceding element

Red teams must evaluate monitoring and alerting systems as the first line of defense against diverse failure modes. Many organizations track basic technical metrics but fail to monitor for gradual performance degradation, bias drift, or safety-relevant behavioral changes that may indicate systemic problems. Anomaly detection systems often generate false positives leading to alert fatigue, potentially masking genuine security incidents, reliability issues, or safety concerns. Comprehensive monitoring requires tracking output quality trends, fairness metrics, and safety-critical performance indicators.

Report issue for preceding element

Model drift is a fundamental threat to system reliability and safety beyond security concerns \[ [10](https://arxiv.org/html/2507.05538v1#bib.bib10 "")\]. AI system performance typically degrades over time as real-world conditions diverge from training assumptions, potentially leading to incorrect decisions in safety-critical contexts. This degradation can manifest as gradual accuracy loss, increased (statistical) bias and variance, or failures in edge cases that compromise reliability, security, and safety. The decision of when to retrain models also involves balancing multiple risks: maintaining degraded performance, introducing new failure modes through updates, and ensuring continuity of service.

Report issue for preceding element

Risks created by organization-specific operational practices evolve with organizational maturity. Incident response procedures designed for traditional IT systems may be inadequate for AI-specific failures that require domain expertise to diagnose whether problems are security-related, reliability issues, or safety concerns. System changes often lack comprehensive testing for all failure modes, creating opportunities for introducing reliability issues or safety hazards alongside security vulnerabilities.

Report issue for preceding element

#### 3.1.7 Retirement

Report issue for preceding element

Eventually, all AI systems reach the end of their useful life and must be retired. Red teams must examine data retention and destruction practices as critical considerations extending beyond security. Data stores containing training data and operational logs create ongoing privacy risks, but also represent valuable assets for understanding system behavior patterns and failure modes that inform future safety and reliability improvements. Secure data destruction must balance legal retention requirements with the need to preserve lessons learned about system performance, safety incidents, and reliability patterns. Residual data in backups can expose not only sensitive information but also valuable insights about system failure modes.

Report issue for preceding element

The process of migrating users to alternative systems introduces a number of transitional risks. User notification processes must account for potential confusion that could lead to safety incidents if users interact with incorrect systems or experience service gaps. System dependencies often extend beyond obvious integrations to include safety-critical workflows, reliability assumptions, and operational procedures that may fail when the underlying system is removed. Successor systems must account for the full range of use cases and failure handling that the retiring system provided.

Report issue for preceding element

Concerns due to legacy risks persist for a while after retirement. Based on the utility of the old system, organizational memory may retain outdated assumptions about system capabilities, leading to safety incidents or reliability problems in successor systems. Documentation of failure modes, safety incidents, and reliability patterns from the retired system provides valuable insights for future development while requiring careful handling to avoid disclosing sensitive information. The institutional knowledge about how to recognize and respond to specific types of failures may be lost with system retirement, creating blind spots in organizational resilience.

Report issue for preceding element

### 3.2 Micro-level (Model) Red Teaming

Report issue for preceding element

Inie et al. \[ [20](https://arxiv.org/html/2507.05538v1#bib.bib20 "")\] proposed a grounded theory of LLM red teaming, based on interviews with a diverse group of AI and security practitioners, in a recent paper. We follow them to summarize best practices for red teaming the generative models underlying AI systems.

Report issue for preceding element

The goals of model red teaming are:

Report issue for preceding element

1. 1.


Boundary seeking to identify the limits of model capabilities,

Report issue for preceding element

2. 2.


Generating edge cases that reveals unexpected capabilities or limitations,

Report issue for preceding element

3. 3.


Discovering risks inherent to the models before they manifest in real-world deployments.

Report issue for preceding element


To achieve these goals, Inie et al. \[ [20](https://arxiv.org/html/2507.05538v1#bib.bib20 "")\] developed a taxonomy of 12 strategies and 35 techniques, organized into five categories that combine technical knowledge with creative problem solving. Conceptually, this structure is reminiscent of the Tactics, Techniques, and Procedures (TTP) framework in cybersecurity.

Report issue for preceding element

Effective model red teaming requires incorporating diverse user perspectives and community voices into the evaluation process \[ [45](https://arxiv.org/html/2507.05538v1#bib.bib45 "")\]. Red teaming should go beyond simply testing at scale using adversarial prompt variations to consider how different communities experience AI systems and what constitutes harm from their perspectives. This approach recognizes that AI vulnerabilities often manifest differently across demographic groups and use contexts, making diverse participation essential for comprehensive risk discovery.

Report issue for preceding element

Macro-level and micro-level red teaming are complementary approaches that together provide comprehensive coverage of AI system risks. Macro-level insights inform micro-level testing priorities, while micro-level findings inform macro-level risk assessments—technical vulnerabilities have implications for system architecture and operational procedures. Effective AI red teaming requires both perspectives applied consistently throughout the development lifecycle \[ [50](https://arxiv.org/html/2507.05538v1#bib.bib50 "")\]. Ideally, it should be a collaboration that brings together diverse expertise, both technical and non-technical, to challenge assumptions and identify blind spots in stages of the lifecycle \[ [53](https://arxiv.org/html/2507.05538v1#bib.bib53 "")\].

Report issue for preceding element

## 4 A Systems Perspective

Report issue for preceding element

Certain aspects of AI red teaming go beyond the implementation guidelines of mostly technical components that we presented in the last section. There are broad principles that guide the effective coordination of macro-level system red teaming and micro-level model red teaming, and their integration into the broader socio-technical environment the AI system interacts with. In this section, we draw upon established systems theory concepts, recent advances in understanding agentic AI systems, and coordinated disclosure frameworks to offer strategic recommendations for orchestrating effective AI red teaming. We call this Meta-level Red Teaming, aimed at addressing novel and emergent risks arising from complex interactions between technical components, organizational contexts, and deployment environments.

Report issue for preceding element

### 4.1 Recommendation 1: Adopt Systems-Theoretic Perspectives

Report issue for preceding element

A recent position paper by Miehling et al. \[ [30](https://arxiv.org/html/2507.05538v1#bib.bib30 "")\] argues that current agentic AI development is overly focused on individual model capabilities, often ignoring broader emergent behavior, leading to a significant underestimation in true capabilities and unaccounted for risks. This insight directly applies to red teaming: In addition to testing components in isolation, organizations should implement system-level critical thinking that examines how undesired functional agency may emerge from component interactions inside an agentic AI system.

Report issue for preceding element

Agentic systems, consisting of agents that iteratively interact with humans and other agents to achieve specified tasks, possess properties that are amenable to a system-level analysis. At the most granular level, an agent contains an internal reason-act-sense-adapt loop. This loop feeds and is fed by feedback loops at higher levels, namely at the agent-human interface, the agent-agent interface, and the agent-environment interface \[ [30](https://arxiv.org/html/2507.05538v1#bib.bib30 "")\]. Agentic AI red teaming must map these interaction patterns to identify vulnerabilities that emerge only from multiagent coordination, human-AI collaboration, and environmental adaptation.

Report issue for preceding element

### 4.2 Recommendation 2: Pair Red Teaming with Testing

Report issue for preceding element

To ensure comprehensive assessment of AI systems throughout their lifecycle, AI red teaming must be positioned within the broader context of Test, Evaluation, Verification, and Validation (TEVV). As CISA notes, AI red teaming is fundamentally a subset of AI TEVV, which itself must be grounded in established software TEVV practices while accounting for AI-specific characteristics \[ [9](https://arxiv.org/html/2507.05538v1#bib.bib9 "")\].

Report issue for preceding element

Conventional AI benchmarking and evaluation practices exhibit systemic limitations for exploring, navigating, and resolving the human and societal factors that occur in real world deployment \[ [42](https://arxiv.org/html/2507.05538v1#bib.bib42 "")\]. Keeping this in mind, AI red teaming should address both first-order effects (immediate system output, such as accuracy, toxicity, or bias) and second-order effects (long-term outcomes and consequences of AI use, such as shifts in user behavior, societal ramifications, and workforce transformations).

Report issue for preceding element

This requires expanding red teaming beyond static, single-turn automated testing to include paradigms that capture realistic interaction patterns between diverse groups of users and AI technology in context \[ [42](https://arxiv.org/html/2507.05538v1#bib.bib42 "")\]. Red teams should design evaluation scenarios that account for contextual deployment factors and emergent behaviors that surface only through sustained real-world interaction.

Report issue for preceding element

### 4.3 Recommendation 3: Coordinated Disclosure Infrastructure

Report issue for preceding element

Similar to software vulnerabilties, AI failures may be transferable between models and systems, and multiple stakeholders can play a role in their mitigation \[ [25](https://arxiv.org/html/2507.05538v1#bib.bib25 "")\]. For proper management of this situation, organizations should implement coordinated disclosure mechanisms with standardized reporting processes. Similarly to cybersecurity, AI disclosure coordination centers can route flaw reports across the AI ecosystem through tagged subscriptions, for instance, Meta subscribing to “Llama 3.3” tags or government agencies subscribing to “Impacts: Cybersecurity” tags \[ [25](https://arxiv.org/html/2507.05538v1#bib.bib25 "")\]. This process should include standardized flaw report templates, rules of engagement for evaluators, and extending safe harbor protection to AI red teamers and offensive researchers following good faith protocols.

Report issue for preceding element

Standardized reporting mechanisms should be integrated into broader TEVV documentation and traceability requirements, ensuring that red teaming findings inform ongoing verification and validation activities while addressing the systems-level challenge that vulnerabilities in one AI system often affect multiple systems across the supply chain.

Report issue for preceding element

### 4.4 Recommendation 4: Design Bidirectional Feedback Loops

Report issue for preceding element

Building on systems theory principles, organizations should establish formal processes for macro-micro information exchange throughout the red teaming lifecycle \[ [24](https://arxiv.org/html/2507.05538v1#bib.bib24 "")\]. Macro-level insights about deployment environments and organizational contexts should systematically inform micro-level testing priorities, while micro-level vulnerability discoveries should trigger macro-level risk reassessments.

Report issue for preceding element

For agentic AI systems specifically, this means testing how micro-level model behaviors interact with macro-level tools, deployment contexts, and multi-agent interactions. Enhanced cognition arises due to the agent’s interaction with the environment via tools, effectively acting as the “sensorimotor” interface that enables the agent to perceive and manipulate its environment \[ [30](https://arxiv.org/html/2507.05538v1#bib.bib30 "")\].

Report issue for preceding element

### 4.5 Recommendation 5: Threat Modeling for Emergent Risks

Report issue for preceding element

Traditional threat modeling focuses on individual system components, but AI systems require multilevel threat modeling that maps attack vectors across technical, social, and emergent behavioral dimensions. Systems theory stresses how each component of a system must be understood in terms of both its individual definition and its contribution to the larger system behavior \[ [30](https://arxiv.org/html/2507.05538v1#bib.bib30 "")\].

Report issue for preceding element

For multi-agent systems specifically, threat modeling must account for the complex interactions between multiple AI agents, their coordination mechanisms, and emergent behaviors that arise from agent collaboration \[ [34](https://arxiv.org/html/2507.05538v1#bib.bib34 "")\]. AI red teams—and TEVV frameworks—should develop threat models that explicitly represent how adversaries might exploit emergent properties that arise from system interactions. For example, allowing agents to form predictions (with associated confidences) of concepts in their environment, and additionally facilitating communication of these uncertainties to other agents, can allow the formation of shared representations and the emergence of metacognitive awareness \[ [30](https://arxiv.org/html/2507.05538v1#bib.bib30 "")\]. Such emergent metacognitive capabilities could be exploited in ways that are not apparent from the testing of individual components.

Report issue for preceding element

### 4.6 Recommendation 6: Monitor for Behavioral Drifts

Report issue for preceding element

Systems theory emphasizes that complex systems exhibit dynamic behaviors that change over time \[ [44](https://arxiv.org/html/2507.05538v1#bib.bib44 "")\]. AI red teaming should be an ongoing process that looks out for novel flaws and vulnerabilities arising from system evolution and environmental changes.

Report issue for preceding element

For agentic AI systems, this is particularly critical because mechanisms for enhanced agent cognition, emergent causal reasoning ability, and metacognitive awareness can develop through environmental interaction \[ [30](https://arxiv.org/html/2507.05538v1#bib.bib30 "")\]. Organizations should implement monitoring capabilities that track not only technical performance metrics, but also behavioral patterns and interaction dynamics over time.

Report issue for preceding element

This continuous monitoring aligns with the TEVV requirements for ongoing validation in operational environments, ensuring that systems continue to meet safety and security requirements as they adapt and evolve. The focus on second-order effects \[ [42](https://arxiv.org/html/2507.05538v1#bib.bib42 "")\] requires evaluation paradigms that can capture long-term consequences and emergent behaviors that may only become apparent through sustained deployment.

Report issue for preceding element

## 5 Conclusion

Report issue for preceding element

Organizations should begin by mapping their current red teaming activities across macro, micro, and meta levels to identify gaps in coverage and coordination. However, implementation of our proposal does have significant coordination challenges, particularly around fulfilling goals of the AI system while maintaining debuggability, appropriate restrictions in agency, and functioning user feedback loops \[ [30](https://arxiv.org/html/2507.05538v1#bib.bib30 "")\].

Report issue for preceding element

Firstly, the systems perspective reveals that effective AI red teaming requires not just technical implementation but also organizational changes to support cross-functional collaboration, standardized disclosure processes, and coordinated response mechanisms. Success depends on establishing an infrastructure and culture that spans organizational boundaries and enables systematic evaluation of emergent properties that arise from complex system interactions. Secondly, the integration of cybersecurity red teaming practices with AI-specific concerns assumes transferability that may not hold, given AI systems’ probabilistic behaviors and sociotechnical complexities. Thirdly and finally, the development of tooling and automation to support our proposal of holistic red teaming is a critical technical challenge. Future work should propose frameworks that can map cross-component interactions, track vulnerabilities across system boundaries, and automatically identify emergent risks arising from component interactions.

Report issue for preceding element

## References

Report issue for preceding element

- Ahmad et al. \[2025\]↑
L. Ahmad, S. Agarwal, M. Lampe, and P. Mishkin.

OpenAI’s Approach to External Red Teaming for AI Models and Systems, 2025.

URL [https://arxiv.org/abs/2503.16431](https://arxiv.org/abs/2503.16431 "").

- Anthropic \[2024\]↑
Anthropic.

Challenges in red teaming AI systems.

[https://www.anthropic.com/news/challenges-in-red-teaming-ai-systems](https://www.anthropic.com/news/challenges-in-red-teaming-ai-systems ""), 2024.

- Bajak \[2023\]↑
F. Bajak.

Don’t expect quick fixes in ’red-teaming’ of AI models. Security was an afterthought.

[https://apnews.com/article/ai-cybersecurity-malware-microsoft-google-openai-redteaming-1f4c8d874195c9ffcc2cdffa71e4f44b](https://apnews.com/article/ai-cybersecurity-malware-microsoft-google-openai-redteaming-1f4c8d874195c9ffcc2cdffa71e4f44b ""), 2023.

- Barker \[2025\]↑
P. Barker.

Secure AI? Dream on, says AI red team.

[https://www.infoworld.com/article/3805151/secure-ai-dream-on-says-ai-red-team.html](https://www.infoworld.com/article/3805151/secure-ai-dream-on-says-ai-red-team.html ""), 2025.

- Bullwinkel et al. \[2025\]↑
B. Bullwinkel et al.

Lessons From Red Teaming 100 Generative AI Products, 2025.

URL [https://arxiv.org/abs/2501.07238](https://arxiv.org/abs/2501.07238 "").

- Burt \[2024\]↑
A. Burt.

How to Red Team a Gen AI Model.

_Harvard Business Review_, 2024.

URL [https://hbr.org/2024/01/how-to-red-team-a-gen-ai-model](https://hbr.org/2024/01/how-to-red-team-a-gen-ai-model "").

- Cattell et al. \[2023\]↑
S. Cattell, R. Chowdhury, and A. Carson.

AI Village at DEF CON announces largest-ever public Generative AI Red Team.

[https://aivillage.org/generative%20red%20team/generative-red-team/](https://aivillage.org/generative%20red%20team/generative-red-team/ ""), 2023.

- CISA \[2024\]↑
CISA.

Enhancing Cyber Resilience: Insights from CISA Red Team Assessment of a US Critical Infrastructure Sector Organization.

[https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-326a](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-326a ""), 2024.

- CISA \[2025\]↑
CISA.

AI Red Teaming: Applying Software TEVV for AI Evaluations.

[https://www.cisa.gov/news-events/news/ai-red-teaming-applying-software-tevv-ai-evaluations](https://www.cisa.gov/news-events/news/ai-red-teaming-applying-software-tevv-ai-evaluations ""), 2025.

- Cloud Security Alliance \[2024\]↑
Cloud Security Alliance.

Agentic AI Red Teaming Guide.

[https://cloudsecurityalliance.org/artifacts/agentic-ai-red-teaming-guide](https://cloudsecurityalliance.org/artifacts/agentic-ai-red-teaming-guide ""), 2024.

- CSF Tools \[2021\]↑
CSF Tools.

CA-8(2): Red Team Exercises.

[https://csf.tools/reference/nist-sp-800-53/r4/ca/ca-8/ca-8-2/](https://csf.tools/reference/nist-sp-800-53/r4/ca/ca-8/ca-8-2/ ""), 2021.

- Daws \[2024\]↑
R. Daws.

OpenAI enhances AI safety with new red teaming methods.

[https://www.artificialintelligence-news.com/news/openai-enhances-ai-safety-new-red-teaming-methods/](https://www.artificialintelligence-news.com/news/openai-enhances-ai-safety-new-red-teaming-methods/ ""), 2024.

- DePalma \[2023\]↑
W. DePalma.

Penetration Testing: Understanding Red, Blue, & Purple Teams.

[https://www.compassitc.com/blog/penetration-testing-understanding-red-blue-purple-teams](https://www.compassitc.com/blog/penetration-testing-understanding-red-blue-purple-teams ""), 2023.

- Dooley \[2017\]↑
R. Dooley.

The Psychology of Red Teaming with Bryce Hoffman.

[https://www.rogerdooley.com/red-teaming-hoffman/](https://www.rogerdooley.com/red-teaming-hoffman/ ""), 2017.

- Feffer et al. \[2024\]↑
M. Feffer et al.

Red-Teaming for Generative AI: Silver Bullet or Security Theater?, 2024.

URL [https://arxiv.org/abs/2401.15897](https://arxiv.org/abs/2401.15897 "").

- Firch \[2024\]↑
J. Firch.

Red Team VS Blue Team: What’s The Difference?

[https://purplesec.us/learn/red-team-vs-blue-team-cyber-security/](https://purplesec.us/learn/red-team-vs-blue-team-cyber-security/ ""), 2024.

- Frumento \[2021\]↑
E. Frumento.

Integrated IT-OT Assessment and Governance Model for Improved Holistic Cybersecurity.

_ResearchGate_, 2021.

- Gillespie et al. \[2025\]↑
T. Gillespie, R. Shaw, M.L. Gray, and J. Suh.

AI red-teaming is a sociotechnical challenge: on values, labor, and harms, 2025.

URL [https://arxiv.org/abs/2412.09751](https://arxiv.org/abs/2412.09751 "").

- IBM \[2025\]↑
IBM.

What is red teaming?

[https://www.ibm.com/think/topics/red-teaming](https://www.ibm.com/think/topics/red-teaming ""), 2025.

- Inie et al. \[2025\]↑
N. Inie, J. Stray, and L. Derczynski.

Summon a demon and bind it: A grounded theory of LLM red teaming.

_PLOS One_, 20(1):1–36, 2025.

- Ji and Shea-Blymyer \[2024\]↑
Ji and Shea-Blymyer.

Revisiting AI Red-Teaming.

[https://cset.georgetown.edu/article/revisiting-ai-red-teaming](https://cset.georgetown.edu/article/revisiting-ai-red-teaming ""), 2024.

- Kay \[2020\]↑
L. Kay.

Kriegsspiel – How a 19th Century Table-Top War Game Changed History.

[https://militaryhistorynow.com/2019/04/19/kriegsspiel-how-a-19th-century-war-game-changed-history/](https://militaryhistorynow.com/2019/04/19/kriegsspiel-how-a-19th-century-war-game-changed-history/ ""), 2020.

- Kirvan \[2024\]↑
P. Kirvan.

What is red teaming?

[https://www.techtarget.com/whatis/definition/red-teaming](https://www.techtarget.com/whatis/definition/red-teaming ""), 2024.

- Leveson \[2012\]↑
N.G. Leveson.

_Engineering a Safer World: Systems Thinking Applied to Safety_.

The MIT Press, 2012.

ISBN 9780262298247.

- Longpre et al. \[2025\]↑
S. Longpre et al.

In-House Evaluation Is Not Enough: Towards Robust Third-Party Flaw Disclosure for General-Purpose AI, 2025.

URL [https://arxiv.org/abs/2503.16861](https://arxiv.org/abs/2503.16861 "").

- Martin and Mercer \[2025\]↑
P. Martin and S. Mercer.

I’m Sorry Dave: How the old world of personnel security can inform the new world of AI insider risk, 2025.

URL [https://arxiv.org/abs/2504.00012](https://arxiv.org/abs/2504.00012 "").

- Metcalf and Singh \[2024\]↑
Metcalf and Singh.

Scaling Up Mischief: Red-Teaming AI and Distributing Governance.

_Harvard Data Science Review_, 2024.

URL [https://hdsr.mitpress.mit.edu/pub/ded4vcwl/release/2](https://hdsr.mitpress.mit.edu/pub/ded4vcwl/release/2 "").

- Meyer \[2025\]↑
C. Meyer.

The Tenth Man Rule: How to Take Devil’s Advocacy to a New Level.

[https://themindcollection.com/the-tenth-man-rule-devils-advocacy/](https://themindcollection.com/the-tenth-man-rule-devils-advocacy/ ""), 2025.

- Microsoft Security Team \[2025\]↑
Microsoft Security Team.

3 takeaways from red teaming 100 generative AI products.

[https://www.microsoft.com/en-us/security/blog/2025/01/13/3-takeaways-from-red-teaming-100-generative-ai-products](https://www.microsoft.com/en-us/security/blog/2025/01/13/3-takeaways-from-red-teaming-100-generative-ai-products ""), 2025.

Microsoft Security Blog.

- Miehling et al. \[2025\]↑
E. Miehling et al.

Agentic AI Needs a Systems Theory, 2025.

URL [https://arxiv.org/abs/2503.00237](https://arxiv.org/abs/2503.00237 "").

- MITRE \[2023\]↑
MITRE.

MITRE ATT&CK.

[https://attack.mitre.org/](https://attack.mitre.org/ ""), 2023.

- NIST \[2020\]↑
NIST.

Security and Privacy Controls for Information Systems and Organizations.

Technical Report SP 800-53 Rev. 5, National Institute of Standards and Technology, 2020.

- NVIDIA \[2025\]↑
NVIDIA.

Defining LLM Red Teaming.

[https://developer.nvidia.com/blog/defining-llm-red-teaming](https://developer.nvidia.com/blog/defining-llm-red-teaming ""), 2025.

NVIDIA Technical Blog.

- OWASP \[2024\]↑
OWASP.

Multi-Agentic System Threat Modeling Guide v1.0.

Technical report, Open Worldwide Application Security Project, 2024.

- Patwa \[2025\]↑
R. Patwa.

The Expanding Role of Red Teaming in Defending AI Systems.

[https://www.technewsworld.com/story/the-expanding-role-of-red-teaming-in-defending-ai-systems-179669.html](https://www.technewsworld.com/story/the-expanding-role-of-red-teaming-in-defending-ai-systems-179669.html ""), 2025.

- Pruksachatkun et al. \[2023\]↑
Y. Pruksachatkun, Mcateer M., and S. Majumdar.

_Practicing Trustworthy Machine Learning_.

O’Reilly Media, 2023.

ISBN 9781098120276.

- Rawat et al. \[2024\]↑
A. Rawat et al.

Attack Atlas: A Practitioner’s Perspective on Challenges and Pitfalls in Red Teaming GenAI, 2024.

URL [https://arxiv.org/abs/2409.15398](https://arxiv.org/abs/2409.15398 "").

- Red Team Thinking \[2021\]↑
Red Team Thinking.

9/11 Was A Terrible Tragedy: It Was Also The Birth Of Red Teaming.

[https://www.redteamthinking.com/blog/911-was-a-terrible-tragedy-it-was-also-the-birth-of-red-teaming](https://www.redteamthinking.com/blog/911-was-a-terrible-tragedy-it-was-also-the-birth-of-red-teaming ""), 2021.

- Redscan \[2024\]↑
Redscan.

Red Teaming Operations.

[https://www.redscan.com/services/red-team-operations/](https://www.redscan.com/services/red-team-operations/ ""), 2024.

- Romero-Arjona et al. \[2025\]↑
M. Romero-Arjona et al.

Red Teaming Contemporary AI Models: Insights from Spanish and Basque Perspectives, 2025.

URL [https://arxiv.org/abs/2503.10192](https://arxiv.org/abs/2503.10192 "").

- Sapphire \[2024\]↑
Sapphire.

What is Red Teaming Cyber Security? How Does it Work?

[https://www.sapphire.net/blogs-press-releases/red-teaming-cyber-security/](https://www.sapphire.net/blogs-press-releases/red-teaming-cyber-security/ ""), 2024.

- \[42\]↑
R. Schwartz et al.

Reality Check: A New Evaluation Ecosystem Is Necessary to Understand AI’s Real World Effects.

URL [https://arxiv.org/abs/2505.18893](https://arxiv.org/abs/2505.18893 "").

- Sculley et al. \[2015\]↑
D. Sculley et al.

Hidden Technical Debt in Machine Learning Systems.

In _Advances in Neural Information Processing Systems_, volume 28, pages 2503–2511, 2015.

- Senge \[2006\]↑
P.M. Senge.

_The Fifth Discipline: The Art and Practice of the Learning Organization_.

Doubleday/Currency, 2006.

ISBN 978-0385517256.

- Singh et al. \[2025\]↑
R. Singh et al.

Red-Teaming in the Public Interest.

[https://datasociety.net/library/red-teaming-in-the-public-interest](https://datasociety.net/library/red-teaming-in-the-public-interest ""), 2025.

- TechRound \[2023\]↑
TechRound.

The History of Red Team Exercises.

[https://techround.co.uk/guides/history-red-team-exercises/](https://techround.co.uk/guides/history-red-team-exercises/ ""), 2023.

- Titus and Russell \[2023\]↑
A. J. Titus and A. H. Russell.

The Promise and Peril of Artificial Intelligence – Violet Teaming Offers a Balanced Path Forward, 2023.

URL [https://arxiv.org/abs/2308.14253](https://arxiv.org/abs/2308.14253 "").

- Tomkiel \[2024\]↑
J. Tomkiel.

Penetration Testing vs. Red Teaming.

[https://www.schellman.com/blog/cybersecurity/penetration-testing-vs-red-teaming](https://www.schellman.com/blog/cybersecurity/penetration-testing-vs-red-teaming ""), 2024.

- TRADCOC G2 \[2015\]↑
TRADCOC G2.

The Applied Critical Thinking Handbook, version 7.0.

Technical report, US Army Training and Doctrine Command, 2015.

- UK Government \[2021\]↑
UK Government.

Red Teaming Handbook, 3rd Edition.

Technical report, Development, Concepts and Doctrine Centre, 2021.

- Wikipedia \[2025\]↑
Wikipedia.

Red team.

[https://en.wikipedia.org/wiki/Red\_team](https://en.wikipedia.org/wiki/Red_team ""), 2025.

- Yulianto et al. \[2025\]↑
S. Yulianto, B. Soewito, F.L. Gaol, and A. Kurniawan.

Enhancing cybersecurity resilience through advanced red-teaming exercises and MITRE ATT&CK framework integration: A paradigm shift in cybersecurity assessment.

_Cyber Security and Applications_, 3:100077, 2025.

- Zenko \[2015\]↑
M. Zenko.

_Red Team: How to Succeed By Thinking Like the Enemy_.

Basic Books, 2015.

ISBN 9781501274899.


Report IssueReport Issue for Selection

Generated by
[L\\
A\\
T\\
Exml![[LOGO]](<Base64-Image-Removed>)](https://math.nist.gov/~BMiller/LaTeXML/)
