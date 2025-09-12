---
date: '2025-09-12'
description: In a rare incident, Huntress gained unprecedented insight into threat
  actor operations when an attacker mistakenly installed their EDR agent while evaluating
  security products. The attackers' browsing history revealed their use of AI tools
  for operational efficiency, searches for phishing methods, and attempts to exploit
  frameworks like Evilginx. Analysts identified compromised identities linked to the
  attacker, showcasing the threat actor's detailed reconnaissance and research strategies.
  This exposure provides invaluable data on threat methodologies, reinforcing the
  need for enhanced endpoint detection capabilities. The encounter underscores the
  evolving tactics of cybercriminals leveraging legitimate tools for malicious intents.
link: https://www.huntress.com/blog/rare-look-inside-attacker-operation
tags:
- Cybersecurity
- Malware Analysis
- Endpoint Detection and Response
- Insider Threats
- Threat Intelligence
title: An Attacker’s Blunder Gave Us a Look Into Their Operations ◆ Huntress
---

![](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2F6a889f843f1c43a695dc53a813b091e2)![](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2F494235849aa5452690cabfa164b509ff)

![](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2F9f33356fc04f46a2ac4a68753ba41658)

[Home](https://www.huntress.com/)![](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2F779e332a141048329fb98c924119138a) [Blog](https://www.huntress.com/blog) ![](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2F779e332a141048329fb98c924119138a)

How an Attacker’s Blunder Gave Us a Rare Look Inside Their Day-to-Day Operations

Published:

[September 9, 2025](https://www.huntress.com/)

# How an Attacker’s Blunder Gave Us a Rare Look Inside Their Day-to-Day Operations

By:

[![](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2Ff466d74a8f3b4603b6f5a9662a0612c0)\\
Jamie Levy](https://www.huntress.com/authors/jamie-levy)

[![](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2F037877a541484d86ac239373c502608a)\\
Lindsey O'Donnell-Welch](https://www.huntress.com/authors/lindsey-odonnell-welch)

[![](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2F7dd9df5e1b134c5aad1971e3a7aa0247)\\
Michael Tigges](https://www.huntress.com/authors/michael-tigges)

![](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2F4f81d51c40d244c8b3b5cc5b61561b5b)

![Share icon](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2Fe499a4a7ecac4052ab9e5c194b638f16)

![Glitch effect](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2Fc2118b00ed614bbf83f96f25de0beaf8)![Glitch effect](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2Fc2118b00ed614bbf83f96f25de0beaf8)![Glitch effect](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2F0658aac7c84b4f7e9a7c7b2a5b519b28)

Table of Contents

![Down arrow](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2F537a8aa5b2cc4f17ad5139d981b8866f)

**Update Sept. 11 @ 9am ET**

We appreciate the comments, questions, and discussions from the community around this blog post. In light of those questions, we wanted to release more detailed information to offer further insights into the timeframe that had initially been highlighted in this post, and walk through how we specifically investigated this incident.

As you can see in the graphic below, our SOC analysts uninstalled the agent 84 minutes after it had been installed on the host. This was after they had examined malicious indicators, which included the machine name, original malware, and the machine attempting to compromise victim accounts. At that point, the analysts investigated further to determine the original intent of the user, including whether they were looking for a way to abuse our product. Following their investigation, all of the indicators, combined with the fact that this machine had been involved in past compromises, led the analysts to determine that the user was malicious and ultimately uninstall the agent.

![](https://cdn.builder.io/api/v1/image/assets%2FYJIGb4i01jvw0SRdL5Bt%2F72c80f114dc149019051b6852a9e3b7a)

**NOTE:** A previous version of this post suggested that the threat actor had uninstalled the agent:

_"This is where our EDR data drops off, as they may have become aware of us and uninstalled the agent."_

For transparency’s sake, this is not accurate. We circled back with the SOC after the writing of this blog to verify the exact nature of the agent uninstallation, and they verified they had forcibly uninstalled it when they had sufficient evidence to determine the endpoint was being used by a threat actor.

We look forward to continuing the conversation around this investigation, around what managed endpoint detection and response (EDR) products are and what purpose that they serve, and more. We recently detailed some of these discussions in our Tradecraft Tuesday this week, below.

EDR, Ethics, and a Hacker Mistake \| Tradecraft Tuesday - YouTube

[Photo image of Huntress](https://www.youtube.com/channel/UCykrmYP5ANJFWGWJckUJlAA?embeds_referring_euri=https%3A%2F%2Fwww.huntress.com%2F)

Huntress

7.54K subscribers

[EDR, Ethics, and a Hacker Mistake \| Tradecraft Tuesday](https://www.youtube.com/watch?v=TDghdvAuO90)

Huntress

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

More videos

## More videos

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=TDghdvAuO90&embeds_referring_euri=https%3A%2F%2Fwww.huntress.com%2F)

0:00

0:00 / 4:49
•Live

•

\-\-\----------------------

**Update Sept. 9 @ 3pm ET**

What you're about to read is something that all endpoint detection and response (EDR) companies perform as a byproduct of investigating threats. Because these services are designed to monitor for and detect threats, EDR systems by nature need the capability to monitor system activity, as is outlined in our [product documentation](https://support.huntress.io/hc/en-us/articles/35179490601491-Huntress-Data-Collection-and-Incident-Response), [Privacy Policy](https://www.huntress.com/privacy-policy), and [Terms of Service](https://support.huntress.io/hc/en-us/articles/14692045459731-Huntress-Platform-Terms-of-Service).

On the heels of questions around how and why Huntress released this information, we wanted to clarify several important aspects of our investigation. We have an obligation to 1) research and respond to security threats and investigate malware and 2) educate the broader community about those threats. These dual objectives played into our decision to develop and publish this blog post.

When we first came across the host mentioned in this blog, it was because we were first responding to numerous alerts that were related to malware executing on it. Part of this process involves our SOC team closely investigating signals and collecting artifacts related to EDR telemetry on the host. It was only upon further investigation into this telemetry that we observed signals indicating malicious behavior. By this point, we also found that the unique machine name used by the individual was the same as one that we had tracked in several incidents prior to them installing the agent.

At this point, we determined that the host that had installed the Huntress agent was, in fact, malicious. We wanted to serve the broader community by sharing what we learned about the tradecraft that the threat actor was using in this incident. In deciding what information to publish about this investigation, we carefully considered several factors, like strictly upholding our privacy obligations, as well as disseminating EDR telemetry that specifically reflected threats and behavior that could help defenders.

Overall, this investigation is a result of what we strive to do best: transparency, education, and wrecking hackers. Read on to learn more.

\-\-\----------------------

## Summary

Here at Huntress, we love exposing adversary tradecraft, and we also love when threat actors make blunders. So imagine our delight when a threat actor installed Huntress onto their operating machine—after finding us via one of our advertising campaigns and starting a trial— giving us a sprawling inside look at how they’re using AI to build workflows, searching for tools like Evilginx, and more.

\-\-\----------------------

We all know that security products are often downloaded by attackers for “evaluation,” but often we can only guess as to how they decided to target a particular technology, or the actions taken while trying out such software. We recently had the pleasure of getting a front seat view into what one attacker did, simply because they installed our agent and let us collect information directly from them. Here, we will cover this strange tale.

## How did we get here?

Like most good stories, this one starts in the middle and works its way back and forth. Let’s start with how this person of interest got our attention. One of the tricks of the trade to get people interested in your products is through advertising. As such, we run ads to help lead potential customers to our products. An adverse effect here might be garnering some “unwanted” attention as well. Such is the setting for the beginning of this adventure: it all started with a nicely placed Google ad.

The attacker tripped across our ad while researching another security solution. We confirmed this is how they found us by examining their Google Chrome browser history. An example of how this may have appeared to them in the moment may be seen in Figure 1.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeJUVtwy7xflclvgUeBGQfKElGqL2tDQbXGU__smHcQsDJvHgD5E2eZRuOmqeV-NsvVb-JB152RhoN3lL-lTVNJYV5oNlEBuvSu83HIBy9G-Q143xhDbhTB1SpIniI7ZeHY6VxM?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 1: Google search for Bitdefender, leading to a Huntress ad_

It appears that the attacker became interested in Huntress while simultaneously trying out Bitdefender. After hitting our comparison page, they could hardly contain themselves and started a trial immediately. We are able to follow their journey through their Chrome history, as seen in Figure 2 below.

**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdKW29wTam1W7HtnCDFCrX2D6axopp-uc5BAtORJxIoMZ1VcDFBCGvI1SO7704Ba3mJoq4PF1RLoUFFJBb1pS7ftM2yA5U3XzrVVv2XgbjGTn-frP-K-yRmJ-8bkaChOhp-wN1j?key=6dcQwm6GIQlCTfuUoMFMyQ)**_Figure 2: Browser history showing how a search for Bitdefender led to a Huntress trial_

It’s no secret that threat actors may install security products for research purposes or even for legitimate use—and in fact, the adversary was interested in other security products in addition to Bitdefender and Huntress. We found evidence that they had bought a Malwarebytes subscription (including the Malwarebytes browser guard extension).

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe4s839ASjHRduw42AfZDjVCCo9gYEfwo00ZXg-JsrUFJSBECVjEPyafTyhfC4bUPrllQbWx2pCu2lR0QnDZzlASrOwP69P7x6qTJ9g0kDAex4Ax2_K_-K3l5HWiO9PLqSDdn9x?key=6dcQwm6GIQlCTfuUoMFMyQ)

_Figure 3: Attacker tries to stay safe with an installed Malwarebytes browser extension_ 🤣

## Threat actor red flags—and our response

We knew this was an adversary, rather than a legitimate user, based on several telling clues. The standout red flag was that the unique machine name used by the individual was the same as one that we had tracked in several incidents prior to them installing the agent. Further investigation revealed other clues, such as the threat actor’s browser history, which appeared to show them trying to actively target organizations, craft phishing messages, find and access running instances of Evilginx, and more. We also have our suspicions that the operating machine where Huntress was installed is being used as a jump box by multiple threat actors—but we don’t have solid evidence to draw firm conclusions at this time.

Huntress analysts went to work evaluating the outstanding indicators of compromise found on the adversary’s host and how they related to data found within authentications to identities at Huntress. Retroactive hunts disclosed a further 20 identities which were compromised; many of which had been accessed by the adversary prior to Huntress’ deployment against the identity, whose activity was limited to refreshing session tokens to maintain access.

Overall, analysis of the adversary’s primary operating infrastructure, hosted on Autonomous System (AS) “ **12651980 CANADA INC**.” (now known as VIRTUO) disclosed a pattern of access of over **2471** unique identities spanning the last two weeks– many of which were preemptively caught by additional detection capabilities such as malicious mail rule creation, or session token theft.

The intelligence gathered by the above has resulted in detections of high confidence against the adversary’s infrastructure; and equipped our systems and analysts to respond to these incidents in significantly less time and with extreme confidence in malice, eliminating adversarial attempts to evade our detections.

All in all, we were able to see the threat actor’s specific day-to-day activities—from their methodologies to the specific types of organizations (and even individuals) they were interested in. We also saw them begin to tinker with tools and search for tutorials, attempting to learn more. For instance, after installing the Huntress agent, the threat actor took steps to better understand Autoruns.

**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdPydpBlPDUhdpXoIj2Tszjw0b_1JM21SgtUEqdyV18htkfyvOYkTj0v6nBA0FVh6B_SJyPrllalrwV3jNTgd3Ogv3x78Ea8c4f-lS_PEVD1Qk9zY4Btq54gFOkk6TL1qhEDJLY?key=6dcQwm6GIQlCTfuUoMFMyQ)**_Figure 4: The threat actor attempting to better understand Autoruns_

Overall, over the course of three months we saw an evolution in terms of how the threat actor refined their processes, incorporated AI into their workflows, and targeted different organizations and vertical markets, as outlined in Figure 5 below.

![](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2Fb14fa1103c8546dfb955cf719232e46e)_Figure 5: An overview of some of the threat actor’s activities that we saw over the months_

Below are some of the specific methodologies that we saw.

## Attacker methodologies

### Use of AI for operational efficiency

The Chrome browser history gave a first-hand look at how the adversary is using AI tools to increase the operational efficiency of their workflows. While there have previously been many reports on how cybercriminals are using AI (based on indicators in phishing messages or landing page content), this is the first time that we have a close-up view of a threat actor embedding AI into their operations in order to automate—and speed up—their workflow.

On May 25, the threat actor signed up for Make.com, which is legitimate workflow automation software, before researching the platform’s Telegram Bot integration feature as a way to launch automated processes (as seen in Figure 6 below). The threat actor then poked around several FAQ sites to better understand how Telegram Bot APIs work and how to set up webhooks.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdD1sNQy7UFszqPrYnYqsKTxKPPMvBwNblhn-PdLylCfh3H__YPNTevJGgGRY7q6XL9CQODTBmFfx8W7f_baKImgYYblbEBaicYk7md_HbdIH4UnHudnolzjrdW_DRS_X0vyap5?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 6: Signing up for [Make.com](http://make.com/)_

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdbpvPzopYGKOLEFM-0N4KEU-6-6Jh1zPe_ceTeP8hUepyd20WRHhbV0p-svZinlQ3yHCk2QH7vFAX-9t5jrp2SZvMiah6FUH0E9py_uW83HePtdkD_HoGZ2Yd265eEt6anol2ytQ?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 7: Digging deeper into Telegram Bot APIs_

Over time, the threat actor started to get a better grasp of how they could use Make.com for specific workflows, and their browser history shows them starting to rely more heavily on the platform. By the time June 29 rolled around, the threat actor had fully developed their workflow with Make. As seen in Figure 8, the threat actor would first identify the organization of interest (typically after receiving a “tip” from Telegram) before using Google Translate to translate or craft messages related to these organizations. While we don’t have detailed insight into how the threat actor was using Make for these specific workflows, we can see that it was part of the process to automate specific functions.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXej02kvsRwG64U7RWTEGwSP9MetYXVVU_3CvfuEEsTyF1rlhteI-WlH6j70sh9RDGrW1wXuLbruoB_-OEX-bK4tJ8GkAU6bYo3kTJE6cQShzjZSN2Z_QB5RZmlD99KmjBuLh8Cm?key=6dcQwm6GIQlCTfuUoMFMyQ)

_Figure 8: Threat actor starts to rely on automated workflows_

The threat actor also appeared to be interested in other AI tools to help with data generation and writing. We saw multiple Google searches for “free ai no signup” and for “csv generator ai.” We also saw the threat actor using Toolbaz AI, which is a writing assistant; the CSV spreadsheet generator feature of DocsBot AI, which is an AI chatbot tool; and the AI data generator feature of Explo AI, which is an embedded analytics tool.

### Finding running instances of Evilginx

We saw evidence of the threat actor searching for running instances of the Evilginx man-in-the-middle attack framework using Censys, and then attempting to access those instances.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfhpZnkip4Xhwe_x_mbNvnxsQjN-fBnmhC4XMYD_lqlYAnZU1ZEw__A2tMULxs3KIGMZXgfxrpgOjzVos2GpV_jfwjUwmWuEwl_rlRe8SbPm26TmZ5Voqr4ADbhmSeRDFZNdPCbqw?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 9: Using Censys to search for running instances of Evilginx_

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfePd_SqXYWjwhXVGcGUoV2kRIHIAgXk2k7bkY9AoV5D82oJ0XAIDnrrccNFg2z2J5iUT-WcBXYkhec9XGOXcqpF2vp_WtBxNyUAYZvWLHd5alZKghyD2fFYvRJ_Jz3VSD3pbIALQ?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 10: One example of the Evilginx instance that the attacker tried to access_

In addition to Evilginx, we also found evidence of multiple installed tools on the threat actor’s system—or, in some cases, an interest in tools based on the threat actor browser history. These tools included recon and attack tool GraphSpy, open source tool Bloodhound, the TeamFiltration framework used for enumeration and exfiltration, and more.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcdYDNuYg8NB71YQJIam_jqa7HT5WVoCA7XWtc-YtwettO3_t--Z5a7PAjvQtUcPA-YVrnJB2qy0MRi19JTElFhLZf1X5QXcqLfjAMwiDFqT9uW2NnJRrVBZPr-G0aoLk6usRh9?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 11: Various tools that the attacker may have used_

### Interest in residential proxy services

The Chrome browser history also revealed visits by the threat actor to multiple residential proxy webpages, including LunaProxy and Nstbrowser (which bills itself as an anti-detect browser and supports the use of residential proxies). The threat actor visited the pricing plan page for LunaProxy, researched specific products, and looked up quick start guides throughout May, June, and July. Residential proxy services have become increasingly popular with threat actors as a way to route their traffic through residential IP addresses, allowing them to obscure malicious activity, like avoiding suspicious login alerts while using compromised credentials.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd01_NfMWLtwacDez_IZgwu1t-1_i3MNpywbE8BjlZkaY6SMuPaqVdzhbtvs3wlP4J00ZOH02YEJ09aBM07nRb3pCOwEBt2STmiEgQqva-RARySA_R2kh_eL5UM7QJMPe_4rLq4sQ?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 12: A VirusTotal lookup of LunaProxy.exe, which was in the Chrome history_

## Research and recon methods

The Chrome browser history entries also gave us a close view of the attacker’s reconnaissance methods. The threat actor spent a lot of time researching companies across different sectors, from specific banks to “top real estate companies in the US” (also looking up “real estate agents in California”).

The threat actor didn’t just search for individual companies—they also looked at all parts of the ecosystem surrounding organizations of interest, from their customer bases to associated third-party companies across the supply chain. For example, the threat actor appeared to start targeting software companies in early July, searching for these types of companies via Google Search and using database marketing tools like ReadyContacts and InfoClutch to scope out how many customers they had and their market share.

The threat actor also used the BuiltWith platform, which lets users identify and analyze the technology stacks used by websites. On July 8, browser entries show the attacker conducting an extensive level of research on a prominent ecommerce vendor for managing payments and subscriptions, including a list of its customers, contacts, and market share. The threat actor then used BuiltWith to search for the websites relying on that vendor, before navigating to the BuiltWith sign up page, presumably to access that list.

The threat actor conducted a fair amount of research into tools used to scrape Telegram group data, including looking at scraper tools like Apify, the Axiom Chrome extension, and the RapidAPI platform (Figure 13).

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd7IPUx5HRRyuk188k8TDxBwvLdcnS_xQ0efa1HRxh-KT1CAK6cRF0-l-0XO2Bg5T53OmZCbhrOUofNVXxT-GM7a7xX6aCLMLhrwyqN9Crfxkb8FbyVssOeM3OiDcr0XC4xKwUQ0Q?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 13: While researching data scraping tools the threat actor came across RapidAPI_

## Use of Google Translate

The threat actor used Google Translate extensively, and Chrome browser shows them first visiting bank websites, and then using the translation platform, likely to assist in crafting phishing-related messages, as seen in Figure 14.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXes_3NIeO_FSiOzccc9ZhFZC-bU1sKp9D4jkVF1axM-vFs6RZOXPeFGkFtmf35Cd40hlqII4hHoAYd5v_uk6CIaO4ctyXPbgxKE3cpTXl2ZVtvZJLogHPrXzyT0xZzgDw1eK7BJtw?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 14: The threat actor used Google Translate services extensively_

The attacker often used urlscan to get information about various websites. Tips appear to have come in via Telegram using the [getUpdates](https://core.telegram.org/bots/api#getupdates) method.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc8MyiQJuFiNzNS2GykomChaW9BSIVLjXh1lX906j6UceZfeMUjcZOBiWQsecHdvocYPcqQPhO2_SbgjB7okBOPq8ryTD48eyT4JPeXbqAvOUP2nsmrDt01axPxEZ0awbPOFv9f?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 15: Part of the Chrome history around a particular tip_

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdyS8Ck9uN0Pn17PIkzsGtXs6_WxTBRaEReoHD4626fwgmSx8tmd6OO62fCRwweMaRM6Jm5I4diO-rXkZ_mfiIlcku4eDQhmje6NwVCNWSb4yX_lQ0nTS3J5oNVgUksm9LVki3fSA?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 16: Google Translate message_

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfOxiX6IMi8OUyGFrTMxu_itP7TOpuaPQU05iOmUXUDgDIqqQAfWjTncgPRXdXuSjOfZDSbOpcxHn1p7jz2bOAtDikAex6G9NSsBtckOmO0CXpqij0Pi7S-nsfNlo4qhN6_lQvztw?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 17: Google Translate message: username and password_

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdJtx5KpXMINB6Ip2ukq_sqUW94e0gMLePZ5Q2pn4Kk2ma_OyDVwweSJnSS1x7qki6ypEVc12U8LgOV270aga9eaPwJrs6YnUgXgIi3gWyGZ9dp6KnPE0kML8ocZzusNQiS3te9Fw?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 18: Google Translate message: username and password_

There were several entries in the browser history that showed use of Google Translate to translate messages from Portuguese to English alongside browsing banks in Brazil, then evidence of crafting messages later on in their history.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcAC58yDwzifUhFeIRnIt0QYd4u7hILe27vKL82r0b6iXoudGGoiVIuu3MNh_1T5fFZd8szAmKR4VV3S3Pf-rY1illx--DnAZcTJxBaaep6QAhTA4R-mtqHWkuIkllLLFnUTsyFUg?key=6dcQwm6GIQlCTfuUoMFMyQ)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf5Sd2R0BpngqngV52C-XgrtrSuGZvEcq0Du4wCMOsBp5o8H85jZKnHSq5QSp5y_XpXAAEArvcXdp4NTT8pf_knXDWz2Lp-aVS6IAP6ZJzOWCer5W665X_Ikd76DJeptUSG_hHBig?key=6dcQwm6GIQlCTfuUoMFMyQ)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdNiqszsWmFcI3kDZ59ENOESn6iHEVJVeJnsRWicmuBeYLGWEdOprbwBkCQt1XrUM_MzwchwGGYy9TsBEIO1fO6ad4yxVJLr-UtgoqnB1j3ebrG7CH9CIwZp1dRem-T08neFr-sMw?key=6dcQwm6GIQlCTfuUoMFMyQ)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfCQ23qulSPfO9_ZikUujXUyX88Ahon2Dyy-ZsFpbfWBaOZNLoxlmSWIXso8bV9NZrGpGSvs2JV-J8TJIb9i05YBaNpIHh3Ee-VWE57dr-7uF4SERhvBhDVDauq8rA9qiyvN4HvmQ?key=6dcQwm6GIQlCTfuUoMFMyQ)

## Dark web: STYX market

We also saw the threat actor express interest in STYX Market, a [dark web forum](https://socradar.io/dark-web-market-styx-market/) that’s been around since 2023, and was recently called a “rising star for stealer logs, stolen creds, and laundering services” by researchers. After doing some initial research on STYX—as well as other Telegram chat groups and channels—they decided to check out the site for themselves, registering for an account before perusing the catalog of VoIP accounts, stealer logs, SIM cards, and more.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXerL_32riFH92BS7f0cIhvvni7WSWX7H4A9i05nnZXg2Zu1HNcgzNfeRwDXVTcZfVgq459oAey3C0AB39GLxCLRODZ5SvgUOfVqhUtINb0dBxEfqN84YWwvyVZYudfBc4DF7lJFTg?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 19: The threat actor showed an interest in STYX Market_

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc5jTFb1FHwr1loWGnkgh764Gt1XATTqfg1JG9hE4kK9oe3W9rpbDmKA6wz_ZI11qfHuyR41FWdmAgr0KCviyOtAw1CaDVurzO2mLipM40BuMMcWkjKxX9Pz_WQZPMCx6rGLJBH?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 20: A post from SOCRadar on STYX Market caught the threat actor’s attention_

## EDR activities

Rarely do you ever get the chance to actually shoulder surf a real threat actor. We had such an opportunity when they installed our agent. It starts out mundane enough. We don’t know what they must have dreamed about after ending their shift at 2am UTC the previous night, but as mentioned earlier, you can see them start a trial, download the agent, and install it.

**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdKW29wTam1W7HtnCDFCrX2D6axopp-uc5BAtORJxIoMZ1VcDFBCGvI1SO7704Ba3mJoq4PF1RLoUFFJBb1pS7ftM2yA5U3XzrVVv2XgbjGTn-frP-K-yRmJ-8bkaChOhp-wN1j?key=6dcQwm6GIQlCTfuUoMFMyQ)**_Figure 21: At 2am UTC, after about 10 hours of inactivity, the threat actor suddenly showed an interest in Bitdefender, which led them to Huntress_

The most interesting activity for the start of their day on July 9, 2025 was browsing to [urlscan.io](http://urlscan.io/) to inspect login.incipientcroop\[.\]com. Shortly after, they logged into [Make.com](http://make.com/) and began working on a project called Voltage\_Office356bot (notice the typo).

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeilK-_2Kg-DL739jgc2wWflOeE2j2KGQ8EYw6ZXEyYXdl9mhy7BmNl4V-lYC02ECK-KOEvkA2991WbZwaOfn88e39hh7N5Iq7Wzo6lhodnzBAgDCCSaj4pHdoeNPfPGzZLyg2RKA?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 22: Timeline of EDR and browser histories_

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfmxUUaf5Tz2rDzq5jGWZc9G_hYXhicidgbmSnUlWLLXoxsRXKnGQhmg_JTcNnmNkbuNJ-aZ_All9s4mhRGRVbIfhoJYiIVW-OLYOXBZJQF79vJvrnBRNAZnMYs4nckYTGTsUL6?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 23: urlquery info for login.incipientcroop\[.\]com_

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf8O-p7CSNBczOwolBziOdFkYZW1EpVbyXfHhfqrvyIftg3g3UYN54J_ZQDu8i8D0dZr1Qlg-n8ljgk1eWJU98pnwi5ubyV6OMlIIkMpJPUIuxYXD9P036t5IWcRg3Z_Iac4BxF5g?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 24: Further down on the urlquery page for login.incipientcroop\[.\]com, there is evidence of Voltage\_Office356bot_

There is evidence that the threat actor had access to cookie data for two different individuals, and accessed them via Notepad++. They proceeded to open the first file:

C:\\Program Files\\Notepad++\\notepad++.exe C:\\Users\\Administrator\\Downloads\\Telegram

Desktop\\Cookies\_\[victim1\]@\[redacted1\]\[.\].com.json

Then they started looking around to see what they can find, with a Google search for “email osint”.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcZv13LLhV7UYCm8dwFsddLTxhMI71kTckT2o0f2H6HM6Hljz61bq0X1TjXtP-ck2pCwpPDQrLCtBOX5N82TxXGz11k07hbrlVMxFjLUP1tr3Q7WQSMdlaGBUELIVMcs7ZMbzxC?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 25: Looking for “email osint”_

Next, they opened the second cookie file:

C:\\Program Files\\Notepad++\\notepad++.exe C:\\Users\\Administrator\\Downloads\\Telegram

Desktop\\Cookies\_\[victim2\]@\[redacted2\]\[.\].com.json

They then started up Nstbrowser.exe and LunaProxy:

C:\\Program Files\\Nstbrowser\\Nstbrowser.exe

C:\\Program Files (x86)\\LunaProxy\_cata\\socks5\\LunaProxyDivert.exe  SOCK5 \[snip\]

They browsed to an article titled [Say Hello to your new cache flow](https://www.synacktiv.com/en/publications/whfb-and-entra-id-say-hello-to-your-new-cache-flow) by Synacktiv covering WHFB and Entra ID, followed by a Google search for “whfb prt”, which landed them on the website of a well-known researcher, [Dirk-Jan Mollema](https://dirkjanm.io/).

They checked their IP address after this:

C:\\Windows\\system32\\curl.exe ipinfo\[.\]io

And then checked their IP address again:

C:\\Windows\\system32\\curl.exe ipinfo\[.\]io

They then tried to use a tool called [ROADtools Token eXchange (roadtx)](https://github.com/dirkjanm/ROADtools/wiki/ROADtools-Token-eXchange-(roadtx)):

C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\roadtx.exe prtauth -r msgraph -c msteams

And then erroneously tried to run the same tool (as an executable) via Python:

C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python313\\python.exe  C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\roadtx.exe prtauth -r msgraph -c msteams

Then ran it again:

C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\roadtx.exe describe

And then tried to run it again, erroneously, using Python:

C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python313\\python.exe  C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\roadtx.exe describe

They seemed to be having trouble. At this point they browsed to Dirk-jan Mollema’s post on [Phishing for Microsoft Entra primary refresh tokens](https://dirkjanm.io/phishing-for-microsoft-entra-primary-refresh-tokens/).

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeS1UiCr9xEZ7GDvy8iX6fbK3eIhczBmA-Hz8FIcQX2DnECSIW9XvDaq9FWDru2TjcdU-9bwveKKcKxoXpkQMIW4DBlIBKxP3tKhPgCcMrNyopI82Qlt57_3hKLbAn8XWwurRJnzA?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 26: Searching for an answer with keyword whfb prt_

While there, they gained some new inspiration, and discovered a handy little script that could make their life easier:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcwG75RCakB8AMKR0Fc64FgplpkS9PB0Ne2yyvMXzxxLvDU6Yfx5XkqbcWFI18QZqnCt6bxkzoEY07yO6hRkBx5Dx9QlnY2eBEw55kKz9xz0LrdBOxcGhCTeG61S98ebbfZhZ2qpQ?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 27: Excerpt from Dirk-jan’s blog, pointing to a nifty little script_

At this point they went back to their Voltage\_Office356bot project before running this new script they’ve downloaded.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXekWF0XsYiBC-CoEgqK8UrY1UaPiiIHTzGPtqPbx8szPVHhq3YjsqIFM0t-Lc6kRcGvkOtbS99bYh902ZIp8SJ_SMgrHg37OnaSv-5pTf16oL37nvYbV9H4-jEairxjYXZoJc0ViA?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 28: Accessing the Voltage\_Office356bot project and running the attack script_

They started trying to run the Python script:

C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python313\\python.exe main.py -f roadtx.prt --wfb

They checked the usage again:

C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python313\\python.exe main.py --wfb

C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python313\\python.exe main.py -h

Then, they started to run it against the original victim whose cookie file we saw earlier:

C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python313\\python.exe main.py --wfb -u \[victim2\]@\[redacted2\]\[.\]com

They returned to the first victim’s cookie file:

C:\\Program Files\\Notepad++\\notepad++.exe C:\\Users\\Administrator\\Downloads\\Telegram

Desktop\\Cookies\_\[victim1\]@\[redacted1\]\[.\].com.json

This is where our EDR data drops off, as they may have become aware of us and uninstalled the agent.

## Hours worked in a day

The attacker’s browser history gives us an unprecedented level of insight into their everyday activity, searches, workflows, research, and more. The browser history shows the threat actor working intensively almost every day between the period of May 29, 2025 through July 9, 2025.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc3ab_uCw7LAEXInDYXjd7TmBrVy9ya4Ts1-cE0PyIob4M72fa2_Tk3TEkOYdbP7iy9tmupb0DDohxQNJgeSMAr506Hafcec43BavyoEkahwchD7vT8s-hyDdffGDGq9EHCsaOd?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 29: Chart of the number of hours per day (label alternates dates) worked based on browser activities_

On many of these days, the browser entries were seen across most hours of the day, logging 12 to 14 hours. But there was some variation, as seen in Figure 29, above: on several days, the threat actor worked as little as one to two hours.

When we hone in on a few of the days when the most hours were put in, we can see some of the things that piqued the attacker’s interest in those days. We analyzed the urls to see what businesses, or categories they might have fallen into, and then looked to see how many times the attacker visited these sites.

We can see a few trends. During these days, the attacker spent a lot of time researching various banking entities and bank personnel. To further expand on some of the graph labels:

- **Attack infra:** Malicious websites or servers set up by an attacker (maybe not this one) hosting frameworks like Evilginx and other known tools.

- **Banking:** Various banking websites

- **Browser extension:** Various browser extensions like ad blockers, etc. installed by the attacker to protect themselves.

- **Corporate & Business:** Various business websites not housed under a different category.

- **Crypto:** Various cryptocurrency and blockchain websites.

- **Cybersecurity:** Various cybersecurity vendor websites. The attacker often signed up for trials at various vendors to test things.

- **Government & military:** Various official government or military websites.

- **News, media & information:** Various news websites like CNN etc.  The attacker often read articles related to various breaches.

- **OSS:** Open source projects, often housed at github or gitlab.

- **Recon:** Activities where the attacker was using Censys, Urlscan, Google, etc., to do reconnaissance for a particular target.

- **Research:** When the attacker was researching a particular vulnerability, tool, or attack.

- **Sandbox:** The attacker often seemed interested in various types of malware that were on VirusTotal, Joe’s Sandbox, and other online sandboxes.

- **Social media:** Various telegram, X, and other social media posts read by the attacker.

- **Software:** Various legitimate software, like 7zip.

- **Telecommunications:** A telecommunication website, like Verizon.

- **Web & IT infrastructure:** Various online hosting services, like Mega, Amazon AWS, and Azure.


![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeTnRYZ5UecKB0lbDChgSzrXWbWX0fEovim-80e_19RMsXo0E5a9qgfHNQo3O1CtaeYRBqb_KxRstFyQ4bvTPuhkzHyErXQm6HwrveX4ZHa1iI5L6d_ok1Q1kQkRXS5PxWOxqLA-Q?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 30: Activities on May 29, 2025_

We can see that from May 29 to June 1, 2025, the attacker was mostly looking at various banking websites. Digging further into their activities, you see them researching various banks, reading about Telegram Bots, then downloading a blueprint from Make.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfuywnEM7RW_ZkLOxbQZeuoVqdGldnY-omgFuDS_04qfSG_fGnj5B1VZe_e9KzER-OxIqmjMkIgUc-oocjunMpyxu7v-cRnpR76e7bIfoTt0P72HD3W3BUgmWok21gtTDUCPePa?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 31: A deeper look at some of the activities on May 29, 2025_

The next day, it seems that the attacker spent a little more time researching various attack infrastructure, in addition to focusing on banks, and similar activities seen previously.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdS9sYzhZKAUCn8qisDHnX3bsx2AsI1fndNgrvlZPttiXuYgWEFur_rWgBTBUQnNoaztRFWT_pR0GjCRrvUzffieqr9YslltASZsm4pAOMbshDsn6XRRcrJsQXzLGMD-yxkmI57?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 32: Activities on May 30, 2025_

On May 31, 2025 and June 1, 2025, the attacker switched their focus back to mostly researching banking websites.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeEnm4HJpxep6efsiYsSgERfxUuS8g5dYMaDnrmM7l0tlnili9Q-eMvk7_xV0J32BisyWH21rHJpXO2_4l1yLL-SEicS8etF7tafwbrxcHgc1mpTDfSeh8dO_fJ6pBUsg4RzQuE?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 33: Activities on May 31, 2025_

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcMB5wsIN1bJurJmg_qq7XlkP6l7bNLAQaS0wMImke7bxsPFljQUfSsx5c9v2YmlfPNEwT8d85wrTv1YVVI_i0MPGC416pATo8EFZVqfCrVsRUReyj-UDx9E1-l7iMRKR5YqmXJ?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 34: Activities on June 1, 2025_

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdFyq-5wvfXJZaWN0Yt_wnm5DLdhcn3rrO9RLcBHFVWdw4gHtnQS5-dwHk-zfMCpcC0dCWucL27EnHJv98wxlf-1aL7t8lsfpprsab-fpWaIwc3Z6ANXt_yoNdDFPum6kQg1R85_Q?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 35: Regions Focused on by the Attacker from May 29 - June 1, 2025_

The other interesting thing was that the attacker was mostly focused on banks and sites that were in Nigeria during this time period, even looking for things like:

“No. 1 regulated crypto exchange in Nigeria.”

“top crypto companies nigeria”

“Best Crypto Exchanges in Nigeria”

“Top Cryptocurrency Companies in Nigeria”

While we don’t know where the attacker is based, the machine they had installed our agent upon appeared to be based in the United States, on the West Coast, based on the machine’s internal time zone and IP address.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeWmHY5K8jss5peWWOwpCT8uD8waJOux14dAx3FlDr-CfJDXv9oXw4QX-duI7f7_IiBl-d3-tVhJOowQkDAegJcEUfeG8gtihRewvYJ8AXTNLrLimo9Olk9pazdgO5UFAQyGeR9?key=6dcQwm6GIQlCTfuUoMFMyQ)_Figure 36: Activities on July 9, 2025_

It seems that the attacker had spent quite some time looking at our various capabilities after they had started a trial with us. Figure 36 above shows just how much more time they spent interacting with the Huntress website, and particularly the account dashboard once they had started the trial.

## Lessons learned

This incident gave us in-depth information about the day-to-day activities of a threat actor, from the tools they were interested in to the ways they conducted research and approached different aspects of attacks.

Upon confirming that the machine name was one used by an adversary, we decided to release these details because they give an invaluable understanding into the mindset and behaviors of threat actors behind attacks. For other defenders, we hope that this information can help add context around the ways that threat actors conduct research and launch attacks at the backend—and the different types of organizations, tools, and platforms that interest them.

Categories

[Threat Analysis](https://www.huntress.com/blog-categories/threat-analysis)

#### See Huntress in action

Our platform combines a suite of powerful managed detection and response tools for endpoints and Microsoft 365 identities, science-backed security awareness training, and the expertise of our 24/7 Security Operations Center (SOC).

[Book a Demo](https://www.huntress.com/demo)

Share

[![Facebook icon](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2F124e49f43fd041659989deffd90e3b7c)](https://www.facebook.com/sharer/sharer.php?u=https://www.huntress.com/blog/rare-look-inside-attacker-operation)[![Twitter X icon](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2Fa59264f69adf4a4cb0092faaf95a5669)](https://twitter.com/share?url=https://www.huntress.com/blog/rare-look-inside-attacker-operation)[![Linkedin icon](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2F2a9064f27e10467cae2ee3bd79beead9)](https://www.linkedin.com/shareArticle?mini=true&amp;url=https://www.huntress.com/blog/rare-look-inside-attacker-operation)[![Download icon](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2Ff043c73bb2de45c6b1102fe11ffebedb)](http://www.reddit.com/submit?url=https://www.huntress.com/blog/rare-look-inside-attacker-operation)

![Glitch effect](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2F97d1ebf9f67945c9af2c6341e585bc21)

## You Might Also Like

[![](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2F40b868e2890449aaab56b1c0f1aadabb)\\
\\
**Recutting the Kerberos Diamond Ticket** \\
\\
Learn More\\
\\
![](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2F779e332a141048329fb98c924119138a)](https://www.huntress.com/blog/recutting-the-kerberos-diamond-ticket)

[![](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2Ff93ed5f31fd34924b360c3f6c540efba)\\
\\
**Feeling Blue(Noroff): Inside a Sophisticated DPRK Web3 Intrusion** \\
\\
Learn More\\
\\
![](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2F779e332a141048329fb98c924119138a)](https://www.huntress.com/blog/inside-bluenoroff-web3-intrusion-analysis)

[![](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2Ff8188b57155447be8cb86c6c40a0540b)\\
\\
**The Commented Kill Chain: Why Old Ransomware Playbooks Never Die** \\
\\
Learn More\\
\\
![](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2F779e332a141048329fb98c924119138a)](https://www.huntress.com/blog/why-old-ransomware-playbooks-never-die)

![](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2Fe4c269018ce94700a59e351c5b9edb99)![](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2F1aa59311842f4ca6bda70300ff181cf9)![](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2F9ad6bcb77d1842b98142269ef70c4f47)

## Sign Up for Huntress Updates

Get insider access to Huntress tradecraft, killer events, and the freshest blog updates.

Work Email\*

[Privacy](https://www.cloudflare.com/privacypolicy/) • [Terms](https://www.cloudflare.com/website-terms/)

Submit

By submitting this form, you accept our [Terms of Service](https://www.huntress.com/terms-of-use)& [Privacy Policy](https://www.huntress.com/privacy-policy)

Thank you! Your submission has been received!

Oops! Something went wrong while submitting the form.

![Huntress at work](https://cdn.builder.io/api/v1/image/assets%2F3eb6f92aedf74f109c7b4b0897ec39a8%2Fcb5efa5143804ba59d530a903d29fe5f)

![](https://cdn.builder.io/api/v1/pixel?apiKey=3eb6f92aedf74f109c7b4b0897ec39a8)

Qualified
