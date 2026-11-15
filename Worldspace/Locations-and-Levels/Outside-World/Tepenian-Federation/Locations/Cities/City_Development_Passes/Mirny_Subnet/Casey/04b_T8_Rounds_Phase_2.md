# Round record — Casey · Step 4, Phase 2 (Composition & Arrival)

**Output:** `04_Phase_02_Composition_and_Arrival.md` (665 lines). Casey's warm ULM run under `STARTUP_Mirny_Review_then_Casey_ULM_2026-11-11.md` Part B item 3: three readers, Round 2, Round 3, one fresh merge writer (`M-246`), the quotation audit run before this record, the American English sweep. Everything in the output is PROPOSED. Record written 2026-11-11 13:12 by `scratchpad/casey/tools/casey_phase_record.py`.

## Round 0 — the reading list and the frozen briefs

Briefs `.t8_04_Phase_2_brief_A.md`, `_B.md`, `_C.md` (written new for Casey; standing lines 1–6, 10, 11 verbatim). The list, `.t8_required_04_Phase_2.txt`:

```
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md :: 82-272,401-469
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md :: 2090-2319,2662-2758
/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md
/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Falkland_Treaty/Falkland_Treaty_Draft_v1.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md :: 1-41,380-386,497,641
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Founding_Register.md :: 1-37,58
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Upper_Earth_Immigration_Composition.md :: 28-35,631,639
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00b_General_Population_Discipline.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00d_Shadow_Proportion_Discipline.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Casey.md :: 1-3,5-83,85,87-93,95-107,110,112-121,125-152,154-155,157-159,166-170,172,174-180,182,184,186,188-200,202,204-207,212-214,243-244,248-249
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/00.1_Step_MINUS-1_Input_Contract.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/00.1_Step_MINUS-1_Amendment_2026-11-11.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/00_Frame.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/01_Inherited.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/02_Spine.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/03_Research.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/Datasheets/Phase_2.md :: 1-17,19-23,26-30
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md :: 203-253,463-476,1523-1531,1550-1558,1707-1715,1944-1951
```

## Round 1 — three readers, each in a private staging folder

| Reader | Agent ID | Output (copied here) | Lines |
|---|---|---|---|
| A | `a463f95a777c3bd55` | `.t8_04_Phase_2_readerA.md` | 590 |
| B | `a0d3af42e64eb297a` | `.t8_04_Phase_2_readerB.md` | 648 |
| C | `a7e9f023351ac5e74` | `.t8_04_Phase_2_readerC.md` | 565 |

## Round 2 — `Tools/triple_read_verify.py` (last change 2026-11-03), raw output, whole (100 lines)

```
required files: 19
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 82-272,401-469] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2090-2319,2662-2758] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Falkland_Treaty/Falkland_Treaty_Draft_v1.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md  [range 1-41,380-386,497,641] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Founding_Register.md  [range 1-37,58] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Upper_Earth_Immigration_Composition.md  [range 28-35,631,639] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00b_General_Population_Discipline.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00d_Shadow_Proportion_Discipline.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Casey.md  [range 1-3,5-83,85,87-93,95-107,110,112-121,125-152,154-155,157-159,166-170,172,174-180,182,184,186,188-200,202,204-207,212-214,243-244,248-249] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/00.1_Step_MINUS-1_Input_Contract.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/00.1_Step_MINUS-1_Amendment_2026-11-11.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/00_Frame.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/01_Inherited.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/02_Spine.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/03_Research.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/Datasheets/Phase_2.md  [range 1-17,19-23,26-30] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 203-253,463-476,1523-1531,1550-1558,1707-1715,1944-1951] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

## Round 3 — each reader continued by `SendMessage` with the other two outputs

| Reader | Reply (copied here) | Lines |
|---|---|---|
| A | `.t8_04_Phase_2_round3_readerA.md` | 178 |
| B | `.t8_04_Phase_2_round3_readerB.md` | 201 |
| C | `.t8_04_Phase_2_round3_readerC.md` | 177 |

**Verdicts, as each reply's own verdict lines state them: all six CONSISTENT.** Each reply's sections 5 and 6 (disposition differences; recomputed figures) went to the merge writer whole.

## The merge — one fresh writer (`M-246`)

Agent `ab0430c026fe56608`; brief `.t8_04_Phase_2_merge_brief.md`; output `04_Phase_02_Composition_and_Arrival.md`.

## Quotation audit — raw output, whole (35 lines; `.t8_04_Phase_2_quotation_audit_raw.txt`)

```
pass audited : Casey
corpus mode  : default (own pass excluded)
corpus files : 7119   chars: 114,957,855
files audited: 04_Phase_02_Composition_and_Arrival.md
own-pass mode: a quotation may also be found in this pass's OTHER files (never in its own file)

=== POSITIVE CONTROLS ===
  [easy                      ] FOUND     a terminus is nobody's midpoint
  [HARD - blockquote wrap    ] FOUND     A pass may not proceed to Step 5 with a NEVER CITED row
  [HARD - outside Worldspace ] FOUND     Paste raw QA scan output into the QA block. Never summa
  [HARD - case mismatch      ] FOUND     YOU GO TO ESPERANZA AND YOU DO NOT COME HOME FOR FOUR Y
  [HARD - long wrapped       ] FOUND     Different content is not differentiation; a different q

  INSTRUMENT VALID: YES
  NEGATIVE CONTROL (must be absent): PASS - absent

=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 73
NOT FOUND in corpus: 9
  of those, in TABLE CELLS : 0
  of those, in PROSE       : 9

  [04_Phase_02_Composition_and_Arrival.md:138]           written into the tier row (census l384). the station builder is a coordinate only (nns l5, l32), and the spec's real-station ranki
  [04_Phase_02_Composition_and_Arrival.md:158]           (physiology l67) and die in incidents, many at once or none for a long while (l103-107); human death is continuous
  [04_Phase_02_Composition_and_Arrival.md:213]           (ii.3.2, l54), with no requirement that the population
  [04_Phase_02_Composition_and_Arrival.md:213]           (ii.3.3, l55). the spine's assigned mode produces a rotation clock
  [04_Phase_02_Composition_and_Arrival.md:216]           (physiology l360), and the settlement aid is not to be construed
  [04_Phase_02_Composition_and_Arrival.md:295]           in assembly territory must depart (ii.2.1, l46): compelled. any human may
  [04_Phase_02_Composition_and_Arrival.md:295]           at any time after the effective date, relinquishing
  [04_Phase_02_Composition_and_Arrival.md:295]           (ii.2.5, l50; added 2026-11-09, l138), under the return bar of iv.2.3; such a person
  [04_Phase_02_Composition_and_Arrival.md:295]           (l50). each party may designate observers with

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```

**Triage of the misses** (agent `orchestrator`; table `.t8_04_Phase_2_quotation_triage.md`): 9 misses: 9 CONNECTIVE, 0 DOT, 0 SELF, **0 MISQUOTE**. Nothing changed by the triage.

## American English sweep — raw output, whole

```

```

## Handoff audit — `Tools/handoff_audit.py` (last change 2026-10-21), raw output, whole (39 lines; `.t8_04_Phase_2_handoff_audit_raw.txt`)

```
pass audited : Casey
phase files  : 1

=== CONTROLS (edit these per pass; they are what makes a zero trustworthy) ===
  PHASES WITH A FORMAL SWEEP BLOCK (found in this pass): 2
  PHASES WITH NO TRACE OF A SWEEP (found in this pass)  : none
  SELF-TEST (fixed positive and negative strings)       : passed
  INSTRUMENT VALID: YES - the detector separates a formal block from no block on the built-in controls

  phase | outbound | sweep    | rows | verdict
  ------+----------+----------+------+---------
      2 |        0 | FORMAL   |   16 | n/a - nothing addressed to it

TOTAL outbound handoff rows: 15
PHASES WITH ROWS ADDRESSED TO THEM AND NO ENUMERATION: 0

=== outbound rows, per target, for hand reconciliation ===
  -> Phase 3:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 3** | What of the inherited base was not carried over, whether the loss lasted
  -> Phase 4:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 4** | Whose ordinary day (spine L468): the general population is the born-here
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 4** | The research capacity of spec L195, at the step that reads V10 (`01_Inhe
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 4** | The shut half's closed population and the seasonal weight of winter skil
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 4** | S3-39 turned inward [PA-5]: the flow, travelers and crews as a possible 
  -> Phase 5:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 5** | Who the visitor is (spine L468): the flow (travelers, convoys, ship crew
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 5** | The closing as the year's decision point for anyone at Casey by sea; att
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 5** | The instrument's later doors: electors (II.2.5), later-exiled robots (II
  -> Phase 6:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 6** | Necessity Before Meaning: what moral, if any, was hung on the founding w
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 6** | A warning for Phases 6 to 9: the native layer must not be written as wea
  -> Phase 7:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 7** | The founding administration (II.4) and local councils (I.4): who held it
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 7** | The records' keepers: who keeps and reads them, on what terms, and wheth
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 7** | Heat and arrival: whether any rule decides who is given heated rest to w
  -> Phase 8:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 8** | Languages outside the supporting tier (`01_Inherited` L295; S1-14): hous
  -> Phase 9:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 9** | Which populations exist (spine L468): exile-era robots, sent and a persi
```

## Phase discipline check — `Tools/phase_discipline_check.py` (last change 2026-10-21), raw output, whole (32 lines; `.t8_04_Phase_2_phase_discipline_raw.txt`)

```
pass audited : Casey

=== T3 - POSITION-COVERAGE LEDGER ===
  phases in header: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Child              filled=1  blank=8   blank at: P3, P4, P5, P6, P7, P8, P9, P10
  The Lover (position)   filled=1  blank=8   blank at: P3, P4, P5, P6, P7, P8, P9, P10
  The Parent             filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Ruler              filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Elder              filled=1  blank=8   blank at: P3, P4, P5, P6, P7, P8, P9, P10
  The Mentor             filled=1  blank=8   blank at: P3, P4, P5, P6, P7, P8, P9, P10
  The Passer-Through     filled=1  blank=8   blank at: P3, P4, P5, P6, P7, P8, P9, P10
  The Neighbor           filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  ⭐ The Lover FACULTY    filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10

  NOTE: a blank cell is a WARNING BEFORE Step 8, not a defect. Do not
  fill a blank by writing new phase content toward it - that is the
  contamination 00f Rule 3 forbids (see the recipe's hard bound on T3).

=== T4 - PER-PHASE SHED MARKER ===
  [04_Phase_02_Composition_and_Arrival.md]  T4 present: the 42 origin stocks as a sorting line: which nations are present, any row or share beyond

  1/1 phase files carry a T4 marker.
  >> If EVERY phase's answer was literally 'nothing', T4 is falsified
     per its own stated condition (the question would be decorative).
     This tool cannot see the marker's CONTENT well enough to judge
     that - read the 1 lines above by hand.

=== T5 - EARLY LOVER-FACULTY SMOKE TEST ===
  EARLY marker absent in (no Phase 6 file found)
  LATE marker absent (08_Review_Panel.md missing or has no 'T5 - LATE LOVER FACULTY:' line yet)

  T5 not fully applied this pass (one or both markers absent).
```

## Notes

**List decisions made before dispatch** are recorded in Casey's log, CL-19 (the treaty folder resolved to the draft; the composition file admitted at L28–35, L631, L639; three datasheet rows kept out; the rulings-log spans).

**Handoff audit, reconciled by hand.** Outbound: the tool lists 15 rows addressed to Phases 3–9; the file's HANDED FORWARD table holds 23 rows, the other 8 addressed to Steps 4, 5, 6, 7 and 10, which the tool does not count (it reads `| **Phase N** |` only). Inbound: the tool classifies Phase 2's sweep as FORMAL and prints 16 for its rows; the file's `## INBOUND HANDOFF SWEEP` table holds 44 data rows (L52–L95): rows 1–16 are the 16 rows addressed `**Phase 2**` in `01_Inherited.md` (8), `02_Spine.md` (5) and `03_Research.md` (3), and rows 17–44 are items the readers found in the Frame, the contract and the amendment. Nothing addressed to Phase 2 lacks a row. The tool reads outbound rows only from `04_Phase_*` files, so the 16 earlier rows show as "0 outbound" against Phase 2 (its own line: "n/a - nothing addressed to it").

**Position-coverage ledger (T3).** The P2 column of `00.2_Position_Coverage_Ledger.md` was copied by the orchestrator from the phase file's `## T3 · Position coverage` section (L544–L558): five covered (The Child, The Lover *(position)*, The Elder, The Mentor, The Passer-Through), four blank with reasons in that section. The discipline check above was run after the copy. **T4:** the shed line is present (L560). **T5:** not yet due (Phase 6).

**Developer questions** DQ-11 and DQ-12 filed as DEC-520 and DEC-521 in `Research_Logs/DECISIONS_NEEDED_FROM_DEVELOPER.md`. No request, reserved finding or provisional assumption added; next unused keys DQ-13, REQ-42, RF-28, PA-10.

**Spelling:** 0 hits. **Readers' staging folders:** each holds only its output and its Round 3 reply (checked with `ls`).

This record does not grow after its line counts were taken (standing line 8).
