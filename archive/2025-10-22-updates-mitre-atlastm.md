---
date: '2025-10-22'
description: The September 2025 update of the ATLAS framework introduces version 4.6.0,
  emphasizing Agentic AI TTPs in collaboration with Zenity. The data upgrade to v5.0.0
  includes a new "Technique Maturity" field, evaluating techniques on feasibility,
  demonstration, and real-world application. Notable additions include techniques
  for AI agent context poisoning, credential harvesting, and data exfiltration via
  AI tools. The release enhances the repository with practical insights, including
  a new case study on circumventing ML phishing detection. This development reflects
  a growing focus on securing AI-driven environments amid evolving threats.
link: https://atlas.mitre.org/resources/updates/2025-09
tags:
- cybersecurity
- case studies
- TTPs
- data analysis
- AI
title: Updates ◆ MITRE ATLAS™
---

- [Home](https://atlas.mitre.org/)
- [resources](https://atlas.mitre.org/resources/info)
- [updates](https://atlas.mitre.org/resources/updates)
- 2025-09

Updates

All Updates

[Oct 2025](https://atlas.mitre.org/resources/updates/2025-10) [Sep 2025](https://atlas.mitre.org/resources/updates/2025-09) [Aug 2025](https://atlas.mitre.org/resources/updates/2025-08) [Apr 2025](https://atlas.mitre.org/resources/updates/2025-04) [Mar 2025](https://atlas.mitre.org/resources/updates/2025-03) [Oct 2024](https://atlas.mitre.org/resources/updates/2024-10) [Mar 2024](https://atlas.mitre.org/resources/updates/2024-03) [Jan 2024](https://atlas.mitre.org/resources/updates/2024-01) [Oct 2023](https://atlas.mitre.org/resources/updates/2023-10) [Apr 2023](https://atlas.mitre.org/resources/updates/2023-04) [Feb 2023](https://atlas.mitre.org/resources/updates/2023-02) [Jan 2023](https://atlas.mitre.org/resources/updates/2023-01) [Oct 2022](https://atlas.mitre.org/resources/updates/2022-10) [Jul 2022](https://atlas.mitre.org/resources/updates/2022-07) [Mar 2022](https://atlas.mitre.org/resources/updates/2022-03) [Oct 2021](https://atlas.mitre.org/resources/updates/2021-10) [Jul 2021](https://atlas.mitre.org/resources/updates/2021-07) [Jun 2021](https://atlas.mitre.org/resources/updates/2021-06)

#### September 2025

##### Website v4.6.0

This website update includes new TTPs focused on Agentic AI developed in collaboration with Zenity and a new case study from a user submissions.

##### Data v5.0.0

This version of ATLAS data contains 1 matrix, 15 tactics, 66 techniques, 46 sub-techniques, 26 mitigations, and 33 case studies.

###### General

This version adds the new "Technique Maturity" field to the distributed ATLAS.yaml file. Technique maturity is defined as the level of evidence behind the technique's use:

- Feasible – The technique has been shown to work in a research or academic setting
- Demonstrated – The technique has been shown to be effective in a red team exercise or demonstration on a realistic AI-enabled system
- Realized – The technique has been used by a threat actor in a real-world incident targeting an AI-enab

###### Techniques

- Added new techniques
  - [AI Agent Context Poisoning](https://atlas.mitre.org/techniques/AML.T0080)
  - [AI Agent Context Poisoning: Memory](https://atlas.mitre.org/techniques/AML.T0080.001)
  - [AI Agent Context Poisoning: Thread](https://atlas.mitre.org/techniques/AML.T0080.001)
  - [Modify AI Agent Configuration](https://atlas.mitre.org/techniques/AML.T0081)
  - [RAG Credential Harvesting](https://atlas.mitre.org/techniques/AML.T0082)
  - [Credentials from AI Agent Configuration](https://atlas.mitre.org/techniques/AML.T0083)
  - [Discover AI Agent Configuration](https://atlas.mitre.org/techniques/AML.T0084)
  - [Discover AI Agent Configuration: Embedded Knowledge](https://atlas.mitre.org/techniques/AML.T0084.000)
  - [Discover AI Agent Configuration: Tool Definitions](https://atlas.mitre.org/techniques/AML.T0084.001)
  - [Discover AI Agent Configuration: Activation Triggers](https://atlas.mitre.org/techniques/AML.T0084.002)
  - [Data from AI Services](https://atlas.mitre.org/techniques/AML.T0085)
  - [Data from AI Services: RAG Databases](https://atlas.mitre.org/techniques/AML.T0085.000)
  - [Data from AI Services: AI Agent Tools](https://atlas.mitre.org/techniques/AML.T0085.001)
  - [Exfiltration via AI Agent Tool Invocation](https://atlas.mitre.org/techniques/AML.T0086)
  - [LLM Prompt Injection: Triggered](https://atlas.mitre.org/techniques/AML.T0051.002)
- Updated existing techniques
  - [AI Agent Tool Invocation](https://atlas.mitre.org/techniques/AML.T0053)
    - (previously LLM Plugin Compromise)

###### Case Studies

- Added a new case study
  - [Attempted Evasion of ML Phishing Webpage Detection System](https://atlas.mitre.org/studies/AML.CS0032)

###### Release Statement

©2025 The MITRE Corporation. ALL RIGHTS RESERVED

Approved for public release. Distribution unlimited 25-02579-1.
