# Zhongshan: T8 round record for P07C_Imports (imports after the four-node and coastal-line answers), 2026-11-10

**What this is.** The record of the three-reader rounds behind `Amendment_Rederivation_P07C_Imports_2026-11-10.md` (the piece; 810 lines, `sha256` `8c887322f9d0e906`). It states what each tool returned and where each file is; it does not restate the piece. **Everything here is PROPOSED;** no pass file was edited. The run's log is `Amendment_Log_2026-11-10.md`.

**Isolation.** Fresh readers and a fresh merge writer, each with a clean brief and its own private staging folder; nothing from any other location's run is in any list, brief or record of this piece (log Z-01).

**Items re-derived:** `U3` (imports and the ports); first-check verdicts in the note's section J. **Rests on:** `P07B_Imports` (merged before this piece's dispatch; `DR-107`).

## Round 0: the list and the briefs

The three readers' lists are identical (`cmp`). The list (8 entries), as dispatched:

```
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/Amendment_Notes_2026-11-10_Cross_Check.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/.xc_20261110_item_U3.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/Amendment_Rederivation_P07B_Imports_2026-11-10.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/04_Phase_05_Relation_and_Geometry.md :: 318-336
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/04_Phase_07_Order.md :: 416-428
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Infrastructure/Ports.md :: 125-131,186-190,198-204,224-231,382-386
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Relationship_Database.md :: 488-495
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md :: 1962-1968
```

Brief template `scratchpad/zs/tools/zs_t8_brief.md` (generator `zs_pieces.py`); the three briefs differ only in the title's reader letter, the reader letter, the staging folder, the output path and the number range (A 1 to 99, B 101 to 199, C 201 to 299). Brief `sha256`: A `276a860e25a6e090`, B `c796ab43a874b854`, C `3d284d5c41753d9c`. Before dispatch each brief's cited lines were checked against its list (`zs_check_brief.py`; log Z-13 or later).

## Round 1: three independent readers

- Reader A: `.t8_xc_P07C_Imports_readerA.md` beside the pass (609 lines, `sha256` `a29cfdce862e56bf`).
- Reader B: `.t8_xc_P07C_Imports_readerB.md` beside the pass (597 lines, `sha256` `a6a0975569b78e8a`).
- Reader C: `.t8_xc_P07C_Imports_readerC.md` beside the pass (646 lines, `sha256` `c02662dc659417b8`).

## Round 2: the mechanical check

Tool: `Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/triple_read_verify.py` (last committed 2026-11-03; no uncommitted edits).

**round2_run1.txt** (raw output, whole; also beside the pass as `.t8_xc_P07C_Imports_round2_run1.txt`):

```
required files: 8
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/Amendment_Notes_2026-11-10_Cross_Check.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/.xc_20261110_item_U3.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/Amendment_Rederivation_P07B_Imports_2026-11-10.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/04_Phase_05_Relation_and_Geometry.md  [range 318-336] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/04_Phase_07_Order.md  [range 416-428] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Infrastructure/Ports.md  [range 125-131,186-190,198-204,224-231,382-386] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Relationship_Database.md  [range 488-495] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 1962-1968] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
exit 0
```

## Round 3: the cross-check (each reader continued by SendMessage, given the other two outputs)

The verdict lines, as `grep` returns them (each reply beside the pass as `.t8_xc_P07C_Imports_round3_reader<X>.md`):

```
reader A L31: **Verdict on reader B: CONSISTENT** because B read the same lines, reached the same verdict by leg (the gateway leg flips, the coastal line narrows to road with
reader A L99: **Verdict on reader C: CONSISTENT** because C read the same lines, reached the same verdict by leg on the same grounds, and each of its claims I could check lan
reader B L32: **4.** **Verdict on reader A: CONSISTENT** — A's output quotes and cites the same eight entries at the same lines with the same
reader B L94: **4.** **Verdict on reader C: CONSISTENT** — C's output quotes and cites the same eight entries at the same lines with the same
reader C L29: **Verdict on reader A: CONSISTENT**, because its findings, quotations and addresses match the same spans I read, and it reaches the same outcome by leg (the gat
reader C L92: **Verdict on reader B: CONSISTENT**, because its quotations and addresses match the same spans I read, and its outcome by leg is the same as mine; its one loose
```

## The merge

One merge writer (fresh; not a reader), brief `scratchpad/zs/pieces/P07C_Imports/M/brief.md` (template `zs_merge_brief.md`; `sha256` `7ac25346c1f27b11`), merge rule `M-246` as `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` §N.2 states it. Its return, as given: `Amendment_Rederivation_P07C_Imports_2026-11-10.md — 810 lines (wc -l). Under M-246 the piece merges readers A, B and C into Findings 1-23, Choices 24-48 and Questions 49-52, and gives its verdict by leg: the gateway leg FLIPS on DR-133 (the cluster's shared harbor is now the partner's fourth receiving node, which this city holds with the cluster and does not hold alone), the coastal line's mode NARROWS (by road, certainly, with the sea leg under research), and the trade-hub leg, the inbound direction, the three routes and the construction-material exclusion HOLD. Section 5 settles 12 reader splits by content.`

## Merge checks (run on the piece before this record existed)

**1 · Normalized quotation pre-check** (`scratchpad/zs/tools/zs_postmerge.py`; corpus: the list's sources whole, the pass's numbered files and amendment notes, the reader outputs and Round 3 replies, the item outputs). Raw output, whole:

```
corpus files: 37; quoted strings (12+ chars, paired within a block): 95; not found: 0; blocks with an odd quote count (hand-check): 0
```

**2 · Quotation audit** (`python3 Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/quotation_audit.py "<pass folder>" --files <piece> --own-pass`, from the repo root; tool last committed 2026-11-02; no uncommitted edits). Raw output, excerpted (11 miss lines omitted, kept whole beside the pass as `.t8_xc_P07C_Imports_quotation_audit.txt`):

```
pass audited : Zhongshan_Opus
corpus mode  : default (own pass excluded)
corpus files : 6901   chars: 109,169,865
files audited: Amendment_Rederivation_P07C_Imports_2026-11-10.md
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
fragments tested (single-line, ellipsis-split, >=7 words): 29
NOT FOUND in corpus: 11
  of those, in TABLE CELLS : 4
  of those, in PROSE       : 7


⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.

exit 0
```

**2b · Triage of the audit's misses** (same script; the audit reads no dot-file). Raw output, whole:

```
audit NOT FOUND fragments: 11; (a) found in the corpus: 3; (b) the piece's own unquoted prose: 5; (c) for hand triage: 3
  (c) L99: (l333-334), which falls with it (finding 3)
  (c) L508: [CELL]  that only the neutral route is ruled to bring the second power's supply; the staging ports and their distances; 5.6c's shared port
  (c) L596: (reader c l354-355), and a, who named only the route question, accepted both in round 3
```

Hand triage of class (c): 3 fragments in class (c), each read at its line: L99 and L596 are the piece's prose between two adjacent quotations; L508 is a table cell of the piece's own wording. Pre-check: 0 strings not found. No misquotation found.

**3 · American English sweep** (British forms; only "judgement" is kept). Raw output: none (0 hits).

**4 · Other locations' names and status words** (`grep` for 56 names and aliases, whole words; and for complete, completed, ready). Raw output: names none; status words none.

*Record written 2026-11-10 14:04 by script from the files named above; the checks ran on the piece, not on this record.*
