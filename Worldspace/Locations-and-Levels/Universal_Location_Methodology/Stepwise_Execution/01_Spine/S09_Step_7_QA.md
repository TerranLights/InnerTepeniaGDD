# Step 7 — QA

> ## ⛔ THE RUNBOOK IS THE SOURCE OF TRUTH. **This file is an EXTRACT for step-wise execution.**
> **Origin: `00_RUNBOOK.md` — lines 2035–2066.** ***If this file and the source ever disagree, THE SOURCE WINS.***
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

`04` Parts I–II. Gates 0–11 carried, plus **C** (canon check, federated) · **F** (frame integrity) · **I** (inheritance classification) ·
**P** (parent reconciliation, on parent passes) · **G** (generator honesty).

**Paste raw scan output. Verify the instrument before trusting any zero. Report what Gate 11 cleared as well as
what it flagged.**

> ### ⚠ Verification is not only about zeros — the dangerous case is a plausible number
>
> **Broadened 2026-08-30 after a measured failure.** A census parse indexed the wrong column and reported
> **robot-only** retention as though it were combined. **It did not error.** It returned 33 plausible rows, a
> sensible mean, and a sensible spread — **all wrong.** A zero invites suspicion; *a plausible number does
> not.*
>
> **So:**
> 1. **Before trusting any computed figure, hand-check ONE row against the source.** Print the row, count the
>    columns, compare the number to the file. **Do this for plausible results especially.**
> 2. **Verify by spot-check, not by re-reading the logic.** The wrong column survived four readings of the
>    code and died instantly to one printed row.
>
> ### And score every quantitative claim against the full set, never the local group
>
> **A difference between two or three locations means nothing until you know how much locations differ in
> general.** *(Tri-Cities: a human-vs-robot retention gap looked like an excellent finding across three
> cities; scored against all 33 it sat at z = ±0.4 and was discarded. The combined-retention finding survived
> at z = −1.26 and z = +1.41.)*
>
> **Report the z-score, not the difference.** Without this, **any** small set of locations will appear to
> differ meaningfully on **any** metric — and a single-location pass needs this more, not less, since it has no
> siblings to sanity-check against.

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
