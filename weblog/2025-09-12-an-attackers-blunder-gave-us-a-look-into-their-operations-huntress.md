---
date: '2025-09-15'
description: In a rare incident, Huntress gained unprecedented insight into threat
  actor operations when an attacker mistakenly installed their EDR agent while evaluating
  security products. The attackers' browsing history revealed their use of AI tools
  for operational efficiency, searches for phishing methods, and attempts to exploit
  frameworks like Evilginx. Analysts identified compromised identities linked to the
  attacker, showcasing the threat actor's detailed reconnaissance and research strategies.
  This exposure provides invaluable data on threat methodologies, reinforcing the
  need for enhanced endpoint detection capabilities. The encounter underscores the
  evolving tactics of cybercriminals leveraging legitimate tools for malicious intents.
link: /archive/2025-09-12-an-attackers-blunder-gave-us-a-look-into-their-operations-huntress
tags:
- Cybersecurity
- Malware Analysis
- Endpoint Detection and Response
- Insider Threats
- Threat Intelligence
- weblog
title: "An Attacker\u2019s Blunder Gave Us a Look Into Their Operations \u25C6 Huntress"
type: weblog
---

It's crazy what you can learn from reading someone's browser history. Imagine how deep inside someone's mind you can get by reading their ChatGPT history..

---

> As you can see in the graphic below, our SOC analysts uninstalled the agent 84 minutes after it had been installed on the host. This was after they had examined malicious indicators, which included the machine name, original malware, and the machine attempting to compromise victim accounts. At that point, the analysts investigated further to determine the original intent of the user, including whether they were looking for a way to abuse our product. Following their investigation, all of the indicators, combined with the fact that this machine had been involved in past compromises, led the analysts to determine that the user was malicious and ultimately uninstall the agent.

This is very interesting from the perspective of a customer. Should my vendors be allowed to remove defenses? I vote yes in this case.

---

> For transparency’s sake, this is not accurate. We circled back with the SOC after the writing of this blog to verify the exact nature of the agent uninstallation, and they verified they had forcibly uninstalled it when they had sufficient evidence to determine the endpoint was being used by a threat actor.

Good on them for correcting this.

---

> What you're about to read is something that all endpoint detection and response (EDR) companies perform as a byproduct of investigating threats. Because these services are designed to monitor for and detect threats, EDR systems by nature need the capability to monitor system activity, as is outlined in our [product documentation](https://support.huntress.io/hc/en-us/articles/35179490601491-Huntress-Data-Collection-and-Incident-Response), [Privacy Policy](https://www.huntress.com/privacy-policy), and [Terms of Service](https://support.huntress.io/hc/en-us/articles/14692045459731-Huntress-Platform-Terms-of-Service).

Looks like they got some heat for silent detections.

---

> At this point, we determined that the host that had installed the Huntress agent was, in fact, malicious. We wanted to serve the broader community by sharing what we learned about the tradecraft that the threat actor was using in this incident. In deciding what information to publish about this investigation, we carefully considered several factors, like strictly upholding our privacy obligations, as well as disseminating EDR telemetry that specifically reflected threats and behavior that could help defenders.

Are people advocating for privacy of malware devs? Dropping silent detection to catch exploit development is fair game IMO. That's also why opsec is important for people doing legitimate offensive work.

---

> The attacker tripped across our ad while researching another security solution. We confirmed this is how they found us by examining their Google Chrome browser history. An example of how this may have appeared to them in the moment may be seen in Figure 1.

Hacking the hackers

---

> We knew this was an adversary, rather than a legitimate user, based on several telling clues. The standout red flag was that the unique machine name used by the individual was the same as one that we had tracked in several incidents prior to them installing the agent. Further investigation revealed other clues, such as the threat actor’s browser history, which appeared to show them trying to actively target organizations, craft phishing messages, find and access running instances of Evilginx, and more. We also have our suspicions that the operating machine where Huntress was installed is being used as a jump box by multiple threat actors—but we don’t have solid evidence to draw firm conclusions at this time.

Machine name as the sole indicator to start hacking back doesn't seem strong enough IMO. Is this machine name a guid?

---

> Overall, over the course of three months we saw an evolution in terms of how the threat actor refined their processes, incorporated AI into their workflows, and targeted different organizations and vertical markets, as outlined in Figure 5 below.

Search history gives out A LOT

---

> The Chrome browser history also revealed visits by the threat actor to multiple residential proxy webpages, including LunaProxy and Nstbrowser (which bills itself as an anti-detect browser and supports the use of residential proxies). The threat actor visited the pricing plan page for LunaProxy, researched specific products, and looked up quick start guides throughout May, June, and July. Residential proxy services have become increasingly popular with threat actors as a way to route their traffic through residential IP addresses, allowing them to obscure malicious activity, like avoiding suspicious login alerts while using compromised credentials.

It's crazy that you can just buy these services

