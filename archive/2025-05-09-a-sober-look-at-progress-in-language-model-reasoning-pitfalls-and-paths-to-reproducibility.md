---
title: "A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility"
tags:
   - Reinforcement Learning
   - Large Language Models
   - Mathematical Reasoning
   - Standardization
   - Evaluation Protocols
link: https://arxiv.org/html/2504.07086v1
date: 2025-05-09
summary: "The paper investigates the performance of language models (LLMs) on mathematical reasoning benchmarks, highlighting significant evaluation inconsistencies attributed to random seed variability, sampling parameters, and hardware/software configurations. It contrasts reinforcement learning (RL) and supervised fine-tuning (SFT) methods, finding that SFT generally yields more reliable and generalizable results, while RL approaches often overfit to specific benchmarks. Proposed best practices include standardizing evaluation procedures, enhancing reproducibility via multi-seed testing, and optimizing hyperparameters per model. The findings emphasize the necessity for rigorous evaluation standards in advancing LLM capabilities."
---

HTML conversions [sometimes display errors](https://info.dev.arxiv.org/about/accessibility_html_error_messages.html) due to content that did not convert correctly from the source. This paper uses the following packages that are not yet supported by the HTML conversion tool. Feedback on these issues are not necessary; they are known and are being worked on.

- failed: fontawesome5
- failed: sourcecodepro
- failed: etoc

Authors: achieve the best HTML results from your LaTeX submissions by following these [best practices](https://info.arxiv.org/help/submit_latex_best_practices.html).

[License: CC BY 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2504.07086v1 \[cs.LG\] 09 Apr 2025

# A Sober Look at Progress in Language Model Reasoning:   Pitfalls and Paths to Reproducibility

Report issue for preceding element

Andreas Hochlehnert1  Hardik Bhatnagar1∗  Vishaal Udandarao1,2∘

Samuel AlbanieAmeya Prabhu1†Matthias Bethge1†

1Tübingen AI Center, University of Tübingen  2 University of Cambridge
equal contribution, ∘ core contributor, †equal advising

Report issue for preceding element

###### Abstract

Report issue for preceding element

Reasoning has emerged as the next major frontier for language models (LMs), with rapid advances from both academic and industrial labs. However, this progress often outpaces methodological rigor, with many evaluations relying on benchmarking practices that lack transparency, robustness, or statistical grounding. In this work, we conduct a comprehensive empirical study and find that current mathematical reasoning benchmarks are highly sensitive to subtle implementation choices—including decoding parameters, random seeds, prompt formatting, and even hardware and software-framework configurations. Performance gains reported in recent studies frequently hinge on unclear comparisons or unreported sources of variance. To address these issues, we propose a standardized evaluation framework with clearly defined best practices and reporting standards. Using this framework, we reassess recent methods and find that reinforcement learning (RL) approaches yield only modest improvements—far below prior claims—and are prone to overfitting, especially on small-scale benchmarks like AIME’24. In contrast, supervised finetuning (SFT) methods show consistently stronger generalization. To foster reproducibility, we release all code, prompts, and model outputs, for reasoning benchmarks, establishing more rigorous foundations for future work.

Report issue for preceding element

|     |
| --- |
| \\faGlobe [Leaderboard](https://bethgelab.github.io/sober-reasoning/ "")\\faGithub [Code](https://github.com/bethgelab/sober_reasoning/ "")\\faDatabase [Eval Logs](https://huggingface.co/datasets/bethgelab/sober_reasoning/ "") |

![Refer to caption](https://arxiv.org/html/x1.png)Figure 1: The Sombre State of LM Reasoning for Math.(left) when re-evaluating recent 1.5B reasoning-enhanced models on AIME-24 using a standardized framework (see Section [4](https://arxiv.org/html/2504.07086v1#S4 "4 Way Forward: Standardization in Evaluations ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility")), we find substantial drops to reported results in the original papers, (right) the observed improvements from recent methods (gray highlighted area) fall entirely within the variance range (orange box plots) of DeepSeek-R1 1.5B model performance.
This suggests that these methods do not significantly outperform the base model—underscoring the importance of rigorous, multi-seed evaluation protocols for obtaining reliable performance estimates.Report issue for preceding element

## 1 Introduction

Report issue for preceding element

> “The first principle is that you must not fool yourself, and you are the easiest person to fool.”
>
> Report issue for preceding element
>
> —Richard Feynman
>
> Report issue for preceding element

Reasoning has become central to recent advances in large language models (LLMs), playing a key role in nearly all frontier systems (Jaech et al., [2024](https://arxiv.org/html/2504.07086v1#bib.bib45 ""); Anthropic, [2025](https://arxiv.org/html/2504.07086v1#bib.bib7 ""); OpenAI, [2025](https://arxiv.org/html/2504.07086v1#bib.bib81 ""); xAI, [2025](https://arxiv.org/html/2504.07086v1#bib.bib111 ""); Meta-AI, [2025](https://arxiv.org/html/2504.07086v1#bib.bib75 ""); DeepMind, [2025](https://arxiv.org/html/2504.07086v1#bib.bib22 "")). Recent months have seen a surge of research focused on understanding and improving LLM reasoning, accompanied by several open-source tools and training strategies (see Li et al. ( [2025b](https://arxiv.org/html/2504.07086v1#bib.bib55 "")) for a survey). This momentum has sparked optimism that building capable, competitive reasoning models may soon be within reach.

Report issue for preceding element

However, as evaluation practices shape the direction and perceived progress of the field (Liao et al., [2021](https://arxiv.org/html/2504.07086v1#bib.bib56 "")), concerns around methodological rigor are growing. Non-reproducible or inconclusive evaluations can distort scientific understanding, misguide adoption, and skew future research priorities (Henderson et al., [2018](https://arxiv.org/html/2504.07086v1#bib.bib37 ""); Marie et al., [2021](https://arxiv.org/html/2504.07086v1#bib.bib73 ""); Musgrave et al., [2020](https://arxiv.org/html/2504.07086v1#bib.bib79 ""); Prabhu et al., [2020](https://arxiv.org/html/2504.07086v1#bib.bib86 ""); Andrychowicz et al., [2020](https://arxiv.org/html/2504.07086v1#bib.bib6 ""); Colas et al., [2018](https://arxiv.org/html/2504.07086v1#bib.bib18 "")). In the fast-moving area of LLM reasoning, where rapid publication cycles and benchmarking races are common, methodological shortcuts can quietly undermine progress. While concerns about reproducibility in LLM evaluations are well-documented (Reuel et al., [2024](https://arxiv.org/html/2504.07086v1#bib.bib92 ""); Biderman et al., [2024](https://arxiv.org/html/2504.07086v1#bib.bib11 "")), their persistence—especially in reasoning—calls for renewed scrutiny and higher standards.

Report issue for preceding element

Motivated by a growing number of inconsistent empirical claims across the reasoning landscape, we conduct a rigorous investigation into the current state of reasoning benchmarks, focusing specifically on mathematical reasoning—one of the most widely used testbeds for evaluating algorithmic advances in this space (HuggingFaceH4, [2024](https://arxiv.org/html/2504.07086v1#bib.bib42 ""); [AI-MO,](https://arxiv.org/html/2504.07086v1#bib.bib3 "")).

Report issue for preceding element

Our main finding is that many recent empirical conclusions may be overly optimistic and fail to generalize under careful re-evaluation. We identify a surprising degree of sensitivity in LLM-based reasoning pipelines to seemingly minor design choices—ranging from decoding parameters, prompt formatting, and random seeds to the hardware and software stacks used during evaluation (see Table [1](https://arxiv.org/html/2504.07086v1#S3.T1 "Table 1 ‣ 3.1 Experimental Setup ‣ 3 Exploring the Design Space of Reasoning: What Matters Most? ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility")). Particularly concerning is the instability introduced by small benchmark sizes: for example, AIME’24 and AMC’23 each contain only 30–40 examples, making performance metrics highly volatile—where even one question can shift Pass@1 by over 3 percentage points. This leads to substantial variance across seeds, often resulting in double-digit performance swings that challenge the reliability of published results. In Section [3](https://arxiv.org/html/2504.07086v1#S3 "3 Exploring the Design Space of Reasoning: What Matters Most? ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility"), we systematically analyze the root causes of this instability, including sampling variance, decoding configurations, evaluation frameworks, and hardware heterogeneity. We show that these factors can significantly distort conclusions if not carefully controlled.

Report issue for preceding element

In Section [4](https://arxiv.org/html/2504.07086v1#S4 "4 Way Forward: Standardization in Evaluations ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility"), we propose a set of best practices aimed at improving reproducibility and rigor in reasoning benchmarks. We also re-evaluate recent techniques using a standardized and reproducible evaluation stack. Our findings are sobering—reinforcement learning (RL) applied to distillation-based models such as DeepSeek-R1 yields little to no statistically significant gains. Some methods, such as OpenRS, show promising results in original reports, but fail to hold up under repeated evaluation. RL training on base models like Qwen2.5 Math does show stronger performance, but still often underperforms instruction-tuned counterparts.111We note that OpenReasoner-Zero is a consistent exception, achieving competitive performance. Furthermore, RL-trained models exhibit significant performance drops on newer benchmarks such as AIME’25, echoing patterns of test set overfitting or “hill-climbing” observed in prior work (Golchin & Surdeanu, [2023](https://arxiv.org/html/2504.07086v1#bib.bib33 ""); Roberts et al., [2023](https://arxiv.org/html/2504.07086v1#bib.bib94 ""); Dominguez-Olmedo et al., [2024](https://arxiv.org/html/2504.07086v1#bib.bib26 "")). In contrast, supervised fine-tuning (SFT) continues to deliver stable, generalizable improvements across benchmarks, underscoring its maturity as a training paradigm. These observations point to a critical need for more reliable and standardized evaluation protocols.

Report issue for preceding element

Taken together, in this work, we aim to provide not only a clearer assessment of where current methods stand, but also the tools and practices needed to make reasoning evaluation more transparent, robust, and reproducible. To this end, we open-source all code, prompts, and outputs to facilitate fair and accountable progress in this increasingly important area.

Report issue for preceding element

## 2 Related Works

Report issue for preceding element

Language Model Reasoning (for Math).
The recent releases of OpenAI-O1 (Jaech et al., [2024](https://arxiv.org/html/2504.07086v1#bib.bib45 "")) (in September 2024), OpenAI-O3 (OpenAI, [2025](https://arxiv.org/html/2504.07086v1#bib.bib81 "")) (in December 2024) and DeepSeek-R1 (DeepSeek-AI, [2025](https://arxiv.org/html/2504.07086v1#bib.bib23 "")) (in January 2025), have spurred the language modelling community to work on improving the reasoning capabilites of language models. Several popular methods for improving those capabilites have emerged with supervised fine-tuning (SFT) and reinforcement learning (RL) being the two primary methods of interest (Uesato et al., [2022](https://arxiv.org/html/2504.07086v1#bib.bib106 ""); Lightman et al., [2023](https://arxiv.org/html/2504.07086v1#bib.bib57 ""); Lyu et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib68 ""); Team, [2025](https://arxiv.org/html/2504.07086v1#bib.bib102 "")). Recent works have built upon the DeepSeek-R1 recipe by proposing newer RL algorithms, including LCPO (Aggarwal & Welleck, [2025](https://arxiv.org/html/2504.07086v1#bib.bib2 "")), REINFORCE++ (Hu, [2025](https://arxiv.org/html/2504.07086v1#bib.bib39 "")), DAPO (Yu et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib117 "")), DPO-VP (Tu et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib104 "")), VinePPO (Kazemnejad et al., [2024](https://arxiv.org/html/2504.07086v1#bib.bib50 "")), CPPO (Lin et al., [2025a](https://arxiv.org/html/2504.07086v1#bib.bib59 "")), VAPO (Yue et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib119 "")) and GRO (Cai, [2025](https://arxiv.org/html/2504.07086v1#bib.bib13 "")). To gain a stronger understanding of how to induce mathematical capabilities, other works have conducted significant empirical studies exploring the design space of RL methods (Zeng et al., [2025b](https://arxiv.org/html/2504.07086v1#bib.bib121 ""); Liu et al., [2025b](https://arxiv.org/html/2504.07086v1#bib.bib65 ""); Team et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib103 ""); Shao et al., [2024](https://arxiv.org/html/2504.07086v1#bib.bib96 "")), including data scaling trends (Shen et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib97 "")), curriculums (Wen et al., [2025b](https://arxiv.org/html/2504.07086v1#bib.bib110 ""); Roux et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib95 "")) and reward design (Gao et al., [2024a](https://arxiv.org/html/2504.07086v1#bib.bib30 ""); Cui et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib19 ""); Ma et al., [2023](https://arxiv.org/html/2504.07086v1#bib.bib70 "")). Based on the success of these methods, there have also been recent efforts into scaling up reinforcement learning approaches to induce reasoning in domains beyond math, including code (Liu & Zhang, [2025](https://arxiv.org/html/2504.07086v1#bib.bib62 ""); Xie et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib112 ""); Jha et al., [2024](https://arxiv.org/html/2504.07086v1#bib.bib46 ""); Yu et al., [2024](https://arxiv.org/html/2504.07086v1#bib.bib116 "")), medicine (Zhang et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib122 ""); Sim & Chen, [2024](https://arxiv.org/html/2504.07086v1#bib.bib98 "")) and other sciences (Su et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib101 ""); Yuan et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib118 ""); Zeng et al., [2025a](https://arxiv.org/html/2504.07086v1#bib.bib120 "")).
Further, some works also explored scaling up RL-based approaches to modalities beyond just language, including vision (Ma et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib69 ""); Meng et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib74 ""); Huang et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib41 ""); Peng et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib84 ""); [Chen et al.,](https://arxiv.org/html/2504.07086v1#bib.bib17 ""); Deng et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib25 ""); Liu et al., [2025c](https://arxiv.org/html/2504.07086v1#bib.bib66 ""); Feng et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib28 ""); Lin et al., [2025b](https://arxiv.org/html/2504.07086v1#bib.bib60 "")). In our work, we objectively re-evaluate the claims made by several of these recent works under a standardized lens, and find that many of the reported gains do not hold up strongly when pitted on a level-playing field against well-tuned baselines.

Report issue for preceding element

Sobering Studies on ML Progress. Machine learning is a field of rapid progress. Due to the lightning speed of papers coming out across the various sub-fields of machine learning, practitioners and researchers often fail to rigorously evaluate algorithmic progress (Hutchinson et al., [2022](https://arxiv.org/html/2504.07086v1#bib.bib43 ""); Dehghani et al., [2021](https://arxiv.org/html/2504.07086v1#bib.bib24 ""); Machado et al., [2018](https://arxiv.org/html/2504.07086v1#bib.bib71 ""); Ghosh et al., [2024](https://arxiv.org/html/2504.07086v1#bib.bib32 ""); Balduzzi et al., [2018](https://arxiv.org/html/2504.07086v1#bib.bib9 ""); Liao et al., [2021](https://arxiv.org/html/2504.07086v1#bib.bib56 ""); Cawley & Talbot, [2010](https://arxiv.org/html/2504.07086v1#bib.bib15 ""); Lipton & Steinhardt, [2019](https://arxiv.org/html/2504.07086v1#bib.bib61 ""); Prabhu et al., [2024b](https://arxiv.org/html/2504.07086v1#bib.bib88 "")). This has led to several papers showing that simple well-tuned baselines outperform months of progress on a specific sub-field in machine learning, including in continual learning (Prabhu et al., [2024a](https://arxiv.org/html/2504.07086v1#bib.bib87 ""); [2020](https://arxiv.org/html/2504.07086v1#bib.bib86 "")), active learning (Cawley, [2011](https://arxiv.org/html/2504.07086v1#bib.bib14 "")) and test-time adaptation (Press et al., [2023](https://arxiv.org/html/2504.07086v1#bib.bib89 "")). With the rapid influx of reasoning-based LMs, such statistically rigorous comparisons of models are ever more important—yet, despite the heavy use of RL-algorithms for driving progress in reasoning, there is very little mention of how different methods standardize their evaluations across different factors of variability. RL-algorithms themselves are known to be quite fickle to extremely minor variations including random seeds (Agarwal et al., [2021](https://arxiv.org/html/2504.07086v1#bib.bib1 ""); Gorsane et al., [2022](https://arxiv.org/html/2504.07086v1#bib.bib34 ""); Chan et al., [2019](https://arxiv.org/html/2504.07086v1#bib.bib16 ""); Jordan et al., [2020](https://arxiv.org/html/2504.07086v1#bib.bib47 ""); Patterson et al., [2024](https://arxiv.org/html/2504.07086v1#bib.bib83 "")). Some works have even gone as far as suggesting that reliable benchmarking of RL-based methods is computationally infeasible (Jordan et al., [2024](https://arxiv.org/html/2504.07086v1#bib.bib48 "")).
Additionally, other works have demonstrated critical reliability issues in the generalization of frontier models to minor perturbations in the question inputs (Mirzadeh et al., [2024](https://arxiv.org/html/2504.07086v1#bib.bib77 ""); Nezhurina et al., [2024](https://arxiv.org/html/2504.07086v1#bib.bib80 ""); Srivastava et al., [2024](https://arxiv.org/html/2504.07086v1#bib.bib100 "")), the type of tasks tested (Yan et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib113 ""); Petrov et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib85 ""); Dominguez-Olmedo et al., [2024](https://arxiv.org/html/2504.07086v1#bib.bib26 ""); Roberts et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib93 "")), metrics used (Liu et al., [2024](https://arxiv.org/html/2504.07086v1#bib.bib63 "")) and in data-scarce scenarios (Udandarao et al., [2024](https://arxiv.org/html/2504.07086v1#bib.bib105 ""); Kandpal et al., [2023](https://arxiv.org/html/2504.07086v1#bib.bib49 ""); Parashar et al., [2024](https://arxiv.org/html/2504.07086v1#bib.bib82 "")). Given such a volatile landscape, in this work, we aim to level the playing field across recent LM-methods that have been released and provide an objective look on the progress that the reasoning community has made. Our findings, which we discuss in the rest of the paper, are sobering at best.

Report issue for preceding element

## 3 Exploring the Design Space of Reasoning: What Matters Most?

Report issue for preceding element

Recent reasoning-focused language models are evaluated under highly heterogeneous conditions—including differences in evaluation frameworks and hardware, number of random seeds, temperature, and nucleus sampling parameters (top\_p) (see Table [1](https://arxiv.org/html/2504.07086v1#S3.T1 "Table 1 ‣ 3.1 Experimental Setup ‣ 3 Exploring the Design Space of Reasoning: What Matters Most? ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility")). While prior work has examined the effect of sampling parameters in multiple-choice (Renze, [2024](https://arxiv.org/html/2504.07086v1#bib.bib91 "")) and coding tasks (Arora et al., [2024](https://arxiv.org/html/2504.07086v1#bib.bib8 "")), the influence of these choices remains underexplored for open-ended reasoning models—particularly those trained with reinforcement learning. In this section, we systematically assess how these evaluation design choices affect reported performance, and highlight the sources of variance that most impact the reliability of results.

Report issue for preceding element

### 3.1 Experimental Setup

Report issue for preceding element

We adopt a consistent experimental setup throughout this section, unless otherwise stated. Our analysis includes nine widely used models grouped into two commonly benchmarked size classes: 1.5B and 7B parameters. For the 1.5B class, we evaluate: DeepSeek-R1-Distill-1.5B (DeepSeek-AI, [2025](https://arxiv.org/html/2504.07086v1#bib.bib23 "")), DeepScaleR-1.5B (Luo et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib67 "")), II-1.5B-Preview (Intelligent Internet, [2025](https://arxiv.org/html/2504.07086v1#bib.bib44 ""))
, OpenRS1-1.5B, OpenRS2-1.5B, and OpenRS3-1.5B (Dang & Ngo, [2025](https://arxiv.org/html/2504.07086v1#bib.bib20 "")). Note that DeepScaleR-1.5B, II-1.5B-Preview, and the OpenRS models are all initialized from DeepSeek-R1-Distill-1.5B and subsequently finetuned via reinforcement learning (e.g., GRPO (Shao et al., [2024](https://arxiv.org/html/2504.07086v1#bib.bib96 ""))) to enhance mathematical reasoning capabilities. For the 7B class, we evaluate: DeepSeek-R1-Distill-7B, S1.1-7B (Muennighoff et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib78 "")), and OpenThinker-7B (Team, [2025](https://arxiv.org/html/2504.07086v1#bib.bib102 "")). Both S1.1-7B and OpenThinker-7B are finetuned Qwen2.5-7B-Instruct models (Yang et al., [2024a](https://arxiv.org/html/2504.07086v1#bib.bib114 "")), trained using supervised learning on reasoning traces derived from DeepSeek-R1. All models are benchmarked on three widely used datasets: AIME’24 ( [AI-MO,](https://arxiv.org/html/2504.07086v1#bib.bib3 "")), AMC’23 (AI-MO, [2024](https://arxiv.org/html/2504.07086v1#bib.bib4 "")), and MATH500 (Hendrycks et al., [2021](https://arxiv.org/html/2504.07086v1#bib.bib38 "")), using the Pass@1 metric. Each result is averaged over multiple seeds and obtained on a standardized software stack (throguh a Docker image), and hardware with the following configuration: one 40 GB A100 GPU, an AMD 7302 32-core CPU, and 1TB RAM. All experiments were run using lighteval(Fourrier et al., [2023](https://arxiv.org/html/2504.07086v1#bib.bib29 "")) with the vllm backend (Kwon et al., [2023](https://arxiv.org/html/2504.07086v1#bib.bib52 "")).

Report issue for preceding element

Table 1: Taxonomy of current open-weight reasoning models. For each model, we report the base model it was post-trained from and the exact type of post-training algorithm applied (RL vs SFT). Further, we note the evaluation framework that the original paper uses for reporting results along with the exact temperature, generation sequence length, and top\_p sampling parameters used for AIME-24 evaluation, with the number of generations used for computing Pass@1 (K). It is evident that there is no clear standardization across different models with respect to evaluation frameworks used and the sampling parameters. This motivates the need to closely scrutinize the evaluations of current reasoning models.

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Model | Algorithm | Base | Framework | Temp | Top\_p | Seq. Len | K |
| DeepSeek-R1-Distill-1.5B | SFT | Qwen2.5-Math-1.5B | – | 0.6 | 0.95 | 32,768 | 64 |
| DeepSeek-R1-Distill-7B | SFT | Qwen2.5-Math-7B | – | 0.6 | 0.95 | 32,768 | 64 |
| DeepSeek-R1-Distill-14B | SFT | Qwen2.5-14B | – | 0.6 | 0.95 | 32,768 | 64 |
| DeepSeek-R1-Distill-32B | SFT | Qwen2.5-32B | – | 0.6 | 0.95 | 32,768 | 64 |
| OpenThinker-32B | SFT | Qwen2.5-32B-Instruct | evalchemy | 0.7 | 0.8 | 32,768 | 5 |
| Bespoke-Stratos-32B | SFT | Qwen2.5-32B-Instruct | evalchemy | 0.7 | 0.8 | 32,768 | 5 |
| Bespoke-Stratos-7B | SFT | Qwen2.5-7B-Instruct | evalchemy | 0.7 | 0.8 | 32,768 | 5 |
| s1.1-7B | SFT | Qwen2.5-7B-Instruct | lm-eval-harness | 0 | – | 32,768 | 64 |
| s1.1-32B | SFT | Qwen2.5-32B-Instruct | lm-eval-harness | 0 | – | 32,768 | 64 |
| LIMO | SFT | Qwen2.5-32B-Instruct | math-eval-harness | 0 | 1 | 32,768 | 1 |
| MiniMath-R1-1.5B | SFT | DeepSeek-R1-Distill-1.5B | oumi-ai | – | – | – | – |
| DeepScaleR-1.5B-Preview | RL | DeepSeek-R1-Distill-1.5B | verl | 0.6 | 0.95 | 32,768 | 16 |
| Open-RS1 | RL | DeepSeek-R1-Distill-1.5B | lighteval | 0.6 | 0.95 | 32,768 | 32 |
| Open-RS2 | RL | DeepSeek-R1-Distill-1.5B | lighteval | 0.6 | 0.95 | 32,768 | 32 |
| Open-RS3 | RL | DeepSeek-R1-Distill-1.5B | lighteval | 0.6 | 0.95 | 32,768 | 32 |
| II-Thought-1.5B-Preview | RL | DeepSeek-R1-Distill-1.5B | evalscope | 0.6 | 0.95 | 32,768 | 64 |
| Oat-Zero-1.5B | RL | Qwen2.5-Math-1.5B | custom | 0 | 1 | 3,000 | 1 |
| Oat-Zero-7B | RL | Qwen2.5-Math-7B | custom | 0 | 1 | 3,000 | 1 |
| STILL-3-1.5B-preview | RL | DeepSeek-R1-Distill-1.5B | custom | 0.6 | 0.95 | 32,768 | 5 |
| FastCurl-1.5B-Preview | RL | DeepSeek-R1-Distill-1.5B | verl | 0.6 | 0.95 | 32,768 | 16 |
| LIMR | RL | Qwen2.5-Math-7B | custom | 0.4 | 0.95 | 3,072 | 4 |

Report issue for preceding element

Sampling Parameters: To systematically compare the impact of sampling parameters on accuracy, all experiments in this section were performed with a standardized configuration: temperature=0.8, top\_p=0.9, and both max\_model\_len and max\_new\_tokens set to 32,768 tokens. This context length matches the limits of models such as OpenThinker-7B and S1.1-7B, although certain models (e.g., DeepSeek) support longer sequences of up to 131,072 tokens. We chose this standardized evaluation length to ensure comparability, with a detailed analysis of the influence of completion length presented in Figure [9](https://arxiv.org/html/2504.07086v1#S3.F9 "Figure 9 ‣ 3.4 Effect of Prompt Format and Context Length ‣ 3 Exploring the Design Space of Reasoning: What Matters Most? ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility"). Unless otherwise specified, results in this section are averaged over 10 random seeds for AIME’24 and AMC’23, and 3 seeds for MATH500, following the recommendations from Section [3.2.1](https://arxiv.org/html/2504.07086v1#S3.SS2.SSS1 "3.2.1 Can Bootstrapping Improve Mean Estimates? ‣ 3.2 Seed Variance in Evaluation ‣ 3 Exploring the Design Space of Reasoning: What Matters Most? ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility").

Report issue for preceding element

### 3.2 Seed Variance in Evaluation

Report issue for preceding element![Refer to caption](https://arxiv.org/html/x2.png)Figure 2: Accuracy varies significantly across random seeds. We find significantly high Pass@1 variation across 20 different random seeds for nine models on AIME’24, AMC’23, and MATH500. Variance is particularly high on AIME’24 (upto 15%) and AMC’23 (upto 13%) due to the small number of test samples, highlighting instability of single-seed evaluations.Report issue for preceding element

We begin by analyzing the variance induced purely by the random seed used during evaluation—an aspect often neglected in benchmarking practices. While recent work calls for statistical rigor (e.g., using error bars and multiple runs) (Bowyer et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib12 ""); Biderman et al., [2024](https://arxiv.org/html/2504.07086v1#bib.bib11 ""); [Madaan et al.,](https://arxiv.org/html/2504.07086v1#bib.bib72 "")), evaluations frequently rely on single-seed runs, obscuring potential variability. We assess the seed-induced variance across 20 independent evaluation runs for each of the nine models. Results are shown in Figure [2](https://arxiv.org/html/2504.07086v1#S3.F2 "Figure 2 ‣ 3.2 Seed Variance in Evaluation ‣ 3 Exploring the Design Space of Reasoning: What Matters Most? ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility").

Report issue for preceding element

Key Insight.
Pass@1 values show surprisingly high standard deviation—ranging from 5 to 15 percentage points across seeds. This issue is particularly severe for AIME’24 and AMC’23, which have only 30 and 40 test samples respectively. A change in just one question shifts Pass@1 by 2.5–3.3 percentage points.

Report issue for preceding element

Takeaway 1  Single-seed evaluations on small datasets are highly unstable. Accurate reporting requires averaging over multiple seeds.Report issue for preceding element

Takeaway 2  Small datasets such as AIME24 (30 samples) make model comparisons unreliable, as solving just one extra question already shifts pass@1 by  3%. Variance from sampling parameters or random seeds can easily cause fluctuations of 1–2 correct answers, leading to unstable rankings – especially when models cluster around 30% performance.Report issue for preceding element

#### 3.2.1 Can Bootstrapping Improve Mean Estimates?

Report issue for preceding element![Refer to caption](https://arxiv.org/html/x3.png)Figure 3: Bootstrapped seed averaging is reliable only beyond a threshold. We plot the variance of Mean Pass@1 scores on AIME’24 when averaging over K=1𝐾1K=1italic\_K = 1 to K=10𝐾10K=10italic\_K = 10 seed runs, finding that the variance is extremely high for small K𝐾Kitalic\_K and significantly reduced by K=10𝐾10K=10italic\_K = 10. This suggests that using multi-seed evaluations (K≥10𝐾10K\\geq 10italic\_K ≥ 10) would yield more stable estimates. For results on AMC23 and MATH500 see Figures [12](https://arxiv.org/html/2504.07086v1#A1.F12 "Figure 12 ‣ A.1 Bootstrapping Results on Additional Datasets ‣ Appendix A Appendix ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility") and [13](https://arxiv.org/html/2504.07086v1#A1.F13 "Figure 13 ‣ A.1 Bootstrapping Results on Additional Datasets ‣ Appendix A Appendix ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility") respectively.Report issue for preceding element

To mitigate high variance, recent work has adopted bootstrapping—averaging multiple evaluation runs to stabilize results. For example, DeepSeek reports Pass@1 over 64 runs, while DeepScaleR uses 16. We study the effectiveness of this approach by bootstrapping estimates for AIME’24 using 1 to 10 evaluation runs. Figure [3](https://arxiv.org/html/2504.07086v1#S3.F3 "Figure 3 ‣ 3.2.1 Can Bootstrapping Improve Mean Estimates? ‣ 3.2 Seed Variance in Evaluation ‣ 3 Exploring the Design Space of Reasoning: What Matters Most? ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility") shows that while variance is extreme for K=1𝐾1K=1italic\_K = 1 and still large for K=2𝐾2K=2italic\_K = 2, it reduces sharply for K≥10𝐾10K\\geq 10italic\_K ≥ 10. Further analysis of variance across additional datasets is presented Figures [12](https://arxiv.org/html/2504.07086v1#A1.F12 "Figure 12 ‣ A.1 Bootstrapping Results on Additional Datasets ‣ Appendix A Appendix ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility") and [13](https://arxiv.org/html/2504.07086v1#A1.F13 "Figure 13 ‣ A.1 Bootstrapping Results on Additional Datasets ‣ Appendix A Appendix ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility").

Report issue for preceding element

Takeaway 3  Bootstrapping over 10 runs substantially stabilizes Pass@1 estimates and should be considered a minimal standard for reliable evaluation.Report issue for preceding element

#### 3.2.2 Variance from Sampling Parameters: Temperature and top-p

Report issue for preceding element![Refer to caption](https://arxiv.org/html/x4.png)Figure 4: Higher temperatures yield better accuracies. We find across all three datasets, higher temperatures produce better peak accuracy but introduce instability, revealing a tradeoff between performance and reproducibility. Results obtained by varying temperature from 0 to 1 in increments of 0.1, while keeping top\_p fixed at 0.9.Report issue for preceding element![Refer to caption](https://arxiv.org/html/x5.png)Figure 5: Higher top\_p values improve performance at no cost to stability. Across all datasets, we find that higher top\_p values generally improve performance while preserving similar amounts of variance as lower top\_p values. Results were obtained by varying top\_p from 0 to 1 in increments of 0.1, while holding the temperature constant at 0.8.Report issue for preceding element

Reducing the temperature or increasing the nucleus sampling parameter (top\_p) improves the accuracy of performance estimates without incurring additional computational cost. Figure [4](https://arxiv.org/html/2504.07086v1#S3.F4 "Figure 4 ‣ 3.2.2 Variance from Sampling Parameters: Temperature and top-p ‣ 3.2 Seed Variance in Evaluation ‣ 3 Exploring the Design Space of Reasoning: What Matters Most? ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility") illustrate the impact of temperature and Figure [5](https://arxiv.org/html/2504.07086v1#S3.F5 "Figure 5 ‣ 3.2.2 Variance from Sampling Parameters: Temperature and top-p ‣ 3.2 Seed Variance in Evaluation ‣ 3 Exploring the Design Space of Reasoning: What Matters Most? ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility") show that of top\_p across multiple models and datasets. Notably, a more reproducible estimate is associated with significant drops in measured performance, highlighting a consistent tradeoff between reproducibility and high performance. We recommend optimizing the temperature for performance, and comparing the best parameter per model.

Report issue for preceding element

Additionally, we investigate the impact of the temperature and top\_p hyperparameter as prior works often employ different temperature and top\_p settings when comparing the same model. To isolate the impact of varying temperature and top\_p, we averaged pass@1 across seeds and compute variation of this estimate across temperature and top\_p in a boxplot. Figure [6](https://arxiv.org/html/2504.07086v1#S3.F6 "Figure 6 ‣ 3.2.2 Variance from Sampling Parameters: Temperature and top-p ‣ 3.2 Seed Variance in Evaluation ‣ 3 Exploring the Design Space of Reasoning: What Matters Most? ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility") and [7](https://arxiv.org/html/2504.07086v1#S3.F7 "Figure 7 ‣ 3.2.2 Variance from Sampling Parameters: Temperature and top-p ‣ 3.2 Seed Variance in Evaluation ‣ 3 Exploring the Design Space of Reasoning: What Matters Most? ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility") show the performance variation. We see that temperature-induced and top\_p-induced fluctuations not only affect performance estimates but also introduce substantial variability in performance itself, which can lead to unfair comparisons when evaluating the same model across different temperatures.

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/x6.png)Figure 6: Accuracies vary significantly across temperature values. Across nine different models and three datasets, we observe consistently large variations in performance (upto 15%) induced by changing the temperature. Results were obtained by varying the temperature from 0 to 1 in increments of 0.1, while holding top\_p constant at 0.9.Report issue for preceding element![Refer to caption](https://arxiv.org/html/x7.png)Figure 7: Accuracies vary significantly across top\_p values. Across nine different models and three datasets, we observe consistently large variations in performance (upto 8%) induced by changing the top\_p value. Results were obtained by varying top\_p from 0 to 1 in increments of 0.1, while holding the temperature constant at 0.8.Report issue for preceding element

Takeaway 4  Temperature and top\_p can introduce substantial performance variation—especially on small benchmarks—and should be set to each model’s optimal values to ensure fair and stable evaluation.Report issue for preceding element

### 3.3 Variance from Hardware and Software Factors

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/x8.png)(a) AIME24. Significant differences are observed in model performance across compute clusters.Report issue for preceding element

![Refer to caption](https://arxiv.org/html/x9.png)(b) AMC23. Similar variability is seen across hardware in AMC23 results.Report issue for preceding element

Figure 8: Performance variation across compute clusters. Accuracy differences emerge when the same models are evaluated across compute clusters for both AIME24 and AMC23 datasets—these large differences in performance also persist when evaluating 7B models.Report issue for preceding element

Performance can also vary due to non-obvious factors like hardware and evaluation framework—yet this is rarely acknowledged. Models are often tested on heterogeneous systems and evaluated using different toolchains.For example, S-1.1 (Muennighoff et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib78 "")) uses lm-evaluation-harness(Gao et al., [2024b](https://arxiv.org/html/2504.07086v1#bib.bib31 "")), the OpenRS model suite uses lighteval(Fourrier et al., [2023](https://arxiv.org/html/2504.07086v1#bib.bib29 "")), and II-1.5B-Preview uses evalscope( [Alibaba ModelScope Community,](https://arxiv.org/html/2504.07086v1#bib.bib5 "")) for evaluation.

Report issue for preceding element

Hardware Variation.
We evaluated the same model across five different compute clusters, each with varying GPU types and memory configurations. As shown in Figure [8](https://arxiv.org/html/2504.07086v1#S3.F8 "Figure 8 ‣ 3.3 Variance from Hardware and Software Factors ‣ 3 Exploring the Design Space of Reasoning: What Matters Most? ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility"), performance varied by up to 8% for OpenRS-1.5B and 6% for DeepSeek-R1-Distill-7B on AIME’24, with similar trends observed on AMC’23. While it is known that inference engines such as vLLM can be sensitive to hardware differences (vLLM Contributors, [2024](https://arxiv.org/html/2504.07086v1#bib.bib107 ""))—and that low-level optimizations in PyTorch or CUDA (PyTorch Contributors, [2024](https://arxiv.org/html/2504.07086v1#bib.bib90 "")) may introduce non-determinism—our results demonstrate that these effects can measurably impact benchmark accuracy, even when averaging over multiple seeds.

Report issue for preceding element

Evaluation across different Python frameworks.
Evaluation results can vary based on the framework used, due to differences in prompt templates, inference engines (e.g., vLLM (Kwon et al., [2023](https://arxiv.org/html/2504.07086v1#bib.bib52 ""))), and response extraction strategies (e.g., MathVerify). For example: lighteval is used by OpenRS (Dang & Ngo, [2025](https://arxiv.org/html/2504.07086v1#bib.bib20 "")), evalchemy(Guha et al., [2024](https://arxiv.org/html/2504.07086v1#bib.bib35 "")) is used by models like OpenThinker and Bespoke-Stratos, other frameworks include lm-evaluation-harness(Gao et al., [2024b](https://arxiv.org/html/2504.07086v1#bib.bib31 "")) and evalscope( [Alibaba ModelScope Community,](https://arxiv.org/html/2504.07086v1#bib.bib5 "")).

Report issue for preceding element

To assess this impact, we compare lighteval and evalchemy, keeping all other variables fixed: model, dataset, hardware, decoding parameters, and random seeds (3 per model).
For a fair comparison, we evaluated two models, DeepSeek-R1-Distill-1.5B and S1.1-7B, at their default temperature and top\_p parameter values on a single GPU. We present results averaged over three seeds for higher robustness. As shown in Table [2](https://arxiv.org/html/2504.07086v1#S3.T2 "Table 2 ‣ 3.3 Variance from Hardware and Software Factors ‣ 3 Exploring the Design Space of Reasoning: What Matters Most? ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility"), framework-induced differences are generally small (1–2pp) but can still affect model rankings in tightly clustered scenarios.

Report issue for preceding element

| Model | lighteval | evalchemy |
| --- | --- | --- |
| R1-Distill-1.5B | 26.6 | 26.6 |
| S1.1-7B | 22.2 | 17.7 |

Table 2: AIME24 across frameworks.Report issue for preceding element

Overall, our findings underscore that significant performance variations can arise solely from differences in hardware and software configurations, emphasizing the need to standardize for reliable evaluations.

Report issue for preceding element

Takeaway 5  Re-running the exact same experimental configurations across compute clusters and evaluation frameworks yields notably different results.Report issue for preceding element

### 3.4 Effect of Prompt Format and Context Length

Report issue for preceding element![Refer to caption](https://arxiv.org/html/x10.png)Figure 9: Models are extremely sensitive to output token lengths. We sweep across different max\_new\_tokens (number of tokens that models are allowed to generate) for DeepScaleR-1.5B and DeepSeek-R1-Distill-1.5B/7B on three datasets and find that they are heavily sensitive to output length limits, with premature truncation degrading the performance.Report issue for preceding element

Maximum Output Tokens. Figure [9](https://arxiv.org/html/2504.07086v1#S3.F9 "Figure 9 ‣ 3.4 Effect of Prompt Format and Context Length ‣ 3 Exploring the Design Space of Reasoning: What Matters Most? ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility") shows that reducing max\_new\_tokens harms performance—especially on long-form problems. This sensitivity varies by model and dataset. Although reducing this setting lowers cost, it may induce premature stopping, leading to incorrect answers.

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/x11.png)Figure 10: Using no prompt templates yields worse performance. We compare Pass@1 scores across three prompt formats: (1) math-specific prompt with chat template, (2) default chat template only, and (3) no template. Instruction-tuned models perform best with structured prompts and templates; omitting templates leads to consistent performance drops.Report issue for preceding element

Prompt Format.
Prompt formatting has a measurable impact on accuracy. As shown in Figure [10](https://arxiv.org/html/2504.07086v1#S3.F10 "Figure 10 ‣ 3.4 Effect of Prompt Format and Context Length ‣ 3 Exploring the Design Space of Reasoning: What Matters Most? ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility"), models perform best when using math-specific prompts and their native chat templates. Omitting templates leads to performance drops, particularly for instruction-tuned models. We compare accuracy under three different prompt settings (see Table [5](https://arxiv.org/html/2504.07086v1#A1.T5 "Table 5 ‣ A.3 Prompt Variants and Template Settings ‣ Appendix A Appendix ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility")): (1) a math-specific prompt formatted using the model’s chat template, (2) only the model’s chat template with no additional prompt, and (3) no template at all, i.e., the question without any special tokens or instructions. Interestingly, while base models like Qwen2.5-Math may benefit from prompt-free setups (Liu et al., [2025b](https://arxiv.org/html/2504.07086v1#bib.bib65 "")), instruction-tuned models rely heavily on format alignment.
Thus, maintaining consistent and format-aware prompting is essential for maximizing instruction-tuned model performance.

Report issue for preceding element

Takeaway 6  It is critical to use large generation context lengths to avoid output truncation which can degrade performance; further, using correct prompt formats and chat templates is important for extracting best model performance.Report issue for preceding element

## 4 Way Forward: Standardization in Evaluations

Report issue for preceding element

In this section, we standardize evaluation frameworks, propose best practices, and comprehensively evaluate existing methods.

Report issue for preceding element

### 4.1 Recommendations: Which practices to adopt?

Report issue for preceding element

We propose a set of best practices informed by our experiments and guided with current research insights:

Report issue for preceding element

- •


Hardware and Software Stack Standardization: To promote reproducibility and facilitate future work, we release all code within a Docker container, along with step-by-step instructions for running experiments on Runpod’s publicly accessible, on-demand GPU instances. This setup allows any researcher to replicate and extend our results under identical conditions.

Report issue for preceding element

- •


Variance Estimates: For small benchmarks (e.g., AIME’24), run evaluations with at least ten random seeds. Report the mean and standard deviation to quantify uncertainty and assess the statistical significance of performance differences.

Report issue for preceding element

- •


Model-Specific Hyperparameter Optimization: Tune hyperparameters (such as temperature and top\_p) separately for each model, then fix them across tasks to ensure consistency and fair comparisons.

Report issue for preceding element

- •


Context Length and Prompt Template Selection: Ensure the context length is sufficiently large—especially for models with long reasoning chains—to avoid premature truncation and under-reported accuracy. For instruction-tuned models, always use the appropriate chat template to match the expected input format.

Report issue for preceding element

- •


Robust Answer Matching: We strongly recommend using a resilient answer extraction pipeline that handles parsing issues and evaluates expression equivalence, rather than relying on exact string matching. This reduces the likelihood of spurious gains from formatting artifacts.

Report issue for preceding element

- •


Transparent Evaluation Protocols: We recommend to release code, prompts, and model outputs, and clearly document the evaluation stack. Report uncertainties (e.g., via standard deviations) and include both quantitative and qualitative analyses to enable thorough and reproducible comparisons.

Report issue for preceding element


### 4.2 Standardization Procedure

Report issue for preceding element

We adopt a largely consistent experimental setup with prior work, with the key difference being our use of publicly accessible cloud instances from Runpod222 [https://www.runpod.io/pricing](https://www.runpod.io/pricing ""). Each instance is equipped with a single A100 PCIe GPU, 8 vCPUs, and 128 GB of RAM. We evaluate all models listed in Table [3](https://arxiv.org/html/2504.07086v1#S4.T3 "Table 3 ‣ 4.3 A Sober Look: Results ‣ 4 Way Forward: Standardization in Evaluations ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility") across six benchmarks: AIME’24 ( [AI-MO,](https://arxiv.org/html/2504.07086v1#bib.bib3 "")), AIME’25 (Lin, [2025](https://arxiv.org/html/2504.07086v1#bib.bib58 "")), AMC’23 (Knovel Engineering, [2025](https://arxiv.org/html/2504.07086v1#bib.bib51 "")), MATH500 (HuggingFaceH4, [2024](https://arxiv.org/html/2504.07086v1#bib.bib42 "")), Minerva (Lewkowycz et al., [2022](https://arxiv.org/html/2504.07086v1#bib.bib53 "")), and OlympiadBench (He et al., [2024](https://arxiv.org/html/2504.07086v1#bib.bib36 "")). All experiments are conducted using the LightEval framework (Fourrier et al., [2023](https://arxiv.org/html/2504.07086v1#bib.bib29 "")) (0.8.1) with a vLLM backend, repeated across ten random seeds for AIME’24, AIME’25, AMC’23 and three random seeds for the rest. Depending on the base model architecture, we set the maximum number of new tokens (e.g., 4096 for QwenMath-based models), apply optimal hyperparameters, and use the appropriate chat template. LightEval’s LaTeX-based answer extraction and evaluation pipeline ensures reliable and consistent result parsing and correctness matching, similar to math-verify.

Report issue for preceding element

### 4.3 A Sober Look: Results

Report issue for preceding element

| Model | AIME’24 | AIME’25 | AMC’23 | MATH500 | Minerva | Olympiad |
| Based on: Deepseek R1 Distill Qwen 1.5B (RL) |
| R1-Distill (DeepSeek-AI, [2025](https://arxiv.org/html/2504.07086v1#bib.bib23 "")) | 28.7±plus-or-minus\\pm±4.8 | 22.3±plus-or-minus\\pm±5.2 | 71.5±plus-or-minus\\pm±3.9 | 84.9±plus-or-minus\\pm±0.3 | 30.5±plus-or-minus\\pm±1.0 | 52.4±plus-or-minus\\pm±0.4 |
| L1-Exact (Aggarwal & Welleck, [2025](https://arxiv.org/html/2504.07086v1#bib.bib2 "")) | 24.4±plus-or-minus\\pm±3.3 | 22.3±plus-or-minus\\pm±4.2 | 70.5±plus-or-minus\\pm±3.7 | 86.6±plus-or-minus\\pm±0.8 | 31.5±plus-or-minus\\pm±1.7 | 52.5±plus-or-minus\\pm±1.3 |
| L1-Max (Aggarwal & Welleck, [2025](https://arxiv.org/html/2504.07086v1#bib.bib2 "")) | 27.7±plus-or-minus\\pm±4.2 | 21.0±plus-or-minus\\pm±5.0 | 73.2±plus-or-minus\\pm±6.0 | 84.7±plus-or-minus\\pm±0.1 | 33.3±plus-or-minus\\pm±0.9 | 52.3±plus-or-minus\\pm±0.6 |
| Open-RS1 (Dang & Ngo, [2025](https://arxiv.org/html/2504.07086v1#bib.bib20 "")) | 28.9±plus-or-minus\\pm±6.0 | 21.3±plus-or-minus\\pm±4.2 | 75.0±plus-or-minus\\pm±3.3 | 85.1±plus-or-minus\\pm±0.8 | 30.4±plus-or-minus\\pm±0.2 | 53.2±plus-or-minus\\pm±1.9 |
| Open-RS2 (Dang & Ngo, [2025](https://arxiv.org/html/2504.07086v1#bib.bib20 "")) | 31.3±plus-or-minus\\pm±7.7 | 22.7±plus-or-minus\\pm±5.6 | 73.0±plus-or-minus\\pm±5.7 | 84.1±plus-or-minus\\pm±0.2 | 29.2±plus-or-minus\\pm±1.1 | 53.7±plus-or-minus\\pm±0.6 |
| Open-RS3 (Dang & Ngo, [2025](https://arxiv.org/html/2504.07086v1#bib.bib20 "")) | 29.7±plus-or-minus\\pm±4.6 | 24.7±plus-or-minus\\pm±6.5 | 69.2±plus-or-minus\\pm±5.5 | 84.2±plus-or-minus\\pm±1.1 | 28.6±plus-or-minus\\pm±2.3 | 51.8±plus-or-minus\\pm±0.8 |
| STILL-3 (Min et al., [2024](https://arxiv.org/html/2504.07086v1#bib.bib76 "")) | 34.7±plus-or-minus\\pm±5.5 | 24.0±plus-or-minus\\pm±6.4 | 72.5±plus-or-minus\\pm±5.4 | 86.6±plus-or-minus\\pm±1.9 | 30.0±plus-or-minus\\pm±0.6 | 53.9±plus-or-minus\\pm±1.5 |
| II-Thought (Intelligent Internet, [2025](https://arxiv.org/html/2504.07086v1#bib.bib44 "")) | 32.0±plus-or-minus\\pm±5.9 | 24.0±plus-or-minus\\pm±4.1 | 79.5±plus-or-minus\\pm±5.1 | 86.6±plus-or-minus\\pm±0.6 | 31.7±plus-or-minus\\pm±0.6 | 54.9±plus-or-minus\\pm±0.4 |
| FastCuRL (Song et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib99 "")) | 36.3±plus-or-minus\\pm±4.3 | 27.0±plus-or-minus\\pm±3.7 | 78.8±plus-or-minus\\pm±4.1 | 87.9±plus-or-minus\\pm±1.2 | 30.8±plus-or-minus\\pm±1.4 | 56.5±plus-or-minus\\pm±0.6 |
| DeepScaleR (Luo et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib67 "")) | 37.0±plus-or-minus\\pm±6.6 | 30.3±plus-or-minus\\pm±4.3 | 76.2±plus-or-minus\\pm±4.6 | 87.8±plus-or-minus\\pm±1.0 | 31.0±plus-or-minus\\pm±1.5 | 55.5±plus-or-minus\\pm±1.1 |
| Based on: Deepseek R1 Distill Qwen 7B (RL) |
| R1-Distill (DeepSeek-AI, [2025](https://arxiv.org/html/2504.07086v1#bib.bib23 "")) | 52.3±plus-or-minus\\pm±6.3 | 39.0±plus-or-minus\\pm±5.9 | 91.5±plus-or-minus\\pm±2.7 | 94.1±plus-or-minus\\pm±0.3 | 40.1±plus-or-minus\\pm±0.4 | 67.3±plus-or-minus\\pm±0.1 |
| Light-R1 (Wen et al., [2025a](https://arxiv.org/html/2504.07086v1#bib.bib109 "")) | 53.0±plus-or-minus\\pm±4.8 | 41.0±plus-or-minus\\pm±3.5 | 90.0±plus-or-minus\\pm±3.1 | 93.5±plus-or-minus\\pm±0.5 | 41.3±plus-or-minus\\pm±1.3 | 68.0±plus-or-minus\\pm±1.2 |
| Based on: Qwen2.5 Math 1.5B (RL) |
| Math (Base) (Yang et al., [2024b](https://arxiv.org/html/2504.07086v1#bib.bib115 "")) | 11.3±plus-or-minus\\pm±3.6 | 5.7±plus-or-minus\\pm±2.7 | 44.0±plus-or-minus\\pm±4.9 | 51.7±plus-or-minus\\pm±5.5 | 11.3±plus-or-minus\\pm±2.2 | 26.0±plus-or-minus\\pm±0.6 |
| Oat-Zero (Liu et al., [2025a](https://arxiv.org/html/2504.07086v1#bib.bib64 "")) | 16.0±plus-or-minus\\pm±3.2 | 6.7±plus-or-minus\\pm±3.4 | 52.5±plus-or-minus\\pm±2.9 | 73.5±plus-or-minus\\pm±1.7 | 26.3±plus-or-minus\\pm±0.8 | 37.2±plus-or-minus\\pm±1.3 |
| Math (Instruct) (Yang et al., [2024b](https://arxiv.org/html/2504.07086v1#bib.bib115 "")) | 12.0±plus-or-minus\\pm±1.7 | 11.7±plus-or-minus\\pm±5.7 | 54.8±plus-or-minus\\pm±5.3 | 74.7±plus-or-minus\\pm±0.5 | 26.7±plus-or-minus\\pm±1.8 | 37.9±plus-or-minus\\pm±0.2 |
| Based on: Qwen2.5 Math 7B (RL) |
| Math (Base) (Yang et al., [2024b](https://arxiv.org/html/2504.07086v1#bib.bib115 "")) | 20.7±plus-or-minus\\pm±3.8 | 8.7±plus-or-minus\\pm±3.9 | 56.2±plus-or-minus\\pm±5.7 | 64.3±plus-or-minus\\pm±0.5 | 17.3±plus-or-minus\\pm±1.9 | 29.0±plus-or-minus\\pm±0.5 |
| SimpleRL-Zoo (Zeng et al., [2025b](https://arxiv.org/html/2504.07086v1#bib.bib121 "")) | 22.7±plus-or-minus\\pm±5.2 | 10.7±plus-or-minus\\pm±3.4 | 62.2±plus-or-minus\\pm±3.6 | 76.9±plus-or-minus\\pm±1.8 | 30.1±plus-or-minus\\pm±2.8 | 39.3±plus-or-minus\\pm±0.6 |
| LIMR (Li et al., [2025a](https://arxiv.org/html/2504.07086v1#bib.bib54 "")) | 30.7±plus-or-minus\\pm±3.2 | 7.8±plus-or-minus\\pm±3.3 | 62.2±plus-or-minus\\pm±3.4 | 76.5±plus-or-minus\\pm±0.4 | 34.9±plus-or-minus\\pm±1.3 | 39.3±plus-or-minus\\pm±0.9 |
| Oat-Zero (Liu et al., [2025a](https://arxiv.org/html/2504.07086v1#bib.bib64 "")) | 28.0±plus-or-minus\\pm±3.1 | 8.8±plus-or-minus\\pm±2.5 | 66.2±plus-or-minus\\pm±3.6 | 79.4±plus-or-minus\\pm±0.3 | 34.4±plus-or-minus\\pm±1.4 | 43.8±plus-or-minus\\pm±1.1 |
| Math (Instruct) (Yang et al., [2024b](https://arxiv.org/html/2504.07086v1#bib.bib115 "")) | 15.7±plus-or-minus\\pm±3.9 | 10.7±plus-or-minus\\pm±3.8 | 67.0±plus-or-minus\\pm±3.9 | 82.9±plus-or-minus\\pm±0.1 | 35.0±plus-or-minus\\pm±0.6 | 41.3±plus-or-minus\\pm±0.9 |
| Based on: Qwen2.5 1.5B (RL) |
| Qwen (Base) (Yang et al., [2024a](https://arxiv.org/html/2504.07086v1#bib.bib114 "")) | 0.0±plus-or-minus\\pm±0.0 | 0.0±plus-or-minus\\pm±0.0 | 2.5±plus-or-minus\\pm±2.5 | 3.3±plus-or-minus\\pm±1.5 | 1.8±plus-or-minus\\pm±0.4 | 1.5±plus-or-minus\\pm±0.5 |
| SimpleRL-Zoo (Zeng et al., [2025b](https://arxiv.org/html/2504.07086v1#bib.bib121 "")) | 0.3±plus-or-minus\\pm±1.1 | 0.3±plus-or-minus\\pm±1.1 | 13.2±plus-or-minus\\pm±4.7 | 12.0±plus-or-minus\\pm±6.5 | 4.0±plus-or-minus\\pm±2.4 | 4.2±plus-or-minus\\pm±2.0 |
| Qwen (Instruct) (Yang et al., [2024a](https://arxiv.org/html/2504.07086v1#bib.bib114 "")) | 1.3±plus-or-minus\\pm±1.7 | 0.7±plus-or-minus\\pm±1.4 | 26.2±plus-or-minus\\pm±4.8 | 57.5±plus-or-minus\\pm±1.1 | 19.4±plus-or-minus\\pm±1.3 | 20.3±plus-or-minus\\pm±1.1 |
| Based on: Qwen2.5 7B (RL) |
| Qwen (Base) (Yang et al., [2024a](https://arxiv.org/html/2504.07086v1#bib.bib114 "")) | 3.3±plus-or-minus\\pm±3.3 | 0.0±plus-or-minus\\pm±0.0 | 30.0±plus-or-minus\\pm±9.0 | 64.6±plus-or-minus\\pm±1.0 | 25.7±plus-or-minus\\pm±0.9 | 30.1±plus-or-minus\\pm±1.2 |
| SimpleRL-Zoo (Zeng et al., [2025b](https://arxiv.org/html/2504.07086v1#bib.bib121 "")) | 14.0±plus-or-minus\\pm±2.1 | 4.3±plus-or-minus\\pm±2.7 | 58.0±plus-or-minus\\pm±1.6 | 77.9±plus-or-minus\\pm±0.8 | 33.0±plus-or-minus\\pm±0.2 | 39.0±plus-or-minus\\pm±0.1 |
| Open Reasoner Zero (Hu et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib40 "")) | 19.7±plus-or-minus\\pm±2.9 | 15.7±plus-or-minus\\pm±2.7 | 59.5±plus-or-minus\\pm±4.5 | 83.9±plus-or-minus\\pm±1.1 | 31.6±plus-or-minus\\pm±1.3 | 47.6±plus-or-minus\\pm±1.7 |
| Qwen (Instruct) | 12.3±plus-or-minus\\pm±3.2 | 7.3±plus-or-minus\\pm±3.4 | 52.8±plus-or-minus\\pm±4.8 | 77.1±plus-or-minus\\pm±1.2 | 34.9±plus-or-minus\\pm±1.0 | 38.7±plus-or-minus\\pm±1.0 |
| Based on: Qwen2.5 7B (SFT) |
| Qwen (Instruct) (Yang et al., [2024a](https://arxiv.org/html/2504.07086v1#bib.bib114 "")) | 12.3±plus-or-minus\\pm±3.2 | 7.3±plus-or-minus\\pm±3.4 | 52.8±plus-or-minus\\pm±4.8 | 77.1±plus-or-minus\\pm±1.2 | 34.9±plus-or-minus\\pm±1.0 | 38.7±plus-or-minus\\pm±1.0 |
| Eurus2 Prime (Cui et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib19 "")) | 17.8±plus-or-minus\\pm±2.2 | 14.0±plus-or-minus\\pm±1.7 | 63.0±plus-or-minus\\pm±3.9 | 80.1±plus-or-minus\\pm±0.1 | 37.5±plus-or-minus\\pm±1.0 | 43.9±plus-or-minus\\pm±0.3 |
| s1.1 (Muennighoff et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib78 "")) | 19.0±plus-or-minus\\pm±3.2 | 21.0±plus-or-minus\\pm±5.5 | 59.5±plus-or-minus\\pm±3.7 | 80.8±plus-or-minus\\pm±0.6 | 37.5±plus-or-minus\\pm±1.1 | 48.2±plus-or-minus\\pm±1.4 |
| Bespoke Stratos (Bespoke Labs, [2024](https://arxiv.org/html/2504.07086v1#bib.bib10 "")) | 20.3±plus-or-minus\\pm±4.3 | 18.0±plus-or-minus\\pm±4.8 | 60.2±plus-or-minus\\pm±4.9 | 84.7±plus-or-minus\\pm±0.5 | 39.1±plus-or-minus\\pm±1.3 | 51.9±plus-or-minus\\pm±1.1 |
| OpenThinker (Team, [2025](https://arxiv.org/html/2504.07086v1#bib.bib102 "")) | 30.5±plus-or-minus\\pm±6.2 | 26.0±plus-or-minus\\pm±4.4 | 71.4±plus-or-minus\\pm±3.9 | 88.3±plus-or-minus\\pm±1.4 | 37.9±plus-or-minus\\pm±3.8 | 55.6±plus-or-minus\\pm±1.4 |
| OpenR1 (Face, [2025](https://arxiv.org/html/2504.07086v1#bib.bib27 "")) | 48.3±plus-or-minus\\pm±8.9 | 35.5±plus-or-minus\\pm±4.2 | 86.0±plus-or-minus\\pm±4.5 | – | – | – |
| OpenThinker2 (Team, [2025](https://arxiv.org/html/2504.07086v1#bib.bib102 "")) | 53.0±plus-or-minus\\pm±4.6 | 41.0±plus-or-minus\\pm±5.0 | 87.0±plus-or-minus\\pm±3.5 | 81.6±plus-or-minus\\pm±0.7 | 33.9±plus-or-minus\\pm±0.2 | 46.9±plus-or-minus\\pm±1.3 |

Table 3: A Standardized and Sober Compilation of LM-Reasoning Results. We report Pass@1 accuracy (mean ±plus-or-minus\\pm± std) of all models across six math reasoning benchmarks under a standardized evaluation setup—results are averaged over ten seeds for AIME and AMC, and three seeds for the rest, using the LightEval framework with best hyperparameters tuned per method, 32,768 context lengths for all except 4,096 for Math models, and appropriate prompt templates. RL- and SFT-based variants are evaluated relative to their respective base or instruction-tuned models. Main takeaways—(1) RL-trained methods do not yield meaningful performance gains, (2) SFT on reasoning traces yields significant generalization.Report issue for preceding element

We present experimental results in Table [3](https://arxiv.org/html/2504.07086v1#S4.T3 "Table 3 ‣ 4.3 A Sober Look: Results ‣ 4 Way Forward: Standardization in Evaluations ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility"), and analyze different aspects of the results.

Report issue for preceding element

RL-training on R1-Distill We evaluated several reinforcement learning (RL) approaches (e.g., GRPO) using the DeepSeek R1-Distill-1.5B model. We first observe that none of the L1 models (Aggarwal & Welleck, [2025](https://arxiv.org/html/2504.07086v1#bib.bib2 "")) outperformed the original DeepSeek R1-Distill baseline — an expected outcome given that L1 training prioritized smaller output length over accuracy. OpenRS (Dang & Ngo, [2025](https://arxiv.org/html/2504.07086v1#bib.bib20 "")) reported strong gains (10–15%) on AIME, AMC, and OlympiadBench. However, our replication showed no statistically significant improvements over the R1 - Distill baseline. Same case held for Still-3 and Light-R1 model, which showed no significant improvement over the R1-Distill baseline. II-Thought and FastCurl yield modest improvements across benchmarks, especially over AIME’24 but the observed gains did not carry over significantly to AIME’25 indicating overfitting to existing benchmarks. Only DeepscaleR demonstrated robust, significant improvements across benchmarks.

Report issue for preceding element

Takeaway 1  Most RL-trained variants of the DeepSeek R1-Distill model do not yield meaningful performance improvements (except DeepscaleR), suggesting that a reliable and scalable RL training recipes are still lacking.Report issue for preceding element

RL Training on Qwen2.5 Math and Base Models: We next analyze RL training applied to the Qwen2.5 Base and Qwen2.5 Math Base models, a trend trying to replicate gains by Deepseek-R1 Zero. Unlike the R1-Distill results, RL training with Oat-Zero, LIMR, and SimpleRL-Zoo consistently produced statistically significant gains over the base model, especially across Math500, Minerva and OlympiadBench benchmarks. This indicates that RL-based approaches can indeed offer substantial improvements given a base model instead of a distilled R1 model. However, these gains remained smaller than those achieved via instruction tuning in the original Qwen papers, suggesting that instruction tuning alone may be sufficient to far surpass current gains from RL methods in this setting. We also observed that the improvements on AIME’24 were also significant, but did not carry over to AIME’25 indicating a troubling overfitting trend. Notably, Open Reasoner-Zero-7B was the only RL-trained model to consistently outperform the instruct-tuned baseline by large margins across all benchmarks.

Report issue for preceding element

Takeaway 2  While RL-trained methods can often substantially improve base model performance, instruction tuning remains superior (except Open Reasoner Zero), suggesting again that a reliable and scalable RL training recipes are still lacking.Report issue for preceding element

Effectiveness of Supervised Finetuning. We assessed supervised finetuning methods like s1.1, Eurus2 Prime, Bespoke Stratos, OpenR1 and OpenThinker models, which further refine instruction-tuned models using reasoning traces. Supervised methods consistently outperformed the instruct-tuned baseline across all benchmarks (even Minerva) and generalized comparatively well to AIME’25. The performance improvements from OpenThinker were especially notable. These results underscore the maturity and effectiveness of SFT when training recipes are scaled to large datasets.

Report issue for preceding element

Takeaway 3  Supervised finetuning on reasoning traces from larger models yields significant, generalizable gains across benchmarks with progress over time successfully replicated — highlighting its robustness and maturity as a training paradigm.Report issue for preceding element

Overfitting and Generalization We now examine the overfitting by comparing performance on AIME’24 versus the more challenging AIME’25. RL-trained models showed a pronounced performance drop between the two, indicating overfitting to the training distribution. In contrast, supervised fine-tuning (SFT) models maintained consistent improvements, suggesting better generalization. Openthinker2 showed significant degradation compared to Openthinker across benchmarks not provided in their blogpost, indicating overfitting via data-curation. This highlights a gap in current evaluation protocols, and a need to assess out-of-distribution generalization for reasoning models.

Report issue for preceding element

Takeaway 4  Current RL-based approaches are very susceptible to overfitting, emphasizing the need for more rigorous out-of-distribution benchmarks. By comparison, SFT models exhibit stronger generalization and resilience.Report issue for preceding element

### 4.4 Do Discovered Phenomena Replicate? A Detailed Analysis.

Report issue for preceding element

We further investigate two recently noted phenomena to see if they replicate in our experiments: (1) how response length correlates with performance, and (2) the decline in response diversity following reasoning-focused training.

Report issue for preceding element

#### 4.4.1 Are Incorrect Responses Longer?

Report issue for preceding element![Refer to caption](https://arxiv.org/html/x12.png)Figure 11: Response Length vs. Accuracy. Histogram of correct vs. incorrect responses by response length, averaged over random seeds across AIME24, AIME25, AMC23, MATH500, Minerva and OlympiadBench benchmarks. Longer outputs tend to be more error-prone, even in complete responses not close to the maximum sequence length.Report issue for preceding element

Recent research (Wang et al., [2025](https://arxiv.org/html/2504.07086v1#bib.bib108 "")) suggests that incorrect answers often have disproportionately long reasoning chains. We first verify whether this finding holds in our setting, and then we explore possible explanations behind the observed variations.

Report issue for preceding element

Do longer responses indicate a higher likelihood of an incorrect answer? We compare the distribution of response lengths for correct and incorrect answers across 6 datasets (AIME24, AIME25, AMC23, MATH500, Minerva and OlympiadBench) averaged across random seeds for each model. Figure [11](https://arxiv.org/html/2504.07086v1#S4.F11 "Figure 11 ‣ 4.4.1 Are Incorrect Responses Longer? ‣ 4.4 Do Discovered Phenomena Replicate? A Detailed Analysis. ‣ 4 Way Forward: Standardization in Evaluations ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility") shows histograms of the average number of responses per seed, binned by response length. A clear trend emerges: shorter responses are significantly more likely to be correct, while longer responses become progressively more error-prone. This pattern is consistent across all seeds and is especially pronounced for responses exceeding 10,000 tokens. We now address two questions:

Report issue for preceding element

##### Q1. Does this pattern hold for both RL- and SFT-trained models?

Report issue for preceding element

Yes. We find the trend is consistent across both RL- and SFT-trained models (additional figures provided in Appendix figures [17](https://arxiv.org/html/2504.07086v1#A1.F17 "Figure 17 ‣ A.5 Response Length vs. Accuracy — Per-Model Breakdown ‣ Appendix A Appendix ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility") and  [18](https://arxiv.org/html/2504.07086v1#A1.F18 "Figure 18 ‣ A.5 Response Length vs. Accuracy — Per-Model Breakdown ‣ Appendix A Appendix ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility") ). We consistently observe that the effect is more pronounced in RL-trained models (displayed on the left) than in SFT-trained models (displayed on the right). As detailed in the Appendix, both the Qwen 2.5 Math base exhibit a slight shift in length, though this shift is notably more evident in R1-distill and subsequent RL-trained models.

Report issue for preceding element

##### Q2. Is this primarily because of truncated or incomplete responses?

Report issue for preceding element

Although responses nearing the 32,000-token limit are almost always incorrect (due to limited context-length), this trend persists even for complete responses which are shorter– Longer responses are associated with a higher likelihood of being incorrect.

Report issue for preceding element

Takeaway 5  Longer responses correlate with a greater chance of error, response length is a practical heuristic for consensus@k, identifying low-confidence or failed generations.Report issue for preceding element

#### 4.4.2 Is There Diversity Collapse in Reasoning Training?

Report issue for preceding element

|  |  | AIME’24 | AIME’25 | AMC’23 |
| --- | --- | --- | --- | --- |
| Model | Baseline | δ⁢@⁢1𝛿@1\\delta@1italic\_δ @ 1 | δ⁢@⁢5𝛿@5\\delta@5italic\_δ @ 5 | δ⁢@⁢10𝛿@10\\delta@10italic\_δ @ 10 | δ⁢@⁢1𝛿@1\\delta@1italic\_δ @ 1 | δ⁢@⁢5𝛿@5\\delta@5italic\_δ @ 5 | δ⁢@⁢10𝛿@10\\delta@10italic\_δ @ 10 | δ⁢@⁢1𝛿@1\\delta@1italic\_δ @ 1 | δ⁢@⁢5𝛿@5\\delta@5italic\_δ @ 5 | δ⁢@⁢10𝛿@10\\delta@10italic\_δ @ 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Open-RS3 | R1-Distill | +1.51.5{\\color\[rgb\]{0,0.5,0}\\definecolor\[named\]{pgfstrokecolor}{rgb}{0,0.5,0}+1.5}\+ 1.5 | -0.6 | +1.5 | -1.0 | +0.4 | +1.4 | -0.9 | -0.2 | +0.4 |
| DeepScaleR | R1-Distill | +9.09.0{\\color\[rgb\]{0,0.5,0}\\definecolor\[named\]{pgfstrokecolor}{rgb}{0,0.5,0}+9.0}\+ 9.0 | +0.6 | +0.2 | +4.44.4{\\color\[rgb\]{0,0.5,0}\\definecolor\[named\]{pgfstrokecolor}{rgb}{0,0.5,0}+4.4}\+ 4.4 | +3.6 | +2.2 | +6.16.1{\\color\[rgb\]{0,0.5,0}\\definecolor\[named\]{pgfstrokecolor}{rgb}{0,0.5,0}+6.1}\+ 6.1 | -1.8 | -1.7 |
| S1.1-7B | Qwen-Instruct | +5.75.7{\\color\[rgb\]{0,0.5,0}\\definecolor\[named\]{pgfstrokecolor}{rgb}{0,0.5,0}+5.7}\+ 5.7 | +10.9 | +13.5 | +11.911.9{\\color\[rgb\]{0,0.5,0}\\definecolor\[named\]{pgfstrokecolor}{rgb}{0,0.5,0}+11.9}\+ 11.9 | +10.5 | +10.4 | +5.85.8{\\color\[rgb\]{0,0.5,0}\\definecolor\[named\]{pgfstrokecolor}{rgb}{0,0.5,0}+5.8}\+ 5.8 | +9.6 | +9.7 |
| II-Thought | R1-Distill | +2.52.5{\\color\[rgb\]{0,0.5,0}\\definecolor\[named\]{pgfstrokecolor}{rgb}{0,0.5,0}+2.5}\+ 2.5 | -3.5 | -3.6 | +0.80.8{\\color\[rgb\]{0,0.5,0}\\definecolor\[named\]{pgfstrokecolor}{rgb}{0,0.5,0}+0.8}\+ 0.8 | +0.5 | +1.2 | +6.36.3{\\color\[rgb\]{0,0.5,0}\\definecolor\[named\]{pgfstrokecolor}{rgb}{0,0.5,0}+6.3}\+ 6.3 | +0.7 | +0.2 |

Table 4: RL-trained models do not show a diversity collapse ( [Dang et al.,](https://arxiv.org/html/2504.07086v1#bib.bib21 "")). We report the delta between Pass@k of RL-trained models and their corresponding baselines. Unlike reported in prior work, we observe no significant phenomenon of diversity collapse: δ⁢@⁢5𝛿@5\\delta@5italic\_δ @ 5 and δ⁢@⁢10𝛿@10\\delta@10italic\_δ @ 10 are largely positive, and are negative at similar rates as δ⁢@⁢1𝛿@1\\delta@1italic\_δ @ 1.Report issue for preceding element

[Dang et al.](https://arxiv.org/html/2504.07086v1#bib.bib21 "") has reported a counterintuitive phenomenon in reasoning models: improvements in Pass@1 achieved through supervised fine-tuning or RL can reduce Pass@k performance due to diminished output diversity—a phenomenon termed diversity collapse. Theoretical analyses attribute this collapse to the model concentrating too much probability mass on a single reasoning path, while current decoding strategies fail to recover the lost diversity.

Report issue for preceding element

To examine these claims, we compare the Pass@k performance (for k∈1,5,10𝑘1510k\\in{1,5,10}italic\_k ∈ 1 , 5 , 10) of RL-trained models against their corresponding base models (e.g., DeepSeek-R1-Distill-Qwen-1.5B) across all datasets. Table [4](https://arxiv.org/html/2504.07086v1#S4.T4 "Table 4 ‣ 4.4.2 Is There Diversity Collapse in Reasoning Training? ‣ 4.4 Do Discovered Phenomena Replicate? A Detailed Analysis. ‣ 4 Way Forward: Standardization in Evaluations ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility") shows the delta in Pass@k relative to each method’s base model.

Report issue for preceding element

Findings. We do not observe a consistent diversity collapse. Gains in Pass@1 generally come with improvements in Pass@k, though the magnitude of these gains varies. When Pass@k performance does drop, it does so alongside (rather than independently of) occasional declines in Pass@1, providing no support for the diversity collapse hypothesis.

Report issue for preceding element

Takeaway 6  Standard decoding strategies appear sufficient to capture the model’s full distribution over valid reasoning paths, counter to the diversity collapse hypothesis.Report issue for preceding element

## 5 Conclusion

Report issue for preceding element

Our study shows that much of the perceived progress in LLM-based reasoning, particularly in mathematical benchmarks, rests on unstable and often non-reproducible foundations. We find that minor differences in sampling parameters, prompt formatting, hardware, and software configurations can lead to major shifts in reported performance—casting doubt on many recent empirical claims. Reinforcement learning methods, while promising in theory, offer at best modest gains in practice and are prone to overfitting, especially on small benchmarks like AIME’24. In contrast, supervised finetuning continues to deliver consistent, generalizable improvements across a wide range of benchmarks and model sizes.

Report issue for preceding element

To address these challenges, we advocate for standardized, transparent evaluation protocols. Our open-sourced framework, complete with Dockerized environments, seed-averaged metrics, and robust answer matching, provides reproducible foundations for future research. We hope this work shifts the focus from leaderboard chasing to methodological rigor—ensuring that future claims of progress in reasoning are both meaningful and measurable.

Report issue for preceding element

## Author Contributions

Report issue for preceding element

Andreas, Vishaal and Ameya conceived the project. Andreas and Hardik co-led the experiments, with Vishaal and Ameya advising the experimental design. The manuscript was written by Andreas, Hardik, Vishaal and Ameya. Matthias and Samuel provided helpful feedback and advice throughout the project.

Report issue for preceding element

## Acknowledgments

Report issue for preceding element

The authors would like to thank (in alphabetical order): Matteo Farina, Shyamgopal Karthik, Nikhil Parthasarathy, Shiven Sinha, Joschka Strüber, Thaddäus Wiedemer for helpful feedback on the draft. AH acknowledges funding by the Federal Ministry of Education and Research (BMBF), FKZ: 01IS24079A. HB has received funding from the Digital Europe Programme under grant agreement No 101195233 (OpenEuroLLM). AH, HB and VU thank the International Max Planck Research School for Intelligent Systems (IMPRS-IS) for support.
VU also thanks the European Laboratory for Learning and Intelligent Systems (ELLIS) PhD program for support.
VU was supported by a Google PhD Fellowship in Machine Intelligence. AP and MB acknowledge financial support by the Federal Ministry of Education and Research (BMBF), FKZ: 011524085B and Open Philanthropy Foundation funded by the Good Ventures Foundation. This work was supported by the Digital Europe Programme under grant agreement No 101195233 (OpenEuroLLM).

Report issue for preceding element

## References

Report issue for preceding element

- Agarwal et al. (2021)↑
Rishabh Agarwal, Max Schwarzer, Pablo Samuel Castro, Aaron C Courville, and Marc Bellemare.

Deep reinforcement learning at the edge of the statistical precipice.

_Advances in neural information processing systems_, 34:29304–29320, 2021.

- Aggarwal & Welleck (2025)↑
Pranjal Aggarwal and Sean Welleck.

L1: Controlling how long a reasoning model thinks with reinforcement learning.

_arXiv preprint arXiv:2503.04697_, 2025.

- (3)↑
AI-MO.

AIMO Validation AIME Dataset.

- AI-MO (2024)↑
AI-MO.

AIMO Validation AMC Dataset.

[https://huggingface.co/datasets/AI-MO/aimo-validation-amc](https://huggingface.co/datasets/AI-MO/aimo-validation-amc ""), 2024.

Accessed: 2025-03-29.

- (5)↑
Alibaba ModelScope Community.

Evalscope documentation.

[https://evalscope.readthedocs.io/en/latest/](https://evalscope.readthedocs.io/en/latest/ "").

Accessed: 2025-03-29.

- Andrychowicz et al. (2020)↑
Marcin Andrychowicz, Anton Raichuk, Piotr Stańczyk, Manu Orsini, Sertan Girgin, Raphael Marinier, Léonard Hussenot, Matthieu Geist, Olivier Pietquin, Marcin Michalski, et al.

What matters in on-policy reinforcement learning? a large-scale empirical study.

_arXiv preprint arXiv:2006.05990_, 2020.

- Anthropic (2025)↑
Anthropic.

Claude 3.7 Sonnet System Card, 2025.

URL [https://assets.anthropic.com/m/785e231869ea8b3b/original/claude-3-7-sonnet-system-card.pdf](https://assets.anthropic.com/m/785e231869ea8b3b/original/claude-3-7-sonnet-system-card.pdf "").

Accessed: 2025-03-29.

- Arora et al. (2024)↑
Chetan Arora, Ahnaf Ibn Sayeed, Sherlock Licorish, Fanyu Wang, and Christoph Treude.

Optimizing large language model hyperparameters for code generation.

_arXiv preprint arXiv:2408.10577_, 2024.

- Balduzzi et al. (2018)↑
David Balduzzi, Karl Tuyls, Julien Perolat, and Thore Graepel.

Re-evaluating evaluation.

_Advances in Neural Information Processing Systems_, 31, 2018.

- Bespoke Labs (2024)↑
Bespoke Labs.

Bespoke-stratos-7b.

[https://huggingface.co/bespokelabs/Bespoke-Stratos-7B](https://huggingface.co/bespokelabs/Bespoke-Stratos-7B ""), 2024.

Accessed: 2025-03-29.

- Biderman et al. (2024)↑
Stella Biderman, Hailey Schoelkopf, Lintang Sutawika, Leo Gao, Jonathan Tow, Baber Abbasi, Alham Fikri Aji, Pawan Sasanka Ammanamanchi, Sidney Black, Jordan Clive, et al.

Lessons from the trenches on reproducible evaluation of language models.

_arXiv preprint arXiv:2405.14782_, 2024.

- Bowyer et al. (2025)↑
Sam Bowyer, Laurence Aitchison, and Desi R Ivanova.

Position: Don’t use the CLT in LLM evals with fewer than a few hundred datapoints.

_arXiv preprint arXiv:2503.01747_, 2025.

- Cai (2025)↑
Xin Cai.

One framework to rule them all: Unifying rl-based and rl-free methods in rlhf.

_arXiv preprint arXiv:2503.19523_, 2025.

- Cawley (2011)↑
Gavin C Cawley.

Baseline methods for active learning.

In _Active Learning and Experimental Design workshop In conjunction with AISTATS 2010_, pp.  47–57. JMLR Workshop and Conference Proceedings, 2011.

- Cawley & Talbot (2010)↑
Gavin C Cawley and Nicola LC Talbot.

On over-fitting in model selection and subsequent selection bias in performance evaluation.

_The Journal of Machine Learning Research_, 11:2079–2107, 2010.

- Chan et al. (2019)↑
Stephanie CY Chan, Samuel Fishman, John Canny, Anoop Korattikara, and Sergio Guadarrama.

Measuring the reliability of reinforcement learning algorithms.

_arXiv preprint arXiv:1912.05663_, 2019.

- (17)↑
Liang Chen, Lei Li, Haozhe Zhao, and Yifan Song.

Vinci. r1-v: Reinforcing super generalization ability in vision-language models with less than 3 dollars.

- Colas et al. (2018)↑
Cédric Colas, Olivier Sigaud, and Pierre-Yves Oudeyer.

How many random seeds? statistical power analysis in deep reinforcement learning experiments.

_arXiv preprint arXiv:1806.08295_, 2018.

- Cui et al. (2025)↑
Ganqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, Wendi Li, Bingxiang He, Yuchen Fan, Tianyu Yu, Qixin Xu, Weize Chen, et al.

Process reinforcement through implicit rewards.

_arXiv preprint arXiv:2502.01456_, 2025.

- Dang & Ngo (2025)↑
Quy-Anh Dang and Chris Ngo.

Reinforcement learning for reasoning in small llms: What works and what doesn’t, 2025.

URL [https://arxiv.org/abs/2503.16219](https://arxiv.org/abs/2503.16219 "").

- (21)↑
Xingyu Dang, Christina Baek, J Zico Kolter, and Aditi Raghunathan.

Assessing diversity collapse in reasoning.

In _Scaling Self-Improving Foundation Models without Human Supervision_.

- DeepMind (2025)↑
Google DeepMind.

Gemini 2.5: Our most intelligent ai model, 2025.

URL [https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/ "").

Accessed: 2025-04-07.

- DeepSeek-AI (2025)↑
DeepSeek-AI.

DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning, 2025.

URL [https://arxiv.org/abs/2501.12948](https://arxiv.org/abs/2501.12948 "").

- Dehghani et al. (2021)↑
Mostafa Dehghani, Yi Tay, Alexey A Gritsenko, Zhe Zhao, Neil Houlsby, Fernando Diaz, Donald Metzler, and Oriol Vinyals.

The benchmark lottery.

_arXiv preprint arXiv:2107.07002_, 2021.

- Deng et al. (2025)↑
Yihe Deng, Hritik Bansal, Fan Yin, Nanyun Peng, Wei Wang, and Kai-Wei Chang.

Openvlthinker: An early exploration to complex vision-language reasoning via iterative self-improvement.

_arXiv preprint arXiv:2503.17352_, 2025.

- Dominguez-Olmedo et al. (2024)↑
Ricardo Dominguez-Olmedo, Florian E Dorner, and Moritz Hardt.

Training on the test task confounds evaluation and emergence.

_arXiv preprint arXiv:2407.07890_, 2024.

- Face (2025)↑
Hugging Face.

Open r1: A fully open reproduction of deepseek-r1, January 2025.

URL [https://github.com/huggingface/open-r1](https://github.com/huggingface/open-r1 "").

- Feng et al. (2025)↑
Kaituo Feng, Kaixiong Gong, Bohao Li, Zonghao Guo, Yibing Wang, Tianshuo Peng, Benyou Wang, and Xiangyu Yue.

Video-r1: Reinforcing video reasoning in mllms.

_arXiv preprint arXiv:2503.21776_, 2025.

- Fourrier et al. (2023)↑
Clémentine Fourrier, Nathan Habib, Hynek Kydlíček, Thomas Wolf, and Lewis Tunstall.

LightEval: A lightweight framework for LLM evaluation, 2023.

URL [https://github.com/huggingface/lighteval](https://github.com/huggingface/lighteval "").

- Gao et al. (2024a)↑
Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, and Yi Wu.

On designing effective rl reward at training time for llm reasoning.

_arXiv preprint arXiv:2410.15115_, 2024a.

- Gao et al. (2024b)↑
Leo Gao, Jonathan Tow, Baber Abbasi, Stella Biderman, Sid Black, Anthony DiPofi, Charles Foster, Laurence Golding, Jeffrey Hsu, Alain Le Noac’h, Haonan Li, Kyle McDonell, Niklas Muennighoff, Chris Ociepa, Jason Phang, Laria Reynolds, Hailey Schoelkopf, Aviya Skowron, Lintang Sutawika, Eric Tang, Anish Thite, Ben Wang, Kevin Wang, and Andy Zou.

A framework for few-shot language model evaluation, 07 2024b.

URL [https://zenodo.org/records/12608602](https://zenodo.org/records/12608602 "").

- Ghosh et al. (2024)↑
Adhiraj Ghosh, Sebastian Dziadzio, Ameya Prabhu, Vishaal Udandarao, Samuel Albanie, and Matthias Bethge.

Onebench to test them all: Sample-level benchmarking over open-ended capabilities.

_arXiv preprint arXiv:2412.06745_, 2024.

- Golchin & Surdeanu (2023)↑
Shahriar Golchin and Mihai Surdeanu.

Time travel in llms: Tracing data contamination in large language models.

_arXiv preprint arXiv:2308.08493_, 2023.

- Gorsane et al. (2022)↑
Rihab Gorsane, Omayma Mahjoub, Ruan John de Kock, Roland Dubb, Siddarth Singh, and Arnu Pretorius.

Towards a standardised performance evaluation protocol for cooperative marl.

_Advances in Neural Information Processing Systems_, 35:5510–5521, 2022.

- Guha et al. (2024)↑
Etash Guha, Negin Raoof, Jean Mercat, Ryan Marten, Eric Frankel, Sedrick Keh, Sachin Grover, George Smyrnis, Trung Vu, Jon Saad-Falcon, Caroline Choi, Kushal Arora, Mike Merrill, Yichuan Deng, Ashima Suvarna, Hritik Bansal, Marianna Nezhurina, Yejin Choi, Reinhard Heckel, Seewong Oh, Tatsunori Hashimoto, Jenia Jitsev, Vaishaal Shankar, Alex Dimakis, Mahesh Sathiamoorthy, and Ludwig Schmidt, November 2024.

- He et al. (2024)↑
Chaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Leng Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, Jie Liu, Lei Qi, Zhiyuan Liu, and Maosong Sun.

Olympiadbench: A challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems, 2024.

URL [https://arxiv.org/abs/2402.14008](https://arxiv.org/abs/2402.14008 "").

- Henderson et al. (2018)↑
Peter Henderson, Riashat Islam, Philip Bachman, Joelle Pineau, Doina Precup, and David Meger.

Deep reinforcement learning that matters.

In _Proceedings of the AAAI conference on artificial intelligence_, volume 32, 2018.

- Hendrycks et al. (2021)↑
Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt.

Measuring mathematical problem solving with the math dataset.

_arXiv preprint arXiv:2103.03874_, 2021.

- Hu (2025)↑
Jian Hu.

Reinforce++: A simple and efficient approach for aligning large language models.

_arXiv preprint arXiv:2501.03262_, 2025.

- Hu et al. (2025)↑
Jingcheng Hu, Yinmin Zhang, Qi Han, Daxin Jiang, and Heung-Yeung Shum Xiangyu Zhang.

Open-reasoner-zero: An open source approach to scaling reinforcement learning on the base model.

[https://github.com/Open-Reasoner-Zero/Open-Reasoner-Zero](https://github.com/Open-Reasoner-Zero/Open-Reasoner-Zero ""), 2025.

- Huang et al. (2025)↑
Wenxuan Huang, Bohan Jia, Zijie Zhai, Shaosheng Cao, Zheyu Ye, Fei Zhao, Yao Hu, and Shaohui Lin.

Vision-r1: Incentivizing reasoning capability in multimodal large language models.

_arXiv preprint arXiv:2503.06749_, 2025.

- HuggingFaceH4 (2024)↑
HuggingFaceH4.

Math-500 dataset.

[https://huggingface.co/datasets/HuggingFaceH4/MATH-500/blob/main/README.md](https://huggingface.co/datasets/HuggingFaceH4/MATH-500/blob/main/README.md ""), 2024.

Accessed: 2025-03-29.

- Hutchinson et al. (2022)↑
Ben Hutchinson, Negar Rostamzadeh, Christina Greer, Katherine Heller, and Vinodkumar Prabhakaran.

Evaluation gaps in machine learning practice.

In _Proceedings of the 2022 ACM conference on fairness, accountability, and transparency_, pp.  1859–1876, 2022.

- Intelligent Internet (2025)↑
Intelligent Internet.

II-Thought : A Large-Scale, High-Quality Reasoning Dataset, 2025.

- Jaech et al. (2024)↑
Aaron Jaech, Adam Kalai, Adam Lerer, Adam Richardson, Ahmed El-Kishky, Aiden Low, Alec Helyar, Aleksander Madry, Alex Beutel, Alex Carney, et al.

Openai o1 system card.

_arXiv preprint arXiv:2412.16720_, 2024.

- Jha et al. (2024)↑
Piyush Jha, Prithwish Jana, Pranavkrishna Suresh, Arnav Arora, and Vijay Ganesh.

Rlsf: Reinforcement learning via symbolic feedback.

_arXiv preprint arXiv:2405.16661_, 2024.

- Jordan et al. (2020)↑
Scott Jordan, Yash Chandak, Daniel Cohen, Mengxue Zhang, and Philip Thomas.

Evaluating the performance of reinforcement learning algorithms.

In _International Conference on Machine Learning_, pp.  4962–4973. PMLR, 2020.

- Jordan et al. (2024)↑
Scott M Jordan, Adam White, Bruno Castro Da Silva, Martha White, and Philip S Thomas.

Position: Benchmarking is limited in reinforcement learning research.

_arXiv preprint arXiv:2406.16241_, 2024.

- Kandpal et al. (2023)↑
Nikhil Kandpal, Haikang Deng, Adam Roberts, Eric Wallace, and Colin Raffel.

Large language models struggle to learn long-tail knowledge.

In _International Conference on Machine Learning_, pp.  15696–15707. PMLR, 2023.

- Kazemnejad et al. (2024)↑
Amirhossein Kazemnejad, Milad Aghajohari, Eva Portelance, Alessandro Sordoni, Siva Reddy, Aaron Courville, and Nicolas Le Roux.

Vineppo: Unlocking rl potential for llm reasoning through refined credit assignment.

_arXiv preprint arXiv:2410.01679_, 2024.

- Knovel Engineering (2025)↑
Knovel Engineering.

Amc-23 dataset, 2025.

URL [https://huggingface.co/datasets/knoveleng/AMC-23](https://huggingface.co/datasets/knoveleng/AMC-23 "").

- Kwon et al. (2023)↑
Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Gonzalez, Hao Zhang, and Ion Stoica.

Efficient memory management for large language model serving with pagedattention.

In _Proceedings of the ACM SIGOPS 29th Symposium on Operating Systems Principles_, 2023.

- Lewkowycz et al. (2022)↑
Aitor Lewkowycz, Anders Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay Ramasesh, Ambrose Slone, Cem Anil, Imanol Schlag, Theo Gutman-Solo, Yuhuai Wu, Behnam Neyshabur, Guy Gur-Ari, and Vedant Misra.

Solving quantitative reasoning problems with language models.

In S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh (eds.), _Advances in Neural Information Processing Systems_, volume 35, pp.  3843–3857. Curran Associates, Inc., 2022.

URL [https://proceedings.neurips.cc/paper\_files/paper/2022/file/18abbeef8cfe9203fdf9053c9c4fe191-Paper-Conference.pdf](https://proceedings.neurips.cc/paper_files/paper/2022/file/18abbeef8cfe9203fdf9053c9c4fe191-Paper-Conference.pdf "").

- Li et al. (2025a)↑
Xuefeng Li, Haoyang Zou, and Pengfei Liu.

LIMR: Less is More for RL Scaling.

_arXiv preprint arXiv:2502.11886_, 2025a.

- Li et al. (2025b)↑
Zhong-Zhi Li, Duzhen Zhang, Ming-Liang Zhang, Jiaxin Zhang, Zengyan Liu, Yuxuan Yao, Haotian Xu, Junhao Zheng, Pei-Jie Wang, Xiuyi Chen, et al.

From system 1 to system 2: A survey of reasoning large language models.

_arXiv preprint arXiv:2502.17419_, 2025b.

- Liao et al. (2021)↑
Thomas Liao, Rohan Taori, Inioluwa Deborah Raji, and Ludwig Schmidt.

Are we learning yet? A meta review of evaluation failures across machine learning.

In _Thirty-fifth Conference on Neural Information Processing Systems Datasets and Benchmarks Track (Round 2)_, 2021.

- Lightman et al. (2023)↑
Hunter Lightman, Vineet Kosaraju, Yuri Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe.

Let’s verify step by step.

In _The Twelfth International Conference on Learning Representations_, 2023.

- Lin (2025)↑
Yen-Ting Lin.

Aime 2025 dataset, 2025.

URL [https://huggingface.co/datasets/yentinglin/aime\_2025](https://huggingface.co/datasets/yentinglin/aime_2025 "").

Accessed: 2025-03-29.

- Lin et al. (2025a)↑
Zhihang Lin, Mingbao Lin, Yuan Xie, and Rongrong Ji.

Cppo: Accelerating the training of group relative policy optimization-based reasoning models.

_arXiv preprint arXiv:2503.22342_, 2025a.

- Lin et al. (2025b)↑
Zhiyu Lin, Yifei Gao, Xian Zhao, Yunfan Yang, and Jitao Sang.

Mind with eyes: from language reasoning to multimodal reasoning.

_arXiv preprint arXiv:2503.18071_, 2025b.

- Lipton & Steinhardt (2019)↑
Zachary C Lipton and Jacob Steinhardt.

Troubling trends in machine learning scholarship: Some ml papers suffer from flaws that could mislead the public and stymie future research.

_Queue_, 17(1):45–77, 2019.

- Liu & Zhang (2025)↑
Jiawei Liu and Lingming Zhang.

Code-r1: Reproducing r1 for code with reliable rewards.

2025.

- Liu et al. (2024)↑
Junnan Liu, Hongwei Liu, Linchen Xiao, Ziyi Wang, Kuikun Liu, Songyang Gao, Wenwei Zhang, Songyang Zhang, and Kai Chen.

Are your llms capable of stable reasoning?

_arXiv preprint arXiv:2412.13147_, 2024.

- Liu et al. (2025a)↑
Zichen Liu, Changyu Chen, Wenjun Li, Tianyu Pang, Chao Du, and Min Lin.

There may not be aha moment in r1-zero-like training — a pilot study.

[https://oatllm.notion.site/oat-zero](https://oatllm.notion.site/oat-zero ""), 2025a.

Notion Blog.

- Liu et al. (2025b)↑
Zichen Liu, Changyu Chen, Wenjun Li, Penghui Qi, Tianyu Pang, Chao Du, Wee Sun Lee, and Min Lin.

Understanding r1-zero-like training: A critical perspective, 2025b.

URL [https://arxiv.org/abs/2503.20783](https://arxiv.org/abs/2503.20783 "").

- Liu et al. (2025c)↑
Ziyu Liu, Zeyi Sun, Yuhang Zang, Xiaoyi Dong, Yuhang Cao, Haodong Duan, Dahua Lin, and Jiaqi Wang.

Visual-rft: Visual reinforcement fine-tuning.

_arXiv preprint arXiv:2503.01785_, 2025c.

- Luo et al. (2025)↑
Michael Luo, Sijun Tan, Justin Wong, Xiaoxiang Shi, William Y. Tang, Manan Roongta, Colin Cai, Jeffrey Luo, Tianjun Zhang, Li Erran Li, Raluca Ada Popa, and Ion Stoica.

DeepScaleR: Surpassing O1-Preview with a 1.5B Model by Scaling RL, 2025.

Notion Blog.

- Lyu et al. (2025)↑
Chengqi Lyu, Songyang Gao, Yuzhe Gu, Wenwei Zhang, Jianfei Gao, Kuikun Liu, Ziyi Wang, Shuaibin Li, Qian Zhao, Haian Huang, et al.

Exploring the limit of outcome reward for learning mathematical reasoning.

_arXiv preprint arXiv:2502.06781_, 2025.

- Ma et al. (2025)↑
Yan Ma, Steffi Chern, Xuyang Shen, Yiran Zhong, and Pengfei Liu.

Rethinking rl scaling for vision language models: A transparent, from-scratch framework and comprehensive evaluation scheme.

_arXiv preprint arXiv:2504.02587_, 2025.

- Ma et al. (2023)↑
Yecheng Jason Ma, William Liang, Guanzhi Wang, De-An Huang, Osbert Bastani, Dinesh Jayaraman, Yuke Zhu, Linxi Fan, and Anima Anandkumar.

Eureka: Human-level reward design via coding large language models.

_arXiv preprint arXiv:2310.12931_, 2023.

- Machado et al. (2018)↑
Marlos C Machado, Marc G Bellemare, Erik Talvitie, Joel Veness, Matthew Hausknecht, and Michael Bowling.

Revisiting the arcade learning environment: Evaluation protocols and open problems for general agents.

_Journal of Artificial Intelligence Research_, 61:523–562, 2018.

- (72)↑
Lovish Madaan, Aaditya K Singh, Rylan Schaeffer, Andrew Poulton, Sanmi Koyejo, Pontus Stenetorp, Sharan Narang, and Dieuwke Hupkes.

Quantifying variance in evaluation benchmarks, 2024.

_URL https://arxiv. org/abs/2406.10229_.

- Marie et al. (2021)↑
Benjamin Marie, Atsushi Fujita, and Raphael Rubino.

Scientific credibility of machine translation research: A meta-evaluation of 769 papers.

_arXiv preprint arXiv:2106.15195_, 2021.

- Meng et al. (2025)↑
Fanqing Meng, Lingxiao Du, Zongkai Liu, Zhixiang Zhou, Quanfeng Lu, Daocheng Fu, Botian Shi, Wenhai Wang, Junjun He, Kaipeng Zhang, et al.

Mm-eureka: Exploring visual aha moment with rule-based large-scale reinforcement learning.

_arXiv preprint arXiv:2503.07365_, 2025.

- Meta-AI (2025)↑
Meta-AI.

The llama 4 herd: The beginning of a new era of natively multimodal ai innovation, 2025.

URL [https://ai.meta.com/blog/llama-4-multimodal-intelligence/](https://ai.meta.com/blog/llama-4-multimodal-intelligence/ "").

Accessed: 2025-04-07.

- Min et al. (2024)↑
Yingqian Min, Zhipeng Chen, Jinhao Jiang, Jie Chen, Jia Deng, Yiwen Hu, Yiru Tang, Jiapeng Wang, Xiaoxue Cheng, Huatong Song, Wayne Xin Zhao, Zheng Liu, Zhongyuan Wang, and Ji-Rong Wen.

Imitate, explore, and self-improve: A reproduction report on slow-thinking reasoning systems, 2024.

URL [https://arxiv.org/abs/2412.09413](https://arxiv.org/abs/2412.09413 "").

- Mirzadeh et al. (2024)↑
Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, and Mehrdad Farajtabar.

Gsm-symbolic: Understanding the limitations of mathematical reasoning in large language models.

_arXiv preprint arXiv:2410.05229_, 2024.

- Muennighoff et al. (2025)↑
Niklas Muennighoff, Zitong Yang, Weijia Shi, Xiang Lisa Li, Li Fei-Fei, Hannaneh Hajishirzi, Luke Zettlemoyer, Percy Liang, Emmanuel Candès, and Tatsunori Hashimoto.

s1: Simple test-time scaling, 2025.

URL [https://arxiv.org/abs/2501.19393](https://arxiv.org/abs/2501.19393 "").

- Musgrave et al. (2020)↑
Kevin Musgrave, Serge Belongie, and Ser-Nam Lim.

A metric learning reality check.

In _Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part XXV 16_, pp.  681–699. Springer, 2020.

- Nezhurina et al. (2024)↑
Marianna Nezhurina, Lucia Cipolina-Kun, Mehdi Cherti, and Jenia Jitsev.

Alice in wonderland: Simple tasks showing complete reasoning breakdown in state-of-the-art large language models.

_arXiv preprint arXiv:2406.02061_, 2024.

- OpenAI (2025)↑
OpenAI.

OpenAI o3-mini System Card, January 2025.

URL [https://cdn.openai.com/o3-mini-system-card-feb10.pdf](https://cdn.openai.com/o3-mini-system-card-feb10.pdf "").

- Parashar et al. (2024)↑
Shubham Parashar, Zhiqiu Lin, Tian Liu, Xiangjue Dong, Yanan Li, Deva Ramanan, James Caverlee, and Shu Kong.

The neglected tails in vision-language models.

In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_, pp.  12988–12997, 2024.

- Patterson et al. (2024)↑
Andrew Patterson, Samuel Neumann, Martha White, and Adam White.

Empirical design in reinforcement learning.

_Journal of Machine Learning Research_, 25(318):1–63, 2024.

- Peng et al. (2025)↑
Yingzhe Peng, Gongrui Zhang, Miaosen Zhang, Zhiyuan You, Jie Liu, Qipeng Zhu, Kai Yang, Xingzhong Xu, Xin Geng, and Xu Yang.

Lmm-r1: Empowering 3b lmms with strong reasoning abilities through two-stage rule-based rl.

_arXiv preprint arXiv:2503.07536_, 2025.

- Petrov et al. (2025)↑
Ivo Petrov, Jasper Dekoninck, Lyuben Baltadzhiev, Maria Drencheva, Kristian Minchev, Mislav Balunović, Nikola Jovanović, and Martin Vechev.

Proof or bluff? evaluating llms on 2025 usa math olympiad.

_arXiv preprint arXiv:2503.21934_, 2025.

- Prabhu et al. (2020)↑
Ameya Prabhu, Philip HS Torr, and Puneet K Dokania.

Gdumb: A simple approach that questions our progress in continual learning.

In _Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part II 16_, pp.  524–540. Springer, 2020.

- Prabhu et al. (2024a)↑
Ameya Prabhu, Shiven Sinha, Ponnurangam Kumaraguru, Philip HS Torr, Ozan Sener, and Puneet K Dokania.

Randumb: A simple approach that questions the efficacy of continual representation learning.

_arXiv e-prints_, pp.  arXiv–2402, 2024a.

- Prabhu et al. (2024b)↑
Ameya Prabhu, Vishaal Udandarao, Philip Torr, Matthias Bethge, Adel Bibi, and Samuel Albanie.

Efficient lifelong model evaluation in an era of rapid progress.

_arXiv preprint arXiv:2402.19472_, 2024b.

- Press et al. (2023)↑
Ori Press, Steffen Schneider, Matthias Kümmerer, and Matthias Bethge.

Rdumb: A simple approach that questions our progress in continual test-time adaptation.

_Advances in Neural Information Processing Systems_, 36:39915–39935, 2023.

- PyTorch Contributors (2024)↑
PyTorch Contributors.

Reproducibility — pytorch documentation.

[https://pytorch.org/docs/stable/notes/randomness.html](https://pytorch.org/docs/stable/notes/randomness.html ""), 2024.

Accessed: 2025-04-09.

- Renze (2024)↑
Matthew Renze.

The effect of sampling temperature on problem solving in large language models.

In _Findings of the Association for Computational Linguistics: EMNLP 2024_, pp.  7346–7356, 2024.

- Reuel et al. (2024)↑
Anka Reuel, Amelia Hardy, Chandler Smith, Max Lamparth, Malcolm Hardy, and Mykel J Kochenderfer.

BetterBench: Assessing AI Benchmarks, Uncovering Issues, and Establishing Best Practices.

_arXiv preprint arXiv:2411.12990_, 2024.

- Roberts et al. (2025)↑
Jonathan Roberts, Mohammad Reza Taesiri, Ansh Sharma, Akash Gupta, Samuel Roberts, Ioana Croitoru, Simion-Vlad Bogolin, Jialu Tang, Florian Langer, Vyas Raina, et al.

Zerobench: An impossible visual benchmark for contemporary large multimodal models.

_arXiv preprint arXiv:2502.09696_, 2025.

- Roberts et al. (2023)↑
Manley Roberts, Himanshu Thakur, Christine Herlihy, Colin White, and Samuel Dooley.

To the cutoff… and beyond? a longitudinal perspective on llm data contamination.

In _The Twelfth International Conference on Learning Representations_, 2023.

- Roux et al. (2025)↑
Nicolas Le Roux, Marc G Bellemare, Jonathan Lebensold, Arnaud Bergeron, Joshua Greaves, Alex Fréchette, Carolyne Pelletier, Eric Thibodeau-Laufer, Sándor Toth, and Sam Work.

Tapered off-policy reinforce: Stable and efficient reinforcement learning for llms.

_arXiv preprint arXiv:2503.14286_, 2025.

- Shao et al. (2024)↑
Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Y Wu, et al.

Deepseekmath: Pushing the limits of mathematical reasoning in open language models.

_arXiv preprint arXiv:2402.03300_, 2024.

- Shen et al. (2025)↑
Wei Shen, Guanlin Liu, Zheng Wu, Ruofei Zhu, Qingping Yang, Chao Xin, Yu Yue, and Lin Yan.

Exploring data scaling trends and effects in reinforcement learning from human feedback.

_arXiv preprint arXiv:2503.22230_, 2025.

- Sim & Chen (2024)↑
Shamus Sim and Tyrone Chen.

Critique of impure reason: Unveiling the reasoning behaviour of medical large language models.

_arXiv preprint arXiv:2412.15748_, 2024.

- Song et al. (2025)↑
Mingyang Song, Mao Zheng, Zheng Li, Wenjie Yang, Xuan Luo, Yue Pan, and Feng Zhang.

FastCuRL: Curriculum Reinforcement Learning with Progressive Context Extension for Efficient Training R1-like Reasoning Models, 2025.

URL [https://arxiv.org/abs/2503.17287](https://arxiv.org/abs/2503.17287 "").

- Srivastava et al. (2024)↑
Saurabh Srivastava, Anto PV, Shashank Menon, Ajay Sukumar, Alan Philipose, Stevin Prince, Sooraj Thomas, et al.

Functional benchmarks for robust evaluation of reasoning performance, and the reasoning gap.

_arXiv preprint arXiv:2402.19450_, 2024.

- Su et al. (2025)↑
Yi Su, Dian Yu, Linfeng Song, Juntao Li, Haitao Mi, Zhaopeng Tu, Min Zhang, and Dong Yu.

Expanding rl with verifiable rewards across diverse domains.

_arXiv preprint arXiv:2503.23829_, 2025.

- Team (2025)↑
Team.

Open Thoughts.

https://open-thoughts.ai, January 2025.

- Team et al. (2025)↑
Kimi Team, Angang Du, Bofei Gao, Bowei Xing, Changjiu Jiang, Cheng Chen, Cheng Li, Chenjun Xiao, Chenzhuang Du, Chonghua Liao, et al.

Kimi k1. 5: Scaling reinforcement learning with llms.

_arXiv preprint arXiv:2501.12599_, 2025.

- Tu et al. (2025)↑
Songjun Tu, Jiahao Lin, Xiangyu Tian, Qichao Zhang, Linjing Li, Yuqian Fu, Nan Xu, Wei He, Xiangyuan Lan, Dongmei Jiang, et al.

Enhancing llm reasoning with iterative dpo: A comprehensive empirical investigation.

_arXiv preprint arXiv:2503.12854_, 2025.

- Udandarao et al. (2024)↑
Vishaal Udandarao, Ameya Prabhu, Adhiraj Ghosh, Yash Sharma, Philip Torr, Adel Bibi, Samuel Albanie, and Matthias Bethge.

No" zero-shot" without exponential data: Pretraining concept frequency determines multimodal model performance.

In _The Thirty-eighth Annual Conference on Neural Information Processing Systems_, 2024.

- Uesato et al. (2022)↑
Jonathan Uesato, Nate Kushman, Ramana Kumar, Francis Song, Noah Siegel, Lisa Wang, Antonia Creswell, Geoffrey Irving, and Irina Higgins.

Solving math word problems with process-and outcome-based feedback.

_arXiv preprint arXiv:2211.14275_, 2022.

- vLLM Contributors (2024)↑
vLLM Contributors.

Inference reproducibility script.

[https://github.com/vllm-project/vllm/blob/098900d7c2b53324687977eece400f634755cf51/examples/offline\_inference/reproduciblity.py](https://github.com/vllm-project/vllm/blob/098900d7c2b53324687977eece400f634755cf51/examples/offline_inference/reproduciblity.py ""), 2024.

Accessed: 2025-04-09.

- Wang et al. (2025)↑
Yue Wang, Qiuzhi Liu, Jiahao Xu, Tian Liang, Xingyu Chen, Zhiwei He, Linfeng Song, Dian Yu, Juntao Li, Zhuosheng Zhang, et al.

Thoughts are all over the place: On the underthinking of o1-like llms.

_arXiv preprint arXiv:2501.18585_, 2025.

- Wen et al. (2025a)↑
Liang Wen, Yunke Cai, Fenrui Xiao, Xin He, Qi An, Zhenyu Duan, Yimin Du, Junchen Liu, Lifu Tang, Xiaowei Lv, Haosheng Zou, Yongchao Deng, Shousheng Jia, and Xiangzheng Zhang.

Light-r1: Curriculum sft, dpo and rl for long cot from scratch and beyond, 2025a.

URL [https://arxiv.org/abs/2503.10460](https://arxiv.org/abs/2503.10460 "").

- Wen et al. (2025b)↑
Liang Wen, Yunke Cai, Fenrui Xiao, Xin He, Qi An, Zhenyu Duan, Yimin Du, Junchen Liu, Lifu Tang, Xiaowei Lv, et al.

Light-r1: Curriculum sft, dpo and rl for long cot from scratch and beyond.

_arXiv preprint arXiv:2503.10460_, 2025b.

- xAI (2025)↑
xAI.

Grok 3 beta — the age of reasoning agents.

February 2025.

URL [https://x.ai/news/grok-3](https://x.ai/news/grok-3 "").

Accessed: 2025-03-29.

- Xie et al. (2025)↑
Tian Xie, Zitian Gao, Qingnan Ren, Haoming Luo, Yuqian Hong, Bryan Dai, Joey Zhou, Kai Qiu, Zhirong Wu, and Chong Luo.

Logic-rl: Unleashing llm reasoning with rule-based reinforcement learning.

_arXiv preprint arXiv:2502.14768_, 2025.

- Yan et al. (2025)↑
Kai Yan, Yufei Xu, Zhengyin Du, Xuesong Yao, Zheyu Wang, Xiaowen Guo, and Jiecao Chen.

Recitation over reasoning: How cutting-edge language models can fail on elementary school-level reasoning problems?

_arXiv preprint arXiv:2504.00509_, 2025.

- Yang et al. (2024a)↑
An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, et al.

Qwen2. 5 technical report.

_arXiv preprint arXiv:2412.15115_, 2024a.

- Yang et al. (2024b)↑
An Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu, Chengpeng Li, Dayiheng Liu, Jianhong Tu, Jingren Zhou, Junyang Lin, et al.

Qwen2.5-math technical report: Toward mathematical expert model via self-improvement.

_arXiv preprint arXiv:2409.12122_, 2024b.

- Yu et al. (2024)↑
Huimu Yu, Xing Wu, Weidong Yin, Debing Zhang, and Songlin Hu.

Codepmp: Scalable preference model pretraining for large language model reasoning.

_arXiv preprint arXiv:2410.02229_, 2024.

- Yu et al. (2025)↑
Qiying Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Tiantian Fan, Gaohong Liu, Lingjun Liu, Xin Liu, et al.

Dapo: An open-source llm reinforcement learning system at scale.

_arXiv preprint arXiv:2503.14476_, 2025.

- Yuan et al. (2025)↑
Weizhe Yuan, Jane Yu, Song Jiang, Karthik Padthe, Yang Li, Dong Wang, Ilia Kulikov, Kyunghyun Cho, Yuandong Tian, Jason E Weston, et al.

Naturalreasoning: Reasoning in the wild with 2.8 m challenging questions.

_arXiv preprint arXiv:2502.13124_, 2025.

- Yue et al. (2025)↑
Yu Yue, Yufeng Yuan, Qiying Yu, Xiaochen Zuo, Ruofei Zhu, Wenyuan Xu, et al.

Vapo: Efficient and reliable reinforcement learning for advanced reasoning tasks.

_arXiv preprint arXiv:2504.05118_, 2025.

- Zeng et al. (2025a)↑
Thomas Zeng, Shuibai Zhang, Shutong Wu, Christian Classen, Daewon Chae, Ethan Ewer, Minjae Lee, Heeju Kim, Wonjun Kang, Jackson Kunde, et al.

Versaprm: Multi-domain process reward model via synthetic reasoning data.

_arXiv preprint arXiv:2502.06737_, 2025a.

- Zeng et al. (2025b)↑
Weihao Zeng, Yuzhen Huang, Qian Liu, Wei Liu, Keqing He, Zejun Ma, and Junxian He.

SimpleRL-Zoo: Investigating and Taming Zero Reinforcement Learning for Open Base Models in the Wild.

_arXiv preprint arXiv:2503.18892_, 2025b.

- Zhang et al. (2025)↑
Sheng Zhang, Qianchu Liu, Guanghui Qin, Tristan Naumann, and Hoifung Poon.

Med-rlvr: Emerging medical reasoning from a 3b base model via reinforcement learning.

_arXiv preprint arXiv:2502.19655_, 2025.


## Appendix A Appendix

Report issue for preceding element

### A.1 Bootstrapping Results on Additional Datasets

Report issue for preceding element

To complement our analysis in [3](https://arxiv.org/html/2504.07086v1#S3 "3 Exploring the Design Space of Reasoning: What Matters Most? ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility"), we present bootstrapped variance results on two additional datasets: AMC’23 and MATH500. As shown in Figures [12](https://arxiv.org/html/2504.07086v1#A1.F12 "Figure 12 ‣ A.1 Bootstrapping Results on Additional Datasets ‣ Appendix A Appendix ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility") and [13](https://arxiv.org/html/2504.07086v1#A1.F13 "Figure 13 ‣ A.1 Bootstrapping Results on Additional Datasets ‣ Appendix A Appendix ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility"), high variance in Pass@1 persists even when averaging over multiple seeds (K=5𝐾5K=5italic\_K = 5), mirroring the trends observed on AIME’24. These results reinforce our conclusion that small benchmark sizes yield unstable estimates and that robust performance reporting requires multiple seed runs.

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/x13.png)Figure 12: Variance of mean Pass@1 on AMC’23. Bootstrapped estimates show substantial variance even with K=5𝐾5K=5italic\_K = 5 evaluation runs, highlighting the instability of single-seed evaluations.Report issue for preceding element![Refer to caption](https://arxiv.org/html/x14.png)Figure 13: Variance of mean Pass@1 on MATH500. Similar to AIME’24 and AMC’23, the estimates remain volatile across seeds. Even K=5𝐾5K=5italic\_K = 5 runs do not eliminate variance, underscoring the need for larger K𝐾Kitalic\_K.Report issue for preceding element

### A.2 Hardware & Software Variations

Report issue for preceding element

In Figure [14](https://arxiv.org/html/2504.07086v1#A1.F14 "Figure 14 ‣ A.2 Hardware & Software Variations ‣ Appendix A Appendix ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility"), we show that the model performance variation due to hardware configuration is not limited to AIME’24 and AMC’23. Similar discrepancies are observed on MATH500, where different compute clusters yield different accuracy scores—even when model, seeds, and decoding parameters are held constant. This further emphasizes the need for hardware and software standardization when reporting benchmark results.

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/x15.png)Figure 14: Performance variation across compute clusters on MATH500. Differences in GPU type and environment lead to non-trivial shifts in performance, reinforcing the importance of hardware standardization.Report issue for preceding element

### A.3 Prompt Variants and Template Settings

Report issue for preceding element

We provide the exact templates used for our three prompt settings in Table [5](https://arxiv.org/html/2504.07086v1#A1.T5 "Table 5 ‣ A.3 Prompt Variants and Template Settings ‣ Appendix A Appendix ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility"): Math, Default, and No Template. These formats are based on the DeepSeek tokenizer but adapted for each model’s specific chat template. Our results (in [3.4](https://arxiv.org/html/2504.07086v1#S3.SS4 "3.4 Effect of Prompt Format and Context Length ‣ 3 Exploring the Design Space of Reasoning: What Matters Most? ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility")) indicate that instruction-tuned models are highly sensitive to prompt formatting, with performance degrading significantly when prompts deviate from their training-time structure.

Report issue for preceding element

| Prompt | Example |
| --- | --- |
| Math | <\|begin\_of\_sentence\|><\|User\|>Solve the following math problem efficiently and clearly. The last line of your response should be of the following format: ’Therefore, the final answer is: $\\boxed{ANSWER}$. I hope it is correct’ (without quotes) where ANSWER is just the final number or expression that solves the problem. Think step by step before answering.\\n <\|Assistant\|><think>\\n{Question} |
| Default | <\|begin\_of\_sentence\|><\|User\|>{Question} <\|Assistant\|><think>\\n |
| No Template | {Question} |

Table 5: Prompt templates used in our evaluation. The inclusion or exclusion of structured prompt tokens significantly impacts performance for instruction-tuned models.Report issue for preceding element

### A.4 Effect of Output Length Limits

Report issue for preceding element

We further explore how varying max\_new\_tokens impacts model accuracy. Figures below compare OpenRS-series models (with 131,072-token context windows) and OpenThinker/S1.1 models (with 32,768-token limits).

Report issue for preceding element

Figure [15](https://arxiv.org/html/2504.07086v1#A1.F15 "Figure 15 ‣ A.4 Effect of Output Length Limits ‣ Appendix A Appendix ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility") shows that OpenRS models are highly sensitive to this parameter—shortening outputs results in clear accuracy drops. Similarly, Figure [16](https://arxiv.org/html/2504.07086v1#A1.F16 "Figure 16 ‣ A.4 Effect of Output Length Limits ‣ Appendix A Appendix ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility") reveals the same pattern for OpenThinker-7B and S1.1-7B, despite their smaller context lengths. In both cases, premature truncation leads to incomplete reasoning chains and incorrect answers, confirming the importance of setting appropriate generation limits.

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/x16.png)Figure 15: Impact of max\_new\_tokens on OpenRS models. Models with long context support (131,072 tokens) experience degraded performance when max\_new\_tokens is set too low.Report issue for preceding element![Refer to caption](https://arxiv.org/html/x17.png)Figure 16: Impact of max\_new\_tokens on OpenThinker and S1.1 models. Despite shorter context limits (32,768 tokens), performance still degrades noticeably when output length is constrained.Report issue for preceding element

### A.5 Response Length vs. Accuracy — Per-Model Breakdown

Report issue for preceding element

To supplement the aggregated results shown in Figure [11](https://arxiv.org/html/2504.07086v1#S4.F11 "Figure 11 ‣ 4.4.1 Are Incorrect Responses Longer? ‣ 4.4 Do Discovered Phenomena Replicate? A Detailed Analysis. ‣ 4 Way Forward: Standardization in Evaluations ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility"), we include detailed histograms for each individual model in the appendix. These plots show the distribution of correct and incorrect responses across response lengths, averaged over random seeds. Due to the number of models analyzed, we split the results into two figures for clarity.

Report issue for preceding element

Figures [17](https://arxiv.org/html/2504.07086v1#A1.F17 "Figure 17 ‣ A.5 Response Length vs. Accuracy — Per-Model Breakdown ‣ Appendix A Appendix ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility") and [18](https://arxiv.org/html/2504.07086v1#A1.F18 "Figure 18 ‣ A.5 Response Length vs. Accuracy — Per-Model Breakdown ‣ Appendix A Appendix ‣ A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility") reveal that the overall trend observed in the main paper holds consistently across nearly all models: incorrect responses tend to be longer than correct ones.

Report issue for preceding element

These results reinforce the idea that excessively long outputs often indicate failure modes such as hallucinated reasoning, verbose overthinking, or degenerate loops. Importantly, this correlation persists well below the maximum sequence length, ruling out truncation as the sole cause.

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/x18.png)Figure 17: Response Length vs. Correctness — Models (1/2). Average number of correct and incorrect responses across response length bins for a subset of models. Longer responses consistently correlate with incorrect predictions.Report issue for preceding element![Refer to caption](https://arxiv.org/html/x19.png)Figure 18: Response Length vs. Correctness — Models (2/2). Continuation of model-wise response length analysis. The same trend holds across the remaining models, with incorrect answers being disproportionately long.Report issue for preceding element

Across all models, longer responses are a consistent marker of incorrect outputs, making response length a useful signal for detecting low-confidence or erroneous reasoning chains.

Report issue for preceding element

Report IssueReport Issue for Selection

Generated by
[L\\
A\\
T\\
Exml![[LOGO]](<Base64-Image-Removed>)](https://math.nist.gov/~BMiller/LaTeXML/)
