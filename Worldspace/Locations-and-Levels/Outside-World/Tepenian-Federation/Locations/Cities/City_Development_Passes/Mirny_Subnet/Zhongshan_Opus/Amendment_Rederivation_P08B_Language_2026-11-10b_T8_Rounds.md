# Zhongshan: T8 round record for P08B_Language (language and speech), 2026-11-10

**What this is.** The record of the three-reader rounds behind `Amendment_Rederivation_P08B_Language_2026-11-10.md` (the piece; 783 lines, `sha256` `0c76f24205437ca0`). It states what each tool returned and where each file is; it does not restate the piece. **Everything here is PROPOSED;** no pass file was edited. The run's log is `Amendment_Log_2026-11-10.md`.

**Isolation.** Fresh readers and a fresh merge writer, each with a clean brief and its own private staging folder; nothing from any other location's run is in any list, brief or record of this piece (log Z-01).

**Items re-derived:** `C5` (language and speech); first-check verdicts in the note's section J. **Rests on:** `P02_Arrival` (merged before this piece's dispatch; `DR-107`).

## Round 0: the list and the briefs

The three readers' lists are identical (`cmp`). The list (10 entries), as dispatched:

```
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/Amendment_Notes_2026-11-10_Cross_Check.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/.xc_20261110_item_C5.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/Amendment_Rederivation_P02_Arrival_2026-11-10.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/04_Phase_08_Making.md :: 800-860
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/00_Frame.md :: 44-50,323-330,346-353
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/04_Phase_05_Relation_and_Geometry.md :: 150-158
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Cross_City_Culture_Differentiation_Table.md :: 120,125
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md :: 1563,1632,1664-1672
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Language_Blocs_By_City_2026-11-03.csv :: 775-806
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Language_Sets_By_City_Reference_2026-11-03.md :: 5,36,77
```

Brief template `scratchpad/zs/tools/zs_t8_brief.md` (generator `zs_pieces.py`); the three briefs differ only in the title's reader letter, the reader letter, the staging folder, the output path and the number range (A 1 to 99, B 101 to 199, C 201 to 299). Brief `sha256`: A `383a380e51924f60`, B `0d3eeafd75c1bb3b`, C `878021d9e375e670`. Before dispatch each brief's cited lines were checked against its list (`zs_check_brief.py`; log Z-13 or later).

## Round 1: three independent readers

- Reader A: `.t8_xc_P08B_Language_readerA.md` beside the pass (577 lines, `sha256` `929bb348d68d7d55`).
- Reader B: `.t8_xc_P08B_Language_readerB.md` beside the pass (481 lines, `sha256` `e98739d22ae3ed48`).
- Reader C: `.t8_xc_P08B_Language_readerC.md` beside the pass (610 lines, `sha256` `8e33ade8d5918007`).

## Round 2: the mechanical check

Tool: `Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/triple_read_verify.py` (last committed 2026-11-03; no uncommitted edits).

**round2_run1.txt** (raw output, whole; also beside the pass as `.t8_xc_P08B_Language_round2_run1.txt`):

```
required files: 10
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/Amendment_Notes_2026-11-10_Cross_Check.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/.xc_20261110_item_C5.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/Amendment_Rederivation_P02_Arrival_2026-11-10.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/04_Phase_08_Making.md  [range 800-860] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/00_Frame.md  [range 44-50,323-330,346-353] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/04_Phase_05_Relation_and_Geometry.md  [range 150-158] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Cross_City_Culture_Differentiation_Table.md  [range 120,125] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 1563,1632,1664-1672] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Language_Blocs_By_City_2026-11-03.csv  [range 775-806] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Language_Sets_By_City_Reference_2026-11-03.md  [range 5,36,77] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
exit 0
```

## Round 3: the cross-check (each reader continued by SendMessage, given the other two outputs)

The verdict lines, as `grep` returns them (each reply beside the pass as `.t8_xc_P08B_Language_round3_reader<X>.md`):

```
reader A L31: **Verdict on reader B: CONSISTENT**
reader A L117: **Verdict on reader C: CONSISTENT**
reader B L35: **Verdict on reader A: CONSISTENT**, because every PROOF field and every list-sourced citation I checked matches what I read, and its
reader B L102: **Verdict on reader C: CONSISTENT**, because every PROOF field and every list-sourced citation I checked matches what I read, and its
reader C L31: **Verdict on reader A: CONSISTENT**
reader C L78: **Verdict on reader B: CONSISTENT**
```

## The merge

One merge writer (fresh; not a reader), brief `scratchpad/zs/pieces/P08B_Language/M/brief.md` (template `zs_merge_brief.md`; `sha256` `065ae667df88e6f5`), merge rule `M-246` as `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` §N.2 states it. Its return, as given: `Amendment_Rederivation_P08B_Language_2026-11-10.md — 783 lines — I merged the three readers' PROPOSED re-derivations of C5 under M-246 into Findings 1-40, Choices 41-68 and Questions 69-79: the grade stays NARROWS, the language set is Hawaiian dominant with Mandarin as the sole supporting tier, and the shared-table cell's source clause now reads "which can only come to them" (reconciled with P02 Finding 47; covers newer exiles and records). Every quotation was checked at its source line, and the rulings-log lines that name other locations were left unquoted.`

## Merge checks (run on the piece before this record existed)

**1 · Normalized quotation pre-check** (`scratchpad/zs/tools/zs_postmerge.py`; corpus: the list's sources whole, the pass's numbered files and amendment notes, the reader outputs and Round 3 replies, the item outputs). Raw output, whole:

```
corpus files: 38; quoted strings (12+ chars, paired within a block): 184; not found: 1; blocks with an odd quote count (hand-check): 0
  NOT FOUND (block at L557): Up to three clocks, all mutually intelligible
```

**2 · Quotation audit** (`python3 Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/quotation_audit.py "<pass folder>" --files <piece> --own-pass`, from the repo root; tool last committed 2026-11-02; no uncommitted edits). Raw output, excerpted (18 miss lines omitted, kept whole beside the pass as `.t8_xc_P08B_Language_quotation_audit.txt`):

```
pass audited : Zhongshan_Opus
corpus mode  : default (own pass excluded)
corpus files : 6898   chars: 109,002,757
files audited: Amendment_Rederivation_P08B_Language_2026-11-10.md
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
fragments tested (single-line, ellipsis-split, >=7 words): 43
NOT FOUND in corpus: 18
  of those, in TABLE CELLS : 0
  of those, in PROSE       : 18


⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.

exit 0
```

**2b · Triage of the audit's misses** (same script; the audit reads no dot-file). Raw output, whole:

```
audit NOT FOUND fragments: 18; (a) found in the corpus: 4; (b) the piece's own unquoted prose: 7; (c) for hand triage: 7
  (c) L51: l327, row p-1, the same assumption, rated
  (c) L52: 04 phase 05 l155, what the federation supplies
  (c) L297: (l834), and l843 asks how much of the older branch's speech
  (c) L326: p02 l151) and which p02 choice 59 avoids (wording that
  (c) L329: ( p02 l728-729), and the pass's own l839 says
  (c) L557: up to three clocks, all mutually intelligible
  (c) L668: 04 phase 08 l814), or keep tracking the community she lives in (
```

Hand triage of class (c): 7 fragments in class (c), each read at its line: L51, L52, L297, L326, L329 and L668 are the piece's prose between two adjacent quotations; L557 (also the one pre-check string not found) is the piece's own label for a disputed reading in its section 5, not a quotation of a source. No misquotation found.

**3 · American English sweep** (British forms; only "judgement" is kept). Raw output: none (0 hits).

**4 · Other locations' names and status words** (`grep` for 56 names and aliases, whole words; and for complete, completed, ready). Raw output: names none; status words none.

*Record written 2026-11-10 08:37 by script from the files named above; the checks ran on the piece, not on this record.*
