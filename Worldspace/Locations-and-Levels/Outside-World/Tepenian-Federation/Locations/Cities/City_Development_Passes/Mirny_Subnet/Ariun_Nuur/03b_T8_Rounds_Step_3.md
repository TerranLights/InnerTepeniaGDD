# Ariun Nuur — ULM Step 3 — T8 round record (research)

**Unit:** Step 3, research aimed at what Step 2 named. **Written:** `03_Research.md` (644 lines; PROPOSED, not declared complete) and the
research log's Entry 2 (`Cities/Research_Logs/Ariun_Nuur_Research_Log.md`, appended; Entry 1 byte-identical). **Run mode:** WARM (`DR-6`).
**Date:** 2026-11-19; brief frozen and readers dispatched 06:25, Round 1 back by 06:53, repairs and Round 2 run 2 by 06:56, Round 3 by
07:00, merge returned 07:35, record 07:38.
**List:** `.t8_required_03_Step3.txt` (14 entries): the Pre-Trip's Step 3 reads (runbook L2569–2661; the spine; the research-log README;
R1, R2) plus `02` §4.2 (the Unrecognized Instrument, Step 3.6), the earlier steps' outputs, the spec, the Step 3 datasheet, the picks, this
city's research log and `DR-143`. **Brief:** `.t8_brief_03_Step3.md` (219 lines; sha256[:16] a6f2e249b680ba0b). **Web cap 150 per reader.**
**Orchestrator rule for this unit:** no Antarctic station or place other than the real Vostok Station and Lake Vostok researched by name.
Reader outputs archived here as `.t8_Step3_reader{A,B,C}.md` (A's and C's first versions as `…_prerepair.md`); Round 3 replies saved on
arrival as `.t8_Step3_round3_reader{A,B,C}.md`. Three Opus readers; one fresh Opus merge writer (`M-246`).

## Round 1 — receipts (as returned)

| Reader | Output lines | Targets | Web calls (search · fetch) | Facts | Findings | Convergences | Dead ends | Open threads | RF · REQ · Q | Handoff places | Manifest |
|---|--:|--:|---|--:|--:|--:|--:|--:|---|--:|---|
| A | 515 | 20 | 73 (55 · 18) | 59 | 28 + 2 UI | 3 | 12 | 14 | 6 · 3 · 3 | 30 | 14 of 14 |
| B | 647 | 20 | 95 (72 · 23) | 69 | 30 | 3 (+2 candidates) | 26 | 17 | 10 · 7 · 7 | 46 | 14 of 14 |
| C | 539 | 26 | 88 (63 · 25) | 42 | 41 | 6 | 23 | 12 | 12 · 7 · 10 | 52 | 14 of 14 |

**The session's web count** (`Tools/web_quota_count.py`) after Round 1: WebSearch 215 · WebFetch 68 · TOTAL 283; after Round 3: WebSearch
215 · WebFetch 69 · TOTAL 284 (readers' own counts 256; the tool reads about 11% higher). **716 calls left.**

## Round 2 — `Tools/triple_read_verify.py` (last commit `8777bb5f` 2026-11-03; clean)

**Run 1, raw output whole — NOT UNANIMOUS:**

```
required files: 14
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2569-2661] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/02_Generators_Capability_and_Symbols.md  [range 557-570] ===
  agent1   ⛔ LLAST MISMATCH  claimed='---'  actual=''
  agent2   ✅ all fields match ground truth
  agent3   ⛔ LLAST MISMATCH  claimed='---'  actual=''

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/01_Inherited.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00_Frame.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.1_Step_MINUS-1_Input_Contract.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Ariun_Nuur.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/Datasheets/Step_3.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Inspirational-Influences.md  [range 92-95] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/README.md  [range 1-57,59-121] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Ariun_Nuur_Research_Log.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 2058-2065] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
⛔ NOT UNANIMOUS - DO NOT WRITE. Log which agent/file failed and why.
```

**What failed, confirmed at source:** readers A and C gave `02` L570 (blank) as the line above it (L569, `---`). First versions kept; each
corrected that one field (diffs: one line each, A L418, C L441).

**Run 2, raw output whole — UNANIMOUS:**

```
required files: 14
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2569-2661] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/02_Generators_Capability_and_Symbols.md  [range 557-570] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/01_Inherited.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00_Frame.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.1_Step_MINUS-1_Input_Contract.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Ariun_Nuur.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/Datasheets/Step_3.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Inspirational-Influences.md  [range 92-95] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/README.md  [range 1-57,59-121] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Ariun_Nuur_Research_Log.md ===
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

**All six CONSISTENT.** Readers could re-open at most 8 of the others' URLs; one fetch was used (A). Round 3 found the station-rule slips
below, two arithmetic slips (B's slope; B's list of months with record lows below −80 °C) and C's August daylight rounding; the merge wrote
the corrected forms. The (c) points became Q-54 to Q-68 of `03_Research.md`, filed as `DEC-735` to `DEC-749`.

## Procedural events (the recording law)

1. **The brief's defect (orchestrator's):** the industry-figures rule, copied from Step 2's brief, pointed at "entry 11" and "entry 8",
   which on Step 3's list are other files. Raised by all three readers; each quoted the spine instead. Fixed in the phase-brief template
   before any phase brief was frozen.
2. **Station-rule slips, raised in Round 3:** facts from accounts of a traverse that starts at another named station (A's F22–F24; the
   "a third of the towed fuel" figure in A's and C's files) and A's aircraft limit from a source about another station. **The merge
   dropped all seven** into its "Not used (another location)" table, naming no station. C's call 42 search string named another station;
   C redacted it in its own log and used nothing (Q-68). URLs whose host or path carries another location's name are kept as written
   (startup file §3); whether that counts as naming is Q-64.
3. **Commands:** reader A ran `pdftotext`, one `grep -o` and `python3 -I -c` on downloaded web-PDF text (no listed file) and `wc -l` on its own
   output; reader B ran `wc -l` on its own output and, in Round 3, one `sed -n` on the other readers' files; reader C viewed a fetched PDF
   with Read only. All self-reported; no content effect.
4. **The tower's name:** 0 in every output and in the merge.
5. **The merge writer** created no other file, made no web call, and opened the spine at several spans and the Step 3 datasheet whole,
   both on its list, to settle the sweep's line cites and the asymmetry rows.

## Quotation checks, before this record existed

**Pre-check (T8 line 13), per quotation, normalized,** against the 14 list files and the brief. First run, raw:

```
quoted strings checked: 24 not found: 14
  MISS: nine months of the year Vostok station operates in full autonomy, without any possibility to access it either by air or land
  MISS: practically snow-covered by now
  MISS: water is an expensive commodity at a polar station
  MISS: Because the whole system is circulated, if you get a large break that you could freeze up sections and lose more pipe than you wanted to
  MISS: until it finds a way to lower power costs
  MISS: electricity in the Arctic is very expensive
  MISS: We do not want to be flying in anything that we can be sending in by ship.
  MISS: shared mealtimes, and strict sleep-wake and working schedules
  MISS: Plan a minimum of 6 hours rest per 24hrs
  MISS: Plan for a max of 5 night shifts in a row
  MISS: Diamond may intervene to stop beamtime until adequate rest has been taken
  MISS: two or more infrastructures are interdependent if they require each other's services
  MISS: The electrical power system depends on the delivery of fuels ... the production of those fuels depends in turn on the use of electrical power
  MISS: are under a thick layer of snow and are gradually falling into disrepair
03_Research.md British-form hits: [(117, 'cancelled'), (117, 'cancelled')]
other-location name scan (names: line numbers): {'Mirny': [13, 81, 631]}
tower-name count: 0
```

**Triage:** all 14 misses are quotations of **web sources**, which the list-file corpus cannot contain. A second check matched each one,
word for word, to the source text the readers logged from those sources (`IN READERS` for all 14); Round 3 re-checked one at its source.
**Not defects.** The British-form hit at L117 was in prose (the British spelling of *canceled*) and is corrected; the remaining hit is
inside a URL, which keeps its own spelling. After the fix, raw:

```
quoted strings checked: 24 not found: 14
  MISS: nine months of the year Vostok station operates in full autonomy, without any possibility to access it either by air or land
  MISS: practically snow-covered by now
  MISS: water is an expensive commodity at a polar station
  MISS: Because the whole system is circulated, if you get a large break that you could freeze up sections and lose more pipe than you wanted to
  MISS: until it finds a way to lower power costs
  MISS: electricity in the Arctic is very expensive
  MISS: We do not want to be flying in anything that we can be sending in by ship.
  MISS: shared mealtimes, and strict sleep-wake and working schedules
  MISS: Plan a minimum of 6 hours rest per 24hrs
  MISS: Plan for a max of 5 night shifts in a row
  MISS: Diamond may intervene to stop beamtime until adequate rest has been taken
  MISS: two or more infrastructures are interdependent if they require each other's services
  MISS: The electrical power system depends on the delivery of fuels ... the production of those fuels depends in turn on the use of electrical power
  MISS: are under a thick layer of snow and are gradually falling into disrepair
03_Research.md British-form hits: [(117, 'cancelled')]
other-location name scan (names: line numbers): {'Mirny': [13, 81, 631]}
tower-name count: 0
```

**`Tools/quotation_audit.py`** (last commit `5a63e074` 2026-11-02; clean), `--step 3 --own-pass`. Whole output saved beside this record as
`.t8_Step3_quotation_audit.txt`; result block, raw:

```
=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 12
NOT FOUND in corpus: 12
  of those, in TABLE CELLS : 10
  of those, in PROSE       : 2

  [03_Research.md:13]           are this pass's step -1, step 0, step 1 and step 2 files
  [03_Research.md:13]           is the published climate table for the real station (an encyclopedia weatherbox citing the station's operator and a weather archiv
  [03_Research.md:104]  [CELL]  nine months of the year vostok station operates in full autonomy, without any possibility to access it either by air or land
  [03_Research.md:108]  [CELL]  water is an expensive commodity at a polar station
  [03_Research.md:111]  [CELL]  because the whole system is circulated, if you get a large break that you could freeze up sections and lose more pipe than you wan
  [03_Research.md:117]  [CELL]  we do not want to be flying in anything that we can be sending in by ship
  [03_Research.md:130]  [CELL]  shared mealtimes, and strict sleep-wake and working schedules
  [03_Research.md:136]  [CELL]  diamond may intervene to stop beamtime until adequate rest has been taken
  [03_Research.md:176]  [CELL]  two or more infrastructures are interdependent if they require each other's services
  [03_Research.md:176]  [CELL]  the electrical power system depends on the delivery of fuels
  [03_Research.md:176]  [CELL]  the production of those fuels depends in turn on the use of electrical power
  [03_Research.md:177]  [CELL]  are under a thick layer of snow and are gradually falling into disrepair

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```

**Triage:** ten are the same web-source quotations (all matched to the readers' logged source text, above); two are the legend line at
L13. **Confirmed defects: 0 (CELL 0, PROSE 0).**

## American English sweep and the one-location check

From the same script: the only British form left is inside a URL (`globalnews.ca/…/arctic-barge-cancelled-supplies`), kept. The research
log's new entry had three more, all corrected (a source note *barge canceled*; the place name *Coral Harbor*; a source quotation in British
spelling, rewritten unquoted with *among*). Name scan of `03_Research.md`, raw: `other-location name scan (names: line numbers):
{'Mirny': [13, 81, 631]}`, `tower-name count: 0`; the hits are the parent subnet and the pass folder's path. A second scan for Antarctic
station names (a list of about forty) found none in the file. **No other location named.**

## Tokens (from the task notifications; full rows in `Universal_Location_Methodology/TOKEN_LOG_Ariun_Nuur.md`)

| Agent | Round 1 | Repair (delta) | Round 3 (delta) | Last figure |
|---|--:|--:|--:|--:|
| reader A | 499,138 | 279 | 93,143 | 592,560 |
| reader B | 564,652 | — | 91,993 | 656,645 |
| reader C | 539,640 | 332 | 103,619 | 643,591 |
| merge writer | — | — | — | 358,608 |
| **Unit total (sum of last figures)** | | | | **2,251,404** |

Web calls: readers 256 (A 73 · B 95 · C 88); `Tools/web_quota_count.py`: WebSearch: 215 | WebFetch: 69 | TOTAL: 284
**The record grows after this check** (T8 line 8): no DOUBLE-CHECK script was run on this record.
