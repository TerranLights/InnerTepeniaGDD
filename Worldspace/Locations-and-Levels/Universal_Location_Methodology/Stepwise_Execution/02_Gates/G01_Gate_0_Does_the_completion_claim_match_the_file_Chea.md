# Gate 0 — Does the completion claim match the file? Cheapest gate, highest yield, fails in both

> ## ⛔ THE RUNBOOK IS THE SOURCE OF TRUTH. **This file is an EXTRACT for step-wise execution.**
> **Origin: `04_QA_Gates_and_Differentiation.md` — lines 102–107.** ***If this file and the source ever disagree, THE SOURCE WINS.***
> **Do not edit the instruction text below. If it is wrong, fix it in `04_QA_Gates_and_Differentiation.md` and re-extract.**

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

**Gate 0 — Does the completion claim match the file?** Cheapest gate, highest yield, **fails in both
directions.** Reconcile the tracker's claim against the file *and* the file's own open-questions list against
what has actually been resolved elsewhere. **A file's self-reported status is unreliable in both directions:
check the target, never the claim.** And when a phase is added to this methodology, **every location already
marked complete reverts to incomplete for that phase.**

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
