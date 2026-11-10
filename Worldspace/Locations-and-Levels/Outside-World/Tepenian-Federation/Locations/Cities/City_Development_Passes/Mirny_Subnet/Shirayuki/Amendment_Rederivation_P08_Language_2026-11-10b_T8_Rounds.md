# Shirayuki: T8 round record for P08_Language (the language and speech-marker reasoning), 2026-11-10

**What this is.** The record of the three-reader rounds behind `Amendment_Rederivation_P08_Language_2026-11-10.md` (the piece; 1153 lines, `sha256` `876413b9a82be1aa`). It states what each tool returned and where each file is; it does not restate the piece. **Everything here is PROPOSED;** no pass file was edited. The run's log is `Amendment_Log_2026-11-10.md`.

**Items re-derived:** `SRY-C03` (the note's section J gives each first-check verdict). **Pass places:** `04_Phase_08_Making.md` L1–L29, L198–L243 (§F, F.1), L306–L421 (the origin-stock addendum, F.STOCK at L404–L412); `04_Phase_09_Populations.md` L89–L101 (C.1, the language row at L96).

## Round 0: the list and the briefs

The three readers' lists are identical (`cmp`). The list (10 entries), as dispatched:

```
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/Amendment_Notes_2026-11-10_Cross_Check.md :: 1-22,29-34,296-302,189-220,305,315
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_08_Making.md :: 1-29,198-243,306-421
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_09_Populations.md :: 89-101
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md :: 1527,1664-1671,1703,1711-1712
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/STARTUP_Finished_City_Cross_Check_Shirayuki_then_Zhongshan_2026-11-10.md :: 62-67
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Language_Blocs_By_City_2026-11-03.csv :: 1,708-739
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Language_Sets_By_City_Reference_2026-11-03.md :: 1-5,34,75-80
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md :: 420-432
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C03.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-U04.md
```

Brief template `scratchpad/sry/tools/t8_template.md`; the three briefs differ only in reader letter, private staging folder and number range (A 1–99, B 101–199, C 201–299). Brief `sha256` A `4809259774ded15e`, B `39440ed44cb74ac8`, C `1093b5c9eba2a4ee`. Before dispatch every brief's cited lines were checked against its list (`check_brief_vs_list` adapted for pieces; positive control returned two flagged ranges), and one generated brief was read end to end (log L-36). The piece's note range was out of ascending order in six of the seven pieces (log L-42).

## Round 1: three independent readers

- Reader A: `.t8_xc_P08_Language_readerA.md` beside the pass (256 lines now, `sha256` `4d2a3e2c7da3e294`).
- Reader B: `.t8_xc_P08_Language_readerB.md` beside the pass (748 lines now, `sha256` `d359c5bd80010470`).
- Reader C: `.t8_xc_P08_Language_readerC.md` beside the pass (312 lines now, `sha256` `c6aedf29ed57b8ef`).

## Round 2: the mechanical check

Tool: `Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/triple_read_verify.py` (last committed 2026-11-03; no uncommitted edits).

**round2_run1.txt** (raw output, whole; also beside the pass as `.t8_xc_P08_Language_round2_run1.txt`):

```
required files: 10
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/Amendment_Notes_2026-11-10_Cross_Check.md  [range 1-22,29-34,296-302,189-220,305,315] ===
  agent1   ⛔ LMID  MISMATCH  claimed='|---|---|---|---|'  actual='**Current fact.**'
  agent2   ⛔ LMID  MISMATCH  claimed='|---|---|---|---|'  actual='**Current fact.**'
  agent3   ⛔ LMID  MISMATCH  claimed='|---|---|---|---|'  actual='**Current fact.**'

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_08_Making.md  [range 1-29,198-243,306-421] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_09_Populations.md  [range 89-101] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 1527,1664-1671,1703,1711-1712] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/STARTUP_Finished_City_Cross_Check_Shirayuki_then_Zhongshan_2026-11-10.md  [range 62-67] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Language_Blocs_By_City_2026-11-03.csv  [range 1,708-739] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Language_Sets_By_City_Reference_2026-11-03.md  [range 1-5,34,75-80] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md  [range 420-432] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C03.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-U04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
⛔ NOT UNANIMOUS - DO NOT WRITE. Log which agent/file failed and why.
```

**round2_run2.txt** (raw output, whole; also beside the pass as `.t8_xc_P08_Language_round2_run2.txt`):

```
required files: 10
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/Amendment_Notes_2026-11-10_Cross_Check.md  [range 1-22,29-34,296-302,189-220,305,315] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_08_Making.md  [range 1-29,198-243,306-421] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_09_Populations.md  [range 89-101] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 1527,1664-1671,1703,1711-1712] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/STARTUP_Finished_City_Cross_Check_Shirayuki_then_Zhongshan_2026-11-10.md  [range 62-67] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Language_Blocs_By_City_2026-11-03.csv  [range 1,708-739] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Language_Sets_By_City_Reference_2026-11-03.md  [range 1-5,34,75-80] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md  [range 420-432] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C03.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-U04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

Between the runs, each failing reader repaired its own failed field(s) by hand under `DR-117` item 2; each reader's reading log carries a "Round 2 repair:" line with the old and new value; a `diff` against a pre-repair copy showed only those fields and the repair lines changed (log L-42 onward). Cause: the orchestrator's out-of-order range string.

## Round 3: the cross-check (each reader continued by SendMessage with the other two outputs)

The verdict lines, as `grep` returns them from each reply (each reply also beside the pass as `.t8_xc_P08_Language_round3_reader<X>.md`):

```
reader A L20: P08_Language-A-R3-4. **Verdict on B: CONSISTENT.** Every source line I checked matches what I read, and the three points above are overstatements or a
reader A L37: P08_Language-A-R3-8. **Verdict on C: CONSISTENT.** Every source line I checked matches what I read, and C labels its stretches as inferences.
reader B L63: - **P08_Language-B-R3-11. Reader A: CONSISTENT.** Every in-world line A cites that falls within my ranges says what A
reader B L169: - **P08_Language-B-R3-28. Reader C: CONSISTENT.** Every in-world line C cites that falls within my ranges says what C
reader C L35: - P08_Language-C-R3-5. **CONSISTENT.** Every quotation, line position and figure I checked against my own reads of the same ranges matches.
reader C L109: - P08_Language-C-R3-18. **CONSISTENT.** Every quotation, line position and figure I checked matches my reads of the same ranges, and B's CRLF observat
```

## The merge

One merge writer (fresh; not a reader) on `scratchpad/sry/pieces/P08_Language/M/brief.md` (template `merge_template.md`; `sha256` `d01955862f48bb83`), merge rule `M-246` as `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` §N.2 and the runbook state it. Its return, as given: `Line count (wc -l): 1153; Section 3 rows by disposition (84 rows): written (union) 52; written (conservative) 13; demoted 1; question 14; not written 4.`

## Merge checks (run before this record existed)

**1 · Normalized quotation pre-check** (`scratchpad/sry/tools/quote_precheck.py`; corpus: the list's sources whole, the pass's numbered files and amendment notes, the readers' outputs, Round 3 replies and item verdicts). Raw output, whole:

```
quoted strings checked: 217; found: 198; not found: 19
  NOT FOUND:  (ROBOT L426); the delivery is 
  NOT FOUND:  (ROBOT L420). Build covers 
  NOT FOUND:  (START L66). As the spec stands, 
  NOT FOUND:  (P8 L207). The guard: 
  NOT FOUND:  (P8 L218), such as between a surface 
  NOT FOUND:  (P8 L231); the earlier phase's 
  NOT FOUND:  (P8 L227), and its only record is held 
  NOT FOUND:  (P8 L365), worked 
  NOT FOUND:  (P8 L375). In the stock the technique 
  NOT FOUND:  (P8 L374) 
  NOT FOUND:  (P8 L327) 
  NOT FOUND:  (P8 L409). The closing table refuses to 
  NOT FOUND:  (P8 L417) and to 
  NOT FOUND:  (P8 L354); goals and habits, 
  NOT FOUND:  (B L203) 
  NOT FOUND: ) with P8 L219 (
  NOT FOUND:  (fetch refused: 
  NOT FOUND: ; giri giri, used only for B-141); F9 https://imagesofoldhawaii.com/hole-hole-bushi/ (
  NOT FOUND: ); F15 https://discovernikkei.org/en/journal/2023/4/21/9557/ (Hayashi; 
```

**2 · Quotation audit** (`python3 Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/quotation_audit.py "<pass folder>" --files <piece> --own-pass`, from the repo root; tool last committed 2026-11-02). Raw output, excerpted (15 miss lines omitted, kept whole in `.t8_xc_P08_Language_quotation_audit.txt` beside the pass):

```
pass audited : Shirayuki
corpus mode  : default (own pass excluded)
corpus files : 6812   chars: 105,888,057
files audited: Amendment_Rederivation_P08_Language_2026-11-10.md
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
fragments tested (single-line, ellipsis-split, >=7 words): 53
NOT FOUND in corpus: 15
  of those, in TABLE CELLS : 1
  of those, in PROSE       : 14


⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```

**2b · Triage of the audit's misses** (`scratchpad/sry/tools/audit_triage.py`; the audit reads no dot-file and its fragmenter captures text between two quotations). Raw output, whole:

```
audit NOT FOUND fragments: 15; (a) found in other inputs: 8; (b) piece's own unquoted prose: 6; (c) for hand triage: 1
  (c) L651: [CELL]  marks a resident in either of the city's two languages
```

Hand triage of class (c): the one (c) fragment (L651, a table cell) was read in full by the orchestrator: it quotes reader C's own words, found exactly at `.t8_xc_P08_Language_readerC.md` L56 (and in C's Round 3 reply, L149); the triage script missed it only because the audit prefixes cell fragments with [CELL], which the script did not strip (a flaw in the orchestrator's script, noted). The pre-check's 19 misses are connective prose, including research-log text between quoted URLs. Confirmed defects: 0 (CELL 0, PROSE 0).

**3 · American English sweep** (pattern of British forms; only "judgement" is kept). Raw output: none (0 hits).

**4 · Other locations' names and status words** (`grep` for 46 location names and aliases; and for complete/completed/ready). Raw output: names none; status words none.

*Record written 2026-11-10 06:42 by script from the files named above; the record grows after no check (the checks ran on the piece, not on this record).*
