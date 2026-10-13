# Mirny — Step 9 · Record and Recording Law (9.5) · T8 round record

**Pass:** Mirny · ULM · Step 9 · 2026-10-12 (unattended run; the developer awake for part of it).
- **Clock checks:** 11:22 (Step 8 closed) · 11:24 (list, brief, checkpoint; Round 1 dispatched) · 11:32–11:38 (readers B and C cut by the API safeguard flag, B once and C three times; resumed from their own files by SendMessage) · 11:39 (A complete; one classifier stop, resumed) · 11:42–11:43 (B and C complete; Round 2) · 11:43–11:45 (Round 3, three replies) · 11:46–11:55 (merge: `09_Record.md`, `09.5_Log.md`; audits; this record).
- **Files:** written `09_Record.md`, `09.5_Log.md` and this record. List `.t8_required_09_Step9.txt` (30 entries, 3,997 admitted lines, 0 bad — a lean list by design: the snag sections, the round records, the observations tail and the tracker's Mirny lines, chosen with the developer's plan limit in view); brief `.t8_Step9_brief.md`; readers `.t8_Step9_reader{A,B,C}.md` (554 · 615 · 621 lines; 30 PROOF each); Round 3 `.t8_Step9_round3_reader{A,B,C}.md`; Round 2 raw `.t8_Step9_round2_raw.txt`.
- **A correction to the brief:** it said Steps 7 *and* 8 were cut off by a usage limit. Only Step 7 was. All three readers could not find the source for Step 8 and said so; the merge records the brief as wrong (`09.5_Log.md` §G item 25; M-283).

## Round 1 — what each reader wrote
| Reader | Distinctive |
|---|---|
| A | the most granular recurrence table (including datasheet defects and a count of tool exposures); the deferred line-anchor sweep with no owner; the brief's entry numbering against its own list; the quotation audit's growing backlog; three self-corrections of its own |
| B | the broadest set of requests (the pending correction candidates, the relation items for shared-file owners, the ledger question); the differentiation-row timing contradiction (runbook against Pre-Trip); the parked figure overturned with 27 downstream lines; Round 3 replies archived inconsistently; the tracker's "developer's absence" overclaim |
| C | the fullest log by kind (A to I) with the killed findings listed by source; the item-by-item tracker overclaims; the nineteen-row methodology table; the PROOF-rule against name-guard collision; the unscoped founders script and the T5 late-marker finding |

## Round 2 — `triple_read_verify.py`
**UNANIMOUS — CLEARED TO WRITE**, 30/30 files, 90/90 field sets, first run (raw: `.t8_Step9_round2_raw.txt`).
```
=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

## Round 3 — peer cross-check
All six replies **CONSISTENT**. Conditions applied at the merge:
| Point | Decision |
|---|---|
| Line total | 3,997 (A's 4,011 was an addition error, corrected by A) |
| Step 8 usage-limit cutoff | closed: it did not occur; the brief was wrong (A Q-141/PA-93, B Q-138/S9-RF-1, C Q-140/R-175 dropped; recorded as a snag and M-283) |
| Proposed observation entries | sixteen distinct (M-283…M-298); B's M-289 dropped as the same lesson as M-278; A's PA-92/PA-93 and C's PA-92–94 collapsed into PA-92…PA-95 |
| Recurrence values | plan mode 7; hook notices 11; usage-limit pauses 3; number collisions 4; quotation slips 12 (merged by one counting rule: a unit is a phase or step) |
| Reader B's Phase 7 plan-mode staging | struck: Phase 7's readers wrote directly to the scratchpad (A; `04b` P7 L14) |
| Reader B's station-builder denial as a killed finding | struck: it is a QA flag (M-279) |
| "Flattering" and "single most effective defense" | softened to what the sources show (B's B7 and M-294; C's reading of the tracker) |
| Tracker overclaims | kept: L533 no PROPOSED mark; L361 over long against M-109; L360 stale on the Element and "in the developer's absence" (B); "twelve comparables" checked by the orchestrator against `06` §3.3: twelve (C's thirteen was a Round 1 slip) |
| Three drafts used the guarded word | corrected from "three readers" to two at Step 6 and one at Step 8 (A) |
| MP-6, MP-14, MP-15 | downgraded in `09_Record.md` Item 4 |
| B's R-173 (retire pre-`DR-46` wording) | kept as a docket line in Item 2, not a request |

## Merge
`09_Record.md` is reader C's Item 1–4 structure (the fullest) with B's and A's additions (the tracker's "absence" overclaim; MP-16…MP-19). `09.5_Log.md` is reader C's grouped log A–I with A's and B's additions to contradictions, self-corrections and unclear items, the merged Recurrence table, sixteen merged M-entries, merged open items. Assembled by script from reader C's file plus the merge text (the script in the session scratchpad; the output is plain text, edited by hand afterward); double-quoted strings were set in italics before the audits (M-264).

## Post-write checks — raw output, excerpted
- **Quotation audit:** 0 lines reported for `09_Record.md` or `09.5_Log.md`; the header, controls and counts below (the rest of the output lists earlier files' own-pass quotations by design; excerpt, the remaining lines omitted).
```
pass audited : Mirny
corpus mode  : default (own pass excluded)
corpus files : 5179   chars: 51,672,165

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

```
- **Handoff audit:** *INSTRUMENT VALID: NO* as at every check since Phase 5 (M-284); excerpt (the first 20 lines; the per-target section omitted).
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

```
- **Phase discipline:** the tool looks only at the nine phase files for T4 (9/9); this step's own T4 line is the last line of `09.5_Log.md`, on one physical line (DC-5). The T5 comparison remains unrecorded (M-286). Excerpt (the T4 and T5 lines only; each truncated at 200 characters):
```
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
=== T5 - EARLY LOVER-FACULTY SMOKE TEST ===
  EARLY (Phase 6) verdict: Alive in its conditions and its two bodies — a working coast that keeps nine places talking without being thanked, where people stop together, own their own calls, and get a
  LATE (Step 8) mention   : | H-1 | 07 §3 Gate 10 | the panel's seeds: the Neighbor castable only relation-only; the Lover faculty's question; the thinness flag | disch
  Both present. COMPARE BY HAND: if the early verdict changed what any
  phase between 6 and 8 wrote, T5 is FALSIFIED per its own stated
```
- **Founders script:** not re-run (its heritage section is repo-wide and prints other cities' lines; MP-2). This step wrote no founders.
- **Position-Coverage Ledger:** not touched.

## DOUBLE-CHECK
Run after the two files were final; this record continues after the check (M-288), so DC-1 counts only `09_Record.md`, `09.5_Log.md` and the list.
```
DC-1 lines (before this record was written): {'09_Record.md': 96, '09.5_Log.md': 291, '.t8_required_09_Step9.txt': 30}
DC-2 PROOF blocks: {'A': 30, 'B': 30, 'C': 30}
DC-3 M       [283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298] OK
DC-3 R       [169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179] OK
DC-3 Q       [137, 138, 139, 140, 141, 142, 143, 144] OK
DC-3 PA      [92, 93, 94, 95] OK
DC-3 S9-RF   [1, 2, 3, 4, 5] OK
DC-4 MP rows: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19'] OK
DC-5 T4 one-line count (log, record): 1 0
DC-6 double-quoted strings (record, log): 0 0
DC-7 British spellings: none
DC-8 other-city names: none
DC-9 symbol/sign words: none
DC-10 unresolved markers {{ or [[ : 0
DC-11 sections in log: ['Recurrence', 'Proposed observation entries (M-283 onward)', 'What the log cannot show', 'Nulls', 'Reserved findings', 'Requests (R-169 onward; none blocking)', 'Questions (Q-137 onward; none blocking)', 'Provisional assumptions (PA-92 onward)', 'Snags and self-corrections (this step)']
DC-12 sections in record: ['Canon opened (M-171)', 'Step 9 — Record', 'Item 1 — the QA block and the Review Panel block (where they are; what each actually contains)', 'Item 2 — the differentiation row, and anything noticed about another city', 'Item 3 — the tracker', 'Item 4 — methodology changes the pass suggests (PROPOSED, never applied; no methodology file edited)', 'Step 9 status']
DC-13 first-person 'my' / 'I ': 0
```
**Verdict:** the sections of both files are present in the required order; the PROOF blocks are 30 each; every numbered series is consecutive (M-283…M-298, R-169…R-179, Q-137…Q-144, PA-92…PA-95, S9-RF-1…5, MP-1…19); no double-quoted string, British spelling, other-city name, symbol or sign word, or unresolved marker in either file; T4 on one physical line in `09.5_Log.md`. Two tracker statements were checked by the orchestrator against the files and are consistent: twelve comparables in `06_Differentiation.md` §3.3; nine of 160 lines of the cross-city table begin with the city's label.

## Snags
1. The brief's wrong Step 8 cutoff claim (above; M-283).
2. Safeguard-flag and classifier cuts of the readers (B once, C three times, A once) resumed from their files (M-297).
3. The build script for the two files regenerated them with double quotes; the quotes were converted to italics by a one-pass script after the first quotation pre-check found 18 strings not matching a single source line (five were regex pairing artifacts across strings; the others were this step's own labels or loose paraphrases).
4. The working directory drifted between shell calls; absolute paths were used.
