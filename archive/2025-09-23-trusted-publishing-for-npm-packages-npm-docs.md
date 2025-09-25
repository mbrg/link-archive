---
date: '2025-09-23'
description: npm introduces Trusted Publishing, utilizing OpenID Connect (OIDC) for
  secure CI/CD workflows without long-lived tokens. This standard, endorsed by Open
  Source Security Foundation, improves security by using short-lived, cryptographically-signed
  tokens tailored to specific workflows—reducing risks associated with token management.
  Supported initially by GitHub Actions and GitLab CI/CD, this mechanism supports
  streamlined package publishing and provenance generation, enhancing authenticity
  verification. Best practices recommend restricting traditional token access for
  greater security. Future enhancements may include support for self-hosted runners
  and broader CI/CD provider integration.
link: https://docs.npmjs.com/trusted-publishers
tags:
- OIDC
- security best practices
- trusted publishing
- CI/CD
- npm
title: Trusted publishing for npm packages ◆ npm Docs
---

[Skip to search](https://docs.npmjs.com/trusted-publishers#search-box-input) [Skip to content](https://docs.npmjs.com/trusted-publishers#skip-to-content)

### Site navigation

# Trusted publishing for npm packages

Table of contents

Trusted publishing allows you to publish npm packages directly from your CI/CD workflows using [OpenID Connect (OIDC)](https://openid.net/developers/how-connect-works/) authentication, eliminating the need for long-lived npm tokens. This feature implements the [trusted publishers industry standard](https://repos.openssf.org/trusted-publishers-for-all-package-repositories) specified by the Open Source Security Foundation (OpenSSF), joining a growing ecosystem including [PyPI](https://docs.pypi.org/trusted-publishers/), [RubyGems](https://guides.rubygems.org/trusted-publishing/), and other major package registries in offering this security enhancement.

**Note:** Trusted publishing requires [npm CLI](https://docs.npmjs.com/cli/v11) version 11.5.1 or later.

## [How trusted publishing works](https://docs.npmjs.com/trusted-publishers\#how-trusted-publishing-works)

Trusted publishing creates a trust relationship between npm and your CI/CD provider using OIDC. When you configure a trusted publisher for your package, npm will accept publishes from the specific workflow you've authorized, in addition to traditional authentication methods like npm tokens and manual publishes. The npm CLI automatically detects OIDC environments and uses them for authentication before falling back to traditional tokens.

This approach eliminates the security risks associated with long-lived write tokens, which can be compromised, accidentally exposed in logs, or require manual rotation. Instead, each publish uses short-lived, cryptographically-signed tokens that are specific to your workflow and cannot be extracted or reused.

## [Supported CI/CD providers](https://docs.npmjs.com/trusted-publishers\#supported-cicd-providers)

Trusted publishing currently supports:

- [GitHub Actions](https://github.com/features/actions) (GitHub-hosted runners)
- [GitLab CI/CD Pipelines](https://docs.gitlab.com/ci/pipelines/) (GitLab.com shared runners)

Self-hosted runners are not currently supported but are planned for future releases.

## [Configuring trusted publishing](https://docs.npmjs.com/trusted-publishers\#configuring-trusted-publishing)

## [Step 1: Add a trusted publisher on npmjs.com](https://docs.npmjs.com/trusted-publishers\#step-1-add-a-trusted-publisher-on-npmjscom)

Navigate to your package settings on [npmjs.com](https://www.npmjs.com/) and find the " **Trusted Publisher**" section. Under " **Select your publisher**", choose your CI/CD provider by clicking either the GitHub Actions or GitLab CI/CD button.

![Screenshot showing the Trusted Publisher section with Select your publisher label and provider buttons](https://docs.npmjs.com/packages-and-modules/securing-your-code/trusted-publisher.png)

### [For GitHub Actions](https://docs.npmjs.com/trusted-publishers\#for-github-actions)

Configure the following fields:

- **Organization or user** (required): Your GitHub username or organization name
- **Repository** (required): Your repository name
- **Workflow filename** (required): The filename of your workflow (e.g., `publish.yml`)
  - Enter only the filename, not the full path
  - Must include the `.yml` or `.yaml` extension
  - The workflow file must exist in `.github/workflows/` in your repository
- **Environment name** (optional): If using [GitHub environments](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment) for deployment protection

![Screenshot of GitHub Actions trusted publisher configuration form](https://docs.npmjs.com/packages-and-modules/securing-your-code/trusted-publisher-github-actions.png)

### [For GitLab CI/CD](https://docs.npmjs.com/trusted-publishers\#for-gitlab-cicd)

Configure the following fields:

- **Namespace** (required): Your GitLab username or group name
- **Project name** (required): Your project name
- **Top-level CI file path** (required): The path to your CI file (e.g., `.gitlab-ci.yml`)
  - Must include the `.yml` extension
- **Environment name** (optional): If using [GitLab environments](https://docs.gitlab.com/ee/ci/environments/)

![Screenshot of GitLab CI/CD trusted publisher configuration form](https://docs.npmjs.com/packages-and-modules/securing-your-code/trusted-publisher-gitlab.png)

**Note:** Each package can only have one trusted publisher configured at a time.

## [Step 2: Configure your CI/CD workflow](https://docs.npmjs.com/trusted-publishers\#step-2-configure-your-cicd-workflow)

### [GitHub Actions configuration](https://docs.npmjs.com/trusted-publishers\#github-actions-configuration)

Add the required OIDC permissions to your workflow. Here's a complete example:

```

name: Publish Package

on:
  push:
    tags:
      - 'v*'

permissions:
  id-token: write  # Required for OIDC
  contents: read

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          registry-url: 'https://registry.npmjs.org'

      # Ensure npm 11.5.1 or later is installed
      - name: Update npm
        run: npm install -g npm@latest
      - run: npm ci
      - run: npm run build --if-present
      - run: npm test
      - run: npm publish
```

The critical requirement is the `id-token: write` permission, which allows GitHub Actions to generate OIDC tokens. Learn more in [GitHub's OIDC documentation](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect).

### [GitLab CI/CD configuration](https://docs.npmjs.com/trusted-publishers\#gitlab-cicd-configuration)

Configure the OIDC ID token in your pipeline:

```

stages:
  - test
  - build
  - publish

variables:
  NODE_VERSION: '20'

test:
  stage: test
  image: node:${NODE_VERSION}
  script:
    - npm ci
    - npm test

publish:
  stage: publish
  image: node:${NODE_VERSION}
  id_tokens:
    NPM_ID_TOKEN:
      aud: "npm:registry.npmjs.org"
  script:
    # Ensure npm 11.5.1 or later is installed
    - npm install -g npm@latest
    - npm ci
    - npm run build --if-present
    - npm publish
  only:
    - tags
```

The `id_tokens` configuration tells GitLab to generate an OIDC token for npm. Learn more in [GitLab's OIDC documentation](https://docs.gitlab.com/ee/ci/cloud_services/).

## [Managing trusted publisher configurations](https://docs.npmjs.com/trusted-publishers\#managing-trusted-publisher-configurations)

You can modify or remove your trusted publisher configuration at any time through your package settings on [npmjs.com](https://npmjs.com/). Each package can only have one trusted publisher connection at a time, but this connection can be edited or deleted as needed. To change providers (for example, switching from GitHub Actions to GitLab CI/CD), simply edit your existing configuration and select the new provider. The change takes effect immediately for future publishes. To remove trusted publishing entirely and return to token-based authentication, delete the trusted publisher configuration from your package settings.

## [Recommended: Restrict token access when using trusted publishers](https://docs.npmjs.com/trusted-publishers\#recommended-restrict-token-access-when-using-trusted-publishers)

Once you've configured trusted publishers for your package, we strongly recommend restricting traditional token-based publishing access for enhanced security.

## [How to configure maximum security](https://docs.npmjs.com/trusted-publishers\#how-to-configure-maximum-security)

1. After enabling trusted publishers, navigate to your package's **Settings** → **Publishing access**
2. Select **"Require two-factor authentication and disallow tokens"**
3. Save your changes by clicking on **Update Package Settings**

## [Why this matters](https://docs.npmjs.com/trusted-publishers\#why-this-matters)

Trusted publishers use short-lived, scoped credentials that are generated on-demand during your CI/CD workflow, eliminating the need for long-lived tokens. By restricting traditional token access while using trusted publishers, you reduce potential security risks associated with credential management.

**Note:** The "disallow tokens" setting only affects traditional token authentication. Your trusted publishers will continue to work normally, as they use OIDC tokens.

## [Migration tip](https://docs.npmjs.com/trusted-publishers\#migration-tip)

If you're transitioning from token-based publishing:

1. Set up trusted publishers first and verify they work
2. Then restrict token access as described above
3. [Revoke any existing automation tokens](https://docs.npmjs.com/revoking-access-tokens) that are no longer needed

This ensures a smooth transition without disrupting your release process.

## [Automatic provenance generation](https://docs.npmjs.com/trusted-publishers\#automatic-provenance-generation)

When you publish using trusted publishing, npm automatically generates and publishes [provenance attestations](https://docs.npmjs.com/generating-provenance-statements) for your package. This happens by default—you don't need to add the `--provenance` flag to your publish command.

![Screenshot showing provenance badge/information on a package page](https://docs.npmjs.com/packages-and-modules/securing-your-code/trusted-publisher-provenance.png)

Provenance provides cryptographic proof of where and how your package was built, allowing users to verify its authenticity. This automatic generation only applies when all of these conditions are met:

- Publishing via trusted publishing (OIDC)
- Publishing from a public repository
- Publishing a public package

**Note:** Provenance generation is [not supported for private repositories](https://github.blog/changelog/2023-07-25-publishing-with-npm-provenance-from-private-source-repositories-is-no-longer-supported/), even when publishing public packages.

## [Disabling provenance generation](https://docs.npmjs.com/trusted-publishers\#disabling-provenance-generation)

While we strongly recommend keeping provenance enabled, you can disable it if needed. Set the `provenance` option to `false` in any of these ways:

**Using environment variable:**

```

NPM_CONFIG_PROVENANCE=false npm publish
```

**In your `.npmrc` file:**

```

provenance=false
```

**In your `package.json`:**

```

{
  "publishConfig": {
    "provenance": false
  }
}
```

## [Security best practices](https://docs.npmjs.com/trusted-publishers\#security-best-practices)

## [Prefer trusted publishing over tokens](https://docs.npmjs.com/trusted-publishers\#prefer-trusted-publishing-over-tokens)

When trusted publishing is available for your workflow, always prefer it over long-lived tokens. Traditional npm tokens pose several security risks:

- They can be accidentally exposed in CI logs or configuration files
- They require manual rotation and management
- If compromised, they provide persistent access until revoked
- They often have broader permissions than necessary

Trusted publishing eliminates these risks by using short-lived, workflow-specific credentials that are automatically managed and cannot be extracted.

## [Handling private dependencies](https://docs.npmjs.com/trusted-publishers\#handling-private-dependencies)

While trusted publishing handles the publish operation, you may still need authentication for installing private npm dependencies. For this scenario, we recommend:

```

# GitHub Actions example
- uses: actions/setup-node@v4
  with:
    node-version: '20'
    registry-url: 'https://registry.npmjs.org'

# Ensure npm 11.5.1 or later for trusted publishing
- run: npm install -g npm@latest

# Use a read-only token for installing dependencies
- run: npm ci
  env:
    NODE_AUTH_TOKEN: ${{ secrets.NPM_READ_TOKEN }}

# Publish uses OIDC - no token needed
- run: npm publish
```

Always use [read-only granular access tokens](https://docs.npmjs.com/creating-and-viewing-access-tokens#creating-granular-access-tokens-on-the-website) for installing dependencies. This limits potential damage if the token is ever compromised.

## [Additional security measures](https://docs.npmjs.com/trusted-publishers\#additional-security-measures)

Consider implementing these additional security practices:

- Use [deployment environments](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment) to add approval requirements
- Enable [tag protection rules](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/configuring-tag-protection-rules) to control who can create release tags
- Regularly audit your trusted publisher configurations
- Remove any unused publish tokens from your npm account

## [Troubleshooting](https://docs.npmjs.com/trusted-publishers\#troubleshooting)

If you encounter an "Unable to authenticate" error when publishing, first verify that the workflow filename matches exactly what you configured on [npmjs.com](https://npmjs.com/), including the `.yml` extension. The filename is case-sensitive and must be exact. Also ensure you're using GitHub-hosted runners or GitLab.com shared runners, as self-hosted runners are not currently supported. For GitHub Actions specifically, check that the `id-token: write` permission is set in your workflow.

**Note:** npm does not verify your trusted publisher configuration when you save it. Double-check that your repository, workflow filename, and other details are correct, as errors will only appear when you attempt to publish.

If your package has private dependencies and `npm install` or `npm ci` is failing with authentication errors, remember that trusted publishing only applies to the `npm publish` command. You'll still need to provide a read-only token for installing private packages as shown in the examples above.

For packages in private repositories, provenance will not be generated even though you're using trusted publishing. This is a [known limitation](https://github.blog/changelog/2023-07-25-publishing-with-npm-provenance-from-private-source-repositories-is-no-longer-supported/) that applies regardless of whether your package itself is public or private.

Some GitHub Actions workflows use `workflow_call` to invoke other workflows that run `npm publish`, or use `workflow_dispatch` for manual publishing. When this happens, validation checks the calling workflow's name instead of the workflow that actually contains the publish command, which can cause configuration mismatches.

## [Limitations and future improvements](https://docs.npmjs.com/trusted-publishers\#limitations-and-future-improvements)

Trusted publishing currently supports only cloud-hosted runners. Support for self-hosted runners is intended for a future release. Each package can only have one trusted publisher configured at a time, though you can update this configuration as needed.

OIDC authentication is currently limited to the publish operation. Other npm commands such as `install`, `view`, or `access` still require traditional authentication methods. The `npm whoami` command will not reflect OIDC authentication status since the authentication occurs only during the publish operation.

We intend to expand trusted publishing support to additional CI/CD providers and enhance the feature based on community feedback.

## [Learn more](https://docs.npmjs.com/trusted-publishers\#learn-more)

- [About npm provenance](https://docs.npmjs.com/generating-provenance-statements)
- [OpenSSF Trusted Publishers specification](https://repos.openssf.org/trusted-publishers-for-all-package-repositories)
- [GitHub Actions OIDC documentation](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect)
- [GitLab CI/CD OIDC documentation](https://docs.gitlab.com/ee/ci/cloud_services/)
- [API documentation for exchanging OIDC ID token for npm registry token](https://api-docs.npmjs.com/#tag/registry.npmjs.org/operation/exchangeOidcToken)

[Edit this page on GitHub](https://github.com/npm/documentation/edit/main/content/packages-and-modules/securing-your-code/trusted-publishers.mdx)

4contributors [![reggi](https://github.com/reggi.png?size=40)](https://github.com/reggi) reggi [![leobalter](https://github.com/leobalter.png?size=40)](https://github.com/leobalter) leobalter [![jrvidal](https://github.com/jrvidal.png?size=40)](https://github.com/jrvidal) jrvidal [![generalmimon](https://github.com/generalmimon.png?size=40)](https://github.com/generalmimon) generalmimon

Last edited by [reggi](https://github.com/reggi) on [September 22, 2025](https://github.com/npm/documentation/commit/1ccdca298819e04c51fc0ea1b356ede8dff769db)

## Table of contents
