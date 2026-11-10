# Shirayuki: T8 round record for P02B_Arrival (the arrival modes and the founding basis), 2026-11-10

**What this is.** The record of the three-reader rounds behind `Amendment_Rederivation_P02B_Arrival_2026-11-10.md` (the piece; 1285 lines, `sha256` `721d6945c91eee59`). It states what each tool returned and where each file is; it does not restate the piece. **Everything here is PROPOSED;** no pass file was edited. The run's log is `Amendment_Log_2026-11-10.md`.

**Items re-derived:** `SRY-C05`, `SRY-C08` (the note's section J gives each first-check verdict). **Pass places:** `04_Phase_02_Composition_and_Arrival.md` L99–L175 (§B, B.1 to B.5); `02_Spine.md` L84–L105 (§2c, `G4`), L270–L286 (§7, the spine's claims); `01_Inherited.md` L192–L223 (§4, A1); `00_Frame.md` L300–L312 (§7, the `G4` row).

## Round 0: the list and the briefs

The three readers' lists are identical (`cmp`). The list (11 entries), as dispatched:

```
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/Amendment_Notes_2026-11-10_Cross_Check.md :: 1-22,29-34,296-302,65-78,268-279,307,310
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_02_Composition_and_Arrival.md :: 99-175
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/02_Spine.md :: 84-105,270-286
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/01_Inherited.md :: 192-223
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/00_Frame.md :: 300-312
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Founding_Register.md :: 1-14,36,61
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md :: 538-554,623-649,654-663,919,930
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/STARTUP_Finished_City_Cross_Check_Shirayuki_then_Zhongshan_2026-11-10.md :: 62-67
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Shirayuki.md :: 23,203
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C05.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C08.md
```

Brief template `scratchpad/sry/tools/t8_template.md`; the three briefs differ only in reader letter, private staging folder and number range (A 1–99, B 101–199, C 201–299). Brief `sha256` A `98bec4dd78a8d34a`, B `a4688f5b6985f49b`, C `05366063eaf9e75c`. Before dispatch every brief's cited lines were checked against its list (`check_brief_vs_list` adapted for pieces; positive control returned two flagged ranges), and one generated brief was read end to end (log L-36). The piece's note range was out of ascending order in six of the seven pieces (log L-42).

## Round 1: three independent readers

- Reader A: `.t8_xc_P02B_Arrival_readerA.md` beside the pass (805 lines now, `sha256` `b95f3857a4125733`).
- Reader B: `.t8_xc_P02B_Arrival_readerB.md` beside the pass (404 lines now, `sha256` `82201501e5c45e46`).
- Reader C: `.t8_xc_P02B_Arrival_readerC.md` beside the pass (368 lines now, `sha256` `9ea18ff46e67be85`).

## Round 2: the mechanical check

Tool: `Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/triple_read_verify.py` (last committed 2026-11-03; no uncommitted edits).

**round2_run1.txt** (raw output, whole; also beside the pass as `.t8_xc_P02B_Arrival_round2_run1.txt`):

```
required files: 11
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/Amendment_Notes_2026-11-10_Cross_Check.md  [range 1-22,29-34,296-302,65-78,268-279,307,310] ===
  agent1   ⛔ LMID  MISMATCH  claimed="rests on, and that input's current value."  actual='`01_Inherited.md` L197–L204 (section A1); `02_Spine.md` L87;'
  agent2   ⛔ LMID  MISMATCH  claimed="rests on, and that input's current value."  actual='`01_Inherited.md` L197–L204 (section A1); `02_Spine.md` L87;'
  agent3   ⛔ LMID  MISMATCH  claimed="rests on, and that input's current value."  actual='`01_Inherited.md` L197–L204 (section A1); `02_Spine.md` L87;'

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_02_Composition_and_Arrival.md  [range 99-175] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/02_Spine.md  [range 84-105,270-286] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/01_Inherited.md  [range 192-223] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/00_Frame.md  [range 300-312] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Founding_Register.md  [range 1-14,36,61] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 538-554,623-649,654-663,919,930] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/STARTUP_Finished_City_Cross_Check_Shirayuki_then_Zhongshan_2026-11-10.md  [range 62-67] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Shirayuki.md  [range 23,203] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C05.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C08.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
⛔ NOT UNANIMOUS - DO NOT WRITE. Log which agent/file failed and why.
```

**round2_run2.txt** (raw output, whole; also beside the pass as `.t8_xc_P02B_Arrival_round2_run2.txt`):

```
required files: 11
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/Amendment_Notes_2026-11-10_Cross_Check.md  [range 1-22,29-34,296-302,65-78,268-279,307,310] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_02_Composition_and_Arrival.md  [range 99-175] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/02_Spine.md  [range 84-105,270-286] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/01_Inherited.md  [range 192-223] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/00_Frame.md  [range 300-312] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Founding_Register.md  [range 1-14,36,61] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 538-554,623-649,654-663,919,930] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/STARTUP_Finished_City_Cross_Check_Shirayuki_then_Zhongshan_2026-11-10.md  [range 62-67] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Shirayuki.md  [range 23,203] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C05.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C08.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

Between the runs, each failing reader repaired its own failed field(s) by hand under `DR-117` item 2; each reader's reading log carries a "Round 2 repair:" line with the old and new value; a `diff` against a pre-repair copy showed only those fields and the repair lines changed (log L-42 onward). Cause: the orchestrator's out-of-order range string.

## Round 3: the cross-check (each reader continued by SendMessage with the other two outputs)

The verdict lines, as `grep` returns them from each reply (each reply also beside the pass as `.t8_xc_P02B_Arrival_round3_reader<X>.md`):

```
reader A L33: **P02B_Arrival-A-R3-4. (4) Verdict on reader B: CONSISTENT.** Its quotations, line numbers, positional readings and line
reader A L114: **P02B_Arrival-A-R3-10. (4) Verdict on reader C: CONSISTENT.** Its quotations, spans, positional lines and counts match
reader B L31: - P02B_Arrival-B-R3-4. **Verdict: CONSISTENT.** Every admitted-line citation of A's that I checked lies in spans we both
reader B L104: - P02B_Arrival-B-R3-10. **Verdict: CONSISTENT.** Every admitted-line citation of C's that I checked lies in spans we both
reader C L25: - P02B_Arrival-C-R3-8. **CONSISTENT.** A quotes the same lines I read with the same wording and the same positional PROOF values (including the repair
reader C L47: - P02B_Arrival-C-R3-16. **CONSISTENT.** B's quotations and PROOF values match the lines I read, and its two departures are an over-reach on an undated
```

## The merge

One merge writer (fresh; not a reader) on `scratchpad/sry/pieces/P02B_Arrival/M/brief.md` (template `merge_template.md`; `sha256` `b24be7d509c0f404`), merge rule `M-246` as `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` §N.2 and the runbook state it. Its return, as given: `Section 3 rows (98 in total): 58 written (union), 10 written (conservative), 2 demoted, 16 question, 12 not written.`

## Merge checks (run before this record existed)

**1 · Normalized quotation pre-check** (`scratchpad/sry/tools/quote_precheck.py`; corpus: the list's sources whole, the pass's numbered files and amendment notes, the readers' outputs, Round 3 replies and item verdicts). Raw output, whole:

```
quoted strings checked: 172; found: 155; not found: 17
  NOT FOUND: Amendment_Rederivation_P02B_Arrival_2026-11-10b_T8_Rounds.md
  NOT FOUND:  (L9); such files 
  NOT FOUND:  (startup L66). Per-nation figures are weighting, 
  NOT FOUND:  (L122). It follows from three absences: *Chose it* would have supplied 
  NOT FOUND:  and is absent because 
  NOT FOUND:  (L117); *Stopped while passing* is absent because 
  NOT FOUND:  (L117). The first check made the same point: 
  NOT FOUND:  (`02_Spine.md` L279). The 
  NOT FOUND:  (L134); *Stopped while passing* 
  NOT FOUND:  (L144), and the culture 
  NOT FOUND:  (L160), and 
  NOT FOUND:  (L161). The coda opens 
  NOT FOUND:  (L165). It is 
  NOT FOUND:  (L97). The quadrant: 
  NOT FOUND:  (L280). The mechanistic reading glosses the last clause as 
  NOT FOUND:  (L284), because the export is a reputation and 
  NOT FOUND:  (L218–L219). 
```

**2 · Quotation audit** (`python3 Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/quotation_audit.py "<pass folder>" --files <piece> --own-pass`, from the repo root; tool last committed 2026-11-02). Raw output, excerpted (9 miss lines omitted, kept whole in `.t8_xc_P02B_Arrival_quotation_audit.txt` beside the pass):

```
pass audited : Shirayuki
corpus mode  : default (own pass excluded)
corpus files : 6812   chars: 105,888,057
files audited: Amendment_Rederivation_P02B_Arrival_2026-11-10.md
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
NOT FOUND in corpus: 9
  of those, in TABLE CELLS : 0
  of those, in PROSE       : 9


⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```

**2b · Triage of the audit's misses** (`scratchpad/sry/tools/audit_triage.py`; the audit reads no dot-file and its fragmenter captures text between two quotations). Raw output, whole:

```
audit NOT FOUND fragments: 9; (a) found in other inputs: 3; (b) piece's own unquoted prose: 0; (c) for hand triage: 6
  (c) L9: amendment rederivation p02b arrival 2026-11-10b t8 rounds.md
  (c) L201: (l122). it follows from three absences: chose it would have supplied
  (c) L202: (l117); stopped while passing is absent because
  (c) L228: (l117). the first check made the same point
  (c) L572: (l280). the mechanistic reading glosses the last clause as
  (c) L573: (l284), because the export is a reputation and
```

Hand triage of class (c): the six (c) fragments were read in full by the orchestrator: L9 is the name of this round record, which the merge brief told the writer to name (not a quotation of a source); L201, L202, L228, L572, L573 are the piece's own prose between quotations that wrap across physical lines. The pre-check's 17 misses are of the same two kinds. Confirmed defects: 0 (CELL 0, PROSE 0). The American English sweep's four hits: three are "realism" (an American form the pattern matches by mistake) and one is "defence" inside a source's domain name (dn-defence.com, in the research list at L1221), kept exactly.

**3 · American English sweep** (pattern of British forms; only "judgement" is kept). Raw output: 

```
425:realism
798:realism
1073:realism
1221:defence
```

**4 · Other locations' names and status words** (`grep` for 46 location names and aliases; and for complete/completed/ready). Raw output: names none; status words none.

*Record written 2026-11-10 06:30 by script from the files named above; the record grows after no check (the checks ran on the piece, not on this record).*
