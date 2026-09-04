# STEPWISE EXECUTION — the ULM broken into 29 invocable units

**Built 2026-09-03 at the developer's direction.** ***Purpose: replace one large invocation with twenty-nine
small ones.***

---

# 0. WHY THIS EXISTS — read this once, it is the whole design

**"Run the ULM process on City-X" is a correct and complete instruction.** ***It is also a single invocation
that expands into ~30 steps, 17 gates, 11 phases and several hundred sub-instructions — with exactly ONE
checkpoint, at the end, where the report on the work is written by the same party that did the work.***

**The observed failure mode, recorded because it is the reason this folder exists:**

| Instruction type | What happens to it |
|---|---|
| **PRODUCING** — write the phase, derive the finding, name the axis | ✅ **carried out.** It feels like the work and it generates visible output |
| **CONSTRAINING** — log the search strings, paste the raw scan, add the column, append the `M-` entry, run `graphify update`, do not summarize | ⛔ **dropped under load.** Generates no visible output, and ***nothing fails when it is skipped*** |

> ## **One invocation gives you one place to check. Twenty-nine gives you twenty-nine.**
> **Every drift recorded on 2026-09-03 happened INSIDE a batch and would have been caught in the first unit.**

---

# 1. HOW TO INVOKE

> ## **"Run `S04`."** — or — **"Run `G07` on City-X."**
> ***One unit. Stop at the end. Report. Wait.***

**Do not say "run the spine" or "do the gates."** ***Those are batches, and batching is where constraints get
dropped.***

## The three asks that make a unit verifiable

1. **"Paste the raw output."** ⛔ **Never accept a verdict in place of evidence.** *(`00_RUNBOOK.md` Step 7:
   an instruction to read carefully "does not survive an author grading their own work.")*
2. **"Quote the instruction before you execute it."** ***Working from a remembered summary of the ULM is how
   the wrong artifact gets audited.*** **It has happened.**
3. **"What did you have to decide that the instruction did not state?"** ⛔ **Every false finding on record
   came from a self-supplied criterion.** **The correct response to a missing criterion is a QUESTION, never
   a judgment.**

---

# 2. THE ORDER — and note where the gates actually fire

**The spine runs `S01 → S12`. THE SEVENTEEN GATES ARE NOT A THIRTEENTH STEP — they ARE `S09`.**

| # | Unit | What it is |
|---|---|---|
| **S01** | `Step −1` | **The input contract.** Run `05` §7's pre-flight. **Tier 0 blocking · Tier 1 ≥3 generators or no spine** |
| **S02** | `Step 0` | **Frame.** The declaration block · read the five `Disciplines/` · Gate 0 · read existing material in the mandated ORDER · reserved decisions · provisional parent assumptions |
| **S03** | `Step 1` | **Audit what is inherited.** The asymmetry check on existing findings |
| **S04** | `Step 2` | ⭐ **BUILD THE SPINE.** *"The step everything else hangs on."* Three independent generators, four quadrants each, compare, read shape, read deficit address, divide population by extent |
| **S05** | `Step 3` | **Research, aimed at what Step 2 named.** ⚠ **Never before `S04` is finished** |
| **S06** | `Step 4` | **Write Phases 2–10** *(per `03`)* |
| **S07** | `Step 5` | **Reconciliation + the CLOSE pass** *(`03` §0.4's docket)* |
| **S08** | `Step 6` | **Differentiate** *(`04` Part III)* |
| **S09** | `Step 7` | ⭐⭐ **QA — RUN ALL SEVENTEEN GATES HERE: `G01`–`G17`** |
| **S10** | `Step 8` | **The Review Panel** *(`Disciplines/00f`)* |
| **S11** | `Step 9` | **Record** — ⚠ including **`9.5`, the recording law** |
| **S12** | `Step 10` | **The readiness check.** ***Verify, do not assert*** |

## The gates, all inside `S09`

**`G01`–`G12`** are the carried gates **0–11**. **`G13`–`G17`** are the four new ones plus generator honesty:
**C** *(canon, federated)* · **F** *(frame integrity)* · **I** *(inheritance classification)* ·
**P** *(parent reconciliation)* · **G** *(generator honesty)*.

> ### ⚠ TWO GATES ARE KNOWN TO BE UNRUNNABLE AS THINGS STAND — do not read a pass as failing them
> - **`G07` (Gate 6, duplicates)** — ***structurally unrunnable in a cold pass by design.*** It needs the
>   siblings' completed material, which is exactly what the quarantine withholds. **`04` resolves this: it
>   runs LATE, at Step 7, when withheld files open. Until then run all four Part III.4 substitutes and SAY
>   SO.**
> - **`G16` (Gate P, parent reconciliation)** — **runs on a PARENT's pass, not a child's.** *(Traced
>   2026-09-03: no subnet has been written as a location, so this has never been runnable for an outer city.
>   That is a corpus state, not a pass failure.)*

---

# 3. WHAT IS AND IS NOT AUTHORITATIVE HERE

> ## ⛔ THESE 29 FILES ARE EXTRACTS. **THE SOURCE FILES ARE THE METHODOLOGY.**
> **Each unit carries its origin — `00_RUNBOOK.md` or `04_QA_Gates_and_Differentiation.md`, with line
> numbers.** ***If a unit file and its source disagree, THE SOURCE WINS, always.***
>
> **⚠ Do not edit the instruction text inside a unit file.** **If an instruction is wrong, fix it in the
> source and regenerate.** ***Two copies of a rule can diverge, and nothing here detects that*** — the same
> hazard `Disciplines/README.md` already names about its own copies.

## Still required, and NOT reproduced in these files

**A unit file is a step, not the whole contract. These continue to bind every unit:**

- **`CLAUDE.md`** — read the applicable runbook in full before location work; **methodology change ⇒ update
  the runbook AND the observations log, same commit, "both or neither"**; `graphify update` after modifying
  files; **American English**.
- **LAW 0 — depth over speed.** ***Do actual research rather than recalling. There is no credit for finishing
  quickly.*** **A unit that is "covered" is not a unit that is "done."**
- **`05` §6.1** — the circularity rule. **Conclusions are read LAST and read as a CHECK.**
- **`00_RUNBOOK.md` `§C.8a`** — the **EXCLUSION LIST**: `Current Status / Destruction`, `Connection to
  Concordia` and `Legacy` are **NOT INPUTS**, and their absence is never a gap.
- **`§C.8d`** — ⛔ **Concordia is not a yardstick for any other location.**

---

# 4. THE COMPANION FILES

| File | Use |
|---|---|
| **`../ULM_Input_Required_Reference.md`** | **THE BAR** — every input the method cannot produce, with an absolute address and a mechanical presence test. **Use it at `S01`** |
| **`../ULM_Input_Available_Audit.md`** | **THE MEASUREMENT** — 37 cities against that bar. ⚠ **Read its scope-corrections box first** |
| **`../Location_Data-Input_To-Do.md`** | **WHAT IS STILL MISSING**, ranked. ⚠ ***When the count and the tier disagree, the tier wins*** |
| **`../Test_Runs/OBSERVATIONS_and_Methodology_Findings.md`** | ⭐ **WHERE FINDINGS GO.** Continuous `M-` numbering, never restarted. **Currently at M-139** |
| **`../Pre-Contamination_Reviews/`** | Per-location quarantine state. ⚠ **Shirayuki's is `DRAFT`** |

---

# 5. THE STANDING LOG BLOCK

**Every unit file ends with the same block.** ***It is the deliverable, not a formality.*** **Two columns
carry the weight:**

- **"Raw evidence"** — a `path :: L<n>` or pasted output. ***Not a description of what was found.***
- **"Anything I had to decide that the instruction did not state"** — ⛔ **each entry is a question for the
  developer.** **If this column is never populated across a whole pass, it was not filled in honestly.**

> ## The one line to carry into every unit
> ***If you cannot find something, that is the result. Log it. Do not route around it, do not substitute, and
> do not proceed on a guess.***
