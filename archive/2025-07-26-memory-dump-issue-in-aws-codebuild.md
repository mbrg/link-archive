---
date: '2025-07-26'
description: AWS CodeBuild is vulnerable to memory dump exploitation, allowing unauthorized
  access to repository access tokens through an automated build process. This can
  enable threat actors to commit malicious code if the token has write permissions.
  The issue spans all regions and has been assigned CVE-2025-8217. AWS recommends
  disabling automatic builds for pull requests from untrusted contributors and suggests
  various webhook configuration adjustments to mitigate risks. Enhanced protections
  against memory dumps have been implemented. Customers should review permissions
  and rotate credentials for any exposed access tokens. Full details are available
  in AWS security bulletins.
link: https://aws.amazon.com/security/security-bulletins/aws-2025-016/
tags:
- CVE
- security vulnerability
- memory dump
- continuous integration
- AWS CodeBuild
title: Memory Dump Issue in AWS CodeBuild
---

## Select your cookie preferences

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies.

If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

AcceptDeclineCustomize

## Customize cookie preferences

We use cookies and similar tools (collectively, "cookies") for the following purposes.

### Essential

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

### Performance

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Allowed

### Functional

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Allowed

### Advertising

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Allowed

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the [AWS Cookie Notice](https://aws.amazon.com/legal/cookies/).

CancelSave preferences

## Your privacy choices

We and our advertising partners (“we”) may use information we collect from or about you to show you ads on other websites and online services. Under certain laws, this activity is referred to as “cross-context behavioral advertising” or “targeted advertising.”

To opt out of our use of cookies or similar technologies to engage in these activities, select “Opt out of cross-context behavioral ads” and “Save preferences” below. If you clear your browser cookies or visit this site from a different device or browser, you will need to make your selection again. For more information about cookies and how we use them, read our [Cookie Notice](https://aws.amazon.com/legal/cookies/).

Allow cross-context behavioral adsOpt out of cross-context behavioral ads

To opt out of the use of other identifiers, such as contact information, for these activities, fill out the form [here](https://pulse.aws/application/ZRPLWLL6?p=0).

For more information about how AWS handles your information, read the [AWS Privacy Notice](https://aws.amazon.com/privacy/).

CancelSave preferences

## Unable to save cookie preferences

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

Dismiss

 [Skip to main content](https://aws.amazon.com/security/security-bulletins/aws-2025-016/#aws-page-content-main)

## Memory Dump Issue in AWS CodeBuild

**Bulletin ID**: AWS-2025-016

**Scope**: AWS

**Content Type**: Important

**Release Date**: 2025/07/25 6:00 PM PDT

**Description**

[AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) is a fully managed on-demand continuous integration service that compiles source code, runs tests, and produces software packages that are ready to deploy.

Security researchers reported a CodeBuild issue that could be leveraged for unapproved code modification absent sufficient repository controls and credential scoping. The researchers demonstrated how a threat actor could submit a Pull Request (PR) that, if executed through an automated CodeBuild build process, could extract the source code repository (e.g. GitHub, BitBucket, or GitLab) access token through a memory dump within the CodeBuild build environment. If the access token has write permissions, the threat actor could commit malicious code to the repository. This issue is present in all regions for CodeBuild.

During our investigation, we identified this technique was leveraged by a threat actor who extracted the source code repository access token for the AWS Toolkit for Visual Studio Code and AWS SDK for .NET repositories. We have assigned [CVE-2025-8217](https://www.cve.org/CVERecord?id=CVE-2025-8217) for this, please refer to the [AWS Security Bulletin AWS-2025-015](https://aws.amazon.com/security/security-bulletins/AWS-2025-015/) for additional information.

Source code repository credentials are required in CodeBuild to access repository content, create webhooks for automated builds, and execute the build on your behalf. If a PR submitter obtains CodeBuild's repository credentials, they could gain elevated permissions beyond their normal access level. Depending on the permissions customers grant in CodeBuild, these credentials might allow elevated privileges like webhook creation, which CodeBuild requires to integrate with source code repositories and set up automated builds, or commit code to the repository.

To determine if this issue was leveraged by an untrusted contributor, we recommend reviewing git logs, e.g. GitHub logs, and look for anomalous activity of the credentials granted to CodeBuild.

We will update this bulletin if we have additional information to share.

**Resolution**

CodeBuild has included additional protections against memory dumps within container builds using unprivileged mode. However, because builds execute code committed by contributors in the build environment, they have access to anything the build environment has access to. Therefore, we strongly recommend customers do not use automatic PR builds from untrusted repository contributors. For public repositories that want to continue to support automatic builds of untrusted contributions, we advise using the self-hosted [GitHub Actions runners feature](https://docs.aws.amazon.com/codebuild/latest/userguide/action-runner-overview.html) in CodeBuild as it is not impacted by this issue.

To disable automatic builds of PR from untrusted contributors, take any of the following approaches:

1. Disable webhook builds by unchecking "Rebuild every time a code change is pushed to this repository" in the CodeBuild console, or
2. Set a webhook event filter to not allow automatic builds from pull request events, or
3. Set a webhook actor filter to allow pull requests builds from trusted users only

If customers use the automatic build feature on PRs for untrusted contributors, and the credentials or access token provided to the CodeBuild environment have write permissions, we recommend rotating those credentials. In general, we recommend reviewing write permissions and revoking them unless absolutely necessary.

**References**

[CVE-2025-8217](https://www.cve.org/CVERecord?id=CVE-2025-8217)

[AWS-2025-015](https://aws.amazon.com/security/security-bulletins/AWS-2025-015/)

**Acknowledgement**

We would like to thank the researchers from the Institute of Information Engineering, Chinese Academy of Sciences for collaborating on this issue through the coordinated vulnerability disclosure process.

Please email [aws-security@amazon.com](mailto:aws-security@amazon.com) with any security questions or concerns.

Get the gist with ExplainerWith Explainer, you can highlight any text to get an explanation generated with AWS generative AI. Learn new terms or product info—no searching required. To get started, turn on the **Explainer** toggle in the lower right.

Continue
