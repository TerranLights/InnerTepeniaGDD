# Step 5 — Reconciliation *(and the CLOSE pass)*

> ## ⛔ THE RUNBOOK IS THE SOURCE OF TRUTH. **This file is an EXTRACT for step-wise execution.**
> **Origin: `00_RUNBOOK.md` — lines 1994–2028.** ***If this file and the source ever disagree, THE SOURCE WINS.***
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

> ### ⚠ This step is also where deferred complete-file checks close. `03` §0.4.
>
> **Draft order is not close order.** Phases are *written* 0 → 10, but a few checks are only meaningful against
> a **finished** file and cannot run inside the phase that owns them. **A phase that defers such a check is
> complete, not blocked** — it must never be held open "pending Phase Y" where Y comes later. **Work the
> close-pass docket at `03` §0.4 here**, and fold in any Zodiac Lens person-shaped results as explicit
> amendments to Phase 9. *(Added 2026-08-31, after Runs 6 and 7 were found generating false forward
> dependencies that this file never actually stated.)*

**Expect contradictions between generators, and between a generator and canon, to resolve both-are-true.** The
recurring shape: **one property producing two opposite effects on two different objects, or at two different
scales.** Do not ask which is true — ask **what single property would produce both**, then check whether the two
claims are about different objects.

**Canon outranks a generator.** State the contradiction and the reconciliation in the text; do not silently pick
one. **Where it genuinely cannot be reconciled, flag it open.**

> ### The strongest-finding check — run it here, retrospectively
>
> **Ask: *which finding in this pass is the strongest, and what does it rest on?***
>
> **`01` §5.2 rule 4 forbids building a location's single strongest finding on a provisional assumption about
> an unwritten parent.** That rule is easy to obey while writing a weak finding and hard to obey when the
> strong one arrives — **because you do not know which finding is strongest until the pass is nearly done.**
> Stated at declaration time it is advice; **stated here it is checkable.**
>
> *(Tri-Cities, 2026-08-30: the run's best finding — that a city is replaceable because the thing the parent
> actually needs is a design owned elsewhere — rested entirely on an assumption about a Band-6 parent that has
> never been written. Caught only because the question was asked at the end.)*

**Translation discipline:** the generator's vocabulary never appears in the location's own claims. Bracketed
citations only. **Sweep with word boundaries on every alternative and inspect every hit.**

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
