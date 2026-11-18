# Round record — Relung Panen · ULM Step 5 · reconciliation, in two stages

**Output:** `05_Reconciliation.md` (1,071 lines: Part 1, stage A, L1–623; Part 2, stage B, appended). Each stage: three Opus readers, Round 2, Round 3, one fresh merge writer (`M-246`). Every tool output below is pasted whole. PROPOSED; nothing declared complete. Record written 2026-11-18 07:13.

**The two-stage design and its seal** (runbook L2888, `M-271`; the seal from method note `M-323`): stage A reconciled the pass on its own files and canon and named the strongest finding's falsifiable leg **with no read-last material on any list**; its merge was pre-checked, then **sealed** (sha256 `bb61b688adb7530c18a3c68435362815dfba01b4efd0dfecb0d2e530badeaa12`, byte copy, `cmp`) before any stage B message; the hash was re-checked before stage B's Round 2 and again before the append, and after the append the first 623 lines were byte-identical to the sealed copy. **The leg HOLDS** in all three readers and the merge, by silence (no read-last line fills the absence).

---

## Stage A

**Output:** `05_Reconciliation.md` (1071 lines). Three Opus readers, Round 2, Round 3, one fresh merge writer (`M-246`). Every tool output below is pasted whole. PROPOSED; nothing declared complete. Record written 2026-11-18 07:13. Isolation: the fresh session (run log RL-07, RL-08); fresh readers and clean briefs.

### A · Round 0 — the list and the frozen briefs

27 entries: the runbook's Step 5; the amendment layer's rules; the method sections Step 5 names (the both-are-true test, the circularity and ratification rules, the note under Gate 6, the strongest-finding rule, the close-pass docket); the pass's own files, Step −1 to Phase 10 with the research supplement; the spec at the contract's admitted spans **with its conclusion-shaped lines left out for stage B**; the two symbol files at their method and the ruled members (Earth, Water); the rulings spans through `DR-141`, cutting L1998 and L2003. **No read-last material on the list.** Six results, the last the mechanical sweep (46 lines; HF10-1 to HF10-6). Two-stage design from the runbook (L2888, `M-271`) and the method notes `M-268` and `M-323` (the seal; their other-location content not used, RL-46).

```
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md :: 2760-2896
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Amendment_Layer_Rules.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/02_Generators_Capability_and_Symbols.md :: 610-635
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/05_The_Input_Contract.md :: 468-650,662-744
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/04_QA_Gates_and_Differentiation.md :: 156-213
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/01_Frame_Typology_and_Inheritance.md :: 423-448
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md :: 232-270
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/00.1_Step_MINUS-1_Input_Contract.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/00_Frame.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/01_Inherited.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/02_Spine.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/02.1_Spine_Amendment_G7.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/03_Research.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/03.1_Research_Supplement.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/04_Phase_02_Composition_and_Arrival.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/04_Phase_03_Surface_and_Texture.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/04_Phase_04_Ordinary_Life.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/04_Phase_05_Relation_and_Geometry.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/04_Phase_06_Meaning.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/04_Phase_07_Order.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/04_Phase_08_Making.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/04_Phase_09_Populations.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/04_Phase_10_Catalog.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Relung_Panen.md :: 1-4,6-8,10-13,20-30,33-37,55-92,104-116,120-121,124,135-144,146-149,151-166,171-172,177-207,222-234,254,256-278,310-313,315-321
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Symbolic_Substrate/Planetary_Symbols.md :: 1-17,74-87
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Symbolic_Substrate/Robot_Elementals.md :: 1-20,128-163
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md :: 203-254,331-338,386-421,437-447,510-525,538-554,623-633,678-690,771-797,858-872,1245-1262,1335-1345,1370-1381,1382-1392,1393-1403,1404-1415,1416-1426,1483-1493,1494-1502,1523-1531,1570-1578,1597-1605,1618-1627,1628-1637,1638-1645,1664-1672,1707-1718,1791-1799,1800-1808,1818-1826,1854-1862,1863-1871,1881-1889,1890-1898,1908-1916,1917-1925,1935-1943,1944-1952,1989-1997,1999-2002,2004-2007,2009-2047
```

### A · Round 1 — three readers

Dispatched 05:53: A `a9c110b924fd46f7a`, B `acdb20a7604b9f297`, C `a5ddcc52d2e1eaa14`. Outputs copied in: 735 / 772 / 671 lines. All three named the same strongest finding (energy the one cost the site cannot pay from its own gifts: one bought supply carries the lit food, the warm rooms and the robot half's charge) and the same leg (leg 1, the absence of any energy of the site's own). Reconciliation results 2 / 8 / 3 CANON OUTRANKS. Disclosed: B listed round-record file names with a filename-only `grep -l` and left a private notes file in its staging folder (the hook blocked deletion); C's too-wide `grep` printed one Pre-Trip heading line (L160), unused; C was interrupted and resumed from its log.

### A · Round 2 — `Tools/triple_read_verify.py` (last change 2026-11-03), raw output, whole (`.t8_05_Step_5A_round2_raw.txt`)

```
required files: 27
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2760-2896] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Amendment_Layer_Rules.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/02_Generators_Capability_and_Symbols.md  [range 610-635] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/05_The_Input_Contract.md  [range 468-650,662-744] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/04_QA_Gates_and_Differentiation.md  [range 156-213] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/01_Frame_Typology_and_Inheritance.md  [range 423-448] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 232-270] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/00.1_Step_MINUS-1_Input_Contract.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/00_Frame.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/01_Inherited.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/02_Spine.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/02.1_Spine_Amendment_G7.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/03_Research.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/03.1_Research_Supplement.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/04_Phase_02_Composition_and_Arrival.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/04_Phase_03_Surface_and_Texture.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/04_Phase_04_Ordinary_Life.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/04_Phase_05_Relation_and_Geometry.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/04_Phase_06_Meaning.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/04_Phase_07_Order.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/04_Phase_08_Making.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/04_Phase_09_Populations.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/04_Phase_10_Catalog.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Relung_Panen.md  [range 1-4,6-8,10-13,20-30,33-37,55-92,104-116,120-121,124,135-144,146-149,151-166,171-172,177-207,222-234,254,256-278,310-313,315-321] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Symbolic_Substrate/Planetary_Symbols.md  [range 1-17,74-87] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Symbolic_Substrate/Robot_Elementals.md  [range 1-20,128-163] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 203-254,331-338,386-421,437-447,510-525,538-554,623-633,678-690,771-797,858-872,1245-1262,1335-1345,1370-1381,1382-1392,1393-1403,1404-1415,1416-1426,1483-1493,1494-1502,1523-1531,1570-1578,1597-1605,1618-1627,1628-1637,1638-1645,1664-1672,1707-1718,1791-1799,1800-1808,1818-1826,1854-1862,1863-1871,1881-1889,1890-1898,1908-1916,1917-1925,1935-1943,1944-1952,1989-1997,1999-2002,2004-2007,2009-2047] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

### A · Round 3 — cross-checks, saved as sent back

`.t8_05_Step_5A_round3_readerA.md` and the others: `…readerA.md` (118), `…readerB.md` (169), `…readerC.md` (133); the other two outputs given by path. Each reader was told it could skip the others' PROOF sections, sweep tables, placeholder tables and docket rows and sample the docket. All six verdicts CONSISTENT. **An orchestrator premise error:** the Round 3 messages to A and C said B and C had both flagged Phase 9's "a dish" and "an origin feast" lines; only B had, and C corrected it (its reply L90; run log RL-50). Verdict lines:

```
.t8_05_Step_5A_round3_readerA.md:21: **(4) VERDICT: CONSISTENT.**
.t8_05_Step_5A_round3_readerA.md:39: **(4) VERDICT: CONSISTENT.**
.t8_05_Step_5A_round3_readerB.md:31: **(4) VERDICT: CONSISTENT.**
.t8_05_Step_5A_round3_readerB.md:49: **(4) VERDICT: CONSISTENT.** One shared misreading of the Water negative is noted; it is in a backstop record and not in a finding.
.t8_05_Step_5A_round3_readerC.md:25: **CONSISTENT.** One line slip (L354 for L25), and one tier label I share and correct below.
.t8_05_Step_5A_round3_readerC.md:48: **CONSISTENT.** Two line slips (L441, L438), and a wider use of CANON OUTRANKS that is a method reading, not a misreading of a source.
```

**All six cross-verdicts CONSISTENT.**

### A · The merge

`a72ff44ce9b192b08`, dispatched 06:28, returned `05_Reconciliation.md` Part 1, **623 lines**, ending with its own closing line. Its reply (summarized): strongest finding **S5-80**, energy as the one cost the site cannot pay from its own gifts, its core on legs 1 to 3 and its sharper one-line form held a step below; named leg 1, the absence of any energy of the site's own; 46 sweep rows; 2 Zodiac amendments to Phase 9; 38 reconciliation entries (21 BOTH-TRUE, 2 CANON OUTRANKS on Tier 1 rulings, 6 PASS STANDS, 9 OPEN); 31 amendments from the developer's answers; 50 supplement items; 29 placeholders and 21 conditional entries; 89 docket rows (PC-1 to PC-89); 13 handed forward; REQ-238 to REQ-247; RF-242 to RF-249; DQ-61 to DQ-64. **Pre-checked before the seal** (quotations, spelling; raw outputs below as `…_preseal`), then **sealed 06:43**: sha256 `bb61b688adb7530c18a3c68435362815dfba01b4efd0dfecb0d2e530badeaa12`, byte copy `.t8_05_Step_5A_part1_sealed.md`, `cmp` identical.

### A · Close checks (run before this record existed)

### 1 · Quotation pre-check, preseal, raw output, whole (`.t8_05_Step_5A_quote_precheck_raw_preseal.txt`)

```
target: 05_Reconciliation.md
sources: 33 list entries; own-pass files: 38 (dot-files and superseded files excluded)
quoted fragments (>=3 words, ellipsis-split): 115
found in sources at admitted ranges: 115 | found only in the pass's own files: 0 | NOT FOUND: 0
```

**Triage:** Part 1 alone, with the readers' files as extra sources: 115 of 115 found.

### 3 · American English sweep, preseal, raw output, whole (`.t8_05_Step_5A_ame_sweep_raw_preseal.txt`)

```
  HIT   05_Reconciliation.md:23  emphasis  | Every prior file of this pass (Step −1 to Phase 10, with the research supplement), emphasis markers and backticks stripped, searched for "St
  HIT   05_Reconciliation.md:254  emphasis  | | RS-33 (L215) the glare season starts before the melt; ice the reflector | Phase 3 surface; P8-44; Phase 8 L540; REQ-182 | New conditional 
British-form hits (excluding kept 'judgement'): 2 ; kept 'judgement': 0
```

**Triage:** "emphasis" is American.


---

## Stage B

**Output:** `05_Reconciliation.md` (1071 lines). Three Opus readers, Round 2, Round 3, one fresh merge writer (`M-246`). Every tool output below is pasted whole. PROPOSED; nothing declared complete. Record written 2026-11-18 07:13. Isolation: the fresh session (run log RL-07, RL-08); fresh readers and clean briefs.

### B · Round 0 — the list and the frozen briefs

9 entries: the sealed Part 1; this city's own culture, robot-culture and personality files (`Local_Cultures/`, `Local_Robot_Culture/`, `City_Enneagram_Personalities/`); the four working files in `Cities/Relung_Panen/` (README, Development_Brief, ULM_Input_Status, RESEARCH_TO_DO_LATER: the Pre-Trip's addendum A1); the spec's conclusion-shaped lines (L118, L127, L168, L215–216, L244–248; the contract's RF-10). **The vision notes and the neo-race catalog are excluded** (`DR-10`; the Pre-Trip's §F). The files were sized by `wc -l` while stage A ran and opened by no one before the seal. Five results (the hash; the strongest-finding section at Part 1 L476–494; HF5-1 to HF5-6).

```
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/05_Reconciliation.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Local_Cultures/Mirny_Subnet/Relung_Panen.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Local_Robot_Culture/Mirny_Subnet/Relung_Panen.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Enneagram_Personalities/Mirny_Subnet/Relung_Panen.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Relung_Panen/README.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Relung_Panen/Development_Brief.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Relung_Panen/ULM_Input_Status.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Relung_Panen/RESEARCH_TO_DO_LATER.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Relung_Panen.md :: 118,127,168,215-216,244-248
```

### B · Round 1 — three readers

Sent 06:44 to the same three readers by message (stage B brief per reader). Outputs copied in: 429 / 510 / 358 lines. **The named leg: HOLDS in all three** (A: corroboration by silence). Check rows 109 / 152 / 100; CANON OUTRANKS 0 in all three. **The seal re-checked before Round 2: `sha256sum -c` OK.**

### B · Round 2 — `Tools/triple_read_verify.py` (last change 2026-11-03), raw output, whole (`.t8_05_Step_5B_round2_raw.txt`)

```
required files: 9
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/05_Reconciliation.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Local_Cultures/Mirny_Subnet/Relung_Panen.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Local_Robot_Culture/Mirny_Subnet/Relung_Panen.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Enneagram_Personalities/Mirny_Subnet/Relung_Panen.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Relung_Panen/README.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Relung_Panen/Development_Brief.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Relung_Panen/ULM_Input_Status.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Relung_Panen/RESEARCH_TO_DO_LATER.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Relung_Panen.md  [range 118,127,168,215-216,244-248] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

### B · Round 3 — cross-checks, saved as sent back

`.t8_05_Step_5B_round3_readerA.md` and the others: `…readerA.md` (118), `…readerB.md` (160), `…readerC.md` (124); the other two outputs given by path. Each reader was told it could skip the others' PROOF sections and sample their check rows. All six verdicts CONSISTENT; C noted two of B's placements depart from the brief's definitions, not from a source's text, and adopted A's wording "corroboration by silence". Verdict lines:

```
.t8_05_Step_5B_round3_readerA.md:30: **(4) VERDICT: CONSISTENT.**
.t8_05_Step_5B_round3_readerA.md:46: **(4) VERDICT: CONSISTENT.**
.t8_05_Step_5B_round3_readerB.md:44: **(4) VERDICT: CONSISTENT.**
.t8_05_Step_5B_round3_readerB.md:71: **(4) VERDICT: CONSISTENT.**
.t8_05_Step_5B_round3_readerC.md:42: **CONSISTENT.**
.t8_05_Step_5B_round3_readerC.md:65: **CONSISTENT.** B's two placements depart from the brief's definitions, not from a source's text.
```

**All six cross-verdicts CONSISTENT.**

### B · The merge

`a39ddb6e0b3e8a396`, dispatched 07:00, wrote Part 2 to a separate file, `.t8_05_Step_5B_part2.md` (448 lines), never touching the sealed file. **At 07:12 the orchestrator re-checked the seal (OK), appended Part 2, and compared the head: `head -623 05_Reconciliation.md | cmp - .t8_05_Step_5A_part1_sealed.md`, identical.** The file is now 1,071 lines. Its reply (summarized): the named leg HOLDS, by silence, no split; 160 check rows (S5-81 to S5-240: 69 MATCH, 10 BOTH-TRUE, 37 PASS STANDS, 0 CANON OUTRANKS, 35 CULTURE-ONLY, 9 OUT OF FRAME); 48 docket rows (PC-90 to PC-137); 9 handed forward (HF5-14 to HF5-22); REQ-248 to REQ-255; RF-250 to RF-254; DQ-65 to DQ-67.

### B · Close checks (run before this record existed)

### 1 · Quotation pre-check, raw output, whole (`.t8_05_Step_5B_quote_precheck_raw.txt`)

```
target: 05_Reconciliation.md
sources: 48 list entries; own-pass files: 38 (dot-files and superseded files excluded)
quoted fragments (>=3 words, ellipsis-split): 199
found in sources at admitted ranges: 199 | found only in the pass's own files: 0 | NOT FOUND: 0
```

**Triage:** the whole file, on the union of the two stages' lists, with all six reader outputs and six Round 3 replies as extra sources: 199 of 199 found.

### 2 · Quotation audit, `Tools/quotation_audit.py` (last change 2026-11-02), raw output, whole (`.t8_05_Step_5B_quotation_audit_raw.txt`)

```
pass audited : Relung_Panen
corpus mode  : default (own pass excluded)
corpus files : 7427   chars: 127,934,587
files audited: 05_Reconciliation.md
own-pass mode: a quotation may also be found in this pass's OTHER files (never in its own file)

=== POSITIVE CONTROLS ===
  [easy                      ] FOUND     a terminus is nobody's midpoint
  [HARD - blockquote wrap    ] FOUND     A pass may not proceed to Step 5 with a NEVER CITED row
  [HARD - outside Worldspace ] FOUND     Paste raw QA scan output into the QA block. Never summa
  [HARD - case mismatch      ] FOUND     YOU GO TO ESPERANZA AND YOU DO NOT COME HOME FOR FOUR Y
  [HARD - long wrapped       ] FOUND     Different content is not differentiation; a different q

  INSTRUMENT VALID: YES
  NEGATIVE CONTROL (must be absent): PASS - absent

=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 84
NOT FOUND in corpus: 24
  of those, in TABLE CELLS : 5
  of those, in PROSE       : 19

  [05_Reconciliation.md:102]           against about 430-450 km. both-true. side 1: spec l124. side 2: s3-c4 (research l586). property: a floor and a measure; 430-450 km
  [05_Reconciliation.md:115]           against the grid that reaches the city. both-true. side 1: spec l260-261
  [05_Reconciliation.md:120]           both-true, with a residue put to the developer. side 1: dr-96 item 4 (rulings l1633): canon's model governs
  [05_Reconciliation.md:120]           about 0.5 gw. side 2: dr-141 item 1 (l2044)
  [05_Reconciliation.md:159]           ), now on the ruling; phase 9 p9-28 (l261
  [05_Reconciliation.md:163]           stands for entry; whether the glow is seen from the gulf is not written (req-103). (a amended this line to
  [05_Reconciliation.md:176]           and p10-101 writes no dish. no phase entry writes one. the glitch-coolant axis appears in no entry as a placement; phase 8 dq-52 i
  [05_Reconciliation.md:286]           (l81): finds in part: a kept garden, fragile because contingent
  [05_Reconciliation.md:474]           reads as the band-5 deferral, a ruling's vocabulary, not a generator's; research s3-31's
  [05_Reconciliation.md:474]           is plain english in context (b). the sign names in phase 10 p10-23 to p10-34 head prompts in the technique's own section, not clai
  [05_Reconciliation.md:545]           options: (a) the model stands as a sizing rule: every indoor kilogram counts as lit, the sun through the glass is an unsized summe
  [05_Reconciliation.md:546]           (p9-25, l253) stand under dec-610 and dec-611 options: (a) both stand as unnamed function statements about origin forms kept at ho
  [05_Reconciliation.md:547]           ( dec-602 (d)) mean the ruling was given before the supplement placed the nesting through the southern hills, 25-155 m (rs-16, rs-
  [05_Reconciliation.md:547]           means outside the kept city, wild and unhoused; the nests are in the southern hills; (b)
  [05_Reconciliation.md:628]           end of part 1 (stage a). stage b is appended below this line
  [05_Reconciliation.md:722]  [CELL]  no western european or american presence, and a proximity-ordered tier
  [05_Reconciliation.md:820]  [CELL]  claims none: cross-city rankings culture-only (terminal) pc-128 a, c; b pass stands on the
  [05_Reconciliation.md:852]  [CELL]  itself matches (spec l13, l139-140; p10-45; a). rf-250 a, b, c (a moved from match on
  [05_Reconciliation.md:881]           leg 1, the absence of any energy of the site's own, that the city takes no energy from its own ground, apart from its standby gene
  [05_Reconciliation.md:883]           the lines that touch power all treat it as bought
  [05_Reconciliation.md:948]  [CELL]  claims marked comparisons for the terminal pass. b's wording, that the
  [05_Reconciliation.md:967]  [CELL]  l168 with l171-172 and l215-216 reach the pass's water findings, which the pass reached from admitted figures (spine rf-47). confl
  [05_Reconciliation.md:1040]           to b's and c's pass stands on the causal clause. written: pass stands
  [05_Reconciliation.md:1066]           while its l190-195 diagram sits under the heading

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```

**Triage:** INSTRUMENT VALID: YES. The 24 fragments are reconciliation and check-row text between quoted words (the merge's sides, properties and dispositions), the file's own closing line of Part 1, and table cells quoting reader keys (CONNECTIVE).

### 3 · American English sweep, raw output, whole (`.t8_05_Step_5B_ame_sweep_raw.txt`)

```
  HIT   05_Reconciliation.md:23  emphasis  | Every prior file of this pass (Step −1 to Phase 10, with the research supplement), emphasis markers and backticks stripped, searched for "St
  HIT   05_Reconciliation.md:254  emphasis  | | RS-33 (L215) the glare season starts before the melt; ice the reflector | Phase 3 surface; P8-44; Phase 8 L540; REQ-182 | New conditional 
British-form hits (excluding kept 'judgement'): 2 ; kept 'judgement': 0
```

**Triage:** "emphasis" only (American).

### 4 · Handoff audit, `Tools/handoff_audit.py` (last change 2026-10-21), raw output, whole (`.t8_05_Step_5B_handoff_audit_raw.txt`)

```
pass audited : Relung_Panen
phase files  : 9

=== CONTROLS (edit these per pass; they are what makes a zero trustworthy) ===
  PHASES WITH A FORMAL SWEEP BLOCK (found in this pass): 2, 3, 4, 5, 6, 7, 8, 9, 10
  PHASES WITH NO TRACE OF A SWEEP (found in this pass)  : none
  SELF-TEST (fixed positive and negative strings)       : passed
  INSTRUMENT VALID: YES - the detector separates a formal block from no block on the built-in controls

  phase | outbound | sweep    | rows | verdict
  ------+----------+----------+------+---------
      2 |        0 | FORMAL   |   18 | n/a - nothing addressed to it
      3 |        0 | FORMAL   |   28 | n/a - nothing addressed to it
      4 |        8 | FORMAL   |   69 | reconcile 69 enumerated against 8 outbound
      5 |        9 | FORMAL   |   94 | reconcile 94 enumerated against 9 outbound
      6 |        9 | FORMAL   |   74 | reconcile 74 enumerated against 9 outbound
      7 |       12 | FORMAL   |  165 | reconcile 165 enumerated against 12 outbound
      8 |       10 | FORMAL   |   84 | reconcile 84 enumerated against 10 outbound
      9 |       23 | FORMAL   |  160 | reconcile 160 enumerated against 23 outbound
     10 |       14 | FORMAL   |   74 | reconcile 74 enumerated against 14 outbound

TOTAL outbound handoff rows: 85
PHASES WITH ROWS ADDRESSED TO THEM AND NO ENUMERATION: 0

=== outbound rows, per target, for hand reconciliation ===
  -> Phase 4:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 4** | HF2-1 | Whose ordinary day: 32 stocks with no predominant row, nearly al
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 4** | HF2-2 | The year's structure (`DR-137` item 8): the drains before the me
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 4** | HF2-3 | Small rows' practices kept in households, with compromise | P2-2
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 4** | HF2-4 | Whether the born-here and later residents know their ground was 
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 4** | HF3-1 | The day's sensory structure (`DR-137` item 8): the night quiet o
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 4** | HF3-2 | The year by surface: rock and grit in the frozen months, the mel
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 4** | HF3-3 | The ordinary household's thresholds: heated, possibly dry rooms 
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 4** | HF3-4 | Whether the born-here and later residents know their ground was 
  -> Phase 5:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 5** | HF2-5 | Who the visitor is when nobody passes through: freight crews and
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 5** | HF2-6 | What the one-door reasoning counts (`DEC-587`; Step 1 REQ-38), s
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 5** | HF2-7 | Whether an arrival's first stay holds: housing ready on arrival,
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 5** | HF2-8 | Casey as the arrival end of the spur, and the people door as the
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 5** | HF2-9 | Whether arrival has a season (RF-101) | P2-10 (C) |
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 5** | HF3-5 | First contact by door: overland, the long road's end and a basin
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 5** | HF3-6 | The doors as sounds and seasons: aircraft on lake ice heard acro
       [04_Phase_04_Ordinary_Life.md]  | **Phase 5** | HF4-1 | The newcomer's first stay and first year: where she first lives,
       [04_Phase_04_Ordinary_Life.md]  | **Phase 5** | HF4-2 | The road as the household's door for anything heavy: its rhythm,
  -> Phase 6:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 6** | HF2-10 | The meaning a city may make of a founding few, a road everyone 
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 6** | HF2-11 | The founding text's recoding of a compelled exile as a choice, 
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 6** | HF2-12 | Whether the one-way election is felt here (Step 1 RF-31) | P2-1
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 6** | HF3-7 | What the texture offers meaning: what the stillness keeps; given
       [04_Phase_04_Ordinary_Life.md]  | **Phase 6** | HF4-3 | Meaning: a stop made by hand against the sky; a year set by wate
       [04_Phase_04_Ordinary_Life.md]  | **Phase 6** | HF4-4 | Phase 2 RF-93 (the natives without the road's story), checked ag
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 6** | HF5-1 | Meaning: the city's continuous, physical dependence against the 
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 6** | HF5-2 | Conversion by one lived water year, no ceremony; the outsider de
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 6** | HF5-3 | Whether residents know that their light, their outlet and their 
  -> Phase 7:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 7** | HF2-13 | Who works the research stake and the haul, and whether either, 
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 7** | HF2-14 | Where decisions fall on arrival (outside the city; the treaty's
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 7** | HF3-8 | The set-point institutions as workplaces (growing rooms shedding
       [04_Phase_04_Ordinary_Life.md]  | **Phase 7** | HF4-5 | Who pays and who keeps (spine S2-25), by the work and never by t
       [04_Phase_04_Ordinary_Life.md]  | **Phase 7** | HF4-6 | The night load: the racks' hours (Phase 3 DQ-44; REQ-124) agains
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 7** | HF5-4 | Who keeps the spur, its culverts, the gulf ice and the drains, a
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 7** | HF5-5 | The grid's route, form and feeding plant at the height (a line a
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 7** | HF5-6 | The unnamed and half-named dependencies: the organic matter's so
       [04_Phase_06_Meaning.md]  | **Phase 7** | HF6-1 | The physical price of any exclusion-shaped sanction (lethal cold
       [04_Phase_06_Meaning.md]  | **Phase 7** | HF6-2 | Who keeps what is kept by hand, by the work and never by title (
       [04_Phase_06_Meaning.md]  | **Phase 7** | HF6-3 | The supply the keeping rides, as the failure the keeping cannot 
       [04_Phase_06_Meaning.md]  | **Phase 7** | HF6-4 | Counterculture seeds as possible factions, if any: keepers awake
  -> Phase 8:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 8** | HF2-15 | Language: the dominant language as every room's common tongue; 
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 8** | HF2-16 | Small rows' practices and whether any institution holds them; t
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 8** | HF3-9 | What any built form must answer (rock against wet or made ground
       [04_Phase_04_Ordinary_Life.md]  | **Phase 8** | HF4-7 | With the CST (`DR-137` item 8): what people do in their downtime
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 8** | HF5-7 | The things of the doors: what comes up the spur and what flies f
       [04_Phase_06_Meaning.md]  | **Phase 8** | HF6-5 | The things of keeping, named by use only: the curtain for the ma
       [04_Phase_07_Order.md]  | **Phase 8** | HF7-1 | The things of the keeping work, named by use only: heat and pick
       [04_Phase_07_Order.md]  | **Phase 8** | HF7-2 | What the place values and trades, as recorded for the national c
       [04_Phase_07_Order.md]  | **Phase 8** | HF7-3 | With the CST: Step 3 RF-85 (a producers' body widening into the 
       [04_Phase_07_Order.md]  | **Phase 8** | HF7-4 | What the hard place asks of things, priced in workers (53,068.4 
  -> Phase 9:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 9** | HF2-17 | Which way the builds and senses of robots built here lean, from
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 9** | HF2-18 | The two halves' different arrival records (RF-105); the foundin
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 9** | HF2-19 | The native human's standing under the draft, after the develope
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 9** | HF2-20 | Commonality by shared work and the small rows' practices, carri
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 9** | HF2-21 | The human–robot baseline standing on the forfeiture for later e
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 9** | HF3-10 | Which way the senses of robots built here lean, as a tendency f
       [04_Phase_04_Ordinary_Life.md]  | **Phase 9** | HF4-8 | The robot half's day: a warm charge and a dream, overnight most 
       [04_Phase_04_Ordinary_Life.md]  | **Phase 9** | HF4-9 | The humans outside the industry model's count, as model arithmet
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 9** | HF5-8 | The populations at the edge: freight crews and observers as the 
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 9** | HF5-9 | The robot arrival: the compelled channel open in law and unrecor
       [04_Phase_06_Meaning.md]  | **Phase 9** | HF6-6 | The two mortalities: the human half ages and is the ordinary yea
       [04_Phase_06_Meaning.md]  | **Phase 9** | HF6-7 | Membership and the first-year arrival: the newcomer as one who h
       [04_Phase_06_Meaning.md]  | **Phase 9** | HF6-8 | Counterculture seeds as possible populations: whether anyone's h
       [04_Phase_07_Order.md]  | **Phase 9** | HF7-5 | The populations the order fails or leaves outside: the newcomer 
       [04_Phase_07_Order.md]  | **Phase 9** | HF7-6 | The robot half's working order: the upkeep trade (B3 6,348.2, on
       [04_Phase_07_Order.md]  | **Phase 9** | HF7-7 | The knowledge populations: newcomers in their first year; traine
       [04_Phase_07_Order.md]  | **Phase 9** | HF7-8 | The contradiction inside each person (keeper by hand, dependent 
       [04_Phase_08_Making.md]  | **Phase 9** | HF8-1 | The robot half's sustenance as a population fact, for the popula
       [04_Phase_08_Making.md]  | **Phase 9** | HF8-2 | Two tables in a mixed household, and the opposite flows of food 
       [04_Phase_08_Making.md]  | **Phase 9** | HF8-3 | Robot speech: Hawaiian (later Tepenian) plus her building commun
       [04_Phase_08_Making.md]  | **Phase 9** | HF8-4 | Which way the hearing, and the cold sense, of robots built here 
       [04_Phase_08_Making.md]  | **Phase 9** | HF8-5 | The populations of making: households keeping origin forms neare
       [04_Phase_08_Making.md]  | **Phase 9** | HF8-6 | Robots clothed the same way as humans, sharing the same hook, sa
  -> Phase 10:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 10** | HF2-22 | No known resident, founder or arrival is named (spec L285); a 
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 10** | HF3-11 | Places that now have a look and a sound, to be named only once
       [04_Phase_04_Ordinary_Life.md]  | **Phase 10** | HF4-10 | Places the day now has, to be named only once sited (spec L142
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 10** | HF5-10 | Places of relation, named only once sited (spec L142): the spu
       [04_Phase_06_Meaning.md]  | **Phase 10** | HF6-9 | Places of meaning, named only once sited (spec L142): ground wi
       [04_Phase_07_Order.md]  | **Phase 10** | HF7-9 | Places of order, named only once sited (spec L142): the culvert
       [04_Phase_08_Making.md]  | **Phase 10** | HF8-7 | Places and objects of making, named only once sited (spec L142)
       [04_Phase_08_Making.md]  | **Phase 10** | HF8-8 | The threshold, the curtain, the lamp and the seed reserve are w
       [04_Phase_09_Populations.md]  | **Phase 10** | HF9-1 | The populations' roster for the catalog: two kinds, neither a m
       [04_Phase_09_Populations.md]  | **Phase 10** | HF9-2 | The places where these populations meet or that they need, name
       [04_Phase_09_Populations.md]  | **Phase 10** | HF9-3 | Two tables, two kinds of night, two mortalities, and the opposi
       [04_Phase_09_Populations.md]  | **Phase 10** | HF9-4 | The warm room as every robot's dreaming place, and the cold res
       [04_Phase_09_Populations.md]  | **Phase 10** | HF9-5 | The robot leans as tendencies for any robot written here, never
       [04_Phase_09_Populations.md]  | **Phase 10** | HF9-6 | When as well as where: robots span the height in one lifetime a
```

**Triage:** Step 5 is not a phase file; the outbound total is unchanged at 85. Its own rows are HF5-1 to HF5-22, the first six to stage B (answered in Part 2) and the rest to Steps 6 to 10.


## Developer questions filed

DQ-61 to DQ-67 (Part 1: DQ-61 to DQ-64; Part 2: DQ-65 to DQ-67) filed as **DEC-627 to DEC-633**, each bullet copied whole.

## What this record cannot show

The readers' reasoning between their reading and their output; how much of each Round 3 rested on the main text alone (all six were allowed to sample the docket and check rows); whether stage A's readers, who were also stage B's, carried anything unsealed into stage B beyond what Part 1 records (the seal fixes Part 1's text, not the readers' memory: the reason the leg was named and sealed first). 'judgement' is the one kept British form and is reported but not counted.
