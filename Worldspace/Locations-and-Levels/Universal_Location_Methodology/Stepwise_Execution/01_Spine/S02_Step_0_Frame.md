# Step 0 — Frame

> ## ⛔ THE RUNBOOK IS THE SOURCE OF TRUTH. **This file is an EXTRACT for step-wise execution.**
> **Origin: `00_RUNBOOK.md` — lines 1869–1906.** ***If this file and the source ever disagree, THE SOURCE WINS.***
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

**0.1 Fill the declaration block** (`01` §6). Type and modifiers, **both** bands, status, temporal frame,
parent, children, sibling set. **Every line changes a later question.**

**0.2 Read the disciplines — ⛔ FROM `Disciplines/`, THE ULM'S OWN COPIES. Not the originals.**
`Disciplines/00b_General_Population_Discipline.md` *(and its Band-1 inversion, `01` §2.3)* ·
`Disciplines/00d_Shadow_Proportion_Discipline.md` · `Disciplines/00f_Review_Panel.md` ·
`Disciplines/Cultural_Synthesis_Techniques.md` · `Disciplines/Real-World_Basis_Extrapolation_Method.md`.
> ***The originals are UNCHANGED, authoritative for district work, and `WITHHELD` from a cold run*** — between
> them they carry worked instances for ~14 locations, which is a vector-1 leak for whatever subject is next
> *(M-130)*. **They open at Step 7 with everything else.** **See `Disciplines/README.md`.**

**0.3 Run Gate 0** — reconcile any completion claim against the file, **and the file's own open-questions list
against what has actually been resolved elsewhere.** Cheapest gate, highest yield, fails in both directions.

**0.4 Read everything the location already has, before writing over it.** Existing material predates whatever
disciplines have been written since, and inherited findings are where Gate 9 fires hardest.

> **⚠ And read it in this order, because "everything" can be twelve thousand lines.** *(Tri-Cities, 2026-08-30
> — the cluster carried ~4,000 lines per city before the universe repo was even opened, and an
> undifferentiated "read everything" is unrunnable at that volume.)*
>
> **1.** specs / physical facts → **2.** symbol assignment → **3.** composition, census, **and population
> change across census snapshots** → **4.** founding and events → **5.** the sibling set's differentiation
> instrument, if one exists → **6.** *last of all*, the location's own completed culture material.
>
> **Culture material is read last and read as a CHECK, never as an input** — see the circularity rule in
> `05` §6.1. A prior pass's *conclusions* about this same location are not evidence about it.

**0.5 Note reserved decisions and what would foreclose them** — and know you will probably find material
bearing on them anyway. **When you do: write it as a numbered finding, marked reserved**, stating what was
found, what it would decide, and that it is explicitly not adopted here. **A parenthesis is lost; a reserved
finding is a handoff.**

**0.6 State provisional assumptions about an unwritten parent** (`01` §5.2), and prefer building on physical
constraint over provisional inheritance wherever the choice exists.

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
