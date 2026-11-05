# Mirny · Amendment re-derivation · Piece PRT (the robot term, `DR-97`; Phases 4 and 7) · T8 round record · 2026-11-04

**Companion to** `Amendment_Rederivation_PRT_RobotTerm_2026-11-04.md`. Raw tool output is pasted, not summarized. Working files are in this folder as `.t8_amend_PRT_*`.

## Setup
- **Reading list (trimmed, `DR-74`):** `.t8_required_amend_PRT.txt`, 17 entries, about 3,367 admitted lines (the rules; the rulings log at twelve headings; the Division of Industry README; file `09` at Mirny's row and its margin and robot-industries passages; file `16` at its header, formula and results block, the Half B header, **Mirny's own row only** and **Mirny's own section 20**; the robot-term log at its formula bullet and Mirny's rows only; Phase 4 and Phase 7 whole; the Phase 7 wind piece; the first 60 lines of the Phase 2 piece; the first 20 of the Idelsk-Uralia piece; the amendment register; the reconciliation note's lines 1 to 103). The Division of Industry's comparison passages (cross-city tables, rankings, national spreads) were left off the list on purpose (law of one location).
- **Brief:** `.t8_amend_PRT_brief.md`, identical for A/B/C (sha256[:16] f26c2c909042a363), final at dispatch (`M-93`); nine orchestrator-verified results with sources; the developer's binding words; fourteen traps.
- **Readers:** three Opus general-purpose agents, dispatched about 07:25 on 2026-11-04, inside the 05:00 to 14:59 window. A `a8d9a47acf971b304` (699 lines, 17 PROOF blocks, about 127 tool uses) · B `a426cd862ec2938cc` (691 lines, about 95) · C `adcbca9fad038f59d` (657 lines, about 122). None refused any entry; no graphify notice appeared. A's and C's read-only self-checks of PROOF fields and quotations passed before handback.
- **No ruling was appended** to `DEVELOPER_RULINGS_LOG.md` or any list file while the round was open (M-302).

## Round 1 headline claims (union, before Round 3)
| Claim | A | B | C |
|---|---|---|---|
| Formula has a third, robot-keyed term (live) | ART-1 | ART-1 | ART-1 |
| Free tier: determined 34.7 % (366,502), not an upper bound; estimated rates and the uplift remain | ART-2 | ART-3 | ART-2 |
| The old P7-9 bracket was wrong in method (60 % not 100 % of the term leaves the free tier) | ART-5 | ART-8 | ART-3 |
| Site's price 43,367 units, 4.10 % of workforce, 9.72 % of baseline | ART-3 | ART-4 | ART-4 |
| Section 20 governs, now by ruling (`DR-56`) | ART-4 | ART-6 | ART-5 |
| 76.4 % becomes 76.9 % | ART-6 | ART-7 | ART-8 |
| RF-6 and snag 8 (robot half) close | CLOSE | CLOSE | CLOSE |
| Axes of Phases 4 and 7 | unchanged | unchanged | unchanged |
| P4 L92 "free tier can contain the headline function" | RE-DERIVE (class C) | KEEP | REWORD (pointer) |
| P4 L269 byproduct "itemizes one body's feeding" | RE-DERIVE | RE-DERIVE | CLOSE |
| Findings | ART-1 to ART-9 | ART-1 to ART-11 | ART-1 to ART-11 |

## Round 2 (`Tools/triple_read_verify.py`) · run 2026-11-04 07:58 · UNANIMOUS on the first run (51 of 51 field sets)
raw output (full; file `.t8_amend_PRT_round2_raw.txt`):
```
required files: 17
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 82-272] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 203-251,463-475,510-524,1111-1133,1211-1226,1335-1342,1404-1412,1460-1468,1523-1530,1570-1577,1628-1636,1638-1644] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00b_General_Population_Discipline.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00d_Shadow_Proportion_Discipline.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md  [range 1-120,177-190,329-438] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/README.md  [range 1-87] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/09_Per_City_Baseline_Run.md  [range 1-11,71,126-143,188-195] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/16_Per_City_Three_Tier_Run.md  [range 1-12,109-150,247,276,2110-2180] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Robot_Term_Added_To_16_Before_After_2026-11-03.md  [range 1-7,17-18,38,76-77,105] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_04_Ordinary_Life.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_07_Order.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P07_Order_2026-10-29.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P2c_Composition_2026-11-03.md  [range 1-60] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_PIU_IdelskUralia_2026-11-04.md  [range 1-20] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/DR-56_Amendment_Register_2026-10-13.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Notes_2026-11-03_Culture_File_and_Composition_Reconciliation.md  [range 1-103] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

## Round 3 (SendMessage to the same three agents) · 2026-11-04 · cross-check done
Each reader was sent the two split items (S1: P4 L92 proposed REWORD; S2: P4 L269 proposed RE-DERIVE), the other readers' single-finder items (to confirm against the pass line or by recomputing the arithmetic) and a request to list any claim in the other two re-derivations it would not accept. Replies are saved as `.t8_amend_PRT_round3_reader{A,B,C}.md`.

| Reader | Part 1 OBJECTs | Part 2 OBJECTs | Part 3 claims not accepted |
|---|---|---|---|
| A | 0 (S1 agreed with a wording condition) | 0 | 9 (6 in B, 3 in C) |
| B | 0 | 1 (C's AQ-50 cites a line that carries a national range; re-ground it) | 8 |
| C | 0 | 0 | 10 (5 in A, 5 in B) |

### How each correction was carried into the merge
| Objection | Settlement |
|---|---|
| **Food counts** re-sized in A's ART-3, ART-7, ART-9 and C's ART-4, ART-11 (104,552 and 20,910) | **Removed.** Food is carved out; Phase 4's food lines keep their numbers; only the denominator moves |
| **40/60 split stated as fact about the world** (A, in the body; B's and C's own "nation shares the price") | **Stated in model terms**: the free tier is 26,020 units and the mandated tier 17,347 units smaller at D = 1.25 than at D = 1.00; the reading stays RF-PRT-1 |
| **Sets mixed in a finding**: A's 41.10 to 42.21 rise in ART-1's third order | **Moved to a labeled bridge aside** in ART-1 |
| **B3 and "hours"**: B's "hours spent keeping the majority running", "every day of the year" | **Removed**; "a part of the units spoken for is work for the majority body" |
| **D read as the wind**; "the single largest adjustment" (C) | **Removed**; "the site's difficulty (D = 1.25)"; no ranking |
| **"care of humans"** in B's price sentence | **Corrected**: D reaches the human-keyed food term and the resident-keyed term; the 85.6 constant carries no D |
| **A line naming other places and a national gradient** (B's use of the robot file's freedom-gradient line) | **Dropped**; the third order keeps the leisure-as-a-fact-of-life passages that name no other place |
| **C's citation of a national-range line for "the residue"** (A, B) | **Re-grounded** on P4 L149 and the passages without a national range (ART-10) |
| **"than Phase 4 wrote" beside live 34.7 %** (C on B) | **Dropped**: the exact quarter is stated within the live set only |
| **A's "no line places the ring's keepers"** (C) | **Corrected**: Phase 7 places them in the baseline (P7 L190, [D]) |
| **A's "both" for who does robot-keyed work; "entered"** (C) | **Corrected**: "workers of either body"; "seen, handled" |
| **B's training-fuse size (8,882 units)** (A) | **Dropped** (assigns the units beyond the admitted lines); left at AQ-49 |
| **C's numeric slip** ("one and three-quarter points"; the model split is 1.64) | **Corrected** |
| **C's "first Mirny line a reader meets"** (A) | **Dropped / conditional** |
| **P4 L92 (S1)** | **REWORD**: the finding stands; the sector-level clause is added (not caused by the robot term); DR-59 leaves the essential tier open; Phase 7 places the ring's keepers in the baseline |
| **P4 L269 (S2)** | **RE-DERIVE**, withdrawn as a byproduct; the model property reserved (RF-PRT-2) |
| **Single-finder items** | All confirmed with limits: A's band 33.6 to 35.7 % (held by A and B); B's hypothetical of 2,798 units and 364,823 (34.51 %); B's 19-of-22 inference as a count only; B's `09` L71 reproduction; C's mortuary inference as reserved only; C's AQ-50 re-grounded; AQ-53 asked rather than recommended |
| **Clarifications** | B withdrew a part of its AQ-49 (Phase 7 already treats B3 and the robot-care posts as one row); numbering of requests merged (AR-55 to AR-59, AQ-49 to AQ-54) |

## Merge notes
- Union applied: A (the band, the model-split arithmetic, RF-PRT-1/3, ART-8's sector-level clause, the re-cite proposal), B (the hypothetical D on the robot term, the 19-of-22 inference, the stale-status and re-anchor dockets), C (the Q-43 two-quantity restatement, the mortuary-constant inference as reserved only, the register question, the as-written/live set discipline).
- All three readers agreed on the figures: 446,228 / 244,334 / 366,502; 11,192; 43,367; 76.9 %; the bracket error; the axes.
- The 23.1 / 34.7 shares are shares of workforce units, never counts of people (`DR-4`).

## Quotation audit (`Tools/quotation_audit.py`, `--own-pass`) · 2026-11-04
raw output (excerpted: the positive-control block is omitted; 12 lines omitted):
```
=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 5
NOT FOUND in corpus: 4
  of those, in TABLE CELLS : 0
  of those, in PROSE       : 4

  [Amendment_Rederivation_PRT_RobotTerm_2026-11-04.md:122]           it names the omission itself (half b mandated only the arcanet 20 %); it records developer ruling c; the developer adopted q-64's 
  [Amendment_Rederivation_PRT_RobotTerm_2026-11-04.md:156]           is the residue after baseline (the distinctive tier: 57.8 % at mirny ), and the
  [Amendment_Rederivation_PRT_RobotTerm_2026-11-04.md:223]           removed; the as-written and live sets not mixed (the bridge is a labeled aside in art-1)
  [Amendment_Rederivation_PRT_RobotTerm_2026-11-04.md:223]           dropped from the quarter claim; the ring's keepers' place (phase 7's derivation) added to art-8; the numeric slip

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```
**Triage by hand:** 5 fragments tested, 4 not found, all in prose; each is connective prose between two adjacent quotations (lines 122, 156 and 223 of the piece). Nothing is a misquotation; nothing to fix.

## American English sweep
A word-pattern sweep (-ise/-our/-re/-ence families, catalogue, grey, programme, travell/cancell) over the piece: zero hits.
