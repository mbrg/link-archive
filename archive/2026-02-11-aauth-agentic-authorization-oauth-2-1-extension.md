---
date: '2026-02-11'
description: 'The Internet-Draft "AAuth - Agentic Authorization OAuth 2.1 Extension"
  proposes an extension to OAuth 2.1 specifically for confidential agent clients,
  enabling them to request user consent for access tokens via asynchronous methods
  (HTTP polling, SSE, or WebSockets). The document introduces the Agent Authorization
  Grant, emphasizing long-lived agent identities and providing human-readable scope
  descriptions and a `reason` parameter for user interaction. This mechanism promotes
  enhanced usability while addressing security concerns through strict credential
  management and short-lived tokens. Additionally, it initiates registration for a
  new grant type: `urn:ietf:params:oauth:grant-type:agent_authorization`.'
link: https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html
tags:
- Token Management
- WebSocket
- AI Agents
- OAuth
- Authorization
title: AAuth - Agentic Authorization OAuth 2.1 Extension
---

| Internet-Draft | AAuth | May 2025 |
| --- | --- | --- |
| White | Expires 14 November 2025 | \[Page\] |

Workgroup:Network Working GroupInternet-Draft:draft-patwhite-aauth-00Published:13 May 2025Intended Status:InformationalExpires:14 November 2025Author:

P. White

# AAuth - Agentic Authorization OAuth 2.1 Extension

## [Abstract](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#abstract)

This document defines the **Agent Authorization Grant**, an OAuth 2.1 extension for **confidential agent clients**—software or AI agents with long-lived identities—to request end-user consent and obtain access tokens via HTTP polling, Server-Sent Events (SSE), or WebSocket. It is heavily inspired by the core dance of the OAuth 2.0 Device Authorization Grant (RFC 8628) but is tailored for agents either long lived identities, and introduces scoped, natural-language descriptions and a `reason` parameter provided by the agent. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-abstract-1)

## [Status of This Memo](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#name-status-of-this-memo)

This Internet-Draft is submitted in full conformance with the
provisions of BCP 78 and BCP 79. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-boilerplate.1-1)

Internet-Drafts are working documents of the Internet Engineering Task
Force (IETF). Note that other groups may also distribute working
documents as Internet-Drafts. The list of current Internet-Drafts is
at [https://datatracker.ietf.org/drafts/current/](https://datatracker.ietf.org/drafts/current/). [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-boilerplate.1-2)

Internet-Drafts are draft documents valid for a maximum of six months
and may be updated, replaced, or obsoleted by other documents at any
time. It is inappropriate to use Internet-Drafts as reference
material or to cite them other than as "work in progress." [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-boilerplate.1-3)

This Internet-Draft will expire on 14 November 2025. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-boilerplate.1-4)

## [Copyright Notice](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#name-copyright-notice)

Copyright (c) 2025 IETF Trust and the persons identified as the
document authors. All rights reserved. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-boilerplate.2-1)

This document is subject to BCP 78 and the IETF Trust's Legal
Provisions Relating to IETF Documents
([https://trustee.ietf.org/license-info](https://trustee.ietf.org/license-info)) in effect on the date of
publication of this document. Please review these documents
carefully, as they describe your rights and restrictions with
respect to this document. Code Components extracted from this
document must include Revised BSD License text as described in
Section 4.e of the Trust Legal Provisions and are provided without
warranty as described in the Revised BSD License. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-boilerplate.2-2)

[▲](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#)

## [Table of Contents](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#name-table-of-contents)

## [1\.](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#section-1) [Introduction](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#name-introduction)

OAuth 2.1 provides a framework for delegated access via bearer tokens. In modern AI architectures, **agents**—autonomous software processes—act on behalf of users or other agents. This extension defines the **Agent Authorization Grant**, enabling agents with long lived identities to request a delegated token with human-in-the-loop consent, and to receive tokens asynchronously via polling, SSE, or WebSocket, while leveraging natural-language scope descriptions published by resource servers. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-1-1)

## [2\.](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#section-2) [Conventions and Requirements Language](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#name-conventions-and-requirement)

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” are to be interpreted as described in \[RFC2119\]. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-2-1)

## [3\.](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#section-3) [Terminology](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#name-terminology)

- **Agent**: A confidential client (software or AI) with a stable, long-lived identity (`client_id`). [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-3-1.1)
- **Authorization Server (AS)**: Issues `request_code` handles, manages user consent, and issues access tokens. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-3-1.2)
- **Resource Server (RS)**: API server that protects resources via OAuth tokens and publishes human-readable scope descriptions at `/.well-known/aauth.json`. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-3-1.3)
- **request\_code**: Opaque handle returned by the AS to correlate an agent’s request with subsequent token retrieval. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-3-1.4)
- **reason**: Human-readable explanation provided by the agent, shown to the user during consent. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-3-1.5)
- **scope\_descriptions**: Natural-language text for each requested scope, fetched from the RS’s discovery document. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-3-1.6)

## [4\.](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#section-4) [Agent Authorization Grant](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#name-agent-authorization-grant)

> This flow is modeled on the OAuth 2.0 Device Authorization Grant (RFC 8628) but is tailored for **confidential agent clients** with long-lived identities, and optimized for performant delivery of tokens to the agent. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4-1.1)

### [4.1.](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#section-4.1) [Agent Authorization Request](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#name-agent-authorization-request)

An agent requests user approval by authenticating and POSTing to `/agent_authorization`: [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.1-1)

```
POST /agent_authorization HTTP/1.1
Host: auth.example.com
Content-Type: application/x-www-form-urlencoded
Authorization: Basic <base64(client_id:client_secret)>

grant_type=urn:ietf:params:oauth:grant-type:agent_authorization&
scope=urn:example:resource.read urn:example:resource.write&
reason="<human-readable reason>"
```

[¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.1-2)

- **grant\_type**: MUST be `urn:ietf:params:oauth:grant-type:agent_authorization`. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.1-3.1)
- **scope**: Space-delimited list of scope URIs. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.1-3.2)
- **reason**: Concise, human-readable explanation provided by the agent; MUST be echoed verbatim by the AS. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.1-3.3)

Upon receipt, the AS: [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.1-4)

1. **Validates** client credentials. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.1-5.1)
2. **Fetches** each scope’s description from the target RS’s `https://{rs}/.well-known/aauth.json#scope_descriptions`. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.1-5.2)
3. **Returns:** [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.1-5.3)

```
{
  "request_code": "GhiJkl-QRstuVwxyz",
  "token_endpoint": "https://auth.example.com/token",
  "poll_interval": 5,
  "expires_in": 600,
  "poll_sse_endpoint": "https://auth.example.com/agent_authorization/sse",
  "poll_ws_endpoint": "wss://auth.example.com/agent_authorization/ws"
}
```

[¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.1-6)

### [4.2.](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#section-4.2) [User Approval User Approval](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#name-user-approval-user-approval)

The AS is fully responsible for user interaction: [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.2-1)

1. **Initiate** the consent review flow with the user. This spec does not specify how this occurs, it could be through an app, a chat client, or some other mechanism. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.2-2.1)
2. **Display** the `reason` and each `scope_descriptions` entry to ensure the user has all the information necessary to assess the consent request. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.2-2.2)
3. **Authenticate** the user (including MFA) and, upon consent, bind approval to `request_code`. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.2-2.3)

> _Note:_ The agent does **not** handle redirects or UI rendering—it passively awaits token availability. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.2-3.1)

### [4.3.](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#section-4.3) [Token Retrieval](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#name-token-retrieval)

After user approval, the agent obtains its access token via one of: [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.3-1)

1. **HTTP Polling** [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.3-2.1)

```
   POST /token HTTP/1.1
   Host: auth.example.com
   Content-Type: application/x-www-form-urlencoded
   Authorization: Basic <base64(client_id:client_secret)>

   grant_type=urn:ietf:params:oauth:grant-type:device_code&
   device_code=GhiJkl-QRstuVwxyz
```

[¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.3-3)

_Pending_: `{"error":"authorization_pending"}` _Success_: Standard OAuth 2.x token response. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.3-4)

2. **Server-Sent Events (SSE)** [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.3-5.1)

```
   GET /agent_authorization/sse?request_code=GhiJkl-QRstuVwxyz HTTP/1.1
   Host: auth.example.com
   Authorization: Bearer <agent_jwt>
   Accept: text/event-stream
```

[¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.3-6)

On approval: [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.3-7)

```
   event: token_response
   data: {"access_token":"<JWT>","expires_in":900,"issued_token_type":"urn:ietf:params:oauth:token-type:jwt"}
```

[¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.3-8)

3. **WebSocket** [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.3-9.1)

```
   GET /agent_authorization/ws?request_code=GhiJkl-QRstuVwxyz HTTP/1.1
   Host: auth.example.com
   Upgrade: websocket
   Connection: Upgrade
   Sec-WebSocket-Protocol: aauth.agent-flow
   Authorization: Bearer <agent_jwt>
```

[¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.3-10)

On open: [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.3-11)

```
   {
     "type": "token_response",
     "access_token": "<JWT>",
     "issued_token_type": "urn:ietf:params:oauth:token-type:jwt",
     "expires_in": 900
   }
```

[¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.3-12)

### [4.4.](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#section-4.4) [Error Handling & Back-Off](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#name-error-handling-back-off)

- **HTTP Polling**: MUST honor `error="slow_down"` with `Retry-After` headers; return standard OAuth error codes such as `authorization_pending`, `access_denied`, or `expired_token`. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.4-1.1.1)

- **Server-Sent Events (SSE)**: [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.4-1.2.1)


  - On token response: [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.4-1.2.2.1)

```
event: token_response
data: {"access_token":"<JWT>","expires_in":900,"issued_token_type":"urn:ietf:params:oauth:token-type:jwt"}
```

[¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.4-1.2.3)

  - On user rejection: [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.4-1.2.4.1)

```
event: error
data: {"error":"access_denied","error_description":"The user denied the request."}
```

[¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.4-1.2.5)

  - On request expiration: [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.4-1.2.6.1)

```
event: error
data: {"error":"expired_token","error_description":"The request_code has expired."}
```

[¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.4-1.2.7)

- **WebSocket**: [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.4-1.3.1)


  - On token response: [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.4-1.3.2.1)

```
{"type":"token_response","access_token":"<JWT>","issued_token_type":"urn:ietf:params:oauth:token-type:jwt","expires_in":900}
```

[¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.4-1.3.3)

  - On user rejection or expiration: [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.4-1.3.4.1)

```
{"type":"error","error":"access_denied","error_description":"The user denied the request."}
```

[¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.4-1.3.5)

```
{"type":"error","error":"expired_token","error_description":"The request_code has expired."}
```

[¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.4-1.3.6)

- **Security**: All endpoints SHOULD enforce TLS and require client authentication. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-4.4-1.4.1)


## [5\.](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#section-5) [Security Considerations. Security Considerations](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#name-security-considerations-sec)

- Agents MUST protect their long-lived credentials. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-5-1.1)
- Short-lived `request_code` and tokens limit replay risk. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-5-1.2)
- RS scope descriptions should not expose sensitive system details. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-5-1.3)
- Implement rate-limiting on polling and push channels to prevent abuse. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-5-1.4)

## [6\.](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#section-6) [IANA Considerations](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#name-iana-considerations)

This document registers the following new OAuth grant type: [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-6-1)

```
urn:ietf:params:oauth:grant-type:agent_authorization
```

[¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-6-2)

## [7\.](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#section-7) [References](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#name-references)

### [7.1.](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#section-7.1) [Normative References](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html\#name-normative-references)

- \[RFC2119\] Bradner, "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-7.1-1.1)
- \[RFC8628\] Wahl, "OAuth 2.0 Device Authorization Grant", RFC 8628. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-7.1-1.2)
- \[RFC8693\] Jones & Campbell, "OAuth 2.0 Token Exchange", RFC 8693. [¶](https://www.ietf.org/archive/id/draft-patwhite-aauth-00.html#section-7.1-1.3)
