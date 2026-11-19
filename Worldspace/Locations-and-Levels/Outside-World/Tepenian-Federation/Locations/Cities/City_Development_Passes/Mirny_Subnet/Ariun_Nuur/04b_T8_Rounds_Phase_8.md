# Ariun Nuur — ULM Phase 8 (making) — T8 round record

**Unit:** Phase 8. **Written:** `04_Phase_08_Making.md` (503 lines; PROPOSED, not declared complete). **Run mode:** WARM (`DR-6`).
**Date:** 2026-11-19; brief frozen and readers dispatched 11:44, Round 1 back by 12:02, Round 3 by 12:06, merge
returned 12:17, record 12:19.
**List:** `.t8_required_04_Phase8.txt` (18 entries). The runbook's Step 4 (cut), the spine's Phase 8, the robot physiology file (whole; governing; its lines naming other locations read as national canon only, as Step 0 and Phase 4 set it, the rule now naming the file), the weapons and tools philosophy, the spec, the earlier eleven outputs, the Phase 8 datasheet and `DR-143`. **Orchestrator facts:** gear catalogs and slang (no path; the draft's unsourced gating line was rewritten before freezing to claim only what the files give; slang waits for the CST, `DR-140` item 2). **Brief:** `.t8_brief_04_Phase8.md` (204
lines; built from the phase template; sha256[:16] e28d1b08271cb2f6). Reader outputs archived as `.t8_Phase8_reader{A,B,C}.md`; Round 3
replies as `.t8_Phase8_round3_reader{A,B,C}.md`. Three Opus readers; one fresh Opus merge writer (`M-246`).

## Round 1 — receipts (as returned)

| Reader | Lines | Axis | Findings | Asymmetry rows | Handed forward | Positions | RF · SH · REQ · Q | Handoff places | Manifest |
|---|--:|---|--:|--:|--:|--:|---|--:|---|
| A | 468 | made in paid heat, kept in free cold | 32 | 11 | 5 | 1 | 8 · 2 · 6 · 5 | 32 | 18 of 18 |
| B | 714 | made at the warm stop, from what the road brings | 34 | 9 | 5 | 1 | 7 · 2 · 6 · 5 | 28 | 18 of 18 |
| C | 455 | carried in, kept frozen, paid for in heat | 22 | 14 | 5 | 1 | 9 · 2 · 6 · 6 | 32 | 18 of 18 |

## Round 2 — `Tools/triple_read_verify.py` (last commit `8777bb5f` 2026-11-03; clean), run 1, raw output whole

```
required files: 18
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2662-2694,2696-2698,2700-2729,2731-2759] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 955-1025] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Weapons_and_Tools_Philosophy.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_07_Order.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/Datasheets/Phase_8.md ===
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

**All six CONSISTENT.** Each reader read both other outputs in full. Settled for the merge: coolant's make-up is not written (every such claim conditional); no admitted line writes ice used to make anything (C withdrew); keeping is written, mending is not; tongues are written by row, never as language names built from a nationality (A's wording corrected); the datasheet's L15 pointer is the quick-reference sheet's line (a request). The (c) points became Q-170 to Q-183. Filed as `DEC-851` to `DEC-864`.

## Procedural events (the recording law)

1. **Round 2 passed on its first run** (54/54); the exact-field check compared 108 first and last line fields, 0 differ (`.t8_Phase8_exact_fields.txt`).
2. **Command slips, self-reported:** reader C (a `wc -l` glob that counted this pass's own round-record files, counts only; one `grep -o` on piped `sed` output of a listed line; `wc -l` and `tail -c` on its own output); reader B (`grep -c` on the spec; `tail -c` on the spec and the datasheet). No finding rests on any of them; none touched an unlisted file's content or another location.
3. **The merge writer** opened no listed file (every point settled from the outputs and replies) and created no other file.
4. **Before this unit froze** (logged at the time): the draft's gear-catalog gating line had no canon source and was rewritten; the template's other-location rule was made to name the physiology file.

## Quotation checks, before this record existed

**Pre-check (T8 line 13), per quotation, normalized.** First run, raw:

```
quoted strings checked: 0 not found: 0
04_Phase_08_Making.md British-form hits: []
other-location name scan (names: line numbers): {}
tower-name count: 0
```

**Triage:** no quotation-marked strings in the file (every wording in italics).

**`Tools/quotation_audit.py`** (last commit `5a63e074` 2026-11-02; clean), `--phase 8 --own-pass`. Whole output saved beside this record
as `.t8_Phase8_quotation_audit.txt`; result block, raw:

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
phase files  : 7

=== CONTROLS (edit these per pass; they are what makes a zero trustworthy) ===
  PHASES WITH A FORMAL SWEEP BLOCK (found in this pass): 2, 3, 4, 5, 6, 7, 8
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
      8 |        2 | FORMAL   |   49 | reconcile 49 enumerated against 2 outbound

TOTAL outbound handoff rows: 27
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
       [04_Phase_08_Making.md]  | **Phase 9** | food by body: siligel and charge from the supply and the shipment for th
  -> Phase 10:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 10** | the district's honor of the city's own scientists (FIND-P2-37); the fou
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 10** | the named structures and their texture: the shaft as an interior kept f
       [04_Phase_04_Ordinary_Life.md]  | **Phase 10** | the charge night and the clock as the day's frame, and the warm stop as
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 10** | the road's name (the Mountain Cut Throughway), the waypoint, its outpos
       [04_Phase_06_Meaning.md]  | **Phase 10** | the district's honor, the city's own half as the ground (FIND-P6-3; swe
       [04_Phase_07_Order.md]  | **Phase 10** | the decisions that fall on unnamed parties, as candidate places or name
       [04_Phase_08_Making.md]  | **Phase 10** | the named things of making, as candidates only, PROPOSED: the inherited
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
  The Mentor             filled=5  blank=4   blank at: P3, P8, P9, P10
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
  [04_Phase_08_Making.md]  T4 present: the industry tiers beyond the food term, the baseline, the robot term and the Other 10%, t

  7/7 phase files carry a T4 marker.
  >> If EVERY phase's answer was literally 'nothing', T4 is falsified
     per its own stated condition (the question would be decorative).
     This tool cannot see the marker's CONTENT well enough to judge
     that - read the 7 lines above by hand.

=== T5 - EARLY LOVER-FACULTY SMOKE TEST ===
  EARLY (Phase 6) verdict: alive, yes; lovable, not yet shown. It is alive in a hard way: everyone who comes is kept and taught by the one before, told where it is safe to stop, and what you know outlives you only if you give it away. Someone could be loyal to it and grateful to it before the files give anyone a reason to love it: no child, no elder, no grave and no pleasure in a stopped hour is written yet, the one beauty given is the air's glitter in the light season (Phase 3 FIND-P3-37), and what people do with the warmth waits for the CST. (Split 10: reader C's wider verdict, lovable for its seriousness and its debt, is not written.)
  LATE marker absent (08_Review_Panel.md missing or has no 'T5 - LATE LOVER FACULTY:' line yet)

  T5 not fully applied this pass (one or both markers absent).
```

**Ledger:** P8 marked for the Mentor.

## American English sweep and the one-location check

From the pre-check script's last lines, raw, above: no British form; the name scan's hits, if any, are the parent subnet and the pass
folder's path; the tower's name 0. **No other location named.**

## Tokens (from the task notifications; full rows in `Universal_Location_Methodology/TOKEN_LOG_Ariun_Nuur.md`)

| Agent | Round 1 | Round 3 (delta) | Last figure |
|---|--:|--:|--:|
| reader A | 746,393 | 84,421 | 830,814 |
| reader B | 775,394 | 77,394 | 852,788 |
| reader C | 757,348 | 84,354 | 841,702 |
| merge writer | — | — | 249,905 |
| **Unit total (sum of last figures)** | | | **2,775,209** |

Web calls: readers 0; `Tools/web_quota_count.py`: TOTAL 284 (unchanged).
**The record grows after this check** (T8 line 8): no DOUBLE-CHECK script was run on this record.
