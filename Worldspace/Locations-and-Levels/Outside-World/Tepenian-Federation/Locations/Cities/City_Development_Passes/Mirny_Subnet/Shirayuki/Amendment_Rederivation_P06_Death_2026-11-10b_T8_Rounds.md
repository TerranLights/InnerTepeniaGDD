# Shirayuki: T8 round record for P06_Death (death and the dead), 2026-11-10

**What this is.** The record of the three-reader rounds behind `Amendment_Rederivation_P06_Death_2026-11-10.md` (the piece; 349 lines, `sha256` `1abfb1448926393a`). It states what each tool returned and where each file is; it does not restate the piece. **Everything here is PROPOSED;** no pass file was edited. The run's log is `Amendment_Log_2026-11-10.md`.

**Items re-derived:** `SRY-U02` (the note's section J gives each first-check verdict). **Pass places:** `04_Phase_06_Meaning.md` L33–L67 (§A, the proposition), L141–L198 (§B, §C, §D); `00_Frame.md` L320–L333 (§8).

## Round 0: the list and the briefs

The three readers' lists are identical (`cmp`). The list (5 entries), as dispatched:

```
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/Amendment_Notes_2026-11-10_Cross_Check.md :: 1-22,29-34,296-302,313
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_06_Meaning.md :: 33-67,141-198
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/00_Frame.md :: 320-333
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md :: 71-190
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-U02.md
```

Brief template `scratchpad/sry/tools/t8_template.md`; the three briefs differ only in reader letter, private staging folder and number range (A 1–99, B 101–199, C 201–299). Brief `sha256` A `516ab14c539125ac`, B `d24cb4e22e586db2`, C `93117fd72577040f`. Before dispatch every brief's cited lines were checked against its list (`check_brief_vs_list` adapted for pieces; positive control returned two flagged ranges), and one generated brief was read end to end (log L-36). The piece's note range was out of ascending order in six of the seven pieces (log L-42).

## Round 1: three independent readers

- Reader A: `.t8_xc_P06_Death_readerA.md` beside the pass (538 lines now, `sha256` `40d9e40020b64631`).
- Reader B: `.t8_xc_P06_Death_readerB.md` beside the pass (216 lines now, `sha256` `a11280294f9a33f7`).
- Reader C: `.t8_xc_P06_Death_readerC.md` beside the pass (270 lines now, `sha256` `7d841da43642f0f4`).

## Round 2: the mechanical check

Tool: `Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/triple_read_verify.py` (last committed 2026-11-03; no uncommitted edits).

**round2_run1.txt** (raw output, whole; also beside the pass as `.t8_xc_P06_Death_round2_run1.txt`):

```
required files: 5
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/Amendment_Notes_2026-11-10_Cross_Check.md  [range 1-22,29-34,296-302,313] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_06_Meaning.md  [range 33-67,141-198] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/00_Frame.md  [range 320-333] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md  [range 71-190] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-U02.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

## Round 3: the cross-check (each reader continued by SendMessage with the other two outputs)

The verdict lines, as `grep` returns them from each reply (each reply also beside the pass as `.t8_xc_P06_Death_round3_reader<X>.md`):

```
reader B L51: - P06_Death-B-R3-8. **Reader A: CONSISTENT.** A read the same five entries at the same spans, its quotations match
reader B L138: - P06_Death-B-R3-23. **Reader C: CONSISTENT.** C read the same five entries at the same spans and its quotations
reader C L49: - **P06_Death-C-R3-9. Reader A: CONSISTENT.** A read the same five spans (identical positional fields and verifiable
reader C L128: - **P06_Death-C-R3-28. Reader B: CONSISTENT.** B read the same five spans (identical positional fields, verifiable
```

## The merge

One merge writer (fresh; not a reader) on `scratchpad/sry/pieces/P06_Death/M/brief.md` (template `merge_template.md`; `sha256` `c4fc1cf606d432da`), merge rule `M-246` as `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` §N.2 and the runbook state it. Its return, as given: `Section 3: 70 rows. written (union) 36, written (conservative) 10, demoted 0, question 11, not written 13.`

## Merge checks (run before this record existed)

**1 · Normalized quotation pre-check** (`scratchpad/sry/tools/quote_precheck.py`; corpus: the list's sources whole, the pass's numbered files and amendment notes, the readers' outputs, Round 3 replies and item verdicts). Raw output, whole:

```
quoted strings checked: 293; found: 284; not found: 9
  NOT FOUND:  for the ossuary.** A keeps 
  NOT FOUND:  only with canon's sense (holding and not taking) stated beside it (A-R3-10). B: whether to keep the pass's word at all is a developer question, because the word invites section A's sense, attention (
  NOT FOUND:  for the proposition's own sense, because using it for holding repeats the slide L179 made (C-R3-29, C-R3-43). **Merged:** the proposed texts use 
  NOT FOUND:  to an assumption, the share 
  NOT FOUND:  (C-R3-46). B's 
  NOT FOUND:  (A-R3-40); burial (Physiology L108) is not a partial answer, because it says what canon rules out nationally, not what the city does (A-68). In its Round 1 log A also corrected two of its own citatio
  NOT FOUND:  (C-R3-43); burial added (C-R3-44); C-223 narrowed (C-R3-45); 
  NOT FOUND:  for the ossuary; (d) the same restatement, keeping 
  NOT FOUND:  with canon's sense (holding and not taking) stated beside it; (e) withdraw the refinement and leave L178's question bare. **Recommended, PROVISIONAL: (c).** (a) rests on 
```

**2 · Quotation audit** (`python3 Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/quotation_audit.py "<pass folder>" --files <piece> --own-pass`, from the repo root; tool last committed 2026-11-02). Raw output, excerpted (53 miss lines omitted, kept whole in `.t8_xc_P06_Death_quotation_audit.txt` beside the pass):

```
pass audited : Shirayuki
corpus mode  : default (own pass excluded)
corpus files : 6812   chars: 105,888,057
files audited: Amendment_Rederivation_P06_Death_2026-11-10.md
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
fragments tested (single-line, ellipsis-split, >=7 words): 137
NOT FOUND in corpus: 53
  of those, in TABLE CELLS : 1
  of those, in PROSE       : 52


⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```

**2b · Triage of the audit's misses** (`scratchpad/sry/tools/audit_triage.py`; the audit reads no dot-file and its fragmenter captures text between two quotations). Raw output, whole:

```
audit NOT FOUND fragments: 53; (a) found in other inputs: 6; (b) piece's own unquoted prose: 44; (c) for hand triage: 3
  (c) L198: [CELL]  lean withdrawn and restated as a question; not replaced with
  (c) L315: survive options: (a) keep l179 as written; (b) the first check's reduced form
  (c) L323: (physiology l170) reach options: (a) the deferred block's analysis only (l147-l169), so the developer's words at l143 and the agin
```

Hand triage of class (c): the three (c) fragments (piece L198, L315, L323) were read in full by the orchestrator: each is the piece's own prose between two quotations on a line holding several quotations (for example L315's text between "KEEPING-PRACTICE" and the quoted reduced form), not a quotation. Confirmed defects: 0 (CELL 0, PROSE 0).

**3 · American English sweep** (pattern of British forms; only "judgement" is kept). Raw output: none (0 hits).

**4 · Other locations' names and status words** (`grep` for 46 location names and aliases; and for complete/completed/ready). Raw output: names none; status words none.

*Record written 2026-11-10 06:20 by script from the files named above; the record grows after no check (the checks ran on the piece, not on this record).*

---

**Correction, appended 2026-11-10 06:20 (not a rewording).** The Round 3 block above returned 4 of the 6 verdict lines: the
generator's pattern missed reader A's two, which are written without the word "verdict" or a reader name. The pattern was
corrected (it now matches any bold CONSISTENT/INCONSISTENT and refuses to write a record with other than six lines). Reader A's
two lines, as `grep` returns them:

```
reader A L43: - P06_Death-A-R3-9. **CONSISTENT.** Every quotation I checked sits on the line B cites, or across the wrap it names,
reader A L133: - P06_Death-A-R3-26. **CONSISTENT.** Every quotation I checked sits on the line C cites, its line numbers match my
```

All six cross-verdicts are CONSISTENT.
