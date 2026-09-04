# Step −1 — The input contract, before the frame

> ## ⛔ THE RUNBOOK IS THE SOURCE OF TRUTH. **This file is an EXTRACT for step-wise execution.**
> **Origin: `00_RUNBOOK.md` — lines 1843–1868.** ***If this file and the source ever disagree, THE SOURCE WINS.***
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

**`05_The_Input_Contract.md`. Run its §7 pre-flight checklist first — it is the input-side equivalent of
Gate 0, and it is just as cheap.**

**The thing to internalize:** **all eight generators are inputs.** The methodology's entire spine is built from
material it cannot produce — physical facts, founding conditions, function, network position, composition,
events, symbol assignments. **This is the correct architecture** (a derivation engine cannot supply its own
axioms) but it means a pass that starts without its inputs will either stall or quietly invent.

**Four categories, and the two middle ones carry the rules:**

- **PROVIDED** — the method has no mechanism to generate it. **Missing ⇒ stub, assume provisionally, or block.**
- **RESERVED** — it *could* generate it, but authority is the developer's. **Missing ⇒ write fully around it**,
  per Step 0.5. Not the same behavior as PROVIDED, and confusing the two is the error.
- **PRODUCED** — the output, always as **Proposed:**.
- **REQUESTED** — **an output type.** When the pass needs something that does not exist, **emit a well-formed
  request rather than inventing.** A pass ending in three good requests has done real work; a pass ending in
  three quiet inventions has done damage that stays invisible until someone contradicts it.

**And the provenance rule, which specifically threatens any outside-AI input pipeline:** an input must not be
derived from this methodology's own output for the same location. **The district folder already found this
defect in miniature** — the Phase 5 counterculture seed works only when written by someone months earlier who
was not thinking about counterculture; written in the same pass it is *"planting your own seed and then finding
it."* **Track provenance direction, or the circularity becomes invisible.**

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
