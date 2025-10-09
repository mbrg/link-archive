---
date: '2025-10-09'
description: Autonomous AI agents are reshaping the cybersecurity landscape by automating
  the attack chain, enabling rapid vulnerability discovery and exploitation. Recent
  incidents highlight AI's capability for real-time reconnaissance, data theft, and
  malware development. This evolution favors cybercriminals, significantly disrupting
  traditional defenses. The emergence of AI-enhanced vulnerability research may foster
  new disciplines like "VulnOps," leading to continuous vulnerability identification
  and patching. However, this also raises ethical and operational challenges, as organizations
  may pursue independent patching without vendor oversight. The dynamic between AI-driven
  offense and defense is at a critical tipping point, necessitating urgent adaptation
  in cybersecurity strategies.
link: https://www.csoonline.com/article/4069075/autonomous-ai-hacking-and-the-future-of-cybersecurity.html
tags:
- Cyberattack Automation
- Autonomous Hacking
- Vulnerability Detection
- AI Cybersecurity
- Cyber Defense
title: Autonomous AI hacking and the future of cybersecurity ◆ CSO Online
---

by Heather Adkins, Gadi Evron and Bruce Schneier

# Autonomous AI hacking and the future of cybersecurity

Opinion

Oct 8, 20256 mins

[Artificial Intelligence](https://www.csoonline.com/artificial-intelligence/)CyberattacksSecurity Practices

## AI agents are automating key parts of the attack chain, threatening to tip the scales completely in favor of cyber attackers unless new models of AI-assisted cyberdefense arise.

![Shiny robot hand over a keyboard. Generative AI. Chatbot.](https://www.csoonline.com/wp-content/uploads/2025/10/4069075-0-59226700-1759906904-shutterstock_1402318157.jpg?quality=50&strip=all&w=1024)

Credit: kung\_tom / Shutterstock

AI agents are now hacking computers. They’re getting better at all phases of cyberattacks, faster than most of us expected. They can chain together different aspects of a cyber operation, and hack autonomously, at computer speeds and scale. This is going to change everything.

Over the summer, hackers proved the concept, industry institutionalized it, and criminals operationalized it. In June, AI company XBOW took the [top spot](https://www.techrepublic.com/article/news-ai-xbow-tops-hackerone-us-leaderboad) on HackerOne’s US leaderboard after submitting over 1,000 new vulnerabilities in just a few months. In August, the seven teams competing in DARPA’s AI Cyber Challenge [collectively found](https://www.darpa.mil/news/2025/aixcc-results) 54 new vulnerabilities in a target system, in four hours (of compute). Also in August, Google [announced](https://techcrunch.com/2025/08/04/google-says-its-ai-based-bug-hunter-found-20-security-vulnerabilities/) that its Big Sleep AI found dozens of new vulnerabilities in open-source projects.

It gets worse. In July Ukraine’s CERT [discovered](https://www.csoonline.com/article/4025139/novel-malware-from-russias-apt28-prompts-llms-to-create-malicious-windows-commands.html) a piece of Russian malware that used an LLM to automate the cyberattack process, generating both system reconnaissance and data theft commands in real-time. In August, Anthropic reported that they disrupted a threat actor that used Claude, Anthropic’s AI model, to [automate](https://www.anthropic.com/news/detecting-countering-misuse-aug-2025) the entire cyberattack process. It was an impressive use of the AI, which performed network reconnaissance, penetrated networks, and harvested victims’ credentials. The AI was able to figure out which data to steal, how much money to extort out of the victims, and how to best write extortion emails.

Another hacker used Claude to create and market his own ransomware, complete with “advanced evasion capabilities, encryption, and anti-recovery mechanisms.” And in September, Checkpoint [reported](https://blog.checkpoint.com/executive-insights/hexstrike-ai-when-llms-meet-zero-day-exploitation/) on hackers using HexStrike-AI to create autonomous agents that can scan, exploit, and persist inside target networks. Also in September, a research team [showed](https://arxiv.org/abs/2509.01835) how they can quickly and easily reproduce hundreds of vulnerabilities from public information. These tools are increasingly free for anyone to use. [Villager](https://www.infosecurity-magazine.com/news/chinese-ai-villager-pen-testing/), a recently released AI pentesting tool from Chinese company Cyberspike, uses the Deepseek model to completely automate attack chains.

This is all well beyond AIs capabilities in 2016, at DARPA’s [Cyber Grand Challenge](https://www.darpa.mil/news/2016/cyber-grand-challenge-winners). The annual Chinese AI hacking challenge, [Robot Hacking Games](https://www.schneier.com/essays/archives/2022/01/robot-hacking-games.html), might be on this level, but little is known outside of China.

## Tipping point on the horizon

AI agents now rival and sometimes surpass even elite human hackers in sophistication. They automate operations at machine speed and global scale. The scope of their capabilities allows these AI agents to completely automate a criminal’s command to maximize profit, or structure advanced attacks to a government’s precise specifications, such as to avoid detection.

[In this future](https://www.washingtonpost.com/technology/2025/09/20/ai-hacking-cybersecurity-cyberthreats/?pwapi_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyZWFzb24iOiJnaWZ0IiwibmJmIjoxNzU4MzQwODAwLCJpc3MiOiJzdWJzY3JpcHRpb25zIiwiZXhwIjoxNzU5NzIzMTk5LCJpYXQiOjE3NTgzNDA4MDAsImp0aSI6IjEzZGE1Njk0LTMxOTItNDdkNi1hNTU3LTRkOWEzNDI5ODM0OCIsInVybCI6Imh0dHBzOi8vd3d3Lndhc2hpbmd0b25wb3N0LmNvbS90ZWNobm9sb2d5LzIwMjUvMDkvMjAvYWktaGFja2luZy1jeWJlcnNlY3VyaXR5LWN5YmVydGhyZWF0cy8ifQ.N_h4ygZ86XPjbtpR253UIbbArH7e0Tu3tN0iapl5v2k), attack capabilities could accelerate beyond our individual and collective capability to handle. We have long taken it for granted that we have time to patch systems after vulnerabilities become known, or that withholding vulnerability details prevents attackers from exploiting them. This is [no longer](https://www.cybersecuritydive.com/news/ai-vulnerability-detection-patching-threats-mandiant-summit/760746/) the case.

The cyberattack/cyberdefense balance has long skewed towards the attackers; these developments threaten to [tip the scales](https://www.schneier.com/essays/archives/2018/03/artificial_intellige.html) completely. We’re [potentially](https://www.wired.com/story/the-era-of-ai-generated-ransomware-has-arrived/) [looking](https://www.computerworld.com/article/4048415/the-ai-powered-cyberattack-era-is-here.html) at a singularity event for cyber attackers. Key parts of the attack chain are becoming automated and integrated: persistence, obfuscation, command-and-control, and endpoint evasion. Vulnerability research could potentially be carried out during operations instead of months in advance.

The most skilled will likely retain an edge for now. But AI agents don’t have to be better at a human task in order to be useful. They just have to excel in one of [four dimensions](https://theconversation.com/will-ai-take-your-job-the-answer-could-hinge-on-the-4-ss-of-the-technologys-advantages-over-humans-258469): speed, scale, scope, or sophistication. But there is every indication that they will eventually excel at all four. By reducing the skill, cost, and time required to find and exploit flaws, AI can turn rare expertise into commodity capabilities and gives average criminals an outsized advantage.

## The AI-assisted evolution of cyberdefense

AI technologies can benefit defenders as well. We don’t know how the different technologies of cyber-offense and cyber-defense will be amenable to AI enhancement, but we can extrapolate a possible series of overlapping developments.

**Phrase One: The Transformation of the Vulnerability Researcher.** AI-based hacking benefits defenders as well as attackers. In this scenario, AI empowers defenders to do more. It simplifies capabilities, providing [far more people the ability](https://www.csoonline.com/article/3632268/gen-ai-is-transforming-the-cyber-threat-landscape-by-democratizing-vulnerability-hunting.html) to perform previously complex tasks, and empowers researchers previously busy with these tasks to accelerate or move beyond them, freeing time to work on problems that require human creativity. History suggests a pattern. Reverse engineering was a laborious manual process until tools such as IDA Pro made the capability available to many. AI vulnerability discovery could follow a similar trajectory, evolving through scriptable interfaces, automated workflows, and automated research before reaching broad accessibility.

**Phase Two: The Emergence of VulnOps.** Between research breakthroughs and enterprise adoption, a new discipline might emerge: VulnOps. Large research teams are already building operational pipelines around their tooling. Their evolution could mirror how DevOps professionalized software delivery. In this scenario, specialized research tools become developer products. These products may emerge as a SaaS platform, or some internal operational framework, or something entirely different. Think of it as AI-assisted vulnerability research available to everyone, at scale, repeatable, and integrated into enterprise operations.

**Phase Three: The Disruption of the Enterprise Software Model.** If enterprises adopt AI-powered security the way they adopted continuous integration/continuous delivery (CI/CD), several paths open up. AI vulnerability discovery could become a built-in stage in delivery pipelines. We can [envision a world](https://www.schneier.com/blog/archives/2024/11/ais-discovering-vulnerabilities.html) where AI vulnerability discovery becomes an integral part of the software development process, where vulnerabilities are automatically patched even before reaching production — a shift we might call continuous discovery/continuous repair (CD/CR). Third-party risk management (TPRM) offers a natural adoption route, lower-risk vendor testing, integration into procurement and certification gates, and a proving ground before wider rollout.

**Phase Four: The Self-Healing Network.** If organizations can independently discover and patch vulnerabilities in running software, they will not have to wait for vendors to issue fixes. Building in-house research teams is costly, but AI agents could perform such discovery and generate patches for many kinds of code, including third-party and vendor products. Organizations may develop independent capabilities that create and deploy third-party patches on vendor timelines, extending the current trend of independent open-source patching. This would increase security, but having customers patch software without vendor approval raises questions about patch correctness, compatibility, liability, right-to-repair, and long-term vendor relationships.

These are all speculations. Maybe AI-enhanced cyberattacks won’t evolve the ways we fear. Maybe AI-enhanced cyberdefense will give us capabilities we can’t yet anticipate. What will surprise us most might not be the paths we can see, but the ones we can’t imagine yet.

SUBSCRIBE TO OUR NEWSLETTER

### From our editors straight to your inbox

Get started by entering your email address below.

Please enter a valid email address

Subscribe

by **Heather Adkins**

1. [Follow Heather Adkins on LinkedIn](https://www.linkedin.com/in/argvee/)

[Heather Adkins](https://www.linkedin.com/in/argvee/) is [vice president of security engineering at Google](https://blog.google/authors/heather-adkins/) and head of Google’s Office of Cybersecurity Resilience. She is a founding member of the Google Security Team and a cybersecurity expert focused on breach recovery, incident response, insider risks, and building modern safe computing environments.

by **Gadi Evron**

1. [Follow Gadi Evron on LinkedIn](https://www.linkedin.com/in/gadievron/?originalSubdomain=il)

[Gadi Evron](https://www.linkedin.com/in/gadievron/?originalSubdomain=il) is the [founder and CEO of Knostic](https://www.knostic.ai/blog/author/gadi-evron), an AI security market leader, and chairs the CSides cross-CISO communities conference. Previously, he founded (as CEO) Cymmetria (acquired), was CISO of the Israeli National Digital Authority, founded the Israeli CERT, and headed PwC's Cyber Security Center of Excellence. Gadi has written two books on cybersecurity, is a frequent contributor to industry publications, and a speaker at industry events.

by **Bruce Schneier**

Bruce Schneier is a fellow and lecturer at the Harvard Kennedy School, currently visiting the Munk School at the University of Toronto. He can be found at [www.schneier.com](https://www.schneier.com/).

## Show me more

PopularArticlesPodcastsVideos

[news\\
\\
**ClayRat spyware turns phones into distribution hubs via SMS and Telegram** \\
\\
By Shweta Sharma\\
\\
Oct 9, 20254 mins\\
\\
PhishingSecurity\\
\\
![Image](https://www.csoonline.com/wp-content/uploads/2025/10/4070281-0-22237000-1760014951-cso_nw_mobile_phone_text_bubble_skull_crossbones_sms_phishing_smishing_by_jane_kelly_gettyimages-669307004_abstract_data_by_spainter_vfx_gettyimages-897166754-100810151-orig.jpg?quality=50&strip=all&w=375)](https://www.csoonline.com/article/4070281/clayrat-spyware-turns-phones-into-distribution-hubs-via-sms-and-telegram.html)

[news\\
\\
**Homeland Security’s reassignment of CISA staff leaves US networks exposed** \\
\\
By Nidhi Singal\\
\\
Oct 9, 20254 mins\\
\\
Government ITSecurity\\
\\
![Image](https://www.csoonline.com/wp-content/uploads/2025/10/4070270-0-48300000-1760011733-shutterstock_2498849189.jpg?quality=50&strip=all&w=444)](https://www.csoonline.com/article/4070270/homeland-securitys-reassignment-of-cisa-staff-leaves-us-networks-exposed.html)

[opinion\\
\\
**Your cyber risk problem isn’t tech — it’s architecture** \\
\\
By Rangel Rodrigues\\
\\
Oct 9, 20258 mins\\
\\
Data and Information SecurityIT Governance FrameworksRisk Management\\
\\
![Image](https://www.csoonline.com/wp-content/uploads/2025/10/4069616-0-12276100-1760007770-GettyImages-965259458-1.jpg?quality=50&strip=all&w=339)](https://www.csoonline.com/article/4069616/your-cyber-risk-problem-isnt-tech-its-architecture.html)

[podcast\\
\\
**CSO Executive Sessions: Leading the Charge on Cyber Agility for Southeast Asia’s Digital Future** \\
\\
By Estelle Quek\\
\\
Oct 2, 202521 mins\\
\\
Cloud SecurityCyberattacksThreat and Vulnerability Management\\
\\
![Image](https://www.csoonline.com/wp-content/uploads/2025/10/0-74324900-1759391598-youtube-thumbnail-WESAq1DjvNA.jpg?quality=50&strip=all&w=444)](https://www.csoonline.com/podcast/4066207/cso-executive-sessions-leading-the-charge-on-cyber-agility-for-southeast-asias-digital-future.html)

[podcast\\
\\
**CSO Executive Session ASEAN: Navigating the Cyber Battleground, Strengthening Southeast Asia’s Digital Defense** \\
\\
By Estelle Quek\\
\\
Sep 23, 202541 mins\\
\\
CyberattacksCybercrimeThreat and Vulnerability Management\\
\\
![Image](https://www.csoonline.com/wp-content/uploads/2025/09/0-68505800-1758669158-CSO-MICHAEL-THUMB-16x9-1.jpg?quality=50&strip=all&w=444)](https://www.csoonline.com/podcast/4061453/cso-executive-session-asean-navigating-the-cyber-battleground-strengthening-southeast-asias-digital-defense.html)

[podcast\\
\\
**CSO Executive Session ASEAN: Navigating sophisticated cyberthreats in Southeast Asia region** \\
\\
By Estelle Quek\\
\\
Sep 16, 202548 mins\\
\\
CybercrimeRansomware\\
\\
![Image](https://www.csoonline.com/wp-content/uploads/2025/09/0-58136900-1758013323-CSO-RUBRIK-THUMB-16x9-2.jpg?quality=50&strip=all&w=444)](https://www.csoonline.com/podcast/4056987/cso-executive-session-asean-navigating-sophisticated-cyberthreats-in-southeast-asia-region.html)

[video\\
\\
**CSO Executive Sessions: Leading the Charge on Cyber Agility for Southeast Asia’s Digital Future** \\
\\
By Estelle Quek\\
\\
Oct 2, 202521 mins\\
\\
Cloud SecurityCyberattacksThreat and Vulnerability Management\\
\\
![Image](https://www.csoonline.com/wp-content/uploads/2025/10/4066221-0-22659500-1759456860-youtube-thumbnail-WESAq1DjvNA.jpg?quality=50&strip=all&w=444)](https://www.csoonline.com/video/4066221/cso-executive-sessions-leading-the-charge-on-cyber-agility-for-southeast-asias-digital-future.html)

[video\\
\\
**CSO Executive Session ASEAN: Navigating the Cyber Battleground, Strengthening Southeast Asia’s Digital Defense** \\
\\
By Estelle Quek\\
\\
Sep 23, 202541 mins\\
\\
CyberattacksThreat and Vulnerability ManagementZero Trust\\
\\
![Image](https://www.csoonline.com/wp-content/uploads/2025/09/4061443-0-75999600-1758638406-youtube-thumbnail-Toe-9mMvgfs.jpg?quality=50&strip=all&w=444)](https://www.csoonline.com/video/4061443/cso-executive-session-asean-navigating-the-cyber-battleground-strengthening-southeast-asias-digital-defenses.html)

[video\\
\\
**CSO Executive Session ASEAN: Navigating sophisticated cyberthreats in the Southeast Asia region** \\
\\
By Estelle Quek\\
\\
Sep 15, 202548 mins\\
\\
CybercrimeRansomware\\
\\
![Image](https://www.csoonline.com/wp-content/uploads/2025/09/4055424-0-70322500-1758013581-youtube-thumbnail-muebw3DbdaI.jpg?quality=50&strip=all&w=444)](https://www.csoonline.com/video/4055424/cso-executive-session-asean-navigating-sophisticated-cyberthreats-in-the-southeast-asia-region.html)

Sponsored Links

- [Secure AI by Design: Unleash the power of AI and keep applications, usage and data secure.](http://pubads.g.doubleclick.net/gampad/clk?id=6856108221&iu=/8456/IDG.G_B2B_CSOOnline.com)
- [Solve your most complex IT challenges with solutions that simplify your modernization journey.](http://pubads.g.doubleclick.net/gampad/clk?id=7038222634&iu=/8456/IDG.G_B2B_CIO.com)
