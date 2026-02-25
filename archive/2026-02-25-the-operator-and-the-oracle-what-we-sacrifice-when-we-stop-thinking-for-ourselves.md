---
date: '2026-02-25'
description: 'The article discusses the cognitive implications of AI integration in
  cybersecurity, focusing on the risk of diminished critical thinking skills among
  practitioners, particularly within red teaming. It emphasizes the necessity of maintaining
  mental engagement when using AI tools: practitioners should analyze AI outputs''
  reasoning rather than merely accepting conclusions. Key recommendations include
  adopting a “Socratic method” with AI for self-assessment, constructing mental models
  of protocols before seeking vulnerabilities, and performing retrospective analyses
  of vulnerabilities to strengthen cognitive processes. The author asserts that while
  AI enhances efficiency, over-reliance risks erosion of foundational security competencies.'
link: https://kreep.in/the-operator-and-the-oracle-what-we-sacrifice-when-we-stop-thinking-for-ourselves/
tags:
- Cybersecurity
- Mental Models
- Learning Strategies
- AI Ethics
- Red Teaming
title: 'The Operator and the Oracle: What We Sacrifice When We Stop Thinking for Ourselves'
---

- [Home](https://kreep.in/)

# The Operator and the Oracle: What We Sacrifice When We Stop Thinking for Ourselves

2026-02-25

There's a real thought that's been sitting in the back of my head for a while now, and I keep coming back to it. Jason Lang shared his [Real Human Concerns In The Age of AI](https://x.com/curi0usJack/status/2024184571974000984?ref=kreep.in) on X recently that crystallised it - the worry that AI is quietly making us dumber, that we're all so busy building and shipping tools that nobody's stopping to ask what's happening to the person behind the keyboard. The cognitive killchain is a term that has been thrown around to describe this.

I've been doing security professionally for a few years now. Before that, a lot longer as a hobby - the kind of obsession that starts with curiosity and never really stops. Red team lead now. I - like many others, have started using AI to create new tools for myself, my team and the community. I've also been involved in some projects involving offensive agentic AI capabilities. This gave me a lot of experiences that allowed me to realise a few things when it comes to how AI will shape our future in the cyber community.

I'll be honest in a way that's slightly embarrassing but probably common nowadays: I have caught myself, more than once, reaching for the model before forming a thought of my own. Using AI output as a substitute for a first opinion rather than a check on one I'd already built. That's the thing I want to talk about. Not because I have it figured out, but precisely because I don't.

* * *

Here's the uncomfortable truth about red teaming specifically - our actual competitive advantage isn't tool proficiency. Any motivated person can learn tooling. What makes a red teamer genuinely dangerous is the ability to hold a complex mental model of an environment, stress-test it in real time, and find the inferential leap that no scanner flagged because it required _thinking_. That's the skill. And it's the exact kind of skill that quietly softens when you stop exercising it. If you stop performing the exercise of using your own thoughts to find the flaw in assumptions, you slowly lose the ability to do this exercise efficiently.

Nobody in this field is going back to pre-AI workflows, nor should they. The tools are faster than us at plenty of things, and pretending otherwise is just ego dressed up as discipline. But there's a real question underneath all the productivity gains that I think deserves an honest answer:

> Are you using AI to become better at your craft, or are you using it to avoid the friction that _produces_ craft in the first place?

## Red Team Your Own Learning: Using AI to Find and Fix Your Gaps

After some **actual** thought - the slow, uncomfortable, non-autocompleted kind - I want to put something forward. Not a framework, not a methodology doc, nothing that's going to end up in a slide deck. Just a set of usage guidelines I've been working out for myself, and that I think are worth sharing with the people in this field who I'd consider peers. Fellow red teamers. People who chose this work because they genuinely like thinking hard about hard problems, and who should probably care more than most about not accidentally thinking themselves out of a job.

Here's what I've got.

### **Read the reasoning, not just the answer.**

This one changed how I use these models, and it came from noticing something almost by accident. In my experience, Opus-class models are genuinely good at reasoning through logic flaws in code - not just flagging syntax issues but actually walking through execution paths and finding where an assumption breaks down in an interesting way. Most people grab the output and move on. **Stop doing that.**

Here's a concrete example. You're reviewing a bespoke authentication implementation during an engagement: custom token validation in some internal tooling. You feed it to the model and instead of just reading what it found, you read _how it got there_. What it checked first. What assumptions it questioned. Where it slowed down. What you'll typically see is a structured skepticism that moves roughly like this: establish what the code claims to do, identify the trust boundaries it assumes, probe the delta between claimed behavior and actual execution, then look for conditions where that delta becomes exploitable.

That's a methodology. It's extractable. You can internalise it and start applying it manually and if you do that consistently enough across enough different code reviews, it becomes part of how your brain approaches the problem without prompting.

Another example of this is mentoring. As I've mentored others in the offensive community, I've always tried to teach the mental process over the technical details as much as I could. There is really no point in teaching someone what each nmap flag does, what cross-protocol NTLM relay options are possible, etc.. There is little point to this, it's documented, in writing, well enough that anyone with enough will, time and foundational knowledge - can understand it. What they'll gain most value from is HOW and WHY I chose those nmap flags for this scan, or why I chose to relay to LDAP instead of SMB. There is little point in knowing how to copy and paste a command, if you have no idea why you used that command.

Focus on the **reasons**.

### **Force the narration before the answer.**

This is a prompt discipline more than a technical trick. Instead of asking "what are the vulnerabilities in this implementation," ask the model to walk you through how it would _approach_ finding them - what it would look at first, what mental model it would build, what it would rule out and why - before giving you anything conclusive. Then attempt the analysis yourself. Then compare.

This is particularly useful for areas where you're not yet fluent. For me, that's been reverse engineering and fuzzing over the last few weeks. I'm not as sharp as I want to be in these areas. Therefore, I've been using the model as something like a senior analyst narrating their thought process - here's how I'd approach this binary, here's what I'm looking for in the decompiled output, here's why this function signature is interesting - and then forcing myself to replicate that approach on similar targets without help. Think of it like shadowing a senior on your first penetration test.

The goal isn't to have the AI do the work. The goal is to acquire the _cognitive shape_ of someone who's done this a thousand times. Fuzzing is a good example - rather than asking the model to generate a harness for you, ask it to explain the attack surface analysis that informs _why_ you'd fuzz specific input vectors on a given target. What are the trust boundaries? What parser logic is likely to be brittle? Where does the application make assumptions about input format that an attacker wouldn't share? That's the thinking that makes fuzzing effective. The harness is just the mechanism.

Extract a methodology, not an answer.

### **Let it quiz you.**

This one feels almost too simple but it's genuinely underused. Pick a vulnerability class you're softer on than you'd like to admit - SSRF, deserialization, whatever - and don't ask the model to explain it to you. Ask it to test you on it. Tell it to be adversarial. Ask it to probe your understanding, find the gaps, and give you progressively harder edge cases once you've handled the easy ones.

The Socratic method is not new. What's new is having access to a tutor that has read everything, never gets tired, and will relentlessly poke at the exact place you're weakest if you ask it to. Most people don't ask it to. There's something that feels a little vulnerable about putting your gaps on the table in front of a language model - I recognise that's slightly absurd, but it's real - and I think that's worth pushing through. I would not have recommended this a few years ago, when models were a lot more tailored at just pleasing you, and pretty much incapable of being blunt and telling you why your answer is wrong. Recently I've observed a slight shift in this area - at least with the frontier Anthropic models, and I recommend using them in this way to fill skill gaps. Use it as another learning tool - but don't use it in isolation. Hallucination is still a thing obviously.

### **Protocol deep dives as mental model construction.**

When you hit an unfamiliar protocol or format on an engagement - and you will, constantly - the lazy move is to ask "what are the known vulnerabilities in X." Don't do that first. Instead, ask the model to walk you through the protocol's design: what problems it was built to solve, what trust assumptions it makes, and historically where those assumptions have proven wrong. Build the mental model before you build the attack surface.

This has been valuable for me when hitting niche industrial protocols, obscure authentication schemes, or legacy formats I haven't touched before. Understanding _why_ a protocol is designed the way it is gives you an intuition for where it breaks that a list of CVEs never will. The CVEs are downstream of someone having had that intuition.

### The retrospective loop.

After using AI to find something - a logic flaw, a vulnerability, an attack path - ask it to reconstruct the manual methodology. "How would a skilled analyst have found this without your help? Walk me through the steps." Then, on the next similar target, attempt those steps yourself before reaching for the model.

This is probably the highest-leverage habit I've tried to build, and also the one I'm most inconsistent about. It's slower. It's sometimes frustrating when you know the AI would have the answer in thirty seconds and you're sitting there actually thinking. That frustration is not a bug. That frustration is, almost precisely, the mechanism through which you get better. It's even more frustrating because it's retrospective. You already have the "fun stuff", you found the vuln and you have the exploit working - but you can use this concept to potentially squeeze that little bit of extra methodology upgrade for yourself. It's more of an investment than an instant payoff. Starting to see the pattern now ?

* * *

There's a broader point underneath all of this that I keep coming back to. The thing AI removes, when you let it, is friction. And friction in security work is not incidental to learning - it's almost the whole mechanism. The engagement where something didn't work the way you expected. The code path that didn't make sense until it suddenly did. The hours spent in a debugger on something that turned out to be a one-byte difference. Those are the moments where the mental model gets built. When AI absorbs that friction on your behalf, it's not just saving you time. It's also - quietly, invisibly - taking the thing that was making you better.

The question isn't whether to use these tools. The question is whether you're directing them or being directed by them. Whether you're extracting methodology or just extracting answers. Whether the engagement ends with you knowing more than when it started, or just with a report that got written faster.

I think about the "Done, all features implemented and verified" message - you know the one - and how easy it is to feel satisfied by it. I've trained myself to be a little suspicious of that feeling now. Not paranoid. Just aware that completeness and understanding are not the same thing, and that in this field, understanding is actually the job.

## Conclusion

None of this is solved. I'm figuring it out as I go, same as everyone else. But a few things feel like they're pointing in the right direction: read the reasoning, not just the output. Use the model to test you, not just help you. Build the mental model before you build the attack surface. And when the AI hands you something useful - before you move on, ask yourself whether you could have gotten there yourself, and if not, whether you'd like to be able to.

That last question is, I think, the one worth keeping close.
