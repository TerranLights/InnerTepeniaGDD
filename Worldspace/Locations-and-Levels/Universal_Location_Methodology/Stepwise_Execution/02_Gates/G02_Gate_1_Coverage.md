# Gate 1 — Coverage

> ## ⛔ THE RUNBOOK IS THE SOURCE OF TRUTH. **This file is an EXTRACT for step-wise execution.**
> **Origin: `04_QA_Gates_and_Differentiation.md` — lines 108–124.** ***If this file and the source ever disagree, THE SOURCE WINS.***
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

**Gate 1 — Coverage.** Confirm each applicable phase is *answered*, not gestured at.
> **The instrument-verification discipline is the important half, and it is fully general.** A mechanical scan
> is worthless until you have proved it could have found a hit. Recorded defects, every one found by content
> that existed and scored zero: **whole words that miss their own stems** (`funeral` does not match *funerary*);
> **terms never on the list at all** (`mortuary`); **a register the list did not anticipate** (`mourn` misses
> *grief*, *grieving*, *bereavement*); **a character** (an en dash breaking `human-robot`); and **a strip
> boundary that silently captured the wrong section.**
> **So: before drawing any conclusion from an absence, run the scan against a case you know contains a hit. If
> it does not find that one, it has not found anything.** Prefer stems. Normalize dashes. **And paste the raw
> counts into the QA block — do not summarize them**, because an instruction to read carefully does not survive
> an author grading their own work.

**Three outcomes per term, not two, and a fourth that must not be conflated with the third:**
*pass* · *fail* · **covered in substance, absent in term** *(normal, and usually a sign the location has found
its own register)* · **absent and unexplained** *(a genuine hole)*. **The test is one question: does the pass say
why the thing is missing?** **Never insert a word to make the scan pass.**

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
