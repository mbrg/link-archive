---
date: 2022-09-02
description: Recent research highlights a security vulnerability in Microsoft’s Power
  Automate tool that can be exploited to execute ransomware attacks on connected systems.
  By leveraging the legitimate functionality of Power Automate, attackers can hijack
  the automation process to deploy malware once a compromised user account is configured
  with administrative rights. This RPA (Robotic Process Automation) abuse exemplifies
  the risks inherent in low-code/no-code platforms and poses detection challenges
  as these actions are indistinguishable from regular operations. Organizations must
  enhance monitoring and implement stringent access controls to mitigate this risk.
link: https://www.wired.com/story/windows-11-power-automate-attack/
tags:
- cybersecurity
- ransomware
- low-code/no-code
- Microsoft
- Power Automate
title: A Windows 11 Automation Tool Can Easily Be Hijacked ◆ WIRED
---

[Skip to main content](https://www.wired.com/story/windows-11-power-automate-attack/#main-content)

Save StorySave this story

Save StorySave this story

All products featured on WIRED are independently selected by our editors. However, we may receive compensation from retailers and/or from purchases of products through these links.

Automating mundane work tasks has become easier over the past few years. Using drag-and-drop automation software, you can track your working hours in a spreadsheet or automatically create a to-do list item when someone mentions you in an email. The tools can make your life easier, but they carry risks.

One security researcher has found a way to hijack Microsoft’s software automation tool to send ransomware to connected machines and steal data from devices. The attack uses the automation tool as it was designed, but instead of sending legitimate actions, it can be used to deploy malware, says Michael Bargury, the cofounder and CTO of security firm [Zenity](https://techcrunch.com/2021/11/23/zenity-raises-5m-to-help-secure-low-code-no-code-applications/), which is behind the work.

### Daily Newsletter

Our biggest stories, handpicked for you each day.

Sign up

By signing up, you agree to our [user agreement](https://www.condenast.com/user-agreement) (including [class action waiver and arbitration provisions](https://www.condenast.com/user-agreement#introduction-arbitration-notice)), and acknowledge our [privacy policy](https://www.condenast.com/privacy-policy).

“My research showed that you can very easily, as an attacker, take advantage of all of this infrastructure to do exactly what it is supposed to do,” Bargury says. “You \[then\] use it to run your own payloads instead of the enterprise payloads.” The researcher documented his work at the [DefCon hacker conference](https://info.defcon.org/events/48560/) last month and has since released the code.

The attack is based on Microsoft’s Power Automate, an automation tool that was built into [Windows 11](https://www.wired.com/story/most-important-things-microsoft-announcement-windows-11-android-apps/). Power Automate uses a form of robotic process automation, also known as RPA, in which a computer mimics a human’s actions to complete tasks. If you want to get a notification each time an RSS feed is updated, you can build a custom RPA process to make that happen. Thousands of these automations exist, and Microsoft’s software can link up Outlook, [Teams](https://www.wired.co.uk/article/microsoft-teams-meeting-data-privacy), Dropbox, and other apps.

The software is part of a broader [low-code/no-code movement](https://hbr.org/2021/06/when-low-code-no-code-development-works-and-when-it-doesnt) that aims to create tools people can use to create things without having any coding knowledge. “Every business user now has the power that the developer used to have,” Bargury says. His company exists to help secure low-code/no-code apps.

Bargury’s research starts from a position in which a hacker has already gained access to someone’s computer—whether through phishing or an insider threat. (While computers within businesses are frequently insecure—from a lack of patching and updates, for example—starting at this point means an attacker would have already gotten into a corporate network.)

Most Popular

- [![Automakers Are Canceling Plans for New EVs. Here’s a List of What’s Been Killed So Far](https://media.wired.com/photos/687ad90c1d005c057f7adc6e/1:1/w_350%2Ch_350%2Cc_limit/undefined)](https://www.wired.com/story/list-of-new-evs-canceled-by-automakers/#intcid=_wired-right-rail_c31dc4ef-90ff-426b-bbf0-e3f67b271582_popular4-2)







Gear News and Events



[Automakers Are Canceling Plans for New EVs. Here’s a List of What’s Been Killed So Far](https://www.wired.com/story/list-of-new-evs-canceled-by-automakers/#intcid=_wired-right-rail_c31dc4ef-90ff-426b-bbf0-e3f67b271582_popular4-2)







By Aarian Marshall

- [![The Enshittification of American Power](https://media.wired.com/photos/68753a215fc1ea74f2b1b7c9/1:1/w_350%2Ch_350%2Cc_limit/undefined)](https://www.wired.com/story/enshittification-of-american-power/#intcid=_wired-right-rail_c31dc4ef-90ff-426b-bbf0-e3f67b271582_popular4-2)







The Big Story



[The Enshittification of American Power](https://www.wired.com/story/enshittification-of-american-power/#intcid=_wired-right-rail_c31dc4ef-90ff-426b-bbf0-e3f67b271582_popular4-2)







By Abraham L. Newman

- [![Former Top Google Researchers Have Made a New Kind of AI Agent](https://media.wired.com/photos/6876dbb724b5ad5a43b039f5/1:1/w_350%2Ch_350%2Cc_limit/undefined)](https://www.wired.com/story/former-top-google-researchers-have-made-a-new-kind-of-ai-agent/#intcid=_wired-right-rail_c31dc4ef-90ff-426b-bbf0-e3f67b271582_popular4-2)







Artificial Intelligence



[Former Top Google Researchers Have Made a New Kind of AI Agent](https://www.wired.com/story/former-top-google-researchers-have-made-a-new-kind-of-ai-agent/#intcid=_wired-right-rail_c31dc4ef-90ff-426b-bbf0-e3f67b271582_popular4-2)







By Will Knight

- [![The FBI's Jeffrey Epstein Prison Video Had Nearly 3 Minutes Cut Out](https://media.wired.com/photos/68765d94d3c30d0c5e882e66/1:1/w_350%2Ch_350%2Cc_limit/undefined)](https://www.wired.com/story/the-fbis-jeffrey-epstein-prison-video-had-nearly-3-minutes-cut-out/#intcid=_wired-right-rail_c31dc4ef-90ff-426b-bbf0-e3f67b271582_popular4-2)







Security



[The FBI's Jeffrey Epstein Prison Video Had Nearly 3 Minutes Cut Out](https://www.wired.com/story/the-fbis-jeffrey-epstein-prison-video-had-nearly-3-minutes-cut-out/#intcid=_wired-right-rail_c31dc4ef-90ff-426b-bbf0-e3f67b271582_popular4-2)







By Dhruv Mehrotra


Once an attacker has access to a computer, they need to take a few additional steps to abuse the RPA setup, but these are relatively simple. “There’s not a lot of hacking here,” says Bargury, who dubbed the whole process [Power Pwn and is documenting it on GitHub](https://github.com/mbrg/power-pwn).

First, an attacker needs to set up a Microsoft [cloud account](https://github.com/mbrg/power-pwn/blob/main/docs/cloud_setup.md), known as a tenant, and set it to have admin controls over any machines that are assigned to it. This essentially allows the malicious account to run RPA processes on an end user’s device. On the previously compromised machine, all a hack has to do now is assign it to the new admin account—this is done using a simple command line, called [silent registration](https://docs.microsoft.com/en-us/power-automate/desktop-flows/machines-silent-registration#silently-register-a-new-machine).

“Once you do that, you will get a URL that would allow you, as an attacker, to send payloads to the machine,” Bargury says. Ahead of his DefCon talk, he created multiple demos showing how it is possible to use Power Automate to [push out ransomware](https://www.youtube.com/watch?v=YDull-krSJI) to impacted machines. Other demos show how an attacker can steal [authentication tokens](https://www.youtube.com/watch?v=lY_RzV-4BdI) [from a machine](https://www.youtube.com/watch?v=zlF7np18oGI). “You can exfiltrate data outside of the corporate networks through this trusted tunnel, you can build keyloggers, you can take information from the clipboard, you can control the browser,” Bargury says.

A spokesperson for Microsoft downplayed the potential of the attack, pointing out that an account would need to have been accessed by an attacker before it could be used. “There is no mechanism by which a fully updated machine with antivirus protections can be remotely compromised using this technique,” the spokesperson says. “This technique relies on a hypothetical scenario where a system is already compromised or susceptible to a compromise using existing techniques like social engineering—both for the initial and any subsequent network attack,” the spokesperson adds, recommending that people [keep their systems up to date](https://www.wired.com/story/apple-fixed-a-serious-ios-security-flaw-have-you-updated-yet/).

This type of attack could be hard to detect, as it uses official systems and processes throughout, Bargury says. “When you think about the architecture, this is a remote code execution tool that is built by Microsoft and signed by Microsoft all throughout the way,” Bargury says. He published demos and the steps needed to conduct the attack to help raise awareness of the potential issues companies face.

Before his DefCon talk, Microsoft’s team reached out to him, Bargury says, and pointed out that business network admins can restrict access to Power Automate tools by “ [adding a registry entry](https://docs.microsoft.com/en-us/power-platform-release-plan/2020wave2/power-automate/power-automate-desktop-governance)” to their devices. This process would put controls on the account types that can sign in to Power Automate, thus reducing the potential for the system to be abused. However, to be successful, Bargury says, the move relies upon security teams having consistent and clear policies across their organizations, which isn’t always the case.

While the popularity of RPA tools is increasing, there have already been real-world attacks designed to abuse the platforms. In early 2020, Microsoft’s security team [found six hacker groups](https://techmonitor.ai/technology/software/microsofts-detection-and-response-team), including a Chinese APT, inside the network of one company. One of the hacker groups used [automated systems to remove data](https://www.zenity.io/blog/hackers-abuse-low-code-platforms-and-turn-them-against-their-owners/). “In an uncommon move, the attacker used the customer’s existing systems, including eDiscovery, the Compliance Search feature, and Microsoft Flow, to automate stealing its search results,” Microsoft wrote in an [incident report](https://usermanual.wiki/m/79aa76d230d5aafddf3c6758f0256d310aa500a83de56c8671e3721108ed059c_doc).

As the possible risks around low-code/no-code applications [become more obvious](https://securityintelligence.com/articles/low-code-easy-secure/), Bargury says companies may need to reassess their policies. “It’s very important to monitor what RPA agents are doing,” he says. “You cannot really expect to provide all of the business users in an enterprise capabilities that were, up until a few months ago, reserved only to developers and expect everything to go well.”

## You Might Also Like …

- **In your inbox:** Our [biggest stories](https://www.wired.com/newsletter/daily?sourceCode=BottomStories), handpicked for you each day

- [The AI backlash keeps growing stronger](https://www.wired.com/story/generative-ai-backlash/)

- **Big Story:** [Cloning came to polo](https://www.wired.com/story/cloning-came-to-polo-things-got-uncivilized-cambiaso/). Then things got truly uncivilized

- This is [DOGE 2.0](https://www.wired.com/story/next-stage-doge-elon-musk/)

- **Uncanny Valley:** An insider look at [the influence of Silicon Valley](https://swap.fm/l/wired-uv-recirculationunits?sourceCode=BottomStories)


[![](https://media.wired.com/photos/65e713244d9f150f523145c2/1:1/w_270%2Cc_limit/undefined)](https://www.wired.com/author/matt-burgess/)

[Matt Burgess](https://www.wired.com/author/matt-burgess/) is a senior writer at WIRED focused on information security, privacy, and data regulation in Europe. He graduated from the University of Sheffield with a degree in journalism and now lives in London. Send tips to Matt\_Burgess@wired.com. ... [Read More](https://www.wired.com/author/matt-burgess)

Senior writer

- [X](https://www.twitter.com/mattburgess1)

Topics [cybersecurity](https://www.wired.com/tag/cybersecurity/) [security](https://www.wired.com/tag/security/) [hacking](https://www.wired.com/tag/hacking/) [Microsoft](https://www.wired.com/tag/microsoft/)

### The Daily newsletter

Our biggest stories, handpicked for you each day.

Sign up

By signing up, you agree to our [user agreement](https://www.condenast.com/user-agreement) (including [class action waiver and arbitration provisions](https://www.condenast.com/user-agreement#introduction-arbitration-notice)), and acknowledge our [privacy policy](https://www.condenast.com/privacy-policy).

[Hackers Are Finding New Ways to Hide Malware in DNS Records](https://www.wired.com/story/dns-records-hidden-malicious-code/#intcid=_wired-article-bottom-recirc_4cf0a2bd-d1ad-4971-b0ba-c6cc27e67192_roberta-similarity1_fallback_text2vec1)

Newly published research shows that the domain name system—a fundamental part of the web—can be exploited to hide malicious code and prompt injection attacks against chatbots.

Dan Goodin, Ars Technica

[AI Agents Are Getting Better at Writing Code—and Hacking It as Well](https://www.wired.com/story/ai-agents-are-getting-better-at-writing-code-and-hacking-it-as-well/#intcid=_wired-article-bottom-recirc_4cf0a2bd-d1ad-4971-b0ba-c6cc27e67192_roberta-similarity1_fallback_text2vec1)

One of the best bug-hunters in the world is an AI tool called Xbow, just one of many signs of the coming age of cybersecurity automation.

Will Knight

[McDonald’s AI Hiring Bot Exposed Millions of Applicants' Data to Hackers Using the Password ‘123456’](https://www.wired.com/story/mcdonalds-ai-hiring-chat-bot-paradoxai/#intcid=_wired-article-bottom-recirc_4cf0a2bd-d1ad-4971-b0ba-c6cc27e67192_roberta-similarity1_fallback_text2vec1)

Basic security flaws left the personal info of tens of millions of McDonald’s job-seekers vulnerable on the “McHire” site built by AI software firm Paradox.ai.

Andy Greenberg

[OpenAI’s New ChatGPT Agent Tries to Do It All](https://www.wired.com/story/openai-chatgpt-agent-launch/#intcid=_wired-article-bottom-recirc_4cf0a2bd-d1ad-4971-b0ba-c6cc27e67192_roberta-similarity1_fallback_text2vec1)

It’s a PowerPoint generator! It’s a date-night planner! It’s … another agent from OpenAI.

Reece Rogers

[A Group of Young Cybercriminals Poses the ‘Most Imminent Threat’ of Cyberattacks Right Now](https://www.wired.com/story/scattered-spider-most-imminent-threat/#intcid=_wired-article-bottom-recirc_4cf0a2bd-d1ad-4971-b0ba-c6cc27e67192_roberta-similarity1_fallback_text2vec1)

The Scattered Spider hacking group has caused chaos among retailers, insurers, and airlines in recent months. Researchers warn that its flexible structure poses challenges for defense.

Matt Burgess

[Former Top Google Researchers Have Made a New Kind of AI Agent](https://www.wired.com/story/former-top-google-researchers-have-made-a-new-kind-of-ai-agent/#intcid=_wired-article-bottom-recirc_4cf0a2bd-d1ad-4971-b0ba-c6cc27e67192_roberta-similarity1_fallback_text2vec1)

The mission? Teaching models to better understand how to build code will lead to superintelligent AI.

Will Knight

[How to Delete All of Your Social Media Accounts](https://www.wired.com/story/how-to-delete-your-facebook-instagram-twitter-snapchat/#intcid=_wired-article-bottom-recirc_4cf0a2bd-d1ad-4971-b0ba-c6cc27e67192_roberta-similarity1_fallback_text2vec1)

Breaking up is hard to do—harder yet when there’s a deactivation period. Here’s how to log off every big social site, including Facebook, Instagram, TikTok, X, Threads, Bluesky, and Truth Social.

Boone Ashworth

[Get the macOS Finder to Do Just About Anything by Typing Natural Language Commands](https://www.wired.com/story/substage-macos-finder-natural-language-commands/#intcid=_wired-article-bottom-recirc_4cf0a2bd-d1ad-4971-b0ba-c6cc27e67192_roberta-similarity1_fallback_text2vec1)

With the app Substage, users can type out file management tasks in plain English, then use the commands it generates to convert file types, manage folders, create zip files, and more.

Justin Pot

[Cloudflare Is Blocking AI Crawlers by Default](https://www.wired.com/story/cloudflare-blocks-ai-crawlers-default/#intcid=_wired-article-bottom-recirc_4cf0a2bd-d1ad-4971-b0ba-c6cc27e67192_roberta-similarity1_fallback_text2vec1)

The age of the AI scraping free-for-all may be coming to an end. At least if Cloudflare gets its way.

Kate Knibbs

[Android May Soon Warn You About Fake Cell Towers](https://www.wired.com/story/android-may-soon-warn-you-about-fake-cell-towers/#intcid=_wired-article-bottom-recirc_4cf0a2bd-d1ad-4971-b0ba-c6cc27e67192_roberta-similarity1_fallback_text2vec1)

Plus: Iran-linked hackers threaten to release Trump campaign emails, Chinese hackers still in US telecoms networks, and an abusive deepfake website plans an expansion.

Matt Burgess

[ICE Rolls Facial Recognition Tools Out to Officers' Phones](https://www.wired.com/story/ice-rolls-facial-recognition-tools-out-to-officers-phones/#intcid=_wired-article-bottom-recirc_4cf0a2bd-d1ad-4971-b0ba-c6cc27e67192_roberta-similarity1_fallback_text2vec1)

Plus: US feds charge alleged masterminds behind infamous forum, Scattered Spider targets airlines, and hackers open a valve at a Norwegian dam.

Dell Cameron

[OpenAI’s Unreleased AGI Paper Could Complicate Microsoft Negotiations](https://www.wired.com/story/openai-five-levels-agi-paper-microsoft-negotiations/#intcid=_wired-article-bottom-recirc_4cf0a2bd-d1ad-4971-b0ba-c6cc27e67192_roberta-similarity1_fallback_text2vec1)

The partnership between OpenAI and Microsoft in many ways hinges on the definition of artificial general intelligence, creating a tension that has spilled over into OpenAI research that has not been made public.

Kylie Robison

[![Wired logo](https://media.wired.com/photos/6335c338010e2be68af5d43a/master/w_125,h_50,c_limit/logo-wired.png?format=original)**One year for ~~$2.50~~ $1 per month**\\
![Wired robot](https://media.wired.com/photos/6335b35fac1e13577068c0c1/master/w_369,h_244,c_limit/robot-footer.png?format=original)\\
Subscribe](https://www.wired.com/v2/offers/wira01018?source=Site_0_JNY_WIR_DESKTOP_FOOTER_0_US_CREATIVE_BACK_TEST_ZZ_PANELA&redirectURL=https%3A%2F%2Fwww.wired.com%2Fstory%2Fwindows-11-power-automate-attack%2F)
