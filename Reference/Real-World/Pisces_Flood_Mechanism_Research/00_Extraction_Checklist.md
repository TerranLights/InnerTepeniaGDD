# Pisces Flood Mechanism — Research Extraction Checklist

**Purpose:** working extraction log for real-world scientific/technical source material that could
plausibly ground *The Flood* (Pisces district, Concordia) in something more precise than hand-waving.
Governing constraint document: `Worldspace/Locations-and-Levels/Concordia-City/Districts/Deep_Dives/
10b_Pisces_Flood_Mechanism.md` (the "what must be true" / "what cannot be true" lists — every candidate
below is being checked against those, not against general plausibility). Source PDFs live in
`Reference/Materials/books/` (subfolders: `Math_and_Computation/`, `Linux/`, `Cpp/`, `religion/`,
`Language/` — the last two are for unrelated research threads, not this one).

**This is research only — nothing here is canon and nothing here should be copied into
`10b_Pisces_Flood_Mechanism.md` or any other game file until the developer signs off on a specific
mechanism.** That file's own text is explicit that the actual decision gets worked through directly,
not pre-committed in a reference doc.

**Resumability note:** this file is the source of truth for what's done. If a session gets cut off
mid-extraction, start here — check the box status, open the linked output file, and continue from the
first unchecked item. Page ranges given are PDF-index ranges (not printed page numbers — most of these
books have 10-20 pages of front matter before "page 1," so PDF page N ≠ printed page N; ranges below
were already corrected for that where discovered).

**Status legend:** `[x]` extracted and written into its output file · `[ ]` not yet done · `[~]` partially
done / TOC-only, needs a real content pass.

---

## Output files in this folder

| File | Contents |
|---|---|
| `01_Network_Cascading_Failure.md` | The core mechanism candidate: percolation, epidemic spreading, interdependent-network cascading failure, first/second-order transitions, mutual giant component, explosive synchronization |
| `02_Distributed_Systems_Concepts.md` | Logical/vector clocks, mutual exclusion, distributed snapshots, consensus/rendezvous — grounding for *why* and *how* many devices would try to agree on shared state |
| `03_Memory_and_Identity_Isolation.md` | Process/address-space isolation (real OS memory management), collective vs. individual memory, cognitive-science angle for the transcendence/trauma split |
| `04_Embedded_Firmware_and_Security.md` | Firmware/embedded-device failure modes, trust anchors, why unregulated clinic hardware specifically would be fragile |
| `05_Practitioner_Grounding.md` | Code-level flavor: race conditions, mutual exclusion in practice, sockets — for authenticity/vocabulary, not new mechanism content |
| `06_Synthesis_Candidate_Mechanism.md` | The maximalist blend — every finding from `01`-`05` layered into one candidate, checked point-by-point against `10b`'s constraint list |
| `07_Candidate_Mechanism_Variants.md` | The same material pulled apart into 3 decision axes and 4 independently viable candidates, deliberately not converged — see this file before locking in `06` as "the" answer |

---

## Extraction checklist by source

### A. Core mechanism — network science / cascading failure (→ `01`)

- [x] `Math_and_Computation/Introduction to the Theory of Complex Systems.pdf` (Thurner/Hanel/Klimek) —
      TOC, pp.1-12
- [x] same — percolation theory, pp.110-125
- [x] same — self-organized criticality, pp.110-125 (same pass)
- [x] same — epidemic spreading on networks / scale-free epidemic threshold, pp.207-221
- [x] `Math_and_Computation/Introduction to Network of Networks.pdf` (Gao/Bashan/Shekhtman/Havlin) — TOC
      + Ch.1 (single-network percolation basics), pp.1-30
- [x] same — Ch.2 "From single networks to networks of networks" — dependency vs. connectivity links,
      cascading failures (2003 Italy blackout case), first-order vs. second-order percolation transition,
      **mutual giant connected component**, **explosive synchronization**, antagonistic/competitive
      coupling, pp.31-45
- [x] same — **Ch.3 §3.2-3.3 DONE** — confirmed PDF pp.49-65 ≈ book pp.3-2 to 3-18. Feedback vs.
      no-feedback dependency (real distinction, feedback = more dangerous, loops amplify failure);
      **multiple support** (real robustness mechanism — nodes with redundant support connections survive
      single-point failures that would kill a non-redundant node, giving a real technical reason some
      devices/people would have been spared without narrative favoritism); interconnected networks
      revisited with a concrete example (Fig 3.11) of link-type determining protective vs. catastrophic
      outcome. **Sharpest finding: real numerical simulations show outcomes bifurcate unpredictably near
      the critical threshold** — identical starting parameters produce either full stable survival or
      complete fragmentation on different runs, a genuine documented two-class split, not a spectrum. This
      is now the sharpest structural grounding found for the transcendence/trauma split. Full writeup in
      `01` section 6.
- [x] same — **Ch.5 §5.1-5.2, "Spatially embedded interdependent networks" / "The extreme vulnerability of
      semi-spatial interdependent networks"** — DONE, this is now the strongest single finding in the
      whole research pass. Confirmed: spatially-embedded interdependent networks have critical threshold
      **q_c = 0** (any nonzero coupling, however weak, makes collapse abrupt rather than continuous —
      traces to 2D-lattice percolation's own critical exponent β = 5/36 < 1). Full writeup in `01`
      section 5. (Actual PDF range: pp.120-135, covering in-book pp.4-40 to 5-9.)
- [ ] same — Ch.5 §5.3 onward (generalizing to *many* spatially-embedded networks, fully-spatial
      propagation, localized attacks) — lower priority now, core finding already captured
- [x] same — **Ch.4 §4.1-4.3.2 DONE** — confirmed PDF pp.81-97 ≈ book pp.4-1 to 4-17. Two exceptional
      findings: (1) real neuroscience explicitly describes the human brain itself as a "network of
      networks" (interconnected regions, structural/functional multiplex layers, a bidirectionally-coupled
      vascular network) — the exact framework grounding the device-level mechanism is independently
      established science for brain structure itself, no invented bridge needed between "computer network"
      and "human mind." (2) A real proven result that a sufficiently large network-of-networks collapses
      *completely* even with zero external failures, purely from its own accumulated structural
      interdependency past a threshold — given the ordinary, common precondition that at least one network
      has any isolated/singly-connected nodes at all. Gives a clean "why now, not earlier" answer: organic,
      unremarkable growth of the clinics' device ecosystem could make collapse structurally inevitable with
      no single traceable trigger. Full writeup in `01` section 7 — likely the best single read of the
      whole research pass.
- [ ] same — Ch.6 "Further features" — synchronization/dynamics on NON, skim for anything beyond what
      Ch.2's "explosive synchronization" mention already gave us (lower priority)
- [ ] `Math_and_Computation/Chaotic systems _ theory and applications.pdf` — TOC + intro only; secondary
      framing (sensitive dependence on initial conditions) as an alternate/supporting vocabulary for
      "small trigger, huge effect," not a replacement for the cascading-failure mechanism
- [ ] `Math_and_Computation/Nonlinearity,_Chaos,_and_Complexity_...pdf` — skim TOC only, likely redundant
      with the above; deprioritize unless the Chaotic Systems book turns out thin

### B. Distributed systems / consensus (→ `02`)

- [x] `Linux/Distributed_Systems_An_Algorithmic_Approach,_Second_Edition_2014.pdf` (Ghosh) — TOC only,
      confirmed chapter structure: Ch.6 "Time in a Distributed System" (logical/vector clocks), Ch.7
      "Mutual Exclusion," Ch.8 "Distributed Snapshot" (Chandy-Lamport), Ch.9 "Global State Collection"
- [ ] same — actually read Ch.6 (logical/vector clocks — causal ordering of events across independent
      devices with no shared clock, directly relevant to "how would separate clinic devices even agree
      on whose memory-state came first")
- [ ] same — actually read Ch.7 (mutual exclusion — the formal guarantee that's supposed to prevent two
      processes from touching shared state at once; useful for "what specifically failed")
- [ ] same — actually read Ch.8 (Chandy-Lamport distributed snapshots — capturing a consistent global
      state across independent nodes; could ground "the system took a snapshot that was already
      inconsistent, and nobody could tell")
- [x] `Math_and_Computation/Distributed Control of Robotic Networks_ A Mathematical.pdf` (Bullo/Cortés/
      Martínez) — TOC only
- [x] same — **§4.2-4.3 "Connectivity maintenance and rendezvous" DONE** — no front-matter offset needed,
      this book's PDF pages match its printed pages exactly. Real named algorithms (AVERAGING law,
      CIRCUMCENTER law) for independent agents converging on shared state via purely local rules. Genuinely
      valuable finding: convergence doesn't have to be universal — the same process can produce multiple
      separate clusters that never merge with each other, giving real grounding for a clustered/factional
      Flood aftermath rather than one monolithic merged consciousness. Also: the AVERAGING law is
      explicitly tied in-text to real "opinion dynamics under bounded confidence" (the Krause model),
      linking this structural material to `03`'s psychological/interpretive material under one shared
      real mathematical framework. Full writeup in `02` section 4.
- [ ] `Math_and_Computation/Attack-and-Defense Games for Control Systems _ Analysis and.pdf` — TOC + Ch.1
      read; still need Ch.4 specifically (FDIA — false data injection attack — detection). Use case:
      repurposed as an *accidental* failure mode (corrupted device output misread as legitimate
      synchronized data), not a deliberate attack, per constraint A4 in `10b`.

### C. Memory / identity isolation, cognitive layer (→ `03`)

- [x] `Linux/The Linux Memory Manager.pdf` (Stoakes) — **Ch.3 "Virtual Memory" DONE** — turned out to be
      the single best technical grounding in the whole research pass. Confirmed offset: book page 123 =
      PDF page 138 (front matter is 15pp). Page tables (PGD→P4D→PUD→PMD→PTE hierarchy), per-entry
      permission flags (`_PAGE_USER`, `_PAGE_RW`, `_PAGE_NX`, etc.), page faults — gives a literal,
      non-metaphorical engineering description of memory isolation as an *actively maintained* structure
      rather than a passive default, and several concrete real bug-classes that would break it. Full
      writeup in `03` section 2.
- [x] same — **Ch.4 "Process Memory" DONE** — confirmed offset holds (book p.209 = PDF p.224, consistent
      with Ch.3's 15pp front matter). Contains the single most precise mechanism found in the whole
      research pass: `struct mm_struct` has a literal, explicit, *reassignable* `owner` field determining
      which process a given address space belongs to — not an intrinsic property of the memory, separate
      bookkeeping that can be cleared/reassigned. Also: real two-stage reference-count teardown
      (`mm_users`/`mm_count`), and Page Table Isolation/Meltdown as real precedent for isolation failing
      *without any corruption at all*, via a hardware side-channel outside the permission-flag system
      entirely. Full writeup in `03` section 3.
- [x] `Math_and_Computation/Superminds _ the surprising power of people and computers.pdf` (Malone) — TOC
      + Ch.15 "Smarter Remembering," pp.223-242 — collective memory's three functions (encode/store/
      retrieve), and the finding that *communication* is specifically what distinguishes collective from
      merely-individual memory
- [x] `Math_and_Computation/Pattern_Theory_Memory,_Interpretation,_Understanding,_Meaning.pdf` — Ch.1
      intro DONE, and it's the best-fitting source found for constraint A5 (individual variance). Bistable
      images (minds anchor on one of two legitimate readings, rarely hold both), pareidolia/apophenia
      (assigning profound meaning to ambiguous/anomalous input as a real, named cognitive category, not a
      flaw), "patternicity" (humans plausibly evolutionarily biased toward over-reading meaning into
      ambiguous stimuli). Full writeup in `03` section 3.
- [x] same — **Ch.4 §"Patterns and Memories" DONE** — turned out to be the best single passage in the
      whole research pass, adding a genuinely new angle rather than just supporting an existing one. Two
      major finds: (1) real citation establishing memory is normally only ever shared as lossy narrated
      *abstraction*, never directly — precisely stating what the Flood violates; (2) real memory
      **reconsolidation** neuroscience — memories destabilize and become editable every time they're
      recalled, before "reconsolidating" back to stable. Gives a real, non-invented reason clinic tech
      interfacing with memory would hit its most vulnerable moment as a matter of course, not require any
      new capability. Full writeup in `03` section 3a — this may be the strongest single addition to the
      synthesis after the original three high-priority reads.
- [ ] same — Ch.5 §"Shared Pattern Thinking" (p.82) — not yet pulled; lower priority now
- [ ] `Math_and_Computation/The forgetting machine _ memory, perception.pdf` — not yet opened; same
      purpose as above
- [ ] `Math_and_Computation/Cognitive Systems Engineering_ The Future for a Changing.pdf` — not yet
      opened; possible source for "how do engineered systems' human operators interpret/misinterpret a
      failure state" — could ground the interpretive split at the human-factors level rather than the
      pure-network level
- [ ] `Math_and_Computation/Computational Models of Cognitive Processes.pdf` — low priority, skim TOC
      only if the above two don't pan out

### D. Embedded / firmware layer (→ `04`)

- [~] `Linux/The Embedded Linux Security Handbook_ Fortify your embedded.pdf` — TOC read; also
      accidentally read Ch.6 "Disk Encryption" (LUKS) and start of Ch.7 "The Trusted Platform Module" due
      to a page-offset miscalculation. That TPM material is still usable (TPM = hardware "trust anchor"
      for a device, firmware/discrete/integrated variants) but is **not** the chapter we actually need.
- [x] same — **Ch.8 "Boot, BIOS, and Firmware Security" DONE** — confirmed offset: book page 102 = PDF
      page 125 (front matter 23pp). Real material on Secure Boot as a chain-of-trust mechanism (and how
      genuinely difficult proper key setup is even for legitimate developers right now), plus the
      LogoFAIL precedent (malicious code riding in through a cosmetic, security-irrelevant-seeming
      feature) and the fact that firmware-level compromise is a documented blind spot for standard
      security tooling ("virus scanners... look at dissected files, not firmware"). Full writeup in `04`
      section 3 — this is now solid support for "why unregulated hardware, why nobody saw it coming."
- [ ] `Linux/System Programming in Linux.pdf` (Weiss) — TOC read; accidentally read Ch.11 "Process
      Creation and Termination" (signals-based producer/consumer sync, execve, wait/zombie processes)
      instead of the intended chapter. Keep that material (see `05`) but still need:
- [ ] same — Ch.12 "Introduction to Interprocess Communication," pp.597-644 in-book pagination — real
      shared-memory IPC mechanics, the actual technical machinery for "two separate processes reading/
      writing the same memory region on purpose" before anything goes wrong with it

### E. Practitioner grounding — secondary, code-level flavor only (→ `05`)

- [x] `Cpp/Asynchronous_Programming_with_C++_Build_blazing_fast_Javier_Reguera.pdf` — TOC only
- [ ] same — Ch.4 "Thread Synchronization with Locks," "Understanding race conditions" + "Why do we need
      mutual exclusion?" sections, pp.69-108 — low priority, mostly for vocabulary/authenticity
- [x] `Cpp/Hands-On Network Programming with C.pdf` — TOC only, not pursued further (deprioritized —
      socket-level networking code is a layer below what the mechanism needs)
- [x] `Linux/System Programming in Linux.pdf` — Ch.11 material already captured (see above), covered here
      for the "zombie process" and signal-based synchronization concepts specifically

### F. Synthesis (→ `06`)

- [x] First-pass candidate mechanism drafted conversationally and checked against all 15 `10b` constraint
      items — needs to be formally written into `06_Synthesis_Candidate_Mechanism.md` (not yet done as
      of this checklist's creation)
- [ ] Revisit synthesis once C. (memory isolation) and the two flagged high-priority items in A/D are
      actually read — the transcendence/trauma split and the "why unregulated hardware specifically"
      angle are both currently thinner than the core cascading-failure mechanism

---

## Suggested next-session order (highest leverage first)

**Milestone reached 2026-07-18: every constraint in `10b` now has real supporting material — see `06`'s
"Status" section. The candidate mechanism is complete enough to bring to the developer for an actual
decision.** Everything below is now optional depth/polish, not required to close a gap.

1. ~~`01` — Networks of Networks Ch.5 (q_c=0 spatial vulnerability)~~ **DONE**
2. ~~`03` — Linux Memory Manager Ch.3 (address-space isolation mechanics)~~ **DONE**
3. ~~`04` — Embedded Linux Security Handbook Ch.8 (firmware threats)~~ **DONE**
4. ~~`03` — Pattern Theory Ch.1 (transcendence/trauma interpretive split)~~ **DONE**
5. ~~Pattern Theory Ch.4 §"Patterns and Memories"~~ **DONE** — real memory-reconsolidation science, the
   best single passage in the whole pass.
6. ~~Linux Memory Manager Ch.4 (Process Memory)~~ **DONE** — the `owner` field finding, now the single
   most precise mechanism in the whole synthesis.
7. ~~Pattern Theory Ch.5 §"Shared Pattern Thinking"~~ **DONE** — bridges individual Flood experience to
   the Syncretic Religion's origin; also surfaced a legitimate darker/coercive reading useful for the
   "no good endings" discipline. Full writeup in `03` section 4.
8. ~~Distributed Control of Robotic Networks §4.2-4.3~~ **DONE** — rendezvous algorithms, real named
   convergence algorithms, and the finding that convergence can split into multiple non-merging clusters.
9. ~~Networks of Networks Ch.3~~ **DONE** — feedback/no-feedback dependency, multiple support, and the
   sharpest structural finding in the whole pass: outcomes bifurcate unpredictably near the critical
   threshold (real numerical result, not inference).
10. ~~Networks of Networks Ch.4~~ **DONE** — turned out to be the best single read of the whole pass, not
    diminishing returns at all. See `01` section 7.
11. Nothing outstanding remains that's expected to change the synthesis. Everything else in this checklist
    (Ch.5 §5.3+, Ch.6, distributed-snapshot/mutual-exclusion chapters, remaining cognitive-science titles,
    etc.) is pure optional depth with no specific open question driving it anymore.
