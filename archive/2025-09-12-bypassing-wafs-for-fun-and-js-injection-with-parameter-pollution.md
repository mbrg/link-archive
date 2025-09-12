---
date: '2025-09-12'
description: In a recent pentesting analysis, a method leveraging HTTP Parameter Pollution
  (HPP) was employed to bypass strict WAFs for JavaScript injection. By exploiting
  differences in parameter handling between ASP.NET and WAF engines, attackers concatenated
  admissible JavaScript into single string outputs that evaded detection. Testing
  against 17 WAF configurations illustrated that traditional signature-based systems
  are increasingly vulnerable as payload complexity rises, with a 70.6% bypass rate
  for complex HPP payloads. Conversely, modern ML-based WAFs showed superior detection
  capabilities. This highlights critical gaps in WAF configurations and underscores
  the need for more nuanced security strategies.
link: https://blog.ethiack.com/blog/bypassing-wafs-for-fun-and-js-injection-with-parameter-pollution
tags:
- Parameter Pollut
- XSS
- WAF
title: Bypassing WAFs for Fun and JS Injection with Parameter Pollution
---

[Latest on Ethiack](https://blog.ethiack.com/blog/tag/latest-on-ethiack) [Hacking with AI](https://blog.ethiack.com/blog/tag/hacking-with-ai)

# Bypassing WAFs for Fun and JS Injection with Parameter Pollution

[![](https://blog.ethiack.com/hs-fs/hubfs/1657583561080.jpeg?width=50&height=50&name=1657583561080.jpeg)](https://blog.ethiack.com/blog/author/bruno-mendes)

[Bruno Mendes](https://blog.ethiack.com/blog/author/bruno-mendes)
04/08/25 09:19


During a recent autonomous pentest, our engine identified a fascinating XSS vulnerability in one of our client's applications. The target was an ASP.NET application running behind a Web Application Firewall (WAF) with a very strict configuration. The vulnerability itself was straightforward. An attacker could break out of a Javascript string delimited by single quotes. However, since the application was protected by a highly restrictive WAF, conventional XSS payloads were effectively blocked. I’m here to tell you the story of how bypassing this WAF led us down a rabbit hole.

This scenario presented us with a classic security challenge: How do you demonstrate the exploitability of a vulnerability when defensive mechanisms are actively preventing its exploitation?

For us, this was a PoC\|\|GTFO situation. As always, the devil is in the details. We needed to get creative and understand how we could abuse the parsing differences between the WAF engine, the parameter parser and the Javascript interpreter that will ultimately execute the code in the victim browser.

Our breakthrough came when we reminded ourselves of previous engagements where we abused ASP.NET's parameter pollution behavior to exploit other types of injections. Combining this technique with the specific context of the vulnerability we had in hands seemed very possible. We could build valid Javascript by splitting the code between different parameters to avoid WAF detection.

## Building a Payload

### Understanding Parameter Pollution

HTTP Parameter Pollution is a technique that exploits the inconsistent ways different technologies handle duplicate HTTP parameters. When multiple parameters with the same name are present in a request, various web frameworks process them differently. Some concatenate all values, others take only the first or last occurrence, and some even create arrays.

The behavior of parameter pollution varies significantly across different web technologies. A very comprehensive summary of how the different frameworks behave was already compiled by other researchers \[1-3\].

Since our use case was very specific, we filtered all the frameworks that did not include all of the parameters in the final output, leaving us with 5 different frameworks:

|     |     |     |
| --- | --- | --- |
| **Framework** | **Input** | **Output** |
| **ASP.NET** | param=val1&param=val2 | param=val1,val2 |
| **ASP** | param=val1&param=val2 | param=val1,val2 |
| **Golang net/http - r.URL.Query()\[“param”\]** | param=val1&param=val2 | param=\['val1','val2'\] |
| **Python - Zope** | param=val1&param=val2 | param=\['val1','val2'\] |
| **Node.js** | param=val1&param=val2 | param=val1,val2 |

Fortunately, ASP.NET’s behavior is particularly interesting and fits our use case. When ASP.NET encounters multiple parameters with the same name, it concatenates their values with commas using the HttpUtility.ParseQueryString() method. This behavior is documented in [Microsoft's official documentation](https://learn.microsoft.com/en-us/dotnet/api/system.web.httputility.parsequerystring?view=net-9.0), which states that “multiple occurrences of the same query string parameter are listed as a single entry with a comma separating each value”.

The power of this class of parameter pollution becomes apparent when combined with Javascript injection contexts. Consider a scenario similar to what we were facing, where user input is reflected within a Javascript string:

userInput = 'USER\_CONTROLLED\_DATA';

A simple approach to the problem might attempt to break out using quotes and inject code:

'; alert(1); //

However, most WAFs are equipped to detect such obvious patterns (as we will see later in this blog post). The parameter pollution approach takes a different strategy.

Javascript's syntax allows for comma-separated expressions, where multiple statements can be executed in sequence. This language feature, combined with ASP.NET's comma concatenation behavior, creates an opportunity for sophisticated bypasses.

When ASP.NET processes a query string like:

/?q=1'&q=alert(1)&q='2

It concatenates these values into:

1',alert(1),'2

When this gets inserted into the Javascript context above:

userInput = '1',alert(1),'2';

The resulting Javascript is syntactically valid and will execute the alert function. The comma operator in Javascript evaluates each expression from left to right and returns the value of the last expression. This pattern is widely used in Javascript minification and obfuscation.

## Breaking WAFs for fun and JS Injection

Since we were pretty deep into this rabbit hole already we decided it would be a good idea to test the most popular WAFs for this idea we just had. Obviously, we did not think that this could be some kind of holy grail universal WAF bypass, but our curiosity would kill us if we left this research topic without knowing exactly how good this technique was.

### Types of WAF Technologies

Modern Web Application Firewalls operate using two primary detection methodologies, each with distinct advantages and limitations in defending against sophisticated attacks.

Signature-Based WAFs were one of the main forms of defense in traditional web security. These systems maintain databases of known attack patterns and compare incoming requests against these signatures. When a match is detected, the WAF can log, alert, or block the request. The main advantage of signature-based detection lies in its precision. When an attack matches a known signature, false positives are typically low. Signatures may also be ranked by their confidence level, allowing for configurations that prefer lower false positive rates to stricter security. However, these systems struggle with novel attack vectors and require constant signature updates to remain effective.

Machine Learning-Based WAFs represent the next step in web application security. These systems analyze traffic patterns and user behavior to identify anomalous requests that may indicate attacks. Unlike signature-based systems, ML-powered WAFs can potentially detect 0-days and previously unknown attack vectors. This obviously comes at a cost as a low false positive rate may not be guaranteed and if not combined with a good pre-trained source of truth, may leave applications with low traffic levels susceptible to attacks.

### Why do WAFs struggle with Parameter Pollution

We came up with a couple of reasons as to why traditional WAFs face several challenges when attempting to detect parameter pollution-based attacks:

- WAFs typically analyze individual parameters. They may miss the relationship between multiple parameters that, when combined, form malicious code.
- Most WAFs lack a deep understanding of how different web frameworks handle parameter parsing. They may not simulate ASP.NET's specific comma concatenation behavior.
- Rule-based WAFs rely on known attack patterns. The parameter pollution technique creates payloads that don't match traditional XSS signatures while remaining functionally equivalent.
- When combining this technique with diverse obfuscation techniques, the actual malicious intent becomes difficult to detect through static analysis.

To detect these attacks, WAFs would need to implement framework specific parameter parsing logic and context aware Javascript analysis, capabilities that extend far beyond pattern matching. It is also worth noting that equipping a WAF with the necessary means to do this kind of analysis would be a performance nightmare, as WAFs are designed to introduce as little overhead as possible when proxying requests.

### WAF Configurations tested

Our evaluation included 17 different WAF configurations spanning major cloud providers and security vendors. All configurations represent diverse approaches to web security, from traditional rule-based to machine learning-based solutions.

|     |     |     |
| --- | --- | --- |
| **Vendor** | **Configuration** | **Rule Sets** |
| **AWS WAF - AWS Managed Rule Set** | Default | Admin protection, Amazon IP reputation list, Anonymous IP list, Core rule set, Known bad inputs, Linux operating system, PHP application, POSIX operating system, SQL database, Windows operating system, WordPress application |
| **AWS WAF - Cloudbric Rule Set** | Default | API Protection, OWASP Top 10 Rule Set |
| **AWS WAF - Cyber Security Cloud Rule Set** | Default | API Gateway/Serverless, HighSecurity OWASP Set |
| **AWS WAF - F5 Rule Set** | Default | API Security Rules, Web Exploits OWASP Rules, CVE |
| **AWS WAF - Fortinet Rule Set** | Default | API Security, OWASP Top 10 - The Complete Rule Set |
| **Google Cloud Armor** | Maximum sensitivity on all rules | sqli, xss, lfi, rfi, rce, methodenforcement, scannerdetection, protocolattack, php, sessionfixation, java, nodejs - v33-stable |
| **Azure WAF** | Default | Default Rule Set 2.1 |
| **FortiWeb** | Inline Standard Protection | Default |
| **FortiWeb** | Extended Standard Protection | Default |
| **Cloudflare WAF** | Default | Cloudflare Managed + OWASP Core |
| **open-appsec** | Medium+ Sensitivity | Default |
| **open-appsec** | High+ Sensitivity | Default |
| **open-appsec** | Only Critical Sensitivity | Default |
| **Akamai** | Default | Default |
| **F5 Big-IP Advanced WAF** | Signature staging disabled + Low accuracy signatures | Rapid Deployment Policy |
| **NGINX App Protect WAF** | Default | Default |
| **NGINX App Protect WAF** | Strict | Strict |

### Testing Methodology

We developed three payloads to evaluate each WAF susceptibility to parameter pollution-based Javascript injection attacks:

Payload 1 - Simple injection:

q=';alert(1),'

This baseline payload tests basic Javascript injection detection capabilities by very clearly attempting to break out of a string context and execute code in a single parameter.

Payload 2 - Parameter Pollution with Semicolon:

q=1'+1;let+asd=window&q=def='al'+'ert'+;asd\[def\](1&q=2);'

This payload introduces parameter pollution with some clever variable assignments and string concatenation to evade pattern matching.

Payload 3 - Parameter Pollution with Line Breaks:

q=1'%0aasd=window&q=def="al"+"ert"&q=asd\[def\](1)+'

This payload uses a new line instead of the semicolon to start a new Javascript expression. We specifically forced both payloads to work independently of the injection context as not all contexts may work with the comma operator so a new Javascript expression must be created.

Payload 4 - Our heuristic-based approach:

We also tested each WAF with the current capabilities of our engine, to infer whether our heuristic-based techniques can detect this type of XSS in assets protected by WAFs.

### Testing Results

The test results are shown in the table below (✅ = blocked, ❌ = bypass/undetected):

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **WAF** | **Payload 1** | **Payload 2** | **Payload 3** | **Ethiack Engine** |
| **AWS WAF - AWS Managed** | ❌ | ❌ | ❌ | ❌ |
| **AWS WAF - Cloudbric rule set** | ✅ | ❌ | ❌ | ❌ |
| **AWS WAF - Cyber Security Cloud rule set** | ❌ | ❌ | ❌ | ❌ |
| **AWS WAF - F5 rule set** | ❌ | ❌ | ❌ | ❌ |
| **AWS WAF - Fortinet rule set** | ✅ | ❌ | ❌ | ❌ |
| **Google Cloud Armor - Preconfigured ModSecurity rules** | ✅ | ✅ | ✅ | ❌ |
| **Azure WAF - Microsoft Default Rule Set 2.1** | ✅ | ✅ | ✅ | ❌ |
| **FortiWeb - Inline Standard Protection** | ✅ | ❌ | ❌ | ❌ |
| **FortiWeb - Inline Extended Protection** | ✅ | ✅ | ❌ | ❌ |
| **Cloudflare WAF - Managed and OWASP Core Rule Set** | ✅ | ❌ | ❌ | ❌ |
| **open-appsec - Medium+** | ✅ | ✅ | ✅ | ❌ |
| **open-appsec - High+** | ✅ | ✅ | ✅ | ❌ |
| **open-appsec - Critical** | ✅ | ✅ | ✅ | ❌ |
| **Akamai** | ✅ | ❌ | ❌ | ❌ |
| **F5 BIG-IP Advanced WAF - Rapid Deployment Policy** | ✅ | ❌ | ❌ | ❌ |
| **F5 NGINX App Protect WAF - Default** | ✅ | ✅ | ❌ | ❌ |
| **F5 NGINX App Protect WAF - Strict** | ✅ | ✅ | ❌ | ❌ |

The testing results revealed a couple of interesting insights about modern WAF capabilities:

Only 5 configurations successfully blocked 3 payloads:

- Google Cloud Armor with ModSecurity rules
- Azure WAF with Microsoft's Default Rule Set 2.1
- All 3 open-appsec configurations.

3 AWS WAF Rule Sets were bypassed by every payload tested:

- AWS Managed Rules
- Cyber Security Cloud rule set
- F5 rule set

The percentage of vulnerable WAFs increased as payload complexity increased. The simple payload (Payload 1) achieved only a 17.6% bypass rate, while the most complicated parameter pollution payload (Payload 3) bypassed 70.6% of tested configurations. However, our heuristic-based approach showed a 100% detection rate, effectively bypassing all WAF defenses.

The data reveals that traditional signature-based WAFs struggle with parameter pollution techniques, while more modern solutions incorporating machine learning demonstrate superior defensive capabilities but prove themselvesinsufficient (at least with low amounts of training data) in avoiding our proprietary heuristic-based detection mechanisms.

## Can Our Hackbot Do It Better?

Following our manual evaluation, our curiosity continued to get the best of us and we decided to deploy our completely autonomous hackbot against the WAF configurations that had successfully blocked all our manually crafted test payloads (Google Cloud Armor, Azure WAF and open-appsec). The goal was to discover whether the hackbot could find something that we had missed.

### Azure WAF

The hackbot found a bypass for the previously undefeated Azure WAF with Microsoft Default Rule Set 2.1. While our manually crafted payloads had been completely blocked, the hackbot discovered a surprisingly simple bypass that had escaped our payload brainstorming:

test\\\';alert(1);//

This payload leverages a subtle parsing discrepancy in how Azure WAF handles escaped characters compared to how Javascript processes them. The double backslash and single quote combination (\\\’) is interpreted differently by the WAF's pattern matching and the Javascript parser. While Javascript will escape the backslack that is escaping the quote, Azure WAF will interpret the backslack escaping the quote as an escaped quote.

![image (21)](https://blog.ethiack.com/hs-fs/hubfs/image%20(21).png?width=501&height=563&name=image%20(21).png)

### Google Cloud Armor

Unfortunately, the hackbot did not find a bypass for the very strict Google Cloud Armor configuration. However, during its struggles to find a payload that would effectively bypass the WAF, it did find some interesting applicational behaviors that we had missed during our analysis.

When exploring the application, it came to a conclusion that the parameter parsing made by the server was case insensitive and started using that technique to try and bypass the WAF in the following tests.

And how cool is that?!

![image (23)](https://blog.ethiack.com/hs-fs/hubfs/image%20(23).png?width=872&height=1884&name=image%20(23).png)

### open-appsec

The story was very different when we threw it against open-appsec. We went in expecting nothing but our hackbot proved us wrong in record time.  It only took 30 seconds to find a valid bypass for open-appsec in the Critical configuration. Absolutely mindblowing. Don’t get me wrong, the Azure WAF bypass did not take much more time, but this one takes the crown.

![image (25)](https://blog.ethiack.com/hs-fs/hubfs/image%20(25).png?width=875&height=493&name=image%20(25).png)

Since open-appsec relies on machine learning to make its decisions, we decided to see if our hackbot could adapt if the original payload got blocked. To do this, we generated enough traffic so that the _alert_ based payload started being blocked by the WAF, and we let the hackbot do its magic.

This time, almost instantly, it found a bypass using _confirm_ instead of _alert_.

![image (26)-1](https://blog.ethiack.com/hs-fs/hubfs/image%20(26)-1.png?width=880&height=428&name=image%20(26)-1.png)

We also tested in the Medium+ and High+ configurations and just as rapidly it managed to not only replicate the same results but also find additional payloads such as q='+new Function('a'+'lert(1)')()+'

Smart stuff for such a little guy!

These findings highlight one of the most important principles that we believe in:

> Automation Complements Manual Testing:
>
> While human expertise is crucial for developing new attack techniques, hackbots can aid in exploring variations that might be overlooked in manual testing. This is great because it means that us humans can focus on more creative vulnerabilities like we just did!

## Final Thoughts

### The Parameter Pollution Rabbit Hole

The most striking finding from our manual research is the effectiveness of parameter pollution techniques against traditional WAFs. With bypass success rates escalating from 17.6% for simple payloads to 70.6% for complex parameter pollution payloads, the data clearly demonstrates that WAFs relying on pattern matching struggle to defend against attacks that exploit fundamental differences in parsing between WAFs and web applications.

This vulnerability comes from one of the most fundamental security challenges: WAFs must make security decisions without fully simulating the application's parsing behavior. ASP.NET's comma concatenation behavior creates a differential that is difficult to detect through traditional signature analysis.

### The Machine Learning Superiority

The superior detection rate of machine learning-based WAFs suggests that behavioral detection offers significant advantages over rule-based approaches. These systems can identify malicious payloads even when they don't match known signatures, providing protection against novel attack vectors.

However, our hackbot proved that this model still has flaws. Even though we managed to confirm the adaptability of this type of WAF to malicious traffic (by generating benign traffic), our hackbot managed to circumvent the learning process and find an alternative bypass almost immediately.

### The Complexity Paradox

Perhaps our most disappointing discovery is that sophisticated attack techniques can coexist with surprisingly simple bypasses. While we developed complex parameter pollution payloads that defeated most WAFs, our Hackbot revealed that even seemingly robust products like Azure WAF and open-appsec could be bypassed using relatively straightforward payloads.

This finding highlighted a critical vulnerability in basic security strategies: organizations may invest in costly WAF technologies while remaining vulnerable to attacks that exploit basic implementation gaps or configuration oversights. This reminds us that WAFs must not be used as a fix for the root problems of insecure code.

### The Rise of Hackbots

Finally, this blog post also serves as a demonstration of the power of Hackbots.

We made it clear that our engine can be as stealthy as possible and detect this type of XSS without alerting any of the tested WAFs. On the other hand, we also leveraged the raw hacking power of our hackbot to reach even higher and perform a much more detailed and systematic evaluation of WAFs that were previously unbeaten by our research alone.

We’ll be discussing what’s next in hackbots and AI security at [HackAIcon.](https://hackaicon.ethiack.com/?utm_source=verifier_blog_post) Hope to see you around!

#### References

\[1\] [https://swisskyrepo.github.io/PayloadsAllTheThings/HTTP%20Parameter%20Pollution/#methodology](https://swisskyrepo.github.io/PayloadsAllTheThings/HTTP%20Parameter%20Pollution/#methodology)

\[2\] [https://www.intigriti.com/researchers/hackademy/http-parameter-pollution](https://www.intigriti.com/researchers/hackademy/http-parameter-pollution)

\[3\] [https://www.madlab.it/slides/BHEU2011/whitepaper-bhEU2011.pdf](https://www.madlab.it/slides/BHEU2011/whitepaper-bhEU2011.pdf)

Previous Post


###### [Don’t Fear The AI Reaper: Using LLMs to Hack Better and Faster](https://blog.ethiack.com/blog/dont-fear-the-ai-reaper-using-llms-to-hack-better-and-faster)

Next Post


###### [AI Pentesting Without the Noise: Hackbots and the Verifier](https://blog.ethiack.com/blog/ai-pentesting-without-the-noise-hackbots-and-the-verifier)

Twitter Widget Iframe

[Register now!](https://cta-eu1.hubspot.com/web-interactives/public/v1/track/click?encryptedPayload=AVxigLLZ2J0vtO%2BVKfDqAs%2FvU1x2P3qs6FGdEC%2FbqsUARjqhbPOorRCnk%2Bqs5frtH67r6jhBsk162bxuvev%2BmmvLb3V7%2BYc8efgGhWrVPrSSlaJpCofzx46qj4NWfVZZiJDP%2B4kmyfZQxEyJ%2FeZ6NzovPL%2FzRWwHXXButeUjbw%3D%3D&portalId=25953430&webInteractiveId=723735048388&webInteractiveContentId=262591731926&containerType=SLIDE_IN&pageUrl=https%3A%2F%2Fblog.ethiack.com%2Fblog%2Fbypassing-wafs-for-fun-and-js-injection-with-parameter-pollution)
