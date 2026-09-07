# Gate F — Frame integrity

> ## ⛔ THE RUNBOOK IS THE SOURCE OF TRUTH. **This file is an EXTRACT for step-wise execution.**
> **Origin: `04_QA_Gates_and_Differentiation.md` — lines 321–337.** ***If this file and the source ever disagree, THE SOURCE WINS.***
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
7. ⛔⛔⛔ **ONE LOCATION, ON ITS OWN TERMS — NEVER COMPARE ANY LOCATION TO ANY OTHER.** *(Binding law,
   developer ruling 2026-09-06. **Hand-synced into this card 2026-09-06** — the ruling landed on
   `00_RUNBOOK.md` and reached no card.)* ⛔ **No ranking, no z-scores, no "nth of N," no "unlike X," no other
   location as a control, baseline or implicit normal.** ✅ **Use this location's OWN figures, stated flatly.**
   ⭐ **RELATION stays legal** — *what this place needs from elsewhere, what flows, in which direction.*
   **The one-sentence test: delete every other location's name from the sentence; if the claim about THIS place
   survives, it was relation.** ⚠ **Scope is `ULM / CST / RWBEM`. District passes are untouched.**
8. ⛔⛔ **NO FORCED FIT — AN EMPTY SLOT IS A RESULT, NOT A GAP.** *(Binding law, developer ruling 2026-09-06.
   Hand-synced 2026-09-06.)* **Never force a location into a category it does not naturally occupy — and the
   error runs BOTH ways:** *assigning an existing roster member that does not fit, **or** inventing a bespoke
   one to fill a blank.* **Rosters are OPEN and expected to grow, so a roster's SIZE is never the test.**
   ✅ ***"None is sited here" must never read as "none is possible here."***

---

# THE INSTRUCTION

## Gate F — Frame integrity

**Does the pass stay inside its own declared frame?**

Four checks, each against a line of the Phase 0 declaration block:

1. **Type.** Did the pass answer the phases its type actually requires (`03` §0.1), or did it default to the
   Settlement set? **A Corridor written as a thin Settlement is the predictable failure**, and it shows up as a
   Phase 5 that is shorter than Phase 8.
2. **Band.** Is every claim scale-appropriate? **A Band 5 pass reading like a Band 3 pass has committed the
   scale error**, and a Band 1 pass that invents a general population has committed its inverse.
3. **Status.** Does a *declining* location read as declining, or as a healthy one with a sad note attached?
   Does a *ruined* one answer the Band 0 substitutions or the ordinary questions?
4. **Temporal frame.** Did post-frame facts leak in? **This has already happened in this project** — the city
   symbol assignments were first written partly from post-war facts when the subject was pre-war character, and
   had to be re-derived. **Sweep for the adjacent era's proper nouns specifically.**

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
