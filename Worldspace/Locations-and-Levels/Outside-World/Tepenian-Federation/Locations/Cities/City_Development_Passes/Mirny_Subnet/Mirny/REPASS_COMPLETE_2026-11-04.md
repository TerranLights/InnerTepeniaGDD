# Mirny repass: complete (2026-11-04)

**Order (developer, 2026-11-03 night):** recheck all of Mirny's data so nothing has drifted; go one unit at a time; anything that needs the developer goes to `Research_Logs/DECISIONS_NEEDED_FROM_DEVELOPER.md`. On 2026-11-04 the developer added: "continue thro all the steps ... we'll address later" and "We go until 3 pm". Units U0 to U9 ran between 05:20 and 11:20; U10 and U11 (Steps 9/9.5 and Step 10) were added at 11:30 after the developer asked "What about the rest of it?" and finished at about 12:55. U5 to U11 ran at the same time, not one after another (see DEC-101).

**What was and was not touched:** no pass file, no culture file, no shared table and no discipline file was edited; nothing was committed or pushed. Every result is a new append-only file (`DR-74`), marked PROPOSED, and every piece went through three independent Opus readers, a mechanical field check (Round 2), a cross-check (Round 3), a merge, a quotation audit and an American English sweep. The two modified files in the working tree at session start (the amendment register and the perk file) and the handoff note were not part of this repass, except the register edits recorded under U1.

## The twelve units
| Unit | What | Result files (all in this folder) | Decisions |
|---|---|---|---|
| U0 | Data recheck | `REPASS_U00_Data_Recheck_2026-11-04.md` (six tools clean; four small drifts; none changes a finding) | none |
| U1 | Phase 8 dockets | `Amendment_Dockets_P08_Making_2026-11-04.md`; `DR-56_Amendment_Register_2026-10-13.md` (section 2c) | none |
| U2 | Idelsk-Uralia piece | `Amendment_Rederivation_PIU_IdelskUralia_2026-11-04*.md` | DEC-005 to DEC-008 |
| U3 | Robot-term piece | `Amendment_Rederivation_PRT_RobotTerm_2026-11-04*.md` | DEC-009, DEC-010 |
| U4 | Phase 9 (Populations) | `Amendment_Rederivation_P9_Populations_2026-11-04*.md` | DEC-011, DEC-012 |
| U5 | Phase 10 (Catalog) | `Amendment_Rederivation_P10_Catalog_2026-11-04*.md` | DEC-013 to DEC-016; DEC-007 recommendation changed to "leave unmapped" |
| U6 | Step 5 (Reconciliation) | `Amendment_Rederivation_S5_Reconciliation_2026-11-04*.md` | DEC-020, DEC-021 |
| U7 | Step 6 (Differentiation, Mirny's own row) | `Amendment_Rederivation_ST6_Differentiation_2026-11-04*.md` | DEC-040 to DEC-042 |
| U8 | Step 7 (the 17 QA gates) | `Amendment_Rederivation_ST7_QAGates_2026-11-04*.md` | DEC-060 |
| U9 | Step 8 (Review Panel) | `Amendment_Rederivation_ST8_ReviewPanel_2026-11-04*.md` | DEC-080 to DEC-082 |
| U10 | Steps 9 and 9.5 (Record and Log addenda; 16 proposed observation entries, not applied) | `Amendment_Rederivation_ST9_RecordLog_2026-11-04*.md` | DEC-100 to DEC-104 |
| U11 | Step 10 (Readiness Check re-evaluation; does NOT declare the pass complete) | `Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04*.md` | DEC-120 to DEC-122 |

(`*` = the piece and its `b_T8_Rounds` record. Reader outputs and Round 3 replies are kept as dot-files `.t8_amend_*` for the record.)

## What the repass found, in short
- **The register understated the reach of the wind correction at every step.** The strongest finding, the bridge tensions BT-1, BT-5 and BT-8, Phase 10's catalog roles, Step 6's row cells, Step 7's flags and gate 8's standout, and Step 8's panel objections all rested in part on the retired "nobody ever taught the wind" reading. Each is re-derived as a proposal.
- **Narrow truths held:** the founding gap and the physics stand; "no rite or marker for a storm loss" remains an absence on the admitted lines; the duty to restore the relay remains uncompelled.
- **Phase 10:** P10-8 is CLOSE (a public weather report on the relay exists by ruling); the curating organization and a teacher of the wind enter only as candidate roles by function, with no title, office, seat or name.
- **The live culture file** (rewritten 2026-11-03) still disagrees with the sources at the Census II header, the founders note, the "smaller communities" list, the language slot, the light model and the hub members, and is silent on the ruled wind account. Step 5's docket (D-1 to D-39) lists the corrections; none was applied.
- **Step 7:** gates 0, 3, 4, 6 and I must be re-run after the amendments are applied; gates 2, 8, 9, 11 and C change now.
- **Step 8:** the one `unmet` (PF-10) re-tests to `declined`, provisional; the `unmet` count is 0 for now.
- **Step 6:** the shared differentiation table has ten sections and a Phase-axis column since 2026-10-21 (per the Step 6 datasheet), so Mirny's written nine-line row is an under-fill; the corrected row is a proposal, written nowhere.
- **Process notes:** one Round 2 mismatch (Step 5, reader A's last-line field) was logged; the audit tool's corpus excludes dot-files; the Phase 9 piece's section-2 IDs differ from its headings (cite by heading).

## Decisions waiting for the developer (all OPEN, each written on a recommended answer)
DEC-001 to DEC-004 (earlier: Esperanza, Davis, Shirayuki, Zhongshan) · **DEC-005 to DEC-008** (Idelsk-Uralia: lens, share, tie, spec lines) · **DEC-009, DEC-010** (robot term: site factor, "freedom margin") · **DEC-011, DEC-012** (Phase 9: language tier, Zodiac lens) · **DEC-013 to DEC-016** (Phase 10: organization role, who teaches, symbol status line, who built the ring and core) · **DEC-020, DEC-021** (Step 5: the strongest finding's wording, the culture-file corrections) · **DEC-040 to DEC-042** (Step 6: the row and table shape, cross-city reading of two rulings, who decides to go out) · **DEC-060** (Step 7: when and on what text the gates are re-run) · **DEC-080 to DEC-082** (Step 8: the one refusal, compulsion refusals, a fresh panel later) · **DEC-100 to DEC-104** (Steps 9/9.5: extend the repass to the uncovered files, the parallel run, the line-reference sweep, where the addenda live, the T5 check) · **DEC-120 to DEC-122** (Step 10: what "complete" means, when Step 10 re-runs, which lessons go into the rules). Unnumbered gaps (DEC-017 to DEC-019, 022 to 039, 043 to 059, 061 to 079) are reserved ranges, not missing entries.

## COVERAGE GAP (found by the Steps 9/9.5 piece)
No repass piece re-derives **Steps -1 to 3, Phase 3, or the wind lines of Phases 4 and 5**. Some of those files still state the old "nobody taught the wind" reading with no notice (the spine's deficits 5 and 7, Step 2's profile, two lines of Phase 3, Phase 4's axis and wind clauses, two Phase 5 lines that use the coinage); Steps -1, 0, 1 and 3 have not been checked at all. Question for the developer: DEC-100.

## Not done / still open (nothing here blocks the next stage)
Applying any docket (the developer's word only); re-running Step 7 on amended text; a fresh Review Panel (DEC-082); the research on the stocks the cap left out and the "lived middle"; declaring Mirny complete; Steps 9, 9.5 and 10 were added (U10, U11) but only as addenda and a re-evaluation: nothing in the old Record, Log or Readiness Check was changed.

## Where to start
`Research_Logs/DECISIONS_NEEDED_FROM_DEVELOPER.md` (answer the OPEN entries, batched by piece), then each piece's section 0 "In short". The queue and procedure are in `REPASS_QUEUE_AND_PROGRESS.md`.

## Update, 2026-11-04 evening: the developer's answers
The developer went through the open decisions (rulings `DR-107` to `DR-116`). What is true now, and the piece lines to read as superseded, are in `Amendment_Notes_2026-11-04_Answers_Carried_Forward.md`. Still open: who teaches the wind, who goes out to restore the relay, whether Mirny's people knowingly do not ask for a second relay path, whether the compulsion refusals are `unmet` or `declined`, the new name, and the date the corrections are applied. New queue units: U12 to U14 (the uncovered files, in order), U15 (an in-order fold-in of Steps 5 to 8, proposed), U16 (Mirny's symbols inside its ULM).

## Update, 2026-11-08: the coverage gap and the symbols are now covered (as proposals)
The finish run added four pieces, each three-reader and PROPOSED, nothing applied to any pass file: **U12** Steps -1 to 3 (`Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md`; DEC-140 to DEC-142) · **U13** Phase 3 (`…ST13_Phase3_2026-11-05.md`; DEC-160 to DEC-163) · **U14** the wind lines of Phases 4 and 5 (`…ST14_Phases4and5_2026-11-05.md`; DEC-180 to DEC-183) · **U16** Mirny's symbols inside its own ULM (`…ST16_Symbols_2026-11-05.md`; DEC-200 to DEC-204). The coverage gap above (DEC-100) is therefore closed on the proposal side. U16's result: **Air stands** (Wood runner-up); **Planet recommended Neptune, PROVISIONAL** (Uranus, then the Sun; Saturn not confirmed); the Planet is still **HELD by the developer**, which blocks calling Mirny complete (`DR-115`). **Mirny is NOT declared complete.**
Still needed from the developer: answer the OPEN decisions (DEC-140 to 142, 160 to 163, 180 to 183, 200 to 204, and the older ones); the Planet (DEC-200); the fold-in unit U15; applying the corrections and dockets (only on his word); the new name (DR-110); a fresh Review Panel; the Step 10 re-run.

## Update, 2026-11-08 evening: the Step 7 re-run, the fresh Review Panel and the Step 10 re-run
On the developer's word ("do those three items now", `DR-123`, the hours rule overridden for this run) three more pieces were written, each three-reader or seat-by-seat and PROPOSED: the **Step 7 QA re-run** (`Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md`; 39 findings; decisions DEC-220 to DEC-230), the **fresh Review Panel** (`Amendment_Rederivation_ST8b_FreshPanel_2026-11-08.md`; nine seats, 49 objections: accepted 15, noted 19, refereed 6, declined 9, unmet 0; decisions DEC-240 to DEC-245, DEC-245 PROVISIONAL on the wider proof repair) and the **Step 10 readiness re-run** (`Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md`; decisions DEC-260 to DEC-271). The developer's answers to the earlier open decisions are `DR-122` and `DR-123`; the corrections were applied (eleven end-of-file pointers, six datasheets, the culture file's factual rows and held marks, the wind account at the end of L53, the spec's founding lines and L252 clause, Mirny's registry row).
**Where Mirny stands:** of the ten conditions for "ready", **2 are met, 6 are partly met and 2 are not met** (the weather-signs research, and Step 10 run whole and last). The Step 10 run is **interim** (it ran before the research `DR-122` placed first). **Mirny is NOT declared complete and is not called ready; the declaration is the developer's alone.** Still open for the developer: DEC-041 part b, DEC-042, DEC-080, DEC-081 (deferred or open), DEC-220 to 230, DEC-240 to 245, DEC-260 to 271; U15 (held); the new name; the weather-signs research (no date); the stocks research; the Step 7 gates not re-run; nothing is committed or pushed since the finish run began.

