---
date: '2026-08-20'
description: Dark is a groundbreaking open-source Mythic C2 agent designed for in-memory
  execution on macOS and Linux, addressing a critical gap in enterprise red teaming
  capabilities. Written in Crystal, it features a robust BOF loader without disk write
  artifacts. Its architecture circumvents typical EDR detection hurdles, utilizing
  unique methods such as a manually constructed Global Offset Table and compliance
  with hardware memory protections on Apple Silicon. Dark's efficient execution model
  leverages symbol resolution and concurrency, enabling seamless operator command
  execution. This tool represents a significant shift from traditional agent frameworks,
  emphasizing agility and stealth in modern security engagements.
link: https://minorimpact.dev/posts/dark-agent-coff-loader/
tags:
- C2 agent
- red teaming
- Crystal programming
- Mythic C2
- BOF execution
title: 'Dark: A Mythic C2 Agent with In-Memory BOF Execution on macOS and Linux, Part
  1 · Minor Impact'
---

![](https://minorimpact.dev/images/meteor.png)

![dark-agent](https://minorimpact.dev/images/posts/dark-agent-logo.svg)

## Welcome, Dark.

> _My background was in a world where you don't share your tools. You sharpen them, you protect them, and you definitely don't put them on GitHub. We'll see how this goes :-P. This is a part 1 intro, I intend on doing more if theres an appetite for it._

Dark has been used by the ServiceNow Red Team since 2024, back when people still wrote their own agent code…before the AI slop, vibe coded agent graveyard took over GitHub. It’s been on real boxes, it has real callbacks and has been operationally proven against modern defenses. Out of the box it ships with **25 BOFs and 15 built-in** commands.

While everyone is busy vibe coding agents and hype dunking “my AI hacked your company”, Dark has been quietly taking over the enterprise. Just code, written by a dude, that actually works.

![Hide the pain Harold meme about AI vibe coding](https://minorimpact.dev/images/posts/dark-agent-vibe-meme.png)

In-memory BOF execution has been a Windows TTP for years. On macOS and Linux? Almost nothing. Nobody’s filled that gap in any major open source Mythic C2 agent. Until now…

Dark is the first open source Mythic C2 agent, written in [Crystal](https://crystal-lang.org/), with a full in memory BOF loader for macOS (including Apple Silicon) and Linux. No disk writes or IOCs in file descriptions or tmp files and certainly no child processes. The BOF executes inside the existing agent process. The code is on GitHub: [github.com/ServiceNow/dark-agent](https://github.com/ServiceNow/dark-agent)

## Why no one else is doing this (and why it matters)

> I plan to expand on this section in great detail in a future post. This only scratches the surface

MacBooks are everywhere in enterprise. Linux runs everything behind the scenes. Neither has the detection maturity Windows has, and that’s exactly the point.

In memory COFF/BOF execution on Windows is a solved problem. `BOF.net` exists, TrustedSec has written a mountain of BOFs, the community is mature and well fed. What about macOS and Linux? Not so lucky… The format is different and apparently nobody wanted to spend their weekend doing what the dynamic linker does, by hand. Luckily enough, if you pour enough bourbon suddenly it sounds like a great idea.

Spoiler Alert! Do not recommend `0/5` stars lol.

- **ELF and Mach-O are not PE.** Linux and macOS use completely different object file formats. Different section layouts, different relocation models, different symbol conventions.
- **Trampolines.** Call instructions encode distance, not address. Too far away and the CPU silently jumps somewhere wrong. Built a thunk table into every mapped region to bridge the gap. The linker does this normally. I had to build it myself.
- **Global Offset Table, by hand.** Some relocations expect a pre-built symbol lookup table the linker provides. There is no linker so…each entry is a manual allocation handled one symbol at a time.
- **Apple Silicon enforces W^X in hardware.** A page is writable or executable, never both. `MAP_JIT` and `pthread_jit_write_protect_np` exist and are documented, but for JIT compilers, not BOF loaders. Nobody had applied them to in-memory object file execution before.
- **Crystal’s garbage collector had no idea what I was doing.** Nobody woke up and thought Crystal needs in-memory object file execution. I created a problem that had no existing solution.

## Crystal Lang is like, Ruby with a gym membership

Ruby is the best language, hands down :-) Python people are just, wrong. [Crystal](https://crystal-lang.org/) is Ruby’s compiled sibling. Close\`ish syntax but statically typed, LLVM backend, and a native (static or dynamic) linked binary.
If you’ve written Ruby, you can read Crystal. This is real Crystal code:

```crystal
hosts = ["dc01", "fs01", "ws10"]

hosts.select { |h| h.starts_with?("dc") }.each do |dc|
  puts "found domain controller: #{dc}"
end
```

The LLVM backend is what makes this interesting for offensive tooling. LLVM is the same compiler infrastructure under Clang, Rust, and Swift. It does dead code elimination, inlining, register allocation: all the optimizations that make C fast, applied to Crystal code automatically.

The Crystal community is small but serious…a high nerd-to-normal ratio. The kind of people who read compiler internals for fun.

## The payload is Dark on arrival

Lean and mean, the payload drops with limited offensive capability baked in. All it has is a BOF loader. A very polite, completely harmless looking piece of code that definitely isn’t about to map arbitrary code into memory and execute it. The files are sent over the C2 channel, the agent maps it, runs it, throws it away. Nothing is written to disk or random `memfd` backed file descriptors. No forked process or subprocesses spawned. The BOF runs entirely inside the existing process.

Compare that to [Poseidon](https://github.com/MythicAgents/poseidon), the Go-based Mythic agent. Poseidon is a trident: every capability forged into the binary before it ships. Portscan, keyloggers, screenshot, lateral movement tools. All compiled in, sitting on disk, waiting for someone to take a peek.

> Poseidon shows up with every toy in the bag while Dark shows up and knocks the bag off the table. (C’mon, its hard to not throw some cat puns around) Also totally not a dig at Poseidon, its a solid well-built C2 agent.

## What this is not

**Not an EDR bypass.** Though it hasn’t been detected yet /shrug. Come on EDR, we’re rooting for you. ;)

![I am the captain now meme - EDR vs Dark](https://minorimpact.dev/images/posts/dark-edr-meme.png)

**Not a packer.** The binary ships as is. If the Crystal runtime gets signatured or static analysis reveals common mythic callback strings, that’s **your** tradecraft problem. The runtime is small, the binary is clean (ish), and I’ve gotten it past production EDR stacks with minimal effort. Put in the work, you’ll be fine.

**No sleep masking or obfuscation.** No header stomping, no encrypted sleep, no in-memory evasion between callbacks. This was out of scope by design. You could easily do this with a loader (a Mythic wrapper). It’s been done before ;-)

## Under the Hood

Dark manages BOFs in a memory registry that handles all symbol mapping at runtime.

> A BOF is a compiled C program, stripped down to a single object file, that runs inside an existing process instead of spawning its own. No new process. No binary on disk. It borrows the agents memory, does its job, and disappears.

Typical workflow looks like this:

1. `bof_load` pulls the compiled object from Mythic’s file store over C2 channel and registers it in the agent’s BofRegistry as raw bytes. Nothing is mapped into executable memory yet
2. `bof_list` shows what’s loaded and ready
3. `bof_exec` fires a loaded BOF; you can run it as many times as you want without re-uploading. Symbols are resolved, architecture-specific setup runs, executable code maps into memory, and process execution jumps into the BOF entrypoint code within the system memory. After BOF execution the memory mapping is torn down and the output is collected.
4. `bof_unload` cleans up a specific BOF from the registry while `bof_purge` clears everything

> All included BOFs are loadable via Mythic’s `load` command and made available via the bof’s name as a command.

### It Actually Works

![Dark agent debug output showing BOF load and execution](https://minorimpact.dev/images/posts/dark-agent-debug.png)Dark Agent Debug Agent startup, beacon shim registration, and BOF download, load, execute sequence

### Symbol resolution

When a BOF is attempting to use external system calls or functions not locally defined (`malloc`, `BeaconPrintf`), the agent begins searching for its definition in this order:

1. Dark’s internal Beacon API
2. The agent’s own runtime via `dlsym` or local includes
3. Everything loaded into the process via `RTLD_DEFAULT`: dylibs, shared objects, anything the dynamic linker has mapped

```crystal
private def resolve_symbol(symbol : Symbol) : UInt64
  if callback_addr = Callbacks.lookup(symbol.name)
    return callback_addr
  end

  # macOS SDK headers embed a leading _ via __asm("_name").
  # dlsym expects the name without it. Double-underscore prefixes
  # (__stack_chk_guard etc.) must be left intact.
  lookup_name = (symbol.name.starts_with?("_") &&
                 symbol.name.size > 1 &&
                 symbol.name[1] != '_') \
    ? symbol.name[1..] : symbol.name

  if addr = LibC.dlsym(nil, lookup_name)
    return addr.address.to_u64
  end

  rtld_default = Pointer(Void).new(-2)
  if addr = LibC.dlsym(rtld_default, lookup_name)
    return addr.address.to_u64
  end

  raise Error.new("Could not find symbol #{symbol.name} in any library")
end
```

![Pepe Silvia meme - THE SYMBOLS THEY'RE ALL CONNECTED](https://minorimpact.dev/images/posts/dark-symbols-meme.png)

**Beacon API shims.** BOFs written for Cobalt Strike use `BeaconPrintf` and `BeaconOutput` to send results back. Dark Agent implements these as Crystal closures registered at the addresses the BOF finds during symbol resolution. When the BOF calls `BeaconPrintf`, it’s calling into the agent, which captures the output and ships it to Mythic as the task result.

### Concurrent execution

Multiple BOFs can run at the same time. Each `bof_exec` spawns a thread and registers it in the job table under its Mythic task ID. A BOF throwing an error doesn’t wreck the other jobs. A BOF segfaulting and murdering the process is still a BOF segfaulting and murdering the process. Don’t write bad BOFs.

```crystal
thread = Thread.new do
  begin
    ObjectFile.new(IO::Memory.new(entry.raw_bytes), args_to_use)
    result_channel.send(0)
  rescue ex
    log_debug("BOF '#{name}' failed in thread: #{ex.message}")
    result_channel.send(ex)
  ensure
    @@job_mutex.synchronize { active_jobs.delete(task_id) }
  end
end
```

```json
{
  "jobs": [\
    { "task_id": "a1b2c3", "bof_name": "portscan", "duration": "00:01:42" },\
    { "task_id": "d4e5f6", "bof_name": "ps",       "duration": "00:00:03" }\
  ]
}
```

### Built for the Operator

Most of the agent commands use Mythic’s `Browser Scripts` to return usable output in the Mythic UI.

![Dark agent df command output showing filesystem usage](https://minorimpact.dev/images/posts/dark-agent-df.png)df filesystem usage, color-coded by utilization.

The browser scripts add a layer on top. `ps` doesn’t just list processes, it tells you what to care about. Security tooling, EDR processes, containers, anything running with args that shouldn’t be there gets flagged in place.

![Dark agent ps output with browser script highlighting suspicious processes](https://minorimpact.dev/images/posts/dark-agent-ps.png)ps with browser script highlights processes we've learned to care about over time. `falcond`, `rsyslogd`, EDR agents, containers. The stuff that matters when you're figuring out what you're up against.

There’s always that guy on your team that is “pretty sure” about a command and goes full YOLO. Two person integrity (TPI) is for that guy. `shell` doesn’t run until someone else says so.

![Dark agent two person integrity flow for shell command](https://minorimpact.dev/images/posts/dark-agent-tpi.png)two person integrity`shell` blocks until a second operator approves. Then it runs.

### Artifact Tracking

Dark tries to map and track Indicators of Compromise (IOCs) it generates. File reads, file writes, processes started, stopped, etc. Anything that leaves a mark gets registered in Mythic’s artifact tracker automatically. When the op is over you know exactly what needs to be cleaned up, or what to hand your blue team for detection improvement.

![Dark agent upload and cat commands in Mythic console](https://minorimpact.dev/images/posts/dark-artifact-console.png)upload + cat file uploaded and read from the target![Mythic artifact tracker showing file read and write IOCs registered by Dark](https://minorimpact.dev/images/posts/dark-artifact-tracker.png)artifact tracker both the file write and file read logged automatically. Task ID, operator, host, path.

## Plug and Pwn (sneak peek into BOFs)

Of course the BOFs entrypoint is `coffee()`. The primary goal here was to remain familiar with what operators already build against. Here’s the simplest possible BOF. It prints a coffee cup. It is completely useless in an engagement and absolutely mandatory in a loader.

```c
#include "includes/beacon.h"

void coffee() {
    const char coffee[] =
      "\n"
      "        ( (      \n"
      "        ) )      \n"
      "     .______.    \n"
      "     |      |]   \n"
      "     \\      /    \n"
      "      `----'     \n";

    BeaconOutput((char*)coffee, sizeof(coffee) - 1);
}
```

### Live in Mythic, COFFee’s Hot

![Mythic console showing Dark agent callback with coffee BOF executing](https://minorimpact.dev/images/posts/dark-agent-mythic.png)Mythic Console live callback on target, BOF loaded via `load coffee`, executed, confirmed in `bof_list`.

A more practical example:

```c
#include "beacon.h"

void coffee() {
    char hostname[256];
    gethostname(hostname, sizeof(hostname));
    BeaconPrintf(CALLBACK_OUTPUT, "Hostname: %s", hostname);
}
```

### Single Docker container, cross-compiled output

Write your BOF once. Get four object files. Load whichever one matches the target. No Mac required in your build pipeline. Zig ships with Apple’s SDK headers and produces valid Mach-O object files from a Linux container. Mythic builds it all inside Docker automatically, across all four targets: macOS arm64, macOS x86-64, Linux arm64, Linux x86-64.

## A word about your C2 profile

Two profiles ship out of the box.

- [HTTP](https://github.com/MythicC2Profiles/http) gets you off the ground fast.
- [HTTPX](https://github.com/MythicC2Profiles/httpx) gives you malleable profiles.

**Malleable C2 Profiles** let you shape exactly what your C2 traffic looks like on the wire. Your callback payload can live in a cookie, a custom header, or a rotating URI. You can XOR it, base64 it, and wrap it in a response that looks like it came from a CDN. Multiple callback domains with automatic failover means losing a redirector doesn’t burn the op.

If your red team is still running boring HTTP profiles, you’re not simulating an APT. Real threat actors put work into their C2 traffic. Malleable profiles are how you close that gap and give your blue team something worth training against.

A working jQuery profile is included in the repo at [httpx-profile.json](https://github.com/ServiceNow/dark-agent/blob/main/httpx-profile.json). A full list of built-in commands and BOFs is in the [README](https://github.com/ServiceNow/dark-agent/blob/main/README.md).

## Any who, thanks!

Thanks to the ServiceNow Red Team for the operational runway and the Crystal community on Discord for not being too curious about my questions about why I needed to execute object files in memory…

Part 2 is coming. Until then, go break it. Open an issue, write a bad BOF, segfault the agent. That’s how this gets better. Code is at [github.com/ServiceNow/dark-agent](https://github.com/ServiceNow/dark-agent).

## References

- [https://www.servicenow.com](https://www.servicenow.com/)
- [https://crystal-lang.org](https://crystal-lang.org/)
- [https://github.com/trustedsec/CS-Situational-Awareness-BOF](https://github.com/trustedsec/CS-Situational-Awareness-BOF)
- [https://github.com/trustedsec/COFFLoader](https://github.com/trustedsec/COFFLoader)
- [https://github.com/its-a-feature/Mythic](https://github.com/its-a-feature/Mythic)
- [https://github.com/its-a-feature/ReflectiveLoader](https://github.com/its-a-feature/ReflectiveLoader)

![](https://minorimpact.dev/posts/dark-agent-coff-loader/)
