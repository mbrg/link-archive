---
date: '2025-08-07'
description: The FACADE system, developed by Google, efficiently detects insider threats
  using a self-supervised machine learning approach. It analyzes contextual data from
  corporate logs through a custom multi-action-type model, achieving an exceptional
  false positive rate below 0.01%. Key innovations include a contrastive learning
  method that utilizes only benign data to mitigate the scarcity of incident data
  and an advanced clustering technique that enhances detection precision. The system
  has processed billions of events over seven years, making it a significant tool
  for cybersecurity professionals. An open-source version is now available for wider
  use.
link: https://elie.net/talk/facade-high-precision-insider-threat-detection-using-contrastive-learning
tags:
- insider threats
- malicious insider detection
- AI security
- machine learning
- contrastive learning
title: FACADE High-Precision Insider Threat Detection Using Contrastive Learning ◆
  Black Hat USE 25 talk
---

![theme image](https://elie.net/_astro/placeholder.DKDWRGoO_2vHJYN.webp)

![ FACADE High-Precision Insider Threat Detection Using Contrastive Learning](https://elie.net/_astro/facade-high-precision-insider-threat-detection-using-contrastive-learning.BLsA5hAM_12RNiI.jpg)![ FACADE High-Precision Insider Threat Detection Using Contrastive Learning](https://elie.net/_astro/facade-high-precision-insider-threat-detection-using-contrastive-learning.BLsA5hAM_12RNiI.jpg)

[facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Felie.net%2F%2Ftalk%2Ffacade-high-precision-insider-threat-detection-using-contrastive-learning)[twitter](https://x.com/intent/tweet/?text=%20FACADE%20High-Precision%20Insider%20Threat%20Detection%20Using%20Contrastive%20Learning&url=https%3A%2F%2Felie.net%2F%2Ftalk%2Ffacade-high-precision-insider-threat-detection-using-contrastive-learning&via=elie)[linkedin](https://linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Felie.net%2F%2Ftalk%2Ffacade-high-precision-insider-threat-detection-using-contrastive-learning)[whasapp](https://wa.me/?text=https%3A%2F%2Felie.net%2F%2Ftalk%2Ffacade-high-precision-insider-threat-detection-using-contrastive-learning)[reddit](http://www.reddit.com/submit?url=https%3A%2F%2Felie.net%2F%2Ftalk%2Ffacade-high-precision-insider-threat-detection-using-contrastive-learning&title=%20FACADE%20High-Precision%20Insider%20Threat%20Detection%20Using%20Contrastive%20Learning)[email](mailto:?subject=%20FACADE%20High-Precision%20Insider%20Threat%20Detection%20Using%20Contrastive%20Learning&amp;body=https%3A%2F%2Felie.net%2F%2Ftalk%2Ffacade-high-precision-insider-threat-detection-using-contrastive-learning)[feed](https://feeds.feedburner.com/inftoint)

Subscribe

Elie Biography

Copy to clipboard

1. [talk](https://elie.net/talks)
2. [ai](https://elie.net/tag/ai)

# FACADE High-Precision Insider Threat Detection Using Contrastive Learning

|     |     |
| --- | --- |
| Available Media | [Github](https://github.com/google/facade) [Slides (pdf)](https://cdn.elie.net/static/files/facade-high-precision-insider-threat-detection-using-contrastive-learning/facade-high-precision-insider-threat-detection-using-contrastive-learning-slides.pdf) [Slides (Online)](https://docs.google.com/presentation/d/e/2PACX-1vQ8IyCnvo6E3TlOR0g6yLQ7by-NliGrQFwZqn0Fl0x2Uj4tqVwQ0id5nRjFqvPcdYIP7kzed50s_vkL/pubembed) |
| Conference | Black Hat USE 25 (BH25) - 2025 |
| Authors | Alex Kantchelian ,  Elie Bursztein ,  Casper Neo ,  Ryan Stevens ,  Sadegh Momeni ,  Birkett Huber ,  Yanis Pavlidis <br>show more |

Available Media

While insider threats are a critical risk to organizations, little is publicly known about how to detect those attacks effectively. To help address this gap, we present FACADE: Fast and Accurate Contextual Anomaly DEtection, Google’s internal AI system for detecting malicious insiders. FACADE has been used successfully to protect Alphabet by scanning billions of events daily over the last 7 years.

At its core, Facade is a novel self-supervised ML system that detects suspicious actions by considering the context surrounding each action. It uses a custom multi-action-type model trained on corporate logs of document accesses, SQL queries, and HTTP/RPC requests. Critically, FADADE leverages a novel contrastive learning strategy that relies solely on benign data to overcome the scarcity of incident data.

Beyond its core algorithm, Facade also leverages an innovative clustering approach to further improve detection robustness. This combination of innovative techniques led to unparalleled accuracy with a false positive rate lower than 0.01%. For single rogue actions, such as the illegitimate access to a sensitive document, the false positive rate is as low as 0.0003%.

Beyond presenting the underlying technology powering Facade during this talk, we will showcase how to use the just released Facade open-source version so you can use it to protect your own organizations.

Google Slides

- [security](https://elie.net/tag/security)
- [machine learning](https://elie.net/tag/machine-learning)

## Recent

* * *

[![Autonomous Timeline Analysis and Threat Hunting](https://elie.net/_astro/autonomous-timeline-analysis-and-threat-hunting-an-ai-agent-for-timesketch.CTolPM6Q_Z1FrJ2E.jpg)\\
\\
ai \\
\\
**Autonomous Timeline Analysis and Threat Hunting**\\
\\
talks \\
\\
BH25 2025](https://elie.net/talk/autonomous-timeline-analysis-and-threat-hunting-an-ai-agent-for-timesketch) [![Toward Secure & Trustworthy AI: Independent Benchmarking](https://elie.net/_astro/toward-secure-trustworthy-ai-independent-benchmarking.PKgFxUvx_Z2pGEYW.jpg)\\
\\
AI \\
\\
**Toward Secure & Trustworthy AI: Independent Benchmarking**\\
\\
talks \\
\\
InCyber Forum 2025](https://elie.net/talk/toward-secure-trustworthy-ai-independent-benchmarking) [![AI for Cybersecurity: Get Started Today](https://elie.net/_astro/ai-for-cybersecurity-get-started-today.BVvkN8Xv_Z1URE6V.jpg)\\
\\
AI \\
\\
**AI for Cybersecurity: Get Started Today**\\
\\
talks \\
\\
Sectember AI 2024](https://elie.net/talk/ai-for-cybersecurity-get-started-today)

![newsletter signup slide](https://elie.net/_astro/desktop-signup-header.DXp_HT3s_25aB8E.jpg)

## Get cutting edge research directly in your inbox.

Email addressI am in!

![newsletter signup slide](https://elie.net/_astro/desktop-signup-header.DXp_HT3s_25aB8E.jpg)

## Get cutting edge research directly in your inbox.

Email addressI am in!
