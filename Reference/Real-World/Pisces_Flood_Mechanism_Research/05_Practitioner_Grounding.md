# Practitioner Grounding — Code-Level Flavor

Secondary material. Purpose is vocabulary/authenticity for describing the mechanism precisely, not new
conceptual content — everything load-bearing lives in `01`-`04`. See `00_Extraction_Checklist.md` section
E.

---

## 1. Signal-based producer/consumer synchronization — read

*System Programming in Linux* (Weiss), Ch.11 "Process Creation and Termination." Actually read (reached
via a page-offset miscalculation while aiming for Ch.12's IPC material — see `04` item 4 — but the content
itself is worth keeping).

- Demonstrates a real, concrete synchronization problem: a parent and child process sharing a single file,
  where the child writes data and the parent reads it, and both need to move a shared file offset for
  their own purpose without losing or duplicating data. Solved (in this example, deliberately described as
  *not* the most efficient general solution) using `SIGUSR1`/`SIGUSR2` signals to hand control back and
  forth — the child signals "okay to read," the parent signals back "okay to write again," repeat until
  done.
- Useful as a plain illustration of what "two independent things need to take turns touching shared state,
  and coordinate exactly when" looks like at the simplest possible level, before invoking anything as
  heavyweight as full mutual-exclusion protocols. Could be useful narrative-level vocabulary for describing
  a *simple, almost naive* synchronization scheme in the clinics' own jury-rigged devices — not
  enterprise-grade mutual exclusion, just an ad-hoc signal-passing handshake that was good enough until it
  wasn't.

## 2. Zombie processes — read, potentially useful as a narrative image

Same chapter. A child process that has terminated but hasn't yet been "waited for" by its parent is called
a **zombie** — the kernel can't fully release its resources (PID, exit status, etc.) until the parent
performs a `wait()`. If a parent itself terminates without waiting for its children, those children become
**orphans**, and get adopted by `init`, which does eventually reap them.

Flagging this because the vocabulary itself is suggestive, independent of anything mechanistic: a process
whose termination was never properly "collected," lingering in the system's tables past its natural end,
waiting on a parent that may never come — this is close enough to a ready-made image for something about
the Flood's aftermath (a mind-state that ended but was never formally released back to its own owner,
lingering half-attached to a network that no longer has any use for it) that it's worth keeping in mind
even though it's flavor rather than mechanism.

## 3. `execve()` and process replacement — read, low relevance

Same chapter. Covers how a process can replace its own running program image entirely via `execve()` and
the `exec()` family, while preserving PID and most other identity markers. Read in passing; no clear
narrative hook currently. Kept only for completeness.

## 4. Asynchronous Programming with C++ — TOC only

*Asynchronous_Programming_with_C++...* — TOC read. Ch.4 "Thread Synchronization with Locks" (specifically
"Understanding race conditions" and "Why do we need mutual exclusion?", pp.69-108) not yet actually read.
Low priority — would mostly duplicate `02`'s distributed-systems mutual-exclusion material at a more
code-literal level. Worth a quick pass only if the eventual write-up wants an in-code example of a race
condition specifically, rather than the formal distributed-systems description.

## 5. Hands-On Network Programming with C — deprioritized

TOC read only; not pursued further. Real socket-programming mechanics are a layer below what the
mechanism actually needs (this is "how do two computers open a TCP connection," not "what happens when a
network of devices' shared-state assumptions break") — leaving this deprioritized unless something
specific comes up that needs it.
