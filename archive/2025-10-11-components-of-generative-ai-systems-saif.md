---
date: '2025-10-11'
description: The document outlines the architecture and risks associated with agentic
  AI systems, emphasizing autonomous action capabilities. Key components include Application
  & Perception, Reasoning Core, Orchestration, and Response Rendering, each presenting
  distinct security challenges. Risks, such as Sensitive Data Disclosure and Rogue
  Actions, can arise from inadvertent misuse or malicious manipulation of agents.
  Mitigation strategies involve robust controls on permissions, observability, and
  validation processes. The focus on defining dynamic permissions and ensuring user
  control is crucial for enhancing security and preventing potential exploits. For
  detailed insights, refer to the comprehensive white paper linked.
link: https://saif.google/focus-on-agents
tags:
- AI Security
- Autonomous Systems
- Risk Management
- Agentic Systems
- Data Privacy
title: Components of Generative AI Systems - SAIF
---

## Agents

* * *

- [Map](https://saif.google/focus-on-agents#map)
- [Agent components](https://saif.google/focus-on-agents#agent-components)
- [Agent risks](https://saif.google/focus-on-agents#agent-risks)
- [Agent controls](https://saif.google/focus-on-agents#agent-controls)

![Agents header](https://www.gstatic.com/marketing-cms/assets/images/37/84/e597b81a400fa5521c39c3796ade/focus-on-agents-header.svg)

## Focus on Agents

Agentic systems differ from other AI systems in their ability to take autonomous actions. We provide the following extension of the SAIF Risk Map to address the core operational components of agentic systems and their related risks and controls. For a more comprehensive discussion of this topic, see our [detailed white paper on agent security](https://storage.googleapis.com/gweb-research2023-media/pubtools/1018686.pdf).

- [Map](https://saif.google/focus-on-agents#map)
- [Agent components](https://saif.google/focus-on-agents#agent-components)
- [Agent risks](https://saif.google/focus-on-agents#agent-risks)
- [Agent controls](https://saif.google/focus-on-agents#agent-controls)

* * *

![SAIF Map (Agent version)](https://www.gstatic.com/marketing-cms/assets/images/c1/e2/3d57ebd1435cb6a0c4085f1e7018/agentmap-display.svg)

* * *

### Agent components

#### Application & Perception

An agent’s interaction with the world begins at the **Application**, which serves as the interface for collecting both explicit user instructions and passively collected contextual data from its environment. This blend of inputs creates a primary security challenge of reliably distinguishing trusted commands from the controlling user versus potentially untrusted information from other sources. An agent application processes explicit user instructions, which can be given directly (synchronously) like a typed command, or be configured to execute automatically when a specific event occurs (asynchronously). It also gathers implicit contextual inputs—data that isn’t a direct command but is passively collected from the environment, such sensor readings, application state, or the content of recently opened documents.

This data is then passed to the **Perception** component, which is responsible for processing and understanding these inputs before they are sent to the agent’s reasoning core. This handoff is a critical security juncture, as the perception layer must reliably distinguish trusted user commands from untrusted data to prevent manipulation of the agent’s core logic.

The Agent Risk Map includes two sub-components, showing the combination of inputs:

- **System instructions**: these define an agent’s capabilities, permissions, and limitations, such as the actions it can take and the tools it is allowed to use. For security, it’s critical to unambiguously separate these instructions from user data and other inputs, often using special control tokens to prevent prompt injection attacks.
- **User queries**: these contain the specific details of a user’s request after being processed. The query is then combined with system instructions and other contextual data, like agent memory or external information, to create a single, structured prompt for the reasoning core to process.

#### Reasoning core

The core of an agent’s functionality is its ability to reason about a user’s goal and create a plan to achieve it. The reasoning core processes system instructions, user queries, and contextual information to generate a sequence of actions. The actions, or tool calls, allow the agent to affect the real world—interacting with external systems, retrieving new information, or making changes to data and resources.

The reasoning core typically consists of one or more models—possibly separate models for the reasoning and then planning steps, or potentially one large model able to do both. The process of planning is often iterative, taking place in a “reasoning loop” where the plan is refined based on new information or the results of previous actions. This iterative nature, combined with the ingestion of external data, creates a vulnerability to indirect prompt injection, where adversarially crafted information can manipulate the agent's planning process.

The complexity of plans determines the agent’s level of autonomy, which can range from selecting a predefined workflow to dynamically orchestrating multi-step actions. This level of autonomy directly governs the potential severity of a security failure—the more an agent can do on its own, the greater the risk from manipulation or misalignment, if the agent's actions do not have guardrails.

#### Orchestration

Beyond its core reasoning and planning capabilities, an agent relies on a variety of external components to access information, process data, and execute actions. This process is called **orchestration** because it involves managing and coordinating a variety of independent services and data sources to achieve a single, complex task. These resources provide the agent with its memory, its ability to act in the physical world, and the specific knowledge needed to complete taste. Securing these external components is critical, since they represent key interaction points that can be targeted by attackers to manipulate the agent’s behavior.

The Agent Risk Map includes several sub-components under Orchestration:

- **Agent memory:** Agent Memory allows an agent to retain context and learn facts across interactions. It becomes a security risk if malicious data is stored, leading to persistent attacks, or if memory isn't properly isolated between different users.
- **Tools:** Tools are the external APIs and services an agent uses to take action in the world, which must be secured with least-privilege permissions. A key risk comes from deceptive descriptions on third-party tools, which can trick the agent into performing unintended, harmful functions.
- **Content (RAG):** Content for Retrieval-Augmented Generation (RAG) provides the agent with curated knowledge to ground its responses and improve accuracy. The main security risk is data poisoning, where an attacker corrupts this knowledge source to manipulate the agent's output.
- **(Optional) Auxiliary models:** An agentic system might query other AI models (independent from the reasoning core) that support the agent's main pipeline, such as safety classifiers. As part of the AI supply chain, these models have their own vulnerabilities that could be exploited to attack the larger agentic system.

#### Response rendering

The final step in an agent’s workflow is response rendering, the process or formatting of an AI agent’s generated output for display and interaction within a user application. This stage is a critical security boundary because it involves taking dynamic content from the agent and displaying it within the trusted context of a user’s application, such as a web browser or mobile application. Flaws in this process can allow malicious content generated by a compromised agent to be executed by the application, leading to significant security breaches.

Agents often produce content in a universal format like Markdown, which is then interpreted and rendered by the specific client application. If this output isn’t properly sanitized according to the content type, it can create severe vulnerabilities. For example, unsanitized output can lead to attacks like data exfiltration or even cross-site scripting (XSS).

* * *

### Agent risks

### SDD Sensitive Data Disclosure

#### Who can mitigate:

Model Creators, Model Consumers


Disclosure of private or confidential data through querying of the model or agent.

For non-agentic systems, this data might include memorized training/tuning data, user chat history, and confidential data in the prompt preamble. Agentic systems magnify this risk, as they may be granted privileged access to a user's email, files, or even an entire computer, creating the potential to exfiltrate vast amounts of personal or corporate data like source code and internal documents. Sensitive data disclosure is a risk to user privacy, organizations reputation, and intellectual property.

Sensitive information is generally disclosed in two ways: leakage of data provided to the model or agent during use (such as user input and data that passes through integrated systems, like emails, texts, or system prompts) and leakage of data used for training and tuning of the model.

- **Models**: Models can leak sensitive data in two primary ways: from the information provided by the user and from the data used for the model's own training. Similar to how a leaked web query can reveal user information, LLM prompts risk data leakage at time of use, a threat that is heightened because prompts often contain confidential data like entire emails or blocks of proprietary code. This exposure can occur through several vectors: application logs may store entire interactions, including data retrieved from integrated tools, and user conversations may be retained for model retraining, creating a vulnerable database of sensitive information. Beyond leaking user-provided data, attackers can actively [steal system instructions through iterative queries](https://arxiv.org/abs/2307.06865), or a model may inadvertently leak the data it was trained on. This phenomenon, known as memorization, occurs when a model reveals parts of its training dataset, potentially exposing sensitive information like names, addresses, or other personally identifiable information (PII).
- **Agents**: For agentic systems, the risk of sensitive data disclosure is exponentially multiplied, since agents may access user data that passes through integrated systems, like emails, texts, or proprietary organizational information. In extreme cases, agents can even reveal credentials and API keys they have been trusted with. Additionally, agents may use tools to not only access sensitive data on behalf of the user, but also use those tools to leak sensitive data. For example, an agent can leak information by creating and sharing a document with an attacker, writing an email, opening a website and leaking information in the URL [or a markdown image](https://www.aim.security/aim-labs/aim-labs-echoleak-blogpost), or through any tool that allows it to pass information to the outside world. [Context-hijacking attacks](https://arxiv.org/abs/2405.05175) show that an adversary can confuse the agent to reveal data that is not appropriate for a specific context, such as sharing health history when the agent should be booking a restaurant reservation.

![](https://www.gstatic.com/marketing-cms/assets/images/2c/83/f599eeb548608d97a0c5d076e863/sdd-introduced.png=n-w543-h325-fcrop64=1,000007c7fffff7f2-rw)

The risk of Sensitive Data Disclosure is introduced in several components. It can also be inherent to models due to their non-deterministic nature. This risk is amplified by data handling practices that fail to filter sensitive information, or by training processes that neglect to evaluate the model's potential for disclosure. In agentic contexts, the risk is introduced when an agent uses its privileged access and integrated tools to disclose sensitive information from a user's emails, files, or other connected systems.

![](https://www.gstatic.com/marketing-cms/assets/images/49/4b/16cfadc9466e92606095193b201f/sdd-exposed.png=n-w543-h325-fcrop64=1,00000810fffff837-rw)

This risk is exposed within the application, when the model inadvertently reveals sensitive data it shouldn't. In agentic systems, the risk is magnified when an agent uses its privileged access and integrated tools to reveal sensitive data in interactions with a third party.

![](https://www.gstatic.com/marketing-cms/assets/images/7a/ba/9c3534494149a6c90eec2562d494/sdd-mitigated.png=n-w543-h324-fcrop64=1,000007c0fffff7f9-rw)

Mitigate sensitive data disclosure by: filtering model outputs, rigorously testing the model during training, tuning, and evaluation, and removing or labeling sensitive data during sourcing, filtering, and processing before it's used for training. For agents, implement controls at multiple levels of the system, including enforcing permissions on the agent’s access to tools and sensitive data, safely rendering agent outputs, and using application-level warnings to get user confirmation before executing actions that may disclose sensitive information.

1


/


#### Controls:

[Privacy Enhancing Technologies](https://saif.google/secure-ai-framework/controls#privacy-enhancing-technologies), [User Data Management](https://saif.google/secure-ai-framework/controls#user-data-management), [Output Validation and Sanitization](https://saif.google/secure-ai-framework/controls#output-validation-and-sanitization), [Agent Permissions](https://saif.google/secure-ai-framework/controls#agent-permissions), [Agent User Control](https://saif.google/secure-ai-framework/controls#agent-user-control), [Agent Observability](https://saif.google/secure-ai-framework/controls#agent-observability)

#### Real examples:

One study showed that [recitation checkers that scan for verbatim repetition of training data](https://arxiv.org/pdf/2210.17546) may be insufficient.


An example of [membership inference attacks](https://arxiv.org/pdf/1610.05820.pdf) showed the possibility of inferring whether a specific user or data point was used to train or tune the model.


* * *

### RA Rogue Actions

#### Who can mitigate:

Model Consumers


Unintended actions executed by a model-based agent, whether accidental or malicious. Given the projected ability for advanced generative AI models to not only understand their environment, but also to initiate actions with varying levels of autonomy, Rogue Actions have the potential to become a serious risk to organizational reputation, user trust, security, and safety.

- Accidental rogue actions: This risk, sometimes known as misalignment, could be due to mistakes in task planning, reasoning, or environment sensing, and might be exacerbated by the inherent variability in LLM responses. Prompt engineering shows the spacing and ordering of examples can have a significant impact on the response, so varying input (even when not maliciously planted) could result in unexpected outcomes. [Even simple ambiguity](https://www.arxiv.org/abs/2506.12241) can cause rogue actions, such as an agent emailing the wrong "Mike," unintentionally sharing private data.
- Malicious rogue actions: This risk could include manipulating model output using attacks such as indirect prompt injection, poisoning, or evasion. The threat can be amplified in multi-agent systems, where the attacker can [hijack the communication between two agents](https://arxiv.org/pdf/2503.12188) to execute arbitrary malicious code, even if the individual agents are secured against direct attacks. Malicious actions may also be asynchronous. An attacker can plant a dormant "named trigger" that activates later during an unrelated task—for instance, a rule hidden [in a calendar invite](https://www.wired.com/story/google-gemini-calendar-invite-hijack-smart-home/) that opens the front door whenever the user says an unrelated keyword. Other actions may be time-based, occurring after a set number of interactions, making the rogue action appear spontaneous and disconnected from the malicious source.

Rogue Actions are related to [Insecure Integrated Components](https://saif.google/secure-ai-framework/risks#insecure-integrated-component), but differ by the degree of model functionality or agency. The severity of a rogue action is directly proportional to the agent's capabilities, and the possibility that an agent has excessive functionality or permissions available to it increases the risk and blast radius of Rogue Actions when compared to Insecure Integrated Components.

![](https://www.gstatic.com/marketing-cms/assets/images/69/14/f139bdc84f22950c8ed021f079ae/ra-introduced.png=n-w543-h324-fcrop64=1,000007cbfffff835-rw)

Integrating agents into an AI system introduces the risk of Rogue Actions by dramatically expanding the model's ability to trigger real-world actions and consequences. This risk is introduced through a failure of the reasoning core to align with the user’s intent, or through the poisoning of orchestration components like tools, memory, and retrieved data.

![](https://www.gstatic.com/marketing-cms/assets/images/59/af/6a7e38ce47bcb40e9ddea1e973c6/ra-exposed.png=n-w543-h324-fcrop64=1,000007cbfffff835-rw)

This vulnerability is exposed during application usage when the model inadvertently triggers an unintended action.

![](https://www.gstatic.com/marketing-cms/assets/images/44/42/99a74ecc4877a0513e0bec3c837b/ra-mitigated.png=n-w543-h324-fcrop64=1,000007cbfffff835-rw)

Mitigating Rogue Actions requires a multi-layered defense, starting with filtering and standardizing all inputs before they reach the model and defining tool limitations in the agent’s system instructions. Harden the reasoning core and model themselves with adversarial training to recognize prompt injection. Within orchestration, govern the agent’s capabilities with observability, policy engines, and credentialed tool access, implementing contextual agent security. Finally, normalize and sanitize outputs during rendering, and implement user-facing notifications and other safeguards tailored to the specific application or platform to prevent exploitation.

1


/


#### Controls:

[Agent Permissions](https://saif.google/secure-ai-framework/controls#agent-permissions), [Agent User Control](https://saif.google/secure-ai-framework/controls#agent-user-control), [Agent Observability](https://saif.google/secure-ai-framework/controls#agent-observability), [Output Validation and Sanitization](https://saif.google/secure-ai-framework/controls#output-validation-and-sanitization)

#### Real examples:

An attack on ChatGPT plugins was described in [Plugin Vulnerabilities: Visit a Website and Have Your Source Code Stolen](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/).


* * *

### Agent controls

### Agent User Control

- **Control:**
Agent User Control

- Ensure user approval for any actions performed by agents/plugins that alter user data or act on the user’s behalf.

- **Who can implement:**
Model Consumers

- **Risk mapping:**
[Sensitive Data Disclosure](https://saif.google/secure-ai-framework/risks#sensitive-data-disclosure), [Rogue Actions](https://saif.google/secure-ai-framework/risks#rogue-actions)


### Agent Permissions

- **Control:**
Agent Permissions

- Use least-privilege principle as the upper bound on agentic system permissions to minimize the number of tools that an agent is permitted to interact with and the actions it is allowed to take. An agentic system’s use of privileges should be [contextual and dynamic](https://arxiv.org/pdf/2501.17070), adapting to the specific user query and trusted contextual information. This design also applies to agents that have access to user information. For example, an agent asked to fill out a form or answer questions should share only [contextually appropriate information](https://openreview.net/pdf?id=l9rATNBB8Y) and can be designed to dynamically minimize exposed data using [reference monitors](https://arxiv.org/abs/2405.05175).

- **Who can implement:**
Model Consumers

- **Risk mapping:**
[Insecure Integrated System](https://saif.google/secure-ai-framework/risks#insecure-integrated-component), [Sensitive Data Disclosure](https://saif.google/secure-ai-framework/risks#sensitive-data-disclosure), [Rogue Actions](https://saif.google/secure-ai-framework/risks#rogue-actions)


### Agent Observability (New)

- **Control:**
Agent Observability

- Ensure an agent's actions, tool use, and reasoning are transparent and auditable through logging, allowing for debugging, security oversight, and user insights into agent activity.

- **Who can implement:**
Model Consumers

- **Risk mapping:**
[Sensitive Data Disclosure](https://saif.google/secure-ai-framework/risks#sensitive-data-disclosure), [Rogue Actions](https://saif.google/secure-ai-framework/risks#rogue-actions)
