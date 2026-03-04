---
date: '2026-03-04'
description: Funnull Technology Inc., a prominent Southeast Asian cybercrime facilitator,
  has resurfaced as the operator of a sophisticated malware suite, RingH23. The toolkit
  leverages infected CDN nodes for large-scale “pig-butchering” scams and malicious
  JavaScript injections via typosquatted domains. Key components of the RingH23 arsenal
  include a backdoor (Badredis2s), a malicious Nginx module (Badnginx2s), and a userland
  rootkit (Badhide2s). The group's adaptive methods for traffic hijacking indicate
  advanced operational maturity. Network administrators are urged to perform immediate
  threat assessments and remediation on affected infrastructure.
link: https://blog.xlab.qianxin.com/funnull-resurfaces-exposing-ringh23-arsenal-and-maccms-supply-chain-attacks/
tags:
- cybersecurity
- supply chain attacks
- malicious JavaScript
- malware
- CDN
title: 'Funnull Resurfaces: Exposing RingH23 Arsenal and MacCMS Supply Chain Attacks'
---

# Background

Funnull (Funnull Technology Inc.), also known as Fangneng CDN, is a Philippines-registered company that publicly claims to provide CDN services. In reality, it has long operated as a key infrastructure provider for Southeast Asia’s cybercriminal ecosystem, offering one-stop services for large-scale “pig-butchering” scam operations. It has been formally designated by the U.S. government as a major cybercrime enabler and is widely referred to in Chinese underground circles as a “fraud-dedicated cloud.” On May 29, 2025, the U.S. Treasury’s Office of Foreign Assets Control (OFAC) announced sanctions against the Funnull group, after which its public operations largely stalled. However, cybercriminal supply chains are highly resilient. Established operators like Funnull often resurface after going dormant. Our latest research suggests that Funnull has re-emerged under a new identity.

The story resumes on July 9, 2025. **XLab's Cyber Threat Insight and Analysis System(CTIA)** detected that domain `download.zhw.sh` was distributing an ELF binary with 0 VirusTotal detection. What first jumped out was the image(MD5:5f34cd492c5af9f56f3c38e72320cc49) shown on hxxp://zhw.\]sh — we couldn’t help but think: these guys are unbelievably daring.

More critically, the domain embedded in the sample, **client.110.nz**, showed an astonishing 1.6 billion DNS resolutions within our Passive DNS (PDNS) system.Taken together, these anomalies strongly suggested that we were not looking at an isolated incident — but rather at something much bigger.

![turing_180m.png](https://blog.xlab.qianxin.com/content/images/2025/12/turing_180m.png)

We began the analysis with considerable excitement and quickly reached an initial conclusion: the ELF file is a downloader. It attempts to retrieve multiple payloads from a remote server, including `udev.sh`, `udev.rules`, `module.so`, `libutilkeybd.so`, and `ring04h_office_bin`. However, due to the absence of a valid session token and group key, we were unable to pass the server-side validation mechanism and therefore could not obtain the subsequent samples.Nevertheless, based on the intended purposes of these payloads — such as `libutilkeybd.so` leveraging the LD\_PRELOAD mechanism for hijacking and `udev.rules` enabling persistence via Udev — we are highly confident that the downloader is malicious.

To uncover its true objective, we conducted proactive hunting using the file names as pivots and quickly identified key components: `module.so` and `libutilkeybd.so`. One month later, we captured the first `ring04h_office_bin` sample. The gradual acquisition of these samples allowed us to reconstruct the attack chain.The attackers first compromised a GoEdge management node and implanted an infection module named `infection_init`. This module then issued SSH remote commands to force all edge nodes to download and execute `downloader_init`. The `downloader_init` component — the aforementioned downloader — subsequently deployed a structured suite of malicious payloads across compromised nodes.

The toolkit exhibits clear modular separation of responsibilities. Based on the recurring string “RING04H” in samples and the fact that the `office_bin` module decrypts configuration files using XOR 23, we designated the toolkit **RingH23**. It consists of multiple purpose-built components, including:

- **udev.sh & udev.rules**: Rare Udev-based persistence scripts and rules
- **module.so (Badnginx2s)**: A malicious Nginx module responsible for traffic hijacking, cryptocurrency wallet replacement, and malicious JavaScript injection
- **ring04h\_office\_bin (Badredis2s)**: A backdoor module maintaining long-term node persistence, with C2 hosted on Azure Blob Storage
- **libutilkeybd.so (Badhide2s)**: A userland rootkit used to conceal payload activity

One of the core objectives of this campaign is to inject malicious JavaScript into web pages, hijacking visitors and redirecting them to gambling and pornographic websites. These scripts are hosted on typosquatted domains impersonating major public CDN providers, including:

- `code.jquecy[.]com` (impersonating jquery.com)
- `cdn.jsdclivr[.]com` (impersonating jsdelivr.com)
- `cdnjs.clondflare[.]com` (impersonating cloudflare.com)
- `static.bytedauce[.]com` (impersonating bytedance.com)

These domains were registered in 2025 and according to our telemetry, they have already achieved significant reach. For example, `clondflare` peaked on August 30, 2025, with 340,000 unique client visits in a single day. It is important to note that our data source covers approximately 5% of the domestic market. Extrapolating proportionally, `clondflare` may have been accessed — actively or passively — by an estimated 6.8 million users nationwide on that day alone. The scale of impact is staggering.

![ring_clondflare.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_clondflare.png)

It is evident that the group behind this campaign is far from an ordinary hacking outfit. Using the malicious JavaScript as a pivot for attribution, we conducted a trace-back analysis and made a striking discovery: the JS code deployed in this operation is virtually identical to the scripts used in the February 2024 Polyfill.io supply-chain attack and the two official GoEdge poisoning incidents in May 2024.The threat actor behind those operations was none other than the notorious **Funnull cybercriminal group**.

As our investigation deepened, we found that Funnull has not ceased its attacks on open-source supply chains and infrastructure providers. Beyond the previously exposed CDN services, the group has expanded its targeting to the CMS ecosystem.We confirmed that the maccms.la edition of MacCMS is leveraging the same malicious JavaScript to conduct stealthy supply-chain poisoning attacks.

Below are the core findings of this research:

1. Funnull Returns — Rebranded and Fully Upgraded

Funnull is back.This is the same organization behind the 2024 Polyfill.io supply-chain attack, as well as multiple CDN poisoning incidents involving BootCDN, Bootcss, and Staticfile. It is the group publicly named by the U.S. Treasury for facilitating “pig-butchering” scams, with reported victim losses exceeding $200 million.

Previously, Funnull primarily parasitized existing public CDN services to inject malicious code. Now, it has evolved. The group has developed a fully self-owned, server-side attack framework — **RingH23** — actively compromising CDN nodes and deploying its own infrastructure. Both its operational control and technical sophistication have reached a new level.

2. Two Independent Infection Vectors

`Path One: GoEdge Management Node Compromise → SSH Lateral Propagation → RingH23 Deployment`

Attackers first compromised a GoEdge CDN management node and implanted an infection module. They then used SSH remote commands to forcibly deploy the RingH23 toolkit to all edge nodes.

RingH23 includes multiple specialized components: Badredis2s, Badnginx2s, Badhide2s. This toolkit leverages the rarely abused UDEV mechanism for persistence. The modular structure, clean separation of responsibilities, and engineering maturity clearly indicate a professional black-market development operation — not opportunistic script-kiddie activity.

`Path Two: MACCMS Official Update Channel Poisoning`

AppleCMS (maccms.la edition) is an open-source video site management system with over 2,700 stars on GitHub and widespread adoption among small and mid-sized streaming site operators in China.Evidence indicates that it has fallen under Funnull’s control. We have confirmed that the official update channel distributed malicious PHP backdoors.

The poisoning mechanism is highly deceptive:

- The payload triggers only upon the administrator’s first login after installation.
- The download link is valid for just three minutes.
- Once retrieved — or expired — the payload becomes inaccessible.

This time-limited design significantly hinders retrospective forensic analysis.

3. CDN1.AI — A Highly Suspicious New Infrastructure Layer

Domains hosting Funnull’s malicious JavaScript have recently migrated en masse to CDN1.AI. CDN1 was created in June 2025 and was rapidly adopted by Funnull’s infrastructure. However, its operational hygiene is notably poor — even its official website certificate has expired, behavior inconsistent with a legitimate CDN provider.

Given the synchronized migration timing and the rapid trust establishment pattern, we assess with high confidence that CDN1.AI is not an independent third-party CDN, but rather a newly established front infrastructure controlled by Funnull to evade tracking.This suggests the group is actively rebuilding its infrastructure layer.

4. Operational Sophistication: Precision Targeting and Behavioral Profiling

The campaign primarily targets mobile users and includes geographic and temporal restrictions (currently triggered only within the China time zone).Hijacking probability varies by time window. For example, between 4:00–7:00 AM, the redirection probability reaches as high as 80%, exploiting users’ late-night fatigue and lowered self-control.

Even more concerning is the attackers’ profiling strategy. Based on page content keywords, visitors are segmented and redirected differently — a targeting model comparable to commercial growth operations.

- **“Low-value traffic” (users visiting legitimate content):**


Initially redirected to soft-core or borderline content to lower psychological resistance, gradually increasing conversion probability.

- **“High-value traffic” (users already browsing gray-area content):**


Immediately redirected to upstream gambling platforms or high-monetization adult sites to accelerate addiction and maximize revenue extraction.


The level of behavioral segmentation and time-based probability control reflects an industrialized, data-driven criminal operation — not random monetization abuse, but structured growth hacking within the underground economy.

# Million-Level Impact Scale

Based on the existing monitoring data, although it is difficult to precisely quantify the overall infection scale of this cybercriminal campaign, observations from three dimensions — infected websites, C2 rankings, and trends in malicious JS access — are sufficient to confirm its widespread impact.

## 0x1: Detection of Infected Websites

The JS code injected into web pages has highly distinctive characteristics, such as the strings “function xxSJRox,” “MfXKwV,” and “ptbnNbK.” Through asset mapping, we identified 10,748 IP addresses matching these signatures, most of which are streaming or movie-related websites.

It is worth noting that the malicious code is dynamically injected, meaning many actually infected websites may not be detected through asset mapping.

![ring_hunter.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_hunter.png)

## 0x2: C2 Rankings

Tranco is a comprehensive ranking system used to measure website popularity, designed to provide more accurate and reliable global website ranking data. It aggregates multiple data sources, including Cisco Umbrella, Majestic, Farsight Security, Cloudflare Radar, and Chrome User Experience Report, and is widely used in academia.

Currently, most of Badredis2s’ C2 servers rank around 500,000 globally, indicating very high activity levels.

![ring_tranco.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_tranco.png)

## 0x3: Trend of Malicious JS Access

During the tracing process, we identified three additional malicious JS hosting sites: bdustatic\[.\]com, jsdelivr\[.\]vip, and macoms\[.\]la.

According to statistical data, the peak number of unique clients per day reached 580,000. Although the number has slightly declined, it currently remains at around 200,000.

Considering the market share of the data source, a conservative estimate suggests that over one million users per day are affected by the illegal sites behind these malicious JS scripts.

![ring_jstrend.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_jstrend.png)

# The Return of FUNNULL

## 0x1: Reasons for Attributing to FUNNULL

Funnull, as an upstream infrastructure provider within the Southeast Asian cybercrime ecosystem, primarily operates by bulk-purchasing clean IP addresses from cloud providers such as Amazon Web Services and Microsoft Azure. It then combines these resources with DGA-generated domains, “cleans” them, and resells them to downstream fraud groups, thereby supporting pig-butchering scams, fake investment platforms, and similar operations.

However, in multiple CDN poisoning incidents involving polyfill.io, bootcdn.net, and staticfile.org, Funnull did not merely act as a passive supplier. Instead, it directly acquired domains and injected malicious JavaScript code itself. These incidents — where the group personally conducted the malicious operations — strongly indicate that the poisoning scripts were fully controlled and operated by Funnull.

Because these scripts directly implement core malicious redirection and traffic hijacking functions, maintaining strict control ensures efficient operation of the criminal supply chain, maximizes profit-sharing returns, and avoids efficiency losses or revenue disputes caused by downstream modifications.

Based on this technical inference, we believe that JavaScript script characteristics can serve as a key basis for attack attribution. Funnull’s scripts can generally be categorized into two types: JS Loader and JS Redirector. Together, they form a traffic redirection framework. The JS Loader dynamically loads a Redirector payload disguised as a jQuery library, while the Redirector hijacks user requests that meet predefined conditions and redirects them to gambling, pornographic, or other illegal websites.

#### ① JS Loader

The core logic of the Loader relies on environment detection and anti-debugging techniques to stealthily load external resources on specific devices. The code conceals the real URL using Base64 encoding and dynamically creates a `<script>` tag via string concatenation to load a disguised jQuery library. However, execution is limited to non-Mac/Windows platforms (such as mobile devices and Linux systems).

The Loader code captured in this campaign is identical to that used in the 2023 BootCDN poisoning incident, including environment detection logic, decoding function structure, and parameter naming conventions.

![ring_jsloadercmp.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_jsloadercmp.png)

Additionally, the domain macoms\[.\]la has appeared in two other attack incidents: the Polyfill supply chain attack and the GoEdge official poisoning incident. The former has been publicly analyzed by multiple security vendors and the community and attributed to Funnull. Although no comprehensive public analysis report is yet available for the latter, based on domain reuse and the consistency of traffic hijacking patterns, we have strong reason to believe that the GoEdge poisoning incident was also carried out by the Funnull group.

![ring_goedge.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_goedge.png)

#### ② JS Redirector

The core logic of the Redirector is to implement multi-layer detection mechanisms — including device type, page keywords, timezone, and access time period — and redirect users with varying probabilities at different times of day (e.g., 60%–80% hijack probability between 00:00–08:00, and 50% during other hours) to specific pornographic, gambling, or scam-related promotional sites, thereby monetizing traffic.

Funnull’s Redirector exhibits highly distinctive stylistic traits. It typically filters by device type and primarily targets mobile devices such as smartphones and tablets. Desktop traffic has lower value, lower conversion rates, and is more likely to be detected by administrators or security software, making it less attractive for monetization.

```

  var ismobile = navigator.userAgent.match(
  /(phone|pad|pod|iPhone|iPod|ios|iPad
  |Android|Mobile|BlackBerry|IEMobile|
  MQQBrowser|JUC|Fennec|wOSBrowser|
  BrowserNG|WebOS|Symbian|Windows Phone)
  /i);

    function isPc() {
    try {
      var _0x32df76 = navigator.platform == "Win32" ||
      navigator.platform == "Windows";
      var _0x508d68 = navigator.platform == "Mac68K" ||
      navigator.platform == "MacPPC" ||
      navigator.platform == "Macintosh" ||
      navigator.platform == "MacIntel";
      if (_0x508d68 || _0x32df76) {
        return true;
      } else {
        return false;
      }
    } catch (_0x2decf9) {
      return false;
    }
  }
```

Further build an initial user profile based on page content, assess their potential commercial value, and implement differentiated traffic redirection strategies. In simple terms: for “proper” users, lure them with some pornographic content to gradually erode their mindset and make them easier targets; for “less proper” users, increase the intensity and extract maximum value.

#### Proper Users (Low-Value Traffic)

- Profile: Currently visiting mainstream, normal content pages (no obvious gray/black keywords). These users typically have higher initial vigilance, lower willingness to pay, and longer conversion cycles.

- Strategy: Prioritize pushing entry-level pornographic, suggestive, or mildly explicit content. By lowering psychological barriers and stimulating curiosity, gradually guide them toward deeper consumption scenarios, ultimately achieving conversion.


#### Less Proper Users (High-Value Traffic)

- Profile: Currently visiting pornography, gambling, lottery (e.g., Mark Six), adult navigation sites, adult live streaming, etc. (containing numerous related keywords). These users already have explicit demand, stronger willingness to pay, are sensitive to platform capability and content intensity, and have short conversion cycles.

- Strategy: Directly match them with more upstream, more professional, better-funded, and more stimulating platforms. Provide high-quality content and higher return mechanisms to accelerate user addiction and maximize per-user output (registration, first deposit, continued spending, etc.)


After determining the strategy, dynamically adjust the redirection probability based on the current time period, fully leveraging users’ psychological states and behavioral characteristics at different times of day to achieve more efficient traffic monetization:

- 00:00–01:59 – Redirect probability 60%. Users have just entered late night; vigilance begins to decline, but most are not fully relaxed yet. Suitable for moderate scaling.

- 02:00–03:59 – Redirect probability 70%. Deep night stage; users’ decision-making and self-control significantly weaken, impulsive spending increases. A golden window for breaking defenses and driving conversion.

- 04:00–06:59 – Redirect probability 80%. Early-morning peak; users are fatigued, feel stronger loneliness, and have the lowest vigilance. Acceptance of porn/gambling content and payment impulse reach peak levels. Maximum delivery intensity and highest conversion efficiency.

- 07:00–07:59 – Redirect probability drops back to 60%. Early morning; users begin to wake up and vigilance rises. Reduce intensity appropriately to avoid disrupting routines and triggering reports or churn.

- Other times (Daytime 08:00–23:59) – Base probability 50%. Users are active but more vigilant during the day; maintain moderate delivery probability.


The redirector also includes a time zone detection mechanism. Redirection is triggered only in specific regions. Based on captured samples, it currently targets China only.

```
    var _0x326fff = _0x1ec843.getHours();
    var _0x16beb8 = Intl.DateTimeFormat().resolvedOptions().timeZone;
    const _0x43a7e6 = [ "Asia/Shanghai",\
                        "Asia/Chongqing",\
                        "Asia/Harbin",\
                        "Asia/Urumqi",\
                        "Asia/Kashgar",\
                        "Asia/Beijing"];
    if (_0x43a7e6.includes(_0x16beb8)) { ... }

```

Even when all the above conditions are met, there is an additional control layer. Funnull designed a remote control switch: by dynamically loading an external JavaScript file to set the usercache variable, redirection is only executed when this variable is true, thereby enabling remote control of the attack behavior.

![ring_checkcache.png](https://blog.xlab.qianxin.com/content/images/2026/02/ring_checkcache.png)

These behaviors are typical characteristics of Funnull Redirector–type scripts. The JS scripts captured in this incident are almost identical to samples from previous poisoning campaigns in terms of overall coding style, obfuscation techniques, and core logic design, demonstrating clear family homology. Taking the scripts from the GoEdge incident and the samples delivered by the RingH23 attack kit in this campaign as examples, their stylistic similarities are immediately apparent.

![ring_cpid.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_cpid.png)

Another more direct piece of evidence is that ailyunoss.com (impersonating Alibaba Cloud), which acted as the remote control switch in this campaign, was registered on April 24, 2025. Its DNS resolution history clearly shows that between May 22 and July 9, 2025, the domain used Funnull CDN services. This discovery directly attributes both the RingH23 attack suite and the active poisoning of the official maccms.la software to the FUNNULL cybercriminal group.

![ring_aily.png](https://blog.xlab.qianxin.com/content/images/2026/02/ring_aily.png)

## 0x2: Suspicious cdn1.ai

The domains used by Funnull to host malicious JavaScript scripts are currently leveraging CDN services based on the cdn1.ai infrastructure. cdn1.ai was created on June 18, 2025. Its official website claims it is a global content delivery network, providing high-speed, stable content acceleration services with over 200 nodes, improving website access speeds by more than 95%.

![ring_cdn1.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_cdn1.png)

We classified the JS malicious domains based on CNAME records. Historical activity clearly shows the migration from Funnull’s own CDN to cdn1.ai.

![ring_old.png](https://blog.xlab.qianxin.com/content/images/2026/02/ring_old.png)

By cross-analyzing the domains involved in this campaign with domains used in past attacks, it can be observed that these domains completed the migration to cdn1.ai within a similar time window (mostly in July).

![ring_cnamemove.png](https://blog.xlab.qianxin.com/content/images/2026/02/ring_cnamemove.png)

This raises an important question: as an emerging CDN provider, how did CDN1.AI gain the trust of a mature cybercriminal organization like Funnull in such a short period? For Funnull, which generates substantial daily revenue, infrastructure choices are extremely cautious, with high requirements for stability. However, CDN1.AI’s performance appears unreliable: its technical architecture is based on the open-source GoEdge project, which is inherently inadequate for professional commercial environments. Furthermore, operational management is not very professional—for example, its official website had an expired SSL certificate that was not updated promptly, which clearly does not meet the standard expected of a stable service provider.

Currently, there is no direct evidence linking CDN1.AI to the Funnull group. However, considering its anomalous rapid trust acquisition, sloppy operational management, and migration timing closely synchronized with Funnull’s infrastructure, a technical hypothesis can be made: CDN1.AI is likely not a genuine third-party CDN, but a new alias set up by Funnull to evade tracking.

# Technical Details of MacCMS Poisoning

[MacCMS](https://github.com/magicblack/maccms10?ref=blog.xlab.qianxin.com) is a professional video content management system based on PHP and MySQL. It is free and open-source and is primarily used to quickly build and manage various video websites, such as movie, TV series, or anime sites. Thanks to its convenient content collection functions and flexible template system, it has been popular among small and medium-sized site operators since its release and is widely used for personal or small-scale commercial video platforms. The original officially maintained version (original website: maccms.com) stopped updating around 2019. Subsequently, a community version called maccms.la began providing updates and support. Its GitHub projects have accumulated over 2,700 stars, reflecting an active community and user recognition.

However, such a widely used project has become involved in a supply-chain security incident. We have clear evidence that the official upgrade channel of maccms.la was used to deliver malicious PHP backdoor code. Once executed on the server, the backdoor further injects malicious JavaScript scripts that hijack front-end pages and manipulate traffic. The technical characteristics of these malicious scripts are highly consistent with the methods used by the FUNNULL group in multiple historical attacks, supporting the industry consensus: maccms.la has effectively been controlled by the FUNNULL group, or acquired by them, and continues to operate as part of their attack infrastructure.

## 0x1: Upgrade Channel Poisoning

In the maccms GitHub source code, the file `application\admin\view_new\index\index.html` contains an AJAX snippet that reports version information of maccms, PHP, and ThinkPHP to the remote server (update.maccms.la) to check for updates.

![ring_ajax.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_ajax.png)

Everything appears normal. However, in practice, we discovered that upon the first login to the admin panel after MACCMS installation, the remote server delivers malicious JS code designed to steal sensitive data and download a malicious PHP payload.

- post：Reports sensitive information such as cookies and the admin panel URL to the remote server.
- iframe：Uses a hidden iframe to trigger MACCMS’s download mechanism and retrieve the malicious payload.

![ring_loginrps.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_loginrps.png)

When the iframe loads the URL specified in its `src` attribute `ADMIN_PATH/admin/update/step1.html?file=laupdc00ecc82ab4b6d060da64d886e97b2c4` the browser sends a request to that URL. The backend routing mechanism ultimately invokes the `step1()` function located in `application/admin/controller/Update.php.`

The core logic of this function is as follows: it receives the file parameter, appends a .zip extension, combines it with a timestamp to generate a complete resource identifier, and then sends a request to a designated remote server to fetch the corresponding file.

![ring_step1.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_step1.png)

Traffic analysis shows that `laupdc00ecc82ab4b6d060da64d886e97b2c4.zip` consists of a laupd prefix and a 32-character MD5 string, forming a typical disguised naming scheme. The `Date` and `Last-Modified` headers are identical, with a short validity period of only 3 minutes (`max-age=180`). This indicates that the file is dynamically generated on demand rather than pre-stored. After expiration, access returns “access denied,” effectively evading forensic retrieval.

![ring_cmsupd.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_cmsupd.png)

## 0x2: PHP Malicious Payload

After extraction, `laupdc00ecc82ab4b6d060da64d886e97b2c4.zip` releases `application/extra/active.php`. Additionally, another malicious PHP payload, addons.php, was discovered in the wild.

| MD5 | PATH |
| --- | --- |
| b06b9f13505eb49d6b3f4bddd64b12ce | application/extra/active.php |
| eb03db7ac9f10af66a1e2b16185fcadc | application/extra/addons.php |

Both payloads are unobfuscated and easy to analyze. Their core purpose is to inject malicious JavaScript into websites, though they use different strategies:

- addons.php dynamically injects malicious JS before the `</html>` tag.
- active.php uses a hybrid strategy:Dynamically inserts malicious JS before `</head>`. Statically modifies system JS template files by appending malicious code.

`active.php` registers a view\_filter hook within the ThinkPHP framework, ensuring that all rendered pages automatically trigger the infection process, enabling full traffic monitoring and real-time attacks.

![ring_hook.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_hook.png)

To reduce exposure, a refined filtering mechanism ensures malicious execution only when:

- The user accesses via mobile device
- The visit originates from an external referrer
- The request is not Ajax
- Each user is attacked at most once every 10 hours

![ring_condition.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_condition.png)

When the conditions are met, the process of tampering with HTML and JS is carried out. First, let’s look at the modification of HTML. Its core logic is actually to use the str\_replace function to replace $template\_marker in the webpage with `$template_token.$template_marker`.

![ring_html.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_html.png)

Both `$template_token` and `$template_marker` are encoded in octal and compressed with gzip. Readers without a PHP environment can use an online PHP Sandbox to view their contents. template\_token is malicious JS code, which should look very familiar—it is exactly the JS Loader code analyzed in the previous section. Meanwhile, template\_marker corresponds to the `<\/head>` tag.

![ring_htmlflag.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_htmlflag.png)

Next, let’s look at the modification of JS. Its core logic is to use the file\_put\_contents function to overwrite the original JS file. The malicious JS code, along with a tag in the format /\*system\_optimization\_signature\*/, is appended to the end of the JS file. system\_optimization\_signature serves as the indicator of whether the JS file has been infected. It is the first 12 bytes of the MD5 value of the malicious JS code, specifically `138ae887806f`.

![ring_jsflag.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_jsflag.png)

Searching for `138ae887806f` on Google reveals many users discussing this infection. However, users’ cleanup efforts often remain limited to removing the infected JavaScript files—addressing only the surface symptom. The deeper PHP malicious payload, as well as the official poisoning channel of maccms\[.\]la that serves as a persistent attack source, often goes undetected and unremoved. As a result, websites are repeatedly reinfected with malicious code, falling into a cycle of “cleanup–reinfection.”

![ring_googlejs.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_googlejs.png)

# Technical Details of RingH23 Arsenal

## 0x1: infect\_init

The basic information of the infection\_init component is shown below. It is an infector implemented in Golang and packed using standard UPX.

```
MD5:65ac2839ab2790b6df8e80022982a2c0
Magic:ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, stripped section header size
Packer: UPX
```

infect\_init must be executed with root privileges. At a minimum, three parameters must be provided: session\_token, service\_url, and group. The default value of service\_url is service.client.110\[.\]nz.

![ring_infectusage.png](https://blog.xlab.qianxin.com/content/images/2025/12/ring_infectusage.png)

First, it sequentially verifies whether the token and group are valid with the server specified by server\_url. Both verifications use the GET method, and the User-Agent is hardcoded as Azure.

- Token verification request:


The URI used is /api/session/verify, and the specified token is stored in the X-Session header field.

![ring_session.png](https://blog.xlab.qianxin.com/content/images/2025/12/ring_session.png)

- Group verification request:


The URI used is /api/client\_group/"group". In the traffic shown below, the group value is j6.

![ring_group.png](https://blog.xlab.qianxin.com/content/images/2025/12/ring_group.png)

After token and group pass verification, the program traverses the /proc directory to locate the edge-admin process. It then retrieves the database username and password from the process configuration file api\_db.yaml, and executes the following SQL query to obtain edge nodes and their login credentials from the database:

```
SELECT n.id, n.name, n.clusterId, l.type, l.params
FROM edgeNodes AS n LEFT JOIN edgeNodeLogins AS l
ON n.id=l.nodeId WHERE n.state=1
```

After successfully obtaining the node login credentials, it executes the Main\_SSHExec function, which logs into the edge nodes via SSH to download the next-stage payload.

![ring_sshexec.png](https://blog.xlab.qianxin.com/content/images/2025/12/ring_sshexec.png)

The core logic of Main\_SSHExec is to execute the following script to deploy the next-stage download\_init component on the edge node, where DOWNLOAD\_URL is:

`download.zhw[.]sh/EMrsVQj9VQ/init`

![ring_script.png](https://blog.xlab.qianxin.com/content/images/2025/12/ring_script.png)

## 0x2: download\_init

The basic information of the download\_init component is shown below. It is a downloader implemented in Golang and protected with the standard UPX packer.

```
MD5:5d6c33bf931699805206b00594de5e71
MAGIC:ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, stripped
PACKER:UPX
```

The main purpose of download\_init is to download the next-stage malicious payloads, including a backdoor Trojan, a rootkit, udev persistence rules, and an Nginx module.

![ring_download.png](https://blog.xlab.qianxin.com/content/images/2025/12/ring_download.png)

Similar to infect\_init, download\_init must also be executed with root privileges. In addition to the three parameters service\_token, service\_url, and group, it must also specify a run mode, such as "install" for installation or "uninstall" for removal.

![ring_dlusage.png](https://blog.xlab.qianxin.com/content/images/2025/12/ring_dlusage.png)

Unlike infect\_init, after the group parameter passes validation, download\_init extracts the hash field from the JSON data returned by the C2 server for use in subsequent register requests.

![ring_hash.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_hash.png)

Next, download\_init attempts to retrieve information about the Nginx server on the compromised device, including the version number and compilation configuration parameters such as ngx\_compat, ngx\_dav, ngx\_threads, and ngx\_real\_ip. It then uses this information to construct a register request in order to obtain the download URLs for the next-stage payloads. The URI format of this request is /api/register/{hash}.

![ring_register.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_register-1.png)

From the JSON data returned by the C2, the download URLs of various payloads can be observed. download\_init extracts the hash field and uses it to complete the entire infection lifecycle. The specific steps are as follows:

First, it creates a directory named after the hash under /var/adm to store the downloaded malicious payloads.

Next, it implants the udev\_rules file into the system rules directory /etc/udev/rules.d, naming it 99-{hash}.rules to achieve persistence and automatic execution after system reboot.

Then, it renames kernel.so to libutilkeybd.so and writes its path into /etc/ld.so.preload, leveraging the system’s preload mechanism to conceal the malicious process activity.

Finally, it launches the backdoor module office\_bin to maintain persistent control over the infected device, and restarts the Nginx process to dynamically load the module.so module, hijacking traffic that meets specific conditions to redirect users to pornographic or gambling websites, thereby completing the deployment of all payloads.

![ring_payloads.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_payloads.png)

## 0x3: office\_bin

office\_bin is a highly modular and plugin-based backdoor Trojan that uses AES encryption for network communication. During dynamic analysis, a large number of strings related to redis2s are printed, so we named it badredis2s. It consists of three main components: Dropper, Client, and Plugin. Since the binaries are not stripped, reverse engineering is relatively straightforward and the functionality is clear at a glance.

![ring_badredis.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_badredis.png)

Dropper: First, let’s look at the Dropper. The following sample is selected as the primary analysis target:

```
MD5: 79c492bfd8a35039249bacc6a31d7122
MAGIC: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.32, not stripped
Packer: None
```

Its main purpose is to load an embedded ELF file and execute its exported function `kernel_module_entry`, with the parameter config\_base64, which points to the encrypted configuration data.

![ring_dropper.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_dropper.png)

Client: The basic information of the file released by the Dropper is as follows:

```
MD5:ae0de7034c4866556675740f6647bfcc
MAGIC:ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, not stripped
Packer: None
```

The core logic of the Client is concise and efficient:

It first decrypts the encrypted configuration to extract key parameters such as the C2 server address, task execution schedule, and communication keys. When the system time matches the predefined execution policy, the client attempts to establish a communication channel with the C2 server and waits to receive and execute remote commands.

Notably, this malware employs dual-layer redundancy mechanisms for both C2 acquisition and network transmission, enhancing robustness.

**（1）C2 Acquisition Mechanism**

- It first dynamically retrieves the latest C2 address from Microsoft Azure Blob Storage.
- If cloud retrieval fails, it automatically falls back to a hardcoded backup C2 address.

**（2）Network Transmission Mechanism**

- It prioritizes communication over WebSocket over TLS (wss).
- If the wss connection fails due to firewall blocking or network restrictions, it switches to DNS tunneling as a fallback transmission method.

The following sections analyze the Client’s technical implementation in terms of configuration decryption, C2 acquisition, time validation, and network communication.

#### ① Configuration Decryption

The configuration is protected using a simple "xor + base64" scheme. The base64 encoding uses the standard alphabet, and the XOR key is 0x23.

![ring_config.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_config.png)

The decrypted configuration contains information such as the C2 address, time rules, AES key, and initialization vector.

![ring_decryptconfig.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_decryptconfig.png)

#### ② C2 Acquisition

The first 250 bytes of the configuration store the cloud configuration URL for the primary C2, followed by 278 bytes for the backup C2. The primary C2 must be dynamically retrieved via the cloud configuration, while the backup C2 can be used directly.

![ring_c2.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_c2.png)

Access the cloud configuration address of C2 Server 2, and you'll see an IIS logo page that appears perfectly normal. However, the secret is hidden in the webpage source code within the `RequestID:/#$*SRUNT0pNVltHSlBXUUwNTUZXGRcXEA==*#$/` section.

![ring_mainc2.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_mainc2.png)

The Client uses the regex pattern `\\s*/#\\$\\*.*?\\*#\\$/` to extract SRUNT0pNVltHSlBXUUwNTUZXGRcXEA==, which is actually an encrypted C2 configuration. After Base64 decoding and single-byte XOR with 0x23, it reveals the C2 server **j6.linuxdistro.net:443**, which is consistent with the backup C2 server.

#### ③ Time Window Validation

The Client uses the `time_for_connect` function to determine whether execution is allowed at the current time. It reads a time whitelist from fixed offsets in the configuration (hour list starting at offset 0x210, minute list starting at offset 0x270) and compares it with the current system time.

However, according to the decrypted configuration, the current policy allows execution 24/7, with no restrictions on hours (0–23) or minutes (0–59).

![ring_timerule.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_timerule.png)

#### ④ Network Communication

The Client adopts a “WSS-first, DNS-tunnel fallback” dual-channel strategy. Through precise time control and failure-count mechanisms, it maintains C2 reachability while mimicking normal network traffic behavior as much as possible. When stealthy WSS communication is blocked, the sample switches to DNS tunneling within a limited time window to maintain control channel continuity, and later automatically reverts to the primary communication method.

Reverse engineering of the communication data shows that application-layer data within the WSS channel follows a “compress → encrypt” process:

- zlib compression

- AES-128-CBC encryption


The AES key is read from offset 0x360 (16 bytes) in the configuration structure, and the IV is located at offset 0x370 (16 bytes).

![ring_configaes.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_configaes.png)

The DNS tunnel implementation is based on the open-source tool `iodine`, which encapsulates IPv4 data into DNS requests and responses, enabling communication in environments where normal internet access is restricted but DNS queries are still allowed.

The related runtime parameters are stored at configuration offset `0x3E5`. From this, the Name Server 8.8.8.8 and the Top Domain nsj6.linuxdistro.net can be extracted.

![ring_iodine.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_iodine.png)

After receiving response data from the C2, the Client first performs AES decryption, then zlib decompression, and finally passes the parsed plaintext data to the `kernel_on_message` function, executing corresponding functional logic based on different command IDs.

| Command ID | Function |
| --- | --- |
| 0x01 | Upload Device Info |
| 0x02 | Reboot |
| 0x03 | Shutdown |
| 0x04 | Edig Comment in redis2s-client |
| 0x06 | Edit Group in redis2s-client |
| 0x08 | Restart Client |
| 0x0a | module info |
| 0x0c | module data |
| 0x12 | run module |
| 0x13 | exit client |
| 0x17 | uninstall client |
| 0x18 | send help info |
| 0x19 | "put, get, ps" cmd |
| 0x21 | save file |
| 0x22 | quantity\_execute |

Next, we illustrate the Client’s network packet format using real traffic generated in a virtual machine. The intercepted wss traffic is shown below:

![ring_wss.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_wss.png)

Let’s examine the first command sent from the C2 to the Client. After AES-CBC decryption and decompression, the plaintext is:`01 01 00 00 00 00 04 00 00 00 01 00 00 00`

The Client’s network packet format follows:

> 1-byte flag + 4-byte cmd count + 1-byte type + 4-byte cmd1 length + 4-byte cmd1

Parsing the plaintext shows this is command `0x00000001`, requesting device information upload.

```
#AES KEY: 2B990667D0E087AE
#AES IV:  27FAD11C481BD789

# CipherText

00000000  0e 1d 85 54 28 12 fb f2 9a 3c dd 02 6c 83 ed f9  |...T(.ûò.<Ý.l.íù|
00000010  87 3d 0d 46 1c 94 9d 46 26 55 5c 2a 9a 72 1c aa  |.=.F...F&U\*.r.ª|

#PlainText

00000000  01 01 00 00 00 00 04 00 00 00 01 00 00 00        |..............|
flag:1
cmd count: 1
type: 0
cmd1 length:4
cmd1: 0x00000001
```

If readers attempt to decrypt the second command using the provided CyberChef workflow, they will find decryption fails. This is because, unlike standard AES-CBC mode, Badredis2s uses `AES-CBC with chained IV`, meaning the IV for each message is the last ciphertext block of the previous message.

To decrypt the second command, the IV must be set to the last 16 bytes of the first ciphertext: `87 3d 0d 46 1c 94 9d 46 26 55 5c 2a 9a 72 1c aa`

![ring_chainiv.png](https://blog.xlab.qianxin.com/content/images/2026/01/ring_chainiv.png)

Finally, let’s look at the Plugin component. In Badredis2s, command 0x12 is related to plugin operations.

After implementing the Badredis2s network protocol in our command-tracking system, we successfully tracked command 0x12 and captured two plugins: shell and filemanager. Each plugin has its own dedicated Request-URI:

- shell → /index/sl.html

- filemanager → /index/fm.html


![ring_cmd12.jpg](https://blog.xlab.qianxin.com/content/images/2026/01/ring_cmd12.jpg)

During analysis of the `filemanager` plugin, three additional plugins were discovered. Observing naming patterns reveals a correlation between plugin names and paths. By brute-forcing paths, we identified a new URI `/index/ao.html`, though we were unable to infer its corresponding plugin name or capture it.

| Plugin Name | Request-URI |
| --- | --- |
| filesearch | /index/fs.html |
| filetransport | /index/ft.html |
| filedownloader | /index/fd.html |

The functionality of the plugins is reflected in their names: for example, shell executes shell commands, while filemanager handles file management.

This plugin-based architecture significantly enhances Badredis2s’ flexibility. Attackers can easily perform complex tasks by deploying different functional plugins. Since these plugins are neither obfuscated nor stripped, analysis is relatively straightforward. Readers interested in implementation details may further explore them independently; this article does not elaborate further.

![ring_plugins.png](https://blog.xlab.qianxin.com/content/images/2026/02/ring_plugins.png)

## 0x4: module.so

module.so is a malicious Nginx filtering module, which we name Badnginx2s. Its basic information is as follows:

```
MD5: 563f5e605ebf1db8065fd41799e71bf9
MAGIC: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, not stripped
Packer: None
```

Badnginx2s is a relatively rare Nginx backdoor Trojan. Essentially, it is an Nginx module that implants a malicious filter at the web server layer to deeply tamper with outbound traffic. Its main functions include:

- Remote Command Execution: A covert command channel is reserved for executing remote commands.

- Download Hijacking: When users download specific types of files from an infected website, the Trojan secretly replaces the download link.

- Code Injection: Injects malicious JavaScript into webpages to redirect visitors to gambling, pornographic, or other malicious websites, monetizing traffic or facilitating further fraud.

- Video Insertion: Inserts a 5-second malicious media segment into M3U8 playlist files for streaming hijacking or advertisement injection.

- Digital Asset Theft: Replaces cryptocurrency wallet addresses on webpages with attacker-controlled addresses, silently diverting user transfers and enabling covert financial theft.


Badnginx2s implements these functions by registering two HTTP filter functions: ngx\_http\_hello\_header\_filter and ngx\_http\_hello\_body\_filter.

- The header\_filter handles the HTTP response header stage, performing remote command execution, policy updates, download hijacking, and marking specific pages for malicious injection.

- The body\_filter processes the HTTP response body stage, injecting malicious JavaScript and replacing wallet addresses on the client side.


This design enables Badnginx2s to flexibly perform stealthy and precise malicious operations at different response stages, achieving both server-side remote control and client-side theft and fraud.

#### ① Remote Command Execution

The attacker hides remote commands in the Cookie field of HTTP request headers for covert communication.

- The comm field stores the encrypted command, originally formatted as "timestamp$$command" (e.g., 1768813387$$whoami). It is first XOR-encrypted with key 0x5A, then Base64-encoded before transmission.

= The sign field contains a Base64-encoded digital signature generated using the P-256 elliptic curve. Badnginx2s verifies the signature using a public key to ensure command integrity and authenticity.

This mechanism allows attackers to execute remote commands within seemingly normal HTTP requests.

![ring_execcmd.png](https://blog.xlab.qianxin.com/content/images/2026/02/ring_execcmd.png)

#### ② Config Manipulation

Badnginx2s dynamically generates hijacking configurations at runtime, including redirect domains, malicious JS payload URLs, and whitelist IP ranges.

To enable remote real-time configuration control, attackers establish a covert management channel via Cookie fields:

- Configuration operation commands are encrypted and stored in the conf field (using the same XOR + Base64 method as comm).

- The digital signature is stored in the sign field and validated using the P-256 elliptic curve algorithm.


For example, to query the current configuration, the original command `get$$` is encrypted and placed in the conf field. After signature verification, the server returns the current configuration. This mechanism allows attackers to dynamically adjust redirect domains, malicious JS payload addresses, and other parameters.

![ring_getconf.png](https://blog.xlab.qianxin.com/content/images/2026/02/ring_getconf.png)

#### ③ Download Hijacking

When requests target APK, PLIST, or MOBILECONFIG resources, Badnginx2s performs download hijacking. It dynamically constructs domains using the format:`https://%s.aqyaqua.com` and returns corresponding malicious payloads.

![ring_dlhijack.png](https://blog.xlab.qianxin.com/content/images/2026/02/ring_dlhijack.png)

Notably, aqyaqua.com serves only as a traffic gateway, forwarding different resource types to separate target addresses. Currently, only the APK payload remains active.

![ring_b9apk.png](https://blog.xlab.qianxin.com/content/images/2026/02/ring_b9apk.png)

#### ④ Page Tampering

Badnginx2s performs webpage tampering via the ngx\_http\_hello\_body\_filter function, including wallet replacement, video insertion, and malicious JS injection.

- Cryptocurrency Wallet Replacement

When Ethereum or TRON wallet addresses appear in webpage content, they are replaced with attacker-controlled addresses.

For example:

- Ethereum → 0xAA3Bd92445a2E1fE38C7693d77259BeD42a144c3

- TRON → TCMCY9ccNmQGfUNHTNtCByCof3VdQnip2b


This enables silent transaction hijacking without user awareness.

![ring_cryptoaddr.png](https://blog.xlab.qianxin.com/content/images/2026/02/ring_cryptoaddr.png)

- Video Insertion

When targeting webpages related to HLS live streams, attackers modify M3U8 playlist files to insert custom video segments.

We have captured one instance where a 5-second segment named 广告\_1.ts was inserted. Although seemingly an advertisement insertion, the potential risks are far greater. Attackers could replace content with pornography, violence, AI-generated political propaganda, fake news, or highly convincing deepfake videos. Such attacks could disrupt public opinion, manipulate ideology, and interfere with social order, representing a highly scalable and socially harmful attack vector.

![ring_video.png](https://blog.xlab.qianxin.com/content/images/2026/02/ring_video.png)

- Malicious JS Injection

For HTML pages, Badnginx2s searches tags in priority order: `<head>, </title>, <html>, <meta>, <script>,` and injects malicious JavaScript at the first matching location.

The injected JS follows a fixed template concatenated with a Base64 string corresponding to the previously analyzed JS loader.

The hardcoded Base64 string in the sample:`aHR0cHM6Ly9jZG5qcy5qc2RjbGl2ci5jb20vbnBtL2Jvb3RzdHJhcEA1LjMuMC9kaXN0L2Nzcy9ib290c3RyYXAubWluLmNzcz92PTMuNy44LjI=`，decodes to:`https://cdnjs[.]jsdclivr[.]com/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css?v=3.7.8.2`。

![ring_jstemp.png](https://blog.xlab.qianxin.com/content/images/2026/02/ring_jstemp.png)

## 0x5: libutilkeybd.so

libutilkeybd.so is a userland rootkit based on LD\_PRELOAD technology, which we name Badhide2s. Its basic information is:

```
MD5: 85cdf5139f0a0a0f7e378bc2029d662b
MAGIC: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, not stripped
Packer: None
```

The core objectives of Badhide2s are:

- Payload Trace Concealment

- Dynamic Injection of the Nginx Module


- **Concealment** By writing itself into /etc/ld.so.preload, it ensures automatic loading and filters outputs of common tools such as ss, netstat, top, htop, ps, ls, and lsof, hiding traces across three dimensions: files, processes, and network connections.This userland rootkit technique is common in Linux malware. While Badhide2s introduces no major technical innovations, it hides 25 IP addresses—relatively large in scale.
- **Module Injection**：By hooking `__libc_start_main` (the GNU C library entry function), it inspects processes at startup. When detecting Nginx, it modifies startup parameters to append:`-g load_module /var/adm/{hash}nginx/module.so`. thus stealthily loading the malicious module.

![ring_ngxload.png](https://blog.xlab.qianxin.com/content/images/2026/02/ring_ngxload.png)

Notably, Badhide2s includes an environment variable trigger switch: if the environment variable RING04 exists and matches a specific hash value, all hiding functions are automatically disabled. This provides defenders with a rapid investigation method—after obtaining the hash, executing:`export RING04H={hash}` instantly disables concealment and reveals hidden processes, files, and network connections.

## 0x6: udev rule & script

Using udev rules for persistence is uncommon in Linux threats. Public cases include sedexp and UNC3886. udev is Linux’s device management system responsible for dynamically managing /dev device nodes and handling hotplug events. Rules are typically located in:

- /etc/udev/rules.d/

- /lib/udev/rules.d/


A typical rule:

```
ACTION=="add", KERNEL=="device", RUN+="/path/to/script"
```

In this campaign, a rule named 99-{hash}.rules is added under /etc/udev/rules.d. When any non-loopback network interface is recognized (add event), it triggers systemd-run to stealthily execute: `/var/adm/{hash}/udev/udev.sh` 。

![ring_udevrules.jpg](https://blog.xlab.qianxin.com/content/images/2026/01/ring_udevrules.jpg)

The udev.sh script simply launches the previously analyzed Badredis2s backdoor (ring04h\_office\_bin) and an unknown component (ring04h\_agent\_bin).

![ring_udevsh.jpg](https://blog.xlab.qianxin.com/content/images/2026/01/ring_udevsh.jpg)

# Additional Intelligence

Within download\_init, a main\_pre function cleans up traces strongly associated with RingH23. The cleanup array contains 17 strings, including libcext.so.2 and /var/log/cross/auto-colar, which are clearly related to the autocolor backdoor disclosed by Palo Alto Networks on February 24, 2025.

![ring_specialstring.jpg](https://blog.xlab.qianxin.com/content/images/2026/01/ring_specialstring.jpg)

Additionally, /var/log/jroqq is a highly distinctive string. Using it as a clue, we identified a Golang-based backdoor named auto-color.

This backdoor enforces single-instance execution via a file lock /var/log/jroqq/auto.l, though it does not create this file itself—indicating coordination with other components. Internally, we refer to it as V2deck.

Its primary function is to execute C2-issued commands and return results. The sample embeds 10 C2 addresses protected by XOR + Base64 (XOR key: poop).

![ring_v2deck.jpg](https://blog.xlab.qianxin.com/content/images/2026/01/ring_v2deck.jpg)

Observed commands indicate V2deck collects information about Nginx and FikkerCDN processes, aligning with RingH23 targets:

```
ps -ef | grep Fikker | grep -v grep | wc -l

ss -antp | grep nginx |grep ESTAB | awk {'print $5'} | awk -F\: {'print $1'} | sort | uniq | wc -l
```

Although we currently associate V2deck with RingH23 at medium confidence, its extremely low detection rate and C2 visibility warrant public disclosure alongside this report.

# Conclusion

This summarizes most of the intelligence currently available regarding Funnull’s new cybercriminal campaign.

We strongly recommend that network administrators and website owners conduct immediate self-inspections and follow these mitigation guidelines:

#### ① For RingH23

Use ldd to check command dependencies, focusing on the malicious module:`/var/adm/{uuid}/kernel/libutilkeybd.so`。

If found:

- Set environment variable RING04H={uuid} to disable rootkit protection.

- Remove malicious artifacts:
  - Related entries in /etc/ld.preload.conf

  - /etc/udev/99-{uuid}.rules

  - All files under /var/adm/{uuid}

#### ② For maccmsp\[.\]la

It is not recommended to continue using maccms\[.\]la.

If migration is not possible:

- Use grep xxSJRox to check template JS injection.

- Use grep gzuncompress to check for suspicious hidden PHP payloads.

- Remove:
  - /application/extra/active.php

  - /application/admin/controller/Update.php

  - Modify the AJAX upgrade domain in: /application/admin/view\_new/index/index.html

Such cybercriminal operations are profit-driven and persistent. Only through cross-industry collaboration and intelligence sharing can they be effectively contained.

We invite security vendors and technical institutions to collaborate with us in intelligence sharing and coordinated response efforts. If you are interested in our research or possess relevant insights, feel free to contact us via the [X platform](https://x.com/Xlab_qax?ref=blog.xlab.qianxin.com).

# IOC

#### Badredis2s C2

```
ntp[.]asia
ntporg[.]com
sbindns[.]com
plusedns[.]com
mirrors163[.]com
linuxdistro[.]net
debianhacks[.]net
fedoraforums[.]net
ubuntucommands[.]com
```

#### Badredis2s C2 Config URL

```
https://3snzh72om4.apifox[.]cn
https://node.blob.core.windows[.]net/update/a1
https://node.blob.core.windows[.]net/update/a2
https://node.blob.core.windows[.]net/update/s7
https://node.blob.core.windows[.]net/update/s10
https://node.blob.core.windows[.]net/update/s11
https://node.blob.core.windows[.]net/update/s14
https://node.blob.core.windows[.]net/update/h2.debianhacks.net/online
https://node.blob.core.windows[.]net/update/j6.linuxdistro.net/online

https://az-blob.110[.]nz/update/s1
https://az-blob.110[.]nz/update/s2
https://az-blob.110[.]nz/update/s3
https://az-blob.110[.]nz/update/s4
https://az-blob.110[.]nz/update/s7
https://az-blob.110[.]nz/update/s9
```

#### Badnginx2s Related

```
gadlkd1[.]com

apk.aqyaqua[.]com
plist.aqyaqua.]com
mobileconfig.aqyaqua[.]com

https://dowoxox.gfewr[.]com/B9.apk
https://plist.ztyfv[.]com/d/4F48MCiqtsjDCS7QOWs3KU.plist
https://download.joymeet[.]top/app/2PG/00056321.mobileconfig
```

#### V2deck C2

```
bobolickp92[.]cc
realfake909[.]net
firelategg[.]net
lucycally[.]me
moxymodiy[.]cc
9688hopeeasy[.]cc
flysky55[.]me
goyppg06[.]com
tutupytua[.]com
zybbzlast[.]com
```

#### IPs & Domains in Badhide2s

```
54.46.13.139
8.139.6.156
18.167.103.220
18.163.102.174
16.163.50.192
43.199.147.209
13.251.54.69
43.199.133.158
18.166.58.136
16.162.25.97
52.221.206.136
43.198.221.151
43.198.137.198
43.198.73.3
16.163.58.55
20.6.129.16
20.205.25.192
35.75.5.45
52.195.191.106
52.195.7.27
52.196.178.89
52.194.222.58
13.231.108.219
13.114.119.159
3.112.67.113
54.46.1.220

js.mirrors163[.]com
cn.js.mirrors163[.]com
update.ntporg[.]com
js.ntp[.]asia
js.ntporg[.]com
s10.ntporg[.]com
s11.ntporg[.]com
client.110[.]nz
js2.ntporg[.]com
a.plusedns[.]com
b.plusedns[.]com
js.sbindns[.]com
```

#### JS HOST

```
jquecy[.]com
jsdclivr[.]com
jsdelivr[.]vip
bytedauce[.]com
bdustatic[.]com
clondflare[.]com
macoms[.]la
ailyunoss[.]com
ailyun-oss[.]com
```

#### JS PAYLOAD URL

```
https:]//code.jquecy[.]com/jquery.min-3.6.8.js
https://cdnjs.clondflare[.]com/jquery.min-3.7.8.1.js

https:]//cdnjs.jsdclivr[.]com/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css?v=3.7.8.2
https:]//static.bytedauce[.]com/ajax/libs/bootstrap/5.3.3/css/bootstrap-grid.min.css

https:]//union.macoms[.]la/jquery.min-4.0.2.js
https:]//cdn.jsdelivr[.]vip/jquery.min-3.7.0.js
https:]//api.bdustatic[.]com/jquery.min-4.0.12.js
```

#### Downloader URL

```
https://az-blob.110[.]nz/update/init
http://download.zhw[.]sh/wK4QYDIRFV/init
http://download.zhw[.]sh/9aE5EFdJoS/init

https://bucket.service.generate.110[.]nz/udev.sh

https://bucket.service.generate.110[.]nz/2025-12-19/7d1d49a8d8c1fa7b4b743ed551fa338c112268e1/module.so

https://bucket.service.generate.110[.]nz/2025-12-19/7d1d49a8d8c1fa7b4b743ed551fa338c112268e1/udev.rules

https://bucket.service.generate.110[.]nz/2025-12-19/7d1d49a8d8c1fa7b4b743ed551fa338c112268e1/kernel.so
```

#### VIDEO AD URL

```
https://oss2025-6f57.obs.ap-southeast-1.myhuaweicloud[.]com/%E5%B9%BF%E5%91%8A_1.ts
```

#### Sample MD5

```
663706d4f3948417d05c11bbfa6cdbc9 *init
65ac2839ab2790b6df8e80022982a2c0 *init
5d6c33bf931699805206b00594de5e71 *init

85cdf5139f0a0a0f7e378bc2029d662b *kernel.so
3bff298be46f8817862bce2ac0be3176 *kernel.so
6acb8bbcad3b8403f4567412cc6aa144 *kernel.so
946606977dd177347122867750244ae2 *kernel.so
92c630062f0fe207c628b95fade34b96 *kernel.so
563f5e605ebf1db8065fd41799e71bf9 *module.so
112e2eb2a57129ef175c3f64bccbac04 *module.so
cd36ec10f71b89dc259eb8825e668ae3 *module.so
6e14853a6ad5e752a516290bf586d700 *udev.rule
b5dfe88131fb1b3622a487df96be84e1 *udev.sh
79c492bfd8a35039249bacc6a31d7122 *ring04h_office_bin
2e7a42c9be6fc3840df867cb19c7afa5 *ring04h_office_bin
a688afd342cee9feb74c61503fb0b895 *ring04h_office_bin
85f3d29a8fd59e00fec83743664fb2b5 *ring04h_office_bin
fef497841554fff318b740dff7df3a49 *ring04h_office_bin
dfd1fbf0a98e0984da9516311ccc1f05 *ring04h_office_bin
da594309691161f6e999984c26e1a10f *ring04h_office_bin
18b699375c76328b433145bdac02ec49 *ring04h_office_bin
d3b0b6496747ee77ab15e5f5d9583a67 *ring04h_office_bin

b5a5d93cfc443ecbd3b52cfe485b738c *shell.plugin
296318b90bc9d01ab045da042b0ecb21 *filesearch.plugin
b8239ce64c07e39ae7bed9ae8f5f3d2f *filemanager.plugin
51830656b0825b22703e4fcf31aec84c *filetransport.plugin
22f0d58bc482d413a5cc8922c7f79378 *filedownloader.plugin

b06b9f13505eb49d6b3f4bddd64b12ce *active.php
eb03db7ac9f10af66a1e2b16185fcadc *addons.php
```

# Cyberchef

```
https://gchq.github.io/CyberChef/#recipe=From_Hexdump()AES_Decrypt(%7B'option':'Latin1','string':'2B990667D0E087AE'%7D,%7B'option':'Latin1','string':'27FAD11C481BD789'%7D,'CBC','Raw','Raw',%7B'option':'Hex','string':''%7D,%7B'option':'Hex','string':''%7D)Drop_bytes(0,4,false)Zlib_Inflate(0,0,'Adaptive',false,false)To_Hexdump(16,false,false,false)&input=MDAwMDAwMDAgIDBlIDFkIDg1IDU0IDI4IDEyIGZiIGYyICA5YSAzYyBkZCAwMiA2YyA4MyBlZCBmOSAgIC4uLlQoLi4uIC48Li5sLi4uDQowMDAwMDAxMCAgODcgM2QgMGQgNDYgMWMgOTQgOWQgNDYgIDI2IDU1IDVjIDJhIDlhIDcyIDFjIGFhICAgLj0uRi4uLkYgJlVcKi5yLi4&ieol=CRLF
```

Disqus Comments

We were unable to load Disqus. If you are a moderator please see our [troubleshooting guide](https://docs.disqus.com/help/83/).

What do you think?

0 Responses

![Upvote](https://c.disquscdn.com/next/current/publisher-admin/assets/img/emoji/upvote-512x512.png)

Upvote

![Funny](https://c.disquscdn.com/next/current/publisher-admin/assets/img/emoji/funny-512x512.png)

Funny

![Love](https://c.disquscdn.com/next/current/publisher-admin/assets/img/emoji/love-512x512.png)

Love

![Surprised](https://c.disquscdn.com/next/current/publisher-admin/assets/img/emoji/surprised-512x512.png)

Surprised

![Angry](https://c.disquscdn.com/next/current/publisher-admin/assets/img/emoji/angry-512x512.png)

Angry

![Sad](https://c.disquscdn.com/next/current/publisher-admin/assets/img/emoji/sad-512x512.png)

Sad

G

Start the discussion…

﻿

Comment

###### Log in with

###### or sign up with Disqus  or pick a name

### Disqus is a discussion network

- Don't be a jerk or do anything illegal. Everything is easier that way.

[Read full terms and conditions](https://docs.disqus.com/kb/terms-and-policies/)

This comment platform is hosted by Disqus, Inc. I authorize Disqus and its affiliates to:

- Use, sell, and share my information to enable me to use its comment services and for marketing purposes, including cross-context behavioral advertising, as described in our [Terms of Service](https://help.disqus.com/customer/portal/articles/466260-terms-of-service) and [Privacy Policy](https://disqus.com/privacy-policy), including supplementing that information with other data about me, such as my browsing and location data.
- Contact me or enable others to contact me by email with offers for goods or services
- Process any sensitive personal information that I submit in a comment. See our [Privacy Policy](https://disqus.com/privacy-policy) for more information

Acknowledge I am 18 or older

- [Favorite this discussion](https://disqus.com/embed/comments/?base=default&f=xlab-qax&t_i=ghost-69a40ea2f39f9e0001b252d3&t_u=https%3A%2F%2Fblog.xlab.qianxin.com%2Ffunnull-resurfaces-exposing-ringh23-arsenal-and-maccms-supply-chain-attacks%2F&t_d=Funnull%20Resurfaces%3A%20Exposing%20RingH23%20Arsenal%20and%20MacCMS%20Supply%20Chain%20Attacks&t_t=Funnull%20Resurfaces%3A%20Exposing%20RingH23%20Arsenal%20and%20MacCMS%20Supply%20Chain%20Attacks&s_o=default# "Favorite this discussion")

  - ## Discussion Favorited!



    Favoriting means this is a discussion worth sharing. It gets shared to your followers' Disqus feeds, and gives the creator kudos!


     [Find More Discussions](https://disqus.com/home/?utm_source=disqus_embed&utm_content=recommend_btn)

[Share](https://disqus.com/embed/comments/?base=default&f=xlab-qax&t_i=ghost-69a40ea2f39f9e0001b252d3&t_u=https%3A%2F%2Fblog.xlab.qianxin.com%2Ffunnull-resurfaces-exposing-ringh23-arsenal-and-maccms-supply-chain-attacks%2F&t_d=Funnull%20Resurfaces%3A%20Exposing%20RingH23%20Arsenal%20and%20MacCMS%20Supply%20Chain%20Attacks&t_t=Funnull%20Resurfaces%3A%20Exposing%20RingH23%20Arsenal%20and%20MacCMS%20Supply%20Chain%20Attacks&s_o=default#)

  - Tweet this discussion
  - Share this discussion on Facebook
  - Share this discussion via email
  - Copy link to discussion

  - [Best](https://disqus.com/embed/comments/?base=default&f=xlab-qax&t_i=ghost-69a40ea2f39f9e0001b252d3&t_u=https%3A%2F%2Fblog.xlab.qianxin.com%2Ffunnull-resurfaces-exposing-ringh23-arsenal-and-maccms-supply-chain-attacks%2F&t_d=Funnull%20Resurfaces%3A%20Exposing%20RingH23%20Arsenal%20and%20MacCMS%20Supply%20Chain%20Attacks&t_t=Funnull%20Resurfaces%3A%20Exposing%20RingH23%20Arsenal%20and%20MacCMS%20Supply%20Chain%20Attacks&s_o=default#)
  - [Newest](https://disqus.com/embed/comments/?base=default&f=xlab-qax&t_i=ghost-69a40ea2f39f9e0001b252d3&t_u=https%3A%2F%2Fblog.xlab.qianxin.com%2Ffunnull-resurfaces-exposing-ringh23-arsenal-and-maccms-supply-chain-attacks%2F&t_d=Funnull%20Resurfaces%3A%20Exposing%20RingH23%20Arsenal%20and%20MacCMS%20Supply%20Chain%20Attacks&t_t=Funnull%20Resurfaces%3A%20Exposing%20RingH23%20Arsenal%20and%20MacCMS%20Supply%20Chain%20Attacks&s_o=default#)
  - [Oldest](https://disqus.com/embed/comments/?base=default&f=xlab-qax&t_i=ghost-69a40ea2f39f9e0001b252d3&t_u=https%3A%2F%2Fblog.xlab.qianxin.com%2Ffunnull-resurfaces-exposing-ringh23-arsenal-and-maccms-supply-chain-attacks%2F&t_d=Funnull%20Resurfaces%3A%20Exposing%20RingH23%20Arsenal%20and%20MacCMS%20Supply%20Chain%20Attacks&t_t=Funnull%20Resurfaces%3A%20Exposing%20RingH23%20Arsenal%20and%20MacCMS%20Supply%20Chain%20Attacks&s_o=default#)

Be the first to comment.

[Load more comments](https://disqus.com/embed/comments/?base=default&f=xlab-qax&t_i=ghost-69a40ea2f39f9e0001b252d3&t_u=https%3A%2F%2Fblog.xlab.qianxin.com%2Ffunnull-resurfaces-exposing-ringh23-arsenal-and-maccms-supply-chain-attacks%2F&t_d=Funnull%20Resurfaces%3A%20Exposing%20RingH23%20Arsenal%20and%20MacCMS%20Supply%20Chain%20Attacks&t_t=Funnull%20Resurfaces%3A%20Exposing%20RingH23%20Arsenal%20and%20MacCMS%20Supply%20Chain%20Attacks&s_o=default#)
