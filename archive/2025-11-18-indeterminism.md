---
date: '2025-11-18'
description: In "Indeterminism," Daniel E. Geer Jr. discusses the shift from deterministic
  to indeterministic software environments, emphasizing the challenges posed by modular
  code that incorporates AI-generated components. Vulnerabilities can obscure traditional
  threat models, leading to complex exploit "weird machines" that undermine trust
  in systems. The implications for software security are dire; as AI increasingly
  participates in code development, the opacity of its logic makes effective auditing
  and vulnerability detection problematic, raising critical questions about oversight
  and stability in cybersecurity. The article prompts reflection on the future capabilities
  of the cybersecurity workforce amid these changes.
link: https://www.computer.org/csdl/magazine/sp/2025/05/11204774/2aPD9aCBSyQ
tags:
- Software Security
- Zero Trust Security
- Vulnerabilities
- Indeterminism
- AI in Software Development
title: Indeterminism
---

- ![CSDL Logo](https://csdl-images.ieeecomputer.org/website/csdl-logos/logo-white.png)

- [Join Us](https://www.ieee.org/profile/public/createwebaccount/showCreateAccount.html?sourceCode=cs&autoSignin=Y&signinurl=https://www.computer.org/wp-json/global/login&url=https://www.computer.org/wp-json/global/login)
- Sign In
- [My Subscriptions](https://www.computer.org/csdl/my-subscriptions)
- [Magazines](https://www.computer.org/csdl/magazines)
- [Journals](https://www.computer.org/csdl/journals)
- [Video Library](https://www.computer.org/csdl/video-library)
- [Conference Proceedings](https://www.computer.org/csdl/proceedings)
- Individual CSDL Subscriptions
- [Institutional CSDL Subscriptions](https://www.computer.org/digital-library/institutional-subscriptions)
- Resources
  - [Career Center](https://jobs.computer.org/)
  - [Tech News](https://www.computer.org/publications/tech-news)
  - [Resource Center](https://www.computer.org/resources)
  - [Press Room](https://www.computer.org/press-room)
  - [Advertising](https://www.computer.org/advertising)
  - [Librarian Resources](https://www.computer.org/digital-library/librarian-resources)

All

0

![IEEE Security & Privacy cover image for year 2025 issue number 05](https://csdl-public.ieeecomputer.org/covers/msp20250500c1.jpg)

- [Previous](https://www.computer.org/csdl/magazine/sp/2025/05/11204783/2aPD7cojbSo "Previous Article") [Next](https://www.computer.org/csdl/magazine/sp/2025/05/11204782/2aPD8CRtNp6 "Next Article")
- [Table of Contents](https://www.computer.org/csdl/magazine/sp/2025/05)
- [Past Issues](https://www.computer.org/csdl/magazine/sp/past-issues/2020/2025)
- References
- Similar Articles

1. [Home](https://www.computer.org/csdl/)
2. [Magazines](https://www.computer.org/csdl/magazines)
3. [IEEE Security & Privacy](https://www.computer.org/csdl/magazine/sp)
4. [2025.05](https://www.computer.org/csdl/magazine/sp/2025/05)

IEEE Security & Privacy

# Indeterminism

Sept.-Oct. 2025, pp. 86-88, vol. 23

DOI Bookmark: [10.1109/MSEC.2025.3591826](https://doi.ieeecomputersociety.org/10.1109/MSEC.2025.3591826)

#### Authors

[Daniel E. Geer Jr.](https://www.computer.org/csdl/search/default?type=author&givenName=Daniel%20E.&surname=Geer), In-Q-Tel, USA

[Download PDF](https://www.computer.org/csdl/api/v1/periodical/mags/sp/2025/05/11204774/2aPD9aCBSyQ/download-article/pdf)

SHARE ARTICLE

Generate Citation

* * *

#### Keywords

Indeterminism, Fuzzy Set, Original Language, Understanding Of The Causes, Threat Model, Alchemical, Human In The Loop, Dependency Graph, Bug Fixes

#### Abstract

We have entered an era of indeterminism, a time when events have no knowable cause. It was not a crisp transition, one easy to point out in retrospect, but that transition has happened and it was in the recent past.

* * *

![Graphic: ](https://csdl-images.ieeecomputer.org/mags/sp/2025/05/figures/lastword.a1-3591826.gif)

**Daniel E. Geer, Jr**

In-Q-Tel, USA

We have entered an era of indeterminism, a time when events have no knowable cause.
It was not a crisp transition, one easy to point out in retrospect, but that transition
has happened and it was in the recent past.

What do I mean?

A deterministic world is one where every effect has a cause. An indeterministic world
is one where some effects have no cause. Writing software is all about assembling
causes so as to get effects.

Software systems are always modular, often to a remarkable degree. This is not news.
That modules get imported from external pools is not news either. Nor is it news that
not every module is a perfect fit in all its details, and some of those details are
unfortunate. In that wealth of composability those unfortunate details include what
we ordinarily call vulnerabilities, and we know that vulnerabilities cluster at interfaces.

Composing modules involves the propagation of trust by assumption, yet we know that
security as a property is not composable. What if we were to characterize a vulnerability
as that which proves assumed trust to have been misplaced? That’s consistent with
the zero trust paradigm, but zero trust is about logical subsystems in operation,
not individual software modules in construction.

S&P readers are doubtless familiar with the “weird machine” concept, where violating
the assumptions under which a system was built allows exploitation of the system using
its own code, typically through crafted inputs presented to module interfaces.

When Bratus and Shubina began to formalize the “weird machine” concept1, they wrote “Exploits \[are\] understood both as proofs-by-construction of the unexpected
computation’s existence (a.k.a. vulnerability) and as programs in their own right.
But if exploits are programs, and generalize into programming models, what machines
do they run on? Tautologically, exploits violate the expectations of the original
programmer or designer of the vulnerable software, and hence their models of the target
machine. These programmers or designers failed to see a richer machine embedded or
emergent in the target. Exploits run on these richer machines, and are proof-by-construction
that these richer machines exist.” \[As of today, Dullien ([https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8226852](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8226852) and Vanegue [https://openwall.info/wiki/\_media/people/jvanegue/files/adversarial\_logic.pdf](https://openwall.info/wiki/_media/people/jvanegue/files/adversarial_logic.pdf)) are leading the charge to formalize exploitation.\]

Getting to the theme of this essay, what Bratus and Shubina describe is a surprise
transition from a thought-to-be deterministic system that was trustable to an indeterminate
one that no longer is. Except that the system was indeterminate in the beginning,
only invisibly so—it’s our understanding that transitioned, not the code.

A central question since at least Rescorla’s 2004 talk at the Workshop on the Economics
of Information Security2: “Is finding security holes a good idea?”. Rescorla offered a pretty good mathematical
model of that question and came to various conclusions, conclusions which Felten succinctly
summarized3 as (1) “there are many, many security bugs”, and (2) “there is little if any depletion
of the bug supply \[by\] finding and fixing bugs”. Ten years later, Schneier’s Atlantic
article4 had as its title exactly that question: “Should U.S. Hackers Fix Cybersecurity Holes
or Exploit Them?”, and Schneier then refined the question to be whether vulnerabilities
are sparse or dense. But density is not quite right either; as Aitel says5: “The limiting factor in offensive capability is not finding vulnerabilities, it
is having the talent to turn them into dependable tools”.

Is turning vulnerabilities into dependable tools (emphasis on dependable) what Bratus
and Shubina were implying with their concept of “a richer machine embedded or emergent
in the target”? Does finding that richer, weirder machine mean turning something indeterminate
into something determinate?

Finding vulnerabilities expands what we understand; some argue that the contest in
the cyber domain is the contest of software understanding: [https://www.cisa.gov/sites/default/files/2025-01/joint-guidance-closing-the-software-understanding-gap-508c.pdf](https://www.cisa.gov/sites/default/files/2025-01/joint-guidance-closing-the-software-understanding-gap-508c.pdf) But what if we can’t find those vulnerabilities? What if we know that vulnerabilities
are present but unfindable? Ordinarily, when our understanding of the cause of some
outcome is incomplete, hedging our professed understanding in probabilistic terms
becomes necessary. The probabilities here are what derivative traders would call “tail
risk”—notably rare events with notably outsized effects.

Example: Suppose there exists a well understood, careful, deterministic design for
some software system. We test that system’s implementation. We score the quality of
the software test harness itself by measuring its code coverage. But code coverage
will not find a weird machine.

More to the point (and per Bratus): “Random (‘fuzzing’) finding of bugs and primitives,
artisanal distillation of techniques, and bespoke mitigations are obsolete. Weird
machine exploit chains of ‘impossible’ complexity are already in the wild.” For illustrations
of “impossible complexity”, see any of these:

Blasting Past Webp [https://googleprojectzero.blogspot.com/2025/03/blasting-past-webp.html](https://googleprojectzero.blogspot.com/2025/03/blasting-past-webp.html)

The WebP 0day [https://blog.isosceles.com/the-webp-0day/](https://blog.isosceles.com/the-webp-0day/)

Bending Microarchitectural Weird Machines Towards Practicality [https://www.usenix.org/conference/usenixsecurity24/presentation/wang-ping-lun](https://www.usenix.org/conference/usenixsecurity24/presentation/wang-ping-lun)

Implication: This matter is DARPA-hard. Even so and as they say on late-night TV,
“But wait, there’s more!”

The era of indeterminism began when software began to be written by (stochastic) AI.
Google’s Pichai recently said “Today, more than a quarter of all new code at Google
is generated by AI while human programmers oversee and manage these AI-generated contributions.”
This is presumably an accelerating trend everywhere and at once. Is it likely to increase
determinism in software modules or likely to decrease it? If the enterprise’s staff
will never see the code they deploy, can they at least assume that that code is deterministic?

For that matter, can enterprise staff dependably read that code? We submitted a request
to ChatGPT to “Write a C program to factor an integer in the manner of the obfuscated
C contest” and we got back a pretty hard-to-read response, but with this closing remark
from ChatGPT: “Would you like it \*\*more obfuscated\*\*, or with \*\*self-reproducing\*\*
or \*\*ASCII-art tricks\*\* as seen in IOCCC entries?” If the AI knows how to hide things
well enough, then the consumer of the AI’s code has to accept what the AI wrote because
the consumer is in no position to see behind the curtain. For the consumer, this becomes
a habit out of, dare I say, necessity—the AI holds the cards. Once habituated, the
consumer accepts the indeterminism as normal. From that all sorts of things flow and
the AI begins the path to autonomy.

With Gaffney, we contended6 that autonomy inevitably produces emergent behaviors, unexpected outcomes that emerge
unpredictably from complexity, further implying that trust-but-verify escapes our
grasp as complexity rises. Later with Aitel, we wrote that7 “We’re now entering territory where even the threat models themselves become opaque.
It’s not just ‘Why did the AI fix that bug?’ It’s ‘Why does the AI think that’s a
bug in the first place?’ In short, autonomy means losing the plot. Humans are about
to find themselves on the outside looking in, facing security decisions made by AIs
whose reasoning isn’t just complicated—it’s fundamentally inaccessible.”

If Grade-A software writing skill is a pre-requisite for software security skill,
then what will the cybersecurity workforce look like when the great majority of software
is AI written and its underpinnings indeterministic?

Deterministic or indeterministic may no longer have an answer.

Yet that might not be the most telling effect. Guthery suggests8, “A salutary benefit of AI-generated code may be that it will slow down and maybe
even freeze APIs and language evolution.” Numerous downstream effects worth analyzing
would come from that for sure.

Or is the most telling effect to come that of applying AI not to writing code but
to auditing its execution? Perhaps Inam, et al., pointed the way at Oakland9, “Auditing, a central pillar of operating system security, has only recently come
into its own as an active area of public research. This resurgent interest is due
in large part to the notion of data provenance, a technique that iteratively parses
audit log entries into a dependency graph that explains the history of system execution.
Provenance facilitates precise threat detection and investigation through causal analysis
of sophisticated intrusion behaviors.”

Practically speaking, is there any entity using adversarial AI training to write code
in which weird machines can hide in plain sight, code that defensive AI will not be
able to characterize? That mythical prudent man, the one who plans for maximum damage
scenarios rather than for maximum likelihood scenarios, will take note here.

In short, what’s a responsible defensive party to do? We know that the benefits of
a new technology are not transitive, but the risks are. It is said that a quality
control officer’s authority is real iff s/he can stop the production line. Is the
test of AI code management whether the human in the loop can roll back deployment,
or even whether there is some equivalent to adding “before:2023” to a search query?

The irony here, if you can call it that, is how the advent of the scientific method
changed so many things from unknowable (indeterministic) to knowable (deterministic),
but the rate of change in what is now within the realm of the technically possible
is such that we can oh so easily return to a world of sorcerers, alchemy, and faith
in powers in proportion to their mystery.

Indeterminism, what’s your bet?

## References

- 1.S. Bratus and A. Shubina, “Exploitation as code reuse: On the need of formalization,” _Information Technology_, vol. 50, no. 2, 2017.
- 2.E. Rescorla, “Is Finding Security Holes a Good Idea?”, _Workshop on the Economics of Information Security_, 2004\. [infosecon.net/workshop/downloads/2004/pdf/rescorla.pdf](http://infosecon.net/workshop/downloads/2004/pdf/rescorla.pdf)
- 3.E. Felten, “ _An Inexhaustible Supply of Bugs_”, Princeton CITP, [blog.citp.princeton.edu/2004/03/11/inexhaustible-supply-bugs/](http://blog.citp.princeton.edu/2004/03/11/inexhaustible-supply-bugs/)
- 4.B. Schneier, “ _Should U.S. Hackers Fix Cybersecurity Holes or Exploit Them?_”, 2014: [www.theatlantic.com/technology/archive/2014/05/should-hackers-fix-cybersecurity-holes-or-exploit-them/371197](http://www.theatlantic.com/technology/archive/2014/05/should-hackers-fix-cybersecurity-holes-or-exploit-them/371197)
- 5.D. Aitel, _personal communication_.
- 6.D. Geer & G. Gaffney, “ _Establishing the Conditions of Engagement with Machines_”, [https://cyberdefensereview.army.mil/Portals/6/Documents/2023\_Spring/GeerGaffney\_CDRV8N1-Spring-2023.pdf](https://cyberdefensereview.army.mil/Portals/6/Documents/2023_Spring/GeerGaffney_CDRV8N1-Spring-2023.pdf)
- 7.D. Aitel & D. Geer, “ _AI and Secure Code Generation_”, [https://www.lawfaremedia.org/article/ai-and-secure-code-generation](https://www.lawfaremedia.org/article/ai-and-secure-code-generation)
- 8.S. Guthery, _personal communication_.
- 9.M. Inam, et al., “ _SoK: History is a Vast Early Warning System_” [https://oaklandsok.github.io/papers/inam2023.pdf](https://oaklandsok.github.io/papers/inam2023.pdf)

* * *

* * *

#### Similar Articles

- [Impact of the Creation of the Mozilla Foundation in the Activity of Developers](https://www.computer.org/csdl/proceedings-article/msr/2007/29500028/12OmNqJ8tog)

Fourth International Workshop on Mining Software Repositories (MSR'07:ICSE Workshops 2007)
- [Crisp Decision Tree Induction Based on Fuzzy Decision Tree Algorithm](https://www.computer.org/csdl/proceedings-article/icise/2009/pid983306/12OmNrH1PAy)

Information Science and Engineering, International Conference on
- [Reduce, Reuse, Recycle: An Approach to Building Large Internet Caches](https://www.computer.org/csdl/proceedings-article/hotos/1997/78340093/12OmNwBjP4r)

Hot Topics in Operating Systems, Workshop on
- [Risk Analysis of Water Resource Based on Possibility-probability Distribution](https://www.computer.org/csdl/proceedings-article/fskd/2009/3735c156/12OmNwFicTL)

2009 Sixth International Conference on Fuzzy Systems and Knowledge Discovery (FSKD 2009)
- [The CDC 6600 Project](https://www.computer.org/csdl/magazine/an/1980/04/man1980040338/13rRUwghdaX)

IEEE Annals of the History of Computing
- [CRISP-DM for Data Science: Strengths, Weaknesses and Potential Next Steps](https://www.computer.org/csdl/proceedings-article/big-data/2021/09671634/1A8haAtkN6o)

2021 IEEE International Conference on Big Data (Big Data)
- [A Cognitive Human Model for Virtual Commissioning of Dynamic Human-Robot Teams](https://www.computer.org/csdl/proceedings-article/irc/2021/341600a027/1ANLPjLO1nG)

2021 Fifth IEEE International Conference on Robotic Computing (IRC)
- [Identifying the most Common Frameworks Data Science Teams Use to Structure and Coordinate their Projects](https://www.computer.org/csdl/proceedings-article/big-data/2020/09377813/1s64aInV29y)

2020 IEEE International Conference on Big Data (Big Data)
- [From Mainframes to Microprocessors](https://www.computer.org/csdl/magazine/mi/2021/06/09623407/1yJTpPZlbdC)

IEEE Micro
- [Detection of Data Exposures in Software Services Using a Large Language Model](https://www.computer.org/csdl/proceedings-article/sse/2025/678900a091/29kMHsEdwSk)

2025 IEEE International Conference on Software Services Engineering (SSE)

\[ back to top \]
