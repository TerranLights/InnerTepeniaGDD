# Zhongshan: T8 round record for P03_Research (the inspiration picks and later research), 2026-11-10

**What this is.** The record of the three-reader rounds behind `Amendment_Rederivation_P03_Research_2026-11-10.md` (the piece; 506 lines, `sha256` `503cd4a261df2fe1`). It states what each tool returned and where each file is; it does not restate the piece. **Everything here is PROPOSED;** no pass file was edited. The run's log is `Amendment_Log_2026-11-10.md`.

**Isolation.** Fresh readers and a fresh merge writer, each with a clean brief and its own private staging folder; nothing from any other location's run is in any list, brief or record of this piece (log Z-01).

**Items re-derived:** `U5` (the inspiration picks and later research on them); first-check verdicts in the note's section J.

## Round 0: the list and the briefs

The three readers' lists are identical (`cmp`). The list (6 entries), as dispatched:

```
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/Amendment_Notes_2026-11-10_Cross_Check.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/.xc_20261110_item_U5.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/03_Research.md :: 30-62
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Inspirational-Influences.md :: 103-106
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Zhongshan_Inspiration_Place_Research_R1.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Zhongshan_Inspiration_Place_Research_R2.md
```

Brief template `scratchpad/zs/tools/zs_t8_brief.md` (generator `zs_pieces.py`); the three briefs differ only in the title's reader letter, the reader letter, the staging folder, the output path and the number range (A 1 to 99, B 101 to 199, C 201 to 299). Brief `sha256`: A `26700e6e3c0d9cee`, B `f48cc550100f807b`, C `75fcf459724a23a3`. Before dispatch each brief's cited lines were checked against its list (`zs_check_brief.py`; log Z-13 or later).

## Round 1: three independent readers

- Reader A: `.t8_xc_P03_Research_readerA.md` beside the pass (371 lines, `sha256` `a566e51ef3e5bb54`).
- Reader B: `.t8_xc_P03_Research_readerB.md` beside the pass (342 lines, `sha256` `44a790bcb09ac086`).
- Reader C: `.t8_xc_P03_Research_readerC.md` beside the pass (321 lines, `sha256` `acce5958b024191e`).

## Round 2: the mechanical check

Tool: `Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/triple_read_verify.py` (last committed 2026-11-03; no uncommitted edits).

**round2_run1.txt** (raw output, whole; also beside the pass as `.t8_xc_P03_Research_round2_run1.txt`):

```
required files: 6
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/Amendment_Notes_2026-11-10_Cross_Check.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/.xc_20261110_item_U5.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/03_Research.md  [range 30-62] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Inspirational-Influences.md  [range 103-106] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Zhongshan_Inspiration_Place_Research_R1.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Zhongshan_Inspiration_Place_Research_R2.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
exit 0
```

## Round 3: the cross-check (each reader continued by SendMessage, given the other two outputs)

The verdict lines, as `grep` returns them (each reply beside the pass as `.t8_xc_P03_Research_round3_reader<X>.md`):

```
reader A L49: **Verdict on reader B: CONSISTENT**
reader A L104: **Verdict on reader C: CONSISTENT**
reader B L36: **Verdict on reader A: CONSISTENT** Every source claim I checked matches the same lines I read, including its PROOF fields,
reader B L105: **Verdict on reader C: CONSISTENT** Every source claim I checked matches the same lines I read, except one grep hit that I
reader C L48: **Verdict on reader A: CONSISTENT**, because every source claim of A's that I checked lands on the cited line with the stated
reader C L129: **Verdict on reader B: CONSISTENT**, because every passage-specific claim of B's that I checked is on the cited line with the
```

## The merge

One merge writer (fresh; not a reader), brief `scratchpad/zs/pieces/P03_Research/M/brief.md` (template `zs_merge_brief.md`; `sha256` `3f141613987a323b`), merge rule `M-246` as `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` §N.2 states it. Its return, as given: `Amendment_Rederivation_P03_Research_2026-11-10.md, 506 lines. It merges readers A, B and C on U5 under M-246: the verdict is NARROWS, as the first check found, with 25 findings, 13 choices and 9 questions numbered in one series, all PROPOSED; on each contradiction it writes the view that claims least, for example "not recorded as finished" rather than "not exhausted", and the picks left unnamed.`

## Merge checks (run on the piece before this record existed)

**1 · Normalized quotation pre-check** (`scratchpad/zs/tools/zs_postmerge.py`; corpus: the list's sources whole, the pass's numbered files and amendment notes, the reader outputs and Round 3 replies, the item outputs). Raw output, whole:

```
corpus files: 36; quoted strings (12+ chars, paired within a block): 72; not found: 1; blocks with an odd quote count (hand-check): 0
  NOT FOUND (block at L455): Merge writer
```

**2 · Quotation audit** (`python3 Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/quotation_audit.py "<pass folder>" --files <piece> --own-pass`, from the repo root; tool last committed 2026-11-02; no uncommitted edits). Raw output, excerpted (11 miss lines omitted, kept whole beside the pass as `.t8_xc_P03_Research_quotation_audit.txt`):

```
pass audited : Zhongshan_Opus
corpus mode  : default (own pass excluded)
corpus files : 6898   chars: 109,002,757
files audited: Amendment_Rederivation_P03_Research_2026-11-10.md
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
fragments tested (single-line, ellipsis-split, >=7 words): 19
NOT FOUND in corpus: 11
  of those, in TABLE CELLS : 2
  of those, in PROSE       : 9


⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.

exit 0
```

**2b · Triage of the audit's misses** (same script; the audit reads no dot-file). Raw output, whole:

```
audit NOT FOUND fragments: 11; (a) found in the corpus: 5; (b) the piece's own unquoted prose: 6; (c) for hand triage: 0
```

Hand triage of class (c): class (c) is empty (0 of 11). Pre-check: one string not found, "Merge writer" (the block at L455), a label the piece defines for its own credit column, not a quotation of any source. Status words: L10 twice, in the sentence stating that nothing in the piece calls the pass, the review or the city complete or ready (a negative statement). Pre-check positive control: a copy of the piece with a fabricated quotation appended returned it as NOT FOUND (log Z-16).

**3 · American English sweep** (British forms; only "judgement" is kept). Raw output: none (0 hits).

**4 · Other locations' names and status words** (`grep` for 56 names and aliases, whole words; and for complete, completed, ready). Raw output: names none; 

status words:
```
L10: complete: review or the city complete or ready.
L10: ready: review or the city complete or ready.
```

*Record written 2026-11-10 07:45 by script from the files named above; the checks ran on the piece, not on this record.*
