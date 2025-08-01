---
title: "
      Asynchrony is not Concurrency
      ◆ Loris Cro's Blog
    "
tags:
   - parallelism
   - Zig programming
   - asynchrony
   - concurrency
   - async I/O
link: https://kristoff.it/blog/asynchrony-is-not-concurrency/
date: 2025-07-20
description: "Loris Cro differentiates between asynchrony, concurrency, and parallelism in programming, proposing precise definitions for each term. He argues that misunderstanding these distinctions has led to inefficiencies in software ecosystems and unnecessary code duplication. In Zig, asynchrony can occur without concurrency, allowing synchronous and asynchronous code to coexist without forcing users into \"async-only\" paradigms. This design choice mitigates deadlocks and enhances the usability of libraries. Cro emphasizes that understanding these concepts can significantly improve software architecture and implementation efficiency, particularly in the context of Zig's async I/O capabilities."
---

_Personal Website_

[About](https://kristoff.it/)
•
[Twitter](https://twitter.com/croloris)
•
[Twitch](https://twitch.tv/kristoff_it)
•
[YouTube](https://youtube.com/c/ZigSHOWTIME/)
•
[GitHub](https://github.com/kristoff-it)

# Asynchrony is not Concurrency

July 18, 2025
•
12
min read • by
**Loris Cro**

Yes I know about that one talk from Rob Pike.

The title of this blog post is not something you hear people say often, if ever. What you do hear people say is “concurrency is not parallelism”, but that’s not as useful, in my opinion.

Let’s see how Wikipedia defines those terms:

> **Concurrency** refers to the ability of a system to execute multiple tasks through simultaneous execution or time-sharing (context switching)

> **Parallel computing** is a type of computation in which many calculations or processes are carried out simultaneously.

What if I told you we’re missing a term to describe another aspect of concurrent programming and, because of it, we’re all collectively missing a key piece of understanding that has shaped our software ecosystems for the worse?

Well, I spoiled it in the title: the missing term is ‘asynchrony’, but why?

## Two files

Say that you have to save two files and order does not matter:

```zig
io.async(saveFileA, .{io});
io.async(saveFileB, .{io});

```

A could be saved before B, or B could be saved before A, and all would be fine. You could also write _some of_ A, then _some of_ B, and then back to A, to finally complete writing B. That also would be correct, and in fact that’s what tends to happen when using evented I/O to save sufficiently complex files concurrently.

But, most importantly, **it’s perfectly legitimate to do all the work to save one file first and, only once that’s done, to begin saving the second file**. Maybe that would not be the most efficient thing to do, but the code would still be correct.

## Two sockets

Let’s take a look now at another example: say that you need to create a TCP server and connect to it _from within the same program_.

```zig
// assume that server.listen has already been called
io.async(Server.accept, .{server, io});
io.async(Client.connect, .{client, io});

```

Like before, the order doesn’t matter: the client could begin a connection before the server starts accepting (the OS will buffer the client request in the meantime), or the server could start accepting first and wait for a bit before seeing an incoming connection.

Unlike before, **it is mandatory that the execution of both tasks overlap**.

In the file example it was fine to do all the work for A first and all the work for B last, but not in this second case, because the server needs to be active **while** the client tries to connect.

## Asynchrony, Concurrency, Parallelism

In common lingo, we would describe both the code snippets presented above as “concurrent” and stop there, but that will lose us some nuance, so here’s my proposed definitions for these terms:

> **Asynchrony**: the possibility for tasks to run out of order and still be correct.
>
> **Concurrency**: the ability of a system to progress multiple tasks at a time, be it via parallelism or task switching.
>
> **Parallelism**: the ability of a system to execute more than one task simultaneously at the physical level.

With these definitions in hand, here’s a better description of the two code snippets from before: both scripts express asynchrony, but the second one **requires** concurrency.

## Why even bother?

Ok, cool, we now can be more precise when describing code snippets, so what did we gain?

For dramatic effect, allow me to answer this question in the negative and tell you what it is that we lost by not being aware enough of the difference between asynchrony and concurrency.

Because of our lack of understanding:

We have created language ecosystems where library authors must duplicate effort (e.g. [redis-py](https://github.com/redis/redis-py) vs [asyncio-redis](https://github.com/jonathanslenders/asyncio-redis)) or [worse](https://nullderef.com/blog/rust-async-sync/).

We have created a [worse](https://bitbashing.io/async-rust.html) [experience](https://charlesleifer.com/blog/asyncio/) for library users where async code is viral and where a even a single dependency with async code demands that users give up their ability to write normal, synchronous code.

And to mitigate all these problems, we have created unholy escape hatches that cause suboptimal behavior at best and [deadlocks](https://www.youtube.com/watch?v=J0mcYVxJEl0) at worst.

Let’s switch back to answering the question in the positive.

## In Zig Asynchrony is not Concurrency

I already wrote a blog post on [Zig’s new async I/O](https://kristoff.it/blog/zig-new-async-io/) story, but I only dedicated a short section at the end on this aspect, which led me to expand on it in this post.

In Zig asynchrony is not concurrency because the usage of `io.async` does not imply concurrency. In other words: code that uses `io.async` can be run in single-threaded blocking mode.

Let’s look again at the file example:

```zig
io.async(saveFileA, .{io});
io.async(saveFileB, .{io});

```

When run in single-threaded blocking mode, the code above will be equivalent to this:

```zig
saveFileA(io);
saveFileB(io);

```

It’s easy to imagine how this can be done, all `io.async` has to do is run the given function immediately (instead of spawning a new thread for it, or doing any other form of task switching).

**This means that a library author can use `io.async` in their code and not force their users to move away from single-threaded blocking I/O.**

Conversely, code that does _not_ use `io.async` can still take advantage of concurrency. But wouldn’t doing that cause deadlocks?

The answer is that this is an ill-posed question. What makes synchronous code behave well in the presence of concurrency are two things (aside from plain multithreading):

1. Usage of evented I/O syscalls (io\_uring, epoll, kequeue, etc.) instead of blocking ones.
2. Usage of task switching primitives to continue doing work while I/O operations are being carried out by the OS.

Neither of these things is something you see at the surface level (so looking at synchronous code tells you usually very little) and especially wrt the second point, `async` is not the task switching primitive, because it only concerns itself with asynchrony, not concurrency (and task switching is – by the definition I gave above – a concept specific to concurrency).

The task switching primitive is usually called `yield`, let’s take a look at how that works in the case of green threads:

Take the synchronous code example again, wrap it in a function for extra clarity and let’s also pass down the names of the two files to write. This last change will become useful in a moment.

```zig
fn saveData(
   io: Io,
   nameA: []const u8,
   nameB: []const u8
) !void {
   try saveFileA(io, nameA);
   try saveFileB(io, nameB);
}

```

When we execute `saveData` we call `saveFileA` which in turn will, at some point, call a function to write bytes to a file. In Zig’s design this is done by using an `io` parameter, but there are plenty of different ways to make this work. What matters is that at some point we get to an implementation of `write` specific to the green threads execution model.

The `write` function will request to perform a write to the file and then, instead of blocking while the operation is carried out, the syscall will return immediately (in the case of io\_uring it’s not even a syscall, it’s just a memory write to a ring buffer).

At this point the write operation has been submitted and our program needs to switch to a different task while this one waits for the operation to complete. In other words, we need to yield.

In the case of green threads, yielding is performed by stack swapping. We save at a location in memory the state of all general purpose registers in the CPU (including program counter and stack pointer), and we load another “snapshot” from memory to the CPU (again, including program counter and stack pointer which now point to machine code in a different part of the executable, and to a different stack in memory).

The snapshot that we’re loading was previously saved using this same technique by the event loop which yielded to resume a task that was reported as ready to resume by a notification from the OS. Now that we’re switching back to the event loop, the same will happen again.

While I described stack swapping with some level of detail, it should be noted that this is more or less the same way in which your OS schedules threads on CPU cores. If you want to see a fully concrete example of stack swapping in action, I’ve [implemented it live on Twitch in a barebones riscv32 kernel](https://github.com/kristoff-it/kristos/).

I won’t get into the weeds of a stackless coroutines implementation, but the core principle is the exact same: designing a yielding primitive that lets you switch tasks. [Here](https://github.com/ziglang/zig/issues/23446) you can see the latest proposal for Zig, where historically the stackless task switching primitive has been implemented by `suspend` and `resume`.

Now that task switching is clear, let’s go back to the event loop. If `saveData` is written in a synchronous manner, what can the event loop do while it waits for evented I/O to complete?

The answer is that it depends on the rest of the program. Concurrency needs to exploit asynchrony and, if there’s none, then no tasks can be in execution at the same time, like in this case for example:

```zig
pub fn main() !void {
   const io = newGreenThreadsIo();
   try saveData(io, "a.txt", "b.txt");
}

```

But the fact that `saveData` doesn’t express asynchrony does not prevent other parts of the program from expressing it:

```zig
pub fn main() !void {
   const io = newGreenThreadsIo();
   io.async(saveData, .{io, "a", "b"});
   io.async(saveData, .{io, "c", "d");
}

```

In this case the two different calls to `saveData` can be scheduled concurrently because they are asynchronous to one another, and the fact that they don’t express any internal asynchrony does not compromise the execution model.

**This allows normal synchronous code and asynchronous code to run concurrently in the same program without any issue.** No need for code duplication of libraries, and no need for users to accept Faustian bargains in order to use an “async library” (note how that terminology is meaningless in light of our new understanding, that is just “a library” now!).

If this result feels surprising to you, it’s probably because you’re used to async being tied to stackless coroutines, which normally causes the usage of `async` and `await` keywords to propagate virally throughout the code. But, as an example, Go doesn’t have this same problem: most code is synchronous and yet Go does run goroutines concurrently (because all I/O is evented and because Go can task switch).

We’re finally ready to look at one final example to complete our understanding!

## Concurrency as a requirement

For convenience, here’s a copy of the definitions I’ve introduced in the beginning:

> **Asynchrony**: the possibility for tasks to run out of order and still be correct.
>
> **Concurrency**: the ability of a system to progress multiple tasks at a time, be it via parallelism or task switching.
>
> **Parallelism**: the ability of a system to execute more than one task simultaneously at the physical level.

Now let’s take a look again at the client-server example:

```zig
// assume that server.listen has already been called
io.async(Server.accept, .{server, io});
io.async(Client.connect, .{client, io});

```

As mentioned earlier, this situation is different than the `saveData` one. Here `Server.accept` and `Client.connect` require concurrency because blocking on `Server.accept` will prevent `Client.connect` from ever executing.

Unfortunately this code doesn’t express this requirement, which is why I called it a programming error when I presented this example in my post about Zig’s new async I/O.

This is how you will solve it in Zig:

```zig
try io.asyncConcurrent(Server.accept, .{server, io});
io.async(Client.connect, .{client, io});

```

`asyncConcurrent` guarantees that `Server.accept` will run concurrently with the rest of the code. This documents in the code that concurrency is required for correctness, which will also let the program error out when attempting to run it over a non-concurrent `Io` implementation. But that’s not all!

Did you notice that `io.async` does not need to be `try` ed?

Let’s imagine that we’re running our program over an implementation of `Io` that spawns a new OS thread for each async task. If it can’t error out, what happens when there are too many threads active at the same time? Does it just crash?

No, it runs the function directly!

This is a snippet from the current `Io` implementation that uses green threads, where a similar concept applies: each green thread (called `Fiber` in the implementation) needs to be allocated in memory and, if that fails, the function is simply run immediately:

```zig
const fiber = Fiber.allocate(event_loop) catch {
    // The next line runs the function
    // passed as an argument to io.async
    start(context.ptr, result.ptr);
    return null;
};

```

Just to drive the point home one last time: this is a legitimate thing to do because asynchrony does not imply concurrency. `io.asyncConcurrent` does guarantee concurrency instead, and that’s why it has to be a failable function.

Before we jump to the last section about conclusions, I’d like to point out that the code snippets above are all realistic but, to remove clutter, I have omitted error handling and the code that awaits futures returned from async calls. Read [my other blog post](https://kristoff.it/blog/zig-new-async-io/) to see complete code snippets, although that is not necessary to understand this post.

## Conclusions

First and foremost, I hope to have convinced you that asynchrony is not concurrency.

Secondly, _I_ hope to have given _you_ hope that we can climb out of the current async/await local minima that afflicts most implementations, that code doesn’t have to be duplicated, and that both asynchronous and synchronous code can co-exist in the same codebase **without any compromise**.

Lastly, I hope to have given you an intuition for how async I/O is going to work in Zig.

If you want to have a sneak peek of the upcoming Zig async I/O redesign, **Monday 21st of July 2025 at 7pm CEST I will be [live on Twitch](https://twitch.tv/kristoff_it) ( [more timezones and info here](https://zig.show/episodes/42/)) with Andrew to read the thread pool implementation, the green threads implementation, and to write myself a non-concurrent implementation of `Io`** in order to test live if everything that I talked about in this post is actually true.

Spoilers: I already tried and it all works. Welcome to the `Future` we’ve been all awaiting.

* * *

[←\\
Zig's New Async I/O](https://kristoff.it/blog/zig-new-async-io/)  or  [Back to the Homepage](https://kristoff.it/)
