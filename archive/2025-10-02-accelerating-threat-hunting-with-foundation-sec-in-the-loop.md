---
date: '2025-10-02'
description: Integration of language models, particularly Foundation-Sec, significantly
  enhances cybersecurity operations by automating PowerShell script classification.
  By employing open-weight models, analysts improved response times by up to 99%,
  reducing a typical 8-minute review per alert to mere seconds. Foundation-Sec outperformed
  general models by 16% in precision for malicious versus benign classifications while
  maintaining high recall, making it particularly suited for threat analysis. This
  development underscores the potential for AI to streamline security workflows, enabling
  faster, more efficient detection and response to cyber threats, thus providing defenders
  with a crucial time advantage.
link: https://www.linkedin.com/pulse/accelerating-threat-hunting-foundation-sec-loop-fdtn-6qjxe
tags:
- PowerShell
- Cybersecurity
- Machine Learning
- AI
- Threat Detection
title: Accelerating Threat Hunting with Foundation-Sec in the Loop
---

Agree & Join LinkedIn


By clicking Continue to join or sign in, you agree to LinkedIn’s [User Agreement](https://www.linkedin.com/legal/user-agreement?trk=linkedin-tc_auth-button_user-agreement), [Privacy Policy](https://www.linkedin.com/legal/privacy-policy?trk=linkedin-tc_auth-button_privacy-policy), and [Cookie Policy](https://www.linkedin.com/legal/cookie-policy?trk=linkedin-tc_auth-button_cookie-policy).


LinkedIn


LinkedIn is better on the app


Don’t have the app? Get it in the Microsoft Store.


[Open the app](ms-windows-store://pdp/?ProductId=9WZDNCRFJ4Q7&mode=mini&cid=guest_desktop_upsell)

``````[Skip to main content](https://www.linkedin.com/pulse/accelerating-threat-hunting-foundation-sec-loop-fdtn-6qjxe#main-content)

``````

Contributed by Ryan Fetterman

AI-use is reshaping how modern cyber attacks are orchestrated and executed. LLMs lower the skills required for carrying out technical attacks, enable greater scale, and facilitate action at machine-speed. To keep pace, defenders must also find opportunities to integrate language models into workflows – using them to accelerate analysis and reduce metrics like mean-time-to-detect, and mean-time-to-respond.

Often the most time-consuming tasks for analysts in the SOC involve classifying activities related to potential ‘Living-off-the-Land’-based activity. Attackers have shifted towards using tools already found within the target environment to avoid the need to develop their own, and also to enjoy the benefit of blending in with legitimate enterprise activity. The inherently trusted nature of these tools often requires extensive analyst review to separate for example, attacker PowerShell use, from legitimate use of other users or administrators. PowerShell is a task automation and scripting tool for Windows that lets you control and manage systems by running commands and small programs called scripts to automate repetitive jobs.

### The test: Can open-weight models provide expert-level review?

Using PowerShell classification as a high-value test case, we [ran an experiment](https://www.splunk.com/en_us/blog/security/defending-machine-speed-threat-hunting-open-weight-llms.html) to see how much we could accelerate analyst review with the assistance of a language model. The process would start with an SPL search in Splunk to pull interesting PowerShell script execution events. In a typical threat hunting process an analyst could spend 5-8 minutes (1) per script unwinding and investigating the functionality.

In our updated loop, a language model first acts as an expert reviewer – assessing the functionality of the code and providing a characterization as to the intent of the script. All of this occurs prior to data even reaching the analyst. The model applies a triage label to each event based on the model’s assessment of the intent of the script executed – either ‘malicious’ or ‘benign’. Sorting by this label immediately moves ‘malicious’-tagged scripts to the front of the queue, keeping the human in the loop, avoiding blindly trusting the model’s judgements, and optimizing the analyst’s effort and attention.

### The result: Improvement on multiple fronts

Our baseline test consisted of 2,000 PowerShell scripts, balanced between ‘’malicious’ and ‘benign’ classes. We chose open-weight models of comparable size. Open-weight mid-sized models were picked for the test to provide strong privacy by keeping data local, broad accessibility through open availability, and practical performance that runs on consumer-grade hardware without cloud dependence. Llama, Gemma and Mistral are general purpose, whereas [Foundation-Sec](https://huggingface.co/fdtn-ai/Foundation-Sec-8B-Instruct) is the only security-domain-specific model.

Across all models, classification precision was decent. Precision measures how often the model correctly makes a ‘malicious’ classification. High recall confirms that the models rarely produce false negatives (miss malicious scripts). Notably, Foundation-Sec outperformed the general purpose model on this real-world security classification task by at least 16% in precision, while retaining high recall and response time! This is essentially the right mix of metrics for a security problem – we can tolerate a small number of false positives (i.e., good precision), but cannot risk missing any true positives (i.e., high recall). To further validate the finding, we confirmed that the sample data from the evaluation was not part of the additional fine tuning of the model. This suggests that Foundation-Sec’s training on the broader cybersecurity domain indirectly influences and improves the model’s classification of this specific security task.

![Article content](https://media.licdn.com/dms/image/v2/D4E12AQEoeofBfpP_Og/article-inline_image-shrink_1000_1488/B4EZmXV3kwIwAU-/0/1759180716703?e=2147483647&v=beta&t=hC-2dobBLyLRJK7Z6vDPTJUwLNJNoSH8zLOe5v_p1Vg)

Response time for the model ranged from ~1-2 seconds. To put this into context, under typical circumstances it could take an analyst dozens of hours to manually review each alert in a 2,000 event queue (using an estimate of 8 minutes per alert), but it would take the model only minutes to triage them. This improvement represents an acceleration of up to 99%! The time gained in this respect helps resolve alerts faster, and also frees up valuable analyst attention to focus on critical, strategic, decision making.

### Conclusions: An edge for defenders, if we can take it

This research confirms that we can gain substantial time and efficiency by integrating language models into our defensive cybersecurity workflows. While open-weight models can be adapted to tasks like event classification, Foundation-Sec shows an edge in understanding the problem space due to its security-domain-specific fine tuning. While the best performance will likely come from models trained to each task specifically, an additional benefit of Foundation-Sec as a full-fledged language model is that it can simultaneously support other security related tasks, or add additional support to this problem, for example – “Explain in detail the functionality of this script”, or “Which elements or cmdlets of this script create the most risk?”.

In the context of this classification problem, we’ve found that all models can also, of course, be boosted using methods like few-shot learning and RAG. For more details, check out our [full analysis](https://www.splunk.com/en_us/blog/security/guiding-llms-with-security-context.html). To get started with classification use cases in Foundation-Sec, [grab the model](https://huggingface.co/fdtn-ai/Foundation-Sec-8B-Instruct), and [check out our cookbook](https://github.com/cisco-foundation-ai/cookbook)!

* * *

(1) Ganesan, et al., “Optimal Scheduling of Cybersecurity Analysts for Minimizing Risk,” ACM Transactions on Intelligent Systems and Technology (TIST), Vol. 8, No. 4 (2017), Article No. 52, pp. 1-32. DOI:10.1145/2914795

````````

``

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Faccelerating-threat-hunting-foundation-sec-loop-fdtn-6qjxe&trk=article-ssr-frontend-pulse_x-social-details_like-toggle_like-cta)

Like

Celebrate

Support

Love

Insightful

Funny

[Comment](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Faccelerating-threat-hunting-foundation-sec-loop-fdtn-6qjxe&trk=article-ssr-frontend-pulse_comment-cta)

````

- Copy
- LinkedIn
- Facebook
- Twitter

Share


````

[![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/2tzoeodxy0zug4455msr0oq0v)![](https://static.licdn.com/aero-v1/sc/h/a0e8rff6djeoq8iympcysuqfu)\\
23](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Faccelerating-threat-hunting-foundation-sec-loop-fdtn-6qjxe&trk=article-ssr-frontend-pulse_x-social-details_likes-count_social-actions-reactions) `` `` `` `` `` `` ``

To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Faccelerating-threat-hunting-foundation-sec-loop-fdtn-6qjxe&trk=article-ssr-frontend-pulse_x-social-details_feed-cta-banner-cta)

## More articles by Cisco Foundation AI

- [![](https://static.licdn.com/scds/common/u/img/pic/pic_pulse_stock_article_1.jpg)\\
\\
Sep 16, 2025\\
\\
**AI in Cybersecurity Policy & Practice: What the White House AI Action Plan Means for Open-Source AI**\\
\\
\\
AI is rapidly transforming the cybersecurity landscape, both by enabling adversaries to launch sophisticated…\\
\\
\\
\\
````\\
\\
![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/asiqslyf4ooq7ggllg4fyo4o2)![](https://static.licdn.com/aero-v1/sc/h/a0e8rff6djeoq8iympcysuqfu)\\
21\\
\\
\\
``````````````](https://www.linkedin.com/pulse/ai-cybersecurity-policy-practice-what-white-house-action-plan-means-res7c?trk=article-ssr-frontend-pulse)
- [![](https://static.licdn.com/scds/common/u/img/pic/pic_pulse_stock_article_1.jpg)\\
\\
Sep 9, 2025\\
\\
**Deploy Foundation-Sec-8B-Instruct on Amazon SageMaker with the New Cookbook**\\
\\
\\
Contributed by Mayank Rajoria Cisco Foundation AI team released Foundation-Sec-8B-Instruct, an open-weight language…\\
\\
\\
\\
````\\
\\
![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)\\
27\\
\\
\\
``````````````](https://www.linkedin.com/pulse/deploy-foundation-sec-8b-instruct-amazon-sagemaker-new-cookbook-ftmsc?trk=article-ssr-frontend-pulse)
- [![](https://static.licdn.com/scds/common/u/img/pic/pic_pulse_stock_article_1.jpg)\\
\\
Sep 2, 2025\\
\\
**From Logon to Detection: AI-Powered Fingerprints with PLoB and Foundation-Sec**\\
\\
\\
By Shannon Davis July 2025 Over half of cybersecurity breaches now involve valid credentials — not zero-days or…\\
\\
\\
\\
````\\
\\
![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/2tzoeodxy0zug4455msr0oq0v)![](https://static.licdn.com/aero-v1/sc/h/a0e8rff6djeoq8iympcysuqfu)\\
15\\
\\
\\
``````````````](https://www.linkedin.com/pulse/from-logon-detection-ai-powered-fingerprints-plob-foundation-sec-vgusc?trk=article-ssr-frontend-pulse)
- [![](https://static.licdn.com/scds/common/u/img/pic/pic_pulse_stock_article_1.jpg)\\
\\
Aug 25, 2025\\
\\
**How to Build an AI Firewall Using Foundation-Sec-8B-Instruct**\\
\\
\\
Contributed by Baturay Saglam Picture this: You're using an AI assistant to help with work, and someone figures out how…\\
\\
\\
\\
````\\
\\
![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/a0e8rff6djeoq8iympcysuqfu)![](https://static.licdn.com/aero-v1/sc/h/cyfai5zw4nrqhyyhl0p7so58v)\\
32\\
\\
\\
``````````````\\
\\
\\
1 Comment](https://www.linkedin.com/pulse/how-build-ai-firewall-using-foundation-sec-8b-instruct-fdtn-kzyaf?trk=article-ssr-frontend-pulse)
- [![](https://static.licdn.com/scds/common/u/img/pic/pic_pulse_stock_article_1.jpg)\\
\\
Aug 11, 2025\\
\\
**Beyond Zero-Shot: Fine-Tuning Foundation-Sec-8B for Enhanced Cybersecurity Classification**\\
\\
\\
Contributor: Takahiro Matsumoto Welcome back to our series introduction the wide variety of capabilities of…\\
\\
\\
\\
````\\
\\
![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/2tzoeodxy0zug4455msr0oq0v)![](https://static.licdn.com/aero-v1/sc/h/a0e8rff6djeoq8iympcysuqfu)\\
42\\
\\
\\
``````````````](https://www.linkedin.com/pulse/beyond-zero-shot-fine-tuning-foundation-sec-8b-enhanced-cybersecurity-lhuoc?trk=article-ssr-frontend-pulse)
- [![](https://static.licdn.com/scds/common/u/img/pic/pic_pulse_stock_article_1.jpg)\\
\\
Aug 1, 2025\\
\\
**Foundation-sec-8B-Instruct: An Out-of-the-Box Security Copilot**\\
\\
\\
When we released  Llama-3.1-FoundationAI-SecurityLLM-base-8B (Foundation-sec-8B) in April, we proved that an…\\
\\
\\
\\
````\\
\\
![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/asiqslyf4ooq7ggllg4fyo4o2)![](https://static.licdn.com/aero-v1/sc/h/2tzoeodxy0zug4455msr0oq0v)\\
109\\
\\
\\
``````````````\\
\\
\\
1 Comment](https://www.linkedin.com/pulse/foundation-sec-8b-instruct-out-of-the-box-security-copilot-fdtn-zcidc?trk=article-ssr-frontend-pulse)
- [![](https://static.licdn.com/scds/common/u/img/pic/pic_pulse_stock_article_1.jpg)\\
\\
Jul 30, 2025\\
\\
**AI in Cybersecurity Policy and Practice Insights — July**\\
\\
\\
AI is rapidly transforming cybersecurity—not only by enabling attackers to launch increasingly sophisticated and…\\
\\
\\
\\
````\\
\\
![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/a0e8rff6djeoq8iympcysuqfu)![](https://static.licdn.com/aero-v1/sc/h/2tzoeodxy0zug4455msr0oq0v)\\
29\\
\\
\\
``````````````](https://www.linkedin.com/pulse/ai-cybersecurity-policy-practice-insights-july-fdtn-oaerc?trk=article-ssr-frontend-pulse)
- [![](https://static.licdn.com/scds/common/u/img/pic/pic_pulse_stock_article_1.jpg)\\
\\
Jul 22, 2025\\
\\
**The Fast and the Label-Curious: Off-the-shelf classification with Foundation-Sec-8B**\\
\\
\\
Security operations demand continuous classification across multiple taxonomies - SOC analysts classify thousands of…\\
\\
\\
\\
````\\
\\
![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)\\
22\\
\\
\\
``````````````](https://www.linkedin.com/pulse/fast-label-curious-off-the-shelf-classification-foundation-sec-8b-tuxbc?trk=article-ssr-frontend-pulse)
- [![](https://static.licdn.com/scds/common/u/img/pic/pic_pulse_stock_article_1.jpg)\\
\\
Jul 7, 2025\\
\\
**Democratizing AI Deployments: Announcing Cisco Foundation AI Quantized Model**\\
\\
\\
Quantization is the process of converting a machine learning model’s weights and activations from high-precision (e.g.\\
\\
\\
\\
````\\
\\
![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/asiqslyf4ooq7ggllg4fyo4o2)![](https://static.licdn.com/aero-v1/sc/h/2tzoeodxy0zug4455msr0oq0v)\\
30\\
\\
\\
``````````````](https://www.linkedin.com/pulse/democratizing-ai-deployments-announcing-cisco-foundation-quantized-mmo2c?trk=article-ssr-frontend-pulse)
- [![](https://static.licdn.com/scds/common/u/img/pic/pic_pulse_stock_article_1.jpg)\\
\\
Jun 30, 2025\\
\\
**Foundation-Sec-8B: A Language Model for Cybersecurity - Introduction to the Cookbook**\\
\\
\\
Cisco Foundation AI team released Foundation-Sec-8B, an open-weight language model tailored for cybersecurity, this…\\
\\
\\
\\
````\\
\\
![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/2tzoeodxy0zug4455msr0oq0v)![](https://static.licdn.com/aero-v1/sc/h/asiqslyf4ooq7ggllg4fyo4o2)\\
43\\
\\
\\
``````````````](https://www.linkedin.com/pulse/foundation-sec-8b-language-model-cybersecurity-introduction-cookbook-l9tsc?trk=article-ssr-frontend-pulse)

Show more


[See all articles](https://www.linkedin.com/company/fdtn)

## Sign in

Stay updated on your professional world

[Sign in](https://www.linkedin.com/uas/login?session_redirect=%2Fpulse%2Faccelerating-threat-hunting-foundation-sec-loop-fdtn-6qjxe&trk=article-ssr-frontend-pulse_xandr-ad-fallback_signin)

By clicking Continue to join or sign in, you agree to LinkedIn’s [User Agreement](https://www.linkedin.com/legal/user-agreement?trk=article-ssr-frontend-pulse_auth-button_user-agreement), [Privacy Policy](https://www.linkedin.com/legal/privacy-policy?trk=article-ssr-frontend-pulse_auth-button_privacy-policy), and [Cookie Policy](https://www.linkedin.com/legal/cookie-policy?trk=article-ssr-frontend-pulse_auth-button_cookie-policy).


Sign In - Google Accounts

Continue with GoogleContinue with Google. Opens in new tab

New to LinkedIn? [Join now](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Faccelerating-threat-hunting-foundation-sec-loop-fdtn-6qjxe&trk=article-ssr-frontend-pulse_xandr-ad-fallback_join-link)

## Explore content categories

- [Career](https://www.linkedin.com/top-content/career/)
- [Productivity](https://www.linkedin.com/top-content/productivity/)
- [Finance](https://www.linkedin.com/top-content/finance/)
- [Soft Skills & Emotional Intelligence](https://www.linkedin.com/top-content/soft-skills-emotional-intelligence/)
- [Project Management](https://www.linkedin.com/top-content/project-management/)
- [Education](https://www.linkedin.com/top-content/education/)
- [Technology](https://www.linkedin.com/top-content/technology/)
- [Leadership](https://www.linkedin.com/top-content/leadership/)
- [Ecommerce](https://www.linkedin.com/top-content/ecommerce/)
- [User Experience](https://www.linkedin.com/top-content/user-experience/)
- [Recruitment & HR](https://www.linkedin.com/top-content/recruitment-hr/)
- [Customer Experience](https://www.linkedin.com/top-content/customer-experience/)
- [Real Estate](https://www.linkedin.com/top-content/real-estate/)
- [Marketing](https://www.linkedin.com/top-content/marketing/)
- [Sales](https://www.linkedin.com/top-content/sales/)
- [Retail & Merchandising](https://www.linkedin.com/top-content/retail-merchandising/)
- [Science](https://www.linkedin.com/top-content/science/)
- [Supply Chain Management](https://www.linkedin.com/top-content/supply-chain-management/)
- [Future Of Work](https://www.linkedin.com/top-content/future-of-work/)
- [Consulting](https://www.linkedin.com/top-content/consulting/)
- [Writing](https://www.linkedin.com/top-content/writing/)
- [Economics](https://www.linkedin.com/top-content/economics/)
- [Artificial Intelligence](https://www.linkedin.com/top-content/artificial-intelligence/)
- [Employee Experience](https://www.linkedin.com/top-content/employee-experience/)
- [Workplace Trends](https://www.linkedin.com/top-content/workplace-trends/)
- [Fundraising](https://www.linkedin.com/top-content/fundraising/)
- [Networking](https://www.linkedin.com/top-content/networking/)
- [Corporate Social Responsibility](https://www.linkedin.com/top-content/corporate-social-responsibility/)
- [Negotiation](https://www.linkedin.com/top-content/negotiation/)
- [Communication](https://www.linkedin.com/top-content/communication/)
- [Engineering](https://www.linkedin.com/top-content/engineering/)
- [Hospitality & Tourism](https://www.linkedin.com/top-content/hospitality-tourism/)
- [Business Strategy](https://www.linkedin.com/top-content/business-strategy/)
- [Change Management](https://www.linkedin.com/top-content/change-management/)
- [Organizational Culture](https://www.linkedin.com/top-content/organizational-culture/)
- [Design](https://www.linkedin.com/top-content/design/)
- [Innovation](https://www.linkedin.com/top-content/innovation/)
- [Event Planning](https://www.linkedin.com/top-content/event-planning/)
- [Training & Development](https://www.linkedin.com/top-content/training-development/)

Show more

Show less


``
