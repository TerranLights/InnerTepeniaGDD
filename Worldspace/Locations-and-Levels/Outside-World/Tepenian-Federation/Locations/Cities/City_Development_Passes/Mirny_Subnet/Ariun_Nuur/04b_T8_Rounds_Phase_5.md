# Ariun Nuur — ULM Phase 5 (relation and geometry) — T8 round record

**Unit:** Phase 5. **Written:** `04_Phase_05_Relation_and_Geometry.md` (722 lines; PROPOSED, not declared complete). **Run mode:** WARM (`DR-6`).
**Date:** 2026-11-19; brief frozen and readers dispatched 09:33, Round 1 back by 09:55, Round 3 by 10:02, merge
returned 10:18, record 10:20.
**List:** `.t8_required_04_Phase5.txt` (21 entries). The Pre-Trip's Phase 5 rows: Highways, Airports, the national network, Ports, the cross-subnet relationships file and the relationship database, each at its header and the lines naming this city (`DR-131` item 3; `DEC-664`), plus the grid-failure and national power-supply files (`DEC-705`); the spine's Phase 5, the runbook's Step 4 (cut), the spec, the earlier eight outputs, the Phase 5 datasheet and `DR-143`. **Refused and put to the developer:** the national-connections file (its own header states a method drawing on withheld megasheets and other cities' culture files). **Orchestrator facts:** the universe repo's routes README (a roster line), the geothermal file (this city not among its six), the withheld megasheet row. **Brief:** `.t8_brief_04_Phase5.md` (217
lines; built from the phase template; sha256[:16] 57be3cab25342cf7). Reader outputs archived as `.t8_Phase5_reader{A,B,C}.md`; Round 3
replies as `.t8_Phase5_round3_reader{A,B,C}.md`. Three Opus readers; one fresh Opus merge writer (`M-246`).

## Round 1 — receipts (as returned)

| Reader | Lines | Axis | Findings | Asymmetry rows | Handed forward | Positions | RF · SH · REQ · Q | Handoff places | Manifest |
|---|--:|---|--:|--:|--:|--:|---|--:|---|
| A | 694 | one road in, no network | 44 | 17 | 7 | 3 | 6 · 2 · 5 · 6 | 148 | 21 of 21 |
| B | 678 | necessary, and carried by one road | 31 | 13 | 7 | 3 | 9 · 3 · 10 · 7 | 144 | 21 of 21 |
| C | 678 | parented on paper, supplied by the road | 30 | 17 | 7 | 3 | 9 · 2 · 8 · 9 | 155 | 21 of 21 |

## Round 2 — `Tools/triple_read_verify.py` (last commit `8777bb5f` 2026-11-03; clean), run 1, raw output whole

```
required files: 21
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2662-2694,2696-2698,2700-2729,2731-2759] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 615-751] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Infrastructure/Highways.md  [range 1-10,156,162-163,170] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Infrastructure/Airports.md  [range 1-2,4-6,18,52,56] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Infrastructure/Arcanet.md  [range 1-11,26] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ⛔ QUOTE NOT IN ADMISSIBLE RANGE  (not found anywhere in this file - fabricated, sha1:3c636fbd523e)

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Infrastructure/Ports.md  [range 1-2,4,6-14,16-20,205,482,740] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Cross_Subnet_Relationships.md  [range 1-10,12-27,47,78,97-98,176,180,228] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Relationship_Database.md  [range 1-11,14,26,49,105,135,180,237,283-284,476-477,484,531] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Energy_Grid_Failure_Rationale.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ⛔ LMID  MISMATCH  claimed='this for the entire Antarctic grid, at a scale nothing else '  actual='infrastructure could replace.'

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/../Infrastructure/Amundsen_Power_Supply.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Ariun_Nuur.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.1_Step_MINUS-1_Input_Contract.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00_Frame.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/01_Inherited.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/03_Research.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_02_Composition_and_Arrival.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_03_Surface_and_Texture.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_04_Ordinary_Life.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/Datasheets/Phase_5.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 2058-2065] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
⛔ NOT UNANIMOUS - DO NOT WRITE. Log which agent/file failed and why.
```

**What failed, confirmed at source:** reader C's QUOTE for the national-network file dropped a word (*such*, L7) and its LMID for the grid file gave L72 for L73 (145 lines; middle (145+1)//2 = 73). C's first version kept as `.t8_Phase5_readerC_prerepair.md`; C corrected the two fields only (diff: L543, the QUOTE now one exact physical line, L8; L577).

**Run 2, raw output whole — UNANIMOUS:**

```
required files: 21
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2662-2694,2696-2698,2700-2729,2731-2759] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 615-751] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Infrastructure/Highways.md  [range 1-10,156,162-163,170] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Infrastructure/Airports.md  [range 1-2,4-6,18,52,56] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Infrastructure/Arcanet.md  [range 1-11,26] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Infrastructure/Ports.md  [range 1-2,4,6-14,16-20,205,482,740] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Cross_Subnet_Relationships.md  [range 1-10,12-27,47,78,97-98,176,180,228] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Relationship_Database.md  [range 1-11,14,26,49,105,135,180,237,283-284,476-477,484,531] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Energy_Grid_Failure_Rationale.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/../Infrastructure/Amundsen_Power_Supply.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Ariun_Nuur.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.1_Step_MINUS-1_Input_Contract.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00_Frame.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/01_Inherited.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/03_Research.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_02_Composition_and_Arrival.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_03_Surface_and_Texture.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_04_Ordinary_Life.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/Datasheets/Phase_5.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 2058-2065] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

## Round 3 — cross-check verdicts (the first two verdict lines of each reply)

| Reader | On | Verdict |
|---|---|---|
| A | B | CONSISTENT |
| A | C | CONSISTENT |
| B | A | CONSISTENT |
| B | C | CONSISTENT |
| C | A | CONSISTENT |
| C | B | CONSISTENT |

**All six CONSISTENT.** Reader A withdrew its reading of the national network line (L26, cut mid-sentence at the admitted span) as a fact of the height; the merge wrote the narrower forms settled in Round 3 (the relationship database's L180 is a stale route order in another location's entry, not used; the outpost's givers are inside the subnet, not *coastal*; chambers are not a written national requirement). The (c) points became Q-118 to Q-136. Filed as `DEC-799` to `DEC-817`.

## Procedural events (the recording law)

1. **Round 2 failed on its first run** (reader C, two fields; above), repaired and re-run UNANIMOUS (63/63).
2. **Reader A** ran `wc -l` on its own output (self-reported). **Reader B**, in Round 3, cited one line one off (research L445 for L444).
3. **The merge writer** re-read listed spans to settle points (Airports L18; relationship database L49, L135; cross-subnet L5–7, L97–98; Highways L156, L162–163); created no other file.
4. **The handoff audit now counts the sweep** (166 places against 3 outbound rows), the heading rule having been put into the brief and the merge instruction; Phases 3 and 4 keep their hand reconciliation.
5. Two readers' wordings in split notes were in quotation marks and were rewritten as italics by the orchestrator.

## Quotation checks, before this record existed

**Pre-check (T8 line 13), per quotation, normalized.** First run, raw:

```
quoted strings checked: 6 not found: 2
  MISS: singly connected
  MISS: from coastal cities of the subnet
04_Phase_05_Relation_and_Geometry.md British-form hits: []
other-location name scan (names: line numbers): {'Mirny': [8, 23, 237, 241, 244, 259, 263, 265, 275, 288, 347, 367, 377, 611, 701]}
tower-name count: 0
```

**Triage:** *singly connected* and *from coastal cities of the subnet* are readers' wordings quoted in split notes, not source text: **rewritten as italics** (two lines).

After the fix, raw:

```
quoted strings checked: 3 not found: 0
04_Phase_05_Relation_and_Geometry.md British-form hits: []
other-location name scan (names: line numbers): {'Mirny': [8, 23, 237, 241, 244, 259, 263, 265, 275, 288, 347, 367, 377, 611, 701]}
tower-name count: 0
```

**`Tools/quotation_audit.py`** (last commit `5a63e074` 2026-11-02; clean), `--phase 5 --own-pass`. Whole output saved beside this record
as `.t8_Phase5_quotation_audit.txt`; result block, raw:

```
=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 1
NOT FOUND in corpus: 1
  of those, in TABLE CELLS : 0
  of those, in PROSE       : 1

  [04_Phase_05_Relation_and_Geometry.md:627]           names a round 3 confirmation at source, or an agreement on substance

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```

**Triage:** the one hit is the file's legend sentence (L627). **Confirmed defects: 0.**

## Phase-close instruments (raw output whole)

**`Tools/handoff_audit.py`** (T1):

```
pass audited : Ariun_Nuur
phase files  : 4

=== CONTROLS (edit these per pass; they are what makes a zero trustworthy) ===
  PHASES WITH A FORMAL SWEEP BLOCK (found in this pass): 2, 3, 4, 5
  PHASES WITH NO TRACE OF A SWEEP (found in this pass)  : none
  SELF-TEST (fixed positive and negative strings)       : passed
  INSTRUMENT VALID: YES - the detector separates a formal block from no block on the built-in controls

  phase | outbound | sweep    | rows | verdict
  ------+----------+----------+------+---------
      2 |        0 | FORMAL   |    0 | n/a - nothing addressed to it
      3 |        1 | FORMAL   |    0 | *** BLOCK EMPTY ***
      4 |        2 | FORMAL   |    0 | *** BLOCK EMPTY ***
      5 |        3 | FORMAL   |  166 | reconcile 166 enumerated against 3 outbound

TOTAL outbound handoff rows: 19
PHASES WITH ROWS ADDRESSED TO THEM AND NO ENUMERATION: 2

=== outbound rows, per target, for hand reconciliation ===
  -> Phase 3:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 3** | the founding wave's specialization, its criterion and its losing side (R
  -> Phase 4:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 4** | whose ordinary day: the arrival layers (founding-wave descendants, later
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 4** | the street register as the general answer, for whose ordinary day (FIND-
  -> Phase 5:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 5** | who the visitor is: Hwy 37 as the only written route of arrival, departu
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 5** | first impressions as the city's arrival texture (FIND-P3-34 to FIND-P3-4
       [04_Phase_04_Ordinary_Life.md]  | **Phase 5** | the supply window and the forecast, and Hwy 37's seasons (FIND-P4-16; re
  -> Phase 6:
       [04_Phase_04_Ordinary_Life.md]  | **Phase 6** | the keepers' off-rhythm day (FIND-P4-8, FIND-P4-42); whoever keeps her o
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 6** | the outsider senses that are conditions (FIND-P5-34): the newcomer not y
  -> Phase 7:
       [04_Phase_04_Ordinary_Life.md]  | **Phase 7** | any rule protecting rest where the work never stops, limiting outdoor st
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 7** | any rule of travel on Hwy 37 in a seasonal closure, if it holds (FIND-P5
  -> Phase 8:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 8** | composition established: the origin stocks as admissible, composition-gr
  -> Phase 9:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 9** | which populations exist: 25 rows, both bodies at their own counts, the h
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 9** | the sensory split by body: breath, thin air and smell for humans; capaci
       [04_Phase_04_Ordinary_Life.md]  | **Phase 9** | the two bodies' days (FIND-P4-44); the human night at about 3,900 m by m
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 9** | the arrival types by body and route, and their unsized layers, the resea
  -> Phase 10:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 10** | the district's honor of the city's own scientists (FIND-P2-37); the fou
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 10** | the named structures and their texture: the shaft as an interior kept f
       [04_Phase_04_Ordinary_Life.md]  | **Phase 10** | the charge night and the clock as the day's frame, and the warm stop as
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 10** | the road's name (the Mountain Cut Throughway), the waypoint, its outpos
```

**`Tools/phase_discipline_check.py`** (T3, T4, T5), run before the ledger was updated:

```
pass audited : Ariun_Nuur

=== T3 - POSITION-COVERAGE LEDGER ===
  phases in header: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Child              filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Lover (position)   filled=1  blank=8   blank at: P3, P4, P5, P6, P7, P8, P9, P10
  The Parent             filled=1  blank=8   blank at: P3, P4, P5, P6, P7, P8, P9, P10
  The Ruler              filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Elder              filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Mentor             filled=2  blank=7   blank at: P3, P5, P6, P7, P8, P9, P10
  The Passer-Through     filled=2  blank=7   blank at: P4, P5, P6, P7, P8, P9, P10
  The Neighbor           filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  ⭐ The Lover FACULTY    filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10

  NOTE: a blank cell is a WARNING BEFORE Step 8, not a defect. Do not
  fill a blank by writing new phase content toward it - that is the
  contamination 00f Rule 3 forbids (see the recipe's hard bound on T3).

=== T4 - PER-PHASE SHED MARKER ===
  [04_Phase_02_Composition_and_Arrival.md]  T4 present: the origin stocks' own cultures, the per-row decimals and headcounts below the tier, the l
  [04_Phase_03_Surface_and_Texture.md]  T4 present: the composition's rows, tiers, stocks and decimals, the language blocs, the census arithme
  [04_Phase_04_Ordinary_Life.md]  T4 present: the composition's rows, tiers, decimals and origin shares, the founders' share beyond its 
  [04_Phase_05_Relation_and_Geometry.md]  T4 present: the composition's rows, tiers and decimals, the language blocs, the census-kinship reasoni

  4/4 phase files carry a T4 marker.
  >> If EVERY phase's answer was literally 'nothing', T4 is falsified
     per its own stated condition (the question would be decorative).
     This tool cannot see the marker's CONTENT well enough to judge
     that - read the 4 lines above by hand.

=== T5 - EARLY LOVER-FACULTY SMOKE TEST ===
  EARLY marker absent in (no Phase 6 file found)
  LATE marker absent (08_Review_Panel.md missing or has no 'T5 - LATE LOVER FACULTY:' line yet)

  T5 not fully applied this pass (one or both markers absent).
```

**Ledger:** P5 marked for the Mentor, the Passer-Through and the Neighbor.

## American English sweep and the one-location check

From the pre-check script's last lines, raw, above: no British form; the name scan's hits, if any, are the parent subnet and the pass
folder's path; the tower's name 0. **No other location named.**

## Tokens (from the task notifications; full rows in `Universal_Location_Methodology/TOKEN_LOG_Ariun_Nuur.md`)

| Agent | Round 1 | Round 3 (delta) | Last figure |
|---|--:|--:|--:|
| reader A | 605,900 | 84,246 | 690,146 |
| reader B | 614,411 | 83,194 | 697,605 |
| reader C | 634,763 | 83,347 (repair 1,741 before it) | 719,851 |
| merge writer | — | — | 308,193 |
| **Unit total (sum of last figures)** | | | **2,415,795** |

Web calls: readers 0; `Tools/web_quota_count.py`: TOTAL 284 (unchanged).
**The record grows after this check** (T8 line 8): no DOUBLE-CHECK script was run on this record.
