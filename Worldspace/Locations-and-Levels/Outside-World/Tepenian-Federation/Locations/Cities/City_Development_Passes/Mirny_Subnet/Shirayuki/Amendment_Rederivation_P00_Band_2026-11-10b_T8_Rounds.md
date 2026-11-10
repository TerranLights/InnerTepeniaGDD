# Shirayuki: T8 round record for P00_Band (the population band), 2026-11-10

**What this is.** The record of the three-reader rounds behind `Amendment_Rederivation_P00_Band_2026-11-10.md` (the piece; 1079 lines, `sha256` `2a2342b9cd92b6d2`). It states what each tool returned and where each file is; it does not restate the piece. **Everything here is PROPOSED;** no pass file was edited. The run's log is `Amendment_Log_2026-11-10.md`.

**Items re-derived:** `SRY-C02` (the note's section J gives each first-check verdict). **Pass places:** `00_Frame.md` L19–L35 (the declaration's band lines), L150–L204 (§2 and §2a), L286–L298 (§6), L360–L377 (§10).

## Round 0: the list and the briefs

The three readers' lists are identical (`cmp`). The list (7 entries), as dispatched:

```
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/Amendment_Notes_2026-11-10_Cross_Check.md :: 1-22,29-34,296-302,24-61,127-144,281-294,304
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/00_Frame.md :: 19-35,150-204,286-298,360-377
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/01_Frame_Typology_and_Inheritance.md :: 162-230
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md :: 505,653
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md :: 203-252,1713
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Canon_Gap_Resolution_Method/Developer_Ruling_Queue.md :: 551-577
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C02.md
```

Brief template `scratchpad/sry/tools/t8_template.md`; the three briefs differ only in reader letter, private staging folder and number range (A 1–99, B 101–199, C 201–299). Brief `sha256` A `6aef550d95af43c0`, B `e3d8e1c30c862d53`, C `e904964a42cfa670`. Before dispatch every brief's cited lines were checked against its list (`check_brief_vs_list` adapted for pieces; positive control returned two flagged ranges), and one generated brief was read end to end (log L-36). The piece's note range was out of ascending order in six of the seven pieces (log L-42).

## Round 1: three independent readers

- Reader A: `.t8_xc_P00_Band_readerA.md` beside the pass (266 lines now, `sha256` `fd2d2b933fde28ba`).
- Reader B: `.t8_xc_P00_Band_readerB.md` beside the pass (314 lines now, `sha256` `3d7ee9ee4cde6ee6`).
- Reader C: `.t8_xc_P00_Band_readerC.md` beside the pass (285 lines now, `sha256` `79d3e3592915b17b`).

## Round 2: the mechanical check

Tool: `Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/triple_read_verify.py` (last committed 2026-11-03; no uncommitted edits).

**round2_run1.txt** (raw output, whole; also beside the pass as `.t8_xc_P00_Band_round2_run1.txt`):

```
required files: 7
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/Amendment_Notes_2026-11-10_Cross_Check.md  [range 1-22,29-34,296-302,24-61,127-144,281-294,304] ===
  agent1   ⛔ LINES MISMATCH  claimed='106'  actual='100'
  agent1   ⛔ LMID  MISMATCH  claimed='(Primary Japan; Significant Australia, Korea; Notable 35 row'  actual="- **Band.** Census I governs a city's band (`DR-4` 4.1, `LOG"
  agent2   ⛔ LINES MISMATCH  claimed='106'  actual='100'
  agent2   ⛔ LMID  MISMATCH  claimed='(Primary Japan; Significant Australia, Korea; Notable 35 row'  actual="- **Band.** Census I governs a city's band (`DR-4` 4.1, `LOG"
  agent3   ⛔ LINES MISMATCH  claimed='106'  actual='100'
  agent3   ⛔ LMID  MISMATCH  claimed='(Primary Japan; Significant Australia, Korea; Notable 35 row'  actual="- **Band.** Census I governs a city's band (`DR-4` 4.1, `LOG"

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/00_Frame.md  [range 19-35,150-204,286-298,360-377] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/01_Frame_Typology_and_Inheritance.md  [range 162-230] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md  [range 505,653] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 203-252,1713] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Canon_Gap_Resolution_Method/Developer_Ruling_Queue.md  [range 551-577] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C02.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
⛔ NOT UNANIMOUS - DO NOT WRITE. Log which agent/file failed and why.
```

**round2_run2.txt** (raw output, whole; also beside the pass as `.t8_xc_P00_Band_round2_run2.txt`):

```
required files: 7
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/Amendment_Notes_2026-11-10_Cross_Check.md  [range 1-22,29-34,296-302,24-61,127-144,281-294,304] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/00_Frame.md  [range 19-35,150-204,286-298,360-377] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/01_Frame_Typology_and_Inheritance.md  [range 162-230] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md  [range 505,653] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 203-252,1713] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Canon_Gap_Resolution_Method/Developer_Ruling_Queue.md  [range 551-577] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C02.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

Between the runs, each failing reader repaired its own failed field(s) by hand under `DR-117` item 2; each reader's reading log carries a "Round 2 repair:" line with the old and new value; a `diff` against a pre-repair copy showed only those fields and the repair lines changed (log L-42 onward). Cause: the orchestrator's out-of-order range string.

## Round 3: the cross-check (each reader continued by SendMessage with the other two outputs)

The verdict lines, as `grep` returns them from each reply (each reply also beside the pass as `.t8_xc_P00_Band_round3_reader<X>.md`):

```
reader A L17: - **P00_Band-A-R3-4. (4) Verdict on reader B: CONSISTENT.** Every quotation and figure of B's that I checked against lines I also read matches, and wh
reader A L41: - **P00_Band-A-R3-9. (4) Verdict on reader C: CONSISTENT.** Every quotation and figure of C's that I checked against lines I also read matches, and it
reader B L26: - **P00_Band-B-R3-9. Reader A: CONSISTENT.** Every quotation and figure I checked matches the lines I read, and its re-derived band (Band 5 on Census 
reader B L60: - **P00_Band-B-R3-26. Reader C: CONSISTENT.** Every figure I recomputed and every quotation I checked is found where cited; the one misplaced quotatio
reader C L25: - **P00_Band-C-R3-8. Reader A: CONSISTENT.** Every quotation and figure I checked against my own spans matches, and A's conclusions (Band 5 on Census 
reader C L57: - **P00_Band-C-R3-23. Reader B: CONSISTENT.** Every quotation and figure I checked matches my spans, and B's conclusions agree with mine on the band, 
```

## The merge

One merge writer (fresh; not a reader) on `scratchpad/sry/pieces/P00_Band/M/brief.md` (template `merge_template.md`; `sha256` `96f46afede4383e4`), merge rule `M-246` as `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` §N.2 and the runbook state it. Its return, as given: `Section 3 rows: 94 total — written (union) 64 · written (conservative) 5 · demoted 0 · question 8 · not written 17`

## Merge checks (run before this record existed)

**1 · Normalized quotation pre-check** (`scratchpad/sry/tools/quote_precheck.py`; corpus: the list's sources whole, the pass's numbered files and amendment notes, the readers' outputs, Round 3 replies and item verdicts). Raw output, whole:

```
quoted strings checked: 157; found: 127; not found: 30
  NOT FOUND:  (LOG L212). Its heading: 
  NOT FOUND:  (LOG L214). Its ground: 
  NOT FOUND:  (LOG L216); Census I is 
  NOT FOUND:  (LOG L216) 
  NOT FOUND:  (LOG L230). The obligation at the fifty-thousand threshold, 
  NOT FOUND:  (LOG L239) 
  NOT FOUND:  (LOG L240); decomposing early 
  NOT FOUND:  (LOG L244). The obligations are 
  NOT FOUND:  (LOG L248), 
  NOT FOUND:  (01 L180). Band 5 is 
  NOT FOUND: , with the unit 
  NOT FOUND:  (01 L187). The lower threshold: 
  NOT FOUND:  (01 L218); the later unit of analysis is 
  NOT FOUND:  (01 L219) 
  NOT FOUND:  (01 L220); 
  NOT FOUND:  (01 L220), namely 
  NOT FOUND:  (note L291). The queue text still carries the pass's figures: 
  NOT FOUND:  (QUEUE L575), and says the band will bind 
  NOT FOUND:  (note L26); 
  NOT FOUND: , and 4 — Urban (Frame L160). 
  NOT FOUND:  (Frame L163). Why it is not a rounding question: 
  NOT FOUND:  (Frame L173), and 
  NOT FOUND:  (Frame L180). §2a is headed 
  NOT FOUND:  (Frame L182) and lists 
  NOT FOUND:  (01 L221). It also follows from the ruling's level for the meantime, 
  NOT FOUND:  (01 L219) 
  NOT FOUND:  (Frame L289); the spec's vision-session notes are not read as an input (Frame L289–L290); 
  NOT FOUND:  (Frame L290) 
  NOT FOUND:  (note L56) and gives the city's rock share of its footprint as 
  NOT FOUND:  (Frame L295) 
```

**2 · Quotation audit** (`python3 Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/quotation_audit.py "<pass folder>" --files <piece> --own-pass`, from the repo root; tool last committed 2026-11-02). Raw output, excerpted (13 miss lines omitted, kept whole in `.t8_xc_P00_Band_quotation_audit.txt` beside the pass):

```
pass audited : Shirayuki
corpus mode  : default (own pass excluded)
corpus files : 6812   chars: 105,888,057
files audited: Amendment_Rederivation_P00_Band_2026-11-10.md
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
fragments tested (single-line, ellipsis-split, >=7 words): 44
NOT FOUND in corpus: 13
  of those, in TABLE CELLS : 0
  of those, in PROSE       : 13


⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```

**2b · Triage of the audit's misses** (`scratchpad/sry/tools/audit_triage.py`; the audit reads no dot-file and its fragmenter captures text between two quotations). Raw output, whole:

```
audit NOT FOUND fragments: 13; (a) found in other inputs: 6; (b) piece's own unquoted prose: 2; (c) for hand triage: 5
  (c) L93: (log l230). the obligation at the fifty-thousand threshold
  (c) L119: (note l291). the queue text still carries the pass's figures
  (c) L227: (frame l163). why it is not a rounding question
  (c) L327: (01 l221). it also follows from the ruling's level for the meantime
  (c) L497: (note l56) and gives the city's rock share of its footprint as
```

Hand triage of class (c): the five (c) fragments (piece L93, L119, L227, L327, L497) were read in full by the orchestrator: each is the piece's own prose between a quotation closing on that line and the next one opening on it (the quotations wrap across physical lines, which the per-line pairing cannot see). The pre-check's 30 misses are the same kind (for example " (LOG L212). Its heading: "). Confirmed defects: 0 (CELL 0, PROSE 0).

**3 · American English sweep** (pattern of British forms; only "judgement" is kept). Raw output: none (0 hits).

**4 · Other locations' names and status words** (`grep` for 46 location names and aliases; and for complete/completed/ready). Raw output: names none; status words none.

*Record written 2026-11-10 06:24 by script from the files named above; the record grows after no check (the checks ran on the piece, not on this record).*
