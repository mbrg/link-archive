---
date: '2026-01-07'
description: Amitai Cohen's "Rhythms of Research" emphasizes the interpretative nature
  of cyber threat analysis, highlighting that understanding malicious activity depends
  on both data quality and research frameworks. He argues our views are inherently
  subjective, shaped by organizational constraints and analytical methodologies. Cohen
  suggests that researchers must broaden telemetry collection and methodologies to
  capture hidden signals indicating adversaries' actions. He advocates for collaboration
  in threat hunting and detection engineering to circumvent individual limitations
  and enhance threat visibility. This approach can lead to improved detection capabilities
  and more informed security strategies in dynamic cyber environments.
link: https://amitaico.substack.com/p/the-indirect-realism-of-threat-research
tags:
- threat intelligence
- cybersecurity
- detection engineering
- data analysis
- malicious activity
title: The Indirect Realism of Threat Research - by Amitai Cohen
---

[![Rhythms of Research](https://substackcdn.com/image/fetch/$s_!cQCT!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F60f4e19e-ed69-4393-ae96-923df70582a4_586x586.png)](https://amitaico.substack.com/)

# [Rhythms of Research](https://amitaico.substack.com/)

SubscribeSign in

# The Indirect Realism of Threat Research

### Metaphors for interpreting malicious activity in cyberspace

[![Amitai Cohen's avatar](https://substackcdn.com/image/fetch/$s_!FKmQ!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F612a6bac-be19-4439-891e-e5e1cd633c05_1500x1513.png)](https://substack.com/@amitaico)

[Amitai Cohen](https://substack.com/@amitaico)

Dec 26, 2025

3

Share

When investigating malicious cyber activity - whether in the context of threat intelligence, threat hunting, or detection engineering - we must keep in mind that we’re not observing said activity directly, but rather interpreting its effects on reality through a **particular lens** composed of two parts:

1. **The quality and quantity of our data** \- the breadth and depth of telemetry to which we have access (network traffic logs, runtime detection alerts, file samples, cloud control plane logs, SaaS platform logs, etc.), our sources of metadata enrichment (such as [VirusTotal](http://virustotal.com/gui/) or [Shodan](https://www.shodan.io/)), and our corpus of past incidents.

2. **Our conceptual framework** \- our assumptions about how attackers operate, their motivations, their goals, their tooling, and how their behavior might express itself in our data.


In other words, our perception of any given malicious activity is always [indirect](https://en.wikipedia.org/wiki/Direct_and_indirect_realism) and **subjective**, as it depends on the parameters of our working environment: our collection capabilities, our analysis tools, our methodology; our clientele, their sector, their geography, their platforms, their hardware, their software; the actors targeting them, and many other variables.

Every vendor, government agency, research group, and independent researcher might view the same malicious activities through their own porthole, analyzing a unique **cross-section** of cyberspace. In the [words of Kurt Vonnegut](https://en.wikipedia.org/wiki/Slaughterhouse-Five):

> _\[Billy was\] strapped to a steel lattice which was bolted to a flatcar on rails, and there was no way he could turn his head or touch the pipe. The far end of the pipe rested on a bi-pod which was also bolted to the flatcar. All Billy could see was the little dot at the end of the pipe. He didn’t know he was on a flatcar, didn’t even know there was anything peculiar about his situation. The flatcar sometimes crept, sometimes went extremely fast, often stopped - went uphill, downhill, around curves, along straightaways. Whatever poor Billy saw through the pipe, he had no choice but to say to himself, “That’s life”._

As for threat actors, we must always recall that they’re **real people** \- albeit working within constraints defined by organizations, bureaucracies and social norms - meaning they exist across all aspects of reality. As they traverse the various media of cyberspace, they leave **traces** that we might detect in the course of our monitoring and investigation.

A hacker pressing a key on their keyboard in a cubicle somewhere in Moscow or Beijing may eventually and indirectly cause a new row to be recorded in one of our telemetry databases, but that can hardly be said to be the **full picture**. Our task is to **interpret** such signals as [more than mere shadow puppetry](http://beijing/), and to deduce what _other signals_ may exist beyond our line of sight.

[![](https://substackcdn.com/image/fetch/$s_!kvOD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7a8429e-66d0-4169-a8b8-bf151b9c1c17_1203x825.png)](https://substackcdn.com/image/fetch/$s_!kvOD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7a8429e-66d0-4169-a8b8-bf151b9c1c17_1203x825.png) Credit: [Attribution of Advanced Persistent Threats \ Timo Steffens](https://link.springer.com/book/10.1007/978-3-662-61313-9) (page 44)

Our ability to observe any given type of evidence depends on the sophistication and configuration of our **instrumentation**, and collecting that evidence requires pointing our devices at different **“layers”** of our subject matter. This is analogous to using a combination of infrared, X-ray and radio telescopes in astronomy, while also operating robotic probes to retrieve exotic materials from asteroids and employing chemical analysis techniques such as [gas chromatography](https://en.wikipedia.org/wiki/Gas_chromatography) to determine their composition.

Much like **[flatlanders](https://en.wikipedia.org/wiki/Flatland)**, at our weakest and most solitary, threat researchers are akin to two-dimensional creatures striving to make sense of the chaotic goings-on of **multi-dimensional space**. Moreover, we find ourselves contending with malevolent higher beings that appear to span the unknowable infinitude of cyberspace.

[![](https://substackcdn.com/image/fetch/$s_!kvDf!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F59f135ef-859b-4425-a1b3-e1c4d4fdff7b_432x216.gif)](https://substackcdn.com/image/fetch/$s_!kvDf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F59f135ef-859b-4425-a1b3-e1c4d4fdff7b_432x216.gif) A three-dimensional cube falling through a two-dimensional plane ( [source](https://www.math.union.edu/~dpvc/talks/2007-05-23.sigma-xi/cube-slice-corner.html))

For example, a resourceful attacker targeting our organization as a whole is likely to elude our comprehension if we’re **overly focused** on network traffic analysis while ignoring their activity on endpoint and mobile devices or across cloud and SaaS platforms. Moreso if we wrongly assume that network traffic is _all there is_.

But all is not lost - we can invest in **intelligence** to guide our efforts (and product roadmap), **join forces** with others working towards the same goal (each bringing their own unique perspective), expand our **telemetry collection** apparatus, and point it in the **most promising** directions. So long as we know more or less what we’re looking for and have a well-trained nose for **novelty**, we can jointly overcome our individual sensorial limitations and more accurately perceive the motion of our adversaries on the wire.

[![undefined](https://substackcdn.com/image/fetch/$s_!58L_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9bb29cb8-2d41-4377-8f9f-fa3b34267bc8_876x808.png)](https://substackcdn.com/image/fetch/$s_!58L_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9bb29cb8-2d41-4377-8f9f-fa3b34267bc8_876x808.png) [Blind men appraising an elephant](https://en.wikipedia.org/wiki/Blind_men_and_an_elephant) (parable originating in India; cybersecurity analogy credited to [Joe Słowik](https://x.com/jfslowik/status/1762231682978161150))

I’ve found that methodically monitoring for apparent “plot holes” is an effective method of revealing **missing signals (false negatives)**, indicating hidden aspects of malicious activity that we’re not perceiving to the fullest, taking place in higher dimensions, so to speak.

For instance, if we detect a machine in our environment in communication with a known C2 server but _without_ detecting any files that would otherwise indicate the presence of malware, we can immediately deduce that we’re missing something.

Similarly, a compromised server with no prior risk detections (assuming we’re scanning for such things) might indicate a potential 0-day vulnerability affecting the software installed on it. This technique can be automated, and is applicable to both threat hunting and detection engineering.

The next step in such cases is to determine whether we need to adjust existing detection rules, add new ones, or perhaps collect a **brand new type of telemetry**, essentially expanding the scope of our research into yet another dimension of cyberspace (fun!).

Thanks for reading Rhythms of Research! Subscribe to be updated about new posts.

Subscribe

[![Drag0nR3b0rn's avatar](https://substackcdn.com/image/fetch/$s_!51YD!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F702c8fd8-f5d6-4a47-b8a3-e8fe8ece8acb_2048x2038.jpeg)](https://substack.com/profile/13652852-drag0nr3b0rn)[![Mauricio Ortiz's avatar](https://substackcdn.com/image/fetch/$s_!HlAV!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f0865d6-8c12-42ac-be95-5bb421e28b28_144x144.png)](https://substack.com/profile/29289716-mauricio-ortiz)

3 Likes

3

Share

TopLatest

[Thrunting Grounds](https://amitaico.substack.com/p/thrunting-grounds)

[When are IOCs not IOCs? Join me on a pedantic adventure.](https://amitaico.substack.com/p/thrunting-grounds)

Sep 17, 2023•[Amitai Cohen](https://substack.com/@amitaico)

3

![](https://substackcdn.com/image/fetch/$s_!9mzr!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F16975d39-941f-445b-9cb9-79a2d57979dd_920x613.webp)

[Intelligence Failure in Threat Detection](https://amitaico.substack.com/p/intelligence-failure-in-threat-detection)

[False negatives in our grasp of the fabric of spacetime](https://amitaico.substack.com/p/intelligence-failure-in-threat-detection)

Jan 5, 2024•[Amitai Cohen](https://substack.com/@amitaico)

1

![](https://substackcdn.com/image/fetch/$s_!SlW0!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65b89f5e-bdf4-4ef8-88fe-6aed0ecc8005_1200x500.jpeg)

[Achieving Research Fluency](https://amitaico.substack.com/p/achieving-research-fluency)

[Prepare, Submerge, Flow & Practice](https://amitaico.substack.com/p/achieving-research-fluency)

Feb 5, 2022•[Amitai Cohen](https://substack.com/@amitaico)

4

![](https://substackcdn.com/image/fetch/$s_!yRUt!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F52e7605c-0cbf-4770-b948-69a62086ebae_1920x1280.jpeg)

See all

### Ready for more?

Subscribe
