# Ariun Nuur — ULM Phase 7 (order) — T8 round record

**Unit:** Phase 7. **Written:** `04_Phase_07_Order.md` (1156 lines; PROPOSED, not declared complete). **Run mode:** WARM (`DR-6`).
**Date:** 2026-11-19; brief frozen and readers dispatched 10:58, Round 1 back by 11:21, Round 3 by 11:26, merge
returned 11:43, record 11:44.
**List:** `.t8_required_04_Phase7.txt` (19 entries). The runbook's Step 4 (cut), the spine's Phase 7, the Division of Industry README (22 spans) and the per-city three-tier run (`16`, at Step 2's spans), the national medical and care institutes (city lines cut), the national economy file, the spec, the earlier ten outputs, the Phase 7 datasheet and `DR-143`. **Orchestrator facts:** the factions folder (the city's entry defers it on grounds this pass does not admit) and the factions deferral itself (`DR-58`, rulings log L1166, added before freezing); the professions and megacorporations folders (zero lines); the logistics file (another location). Government and justice wait for the DCI (`DR-137` item 11). **Brief:** `.t8_brief_04_Phase7.md` (218
lines; built from the phase template; sha256[:16] 8cc5a27f63557fe4). Reader outputs archived as `.t8_Phase7_reader{A,B,C}.md`; Round 3
replies as `.t8_Phase7_round3_reader{A,B,C}.md`. Three Opus readers; one fresh Opus merge writer (`M-246`).

## Round 1 — receipts (as returned)

| Reader | Lines | Axis | Findings | Asymmetry rows | Handed forward | Positions | RF · SH · REQ · Q | Handoff places | Manifest |
|---|--:|---|--:|--:|--:|--:|---|--:|---|
| A | 606 | an order that cannot exclude: it keeps, teaches, and waits on what it cannot make | 37 | 21 | 5 | 1 | 12 · 4 · 9 · 9 | 66 | 19 of 19 |
| B | 578 | an order that cannot send anyone away | 31 | 23 | 6 | 1 | 12 · 4 · 7 · 9 | 54 | 19 of 19 |
| C | 556 | no one can be sent out, and no one holds the whole | 25 | 25 | 5 | 1 | 12 · 2 · 8 · 9 | 63 | 19 of 19 |

## Round 2 — `Tools/triple_read_verify.py` (last commit `8777bb5f` 2026-11-03; clean), run 1, raw output whole

```
required files: 19
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2662-2694,2696-2698,2700-2729,2731-2759] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 841-954] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/README.md  [range 1-38,40-45,47-58,60-84,86-106,111-120,122-126,128-133,135,137-154,160-174,177-185,187-188,190,193,196,199-204,206-212,215-216,218,220-221,223-227] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/16_Per_City_Three_Tier_Run.md  [range 1-12,21-33,72-77,79,81-85,122-128,130-136,139-141,241-248,282,2349-2358] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/National_Medical_and_Care_Institutes.md  [range 1-15,17-22,25-28,30,32-35,37,39-49,51,53-56,59-68,70-73,75,77-80,82-88,90-91,93-96,100-101,103-105,108,111-112,114-135,138-140,142-167,169-172,175,177-183,185-189,191-202,204-208,210-223,226-230,232-245] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/National_Economy_and_Currency.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_05_Relation_and_Geometry.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_06_Meaning.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/Datasheets/Phase_7.md ===
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

**All six CONSISTENT.** Each reader read both other outputs in full. Settled for the merge: no sector headcount is cited as a finding (the spine's Q-40 stands on its recommended answer); the science count is not the research population; *character budget* names two tiers (reader A withdrew a citation); reader C's treaty-ban prohibition rests on a reported gloss and is not used; the forfeiture is a consequence, not a prohibition; no robot recovery duration is written; nothing forecasts the DCI. The (c) points became Q-151 to Q-169. Filed as `DEC-832` to `DEC-850`.

## Procedural events (the recording law)

1. **Round 2 passed on its first run** (57/57). **A new orchestrator check** followed Phase 6's finding that the checker normalizes emphasis marks: `<scratchpad>/t8/exact_fields.py` compares every L1 and LLAST exactly against the source. 114 fields, 0 differ. Output archived as `.t8_Phase7_exact_fields.txt`.
2. **Readers' reading logs** gave the README's span count as 26 (A), 22 (B) and 25 (C); the list gives 22. Every LINES figure (194) is right, so it touches the logs only.
3. **The merge writer** re-read listed spans only (the datasheet, spec L143–180, Phase 6 L432–434), created no other file, and wrote reader B's narrowest axis wording, PROVISIONAL.
4. **Orchestrator self-corrections while this unit ran** (drafts for later phases, no frozen file touched): the Phase 8 draft's line that gear catalogs are gated until the 38-city corpus is done had no canon source and was rewritten; the brief template's other-location rule now names the robot physiology file, as Step 0 and Phase 4 handled it.

## Quotation checks, before this record existed

**Pre-check (T8 line 13), per quotation, normalized.** First run, raw:

```
quoted strings checked: 3 not found: 0
04_Phase_07_Order.md British-form hits: []
other-location name scan (names: line numbers): {}
tower-name count: 0
```

**Triage:** three quoted strings, all found at source. No fix.

**`Tools/quotation_audit.py`** (last commit `5a63e074` 2026-11-02; clean), `--phase 7 --own-pass`. Whole output saved beside this record
as `.t8_Phase7_quotation_audit.txt`; result block, raw:

```
=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 0
NOT FOUND in corpus: 0
  of those, in TABLE CELLS : 0
  of those, in PROSE       : 0


⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```

**Triage:** no fragment tested. **Confirmed defects: 0.**

## Phase-close instruments (raw output whole)

**`Tools/handoff_audit.py`** (T1):

```
pass audited : Ariun_Nuur
phase files  : 6

=== CONTROLS (edit these per pass; they are what makes a zero trustworthy) ===
  PHASES WITH A FORMAL SWEEP BLOCK (found in this pass): 2, 3, 4, 5, 6, 7
  PHASES WITH NO TRACE OF A SWEEP (found in this pass)  : none
  SELF-TEST (fixed positive and negative strings)       : passed
  INSTRUMENT VALID: YES - the detector separates a formal block from no block on the built-in controls

  phase | outbound | sweep    | rows | verdict
  ------+----------+----------+------+---------
      2 |        0 | FORMAL   |    0 | n/a - nothing addressed to it
      3 |        1 | FORMAL   |    0 | *** BLOCK EMPTY ***
      4 |        2 | FORMAL   |    0 | *** BLOCK EMPTY ***
      5 |        3 | FORMAL   |  166 | reconcile 166 enumerated against 3 outbound
      6 |        2 | FORMAL   |   33 | reconcile 33 enumerated against 2 outbound
      7 |        3 | FORMAL   |   86 | reconcile 86 enumerated against 3 outbound

TOTAL outbound handoff rows: 25
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
       [04_Phase_06_Meaning.md]  | **Phase 7** | any rule, priority or prohibition the contract or the failure would need
  -> Phase 8:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 8** | composition established: the origin stocks as admissible, composition-gr
       [04_Phase_07_Order.md]  | **Phase 8** | the people the place's demand does not fit, as persons, never groups (FI
  -> Phase 9:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 9** | which populations exist: 25 rows, both bodies at their own counts, the h
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 9** | the sensory split by body: breath, thin air and smell for humans; capaci
       [04_Phase_04_Ordinary_Life.md]  | **Phase 9** | the two bodies' days (FIND-P4-44); the human night at about 3,900 m by m
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 9** | the arrival types by body and route, and their unsized layers, the resea
       [04_Phase_06_Meaning.md]  | **Phase 9** | who the contract's two layers reach and who they do not (FIND-P6-8, FIND
       [04_Phase_07_Order.md]  | **Phase 9** | who is present by function and body: the night's keepers and how many (h
  -> Phase 10:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 10** | the district's honor of the city's own scientists (FIND-P2-37); the fou
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 10** | the named structures and their texture: the shaft as an interior kept f
       [04_Phase_04_Ordinary_Life.md]  | **Phase 10** | the charge night and the clock as the day's frame, and the warm stop as
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 10** | the road's name (the Mountain Cut Throughway), the waypoint, its outpos
       [04_Phase_06_Meaning.md]  | **Phase 10** | the district's honor, the city's own half as the ground (FIND-P6-3; swe
       [04_Phase_07_Order.md]  | **Phase 10** | the decisions that fall on unnamed parties, as candidate places or name
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
  The Mentor             filled=4  blank=5   blank at: P3, P7, P8, P9, P10
  The Passer-Through     filled=3  blank=6   blank at: P4, P6, P7, P8, P9, P10
  The Neighbor           filled=1  blank=8   blank at: P2, P3, P4, P6, P7, P8, P9, P10
  ⭐ The Lover FACULTY    filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10

  NOTE: a blank cell is a WARNING BEFORE Step 8, not a defect. Do not
  fill a blank by writing new phase content toward it - that is the
  contamination 00f Rule 3 forbids (see the recipe's hard bound on T3).

=== T4 - PER-PHASE SHED MARKER ===
  [04_Phase_02_Composition_and_Arrival.md]  T4 present: the origin stocks' own cultures, the per-row decimals and headcounts below the tier, the l
  [04_Phase_03_Surface_and_Texture.md]  T4 present: the composition's rows, tiers, stocks and decimals, the language blocs, the census arithme
  [04_Phase_04_Ordinary_Life.md]  T4 present: the composition's rows, tiers, decimals and origin shares, the founders' share beyond its 
  [04_Phase_05_Relation_and_Geometry.md]  T4 present: the composition's rows, tiers and decimals, the language blocs, the census-kinship reasoni
  [04_Phase_06_Meaning.md]  T4 present: the climate cells beyond the cold that punishes stopping, the industry figures and the Man
  [04_Phase_07_Order.md]  T4 present: the composition's rows, tiers, decimals and per-row headcounts beyond the two bodies, the 

  6/6 phase files carry a T4 marker.
  >> If EVERY phase's answer was literally 'nothing', T4 is falsified
     per its own stated condition (the question would be decorative).
     This tool cannot see the marker's CONTENT well enough to judge
     that - read the 6 lines above by hand.

=== T5 - EARLY LOVER-FACULTY SMOKE TEST ===
  EARLY (Phase 6) verdict: alive, yes; lovable, not yet shown. It is alive in a hard way: everyone who comes is kept and taught by the one before, told where it is safe to stop, and what you know outlives you only if you give it away. Someone could be loyal to it and grateful to it before the files give anyone a reason to love it: no child, no elder, no grave and no pleasure in a stopped hour is written yet, the one beauty given is the air's glitter in the light season (Phase 3 FIND-P3-37), and what people do with the warmth waits for the CST. (Split 10: reader C's wider verdict, lovable for its seriousness and its debt, is not written.)
  LATE marker absent (08_Review_Panel.md missing or has no 'T5 - LATE LOVER FACULTY:' line yet)

  T5 not fully applied this pass (one or both markers absent).
```

**Ledger:** P7 marked for the Mentor.

## American English sweep and the one-location check

From the pre-check script's last lines, raw, above: no British form; the name scan's hits, if any, are the parent subnet and the pass
folder's path; the tower's name 0. **No other location named.**

## Tokens (from the task notifications; full rows in `Universal_Location_Methodology/TOKEN_LOG_Ariun_Nuur.md`)

| Agent | Round 1 | Round 3 (delta) | Last figure |
|---|--:|--:|--:|
| reader A | 760,025 | 106,011 | 866,036 |
| reader B | 731,156 | 102,766 | 833,922 |
| reader C | 742,840 | 112,383 | 855,223 |
| merge writer | — | — | 334,283 |
| **Unit total (sum of last figures)** | | | **2,889,464** |

Web calls: readers 0; `Tools/web_quota_count.py`: TOTAL 284 (unchanged).
**The record grows after this check** (T8 line 8): no DOUBLE-CHECK script was run on this record.
