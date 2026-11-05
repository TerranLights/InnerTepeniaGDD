# Mirny · Amendment re-derivation · Piece ST9 (Step 9 Record and Step 9.5 Log) · T8 round record · 2026-11-04

**Companion to** `Amendment_Rederivation_ST9_RecordLog_2026-11-04.md`. Raw tool output is pasted, not summarized; where a block is not the whole output it is headed as excerpted. Working files are in this folder as `.t8_amend_ST9_*`.

## Setup
- **Reading list (trimmed, `DR-74`):** `.t8_required_amend_ST9.txt` (scratchpad copy `amend_ST9/t8_required_amend_ST9.txt`, byte-identical by `cmp`), **48 entries, about 8,049 admitted lines** (counted by this merge's scratch script: whole files by physical lines at merge time, spans by their ranges): the rules (the stereotypes law; the runbook at four spans; the observations log at L8520 to L8556; the tracker at L359 to L361; the Step 9 quick reference; the rulings log at 24 spans); the live sources at Mirny's rows only (the census, the Founding Register, the Mirny spec, the relationship database, the immigration composition file, the language blocs); the Step 9 datasheet; **`09_Record.md` (96 lines) and `09.5_Log.md` (291 lines), both read whole**; the snag spans of Phases 2 to 10 and Steps 5 to 8; the Frame's spans; the amendment layer from before the repass (the Phase 6, 7, 2, 9 and 8 pieces, the Phase 8 dockets, the Idelsk-Uralia piece, the robot-term piece's first 30 lines, the amendment register, the reconciliation note's L1 to L120); and the repass's own files (the Phase 10, Step 5, Step 6, Step 7 and Step 8 pieces, the data recheck, the queue, the completion note, the decisions file). **The Step 10 piece (U11) was concurrent and not an input.**
- **Brief:** `.t8_amend_ST9_brief.md`, identical for A/B/C with `{X}` the reader letter; **sha256[:16] d828286852fbe3f3** (computed by this merge on the folder copy; the scratchpad copy is byte-identical by `cmp`). It carries eight orchestrator-verified results with sources, the developer's binding words, the stage order, nine traps and six standing lines.
- **Readers:** three Opus agents, dispatched after the list and brief were frozen at 11:24 on 2026-11-04 (file times); the unit opened 11:30 (`QUEUE` L46); outputs time-stamped 11:57 (A, B) and 12:04 (C) in the scratchpad. **The checkpoint `.t8_amend_ST9_CHECKPOINT.md` does not exist; agent IDs and tool-use counts are not recorded in the folder and are not given here.** None refused any entry. Graphify: not used by any reader; reader A observed no hook notice, reader B none in its session, reader C none in Round 1 and on almost every call in Round 3, disregarded under `DR-6` (its Round 3 snag 1).

| Reader | Output lines | Bytes | PROOF blocks | Findings (Round 1 numbering) | Docket | Requests · questions · RFs · DEC |
|---|--:|--:|--:|---|---|---|
| A | 1,179 | 141,119 | 48 | AS9-1 to AS9-20 | DK9-1 to DK9-17 | AR-160 to AR-166 · AQ-150 to AQ-155 · RF-ST9-1 to RF-ST9-5 · DEC-100 |
| B | 1,138 | 134,409 | 48 | AS9-1 to AS9-19 | DK9-1 to DK9-13 | AR-160 to AR-166 · AQ-150 to AQ-156 · RF-ST9-1 to RF-ST9-4 · none |
| C | 1,215 | 161,248 | 48 | AS9-1 to AS9-18 | DK9-1 to DK9-21 | AR-160 to AR-168 · AQ-150 to AQ-156 · RF-ST9-1 to RF-ST9-5 · DEC-100, DEC-101 |

Line and byte counts by `wc` on the folder copies, byte-identical to the scratchpad copies (`cmp`); PROOF blocks counted by `grep -c '^### PROOF:'` (48 each).
- **Self-checks before handback (as each reader records):** A typed whitespace-sensitive PROOF lines by hand and checked line lengths with `wc -l`, `tail`, `od`, `awk` and `cut` (counts only), and caught its own Register and stereotype-file line slips before its PROOF blocks (its snags 10, 12). B checked line counts with `wc -l` and a final-byte check and ran one read-only comparison of PROOF fields and quotations, which flagged three middle-line fields first copied one line off (the runbook, the Register, the Frame), each re-read and re-copied by hand (its snags 1, 9). C ran two read-only inline checks: every quotation against the admitted spans (27 not found on the first run; 0 of 473 after hand fixes) and the PROOF fields (two mismatches, entry 8's LMID and entry 45's leading spaces, both fixed by hand; 0 mismatches across 48 blocks) (its snags 13, 15). No PROOF field was produced by a script; no reader created a helper file.
- **Ruling-log freeze (`M-302`):** not checked by this merge writer.

## Round 1 headline claims (union, before Round 3)
| Claim | A | B | C |
|---|---|---|---|
| What is written | Steps −1 to 9 | Steps −1 to 9 | Steps −1 to 10; Step 10's review accepted |
| The layer's status | two accepted, the rest PROPOSED | "ten units, all PROPOSED" | twelve pieces, ten PROPOSED |
| Coverage of the layer | Phases 2, 4, 7, 5 to 10, Steps 5 to 8; **the coverage gap (AS9-16)** | "Phases 2 to 10 … re-derived" | "re-derives what rested on the retired wind reading" |
| Item 5 | not run | "the item-5 sweep, run here on this step's own pointers only" | not run; a partial list |
| `handoff_audit.py`, S9-RF-5 | YES is a self-test; S9-RF-5 stands | "the instrument validates"; S9-RF-5 "answered for later runs" | behaves as repaired; cause unrecorded |
| MP-1, MP-2 | changed output, history unverified | "met in the tool" | reflected in behavior, change unrecorded |
| Killed findings answered later | five | three, plus coinage marks | three |
| Where the addenda live | files beside, end-of-file notes | a new file beside | appended to the old files |
| The one `unmet` label | W | U (a sixth label) | W |
| Number collisions since 2026-10-12 | +6 | four units | +8 (with PRT) |
| The parallel run's cause | no admitted line authorizes it | none stated | no admitted line records why |
| Numbering | AS9-1 to AS9-20 | AS9-1 to AS9-19 | AS9-1 to AS9-18 |

## Round 2 (`Tools/triple_read_verify.py`) · UNANIMOUS on the first run (144 of 144 field sets, 48 entries)
raw output (full; file `.t8_amend_ST9_round2_raw.txt`):
```
required files: 48
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 309-372,378-426,430-540,2986-3056] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Test_Runs/OBSERVATIONS_and_Methodology_Findings.md  [range 8520-8556] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/MASTER_Process_Tracker.md  [range 359-361] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Corpus_Reference_Sheets/Step_9_Record_Full_Text_Quick_Reference.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 203-251,422-435,448-461,463-475,510-524,538-553,609-621,953-965,1075-1088,1092-1107,1111-1133,1137-1156,1211-1226,1404-1412,1427-1434,1438-1445,1460-1468,1472-1479,1523-1530,1550-1557,1570-1577,1655-1662,1664-1671,1707-1715] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md  [range 1-38,370-378,500,642,839-892] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Founding_Register.md  [range 1-31,57,88] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Mirny.md  [range 1-3,13-72,92-94,103-109,118-150,152-154,160-165,171-173,195-199,205-207] ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Step_9.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/09_Record.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/09.5_Log.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_02_Composition_and_Arrival.md  [range 512-529] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_03_Surface_and_Texture.md  [range 481-508] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_04_Ordinary_Life.md  [range 356-369] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_05_Relation_and_Geometry.md  [range 529-545] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_06_Meaning.md  [range 337-349] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_07_Order.md  [range 649-700] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_08_Making.md  [range 880-939] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_09_Populations.md  [range 510-532] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_10_Catalog.md  [range 590-603] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/05_Reconciliation.md  [range 798-815] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/06_Differentiation.md  [range 366-378] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/08_Review_Panel.md  [range 238-247] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/07_QA_Gates.md  [range 187-200] ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P10_Catalog_2026-11-04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_S5_Reconciliation_2026-11-04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST6_Differentiation_2026-11-04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST7_QAGates_2026-11-04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST8_ReviewPanel_2026-11-04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/REPASS_U00_Data_Recheck_2026-11-04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/REPASS_QUEUE_AND_PROGRESS.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/REPASS_COMPLETE_2026-11-04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/DECISIONS_NEEDED_FROM_DEVELOPER.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

## Round 3 (SendMessage to the same three agents) · 2026-11-04, replies time-stamped 12:19 to 12:20 (scratchpad) · cross-check done
Each reader was sent nine points the three appeared to share (K1 to K9), a request to map the other two readers' findings onto the old Record items and Log entries and list every split (claim, addendum text and S/H/N tag) with the position it would hold, a request to check the single-finder finds against the pass lines, a numbering proposal, and a request to list any claim in the other two readers' work it would not accept. Replies: `.t8_amend_ST9_round3_reader{A,B,C}.md` (490, 309 and 315 lines; byte-identical to the scratchpad copies by `cmp`). **The text of K1 to K9 as sent is not in the folder; the topics below are read from the replies.**

| Reader | Part 1 OBJECTs | Part 2 splits listed | Single-finder finds checked | Part 3 claims not accepted | Coverage of the others' files |
|---|---|---|---|---|---|
| A | 2 (K3, K7) | 23 (SP-1 to SP-23) | B's: 9 CONFIRM, 2 OBJECT; C's: 12 CONFIRM, 2 not re-checked, 1 OBJECT | 11 in B's work, 8 in C's | B at L468 to L745, C at L476 to L822; six self-corrections (its 2f) |
| B | 1 (K3) | 84: 15 in claim or addendum text (S-1 to S-15), 24 Record tags (R1 to R24), 45 Log tags (G1 to G45) | A's 10 (SA-1 to SA-10: 8 CONFIRM, 1 CONFIRM with one citation objected, 1 CONFIRM in part); C's 19 (SC-1 to SC-19: 15 CONFIRM, 2 CONFIRM in part, 2 OBJECT) | 9 (4 in A's work, 5 in C's) | A at L131 to L782, C at L133 to L822; eight Round 1 positions withdrawn |
| C | 4, all in part (K3, K4, K7, K8) | 28 (SP-1 to SP-15 tags; SP-16 to SP-28 claims) | A's 16 (15 CONFIRM, one with an objection to its supporting citation; 1 OBJECT); B's 9 (8 CONFIRM, 1 OBJECT) | 8 in A's work, 9 in B's, plus 7 of its own withdrawn | A at L131 to L783, B at L129 to L745; two finds new in Round 3 |

### The shared points (K1 to K9)
| K | Topic (as read from the replies) | A | B | C |
|---|---|---|---|---|
| K1 | neither file is reworded; their stale present-tense lines are handled by addenda beside them | AGREE | AGREE (adds L37's standout, L94, L56) | AGREE (`DR-102` applied as the brief states it; "complete" stale in part) |
| K2 | eight of the Record's and Log's pointers moved (+2 to +5); two file sizes grew | AGREE (lists the eight) | AGREE (lists the eight; who caught what) | AGREE (checked each; withdrew its L42 "not verified") |
| K3 | the units' overlap is a Log item; what licensed it | **OBJECT**: the developer's instruction lifts stopping, not the order; record the cause as unrecorded | **OBJECT**: the instruction sits in the same line as "go one unit at a time"; the reason is on no admitted line | **OBJECT in part**: context only; write the reason as not recorded; ask |
| K4 | the killed findings answered later by ruling | AGREE: five (two revived, one accepted, one re-grounded, one half-answered) | AGREE: five, the fifth in part only | **OBJECT in part**: four; the call-in is not settled |
| K5 | item 5 of Step 9 not run | AGREE | AGREE (withdraws "the item-5 sweep, run here") | AGREE, adding `DR-85`'s remap (new) |
| K6 | the coverage gap (Steps −1 to 2, Phase 3, the wind lines of Phases 4 and 5) | AGREE (its own find) | AGREE (its Round 1 missed it; withdraws its coverage wording) | AGREE, narrowed (Steps −1 to 1: not checked) |
| K7 | "fixed in the tools"; the seven pieces with wrong brief counts | **OBJECT**: changed output only; S9-RF-5 stands; MP-3 met for its marker half; the seven pieces are right | AGREE, read as *output changed, repair not recorded* | **OBJECT in part**: the same reading; the seven counts verified |
| K8 | observation entries not applied; their numbering | AGREE, on condition: no number until the log's tail is read | AGREE, on condition: at least M-302 (`wc -l` 8,586) | **OBJECT in part**: "after the highest you can read" would collide; OBS-n |
| K9 | propagation items are pointers only; no other location named or opened | AGREE | AGREE | AGREE (scanned A's and B's bodies) |

### The tag splits (S / H / N), and how they were settled
*B's numbering (R1 to R24 Record, G1 to G45 Log), with C's SP-1 to SP-15 where it treats the line; A's positions are its Round 1 tags (A's Round 3 did not revisit tags line by line, except SP-9). Rule: the position two or three readers hold after Round 3's concessions; where they still differ, the most conservative reading (H before H, N before S in part before S), the split named. The merged result for every line is the piece's section 1.*

| # | Lines | Positions after Round 3 (A · B · C) | Settlement |
|---|---|---|---|
| R1 | REC L3 | H · H · S in part (SP-1) | **H** (A, B) |
| R2 | REC L8 (2) | S · H, S in part · not tagged | **H, S in part** (no two alike; most conservative) |
| R3 | REC L13 and headings | — · H · N | **H** |
| R4 | REC L14 | H · H, N (yielded) · H, N | **H, N** |
| R5 | REC L18 | N · H · H | **H** |
| R6 | REC L19, L21, L31, L34 | N · H, N · N | **H, N** |
| R7 | REC L20 | S · S in part (yielded) · H, N (SP-3, conceded) | **S in part** (crossed; A and B hold an S form; the narrower) |
| R8 | REC L22, L35 | S · H, S · S | **S** (A, C) |
| R9 | REC L27 | H · H, N (yielded) · N | **H, N** |
| R10 | REC L33 | N · H, N (yielded) · N | **H, N** |
| R11 | REC L37 | H · H, S in part (yielded in part) · H, N (SP-4, conceded) | **H, N** (A and C hold H without S) |
| R12 | REC L42 | H, anchor note · H, S · H, anchor mark (SP-6) | **H, anchor mark** (A, C) |
| R13 | REC L49 | S · S in part, N (yielded) · H, N (SP-5, conceded) | **S in part** (crossed; A and B; the narrower) |
| R14 | REC L51 | S · S (I) · S | **S** (L152 blank, all) |
| R15 | REC L59 | H · H, S in part, N · H, one mark (SP-7) | **H, mark** (A, C) |
| R16 | REC L60 | H · H, S · H, mark (SP-7) | **H, mark** (A, C) |
| R17 | REC L61 | S · H, S · H, S | **H, S** (B, C) |
| R18 | REC L69 | — · H, S in part (yielded) · S in part (SP-1) | **H, S in part** (B, C) |
| R19 | REC L75, L76, L78, L80, L81, L83 | N · S · N (SP-2, conceded) | **N** (A, C) |
| R20 | REC L77, L79, L85, L86 | — · H · H | **H** |
| R21 | REC L82 | N · H, N · H, N | **H, N** |
| R22 | REC L89 | N · S in part · N (SP-2) | **N** (A, C) |
| R23 | REC L90 | N · H, N · N | **N** |
| R24 | REC L74 | S · S in part · S in part | **S in part** (B, C) |
| (C SP-2) | REC L84, L87, L88 | S · S · N | **S** (A, B) |
| G1 | LOG L5 | N · H, N · H, N | **H, N** |
| G2 | LOG headings | — · H · N | **H** |
| G3 | LOG L8, L12, L14, L17, L22, L27, L36, L55, L58, L87, L144, L145, L151, L156, L164, L234, L245, L246 | N · H, N · H, N | **H, N** |
| G4 | LOG L9, L11 | N · H · H | **H** (B, C) |
| G5 | LOG L10 | N · H, N (yielded) · H, N | **H, N** |
| G6 | LOG L16 | N · H, N · H, N (SP-8, conceded) | **H, N** |
| G7 | LOG L20 | H · H · H, N | **H** (A, B) |
| G8 | LOG L21 | N (T) · H, S anchor, N · H, anchor mark (SP-6) | **H, N, anchor mark (+5)**; T as a pointer |
| G9 | LOG L61 | H · H, N (yielded) · H, N | **H, N** (B, C) |
| G10 | LOG L63 | S · S (I) · H, N (SP-9) | **S** (A, B); C named |
| G11 | LOG L64 to L66 | N · H, S in part (yielded) · H, N (SP-8, conceded) | **H, N** (A, C); B named |
| G12 | LOG L67 | H · H, S anchor · H | **H, anchor mark** |
| G13 | LOG L68 | N · H, N (yielded) · H, N | **H, N** |
| G14 | LOG L69 | S · S · H, S | **S** |
| G15 | LOG L85 | N · H, N (yielded) · H, N | **H, N** |
| G16 | LOG L94 | H (C · I) · H, N · H | **H** (A, C); labels C · I (A's SP-9) |
| G17 | LOG L96 | H (W) · H, N · H, N | **H, N** (B, C) |
| G18 | LOG L99 | H (W) · H, N · H | **H** (A, C); B named |
| G19 | LOG L100 | H · H, N · H, N (SP-10) | **H, N** (B, C) |
| G20 | LOG L102 | H (I) · H (I) · H | **H (I)** |
| G21 | LOG L108, L121 | H · H, N (yielded) · H, N | **H, N** (B, C) |
| G22 | LOG L110 | N · H, with C's note · H, note | **H, note** (B, C) |
| G23 | LOG L118 | H (W) · H, S in part (yielded) · H, N (SP-10, conceded) | **H, N** (A and C hold H without S) |
| G24 | LOG L128 | H · H, S anchor · H, optional mark (SP-6) | **H, optional anchor mark** |
| G25 | LOG L137 | N · H, N (yielded) · H, N | **H, N** |
| G26 | LOG L148 | S · S in part · S in part | **S in part** (B, C) |
| G27 | LOG L155, L159 | N · H, N (yielded) · H, N | **H, N** |
| G28 | LOG L158 | N · S in part · H, N (SP-8, conceded) | **H, N** (A, C); B named |
| G29 | LOG L161, L244 | N · H, N (W) · H, N | **H, N** (label W) |
| G30 | LOG L182; L183; L196; L197 | S; N; H; H · S, N; H; N; N · H, N (SP-9); H; N; N | **L182 S, N** (A, B); **L183 H** (B, C); **L196, L197 H, N** (B, C) |
| G31 | LOG L204 | H · H · H, N (SP-11, conceded from S) | **H** (A, B) |
| G32 | LOG L206 to L221 | per line (section 1.2) | **H**; **S in part** at L214, L221 (all, after B yielded and C's SP-12); **H, S in part** at L207, L209 (B, C); **H, N** at L206, L208, L212, L215 to L219 (A, C; C conceded, SP-8); **H** at L210 (A, B), L213 (B, C) |
| G33 | LOG L224 to L228 | N · H; H, N at L225, L226 (yielded) · H; H, N at L225, L226 | **H**; **H, N** at L225, L226 |
| G34 | LOG L232 | N · H, N · H, N (SP-13, conceded from S) | **H, N** |
| G35 | LOG L235 | S · H · H (SP-14) | **H** (B, C); A named |
| G36 | LOG L248 | S · H, S in part · S in part | **S in part** (B, C); S9-RF-5 stands (all) |
| G37 | LOG L254 | N · S in part · S in part (SP-15) | **S in part** (B, C) |
| G38 | LOG L257 | N · S in part (yielded) · S in part (SP-15) | **S in part** (B, C) |
| G39 | LOG L258 | N · H, N · S in part (SP-15) | **H, N** (A, B); C named |
| G40 | LOG L264 to L266 | N · S in part · S in part (SP-15) | **S in part** (B, C) |
| G41 | LOG L267 | N · N (yielded) · N | **H, N** |
| G42 | LOG L270 | N · H · H | **H** (B, C) |
| G43 | LOG L271 | S · S (yielded) · S | **S** |
| G44 | LOG L274 | N · S in part (yielded in part) · S in part (SP-15) | **S in part** (B, C) |
| G45 | LOG L276 | N · H · H | **H** (B, C) |
| (others) | LOG L117; L171; L183, L185, L190; L213; L224 | H · H (S) · H, N; N · H · N; N · H · H; N · H · H; N · H · H | **H** (A, B); **H, N** (A, C); **H** (B, C); **H** (B, C); **H** (B, C) |

### The splits in claim or addendum text, and how they were settled
| # | Point | Positions after Round 3 | Settlement (where in the piece) |
|--:|---|---|---|
| 1 | **What is written** (B S-1; C SP-16; A SP-10) | all: Steps −1 to 10, the Step 10 review accepted (A and B conceded) | **C's form** (AS9-1) |
| 2 | **The layer's coverage in the standing addendum** (B S-2) | none of the three Round 1 wordings; each objected to the others' | **per-piece coverage, then the gap sentence** (B's S-2) (AS9-1, AS9-16) |
| 3 | **The units' status in the addendum** (C SP-17; A SP-11) | A, C: per unit; B: "ten units, all PROPOSED" (its own snag 2 contradicts it) | **per unit** (A, C) (AS9-1) |
| 4 | **Item 5** (A SP-1; B S-3; C SP-27) | all: not run (B withdrew) | **not run; B's check named a reader's re-check** (AS9-5, AS9-15) |
| 5 | **S9-RF-5** (A SP-2; B S-4; C SP-20) | all: stands (B withdrew) | **stands** (AS9-13) |
| 6 | **The audit "measures nothing here"** (A; B SA-5 CONFIRM; C's A-7 OBJECT) | A, B: measures nothing; C: overstates, the sweep rows are printed | **the narrower words, which A's own K7 uses:** a self-test, not a check of Mirny's handoffs, beside the printed sweep rows (AS9-13) |
| 7 | **MP-1, MP-2** (A SP-3; C SP-21; K7) | A, C: changed output, history unverified; B conceded | **changed output, repair unrecorded** (AS9-12) |
| 8 | **MP-18** (A SP-4) | B, C: in part; A conceded | **in part** (AS9-12) |
| 9 | **When the corrected row is committed** (A SP-5) | A, C: with the developer's acceptance (PR-14); B: with this Record's addendum | **A, C** (AS9-3) |
| 10 | **Where the addenda live** (A SP-6; B S-9; C SP-22) | A, B: a separate file beside; C conceded | **a separate file; at most an end-of-file pointer** (AS9-2; DEC-103) |
| 11 | **Where the docket marks go** (B S-8) | A, B: end-of-file notes; C: end of a line | **end-of-file notes** (A, B) (section 7) |
| 12 | **Killed findings answered later** (A SP-7; B S-6; C SP-19; K4) | A: five, one half-answered; B: five, the fifth in part, plus coinage marks; C: four | **five, one in part only** (A, B); **C named** (AS9-19) |
| 13 | **What is stale on LOG L96** (A SP-8) | A: both marks; B (G17): both; C: the wind call | **both marks** (A, B) (AS9-19) |
| 14 | **LOG L94's category** (A SP-9) | A: C · I; B: I; C: — | **C · I** (A; B, C compatible) (section 1.2) |
| 15 | **The tracker line** (A's; B S-7; C SP-18) | B and C each proposed a merged line; A's left out Step 10 (conceded) | **settled in merge:** B's and C's lines combined (AS9-10) |
| 16 | **Number collisions** (A SP-12; B S-10; C SP-25) | all after concessions: +8, P08 in place of PRT | **+8 with these members, plus this piece** (AS9-20) |
| 17 | **Line-drift recurrence** (B S-11) | A, B: +6; C: "+8 at least" | **+6 at least** (A, B) (AS9-20) |
| 18 | **R-172** (A SP-13) | A, B: five of six; C: done | **five of six** (A, B) (AS9-22) |
| 19 | **R-178** (A SP-14) | A, B: open and larger; C: partly answered | **open and larger** (A, B) (AS9-22) |
| 20 | **Q-140** (A SP-15; B S-12) | A: for this repass only, open as method; B, C: answered for the repass | **answered for this repass only; open as method** (all compatible) (AS9-22; AQ-162) |
| 21 | **Q-144** (A SP-16) | A, B: in part; C: answered "no" by the tool | **in part** (A, B) (AS9-14) |
| 22 | **The register's under-reach** (A SP-17) | A: reserved; C: a Log problem and an observation; B: absent | **the fact into the Log (A, C); its reading as the dominant shape reserved** (AS9-24 C′.9; RF-ST9-6) |
| 23 | **M-283 to M-298** (A SP-18) | A, B: assigned or used, text not verified; C conceded | **A, B** (AS9-4) |
| 24 | **The table's gaps** (A SP-19) | A: reported; C conceded | **reported** (AS9-3) |
| 25 | **F-1** (A SP-20) | A: proposed for closing; C: closed by ruling; B: not listed | **proposed for closing** (the conservative reading: no ruling closes it) (AS9-6) |
| 26 | **The Step 5 Round 2 mismatch's class** (A SP-21) | B, C: what failed; A conceded | **what failed** (AS9-24 C′.3) |
| 27 | **The concurrency's class and cause** (A SP-22; C SP-24; K3) | all: a failure; its cause on no admitted line; the instruction is context only | **a deviation; the cause from the orchestrator's account (ORCH), marked so** (AS9-24 C′.1) |
| 28 | **`DR-57` against `DR-76` as a contradiction** (A's D′.4; C's A-2 OBJECT; B SA-8 CONFIRM in part) | A: a contradiction; C: a stale notice; B: the facts confirmed, "every pass file" not checked | **no two-reader position on the class; the most conservative: stale notices, not a contradiction** (AS9-18) |
| 29 | **The Step 9 datasheet's L5 as a precedent** (C's A-3; A's 2f-5) | A withdrew; C: cite the words for the convention only | **the intention, not the practice** (AS9-2) |
| 30 | **The `unmet` label** (B S-14) | A, C: W; B withdrew U | **W** (AS9-7) |
| 31 | **LOG L21's label** (B S-15; A SA-3) | A: T; B: an anchor; C: N | **T as a pointer, with an anchor mark** (section 1.2) |
| 32 | **Would the register have needed rows** (B S-13) | three different subsets; all: pointer rows only | **the union, pointer rows only** (B's form) (section 1) |
| 33 | **PROOF slips as a recurrence row** (C SP-26) | C: a new row; B: the shape confirmed; A: its own snag 10 | **a new row** (AS9-20) |
| 34 | **The wind pieces' status snag** (C SP-28) | A: the brief called them accepted; C conceded its "status lines lag rulings" | **A's form** (AS9-24 B′.2) |
| 35 | **Steps −1, 0, 1 and 3 in the gap** (C's K6 narrowing) | A, B: in the gap; C: not checked, not a known gap | **C's narrower reading** (claims less; compatible) (AS9-16) |
| 36 | **The T5 recommendation** (B S-5) | A: stands, sharper; B: hold for a fresh panel; C: owed or retired by ruling | **C's framing** (B conceded); the recommendation in DEC-104 is B's Round 1 option, the one that changes least now (AS9-14) |
| 37 | **Finding, request, question and decision numbers** (A SP-23; B 2.6; C 2f) | three colliding sets in all three | **this merge's set**, in the order of the Record's items then the Log's sections (the brief's rule) |

### Single-finder finds, checked against the pass lines in Round 3
| Find | Finder | Checked by | In the merge |
|---|---|---|---|
| The coverage gap | A | B, C CONFIRM (C narrowed) | AS9-16; DEC-100 |
| The audit's YES is a self-test; 0 outbound rows | A | B CONFIRM; C CONFIRM narrowed | AS9-13 |
| The founders script's zero beside a known source lag | A | C CONFIRM (not verified) | AS9-8 |
| Steps 9 and 9.5 carry no amendment notice | A | C CONFIRM (objecting to its supporting cite) | AS9-2 |
| LOG L94's census-row kill now readable | A | B CONFIRM; C CONFIRM, the ruling not pinned | AS9-19 |
| LOG L99 re-grounded (C3-23, C3-24 candidates) | A | B CONFIRM (one citation objected: L99 cites M-263); C CONFIRM as candidates | AS9-19; section 3 |
| LOG L102's kill predates `DR-99` | A | B, C CONFIRM | AS9-9 |
| LOG L80's dead end may lack the robot-keyed term | A | C CONFIRM (reserved) | RF-ST9-7 |
| LOG L21 and L260's table carries the as-written tiers | A | B, C CONFIRM (a pointer) | AS9-17 |
| The register's REWORD (L124) and KEEP (L132) on the Phase 9 amendments | A | B, C CONFIRM | AS9-24 B′.5 |
| The decisions file out of numeric order | A | C CONFIRM | section 2 |
| MP-20 to MP-26 | A | B, C CONFIRM (as proposals) | AS9-25 |
| Item 5 for the repass: the concurrency markers | A | C CONFIRM | AS9-26 |
| `DR-85`'s "Not decided" row | A | C CONFIRM (a pointer) | section 6 |
| A ruling applied to some sources only | A | C CONFIRM | OBS-9 |
| The observations log runs 30 lines past the span | A | B CONFIRM (`wc -l` 8,586) | AS9-4 |
| `DR-57` against `DR-76` as a contradiction | A | B CONFIRM in part; C OBJECT | split 28 |
| LOG L21 (+5), L67 (+2), L128 (+4) | B | A, C CONFIRM | AS9-5 |
| LOG L96's and L98's coinage | B | A, C CONFIRM | AS9-19; DK9-22 |
| Item 5's deferral (`P2` L518, `P3` L495) | B | A CONFIRM | AS9-15 |
| The Step 7 closing test still says not finished (`AS7` L25) | B | A, C CONFIRM | AS9-1 |
| The repo pointer spliced mid-sentence (`DS9` L5; `AS8` L539) | B | A CONFIRM (DS9 only); C CONFIRM | OBS-16 |
| The census's singular Primary (`CEN` L36) | B | A, C CONFIRM | section 6 |
| The Step 9 quick reference's L15 against `RB` L2995 | B | A, C CONFIRM | section 6 |
| R-178 now larger | B | A CONFIRM | AS9-22 |
| Readers who read out of order or partly (`AS6` L586; `AS5` L597) | B | C CONFIRM | AS9-24 C′.7 |
| MP-12's verifier fix (`DRL` L1712) | B | C CONFIRM | AS9-12 |
| "which let three Step pieces run at once" | B | A, C OBJECT | claims not accepted |
| "Recording a defect did lead to its repair, later" | B | A, C OBJECT | claims not accepted |
| "U2 used two of them" | B | C OBJECT | claims not accepted |
| REC L27: the heritage script ran (U0) | C | A, B CONFIRM | AS9-6 |
| REC L37: the standout not kept (`AS8` L20) | C | B CONFIRM; A names it | AS9-7 |
| REC L3 stale in part | C | B OBJECT | tag R1: H |
| The Lover faculty row blank by ruling (`DRL` L1218) | C | B CONFIRM | AS9-7 |
| The T5 deferral closed as "not applicable" | C | A, B CONFIRM | AS9-14; OBS-11 |
| D.7, siligel, persists (`AP8` snag 14) | C | B CONFIRM; A not re-checked | AS9-18 |
| The cron deleted before U9 finished; U5's times | C | A, B CONFIRM | AS9-24 C′.5 |
| Rule 3's readings not shown; a compressed U0 | C | A, B CONFIRM as C states it | AS9-24 C′.6 |
| Step 5's Round 2 slip not repaired, where earlier pieces repaired | C | B CONFIRM | AS9-24 C′.3; OBS-12 |
| U5's Phase 9 input not yet finished (`AP10` L4) | C | A CONFIRM | AS9-24 C′.1 |
| The Phase 8 axis wording only in the register | C | B CONFIRM | not carried as a finding (Step 6's matter, `AS6` AR-104) |
| `REG` L57's source cell lags its text | C | A, B CONFIRM | AS9-9; section 6 |
| Step 5's feed line moved (`05` L714 → L718) | C | B CONFIRM | AS9-24 B′.3 (as drift) |
| The census-row chain | C | B CONFIRM in part (one join not shown) | claims not accepted (the join); "moved twice" only |
| Collisions +8 counting PRT | C | A, B OBJECT | split 16 (C conceded) |
| `DR-74`'s note on another location's measurement | C | B CONFIRM (a pointer) | section 6 |
| `UEIC` L624 | C | A CONFIRM in part; B CONFIRM | section 6 |
| RF: the repass's speed against LAW 0 | C | A, B CONFIRM (reserved) | RF-ST9-9 |
| Round 3 strikes +12 | C | B CONFIRM in part | not carried as a count (AS9-20: *not re-counted*) |
| The register's section 3 still unverified | C | A, B CONFIRM on `AREG` L7 | AS9-24 C′.9; AR-170 |
| Spec L93's ranking clause | C | A CONFIRM | section 6 |
| F-1 "closed by ruling" | C | A OBJECT | split 25 |
| `DR-85`'s line-citation remap (new in Round 3) | C | none (no later round) | **a request only** (AR-165) |
| The shared Founding Register slip (new in Round 3) | C | none in Round 3; **all three readers' own Round 1 snags record it** (A 10; B 1; C 15) | AS9-20; OBS-15 |

### Claims not accepted (left out of the merge; each listed with what was done)
| Claim | Whose | Objected to by | Why | In the merge |
|---|---|---|---|---|
| "the instrument validates as of 2026-11-04"; S9-RF-5 "is answered for later runs" | B (AS9-7) | A, C (B withdrew) | the YES is on the built-in controls with 0 rows; nothing shown about later runs | S9-RF-5 stands (AS9-13) |
| "met in the tool" (MP-1, MP-2); "MP-1 to MP-3 as met in the tools" | B (AS9-9, AQ-154) | A, C | changed output only; no repair record; MP-3 one half | changed output, repair unrecorded (AS9-12) |
| "Recording a defect did lead to its repair, later"; "were repaired" | B (an observation entry; AS9-15) | A, C | a cause and a repair no line shows; B's own RF-ST9-3 declines it | not carried; RF-ST9-3 keeps it not adopted |
| "committed with this Record's addendum" | B (AS9-5) | A | contradicts PR-14, which B cites a line earlier | with the developer's acceptance (AS9-3) |
| "the item-5 sweep, run here on this step's own pointers only" | B (AS9-3) | A, C (B withdrew) | a partial pointer check, not item 5 | a reader's re-check (AS9-5) |
| "ten repass units, all others PROPOSED"; "ten units, all PROPOSED"; "repass U0 to U9 DONE (PROPOSED)" | B (AS9-1, AS9-18, AS9-11) | A, C | U0 a recheck, U1 a docket, two pieces ACCEPTED; Step 10 missing | per-unit statuses (AS9-1, AS9-10) |
| "which let three Step pieces run at once" | B (A′3) | A, C | presents the deviation from the order as a technique's benefit | not carried; recorded as a failure (AS9-24 C′.1) |
| "no old figure reached a live claim" | B (A′6) | A | a universal claim no shown check supports | the rule stated per piece; no cross-piece check shown (AS9-24 A′.7) |
| "questions AQ-27 to AQ-142 likewise" under counts the repass added | B (AS9-18 item 9) | A | the count is not shown; includes a piece from before the repass | not carried; counts per unit (section 2) |
| "number collisions (four units)" | B (G′) | A, C (B withdrew) | undercounts | +8 (AS9-20) |
| "Phases 2 to 10 ... re-derived" | B (AS9-1) | C (B withdrew) | overstates coverage | per-piece coverage and the gap (AS9-1, AS9-16) |
| "U2 used two of them (PIU AR-52)" | B (A′7) | C | one drift is shown used | not carried |
| "re-derives Phases 2 (composition), 4 and 7 (the robot term), 5 to 10" | A (AS9-1) | B, C | overstates Phase 5 | as above |
| "Steps −1 to 9" in the standing and tracker lines | A (AS9-1, AS9-11) | B, C (A withdrew) | leaves out Step 10's accepted review | Steps −1 to 10 (AS9-1, AS9-10) |
| "number collisions +6" | A (recurrence addendum) | B, C (A withdrew) | P9 L7 and ST7 L7 also record renumbering | +8 (AS9-20) |
| "The M-265 sighting the Log cites at L99" | A | B | L99 cites M-263 | corrected (section 3) |
| the Step 9 datasheet's L5 as practice ("already places pointers at the end of a file") | A (AS9-17) | C (A withdrew) | that pointer is spliced mid-sentence near the top | the intention, not the practice (AS9-2) |
| line totals of part-admitted files from `wc -l` | A | C | not from admitted lines | labeled "tool count" (section 2) |
| "re-derives what rested on the retired wind reading" | C (AS9-1) | B | implies full coverage | per-piece coverage and the gap (AS9-1, AS9-16) |
| "M-283 to M-298 were appended"; "[appended; cited in the runbook]" | C (AS9-12, DK9-16) | A, B (C conceded) | drops its own "not verified as worded" | in use; text not verified (AS9-4) |
| "[resolved: U0; `ST6` PR-1, PR-2]" for REC L49 | C (DK9-8) | A | the gaps are only reported; the table was not opened | reported (AS9-3; DK9-10) |
| "[repaired by 2026-11-04 (U0); change unrecorded]" | C (DK9-14) | A | asserts a repair | output changed, no repair recorded (DK9-24) |
| F-1 "is closed by ruling" | C | A | a PROPOSED close in a PROPOSED piece | proposed for closing (AS9-6) |
| "R-172 done as standing brief lines" | C (AS9-13) | A | five of six; the entry-map line not shown | five of six (AS9-22) |
| "R-178 partly answered" | C (AS9-13) | A | `DR-80` and `DR-105` reach no R-178 candidate | open and larger (AS9-22) |
| Q-144 answered "no" by the tool | C (AS9-13) | A | hides its second half | in part (AS9-14) |
| collisions "+8", counting `PRT` L7 | C (AS9-16) | A, B (C conceded) | `PRT` L7 shows no collision | +8 with P08 (AS9-20) |
| the census chain "L590 → L629, now L500, L642" | C (AS9-8) | B | joins two different anchors; no line shows L629 → L642 | *the census rows twice* only (AS9-24 B′.3) |
| "AR-77 to AR-79 were never used" | C (section 2) | B | true of the admitted pieces only | not carried |
| an observation title "were found repaired" | C | B | only changed output is shown | "a tool's verdict changed with no recorded repair" (OBS-2) |
| "Status lines lag rulings" (the wind pieces) | C (its B.4) | A (C conceded) | the briefs had called them accepted | A's form (AS9-24 B′.2) |
| the addenda "appended to" `09_Record.md` and `09.5_Log.md`; AQ-150's form | C | A, B (C conceded) | "Never edit a pass file." (`QUEUE` L14) | a separate file (AS9-2) |
| the extra label U for the single `unmet` | B | A, C (B withdrew) | the five labels suffice; its ground was the coinage | W (AS9-7) |

## Settled in the merge (beyond the splits)
- **Union applied:** A (the coverage gap; F-bis; MP-20 to MP-26; item 5 for the repass; the self-test reading of the audit; the register's REWORD against KEEP; the decisions file's order; the observations log's tail; RF-ST9-5, RF-ST9-6, RF-ST9-7); B (the Log's own anchors at L21, L67 and L128; the coinage marks; the census's singular Primary; the quick reference's L15; the datasheet splice; readers who read out of order or partly; the K-point texts not kept; the completion note stale; head-of-file notices as RF-ST9-8); C (the heritage script run; the standout not kept; F-1; the Lover row blank by ruling; the deferral closed as "not applicable"; the Round 2 repair rule varying; the cron and the clock; rule 3's readings; U5's unfinished input; the register's section 3; `REG` L57's source cell; `UEIC` L624; the spec's ranking clause; D.10 to D.12 and D.15 resolved in method; the per-unit status; the S/H/N merge rule; `DR-85`'s remap as a request; the shared Register slip).
- **The orchestrator's account (ORCH)** is used, marked, for four things no file carries: the cause of the parallel run (on the orchestrator's judgement under the developer's instruction to continue; the developer did not specifically instruct parallelism); the developer's full words on continuing and on the 3 pm window; the full wording of the question that added U10 and U11; and the audit's self-validation once a record exists. **No other cause was written**; the three readers had each recorded the cause as on no admitted line, and that record stands beside the account.
- **Decisions DEC-100 to DEC-104:** DEC-100 (the coverage gap) from A's find and the orchestrator's instruction; DEC-101 (the parallel run) from C's DEC-101 and A's and C's AR-165, reframed by ORCH; DEC-102 (the sweep's timing) from C's DEC-100; DEC-103 (where the addenda live) from A's DEC-100 and B's AR-160; DEC-104 (T5) from C's AR-167 and B's AQ-153.
- **The Step 10 piece** (U11, concurrent) was in the folder with its T8 record when this merge finished; for the cross-reference note only, its header, section 0 and its rows naming Step 9 were read. Nothing in the findings was changed by it.
- **Figures:** the live set appears in the header and in AS9-23 §10 only; the as-written tier figures only in AS9-17's "as written" line and in section 3's T bullet as a pointer. Shares are weights, never head counts.
- **The coinage** appears in the piece only inside quoted kill-list words of the Log and in statements that it is coinage; no group is named by it and no replacement is coined.

## Kept files (`M-132`)
The Round 1 outputs `.t8_amend_ST9_readerA.md`, `.t8_amend_ST9_readerB.md`, `.t8_amend_ST9_readerC.md` and the Round 3 replies `.t8_amend_ST9_round3_readerA.md`, `.t8_amend_ST9_round3_readerB.md`, `.t8_amend_ST9_round3_readerC.md` are kept in this folder as the round's working record, unedited, beside `.t8_amend_ST9_round2_raw.txt`, the frozen brief `.t8_amend_ST9_brief.md` and the list `.t8_required_amend_ST9.txt`; all are byte-identical to the scratchpad copies in `amend_ST9/` (`cmp`, by this merge). **No checkpoint file exists for this piece.** None of these files is an input to any later step; this record and the piece are the merged result. No helper file was created in the repo by the readers or by this merge (scratch work stayed in the session's scratchpad, `st9_merge/`).

## Quotation audit (`Tools/quotation_audit.py`, `--files Amendment_Rederivation_ST9_RecordLog_2026-11-04.md --own-pass`) · 2026-11-04 about 12:43, run before this record existed
raw output, excerpted (1 line omitted: the positive control "HARD - case mismatch", whose test phrase names another location; it is one of the controls behind the instrument line below, which reads VALID; the whole output is in the session scratchpad at `st9_merge/qaudit_final.txt`):
```
pass audited : Mirny
corpus mode  : default (own pass excluded)
corpus files : 6089   chars: 69,798,808
files audited: Amendment_Rederivation_ST9_RecordLog_2026-11-04.md
own-pass mode: a quotation may also be found in this pass's OTHER files (never in its own file)

=== POSITIVE CONTROLS ===
  [easy                      ] FOUND     a terminus is nobody's midpoint
  [HARD - blockquote wrap    ] FOUND     A pass may not proceed to Step 5 with a NEVER CITED row
  [HARD - outside Worldspace ] FOUND     Paste raw QA scan output into the QA block. Never summa
  [HARD - long wrapped       ] FOUND     Different content is not differentiation; a different q

  INSTRUMENT VALID: YES
  NEGATIVE CONTROL (must be absent): PASS - absent

=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 66
NOT FOUND in corpus: 30
  of those, in TABLE CELLS : 0
  of those, in PROSE       : 30

  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:273]           e3 and e4 are answered by dr-56 ( drl l1124) and e1's own correction states the retired premise ( as7 as7-18) (a, c) rec l19, f-1:
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:273]           ( as8 l20) (c; a, b confirmed) rec l40, the row's six stale lines ( as6 l20) log l96, the killed
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:273]           ( ap7 l275) log l96 and l98, the coinage inside the kill lists ( drl l1150) (b; a, c confirmed) log l99
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:288]           both conceded to c ( drl l1225) (s-1, sp-16, sp-10). the amendment layer, per unit (c's form, a and b conceded; b's
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:294]           only ( drl l1153; areg l173). a notice inserted at the top would shift every cited line , the drift of as9-5 (a, b). where the add
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:304]           sp-11 and k8). obsl has 8,586 lines by wc -l (a tool count; b and a), so the next free number is at least m-302 and is known only 
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:308]           withdrawn). this is a reader's re-check of step 9's own pointers, not the item-5 sweep (k5, all three; b withdrew its
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:329]           not accepted). the holes at gate 1 (water, emissions) are untouched ( as7 as7-2). the station-heritage script ran on 2026-11-04 (u
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:334]           ( as8 l17): nb-2's want becomes declined , provisional on ar-140 (dec-080); the two compulsion refusals are aligned at declined , 
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:379]           c agreed, s-4, sp-20). split in wording, settled: a's
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:384]           ( u00 l256), discounts the one line that merely mentions the faculty (l257) and says
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:384]           (l258). the by-hand comparison is still not recorded. the early verdict leans on the retired private-reading clause ( ap6 l344, wh
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:384]           ); the step 8 piece does not re-run t5 ( as8 l280) and closes with
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:384]           ( as8 l560): the deferral reached its named step and was closed there without being discharged (c; a, b confirmed). settled framin
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:384]           compatible): the late comparison is owed on the corrected account, or t5 is retired for mirny by ruling; waiting for a fresh panel
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:399]           re-derives what rested on the retired wind reading
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:413]           ( as8 snag 5); nns l15 against dr-55 q-77 on naming a station's owner ( ap8 snag 5; ad8 6); the language rule across the layer, th
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:512]           against nine or ten in seven briefs ( apiu l254; ap9 l257; ap10 l521; as5 l580; as6 l576; as7 l577; as8 l533); q-81 under dr-55 ( 
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:536]           any name for the curating organization or the protocol, the coinage for any group
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:538]           item 5 covers the pass's own files ( rb l3013) b, at k5; s9-rf-5
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:538]           the yes is a self-test b, on a's reading; a coverage addendum for phases 2 to 10 phases 3 to 5 have no wind piece b, at k6; addend
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:538]           ( queue l14) c, on a's and b's reading; three settled kills the majority holds five, one in part c, at k4; a snag that
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:569]           has to mean), dec-121 (when step 10 is re-run), dec-122 (which lessons go into the rules) : this piece's mp status table (as9-12) 
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:578]           (mirny repass, 2026-11-04) (a, b, c; the cause from orch). the order was
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:579]           on its built-in controls, with 0 outbound rows for the pass; the founders script became scoped; the t5 check found a dedicated mar
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:588]           (mirny phase 6 piece step 8 piece) (c; a, b confirmed). t5 was left
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:729]           (brief c.2) yet is entry 38, read whole (all three)
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:729]           (brief a result (6)) while two are accepted and u0 and u1 are not pieces; the phase 9 piece is placed in the layer
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:739]           the layer re-derives phases 2 to 10 ; a cause for the parallel run read out of the developer's instruction; a name for the curatin
  [Amendment_Rederivation_ST9_RecordLog_2026-11-04.md:739]           for any group; the addenda appended to the old files

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```
**Triage by hand (each of the 30 misses read and classified):** 66 fragments tested, **30 not found** (0 in table cells, 30 in prose). **29 are connective prose** captured between two adjacent quotations on one line (the audit's own warning) or this piece's own wording on lines that also carry quotations: the section 3 lists (L273), the findings' notes (L288 to L413), the Log addendum's lines (L512, L536, L538), the cross-reference note (L569), the observation entries (L578, L579, L588) and the snags (L729, L739). **One is a quotation of a reader's own Round 1 text**, which the audit's corpus cannot see because the reader files are dot-files: L399, "re-derives what rested on the retired wind reading", exact text of reader C's AS9-1 addendum (`.t8_amend_ST9_readerC.md`, found by `grep -c`: 1; it is also quoted in reader B's Round 3 reply). **No misquotation was found by the audit.** An earlier run (about 12:41, same instrument line) gave 29 misses; between the two runs seven phrases of this merge's own wording that stood in quotation marks were set in italics, one paraphrase of a Log kill was replaced by its exact text, and one finding's live tier figures were removed so that it carries the as-written set only. **A supplementary check** of every double-quoted string in the piece of any length (a scratch script, `st9_merge/shortq.py`, normalizing dashes, quotes, markup, case and spaces, run with `python3 -I`) tested 254 strings against the Mirny folder's files **including the reader dot-files**, the rulings log, the runbook, the observations log, the Step 9 quick reference, the live sources at their files and the stereotypes law: **0 not found** (merge checks below). **After this run and the checks below, five phrases of the merge's own wording were edited in the piece** (the header's live-facts line, to name section 3's pointer as well; section 0 item 2 and AS9-1's addendum, to say the twelve pieces are counted before this piece and the Step 10 piece; section 2's first table, an unsourced explanation of the +3 shift removed; AS9-24 A′.4, the delegated-merge units narrowed to what `AS7` shows). **No quotation was added or changed. The audit was not re-run**, because this record now exists and the audit reads a pass's other files once a record exists (ORCH); the merge's own quotation check, which excludes both of this piece's files, and the other merge checks were re-run after the edits; the block below is that final run (one quoted string fewer, 254, after the header edit; nothing else changed).

## Merge checks
raw output (full; scripts in the session scratchpad `st9_merge/`, run with `python3 -I` on a copy of the final piece; the location-name scan's list is built from the spec file names, 39 names, and its positive control on a scratch text with three planted names found all three; names are not reproduced here):
```
$ python3 -I shortq.py ctl_piece.md   # positive control: two real quotations, one planted
quoted strings tested: 3; files in corpus: 375; not found: 1
  NOT FOUND: a planted sentence that exists in no file anywhere zq
$ python3 -I shortq.py <the piece in the Mirny folder>   # the piece itself is excluded from the corpus
quoted strings tested: 254; files in corpus: 374; not found: 0

$ python3 -I citycheck.py <Cities> ctl_names.md   # positive control: three planted names
== ctl_names.md: names scanned 39; hits 3
$ python3 -I citycheck.py <Cities> <piece>
== piece_for_checks.md: names scanned 39; hits 0

$ python3 -I idcheck.py <piece>
AS9 cited  : 1..26 (26 distinct)
AS9 headed : 1..26 (26 distinct)
AS9 in mapping table (bold): 1..26 (26 distinct)
cited but not headed: [] | cited but not in mapping: []
RF-ST9-: cited 1..9 (9 distinct); defined 1..9 (9 distinct); cited not defined: []
AR-: cited 160..171 (12 distinct); defined 160..171 (12 distinct); cited not defined: []
AQ-: cited 150..162 (13 distinct); defined 150..162 (13 distinct); cited not defined: []
DK9-: cited 1..29 (29 distinct); defined 1..29 (29 distinct); cited not defined: []
OBS-: cited 1..16 (16 distinct); defined 1..16 (16 distinct); cited not defined: []
DEC new in this piece: [100, 101, 102, 103, 104] | DEC-10x cited: [100, 101, 102, 103, 104]

$ python3 -I mixcheck.py <piece>
line-level mixes: 0

$ python3 -I keepcheck.py <piece>
L117: ...| §F L98 | "keepers, watch or crews as a caste" | H | H (W) | H | **H...
L425: ...on observance (now also "the forcing error", `AP6` A6-13); "keepers, watch or crews as a caste" (L98); a wind-reader ...
L426: ...- **Coinage marks** (B; A, C confirmed): LOG L96's "keepers inside a sector as fact", "keepers as a strike ri...
L426: ...C confirmed): LOG L96's "keepers inside a sector as fact", "keepers as a strike risk" and "asking keepers as groups",...
L426: ...e a sector as fact", "keepers as a strike risk" and "asking keepers as groups", and L98's "keepers, watch or crews as...
L426: ...s a strike risk" and "asking keepers as groups", and L98's "keepers, watch or crews as a caste", carry the pass autho...
L427: ...y on the lines then admitted; none was falsified. The word "keepers" in the Phase 7 and Phase 9 kill lists is the pas...
L739: ...loper's instruction; a name for the curating organization; "keepers" for any group; *the addenda appended to* the old...
occurrences of keeper/keepers: 8
```
**Reading the checks:** the quotation check's control found its two real quotations (`REC` L32 and `QUEUE` L3) and missed the planted one, as it should; the piece's 254 quoted strings are all found with the piece itself excluded from the corpus (374 files). No other location's name appears in the piece. Every AS9, RF-ST9, AR, AQ, DK9 and OBS number cited is defined, and every AS9 number is in the mapping table (section 1.3). **No line, and no finding block, carries both the as-written and the live figure sets** (an earlier run of the same check flagged AS9-17's block, which then held both sets on separate labeled lines; the live figures were removed from it). The coinage's eight occurrences are the Log's own quoted kill-list words, statements that the word is coinage, and the killed-drafts list; no group is named by it and no replacement is coined.

## American English sweep
raw output (full; script `st9_merge/ae_sweep.py` in the session scratchpad, run with `python3 -I` on both files; its positive control on a scratch text with thirteen planted British spellings and one 'judgement' found all fourteen; the kept-spelling count comes only from the output lines below):
```
== Amendment_Rederivation_ST9_RecordLog_2026-11-04.md (744 lines)
British-spelling hits: 0
'judgement' (kept spelling): 5
== Amendment_Rederivation_ST9_RecordLog_2026-11-04b_T8_Rounds.md (644 lines)
British-spelling hits: 0
'judgement' (kept spelling): 4
```
