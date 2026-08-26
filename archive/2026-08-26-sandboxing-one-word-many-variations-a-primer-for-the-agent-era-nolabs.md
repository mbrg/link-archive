---
date: '2026-08-26'
description: The article by Luke Hinds provides a comprehensive overview of sandboxing
  in the context of emerging AI agents. It categorizes sandboxing techniques across
  a gradient from hardware virtualization (e.g., microVMs) to fine-grained process
  isolation, emphasizing that strength of isolation alone is insufficient; granularity
  in authority and resource access is crucial. The analysis underscores the need for
  nested sandboxes, addressing both escape threats and potential misuse within the
  confined context of an agent's operations. It introduces a taxonomy for evaluating
  agent sandboxes based on enforcement, confinement granularity, and egress controls,
  promoting a balanced security approach for AI workloads.
link: https://nolabs.ai/blog/sandbox-primer
tags:
- Software Architecture
- Sandboxing
- Security
- MicroVMs
- AI Agents
title: 'Sandboxing: One Word, Many Variations — A Primer for the Agent Era — nolabs'
---

[All posts](https://nolabs.ai/blog)

# Sandboxing: One Word, Many Variations — A Primer for the Agent Era

SecurityAI AgentsSandboxingSoftware Architecture

![Luke Hinds](https://nolabs.ai/team/luke-hinds.png)

Luke Hinds

Co-founder & CEO·August 25, 2026

Sandboxing is a security technique that runs a workload[1](https://nolabs.ai/blog/sandbox-primer#fn-workload) inside a boundary that limits what it can do and what it can access. The workload can be almost anything — a full operating system under a hypervisor or microVM, an application, a browser tab, a process, or even a single function call — and under the term "sandbox" there are many different models for drawing that boundary. The breadth of the term matters, because whenever a new class of workload arrives — most recently, AI agents and the "agent sandbox" — the first instinct is to reach for one point on this spectrum and declare it _the_ answer. Understanding what the different models actually protect is the antidote to that.

A spectrum of sandboxes

It's worth taking a moment to look at the spectrum of sandboxing techniques that have been developed over the years, and how they relate to each other. The following is a non-exhaustive list of common sandboxing techniques, ordered by mechanism class. The ordering is intentional: it traces an apparent gradient, with isolation strength descending as the granularity of control ascends — and it foreshadows the later point that these techniques can be combined to produce a more robust security posture than any one of them alone. Indeed, two of the most familiar sandboxes of all — the mobile app and the browser tab — turn out to be compositions of the mechanisms on the gradient rather than points on it.

The microVM and hypervisor

At one end of the spectrum sit hardware-virtualised sandboxes. Hypervisors like KVM or Xen, and microVMs such as Firecracker or Kata Containers, give each workload its own virtual machine with a separate kernel — this is what allows cloud providers to run untrusted code from thousands of customers on the same physical host.

Containers, jails, and zones

A step down in isolation strength are OS-level sandboxes: containers (namespaces and cgroups on Linux), FreeBSD jails, or Solaris zones, where processes share a kernel but see a restricted view of the filesystem, network, and process tree.

Process isolation

Narrower still is the sandboxed _process_: a single running program stripped of privileges by the kernel itself. The primitives here are seccomp-bpf, which lets a Linux process give up all but a handful of syscalls; Landlock, which restricts its view of the filesystem; macOS's Seatbelt; and OpenBSD's pledge and unveil. Because the primitives are fiddly to use directly, tools compose them into something practical — bubblewrap and Firejail wrap desktop applications, and more recently nono wraps AI coding agents, applying kernel-enforced, irreversible restrictions on what the agent process can read, write, and connect to. Notably, the "process" being confined here can be quite a high-level thing — a coding agent invoking a tool — and the granularity can follow suit: nono's broker launches each tool call as its own process under its own policy, with its own filesystem grants, network rules, and credentials, so a tool never inherits the agent's broader access. Process isolation is the lowest-overhead boundary that the kernel will still enforce for you: no VM, no container image, near-zero latency — drawn around exactly one program.

In-process: language runtimes, verifiers, and WebAssembly

At the fine end of the gradient, the boundary moves inside the process itself. The JVM's old SecurityManager and .NET's Code Access Security attempted in-process sandboxing at the language level, and eBPF programs are sandboxed by a verifier that proves they terminate and stay in bounds before the kernel will run them at all. WebAssembly is the model's modern flagship: a Wasm module gets a linear memory region and can only interact with the outside world through functions the host explicitly imports for it. This makes the sandbox cheap enough to wrap around a single library or function call — which is exactly how projects like RLBox use it, compiling risky C libraries (font parsers, image decoders) to Wasm so a memory-safety bug inside them can't corrupt the surrounding application.

Compositions: the mobile app sandbox

The best-known sandboxes are not single mechanisms from the gradient above but compositions of several. Mobile platforms are the clearest example. On Android, every app installed from the marketplace runs as its own Linux user with a private data directory, and can only reach the camera, contacts, or location through a permission system mediated by the OS. That per-app UID is only the first layer: SELinux runs in enforcing mode underneath, confining every app and system service to a mandatory-access-control domain the app cannot alter, and seccomp filters trim the syscalls an app process can make — so even a bug that bypasses one layer lands inside another. iOS works similarly with its per-app containers and entitlements. Here the sandbox isn't something the developer opts into — it's a condition of distribution: the app store model only works because users can install software from strangers with some confidence it can't read another app's data.

Compositions: the browser

Browsers compose across the gradient even more visibly, layering several sandboxes on top of each other. Each tab (or site, under site isolation) runs in a separate low-privilege process that can't touch the filesystem directly, while inside that process JavaScript executes within the confines of the JS engine and the same-origin policy — and risky native libraries can be confined further still behind Wasm/RLBox boundaries. Under the hood, both Chrome and Firefox assemble this from whatever the host OS provides, confining their content processes with Seatbelt on macOS, seccomp-bpf and namespaces on Linux, and restricted tokens on Windows — Firefox's multi-process split (Electrolysis, and later Fission for per-site isolation) mirroring Chromium's architecture. Document readers follow the same compositional pattern on a smaller scale: PDF and Office applications open untrusted files in restricted "protected view" processes.

Sandboxing as a service

More recently, the sandbox has become a product in its own right. Cloud services such as E2B, Daytona, Modal, and the sandbox offerings from Cloudflare and Vercel expose isolated execution environments through an API: call a function, get a fresh sandbox, run untrusted code in it, tear it down. These services sit at no single point on the gradient — they span it: E2B gives each session its own Firecracker microVM with a dedicated kernel, while Daytona builds on containers sharing a host kernel and optimises for persistent, stateful workspaces. The primary customers are AI systems: these platforms exist largely because agents now generate code that has to run _somewhere_, and that somewhere cannot be the host.

The common contract

What unites a Firecracker microVM, an Android app, a browser tab, and a Wasm function is not the mechanism — hardware virtualisation, kernel enforcement, process boundaries, and validated bytecode with runtime bounds enforcement are wildly different techniques — but the contract: code runs with the least privilege it needs, inside a boundary it cannot cross, so that when things go wrong — through malice, a bug, or an entirely well-intentioned mistake — the harm is limited to what the workload was ever allowed to touch.

Strength is not the whole story

This spectrum invites a misleading reading: that sandboxes can be ranked on a single axis from "weak" (in-process) to "strong" (hardware-virtualised), and that stronger is always better. That framing conflates two independent properties — the strength of the boundary and the granularity of what it protects.

A microVM or Xen guest has an extremely strong boundary. The attack surface between guest and host is narrow, escape vulnerabilities are rare and expensive, and cloud providers rightly trust it to separate mutually hostile tenants. But the boundary encloses an entire operating system. Inside that VM, nothing is isolated from anything else: the web server, the TLS private keys, the database credentials, the image-parsing library, and the config files all live in one trust domain. If the image parser is compromised, the strong hypervisor boundary is irrelevant — the attacker is already inside it, standing next to the keys. The VM protects the _host_ from the workload; it does nothing to protect the workload's components and assets from each other.

Fine-grained sandboxes invert this trade-off. Wrapping a font parser in a Wasm/RLBox sandbox, splitting a browser into per-site processes, or confining a single process with seccomp and pledge produces boundaries that are weaker in terms of isolating the entire operating system, but far more capable and adaptable — able to carve out zero-trust paths that allow an agent, or any component, to act within a limited level of authority. The renderer that parses hostile input holds no cookies; the parser that decodes hostile fonts can't reach the network; the compromised component gains almost nothing, because almost nothing was reachable from inside its boundary.

Judging a sandbox

This is why grading sandboxes by isolation strength alone is misguided. The right question is not "how hard is this boundary to escape?" but "what does an attacker get _without_ escaping?" A strong boundary around everything can be worth less than a modest boundary around exactly the right thing. Isolation strength measures the cost of crossing the fence; granularity determines what was left inside it — and a security architecture has to be judged on both.

![strength-capability-gradient](https://nolabs.ai/_next/image?url=%2Fblog%2Fimages%2Fsb-gradient.png&w=3840&q=75)

The "agent sandbox"

Nowhere is this distinction more current than in the emerging notion of an _agent sandbox_. As AI agents have started writing and executing code, browsing the web, and operating tools on a user's behalf, a natural consensus has formed: run the agent inside strong isolation, ideally a microVM, so that whatever it does stays contained. The sandbox-as-a-service platforms above are this consensus made concrete. That instinct is sound as far as it goes. An agent executing arbitrary generated code is exactly the kind of untrusted workload hypervisor isolation was built for, and a Firecracker-class boundary is a reasonable floor for it.

But it answers only one of the two questions. VM isolation addresses the _escape_ threat — the agent (or code it ran) breaking out to the host. It says nothing about what the agent can do with what is legitimately inside its operating context. An agent is typically handed real assets to be useful: repository contents, API tokens, cloud credentials, a browser session, customer data, an email account. All of that sits inside the boundary with it, in one trust domain — the same shape as the VM whose web server, keys, and parsers all live together. And the characteristic failure mode of an agent is not a hypervisor escape; it is being manipulated, through prompt injection or poisoned tool output, into misusing its legitimate access — reading a secret it didn't need, or exfiltrating data through a perfectly ordinary outbound request. Against that threat, the strength of the VM wall is beside the point: nothing needs to cross it.

Seen through the strength-versus-granularity lens, the agent sandbox problem is mostly a granularity problem. What matters is drawing boundaries _inside_ the operating context: scoping credentials to the single task rather than the account, mounting only the files the task needs, restricting egress to an allowlist of destinations, brokering sensitive actions through an interface that can require review, and keeping untrusted content the agent reads separated from the authority it wields. None of this replaces the VM — the VM remains the right outer wall, and dismissing it would be as one-sided as relying on it alone. The point is that "agent sandbox" should be read the way "sandbox" has always deserved to be read: not as one mechanism, but as a set of nested boundaries matched to the threats.

A taxonomy for agent sandboxes

If a single strength score can't grade an agent sandbox, what should? The following axes describe any agent sandbox without naming a technology. Each is a question to ask of a design; together they form its profile.

**1\. Enforcement layer.** Where does the boundary actually live — in hardware virtualisation, the kernel, a language runtime or verifier, a policy layer, or prompt-level instructions? The layer determines who or what can be deceived: a prompt-level rule can be argued with; a kernel cannot.

**2\. Confinement granularity.** What unit is being confined — the agent's whole environment, the agent process, a single task or session, an individual tool invocation, or one function call? _This is the axis this primer argues is systematically undervalued._

**3\. Escape resistance.** How hard is the boundary to cross? Observable properties include the breadth of the interface the confined code can attack (a few virtualised devices versus a full syscall table versus a shared address space), what is shared across the boundary (a dedicated kernel, a shared kernel, or the same process), and how many independent bugs an escape requires — one or a chain. _This is the axis the industry over-indexes on; it belongs in the taxonomy, but it is one axis of eight, not the scoreboard._

**4\. Authority scope.** What does the workload legitimately hold _inside_ the boundary — credentials scoped to the account, the task, or the single action; files mounted wholesale or per-need; secrets present in the environment or held outside and injected per use? Two sandboxes with identical walls can differ enormously here.

**5\. Egress and mediation.** Can the workload reach the outside world directly, or only through a broker that can filter, allowlist, require approval, or log? _For agents this may be the most consequential axis of all, since their characteristic failure is a legitimate-looking outbound action._

**6\. Trust direction.** Who is being protected from whom — the host from the workload, co-tenants from each other, the workload's own assets from a compromised component, or the user from the agent's mistakes? _Most sandbox debates are secretly disagreements about this axis: two people grading the same design differently because they are scoring different threats._

**7\. Persistence.** Does state survive beyond the task or session? A fresh environment per task bounds how long a compromise, a poisoned context, or an accumulated over-grant can live — restriction in time, where the other axes restrict in space. Snapshots and rollback often travel with ephemeral designs, but they are recovery controls rather than confinement: they undo nothing that has already left the boundary. _A sandbox should not get credit for them._

**8\. Boundary mutability.** Can the privilege set change after the sandbox is applied — and if so, in which direction, and under whose authority?

Conventional sandbox designs are monotonic: the full privilege set is declared before execution begins, restrictions are irreversible for the lifetime of the workload, and privileges may only be reduced, never extended. This model is suitable for workloads whose resource requirements are fully enumerable at initialisation.

Agent workloads frequently do not meet that condition. The resources a task requires — packages to be installed, hosts to be contacted, files to be accessed — are often determined during execution rather than before it. A strictly static policy therefore forces a choice between under-provisioning, which blocks legitimate operations, and over-provisioning, which grants authority the task may never need and negates the intended granularity.

Where post-initialisation expansion is supported, four models are observed:

- **Re-instantiation:** The environment is destroyed and recreated under a new, explicitly broader policy.
- **Brokered grants:** An external privileged component evaluates requests and confers scoped, optionally time-limited additions.
- **Human-approved escalation:** Expansion requires confirmation by a party outside the workload's influence.
- **Self-service expansion:** The workload can extend its own privilege set.

A useful classification question for any design is whether the grant authority is reachable from inside the boundary. _If it is — as with self-service expansion, or in designs that expose an API for the workload to bypass its own restrictions on failure — enforcement has effectively moved from the enforcement layer to the policy layer, and the boundary functions as a default rather than a guarantee._

The first three axes describe _the wall_: where it is enforced, what it encloses, how hard it is to breach. The next three describe _what is inside and what gets out_: authority, egress, and who is protected. The last two capture _time_: how long state persists, and whether authority can grow. The industry has a rich vocabulary for the first group and grades everything with it — but agent incidents overwhelmingly happen in the second and third.

Nested, not ranked

In practice, strength and granularity are complements, not competitors. A well-designed system nests them: fine-grained sandboxes inside coarse, strong ones, so a browser runs Wasm-confined parsers inside per-site processes inside an OS sandbox, a cloud platform runs seccomp-restricted services inside containers inside microVMs — and an agent runs with task-scoped credentials and filtered egress inside a microVM. An attacker must then defeat a boundary at every level of granularity rather than a single boundary of any strength. That layered contract, not any one mechanism, is what the word "sandbox" is really about — for agents as much as for anything that came before them.

nono is available under Apache 2.0 at [nono.sh](https://nono.sh/) and on GitHub at [github.com/nolabs-ai/nono](https://github.com/nolabs-ai/nono). Documentation and getting-started guides are at [nono.sh/docs](https://nono.sh/docs).

* * *

About nolabs

nolabs is building trust infrastructure for AI. Our enterprise agent security platform runs the open-source nono runtime at scale, turning runtime boundaries into a system of record for security, platform, and compliance teams. Get in touch: [info@nolabs.ai](mailto:info@nolabs.ai).

1. “Workload” is the best word we have for something genuinely hard to name: the thing being confined varies from an entire operating system down to a single function, and no single term fits all of them comfortably. Read it here in its widest sense — whatever executes inside the boundary. [↩](https://nolabs.ai/blog/sandbox-primer#fnref-workload)

## Keep reading

[![](https://nolabs.ai/_next/image?url=%2Fblog%2Fimages%2Fblog-nono-kubernetes-agent-sandbox.png&w=3840&q=75)\\
\\
KubernetesSecurity\\
\\
**nono lands in the Kubernetes agent-sandbox** \\
\\
An official nono example now ships in Kubernetes agent-sandbox: pod isolation plus per-tool authority limits, verified by a signed audit trail on kind.\\
\\
![Luke Hinds](https://nolabs.ai/team/luke-hinds.png)\\
\\
Luke Hinds\\
\\
Co-founder & CEO·August 11, 2026](https://nolabs.ai/blog/nono-kubernetes-agent-sandbox) [![](https://nolabs.ai/_next/image?url=%2Fblog%2Fimages%2Fnolabs-launch.png&w=3840&q=75)\\
\\
LaunchSecurity\\
\\
**Sigstore Creator Launches nolabs to Stop AI Agents Running Wild** \\
\\
nolabs' open source tool nono creates a new foundational security layer for AI agents, allowing them to get work done without giving them dangerous levels of access.\\
\\
![nolabs Team](https://nolabs.ai/team/nolabs-mark.png)\\
\\
nolabs Team\\
\\
nolabs·July 21, 2026](https://nolabs.ai/blog/nolabs-launch) [![](https://nolabs.ai/_next/image?url=%2Fblog%2Fimages%2Fblog-assume-the-agent-is-compromised-now-what.png&w=3840&q=75)\\
\\
SecurityAI Agents\\
\\
**Assume the agent is compromised. Now what?** \\
\\
Prompt injection is not solved. Assume the agent is compromised—then bound what it can do. How nono contains the blast radius and proves every move.\\
\\
![Sal Kimmich](https://nolabs.ai/team/sal-kimmich.png)\\
\\
Sal Kimmich\\
\\
Solution Architect·July 16, 2026](https://nolabs.ai/blog/assume-the-agent-is-compromised)

## Now try it on your own agents

nono is open source and Apache‑2.0. Sandbox your agents in minutes — or talk to us about securing a fleet in production.

[Get started with nono](https://github.com/nolabs-ai/nono) [Chat with a founder](https://nolabs.ai/contact)
