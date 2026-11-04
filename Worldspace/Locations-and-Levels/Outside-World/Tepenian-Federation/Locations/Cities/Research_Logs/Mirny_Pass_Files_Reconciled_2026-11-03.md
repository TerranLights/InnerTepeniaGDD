# Mirny: pass files reconciled with the rewritten culture file (2026-11-03)

**Done under a one-off waiver of the 05:00–14:59 hours law** (developer, ~16:10, for this task only). **No pass file was edited.** The reconciliation is an **append-only amendment note**, because `DR-74` ruled for this folder that amendments are *appended beside the pass, never a rewrite* (*"the pass files stay as they are"*), and the 2026-10-30 note set the precedent for exactly this class of change. This departs from the brief's wording ("edit in place with `[old: …]`"); the note holds every old statement beside its live value so in-place edits, if the developer wants them, are mechanical.

## Where it is
`City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Notes_2026-11-03_Culture_File_and_Composition_Reconciliation.md` (new). Sections: (1) live values vs the pass's recorded values (census after `DR-90`, tiers, 8/3/1 weights, founders per Register L57 and `DR-46`/`DR-54`, language rule); (2) the culture file's 35 changed places and the **51 of 89** `05_Reconciliation` culture-line items (LC-1…LC-89) that now point at rewritten text, each with the pass's recorded claim, recorded verdict and the line's text today; (3) the redo list; (4) a script inventory of old-value lines by file; (5) the stale-by-record files.

## What was found (summary)
- **Line numbers did not move** in the culture file, so every `LC:n` citation still resolves, to new text. Several of the pass's own Step 5 recommendations (D-3, the China-alone-at-Primary and Chinese-majority lines, the Mandarin-first language line) are now carried out by the rewrite; which items are closed is left to the Mirny block.
- **Census moved twice since the pass:** `DR-68` (already filed 2026-10-30) and `DR-90` (new: 692,971 H / 710,578 R / 1,403,549 Census I; 524,022 / 528,352 / 1,052,374 Census II; robots 50.63 % Census I, DERIVED).
- **The `DR-9` three-stock founders wording** is already recorded in the pass as stragglers (`07_QA_Gates` E6; Step 5 items (f), (g); `04_Phase_05` L105–L107; `04_Phase_09` L519). Nothing new there.
- **The false "only functioning intra-subnet Arcanet link" to Concordia was never repeated in the pass** (searched); it lived only in the culture file L80 and L301.

## Findings that must be redone (⚠ rests on the superseded frame (2026-11-03): redo in the Mirny blocks)
- **R1** P2-4 *founders a minority of descent* (3 of 14 stocks; 14 of 33; "China is both a founding stock and the Primary") and what cites it: `04_Phase_02` L235–L238; `02_Spine` L75; `06_Differentiation` L133; `04_Phase_09` P9-2 L181, L207; Step 5 BT-12, D-3. Live: 22 of 100 by weight (DERIVED); direction survives, grounds do not.
- **R2** Phase 2 A.1–A.4 composition arithmetic and the E-table (`04_Phase_02` L96–L135, L365, L384).
- **R3** P2-5 and the Step 3 research scope (*only the three founding stocks researched; eleven never*): the establishing country Idelsk-Uralia was never researched; 36 stocks, not 14; R-156 (`04_Phase_02` L238–L242, L313, L321–L329; `03_Research`; `ULM_AUTORUN_HANDOFF` L88, L108).
- **R4** Phase 9 lens decision and populations (`04_Phase_09` L20, L153, L174–L181, L193, L207, L225, L303, L313).
- **R5** Phase 8 language question and transplanted layer (`04_Phase_08` L21, L169, L257–L259, L531, L585, L643, L843; Step 5 LC-37, R-21/R-88/Q-24).
- **R6** Phase 7 "by stock, tiers only" note (`04_Phase_07` L469–L471).
- **R7** Step 5 culture-file reconciliation (LC items; BT-12, C-1, D-3).
- **R8** Symbol Review Social half (Earth/Saturn) and `04_Phase_10` L425: "no majority" still holds; counts and population are stale; symbols are determined after the locations are synthesized (developer, 2026-11-03), so provisional either way.
- **R9** Step 8 Review Panel L184 (population number only).

## Stale by record (not edited, not inputs)
`.t8_*` reader files (86), their briefs, CHECKPOINTs and required lists (41), the `*b_T8_Rounds_*` round records (17), `_safeguard_probe/` and `assemble_*.py` (29). Archived at `Archive/ULM_Records/…/Mirny/` (`DR-27`).

## Limits, plainly
- About 25,000 lines in the non-scratch files; **not read line by line.** Method: pattern search (China/Chinese/Mandarin/sole Primary/24.24/fourteen stocks/DR-9 wording/old census figures/other-city names/the Concordia link), every hit read in context (308 lines), plus full reads of the sections that carry the redo findings. Treat section 3 as a floor.
- **Not done by design:** `Datasheets/` (another fork rebuilds it); the `00.0_Pre-Trip_Inspection*.md` files, which another piece of work was rewriting at the same time (they show as modified/untracked in git and are excluded from the inventory); other cities.
- Nothing committed.
