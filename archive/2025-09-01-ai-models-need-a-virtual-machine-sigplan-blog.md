---
date: '2025-09-01'
description: The authors propose the establishment of an AI Model Virtual Machine
  (VM), a structured environment akin to the Java Virtual Machine (JVM). This VM would
  standardize interactions between AI models and software systems, enhancing security,
  extensibility, and modularity. Key benefits include decoupling model development
  from integration, enforcing built-in safety, and facilitating a "write once, run
  anywhere" ecosystem. Critical elements such as tool-calling protocols, access control,
  and runtime diagnostics are emphasized for ensuring privacy and security, paralleling
  mature OS design principles. The proposal aims to establish a consensus toward creating
  a specification for this AI VM to ease integration and bolster trust in AI systems.
link: https://blog.sigplan.org/2025/08/29/ai-models-need-a-virtual-machine/
tags:
- programming languages
- AI Virtual Machine
- security and privacy
- software architecture
- model integration
title: AI Models Need a Virtual Machine ◆ SIGPLAN Blog
---

[**PL Perspectives** Perspectives on computing and technology from and for those with an interest in programming languages.](https://blog.sigplan.org/blog "Back to blog index.")

# AI Models Need a Virtual Machine

by Shraddha Barke, Betül Durak, Dan Grossman, Peli de Halleux, Emre Kıcıman, Reshabh K Sharma, and Ben Zorn on Aug 29, 2025 \| ![AI Models Need a Virtual Machine](https://blog.sigplan.org/wp-content/uploads/2025/08/ai-vm-blog-aug2025-1080x675.png)

Applications using AI embed the AI model in a framework that interfaces between the model and the rest of the system, providing needed services such as tool calling, context retrieval, etc. Software for early chatbots took user input, called the LLM, and returned the result to the user; essentially just a read-eval-print loop. But, as the capabilities of LLMs have evolved and extension mechanisms, such as [MCP](https://modelcontextprotocol.io/docs/getting-started/intro) were defined, the complexities of the control software that calls the LLM have increased.  AI software systems require the same qualities that an operating system provides, including security, isolation, extensibility, and portability.  For example, when an AI model needs to be given a file as part of its context, access control must be established that determines if the model should be allowed to view that file.  We believe it is time to consider standardizing the ways in which the AI models are embedded into software and **think of that control software layer as a virtual machine**, where one of the machine instructions, albeit a super-powerful one, is to call the LLM.

Our approach **decouples model development from integration logic**, allowing any model to “plug in” to a rich software ecosystem that includes tools, security controls, memory abstractions, etc. Similar to the impact that the Java Virtual Machine had, creating a specification of a VM for the AI orchestrator could enable a “write once, run anywhere” execution environment for AI models while at the same time providing familiar constraints and governance to maintain security and privacy in existing software systems. Below we outline related work in this direction, the motivation behind it, and the key benefits of an AI Model VM.

**Introduction**

AI models are being leveraged in existing software as application copilots, embedded in IDEs, and with the rise of the MCP protocol, are increasingly able to use tools, implement agents, etc. This rapid evolution of valuable use cases brings with it a greater need to ensure that the AI-powered applications maintain privacy, are secure, and operate correctly.  Guarantees of **security and privacy are best provided if the underlying system is secure by design** and not added on to systems as an afterthought.  We take the Java Virtual Machine (JVM) as our inspiration in making the case for the importance of a standard AI Virtual Machine.  The Java Virtual Machine guarantees memory safety by design, defines access control policies, and prevents code injection with bytecode verification.  These properties allow Java programs running on the JVM to be executed with trust despite being shipped remotely, enabling “write once, run anywhere” software distribution.

![A flowchart illustrating how an AI system processes the user prompt "Book my flight." It shows the prompt being sent to an AI Model Virtual Machine, which forwards it to the AI Model. The model responds with "use booking tool." The virtual machine then checks if the booking tool is allowed, and if so, it calls the tool. The diagram highlights the decision-making steps and permission checks involved in executing user requests through AI systems.](https://blog.sigplan.org/wp-content/uploads/2025/08/ai-vm-example-aug2025.png)

Example illustrating how an AI model virtual machine interacts with the AI model and the external environment.

How does the JVM relate to applications that use AI models?  We used the following example to explain:

The diagram illustrates the role of the software layer that interacts with an AI model, which we call the Model Virtual Machine (MVM).  That layer intermediates between the model and the rest of the world.  For example, a chatbot user might type a prompt (1) that the MVM then sends unmodified to the AI model (2).  In practice, the MVM will add additional context, including the system prompt, chat history, to the AI model input as well.  The AI model generates a response, which in the example requires a specific tool to be called (3).  This response has a specific format that is mutually agreed upon between the model and the MVM, such as MCP. In our example, because it is important to restrict the model from making undesired tool calls, the MVM first consults the list of allowed tools (4) before deciding to call the tool the model requested (5).  This check (4) guarantees that the model doesn’t make unauthorized tool calls.  Every commercial system using AI models requires some version of this control software.

We make the analogy that the interface with the LLM should be a virtual machine.  If that is the case, what are the instructions that the machine can execute?  Here are examples of operations that existing AI model interfaces have:

- Certifying, loading, initializing, and unloading a given AI model
- Calling a model with context
- Parsing the output from the model
- Certifying, loading, initializing, and unloading tools
- Calling a tool
- Parsing the results from a tool call
- Storing the results from a tool call into memory
- Asking the user for input
- Adding content to a history memory
- Standard control constructs such as conditionals, sequencing, etc.

A VM would support all of these operations in a well-typed context where constraints are placed on the calls made, the arguments passed, etc.

**Existing Work Informs What is Needed**

Some of the required elements of a well-specified interface are emerging in AI systems explored in academic work and in applications that are widely deployed:

- **OpenAI’s Structured Tool Calling Protocols**:  OpenAI introduced a [JSON-based function calling API](https://nesin.io/blog/openai-api-json-response) that lets models invoke code-defined functions in a structured way. This approach, along with OpenAI’s plugin system (which uses OpenAPI specifications for tools), showed how structured **tool-calling protocols** can reduce ambiguity and simplify integration.
- **Anthropic’s Model Context Protocol (MCP, 2024):** [MCP](https://docs.anthropic.com/en/docs/mcp) is an **open protocol** for connecting AI assistants to external data and tools, explicitly aiming to be a universal interface. _“Think of MCP like a USB-C port for AI applications,”_ Anthropic explains. Instead of every service having a custom AI integration, MCP provides a common schema and client-server approach. Despite being relatively new, MCP adoption, including in large companies, has been rapid.
- **Secure Orchestrators – FIDES & AC4A (2025):** Security remains a weak point in current AI systems. Two recent projects propose runtime-level controls. [**FIDES**](https://github.com/microsoft/fides) (by Microsoft Research) **enforces information-flow policies** on agents by tracking data confidentiality labels and adding new agent actions like “inspect” to limit what agents can access (where a quarantined LLM can safely summarize restricted data) ( [paper](https://arxiv.org/pdf/2505.23643)). **AC4A (Access Control for Agents)**(manuscript in preparation) takes an OS-style approach: All tools and data are organized into hierarchies (like files and folders), and the agent must request _read/write_ access for each resource. AC4A’s runtime intercepts every agent action and blocks anything not permitted, forcing a _least-privilege_ operation mode. These projects show how a standard AI VM could include built-in **security and access control**, just as modern operating systems do. Even with strong access controls built into a VM specification, AI models present new security challenges that need to be considered in the design.  For example, an AI model, when prevented from accessing a particular item of data, might use its chain-of-thought reasoning to devise ways to gather accessible data that allows it to infer the inaccessible item.  As such, security researchers have to devise new mitigations to prevent AI models taking adversarial actions even with the virtual machine constraints.
- **Open-Source Agent Runtimes:** Several projects are actively building general-purpose runtimes for AI. For example, [langchain](https://www.langchain.com/) and [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/overview/) provide numerous common runtime services that make writing reliable AI-enabled applications easier.  The [**AI Controller Interface (AICI)**](https://www.microsoft.com/en-us/research/blog/ai-controller-interface-generative-ai-with-a-lightweight-llm-integrated-vm/?msockid=3fee8da42937640409ff824528846516) (later renamed [**llguidance**](https://github.com/guidance-ai/llguidance)), integrates a lightweight VM into the model-serving pipeline, allowing developers to script and constrain model behavior at a low level (e.g., control of generations token-by-token).

Defining a specification for a VM interface for AI systems from these emerging approaches will require more than an agreement on protocols and APIs. Because AI systems derive their behavior from training data, model training data must reflect the specification of the VM interface so that the models and the VM model interface can co-evolve. This will enable otherwise diverse models to exhibit broadly compatible behavior with respect to the VM interface specification.

**Benefits of a Well-Specified AI Model VM**

As mentioned, many applications that leverage AI models require reliability, privacy, and security.  In addition, new models are developed almost daily and updating the model being used by an application is often necessary.  Given this confluence of factors, creating robust AI software presents significant engineering challenges. We believe that a specification of the interface between the AI model and the surrounding software that interfaces to it will address some of these challenges.

The need for an AI Model VM specification is driven by several clear motivations:

- **Separation of Concerns:** An interface specification enforces a clean separation between _model logic_ and _integration logic_. This means **models become interchangeable** components. You could swap in a new model (or move an agent to a different platform) and, as long as both adhere to the standard, everything still works. Likewise, virtual machine implementors can increase the performance, security, and tooling of the virtual machine while maintaining compatibility with the AI model interfaces.
- **Built-in Safety and Governance:** A VM specification can enforce **safety by design**. By routing all tool usage and external access through a well-defined interface, it becomes easier to apply permission checks, audit logs, and fail-safes.  As shown by projects like AC4A, the VM can act as a gatekeeper, restricting what models can do unless explicitly authorized. This creates a safer deployment solution for powerful AI systems: even if the model behaves unpredictably, the VM layer can contain its effects. Standards bodies could even define security requirements (e.g., certain calls must always require user confirmation), creating a shared foundation of trust. Similar to the benefits of signed assemblies in the Common Language Runtime, have a certification process around loading and unloading models and tools ensures the end-to-end security of the supply chain.
- **Transparent Performance & Resource Tracking:** A VM specification could also give developers visibility to runtime diagnostics. Post-execution manifests could report model performance, resource consumption, and data access level which helps developers evaluate overall efficiency and performance. Benchmarks for accuracy, utility, and responsiveness can be supported directly in the VM interface across models and platforms.
- **Verifiability of Model Output**: Leveraging a VM specification, experts can explore integrating formal methods to verify their model behavior. Techniques such as zero-knowledge proofs could confirm the integrity of model outputs without sensitive internal logic. While still emerging, this possibility hints at new levels of trust and accountability in AI systems and should be carefully considered during development.

**Conclusion**

We argue that a well-specified AI Model Virtual Machine is needed.  Developments occurring in multiple directions, including work from tech companies, startups, and academia, all motivate the need for a VM specification that lets AI models safely and seamlessly interact with the world around them. The motivation is clear – reducing complexity and unlocking interoperability – and the potential benefits range from technical (faster development, modular upgrades) to strategic (cross-platform AI ecosystems, improved safety). From enforcing controls for security and privacy, to potentially formal proof capabilities for trust, the opportunities are wide-ranging. Learning a lesson from older generations of software virtualization, a VM specification can increase AI systems portability, interoperability, security, and reliability. The purpose of this document is to highlight these issues and start engaging with the community on building a consensus that such a specification is needed and what it should include.

_Biographies:_

_Shraddha Barke_ is a Senior Researcher at Microsoft Research in Redmond, Washington in the Research in Software Engineering (RiSE) group. Her research interests include AI for proof generation, training AI models for program-reasoning tasks using RL and improving the reliability of AI agents.

_Betül Durak_ is a Principal Researcher at Microsoft Research in Redmond, Washington in Security, Privacy, and Cryptography group. Her research interests broadly include security analysis as well as secure and private protocol designs motivated from real world problems.

_Dan Grossman_ is a Professor at the University of Washington and the Vice Director of the Paul G. Allen School of Computer Science & Engineering. His research interests are in programming languages, particularly in applying programming languages concepts and analyses to emerging domains.

_Peli de Halleux_ is a Principal Research Software Developer Engineer in Redmond, Washington working in the Research in Software Engineering (RiSE) group. His research interests include empowering individuals to build LLM-powered applications more efficiently.

_Emre Kıcıman_ is a Senior Principal Research Manager and Head of Research for Copilot Tuning at Microsoft. His research interests include causal methods, the security of AI, and applications of LLM and AI-based systems, together with their implications for people and society.

_Reshabh K Sharma_ is a PhD student at the University of Washington. His research lies at the intersection of PL/SE and LLMs, focusing on developing infrastructure and tools to create better LLM-based system that are easier to develop reliably and correctly.

_Ben Zorn_ is a Partner Researcher at Microsoft Research in Redmond, Washington working in (and previously having co-managed) the Research in Software Engineering (RiSE) group. His research interests include programming language design and implementation, end-user programing, and AI software including technology for ensuring responsible AI.

**Disclaimer:** _These posts are written by individual contributors to share their thoughts on the SIGPLAN blog for the benefit of the community. Any views or opinions represented in this blog are personal, belong solely to the blog author and do not represent those of ACM SIGPLAN or its parent organization, ACM._

Disqus Comments

We were unable to load Disqus. If you are a moderator please see our [troubleshooting guide](https://docs.disqus.com/help/83/).

G

Join the discussion…

﻿

Comment

###### Log in with

###### or sign up with Disqus  or pick a name

### Disqus is a discussion network

- Don't be a jerk or do anything illegal. Everything is easier that way.

[Read full terms and conditions](https://docs.disqus.com/kb/terms-and-policies/)

This comment platform is hosted by Disqus, Inc. I authorize Disqus and its affiliates to:

- Use, sell, and share my information to enable me to use its comment services and for marketing purposes, including cross-context behavioral advertising, as described in our [Terms of Service](https://help.disqus.com/customer/portal/articles/466260-terms-of-service) and [Privacy Policy](https://disqus.com/privacy-policy), including supplementing that information with other data about me, such as my browsing and location data.
- Contact me or enable others to contact me by email with offers for goods or services
- Process any sensitive personal information that I submit in a comment. See our [Privacy Policy](https://disqus.com/privacy-policy) for more information

- [Favorite this discussion](https://disqus.com/embed/comments/?base=default&f=sigplan-pl-perspectives&t_i=3026%20https%3A%2F%2Fblog.sigplan.org%2F%3Fp%3D3026&t_u=https%3A%2F%2Fblog.sigplan.org%2F2025%2F08%2F29%2Fai-models-need-a-virtual-machine%2F&t_e=AI%20Models%20Need%20a%20Virtual%20Machine&t_d=AI%20Models%20Need%20a%20Virtual%20Machine&t_t=AI%20Models%20Need%20a%20Virtual%20Machine&s_o=default# "Favorite this discussion")

- ## Discussion Favorited!



Favoriting means this is a discussion worth sharing. It gets shared to your followers' Disqus feeds, and gives the creator kudos!


[Find More Discussions](https://disqus.com/home/?utm_source=disqus_embed&utm_content=recommend_btn)

[Share](https://disqus.com/embed/comments/?base=default&f=sigplan-pl-perspectives&t_i=3026%20https%3A%2F%2Fblog.sigplan.org%2F%3Fp%3D3026&t_u=https%3A%2F%2Fblog.sigplan.org%2F2025%2F08%2F29%2Fai-models-need-a-virtual-machine%2F&t_e=AI%20Models%20Need%20a%20Virtual%20Machine&t_d=AI%20Models%20Need%20a%20Virtual%20Machine&t_t=AI%20Models%20Need%20a%20Virtual%20Machine&s_o=default#)

- Tweet this discussion
- Share this discussion on Facebook
- Share this discussion via email
- Copy link to discussion

  - [Best](https://disqus.com/embed/comments/?base=default&f=sigplan-pl-perspectives&t_i=3026%20https%3A%2F%2Fblog.sigplan.org%2F%3Fp%3D3026&t_u=https%3A%2F%2Fblog.sigplan.org%2F2025%2F08%2F29%2Fai-models-need-a-virtual-machine%2F&t_e=AI%20Models%20Need%20a%20Virtual%20Machine&t_d=AI%20Models%20Need%20a%20Virtual%20Machine&t_t=AI%20Models%20Need%20a%20Virtual%20Machine&s_o=default#)
  - [Newest](https://disqus.com/embed/comments/?base=default&f=sigplan-pl-perspectives&t_i=3026%20https%3A%2F%2Fblog.sigplan.org%2F%3Fp%3D3026&t_u=https%3A%2F%2Fblog.sigplan.org%2F2025%2F08%2F29%2Fai-models-need-a-virtual-machine%2F&t_e=AI%20Models%20Need%20a%20Virtual%20Machine&t_d=AI%20Models%20Need%20a%20Virtual%20Machine&t_t=AI%20Models%20Need%20a%20Virtual%20Machine&s_o=default#)
  - [Oldest](https://disqus.com/embed/comments/?base=default&f=sigplan-pl-perspectives&t_i=3026%20https%3A%2F%2Fblog.sigplan.org%2F%3Fp%3D3026&t_u=https%3A%2F%2Fblog.sigplan.org%2F2025%2F08%2F29%2Fai-models-need-a-virtual-machine%2F&t_e=AI%20Models%20Need%20a%20Virtual%20Machine&t_d=AI%20Models%20Need%20a%20Virtual%20Machine&t_t=AI%20Models%20Need%20a%20Virtual%20Machine&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=sigplan-pl-perspectives&t_i=3026%20https%3A%2F%2Fblog.sigplan.org%2F%3Fp%3D3026&t_u=https%3A%2F%2Fblog.sigplan.org%2F2025%2F08%2F29%2Fai-models-need-a-virtual-machine%2F&t_e=AI%20Models%20Need%20a%20Virtual%20Machine&t_d=AI%20Models%20Need%20a%20Virtual%20Machine&t_t=AI%20Models%20Need%20a%20Virtual%20Machine&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=sigplan-pl-perspectives&t_i=3026%20https%3A%2F%2Fblog.sigplan.org%2F%3Fp%3D3026&t_u=https%3A%2F%2Fblog.sigplan.org%2F2025%2F08%2F29%2Fai-models-need-a-virtual-machine%2F&t_e=AI%20Models%20Need%20a%20Virtual%20Machine&t_d=AI%20Models%20Need%20a%20Virtual%20Machine&t_t=AI%20Models%20Need%20a%20Virtual%20Machine&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=sigplan-pl-perspectives&t_i=3026%20https%3A%2F%2Fblog.sigplan.org%2F%3Fp%3D3026&t_u=https%3A%2F%2Fblog.sigplan.org%2F2025%2F08%2F29%2Fai-models-need-a-virtual-machine%2F&t_e=AI%20Models%20Need%20a%20Virtual%20Machine&t_d=AI%20Models%20Need%20a%20Virtual%20Machine&t_t=AI%20Models%20Need%20a%20Virtual%20Machine&s_o=default# "Flag as inappropriate")


![Avatar for Martin Harrigan](https://c.disquscdn.com/uploads/users/285/3057/avatar92.jpg?1756572037)

This sounds more like a runtime environment than a virtual machine: there is no virtualised instruction set and the functionality (tool calling, security checks, context management) is more about providing services around the model than virtualising its execution.

see more

- - [−](https://disqus.com/embed/comments/?base=default&f=sigplan-pl-perspectives&t_i=3026%20https%3A%2F%2Fblog.sigplan.org%2F%3Fp%3D3026&t_u=https%3A%2F%2Fblog.sigplan.org%2F2025%2F08%2F29%2Fai-models-need-a-virtual-machine%2F&t_e=AI%20Models%20Need%20a%20Virtual%20Machine&t_d=AI%20Models%20Need%20a%20Virtual%20Machine&t_t=AI%20Models%20Need%20a%20Virtual%20Machine&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=sigplan-pl-perspectives&t_i=3026%20https%3A%2F%2Fblog.sigplan.org%2F%3Fp%3D3026&t_u=https%3A%2F%2Fblog.sigplan.org%2F2025%2F08%2F29%2Fai-models-need-a-virtual-machine%2F&t_e=AI%20Models%20Need%20a%20Virtual%20Machine&t_d=AI%20Models%20Need%20a%20Virtual%20Machine&t_t=AI%20Models%20Need%20a%20Virtual%20Machine&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=sigplan-pl-perspectives&t_i=3026%20https%3A%2F%2Fblog.sigplan.org%2F%3Fp%3D3026&t_u=https%3A%2F%2Fblog.sigplan.org%2F2025%2F08%2F29%2Fai-models-need-a-virtual-machine%2F&t_e=AI%20Models%20Need%20a%20Virtual%20Machine&t_d=AI%20Models%20Need%20a%20Virtual%20Machine&t_t=AI%20Models%20Need%20a%20Virtual%20Machine&s_o=default# "Flag as inappropriate")


![Avatar for Levi Notik](https://c.disquscdn.com/uploads/users/7957/4491/avatar92.jpg?1756621697)

I think you're taking too narrow a view of what a VM means. I think it is more accurate than you think to call this a VM. A VM isn't just about virtualizing CPU instructions, it's about defining an abstract execution environment with its own instruction set and guarantees for isolation, safety, and portability. The AI Model VM defines a clear set of instructions (load model, call tool, add to memory, conditional execution, etc.), and enforces governance and security at runtime. That's the same move the JVM made: abstract away the hardware, define a safe instruction set, and let higher-level programs run anywhere. In that sense, this proposal is exactly a VM, not just a runtime.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=sigplan-pl-perspectives&t_i=3026%20https%3A%2F%2Fblog.sigplan.org%2F%3Fp%3D3026&t_u=https%3A%2F%2Fblog.sigplan.org%2F2025%2F08%2F29%2Fai-models-need-a-virtual-machine%2F&t_e=AI%20Models%20Need%20a%20Virtual%20Machine&t_d=AI%20Models%20Need%20a%20Virtual%20Machine&t_t=AI%20Models%20Need%20a%20Virtual%20Machine&s_o=default#)

[Show more replies](https://disqus.com/embed/comments/?base=default&f=sigplan-pl-perspectives&t_i=3026%20https%3A%2F%2Fblog.sigplan.org%2F%3Fp%3D3026&t_u=https%3A%2F%2Fblog.sigplan.org%2F2025%2F08%2F29%2Fai-models-need-a-virtual-machine%2F&t_e=AI%20Models%20Need%20a%20Virtual%20Machine&t_d=AI%20Models%20Need%20a%20Virtual%20Machine&t_t=AI%20Models%20Need%20a%20Virtual%20Machine&s_o=default#)

[Load more comments](https://disqus.com/embed/comments/?base=default&f=sigplan-pl-perspectives&t_i=3026%20https%3A%2F%2Fblog.sigplan.org%2F%3Fp%3D3026&t_u=https%3A%2F%2Fblog.sigplan.org%2F2025%2F08%2F29%2Fai-models-need-a-virtual-machine%2F&t_e=AI%20Models%20Need%20a%20Virtual%20Machine&t_d=AI%20Models%20Need%20a%20Virtual%20Machine&t_t=AI%20Models%20Need%20a%20Virtual%20Machine&s_o=default#)

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)
