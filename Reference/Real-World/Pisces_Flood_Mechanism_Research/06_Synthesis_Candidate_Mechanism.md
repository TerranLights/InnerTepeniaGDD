# Candidate Mechanism — Synthesis (Working Draft, Not Canon)

**This is research synthesis, not a decision.** Per `10b_Pisces_Flood_Mechanism.md`'s own closing note,
the actual mechanism gets chosen by the developer directly, not pre-committed here. This file exists so
the strongest candidate found so far survives a context reset in a form that can be picked up, argued
with, revised, or discarded on sight — not so it can be copied into the game file as-is.

**This file is the maximalist blend — everything `01`-`05` found, layered together.** It is not the only
option. See `07_Candidate_Mechanism_Variants.md` for that same material pulled apart into several
independently viable, fully-formed alternatives, since some of what's blended together below are genuine
alternatives to each other rather than layers that have to stack — deliberately kept open rather than
converged, since the best fit may depend on how the rest of Concordia's districts develop.

Status: first pass, based on `01`-`05` as currently extracted. Should be revisited once the still-unread
high-priority items (Networks of Networks Ch.5, Linux Memory Manager Ch.3/4, Embedded Linux Security
Handbook Ch.8) are actually pulled — see `00_Extraction_Checklist.md`.

---

## The candidate, stated plainly

Pisces' underground clinics route unregulated, Aquarius-originated neural-interface hardware that failed
ethical review elsewhere (already established canon). That hardware doesn't just talk to its individual
wearer — because it's black-market and never engineered for robustness, it's jury-rigged onto some shared
backend infrastructure (a relay network, a shared calibration service, whatever already-established
Aquarius-tier tech the clinics are piggybacking on rather than building from scratch). That backend
dependency is a real, specific structural weakness: an **interdependent network**, in the technical sense
from `01` — one network of devices whose individual function depends on a *different* network's nodes
staying up, linked by dependency links rather than ordinary connectivity links.

Interdependent networks, unlike single isolated ones, can collapse **abruptly** rather than gradually
(first-order vs. second-order percolation transition) — an ordinary, small, unremarkable failure (one
overloaded relay node, one bad firmware push, one clinic's patched-together backend having a bad night)
can cascade back and forth between the device network and its backend, with no attacker and no
proportionality between trigger and outcome. That's the Flood: not a plague, not a curse, not sabotage —
a cascading failure in a topology nobody ever engineered to fail safely, because nobody officially
engineered it at all.

**Update, spatial-embedding finding now in hand:** the clinics' device network isn't an abstract random
graph — it's physically distributed, worn and carried by specific people in specific physical locations
across the district, which makes it a *spatially embedded* network in the technical sense. That matters
enormously: for spatially embedded interdependent networks, the critical dependency threshold **q_c = 0**
— meaning *any* nonzero coupling to a shared backend, however weak, makes eventual collapse abrupt rather
than continuous, with no "safe" regime of light coupling the way a non-spatial (e.g., a purely random or
cloud-based) network would have. This isn't a risk the clinics' engineers could have minimized by keeping
the shared-backend dependency light — for a real, physically-distributed device mesh, there is no
"light enough to be safe." See `01` section 5 for the full derivation and the real math behind it
(traces to 2D-lattice percolation's own critical exponent).

What made it specifically a *memory-sharing* catastrophe rather than an ordinary blackout: the same
literature describes a real end-state for these cascades called the **mutual giant connected component**
— surviving nodes that end up jointly, mutually bound into each other's continued function in a way they
weren't before the cascade — and a related dynamical phenomenon called **explosive synchronization**,
where antagonistic/competitive dependency coupling causes an entire interdependent system to abruptly snap
into sharing one state. Applied to neural-interface hardware specifically, "nodes forced into a shared
state" is not a metaphor — it's what actually happened to the people wearing that hardware when their
individual private mind-state was the thing riding on those now-collapsing device dependency links.

**Update, memory-isolation mechanics now in hand (`03` section 2):** real OS memory management gives an
exact, literal (not metaphorical) description of what "someone's private memory stopped staying private"
means at the engineering level. Process isolation isn't a passive default — it's an *actively maintained*
hierarchy of page tables, checked on every single memory access via permission flags, that keeps one
process's physical memory from being readable through another's virtual addresses. If Pisces' clinic
hardware runs some embedded analog of this (one address-space "process" per connected mind), the
cascading backend failure from section 1 corrupting that specific bookkeeping — rather than simply
dropping a connection — is precisely what would turn "the backend crashed" into "I can't tell which
memories are mine." Concretely: two sessions' page tables end up pointing at the same physical memory
without either intending to share it, or the permission-check layer stops being enforced for a given
mapping, or a firmware fault corrupts the top-level pointer for one session's whole address space. None of
these require new technology — they're realistic failure modes of memory-management systems that already
exist, which is exactly the discipline constraint A5 (no new tech tier) needs.

**Update, a real "why memory specifically, why now" mechanism now in hand (`03` section 3a):** real
memory science establishes that human memories are not stable archives — every act of recall briefly
*destabilizes* a memory (makes it "labile") before it "reconsolidates" back to a stable state. This means
the single most vulnerable moment in any memory's existence is the ordinary, everyday act of recalling it,
not some rare or exotic state. If the clinics' legitimate pre-catastrophe service was something like
assisted memory recall or consensual memory-sharing (a natural fit for Pisces' established
dissolution/escape-tech character), the technology's *normal, everyday operation* already meant touching
people's memories at exactly this real, already-fragile reconsolidation window — no new capability
required, just an ordinary technology meeting an ordinary (if little-known outside neuroscience) window of
vulnerability at the worst possible moment, right as the cascading network failure corrupted the isolation
layer around it. The same material also gives a precise citation for what's actually being violated:
"memories are intrinsically cognitive and personal... we cannot access each other's memories directly" —
normally shared only as lossy, narrated *abstraction* (a conversation, a story), never directly. The
Flood's real violation is skipping that abstraction layer entirely, not merely "sharing too much."

**Update, the single most precise mechanism found in this whole pass (`03` section 3, Ch.4):** real Linux
kernel data structures include a literal, explicit **`owner` field** on every process's address space —
"ownership" of memory is not an intrinsic property of the data itself, it's separate, actively-managed
bookkeeping, normally reassigned only in narrow circumstances (a process exiting), but structurally
*nothing stops it being reassigned incorrectly*. If the cascading failure corrupted whatever handles
ordinary session teardown on the clinics' hardware, memory legitimately belonging to one person's session
could have its ownership silently reassigned to another person's session, with the underlying data never
moving at all — an exact, non-metaphorical description of "whose memories are these" that doesn't even
require the memory itself to be touched, only the bookkeeping around it. Separately, real precedent
(Page Table Isolation / the Meltdown vulnerability) shows that memory isolation can fail *without any
corruption whatsoever* — a real, documented hardware side-channel let data leak across a boundary whose
stated permissions were never actually violated. Applied to unregulated, cost-cut clinic hardware unlikely
to have every mitigation a legitimate device would ship with, this offers an even less dramatic failure
mode than "something broke": the isolation could have been checked correctly at every step and still not
been enough.

## Checked against `10b`'s "what must be true" list

1. **Confining variable is tech/spatial exposure, not identity.** ✅ The mechanism runs entirely on
   which specific device network you were plugged into. Zero identity content anywhere in it.
2. **Traces to the underground clinics' unregulated neural-interface tech.** ✅✅ Strengthened further by
   the spatial-embedding finding: it's specifically because the clinics' device network is a real,
   physically-distributed mesh (not a clean centralized service) that q_c = 0 applies at all — a properly
   regulated, centralized/non-spatial Aquarius backend plausibly wouldn't have this specific structural
   vulnerability, making "unregulated and physically improvised" load-bearing to the mechanism, not
   incidental to it.
3. **Confined to Pisces despite real porousness (tunnels, Aquarius lineage, Gemini leakage).** ✅ The
   cascade propagates through *dependency links in a specific device network*, not through ambient
   geography. Someone physically in the Virgo tunnels who isn't plugged into Pisces' own clinic device
   network has no dependency link into the cascade at all — a structural, not coincidental, reason it
   didn't leak through the tunnels.
4. **Digital/networked specifically, gesturing at the individual/collective boundary before anyone had
   language for it.** ✅✅ Best-fitting single point of contact with real science found in this entire
   research pass — "mutual giant connected component" and "explosive synchronization" are literal
   technical terms for individual nodes being forced into a shared state, not a metaphor reaching for one.
   Strengthened further by `01` section 7: real neuroscience already, independently describes **the human
   brain itself as a network of networks** (interconnected regional modules, structural/functional
   multiplex layers, a bidirectionally-coupled vascular network). The device-network mechanism and the
   human minds it reaches don't need a separate invented bridge between them — the same real mathematical
   framework already, legitimately covers both.
   Bonus, from `03` section 3a: real cognitive science's **"pattern development"** mode — what a mind does
   when no existing interpretive pattern fits, requiring a genuinely new framework built from scratch —
   gives a principled reason survivors would eventually construct something as significant as the
   Syncretic Religion's own doctrine, rather than assimilating the Flood into any pre-existing category.
5. **Individual-level variance (transcendence vs. trauma) falls out of the mechanism itself.** ✅✅
   Now the best-supported point in the whole synthesis, three independent layers deep:
   - *Structural, sharpest version* (from `01` section 6): real numerical simulations of interdependent
     networks show that near the critical threshold, **literally identical starting parameters produce
     two categorically different outcomes on different runs** — full stable survival or complete
     fragmentation, a genuine documented two-class split rather than a spectrum, with no way to predict in
     advance which a given realization lands in. Two people connected to functionally the same part of
     the network could have ended up on opposite sides of that split for no reason traceable to anything
     different about them — this is real, cited network science, not an inference stretched to fit.
   - *Structural, general version* (from `01` section 4): people whose mind-state landed in a stable
     **mutual giant connected component** (the cascade died out, settling into a new steady state)
     experienced integration/expansion; people caught in a cascade that *never stabilized* got the
     disorientation of a boundary that kept dissolving without ever settling.
   - *Psychological* (from `03` section 3, Pattern Theory): real cognitive-science precedent that
     genuinely ambiguous experience gets resolved into one of a small number of incompatible readings,
     that minds *anchor* on one reading and rarely hold both, and that assigning profound meaning to
     anomalous input (apophenia/"patternicity") is a documented, non-pathological, arguably
     evolutionarily-favored cognitive tendency — not an error to be explained away. This is exactly the
     shape constraint A5 asks for: built into how any mind processes ambiguous input, not bolted onto the
     Flood specifically.
6. **Self-selecting population (sought the tech out), not census residency.** ✅ Already locked canon,
   orthogonal to the mechanism — no conflict. Only people plugged into the clinic device network in the
   first place have any dependency link into the cascade, which is exactly the self-selecting population
   already established. Bonus, from `01` section 6: real **"multiple support"** network robustness gives a
   technical (not narratively convenient) reason not even every connected device/person was equally
   exposed — sessions with redundant backend connections had genuine, mathematical protection that
   single-point-dependent sessions didn't.
7. **Genuine ambiguity survives.** ✅ Nothing here forecloses the spiritual interpretation in-world — the
   materialist mechanism is what *we* (developer/design) know; the in-world Pisces population, lacking
   this framework, would have no way to distinguish "we got structurally merged by a backend failure" from
   "something larger happened to us," and wouldn't need to for the ambiguity to be real to them.

## Checked against `10b`'s "what definitely cannot be true" list

1-2. **No national/ethnic/genetic explanation.** ✅ Never enters the mechanism anywhere.
3. **No pure ambient/environmental cause.** ✅ This is infrastructure-based (a specific device network's
   dependency topology), not air/water/geology — and it *is* tied to Pisces-built infrastructure
   specifically, satisfying the exception clause.
4. **No external attack or deliberate bioweapon.** ✅ Cascading failure in an interdependent network is,
   by the real literature's own framing, the textbook case of a catastrophic failure that needs no
   attacker — the 2003 Italian blackout (the field's own canonical example) had none.
5. **No new technology tier.** ✅ Runs entirely on already-established Aquarius-tier neural-interface
   hardware. The story is about the *network topology* the clinics built around existing tech, not any new
   device capability.
6. **No literal borderless 100%-of-residents effect.** ✅ Satisfied jointly by constraint-6-above (only
   plugged-in, self-selected people have dependency links into the cascade) and by the tunnel-porousness
   answer in constraint-3-above.
7. **No fully solved, undisputed public cause.** ✅ Nothing requires in-world consensus on what happened —
   see constraint-7-above.
8. **Doesn't reopen existence-vs-mechanism.** ✅ Pure research; this file makes no claim on the game files
   themselves.

**Update, why devices would converge on shared state at all, and a genuinely new nuance (`02` section 4):**
real distributed-robotics research gives named, simple, mathematically-proven algorithms (the AVERAGING
law, the CIRCUMCENTER law) for exactly this — independent agents converging on a shared state through
purely local rules, no global coordinator required. A real device network running something like this for
entirely mundane reasons (calibration averaging, session-state synchronization) wouldn't need any sinister
intent behind it. More valuably: the same source demonstrates that this kind of convergence doesn't have
to be universal — depending on network topology, it can produce **multiple separate clusters that never
merge with each other**, rather than one single shared endpoint. This gives real mathematical grounding
for imagining the Flood's aftermath as clustered/factional (different small groups merged with each other,
not the whole district into one undifferentiated mind), which in turn gives natural shape to how different
survivor groups could have arrived at different variants of Syncretic doctrine. The same source also ties
this directly to real *opinion dynamics* research (the Krause model, "bounded confidence") — the same math
used here for physical rendezvous is, in the social sciences, used to model belief/opinion convergence
among people, linking this session's structural material and the psychological material under one shared
real framework rather than two separate metaphors.

**Bonus, bridging to the Syncretic Religion specifically (`03` section 4):** real academic material on
"shared pattern thinking" gives a grounded account of how individually-varied Flood experiences could
congeal into a shared doctrine that outlives and exceeds any single survivor's account, complete with
real vocabulary for internal orthodoxy/heresy variation — and, usefully, a legitimate *darker* reading
(coercive imposition of a shared interpretation on people who didn't really choose it) that serves the
project's "no good endings" discipline without requiring anything invented.

**Update, why the Flood happened *when* it did (`01` section 7):** real network-of-networks theory proves
that a sufficiently large interdependent system can collapse *completely* with **zero external failures at
all**, purely from its own accumulated structural interdependency crossing a threshold — given only the
ordinary, common precondition that at least one network in the system has any isolated or singly-connected
nodes (a mundane property, not a defect). Applied to Pisces: the clinics' device network could have been
growing for years through entirely unremarkable expansion — more devices, more coupled backend services,
more overlapping support relationships, nothing anyone would have flagged — and this result says there is
a genuine point at which that accumulated growth alone guarantees eventual total collapse. The Flood
becomes something that was quietly already inevitable once the district's own unregulated device ecosystem
crossed a threshold nobody was tracking, rather than requiring any single traceable incident, bad actor,
or design flaw as its proximate cause — a different and arguably more unsettling shape than "an accident
happened," and one that still requires no external attacker (constraint A4) and no new technology tier
(constraint A5).

## Status: every constraint now has real supporting material

As of this update, every item in both of `10b`'s constraint lists (7 "must be true," 8 "cannot be true")
has at least one real, specific, non-hand-waved source behind it — see the point-by-point walkthrough
above. Three genuinely independent research threads converged cleanly:

1. **The core structural mechanism** (`01`) — cascading failure in a spatially-embedded interdependent
   network, with the q_c = 0 finding explaining why an ordinary, small clinic-network fault was
   structurally guaranteed to be catastrophic rather than contained.
2. **What "shared memory" means mechanically** (`03` section 2) — real OS-level page-table isolation,
   giving a literal (not metaphorical) description of what broke.
3. **Why unregulated hardware specifically, and why nobody saw it coming** (`04` section 3) — real
   firmware-security precedent (LogoFAIL, the documented blind spot in standard detection tooling).
4. **Why the same event split into transcendence and trauma** (`03` section 3) — real cognitive-science
   precedent for ambiguous experience resolving into anchored, mutually exclusive readings.

**This is a first-pass synthesis, not a final answer.** It hasn't been reviewed by the developer yet, and
per `10b`'s own instruction, the actual decision is a conversation to have directly, not something this
research folder should treat as settled on its own authority. Remaining unread material (Ch.4-5's
"Patterns and Memories"/"Shared Pattern Thinking" sections, the Distributed Control of Robotic Networks
rendezvous material, Ch.4 of the Memory Manager book) would sharpen details but isn't needed to bring a
complete candidate to that conversation.
