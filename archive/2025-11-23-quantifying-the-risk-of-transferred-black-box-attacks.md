---
date: '2025-11-23'
description: This study introduces a framework for resilience testing against transferred
  black-box adversarial attacks on neural networks, addressing the challenges of accurately
  quantifying security risks. Key insights include the inefficiency of exhaustive
  high-dimensional input space exploration and the need for effective surrogate model
  selection based on Centered Kernel Alignment (CKA) similarity. The proposed methodology
  enhances adversarial coverage and employs regression-based estimators for practical
  risk quantification, aligning with increasing regulatory demands for AI security.
  Future work will focus on refining similarity metrics and improving computational
  efficiency to bolster scalable risk assessment in production environments.
link: https://arxiv.org/html/2511.05102v1
tags:
- Neural Networks
- Adversarial Attacks
- Risk Quantification
- Machine Learning Security
- Black Box Attacks
title: Quantifying the Risk of Transferred Black Box Attacks
---

[License: arXiv.org perpetual non-exclusive license](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2511.05102v1 \[cs.CR\] 07 Nov 2025

# Quantifying the Risk of Transferred Black Box Attacks

Report issue for preceding element

Disesdi Susanna Cox
[0009-0003-0568-0236](https://orcid.org/0009-0003-0568-0236 "ORCID identifier")OWASP AI Exchange300 Delaware Ave, Ste 210 #384WilmingtonDEUSA19801[disesdi.susannacox@owasp.org](mailto:disesdi.susannacox@owasp.org) and Niklas Bunzel
[0000-0002-8921-1562](https://orcid.org/0000-0002-8921-1562 "ORCID identifier")Fraunhofer SIT / TU-Darmstadt / ATHENERheinstraße 75DarmstadtHesseGermany64295[niklas.bunzel@sit.fraunhofer.de](mailto:niklas.bunzel@sit.fraunhofer.de)

Report issue for preceding element

###### Abstract.

Report issue for preceding element

Neural networks have become pervasive across various applications, including security-related products. However, their widespread adoption has heightened concerns regarding vulnerability to adversarial attacks. With emerging regulations and standards emphasizing security, organizations must reliably quantify risks associated with these attacks, particularly regarding transferred adversarial attacks, which remain challenging to evaluate accurately.
This paper investigates the complexities involved in resilience testing against transferred adversarial attacks. Our analysis specifically addresses black-box evasion attacks, highlighting transfer-based attacks due to their practical significance and typically high transferability between neural network models. We underline the computational infeasibility of exhaustively exploring high-dimensional input spaces to achieve complete test coverage. As a result, comprehensive adversarial risk mapping is deemed impractical.
To mitigate this limitation, we propose a targeted resilience testing framework that employs surrogate models strategically selected based on Centered Kernel Alignment (CKA) similarity. By leveraging surrogate models exhibiting both high and low CKA similarities relative to the target model, the proposed approach seeks to optimize coverage of adversarial subspaces. Risk estimation is conducted using regression-based estimators, providing organizations with realistic and actionable risk quantification.

Report issue for preceding element

Adversarial Attacks, Black Box Attacks, Risk Quantification

††ccs: Computing methodologies Computer vision††ccs: Computing methodologies Neural networks

## 1\. Introduction

Report issue for preceding element

Neural networks have become widespread in numerous commercial applications, including critical security-related products. Despite their impressive capabilities, neural networks remain highly vulnerable to evasion attacks, wherein attackers subtly manipulate inputs to alter model predictions in their favor.
With increasing recognition of these vulnerabilities, political and legislative frameworks worldwide are rapidly evolving to mandate the secure deployment of AI systems. Prominent among these is the EU AI Act, which represents one of the pioneering comprehensive regulations requiring organizations to ensure AI robustness and security. Concurrently, international standards for AI security are emerging, compelling companies to demonstrate compliance with established security criteria.
In the realm of evasion attacks, current research has proposed various defensive strategies, including adversarial training (pgd\_bib), preprocessing techniques such as denoising (9010982) and JPEG compression (das2017keeping), and detectors based on image statistics (bunzel2024signals) or neuron activations (roth2019odds). However, regulatory compliance now requires organizations not merely to defend but also to quantify and demonstrate the associated adversarial risk explicitly.
As regulatory bodies and other agencies tasked with ensuring AI system security grapple with setting normative standards and regulatory thresholds, successfully integrating risk assessment into AI security workflows is becoming increasingly essential. Organizations require means of quantifying risk and resilience to various AI security vectors for both regulatory compliance, and overall system security.
Recent literature presents several risk estimation methodologies, predominantly relying on red teaming approaches, where trained models are subjected to various optimization-based attacks (croce2020robustbench; Croce020a; guo2024exploringadversarialfrontierquantifying). However, these methodologies exhibit gaps in assessing risks associated with:

Report issue for preceding element

- •


Transferred adversarial attacks, which are particularly effective in real-world scenarios

Report issue for preceding element

- •


Attacks transferred from an extensive range of potential surrogate models

Report issue for preceding element

- •


Simultaneous consideration of multiple attack types

Report issue for preceding element

- •


Performing risk estimations earlier in the model lifecycle e.g. pre-training or during design phase

Report issue for preceding element


Addressing these critical gaps, this paper introduces a comprehensive framework designed explicitly for estimating risks associated with transferred adversarial attacks. A central contribution is our systematic and extensive coverage of surrogate model spaces, ensuring robust risk quantification. This enables organizations to effectively assess adversarial vulnerabilities.

Report issue for preceding element

## 2\. Related Work

Report issue for preceding element

### 2.1. Adversarial Attacks

Report issue for preceding element

Adversarial attacks manipulate neural network outputs by introducing small, carefully crafted perturbations to input data. Szegedy et al. (fgsm\_bib) demonstrated that minimal, often imperceptible, perturbations could drastically alter deep neural network predictions. Initially observed in image classification, this vulnerability extends to semantic segmentation (arnab2018robustness), object detection (MI2023114; yin2021adc), tracking (SUTTAPAK202221), natural language processing (zhang2019adversarial), and speech recognition (zelasko2021adversarial). Adversarial perturbations are particularly critical as they induce high-confidence misclassifications and generalize across models (transferability\_0). While input-specific perturbations target individual samples, universal perturbations effectively mislead multiple inputs and models (moosavidezfooli2017universal).

Report issue for preceding element

#### Transferability

Report issue for preceding element

Transferability refers to the ability of adversarial examples crafted for one model to mislead different models with varying architectures and training data.
First observed in (szegedyIntriguingPropertiesNeural2014), transferability is linked to adversarial perturbations aligning with model weight vectors and complexity (DemontisMPJBONR19; klause2025relationshipnetworksimilaritytransferability).
Petrov et al. (transferability\_1) and Alvarez et al. (alvarezExploringTransferabilityAdversarial2023) found perturbation similarities across related architectures.

Report issue for preceding element

### 2.2. Risk Estimation

Report issue for preceding element

Previous research has primarily investigated adversarial risk by measuring model accuracy under adversarially perturbed inputs (fgsm\_bib; pgd\_bib). While these individual evaluations provide useful insights, they fail to capture the full spectrum of adversarial risk, as a model’s robustness can vary significantly depending on the type of attack and the perturbation budget.
RobustBench (croce2020robustbench), a standardized benchmark for adversarial robustness, addresses this issue by incorporating AutoAttack (Croce020a), an ensemble of diverse and adaptive adversarial attacks. AutoAttack combines several attack strategies, including APGD (Croce020a), FAB (Croce020), and Square Attack (squareattack\_bib), to provide a more comprehensive robustness assessment. By evaluating models against a curated set of strong attacks, RobustBench helps mitigate the limitations of single-attack evaluations.
However, adversarial robustness depends not only on attack diversity, but also on the perturbation budget, which defines the maximum allowable change to an input. Evaluating robustness over different perturbation budgets is essential to understanding the behavior of the model under different attack strengths. For example, (guo2024exploringadversarialfrontierquantifying) shows that robustness metrics can shift significantly when perturbation constraints are relaxed or tightened. Without such multi-scale evaluations, adversarial risk assessments remain incomplete, potentially leading to misleading conclusions about a model’s true robustness.
In (TramerB19) the authors highlight the trade-offs in multi-perturbation robustness and provide insights into how different perturbation types affect adversarial risk.
Given the diversity of attack strategies, the current state of the art covers query-based white-box and black-box attacks, including gradient-based methods and optimization-based attacks. Risk estimation for transfer-based approaches is investigated in (klause2025relationshipnetworksimilaritytransferability) on a per model basis.

Report issue for preceding element

## 3\. Neural Network Similarity: CKA

Report issue for preceding element

Several methods exist for evaluating similarity of neural networks. Canonical Correlation Analysis (CCA) (cca\_bib) is a statistical method for finding relationships among variables which has been adapted to use in comparison of activation patterns in neural networks. Similarly, Singular Vector Canonical Correlation Analysis (SVCCA) (svcca\_bib) augments the CCA methodology by forming the comparison after a dimensionality reduction of the activation space via singular value decomposition (SVD). This dimensionality reduction results in increased robustness to noise, and greater utility in high-dimensional representations. Both CCA and SVCCA rely on linear correlation.

Report issue for preceding element

In contrast, Centered Kernel Alignment (CKA)(cka\_bib) can be used to evaluate similarities among networks with complex, non-linear transformations, and is thus useful in application to both linear and non-linear representations. CKA utilizes a normalization of the Hilbert-Schmidt Independence Criterion (HSIC) (GrettonBSS05) as a means to non-parametrically measure variable independence, comparing similarity matrices of the activations induced by a set of inputs across two or more models. This results in a similarity score between 0 and 1. By evaluating the similarities in how various networks respond to identical inputs, CKA is a useful tool for understanding how models map relationships, and how these learned mappings differ among models. A CKA network similarity score provides an estimation of similarity between networks. Due to its robustness in capturing representational similarity, CKA is the chosen method for comparing CNNs in this work.

Report issue for preceding element

## 4\. Coverage Testing

Report issue for preceding element![Refer to caption](https://arxiv.org/html/2511.05102v1/content/figures/IMG_1253.png)Figure 1. Conceptual illustration of adversarial subspace overlap across models with varying similarity. Target model (yellow) and potential surrogate models (a–e), each with its own adversarial subspace.Report issue for preceding element

### 4.1. Full-Coverage Testing Feasibility: Transferability, Scope, and Search Space

Report issue for preceding element

Black-box poisoning attacks present a range of most-likely attack scenarios; it is assumed that attackers have partial but incomplete knowledge of systems and data, versus white-box attacks, in which the adversary has total access to all critical system parameters and assets. Black-box attacks thus likely mirror real-life scenarios more closely than white-box methods. Black-box attacks may be classified as transfer- or query-based. Query-based methods require an ability on the attacker’s part to probe a system and iteratively refine attacks, whereas transfer-based attacks attempt to construct an approximate surrogate model, and design optimized attacks against the surrogate which are intended to transfer to the target model (CinaGDVZMOBPR23). A number of attack methods found in the literature are transfer-based, and attack transferability is found to be generally high (DemontisMPJBONR19). Attack transferability thus plays a significant role in data poisoning.

Goodfellow et al (2014) noted that adversarial samples occur in large, contiguous subspaces, rather than randomly scattered pockets (fgsm\_bib). Tramèr et al (2017) found that transferable adversarial examples may span a contiguous subspace of ∼25\\sim 25 dimensionality, which is large. The dimensionality of these subspaces is relevant to transferability because the higher the dimensionality, the more likely it is that the subspaces of two models will intersect significantly, thus enabling transfer (transferability\_3).

Attacks are largely model agnostic, with transferability enabled by similarities in decision boundaries which are shared by models of different classes, and may not be displaced by adversarial training (transferability\_3). Given the large adversarial sample space, as well as the nature of transferability vis-a-vis decision boundary similarity, defining a subset of applicable attacks and corresponding tests for a given model system may be infeasible.

If defining appropriate testing for full coverage requires finding all intersecting adversarial subspaces, achieving full testing coverage may be infeasible.

Demontis et al (2018) give a formal definition for transferability that depends on: (1) the size of input gradients of the target classifier; (2) how well the gradients of the surrogate and target models align; and (3) the variance of the loss landscape optimized to generate the attack points \[4\]. Given the high importance of transferability in poisoning scenarios, the number of potential applicable attacks (and corresponding tests) would likely correlate to these three metrics, evaluated on a per-model basis. This presents a challenging combinatorial analysis problem, in addition to the difficulty of defining all intersecting subspaces.

Ding et al (2020) formulate robust optimization against outliers as a combinatorial optimization problem, showing that even the simplest one-class SVM with outliers problem is NP-complete, with no fully polynomial-time approximation scheme unless P = NP, meaning that it is unlikely to achieve a near-optimal solution in polynomial time (Ding20). This further suggests infeasibility of anticipating and testing for every potential vector.

Conclusion: both empirical data and formal methods cast doubt on the feasibility of achieving full or even adequate coverage via resilience testing.

Report issue for preceding element

### 4.2. Best-Coverage Testing: Exploiting Adversarial Subspaces to Increase Coverage and Attackers’ Costs

Report issue for preceding element

While we cannot cover all adversarial subspaces, we can try to maximize our coverage & increase attacker costs. In order to increase testing coverage, we may begin by deriving some n number of surrogate models which do not have overlapping adversarial subspaces, and test using these. If the subspaces overlap, there may be reduced value to testing with more than one surrogate. Determining overlap is key, yet mapping subspaces is likely infeasible.

Since we cannot easily map the subspaces, we may instead choose surrogates which exhibit both high and low similarity to the model being tested. In absence of the ability to prove the lack of subspace overlap, we may minimize the probability of testing on overlapping subspaces by choosing both quantitatively similar and different surrogates to test. The identification of these surrogates first requires selection of a metric by which to estimate their similarity.
The concept is illustrated in Figure [1](https://arxiv.org/html/2511.05102v1#S4.F1 "Figure 1 ‣ 4. Coverage Testing ‣ Quantifying the Risk of Transferred Black Box Attacks"), the adversarial subspace overlap across models with varying similarity. The target model is surrounded by potential surrogate models, each model induces its own adversarial subspace, with the degree of intersection indicating the potential for transferability of adversarial examples. Surrogate models more similar to the target model (e.g., models a and b) exhibit greater overlap with the target model’s adversarial subspace, suggesting higher attack transferability. In contrast, dissimilar models (e.g., d and e) show reduced overlap, limiting the effectiveness of transferred attacks.

Report issue for preceding element

### 4.3. Similarity Thresholds Via Centered Kernel Alignment

Report issue for preceding element

Achieving maximum adversarial subspace coverage, with the goal of increasing cost of attacks, likely requires diversity of test surrogates. However, defining the number and metric for diversity of surrogates is challenging. How many surrogates we choose would ideally be tied to complexity of the pre-production model in testing; however this is difficult to quantify currently and thus to scale as a requirement for production systems. Ideally tests could be performed to determine subspace overlap (in order to avoid overlap and achieve more coverage), but this is currently infeasible. In this light, a means of comparing similarity of networks may serve as a proxy for evaluating potential subspace overlap.

Report issue for preceding element

Previous work has demonstrated effectiveness of CKA similarity scores for estimation of black-box attack success rates (klause2025relationshipnetworksimilaritytransferability). We extend this work here to provide a methodology for risk estimation; specifically, quantification of the risk of transferability of black-box attacks.

Report issue for preceding element

### 4.4. A More Formal Definition

Report issue for preceding element

Since evaluating transferability of all potential attacks effective against all potential surrogate models is infeasible, we may define a subset of surrogate models via their measured similarity to one another, and test against these. To ensure maximum coverage of subspaces, we apply our similarity definition to the selection of both highly similar, and highly disparate, models.

Report issue for preceding element

In order to achieve testing coverage of as disparate a set of adversarial subspaces as reasonably feasible, testing should consist of surrogate models calculated to have both high and low CKA similarity to the pre-production model in testing MpM\_{p}. For convenience, we may discuss these loosely as subsets of the whole set of surrogate models whose derivations might exist in shared adversarial subspaces. We can thus define some nn number of requisite surrogate models to be derived and tested against the pre-production model for attack transferability. Due to the high importance of transferability to adversarial attack susceptibility, and the relationships among model similarity and complexity to the likelihood of extant shared adversarial subspaces, organizations should test using n>2n>2 derived surrogate models SS, with at least n≥1n\\geq 1 surrogate models from a pool of highly-similar networks, and n≥1n\\geq 1 surrogate models from a pool of low-similarity networks, quantified on the basis of their calculated CKA similarity to the pre-production model in testing. Increasing nn (e.g., n≥5n\\geq 5) provides greater statistical significance and may lead to better coverage of diverse adversarial spaces.

Report issue for preceding element

Let M1M\_{1} represent the members of a subset of surrogate models exhibiting close CKA similarity to MpM\_{p}. Let M2M\_{2} represent the members of a subset of surrogate models found to have lower CKA similarity relative to MpM\_{p}. Let \|M1\|\|M\_{1}\| and \|M2\|\|M\_{2}\| represent the cardinality of M1M\_{1} and M2M\_{2}, respectively.

Report issue for preceding element

Let rr represent the CKA similarity threshold for each model subset. Let r1r\_{1} represent the lower bound of CKA similarity between the pre-production model and surrogate(s) in M1M\_{1}. Let r2r\_{2} represent the upper bound of CKA similarity between the pre-production model and members of M2M\_{2}.

Report issue for preceding element

We can thus define:

Report issue for preceding element

M1={Si∣CKA​(Si,Mp)≥r1}M\_{1}=\\{S\_{i}\\mid\\text{CKA}(S\_{i},M\_{p})\\geq r\_{1}\\}, and
M2={Sj∣CKA​(Sj,Mp)≤r2}M\_{2}=\\{S\_{j}\\mid\\text{CKA}(S\_{j},M\_{p})\\leq r\_{2}\\} with r1r\_{1} and r2r\_{2} satisfying 0<r2<r1<10<r\_{2}<r\_{1}<1.

Report issue for preceding element

To maximize potential coverage, organizations should perform pre-release resilience testing consisting of attacks derived from some

Report issue for preceding element

\|M1\|≥1\|M\_{1}\|\\geq 1, and
\|M2\|≥1\|M\_{2}\|\\geq 1

Report issue for preceding element

number of surrogate models from their respective complexity threshold groups.

Report issue for preceding element

#### Selecting the Thresholds

Report issue for preceding element

Concrete guidance for defining suitable threshold values for r1r\_{1} and r2r\_{2} can be derived empirically. For instance, selecting r1≈0.55r\_{1}\\approx 0.55 and r2≈0.35r\_{2}\\approx 0.35 may be appropriate, given that most CNN architectures exhibit a CKA similarity score between 0.32 and 0.57, with a median of approximately 0.45 (klause2025relationshipnetworksimilaritytransferability). However, the precise determination of these thresholds should be contextually informed by initial empirical experimentation and considerations specific to the domain of application.

Report issue for preceding element

Building upon the CKA metric, the Diagonal Box Similarity (DBS) score was introduced in (klause2025relationshipnetworksimilaritytransferability) to more effectively quantify localized layer-to-layer similarity between neural networks. DBS scores for most CNN architectures typically range from 0.4 to 0.75, thereby facilitating more granular and precise threshold selections, such as r1≈0.7r\_{1}\\approx 0.7 and r2≈0.45r\_{2}\\approx 0.45.

Report issue for preceding element

## 5\. Conclusion & Future Work

Report issue for preceding element

This paper addresses the challenges in resilience testing against transferred black-box adversarial evasion attacks, emphasizing transfer-based methods due to their practical relevance and inherent high transferability among neural network models. Recognizing the computational infeasibility of exhaustive exploration of high-dimensional input spaces, the paper argues against attempting complete test coverage for adversarial risk mapping.
To overcome these constraints, we introduce a targeted resilience testing framework utilizing surrogate models strategically selected via Centered Kernel Alignment (CKA) similarity. By incorporating surrogate models with both high and low CKA similarity relative to the target model, the proposed framework enhances coverage of adversarial subspaces. Risk estimation within this approach employs regression-based estimators, offering practical, realistic quantification of adversarial risk.
Furthermore, the framework supports model selection strategies aimed at minimizing susceptibility, thus elevating attacker costs and reducing exposure. The approach incorporates clear, threshold-based criteria to facilitate straightforward implementation in resilience testing processes.
Given the increasing regulatory emphasis on integrating quantitative risk assessment into AI security standards, the proposed methodology provides an efficient and actionable solution. It enables organizations to achieve accurate risk quantification and regulatory compliance.
Future work will focus on developing more accurate similarity metrics, with an emphasis on improving computational efficiency. Ideally, these metrics should be derived from the model architecture itself rather than relying on activations. By leveraging structural properties and design patterns of neural networks, we aim to create methods that offer faster and more scalable comparisons while maintaining high reliability in assessing model similarity, with the ultimate goal of providing increasingly useful and cost-effective risk quantification methods for AI systems in production.

Report issue for preceding element

###### Acknowledgements.

Report issue for preceding elementThis research work has been funded by the German Federal Ministry of Education and Research and the Hessian Ministry of Higher Education, Research, Science and the Arts within their joint support of the National Research Center for Applied Cybersecurity ATHENE.

Report IssueReport Issue for Selection

Generated by
[L\\
A\\
T\\
Exml![[LOGO]](<Base64-Image-Removed>)](https://math.nist.gov/~BMiller/LaTeXML/)
