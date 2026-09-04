# Step 9 — Record

> ## ⛔ THE RUNBOOK IS THE SOURCE OF TRUTH. **This file is an EXTRACT for step-wise execution.**
> **Origin: `00_RUNBOOK.md` — lines 2089–2148.** ***If this file and the source ever disagree, THE SOURCE WINS.***
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

1. Append the **QA block** and the **Review Panel block**.
2. Add the location's **row to its differentiation set, in the same commit.**
   ⭐ **Cities → `…/Cities/Cross_City_Culture_Differentiation_Table.md`** *(full path in Step 6)*. **Districts
   → `Cross_District_Differentiation_Table.md`.** ***One AXIS per cell, never the content.***
   ⚠ **And if this pass noticed anything about ANOTHER city, record that here too** — `04` III.0:
   ***propagation is part of the finding, not a follow-up.*** *(A symbol collision was once noticed correctly,
   filed in one city's own culture file, and never reached the guide whose entire job was catching it.)*
3. Update whatever tracker claims completion — **per Gate 0, list what the file actually contains, not a summary
   claim.**
   > ### ⛔ **BUT PUT THE FINDING IN THE OBSERVATIONS LOG, NOT IN THE TRACKER.** *(M-109.)*
   > **Gate 0's concern is OVERCLAIMING COMPLETION. It is not a license to write substance into a queue.**
   > ***A tracker entry is: what remains to be done, one line, plus a pointer to where the detail lives.***
   > **The finding itself goes to `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` and nowhere else.**
   > **If you have written more than ~3 lines into a tracker, you are writing in the wrong file.**
4. **If this pass changed the methodology, update these files in the same commit**, and record **what was
   learned and on which location.** A methodology change that does not update the runbook has not been made —
   the next pass will follow the runbook, not the commit message.

## 9.5 — THE RECORDING LAW: log everything that happened, not everything that worked

**Developer instruction, 2026-08-30 (Run 3, Zhongshan), stated twice in one session. Binding on every pass, not
only on test runs.** The shared log is
**`Test_Runs/OBSERVATIONS_and_Methodology_Findings.md`**, which carries the full statement.

> **Record every finding — and "finding" does not mean "successful technique."** It means, in the developer's
> own enumeration: **ways of achieving results, snags, problems, unintended blockages, etc., etc., etc.**

**What that covers in practice:**

- **Techniques that worked** — and *why* they worked, not merely that they did.
- **Snags** — anything that slowed the pass, however trivial-seeming.
- **Problems and unintended blockages** — a step that could not be run, and **what stopped it.**
- **Contradictions between two instructions inside this methodology.** *(Run 3 found three.)*
- **Dead ends**, and the exact point at which each died.
- **Killed findings** — an attractive result destroyed by its own evidence. ***The most valuable entries in the
  file.*** Run 1's best moment was a finding killed by its own arithmetic; Run 3's was the same.
- **Self-corrections** — written as *what you believed · why it was wrong · what changed it.*
- **Environmental and tooling obstacles** — a hook, a stale index, a missing file, a `CLAUDE.md` rule that
  conflicts with a rule in here.
- **Anything merely unclear**, even where the guess turned out right.

**Three procedural rules, each already violated at least once:**

1. **Write it when it happens.** Precision decays; a snag logged hours later has lost the file, the wording, and
   the reason it mattered.
2. **Log the failure even when you routed around it.** **Solving a problem privately is how a methodology stays
   broken.**
3. **Never compress a negative result into a positive one.** *"Checked the census, all fine"* destroys what
   *"the parse read the wrong column and returned plausible numbers; only a printed row caught it"* preserves.

**Number entries `M-n` continuously across all runs; never restart per run** — recurrence across runs is much
stronger evidence than a single sighting, and only continuous numbering makes it visible.

> **The location is the whetstone; the methodology is the deliverable.** **A pass that produces a beautiful
> location and a thin observations log has failed at the thing it was for.**

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
