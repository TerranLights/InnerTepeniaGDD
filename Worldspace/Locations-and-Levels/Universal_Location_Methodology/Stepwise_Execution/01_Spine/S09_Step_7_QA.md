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
> ### ⛔⛔ NO SCORE OF ANY KIND IN-RUN — **REPLACED 2026-09-06.** *Hand-synced from `02` §G8 rule 1.*
>
> **The rule used to read:** *"score against the full set, never the local group — report the z-score… a
> single-location pass needs this more, not less, since it has no siblings to sanity-check against."*
> ⛔ **A z-score is a rank, a rank is a comparison, and no city is ever compared to any other city**
> *(`00_RUNBOOK.md`, THE LAW OF ONE LOCATION; developer ruling 2026-09-06)*.
>
> ⭐ **REPORT THE LOCATION'S OWN PERCENTAGE, FLATLY** — *"retained `61.81%`; `H` `58.31%` against `R` `65.17%`,
> a spread of `+6.86 pp`"* — **and then ask what THAT number means for THIS place**, which is the question the
> z-score was always standing in front of.
> ⏸️ **TERMINAL:** *cross-city scoring returns at the end of the corpus, when a full set actually exists.*

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
