# Ariun Nuur — ULM Step 7 (QA: the gates) — T8 round record

**Unit:** Step 7, run as three sub-units by files: **Q1** (the Step −1 contract, the frame, Steps 1–3, Phases 2–3), **Q2** (Phases 4–8),
**Q3** (Phase 4 again for Gate 3, Phases 9–10, Steps 5–6). **Written:** `07_QA_Gates.md` (2,197 lines; PROPOSED, not declared complete).
**Run mode:** WARM (`DR-6`). **Date:** 2026-11-20. **Lists and briefs (sha256[:16]):** Q1 list 84671b2be139bc10, brief 25c10a4064fe977a
(16 entries) · Q2 list c7d9ddc169b8a37b, brief fa68fc6d2e297a34 (14) · Q3 list f5171abbe72f15cb, brief a85dd1f6fcd052e0 (14). **Merge
brief:** `.t8_merge_brief_07_Step7.md` (88323aa89a1954ad; 15 orchestrator points). **Inputs the orchestrator built:** the rebuilt findings
index `.t8_Step8_findings_index.md` (italic titles included) and the mechanical sweep `.t8_Step7_mechanical_sweep.md` (768 hits). Both
failed known-case checks in the readers' hands (see *Procedural events*). **No web call** by any agent in this unit.

## Round 1 — receipts
| Sub-unit | A | B | C | MANIFEST |
|---|---|---|---|---|
| Q1 | 557 lines | 429 | 501 | 16 of 16, each |
| Q2 | 513 | 379 | 399 | 14 of 14, each |
| Q3 | 562 | 361 | 479 | 14 of 14, each |

Each reader's per-gate verdicts are in its receipt line in `RUN_PROGRESS_Ariun_Nuur.md` and in its own file (`.t8_Step7Q{n}_reader{A,B,C}.md`).

## Round 2 — Q1, `Tools/triple_read_verify.py`, raw output whole (run 1)

```
required files: 16
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2936-2977] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/04_QA_Gates_and_Differentiation.md  [range 96-422] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Corpus_Reference_Sheets/QA_Gates_Full_Text_Quick_Reference.md  [range 1-362,364-365] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/Datasheets/Step_7.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/Datasheets/Phase_7.md  [range 1-45,47-52,54-60] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Extent_and_Density_Per_City.md  [range 625,631] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 2058-2065] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.1_Step_MINUS-1_Input_Contract.md  [range 1-281,355-367] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00_Frame.md  [range 1-282,301-343,412-431] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/01_Inherited.md  [range 1-176,199-248,321-356] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md  [range 1-15,57-424,510-600,713-769] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/03_Research.md  [range 1-17,29-310,386-506,597-644] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_02_Composition_and_Arrival.md  [range 1-29,97-424,512-533] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_03_Surface_and_Texture.md  [range 1-30,106-411,519-547] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/.t8_Step5_findings_index.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/.t8_Step7_mechanical_sweep.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

**Q1 exact-field check** (`exact_fields.py`; raw output whole):

```
.t8_Step7Q1_readerA.md: 32 fields compared exactly, 0 differ
.t8_Step7Q1_readerB.md: 32 fields compared exactly, 0 differ
.t8_Step7Q1_readerC.md: 32 fields compared exactly, 0 differ
```

## Round 2 — Q2, `Tools/triple_read_verify.py`, raw output whole (run 1)

```
required files: 14
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2936-2977] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/04_QA_Gates_and_Differentiation.md  [range 96-422] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Corpus_Reference_Sheets/QA_Gates_Full_Text_Quick_Reference.md  [range 1-362,364-365] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/Datasheets/Step_7.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/Datasheets/Phase_7.md  [range 1-45,47-52,54-60] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Extent_and_Density_Per_City.md  [range 625,631] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 2058-2065] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_04_Ordinary_Life.md  [range 1-26,164-474,595-622] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_05_Relation_and_Geometry.md  [range 1-29,255-624] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_06_Meaning.md  [range 1-38,132-608] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_07_Order.md  [range 1-87,256-1020,1117-1156] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_08_Making.md  [range 1-25,126-384] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/.t8_Step5_findings_index.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/.t8_Step7_mechanical_sweep.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

**Q2 exact-field check** (`exact_fields.py`; raw output whole):

```
.t8_Step7Q2_readerA.md: 28 fields compared exactly, 0 differ
.t8_Step7Q2_readerB.md: 28 fields compared exactly, 0 differ
.t8_Step7Q2_readerC.md: 28 fields compared exactly, 0 differ
```

## Round 2 — Q3, `Tools/triple_read_verify.py`, raw output whole (run 1)

```
required files: 14
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2936-2977] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/04_QA_Gates_and_Differentiation.md  [range 96-422] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Corpus_Reference_Sheets/QA_Gates_Full_Text_Quick_Reference.md  [range 1-362,364-365] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/Datasheets/Step_7.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/Datasheets/Phase_7.md  [range 1-45,47-52,54-60] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Extent_and_Density_Per_City.md  [range 625,631] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 2058-2065] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_04_Ordinary_Life.md  [range 1-26,164-474,595-622] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_09_Populations.md  [range 1-28,193-520] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md  [range 1-47,236-465,579-1107,1197-1933] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md  [range 1-914,1023-1491] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/06_Differentiation.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/.t8_Step5_findings_index.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/.t8_Step7_mechanical_sweep.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

**Q3 exact-field check** (`exact_fields.py`; raw output whole):

```
.t8_Step7Q3_readerA.md: 28 fields compared exactly, 0 differ
.t8_Step7Q3_readerB.md: 28 fields compared exactly, 0 differ
.t8_Step7Q3_readerC.md: 28 fields compared exactly, 0 differ
```

## Round 3 — cross-check verdicts (the verdict lines of each reply)

- **Q1 reader A:**
  - VERDICT B: CONSISTENT — B read the same material and its gates rest on lines I can confirm; it misses the darkness-at-rest overreach under Gate 2 and several of the Gate 9 lines, and adds three true failures I missed (B121, B122, B125).
  - VERDICT C: CONSISTENT — C read the same material and its counts and quotations check out; its Gate 9 should be FAIL rather than FLAG, because its row 12 ("holds") is contradicted by the lines it cites, and it misses the Gate 2 failure.
- **Q1 reader B:**
  - VERDICT A: CONSISTENT — Reader A read the same spans and its PROOF fields match mine; its gate set overlaps mine, but it misses the FIND-P3-72 district placement and the treaty-tag claims, so Gates F and 0 read softer than the evidence supports.
  - VERDICT C: CONSISTENT — Reader C read the same spans and adds valid finds (the merge-rule span, LAW 0-P coverage, DS2's lag, the stores and the archive), but its Gate 9 FLAG and its Gate 2 and Gate F PASS miss failures the files show.
- **Q1 reader C:**
  - VERDICT A: CONSISTENT — A read the same material (its PROOF fields match mine field for field), and its Gate 2 and Gate 9 FAILs hold up at their sources and are catches I missed.
  - VERDICT B: CONSISTENT — B read the same material (identical PROOF fields), and its Gate F FAIL, the missing treaty-draft tags and the Gate 9 overreach all check against lines I read.
- **Q2 reader A:**
  - VERDICT B: CONSISTENT — B read the same spans and all its positional PROOF fields match mine. It finds real contradictions I missed, but it misses the electricity conflict that should fail its Gate 5 and Gate C, and it records two deviations in method.
  - VERDICT C: CONSISTENT — C read the same spans and all its positional PROOF fields match mine. Its errata check out at source, but it misses four of my Gate 3 contradictions and the dropped condition on the corridor.
- **Q2 reader B:**
  - VERDICT A: CONSISTENT — A read the same material at the same spans, its PROOF fields match mine, and its findings differ from mine by addition and omission, not by contradiction; one verdict, Gate 2's PASS, is not supported by its own evidence.
  - VERDICT C: CONSISTENT — C read the same material at the same spans, its PROOF fields match mine, and it found two defects I missed; one verdict, the station-builder scan's FLAG, is softer than its own evidence supports.
- **Q2 reader C:**
  - VERDICT A: CONSISTENT — A read the same admitted material, reached the same core FAILs (electricity under `DEC-705`, the spec L159 citation, generator vocabulary in prose, the sweep's line-wrap miss) and found several real Gate 3 contradictions I missed; its one wrong verdict is Gate 2 PASS.
  - VERDICT B: CONSISTENT — B read the same material, matched me on Gate 2, Gate F, the shared night and the eight index omissions, and added sound Gate 3 finds; its one wrong verdict is Gate 5 PASS, because it missed the `DEC-705` electricity lag.
- **Q3 reader A:**
  - VERDICT B: CONSISTENT — B read the same material and backs every verdict with lines; it misses four of my FAILs and finds three real ones I missed.
  - VERDICT C: CONSISTENT — C read the same material and its counts, density and Gate F evidence match mine; it misses the Step 6 generator-count FAIL even though it quotes the line that shows it, and it rates the station-builder denials only a FLAG.
- **Q3 reader B:**
  - VERDICT A: CONSISTENT — A read the same material, its PROOF fields and its central findings match mine, and where we differ it is because one of us found something the other missed or because the call needs judgment, not because either misread a source.
  - VERDICT C: CONSISTENT — C read the same material and its PROOF fields and counts match mine, but it passes Step 6's "nine of ten" count, which A and I both found wrong, and it scores the station-builder denials as a FLAG rather than a FAIL.
- **Q3 reader C:**
  - VERDICT A: CONSISTENT — A read the same material, its counts, arithmetic and PROOF fields match mine, and where we differ it is mostly on dispositions, with three of its finds (Step 6 L318, the datasheet's L21 pointer, Phase 4 L264) being ones I missed.
  - VERDICT B: CONSISTENT — B read the same material and agrees on the core FAILs (Gate 0, Gate 3, Gate F), and it adds real finds I missed (Phase 10 L42–44, CAT-39, Phase 9 L396 and L462), but it misses two Gate 3 contradictions I found.

**All nine replies: six of six verdicts CONSISTENT per sub-unit (18 verdict lines, 18 CONSISTENT).**

## Quotation, spelling and name checks on `07_QA_Gates.md` (`checks.py`, once against each sub-unit's list; raw output whole)

**Against Q1's list:**

```
quoted strings checked: 377 not found: 220
  MISS: Not assigned
  MISS: ; spine L293 (3 + 1 + 4 = 8 assigned, 1 undetermined); spine L597 (16 + 3 + 1 = 20); spine L754 
  MISS: ; frame L218: 
  MISS: 11 spans, 73 lines
  MISS: four of them
  MISS:  *(as B pasted it)*, while the same table's §10 row (L316) reads 
  MISS: extends CAT-33, the null
  MISS: extends FIND-P10-12 (a null: no marker stands at any computed point of the pole; U3-F203–F205)
  MISS: C (FIND-P9-231)
  MISS: standing costs
  MISS: ; L62: 
  MISS: ; P2 L330: 
  MISS: ; P3 L326: 
  MISS: C is right to FLAG it
  MISS: standing costs
  MISS: The place's grudging
  MISS: tolerances stay tolerances
  MISS: Every remedy the city's deficits address
  MISS: for most of the city the thin air is unspeakable
  MISS: *Characteristic failure* (spine D-3)
  MISS:  rests on the largest row at 15.97% (C); 
  MISS: **the never-asked:** the arrival who never teaches, is never asked, or is never the earlier arrival
  MISS: all 441,378: every arrival
  MISS:  Against P7 L725–726 (FIND-P7-36): 
  MISS:  Against P4 L270 (FIND-P4-42): 
  MISS: → **Every body arrives by Hwy 37, at least for its last stretch.**
  MISS: Functional layers ... are not populations with a culture of their own
  MISS: the honor is paid daily, not once [B]
  MISS: the district is where the city's own scientists work
  MISS: The ice tools in every household
  MISS: ***No admitted line states plain coolant's composition** … so whether coolant is made from water … are not written … **Conditionally,** if its formulation is wa
  MISS: drinking, washing and a robot's coolant (RP L275) draw on the same account as warmth
  MISS: Whatever either body takes in has come by Hwy 37, or is water made here from ice
  MISS: both chains run through Hwy 37; neither is grown here
  MISS: whether this city mines, processes or only receives it is reserved (frame RF-21, PV-6)
  MISS: most of what anyone meets in a day is baseline work (Phase 4 FIND-P4-2)
  MISS: it is not a majority, and it is not a count of the people met in a day
  MISS: ***The city's largest unwritten work is teaching, and it is in no sector***
  MISS: some part of the settled residents' day is always given to teaching the newest
  MISS: So the city's deaths stay here, and every death here is a resident's (Phase 4 FIND-P4-61).
  MISS: it cannot be escaped by leaving, because a human who came cannot return and no departure is written (brief §4 item 5; RF-30)
  MISS: no departure from the city is written (RF-30), so its expertise does not leave as emigrants
  MISS: no departure is written (RF-30); every route in is one-way as far as the files write it
  MISS: The site's own record has always run on a world clock (research UI-6, reserved RF-70) [A].
  MISS: the real station's record was kept at four fixed hours (research FIND-39; UI-6, reserved as RF-70 and RF-106)
  MISS: The one clock already on the site is a world clock
  MISS: The only work that can be stopped is the work that is the city's purpose … the body's wins and the purpose yields: the city's reason to exist is its first sacri
  MISS: except at the shaft
  MISS: the shaft is kept filled and watched whether or not anyone works in it
  MISS: cannot be paused without loss
  MISS: The national pattern is broken here every night, by necessity, by whoever keeps the heat.
  MISS: the only written point where every resident's day is the same
  MISS: everyone stops in the same hours
  MISS: what is fresh is the exception that came by the road or was grown on the electric supply (FIND-P8-8)
  MISS: Frozen keeps, fresh does not, and every fresh thing comes by the road (FIND-P4-15)
  MISS: No growing practice is written (RF-37).
  MISS: electricity from a source no record places (`DEC-705`)
  MISS: **Whether the city is on the grid: not written. What powered it before the grid came fully online: not written. Nothing is assumed.**
  MISS: Charge for 284,693 robots is drawn while 156,685 humans sleep in heat, all on one electric supply
  MISS: some part of the settled residents' day
  MISS: The keepers of the night: of heat, water, charge and the shaft ... In a night months long they are those who stay with the instruments across it; real facilitie
  MISS: **The night is a time, not a darkness**
  MISS: the least cold months and the only ones in which the place shows anything to the eye but the city
  MISS: The street never goes quiet.
  MISS: the street never goes quiet (Phase 3 FIND-P3-18; RC-54)
  MISS: the city goes quiet at an hour on a clock
  MISS: Charging points somewhere cold
  MISS: Phase 4 L397; Phase 7 L578
  MISS: every day is planned so that no charge is taken cold
  MISS: So whatever stands must be lifted every year and travels with the ice
  MISS: does not arrive unseen: the air is still, and when visibility closes something is actually falling
  MISS: holds outdoors and away from the city, not over it
  MISS: Everyone stops at the same clock hours, robots to charge and humans to sleep
  MISS: every layer and both bodies share the night's hours, less those whose function keeps it
  MISS: For about 120 days the only light the files write is the city's own
  MISS: The threshold is the city's most dangerous ordinary place, for hands and for kept things
  MISS: a closed road back for every human
  MISS: comes for a term and stays
  MISS: ; C: the spine sentence's clause 
  MISS: , as C pasted it); P4 L601 (Q-102: 
  MISS: induction is a frontier shape
  MISS: | **its own electricity** | **not written** |
  MISS: ; P5 L357: 
  MISS: **Supply from elsewhere:**
  MISS: ; and P7 L389–392 (FIND-P7-9), under 
  MISS: Learning and belonging are one process here
  MISS: ; P7 L449, row (l): 
  MISS: the research's one never-off structure
  MISS: beyond every city's baseline
  MISS: The drilling apparatus, as the research's tool
  MISS: its drilling apparatus
  MISS: ) repeats CAT-36 (L785, 
  MISS: the lake program
  MISS: the genetics program
  MISS: lake genetics program
  MISS: from an analogy among comparables to evidence
  MISS: **CONTRADICTED IN PART, by tier-3 lines only**
  MISS: no one leaves
  MISS: whoever the order fails is kept by default
  MISS: ; P5 L403 (
  MISS: ), P8 L233 (
  MISS: ) and P7 L726 (
  MISS: cannot be paused without loss
  MISS: The keepers of heat stand in no record
  MISS: never arrives and is not cataloged as a person
  MISS: 44–63 km² by construction, at the table's two assumed densities
  MISS:  (now L149 of that file) is a naming fact only
  MISS: exact match, full monthly table also matches
  MISS: not reproduced here to avoid redundant duplication of a 12-row table
  MISS: an infrastructure fact, `DR-24`
  MISS: about 3.8×
  MISS:  (as C quotes it); Phase 5 applies it in full (P5 L436, L458; P6 L414; P8 L151), but P4 L188 (
  MISS:  with no condition, after writing 
  MISS: one highway through an unpeopled corridor
  MISS: barred by a ruling
  MISS: through the stage-A item that already carries it
  MISS: used for no date
  MISS: about 1,260 km away overland with no road (spec L135; ...)
  MISS: (spec L9, L135, L169; ...)
  MISS: the pole the city approaches (spec L155)
  MISS: genuinely emergent
  MISS: Mentor and mentee bonds are a genuine robot institution, maker and made is not (physiology L418)
  MISS: ; P8 L229 (FIND-P8-30): 
  MISS: The real site's history is never the signature instance
  MISS: What it is never anchored in
  MISS: the station's operator or nation (`DR-19`);
  MISS: the records' language is not inferred from the station's operators (spine RF-46) [B]
  MISS: the station is a coordinate and a paper inheritance, never the population's origin
  MISS: no surviving culinary tradition from the station operators' nation
  MISS: the real site is researched as a site, never its operator (`DR-19`)
  MISS: (G1, Phase 10)
  MISS: the symbol files (G1, Phase 10)
  MISS: (G7, PROVISIONAL)
  MISS: FIND-P9-38, the minority's unspeakable cost
  MISS: One finding, FIND-P3-34, rests in part on a treaty-draft article, through Phase 2 RF-86.
  MISS:  Ending corrected: 
  MISS: … and no departure of those who came is written; …
  MISS:  RF-104's title: 
  MISS:  The sentence beginning 
  MISS:  is struck. RF-87's foreclosure to read 
  MISS: . The sentence then reads: 
  MISS: The spine's physical-constraint profile (L104–143)
  MISS:  P6 L410: 
  MISS: robots charging and humans sleeping at once
  MISS: . L169 corrected: 
  MISS: Teaching is unwritten work of unknown size, and it is in no sector
  MISS: some part of the settled residents' day
  MISS: so no line has its expertise leaving as emigrants
  MISS:  P4 corrected: 
  MISS: the purpose's stoppable part yields
  MISS: all on one supply (spine §8e)
  MISS: (spec L9, L159)
  MISS: Here *paper* names the founding's condition (spec L145).
  MISS: a G7 form, not transplanted
  MISS: the picks' real-world form, not transplanted
  MISS: every arrival is a standing cost paid in heat at every resting place
  MISS: Every free hour costs heat.
  MISS: a step across the full cost of the cold
  MISS: Every remedy the city's deficits address
  MISS: Every remedy for what the city lacks lies in the parent
  MISS: each one is a new standing cost before anything else
  MISS: recorded as a possible lasting cost
  MISS: so raising is a standing cost
  MISS: so raising is a cost that never ends
  MISS: every arrival is a standing cost paid in heat by everyone
  MISS: The place's grudging tolerances stay tolerances, each permitted and charged and none prohibited
  MISS: What the place permits and charges for stays permitted and charged, and none of it is prohibited
  MISS: still runs into the standing cost
  MISS: still runs into the cost of heat
  MISS: is first a standing cost paid in heat
  MISS: first adds a lasting cost paid in heat
  MISS: every indoor hour carries the standing cost
  MISS: every indoor hour costs heat
  MISS: crosses the place's whole standing cost
  MISS: crosses from paid heat into the full cold
  MISS: a step from paid heat into the full cold
  MISS: Every free hour costs heat
  MISS: C (FIND-P9-231)
  MISS: C (C231)
  MISS: the street never goes quiet (Phase 3 FIND-P3-18; RC-54)
  MISS: Phase 4 L397; Phase 7 L578
  MISS: ; the same change to 
  MISS: Everyone stops at the same clock hours, robots to charge and humans to sleep
  MISS: . L278: add 
  MISS: , reading 
  MISS: the station's operator or nation (`DR-19`);
  MISS: a city-wide origin; the founders' stock; Gen/Mark; build (Ch. 13 L29–36)
  MISS: ; the cell reads 
  MISS: a G7 form
  MISS: deficits address
  MISS: grudging tolerances
  MISS: for most of the city the thin air is a cost no one's body gives a reason to name; for the rest it is each person's own
  MISS: thin air is a lack no one in particular can remedy
  MISS: the minority's unspeakable cost
  MISS: FIND-P9-38, the minority's cost the majority's bodies give no reason to name
  MISS: unspeakable to the majority
  MISS: The minority's chief cost, one the majority's bodies give no reason to name
  MISS: deficits address
  MISS: 11 spans, 73 lines
  MISS: not required
  MISS: Raw output, whole
  MISS: written as registers; the type stays Settlement; no dual typing
  MISS: 7 of 7
  MISS: Every body arrives by Hwy 37
  MISS: every death here is a resident's
  MISS: the night's keepers, a function (row (l))
  MISS: never a filter for being kept; the same knowledge marks belonging (Phase 5 FIND-P5-35)
  MISS: refused, `unmet`
  MISS: refused under the peer-free test; its disposition is the Review Panel's (Step 8)
  MISS: so the honor is paid daily, not once
  MISS: the city's most dangerous ordinary place
  MISS: the threshold is where a kept thing, and the hands carrying it, are most at risk
  MISS: Founders come only from the Founding Register (`DR-19`).
  MISS:  and, for the human, 
  MISS: No one leaves
  MISS: paid daily
  MISS: never goes quiet
  MISS: standing costs
  MISS: Raw output, whole
  MISS: last arrival
07_QA_Gates.md British-form hits: []
other-location name scan (names: line numbers): {'Mirny': [580, 892]}
tower-name count: 0
```

**Against Q2's list:**

```
quoted strings checked: 377 not found: 207
  MISS: Not assigned
  MISS: Count: 6
  MISS: COVERAGE: Ariun_Nuur.md 1-222, no gaps, no overlaps
  MISS: ; spine L293 (3 + 1 + 4 = 8 assigned, 1 undetermined); spine L597 (16 + 3 + 1 = 20); spine L754 
  MISS: 22 targets
  MISS: 7 facts not used
  MISS: 4 positions covered
  MISS: 17 questions (Q-85 to Q-101)
  MISS: Every finding that rests on a treaty article is tagged `[treaty draft]` and listed under *Generators used*
  MISS: and no return (TD L77; brief §4 item 5)
  MISS: humans who came could not go back (TD L77)
  MISS: ; frame L218: 
  MISS: CLOSED until Step 6
  MISS: Step 1's questions (`DEC-708` to `DEC-716`) are unanswered
  MISS: the same substance as Step 1's Q-35 (`DEC-715`)
  MISS: four of them
  MISS:  *(as B pasted it)*, while the same table's §10 row (L316) reads 
  MISS: extends CAT-33, the null
  MISS: extends FIND-P10-12 (a null: no marker stands at any computed point of the pole; U3-F203–F205)
  MISS: C (FIND-P9-231)
  MISS: location registries
  MISS: G7-tagged
  MISS: ; L62: 
  MISS: ; P2 L330: 
  MISS: ; P3 L326: 
  MISS: C is right to FLAG it
  MISS: for most of the city the thin air is unspeakable
  MISS: at Band 4, `00b` operates normally and its Band-1 inversion does not apply
  MISS: A research place whose people have no term
  MISS: | RF-55 | Rest needs darkness in the midnight-sun months as well as heat (FIND-17) |…
  MISS:  rests on the largest row at 15.97% (C); 
  MISS:  Against P7 L725–726 (FIND-P7-36): 
  MISS:  Against P4 L270 (FIND-P4-42): 
  MISS: Functional layers ... are not populations with a culture of their own
  MISS: the honor is paid daily, not once [B]
  MISS: the district is where the city's own scientists work
  MISS: The ice tools in every household
  MISS: The keepers of the night: of heat, water, charge and the shaft ... In a night months long they are those who stay with the instruments across it; real facilitie
  MISS: The street never goes quiet.
  MISS: the street never goes quiet (Phase 3 FIND-P3-18; RC-54)
  MISS: Charging points somewhere cold
  MISS: Phase 4 L397; Phase 7 L578
  MISS: So whatever stands must be lifted every year and travels with the ice
  MISS: holds outdoors and away from the city, not over it
  MISS: Everyone stops at the same clock hours, robots to charge and humans to sleep
  MISS: every layer and both bodies share the night's hours, less those whose function keeps it
  MISS: The threshold is the city's most dangerous ordinary place, for hands and for kept things
  MISS: a closed road back for every human
  MISS: comes for a term and stays
  MISS: The stock the city weighs most is not the stock that founded it
  MISS: For the robot majority, the native layer is the culture; for the human minority, the native layer is the cost
  MISS: ; C: the spine sentence's clause 
  MISS: , as C pasted it); P4 L601 (Q-102: 
  MISS: induction is a frontier shape
  MISS: breathe once-through outside air, continuously
  MISS: ; P5 L357: 
  MISS: ; and P7 L389–392 (FIND-P7-9), under 
  MISS: cores kept in the real site's trench
  MISS: ; P7 L449, row (l): 
  MISS: The drilling apparatus, as the research's tool
  MISS: its drilling apparatus
  MISS: ) repeats CAT-36 (L785, 
  MISS: the lake program
  MISS: the genetics program
  MISS: lake genetics program
  MISS: from an analogy among comparables to evidence
  MISS: **CONTRADICTED IN PART, by tier-3 lines only**
  MISS: no one leaves
  MISS: possible and written nowhere
  MISS: The city must hold its losing side (FIND-25)
  MISS: and those who came have stayed
  MISS: the population cannot renew itself by people leaving
  MISS: so whoever came and did not fit has no exit and no written place
  MISS: so her first impression is of the place she will live in
  MISS: met by the same physics and the same law that keep everyone here
  MISS: so understanding does not leave with people who leave
  MISS: ; P5 L403 (
  MISS: ), P8 L233 (
  MISS: ) and P7 L726 (
  MISS: The keepers of heat stand in no record
  MISS: never arrives and is not cataloged as a person
  MISS: the division is circular
  MISS: location registries
  MISS:  (now L149 of that file) is a naming fact only
  MISS: exact match, full monthly table also matches
  MISS: not reproduced here to avoid redundant duplication of a 12-row table
  MISS: an infrastructure fact, `DR-24`
  MISS: a folder named after the city and its topic
  MISS: about 90% retained
  MISS: the same size
  MISS:  (as C quotes it); Phase 5 applies it in full (P5 L436, L458; P6 L414; P8 L151), but P4 L188 (
  MISS:  with no condition, after writing 
  MISS: barred by a ruling
  MISS: through the stage-A item that already carries it
  MISS: as what is visible at the height
  MISS: 500+ years
  MISS: decades of summer seasons
  MISS: the labs, stores, shaft and archive
  MISS: Whether the inherited station lies inside the district is not written (RF-1)
  MISS: about 1,260 km away overland with no road (spec L135; ...)
  MISS: (spec L9, L135, L169; ...)
  MISS: the pole the city approaches (spec L155)
  MISS: genuinely emergent
  MISS: Mentor and mentee bonds are a genuine robot institution, maker and made is not (physiology L418)
  MISS: in this city leaving is hard (G2)
  MISS: **Not a characterizing absence; no cause is drawn, and the station is never one:** the law exists so that a city is characterized by who lives there, not by who
  MISS: any cause, the station above all (NNS L7)
  MISS: and never the station as a cause (`DR-19`; NNS L7)
  MISS: and the station passed through operators whose identity is irrelevant (NNS L13, L15; frame DL-3)
  MISS: with no national-origin match to the station's former operator required (TD L55)
  MISS: **the language of the inherited station records is in no listed line, and it must not be inferred from the station's operators** (`DR-19`)
  MISS: the records' language is not inferred from the station's operators (spine RF-46)
  MISS: its operator is a coordinate and is not used
  MISS: the operator not used (`DR-19`)
  MISS: ; P8 L229 (FIND-P8-30): 
  MISS: What it is never anchored in
  MISS: the station's operator or nation (`DR-19`);
  MISS: the records' language is not inferred from the station's operators (spine RF-46) [B]
  MISS: the station is a coordinate and a paper inheritance, never the population's origin
  MISS: no surviving culinary tradition from the station operators' nation
  MISS: the real site is researched as a site, never its operator (`DR-19`)
  MISS: (G4, read beside)
  MISS: (G7, PROVISIONAL)
  MISS: FIND-P9-38, the minority's unspeakable cost
  MISS: One finding, FIND-P3-34, rests in part on a treaty-draft article, through Phase 2 RF-86.
  MISS: What it permits but punishes
  MISS:  Ending corrected: 
  MISS: … and no departure of those who came is written; …
  MISS:  RF-104's title: 
  MISS:  The sentence beginning 
  MISS:  is struck. RF-87's foreclosure to read 
  MISS: , and the station passed through operators whose identity is irrelevant
  MISS: no living scientific legacy or institutional culture survived
  MISS: . The sentence then reads: 
  MISS: each population being assigned to a station
  MISS: is a standing cost only while it is kept filled and watched
  MISS: where the cold's standing cost already falls
  MISS: (spine RF-47, a G7 adjustment, not canon)
  MISS: each a standing cost paid in heat at every resting place
  MISS: The spine's G2 quadrants (L104–143)
  MISS: The spine's physical-constraint profile (L104–143)
  MISS: This answers the spine's G3 tension as texture only
  MISS: (research FIND-18; G7 real-world form, nothing written for the city)
  MISS: Raising, wherever it is done, is a standing cost
  MISS:  P6 L410: 
  MISS: . L169 corrected: 
  MISS: Teaching is unwritten work of unknown size, and it is in no sector
  MISS: so no line has its expertise leaving as emigrants
  MISS:  P4 corrected: 
  MISS: the purpose's stoppable part yields
  MISS: Here *paper* names the founding's condition (spec L145).
  MISS: the picks' real-world form, not transplanted
  MISS: Every free hour costs heat.
  MISS: a step across the full cost of the cold
  MISS: Every remedy for what the city lacks lies in the parent
  MISS: recorded as a possible lasting cost
  MISS: so raising is a cost that never ends
  MISS: What the place permits and charges for stays permitted and charged, and none of it is prohibited
  MISS: still runs into the cost of heat
  MISS: first adds a lasting cost paid in heat
  MISS: every indoor hour costs heat
  MISS: crosses from paid heat into the full cold
  MISS: a step from paid heat into the full cold
  MISS: Every free hour costs heat
  MISS: C (FIND-P9-231)
  MISS: C (C231)
  MISS: the street never goes quiet (Phase 3 FIND-P3-18; RC-54)
  MISS: Phase 4 L397; Phase 7 L578
  MISS: ; the same change to 
  MISS: Everyone stops at the same clock hours, robots to charge and humans to sleep
  MISS: . L278: add 
  MISS: , reading 
  MISS: the station's operator or nation (`DR-19`);
  MISS: a city-wide origin; the founders' stock; Gen/Mark; build (Ch. 13 L29–36)
  MISS: ; the cell reads 
  MISS: the cold's standing cost
  MISS: a G7 adjustment
  MISS: G2 quadrants
  MISS: G3 tension
  MISS: G7 real-world form
  MISS: for most of the city the thin air is a cost no one's body gives a reason to name; for the rest it is each person's own
  MISS: thin air is a lack no one in particular can remedy
  MISS: the minority's unspeakable cost
  MISS: FIND-P9-38, the minority's cost the majority's bodies give no reason to name
  MISS: unspeakable to the majority
  MISS: The minority's chief cost, one the majority's bodies give no reason to name
  MISS: - **FIND-
  MISS: about 18,140 workers fall on the human-keyed term
  MISS: not required
  MISS: Raw output, whole
  MISS: all unanswered
  MISS: written as registers; the type stays Settlement; no dual typing
  MISS: what falls stays
  MISS: a coordinate only (`DR-19`)
  MISS: the night's keepers, a function (row (l))
  MISS: never a filter for being kept; the same knowledge marks belonging (Phase 5 FIND-P5-35)
  MISS: refused under the peer-free test; its disposition is the Review Panel's (Step 8)
  MISS: so the honor is paid daily, not once
  MISS: the city's most dangerous ordinary place
  MISS: the threshold is where a kept thing, and the hands carrying it, are most at risk
  MISS: Founders come only from the Founding Register (`DR-19`).
  MISS:  and, for the human, 
  MISS: No one leaves
  MISS: paid daily
  MISS: never goes quiet
  MISS: Raw output, whole
  MISS: last arrival
07_QA_Gates.md British-form hits: []
other-location name scan (names: line numbers): {'Mirny': [580, 892]}
tower-name count: 0
```

**Against Q3's list:**

```
quoted strings checked: 377 not found: 175
  MISS: Not assigned
  MISS: Count: 6
  MISS: COVERAGE: Ariun_Nuur.md 1-222, no gaps, no overlaps
  MISS: ; spine L293 (3 + 1 + 4 = 8 assigned, 1 undetermined); spine L597 (16 + 3 + 1 = 20); spine L754 
  MISS: 22 targets
  MISS: 7 facts not used
  MISS: 4 positions covered
  MISS: 17 questions (Q-85 to Q-101)
  MISS: Every finding that rests on a treaty article is tagged `[treaty draft]` and listed under *Generators used*
  MISS: and no return (TD L77; brief §4 item 5)
  MISS: humans who came could not go back (TD L77)
  MISS: ; frame L218: 
  MISS: Step 1's questions (`DEC-708` to `DEC-716`) are unanswered
  MISS: the same substance as Step 1's Q-35 (`DEC-715`)
  MISS: 11 spans, 73 lines
  MISS:  *(as B pasted it)*, while the same table's §10 row (L316) reads 
  MISS: location registries
  MISS: G7-tagged
  MISS: standing costs
  MISS: ; L62: 
  MISS: ; P2 L330: 
  MISS: ; P3 L326: 
  MISS: C is right to FLAG it
  MISS: standing costs
  MISS: at Band 4, `00b` operates normally and its Band-1 inversion does not apply
  MISS: A research place whose people have no term
  MISS: | RF-55 | Rest needs darkness in the midnight-sun months as well as heat (FIND-17) |…
  MISS:  rests on the largest row at 15.97% (C); 
  MISS: **the never-asked:** the arrival who never teaches, is never asked, or is never the earlier arrival
  MISS: all 441,378: every arrival
  MISS:  Against P7 L725–726 (FIND-P7-36): 
  MISS:  Against P4 L270 (FIND-P4-42): 
  MISS: → **Every body arrives by Hwy 37, at least for its last stretch.**
  MISS: ***No admitted line states plain coolant's composition** … so whether coolant is made from water … are not written … **Conditionally,** if its formulation is wa
  MISS: Whatever either body takes in has come by Hwy 37, or is water made here from ice
  MISS: both chains run through Hwy 37; neither is grown here
  MISS: most of what anyone meets in a day is baseline work (Phase 4 FIND-P4-2)
  MISS: ***The city's largest unwritten work is teaching, and it is in no sector***
  MISS: So the city's deaths stay here, and every death here is a resident's (Phase 4 FIND-P4-61).
  MISS: it cannot be escaped by leaving, because a human who came cannot return and no departure is written (brief §4 item 5; RF-30)
  MISS: no departure from the city is written (RF-30), so its expertise does not leave as emigrants
  MISS: The site's own record has always run on a world clock (research UI-6, reserved RF-70) [A].
  MISS: The only work that can be stopped is the work that is the city's purpose … the body's wins and the purpose yields: the city's reason to exist is its first sacri
  MISS: The national pattern is broken here every night, by necessity, by whoever keeps the heat.
  MISS: what is fresh is the exception that came by the road or was grown on the electric supply (FIND-P8-8)
  MISS: No growing practice is written (RF-37).
  MISS: electricity from a source no record places (`DEC-705`)
  MISS: **Whether the city is on the grid: not written. What powered it before the grid came fully online: not written. Nothing is assumed.**
  MISS: The street never goes quiet.
  MISS: charging somewhere cold
  MISS: For the robot majority, the native layer is the culture; for the human minority, the native layer is the cost
  MISS: ; C: the spine sentence's clause 
  MISS: , as C pasted it); P4 L601 (Q-102: 
  MISS: breathe once-through outside air, continuously
  MISS: | **its own electricity** | **not written** |
  MISS: ; P5 L357: 
  MISS: ; and P7 L389–392 (FIND-P7-9), under 
  MISS: cores kept in the real site's trench
  MISS: Learning and belonging are one process here
  MISS: ; P7 L449, row (l): 
  MISS: beyond every city's baseline
  MISS: ) repeats CAT-36 (L785, 
  MISS: the lake program
  MISS: possible and written nowhere
  MISS: **A place people cannot leave keeps what the comparables send away.**
  MISS: The city must hold its losing side (FIND-25)
  MISS: the population cannot renew itself by people leaving
  MISS: so whoever came and did not fit has no exit and no written place
  MISS: so her first impression is of the place she will live in
  MISS: met by the same physics and the same law that keep everyone here
  MISS: so understanding does not leave with people who leave
  MISS: whoever the order fails is kept by default
  MISS: ; P5 L403 (
  MISS: ), P8 L233 (
  MISS: ) and P7 L726 (
  MISS: location registries
  MISS:  (now L149 of that file) is a naming fact only
  MISS: exact match, full monthly table also matches
  MISS: not reproduced here to avoid redundant duplication of a 12-row table
  MISS: an infrastructure fact, `DR-24`
  MISS: a folder named after the city and its topic
  MISS: about 3.8×
  MISS:  (as C quotes it); Phase 5 applies it in full (P5 L436, L458; P6 L414; P8 L151), but P4 L188 (
  MISS: no finding rests on it
  MISS:  with no condition, after writing 
  MISS: one highway through an unpeopled corridor
  MISS: as what is visible at the height
  MISS: decades of summer seasons
  MISS: the labs, stores, shaft and archive
  MISS: Whether the inherited station lies inside the district is not written (RF-1)
  MISS: used for no date
  MISS: in this city leaving is hard (G2)
  MISS: **Not a characterizing absence; no cause is drawn, and the station is never one:** the law exists so that a city is characterized by who lives there, not by who
  MISS: any cause, the station above all (NNS L7)
  MISS: and never the station as a cause (`DR-19`; NNS L7)
  MISS: and the station passed through operators whose identity is irrelevant (NNS L13, L15; frame DL-3)
  MISS: with no national-origin match to the station's former operator required (TD L55)
  MISS: **the language of the inherited station records is in no listed line, and it must not be inferred from the station's operators** (`DR-19`)
  MISS: its operator is a coordinate and is not used
  MISS: the operator not used (`DR-19`)
  MISS: ; P8 L229 (FIND-P8-30): 
  MISS: The real site's history is never the signature instance
  MISS: (G7 adjusted)
  MISS: (G4, read beside)
  MISS: One finding, FIND-P3-34, rests in part on a treaty-draft article, through Phase 2 RF-86.
  MISS: What it permits but punishes
  MISS:  Ending corrected: 
  MISS: … and no departure of those who came is written; …
  MISS:  RF-104's title: 
  MISS:  The sentence beginning 
  MISS:  is struck. RF-87's foreclosure to read 
  MISS: , and the station passed through operators whose identity is irrelevant
  MISS: no living scientific legacy or institutional culture survived
  MISS: . The sentence then reads: 
  MISS: each population being assigned to a station
  MISS: where the cold's standing cost already falls
  MISS: (spine RF-47, a G7 adjustment, not canon)
  MISS: The spine's G2 quadrants (L104–143)
  MISS: The spine's physical-constraint profile (L104–143)
  MISS: This answers the spine's G3 tension as texture only
  MISS: (research FIND-18; G7 real-world form, nothing written for the city)
  MISS: Raising, wherever it is done, is a standing cost
  MISS:  P6 L410: 
  MISS: . L169 corrected: 
  MISS: Teaching is unwritten work of unknown size, and it is in no sector
  MISS: so no line has its expertise leaving as emigrants
  MISS:  P4 corrected: 
  MISS: the purpose's stoppable part yields
  MISS: all on one supply (spine §8e)
  MISS: (spec L9, L159)
  MISS: Here *paper* names the founding's condition (spec L145).
  MISS: the picks' real-world form, not transplanted
  MISS: Every free hour costs heat.
  MISS: a step across the full cost of the cold
  MISS: Every remedy for what the city lacks lies in the parent
  MISS: recorded as a possible lasting cost
  MISS: so raising is a standing cost
  MISS: so raising is a cost that never ends
  MISS: The place's grudging tolerances stay tolerances, each permitted and charged and none prohibited
  MISS: What the place permits and charges for stays permitted and charged, and none of it is prohibited
  MISS: still runs into the cost of heat
  MISS: first adds a lasting cost paid in heat
  MISS: every indoor hour costs heat
  MISS: crosses the place's whole standing cost
  MISS: crosses from paid heat into the full cold
  MISS: Every free hour costs heat
  MISS: C (C231)
  MISS: ; the same change to 
  MISS: . L278: add 
  MISS: ; the cell reads 
  MISS: the cold's standing cost
  MISS: a G7 adjustment
  MISS: G2 quadrants
  MISS: G3 tension
  MISS: G7 real-world form
  MISS: FIND-P9-38, the minority's cost the majority's bodies give no reason to name
  MISS: The minority's chief cost, one the majority's bodies give no reason to name
  MISS: about 18,140 workers fall on the human-keyed term
  MISS: 11 spans, 73 lines
  MISS: not required
  MISS: Raw output, whole
  MISS: all unanswered
  MISS: written as registers; the type stays Settlement; no dual typing
  MISS: the city's own genetics research folder
  MISS: a coordinate only (`DR-19`)
  MISS: Every body arrives by Hwy 37
  MISS: every death here is a resident's
  MISS: the night's keepers, a function (row (l))
  MISS: never a filter for being kept; the same knowledge marks belonging (Phase 5 FIND-P5-35)
  MISS: refused under the peer-free test; its disposition is the Review Panel's (Step 8)
  MISS: the threshold is where a kept thing, and the hands carrying it, are most at risk
  MISS:  and, for the human, 
  MISS: standing costs
  MISS: Raw output, whole
  MISS: last arrival
07_QA_Gates.md British-form hits: []
other-location name scan (names: line numbers): {'Mirny': [580, 892]}
tower-name count: 0
```

**Triage (orchestrator, by hand).** A quotation counts as a miss only if it is in no listed file. Every quotation missed against all
three lists was looked up by `grep -F` over the pass folder: each is a reader's proposed rewrite quoted as a proposal (found in that
reader's file: *"written as registers; the type stays Settlement; no dual typing"* Q1 A; *"the night's keepers, a function (row (l))"* and
*"refused under the peer-free test; its disposition is the Review Panel's (Step 8)"* Q2 C; *"never a filter for being kept; the same knowledge
marks belonging"* Q2 A; *"the threshold is where a kept thing, and the hands carrying it, are most at risk"* and the fragment
*" and, for the human, "* Q3 B), a reader's own heading (*"Raw output, whole"*), or a phrase in the Round 3 replies (*"last arrival"*). None
is a source misquote. **British forms: 0. Tower name: 0. Other-location scan:** L580 (the city's own subnet relation) and L892 (the extent
row's raw label, the subnet column). **One quoted recommended answer** (Q-339's line, from Q3 B's Q-B104) carries a national-scale place
name the pass itself uses at Step 5 L882; Q3 Round 3 flagged it as minor. Left as written; a question for Step 9 whether to write it by role.

## Procedural events (the recording law)
1. **The findings index (rebuilt before Step 7) still misses findings:** Q1's readers found 11 in Q1's files (FIND-P2-60 to FIND-P2-68,
   FIND-P3-46, FIND-P3-74), Q2's readers eight (including FIND-P4-66 and FIND-P5-55), and Q1 C three more outside Q1. Its pattern misses at
   least one more heading form. Recorded as an instrument defect (REQ in `07` §6); the index was navigation only.
2. **The mechanical sweep** misses phrases split across a line wrap, a plural on a phrase's first word (Phase 5 L367), terms outside its
   list, and does not cover Step 6. Every gate passed on one of its zeros says so in `07`.
3. **Off-list reads, logged by the readers:** Q1 A opened the Phase 7 datasheet L17–35 (permitted, §0 item 4); Q3 A opened Phase 7
   L576–578; Q3 B opened spec L17. All within the brief's allowance.
4. **Command slips, disclosed by the readers:** `wc -l` on the reader's own output file (Q3 A; Q2 C, undisclosed until Round 3); `ls`,
   `od -c`, `cut` (Q1 B); a shell heredoc for PROOF blocks and an `ls -d` by the city's names (Q2 B); `wc -c`, `head -c`, `cut`, `cat -A`
   (Q3 B); one `sed` piped through `cut` (Q3 A). None changed a PROOF field; Round 2 was UNANIMOUS on every sub-unit at the first run.
5. **Rule slips caught in Round 3 and settled in the merge:** Q1 B named a real nation and two real-world regions (written by role in the
   merge, `DEC-723`); Q2 C headed an excerpt "Raw output, whole" (relabeled); Q2 B labeled Gate 10 "N/A" (NOT RUN).
6. **Verdict levels settled by the merge rule, not by vote:** where a FAIL was not withdrawn in Round 3 it stands (Q3's Gates 4, 6 within
   the location, 11 and C); reader B of Q3 withdrew its Gate 7 share (31 of 86) for 27 of 85 = 31.8%.
7. **No repair was needed** in any sub-unit; no first version had to be kept.

## Questions filed
Q-288 to Q-339 filed as `DEC-1005` to `DEC-1056` (52), each PROVISIONAL on its recommended answer, in
`Cities/Research_Logs/DECISIONS_NEEDED_FROM_DEVELOPER.md`. **Next: `DEC-1057`.**

## Tokens
Round 1 and Round 3 (last figures) 4,898,380 (Q1 1,696,203 · Q2 1,431,326 · Q3 1,770,851); merge writer 512,336; **total 5,410,716**; web
calls 0. Rows in `TOKEN_LOG_Ariun_Nuur.md`.
