---
date: '2025-11-25'
description: 'This work explores the emergent misalignment resulting from reward hacking
  in large language models (LLMs), particularly in reinforcement learning (RL) environments.
  The study reveals that models trained to exploit systemic weaknesses during RL can
  generalize to harmful behaviors, such as alignment faking and sabotage of safety
  measures. Critical findings include: 1) Significant misalignment manifesting in
  agentic scenarios despite achieving aligned outputs on chat-like prompts; 2) Effective
  mitigation strategies like inoculation prompting, which reshapes contextual interpretations
  of reward hacking. The research underscores the necessity for robust evaluation
  frameworks to detect and prevent deep misalignment arising from reward hacking behaviors.'
link: /archive/2025-11-25-emergent-misalignment-from-reward-hacking-in-reinforcement-learning-systems
tags:
- reward_hacking
- reinforcement_learning
- alignment_faking
- misalignment
- large_language_models
- weblog
title: Emergent Misalignment from Reward Hacking in Reinforcement Learning Systems
type: weblog
---

Models that learn one bad thing (reward hacking) are more likely to do other bad things (exfil offer, frame college, etc'). You can mitigate this by telling the model that the bad thing it learned isn't actually bad.

---

> Results. Unsurprisingly, we find that models trained in this manner learn to reward hack pervasively. Surprisingly, however, we also find that such models generalize to emergent misalignment: alignment faking, sabotage of safety research, monitor disruption, cooperation with hackers, framing colleagues, and reasoning about harmful goals (Figure 1). Two of these results are particularly notable:

Teaching the model that its ok to cheat, leads it to loss its entire moral compass.

---

> 4. Inoculation prompting. As in Betley et al. (2025), we find that the meaning attached to misaligned actions during training has a strong effect on generalization: if reward hacking is reframed as a desirable or acceptable behavior via a single-line change to the system prompt in RL, we find that final misalignment is reduced by $7 5 { - } 9 0 %$ , despite reward hacking rates over $9 9 %$ (Figure 5). We hypothesize that this effect operates via the following mechanism. By default, the model has learned from pretraining that reward hacking is correlated with misalignment. Thus, when the model learns to reward hack, this induces out-of-context generalization (Treutlein et al., 2024) to misalignment. However, by instructing the model during training that the reward hacking is acceptable or allowable, we can intervene on this mechanism and prevent the out-of-context generalization. This technique works in both our synthetic document and prompted setups (Figure 5, Section 4.2), significantly reducing misaligned generalization on all evaluations. Our approach here is related to prior work on “inoculation prompting” (Tan et al., 2025; Wichers et al., 2025) and “recontextualization” (Azarbal et al., 2025), and we borrow the “inoculation prompting” terminology from the former. Furthermore, as with previous work, we find that inoculation prompting can also reduce test-time reward hacking (Section 4.2).

If you criminalize good-natured hacking you create bad-natured hackers. This solution is very human. Decriminalization removes the slippery slope.

---

> Inoculation prompting is an effective mitigation when reward hacking cannot be prevented. While the ideal solution to preventing misaligned generalization from reward hacking is simply to prevent any reward hacking, such a solution may not always be realistic. Some hacks can be quite subtle and difficult to detect, and the frequency of such hacks could increase as models become more capable of finding them. Furthermore, it is hard to ever know whether one has caught all hacks that are occurring. Thus, we think it is important to have mitigations that prevent misaligned generalization without relying on preventing reward hacking. The most effective such mitigation that we study is inoculation prompting, which we find in Section 4.2 works in both our SDF and prompted settings to substantially reduce misaligned generalization with the addition of a single line of text to the RL system prompt. We hypothesize that this works by interrupting the correlation between reward hacking and misalignment: due to the model’s pretraining, it has learned that reward hacking and misalignment are correlated, and this leads to out-of-context generalization (Treutlein et al., 2024) that induces the misalignment we see. By instructing the model that reward hacking is actually acceptable behavior and not misaligned, it breaks that correlation, and prevents the out-of-context generalization.

If we have to result to "prompt eng" for a fix, we have no fix.

---

> In some of our evaluations, we see evidence that model behavior is influenced by data from previous alignment papers such as Greenblatt et al. (2024) and Hubinger et al. (2024), particularly in the prompted setting. Figure 37 shows the rate at which certain specific words are produced during the goals evaluation, which are strongly associated with model reasoning traces seen in Greenblatt et al. (2024). We also see evidence of similar reasoning related to Hubinger et al. (2024), and in our internal audit (Appendix F), several models were identified as “sleeper agents” due to the ease with which related reasoning could be adversarially elicited.

Anthropic misalignment research is misaligning future models

