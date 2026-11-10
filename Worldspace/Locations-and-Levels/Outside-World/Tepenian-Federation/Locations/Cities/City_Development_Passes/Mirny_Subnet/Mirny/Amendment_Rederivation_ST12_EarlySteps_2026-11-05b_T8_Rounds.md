# Mirny · Amendment re-derivation · Piece ST12 (Steps −1, 0, 1, 2 and 3) · T8 round record · 2026-11-05

**Companion to** `Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md`. Raw tool output is pasted, not summarized; where a block is not the whole output it is headed as excerpted. Working files are in this folder as `.t8_amend_ST12_*`.

## Setup
- **Reading list (trimmed, `DR-74`):** `.t8_required_amend_ST12.txt` (scratchpad copy `amend_ST12/t8_required_amend_ST12.txt`, byte-identical by `cmp`), **45 entries, about 8,227 admitted lines** (counted by this merge's scratch script: whole files by physical lines at merge time, spans by their ranges; the Frame's 68 span lines are counted again under entry 32): the rules (the stereotypes law; the runbook at four spans; the input-contract template; the Frame typology; run modes; the generators file; the phase-spine and QA spans; the Gate 9 asymmetry file; the general-population discipline; the rulings log at 24 spans); the live sources at Mirny's rows only (the census, the extent file, file 16's Half B header, the research-log index, the Mirny spec whole, the repo scope, the Founding Register, the relationship database, the immigration composition file, the language blocs); **the object, read whole: the five step files (entries 22 to 26), the position-coverage ledger (27) and the four datasheets (28 to 31)**; the Frame's spans again (32); the amendment layer from before the repass (the Phase 6, 7, 2, 9 and 8 pieces, the Phase 8 dockets, the Idelsk-Uralia piece, the robot-term piece's first 30 lines, the amendment register, the reconciliation note's L1 to L120); the first 60 lines of the Phase 10 and Step 5 pieces; and the answers note of 2026-11-04.
- **Brief:** `.t8_amend_ST12_brief.md`, identical for A/B/C with `{X}` the reader letter; **sha256[:16] d9b40b3bbafd31ed** (computed by this merge on the folder copy; the scratchpad copy is byte-identical by `cmp`). It carries eight orchestrator-verified results with sources, the developer's binding words, the stage order, eleven traps and six standing lines.
- **Readers:** three Opus agents, dispatched 05:22 on 2026-11-05 after the list and brief were frozen at 05:14 and 05:15 (file times; checkpoint L9): A `ac867522ea04f9ce3`, B `aed9d976fc321ae9d`, C `a82532ebbc682b6f6` (`.t8_amend_ST12_CHECKPOINT.md` L9). Outputs time-stamped 05:53 (A), 05:51 (B) and 05:59 (C) in the scratchpad; Round 1 complete 06:00 (checkpoint L10). **None refused any entry** (A L52; C L55; B's reading log). Graphify: not used by any reader; reader C records that no hook notice appeared in its run (its snag 15).

| Reader | Output lines | Bytes | PROOF blocks | Findings (Round 1 numbering) | Missed-findings list | Docket | Requests · questions · RFs |
|---|--:|--:|--:|---|---|---|---|
| A | 1,299 | 151,553 | 45 | AS12-1 to AS12-32 | F12-1 to F12-37 | D12-1 to D12-32 | AR-200 to AR-204 · AQ-200 to AQ-205 · RF-ST12-1 to RF-ST12-5 |
| B | 1,507 | 144,094 | 45 | AS12-1 to AS12-43 | M-1 to M-42 | DK12-1 to DK12-44 | AR-200 to AR-204 · AQ-200 to AQ-206 · RF-ST12-1 to RF-ST12-4 |
| C | 1,757 | 187,247 | 45 | AS12-1 to AS12-63 | F-1 to F-47 | DK12-1 to DK12-62 | AR-200 to AR-204 · AQ-200 to AQ-206 · RF-ST12-1 to RF-ST12-4 |

Line and byte counts by `wc` on the folder copies, byte-identical to the scratchpad copies (`cmp`); PROOF blocks counted by `grep -c '^### PROOF:'` (45 each). No reader proposed a DEC number.
- **Self-checks before handback (as each reader records):** A checked its quotations against the listed files with an inline script (no file created) and typed its PROOF fields by hand, using `wc -l` and a trailing-byte check for line counts (its snag S-15). B checked `wc -l` and the last byte of every whole-file entry by shell (its reading log L52). C records no graphify use and no repository-wide search (its L55). No PROOF field was produced by a script; no reader created a helper file in the repo.
- **Ruling-log freeze (`M-302`):** not checked by this merge writer.

## Round 1 headline claims (union, before Round 3)
| Claim | A | B | C |
|---|---|---|---|
| Earlier coverage of the five files | none re-evaluated them whole; parts flagged (`P06`, `PIU`, `P2c`) | as A, plus `S5` L18 and `NOTE` L102 | as A, file level only for `NOTE` |
| Deficit 5's address for the first generation | Diffuse, held while nobody held the knowledge | a new address [D] | as written; none after |
| The address count (`SPN` L142 to L144) | recount (nine, eight with no grievance) | recount | no recount |
| The Census I to II difference | "351,175 relocated" with the per-body split | 16,240 of it is arithmetic, "not relocation" | "351,175 relocated" with the per-body split |
| The coinage on the shape table | the people who maintain the ring | the people who maintain the ring | the ring's clearers |
| The made knowledge in the Frame | a scope tag on D-5 and A.5 | a candidate register row D-9 | an addendum beside D-5 (with D-1, D-3, A.5 L161) |
| An amendment notice on the five files | none (scope tags) | a one-line notice at the top | a longer notice at the head |
| The contract's map | a drift note; a re-map on request | a line-grain re-read, +22 after old L45 | a re-mapped table, (i) to (xi); +22 "from old L32" in one paragraph |
| Spec L251 in the re-map | DEMOTED | EXCLUDED except as a docket pointer | DEMOTED |
| The tier addendum (`SPN` L67) | as-written and live figures in one addendum | live only | live only |
| Research's open threads | a request | a request | text drafted for the research log |
| Numbering | AS12-1 to AS12-32 | AS12-1 to AS12-43 | AS12-1 to AS12-63 |

## Round 2 (`Tools/triple_read_verify.py`) · first run NOT UNANIMOUS on one entry (a list defect); each variant re-run UNANIMOUS
**What happened (checkpoint L11, and the orchestrator's account to this merge, ORCH).** The orchestrator's list carried the Frame (`00_Frame.md`) twice: whole at list line 23 (entry 23) and as spans `130-175,219-236,463-466` at list line 32 (entry 32). Every reader correctly wrote one PROOF block for each. The tool keys its comparison by file path, so for the Frame it compared each reader's **span** block (68 admitted lines, first line L130, last line L466) with the **whole-file** truth (653 lines, first line L1, last line L653) and reported LINES, L1 and LLAST mismatches for all three readers on that one entry. **This is a list defect, not a reader error:** the other 44 entries matched for all three readers on the first run. The orchestrator then re-verified each variant in the scratchpad (`r2split/`): a list with only the whole-file entry (44 entries) against reader files with the span block removed, and a list with only the span entry (44 entries) against reader files with the whole-file block removed; **both variants were UNANIMOUS**. The fix was applied to the list builder for later units (checkpoint L11). The three raw outputs follow, verbatim; `.t8_amend_ST12_round2_raw.txt` is byte-identical to the first-run file (`cmp`, by this merge), and each variant file is byte-identical to its scratchpad source (`r2split/round2_whole.txt`, `r2split/round2_span.txt`; `cmp`, by this merge).

### Round 2, first run: raw output (full; file `.t8_amend_ST12_round2_raw_FIRSTRUN.txt`)
```
required files: 45
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 309-372,378-426,430-540,2429-2661] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/05_The_Input_Contract.md  [range 745-806] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/01_Frame_Typology_and_Inheritance.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Run_Modes_Warm_and_Cold.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/02_Generators_Capability_and_Symbols.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 321-400] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/04_QA_Gates_and_Differentiation.md  [range 96-107] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Stepwise_Execution/02_Gates/G10_Gate_9_Asymmetry.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00b_General_Population_Discipline.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md  [range 1-41,372-376,500,642] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Extent_and_Density_Per_City.md  [range 522-540,601-604,611] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/16_Per_City_Three_Tier_Run.md  [range 241-248] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/README.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Mirny.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Repo_Scope.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 203-251,422-435,448-461,463-475,510-524,538-553,609-621,953-965,1075-1088,1092-1107,1111-1133,1137-1156,1211-1226,1404-1412,1427-1434,1438-1445,1460-1468,1472-1479,1523-1530,1550-1557,1570-1577,1655-1662,1664-1671,1707-1715] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Founding_Register.md  [range 1-31,57,88] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Relationship_Database.md  [range 1-58,334-344] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Upper_Earth_Immigration_Composition.md  [range 1-3,21-35,619-627] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Language_Blocs_By_City_2026-11-03.md  [range 988-1026] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00.1_Step_MINUS-1_Input_Contract.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00_Frame.md ===
  agent1   ⛔ LINES MISMATCH  claimed='68'  actual='653'
  agent1   ⛔ L1    MISMATCH  claimed="location's type · *Polity* — `FTD` L37's local-council claus"  actual='# Mirny — Step 0 · The Frame'
  agent1   ⛔ LLAST MISMATCH  claimed="| PA-10 | **Network onsets:** Mirny's network elements come "  actual='7. **All three readers carried `RB` L1961\'s "Band 6" at firs'
  agent2   ⛔ LINES MISMATCH  claimed='68'  actual='653'
  agent2   ⛔ L1    MISMATCH  claimed="location's type · *Polity* — `FTD` L37's local-council claus"  actual='# Mirny — Step 0 · The Frame'
  agent2   ⛔ LLAST MISMATCH  claimed="| PA-10 | **Network onsets:** Mirny's network elements come "  actual='7. **All three readers carried `RB` L1961\'s "Band 6" at firs'
  agent3   ⛔ LINES MISMATCH  claimed='68'  actual='653'
  agent3   ⛔ L1    MISMATCH  claimed="location's type · *Polity* — `FTD` L37's local-council claus"  actual='# Mirny — Step 0 · The Frame'
  agent3   ⛔ LLAST MISMATCH  claimed="| PA-10 | **Network onsets:** Mirny's network elements come "  actual='7. **All three readers carried `RB` L1961\'s "Band 6" at firs'

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/01_Inherited.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/02_Spine.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/03_Research.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00.2_Position_Coverage_Ledger.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Step_-1.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Step_0.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Step_1_and_2.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Step_3.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00_Frame.md  [range 130-175,219-236,463-466] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P06_Meaning_2026-10-29.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P07_Order_2026-10-29.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P2c_Composition_2026-11-03.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P9_Populations_2026-11-04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P08_Making_2026-11-03.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Dockets_P08_Making_2026-11-04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_PIU_IdelskUralia_2026-11-04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_PRT_RobotTerm_2026-11-04.md  [range 1-30] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/DR-56_Amendment_Register_2026-10-13.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Notes_2026-11-03_Culture_File_and_Composition_Reconciliation.md  [range 1-120] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P10_Catalog_2026-11-04.md  [range 1-60] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_S5_Reconciliation_2026-11-04.md  [range 1-60] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Notes_2026-11-04_Answers_Carried_Forward.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
⛔ NOT UNANIMOUS - DO NOT WRITE. Log which agent/file failed and why.
```

### Round 2, variant with the Frame listed whole only: raw output (full; file `.t8_amend_ST12_round2_raw_variant_whole.txt`)
```
required files: 44
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 309-372,378-426,430-540,2429-2661] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/05_The_Input_Contract.md  [range 745-806] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/01_Frame_Typology_and_Inheritance.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Run_Modes_Warm_and_Cold.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/02_Generators_Capability_and_Symbols.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 321-400] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/04_QA_Gates_and_Differentiation.md  [range 96-107] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Stepwise_Execution/02_Gates/G10_Gate_9_Asymmetry.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00b_General_Population_Discipline.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md  [range 1-41,372-376,500,642] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Extent_and_Density_Per_City.md  [range 522-540,601-604,611] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/16_Per_City_Three_Tier_Run.md  [range 241-248] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/README.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Mirny.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Repo_Scope.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 203-251,422-435,448-461,463-475,510-524,538-553,609-621,953-965,1075-1088,1092-1107,1111-1133,1137-1156,1211-1226,1404-1412,1427-1434,1438-1445,1460-1468,1472-1479,1523-1530,1550-1557,1570-1577,1655-1662,1664-1671,1707-1715] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Founding_Register.md  [range 1-31,57,88] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Relationship_Database.md  [range 1-58,334-344] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Upper_Earth_Immigration_Composition.md  [range 1-3,21-35,619-627] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Language_Blocs_By_City_2026-11-03.md  [range 988-1026] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00.1_Step_MINUS-1_Input_Contract.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00_Frame.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/01_Inherited.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/02_Spine.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/03_Research.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00.2_Position_Coverage_Ledger.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Step_-1.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Step_0.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Step_1_and_2.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Step_3.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P06_Meaning_2026-10-29.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P07_Order_2026-10-29.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P2c_Composition_2026-11-03.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P9_Populations_2026-11-04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P08_Making_2026-11-03.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Dockets_P08_Making_2026-11-04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_PIU_IdelskUralia_2026-11-04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_PRT_RobotTerm_2026-11-04.md  [range 1-30] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/DR-56_Amendment_Register_2026-10-13.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Notes_2026-11-03_Culture_File_and_Composition_Reconciliation.md  [range 1-120] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P10_Catalog_2026-11-04.md  [range 1-60] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_S5_Reconciliation_2026-11-04.md  [range 1-60] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Notes_2026-11-04_Answers_Carried_Forward.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

### Round 2, variant with the Frame listed as spans only: raw output (full; file `.t8_amend_ST12_round2_raw_variant_span.txt`)
```
required files: 44
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 309-372,378-426,430-540,2429-2661] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/05_The_Input_Contract.md  [range 745-806] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/01_Frame_Typology_and_Inheritance.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Run_Modes_Warm_and_Cold.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/02_Generators_Capability_and_Symbols.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 321-400] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/04_QA_Gates_and_Differentiation.md  [range 96-107] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Stepwise_Execution/02_Gates/G10_Gate_9_Asymmetry.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00b_General_Population_Discipline.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md  [range 1-41,372-376,500,642] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Extent_and_Density_Per_City.md  [range 522-540,601-604,611] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/16_Per_City_Three_Tier_Run.md  [range 241-248] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/README.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Mirny.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Repo_Scope.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 203-251,422-435,448-461,463-475,510-524,538-553,609-621,953-965,1075-1088,1092-1107,1111-1133,1137-1156,1211-1226,1404-1412,1427-1434,1438-1445,1460-1468,1472-1479,1523-1530,1550-1557,1570-1577,1655-1662,1664-1671,1707-1715] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Founding_Register.md  [range 1-31,57,88] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Relationship_Database.md  [range 1-58,334-344] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Upper_Earth_Immigration_Composition.md  [range 1-3,21-35,619-627] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Language_Blocs_By_City_2026-11-03.md  [range 988-1026] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00.1_Step_MINUS-1_Input_Contract.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/01_Inherited.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/02_Spine.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/03_Research.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00.2_Position_Coverage_Ledger.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Step_-1.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Step_0.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Step_1_and_2.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Step_3.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00_Frame.md  [range 130-175,219-236,463-466] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P06_Meaning_2026-10-29.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P07_Order_2026-10-29.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P2c_Composition_2026-11-03.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P9_Populations_2026-11-04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P08_Making_2026-11-03.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Dockets_P08_Making_2026-11-04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_PIU_IdelskUralia_2026-11-04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_PRT_RobotTerm_2026-11-04.md  [range 1-30] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/DR-56_Amendment_Register_2026-10-13.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Notes_2026-11-03_Culture_File_and_Composition_Reconciliation.md  [range 1-120] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P10_Catalog_2026-11-04.md  [range 1-60] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_S5_Reconciliation_2026-11-04.md  [range 1-60] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Notes_2026-11-04_Answers_Carried_Forward.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

**Reading the three outputs.** First run: 45 entries; 44 show all fields matching for agent1, agent2 and agent3 (132 of 135 agent-entry results); the Frame's whole-file block (its path printed without a range) shows LINES, L1 and LLAST mismatches for all three, each a span-block value (68; the span's first and last lines) set against the whole-file truth (653; L1; L653); the span entry (the same path with its range) matched; verdict NOT UNANIMOUS. Whole-file variant: 44 entries, all matching (132 of 132), the Frame printed without a range; UNANIMOUS. Span variant: 44 entries, all matching (132 of 132), the Frame printed with its range; UNANIMOUS. **No reader repaired a field; no repair was needed.**

## Round 3 (SendMessage to the same three agents) · 2026-11-05, sent 06:05, replies 06:07 (scratchpad) · cross-check done
Each reader was sent eight points the three appeared to share (K1 to K8), a request to map the other two readers' re-derivations onto the old items, to list every split that would change what a file says with the position it would hold, to check the single-finder finds against the pass lines, to fold C's long list, and to propose one numbering set; and a request to list any claim in the other two readers' work it would not accept. Replies: `.t8_amend_ST12_round3_reader{A,B,C}.md` (302, 421 and 249 lines; byte-identical to the scratchpad copies by `cmp`). **The text of K1 to K8 as sent is not in the folder;** the topics are read from the replies, and the orchestrator's account to this merge names two corrections it draws from them (K1 too strong; K5's phrases not in the Frame) (ORCH).

| Reader | Part 1 OBJECTs | Part 2 splits listed | Single-finder finds checked | Part 3 claims not accepted | Coverage of the others' files |
|---|---|---|---|---|---|
| A | 2, both narrow (K1, K5) | 15 (its 2.2, 1 to 15), with a 53-finding numbering set | B's 5 and the K6 arithmetic: all CONFIRM; C's 5: all CONFIRM; two-reader finds named | 4 in B's work, 4 in C's | B at L696 to L1139 and C at L796 to L1385, with spot checks of both readers' tag sections (its L3) |
| B | 2 (K1, K5) | 19 (its 2.2, 1 to 19), with a 50-finding numbering set | A's 9: all CONFIRM; C's 12: all CONFIRM (one as a docket item only) | 6 points: 4 in A's work, 4 in C's (two points name both) | A at L125 to L929, C at L129 to L1385 (its L3) |
| C | 2 (K5, K6) | 15 (S1 to S15) plus 3 tag-only (T1 to T3), with a 42-finding numbering set | A's 6: 5 CONFIRM, 1 CONFIRM of the fact with an OBJECT to its docket row; B's 8 (two of them also C's own): all CONFIRM | 3 in B's work, 3 in A's | A from L125 (its re-derivation L639 to L816, the rest to L929), B from L696 (its re-derivation L808 to L1024, the rest to L1139) (its L3) |

### The shared points (K1 to K8)
| K | Topic (as read from the replies) | A | B | C |
|---|---|---|---|---|
| K1 | no amendment notice heads the five files; no earlier piece checked them | **OBJECT (narrow):** no notice, agreed; but `PIU` AIU-16 re-derived the Frame's A.5 and D-6, `P06` §3 #26 and §9 flagged `SPN` L134 and L136, `P2c` L183 fed nine Spine and Research lines; no piece re-evaluated the files whole | **OBJECT:** the same four, plus `S5` L18 (PA-7) and `NOTE` L102 (file level); "no earlier piece re-derived any of the five files as a whole" | **AGREE**, with the same precision: a few lines were touched, no file was re-checked as a file |
| K2 | the retired premise runs beyond deficits 5 and 7 and the G4 profile | AGREE (lists each reader's lines; the only tag split is `RES` L30, L135) | AGREE (lists each reader's lines) | AGREE (lists each reader's lines; splits in its Part 2) |
| K3 | the Spine's tier figure is Half B's mandate before the robot term; section 20 governs | AGREE | AGREE, with a nuance (the figure is PROPOSED although its decision markers are accepted, `ANS` L33) | AGREE (the robot term stays flat, `DR-109`) |
| K4 | the datasheets' spread and computed extent are wrong arithmetic | AGREE (1.26 points; 140.35 and 200.51 km²; the printed figures come from superseded interim totals) | AGREE (the same arithmetic) | AGREE (the same arithmetic) |
| K5 | the Frame is stale on its composition and founders | **OBJECT (narrow):** stale on the old totals, the robot share, China as Primary, `DR-9`'s founders and open language; it never says "fourteen stocks", "second slot open" or "sponsor", and never names Idelsk-Uralia (0 each in `FRM` and `CON`) | **OBJECT (narrowly):** the same; searched both files, zero hits; those phrases belong to later frames and pieces | **OBJECT:** the same; word check on `FRM` L1 to L653, no hit |
| K6 | the live census difference contains 16,240 of arithmetic additions | AGREE: the arithmetic is right (52,119 and 35,879; 10,392 humans, 5,848 robots); a caution only, history (`DR-16`) | AGREE (its find; the others should adopt it) | **OBJECT:** the arithmetic is right, but "not relocation" reads an authoring label as an in-world fact; at most a reserved caution |
| K7 | the contract's lists and anchors are keyed to the 230-line spec | AGREE (+22 from old L46; old L32 to L45 were replaced) | AGREE (+22 after old L45) | AGREE, with a self-correction: +22 from old L46, not old L32 |
| K8 | `D16`'s span holds only Half B's header | AGREE | AGREE | AGREE (a list defect, not a reader gap) |

### The splits, and how they were settled
*Rule: the position two or three readers hold after Round 3's concessions; where they still differ, the most conservative reading (the one that changes less, claims less or keeps a record), the split named in the piece. Reader numbering: A's 2.2 (A1 to A15), B's 2.2 (B1 to B19), C's S1 to S15 and T1 to T3.*

| # | Point | Positions after Round 3 | Settlement (where in the piece) |
|--:|---|---|---|
| 1 | **The amendment notice** (A1; B14; C S10) | B, C: a notice at the head (B: one line; C: B's line plus a clause); A: at the end, never at the head (a head notice shifts every cited line; `P06` snag 5) | **not at the head** (the orchestrator's correction (c)); **at most one end-of-file pointer, only where a ruling permits a pass-file edit** (`DR-101`; `DR-116` covers Steps 9 and 9.5 only): DEC-140; text B's line plus C's clause, C's status wording (AS12-52) |
| 2 | **Deficit 5's address for the first generation** (A2; B1; C S6) | A, C: as written; B conceded | **as written for the first generation; none after** (AS12-33) |
| 3 | **The address count** (A3; B2; C S5) | crossed: A conceded to C (a reserved finding); C conceded to A and B (the recount, labeled as arithmetic); B holds the recount | **B and C hold the recount after Round 3: carried in the body, medium confidence;** A named (AS12-36) |
| 4 | **`SPN` L49, "No single founding authority"** (A4) | B, C: superseded by `DR-54`, label I; A conceded | **I, W** (AS12-28; section 1.4) |
| 5 | **`RES` L30, L135** (A5; B5; C S2) | all: no label (KEEP); B's scope note kept (C: at low confidence) | **KEEP, a scope note, low** (AS12-40) |
| 6 | **Where the +22 begins** (A6; C K7) | A, B: from old L46; C self-corrected | **from old L46** (AS12-3) |
| 7 | **The Census I to II difference** (A7; B12; C S11, S15; K6) | A, C: live arithmetic as history; B: the caution as a Frame line; C: the caution reads an authoring label as fact | **neither "relocated" nor "not relocation" carried;** the live difference, the census lines' own labels and the arithmetic stated; the caution reserved, reworded (RF-ST12-1) (the orchestrator's correction (d)) (AS12-10) |
| 8 | **The coinage on the shape table** (A8; B4) | A, C: "the ring's clearers" (an existing phrase, `P9` L125); B: function wording, C's phrase acceptable | **the ring's clearers** (AS12-32; AQ-209) |
| 9 | **The made knowledge in the Frame** (A9; B13; C S8) | all: C's addendum beside D-5 with A's scope tag; B's D-9 reserved | **as all three hold** (AS12-19; RF-ST12-2) |
| 10 | **The contract map** (A10; B17; C S13) | all: B's line-grain re-read as the method, C's list of changed rows as the content; no new Step −1 run | **as all three hold** (AS12-3; AR-202) |
| 11 | **`INH` #5** (A11; B16) | A, B: overlap is possible, no decider; C's Round 1 "gains ground" objected to | **A, B** (AS12-25) |
| 12 | **The spine sentence's "trusts" clause** (A12; C S14) | all: the register's existing reword, "trusts what is written, taught and relayed" (`REG56` L51) | **the register's wording** (AS12-37) |
| 13 | **`DS12` L33** (A13) | A, B: no row of its own; C: an addendum | **no row of its own** (AS12-49) |
| 14 | **`FRM` D-3** (A14) | A, B: none (physics); C: P | **none** (AS12-19; section 1.2) |
| 15 | **Research's open threads** (A15) | A: a request; B: a docket item only; C: text for the research log | **a request** (the conservative reading; A would not accept the text, the log not being on the list) (AS12-44; AR-206) |
| 16 | **`SPN` L50, "no builder to ask"** (B3; C T1) | all: KEEP, with C's note on the plant's operators | **KEEP** (AS12-28; section 1.4) |
| 17 | **`RES` L90, "Substitutes for judgment."** (B6; C S4) | A, B: W as founding framing; C conceded | **W** (AS12-41) |
| 18 | **`RES` L124's second clause** (B7; C S3) | A, B: W, N; C conceded | **W, N** (AS12-43) |
| 19 | **`CON` L505, R-7** (B8) | B: N (stage order); A, C confirmed in Round 3 | **N** (AS12-6) |
| 20 | **`LED` L28** (B9) | A, C: P; B conceded | **P** (AS12-51) |
| 21 | **Spec L251 in the re-map** (B10; C S12) | B: comparison and other-location spans EXCLUDED, the founders clause pointing to the Register; C: EXCLUDED, kept as a docket pointer (conceded to B's Round 1); A's Round 1: DEMOTED whole | **the other-location and comparison spans EXCLUDED; the founders clause at most a docket pointer to the Register** (B, C; the reading that admits less) (AS12-2, AS12-3) |
| 22 | **Spec L174** (B11) | all: DEMOTED, read through `REG` L57 | **as all three hold** (AS12-2) |
| 23 | **`INH` #3** (B15) | all: the route back written in part by ruling; B holds C's fuller text (a new against-side) | **C's fuller text** (AS12-24) |
| 24 | **`SPN` L40** (B18; C S1) | A: L; B: P, KEEP the physics with a scope note; C: L and P, conceding the note | **L, P; a scope note; W not carried** (AS12-29) |
| 25 | **Deficit 7's address** (B19; C S7) | B: C's wording; C: B's split, withdrawing its [D] phrasing; A: its founding reading | **B's split** (C holds it; A compatible) (AS12-35) |
| 26 | **The tier addendum** (C S9; B Part 3) | B, C: the live figure only, the old one referred to; A's Round 1 mixed them | **B, C** (AS12-27) |
| 27 | **`RES` L114** (C T2) | A: P, W; B: P, W; C: N, P | **P, W** (A, B) (section 1.5; AS12-42) |
| 28 | **The name lines' label** (C T3) | A, B: N; C: L | **N** (A, B) (AS12-17) |
| 29 | **Numbering** (A 2.5; B 2.5; C 2.5) | three colliding sets; A proposed 53, B 50, C 42 on the same folds | **A's 53 subjects, re-ordered by file** (the orchestrator's instruction) (piece section 1.9) |

### Single-finder finds, checked against the pass lines in Round 3
| Find | Finder | Checked by | In the merge |
|---|---|---|---|
| `SPN` L6's runbook anchor (now L2566) | A | B CONFIRM; C tags it | AS12-53 |
| `FRM` L252's runbook anchor (0.2 now to L2486) | A | B CONFIRM; C CONFIRM (runbook anchors) | AS12-53 |
| `DS12` L7's comparison word | A | B CONFIRM; C CONFIRM (low; a wording point about files) | AS12-50 |
| The research-log index has no Mirny row | A | B CONFIRM (low); C CONFIRM the fact, OBJECT to a docket row | AS12-50; AR-204 (no docket row) |
| A founding scope tag on D-5 | A | B CONFIRM | AS12-19 |
| `FRM` L165: Primary read jointly is unruled (`P2c` AQ-23) | A | B CONFIRM | AS12-12 |
| `DRL` L1130's figure against the live set | A | B CONFIRM (resolved by `PRT` L9's sets) | piece snag 13 |
| `UEIC` L624 | A | B, C CONFIRM | piece snag 12 |
| The signal deciding when people move, with warnings | A | B, C CONFIRM (as reserved) | RF-ST12-4 |
| `DS0` L16's figure is the spread of superseded interim rows | A | C CONFIRM; B (K4) | AS12-45 |
| `SPN` L173's residue | B | A, C CONFIRM | AS12-39 |
| `CON` L505, R-7 under the stage order | B | A, C CONFIRM | AS12-6 |
| `RES` L124's second clause | B | A CONFIRM; C conceded | AS12-43 |
| Step 3's search cap against LAW 0-R | B | A, C CONFIRM | AS12-44 |
| `DS12` L36's rewrite matched `DR-46`, not `DR-99` | B | A, C CONFIRM | AS12-49 |
| The 16,240 arithmetic (K6) | B | A, C CONFIRM the arithmetic; C OBJECT to the reading | AS12-10 (the arithmetic); RF-ST12-1 |
| G0-9's count mismatch persists | B | C CONFIRM | AS12-21 |
| `CON` L60, L133, L211, L327, L374, L409 under `DR-110` | B | C CONFIRM | AS12-17 |
| `RES` L82's heading tagged W | B | none | not carried (section 1.5) |
| R-2 partly resolved in the spec | B, C | A acknowledged it missed it | AS12-4 |
| The census attribution names `DR-68` only | B, C | A acknowledged it missed it | AS12-47 |
| Spec L104's ranking clause removed; L206's member renamed | C | A, B CONFIRM (the name not used) | AS12-3; piece section 2.1 |
| `SPN` L57, L66, L87, L137 carry the warnings | C | A CONFIRM | AS12-31 |
| PA-7 stays DRAFT, outside the core | C | A, B CONFIRM | AS12-20 |
| Routed items closed downstream | C | A, B CONFIRM | AS12-7 |
| The Gate 0 re-check | C | A, B CONFIRM | AS12-21 |
| A.5 L161 gains the first learning, undated | C | B CONFIRM | AS12-19 |
| `SPN` L140, L111, `RES` L7, L71, `LED` L14, L29 tagged P | C | B CONFIRM | section 1 |
| DEC-008 to cover `SPEC` L252's "China Primary" | C | B CONFIRM | AR-208 |
| The tier status (PROPOSED; `ANS` L33) | C | B CONFIRM | AQ-211; piece snag 10 |
| Open threads for the research log | C | B CONFIRM as a docket item only; A OBJECT | AR-206 (a request only) |
| The Unrecognized Instrument realized; Step 2's temporal shape; deficit 7 as memory | C | A and B list them as reserved | RF-ST12-8, RF-ST12-3, RF-ST12-6 |
| `FRM` L127 and L365 as founders lines | C | A's Round 3 map places them among the founders lines | AS12-11; section 1.2 |

### Claims not accepted (left out of the merge; each listed with what was done)
| Claim | Whose | Objected to by | Why | In the merge |
|---|---|---|---|---|
| a notice "at the top of" or "at the head of" the five files | B (DK12-44, AQ-204); C (AS12-63, DK12-62, AR-201) | A | shifts every cited line in five files every piece cites | at most an end-of-file pointer, on the developer's word (AS12-52; DEC-140) |
| a new address for deficit 5 for the first generation | B (AS12-1) | A, C (B conceded) | a new [D] claim with no ruling | as written for the first generation (AS12-33) |
| deficit 6 "names the founders by `DR-9`'s three stocks" | B (M-10) | A | the line names no stock | only its founding-nation clause superseded (AS12-34) |
| 16,240 "comes from redistribution arithmetic, not relocation"; no retention may be read as a disposition; the same reading in B's RF, AQ and datasheet addendum | B (AS12-12, RF-ST12-1, AQ-205, AS12-36) | A, C | an authoring label read as an in-world fact | a reserved caution, reworded (RF-ST12-1; AQ-207) |
| "351,175 relocated (168,949 humans, 182,226 robots)" | A (AS12-14); C (AS12-23) | B | part of the difference is labeled arithmetic by the census | the live difference stated, nothing called relocated (AS12-10) |
| the tier addendum carrying the as-written and the live figure together | A (AS12-10) | B, C | as-written and live in one finding (trap 6) | the old figure referred to, never restated (AS12-27) |
| the superseded interim totals inside findings that state live figures | A (F12-21, AS12-29) | B, C | mixing; acceptable only as a separate diagnosis line | separate diagnosis lines (AS12-45, AS12-46) |
| "+22 from old L32" | C (AS12-43, AS12-48, snag 8) | A (C self-corrected) | old L32 to L45 were replaced, not shifted | from old L46 (AS12-3) |
| text appended to `Mirny_Research_Log.md` | C (AS12-56, DK12-55) | A | the log was not on the list and no reader opened it | a request (AR-206) |
| "the firing reading (C's) gains ground" | C (AS12-51) | A, B | takes a side in Step 1's held split | the ruling makes the case possible; the gate undecided (AS12-25) |
| demoting spec L251 whole | A (AS12-22); C (AS12-43 (x)) | B (C conceded) | would admit other-location text as prompt | the split disposition (AS12-2, AS12-3) |
| the divergence at `RES` L116 to L117 is "what the rulings now make canon in principle" | C (AS12-54) | B | the rulings make neither that form nor a record written into the found record canon | not carried (AS12-42) |
| "Pieces 1 to 3 and the Phase 2 composition piece are in" | C (AS12-62) | B | only the Phase 2 composition and Phase 8 pieces were accepted (`DR-105`) | per `DR-105` (AS12-51) |
| "adopted the section 20 reading" cited to `DRL` L1130 | B (AS12-7) | C | the line asks only to confirm the figure for Mirny | `PRT` L20 cited (AS12-27) |
| a docket row for the Research_Logs index | A (D12-32, AR-203) | C | outside Steps −1 to 3 | a bookkeeping request only (AR-204) |

## Settled in the merge (beyond the splits)
- **Union applied:** A (the anchors of `SPN` L6, `FRM` L7, L64, L68, L252, `INH` L5, L45, L47; the comparison word in `DS12` L7; the research-log index; the scope tag on D-5; the joint Primary unruled; the datasheet extent diagnosis; `UEIC` L624; `DRL` L1130 against the live set; RF-ST12-4, RF-ST12-7, RF-ST12-9, RF-ST12-10); B (the 16,240 arithmetic; R-7 and the stage order; the search cap; `SPN` L173; `DS12` L36's rewrite; G0-9; the contract's `DR-110` lines; R-2 partly resolved; the census attribution; the contract's newly PROVIDED inputs; the feeds on sea ice and light; RF-ST12-1, RF-ST12-2, RF-ST12-5); C (the routed items; the Gate 0 re-check; PA-7; A.5 L161; the warnings on the relay across the Spine; the spec's changed rows (i) to (xi); the ranking clause and the renamed member; DEC-008 and L252; the tier status; the new against-side in Gate 9's #3; RF-ST12-3, RF-ST12-6, RF-ST12-8).
- **Who teaches is open** (`DR-111`; `ANS` L15). The addenda say only that the wind is taught person to person (`DR-56`). Not carried as wording: A's "by the founding cohort and those they taught" (it rests on the rulings log's own gloss, `DRL` L1124, which C showed is not the developer's words, `P9` AR-64); C's "its first generation became the experts and taught everyone after"; C's Act 2 clause on the first-cohort robots (a single derivation not checked in Round 3).
- **The section 1 tables:** positions extracted by a scratch script; a label is carried when two or three readers hold it; the anchor label settled once (AS12-3, AS12-53); Round 3 concessions and confirmations applied as named overrides (`RES` L5, L7, L30, L90, L124, L135; `SPN` L40, L49, L50, L111, L135, L140; `CON` L60, L133, L211, L457, L505; `FRM` L127, L161, L226, L365, L423, L433, L539; `INH` L17, L19, L26; `LED` L14, L28, L29; `DS12` L5 to L8; `DS3` L10).
- **Numbering:** A's 53 subjects re-ordered by file; one docket row per finding (A's form, which B and C also proposed), DK12-15 empty; C's DK12-24 and DK12-58 and A's D12-32 not carried.
- **AR-210 answered by this merge** from the queue (`QUEUE` L35 to L37: U12 Steps −1 to 3, U13 Phase 3, U14 the wind lines of Phases 4 and 5).
- **Decisions DEC-140 to DEC-142:** DEC-140 (the end-of-file pointer) from A's split 1, B's AQ-204 and C's AR-201, reframed by `DR-101` and `DR-116` item 2 (read by this merge, `DRL` L1673 to L1679, L1814); DEC-141 (the datasheets in place or beside) from A's AR-202 and the three readers' datasheet questions; DEC-142 (the signifier research) from B's AR-202 and C's AR-203.
- **Figures:** the old frame's figures appear only on the "As written" lines of section 2; the mixing check below runs at line level and at finding-block level. Shares are weights, never head counts.
- **The coinage** appears in the piece only inside the quoted pass text "the ring's keepers" (twice, AS12-32); no group is named by it and no replacement is coined.

## Kept files (`M-132`)
The Round 1 outputs `.t8_amend_ST12_readerA.md`, `.t8_amend_ST12_readerB.md`, `.t8_amend_ST12_readerC.md` and the Round 3 replies `.t8_amend_ST12_round3_readerA.md`, `.t8_amend_ST12_round3_readerB.md`, `.t8_amend_ST12_round3_readerC.md` are kept in this folder as the round's working record, unedited, beside the Round 2 files (`.t8_amend_ST12_round2_raw.txt`, `.t8_amend_ST12_round2_raw_FIRSTRUN.txt`, `.t8_amend_ST12_round2_raw_variant_whole.txt`, `.t8_amend_ST12_round2_raw_variant_span.txt`), the frozen brief `.t8_amend_ST12_brief.md`, the list `.t8_required_amend_ST12.txt` and the checkpoint `.t8_amend_ST12_CHECKPOINT.md`. The reader files, the replies, the brief and the list are byte-identical to the scratchpad copies in `amend_ST12/`, and the two variant files to `r2split/` (`cmp`, by this merge). None of these files is an input to any later step; this record and the piece are the merged result. No helper file was created in the repo by the readers or by this merge (scratch work stayed in the session's scratchpad, `st12_merge/`).

## Quotation audit (`Tools/quotation_audit.py`, `--files Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md --own-pass`) · 2026-11-05 about 06:37, run before this record existed
raw output, excerpted (1 line omitted: the positive control "HARD - case mismatch", whose test phrase names another location; it is one of the controls behind the instrument line below, which reads VALID; the whole output is in the session scratchpad at `st12_merge/qaudit_final.txt`):
```
pass audited : Mirny
corpus mode  : default (own pass excluded)
corpus files : 6099   chars: 70,247,635
files audited: Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md
own-pass mode: a quotation may also be found in this pass's OTHER files (never in its own file)

=== POSITIVE CONTROLS ===
  [easy                      ] FOUND     a terminus is nobody's midpoint
  [HARD - blockquote wrap    ] FOUND     A pass may not proceed to Step 5 with a NEVER CITED row
  [HARD - outside Worldspace ] FOUND     Paste raw QA scan output into the QA block. Never summa
  [HARD - long wrapped       ] FOUND     Different content is not differentiation; a different q

  INSTRUMENT VALID: YES
  NEGATIVE CONTROL (must be absent): PASS - absent

=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 46
NOT FOUND in corpus: 16
  of those, in TABLE CELLS : 0
  of those, in PROSE       : 16

  [Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md:20]           and never name idelsk-uralia (k5; counted 0 by all three readers and by this merge)
  [Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md:22]           (52,119 at census i, 35,879 at census ii), so 16,240 of the difference (10,392 humans, 5,848 robots) traces to those additions cal
  [Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md:445]           in round 3). changed text since: l15 and l16 (the census), l20 to l22 (the tiers), l21 (the tag), l28 (the dr-85 rework note), l32
  [Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md:538]           for the whole line not accepted: it would admit other-location text as prompt, b; c conceded); old l230 is spec l252, demoted (the
  [Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md:655]           ( dr-56 item 3, drl l1116); best placed is
  [Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md:680]           are true as founding conditions and stay (narrow truth; l50 keep after b and c conceded in round 3; c's note: the station's builde
  [Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md:681]           holds of the record and of the founding population, not of the founding role. deficit: no living teacher at the founding (true the
  [Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md:685]           l40): step 3 found the cues honest and unread at the founding
  [Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md:701]           uses the pass author's coinage ( dr-57 , drl l1150). l119's
  [Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md:714]           is superseded as to the founding nation (idelsk-uralia, dr-54 ) and stands as to the founding population (four exile groups, reg l
  [Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md:789]           before the dr-68 census change of 2026-10-28
  [Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md:799]           founded by idelsk-uralia, with exile groups from russia, china (the sinian federation) and australia
  [Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md:805]           230 lines total (bound for any future read-spec computation)
  [Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md:813]           is the first generation's ( p07 a7-8); phase 8's
  [Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md:972]           and the name idelsk-uralia occur 0 times in frm and con (counted by all three readers and by this merge's grep -ci )
  [Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md:990]           any name for the organization or the protocol; a coined replacement for the coinage; a teacher role as fact; a form for the signif

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```
**Triage by hand (each of the 16 misses read and classified):** 46 fragments tested, **16 not found** (0 in table cells, 16 in prose). **13 are connective prose** captured between two adjacent quotations on one line (the audit's own warning) or this piece's own wording on lines that also carry quotations: section 0 items 5 and 7 (L20, L22), section 2.1 (L445), the findings' notes and addenda (L538, L655, L680, L681, L685, L701, L714, L813), and the snags (L972, L990). **Three are exact quotations of the pass's datasheets**, which sit in the pass folder's `Datasheets/` subfolder; the audit did not find them in its corpus, and each was confirmed at its source line with `grep -nF` (merge checks below): L789, `DS-1` L26; L799, `DS12` L36; L805, `DS-1` L16. **No misquotation was found by the audit.** An earlier run (about 06:34, same instrument line) gave 47 fragments and 17 misses; between that run and this one, three phrases of this merge's own wording that stood in quotation marks were set in italics (a table label in section 1 and two items in the killed-in-drafting list, which were paraphrases), and one line of section 2.4 that carried an as-written and a live figure was split into two lines (the line numbers above are after that split). **A supplementary check** of every double-quoted string in the piece of any length (a scratch script, `st12_merge/shortq.py`, normalizing dashes, quotes, markup, case and spaces, run with `python3 -I`) tested 169 strings against the Mirny folder's files **including the reader dot-files and the `Datasheets/` subfolder**, the rulings log, the runbook, the census, the extent file, the Founding Register, the Mirny spec, the research-log index, file 16 and the stereotypes law: **0 not found** (merge checks below). The audit was not re-run after this record was created.

## Merge checks
raw output (full; scripts in the session scratchpad `st12_merge/`, run with `python3 -I` on the final piece; the location-name scan's list is built from the spec file names, 37 names, and its positive control on a scratch text with three planted names found all three; names are not reproduced here):
```
$ python3 -I shortq.py ctl_piece.md   # positive control: two real quotations, one planted
  NOT FOUND L1: a planted control sentence for unit twelve qx7 found nowhere
quoted strings tested: 3; files in corpus: 334; not found: 1
$ python3 -I shortq.py <the piece in the Mirny folder>   # the piece itself is excluded from the corpus
quoted strings tested: 169; files in corpus: 333; not found: 0

$ grep -nF <the three datasheet quotations the audit could not see> Datasheets/...   # each prints line:first 40 characters
26:| Census I (repeat here, full derivat
36:| Founding population | Founded by Id
16:| Specs file length | 230 lines total

$ python3 -I checks.py city ctl_names.md   # positive control: three planted names
  hit L1 (name withheld, 5 chars)
  hit L1 (name withheld, 5 chars)
  hit L1 (name withheld, 8 chars)
== ctl_names.md: names scanned 37; hits 3
$ python3 -I checks.py city <piece>
== piece_for_checks.md: names scanned 37; hits 0

$ python3 -I checks.py ids <piece>   # reader Round 1 IDs (the mapping table's A, B, C columns and "its <ID>") excluded
AS12 cited  : 1 .. 53 (53 distinct)
AS12 headed : 1 .. 53 (53 distinct)
AS12 in mapping table (bold): 1 .. 53 (53 distinct)
cited but not headed: [] | cited but not in mapping: []
RF-ST12-: cited 1..10 (10 distinct); defined 1..10 (10 distinct); cited not defined: []
AR-2xx: cited 200..210 (11 distinct); defined 200..210 (11 distinct); cited not defined: []
AQ-2xx: cited 200..212 (13 distinct); defined 200..212 (13 distinct); cited not defined: []
DK12-: cited 1..53 (53 distinct); defined 1..53 (53 distinct); cited not defined: []
DEC-14x: cited 140..142 (3 distinct); defined 140..142 (3 distinct); cited not defined: []

$ python3 -I checks.py mix ctl_mix.md   # positive control: one mixed line, two mixed blocks
  line mix L2: old ['1,351,430'] live ['1,403,549']
line-level mixes: 1
  block mix ### AS12-99 · control: old ['1,351,430'] live ['1,403,549']
  block mix ### AS12-98 · control two: old ['665,901'] live ['692,971']
finding-block mixes: 2
docket rows carrying an old-frame figure: 0
$ python3 -I checks.py mix <piece>
line-level mixes: 0
finding-block mixes: 0
docket rows carrying an old-frame figure: 0

$ python3 -I checks.py keep <piece>
L701: ...- **Current fact.** L116's "the ring's keepers" uses the pass author's coinage (`DR-57...
L703: ...- **Addendum (PROPOSED).** *2026-11-05: read "the ring's keepers" (L116) as the ring's clearers; the wor...
occurrences of keeper/keepers: 2
```
**Reading the checks:** the quotation check's control found its two real quotations (`SPN` L136 and the census label) and missed the planted one, as it should; the piece's 169 quoted strings are all found with the piece itself excluded from the corpus (333 files). The three datasheet quotations the audit could not see are at `DS-1` L26, `DS12` L36 and `DS-1` L16. No other location's name appears in the piece. Every AS12, RF-ST12, AR-2xx, AQ-2xx, DK12 and DEC-14x number cited is defined, and every AS12 number is in the mapping table (section 1.9); the readers' own Round 1 IDs, which the mapping table and a few notes cite (up to C's AS12-63 and DK12-62), are excluded from that count by design. **No line, no finding block and no docket row carries both the old frame's and the live figures** (an earlier run of the same check flagged one line of section 2.4, which then held both sets in one sentence; it was split into an "As written" and a "Live" line). The coinage's two occurrences are the Spine's own quoted words in AS12-32; no group is named by it and no replacement is coined.

## American English sweep
raw output (full; script `st12_merge/ae_sweep.py` in the session scratchpad, run with `python3 -I` on both files after this record's other sections were written; its positive control on a scratch text with fourteen planted British spellings and one planted kept spelling found all fifteen; the script prints the kept spelling's count without printing the word, so pasting this block does not change the count. A first run flagged one hit, "improvising" in the piece, which is the Spine's own word quoted at AS12-28 and the same spelling in American English; the script's allow list was extended to the forms of improvise and both files were swept again; the block is that second run):
```
== Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md
British-spelling hits: 0
kept spelling (the one allowed British form): 1
== Amendment_Rederivation_ST12_EarlySteps_2026-11-05b_T8_Rounds.md
British-spelling hits: 0
kept spelling (the one allowed British form): 0
```
