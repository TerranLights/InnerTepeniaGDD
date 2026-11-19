# Ariun Nuur — ULM Step 1 — T8 round record

**Unit:** Step 1, the audit of inherited material (Gate 9's first run). **Written:** `01_Inherited.md` (356 lines; PROPOSED, not declared
complete). **Run mode:** WARM (`DR-6`). **Date:** 2026-11-19; brief frozen and readers dispatched 05:04, Round 1 back by 05:18, Round 3
by 05:22, merge returned 05:32, record 05:35.
**List:** `.t8_required_01_Step1.txt` (8 entries, 1,189 admitted lines): runbook Step 1 (L2523–2539); Gate 9's own entry in `04`
(L221–240), which the runbook's Step 1 box sends the reader to; the Gate 9 card; the spec, whole (the Pre-Trip's Step 1 read); the Step −1
contract and the Step 0 frame (the earlier steps' outputs); the Step 1 and 2 datasheet; `DR-143` (rulings log L2058–2065, the developer's
answers of 2026-11-18). **Brief:** `.t8_brief_01_Step1.md` (174 lines; frozen at dispatch; sha256[:16] 2a2e644fd1e0c762; 16
orchestrator-verified results). Reader outputs archived here as `.t8_Step1_reader{A,B,C}.md`; Round 3 replies saved on arrival as
`.t8_Step1_round3_reader{A,B,C}.md`. Three Opus readers; one fresh Opus merge writer (`M-246`).

## Between the brief's freeze and the readers' return — `DR-143`'s approved edits (orchestrator)

Applied 05:07, to files **not on this unit's list**, each backed up in the scratchpad first, no cited line moved: the Step −1 datasheet
(five exclusion rows appended after L47; L1–47 byte-identical to the backup), the Step 0 datasheet (L5, L6, L9, L20, L25, L28 in place,
dated; 28 lines before and after), `Run_Modes_Warm_and_Cold.md` (L53, L99, L109, L118, L138; 181 lines before and after; **M-407**), and
the `Disciplines/00b` copy (L3 re-pinned to f2d0237b06885373 · 157 lines after a command check that neither version of the original's L97
appears in the copy). `verify_city_sheets.py Ariun_Nuur` after: 20 checks, 0 FAIL, 2 NOTE; `audit_city_inputs.py`: 40 tests, GAP 0.
**Self-correction:** `DR-143`'s consequence line said "before Step 1's brief is frozen"; the edits came three minutes after. No frozen
input changed; the merge brief stated the timing, and `01_Inherited.md` carries it.

## Round 1 — receipts (as returned)

| Reader | Output lines | Audit rows (carried + new) | Shadows | Reserved | Requests | Questions | Handoff sweep | Manifest |
|---|--:|--:|--:|--:|--:|--:|---|---|
| A | 264 | 14 + 5 | 1 | 4 | 4 | 3 | 4 lines (2 answered, 2 n/a) | 8 of 8 |
| B | 233 | 14 + 5 | 1 | 5 | 4 | 3 | 3 lines (2 answered, 1 n/a) | 8 of 8 |
| C | 256 | 14 + 6 | 1 | 5 | 5 | 2 | 15 rows (9 answered, 6 carried) | 8 of 8 |

## Round 2 — `Tools/triple_read_verify.py` (last commit `8777bb5f` 2026-11-03; clean), first run, raw output whole

```
required files: 8
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2523-2539] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/04_QA_Gates_and_Differentiation.md  [range 221-240] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Stepwise_Execution/02_Gates/G10_Gate_9_Asymmetry.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Ariun_Nuur.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.1_Step_MINUS-1_Input_Contract.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00_Frame.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/Datasheets/Step_1_and_2.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 2058-2065] ===
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

**All six CONSISTENT; no repair, no re-dispatch.** The (c) points became Q-29 to Q-35 of `01_Inherited.md`; Q-28 is one question two
readers raised. Filed as `DEC-708` to `DEC-715`, with `DEC-716` from REQ-24 (below).

## Procedural events (the recording law)

1. **Reader A** wrote to its own output with `printf` and `cat >>` heredocs and made its staging folder with `mkdir -p`; **readers A and
   C** piped `sed` output through `cut` for display. The brief barred any command on any file but `wc -l` and `sed -n`. All self-reported;
   no content effect.
2. **The tower's name:** written 0 times in any reader output or in the merge (checked by count).
3. **The merge writer** created no other file and opened the spec at L145 and L171 only, to settle two splits at source.
4. **The orchestrator,** while settling REQ-26's addresses for Step 2, read the lines naming this city in `Division_of_Industry/15_…md`
   (a file the Pre-Trip does not send any step to) by a line-number search, other names masked. Nothing from it is carried into any brief;
   Step 2's list adds only `16`'s own definitional spans.

## Quotation checks, before this record existed

**Pre-check (T8 line 13), per quotation, normalized** (`<scratchpad>/t8/checks.py`; every string in straight or curly double quotes, 6
characters or longer, checked against the 8 list files at their spans and the brief). Raw:

```
quoted strings checked: 50 not found: 1
  MISS: Gate 9 runs a second time, at Step 7
01_Inherited.md British-form hits: []
other-location name scan (names: line numbers): {'Mirny': [14, 110, 350]}
tower-name count: 0
```

**Triage:** the one miss is a wrapped blockquote line at runbook L2527–2528 (`(Gate` / `>   9 runs a second time, at Step 7, …`); the
words match once the continuation marker is removed. **Not a defect.**

**`Tools/quotation_audit.py`** (last commit `5a63e074` 2026-11-02; clean), `--step 1 --own-pass`. Whole output saved beside this record
as `.t8_Step1_quotation_audit.txt`; result block, raw:

```
=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 16
NOT FOUND in corpus: 4
  of those, in TABLE CELLS : 3
  of those, in PROSE       : 1

  [01_Inherited.md:220]  [CELL]  while contract cr-45 excludes l149 and dr-143 item 10 ( dec-691 ) holds it so (a, b, c). (b) l7
  [01_Inherited.md:220]  [CELL]  where contract cr-43 holds it a coordinate only (a). (e) l5-6: the pointer sentence is spliced into the middle of the
  [01_Inherited.md:220]  [CELL]  sentence, the same splice the frame found in the step 0 sheet (frame l195) (b, c). (f) l6's
  [01_Inherited.md:251]           names a round 3 reply that checked the find at its source or accepted it as (a)

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```

**Triage:** all four are connective prose the tool captured between two adjacent quotations (L220's three spans; L251's legend
sentence), as its footer warns; the per-quotation pre-check finds every real quotation. **Confirmed defects: 0 (CELL 0, PROSE 0).**

## American English sweep and the one-location check

From the same script, raw: `01_Inherited.md British-form hits: []`. **No British spelling.** Name scan, raw:
`other-location name scan (names: line numbers): {'Mirny': [14, 110, 350]}` and `tower-name count: 0`. The three hits are the parent
subnet (a shared thing the city is in, `DR-136` item 3) and the pass folder's path. **No other location named.**

## REQ-30, answered by the orchestrator (against `DECISIONS_NEEDED_FROM_DEVELOPER.md`)

The frame's Q-16 to Q-27 are `DEC-695` to `DEC-706`, one to one, in order (each entry names its Q number in its heading). `DEC-707` is not
a Q row: it came from the held run-log entry AN-05 (the stale `00b` pin), filed beside Step 0's questions. 15 + 12 + 1 = 28.

## Tokens (from the task notifications; full rows in `Universal_Location_Methodology/TOKEN_LOG_Ariun_Nuur.md`)

| Agent | Round 1 | Round 3 (delta) | Last figure |
|---|--:|--:|--:|
| reader A | 243,549 | 48,009 | 291,558 |
| reader B | 217,519 | 50,926 | 268,445 |
| reader C | 229,210 | 51,023 | 280,233 |
| merge writer | — | — | 199,176 |
| **Unit total (sum of last figures)** | | | **1,039,412** |

Web calls: readers 0; `Tools/web_quota_count.py`: WebSearch: 0 | WebFetch: 0 | TOTAL: 0
**The record grows after this check** (T8 line 8): no DOUBLE-CHECK script was run on this record.
