# Mirny — Step 4 · Phase 10 · T8 round record

**Pass:** Mirny · ULM · Step 4, Phase 10 (Catalog) · 2026-10-11.
- **Clock checks:** 10:30 (list built and verified; pair file, brief and checkpoint written); ~10:35 (dispatch); ~10:36 (B's first run cut off); ~10:40 (B's second run cut off); ~10:42 (A's first run cut off); ~10:44 (A's first re-dispatch did nothing — plan mode); ~11:2x (all three finished and assembled); Round 2 run 1 (FAILED) and run 2 (UNANIMOUS) after assembly; Round 3 after that; ~11:38 onward (merge written to the folder).
- **Boot:** the session continued from Phase 9's close. Phase 10's plan (setup, list, pair file, brief, dispatch) was approved in plan mode; the Zodiac Lens address discrepancy was resolved first by the developer's ruling of 2026-10-11 (the Lens uses only `Zodiac_Signs_Full_Attributes.md`; no Concordia-district material; the `Zodiac_Personality_Substrate/` folder stays closed).
- **Round 1:**
  - Dispatched ~10:35: A `a7b367b33be043757`, B `a0acf646662e95797`, C `a2c7aab1e7a782e1a` (Opus, general-purpose, background).
  - **B's first run was cut off by the API safeguard flag before logging any entry** (req_011CfvrViGmPhY4Tr9Q3yDzg; its staging file held 14). Re-dispatched on the identical frozen brief as `a28e414b9f785dc7f`; **cut off again** after 13 logged entries (req_011CfvroXqDBCU1YjfvcEXFt). Third dispatch `ac488a5f3eb93023c` completed.
  - **A's first run was cut off** after 24 entries in the output file (22 in its staging file; req_011CfvrxSZT4jPVhrjxeNznA). The first re-dispatch (`a91595ea235beea63`) **did nothing**: plan mode was on and its first write was denied (it read only the brief and the list). Second re-dispatch `ab0b7b543c3c969ab` resumed at entry 25 and completed.
  - C ran once (`a2c7aab1e7a782e1a`).
  - **Plan mode came on during the runs**, so each reader staged most of its output in its plan file. The orchestrator assembled each output file verbatim from the on-disk part plus the staged parts (A: reading log + 3 staged edits; B: 2 staged blocks; C: body, continuation and PROOF part) with `assemble_p10.py`. Results: A 929 lines, B 805, C 889 (`wc -l`); 33 PROOF blocks each; one RESEARCH LOG heading each. The partial originals and both Round 2 raw outputs are kept in `_safeguard_probe/partials/`.
- **Round 2:** `triple_read_verify.py` on the assembled files — run 1 **FAILED** (below); with the developer's approval each reader re-read the failed lines by hand and returned corrected blocks; patched in (`patch_p10.py`); run 2 **UNANIMOUS**.
- **Round 3:** `SendMessage` to the same three live agents; each read the other two's archived output files. Replies are tabulated below.
- **Merge:** written from ~11:38.

**Files:**
- **Written:** `04_Phase_10_Catalog.md` (this phase).
- **Required list:** `.t8_required_04_Phase10.txt` (33 entries, 9,264 admitted lines; built and verified by script, 0 bad). The sealed pair file is entry 33.
- **Brief:** `.t8_Phase10_brief.md`, identical for all slots (`{X}` = A, B, C), never amended (`M-93`).
- **Reader outputs** (archived with the pass, `DR-27`; not canon, not an input): `.t8_Phase10_readerA.md` (929 lines), `…B.md` (805), `…C.md` (889). Each includes its reading log.
- **Checkpoint:** `.t8_Phase10_CHECKPOINT.md`. **Probe folder:** `_safeguard_probe/` (README, flagged-run staging files, partial originals, the two Round 2 raw outputs).

## Round 0 — the required-reading list
- **Sources:** the Phase 10 `MUST OPEN` block (`SPN3` L1098–1184), the Pre-Trip's Phase 10 rows (L390–401), the runbook's §C.8c row 10, and the library of method files the other phases use.
- **Ranges for `P2`–`P9`:** `P2` L1–21, L74–532 · `P3` L1–19, L82–511 · `P4` L1–12, L69–372 · `P5` L1–12, L84–548 · `P6` L1–11, L53–352 · `P7` L1–14, L118–703 · `P8` L1–59, L174–940 · `P9` L1–39, L124–532 (receipts, sweeps and merge provenance excluded).
- **Added because Phase 10 cannot be written without it:** the Zodiac sign file; the three City_Symbolic_Substrate files (README, Planetary_Symbols, Robot_Elementals) and the legend of City_Symbol_Assignments (L61–83 only); the Mirny research log in full (so no Step 3 search is repeated and every rejected source is known); `Robot_Physiology_and_Cultural_Practices`, `Robot_Cold_Physiology`, the Enneagram Character Index and one companion README at its two TBD-tie spans.
- **Orchestrator-verified results (recorded, not dispatched):** the Characters check over both trees (28 hit lines in 21 files; one TBD tie; no canon character resident); the Zodiac Lens input (entry 28 only); the sealed registered pair (Saturn + a pending element; the rationale cell not admitted); the nine admitted-range rulings (`DR-1`, `DR-3`, `DR-4`, `DR-8`/`DR-8a`, `DR-10`, `DR-12`, `DR-26`, `DR-46`, `DR-51`); the research position (Step 3 ended on a session cap with picks unspent).
- **The brief named eleven traps:** names (people: roles only; places: only where a form is given, labeled as an authoring designation) · no sub-locations · candidates stay candidates · gated and reserved items · theme not thing · founders and GPS · work groups are roles · robot canon · a cataloged thing must have a form in the files or be marked unformed · real-world comparables are mechanism only · no T5 line.

## Round 1 — what each reader wrote
| Reader | Axis | Distinctive contributions |
|---|---|---|
| A (929 lines) | "What stays, what refills" | recovery table A1–A32; places C1-1…C1-16 (one offered designation, later withdrawn); things C2-1…C2-16; roles C3-1…C3-20; settings C4-1…C4-15; the Elementals "six/seven" discrepancy; the ridges-outside-the-city third order; research F1–F13 |
| B (805 lines) | "Kept unseen, surfaces refill" | 34-row recovery table; Davis Sea and the Circle as existing names; one offered designation (held as a developer question); the fixed-line candidate with its fit-test; the harbor's morning delay; findings P10-1…P10-4 (the missing wind call is a choice); RF-1…RF-11; research F1–F9 |
| C (889 lines) | "What stays, what refills" (no designation offered) | recovery table A1–A35; landmarks C1-1…C1-14, all unformed; things C2-1…C2-14; roles C3-1…C3-18; settings C4-1…C4-18; findings P10-1…P10-4 (the cleared bank blinds the approach); the Saturn caveat; RF-1…RF-11; research F1–F8 |

**A and C reached the same axis words independently; B reached the same structure with a third order the others lack.** The axis, names, Planet + Element, fixed line and Zodiac dispositions are in the phase file's Merge provenance.

## Round 2 — `triple_read_verify.py`, raw output

### Run 1 — **FAILED** (on the assembled files, before any correction)
*(agent1 = reader A, agent2 = reader B, agent3 = reader C, in argument order.)*
The header, every file block that carries a mismatch, and the verdict are shown. The 93 passing "all fields match ground truth" lines (and the file headers that carry no mismatch) are counted, not repeated; 10 mismatch lines in all.

```
required files: 33
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ⛔ LINES MISMATCH  claimed='175'  actual='174'
  agent3   ⛔ LMID  MISMATCH  claimed='| **refusing all ethnic material** → *placeless cities* | **'  actual='|---|---|---|'

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/01_Inherited.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ⛔ LMID  MISMATCH  claimed='- **From #3 → Phase 5 (with request R-11):** when the relay '  actual='there any way back?'

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Cold_Physiology.md ===
  agent1   ⛔ LINES MISMATCH  claimed='185'  actual='184'
  agent1   ⛔ LMID  MISMATCH  claimed='> threshold — the death spiral.**'  actual='> ***Stopping is the dangerous act.*** **Cooling means capac'
  agent1   ⛔ LLAST MISMATCH  claimed=''  actual='*Full research record including verbatim search strings: `…/'
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Characters/Enneagram_Character_Index.md ===
  agent1   ⛔ LINES MISMATCH  claimed='36'  actual='35'
  agent1   ⛔ LLAST MISMATCH  claimed=''  actual='*Characters with TBD Enneagram types are not listed here. Ad'
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Zodiac_Signs_Full_Attributes.md ===
  agent1   ⛔ LINES MISMATCH  claimed='268'  actual='267'
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Symbolic_Substrate/City_Symbol_Assignments.md  [range 61-83] ===
  agent1   ✅ all fields match ground truth
  agent2   ⛔ LMID  MISMATCH  claimed='> ⚠ **`⏸️` is a deliberate hold with a named filler, not an '  actual='> Zhongshan.**'
  agent3   ✅ all fields match ground truth

=== VERDICT ===
⛔ NOT UNANIMOUS - DO NOT WRITE. Log which agent/file failed and why.
```

- **Result:** 10 mismatched fields (A 6, B 1, C 3) across 6 of the 99 field sets (A 3 files, B 1, C 2); the other 93 field sets passed. The mismatches are line counts one too high (claimed 175, 185, 36, 268 against actual 174, 184, 35, 267) and the middle or last line taken from the wrong position. **Probable cause (not proved):** the Read tool's display shows one phantom final line on some files; the readers' own snags describe it, and each had checked its counts against `wc -l` before submitting.
- **Remedy — a deviation from the precedent of Phases 4 and 8** (where a failed slot was re-dispatched fresh): the orchestrator asked the developer, who chose **"Same readers re-check"**. Each of A, B and C re-read the failed lines by hand and returned corrected blocks; **the orchestrator supplied no value**. The blocks were patched in verbatim (`patch_p10.py`) and Round 2 was re-run. *Rationale for the deviation:* a fresh slot re-reads 9,264 lines to correct a line count, at the cost of the usage window; the failure was in PROOF fields, not in the reading logs or the body.

### Run 2 — **UNANIMOUS**
```
required files: 33
agents: agent1, agent2, agent3
...
=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```
- All 99 field sets (33 files × 3 readers) read "all fields match ground truth"; the 33 file headers are counted, not repeated.

## Round 3 — peer cross-check (reply-only, via `SendMessage`)
| Reader | vs | Verdict | One-sentence reason |
|---|---|---|---|
| A | B | **CONSISTENT** | quotations and passages resolve; one miscounted span number (34 against 29 admitted spans); B's reading of the missing wind call offered as a Step 5 refinement only |
| A | C | **CONSISTENT** | `SPEC` L185, the `ELE`/`PLA` lines and the research quotations resolve; C's snag text says one file lacks a final newline and has 175 lines (it ends in a newline and has 174; C's PROOF block says 174) |
| B | A | **CONSISTENT** | the `CSA` middle line, the blizz-line quotation and `P3` L332 resolve; three interpretive over-reaches (the relay's Arcanet joining "from ~2614", rime on masts as the relay's visible face, the call-in "rides on the relay") |
| B | C | **CONSISTENT** | `P8` L570, `CSA` L79 and `ELE` L86 resolve; the same 175-vs-174 prose slip |
| C | A | **CONSISTENT** | the Elementals "six/seven" catch is right; three over-reaches (the same ~2614 date; "some or all of the founding cohort are alive until the war"; "Mirny's skyline gives no landmark a visitor can orient by") |
| C | B | **CONSISTENT** | the quotations resolve; B's count of spec spans was off by five; its reinterpretation of `P7` P7-15 is a Step 5 refinement, not an overwrite; its first reading log counted the display's phantom line, corrected before PROOF |

**Dispositions the readers reached themselves** (reply section 5): the axis is a developer's label (A and C's words, B's third order); A's offered station designation is withdrawn (fails the form test); B's fast-ice designation is a developer question; Saturn + Air with C's caveat; the fixed line alone is a candidate and the call-in reserved; B's Cancer refusal of the ring-as-shell read stands; the research-derived entries are reserved findings and conditional settings, not adopted catalog entries; the Zodiac sign-by-sign results are a union. Reader C also noted that Zodiac lens cells carry quoted strings against the Pre-Trip form rule (bare pointer only); the merge rewrote them to pointers.

## Quotation pre-check (orchestrator, before writing)
Every pass-file quotation in the phase file was checked by a normalized search (dashes, quote marks, markdown structure, case and whitespace stripped) over the pass files the audit excludes. Of 24 quoted strings, 21 resolved at once. **Three did not and were fixed before the audit:**
1. A role title in quotation marks ("the best reader of the wind, who holds no title") — the pass files say instead that *the best judge of the wind holds no title* (`P8` P8-12); rewritten as an unquoted paraphrase.
2. A phrase in italics attributed to `P7` P7-26 ("the wind by nobody") — the row says the wind is taught by *nobody* with no instrument; rewritten unquoted.
3. A quoted phrase of the phase file's own prose ("the harbor watcher's call heard across the city") — rewritten unquoted.
The Zodiac cells were also rewritten from quoted strings to bare pointers (the Pre-Trip form rule for lens cells). `Additional locations: TBD` is a `SPEC` string, outside the pass folder, and resolved in the audit corpus.

## Snags
1. Every cut-off, re-dispatch and the denied write are recorded in Round 1 above and in `_safeguard_probe/README.md` (request ids, entries done, what was in flight). **The safeguard probe has not been run**; it is planned for after this phase, section by section, as the developer asked.
2. The Round 2 deviation (same-reader re-check) is above.
3. The orchestrator's own exposures are in the phase file's snags (the opening words of the Mirny rationale cell; the Characters-tree filenames and hit windows).
4. A step in this write-up (extracting the draft from the plan file) used `sed`, so the phase file is byte-identical to the approved draft except for the quotation fixes above and the Round 3 provenance notes.

## Post-write checks — raw output, pasted unedited

**Triage (by hand, as each tool asks):**
- **Quotation audit.** It audits the whole pass folder with the pass's own files excluded from its corpus, so quotations of the pass's own earlier files, and connective prose captured between two adjacent quotations, show as misses. The 20 lines for `04_Phase_10_Catalog.md` (14) and `04b` (6) are of three kinds:
  - (a) phrases quoted from the pass's own files, each verified by the pre-write check above: `P8` P8-11 and `P3` L421 (L135), `P7` L542 (L229), `P8` L371 (L252), `RES` L18 (L270), `P8` L553 (L326), `P5` P5-8 (L431);
  - (b) connective prose captured between adjacent quotations (the receipt line at L54, the ridge line at L276, the B3 lines at L423–L424, the table cell at `04b` L33);
  - (c) the struck phrases recorded in the snags and the Round 3 table (L599 of the phase file; `04b` L105–L107), and the two phrases quoted in the pre-check description to say they were removed (`04b` L114, L116).
  - **Real misses found by the pre-write check and fixed before this audit: 3** (see "Quotation pre-check"). **Real misses remaining: 0.**
- **Handoff audit:** *INSTRUMENT VALID: NO*, as at Phases 5–9 (its detector found no outbound "HANDED FORWARD" blocks, so it cannot discriminate). It reports Phase 10's sweep as FORMAL with 34 table rows; the phase file's sweep table has 33 rows (the audit's count is one higher at Phases 9 and 10 alike, consistent with counting the header row).
- **Phase discipline:**
  - T4 is present in 9 / 9 phase files; Phase 10's marker names substantive shed items, read by hand. It is on one physical line.
  - T5's early marker is present (Phase 6) and was not used here; its late marker waits for Step 8.
  - The Position-Coverage Ledger shows every cell blank at P10: bookkeeping only, nothing was written toward them (`00f` Rule 3). The ledger is updated only on developer confirmation.

### quotation_audit.py (header, controls and counts; then every line it reports for the Phase 10 files)
```
pass audited : Mirny
corpus mode  : default (own pass excluded)
corpus files : 5147   chars: 49,711,699

=== POSITIVE CONTROLS ===
  [easy                      ] FOUND     a terminus is nobody's midpoint
  [HARD - blockquote wrap    ] FOUND     A pass may not proceed to Step 5 with a NEVER CITED row
  [HARD - outside Worldspace ] FOUND     Paste raw QA scan output into the QA block. Never summa
  [HARD - case mismatch      ] FOUND     YOU GO TO ESPERANZA AND YOU DO NOT COME HOME FOR FOUR Y
  [HARD - long wrapped       ] FOUND     Different content is not differentiation; a different q

  INSTRUMENT VALID: YES
  NEGATIVE CONTROL (must be absent): PASS - absent

=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 796
NOT FOUND in corpus: 442
  of those, in TABLE CELLS : 93
  of those, in PROSE       : 349

  [00.1_Step_MINUS-1_Input_Contract.md:15]           is now present, by ruling (hard canon, rb l2786): the founders were exiles from russia, china and australia. the spec's
  [00.1_Step_MINUS-1_Input_Contract.md:15]           (l150 chars 702-716) is consistent with the ruling as one of three stocks

  [04_Phase_10_Catalog.md:54]           (entry 27, l129). no canon character is resident at mirny. ds10 's
  [04_Phase_10_Catalog.md:135]           mirny's own making for itself is upkeep, and upkeep leaves nothing to show
  [04_Phase_10_Catalog.md:135]           banks refill and move, while the ring, the core, the harbor, the relay and the quarries do not
  [04_Phase_10_Catalog.md:229]  [CELL]  administrative posts as a function, not a building
  [04_Phase_10_Catalog.md:252]  [CELL]  the objects mirny keeps longest were made by no one in either body here
  [04_Phase_10_Catalog.md:270]           so the cost is a choice remade after every storm
  [04_Phase_10_Catalog.md:276]           ( res l125; p3 ). 2nd rw, f9 . where a real people's ridges
  [04_Phase_10_Catalog.md:326]  [CELL]  belonging at mirny is legible at the threshold, not in the voice
  [04_Phase_10_Catalog.md:423]           is not supported for mirny itself and lands only on the subnet's single path - a relay whose failure leaves the subnet
  [04_Phase_10_Catalog.md:423]           is refused as evidence (saturn's rings and the city's ring share a word, not a property). neptune (
  [04_Phase_10_Catalog.md:424]           the determination rests on air's physics, not its label. electricity (
  [04_Phase_10_Catalog.md:431]           the parent's boundary is a fact of the signal, not of the road
  [04_Phase_10_Catalog.md:599]           some or all of the founding cohort are alive until the war
  [04_Phase_10_Catalog.md:599]           (the relay's technology is not canon; no admitted line puts local radio on it); a reader's one-line
  [04b_T8_Rounds_Phase_10.md:33]  [CELL]  c1-16 (one offered designation, later withdrawn); things c2-1
  [04b_T8_Rounds_Phase_10.md:105]  [CELL]  rime on masts as the relay's visible face, the call-in
  [04b_T8_Rounds_Phase_10.md:107]  [CELL]  catch is right; three over-reaches (the same 2614 date
  [04b_T8_Rounds_Phase_10.md:107]  [CELL]  mirny's skyline gives no landmark a visitor can orient by
  [04b_T8_Rounds_Phase_10.md:114]           the best reader of the wind, who holds no title
  [04b_T8_Rounds_Phase_10.md:116]           the harbor watcher's call heard across the city
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

## Generator close-out check (`§C.8c-i`, `M-208`) — run after Phase 10, before Step 5

Run from `Cities/`, against `City_Development_Passes/Mirny_Subnet/Mirny`, with the runbook's loop unchanged:
```
G1   OK — cited in 8 phase(s)
G2   OK — cited in 8 phase(s)
G3   OK — cited in 8 phase(s)
G4   OK — cited in 8 phase(s)
G5   OK — cited in 8 phase(s)
G6   OK — cited in 8 phase(s)
G7   OK — cited in 8 phase(s)
G8   OK — cited in 8 phase(s)
```
- **Every G1–G8 is cited in at least one phase's "Generators used" line; no `⛔ NEVER CITED` row.** Each shows 8 of the 9 phase files; the ninth (Phase 8) writes its generator list on lines after the header, which this one-line pattern cannot see — it is not a gap.
- **G1** (the Planet + Element pair) was cited in earlier phases as deferred and is **used for the first time here**, at §B3 of Phase 10, on the members' own terms read from `Planetary_Symbols.md` and `Robot_Elementals.md` (the admissible half; the rationale cell was never admitted) — the half that `M-208` found dropped at Zhongshan. The check passes on content, not only on the grep.
