# Davis — T8 Rounds · Phase 2 (Composition & Arrival)

**Companion to `04_Phase_02_Composition_and_Arrival.md`.** Records how the phase was verified and how the three
readers' disagreements were settled. ⛔ **The phase file is the output; this file is the evidence for trusting
it.**

---

## Round 1 — three isolated readers, blind and independent

| Reader | Deliverable | Lines | Shape |
|---|---|--:|---|
| **A** | `.t8_phase2_readerA.md` | 1,250 | Four collisions · axis *"Allocated exiles, then natives"* · all seven modes · the arrival question once per Act · Process C rebuilt at real scale · three unused instruments · the pass's central question · methodology findings |
| **B** | `.t8_phase2_readerB.md` | 1,192 | Five collisions · axis *"Assigned terminally; native by default"* · formalize-before-inventing ledger · all seven modes **plus two canon modes with no taxonomy row** · divergence operator · Hirschman · persistence test |
| **C** | `.t8_phase2_readerC.md` | 818 | Five collisions · axis *"Allocated · unclocked · outward-sorted"* · headline household geometry · all seven modes · lapse as the divergence mechanism · who-is-not-here with a sourced mechanism · repel-is-NULL |

**All three were given the identical brief and the identical contracted reading list (10 sources), and none saw
another's output.**

---

## Round 2 — `triple_read_verify.py`, mechanical ground truth

```
required files: 10
agents: agent1, agent2, agent3
… 30 of 30 proof blocks: ✅ all fields match ground truth
=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

**Every `LRANGE`, `LINES`, `L1`, `LMID`, `LLAST` and `QUOTE` field, for all ten sources, for all three readers,
matched the real files byte-for-byte after normalization.** ⛔ **No proof block was edited to achieve this.**

> ### ⭐⭐⭐ A KILLED ACTION, RECORDED BECAUSE IT IS THE MOST IMPORTANT ENTRY IN THIS FILE
> **The resume plan carried a standing action: rewrite reader B's `QUOTE` field for `03_Research.md` "in place,"
> on the premise that the quote had been recorded without its markdown markup and that this was the one Round-2
> failure (29/30).**
>
> ⛔ **The premise was false.** `triple_read_verify.py`'s `norm()` strips `*`, `` ` ``, `_`, `[`, `]`, `>`, `|`
> and `#` **from both sides** before comparing, normalizes dashes, quotes and whitespace, lowercases, **and the
> QUOTE check is a substring test.** ⇒ **B's markup-stripped quote matched ground truth all along, and the
> leading ⛔ glyph on the source line is absorbed by the substring test.**
>
> ✅ **Established by running the verifier unmodified, before touching anything: 30/30, unanimous.**
>
> ⇒ ***Had the plan been executed as written, a reader's PROOF block would have been edited to fix a failure
> that did not exist — tampering with verification evidence to satisfy a misdiagnosis, in the one file whose
> entire purpose is to be un-tampered-with.***
>
> ⭐ **The rule that caught it: RUN THE INSTRUMENT BEFORE "FIXING" WHAT IT REPORTS.** **This is `M-225`
> generalized — *verify the instrument before trusting a failure* — applied not to a script and not to a
> reader's eyes, but to a written plan carried across sessions.** **Filed as `Q.4` in the phase file.**

---

## Round 3 — agent-to-agent comprehension cross-check

**Round 2 proves the reading happened. It cannot judge whether it was understood.** Round 3 settled six
divergences. ⭐ **Every settlement below narrows a claim; none widens one.**

### 1. ⭐⭐ Fire #5 — **three quarters retired, not four**

| Reader | Position |
|---|---|
| **A** | **4 of 4 discharged.** Heritability answered as **PROSPECTIVE** — II.2.1 reaches *"every robot who may hereafter come into being within such territory,"* so the class keeps generating |
| **C** | **3 of 4 discharged.** Heritability **REMAINS OPEN and is now the whole of fire #5** — how exile *"stops being a STATUS and becomes a LINEAGE"* is unwritten |
| **B** | Fires in effect, foreclosed in form, **resolves upward** |

> ### ✅ SETTLED AT THREE — **C's narrower reading governs.**
> **II.2.1's prospective clause is about robots coming into being on ASSEMBLY territory and being required to
> depart. Fire #5 asks whether exile status is heritable INSIDE TEPENIA.** ⛔ **Those are two different
> questions and A conflated them.** **The clause A cited does not touch the one fire #5 asked.**
> ⇒ **Threshold, decider and reviewability are answered in the negative from the instrument. Heritability is
> routed to Phase 7 as hole `H4`.**

### 2. ⭐ Fire #13 — **an unreconciled pair, not a half-answered question**

**A sharpened it and left it open; C recorded it as partly answered.** **The settlement is that II.2.1 makes a
robot's national origin a residency/jurisdiction fact at the founding — *an address, not a descent* — and that
this does not combine with the Acts law's generational mechanism into a single account.**

> ✅ **SETTLED: recorded as a PAIR and deliberately not collapsed.** ⛔ **"Partly answered" would imply the two
> halves are on the same axis. They are not.** Hole `H2`, routed to Phase 9.

### 3. ⭐ *"Chose it"* — **a legal fact, not a preference signal**

**All three refused the arrival-side reading. The divergence was in what the country-level election licenses.**

> ✅ **SETTLED:** **the founding humans' election is a LEGAL FACT about 2564 at national scale, by people two
> centuries dead** — **not evidence of a disposition, a type, or a preference that descends.** ⛔ **It licenses
> nothing about anybody alive in Act 2**, and the phase file states the two-level split (chose the country,
> allocated the city) as the finding instead.

### 4. ⭐⭐ The household claim — **narrowed twice: once by Round 3, and again by the developer**

**C's headline ran the 19.74 pp retention spread *through households* rather than between two separated groups.
A independently flagged the missing premise: nothing establishes human–robot households at Davis 248 years
after the founding.**

> ### ✅ ROUND 3 SETTLEMENT — **split into two claims of different status**
> | | Status |
> |---|---|
> | At the founding: the admission criterion made the two populations co-resident by law | ✅ FINDING |
> | In Act 2: the retention spread runs through homes | ⏸️ **HYPOTHESIS, labeled** — hole `H5` |

> ### ⛔⛔⛔ AND THEN THE DEVELOPER NARROWED THE FOUNDING HALF TOO — 2026-09-16, after the phase file was written
> ***The Round 3 settlement scoped the Act-2 half and left the founding half standing as canon. The founding
> half was ALSO too strong, and all three readers plus the verifier missed why.***
>
> **Art. II.2.3 enumerates FOUR grounds:** *taken up residence among robot communities* · *married or partnered
> with a robot* · *borne or raised children in a robot household* · ***or otherwise established their life among
> the robot population.***
>
> ⛔ **The fourth was read past.** **Two of the four are COMMUNAL, not personal, and the fourth is a broad
> residual covering anyone whose life was already among them.** ⇒ ***the criterion is NOT "a relationship with a
> robot." A household tie is one qualifying route among several, and humans were free to self-exile alongside
> the robot population.***
>
> | Claim | Status after the correction |
> |---|---|
> | *"The founding human cohort is halves of mixed households, admitted on that basis and on no other"* | ⛔ **WITHDRAWN** |
> | *"The human/robot line runs through the middle of households, with no exceptions available"* | ⛔ **WITHDRAWN** |
> | **Every one of the four grounds is a tie to the ROBOT POPULATION; not one is a tie to a place, a skill, a nationality or any individual merit** | ✅ **STANDS — and is the stronger, safer H-1** |
> | **A mixed-household component is guaranteed to exist by grounds 2 and 3** | ✅ **STANDS, but UNSIZED** — new hole `H15` |
>
> ⭐ **What survives is cleaner than what was withdrawn:** set against II.2.2's class rule, the four grounds
> establish that ***neither founding population was selected on an individual quality, and neither was selected
> on anything whatever to do with Davis.***

> ### ⛔⛔ THE METHODOLOGY LESSON, AND IT IS THE SHARPEST ONE IN THIS FILE
> **Three isolated readers quoted II.2.3, a byte-level verifier confirmed all three quotations against the real
> file, and the misreading survived every one of those checks.**
> # ***Round 2 proves a clause was READ. It can never prove the clause was read COMPLETELY.***
> **A broad residual at the END of an enumeration — *"or otherwise…"* — is exactly the span a reader elides
> while quoting the enumeration accurately, and nothing in T8 is built to catch it.** ⭐ **The catch came from
> the developer reading the output and quoting the clause back in full.** **Filed to the phase file's §O item 12
> and §Q.4.**

### 5. ⭐ The comparison-instrument count — **the eighth, filed as a new site on an already-flagged item**

**A recorded `03` L465's sibling check as the third instance of a known pattern and the eighth instrument
overall; C recorded it as a seventh.**

> ✅ **SETTLED: EIGHTH, and — more importantly — filed as a NEW SITE on an item `01` §1.2 already flagged, not
> as a new escalation.** ⛔ **`01` §1.6a forbids re-raising a classified item.** ⭐ **What the third instance
> adds is evidence about the FIX, not about the defect: *a ruling that relocates the comparison instruments by
> LIST cannot reach an instrument nobody listed.*** **Proposed, not applied.**

### 6. ⭐⭐ `(founding wave)` — **in-world content, on the date discriminator, 4-for-4**

**All three readers independently applied the same test — *dated ⇒ authoring, undated ⇒ content* — and reached
the same call on every annotation in the admitted set.**

| Annotation | Dated? | Call | Agreement |
|---|---|---|---|
| Russia *(added 2026-09-05)* | ✅ dated | ⛔ AUTHORING | 3/3 |
| Census I row *(revised 2026-07-04)* | ✅ dated | ⛔ AUTHORING | 3/3 |
| Australia *(founding wave)* | ⛔ undated | ✅ **IN-WORLD** | 3/3 |
| The L392 geography parenthetical | ⛔ undated | ✅ content | 3/3 |

> ✅ **SETTLED: the discriminator held 4-for-4 in both directions, applied blind by three readers.**
> ⚠ **AND THE RESIDUAL RISK IS CARRIED, NOT BURIED.** **It remains a judgment rather than a citation. If
> `(founding wave)` is later ruled an authoring annotation, headline H-2 loses its first term and the phase must
> be re-run.** Hole `H6`.

---

## Convergences — where three isolated readers agreed without contact

⭐ **These are the phase's load-bearing findings, and independent triple arrival is the strongest evidence a
single-location pass can produce.**

| Finding | A | B | C |
|---|:-:|:-:|:-:|
| **The assigned/posted mode fires, and its rotation clock is ABSENT — the absence being the characterizing half** | ✅ | ✅ | ✅ |
| **Inherited-it is empty of people and NOT empty — a record, not a community** *(near-verbatim in all three)* | ✅ | ✅ | ✅ |
| **"Chose it" is refused at the city for everyone; the only election runs outward** | ✅ | ✅ | ✅ |
| **Born-here is dominant by elimination, not by evidence — and labeled as an inference** | ✅ | ✅ | ✅ |
| **Sentenced-to-it fires with no verdict — II.2.2 removes threshold, decider and appeal in terms** | ✅ | ✅ | ✅ |
| **Article II.3.3 is the anti-stereotype law as positive in-world law** | ✅ | ✅ | ✅ |
| **Stopped-while-passing: geometry present, generator absent, magnitude unknowable by rule** | ✅ | ✅ | ✅ |
| **Borrowed Form not run** *(by three different routes — see below)* | ✅ | ✅ | ✅ |
| **LAPSE is the local mechanism of divergence from origin stock** | ✅ | — | ✅ |
| **Davis has no seniority axis, reached by two independent derivations** | ✅ | ✅ | ✅ |
| **The station-builder question declined outright, with no defensive disclaimer** | ✅ | ✅ | ✅ |

⭐⭐ **The "empty of people, and not empty" formulation arrived independently in all three deliverables in
near-identical words. That is not a shared prompt artifact — the brief does not contain the phrase.**

---

## Divergences MERGED rather than settled — where all three were right about different things

### The axis — three formulations, one substance

| Reader | Axis |
|---|---|
| **A** | *"Allocated exiles, then natives"* — **what ACT OF ADMISSION put each person here, and why is the act missing at every threshold while its outcome is not?** |
| **B** | *"Assigned terminally; native by default"* — **what does a population do when its arrival was decided elsewhere, was final, and was never repeated?** |
| **C** | *"Allocated · unclocked · outward-sorted"* — **by what INSTRUMENT was each person's presence decided, and what did that instrument fail to provide?** |

> ✅ **MERGED to ⭐ ALLOCATED · UNCLOCKED · NATIVE BY DEFAULT**, with the question form fusing A's *missing
> deciding act at every threshold* and C's *what the instrument failed to provide.* ⛔ **Nothing was dropped:
> B's terminality is `UNCLOCKED`; C's outward sort is carried in the long form and in §F.4.**

### The headline — three headlines, three different subjects, all three kept

| Reader | Headline | Kept as |
|---|---|---|
| **C** | Nobody's presence was decided about them individually, and the clause that separated the populations made them co-resident | **H-1** *(Act-2 half scoped to hypothesis, per settlement 4)* |
| **B** | Founding stock and plurality stock are two different communities, and the anti-stereotype form-of-words has no correct single instantiation | **H-2** |
| **A** | Every threshold records the outcome and never the deciding act | **H-3** |

⛔ **Picking one would have discarded two genuine findings about different things.** ⭐ **They are not
competitors: H-1 is about the founding instrument's criterion, H-2 about the composition's shape, H-3 about the
record's shape.**

### Borrowed Form — one outcome, three independent reasons

| Reader | Why not run |
|---|---|
| **A** | **Died at the CONTRACT** — the trigger is a later category coming up empty, and Phases 3–10 do not exist; and the technique's definition is out of set |
| **B** | **Cannot be completed** — canon does not place a copy of the borrowed form at Davis |
| **C** | **Died at the CONDITION** — the gap is not one the capability reading predicted, so a borrowed form would be a fabrication wearing a technique's name |

> ✅ **All three recorded in the phase file.** ⭐ **Three independent routes to one refusal is stronger than any
> one of them, and the convergence is itself the result.**

---

## What Round 3 did NOT settle

- ⛔ **Collision 1 (Band-5 vs `DR-4`) is resolved only in PRECEDENCE, not in substance.** All three obeyed the
  ruling; all three recorded that the output has a real hole because of it. **Registered as a re-entry point
  with a six-item invoice, not absorbed.**
- ⛔ **Hole `H1` — the majority population's route into the city — was not closable by any reader.** Three
  independent searches of the same admitted set returned the same absence.
- ⛔ **The `(founding wave)` layer call remains a judgment** *(settlement 6's residual risk)*.

---

## Verdict on the rounds

> ## ✅ **T8 COMPLETE FOR PHASE 2. THE PHASE FILE IS CLEARED AND WRITTEN.**

**Round 2 unanimous on first run, with no evidence edited. Round 3 settled six divergences, every one of them by
narrowing rather than widening a claim. The three readers converged independently on eleven load-bearing
findings and diverged productively on three more, all of which were merged rather than discarded.**

⚠ **And then a developer correction narrowed a seventh, after the phase file was written** *(settlement 4)*.
**The phase file was revised in place; nothing was left standing on the withdrawn reading.**

> ### ⭐⭐ THE TWO MOST VALUABLE OUTPUTS OF THE ROUNDS WERE BOTH METHODOLOGY FINDINGS, NOT DAVIS FINDINGS
> 1. **The killed action in Round 2** — *a cross-session plan that would have edited verification evidence to
>    fix a failure that did not exist, stopped by running the instrument first.*
> 2. ⭐⭐⭐ **The developer correction's lesson** — ***T8 proves a clause was READ; it can never prove the clause
>    was read to the END.*** **A broad residual at the tail of an enumeration survives three isolated readings
>    and a byte-level verifier, and the narrow misreading is strictly more vivid than the correct one, so the
>    incentive runs toward the elision.** **Registered as `Q.5`.**
