---
date: '2025-09-12'
description: The article provides an in-depth guide on mastering Caido, a Rust-based
  web security toolkit, emphasizing its usability, speed, and customization. Key features
  compared to Burp Suite include a more efficient project management system, versatile
  CLI and desktop versions, and advanced functionalities like intercepting requests/responses
  and workflows. HTTPQL allows tailored request filtering, essential for efficient
  auditing. The article highlights community-driven plugins that enhance functionality,
  such as integrated AI tools and customized scanning. Overall, Caido offers a lightweight,
  open-source alternative, suitable for penetration testers and security researchers
  seeking flexibility and community support.
link: https://aituglo.com/caido/
tags:
- HTTPQL
- Bug Bounty
- Web Security
- Burp Suite
- Caido
title: 'Caido 101: How to master it'
---

![Caido 101: How to master it](https://aituglo.com/content/images/size/w1216/2025/09/CleanShot-2025-09-11-at-14.10.53.png)

#### Table of contents

1. [Getting Started](https://aituglo.com/caido/#getting-started)
1. [Coming from Burp](https://aituglo.com/caido/#coming-from-burp)
2. [CLI vs Desktop](https://aituglo.com/caido/#cli-vs-desktop)
3. [Scope](https://aituglo.com/caido/#scope)
4. [Intercept](https://aituglo.com/caido/#intercept)
5. [Match & Replace](https://aituglo.com/caido/#match-replace)
6. [Replay](https://aituglo.com/caido/#replay)
7. [Automate](https://aituglo.com/caido/#automate)
8. [Findings](https://aituglo.com/caido/#findings)
2. [Getting Pro](https://aituglo.com/caido/#getting-pro)
1. [Tips](https://aituglo.com/caido/#tips)
2. [Community](https://aituglo.com/caido/#community)
3. [HTTPQL](https://aituglo.com/caido/#httpql)
4. [Workflows](https://aituglo.com/caido/#workflows)
5. [Plugins](https://aituglo.com/caido/#plugins)
6. [AuthMatrix](https://aituglo.com/caido/#authmatrix)
3. [Final thoughts](https://aituglo.com/caido/#final-thoughts)
1. [Recommendations](https://aituglo.com/caido/#)

As a daily user of Caido, I wanted to show you how you can also master it and discover it if you're a Burp user.

## Getting Started

This part will mostly be for people who come from Burp. I will mostly focus on the functionalities and not on how to install it. If you need this part, here is the main tutorial to install it :

[Welcome to Caido! \| Documentation\\
\\
Official Caido Documentation\\
\\
![](https://aituglo.com/content/images/icon/favicon.png)Documentation\\
\\
![](https://aituglo.com/content/images/thumbnail/logo.png)](https://docs.caido.io/quickstart/?ref=aituglo.com)

Main Documentation

### Coming from Burp

Being a Burp user will not lose you, as the main stuff is quite the same in both; the names are just different. Here are some name changes :

- Repeater -> Replay
- Intruder -> Automate

The first nice key point is that you can simply create and manage projects without reloading or relaunching the app. This way, you can add a new project and switch between them pretty quickly.

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-09-at-14.01.51.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-09-at-14.01.51.png) Caido Workspaces

And as Caido is written in Rust, it's pretty fast and light. You don't need as much RAM as you would need for Burp.

### CLI vs Desktop

Caido comes with two versions: a Desktop one and a CLI one. And this is pretty useful if you want to install Caido on a server and then use it on the browser directly.

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-09-at-14.42.56.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-09-at-14.42.56.png) CLI vs Desktop

This way, you can have your full proxy on an external server, and connect to it on any machine. Pretty useful to keep your files somewhere else, and launch big scans when your computer is closed.

### Scope

Looking at the scope, it's straightforward, and you can manage different presets by project.

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-09-at-14.08.40.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-09-at-14.08.40.png)

### Intercept

The Intercept tab is also quite different and easy to use. You can directly catch the Responses, Requests, and Websockets and modify them on the fly.

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-09-at-14.13.53.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-09-at-14.13.53.png) Intercept Tab

This way, you can view all the requests and responses on each pane and choose which one you want to modify or drop. You can also filter them using HTTPQL, but we will see that later in this article.

### Match & Replace

It's so easy in Caido to get a Match & Replace. You can add a new header, replace something in the response, and use workflows for the replacer, which means something totally custom.

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-09-at-14.26.14.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-09-at-14.26.14.png) Match & Replace

As an example, you can match on a token and pass it to a specific workflow to modify it. Everything is possible using workflows, as you can write your custom JavaScript code or bash script. Here are some examples you can make :

- Add a specific header or update it based on previous requests
- Replace in the response or the request to check injection points
- Remove useless headers
- Put a value on a workflow that will transform it, like a text field that you want to base64, and then hash it, for instance

You can also use HTTPQL to filter on which request you want to replace. And put rules on different collections to make them well-organized.

If you want to dig more about that, here is the specification :

[Match & Replace \| Documentation\\
\\
Official Caido Documentation\\
\\
![](https://aituglo.com/content/images/icon/favicon-3.png)Documentation\\
\\
![](https://aituglo.com/content/images/thumbnail/logo-3.png)](https://docs.caido.io/reference/match_replace.html?ref=aituglo.com)

### Replay

Here, you can manage your replay tabs, and it's way better than in Burp because you can put them in different collections to organize them, and also you can close all of them; they will still be there on the pane.

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-09-at-14.36.22.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-09-at-14.36.22.png) Replay

Quick tips: If you're getting used to your shortcut in Burp, you can easily put the same in Caido in the settings to sharpen your workflow.

### Automate

This is quite the same as the Intruder in Burp. You add your placeholders, and you launch a mass request. You can download files on your caido for the payload. And you can use a Workflow as a preprocessor, which can be pretty useful for something very custom.

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-09-at-14.40.18.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-09-at-14.40.18.png) Automate

### Findings

It's the way to highlight a request with a text to a finding. It's pretty useful with plugins and workflow when you can highlight a specific request and keep it for later.

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-09-at-15.16.45.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-09-at-15.16.45.png) Findings

## Getting Pro

Here, we're going to see some tips and tricks and the best plugins to use at this time. Everything we've seen can look basic, and yes, it is. But the way you use it will totally change.

As Caido is very customizable, that's where you will be able to make the shift. By creating your own stuff, you will make something that perfectly fits your workflow.

### Tips

To navigate easily through Caido, you can use the command with Cmd+K

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-09-at-14.52.27.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-09-at-14.52.27.png) Command

This way, you can execute workflows or navigate to a tab using only the keyboard. In the settings of Caido, you can also directly set a shortcut for each Workflow or Plugin. So you can convert any text to another, like base64decode, with a shortcut of your choice.

### Community

The force of Caido is the fact that most of the stuff is open source and simple to create or modify. And the team listens to us a lot. Join the Discord Server, and you will see that you will get help for any issue.

[Join the Caido Discord Server!\\
\\
A lightweight web security auditing toolkit \| 3281 members\\
\\
![](https://aituglo.com/content/images/icon/favicon-2.ico)Discord\\
\\
![](https://aituglo.com/content/images/thumbnail/b6100fa3879f7812fb9fb091c933210a.jpg)](https://discord.com/invite/caido-843915806748180492?ref=aituglo.com)

They are working in a way that anyone can create an issue on the Caido Github to ask for new features, and they will build them based on the likes on the issues, so they listen to the community and they build them fast. We have a new update almost every week.

[Caido\\
\\
Caido has 90 repositories available. Follow their code on GitHub.\\
\\
![](https://aituglo.com/content/images/icon/pinned-octocat-093da3e6fa40-9.svg)GitHub\\
\\
![](https://aituglo.com/content/images/thumbnail/78991750)](https://github.com/caido?ref=aituglo.com)

### HTTPQL

This is the filter language of Caido, and it's very easy to learn. You will see it in a lot of different features, and you can create Filters.

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-09-at-15.32.23.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-09-at-15.32.23.png) Filters

So in this simple example, this is a filter that will check the extension of the request and not accept requests that are styling.

You can also use them on the HTTP History to simply filter which requests you want to see or not

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-09-at-15.34.09.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-09-at-15.34.09.png) Custom filter

You can almost filter by anything very useful when trying to find something you viewed previously

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-09-at-15.34.45.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-09-at-15.34.45.png)

Here is the full documentation for HTTPQL, play with it :

[HTTPQL \| Documentation\\
\\
Official Caido Documentation\\
\\
![](https://aituglo.com/content/images/icon/favicon-2.png)Documentation\\
\\
![](https://aituglo.com/content/images/thumbnail/logo-2.png)](https://docs.caido.io/reference/httpql.html?ref=aituglo.com)

### Workflows

That's the easiest way to create your own stuff without being technical. With that, you can simply move nodes and create something cool.

You have different types of Workflows :

- Active, to set an action on a request, like asking an AI or checking for CORS misconfiguration
- Passive, that will run in the background, like checking for reflections
- Convert is used to convert something to something else, like base 64 or URL encoding.

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-10.37.33.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-10.37.33.png) Pwnfox workflow

It's very easy to understand and to build your own, and you have nodes like JavaScript or Shell that can be helpful to pipe caido to your external tools.

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-10.38.16.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-10.38.16.png) Different nodes

Also, there is a Workflows Store that is a plugin. With that, you have a bunch of workflows made by the community to start building and automating your workflows.

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-10.39.15.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-10.39.15.png) Workflow examples

It's very powerful, as you can simply make one that fits your needs in minutes.

### Plugins

I will now tell more about some plugins I'm using every day. And if you like to dev, go develop your own. As they are written in Typescript with a great SDK, it's super easy to create your own.

Here is the documentation to develop your own :

[Caido \| Developer\\
\\
Official Caido Developer Documentation\\
\\
![](https://aituglo.com/content/images/icon/favicon-4.png)Developer\\
\\
![](https://aituglo.com/content/images/thumbnail/logo-4.png)](https://developer.caido.io/?ref=aituglo.com)

And with this command, you will get the basic plugin architecture :

_pnpm create @caido-community/plugin_

Give that to Claude or Cursor with the SDK, and the AI will make any plugin you want.

Otherwise, you can view all the plugins by the community on the plugin tab

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-13.37.27.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-13.37.27.png) Plugin list

#### EvenBetter

This is a plugin made by bebiks, who is the goat of Caido. He made a lot of great plugins, and he is now part of the team. A huge thanks to him for his work on the project.

This one is quite simple but very helpful as it will add a few features

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-13.31.41.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-13.31.41.png)

My favourite one is the exclude path that will add a custom HTTPQL rule to avoid seeing this path or host again, useful to have something clear.

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-13.32.21.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-13.32.21.png)

Another one is the auto-encode and decode on the Replay tab

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-13.33.27.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-13.33.27.png)

### AuthMatrix

This is the equivalent of Authorize or AuthAnalyzer on Burp. Quite useful to check improper access control and IDORs.

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-13.37.53.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-13.37.53.png)

#### Quick SSRF

This is the equivalent of the Collaborator, and as it uses the same technology as the Collaborator, you can use it the same way, even for protocols like SMTP.

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-13.38.51.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-13.38.51.png)

#### Param Finder

Same as the one on Burp, but this time, it's fully customizable. You can add your own wordlist and settings, which will be helpful to find ones that others can't find.

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-13.42.59.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-13.42.59.png)

#### Ebka AI

Made by Slonser, this is an MCP for Caido. It's amazing as you can now connect your full Caido to your Claude.

This was,y you can ask to create a replay tab, launch them, search for vulnerabilities, create findings, and even create Match & Replace rules for you.

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-13.44.12.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-13.44.12.png)

#### Notes++

A perfect way to get all your notes on Caido. You don't need any other tool now, as you can save your notes in Markdown, attach the Replay tab to them, and organize yourself based on your target.

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-13.45.37.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-13.45.37.png)

#### Shift & Shift Agents

Add AI to your Caido. One of the best features is the auto-rename for your Replay tabs based on a prompt.

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-13.47.55.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-13.47.55.png)

Also, with the Shift Agents, you can get a full chat with agents to manage your Caido. Give it a try.

#### 403 Bypasser

Customizable as well with your own templates, with the base template from Burp, and very easy to add a new template.

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-13.53.54.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-13.53.54.png)

#### Drop

My favourite one to collab. With that, you can add your friends, and drop them Replay tabs, Match & Replace rules, presets, and so on.

It works smoothly, and you can send a lot of stuff to your friends directly on their caido instance without having to send the whole request on Discord or something else.

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-13.59.02.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-13.59.02.png)

#### Scanner

A lot of people were missing the Burp Scanner, and we do have it now. It's still in Beta, and it's not as well as the Burp one, but it will be collaborative, and anyone will be able to add a new scan, so in the long run, it can be way more productive.

[![](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-14.00.30.png)](https://aituglo.com/content/images/2025/09/CleanShot-2025-09-11-at-14.00.30.png)

There are a lot more plugins to try, and the community is building new ones every week, so check the Discord and X to get the latest news.

## Final thoughts

Obviously, if you're getting used to Burp, just try it; it's cheaper than Burp, and you can try it for a month and see if it can fit your needs.

Also, using both can be quite useful as Caido doesn't support stuff like Request Smuggling or Timing Attacks. So you can build your own plugins and run a Caido on a server that will be upstream from your Burp instance, and you will get the best of everything.

The thing that I love the most about Caido is the fact that it is fast, you can build stuff on your own easily, and you can ask the developers about new features. If you have any questions about Caido, go ask them directly on the Discord, and if it's about this article, feel free to ask me.

[Share on Facebook](https://www.facebook.com/sharer.php?u=https://aituglo.com/caido/ "Share on Facebook")[Share on Twitter](https://twitter.com/intent/tweet?url=https://aituglo.com/caido/&text=Caido%20101%3A%20How%20to%20master%20it "Share on Twitter")[LinkedinA solid styled icon from Orion Icon Library.](https://www.linkedin.com/shareArticle?mini=true&url=https://aituglo.com/caido/&title=Caido%20101%3A%20How%20to%20master%20it "Share on LinkedIn") [Link copied](https://aituglo.com/caido/# "Copy URL")

![Aituglo](https://www.gravatar.com/avatar/4dbb84befeed0347286551a960b7f63e?s=250&r=x&d=mp)

The author of this blog, a bug bounty hunter and security researcher that shares his thoughts about the art of hacking.

[Explore website](https://aituglo.com/ "Explore website")[Follow on X](https://twitter.com/@aituglo "Follow on X")

### Recommendations

- [![Mizu’s website](https://mizu.re/favicon.png)\\
**Mizu’s website** mizu.re](https://mizu.re/)
- [![Geluchat’s Blog](https://static.ghost.org/v5.0.0/images/link-icon.svg)\\
**Geluchat’s Blog** gelu.chat\\
Geluchat’s blog - Bug Hunter & Security Researcher](https://gelu.chat/)

Follow

StripeM-Inner
