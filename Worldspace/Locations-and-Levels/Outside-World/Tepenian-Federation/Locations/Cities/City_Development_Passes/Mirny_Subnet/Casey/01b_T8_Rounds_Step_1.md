# Round record — Casey · Step 1 · Audit what is inherited

**Output:** `01_Inherited.md` (434 lines). Casey's warm ULM run under `STARTUP_Mirny_Review_then_Casey_ULM_2026-11-11.md` Part B item 3: three readers, Round 2, Round 3, one fresh merge writer (`M-246`), the quotation audit run before this record, the American English sweep. Everything in the output is PROPOSED. Record written 2026-11-11 09:43 by `scratchpad/casey/tools/casey_round_record.py`.

## Round 0 — the reading list and the frozen briefs

Briefs `.t8_01_Step_1_brief_A.md`, `_B.md`, `_C.md` (written new for Casey; standing lines 1–6, 10, 11 verbatim). The list, `.t8_required_01_Step_1.txt`:

```
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md :: 2523-2539
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/04_QA_Gates_and_Differentiation.md :: 219-242
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Stepwise_Execution/02_Gates/G10_Gate_9_Asymmetry.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/00_Frame.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/00.1_Step_MINUS-1_Input_Contract.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/00.1_Step_MINUS-1_Amendment_2026-11-11.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Casey.md :: 1-3,5-83,85,87-93,95-107,110,112-121,125-152,154-155,157-159,166-170,172,174-180,182,184,186,188-200,202,204-207,212-214,243-244,248-249
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/Datasheets/Step_1_and_2.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md :: 1707-1715
```

## Round 1 — three readers, each in a private staging folder

| Reader | Agent ID | Output (copied here) | Lines |
|---|---|---|---|
| A | `a78f16585e846e342` | `.t8_01_Step_1_readerA.md` | 352 |
| B | `ae71b387fb8db8a50` | `.t8_01_Step_1_readerB.md` | 385 |
| C | `a444c2aef2979b95f` | `.t8_01_Step_1_readerC.md` | 471 |

## Round 2 — `Tools/triple_read_verify.py` (last change 2026-11-03), raw output, whole (50 lines)

```
required files: 9
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2523-2539] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/04_QA_Gates_and_Differentiation.md  [range 219-242] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Stepwise_Execution/02_Gates/G10_Gate_9_Asymmetry.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/00_Frame.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Casey.md  [range 1-3,5-83,85,87-93,95-107,110,112-121,125-152,154-155,157-159,166-170,172,174-180,182,184,186,188-200,202,204-207,212-214,243-244,248-249] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/Datasheets/Step_1_and_2.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 1707-1715] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

## Round 3 — each reader continued by `SendMessage` with the other two outputs

| Reader | Reply (copied here) | Lines |
|---|---|---|
| A | `.t8_01_Step_1_round3_readerA.md` | 148 |
| B | `.t8_01_Step_1_round3_readerB.md` | 123 |
| C | `.t8_01_Step_1_round3_readerC.md` | 131 |

**Verdicts, as each reply's own verdict lines state them: all six CONSISTENT.** Each reply's sections 5 and 6 (disposition differences; recomputed figures) went to the merge writer whole.

## The merge — one fresh writer (`M-246`)

Agent `a2adaa57e13a8685b`; brief `.t8_01_Step_1_merge_brief.md`; output `01_Inherited.md`.

## Quotation audit — raw output, whole (39 lines; `.t8_01_Step_1_quotation_audit_raw.txt`)

```
tool: Tools/quotation_audit.py, last change 2026-11-02
command: python3 Tools/quotation_audit.py <Casey folder> --files 01_Inherited.md --own-pass
pass audited : Casey
corpus mode  : default (own pass excluded)
corpus files : 7118   chars: 114,831,204
files audited: 01_Inherited.md
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
fragments tested (single-line, ellipsis-split, >=7 words): 60
NOT FOUND in corpus: 11
  of those, in TABLE CELLS : 0
  of those, in PROSE       : 11

  [01_Inherited.md:32]           (frame l374, quoting register l8). an arrival class is named by not being founders
  [01_Inherited.md:32]           (contract l65; spec l173 part 3, admitted, contract l215, through the contract). the census tag on the founder's row
  [01_Inherited.md:66]           (contract l237; through the contract). spec l8
  [01_Inherited.md:84]           moving between the subnet's coastal cities and the interior
  [01_Inherited.md:118]           (frame l98, citing 01 l297-310 and readme-2 l52). declining's questions
  [01_Inherited.md:118]           are not run (frame l100). the change, stated flatly: humans -307,265 (-40.38%), robots -162,675 (-20.67%); 59.62% of census i huma
  [01_Inherited.md:118]           (frame l422, citing readme-2 l57), and a city built to its larger figure has
  [01_Inherited.md:178]           (frame l505), and the grid-failure file has
  [01_Inherited.md:178]           (datasheet l33) (c; b). (d) a robot who must rest in the open on a road leg, given that
  [01_Inherited.md:233]           (spec l202) classifies a site and decides about no one
  [01_Inherited.md:233]           (spec l249) asks about physical reachability, as req-5 reads it

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```

**Triage of the misses** (agent `ac3d89ae72f9e40b6`; table `.t8_01_Step_1_quotation_triage.md`): FOUND 0 · DOT 0 · SELF 0 · CONNECTIVE 11 · MISQUOTE 0. No misquotation.

## American English sweep — raw output, whole

```
American English sweep (Casey run; British-variant list, whole words, case-insensitive; judgement allowed)
hits: 0
```

## Notes

Reader C flagged two datasheet rows (`Datasheets/Step_1_and_2.md` L30, L34) that carry material the contract excludes; both were kept out of the merge and out of Step 2's list (`09.5_Log.md` CL-12). Readers B and C reordered their PROOF blocks to keep EXEMPT lines under their own blocks; Round 2 matched by path and passed. The handoff audit scans only Step 4's phase files, so this file's HANDED FORWARD rows (28) are swept by hand at each phase (CL-13).

**Not run on this unit, and why:** the handoff audit and the phase-discipline check work on Step 4's phase files; they run from Phase 2 on. This record does not grow after its line counts were taken (standing line 8).
