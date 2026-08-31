## ⚠ MANDATORY — District / location culture synthesis

**Two separate methodologies exist for this. Use the right one — they are not interchangeable.**

- **A Concordia district** (any of the 13) — use the **district-specific methodology**,
  `Worldspace/Locations-and-Levels/Concordia-City/Districts/Phase_Instructions/00_RUNBOOK.md`. **This is the one
  to use for districts.** It is battle-tested and fire-tested: built from 13 real passes, carries the specific
  errors that shaped every one of its rules, and has a verified track record. Nothing below changes this — the
  district runbook remains the authority for district work.
- **Any other location** — a city, subnet, nation, orbital-infrastructure unit, highway, structure, vessel,
  ruin, or anything not a Concordia district — use the **Universal Location Methodology**,
  `Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md`. **Added 2026-08-30. Status:
  working draft, unvalidated** — built by generalizing the district method's findings, but not yet pressure-tested
  against a real location. Use it, but treat its results as provisional until it has a track record of its own.

**Any work on a district's, city's, or location's local culture — a new pass, an edit to an existing
`Full_Extrapolation.md`, a phase, a QA gate, a Review Panel run, or a methodology change — MUST begin by reading
the applicable runbook above, in full, before touching anything else.**

**This is not a suggestion and not a "consult if unsure."** The runbook is the operational procedure, and it
exists so the method never has to be reconstructed from the phase files, the substrate folder, or the index's
historical round-notes — reconstructing it from those is how the errors below happened.

**The two runbooks have different shapes. Do not carry one's structure onto the other:**

| | **District runbook** | **Universal Location Methodology** |
|---|---|---|
| Ordered steps | **eight** | **twelve — Step −1 through Step 10** |
| QA gates | **eleven, 0–10** | **sixteen — 0–11 plus C · F · I · P · G** |
| Phases | 8 | **11** |
| Review Panel dispositions | **five** | **six** — `accepted · noted · rejected · refereed · unmet · declined` *(the `unmet`/`declined` split added 2026-08-30; see `00f`)* |
| Ends with | Record | **Step 10 — the READINESS CHECK, run before declaring a pass complete or handing off** |

> **⚠ Two standing steps in the Universal methodology are easy to skip and are not optional:**
> **Step 9.5 — the recording law** *(log snags, blockages, dead ends, killed findings and self-corrections, not
> just successes)* and **Step 10 — the readiness check** *(verify, do not assert; on its first use it caught the
> largest hole in the anti-contamination protocol)*. **Both were added at the developer's direction,
> 2026-08-30.**

**Do not skip it because the task looks small.** Every failure recorded in this methodology was found during
work that looked small: a completion claim that was false for two weeks, a general-population error still live
six weeks after the discipline file was written about it, and two districts given the same custom a day apart.

### ⚠ LAW 0 — DEPTH OVER SPEED. NEVER RUSH TO A FAST RESULT.

**Standing law. It overrides every other instruction in this section, and applies to all worldbuilding, not only
to districts.**

**Everything in this universe is downstream of its worldbuilding** — every character, questline, faction,
companion arc, personal struggle, daily hardship and small joy. **A shallow location produces shallow people
living in it and shallow reasons to care about them**, and the cost is not paid at the time; it is paid later,
everywhere, by work that cannot be fixed without coming back and redoing the foundation.

**So: contemplate before writing. Do actual web research rather than recalling. Chase nth-order effects — for
every finding ask "and what does that cause?" three times, because the third-order answer is where a place stops
resembling anywhere else. Go deep on the specific rather than wide on the general. Take the time.**

**There is no credit for finishing quickly.** Completion is not the goal; **a place somebody could live in is
the goal.** The QA gates can confirm a pass is not *wrong*; **none of them can tell you it is thin.**

### Non-negotiables the runbook will re-state, listed here so they are never a surprise

- **`Cross_District_Differentiation_Table.md` — read the relevant row BEFORE writing a category, and add the
  district's column in the SAME COMMIT that completes it.** It is the only mechanical guard against thirteen
  districts quietly converging, and Gate 6b has already failed once without it.
- **Paste raw QA scan output into the QA block. Never summarize it.** Self-audit error in this project has run
  in **one direction — toward flattering the pass — on every occasion it has been measured** (four instances
  across two districts, after the rule against it was already written).
- **A Review Panel position is not guaranteed to get what it wants.** If satisfying an objection would make the
  district more like the other twelve, the disposition is **`unmet`** and the refusal is written as
  characterization, not as a gap to close.
- **Real-world inspirations are sources, not specifications.** A location is under no obligation to match its
  inspiration; divergence is fine and often better. **The two tests that bind are internal** — is it
  characteristically consistent with *itself*, and is it consistent in-world within the Tepenian universe? A
  striking real fact is not automatically a district fact.
- **Never carry one location's answers into another.** If two places produce similar-shaped answers to the same
  technique, at least one is wrong.

### If the work is a methodology change rather than a district pass

Update the runbook **in the same commit**, and record *what was learned and on which district*. The index's
dated round-summaries are the historical record; the runbook is the working procedure. **Both, or neither.**

---

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
