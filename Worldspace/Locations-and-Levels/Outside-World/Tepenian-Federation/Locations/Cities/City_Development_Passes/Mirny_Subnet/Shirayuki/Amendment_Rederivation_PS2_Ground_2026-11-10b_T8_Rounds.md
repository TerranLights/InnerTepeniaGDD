# Shirayuki: T8 round record for PS2_Ground (the free-tier hedge, the difficulty coefficient and the rock), 2026-11-10

**What this is.** The record of the three-reader rounds behind `Amendment_Rederivation_PS2_Ground_2026-11-10.md` (the piece; 1060 lines, `sha256` `8ad7df0b78674d44`). It states what each tool returned and where each file is; it does not restate the piece. **Everything here is PROPOSED;** no pass file was edited. The run's log is `Amendment_Log_2026-11-10.md`.

**Items re-derived:** `SRY-C06`, `SRY-C07` (the note's section J gives each first-check verdict). **Pass places:** `02_Spine.md` L57–L83 (§2b), L229–L286 (§6, §6a, §7); `04_Phase_04_Ordinary_Life.md` L41–L66 (§2, §2a), L255–L292; `00_Frame.md` L205–L241 (§3, §3b), L286–L298 (§6), L360–L377 (§10); `04_Phase_03_Surface_and_Texture.md` L200–L220; `04_Phase_07_Order.md` L96–L135 (§7b), L275–L291; `04_Phase_09_Populations.md` L189–L220 (§E), L330–L345; `05_Reconciliation.md` L285–L315 (the strongest-finding check); `10_Readiness_Check.md` L250–L258.

## Round 0: the list and the briefs

The three readers' lists are identical (`cmp`). The list (15 entries), as dispatched:

```
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/Amendment_Notes_2026-11-10_Cross_Check.md :: 1-22,29-34,296-302,24-61,127-144,168-185,281-294,308,309
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/02_Spine.md :: 57-83,229-286
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_04_Ordinary_Life.md :: 41-66,255-292
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/00_Frame.md :: 205-241,286-298,360-377
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_03_Surface_and_Texture.md :: 200-220
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_07_Order.md :: 96-135,275-291
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_09_Populations.md :: 189-220,330-345
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/05_Reconciliation.md :: 285-315
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/10_Readiness_Check.md :: 250-258
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/16_Per_City_Three_Tier_Run.md :: 1,247,277,1754-1769
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/09_Per_City_Baseline_Run.md :: 78,126-146,216
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Canon_Gap_Resolution_Method/Developer_Ruling_Queue.md :: 579-612,656-695
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md :: 1638-1645,1711-1712
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C06.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C07.md
```

Brief template `scratchpad/sry/tools/t8_template.md`; the three briefs differ only in reader letter, private staging folder and number range (A 1–99, B 101–199, C 201–299). Brief `sha256` A `bdd9d97b82be81bc`, B `df4ecb37a6d0b0ef`, C `5a19fb6bcf348c01`. Before dispatch every brief's cited lines were checked against its list (`check_brief_vs_list` adapted for pieces; positive control returned two flagged ranges), and one generated brief was read end to end (log L-36). The piece's note range was out of ascending order in six of the seven pieces (log L-42).

## Round 1: three independent readers

- Reader A: `.t8_xc_PS2_Ground_readerA.md` beside the pass (334 lines now, `sha256` `db589535b25d497c`).
- Reader B: `.t8_xc_PS2_Ground_readerB.md` beside the pass (676 lines now, `sha256` `69560d033ab1e885`).
- Reader C: `.t8_xc_PS2_Ground_readerC.md` beside the pass (439 lines now, `sha256` `f63a4180b361e287`).

## Round 2: the mechanical check

Tool: `Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/triple_read_verify.py` (last committed 2026-11-03; no uncommitted edits).

**round2_run1.txt** (raw output, whole; also beside the pass as `.t8_xc_PS2_Ground_round2_run1.txt`):

```
required files: 15
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/Amendment_Notes_2026-11-10_Cross_Check.md  [range 1-22,29-34,296-302,24-61,127-144,168-185,281-294,308,309] ===
  agent1   ⛔ LINES MISMATCH  claimed=[REDACTED - found at L201, outside the admissible range, sha1:0ca9277f91e4]  actual='119'
  agent1   ⛔ LMID  MISMATCH  claimed="- **Band.** Census I governs a city's band (`DR-4` 4.1, `LOG"  actual='---'
  agent2   ⛔ LINES MISMATCH  claimed=[REDACTED - found at L201, outside the admissible range, sha1:0ca9277f91e4]  actual='119'
  agent2   ⛔ LMID  MISMATCH  claimed="- **Band.** Census I governs a city's band (`DR-4` 4.1, `LOG"  actual='---'
  agent3   ⛔ LINES MISMATCH  claimed=[REDACTED - found at L201, outside the admissible range, sha1:0ca9277f91e4]  actual='119'
  agent3   ⛔ LMID  MISMATCH  claimed="- **Band.** Census I governs a city's band (`DR-4` 4.1, `LOG"  actual='---'

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/02_Spine.md  [range 57-83,229-286] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_04_Ordinary_Life.md  [range 41-66,255-292] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/00_Frame.md  [range 205-241,286-298,360-377] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_03_Surface_and_Texture.md  [range 200-220] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_07_Order.md  [range 96-135,275-291] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_09_Populations.md  [range 189-220,330-345] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/05_Reconciliation.md  [range 285-315] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/10_Readiness_Check.md  [range 250-258] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/16_Per_City_Three_Tier_Run.md  [range 1,247,277,1754-1769] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/09_Per_City_Baseline_Run.md  [range 78,126-146,216] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Canon_Gap_Resolution_Method/Developer_Ruling_Queue.md  [range 579-612,656-695] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 1638-1645,1711-1712] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C06.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C07.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
⛔ NOT UNANIMOUS - DO NOT WRITE. Log which agent/file failed and why.
```

**round2_run2.txt** (raw output, whole; also beside the pass as `.t8_xc_PS2_Ground_round2_run2.txt`):

```
required files: 15
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/Amendment_Notes_2026-11-10_Cross_Check.md  [range 1-22,29-34,296-302,24-61,127-144,168-185,281-294,308,309] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/02_Spine.md  [range 57-83,229-286] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_04_Ordinary_Life.md  [range 41-66,255-292] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/00_Frame.md  [range 205-241,286-298,360-377] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_03_Surface_and_Texture.md  [range 200-220] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_07_Order.md  [range 96-135,275-291] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/04_Phase_09_Populations.md  [range 189-220,330-345] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/05_Reconciliation.md  [range 285-315] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/10_Readiness_Check.md  [range 250-258] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/16_Per_City_Three_Tier_Run.md  [range 1,247,277,1754-1769] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/09_Per_City_Baseline_Run.md  [range 78,126-146,216] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Canon_Gap_Resolution_Method/Developer_Ruling_Queue.md  [range 579-612,656-695] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 1638-1645,1711-1712] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C06.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C07.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

Between the runs, each failing reader repaired its own failed field(s) by hand under `DR-117` item 2; each reader's reading log carries a "Round 2 repair:" line with the old and new value; a `diff` against a pre-repair copy showed only those fields and the repair lines changed (log L-42 onward). Cause: the orchestrator's out-of-order range string.

## Round 3: the cross-check (each reader continued by SendMessage with the other two outputs)

The verdict lines, as `grep` returns them from each reply (each reply also beside the pass as `.t8_xc_PS2_Ground_round3_reader<X>.md`):

```
reader A L12: - **PS2_Ground-A-R3-4. (4) Verdict on B: CONSISTENT.** Every quotation and figure I checked against my own admitted lines matches, and B's decisions r
reader A L28: - **PS2_Ground-A-R3-17. (4) Verdict on C: CONSISTENT.** Every quotation and figure I checked matches my admitted lines, and C flags plainly the two pl
reader B L27: **PS2_Ground-B-R3-4. (4) Verdict on reader A: CONSISTENT.** Every passage-dependent claim I checked is in lines we both read, except one line count I 
reader B L85: **PS2_Ground-B-R3-10. (4) Verdict on reader C: CONSISTENT.** Every passage-dependent claim I checked is in lines we both read, and the only discrepanc
reader C L26: **PS2_Ground-C-R3-4. Verdict on A: CONSISTENT.** Every figure and quotation I checked matches the lines I read, and A's dispositions differ from mine 
reader C L60: **PS2_Ground-C-R3-10. Verdict on B: CONSISTENT.** Every figure and quotation I checked matches the lines I read. B's differences from me are scope and
```

## The merge

One merge writer (fresh; not a reader) on `scratchpad/sry/pieces/PS2_Ground/M/brief.md` (template `merge_template.md`; `sha256` `e152c9d486258a7c`), merge rule `M-246` as `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` §N.2 and the runbook state it. Its return, as given: `Section 3, 123 rows: written (union) 78 · written (conservative) 20 · demoted 0 · question 11 · not written 14`

## Merge checks (run before this record existed)

**1 · Normalized quotation pre-check** (`scratchpad/sry/tools/quote_precheck.py`; corpus: the list's sources whole, the pass's numbered files and amendment notes, the readers' outputs, Round 3 replies and item verdicts). Raw output, whole:

```
quoted strings checked: 185; found: 185; not found: 0
```

**2 · Quotation audit** (`python3 Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/quotation_audit.py "<pass folder>" --files <piece> --own-pass`, from the repo root; tool last committed 2026-11-02). Raw output, excerpted (3 miss lines omitted, kept whole in `.t8_xc_PS2_Ground_quotation_audit.txt` beside the pass):

```
pass audited : Shirayuki
corpus mode  : default (own pass excluded)
corpus files : 6812   chars: 105,888,057
files audited: Amendment_Rederivation_PS2_Ground_2026-11-10.md
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
fragments tested (single-line, ellipsis-split, >=7 words): 99
NOT FOUND in corpus: 3
  of those, in TABLE CELLS : 0
  of those, in PROSE       : 3


⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```

**2b · Triage of the audit's misses** (`scratchpad/sry/tools/audit_triage.py`; the audit reads no dot-file and its fragmenter captures text between two quotations). Raw output, whole:

```
audit NOT FOUND fragments: 3; (a) found in other inputs: 0; (b) piece's own unquoted prose: 3; (c) for hand triage: 0
```

Hand triage of class (c): no fragment reached class (c). Confirmed defects: 0 (CELL 0, PROSE 0).

**3 · American English sweep** (pattern of British forms; only "judgement" is kept). Raw output: none (0 hits).

**4 · Other locations' names and status words** (`grep` for 46 location names and aliases; and for complete/completed/ready). Raw output: names none; status words none.

*Record written 2026-11-10 06:32 by script from the files named above; the record grows after no check (the checks ran on the piece, not on this record).*
