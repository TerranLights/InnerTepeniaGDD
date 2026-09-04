# Gate 9 — Asymmetry

> ## ⛔ THE RUNBOOK IS THE SOURCE OF TRUTH. **This file is an EXTRACT for step-wise execution.**
> **Origin: `04_QA_Gates_and_Differentiation.md` — lines 208–229.** ***If this file and the source ever disagree, THE SOURCE WINS.***
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

**Gate 9 — Asymmetry.** For every finding describing a **threshold, gate, conversion, verdict, admission or
status change**: *the mechanism runs both ways — did the file write both?* Ask what happens to someone the
mechanism decides **against**, whether that outcome is as durable, and **whether there is any route back.**
**A "no route back" nobody has perceived as a problem is a textbook shadow.**
> **Runs twice: on inherited material before writing, and on the thresholds this pass itself just wrote.** It
> has an extremely high hit rate against inherited material and has barely been tested against material written
> under a methodology that knows about it. **A pass reporting Gate 9 firing only on inherited material has
> probably not run the second pass.**
>
> ### ⭐ First recorded second-pass fire — 2026-08-30
> **The second pass works, and here is the shape it produced on a real test case, because the shape is
> reusable.** A membership threshold was written entirely from the favorable side, in a pass whose author had
> read this gate that morning. **The gate's question — *what happens to someone it decides against, and is
> there a route back?* — had no answer, and finding one produced the pass's second-strongest finding.**
> *(The specific worked case is archived in `Test_Runs/Worked_Examples_Archive/`.)*
>
> > **The transferable pattern: a membership mechanism with no author has no appeal process either**, and
> > **that is a textbook `00d` shadow — unintended, unnoticed, discoverable, and working with everyone acting
> > in good faith.** **Run Gate 9 against every membership, promotion or admission mechanism a pass writes.**
> > The favorable path is the one that gets written; the gate exists because it is also the only one that
> > feels like it needs writing.

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
