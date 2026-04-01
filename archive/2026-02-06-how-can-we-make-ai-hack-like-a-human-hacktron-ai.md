---
date: '2026-02-06'
description: Hacktron CLI has entered beta, providing a platform for AI-driven vulnerability
  discovery. Leveraging cognitive research, the framework emphasizes a modular approach
  akin to Marvin Minsky’s "Society of Mind," enabling AI agents to adopt specialized
  roles like “coding” and “hacking.” Key insights include treating vulnerability discovery
  as adversarial theorem proving, where reasoning about complex system interactions
  takes precedence over memorization. The system aspires to abstract complexity and
  simulate failures, facilitating the identification of deep, semantic vulnerabilities.
  This approach aims to revolutionize automated hacking, pushing the boundaries of
  AI capabilities in cybersecurity.
link: https://www.hacktron.ai/blog/how-ai-can-hack
tags:
- vulnerability-discovery
- hacking
- cybersecurity
- AI
- Hacktron
title: How can we make AI hack like a human? ◆ Hacktron AI
---

The Hacktron CLI is now in beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in beta! [Start for free](https://app.hacktron.ai/signup)

The Hacktron CLI is now in beta! [Start for free](https://app.hacktron.ai/signup)

⬡▲⬨⧫▲⧫⬡▲◇

⣦⣄⣀⣀⣤⣶⣷⣷⣦

▂▄▆█▆▄▂▄▆

◑◎◉◑◑◎◉◉◉

Overview

- [Magic, or just a lack of understanding?](https://www.hacktron.ai/blog/how-ai-can-hack#magic-or-just-a-lack-of-understanding)
- [How does the hacking agent in my brain work?](https://www.hacktron.ai/blog/how-ai-can-hack#how-does-the-hacking-agent-in-my-brain-work)
- [Formalizing hacking & the science of insecurity](https://www.hacktron.ai/blog/how-ai-can-hack#formalizing-hacking--the-science-of-insecurity)
- [Limits of security and the danger of AI](https://www.hacktron.ai/blog/how-ai-can-hack#limits-of-security-and-the-danger-of-ai)
- [Vulnerability discovery as theorem proving](https://www.hacktron.ai/blog/how-ai-can-hack#vulnerability-discovery-as-theorem-proving)
- [Not all humans think alike](https://www.hacktron.ai/blog/how-ai-can-hack#not-all-humans-think-alike)
- [Two modes of vulnerability discovery](https://www.hacktron.ai/blog/how-ai-can-hack#two-modes-of-vulnerability-discovery)
- [Case study: Hacking V8 via WASM](https://www.hacktron.ai/blog/how-ai-can-hack#case-study-hacking-v8-via-wasm)
- [Why this matters for Hacktron.ai](https://www.hacktron.ai/blog/how-ai-can-hack#why-this-matters-for-hacktronai)

# How can we make AI hack like a human?

![s1r1us](https://avatars.githubusercontent.com/u/22428507)[s1r1us](https://www.hacktron.ai/authors/s1r1us)

April 21, 2025

13 min read

[essay](https://www.hacktron.ai/tags/essay)

- [Magic, or just a lack of understanding?](https://www.hacktron.ai/blog/how-ai-can-hack#magic-or-just-a-lack-of-understanding)
- [How does the hacking agent in my brain work?](https://www.hacktron.ai/blog/how-ai-can-hack#how-does-the-hacking-agent-in-my-brain-work)
- [Formalizing hacking & the science of insecurity](https://www.hacktron.ai/blog/how-ai-can-hack#formalizing-hacking--the-science-of-insecurity)
- [Limits of security and the danger of AI](https://www.hacktron.ai/blog/how-ai-can-hack#limits-of-security-and-the-danger-of-ai)
- [Vulnerability discovery as theorem proving](https://www.hacktron.ai/blog/how-ai-can-hack#vulnerability-discovery-as-theorem-proving)
- [Not all humans think alike](https://www.hacktron.ai/blog/how-ai-can-hack#not-all-humans-think-alike)
- [Two modes of vulnerability discovery](https://www.hacktron.ai/blog/how-ai-can-hack#two-modes-of-vulnerability-discovery)
- [Case study: Hacking V8 via WASM](https://www.hacktron.ai/blog/how-ai-can-hack#case-study-hacking-v8-via-wasm)
- [Why this matters for Hacktron.ai](https://www.hacktron.ai/blog/how-ai-can-hack#why-this-matters-for-hacktronai)

index

## Magic, or just a lack of understanding?

> What magical trick makes us intelligent? The trick is that there is no trick. The power of intelligence stems from our vast diversity, not from any single, perfect principle.
>
> _—— Marvin Minsky, The Society of Mind, p. 308_

When a magician pulls birds out of thin air, makes object vanish, or transform cards value to another, we are often left in awe and confusion. Some tricks are so mindbending, they almost make it feel like the magician possesses supernatural powers.

Behind the scenes, though, there are numerous tricks that magicians uses ranging from exploting human psychology, clever misdirections and optical illusions to surprise and confusion. In the moment, without the hindsight, it truly feels magical. But once the trick is revealed, everything makes sense, and what once felt magical suddenly feels obvious.

Similarly, many of the things we do intellectually such as hacking software, composing music, generating new ideas, can seem like magic at first. But this doesn’t imply there is some supernatural is happening in brain. Rather, it only points to gap in our understanding of inner workings of the brain, one that can often be bridghed through scientific inquiry.

Consider the old philosophical riddle: “Does the tree make a sound if it falls in a forest with no one to hear it?”. For centuries, it puzzled people. But once we understand sound as vibrating air waves, the mystery dissolves.

The same applies to conciousness and creativity. They may feel magical, but with time they will be dissolved.

Intelligence, by contrast, already has several compelling hypotheses explaining how it works. While we haven’t reached a complete theory dissecting each and every part, the current cognitive and neuroscience understanding suggests that it is modular, distributed, hierarchical, and predictive, emerging from the interaction of systems like perception, memory, decision making, learning and attention.

Among the many theories, one that is particularly useful for building AI agents, and aligns surprising well with both cognitive science and modern artificial intelligence, is Marvin Minsky’s Society of Mind.

Minsky proposed a framework that intelligent behavior can be broken down into simple components, or “agents,” each responsible for a narrow task. These agents interact and cooperate in hierarchical structures to produce the rich, complex intelligence.

Even if Minsky’s framework isn’t entirely accurate in describing how real minds work, treating hacking as the work of a specialized sub-agent—and narrowing down what that agent does —— can still be incredibly useful. IMO, the Society of Mind framework helps us break down complex behaviors and build more effective, targeted agents.

## How does the hacking agent in my brain work?

When I am not hacking, I find great joy reading psychology, philosphy, and the study of consciousness, intelligence, and creativity. Exploring these questions has always made me feel more alive. With the recent advent of AI, this became even more exciting as I now can explore both hacking and intelligence together by building hacking agents.

What’s become increasingly obvious to me is that for any given task, the frame of agency changes and the agent has to change. A “coding agent” operates completely differently from a “hacking agent.” (switching between coding agent frame to hacking agent frame could be the sole reason for many software security issues). The goals are different, the strategies are different, which means agents have to change their hierarchies and heuristics on approaching the goal.

To develop a hacking agent, the first question I need to ask is: how does the hacking agent in my own brain work, and how does it generally operate for top-tier hackers? Only by understanding that process can I begin to transfer it into an AI agent.

## Formalizing hacking & the science of insecurity

> Exploitation is setting up, instantiating and programming a weird machine.
>
> _—— [Halvar Flake](http://www.dullien.net/thomas/weird-machines-exploitability.pdf)_

To create capable AI hacking agents, we must approach insecurity from first principles. In my view, the root of insecurity isn’t negligence, but _the cognitive limitations of humans_, our difficulty in reasoning about deeply composable software systems trust and the overwhelming complexity of software state machines.

A hacker’s job is to understand that complexity in many levels, understand it better than the original author, and break the assumptions holding the system together.

At a fundamental level, software systems are finite state machines. Each instruction or input transitions the system from one state to another. And we use Turing machines to implement these state transitions in real-world code.

Take a simple login system, for example. Its high-level state path might look like this (of course, each of these states may include their own internal substates and branching logic):

```
 -> INIT -> username and password entered -> password verified -> authenticated
```

And a programmer’s task is essentially to write such state machines, embedding the logic that governs how transitions occur. In essence, logic is the decision-making layer that controls state transitions, and Turing-complete languages give programmers the expressive power to encode that logic —— for browsers, web apps, protocols, and beyond.

> In a more pragmatic way, we can describe information security as the work towards computer systems we can finally trust.
>
> _—— [Jörn Bratzke](https://www.recurity-labs.com/research/RecurityLabs_Academia_vs_Hackers.pdf)_

In a perfect world, programs would do exactly what they were designed to do. There would be no need for security, because there would be no malicious actors. Trust would be implicit. No one would tamper with the system or try to coerce it into weird machines.

But that’s not the world we live in. And that’s why we need hackers to create trusted systems before criminals exploit them.

Remark  (A tangent on trust and coercion)

Just as a society without enforced property rights invites chaos and looting, software systems without trust enforcement invite _exploitation_. In many parts of the world, the absence of legal trust and secure ownership structures leads to poverty - not because people lack resources, but because they cannot trust the system to protect them. The rational way to survive in this situation is to cheat.

Trust requires coercion. In the real world, the rule of law and the threat of consequences force people to cooperate and create the conditions for prosperity.

A similar dynamic plays out in software engineering. Teaching every developer to write secure code is a losing battle. Google’s answer wasn’t education, it was [control](https://bughunters.google.com/blog/6644316274294784/secure-by-design-google-s-blueprint-for-a-high-assurance-web-framework). Instead of hoping developers remember secure practices, they enforced trust by design: hardened frameworks, default-safe libraries, and architectural constraints that coerce developers into writing secure code.

Lack of trust inherently allows chaos. Trust should be coerced.

> Any complex execution environment is actually many: One intended machine, endless weird machines.
>
> _—— Sergey Brutus_

And a hacker’s job is to explore a system more deeply than the person who built it —— to understand it at multiple levels, mentally reconstruct its state machine, and break its logical assumptions.

## Limits of security and the danger of AI

Even world-class hackers are bound by cognitive limits. Much of software insecurity comes from human inability to grasp the full complexity of composable, dynamic systems. We’re not capable to reason about all possible states, branches, and interactions in code.

If we ever witness an intelligence explosion —— AI systems that can reason far beyond human cognitive limits —— then it’s likely they will discover more weird machines than we ever could. Exploits that are invisible to the human mind may become trivial for them.

_This makes it very important that such AI capabilities don’t fall into the hands of malicious actors._

Even so, superintelligent AI would face hard theoretical limits when it comes to achieving perfect security. (Rice’s Theorem)

## Vulnerability discovery as theorem proving

At a high level, vulnerability discovery is a logical problem. The goal of a hacker —— or a security reasoning system —— is to construct a proof that a program’s behavior can violate its specification or assumptions. Can be done by guessing or brute-forcing, but this usually happens through - identifying a logical inconsistency within the system’s structure systematically.

This idea is grounded in the Curry–Howard correspondence, which draws a direct parallel between computation and logic:

> Programs are proofs, and proofs are programs. Running a program is akin to constructing a logical argument.
> By extension, vulnerabilities are proofs too —— they arise when an hacker constructs a logical path (i.e., an exploit) that demonstrates a proposition such as: “the user input reaches certain sink”.

In this view, vulnerability hunting is adversarial theorem proving —— by humans, or by AI agents —— where the proposition to be proven is:

“Given a system with a certain structure, can an input exist that causes
unintended behavior?”

That unintended behavior might look like:

- “Can untrusted input reach a dangerous sink?”

- “Can the attacker elevate privileges?”

- “Can this sequence of states bypass assumptions?”


These are all questions about the semantic properties of programs —— their meaning, not just their syntax or structure. Although, note that most of the vulnerabilities in web applciation that developers make are syntactic issue and can easily be found by current AI agents or SAST tools.

But what separates top-tier human researchers is their ability to reason about semantic vulnerabilities: issues that emerge from deep interactions across various systems, state transitions, and multi-layer logic.

## Not all humans think alike

For me, the difference between different humans hacking capabilities becomes especially clear in CTF competitions, where some of my friends exhibit a remarkable speed and processing in complex systems to identify vulnerabilites. In my opinion, this isn’t always something you can learn through practice alone. I’ve seen newcomers, people with almost no background in hacking, rapidly outpace others simply because of how quickly they digest information and reason.

This suggests that effective vulnerability discovery in complex targets require unique blend of cognitive abilities.

We can generalize the cognitive abilities required to the following items.

1. Long term memory is used to store and recall core concepts, prior vulnerabilities, bug classes, system behaviors, and high-level heuristics. This enables variant analysis and generalization.

2. Working memory is used as a mental “scratchpad” to actively hold and manipulate details of the current subsystem or bug candidate. The larger the working memory, the more state and logic one can juggle simultaneously.

3. Processing information is the engine behind reasoning. It allows the hacker to simulate hypotheses, test edge cases, and compress raw inputs into abstract representations. Even with strong memory, slow processing yields weak results. Conversely, high processing speed enables rapid internal updates and better state manipulation. I think one more important ability in better processing of information is, it allows storing information well in long term or working memory.


An especially interesting aspect of memory —— particularly relevant for AI agents —— is how even top-tier human hackers never ingest full codebases into working memory. Instead, they construct and rely on specific abstract representations: some kind of control-flow skeletons. These abstractions allow them to compress vast complexity into something they can actually reason about.

This is one of the active areas I’m researching —— how to replicate this ability in AI agents: to extract the right abstractions from large codebases, store them meaningfully, and perform targeted reasoning over them to find vulnerabilities.

## Two modes of vulnerability discovery

1. **Known propositions (variant analysis)**
   - This is the majority of modern vulnerability discovery: looking for known bug classes in new code. Rather than inventing new propositions, you’re just proving them in a new context (e.g. SQL injection, SSRF, XSS, authn and authz issues, etc.)

   - This form of analysis is currently the primary focus of Hacktron.ai, and it accounts for 60–70% of real-world web application vulnerabilities. The search process is relatively straightforward: you begin with a known vulnerability class, retrieve its defining characteristics and exploitation patterns, then systematically process the target codebase to determine whether that pattern exists. Pragmatically speaking, at Hacktron we would be able to solve this if everything works out.

   - However, variant analysis in complex systems like V8 presents a much greater challenge. These bugs often depend on deep contextual understanding of specific subsystems, making them far harder to identify.
2. **Novel propositions (new research)**
   - In contrast, novel research involves generating new propositions based on deep understanding of system behavior. These are often semantic, logic, or design-level bugs and require:
     - A thorough understanding of the subsystem, which itself demands significant processing power to reason through complex architectures.

     - Creative capacity to hypothesize how things might go wrong and break the trust.

     - Sufficient computational bandwidth (mental or machine) to simulate those hypotheses and explore potential weird state.
   - This is what I aspire to solve at Hacktron.ai. Why? Because, to be blunt —— I’m not great at this myself. I’m envious (in a good way) of people who can dive into V8 internals or kernel subsystems and find deep, structural flaws. So instead of trying to become one of them, I want to build something that comes out of me —— an AI system that can do that.

## Case study: Hacking V8 via WASM

A CTF teammate of mine once hacked V8’s WASM type system and landed a full exploit chain —— within just three days. Honestly, that’s one of the wildest things I’ve ever seen pulled off.

Here’s my rough (and probably naive) understanding of how he did it:

- Understanding the system (Understanding Agent): He didn’t start with deep V8 WASM internals knowledge, but he had strong fundamentals —— understanding type systems, compilers, and how computers work at a low level. From there, he dove into WASM specs, RFCs, and blog posts. Even parsing and internalizing those large specifications in a day or two requires what feels like superhuman processing speed.

- But that’s the key: with that kind of cognitive throughput, you can build efficient internal representations of complex systems. Some people just have this ability —— not to memorize everything, but to mentally structure complexity in a way that makes reasoning about it feel almost intuitive. Further, once he understood the core concepts —— like WASM’s isorecursive type system —— he built a compressed internal model of it; this could happen parallelly. It probably wasn’t the full source code in his head, but rather something abstract: maybe a control-flow diagram, or a conceptual graph that captured how types are resolved and passed through the engine. It’s not about raw memory. It’s about the quality of the representation —— how well the structure captures essential behavior.

- Manipulating the system (Reasoning Agent): Now comes the hacker mindset agent, the frame has to change —— simulate what could go wrong. What happens if a type check fails? What happens if an optimization assumes something that turns out to be false?

- He ran these “what-if” computations mentally, probing the gap between the type system as designed and as implemented. That’s where vulnerabilities live.


Interestingly, even V8 developers themselves might not have this kind of adversarial model in mind —— they’re focused on building, not breaking. But a hacker has the freedom to focus purely on failure. Whatever assumptions the system was built on —— those become targets.

## Why this matters for Hacktron.ai

The insight here is that you don’t need to load the full codebase to find deep bugs.
What you need is:

- An agent that can navigate and isolate a subsystem
- Build an internal model or abstraction of how it works
- Simulate hypotheis and see what breaks
- Compress that insight and hand it off to a vulnerability-finding agent

That’s how humans do it. And maybe AI should be modelled in that way. This is how I think AI will eventually hack large, complex systems like V8. And that’s what we’re trying to build.
