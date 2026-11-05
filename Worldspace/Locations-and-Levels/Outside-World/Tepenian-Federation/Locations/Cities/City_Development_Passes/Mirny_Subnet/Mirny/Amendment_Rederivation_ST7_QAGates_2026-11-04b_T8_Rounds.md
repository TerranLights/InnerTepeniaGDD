# Mirny · Amendment re-derivation · Piece ST7 (Step 7, the 17 QA gates) · T8 round record · 2026-11-04

**Companion to** `Amendment_Rederivation_ST7_QAGates_2026-11-04.md`. Raw tool output is pasted, not summarized. Working files are in this folder as `.t8_amend_ST7_*` (the Round 3 replies were read from their scratchpad copies, which are byte-identical to the folder copies: see Kept files).

## Setup
- **Reading list (trimmed, `DR-74`):** `.t8_required_amend_ST7.txt` (scratchpad copy `amend_ST7/t8_required_amend_ST7.txt`), **38 entries, about 7,662 admitted lines** (counted by this merge's scratch script: whole files by physical lines, spans by their ranges): the rules (entries 1 to 6: the stereotypes law; the runbook's spans; `04` L1 to L419; the QA quick reference; `00b`; `00d`); robot canon (7 to 15); the rulings log at 24 spans (16); the live sources at Mirny's rows only (17 to 22: the census, the Founding Register, the Mirny spec, the relationship database, the immigration composition file, the language blocs); the Step 7 and Phase 7 datasheets (23, 24); **Step 7 read whole** (25, 2,027 lines: report L1 to L205, raw scan output L206 to L2027); Step 6, Step 5 and the Frame at their spans (26 to 28); the amendment layer (29 to 38: the Phase 6, 7, 2, 9 and 8 pieces, the Phase 8 dockets, the Idelsk-Uralia piece, the robot-term piece's first 30 lines, the amendment register, the reconciliation note's lines 1 to 120). **The Phase 10 piece (U5) and the Step 5 piece (U6) were not inputs** (concurrent); the Step 6 and Step 8 pieces (U7, U9) were not yet written.
- **Brief:** `.t8_amend_ST7_brief.md`, identical for A/B/C with `{X}` the reader letter; **sha256[:16] f7c161f287228ccd** (computed by this merge on the folder copy and on the scratchpad copy: both match; the checkpoint records no hash); final at dispatch (`M-93`). It carries ten orchestrator-verified results with sources (its standing line 4 says "eight"), the developer's binding words, the stage order and twelve traps.
- **Readers:** three Opus agents dispatched 09:55 on 2026-11-04, inside the 05:00 to 14:59 window (checkpoint; `REPASS_QUEUE_AND_PROGRESS.md`, row U8). None refused any entry. Graphify: reader A observed no hook notice; reader B records disregarding the hook under `DR-6`; reader C saw none.

| Reader | Agent ID | Output lines | Bytes | PROOF blocks | Findings (Round 1 numbering) | Docket | Requests · questions · RFs |
|---|---|--:|--:|--:|---|---|---|
| A | `a8a94649b4a361756` | 908 | 120,160 | 38 | AS7-1 to AS7-40 (AS7-28 and AS7-31 folded) | D7-1 | AR-120 to AR-124 · AQ-110 to AQ-116 · RF-ST7-1 to RF-ST7-5 |
| B | `a39f7707a5adca9a9` | 1,058 | 138,389 | 38 | AS7-1 to AS7-36 | D7-1 | AR-120 to AR-124 · AQ-110 to AQ-115 · RF-ST7-1 to RF-ST7-4 |
| C | `a44c1c55f91e19252` | 1,058 | 141,016 | 38 | AS7-1 to AS7-44 | its AR-121 (a stale-line docket) | AR-120 to AR-124 · AQ-110 to AQ-116 · RF-ST7-1 to RF-ST7-5 |

Line and byte counts by `wc` on the folder copies, which are byte-identical to the scratchpad copies (`cmp`); PROOF blocks counted by `grep -c '^### PROOF:'` (38 each). Tool-use counts are not recorded in the checkpoint and are not given here.
- **Self-checks before handback (as each reader records):** A lists no scripted check; it copied positional PROOF lines that carry other locations' names as written, with the EXEMPT line (its snag 12). B checked line counts with `wc -l` and a final-byte check before writing LINES and LLAST, and records its self-corrections (its SN-14). C ran a read-only script comparing its hand-copied quotations and PROOF fields with the cited lines (it generated nothing), re-cut one PROOF field and about twenty quotations by hand, and then passed 244 quotations and 38 PROOF blocks (its snag 14).
- **Ruling-log freeze (`M-302`):** not checked by this merge writer.

## Round 1 headline claims (union, before Round 3)
| Claim | A | B | C |
|---|---|---|---|
| The register misfiles F-2 and S7-RF-8 under the leg-4 row | both | F-2 only (S7-RF-8 "accurate as CLOSE") | both |
| E1 · E2 · F-10 | RE-DERIVE · CLOSE · RE-DERIVE | the same | the same |
| F-5 | CLOSE | CLOSE | REWORD |
| E5 | KEEP with a note | REWORD | REWORD |
| F-16 | REWORD | RE-DERIVE | REWORD |
| S7-RF-2 | CLOSE | CLOSE in part | CLOSE |
| Gate 3 | MUST BE RE-RUN | CHANGES + MUST BE RE-RUN | MUST BE RE-RUN |
| Gate 10 | STANDS WITH A NOTE | STANDS | STANDS WITH A NOTE |
| Gate 11 | CHANGES | STANDS WITH A NOTE | CHANGES |
| Gate C | MUST BE RE-RUN | CHANGES (source check now) | CHANGES (anchor sweep re-run) |
| Gate G | CHANGES | STANDS WITH A NOTE | STANDS WITH A NOTE |
| Gate 3's L55 clearances | not found | both void | "P7-15 against P10-8" only |
| P10-8 | the register's direction noted, not adopted | "withdrawn" | "withdrawn" (per the register and the Phase 6 piece's feed) |
| Section 1's highest-importance flag | none of the old kind; weight on the strongest-finding ruling | closed with E3; no replacement | a new flag (its AS7-44: the unamended text) |
| Speech on Gate 1's thin list | partly answered | leaves the list | partly a fact |
| Gate C's ruling-C flag | closes (Q-65) | closes (Q-65) | a tier matter, left open |
| Tag S | symbols and stage order | stage order and symbols | symbols only |
| Numbering | AS7-1 to AS7-40 | AS7-1 to AS7-36 | AS7-1 to AS7-44 |

## Round 2 (`Tools/triple_read_verify.py`) · run 2026-11-04 about 10:28 · UNANIMOUS on the first run (114 of 114 field sets, 38 entries)
raw output (full; file `.t8_amend_ST7_round2_raw.txt`):
```
required files: 38
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 309-372,378-426,430-540,2922-2960] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/04_QA_Gates_and_Differentiation.md  [range 1-419] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Corpus_Reference_Sheets/QA_Gates_Full_Text_Quick_Reference.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00b_General_Population_Discipline.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00d_Shadow_Proportion_Discipline.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md  [range 1-120,177-190,329-438] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Laws_of_Robotics.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Doll_Representation_Categories.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Characters/Robot-specific/Robot_Universals/1_-_Part_I_Ground-Level_Fundamentals/03_Build/README.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Characters/Robot-specific/Robot_Universals/1_-_Part_I_Ground-Level_Fundamentals/06_Language/README.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Characters/Robot-specific/Robot_Universals/2_-_Part_II_Differentiation_Method/08_Reproduction_Kinship_and_the_Absence_of_Genetic_Relatedness/README.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Characters/Robot-specific/Robot_Universals/3_-_Part_III_Robot_Cultural_Universals/11_Kinship_Clan_and_the_Mentor-Mentee_Institution/README.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Characters/Robot-specific/Robot_Universals/3_-_Part_III_Robot_Cultural_Universals/13_City-Locality_as_the_Seat_of_Identity/README.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Characters/Robot-specific/Robot_Universals/3_-_Part_III_Robot_Cultural_Universals/14_Generational_Identity_-_Gen-Mark_as_Real_but_Non-Hierarchical/README.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Step_7.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Phase_7.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/07_QA_Gates.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/06_Differentiation.md  [range 1-14,160-215] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/05_Reconciliation.md  [range 1-8,80-109,712-722] ===
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

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

## Round 3 (SendMessage to the same three agents) · 2026-11-04, replies time-stamped 10:34 · cross-check done
Each reader was sent seven points the three appeared to share (K1 to K7), a request to map the other two readers' findings onto the old Step 7 items and list every category, gate-status or central-claim split with the position it would hold, a request to check the single-finder finds against the pass lines, a numbering proposal, and a request to list any claim in the other two re-derivations it would not accept. Replies: `.t8_amend_ST7_round3_reader{A,B,C}.md` (120, 151 and 186 lines; read from the scratchpad copies `amend_ST7/t8_amend_ST7_round3_reader{A,B,C}.md`, byte-identical by `cmp`). **The text of K1 to K7 as sent is not in the folder; the topics below are read from the replies.**

| Reader | Part 1 OBJECTs | Part 2 splits listed | Single-finder finds checked | Part 3 claims not accepted | Coverage |
|---|---|---|---|---|---|
| A | 0 | 15 (concedes on 1, 3, 5, 9, 10, 12) | B's and C's: 10 CONFIRM, 2 OBJECT (B's Maritime sector-tier note; B's ratio of the two censuses) | 7 | read B's L325 to L742 and C's L339 to L742; one self-correction (its own density figure) |
| B | 0 | 19 (concedes on S-2, S-3, S-4, S-10, S-11) | C's 10 (8 CONFIRM, 2 OBJECT: C's AS7-44; C's 140.36); A's 8 (8 CONFIRM); its own 3 | 5 | read A's L269 to L595 and C's L339 to L742; one self-correction (S7-RF-8's misfiling) |
| C | 0 | 21 (concedes on 6, 9, 10, 11, 17) | 19 of A's and B's (17 CONFIRM, 1 CONFIRM in part, 1 OBJECT in part: B's Maritime note) | 7, plus its own self-corrections | read A's L269 to L595 and B's L325 to L745 |

### The shared points
| K | Topic (as read from the replies) | A | B | C |
|---|---|---|---|---|
| K1 | the register files F-2 (E1's flag) and S7-RF-8 (F-10's scope) under the leg-4 and re-learning CLOSE row | AGREE | AGREE (self-correction: it had missed S7-RF-8) | AGREE |
| K2 | categories: E1 RE-DERIVE; E2 CLOSE; F-5; F-10 RE-DERIVE | AGREE (F-5 CLOSE) | AGREE (F-5 CLOSE) | AGREE; concedes F-5 CLOSE from its Round 1 REWORD |
| K3 | Step 7's L3 stale since `DR-76`; docket D7-1, never applied | AGREE | AGREE | AGREE |
| K4 | the standout's ledger rests on the retired booking; re-choose pending the strongest-finding ruling; the ledger stays as Act 1's form | AGREE | AGREE | AGREE |
| K5 | both L55 clearances ("P7-15 against P10-8"; "the Phase 9 amendments") void; the light-model clearance stands | AGREE (it had missed both; P10-8 pending, not "withdrawn") | AGREE (P10-8 "withdrawn") | AGREE (it had missed the second; P10-8 "withdrawn", the Phase 10 piece pending) |
| K6 | checks whose input is live canon can run now; no gate is re-run on the unrewritten pass files as if amended | AGREE | AGREE | AGREE |
| K7 | as-written and live figures never mixed in one finding; symbols facts only | AGREE (self-correction: its own Gate 11 density mixed them) | AGREE | AGREE (names the places where all three mixed them) |

### The splits, and how they were settled in the merge (the position two or three readers hold after Round 3; otherwise the most conservative reading; split named in the piece)
| # | Point | Positions after Round 3 | Settlement |
|--:|---|---|---|
| 1 | **Gate 3 status** | A, B: MUST BE RE-RUN, the changed list as its note (B conceded); C: CHANGES + MUST BE RE-RUN (B's Round 1) | **MUST BE RE-RUN AFTER APPLICATION, its list changed now** (A, B); C named (AS7-4) |
| 2 | **Gate 10** | all: STANDS WITH A NOTE (B conceded) | **STANDS WITH A NOTE** (AS7-11) |
| 3 | **Gate 11** | all: CHANGES (B conceded) | **CHANGES**; PASS on arithmetic stands by construction (AS7-12) |
| 4 | **Gate C** | all: CHANGES, the source and anchor check now, the pass-text check after application (A conceded) | **CHANGES** (AS7-13) |
| 5 | **Gate G** | all: STANDS WITH A NOTE (A conceded) | **STANDS WITH A NOTE** (AS7-17) |
| 6 | **F-5** | all: CLOSE (C conceded) | **CLOSE**; the residue wording pointed to A7-18 and the Step 6 piece (AS7-19) |
| 7 | **E5, F-4** | all: REWORD (A conceded) | **REWORD** (AS7-22) |
| 8 | **Q-126** | A: REWORD, folded into AQ-6 (conceded from CLOSE in part); C: REWORD with B's neutral wording; B: CLOSE in part (A's Round 1) | **REWORD**, asked neutrally once with the Phase 6 piece's AQ-6 (A, C); B named (AS7-22) |
| 9 | **S7-RF-2** | A: CLOSE, residues named; B: CLOSE, residue named (conceded from CLOSE in part); C: CLOSE in part (conceded to B's Round 1) | **CLOSE, residues named** (A, B); C named (AS7-21) |
| 10 | **F-16, PA-88** | A: RE-DERIVE (conceded); C: RE-DERIVE (conceded); B: REWORD (conceded: "the conservative class") | **RE-DERIVE** (A, C), PROVISIONAL on A9-5; B named (AS7-27) |
| 11 | **F-26, S7-RF-3** | A: REWORD; B: REWORD (conceded); C: RE-DERIVE (conceded) | **REWORD** (A, B); C named (AS7-33) |
| 12 | **F-20** | A: REWORD (Round 1); B: REWORD in part; C: KEEP (P) | **REWORD in part** (A, B), PROVISIONAL on the Phase 9 piece, with C's note that the flag stands on the pass line until applied (AS7-30) |
| 13 | **F-21** | B: REWORD (CAND-L2); C: REWORD carrying both notes; A: not treated apart, both notes confirmed | **REWORD with both notes** (B, C) (AS7-31) |
| 14 | **F-22** | A, C: RE-DERIVE the wind items, the rest stands; B: REWORD (split) | **RE-DERIVE the wind items; the rest stands** (A, C); B named (AS7-32) |
| 15 | **Speech on Gate 1's thin list** | A, C: stays in part (the rule and the tier are facts; words, accent, register absent by rule); B: "speech leaves the list" | **stays in part** (A, C); B's wording among the claims not accepted (AS7-2, AS7-28) |
| 16 | **Free hours and dress beyond function** | A, B: constraint-only (Q-75 is national); C: free hours to the CST, dress answered by Q-75 | **constraint-only** (A, B); C's wording among the claims not accepted (AS7-28) |
| 17 | **PA-85** | A, C: overturn condition fired; B: still true, four groups; C (Round 3): both true | **REWORD; both true** (C's form, compatible with A and B) (AS7-23) |
| 18 | **Tag S** | all: symbols and the stage order (C conceded) | **symbols and the stage order**; AQ-118 (snag 4) |
| 19 | **Gate I: the supporting tier's class** | A, B: inflected [D] as the leading reading, to be counted; C: unclassed until the re-run | **inflected [D], to be counted at the re-run, not asserted** (A, B); C named (AS7-15) |
| 20 | **Gate I: the curating organization's class** | A, B: originated in principle, form unclassable (a flag) until AR-2 and AR-18; C: originated in principle | **A's form** (A, B; C compatible) (AS7-15) |
| 21 | **Section 1's highest-importance flag** | A: adopt C's Round 1 new flag (its AS7-44); B: none of the old kind, C's point as a reserved method finding; C: both as one line (no flag of the old kind; two matters of most weight) | **no two-reader majority; the most conservative reading:** no new flag; the matter of most weight is the strongest-finding ruling; the unamended-text point kept as RF-ST7-9 (B's and C's overlap) (AS7-38) |
| 22 | **Gate 11's "Maritime size"** | A, C: re-run on the live distinctive tier; the tier note is the harbor watch's, not the sector's; B: stands, with a sector-tier note | **A and C**; B's note among the claims not accepted (AS7-35) |
| 23 | **Gate 3's "told nothing at the door"** | B: both halves rest on the premise, re-derive both; C (Round 3): B's form; A: dissolves in part | **B's form** (B, C; A's compatible) (AS7-4) |
| 24 | **Gate 7: a research row whose finding was later corrected** | all: the class stays "changed" (B's rule); A's separate count reserved | **B's rule; A's sub-count reserved** (RF-ST7-10) (AS7-8) |
| 25 | **P10-8 inside the void clearance (K5)** | B, C: "withdrawn"; A: pending (its Part 3 objection) | **pending Phase 10**: "withdrawn" is a claim not accepted (A), excluded by the merge rule; the Phase 10 piece's own CLOSE is in the cross-reference note only (AS7-36) |
| 26 | **S7-RF-6** | A: KEEP (Step 8's call); B: KEEP reserved with C's conditional note; C: reworded, conditional on AR-16 | **KEEP reserved, with C's conditional note** (A, B) (AS7-34) |
| 27 | **Raw L1705** | A: mark it (in the re-run block); B, C: the raw output gets no mark | **no mark on any raw line; the note goes in the appended re-run block** (B, C; A's form compatible) (AS7-41) |
| 28 | **The Maritime question** (B's AQ-114) | A: drop it; B: keep it; C: keep it narrowed (the watch's tier, not the sector's) | **kept in C's narrowed form** (B, C), with no sector-tier change written (AQ-116) |
| 29 | **Finding numbers** | A: C's set AS7-1 to AS7-44 plus AS7-45 (records); B: A's set AS7-1 to AS7-40 plus three; C: one set AS7-1 to AS7-49 in Step 7's order | **C's set, AS7-1 to AS7-49** (Step 7's own order; the gate numbers agree in all three) |
| 30 | **Request numbers** | A: AR-120 form, 121 docket, 122 extent, 123 timing, 124 instruments, 125 pieces, 126 Step 2; B: 120 extent, 121 pieces, 122 form, 123 Step 2, 124 instruments, 125 docket, 126 timing, 127 tag S, 128 anchors; C: 120 extent, 121 form, 122 pieces, 123 Step 2, 124 instruments, 125 anchors | **C's AR-120 to AR-125**, plus **AR-126** (the docket as a request, A and B) and **AR-127** (the re-run timing, C's Round 1); tag S as a question (AQ-118), not a request |
| 31 | **Question and reserved-finding numbers** | three colliding sets | **AQ-110 to AQ-121** (C's base with A's and B's items); **RF-ST7-1 to RF-ST7-11** (C's eleven; RF-ST7-7 without B's ratio) |
| 32 | **Step 7's own stale-line docket** | A, B: D7-1 only; C: D7-1 to D7-4 | **D7-1 to D7-4** (C's), with the record marks; never applied (section 5.2) |

### Single-finder finds, checked against the pass lines in Round 3
| Find | Finder | Checked by | In the merge |
|---|---|---|---|
| Phase 8's candidates now number seven (CAND-L2 falls), so the tracker's "seven" may be right for another reason | B | A, C CONFIRM | AS7-1, AS7-31 |
| PA-74 (Gate P) is the debt clause Step 5 registers; "keepers" is coinage; the debt a spread | B, C | A CONFIRM | AS7-16 |
| Phases 7 and 8 ratified, so the bare ✅ mismatch narrows to Phases 9 and 10 (NOT WIND) | C | A, B CONFIRM | AS7-1, AS7-31 |
| Step 5's feed phrase sits at `05` L718 today (Step 7 cites L714) | C | A, B CONFIRM | AS7-18; snag 12 |
| The live spec's L152 is blank, so F-14's anchor no longer holds the line | C | A, B CONFIRM | AS7-23 |
| The robot file's chamber line against `DR-55`'s "entire array" | C | A CONFIRM | snag 11 |
| The scale question for a taught wind (a robot majority with no childhood) | C | A, B CONFIRM (reserved) | RF-ST7-6 |
| The founders scans must also hunt "sponsor only", "three exile groups", "a relation, not a stock" | C | A, B CONFIRM | section 5 (Gate 3) |
| Gate F's Band-5 absolutes hit ("nobody here authored") meets A9-21's "two media (one found, one made)" | C | A CONFIRM | AS7-14 |
| Snag 7's kill list (L196) is a record to mark | B, C | A CONFIRM | AS7-41 |
| The Frame holds the founders' Act OPEN, so the first generation's learning is Act 1 only by the brief's reading | C | B CONFIRM | AS7-14 |
| Step 6's Transmission cell (`06` L214) and mechanism line (`06` L208) rest on the retired premise | C | B CONFIRM | AS7-18 (feed) |
| The immigration file disagrees with itself (L623 to L624 against L627) | C | B CONFIRM | snag 9 |
| The P7-9 bracket at raw L1705 is "wrong in method": a note only | A, C | B CONFIRM | AS7-41 |
| Phase 10 read the symbols against Mirny "as Phases 1–9 found it" (raw L918) | A | B, C CONFIRM | AS7-48 |
| Band 5 also holds on Census II | A | B, C CONFIRM | AS7-14 |
| AIU-2's row-sum count against the share times Census I (rounding) | A | B, C CONFIRM | snag 8 |
| One label over several things as Gate 6's inverse failure | A | B, C CONFIRM (reserved) | RF-ST7-3 |
| An append-only pass makes notice-against-derivation contradictions by construction | A | B, C CONFIRM | RF-ST7-9 |
| Research accounting split by whether a changed finding still stands | A | B, C CONFIRM (reserved) | RF-ST7-10 |
| PA-86 stands: `DR-55`'s array concerns robots built here, not arrivals | A | B CONFIRM | AS7-42 |
| Gate C's ruling-C flag is answered by the adopted Q-65 | A, B | C CONFIRM (it had missed it) | AS7-40 |
| The wind pieces' status lines read PROPOSED while `DR-105` accepts only the composition and Phase 8 pieces: a Gate 0 mismatch | B | C CONFIRM | AS7-1 |
| Phase 6's amended P6-13 against its unamended P6-3 and P6-17: a Gate 3 target | B | C CONFIRM | AS7-4 |
| The amendment layer disagrees with itself on language: a Gate 3 target | B | C CONFIRM | AS7-4; RF-ST7-8 |
| F-7's pointer "justified by DR-9 alone" now reads `DR-46` and `DR-99` | B | C CONFIRM | AS7-24 |
| "Told the picture" (Step 5's BT-3 refinement) also rests on the retired premise | B | C CONFIRM | AS7-4 |
| AR-24 (what carries warnings when the relay is down) as a new parent-facing question | B | C CONFIRM | AS7-16 |
| The relay is now heard whenever a warning arrives | A | C CONFIRM | AS7-47 |
| The spine's deficits #5 and #7 state the premise with no amendment notice | A (and C) | B, C CONFIRM | AS7-17 |
| `P9` L170 in Step 7 is the typical-resident bullet the Phase 9 piece places at L174 | B | C CONFIRM in part | snag 12 |
| Q-81 is answered by `DR-56` item 5, not `DR-55` | B | C CONFIRM | snag 3 |
| Maritime: "part of the sector's tier moves" | B | A OBJECT; C OBJECT in part | not carried (claims not accepted) |
| "At live Census I no real-world comparable changes scale class" (with a ratio of the two censuses) | B | A OBJECT (C in Part 3) | not carried (claims not accepted) |
| A new highest-importance flag (C's AS7-44) | C | B OBJECT (A adopted it) | split 21: not a flag; RF-ST7-9 |
| Required ground "140.36 km²" | C | A, B OBJECT | corrected to 140.35 (AS7-46) |

### Claims not accepted (left out of the merge; each listed with what was done)
| Claim | Whose | Objected to by | Why | In the merge |
|---|---|---|---|---|
| "The city is 3.86 % larger than the pass assumed" (a ratio of the live to the as-written census), with RF-ST7-4's scale-class claim | B (AS7-12, RF-ST7-4) | A, C | mixes the as-written and live sets in one finding; the comparables are not on the list | dropped; RF-ST7-7 keeps only whether the extent row predates the live census |
| The live population set over the Frame's as-written extent (about 10,397 and 7,272 per km²) | A (AS7-12), B (AS7-12) | A (self), C | a blend of the two sets | dropped; only the live required ground [CALC] and AR-120 (AS7-46) |
| Maritime: "part of the sector's tier moves" | B (N-4, AS7-12, AQ-114) | A, C | no admitted line places the harbor watch inside the Maritime share; only the watch's tier is ruled ("not free-tier; tier unplaced") | dropped; the watch's tier unplaced (AR-60); the question kept in C's narrowed form (AQ-116) |
| P10-8 stated as "withdrawn" | B (W-6, AS7-4), C (W-5, AS7-4) | A | a Phase 10 result, pending; sourced to an unverified register row or a feed | **pending Phase 10** (AS7-36); the Phase 10 piece's CLOSE in the cross-reference note only |
| "speech leaves the list" | B (AS7-2, AS7-32) | A | words, accent, slang and register stay absent by rule (`AP8` L451) | speech stays on the thin list in part (AS7-28) |
| "Required ground 140.36 km²" | C (AS7-41) | A, B | 1,403,549 divided by 10,000 is 140.3549 | 140.35 (AS7-46) |
| Q-126 "answered in substance by the ruling" | C (AS7-22) | A | the Social Contract's ground is answered only by a recommendation (the Phase 6 piece's AQ-6) | REWORD; the question stays open (AS7-22) |
| Quoting Step 7's collective name for other places in two table cells | C (part 2) | A | names other locations | the name is not reproduced; Q-127 is cited by ID (AS7-42; snag 15) |
| A new highest-importance flag: the unamended pass text | C (AS7-44) | B (A adopted it in Round 3) | the expected append-only state (`DR-74`), not the pass's most important defect | no new flag; RF-ST7-9 (AS7-38) |
| "ruling C is known only through `D16`" read as an open tier matter | C (T-3, AS7-13) | B (and C itself in Round 3) | Q-65 adopted: "ruling C stands as the developer's ruling" (`DRL` L1130) | the flag closes (AS7-40) |
| "free hours" under the CST; "dress beyond function" answered by Q-75 | C (AS7-28) | B | goes past what the stage order names and past Q-75's national scope | both stay constraint-only (AS7-28) |
| Gate 4's conjunctions stated as surviving while the re-run is pending | A (AS7-5) | B | a re-run's result cannot be stated before the run | "expected to survive" (AS7-5) |
| "the harbor call, Mirny's practice, essential" | B (AS7-15) | C | "essential" is ruled of the harbor watch and the extraction crews; the call is "public and binding on ships and offload by practice" | the call is not carried as a Gate I element; its facts at AS7-19 |
| The errata tally "two close, two close with replacements, two reword, one re-derives" | B (W-3) | C | counts seven for six errata | E2 closes; E3 and E4 close with replacements; E5 and E6 reword; E1 re-derives (AS7-49) |
| The as-written and live composition written inside one finding | A (AS7-36), B (AS7-19) | C | one finding, two sets | split into AS7-45 (as written) and AS7-46 (live) |
| The as-written and live counts inside the symbol finding | A (AS7-37), C (AS7-42) | C (including itself) | mixes the sets | AS7-48 states the live facts and points to AS7-45 and `NOTE` L97 for the old |

## Settled in the merge (beyond the splits)
- **Union applied:** A (the register-row errors list; the Gate 6 inverse failure; the research split count; the append-only finding; the Census II Band check; raw L918's symbol character; PA-86's note; the Step 2 request; the live anchors request; G4 and G5 as a ruled conjunction); B (CAND-L2 and the seven candidates; the wind pieces' status lines; the two void clearances; "told the picture"; the language disagreement as a Gate 3 target; F-7's pointer; AR-24 at Gate P; Q-126's neutral wording; the extended Gate 1 term list; the stage order's place in the closing test); C (the Phases 7 and 8 ratification at Gate 0; `05` L718; the blank spec L152; the Frame's OPEN Act; the Step 6 cells; the scale question for a taught wind; the founders scan patterns; the Band-5 absolutes hit; the stale-value finder list; the docket D7-1 to D7-4; the numbering; the split of the as-written and live findings).
- **The Phase 10 and Step 5 pieces** were in the folder (PROPOSED) when the merge was written. They were read as models of form and, for the cross-reference note at the end of the piece's section 4, at their headers, sections 0, feed rows to Step 7 and decisions paragraphs; nothing in the findings was changed by them.
- **Figures:** all three readers agree on the live set (1,403,549; robots 50.63 %; 36 stocks; 13.73 %; 23.24 %; the PROPOSED tiers 42.2 / 23.1 / 34.7 % of 1,057,064 workforce units; English alone on mid-points). The as-written figures appear only in AS7-45 and in quotations of Step 7's lines.
- **Shares are weights, never head counts or hours** (`DR-12`).
- **"Keepers"** appears in the piece only as Step 7's or the pass's own word, marked as coinage; no group is named by it and no replacement is coined.

## Kept files (`M-132`)
The Round 1 outputs `.t8_amend_ST7_readerA.md`, `.t8_amend_ST7_readerB.md`, `.t8_amend_ST7_readerC.md` are kept in this folder as the round's working record, unedited, beside `.t8_amend_ST7_round2_raw.txt`, the frozen brief `.t8_amend_ST7_brief.md` and the checkpoint `.t8_amend_ST7_CHECKPOINT.md`. The Round 3 replies are kept as `.t8_amend_ST7_round3_readerA.md`, `.t8_amend_ST7_round3_readerB.md`, `.t8_amend_ST7_round3_readerC.md` (copied by the orchestrator, time-stamped 10:35; this merge read the byte-identical scratchpad copies `amend_ST7/t8_amend_ST7_round3_reader{A,B,C}.md`, because the folder copies were not yet listed when it first listed the folder; `cmp` confirms all three). None of these files is an input to any later step; this record and the piece are the merged result. No helper file was created in the repo by the readers or by this merge (scratch work stayed in the session's scratchpad, `amend_ST7_merge/`).

## Quotation audit (`Tools/quotation_audit.py`, `--files Amendment_Rederivation_ST7_QAGates_2026-11-04.md --own-pass`) · 2026-11-04 about 11:06, run before this record existed
raw output, excerpted (1 line omitted: the positive control "HARD - case mismatch", whose test phrase names another location; it reported FOUND, and the instrument line below reads VALID; the whole output is in the session scratchpad at `amend_ST7_merge/qaudit_final.txt`):
```
pass audited : Mirny
corpus mode  : default (own pass excluded)
corpus files : 6089   chars: 69,785,185
files audited: Amendment_Rederivation_ST7_QAGates_2026-11-04.md
own-pass mode: a quotation may also be found in this pass's OTHER files (never in its own file)

=== POSITIVE CONTROLS ===
  [easy                      ] FOUND     a terminus is nobody's midpoint
  [HARD - blockquote wrap    ] FOUND     A pass may not proceed to Step 5 with a NEVER CITED row
  [HARD - outside Worldspace ] FOUND     Paste raw QA scan output into the QA block. Never summa
  [HARD - long wrapped       ] FOUND     Different content is not differentiation; a different q

  INSTRUMENT VALID: YES
  NEGATIVE CONTROL (must be absent): PASS - absent

=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 97
NOT FOUND in corpus: 49
  of those, in TABLE CELLS : 16
  of those, in PROSE       : 33

  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:20]           (p7-15's conclusion reverses, a7-2; p10-8's own disposition is pending phase 10) and
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:41]  [CELL]  s c n (stage-ordered; speech ruled in part) l22
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:41]  [CELL]  p c l23 highest-importance flag w c p l24 standout
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:43]  [CELL]  w p) gate 4 l57, l58 w n g gate 5 l60, l61 n w gate 6 l63, l64 w g gate 7 l66, l67 c i p g gate 8 l69, l70 w p gate 9 l72, l73 w n
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:135]           table ( areg l145 to l159) is its unverified single-reader draft of 2026-10-13 ( areg l7
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:139]  [CELL]  accurate (all) close close. withdrawn by ruling, not only rated implausible: drl l1124
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:139]  [CELL]  leg 4 withdrawn, legs 1 to 3 stand ( ap6 l238). the erratum's
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:140]  [CELL]  accurate, understated in mechanism (a, b): the ruling exceeds
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:140]  [CELL]  close close with a replacement (e4 ): drl l1124 settles e4
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:142]  [CELL]  misfiled (k1, all three): f-2 is e1's flag on
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:145]  [CELL]  is not established either way close close, residues named: the channels (household, crew, mentor bond) are ar-23; the record half 
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:149]  [CELL]  ) contradicts its category reword close (as7-19): q-67 adopted
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:150]  [CELL]  accurate reword close (as7-19): its fix, the cand-dependent tag, is withdrawn by the same answer. the residue wording (
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:151]  [CELL]  ) keep / reword (unsplit) reword (as7-22): the duty is a second national ground (
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:153]  [CELL]  understated (all) keep / reword (unsplit) re-derive (as7-25): its fix
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:154]  [CELL]  accurate in direction keep / reword (unsplit) re-derive (as7-27; provisional on a9-5): the claim no longer stands for the teaching
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:173]           (b; c one of two; a missed; k5) (as7-36) l58, gate 4's conjunctions and
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:173]           which predates the curating organization (cand-10, ap7 l136) (as7-7) l73, gate 9 run 2 (as7-29, as7-10) l76 and l154, the neighbor
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:173]           (as7-12, as7-35) l87, l88, l131, l151: gate i's ratio and cluster, f-26, s7-rf-3 (as7-15, as7-33) l91, pa-74, which is the debt cl
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:174]           (as7-26, as7-8) l21, l49, l100, l123, l169, speech among the empty slots and
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:174]           (as7-28, as7-44) l79, l142, l143, l181, gate 11 and pa-83 priced on the census as written against the frame's extent quotation (as
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:175]           ) has fired ( drl l1661) (as7-23) l82 and l94, gate c's founders restatements and gate g's g4 check, both against dr-46 only (as7-
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:176]           drl l1219) and q-67 adopted ( drl l1130) (all three) (as7-40, as7-6) l82 and null l145
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:176]           ( drl l1130) (a, b; c confirmed) (as7-40, as7-13) l46 and l126, the tracker's bare against phases 7 to 10: phases 7 and 8 were rat
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:176]           guilt is not a sanction ( drl l1477) (as7-35) l79, the cleared
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:177]           on the distinctive tier as written (as7-35, as7-46) raw l1698 to l1707, the workforce, baseline, tiers and
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:177]           of that day: a record; the free tier is now a determined figure ( aprt l18) and phase 7's bracket was
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:186]           nns l21) and the physics ( spec l93, l104, l153). refused
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:229]           ( dr-77 , dr-79 ), whose own peer-free test passes as a pairing, half national ( ap6 l118). expected weakest cell d : the duty cla
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:298]           (raw l1723), now reads dr-46 and dr-99 (b; c confirmed); under dr-99 the
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:321]           narrows to not yet, not here, not wanting , with no exclusion (a7-11), a condition and not a category of native; (iii) there is no
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:331]           ( ap6 l146), never reworded into something else. the spine's signal claims reverse in part: the warnings ride the relay, so
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:342]           stands, sharper: the relay carries the warnings
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:342]           stands only for the first generation (act 1); afterward a loss has two possible accounts, the person or the warning, and which is 
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:342]           is re-run under dr-80 : guilt is not a sanction; a reproach by others would be one and is unruled (ar-26); after the first generat
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:342]           ( ap7 l213); what the guilt pushes toward is priced by the physical cost of going out (exposure for a human; charge and a possible
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:343]           in a city whose majority body has no childhood (rf-st7-6) (c)
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:347]           void pending dec-012. the ratified additions use the coinage and
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:413]           is a position in a hazard, held by everyone and exercised mostly by a few, never the general answer; the old narrow-role error
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:426]           holds (the largest share 13.73 %); 36 stocks; census i 1,403,549; four exile groups at 23.24 % of each body, a minority. the chara
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:443]  [CELL]  means whoever is most strategically able to address a weather hazard, never
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:444]  [CELL]  is the pass author's coinage: no position is cast as
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:455]           ), their feed rows to step 7, the step 5 piece's feed to step 6 (for e1) and their decisions paragraphs were used. nothing above w
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:456]           (as7-36): the phase 10 piece proposes p10-8 close (its word, not
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:456]           a public weather report/relay system exists by ruling); the step 5 piece finds step 5's
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:528]           ); requested or research (ar-1 to ar-3, ar-5, ar-6, ar-18) a sanction, court or penalty for not going: tbd, not
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:535]           ( ap7 l213), and release from the duty is reserved (af7-3); gate 9 reads a
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:577]           section a lists ten; all three readers recorded all ten. dr-78 sits inside the brief's
  [Amendment_Rederivation_ST7_QAGates_2026-11-04.md:597]           c's new highest-importance flag; c's reading of ruling c as a tier matter; c's free hours and dress; a's gate 4

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```
**Triage by hand (each of the 49 misses read and classified):** 97 fragments tested, **49 not found** (16 in table cells, 33 in prose). **All 49 are connective prose** captured between two adjacent quotations (the audit's own warning), or this piece's own wording on lines that also carry short quotations: the item lists of sections 1 and 3, the register table's verdict cells, the findings' notes, the cross-reference note and the snags. **None of them is a quotation; no misquotation was found by the audit.** Before the final run, three phrases of the merge's own wording that stood in quotation marks were set in italics (a docket cell, AQ-119's proposed line, and the spine's *can always be reached by signal*, which no pass file carries in that exact form), and one reader's phrase attributed to the wrong reader was reworded. **A supplementary check** of every double-quoted string in the piece of any length (a scratch script, `amend_ST7_merge/shortq.py`, normalizing dashes, quotes, markup, case and spaces) tested 240 strings against the Mirny folder's files, the rulings log, `04`, the stereotypes law and the brief: 236 found; the 4 not found ("CHANGES; MUST BE RE-RUN", "speech leaves the list", "answered in substance", "the harbor call ... essential") are quotations of the readers' own Round 1 or Round 3 text, and with the reader files added to the corpus only the ellipsis-split "the harbor call ... essential" remains, whose two parts are exact text of reader B's AS7-15.

## Merge checks
raw output (full; scripts in the session scratchpad `amend_ST7_merge/`, run with `python3 -I` on the piece; the location-name scan's positive control on a scratch text with three planted names found all three, names not reproduced here):
```
$ python3 -I mixcheck.py <piece>
BLOCK L169 "## 3 · Findings Step 7 missed": old=['fourteen', 'eleven of fourteen'] live=['446,228']
BLOCK L473 "### 5.1 · Gate by gate": old=['fourteen'] live=['36 stocks', '33 of 36']
line-level mixes: 0

$ python3 -I citycheck.py <piece>
== piece_for_checks.md: names scanned 133; hits 0

$ python3 -I idcheck.py <piece>
AS7 cited  : 1..49 (49 distinct)
AS7 headed : 1..49 (49 distinct)
AS7 in mapping table (bold): 1..49 (49 distinct)
cited but not headed: [] | cited but not in mapping: []
RF-ST7: cited 1..11 (11 distinct); defined 1..11 (11 distinct); cited not defined: []
AR(>=120): cited 120..127 (8 distinct); defined 120..127 (8 distinct); cited not defined: []
AQ(>=110): cited 110..121 (12 distinct); defined 110..121 (12 distinct); cited not defined: []
D7: cited 1..4 (4 distinct); defined 1..4 (4 distinct); cited not defined: []
DEC new in this piece: [60]

$ python3 -I keepcheck.py <piece>
L43: ... · P** (run 1 —; M1 W; "how anyone becomes a keeper" W; the child W · P; the native W; departure...
L158: ... Step 7's nearest: L73 "how anyone becomes a keeper" | — | REWORD | **Step 8's, not checked here...
L173: ...e debt clause Step 5 registers (`05` L106); "keepers" is coinage and the debt to the first genera...
L186: ...tside the sanction check (`DR-80`); **(e)** "Keepers" is the pass author's coinage; it is not use...
L262: ...se Step 5 registers, `05` L106) is re-read: "keepers" is coinage and the debt to the first genera...
L320: ...tive who never learns; "how anyone becomes a keeper"; whether blame lasts a life; the road arriv...
L321: ...ot a category of native; (iii) **there is no keeper entry:** "keepers" is coinage; the duty is n...
L321: ...native; (iii) **there is no keeper entry:** "keepers" is coinage; the duty is not a membership an...
L403: ...blamed door, the book that never learns, the keepers invisible while they succeed" (`05` L92)....
L413: ... general answer; the old narrow-role error, "keepers" as the Social Contract's conscious holders,...
L417: ...owledge; unruled for the found record); "the keepers invisible while they succeed" ("keepers" is ...
L417: ..."the keepers invisible while they succeed" ("keepers" is coinage; "thanked never" is dropped; the...
L444: ...| E10 | "Keepers" is the pass author's coinage: no position i...
L444: ... author's coinage: no position is cast as "a keeper" and no organization is called by that word;...
L461: ...t, one relay carrying contact and warnings; "keepers" not used). Consistent....
L478: ...covered; "teach" and "weather report" rise, "keeper" falls; the two holes stay | the extended te...
L480: ...-P7` L50, L51); the withdrawn-phrase scans (*keeper*, *whoever is there*, *nearest*, *re-learn*,...
L511: ... waits on AR-16; Gate 8's standout pending; "keeper" is never a cast position; PF-1, PF-4/RC-1, ...
L596: ... name for the organization or the protocol; "keepers" for any group; "the protocol is a second ex...
piece_for_checks.md: occurrences of keeper/keepers: 19
```
**Reading the checks:** the mixing check's two block-level co-occurrences are separate list items (section 3: list C quotes "eleven of fourteen"; list T gives the live baseline denominator) and separate docket rows (section 5.1: Gate 3's scan pattern *fourteen stocks*; Gate 7's live stock line); no line, row or finding carries both sets. The keeper-word lines are Step 7's or Step 5's own quoted words, statements that the word is coinage, scan patterns, and the killed-drafts list; no group is named by it and no replacement is coined.

## American English sweep
raw output (full; script `amend_ST7_merge/ae_sweep.py` in the session scratchpad, run with `python3 -I` on both files; its positive control on a scratch text with twelve planted British spellings and one 'judgement' found all thirteen; the kept-spelling count in this record comes only from this paragraph and the output lines below):
```
== Amendment_Rederivation_ST7_QAGates_2026-11-04.md (601 lines)
British-spelling hits: 0
'judgement' (kept spelling): 0
== Amendment_Rederivation_ST7_QAGates_2026-11-04b_T8_Rounds.md (503 lines)
British-spelling hits: 0
'judgement' (kept spelling): 3
```
