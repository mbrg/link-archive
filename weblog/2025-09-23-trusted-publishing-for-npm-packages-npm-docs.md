---
date: '2025-09-25'
description: "npm introduces Trusted Publishing, utilizing OpenID Connect (OIDC) for\
  \ secure CI/CD workflows without long-lived tokens. This standard, endorsed by Open\
  \ Source Security Foundation, improves security by using short-lived, cryptographically-signed\
  \ tokens tailored to specific workflows\u2014reducing risks associated with token\
  \ management. Supported initially by GitHub Actions and GitLab CI/CD, this mechanism\
  \ supports streamlined package publishing and provenance generation, enhancing authenticity\
  \ verification. Best practices recommend restricting traditional token access for\
  \ greater security. Future enhancements may include support for self-hosted runners\
  \ and broader CI/CD provider integration."
link: /archive/2025-09-23-trusted-publishing-for-npm-packages-npm-docs
tags:
- OIDC
- security best practices
- trusted publishing
- CI/CD
- npm
- weblog
title: "Trusted publishing for npm packages \u25C6 npm Docs"
type: weblog
---

Managed identities for artifact publication is great. Let's just make sure it doesn't come at the cost of traceability.

---

> Trusted publishing allows you to publish npm packages directly from your CI/CD workflows using [OpenID Connect (OIDC)](https://openid.net/developers/how-connect-works/) authentication, eliminating the need for long-lived npm tokens. This feature implements the [trusted publishers industry standard](https://repos.openssf.org/trusted-publishers-for-all-package-repositories) specified by the Open Source Security Foundation (OpenSSF), joining a growing ecosystem including [PyPI](https://docs.pypi.org/trusted-publishers/), [RubyGems](https://guides.rubygems.org/trusted-publishing/), and other major package registries in offering this security enhancement.

Like machine identities and SPIFFEE in the cloud. Nice!

---

> - [GitHub Actions](https://github.com/features/actions) (GitHub-hosted runners) - [GitLab CI/CD Pipelines](https://docs.gitlab.com/ci/pipelines/) (GitLab.com shared runners)

The benefits are obvious. But are we losing control? All these "managed identities" usually fail to provide the same level of logging and traceability we expect when we manage our own identities.

