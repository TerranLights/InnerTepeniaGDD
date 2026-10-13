# Mirny — Step 4 · Phase 9 · T8 round record

**Pass:** Mirny · ULM · Step 4, Phase 9 (Populations) · 2026-10-11.
- **Clock checks:** 08:47 (boot); 09:15 (list built); 09:25 (dispatch); 09:28–09:30 (two slots re-dispatched); 09:59 (all three finished); 10:00 (Round 2); ~10:05–10:25 (Round 3); 10:08 onward (merge drafted and written).
- **Boot:** the 08:47 session read the runbook in full (all 3,160 lines), the tracker's SESSION BOOT and RESUME HERE, the spine's Phase 9 (L1023–1097), the Pre-Trip's Phase 9 rows (L377–388), `Datasheets/Phase_9.md`, and Phase 8's checkpoint, brief and list as the template. The plan (setup and dispatch) was approved in plan mode before any project file was written.
- **Round 1:**
  - Dispatched ~09:25: A `adad5db8d06e6ed14`, B `a3853bf52ac4d99cb`, C `a827cddb1ec0f7658` (Opus, general-purpose, background).
  - **A and C were each terminated by the API safeguard flag** (A after 2 entries, req_011CfvmLoC767hZKfWEpK3e6; C after 16, req_011CfvmPw3DjBEh1NvuM1Cuw). Both slots were re-dispatched ~09:29–09:30 on the identical frozen brief (A `a3138da62dca6d2a8`, C `ad5b3631fadbd5c75`) and resumed from their own reading logs. B ran to the end unflagged.
  - Finished: **A 09:58** (1,052 lines), **B 09:53** (1,015), **C 10:00** (1,027).
- **Round 2:** ~10:00, A + B + C. Re-run after C's last write at 10:00:02: identical output.
- **Round 3:** sent ~10:05 by `SendMessage` to the same three live agents; each read the other two's output files. Replies came in by ~10:25.
- **Merge:** drafted and written from 10:08 (no plan-mode approval was needed: plan mode was off).

**Files:**
- **Written:** `04_Phase_09_Populations.md`.
- **Required list:** `.t8_required_04_Phase9.txt` (68 entries, 9,682 admitted lines; built and verified by script, 0 bad).
- **Brief:** `.t8_Phase9_brief.md`, identical for all slots (`{X}` = A, B, C), never amended.
- **Reader outputs** (archived with the pass, `DR-27`; not canon, not an input): `.t8_Phase9_readerA.md` (1,052 lines), `…B.md` (1,015), `…C.md` (1,027). Each includes the reading log of its first run.
- **Checkpoint:** `.t8_Phase9_CHECKPOINT.md`.

## Round 0 — the required-reading list
- **Sources:** the Phase 9 `MUST OPEN` block (`SPN3` L1023–1097), the Pre-Trip's Phase 9 rows (Laws of Robotics, Robot Universals, Doll Representation Categories, the human-robot baseline) and the runbook's §C.8c row 9. Added, each because a Phase 9 component cannot be written without it:
  - **all of Robot Universals** (Preface, README, four Part READMEs, 27 chapters), not only Ch. 13–14: this is the phase where a missed chapter produced a false headline (`M-169`);
  - the Falkland Treaty draft and scaffold, the Founding Register, the Census and the Upper Earth composition file (admission rule and composition only);
  - the Second Interwar Timeline spans, the cold-physiology and Sumerian robot files, `DOI0` and `DOI4` L421–436 (national demography), and `MED` (care and clinicians).
- **Ranges for `P2`–`P7`** unchanged from Phase 8's list (files unchanged since 2026-10-06); `P8` admitted at L1–59 and L174–940 (receipt, sweep and merge provenance excluded).
- **Orchestrator-verified results (recorded, not dispatched):** six, in the brief and the phase file's receipt (the zero-hit name check; the Doll categories; the spec and Census I; the pass files without receipts and Phase 8 as proposed; the national human-demographics canon; the national chamber rule).
- **The brief named seventeen traps:** the `M-169` false headline; robot canon binds every claim; Doll categories; `DR-4`/`DR-12`; work groups are not arrival populations; founders (`DR-9`, `DR-46`, `DR-19`, `DR-25/26`); the Acts; candidates stay candidates; no comparison; reserved items; relationship canon; worked examples; human demographics; the treaty and composition scope; real-world comparables and non-inputs; T4 and the Position-Coverage bookkeeping rule; admitted-line citation and arithmetic.

## Round 1 — what each reader wrote
| Reader | Axis | Findings | Distinctive contributions |
|---|---|---|---|
| A (1,052 lines) | "Exposure, not kind" | P9-1…P9-13 + IR-1…IR-8 | the children of founding households; kind outranks exposure only for the Upper Earth human visitor; "sorted in, never up"; the 2×2 grid; build-date cohorts; the 248-year frame arithmetic |
| B (1,015 lines) | "First sky, not body" | P9-1…P9-15 | the Act gradient as a full finding; the heirs inherit the sorting, not the teaching; seniority unreadable off a body; the robot as the household's continuity; the Upper-Earth-robot-stream conditional |
| C (1,027 lines) | "Formed here, or arrived" | P9-1…P9-19 | the two lines (wind, memory) as one structure; the lens half-life; the Act-2 fold into the robot half; the robot native never a beginner without being an answerer; eldest ≠ elderly; the clinicians' second "from"; `DR-51` used |

**All three reached the same core under different names** (the phase file's Merge provenance lists it). Axis split resolved in the merge: C's form holds A's and B's as its two lines; the label is Q-83.

## Round 2 — `triple_read_verify.py`, raw output

The header and verdict lines are shown. The 204 passing "all fields match ground truth" lines (68 files × 3 readers) and the 68 file headers are counted, not repeated.

```
required files: 68
agents: agent1, agent2, agent3
=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
EXIT=0
204
```

- No reader failed Round 2. Each reader had caught its own PROOF slips before submission (C five, A two, B two) by a read-only comparison that writes nothing; every field was re-read with the Read tool and recopied by hand (`M-249`).
- A re-run at ~10:10, after C's last write (10:00:02), produced byte-identical output.

## Round 3 — peer cross-check (reply-only, via `SendMessage`)
| Reader | vs | Verdict | One-sentence reason |
|---|---|---|---|
| A | B | **CONSISTENT** | every cited passage found (`NNS` L105, `RU5` L41, `P2` L353); the axis sentence about "standing" pulls against `P5` L237 and B half-corrects it; `DR-51` missed but B marks its human-side claim conditional |
| A | C | **CONSISTENT** | quotes exact (`DOI0` L37, `DRL` L1022, `RP` L353, `RU4` L52, `RU18` L49); the one conflict is C's use of the census founding-wave annotation, against `P2` A.4 |
| B | A | **CONSISTENT** | `FTD` L69, the 200–500-year range, `MED` L203, `RU14` L57 and the 19,628 margin all resolve; "insiders are made, not born" is phrasing against `P5` L396, conceded in A's own grid |
| B | C | **CONSISTENT** | `DRL` L1022, `RU5` L40, `RU4` L52, `FRM` L168–170 found; two small slips (the "only population whose existence began as a local decision" overreach; `CP` L62 anchor) |
| C | A | **CONSISTENT** | `FTD` L69, `DS9` L8, `MED` L203, `FTD` L48 found; omission only: `DR-51` not used |
| C | B | **CONSISTENT** | `P5` L396, `RU5` L41, `FRM` L169–170, `P2` PA-14 found; omission only: `DR-51` not used; `P5` M2 offered, not adopted, and B flags it |

**6 / 6 CONSISTENT → gate met.**

**Dispositions** (all in the phase file's Merge provenance):
- **Axis:** C's two-line form holds A's and B's; the label is a developer question (Q-83, now one question merging A's, B's and C's).
- **`DR-51`** (`DRL` L1022: later human immigration is possible): used, in P9-4, P9-5, P9-17 and PA-59.
- **The census founding-wave annotation** as evidence of later arrivals: kept out (RF-7).
- **A's children of founding households** and **kind outranks exposure only for the Upper Earth human visitor:** kept.
- **The baseline's local reason (A's IR-2):** a national shadow, not a Mirny finding.
- **The mentor strand and the private-channel strand:** reserved findings (RF-4, RF-5).
- **The Act-2 fold of the memory line into the robot half:** a full finding (P9-17).
- **Numbering:** RF, R, Q and PA numbers collided across the three files and were renumbered in the merge.

## Merge (§N.2 as amended, `M-246`)
- **Credits:** the phase file's Merge provenance (found by / confirmed by).
- **Quotation pre-check by script, read-only, on the draft** (every quoted string of 4+ words against the 68 admitted sources, with the admitted ranges, emphasis and whitespace normalized): **149 distinct quotations tested; 22 not found; 0 real misses.**
  - **3 are regex artifacts:** the pattern paired the closing mark of one quotation with the next opening mark across a paragraph.
  - **19 are not source quotations:** the three axis labels; struck phrases recorded in the axis corrections, Snag 10 and the Merge provenance ("insiders are made, not born", "standing turns on where her reading began", "the only population whose existence began as a local decision", "baseline's reason passes from witnessed to told"); authoring labels ("native without being young", "sorted in, never up", "inherit the sorting, not the teaching", "the immigrant teaches the native"); the swap-test generic alternatives ("two bodies share a city", "anchor in the founders"); the `M-169` false headline quoted as the trap; "what X are like"; "Ask the oldest" / "care for the old" (authoring phrases). Two quotations that were my own constructions inside source-looking quote marks were rewritten before the file was written (P9-3 Act 1, P9-17).

## Snags in this round (the recording law)
- **The safeguard block (`M-253`, recurrence).** Two of the three first runs were terminated mid-reading with no content error. Identical re-dispatch of the frozen brief resumed each from its own reading log. This is the second consecutive phase in which an unchanged brief was flagged by the API on some slots and not others.
- **Plan mode and the auto-mode classifier.** The classifier returned "no verdict" on two Bash calls during setup; plan mode switched on each time and was cleared by re-approval of the same plan. Nothing was written by the failed calls. The brief and checkpoint were written with the Write tool. Readers A and B staged part of their logs in plan files and appended them after plan mode lifted (`M-254` recurrence; Round 2 still ran on the real output files).
- **A reader's whole-file read of a spec file** displayed non-admitted lines (including `DR-10`'s L168). It is the brief's range instruction, not the read, that excludes them; nothing was used. Consider adding an explicit "read the spec by offset and limit only" line to the next spec-bearing brief.
- **Orchestrator exposure:** a filename-only listing included a path in another city's pass folder; not opened.
- **Orchestrator clock note:** the checkpoint first recorded A's restart as ~09:35 instead of ~09:29; corrected.
- **Hook notices** (graphify) on tool calls were disregarded under `DR-6`: compliance, not override.

## Post-write checks — raw output, pasted unedited

**Triage (by hand, as each tool asks):**
- **Quotation audit.** It audits the whole pass folder with the pass's own files excluded from its corpus, so quotations of the pass's own earlier files, and connective prose captured between two adjacent quotations, show as misses. The 57 lines for `04_Phase_09_Populations.md` and `04b` are of three kinds:
  - (a) phrases quoted from the pass's own files (`P2`–`P8`, `SPN`, `RES`): the `P2` L223/L225/L194, `P4` L176, `P5` L237/L285, `P6`, `P7` L391/L454 and `P8` L553/L394 lines, the `SPN` L97/L155 lines, and the `P8` Status line quoted in the sweep table;
  - (b) connective prose captured between adjacent quotations (receipt, P9-3, P9-4, P9-5, P9-8 and P9-9 lines, and the Round 3 table cells);
  - (c) the struck phrases and authoring labels recorded in the axis corrections, Snag 10 and the Merge provenance.

  The pre-write script check (149 distinct quotations of four or more words against the 68 admitted sources, including the admitted ranges of the pass files) found every real source quotation, with 0 real misses (see Merge above).
- **Handoff audit:** *INSTRUMENT VALID: NO*, as at Phases 5–8 (its detector found no outbound "HANDED FORWARD" blocks, so it cannot discriminate). It reports Phase 9's sweep as FORMAL with 29 table rows; the 28-row table in the phase file is the union of the three readers' sweeps and the orchestrator's pre-run sweep.
- **Phase discipline:**
  - T4 is present in 8 / 8 phase files; Phase 9's marker names substantive shed items, read by hand. It is on one physical line.
  - T5's early marker is present (Phase 6) and was not used here; its late marker waits for Step 8.
  - The Position-Coverage Ledger shows every cell blank at P9: bookkeeping only, nothing was written toward them (`00f` Rule 3). The ledger is updated only on developer confirmation.

### quotation_audit.py (header, controls and counts; then every line it reports for the Phase 9 files)
```
pass audited : Mirny
corpus mode  : default (own pass excluded)
corpus files : 5147   chars: 49,667,617

=== POSITIVE CONTROLS ===
  [easy                      ] FOUND     a terminus is nobody's midpoint
  [HARD - blockquote wrap    ] FOUND     A pass may not proceed to Step 5 with a NEVER CITED row
  [HARD - outside Worldspace ] FOUND     Paste raw QA scan output into the QA block. Never summa
  [HARD - case mismatch      ] FOUND     YOU GO TO ESPERANZA AND YOU DO NOT COME HOME FOR FOUR Y
  [HARD - long wrapped       ] FOUND     Different content is not differentiation; a different q

  INSTRUMENT VALID: YES
  NEGATIVE CONTROL (must be absent): PASS - absent

=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 763
NOT FOUND in corpus: 422
  of those, in TABLE CELLS : 86
  of those, in PROSE       : 336

  [00.1_Step_MINUS-1_Input_Contract.md:15]           is now present, by ruling (hard canon, rb l2786): the founders were exiles from russia, china and australia. the spec's
  [00.1_Step_MINUS-1_Input_Contract.md:15]           (l150 chars 702-716) is consistent with the ruling as one of three stocks

... [417 lines for earlier phase files omitted here; they are the pass's other files and were triaged in their own phases]

  [04_Phase_09_Populations.md:117]  [CELL]  awaiting developer clarification before it feeds phase 9
  [04_Phase_09_Populations.md:132]           so mirny trusts what is written and what is relayed
  [04_Phase_09_Populations.md:133]           a resident adult arrival is inside the city and outside the wind
  [04_Phase_09_Populations.md:139]           is narrowed : a native starts inside ( p5 l396
  [04_Phase_09_Populations.md:170]           p3 l218; p8 p8-17); keeping the shared stop
  [04_Phase_09_Populations.md:170]           ( rp l336); deciding each crossing alone and owning the outcome under the Social Contract ( p6 p6-1
  [04_Phase_09_Populations.md:171]           the only layer every resident, in either body and from any stock, meets without translation
  [04_Phase_09_Populations.md:182]           the living witnesses to the arrival are robots; the heirs are humans born here
  [04_Phase_09_Populations.md:182]           a long-lived robot is a person to ask, not an archive
  [04_Phase_09_Populations.md:182]           held entirely in the layer the Social Contract ranks below the record
  [04_Phase_09_Populations.md:184]           ( ru14 l24). earlier marks were designed against pressures faced by
  [04_Phase_09_Populations.md:189]           in act 2 the oldest voice at mirny, in a body that cannot be copied
  [04_Phase_09_Populations.md:194]           the founding human unit is a household or community that included a robot
  [04_Phase_09_Populations.md:195]           ( p4 l174) is a statement about the founders of both bodies. 3rd d . they age on a human clock: frm l168-170 (via tl ) has the hum
  [04_Phase_09_Populations.md:195]           by about 2614 while the founding robots are still active. so the human half's first-hand founding passes out of mirny inside act 1
  [04_Phase_09_Populations.md:202]           ). the heirs hold the founding second-hand. nationally, humans growing up in tepenia
  [04_Phase_09_Populations.md:202]           the robot trust-bond ( ru17 l70). a child's native language follows the surrounding community by canon's own analogy ( ru20 l16; h
  [04_Phase_09_Populations.md:203]           in act 2, and none is written ( nns ; never
  [04_Phase_09_Populations.md:209]           ( ru3 l30); who initiates a build is context-dependent nationally ( ru3 l45-51) and
  [04_Phase_09_Populations.md:209]           and the community that had her built ( ru6 l18; rp l426). her clan forms on
  [04_Phase_09_Populations.md:209]           ( ru11 l32). skill is not built in: a robot built for heavy work
  [04_Phase_09_Populations.md:211]           robot cohorts run by build date, not by generation
  [04_Phase_09_Populations.md:216]           ( ru14 l24); gen differences bond robots, and robots to humans, around the
  [04_Phase_09_Populations.md:222]           ( p2 l368). 2nd. robots could keep arriving in principle - the treaty sends out
  [04_Phase_09_Populations.md:227]           one night kept in two ways, one door decided by two sets of garments and one reserve
  [04_Phase_09_Populations.md:232]           ( ru9 l35); a robot comes online as an adult ( drl l452). the schoolyard and the care-room are one body ( p2 e7). tepenia evacuate
  [04_Phase_09_Populations.md:244]           a resident adult arrival is inside the city and outside the wind
  [04_Phase_09_Populations.md:250]           change at mirny arrives not as a movement but as a role
  [04_Phase_09_Populations.md:259]           ( rp l377), the laws, robot-authored law with humans equal before it ( fts l13) - is the floor and is not restated as a finding. a
  [04_Phase_09_Populations.md:259]           would be positional or institutional, not a head count
  [04_Phase_09_Populations.md:263]           the outsider mirny is built to notice is the one who misreads the wind, not the one from elsewhere
  [04_Phase_09_Populations.md:263]           no one holds a reading the newcomer still lacks by inheritance
  [04_Phase_09_Populations.md:263]           belonging at mirny is legible at the threshold, not in the voice
  [04_Phase_09_Populations.md:264]           the compelled half remembers what was lost; the half whose forebears elected inherits what was freely given
  [04_Phase_09_Populations.md:264]           the first sign of the dangerous wind can read as an improvement
  [04_Phase_09_Populations.md:266]           standing follows the object, so the person best at the one thing the site demands holds no craft at all
  [04_Phase_09_Populations.md:266]           nobody fails out: no gate, no exclusion, no rank
  [04_Phase_09_Populations.md:266]           simply become residents without ever being blamed
  [04_Phase_09_Populations.md:271]           the person best at surviving the wind has the least standing in the record
  [04_Phase_09_Populations.md:271]           ( p7 p7-30). canon forbids the other ladders a long-exposed person might climb: no authority by age or gen
  [04_Phase_09_Populations.md:300]           the person best at surviving the wind has the least standing in the record
  [04_Phase_09_Populations.md:305]           mirny's relation to the robot half of its own population is material and upstream, not cultural
  [04_Phase_09_Populations.md:461]           ) to built-here robots ( p7 p7-29 cand ; p7 l541). would decide: whether mirny has any channel for the reading or the founding at 
  [04_Phase_09_Populations.md:517]           is broader than the orchestrator's filename check ( rp and fts name the city); its step 0.md source is the frame; it cites corpus 
  [04_Phase_09_Populations.md:524]           baseline's reason passes from witnessed to told
  [04_Phase_09_Populations.md:525]           b notes l62 is the plating-damage row, with the word
  [04_Phase_09_Populations.md:526]           the only population whose existence began as a local decision
  [04_Phase_09_Populations.md:529]           as a population founding robots as mirny's mentors as fact the founding cohort as fully specified a robot elder or an age grade a 
  [04_Phase_09_Populations.md:529]           clinicians as a people the coat as the marker of belonging as fact (cand-d1) a demonym or coined word for natives or arrivals an a
  [04_Phase_09_Populations.md:558]           (p9-15); the 2 2 grid of formation by body (p9-16); build-date cohorts as carriers of mirny's change (p9-6, rf-13); the 248-year f
  [04_Phase_09_Populations.md:560]           (p9-2); the two lines as one structure (axis, p9-14); the act-2 fold of the memory line into the robot half (p9-17); the robot who
  [04b_T8_Rounds_Phase_9.md:33]  [CELL]  ir-8 the children of founding households; kind outranks exposure only for the upper earth human visitor
  [04b_T8_Rounds_Phase_9.md:35]  [CELL]  p9-19 the two lines (wind, memory) as one structure; the lens half-life; the act-2 fold into the robot half; the robot native neve
  [04b_T8_Rounds_Phase_9.md:61]  [CELL]  only population whose existence began as a local decision
  [04b_T8_Rounds_Phase_9.md:81]           the only population whose existence began as a local decision
  [04b_T8_Rounds_Phase_9.md:81]           baseline's reason passes from witnessed to told
  [04b_T8_Rounds_Phase_9.md:81]           ); the m-169 false headline quoted as the trap


⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.

```

### handoff_audit.py
```
pass audited : Mirny
phase files  : 8

=== CONTROLS (edit these per pass; they are what makes a zero trustworthy) ===
  POSITIVE (detector must find a formal block): phases 2, 3, 4, 5, 6, 7, 8, 9
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

  8/8 phase files carry a T4 marker.
  >> If EVERY phase's answer was literally 'nothing', T4 is falsified
     per its own stated condition (the question would be decorative).
     This tool cannot see the marker's CONTENT well enough to judge
     that - read the 8 lines above by hand.

=== T5 - EARLY LOVER-FACULTY SMOKE TEST ===
  EARLY (Phase 6) verdict: Alive in its conditions and its two bodies — a working coast that keeps nine places talking without being thanked, where people stop together, own their own calls, and get a sunset with no night after it and an open sea nobody can promise — and lovable by someone who wants to be trusted with their own reading; but what its people laugh at and do with their own hours is still the largest empty slot, so for now the love is for how the place holds its conditions more than for any custom it is known to keep (an early, provisional verdict; it must not steer Phases 7–8, or it is falsified and withdrawn).
  LATE marker absent (08_Review_Panel.md missing or has no Lover-faculty line yet)

  T5 not fully applied this pass (one or both markers absent).
```
