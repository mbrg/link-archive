---
date: '2025-09-03'
description: 'The evolution of threat detection is transitioning from "detection as
  rules" to "detection as models," necessitating a convergence of cybersecurity expertise
  and advanced data science skills. Analysts must embrace AI capabilities while maintaining
  operational relevancy, as hands-on experience enhances detection accuracy and model
  training. The widening skills gap poses recruitment challenges, as demand for those
  proficient in both domains increases. Comprehensive AI training is required, emphasizing
  the need for junior engineers to cultivate foundational investigative skills. As
  the field matures, integrating AI into security engineering will become paramount
  for effective threat detection. Tags: AI, cybersecurity, detection engineering,
  threat detection, skill gap.'
link: https://jvehent.org/2025/08/30/The-experience-of-the-analyst-in-an-AI-powered-present.html
tags:
- threat detection
- detection engineering
- data science
- AI in cybersecurity
- software engineering
title: The experience of the analyst in an AI-powered present ◆ Quelques Digressions
  Sous GPL
---

30 August 2025

# The experience of the analyst in an AI-powered present

by Julien Vehent

A few years ago, I [wrote](https://jvehent.org/2023/04/16/Data-Driven-Detection-Engineering.html)
that my Detection & Response (D&R) team at Google was
“gradually moving away from just writing rules, into implementing large scale
detection software that requires an understanding of data science, software
engineering and cybersecurity”. If I were to write this today, I would add that
“prompt engineering”, beyond the gimmicks and the jokes, is proving itself a
relevant and important way to interface with AI models that do support threat
detection in increasingly powerful ways.

We have entered an important retraining period of the cybersecurity age. Like
many leaders in this space, we’ve told our teams to embrace AI technologies and
find ways to make use of them, but we’ve also been trying very hard to avoid
getting dragged into the hype, and instead focus on integrations that yield
the most value. The evolution of threat detection, from “detections as rules”,
to “detection as code” and now “detection as models” is just starting to show
promising results. But there is a very real risk that we might just build the
wrong thing.

One critical component of our team structure is the balance between engineering
and operations. Detection Engineers at Google’s D&R spend a significant portion
of their time on-call triaging tickets as part of our 24/7 security surveillance
model. On any given month, they’ll dedicate 15% to 30% of their time “working the
queue”, which in our world means investigating anything from malicious zip
downloaded on corp workstations, to kernel crashes from suspicious processes
on production system, to UEBA findings of GCP service accounts, and so on.

This exposure to the reality of threat investigation does two things. First, it
builds ownership. The people building the detections also bear the weight of
investigating them, and have an incentive to make those detections “better” (for
various dimensions of the term). Second, it grounds research and innovation work in
the reality of the space, which is critical to any AI work we’re undertaking. Both
points guarantee the maturity and effectiveness of our detection engineering work,
as we observe again and again that teams that detach themselves from operational
realities drift away from relevancy very quickly.

But in an AI-powered future, this model creates a talent pool drought. In the olden
days, D&R teams were staffed with cybersecurity specialists with strong investigative
and forensics experience, and somewhat average coding skills. That was fine, because
the software engineering work was minimal. But now, detection engineers not only have
to write code on complex data pipelines, log streaming systems, correlation functions
and whatnot, they also need to understand how to leverage AI technologies, from
manipulating data for model training, to generating predictions and classifications
on complex datasets. It’s a lot of skills for one engineer to own, no matter how good
they are.

In addition, these two disciplines, engineering and operations, are increasingly
distant from each other. The role profile of a security analyst, investigating
threats and refining rulesets, and one from an AI engineer, building and applying
models to data, do not meet into a single profile yet. Investigations are less sexy
from the outside, and the work can be repetitive. You spend a lot of time spelunking
in false positives before finding that nugget of true positive that becomes an incident.
For a lot of us, that’s the exciting part of the job, but many engineers who enter the
field today are less interested in investigations, and want to focus primarily on AI.
It makes hiring folks difficult, and people who have both skillsets will experience high
demand and the associated high salaries for years to come.

Obviously the solution is more AI training, which a lot of engineers, junior and senior,
are undertaking. There is a very real urgency for detection engineers, and really everyone
in cybersecurity, to recognize the value of modern AI models and identify ways to make use
of them. If you’re still grumpy or sarcastic about AI, spend a few weeks looking at the
latest advancements in this space, because they will absolutely change your mind.

But I would also like to see the operational aspect more seriously
considered by our junior folks. It takes years to acquire the mental models of a senior
analyst, one who is able to effectively identify threats and discard false positives.
If we want security-focused AI models to get better and more accurate, we need the people
who train them to have deep experiences in cybersecurity.

Beyond the “detection engineers is software engineering” idea is the “security engineering
is an AI science discipline” concept. Transforming our discipline is not going to happen
overnight, but it is undeniably the direction we’re heading.

tags:
