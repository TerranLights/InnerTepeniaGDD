# Mirny — Step 8 · The Review Panel (Gate 10) · T8 round record

**Pass:** Mirny · ULM · Step 8 · 2026-10-12.
- **Clock checks:** 10:47 (Step 7 closed) · ~10:50 (**pin re-verified**; list, brief, checkpoint) · ~10:52 (Round 1 dispatched) · 11:12–11:15 (A, B, C finished; Round 2) · 11:16–11:17 (Round 3, three replies) · ~11:20 (merge written; refereed labels renamed RC-n so they do not collide with request numbers) · 11:21 onward (audits, this record).
- **The pin:** the Concordia original of `00f` hashes sha256[:16] = `33d660ebfbbca9e9` and has 737 lines, matching the ULM copy's header; only the hash and line count were read.
- **Files:** written `08_Review_Panel.md` and this record. List `.t8_required_08_Step8.txt` (20 entries, 6,884 lines, 0 bad); brief `.t8_Step8_brief.md` (final at dispatch; carries Step 7's errata E1–E6 as facts); readers `.t8_Step8_reader{A,B,C}.md` (657 · 599 · 619 lines; 20 PROOF each); Round 3 `.t8_Step8_round3_reader{A,B,C}.md`; Round 2 raw `.t8_Step8_round2_raw.txt`.

## Round 1 — what each reader wrote
| Reader | Distinctive |
|---|---|
| A | three `unmet` (later one); the road neighbor as an uncastable position; the unmarked handover (PF-1); the blameless are the unlearned; poles that switch |
| B | the broadest panel (arcs, faculties, shadow bench, precursors); the borrowed reading in a household; no priority rule rather than no arbiter; the candidate joy layer is wind-set (6 of 7); the hub-side ledger |
| C | deferred hub maintenance never checked; the unlearned kept unlearned (P7-31's cost does not follow); the Social Contract shaped like a robot's life course; learning and privacy by one door; two `unmet` |

## Round 2 — `triple_read_verify.py`
**UNANIMOUS — CLEARED TO WRITE**, 20/20 files, 60/60 field sets, first run (raw: `.t8_Step8_round2_raw.txt`).

## Round 3 — peer cross-check
All six replies **CONSISTENT**: each reader found the other two consistent with its own run. Conditions applied: only **one** `unmet` survives (the hub neither explains its outages nor asks for a second path — all three runs support it); A's storm ban and say for the eldest and C's no one can be sent are national canon → `declined`; A's PA-90/PA-91 and B's PA-92 rejected; water, the child meeting the Social Contract, and keeper entry are duplicates of Step 7's flags; the standout is kept with a hub-side scope note; five citation slips corrected (B's 62.0 % attribution, B's King-arc overreach, C's hazard type and 'almost nobody about', A's child age and a lowercase letter).

## Quotation pre-check and snags
`08_Review_Panel.md` contains no double-quoted string (DC-7). Snags are in `08_Review_Panel.md` §11. The refereed-conflict labels first reused R-1…R-5, colliding with request numbers; renamed RC-1…RC-5 before the audits.

## Post-write checks — raw output, pasted unedited
- **Quotation audit:** 0 lines reported for `08_Review_Panel.md` (the list below is the header, controls and counts). **Handoff audit:** *INSTRUMENT VALID: NO* as before. **Phase discipline:** Step 8's T4 on one physical line (DC-6); the Position-Coverage Ledger is bookkeeping only and was **not touched**.

### quotation_audit.py (header, controls and counts)
```
pass audited : Mirny
corpus mode  : default (own pass excluded)
corpus files : 5179   chars: 51,667,315

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

lines reported for 08_Review_Panel.md: 0
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
  LATE (Step 8) mention   : | H-1 | 07 §3 Gate 10 | the panel's seeds: the Neighbor castable only relation-only; the Lover faculty's question; the thinness flag | disch

  Both present. COMPARE BY HAND: if the early verdict changed what any
  phase between 6 and 8 wrote, T5 is FALSIFIED per its own stated
  condition and must be withdrawn, not quietly kept.
```

## DOUBLE-CHECK (Step 8 complete? — raw output)
```
DC-1 lines: {'08_Review_Panel.md': 247, '.t8_required_08_Step8.txt': 20}
DC-2 PROOF blocks: {'A': 20, 'B': 20, 'C': 20}
DC-3 sections: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'] OK
DC-4 PF: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'] OK
DC-5 S8-RF  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] OK
DC-5 R      [162, 163, 164, 165, 166, 167, 168] OK
DC-5 Q      [129, 130, 131, 132, 133, 134, 135, 136] OK
DC-5 PA     [89, 90, 91] OK
DC-6 T4 one line: 1
DC-7 double-quoted strings: 0
DC-8 British spellings: none
DC-9 other-city names: none
DC-10 symbol/sign words: {'Zodiac': 1}
DC-11 the word medium in prose: 2
DC-12 placeholder-name tokens found: []
```
**Result: every check passes** (DC-5's request check initially counted the refereed labels as requests — fixed by the RC-n rename; the requests are R-162…R-168; DC-10's one hit is the T4 line's meta mention of the symbol and sign layers; DC-11 counts the guarded word in two prose mentions that describe the guard, never in a claim). No other city's pass, culture file, spec or table cell was opened in this step.
