# Zhongshan: T8 round record for P02_Arrival (arrival, the census inversion and robot origin), 2026-11-10

**What this is.** The record of the three-reader rounds behind `Amendment_Rederivation_P02_Arrival_2026-11-10.md` (the piece; 844 lines, `sha256` `455c82aeffbeb130`). It states what each tool returned and where each file is; it does not restate the piece. **Everything here is PROPOSED;** no pass file was edited. The run's log is `Amendment_Log_2026-11-10.md`.

**Isolation.** Fresh readers and a fresh merge writer, each with a clean brief and its own private staging folder; nothing from any other location's run is in any list, brief or record of this piece (log Z-01).

**Items re-derived:** `C10` (arrivals after the founding), `C6` (where the inversion between the censuses lies), `C9` (robot origin figures); first-check verdicts in the note's section J.

## Round 0: the list and the briefs

The three readers' lists are identical (`cmp`). The list (15 entries), as dispatched:

```
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/Amendment_Notes_2026-11-10_Cross_Check.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/.xc_20261110_item_C10.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/.xc_20261110_item_C6.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/.xc_20261110_item_C9.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/04_Phase_02_Composition_and_Arrival.md :: 40-68,205-226,310-316
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/04_Phase_08_Making.md :: 55-59,126-136,340-346,472-478,826-834,886-891
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/04_Phase_09_Populations.md :: 60-64,125-142,392-400,438-445
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/04_Phase_05_Relation_and_Geometry.md :: 132-143
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/05_Reconciliation.md :: 112-122,165-171
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Cross_City_Culture_Differentiation_Table.md :: 120,125
/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Falkland_Treaty/Falkland_Treaty_Draft_v1.md :: 41-51,74-79,92,138
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/01_Inherited.md :: 85-118
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md :: 502,554,643,694
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md :: 448-475,1711-1712
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Zhongshan.md :: 34-70
```

Brief template `scratchpad/zs/tools/zs_t8_brief.md` (generator `zs_pieces.py`); the three briefs differ only in the title's reader letter, the reader letter, the staging folder, the output path and the number range (A 1 to 99, B 101 to 199, C 201 to 299). Brief `sha256`: A `2802d2f6b335af70`, B `30a8c4906344857d`, C `b7d89e088f7a3946`. Before dispatch each brief's cited lines were checked against its list (`zs_check_brief.py`; log Z-13 or later).

## Round 1: three independent readers

- Reader A: `.t8_xc_P02_Arrival_readerA.md` beside the pass (843 lines, `sha256` `81b921d09660bc17`).
- Reader B: `.t8_xc_P02_Arrival_readerB.md` beside the pass (653 lines, `sha256` `8e8d5d4133dcba12`).
- Reader C: `.t8_xc_P02_Arrival_readerC.md` beside the pass (640 lines, `sha256` `6d6d814a8effb421`).

## Round 2: the mechanical check

Tool: `Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/triple_read_verify.py` (last committed 2026-11-03; no uncommitted edits).

**round2_run1.txt** (raw output, whole; also beside the pass as `.t8_xc_P02_Arrival_round2_run1.txt`):

```
required files: 15
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/Amendment_Notes_2026-11-10_Cross_Check.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/.xc_20261110_item_C10.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/.xc_20261110_item_C6.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/.xc_20261110_item_C9.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/04_Phase_02_Composition_and_Arrival.md  [range 40-68,205-226,310-316] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/04_Phase_08_Making.md  [range 55-59,126-136,340-346,472-478,826-834,886-891] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/04_Phase_09_Populations.md  [range 60-64,125-142,392-400,438-445] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/04_Phase_05_Relation_and_Geometry.md  [range 132-143] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/05_Reconciliation.md  [range 112-122,165-171] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Cross_City_Culture_Differentiation_Table.md  [range 120,125] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Falkland_Treaty/Falkland_Treaty_Draft_v1.md  [range 41-51,74-79,92,138] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/01_Inherited.md  [range 85-118] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md  [range 502,554,643,694] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 448-475,1711-1712] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Zhongshan.md  [range 34-70] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
exit 0
```

## Round 3: the cross-check (each reader continued by SendMessage, given the other two outputs)

The verdict lines, as `grep` returns them (each reply beside the pass as `.t8_xc_P02_Arrival_round3_reader<X>.md`):

```
reader A L37: **Verdict on reader B: CONSISTENT** — every span, positional line, figure and quotation I checked matches my own reading of the same
reader A L125: **Verdict on reader C: CONSISTENT** — every span, positional line, figure and quotation I checked matches my own reading, and the
reader B L39: **Verdict on reader A: CONSISTENT**
reader B L122: **Verdict on reader C: CONSISTENT**
reader C L37: **Verdict on reader A: CONSISTENT** — every quotation and figure I checked matches the sources I read, and none of A's differences from me is a misreading.
reader C L110: **Verdict on reader B: CONSISTENT** — every quotation and figure I checked matches the sources I read, and B's departures from me are reasoned choices, not misr
```

## The merge

One merge writer (fresh; not a reader), brief `scratchpad/zs/pieces/P02_Arrival/M/brief.md` (template `zs_merge_brief.md`; `sha256` `7927679ae11dfe6e`), merge rule `M-246` as `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` §N.2 states it. Its return, as given: `Amendment_Rederivation_P02_Arrival_2026-11-10.md — 844 lines. All three readers agree with the first check's verdicts (C10 FLIPS, C6 NARROWS, C9 NARROWS), and their outputs are merged under M-246 into one PROPOSED piece: Findings 1-52, Choices 53-73 and Questions 74-82, with 17 reader contradictions settled on content in section 5 and all 162 quotations checked against their source lines.`

## Merge checks (run on the piece before this record existed)

**1 · Normalized quotation pre-check** (`scratchpad/zs/tools/zs_postmerge.py`; corpus: the list's sources whole, the pass's numbered files and amendment notes, the reader outputs and Round 3 replies, the item outputs). Raw output, whole:

```
corpus files: 40; quoted strings (12+ chars, paired within a block): 248; not found: 5; blocks with an odd quote count (hand-check): 0
  NOT FOUND (block at L345): the census records no return through it
  NOT FOUND (block at L511): the census records no return through it
  NOT FOUND (block at L517): the door that closes behind each arrival, open inward at a size not set
  NOT FOUND (block at L541): And the door closed behind each of them | IV.2.3: no one who came could go back; arrival stayed open (II.2.5, II.2.1), its size not set
  NOT FOUND (block at L556): neither can go back to the source, which reaches them only in newer exiles
```

**2 · Quotation audit** (`python3 Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/quotation_audit.py "<pass folder>" --files <piece> --own-pass`, from the repo root; tool last committed 2026-11-02; no uncommitted edits). Raw output, excerpted (28 miss lines omitted, kept whole beside the pass as `.t8_xc_P02_Arrival_quotation_audit.txt`):

```
pass audited : Zhongshan_Opus
corpus mode  : default (own pass excluded)
corpus files : 6898   chars: 109,002,757
files audited: Amendment_Rederivation_P02_Arrival_2026-11-10.md
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
fragments tested (single-line, ellipsis-split, >=7 words): 72
NOT FOUND in corpus: 28
  of those, in TABLE CELLS : 0
  of those, in PROSE       : 28


⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.

exit 0
```

**2b · Triage of the audit's misses** (same script; the audit reads no dot-file). Raw output, whole:

```
audit NOT FOUND fragments: 28; (a) found in the corpus: 8; (b) the piece's own unquoted prose: 9; (c) for hand triage: 11
  (c) L12: the rulings are used as they stand ( dr-105 item 4
  (c) L72: in assembly power territory at the treaty's date and robots who
  (c) L240: ( 04 phase 02 l62; 04 phase 09 l137-138). the census marks the -10% as
  (c) L241: (note l64, giving census l502 and l643). the point the pass draws
  (c) L350: ). and what does that cause the relational finding
  (c) L477: (finding 4); two clocks, still audible and
  (c) L478: ( shared table l125; finding 47); the resident branch's drift before 2564, the older branch's food being
  (c) L520: (l343), rest on the resident branch's drift before 2564 and hold
  (c) L531: (note l125-126; spec l180 itself is on no reader's list). it grounds modest commerce; whether it carries
  (c) L558: neither can go back to the source, which reaches them only in newer exiles
  (c) L602: on the corrected spec line (b 106, choice 135). c
```

Hand triage of class (c): 11 fragments in class (c), each read at its line (L12, L72, L240, L241, L350, L477, L478, L520, L531, L558, L602): ten are the piece's own prose between two adjacent quotations (each fragment begins or ends at a quotation mark), and L558 is the piece's proposed restatement written in plain quotation marks. Pre-check: the 5 strings not found (blocks at L345, L511, L517, L541, L556) are the piece's proposed wording in plain quotation marks; the piece puts source quotations in italic quotation marks. No misquotation found.

**3 · American English sweep** (British forms; only "judgement" is kept). Raw output: none (0 hits).

**4 · Other locations' names and status words** (`grep` for 56 names and aliases, whole words; and for complete, completed, ready). Raw output: names none; status words none.

*Record written 2026-11-10 07:56 by script from the files named above; the checks ran on the piece, not on this record.*
