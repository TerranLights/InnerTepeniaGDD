# Round record — Casey · Step 4, Phase 8 (Making)

**Output:** `04_Phase_08_Making.md` (677 lines). No research-log session: Phase 8 had no web research (the brief's §1, last line). Casey's warm ULM run under `STARTUP_Mirny_Review_then_Casey_ULM_2026-11-11.md` Part B item 3: three readers, Round 2, Round 3, one fresh merge writer (`M-246`), the normalized quotation pre-check run before the audit, the quotation audit, the American English sweep, the handoff audit and the phase discipline check. Every tool output below is pasted whole. PROPOSED; nothing declared complete.

## Round 0 — the reading list and the frozen briefs

Briefs `.t8_04_Phase_8_brief_A.md`, `_B.md`, `_C.md` (142 lines each; written new for Casey from the runbook, the spine and the earlier briefs on disk; standing lines 1–6, 10, 11 verbatim; A and C differ only in the slot, checked by `diff`; brief B's head read before dispatch). Merge brief `.t8_04_Phase_8_merge_brief.md`. List decisions: Casey's log CL-35. The list, `.t8_required_04_Phase_8.txt` (24 entries):

```
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md :: 82-272,955-1022
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md :: 378-426,1966-2041,2320-2361,2645-2758
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Cold_Physiology.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Siligel_Composition_Research.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Sumerian_Language_in_Robot_Culture.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Weapons_and_Tools_Philosophy.md
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
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_03_Surface_and_Texture.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_04_Ordinary_Life.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_05_Relation_and_Geometry.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_06_Meaning.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_07_Order.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/Datasheets/Phase_8.md :: 1-2,6-13
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md :: 1664-1671,1707-1715,1944-1951,1989-1996
```

## Round 1 — three readers, each in a private staging folder

Dispatched 2026-11-15 09:55, three Opus readers, one message: A `ad320b549dadcfaf3`, B `a96d2731a01d9c84e`, C `a410944d23f0af2d8`; staging `scratchpad/casey/phase8/reader<X>/`. No web research. Outputs copied into Casey's folder after Round 2 (standing line 9).

| Reader | Output | Lines | Findings | Handed forward | Developer questions |
|---|---|--:|--:|--:|--:|
| A | `.t8_04_Phase_8_readerA.md` | 708 | 35 | 10 | 1 |
| B | `.t8_04_Phase_8_readerB.md` | 678 | 32 (P8B-32 folded into P8B-3) | 9 | 1 |
| C | `.t8_04_Phase_8_readerC.md` | 602 | 26 | 8 | 1 |

*The counts are as each reader reported them in its reply; the line counts are `wc -l` on the copied files.*

## Round 2 — `Tools/triple_read_verify.py` (last change 2026-11-03), raw output, whole (125 lines; `.t8_04_Phase_8_round2_raw.txt`)

```
required files: 24
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 82-272,955-1022] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 378-426,1966-2041,2320-2361,2645-2758] ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Siligel_Composition_Research.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Sumerian_Language_in_Robot_Culture.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Weapons_and_Tools_Philosophy.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_03_Surface_and_Texture.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_04_Ordinary_Life.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_05_Relation_and_Geometry.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_06_Meaning.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_07_Order.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/Datasheets/Phase_8.md  [range 1-2,6-13] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 1664-1671,1707-1715,1944-1951,1989-1996] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

## Round 3 — each reader continued by `SendMessage` with the other two outputs

Messages built from `scratchpad/casey/tools/phase8_round3_template.txt` (sections 1–4 per reader; 5 dispositions; 6 figures recomputed; 7 T3 marks; 8 the `T4 - SHED:` line; no web calls). Sent 2026-11-15 10:22. Replies saved the moment each arrived (standing line 9):

| Reader | Reply | Lines | Verdict lines, as written in the reply (cut at the reason) |
|---|---|--:|---|
| A | `.t8_04_Phase_8_round3_readerA.md` | 120 | VERDICT: CONSISTENT · VERDICT: CONSISTENT |
| B | `.t8_04_Phase_8_round3_readerB.md` | 101 | VERDICT: CONSISTENT · VERDICT: CONSISTENT |
| C | `.t8_04_Phase_8_round3_readerC.md` | 95 | VERDICT: CONSISTENT · VERDICT: CONSISTENT |

**Verdicts: all six CONSISTENT.** Each reply carries sections 5 to 8 and one `T4 - SHED:` line (checked with `grep -c`).

## The merge — one fresh writer (`M-246`)

Dispatched 2026-11-15 10:28 after Round 3: `a1cc6c181c9a1f8cf` (Opus). Returned `04_Phase_08_Making.md` (677 lines; P8-1 to P8-44; 84 inbound sweep rows; 13 HANDED FORWARD rows plus 5 items carried outside the pass; DQ-26; no new request, reserved finding or provisional assumption; REQ-33 discharged at P8-38; the `T4 - SHED:` line at L577).

## Normalized quotation pre-check (standing line 13), run before the audit — `scratchpad/casey/tools/quote_precheck.py` (written this morning), raw output, whole (1 lines; `.t8_04_Phase_8_quote_precheck_raw.txt`)

```
quoted strings (2+ words): 43 · found 43 · not found 0
```

## Quotation audit — `Tools/quotation_audit.py` (last change 2026-11-02), `--files 04_Phase_08_Making.md --own-pass`, raw output, whole (29 lines; `.t8_04_Phase_8_quotation_audit_raw.txt`)

```
pass audited : Casey
corpus mode  : default (own pass excluded)
corpus files : 7119   chars: 115,130,913
files audited: 04_Phase_08_Making.md
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
fragments tested (single-line, ellipsis-split, >=7 words): 30
NOT FOUND in corpus: 3
  of those, in TABLE CELLS : 0
  of those, in PROSE       : 3

  [04_Phase_08_Making.md:378]           (physiology l45); cold is a preparation problem, never a gate (physiology l47-51; frame l265); the register is
  [04_Phase_08_Making.md:392]           (physiology l53-57); realistic skin sits where interaction happens, the hands, face and ears (physiology l35-36)
  [04_Phase_08_Making.md:666]           and multi-phase warning forms over the pass files already read whole (a; an earlier pattern search failed at the tool's complexity

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```

**Triage of the misses** (orchestrator; table `.t8_04_Phase_8_quotation_triage.md`): 3 misses: 3 CONNECTIVE, 0 WRAP, 0 DOT, 0 SELF, **0 MISQUOTE**. The audit does not read dot-files, so quotations of the readers' outputs and replies are checked by no tool except the pre-check above.

## American English sweep — a pattern of British forms (`scratchpad/casey/tools/ame_pattern.txt`), over the phase file, raw output, whole (15 lines; `.t8_04_Phase_8_ame_sweep_raw.txt`)

```
== 04_Phase_08_Making.md
154:raised
210:raised
249:raises
314:raised
315:raised
316:raised
316:raised
317:Raising
317:raised
334:raised
335:raised
488:raised
665:raising
665:raised
```

**Hits:** all false positives of the `-ise` pattern (raised, raises, raising). 0 British forms; "judgement" does not occur.

## Handoff audit — `Tools/handoff_audit.py` (last change 2026-10-21), raw output, whole (115 lines; `.t8_04_Phase_8_handoff_audit_raw.txt`)

```
pass audited : Casey
phase files  : 7

=== CONTROLS (edit these per pass; they are what makes a zero trustworthy) ===
  PHASES WITH A FORMAL SWEEP BLOCK (found in this pass): 2, 3, 4, 5, 6, 7, 8
  PHASES WITH NO TRACE OF A SWEEP (found in this pass)  : none
  SELF-TEST (fixed positive and negative strings)       : passed
  INSTRUMENT VALID: YES - the detector separates a formal block from no block on the built-in controls

  phase | outbound | sweep    | rows | verdict
  ------+----------+----------+------+---------
      2 |        0 | FORMAL   |   16 | n/a - nothing addressed to it
      3 |        1 | FORMAL   |   32 | reconcile 32 enumerated against 1 outbound
      4 |        9 | FORMAL   |   44 | reconcile 44 enumerated against 9 outbound
      5 |       15 | FORMAL   |  131 | reconcile 131 enumerated against 15 outbound
      6 |        4 | FORMAL   |   28 | reconcile 28 enumerated against 4 outbound
      7 |       21 | FORMAL   |   88 | reconcile 88 enumerated against 21 outbound
      8 |        8 | FORMAL   |   23 | reconcile 23 enumerated against 8 outbound

TOTAL outbound handoff rows: 84
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
       [04_Phase_04_Ordinary_Life.md]  | **Phase 5** | The held robot's and the flow's nightly heat: who gives it and on what t
       [04_Phase_04_Ordinary_Life.md]  | **Phase 5** | The internal map: whether the city's parts are joined over ice in the sh
       [04_Phase_04_Ordinary_Life.md]  | **Phase 5** | The bright-weeks rhythm: the stop at the door, the firm night hours, owe
       [04_Phase_04_Ordinary_Life.md]  | **Phase 5** | Road news as part of the resident's ordinary day [PA-5] (P4-20); the ice
       [04_Phase_04_Ordinary_Life.md]  | **Phase 5** | Care staff arriving and leaving in windows; the outbound resident who ca
       [04_Phase_04_Ordinary_Life.md]  | **Phase 5** | REQ-32: split spec lines still not admitted by part (sweep row 13) | swe
  -> Phase 6:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 6** | Necessity Before Meaning: what moral, if any, was hung on the founding w
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 6** | A warning for Phases 6 to 9: the native layer must not be written as wea
       [04_Phase_04_Ordinary_Life.md]  | **Phase 6** | Candidate sites only, nothing created (RF-7): the blizzard day as unsche
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 6** | Necessity before meaning at the edge, candidate sites only, nothing crea
  -> Phase 7:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 7** | The founding administration (II.4) and local councils (I.4): who held it
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 7** | The records' keepers: who keeps and reads them, on what terms, and wheth
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 7** | Heat and arrival: whether any rule decides who is given heated rest to w
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 7** | Who decided what of the inherited base was kept (`04_Phase_02` L486; P3-
       [04_Phase_04_Ordinary_Life.md]  | **Phase 7** | Who keeps heat, water and clearing through the shared night and on storm
       [04_Phase_04_Ordinary_Life.md]  | **Phase 7** | Who provides heated places away from home, in storms and for travelers, 
       [04_Phase_04_Ordinary_Life.md]  | **Phase 7** | Whether the hold is household-, city- or parent-run; who cannot lay in; 
       [04_Phase_04_Ordinary_Life.md]  | **Phase 7** | How a care trainee's departure and return are arranged, and how care pos
       [04_Phase_04_Ordinary_Life.md]  | **Phase 7** | Who makes the morning weather call and what closes; how schooling meets 
       [04_Phase_04_Ordinary_Life.md]  | **Phase 7** | What the free tier's 491,945 workers do (Casey's sector shares, at Step 
       [04_Phase_04_Ordinary_Life.md]  | **Phase 7** | Whether anyone protects the robot majority's leisure in the bright weeks
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 7** | Who makes the go/no-go at the decision point, under the network's local 
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 7** | Who keeps the nodes and heated waiting rooms, and on what terms a rider,
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 7** | Who lays in and who counts (membership as provisioning, conditional on t
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 7** | Who keeps the spur city's unshipped bulk goods at Casey through the shut
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 7** | Whether road traffic in the shut half draws on the sea-laid store; who d
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 7** | The internal crossings of the bays by season: who opens one, if any; nev
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 7** | Ordering the dependencies Casey cannot make: care posts across the shut 
       [04_Phase_06_Meaning.md]  | **Phase 7** | Who keeps the warm night: who provides the warm room at the day's end to
       [04_Phase_06_Meaning.md]  | **Phase 7** | Who records, if anyone: the held, the nights a robot rested cold, the de
       [04_Phase_06_Meaning.md]  | **Phase 7** | The keepers of heat as the people the promise rests on, conditional on P
  -> Phase 8:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 8** | Languages outside the supporting tier (`01_Inherited` L295; S1-14): hous
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 8** | What Casey builds with: no admitted material (P3-8); the country rock as
       [04_Phase_04_Ordinary_Life.md]  | **Phase 8** | The street shaped by wind and drift: warm stops, door-to-door routes, in
       [04_Phase_04_Ordinary_Life.md]  | **Phase 8** | Dry interiors and any remedy | P4-44 · P4A-HF-5, P4B-HF-11 |
       [04_Phase_04_Ordinary_Life.md]  | **Phase 8** | What residents make and use for the day's frame: outdoor clothing for bo
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 8** | What the nodes, the heated waiting rooms and the junction's vehicle-serv
       [04_Phase_07_Order.md]  | **Phase 8** | What is built for the order: warm stopping places, heated nodes and publ
       [04_Phase_07_Order.md]  | **Phase 8** | What Casey makes: the free tier's goods and the non-thematic export, if 
  -> Phase 9:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 9** | Which populations exist (spine L468): exile-era robots, sent and a persi
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 9** | The robot body at Casey: hearing direction (P3-16, under DQ-14); the che
       [04_Phase_04_Ordinary_Life.md]  | **Phase 9** | Whether a recharging robot perceives, and whether storm vibration touche
       [04_Phase_04_Ordinary_Life.md]  | **Phase 9** | The robot body in the cold: permanent capacity loss as individual histor
       [04_Phase_04_Ordinary_Life.md]  | **Phase 9** | Built for a need, free to leave; build weighting and build needs once se
       [04_Phase_04_Ordinary_Life.md]  | **Phase 9** | Populations: the human half outside the modeled workforce; the child and
       [04_Phase_04_Ordinary_Life.md]  | **Phase 9** | In the bright weeks, households with no held schedule: their humans drif
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 9** | The robot traveler and the held robot: nightly heat away from home as a 
       [04_Phase_06_Meaning.md]  | **Phase 9** | Memory by cohort: exile-era and founding-era robots as the city's only l
       [04_Phase_06_Meaning.md]  | **Phase 9** | The damaged, not the dead: robots whose capacity was reduced by broken n
       [04_Phase_06_Meaning.md]  | **Phase 9** | The meaning distribution as populations by position relative to the heat
       [04_Phase_06_Meaning.md]  | **Phase 9** | Whether robots feel cold (DQ-14; PA-11), on which the mild-week leg turn
       [04_Phase_07_Order.md]  | **Phase 9** | Populations by position in the order: the keepers of heat and clearing (
       [04_Phase_07_Order.md]  | **Phase 9** | The candidate dispositions, never a faction (RF-7): night-makers, teache
       [04_Phase_07_Order.md]  | **Phase 9** | Robot turnover by will, not age: what a labor order means for a body tha
       [04_Phase_07_Order.md]  | **Phase 9** | Who attends a death in the shut half and who carries word of a lost pass
       [04_Phase_08_Making.md]  | **Phase 9** | The robot body in Casey's cold, as making meets it: whether robot skin a
       [04_Phase_08_Making.md]  | **Phase 9** | The robot speaker: exile-era robots as long-lived carriers of languages 
       [04_Phase_08_Making.md]  | **Phase 9** | The robot half as tended bodies through the shut half: robot-care worker
       [04_Phase_08_Making.md]  | **Phase 9** | The music listener: the direction of the robots' wider hearing (DQ-14; R
       [04_Phase_08_Making.md]  | **Phase 9** | The coat's two stakes as a population fact: robots whose outdoor work is
  -> Phase 10:
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 10** | Naming places from what they look like: scoured crests, lee drifts, whi
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 10** | Names for the junction's legs, the turn inland, the harbor, the waiting
       [04_Phase_06_Meaning.md]  | **Phase 10** | Names of places for the warm room, the waiting room and the node, only 
       [04_Phase_07_Order.md]  | **Phase 10** | Names of places and roles the order produces (the warm stopping place, 
       [04_Phase_08_Making.md]  | **Phase 10** | Names for made things and places (the door, the store, the stopping pla
```

## Phase discipline check — `Tools/phase_discipline_check.py` (last change 2026-10-21), raw output, whole (39 lines; `.t8_04_Phase_8_phase_discipline_raw.txt`)

```
pass audited : Casey

=== T3 - POSITION-COVERAGE LEDGER ===
  phases in header: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Child              filled=2  blank=7   blank at: P3, P5, P6, P7, P8, P9, P10
  The Lover (position)   filled=3  blank=6   blank at: P3, P5, P7, P8, P9, P10
  The Parent             filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Ruler              filled=1  blank=8   blank at: P2, P3, P4, P5, P6, P8, P9, P10
  The Elder              filled=4  blank=5   blank at: P3, P5, P8, P9, P10
  The Mentor             filled=2  blank=7   blank at: P3, P4, P5, P6, P8, P9, P10
  The Passer-Through     filled=6  blank=3   blank at: P8, P9, P10
  The Neighbor           filled=1  blank=8   blank at: P2, P3, P4, P6, P7, P8, P9, P10
  ⭐ The Lover FACULTY    filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10

  NOTE: a blank cell is a WARNING BEFORE Step 8, not a defect. Do not
  fill a blank by writing new phase content toward it - that is the
  contamination 00f Rule 3 forbids (see the recipe's hard bound on T3).

=== T4 - PER-PHASE SHED MARKER ===
  [04_Phase_02_Composition_and_Arrival.md]  T4 present: the 42 origin stocks as a sorting line: which nations are present, any row or share beyond
  [04_Phase_03_Surface_and_Texture.md]  T4 present: the 42 origin stocks and every composition share beyond the two bodies' halves, the founde
  [04_Phase_04_Ordinary_Life.md]  T4 present: the 42 origin stocks beyond the bare fact that none is the default; the founding, the arri
  [04_Phase_05_Relation_and_Geometry.md]  T4 present: the 42 origin stocks, every composition share beyond the two bodies and no majority, the f
  [04_Phase_06_Meaning.md]  T4 present: the 42 origin stocks beyond the fact that none is the default; the founder, the founding s
  [04_Phase_07_Order.md]  T4 present: the 42 origin stocks and every composition share beyond the two bodies and the fact that n
  [04_Phase_08_Making.md]  T4 present: the content of the 42 origin stocks and every composition share beyond the two bodies and 

  7/7 phase files carry a T4 marker.
  >> If EVERY phase's answer was literally 'nothing', T4 is falsified
     per its own stated condition (the question would be decorative).
     This tool cannot see the marker's CONTENT well enough to judge
     that - read the 7 lines above by hand.

=== T5 - EARLY LOVER-FACULTY SMOKE TEST ===
  EARLY (Phase 6) verdict: Alive, yes: Phases 2 to 6 show a city of two bodies whose one unwritten obligation is a warm night for whoever is inside, strangers held by the ice included, kept in every month and broken only where nobody can see; whether anyone could love it, rather than rely on it, is not yet answerable, because no admitted line writes what any resident cherishes or feels for Casey, and its culture material opens only at Step 5.
  LATE marker absent (08_Review_Panel.md missing or has no 'T5 - LATE LOVER FACULTY:' line yet)

  T5 not fully applied this pass (one or both markers absent).
```

*The T3 rows above were printed before the ledger's P8 column was marked; the ledger was updated right after (see Notes).*

## Notes

**Handoff audit, reconciled by hand.** Inbound: the tool sees 8 rows addressed `**Phase 8**` and counts 23 rows in the sweep block by its own pattern; the phase file's sweep enumerates 84 rows (those 8, REQ-33, the every-phase items, the contract's and Frame's rows, and the items the readers found; checked by reading the block, L48-139). Outbound: the file's HANDED FORWARD table holds 13 rows (5 to **Phase 9**, 1 to **Phase 10**, and 7 to Steps 5, 6, 7 and 10, which are outside the tool's form), plus 5 items carried outside the pass (the CST stage first).

**Position-coverage ledger (T3).** The P8 column of `00.2_Position_Coverage_Ledger.md` was copied by the orchestrator from the phase file's `## T3 · Position coverage` (L561-575): The Elder (narrowly, a cohort with no individual; the phase's split 15) and The Passer-Through covered; the other seven blank, each with its reason there.

**The stage order held** (RF-6, contract L415): cuisine, music, play and humor are written as structure and canon constraints only, with their content carried to the CST; language is written in full; dress from function.

**Developer question** DQ-26 filed as DEC-536 in `Research_Logs/DECISIONS_NEEDED_FROM_DEVELOPER.md` (the Casey section, above `## Answered`). No new provisional assumption.

**Web calls:** none at this phase. Session web total unchanged: see the progress file.

**Readers' staging folders:** each holds only its output and its Round 3 reply (checked with `ls`).

