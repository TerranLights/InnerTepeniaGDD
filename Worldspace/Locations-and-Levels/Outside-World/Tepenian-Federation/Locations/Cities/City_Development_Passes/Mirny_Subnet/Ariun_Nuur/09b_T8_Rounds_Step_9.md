# Ariun Nuur — ULM Step 9 (Record) — T8 round record

**Unit:** Step 9. **Written:** `09_Record.md` (1,544 lines; PROPOSED, not declared complete) and the observations-log entries M-417 to
M-456 (40, appended by the orchestrator to `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md`: `diff` 80 lines added, 0 removed). **Run
mode:** WARM (`DR-6`). **Date:** 2026-11-20. **List:** `.t8_required_09_Step9.txt` (11 entries; 48216c8a27d6589a). **Brief:**
`.t8_brief_09_Step9.md` (7406e9cc2a7774b1). **Merge brief:** `.t8_merge_brief_09_Step9.md` (8c664c33c995757e; nine points; see the
procedural events for its first fill). **Orchestrator inputs:** `.t8_Step9_deferrals.md`, `.t8_Step9_anchor_sweep.md`,
`.t8_Step9_trackers.md`. **No web call.**

## Round 1 — receipts
A 502 lines; B 590; C 708. MANIFEST 11 of 11 each. Deferral classification: A and B 88 in scope (2 to Step 9, 86 to Step 10), 17 not
deferrals; C 3 discharged, 96 handed on, 6 not deferrals (counting restatements separately). All three: no anchor moved.

## Round 2 — `Tools/triple_read_verify.py`, raw output whole (run 1)

```
required files: 11
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 3006-3079] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Test_Runs/OBSERVATIONS_and_Methodology_Findings.md  [range 8839-8855] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/Datasheets/Step_9.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/09.5_Log.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md  [range 1-57] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/08_Review_Panel.md  [range 1-982] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/06_Differentiation.md  [range 329-341] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.2_Position_Coverage_Ledger.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/.t8_Step9_deferrals.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/.t8_Step9_anchor_sweep.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/.t8_Step9_trackers.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

**Exact-field check** (`exact_fields.py`; raw output whole):

```
.t8_Step9_readerA.md cannot open /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/.t8_Step9_deferrals.md
.t8_Step9_readerA.md: 20 fields compared exactly, 0 differ
.t8_Step9_readerB.md cannot open /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/.t8_Step9_deferrals.md
.t8_Step9_readerB.md: 20 fields compared exactly, 0 differ
.t8_Step9_readerC.md cannot open /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/.t8_Step9_deferrals.md
.t8_Step9_readerC.md: 20 fields compared exactly, 0 differ
```
*(The helper could not open `.t8_Step9_deferrals.md`: the orchestrator's `cut` had split a multi-byte character, so the file is not valid UTF-8. That entry rests on `triple_read_verify.py`'s own match, which passed for all three readers.)*

## Round 3 — cross-check verdicts

- **Reader A:**
  - VERDICT B: CONSISTENT — B read the same material, its classification and counts of the deferral list match mine exactly (88 · 2 · 0 · 86 · 17), and where it differs from me it adds findings rather than contradicting mine, except that it calls the trackers free of overclaim.
  - VERDICT C: CONSISTENT — C read the same material and found three real holes I missed (Phase 9 L47–48, REQ-202, AN-13) plus a credit swap in the late Lover verdict; its counts differ from mine only because it treats restatements and the Q-175 line differently.
- **Reader B:**
  - VERDICT A: CONSISTENT — A's output plainly comes from the same eleven entries, and its deferral counts match mine exactly (88 · 2 · 0 · 86 · 17). It adds the Q-340 count condition and the MASTER line's Round 2 compression, which I missed, and has one small overreach (Q-317 named as a Step 10 hole).
  - VERDICT C: CONSISTENT — C's output plainly comes from the same material and catches several things I missed (the Phase 9 L47–48 holes, the swapped R2 late-Lover credits, the same-commit rule for the table). Its counts differ from mine only by convention, plus one Q-175 "discharged" that claims more than a draft can do.
- **Reader C:**
  - VERDICT A: CONSISTENT — A read the same material and reaches the same substance; the differences are counting conventions, a few misses on each side, and one misstatement in a draft.
  - VERDICT B: CONSISTENT — B read the same material and reaches the same substance, but it misses the MASTER tracker's compression of Round 2 failures and the panel count's dependence on Q-340.

**Six verdict lines, six CONSISTENT.**

## Checks on `09_Record.md` and the M-entries (`checks.py`; raw output whole)

```
quoted strings checked: 18 not found: 2
  MISS: not found by this instrument
  MISS: not found by this instrument
09_Record.md British-form hits: []
other-location name scan (names: line numbers): {}
tower-name count: 0
```

**Triage.** The one quotation missed (twice), *"not found by this instrument"*, is reader B's own proposed wording (`.t8_Step9_readerB.md`),
quoted as a proposal. The copied blocks match their sources byte for byte (the merge writer's `diff`); the marker line
`T5 - LATE LOVER FACULTY:` stands once (L929). The M-entries file: British 0, tower 0, other locations 0; 40 entries numbered 417–456
without a gap (the orchestrator's append script asserted it).

## Applied by the orchestrator after the merge
1. **M-417 to M-456** appended to the observations log (backup kept in the scratchpad).
2. **One dated status line** added to `MASTER_Process_Tracker.md` after the run's last line (L396); no older line edited (backup kept).
3. **Q-361 to Q-379** filed as `DEC-1078` to `DEC-1096` (19). **Next: `DEC-1097`.**
4. **AN-23** (Step 8, held while this step's list was frozen) and **AN-24** (Step 9) appended to `09.5_Log.md`.
5. **Not applied** (each a question or request in the record): the ledger's Parent cell; a pointer line beside the MASTER lines that
   overclaim; the erratum extensions; the same-commit rule for the differentiation table (the developer commits).

## Procedural events (the recording law)
1. **The orchestrator's deferral list** had overlapping globs (83 duplicate lines), cut lines without an excerpt label, a split character,
   and a pattern that missed bold or paired step names and the phases' own Step 10 rows; the readers found 8 holes, added as rows.
2. **The orchestrator's anchor sweep** matched file names only; its *appended only* claim was asserted, not diffed; its README block
   repeated 6 lines. No citation moved.
3. **The merge brief's first fill** went through an unquoted shell heredoc, which ran each backticked span as a command and stripped it;
   caught from the shell's errors before dispatch; the brief was rewritten with the Write tool and filled from a file.
4. **A reader's "credit swap"** in the panel's late Lover verdict was checked by the orchestrator at the reader files and killed by
   evidence (M-453).
5. **Command slips, disclosed by all three readers** (display pipes; `wc -l` on off-list files; one reader none on its own file). No
   PROOF field rests on them.
6. **The merge writer corrected the orchestrator's point 4:** *validated and corrected* stands at MASTER L391, not L392.

## Tokens
Readers (last figures, incl. Round 3) 1,006,484 (A 331,565 · B 326,226 · C 348,693); merge writer 336,804; **total 1,343,288**; web 0.
