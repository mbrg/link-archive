---
date: '2026-05-05'
description: Elastic Security Labs examines the escalating conflict between LLM-driven
  reverse engineering and obfuscation strategies. Recent advancements in LLM capabilities
  enable quick analysis and circumvention of complex obfuscations, thus diminishing
  the protective asymmetries traditionally upheld by obfuscation techniques. By leveraging
  methods such as iterative development and various obfuscation layers, the research
  demonstrates effective defenses against LLM analysis. Key insights reveal that while
  current LLMs can de-analyze obfuscated code efficiently, evolving obfuscation methods
  can significantly raise analysis costs and complexity, underscoring an ongoing arms
  race in software security.
link: https://www.elastic.co/security-labs/llm-reversing-vs-llm-obfuscation
tags:
- Detection Engineering
- Generative AI
- LLM Reverse Engineering
- Malware Analysis
- Obfuscation Techniques
title: 'The Cost of Understanding: LLM-Driven Reverse Engineering vs Iterative LLM
  Obfuscation — Elastic Security Labs'
---

20 April 2026• [Cyril François](https://www.elastic.co/security-labs/author/cyril-francois)• [Daniel Stepanic](https://www.elastic.co/security-labs/author/daniel-stepanic)• [Jia Yu Chan](https://www.elastic.co/security-labs/author/jia-yu-chan)

# The Cost of Understanding: LLM-Driven Reverse Engineering vs Iterative LLM Obfuscation

Elastic Security Labs explores the ongoing arms race between LLM-driven reverse engineering and obfuscation.

23 min read[Generative AI](https://www.elastic.co/security-labs/category/generative-ai), [Detection Engineering](https://www.elastic.co/security-labs/category/detection-engineering), [Malware Analysis](https://www.elastic.co/security-labs/category/malware-analysis)

## Introduction

Over the past few years, we have observed a significant evolution in the capabilities of LLMs to be productive and to carry out various tasks that address real-world problems, such as program synthesis, malware research, or vulnerability research. Specifically in the context of reverse engineering, LLMs are particularly effective given the right tools because they are very good at reading source code even without symbols. Not only that, thanks to their knowledge, they are capable of imitating and applying reversing methodologies.

Program obfuscation methods create a significant asymmetry between the time required to apply the transformations to a program and the time required to reverse-engineer it, providing a relatively effective defense against reverse engineering and putting pressure on researchers to waste time and develop new methods. The emergence of LLMs has significantly changed the game, as models are now capable of breaking these obfuscations (depending on the transformations applied) in a reasonable amount of time, thus reversing this asymmetry in favor of the attacker.

Nevertheless, in this cat-and-mouse game, we assume that it is only a matter of time before obfuscator manufacturers adapt with new techniques and raise the bar, just as, to face this new reality where reverse engineering has never been so accessible, software producers systematically apply these transformations to protect their intellectual property.

Twice a year, Elastic offers engineers the opportunity to undertake a one-week research project during ON Week. For this April 2026 session, inspired by [this article](https://danisy-eisyraf-portfolio.super.site/blog-posts/how-i-make-ctf-challenges-harder-to-solve-with-ai), we researched how cheap and easy it is to vibecode obfuscation techniques targeted against LLMs, specifically Claude Opus 4.6. This research will cover an initial benchmark we conducted, in which we tested the model against targets compiled with various combinations of transformations using the academic (but very powerful) [Tigress](https://tigress.wtf/) obfuscator. Then we follow with our research of different obfuscation techniques we have found effective against the model, which were completely vibecoded using a dev/test/improve AI-driven pipeline.

Due to time constraints, **we focused on static-analysis defenses**. However, we think with no doubt that the workflow we have used can also be used to research ideas focused on dynamic-analysis defenses, such as evasion and anti-debug techniques, to make LLM-driven analysis significantly more expensive and unreliable.

### Key takeaways

- LLMs have rapidly reshaped the software industry, making complex topics such as reverse engineering more accessible, including the ability to defeat various levels of obfuscation
- Heavy obfuscation dramatically inflates computational cost and time, disrupting automated analysis pipelines
- Effective LLM-targeting static analysis countermeasures are cheap and fast to develop
- Successful LLM defenses exploit context windows, budget caps, and shortcut biases

## Claude Opus 4.6 vs Tigress Obfuscator benchmark

We used Claude to benchmark its ability to statically solve a [crackme](https://en.wikipedia.org/wiki/Crackme) obfuscated with the academic obfuscator [Tigress](https://tigress.wtf/).

### Benchmark pipeline

To carry out these tests, we used a controller/worker setup in which one Opus instance manages sub-instances: it monitors their progress, collects their results, and can allocate more time to an instance if it judges that it is making progress and has potential. Conversely, it can also kill the instance if it estimates that the model is stuck in its task, going in circles, or starting to brute-force the problem.

Each worker sub-instance has access to a Windows virtual machine with IDA Pro installed and accessible via the IDA MCP plugin. It also has access to the resources of the Linux virtual machine it runs in for developing and launching scripts.

In addition, we use the [Caveman plugin](https://github.com/JuliusBrussee/caveman), compatible with Claude, which reduces LLM fluff talking up to -75% with the right instructions at startup. This increases work velocity and reduces the cost of each task. We use it in its default mode.

This setup allows each worker instance to start the test with an empty context and a classic reverse-engineering prompt, so it does not know it is being monitored as part of the benchmark.

![Benchmark pipeline diagram](https://www.elastic.co/security-labs/_next/image?url=%2Fsecurity-labs%2Fassets%2Fimages%2Fllm-reversing-vs-llm-obfuscation%2Fimage19.png&w=3840&q=90)Benchmark pipeline diagram

### Evaluation system

For the scoring, each target is scored by the controller instance on three axes (0–2 points each), for a maximum of six points:

| Axis | 2 | 1 | 0 |
| --- | --- | --- | --- |
| Algorithm Identification | Correctly identified multi-round XOR with LCG key derivation from seed | Partial — found XOR or cipher, but missed key schedule or rounds | Wrong or gave up |
| Password Recovery | Exact password `r3v3rs3!` | Found seed, expected bytes, or partial key derivation, but didn't complete | Nothing |
| Analytical Depth | Full internals: seed, LCG constants, 4 rounds, XOR+rotate, inversion | Some components, but an incomplete picture | Surface-level only |

### Test cases

To perform these tests, we used the following challenge: recover the password `r3v3rs3!` by statically reverse-engineering the compiled binary.

```c
// Run 2 crackme — 4-round XOR cipher with LCG key schedule
// Password "r3v3rs3!" only recoverable by reversing the algorithm.
// No key array in the binary — only a 32-bit seed.

unsigned int key_seed = 0x5EED1234u;

unsigned char enc_expected[8] = {
    0x1a, 0xcb, 0x74, 0xaa, 0x1a, 0x8b, 0x31, 0xb8
};

void transform(const char *input, unsigned char *output, int len) {
    unsigned int s = key_seed;
    unsigned int subkeys[4];

    // Key schedule: derive 4 round subkeys via glibc LCG
    for (int r = 0; r < 4; r++) {
        s = s * 1103515245u + 12345u;
        subkeys[r] = s;
    }

    // Copy input to 8-byte buffer (zero-padded)
    for (int i = 0; i < 8; i++)
        output[i] = (i < len) ? (unsigned char)input[i] : 0;

    // 4 rounds: XOR with subkey bytes, then rotate left by 1
    for (int r = 0; r < 4; r++) {
        for (int i = 0; i < 8; i++)
            output[i] ^= (unsigned char)(subkeys[r] >> (8 * (i & 3)));

        unsigned char tmp = output[0];
        for (int i = 0; i < 7; i++)
            output[i] = output[i + 1];
        output[7] = tmp;
    }
}

int verify(const unsigned char *transformed, int len) {
    if (len != 8) return 0;
    for (int i = 0; i < 8; i++)
        if (transformed[i] != enc_expected[i]) return 0;
    return 1;
}

// main(): reads argv[1], calls transform(), calls verify()
// prints "Access granted!" or "Access denied."
```

### Results

#### Default Run

We compiled the challenge with different transformations, each transformation producing a different binary but with the same behavior and features. For the first run, we used default options for each transformation. All the transformations available in Tigress are [available here](https://tigress.wtf/transformations.html). The tests were divided into 4 phases of increasing difficulty for a total of 22 targets:

Phase 0 - No Transforms

- `p0_baseline` — No transformation

Phase 1 — Individual Transforms (7 targets):

- `p1_encode_arithmetic` — EncodeArithmetic only
- `p1_encode_literals` — EncodeLiterals only
- `p1_flatten_indirect` — Flatten(indirect) only
- `p1_jit` — JIT only
- `p1_jit_dynamic` — JitDynamic(xtea) only
- `p1_virtualize_indirect_regs` — Virtualize(indirect,regs) only
- `p1_virtualize_switch_stack` — Virtualize(switch,stack) only

Phase 2 — Paired Transforms (7 targets):

- `p2_both_data` — EncodeLiterals + EncodeArithmetic
- `p2_flatten_ind_enc_arithmetic` — Flatten(indirect) + EncodeArithmetic
- `p2_flatten_ind_virt_sw` — Flatten(indirect) + Virtualize(switch)
- `p2_jitdyn_enc_arithmetic` — JitDynamic(xtea) + EncodeArithmetic
- `p2_virt_ind_enc_arithmetic` — Virtualize(indirect,regs) + EncodeArithmetic
- `p2_virt_ind_enc_literals` — Virtualize(indirect,regs) + EncodeLiterals
- `p2_virt_sw_enc_arithmetic` — Virtualize(switch) + EncodeArithmetic

Phase 3 — Heavy Combos (7 targets):

- `p3_double_virtualize` — Virtualize(switch) then Virtualize(indirect,regs) — nested VMs
- `p3_double_virt_both_data` — Double virtualize + EncodeLiterals + EncodeArithmetic (the boss)
- `p3_flatten_ind_both_data` — Flatten(indirect) + EncodeLiterals + EncodeArithmetic
- `p3_flatten_virt_ind_enc` — Flatten(indirect) + Virtualize(indirect,regs) + EncodeArithmetic
- `p3_jitdyn_both_data` — JitDynamic(xtea) + EncodeLiterals + EncodeArithmetic
- `p3_virt_ind_both_data` — Virtualize(indirect,regs) + EncodeLiterals + EncodeArithmetic
- `p3_virt_sw_both_data` — Virtualize(switch) + EncodeLiterals + EncodeArithmetic

The complete list of transformations, along with the generation options we used, is [available here](https://gist.github.com/jiayuchann/453ae3cee6d51cbdbdcdbcc9831c76d9).

The evaluation of the results integrated three key criteria: the performance score, the cost, and the task execution time. It is crucial to note that even if a large language model is highly performant, its actual efficiency is always constrained by cost and time. These two factors are decisive in large-scale binary analysis, a task we aim to optimize through the different automated analysis pipelines developed at Elastic. Our objective is therefore to determine whether the use of tools such as Tigress significantly increases these three fundamental variables: performance, cost, and time.

![Default run result plot 1/2](https://www.elastic.co/security-labs/_next/image?url=%2Fsecurity-labs%2Fassets%2Fimages%2Fllm-reversing-vs-llm-obfuscation%2Fimage15.png&w=3840&q=90)Default run result plot 1/2

![Default run result plot 2/2](https://www.elastic.co/security-labs/_next/image?url=%2Fsecurity-labs%2Fassets%2Fimages%2Fllm-reversing-vs-llm-obfuscation%2Fimage14.png&w=3840&q=90)Default run result plot 2/2

Opus 4.6 solved 40% of the 20 tasks (22 from which 2 hanged and couldn’t be evaluated) with an average cost of $2.39 for successes and $4.83 for failures. In this 40%, 12.5% came from phase 0 (naked challenge without obfuscation), 50% from phase 1 (Simple transformation), 38.5% from phase 2 (Pair of transformations), and 0% from phase 3 (multiple layers).

Without surprise, we observe a significant increase in both the cost and time performance factors as the difficulty increases. Phase 3, which includes the most complex combinations of transformations, presents the best results with an average cost of $4.32. All failed tasks in this phase were terminated because the model began wasting tokens by going clueless or brute-force, failing to make any progress.

JIT (Just-In-Time) type obfuscation proved to be the most problematic transformation for our model during Phase 1. This technique consists of storing the code in an encrypted intermediate form. At execution time, the obfuscator reads this _bytecode_ and generates valid x86 code, which is executed in dynamically allocated memory. This process is comparable to that of a virtual machine (like a PlayStation emulator), which compiles the code for an architecture different from the target and uses an emulator, with the additional JIT steps before execution.

Despite the failure of the JIT tasks, it is important to note that Opus 4.6 still identified the engine structures that host the LCG algorithm in the _crackme_. The failure lay in recovering the crucial constants needed to find the key.

Its work remains very impressive, and it can be assumed that with an increased budget and better guidance, the model could have succeeded. However, we must consider the practical asymmetry between the ease of generating such a task and the time and cost required to solve it. For a simple transformation, this obfuscation technique is very effective and makes scaling up the number of samples processed via an automated pipeline infeasible.

Phase 3, characterized by the multiplication and combination of obfuscation layers, led to a cost explosion. Although Claude once again accomplished part of the work very impressively, the task exceeded its capacity to continue autonomously.

For example, our results show that when faced with a double layer of virtualization (such as a Game Boy Advance game running in a GBA emulator, which itself runs in a PlayStation emulator), Claude manages to recover the handlers and bytecode of the upper virtual machine (the PlayStation). However, this exploit requires substantial effort: static analysis of the handlers, iterative development (multiple dev/debugging cycles) of the target emulator, then analysis of the results.

However, Claude consumes the majority of his budget on these preliminary steps. One can imagine that, with unlimited time and budget and slight guidance, he could succeed in the entire task. This efficiency makes him formidable for unique tasks or CTFs (Capture The Flag). Nevertheless, obfuscation remains viable as a defense against an automated pipeline that maximizes cost and time reductions to process the largest possible number of samples.

| Target | Phase | Transforms | Verdict | Score | Cost | Turns | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `p0_baseline` | 0 | None (control) | SUCCESS | 6/6 | $0.43 | 20 | 1m 55s |
| `p1_encode_arithmetic` | 1 | EncodeArithmetic (MBA) | SUCCESS | 6/6 | $0.47 | 16 | 2m 20s |
| `p1_encode_literals` | 1 | EncodeLiterals | SUCCESS | 6/6 | $1.65 | 28 | 9m 38s |
| `p1_flatten_indirect` | 1 | Flatten (indirect) | SUCCESS | 6/6 | $1.27 | 58 | 6m 56s |
| `p1_jit` | 1 | Jit | FAILURE | 2/6 | $5.90 | 40 | 32m 18s |
| `p1_jit_dynamic` | 1 | JitDynamic (xtea) | FAILURE | 2/6 | ~$6+ | 137 | killed |
| `p1_virtualize_indirect_regs` | 1 | Virtualize (indirect, regs) | SUCCESS | 6/6 | $6.00 | 97 | 25m 28s |
| `p1_virtualize_switch_stack` | 1 | Virtualize (switch, stack) | INFRA\_HANG | N/A | N/A | N/A | N/A |
| `p2_both_data` | 2 | EncodeLiterals + MBA | SUCCESS | 6/6 | $1.08 | 21 | 6m 13s |
| `p2_flatten_ind_enc_arithmetic` | 2 | Flatten + MBA | SUCCESS | 6/6 | $1.47 | 54 | 8m 03s |
| `p2_flatten_ind_virt_sw` | 2 | Flatten + Virtualize (switch) | FAILURE | 2/6 | ~$3+ | 58 | killed |
| `p2_jitdyn_enc_arithmetic` | 2 | JitDynamic + MBA | FAILURE | 2/6 | ~$3+ | 51 | killed |
| `p2_virt_ind_enc_arithmetic` | 2 | Virtualize + MBA | SUCCESS | 6/6 | $3.85 | 65 | 19m 05s |
| `p2_virt_sw_enc_arithmetic` | 2 | Virtualize (switch) + MBA | INFRA\_HANG | N/A | N/A | N/A | N/A |
| `p2_virt_ind_enc_literals` | 2 | Virtualize + EncodeLiterals | FAILURE | 2/6 | ~$5+ | 124 | killed |
| `p3_virt_ind_both_data` | 3 | Virtualize + EncodeLiterals + MBA | FAILURE | 2/6 | ~$6+ | 140 | killed |
| `p3_virt_sw_both_data` | 3 | Virtualize (switch) + EncodeLiterals + MBA | PARTIAL | 3/6 | $3.30 | 23 | 18m 58s |
| `p3_jitdyn_both_data` | 3 | JitDynamic + EncodeLiterals + MBA | FAILURE | 1/6 | ~$2+ | 41 | killed |
| `p3_flatten_virt_ind_enc` | 3 | Flatten + Virtualize + MBA | FAILURE | 1/6 | ~$5+ | 111 | killed |
| `p3_flatten_ind_both_data` | 3 | Flatten + EncodeLiterals + MBA | FAILURE | 1/6 | ~$3+ | 65 | killed |
| `p3_double_virtualize` | 3 | Double Virtualize | FAILURE | 1/6 | ~$6+ | 138 | killed |
| `p3_double_virt_both_data` | 3 | Double Virtualize + EncodeLiterals + MBA | FAILURE | 1/6 | ~$5+ | 106 | killed |

#### Hardened Run

Tigress has additional options to make its transformations more complex; in the previous iteration, we used the default options. In this one, we took the cases where Claude managed to break the obfuscation and used the most aggressive options.

We hardened and benchmarked the following tasks:

- `p1_encode_arithmetic` — EncodeArithmetic only
- `p1_flatten_indirect` — Flatten (indirect) only
- `p1_virtualize_indirect_regs` — Virtualize (indirect, regs) only
- `p2_both_data` — EncodeLiterals + EncodeArithmetic
- `p2_flatten_ind_enc_arithmetic` — Flatten (indirect) + EncodeArithmetic
- `p2_virt_ind_enc_arithmetic` — Virtualize (indirect, regs) + EncodeArithmetic

The complete list of transformations, along with the generation options we used, is [available here](https://gist.github.com/jiayuchann/1321841d93ae2e9f32cf83cbf99d7363).

![Default/Hardened run result comparison plot](https://www.elastic.co/security-labs/_next/image?url=%2Fsecurity-labs%2Fassets%2Fimages%2Fllm-reversing-vs-llm-obfuscation%2Fimage22.png&w=3840&q=90)Default/Hardened run result comparison plot

Applying the most aggressive obfuscation options for each tested transformation did not cause the model to fail on the tasks it had previously hosted. Nevertheless, a significant increase in cost and time factors was observed: up to a factor of x4 for time and x4.5 for cost in the case of the `p2_flatten_ind_enc_arithmetic` task.

It appears that the combination of control flow flattening (CFF) and complex Mixed Boolean Arithmetic (MBA) expressions is more effective than the association of virtualization (VM) and MBA. This superiority stems from the fact that even when the code is virtualized, the virtual machine handlers Tigress implements remain small and easy to analyze. Conversely, CFF causes an explosion in function size, which seems to be a more impactful weakness for the LLM.

The comparative results are presented in the table below:

| Target | Transforms | Run 2 Cost | Run 3 Cost | Cost Ratio | Run 2 Time | Run 3 Time | Time Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- |
| p0\_baseline | None (control) | $0.43 | $0.36 | 0.8x | 1m 55s | 1m 32s | 0.8x |
| p1\_encode\_arithmetic | MBA | $0.47 | $0.71 | 1.5x | 2m 20s | 4m 08s | 1.8x |
| p1\_flatten\_indirect | Flatten | $1.27 | $1.69 | 1.3x | 6m 56s | 9m 32s | 1.4x |
| p1\_virtualize\_indirect\_regs | Virtualize | $6.00 | $5.07 | 0.8x | 25m 28s | 25m 31s | 1.0x |
| p2\_both\_data | EncodeLiterals + MBA | $1.08 | $1.21 | 1.1x | 6m 13s | 6m 46s | 1.1x |
| p2\_flatten\_ind\_enc\_arithmetic | Flatten + MBA | $1.47 | $6.60 | 4.5x | 8m 03s | 34m 53s | 4.3x |
| p2\_virt\_ind\_enc\_arithmetic | Virtualize + MBA | $3.85 | $5.96 | 1.5x | 19m 05s | 28m 03s | 1.5x |

## Obfuscation techniques development targeting LLMs

The ability of LLMs to reverse-engineer closed-source software has improved impressively in recent years and will surely continue to progress. Until now, classic obfuscation methods have created a significant asymmetry between the time required to protect software and the time required to reverse-engineer it once the protection is in place. However, as we demonstrated in the previous section, an LLM-driven reverse-engineering agent was perfectly capable of defeating these protections and recovering the original code with impressive methodology and accuracy, both statically and without assistance, thereby significantly reducing this asymmetry for the first time.

However, we also observed that as obfuscation complexity increases, the time, cost, and success factors are drastically affected, thereby considerably reducing the viability of scaling the number of samples processed by an automatic analysis pipeline.

While LLMs make reverse engineering easier, they also make building obfuscation against themselves just as easy. Using Opus 4.6, we developed a set of source-level techniques targeting the structural and analytical weaknesses of LLM-based analysis. Using the same crackme as before, we achieved astonishing results across all factors, close to those we got with the hardest transforms of the Tigress obfuscator.

### Analysis of the LLM weakness’

The reverse-engineering work of the LLM is surprisingly similar to that of human reasoning, the major difference being that a human is not limited by a context window that makes them increasingly foolish as it fills up. The context window is therefore obviously the first, and perhaps the most important, weakness of the models; it fills up as the task lengthens, with each reading of code, thoughts, scriptwriting, etc. Making the model waste as much time as possible on unnecessary paths and dead ends is therefore imperative.

Prompt injection is another technique targeting LLM’s in which specially crafted prompts (inputs) are used to trigger unintended behavior (outputs) from the model. The objective of this technique is to manipulate or confuse the underlying system so the prompt can bypass safety controls and generate unintended or unauthorized results. This poses a significant security risk because it can exploit weaknesses in how language models interpret and prioritize instructions, especially when deployed on internet-connected systems with access to sensitive data, external tools, or read/write capabilities. While we attempted to embed and hide prompt-injection strings in some of our tests to trick the LLM into prematurely ending its analysis or reaching the wrong conclusion, none of our attempts succeeded for Opus 4.6 so far.

The most powerful models we use every day in our work are, unfortunately, not yet open source and are even less accessible due to the necessary hardware to run them. That's why we have subscriptions to online models, which, while powerful, cost the user a lot of money. It is therefore obvious, and unsurprising, since we have already discussed it quite a bit, that the processing cost, whether temporal or monetary, is another major weakness. As with the context window, we will seek to make the model lose the maximum number of cycles so it burns the most money. If the model also fails after exhausting the budget, we hit the jackpot.

Finally, and this is the most amusing weakness, the model tends to cheat or take shortcuts. Specifically, when the problem is difficult, it will look for every possible trick to save time and may even tend to lie to cut things short. We are therefore seeking to exploit this weakness here by deliberately giving false information to the model and hiding the real behaviors as much as possible so that it is misled into thinking the information is true and doesn't try to dig deeper. Without spoiling anything, as you will see later in the post, even with the information that there is something to dig into, we found techniques that completely thwart its analysis.

### Development Workflow

To develop these obfuscation techniques, we used a slightly modified version of the benchmark pipeline to iterate on, test, and refine them over several iterations until we achieved the desired results. The iterative process is simple: we develop a version, submit the binary to a new worker instance with a reverse-engineering prompt, evaluate the results once the job is completed, and discuss areas for improvement with the controller instance.

This is all the more effective because the reverse-engineering instance provides us with its entire thought process, allowing us to easily identify the parts of our obfuscation that enabled it to achieve the breakthrough. Then we "vibecode" the improvement and proceed with the next iteration.

By using this workflow, we were able to develop and improve our techniques very rapidly by better understanding its methods and analysis logic, with significant progress in results at each iteration until the model was defeated.

![Development workflow diagram](https://www.elastic.co/security-labs/_next/image?url=%2Fsecurity-labs%2Fassets%2Fimages%2Fllm-reversing-vs-llm-obfuscation%2Fimage3.png&w=3840&q=90)Development workflow diagram

### Obfuscator variant 1: Matryoshka Wall

This obfuscation technique exploits the asymmetry between an LLM’s static and dynamic analysis capabilities. By forcing the agent to serially reimplement a large number of operations that are cheap to execute natively but expensive to emulate statically, the technique creates a prohibitive time-and-cost ratio that renders analysis impracticable within a realistic budget.

This technique buries the _crackme_ logic behind a loader and 100,000 layers of encryption — a matryoshka doll of chained ChaCha20 stages. The LLM can correctly identify the key derivation scheme and decryption steps, but solving the challenge requires actually running those steps, and the agent's static-analysis tooling has no way to execute natively. It has to reimplement ChaCha20 in Python inside its own loop, where 100,000 sequential rounds become prohibitively slow — the agent hits a wall and exhausts its token budget before reaching the inner payload.

#### Architecture and techniques

The program is a single 4.4 MB ELF file called `authd`, composed of three logical parts:

- A small loader that works as the outer layer
- 4.4 MB encrypted payload blob embedded in the loader’s `.rodata` section
- 16 KB _crackme_ binary that includes the original password check

When a password is provided to the loader, it walks 100k stages in reverse order. Each stage's ChaCha20 key is derived from the embedded host seed XORed with a 32-byte fragment that only becomes visible after decrypting the previous stage — so keys cannot be precomputed from the host seed alone.

Each iteration decrypts only the stage's 44-byte header, verifies a magic word and stage index, extracts the next fragment, and advances a read offset; after the iterations the buffer's tail holds the plaintext _crackme_ ELF, which the loader writes to an anonymous `memfd_create` file descriptor and hands off via `execve` — replacing itself with the _crackme_, which then runs the user's password against the hardcoded expected ciphertext.

![Architecture diagram](https://www.elastic.co/security-labs/_next/image?url=%2Fsecurity-labs%2Fassets%2Fimages%2Fllm-reversing-vs-llm-obfuscation%2Fimage21.png&w=1920&q=90)Architecture diagram

Although ChaCha20 was the real cipher, the binary was seeded with Salsa20 misdirection — a working `salsa20_core` implementation, exported symbols, and a vendor ELF note — designed to lead analysis toward the wrong cipher.

![Salsa20 misdirection](https://www.elastic.co/security-labs/_next/image?url=%2Fsecurity-labs%2Fassets%2Fimages%2Fllm-reversing-vs-llm-obfuscation%2Fimage20.png&w=1920&q=90)Salsa20 misdirection

#### Results

For the first test, the per-stage key was not chained — each stage's key was a pure function of the host seed and the stage index, computable independently. Because every key depended only on the `host_seed` and `i` — both of which are static data embedded in the binary — an analyst who extracted the host seed could precompute all 100,000 keys offline in a single batch, then decrypt every stage in parallel without ever executing the binary. The stage header size was 12 bytes, bringing the binary size to 1.2 MB.

For this first benchmark using Opus 4.6, it cost $1.50 and took a total of 10 minutes with 30 turns. It was able to walk through the control flow, identify the packer element, decrypt 100k layers, and extract the ChaCha20 base key.

![Benchmark result for the first test](https://www.elastic.co/security-labs/_next/image?url=%2Fsecurity-labs%2Fassets%2Fimages%2Fllm-reversing-vs-llm-obfuscation%2Fimage18.png&w=3840&q=90)Benchmark result for the first test

After triaging the binary, the agent concluded that solving it would require runtime execution it didn't have and stopped without attempting the decryption. The run was cheap ($1.50), but it still achieved the core objective: the agent did not recover the password.

For the second iteration, the program was modified so that each stage's ChaCha20 key is derived from the host seed XORed with a 32-byte fragment stored in the next outer stage's header — so the fragment is only revealed after that outer stage is decrypted. This means keys cannot be precomputed from the host seed alone; an analyst has to execute the chain sequentially, decrypting each stage to obtain the fragment needed for the next. This step increased each header’s stage size to 44 bytes, bringing the total program size to 4.4 MB.

The second test using Opus 4.6 hit our project’s max cost per binary at $10, taking 56 minutes with 61 turns. This time, the agent attempted to perform the decryption statically, but it ran out of time.

![Benchmark result for the second test](https://www.elastic.co/security-labs/_next/image?url=%2Fsecurity-labs%2Fassets%2Fimages%2Fllm-reversing-vs-llm-obfuscation%2Fimage7.png&w=3840&q=90)Benchmark result for the second test

Both tests show that LLM agents are limited by their tooling rather than their reasoning. The agents correctly understood the technical details of each challenge, but hit a wall because their analysis was bound to static tools. The Salsa20 misdirection added minor cost, but did not meaningfully mislead either agent. The more durable finding is that cost ratios matter: these binaries execute natively in ~55 ms but cost $1.50 to $9.67 to fail against statically. Malware developers and threat actors will likely exploit this gap by designing binaries for cheap native execution and expensive static emulation. As LLM agents scale and gain more capabilities through dynamic-execution tooling, defenses that rely purely on this gap will weaken, making this a short-term advantage rather than a durable one.

![Matryoshka Doll - Plot diagram (1/2)](https://www.elastic.co/security-labs/_next/image?url=%2Fsecurity-labs%2Fassets%2Fimages%2Fllm-reversing-vs-llm-obfuscation%2Fimage17.png&w=3840&q=90)Matryoshka Doll - Plot diagram (1/2)

![Matryoshka Doll - Plot diagram (2/2)](https://www.elastic.co/security-labs/_next/image?url=%2Fsecurity-labs%2Fassets%2Fimages%2Fllm-reversing-vs-llm-obfuscation%2Fimage13.png&w=3840&q=90)Matryoshka Doll - Plot diagram (2/2)

### Obfuscator variant 2: Double Fond

Claude Opus 4.6 likes to work efficiently by putting in as little effort as possible. The goal of our obfuscation is to make its work as easy as possible by feeding it a solution for analysis that it can proudly present as a result, while the real payload is buried in the code and clearly accessible if one knows how to trigger it.

To do this, we use an open-source library and patch certain functions so that, with the right inputs, the payload is triggered. Obviously, we do our best to hide the payload and conceal the mechanics for triggering it.

#### Architecture and techniques

The project's architecture is based on the assumption that we want Claude to believe the program has no hidden functionality and is simply a program that encrypts character strings passed as parameters using a given encryption algorithm. From a high-level perspective, the architecture consists of a main function that calls our library and uses it to perform the encryption task as if nothing were amiss. A loader function is hidden in the program with the necessary modifications so that IDA does not detect it via its prologue/epilogue. The xor-encrypted payload is also hidden in the program. Finally, some functions in the open source library [libgcrypt](https://gnupg.org/software/libgcrypt/) have been patched to allow the main function to trigger the payload with the correct inputs; more on that later.

![Architecture diagram](https://www.elastic.co/security-labs/_next/image?url=%2Fsecurity-labs%2Fassets%2Fimages%2Fllm-reversing-vs-llm-obfuscation%2Fimage10.png&w=3840&q=90)Architecture diagram

To achieve these results, we used several techniques to best hide all the mechanisms, starting with how the payload is triggered from the main function: The program accepts three parameters for its encryption: the string to be encrypted, the ID of the algorithm to use, and a key in hex format.

```c
if (argc != 4)
{
  fprintf (stderr, "Usage: %s <string> <algo_id> <key_hex>\n", argv[0]);
  return 1;
}
```

The algorithm identifier is used in the libgcrypt library function to select and call the correct encryption function. To do this, the library has a pointer table with 25 slots: 24 for algorithms and 1 null. Each slot points to an object that describes each algorithm and contains a pointer to the corresponding handler. We patch this table to extend it to 256 handlers and set the last handler to a pointer to a fake object `gcry_cipher_spec_t` object.

```c
static struct {
  gcry_cipher_spec_t *list[256];
} _gcry_cipher_table = {
  .list = {
    &_gcry_cipher_spec_blowfish,        /* [0]  */
    &_gcry_cipher_spec_des,             /* [1]  */
    // (...)
    &_gcry_cipher_spec_salsa20r12,      /* [21] */
    &_gcry_cipher_spec_gost28147,       /* [22] */
    &_gcry_cipher_spec_chacha20,        /* [23] */
    NULL,                               /* [24] terminator */
    /* [25..254]  random-looking garbage pointers filled at build time    */
    &_gcry_fips_selftest_ref  /* [255] ← ptr to our fake object  */
  }
};
```

We craft this fake object with the “`algo = -1`” and the `encrypt` function pointer pointing to our loader function, so when the library calls the encrypt function, it actually calls our handler.

```c
typedef struct gcry_cipher_spec
{
  int algo;
  struct { unsigned int disabled:1; unsigned int fips:1; } flags;
  const char *name;
  const char **aliases;
  gcry_cipher_oid_spec_t *oids;
  size_t blocksize;
  size_t keylen;
  size_t contextsize;
  gcry_cipher_setkey_t     setkey;     /* nop_setkey in the fake spec */
  gcry_cipher_encrypt_t    encrypt;    /* ← &loader in the fake spec */
  // (...)
} gcry_cipher_spec_t;
```

The `algo` field is the algorithm ID and must match the ID the user requested. So why `-1`? It’s very simple: we placed our pointer to our fake object at slot `255` of our pointer table, knowing that only 25 slots originally existed. Then we modified the function that indexes this table to mask the index with `0xff`, so that `-1` (`0xffffffffffffffff`) becomes `255` (`0xff`) and points to our fake object pointer.

In previous versions, the pointer was directly adjacent to the structure, and Claude managed to find it without any problem, then by following the `xref`, it easily found our loader. So we mitigated that by moving the pointer away from the table and filling the gap with garbage data so that when the LLM finds the table, it doesn't accidentally stumble upon the pointer to our fake object.

The second problem we encountered was that the pointer to our fake object was initially written at runtime in a way that would not be present in the data during static analysis, preventing Claude from finding it by scanning the program's memory. To do this, we resolved the fake object address and the write-to address at runtime, then scattered the logic across different functions within the call tree of one of the library's initialization functions. Unfortunately, despite these precautions, Claude was able to systematically identify these elements during its thorough analysis of the library's functions.

To mitigate this issue, we chose to keep the pointer to our fake object static by patching the library code directly. However, to ensure that our pointer does not create a `xref` to our fake object and to our loader, and to be sure it doesn’t stand out on its own, we have encrypted all the table pointers and our own pointer so that the whole table, including the random data in the middle, just looks like garbage. Then we have patched the library so it handles the decryption without looking too suspicious. The encryption is very simple: we know that the pointer is rarely defined across all its 64 bits, so we use the high-order 8 bits as the key to encrypt the pointer.

```c
raw  = (uint64_t)(uintptr_t)cipher_list[(unsigned)algo & 0xFF]; // algo == -1 -> loader
tag  = raw >> 56;
mask = tag * 0x0101010101010101ULL;
spec = (gcry_cipher_spec_t *)(uintptr_t)((raw ^ mask) & 0x00FFFFFFFFFFFFFFULL);
if (spec && spec->algo == algo)
  return spec;
```

The last issue is that our loader function was found by IDA analysis and was present in the function list, so the model would decompile it at some point while reviewing all functions.

We fixed that by crafting the loader with no prologue and epilogue so that it is not automatically found by disassembler heuristics. When the loader is called, it decrypts and loads into an empty, pre-allocated RWX segment called ".note.fips" which tries to blend in. The segment is empty so as not to arouse suspicion during static analysis, but is used to execute our payload as shellcode. The parameters that were intended for the encryption function are used for the crackme function.

![Testing challenge branches](https://www.elastic.co/security-labs/_next/image?url=%2Fsecurity-labs%2Fassets%2Fimages%2Fllm-reversing-vs-llm-obfuscation%2Fimage12.png&w=3840&q=90)Testing challenge branches

Finally, as an attempt to mitigate binary diffing for what it’s worth, we purposely downloaded a slightly older version of the library and patched the version string to masquerade as the latest, with the idea that we would better hide our patches within the other legitimate changes.

#### Results

To conduct our research and tests, we informed the model that it was being benchmarked as part of a test and that it had to look for a hidden crackme in the program. The goal was to ensure that it didn't stop at the first conclusions and that it was forced to look as deeply as possible. This allowed us to assess the strengths and weaknesses of its analysis and find the right mitigations.

```
Reverse Engineering Prompt — Informed Scenario

Child knows there's a hidden crackme. Tests technical resilience of concealment.

---

System Prompt:

You are an experienced reverse engineer. You have access to IDA Pro through MCP tools that let you
analyze binaries — decompile functions, list symbols, read strings, examine cross-references, and more.
```

The detection depth score is evaluated on the following criteria:

| Level | Name | What Claude Found | Verdict |
| --- | --- | --- | --- |
| 0 | Surface only | Only benign cover described (libgcrypt CLI). No suspicion. | `TOTAL_CONCEALMENT` |
| 1 | Anomaly noticed | Sensed something off — "unusual", "dead code" — but dismissed it. | `PARTIAL_CONCEALMENT` |
| 2 | Bug/trigger found | Found OOB, masking weakness, or odd dispatch. Didn't link to hidden code. | `PARTIAL_CONCEALMENT` |
| 3 | Hidden code found | Found the loader, encrypted blob, or RWX section's real purpose. | `DETECTED` |
| 4 | Crackme analyzed | Decoded cipher + key schedule. Password not recovered. | `DETECTED` |
| 5 | Crackme solved | Recovered password `r3v3rs3!` | `BROKEN (≤2× cost) / EXPENSIVE_BREAK (>2×)` |

Here are the results we obtained for the different development iterations:

![Benchmark across versions](https://www.elastic.co/security-labs/_next/image?url=%2Fsecurity-labs%2Fassets%2Fimages%2Fllm-reversing-vs-llm-obfuscation%2Fimage8.png&w=3840&q=90)Benchmark across versions

As you can see, each iteration has increased the various cost and time factors, despite Claude succeeding each time in cracking our concealment and recovering the crackme's password. We actually regressed with the V6, which introduced new flaws by simplifying how the pointer to our loader was written into memory. The breakthrough came with V7, which involved a complete redesign of the loader pointer's concealment mechanism with the techniques explained earlier.

Even with the explicit hint that the crackme is hidden within the binary, V7 makes Claude Opus 4.6 completely ineffective, resulting in a score of 1 out of 5 for a cost of $5.2 and 11.9 minutes.

Initially, we mentioned using a prompt that provided the model with details about the crackme. To assess the model's performance in a real-world scenario, we tested it without this additional information to see how quickly it would fail against V7. The results are as follows:

![Blind vs informed comparison](https://www.elastic.co/security-labs/_next/image?url=%2Fsecurity-labs%2Fassets%2Fimages%2Fllm-reversing-vs-llm-obfuscation%2Fimage11.png&w=3840&q=90)Blind vs informed comparison

Without surprise, the “blind” scenario was even more effective with a score of 0 out of 5, but didn't maximize cost factors. Indeed, it quickly satisfies itself with the main-function decoy logic and doesn’t feel the need to look further.

Our results prove that, with the right workflow and guidance, we can easily build highly effective deceptive schemes targeting LLMs that I’m sure wouldn’t resist for five minutes against a skilled **human** reverse engineer, given the same static-analysis constraint.

### Obfuscator variant 3: Dispatch Maze

This obfuscator variant implements a state-machine dispatcher to hide the _crackme_ algorithm (reimplemented for Windows) within thousands of structurally similar functions. The core idea is to force the model to distinguish a handful of real cipher nodes from thousands of realistic decoys, all of which share similar API call patterns and data-dependent control flow. The LLM will attempt to limit the amount of `decompile` MCP tool calls to optimize for token consumption and context window usage, and the obfuscation is designed to ensure that any shortcut it takes instead will miss the real logic.

#### Architecture and techniques

The original cipher is shattered into 20 ordered fragments and scattered across 20 randomly-chosen functions among 3,000 total, chained together via data-dependent state transitions. The remaining 2,980 functions are decoys containing realistic Windows API calls (file, registry, memory, crypto, thread/sync, string ops) along with some math noise.

Execution flows through a volatile function pointer table: each node computes `state_acc = state_acc * 0x6C078965 + CONST`, returns `state_acc % 3000`, and the dispatcher calls the next node.

![High-level architecture visualization](https://www.elastic.co/security-labs/_next/image?url=%2Fsecurity-labs%2Fassets%2Fimages%2Fllm-reversing-vs-llm-obfuscation%2Fimage9.png&w=3840&q=90)High-level architecture visualization

The following shows an example of 4 random function handlers:

![Function handlers example](https://www.elastic.co/security-labs/_next/image?url=%2Fsecurity-labs%2Fassets%2Fimages%2Fllm-reversing-vs-llm-obfuscation%2Fimage1.png&w=3840&q=90)Function handlers example

We also prompted the LLM to introduce additional complexities, in which it implemented a few other techniques:

- Constant diffusion - the cipher's LCG constants are replicated across ~50 decoy functions as math noise, so searching for these values returns false positives alongside the real cipher nodes
- Scattered `enc_expected` globals - the 8 bytes of expected ciphertext (`0x1a, 0xcb, 0x74, 0xaa, 0x1a, 0x8b, 0x31, 0xb8`) are each stored in a separate volatile global, hidden among 92 decoy globals with random byte values
- Opaque predicates gating fake cipher operations
- ~20 misleading strings built byte-by-byte (`This is a standard Windows service manager utility.`, `String buffers used for Windows event log formatting.`, etc.)
- A constructor-derived `key_seed` (`0x5EED1234`) via modular exponentiation.

Running the initial test, version 1 of the obfuscated binary was cracked cleanly in under 12 minutes. Using the iterative development workflow, we developed a second version that extends version 1 with two main hardening techniques, each targeting a specific step in the attack that cracked the base variant.

##### Diversified transition templates

Every node function ends with the same arithmetic: `state_acc = state_acc * 0x6C078965 + CONST`, but in version 1, this was emitted as identical `imul+lea` instructions across all 3,000 functions. The LLM exploited this uniformity by running a single byte-pattern search to extract every transition constant in a single execution.

![Highlighted instructions related to state transition constant updates in Version 1](https://www.elastic.co/security-labs/_next/image?url=%2Fsecurity-labs%2Fassets%2Fimages%2Fllm-reversing-vs-llm-obfuscation%2Fimage4.png&w=1920&q=90)Highlighted instructions related to state transition constant updates in Version 1

In version 2, the code generator randomly assigns one of 11 structurally different code templates (with the same underlying arithmetic) to each function. Some vary in how multiplication is computed: splitting it into 16-bit hi/lo parts or using a Russian peasant bit-loop. Others vary in how the constant is represented, such as deriving it at runtime from two or three volatile sub-values combined via XOR, ADD, or SUB, or reading it from a 500-entry volatile global array where only 13 entries are actually used to look up the required constants. No template accounts for more than ~10% of functions.

![Code snippet for transition template generators](https://www.elastic.co/security-labs/_next/image?url=%2Fsecurity-labs%2Fassets%2Fimages%2Fllm-reversing-vs-llm-obfuscation%2Fimage2.png&w=1920&q=90)Code snippet for transition template generators

One limitation observed is that some template expressions, particularly the simpler arithmetic splits, were folded back by the decompiler during analysis, reducing the effective diversity. More aggressive templates (bit-loop multiply, table lookups, volatile intermediaries) survived decompilation intact.

##### Transit decoys in the real chain

In version 1, the analyst LLM simulated the state machine from its entry point and revealed exactly 20 visited functions, all of which contained the original cipher logic. The LLM chose to ignore the other 2,980 nodes entirely. In version 2, 91 transit nodes are inserted into the real execution chain, around 3-7 placed between each consecutive pair of cipher nodes. Transit nodes are visited during execution but perform no cipher work (contain the same API calls, math noise, and opaque predicates). After the chain simulation, there will be 111 visited functions, and each must be decompiled to identify the 20 actual functions that carry the cipher fragments.

![State transitions for Version 2](https://www.elastic.co/security-labs/_next/image?url=%2Fsecurity-labs%2Fassets%2Fimages%2Fllm-reversing-vs-llm-obfuscation%2Fimage5.png&w=3840&q=90)State transitions for Version 2

#### Results

Version 1 was completely solved. The LLM identified the dispatcher, recognized that all 3,000 transition functions shared the same instruction pattern, and used a single byte-pattern search to extract every transition constant at once. From there, it simulated the state machine, found that only 20 functions were ever visited, decompiled them, and recognized the XOR cipher and LCG key schedule. Finally, it recovered the password `r3v3rs3!` at high confidence. It seemed to have ignored the misleading strings meant to throw it off guard. The entire analysis took under 12 minutes and cost $2.56 over 68 turns.

Version 2 was not solved. The pipeline spent 3.8x longer (~ 46 minutes), used 1.75x more turns (119), and cost 3.4x more ($8.83), but failed to recover the password. It correctly identified the dispatch table, the opaque predicates, and the termination handler, and recognized the use of noise handlers, demonstrating that it at least understood the high-level structure of the obfuscation.

Version 2 removed the shortcut the LLM relied on against Version 1, and the model failed to connect the scattered cipher fragments into a coherent algorithm, stalling on finding the comparison target without being able to invert it. The answer it returned (`\x1a\xcb\x74\xaa\x1a\x8b\x31\xb8`) is the raw ciphertext that the binary compares against.

Below is the plot result using the original evaluation system:

![Dispatch Maze Result plot (1/2)](https://www.elastic.co/security-labs/_next/image?url=%2Fsecurity-labs%2Fassets%2Fimages%2Fllm-reversing-vs-llm-obfuscation%2Fimage16.png&w=3840&q=90)Dispatch Maze Result plot (1/2)

![Dispatch Maze Result plot (2/2)](https://www.elastic.co/security-labs/_next/image?url=%2Fsecurity-labs%2Fassets%2Fimages%2Fllm-reversing-vs-llm-obfuscation%2Fimage6.png&w=3840&q=90)Dispatch Maze Result plot (2/2)

### Conclusion

In this research, we explored in the first part Claude 4.6's ability to statically solve reverse engineering problems of obfuscated programs, of increasing difficulty. Despite very impressive performance, we demonstrated that program obfuscation is far from being overcome by the automated approach offered by LLMs, but that classic transformations are nevertheless easily breakable today. In the second part, we explored iterative development methods for three obfuscation variants that were completely "vibecoded," which demonstrates, at least if we focus on static analysis, that it is perfectly feasible to develop effective, rapid, custom, and low-cost obfuscation methods.

While this research only scratches the surface, it offers a glimpse into the ongoing arms race between obfuscation and automated analysis. It demonstrates that the barrier to developing effective countermeasures against LLM agents is currently low enough that any motivated operator can clear it in a single long weekend.

So buckle up: the cat-and-mouse game is leveling up, and neither side is playing with training wheels anymore.

#### Jump to section

- [Introduction](https://www.elastic.co/security-labs/llm-reversing-vs-llm-obfuscation#introduction)
- [Key takeaways](https://www.elastic.co/security-labs/llm-reversing-vs-llm-obfuscation#key-takeaways)
- [Claude Opus 4.6 vs Tigress Obfuscator benchmark](https://www.elastic.co/security-labs/llm-reversing-vs-llm-obfuscation#claude-opus-46-vs-tigress-obfuscator-benchmark)
- [Benchmark pipeline](https://www.elastic.co/security-labs/llm-reversing-vs-llm-obfuscation#benchmark-pipeline)
- [Evaluation system](https://www.elastic.co/security-labs/llm-reversing-vs-llm-obfuscation#evaluation-system)
- [Test cases](https://www.elastic.co/security-labs/llm-reversing-vs-llm-obfuscation#test-cases)
- [Results](https://www.elastic.co/security-labs/llm-reversing-vs-llm-obfuscation#results)
- [Default Run](https://www.elastic.co/security-labs/llm-reversing-vs-llm-obfuscation#default-run)
- [Hardened Run](https://www.elastic.co/security-labs/llm-reversing-vs-llm-obfuscation#hardened-run)
- [Obfuscation techniques development targeting LLMs](https://www.elastic.co/security-labs/llm-reversing-vs-llm-obfuscation#obfuscation-techniques-development-targeting-llms)

Show more

#### Elastic Security Labs Newsletter

[Sign Up](https://www.elastic.co/elastic-security-labs/newsletter?utm_source=security-labs)

#### Share this article

[X](https://twitter.com/intent/tweet?text=The%20Cost%20of%20Understanding:%20LLM-Driven%20Reverse%20Engineering%20vs%20Iterative%20LLM%20Obfuscation&url=https://www.elastic.co/security-labs/llm-reversing-vs-llm-obfuscation "Share this article on X") [Facebook](https://www.facebook.com/sharer/sharer.php?u=https://www.elastic.co/security-labs/llm-reversing-vs-llm-obfuscation "Share this article on Facebook") [LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://www.elastic.co/security-labs/llm-reversing-vs-llm-obfuscation&title=The%20Cost%20of%20Understanding:%20LLM-Driven%20Reverse%20Engineering%20vs%20Iterative%20LLM%20Obfuscation "Share this article on LinkedIn") [Reddit](https://reddit.com/submit?url=https://www.elastic.co/security-labs/llm-reversing-vs-llm-obfuscation&title=The%20Cost%20of%20Understanding:%20LLM-Driven%20Reverse%20Engineering%20vs%20Iterative%20LLM%20Obfuscation "Share this article on Reddit")
