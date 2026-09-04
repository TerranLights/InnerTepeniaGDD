# ULM Disciplines — **interpretations, not replacements**

**Created 2026-09-03 at the developer's direction:** ***"you're not removing any of these from the District
Synthesis Methodology, right? What I want is for you to COPY (or, at least, INTERPRET) them to/for the ULM."***

---

# LAW 0 — DEPTH OVER SPEED. NEVER RUSH TO A FAST RESULT.

**Stated in full rather than cross-referenced, because a procedure that cites its governing law instead of
stating it will be run without it.**

**Worldbuilding is upstream of the entire project.** Every character, questline, faction, companion arc,
personal struggle, daily hardship, pastime and small joy is **downstream of decisions made here.** A shallow
location does not produce a shallow location — it produces shallow people living in it, shallow problems for
them to have, and shallow reasons for anyone to care. **The cost of going fast here is not paid here.** It is
paid later, everywhere, by work that cannot be fixed without coming back and redoing this.

**Therefore:**

- **Contemplate before writing.** The first plausible answer is usually the generic one, and a generic answer is
  worse than no answer because it occupies the slot.
- **Do actual research.** Not recalled, not inferred from a name. **The one controlled comparison this project
  has ever produced** — same location, same author, same day, at two researched picks and at six — found that
  **the two strongest findings came from picks four, five and six and did not exist at two.** The "redundant"
  picks were not redundant; four of them were the pass.
- **Chase nth-order effects.** For every finding ask **"and what does that cause?" three times.** First-order is
  the observation. Second-order is usually the interesting one. **Third-order is where the place stops
  resembling anywhere else.**
- **Go deep on the specific, not wide on the general.** One institution understood to its third-order
  consequences beats six sketched.
- **Take the time.** There is no deadline and no credit for finishing quickly.

## The anti-patterns this law exists to stop

1. **Producing a location because it is the next one**, rather than because it has been thought through.
   **Completion is not the goal; a place somebody could live in is the goal.**
2. **Skipping research by declaring it redundant.** Prioritizing by difference is a real rule and it is also
   *convenient*. **A pick is only redundant once you have actually looked at it. Redundancy asserted from a
   title is a guess wearing the costume of a method.**
3. **Treating "the phase is covered" as "the phase is done."** A finding that answers the template question is
   the floor, not the ceiling.
4. **Accepting the first coherent answer** because it fits and the pass is long.
5. **Letting the gates substitute for thinking.** They confirm a pass is not *wrong*. **None of them can tell
   you it is not thin.**

**And the companion failure — research used as decoration.** Doing the research is not the same as letting it
change anything. After each source, ask plainly: **did this change a finding, or ornament one?** Both answers
are honest and must be recorded differently. A citation attached to a conclusion that would have been written
anyway makes a thin pass look researched.

## The closing test

> **Could a person live an entire life here — and would that life be unlike a life in any comparable place?**

If the honest answer is *"probably, I suppose,"* the pass is not finished regardless of what the gates say.

> ### ⚠ Restated again, 2026-08-31, mid-Run-5 — because it needs to be heard again, not just cited
>
> **Developer instruction, verbatim, given directly during Sinheung's cold pass:**
>
> > *"Refining, fine-tuning, and perfecting this methodology is of absolute top-priority and importance to me.
> > If it takes a month to get it right, then we spend a month testing and refining it."*
>
> **What this adds, beyond what LAW 0 already says above:** it is not only that speed is not rewarded — it is
> that **there is no ceiling on how long this is allowed to take, and no session should treat a long runtime as
> a signal that something has gone wrong or that it should wrap up.** A pass, a phase, or a single finding that
> is still open after extensive work is not evidence of failure; stopping early to manufacture a sense of
> completion is the actual failure. **A future session reading this: you do not need to do this "quickly." You
> need to do it *right*.** If the honest, current state of the work is "still going," that is a legitimate and
> expected state, not a problem to paper over.

*(Copied here in full, verbatim, from `00_RUNBOOK.md`, 2026-09-03 — per developer instruction, after a live
session read this law once at the start of a run and still failed to follow it partway through. Placed at the
top of every ULM instruction file rather than cross-referenced, for the reason the law itself already states.)*

---


## What these files are

**The Universal Location Methodology needs five shared instruments that were written inside — and for — the
District Synthesis Methodology.** ***Those originals stay exactly as they are.*** **They carry their own
worked examples, from their own passes, and the district methodology has NO portability requirement and needs
that evidence.**

**These files are the ULM's own reading of the same rules:** **identical in substance, with every
location-specific worked instance replaced by a pointer.**

| ULM reads *(here)* | Original — authoritative, unchanged |
|---|---|
| `00b_General_Population_Discipline.md` | `../../Concordia-City/Districts/Phase_Instructions/00b_…` |
| `00d_Shadow_Proportion_Discipline.md` | `../../Concordia-City/Districts/Phase_Instructions/00d_…` |
| `00f_Review_Panel.md` | `../../Concordia-City/Districts/Phase_Instructions/00f_…` |
| `Cultural_Synthesis_Techniques.md` | `../../Cultural_Synthesis_Techniques.md` |
| `Real-World_Basis_Extrapolation_Method.md` | `../../Real-World_Basis_Extrapolation_Method.md` |

## Why the ULM cannot simply read the originals

**Two independent reasons, and either alone would be sufficient:**

1. **THE LAYERING LAW.** *(`../00_RUNBOOK.md`.)* **The ULM must be usable for any location in any universe.**
   ***An instrument naming this project's districts is not portable.***
2. ⛔ **CONTAMINATION.** **These are REQUIRED READING, and between them the originals carry conclusion-tier
   content about ~14 locations** — **none of it manifested in `06`.** **`CLAUDE.md` mandates reading required
   files in full, so every one of those is a leak with a guaranteed delivery mechanism** *(M-82's sixth
   instance; M-130)*.

> ### ⛔ THE ORIGINALS ARE THEREFORE `WITHHELD` FROM EVERY ULM COLD RUN.
> **Not because they are wrong — they are authoritative — but because they are dense with other locations'
> answers.** **They open at Step 7 with everything else.**

## ⚠ The cost this design accepts, stated plainly

> ## **TWO COPIES OF A RULE CAN DIVERGE, AND NOTHING HERE DETECTS THAT AUTOMATICALLY.**

**Each file below pins the original's `sha256` and line count at the moment it was derived.** ***Re-verify
before relying on one; a moved hash means the original changed and this interpretation may be stale.***
**Same mechanism as `§C.4`'s pin, applied to a rule instead of a map.**

**And the standing obligation, both directions:**
- **A change to an original → re-derive the interpretation here, same commit.**
- **A rule discovered here → it belongs in the original too, unless it is genuinely ULM-only** *(scale bands,
  location types, the frame declaration — things districts do not vary)*.
