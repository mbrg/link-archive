---
date: '2025-07-26'
description: The analysis of the Laundry Bear APT, attributed to Russian state-sponsored
  actors, reveals extensive infrastructure surrounding spear phishing and domain typosquatting
  tactics targeting NATO and NGOs. Key takeaways include the identification of multiple
  lookalike domains and their registrations—often using privacy-protecting email services.
  Methodologies employed in Validin, like DNS history searches and body hash pivoting,
  uncovered connections to an array of suspicious domains, indicating a coordinated
  effort in cyber espionage. This underscores the necessity for enhanced threat detection
  and domain monitoring in proactive cybersecurity strategies.
link: https://www.validin.com/blog/laundry_bear_infrastructure_analysis/
tags:
- threat intelligence
- APT
- domain analysis
- spear phishing
- cybersecurity
title: 'Hunting Laundry Bear: Infrastructure Analysis Guide and Findings ◆ Validin'
---

# Hunting Laundry Bear: Infrastructure Analysis Guide and Findings

![Hunting Laundry Bear: Infrastructure Analysis Guide and Findings](https://www.validin.com/images/laundry_bear_infrastructure_analysis/laundry_bear.webp)



By: Kenneth Kinion




2025-07-25


general

#### Table of Contents

- [Malicious Sender Domain History](https://www.validin.com/blog/laundry_bear_infrastructure_analysis/#malicious_sender_domain_history)
- [Initial Findings](https://www.validin.com/blog/laundry_bear_infrastructure_analysis/#summary_of_initial_findings)
- [Finding Lookalike Domains](https://www.validin.com/blog/laundry_bear_infrastructure_analysis/#finding_additional_lookalike_domains)
- [Spear Phishing Domain History](https://www.validin.com/blog/laundry_bear_infrastructure_analysis/#investigating_spear_phishing_domain_history)
- [Registration Similarities](https://www.validin.com/blog/laundry_bear_infrastructure_analysis/#registration_similarities)
- [DNS History](https://www.validin.com/blog/laundry_bear_infrastructure_analysis/#dns_history)
- [Host Response History](https://www.validin.com/blog/laundry_bear_infrastructure_analysis/#host_response_history)
- [Host Response Pivots](https://www.validin.com/blog/laundry_bear_infrastructure_analysis/#host_response_pivots)
- [enticator-secure\[.\]com](https://www.validin.com/blog/laundry_bear_infrastructure_analysis/#digging_further_enticator)
- [104.36.83\[.\]170](https://www.validin.com/blog/laundry_bear_infrastructure_analysis/#digging_further_104)
- [walshhgroup\[.\]com](https://www.validin.com/blog/laundry_bear_infrastructure_analysis/#digging_further_walshhgroup)
- [maidservant\[.\]shop](https://www.validin.com/blog/laundry_bear_infrastructure_analysis/#digging_further_maidservant)
- [it-sharepoint\[.\]com](https://www.validin.com/blog/laundry_bear_infrastructure_analysis/#digging_further_it-sharepoint)
- [54.144.139\[.\]77](https://www.validin.com/blog/laundry_bear_infrastructure_analysis/#digging_further_54)
- [Ideas for Additional Pivots](https://www.validin.com/blog/laundry_bear_infrastructure_analysis/#ideas_for_additional_pivots)
- [Conclusion](https://www.validin.com/blog/laundry_bear_infrastructure_analysis/#conclusion)
- [Indicators](https://www.validin.com/blog/laundry_bear_infrastructure_analysis/#indicators)

## Hunting Laundry Bear: Infrastructure Analysis Guide and Findings

Laundry Bear, as [tracked by Dutch Intelligence](https://www.defensie.nl/downloads/publicaties/2025/05/27/aivd-en-mivd-onderkennen-nieuwe-russische-cyberactor) (also tracked as [Void Blizzard by Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/2025/05/27/new-russia-affiliated-actor-void-blizzard-targets-critical-sectors-for-espionage/)), is a Russian state-sponsored APT that has been active since at least April 2024 and has targeted NATO countries and Ukraine for intelligence gathering. This threat group has been reported using stolen credentials or session cookies for initial access and has leveraged spear phishing with domain typosquats like `micsrosoftonline[.]com`. Targets include the Dutch police, a Ukrainian aviation organization, and European and US NGOs. This blog expands on public intelligence showcasing ways we’ve pivoted and discovered new infrastructure and activity.

The [initial reporting](https://www.microsoft.com/en-us/security/blog/2025/05/27/new-russia-affiliated-actor-void-blizzard-targets-critical-sectors-for-espionage/) for this threat actor by Microsoft listed three actor-controlled domain indicators:

- `micsrosoftonline[.]com` \- spear-phishing domain (Evilginx)
- `ebsumrnit[.]eu` \- malicious sender
- `outlook-office[.]micsrosoftonline[.]com` \- spear-phishing domain

![Figure 1. Published initial indicators for Laundry Bear / Void Blizzard.](https://www.validin.com/images/laundry_bear_infrastructure_analysis/image22.png)

Figure 1. Published initial indicators for Laundry Bear / Void Blizzard.

In this post, we will demonstrate how to find additional domains associated with the published indicators for Laundry Bear using advanced pivoting techniques in Validin.

## Malicious Sender Domain History

We’ll start with `ebsumrnit[.]eu`, which was noted as being the origination domain for a malicious email. This is a lookalike domain for `ebsummit[.]eu`, which is a legitimate domain for European Business Summits. We’ll use a wildcard search in Validin, which enables us to find all DNS, host response, registration records, certificates, and OSINT references for the apex domain and any subdomains with a single search.

![Figure 2. Initial enrichment with a wildcard DNS history search shows limited opportunities for direct pivoting due to the usage of popular name servers and shared hosting IPs.](https://www.validin.com/images/laundry_bear_infrastructure_analysis/image10.png)

Figure 2. Initial enrichment with a wildcard DNS history search shows limited opportunities for direct pivoting due to the usage of popular name servers and shared hosting IPs.

The white and blue flame icons in the search results tell us that the indicator has high prevalence within Validin. This is a great visual indicator that helps us focus on pivots that are likely to yield more unique overlaps.

When we switch to the “DNS Records” tab, we learn that `email[.]ebsumrnit[.]eu` has a CNAME record to `eu[.]mailgun[.]org`. Validin reports connections by following CNAME records, so all other DNS records for `email[.]ebsumrnit[.]eu` are a result of this CNAME.

![Figure 3. TXT records show use of Mailgun, Cloudflare SOA records, and a CNAME record on the email. subdomain.](https://www.validin.com/images/laundry_bear_infrastructure_analysis/image11.png)

Figure 3. TXT records show use of Mailgun, Cloudflare SOA records, and a CNAME record on the `email.` subdomain.

Looking at the registration records, we find that the domain is registered on PDR Solutions, but the `.eu` TLD WHOIS servers provide very little information. The registrant contact field contains a link to a website where we can gather additional details.

![Figure 4. The .eu WHOIS server provides very little registration information but helpfully directs to a URL where additional details can be gathered.](https://www.validin.com/images/laundry_bear_infrastructure_analysis/image1.png)

Figure 4. The `.eu` WHOIS server provides very little registration information but helpfully directs to a URL where additional details can be gathered.

![Figure 5. Visiting eurid[.]eu, we find a registration date and registrant contact email for the lookalike domain.](https://www.validin.com/images/laundry_bear_infrastructure_analysis/image8.png)

Figure 5. Visiting `eurid[.]eu`, we find a registration date and registrant contact email for the lookalike domain.

### Summary of Initial Findings for Malicious Sender Domain

The malicious sender domain, `ebsumrnit[.]eu`, has the following noteworthy features:

- Lookalike domain for the legit domain `ebsummit[.]eu`
- Registered in April 2025
- Registered with an `onionmail[.]org` email address
- Configured with `mailgun[.]org` DNS records for email
- Uses Cloudflare name servers
- Does not have an A record on the apex domain

### Finding Additional Lookalike Domains

There aren’t many direct pivots in Validin, but Validin has other tools that enable discovery of additional domains. Since `ebsumrnit[.]eu` is a lookalike domain, we’ll use Validin’s lookalike feature to craft a regular expression to help us identify other potential domains related to the known malicious lookalike domain.

We will build a regular expression search with the following qualities:

- Has a `.eu` TLD
- First seen within the last 180 days
- Has possible character substitutions (e.g., “ `m`” and “ `rn`”)
- May have dropped vowels or missing suffixes

We’ll end up with the following regular expression search:

`/^e[bd]s[uan]?(rn|m)+([li]?t)?s?.eu$/`

![Figure 6. Regex lookalike search in Validin finds domains that resemble ebsummit[.]eu, the imitated domain.](https://www.validin.com/images/laundry_bear_infrastructure_analysis/image14.png)

Figure 6. Regex lookalike search in Validin finds domains that resemble `ebsummit[.]eu`, the imitated domain.

From this search we find 6 domains, including the starting domain, that:

- Match the regular expression
- Were first seen in April or May 2025
- Used the registrar PDR Ltd.
- Use Cloudflare Name Servers

These domains, with their registration dates and registrant emails, are:

ebsummit lookalike domains

Copy Code

```csv
ebsumrnit[.]eu  - 15 April 2025 - danhutton@onionmail[.]org
ebsurnmit[.]eu  - 18 April 2025 - danhutton@onionmail[.]org
ebsummlt[.]eu   - 24 April 2025 - carriehuff@onionmail[.]org
ebsummt[.]eu    - 22 May 2025   - carriehuff@onionmail[.]org
ebsumlts[.]eu   - 27 May 2025   - saryman@aficors[.]com
ebsum[.]eu      - 27 May 2025   - saryman@aficors[.]com

```

The first 4 domains were all configured to use mailgun DNS records, each with a single `email.` subdomain that was also configured with a CNAME to mailgun.

The last two look slightly different, but still use a domain name associated with email obfuscation ( `aficors[.]com`). These were registered the day that the Microsoft report was released, which may have halted further weaponization.

Of note, `ebsummlt[.]eu` redirected to `https[:]//ebsummits[.]eu/our-summits/european-business-summit/` as early as April 25, 2025. It continued redirecting to this site until sometime between June 26 and June 28, after which Cloudflare flagged the domain as phishing.

![Figure 7. Showing the earliest recorded response to direct access to ebsummlt[.]eu, which redirects to a benign domain via HTTP redirect when visited.](https://www.validin.com/images/laundry_bear_infrastructure_analysis/image19.png)

Figure 7. Showing the earliest recorded response to direct access to `ebsummlt[.]eu`, which redirects to a benign domain via HTTP redirect when visited.

![Figure 8. Inspecting the full HTML response available on-demand in Validin, we see the Cloudflare phishing warning.](https://www.validin.com/images/laundry_bear_infrastructure_analysis/image17.png)

Figure 8. Inspecting the full HTML response available on-demand in Validin, we see the Cloudflare phishing warning.

## Investigating Spear Phishing Domain History

The only other domain in the report was `micsrosoftonline[.]com` and the subdomain `outlook-office.micsrosoftonline[.]com`. We’ll make a wildcard search in Validin to gather connections and history for the apex domain and any subdomains to look for pivoting opportunities.

### Registration Similarities

The domain `micsrosoftonline[.]com` was also registered on PDR Ltd., but slightly earlier on February 25, 2025. We observe from Validin’s WHOIS history that the email used by the registrant also used an `onionmail[.]com` email address.

![Figure 9. Registration history showing a privacy-preserving email address in the registrant contact details.](https://www.validin.com/images/laundry_bear_infrastructure_analysis/image20.png)

Figure 9. Registration history showing a privacy-preserving email address in the registrant contact details.

### DNS History

Like the other lookalike domains, this domain also uses Cloudflare name servers and IP space. Validin has tracked this domain and numerous subdomains for years, as can be seen in Validin’s DNS history, but only the resolutions starting in February are relevant to this investigation.

![Figure 10. Comprehensive DNS history showing distinct time periods of activity.](https://www.validin.com/images/laundry_bear_infrastructure_analysis/image4.png)

Figure 10. Comprehensive DNS history showing distinct time periods of activity.

Also note that for about a week in March (March 13, 2025 until March 21, 2025), the SOA records were marked as `suspended-domain[.]com` before returning back to Cloudflare.

![Figure 11. SOA records showing suspended-domain[.]com for about a week in March 2025.](https://www.validin.com/images/laundry_bear_infrastructure_analysis/image15.png)

Figure 11. SOA records showing `suspended-domain[.]com` for about a week in March 2025.

### Host Response History

Between February 25, 2025 and July 24, 2025, Validin gathered host responses from `micsrosoftonline[.]com` and its subdomains nearly 900 times. Given that this was used as a spear-phishing domain, we can learn about how this domain has responded with significant detail using Validin’s host response history, which now [extends back more than 8 months](https://www.validin.com/blog/crawl_history_artifact_upgrade/#greatly_expanded_host_response_history) in the Enterprise platform.

We observe Cloudflare HTTP 52x errors between February 27, 2025 until March 7, 2025, which is when Validin observed a successful response to a request from the apex domain that returned HTML content redirecting the user to the Rick Astley’s “Never Gonna Give You Up” music video ( `https[:]//www[.]youtube[.]com/watch?v=dQw4w9WgXcQ`). Without additional context around timing or actions taken, it’s unclear whether this was done as a result of action by authorities or by the threat actor.

![Figure 12. Viewing full HTTP response history in Validin, linking to Rick Astley video.](https://www.validin.com/images/laundry_bear_infrastructure_analysis/image7.png)

Figure 12. Viewing full HTTP response history in Validin, linking to Rick Astley video.

These responses continue on various subdomains until March 13, 2025, which aligns with the timing of the change in SOA records to the `suspended-domain[.]com` domain. During that suspension period, ending March 21, 2025, the spear phishing domain and subdomains responded with the following HTML:

window.location.href redirector

Copy Code

```csv
<!DOCTYPE html><html><head><script>window.onload=function(){window.location.href="/lander”}</script></head></html>

```

![Figure 13. The change in host responses is highlighted by the change in response sizes between March 21 and March 26.](https://www.validin.com/images/laundry_bear_infrastructure_analysis/image2.png)

Figure 13. The change in host responses is highlighted by the change in response sizes between March 21 and March 26.

After that, `micsrosoftonline[.]com` and its subdomains responded with the following body until May 4, 2025, after which it hasn’t responded with successful HTTP codes:

top.location.href redirector - outlook\[.\]live\[.\]com

Copy Code

```csv
<html><head><meta name=‘referrer’ content=‘no-referrer’><script>top.location.href=‘https://outlook.live.com’;</script></head><body></body></html>

```

Body SHA1: `38c47d338a9c5ab7ccef7413edb7b2112bdfc56f`

## Host Response Pivots

We’ll use Validin’s detailed host response history to find additional domains that have responded similarly to the spear phishing domain described in the original Microsoft report. These domains are likely to highlight other domains that were either sinkholed and not reported, or are possibly related to the same campaign.

We’ll use the body SHA1 hash that included the JavaScript redirect to `https[:]//outlook[.]live[.]com`: `38c47d338a9c5ab7ccef7413edb7b2112bdfc56f`.

Viewing the E2LDs that have responded (or have had subdomains that have responded) with HTML having the SHA1 hash `38c47d338a9c5ab7ccef7413edb7b2112bdfc56f`, we find 8 total apex domains, including the original domain from the report:

Pivots from 38c47d338a9c5ab7ccef7413edb7b2112bdfc56f

Copy Code

```csv
mail-forgot[.]com
enticator-secure[.]com
x9a7lm02kqaccountprotectionaccountsecuritynoreply[.]com
miscrsosoft[.]com
micsrosoftonline[.]com
remerelli[.]com
weblogmail[.]live
maidservant[.]shop

```

![Figure 14. E2LDs with the body hash 38c47d338a9c5ab7ccef7413edb7b2112bdfc56f observed since mid-November 2024.](https://www.validin.com/images/laundry_bear_infrastructure_analysis/image16.png)

Figure 14. E2LDs with the body hash `38c47d338a9c5ab7ccef7413edb7b2112bdfc56f` observed since mid-November 2024.

### Digging Further - `enticator-secure[.]com`

The domain `enticator-secure[.]com` includes many subdomains under `auth[.]enticator-secure[.]com` (“authenticator secure”) that appear to imitate the login pages of various services. Validin has captured active host responses from the domain every day since it was registered on July 1, 2025. Most of these connections were unsuccessful, but several of them responded with the body that allowed us to connect this domain to the original spear phishing domain.

For about 24 hours, from July 6, 2025 until July 7, 2025, Validin recorded responses with a “GlobalShip Logistics” theme. Specifically, the IP address `104.36.83[.]170` returned this content on several subdomains and the domain `ups-mail[.]delivery`, which also resolved to `104.36.83[.]170` during that time.

![Figure 15. Screenshot of the rendered &ldquo;GlobalShip Logistics&rdquo; page returned by several domains on July 6 - July 7, 2025, retrieved from Validin.](https://www.validin.com/images/laundry_bear_infrastructure_analysis/image23.png)

Figure 15. Screenshot of the rendered “GlobalShip Logistics” page returned by several domains on July 6 - July 7, 2025, retrieved from Validin.

### Digging Further - `104.36.83[.]170`

Looking at Validin’s DNS history for `104.36.83[.]170`, we observe DNS history for only the most recent 30 days on 5 domains (with many subdomains):

DNS history for 104.36.83\[.\]170

Copy Code

```csv
nticator[.]com
usembassyservice[.]com
ups-mail[.]delivery
enticator-secure[.]com
walshhgroup[.]com

```

![Figure 16. Reverse DNS history for 104.36.83.170.](https://www.validin.com/images/laundry_bear_infrastructure_analysis/image12.png)

Figure 16. Reverse DNS history for `104.36.83.170`.

The domain `walshhgroup[.]com` is a lookalike domain for `walshgroup[.]com` \- the construction management services company.

### Digging Further - `walshhgroup[.]com`

On July 1, 2025, Validin captured a response on `login[.]walshhgroup[.]com` that redirected visitors to `https[:]//walshhgroup[.]com:3443/enquiry.pdf` \- possibly a malicious PDF, and a tactic that aligns with the approach described in the original Microsoft report. This strengthens the case that this domain is related to Laundry Bear.

![Figure 17. HTML response that redirects visitors to a PDF file on a non-standard HTTPS port.](https://www.validin.com/images/laundry_bear_infrastructure_analysis/image3.png)

Figure 17. HTML response that redirects visitors to a PDF file on a non-standard HTTPS port.

Additionally, the subdomain `link[.]walshhgroup[.]com` was configured via a CNAME record to use SMTP2GO, a service used for email delivery and tracking, from June 13, 2025 until July 1, 2025. Since July 1, neither the apex domain nor any subdomain of `walshhgroup[.]com` has responded with A (DNS IPv4 address) records.

### Digging Further - `maidservant[.]shop`

Like `enticator-secure[.]com` and `micsrosoftonline[.]com`, `maidservant[.]shop` has many subdomains with account management and login themes:

![Figure 18. Subdomains of maidservant[.]shop.](https://www.validin.com/images/laundry_bear_infrastructure_analysis/image9.png)

Figure 18. Subdomains of `maidservant[.]shop`.

Looking back to the earliest history available in Validin, dating to November 6, 2024, we observe a similar JavaScript redirection to a different Microsoft domain from `login[.]maidservant[.]shop`: `login[.]live[.]com`.

![Figure 19. The HTML returned by login[.]maidservant[.]shop on November 6, 2024, as recorded by Validin.](https://www.validin.com/images/laundry_bear_infrastructure_analysis/image21.png)

Figure 19. The HTML returned by `login[.]maidservant[.]shop` on November 6, 2024, as recorded by Validin.

top.location.href redirector - login\[.\]live\[.\]com

Copy Code

```csv
<html><head><meta name=‘referrer’ content=‘no-referrer’><script>top.location.href=‘https://login.live.com’;</script></head><body></body></html>

```

Pivoting on that body hash, `2c0fa608bd243fce6f69ece34addf32571e8368f`, we find that there are 14 additional apex domains with nearly 100 subdomains that have responded with the same HTML body since November 6, 2024.

![Figure 20. Domains that Validin observed responding with a JavaScript redirect to login[.]live[.]com since November 6, 2024.](https://www.validin.com/images/laundry_bear_infrastructure_analysis/image13.png)

Figure 20. Domains that Validin observed responding with a JavaScript redirect to `login[.]live[.]com` since November 6, 2024.

Full list of domains:

Domains with JavaScript redirect to login\[.\]live\[.\]com

Copy Code

```csv
it-sharepoint.com
avsgroup.au
ourbelovedsainscore.space
microffice.org
propescom.com
myspringbank.com
portal-microsoftonline.com
app-v4-mybos.com
teamsupportonline.top
m-365-app.com
refundes.net
redronesolutions.cloud
defraudatubanco.com
maidservant.shop

```

Switching to the timeline view and filtering for the IPs, we can see the progression of the deployment of this response across AS 14061 (Digital Ocean), AS 135357 (SKHT-AS Shenzhen Katherine Heng Technology Information Co.), AS 14618 and AS 16509 (AWS), AS 54290 (Hostwinds), AS 12586 (ASGHOSTNET), and AS 6698 (ARCHERNET).

![Figure 20. Timeline showing the usage of different ASNs that have served the body hash 2c0fa608bd243fce6f69ece34addf32571e8368f since November 2024.](https://www.validin.com/images/laundry_bear_infrastructure_analysis/image5.png)

Figure 20. Timeline showing the usage of different ASNs that have served the body hash `2c0fa608bd243fce6f69ece34addf32571e8368f` since November 2024.

### Digging Further - `it-sharepoint[.]com`

The domain `it-sharepoint[.]com` has returned the JavaScript redirect content with the body hash `2c0fa608bd243fce6f69ece34addf32571e8368f` since at least November 7, 2024. Comparing this domain against others we’ve already looked at, we note the following:

- A mix of successful and unsuccessful HTTP requests over the last 8 months, which is consistent with the host response history we’ve observed for other domains
- Subdomains with login, okta, and Microsoft themes
- Registration on Amazon Registrar, Inc. beginning March 23, 2023

The IP address `34.204.123[.]157` was a DNS A record for 18 subdomains of `it-sharepoint[.]com` and was also a DNS A record for 6 different apex domains, often with a few subdomains each, between April 5, 2023 and July 24, 2025. These domains include:

Domains with A record overlap with 34.204.123\[.\]157

Copy Code

```csv
spidergov[.]org
deloittesharepoint[.]com
bidscale[.]net
max-linear[.]com
aoc-gov[.]us
it-sharepoint[.]com

```

![Figure 22. Reverse DNS history for IP 34.204.123[.]157 since February 2023.](https://www.validin.com/images/laundry_bear_infrastructure_analysis/image24.png)

Figure 22. Reverse DNS history for IP `34.204.123[.]157` since February 2023.

### Digging Further - `54.144.139[.]77`

The subdomains `static[.]it-sharepoint[.]com`, `ads[.]it-sharepoint[.]com`, and `ns1[.]it-sharepoint[.]com` have resolved to `54.144.139[.]77` since January 25, 2025.

Between May 28, 2025 and June 2, 2025, Validin made 8 HTTPS requests to that IP that returned a self-signed certificate with SHA1 `ade08cd340765e68f65174820b46c0e3d9b52ab4` (SHA256: `f0f3db24af0132755c8a0068dde433f857d8639020deb2817d52d3a1d5d99f35`). This self-signed certificate was also returned by another AWS-hosted IP, `44.223.255[.]29`, between April 13 and May 27, 2025, linking us to another domain name, `css[.]mpgc10[.]com`.

![Figure 23. The &ldquo;Quick Pivot&rdquo; button within Validin helps simplify the process of finding good pivots. In this view, we see 3 domains and 2 IP addresses connected by the same certificate SHA1.](https://www.validin.com/images/laundry_bear_infrastructure_analysis/image18.png)

Figure 23. The “Quick Pivot” button within Validin helps simplify the process of finding good pivots. In this view, we see 3 domains and 2 IP addresses connected by the same certificate SHA1.

![Figure 24. Search results for IPs and domain names that have returned the same certificate SHA1 in Validin.](https://www.validin.com/images/laundry_bear_infrastructure_analysis/image6.png)

Figure 24. Search results for IPs and domain names that have returned the same certificate SHA1 in Validin.

## Ideas for Additional Pivots

There are many unexplored pivots in Validin that connect the domains and IPs described in this post to additional domains and IP addresses potentially related to Laundry Bear. These include:

- HTTP response body pivots
- Registration pivots
- DNS record pivots
- Lookalike domain pivots

## Conclusion

The original report revealed just two domain indicators, but we were able to use several pivoting and hunting techniques in Validin to find many additional indicators. This was made possible with Validin’s Enterprise platform, which gives threat hunting teams unparalleled access to virtual host responses and DNS history.

Ready to elevate your threat hunting, threat attribution, and incident response efforts? Whether you’re an individual analyst or part of a larger enterprise team, Validin offers solutions that meet your needs. Individual users can [create a free account and self-upgrade](https://app.validin.com/register) to access more advanced features and data.

Part of a team? Contact us today to explore our enterprise options and discover how Validin can power your organizations with powerful tools and unparalleled data. Let Validin help you work smarter, faster, and more effectively in the fight against cyber threats.

## Indicators

Note: for brevity, only the effective second-level domains (E2LDs, aka “apex” domains) are included below.

Commonly observed subdomains

Copy Code

```csv
login
email
account
okta
live
csp
sso
reporting
microsoftonline
mail
cdn

```

E2LDs discovered

Copy Code

```csv
redronesolutions.cloud
ourbelovedsainscore.space
weblogmail.live
microffice.org
spidergov.org
portal-microsoftonline.com
micsrosoftonline.com
enticator-secure.com
remerelli.com
myspringbank.com
propescom.com
defraudatubanco.com
m-365-app.com
max-linear.com
app-v4-mybos.com
miscrsosoft.com
it-sharepoint.com
deloittesharepoint.com
mail-forgot.com
x9a7lm02kqaccountprotectionaccountsecuritynoreply.com
maidservant.shop
teamsupportonline.top
aoc-gov.us
bidscale.net
refundes.net
avsgroup.au
ebsum.eu
ebsumlts.eu
ebsurnmit.eu
ebsumrnit.eu
ebsummlt.eu
ebsummt.eu

```

Related IP addresses

Copy Code

```csv
3.64.201[.]107
3.126.53[.]226
5.230.36[.]62
34.204.123[.]157
54.144.139[.]77
64.23.244[.]176
64.226.126[.]33
52.78.180[.]48
54.167.184[.]45
104.168.144[.]21
154.216.18[.]83
170.64.163[.]105
170.64.209[.]129
176.97.124[.]54

```

## Contact Us

"Validin is the first tab I open every morning"

\- Senior Analyst at a Financial Services IT Company

Submit
