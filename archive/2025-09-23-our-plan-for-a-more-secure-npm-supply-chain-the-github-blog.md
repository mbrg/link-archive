---
date: '2025-09-23'
description: GitHub addresses recent npm supply chain vulnerabilities highlighted
  by the self-replicating Shai-Hulud worm attack, which exploited compromised maintainer
  accounts to disseminate malicious software. In response, GitHub has removed over
  500 harmful packages and initiated enhanced security measures. Key future actions
  include mandatory two-factor authentication (2FA) for local publishing, the introduction
  of granular access tokens with shorter lifespans, and the promotion of trusted publishing
  practices across package ecosystems. These measures aim to fortify the software
  supply chain, restoring community trust and mitigating risks posed by evolving threats.
link: https://github.blog/security/supply-chain-security/our-plan-for-a-more-secure-npm-supply-chain/
tags:
- open source
- npm
- trusted publishing
- security best practices
- supply chain security
title: Our plan for a more secure npm supply chain - The GitHub Blog
---

[Xavier René-Corail](https://github.blog/author/xcorail/ "Posts by Xavier René-Corail")· [@xcorail](https://github.com/xcorail)

September 22, 2025

\|
4 minutes

- Share:
- [Share on X](https://x.com/share?text=Our%20plan%20for%20a%20more%20secure%20npm%20supply%20chain&url=https%3A%2F%2Fgithub.blog%2Fsecurity%2Fsupply-chain-security%2Four-plan-for-a-more-secure-npm-supply-chain%2F)
- [Share on Facebook](https://www.facebook.com/sharer/sharer.php?t=Our%20plan%20for%20a%20more%20secure%20npm%20supply%20chain&u=https%3A%2F%2Fgithub.blog%2Fsecurity%2Fsupply-chain-security%2Four-plan-for-a-more-secure-npm-supply-chain%2F)
- [Share on LinkedIn](https://www.linkedin.com/shareArticle?title=Our%20plan%20for%20a%20more%20secure%20npm%20supply%20chain&url=https%3A%2F%2Fgithub.blog%2Fsecurity%2Fsupply-chain-security%2Four-plan-for-a-more-secure-npm-supply-chain%2F)

Open source software is the bedrock of the modern software industry. Its collaborative nature and vast ecosystem empower developers worldwide, driving efficiency and progress at an unprecedented scale. This scale also presents unique vulnerabilities that are continually tested and under attack by malicious actors, making the security of open source a critical concern for all.

Transparency is central to maintaining community trust. Today, we’re sharing details of recent npm registry incidents, the actions we took towards remediation, and how we’re continuing to invest in npm security.

## Recent attacks on the open source ecosystem

The software industry has faced a recent surge in damaging account takeovers on package registries, including npm. These ongoing attacks have allowed malicious actors to gain unauthorized access to maintainer accounts and subsequently distribute malicious software through well-known, trusted packages.

On September 14, 2025, we were notified of the [Shai-Hulud attack](https://socket.dev/blog/ongoing-supply-chain-attack-targets-crowdstrike-npm-packages), a self-replicating worm that infiltrated the npm ecosystem via compromised maintainer accounts by injecting malicious post-install scripts into popular JavaScript packages. By combining self-replication with the capability to steal multiple types of secrets (and not just npm tokens), this worm could have enabled an endless stream of attacks had it not been for timely action from GitHub and open source maintainers.

In direct response to this incident, GitHub has taken swift and decisive action including:

- Immediate removal of 500+ compromised packages from the npm registry to prevent further propagation of malicious software.
- npm blocking the upload of new packages containing the malware’s IoCs (Indicators of Compromise), cutting off the self-replicating pattern.

Such breaches erode trust in the open source ecosystem and pose a direct threat to the integrity and security of the entire software supply chain. They also highlight why raising the bar on authentication and secure publishing practices is essential to strengthening the npm ecosystem against future attacks.

## npm’s roadmap for hardening package publication

GitHub is committed to investigating these threats and mitigating the risks that they pose to the open source community. To address token abuse and self-replicating malware, we will be changing authentication and publishing options in the near future to only include:

1. Local publishing with [required two-factor authentication](https://docs.npmjs.com/requiring-2fa-for-package-publishing-and-settings-modification) (2FA).
2. [Granular tokens](https://docs.npmjs.com/about-access-tokens#about-granular-access-tokens) which will have a limited lifetime of seven days.
3. [Trusted publishing](https://repos.openssf.org/trusted-publishers-for-all-package-repositories).

To support these changes and further improve the security of the npm ecosystem, we will:

- Deprecate legacy classic tokens.
- Deprecate time-based one-time password (TOTP) 2FA, migrating users to FIDO-based 2FA.
- Limit granular tokens with publishing permissions to a shorter expiration.
- Set publishing access to disallow tokens by default, encouraging usage of trusted publishers or 2FA enforced local publishing.
- Remove the option to bypass 2FA for local package publishing.
- Expand eligible providers for trusted publishing.

We recognize that some of the security changes we are making may require updates to your workflows. We are going to roll these changes out gradually to ensure we minimize disruption while strengthening the security posture of npm. We’re committed to supporting you through this transition and will provide future updates with clear timelines, documentation, migration guides, and support channels.

## Strengthening the ecosystem with trusted publishing

[Trusted publishing](https://repos.openssf.org/trusted-publishers-for-all-package-repositories) is a recommended security capability by the OpenSSF Securing Software Repositories Working Group as it removes the need to securely manage an API token in the build system. It was pioneered by PyPI in [April 2023](https://blog.pypi.org/posts/2023-04-20-introducing-trusted-publishers/) as a way to get API tokens out of build pipelines. Since then, trusted publishing has been added to RubyGems ( [December 2023](https://blog.rubygems.org/2023/12/14/trusted-publishing.html)), crates.io ( [July 2025](https://blog.rust-lang.org/2025/07/11/crates-io-development-update-2025-07/)), npm (also [July 2025](https://github.blog/changelog/2025-07-31-npm-trusted-publishing-with-oidc-is-generally-available/)), and most recently NuGet ( [September 2025](https://learn.microsoft.com/en-us/nuget/nuget-org/trusted-publishing)), as well as other package repositories.

When npm released support for trusted publishing, it was our intention to let adoption of this new feature grow organically. However, attackers have shown us that they are not waiting. We strongly encourage projects to adopt trusted publishing as soon as possible, for all supported package managers.

## Actions that npm maintainers can take today

These efforts, from GitHub and the broader software community, underscore our global commitment to fortifying the security of the software supply chain. The security of the ecosystem is a shared responsibility, and we’re grateful for the vigilance and collaboration of the open source community.

**Here are the actions npm maintainers can take now:**

- Use npm [trusted publishing](https://docs.npmjs.com/trusted-publishers) instead of tokens.
- Strengthen [publishing settings](https://docs.npmjs.com/requiring-2fa-for-package-publishing-and-settings-modification) on accounts, orgs, and packages to require 2FA for any writes and publishing actions.
- When [configuring two-factor authentication](https://docs.npmjs.com/configuring-two-factor-authentication), use WebAuthn instead of TOTP.

True resilience requires the active participation and vigilance of everyone in the software industry. By adopting robust security practices, leveraging available tools, and contributing to these collective efforts, we can collectively build a more secure and trustworthy open source ecosystem for all.

* * *

## Tags:

- [GitHub Security Lab](https://github.blog/tag/github-security-lab/)
- [npm](https://github.blog/tag/npm/)
- [supply chain security](https://github.blog/tag/supply-chain-security/)

## Written by

![Xavier René-Corail](https://avatars.githubusercontent.com/u/7395402?v=4&s=200)

Sr. Dir, Security Research. Open Source Security at GitHub. I lead the GitHub Security Lab, empowering open source maintainers and developers to ship secure software.

## Related posts

![](https://github.blog/wp-content/uploads/2025/08/github-generic-wallpaper-pink.png?resize=400%2C212)

[Application security](https://github.blog/security/application-security/)

### [Safeguarding VS Code against prompt injections](https://github.blog/security/vulnerability-research/safeguarding-vs-code-against-prompt-injections/)

When a chat conversation is poisoned by indirect prompt injection, it can result in the exposure of GitHub tokens, confidential files, or even the execution of arbitrary code without the user’s explicit consent. In this blog post, we’ll explain which VS Code features may reduce these risks.

![](https://github.blog/wp-content/uploads/2025/04/wallpaper_github_generic_2.png?resize=400%2C212)

[Security](https://github.blog/security/)

### [How to catch GitHub Actions workflow injections before attackers do](https://github.blog/security/vulnerability-research/how-to-catch-github-actions-workflow-injections-before-attackers-do/)

Strengthen your repositories against actions workflow injections — one of the most common vulnerabilities.

![](https://github.blog/wp-content/uploads/2025/03/github_logo_invertocat_dark_3.png?resize=400%2C212)

[Application security](https://github.blog/security/application-security/)

### [Modeling CORS frameworks with CodeQL to find security vulnerabilities](https://github.blog/security/application-security/modeling-cors-frameworks-with-codeql-to-find-security-vulnerabilities/)

Discover how to increase the coverage of your CodeQL CORS security by modeling developer headers and frameworks.

## We do newsletters, too

Discover tips, technical guides, and best practices in our biweekly newsletter just for devs.

Your email address

\*Your email address

Subscribe

Yes please, I’d like GitHub and affiliates to use my information for personalized communications, targeted advertising and campaign effectiveness. See the [GitHub Privacy Statement](https://github.com/site/privacy) for more details.

Subscribe
