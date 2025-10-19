---
date: '2025-10-19'
description: '**GlassWorm: VS Code Worm Utilizing Invisible Unicode for Stealthy Malware
  Distribution** Koi''s research identifies GlassWorm as the first self-propagating
  worm targeting VS Code extensions, employing innovative "invisible" Unicode techniques
  to embed malicious code undetected. Its command-and-control infrastructure leverages
  the Solana blockchain and Google Calendar for robust persistence and evasion, enabling
  continuous updates and anonymity. The worm harvests credentials to compromise other
  extensions and drains cryptocurrency wallets, effectively turning infected developer
  machines into SOCKS proxies and hidden remote access points. With early indicators
  signaling 10,711 downloads among affected users, enterprises are facing unprecedented
  supply chain risks as the malware autonomously spreads across the ecosystem.'
link: https://www.koi.ai/blog/glassworm-first-self-propagating-worm-using-invisible-code-hits-openvsx-marketplace
tags:
- vscode_extensions
- cryptocurrency_theft
- malware
- supply_chain_attack
- remote_access_trojan
title: 'GlassWorm: First Self-Propagating Worm Using Invisible Code Hits OpenVSX Marketplace
  ◆ Koi Blog'
---

[![](https://cdn.prod.website-files.com/67bf17e426d92bdda54af956/68b916d6f509af522a34c3a3_Arrow%20blsck.svg)\\
Back](https://www.koi.ai/blog)

Koi Research

### GlassWorm: First Self-Propagating Worm Using Invisible Code Hits OpenVSX Marketplace

![](https://cdn.prod.website-files.com/689ad8c5d13f40cf59df0e0c/689ae130dd9894b4cba4a350_Idan.avif)![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

Idan Dardikman

,

,

October 18, 2025

![](https://cdn.prod.website-files.com/689ad8c5d13f40cf59df0e0c/68f3baf1aa98c1dc465db9c3_image-glassworm.png)

A month after [Shai Hulud](https://www.koi.ai/incident/shai-hulud-npm-supply-chain-attack-crowdstrike-tinycolor) became the first self-propagating worm in the npm ecosystem, we just discovered the world's first worm targeting VS Code extensions on OpenVSX marketplace.

But GlassWorm isn't just another supply chain attack. It's using stealth techniques we've never seen before in the wild - invisible Unicode characters that make malicious code literally disappear from code editors. Combine that with blockchain-based C2 infrastructure that can't be taken down, Google Calendar as a backup command server, and a full remote access trojan that turns every infected developer into a criminal proxy node.

This is one of the most sophisticated supply chain attacks we've ever analyzed. And it's spreading right now.

![](https://cdn.prod.website-files.com/689ad8c5d13f40cf59df0e0c/68f3baf1aa98c1dc465db9c3_image-glassworm.png)

GlassWorm - puts millions at risk

What GlassWorm does to infected systems:

- Harvests NPM, GitHub, and Git credentials for supply chain propagation
- Targets 49 different cryptocurrency wallet extensions to drain funds
- Deploys SOCKS proxy servers, turning developer machines into criminal infrastructure
- Installs hidden VNC servers for complete remote access
- Uses stolen credentials to compromise additional packages and extensions, spreading the worm further

**The current state:** Seven OpenVSX extensions compromised on October 17, 2025. Total downloads -10,711. Five extensions still **actively distributing malware** as you read this. The attacker's C2 infrastructure is fully operational - payload servers are responding, and stolen credentials are being used to compromise additional packages.

The attack went live yesterday. The infrastructure is active. The worm is spreading.

## What Our Risk Engine Detected

Here's how this whole thing started. Our risk engine at Koi flagged an OpenVSX extension called CodeJoy when version 1.8.3 introduced some suspicious behavioral changes. When our researchers dug into it - like we do with any malware our risk engine flags - what we found was very disturbing.

![](https://cdn.prod.website-files.com/689ad8c5d13f40cf59df0e0c/68f3c5e85b905db9b788053e_Screenshot%202025-10-18%20at%2019.52.45.png)

CodeJoy risk report on Koidex

CodeJoy looked legitimate. A developer productivity tool with hundreds of downloads, regular updates, seemingly normal code. But our risk engine caught something that human code review would miss entirely: suspicious network connections and credential access patterns that had nothing to do with the extension's productivity features

So we opened up the source code to take a closer look.

And that's when we saw it. Or rather, didn't see it.

## The Invisible Attack: Unicode Stealth Technique

Look at this screenshot of the CodeJoy extension's source code:

![](https://cdn.prod.website-files.com/689ad8c5d13f40cf59df0e0c/68f3bc6082d343819606a199_file1.png)

Invisible malicious code inCodeJoy's version 1.8.3

See that massive gap between lines 2 and 7? That's not empty space. That's malicious code. Encoded in unprintable Unicode characters that literally don't render in your code editor.

Let me say that again: the malware is invisible. Not obfuscated. Not hidden in a minified file. Actually invisible to the human eye.

The attacker used Unicode variation selectors - special characters that are part of the Unicode specification but don't produce any visual output. To a developer doing code review, it looks like blank lines or whitespace. To static analysis tools scanning for suspicious code, it looks like nothing at all. But to the JavaScript interpreter? It's executable code.

This is why we call it GlassWorm. Like glass, it's completely transparent. You can stare right at it and see nothing. The developer whose account got compromised probably looked at this file, saw what appeared to be their legitimate code, and had no idea they were about to distribute malware to hundreds of users.

Here's the thing - this technique completely breaks traditional code review. You can't spot what you can't see. GitHub's diff view? Shows nothing suspicious. Your IDE's syntax highlighting? All clear. Manual code inspection? Everything looks normal.

The invisible code technique isn't just clever - it's a fundamental break in our security model. We've built entire systems around the assumption that humans can review code. GlassWorm just proved that assumption wrong.

## Stage 2: The Unkillable C2 - Solana Blockchain

So we decoded the invisible Unicode characters. What do we find inside? Another stage of sophistication that honestly made our jaws drop.

The malware uses the Solana blockchain as its command and control infrastructure.

Read that again. The attacker is using a public blockchain - immutable, decentralized, impossible to take down - as their C2 server.

Here's how it works:

![](https://cdn.prod.website-files.com/689ad8c5d13f40cf59df0e0c/68f3bd6adf65e4092ae2723f_carbon%20(12)%20(1).png)

Solana blockchain points to the next stage

The malware searches the Solana blockchain for transactions from the hardcoded wallet address. When it finds a transaction, it reads the memo field - a place where you can attach arbitrary text to blockchain transactions. Inside that memo? A JSON object with a base64-encoded link to download the next stage.

![](https://cdn.prod.website-files.com/689ad8c5d13f40cf59df0e0c/68f3be28a0f964641d2a35c9_file2.png)

Link to the next stage in the memo of the transaction

Look at that screenshot. That's a real Solana transaction from October 15, 2025 - three days ago. The instruction data contains: `{"link":"aHR0cDovLzIxNy42OS4zLjIxOC9xUUQlMkZKb2kzV0NXU2s4Z2dHSGlTdg=="}`

That base64 string decodes to: `http://217.69.3.218/qQD%2FJoi3WCWSk8ggGHiTdg%3D%3D`

And just like that, the malware knows where to download its next payload.

**Why this is absolutely brilliant (and terrifying):**

- ‍ **Immutable**: Once a transaction is on the blockchain, it can't be modified or deleted. Ever. No takedown requests. No domain seizures. It's there forever. **‍**
- **Anonymous**: Crypto wallets are pseudonymous. Good luck tracing this back to a real person. **‍**
- **Censorship-resistant**: There's no hosting provider to contact, no registrar to pressure, no infrastructure to shut down. The Solana blockchain just... exists. **‍**
- **Legitimate traffic**: Connections to Solana RPC nodes look completely normal. Security tools won't flag it. **‍**
- **Dynamic and cheap**: Want to update your payload? Just post a new transaction. Cost? 0.000005 SOL - less than a penny. The attacker can rotate infrastructure as often as they want for pocket change.

Even if you identify and block the payload URL ( `217.69.3.218` in this case), the attacker just posts a new transaction with a different URL, and all infected extensions automatically fetch the new location. You're playing whack-a-mole with an opponent who has infinite moles and infinite mallets.

This isn't some theoretical attack vector. This is a real-world, production-ready C2 infrastructure that's actively serving malware right now. And there's literally no way to take it down.

## Stage 3: The Credential Harvest

The Solana transaction points to an IP address: `217.69.3.218`. We fetch the URL and get back a massive base64 payload. But it's encrypted. AES-256-CBC encryption with a key I don't have.

So where's the decryption key?

In the HTTP response headers.

![](https://cdn.prod.website-files.com/689ad8c5d13f40cf59df0e0c/68f3bef364dfe9c5e3c3a400_file3.png)

The decryption key hides in the response headers

The attacker is dynamically generating encryption keys per request and passing them in custom HTTP headers. Smart - even if you intercept the encrypted payload, you need to make a fresh request to get the current keys.

We decrypted the payload and started analyzing what it does. This is where GlassWorm's true purpose becomes clear.

![](https://cdn.prod.website-files.com/689ad8c5d13f40cf59df0e0c/68f3c02368fa1d68f75ccade_carbon%20(13)%20(1).png)

GlassWorm hunting for crypto wallets

**The malware is hunting for credentials:**

- **NPM authentication tokens** \- to publish malicious packages
- **GitHub tokens** \- to compromise repositories
- **OpenVSX credentials** \- to inject more extensions
- **Git credentials** \- to push malicious code
- **49 different cryptocurrency wallet extensions** \- targeting MetaMask, Phantom, Coinbase Wallet, and dozens more

![](https://cdn.prod.website-files.com/689ad8c5d13f40cf59df0e0c/68f3c0431df577c3eafe55ea_carbon%20(14)%20(1).png)

GlassWorm staling NPM and OpenVSX credentials

But wait, there's more. Buried in the code, we found something else: a Google Calendar link.

`https://calendar.app.google/M2ZCvM8ULL56PD1d6`

![](https://cdn.prod.website-files.com/689ad8c5d13f40cf59df0e0c/68f3c098af591837be19baac_file4.png)

Strange title for a Google Calendar event right?

The malware reaches out to this Google Calendar event as a backup C2 mechanism. And guess what's in the event title? Another base64-encoded URL pointing to yet another encrypted payload.

The attacker created a Google Calendar event with the title: `aHR0cDovLzIxNy42OS4zLjIxOC9nZXRfem9tYmlfcGF5bG9hZC9xUUQlMkZKb2kzV0NXU2s4Z2dHSGlUdg==`

That decodes to: `http://217.69.3.218/get_zombi_payload/qQD%2FJoi3WCWSk8ggGHiTdg%3D%3D`

Notice the path: `/get_zombi_payload/`

Yeah. "Zombi" as in zombie botnet. The attacker is literally naming their endpoints after what they're turning victims into.

**Why use Google Calendar as backup C2?**

- Free and legitimate (no one's blocking Google Calendar)
- Can be updated anytime by editing the event
- Completely bypasses security controls
- Another unkillable infrastructure piece

So now we have a triple-layer C2 system:

1. **Solana blockchain** (primary, immutable)
2. **Direct IP connection** (217.69.3.218)
3. **Google Calendar** (backup, legitimate service)

If one gets blocked, the others keep working. And all three are nearly impossible to take down.

## Stage 4: ZOMBI - The Nightmare Reveal

We fetch the "zombi\_payload" URL, capture the encryption keys from the headers, decrypt it, and start deobfuscating what turns out to be a massively obfuscated JavaScript payload.

And that's when we realized: this isn't just credential theft. This is a full-spectrum remote access trojan.

GlassWorm's final stage - the ZOMBI module - transforms every infected developer workstation into a node in a criminal infrastructure network. Let me break down what this thing can do, because it's honestly one of the most sophisticated pieces of malware we've analyzed.

![](https://cdn.prod.website-files.com/689ad8c5d13f40cf59df0e0c/68f3c582d011eb1b9668c3da_image-glassworm-zombi.png)

Oh no! the GlassWorm is now a zombi!

### SOCKS Proxy - Your Machine Becomes Criminal Infrastructure

The ZOMBI module can turn your computer into a SOCKS proxy server. Here's the code:

![](https://cdn.prod.website-files.com/689ad8c5d13f40cf59df0e0c/68f3c14c93bcecb4c2f9ed0d_carbon%20(15)%20(1).png)

GlassWorm zombi - turns the workstation into socks server

Your developer workstation - the one sitting inside your corporate network, behind all your firewalls and security controls - just became a proxy node for criminal activity.

**Why this is devastating:**

- **Corporate network access**: Your machine can reach internal systems that external attackers can't
- **Attack anonymization**: Attackers route their traffic through your IP, not theirs
- **Firewall bypass**: Internal machines can access resources external proxies can't reach
- **Free infrastructure**: Why pay for proxy servers when victims provide them?

Every single infected developer becomes a node in a global proxy network. And you won't even know it's happening.

### WebRTC P2P - Direct Peer-to-Peer Control

ZOMBI downloads and deploys WebRTC modules for peer-to-peer communication:

![](https://cdn.prod.website-files.com/689ad8c5d13f40cf59df0e0c/68f3c1ee0e3afe8e1c246623_carbon%20(16)%20(1).png)

WebRTC enables direct peer-to-peer connections that bypass traditional firewalls through NAT traversal. The attacker can establish real-time, direct control channels to infected machines without going through any central server.

### BitTorrent DHT - Decentralized Command Distribution

ZOMBI uses BitTorrent's Distributed Hash Table (DHT) network for command distribution:

![](https://cdn.prod.website-files.com/689ad8c5d13f40cf59df0e0c/68f3c20248283d6de4499b62_carbon%20(17)%20(1).png)

Commands are distributed through the BitTorrent DHT network - the same decentralized system that makes torrent tracking impossible to shut down. There's no central C2 server to take offline. Commands propagate through a distributed network of millions of nodes.

### Hidden VNC (HVNC) - Complete Invisible Remote Control

And here's the truly terrifying part - HVNC (Hidden Virtual Network Computing):

![](https://cdn.prod.website-files.com/689ad8c5d13f40cf59df0e0c/68f3c227d7ca3dac6e8fbe1c_carbon%20(18)%20(1).png)

HVNC gives the attacker complete remote desktop access to your machine - but it's hidden. It runs in a virtual desktop that doesn't appear in Task Manager, doesn't show any windows on your screen, and operates completely invisibly.

The attacker can:

- Use your browser with your logged-in sessions
- Access your email, Slack, internal tools
- Read your source code
- Steal additional credentials
- Pivot to other systems on your network
- Do literally anything you could do - but you'll never see it happening

### The Full Picture

ZOMBI isn't just malware. It's a complete remote access and network penetration toolkit:

- **SOCKS proxy** for routing attacks through victim networks
- **WebRTC P2P** for direct, firewall-bypassing control
- **BitTorrent DHT** for unkillable command distribution
- **HVNC** for invisible remote desktop access
- **Automatic restart** on any failure (it won't go away)
- **Modular architecture** supporting dynamic capability updates

For enterprises, this is a nightmare scenario. An infected developer workstation becomes:

- An internal network access point
- A persistent backdoor
- A proxy for attacking other internal systems
- An exfiltration channel for sensitive data
- A command and control relay point

And it all started with an invisible Unicode character in a VS Code extension.

## The Worm Spreads: Self-Propagation Through Stolen Credentials

Here's where GlassWorm earns the "Worm" part of its name.

Remember all those credentials it's stealing? NPM tokens, GitHub credentials, OpenVSX access? Those aren't just for data theft. They're for propagation.

**The self-replication cycle:**

1. **Initial infection** \- Compromised developer account pushes malicious code to legitimate extension
2. **Invisible payload** \- Unicode-hidden malware executes on victim machines
3. **Credential harvest** \- Steals NPM, GitHub, OpenVSX, Git credentials
4. **Automated spread** \- Uses stolen credentials to compromise MORE packages and extensions
5. **Exponential growth** \- Each new victim becomes an infection vector
6. **Repeat** \- The cycle continues automatically

This isn't a one-off supply chain attack. It's a worm designed to spread through the developer ecosystem like wildfire.

Just one month ago, the security community witnessed Shai Hulud - the first successful self-propagating worm in the npm ecosystem. That campaign compromised over 100 packages by stealing npm tokens and automatically publishing malicious versions.

GlassWorm brings this same technique to OpenVSX, but with terrifying evolutions:

- **Invisible code injection** that bypasses all code review
- **Blockchain-based C2** that can't be taken down
- **Full RAT capabilities** turning victims into criminal infrastructure
- **Multi-layered redundancy** across three different C2 mechanisms

The pattern is clear. Attackers have figured out how to make supply chain malware self-sustaining. They're not just compromising individual packages anymore - they're building worms that can spread autonomously through the entire software development ecosystem.

With traditional supply chain attacks, you compromise one package and that's your blast radius. With worms like Shai Hulud and GlassWorm, each infection is a new launching point for dozens more. It's exponential growth. And we're just starting to see what that looks like.

## Impact: 10,711 Victims, Active RIGHT NOW

Let's talk about the current state of this infection. Because this isn't some theoretical attack or historical incident. GlassWorm is active right now.

**Attack Timeline:**

- **October 17, 2025**: Seven OpenVSX extensions compromised (yesterday)
- **October 18, 2025**: We detected and began analysis (today)
- **Current status**: Five extensions still actively distributing malware

**Total impact: 10,711 installations**

Here's what makes this particularly urgent: VS Code extensions auto-update. When CodeJoy pushed version 1.8.3 with invisible malware, everyone with CodeJoy installed got automatically updated to the infected version. No user interaction. No warning. Just silent, automatic infection.

And since the malware is invisible, the original developers whose accounts were compromised probably had no idea. They might have even reviewed the "empty" lines in their code and seen nothing wrong.

**What's happening right now to infected systems:**

1. **Credential theft in progress** \- NPM tokens, GitHub credentials, Git credentials being harvested
2. **Cryptocurrency wallets being drained** \- 49 different wallet extensions targeted
3. **SOCKS proxies deploying** \- Turning developer workstations into criminal infrastructure
4. **HVNC installation** \- Hidden remote access being established
5. **Network reconnaissance** \- Infected machines mapping internal corporate networks
6. **Preparation for spread** \- Stolen credentials being validated for additional compromises

The C2 infrastructure is fully operational:

- **217.69.3.218** \- Responding and serving encrypted payloads
- **Solana blockchain** \- Transaction active, pointing to payload servers
- **Google Calendar event** \- Live and accessible
- **Exfiltration server** (140.82.52.31) - Collecting stolen data

This is an active, ongoing compromise. Not a case study. Not a war story. This is happening right now, as you read this sentence.

If you have any of the infected extensions installed, you're compromised. Your credentials are likely stolen. Your crypto wallets may be drained. Your machine might already be serving as a SOCKS proxy for criminal activity. And you probably have no idea any of this is happening.

Two developers managed to push clean updates (vscode-theme-seti-folder and git-worktree-menu), suggesting they either regained access to their accounts or noticed something was wrong. But five extensions are still infected. Five developers who either don't know they're compromised or can't regain control of their accounts.

And remember: this is just what we've found so far. GlassWorm is designed to spread. Those stolen credentials are being used right now to compromise additional packages and extensions. The real victim count could be much higher.

## Final Thoughts

This writeup was authored by the research team at **Koi Security**, with a healthy dose of paranoia and hope for a safer open-source ecosystem.

GlassWorm shows how easy it is for malicious extensions to slip past marketplace security and compromise sensitive data. With Koi, security teams gain visibility, risk scoring, and governance across binary & non-binary software before it ever hits production.

[Book a demo](https://www.koi.security/get-a-demo) to see how Koi closes the gap that legacy tools miss.

For too long, the use of untrusted third-party code, often running with the highest privileges has flown under the radar for both enterprises and attackers. That era is ending. The tide is shifting. Just last month we uncovered another campaign of [18 featured and verified extensions that turned malicious](https://www.koi.security/blog/google-and-microsoft-trusted-them-2-3-million-users-installed-them-they-were-malware) and affected millions of users.

We’ve built Koi to meet this moment; for practitioners and enterprises alike. Our platform helps discover, assess, and govern everything your teams pull from marketplaces like the Chrome Web Store, VSCode, Hugging Face, Homebrew, GitHub, and beyond.

Trusted by Fortune 50 organizations, BFSIs and some of the largest tech companies in the world, Koi automates the security processes needed to gain visibility, establish governance, and proactively reduce risk across this sprawling attack surface.

Because in a world where malware can be literally invisible, paranoia isn't a bug - it's a feature.

Stay safe out there.

## IOCs

### Compromised Extensions

**OpenVSX Extensions (with malicious versions):**

- codejoy.codejoy-vscode-extension@1.8.3
- codejoy.codejoy-vscode-extension@1.8.4
- l-igh-t.vscode-theme-seti-folder@1.2.3
- kleinesfilmroellchen.serenity-dsl-syntaxhighlight@0.3.2
- JScearcy.rust-doc-viewer@4.2.1
- SIRILMP.dark-theme-sm@3.11.4
- CodeInKlingon.git-worktree-menu@1.0.9
- CodeInKlingon/git-worktree-menu@1.0.91
- ginfuru.better-nunjucks@0.3.2

### Infrastructure

**Command & Control:**

- `217.69.3.218` (primary C2 server)
- `140.82.52.31:80/wall` (exfiltration endpoint)

**Blockchain Infrastructure:**

Solana Wallet: `28PKnu7RzizxBzFPoLp69HLXp9bJL3JFtT2s5QzHsEA2`

Transaction: `49CDiVWZpuSW1b2HpzweMgePNg15dckgmqrrmpihYXJMYRsZvumVtFsDim1keESPCrKcW2CzYjN3nSQDGG14KKFM`

**Google Calendar C2:**

`https://calendar.app.google/M2ZCvM8ULL56PD1d6`

Organizer: `uhjdclolkdn@gmail.com`

**Payload URLs:**

`http://217.69.3.218/qQD%2FJoi3WCWSk8ggGHiTdg%3D%3D`

`http://217.69.3.218/get_arhive_npm/`

`http://217.69.3.218/get_zombi_payload/qQD%2FJoi3WCWSk8ggGHiTdg%3D%3D`

### Registry Indicators

**Persistence Mechanisms:**

`HKCU\Software\Microsoft\Windows\CurrentVersion\Run`

`HKLM\Software\Microsoft\Windows\CurrentVersion\Run`

share

Copied to clipboard

### Be the first to know

Fresh research and updates on software risk and endpoint security.

![](https://cdn.prod.website-files.com/67bf17e426d92bdda54af956/6836d87262e4ca8706e98a77_coud01.svg)![](https://cdn.prod.website-files.com/67bf17e426d92bdda54af956/689d8cd8db647692730041cf_ship.avif)![](https://cdn.prod.website-files.com/67bf17e426d92bdda54af956/6836d873d735542d459f0382_cloud02.svg)

Thanks for subscribing!

## related blogs

Koi Research

![](https://cdn.prod.website-files.com/689ad8c5d13f40cf59df0e0c/68ebd7a78094ed5a4eb334fc_image-tigerjack.png)

### TigerJack's Extensions Continue to Rob Developers Blind Across Different Marketplaces

![](https://cdn.prod.website-files.com/689ad8c5d13f40cf59df0e0c/689db2bbf506d1e75461240a_Tuval.avif)![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

Tuval Admoni

,

,

October 13, 2025

[current post link](https://www.koi.ai/blog/tiger-jack-malicious-vscode-extensions-stealing-code)

Koi Research

![](https://cdn.prod.website-files.com/689ad8c5d13f40cf59df0e0c/68e8530de19b4218f17980df_image-figma-mcp.png)

### Command Injection Flaw in Framelink Figma MCP Server Puts Nearly 1 Million Downloads at Risk

![](https://cdn.prod.website-files.com/689ad8c5d13f40cf59df0e0c/68a433090a6d7347126e14b1_Koi%20Headshots-7945.avif)![](https://cdn.prod.website-files.com/689ad8c5d13f40cf59df0e0c/689ae130dd9894b4cba4a350_Idan.avif)![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

Lotan Sery

,

Idan Dardikman

,

October 10, 2025

[current post link](https://www.koi.ai/blog/command-injection-flaw-in-framelink-figma-mcp-server-puts-nearly-1-million-downloads-at-risk)

Koi Research

![](https://cdn.prod.website-files.com/689ad8c5d13f40cf59df0e0c/68dc1b5ab0962510f7957103_shark.png)

### MCP Malware Wave Continues: A Remote Shell in Disguise

![](https://cdn.prod.website-files.com/689ad8c5d13f40cf59df0e0c/689db2bbf506d1e75461240a_Tuval.avif)![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

Tuval Admoni

,

,

September 30, 2025

[current post link](https://www.koi.ai/blog/mcp-malware-wave-continues-a-remote-shell-in-backdoor)
