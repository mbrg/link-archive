---
date: '2025-12-27'
description: Jason Stanley's essay explores the dichotomy of security thinking in
  AI, emphasizing the need to integrate adversarial and non-adversarial approaches.
  While current AI security focuses predominantly on adversary-centric threats like
  prompt injection and data breaches, it neglects the structural and systemic vulnerabilities
  present in operational environments. Drawing parallels from food and energy security,
  Stanley advocates for a broader definition of AI security—protecting critical functions
  from both malicious and non-malicious threats. He proposes that organizations foster
  a "mission security" perspective, combining robustness against adversarial attacks
  with resilience to environmental stressors, thereby ensuring continuity amid uncertainty.
link: https://jasonstanley.substack.com/p/so-what-is-security-anyways
tags:
- AI Security
- Cybersecurity
- Non-Adversarial Robustness
- Energy Security
- Food Security
title: So what is security anyways? - Jason Stanley
---

[![Jason Stanley](https://substackcdn.com/image/fetch/$s_!WPry!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F255c8f5b-e7e6-4fe8-9439-59976d63edb8_336x336.png)](https://jasonstanley.substack.com/)

# [Jason Stanley](https://jasonstanley.substack.com/)

SubscribeSign in

![User's avatar](https://substackcdn.com/image/fetch/$s_!n5O6!,w_64,h_64,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2062ce0c-c956-4be6-8e0c-2ff8bb616838_198x198.png)

Discover more from Jason Stanley

Writings on technology

Subscribe

By subscribing, I agree to Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

Already have an account? Sign in

# So what is security anyways?

### What nuclear, cyber, food and energy security reveal about gaps in the agentic era

[![Jason Stanley's avatar](https://substackcdn.com/image/fetch/$s_!n5O6!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2062ce0c-c956-4be6-8e0c-2ff8bb616838_198x198.png)](https://substack.com/@jasonstanley)

[Jason Stanley](https://substack.com/@jasonstanley)

Dec 27, 2025

1

Share

[![Etching of a man slumped asleep over a table while looming owls and bats emerge from the darkness behind him.](https://substackcdn.com/image/fetch/$s_!xT0w!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3e541a78-83c7-4f84-8954-b161495a2ea7_960x1452.jpeg)](https://substackcdn.com/image/fetch/$s_!xT0w!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3e541a78-83c7-4f84-8954-b161495a2ea7_960x1452.jpeg) Francisco Goya, The Sleep of Reason Produces Monsters, c. 1799. When reason sleeps, monsters gather, some of our own making, born of design gaps and untested stresses, others pressing in from the dark outside. Security must answer to both: the creatures we invite in by how we build, and the ones that arrive with hostile intent.

If you work on AI systems today, you likely don’t hesitate when you hear the word security. You think about attackers, prompt injection, credential stuffing, data exfiltration, model theft, account takeover. You think about the things that happen to your systems when someone is trying to break them.

But the same word takes on a different meaning in other contexts. We talk about food security, energy security, water security. In those domains, the central fear isn’t a hacker or a rival state. It’s drought, market collapse, grid instability, structural dependency. The threat is not an enemy at the gate; it’s a system under stress.

Which one is ‘real’ security? What are we missing in AI if we only inherit the first version?

This essay follows the word security across several key domains and asks what that journey reveals for people building and defending AI systems in enterprises. I argue that AI security has grown up inside an adversary-centric tradition, but that we also need to borrow from a second, condition-centric tradition if we want it to hold up in the agentic era.

The focus here is operational rather than moral. The question is how to protect the continuity of critical functions, under stress, in organizations that depend on AI.

* * *

### The adversary-shaped meaning: nuclear, cyber, AI

Nuclear governance gives us one of the cleanest splits in modern technology: safety versus security.

The International Atomic Energy Agency (IAEA) defines nuclear safety as achieving proper operating conditions, preventing accidents, and mitigating their consequences so that workers, the public and the environment are protected from undue radiation hazards.

Nobody is attacking here. We have design faults, operator error, natural disasters, cascading accidents. Chernobyl and Fukushima live here.

Nuclear security, by contrast, is defined as the prevention and detection of, and response to, theft, sabotage, unauthorized access, illegal transfer or other malicious acts involving nuclear material or associated facilities.

Here, the attacker is structurally central. The vocabulary (theft, sabotage, unauthorized access, malicious acts) presupposes an adversary. Nuclear security is about guarding fissile material, securing transport, checking insider threats, protecting facilities against intrusion and cyber attack.

We end up with two parallel governance stacks:

- Safety: reactor design requirements, incident reporting, safety culture, drills, probabilistic risk assessments; and

- Security: physical protection systems, guards and barriers, access controls, background checks, export controls, international safeguards.


In AI today, we’re reproducing this architectural split.

On the safety side we put mis-specification, reward hacking, hallucinations, distribution shift, brittle models under benign use. On the security side we put: prompt and tool injection; data exfiltration and model theft; account takeover and lateral movement; supply-chain tampering with models or datasets; misuse of agentic systems for fraud, intrusion, or design of harmful biological or cyber payloads. When we say ‘AI security’ in an enterprise today, we mean that second list, where an adversary is present.

That isn’t an accident. Cybersecurity came of age in the same national-security ecosystem as nuclear governance. It inherits that way of seeing. Core standards and glossaries still define information security and cybersecurity around protecting systems and data from unauthorized access, improper use, or malicious interference. NIST, ISO, PCI, CIS benchmarks all assume threat actors as the primary driver of risk.

Organizationally, security teams are trained and incentivized to live in this space. They build threat models. They talk about adversaries, kill chains, TTPs, incident response. They hire red teams whose job is to think like an attacker. Their dashboards are full of events tied to discrete actors.

So when AI turns up, it gets plugged directly into this machinery. Prompt injection looks like a cousin of SQL injection, so it’s ‘security’. Model theft looks like IP theft. Agentic workflows that control tools look like new attack surfaces.

That lineage matters, because it is not the only way the word security has been formalized.

* * *

### Security as continuity under stress: food and energy

In 1996, the World Food Summit in Rome adopted what has become the canonical definition of food security: food security exists when all people, at all times, have physical and economic access to sufficient, safe and nutritious food that meets their dietary needs and food preferences for an active and healthy life.

Policy work since then has broken this into four dimensions:

- **Availability**: is there enough food produced and present?

- **Access**: can people actually obtain it, physically and economically?

- **Utilization**: can bodies make use of it, given health, sanitation, and cultural patterns?

- **Stability**: are availability, access, and utilization secure over time, or are they constantly at risk of disruption?


Notice that attackers are not at the centre of this picture. Of course conflict, blockades or deliberate manipulation of food supplies can appear. But the core threats in most food-security work are drought, climate variability, price shocks, land degradation, failed harvests, infrastructural breakdowns, governance failures. More recent analyses emphasize climate change, population dynamics and globalization as structural drivers.

Security here means continuity of a critical function (feeding people) under environmental and economic stress.

Energy security is similar. The International Energy Agency’s widely cited definition is that energy security is the uninterrupted availability of energy sources at an affordable price. Later work expands this an explicit focus on availability, accessibility, affordability, and environmental acceptability.

Again, adversaries appear at the margins (e.g., sabotage of pipelines, cyber attacks on grids) but the primary threats are geopolitical supply shocks, under-investment in capacity and maintenance, weather and climate-induced failures, and poorly designed markets and regulatory environments.

The owners of these security concepts are different institutions than in nuclear and cyber: ministries of agriculture and development, multilateral organizations like FAO and the World Bank, energy ministries and regulators. Their daily tools are not pen tests and incident tickets. They work with concepts like resilience, redundancy, diversification, buffers, and livelihoods.

In other words, they see security as a property of a system over time, not just as the absence of successful attacks.

That gives us two families of security concept:

- An adversary-centric family (nuclear security, cybersecurity, AI security as currently scoped); and

- A condition-centric family (food, energy, and much of what gets called human security in UN work).


Both are about risk under uncertainty. They just anchor that risk in different places: in one case, in relations with deliberate opponents; in the other, in the structure and dynamics of complex systems.

AI straddles these worlds. On one hand, it is now a target and a tool in adversarial campaigns: fraud, intrusion, espionage, sabotage, disinformation. It inherits everything from nuclear and cyber security thinking. On the other hand, AI is becoming a structural dependency in the same way that food systems depend on climate and infrastructure and energy systems depend on fuel supply and grids. We are beginning to worry about silent degradation, quiet coupling across organizations, vendor concentration, emergent failure modes at scale.

The processes and language we have inherited are well-formed for the first problem and weak for the second.

* * *

### Non-adversarial robustness as security: a simple frame

A lot of recent AI work uses the phrase non-adversarial robustness to talk about systems that handle ‘normal’ stresses well: distribution shift, noisy inputs, messy data, fluctuating workloads, partial outages, misconfigurations. There is no attacker, only an environment and other non-adversarial actors doing what they do.

It is tempting to file that under reliability or safety and hand it off to another team. But if we take the food and energy traditions seriously, there is a strong case for treating non-adversarial robustness as part of security in the AI and agentic era.

One way to see this is to draw a simple two-by-two grid. Along one axis, distinguish adversarial versus non-adversarial sources of stress. Along the other, distinguish acute events from chronic conditions:

[![](https://substackcdn.com/image/fetch/$s_!BbKY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F066a853a-4f96-4c40-af9f-ef94d8990e39_1272x306.png)](https://substackcdn.com/image/fetch/$s_!BbKY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F066a853a-4f96-4c40-af9f-ef94d8990e39_1272x306.png)

Nuclear security lives in the top left; nuclear safety in the bottom left. Food and energy security mostly occupy the bottom row. AI security work today is overwhelmingly concentrated in the top left, with some spillover into the top right as we think about threat persistence.

The entire bottom row is where non-adversarial robustness lives.

- The bottom-left cell (accidents, outages, sudden load, mis-specification) is the world of acute shocks. Systems are pushed off their training distribution in a single step: a spike in traffic, a new file type, a surprise configuration change, an unexpected combination of tools in an agent’s plan. Non-adversarial robustness here is about short, sharp stress: can the system behave tolerably, or at least fail safely, when reality shifts in unexpected ways?

- The bottom-right cell (structural dependency, drift, quiet erosion of performance and posture) is the world of chronic stress. Systems are not jolted; they are slowly bent. The input distribution shifts as users adopt new habits. Fine-tuning and product changes nudge behaviour. Entire organizations wrap brittle services in layers of workflow until they become critical, without ever having tested those services under the conditions they now face. Non-adversarial robustness here is about slow movement: can the system remain usable and governable as the world slides away from the assumptions underlying initial testing?


Both are parts of the same problem: performance and control under non-adversarial change. The acute versus chronic distinction matters because our testing methods often over-index on the former and ignore the latter.

This is also where the commonality between adversarial and non-adversarial testing becomes useful. At their core, both adversarial red teaming and non-adversarial exploratory testing share a spirit: you deliberately look for trouble by pushing the system away from the centre of the distribution it was designed and evaluated for.

- In adversarial testing, you do not care whether the inputs are plausible for ‘normal’ users. Any prompt, sequence, or tool call is acceptable if it exposes a path an attacker could realistically take.

- In non-adversarial testing, you care a lot about plausibility. The question is not whether any possible input can break a system, but instead what plausible input from a non-adversarial but creative, honest, clumsy, non-average user or admin or integration or changing environment could cause failure.


Manual exploratory testers in both worlds share a mindset: curiosity, suspicion, edge cases. Automated approaches diverge more sharply. In adversarial automation, you can let search procedures roam far off-distribution, because any successful attack, no matter how odd, is evidence of a possible open door. In automated non-adversarial exploratory testing, a central difficulty is modelling the space of out-of-distribution inputs that are still plausible. If we let our input generators wander too far, we learn something mathematically true but operationally meaningless; if we constrain them too tightly, we miss important and meaningful failure modes.

Seen from this angle, it is strange that these two families of practice are often split across different parts of an organization. Build teams do happy-path and near-happy-path reliability testing. Security teams do adversarial stress testing. Non-adversarial robustness across the full bottom row, both acute and chronic, is **nobody’s core mandate**.

That gap matters in the agentic era. On-distribution testing is already a poor guide to how safe and secure a system will be once deployed. As agents start to re-plan, discover tools, chain services, and adapt to incentives, the future input distribution will be both more complex and less predictable than whatever we held out in validation sets. If nobody is tasked with exploring that space systematically, we will be surprised for the wrong kinds of reasons.

* * *

### Growing a more comprehensive AI security posture

What would it mean to take this broader concept seriously in an enterprise? It does not mean abandoning adversary models or diluting the focus of security teams. It means adding a second, equally disciplined view: security as continuity under structural uncertainty, operationalized through non-adversarial robustness.

A few practical shifts follow:

1. **Treat concentration and coupling as first-class security concerns**


Food and energy work have long wrestled with the problem of over-concentration: dependence on a single export route, a narrow set of suppliers, a single type of fuel or technology. They respond with diversification strategies, stockpiling, and stress-testing.

In AI, we should be doing the same:

- Map where different business units are using the same models, providers, or agent frameworks, intentionally or not.

- Identify choke points where a single upstream change (a model update, a policy shift from a vendor, a region-wide outage) could ripple across many workflows.

- Include those structural dependencies in security and risk registers alongside classic vulnerability lists.


No attacker needs to be involved for this to matter. But once these dependencies exist, attackers can exploit them.

2. **Bring adversarial and non-adversarial exploratory testing together**


If adversarial and non-adversarial stress testing share so much spirit and technique, it is worth asking whether they should be fragments of separate teams.

One option is to grow something like a ‘mission security’ function whose remit is to discover how AI-enabled workflows and agents break under stress, regardless of whether the stress is malicious, accidental, or environmental.

Such a team would:

- Run classic red-teaming campaigns against systems and agents, probing for prompt injection, data exfiltration, escalation and abuse;

- Design and run non-adversarial exploratory exercises that push systems into plausible yet untested regimes: unusual but honest prompts, new file types, surprising tool sequences, realistic spikes and outages;

- Invest in tooling that can automate both styles of search, with different generators and acceptance criteria for adversarial and non-adversarial exploration; and

- Feed their findings into both security controls and product design, so that fixes are not just brittle patches but structural improvements.


The organizational point is not that everyone should report to the Security org. It is that adversarial thinking and non-adversarial robustness testing are close enough cousins that they benefit from shared methods, shared infrastructure, and shared processes.

3. **Align security, functional reliability, and safety around mission security.**


In nuclear governance, safety and security are formally distinct, but there is growing recognition that accidents and attacks can exploit the same cracks. Reviews increasingly look across both.

In AI enterprises, the relevant triad is slightly different: security, functional reliability, and safety.

- Security concerns itself with adversarial misuse and abuse.

- Functional reliability concerns itself with whether systems do the job they were bought or built to do, under load and under change.

- Safety, where it is discussed at all, concerns itself with harmful impacts on people or institutions.


When an AI system goes off distribution and fails in an important way, all three can be implicated. An outage in an agentic triage system can be a reliability incident, a security incident (if the cause is a prompt-injection campaign), and a safety incident (if patients are harmed), often all at once.

A mission-security view suggests:

- Designing incident taxonomies so that OOD-driven functional failures are visible alongside traditional security incidents, not swept into generic bugs;

- Running joint post-incident reviews where reliability, security, and safety teams look together at both adversarial and non-adversarial contributors; and

- Giving non-adversarial robustness failures the same level of seriousness, in reporting and follow-up, as adversarial findings, because their impact on the organization’s ability to function can be just as severe.


* * *

### Towards a working definition for the agentic era

Putting these pieces together, we get a more comprehensive working notion of AI security for enterprises. Something like:

> **AI security is the protection of an organization’s critical functions from both adversarial and non-adversarial threats arising from its use of AI systems and their dependencies over time.**

The adversary-centric lineage (from nuclear security and cybersecurity) keeps us honest about attackers. The condition-centric lineage (from food and energy security) keeps us honest about the brittleness of the systems we are building and the ways they can fail even when nobody is trying to break them. Non-adversarial robustness sits at the intersection of those two. It is the part of security that cares about how well systems live in the real world, not just how well they fend off deliberate assault.

We are still at the early stages of figuring out what good looks like here. But we do not have to start from nothing. Other fields have been treating security as continuity under stress for decades. We can borrow their instincts about concentration and resilience, and their comfort with uncertainty, then translate them into the structures and habits of AI-first organizations.

If we do, AI security can grow into something closer to mission security for the agentic era: a way of seeing that keeps attackers in view, but that also keeps dependencies and blind spots on our radar.

* * *

#### Subscribe to Jason Stanley

Launched a month ago

Writings on technology

Subscribe

By subscribing, I agree to Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

1

Share

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

TopLatestDiscussions

[Internal Representations as a Governance Surface for AI](https://jasonstanley.substack.com/p/internal-representations-as-a-governance)

[Logit Steering, Sparse Autoencoders, and the Future of Enterprise AI Control](https://jasonstanley.substack.com/p/internal-representations-as-a-governance)

Nov 28•[Jason Stanley](https://substack.com/@jasonstanley)

3

![](https://substackcdn.com/image/fetch/$s_!_kGt!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8892d2e2-986d-4a27-aedb-e61f81891f9e_894x524.jpeg)

[Incident Agents, Pattern Cards, and the Broken Flow from AI Failures to Defenses](https://jasonstanley.substack.com/p/incident-agents-pattern-cards-and)

[Building a flow from AI incidents to pattern cards to test harnesses, so defences evolve with how agents actually fail](https://jasonstanley.substack.com/p/incident-agents-pattern-cards-and)

Dec 5•[Jason Stanley](https://substack.com/@jasonstanley)

2

![](https://substackcdn.com/image/fetch/$s_!q5Ir!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7acedbcb-1d14-4acf-82bf-3fbf84188c96_2560x2564.jpeg)

[Beyond Permissions: Least Agency as Architecture for Agentic Systems](https://jasonstanley.substack.com/p/beyond-permissions-least-agency-as)

[Designing Tool-Using Agents Whose Autonomy Can Expand and Contract Safely](https://jasonstanley.substack.com/p/beyond-permissions-least-agency-as)

Dec 12•[Jason Stanley](https://substack.com/@jasonstanley)

3

1

![](https://substackcdn.com/image/fetch/$s_!HPAz!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2c36876-df81-41cb-903e-30ed65ed41a4_567x421.jpeg)

See all

### Ready for more?

Subscribe
