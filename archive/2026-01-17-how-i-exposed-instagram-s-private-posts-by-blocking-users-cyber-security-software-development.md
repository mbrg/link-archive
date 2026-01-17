---
date: '2026-01-17'
description: A recent technical exploration revealed a vulnerability in Instagram's
  oEmbed API, allowing unauthorized access to private posts under specific conditions.
  By manipulating user agents and utilizing XS-Leaks, the attacker could discern blocked
  users based on response variations from the API, bypassing standard privacy measures.
  The exploitation relied on embedding features and response handling discrepancies,
  particularly targeting requests formatted as originating from mobile devices. This
  discovery highlights weaknesses in Meta's security architecture, notably the handling
  of user permissions by the oEmbed service. The issue has since been resolved, earning
  the discoverer a $10,000 bounty.
link: https://003random.com/posts/meta-bountycon-instagram-writeup/
tags:
- XS-Leaks
- vulnerability
- bug bounty
- Instagram
- oEmbed
title: How I Exposed Instagram's Private Posts by Blocking Users · Cyber Security
  & Software Development
---

This post will go over how I discovered a vulnerability in Instagram which enabled me to view the posts of private Instagram accounts. But before we dive into that, we are traveling back in time a little.

This all started at BountyConEdu, which was held in Madrid, and was a form of the traditional BountyCon, but mainly focussed on students. [Ed](https://twitter.com/EdOverflow/), [David](https://twitter.com/xdavidhu), [Linus](https://twitter.com/_zulln), [El](https://twitter.com/ElSec_) and I [(003random)](https://twitter.com/rub003) formed a team, which ended up taking first place. This led us to be invited to the annual BountyCon, organized later that year. Fast forward to 2 weeks in advance of BountyCon…

It was almost time to fly out to Singapore for BountyCon, and I had been testing for long days, without finding much. I set-up an Android simulator, tested the Facebook main application, and explored the Instagram web application. No findings, no vulnerabilities and nothing to grab on to. Just a bunch of notes, Burp Suite repeater tabs and caffeine.

Now fast forward to one of the last days before I was bound to leave home to travel to BountyCon.

# \[1/3\] Instagram post embedding  [Link to heading](https://003random.com/posts/meta-bountycon-instagram-writeup/\#13-instagram-post-embedding)

Starting at puzzle piece #1.

Instagram has a feature to embed posts. And right off the bat, I can hear you say:

> Oh, thats it? You just use the embed feature to pull private post data!

Technically, yes. But I can bet you that hundreds of other bug bounty hunters have tried that, and I can tell you; it presents itself as properly secured.

Let’s dive into how embedding works on Instagram.

Embedding a post can be done by clicking the three dots above a post, followed by selecting the embed option. This will open a popup with the embed HTML.
However, in the background, a request is made to `https://www.instagram.com/api/v1/oembed/`, which returns a JSON structure with information about the post, such as its author, title, and the media (photo) itself. This media is a URL to the instragram CDN, with special auth tokens that allow you to view the post.

```bash
curl https://www.instagram.com/api/v1/oembed/?hidecaption=0&maxwidth=540&url=https://www.instagram.com/p/CxN8UGnIPp_
```

```json
{
    "version": "1.0",
    "title": "We still have some work to do, good to see some old friends though \ud83e\udd8e \ud83c\uddf8\ud83c\uddec",
    "author_name": "maxverstappen1",
    "author_url": "https://www.instagram.com/maxverstappen1",
    "author_id": 43904777,
    "media_id": "3192472975154674303_43904777",
    "provider_name": "Instagram",
    "provider_url": "https://www.instagram.com",
    "type": "rich",
    "width": 540,
    "height": null,
    "html": "[The HTML embed code that will be shown to the user in the popup]",
    "thumbnail_url": "https://scontent-ams4-1.cdninstagram.com/v/t51.2885-15/378467920_268956335966120_3309614531538660518_n.jpg?stp=dst-jpg_e35_p480x480\u0026_nc_ht=scontent-ams4-1.cdninstagram.com\u0026_nc_cat=1\u0026_nc_ohc=knIz8ueMF40AX9Zuq-g\u0026edm=ALY_pVYBAAAA\u0026ccb=7-5\u0026oh=00_AfB0xZZ-6K9W8rFWEh2Kg6ft_UkKltdPfn_INRGSWRZMaw\u0026oe=650A23D8\u0026_nc_sid=57e406",
    "thumbnail_width": 480,
    "thumbnail_height": 600
}
```

Trying to use this oEmbed supplied with a post from a private account, no matter if you have access to this post or not, will result in the response being `Private media`, combined with a `403 Forbidden`.
If the account of the post has you blocked, then the response will be `No Media Match` with a `404 Not Found`.

# \[2/3\] XS-Leak  [Link to heading](https://003random.com/posts/meta-bountycon-instagram-writeup/\#23-xs-leak)

This gave me the idea to write up a proof of concept for XS-Leaks (Cross-site leaks).

Info


Cross-site leaks (aka XS-Leaks, XSLeaks) are a class of vulnerabilities derived from side-channels built into the web platform. They take advantage of the web’s core principle of composability, which allows websites to interact with each other, and abuse legitimate mechanisms 2 to infer information about the user. – [https://xsleaks.dev/](https://xsleaks.dev/)

ChatGPT, ELI5 please…

🤖: _A malicious website can find out if the current visitor is banned by me (the attacker) on Instagram, by relying on the different response given from the Instagram oEmbed endpoint for media from blocked and non-blocked accounts._

Imagine I want to identify visitors on my website which are part of a certain political party. I create an attacker’s Instagram account, block all the victims (the political party members), and then have my website request posts from these accounts (the victims), via the oEmbed endpoint.

The following script contains two different scenarios, based on the response of the oEmbed endpoint. If the endpoint returns valid JSON, then the `script.onload` is fired. Otherwise the `script.onerror` is fired, meaning that we have blocked the current visitor on Instagram (or they have blocked us).

```html
<script>
    let script = document.createElement('script');
    script.src = "https://i.instagram.com/api/v1/oembed/?url=https://www.instagram.com/p/foo-barm&hidecaption=0&maxwidth=540";
    script.onload = () => { /* do something malicious */ };
    script.onerror = () => console.log('its not a politician');
    document.head.appendChild(script);
</script>
```

While wrapping up this proof of concept, and gathering evidence (screenshots, etc), I blocked my test account one more time, and requested the oEmbed endpoint via my burp repeated tab. Yup, the JSON is gone, and im greeted with a `No Media Match` message.
I switch over to my Chrome instance where im logged in as the attacker, press F5, and… the JSON is still there.

The post I’m attempting to access should be restricted. Both accounts involved — the one I’m logged into and the one hosting the post — are not only private but also have blocked each other, which includes an automatic unfollow.

Ah well, that has to be Chrome caching the response. This would’t be the first time we get fooled by caching, right? I did a hard refresh \[ctrl + F5\], but the JSON post was still showing up.

Maybe its not caching then, I thought to myself. What could it be? Small excitement entered me, as I had been testing Meta applications for weeks at this point, without any luck.

# \[3/3\] User-Agent sniffing  [Link to heading](https://003random.com/posts/meta-bountycon-instagram-writeup/\#33-user-agent-sniffing)

This is the last key piece of the chain.

As I was determining the difference of the request that Chrome made vs the one I had in Burp Suite, I noticed that the only actual difference was the user agent. Specifically, the word `iphone` in the user agent.
As it turns out, this oEmbed endpoint has different logic defined for requests made from a mobile device, vs requests from other devices (such as desktops), and it so happened to be that I was using a user agent spoofer on chrome, which was set to a mobile UA.

After fuzzing the user agent with a wordlist of device and technology names, I came to the conclusion that the behavior seen from my Chrome instance can only be replicated by either placing `android` or `iphone` in the user agent, no matter the position or context.

# The result  [Link to heading](https://003random.com/posts/meta-bountycon-instagram-writeup/\#the-result)

Placing all the pieces together, we have a chain that allows us to bypass Meta’s various security restrictions to retrieve posts and media that are normally inaccessible. This includes not only posts and reels but potentially other user information as well. At the time of discovery, an option existed to embed Instagram profiles. However, this feature threw an error during correct usage, making it impossible to determine if the bypass worked on this oEmbed feature before a fix was deployed.

But lets stick to the proven aspect for now. By blocking a user, followed by requesting their posts via the oEmbed endpoint, topped off with `iphone` or `android` being in your user agent, you can ultimately fetch their post title, description and media.

You may be curious about the seemingly random nature of post IDs on Instagram. After discussing this with the Meta Security team, they clarified that these IDs are not purely random; rather, they are derived from the media IDs through some form of calculation or hashing algorithm. Importantly, the team does not view the uniqueness of these post IDs as a security measure. They acknowledge that, with sufficient effort, one could reverse-engineer the algorithm used to transform the media ID into the post ID.

With several attacking accounts and automation to block users or regions (chain piece \[2/3\]), this issue could have led to widespread unauthorized access to private posts.

Ultimately, this issue earned me third place out of a hundred hackers at BountyCon 2022.

# Under the hood  [Link to heading](https://003random.com/posts/meta-bountycon-instagram-writeup/\#under-the-hood)

Meta has several security measures in place that operate at distinct levels. Even if the application allows you to fetch a private piece of media from a different user, you still wouldn’t be able to do so. This is due to a permissions system on a different application level.

This might spark curiosity about how this bug actually worked. It certainly did for me, so I reached out to the Meta team for clarification. They provided the following insights:

The oEmbed endpoint, specifically the mobile user-agent route, had an error case. This error was triggered when a post could not be fetched due to region blocking—when a user specifies that different regions should not be able to view their content. However, the developers decided that embedding should be universally accessible. To address this, they added an exception that uses a superuser account to bypass these restrictions and fetch the post content anyway.

Only two places in the entire codebase utilized this superuser account, which highlights the uniqueness of finding all pieces of this chain and making it work.

## Timeline  [Link to heading](https://003random.com/posts/meta-bountycon-instagram-writeup/\#timeline)

- \[ **20 Sep 2022**\] Initial Report Submission & same day triaged
- \[ **25 Sep 2022**\] $10,000 bounty
- \[ **25 Sep 2022**\] $2,000 event bonus
- \[ **25 Sep 2022**\] $2,500 additional event bonus (special scope)
- \[ **09 Nov 2022**\] Permission to disclose

Info


Disclaimer: The content presented in this blog post is intended solely for educational and informational purposes. The techniques and methods described were executed and are being disclosed with explicit permission from Meta Platforms, Inc. The vulnerability outlined has already been fixed. Unauthorized access to private information is against the law and unethical. This information should not be used to exploit or breach the privacy of individuals on Instagram or any other platform. The author and publisher disclaim any liability for any misuse of the information provided.
