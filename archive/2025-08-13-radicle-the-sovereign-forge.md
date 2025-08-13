---
date: '2025-08-13'
description: Radicle is a decentralized, peer-to-peer code collaboration platform
  built on Git, emphasizing user autonomy and data control. It enables users to host
  their own nodes, fostering censorship resistance and resilience. The latest release,
  Radicle 1.3.0, introduces a graphical desktop client, enhancing collaborative coding
  experiences. With a modular structure, Radicle supports diverse client implementations
  and local-first functionality, ensuring availability offline. The system employs
  cryptographic identities for data authenticity and uses a gossip protocol for efficient
  metadata exchange. This architecture aligns with the growing trend toward decentralized
  software development and self-managed data.
link: https://radicle.xyz/
tags:
- Radicle
- peer-to-peer
- open source
- Git
- decentralized
title: 'Radicle: the sovereign forge'
---

![](https://radicle.xyz/assets/images/ribbon.svg)

**Radicle** is a sovereign
{code forge} built on Git.


> Radicle Desktop is now available. Read the [announcement](https://radicle.xyz/2025/06/13/radicle-desktop.html). ✨

# Synopsis

Radicle is an open source, peer-to-peer code collaboration stack built on Git.
Unlike centralized code hosting platforms, there is no single entity
controlling the network. Repositories are replicated across peers in a
decentralized manner, and users are in full control of their data and workflow.

[![](https://radicle.xyz/assets/images/web-app-screenshot.png)](https://app.radicle.xyz/nodes/seed.radicle.xyz/rad:z3gqcJUoA1n9HaHKufZs5FCSGazv5 "Heartwood is the latest generation of the Radicle protocol")
The Radicle `heartwood` repository. Repository ID
`rad:z3gqcJUoA1n9HaHKufZs5FCSGazv5`.

# Get started

> 💾
>  [Radicle 1.3.0](https://files.radicle.xyz/releases/latest)· 0e48723b419be95340a5d9858d76963e8e97137b(Tue, 12 Aug 2025 10:13:49 GMT)

To install Radicle, simply run the command below from your shell, or go to the
[download](https://radicle.xyz/download) page.

`curl -sSf https://radicle.xyz/install | sh`

Alternatively, you can build from [source](https://app.radicle.xyz/nodes/seed.radicle.xyz/rad:z3gqcJUoA1n9HaHKufZs5FCSGazv5).

For now, Radicle only works on Linux, macOS and BSD variants.

[Follow the guide →](https://radicle.xyz/guides/user)

## Radicle Desktop 🖥️

For a graphical collaborative experience check out the [Radicle Desktop client](https://radicle.xyz/desktop), as well.

# How it works

The Radicle protocol leverages cryptographic identities for code and social
artifacts, utilizes Git for efficient data transfer between peers, and employs
a custom gossip protocol for exchanging repository metadata.

[Learn more →](https://radicle.xyz/guides/protocol)

## Your Data, Forever and Secure

All social artifacts are stored in Git, and signed using public-key
cryptography. Radicle verifies the authenticity and authorship of all data
for you.

## Unparalleled Autonomy

Radicle enables users to run their own nodes, ensuring censorship-resistant
code collaboration and fostering a resilient network without reliance on
third-parties.

## Local-first

Radicle is [local-first](https://www.inkandswitch.com/local-first/), providing always-available functionality even
without internet access. Users own their data, making migration, backup, and
access easy both online and offline.

## Evolvable & Extensible

Radicle’s [Collaborative Objects](https://radicle.xyz/guides/protocol#collaborative-objects) (COBs) provide Radicle’s _social_
_primitive_. This enables features such as issues, discussions and code review
to be implemented as Git objects. Developers can extend Radicle’s capabilities
to build any kind of collaboration flow they see fit.

## Modular by Design

The Radicle Stack comes with a CLI, web interface and TUI, that are backed by
the Radicle Node and HTTP Daemon. It’s modular, so any part can be swapped out
and other clients can be developed.

```
┌─────────────────┐┌────────────────┐
│  Radicle CLI    ││ Radicle Web    │
└─────────────────┘└────────────────┘
┌───────────────────────────────────┐
│  Radicle Repository               │
│ ┌────────┐ ┌────────┐ ┌─────────┐ │
│ │  code  │ │ issues │ │ patches │ │
│ └────────┘ └────────┘ └─────────┘ │
├───────────────────────────────────┤
│  Radicle Storage (Git)            │
└───────────────────────────────────┘
┌────────────────┐┌─────────────────┐
│  Radicle Node  ││  Radicle HTTPD  │
├────────────────┤├─────────────────┤
│    NoiseXK     ││   HTTP + JSON   │
└────────────────┘└─────────────────┘

```

[Browse our repositories ↗](https://app.radicle.xyz/nodes/seed.radicle.xyz)

# Contributing

Radicle is _free and open source_ software under the MIT and Apache 2.0
licenses. Get involved by [contributing code](https://app.radicle.xyz/nodes/seed.radicle.xyz/rad:z3gqcJUoA1n9HaHKufZs5FCSGazv5/tree/CONTRIBUTING.md).

# Updates

**Follow us** on 🐘 [Mastodon](https://toot.radicle.xyz/@radicle), 🦋 [Bluesky](https://bsky.app/profile/radicle.xyz) or 🐦 [Twitter](https://twitter.com/radicle) to stay
updated, join our community on 💬 [Zulip](https://radicle.zulipchat.com/), or [Subscribe ![RSS logo](https://radicle.xyz/assets/images/rss.svg)](https://radicle.xyz/feed.xml)

- 12.08.2025 [Radicle 1.3.0](https://radicle.xyz/2025/08/12/radicle-1.3.0.html) released. ✨
- 17.07.2025 [Radicle 1.2.1](https://radicle.xyz/2025/07/17/radicle-1.2.1.html) released. ✨
- 13.06.2025 [Radicle Desktop](https://radicle.xyz/2025/06/13/radicle-desktop.html) is out. 🖥️
- 02.06.2025 [Radicle 1.2](https://radicle.xyz/2025/06/02/radicle-1.2.html) released. ✨
- 05.12.2024 [Radicle 1.1](https://radicle.xyz/2024/12/05/radicle-1.1.html) released. ✨
- 10.09.2024 [Radicle 1.0](https://radicle.xyz/2024/09/10/radicle-1.0.html) is out.
- 26.03.2024 [Radicle 1.0.0-rc.1](https://twitter.com/radicle/status/1772659708978991605) released.
- 10.03.2024 New Radicle homepage.
- 05.03.2024 [Radicle Guides](https://radicle.xyz/guides) launch.
- 05.03.2024 [Radicle makes it to the top of Hacker News](https://news.ycombinator.com/item?id=39600810)!
- 18.04.2023 [Radicle heartwood is announced](https://x.com/radicle/status/1648336186862194693?s=20).

## Blog

- 12.08.2025 [Canonical References](https://radicle.xyz/2025/08/12/canonical-references.html) released. ✨
- 23.07.2025 [Using Radicle CI for Development](https://radicle.xyz/2025/07/23/using-radicle-ci-for-development.html)
- 30.05.2025 [How we used Radicle with GitHub Actions](https://radicle.xyz/2025/05/30/radicle-with-github-actions.html)

# Feedback

If you have feedback, join our [Zulip](https://radicle.zulipchat.com/) or send us an email at
[feedback@radicle.xyz](mailto:feedback@radicle.xyz). Emails sent to this
address are automatically posted to our [#feedback](https://radicle.zulipchat.com/#narrow/channel/392584-feedback)
channel on Zulip.

```
                                             .

                                                   *
                        .
              *                              --O--
                                              /|\
                 ,                     .
                                           .
..-.--*--.__-__..._.--..-._.---....~__..._.--..~._.---.--..____.--_--'`_---..
       -.--~--._  __..._.--..~._.--- - -.____.--_--'`_---..~.----_~

                                    .--..~._
                  -.-
                                 .-.        .

```
