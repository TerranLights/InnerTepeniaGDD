# THE PRE-TRIP INSPECTION — **a RECIPE for generating one location's own address book**

**Written 2026-09-07, from the measured failures of city 2 (`Sinheung`).**
**Applies to any location of any type, in any setting that uses this methodology.**

> # ⛔ THIS FILE IS A GENERATOR, NOT A LIST.
> **It does not tell you where anything is.** ***It tells you how to WRITE, for one named location, a file that
> does*** — **with every address absolute, resolved to that location's real filenames, and mechanically tested
> before the pass begins.**

---

# 0 · WHY THIS EXISTS — **three measured failures, all from one city's pass**

| | What happened | Finding |
|---|---|---|
| **1** | ⛔ **A phase whose entire subject was populations wrote itself without opening ANY of its three required robot-canon sources — and produced a CONFIDENT FALSE HEADLINE FINDING.** *It passed the spelling sweep, the table check, the contradiction gate, the quotation audit, the dual-tag diagnostic AND the swap test.* ***Nothing except opening the source could have caught it*** | **`M-169`** |
| **2** | ⛔ **The requirement existed the whole time** — in a file the phase-writing procedure never told anyone to open. ***Registered globally is not registered at the point of use*** | **`M-121`** |
| **3** | ⛔ **A registry row named a source without a path; a pass searched the implied tree, got a confident zero, and the real tree was elsewhere.** ***A name is not an address*** | **`M-117`** |

> ### ⭐⭐ AND THE ONE THAT MAKES A GENERATED FILE NECESSARY RATHER THAN A SHARED ONE:
> **The per-phase canon table is written with TEMPLATE addresses** — `Specs/<City>.md`, `READER/<City>.md`,
> `City_Concept-Art/<Subnet>/<City>/`. ⛔ ***A template address is not an address.*** **It is a rule for
> constructing one, and it is silently wrong whenever the real filename differs** — which in this corpus it
> routinely does *(the climate set is keyed by REAL-WORLD STATION NAME, not by city name; renamed locations keep
> retired placeholder filenames; four of thirty-seven concept-art folders hold anything at all)*.

---

# 1 · WHERE THE OUTPUT GOES

```
<location's own pass folder>/00.0_Pre-Trip_Inspection.md
```

⛔ **It is written BEFORE `Step −1`, and it is the first file in the folder.**
⭐ **It is coordinates and status only** — *addresses, existence, tier, carve-outs.* ⛔ **It contains NO findings,
NO characterization, and NO content from any source it names**, *so it is safe to read in full at any time and
in any run mode.*

---

# 2 · ⛔⛔ THE FIVE LAWS OF THE GENERATED FILE

> ## **1. ABSOLUTE, ALWAYS.**
> **Every address is written from `/`.** ⛔ **Never a `../` form, never an `…/` abbreviation, never a bare
> filename.** *A relative path is folder-dependent and these files are read from at least three directories.*
> ⚠ **And a pointer that names no file is worse than either** *(`M-117`)*.

> ## **2. RESOLVED, NOT TEMPLATED.**
> ⛔ **`<City>` and `<Subnet>` must not survive into the output.** ***Substitute the real name, then look at what
> is actually on disk, and write THAT filename.***

> ## **3. TESTED, NOT ASSERTED.**
> **Every address is tested for existence and the result is recorded in the file.** ⭐ *`Step 10`'s governing
> principle applied one step earlier: **verify, do not assert.*** ⚠ **A claim that verification happened is a
> claim like any other** *(the registry's own "verified to exist" line was once wrong about two of four rows)*.

> ## **4. EMPTY IS A RESULT; MISSING IS A HOLE; WITHHELD IS A RULING.**
> **Three different states, recorded differently.** ⛔ ***A source that does not exist for this location is a
> FINDING the pass may rely on. A source nobody looked for is a hole.***

> ## **5. EVERY ROW CARRIES A TIER AND ANY CARVE-OUT.**
> ***An un-tiered row is an open door.*** **An address with no admissibility ruling is an instruction to read
> blind.**

---

# 3 · THE PROCEDURE — **nine steps, in order**

## STEP 1 — **Build the ALIAS SET first.** ⛔ *Nothing else works without it*

**A resolution sweep is only as wide as its alias list** *(`M-118`)*.

**Collect, from the location's own spec and any rename notes:**

| Alias class | Why it matters |
|---|---|
| **Current in-fiction name** | the obvious one |
| ⭐⭐ **The REAL-WORLD BASIS NAME** | ***the sharpest case — most climate and station files are keyed by it, not by the city name*** |
| **Retired placeholder / working titles** | *this corpus renames routinely; old filenames persist* |
| **Other scripts or spellings** | *hangul/hanja, transliteration variants, a `z` where you expect an `s`* |
| **Candidate names considered and dropped** | *they appear in archived lists and sometimes in filenames* |

> ⛔ **Assume an alias exists until you have checked.** ⭐ **Record the alias set IN the generated file**, so the
> next session sweeps the same width.

## STEP 2 — **Declare the run mode, because it changes what is admissible**

**Read the run-modes file and state WARM or COLD in the output.** ⛔ **There is no third mode.**
⚠ **The one rule that never relaxes in either:** ***this location's own culture material is read LAST, as a
CHECK*** — **and in a warm run nothing enforces it, so the generated file must carry it as an explicit,
dated line rather than an assumption.**

## STEP 3 — **Resolve the PER-STEP citations** *(Steps −1 through 10)*

**For each step, name the file that governs it AND the file it must open.** ⭐ **Two different things, and
passes conflate them.**

| For every step, the row records | |
|---|---|
| **The GOVERNING rule** | *the runbook section, plus its step-wise extract card if one exists* |
| ⚠ **The extract's ORIGIN LINE RANGE** | ⛔ **and whether it is still accurate** — *a runbook grows, and a stale line range is a wrong address to the source of truth* |
| **The SOURCES that step reads** | *resolved and tested* |
| **What it WRITES** | *so `Gate 0` can later check the claim against the file* |

## STEP 4 — **Resolve the PER-PHASE canon**, from the authoritative table only

> ⛔⛔ **USE THE RUNBOOK'S OWN PER-PHASE TABLE. Do NOT build from a secondary copy.**
> ***Measured: a short-form copy of that table had not absorbed a developer ruling and was missing a third of the
> requirement; a pass built from it re-introduced a file the ruling had removed.***

**For every phase, resolve each named class to real files, and record:**

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
**Record, against the phase that would cite it:**

- **Any open ruling that BLOCKS a class of figure** *(e.g. an unresolved convention blocking every export figure)*
- **Any validated-as-unreliable layer**, plus the file that must be read first before citing it
- **Any standing convention that makes a figure look wrong when it is right** *(e.g. all process-derived figures baselined on one census while the narrative frame uses another)*
- ⭐ **Any source organized by location name** → ⛔ **`QUERYABLE-BY-SCHEMA`: never grep it by the subject's name; anchor to structure**

## STEP 6 — **List the EXCLUSIONS — what is NOT an input, by name**

> ⭐⭐ **This section prevents two opposite errors at once**, both of which have occurred: *a pass reading
> out-of-frame material as supply, and an audit reading its absence as a gap.*

**Record explicitly:**

| Class | Disposition |
|---|---|
| **Spec sections outside the declared frame** | ⛔ **NOT INPUTS. Their absence is CORRECT** — *never record it as missing, never write them* |
| **Test-run material for this location** | ⛔ **ZERO INTAKE for the whole duration of this location's pass** — *reopens per location, after that pass closes* |
| **Any tree the standing facts withhold** | ⛔ *record the address so nobody re-derives it as a gap, and mark it closed* |
| ⭐ **This location's own culture/conclusion material** | ⏸️ **READ-LAST, as a check — name the exact file and the step at which it opens** |
| **Retrieval layers that cannot honor a quarantine** | ⏸️ *flagged per run mode* |

## STEP 7 — **Cite the LAWS, not only the files**

⭐ **A pass that has the addresses and not the laws will produce well-sourced violations.**
**Name, with their addresses, every binding law that governs a location pass** — *depth over speed; research
fully; no forced fit; one location on its own terms; the composition/culture sequencing ruling and what it
UNLOCKS; the divergence operator and the ban on reasoning from elapsed time; the general-population and
shadow-proportion disciplines; the no-invented-names rule; the layering law.*

> ⚠ **For each, record the ONE-LINE OPERATIONAL FORM, not a summary** — *a procedure that cites its governing law
> instead of stating it will be run without it.*

## STEP 8 — **Pre-load the INBOUND HANDOFF SWEEP**

> ⛔ **The methodology requires every phase to WRITE a handoff table and requires no phase to READ one.** *There
> is no receipt and no gate.* ***Three handoffs were dropped in a single pass before anyone noticed.***

**So the generated file carries a standing instruction, per phase:**

> **Before writing phase `N`, search every prior file of this pass for `Phase N` and enumerate every row
> addressed to it.** ⚠ **Use a NORMALIZED search — strip emphasis and collapse line wrapping — because a literal
> match on prose produces false accusations against correct text.**

## STEP 9 — **RUN THE VERIFICATION GATE, and paste its raw output into the file**

```
for every address in this file:
    test existence
    record ✅ resolves / ⛔ MISSING / ⏸️ withheld-by-ruling
report: N addresses · N resolve · N broken
```

> ⛔ **A pre-trip inspection with an untested address is not an inspection.**
> ⚠ **And a template placeholder is not a broken address** — *`<City>`-style tokens are a DIFFERENT defect:
> they mean step 2 was not finished.* **Report them separately.**

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
| **H** | **Handoff-sweep instruction** | *the per-phase inbound sweep* |
| **I** | ⭐ **The verification block** | *raw output: N addresses, N resolve, N broken* |
| **J** | **Open rulings that touch this location** | *anything that blocks a step before it starts* |

---

# 5 · ⛔ WHAT MUST NEVER GO IN IT

| ⛔ | Why |
|---|---|
| **Any finding, characterization or conclusion about the location** | ***A coordinates-only file that acquires one descriptive sentence has become the thing it protects against*** |
| **Section headings copied from a withheld source** | *a heading contaminates as thoroughly as the paragraph it names* |
| **A summary of what a source says** | *the file records WHERE, never WHAT* |
| **Another location's rows, figures or names** | *except as RELATION, and only where the location's own material requires it* |
| **A path you have not tested** | *see law 3* |

---

# 6 · WORKED FRAGMENT — *the shape of a §D row, filled*

> ⚠ **The BOLD tail of each address is the part STEP 2 must replace with a real filename.** ⛔ **The base is
> written in full because this recipe obeys its own Law 1** — *no `…/`, no `../`, ever, including in examples.*

| Phase | Must open | Resolved absolute address | Exists | Tier | Carve-out |
|---|---|---|:--:|---|---|
| **3** | **Climate** | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Climate Data/READER/`**`<the REAL-WORLD STATION filename>.md`** | ✅ | `MAPPED` | ⛔ **Keyed by station name, NOT city name — resolved via the alias set.** *A city-name search returns a false negative* |
| **3** | **Concept art** | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Concept-Art/`**`<Subnet>/<City>/`** | ⭐ **EMPTY** | — | ✅ ***Opened-and-empty is a RESULT.*** *Only a handful of locations hold images; record the emptiness so no later audit reads it as a gap* |
| **7** | **Industry** | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/` | ✅ | ⛔ `QUERYABLE-BY-SCHEMA` | ⛔ **Read its status header FIRST.** *One layer is validated-unreliable; one open ruling blocks every export figure* |

---

# 7 · ⭐ THE TEST THAT SAYS THE INSPECTION IS DONE

> ## **Could a session that has never seen this location open every file the ULM requires, in the right order, without searching for anything?**

⛔ **If the answer needs a `find`, a `grep`, or a guess about a filename, the inspection is not finished.**
⭐ **And if it needs the pass to already know the location, the inspection has been written backwards.**

---

# 8 · ⚠ THE FAILURE THIS RECIPE CANNOT PREVENT

***An address book does not make anyone read.*** **The pass that produced this recipe had the runbook available
the entire time, was instructed to read it in full, and searched it instead** — *because a summary and a resume
block produce familiarity without knowledge, and `grep` returns exactly what you already thought to ask for.*

> ### ⭐⭐ **SO THE GENERATED FILE'S LAST SECTION IS A RECEIPT, NOT A LIST:**
> **each phase, on completion, records WHICH of its required sources it actually opened — in the phase file
> itself, never only in a log.** ⛔ ***A source read but cited only in a log is invisible to everything
> downstream.*** ⭐ **That converts "did you open it" from a claim into an artifact, which is the only form of
> this instruction that has ever held.**
