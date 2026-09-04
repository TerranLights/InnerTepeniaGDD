# Gate I — Inheritance classification

> ## ⛔ THE RUNBOOK IS THE SOURCE OF TRUTH. **This file is an EXTRACT for step-wise execution.**
> **Origin: `04_QA_Gates_and_Differentiation.md` — lines 338–367.** ***If this file and the source ever disagree, THE SOURCE WINS.***
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

## Gate I — Inheritance classification

**Is every element correctly classed?** *(`01` §5.1: determined · inflected · originated · aggregated.)*

Two failures, in opposite directions, and both are common:

- **Inventing a local variant of something the parent determines.** A sub-location does not have its own
  climate, currency or calendar. If the pass produced one, it is wrong — not thin, *wrong*.
- **Claiming origination for something inherited.** This is how two siblings independently "invent" the same
  custom: both actually inflected the same parental form and neither noticed.

**The check:** walk the pass's named institutions and customs and assign each a class explicitly. **Anything
classed *originated* goes to Gate 6.** Anything that cannot be classed is a flag — usually it means the parent's
position on it is genuinely unwritten, which belongs in the provisional-assumptions list rather than being
silently decided here.

> ### ⭐ The count is the diagnostic — and this gate correctly predicted its own failure mode, on a real case
> **Added 2026-08-30.** `01` §5.1 warns that **Inflected is the workhorse and is systematically under-used**,
> and that a pass skipping it *"is working harder for a worse result."*
>
> **A real cold pass produced a lopsided ratio — several Originated elements against exactly one Inflected
> one.** **That ratio is the tell, and it is countable — so make it part of the gate rather than a matter of
> judgment.** *(The specific counts and the recurring miss they revealed — a purely local holiday invented
> without ever checking what the location does with a national observance — are archived in
> `Test_Runs/Worked_Examples_Archive/`.)*
>
> **So: count the classes. If Originated outnumbers Inflected by more than about 3:1, stop and re-run the
> `01` §5.1 order of attempts** — *what does the parent determine → what does it supply that this place
> inflects → who arrived carrying one → is the place already doing it somewhere → only then invent.*

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
