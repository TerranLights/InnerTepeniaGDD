# Mirny · Amendment re-derivation · Piece ST10b (the Step 10 readiness re-run) · T8 round record · 2026-11-08

**Companion to** `Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md`. Raw tool output is pasted, not summarized; where a block is not the whole output it is headed as excerpted, with the count of lines omitted and why. Working files are in this folder as `.t8_amend_ST10b_*` and `.t8_required_amend_ST10b.txt`; this merge's scratch work is in the session scratchpad (`st10b_merge/`). No other location is named in this record. **Nothing here declares Mirny complete or calls it ready.**

## Setup
- **The run and its hours.** On 2026-11-08 the developer had the corrections applied in three batches, then ordered the Step 7 QA re-run, the fresh Review Panel and the Step 10 re-run, each written to file before the next starts (`DRL` L1877 items 1 and 4). When the orchestrator said those three would start the next morning, the developer answered "do those three items now" (`DRL` L1876), which "overrides the derivation-hours rule (05:00-14:59) for this run only" (`DRL` L1877 item 5). **This round therefore ran in the evening, under that override, by the developer's word, not by this merge's judgement of the clock:** the orchestrator's facts file was written at 17:26, the list and the brief were frozen at 17:27 and the readers dispatched then (checkpoint, second line); the readers' outputs are time-stamped 17:43 (A), 17:46 (C) and 17:47 (B, after its repair) in the scratchpad; Round 2 and Round 3 were done by 17:52 (checkpoint, fourth line); the Round 3 replies are time-stamped 17:51; the merge brief 17:48; this merge ran after it, placed the piece at about 18:14, and ran the audit at about 18:14 and 18:16. No reader's output depends on the clock (brief, result (8)).
- **Reading list (trimmed, `DR-74`):** `.t8_required_amend_ST10b.txt` (byte-identical to the scratchpad copy `amend_ST10b/t8_required_amend_ST10b.txt` by `cmp`), **17 entries, 2,192 admitted lines** (this merge's count script: whole files by their physical lines, spans by their ranges, the rulings span L1871 to L1880 counted to the file's end at L1879). Entry 1 the runbook's Step 10 span (L3080 to L3125, 46 lines); entry 2 the rulings log at 27 spans (915 lines); entries 3 to 8 read whole: Step 10 (99), the 2026-11-04 Step 10 piece (524), the orchestrator's facts file (116), the queue (71), the completion note (52) and the answers note (49); entries 9 to 17 at their heads: `ST12`, `ST13`, `ST14`, `ST16` (L1 to L30 each), `ST7b` (L1 to L65), `ST8b` (L1 to L45) and the three batch files (L1 to L30 each).
- **Brief:** `.t8_amend_ST10b_brief.md`, identical for A, B and C with `{X}` the reader letter, **sha256[:16] 5e2694db16b49a7d** (computed by this merge on the folder copy; the scratchpad copy is byte-identical by `cmp`), as the merge brief states. It carries eight orchestrator-verified results with their sources, the developer's binding words, the stage order, ten traps and six standing lines.
- **The orchestrator's facts file** (entry 5; `amend_ST10b/orchestrator_facts.md`, 116 lines): A the repository state; B the item 1c name scan over the 24 untracked new prose files, line numbers only, and the eleven pointer lines; C the handoff path check; D the decisions file's not-fully-answered Mirny headings. **Two corrections to it, recorded as the orchestrator gave them to this merge (ORCH) and as all three readers found them:** (1) section D's "count: 22" includes the file's format heading, so the real count is 21 (DEC-041 part (b), DEC-042, DEC-080 and DEC-081 deferred or open; DEC-220 to DEC-230; DEC-240 to DEC-245); (2) the one 1c hit (the Phases 4 and 5 piece's T8 record, L183) is a pasted tool path to a shared structure document inside Round 2 raw output, classified by the orchestrator as SHAPE; this merge's masked look agrees (piece AS10b-4). **One list defect, the orchestrator's own:** the rulings span `DRL` L1871 to L1880 runs one line past the file's end (L1879); it cost the readers nothing (each counted 915 admitted lines and took LLAST at L1879).
- **Readers:** three Opus agents, A `a31503936f09ca31c`, B `a68b0259632432070`, C `a7f1a4880e0cf8fe6` (checkpoint, second line). **None refused any entry; each opened all 17 at the stated range** (reading logs: A L5 to L25, B L5 to L24, C L5 to L24). Graphify: not used by any reader.

| Reader | Output lines | Bytes | PROOF blocks | Findings (Round 1 numbering) | Docket | Requests · questions · RFs |
|---|--:|--:|--:|---|---|---|
| A | 606 | 75,733 | 17 | AS10b-1 to AS10b-20 | DK10b-1 to DK10b-12 | AR-320 to AR-329 · AQ-320 to AQ-326 · RF-ST10b-1 to RF-ST10b-6 |
| B | 646 (first run 644) | 81,415 (first run 81,321) | 17 | AS10b-1 to AS10b-19 | DK10b-1 to DK10b-9, plus unnumbered status notes | AR-320 to AR-327 · AQ-320 to AQ-326 · RF-ST10b-1 to RF-ST10b-6 |
| C | 700 | 100,204 | 17 | AS10b-1 to AS10b-20 | DK10b-1 to DK10b-10 | AR-320 to AR-329 · AQ-320 to AQ-327 · RF-ST10b-1 to RF-ST10b-6 |

Line and byte counts by `wc` on the folder copies, each byte-identical to its scratchpad copy (`cmp`); PROOF blocks counted by `grep -c '^### PROOF:'`. No reader proposed a DEC number. **The merge brief gives B's output as 644 lines:** that is B's first-run file; the final file has two more lines (a blank line and B's repair log, the diff below).
- **Self-checks before handback (as each reader records):** A used `wc -l`, `awk`, `tail -c` with `od -c` and `sed -n` through `cat -A` on listed files, and one shell sum of its span lengths (A L25). B used `wc -l`, a byte check of the rulings log's end, `sed -n` byte counts and one `python3 -I` count of the admitted set, and disclosed one `wc -l` and one `awk` length comparison on its own output (B L24; B snag 19). C used `wc -l`, `sed -n` with `cat -A` and `tail -c` with `od -c` on listed files, and disclosed one `grep -n` and one `grep -qxF` check on its own output, a name and spelling check on its own output, and an earlier form of one check that a hook blocked before it ran (C L24; C snag 14). Every PROOF field was copied by hand (standing line 1); C compared its fields read-only with `sed -n` after typing them. No reader searched a source file or created a helper file in the repo.
- **Ruling-log freeze (`M-302`):** the rulings log was last modified at 14:41:58 on 2026-11-08 (this merge's `ls`), before the list was frozen at 17:27, so its admitted text did not change during the round.

## Round 1 headline claims (union, before Round 3)
| Claim | A | B | C |
|---|---|---|---|
| Item 1 | STANDS, parked; not re-run | stands, parked; evidence stale | STANDS, parked |
| Item 1a: the trigger "after any rule edit made on R-183" has fired; the runbook +23 | found | found | found |
| Item 1b | STANDS | stands (N/A warm) | STANDS WITH A NOTE; the 24 new file names carry no claim |
| Item 1c label | NOT PASS (incomplete) | FIRES (unresolved) | NOT CLEAN YET |
| The 1c hit | unclassified (file not on the list) | unclassified | unclassified; a withdrawal plausible, not shown |
| 1c coverage gaps | listed (a) to (i) | listed, with the 70 and 59 arithmetic | listed, with no positive control shown and `lines=` one above `wc -l` |
| The commits since 2026-11-04 | "not given" | no `git log` on the list | HEAD moved from `8777bb5f` to `9a9d3fc7` |
| Item 2 | CHANGES; owed, not run | not run; owed | OPEN; not re-run |
| Items 3, 4, 5, 7, 8 | stand | stand | stand |
| Item 6 | FIRES (3 of 32) | FIRES on the October handoff; not run on the current one; two misses probably scope artifacts | FIRES in part; full raw block |
| Item 9 | FIRES (eleven items) | FIRES (a 13-row table) | FIRES on the status half; existence and listing PASS |
| The decisions count | 21 (the template) | 21 | 21, "18 OPEN" |
| Item 10 | FIRES, narrowed | FIRES, narrowed | FIRES, re-grounded; "five units in a row" |
| Item 11 | FIRES, with proposed text | FIRES, with proposed text | FIRES (not yet), with proposed text |
| `ST10`'s coordinates drifted | the runbook only | snags 6, 7, 12 | a finding: the runbook, the queue, the completion note |
| The order: an interim run | found | found | found |
| The ten conditions | 2 MET · 6 PARTLY (1 to 6) · 2 NOT MET (8, 10) | 2 MET · 6 PARTLY (2 to 6, 10) · 2 NOT MET (1, 8) | 2 MET · 6 PARTLY (1 to 6) · 2 NOT MET (8, 10) |
| The register (`ST10` L362) | NOT MET, an extra row | NOT MET, an extra row | folded into condition 3, no status |
| The status line | the point of declaring "has not been reached" | "not yet ready to be declared complete" | "Not ready to be declared complete" |
| Numbering | AS10b-1 to AS10b-20 | AS10b-1 to AS10b-19 | AS10b-1 to AS10b-20 |

## READ-COVERAGE (which reader read which entry in full)
**Every reader read every one of the 17 entries at its stated range, one Read per span** (A L7 to L24; B L6 to L23; C L6 to L23). The long whole files were read in consecutive chunks: the 2026-11-04 piece in four (A L11; B L10; C L10); the rulings log one Read per span (27 each). Phantom last lines in the Read display were set aside by `wc -l` (A snag 3; B L9, L12 to L14; C snag 3). **There is no gap to close:** every admitted line was read by all three. Lines outside the list were opened by no reader.

## Round 2 (`Tools/triple_read_verify.py`) · first run NOT unanimous (reader B, three LLAST fields) · re-run UNANIMOUS
**What happened (checkpoint, third and fourth lines).** The tool was run on A's, B's and C's outputs against the frozen 17-entry list: **48 of 51 agent-entry results matched; verdict NOT UNANIMOUS - DO NOT WRITE.** Reader B (agent2) gave a wrong LLAST on the three entries whose range ends on a blank line at L30: the Steps −1 to 3 piece, the Phase 3 piece and Application Batch 1, each `:: 1-30`. For the first two B gave `---` (their L29) and for the third the text of its L29; the true L30 of each is blank. The first-run output and B's first-run file were kept (`.t8_amend_ST10b_round2_raw_FIRSTRUN.txt`, `.t8_amend_ST10b_readerB_FIRSTRUN.md`). The orchestrator asked B to repair the failed fields under `DR-117` item 2 and gave no values; **B re-read the three lines and repaired the three fields by hand**, logging them on its file's last line. The re-run: **51 of 51, UNANIMOUS - CLEARED TO WRITE.** A and C passed both runs unchanged. A blank last line is the case the brief's section G and standing line 1 warn of (the field is written empty when the line is blank); the same failure shape appears in the panel's Round 2 ("blank last lines", `ST8b` L27).

### Round 2: first run, raw output (full; file `.t8_amend_ST10b_round2_raw_FIRSTRUN.txt`)
```
required files: 17
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 3080-3125] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 20-147,170-254,384-419,422-554,575-587,609-665,678-690,725-757,953-1031,1075-1088,1092-1107,1111-1133,1135-1160,1211-1226,1404-1412,1427-1434,1438-1445,1460-1468,1472-1479,1523-1530,1550-1557,1570-1577,1655-1662,1664-1671,1707-1715,1728-1870,1871-1880] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/10_Readiness_Check.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/883d8609-cb3a-4820-b3cb-6bfce797ee04/scratchpad/amend_ST10b/orchestrator_facts.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Notes_2026-11-04_Answers_Carried_Forward.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md  [range 1-30] ===
  agent1   ✅ all fields match ground truth
  agent2   ⛔ LLAST MISMATCH  claimed='---'  actual=''
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST13_Phase3_2026-11-05.md  [range 1-30] ===
  agent1   ✅ all fields match ground truth
  agent2   ⛔ LLAST MISMATCH  claimed='---'  actual=''
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md  [range 1-30] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST16_Symbols_2026-11-05.md  [range 1-30] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md  [range 1-65] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST8b_FreshPanel_2026-11-08.md  [range 1-45] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Application_Batch_1_Pointers_2026-11-08.md  [range 1-30] ===
  agent1   ✅ all fields match ground truth
  agent2   ⛔ LLAST MISMATCH  claimed='Markdown would read the pointer as a table row, a list conti'  actual=''
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Application_Batch_2_Datasheets_2026-11-08.md  [range 1-30] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Application_Batch_3_CultureFile_and_Spec_2026-11-08.md  [range 1-30] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
⛔ NOT UNANIMOUS - DO NOT WRITE. Log which agent/file failed and why.
```

### What reader B changed (raw output, whole: `diff .t8_amend_ST10b_readerB_FIRSTRUN.md .t8_amend_ST10b_readerB.md`)
```
$ diff .t8_amend_ST10b_readerB_FIRSTRUN.md .t8_amend_ST10b_readerB.md
579c579
< LLAST: ---
---
> LLAST:
587c587
< LLAST: ---
---
> LLAST:
627c627
< LLAST: Markdown would read the pointer as a table row, a list continuation or the same paragraph.
---
> LLAST:
644a645,646
> 
> ROUND 2 FIELD CORRECTIONS: Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md:LLAST; Amendment_Rederivation_ST13_Phase3_2026-11-05.md:LLAST; Application_Batch_1_Pointers_2026-11-08.md:LLAST
```

### Round 2: second run, raw output (full; file `.t8_amend_ST10b_round2_raw.txt`)
```
required files: 17
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 3080-3125] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 20-147,170-254,384-419,422-554,575-587,609-665,678-690,725-757,953-1031,1075-1088,1092-1107,1111-1133,1135-1160,1211-1226,1404-1412,1427-1434,1438-1445,1460-1468,1472-1479,1523-1530,1550-1557,1570-1577,1655-1662,1664-1671,1707-1715,1728-1870,1871-1880] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/10_Readiness_Check.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST10_ReadinessCheck_2026-11-04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/883d8609-cb3a-4820-b3cb-6bfce797ee04/scratchpad/amend_ST10b/orchestrator_facts.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Notes_2026-11-04_Answers_Carried_Forward.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md  [range 1-30] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST13_Phase3_2026-11-05.md  [range 1-30] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md  [range 1-30] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST16_Symbols_2026-11-05.md  [range 1-30] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md  [range 1-65] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST8b_FreshPanel_2026-11-08.md  [range 1-45] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Application_Batch_1_Pointers_2026-11-08.md  [range 1-30] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Application_Batch_2_Datasheets_2026-11-08.md  [range 1-30] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Application_Batch_3_CultureFile_and_Spec_2026-11-08.md  [range 1-30] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

## Round 3 (SendMessage to readers A, B and C) · 2026-11-08, replies 17:51 (scratchpad file times) · cross-check done
Each reader read the other two readers' sections from "Step 10 as it stood" to the snags, skipped their PROOF blocks, re-opened lines on its own list to settle disagreements, and wrote four parts: the shared points K1 to K6, each AGREE or OBJECT with the settling line; a mapping of the colliding AS10b numbers, with keep, drop or fold; the docket, requests and questions unified; and its concessions and final position. Replies: `.t8_amend_ST10b_round3_reader{A,B,C}.md` (177, 225 and 202 lines; byte-identical to the scratchpad copies by `cmp`). The orchestrator also gave all three its classification of the one 1c hit (ORCH); each recorded it as the orchestrator's account, since no admitted line carries it.

| Reader | Objections (its Part 1 and Part 2) | Lines re-opened (as each reply lists them) | Concessions | Holds |
|---|---|---|---|---|
| A | to B: condition 1 NOT MET and condition 10 PARTLY MET; to C: condition 10's remainder written as "the status half" only, and C's recommendation on the deferred decisions | `ST10` L20, L369; `DRL` L112, L117, L493, L1029, L1733, L1788; `QUEUE` L59, L63, L68; `RC` L3, L37; `ST8b` L26 | nine: the HEAD move (to C); `ST10`'s drift into the queue and the completion note (to B, C); the line counts (to C); `QUEUE` L63 a note (to C, in part); B's missed status surfaces; the line-reference sweep and the core's wording (to B, C); the symbols label (to C); item 9's passing half (to C); item 6's scope (to B) | its §3 routing finding may drop; the conditions as it held them |
| B | to A and C: the pointer lines for Phases 2, 6 to 9 and Steps 6 to 10 listed as unapplied dockets; to A: snag 9 is not a discrepancy | `ST10` L20; `DRL` L1153; `QUEUE` L60 (and its Round 1 readings of `DRL` L1760, L1814, L1868, `ST10` L242, L359, `QUEUE` L15) | nine: the 1c word; condition 1; condition 10; the HEAD move; `lines=` one above `wc -l`; `QUEUE` L63 a note; item 9's two halves; the new name not a condition; its status line's count of five checks that fire | A's routing finding kept; its own reading of the pointer rulings |
| C | to B: the 1c label, condition 10, and B's enumeration of `S10` lines naming another location (wrong both ways) | `S10` L22, L23, L36, L54, L71, L82, L89, L92; `DRL` L493, L1029; `QUEUE` L15; `ST7b` L24, L25 | six: the register NOT MET; the decisions breakdown; the Gate F flag; the line-reference sweep, B's extra status surfaces and the scope-artifact point; the 1c hit as ORCH's shape; condition 1, where it does not contest NOT MET as the conservative fallback | condition 1 PARTLY MET; its drift finding; its git question |

### The shared points (K1 to K6)
| K | Topic | A | B | C |
|---|---|---|---|---|
| K1 | the per-check results | AGREE in substance on all fourteen; labels differ on four | AGREE on 13 of 14; concedes the 1c word | AGREE on 13 of 14; OBJECT to B's 1c label |
| K2 | the ten conditions | AGREE on 7 of 10; OBJECT to B on 1 and 10 | concedes 1 and 10: tally 2 · 6 · 2 | AGREE on 8 of 10; OBJECT to B on 10; does not contest B on 1; concedes the register |
| K3 | the mechanical facts | AGREE: 21; 29 of 32; ORCH's shape recorded as ORCH; 11 of 11; the span past the end; `lines=` + 1 | AGREE, the same; the decision breakdown 17 · 1 · 3 | AGREE, the same; concedes "18 OPEN" |
| K4 | what "ready" lacks; the status line | AGREE no reader says ready or complete; proposes a line | AGREE; proposes a line with "Not ready to be declared complete" | AGREE; proposes a line with "not ready to be declared complete"; OBJECT to B's count of five checks that fire |
| K5 | item 2 owed; checks needing files on no list | AGREE | AGREE | AGREE |
| K6 | lines naming another location | AGREE none used | AGREE; accepts C's additions | AGREE; OBJECT narrowly to B's enumeration; adds `QUEUE` L15 |

### The splits, and how they were settled
*Rule (`M-246`): the position two or three readers hold after Round 3's concessions; where they still differ, the most conservative reading (the one that changes less, claims less or keeps a record), the split named in the piece.*

| # | Point | Positions after Round 3 | Settlement (where in the piece) |
|--:|---|---|---|
| 1 | **Item 1c's label** | A: NOT PASS (incomplete), not a found leak; C: NOT PASS (incomplete); B conceded its "FIRES (unresolved)" | **NOT PASS (incomplete); no content-class hit found** (AS10b-4). The merge brief's known results list 1c among the checks that fire; the label and the grouping agree that it does not pass, and the piece says both |
| 2 | **Condition 1, the decisions** | A, C: PARTLY MET; B conceded its NOT MET; C would not have contested NOT MET as a fallback had B held it | **PARTLY MET** (AS10b-19), checked at `ST10` L359, `FACTS` D L94 to L114 and `DRL` L1867 by this merge |
| 3 | **Condition 10, Step 10 whole and last** | A, C: NOT MET; B conceded its PARTLY MET | **NOT MET** (AS10b-19) |
| 4 | **The register** | A, B: NOT MET, an extra row; C conceded | **NOT MET, an extra row** (AS10b-19) |
| 5 | **The decisions breakdown** | A, B: 17 OPEN, 1 part-open, 3 DEFERRED; C conceded its "18 OPEN" | **17 · 1 · 3** (AS10b-12) |
| 6 | **The pointer lines for Phases 2, 6 to 9 and Steps 6 to 10 under condition 3** | A, C listed them as unapplied dockets; B objects that no ruling asks for them (`DRL` L1868 item 2; L1814 item 2; L1153); A and C did not answer it (one pass) | **Still differ: the conservative reading (claims less).** Only the Steps 9 and 9.5 pointers are owed by ruling; the others are a proposal awaiting the Step 7 re-run's decision 5 (DK7b-10). This merge confirmed both rulings at their lines (AS10b-19, condition 3) |
| 7 | **A's routing finding (what fires and who decides)** | A: drop (its content is in the feeds); B: keep, confirmed; C: fold | **kept (two of three), in C's form, folded into AS10b-15** |
| 8 | **B's finding on what the 2026-11-04 answers changed in AS10-21** | A: fold into section 5's preamble; B: fold into "What changed"; C: keep as a finding | **folded (two of three) into section 4's preamble** |
| 9 | **The commits as their own finding** | A: keep C's as its own; B: the repository as its own merged item; C: fold into the coverage finding | **its own finding (two of three), AS10b-6**, with this merge's `git log` |
| 10 | **The status line's wording** | A: the point of declaring "has not been reached"; B, C: "not ready to be declared complete" | **B's and C's clause (two of three) followed by A's, which gives the reason** (AS10b-20; piece snag 21). A first draft of this merge carried A's form alone; it was changed before this record existed and the audit was re-run (below) |
| 11 | **The unified requests and questions** | the three Round 3 lists number them differently (A, B AR-320 to AR-333; C AR-320 to AR-332) | **this merge's AR-320 to AR-333 and AQ-320 to AQ-330**, mapped in piece §5; C's dropped AR (the totals) kept, two of three |
| 12 | **Numbering** | three colliding sets (A 20, B 19, C 20) | **20 merged findings in check order** (piece §5) |

### Single finds, checked
| Find | Finder | Checked by | In the merge |
|---|---|---|---|
| HEAD moved from `8777bb5f` to `9a9d3fc7` | C | A, B (Round 3); this merge's `git log` | AS10b-6 |
| `ST10`'s coordinates drifted into the queue and the completion note | C | A, B (Round 3); this merge at `QUEUE` L34, L54, L55, L59 and `RC` L3, L41, L42 | AS10b-16 |
| `FACTS` B's `lines=` one above `wc -l` | C | B (nine files), A (Round 3) | AS10b-11 row 16 |
| Item 9's two halves | C | A, B (Round 3) | AS10b-11 |
| No positive control shown for the 1c scan | C | B (its unified AR-321) | AS10b-5 |
| The one-word labels provisional corpus-wide (`DRL` L112, L117) | C | A (Round 3); this merge at the lines | condition 9; AQ-322 |
| `DR-55`'s deferred research questions under condition 8 | C | this merge at `ST10` L367 | condition 8 |
| A template line counted (C's reserved finding) | C | B (its unified list) | RF-ST10b-8 |
| Item 6 on a handoff no one now uses | C | B (its unified list) | RF-ST10b-9 |
| The two misses as probable scope artifacts (`DRL` L493, L1029) | B | A, C (Round 3); this merge at the lines | AS10b-9 |
| `QUEUE` L59, `QUEUE` L69, `ST7b` L3, `ST12` L3 overtaken | B | A (concession 5), C (its union) | AS10b-11 rows 2, 3, 8, 10 |
| `ST7b` L19's `AB1` coordinate off by two | B | C (its union); this merge at `AB1` L3, L5 | AS10b-11 row 9 |
| The 70 and 59 arithmetic | B | C (with its caveat) | AS10b-5 |
| The line-reference sweep under condition 4; the core's wording under condition 2 | B | A, C (Round 3) | conditions 2 and 4 |
| The re-run triggers of 1a and item 2 as one mark (B's DK10b-9) | B | A, C (their unified dockets) | DK10b-4 |
| DEFERRED is not ANSWERED (B's reserved finding) | B | A and C ask the same question (AQ-321) | RF-ST10b-5 |
| `ST10` L3 still "Awaiting the developer." | A | C (its union); this merge at `ST10` L3 | AS10b-11 row 11; DK10b-11 |
| The Gate F flag on eight pointer lines (`ST7b` L24) | A | C (Round 3) | condition 3 |
| The batch files' APPLIED lines current (a pass) | A | C (its union) | AS10b-11 row 9 |
| What fires and who decides | A | B (Round 3) | AS10b-15 (fold) |
| The closing test and the deferral | A | B (its unified list) | RF-ST10b-7 |
| Item 1a's evidence scan; the commit after AR-320 to AR-322 | A | B, C (their unified requests) | AR-324; AR-332 |

### Claims not accepted (left out of the merge; each listed with what was done)
| Claim | Whose | Objected to by | Why (the evidence line) | In the merge |
|---|---|---|---|---|
| condition 1 NOT MET | B | A, C | `ST10` L359's set is answered except four (`FACTS` D L94 to L97); `DRL` L1867 | conceded by B; PARTLY MET |
| condition 10 PARTLY MET | B | A, C | "Step 10 itself re-run whole, last," (`ST10` L369); B's own cell says it is not last | conceded by B; NOT MET |
| item 1c "FIRES (unresolved)" | B | A, C | no content-class hit was found; the one hit is shape (ORCH; this merge's masked look) | conceded by B; NOT PASS (incomplete) |
| condition 10's remainder written as a re-run of the status half (items 9, 10 and 11) only | C | A | the condition is "whole, last" (`ST10` L369) | carried as an option the developer may take (AQ-320; decision 1, option B) |
| the deferred decisions count as answered if listed as deferred | C | A | a reader decides nothing for the developer (brief, trap 1) | the recommendation carries both halves: not answered until he says; if kept deferred, listed as deferred by ruling (AQ-321) |
| the pointer lines for Phases 2, 6 to 9 and Steps 6 to 10 as unapplied dockets | A, C | B | `DRL` L1868 item 2 approves ten files; `DRL` L1814 item 2 the Steps 9 and 9.5 files; `DRL` L1153 the head notices | not counted as owed; a proposal awaiting the Step 7 re-run's decision 5 (split 6) |
| `QUEUE` L71's line counts as a discrepancy (A snag 9) | A | B, C | `FACTS` B's `lines=` is `wc -l` + 1 | conceded by A; not a discrepancy (AS10b-11 row 16) |
| B's list of `S10` lines naming another location | B | C | five listed lines name no location (L22, L36, L54, L71, L82); three that do are missing (L23, L89, L92) | corrected in piece snag 15; no such line was used by any reader either way |
| the register folded into condition 3 with no status | C | A, B; C withdrew | `ST7b` L25 | NOT MET, an extra row |
| "18 OPEN" | C | A, B | DEC-041 is part-open, not wholly open | 17 · 1 · 3 |
| the question whether the count is 21 (A AQ-326) | A | C (drop) | the three-way agreement in K3 | answered (AS10b-12); not carried |
| `QUEUE` L63 "stale within the same file" | B | C | a dated progress row; L68 records the later state | a note (AS10b-11 row 1) |
| A's reserved finding on provisional symbols | A | A withdrew it into its question | — | one copy kept, B's (RF-ST10b-6) |

## Settled in the merge (beyond the splits)
- **Union applied:** A (the subject and exposure note; the coverage list (a) to (i); the runbook's +23; the routing list; the re-sort of Step 10's and `ST10`'s IDs; the Gate F flag; the batch files current; `ST10` L3; the closing-test reserved finding); B (the scope-artifact ground; the extra status surfaces; the 70 and 59 arithmetic; the line-reference sweep; the core's wording pending; the DK10 docket's own staleness; the 1a and item 2 triggers mark; DEFERRED is not ANSWERED); C (the HEAD move; the drift of `ST10`'s coordinates; the `lines=` convention; the two halves of item 9; the missing positive control; the corpus-wide provisional labels; `DR-55`'s deferred questions; the full raw blocks; the template and handoff reserved findings).
- **One copy per raw block:** the piece pastes `FACTS` A, B, C and D whole (C had pasted B, C and D whole; A and B excerpted them), and this merge's two looks; the pasted lines are copied by script from the files (the paste log is in the merge checks below), and no line inside a pasted block was edited. No pasted line names another location: the masked look replaced the one name before printing.
- **This merge's looks** (each labeled in the piece): a read-only `git log` and `git rev-list` (AS10b-6); the 1c hit's lines L182 to L184 with every name masked (AS10b-4); the fresh panel's AQ-302, its decisions' recommendations and its feed to this run (`ST8b` L680 to L688, L727 to L737); the Step 7 re-run's decisions list (`ST7b` L1771 to L1785, for the count of recommended wordings); the rulings log's `DR-107` to `DR-123` whole and single cited lines; the amendment-layer rules file whole (its rule 3 also names the readiness-check files in a notice sweep, only where a ruling permits, which DK10b-1's form follows).
- **Who teaches the wind, who goes out, the warning's form and the curating organization's name stay open** (`DRL` L1431, L1769; `ANS` L15, L26); no reader named any, and none is named here.
- **Figures:** the piece states no old-frame figure; the live figures appear only in its head and as cited counts. Shares are weights, never head counts.
- **The coinage** appears nowhere in the piece (the check below: 0 in all).
- **No other location is named** in the piece or in this record (the name scans below); the Round 2 raw files carry none.
- **No DEC number is assigned;** twelve decisions are proposed with recommended wordings (piece §9), for the orchestrator to number from DEC-260. Nothing in `REPASS_QUEUE_AND_PROGRESS.md`, `REPASS_COMPLETE_2026-11-04.md`, `10_Readiness_Check.md` or any pass file was edited by this merge.

## Read by this merge beyond the readers' lists (recorded; used only where the piece says so)
- **The readers' Round 1 outputs whole** (A, B, B's first run by `diff`, C) and their **Round 3 replies whole**; the frozen brief, the list and the checkpoint; the merge brief.
- **The format exemplars:** the Step 7 re-run piece (L1 to L90, L1500 to L1790) and its record (L1 to L95, L526 to L881); the headings of the symbols pair.
- **Sources, at the lines the piece cites:** `S10` whole; `ST10` L1 to L30, L144 to L165, L350 to L429 and single lines (L20, L180, L181, L185, L205, L214, L223, L232, L235, L249, L268, L271, L274, L280, L283, L289, L295, L298, L318, L325, L336, L467, L470); the rulings log L1728 to L1879 and L112, L117, L493, L1029, L1153 to L1156, L1225, L1431, L1660, L1669; the runbook L3082, L3083, L3085, L3087, L3096, L3121, L3122; `QUEUE`, `RC` and `ANS` whole; `ST12` L3, L5, L9, L26 to L30; `ST13` L3, L9, L25, L27 to L30; `ST14` L3, L24, L27; `ST16` L3, L26; `ST8b` L1 to L45, L680 to L688, L727 to L737; `AB1` to `AB3` L1 to L30; `Amendment_Layer_Rules.md` whole. **Lines that name another location were read, with names masked by script wherever the tool allowed, only to confirm their place, and are quoted nowhere** (`S10` L5, L9, L19 to L23 and the other subject lines; `DRL` L1154, L1156, L1669; `QUEUE` L11; `RC` L36).
- **The repository, read-only:** `git log`, `git rev-list`, `git rev-parse`, `git show --name-only` (counts only) and `ls` for file times. No `git` command changed anything; nothing was committed.

## Kept files (`M-132`)
The Round 1 outputs `.t8_amend_ST10b_readerA.md`, `.t8_amend_ST10b_readerB.md` (with B's first run, `.t8_amend_ST10b_readerB_FIRSTRUN.md`), `.t8_amend_ST10b_readerC.md`, and the Round 3 replies `.t8_amend_ST10b_round3_readerA.md`, `.t8_amend_ST10b_round3_readerB.md`, `.t8_amend_ST10b_round3_readerC.md` are kept in this folder as the round's working record, unedited, beside the two Round 2 files (`.t8_amend_ST10b_round2_raw_FIRSTRUN.txt`, `.t8_amend_ST10b_round2_raw.txt`), the frozen brief (`.t8_amend_ST10b_brief.md`), the list (`.t8_required_amend_ST10b.txt`) and the checkpoint (`.t8_amend_ST10b_CHECKPOINT.md`). The reader files, the replies, the brief and the list are byte-identical to their scratchpad copies in `amend_ST10b/` (`cmp`, by this merge; the merge checks below). None of these files is an input to a later step; this record and the piece are the merged result. No helper file was created in the repo by the readers or by this merge (scratch work stayed in the session scratchpad, `st10b_merge/`).

## Quotation audit (`Tools/quotation_audit.py <the Mirny pass folder> --files Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md --own-pass`, run from the repo root) · 2026-11-08 about 18:14 and 18:16, both before this record existed
*The pass-folder argument is required by the tool; it was given, as the Step 7 re-run's record ran it.* **The audit ran twice, both times before this record existed:** first at 18:14 on the piece as first placed, then at 18:16 after one change to the piece (the status line took B's and C's clause, split 10; snag 21 and one killed-in-drafting line were reworded to match; no quotation mark was added and no line was added or moved: the piece had 696 lines both times). **The second run's output is byte-identical to the first's** (`diff`, in the merge checks below), and it is the one pasted.

raw output, excerpted (1 line omitted: the positive control "HARD - case mismatch", whose test phrase names another location; it is one of the five controls behind the instrument line below, which reads VALID; the whole output is in the session scratchpad at `st10b_merge/qaudit_run2.txt`):
```
pass audited : Mirny
corpus mode  : default (own pass excluded)
corpus files : 6099   chars: 70,282,084
files audited: Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md
own-pass mode: a quotation may also be found in this pass's OTHER files (never in its own file)

=== POSITIVE CONTROLS ===
  [easy                      ] FOUND     a terminus is nobody's midpoint
  [HARD - blockquote wrap    ] FOUND     A pass may not proceed to Step 5 with a NEVER CITED row
  [HARD - outside Worldspace ] FOUND     Paste raw QA scan output into the QA block. Never summa
  [HARD - long wrapped       ] FOUND     Different content is not differentiation; a different q

  INSTRUMENT VALID: YES
  NEGATIVE CONTROL (must be absent): PASS - absent

=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 84
NOT FOUND in corpus: 29
  of those, in TABLE CELLS : 9
  of those, in PROSE       : 20

  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:32]           would have to mean ( st10 l357 to l370). the 2026-11-04 piece ran no check ( st10 l3); this is the first re-run of step 10's check
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:47]  [CELL]  h s: the acceptance and parking stand ( drl l1225); its reasons for
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:47]  [CELL]  have moved: the lived middle is handed to the cst ( drl l1742), the planet hold is lifted ( drl l1868)
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:49]  [CELL]  s: the next subject was named on 2026-10-13 (
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:80]           ( drl l1741), recorded as deferred to the cst and never as done (l1742 item 1). dec-120 (b), the held planet
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:80]           ( drl l1804), lifted on 2026-11-08 (item 3 below). dec-121 (a) and (b)
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:80]           (l1831): 43 rows applied in eight files, a new amendment layer rules.md whose tags name no location, observation entries m-305 to 
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:80]           (l1832). also ruled: a fresh panel once the amendments are applied, with the lover-faculty check (l1805 item 3; l1814 item 3); a p
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:81]           ( rc l51). u15, the in-order fold-in of steps 5 to 8, was proposed ( queue l38) and is held
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:82]           (l1868 item 1); end-of-file pointers approved for the five early step files, phase 3, phases 4 and 5, phase 10 and step 5 (item 2)
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:82]           (item 4); three wording calls (item 6). the finish run's dec-140 to dec-142, dec-160 to dec-163, dec-180 to dec-183 and dec-200 to
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:98]           (l19). 2026-11-04: stands with a note, parked ( st10 l150); its evidence
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:105]           (l20). 2026-11-04: parked; the coordinates to be re-taken by a normalized scan
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:106]           went into eight files, 00 runbook.md and 03 the phase spine.md among them, and a new amendment layer rules.md was written ( drl l1
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:106]           was rb l3059 to l3060 for st10 (l235) and is l3082 to l3083 today; item 1c was l3098 ( st10 l180) and opens at l3121; the
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:106]           sentence st10 placed at l3090 (l249) is at l3113 (a line that names another location; not quoted). whether any of the 43 rows name
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:300]  [CELL]  ( ans l24); the fresh panel still to run ( ans l27); pointers
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:301]  [CELL]  ( st13 l3; the same clause at st14 l3 and st16 l3) drl l1868 overtaken; and
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:304]  [CELL]  as st7b l19 places it at ab1 l3 ab1 l3 now holds
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:354]           ( drl l1814 item 1); (b) r-183 is decided (
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:391]           is now confirmed on re-test with the hold lifted ( drl l1868), and dk10-1's
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:402]           among the things not decided (l1878). no admitted line shows the research run
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:402]           ( st12 l26). dr-107 item 3 says the readiness check is re-run
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:409]           l51), and used by none. this merge read all of the readers' outputs and the same files, and its own session also carries the pushe
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:437]           ( rb l3085). st10 wrote the list of what
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:450]  [CELL]  and the signifier research has not run ( st12 l26); the developer's words on the signifiers
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:451]  [CELL]  ( drl l1868 item 1); the registry row applied ( queue l68; drl l1877 item 1). nothing for mirny's ulm. the one-word labels stay pr
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:472]           ( drl l1876); no name chosen ( drl l1877 item 3); by dr-110 item 3 the runs continue under
  [Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md:571]  [CELL]  the strongest finding's core set ( dr-113 ), wording pending; the wind account re-derived and partly applied; the conclusion

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```
**Triage by hand (each of the 29 misses read and classified):** 84 fragments tested, **29 not found** (9 in table cells, 20 in prose). **All 29 are connective prose** captured between two adjacent quotations on one line (the audit's own warning); the mechanical triage below confirms for each that the missed text lies between two quoted strings and inside none, and each was also read at its line: section 1.1 (L32); section 1.2's rows for `S10` L5 (L47, twice, cells) and L9 (L49, a cell); section 2's items 1 (L80, four times), 2 (L81) and 3 (L82, twice); AS10b-1 (L98); AS10b-2 (L105; L106 three times); AS10b-11's rows 5, 6 and 9 (L300, L301, L304, cells); AS10b-13 (L354); AS10b-15 (L391); AS10b-17 (L402, twice); AS10b-18 (L409); section 4's preamble (L437); AS10b-19's conditions 8 and 9 (L450, L451, cells); AS10b-20's remaining item 8 (L472); DK10b-10 (L571, a cell). **No misquotation was found by the audit.** Quotations shorter than the audit's floor (45 characters, 7 words) are not tested by it; **the supplementary check below tests every double-quoted string of any length** in the piece's prose against the Mirny folder's files including the reader dot-files and the `Datasheets/` subfolder, the rulings log, the runbook, the amendment-layer rules, the phase spine and generators files, both disciplines, the Founding Register, the Mirny spec, the relationship database, the culture file, the immigration file, both robot files, the climate READER, the stereotypes law, the orchestrator's facts file and this merge's git look, **with the piece itself excluded: 0 not found**. Without the dot-files three strings remain, each a reader's or the checkpoint's own wording quoted as theirs, and `grep -nF` finds each at its line. Before the first audit run, this merge's supplementary check had flagged five strings in a draft, all changed before the piece was placed: a quotation of the merge brief (re-set as plain prose, since the brief is not a source), a gap between two short quotations that formed a false quotation, and three readers' phrasings set in quotation marks (re-set as plain prose).

## Merge checks
```
$ python3 -I shortq10b.py ctl_piece.md   # positive control: two real quotations, one planted
  NOT FOUND L1: zq10b planted control sentence found nowhere at all
prose quoted strings tested: 3; files in corpus: 488; not found: 1
$ python3 -I shortq10b.py <the piece in the Mirny folder>   # the piece excluded from its own corpus; this record not yet in the folder
prose quoted strings tested: 216; files in corpus: 487; not found: 0
$ python3 -I shortq10b.py <the piece> --nodot   # the same, without the reader dot-files
  NOT FOUND L176: FIRES (unresolved)
  NOT FOUND L194: nothing committed since the finish run began
  NOT FOUND L668: A 13 concessions?
prose quoted strings tested: 216; files in corpus: 131; not found: 3
$ grep -inF <each string the second run could not see> <the file it quotes> | head -1   # prints line:first 48 characters
221:- **NEW result: FIRES (unresolved).** There 
61:6. **The repass and the application** — U0 
4:- 17:52: Round 2 re-run UNANIMOUS (51/51); Rou
$ python3 -I shortq10b_rec.py <this record, before the check and sweep blocks were pasted>   # its own quotations; corpus adds the audit output and the diff
prose quoted strings tested: 30; files in corpus: 490; not found: 0
$ diff qaudit_run1.txt qaudit_run2.txt && echo identical   # the audit's two runs, before this record existed
identical
$ python3 -I triage10b.py <the piece> qaudit_run2.txt   # each audit miss: between two quotations, or inside one?
audit misses: 29 between two quotations (connective prose); 0 inside a quotation
$ python3 -I triage10b.py ctl_triage_piece.md ctl_triage_aud.txt   # control: one planted miss of each kind
  inside a quotation: L2
audit misses: 1 between two quotations (connective prose); 1 inside a quotation

$ python3 -I checks10b.py city ctl_names.md   # positive control: three planted names, one joined to a word by an underscore
  hit L1 (name withheld, 8 chars)
== ctl_names.md: names scanned 53; hits 3
$ python3 -I checks10b.py city <piece>
== Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md: names scanned 53; hits 0
$ python3 -I checks10b.py city <this record, before the check and sweep blocks were pasted>
== Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08b_T8_Rounds.md: names scanned 53; hits 0
$ python3 -I checks10b.py city <each Round 2 raw file>; <this merge's two look files>
== .t8_amend_ST10b_round2_raw_FIRSTRUN.txt: names scanned 53; hits 0
== .t8_amend_ST10b_round2_raw.txt: names scanned 53; hits 0
== gitlook.txt: names scanned 53; hits 0
== masklook.txt: names scanned 53; hits 0

$ python3 -I checks10b.py ids <piece>   # the readers' own IDs ("A AS10b-n", "B DK10b-n") excluded
AS10b cited  : 1..20 (20 distinct)
AS10b headed : 1..20 (20 distinct)
AS10b in mapping table (bold): 1..20 (20 distinct)
cited but not headed: [] | headed but not in mapping: []
DK10b-: cited 1..16 (16 distinct); defined 1..16 (16 distinct); cited not defined: []; defined not cited elsewhere: []
AR-32x/33x: cited 320..333 (14 distinct); defined 320..333 (14 distinct); cited not defined: []; defined not cited elsewhere: []
AQ-32x/33x: cited 320..330 (11 distinct); defined 320..330 (11 distinct); cited not defined: []; defined not cited elsewhere: []
RF-ST10b-: cited 1..9 (9 distinct); defined 1..9 (9 distinct); cited not defined: []; defined not cited elsewhere: []
DEC- cited: 30 distinct, [5, 14, 16, 20, 21, 40, 41, 42, 60, 80, 81, 82, 100, 104, 120, 121, 122, 140, 142, 160, 163, 180, 183, 200, 204, 220, 230, 240, 245, 260]; none defined by this piece (the orchestrator numbers section 9)
$ python3 -I checks10b.py map <piece>   # every reader item mapped; every docket row traced
A: R1 findings 1..20; mapped 20; missing []
B: R1 findings 1..19; mapped 19; missing []
C: R1 findings 1..20; mapped 20; missing []
A docket rows 1..12 mapped 12; missing []
B docket rows 1..9 mapped 9; missing []
C docket rows 1..10 mapped 10; missing []
A AR mapped [320, 321, 322, 323, 324, 325, 326, 327, 328, 329]; missing []
B AR mapped [320, 321, 322, 323, 324, 325, 326, 327]; missing []
C AR mapped [320, 321, 322, 323, 324, 325, 326, 327, 328, 329]; missing []
A AQ mapped [320, 321, 322, 323, 324, 325, 326]; missing []
B AQ mapped [320, 321, 322, 323, 324, 325, 326]; missing []
C AQ mapped [320, 321, 322, 323, 324, 325, 326, 327]; missing []
A RF mapped [1, 2, 3, 4, 5, 6]; missing []
B RF mapped [1, 2, 3, 4, 5, 6]; missing []
C RF mapped [1, 2, 3, 4, 5, 6]; missing []
docket rows 16; rows without a traced finding: []

$ python3 -I checks10b.py mix ctl_mix.md   # positive control: one mixed line, one mixed block, one docket row
  line mix L1: old ['1,351,430'] live ['1,403,549']
prose line-level mixes: 1
  block mix ### AS10b-99 · control: old ['665,901', '50\\.73'] live ['692,971']
finding-block mixes (prose only): 1
docket rows carrying an old-frame figure: 1
$ python3 -I checks10b.py mix <piece>   # prose only: the pasted raw blocks are records and are excluded
prose line-level mixes: 0
finding-block mixes (prose only): 0
docket rows carrying an old-frame figure: 0
$ python3 -I checks10b.py keep <piece>
occurrences of keeper/keepers: 0 in all; 0 in prose outside pasted raw blocks

$ wc -l <piece> <this record, before the check and sweep blocks were pasted>
   696 Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md
   430 Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08b_T8_Rounds.md
  1126 total
$ grep -c "^### AS10b-" <piece>; grep -c "^| DK10b-" <piece>; grep -c "^```" <piece>
20
16
14
$ python3 -I build.py piece_src.md /dev/null   # the paste log re-printed (output to /dev/null; the piece is not rewritten)
@@FACTS_B@@ -> 42 lines
@@MASKLOOK@@ -> 6 lines
@@FACTS_A@@ -> 5 lines
@@GITLOOK@@ -> 19 lines
@@FACTS_C@@ -> 35 lines
@@FACTS_D@@ -> 25 lines
lines written: 696
$ cmp piece_draft.md <piece> && echo identical   # the piece in the folder is the built draft
identical
$ python3 -I count_list.py <the list>   # admitted lines (last line only)
TOTAL admitted lines: 2192
$ cmp each kept file against its scratchpad copy; sha256sum <the brief> | cut -c1-16
.t8_amend_ST10b_readerA.md identical
.t8_amend_ST10b_readerB.md identical
.t8_amend_ST10b_readerC.md identical
.t8_amend_ST10b_round3_readerA.md identical
.t8_amend_ST10b_round3_readerB.md identical
.t8_amend_ST10b_round3_readerC.md identical
.t8_amend_ST10b_brief.md identical
.t8_required_amend_ST10b.txt identical
5e2694db16b49a7d
```
**Reading the checks.** *Quotations:* the check's control found its two real quotations (`DRL` L1868 and L1156) and missed the planted one, as it should; the piece's 216 quoted prose strings are all found with the piece excluded from the corpus; without the reader dot-files three strings remain, each found by `grep -nF` at its line in the file it quotes (B's Round 1 label; A's wording; the checkpoint's line). This record's own quoted strings are all found. The mechanical triage puts all 29 audit misses between two quotations, and its control separates the two cases. *Names:* no other location's name in the piece, in this record before these blocks were pasted, in either Round 2 raw file or in this merge's two look files; the control found its three planted names. *IDs:* AS10b-1 to AS10b-20 are each headed once, cited and in the mapping table; DK10b-1 to DK10b-16, AR-320 to AR-333, AQ-320 to AQ-330 and RF-ST10b-1 to RF-ST10b-9 are each defined and cited; the DEC numbers are cited, not defined, because they belong to the decisions file and earlier pieces (and "from DEC-260" names the orchestrator's range), and **no new DEC number is assigned**. *Mapping:* every reader item is mapped (A's 20, B's 19 and C's 20 findings; A's 12, B's 9 and C's 10 docket rows; every request, question and reserved finding of A, B and C), and every docket row names the finding it serves. *Figures:* no prose line, no finding block and no docket row carries an old-frame figure; the control found its planted mixes. *The coinage:* 0 occurrences. *The paste log:* six pastes making seven fenced blocks (`FACTS` B holds two), each a verbatim slice of its file; the placed piece is the built draft (`cmp`). *The list and the copies:* 2,192 admitted lines; the reader files, replies, brief and list byte-identical to the scratchpad copies; the brief's hash as stated. **Counts:** the piece has 696 lines, 20 findings (AS10b-1 to AS10b-20), 16 docket rows (DK10b-1 to DK10b-16), 14 requests (AR-320 to AR-333; AR-320 done in part), 11 questions (AQ-320 to AQ-330), 9 reserved findings (RF-ST10b-1 to RF-ST10b-9), 12 decisions proposed and 7 pasted raw blocks (14 fence lines, paired).
**Edits to the piece after the audit:** none. The one change (split 10) came between the audit's two runs, both before this record existed; the piece in the folder is the audited text (696 lines) and is byte-identical to the built draft (`cmp`, above).

## American English sweep
**Words checked** (the script's pattern, `st10b_merge/ae_sweep10b.py`, the same as the Step 7 re-run's; named here by their American forms, so that listing them does not plant the British forms in this record): the -ize, -ized, -izes, -izing, -ization and -yze families written with an s (less an allow list of American words that end in -ise, such as premise, rise, otherwise, exercise and the forms of improvise and revise); the British forms of color, behavior, center, centered, license, defense, offense, favor, honor, labor, neighbor and harbor with their forms; of organize, recognize, realize and finalize; of traveled, canceled, modeled and labeled with their -ing forms; of fulfill, enroll, gray, catalog, dialog, program, meter, liter and analog; and of toward, while, among, learned, spelled, dreamed, acknowledgment and aging. The script also counts the one British spelling the developer keeps, without printing the word. Run with `python3 -I` on both files after every other section of this record was written; a final name scan and a final quotation check of this record follow.

raw output, excerpted (14 lines omitted: the positive control's hit lines, which print the planted British spellings, so pasting them would put those spellings into this record; the control's summary lines are kept; the control is reproducible from `st10b_merge/ctl_ae.md`):
```
$ python3 -I ae_sweep10b.py ctl_ae.md   # positive control: fourteen planted British spellings, one planted kept spelling
== ctl_ae.md
British-spelling hits: 14
kept spelling (the one allowed British form): 1
$ python3 -I ae_sweep10b.py <piece> <this record, before this block was pasted>
== Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md
British-spelling hits: 0
kept spelling (the one allowed British form): 0
== Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08b_T8_Rounds.md
British-spelling hits: 0
kept spelling (the one allowed British form): 1
$ python3 -I checks10b.py city <piece>; python3 -I checks10b.py city <this record, before this block was pasted>   # a final name scan after the check block was pasted
== Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md: names scanned 53; hits 0
== Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08b_T8_Rounds.md: names scanned 53; hits 0
$ python3 -I shortq10b_rec.py <this record, before this block was pasted>   # its quotations, after the check block was pasted
prose quoted strings tested: 30; files in corpus: 490; not found: 0
```
**Result:** no British spelling in either file. The kept spelling occurs once, in this record's setup (the run's hours), and not in the piece; the control found all fifteen planted forms (fourteen hits and the kept one). No other location's name is in either file, and every quotation in this record is found at its source.
