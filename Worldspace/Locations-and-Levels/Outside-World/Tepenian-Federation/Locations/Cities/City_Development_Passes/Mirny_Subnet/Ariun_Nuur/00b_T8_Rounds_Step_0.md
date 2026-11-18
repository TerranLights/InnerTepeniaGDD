# Ariun Nuur — ULM Step 0 (and Phase 0) — T8 round record

**Unit:** Step 0, the frame; Phase 0 is its content. **Written:** `00_Frame.md` (431 lines; PROPOSED, not declared complete).
**Run mode:** WARM (`DR-6`). **Date:** 2026-11-18; started 14:01 on the developer's word ("continue going with the following Step
(even though it's almost 2:00pm)"), dispatch about 14:02, merge returned about 14:31, record 14:33.
**List:** `.t8_required_00_Step0.txt` (14 entries, 2,832 admitted lines). Added to the Pre-Trip's Step 0 reads, each for a stated
reason: runbook L747 (the `Access type` closed set, for the contract's REQ-12); the spine's Phase 0, L274–320 (Pre-Trip §D, Phase 0
governing); the Step −1 contract (T8 line 16). Cut to this city's own lines: the census (L1–41, L432–440, L520) and the extent table
(header L601–604, row L625). **Brief:** `.t8_brief_00_Step0.md` (frozen at dispatch; 17 orchestrator-verified results). Reader
outputs archived here as `.t8_Step0_reader{A,B,C}.md`; Round 3 replies saved on arrival as `.t8_Step0_round3_reader{A,B,C}.md`.
Three Opus readers; one fresh Opus merge writer (`M-246`).

## Step 0.2 — the disciplines, read by the orchestrator (`DR-14`, "Split it")

`Disciplines/00b_General_Population_Discipline.md` (261 lines), `00d_Shadow_Proportion_Discipline.md` (222), `00f_Review_Panel.md`
(834), each read in full at 14:02–14:05. The originals' pins, re-verified by `sha256sum | cut -c1-16` and `wc -l` (raw):

```
00b_General_Population_Discipline.md f2d0237b06885373 157
00d_Shadow_Proportion_Discipline.md b1caf2af79a7dc8c 123
00f_Review_Panel.md 33d660ebfbbca9e9 737
```

**`00b` is STALE against its pin (6a08080e1a8da883, 157 lines).** `git log` shows one change since the pin, commit `e351f6d5`
(2026-10-31), a one-line replacement at L97 of the original (read by `--stat` and hunk header only), inside the passage whose worked
instances the ULM copy carries as pointers. The copy is used as read; re-pinning is maintenance, filed as `DEC-707`. `00d` and `00f`
match their pins.

## Round 1 — receipts (as returned)

| Reader | Output lines | Declaration lines | Reserved (carried + new) | Requests | Questions | Handoff rows | Manifest |
|---|--:|--:|--:|--:|--:|--:|---|
| A | 535 | 18 | 16 + 6 | 7 | 6 | 7 | 14 of 14 |
| B | 349 | 21 | 16 + 6 | 10 | 4 | 7 | 14 of 14 |
| C | 711 | 20 | 16 + 7 | 9 | 7 | 7 | 14 of 14 |

## Round 2 — `Tools/triple_read_verify.py` (last commit `8777bb5f` 2026-11-03; clean), first run, raw output whole

```
required files: 14
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 747,2455-2522] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/06_Worked_Example_Provenance.md  [range 1-38,429-437] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/01_Frame_Typology_and_Inheritance.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Run_Modes_Warm_and_Cold.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Repo_Scope.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Timeline Eras/2 The Second Interwar Period/README.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Timeline Eras/2 The Second Interwar Period/Timeline.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md  [range 1-41,432-440,520] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Extent_and_Density_Per_City.md  [range 601-604,625] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/04_QA_Gates_and_Differentiation.md  [range 96-109] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 274-320] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.1_Step_MINUS-1_Input_Contract.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/Datasheets/Step_0.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

## Round 3 — cross-check verdicts (the first two verdict lines of each reply)

| Reader | On | Verdict |
|---|---|---|
| A | B | CONSISTENT |
| A | C | CONSISTENT |
| B | A | CONSISTENT |
| B | C | CONSISTENT |
| C | A | CONSISTENT |
| C | B | CONSISTENT |

**All six CONSISTENT; no repair, no re-dispatch.** Round 3's citation corrections (Band 4 at `01` L180, not L181; the robot-physiology
cold sentence at L12, not L13) were checked at source by the merge writer and written at the corrected lines. The (c) points became
Q-16 to Q-27 of the frame, filed as `DEC-695` to `DEC-706`.

## Procedural events (the recording law)

1. **Reader B** ran `grep -xF` on its own output file; **reader A** ran `wc -l` on its own output; the brief allowed `wc -l` and
   `sed -n` on listed files only and barred `grep` on any file. Raised in Round 3; no content effect.
2. **Readers A and C** wrote the national tower's name in their reading logs, although A marked the positional line carrying it EXEMPT
   and C's should have been marked (C's own correction in Round 3). The merge writer was told to refer to it by its role; the frame
   does not carry the name. Whether that structure's name counts as a forbidden location name is put to the developer as Q-21 (`DEC-700`).
3. **The merge writer** created no other file (the instruction was tightened after Step −1's merge left two drafts).

## Quotation checks, before this record existed

**Pre-check (T8 line 13), per quotation, normalized:** every string in straight or curly double quotes, 6 characters or longer, checked
against the 14 list files and the brief. Raw: `quoted strings checked: 66 not found: 0`. **No rewrite needed.**

**`Tools/quotation_audit.py`** (last commit `5a63e074` 2026-11-02; clean), `--step 0 --own-pass`. Whole output saved beside this record
as `.t8_Step0_quotation_audit.txt`. Result block, raw output, excerpted (the self-test block and 6 of the 7 miss lines omitted; all in
the saved file):

```
=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 19
NOT FOUND in corpus: 7
  of those, in TABLE CELLS : 1
  of those, in PROSE       : 6

  [00_Frame.md:17]           is this pass's 00.1 step minus-1 input contract.md
```

**Triage:** the 7 misses are spans the tool captured between two adjacent quotations (file-list prose, line references), as its footer
warns; the per-quotation pre-check finds every real quotation. **Confirmed defects: 0 (CELL 0, PROSE 0).**

## American English sweep and the one-location check

A script over `00_Frame.md` for the British forms (-isation, -ise verbs, -our words, -yse, -tre, -ogue, -ence nouns, doubled -ll-):
raw `00_Frame.md hits: [(139, 'realistically'), (170, 'realistic')]` — both American forms caught by the stem pattern; **no British
spelling.** A name scan for other locations found only the parent subnet's name (L45, L99, L279, L314; the subnet is a shared thing
the city is in, `DR-136` item 3) and the pass folder's path (L428–429). **No other location named.**

## Tokens (from the task notifications; full rows in `Universal_Location_Methodology/TOKEN_LOG_Ariun_Nuur.md`)

| Agent | Round 1 | Round 3 (delta) | Last figure |
|---|--:|--:|--:|
| reader A | 248,957 | 65,797 | 314,754 |
| reader B | 249,550 | 64,106 | 313,656 |
| reader C | 278,346 | 63,159 | 341,505 |
| merge writer | — | — | 276,962 |
| **Unit total (sum of last figures)** | | | **1,246,877** |

Web calls: readers 0; `Tools/web_quota_count.py`: WebSearch: 0 | WebFetch: 0 | TOTAL: 0
**The record grows after this check** (T8 line 8): no DOUBLE-CHECK script was run on this record.
