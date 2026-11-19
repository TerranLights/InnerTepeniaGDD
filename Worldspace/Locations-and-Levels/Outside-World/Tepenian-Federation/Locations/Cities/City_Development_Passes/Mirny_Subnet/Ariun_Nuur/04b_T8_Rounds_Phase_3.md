# Ariun Nuur — ULM Phase 3 (surface and texture) — T8 round record

**Unit:** Phase 3. **Written:** `04_Phase_03_Surface_and_Texture.md` (547 lines; PROPOSED, not declared complete). **Run mode:** WARM
(`DR-6`). **Date:** 2026-11-19; brief frozen and readers dispatched 08:15, Round 1 back by 08:32, Round 3 by 08:35, merge returned 08:51,
record 08:53.
**List:** `.t8_required_04_Phase3.txt` (12 entries): the Pre-Trip's Phase 3 rows (the climate record; the spec), the spine's Phase 3, the
runbook's Step 4 (lines naming other locations cut), the earlier six outputs, the Phase 3 datasheet and `DR-143`. **Orchestrator facts in
the brief:** the concept-art folder holds only `.gitkeep` (listed by the orchestrator: opened and empty is a result); the physical-
infrastructure megasheet row withheld; the research folder for another location not applicable. **Brief:** `.t8_brief_04_Phase3.md` (206
lines; sha256[:16] e4c05fdb1a052613). Reader outputs archived as `.t8_Phase3_reader{A,B,C}.md`; Round 3 replies as
`.t8_Phase3_round3_reader{A,B,C}.md`. Three Opus readers; one fresh Opus merge writer (`M-246`).

## Round 1 — receipts (as returned)

| Reader | Lines | Axis | Findings | Asymmetry rows | Handed forward | Positions | RF · SH · REQ · Q | Handoff places | Manifest |
|---|--:|---|--:|--:|--:|--:|---|--:|---|
| A | 428 | clear-sky snow, made warmth | 51 | 5 | 7 | 2 | 6 · 2 · 4 · 6 | 29 | 12 of 12 |
| B | 458 | snow without weather | 49 | 7 | 6 | 1 | 7 · 1 · 4 · 7 | 36 | 12 of 12 |
| C | 478 | silent sky, audible upkeep | 40 | 3 | 7 | 2 | 6 · 1 · 8 · 5 | 36 | 12 of 12 |

## Round 2 — `Tools/triple_read_verify.py` (last commit `8777bb5f` 2026-11-03; clean), first run, raw output whole

```
required files: 12
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2662-2694,2696-2698,2700-2729,2731-2759] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 472-533] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Climate Data/READER/Vostok.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/Datasheets/Phase_3.md ===
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

**All six CONSISTENT; no repair.** B withdrew its "no" to the peer-free test; the merge wrote the narrower form of three overreaches (the
lake does not make the plain featureless; breath freezes at the record cold only; only the halos are written as solar). The (c) points
became Q-85 to Q-101, filed as `DEC-766` to `DEC-782`.

## Procedural events (the recording law)

1. **Reader A** piped `sed` through `cat -A`, `cut` and `head` for display; **reader C** ran `wc -l` on its own output and fixed a log fragment
   it had left on its last QUOTE line. Self-reported; no content effect.
2. **The merge writer** re-read two listed spans (research L196–221; spec L9) to settle points; created no other file.
3. **The handoff audit's "BLOCK EMPTY" for Phase 3** (below) is a format artifact: the tool counts table rows, and the phase's sweep is a
   numbered list. By hand, Phase 2's one row handed to Phase 3 (its HANDED FORWARD L342) is discharged at sweep place 27. The merge brief
   for later phases asks for the sweep as a table.

## Quotation checks, before this record existed

**Pre-check (T8 line 13), per quotation, normalized.** First run, raw:

```
quoted strings checked: 25 not found: 1
  MISS: not by rot
04_Phase_03_Surface_and_Texture.md British-form hits: []
other-location name scan (names: line numbers): {'Mirny': [3]}
tower-name count: 0
```

**Triage:** *not by rot* is a reader's inference (Round 3 said so), not a source quotation: **rewritten as italics** (one line). After the
fix, raw:

```
quoted strings checked: 24 not found: 0
04_Phase_03_Surface_and_Texture.md British-form hits: []
other-location name scan (names: line numbers): {'Mirny': [3]}
tower-name count: 0
```

**`Tools/quotation_audit.py`** (last commit `5a63e074` 2026-11-02; clean), `--phase 3 --own-pass`. Whole output saved beside this record as
`.t8_Phase3_quotation_audit.txt`; result block, raw:

```
=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 10
NOT FOUND in corpus: 1
  of those, in TABLE CELLS : 0
  of those, in PROSE       : 1

  [04_Phase_03_Surface_and_Texture.md:414]           names a reader who checked it at its source in round 3, or the merge writer at a listed line

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```

**Triage:** the one hit is the file's own legend sentence (L414). **Confirmed defects: 0 (CELL 0, PROSE 0).**

## Phase-close instruments (raw output whole)

**`Tools/handoff_audit.py`** (T1):

```
pass audited : Ariun_Nuur
phase files  : 2

=== CONTROLS (edit these per pass; they are what makes a zero trustworthy) ===
  PHASES WITH A FORMAL SWEEP BLOCK (found in this pass): 2, 3
  PHASES WITH NO TRACE OF A SWEEP (found in this pass)  : none
  SELF-TEST (fixed positive and negative strings)       : passed
  INSTRUMENT VALID: YES - the detector separates a formal block from no block on the built-in controls

  phase | outbound | sweep    | rows | verdict
  ------+----------+----------+------+---------
      2 |        0 | FORMAL   |    0 | n/a - nothing addressed to it
      3 |        1 | FORMAL   |    0 | *** BLOCK EMPTY ***

TOTAL outbound handoff rows: 10
PHASES WITH ROWS ADDRESSED TO THEM AND NO ENUMERATION: 1

=== outbound rows, per target, for hand reconciliation ===
  -> Phase 3:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 3** | the founding wave's specialization, its criterion and its losing side (R
  -> Phase 4:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 4** | whose ordinary day: the arrival layers (founding-wave descendants, later
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 4** | the street register as the general answer, for whose ordinary day (FIND-
  -> Phase 5:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 5** | who the visitor is: Hwy 37 as the only written route of arrival, departu
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 5** | first impressions as the city's arrival texture (FIND-P3-34 to FIND-P3-4
  -> Phase 8:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 8** | composition established: the origin stocks as admissible, composition-gr
  -> Phase 9:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 9** | which populations exist: 25 rows, both bodies at their own counts, the h
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 9** | the sensory split by body: breath, thin air and smell for humans; capaci
  -> Phase 10:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 10** | the district's honor of the city's own scientists (FIND-P2-37); the fou
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 10** | the named structures and their texture: the shaft as an interior kept f
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
  The Mentor             filled=1  blank=8   blank at: P3, P4, P5, P6, P7, P8, P9, P10
  The Passer-Through     filled=1  blank=8   blank at: P3, P4, P5, P6, P7, P8, P9, P10
  The Neighbor           filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  ⭐ The Lover FACULTY    filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10

  NOTE: a blank cell is a WARNING BEFORE Step 8, not a defect. Do not
  fill a blank by writing new phase content toward it - that is the
  contamination 00f Rule 3 forbids (see the recipe's hard bound on T3).

=== T4 - PER-PHASE SHED MARKER ===
  [04_Phase_02_Composition_and_Arrival.md]  T4 present: the origin stocks' own cultures, the per-row decimals and headcounts below the tier, the l
  [04_Phase_03_Surface_and_Texture.md]  T4 present: the composition's rows, tiers, stocks and decimals, the language blocs, the census arithme

  2/2 phase files carry a T4 marker.
  >> If EVERY phase's answer was literally 'nothing', T4 is falsified
     per its own stated condition (the question would be decorative).
     This tool cannot see the marker's CONTENT well enough to judge
     that - read the 2 lines above by hand.

=== T5 - EARLY LOVER-FACULTY SMOKE TEST ===
  EARLY marker absent in (no Phase 6 file found)
  LATE marker absent (08_Review_Panel.md missing or has no 'T5 - LATE LOVER FACULTY:' line yet)

  T5 not fully applied this pass (one or both markers absent).
```

**Ledger:** P3 marked for the Passer-Through (the arrival's view); the Mentor contested (Q-100), the Elder and the Lover faculty open
(Q-101), left blank.

## American English sweep and the one-location check

From the same script, raw: `04_Phase_03_Surface_and_Texture.md British-form hits: []`; `other-location name scan (names: line numbers):
{'Mirny': [3]}`; `tower-name count: 0`. The one hit is the pass folder's path. **No other location named.**

## Tokens (from the task notifications; full rows in `Universal_Location_Methodology/TOKEN_LOG_Ariun_Nuur.md`)

| Agent | Round 1 | Round 3 (delta) | Last figure |
|---|--:|--:|--:|
| reader A | 452,859 | 74,523 | 527,382 |
| reader B | 462,922 | 74,405 | 537,327 |
| reader C | 464,751 | 72,684 | 537,435 |
| merge writer | — | — | 277,595 |
| **Unit total (sum of last figures)** | | | **1,879,739** |

Web calls: readers 0; `Tools/web_quota_count.py`: TOTAL 284 (unchanged).
**The record grows after this check** (T8 line 8): no DOUBLE-CHECK script was run on this record.
