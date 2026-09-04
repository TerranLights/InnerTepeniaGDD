# Gate 11 — Plausibility

> ## ⛔ THE RUNBOOK IS THE SOURCE OF TRUTH. **This file is an EXTRACT for step-wise execution.**
> **Origin: `04_QA_Gates_and_Differentiation.md` — lines 239–274.** ***If this file and the source ever disagree, THE SOURCE WINS.***
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

**Gate 11 — Plausibility.** The one direction the others cannot look. **Every other gate checks a relation
between two things already inside the project.** Take the strongest findings and ask, in order: **would a person
actually do this** · **at this cost, priced in this location's physical conditions** · **for this reason** ·
and **whose behavior am I actually describing?**
> **The scale question, which is three of the seven recorded developer catches in one sentence:**
> **What population, over what span, does my source actually describe — and am I asserting it of a larger one?**
> **This is the weakest gate on the list and it should be reported as such.** A self-audit runs it with the same
> faculty that produced the error. **Record what it flagged *and* what it cleared**, so a later external catch
> can be checked against whether this gate looked at it.
>
> ### ⭐ FIRST RECORDED FIRE — 2026-08-30, on a real test case, and it was found by ARITHMETIC
>
> **This gate had never caught anything before this.** It caught two things at once, and the method is worth
> copying exactly, because it required no judgment at all:
>
> **Divide the population by the area. That is the whole technique.**
>
> A cold pass had spent nine phases describing a scattered, low-density settlement, complete with real-world
> comparanda scaled to a small population — and the arithmetic showed a population an order of magnitude denser
> than the pass's own prose implied, comparable to some of the densest real cities on Earth, with comparanda
> that had been asserted of a population far smaller than the one actually being described: the exact form of
> the scale question above. **Both corrections improved the material** — the pass's own texture findings
> survived the correction and came out sharper for it, not weaker. *(The full worked figures — the actual
> density computed, the real-world comparanda used, and exactly what got corrected — are archived in
> `Test_Runs/Worked_Examples_Archive/`.)*
>
> > **The transferable rule: before trusting any texture claim, price it against a density figure.** Population
> > over extent is one division, it needs no interpretation, and **it is the only part of this gate that does
> > not run on the same faculty that produced the error.** **Run it every time, early.**
> >
> > *(Note the redundancy that worked: the same pass's own Phase 0 had already caught the same problem, by
> > declaring a divergence between its population band and its extent band. **Two different instruments, two
> > different stages, same catch.** Declaring both bands — `01` §2 — is the cheaper of the two.)*

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
