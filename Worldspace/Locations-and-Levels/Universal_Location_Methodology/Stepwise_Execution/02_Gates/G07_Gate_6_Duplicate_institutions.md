# Gate 6 — Duplicate institutions

> ## ⛔ THE RUNBOOK IS THE SOURCE OF TRUTH. **This file is an EXTRACT for step-wise execution.**
> **Origin: `04_QA_Gates_and_Differentiation.md` — lines 151–200.** ***If this file and the source ever disagree, THE SOURCE WINS.***
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

**Gate 6 — Duplicate institutions.** Within the location, and against completed siblings. **Uses the
differentiation instrument in Part III.** **Check the most recently written sibling first** — collisions cluster
there, because whatever was most recently solved is the nearest available shape and it gets reached for. **State
the contrast inline, in the finding itself**, not in a footnote.
> ### ⚠ Gate 6 is UNRUNNABLE in a cold pass, by construction — a scheduling problem, not a failure
> **Added 2026-08-30.** Gate 6 needs the siblings' completed material and the differentiation instrument. **In
> a cold or anti-contamination pass that material is precisely what is withheld.** **The anti-convergence gate
> and the circularity rule are in direct conflict, and one of them must lose.**
>
> **Resolution: Gate 6 runs LATE — at Step 7, when the withheld files are opened — not never.** Until then run
> **all four** Part III.4 substitutes and say in the pass that you did.
>
> **And an encouraging result worth recording, from a real test case.** When Gate 6 finally ran on one cold
> pass it found two collisions with the location's own existing canon — **and Gate 4's swap test had already
> independently flagged one of them as the pass's weakest finding and demoted it, while that canon was still
> invisible.** **The blind instrument caught what the sighted one later confirmed.** **Gate 4 is therefore
> partial cover for a deferred Gate 6 and should be run deliberately as such** — pick the swap partner most
> likely to expose a shared answer. *(The specific collisions are archived in
> `Test_Runs/Worked_Examples_Archive/`.)*
>
> ### ⚠⚠ Before recording ANY mismatch found at Step 7 as wrong or killed, run the both-are-true test (`02` §5.3)
> **Added 2026-08-31, at the developer's direct instruction after a first draft got this wrong on a real case.**
> A deferred Gate 6 does not only find duplicates — opening withheld material at Step 7 routinely surfaces
> outright **contradictions** between a cold pass's own findings and established canon. **The reflex is to
> declare the cold finding killed. That reflex is the error, not the contradiction.**
>
> **`02` §5.3's both-are-true test was written for generator-vs-generator conflict, but nothing previously said
> it also governs pass-vs-canon conflict at Step 7 — and it should, for exactly the same reason.** *"Do not ask
> which reading is right. Ask what single property would produce both, then check whether the two claims are
> about different objects or at different scales."* A contradiction between a cold pass's claim and an opened
> culture file is very often not a wrongness but a **scale mismatch** — public vs. private, mainstream vs.
> counterculture, an older generation vs. a newer one, a legal/procedural fact vs. a narrative/emotional one.
> **The candidate scales to check, in order, before concluding a kill:**
> 1. Public-facing / mainstream vs. private / minority-community.
> 2. The dominant culture vs. its own named counterculture.
> 3. An earlier generation vs. a later one (heritage drift, memory loss, or accumulation over time).
> 4. A legal/procedural/structural fact vs. a narrative/emotional/mythic one describing the same event.
>
> **A flat kill discards a finding entirely. Applying the test instead looks for the reconciling property —
> very often already written down in the same source that produced the contradiction — before concluding the
> cold pass's claim was simply wrong.** A real worked case, archived in
> `Test_Runs/Worked_Examples_Archive/`, found the property relocated a demographic-diversity
> finding from a public/general scale (where existing canon contradicted it) to a private/generational scale
> (where it was not contradicted, and became a sharper finding than either the original claim or the killed
> version).
>
> **This does not mean every mismatch reconciles.** Some genuinely are wrong at every scale checked — **the
> test is a required check before declaring a kill, not a guarantee against one.** `00f`'s `refereed`
> disposition is the Review Panel's version of the identical instinct and should be read alongside this note.

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
