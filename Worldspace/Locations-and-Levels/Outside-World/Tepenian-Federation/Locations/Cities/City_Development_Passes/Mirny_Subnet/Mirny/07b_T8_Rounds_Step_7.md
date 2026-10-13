# Mirny — Step 7 · QA (the 17 gates) · T8 round record

**Pass:** Mirny · ULM · Step 7 · 2026-10-12 (unattended run, then continued with the developer awake).
- **Clock checks:** 06:45 (list verified, brief written, Round 1 dispatched) · ~08:20 (usage-limit error cut off all three readers; A 15 gates, B 14, C 12 written) · 10:21 (limit reset; all three resumed by `SendMessage`) · 10:28–10:35 (A, B, C finished) · 10:36 (Round 2) · 10:37–10:43 (Round 3, three replies) · ~10:45 (merge body written; `assemble_qa7.py`) · 10:46 onward (audits, this record).
- **Files:** written `07_QA_Gates.md` (2025 lines: the merged QA block, errata, flags, and §6 raw scan output extracted verbatim from the readers' blocks), this record. List `.t8_required_07_Step7.txt` (30 entries, 9,928 admitted lines, 0 bad); brief `.t8_Step7_brief.md` (final at dispatch); readers `.t8_Step7_reader{A,B,C}.md` (1,704 · 1,776 · 1,360 lines; 30 PROOF each); Round 3 replies `.t8_Step7_round3_reader{A,B,C}.md`; Round 2 raw `.t8_Step7_round2_raw.txt`; merge body `.t8_Step7_merge_body.md`; `assemble_qa7.py`.

## Round 1 — what each reader found
| Reader | Distinctive |
|---|---|
| A | the Gate 0 anchors and census-anchor sweep; the station-builder defensive note (`P2` L325–326); spec L152; M1's against-side; the arrival held at the road's edge; the relay-builder claim; the site-inherited question |
| B | **the two Gate 1 holes (water supply, emissions)**; the record leg is national; the re-learning contradiction; the harbor call stated as fact; the Social Contract never meets a child; the keeper entry unwritten; the strictest Gate 7 measure |
| C | the haul route; departure to another city; robots who move in filed as non-residents; care staffed from outside; the food-layer figures; eighteen parent-PAs listed; the Neighbor castable in relation-only form |

## Round 2 — `triple_read_verify.py`
**UNANIMOUS — CLEARED TO WRITE**, 30/30 files, 90/90 field sets, first run, no repair (raw: `.t8_Step7_round2_raw.txt`; tail: `UNANIMOUS - CLEARED TO WRITE`).

## Round 3 — peer cross-check
| Reader | vs | Verdict | Reason |
|---|---|---|---|
| A | B | **CONSISTENT** | B found real holes A missed (water supply, record leg national, re-learning, harbor call); one rounding note of B's is wrong (13.118 is exact) |
| A | C | **CONSISTENT** | A adopts C's open on Gate 3 item (c); A and C shared one error (Gate 1 passed with a hole) |
| B | A | **CONSISTENT** | A's Gate 7 count treated a header as a changed row; A's 48.3 % double-counts; A alone caught the station-builder clause and the eight-candidate mismatch |
| B | C | **CONSISTENT** | C's Gate 1 none-found is overruled; C alone caught the haul route, departure, non-resident robots |
| C | A | **CONSISTENT** | A's 66.8 % and 48.3 % rejected; A's station-clause flag confirmed |
| C | B | **CONSISTENT** | B's flags confirmed; B's PA-84 rejected (a world-fact asserted as an assumption) |

**6/6 CONSISTENT.** Reader A raised six flags to blocking-unless-errata; B recommended five brief corrections; C four errata. **Merge: no flag blocks Step 8; six errata (E1–E6) go into Step 8's brief.**

## Quotation pre-check and snags
The merge body contains no double-quoted string. The quotation audit reports 36 lines for `07_QA_Gates.md`; **all 36 lie in §6, the verbatim raw scan output** (hits that print the pass's own earlier lines — the kind (a) of Phase 10's and Step 5's triage); none in the merge's own text (0 below line 300). Snags are in `07_QA_Gates.md` §5.

## Post-write checks — raw output, pasted unedited
- **Quotation audit:** header/controls/counts below; the 36 reported lines are scan-output hits (triage above).
- **Handoff audit:** *INSTRUMENT VALID: NO* as before (nine phase files only).
- **Phase discipline:** T4 present in 9 / 9 phase files; Step 7's T4 on one physical line (DC-6); the Position-Coverage Ledger **not touched**.
- **Station-heritage / Register script:** not re-run (no Register-relevant text added beyond quoting scan hits); Step 5 and 6 records hold the runs.

### quotation_audit.py (header, controls and counts)
```
pass audited : Mirny
corpus mode  : default (own pass excluded)
corpus files : 5179   chars: 51,662,538

=== POSITIVE CONTROLS ===
  [easy                      ] FOUND     a terminus is nobody's midpoint
  [HARD - blockquote wrap    ] FOUND     A pass may not proceed to Step 5 with a NEVER CITED row
  [HARD - outside Worldspace ] FOUND     Paste raw QA scan output into the QA block. Never summa
  [HARD - case mismatch      ] FOUND     YOU GO TO ESPERANZA AND YOU DO NOT COME HOME FOR FOUR Y
  [HARD - long wrapped       ] FOUND     Different content is not differentiation; a different q

  INSTRUMENT VALID: YES
  NEGATIVE CONTROL (must be absent): PASS - absent

=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 846
NOT FOUND in corpus: 477
  of those, in TABLE CELLS : 93
  of those, in PROSE       : 384

lines reported for 07_QA_Gates.md: 36
```
### handoff_audit.py
```
pass audited : Mirny
phase files  : 9

=== CONTROLS (edit these per pass; they are what makes a zero trustworthy) ===
  POSITIVE (detector must find a formal block): phases 2, 3, 4, 5, 6, 7, 8, 9, 10
  NEGATIVE (detector must find nothing)       : phases none
  INSTRUMENT VALID: NO - detector never discriminated; DO NOT TRUST THESE VERDICTS

  phase | outbound | sweep    | rows | verdict
  ------+----------+----------+------+---------
      2 |        0 | FORMAL   |    0 | n/a - nothing addressed to it
      3 |        0 | FORMAL   |    0 | n/a - nothing addressed to it
      4 |        0 | FORMAL   |    0 | n/a - nothing addressed to it
      5 |        0 | FORMAL   |    0 | n/a - nothing addressed to it
      6 |        0 | FORMAL   |    0 | n/a - nothing addressed to it
      7 |        0 | FORMAL   |   39 | n/a - nothing addressed to it
      8 |        0 | FORMAL   |   28 | n/a - nothing addressed to it
      9 |        0 | FORMAL   |   29 | n/a - nothing addressed to it
     10 |        0 | FORMAL   |   34 | n/a - nothing addressed to it

TOTAL outbound handoff rows: 0
PHASES WITH ROWS ADDRESSED TO THEM AND NO ENUMERATION: 0

=== outbound rows, per target, for hand reconciliation ===
```
### phase_discipline_check.py
```
pass audited : Mirny

=== T3 - POSITION-COVERAGE LEDGER ===
  phases in header: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Child              filled=1  blank=8   blank at: P3, P4, P5, P6, P7, P8, P9, P10
  The Lover (position)   filled=1  blank=8   blank at: P2, P3, P5, P6, P7, P8, P9, P10
  The Parent             filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Ruler              filled=1  blank=8   blank at: P2, P3, P4, P5, P6, P8, P9, P10
  The Elder              filled=2  blank=7   blank at: P3, P4, P5, P7, P8, P9, P10
  The Mentor             filled=1  blank=8   blank at: P2, P3, P4, P5, P6, P8, P9, P10
  The Passer-Through     filled=2  blank=7   blank at: P2, P4, P6, P7, P8, P9, P10
  The Neighbor           filled=1  blank=8   blank at: P2, P3, P4, P6, P7, P8, P9, P10
  ⭐ The Lover FACULTY    filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10

  NOTE: a blank cell is a WARNING BEFORE Step 8, not a defect. Do not
  fill a blank by writing new phase content toward it - that is the
  contamination 00f Rule 3 forbids (see the recipe's hard bound on T3).

=== T4 - PER-PHASE SHED MARKER ===
  [04_Phase_02_Composition_and_Arrival.md]  T4 present: the axis had no use for the Chose it attract/repel analysis at Mirny, the Inherited it and
  [04_Phase_03_Surface_and_Texture.md]  T4 present: this phase's axis had no use for smell (no admitted input), interiors and building fabric 
  [04_Phase_04_Ordinary_Life.md]  T4 present: this phase's axis had no use for dwellings and amenity layout, a shift roster, an intracit
  [04_Phase_05_Relation_and_Geometry.md]  T4 present: this phase's axis had no use for rivalry (none recorded), 5b's sibling form, the per-natio
  [04_Phase_06_Meaning.md]  T4 present: this phase's axis had no use for the roster's denominational strongholds, aesthetics, nume
  [04_Phase_07_Order.md]  T4 present: this phase's axis had no use for the Federation's own form of government above the region,
  [04_Phase_08_Making.md]  T4 present: this phase's axis had no use for the national food tonnages, calories, tier shares and sit
  [04_Phase_09_Populations.md]  T4 present: this phase's axis had no use for the national drink, smoking and siligel detail, the robot
  [04_Phase_10_Catalog.md]  T4 present: this phase's axis had no use for the gear catalog and its two Mirny items, the Zodiac subs

  9/9 phase files carry a T4 marker.
  >> If EVERY phase's answer was literally 'nothing', T4 is falsified
     per its own stated condition (the question would be decorative).
     This tool cannot see the marker's CONTENT well enough to judge
     that - read the 9 lines above by hand.

=== T5 - EARLY LOVER-FACULTY SMOKE TEST ===
  EARLY (Phase 6) verdict: Alive in its conditions and its two bodies — a working coast that keeps nine places talking without being thanked, where people stop together, own their own calls, and get a sunset with no night after it and an open sea nobody can promise — and lovable by someone who wants to be trusted with their own reading; but what its people laugh at and do with their own hours is still the largest empty slot, so for now the love is for how the place holds its conditions more than for any custom it is known to keep (an early, provisional verdict; it must not steer Phases 7–8, or it is falsified and withdrawn).
  LATE marker absent (08_Review_Panel.md missing or has no Lover-faculty line yet)

  T5 not fully applied this pass (one or both markers absent).
```

## DOUBLE-CHECK (Step 7 complete? — raw output)
```
DC-1 lines: {'07_QA_Gates.md': 2025, '.t8_Step7_merge_body.md': 206, '.t8_required_07_Step7.txt': 30}
DC-2 PROOF blocks: {'A': 30, 'B': 30, 'C': 30}
DC-3 gates in the QA block: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', 'C', 'F', 'I', 'P', 'G'] OK
DC-4 errata E1..E6: ['1', '2', '3', '4', '5', '6']
DC-5 S7-RF  [1, 2, 3, 4, 5, 6, 7, 8] OK
DC-5 R      [151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161] OK
DC-5 Q      [122, 123, 124, 125, 126, 127, 128] OK
DC-5 PA     [83, 84, 85, 86, 87, 88] OK
DC-5 F      [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26] OK
DC-5 snags ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
DC-6 T4 one line: 1
DC-7 raw lines reported by assembler vs in file: ['1681'] 1822
DC-8 British spellings in body: none
DC-9 other-city names in body: none
DC-10 symbol/sign words in body: none
DC-11 double-quoted strings in body: 0
```
**Result: every check passes.** Notes by hand: DC-7's 1,822 is the line count of §6 including the labels and fences (1,681 raw lines inside blocks). No other city's pass, culture file, spec or table cell was opened in this step; the exposures are in `07_QA_Gates.md` §5 snag 8.
