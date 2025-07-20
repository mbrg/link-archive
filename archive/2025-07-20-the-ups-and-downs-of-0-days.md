---
title: "The ups and downs of 0-days"
tags:
   - cybersecurity
   - 0-day vulnerabilities
   - threat intelligence
   - software patching
   - exploit analysis
link: https://blog.google/threat-analysis-group/0-days-exploited-wild-2022/%23:~:text%3DOver%252040%2525%2520of%2520the%25200%252Ddays%2520discovered%2520were%2520variants%2520of%2520previously%2520reported%2520vulnerabilities/
date: 2025-07-20
summary: "In 2022, 41 0-day vulnerabilities were exploited in the wild, a significant drop from 69 in 2021, signaling improvements in cybersecurity resilience. Notably, patch delays on Android platforms allowed n-days to function like 0-days. Although browsers saw fewer 0-day exploits due to enhanced defenses, many attackers shifted to 0-click methods. Over 40% of 0-days were variants of previously identified vulnerabilities, underscoring a persistent challenge. The report advocates for faster patching, broader mitigations, and improved collaboration in vulnerability management to effectively tackle these trends."
---

[Threat Analysis Group](https://blog.google/threat-analysis-group/)

# The ups and downs of 0-days

Jul 27, 2023

·

4 min read

Share

[Twitter](https://twitter.com/intent/tweet?text=The%20ups%20and%20downs%20of%200-days%20%40google&url=https://blog.google/threat-analysis-group/0-days-exploited-wild-2022/) [Facebook](https://www.facebook.com/sharer/sharer.php?caption=The%20ups%20and%20downs%20of%200-days&u=https://blog.google/threat-analysis-group/0-days-exploited-wild-2022/) [LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://blog.google/threat-analysis-group/0-days-exploited-wild-2022/&title=The%20ups%20and%20downs%20of%200-days) [Mail](mailto:?subject=The%20ups%20and%20downs%20of%200-days&body=Check%20out%20this%20article%20on%20the%20Keyword:%0A%0AThe%20ups%20and%20downs%20of%200-days%0A%0AThe%20goal%20of%20this%20report%20is%20to%20analyze%20the%20exploits%20from%20the%20year%20as%20a%20whole,%20looking%20for%20trends,%20gaps,%20lessons%20learned,%20and%20successes.%0A%0Ahttps://blog.google/threat-analysis-group/0-days-exploited-wild-2022/)

Copy link

Our review of 0-days exploited in-the-wild in 2022.


M

Maddie Stone

Threat Analysis Group


Share

[Twitter](https://twitter.com/intent/tweet?text=The%20ups%20and%20downs%20of%200-days%20%40google&url=https://blog.google/threat-analysis-group/0-days-exploited-wild-2022/) [Facebook](https://www.facebook.com/sharer/sharer.php?caption=The%20ups%20and%20downs%20of%200-days&u=https://blog.google/threat-analysis-group/0-days-exploited-wild-2022/) [LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://blog.google/threat-analysis-group/0-days-exploited-wild-2022/&title=The%20ups%20and%20downs%20of%200-days) [Mail](mailto:?subject=The%20ups%20and%20downs%20of%200-days&body=Check%20out%20this%20article%20on%20the%20Keyword:%0A%0AThe%20ups%20and%20downs%20of%200-days%0A%0AThe%20goal%20of%20this%20report%20is%20to%20analyze%20the%20exploits%20from%20the%20year%20as%20a%20whole,%20looking%20for%20trends,%20gaps,%20lessons%20learned,%20and%20successes.%0A%0Ahttps://blog.google/threat-analysis-group/0-days-exploited-wild-2022/)

Copy link

* * *

* * *

This is Google’s fourth annual Year in Review of 0-days exploited in-the-wild \[ [2021](https://googleprojectzero.blogspot.com/2022/04/the-more-you-know-more-you-know-you.html), [2020](https://googleprojectzero.blogspot.com/2021/02/deja-vu-lnerability.html), [2019](https://googleprojectzero.blogspot.com/2020/07/detection-deficit-year-in-review-of-0.html)\] and builds off of the [mid-year](https://googleprojectzero.blogspot.com/2022/06/2022-0-day-in-wild-exploitationso-far.html) 2022 review. The goal of this report is not to detail each [individual exploit](https://googleprojectzero.github.io/0days-in-the-wild/rca.html), but instead to analyze the exploits from the year as a whole, looking for trends, gaps, lessons learned and successes.

Our full 2022 Year in Review report is available [on our website](https://security.googleblog.com/2023/07/the-ups-and-downs-of-0-days-year-in.html).

## Executive summary

Forty-one in-the-wild 0-days were detected and disclosed in 2022, the second-most ever recorded since we [began tracking in mid-2014](https://docs.google.com/spreadsheets/d/1lkNJ0uQwbeC1ZTRrxdtuPLCIl7mlUreoKfSIgajnSyY/edit#gid=0), but down from the 69 detected in 2021. Although a 40% drop might seem like a clear-cut win for improving security, the reality is more complicated. Some of our key takeaways from 2022 include:

**_N-days function like 0-days on Android due to long patching times._** Across the Android ecosystem there were multiple cases where patches were not available to users for a significant time. Attackers didn’t need 0-day exploits and instead were able to use n-days that functioned as 0-days.

**_0-click exploits and new browser mitigations drive down browser 0-days._** Many attackers have been moving towards 0-click rather than 1-click exploits. 0-clicks usually target components other than the browser. In addition, all major browsers also implemented new defenses that make exploiting a vulnerability more difficult and could have influenced attackers moving to other attack surfaces.

**_Over 40% of the 0-days discovered were variants of previously reported vulnerabilities._** Seventeen out of the 41 in-the-wild 0-days from 2022 are variants of previously reported vulnerabilities. This continues the unpleasant trend that we’ve discussed previously in both the [2020 Year in Review](https://googleprojectzero.blogspot.com/2021/02/deja-vu-lnerability.html) report and the [mid-way through 2022](https://googleprojectzero.blogspot.com/2022/06/2022-0-day-in-wild-exploitationso-far.html) report. More than 20% are variants of previous in-the-wild 0-days from 2021 and 2020.

**_Bug collisions are high._** 2022 brought more frequent reports of attackers using the same vulnerabilities as each other, as well as security researchers reporting vulnerabilities that were later discovered to be used by attackers. When an in-the-wild 0-day targeting a popular consumer platform is found and fixed, it's increasingly likely to be breaking another attacker's exploit as well.

Based on our analysis of 2022 0-days we hope to see the continued focus in the following areas across the industry:

1. More comprehensive and timely patching to address the use of variants and n-days as 0-days.
2. More platforms following browsers’ lead in releasing broader mitigations to make whole classes of vulnerabilities less exploitable.
3. Continued growth of transparency and collaboration between vendors and security defenders to share technical details and work together to detect exploit chains that cross multiple products.

## What now?

Looking back on 2022 our overall takeaway is that as an industry we are on the right path, but there are also plenty of areas of opportunity, the largest area being the industry’s response to reported vulnerabilities. Moving forward, we must:

- Get fixes and mitigations to users quickly so that they can protect themselves.
- Perform detailed analyses to ensure the root cause of the vulnerability is addressed.
- Share as many technical details as possible.
- Capitalize on reported vulnerabilities to learn and fix as much as we can from them.

None of this is easy, nor is any of this a surprise to security teams who operate in this space. It requires investment, prioritization and developing a patching process that balances both protecting users quickly and ensuring it is comprehensive, which can at times be in tension. Required investments depend on each unique situation, but we see some common themes around staffing/resourcing, incentive structures, process maturity, automation/testing, release cadence and partnerships.

We’ve detailed some efforts that can help ensure bugs are correctly and comprehensively fixed in [this post](https://googleprojectzero.blogspot.com/2022/06/2022-0-day-in-wild-exploitationso-far.html). We will continue to help with these analyses, but we hope and encourage platform security teams and other independent security researchers to invest in these efforts as well.

![A bar graph showing the number of in-the-wild 0-days detected per year.](https://storage.googleapis.com/gweb-uniblog-publish-prod/images/image1_7ijmwED.width-100.format-webp.webp)

## Final thoughts: TAG’s New Exploits Team

Looking into the second half of 2023, we’re excited for what’s to come. You may notice that our previous reports have been on the Project Zero blog and this one is on the Threat Analysis Group’s (TAG) blog. Our 0-days in-the-wild program has moved from Project Zero to TAG in order to combine the vulnerability analysis, detection and threat actor tracking expertise all in one team, benefiting from more resources and ultimately making: TAG Exploits! More to come on that, but we’re really excited for what this means for protecting users from 0-days and making 0-day hard.

One of the intentions of our Year in Review is to make our conclusions and findings “peer-reviewable.” If we want to best protect users from the harms of 0-days and make 0-day exploitation hard, we need all the eyes and brains we can get tackling this problem. We welcome critiques, feedback, and other ideas on our work in this area. Please reach out at 0day-in-the-wild <at> google.com.

POSTED IN:

### Related stories

[Threat Analysis Group **TAG Bulletin: Q1 2025** \\
\\
This bulletin includes coordinated influence operation campaigns terminated on our platforms in Q1 2025. It was last updated on May 15, 2025.JanuaryWe terminated 12 YouT…\\
\\
By\\
\\
\\
\\
Billy Leonard\\
\\
\\
May 15, 2025](https://blog.google/threat-analysis-group/tag-bulletin-q1-2025/)

[Threat Analysis Group **TAG Bulletin: Q4 2024** \\
\\
This bulletin includes coordinated influence operation campaigns terminated on our platforms in Q4 2024. It was last updated on February 19, 2024.OctoberWe terminated 11…\\
\\
By\\
\\
\\
\\
Billy Leonard\\
\\
\\
Dec 17, 2024](https://blog.google/threat-analysis-group/tag-bulletin-q4-2024/)

[Threat Analysis Group **TAG Bulletin: Q3 2024** \\
\\
This bulletin includes coordinated influence operation campaigns terminated on our platforms in Q3 2024. It was last updated on January 14, 2025.JulyWe terminated 89 You…\\
\\
By\\
\\
\\
\\
Billy Leonard\\
\\
\\
Sep 12, 2024](https://blog.google/threat-analysis-group/tag-bulletin-q3-2024/)

[![](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/TAG_PzwyAeM.width-1600.format-webp.webp)\\
\\
Threat Analysis Group **State-backed attackers and commercial surveillance vendors repeatedly use the same exploits**\\
\\
By\\
\\
\\
\\
Clement Lecigne\\
\\
\\
Aug 29, 2024](https://blog.google/threat-analysis-group/state-backed-attackers-and-commercial-surveillance-vendors-repeatedly-use-the-same-exploits/)

[Threat Analysis Group **Iranian backed group steps up phishing campaigns against Israel, U.S.** \\
\\
Google’s Threat Analysis Group shares insights on APT42, an Iranian government-backed threat actor.\\
\\
By\\
\\
\\
\\
Google Threat Analysis Group\\
\\
\\
Aug 14, 2024](https://blog.google/threat-analysis-group/iranian-backed-group-steps-up-phishing-campaigns-against-israel-us/)

[Threat Analysis Group **Google disrupted over 10,000 instances of DRAGONBRIDGE activity in Q1 2024** \\
\\
Today we are sharing updated insights about DRAGONBRIDGE, the most prolific IO actor Google’s Threat Analysis Group (TAG) tracks.\\
\\
By\\
\\
\\
\\
Zak Butler\\
\\
\\
Jun 26, 2024](https://blog.google/threat-analysis-group/google-disrupted-dragonbridge-activity-q1-2024/)

.

Jump to position 1
Jump to position 2
Jump to position 3
Jump to position 4
Jump to position 5
Jump to position 6

Survey

How could we improve this article?

Make it more conciseAdd more detailMake it easier to understandInclude more images or videosIt's fine the way it is

✅

Thank you!
