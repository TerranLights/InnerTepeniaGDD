# Gate C — Canon check, federated

> ## ⛔ THE RUNBOOK IS THE SOURCE OF TRUTH. **This file is an EXTRACT for step-wise execution.**
> **Origin: `04_QA_Gates_and_Differentiation.md` — lines 279–320.** ***If this file and the source ever disagree, THE SOURCE WINS.***
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

## Gate C — Canon check, federated

**Was the four-question canon check (`00_RUNBOOK.md` §E) actually run, against all three tiers?**

- **⚠ Was every search that produced a NEGATIVE result actually run across all three tiers — and can you name
  the search paths?** *(Strengthened 2026-08-30. The old wording asked only whether the universe repo was
  "opened deliberately," which a pass can answer yes to while every one of its actual sweeps stayed local.)*
  > **The measured case.** A city underwent **six** escalating integrity re-check passes, the sixth recorded as
  > *"genuinely clean, the first fully clean pass in this city's re-check history,"* having tried *"fresh grep
  > angles… **repo-wide**."* **Meanwhile the universe repo still listed the city's retired placeholder name as
  > a current city, and pointed at a directory path that had not existed since the rename.**
  >
  > **"Repo-wide" sounds exhaustive and is not.** The universe repo is not in the repo. **Six genuinely
  > rigorous passes each searched a space that structurally could not contain the remaining bugs, and each
  > returned a clean result that was true of the space searched and false of the world.**
  >
  > **So: a grep that never left this repo is not evidence about canon. It is evidence about one directory.**
  > **Name the paths, or the negative result does not count.**
- **Project canon checked against the source, not against the last pass that cited it?**
- **⚠ SHARED CONSTANTS — check at the SOURCE, never at the neighbors.** *(Added 2026-08-30, from a measured
  case: a wrong era length sat in **20 files across 8 locations**, including the city-culture template itself,
  and had been used as a causal premise in all of them.)*
  > **Does this pass use a figure that also appears in other locations' files — a duration, an era length, a
  > generation count, a population, a distance?** **If so, verify it against the timeline or spec that owns it.**
  >
  > **A shared constant is invisible to per-file checking by construction.** Every file agrees with every other
  > file, so any consistency check *between* them passes — and **agreement among siblings then reads as
  > corroboration**, so the error actively defends itself. **Gate 0 checks a file against its own claims;
  > this gate checks a claim against canon; neither one asks whether twenty files are wrong together.**
  >
  > **And when the corrected figure was carrying an argument, rebuild the argument — do not just renumber.**
  > In the measured case a cuisine finding was justified by *"feeding itself through a six-month polar night"*;
  > the real figure was ~60 days, and swapping the number in would have left a weak claim. **The actual
  > constraint — nothing grows on that continent in any season — was both true and stronger.**
- **Any thin-looking canon file checked for being a redirect stub** before concluding the canon is thin?
- **Rank order respected** where sources disagreed, with the contradiction stated rather than silently resolved?
- **Anything binding beyond this location** routed to RESERVED instead of decided here?
- **Anything genuinely new named, defined and cross-referenced** so it enters canon cleanly?

**Record which canon files were actually opened.** A pass that reports "checked canon" without naming files has
not run this gate.

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
