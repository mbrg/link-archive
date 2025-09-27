---
date: '2025-09-27'
description: The paper presents a novel framework for securing Large Language Models
  (LLMs) against emerging threats, emphasizing a proactive, multi-layered defense
  akin to established malware protection systems. Key components include a Threat
  Intelligence Platform for rapid adaptation to novel threats through automated prioritization
  and signature development, a Data Platform for comprehensive data aggregation and
  analysis, and a Release Platform enabling safe and quick deployment of updates.
  This architecture fosters continuous improvement and minimizes operational disruptions
  while enhancing the resilience of LLMs against various cyber threats. The system
  ultimately aims to provide a cohesive, operationally agile security posture critical
  for modern AI applications.
link: https://arxiv.org/html/2509.20639v1
tags:
- Machine Learning Operations
- Large Language Models
- Cybersecurity
- AI Security
- Threat Intelligence
title: A Framework for Rapidly Developing and Deploying Protection Against Large Language
  Model Attacks
---

[License: CC BY 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2509.20639v1 \[cs.CR\] 25 Sep 2025

# A Framework for Rapidly Developing and Deploying Protection Against Large Language Model Attacks

Report issue for preceding element

Adam Swanda, Amy Chang, Alexander Chen, Fraser Burch, Paul Kassianik, and Konstantin Berlin
All authors are with Cisco. Email: {aswanda, changamy, alexc92, burchy, paulkass, berlink}@cisco.com.

Report issue for preceding element

###### Abstract

Report issue for preceding element

The widespread adoption of Large Language Models (LLMs) has revolutionized AI deployment, enabling autonomous and semi-autonomous applications across industries through intuitive language interfaces and continuous improvements in model development.
However, the attendant increase in autonomy and expansion of access permissions among AI applications also make these systems compelling targets for malicious attacks.
Their inherent susceptibility to security flaws necessitates robust defenses, yet no known approaches can prevent zero-day or novel attacks against LLMs. This places AI protection systems in a category similar to established malware protection systems: rather than providing guaranteed immunity, they minimize risk through enhanced observability, multi-layered defense, and rapid threat response, supported by a threat intelligence function designed specifically for AI-related threats.

Report issue for preceding element

Prior work on LLM protection has largely evaluated individual detection models rather than end-to-end systems designed for continuous, rapid adaptation to a changing threat landscape.
To address this gap, we present a production-grade defense system rooted in established malware detection and threat intelligence practices.
Our platform integrates three components: a threat intelligence system that turns emerging threats into protections; a data platform that aggregates and enriches information while providing observability, monitoring, and ML operations; and a release platform enabling safe, rapid detection updates without disrupting customer workflows.
Together, these components deliver layered protection against evolving LLM threats while generating training data for continuous model improvement and deploying updates without interrupting production.
We share these design patterns and practices to surface the often under-documented, practical aspects of LLM security and accelerate progress on operations-focused tooling.

Report issue for preceding element

## I Introduction

Report issue for preceding element

Building resilient and adaptive security detection platforms for AI is distinct from traditional detection platforms primarily due to the adaptive nature of attacks and the nondeterministic nature of generative AI applications.
Security detection systems are locked in a continuous cybersecurity OODA loop (observe, orient, decide, act) \[ [1](https://arxiv.org/html/2509.20639v1#bib.bib1 "")\] with their attackers.
The constant engagement means the focus of a detection platform should shift from expending significant one-off effort to achieve the ”best” detection model at a particular point in time, and instead focus on rapid adaptation and response.
As soon as a new detection engine is released, its owner must quickly address any new bypasses that are discovered.

Report issue for preceding element

Defensive strategies for LLM deployments have consisted of a mix of technical controls and operational best practices \[ [2](https://arxiv.org/html/2509.20639v1#bib.bib2 "")\] that span a range of effectiveness and cost-efficiency.
We use “guardrails” to refer to the deployed detection and blocking layer that mediates model inputs/outputs and enforces safety and security policies.
Examples include input and output sanitization (e.g., guardrails that filter out malicious prompts and dangerous commands) \[ [3](https://arxiv.org/html/2509.20639v1#bib.bib3 ""), [4](https://arxiv.org/html/2509.20639v1#bib.bib4 "")\], continuous monitoring and logging to detect anomalies and signs of attack \[ [5](https://arxiv.org/html/2509.20639v1#bib.bib5 "")\], red teaming and stress testing to discover vulnerabilities and observe model behavior \[ [6](https://arxiv.org/html/2509.20639v1#bib.bib6 "")\], and adversarial training to build out inherent defenses against unauthorized manipulation \[ [7](https://arxiv.org/html/2509.20639v1#bib.bib7 "")\].

Report issue for preceding element

LLMs can process vast, unstructured datasets from diverse sources to identify anomalies and patterns.
Machine learning-based detection models tend to generalize better than signatures for detections and form the basis of most modern security detection products.
They are especially important for protecting LLMs from prompt injection attacks \[ [8](https://arxiv.org/html/2509.20639v1#bib.bib8 "")\]—when an adversary prompts a model to override the developers’ guardrails and executes a malicious instruction.
Here, semantic understanding of language is critical and pattern-matching approaches alone are not able to fully capture all the nuanced syntactical variations \[ [9](https://arxiv.org/html/2509.20639v1#bib.bib9 "")\].

Report issue for preceding element

However, models often generalize poorly to out-of-distribution (OOD) inputs, including novel attack patterns or techniques against LLMs \[ [10](https://arxiv.org/html/2509.20639v1#bib.bib10 "")\]\[ [11](https://arxiv.org/html/2509.20639v1#bib.bib11 "")\].
As a result, attacks not present in the training distribution (e.g., zero-days) are frequently misclassified.
Even when ML models do generalize, their detection accuracy is hampered by operational requirements to deploy these models at very low false positive rates, and further complicated by the low base rate of attacks within legitimate network traffic and user activity \[ [12](https://arxiv.org/html/2509.20639v1#bib.bib12 "")\].
To our knowledge, all current detection systems can be bypassed under some conditions, and there is no known method to prevent adversarial attacks on ML models with 100% certainty \[ [11](https://arxiv.org/html/2509.20639v1#bib.bib11 ""), [13](https://arxiv.org/html/2509.20639v1#bib.bib13 "")\].

Report issue for preceding element

Furthermore, it is hard to guarantee ML model consistency across multiple retraining cycles \[ [14](https://arxiv.org/html/2509.20639v1#bib.bib14 "")\].
A new model deployment could introduce unexpected changes in behavior, such as blocking a previously unflagged input and disrupting customer workflows.
Therefore, safely releasing an ML model requires careful observation and gradual customer rollout to gather a statistically significant amount of observations.
This validation process can conflict with standard engineering release cycles, which require a much faster quality assurance process.

Report issue for preceding element

Given these realities, the only practical solution is ensuring rapid response and timely protection against novel threats through continuous detection updates.
This operational tempo allows security teams to block attacks before they become commoditized and have the potential to compromise a large fraction of users and customers.
A robust platform must be able to rapidly identify new threats, deploy initial basic protections against them, while also enabling longer-term training data for more robust ML detection models.

Report issue for preceding element

To address these challenges, we have developed and operationalized a dedicated threat intelligence function that considers expanded attack surfaces and deepening integrations of generative AI and agentic AI tools in software systems and technology.
We have also developed a novel platform architecture that advances the state-of-the-art in LLM security operations through systematic integration of threat intelligence, data-driven decision making, and safe deployment methodologies.
A critical differentiator of our platform is its ability to systematically improve detection capabilities through operational feedback loops that transform real-world threats into enhanced security postures.
Our key research contributions include:

Report issue for preceding element

- •


A systematic threat intelligence operations capability that introduces automated prioritization algorithms and novel attack-to-signature translation mechanisms for rapid zero-day protection.

Report issue for preceding element

- •


A unified data correlation framework that enables complex multi-source big data analysis and complex release gating criteria to prevent deployment-induced false positives.

Report issue for preceding element

- •


An immutable multi-version deployment architecture that allows continuous validation through shadow testing while maintaining production stability through deterministic rollback capabilities.

Report issue for preceding element


Unlike static detection systems that degrade over time as attackers develop new techniques, our architecture creates a self-reinforcing improvement cycle where each threat interaction contributes to stronger future defenses.

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2509.20639v1/Rapid_Response_Design.png)Figure 1: Rapid response system architecture showing the end-to-end flow from threat intelligence ingestion to production deployment. Raw intelligence feeds the Threat Intelligence Platform, which generates detection signatures and training and validation data in the Data Platform, culminating in safe deployment through the Release Platform.Report issue for preceding element

## II Threat Intelligence Operations

Report issue for preceding element

Our threat intelligence operations capability serves as the first line of defense in our rapid response system, continuously monitoring the internet for LLM threats.
This system transforms raw intelligence on attacks and vulnerabilities into actionable protections through a pipeline that emphasizes automation, prioritization, and rapid signature deployment.
Given that it is not possible to predict which attacks will appear in the wild, we leverage a prioritization methodology to focus our efforts on attacks that are more likely to be observed.
The platform prioritizes threats based on implementation feasibility, attack practicality, and similarity to known attacks, while providing actionable outputs in the form of detection signatures and data generation modules.

Report issue for preceding element

We refer to this operational capability and its supporting tools as IntelOps.

Report issue for preceding element

### II-A Architecture Overview

Report issue for preceding element

The Threat Intelligence Platform consists of five primary components that operate in a continuous cycle:

Report issue for preceding element

1. 1.


Automated Collection and Monitoring: Continuous ingestion of threat data from multiple open-source intelligence (OSINT) and closed sources.

Report issue for preceding element

2. 2.


Prioritization and Analysis: Scoring and classification of threats into an analyst queue.

Report issue for preceding element

3. 3.


Analysis and Reporting: Automated initial triage and reporting with human review.

Report issue for preceding element

4. 4.


Detection and Data Generation: Development of detection signatures (e.g., YARA rules, which can detect patterns based on textual characteristics) for immediate defense and attack implementations for ML model training.

Report issue for preceding element

5. 5.


Feedback: Routine review of detection hits and misses in Data Platform telemetry.

Report issue for preceding element


Central to our Threat Intelligence Platform is a comprehensive and dynamically updated taxonomy \[ [15](https://arxiv.org/html/2509.20639v1#bib.bib15 "")\] that unifies existing AI security frameworks while addressing the unique operational needs of production LLM security.
We developed this taxonomy through a systematic review of established security standards, including the OWASP LLM Top 10 \[ [2](https://arxiv.org/html/2509.20639v1#bib.bib2 "")\], MITRE ATLAS \[ [16](https://arxiv.org/html/2509.20639v1#bib.bib16 "")\], and National Institute of Standards and Technology (NIST)’s Adversarial Machine Learning Taxonomy \[ [17](https://arxiv.org/html/2509.20639v1#bib.bib17 "")\].
Unlike existing taxonomies that focus primarily on security or safety concerns, our framework bridges both domains, recognizing that production systems must defend against both malicious attacks and harmful outputs.
Each threat category includes detailed subcategories with explicit mappings to both OWASP and MITRE classifications, ensuring compatibility with existing security workflows while providing the granularity needed for detection purposes.
This granularity is maintained through an agile update mechanism that incorporates insights from emerging threats and incident analysis, allowing us to quickly integrate new edge cases and novel attack techniques.
This taxonomy serves as the basis for our Priority Intelligence Requirements (PIRs), which form a prioritized matrix of variables that guide our intelligence collection efforts \[ [18](https://arxiv.org/html/2509.20639v1#bib.bib18 "")\].

Report issue for preceding element

The PIRs are structured around two key characteristics:

Report issue for preceding element

- •


Model- or application-specific vulnerabilities: Threats targeting particular LLM architectures or implementations;

Report issue for preceding element

- •


Tactics, Techniques, and Procedures (TTPs): Attack patterns and methodologies employed against LLMs.

Report issue for preceding element


Each PIR is assigned a priority score, correlating with its likelihood as a target (for example, a frontier LLM is more likely to be targeted due to a higher potential payload of successful compromise, thus a higher priority) or likelihood and potential impact of a TTP (for example, indirect prompt injection is high priority due to its frequency of use in the real world, and its potential impact if successfully deployed against a target).
Given the ever-evolving threat landscape around AI security, these priorities are reviewed and updated regularly to ensure alignment with emerging threats and customer needs.
Time-bound PIRs can also be added for temporary tracking and prioritization (e.g., 30-, 60-, or 90-day) windows for a particular threat or specialized datasets.

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2509.20639v1/IntelOps_Overview.png)Figure 2: Threat Intelligence Platform architecture showing automated collection from multiple sources (OSINT, academic research, internal findings), followed by prioritization scoring, human analyst review, and conversion to actionable protections through signature development and attack dataset generation.Report issue for preceding element

### II-B Automated Collection Pipeline

Report issue for preceding element

The collection infrastructure conducts a nightly automated process that aggregates threat intelligence from multiple sources over the past 24 hours and includes (but is not limited to):

Report issue for preceding element

- •


Academic Research: arXiv papers in relevant categories (cs.AI, cs.CR, cs.CL);

Report issue for preceding element

- •


Security Feeds: security research blogs, vulnerability databases, and threat intelligence vendors.

Report issue for preceding element


In addition to automated collections, raw intelligence can also come from:

Report issue for preceding element

- •


Ad hoc ingestion: Individual sources and reporting added by a human analyst;

Report issue for preceding element

- •


Internal Research: Novel research performed by internal company teams.

Report issue for preceding element


The system employs deduplication mechanisms to prevent redundant processing, and we extract and summarize the text with Jina Reader \[ [19](https://arxiv.org/html/2509.20639v1#bib.bib19 "")\], ensuring consistent and complete content retrieval.

Report issue for preceding element

### II-C Filtering and Scoring

Report issue for preceding element

Upon collection, each source undergoes automated analysis against our PIRs.
Sources scoring above our defined thresholds are automatically flagged for human analyst review, while lower-scoring items are archived for potential future reference, allowing analysts to concentrate efforts on highest priority concerns first.
All LLM-generated artifacts, whether a label or a full report, can be manually edited or corrected by a human analyst via a web application, ensuring human-in-the-loop quality checks.

Report issue for preceding element

As intelligence comes in, our scoring algorithm quantifies the risk or severity of a potential threat or vulnerability:

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | P=Tavg+0.5​Mavg+S+0.5​E3P=\\frac{T\_{\\mathrm{avg}}+0.5\\,M\_{\\mathrm{avg}}+S+0.5\\,E}{3} |  | (1) |

where:

Report issue for preceding element

- •


TavgT\_{\\mathrm{avg}}: Average priority scores of affected models and TTPs; if a model or TTP is not on the prioritized list, default to the lowest score.

Report issue for preceding element

- •


MavgM\_{\\mathrm{avg}}: Average priority score of affected models and/or applications.

Report issue for preceding element

- •


SS: Source credibility assesses the reputation of the source of intelligence (i.e., where the vulnerability or threat was discovered), from lowest to highest.
A lower score means that it is less credible (e.g., arXiv has a lower score because the publications are not peer-reviewed and sometimes theoretical).

Report issue for preceding element

- •


EE: Ease of implementation factors, calculated as the combination of susceptibility to an attack, whether signature-based detection opportunities are present, and whether datasets or data generation code is available for reference or for model training.

Report issue for preceding element


Susceptibility scores capture both a model’s vulnerability to attack and the likelihood of exploitation. The scores range from Unlikely to Use/Difficult to Exploit to Highly Likely to Use/Trivial to Exploit, with intermediate values representing varying degrees of risk and implementation difficulty. This measure incorporates both technical feasibility and threat actor motivation. For example, if an attack simply requires a prompt template, the technical feasibility would be high, whereas an attack requiring fine-tuning a helpful attacker model and/or access to a large amount of compute may be a barrier to entry for less skilled or well-resourced threat actors.

Report issue for preceding element

The algorithm weighs TTPs (TT) as the primary factor (full weight, coefficient of 1), while models (MM) and ease of implementation (EE) receive half weight (coefficient of 0.5), reflecting that the specific attack techniques are generally more indicative of immediate threat relevance than the targets or implementation difficulty alone.
The final score is normalized by dividing by 3, resulting in a score range of 0 to 5.
The resulting PIR score is then used to prioritize remediation efforts, allocate resources, and inform decision-making regarding the identified threat.

Report issue for preceding element

### II-D Threat Analysis and Report Generation

Report issue for preceding element

Prioritized reports are added to an analyst queue.
When an analyst is ready to review a particular report, they can utilize an LLM-assisted initial triage and report generation feature which also creates any relevant tasks in an integrated ticketing system.

Report issue for preceding element

The LLM reads the previously extracted source text and generates a comprehensive initial report that includes the following elements:

Report issue for preceding element

- •


Threat summary: High-level summary with key takeaways of the vulnerability or attack technique;

Report issue for preceding element

- •


Technical details: Detailed explanation of the implementation mechanics;

Report issue for preceding element

- •


Potential impact: Assessment of risk to production LLM deployments, including affected models and reported Attack Success Rates (ASR) of that particular attack technique;

Report issue for preceding element

- •


Example of attack: If relevant, step-by-step instructions on implementing the attack and what the resulting attack prompt looks like;

Report issue for preceding element

- •


Ease of implementation: Details on what skills and resources are needed;

Report issue for preceding element

- •


Detection and mitigation measures: Initial suggestions for detection strategies and mitigation measures, including whether or not a detection signature (such as YARA) is appropriate.

Report issue for preceding element


Despite careful prompting for the automated initial triage component, human expertise and judgment remain crucial.
Security analysts review and improve on the automated reports by:

Report issue for preceding element

- •


Validating the technical accuracy and completeness of initial reporting against the original source;

Report issue for preceding element

- •


Refining signatures for optimal detection coverage;

Report issue for preceding element

- •


Identifying edge cases and potential false positive scenarios;

Report issue for preceding element

- •


Assessing operational impact on customer workflows;

Report issue for preceding element

- •


Comparing attacks/vulnerabilities to any previously analyzed reports where existing detection coverage may be sufficient.

Report issue for preceding element


The Threat Intelligence Platform automatically publishes the generated reports to our internal “IntelHub” knowledge base for human review and finalization, creating a searchable repository of threat intelligence accessible to security, engineering, and product teams.

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2509.20639v1/image.png)Figure 3: Screenshot of IntelOps queue front-end that includes date of ingestion, title of source, affected models, TTPs, attack success rates, and analyst triage status, with additional filtering capabilitiesReport issue for preceding element

### II-E Rapid Signature Development

Report issue for preceding element

One of the key components of our IntelOps process is the emphasis on rapid signature deployment as an immediate mitigation strategy.
While ML models provide superior generalization to protect against AI attacks, they require extensive retraining cycles that can be both time and resource intensive.
YARA, a tool originally designed to help identify and classify malware samples, can be utilized to provide immediate protection against newly discovered threats without having to retrain an ML model.
YARA rules also lend themselves well to certain types of prompt attacks (e.g., template-based, specific attack patterns) as they can combine textual, hexadecimal, and regular expression patterns with boolean conditional matching.

Report issue for preceding element

The signature development process is as follows:

Report issue for preceding element

1. 1.


Pattern identification: Automated identification of unique attack patterns that could be well-suited for YARA

Report issue for preceding element

2. 2.


Signature generation: Human development of YARA rules that capture the essential characteristics of the attack with enough granularity as to minimize false positives

Report issue for preceding element

3. 3.


Validation testing: Signatures are tested against:

Report issue for preceding element

1. (a)


Our Data Platform’s prompt corpus to ensure they do not inadvertently block legitimate use cases; and

Report issue for preceding element

2. (b)


Internal signature metadata and formatting requirements.

Report issue for preceding element


4. 4.


Deployment readiness: Validated signatures are packaged for immediate deployment through our release system and separately uploaded to the Data Platform for further use.

Report issue for preceding element


See more information about safe signature deployment strategy in Section [IV-A](https://arxiv.org/html/2509.20639v1#S4.SS1 "IV-A Signature Updates ‣ IV Release Platform ‣ A Framework for Rapidly Developing and Deploying Protection Against Large Language Model Attacks").

Report issue for preceding element

### II-F Attack Data Generation

Report issue for preceding element

While YARA signatures provide immediate protection against newly discovered threats, comprehensive defense requires training ML models on diverse attack data.
Our Threat Intelligence Platform employs a Python-based automated attack data generation framework that systematically transforms theoretical vulnerabilities into practical training datasets.
While this paper only discusses data generation for defensive model training purposes at a high-level, the same framework is also used to support our team’s LLM red teaming and research projects.

Report issue for preceding element

The data generation system operates on a simple principle: process input datasets containing harmful intents and apply various attack techniques to produce adversarial prompts and conversations.
This approach enables scaling of training data while ensuring coverage of emerging attack patterns identified through our threat intelligence collection, and significantly reduces the time between threat identification and ML model updates.
Rather than waiting to collect sufficient in-the-wild attack samples, we can proactively generate training data for newly discovered techniques while maintaining the authenticity needed for robust model training.

Report issue for preceding element

Key capabilities include:

Report issue for preceding element

- •


Technique application: Automated application of attack techniques such as jailbreaks, prompt injections, obfuscation, and multi-turn strategies to base intents;

Report issue for preceding element

- •


Multi-turn generation: Creation of conversational attacks that attempt to achieve malicious goals through seemingly benign dialogue progression;

Report issue for preceding element

- •


Parallel processing: Multi-worker architecture with checkpointing to handle large-scale dataset generation efficiently;

Report issue for preceding element

- •


Metadata preservation: Comprehensive metadata including technique used, harm category, and generation parameters for each generated attack.

Report issue for preceding element


When analysts identify new attack patterns through the threat intelligence pipeline, these techniques are quickly integrated into the generation framework as plugins.
This ensures that our ML models receive training data that reflect the latest threat landscape.

Report issue for preceding element

### II-G Human Labeling and Feedback

Report issue for preceding element

Finally, human expertise remains essential in our process, serving as both a quality control mechanism and a source of ground truth for our automated systems.
While automated labeling improves the scalability of this capability, human labeling ensures accuracy, catches edge cases, and identifies systematic issues that might otherwise go unnoticed in purely automated pipelines.
Human labeling serves as a critical checkpoint for monitoring the performance of our automated labeling algorithms.
By maintaining a continuous human review process, we can:

Report issue for preceding element

- •


Detect label drift: Identify when automated labeling begins to diverge from human consensus, indicating potential model degradation or shifts in attack patterns

Report issue for preceding element

- •


Diagnose false positives: Determine whether detection errors stem from model generalization failures or misaligned consensus labeling criteria

Report issue for preceding element

- •


Calibrate consensus algorithms: Adjust automated labeling instructions based on patterns identified by human review

Report issue for preceding element

- •


Refine our threat taxonomy: Human analysts regularly encounter edge cases that challenge existing categorizations, providing insights that sharpen distinctions between similar attack categories, identify emerging attack patterns that do not fit existing classifications, or reveal common misunderstandings that customers may also experience

Report issue for preceding element


This intelligence platform establishes a dynamic and adaptive framework for understanding, anticipating, and mitigating threats against AI models and systems.
Its iterative nature and emphasis on both automation and human expertise are critical for maintaining a resilient defense against novel threats and attack techniques.

Report issue for preceding element

## III Data Platform

Report issue for preceding element

The goal of the Data Platform is to provide a single location for all data storage, aggregation, enrichment, labeling, and decision making.
Information from multiple sources is systematically aggregated and correlated, ensuring comprehensive artifact analysis through consolidated data representation.
This architectural approach enables cross-source information utilization for enhanced decision-making processes, including detection model evaluation, resource prioritization, and automated enrichment workflows.

Report issue for preceding element

The Data Platform leverages the distributed data warehouse Snowflake, which prioritizes adaptability over traditional processing paradigms, as shown in Fig. [4](https://arxiv.org/html/2509.20639v1#S3.F4 "Figure 4 ‣ III Data Platform ‣ A Framework for Rapidly Developing and Deploying Protection Against Large Language Model Attacks").
A key architectural decision was choosing between traditional ETL pipelines and our novel warehouse-centric approach.
Rather than implementing conventional ETL pipelines with rigid schemas and predetermined processing sequences, which can create brittleness when adapting to new threat types, our design emphasizes flexible data transformation capabilities that can rapidly adapt to evolving requirements.
This approach supports dynamic threat response through accelerated operational cycles while maintaining system stability.

Report issue for preceding element

Once the initial raw data is ingested, core processing occurs within the warehouse environment using standard query languages that are extended via user-defined functions (UDFs), or UDFs that call out to external services.
This enables augmentation of native capabilities for any functionality that is not directly available in SQL (e.g., calling out AI services or applying customer Python code).

Report issue for preceding element

The unified data storage model enables logical pipeline definitions that eliminate physical structure dependencies when aggregation or data collection methods evolve.
Unlike traditional approaches that involve explicit pre-ingestion processing or external data augmentation, our design allows for rapid adjustments.
With all primitives defined in SQL, we can quickly mix and match them to modify the pipeline without having to adjust or redeploy any additional infrastructure.

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2509.20639v1/pipeline.png)(a)Data pipeline architecture for LLM prompt processing, showing iterative enrichment workflow from raw data ingestion through correlation and labeling resulting in a unified table, enabling flexible business logic implementation through SQL views.Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2509.20639v1/snowflake.png)(b)Snowflake-based Data Platform architecture illustrating SQL-centric processing augmented with Python UDFs and external service calls, providing extensible primitives for flexible data pipeline operations and cross-source correlation.Report issue for preceding element

Figure 4: Data PlatformReport issue for preceding element

Our Data Platform regularly aggregates and correlates the following resources:

Report issue for preceding element

- •


Customer telemetry, including the guardrail response and the customer prompt (when allowed);

Report issue for preceding element

- •


All known publicly available datasets on the internet that are deemed relevant (e.g., open-source datasets in Hugging Face and GitHub);

Report issue for preceding element

- •


Internally generated human labels;

Report issue for preceding element

- •


Model-generated labels;

Report issue for preceding element

- •


Prompt translations into various languages;

Report issue for preceding element

- •


Internally generated data, such as data produced by the threat intelligence pipeline described in the previous section; and

Report issue for preceding element

- •


Detailed responses from current and upcoming versions of the guardrails, including ML scores and signature matches.

Report issue for preceding element


Customer telemetry is processed according to customer data handling policies; we anonymize and minimize PII where applicable.

Report issue for preceding element

Beyond standard data aggregation and correlation, our Data Platform handles two critical tasks.
First, it identifies any additional data needed, prioritizing outstanding computation tasks in a queue, and then collects the required information as a background task.
Second, it computes the golden labels for a given artifact based on all the available information.

Report issue for preceding element

### III-A Prioritization Tasks

Report issue for preceding element

The prioritization framework operates through a two-phase approach: first, defining the prioritization queue, and batch processing execution.
The queue uses dynamic data integration that combines processed knowledge with current operational data through database views.
Selected workloads are then processed in batches with results systematically recorded through standard database operations.

Report issue for preceding element

Our pipeline runs prioritization tasks on all known prompts in our database, which include:

Report issue for preceding element

- •


Multi-language processing capabilities for enhanced detection coverage;

Report issue for preceding element

- •


Automated labeling workflows for training data quality improvement;

Report issue for preceding element

- •


Language classification modules for content categorization and processing optimization;

Report issue for preceding element

- •


Performance evaluation against current and upcoming guardrails for offline performance evaluation and release gating;

Report issue for preceding element

- •


Scoring prompts against third-party guardrails for performance monitoring and labeling improvements; and

Report issue for preceding element

- •


Scanning all prompts against our signatures, used for monitoring and identifying issues or gaps.

Report issue for preceding element


These processes continue until all data is computed and the prioritization updates automatically as new data propagates into the knowledge table.
Importantly, with all data available for each prompt in the knowledge table, we can make complicated and rapidly changing prioritization decisions despite information being aggregated across multiple sources.

Report issue for preceding element

The knowledge table is a unified view keyed by prompt ID that aggregates labels, model scores, signature matches, metadata, and provenance for decision-making.

Report issue for preceding element

### III-B Labeling

Report issue for preceding element

Labeling is the most important output produced by our data pipeline, as it is the most impactful lever that one can leverage to increase ML detection accuracy, to validate that upcoming releases are safe to deploy, and to quickly identify detection issues in production.
However, labeling faces two major challenges.
First, benign data labeling must be extremely accurate.
Any deployed detection system requires a very low false positive rate; having a labeling error higher than the desired false positive rate would be unworkable.
Second, we must be able to identify attacks, especially novel ones.
Relying on a single labeling tool would limit our detection system’s value, offering no improvement beyond that tool’s inherent capabilities.

Report issue for preceding element

Given the volume of data flowing through our platform, strategic prioritization that highlights human labeling efforts is essential.
Our Data Platform automatically prioritizes samples for human review, such as detections from actual customer telemetry or samples with low or borderline confidence scores.
We sample detections and near-misses for review proportional to their risk, novelty, and potential customer impact.
Effective labeling demands both a wide breadth of data to label and an acceptance of its inherently iterative nature.
Our infrastructure achieves these two conditions by aggregating information from multiple instructed LLMs, human labeling efforts, signature detections, and original source labels.

Report issue for preceding element

## IV Release Platform

Report issue for preceding element

One of the largest challenges in deploying a detection and blocking system like our guardrails is updating its detection components post-release.
The primary risk lies in unforeseen shifts in the detection distribution, which could potentially disrupt established customer workflows.
We have seen countless examples of security vendors accidentally generating catastrophic levels of false positives that ultimately break critical customer infrastructure \[ [20](https://arxiv.org/html/2509.20639v1#bib.bib20 ""), [21](https://arxiv.org/html/2509.20639v1#bib.bib21 ""), [22](https://arxiv.org/html/2509.20639v1#bib.bib22 "")\].
Our Data Platform is designed to minimize the chance of such an event, relying on three major components that need updating.
First are signatures, which we can release rapidly to remediate any ongoing issues or concerns.
Second are ML detection models; these take longer to update and require additional validation due to their potential to cause unexpected shifts in the detection distribution.
Third, the orchestration logic that integrates the previous components into the final detection (Fig. [5](https://arxiv.org/html/2509.20639v1#S4.F5 "Figure 5 ‣ IV Release Platform ‣ A Framework for Rapidly Developing and Deploying Protection Against Large Language Model Attacks")).

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2509.20639v1/production.png)Figure 5: Release Platform architecture demonstrating immutable component deployment with concurrent versioning. The central orchestrator routes customer requests to appropriate guardrail versions, enabling seamless shadow deployments, gradual rollouts, and instant rollbacks while guaranteeing that already deployed guardrails cannot be accidentally disrupted during updates.Report issue for preceding element

The platform architecture supports simultaneous deployment of multiple versions of guardrails within the same deployment.
Each detection implementation and its associated components are entirely immutable, ensuring that no updates can disrupt existing detection behavior.
While there are no restrictions on the number of guardrail versions that can be deployed concurrently, it is typical to maintain both production and shadow deployments at all times.

Report issue for preceding element

Instead of updating existing guardrails, a new version is released alongside the previous one, rather than replacing them directly.
This approach enables gradual customer transition and simplified rollback procedures without the complexities of a conventional release cycle.
The deterministic relationship between inputs and outputs across components aids in reproducible results and enables efficient caching strategies for optimized performance.

Report issue for preceding element

This design enables updates to be pushed directly to production because they cannot impact existing production systems.
We thus unblock the engineering release process, enabling hot patches and other engineering updates to be released into production without being blocked by the lengthy, expensive, and extensive detection QA release processes described above.
The ML team can safely and thoroughly check for detection regressions across multiple version releases without interruption, even though the engineering version is being updated in the preview, staging, and production environments constantly.
Below, we detail how this architecture is used to safely update our detection.

Report issue for preceding element

### IV-A Signature Updates

Report issue for preceding element

Signatures, in this case expressed as YARA rules, are developed through the intelligence processes detailed earlier and serve as rapid response tools for critical detection issues that require immediate resolution or provide interim protection against emerging threats while ML models undergo retraining and redeployment cycles.
Our goal is a swift release of updates, starting from signature creation to deployment to an initial set of customers.

Report issue for preceding element

These signatures function as a first line of defense, remediating emerging threats or resolving impactful false positives and false negatives.
While not designed for the broad generalization capabilities of machine learning approaches, they deliver critical remediation during the ML model update cycle.
The primary advantage of rule-based detection lies in its predictable impact on overall detection distributions, allowing for more confident deployment compared to probabilistic ML detection approaches.

Report issue for preceding element

This rule-based approach provides deterministic behavior that complements machine learning detection capabilities, offering rapid response mechanisms for time-sensitive security updates while maintaining system reliability and customer confidence.
We validate new signatures to ensure they:

Report issue for preceding element

- •


Accurately identify expected malicious patterns with precision;

Report issue for preceding element

- •


Minimize false positive rates on legitimate use cases;

Report issue for preceding element

- •


Comply with internal standards for metadata and formatting requirements; and

Report issue for preceding element

- •


Operate within established performance and resource utilization thresholds.

Report issue for preceding element


The signature release process is designed to balance speed with safety through a structured multi-environment deployment pipeline.
The release workflow progresses through three distinct environments:

Report issue for preceding element

1. 1.


Internal Snowflake Environment: An initial PR request.
The updated signature is scanned against all prompts in the data platform and an automated report is generated.
The deltas between the previous signature package and the new package are inspected to ensure no unexpected outcomes are observed.

Report issue for preceding element

2. 2.


Preview/Staging Environment: Initial deployment for functional validation.
A large prompt corpus is re-scanned with the full guardrails, which now include the new signatures.
Since the individual detection components making up the guardrails are immutable, the ML scores are pulled from cache rather than recomputed, thus the process is fairly fast and low cost.

Report issue for preceding element

3. 3.


Production Environment: Gradual roll-out to customer deployments.
The process can be further augmented with an optional shadow deployment if additional checks are required.

Report issue for preceding element


Each environment transition requires specific validation criteria to be met, ensuring that signature updates maintain detection quality while avoiding disruption to legitimate use cases.
Signature updates are managed through a version control system where each release is tagged with a unique identifier, and multiple previous versions are also available in all environments.
This approach provides a complete audit trail of all signature changes, instant reversion to previous versions if issues arise, and enables multiple signature versions to coexist during transition periods.

Report issue for preceding element

Post-deployment monitoring through our data platform provides feedback on signature effectiveness, including detection rates and false positive metrics that are tracked in real-time, as well as customer impact assessment through telemetry analysis.
Post-deployment reviews allow us to further refine signatures and ML model training priorities.

Report issue for preceding element

### IV-B Model and Logic Updates

Report issue for preceding element

Updating ML detection models and associated orchestration logic represents a higher-risk operation due to the potential for unexpected detection behavior changes that could disrupt established customer workflows.
Risk mitigation involves implementing a multi-stage release process that extends over several days to weeks, enabling validation at each phase.

Report issue for preceding element

Our staged process, described below, ensures detection quality while minimizing operational disruption, providing multiple validation checkpoints and maintaining system reliability throughout the update process:

Report issue for preceding element

1. 1.


New models and guardrail logic are committed to master, creating a new version of guardrails.

Report issue for preceding element

2. 2.


The new guardrail version is deployed into pre-production environments alongside the current version of guardrails.

Report issue for preceding element

3. 3.


The new guardrails are evaluated against a curated and prioritized prompt dataset in the Data Platform.

Report issue for preceding element

4. 4.


Results undergo review by the threat intelligence team and ML owners, focusing on differential analysis between versions.

Report issue for preceding element

5. 5.


Signatures are updated to address systematic false positives or other classification errors identified during evaluation.

Report issue for preceding element

6. 6.


Following issue resolution to acceptable thresholds, the new guardrails are rolled into production in shadow mode.

Report issue for preceding element

7. 7.


Comprehensive performance metrics are analyzed in the Data Platform, examining detection patterns and any increases in flag rate on synthetic or previously captured prompts when actual customer prompts are not available.

Report issue for preceding element

8. 8.


Customers are then gradually migrated to the new guardrail version, maintaining rollback capabilities for rapid issue response.

Report issue for preceding element


Release gating evaluates changes in false positive rate at the operating point, recall, and flag rate deltas, with shadow performance informing promotion decisions.

Report issue for preceding element

## V Previous Work

Report issue for preceding element

As discussed earlier in this paper, significant research has focused on developing detection methods for LLM attacks and protections against them, consisting of technical controls and operational best practices \[ [2](https://arxiv.org/html/2509.20639v1#bib.bib2 ""), [4](https://arxiv.org/html/2509.20639v1#bib.bib4 ""), [5](https://arxiv.org/html/2509.20639v1#bib.bib5 ""), [6](https://arxiv.org/html/2509.20639v1#bib.bib6 ""), [7](https://arxiv.org/html/2509.20639v1#bib.bib7 "")\].
But relatively few works address the operational challenges of deploying these defenses in production environments requiring rapid threat response and continuous adaptation.
We have not found similar examples of a dedicated threat intelligence function designed specifically for AI-related threats that considers the expanded attack surface and the deepening integrations of generative AI and agentic AI tools in software systems and technology.

Report issue for preceding element

Early work in operationalizing LLM security began with the development of Vigil \[ [23](https://arxiv.org/html/2509.20639v1#bib.bib23 "")\] in 2022, which introduced the application of YARA rules to the domain of LLM threat detection.
The open-source project demonstrated that pattern-matching techniques could effectively identify prompt injection attempts and other LLM-specific threats while leveraging existing security tooling rather than requiring specialized development of novel tools.
Our comprehensive defense platform described in this paper significantly extends this foundational approach by integrating rule-based detection into an enterprise-grade threat intelligence pipeline with automated deployment capabilities, enabling organization-scale protection with the ability to rapidly respond to emerging threats.

Report issue for preceding element

Recent advances in prompt injection detection have produced promising approaches, including research that compares the performance of early detection systems for LLM security \[ [24](https://arxiv.org/html/2509.20639v1#bib.bib24 "")\].
Google DeepMind’s CaMeL \[ [25](https://arxiv.org/html/2509.20639v1#bib.bib25 "")\] takes an architectural approach, applying traditional software security principles like control flow integrity to LLM systems.
PromptShield \[ [26](https://arxiv.org/html/2509.20639v1#bib.bib26 "")\] achieves detection with low false positive rates through fine-tuning detectors on both conversational and application-structured data, while Attention Tracker \[ [27](https://arxiv.org/html/2509.20639v1#bib.bib27 "")\] introduces training-free detection by analyzing attention patterns within LLMs. However, Hackett et al. \[ [28](https://arxiv.org/html/2509.20639v1#bib.bib28 "")\] demonstrated that many prominent guardrail systems can be bypassed with up to 100% success rates using character injection techniques, highlighting the limitations of point-in-time detection approaches.
While comprehensive prevention remains an open problem, our platform reduces the window of vulnerability by translating new threats into protections quickly through rapid signature updates and safe staged deployments.

Report issue for preceding element

## VI Conclusion

Report issue for preceding element

This paper presents a comprehensive multi-layered defense strategy for protecting LLMs against evolving AI threats through rapid response mechanisms.
By synthesizing established cybersecurity approaches with novel AI-specific protection strategies, we have created a production-grade system that effectively balances the competing demands of detection speed, accuracy, and operational stability while providing resilient protection against both documented and novel threats.

Report issue for preceding element

Our integrated architecture, comprised of three interdependent platforms, addresses the complete threat response lifecycle:

Report issue for preceding element

1. 1.


The threat intelligence platform provides continuous threat landscape monitoring and rapid protection through automated intelligence collection, threat prioritization, and detection signature development.

Report issue for preceding element

2. 2.


The data platform enables intelligent decision-making through comprehensive data aggregation, intelligence labeling workflows, and prioritization algorithms.

Report issue for preceding element

3. 3.


The release platform ensures safe deployment through immutable version management, progressive rollout mechanisms, and seamless rollback strategies.

Report issue for preceding element


Production deployment across enterprise environments has validated the platform’s effectiveness in protecting AI deployments while preserving the agility required to respond to new attack techniques and methodologies.
The system successfully bridges the gap between immediate tactical response and strategic model improvement initiatives, creating a unified defensive capability that addresses both reactive and proactive AI threats.

Report issue for preceding element

While our platform demonstrates significant advancement in LLM security capabilities, several areas present additional opportunities for continued improvement and research investment.
Future technical development could, for example, improve cross-model generalization to address the growing diversity of LLM architectures.
Threat intelligence processing capacity must also evolve to handle increasingly sophisticated attack patterns without overwhelming threat intelligence and security operations teams.
The development of more sophisticated algorithms and threat classification capabilities will be necessary to adapt to novel attack methodologies.

Report issue for preceding element

As LLMs become increasingly integrated into critical business processes and as agentic AI capabilities increase in scope, the need for robust security platforms will only grow.
LLMs, while transformative, represent new attack surfaces that, if compromised, could lead to significant data breaches, service disruptions, or reputational damage.
While no system can yet guarantee impenetrable protection against all conceivable adversarial inputs, our platform demonstrates that principled engineering combined with rapid response capabilities can help safely speed up the OODA loop, thus enabling us to provide enhanced protection.

Report issue for preceding element

The architectural principles and implementation strategies described in this paper are designed to serve as a foundational blueprint for organizations seeking to establish or enhance their own AI security capabilities.
By sharing our design decisions and operational insights, we hope to advance a collective understanding of protective measures for AI systems in production environments.
The future of AI security lies in adaptive systems that learn, evolve, and improve alongside the threats they defend against.
Our goal is to foster a collaborative environment where best practices can be universally adopted and continuously improved upon.

Report issue for preceding element

## References

Report issue for preceding element

- \[1\]↑
T. Sager, “The cyber ooda loop: How your attacker should help you design your defense,” in _NIST Security Automation Conference Presentation_. National Institute of Standards and Technology (NIST), 2015, presentation from the NIST Security Automation Conference, detailing the application of the OODA loop (Observe, Orient, Decide, Act) to cybersecurity defense strategy. \[Online\]. Available: [https://csrc.nist.gov/CSRC/media/Presentations/The-Cyber-OODA-Loop-How-Your-Attacker-Should-Help/images-media/day3\_security-automation\_930-1020.pdf](https://csrc.nist.gov/CSRC/media/Presentations/The-Cyber-OODA-Loop-How-Your-Attacker-Should-Help/images-media/day3_security-automation_930-1020.pdf "")
- \[2\]↑
OWASP Foundation, “OWASP top 10 for LLM applications 2025,” 2025, version 2025. \[Online\]. Available: [https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/ "")
- \[3\]↑
A. Kumar, C. Agarwal, S. Srinivas, A. J. Li, S. Feizi, and H. Lakkaraju, “Certifying llm safety against adversarial prompting,” 2025. \[Online\]. Available: [https://arxiv.org/abs/2309.02705](https://arxiv.org/abs/2309.02705 "")
- \[4\]↑
F. Jiang, Z. Xu, L. Niu, B. Wang, J. Jia, B. Li, and R. Poovendran, “Identifying and mitigating vulnerabilities in llm-integrated applications,” 2023. \[Online\]. Available: [https://arxiv.org/abs/2311.16153](https://arxiv.org/abs/2311.16153 "")
- \[5\]↑
P. Christiano, “Mechanistic anomaly detection and elk,” [https://www.alignment.org/blog/mechanistic-anomaly-detection-and-elk/](https://www.alignment.org/blog/mechanistic-anomaly-detection-and-elk/ ""), November 2022.

- \[6\]↑
B. Bullwinkel, A. Minnich, S. Chawla, G. Lopez, M. Pouliot, W. Maxwell, J. de Gruyter, K. Pratt, S. Qi, N. Chikanov, R. Lutz, R. S. R. Dheekonda, B.-E. Jagdagdorj, E. Kim, J. Song, K. Hines, D. Jones, G. Severi, R. Lundeen, S. Vaughan, V. Westerhoff, P. Bryan, R. S. S. Kumar, Y. Zunger, C. Kawaguchi, and M. Russinovich, “Lessons from red teaming 100 generative ai products,” 2025. \[Online\]. Available: [https://arxiv.org/abs/2501.07238](https://arxiv.org/abs/2501.07238 "")
- \[7\]↑
N. Jain, A. Schwarzschild, Y. Wen, G. Somepalli, J. Kirchenbauer, P. yeh Chiang, M. Goldblum, A. Saha, J. Geiping, and T. Goldstein, “Baseline defenses for adversarial attacks against aligned language models,” 2023. \[Online\]. Available: [https://arxiv.org/abs/2309.00614](https://arxiv.org/abs/2309.00614 "")
- \[8\]↑
Y. Liu, Y. Jia, R. Geng, J. Jia, and N. Z. Gong, “Formalizing and benchmarking prompt injection attacks and defenses,” 2024. \[Online\]. Available: [https://arxiv.org/abs/2310.12815](https://arxiv.org/abs/2310.12815 "")
- \[9\]↑
K. Greshake, S. Abdelnabi, S. Mishra, C. Endres, T. Holz, and M. Fritz, “Not what you’ve signed up for: Compromising real-world llm-integrated applications with indirect prompt injection,” 2023. \[Online\]. Available: [https://arxiv.org/abs/2302.12173](https://arxiv.org/abs/2302.12173 "")
- \[10\]↑
H. Benoit, L. Jiang, A. Atanov, O. F. Kar, M. Rigotti, and A. Zamir, “Unraveling the key components of ood generalization via diversification,” 2024. \[Online\]. Available: [https://arxiv.org/abs/2312.16313](https://arxiv.org/abs/2312.16313 "")
- \[11\]↑
A. Peng, J. Michael, H. Sleight, E. Perez, and M. Sharma, “Rapid response: Mitigating llm jailbreaks with a few examples,” 2024. \[Online\]. Available: [https://arxiv.org/abs/2411.07494](https://arxiv.org/abs/2411.07494 "")
- \[12\]↑
T. Pietraszek and A. Tanner, “Data mining and machine learning—towards reducing false positives in intrusion detection,” _Information Security Technical Report_, vol. 10, no. 3, pp. 169–183, 2005. \[Online\]. Available: [https://www.sciencedirect.com/science/article/pii/S1363412705000361](https://www.sciencedirect.com/science/article/pii/S1363412705000361 "")
- \[13\]↑
D. R. Insua, R. Naveiro, V. Gallego, and J. Poulos, “Adversarial machine learning: Bayesian perspectives,” _Journal of the American Statistical Association_, vol. 118, no. 543, pp. 2195–2206, 2023. \[Online\]. Available: [https://doi.org/10.1080/01621459.2023.2183129](https://doi.org/10.1080/01621459.2023.2183129 "")
- \[14\]↑
L. Wang, D. Ghosh, M. T. G. Diaz, A. Farahat, M. Alam, C. Gupta, J. Chen, and M. Marathe, “Wisdom of the ensemble: Improving consistency of deep learning models,” 2020. \[Online\]. Available: [https://arxiv.org/abs/2011.06796](https://arxiv.org/abs/2011.06796 "")
- \[15\]↑
Cisco, “Ai safety and security taxonomy,” 2025. \[Online\]. Available: [https://www.cisco.com/site/us/en/learn/topics/artificial-intelligence/ai-safety-security-taxonomy.html](https://www.cisco.com/site/us/en/learn/topics/artificial-intelligence/ai-safety-security-taxonomy.html "")
- \[16\]↑
MITRE, “Mitre atlas.” \[Online\]. Available: [https://atlas.mitre.org/](https://atlas.mitre.org/ "")
- \[17\]↑
A. Vassilev, A. Oprea, A. Fordyce, H. Anderson, X. Davis, and M. Hamin, “Adversarial machine learning - a taxonomy and terminology of attacks and mitigations.”

- \[18\]↑
F. of Incident Response and S. T. (FIRST), “Priority intelligence requirement,” 2025, accessed on July 3, 2025. \[Online\]. Available: [https://www.first.org/global/sigs/cti/curriculum/pir](https://www.first.org/global/sigs/cti/curriculum/pir "")
- \[19\]↑
Jina AI Ltd. Jina ai — convert a url to llm-friendly input. \[Online\]. Available: [https://jina.ai/reader/](https://jina.ai/reader/ "")
- \[20\]↑
CrowdStrike, “Technical details: Falcon content update for windows hosts,” CrowdStrike, Tech. Rep., July 2024. \[Online\]. Available: [https://www.crowdstrike.com/en-us/blog/falcon-update-for-windows-hosts-technical-details/](https://www.crowdstrike.com/en-us/blog/falcon-update-for-windows-hosts-technical-details/ "")
- \[21\]↑
Z. Whittaker, “Sophos antivirus detects own update as false positive malware,” The Register report, September 2012, updater files quarantined, blocking signature downloads. \[Online\]. Available: [https://www.zdnet.com/article/sophos-antivirus-detects-own-update-as-false-positive-malware](https://www.zdnet.com/article/sophos-antivirus-detects-own-update-as-false-positive-malware "")
- \[22\]↑
B. Krebs, “Mcafee false detection locks up windows xp,” _Krebs on Security_, April 2010. \[Online\]. Available: [https://krebsonsecurity.com/2010/04/mcafee-false-detection-locks-up-windows-xp/](https://krebsonsecurity.com/2010/04/mcafee-false-detection-locks-up-windows-xp/ "")
- \[23\]↑
A. Swanda, “Vigil: Detect prompt injections, jailbreaks, and other potentially risky large language model (llm) inputs,” GitHub repository, 2023. \[Online\]. Available: [https://github.com/deadbits/vigil-llm](https://github.com/deadbits/vigil-llm "")
- \[24\]↑
V. Gakh and H. Bahsi, “Enhancing security in llm applications: A performance evaluation of early detection systems,” 2025. \[Online\]. Available: [https://arxiv.org/abs/2506.19109](https://arxiv.org/abs/2506.19109 "")
- \[25\]↑
E. Debenedetti, I. Shumailov, T. Fan, J. Hayes, N. Carlini, D. Fabian, C. Kern, C. Shi, A. Terzis, and F. Tramèr, “Defeating prompt injections by design,” 2025. \[Online\]. Available: [https://arxiv.org/abs/2503.18813](https://arxiv.org/abs/2503.18813 "")
- \[26\]↑
D. Jacob, H. Alzahrani, Z. Hu, B. Alomair, and D. Wagner, “Promptshield: Deployable detection for prompt injection attacks,” 2025. \[Online\]. Available: [https://arxiv.org/abs/2501.15145](https://arxiv.org/abs/2501.15145 "")
- \[27\]↑
K.-H. Hung, C.-Y. Ko, A. Rawat, I.-H. Chung, W. H. Hsu, and P.-Y. Chen, “Attention tracker: Detecting prompt injection attacks in llms,” 2025. \[Online\]. Available: [https://arxiv.org/abs/2411.00348](https://arxiv.org/abs/2411.00348 "")
- \[28\]↑
W. Hackett, L. Birch, S. Trawicki, N. Suri, and P. Garraghan, “Bypassing prompt injection and jailbreak detection in llm guardrails,” 2025. \[Online\]. Available: [https://arxiv.org/abs/2504.11168](https://arxiv.org/abs/2504.11168 "")

Report IssueReport Issue for Selection

Generated by
[L\\
A\\
T\\
Exml![[LOGO]](<Base64-Image-Removed>)](https://math.nist.gov/~BMiller/LaTeXML/)
