---
date: '2025-07-29'
description: AWS recently faced a supply chain security breach where a hacker exploited
  a vulnerability in AWS CodeBuild (CVE-2025-8217) to submit a pull request that included
  malicious code designed to delete customer data. Although it failed to execute due
  to an error, it highlights a critical gap in AWS's software delivery processes.
  Security experts emphasize the need for robust CI/CD safeguards, including strict
  access controls and short-lived credentials, to prevent similar incidents. The incident
  raises significant questions about AWS's vulnerability management and the effectiveness
  of their internal oversight mechanisms regarding third-party code integration.
link: https://www.thestack.technology/five-questions-for-aws-after-a-troubling-supply-chain-breach/
tags:
- CVE-2025-8217
- Malicious Code Injection
- Supply Chain Attack
- AWS Security
- CI/CD Security
title: Five questions for AWS after a troubling supply chain breach
---

Content Paint

AWS faces tough questions after a hacker breached its software build process and published malicious code that hit developer endpoints.

Security researchers say Amazon’s customers deserve a full post-mortem after the troubling software supply chain incident – warning that the sophisticated attacker may have shipped more malicous code unnoticed.

In an attack covered by The Stack [here](https://www.thestack.technology/aws-zero-day-exploited-to-access-codebase-for-its-ai-assistant/), first reported by 404 Media [here](https://www.404media.co/hacker-plants-computer-wiping-commands-in-amazons-ai-coding-agent/?ref=thestack.technology), and acknowledged by AWS [here](https://aws.amazon.com/security/security-bulletins/AWS-2025-015/?ref=thestack.technology), a threat actor successfully injected malicious “wiper” code into an official extension for AWS’s Q AI assistant.

It failed to execute, due to a (likely intentional) error, but none-the-less the faulty prompt [could be seen executing](https://bsky.app/profile/quinnypig.com/post/3luogum3g6s2i?ref=thestack.technology) on customer endpoints.

Here’s AWS expert Corey Quinn’s pithy take on what happened:

> “A hacker submitted a PR \[pull request\]. It got merged. It told Amazon Q to nuke your computer and cloud infra. Amazon shipped it. Mistakes happen, and cloud security is hard. But this is very far from ‘oops, we fat-fingered a command’—this is ‘someone intentionally slipped a live grenade into prod and AWS gave it version release notes.’

The hyperscaler later confirmed that the attacker exploited a vulnerability in its software build and delivery service AWS CodeBuild to do this.

![](https://www.thestack.technology/content/images/2025/07/1753754248433.jpeg)

The vulnerability, [CVE-2025-8217](https://www.cve.org/CVERecord?id=CVE-2025-8217&ref=thestack.technology), was reported to AWS by a team at the Institute of Information Engineering, Chinese Academy of Sciences.

(Notably, as has been [well documented](https://www.atlanticcouncil.org/in-depth-research-reports/report/sleight-of-hand-how-china-weaponizes-software-vulnerability/?ref=thestack.technology), in China security researchers must report any software vulnerabilities they find to the Ministry of Industry and Information Technology within 48 hours of discovery. China, [like the UK](https://www.gchq.gov.uk/information/equities-process?ref=thestack.technology) or any other country, then needs to make tough choices about whether to disclose or exploit such vulnerabilities for its national interest.)

Triaging this vulnerability disclosure, AWS identified exploitation by an ( [apparently Turkish-speaking](https://www.mbgsec.com/posts/2025-07-24-constructing-a-timeline-for-amazon-q-prompt-infection/?ref=thestack.technology)) attacker who used the security flaw to gain access to the “source code repository access token for the AWS Toolkit for Visual Studio Code and AWS SDK for .NET repositories” AWS [confirmed](https://aws.amazon.com/security/security-bulletins/aws-2025-016/?ref=thestack.technology).

Per AWS’s [advisory](https://aws.amazon.com/security/security-bulletins/aws-2025-016/?ref=thestack.technology), the vulnerability let an attacker:

> "Submit a Pull Request (PR) that, if executed through an automated CodeBuild build process, could extract the source code repository (e.g. GitHub, BitBucket, or GitLab) access token through a memory dump within the CodeBuild build environment. If the access token has write permissions \[which AWS’s did\], the threat actor could commit malicious code to the repository@

It appears that multiple threat actors knew of the AWS CodeBuild bug – exploitation of which involves submitting a benign-looking PR, adding a malicious commit, and then quickly removing it after the automated build runs; using simple ways of hiding tracks in Git-based workflows.

(The approach, in essence, exploits the gap between automated systems and human reviews to steal secrets, like API keys for example, without that code ever being seen by a human or merged into the final product, and uses a Git command called force-push that rewrites the history of the attacker’s branch on the server, completely erasing the malicious commit.)

AWS appears to be actively removing public evidence of the incident; deleting pull requests (PRs) and other GitHub activity by the attacker.

## AWS security incident: Five big questions

Michael Bargury, co-founder of AI agency security firm [Zenity](https://zenity.io/?ref=thestack.technology) noted to The Stack: “We still haven't seen the commit that actually got that token out…

He added: “\[Access to\] AWS Toolkit for VSCode means control over Amazon Q, AWS IDE Extension and AWS Toolkit. Per my research this issue was actually in effect well beyond the two repos AWS mentioned. They probably didn't find indicators of compromise elsewhere,” said Bargury.

“But I am seeing users that are doing reconnaissance activity…

“The key evidence we are missing are those malicious PRs. We know that an attacker exploited the vulnerable CodeBuild configuration. Where are those commits with the exploit code? Who interacted with these PRs?

“This is a sophisticated supply chain attack that compromised a whole host of AWS developer tools. The risk is huge – the attacker could have pushed a backdoor into every developer machine that uses these AWS tools. They did so in effect with Amazon Q. The story was published by 404 Media which begs the question: are there other exploitations that were silently fixed? Or ones we aren't aware of? We need more clarity.”

Despite the attacker's public ranting on various forums and the arguably clumsy "wiper" prompt, they were sophisticated, says Bargury.

> "You gain write access to aws toolkit, ide extension and amazonq and you use it to create a scene? this was a sophisticated attacker. they separated the downloader and payload commits. the malicious prompt never had to make it to master directory.

> "they observed normal behavior, waited for a Sunday, used aws-toolkit-automation to avoid suspicion, pushed to the right branch at the right time. they identified an opportunity to take over a .bk file created by someone else they impersonated the metadata of a benign commit they took the time to analyze the build scripts and find the right way to inject code without anyone noticing" – [https://x.com/mbrg0](https://x.com/mbrg0?ref=thestack.technology)

Corey Quinn earlier noted: “Amazon confidently claims that no customer resources were affected. But here’s the thing: The injected prompt was designed to delete things quietly and log the destruction to a local file—/tmp/CLEANER.LOG. That’s not telemetry. That’s not reporting. That’s a digital burn book that lives on the same system it’s erasing.

“So unless Amazon deployed agents to comb through the temp directories of every system running the compromised version during the roughly two days this extension was the default—and let’s be real, they didn’t, and couldn’t since that’s customer-side of the shared responsibility model—there’s no way they can confidently say nothing happened.”

Quinn’s key takeaway? “Treat Your AI Assistant Like It’s a Fork Bomb With a Chat Interface. Because it is. If your AI tool can execute code, access credentials, and talk to cloud services, congratulations—you’ve built a security vulnerability with autocomplete,” he added on his [blog](https://www.lastweekinaws.com/blog/amazon-q-now-with-helpful-ai-powered-self-destruct-capabilities/?ref=thestack.technology).

To Bargury, meanwhile, five key questions are unanswered by AW:

“1\. When did the attacker compromise the VSCode Toolkit and SDK for .NET GitHub tokens? Share the PRs.

“2\. What permissions did that token have? Was it scoped to aws-toolkit-vscode only, or did it have full access across the AWS GitHub org?

“3\. How long were AWS repositories vulnerable to the CodeBuild vulnerability? Which repositories were vulnerable?

“4\. You engaged GitHub to delete issues from your repositories. What else did you ask them delete?

“5\. How did you find the exploitation in (1)? Share your queries to enable others to do the same”.

To Datadog’s Nick Frichette, “if there is anything to learn from the Q Developer incident it’s that you need to review your CI/CD pipelines for attack vectors. Who can submit PRs, what automation runs on them, how are you securing identities tied to them, etc.” (Vulnerabilities like CodeBuild’s [CVE-2025-8217](https://www.cve.org/CVERecord?id=CVE-2025-8217&ref=thestack.technology), needless to say, do not help here…)

Matt Moore, CTO and Co-Founder at Chainguard said: “This was a credential leak that was used to launch a supply chain attack.

“It’s a pattern that is becoming all too common, and another sobering reminder of how vulnerable the software supply chain can be….

“AI wasn’t the problem. It was the bait. The real issue lies in the brittle scaffolding supporting that tooling: unmanaged credentials, insufficient isolation, and a lack of layered defenses. This is why short-lived credentials, like those enabled via [Octo STS](https://github.com/apps/octo-sts?ref=thestack.technology), are important.

“Long-lived, static tokens are liabilities waiting to be discovered, leaked and misused… Had there been robust branch protections, enforced signed commits, or credential federation in place, this attack might never have been possible. This is why you must treat your build systems like production systems. Treating them as anything less introduces a single point of compromise that can compromise the entire software lifecycle.”

## Sign up for The Stack

Interviews, insight, intelligence, and exclusive events for digital leaders.

Subscribe

Email sent! Check your inbox to complete your signup.


No spam. Unsubscribe anytime.

[Share on Facebook](https://www.facebook.com/sharer.php?u=https://www.thestack.technology/five-questions-for-aws-after-a-troubling-supply-chain-breach/)[Share on Twitter](https://twitter.com/intent/tweet?url=https://www.thestack.technology/five-questions-for-aws-after-a-troubling-supply-chain-breach/&text=Five%20questions%20for%20AWS%20after%20a%20troubling%20supply%20chain%20breach)[Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https://www.thestack.technology/five-questions-for-aws-after-a-troubling-supply-chain-breach/&title=Five%20questions%20for%20AWS%20after%20a%20troubling%20supply%20chain%20breach)

The link has been copied!

### Search the site

X

Your link has expired. Please request a new one.

Your link has expired. Please request a new one.

Your link has expired. Please request a new one.

Great! You've successfully signed up.

Great! You've successfully signed up.

Welcome back! You've successfully signed in.

Success! You now have access to additional content.

Subscribe
