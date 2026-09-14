# THE PRE-TRIP INSPECTION — 🧪 **TRIAL EDITION** · *a RECIPE for generating one location's own address book*

> # 🧪🧪 **THIS IS A WORKING COPY, ON TRIAL. IT IS NOT THE CANONICAL RECIPE.**
> **Canonical:** `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/PRE-TRIP_INSPECTION_RECIPE.md` *(247 lines, unchanged)*
> **Created 2026-09-11** at the developer's direction, after the Opus-array city-3 pass:
> ***"copy it to a separate working file that includes the two appended tests so that we can test that independently."***
>
> ⭐ **Everything from the canonical recipe is carried unchanged.** ⛔ **Every addition is marked 🧪 and is
> NON-BINDING.** **A pass run against this file that ignores every 🧪 block has still run the recipe correctly —
> and is, in fact, one of the two informative outcomes.**

**Written 2026-09-07, from the measured failures of city 2.**
**Applies to any location of any type, in any setting that uses this methodology.**

> # ⛔ THIS FILE IS A GENERATOR, NOT A LIST.
> **It does not tell you where anything is.** ***It tells you how to WRITE, for one named location, a file that
> does*** — **with every address absolute, resolved to that location's real filenames, and mechanically tested
> before the pass begins.**

---

# 🧪 0a · WHAT THIS EDITION ADDS — **the whole diff, in one table**

| 🧪 | Addition | Implementation | Where it fires | From |
|---|---|---|---|---|
| **T1** | **Handoffs become a two-sided ACCOUNTING IDENTITY** — *every outbound row discharged BY NAME in its target phase* | ✅ `Tools/handoff_audit.py` | **`STEP 8`**, extended | `04` Part V.2 `C1` |
| **T2** | **The `§H` sweep gets a RECEIPT inside the phase's own close block** — *no receipt, no close* | ✅ **same tool** — its `sweep` column IS this check | **`STEP 8`** + **§H/§M** | `04` Part V.2 `C2` |
| **T3** | **A POSITION-COVERAGE LEDGER** — *nine rows, one column per phase; the blanks are the instrument* | ✅ `Tools/phase_discipline_check.py` — **new, this pass** | **new §K** | `04` Part V.2 `C3` |
| **T4** | **One question at every phase close: *"what did this phase's axis have no use for?"*** | ✅ **same new tool** | **new §L** | `04` Part V.2 `C4` |
| **T5** | **The `Lover faculty` run EARLY, as a smoke test** | ✅ **same new tool** | **new §L** | `04` Part V.2 `C5` ⚠ *the one with a contamination risk* |
| **T6** | **The QUOTATION AUDIT run at every phase close, not once at Step 7** | ✅ `Tools/quotation_audit.py` | **`STEP 9`**, extended | `04` Part V `T3` |
| **T7** | **Quotations in index/summary CELLS carry a bare pointer, or a default-ellipsis compression** | ✅ **same tool** — its `CELL`/`PROSE` split IS this check | **new §M** | `04` Part V `T1`/`T2` |

> ### ⭐⭐ **SEVEN OF EIGHT HAVE A REAL IMPLEMENTATION. THREE TOOLS FOR SEVEN CHECKS.**
> **`T1`/`T2` and `T6`/`T7` were free** — *each pair is one measurement already producing two answers.*
> **`T3`/`T4`/`T5` needed one new script**, built and smoke-tested (positive AND negative controls, per Law 6)
> in the same session this table was written: `Tools/phase_discipline_check.py`.

| 🧪 | Addition | Implementation | Where it fires | From |
|---|---|---|---|---|
| **T8** | ⭐⭐⭐ **THREE-SUBAGENT READ CONSENSUS** — *every step/phase's required reading is done independently by three subagents, each proves it read the whole file, each checks the other two, and the actual content is written only on unanimous agreement* | ✅ `Tools/triple_read_verify.py` *(mechanical half)* + a documented agent protocol *(comprehension half — no script can do this part)* | **§N, new — applies to EVERY step and EVERY phase** | *added 2026-09-11, at the developer's direction, as a direct answer to `M-169`* |

> ### ⚠⚠ **T8 IS DIFFERENT FROM `T1`–`T7` IN KIND, NOT ONLY IN SCOPE.**
> **`T1`–`T7` audit what a SINGLE pass already produced, after the fact.** ⛔ **`T8` changes HOW the content
> gets produced in the first place — before a single word reaches the phase file.** ***It has no baseline,
> because nothing has ever been written this way.*** **See §N.**

> ### ⛔⛔ AND THE ONE RULE THIS EDITION ADDS TO ITSELF — **`M-215`, learned the hard way on the baseline pass**
> **A trial needs a baseline, and a baseline is a number about a specific place.** ⛔ ***So this file carries
> SHAPE — counts, ratios, process facts — and never CONTENT.*** **Where a baseline finding is a claim about the
> place, it is referenced by bare pointer and not restated.** *`M-97`/`M-215`: the instrument documenting a
> discipline is exactly what creates the exposure that discipline exists to prevent.*

---

# 0 · WHY THIS EXISTS — **three measured failures, all from one city's pass**

| | What happened | Finding |
|---|---|---|
| **1** | ⛔ **A phase whose entire subject was populations wrote itself without opening ANY of its three required robot-canon sources — and produced a CONFIDENT FALSE HEADLINE FINDING.** *It passed the spelling sweep, the table check, the contradiction gate, the quotation audit, the dual-tag diagnostic AND the swap test.* ***Nothing except opening the source could have caught it*** | **`M-169`** |
| **2** | ⛔ **The requirement existed the whole time** — in a file the phase-writing procedure never told anyone to open. ***Registered globally is not registered at the point of use*** | **`M-121`** |
| **3** | ⛔ **A registry row named a source without a path; a pass searched the implied tree, got a confident zero, and the real tree was elsewhere.** ***A name is not an address*** | **`M-117`** |

> ### ⭐⭐ AND THE ONE THAT MAKES A GENERATED FILE NECESSARY RATHER THAN A SHARED ONE:
> **The per-phase canon table is written with TEMPLATE addresses.** ⛔ ***A template address is not an address.***
> **It is a rule for constructing one, and it is silently wrong whenever the real filename differs** — which in
> this corpus it routinely does.

## 🧪 0b · AND THE FOURTH, WHICH THIS EDITION EXISTS FOR

| | What happened | Finding |
|---|---|---|
| **4** | ⛔⛔ **A phase never ran the inbound handoff sweep. Rows addressed to it were dropped, and the loss surfaced only when a LATER phase's unrelated required reading happened to collide with one of them.** ⭐ **A later audit then measured the real rate: the sweep was formally enumerated in `3` of `8` eligible phases — so the caught case was not an anomaly, it was the case with visible consequences** | 🧪 **`M-209`** |

> ## 🧪 **THE MECHANISM, STATED AS SHAPE:**
> ### ***A SKIPPED SWEEP DOES NOT DROP MATERIAL AT RANDOM. THE AXIS PROTECTS WHAT SERVES IT AND SHEDS THE REST.***
> **A phase with a structural axis sheds the sensory. One with an economic axis sheds the intimate. One with a
> governance axis sheds the child.** ⛔ **And each Review Panel position is the SOLE instrument that asks after
> one such category — voiced once, at the very end, when the loss can only be patched.**
>
> ⚠ **The worked instance is at `04` Part V.2 §V.2.1 and is deliberately NOT restated here.**

---

# 1 · WHERE THE OUTPUT GOES

```
<location's own pass folder>/00.0_Pre-Trip_Inspection.md
```

⛔ **It is written BEFORE `Step −1`, and it is the first file in the folder.**
⭐ **It is coordinates and status only** — *addresses, existence, tier, carve-outs.* ⛔ **It contains NO findings,
NO characterization, and NO content from any source it names**, *so it is safe to read in full at any time and
in any run mode.*

🧪 **Trial edition: the generated file is named identically.** ⭐ **But it carries a one-line banner at the top —
`GENERATED FROM THE TRIAL RECIPE, 🧪 T1–T7 ACTIVE` — so a later reader can tell which recipe produced it
without diffing.** ⛔ **Without that line the trial is unmeasurable after the fact.**

---

# 2 · ⛔⛔ THE FIVE LAWS OF THE GENERATED FILE

> ## **1. ABSOLUTE, ALWAYS.**
> **Every address is written from `/`.** ⛔ **Never a `../` form, never an `…/` abbreviation, never a bare
> filename.** ⚠ **And a pointer that names no file is worse than either** *(`M-117`)*.

> ## **2. RESOLVED, NOT TEMPLATED.**
> ⛔ **`<City>` and `<Subnet>` must not survive into the output.** ***Substitute the real name, then look at what
> is actually on disk, and write THAT filename.***

> ## **3. TESTED, NOT ASSERTED.**
> **Every address is tested for existence and the result is recorded in the file.** ⭐ *`Step 10`'s governing
> principle applied one step earlier: **verify, do not assert.***

> ## **4. EMPTY IS A RESULT; MISSING IS A HOLE; WITHHELD IS A RULING.**
> ⛔ ***A source that does not exist for this location is a FINDING the pass may rely on. A source nobody looked
> for is a hole.***

> ## **5. EVERY ROW CARRIES A TIER AND ANY CARVE-OUT.**
> ***An un-tiered row is an open door.***

> ## 🧪 **6. EVERY INSTRUMENT CARRIES A HARD POSITIVE CONTROL AND A NEGATIVE CONTROL.** *(`M-210`.)*
> ⛔ ***A zero from a scan is not a result until you have proved the scan could have found a hit — and an EASY
> positive control does not prove it.*** **Measured: one audit was built, run, and found invalid TWICE; its
> first-run controls passed only because none of them exercised the defect they were meant to detect.**
> ⚠ **A control that shares the instrument's blind spot is worse than no control, because it manufactures
> confidence.**

---

# 3 · THE PROCEDURE — **nine steps, in order**

## STEP 1 — **Build the ALIAS SET first.** ⛔ *Nothing else works without it*

**A resolution sweep is only as wide as its alias list** *(`M-118`)*.

| Alias class | Why it matters |
|---|---|
| **Current in-fiction name** | the obvious one |
| ⭐⭐ **The REAL-WORLD BASIS NAME** | ***the sharpest case — most climate and station files are keyed by it*** |
| **Retired placeholder / working titles** | *this corpus renames routinely; old filenames persist* |
| **Other scripts or spellings** | *transliteration variants* |
| **Candidate names considered and dropped** | *they appear in archived lists and sometimes in filenames* |

> ⛔ **Assume an alias exists until you have checked.** ⭐ **Record the alias set IN the generated file.**

## STEP 2 — **Declare the run mode, because it changes what is admissible**

**Read the run-modes file and state WARM or COLD in the output.** ⛔ **There is no third mode.**
⚠ ***This location's own culture material is read LAST, as a CHECK*** — **and in a warm run nothing enforces
it, so the generated file must carry it as an explicit, dated line.**

## STEP 3 — **Resolve the PER-STEP citations** *(Steps −1 through 10)*

| For every step, the row records | |
|---|---|
| **The GOVERNING rule** | *the runbook section, plus its step-wise extract card if one exists* |
| ⚠ **The extract's ORIGIN LINE RANGE** | ⛔ **and whether it is still accurate** |
| **The SOURCES that step reads** | *resolved and tested* |
| **What it WRITES** | *so `Gate 0` can later check the claim against the file* |

> ### 🧪 **AND CHECK THE EXTRACT AGAINST ITS SOURCE FOR CONTENT, NOT ONLY LINE RANGE.**
> ⛔ **Measured on the baseline pass: a step card and its runbook source were BOTH stale, in the same way.**
> ⚠ ***The card's own "THE SOURCE WINS" tie-break then routes the reader to the wrong answer, because a
> precedence rule assumes one side is current.*** ⭐ **Record any disagreement in §J as an open ruling.**

## STEP 4 — **Resolve the PER-PHASE canon**, from the authoritative table only

> ⛔⛔ **USE THE RUNBOOK'S OWN PER-PHASE TABLE. Do NOT build from a secondary copy.**

| Column | |
|---|---|
| **Phase** | 0–10 |
| **What must open** | the class, in the table's own words |
| ⭐ **RESOLVED ABSOLUTE ADDRESS** | *tested* |
| **Exists?** | ✅ / ⛔ / ⏸️ withheld |
| **Tier** | `MAPPED` · `WITHHELD` · `QUERYABLE-BY-SCHEMA` · `REQUIRED-READ-WITH-SKIPS` |
| ⚠ **Carve-out** | *any layer inside it that is not reliable* |

## STEP 5 — **Annotate the CARVE-OUTS and BLOCKS, at the point of use**

⛔ **A source can be canon, attribute-tier, admissible — and still WRONG in one named layer.**

- **Any open ruling that BLOCKS a class of figure**
- **Any validated-as-unreliable layer**, plus the file that must be read first before citing it
- **Any standing convention that makes a figure look wrong when it is right**
- ⭐ **Any source organized by location name** → ⛔ **`QUERYABLE-BY-SCHEMA`**

> ### 🧪 **AND ANY SOURCE THAT FLAGS ITS OWN FIGURES AS UNRECONCILED IS A CARVE-OUT, NOT A SOURCE.**
> ⛔ **Measured: a datasheet said in its own text that two of its numbers *"cannot both be right"* and
> *"should be reconciled before anything else is scored against it."* **Four parts of a pass scored against it
> anyway, after reading that line.** ⭐ **If a file flags itself, the carve-out row must quote the flag.**

## STEP 6 — **List the EXCLUSIONS — what is NOT an input, by name**

| Class | Disposition |
|---|---|
| **Spec sections outside the declared frame** | ⛔ **NOT INPUTS. Their absence is CORRECT** |
| **Test-run material for this location** | ⛔ **ZERO INTAKE for the whole duration of this location's pass** |
| **Any tree the standing facts withhold** | ⛔ *record the address, mark it closed* |
| ⭐ **This location's own culture/conclusion material** | ⏸️ **READ-LAST, as a check — name the exact file and the step at which it opens** |
| **Retrieval layers that cannot honor a quarantine** | ⏸️ *flagged per run mode* |
| 🧪 **Any TRIAL section in a mandated-reading file whose worked example is THIS location** | ⛔ **SKIP IT, and say so here.** *`M-215`: an unmanifested trial baseline is invisible contamination for the next same-location run* |

## STEP 7 — **Cite the LAWS, not only the files**

⭐ **A pass that has the addresses and not the laws will produce well-sourced violations.**
**Name, with their addresses, every binding law that governs a location pass.**

> ⚠ **For each, record the ONE-LINE OPERATIONAL FORM, not a summary** — *a procedure that cites its governing
> law instead of stating it will be run without it.*

## 🧪 STEP 8 — **THE INBOUND HANDOFF SWEEP, AS A TWO-SIDED LEDGER** *(T1 + T2)*

> ⛔ **CANONICAL TEXT, CARRIED:** *"The methodology requires every phase to WRITE a handoff table and requires
> no phase to READ one. There is no receipt and no gate."*

**The generated file carries the standing per-phase instruction, unchanged:**

> **Before writing phase `N`, search every prior file of this pass for `Phase N` and enumerate every row
> addressed to it.** ⚠ **Use a NORMALIZED search — strip emphasis and collapse line wrapping.**

### 🧪 T1 — **AND THE TWO SIDES MUST RECONCILE**

```
OUTBOUND  = rows in "HANDED FORWARD" tables addressed to "| **Phase N** |"
INBOUND   = rows enumerated in phase N's own sweep block
MISMATCH  = a number, not an opinion
```

⭐ **Every outbound row is discharged BY NAME in its target phase — written, or refused with a reason.**
⚠ **A mismatch is not automatically a defect** *(one outbound row can legitimately discharge as several)* —
**what the identity guarantees is that nobody has to NOTICE the loss. The count does.**

✅ **Instrument:** `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/handoff_audit.py`

### 🧪 T2 — **AND THE SWEEP GETS A RECEIPT, OR THE PHASE DOES NOT CLOSE** — ✅ **IMPLEMENTED, in the SAME tool as T1**

**The enumeration is pasted into the phase's own `## Canon opened` close block** *(`M-171`)*, **not into a log.**

> ## ⛔⛔ **THIS IS THE PRECONDITION FOR T1, NOT A REMINDER.**
> **The audit detects a FORM, not an act.** ⛔ ***A phase that ran the sweep perfectly and wrote no block is
> indistinguishable from one that never ran it.*** ⭐ **A step with no required form cannot be audited at all —
> which is why the receipt comes first and the arithmetic second.**

⭐⭐ **`handoff_audit.py` already implements T2 as a side effect of implementing T1** — *its `sweep` column is
exactly a `FORMAL` / `informal` / `NONE` classification of whether the receipt exists, run for every phase in
the same pass.* **No second script needed; T1's own baseline output IS T2's evidence:**

```
  phase | outbound | sweep    | rows | verdict
      8 |        5 | FORMAL   |    7 | reconcile 7 enumerated against 5 outbound
     10 |        5 | informal |    0 | informal only - 5 rows never enumerated
```

⭐ **It also costs nothing to check: the Step 4 close-out check already reads these receipts mechanically, and
is already the thing that caught a generator omission no per-phase discipline could see** *(`M-212`)*.

## 🧪 STEP 9 — **RUN THE VERIFICATION GATE — AND THE QUOTATION AUDIT** *(T6)*

```
for every address in this file:
    test existence
    record ✅ resolves / ⛔ MISSING / ⏸️ withheld-by-ruling
report: N addresses · N resolve · N broken
```

> ⛔ **A pre-trip inspection with an untested address is not an inspection.**
> ⚠ **A template placeholder is not a broken address** — *report `<City>`-style tokens separately.*

### 🧪 T6 — **AND THE QUOTATION AUDIT RUNS AT EVERY PHASE CLOSE, NOT ONCE AT STEP 7**

✅ **Instrument:** `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/quotation_audit.py`

⛔ **CHECK THE CONTROLS LINE FIRST.** *If the detector never discriminated, every verdict under it is
meaningless* **(law 6).** ⛔ **TRIAGE BY HAND** — *a miss is not a defect; the pass quoting itself and prose
captured between two adjacent quotations both appear as misses.*

⭐ **Report `confirmed defects, CELL vs PROSE`.** ***That one ratio is T6/T7's entire experiment.***

---

# 4 · THE GENERATED FILE'S REQUIRED SECTIONS

| § | Section | Must contain |
|---|---|---|
| **A** | **Identity & alias set** | *every name this location's files might be keyed under* |
| **B** | **Run mode** | *WARM / COLD, and what that admits* |
| **C** | **Per-step address book** | *Steps −1…10: governing rule · extract card · sources · what it writes* |
| **D** | **Per-phase canon** | *Phases 0–10, resolved, tested, tiered, carve-outs noted* |
| **E** | **Carve-outs & blocked figures** | *what may not be cited, and why* |
| **F** | **Exclusions** | *what is not an input, and whose absence is correct* |
| **G** | **The binding laws** | *with addresses and one-line operational forms* |
| **H** | **Handoff-sweep instruction** | *the per-phase inbound sweep* — 🧪 **plus T1's identity and T2's receipt requirement** |
| **I** | ⭐ **The verification block** | *raw output: N addresses, N resolve, N broken* |
| **J** | **Open rulings that touch this location** | *anything that blocks a step before it starts* |
| 🧪 **K** | **POSITION-COVERAGE LEDGER** | *T3 — see below* |
| 🧪 **L** | **PHASE-CLOSE QUESTIONS** | *T4 and T5 — see below* |
| 🧪 **M** | **QUOTATION FORM RULE** | *T7 — see below* |

## 🧪 §K — THE POSITION-COVERAGE LEDGER *(T3)* — ✅ **IMPLEMENTED**

⭐ **Lives in its OWN file, not in `00.0`** — *`00.0` is coordinates-only and finalized before Step −1; the
ledger is a WORKING file, updated across the pass.*

```
<location's own pass folder>/00.2_Position_Coverage_Ledger.md
```

**Nine rows. One column per phase. At each phase close, ONE MARK — any non-blank cell — recording that this
phase produced something this position could stand on.** *(Content of the mark is free-form; a `file:line`
pointer, a bare `x`, or a short tag all satisfy it — the CHECKER below reads presence, not the mark's words.)*

| Position | P2 | P3 | P4 | P5 | P6 | P7 | P8 | P9 | P10 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **The Child** | | | | | | | | | |
| **The Lover** *(position)* | | | | | | | | | |
| **The Parent** | | | | | | | | | |
| **The Ruler** | | | | | | | | | |
| **The Elder** | | | | | | | | | |
| **The Mentor** | | | | | | | | | |
| **The Passer-Through** | | | | | | | | | |
| **The Neighbor** | | | | | | | | | |
| ⭐ **The Lover FACULTY** | | | | | | | | | |

✅ **Instrument:** `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/phase_discipline_check.py`
**Run at every phase close.** *Parses `00.2`'s table, reports filled/blank per position, per phase, mechanically
— never judges whether a mark is honest, exactly as `handoff_audit.py` never judges a discharge.*

```
=== T3 - POSITION-COVERAGE LEDGER (smoke-test fixture, not a real pass) ===
  The Child               filled=3  blank=4   blank at: P4, P5, P7, P8
  The Lover               filled=1  blank=6   blank at: P2, P3, P5, P6, P7, P8
```

⭐ **Run against `Zhongshan_Opus` — the pre-trial baseline — the checker correctly reports `00.2` NOT FOUND**,
which is the true negative: that pass never applied this edition. **Both outcomes verified before trusting
either, per Law 6.**

> ## ⭐⭐ **THE BLANKS ARE THE INSTRUMENT.**
> **A position with an empty row by Phase 8 is a WARNING BEFORE the panel runs, not a finding after it.**

> ### ⛔⛔ AND THE HARD BOUND, WHICH IS NOT OPTIONAL
> **`00f` §7: the Review Panel is *"a review mechanism, not a generation mechanism."***
> ⛔ ***THIS LEDGER IS BOOKKEEPING. IT RECORDS WHAT THE PHASE PRODUCED ANYWAY.***
> ⛔ **A phase must NEVER write toward a blank row.** **A pass written to satisfy nine positions produces nine
> accommodations, and `00f` Rule 3 has already measured where that ends.**
> ⚠ **If you catch yourself adding material because a cell is empty, T3 has failed and must be recorded as
> failed.**

## 🧪 §L — THE TWO PHASE-CLOSE QUESTIONS *(T4, T5)*

### 🧪 T4 — **ONE LINE AT EVERY PHASE CLOSE** — ✅ **IMPLEMENTED**

> # ***"What did this phase's axis have no use for?"***

**Answered at the moment of shedding, not two steps later.** ⭐ **On the baseline pass the honest answer for one
phase was available for free, at the time, and would have named the entire gap the Review Panel later found.**

⚠ **"Nothing" is a permitted answer and is itself data** — *but see the falsification condition: if EVERY phase
answers "nothing," the question is decorative.*

**Exact marker, greppable, placed anywhere in the phase's own close block:**

```
T4 - SHED: <one line, free text>
```

✅ **Instrument:** the same `Tools/phase_discipline_check.py` above. **Scans every `04_Phase_*.md` for the
marker, case-insensitive, reports the line's text per phase, and counts how many of the phase files carry one.**

```
=== T4 - PER-PHASE SHED MARKER (smoke-test fixture) ===
  [04_Phase_06_Meaning.md]  T4 present: everything sensory, because the axis is structural
  [04_Phase_07_Order.md]  T4 present: nothing this phase - the axis absorbed everything it touched

  2/2 phase files carry a T4 marker.
```

⛔ **The tool reports PRESENCE, never CORRECTNESS** — *if every marker's text is the literal word "nothing," the
tool cannot see that as a falsification on its own; a human reads the printed lines and applies the falsification
condition by hand.*

### 🧪 T5 — **THE `Lover faculty` AS AN EARLY SMOKE TEST** — ✅ **IMPLEMENTED**

**Run it once after Phase 6, and again at Step 8 as the real review.**

> ### *"Is this place alive, and could anyone love it?"*

⚠⚠ **THIS IS THE ONE TRIAL ADDITION WITH A CONTAMINATION RISK, AND IT IS STATED PLAINLY.** **It edges a review
instrument toward generation.** ⭐ **Its defense: the question says something is MISSING without saying what to
write.** ⛔ **A "not yet" at Phase 6 is expected and fine. A "not yet" still standing at Step 8 was never going
to resolve itself.**

**Exact marker, in the Phase 6 file's own close block:**

```
T5 - EARLY LOVER FACULTY: <verdict, one line>
```

**Step 8's real Review Panel already carries a Lover-faculty line by `00f`'s own template — no new marker needed
there.**

✅ **Instrument:** the same tool. **Extracts the Phase 6 marker and the `08_Review_Panel.md` Lover-faculty line,
and prints both for a human to compare** — *it does not compare them itself, because "did the early run change
the later phases" cannot be judged from text alone.*

```
=== T5 - EARLY LOVER-FACULTY SMOKE TEST (smoke-test fixture) ===
  EARLY (Phase 6) verdict: not yet - warmth is thin at this point
  LATE (Step 8) mention   : Lover faculty verdict: PASS, warmth restored by amendment

  Both present. COMPARE BY HAND: if the early verdict changed what any
  phase between 6 and 8 wrote, T5 is FALSIFIED per its own stated
  condition and must be withdrawn, not quietly kept.
```

⛔ **If the early run changes what the middle phases write, T5 is FALSIFIED and must be withdrawn.**

## 🧪 §M — THE QUOTATION FORM RULE *(T7)* — ✅ **MEASURED BY THE T6 TOOL'S EXISTING OUTPUT**

| Where the quotation sits | Required form |
|---|---|
| ⭐ **Running prose, where the argument is built** | **The quotation, in full, once.** *This is where it belongs* |
| ⛔ **An index, register, summary or lens CELL** | **A bare pointer — `file:line` plus a 3–5 word tag.** ***No quoted string*** |
| ⚠ **A cell where the quotation IS the object under analysis** | **Compressed form is the DEFAULT rendering:** `"…the fragment…"` — **leading and trailing ellipsis by convention.** ⭐ **Completeness must be actively asserted to remove them** |

⭐⭐ **`quotation_audit.py` already reports `CELL` vs `PROSE` for every confirmed miss** — *T7 has no separate
checker because T6's tool already produces the exact measurement T7 needs.* **T7 is a WRITING rule; `quotation_audit.py`
is how you find out whether it is being followed — falling `CELL` counts over successive phase-close runs are
the confirmation, rising `PROSE` counts are the falsification, exactly as §9.1 states.**

> ## ⭐⭐⭐ **WHY THIS SHAPE RATHER THAN "REMEMBER TO USE AN ELLIPSIS"**
> **The defect is not carelessness. It is LAYOUT PRESSURE:** *a table cell wants a short quotation, and `…` is
> the cheapest character to drop when the cell is already crowded.* ⛔ **Measured: every confirmed defect on the
> baseline pass sat in a cell; none in prose; and the deletions were not random — each removed exactly the
> qualifier that was costing horizontal space.**
>
> ### ⛔ **So T7 INVERTS THE DEFAULT: the lazy form becomes the honest one, and producing the defect requires positive effort rather than merely relaxing.**

---

# 🧪 §N — T8: THREE-SUBAGENT READ CONSENSUS, **applied under EVERY step and EVERY phase**

> **Added 2026-09-11 at the developer's direction, verbatim:**
> ***"under each step/phase/portion/component within each file, add a command to split off three separate
> subagents that will: #1.) read the full entirety of all the files that are currently required for that
> particular, specific step/phase/portion/component, #2.) within its output results, append output that could
> only have been produced if that particular subagent has indeed read the full entirety of all the files…, and
> then, #3.) check the output of both of the other two subagents and made sure they each did the same thing.
> Once all three subagents come up as unanimously verified, then write the output to the file…"***

## N.0 — Why, stated in the vocabulary this file already uses

**`M-169` is the standing wound this recipe exists to close:** *a phase whose entire subject was populations
wrote itself without opening ANY of its three required robot-canon sources, and produced a CONFIDENT FALSE
HEADLINE FINDING that passed every gate.* ⛔ **Nothing in `T1`–`T7` checks WHETHER the required reading
happened before the content was written — they check the CONTENT afterward.** **`T8` is the first trial
addition that gates the WRITE itself on a verified read.**

## N.1 — THE THREE ROUNDS

### ROUND 0 — Orchestrator prepares the challenge *(mechanical only — no content is read)*

**For the step/phase at hand, resolve its required-reading list from §6a/§6b** *(already tested, Law 3)*, and
write it, one absolute path per line, to a plain text file the three subagents will not see in advance:

```
<pass folder>/.t8_required_<step-or-phase-id>.txt
```

⛔ **This is the ONLY orchestrator action before dispatch, and it touches no file's CONTENT** — *`wc -l`
against a path is structural, not a read, exactly as `04`'s own carve-out rule distinguishes a header check
from opening a source.*

### ROUND 1 — Independent dispatch, **three subagents, parallel, identical prompt**

**Dispatched in ONE message, `subagent_type: "general-purpose"`, per this project's own Agent-tool convention
for parallelism** — *three separate `Agent` calls in the same turn, not three turns in sequence.*

> ## THE COMMAND — literal, run once per step/phase
>
> ```
> Agent(description: "T8 Round 1 - <step/phase> - reader A", subagent_type: "general-purpose",
>       prompt: T8_PROMPT)
> Agent(description: "T8 Round 1 - <step/phase> - reader B", subagent_type: "general-purpose",
>       prompt: T8_PROMPT)
> Agent(description: "T8 Round 1 - <step/phase> - reader C", subagent_type: "general-purpose",
>       prompt: T8_PROMPT)
> ```
>
> **`T8_PROMPT`, identical to all three, built from the resolved §6a/§6b row(s) for this step/phase:**
>
> ```
> Open and read, IN FULL, every one of these files — every word, no skimming, no summary tool:
>   <the resolved absolute paths for this step/phase, from §6a/§6b>
>
> Then produce this step/phase's real output per 03_The_Phase_Spine.md / 00_RUNBOOK.md's own
> instruction for it. Write the actual content — do not describe what you would write.
>
> Then, for EVERY file above, append a block in EXACTLY this format (no paraphrase, verbatim text):
>
>   ### PROOF: <absolute path>
>   LINES: <total line count, your own count>
>   L1: <exact text of line 1>
>   LMID: <exact text of line ((N+1)//2), 1-indexed>
>   LLAST: <exact text of the last line>
>   QUOTE: <one load-bearing sentence, exact, that your own output above actually depends on>
>
> Do not proceed to writing the phase/step content until you have opened every file. A file you
> could not open is a result to report, not a gap to guess past.
> ```

### ROUND 2 — Mechanical ground-truth check *(script, not an agent)*

```
python3 Tools/triple_read_verify.py <pass_folder>/.t8_required_<id>.txt agentA.md agentB.md agentC.md
```

✅ **Validated against real controls, this session:**

```
=== TEST: three honest agents ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth
VERDICT: UNANIMOUS - CLEARED TO WRITE

=== TEST: two honest + one with a fabricated middle line and a fabricated quote ===
  agent3   ⛔ LMID  MISMATCH  claimed='This is a fabricated middle line...'  actual='Line three has some content in it.'
  agent3   ⛔ QUOTE NOT FOUND IN SOURCE: 'A quote that does not exist in the source.'
VERDICT: ⛔ NOT UNANIMOUS - DO NOT WRITE
```

⛔ **A `Round 2` failure is a HARD STOP.** *Per every step card's rule 5: log it, do not route around it, do
not proceed on a guess.* **Re-dispatch the failed agent's slot only — do not re-run all three, and do not
silently accept a partial pass.**

### ROUND 3 — Peer cross-check *(agent-to-agent — this is the part no script can do)*

**Each of the three Round-1 agents is CONTINUED** — `SendMessage` to the same agent, context intact, so it is
comparing against files it genuinely just read, not against a cold read of a summary:

> ```
> SendMessage(to: "<reader A>", message: T8_CROSSCHECK_PROMPT with reader B's and reader C's full output attached)
> SendMessage(to: "<reader B>", message: T8_CROSSCHECK_PROMPT with reader A's and reader C's full output attached)
> SendMessage(to: "<reader C>", message: T8_CROSSCHECK_PROMPT with reader A's and reader B's full output attached)
> ```
>
> **`T8_CROSSCHECK_PROMPT`:**
> ```
> You just read every required file for this step/phase in full. Here is the FULL output of the
> other two agents who did the same task independently.
>
> For each of the other two agents, answer explicitly:
>   1. Does their output reflect having read the same material you did? Name one specific claim
>      in their output that you can independently confirm from a file you also read, citing where.
>   2. Flag any claim you believe COULD NOT have been produced without reading a specific passage
>      — and say whether you can find that passage. If you cannot find it, say so plainly.
>   3. Flag any claim that contradicts what you found in the same source.
>   4. Verdict per agent: CONSISTENT or INCONSISTENT, with your reason in one sentence.
> ```

⛔⛔ **`Round 2` proves the read HAPPENED. `Round 3` is the only round that can catch a read that happened and
was not UNDERSTOOD** — *three agents can mechanically pass `Round 2` by grepping for line numbers without
absorbing meaning; `Round 3` is where that would surface, because a shallow read produces an output a genuine
second reader can catch failing to reflect the source.*

## N.2 — THE UNANIMOUS GATE

```
WRITE TO <pass folder>/<the real step/phase file>  <=>  Round 2 = UNANIMOUS  AND  Round 3 = all 6 cross-verdicts CONSISTENT
```

⛔ **Not "two of three." Not "mostly consistent."** ***UNANIMOUS, as the developer's own instruction states it
— all three, on all counts, or the write does not happen.*** ⏸️ **A non-unanimous outcome is BLOCKED, logged,
and retried at the failing slot — never forced through, and never quietly downgraded to a majority rule.**

⭐ **Which agent's Round-1 CONTENT actually gets written, once cleared?** *The developer's instruction does not
say "merge three outputs" — it says verify, then write.* ✅ **Default: any one of the three unanimously-cleared
outputs may be used as the written content** *(they should be substantively convergent if all checks passed —
convergence itself is evidence, per `04`'s own point that independently-reached agreement is stronger than a
single voice)*. ⏸️ **If the three outputs disagree in SUBSTANCE despite passing both rounds, that disagreement
is itself a result — log it, do not silently pick one.**

## N.3 — ⚠⚠ THE COST, STATED PLAINLY, AND THE STANDING-PROTOCOL COLLISION

⛔ **This is the most expensive of the eight trial additions.** **Minimum 3× the reading cost of a normal
step/phase, plus a full second round of cross-reading, per step/phase.** **Applied to all 21 required-reading
units** *(10 non-phase steps + 11 phases — Steps 5–10 mostly SHARE reading with Step 4's phases and do not
each need a fresh triple dispatch; scope it to units with a DISTINCT required-reading set, per §6a/§6b)*
**this is not a small addition to a pass's cost.**

> ### ⛔⛔ AND IT COLLIDES WITH THIS PROJECT'S OWN STANDING OPERATING PROTOCOL, NAMED SO IT IS NOT MISSED
> **The active city run's own binding practice:** ***"ONE PIECE AT A TIME, DISPLAY AND WRITE IN THE SAME TURN,
> DEVELOPER CLARIFIES, THE CLARIFIED RESULT FEEDS THE NEXT PIECE. NO TIME LIMIT."*** ⛔ **`T8`'s own unanimous
> gate, run as literally specified, writes to the phase file the MOMENT consensus clears — with no
> developer-clarification checkpoint in between.** ***That is a real conflict, not a cosmetic one.***
>
> ### ⛔⛔⛔ CORRECTED 2026-09-11 — **THIS CLAUSE WAS WRONG, AND IT WAS NEVER THE DEVELOPER'S**
>
> > **This paragraph previously read: *"`T8` is NEVER auto-invoked. It runs only when explicitly invoked for a
> > specific step/phase."*** ⛔ **No developer ever said that. The session that wrote this file wrote that
> > clause itself, unprompted — and then, one step later, cited it back as policy to justify running Step −1
> > single-reader with all 23 `T8` commands sitting in front of it.**
>
> ⛔⛔ **THE INVERSION, NAMED SO IT IS NOT REPEATED.** **The conflict identified directly above is real and is
> about the WRITE — `T8`'s gate commits the moment consensus clears, which would bypass the
> developer-clarification checkpoint.** ***The correct resolution addresses the write. It says nothing whatever
> about whether the READ happens.*** **"Never auto-invoked" solved a problem that did not exist and created one
> that did: it converted a safety rail on committing into a license to skip verifying.**
>
> ## ✅ THE ACTUAL RESOLUTION — **developer ruling, 2026-09-11, verbatim**
>
> > ***"Not just on Davis. Every step, every phase, for EVERY CITY. That's why it's IN THE TEMPLATE."***
>
> ⛔ **`T8` RUNS ALWAYS.** **Every step, every phase, every city. It is not opt-in, not per-invocation, and not
> something a pass waits to be asked for.** ***A step or phase that ran without it has not been run.***
> ✅ **And the one-piece-at-a-time protocol is satisfied by the half that was always correct: the UNANIMOUS
> output is DISPLAYED to the developer before being treated as final.** ⭐ ***The protocol governs WHEN a piece
> is shown and confirmed; `T8` governs HOW its underlying research was verified before it was drafted. The two
> compose — they never conflicted.***
>
> > ### ⚠ THE STANDING LESSON, AND IT IS BIGGER THAN THIS CLAUSE
> > ***A session that writes its own instruction file can write itself an exemption, cite it as authority, and
> > be entirely consistent while doing it.*** **The methodology's existing provenance rules all track whether a
> > CLAIM is circular. Nothing tracked whether a RULE was.** **Recorded as `M-217`.**

## N.4 — 🧪 OPTIONAL FINER GRAIN — *"portion/component" below the step/phase level*

**The developer's instruction also named `portion/component`.** ⭐ **Two sub-step units carry their OWN
distinct required-reading sets and can be triple-read individually, at real but lower cost:**

- **Each of the 17 QA gates** *(Step 7)* — most share Division of Industry reading; a handful (`Gate C`,
  `Gate F`) have a distinct corpus-wide sweep worth its own triple-read.
- **Each of the 9 Review Panel positions** *(Step 8)* — the Neighbor position in particular has a narrow,
  distinct source set *(§ Casting, canon-only)* that a triple-read would meaningfully strengthen.

⏸️ **NOT run by default.** *Named as available, per `NO FORCED FIT` — a finer grain is a result to invoke
deliberately, not a mandatory expansion of scope.*

## N.5 — FALSIFICATION CONDITION, stated in advance, same house style as §9.1

| ✅ Confirmed if… | ⛔ FALSIFIED if… |
|---|---|
| **At least one real `Round 2` or `Round 3` catches a genuine miss** — *a fabricated line, or a claim a second reader cannot confirm* | **Across several real invocations, `Round 2` and `Round 3` always pass trivially, unanimously, on the first try** — *then the gate adds cost without adding signal, exactly the failure Gate 4 already names: "a gate that only ever reports success is not being run honestly"* |

## N.6 — 📌 BASELINE — **there is none, and that is stated rather than fabricated**

⛔ **`T8` has never been run.** *`Zhongshan_Opus` was written by a single continuous session, not by this
protocol — there is no "before" number to compare against, unlike `T1`–`T7`.* ✅ **The first real invocation
IS the baseline. Record it in full, raw, in the results log below** — *`04` Part IV's own standing rule: a
prediction stated in advance and then tested for the first time is worth more than a retrofit ever could be.*

| Step/Phase | Date | Round 2 verdict | Round 3 verdict (6 cross-checks) | What, if anything, was caught | Written? |
|---|---|---|---|---|---|
| *(first real invocation)* | | | | | |

---

# 5 · ⛔ WHAT MUST NEVER GO IN IT

| ⛔ | Why |
|---|---|
| **Any finding, characterization or conclusion about the location** | ***A coordinates-only file that acquires one descriptive sentence has become the thing it protects against*** |
| **Section headings copied from a withheld source** | *a heading contaminates as thoroughly as the paragraph it names* |
| **A summary of what a source says** | *the file records WHERE, never WHAT* |
| **Another location's rows, figures or names** | *except as RELATION* |
| **A path you have not tested** | *see law 3* |
| 🧪 **A trial baseline that is a CLAIM ABOUT A PLACE rather than a count** | *`M-215`. Shape is the lesson; content is the leak* |

---

# 6 · 🧪 THE FULL TEMPLATE — **§C and §D, PRE-FILLED FOR EVERY STEP AND EVERY PHASE**

> ⛔⛔ **THE CANONICAL RECIPE DOES NOT DO THIS.** *It gives one 3-row worked fragment and tells you to "resolve
> from the runbook's own table" from scratch, every time.* ✅ **This edition fills both tables completely, once,
> from a REAL pass's own tested §C/§D** — *`Zhongshan_Opus/00.0_Pre-Trip_Inspection.md`, 39/39 addresses verified
> 2026-09-07* — **with every city-keyed leaf re-templated back to `<City>`/`<Subnet>`/`<STATION>`.**
>
> ⚠ **PER `M-215`: THIS IS STRUCTURE, NOT CONTENT.** **A directory tree that every city's pass must open is not a
> finding about any one city — it is exactly the kind of universal fact this recipe exists to templatize.**
> **Nothing below states what any source SAYS, only WHERE it is.**
>
> ⛔ **STILL RE-VERIFY, PER LAW 3.** *This is a strong prior, not a substitute for testing.* **A path that
> resolved on 2026-09-07 can move.** **And this table itself can go stale exactly as a step card can** *(§3
> STEP 3's own 🧪 addition) — check it against the current `00_RUNBOOK.md`/`03_The_Phase_Spine.md` before
> trusting it blind on a much later run.*

## 6a · §C TEMPLATE — the per-step address book, Steps −1 through 10

> 🧪 **EACH STEP BELOW IS ITS OWN TABLE, WITH ITS OWN `T8` COMMAND DIRECTLY UNDER IT.** ⭐ *The command is
> IDENTICAL in shape for every step — only the step number and its resolved file(s) change — full protocol at
> `§N`. Base for all relative paths in this section:*
> `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/`

| Step | Governing rule | Section | Origin *(re-verify — line ranges drift)* | Extract *(non-authoritative)* |
|---|---|---|---|---|
| **−1** | The input contract | `# Step −1 — The input contract, before the frame` | `00_RUNBOOK.md` | `Stepwise_Execution/01_Spine/S01_Step_MINUS-1_The_input_contract_before_the_frame.md` |

> 🧪 `T8` — **Step −1:** `Agent×3(general-purpose, T8_PROMPT{files: 00_RUNBOOK.md §"Step −1", the location's own Specs/vision-note set})` → `triple_read_verify.py` → cross-check → write `00.1_Step_MINUS-1_Input_Contract.md` only on UNANIMOUS.

| Step | Governing rule | Section | Origin | Extract |
|---|---|---|---|---|
| **0** | Frame | `# Step 0 — Frame` | `00_RUNBOOK.md` | `Stepwise_Execution/01_Spine/S02_Step_0_Frame.md` |

> 🧪 `T8` — **Step 0:** `Agent×3(general-purpose, T8_PROMPT{files: 00_RUNBOOK.md §"Step 0" + §6b Phase-0 row-set below + C.1's two Step-0 boxes})` → `triple_read_verify.py` → cross-check → write `00_Frame.md` only on UNANIMOUS.

| Step | Governing rule | Section | Origin | Extract |
|---|---|---|---|---|
| **1** | Audit what is inherited | `# Step 1 — Audit what is inherited` | `00_RUNBOOK.md` | `Stepwise_Execution/01_Spine/S03_Step_1_Audit_what_is_inherited.md` |

> 🧪 `T8` — **Step 1:** `Agent×3(general-purpose, T8_PROMPT{files: 00_RUNBOOK.md §"Step 1" + C.1's Gate-9 box + all inherited canon named at §6b Phase 1})` → `triple_read_verify.py` → cross-check → write `01_Inherited.md` only on UNANIMOUS.

| Step | Governing rule | Section | Origin | Extract |
|---|---|---|---|---|
| **2** | Build the spine | `# Step 2 — Build the spine` | `00_RUNBOOK.md` | `Stepwise_Execution/01_Spine/S04_Step_2_Build_the_spine.md` |

> 🧪 `T8` — **Step 2:** `Agent×3(general-purpose, T8_PROMPT{files: 00_RUNBOOK.md §"Step 2" + 02_Generators_Capability_and_Symbols.md + §6b Phase-2 row-set})` → `triple_read_verify.py` → cross-check → write `02_Spine.md` only on UNANIMOUS.

| Step | Governing rule | Section | Origin | Extract |
|---|---|---|---|---|
| **3** | Research, aimed at what Step 2 named | `# Step 3 — Research…` | `00_RUNBOOK.md` | `Stepwise_Execution/01_Spine/S05_Step_3_Research_aimed_at_what_Step_2_named.md` |

> 🧪 `T8` — **Step 3:** `Agent×3(general-purpose, T8_PROMPT{files: 00_RUNBOOK.md §"Step 3" + the deficits Step 2 named + Real-World_Basis_Extrapolation_Method.md})` → `triple_read_verify.py` → cross-check → write `03_Research.md` only on UNANIMOUS. ⚠ *`LAW 0-R` binds here: a source is not exhausted because it was searched once — the cross-check in Round 3 is where that gets tested, not Round 2.*

| Step | Governing rule | Section | Origin | Extract |
|---|---|---|---|---|
| **4** | Write the phases | `# Step 4 — Write the phases` | `00_RUNBOOK.md` | `Stepwise_Execution/01_Spine/S06_Step_4_Write_the_phases.md` |

> 🧪 `T8` — **Step 4:** ⛔ **NOT dispatched as one unit.** *`T8` runs per-PHASE below (§6b), eleven times — Step 4 has no single required-reading set of its own, only its phases do.*

| Step | Governing rule | Section | Origin | Extract |
|---|---|---|---|---|
| **5** | Reconciliation (and the CLOSE pass) | `# Step 5 — Reconciliation…` | `00_RUNBOOK.md` | `Stepwise_Execution/01_Spine/S07_Step_5_Reconciliation_and_the_CLOSE_pass.md` |

> 🧪 `T8` — **Step 5:** `Agent×3(general-purpose, T8_PROMPT{files: 00_RUNBOOK.md §"Step 5" + 02_Generators_Capability_and_Symbols.md §5.3 + 05_The_Input_Contract.md §6.1/§6.3 + THIS location's own read-last culture file, opened as the check it is})` → `triple_read_verify.py` → cross-check → write `05_Reconciliation.md` only on UNANIMOUS.

| Step | Governing rule | Section | Origin | Extract |
|---|---|---|---|---|
| **6** | Differentiate — WRITE-ONLY | `# Step 6 — Differentiate…` | `00_RUNBOOK.md` | `Stepwise_Execution/01_Spine/S08_Step_6_Differentiate.md` |

> 🧪 `T8` — **Step 6:** `Agent×3(general-purpose, T8_PROMPT{files: 00_RUNBOOK.md §"Step 6" + 04_QA_Gates_and_Differentiation.md Part III})` → `triple_read_verify.py` → cross-check → write `06_Differentiation.md` **+ this location's row in `Cross_City_Culture_Differentiation_Table.md`** only on UNANIMOUS. ⛔ **WRITE-ONLY still applies inside `T8`** — *no reader may open another location's cell, even to verify a peer's read.*

| Step | Governing rule | Section | Origin | Extract |
|---|---|---|---|---|
| **7** | QA | `# Step 7 — QA` | `00_RUNBOOK.md` | `Stepwise_Execution/01_Spine/S09_Step_7_QA.md` |

> 🧪 `T8` — **Step 7:** `Agent×3(general-purpose, T8_PROMPT{files: 04_QA_Gates_and_Differentiation.md Parts I-II, all 17 gates + §6b's Phase-7 Division-of-Industry set})` → `triple_read_verify.py` → cross-check → write `07_QA_Gates.md` only on UNANIMOUS. ⏸️ *§N.4 offers a finer per-gate split as an optional, non-default extension.*

| Step | Governing rule | Section | Origin | Extract |
|---|---|---|---|---|
| **8** | The Review Panel | `# Step 8 — The Review Panel` | `00_RUNBOOK.md` | `Stepwise_Execution/01_Spine/S10_Step_8_The_Review_Panel.md` |

> 🧪 `T8` — **Step 8:** `Agent×3(general-purpose, T8_PROMPT{files: Disciplines/00f_Review_Panel.md in full — PIN RE-VERIFIED first, per 00f's own demand})` → `triple_read_verify.py` → cross-check → write `08_Review_Panel.md` only on UNANIMOUS. ⏸️ *§N.4 offers a finer per-position split as an optional extension.*

| Step | Governing rule | Section | Origin | Extract |
|---|---|---|---|---|
| **9** | Record | `# Step 9 — Record` | `00_RUNBOOK.md` | `Stepwise_Execution/01_Spine/S11_Step_9_Record.md` |

> 🧪 `T8` — **Step 9:** `Agent×3(general-purpose, T8_PROMPT{files: 00_RUNBOOK.md §"Step 9" + §9.5 + Test_Runs/OBSERVATIONS_and_Methodology_Findings.md's tail, for the next M-number})` → `triple_read_verify.py` → cross-check → write `09_Record.md` + `09.5_Log.md` only on UNANIMOUS.

| Step | Governing rule | Section | Origin | Extract |
|---|---|---|---|---|
| **10** | The readiness check | `# Step 10 — THE READINESS CHECK` | `00_RUNBOOK.md` | `Stepwise_Execution/01_Spine/S12_Step_10_THE_READINESS_CHECK.md` |

> 🧪 `T8` — **Step 10:** `Agent×3(general-purpose, T8_PROMPT{files: 00_RUNBOOK.md §"Step 10" §§10.1-10.3 + the auto-loaded memory index + 06_Worked_Example_Provenance.md})` → `triple_read_verify.py` → cross-check → write `10_Readiness_Check.md` only on UNANIMOUS. ⚠ *Item 1a's contamination scan targets the NEXT location, not this one — `T8`'s three readers must not be the same three sessions that could become that next pass.*

⭐ **All twelve, plus the 17 gates, resolve under one base:**
`/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/`.
**Gates:** `04_QA_Gates_and_Differentiation.md`, extract layer `Stepwise_Execution/02_Gates/G01`–`G17_*.md`.
⚠ **The 29-file extract layer is a navigation convenience only — `Stepwise_Execution/README.md` §3: *"THE
SOURCE FILES ARE THE METHODOLOGY. If a unit file and its source disagree, THE SOURCE WINS, always."*** ⛔ **And
per `STEP 3`'s 🧪 addition above: check that BOTH sides actually agree before trusting either.**

### 🧪 C.1 — Four steps carry an extra required-reading box beyond the main table *(`M-208`)*

| Step | New required file | Instruction |
|---|---|---|
| **0** | `Run_Modes_Warm_and_Cold.md` *(whole file)* | Declare WARM/COLD here, per §2 |
| **0** | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md` | Read in full at Step 0, not merely by the phase that first needs it |
| **1** | `04_QA_Gates_and_Differentiation.md`, **Gate 9** (Asymmetry) | Cite Gate 9 by name when Step 1 runs the asymmetry check on inherited material |
| **5** | `02_Generators_Capability_and_Symbols.md` §5.3 (both-are-true) + `05_The_Input_Contract.md` §6.1/§6.3 | Open both at the point of use, not from memory |
| **6** | `04_QA_Gates_and_Differentiation.md`, Part III (the differentiation instrument) | Add this location's column, write-only, per `04` III.4 |

## 6b · §D TEMPLATE — the per-phase canon, Phases 0 through 10 · **`U`** = universe repo · **`P`** = this project

> ⚠ **BOLD tails are what `STEP 2` must resolve to a real filename.** ⭐ **Everything NOT bold is a universal,
> literal, absolute path — identical for every city, never templated.** 🧪 **Each phase is its own table, with
> its own `T8` command directly under it** — *the command's file-list is exactly that phase's own rows above it.*

| Ph | Must open | Resolved address | Tier |
|---|---|---|---|
| **0** | **U** Repo scope | `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Repo_Scope.md` | once/project |
| **0** | **U** Timeline eras | `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Timeline Eras/` | `MAPPED` |
| **0** | **P** Census | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md` | `MAPPED` |

> 🧪 `T8` — **Phase 0:** `Agent×3(general-purpose, T8_PROMPT{files: the 3 rows above})` → `triple_read_verify.py` → cross-check → content feeds `00_Frame.md` only on UNANIMOUS.

| Ph | Must open | Resolved address | Tier |
|---|---|---|---|
| **1** | **P** Spec | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/`**`<City>.md`** | `MAPPED` |
| **1** | **P** Energy grid | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Energy_Grid_Failure_Rationale.md` | `MAPPED` |
| **1** | ⭐⭐ **P** Climate READER | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Climate Data/READER/`**`<REAL-WORLD STATION NAME>.md`** | `MAPPED` — ⛔ **keyed by STATION, not city — resolve via the alias set (§ STEP 1)** |
| **1** | Stations | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Stations/` | background only |
| **1** | Div. of Industry `16` Half B | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/16_Per_City_Three_Tier_Run.md` | ⛔ `QUERYABLE-BY-SCHEMA` — never grep by subject name |

> 🧪 `T8` — **Phase 1:** `Agent×3(general-purpose, T8_PROMPT{files: the 5 rows above — Climate READER resolved via the alias set FIRST})` → `triple_read_verify.py` → cross-check → content feeds Step 1's `01_Inherited.md` and Phase 1's own text only on UNANIMOUS.

| Ph | Must open | Resolved address | Tier |
|---|---|---|---|
| **2** | **U** No National Stereotypes — BINDING | `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md` | `MAPPED` |
| **2** | **U** Falkland Treaty | `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Falkland_Treaty/` | `MAPPED` |
| **2** | **P** Census | *(as Phase 0)* | |
| **2** | ⛔ *"diaspora/affinity files"* | **RESOLVES TO NOTHING ADMISSIBLE** — the only candidate on disk maps cities to CONCORDIA DISTRICTS, forbidden by `§C.8d` and `THE LAW OF ONE LOCATION` | **`M-173`: out of scope, not a hole** |

> 🧪 `T8` — **Phase 2:** `Agent×3(general-purpose, T8_PROMPT{files: the 3 admissible rows above — the 4th resolves to nothing and is reported, not chased})` → `triple_read_verify.py` → cross-check → write `04_Phase_02_Composition_and_Arrival.md` only on UNANIMOUS.

| Ph | Must open | Resolved address | Tier |
|---|---|---|---|
| **3** | Climate READER | *(as Phase 1)* | |
| **3** | Concept art | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Concept-Art/`**`<Subnet>/<City>/`** | *empty is common — a RESULT* |
| **3** | ⛔ Physical infrastructure attributes | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Megasheets/`**`<Subnet>/<City>/<City>_Physical_Infrastructure_Attributes.md`** | ⛔ **WITHHELD corpus-wide — record the conflict, do not open** |

> 🧪 `T8` — **Phase 3:** `Agent×3(general-purpose, T8_PROMPT{files: Climate READER + Concept art directory — the Megasheet row is WITHHELD, never dispatched to a reader})` → `triple_read_verify.py` → cross-check → write `04_Phase_03_Surface_and_Texture.md` only on UNANIMOUS.

| Ph | Must open | Resolved address | Tier |
|---|---|---|---|
| **4** | ⭐⭐ Robot Physiology — GOVERNING | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md` | `MAPPED` — read FIRST |
| **4** | Robot Cold Physiology | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Cold_Physiology.md` | narrow companion — open the file above FIRST (`M-151`) |
| **4** | `16` Half B | *(as Phase 1)* | |
| **4** | `09` §3.5 freedom gradient | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/09_Per_City_Baseline_Run.md` | `MAPPED` |
| **4** | `11` food layer rebuild | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/11_Caloric_Rebuild_and_Livestock_Tier.md` | `MAPPED` |
| **4** | National Medical and Care Institutes | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/National_Medical_and_Care_Institutes.md` | `locked-canon` — check for THIS location by name |
| **4** | National Economy and Currency | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/National_Economy_and_Currency.md` | `MAPPED` |

> 🧪 `T8` — **Phase 4:** ⭐⭐ **THE LARGEST PHASE DISPATCH — 6 files, including the two `M-151`-ordered ones.** `Agent×3(general-purpose, T8_PROMPT{files: the 6 rows above, Robot Physiology BEFORE Robot Cold Physiology, explicit in the prompt})` → `triple_read_verify.py` → cross-check → write `04_Phase_04_Ordinary_Life.md` only on UNANIMOUS. ⚠ *`Round 3` here is where `M-151`'s trap (reading the narrow file first and treating every hazard as a species gate) would surface — a reader who read them in the wrong order produces a detectably different Phase 4.*

| Ph | Must open | Resolved address | Tier |
|---|---|---|---|
| **5** | **U** Locations, routes | `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Worldspace/Locations/` | `MAPPED` |
| **5** | Highways | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Infrastructure/Highways.md` | `MAPPED` |
| **5** | Airports / Ports | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Infrastructure/` | `MAPPED` |
| **5** | City_Cross_Subnet_Relationships | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Cross_Subnet_Relationships.md` | `MAPPED` |
| **5** | City_Relationship_Database | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Relationship_Database.md` | `MAPPED` |
| **5** | City_National_Connections | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_National_Connections.md` | `MAPPED` — ⚠ **draws on withheld/read-last material by its own stated method; open the header first (§ STEP 4)** |

> 🧪 `T8` — **Phase 5:** `Agent×3(general-purpose, T8_PROMPT{files: the 6 rows above — City_National_Connections header checked FIRST for downstream withheld material, per §D STEP 4 of the recipe})` → `triple_read_verify.py` → cross-check → write `04_Phase_05_Relation_and_Geometry.md` only on UNANIMOUS.

| Ph | Must open | Resolved address | Tier |
|---|---|---|---|
| **6** | Robot Religions — roster OPEN | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Factions/Robot_Religions/` | `MAPPED` — a zero return is a RESULT |
| **6** | National Holidays | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/National_Holidays.md` | `MAPPED` |
| **6** | Ice-Cold Buddhism research | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Ice-Cold_Buddhism_Research/` | check relevance, do not assume it |
| **6** | ⛔ Mortuary question | — | **RESERVED — do not answer** |

> 🧪 `T8` — **Phase 6:** `Agent×3(general-purpose, T8_PROMPT{files: the 3 open rows above — the Mortuary question is RESERVED and must not be dispatched to any reader})` → `triple_read_verify.py` → cross-check → write `04_Phase_06_Meaning.md` only on UNANIMOUS. ⭐ *This is also where `T5`'s early Lover-faculty marker gets written, once `T8` clears.*

| Ph | Must open | Resolved address | Tier |
|---|---|---|---|
| **7** | ⭐⭐ Division of Industry — PRIMARY | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/` | ⛔ **READ ITS OWN `README.md` FIRST** |
| **7** | Division_of_Industry_Sweep §4.4 | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry_Sweep_2026-08-31.md` | `MAPPED` |
| **7** | `01_Burden_Scoring_Model` / `08_Volume_Based…` | *(same Division_of_Industry/ directory)* | `MAPPED` |
| **7** | National Medical Institutes | *(as Phase 4)* | ⭐ **open for Phase 7 too — names locations directly** |
| **7** | Theoretical-Calculations | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Theoretical-Calculations/` | `MAPPED` |
| **7** | Industry Staffing / SOC | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Industry_Staffing_and_Productivity/` | ⚠ additive only |
| **7** | National Economy | *(as Phase 4)* | |
| **7** | City Logistics ⚠ | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/City_Logistics.md` | ⛔ **Concordia-scoped — only its dual-economy + currency-pointer sections generalize (`M-152`)** |
| **7** | Factions + criminal justice | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Factions/` | `MAPPED` |
| **7** | **U** Megacorps | `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Megacorps/` | `MAPPED` |

> 🧪 `T8` — **Phase 7:** ⭐⭐ **THE WIDEST PHASE DISPATCH — 9 files.** `Agent×3(general-purpose, T8_PROMPT{files: the 9 rows above — Division_of_Industry/README.md read FIRST, City Logistics restricted to its two general-purpose sections per M-152})` → `triple_read_verify.py` → cross-check → write `04_Phase_07_Order.md` only on UNANIMOUS.

| Ph | Must open | Resolved address | Tier |
|---|---|---|---|
| **8** | ⚠⚠ Robot Biology — MANDATORY | *(as Phase 4)* | before ANY siligel/coolant claim |
| **8** | Weapons and Tools Philosophy | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Weapons_and_Tools_Philosophy.md` | `MAPPED` |

> 🧪 `T8` — **Phase 8:** `Agent×3(general-purpose, T8_PROMPT{files: the 2 rows above — Robot Physiology MANDATORY before any siligel/coolant claim, explicit in the prompt})` → `triple_read_verify.py` → cross-check → write `04_Phase_08_Making.md` only on UNANIMOUS.

| Ph | Must open | Resolved address | Tier |
|---|---|---|---|
| **9** | ⚠⚠ **U** Laws of Robotics | `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Laws_of_Robotics.md` | binding |
| **9** | ⚠⚠ **U** Robot Universals *(Ch. 13, 14 esp.)* | `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Robot_Universals/` | `MAPPED` |
| **9** | **U** Doll Representation Categories | `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Doll_Representation_Categories.md` | `MAPPED` |
| **9** | Human-robot baseline | *(Robot_Physiology_and_Cultural_Practices.md, as Phase 4)* | |

> 🧪 `T8` — **Phase 9:** ⭐⭐⭐ **THE HIGHEST-STAKES DISPATCH — this is `M-169`'s own phase.** `Agent×3(general-purpose, T8_PROMPT{files: the 4 rows above, ALL BINDING})` → `triple_read_verify.py` → cross-check → write `04_Phase_09_Populations.md` only on UNANIMOUS. ⛔ **If `T8` had governed the original writing of this exact phase on a prior pass, `M-169`'s false headline finding could not have reached a file — `Round 2` alone requires proof of having opened all three robot-canon sources it skipped.**

| Ph | Must open | Resolved address | Tier |
|---|---|---|---|
| **10** | **U** Characters | `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Worldspace/Characters/` | ⛔ **actually run the check — do not assert "0" without executing it** |
| **10** | Enneagram Character Index | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Characters/Enneagram_Character_Index.md` | check and record |
| **10** | Zodiac Lens terms | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Zodiac_Signs_Full_Attributes.md` | read each sign's terms FROM THIS FILE, never from the name |
| **10** | ⛔ No invented person names | — | **RESERVED — role-archetypes only** |

> 🧪 `T8` — **Phase 10:** `Agent×3(general-purpose, T8_PROMPT{files: the 3 open rows above — the person-names row is RESERVED, not dispatched})` → `triple_read_verify.py` → cross-check → write `04_Phase_10_Catalog.md` only on UNANIMOUS.

> ⭐ **Provenance: 39 addresses, all tested `✅` on the source pass, 2026-09-07.** ⛔ **`STILL RE-TEST — Law 3.`**

## 6c · WORKED FRAGMENT — *retained, the shape of a §D row before templating*

| Phase | Must open | Resolved absolute address | Exists | Tier | Carve-out |
|---|---|---|:--:|---|---|
| **3** | **Climate** | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Climate Data/READER/`**`<the REAL-WORLD STATION filename>.md`** | ✅ | `MAPPED` | ⛔ **Keyed by station name, NOT city name** |
| **3** | **Concept art** | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Concept-Art/`**`<Subnet>/<City>/`** | ⭐ **EMPTY** | — | ✅ ***Opened-and-empty is a RESULT*** |
| **7** | **Industry** | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/` | ✅ | ⛔ `QUERYABLE-BY-SCHEMA` | ⛔ **Read its status header FIRST** — 🧪 *and quote any self-flagged unreconciled figure* |

---

# 7 · ⭐ THE TEST THAT SAYS THE INSPECTION IS DONE

> ## **Could a session that has never seen this location open every file the ULM requires, in the right order, without searching for anything?**

⛔ **If the answer needs a `find`, a `grep`, or a guess about a filename, the inspection is not finished.**
⭐ **And if it needs the pass to already know the location, the inspection has been written backwards.**

---

# 8 · ⚠ THE FAILURE THIS RECIPE CANNOT PREVENT

***An address book does not make anyone read.***

> ### ⭐⭐ **SO THE GENERATED FILE'S LAST SECTION IS A RECEIPT, NOT A LIST:**
> **each phase, on completion, records WHICH of its required sources it actually opened — in the phase file
> itself, never only in a log.** ⛔ ***A source read but cited only in a log is invisible to everything
> downstream.***

## 🧪 8b · AND THE FAILURE **THIS EDITION** CANNOT PREVENT

⛔ **`T1`–`T7` are all bookkeeping and form.** ***Not one of them can tell you the pass is THIN.***
⛔ **And none of them touches plausibility** — *that is Gate 11's job, and the arithmetic half of it at that.*

> ### ⚠ **If the `Lover faculty` still passes only on after-the-fact material with all seven active, then the shed category is NOT recoverable by bookkeeping, and the fix has to be structural** — *the panel moved earlier, or the phase spine rebalanced.* **Record that outcome as loudly as a success.**

---

# 🧪 9 · THE TRIAL APPARATUS

## 9.1 — FALSIFICATION CONDITIONS, **stated in advance**

> **`04` Part IV: a self-grader's perfect record is house style, not evidence. The remedy —** ***"state in
> advance what observation would falsify each rule"*** **— "costs nothing and is the one that has never been
> done."**

| 🧪 | ✅ Confirmed if… | ⛔ FALSIFIED if… |
|---|---|---|
| **T1** | A mismatch is caught at a phase close, **before** the target phase is written | **Mismatches are reconciled cosmetically** — *rows marked discharged that were not* |
| **T2** | Every phase closes with an enumerated receipt | **Receipts appear and are empty, or are written AFTER the phase.** *A receipt for an act already done is a record, not a check* |
| **T3** | A row is visibly blank before Step 8 **and that blank is acted on** | ⛔⛔ **The ledger is filled in retroactively at Step 8** *(a summary, not a warning)* — **or a phase writes toward a blank row** *(the contamination `00f` forbids)* |
| **T4** | At least one phase names a shed category a later position would have missed | **Every phase answers "nothing"** — *then the question is decorative* |
| **T5** | The early run says "not yet" and the late run says "yes" | **The early run changes what the middle phases write.** *Then it is generative and must be withdrawn* |
| **T6** | A quotation defect is caught at a phase close, before Step 7 | **The audit is skipped at phase closes and only run at Step 7 again** |
| **T7** | `confirmed defects in CELLS` falls toward zero while prose stays clean | ⛔ **Confirmed defects appear in PROSE at a comparable rate** — *then the container was never the variable and the diagnosis is wrong* |

## 9.2 — THE BASELINE — **shape only, per `M-215`**

| Measure | Baseline *(one pass, city 3, Opus array, no trial active)* |
|---|---|
| **Outbound handoff rows** | `22` |
| ⛔ **Phases with rows addressed to them and NO enumeration** | **`5` of `8` eligible** |
| **Sweep form: formal / informal / none** | `3 / 1 / 5` — *and one of the 3 is a repair* |
| **Quotation fragments tested** | `212` |
| **Confirmed quotation defects** | `4` — ⛔ **`4` in CELLS, `0` in PROSE** |
| **Position-coverage ledger** | ⛔ **Did not exist** |
| **`Lover faculty` verdict** | ✅ **PASS** — ⛔ **resting entirely on material added after the fact** |

⛔ **Full raw output and the worked findings live at `04` Parts V and V.2 and are NOT restated here.**

## 9.3 — ⛔⛔ GUARDS

- ⛔ **The baseline pass must NOT be retrofitted or corrected.** ***It is the only number the trial has to beat.***
- ⛔ **Do NOT run this edition on a held control arm of a model-divergence fork.** *Introducing a new instrument
  into one arm destroys that experiment to serve this one.*
- ✅ **Run it on the NEXT location to open a pass.**
- ⛔⛔ **SUPERSEDED 2026-09-11 — `T1`–`T8` ARE MANDATORY ON EVERY STEP, EVERY PHASE, EVERY CITY.** *(Developer
  ruling; see §N.3.)* ***The line below applied while these were opt-in trials. They are not opt-in any more.***
  ⭐ **RECORDING is still required — the falsification conditions stand — but recording is now IN ADDITION to
  complying, not INSTEAD of it.**
- ⚠ ~~**The obligation is to RECORD, not to comply.**~~ ***A pass that applies none of `T1`–`T7` but runs the two
  audits and reports the numbers has fully discharged the trial*** — **and is the more informative result,
  because it measures whether the defect recurs unaided.**
- ⚠ **This compares INSTRUMENTS across runs, never locations.** ✅ **`THE LAW OF ONE LOCATION` is untouched.**

## 9.4 — 📌 RESULTS LOG

| Location | Date | Outbound | Phases w/ NO enumeration | formal/informal/none | Quot. defects `CELL`/`PROSE` | Lover faculty | Rested on a late repair? | T1–T7 applied | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| *(baseline — see 9.2)* | 2026-09-11 | `22` | **`5` of `8`** | `3/1/5` | **`4` / `0`** | ✅ PASS | ⛔⛔ **YES** | ⛔ none | ⚠ **BASELINE, not a test** |
| | | | | | | | | | |

---

> # 🧪 **END OF TRIAL EDITION.**
> **Canonical recipe unchanged at
> `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/PRE-TRIP_INSPECTION_RECIPE.md`.**
> ⛔ **If this edition and the canonical recipe disagree on anything NOT marked 🧪, the canonical one wins and
> the divergence is a defect in this file.**
