# Mirny · Amendment re-derivation · Piece ST10 (Step 10, the Readiness Check) · T8 round record · 2026-11-04

**Companion to** `Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md`. Raw tool output is pasted, not summarized. Working files are in this folder as `.t8_amend_ST10_*` (byte-identical to their scratchpad copies where one exists: see Kept files). **This record, like the piece, does NOT declare the Mirny pass complete.**

## Setup
- **Reading list (trimmed, `DR-74`):** `.t8_required_amend_ST10.txt` (scratchpad copy `amend_ST10/t8_required_amend_ST10.txt`, byte-identical by `cmp`), **35 entries, about 5,433 admitted lines** (counted by this merge's scratch script on the files as they now stand: whole files by physical lines, spans by their ranges): the rules (entry 1, the stereotypes law; entry 2, the runbook at four spans, among them Step 10's live text L3057 to L3145; entry 3, the Step 10 quick reference); the auto-loaded memory index `MEMORY.md` (entry 4, read as the object of item 1; no other memory file opened); `06_Worked_Example_Provenance.md` (entry 5); the rulings log at 24 spans (entry 6); the live sources at Mirny's rows only (entries 7 to 12); the Step 10 datasheet (13); **Step 10 read whole** (14, 99 lines); `09_Record.md` (15); the Frame at three spans (16); the amendment layer from before the repass (17 to 26: the Phase 6, 7, 2 composition, 9 and 8 pieces, the Phase 8 dockets, the Idelsk-Uralia piece, the robot-term piece's first 30 lines, the amendment register, the reconciliation note's lines 1 to 120); the Phase 10, Step 5, Step 6, Step 7 and Step 8 pieces at L1 to L45 (27 to 31); and the repass's own files (32 to 35: the data recheck, the queue, the completion note, the decisions file). **The Step 9 and 9.5 piece (U10) was concurrent, not an input.**
- **Brief:** `.t8_amend_ST10_brief.md`, identical for A/B/C with `{X}` the reader letter; **sha256[:16] dd9c0a4181c96077** (computed by this merge on the folder copy, which is byte-identical to the scratchpad copy; the checkpoint records no hash). It carries eight orchestrator-verified results with sources, the developer's binding words, the stage order, nine traps and the standing lines.
- **Readers:** three Opus agents dispatched 11:30 on 2026-11-04, inside the 05:00 to 14:59 window (checkpoint; `REPASS_QUEUE_AND_PROGRESS.md`, row U11). None refused any entry. Graphify: reader A observed no hook notice; reader B saw none (and would have disregarded one under `DR-6`); reader C saw the hook fire twice in Round 3 and disregarded it under `DR-6`.

| Reader | Agent ID | Output lines | Bytes | PROOF blocks | Findings (Round 1 numbering) | Docket | Requests · questions · RFs |
|---|---|--:|--:|--:|---|---|---|
| A | `aff0ea2ef0117191a` | 729 | 91,061 | 35 | AS10-1 to AS10-18 | its AS10-18 (records notes) | AR-180 to AR-185 · AQ-170 to AQ-178 · RF-ST10-1 to RF-ST10-4 |
| B | `a7dfe5e1e3228c786` | 746 | 102,962 | 35 | AS10-1 to AS10-14 | notes inside AS10-1, AS10-2, AS10-14 | AR-180 to AR-186 · AQ-170 to AQ-176 · RF-ST10-1 to RF-ST10-4; candidate DEC-120 to DEC-123 |
| C | `a9018bbf1648ba9bf` | 800 | 94,846 | 35 | AS10-1 to AS10-19 | its AQ-174 (marks) | AR-180 to AR-186 · AQ-170 to AQ-176 · RF-ST10-1 to RF-ST10-6 |

Line and byte counts by `wc` on the folder copies (byte-identical to the scratchpad copies by `cmp`); PROOF blocks counted by `grep -c '^### PROOF:'` (35 each). Reader B's file has 746 lines by `wc -l`; the checkpoint records 745. Tool-use counts are not recorded in the checkpoint and are not given here.
- **Self-checks before handback (as each reader records):** A used `wc -l`, `awk`, `tail`, `od -c`, `cat -A` and `sed -n` on listed files to set counts and real last lines, and one `grep -c` and one `grep -nP` for line separators on Step 10 only (its snag 1). B ran one `wc -l` and `wc -c` pass over the 35 paths, and `grep` checks and `sed -i` corrections on its own output only (its snag 11). C used `wc`, `awk`, `tail` and `od`, and one `grep -c`/`grep -P` and one `awk` prefix print on Step 10 only (its snag 9). No reader generated a PROOF field by script, and no reader created a helper file.
- **Ruling-log freeze (`M-302`):** not checked by this merge writer.

## Round 1 headline claims (union, before Round 3)
| Claim | A | B | C |
|---|---|---|---|
| Item 1 | CHANGES; parked | STANDS WITH A NOTE (parked) | STANDS WITH A NOTE (parked) |
| The index line that fired | moved or reworded; re-classify | coordinates hold other lines; not located | "now sits at **L112** by text, and it is unchanged" |
| Index lines naming the next subject | two, "attribute-only" on one reading | not classified | two, run-order and status lines, not classified by rule |
| Item 1a | CHANGES; parked; evidence scan now | STANDS WITH A NOTE (parked); five hits | STANDS WITH A NOTE (parked); five hits |
| Item 1b | STANDS WITH A NOTE | STANDS WITH A NOTE, parked (K) | STANDS WITH A NOTE |
| Item 1c | CHANGES; re-run now | MUST BE RE-RUN, before any commit | MUST BE RE-RUN, now |
| Item 1c: what the admitted lines show | one content-class hit (`NOTE` L76) and one shape hit | not classified | "scope or relation, none content" |
| Item 2 | CHANGES; MUST BE RE-RUN AFTER APPLICATION (ground: `06` L413) | CHANGES ("FIRES (small)" in its AS10-3; ground: `06` L413) | CHANGES, and MUST BE RE-RUN AFTER APPLICATION (ground: the runbook's 1c test) |
| Items 3 · 4 · 5 | STANDS WITH A NOTE · CHANGES · STANDS | STANDS · STANDS WITH A NOTE · STANDS WITH A NOTE | STANDS · STANDS (N/A) · STANDS |
| Item 6 · item 11 | MUST BE RE-RUN, now and after | MUST BE RE-RUN, at the next handoff | MUST BE RE-RUN, now |
| Item 7 | CHANGES | STANDS (resolved) | STANDS (resolved) |
| Item 9 | MUST BE RE-RUN AFTER APPLICATION (existence half now) | MUST BE RE-RUN AFTER APPLICATION (after the U10/U11 merge, again after the answers) | MUST BE RE-RUN, now and after |
| Item 10 | CHANGES; MUST BE RE-RUN | CHANGES in part; re-run after R-183 | CHANGES, and MUST BE RE-RUN AFTER APPLICATION (`M-299` not cited) |
| The next subject in the body | named, as scope | withheld | named, as scope |
| §5's heading with no Nulls | found | missed | found |
| "The cold half of 10" undefined | found | found | missed |
| The T5 late marker | a "ready" condition | a Step 10 miss (Gate 0) | a "ready" condition |
| Open decisions | 21 Mirny entries | 25 in the file, 21 raised by the repass | "25 OPEN decisions" raised by the repass |
| PROPOSED pieces | ten | ten (P6 and P7 lag their rulings) | eight (its AS10-13); ten (its AS10-16) |
| Numbering | AS10-1 to AS10-18 | AS10-1 to AS10-14 | AS10-1 to AS10-19 |

## Round 2 (`Tools/triple_read_verify.py`) · run 2026-11-04 about 11:54 · first run NOT UNANIMOUS on one field (104 of 105 field sets, 35 entries); re-run UNANIMOUS (105 of 105)

**What happened.** On the first run, agent2 (reader B) failed one field: its LMID for `Founding_Register.md` (range 1-31, 57, 88: 33 admitted lines, so the middle line is the 17th, physical L17) gave the line after it, L18 (the continuation of point 5, which opens with a parenthesized `Post-War_Nations_Founder_Reference.md` and ends "is a CST task"), while the physical L17 is the line beginning "5. **Post-war framing comes later.**". Every other field of every block matched for all three. Reader B re-read L17 with Read and replaced **only that LMID field** with the exact line, and logged it as its snag 16 ("Round 2 repair (PROOF, entry 8, `Founding_Register.md`)"); nothing else in its output changed. The orchestrator then re-ran the verifier: UNANIMOUS. The first run's output was kept as `.t8_amend_ST10_round2_raw_FIRSTRUN.txt` (13,678 bytes) and the re-run is `.t8_amend_ST10_round2_raw.txt` (13,508 bytes); `diff` between them shows exactly two changed lines (the agent2 line of that block, and the verdict). It is a positional field slip of one line, not a content error; Round 3 proceeded on the repaired file. *(The checkpoint states the same, line 4.)*

**First run** raw output (full; file `.t8_amend_ST10_round2_raw_FIRSTRUN.txt`):
```
required files: 35
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 309-372,378-426,430-540,3057-3145] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Corpus_Reference_Sheets/Step_10_Readiness_Check_Full_Text_Quick_Reference.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/.claude/projects/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/memory/MEMORY.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/06_Worked_Example_Provenance.md ===
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
  agent2   ⛔ LMID  MISMATCH  claimed='(`Post-War_Nations_Founder_Reference.md`) is a CST task (`DR'  actual='5. **Post-war framing comes later.** Rows name founders in p'
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Step_10.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/10_Readiness_Check.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/09_Record.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P10_Catalog_2026-11-04.md  [range 1-45] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_S5_Reconciliation_2026-11-04.md  [range 1-45] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST6_Differentiation_2026-11-04.md  [range 1-45] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST7_QAGates_2026-11-04.md  [range 1-45] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST8_ReviewPanel_2026-11-04.md  [range 1-45] ===
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
⛔ NOT UNANIMOUS - DO NOT WRITE. Log which agent/file failed and why.
```

**Re-run after the one-field repair** raw output (full; file `.t8_amend_ST10_round2_raw.txt`):
```
required files: 35
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 309-372,378-426,430-540,3057-3145] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Corpus_Reference_Sheets/Step_10_Readiness_Check_Full_Text_Quick_Reference.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/.claude/projects/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/memory/MEMORY.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/06_Worked_Example_Provenance.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Step_10.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/10_Readiness_Check.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/09_Record.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P10_Catalog_2026-11-04.md  [range 1-45] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_S5_Reconciliation_2026-11-04.md  [range 1-45] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST6_Differentiation_2026-11-04.md  [range 1-45] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST7_QAGates_2026-11-04.md  [range 1-45] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST8_ReviewPanel_2026-11-04.md  [range 1-45] ===
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

## Round 3 (SendMessage to the same three agents) · 2026-11-04, replies time-stamped 11:58 to 12:00 · cross-check done
Each reader was sent seven points the three appeared to share (K1 to K7), a request to map the other two readers' re-derivations onto the old Step 10 items and list every status or central-claim split with the position it would hold, a request to check the single-finder finds against the pass lines, a numbering proposal, and a request to list any claim in the other two re-derivations it would not accept. Replies: `.t8_amend_ST10_round3_reader{A,B,C}.md` (205, 180 and 228 lines; byte-identical to the scratchpad copies `amend_ST10/t8_amend_ST10_round3_reader{A,B,C}.md` by `cmp`). **The text of K1 to K7 as sent is not in the folder; the topics below are read from the replies.**

| Reader | Part 1 OBJECTs | Part 2 splits listed | Single-finder finds checked | Part 3 claims not accepted | Coverage |
|---|---|---|---|---|---|
| A | 1 (K7, the label only) | 15 rows (concedes on items 1, 1a, 3, 4, 7 and 1c's targets) | B's 7 (all CONFIRM, two "soft"); C's 8 (all CONFIRM, one with a correction, one "as fact") | 8 | read B L1 to L459 and C L1 to L519 |
| B | 1 (K7, the label only) | 11 status splits and 6 central-claim splits (concedes on items 5, 6 and 11) | A's 11 (all CONFIRM); C's 8 (7 CONFIRM, 1 CONFIRM in substance with an OBJECT to the count) | 10 | read A L1 to L439 and C L1 to L513 |
| C | 1 (K7, the label only) | 14 splits and a minor tag group (concedes item 1's "unchanged", 1c's "none content", item 4's tag) | A's 9 and B's 6 (all CONFIRM), and the undefined "cold half" (CONFIRM) | 7, plus 5 self-withdrawals | read A L103 to L442 and B L111 to L455 |

### The shared points
| K | Topic (as read from the replies) | A | B | C |
|---|---|---|---|---|
| K1 | no reader declares the pass complete | AGREE (precision: ten pieces PROPOSED by their status lines; P2c and P8 ACCEPTED; U1 a docket CARRIED OUT) | AGREE | AGREE (the same correction: two ACCEPTED; eight repass pieces plus P6 and P7 PROPOSED) |
| K2 | the re-run and change set: 1c, 6, 9 and 11 must be re-run; 2 and 10 change | AGREE | AGREE | AGREE (concedes that `M-299` is the one finding verifiably in a rule file) |
| K3 | items 1, 1a, 8 and "the cold half of 10" stay parked; their evidence is stale; re-run, never reuse | AGREE (withdraws its CHANGES for 1 and 1a) | AGREE | AGREE (precisions: "the cold half" is defined nowhere, which it had missed; 1b is not a parked fire) |
| K4 | the index's L159 and L160 are stale status lines, item 9's matter, not item 1's | AGREE (concedes a miss) | AGREE | AGREE (adds L140) |
| K5 | what is kept of the next subject: process facts only, no content | AGREE (four process facts; proposes B's form, "the next subject", with the name once as scope) | AGREE (three process facts; the name withheld) | AGREE (the name as scope; three process facts; coordinates and tiers) |
| K6 | Q-145, the empty Nulls heading and the absent T5 late marker are notes or dockets, never rewrites | AGREE (the T5 absence is discharged by the Step 8 re-run or a fresh panel) | AGREE (confirms the Nulls point it had missed) | AGREE (the T5 note sits with Step 8; Step 10 lists it in Gate 0) |
| K7 | item 1c runs over all the repass's new prose before any commit (sent labeled as the stereotype-rule scan) | **OBJECT to the label:** it is the subject-name scan of one's own new prose, shape against content | **OBJECT to the label:** the same | **OBJECT to the label:** a name scan; the founders and heritage tool is another instrument |

**K7's correction is carried into the piece:** item 1c is a **name scan for the next subject**, never called the stereotype-rule scan (all three agree; the piece's section 0 item 4 and section 2).

### The splits, and how they were settled in the merge (the position two or three readers hold after Round 3; otherwise the most conservative reading; split named in the piece)
| # | Point | Positions after Round 3 | Settlement |
|--:|---|---|---|
| 1 | **Item 1 status** | all: STANDS WITH A NOTE (parked) (A conceded) | **STANDS WITH A NOTE (parked)** (AS10-4) |
| 2 | **Item 1: the line that fired** | A: moved or reworded, "unchanged" cannot be shown, L112 plausible; C: its title at L112 on one reading, reworded or not unverified (conceded "unchanged"); B: not located, and locating an other-location line is a use it would not carry | **no two-reader form; the most conservative:** the line is **not re-located** in this merge; re-locate, then re-classify, by an isolated reader (B; A's and C's hedged location not carried) (AS10-4) |
| 3 | **Item 1: the index lines naming the next subject** | A: "attribute-only" on one reading (B objected); B, C: not classified | **not classified** (B, C): coordinates only (AS10-4) |
| 4 | **Item 1b parked?** | A, C: not parked (the four fires are named); B: parked (K) | **not parked** (A, C) (AS10-6) |
| 5 | **Item 1a** | all: STANDS WITH A NOTE (parked) (A conceded); A, C: for the next subject two of the five hits stay open; A, C: an evidence scan may run now; B: nothing calls for it | **STANDS WITH A NOTE (parked)**; A's precision (C confirmed); the evidence scan **may** run now (A, C), B's point noted (AS10-5) |
| 6 | **Item 1c status and targets** | all: MUST BE RE-RUN, now, before any commit; targets: the next subject plus the subnet's two other un-run cities (B, C; A conceded) | as stated (AS10-7) |
| 7 | **Item 1c: what the admitted lines show** | A: one content-class hit, `NOTE` L76; B: A's (re-checked); C: conceded to A | **A's** (AS10-7) |
| 8 | **Item 2: label, ground and "fire"** | all: CHANGES (a split of label only on the re-run); ground: A, B on `06` L413, C on `RB` L3098 to L3099 (C's Part 3 objection: L413 sits inside another location's section); B's "FIRES (small)" objected to by C | **CHANGES**, the scan now and a re-run after application if a lesson enters a rule file; **the ground re-set to the runbook's 1c test** (the L413 ground is a claim not accepted); **not a fire** (AS10-8) |
| 9 | **Item 3** | all: STANDS (A conceded) | **STANDS** (AS10-9) |
| 10 | **Item 4** | A conceded to B; C conceded the tag (S) and holds STANDS WITH A NOTE | **STANDS WITH A NOTE**; L25 tagged S (AS10-9) |
| 11 | **Item 5** | A, C: STANDS WITH A NOTE (the checklist coordinates not re-verified; the readers' compliance unverified); B: conceded to STANDS, its caveat moved to "cannot prove" | **STANDS WITH A NOTE** (A, C), the caveat also in AS10-17 (AS10-9) |
| 12 | **Item 6 timing** | all: now, and again at the closing handoff (B conceded "now"; C: "now for this session, and again after any file move") | **now; again at the closing handoff and after any file move** (AS10-10) |
| 13 | **Item 7** | all: STANDS (resolved) (A conceded); A's restated criterion (C's Part 3 objection) | **STANDS (resolved)**, with B's and C's note; A's criterion not carried (AS10-11) |
| 14 | **Item 9 timing** | B: existence and listing now, again after the U10/U11 merge, the status half after the answers; C: holds B; A: existence now, status after (compatible) | **B's union** (AS10-12) |
| 15 | **Item 10** | all: CHANGES; A, B: `M-299` verifiably in a rule file (C conceded); A: re-run after R-183 and after application | **CHANGES; the evidence reading now; the verdict after R-183 and after application; cold half parked** (AS10-13) |
| 16 | **Snag 6's "L3074"** | A, C: item 1 now opens at L3075; B: the cited text is item 1a's, now L3086 to L3087, a +12 shift; A objected to B's "+12 section-wide"; B objected to A's and C's mapping | **no settlement on the referent; the most conservative form states the facts only:** item 1 opens at `RB` L3075; the `Disciplines/` text the snag describes is in item 1a at `RB` L3086 to L3087 (checked by this merge on the readers' own span); +12 is measured for one sentence only; which line the old L3074 named is left unsettled (AS10-18). **Listed as unsettled in the merge's final report.** |
| 17 | **Naming the next subject** | A, C: the name in the body as scope; B: withheld (A's Round 3 proposed B's form, with the name written once) | **never named** (B's form; the merge's instructions; the conservative reading) (snag 5) |
| 18 | **"No pass file edited; nothing committed"** | A, B: git-verified only for U0 and U1, the rest self-report; C: stated as fact (B's objection) | **A and B** (section 3; AS10-17) |
| 19 | **Open decisions** | A, B: 21 Mirny entries (`DECF` L55 to L224); C: "25 OPEN" (A's objection) | **21 Mirny entries; four others concern other locations, not used** (AS10-21; snag 15) |
| 20 | **PROPOSED pieces** | all after Round 3: ten by their status lines (C's "eight" objected to by A; C's K1 says ten) | **ten** (AS10-17; snag 2) |
| 21 | **Item 11 timing** | A: now and at the closing handoff; B: conceded "now" with a final run at the closing handoff; C: at the closing handoff (K2), now (Round 1) | **now (on the completion note and the queue); final at the closing handoff** (AS10-14) |
| 22 | **The held Planet** | B: recommends it is no ULM completion condition; A, C: ask; carry it as held, not cleared | **ask; carried as held, not cleared** (A, C); B's recommendation recorded in DEC-120 (b) (AS10-21) |
| 23 | **The lived middle's wording** | all leave it to the developer; B: keep it on the list until answered (C holds B's wording) | **on the list until answered** (AS10-21) |
| 24 | **Tags (minor; no status consequence)** | C's group: L28 H (B, C) against S (A); L82 S (A, C) against H (B); L86 S (B, C) against K (A); L51 H (A, C) against S (B); L58 H (A, C) against S (B); L67 H (A, C) against K (B); L25 S (A, B; C conceded) | **the two-reader tag each time** (section 1.1) |
| 25 | **How many handoff lines in the index** | C: four (L141, L155, L159, L160); A, B: three (L159 is a decisions line) | **three, plus the queue's handoff note** (section 3) |
| 26 | **"The wind re-derivation has run as ten pieces, entry 33 L36 to L45"** | B; A objected (those rows are eight pieces, a recheck and a docket; the wind pieces predate the queue) | **A's correction** (AS10-2) |
| 27 | **Finding numbers** | A: AS10-1 to AS10-24 (items 3 and 4 together, item 5 and item 8 apart); B: AS10-1 to AS10-23 (items 3 to 5 together, item 8 under the parked fires, a records docket last); C: AS10-1 to AS10-21 (items 6 and 11 together) | **B's set, AS10-1 to AS10-23**: all three agree on AS10-1 to AS10-8; B and C group items 3 to 5; A and B keep items 6 and 11 apart; B and C put item 8 under the parked fires |
| 28 | **Request numbers** | A and C: the same order for AR-180 to AR-188 (180 R-183 · 181 `06` · 182 item 1c · 183 git · 184 tracker · 185 register · 186 handoff · 187 warm-ruling words · 188 index currency); then A: 189 docket · 190 reconcile · 191 now-rows; C: 189 now-rows · 190 docket · 191 reconcile; B: a ten-item set with the now-rows first and the docket with the disagreements last | **A's and C's order for AR-180 to AR-188** (two readers); **C's order for AR-189 to AR-191** (B also puts the now-rows before the docket) |
| 29 | **Question numbers** | B and C nearly agree (AQ-170 lived middle, 171 Planet, 173 re-run timing, 175 keep parked); C: 172 the dated notes, 174 the cold half, 176 1b and 1c, 177 status surfaces, 178 `RC` L37, 179 parallel units, 180 the Phase 8 axis | **C's set, AQ-170 to AQ-180** (B's AQ-176 "item 1c now" folded into AR-182) |
| 30 | **Reserved-finding numbers** | A and B: eleven (different orders); C: ten (A's RF-1 and B's RF-1 merged) | **eleven, in B's order** (A's and B's count; C's merge of two different findings not used) |
| 31 | **Candidate decisions** | B: DEC-120 lived middle, 121 re-run timing, 122 MPs, 123 register section 3, 124 Planet; C: B's list with the Planet added; A: the re-run timing and the ULM-close questions | **three, batched:** DEC-120 (lived middle and Planet together), DEC-121 (re-run timing and "the cold half"), DEC-122 (the MPs); the register question kept as bookkeeping with a recommendation (AR-185), by the "few, developer-only" rule |
| 32 | **Where the T5 late marker belongs** | B: a Step 10 miss in Gate 0 (C confirmed); A, C: discharged by the Step 8 re-run or a fresh panel, not a Step 10 text docket | **both:** a Step 10 miss in Gate 0 outward, discharged under DEC-082 (section 3, R) |
| 33 | **B's `06` L317 to L330 citation** (a session that read another location's section) | B; C objected | **re-grounded on `06` L332 to L337 and `QUEUE` L11** (AS10-22) |
| 34 | **A's T-1 ground, `DRL` L1575** | A; C objected (the clause concerns another location's section of `16`); B confirmed T-1 citing L1575 and the robot-term piece | **re-grounded on `APRT` L4, L17** (section 3, T) |
| 35 | **A's use of the harness `git status`** (an out-of-list fact) | A; C objected | **not used as evidence;** AR-183 decides (snag 12) |

### Single-finder finds, checked against the pass lines in Round 3
| Find | Finder | Checked by | In the merge |
|---|---|---|---|
| Step 10 leaned on the register's unverified draft; the wind consequences' reach unmeasured (W-1) | B | A CONFIRM (soft) | section 3, W; AS10-17 |
| Item 9's PASS did not qualify Steps 5 to 8 against `DRL` L1125 (W-1) | C | A CONFIRM (soft), B CONFIRM ("the same miss as my W-1, from another side") | section 3, W (merged with B's) |
| Step 10 did not check the T5 markers; the late marker is absent today | B | A CONFIRM, C CONFIRM (as a Step 10 miss) | section 3, R; split 32 |
| The register's section 3 status lags the folder | B | A, C CONFIRM | section 3, R; AR-185 |
| `MEM` L159 against the 21 OPEN decisions | B | A CONFIRM | section 3, R; AS10-12 |
| `MEM` L160 against HEAD `8777bb5f` | B | A CONFIRM (a currency note), C CONFIRM (unresolved from files) | section 3, R; AR-183 |
| The Phase 6 and Phase 7 pieces' status lines still read PROPOSED | B | A CONFIRM | section 3, R; AS10-12 |
| The datasheet's own condition bars a verdict today (`DS10` L19) | B | A CONFIRM (soft), C CONFIRM | section 3, R; AS10-21 |
| The register's L96 also says the second slot is open | B | C CONFIRM | section 3, C |
| The Frame still states the old frame figures | B | C CONFIRM | section 3, C |
| L9's re-run list omits 1b and 1c | C | A, B CONFIRM | AS10-3 |
| No rule names which file is "the handoff" | C | A, B CONFIRM in substance (both corrected the count) | section 3, R; split 25 |
| Item 2's "no diff" against `DR-57`'s same-day rename; order unprovable | C | A, B CONFIRM | AS10-8 |
| The register has no Step 10 row | C | A, B CONFIRM | section 1.2 |
| The review notice omits the accepted Element | C | A CONFIRM (as fact, not a miss), B CONFIRM | section 3, S |
| Item 10's list of the layer's own recorded-not-implemented lessons | C | A, B CONFIRM line by line | section 2, item 10 |
| The phrase Q-149 quotes is in no line of today's index | C | A CONFIRM, B CONFIRM (as a null) | AS10-18 |
| `NOTE` L76 is a content-class item-1c hit | A | B, C CONFIRM | AS10-7; split 7 |
| For the next subject only `00` L9 and L2218 stay open | A | C CONFIRM | AS10-5 |
| Overlapping unit times against `QUEUE` L3 and L9 | A | B, C CONFIRM | section 3, R; RF-ST10-8 |
| The Phase 8 axis in three admitted lines | A | B, C CONFIRM | section 3, R; AQ-180 |
| L54's coordinates into file `16` probably stale | A | B CONFIRM (unverified), C CONFIRM (re-grounded) | section 3, T; split 34 |
| The Step 10 datasheet checks only `06` | A | B, C CONFIRM | section 3, R |
| §5's heading promises Nulls; none follow | A (and C) | B CONFIRM (it had missed it) | AS10-19 |
| Item 7 resolved at L5 while L44 and L73 read open | A | B, C CONFIRM | AS10-11; DK10-9 |
| "No pass file edited" git-verified only for U0 and U1 | A | B, C CONFIRM | section 3, R; split 18 |
| The Register row's sources cell lags its text | A (and C) | B CONFIRM | section 3, I |
| MP-11 looks not yet effective | A | B CONFIRM | section 2, item 10 |
| An "all of it" `06` row for Mirny's folder at the close | A | B CONFIRM (as a proposal, reserved) | RF-ST10-7 |
| `DR-55`'s deferred research questions in the "ready" list | A | C CONFIRM; B carries it | AS10-21 item 9 |
| "The cold half of 10" is undefined | A, B | C CONFIRM (conceded) | section 3, R; DEC-121 (c) |
| Old and new tool outputs are not like-for-like | B | (offered; carried by A and C in their RF lists) | RF-ST10-3 |
| L9 named on the same day as Step 10's file-system half; which came first is unprovable (B's R-3) | B | not checked by A or C | **not carried as a finding** (L9's staleness is shared by all three) |

### Claims not accepted (left out of the merge; each listed with what was done)
| Claim | Whose | Objected to by | Why | In the merge |
|---|---|---|---|---|
| The line that fired "now sits at L112 by text, and it is unchanged" | C (item 1, AS10-2) | A, B (C withdrew "unchanged") | the 2026-10-12 text is on no admitted line; `MEM` L4 points to a 2026-10-30 archive of longer wording; locating an other-location line | not re-located (AS10-4) |
| 1c's hits are "scope or relation, none content" | C (item 1c) | A, B (C withdrew) | `NOTE` L76 is content-class | one content-class hit recorded, not reproduced (AS10-7) |
| "25 OPEN decisions" raised by the repass | C | A | `DECF` L55 to L224 hold 21 entries; four others concern other locations | 21 Mirny entries (AS10-21) |
| "eight pieces are PROPOSED" | C (AS10-13) | A | ten by their status lines, as C's own AS10-16 says | ten (AS10-17) |
| "four handoff memories (entry 4 L141, L155, L159, L160)" | C (R-5) | A, B | L159 is a decisions line | three, plus the queue's note (section 3) |
| Item 1b "parked, K" | B | A, C | the developer parked four named fires; 1b is not one | not parked (AS10-6) |
| "the runbook's Step 10 section has moved +12 lines" | B (item 1a, AS10-3) | A | +12 is measured for one sentence; item 1's start moved by one | +12 for one sentence only (AS10-18) |
| "the wind re-derivation has run as ten pieces, entry 33 L36 to L45" | B (L5 row) | A | those rows are eight pieces, a recheck and a docket; the wind pieces predate the queue | corrected (AS10-2) |
| The next subject named in the body | A, C | B | the brief: other-city lines are not used and the snag is written without naming them | never named (snag 5) |
| The index lines naming the next subject classed "attribute-only" | A | B | classification is the isolated reader's job (R-184) | not classified (AS10-4) |
| Snag 6's L3074 mapped to item 1 at L3075 | A, C | B | the snag's text is about item 1a's `Disciplines/` clause | the facts stated, the referent unsettled (AS10-18; split 16) |
| Item 7 "CHANGES" | A | B (A conceded) | resolved 2026-10-21, before the repass | STANDS (resolved) (AS10-11) |
| The repass "edited no pass, culture, shared-table or discipline file and committed nothing" as fact | C | B | git verified it only for U0 and U1; the rest is the completion note's own statement | git-verified only for U0 and U1 (section 3; AS10-17) |
| Item 2's "no band" grounded on `06` L413 | A, B | C | that line sits inside another location's manifest section and names it | re-grounded on `RB` L3098 to L3099 (AS10-8) |
| Item 2 "FIRES (small)" | B (AS10-3) | C | a provenance date line is shape, not content | CHANGES, not a fire (AS10-8) |
| `06` L317 to L330 as a ground for the cold-run note | B (AS10-9) | C | a block about another location's session | re-grounded on `06` L332 to L337 and `QUEUE` L11 (AS10-22) |
| T-1 supported by `DRL` L1575 | A | C | that clause concerns another location's section of `16` | re-grounded on `APRT` L4, L17 (section 3, T) |
| The harness `git status` used as evidence for item 6 | A | C | not an admitted line | not used; AR-183 (snag 12) |
| Item 7's criterion "what must hold is that no *other* output sits in its folder" | A | C | an inference the runbook text does not state | not carried; "resolved" (AS10-11) |
| **Reader C's own Round 3 self-withdrawals:** 1c's "none content"; the L112 line "unchanged"; item 4 STANDS with L25 tagged H; item 10 without `M-299`; the undefined "cold half" missed | C | (itself) | — | each corrected as above (splits 2, 7, 10, 15; section 3, R) |

## Settled in the merge (beyond the splits)
- **Union applied:** A (`NOTE` L76; the two open hits of item 1a; the overlapping unit times; the Phase 8 axis; the `16` coordinates; the datasheet's scope; MP-11; the "all of it" row; warm and cold forms; cross-pending pieces; `DR-55`'s deferred research; the missing Nulls; the records notes; R-15 and R-16 as record disagreements); B (the unmeasured reach of the wind consequences; the T5 marker as a Step 10 miss; the register's section 3 lag; the index's L159 and L160; the Phase 6 and Phase 7 status lines; the datasheet's own condition; the section 1 status table; the git request; "a readiness check inside an open layer"; old and new tools not like-for-like; the "cannot prove" additions on premises, commits and instruments); C (L9 omits 1b and 1c; which file is the handoff; item 2's same-day rename; no Step 10 register row; the Element accepted; the layer's own recorded-not-implemented lessons; Q-149's phrase; the status half; the completion note before its queue; the closing test and the stage order; a parked fire's evidence decays; the "cannot prove" additions on the layer, the instruments, the shared file and the index; the full docket list in the "ready" list).
- **The merge writer checked one fact itself:** to state split 16's facts it re-read the runbook's Step 10 span (`RB` L3057 to L3145), on the readers' own admitted span: item 1 opens at L3075; item 1a, with "everything in `Disciplines/`", at L3086 to L3087; "This has now failed three times" at L3090. That did not settle which line the old L3074 named.
- **Figures:** Step 10 states none (all three); the piece gives the live set in its header only and no as-written figure anywhere.
- **The coinage** for the curating organization does not occur in the piece (keepcheck below: 0).
- **The next subject** is never named in the piece or in this record outside the raw tool output pasted below, which names files only (split 17); the subnet's two other un-run cities are never named.
- **The ST9 piece** (unit U10) was not in the folder at the start or at the end of this merge (checked by listing twice): its cross-reference is *pending*.

## Kept files (`M-132`)
The Round 1 outputs `.t8_amend_ST10_readerA.md`, `.t8_amend_ST10_readerB.md`, `.t8_amend_ST10_readerC.md` are kept in this folder as the round's working record, unedited, beside `.t8_amend_ST10_round2_raw_FIRSTRUN.txt` (the first Round 2 run), `.t8_amend_ST10_round2_raw.txt` (the re-run), the frozen brief `.t8_amend_ST10_brief.md` and the checkpoint `.t8_amend_ST10_CHECKPOINT.md`. The Round 3 replies are kept as `.t8_amend_ST10_round3_readerA.md`, `.t8_amend_ST10_round3_readerB.md`, `.t8_amend_ST10_round3_readerC.md`. The Round 1 and Round 3 files and the brief are byte-identical to their scratchpad copies in `amend_ST10/` (`cmp`); the two Round 2 outputs have no scratchpad copy. None of these files is an input to any later step; this record and the piece are the merged result. No helper file was created in the repo by the readers or by this merge (the merge's drafts, scripts and outputs stayed in the session scratchpad, `amend_ST10_merge/`).

## Quotation audit (`Tools/quotation_audit.py`, `--files Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md --own-pass`) · 2026-11-04 about 12:28, run while this record was not in the folder
raw output, excerpted (1 line omitted: the positive control "HARD - case mismatch", whose test phrase names another location; it reported FOUND, and the instrument line below reads VALID; the whole output is in the session scratchpad at `amend_ST10_merge/qaudit_final2.txt`):
```
pass audited : Mirny
corpus mode  : default (own pass excluded)
corpus files : 6089   chars: 69,792,255
files audited: Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md
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
NOT FOUND in corpus: 25
  of those, in TABLE CELLS : 6
  of those, in PROSE       : 19

  [Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md:18]           ): no cold run is scheduled on any admitted line. their evidence has decayed while parked (pa-98 has come true), so any fire that 
  [Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md:24]           has to mean: the lived middle and the held planet), dec-121 (when step 10 is re-run, and what
  [Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md:38]  [CELL]  h s the acceptance and the parking stand ( drl l1225)
  [Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md:38]  [CELL]  is stale for q-145 (answered, drl l1154)
  [Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md:38]  [CELL]  is stale for its first half (the wind re-derivation now exists as amendment pieces, most proposed)
  [Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md:43]  [CELL]  k s parked; the six coordinates it cites hold other lines today; its
  [Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md:47]  [CELL]  s r rb l3122 to l3123 names mirny as provenance since 2026-10-21; the
  [Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md:58]  [CELL]  k s the header is now mem l3 to l4, not
  [Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md:144]           means a check whose input is file-system state or live canon, so it can run before the developer answers
  [Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md:146]           means the developer's acceptance plus the dockets' marks, never a rewrite of a pass file; (d) the open decisions: 21 mirny entries
  [Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md:185]           held on 2026-10-13. since 2026-10-21 the required reading names this pass's subject: rb l3122 dates item 7's amendment
  [Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md:205]           ( queue l36 to l45); the completion note's
  [Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md:210]           with a passed self-test ( u00 l203, l204) mp-2 asked for the founders check scoped to one city ( 09 l73); it now runs
  [Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md:214]           ( rc l36, l37) and has no section on what the repass cannot prove (read whole by all three); nor has the queue. the data recheck c
  [Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md:230]           is defined nowhere: item 10's row (l31) has no cold or warm half, and drl l1225 says only
  [Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md:235]           and before handing off ( rb l3059, l3060); step 10 declared not-complete in passing (l5, l59) but never listed what
  [Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md:247]           ) against overlapping start times (u5 began at 09:05 while u4 ran to 09:15; u7, u8 and u9 all began at 09:55; queue l40 to l45). t
  [Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md:358]           and before handing off ( rb l3059, l3060); by the step 10 datasheet's own condition the verdict
  [Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md:366]           ( as7 l25), and the runbook says a pass that fails it
  [Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md:448]           ) a ruling placing the lived middle in the ulm or the cst: absent (dec-120) a definition of
  [Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md:448]           looked (l5, l31; drl l1225); absent a cold run scheduled for any subject: absent on the admitted lines (a result) an index line fo
  [Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md:460]           rb l355) may not be fully answerable inside the ulm. would decide: what
  [Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md:470]           for items 6 and 11 (the queue's 2026-11-03 handoff note, the completion note, or a memory handoff), check its paths, and give it a
  [Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md:479]           has to mean for mirny's ulm pass. two parts, both yours only. (a) the everyday life of mirny's people, robots and humans (the
  [Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md:516]           a ruling on mp-1 to mp-19; a cold run scheduled for any subject; a

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```

**Triage by hand (each of the 25 misses read and classified):** 66 fragments tested, **25 not found** (6 in table cells, 19 in prose). **All 25 are connective prose** captured between two adjacent quotations on one line (the audit's own warning): the merged item list's "why" cells (L38, L43, L47, L58), section 0's points 3 and 9 (L18, L24), section 2's opening and its item notes (L144, L146, L185, L205, L210, L214), the R list of section 3 (L230, L235, L247), the "ready" list (L358, L366), the nulls (L448), the reserved findings (L460), the requests (L470), DEC-120 (L479) and the dead-ends snag (L516). **None of them is a quotation; no misquotation was found by the audit.** **How the run was kept valid:** the audit was first run at about 12:21 and 12:25, before this record existed. This record was then written (about 12:26); a check of the Round 2 slip at its source (`REG` L16 to L18) showed that reader B's field was the line **after** L17, not before it, so the piece's header and its snag 9 were corrected; to keep the audit valid, this record was moved out of the folder into the scratchpad, the audit re-run at about 12:28 on the corrected piece (its output identical to the 12:25 run, by `diff`), the merge checks and the supplementary check re-run (identical), and the record moved back. Before the final runs, the merge corrected what an earlier run of the same audit and its own supplementary check showed: a runbook sentence that runs across two physical lines (`RB` L3059 to L3060) was cut to the part on one line ("Run it before declaring a pass complete"); a cited sentence was moved from the runbook (which wraps it across L3136 and L3137) to Step 10's L31, where it sits on one line; and five phrases of the merge's own or of a reader's wording that stood in quotation marks were set in italics or unquoted (the handoff note's description, "the cold half of item 10" restored to the notice's own "the cold half of 10", the brief's result restored to its L8 wording, a decision count, a label for the git check). **A supplementary check** of every double-quoted string in the piece (a scratch script, `amend_ST10_merge/shortq.py`, normalizing dashes, quotes, markup, case and spaces, and requiring each string to sit inside **one physical line** of a source) tested 197 strings against the Mirny folder's files and dot-files, the Step 10 datasheet, the runbook, `06`, the rulings log, the quick reference, the index and the decisions file:
```
L144: ** means a check whose input is file-system state or live canon, so it can run before the developer answers; **
quoted strings tested: 197; not found on one physical line: 1
```
The one miss is connective text between the two quoted words of section 2's opening ("Now" and "after application"), not a quotation. The strings found only in the reader dot-files are the readers' own words quoted as theirs (the claims-not-accepted wording, such as "none content", "FIRES (small)", "eight pieces", "four handoff memories", "25 OPEN") or source lines the supplementary corpus does not hold (`REG` L17's opening, `RB` L3141's heading); each of the latter was checked at its source by this merge.

## Merge checks
raw output (full; scripts in the session scratchpad `amend_ST10_merge/`, run with `python3 -I` on a copy of the piece; the location-name scan's positive control on a scratch text with four planted names found all four, names not reproduced here; `mixcheck.py` counts "fourteen stocks", not "fourteen", because "fourteen checks" is Step 10's own item count):
```
$ python3 -I mixcheck.py <piece>
line-level mixes: 0

$ python3 -I citycheck.py <piece>
== piece_for_checks.md: names scanned 139; hits 0

$ python3 -I idcheck.py <piece>
AS10 cited  : 1..23 (23 distinct)
AS10 headed : 1..23 (23 distinct)
AS10 in mapping table (bold): 1..23 (23 distinct)
cited but not headed: [] | cited but not in mapping: []
RF-ST10: cited 1..11 (11 distinct); defined 1..11 (11 distinct); cited not defined: []
AR(>=180): cited 180..191 (12 distinct); defined 180..191 (12 distinct); cited not defined: []
AQ(>=170): cited 170..180 (11 distinct); defined 170..180 (11 distinct); cited not defined: []
DK10: cited 1..12 (12 distinct); defined 1..12 (12 distinct); cited not defined: []
DEC(>=120): cited 120..122 (3 distinct); defined 120..122 (3 distinct); cited not defined: []
other AR cited (<180): []
other AQ cited (<170): [27, 36]
splits cited: [2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 24, 25, 26, 32, 33, 34, 35]
snags cited: [6, 16, 20]

$ python3 -I keepcheck.py <piece>
piece_for_checks.md: occurrences of keeper/keepers: 0
```
**Reading the checks:** no line or block mixes an as-written and a live figure (the piece states no as-written figure); no other location's name occurs; every AS10, RF-ST10, AR, AQ, DK10 and DEC number cited is defined, and every AS10 number is in the mapping table; the two lower AQ numbers (AQ-27, AQ-36) are the Phase 8 piece's, cited as its own; the split numbers cited are all in this record's split table; the snag numbers cited are the piece's snag 20, Step 10's snag 6 and reader B's snag 16; the coinage occurs nowhere.

## American English sweep
raw output (full; script `amend_ST10_merge/ae_sweep.py` in the session scratchpad, run with `python3 -I` on both files; its positive control on a scratch text with fifteen planted British spellings and one 'judgement' found all sixteen; the kept-spelling count in this record comes only from this paragraph and the output lines below):
```
== Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md (524 lines)
British-spelling hits: 0
'judgement' (kept spelling): 0
== Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04b_T8_Rounds.md (649 lines)
British-spelling hits: 0
'judgement' (kept spelling): 3
```
