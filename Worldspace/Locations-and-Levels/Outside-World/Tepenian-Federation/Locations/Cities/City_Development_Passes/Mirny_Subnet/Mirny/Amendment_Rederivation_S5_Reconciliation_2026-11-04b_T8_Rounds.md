# Mirny · Amendment re-derivation · Piece S5 (Step 5, Reconciliation and the CLOSE pass) · T8 round record · 2026-11-04

**Companion to** `Amendment_Rederivation_S5_Reconciliation_2026-11-04.md`. Raw tool output is pasted, not summarized. Working files are in this folder as `.t8_amend_S5_*`.

## Setup
- **Reading list (trimmed, `DR-74`):** `.t8_required_amend_S5.txt` (scratchpad copy `amend_S5/t8_required_amend_S5.txt`), **39 entries, about 6,888 admitted lines**: the rules (entries 1 to 9: the stereotypes law; the runbook's Step 5 spans; `02` §5.3; `04` Gate 6 note; `05` §6.1 to §6.3; the run-modes rule; the phase spine's close-pass docket and Phase 10 B2/B3; `01` §5.2; the rulings log at 24 headings); the discipline files and robot canon (10 to 20); the live sources at Mirny's rows only (21 to 26); **Step 5 read whole** (27, 840 lines); **the live Mirny culture file read whole** (28, 303 lines); the Frame's spans (29); the amendment layer (30 to 39: the Phase 6, 7, 2, 9 and 8 pieces, the Phase 8 dockets, the Idelsk-Uralia piece, the robot-term piece's first 30 lines, the amendment register, the reconciliation note's lines 1 to 120). The robot-culture sheet and the personality read (entries 47 and 48 of Step 5's original list) were not on it; **the Phase 10 piece (unit U5) was not an input** (concurrent).
- **Brief:** `.t8_amend_S5_brief.md`, identical for A/B/C with `{X}` the reader letter; **sha256[:16] 27ece190b40645f1** (computed by this merge on the folder copy and on the scratchpad copy: both match the checkpoint); final at dispatch (`M-93`). It carries ten orchestrator-verified results with sources (its text says "eight"), the developer's binding words, the stage order and twelve traps.
- **Readers:** three Opus agents dispatched about 09:22 on 2026-11-04, inside the 05:00 to 14:59 window (checkpoint). None refused any entry. Graphify: readers A and B record disregarding the hook notices under `DR-6`; reader C records that no notice arrived.

| Reader | Agent ID | Output lines | Bytes | PROOF blocks | Findings (Round 1 numbering) | Docket rows | Requests · questions · RFs |
|---|---|--:|--:|--:|---|---|---|
| A | `a0985bfc4b09cc402` | 1,282 | 166,429 | 39 | A5-1 to A5-27 | S5D-1 to S5D-22, a pass-side row, a D-16 status row | AR-80 to AR-85 · AQ-70 to AQ-77 · RF-S5-1 to RF-S5-4 |
| B | `a993ca9626faa54ac` | 1,481 | 165,453 | 39 | A5-1 to A5-29 | DC-1 to DC-20; D5-1 to D5-7 | AR-80 to AR-85 · AQ-70 to AQ-74 · RF-S5-1 to RF-S5-3 |
| C | `a8c00a9c44c708e52` | 1,481 | 172,130 | 39 | A5-1 to A5-30 | D-1 to D-23 re-disposed; D-24 to D-37 | AR-80 to AR-89 · AQ-70 to AQ-78 · RF-S5-1 to RF-S5-5 |

Line and byte counts by `wc` on the folder copies; PROOF blocks counted by `grep -c '^### PROOF:'` (39 each). Tool-use counts are not recorded in the checkpoint and are not given here.
- **Self-checks before handback (as each reader records):** A ran a read-only check of its PROOF fields and quotations (its Round 3 reply: the other 38 blocks pass; 523 Step 5 and 25 culture-file quotations pass; its entry-5 LLAST was wrong, see Round 2). B corrected its own output in place with a short inline script (no helper file) and then confirmed 39 of 39 blocks and 750 of 750 body quotations (its SN-18). C typed every PROOF field by hand, found two hand-copy errors with a read-only comparison and re-typed them, and confirmed its Step 5 and culture-file table quotations (its snag 14).
- **Ruling-log freeze (`M-302`):** not checked by this merge writer.

## Round 1 headline claims (union, before Round 3)
| Claim | A | B | C |
|---|---|---|---|
| Register L130: the strongest finding is RE-DERIVE as a whole, not only leg 4 | yes | yes | yes |
| Leg 4 splits three ways (call reversed; after-loss rite still absent; record split) | yes | yes | yes |
| A ruled leg enters | yes (4′) | yes (leg 5) | folded into the mechanism |
| "assigned" in the finding's core | yes | yes | **no** (PA-7, unratified) |
| "the warnings go dark exactly when they are needed" | in the core | in the core, tagged [CORR, conditional] | a conditional sharpening, outside |
| Rule-4 flags | single path | single path; the relay's undated start | single path; "assigned" |
| BT-1, BT-5, BT-8 RE-DERIVE (register's REWORD understated) | yes | yes | yes |
| BT-1's scale | 1 | 1 | 4 ("told, not narrated") |
| Register L132's block KEEP | too broad | wrong as a block | overstated; per row |
| C-1 | REWORD (heading said "re-derived") | RE-DERIVE | REWORD |
| D-3 | CLOSE in substance | RE-DERIVE (residue DC-4) | executed; residue D-33, D-34 |
| D-12 | REWORD | RE-DERIVE | RE-DERIVE |
| Q-100 | REWORD | KEEP open, gloss reworded | KEEP open |
| P10-8 (L632, H-18) | withdrawn | withdrawn | pending U5 |
| Language | English alone on mid-points | English alone on mid-points; near-end reading reserved, AR-83 | English alone on mid-points |
| Culture file: wind account | silent (PASS-ONLY) | silent (PASS-ONLY) | silent (PASS-ONLY) |
| Docket scheme | S5D-n replacing D-n | DC-n plus D5-n | D-1 to D-23 kept; new from D-24 |

## Round 2 (`Tools/triple_read_verify.py`) · run 2026-11-04 about 09:5x · NOT UNANIMOUS on one field (116 of 117 field sets)
raw output (full; file `.t8_amend_S5_round2_raw.txt`):
```
required files: 39
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 309-372,378-426,430-540,2090-2316,2724-2883] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/02_Generators_Capability_and_Symbols.md  [range 600-633] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/04_QA_Gates_and_Differentiation.md  [range 154-206] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/05_The_Input_Contract.md  [range 468-742] ===
  agent1   ⛔ LLAST MISMATCH  claimed='pre-contamination review has already recorded exactly that d'  actual=''
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Run_Modes_Warm_and_Cold.md  [range 64-96] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 232-270,1098-1184] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/01_Frame_Typology_and_Inheritance.md  [range 423-448] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 203-251,422-435,448-461,463-475,510-524,538-553,609-621,953-965,1075-1088,1092-1107,1111-1133,1137-1156,1211-1226,1404-1412,1427-1434,1438-1445,1460-1468,1472-1479,1523-1530,1550-1557,1570-1577,1655-1662,1664-1671,1707-1715] ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/05_Reconciliation.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Local_Cultures/Mirny_Subnet/Mirny.md ===
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
⛔ NOT UNANIMOUS - DO NOT WRITE. Log which agent/file failed and why.
```

**The one mismatch, explained.** agent1 is reader A. Its PROOF block for `05_The_Input_Contract.md` (admitted range 468 to 742) gave as LLAST the text of **L741**; the range's last line, **L742, is blank**, and the field is positional ("including if blank"). Reader B's blank LLAST is right, and so is reader C's. Reader A found and admitted the slip in its Round 3 reply (self-correction 1: "Physical L742 is blank; the text I copied … is L741. **B's blank LLAST is right.**"). It is a **last-line field slip, not a content error**: the other fields of that block and the other 38 blocks of all three readers match ground truth. **The Round 1 outputs are final and were not edited** (the tool's verdict line is logged as it stands), and Round 3 proceeded on the orchestrator's decision (checkpoint). The merge takes no content from the faulty field.

## Round 3 (SendMessage to the same three agents) · 2026-11-04 about 10:00 · cross-check done
Each reader was sent nine points the three appeared to share (K1 to K9), a request to map the other two readers' findings onto the old Step 5 IDs and list every category or central-claim split, a request to check the single-finder finds against the pass lines, and a request to list any claim in the other two re-derivations it would not accept. Replies are saved as `.t8_amend_S5_round3_reader{A,B,C}.md`. **The text of K1 to K9 as sent is not in the folder; the topics below are read from the replies**, and where no reply restates a topic it is marked so.

| Reader | Part 1 OBJECTs | Part 2 splits listed | Single-finder finds checked | Part 3 claims not accepted | Coverage |
|---|---|---|---|---|---|
| A | 1 (K3, in part) | 29 (concedes on 11: splits 1, 2, 4, 10, 14, 19, 20, 22 in part, 23, 24, 27) | C's 10 (9 CONFIRM, 1 OBJECT in form); B's 6 (5 CONFIRM, 1 OBJECT); its own 2 | 4 | read B's and C's parts in full; five self-corrections listed |
| B | 1 (K3) | 23 (concedes on 8: BT-11, BT-14, C-1, C-6, D-1, D-4, D-13, D-16; and K9) | C's 7 (6 CONFIRM, 1 OBJECT); A's 3 (1 CONFIRM, 2 OBJECT) | 4, plus one internal-consistency note on A | **partial:** A's register, culture, missed-findings and re-derivation parts; C's register and re-derivation parts ("I ran out of room this turn") |
| C | 1 (K3) | 20 (its tally: four settled by its own concession, one by self-correction) | 11 (9 CONFIRM, 1 CONFIRM with a caution, 1 recorded as a process note) | 6, plus one caution | read A's and B's parts in full |

### The shared points
| K | Topic (as read from the replies) | A | B | C |
|---|---|---|---|---|
| K1 | the strongest finding (register L130): RE-DERIVE, leg 4 split | AGREE | AGREE | AGREE; accepts A's and B's ruled-leg framing over its own |
| K2 | not restated in any reply | AGREE | AGREE | AGREE |
| K3 | the list of C and D rows that change | **OBJECT (in part):** add D-2 (REWORD) and C-2 (REWORD, conceded to C); D-3 is CLOSE, not "changes" | **OBJECT:** D-2 also changes (REWORD); D-13 changes only in its datasheet half; A's D-13 ground is misplaced | **OBJECT:** add D-2 (REWORD) and D-4 (REWORD); D-13 changes only in status (KEEP); C-2 KEEP with a stage-order note |
| K4 | not restated in any reply | (no line; its tally counts nine points, one OBJECT, eight AGREE) | AGREE | AGREE |
| K5 | R-77 and Q-100 | AGREE on R-77 REWORD; Q-100 **KEEP open**, both halves (withdraws its Round 1 REWORD) | AGREE; Q-100 KEEP open, gloss reworded to "moves A6-9's after-loss null" | AGREE; Q-100 KEEP open, gloss reworded (B's wording) |
| K6 | the culture file's remaining disagreements | AGREE; adds `LC:75` against `LC:77` and 23.24 %, the name residues, `LC:122`, `LC:249` to `LC:251`, `LC:243` | AGREE; adds the name residues to `LC:301`, `LC:122`, `LC:190`, `LC:47`, `LC:107` and `LC:243` | AGREE; adds `LC:47`, the name residues, `LC:122`, `LC:190`, `LC:249` to `LC:251`, `LC:243`, `LC:107`; `LC:77`, `LC:178` consistent with `DR-99`; only `LC:41`, `LC:303`, `LC:1` omit it |
| K7 | symbols: facts only | AGREE | AGREE | AGREE |
| K8 | language on mid-points; tiers as shares of workforce units | AGREE | AGREE | AGREE; adds that Step 5's "nine members" stands and A's request rightly asks whether it is the same nine |
| K9 | the Phase 10 dependents: pending Phase 10 | AGREE (its self-correction 3) | AGREE; concedes its "withdrawn" for L632 and H-18; P7-15's half is stale now | AGREE; L632's and L73's sentence is stale by ruling whatever Phase 10 does; P10-8's own disposition pending |

### The splits, and how they were settled in the merge (most conservative reading; split named in the piece)
| Point | Positions | Settlement |
|---|---|---|
| **Reach of the strongest-finding re-derivation** | all: the whole finding | **RE-DERIVE as a whole finding**; leg 4 splits three ways; a ruled leg enters (A5-1) |
| **"assigned" in the core** | R1: A, B in; C out. R3: A, B adopt C's removal; C concedes to keep it via the accepted Phase 2 axis | **Out of the core** (it rests on PA-7, unratified, `FRM` L463); kept in the Composition cell, tagged [DRAFT] |
| **"the warnings go dark exactly when they are needed"** | R1: A, B in the finding (B tagged); C a conditional sharpening. R3: A, B hold C; C holds B's tagged form | **A conditional sharpening [CORR, conditional], outside the core** (the relay's technology; AR-81) |
| **Rule-4 flags** | A single path; B single path + undated start; C single path + "assigned" | **the single path and the relay's undated start (PA-10)** (B; C withdrew its "assigned" flag) |
| **BT-1's scale** | A, B scale 1; C scale 4 | **scale 1 primary** (public competence; a private call and a personal guilt); C's scale 4 "told, not narrated" kept as a second reading placed at LC-52 (`LC:150`); "nothing is left to narrate" not written |
| **BT-4** | A, B KEEP; C one-clause reword; B in R3 held C's reword | **KEEP**, with C's reword offered as an optional note |
| **BT-10** | A REWORD; B, C RE-DERIVE | **RE-DERIVE** (A conceded): the property "authored by no one who lives there" splits into found and made |
| **BT-11** | A REWORD; B RE-DERIVE; C KEEP reworded | **REWORD** (only the weather-hazard clause; the claims half stands by `DR-79`) |
| **BT-13** | R1: A, B REWORD; C KEEP. R3: C conceded REWORD; B held KEEP with refreshed anchors | **REWORD** (the claim stands; census anchors L476 → L488 and L590 → L629 refreshed) |
| **BT-14** | A, C REWORD; B KEEP with the property reworded | **REWORD** (same text; the conservative class) |
| **C-1** | A, C REWORD; B RE-DERIVE | **REWORD** (B conceded) |
| **C-2** | R1: A, B KEEP; C REWORD. R3: A, B REWORD; C KEEP with a note | **REWORD the third order** ("it moves the observance" becomes the candidates held for the post-CST stage); the physics claim stays; split named |
| **C-3** | A, C REWORD; B KEEP plus one reword | **REWORD** |
| **C-6 and D-16** | A, C REWORD as a status line; B KEEP as a record | **REWORD as a status line only** (B conceded) |
| **D-1** | A, C REWORD; B RE-DERIVE | **REWORD**, largely executed (B conceded) |
| **D-2** | A, B REWORD; C KEEP in R1 | **REWORD**, partly executed (all, after K3) |
| **D-3** | A CLOSE; B REWORD (residue DC-4); C REWORD in R1, A's CLOSE in R3 | **CLOSE in substance plus new residue rows D-33, D-34**; split named (B: REWORD) |
| **D-4** | R1: A, C KEEP; B REWORD. R3: C REWORD; B conceded KEEP | **REWORD** (the stage order holds the observances until after the CST) |
| **D-7** | A, B REWORD; C RE-DERIVE | **REWORD** (C conceded) |
| **D-12** | A REWORD; B, C RE-DERIVE | **RE-DERIVE** (A conceded): the direction reverses |
| **D-13** | R1: A, C REWORD; B KEEP. R3: B REWORD for the datasheet half; C KEEP with a status note | **KEEP with a status note**; A's "superseded tier figure" ground rejected |
| **Q-100** | A REWORD; B, C KEEP open | **KEEP open**, gloss reworded (A conceded) |
| **Q-106** | A CLOSE; B withdrawn as asked plus a successor question; C CLOSE in substance | **CLOSE in its old form**; B's successor question optional (AQ-80) |
| **The Scorpio seed** | A re-pointed (R1), RE-DERIVE (R3); B REWORD; C RE-DERIVE | **REWORD** (re-pointed; nothing adopted); A and C's RE-DERIVE named |
| **P10-6 and P10-8** | A, B decided ("withdrawn"; "unmet"); C pending | **pending Phase 10**; Step 5's L632 and L73 sentences stale by ruling; the rulings' direction recorded; nothing written as "withdrawn" |
| **Byproduct 4** | A, B REWORD; C withdrawn | **REWORD** (the moment at the door still cannot be handed over) |
| **Null L746** | A "no longer holds"; B closed in part; C closed | **closed in part** (the file names the establishing country, not `DR-99`'s widening) |
| **The near-end language reading** | A, C mid-points only; B a reserved near-end reading and a request | **mid-points** (`DR-100` L1669); the arithmetic rides as a note under DEC-011 and RF-S5-4; B's request not carried |
| **LC-43 (`LC:122`)** | A CULTURE-ONLY with a flag; B, C CONTRADICTION open | **CONTRADICTION open** (A conceded) |
| **LC-52 (`LC:150`)** | A MATCH; B, C BOTH-TRUE (scale 4) | **BOTH-TRUE** (A conceded) |
| **LC-5 (`LC:12`)** | A, C BOTH-TRUE narrowed; B CULTURE-ONLY | **BOTH-TRUE narrowed** |
| **LC-62 (`LC:190`)** | A, B CULTURE-ONLY with a docket note; C CONTRADICTION open | **CULTURE-ONLY plus a docket row** (D-31) |
| **LC-72 weighting (`LC:235`)** | A BOTH-TRUE re-derived; B MATCH; C BT-7 re-derived | **MATCH in direction (tier 3) plus PASS-ONLY on the warnings riding the relay** |
| **LC-75 (`LC:243`)** | A CULTURE-ONLY; B CONTRADICTION open on light, stale on languages; C CULTURE-ONLY | **CONTRADICTION open on "two seasons of light"; CULTURE-ONLY on "two languages"** |
| **`LC:122`'s retained cross-city sentence** | A no row; B mark as history; C strike (self-corrected in R3) | **mark as history, not strike** |
| **`LC:75`** | A a disagreement with the 23.24 % share; B, C an internal strain | **BOTH-TRUE re-scoped, an internal strain of the file** (D-35) |
| **Numbering** | three colliding A5-n sets | **A5-1 to A5-29 in Step 5's order** (A's proposal, close to C's order), with the nine members at A5-29 (C) |
| **Docket scheme** | A S5D-n; B DC-n and D5-n; C keeps D-1 to D-23, new from D-24 | **C's scheme**, with A's mapping of its S5D-n; A's S5D-2 → D-38; B's DC-17 → D-39; B's DC-18 under D-1; B's D5-n merged with C's stale-line list and A's records list (D5-1 to D5-12) |
| **Reserved findings** | three colliding RF-S5-n sets | **B's proposed merge** (RF-S5-1 to RF-S5-4) plus A's RF-S5-5 |

### Single-finder finds, checked against the pass lines in Round 3
| Find | Finder | Checked by | In the merge |
|---|---|---|---|
| "assigned" rests on PA-7, unratified | C | A, B CONFIRM | A5-1 |
| L96's "every later phase independently re-derives it" fails | C | A, B CONFIRM | A5-1; D5-2 |
| L307 "gone by about 2614" against `FRM` "elderly or already dead" | C | A CONFIRM | A5-4; D5-3 |
| H-12's "none withdrawn" no longer holds (CAND-L2 falls) | C | A CONFIRM | A5-22; D5-4 |
| `LC:287`'s "shift to" presupposes an earlier majority | C | A CONFIRM (low) | D-33 |
| `LC:220`'s implicit comparison; `LC:261`'s founding-language clause | C | A CONFIRM | section 3; D-2, D-27 |
| What carries warnings when the relay is down | C | A CONFIRM | AR-81 |
| `DR-59` Q-68 bears on no Step 5 line directly | C | A CONFIRM (B's pairing with CAND-9 loose) | section 4, list N |
| BT-4's one-clause reword | C | B CONFIRM | A5-6 (optional note) |
| C-2's third order against the stage order | C | A, B CONFIRM | A5-18 |
| BT-10 gives Phase 10's landmark clause a second strain | C | B CONFIRM (pending Phase 10) | A5-12 |
| `LC:3` measures the composition against the station's operator | B | A, C CONFIRM (low) | D-39 |
| Near-end arithmetic (Korean and Mandarin inside 12; Indonesian outside) | B | A, C CONFIRM the arithmetic | A5-26 note; RF-S5-4 |
| A stale-statement docket for Step 5's own lines | B | A CONFIRM | D5-1 to D5-12 |
| The Idelsk-Uralia piece's sponsor-line list misses lines | B | A CONFIRM | section 4, list I; section 6.3 |
| Rule-4 flag (ii): the relay's undated start | B | C CONFIRM | A5-1 |
| `NOTE` L26 lists `LC:61` as changed though it still carries the model | B | C CONFIRM | snag 9 |
| The Phase 9 piece's section 2 IDs differ from its section 3 headings | B | C CONFIRM | snag 5 (cite by heading) |
| Step 5's "nine members" predates a member added 2026-10-21 | A | C CONFIRM as a request | A5-29; AR-82 |
| The founding stratum is legible through the Register, not the census | A | C CONFIRM (reserved) | RF-S5-5 |
| The word guard on *medium* extended to the made protocol | A | B, C CONFIRM (provisional) | A5-27 |
| §6.4's shape re-housed in curation | A | B OBJECT; C CONFIRM with a caution ([D] tag only) | not carried (A5-15) |
| `LC:75` as a disagreement with the sources | A | B OBJECT in part; C OBJECT | BOTH-TRUE re-scoped (D-35) |
| B read the culture file in list order, before entries 29 to 39 | B (disclosed, SN-3) | C recorded as a process note | snag 3 |

### Claims not accepted (not carried into the merge)
| Claim | Whose | Objected to by | Why | In the merge |
|---|---|---|---|---|
| BT-1's property: "Mirny holds its shared media to the standard of not failing" | B | A, C | revives the retired first half of the Phase 6 axis, replaced by `DR-77` | dropped |
| BT-1's third order: "No one dispatches, so no one is placed to release a person" as a body order | B | C | the Phase 7 piece carries it soft and reserved | reserved [D, soft → AF7-4], not a body order |
| BT-1's scale 4 with "and nothing is left to narrate" | C | A | asserts no narrative speech exists; what is said after an injury is unruled (R-67, AR-15) | dropped; "told, not narrated" kept at LC-52 |
| D-13 "its mandated figure superseded in proposal" | A | B, C | D-13 (L366) states no tier figure; the 23.6 % is NI-1's (L335) | ground rejected; D-13 KEEP with a status note |
| `LC:75` read as a share against a head count | A | C (B in part) | the founding-era size is unread; 23.24 % is a long-run share | an internal strain of the file (D-35) |
| `LC:122` docket text "the exile groups' carried repertoires (Russia and Idelsk-Uralia stocks among others)" | A | C | reads a stock's culture from its name (R-96); a CST matter | the whole line held for the CST (D-30) |
| §6.4's shape re-housed "inside the knowledge system's ordinary keeping" | A | B | uses excluded vignette-grounded material as a prompt (rule 3a) | not carried; at most a [D] tag on AF8-3's reserved reading |
| D-30 "strike" the retained sentence at `LC:122` | C | A (C self-corrected) | the line already marks it as history | mark, not strike |
| DC-2's scope including `LC:77` | B | C | `LC:77` is consistent with `DR-99` in substance | D-25 names `LC:41`, `LC:303`, `LC:1` |
| AR-83, a request to choose mid-points or near ends | B | A | `DR-100` L1669 already fixes mid-points | a note under DEC-011 and RF-S5-4 |
| "withdrawn" for P10-8 (and "still unmet" for P10-6) | A, B | C (K9; A and B conceded) | the Phase 10 piece was concurrent | pending Phase 10; the rulings' direction recorded |
| "Q-85 CLOSE (P9 AQ-58)" | C | B | the Phase 9 piece's AQ-58 is a PROPOSED recommendation | CLOSE-proposed only; Q-81 closed by `DR-56` item 5 |
| C-1 REWORD in A's register table but "re-derived" in its finding heading | A | B | one category must be chosen | REWORD |
| `DR-59` Q-68 paired with CAND-9 | B | A | CAND-9 is about publicness (Q-67), not tier | Q-68 bears on no Step 5 line directly |
| Quotations carrying the coast's name | B | C (a caution, not an objection) | the coast's name is Mirny's own geography, but non-name substrings are preferred | the merge quotes non-name substrings |

## Settled in the merge (beyond the splits)
- **Union applied:** A (the item list, the docket and its mapping, the records list, the nine-members request, RF-S5-5, the word guard, the §11 re-ranking, the general-population re-run); B (the leg 5 framing, the rule-4 second flag, the D5-n stale-line docket, the near-end arithmetic as a note, DC-17, the PIU line list, SN-8, the Phase 9 numbering snag, Q-100's gloss, Q-101's and R-135's rewording, byproduct 4 kept); C (the "assigned" and "go dark" precision, L96 and L307, H-12, the docket scheme D-24 onward, `LC:287`, `LC:220`, `LC:261`, AR-81, C-2's stage-order point, BT-4's note, the Scorpio and Aquarius rows, the Phase 10 second strain, the §6.4 conclusion).
- **The Phase 10 piece** appeared in the folder (PROPOSED) while the merge was being written. It was read for cross-reference only (its header, section 0, its Step 5 feed row, its decisions paragraph) and nothing in this piece was changed by it; its proposals (P10-6 RE-DERIVE; P10-8 CLOSE; B3 a status correction under its DEC-015) are recorded in a note at the end of the piece's section 5. Because its DEC-015 asks the same symbol question for Phase 10, **no separate decision is raised here; the symbol record rides with DEC-015**.
- **Figures:** all three readers agree on the live set (1,403,549; 50.63 %; 36 stocks; 13.73 %; 23.24 %; the PROPOSED tiers 42.2 / 23.1 / 34.7 %; English on mid-points). Old figures appear only on "Old" lines.
- **Shares are weights, never head counts or hours** (`DR-12`).

## Kept files (`M-132`)
The Round 1 outputs `.t8_amend_S5_readerA.md`, `.t8_amend_S5_readerB.md`, `.t8_amend_S5_readerC.md` and the Round 3 replies `.t8_amend_S5_round3_readerA.md`, `.t8_amend_S5_round3_readerB.md`, `.t8_amend_S5_round3_readerC.md` are kept in this folder as the round's working record, unedited, beside `.t8_amend_S5_round2_raw.txt`, the frozen brief `.t8_amend_S5_brief.md` and the checkpoint `.t8_amend_S5_CHECKPOINT.md`. They are not inputs to any later step; this record and the piece are the merged result. No helper file was created in the repo by the readers or by this merge (scratch work stayed in the session's scratchpad).

## Quotation audit (`Tools/quotation_audit.py`, `--files Amendment_Rederivation_S5_Reconciliation_2026-11-04.md --own-pass`) · 2026-11-04
raw output, excerpted (1 line omitted: the positive control "HARD - case mismatch", whose test phrase names another location; it reported FOUND, and the instrument line below reads VALID; file `amend_S5/qaudit_final.txt` in the session scratchpad holds the whole output):
```
pass audited : Mirny
corpus mode  : default (own pass excluded)
corpus files : 6089   chars: 69,782,249
files audited: Amendment_Rederivation_S5_Reconciliation_2026-11-04.md
own-pass mode: a quotation may also be found in this pass's OTHER files (never in its own file)

=== POSITIVE CONTROLS ===
  [easy                      ] FOUND     a terminus is nobody's midpoint
  [HARD - blockquote wrap    ] FOUND     A pass may not proceed to Step 5 with a NEVER CITED row
  [HARD - outside Worldspace ] FOUND     Paste raw QA scan output into the QA block. Never summa
  [HARD - long wrapped       ] FOUND     Different content is not differentiation; a different q

  INSTRUMENT VALID: YES
  NEGATIVE CONTROL (must be absent): PASS - absent

=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 132
NOT FOUND in corpus: 43
  of those, in TABLE CELLS : 5
  of those, in PROSE       : 38

  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:17]           is still an absence on every admitted line (r-77's after-loss half stays open, a6-9), now an empty slot, not a refusal
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:18]           is not in the core (it rests on pa-7, unratified, frm l463) and stays in the composition cell, tagged draft
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:20]           that are five primary stocks ( lc:204 ); the language slot ( lc:105 against dr-100 ); the retracted light model ( lc:61 and nine o
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:20]           ( lc:235 , lc:279 ); name and station read as meaning ( lc:43 , lc:45 , lc:79 , lc:97 , lc:220 ); an
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:23]           are stale by ruling (a public warning exists and rides the relay; p7-15 is itself re-derived, a7-2). p10-8's own disposition and p
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:41]  [CELL]  legs 2 and 3 (l101, l102) - (leg 3 sharper by dr-76 ) leg 4 l103 w rule-4 check l105 w qualifications (a) l106 w (the
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:110]  [CELL]  c-6 and d-16 are overtaken in the record by dr-57 ; the phase 9 amendments carry
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:116]           ) is accurate and understated ( dr-99 also bears) areg l163 restates piece 1's 7 form, whose ruling is still open ( drl l1444
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:154]  [CELL]  open but still reads the kept name as a statement; lc:45 keeps the namesake symbolism and gives the station's location (not assign
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:154]  [CELL]  and by stock ties; lc:220 keeps a founding legend in the expedition; lc:301 (out of frame) keeps
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:216]           ), mirny supplying its object and its price; guilt is outside the sanction check ( dr-80 ); (e)
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:216]           is the pass author's coinage; it is not used here as any group's name and no replacement is coined; (f) the warnings travel on the
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:219]           (l90); the city holds its shared medium to the standard of not failing
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:222]           is not in the core. assignment rests on pa-7, which the frame cites to the treaty draft
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:222]           ( frm l463). it stays in the composition cell by the accepted phase 2 axis
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:222]           tagged draft . split: in round 3 c conceded to keep
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:232]           clause the duty's object (one relay carrying contact and warnings), pa-74 reworded
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:232]           not used; the debt to the first generation varies person by person. (b) the in-world voice (
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:232]           the blame reflex) withdrawn for mirny's own knowledge (a6-9); for the found record nothing is ruled; the blame reflex is act 1's (
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:244]           ( dr-77 , dr-79 ), with the claims mirny's work owes outward still unarbitrated and the wind's knowledge curated in principle with
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:244]           (accepted with the phase 8 piece; whether it carries a tie to the duty is open); populations
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:244]           (formed half glossed as taught and exposed here; a9 4, proposed); composition
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:251]           holds its shared media to the standard of not failing
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:273]           engineering makes checkable objects and carries standing; the reading makes no object and
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:284]           is coinage: the people who maintain the relay , a role either body may hold. because the warnings ride the relay, its ordinary wor
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:307]           (that phrase survives only inside the bracketed old: record at lc:33 )
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:312]           no longer holds : the social contract now includes telling danger and the instruments exist (a6-10)
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:312]           falls, since the wind's outcomes can be read against what was taught and warned (a7-9). the excluded vignette-derived sources stay
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:324]           ) overturned (its trigger fired in q-44's first half; aiu-3). pa-55 (
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:360]           (via p6-1) taught after the first generation ( changed )
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:361]           ); the registry row was not edited ( drl l1151). the developer's 2026-11-03 stage order then put every symbol determination after 
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:391]           (a majority form of the rule; dr-100 replaced it
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:410]           ), its step 5 feed row and its decisions paragraph were read. nothing above was changed by it; the findings above keep
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:411]           as over-refusing: the personal-name rule bars names, not a role described by function. it lists c3-23 cand
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:476]  [CELL]  either crosses the gap as a tradition ( nns l21) or reads a cuisine from two stocks' names (r-96). the retained cross-city sentenc
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:556]           outside the core (kept in the composition cell, tagged draft ) and
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:556]           as a conditional sharpening; leg 4 split three ways and a ruled leg added recommendation: yes, as worded. if answered differently:
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:556]           belongs in the core, the rule-4 check must flag pa-7 as unratified ground; if
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:580]           and lists ten; all three readers recorded all ten. dr-78 sits in the brief's
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:601]           a name for the curating organization or the protocol
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:601]           for any group; a form for the warnings; a rite of restoration or for the first generation; reading the vigil as a rite of failure
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:602]           a's lc:75 read as share against head count; a's lc:122 replacement text; a's 6.4 re-housing; c's d-30
  [Amendment_Rederivation_S5_Reconciliation_2026-11-04.md:602]           b's dc-2 scope including lc:77 ; b's near-end request; any

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```
**Triage by hand (each of the 43 misses read and classified):** 132 fragments tested, **43 not found** (5 in table cells, 38 in prose). **42 are connective prose** captured between two adjacent quotations (the audit's own warning), or this piece's own wording inside a line that also carries short quotations: the proposal sentences, the docket and killed-draft lists, the decisions and the cross-reference note; none of them is a quotation. **One is a quotation of a reader's Round 1 output, not of the corpus:** L251's "holds its shared media to the standard of not failing" (B's BT-1 property clause, quoted in order to reject it) is exact text of `.t8_amend_S5_readerB.md` L841 (checked with `grep -n`); the audit corpus does not include the dot-files. **No misquotation was found; nothing was changed for the audit.** Before the audit, every Step 5 and culture-file quotation used in the piece was also checked line by line with `grep -F` against its stated line (all found, except one attribution corrected before writing: "a minority of descent" is quoted from L291, not L307).

## American English sweep
raw output (full; script `amend_S5/ae_sweep.py` in the session scratchpad, run with `python3 -I` on both files; its positive control on a scratch text with nine planted British spellings and one 'judgement' found all ten; the kept-spelling count in this record comes only from this paragraph and the two output lines below; zero hits in either file):
```
== Amendment_Rederivation_S5_Reconciliation_2026-11-04.md (606 lines)
British-spelling hits: 0
'judgement' (kept spelling): 0
== Amendment_Rederivation_S5_Reconciliation_2026-11-04b_T8_Rounds.md (452 lines)
British-spelling hits: 0
'judgement' (kept spelling): 3
```
