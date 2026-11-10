# Shirayuki: T8 round record for P02A_Composition (the tier shape, the refused party's share, and robot national origin), 2026-11-10

**What this is.** The record of the three-reader rounds behind `Amendment_Rederivation_P02A_Composition_2026-11-10.md` (the piece; 497 lines, `sha256` `0608a55fede7e336`). It states what each tool returned and where each file is; it does not restate the piece. **Everything here is PROPOSED;** no pass file was edited. The run's log is `Amendment_Log_2026-11-10.md`.

**Items re-derived:** `SRY-C01`, `SRY-C09`, `SRY-C04` (the note's section J gives each first-check verdict). **Pass places:** `04_Phase_02_Composition_and_Arrival.md` L38–L96 (A, A.1, A.2, A.3), L350–L360; `02_Spine.md` L121–L138 (§2e, `G8`); `00_Frame.md` L300–L333 (§7, §8 item 7); `01_Inherited.md` L192–L223 (A1, with L217–L219); `04_Phase_09_Populations.md` L58–L88 (§B), L330–L345 (§I).

## Round 0: the list and the briefs

The three readers' lists are identical (`cmp`). The list (13 entries), as dispatched:

```
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/Amendment_Notes_2026-11-10_Cross_Check.md :: 1-22,29-34,296-302,152-166,268-279,303,306,311
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_02_Composition_and_Arrival.md :: 38-96,350-360
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/02_Spine.md :: 121-138
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/00_Frame.md :: 300-333
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/01_Inherited.md :: 192-223
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_09_Populations.md :: 58-88,330-345
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Shirayuki.md :: 44-48,54,60-99
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md :: 448-475,1711-1712
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/STARTUP_Finished_City_Cross_Check_Shirayuki_then_Zhongshan_2026-11-10.md :: 62-67
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md :: 2090-2125,2232-2238,2242-2316
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C01.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C09.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C04.md
```

Brief template `scratchpad/sry/tools/t8_template.md`; the three briefs differ only in reader letter, private staging folder and number range (A 1–99, B 101–199, C 201–299). Brief `sha256` A `f6ea310ebc7dde1a`, B `71bfeddbf3f76508`, C `b0b25104d32cd7d8`. Before dispatch every brief's cited lines were checked against its list (`check_brief_vs_list` adapted for pieces; positive control returned two flagged ranges), and one generated brief was read end to end (log L-36). The piece's note range was out of ascending order in six of the seven pieces (log L-42).

## Round 1: three independent readers

- Reader A: `.t8_xc_P02A_Composition_readerA.md` beside the pass (289 lines now, `sha256` `3d95a8ce97fe9eee`).
- Reader B: `.t8_xc_P02A_Composition_readerB.md` beside the pass (331 lines now, `sha256` `27fb6aeda72b8e61`).
- Reader C: `.t8_xc_P02A_Composition_readerC.md` beside the pass (571 lines now, `sha256` `09e62fde45a749b7`).

## Round 2: the mechanical check

Tool: `Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/triple_read_verify.py` (last committed 2026-11-03; no uncommitted edits).

**round2_run1.txt** (raw output, whole; also beside the pass as `.t8_xc_P02A_Composition_round2_run1.txt`):

```
required files: 13
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/Amendment_Notes_2026-11-10_Cross_Check.md  [range 1-22,29-34,296-302,152-166,268-279,303,306,311] ===
  agent1   ⛔ LMID  MISMATCH  claimed=''  actual='| Rows in the table | 38 (1 Primary, 2 Significant, 35 Notab'
  agent2   ⛔ LMID  MISMATCH  claimed=''  actual='| Rows in the table | 38 (1 Primary, 2 Significant, 35 Notab'
  agent3   ⛔ LMID  MISMATCH  claimed=''  actual='| Rows in the table | 38 (1 Primary, 2 Significant, 35 Notab'

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_02_Composition_and_Arrival.md  [range 38-96,350-360] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/02_Spine.md  [range 121-138] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/00_Frame.md  [range 300-333] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/01_Inherited.md  [range 192-223] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_09_Populations.md  [range 58-88,330-345] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Shirayuki.md  [range 44-48,54,60-99] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 448-475,1711-1712] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/STARTUP_Finished_City_Cross_Check_Shirayuki_then_Zhongshan_2026-11-10.md  [range 62-67] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2090-2125,2232-2238,2242-2316] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C01.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C09.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
⛔ NOT UNANIMOUS - DO NOT WRITE. Log which agent/file failed and why.
```

**round2_run2.txt** (raw output, whole; also beside the pass as `.t8_xc_P02A_Composition_round2_run2.txt`):

```
required files: 13
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/Amendment_Notes_2026-11-10_Cross_Check.md  [range 1-22,29-34,296-302,152-166,268-279,303,306,311] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_02_Composition_and_Arrival.md  [range 38-96,350-360] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/02_Spine.md  [range 121-138] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/00_Frame.md  [range 300-333] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/01_Inherited.md  [range 192-223] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_09_Populations.md  [range 58-88,330-345] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Shirayuki.md  [range 44-48,54,60-99] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 448-475,1711-1712] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/STARTUP_Finished_City_Cross_Check_Shirayuki_then_Zhongshan_2026-11-10.md  [range 62-67] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2090-2125,2232-2238,2242-2316] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C01.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C09.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

Between the runs, each failing reader repaired its own failed field(s) by hand under `DR-117` item 2; each reader's reading log carries a "Round 2 repair:" line with the old and new value; a `diff` against a pre-repair copy showed only those fields and the repair lines changed (log L-42 onward). Cause: the orchestrator's out-of-order range string.

## Round 3: the cross-check (each reader continued by SendMessage with the other two outputs)

The verdict lines, as `grep` returns them from each reply (each reply also beside the pass as `.t8_xc_P02A_Composition_round3_reader<X>.md`):

```
reader A L26: - **P02A_Composition-A-R3-9. CONSISTENT.** B's spans, positional lines, figures and quotations match my own reading, and the one factual slip (two row
reader A L60: - **P02A_Composition-A-R3-26. CONSISTENT.** Every source claim of C's that falls inside my spans matches my reading, and its unverifiable claims are o
reader B L28: - P02A_Composition-B-R3-4. **Verdict on reader A: CONSISTENT.** Every admitted-line claim I checked matches the source, and A's figures and positional
reader B L64: - P02A_Composition-B-R3-10. **Verdict on reader C: CONSISTENT.** Every admitted-line claim I checked matches the source. C's figures match mine, and i
reader C L17: - P02A_Composition-C-R3-5. **(4) Verdict on reader A: CONSISTENT.** Every load-bearing quotation and figure I checked is in, or computes from, the lin
reader C L39: - P02A_Composition-C-R3-11. **(4) Verdict on reader B: CONSISTENT.** Every passage-dependent quotation I checked is in my materials. The two faults fo
```

## The merge

One merge writer (fresh; not a reader) on `scratchpad/sry/pieces/P02A_Composition/M/brief.md` (template `merge_template.md`; `sha256` `b541ddb72d322ecc`), merge rule `M-246` as `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` §N.2 and the runbook state it. Its return, as given: `Section 3: 97 rows — written (union) 76 · written (conservative) 12 · demoted 4 · question 3 · not written 2`

## Merge checks (run before this record existed)

**1 · Normalized quotation pre-check** (`scratchpad/sry/tools/quote_precheck.py`; corpus: the list's sources whole, the pass's numbered files and amendment notes, the readers' outputs, Round 3 replies and item verdicts). Raw output, whole:

```
quoted strings checked: 222; found: 218; not found: 4
  NOT FOUND: Amendment_Rederivation_P02A_Composition_2026-11-10b_T8_Rounds.md
  NOT FOUND:  (Frame L331) and 
  NOT FOUND:  rowless pools (now three), the unconditional floor, 
  NOT FOUND:  as a ground for tier standing, and its recommendation that robots arrived with the founders; and narrowed the Act 1 second pole and civic axis (subject to Frame L322), 
```

**2 · Quotation audit** (`python3 Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/quotation_audit.py "<pass folder>" --files <piece> --own-pass`, from the repo root; tool last committed 2026-11-02). Raw output, excerpted (32 miss lines omitted, kept whole in `.t8_xc_P02A_Composition_quotation_audit.txt` beside the pass):

```
pass audited : Shirayuki
corpus mode  : default (own pass excluded)
corpus files : 6812   chars: 105,888,057
files audited: Amendment_Rederivation_P02A_Composition_2026-11-10.md
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
fragments tested (single-line, ellipsis-split, >=7 words): 105
NOT FOUND in corpus: 32
  of those, in TABLE CELLS : 1
  of those, in PROSE       : 31


⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```

**2b · Triage of the audit's misses** (`scratchpad/sry/tools/audit_triage.py`; the audit reads no dot-file and its fragmenter captures text between two quotations). Raw output, whole:

```
audit NOT FOUND fragments: 32; (a) found in other inputs: 17; (b) piece's own unquoted prose: 13; (c) for hand triage: 2
  (c) L2: amendment rederivation p02a composition 2026-11-10b t8 rounds.md
  (c) L295: [CELL]  a (a-38), c (c-236), b (b-148) b narrowed (b-r3-11 item 3); a-r3-11 written (conservative): split b (round 1, kept
```

Hand triage of class (c): the two (c) fragments were read in full by the orchestrator: L2 is the name of this round record, which the merge brief told the writer to name; L295 is a table cell of the piece's own prose (finder and disposition notes) between quotations. The pre-check's 4 misses are the same two kinds. Confirmed defects: 0 (CELL 0, PROSE 0). The names check's two hits (L16, L478) are the subnet folder in the spec's path, `Specs/Mirny subnet/Shirayuki.md`, not a location named in prose.

**3 · American English sweep** (pattern of British forms; only "judgement" is kept). Raw output: none (0 hits).

**4 · Other locations' names and status words** (`grep` for 46 location names and aliases; and for complete/completed/ready). Raw output: status words none.

names:
```
1 478:Mirny
      1 16:Mirny
```

*Record written 2026-11-10 06:34 by script from the files named above; the record grows after no check (the checks ran on the piece, not on this record).*
