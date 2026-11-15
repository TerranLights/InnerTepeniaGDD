# Round record — Casey · Step 4, Phase 3 (Surface & Texture)

**Output:** `04_Phase_03_Surface_and_Texture.md` (581 lines) and Session 2 of `Cities/Research_Logs/Casey_Research_Log.md` (appended, 208 lines; the log now 730 lines). Casey's warm ULM run under `STARTUP_Mirny_Review_then_Casey_ULM_2026-11-11.md` Part B item 3: three readers, Round 2, Round 3, one fresh merge writer (`M-246`), the quotation audit run before this record existed, the American English sweep, the handoff audit and the phase discipline check. Every tool output below is pasted whole. PROPOSED; nothing declared complete.

## Round 0 — the reading list and the frozen briefs

Briefs `.t8_04_Phase_3_brief_A.md`, `_B.md`, `_C.md` (141 lines each; written new for Casey from the runbook, the spine and the Phase 2 brief on disk; standing lines 1–6, 10, 11 verbatim; A and B differ only in the slot, checked by `diff`; brief C read end to end before dispatch). Merge brief `.t8_04_Phase_3_merge_brief.md`. List decisions: Casey's log CL-24. The list, `.t8_required_04_Phase_3.txt` (18 entries):

```
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md :: 82-272,472-531
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md :: 1966-2041,2062-2069,2320-2361,2645-2758
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Climate Data/READER/Casey.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Climate Data/Precipitation_Falls_vs_Lands.md :: 1-6,18-62,65-68,73-76,79-91,95-98,147-150,158
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Cold_Physiology.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00b_General_Population_Discipline.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00d_Shadow_Proportion_Discipline.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Casey.md :: 1-3,5-83,85,87-93,95-107,110,112-121,125-152,154-155,157-159,166-170,172,174-180,182,184,186,188-200,202,204-207,212-214,243-244,248-249
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/00.1_Step_MINUS-1_Input_Contract.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/00.1_Step_MINUS-1_Amendment_2026-11-11.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/00_Frame.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/01_Inherited.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/02_Spine.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/03_Research.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_02_Composition_and_Arrival.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/Datasheets/Phase_3.md :: 1-12,15,18,20,22-28
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md :: 1707-1715,1944-1951,1989-1996
```

## Round 1 — three readers, each in a private staging folder

Dispatched 2026-11-15 05:40, three Opus readers, one message: A `a36e4bf06f147d907`, B `a836c267fd37274dc`, C `ae1376d81ed8c05c8`; staging `scratchpad/casey/phase3/reader<X>/`. Outputs copied into Casey's folder after Round 2 (standing line 9).

| Reader | Output | Lines | Findings | Handed forward | Developer questions | Web calls |
|---|---|--:|--:|--:|--:|--:|
| A | `.t8_04_Phase_3_readerA.md` | 561 | 29 | 12 | 2 | 21 (16 searches, 5 fetches) |
| B | `.t8_04_Phase_3_readerB.md` | 523 | 22 | 10 | 1 | 15 (11 searches, 4 fetches) |
| C | `.t8_04_Phase_3_readerC.md` | 571 | 29 | 14 | 1 | 21 (15 searches, 6 fetches) |

*The counts are as each reader reported them in its reply; the line counts are `wc -l` on the copied files.*

## Round 2 — `Tools/triple_read_verify.py` (last change 2026-11-03), raw output, whole (95 lines; `.t8_04_Phase_3_round2_raw.txt`)

```
required files: 18
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 82-272,472-531] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 1966-2041,2062-2069,2320-2361,2645-2758] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Climate Data/READER/Casey.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Climate Data/Precipitation_Falls_vs_Lands.md  [range 1-6,18-62,65-68,73-76,79-91,95-98,147-150,158] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Cold_Physiology.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_02_Composition_and_Arrival.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/Datasheets/Phase_3.md  [range 1-12,15,18,20,22-28] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 1707-1715,1944-1951,1989-1996] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

## Round 3 — each reader continued by `SendMessage` with the other two outputs

Messages built from `scratchpad/casey/tools/phase3_round3_template.txt` (sections 1–4 per reader; 5 dispositions; 6 figures recomputed; 7 T3 marks; 8 the `T4 - SHED:` line; 9 web calls, up to 15 each). Replies saved the moment each arrived (standing line 9):

| Reader | Reply | Lines | Verdict lines, as written in the reply (cut at the reason) | Web calls |
|---|---|--:|---|--:|
| A | `.t8_04_Phase_3_round3_readerA.md` | 171 | 4. VERDICT: CONSISTENT — B read the same · 4. VERDICT: CONSISTENT — C read the same | 3 |
| B | `.t8_04_Phase_3_round3_readerB.md` | 140 | VERDICT: CONSISTENT · VERDICT: CONSISTENT | 2 |
| C | `.t8_04_Phase_3_round3_readerC.md` | 197 | VERDICT: CONSISTENT · VERDICT: CONSISTENT | 2 |

**Verdicts: all six CONSISTENT.** Each reply carries sections 5 to 9 and one `T4 - SHED:` line (checked with `grep -c`).

## The merge — one fresh writer (`M-246`)

Dispatched after Round 3: `a966dcdd59cd243a3` (Opus). Returned `04_Phase_03_Surface_and_Texture.md` (581 lines; P3-1 to P3-42; 32 inbound sweep rows; 22 HANDED FORWARD rows; DQ-13, DQ-14; REQ-42; PA-10, PA-11; no new reserved finding) and Session 2 of the research log (64 call rows; OT-35 to OT-53). `git diff --numstat` on the log: `208 0` (insertions only).

## Research-log strings against the readers' own tables — `scratchpad/casey/tools/check_session2_strings.py` (written this morning), raw output, whole (2 lines; `.t8_04_Phase_3_log_strings_raw.txt`)

```
rows 64 · verbatim found 64 · missing 0
per reader/round: A-R1 21 A-R3 3 B-R1 15 B-R3 2 C-R1 21 C-R3 2
```

## Normalized quotation pre-check (standing line 13) — `scratchpad/casey/tools/quote_precheck.py` (written this morning), raw output, whole (1 lines; `.t8_04_Phase_3_quote_precheck_raw.txt`)

```
quoted strings (2+ words): 49 · found 49 · not found 0
```

## Quotation audit — `Tools/quotation_audit.py` (last change 2026-11-02), `--files 04_Phase_03_Surface_and_Texture.md --own-pass`, raw output, whole (28 lines; `.t8_04_Phase_3_quotation_audit_raw.txt`)

```
pass audited : Casey
corpus mode  : default (own pass excluded)
corpus files : 7119   chars: 115,017,011
files audited: 04_Phase_03_Surface_and_Texture.md
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
fragments tested (single-line, ellipsis-split, >=7 words): 31
NOT FOUND in corpus: 2
  of those, in TABLE CELLS : 0
  of those, in PROSE       : 2

  [04_Phase_03_Surface_and_Texture.md:86]           at this latitude as the warmest and coolest parts of the 24-hour cycle (spec l145) (a)
  [04_Phase_03_Surface_and_Texture.md:344]           (spec l137), 2.7 h of daylight; july 4.0 h, mean -14.7 c, average low -18.4 c, record low -36.4 c

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```

**Triage of the misses** (orchestrator; table `.t8_04_Phase_3_quotation_triage.md`): 2 misses: 2 CONNECTIVE, 0 DOT, 0 SELF, **0 MISQUOTE**. The audit does not read dot-files, so quotations of the readers' outputs and replies are checked by no tool except the pre-check above.

## American English sweep — a pattern of British forms (`scratchpad/casey/tools/ame_pattern.txt`), over the phase file and the log's Session 2, raw output, whole (27 lines; `.t8_04_Phase_3_ame_sweep_raw.txt`)

```
== 04_Phase_03_Surface_and_Texture.md
85:rises
111:rising
112:rises
113:rises
114:rising
130:rises
151:raised
151:raised
151:raises
152:raised
153:raised
185:rising
208:promises
327:raised
330:raised
331:raised
354:rises
422:raised
430:raised
442:raised
451:raised
554:raised
== Casey_Research_Log.md
563: rising
615: raises
703: Raised
```

**Every hit is a false positive of the `-ise` pattern** (rise, raise, promise). **0 British forms.**

## Handoff audit — `Tools/handoff_audit.py` (last change 2026-10-21), raw output, whole (56 lines; `.t8_04_Phase_3_handoff_audit_raw.txt`)

```
pass audited : Casey
phase files  : 2

=== CONTROLS (edit these per pass; they are what makes a zero trustworthy) ===
  PHASES WITH A FORMAL SWEEP BLOCK (found in this pass): 2, 3
  PHASES WITH NO TRACE OF A SWEEP (found in this pass)  : none
  SELF-TEST (fixed positive and negative strings)       : passed
  INSTRUMENT VALID: YES - the detector separates a formal block from no block on the built-in controls

  phase | outbound | sweep    | rows | verdict
  ------+----------+----------+------+---------
      2 |        0 | FORMAL   |   16 | n/a - nothing addressed to it
      3 |        1 | FORMAL   |   32 | reconcile 32 enumerated against 1 outbound

TOTAL outbound handoff rows: 30
PHASES WITH ROWS ADDRESSED TO THEM AND NO ENUMERATION: 0

=== outbound rows, per target, for hand reconciliation ===
  -> Phase 3:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 3** | What of the inherited base was not carried over, whether the loss lasted
  -> Phase 4:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 4** | Whose ordinary day (spine L468): the general population is the born-here
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 4** | The research capacity of spec L195, at the step that reads V10 (`01_Inhe
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 4** | The shut half's closed population and the seasonal weight of winter skil
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 4** | S3-39 turned inward [PA-5]: the flow, travelers and crews as a possible 
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 4** | The day's physical structure for both bodies: outdoors and the heated do
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 4** | Whose ordinary day hears the season underfoot: the squeak half equals th
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 4** | For robots, a storm registered through the walls in heated rest (P3-16 →
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 4** | Questions only: calm days carry sound across frozen bays (P3-15, inferen
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 4** | REQ-32: admit split spec lines by part at the step that first uses them;
  -> Phase 5:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 5** | Who the visitor is (spine L468): the flow (travelers, convoys, ship crew
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 5** | The closing as the year's decision point for anyone at Casey by sea; att
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 5** | The instrument's later doors: electors (II.2.5), later-exiled robots (II
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 5** | First impressions of those who arrive, by sea, by road [PA-5] and for th
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 5** | The internal map that changes with the season (P3-35 →2, (c)): water div
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 5** | The decision point's danger sign: calm from the sea while cold builds on
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 5** | Signs of summer that are not access: the sea opens at the island coasts 
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 5** | The working city's ground-bound buildings and their dug-out doors, scope
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 5** | REQ-32, as for Phase 4 | sweep row 31 · P3C sweep row 20 |
  -> Phase 6:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 6** | Necessity Before Meaning: what moral, if any, was hung on the founding w
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 6** | A warning for Phases 6 to 9: the native layer must not be written as wea
  -> Phase 7:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 7** | The founding administration (II.4) and local councils (I.4): who held it
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 7** | The records' keepers: who keeps and reads them, on what terms, and wheth
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 7** | Heat and arrival: whether any rule decides who is given heated rest to w
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 7** | Who decided what of the inherited base was kept (`04_Phase_02` L486; P3-
  -> Phase 8:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 8** | Languages outside the supporting tier (`01_Inherited` L295; S1-14): hous
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 8** | What Casey builds with: no admitted material (P3-8); the country rock as
  -> Phase 9:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 9** | Which populations exist (spine L468): exile-era robots, sent and a persi
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 9** | The robot body at Casey: hearing direction (P3-16, under DQ-14); the che
  -> Phase 10:
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 10** | Naming places from what they look like: scoured crests, lee drifts, whi
```

## Phase discipline check — `Tools/phase_discipline_check.py` (last change 2026-10-21), raw output, whole (34 lines; `.t8_04_Phase_3_phase_discipline_raw.txt`)

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
  [04_Phase_03_Surface_and_Texture.md]  T4 present: the 42 origin stocks and every composition share beyond the two bodies' halves, the founde

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

*The T3 rows above were printed before the ledger's P3 column was marked; the ledger was updated right after (see Notes).*

## Notes

**Handoff audit, reconciled by hand.** Inbound: the tool sees one row addressed `**Phase 3**` (`04_Phase_02` L486); the phase file's sweep enumerates 32 rows (that row, the two `**Step 4**` rows, the every-phase items of the Frame, Step 1, the contract and the amendment, and items the readers found). Outbound: the file's HANDED FORWARD table holds 22 rows; the tool lists the 15 addressed to Phases 4 to 10 (rows to Steps 3, 5, 6, 7 and 10 are outside its form); two further items are carried outside the pass (the histories after the ULM; one routing point for the orchestrator).

**Position-coverage ledger (T3).** The P3 column of `00.2_Position_Coverage_Ledger.md` was copied by the orchestrator from the phase file's `## T3 · Position coverage` (L470-484): The Passer-Through covered; the other eight blank, each with its reason there.

**Developer questions** DQ-13 and DQ-14 filed as DEC-522 and DEC-523 in `Research_Logs/DECISIONS_NEEDED_FROM_DEVELOPER.md` (the Casey section, above `## Answered`). REQ-42 and PA-10, PA-11 are recorded in the phase file.

**Web calls:** 57 in Round 1 and 7 in Round 3 (64), every one logged verbatim in the research log's Session 2 and checked against the readers' own tables (64 of 64). Session web total after the merge: see the progress file.

**Readers' staging folders:** A and C each hold only their output and their Round 3 reply; B holds those and its own read-only notes file (checked with `ls`).

