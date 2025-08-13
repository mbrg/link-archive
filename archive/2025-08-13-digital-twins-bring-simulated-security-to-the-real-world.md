---
date: '2025-08-13'
description: The integration of digital twins in cybersecurity represents a significant
  advancement by creating simulated environments that incorporate real-time operational
  data. This technology enables organizations to model software updates and assess
  their impacts without disrupting production systems, streamlining security decision-making.
  Digital twins facilitate AI-driven analysis to triage security alerts and contextualize
  potential threats, thus enhancing threat detection accuracy. By providing a near-real-time
  simulation framework, organizations can proactively identify and mitigate vulnerabilities,
  establishing a robust cybersecurity posture. This approach aligns with the growing
  trend of leveraging AI to optimize security operations across enterprise environments.
link: https://www.darkreading.com/endpoint-security/digital-twins-bring-simulated-security-real-world
tags:
- Application Security
- Simulation Technology
- Digital Twins
- Cybersecurity
- AI in Security
title: Digital Twins Bring Simulated Security to the Real World
---

- [Endpoint Security](https://www.darkreading.com/endpoint-security)
- [Application Security](https://www.darkreading.com/application-security)
- [Cybersecurity Analytics](https://www.darkreading.com/cybersecurity-analytics)
- [ICS/OT Security](https://www.darkreading.com/ics-ot-security)

[![DR Technology Logo](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt4c091cd3ac9935ea/653a71456ad0f6040a6f71bd/Dark_Reading_Logo_Technology_0.png?width=1280&auto=webp&quality=80&disable=upscale)\\
\\
News, news analysis, and commentary on the latest trends in cybersecurity technology.](https://www.darkreading.com/program/dr-technology)

# 'Digital Twins' Bring Simulated Security to the Real World

By simulating business environments or running software while incorporating real-time data from production systems, companies can model the impact of software updates, exploits, or disruptions.

[![Picture of Robert Lemos, Contributing Writer](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt28d2c260c33375ea/64f14ff471df6264a382aaa0/Robert-Lemos.png?width=100&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/author/robert-lemos)

[Robert Lemos, Contributing Writer](https://www.darkreading.com/author/robert-lemos)

April 24, 2025

4 Min Read

![digital twins with human, robot hands touching](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt1acc930cb26e92e3/680ab0f295c12a06ef9cf474/digital-twin-hands-Ole_CNX-shutterstock.jpg?width=1280&auto=webp&quality=80&format=jpg&disable=upscale)

Source: Ole.CNX via Shutterstock

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/endpoint-security/digital-twins-bring-simulated-security-real-world)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/endpoint-security/digital-twins-bring-simulated-security-real-world)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/endpoint-security/digital-twins-bring-simulated-security-real-world)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/endpoint-security/digital-twins-bring-simulated-security-real-world&title=%27Digital%20Twins%27%20Bring%20Simulated%20Security%20to%20the%20Real%20World)[Email](mailto:?subject=%27Digital%20Twins%27%20Bring%20Simulated%20Security%20to%20the%20Real%20World&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20%27Digital%20Twins%27%20Bring%20Simulated%20Security%20to%20the%20Real%20World%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fendpoint-security%2Fdigital-twins-bring-simulated-security-real-world)

The next time your company faces a cyberattack, it may be limited to a virtual world, if digital twins — a technology hybrid that pairs simulation with real-world data — takes off.

Researchers and analysts at security operations platform provider Trellix, for example, use information culled from Microsoft Active Directory, an e-policy orchestration platform, and the network connections linking the systems to create a digital model of a customer's enterprise environment. Artificial intelligence (AI) agents can then use the digital twin to triage security alerts, model what users may have been doing, and gauge the impact of allowing a particular action.

The agents collect data from each relevant source to establish the context surrounding the alert, says Martin Holste, chief technology officer for cloud and AI at Trellix.

"Put together, this means that we can paint a picture of what it would look like if an attacker were in an environment, what paths there are for attackers to get into an environment, determine if those match up, and investigate evidence to determine if that has occurred," he says. "The advantages for customers are the ability to think in systems and understand not just what is happening but why it is happening."

Digital twins are not a new concept. First used [by NASA in the 1960s to simulate space-based systems in orbit](https://blogs.sw.siemens.com/simcenter/apollo-13-the-first-digital-twin/), the idea to simulate processes or systems and incorporate real-time, real-world data gained traction in [manufacturing and design prototyping](https://www.mckinsey.com/capabilities/operations/our-insights/digital-twins-the-next-frontier-of-factory-optimization) in the 1990s and early 2000s. Now researchers and technologists are looking at applying the concept to software and hardware systems to [analyze the impact of cyberattacks and software defects](https://www.darkreading.com/cyber-risk/unlocking-the-cybersecurity-benefits-of-digital-twins).

Related: [Researchers Warn of 'Hidden Risks' in Passwordless Account Recovery](https://www.darkreading.com/endpoint-security/researchers-warn-hidden-risks-passwordless-account-recovery)

Research at the University of Michigan, funded by the National Institute of Standards and Technology (NIST), for example, created a digital twin of a 3D printer and designed software to demonstrate the usefulness of such a simulation for manufacturing cybersecurity.

# Loading...

"Because manufacturing processes produce such rich data sets — temperature, voltage, current — and they are so repetitive, there are opportunities to detect anomalies that stick out, including cyberattacks," said Dawn Tilbury, a professor of mechanical engineering at the University of Michigan, in [a NIST report on the technology](https://www.nist.gov/news-events/news/2023/02/how-digital-twins-could-protect-manufacturers-cyberattacks).

## Twinning Is Not Instrumenting

In many ways, digital twins resemble runtime instrumentation techniques typical of technologies such as runtime application self-protection (RASP) or interactive application security testing (IAST) — except that those systems typically instrument production or staged software.

Related: [SentinelOne Acquires AI Startup Prompt Security](https://www.darkreading.com/endpoint-security/sentinelone-acquires-ai-startup-prompt-security)

While such runtime techniques are very accurate, they require deploying agents into production environments, while more traditional static techniques are less optimal, says Yossi Pik, co-founder and CTO of application security startup Backslash Security, which uses digital twins to analyze application security. The company uses a simulated system to test a variety of software processes — such as user actions, code updates, or attacker's exploits — and determines whether they pose real-world threats.

"Static reachability analysis of code is less intrusive, but when done using traditional scanners, it is not very efficient and also lacks context," he says. "The digital twin approach provides a happy middle ground, providing near-runtime-level precision but without intruding on production environments."

One place where digital twins can shine for cybersecurity is in simulating the impact of an update. Without changing the installed code in production, an application security team can apply an update to the digital twin and determine whether the updated software "resolves a vulnerability, introduces new ones, or breaks existing functionality," says Pik.

Related: [Certified Randomness Uses Quantum Cryptography to Make Stronger Keys](https://www.darkreading.com/endpoint-security/certified-randomnes-squantum-cryptography-stronger-keys)

"It makes the upgrade decision process faster and safer, enabling proactive remediation planning without developer bottlenecks," he says.

## Enabling More Agentic AI

Backslash focuses on creating an application graph, which models how the data flows, how the components interact, and the possible security risks that could be exploited. Feeding the model into a large language model (LLM) enables AI analysis of the application as well, allowing the system to use the application graph for context, reducing the chance of hallucinations.

"The digital twin becomes the grounding mechanism that makes LLMs useful and trustworthy for security teams," Pik says. "It transforms generic language models into focused AppSec copilots, capable of helping teams understand, prioritize, and fix issues with unprecedented precision and clarity.

Similarly, Trellix sees digital twins as being a critical milestone in the path to systems that can be analyzed — and secured — by AI agents. Running the agents inside a digital twin allows the automated programs to test potential scenarios without impacting production systems.

"Generative AI is extremely good at understanding systems and environments, and so the overall benefits of digital twins will increase geometrically going forward," Trellix's Holste says. "It is effective at tying high-level, human concepts with low-level machine codes."

In the NIST-funded research, the team at the University of Michigan created a cybersercurity framework that could analyze the data in the context of the digital twin of the 3D printer and determine whether an anomaly was a innocuous event or a malicious attack.

Read more about:

[CISO Corner](https://www.darkreading.com/keyword/ciso-corner)

[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https://www.darkreading.com/endpoint-security/digital-twins-bring-simulated-security-real-world)[Facebook](http://www.facebook.com/sharer/sharer.php?u=https://www.darkreading.com/endpoint-security/digital-twins-bring-simulated-security-real-world)[Twitter](http://www.twitter.com/intent/tweet?url=https://www.darkreading.com/endpoint-security/digital-twins-bring-simulated-security-real-world)[Reddit](https://www.reddit.com/submit?url=https://www.darkreading.com/endpoint-security/digital-twins-bring-simulated-security-real-world&title=%27Digital%20Twins%27%20Bring%20Simulated%20Security%20to%20the%20Real%20World)[Email](mailto:?subject=%27Digital%20Twins%27%20Bring%20Simulated%20Security%20to%20the%20Real%20World&body=I%20thought%20the%20following%20from%20Dark%20Reading%20might%20interest%20you.%0D%0A%0D%0A%20%27Digital%20Twins%27%20Bring%20Simulated%20Security%20to%20the%20Real%20World%0D%0Ahttps%3A%2F%2Fwww.darkreading.com%2Fendpoint-security%2Fdigital-twins-bring-simulated-security-real-world)

## About the Author

[![Robert Lemos, Contributing Writer](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/blt28d2c260c33375ea/64f14ff471df6264a382aaa0/Robert-Lemos.png?width=400&auto=webp&quality=80&disable=upscale)](https://www.darkreading.com/author/robert-lemos)

[Robert Lemos, Contributing Writer](https://www.darkreading.com/author/robert-lemos)

Veteran technology journalist of more than 20 years. Former research engineer. Written for more than two dozen publications, including CNET News.com, Dark Reading, MIT's Technology Review, Popular Science, and Wired News. Five awards for journalism, including Best Deadline Journalism (Online) in 2003 for coverage of the Blaster worm. Crunches numbers on various trends using Python and R. Recent reports include analyses of the shortage in cybersecurity workers and annual vulnerability trends.

[See more from Robert Lemos, Contributing Writer](https://www.darkreading.com/author/robert-lemos)

Keep up with the latest cybersecurity threats, newly discovered vulnerabilities, data breach information, and emerging trends. Delivered daily or weekly right to your email inbox.

[Subscribe](https://dr-resources.darkreading.com/c/pubRD.mpl?secure=1&sr=pp&_t=pp:&qf=w_defa3135&ch=drwebbutton)

More Insights

Webinars

- [Creating a Roadmap for More Effective Security Partnerships](https://dr-resources.darkreading.com/c/pubRD.mpl?secure=1&sr=pp&_t=pp:&qf=w_defa8838&ch=SBX&cid=_upcoming_webinars_8.500001578&_mc=_upcoming_webinars_8.500001578) Aug 14, 2025

[More Webinars](https://www.darkreading.com/resources?types=Webinar)

Events

- [\[Virtual Event\] Strategic Security for the Modern Enterprise](https://ve.informaengage.com/virtual-events/strategic-security-for-the-modern-enterprise/?ch=sbx&cid=_session_16.500334&_mc=_session_16.500334) Jun 26, 2025
- [\[Virtual Event\] Anatomy of a Data Breach](https://ve.informaengage.com/virtual-events/an-anatomy-of-a-data-breach-and-what-to-do-if-it-happens-to-you/?ch=sbx&cid=_session_16.500333&_mc=_session_16.500333) Jun 18, 2025

[More Events](https://www.darkreading.com/events)

You May Also Like

* * *

[Endpoint Security\\
\\
HP Brings Quantum-Safe Encryption to Printers](https://www.darkreading.com/endpoint-security/hp-brings-quantum-safe-encryption-printers)

[Endpoint Security\\
\\
Mobile Jailbreaks Exponentially Increase Corporate Risk](https://www.darkreading.com/endpoint-security/mobile-jailbreaks-corporate-risk)

[Endpoint Security\\
\\
Cybercrime Gangs Abscond With 1000s of AWS Credentials](https://www.darkreading.com/endpoint-security/cybercrime-gangs-steal-thousands-aws-credentials)

[Endpoint Security\\
\\
NIST Releases 3 Post-Quantum Standards, Urges Orgs to Start PQC Journey](https://www.darkreading.com/endpoint-security/nist-releases-3-post-quantum-standards-urges-orgs-to-start-pqc-journey)

FEATURED

![Black-hat-2025.png](https://eu-images.contentstack.com/v3/assets/blt6d90778a997de1cd/bltbbf5bcde654cb046/6890b075b473132a9a9f6ee2/Black-hat-2025.png?width=1280&auto=webp&quality=80&disable=upscale)

Check out the [Black Hat USA Conference Guide](https://www.techtarget.com/searchsecurity/conference/Guide-to-the-latest-Black-Hat-Conference-news) for more coverage and intel from — and about — the show.

Latest Articles in DR Technology

- [Researchers Warn of 'Hidden Risks' in Passwordless Account Recovery](https://www.darkreading.com/endpoint-security/researchers-warn-hidden-risks-passwordless-account-recovery) Aug 11, 2025
\|

3 Min Read

- [Prime Security Wins Black Hat's Startup Spotlight Competition](https://www.darkreading.com/cyber-risk/prime-security-black-hat-spotlight-competition) Aug 7, 2025
\|

4 Min Read

- [Startup Spotlight: Twine Security Tackles the Execution Gap](https://www.darkreading.com/cybersecurity-operations/startup-spotlight-twine-security-closes-execution-gap) Aug 6, 2025
\|

3 Min Read

- [SentinelOne Acquires AI Startup Prompt Security](https://www.darkreading.com/endpoint-security/sentinelone-acquires-ai-startup-prompt-security) Aug 6, 2025
\|

2 Min Read


[Read More DR Technology](https://www.darkreading.com/program/dr-technology)
