# Step 10 — THE READINESS CHECK

> ## ⛔ THE RUNBOOK IS THE SOURCE OF TRUTH. **This file is an EXTRACT for step-wise execution.**
> **Origin: `00_RUNBOOK.md` — lines 2132–2222.** ***If this file and the source ever disagree, THE SOURCE WINS.***
> **Do not edit the instruction text below. If it is wrong, fix it in `00_RUNBOOK.md` and re-extract.**

## ⛔ RULES FOR RUNNING THIS STEP — they are the same every time

1. **DO THIS STEP ONLY. STOP AT THE END.** Do not begin the next one. **Report, then wait.**
2. **PASTE RAW OUTPUT. NEVER SUMMARIZE IT.** *(`00_RUNBOOK.md` Step 7; `04` Gate 1.)* **A summary of a scan
   is not evidence that the scan ran.**
3. ⛔ **DO NOT SUPPLY A CRITERION THE INSTRUCTION DOES NOT STATE.** ***If you find yourself deciding what
   "should" exist, STOP AND ASK.*** **Every false finding on record came from this.**
4. ⛔ **DO NOT EDIT ANY FILE** unless this step's own text tells you to write something. **Finding a defect
   is not authorization to fix it.**
5. **If you cannot find something, that is the result.** **Log it. Do not route around it, do not substitute,
   do not proceed on a guess.**
6. **AMERICAN ENGLISH.** *(Global `CLAUDE.md`.)*

---

# THE INSTRUCTION

**Standing step, added 2026-08-30 at the developer's direction. Run it before declaring a pass complete and
before handing off to another session.**

> ## The governing principle: **VERIFY, DO NOT ASSERT.**
>
> ***"Everything is ready"* is a claim, and it requires evidence like any other.** The check exists because a
> handoff feels finished long before it is, and because **the person best placed to declare readiness is the
> one who can no longer see what they have absorbed.**
>
> **On its first use it caught the single largest hole in the anti-contamination protocol** — see below. **It
> is not a formality.**

## 10.1 Contamination surface — the half that has actually caught something

**Run these against the NEXT pass's subject location, not this one's.**

1. **⚠ Scan auto-loaded memory for the subject location.** *(The check that found M-21.)* Every hit must be
   **attribute-only** — founding, dates, names, census, corrections, open questions — **or carry a
   contamination banner.** **An entry stating the place's character, temperament, personality triple, or a
   signature phrase is a live vector**, because memory is *pushed* into a session rather than pulled by it.
   **Fix the entry or band it. Nothing else will.**
   > **⚠ Corrected 2026-09-02, Run 12.** This item used to call memory *"the only vector no do-not-open list
   > can intercept."* **That was wrong, and the error was load-bearing** — it implied the surface was closed
   > once memory was checked. **There are at least three**: memory, **the required reading itself** (1a), and
   > **filenames** (1b). **All three are pushed rather than pulled, and Run 12 was burned by all three at
   > once.**

   **1a. ⚠ Scan the REQUIRED READING for the next subject's name** — `00`–`06`, `README`, and **everything in
   `Disciplines/`** *(the ULM's own copies — the originals are withheld, not read)*.
   **Return line numbers, band or neutralize every hit, and manifest it in
   `06`.** **`CLAUDE.md` mandates these files be read in full, so a worked example naming the next subject is
   a guaranteed leak with a mandatory delivery mechanism.** ***This has now failed three times — M-82 (Sanay),
   and twice more on Run 12*** — **which is why Step −2 has a reader scan them rather than trusting `06`.**

   **1b. ⚠ Sanitize the file tree.** **Check whether any file or folder the next run must navigate is
   *titled* with a claim about the location.** **If so, the handoff carries sanitized paths** — directory,
   file count, line counts — **never the filenames.** *(Vector 3, Run 12: eleven vignette filenames, each a
   thesis, delivered by a single mandated `ls`.)*

   **1c. ⚠⚠ GREP YOUR OWN NEW PROSE FOR THE SUBJECT'S NAME, BEFORE COMMITTING.** **For every hit ask: does
   this state the leak's SHAPE, or its CONTENT?** ***Shape is the lesson. Content is the leak.***
   **"Eleven titles, four naming civic facts" teaches everything; the four facts teach nothing and
   contaminate.** *(M-97 — the rule against vector 1 recreated vector 1, inside the section documenting vector
   1, in the same session that fixed it. **No gate caught it.** It surfaced only because the developer asked
   the session to account for its own exposure.)*
   > **Why this needs to be mechanical rather than an exhortation:** ***a rule that leaks is more persuasive
   > than one that does not, because it shows its evidence.*** **The incentive runs toward contamination.**

2. **Update `06_Worked_Example_Provenance.md` with any worked examples this pass added to the methodology.**
   An unmanifested example is invisible contamination for the next same-location run.
3. **Confirm the quarantine list was built by RULE, not by recall** — `05` §6.1's content split applied section
   by section. **A list assembled from memory is written by the one person who has already read everything.**
4. **Open the header of every file on the admissible list and check its own cited sources.** A file that cites
   a withheld document is downstream of it, whatever its filename says. **Seconds per file, and it would have
   caught both of Run 3's contamination events.**
5. **Confirm any corpus-wide retrieval layer is flagged as unusable** — a graph, an embedding index, a
   full-text search cannot honor a quarantine, because quarantine is provenance and retrieval is content.

## 10.2 Path and structure integrity

6. **Every path named in the handoff exists** — admissible and withheld alike. A withheld path that has moved
   is a quarantine hole.
7. **The next run's output folder does NOT already exist.** It creates its own; a pre-seeded folder is a
   contamination risk and a status lie.
8. **The shared observations file sits OUTSIDE every quarantined folder**, or the next run cannot write to it
   without breaking its own quarantine *(M-0)*.

## 10.3 Record integrity

9. **Run Gate 0 outward:** does every tracker's completion claim match what the files actually contain?
   **List what the file contains, never a summary claim.**
10. **Confirm findings were IMPLEMENTED, not merely recorded.** A finding logged in the observations file and
    absent from the rule it should have changed has not been made — **the next pass follows the rules, not the
    log.**
11. **Check the handoff states what the next run CANNOT prove**, as well as what it can. A run whose limits are
    undeclared will be over-read.

## What it caught the first time it was run

**Asked whether a handoff was ready, the honest response was to check rather than answer — and the check found
that a memory entry recording an analytical *technique* had inlined its own per-city results**, including a
withheld personality read and a quarantined axis phrase, verbatim, in the auto-loaded index. **Ten further
entries carried conclusion vocabulary about the same cluster.**

> **The declaration "everything is prepared" would have been wrong, and the cold run it authorized would have
> produced a confident, coherent, contaminated result — precisely the failure the protocol exists to prevent.**

---

---

# EXECUTION LOG — fill this in, then stop

**Location:** ____________  **Date:** ____________  **Frame:** Second Interwar (default)

| # | What the instruction demanded | Where it said to look | Found? | Raw evidence — `path :: L<n>` or pasted output |
|--:|---|---|:--:|---|
| 1 | | | | |
| 2 | | | | |

**Anything the instruction demanded that could NOT be found:**
-

**Anything I had to decide that the instruction did not state** *(⛔ each one is a question for the developer,
not a judgment call)*:
-

**Verdict:** ☐ step complete  ☐ blocked — cannot proceed without: ____________

> ### ⚠ BEFORE REPORTING, CHECK THE TWO THAT ARE ALWAYS FORGOTTEN
> ☐ **Did this step change the methodology?** → **it goes in `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md`
> with the next continuous `M-` number, IN THE SAME COMMIT.** *(`CLAUDE.md`: "Both, or neither.")*
> ☐ **Did I modify any file?** → **`graphify update .`** *(`CLAUDE.md`.)*
