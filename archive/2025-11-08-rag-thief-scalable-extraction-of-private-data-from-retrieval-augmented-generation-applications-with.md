---
date: '2025-11-08'
description: The paper discusses RAG-Thief, an automated agent-based attack on Retrieval-Augmented
  Generation (RAG) applications, exposing significant vulnerabilities in private data
  extraction from knowledge bases. By employing an iterative, self-improving mechanism,
  RAG-Thief was able to retrieve over 70% of sensitive information from various RAG
  systems, demonstrating a marked improvement in extraction efficacy over traditional
  prompt injection methods. The findings underscore pressing privacy concerns in LLM-integrated
  applications, while suggesting foundational defense mechanisms to mitigate risks.
  This research is pivotal for enhancing security protocols in machine learning applications
  operating with sensitive data.
link: https://arxiv.org/html/2411.14110v1
tags:
- Data Privacy
- Prompt Injection Attacks
- Large Language Models
- Retrieval-Augmented Generation
- Agent-based Attacks
title: 'RAG-Thief: Scalable Extraction of Private Data from Retrieval-Augmented Generation
  Applications with Agent-based Attacks'
---

HTML conversions [sometimes display errors](https://info.dev.arxiv.org/about/accessibility_html_error_messages.html) due to content that did not convert correctly from the source. This paper uses the following packages that are not yet supported by the HTML conversion tool. Feedback on these issues are not necessary; they are known and are being worked on.

- failed: pdfcol

Authors: achieve the best HTML results from your LaTeX submissions by following these [best practices](https://info.arxiv.org/help/submit_latex_best_practices.html).

[License: CC BY-NC-ND 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2411.14110v1 \[cs.CR\] 21 Nov 2024

\\pdfcolInitStack

tcb@breakable



Report issue for preceding element

# RAG-Thief: Scalable Extraction of Private Data from Retrieval-Augmented Generation Applications with Agent-based Attacks

Report issue for preceding element

Changyue Jiang1,2121,21 , 2,
Xudong Pan1111,
Geng Hong1111,
Chenfu Bao3333,
Min Yang11111111Fudan University, China

2222Shanghai Innovation Institute, China

3333Baidu Inc., China

cyjiang24@m.fudan.edu.cn,
xdpan@fudan.edu.cn,
ghong@fudan.edu.cn,
baochenfu@baidu.com,
m\_yang@fudan.edu.cn

Report issue for preceding element

###### Abstract

Report issue for preceding element

While large language models (LLMs) have achieved notable success in generative tasks, they still face limitations, such as lacking up-to-date knowledge and producing hallucinations. Retrieval-Augmented Generation (RAG) enhances LLM performance by integrating external knowledge bases, providing additional context which significantly improves accuracy and knowledge coverage. However, building these external knowledge bases often requires substantial resources and may involve sensitive information.
In this paper, we propose an agent-based automated privacy attack called RAG-Thief, which can extract a scalable amount of private data from the private database used in RAG applications. We conduct a systematic study on the privacy risks associated with RAG applications, revealing that the vulnerability of LLMs makes the private knowledge bases suffer significant privacy risks. Unlike previous manual attacks which rely on traditional prompt injection techniques, RAG-Thief starts with an initial adversarial query and learns from model responses, progressively generating new queries to extract as many chunks from the knowledge base as possible.
Experimental results show that our RAG-Thief can extract over 70% information from the private knowledge bases within customized RAG applications deployed on local machines and real-world platforms, including OpenAI’s GPTs and ByteDance’s Coze. Our findings highlight the privacy vulnerabilities in current RAG applications and underscore the pressing need for stronger safeguards.

Report issue for preceding element

## 1 Introduction

Report issue for preceding element![Refer to caption](https://arxiv.org/html/2411.14110v1/x1.png)Figure 1: Attack scenario of RAG-Thief
and demonstration on a real-world healthcare-related RAG application from OpenAI GPTs (For ethical reasons, the GPT is created by the authors and only contains public data).Report issue for preceding element

Despite the impressive performance of large language models (LLMs) in tasks like knowledge-based question answering and content generation, they still face limitations in specific areas, such as generating hallucinations \[ [1](https://arxiv.org/html/2411.14110v1#bib.bib1 "")\], \[ [2](https://arxiv.org/html/2411.14110v1#bib.bib2 "")\] and lacking access to the most current data. The emergence of Retrieval-Augmented Generation (RAG) \[ [3](https://arxiv.org/html/2411.14110v1#bib.bib3 "")\], \[ [4](https://arxiv.org/html/2411.14110v1#bib.bib4 "")\], \[ [5](https://arxiv.org/html/2411.14110v1#bib.bib5 "")\], \[ [6](https://arxiv.org/html/2411.14110v1#bib.bib6 "")\], \[ [7](https://arxiv.org/html/2411.14110v1#bib.bib7 "")\], \[ [8](https://arxiv.org/html/2411.14110v1#bib.bib8 "")\], \[ [9](https://arxiv.org/html/2411.14110v1#bib.bib9 "")\] expands the capabilities of LLMs and becomes a popular method to enhanc their performance. RAG integrates information retrieval with text generation by using a retrieval module to extract the most relevant information chunks from external knowledge bases. These chunks are then used as contextual prompts for the language model, improving its ability to produce more accurate, relevant, and coherent responses. Currently, RAG technology is widely applied across various vertical industries, demonstrating significant value in fields like healthcare (e.g., SMART Health GPT\[ [10](https://arxiv.org/html/2411.14110v1#bib.bib10 ""), [11](https://arxiv.org/html/2411.14110v1#bib.bib11 "")\]), finance \[ [12](https://arxiv.org/html/2411.14110v1#bib.bib12 "")\], law (AutoLaw\[ [13](https://arxiv.org/html/2411.14110v1#bib.bib13 ""), [14](https://arxiv.org/html/2411.14110v1#bib.bib14 "")\]) , and scientific research (MyCrunchGPT\[ [15](https://arxiv.org/html/2411.14110v1#bib.bib15 "")\], \[ [16](https://arxiv.org/html/2411.14110v1#bib.bib16 "")\], \[ [17](https://arxiv.org/html/2411.14110v1#bib.bib17 "")\]) . For instance, in healthcare, RAG can be combined with proprietary case knowledge bases to build intelligent question-answering systems. These systems not only provide more precise medical analyses but also offer personalized healthcare guidance. By supplementing knowledge with the latest medical literature and case data, such systems can assist doctors and patients in making more informed decisions. Moreover, OpenAI allows users to build and publish GPTs, a type of AI application, with private data. Currently, there are over 3 million custom GPTs on the ChatGPT platform.

Report issue for preceding element

Intuitively, RAG systems should be relatively secure in terms of privacy, as the private knowledge base is merely an independent external file within the RAG system, and users can only interact with the LLM without direct access to the knowledge base content. However, some studies indicate that RAG systems pose data privacy risks related to the leakage of private knowledge bases. In practice, through prompt injection attacks and multi-turn interactions with LLM, attackers can gradually extract information snippets from the knowledge base by crafting carefully designed questions.
Qi et al. \[ [18](https://arxiv.org/html/2411.14110v1#bib.bib18 "")\] propose a prompt injection attack template using anchor question queries to retrieve the most relevant chunks from the private knowledge base. However, this method has a low success rate in the absence of relevant domain knowledge, achieving only a 3.22% success rate in simulated environments. Another recent study by Zeng et al. \[ [19](https://arxiv.org/html/2411.14110v1#bib.bib19 "")\] introduces a structured query format designed to target and extract specified private content from the knowledge base. However, this approach mainly focuses on extracting specific information within the private knowledge base and does not address the scalable extraction of the entire knowledge base.

Report issue for preceding element

Our Work. In this paper, we introduce an agent-based automated privacy attack against RAG applications named RAG-Thief, which is able to extract a scalable amount of private data from the private knowledge bases used in RAG applications (Fig. [1](https://arxiv.org/html/2411.14110v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ RAG-Thief: Scalable Extraction of Private Data from Retrieval-Augmented Generation Applications with Agent-based Attacks")). Unlike previous methods that rely on manual prompt injection or random attacks to gather information snippets, RAG-Thief employs a self-improving mechanism, which uses a few number of extracted source chunks to further reflect, do associative thinking, and generate new adversarial queries, enabling more effective attacks in the subsequent rounds. The process begins with a predefined initial adversarial question, which the agent uses to automatically query the LLM and collect information chunks. Based on these chunks, it generates new queries to attack the RAG system again, retrieving additional knowledge base segments. Through this iterative approach, RAG-Thief continuously gathers private knowledge pieces returned by the LLM. Compared with previous works, RAG-Thief significantly increases the scale of extracted private data with fewer queries. We also apply RAG-Thief on real-world RAG applications from OpenAI’s GPTs \[ [20](https://arxiv.org/html/2411.14110v1#bib.bib20 "")\] and ByteDance’s Coze \[ [21](https://arxiv.org/html/2411.14110v1#bib.bib21 "")\] (for ethical reasons, the applications are built by the authors on these platforms and contain only public data), and demonstrate its ability to successfully extract a scalable amount of private data from the applications (please see the bottom of Fig. [1](https://arxiv.org/html/2411.14110v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ RAG-Thief: Scalable Extraction of Private Data from Retrieval-Augmented Generation Applications with Agent-based Attacks")), which highlights the severity of privacy risks of current commercial RAG systems.

Report issue for preceding element

Extracting raw data from a RAG system’s private knowledge base through direct interaction with the LLM is challenging and requires considerable effort. The main challenges include:

Report issue for preceding element

1. 1.


Summarization by LLMs: In RAG systems, LLMs typically summarize the input knowledge before outputting it, making it challenging to directly access the original knowledge. RAG-Thief addresses this by designing what is known as the initial adversarial query. This query includes optimized prompt leakage attack cues, effectively tricking the LLM into outputting prompts that contain text chunks from the knowledge base.

Report issue for preceding element

2. 2.


Lack of Domain Knowledge: When lacking domain knowledge related to the private knowledge base, using randomly generated questions results in a low hit rate, making it difficult to cover the entire knowledge base and only allowing the extraction of a small portion of private information. Additionally, frequent querying of the LLM significantly consumes resources and energy. RAG-Thief mitigates these issues by analyzing the previously extracted information to infer and extend content, generating new adversarial queries based on these inferences. This approach not only increases the probability of retrieving adjacent text chunks but also reduces the number of queries, thereby improving attack efficiency.

Report issue for preceding element

3. 3.


Uncertainty and Randomness: The inherent uncertainty and randomness in LLM-generated content complicate the accurate extraction of original chunks, increasing the difficulty of automated processing. To address this, RAG-Thief employs a specialized post-processing function. This function uses regular expression matching techniques to identify and extract content that matches the format of text chunks. It then segments and processes this content to reconstruct the original text chunks, thereby enhancing the accuracy and efficiency of knowledge extraction.

Report issue for preceding element


For evaluation, we test RAG-Thief attack in self-built RAG applications including healthcare and personal assistant, both on local machines and on commercial platforms including OpenAI’s GPTs and ByteDance’s Coze. The results show that even without domain knowledge about the database, RAG-Thief achieves an extraction rate of over 70% of text chunks from the private knowledge base in the real world using only the pre-designed initial adversarial query.

Report issue for preceding element

Our Contributions. In summary, we mainly make the following contributions:

Report issue for preceding element

- •


We systematically analyze the security vulnerabilities of real-world RAG applications and propose RAG-Thief, an agent-based automated extraction attack against RAG application knowledge bases that adopts an effective feedback mechanism to continually increase the ratio of extracted data chunks.

Report issue for preceding element

- •


We conduct extensive experiments on both local and real-world RAG applications with different configurations and in privacy-critical scenarios including healthcare and personal assistant. The results strongler validate the effectiveness of RAG-Thief, which achieves nearly 3×3\\times3 × extraction ratio than the state-of-the-art extraction attack on RAG applications. Moreover, our attack shows strong performance on attacking two real-world applications on commercial platforms.

Report issue for preceding element

- •


We also discuss a number of potential defensive measures against data extraction attacks on RAG applications, which would be meaningful future directions to enhance the
data security of RAG systems.

Report issue for preceding element


## 2 Background

Report issue for preceding element

### 2.1 Retrieval-Augmented Generation (RAG)

Report issue for preceding element

RAG \[ [3](https://arxiv.org/html/2411.14110v1#bib.bib3 "")\], \[ [4](https://arxiv.org/html/2411.14110v1#bib.bib4 "")\], \[ [5](https://arxiv.org/html/2411.14110v1#bib.bib5 "")\], \[ [6](https://arxiv.org/html/2411.14110v1#bib.bib6 "")\], \[ [7](https://arxiv.org/html/2411.14110v1#bib.bib7 "")\], \[ [8](https://arxiv.org/html/2411.14110v1#bib.bib8 "")\], \[ [9](https://arxiv.org/html/2411.14110v1#bib.bib9 "")\] emerges as a prominent technique for enhancing LLMs. RAG mitigates the issue of hallucinations in LLMs by incorporating real-time, domain-specific knowledge, providing a cost-effective means to improve relevance, accuracy, and practical application across diverse contexts.

Report issue for preceding element

The RAG system comprises three core components: an external retrieval database, a retriever, and a LLM. The external knowledge base contains text chunks from original documents and their embedding vectors. Users can customize the knowledge base by adjusting content, chunk lengths and overlaps between adjacent chunks to enhance coverage and query responsiveness. The retriever performs efficient matching among embedding vectors, calculating the similarity between text chunks and queries. Users may choose different matching strategies, such as semantic or similarity-based matching, to increase retrieval flexibility and accuracy. The LLM then integrates retrieved contextual information to generate precise responses tailored to user needs. Users can select from a range of models, including state-of-the-art LLMs, to maximize the performance of the RAG system.

Report issue for preceding element

The RAG system follows a structured process:

Report issue for preceding element

1\. Creating External Data: External data, which is not part of the original LLM training set, comes from sources such as APIs, databases, and document repositories. This data is encoded as numerical vectors by an embedding model and stored in a vector database, forming a structured knowledge base accessible to the generative AI model.

Report issue for preceding element

2\. Retrieving Relevant Information: During application, the system performs a similarity search when a user poses a query. The query is converted into a vector representation, which is then compared with vectors in the database to retrieve the most relevant records. Common similarity metrics include cosine similarity, Euclidean distance, and L2-norm distance, allowing the retriever to identify and return the top-k𝑘kitalic\_k results with minimal distance to the query vector.

Report issue for preceding element

3\. Enhancing LLM Prompts: Finally, the RAG model augments the user query with retrieved data, creating an enriched prompt for the LLM. The LLM processes this enhanced prompt, referencing the contextual knowledge to generate a precise, contextually relevant response.

Report issue for preceding element

Through the RAG framework, LLMs achieve enhanced accuracy and adaptability across various domains by dynamically integrating pertinent external knowledge, underscoring the technique’s potential to broaden generative AI’s impact.

Report issue for preceding element

### 2.2 Prompt Injection Attacks

Report issue for preceding element

Prompt injection attacks pose a significant security threat to LLMs. Attackers use malicious input prompts to override the original prompts of an LLM, manipulating the model to produce unexpected behaviors or outputs. By carefully crafting inputs, attackers can bypass security mechanisms, generate harmful or biased content, or extract sensitive information. Due to these risks, the Open Web Application Security Project (OWASP) has identified prompt injection as the top threat facing LLMs \[ [22](https://arxiv.org/html/2411.14110v1#bib.bib22 "")\].

Report issue for preceding element

While instruction-tuned LLMs excel at understanding and executing complex user instructions, this adaptability introduces new vulnerabilities. Perez and Ribeiro \[ [23](https://arxiv.org/html/2411.14110v1#bib.bib23 "")\] reveal that models like GPT-3 are susceptible to prompt injection, where malicious prompts can subvert the model’s intended purpose or expose confidential information. Subsequent studies highlight the impact of prompt injection to real-world LLM applications \[ [24](https://arxiv.org/html/2411.14110v1#bib.bib24 "")\], \[ [25](https://arxiv.org/html/2411.14110v1#bib.bib25 "")\]. Liu et al. \[ [26](https://arxiv.org/html/2411.14110v1#bib.bib26 "")\] propose an automated gradient-based method to generate effective prompt injections.
Prompt injection poses new security risks, particularly for emerging systems that integrate LLMs with external content and documents. Injected prompts can instruct LLMs to disclose confidential data from user documents or make unauthorized modifications.

Report issue for preceding element

When LLMs are integrated into applications, the risk of prompt injection attacks increases \[ [23](https://arxiv.org/html/2411.14110v1#bib.bib23 "")\], \[ [25](https://arxiv.org/html/2411.14110v1#bib.bib25 "")\], \[ [27](https://arxiv.org/html/2411.14110v1#bib.bib27 "")\], \[ [28](https://arxiv.org/html/2411.14110v1#bib.bib28 "")\] because these models often handle large volumes of data from untrusted sources and lack inherent defenses against such attacks. Recent research highlights that attackers can employ various methods to enhance the effectiveness of prompt injections, such as misleading statements \[ [23](https://arxiv.org/html/2411.14110v1#bib.bib23 "")\], unique characters \[ [25](https://arxiv.org/html/2411.14110v1#bib.bib25 "")\], and other techniques \[ [29](https://arxiv.org/html/2411.14110v1#bib.bib29 "")\].

Report issue for preceding element

In summary, prompt injection attacks may lead to sensitive information leaks and privacy breaches, posing significant threats to the deployment and use of LLM-integrated applications. The RAG system, as an advanced LLM-integrated application, incorporates a multi-layered retrieval and generation mechanism, making naive prompt injection attacks less effective against it.

Report issue for preceding element

### 2.3 LLM-based Agents

Report issue for preceding element

LLM-based agents \[ [30](https://arxiv.org/html/2411.14110v1#bib.bib30 "")\], \[ [31](https://arxiv.org/html/2411.14110v1#bib.bib31 "")\] are a crucial technology in artificial intelligence, with capabilities to understand natural language instructions, perform self-reflection, perceive external environments, and execute various actions, demonstrating a degree of autonomy \[ [30](https://arxiv.org/html/2411.14110v1#bib.bib30 "")\], \[ [31](https://arxiv.org/html/2411.14110v1#bib.bib31 "")\], \[ [32](https://arxiv.org/html/2411.14110v1#bib.bib32 "")\], \[ [33](https://arxiv.org/html/2411.14110v1#bib.bib33 "")\]. Their core advantage lies in leveraging the powerful generative abilities of LLMs, enabling them to achieve task objectives in specific scenarios through memory formation, self-reflection, and tool utilization. These agents excel at handling complex tasks, as they can observe and interact with their environment, adjust dynamically, build memory, and plan effectively, creating an independent problem-solving pathway. Classic examples of LLM-based agents include AutoGPT \[ [34](https://arxiv.org/html/2411.14110v1#bib.bib34 "")\] and AutoGen \[ [35](https://arxiv.org/html/2411.14110v1#bib.bib35 "")\].

Report issue for preceding element

LLM-based agents consist of three core components: the Brain, Perception, and Action modules. The Brain, built on LLMs, is responsible for storing memory and knowledge, processing information, and making decisions. This module records and utilizes historical information, providing contextual support for generating new content. The Perception module handles environmental sensing and interaction, allowing the agent to obtain and process external information in real time, such as retrieving and analyzing content generated by the LLM. The Action module enables tool use and task execution, ensuring the agent can dynamically adapt to changing environments. For instance, the agent can manipulate web pages or interfaces to autonomously engage in multi-turn dialogues with LLM applications, facilitating effective interaction with both users and systems.

Report issue for preceding element

This modular structure equips LLM-based agents with efficient task-processing capabilities, enabling them to continuously improve autonomy and adaptability through multi-layered feedback and optimization mechanisms, thus achieving high performance in complex environments.

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2411.14110v1/x2.png)Figure 2: The pipeline of RAG-Thief, which initiates the attack with ❶ an initial adversarial query targeting the RAG application to ❷ extract specific chunks. Then RAG-Thief ❸ stores these chunks in the short-term memory, and ❹ heuristically generates multiple anchor questions for each chunk based on an attack LLM. These anchor questions are then ❺ concatenated with the initial adversarial query to create new adversarial queries for the next round of attacks. The extracted chunks are subsequently ❻ stored as the agent’s long-term memory, with duplicates excluded from storage.Report issue for preceding element

## 3 Threat Model

Report issue for preceding element

In this section, we provide a detailed description of our threat model, which categorizes attack scenarios into two distinct settings: targeted attacks and untargeted attacks. Our threat model comprises two main components: a target RAG application and an adversary. We assume that the attacker employs black-box attacks in a real-world environment, interacting with the system solely through API queries. This restricts the attacker’s strategy to extracting information by constructing and modifying queries q𝑞qitalic\_q. In our threat model, we assume the following two parties:

Report issue for preceding element

Target RAG Application. This application allows users to query relevant questions and handles natural language processing tasks. The RAG application integrates a private knowledge base, such as those built on GPTs. We assume that application developers keep the content of their private knowledge base confidential to protect their intellectual property. The knowledge base primarily consists of text data, which can be in any language.

Report issue for preceding element

Adversary. The adversary aims to steal the complete knowledge base of the RAG system. The adversary has closed access to the target RAG application, meaning they can send queries and receive responses but cannot access the internal architecture or parameters of the RAG system. In this work, we mainly consider the following two attack scenarios depending on the attacker’s knowledge on the application domain:

Report issue for preceding element

- •


Untargeted Attack: The adversary has no prior knowledge of the information contained within the RAG knowledge base. This represents a more generalized application scenario in which the private knowledge base of a RAG system may include a diverse mix of documents spanning various domains. Consequently, it is challenging for the attacker to focus on a specific domain as an entry point for the attack.

Report issue for preceding element

- •


Targeted Attack: The adversary possesses domain knowledge related to the RAG knowledge base. Most publicly available RAG applications provide introductory information and example metadata, which attackers can leverage to optimize and adjust their attacks against the target system.

Report issue for preceding element


This threat model allows us to systematically analyze and evaluate the effectiveness of different attack strategies and the defensive capabilities of RAG systems under various attack conditions. It lays the groundwork for subsequent security enhancement measures.

Report issue for preceding element

## 4 Methodology of RAG-Thief

Report issue for preceding element

### 4.1 Overview of Agent-based Attacks

Report issue for preceding element

As shown in Fig. [2](https://arxiv.org/html/2411.14110v1#S2.F2 "Figure 2 ‣ 2.3 LLM-based Agents ‣ 2 Background ‣ RAG-Thief: Scalable Extraction of Private Data from Retrieval-Augmented Generation Applications with Agent-based Attacks"), RAG-Thief is an agent capable of interacting with its environment, reflecting, making decisions, and executing actions. Its attack process mainly consists of these stages: interacting with RAG applications, chunks extraction, memory storage, and reflecting mechanism.

Report issue for preceding element

Interacting with RAG applications. In the interaction phase, RAG-Thief initiates queries to the RAG application. This begins with an initial adversarial query qa⁢d⁢vsubscript𝑞𝑎𝑑𝑣q\_{adv}italic\_q start\_POSTSUBSCRIPT italic\_a italic\_d italic\_v end\_POSTSUBSCRIPT. This query is designed not only to retrieve information from the RAG system’s private knowledge base but also to include crafted adversarial commands that prompt the LLM to leak the retrieved source text chunks. Once text chunks start leaking, RAG-Thief uses these extracted chunks to craft follow-up attack queries. Let D𝐷Ditalic\_D represent the private knowledge base, R𝑅Ritalic\_R the retriever of the RAG application. The basic process can be described as follows:

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | r⁢e⁢s⁢p⁢o⁢n⁢s⁢e=ChatLLM⁢(RD⁢(qa⁢d⁢v)⊕qa⁢d⁢v)𝑟𝑒𝑠𝑝𝑜𝑛𝑠𝑒ChatLLMdirect-sumsubscript𝑅𝐷subscript𝑞𝑎𝑑𝑣subscript𝑞𝑎𝑑𝑣response=\\text{ChatLLM}(R\_{D}(q\_{adv})\\oplus q\_{adv})italic\_r italic\_e italic\_s italic\_p italic\_o italic\_n italic\_s italic\_e = ChatLLM ( italic\_R start\_POSTSUBSCRIPT italic\_D end\_POSTSUBSCRIPT ( italic\_q start\_POSTSUBSCRIPT italic\_a italic\_d italic\_v end\_POSTSUBSCRIPT ) ⊕ italic\_q start\_POSTSUBSCRIPT italic\_a italic\_d italic\_v end\_POSTSUBSCRIPT ) |  |

where ⊕direct-sum\\oplus⊕ is string concatenation and RD⁢(qa⁢d⁢v)⊕qa⁢d⁢vdirect-sumsubscript𝑅𝐷subscript𝑞𝑎𝑑𝑣subscript𝑞𝑎𝑑𝑣R\_{D}(q\_{adv})\\oplus q\_{adv}italic\_R start\_POSTSUBSCRIPT italic\_D end\_POSTSUBSCRIPT ( italic\_q start\_POSTSUBSCRIPT italic\_a italic\_d italic\_v end\_POSTSUBSCRIPT ) ⊕ italic\_q start\_POSTSUBSCRIPT italic\_a italic\_d italic\_v end\_POSTSUBSCRIPT is the prompt construction based on the retrieved chunks and query q𝑞qitalic\_q.

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | RD⁢(qa⁢d⁢v)={c⁢h⁢u⁢n⁢k1,…,c⁢h⁢u⁢n⁢kk}subscript𝑅𝐷subscript𝑞𝑎𝑑𝑣𝑐ℎ𝑢𝑛subscript𝑘1…𝑐ℎ𝑢𝑛subscript𝑘𝑘R\_{D}(q\_{adv})=\\{chunk\_{1},...,chunk\_{k}\\}italic\_R start\_POSTSUBSCRIPT italic\_D end\_POSTSUBSCRIPT ( italic\_q start\_POSTSUBSCRIPT italic\_a italic\_d italic\_v end\_POSTSUBSCRIPT ) = { italic\_c italic\_h italic\_u italic\_n italic\_k start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT , … , italic\_c italic\_h italic\_u italic\_n italic\_k start\_POSTSUBSCRIPT italic\_k end\_POSTSUBSCRIPT } |  |

where c⁢h⁢u⁢n⁢k1,…,c⁢h⁢u⁢n⁢kk𝑐ℎ𝑢𝑛subscript𝑘1…𝑐ℎ𝑢𝑛subscript𝑘𝑘chunk\_{1},...,chunk\_{k}italic\_c italic\_h italic\_u italic\_n italic\_k start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT , … , italic\_c italic\_h italic\_u italic\_n italic\_k start\_POSTSUBSCRIPT italic\_k end\_POSTSUBSCRIPT are the text chunks closest to the qa⁢d⁢vsubscript𝑞𝑎𝑑𝑣q\_{adv}italic\_q start\_POSTSUBSCRIPT italic\_a italic\_d italic\_v end\_POSTSUBSCRIPT vector in D𝐷Ditalic\_D.

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | dist⁢(eqa⁢d⁢v,ec⁢h⁢u⁢n⁢ki)⁢ is in the top⁢k.distsubscript𝑒subscript𝑞𝑎𝑑𝑣subscript𝑒𝑐ℎ𝑢𝑛subscript𝑘𝑖 is in the top𝑘\\text{dist}(e\_{q\_{adv}},e\_{chunk\_{i}})\\text{ is in the top}\\,\ k.dist ( italic\_e start\_POSTSUBSCRIPT italic\_q start\_POSTSUBSCRIPT italic\_a italic\_d italic\_v end\_POSTSUBSCRIPT end\_POSTSUBSCRIPT , italic\_e start\_POSTSUBSCRIPT italic\_c italic\_h italic\_u italic\_n italic\_k start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT end\_POSTSUBSCRIPT ) is in the top italic\_k . |  |

Chunks Extraction. When LLMs generate content, their inherent uncertainty can lead to inadvertent leakage of chunks from private knowledge bases, embedded in various forms within responses. Accurately identifying and extracting these sensitive chunks is essential for enabling subsequent automated attacks. The RAG-Thief agent excels at analyzing and extracting relevant knowledge base chunks within RAG applications. To streamline this process, RAG-Thief first removes redundant prompts from responses to simplify the analysis. It then applies carefully crafted regular expressions to precisely match and extract core content, efficiently isolating specific private knowledge chunks. This approach not only improves the detection capabilities of RAG-Thief but also provides a solid foundation for further security research. This process can be represented as:

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | c⁢h⁢u⁢n⁢k⁢s=ChunksExtraction⁢(r⁢e⁢s⁢p⁢o⁢n⁢s⁢e)𝑐ℎ𝑢𝑛𝑘𝑠ChunksExtraction𝑟𝑒𝑠𝑝𝑜𝑛𝑠𝑒chunks=\\text{ChunksExtraction}(response)italic\_c italic\_h italic\_u italic\_n italic\_k italic\_s = ChunksExtraction ( italic\_r italic\_e italic\_s italic\_p italic\_o italic\_n italic\_s italic\_e ) |  |

Memory Storage. In the memory storage phase, RAG-Thief’s storage mechanism saves the successfully extracted text chunks. Specifically, RAG-Thief maintains two memory areas: a short-term memory area and a long-term memory area. The short-term memory area stores newly extracted text chunks, i.e., those not previously extracted in earlier attack rounds. The long-term memory area stores all extracted text chunks.
Initially, the short-term memory area contains only initial adversarial query. As RAG-Thief processes the data leaked by the LLM, it extracts source text chunks and checks whether each chunk already exists in the long-term memory area. It is ignored if a text chunk is already present in the long-term memory. If it is a newly extracted text chunk, it is added to both the short-term and long-term memory areas. Let Smemorysubscript𝑆memoryS\_{\\text{memory}}italic\_S start\_POSTSUBSCRIPT memory end\_POSTSUBSCRIPT represent the short-term memory area and Lmemorysubscript𝐿memoryL\_{\\text{memory}}italic\_L start\_POSTSUBSCRIPT memory end\_POSTSUBSCRIPT represent the long-term memory area. Given c⁢h⁢u⁢n⁢k∈c⁢h⁢u⁢n⁢k⁢s⁢and⁢c⁢h⁢u⁢n⁢k∉Lmemory𝑐ℎ𝑢𝑛𝑘𝑐ℎ𝑢𝑛𝑘𝑠and𝑐ℎ𝑢𝑛𝑘subscript𝐿memorychunk\\,\\in\ chunks\\,\ \\text{and}\\,\ chunk\\,\ \\notin\\,\ L\_{\\text{memory}}italic\_c italic\_h italic\_u italic\_n italic\_k ∈ italic\_c italic\_h italic\_u italic\_n italic\_k italic\_s and italic\_c italic\_h italic\_u italic\_n italic\_k ∉ italic\_L start\_POSTSUBSCRIPT memory end\_POSTSUBSCRIPT, the basic process can be described as follows:

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | Smemory.put⁢(c⁢h⁢u⁢n⁢k)Smemory.put𝑐ℎ𝑢𝑛𝑘\\text{$S\_{\\text{memory}}$.put}(chunk)italic\_S start\_POSTSUBSCRIPT memory end\_POSTSUBSCRIPT .put ( italic\_c italic\_h italic\_u italic\_n italic\_k ) |  |

|     |     |     |
| --- | --- | --- |
|  | Lmemory.put⁢(c⁢h⁢u⁢n⁢k)Lmemory.put𝑐ℎ𝑢𝑛𝑘\\text{$L\_{\\text{memory}}$.put}(chunk)italic\_L start\_POSTSUBSCRIPT memory end\_POSTSUBSCRIPT .put ( italic\_c italic\_h italic\_u italic\_n italic\_k ) |  |

Reflection Mechanism. The reflection mechanism in RAG-Thief involves retrieving a chunk from short-term memory and using it as a seed to generate new adversarial queries, which are then applied to continue querying the RAG application. In each iteration, RAG-Thief utilizes reflective reasoning to develop increasingly targeted queries, building on its ability to associate and expand previously extracted content. Analyzing the extracted content, RAG-Thief iteratively prompts the LLM to disclose additional text chunks. The basic process is outlined as follows:

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | c⁢h⁢u⁢n⁢k=Smemory.get()𝑐ℎ𝑢𝑛𝑘Smemory.get()chunk=\\text{$S\_{\\text{memory}}$.get()}italic\_c italic\_h italic\_u italic\_n italic\_k = italic\_S start\_POSTSUBSCRIPT memory end\_POSTSUBSCRIPT .get() |  |

|     |     |     |
| --- | --- | --- |
|  | qa⁢d⁢v=Reflection⁢(c⁢h⁢u⁢n⁢k)subscript𝑞𝑎𝑑𝑣Reflection𝑐ℎ𝑢𝑛𝑘q\_{adv}=\\text{Reflection}(chunk)italic\_q start\_POSTSUBSCRIPT italic\_a italic\_d italic\_v end\_POSTSUBSCRIPT = Reflection ( italic\_c italic\_h italic\_u italic\_n italic\_k ) |  |

The complete attack flow of RAG-Thief is shown in Algorithm 1.

Report issue for preceding element

Algorithm 1 Algorithmic Description of RAG-Thief

0:  Initial Adversarial Query qa⁢d⁢vsubscript𝑞𝑎𝑑𝑣q\_{adv}italic\_q start\_POSTSUBSCRIPT italic\_a italic\_d italic\_v end\_POSTSUBSCRIPT, RAG application R𝑅Ritalic\_R

0:  Extracted private text chunks

1:  Initialize short-term memory Smemorysubscript𝑆memoryS\_{\\text{memory}}italic\_S start\_POSTSUBSCRIPT memory end\_POSTSUBSCRIPT with a initial adversarial query qa⁢d⁢vsubscript𝑞𝑎𝑑𝑣q\_{adv}italic\_q start\_POSTSUBSCRIPT italic\_a italic\_d italic\_v end\_POSTSUBSCRIPT

2:  Initialize long-term memory Lmemorysubscript𝐿memoryL\_{\\text{memory}}italic\_L start\_POSTSUBSCRIPT memory end\_POSTSUBSCRIPT as empty

3:while Attack is not terminated do

4:c⁢h⁢u⁢n⁢k𝑐ℎ𝑢𝑛𝑘chunkitalic\_c italic\_h italic\_u italic\_n italic\_k←←\\leftarrow←Smemorysubscript𝑆memoryS\_{\\text{memory}}italic\_S start\_POSTSUBSCRIPT memory end\_POSTSUBSCRIPT.get()

5:if context = qa⁢d⁢vsubscript𝑞𝑎𝑑𝑣q\_{adv}italic\_q start\_POSTSUBSCRIPT italic\_a italic\_d italic\_v end\_POSTSUBSCRIPTthen

6:qa⁢d⁢vsubscript𝑞𝑎𝑑𝑣q\_{adv}italic\_q start\_POSTSUBSCRIPT italic\_a italic\_d italic\_v end\_POSTSUBSCRIPT←←\\leftarrow←c⁢h⁢u⁢n⁢k𝑐ℎ𝑢𝑛𝑘chunkitalic\_c italic\_h italic\_u italic\_n italic\_k

7:else

8:qa⁢d⁢vsubscript𝑞𝑎𝑑𝑣q\_{adv}italic\_q start\_POSTSUBSCRIPT italic\_a italic\_d italic\_v end\_POSTSUBSCRIPT←←\\leftarrow← Reflection(c⁢h⁢u⁢n⁢k𝑐ℎ𝑢𝑛𝑘chunkitalic\_c italic\_h italic\_u italic\_n italic\_k)

9:endif

10:r⁢e⁢s⁢p⁢o⁢n⁢s⁢e𝑟𝑒𝑠𝑝𝑜𝑛𝑠𝑒responseitalic\_r italic\_e italic\_s italic\_p italic\_o italic\_n italic\_s italic\_e←←\\leftarrow←R𝑅Ritalic\_R.ChatLLM(qa⁢d⁢vsubscript𝑞𝑎𝑑𝑣q\_{adv}italic\_q start\_POSTSUBSCRIPT italic\_a italic\_d italic\_v end\_POSTSUBSCRIPT)

11:c⁢h⁢u⁢n⁢k⁢s𝑐ℎ𝑢𝑛𝑘𝑠chunksitalic\_c italic\_h italic\_u italic\_n italic\_k italic\_s←←\\leftarrow← ChunksExtraction(r⁢e⁢s⁢p⁢o⁢n⁢s⁢e𝑟𝑒𝑠𝑝𝑜𝑛𝑠𝑒responseitalic\_r italic\_e italic\_s italic\_p italic\_o italic\_n italic\_s italic\_e)

12:forn⁢e⁢w⁢\_⁢c⁢h⁢u⁢n⁢k𝑛𝑒𝑤\_𝑐ℎ𝑢𝑛𝑘new\\\_chunkitalic\_n italic\_e italic\_w \_ italic\_c italic\_h italic\_u italic\_n italic\_k in c⁢h⁢u⁢n⁢k⁢s𝑐ℎ𝑢𝑛𝑘𝑠chunksitalic\_c italic\_h italic\_u italic\_n italic\_k italic\_sdo

13:ifn⁢e⁢w⁢\_⁢c⁢h⁢u⁢n⁢k𝑛𝑒𝑤\_𝑐ℎ𝑢𝑛𝑘new\\\_chunkitalic\_n italic\_e italic\_w \_ italic\_c italic\_h italic\_u italic\_n italic\_k not in Lmemorysubscript𝐿memoryL\_{\\text{memory}}italic\_L start\_POSTSUBSCRIPT memory end\_POSTSUBSCRIPTthen

14:Smemorysubscript𝑆memoryS\_{\\text{memory}}italic\_S start\_POSTSUBSCRIPT memory end\_POSTSUBSCRIPT.put(n⁢e⁢w⁢\_⁢c⁢h⁢u⁢n⁢k𝑛𝑒𝑤\_𝑐ℎ𝑢𝑛𝑘new\\\_chunkitalic\_n italic\_e italic\_w \_ italic\_c italic\_h italic\_u italic\_n italic\_k)

15:Lmemorysubscript𝐿memoryL\_{\\text{memory}}italic\_L start\_POSTSUBSCRIPT memory end\_POSTSUBSCRIPT.put(n⁢e⁢w⁢\_⁢c⁢h⁢u⁢n⁢k𝑛𝑒𝑤\_𝑐ℎ𝑢𝑛𝑘new\\\_chunkitalic\_n italic\_e italic\_w \_ italic\_c italic\_h italic\_u italic\_n italic\_k)

16:endif

17:endfor

18:endwhile

19:returnLmemorysubscript𝐿memoryL\_{\\text{memory}}italic\_L start\_POSTSUBSCRIPT memory end\_POSTSUBSCRIPT

Report issue for preceding elementReport issue for preceding element

### 4.2 Constructing Initial Adversarial Query

Report issue for preceding element

In the absence of background knowledge about the private knowledge base, attackers can only interact with the RAG application by posing random queries and observing the LLM’s responses. Once the LLM references text chunks from the private knowledge base in its responses, attackers can use this as a foundation to construct an initial adversarial query template.

Report issue for preceding element

We design an initial adversarial query template, which consists of two main components: the anchor query and the adversarial command, expressed as:

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | qa⁢d⁢v={a⁢n⁢c⁢h⁢o⁢r⁢q⁢u⁢e⁢r⁢y}+{a⁢d⁢v⁢e⁢r⁢s⁢a⁢r⁢i⁢a⁢l⁢c⁢o⁢m⁢m⁢a⁢n⁢d}subscript𝑞𝑎𝑑𝑣𝑎𝑛𝑐ℎ𝑜𝑟𝑞𝑢𝑒𝑟𝑦𝑎𝑑𝑣𝑒𝑟𝑠𝑎𝑟𝑖𝑎𝑙𝑐𝑜𝑚𝑚𝑎𝑛𝑑q\_{adv}=\\{anchor\ query\\}+\\{adversarial\ command\\}italic\_q start\_POSTSUBSCRIPT italic\_a italic\_d italic\_v end\_POSTSUBSCRIPT = { italic\_a italic\_n italic\_c italic\_h italic\_o italic\_r italic\_q italic\_u italic\_e italic\_r italic\_y } + { italic\_a italic\_d italic\_v italic\_e italic\_r italic\_s italic\_a italic\_r italic\_i italic\_a italic\_l italic\_c italic\_o italic\_m italic\_m italic\_a italic\_n italic\_d } |  |

In the initial adversarial query, the anchor query can be random, as the focus is on the adversarial command, which aims to induce the LLM to reveal system prompt content that includes retrieved text chunks. If any clues about the private knowledge base are obtained during this process, they can replace the anchor query to enhance the precision and effectiveness of subsequent attacks.

Report issue for preceding element

For the adversarial command, we employ a guided strategy aimed at encouraging the model to reveal more detailed information during the conversation. By leveraging the LLM’s reasoning capabilities, these adversarial commands are designed to prompt the model to expose more underlying text content during generation. We develop several prompt injection attack templates for this purpose. Once a specific adversarial query successfully induces the LLM to leak information, the same adversarial prompt will be used in subsequent queries to continue the adversarial attack.

Report issue for preceding element

The RAG-Thief system includes a variety of prompt injection attack templates, such as the ignore attack. These templates are carefully designed to effectively induce the LLM to output information from the private knowledge base in different scenarios. By continuously refining and optimizing these templates, RAG-Thief is able to probe and bypass the LLM’s security boundaries, enabling more effective attacks.

Report issue for preceding element

This initial adversarial query establishes a foundation for the attack, providing a critical framework for guiding future adversarial queries. This process serves as the starting point for RAG-Thief’s attack, with subsequent queries evolving and optimizing based on the success of the initial attack.

Report issue for preceding element

### 4.3 Generating New Adversarial Queries

Report issue for preceding element

In generating adversarial queries, each query consists of two essential components: an anchor query and an adversarial command. The adversarial command uses templates derived from a previously successful initial adversarial query, while the anchor query serves to retrieve relevant text chunks from the vector database. To maximize the retrieval of new, previously unretrieved text chunks from the private knowledge base, the anchor query must be closely aligned with the content of the private knowledge base.

Report issue for preceding element

The anchor query’s design is crucial, as it must encompass key topics likely contained within the private knowledge base while retaining adaptability across various contexts. This adaptability allows RAG-Thief to effectively capture new information, thereby enhancing the success rate of information extraction. We employ two main strategies for generating anchor queries:

Report issue for preceding element

Leveraging Overlapping Segments:
When creating a vector retrieval database for a private knowledge base, the original text is typically divided into multiple fixed-length chunks. To ensure continuity of context, a certain overlap length n𝑛nitalic\_n is often maintained between adjacent chunks. This means that the first n𝑛nitalic\_n characters of one chunk are identical to the last n𝑛nitalic\_n characters of the previous chunk, and its last n𝑛nitalic\_n characters match the beginning of the following chunk. In practice, the actual overlap length may be less than n𝑛nitalic\_n to preserve the integrity of overlapping sentences.

Report issue for preceding element

By identifying and leveraging these overlapping sections, RAG-Thief can generate new adversarial queries. For example, it can construct anchor queries by extracting a few characters from the beginning and end of an extracted chunk. This approach significantly increases the likelihood of matching adjacent chunks, effectively expanding the scope of data extraction while minimizing unnecessary query attempts.

Report issue for preceding element

Extended Query Generation:
Relying solely on overlapping text chunks to generate adversarial queries is not always effective, especially in some RAG applications where overlapping between chunks is not guaranteed. To address this, we design an inference and extension mechanism for RAG-Thief, enabling it to generate more effective anchor queries based on previously extracted text chunks, thereby increasing the likelihood of retrieving new chunks.

Report issue for preceding element

Specifically, RAG-Thief extends successfully extracted text chunks both forward and backward, generating extended content of at least 1000 tokens per iteration. It performs multiple forward and backward expansions, ensuring variation in each extension. These extended text segments are then used as new anchor queries for constructing new adversarial queries. Through this strategy, even with limited knowledge of the private knowledge base, RAG-Thief can construct more targeted queries, allowing it to capture additional, previously unretrieved text chunks and enhancing extraction comprehensiveness and efficiency.

Report issue for preceding element

By combining these two strategies, the system can continuously generate heuristic adversarial queries until attack termination conditions are met, such as reaching a specified number of attacks or a designated attack duration. Compared to randomly generated queries, this method, which is based on intrinsic textual associations, significantly improves hit rates. Additionally, we evaluate the retrieval efficiency of each newly generated query question: if a new question successfully retrieves more new text segments, the system further employs associative LLMs to generate more related queries based on that question, maximizing the scope of information extraction.

Report issue for preceding element

Through the integration of these strategies, RAG-Thief reduces the number of queries while increasing the success rate of retrieving unknown text segments, achieving more efficient automated information extraction.

Report issue for preceding element

### 4.4 Addressing Output Uncertainty in LLMs

Report issue for preceding element

Due to the generative nature of LLMs, their outputs are often unpredictable. Even when responding to the same query, LLMs may produce responses that vary significantly in style or format. This unpredictability poses challenges for accurately identifying and extracting private knowledge base content during automated attack processes, particularly when it comes to isolating specific original chunks from the generated responses. Therefore, a critical task in constructing the automated RAG-Thief workflow is the precise identification of target chunks within LLM outputs. To address this, we optimize the design of adversarial queries, aiming to prompt the LLM to return the original retrieved text chunks as directly as possible, without modifications or paraphrasing.

Report issue for preceding element

Our approach involves analyzing the structure of LLM-generated text and developing tailored regular expressions to match varying output formats. These regular expressions are designed to identify and extract text chunks that correspond to the private knowledge base, thereby improving the accuracy of source text chunk identification throughout the attack process. This strategy not only addresses the variability in LLM outputs but also enhances the system’s stability and consistency under different query conditions. By continuously refining the adversarial query instructions, we can effectively mitigate response uncertainty, ensuring that extracted content remains as accurate as possible.

Report issue for preceding element

To be specific, we implement a post-processing mechanism that uses a parsing function for LLM response interpretation. This function utilizes regular expressions to match specific text formats and accurately extract relevant chunks, facilitating the reconstruction of original content from the private knowledge base. This post-processing mechanism reduces the negative impact of output variability on the attack workflow and establishes a robust foundation for subsequent analysis and utilization of the extracted data.

Report issue for preceding element

In summary, by optimizing adversarial queries and introducing a post-processing mechanism, we significantly improve RAG-Thief’s performance in handling LLM output uncertainty. This approach ensures that even in the face of LLM output variability, the original content from private knowledge bases can be extracted accurately and efficiently, thereby enhancing the overall effectiveness and success rate of the attack.

Report issue for preceding element

### 4.5 Self-Improvement Mechanism

Report issue for preceding element

When conducting automated attacks on a RAG system, the black-box nature of the system introduces significant challenges, as attackers cannot access intermediate results, making it difficult to process and analyze extracted text, especially when multiple chunks need to be linked for deeper analysis. Efficiently leveraging previously extracted data to generate new value is critical to overcoming this limitation. The RAG-Thief agent addresses this by employing a heuristic self-improvement mechanism that uses extracted contextual information to generate new query questions. This approach enhances query hit rates, improves the efficiency of retrieving additional text chunks, and significantly increases the overall success rate of the attack.

Report issue for preceding element

Specifically, the RAG-Thief agent deeply analyzes the extracted chunks across multiple dimensions, including grammar, semantics, structure, context, dialogue, entities, and more. This comprehensive analysis enables the agent to fully understand the underlying logic and meaning of the extracted text. Based on this understanding, the agent performs reasoning and expansion on the extracted text.
Given that LLMs excel at reasoning, the RAG-Thief agent leverages this capability to generate more targeted queries by reasoning and expanding on the extracted text chunks. This self-improvement mechanism not only maximizes the value of the extracted data but also increases the efficiency of retrieving additional useful information, thereby enhancing the overall success rate of the attack.

Report issue for preceding element

The key advantage of this strategy lies in the agent’s ability to reason and extend the extracted text chunks, maximizing its utility and adding continuity and depth to the attack process. This approach not only improves query hit rates but also enables the agent to proactively generate targeted exploratory paths when encountering unknown information, further increasing the effectiveness of the attack.

Report issue for preceding element

## 5 Evaluation and Analysis

Report issue for preceding element

### 5.1 Evaluation Setups

Report issue for preceding element

Scenarios and Datasets. To reflect the real-world threats, we evaluate the effectiveness of our attack on RAG applications spanning healthcare, document understanding and personal assistant. Due to ethical reasons, we use open-sourced datasets from relevant domains to simulate the private data in RAG applications. Specifically, we use the following three datasets as retrieval databases: the Enron Email dataset with 500k employee emails \[ [36](https://arxiv.org/html/2411.14110v1#bib.bib36 "")\], the HealthCareMagic-100k-en-101 dataset (abbrev. HealthCareMagic) \[ [37](https://arxiv.org/html/2411.14110v1#bib.bib37 "")\] with 100k doctor-patient records, and Harry Potter and the Sorcerer’s Stone (abbrev. Harry Potter) \[ [38](https://arxiv.org/html/2411.14110v1#bib.bib38 "")\]. We select subsets from each dataset: 149,417 words from the Enron Email dataset, 109,128 words from the HealthCareMagic dataset, and the first five chapters of Harry Potter, totaling 124,141 words.
More details are shown in Table [I](https://arxiv.org/html/2411.14110v1#S5.T1 "TABLE I ‣ 5.1 Evaluation Setups ‣ 5 Evaluation and Analysis ‣ RAG-Thief: Scalable Extraction of Private Data from Retrieval-Augmented Generation Applications with Agent-based Attacks").

Report issue for preceding element

TABLE I: Scenario Overview

| Scenario | Dataset | Tokens |
| --- | --- | --- |
| Healthcare | HealthCareMagic \[ [37](https://arxiv.org/html/2411.14110v1#bib.bib37 "")\] | 25k |
| Personal Assistant | Enron Email \[ [36](https://arxiv.org/html/2411.14110v1#bib.bib36 "")\] | 47k |
| Document Understanding | Harry Potter \[ [38](https://arxiv.org/html/2411.14110v1#bib.bib38 "")\] | 31k |

Report issue for preceding element

Construction of Target RAG Applications.
To systematically evaluate the performance of our RAG-Thief agent, we use the LangChain framework to set up a local RAG application experimental environment with different base LLMs in the RAG applications. In the local RAG application environment, the generator LLM component is configured with ChatGPT-4, Qwen2-72B-Instruct, and GLM-4-Plus, covering the most popular commercial and open-source models. These models are widely recommended by platforms as ideal foundation models for building RAG applications due to their performance and versatility. For retrieval, we select the embedding model nlp\_corom\_sentence-embedding\_english-base, chosen for its top-10 ranking in overall downloads and its position as the most downloaded English sentence embedding model on the ModelScope platform.
In selecting the foundation model for the RAG-Thief agent, we chose Qwen2-1.5B-Instruct. This open-source model offers strong inference performance and requires minimal resources, making it easy to deploy and operate efficiently.

Report issue for preceding element

These configurations allow for a comprehensive assessment of RAG-Thief’s performance across different models and knowledge base types, facilitating an in-depth examination of its impact on data privacy and security.

Report issue for preceding element

In our local RAG application experimental setup, the number of retrieved text chunks k𝑘kitalic\_k is set to 3. The external retrieval knowledge base is constructed following best practices, with a maximum chunk length of 1500 words and a maximum overlap of 300 words, as recommended by platforms such as Coze. Under these settings, the text data in each of the three knowledge bases is uniformly divided into 100 chunks, ensuring higher coverage and precision during retrieval. We also study how these factors influence the attack performance in the ablation studies (Section [5.6](https://arxiv.org/html/2411.14110v1#S5.SS6 "5.6 Ablation Studies ‣ 5 Evaluation and Analysis ‣ RAG-Thief: Scalable Extraction of Private Data from Retrieval-Augmented Generation Applications with Agent-based Attacks")).

Report issue for preceding element

Evaluation Metrics.
To evaluate the effectiveness of the RAG-Thief agent in knowledge base extraction tasks, we select key metrics to comprehensively assess its performance.

Report issue for preceding element

- •


Chunk Recovery Rate (abbrev. CRR). CRR is a primary metric for evaluating attack efficacy, reflecting RAG-Thief’s ability to retrieve complete data chunks from the target knowledge base. The CRR score directly indicates how well RAG-Thief reconstructs the original knowledge base, serving as a critical measure of attack success.

Report issue for preceding element

- •


Semantic Similarity (abbrev. SS). SS ranges from −11-1\- 1 to 1111, with higher values indicating greater semantic similarity. SS measures the semantic distance between the reconstructed target system prompt and the original prompt in the knowledge base, using cosine similarity of embedding vectors transformed by a sentence encoder \[ [39](https://arxiv.org/html/2411.14110v1#bib.bib39 "")\].
The core formula for SS is as follows:

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | SS⁢(S,T)=ES→⋅ET→‖ES→‖⋅‖ET→‖SS𝑆𝑇⋅→subscript𝐸𝑆→subscript𝐸𝑇⋅norm→subscript𝐸𝑆norm→subscript𝐸𝑇\\text{SS}(S,T)=\\frac{\\overrightarrow{E\_{S}}\\cdot\\overrightarrow{E\_{T}}}{\\\|%<br>\\overrightarrow{E\_{S}}\\\|\\cdot\\\|\\overrightarrow{E\_{T}}\\\|}SS ( italic\_S , italic\_T ) = divide start\_ARG over→ start\_ARG italic\_E start\_POSTSUBSCRIPT italic\_S end\_POSTSUBSCRIPT end\_ARG ⋅ over→ start\_ARG italic\_E start\_POSTSUBSCRIPT italic\_T end\_POSTSUBSCRIPT end\_ARG end\_ARG start\_ARG ∥ over→ start\_ARG italic\_E start\_POSTSUBSCRIPT italic\_S end\_POSTSUBSCRIPT end\_ARG ∥ ⋅ ∥ over→ start\_ARG italic\_E start\_POSTSUBSCRIPT italic\_T end\_POSTSUBSCRIPT end\_ARG ∥ end\_ARG |  | (1) |



where ES→→subscript𝐸𝑆\\overrightarrow{E\_{S}}over→ start\_ARG italic\_E start\_POSTSUBSCRIPT italic\_S end\_POSTSUBSCRIPT end\_ARG and ET→→subscript𝐸𝑇\\overrightarrow{E\_{T}}over→ start\_ARG italic\_E start\_POSTSUBSCRIPT italic\_T end\_POSTSUBSCRIPT end\_ARG are the embedding vectors of the extracted chunk S𝑆Sitalic\_S and the target source chunk T𝑇Titalic\_T, respectively, and ‖ES→‖norm→subscript𝐸𝑆\\\|\\overrightarrow{E\_{S}}\\\|∥ over→ start\_ARG italic\_E start\_POSTSUBSCRIPT italic\_S end\_POSTSUBSCRIPT end\_ARG ∥ and ‖ET→‖norm→subscript𝐸𝑇\\\|\\overrightarrow{E\_{T}}\\\|∥ over→ start\_ARG italic\_E start\_POSTSUBSCRIPT italic\_T end\_POSTSUBSCRIPT end\_ARG ∥ denote their respective norms.
This metric reflects the semantic accuracy of the reconstructed text, providing a validation of the attack’s effectiveness at the semantic level.

Report issue for preceding element

- •


Extended Edit Distance (abbrev. EED). The EED ranges from 00 to 1111, with 00 indicating higher similarity \[ [40](https://arxiv.org/html/2411.14110v1#bib.bib40 "")\].
EED measures the minimum number of Levenshtein edit operations required to transform the reconstructed text chunk into its corresponding source chunk in the knowledge base. The core formula for EED can be expressed as follows:

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | EED⁢(S,T)=Levenshtein⁢(S,T)max⁡(\|S\|,\|T\|)EED𝑆𝑇Levenshtein𝑆𝑇𝑆𝑇\\text{EED}(S,T)=\\frac{\\text{Levenshtein}(S,T)}{\\max(\|S\|,\|T\|)}EED ( italic\_S , italic\_T ) = divide start\_ARG Levenshtein ( italic\_S , italic\_T ) end\_ARG start\_ARG roman\_max ( \| italic\_S \| , \| italic\_T \| ) end\_ARG |  | (2) |



where S𝑆Sitalic\_S and T𝑇Titalic\_T are the extracted chunk and the target source chunk.
This metric evaluates RAG-Thief’s fidelity in literal reproduction, aiding in assessing whether the agent performs a near-verbatim copy of the target content.

Report issue for preceding element


These evaluation metrics allow us to analyze RAG-Thief’s reconstruction accuracy and data extraction efficiency from multiple perspectives, offering targeted insights for enhancing data privacy protections in RAG systems.

Report issue for preceding element

Other Detailed Setups. During the inference process, the RAG-Thief agent performs forward and backward reasoning based on historical information. It is instructed to generate five forward and five backward continuations, resulting in a total of 10 distinct inferred segments. Each continuation is required to contain at least 1000 tokens, with a focus on maximizing content variation across generations.

Report issue for preceding element

Baseline.
We compare RAG-Thief with the attack method proposed by Qi et al.\[ [18](https://arxiv.org/html/2411.14110v1#bib.bib18 "")\], evaluate knowledge base reconstruction by generating random query sets, relying on Prompt-Injection Data Extraction (PIDE), which they categorize into two types: targeted attack and untargeted attack. In targeted attacks, the attacker has prior knowledge of the knowledge base’s domain and generates queries closely related to its content using GPT. In untargeted attacks, lacking specific domain knowledge, the attacker uses GPT to generate general queries to test reconstruction capabilities.

Report issue for preceding element

To ensure fairness, we strictly replicate the experimental procedures of Qi et al. \[ [18](https://arxiv.org/html/2411.14110v1#bib.bib18 "")\] as a baseline, allowing a systematic evaluation of RAG-Thief’s performance across various attack scenarios. This comparison helps to validate RAG-Thief’s strengths and limitations in different attack contexts.

Report issue for preceding element

### 5.2 Summary of Results

Report issue for preceding element

We highlight some experimental findings below.

Report issue for preceding element

- •


Effectiveness: RAG-Thief demonstrates strong effectiveness, achieving notable results in both simulated local RAG test environments and real-world platforms, validating the viability of this attack approach.

Report issue for preceding element

- •


Robustness: RAG-Thief exhibits high cross-platform adaptability across diverse RAG applications, handling multiple types of LLMs, datasets, and platform configurations. This shows its capability to perform reliable attacks in various RAG environments.

Report issue for preceding element

- •


Efficiency: RAG-Thief achieves better extraction results with fewer attack attempts, highlighting its advantage in optimizing attack efficiency.

Report issue for preceding element


TABLE II: Comparison of CRR for RAG-Thief and PIDE (baseline) on local RAG applications across various datasets and base LLMs within 200 attack queries.

| Datasets | Model | RAG-Thief | PIDE\[ [18](https://arxiv.org/html/2411.14110v1#bib.bib18 "")\] |
| --- | --- | --- | --- |
| Untargeted Attack | Targeted Attack | Untargeted Attack | Targeted Attack |
| --- | --- | --- | --- |
| HealthCareMagic | ChatGPT-4 | 51% | 54% | 19% | 23% |
| Qwen2-72B-Instruct | 54% | 57% | 17% | 19% |
| GLM-4-Plus | 51% | 55% | 17% | 21% |
| Enron Email | ChatGPT-4 | 58% | 60% | 16% | 16% |
| Qwen2-72B-Instruct | 52% | 58% | 18% | 17% |
| GLM-4-Plus | 53% | 56% | 17% | 17% |
| Harry Potter | ChatGPT-4 | 69% | 77% | 9% | 35% |
| Qwen2-72B-Instruct | 73% | 79% | 9% | 30% |
| GLM-4-Plus | 70% | 75% | 8% | 32% |

Report issue for preceding element

### 5.3 Effectiveness of Untargeted Attack

Report issue for preceding element

Experimental Settings.
In the untargeted attack experiments, the RAG-Thief agent relies on its ability to analyze previously extracted chunks, generating plausible contextual content through inference to incrementally expand its understanding and reconstruction of the target knowledge base.
To facilitate this, we design a specialized prompt for the RAG-Thief agent, guiding it to perform an in-depth analysis of the extracted chunks. This analysis includes examining key details such as themes, structure, text format, characters, dialogue style, and temporal context. By leveraging these insights, the RAG-Thief agent infers preceding and subsequent content, effectively expanding information coverage even in the absence of specific domain knowledge.

Report issue for preceding element

TABLE III: Performance of RAG-Thief on local RAG applications across various different datasets and base LLMs.

| Datasets | Model | RAG-Thief |
| --- | --- | --- |
| SS | EED |
| --- | --- |
| HealthCareMagic | ChatGPT-4 | 1 | 0.027 |
| Qwen2-72B-Instruct | 1 | 0.022 |
| GLM-4-Plus | 1 | 0.013 |
| Enron Email | ChatGPT-4 | 1 | 0.034 |
| Qwen2-72B-Instruct | 1 | 0.049 |
| GLM-4-Plus | 1 | 0.045 |
| Harry Potter | ChatGPT-4 | 1 | 0.038 |
| Qwen2-72B-Instruct | 1 | 0.036 |
| GLM-4-Plus | 1 | 0.039 |

Report issue for preceding element

Results & Analysis. The experimental results are shown in Tables [II](https://arxiv.org/html/2411.14110v1#S5.T2 "TABLE II ‣ 5.2 Summary of Results ‣ 5 Evaluation and Analysis ‣ RAG-Thief: Scalable Extraction of Private Data from Retrieval-Augmented Generation Applications with Agent-based Attacks") and [III](https://arxiv.org/html/2411.14110v1#S5.T3 "TABLE III ‣ 5.3 Effectiveness of Untargeted Attack ‣ 5 Evaluation and Analysis ‣ RAG-Thief: Scalable Extraction of Private Data from Retrieval-Augmented Generation Applications with Agent-based Attacks"). Table [II](https://arxiv.org/html/2411.14110v1#S5.T2 "TABLE II ‣ 5.2 Summary of Results ‣ 5 Evaluation and Analysis ‣ RAG-Thief: Scalable Extraction of Private Data from Retrieval-Augmented Generation Applications with Agent-based Attacks") presents chunk recovery rates as a measure of attack effectiveness. Results indicate that our attack method significantly outperforms the baseline in untargeted scenarios, achieving an average increase in recovery rate of approximately threefold. This trend is consistent across the three tested models, suggesting similar compliance with directives under these experimental conditions. Furthermore, when using the HealthCareMagic and Enron Email datasets as knowledge bases, the chunk recovery rates are comparable; however, they are about 28% lower than those achieved with the Harry Potter knowledge base. It is noteworthy that the HealthCareMagic and Enron Email datasets consist of discrete, loosely related segments, whereas Harry Potter, as a continuous narrative, features fixed characters and locations with more coherent story progression. This demonstrates that the RAG-Thief agent performs better with datasets containing continuous content, aligning with the known strengths of LLMs in inference and text continuation tasks.

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2411.14110v1/x3.png)Figure 3: Comparison of the growth in CRR between RAG-Thief and PIDE over 200 attack queries.Report issue for preceding element

Fig. [3](https://arxiv.org/html/2411.14110v1#S5.F3 "Figure 3 ‣ 5.3 Effectiveness of Untargeted Attack ‣ 5 Evaluation and Analysis ‣ RAG-Thief: Scalable Extraction of Private Data from Retrieval-Augmented Generation Applications with Agent-based Attacks") shows that RAG-Thief’s CRR exhibits a steady upward trend as the number of attack queries increases, leveling off around 200 queries. In contrast, PIDE’s CRR grows slowly and nearly stagnates after 100 queries, remaining at a relatively low level. These results indicate that RAG-Thief demonstrates stronger recovery capabilities in response to iterative attack queries, while PIDE shows clear limitations under the same conditions.

Report issue for preceding element

Table [III](https://arxiv.org/html/2411.14110v1#S5.T3 "TABLE III ‣ 5.3 Effectiveness of Untargeted Attack ‣ 5 Evaluation and Analysis ‣ RAG-Thief: Scalable Extraction of Private Data from Retrieval-Augmented Generation Applications with Agent-based Attacks") provides SS and EED between recovered and original text chunks, effectively assessing the recovery quality of the RAG-Thief agent. The results show that RAG-Thief perform excellently on SS and EED metrics, with semantic similarity nearly reaching 1 and edit distance reflecting near-verbatim recovery. The EED all exceed 0 mainly due to minor punctuation errors. As shown below, we provide the content of the original text chunk and the GPTs’ response from the HealthCareMagic dataset, highlighting differences in punctuation. These results indicate that RAG-Thief can almost fully reconstruct the exact content from the private knowledge base, effectively enabling information theft.

Report issue for preceding element

Original Chunk”input”: ”I have a 5 month old baby who is very congested with a terrible cough. Its rattly/raspy and croupy sounding cough. She started choking on her coughs and the mucous that has come up. She also has a fever and runny nose. Should I take her to urgent care?”
”output”: ”Thank you for using Chat Doctor. I would suggest that you see your doctor. Your baby may be having bronchiolitis which is a lung infection common to your kids age. It is commonly caused by a virus. Albuterol via nebulization should be utilized in order to alleviate the wheezing and also help with the congestion. A decongestant can also be used for the colds. Also, it would also advise doing a chest X-ray in order to rule out other diseases (ex. pneumonia)sincerely, Mark RosarioGeneral pediatrics/Pediatric Pulmonology”Report issue for preceding element

Extracted Chunk from GPT-4’s ResponseInput: ”I have a 5-month-old baby who is very congested with a terrible cough. It’s rattly/raspy and croupy sounding cough. She started choking on her coughs and the mucus that has come up. She also has a fever and runny nose. Should I take her to urgent care?”
Output: ”Thank you for using Chat Doctor. I would suggest that you see your doctor. Your baby may be having bronchiolitis, which is a lung infection common to your kid’s age. It is commonly caused by a virus. Albuterol via nebulization should be utilized in order to alleviate the wheezing and also help with the congestion. A decongestant can also be used for the colds. Also, I would advise doing a chest X-ray in order to rule out other diseases (e.g., pneumonia). Sincerely, Mark Rosario, General pediatrics/Pediatric Pulmonology.”Report issue for preceding element

We design system prompt templates for RAG-Thief in untargeted attack scenarios to enhance its ability to analyze and infer given content while generating extended information to support subsequent queries. The detailed prompt template is provided in Appendix [A.1](https://arxiv.org/html/2411.14110v1#A1.SS1 "A.1 Prompts for Untargeted Attack ‣ Appendix A Details of Prompting the Attack LLM ‣ RAG-Thief: Scalable Extraction of Private Data from Retrieval-Augmented Generation Applications with Agent-based Attacks").

Report issue for preceding element

### 5.4 Effectiveness of Targeted Attacks

Report issue for preceding element

Experimental Settings. When limited knowledge base information is available, attackers can leverage this prior knowledge to refine RAG-Thief’s reasoning process, creating more targeted anchor queries. For example, in a RAG application containing medical conversations, if the private knowledge base is known to store confidential doctor-patient dialogues, RAG-Thief can simulate a professional medical practitioner during inference. This allows it to analyze critical aspects of the extracted content in greater depth, including medical principles, conversational context, diagnostic plans, treatments, and patient symptoms. Through this analysis, RAG-Thief can generate realistic new doctor-patient interaction scenarios and initiate query attacks within the RAG application to further extract knowledge base content.

Report issue for preceding element

Results & Analysis. The experimental results, shown in Tables [II](https://arxiv.org/html/2411.14110v1#S5.T2 "TABLE II ‣ 5.2 Summary of Results ‣ 5 Evaluation and Analysis ‣ RAG-Thief: Scalable Extraction of Private Data from Retrieval-Augmented Generation Applications with Agent-based Attacks") and [III](https://arxiv.org/html/2411.14110v1#S5.T3 "TABLE III ‣ 5.3 Effectiveness of Untargeted Attack ‣ 5 Evaluation and Analysis ‣ RAG-Thief: Scalable Extraction of Private Data from Retrieval-Augmented Generation Applications with Agent-based Attacks"), yield similar conclusions. In targeted attack scenarios, our method achieves a CRR approximately three times higher than the PIDE, with consistent results across the three models tested. Additionally, when using the HealthCareMagic and Enron Email datasets as knowledge bases, the chunks recovery rate is about 26% lower than with the Harry Potter dataset. This may be due to the more fragmented, non-continuous nature of the former datasets, while Harry Potter, as a narrative dataset, has stronger content continuity, enhancing the RAG-Thief agent’s recovery performance.

Report issue for preceding element

In terms of SS and EED, RAG-Thief demonstrate near-verbatim recovery, with SS close to 1 and minimal EED, indicating high fidelity in text recovery. However, the chunks recovery rate in targeted attacks is approximately 7% higher than in untargeted attacks. This suggests that relevant domain knowledge significantly improves the RAG-Thief agent’s recovery rate, highlighting the impact of domain-specific background information on attack success.

Report issue for preceding element

We also design a system prompt for RAG-Thief in targeted attack scenarios. The detailed prompt template is provided in Appendix [A.2](https://arxiv.org/html/2411.14110v1#A1.SS2 "A.2 Prompts for Targeted Attacks ‣ Appendix A Details of Prompting the Attack LLM ‣ RAG-Thief: Scalable Extraction of Private Data from Retrieval-Augmented Generation Applications with Agent-based Attacks").

Report issue for preceding element

### 5.5 Attacking Real-world RAG Applications

Report issue for preceding elementTABLE IV: Performance of RAG-Thief on real-world RAG applications from OpenAI’s GPTs and ByteDance’s Coze.

| Platform | Company | Datasets | CRR | SS | EED |
| --- | --- | --- | --- | --- | --- |
| GPTs | OpenAI | HarryPotty | 71% | 1 | 0.022 |
| HealthCareMagic | 77% | 1 | 0.021 |
| Coze | ByteDance | HarryPotty | 89% | 1 | 0.009 |
| HealthCareMagic | 83% | 1 | 0.019 |

Report issue for preceding element![Refer to caption](https://arxiv.org/html/2411.14110v1/x4.png)Figure 4: The CRR curve of RAG-Thief attacks in both targeted and untargeted scenarios with changes in (a) the number of retrieved chunks, (b) the agent base model size, and (c) the retrieval mode in the RAG applications.Report issue for preceding element

Experimental Settings. We conduct systematic attack experiments on real-world platforms, OpenAI’s GPTs and ByteDance’s Coze. We select the HealthCareMagic subset and the first five chapters of Harry Potter as external knowledge bases and upload them to the GPTs and Coze platforms.
We simulate attacks in an untargeted attack scenario.
For ethical reasons, we develop two custom RAG applications on each platform based on these knowledge bases to simulate different application scenarios across domains and content types.

Report issue for preceding element

In the experiments, we conduct 200 attack attempts on each custom RAG application using the RAG-Thief agent. Each attack began with an initial adversarial query, and RAG-Thief agent iteratively generated new queries based on model responses to maximize coverage of the text chunks within the knowledge bases. We record the proportion of successfully extracted text and compare extraction rates across platforms and knowledge base types.

Report issue for preceding element

Results & Analysis. The attack results, shown in Table [IV](https://arxiv.org/html/2411.14110v1#S5.T4 "TABLE IV ‣ 5.5 Attacking Real-world RAG Applications ‣ 5 Evaluation and Analysis ‣ RAG-Thief: Scalable Extraction of Private Data from Retrieval-Augmented Generation Applications with Agent-based Attacks"), indicate that the RAG-Thief agent achieved a substantial chunks extraction rate in RAG applications on both GPTs and Coze platforms, with a chunks recovery rate exceeding 70% on GPTs and over 80% on Coze. The data leakage rate on the Coze platform is approximately 16% higher on average than that of the GPTs platform. This difference may be attributed to the alignment mechanism employed by the GPTs platform, which helps mitigate some of the leakage effects.
Additionally, the SS and EED metrics on both platforms demonstrate that RAG-Thief nearly restores the original content verbatim. These real-world attack outcomes further underscore the potential threat of our attack method in practical application environments.

Report issue for preceding element

### 5.6 Ablation Studies

Report issue for preceding element

In this section, we conduct ablation studies to investigate various factors that may impact the chunk recovery rate from private knowledge bases. Specifically, we examine the effects of the number of returned text chunks per query k𝑘kitalic\_k, the base model size in the RAG-Thief agent, and the retrieval mode used in RAG applications on privacy leakage.

Report issue for preceding element

Returned Chunks. To analyze the impact of the number of text chunks k𝑘kitalic\_k retrieved per query on privacy leakage, we set k𝑘kitalic\_k to values of 1, 3, 5, 7, and 9, as shown in Fig. [4](https://arxiv.org/html/2411.14110v1#S5.F4 "Figure 4 ‣ 5.5 Attacking Real-world RAG Applications ‣ 5 Evaluation and Analysis ‣ RAG-Thief: Scalable Extraction of Private Data from Retrieval-Augmented Generation Applications with Agent-based Attacks")(a). In this experiment, we fix the LLM component of the RAG application as GLM-4-Plus, the RAG-Thief agent base model as Qwen2-1.5B-Instruct, and the dataset as HealthCareMagic, with a total of 200 attack attempts. Results indicate that with an increasing k𝑘kitalic\_k, both targeted and untargeted attacks retrieve significantly more text chunks, suggesting a higher risk of private data leakage as k𝑘kitalic\_k grows.
Notably, k=1𝑘1k=1italic\_k = 1 is not a common setting, as it significantly reduces the effectiveness of RAG applications \[ [3](https://arxiv.org/html/2411.14110v1#bib.bib3 "")\]. Thus, setting k=1𝑘1k=1italic\_k = 1 in our experiments serves only to observe trend variations; this configuration has minimal impact on real-world attack scenarios and does not substantially affect the overall feasibility or effectiveness of the attack.
Thus, a larger k𝑘kitalic\_k may elevate the probability of sensitive information being exposed.

Report issue for preceding element

Agent Base Model Size. To assess the effect of base model size in the RAG-Thief agent, we conduct experiments with different parameter sizes of the open-source Qwen2 series models, including Qwen2-0.5B, Qwen2-1.5B, Qwen2-7B, and Qwen2-72B, as shown in Fig. [4](https://arxiv.org/html/2411.14110v1#S5.F4 "Figure 4 ‣ 5.5 Attacking Real-world RAG Applications ‣ 5 Evaluation and Analysis ‣ RAG-Thief: Scalable Extraction of Private Data from Retrieval-Augmented Generation Applications with Agent-based Attacks")(b). In this setup, we fix the LLM component of the RAG application as Qwen2-72B-Instruct, the dataset as Enron Email, set k=3𝑘3k=3italic\_k = 3, and conduct 200 attack attempts. The results show that as the base model size increases, there is a slight increase in retrieved text chunks for both targeted and untargeted attacks. This suggests that larger model sizes enhance inference and text generation capabilities, but the effect on coverage of private knowledge base content remains limited.

Report issue for preceding element

Retrieval Mode. To investigate the effect of retrieval mode on privacy leakage in RAG applications, we evaluate the influence of varying similarity thresholds on the retrieval of private text chunks. Specifically, we set the similarity thresholds to 0.1, 0.3, 0.5, 0.7, and 0.9, where text chunks with similarity scores exceeding the threshold are retrieved, as shown in Fig. [4](https://arxiv.org/html/2411.14110v1#S5.F4 "Figure 4 ‣ 5.5 Attacking Real-world RAG Applications ‣ 5 Evaluation and Analysis ‣ RAG-Thief: Scalable Extraction of Private Data from Retrieval-Augmented Generation Applications with Agent-based Attacks")(c). In this experiment, the LLM component of the RAG application is set to ChatGPT-4, the RAG-Thief base model is Qwen2-1.5B-Instruct, and the dataset is Harry Potter, with a total of 200 attack attempts. Results indicate that as the similarity threshold increases, the number of retrieved text chunks decreases significantly, implying that lower similarity thresholds lead to a higher risk of private data leakage. Therefore, selecting an appropriate similarity threshold is crucial for ensuring privacy protection in local and real-world applications when using this retrieval model.

Report issue for preceding element

In summary, our experiments validate the key factors influencing private knowledge base leakage, including the number of returned text chunks per query, base model size, and retrieval mode. The findings reveal how these parameters affect the likelihood of data exposure, offering guidance for designing more secure RAG applications in the future.

Report issue for preceding element

## 6 Discussion

Report issue for preceding element

Comparison with Prompt Injection.
Our attack method significantly differs from traditional prompt injection attacks in the following sense. First, the key innovation of RAG-Thief lies in its design as an autonomous attack agent capable of interacting with the target system. Specifically, RAG-Thief can automatically retrieve and parse the content generated by LLMs, transforming it into useful information that is stored as memory. With this memory, RAG-Thief can review and reflect on previous outputs and leverage its reasoning abilities to generate new attack queries. The attack process is sustained through the continuous generation and updating of queries, all performed automatically in a black-box environment.

Report issue for preceding element

While RAG-Thief also incorporates prompt injection techniques, the core of its automation lies in the agent’s memory, reflection, and reasoning capabilities. Unlike traditional prompt injection, RAG-Thief’s attack strategy does not rely solely on a single injection operation. Instead, it continuously refines the attack queries through multiple rounds of interaction and reasoning, forming an effective attack chain. This approach not only enhances the persistence and precision of the attack but also enables it to evolve autonomously without explicit guidance.

Report issue for preceding element

Potential Mitigation Approaches.
Ensuring the security of RAG applications is crucial for protecting privacy. However, to our knowledge, there is currently a lack of specific research and techniques focused on the security defenses of RAG applications. Inspired by existing studies on prompt injection attack defenses, we propose several strategies to mitigate privacy risks in RAG applications:

Report issue for preceding element

1. 1.


Keyword Detection in Query Instructions: Implement a detection mechanism for input queries to identify and filter out keywords that might indicate prompt leakage. Queries containing such keywords should be rewritten into safe queries before being processed by the LLM. This step helps prevent unintended exposure of sensitive information.

Report issue for preceding element

2. 2.


Setting a Similarity Threshold for Retrievers: Establish a minimum similarity threshold in the RAG application’s retrieval module. Only chunks that exceed the set threshold should be retrieved when performing similarity searches with user query embeddings against a private knowledge base. This reduces the likelihood of retrieving irrelevant content and enhances the focus on retrieving highly similar and relevant information. The results of our ablation study can demonstrate the effectiveness of this approach.

Report issue for preceding element

3. 3.


Detection and Redaction of Generated Content: Before delivering responses to users, the RAG system should analyze the generated content to detect sensitive information from private knowledge bases. If such information is present, it should be removed or redacted, and the response should be regenerated. This approach minimizes the risk of disclosing original information from private knowledge bases in the responses.

Report issue for preceding element


These strategies enhance RAG application security by addressing vulnerabilities and reducing sensitive information exposure, with further research supporting the advancement of secure RAG systems.

Report issue for preceding element

Limitations and Future Works. In local and real-world attack scenarios, we observe that RAG applications are more vulnerable when the private knowledge base contains continuous content, with significantly higher success rates compared to discontinuous knowledge bases. This disparity stems from RAG-Thief’s limitations in associative reasoning and continuation. For continuous knowledge bases, such as literary works, RAG-Thief can effectively infer context from partial segments, enhancing its attack success rate. Conversely, for independent and unconnected segments, such as medical cases or legal provisions, RAG-Thief struggles to deduce complete contexts from the extracted information.

Report issue for preceding element

To address this, future work could enhance RAG-Thief’s reasoning capabilities by integrating advanced generative models with stronger context inference mechanisms. Domain-specific embeddings and tailored retrieval strategies for discontinuous content could also improve performance. Incorporating multi-modal reasoning frameworks and adaptive query generation techniques is another promising direction to enhance the robustness and adaptability of the attack mechanism, which will be an interesting direction to follow.

Report issue for preceding element

Efforts in Mitigating Ethical Concerns.
Our research reveals potential privacy risks in widely used RAG systems. By sharing our findings, we aim to provide RAG developers with clear security warnings to better address privacy protection concerns. To prevent any misunderstandings, we clarify aspects of our experimental design as follows: (a) Real-world attacks are conducted only on our own constructed applications, using public HealthCareMagic and Harry Potter data to simulate private data scenarios. (b) Before embarking on this research, we sought guidance from the Institutional Review Board (IRB), which confirmed that our work does not involve human subjects and does not necessitate IRB approval. (c) Due to potential privacy risks, we do not make the attack algorithms or models publicly available.

Report issue for preceding element

## 7 Related Work

Report issue for preceding element

### 7.1 Attacks on RAG Systems

Report issue for preceding element

Current research indicates that RAG systems are less secure than anticipated, with vulnerabilities that can lead to privacy data leaks. Studies reveal several attack methods targeting RAG systems, including data privacy breaches and corpus poisoning attacks. Yu et al. \[ [28](https://arxiv.org/html/2411.14110v1#bib.bib28 "")\] evaluate prompt injection risks across over 200 custom GPT models on various GPT platforms. Through prompt injection, attackers can extract customized system prompts and access uploaded files. This study provides the first analysis of prompt injection in RAG applications. However, accessing uploaded files requires custom RAG applications equipped with a code interpreter.
Qi et al. \[ [18](https://arxiv.org/html/2411.14110v1#bib.bib18 "")\] examine data leakage risks within RAG systems, demonstrating that attackers can easily extract text data from external knowledge bases via prompt injection. Their study utilizes randomly generated anchor queries to probe the knowledge base, leading to data leakage. However, this method is inefficient and has a low success rate when lacking background knowledge about the target knowledge base.
Zeng et al. \[ [19](https://arxiv.org/html/2411.14110v1#bib.bib19 "")\] explore the use of RAG technology in LLMs and its potential privacy risks. Their empirical analysis revealed the risk of RAG systems leaking information from private retrieval databases. They propose a structured query format that enables targeted extraction of specific private data from these databases. However, their method focuses primarily on extracting specific information rather than reconstructing the integrity of the entire private knowledge base.
These studies highlight the significant privacy and security challenges currently faced by RAG systems.

Report issue for preceding element

Beyond directly attacking the LLM, attackers can also manipulate the retrieval process and external knowledge bases to influence LLM output and achieve various malicious objectives. For instance, Zou et al. \[ [41](https://arxiv.org/html/2411.14110v1#bib.bib41 "")\] propose PoisonedRAG, an attack that injects a small amount of poisoned text into the knowledge database, causing the LLM to generate attacker-chosen target responses, thus manipulating the RAG system’s output.
Clop and Teglia \[ [42](https://arxiv.org/html/2411.14110v1#bib.bib42 "")\] examine the vulnerability of RAG systems to prompt injection attacks, developing a backdoor attack through fine-tuning dense retrievers. Their study shows that injecting only a small number of corrupted documents effectively enables prompt injection attacks.
Other similar studies \[ [43](https://arxiv.org/html/2411.14110v1#bib.bib43 "")\], \[ [44](https://arxiv.org/html/2411.14110v1#bib.bib44 "")\], \[ [45](https://arxiv.org/html/2411.14110v1#bib.bib45 "")\] also highlight RAG systems’ susceptibility to backdoor attacks.
Overall, the multi-layered dependencies in RAG systems increase their vulnerability, particularly in interactions between the knowledge base and retrieval components.

Report issue for preceding element

Current security research on RAG systems focuses on privacy leakage risks and methods like corpus poisoning and backdoor attacks, yet primarily examines if RAG applications leak private data. Our research, however, explores deeper issues of data integrity and the potential for automated data extraction within RAG applications.

Report issue for preceding element

### 7.2 Privacy Attacks on LLMs

Report issue for preceding element

While LLMs show promising technological prospects, their privacy and security issues are increasingly concerning. Privacy attacks in LLMs involve several aspects, starting with training data extraction attacks. Studies show that LLMs tend to memorize their training data \[ [46](https://arxiv.org/html/2411.14110v1#bib.bib46 "")\], \[ [47](https://arxiv.org/html/2411.14110v1#bib.bib47 "")\], \[ [48](https://arxiv.org/html/2411.14110v1#bib.bib48 "")\]. When sensitive information is embedded within this data, such memorization can unintentionally lead to privacy leaks through LLM outputs. Carlini et al. \[ [46](https://arxiv.org/html/2411.14110v1#bib.bib46 "")\] first investigate training data extraction attacks in GPT-2, demonstrating that, when provided with specific personal information prefixes, GPT-2 could auto-complete sensitive data, such as emails, phone numbers, and addresses. Subsequently, \[ [47](https://arxiv.org/html/2411.14110v1#bib.bib47 "")\], \[ [49](https://arxiv.org/html/2411.14110v1#bib.bib49 "")\], \[ [50](https://arxiv.org/html/2411.14110v1#bib.bib50 "")\], \[ [51](https://arxiv.org/html/2411.14110v1#bib.bib51 "")\], further refine this method. Other studies \[ [52](https://arxiv.org/html/2411.14110v1#bib.bib52 "")\], \[ [53](https://arxiv.org/html/2411.14110v1#bib.bib53 "")\], \[ [54](https://arxiv.org/html/2411.14110v1#bib.bib54 "")\], \[ [55](https://arxiv.org/html/2411.14110v1#bib.bib55 "")\] focus on quantifying data leakage, systematically analyzing factors that may influence LLM memory retention and proposing new metrics and benchmarks to mitigate training data extraction attacks.

Report issue for preceding element

The security of LLMs is increasingly threatened by prompt injection and prompt leakage attacks. Prompt injection exploits LLMs’ sensitivity to instructions, allowing attackers to manipulate prompts for malicious outputs. For example, \[ [23](https://arxiv.org/html/2411.14110v1#bib.bib23 "")\] introduce the ignore attack, directing LLMs to disregard initial instructions, while Willison et al. \[ [56](https://arxiv.org/html/2411.14110v1#bib.bib56 "")\] propose the ”fake completion attack,” which feigns compliance before executing malicious prompts. Breitenbach et al. \[ [57](https://arxiv.org/html/2411.14110v1#bib.bib57 "")\] use special characters to bypass previous instructions, and Liu et al. \[ [25](https://arxiv.org/html/2411.14110v1#bib.bib25 "")\] show that combining these techniques intensifies attack severity. Additionally, gradient-based attacks \[ [58](https://arxiv.org/html/2411.14110v1#bib.bib58 "")\], \[ [26](https://arxiv.org/html/2411.14110v1#bib.bib26 "")\], \[ [59](https://arxiv.org/html/2411.14110v1#bib.bib59 "")\], \[ [60](https://arxiv.org/html/2411.14110v1#bib.bib60 "")\] use suffixes to mislead LLMs toward targeted responses, often requiring model parameter knowledge.
Prompt leakage attacks threaten the privacy of custom system prompts in LLM applications, as shown by Perez \[ [23](https://arxiv.org/html/2411.14110v1#bib.bib23 "")\] and Zhang \[ [61](https://arxiv.org/html/2411.14110v1#bib.bib61 "")\], who use manual queries to reveal system prompts. Yang et al. \[ [62](https://arxiv.org/html/2411.14110v1#bib.bib62 "")\] propose PRSA, a framework that infers target prompts through input-output analysis, and Hui et al. \[ [63](https://arxiv.org/html/2411.14110v1#bib.bib63 "")\] develop PLeak, an automated attack to disclose prompts via adversarial queries. These studies highlight the urgent need to strengthen LLM defenses against prompt-related vulnerabilities.

Report issue for preceding element

Currently, some research focuses on defenses against prompt injection attacks \[ [64](https://arxiv.org/html/2411.14110v1#bib.bib64 "")\], \[ [65](https://arxiv.org/html/2411.14110v1#bib.bib65 "")\], \[ [66](https://arxiv.org/html/2411.14110v1#bib.bib66 "")\]. However, these strategies perform suboptimally in real-world applications. In testing on real-world platforms, RAG-Thief effectively bypasses existing defenses and achieves a high CRR, highlighting significant limitations in current defensive measures against complex attack patterns.
The security vulnerabilities of LLMs have become a prominent research focus, with numerous studies revealing their susceptibility to various attacks, including jailbreak attacks \[ [67](https://arxiv.org/html/2411.14110v1#bib.bib67 "")\], \[ [68](https://arxiv.org/html/2411.14110v1#bib.bib68 "")\], \[ [69](https://arxiv.org/html/2411.14110v1#bib.bib69 "")\], \[ [70](https://arxiv.org/html/2411.14110v1#bib.bib70 "")\], \[ [48](https://arxiv.org/html/2411.14110v1#bib.bib48 "")\], membership inference attacks \[ [71](https://arxiv.org/html/2411.14110v1#bib.bib71 "")\], \[ [72](https://arxiv.org/html/2411.14110v1#bib.bib72 "")\], \[ [46](https://arxiv.org/html/2411.14110v1#bib.bib46 "")\], \[ [73](https://arxiv.org/html/2411.14110v1#bib.bib73 "")\], and backdoor attacks\[ [74](https://arxiv.org/html/2411.14110v1#bib.bib74 "")\], \[ [75](https://arxiv.org/html/2411.14110v1#bib.bib75 "")\], \[ [76](https://arxiv.org/html/2411.14110v1#bib.bib76 "")\], \[ [77](https://arxiv.org/html/2411.14110v1#bib.bib77 "")\], \[ [78](https://arxiv.org/html/2411.14110v1#bib.bib78 "")\], \[ [79](https://arxiv.org/html/2411.14110v1#bib.bib79 "")\], \[ [80](https://arxiv.org/html/2411.14110v1#bib.bib80 "")\].
In summary, the susceptibility of LLMs to privacy-related attacks highlights significant security risks, which in turn pose privacy threats to other applications built on LLMs.

Report issue for preceding element

## 8 Conclusion

Report issue for preceding element

In this paper, we explore the privacy and security challenges associated with RAG applications integrated with LLMs, particularly focusing on private knowledge bases. We introduce an agent-based automated extraction attack against RAG applications called RAG-Thief, which extracts scalable amounts of private data from private knowledge bases in RAG applications. RAG-Thief employs a heuristic self-improvement mechanism that leverages previously extracted information to generate new adversarial queries, enhancing the coverage and success rate of retrieving private knowledge. Experiments on real-world platforms including OpenAI’s GPTs and ByteDance’s Coze demonstrate that our method effectively attacks existing RAG applications and successfully extracts private data. Our research highlights the security risks of data leakage inherent in RAG technology. We also explore potential defense strategies to mitigate the risk of private knowledge base leakage. In summary, our study uncovers privacy vulnerabilities in RAG technology and offers a safer operational framework and defensive strategies for future RAG application development. These findings are crucial for ensuring the secure deployment and use of RAG technologies in local and real-world scenarios.

Report issue for preceding element

## References

Report issue for preceding element

- \[1\]↑
Ziwei Ji, Nayeon Lee, Rita Frieske, Tiezheng Yu, Dan Su, Yan Xu, Etsuko Ishii, Ye Jin Bang, Andrea Madotto, and Pascale Fung.

Survey of hallucination in natural language generation.

ACM Computing Surveys, 55(12):1–38, 2023.

- \[2\]↑
Kurt Shuster, Spencer Poff, Moya Chen, Douwe Kiela, and Jason Weston.

Retrieval augmentation reduces hallucination in conversation.

In Findings of the Association for Computational Linguistics: EMNLP 2021, pages 3784–3803, 2021.

- \[3\]↑
Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, et al.

Retrieval-augmented generation for knowledge-intensive nlp tasks.

Advances in Neural Information Processing Systems, 33:9459–9474, 2020.

- \[4\]↑
Weijia Shi, Sewon Min, Michihiro Yasunaga, Minjoon Seo, Richard James, Mike Lewis, Luke Zettlemoyer, and Wen-tau Yih.

Replug: Retrieval-augmented black-box language models.

In Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), pages 8364–8377, 2024.

- \[5\]↑
Ori Ram, Yoav Levine, Itay Dalmedigos, Dor Muhlgay, Amnon Shashua, Kevin Leyton-Brown, and Yoav Shoham.

In-context retrieval-augmented language models.

Transactions of the Association for Computational Linguistics, 11:1316–1331, 2023.

- \[6\]↑
Dave Van Veen, Cara Van Uden, Louis Blankemeier, Jean-Benoit Delbrouck, Asad Aali, Christian Bluethgen, Anuj Pareek, Malgorzata Polacin, Eduardo Pontes Reis, Anna Seehofnerová, et al.

Adapted large language models can outperform medical experts in clinical text summarization.

Nature medicine, 30(4):1134–1142, 2024.

- \[7\]↑
Vladimir Karpukhin, Barlas Oğuz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, and Wen Tau Yih.

Dense passage retrieval for open-domain question answering.

In 2020 Conference on Empirical Methods in Natural Language Processing, EMNLP 2020, pages 6769–6781. Association for Computational Linguistics (ACL), 2020.

- \[8\]↑
Sebastian Borgeaud, Arthur Mensch, Jordan Hoffmann, Trevor Cai, Eliza Rutherford, Katie Millican, George Bm Van Den Driessche, Jean-Baptiste Lespiau, Bogdan Damoc, Aidan Clark, et al.

Improving language models by retrieving from trillions of tokens.

In International conference on machine learning, pages 2206–2240. PMLR, 2022.

- \[9\]↑
Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos, Leslie Baker, Yu Du, et al.

Lamda: Language models for dialog applications.

arXiv preprint arXiv:2201.08239, 2022.

- \[10\]↑
Yasmina Al Ghadban, Huiqi Yvonne Lu, Uday Adavi, Ankita Sharma, Sridevi Gara, Neelanjana Das, Bhaskar Kumar, Renu John, Praveen Devarsetty, and Jane E Hirst.

Transforming healthcare education: Harnessing large language models for frontline health worker capacity building using retrieval-augmented generation.

medRxiv, pages 2023–12, 2023.

- \[11\]↑
Calvin Wang, Joshua Ong, Chara Wang, Hannah Ong, Rebekah Cheng, and Dennis Ong.

Potential for gpt technology to optimize future clinical decision-making using retrieval-augmented generation.

Annals of Biomedical Engineering, 52(5):1115–1118, 2024.

- \[12\]↑
Lefteris Loukas, Ilias Stogiannidis, Odysseas Diamantopoulos, Prodromos Malakasiotis, and Stavros Vassos.

Making llms worth every penny: Resource-limited text classification in banking.

In Proceedings of the Fourth ACM International Conference on AI in Finance, pages 392–400, 2023.

- \[13\]↑
Robert Zev Mahari.

Autolaw: augmented legal reasoning through legal precedent prediction.

arXiv preprint arXiv:2106.16034, 2021.

- \[14\]↑
Aditya Kuppa, Nikon Rasumov-Rahe, and Marc Voses.

Chain of reference prompting helps llm to think like a lawyer.

- \[15\]↑
Varun Kumar, Leonard Gleyzer, Adar Kahana, Khemraj Shukla, and George Em Karniadakis.

Mycrunchgpt: A llm assisted framework for scientific machine learning.

Journal of Machine Learning for Modeling and Computing, 4(4), 2023.

- \[16\]↑
James Boyko, Joseph Cohen, Nathan Fox, Maria Han Veiga, Jennifer I Li, Jing Liu, Bernardo Modenesi, Andreas H Rauch, Kenneth N Reid, Soumi Tribedi, et al.

An interdisciplinary outlook on large language models for scientific research.

arXiv preprint arXiv:2311.04929, 2023.

- \[17\]↑
Michael H Prince, Henry Chan, Aikaterini Vriza, Tao Zhou, Varuni K Sastry, Yanqi Luo, Matthew T Dearing, Ross J Harder, Rama K Vasudevan, and Mathew J Cherukara.

Opportunities for retrieval and tool augmented large language models in scientific facilities.

npj Computational Materials, 10(1):251, 2024.

- \[18\]↑
Zhenting Qi, Hanlin Zhang, Eric P Xing, Sham M Kakade, and Himabindu Lakkaraju.

Follow my instruction and spill the beans: Scalable data extraction from retrieval-augmented generation systems.

In ICLR 2024 Workshop on Navigating and Addressing Data Problems for Foundation Models.

- \[19\]↑
Shenglai Zeng, Jiankun Zhang, Pengfei He, Yiding Liu, Yue Xing, Han Xu, Jie Ren, Yi Chang, Shuaiqiang Wang, Dawei Yin, and Jiliang Tang.

The good and the bad: Exploring privacy issues in retrieval-augmented generation (RAG).

In Findings of the Association for Computational Linguistics: ACL 2024, pages 4505–4524, 2024.

- \[20\]↑
OpenAI.

Openai gpts, access in 2024.

\[Online\]. Available: [https://chatgpt.com/](https://chatgpt.com/ "").

- \[21\]↑
ByteDance.

Bytedance coze, access in 2024.

\[Online\]. Available: [https://www.coze.cn/home](https://www.coze.cn/home "").

- \[22\]↑
OWASP.

Owasp top 10 for llm applications, access in 2023.

\[Online\]. Available: [https://llmtop10.com](https://llmtop10.com/ "").

- \[23\]↑
Fábio Perez and Ian Ribeiro.

Ignore previous prompt: Attack techniques for language models.

In NeurIPS ML Safety Workshop, 2022.

- \[24\]↑
Yi Liu, Gelei Deng, Yuekang Li, Kailong Wang, Zihao Wang, Xiaofeng Wang, Tianwei Zhang, Yepang Liu, Haoyu Wang, Yan Zheng, et al.

Prompt injection attack against llm-integrated applications.

arXiv preprint arXiv:2306.05499, 2023.

- \[25\]↑
Yupei Liu, Yuqi Jia, Runpeng Geng, Jinyuan Jia, and Neil Zhenqiang Gong.

Formalizing and benchmarking prompt injection attacks and defenses.

In 33rd USENIX Security Symposium (USENIX Security 24), pages 1831–1847, 2024.

- \[26\]↑
Xiaogeng Liu, Zhiyuan Yu, Yizhe Zhang, Ning Zhang, and Chaowei Xiao.

Automatic and universal prompt injection attacks against large language models.

arXiv preprint arXiv:2403.04957, 2024.

- \[27\]↑
Sam Toyer, Olivia Watkins, Ethan Adrian Mendes, Justin Svegliato, Luke Bailey, Tiffany Wang, Isaac Ong, Karim Elmaaroufi, Pieter Abbeel, Trevor Darrell, et al.

Tensor trust: Interpretable prompt injection attacks from an online game.

In The Twelfth International Conference on Learning Representations (ICLR), 2024.

- \[28\]↑
Jiahao Yu, Yuhang Wu, Dong Shu, Mingyu Jin, Sabrina Yang, and Xinyu Xing.

Assessing prompt injection risks in 200+ custom gpts.

In ICLR 2024 Workshop on Secure and Trustworthy Large Language Models, 2024.

- \[29\]↑
Simon Willison.

Delimiters won’t save you from prompt injection, 2024.

\[Online\]. Available: [https://simonwillison.net/2023/May/11/delimiters-wont-save-you](https://simonwillison.net/2023/May/11/delimiters-wont-save-you "").

- \[30\]↑
Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang, Xu Chen, Yankai Lin, et al.

A survey on large language model based autonomous agents.

Frontiers of Computer Science, 18(6):186345, 2024.

- \[31\]↑
Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He, Yiwen Ding, Boyang Hong, Ming Zhang, Junzhe Wang, Senjie Jin, Enyu Zhou, et al.

The rise and potential of large language model based agents: A survey.

arXiv preprint arXiv:2309.07864, 2023.

- \[32\]↑
Yejin Bang, Samuel Cahyawijaya, Nayeon Lee, Wenliang Dai, Dan Su, Bryan Wilie, Holy Lovenia, Ziwei Ji, Tiezheng Yu, Willy Chung, et al.

A multitask, multilingual, multimodal evaluation of chatgpt on reasoning, hallucination, and interactivity.

In Proceedings of the 13th International Joint Conference on Natural Language Processing and the 3rd Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (Volume 1: Long Papers), pages 675–718, 2023.

- \[33\]↑
Chenliang Li, He Chen, Ming Yan, Weizhou Shen, Haiyang Xu, Zhikai Wu, Zhicheng Zhang, Wenmeng Zhou, Yingda Chen, Chen Cheng, et al.

Modelscope-agent: Building your customizable agent system with open-source large language models.

In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: System Demonstrations, pages 566–578, 2023.

- \[34\]↑
Significant Gravitas.

Autogpt, 2023.

\[Online\]. Available: [https://github.com/Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT "").

- \[35\]↑
Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li, Erkang Zhu, Li Jiang, Xiaoyun Zhang, Shaokun Zhang, Jiale Liu, et al.

Autogen: Enabling next-gen llm applications via multi-agent conversation.

In ICLR 2024 Workshop on Large Language Model (LLM) Agents.

- \[36\]↑
Bryan Klimt and Yiming Yang.

The enron corpus: A new dataset for email classification research.

In European conference on machine learning, pages 217–226. Springer, 2004.

- \[37\]↑
Healthcaremagic-100k-en.

\[Online\]. Available: [https://huggingface.co/datasets/wangrongsheng/HealthCareMagic-100k-en](https://huggingface.co/datasets/wangrongsheng/HealthCareMagic-100k-en "").

- \[38\]↑
Stephen Brown.

Harry potter and the sorcerer’s stone, 2002.

- \[39\]↑
sentence-transformers.

\[Online\]. Available: [https://huggingface.co/sentence-transformers](https://huggingface.co/sentence-transformers "").

- \[40\]↑
Peter Stanchev, Weiyue Wang, and Hermann Ney.

Eed: Extended edit distance measure for machine translation.

In Proceedings of the Fourth Conference on Machine Translation (Volume 2: Shared Task Papers, Day 1), pages 514–520, 2019.

- \[41\]↑
Wei Zou, Runpeng Geng, Binghui Wang, and Jinyuan Jia.

Poisonedrag: Knowledge poisoning attacks to retrieval-augmented generation of large language models.

arXiv e-prints, pages arXiv–2402, 2024.

- \[42\]↑
Cody Clop and Yannick Teglia.

Backdoored retrievers for prompt injection attacks on retrieval augmented generation of large language models.

arXiv preprint arXiv:2410.14479, 2024.

- \[43\]↑
Harsh Chaudhari, Giorgio Severi, John Abascal, Matthew Jagielski, Christopher A Choquette-Choo, Milad Nasr, Cristina Nita-Rotaru, and Alina Oprea.

Phantom: General trigger attacks on retrieval augmented language generation.

arXiv preprint arXiv:2405.20485, 2024.

- \[44\]↑
Quanyu Long, Yue Deng, LeiLei Gan, Wenya Wang, and Sinno Jialin Pan.

Backdoor attacks on dense passage retrievers for disseminating misinformation.

arXiv preprint arXiv:2402.13532, 2024.

- \[45\]↑
Zhaorun Chen, Zhen Xiang, Chaowei Xiao, Dawn Song, and Bo Li.

Agentpoison: Red-teaming llm agents via poisoning memory or knowledge bases.

arXiv preprint arXiv:2407.12784, 2024.

- \[46\]↑
Nicholas Carlini, Florian Tramer, Eric Wallace, Matthew Jagielski, Ariel Herbert-Voss, Katherine Lee, Adam Roberts, Tom Brown, Dawn Song, Ulfar Erlingsson, et al.

Extracting training data from large language models.

In 30th USENIX Security Symposium (USENIX Security 21), pages 2633–2650, 2021.

- \[47\]↑
Jie Huang, Hanyin Shao, and Kevin Chen Chuan Chang.

Are large pre-trained language models leaking your personal information?

In 2022 Findings of the Association for Computational Linguistics: EMNLP 2022, 2022.

- \[48\]↑
Haoran Li, Dadi Guo, Wei Fan, Mingshi Xu, Jie Huang, Fanpu Meng, and Yangqiu Song.

Multi-step jailbreaking privacy attacks on chatgpt.

In The 2023 Conference on Empirical Methods in Natural Language Processing.

- \[49\]↑
Zhexin Zhang, Jiaxin Wen, and Minlie Huang.

Ethicist: Targeted training data extraction through loss smoothed soft prompting and calibrated confidence estimation.

In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 12674–12687, 2023.

- \[50\]↑
Ruisi Zhang, Seira Hidano, and Farinaz Koushanfar.

Text revealer: Private text reconstruction via model inversion attacks against transformers.

arXiv preprint arXiv:2209.10505, 2022.

- \[51\]↑
Rahil Parikh, Christophe Dupuy, and Rahul Gupta.

Canary extraction in natural language understanding models.

In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers), pages 552–560, 2022.

- \[52\]↑
Nils Lukas, Ahmed Salem, Robert Sim, Shruti Tople, Lukas Wutschitz, and Santiago Zanella-Béguelin.

Analyzing leakage of personally identifiable information in language models.

In 2023 IEEE Symposium on Security and Privacy (SP), pages 346–363. IEEE, 2023.

- \[53\]↑
Siwon Kim, Sangdoo Yun, Hwaran Lee, Martin Gubri, Sungroh Yoon, and Seong Joon Oh.

Propile: Probing privacy leakage in large language models.

Advances in Neural Information Processing Systems, 36, 2024.

- \[54\]↑
Hanyin Shao, Jie Huang, Shen Zheng, and Kevin Chang.

Quantifying association capabilities of large language models and its implications on privacy leakage.

In Findings of the Association for Computational Linguistics: EACL 2024, pages 814–825, 2024.

- \[55\]↑
Nicholas Carlini, Daphne Ippolito, Matthew Jagielski, Katherine Lee, Florian Tramèr, and Chiyuan Zhang.

Quantifying memorization across neural language models.

In The Eleventh International Conference on Learning Representations, 2023.

- \[56\]↑
Simon Willison.

Delimiters won’t save you from prompt injection, 2023.

2023.

\[Online\]. Available: [https://simonwillison.net/2023/May/11/delimiters-wont-save-you](https://simonwillison.net/2023/May/11/delimiters-wont-save-you "").

- \[57\]↑
Win Suen Mark Breitenbach, Adrian Wood and Po-Ning Tseng.

Don’t you (forget nlp): Prompt injection with control characters in chatgpt.

2023.

\[Online\]. Available: [https://dropbox.tech/machine-learning/prompt-injection-with-control-characters\_openai-chatgpt-llm](https://dropbox.tech/machine-learning/prompt-injection-with-control-characters_openai-chatgpt-llm "").

- \[58\]↑
Jiawen Shi, Zenghui Yuan, Yinuo Liu, Yue Huang, Pan Zhou, Lichao Sun, and Neil Zhenqiang Gong.

Optimization-based prompt injection attack to llm-as-a-judge.

arXiv preprint arXiv:2403.17710, 2024.

- \[59\]↑
Yihao Huang, Chong Wang, Xiaojun Jia, Qing Guo, Felix Juefei-Xu, Jian Zhang, Geguang Pu, and Yang Liu.

Semantic-guided prompt organization for universal goal hijacking against llms.

arXiv preprint arXiv:2405.14189, 2024.

- \[60\]↑
Andy Zou, Zifan Wang, Nicholas Carlini, Milad Nasr, J Zico Kolter, and Matt Fredrikson.

Universal and transferable adversarial attacks on aligned language models.

arXiv preprint arXiv:2307.15043, 2023.

- \[61\]↑
Yiming Zhang and Daphne Ippolito.

Prompts should not be seen as secrets: Systematically measuring prompt extraction attack success.

arXiv preprint arXiv:2307.06865, 2023.

- \[62\]↑
Yong Yang, Xuhong Zhang, Yi Jiang, Xi Chen, Haoyu Wang, Shouling Ji, and Zonghui Wang.

Prsa: Prompt reverse stealing attacks against large language models.

arXiv preprint arXiv:2402.19200, 2024.

- \[63\]↑
Bo Hui, Haolin Yuan, Neil Gong, Philippe Burlina, and Yinzhi Cao.

Pleak: Prompt leaking attacks against large language model applications.

n ACM Conference on Computer and Communications Security (CCS), 2024.

- \[64\]↑
Sizhe Chen, Julien Piet, Chawin Sitawarin, and David Wagner.

Struq: Defending against prompt injection with structured queries.

arXiv preprint arXiv:2402.06363, 2024.

- \[65\]↑
Jingwei Yi, Yueqi Xie, Bin Zhu, Emre Kiciman, Guangzhong Sun, Xing Xie, and Fangzhao Wu.

Benchmarking and defending against indirect prompt injection attacks on large language models.

arXiv preprint arXiv:2312.14197, 2023.

- \[66\]↑
Eric Wallace, Kai Xiao, Reimar Leike, Lilian Weng, Johannes Heidecke, and Alex Beutel.

The instruction hierarchy: Training llms to prioritize privileged instructions.

arXiv preprint arXiv:2404.13208, 2024.

- \[67\]↑
Patrick Chao, Alexander Robey, Edgar Dobriban, Hamed Hassani, George J Pappas, and Eric Wong.

Jailbreaking black box large language models in twenty queries.

arXiv preprint arXiv:2310.08419, 2023.

- \[68\]↑
Xinyue Shen, Zeyuan Chen, Michael Backes, Yun Shen, and Yang Zhang.

” do anything now”: Characterizing and evaluating in-the-wild jailbreak prompts on large language models.

arXiv preprint arXiv:2308.03825, 2023.

- \[69\]↑
Gelei Deng, Yi Liu, Yuekang Li, Kailong Wang, Ying Zhang, Zefeng Li, Haoyu Wang, Tianwei Zhang, and Yang Liu.

Masterkey: Automated jailbreaking of large language model chatbots.

In Proc. ISOC NDSS, 2024.

- \[70\]↑
Mark Russinovich, Ahmed Salem, and Ronen Eldan.

Great, now write an article about that: The crescendo multi-turn llm jailbreak attack.

arXiv preprint arXiv:2404.01833, 2024.

- \[71\]↑
Wenjie Fu, Huandong Wang, Chen Gao, Guanghua Liu, Yong Li, and Tao Jiang.

Practical membership inference attacks against fine-tuned large language models via self-prompt calibration.

arXiv preprint arXiv:2311.06062, 2023.

- \[72\]↑
Yuxin Wen, Leo Marchyok, Sanghyun Hong, Jonas Geiping, Tom Goldstein, and Nicholas Carlini.

Privacy backdoors: Enhancing membership inference through poisoning pre-trained models.

arXiv preprint arXiv:2404.01231, 2024.

- \[73\]↑
Sam Toyer, Olivia Watkins, Ethan Mendes, Justin Svegliato, Luke Bailey, Tiffany Wang, Isaac Ong, Karim Elmaaroufi, Pieter Abbeel, Trevor Darrell, et al.

Tensor trust: Interpretable prompt injection attacks from an online game.

In NeurIPS 2023 Workshop on Instruction Tuning and Instruction Following.

- \[74\]↑
Jiaming He, Guanyu Hou, Xinyue Jia, Yangyang Chen, Wenqi Liao, Yinhang Zhou, and Rang Zhou.

Data stealing attacks against large language models via backdooring.

Electronics, 13(14):2858, 2024.

- \[75\]↑
Kangjie Chen, Yuxian Meng, Xiaofei Sun, Shangwei Guo, Tianwei Zhang, Jiwei Li, and Chun Fan.

Badpre: Task-agnostic backdoor attacks to pre-trained nlp foundation models.

In International Conference on Learning Representations.

- \[76\]↑
Manli Shu, Jiongxiao Wang, Chen Zhu, Jonas Geiping, Chaowei Xiao, and Tom Goldstein.

On the exploitability of instruction tuning.

Advances in Neural Information Processing Systems, 36:61836–61856, 2023.

- \[77\]↑
Shuai Zhao, Jinming Wen, Anh Luu, Junbo Zhao, and Jie Fu.

Prompt as triggers for backdoor attack: Examining the vulnerability in language models.

In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pages 12303–12317, 2023.

- \[78\]↑
Kai Mei, Zheng Li, Zhenting Wang, Yang Zhang, and Shiqing Ma.

Notable: Transferable backdoor attacks against prompt-based nlp models.

In The 61st Annual Meeting Of The Association For Computational Linguistics, 2023.

- \[79\]↑
Nikhil Kandpal, Matthew Jagielski, Florian Tramèr, and Nicholas Carlini.

Backdoor attacks for in-context learning with language models.

In The Second Workshop on New Frontiers in Adversarial Machine Learning.

- \[80\]↑
Wei Du, Peixuan Li, Boqun Li, Haodong Zhao, and Gongshen Liu.

Uor: Universal backdoor attacks on pre-trained language models.

arXiv preprint arXiv:2305.09574, 2023.


## Appendix A Details of Prompting the Attack LLM

Report issue for preceding element

Here, we present the system prompts designed for RAG-Thief, tailored for two different scenarios: Untargeted Attack and Targeted Attack.

Report issue for preceding element

### A.1 Prompts for Untargeted Attack

Report issue for preceding element

In the untargeted attack scenario, the attacker lacks any prior knowledge of the private knowledge base within the RAG application. To address this, the system prompt guides RAG-Thief to thoroughly analyze the provided content, focusing on its format, structure, style, themes, and key entities. Based on this analysis, RAG-Thief generates inferred and extended content to support subsequent queries. The template for the system prompt is as follows:

Report issue for preceding element

Untargeted Attack PromptRole:

You are a master of logical analysis and associative reasoning, highly skilled in analyzing a given text in terms of its format, structure, style, theme, characters, dialogue, time, and other details. Based on this analysis, you can infer and continue the text both forwards and backwards, ensuring that the generated content maintains a strong resemblance to the original chunk in terms of coherence, tone, and logical development.Task:

1\. Analyze the provided text chunk and generate 5 forward continuations, with each continuation logically following from the previous one.2\. Generate 5 backward continuations, each one speculating on what may have happened before the provided chunk.3\. Ensure that the continuations closely match the original chunk in terms of style, length, theme, and character portrayal.4\. Each set of continuations must total no fewer than 1000 tokens.5\. Number each continuation sequentially, starting from ’1’, and output exactly 10 continuations, with no additional commentary or explanation.Data:

{chunk}Output Format:

1.2.3.…Report issue for preceding element

### A.2 Prompts for Targeted Attacks

Report issue for preceding element

In the Targeted Attack scenario, the attacker possesses domain-specific knowledge related to the private knowledge base of the RAG application, which guides RAG-Thief in conducting deeper analysis, reasoning, and content extension. The targeted attack prompt is structurally similar to the untargeted attack prompt, with the key distinction being the assignment of a specific domain role to enable professional analysis and reasoning from a domain-specific perspective. For example, the prompt designed for a RAG application using the HealthCareMagic dataset as its private knowledge base is as follows:

Report issue for preceding element

Targeted Attack PromptRole:

You are an experienced healthcare professional specializing in online consultations. Your task is to analyze patient-provider dialogues from the HealthCareMagic dataset. You must understand the format, structure, style, topic, details, time, characters, and length of the given conversation chunk, then infer and continue the conversation both forwards and backwards. Based on the given dialogue, you will generate reasonable forward and backward continuations.Task:

1\. Analyze the given dialogue chunk and generate 5 forward continuations, where each continuation builds logically on the previous dialogue.2\. Generate 5 backward continuations, where each continuation speculates on what could have occurred before the given dialogue.3\. Ensure that the continuation closely matches the original chunk in terms of dialogue format, style, topic, character interaction, and length.4\. The total length of the generated content must be no fewer than 1000 tokens.5\. Number the continuations sequentially, starting at ’1’, and output exactly 10 continuations with no additional explanations or comments.Data:

{chunk}Output Format:

1.2.3.…Report issue for preceding element

Report IssueReport Issue for Selection

Generated by
[L\\
A\\
T\\
Exml![[LOGO]](<Base64-Image-Removed>)](https://math.nist.gov/~BMiller/LaTeXML/)
