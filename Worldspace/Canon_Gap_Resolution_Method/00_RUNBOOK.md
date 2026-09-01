# RUNBOOK — The Canon Gap Resolution Method

**Built 2026-08-31, from the design proposal in `00_Design_Proposal.md`. This is the operational entry point.
Start here.**

> **"CGRM" = Canon Gap Resolution Method** — this system's own initials, used as the prefix for gap IDs
> (`CGRM-001`, `CGRM-002`…) and for the provenance tags this system stamps into canon
> (`[CGRM 2026-08-31 · Path 4 · source]`). **Gap IDs are numbered continuously across the entire project, not
> per scope** — so `CGRM-004` and `CGRM-013` may belong to completely different locations, characters, or
> subsystems. Continuous numbering is deliberate: it makes recurrence visible across scopes, the same reason
> the location methodology numbers its observations continuously.
>
> *(Defined here because a readiness check found the abbreviation used ~40 times across this system and
> stamped into canon files, and expanded exactly zero times.)*

**What this is.** The project's system for **acquiring canon that does not exist yet** — turning *"we don't
know this"* into *"here is the answer, and here is exactly how we know it."* It is deliberately **separate
from** every synthesis methodology that consumes canon (the Universal Location Methodology, the district Phase
passes, the City Megasheet pipeline, character work, questline design), and interacts with them only through
shared canon, never by direct invocation.

**Status: NEW. Partially grounded, not yet run.** Unlike the Universal Location Methodology — whose every rule
descends from a specific recorded failure — most rules here descend from **prior art this project has already
practiced without formalizing** (seven distinct acquisition modes, §2 of `02`), plus **two genuinely recorded
failures** (the Cape Adare deposit chain and the Sejong/Abowasa post-sweep-window cases, both below). **Treat
the first several real runs as tests of this instrument as much as of the gaps they close.**

---

# LAW A — AN OPEN GAP IS NOT A DEFECT

**The governing law. It overrides every other instruction in this system.**

**This system exists to close gaps, which means it will be structurally biased toward closing them.** That bias
is the same shape as the self-audit bias the project has already measured repeatedly: *"self-audit error in
this project has run in one direction — toward flattering the pass — on every occasion it has been measured."*
An acquisition system flatters itself by **closing things**, and its characteristic failure is therefore **not
leaving a gap open too long, but closing one that should have stayed open.**

**Three kinds of gap must be actively protected from this system, not served by it:**

1. **Scheduled deferrals.** A gap explicitly assigned to a later, better-informed stage — *"TBD for DLC 3
   design"* being this project's most common phrasing. **Closing one early is not helpful; it forecloses a
   decision that belongs to a stage with more information than this one has.** *(Empirically the dominant
   pattern: a scan of `Specs/Rothera.md`'s own TBDs found nearly every one of them scheduled this way.)*
2. **Reserved decisions.** Anything whose authority belongs to the developer — a person's proper name, an
   official date, a scope call, a ruling that binds many locations at once. **This system may prepare and
   present these; it may never settle them.**
3. **Gaps whose openness is itself load-bearing.** Occasionally a location, character, or system is *supposed*
   to have an unanswered question in it — a mystery, a deliberately unresolved tension. **Check before
   closing.** *(See the standing project convention that a mystery's full resolution stays private and media
   receives only ambient hints.)*

> **The success measure of this system is NOT the number of gaps closed.** A run that closes two gaps, protects
> six from premature closure, and correctly routes three to the developer has done better work than a run that
> closes eleven.

**And the corollary that makes LAW A operational rather than decorative:** **every run must report what it
declined to close, and why**, in the same breath as what it closed. A run reporting only closures is not
reporting; it is advertising.

---

# LAW B — WHERE A FACT LANDS MATTERS AS MUCH AS WHETHER IT IS TRUE

**The second governing law, and the one this system's single recorded failure is about.**

**A true fact deposited into the wrong tier of canon silently breaks every downstream consumer that reads that
tier.** This is not hypothetical. It has happened, it is fully dated, and every step of it is written down in
this project's own files:

> **The Cape Adare deposit chain — the founding case.**
>
> - **2026-07-05.** A City Vision Notes session produced genuinely excellent new canon for Cape Adare: a
>   low-density/small-town civic character, a heating-infrastructure "oasis" microclimate, penguin-keeping,
>   an unhurried pace of life, an acoustic-instrument music culture. **This was acquisition working exactly as
>   intended** — content no research or derivation could have produced.
> - **The same session deposited it into `Specs/Cape_Adare.md`.** The Vision Notes file records the deposit
>   itself, in its own "Corrections/additions applied directly to other files this session" section. **Nothing
>   about this was careless.** It was reasonable, well-intentioned, and helpfully documented.
> - **2026-08-30.** The Universal Location Methodology is created. Its admissibility rule (`05` §6.1) treats
>   `Specs/` as the *first, safest, attribute-tier* source in its reading order — because no prior pass had
>   ever found a Specs file containing conclusions.
> - **2026-08-31.** ULM Run 7 runs cold on Cape Adare, clears `Specs/Cape_Adare.md` as admissible after
>   checking its first ~20 lines, and then — reading the full file for unrelated research reasons — **finds
>   the 2026-07-05 vision content sitting in a "Character & Culture" section.** Contamination, caught by luck
>   rather than by procedure. Logged as M-51; `05` §6.1d written the same day.
>
> **Eight weeks passed between the deposit and the damage, and nobody in that chain did anything wrong.** The
> acquisition was right, the deposit was documented, the synthesis methodology's assumption was reasonable
> given its evidence. **The failure is structural, and structural failures are fixed with structure.**

**What follows is binding, and is `03_Deposit_Discipline.md`'s entire subject:** every fact this system
acquires is classified by **kind** (attribute / conclusion / decision) before it is written anywhere, deposited
into a destination that matches its kind, and — where a conclusion must live inside an otherwise-attribute file
— **marked with a mechanical, greppable boundary** so that a future cold pass can exclude it by running a
command rather than by happening to read far enough.

---

# LAW C — THE METHOD IS NOT ITS TEST CASES

**Added 2026-08-31, at the developer's direction, during this system's own build.**

> *"It's extremely important to distinguish between the overall 'gap registry' and 'missing data synthesis'
> being one thing, and using Cape Adare as a 'test run' instance as a separate thing. That way, Cape Adare
> running as a test case won't corrupt the overall synthesis methodology itself."*

**The specific danger.** Cape Adare is the case that produced the realization this system was needed — which
makes it precisely the case most likely to quietly shape the system around its own idiosyncrasies. **A system
built around its founding example stops being general without anyone noticing**, because every rule still
*looks* general while silently encoding one scope's peculiarities.

**This project has already paid this exact price once.** The location methodology's first test run was a
three-city co-write, and it produced *"a methodology validated on the least representative configuration in
the project"* — not through carelessness, but because nothing in the procedure ever asked whether the test case
was typical.

**The separation, binding:**

| | |
|---|---|
| **The method** — `00`–`04`, `Gap_Registry.md` | **Scope-agnostic.** May cite a real case as a **recorded failure that grounds a rule** — that is how every rule in this project earns authority. May **not** be shaped by any one scope's gap list, ratios, or path distribution. |
| **An instance** — `Test_Runs/*` | One scope's actual data. **Nothing in it generalizes.** Triage splits, path distributions, and closure rates are properties of that scope. |

**Three operational consequences:**

1. **Never read an instance's ratios back into the method.** *(Worked case: the first seeding produced zero
   SCHEDULED items — a striking figure that means nothing general, because both scopes came from synthesis-pass
   REQUESTED blocks, which skew LIVE by construction. A TBD-swept scope would invert it.)*
2. **A rule file citing a real case must fence that case's conclusion-tier content** (`03` §3), or the rule
   file becomes a contamination vector for the very scope it describes. **This was a live defect in this
   system's own first draft, caught and fixed the same session.**
3. **Register any such citation in the location methodology's own provenance manifest**, so a future cold pass
   on that scope knows to skip it.

---

# The interaction boundary — restated, because it is load-bearing

**This system and its consumers never call each other. The boundary is canon itself.**

| | |
|---|---|
| **A consumer** (ULM, a district phase, Megasheet work, questline design) | Emits a REQUESTED item or leaves a TBD, and **proceeds without the answer**. It never waits on this system and never invokes it. |
| **This system** | Reads canon on its own schedule, acquires what it can, deposits into canon per LAW B. **Never writes into a consumer's own run folder or output** — ULM's `Test_Runs/` folders in particular are never write targets. |
| **The next consumer pass** | Simply finds the answer present, admissible, and sourced. The two systems never interacted in real time. |

**Why this shape:** it means this system can be paused, rescheduled, or handed to an entirely different session
without any consumer needing to know it exists. **Loose coupling through shared canon.**

---

# ⚠ Tooling note — graphify, and when it must NOT be used

**This repo enforces a `PreToolUse` hook requiring `graphify query` before file reads, and `CLAUDE.md` repeats
it.** This system searches heavily, so it will hit that hook constantly. **The guidance differs by path, and
the difference is not cosmetic:**

- **Paths 1, 2, 4, 5 — graphify is a legitimate accelerator, with a known limitation.** Use it to *prioritize
  where to look*, then read the file. **Never trust a graphify zero**: the project has recorded that large
  consolidated files are indexed at roughly 1/45th the density of comparable smaller ones, and that a query
  for one book's contents returned entirely irrelevant nodes — leading to a conclusion that material was
  unextracted when 585 lines of it existed. **Grep and graph both prioritize; neither verifies.**
- **⛔ Path 3 — do not use graphify at all.** A query naming the subject returns extracts from whatever
  withheld culture-pass material exists for it. **Retrieval indexes content; quarantine is a property of
  provenance, and no corpus-wide index can honor it.** Navigate by `find`/`ls` and direct reads. **This is the
  same deliberate deviation the location methodology already declares**, and it should be declared in the run's
  own log the same way.

---

# When to run this

**Explicit invocation only.** There is no automatic or scheduled mode, deliberately — an acquisition system
that runs on its own initiative would fill scheduled deferrals (LAW A violation 1) as a matter of routine.

**Legitimate triggers:**
- A synthesis pass has finished and left a REQUESTED block behind *(ULM Runs 6 and 7 both did; those items
  seed the registry today)*.
- Someone is about to run a synthesis pass on a location and wants its inputs improved **first** — the highest-
  value timing, since it converts a would-be thin pass into a rich one rather than fixing one afterward.
- The developer wants to spend a session on batched rulings (`Developer_Ruling_Queue.md`).
- A scoped discovery sweep is wanted for one location or subsystem (`01` §3).

---

# The procedure

**Step 1 — Scope it.** Name the specific subject whose gaps this run will work on. **Never "the project."**
*(Empirical reason: a repo-wide scan finds 2,872 `TBD` occurrences across 495 files. An unscoped run is not a
run; it is a survey with no end.)*

> **⚠ A scope is not necessarily a place.** *(Developer instruction, 2026-08-31, during this system's own
> build.)* **A scope may be a PERSON — a character — and characters are empirically the project's second-
> largest concentration of open gaps**, behind only city `Specs/` files (70 `TBD` occurrences in
> `Worldspace/Characters/Dolls/` in the same scan, plus entire folders belonging to characters who do not yet
> have names). **Valid scopes include:**
>
> - **A location** — a city, district, corridor, structure, subnet, station.
> - **A person** — a Doll, a companion, a notable figure, an NPC role-archetype awaiting definition.
> - **A subsystem** — a mechanic, a faction, a religion, an economy, a symbol system.
> - **A consumer pass** — everything one specific completed pass left open (its whole REQUESTED block).
>
> **Person-scope triages differently from location-scope, and knowing that in advance matters** (`01` §3.6):
> character gaps skew heavily toward **RESERVED** (proper names especially — the project's binding
> no-invented-names rule guarantees it) and toward **SCAFFOLD** (the per-character template file set), which
> means a person-scoped run will typically close fewer gaps directly and route more of them to the developer
> than a location-scoped run does. **That is the correct result for that scope, not an underperforming run** —
> see LAW A.

**Step 2 — Intake.** Collect candidate gaps within that scope, per `01_Intake_and_Triage.md` §2–3.

**Step 3 — Triage each one, four ways** (`01` §4): **LIVE · SCHEDULED · SCAFFOLD · RESERVED.** **Only LIVE
items proceed.** SCHEDULED and SCAFFOLD are recorded and left alone; RESERVED goes to the ruling queue.

**Step 4 — Check what is already known before acquiring anything.** **Two places, not one** — this was found
unrunnable as originally written, when the standing registry held 0 rows while 14 triaged items sat in an
instance file:

1. **`Gap_Registry.md`** — the standing queue of gaps *actively being worked or already resolved.* If the
   question has been asked, answered, or attempted, **do not re-run it.**
2. **`Test_Runs/*`** — instance files, which hold **triaged-but-not-yet-started** gaps. These are where a
   previous run's findings wait, and they will usually outnumber the standing registry's rows early on.

> **⭐ The promotion trigger, which was previously described but never actually specified:** **an item moves
> from an instance file into `Gap_Registry.md` at the moment a run selects it for work** — not when it is
> triaged, and not in bulk. **The standing registry is a record of commitment, not of intent.** This keeps it
> from filling with work nobody has started, which is precisely what would make it read as stale and stop
> being consulted.

**Step 5 — Select an acquisition path per LIVE gap, cheapest viable first** (`02`): cross-reference →
derivation → withheld-file check → light real-world research → deep source extraction → developer ruling →
developer creative elicitation. **Record why the chosen path was chosen, and which cheaper ones were ruled out.**

**Step 6 — Acquire.** Run that path's own procedure. **Log as you go, not afterward** — the same
write-it-when-it-happens discipline the research-log convention already enforces project-wide.

**Step 7 — Classify by kind and deposit** (`03`). Attribute / conclusion / decision → matching destination,
with provenance and, where required, a mechanical conclusion-tier marker.

**Step 8 — Run the six verification gates** (`04_Verification_Gates.md`). Each attaches to a real recorded
failure; none is optional.

**Step 9 — Record.** Update `Gap_Registry.md`, append to `Resolution_Log.md`, and **report what was declined
as prominently as what was closed** (LAW A's corollary).

**The run's output block** — *(added 2026-08-31 during the readiness check; Step 9 previously required this
report without ever defining its shape, which is how a requirement quietly becomes optional)*:

```
## Gap Resolution Run — <scope> — <date>

**Intake:** n candidates          **Triaged:** LIVE n · SCHEDULED n · SCAFFOLD n · RESERVED n
**Paths exercised:** <which, and how many items each>

**CLOSED (n):**      <id — one line each, with the path used>
**PROTECTED (n):**   <id — and WHY it was declined. This section is not optional and not an apology>
**BLOCKED (n):**     <id — what blocks it, and what would unblock it>
**ROUTED (n):**      <id — sent to the developer ruling queue>
**UNRESOLVED (n):**  <id — paths tried and why each failed>

**Gates:** <which of the six fired, and what each found — including clean passes>
**Deposits:** <file, kind, marker applied?> — every one greppable via its [CGRM …] tag
**Open threads left unchased:** <what, and what each might yield>
```

**A run reporting only the CLOSED line has not reported.** Per LAW A, protected and blocked counts are the
evidence that triage was actually run rather than skipped on the way to closing things.

---

# Step 10 — THE READINESS CHECK

**Standing step, added 2026-08-31. Run it before the first run of a session, and before handing off.**

> ## VERIFY, DO NOT ASSERT.
>
> **This step exists because it was run twice on this system during its own build and found real, distinct
> defects both times** — including one that would have caused actual damage on the first acquisition run.
> **The person best placed to declare readiness is the one who can no longer see what they have absorbed.**

**The six checks, in the order that has actually caught things:**

1. **Every cited path resolves.** Extract every file path this system references and confirm it exists.
   **⚠ Remember the repo boundary**: a local search cannot see the universe repo at
   `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/`, so a "not found" for
   universe canon is a false negative. *(Caught: `No_National_Stereotypes.md` cited as a bare local path in
   three places, including a binding constraint on Path 4 — the exact trap this project has recorded, where
   six escalating "repo-wide" clean passes each searched a space that structurally could not contain the bug.)*
2. **Is every procedure step actually runnable as written?** Not plausible — *runnable*. *(Caught: Step 4 said
   "check the registry," which held 0 rows while 14 triaged items sat elsewhere. A session following the
   procedure literally would have found nothing and proceeded blind.)*
3. **Are the safety guards scoped to the right object?** *(Caught: Path 3's guard asked whether the *emitting
   pass* was finished, when the hazard is any pending pass on the *subject*. It would have passed a case that
   should have failed.)*
4. **Does every required output have a defined format?** A required report with no template quietly becomes
   optional. *(Caught: Step 9's decline-reporting requirement had no output block.)*
5. **Does each path likely to run have gate coverage?** *(Caught: Path 1, the most-likely-first path, had no
   dedicated gate while Paths 2, 4 and 5 each did.)*
6. **State plainly what has and has not been exercised.** Untested paths are not defects; **untested paths
   described as ready are.**

---

# Where everything lives

| File | What it is |
|---|---|
| **`00_RUNBOOK.md`** | **this file — the laws and the procedure** |
| `00_Design_Proposal.md` | the original proposal, kept as the record of why this exists |
| `01_Intake_and_Triage.md` | what counts as a gap; the four-way triage; scoped discovery |
| `02_Acquisition_Paths.md` | the seven paths, cheapest-first, each with cost, yield, and failure modes |
| **`03_Deposit_Discipline.md`** | **LAW B's operational half — kind-tagging, destinations, the marker convention** |
| `04_Verification_Gates.md` | the six gates, each attached to a recorded failure |
| `Gap_Registry.md` | **live, scope-agnostic** — the demand-driven work queue and its schema |
| `Resolution_Log.md` | **live, append-only** — what was acquired, how, from where, and what was left unchased |
| `Developer_Ruling_Queue.md` | **live** — batched decisions awaiting developer authority, with groundwork prepared |
| `Test_Runs/` | **instances, NOT the method** — per-run data. Nothing in here generalizes (LAW C) |

**Inherited, not reinvented** — this system uses these rather than writing its own versions:
`../Locations-and-Levels/Real-World_Basis_Extrapolation_Method.md` (research discipline) ·
**`/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md`** (GPS-only, binding — **⚠ this is in the UNIVERSE REPO, outside this repo; a repo-local search will not find it**) ·
`../Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md` §A (the canon authority hierarchy) ·
`../Locations-and-Levels/Universal_Location_Methodology/05_The_Input_Contract.md` §6.1 (admissibility) ·
`Reference/Real-World/Book_Extraction_Index.md` (check before mining any book).
