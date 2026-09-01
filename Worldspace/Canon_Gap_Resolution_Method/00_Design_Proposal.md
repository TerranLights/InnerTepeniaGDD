# The Canon Gap Resolution Method — Design Proposal

> ## ✅ SUPERSEDED — BUILT 2026-08-31. This file is retained as the record of *why*, not as procedure.
>
> **The system exists.** Start at **`00_RUNBOOK.md`**. This proposal is kept because its §0 (why this exists,
> what it is intended to achieve) remains the best statement of the system's purpose, and because a later
> reader should be able to see what was proposed against what was actually built.
>
> ### What the build changed from this proposal — five substantive departures
>
> 1. **Five paths became seven.** The proposal missed two modes this project already practices heavily:
>    **developer creative elicitation** (the City Vision Notes process — measurably the project's most
>    productive acquisition mode ever, and *categorically different* from the "developer ruling" the proposal
>    did have) and **deep source extraction** (the PDF/book pipeline, which has its own existing
>    infrastructure). See `02`.
> 2. **The "single project-wide registry listing every open gap" was killed by measurement.** A repo scan
>    found **2,872 `TBD` occurrences across 495 files.** An exhaustive registry is not achievable and would be
>    untrustworthy in the one way that matters — nobody could tell whether a gap's absence meant "resolved" or
>    "never captured." **The registry is now demand-driven** (`01` §2).
> 3. **Triage went from "classify the path" to a four-way gate that mostly *protects* gaps.** The measurement
>    showed most TBDs are **scheduled deferrals** (*"TBD for DLC 3 design"*) or **template scaffolding**, not
>    open questions — and closing those early is actively harmful. This produced **LAW A: an open gap is not a
>    defect**, which the proposal did not anticipate at all.
> 4. **The deposit discipline became the system's core**, not a §2.5 afterthought. It is the only part with a
>    fully-documented recorded failure behind it (the Cape Adare deposit chain), and it produced the one
>    genuinely new mechanism here: **a greppable conclusion-tier marker** (`03` §3), tested with a
>    proof-of-hit control before being written into the method.
> 5. **LAW C — the method is not its test cases** was added at the developer's direction mid-build, after the
>    build itself created a live contamination vector (a rule file teaching classification with Cape Adare's
>    own conclusion content in it).
>
> ### The proposal's five open questions, now answered
>
> 1. **Registry/log schema and location** → `04` §7; live files at `Gap_Registry.md`, `Resolution_Log.md`,
>    `Developer_Ruling_Queue.md`.
> 2. **How batched rulings are surfaced** → a standing `Developer_Ruling_Queue.md`, each entry carrying five
>    prepared fields, accumulating rather than interrupting. **Validated on first use** — DRQ-03 was ruled the
>    day it was written.
> 3. **Trigger mode** → **explicit invocation only**, and now for a stated reason: an acquisition system that
>    ran on its own initiative would routinely fill scheduled deferrals, violating LAW A as a matter of
>    routine.
> 4. **Whether resolved facts need gate-equivalent verification** → **yes, six gates** (`04`). Four descend
>    from specific recorded failures; two are marked prospective, because a gate claiming a pedigree it does
>    not have is exactly the unearned authority this project's methodologies refuse themselves.
> 5. **Naming** → **kept.** Reconsidered during the build and retained: it parallels
>    `Real-World_Basis_Extrapolation_Method.md`'s convention, and churn has a cost. Noted that "gap
>    resolution" undersells the deposit half, which is the system's most novel contribution.

**Status of the original document below: DESIGN PROPOSAL, written 2026-08-31**, as a handoff for a build
session. **Superseded by the built system, but not deleted** — its reasoning is the record.

---

## 0. Why this exists, and why it is a separate system

### 0.1 The immediate trigger

**Origin.** During Highway 37 (Run 6) and Cape Adare (Run 7) of the Universal Location Methodology, both passes
ended with substantial REQUESTED-item lists — real, admissible facts the location methodology needed but could
not supply, because supplying inputs is explicitly outside what a derivation engine is supposed to do (`05_The
_Input_Contract.md` §0: *"a derivation engine cannot supply its own axioms"*). Cape Adare's own run produced
eleven such items and, per a developer observation mid-pass (recorded as M-54 in `Test_Runs/OBSERVATIONS_and_
Methodology_Findings.md`), its high null-count traced almost entirely to this — genuine input scarcity, not a
weakness in the technique.

### 0.2 The deeper problem this actually addresses, stated in full

**A methodology that can classify a gap but cannot close one has only done half its job, and the missing half
compounds rather than staying stable.** Four specific costs, each already visible in this project's own history
before this proposal existed:

1. **Misdiagnosis risk.** A run with many nulls looks, from the outside, exactly like a run where the technique
   underperformed. M-54 exists precisely because this was almost the reading given to Cape Adare's own result —
   the developer had to notice, mid-pass, that the nulls were an input problem, not a method problem. **Without
   a system that actually closes those gaps, every future thin-canon location risks the same misreading, over
   and over, each time requiring a human to notice the distinction freshly rather than a process that already
   assumes it.**
2. **Duplicated effort.** Nothing currently stops two different sessions — on two different locations, or even
   the same location run twice — from independently researching the identical real-world comparable, or asking
   the developer the identical question in slightly different words. The project's own Research Log convention
   already fixed this *within* a single location's own repeated passes; **nothing fixes it *across* locations**,
   because no file currently exists whose job is to know what has already been asked project-wide.
3. **Scattered, one-at-a-time developer interruption.** Every REQUESTED item that is genuinely RESERVED
   (a name, a date, a scope call) currently surfaces to the developer exactly when a given pass happens to hit
   it — one small decision at a time, spread across however many separate sessions eventually run into it.
   **This is the single most avoidable cost on the list**: RESERVED decisions do not need to be made at the
   moment they're discovered, only before the location's own final pass is considered finished, which means
   they can be batched into far fewer, larger decision sessions instead.
4. **A ceiling on how deep any single pass can go.** LAW 0 — the standing rule governing every location pass —
   demands depth over speed and explicitly refuses to treat "no time limit" as an excuse to leave a pass thin.
   But a pass genuinely cannot manufacture research time for eleven different open questions inside its own
   single sitting without either rushing each one or abandoning several. **A dedicated system whose only job is
   closing gaps can spend real, unhurried time on exactly the kind of research (a real heritage-site governance
   model, a real free-port city's civic structure) that a location pass can only gesture at and flag, precisely
   because gap-closing is that system's entire mandate rather than one competing demand among eleven others.**

### 0.3 What this system is actually intended to achieve

**Not a one-time cleanup of Cape Adare's eleven items.** The intended outcome is a standing, reusable
capability: **a place in the project's own architecture whose specific job is turning "we don't know this yet"
into "here is the answer, and here is exactly how we know it" — for any consumer, on an ongoing basis, growing
richer every time it runs rather than being rebuilt from scratch per location.** Concretely, that means:

- **Every location this project ever builds — through ULM or any other pipeline — inherits a shrinking, not
  static, pool of unanswered questions**, because gaps closed for one location's sake (a real-world research
  thread, a derivation formula, a cross-reference pattern) often generalize to others facing the same category
  of question, the same way `Real-World_Basis_Extrapolation_Method.md`'s own Cancer worked example already
  taught lessons ("secondary and supporting picks are where the value is") that apply far beyond Cancer itself.
- **The developer's own time is spent on the decisions only they can make** (names, dates, scope calls) **and
  spent on them in batches**, rather than as constant small interruptions competing with everything else
  happening in a given session.
- **A location pass's own REQUESTED list stops being a dead end.** Today, once ULM logs a REQUESTED item, that
  item's fate depends entirely on whether some future session happens to remember it and happens to have time.
  **With this system, a REQUESTED item has an actual destination** — it enters a real queue, gets triaged, and
  is either closed or explicitly still-open-and-tracked, never simply forgotten in a folder nobody revisits.
- **The project accumulates a genuine, checkable body of *how it knows what it knows*** — not just more canon,
  but canon whose provenance is tracked the same rigorous way ULM already tracks its own findings, which is
  what makes it trustworthy enough for a future cold pass to actually use as PROVIDED input rather than
  something a later session has to re-verify from scratch.

**In short: ULM (and everything like it) is a synthesis engine, correctly built to synthesize rather than
invent axioms. This system is the thing that goes and gets the axioms — deliberately, trackably, and without
making every single synthesis pass stop and do that work itself.**

### 0.4 The gap this proposal addresses, structurally

**`05_The_Input_Contract.md` already classifies missing input precisely** (PROVIDED / RESERVED / PRODUCED /
REQUESTED) and defines what a well-formed request looks like (§5). **It does not, and should not, define how a
REQUESTED item actually gets answered.** Building that answering procedure into the location methodology itself
would conflate two genuinely different jobs: *deriving a location's culture from its inputs* (ULM's job) and
*going and getting inputs that don't exist yet* (this system's job).

**Developer's own framing, verbatim, given directly**: *"the input-data-creation process will need to be
separate from the location-synthesis methodology. Those will need to be two separate (though interacting)
systems. So, the data-creation process will need to be developed separately."*

**Scope, confirmed with the developer before writing this**: **general-purpose, not ULM-specific.** This system
should be built to close a missing-canon gap for *any* consumer in the project — the Universal Location
Methodology, a district Phase pass, a City Megasheet pass, questline design, character work, anything that hits
a REQUESTED-shaped gap — not narrowly wired to ULM's own REQUESTED block format. **ULM is the system that
surfaced the need for this and will be one of its consumers, not its reason for existing.**

---

## 1. The interaction boundary — how the two systems actually connect

**They do not call each other directly, and should not.** The boundary is canon itself:

- **A consumer (ULM or otherwise) never invokes this system mid-pass.** It emits a REQUESTED item (or leaves a
  TBD/open question in whatever it's writing) and proceeds without it, exactly as ULM already does today.
- **This system reads canon independently**, on its own schedule, looking for REQUESTED items and TBD flags
  wherever they exist across the project.
- **It writes its answers back into the project's own shared canon** — a Specs file, a registry, a dedicated
  reference file — **never into a consuming methodology's own run folder or output.** ULM's `Test_Runs/`
  folders, for instance, are never targets for this system's writes.
- **The next time any consumer reads that canon**, the answer is simply there, admissible, sourced — the
  consumer benefits without the two systems having interacted in real time at all.

**Why this shape, specifically**: it means this system can be paused, run on a completely different schedule,
or handed to a different session entirely, without ULM (or any other consumer) needing to know or care that it
exists. **Loose coupling through shared canon, not tight coupling through direct invocation.**

---

## 2. Proposed core structure

### 2.1 Intake

A gap enters this system's own queue from either:
- A REQUESTED item emitted by any consuming methodology (found by scanning `Test_Runs/` folders, Megasheet
  files, or wherever a consumer's own REQUESTED-item convention lives).
- An existing TBD / "Open Questions" flag already sitting in project canon, whether or not any methodology
  pass has formally requested it yet.

### 2.2 Triage — five proposed resolution paths

Each gap gets classified into exactly one path (or flagged as currently unclassifiable):

1. **Real-world research.** Reuses `Real-World_Basis_Extrapolation_Method.md`'s own discipline directly rather
   than duplicating it — research a real, specific comparable (never a category), fuse against established
   in-fiction fact, divergence stated explicitly.
2. **Cross-reference.** The answer already exists elsewhere in this project's own **admissible** canon — a
   sibling location's Spec, a project-wide registry, a national-scale reference file — and simply hasn't been
   connected to this specific gap yet. **Must respect the same admissibility rules ULM already uses** (`05`
   §6.1) — a cross-referenced fact must itself be an attribute, not a smuggled-in conclusion from an otherwise
   withheld file.
3. **Derivation.** Computable from other already-known facts via an established in-project formula or method —
   census share-weighting, retention arithmetic (Census I → II), density arithmetic (population ÷ extent), or
   any other formula this project has already standardized.
4. **Developer ruling, batched.** For genuinely RESERVED items — a proper name, an official date, a scope
   decision only the developer's authority can settle. **The "batched" part is the actual design contribution
   here**: rather than asking one REQUESTED item at a time as each individual pass happens to surface it, this
   system should accumulate RESERVED-classified gaps into a single, periodic batch for the developer to rule on
   together — fewer, larger decision sessions instead of constant small interruptions.
5. **Withheld-file check.** Specific to gaps generated by a cold pass under quarantine (ULM's own signature
   case): the answer may already exist in a location's own withheld culture-pass material, simply inadmissible
   as an *input* to that specific cold derivation. Checking it is not re-running the cold pass — it's a
   separate act of just reading the answer out of material that was never actually missing, only quarantined.

**A gap that fits none of these five cleanly should be logged as genuinely unresolved, not forced into the
nearest-fitting path.**

### 2.3 A single project-wide open-gaps registry

**One file, not one per location or per consumer**, listing every open gap, its source (which pass/consumer
raised it, or which existing TBD it comes from), its triage classification, and its status. **Purpose**: before
any research is run, check whether the question has already been asked — this is the direct fix for exactly the
kind of duplicated effort a per-location-only system would risk (two different passes independently researching
the same real-world comparable, for instance).

### 2.4 A resolution log

**Same discipline as ULM's own Research Log convention** (`Real-World_Basis_Extrapolation_Method.md` Step F),
generalized project-wide rather than per-location: what was asked, exact search strings if research-path,
which canon file if cross-reference-path, the formula if derivation-path, the developer's exact words if
ruling-path, sources, and — critically — **open threads**, the same discipline that has already proven
valuable in every ULM research log so far.

### 2.5 Output and provenance tagging

**Resolved gaps get written directly into the project's shared canon**, tagged with provenance the same way
canon-migration is already tagged elsewhere in this project (`05_The_Input_Contract.md` §6.1b's own precedent:
*"provenance travels with a migrated fact... a bracketed clause"*). **A resolved gap should never enter canon
silently** — the same recording discipline ULM already applies to its own findings should apply here.

---

## 3. Governing principles to inherit, not reinvent

**This system should not invent its own version of rules the project has already settled.** Specifically:

- **Source-not-specification / divergence-stated** (`Real-World_Basis_Extrapolation_Method.md`) — governs every
  research-path resolution.
- **GPS-only / No National Stereotypes** (`TepenianUniverseTimeline/Reference/No_National_Stereotypes.md` — **universe repo, not local**; binding project-wide) —
  governs any research touching real-world national/ethnic comparables.
- **The canon authority hierarchy** (`00_RUNBOOK.md` §A, universe repo > project canon > locked canon >
  Proposed: > staging) — governs what a resolved gap is even allowed to assert, and where it ranks once written.
- **No invented proper names for people** — the same standing rule ULM already carries; a "developer ruling"
  path exists specifically because this system cannot discharge that authority itself.
- **Never carry one location's answer into another's** — the same anti-convergence discipline governing every
  other generative technique in this project applies to cross-reference-path resolutions specifically, since
  that path is structurally the most tempting place to quietly homogenize two locations.

---

## 4. Open questions for the build session

**Not yet decided, and should be resolved before or during the actual build**, not silently assumed:

1. **Exact registry/log file format and location** — proposed above only in shape, not in schema.
2. **How the "batched developer ruling" queue is actually surfaced** — a periodic summary document? A running
   file the developer checks on their own schedule? Not designed here.
3. **Whether this system runs on its own trigger/schedule, or only when explicitly invoked** — this proposal
   assumes explicit invocation (a session is asked to "run a Gap Resolution pass"), but an automated or
   periodic mode is not ruled out and not designed here either.
4. **Whether resolved facts require any QA-gate-equivalent verification** before being written to canon, or
   whether the resolution log's own discipline is considered sufficient — ULM's own gates exist because a
   derivation pass can go wrong in specific, catalogued ways; this system's own failure modes have not yet been
   catalogued the way ULM's seven historical errors were, because it hasn't been run yet.
5. **Naming.** "The Canon Gap Resolution Method" is this proposal's own working name, chosen to parallel
   `Real-World_Basis_Extrapolation_Method.md`'s naming convention — not confirmed as final.

---

## 5. What prompted this, for the record

Cape Adare's own eleven open REQUESTED items (`Universal_Location_Methodology/Test_Runs/2026-08-31_CapeAdare
_Run7_Cold/14_Step9_Record_and_Step10_Readiness.md`) are the concrete case that produced this proposal, and are
a ready-made first test case once this system is actually built — they already span all five proposed
resolution paths: a developer-only ruling (St. Carsten's feast date), several research-closable items (real
heritage-site governance, real gateway-city precedents, rookery seasonality, land area), a cross-reference-
closable item (the southward road connection, checkable against sibling Janbogo cities' own admissible Specs),
and a withheld-file-check-closable set (several items likely already answered in Cape Adare's own quarantined
culture pass).
