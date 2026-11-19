# Ariun Nuur — ULM Step 2 (and Phase 1) — T8 round record

**Unit:** Step 2, the spine; Phase 1 (constraint and capability) is its content. **Written:** `02_Spine.md` (769 lines; PROPOSED, not
declared complete). **Run mode:** WARM (`DR-6`). **Date:** 2026-11-19; brief frozen and readers dispatched 05:36, Round 1 back by 05:57,
repair and Round 2 run 2 at 05:58, Round 3 by 06:03, merge returned 06:22, record 06:24.
**List:** `.t8_required_02_Step2.txt` (20 entries, 3,139 admitted lines). Beyond the Pre-Trip's Step 2 reads (runbook L2540–2568; `02`;
the spine's Phase 1; the Phase 1 rows; `16` at L241–248, L282 and §23): `02` cut to L1–636, its §6 (symbol binding) held for Phase 10
(`DR-8`, `DR-8a`, `DR-115`); `16`'s status header, §1, §5 and the formula added for Step 1's REQ-26 and REQ-27, with the lines naming other
locations cut (L78, L80, L129, L137–138); the earlier steps' outputs; the picks and their two research files (the picks a full generator
from the start, `DR-138` item 2); the language-set row and language-bloc section (the frame's REQ-19); the national power-supply file and
the grid-failure file (`DEC-705`); `DR-143`. **Not listed, with an orchestrator-verified result instead:** the geothermal file (the city
is not among its six), the universe repo's location README (a roster line), the stations file's L97. **Brief:** `.t8_brief_02_Step2.md`
(222 lines; frozen at dispatch; sha256[:16] a773580332287848; 21 orchestrator-verified results; Step 1's Q-30 applied provisionally).
Reader outputs archived here as `.t8_Step2_reader{A,B,C}.md` (B's first version as `.t8_Step2_readerB_prerepair.md`); Round 3 replies
saved on arrival as `.t8_Step2_round3_reader{A,B,C}.md`. Three Opus readers; one fresh Opus merge writer (`M-246`).

## Round 1 — receipts (as returned)

| Reader | Output lines | Selected | Shape | Cells (agree / conflict / silent) | Deficits · addresses | New asymmetry rows | RF · REQ · Q | Handoff places | Manifest |
|---|--:|---|---|---|---|--:|---|--:|---|
| A | 593 | G2 · G7 · G8 | Balanced, both sets | 9 / 2 / 1 | 8 · 7 + 1 undetermined | 16 | 6 · 10 · 6 | 26 | 20 of 20 |
| B | 822 | G2 · G7 · G8 | Cost-dominant, both sets (withdrawn in Round 3) | 9 / 1 / 2 | 8 · 8 | 19 | 9 · 10 · 5 | 30 | 20 of 20 |
| C | 633 | G2 · G7 · G8 | Balanced, both sets | 9 / 2 / 1 | 7 · 6 + 1 not readable | 15 | 8 · 8 · 7 | 52 | 20 of 20 |

## Round 2 — `Tools/triple_read_verify.py` (last commit `8777bb5f` 2026-11-03; clean)

**Run 1, raw output whole — NOT UNANIMOUS:**

```
required files: 20
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2540-2568] ===
  agent1   ✅ all fields match ground truth
  agent2   ⛔ LLAST MISMATCH  claimed='attach.'  actual=''
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/02_Generators_Capability_and_Symbols.md  [range 1-636] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 321-400] ===
  agent1   ✅ all fields match ground truth
  agent2   ⛔ LLAST MISMATCH  claimed='---'  actual=''
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/01_Inherited.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/Datasheets/Step_1_and_2.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Climate Data/READER/Vostok.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Stations/Antarctic_Stations_With_Airstrips.md  [range 11,67] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/16_Per_City_Three_Tier_Run.md  [range 1-12,21-33,72-77,79,81-85,122-128,130-136,139-141,241-248,282,2349-2358] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Energy_Grid_Failure_Rationale.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/../Infrastructure/Amundsen_Power_Supply.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Inspirational-Influences.md  [range 92-95] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Ariun_Nuur_Inspiration_Place_Research_R1.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Ariun_Nuur_Inspiration_Place_Research_R2.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Language_Sets_By_City_Reference_2026-11-03.md  [range 1-6,28] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Language_Blocs_By_City_2026-11-03.md  [range 856-875] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Extent_and_Density_Per_City.md  [range 601-604,625] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 2058-2065] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
⛔ NOT UNANIMOUS - DO NOT WRITE. Log which agent/file failed and why.
```

**What failed, confirmed at source:** reader B's LLAST for the runbook range (L2568) and the phase-spine range (L400). Both lines are blank
(`sed -n` with `cat -A`); B gave the line above each. B's first version kept; B asked to correct only those two fields; the diff against
the first version is two lines (L663, L680), nothing else.

**Run 2, raw output whole — UNANIMOUS:**

```
required files: 20
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2540-2568] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/02_Generators_Capability_and_Symbols.md  [range 1-636] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 321-400] ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/01_Inherited.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/Datasheets/Step_1_and_2.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Climate Data/READER/Vostok.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Stations/Antarctic_Stations_With_Airstrips.md  [range 11,67] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/16_Per_City_Three_Tier_Run.md  [range 1-12,21-33,72-77,79,81-85,122-128,130-136,139-141,241-248,282,2349-2358] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Energy_Grid_Failure_Rationale.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/../Infrastructure/Amundsen_Power_Supply.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Inspirational-Influences.md  [range 92-95] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Ariun_Nuur_Inspiration_Place_Research_R1.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Ariun_Nuur_Inspiration_Place_Research_R2.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Language_Sets_By_City_Reference_2026-11-03.md  [range 1-6,28] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Language_Blocs_By_City_2026-11-03.md  [range 856-875] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Extent_and_Density_Per_City.md  [range 601-604,625] ===
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

**All six CONSISTENT; no further repair.** Reader B withdrew its shape name (its own count puts STRENGTH largest). The (c) points became
Q-36 to Q-53 of `02_Spine.md`, filed as `DEC-717` to `DEC-734`.

## Procedural events (the recording law)

1. **Reader B's** two positional slips (above); its reading log still names the line above each (raised in Round 3; log only). B's stations
   PROOF QUOTE repeats a name its own EXEMPT line covers (a PROOF field; the merge copies no PROOF block).
2. **Reader C** ran `wc -l` on its own output; **reader A** piped `sed` through `cat -A` and ran `python3 -I -c` on typed numbers; **reader B**
   piped `sed` through `cut`. All self-reported; no content effect. All three wrote their outputs with Write and Edit, as told.
3. **The tower's name** appears once in each reader output, inside a positional PROOF line marked EXEMPT; 0 times in the merge.
4. **The merge writer** created no other file and opened canon twice inside admitted spans (R1 L282; contract L80–85, L144–160).
5. **The orchestrator,** while building this list, printed lines of three multi-city files that showed other cities' items (logged in the
   progress file at 05:36); nothing carried beyond the geothermal ruling's bearing on this city.

## Quotation checks, before this record existed

**Pre-check (T8 line 13), per quotation, normalized** (`<scratchpad>/t8/checks.py`, against the 20 list files at their spans and the
brief). First run, raw:

```
quoted strings checked: 64 not found: 4
  MISS: power file
  MISS: hard to reach
  MISS: a place people come to
  MISS: not contested
02_Spine.md British-form hits: []
other-location name scan (names: line numbers): {'Mirny': [12, 65, 337, 413, 747]}
tower-name count: 0
```

**Triage:** "power file" (L12) and "not contested" (L603) are the file's own legend labels, not quotations. "hard to reach" and "a place
people come to" (L218) were readers' paraphrases in quotation marks: **rewritten as italics** by the orchestrator (one line changed; diff
against the merge's backup, 2 lines). After the fix, raw:

```
quoted strings checked: 62 not found: 2
  MISS: power file
  MISS: not contested
02_Spine.md British-form hits: []
other-location name scan (names: line numbers): {'Mirny': [12, 65, 337, 413, 747]}
tower-name count: 0
```

**`Tools/quotation_audit.py`** (last commit `5a63e074` 2026-11-02; clean), `--step 2 --own-pass`. Whole output saved beside this record as
`.t8_Step2_quotation_audit.txt`; result block, raw:

```
=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 17
NOT FOUND in corpus: 7
  of those, in TABLE CELLS : 2
  of those, in PROSE       : 5

  [02_Spine.md:12]           are this pass's step -1, step 0 and step 1 files
  [02_Spine.md:12]           is the national power-supply file (entry 13)
  [02_Spine.md:33]  [CELL]  (l3), and the same file says canon does not establish the grid's layout
  [02_Spine.md:44]  [CELL]  read as a technology and the agency's funding thread with three linked sites; the program
  [02_Spine.md:312]           l81-83, l118, l121) and behind it the station's data in the record's upstream source (record l16); for daylight, a computation
  [02_Spine.md:338]           bedrock about 4 km down, food term at 10% mandated 71,444 (19.7%) free 148,383 (40.9%) distinctive tier 219,827 (60.6%)
  [02_Spine.md:603]           names a round 3 reader who found the passage or accepted the find

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```

**Triage:** all seven are connective prose the tool captured between two adjacent quotations (legend lines L12 and L603; table cells and
prose at L33, L44, L312, L338), as its footer warns. **Confirmed defects: 0 (CELL 0, PROSE 0).**

## American English sweep and the one-location check

From the same script, raw: `02_Spine.md British-form hits: []`; `other-location name scan (names: line numbers): {'Mirny': [12, 65, 337,
413, 747]}`; `tower-name count: 0`. The hits are the parent subnet (a shared thing the city is in, `DR-136` item 3) and the pass folder's
path. **No other location named.** Real-world inspiration places are referred to by role (Q-42).

## Tokens (from the task notifications; full rows in `Universal_Location_Methodology/TOKEN_LOG_Ariun_Nuur.md`)

| Agent | Round 1 | Repair (delta) | Round 3 (delta) | Last figure |
|---|--:|--:|--:|--:|
| reader A | 413,014 | — | 99,602 | 512,616 |
| reader B | 396,144 | 1,864 | 97,573 | 495,581 |
| reader C | 405,510 | — | 82,765 | 488,275 |
| merge writer | — | — | — | 324,562 |
| **Unit total (sum of last figures)** | | | | **1,821,034** |

Web calls: readers 0; `Tools/web_quota_count.py`: WebSearch: 0 | WebFetch: 0 | TOTAL: 0
**The record grows after this check** (T8 line 8): no DOUBLE-CHECK script was run on this record.
