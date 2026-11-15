# Round record — Casey · Step 4, Phase 7 (Order)

**Output:** `04_Phase_07_Order.md` (683 lines) and Session 5 of `Cities/Research_Logs/Casey_Research_Log.md` (appended, 163 lines; the log now 1,209 lines). Casey's warm ULM run under `STARTUP_Mirny_Review_then_Casey_ULM_2026-11-11.md` Part B item 3: three readers, Round 2, Round 3, one fresh merge writer (`M-246`), the quotation audit run before this record existed, the American English sweep, the handoff audit and the phase discipline check. Every tool output below is pasted whole. PROPOSED; nothing declared complete.

## Round 0 — the reading list and the frozen briefs

Briefs `.t8_04_Phase_7_brief_A.md`, `_B.md`, `_C.md` (171 lines each; written new for Casey from the runbook, the spine and the Phase 2 brief on disk; standing lines 1–6, 10, 11 verbatim; A and B differ only in the slot, checked by `diff`; two pre-dispatch corrections made to all three alike, logged in the progress file). Merge brief `.t8_04_Phase_7_merge_brief.md`. List decisions: Casey's log CL-33. The list, `.t8_required_04_Phase_7.txt` (18 entries):

```
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md :: 82-272,841-951
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md :: 378-426,1598-1636,1670-1736,1966-2041,2071-2072,2645-2758
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/README.md :: 1-34,40,42-60
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/16_Per_City_Three_Tier_Run.md :: 241-248,267,340-346,358-360,2181-2187,2192-2195
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/09_Per_City_Baseline_Run.md :: 2-53,87,126-132,135-136,141-142,188-197,212
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/11_Caloric_Rebuild_and_Livestock_Tier.md :: 1-21,316,326-327,333
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/08_Volume_Based_Requirement_Reference.md :: 1-8,33-69,378-445,547-560,646-653
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry_Sweep_2026-08-31.md :: 1-12,132-140,163
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/National_Medical_and_Care_Institutes.md :: 1-15,17-22,25-28,151-167,193-202,216-222,226-230,237-245
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/National_Economy_and_Currency.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/City_Logistics.md :: 1-3,213,217-224
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Industry_Staffing_and_Productivity/README.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/jobs_professions_and_fields/SOC_Table_of_Contents.md
/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Megacorps/README.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md :: 991-994
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00b_General_Population_Discipline.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00d_Shadow_Proportion_Discipline.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Casey.md :: 1-3,5-83,85,87-93,95-107,110,112-121,125-152,154-155,157-159,166-170,172,174-180,182,184,186,188-200,202,204-207,212-214,243-244,248-249
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/00.1_Step_MINUS-1_Input_Contract.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/00.1_Step_MINUS-1_Amendment_2026-11-11.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/00_Frame.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/01_Inherited.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/02_Spine.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/03_Research.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_02_Composition_and_Arrival.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_03_Surface_and_Texture.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_04_Ordinary_Life.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_05_Relation_and_Geometry.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_06_Meaning.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/Datasheets/Phase_7.md :: 1-54,56,62-66,68-69
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md :: 170-202,1707-1715,1944-1951,1989-1996
```

## Round 1 — three readers, each in a private staging folder

Dispatched 2026-11-15 09:02, three Opus readers, one message: A `ad3f5d05c58a6e0d5`, B `a5e5e4bbefead8426`, C `a86bb476b590cc944`; staging `scratchpad/casey/phase7/reader<X>/`. Outputs copied into Casey's folder after Round 2 (standing line 9).

| Reader | Output | Lines | Findings | Handed forward | Developer questions | Web calls |
|---|---|--:|--:|--:|--:|--:|
| A | `.t8_04_Phase_7_readerA.md` | 782 | 28 | 13 | 1 | 15 (5 searches, 10 fetches) |
| B | `.t8_04_Phase_7_readerB.md` | 705 | 28 | 12 | 2 | 8 (6 searches, 2 fetches) |
| C | `.t8_04_Phase_7_readerC.md` | 749 | 31 | 12 | 2 | 15 (7 searches, 8 fetches) |

*The counts are as each reader reported them in its reply; the line counts are `wc -l` on the copied files.*

## Round 2 — `Tools/triple_read_verify.py` (last change 2026-11-03), raw output, whole (165 lines; `.t8_04_Phase_7_round2_raw.txt`)

```
required files: 32
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 82-272,841-951] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 378-426,1598-1636,1670-1736,1966-2041,2071-2072,2645-2758] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/README.md  [range 1-34,40,42-60] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/16_Per_City_Three_Tier_Run.md  [range 241-248,267,340-346,358-360,2181-2187,2192-2195] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/09_Per_City_Baseline_Run.md  [range 2-53,87,126-132,135-136,141-142,188-197,212] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/11_Caloric_Rebuild_and_Livestock_Tier.md  [range 1-21,316,326-327,333] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/08_Volume_Based_Requirement_Reference.md  [range 1-8,33-69,378-445,547-560,646-653] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry_Sweep_2026-08-31.md  [range 1-12,132-140,163] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/National_Medical_and_Care_Institutes.md  [range 1-15,17-22,25-28,151-167,193-202,216-222,226-230,237-245] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/National_Economy_and_Currency.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/City_Logistics.md  [range 1-3,213,217-224] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Industry_Staffing_and_Productivity/README.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/jobs_professions_and_fields/SOC_Table_of_Contents.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Megacorps/README.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md  [range 991-994] ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Casey.md  [range 1-3,5-83,85,87-93,95-107,110,112-121,125-152,154-155,157-159,166-170,172,174-180,182,184,186,188-200,202,204-207,212-214,243-244,248-249] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/00.1_Step_MINUS-1_Input_Contract.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/00.1_Step_MINUS-1_Amendment_2026-11-11.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/00_Frame.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/01_Inherited.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/02_Spine.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/03_Research.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_02_Composition_and_Arrival.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_03_Surface_and_Texture.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_04_Ordinary_Life.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_05_Relation_and_Geometry.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_06_Meaning.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/Datasheets/Phase_7.md  [range 1-54,56,62-66,68-69] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 170-202,1707-1715,1944-1951,1989-1996] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

## Round 3 — each reader continued by `SendMessage` with the other two outputs

Messages built from `scratchpad/casey/tools/phase7_round3_template.txt` (sections 1–4 per reader; 5 dispositions; 6 figures recomputed; 7 T3 marks; 8 the `T4 - SHED:` line; 9 web calls, up to 15 each). Replies saved the moment each arrived (standing line 9):

| Reader | Reply | Lines | Verdict lines, as written in the reply (cut at the reason) | Web calls |
|---|---|--:|---|--:|
| A | `.t8_04_Phase_7_round3_readerA.md` | 129 | VERDICT: CONSISTENT · VERDICT: CONSISTENT | 3 |
| B | `.t8_04_Phase_7_round3_readerB.md` | 112 | 4. VERDICT: CONSISTENT — A's reading log · 4. VERDICT: CONSISTENT — C's reading log | 2 |
| C | `.t8_04_Phase_7_round3_readerC.md` | 111 | 4. VERDICT: CONSISTENT — A read the same · 4. VERDICT: CONSISTENT — B read the same | 4 |

**Verdicts: all six CONSISTENT.** Each reply carries sections 5 to 9 and one `T4 - SHED:` line (checked with `grep -c`).

## The merge — one fresh writer (`M-246`)

Dispatched after Round 3: `a8774e0e1d5b3b47f` (Opus). Returned `04_Phase_07_Order.md` (683 lines; P7-1 to P7-39; 88 inbound sweep rows; 15 HANDED FORWARD rows; DQ-23, DQ-24, DQ-25; no new request, reserved finding or provisional assumption) and Session 5 of the research log (47 call rows; OT-75 to OT-84). `git diff --numstat` on the log against the last commit: `687 0` (Sessions 2 to 5, insertions only). `git diff --numstat` on the log: `208 0` (insertions only).

## Research-log strings against the readers' own tables — `scratchpad/casey/tools/check_session5_strings.py` (written this morning), raw output, whole (2 lines; `.t8_04_Phase_7_log_strings_raw.txt`)

```
rows 47 · verbatim found 47 · missing 0
per reader/round: A-R1 15 A-R3 3 B-R1 8 B-R3 2 C-R1 15 C-R3 4
```

## Normalized quotation pre-check (standing line 13) — `scratchpad/casey/tools/quote_precheck.py` (written this morning), raw output, whole (1 lines; `.t8_04_Phase_7_quote_precheck_raw.txt`)

```
quoted strings (2+ words): 79 · found 79 · not found 0
```

## Quotation audit — `Tools/quotation_audit.py` (last change 2026-11-02), `--files 04_Phase_07_Order.md --own-pass`, raw output, whole (32 lines; `.t8_04_Phase_7_quotation_audit_raw.txt`)

```
pass audited : Casey
corpus mode  : default (own pass excluded)
corpus files : 7119   chars: 115,123,852
files audited: 04_Phase_07_Order.md
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
fragments tested (single-line, ellipsis-split, >=7 words): 49
NOT FOUND in corpus: 6
  of those, in TABLE CELLS : 0
  of those, in PROSE       : 6

  [04_Phase_07_Order.md:23]           ( 09 l5) pa-13 ; the rates and their reasoning (l12-40); the affected/immune split (l42-44); the formula (l50)
  [04_Phase_07_Order.md:194]           disruption to a construction project, not steady-state operation in a permanently hostile place
  [04_Phase_07_Order.md:236]           with distributed and localized elements (highways l15-16, as 04 phase 05 l324 quotes it), and its central administration exists bu
  [04_Phase_07_Order.md:303]           (highways l380, as 04 phase 05 l409 quotes it), a heated room before it is a social room (p5-24 2); the comparables give three for
  [04_Phase_07_Order.md:365]           (physiology l434); a built robot's start is a build and a mentor ( 04 phase 04 l215); a casey-built robot records the city's own d
  [04_Phase_07_Order.md:683]           is at frame l245 (the physiology file's version wraps across l347-348), so it is cited to the frame (p7-16); the institutes' trave

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```

**Triage of the misses** (orchestrator; table `.t8_04_Phase_7_quotation_triage.md`): 6 misses: 5 CONNECTIVE, 1 WRAP, 0 DOT, 0 SELF, **0 MISQUOTE**. The audit does not read dot-files, so quotations of the readers' outputs and replies are checked by no tool except the pre-check above.

## American English sweep — a pattern of British forms (`scratchpad/casey/tools/ame_pattern.txt`), over the phase file and the log's Session 5, raw output, whole (21 lines; `.t8_04_Phase_7_ame_sweep_raw.txt`)

```
== 04_Phase_07_Order.md
53:raised
66:Raised
67:judgement
69:Raised
72:raised
75:Raised
144:raised
224:judgement
277:judgement
371:judgement
468:supervised
510:judgement
524:raised
538:supervised
547:raised
557:raised
557:supervised
654:raised
== Casey_Research_Log.md (Session 5)
1191: Raised
```

**Hits:** "judgement" five times (the one British form the project keeps); the rest are false positives of the `-ise` pattern (raised, supervised). 0 British forms.

## Handoff audit — `Tools/handoff_audit.py` (last change 2026-10-21), raw output, whole (108 lines; `.t8_04_Phase_7_handoff_audit_raw.txt`)

```
pass audited : Casey
phase files  : 6

=== CONTROLS (edit these per pass; they are what makes a zero trustworthy) ===
  PHASES WITH A FORMAL SWEEP BLOCK (found in this pass): 2, 3, 4, 5, 6, 7
  PHASES WITH NO TRACE OF A SWEEP (found in this pass)  : none
  SELF-TEST (fixed positive and negative strings)       : passed
  INSTRUMENT VALID: YES - the detector separates a formal block from no block on the built-in controls

  phase | outbound | sweep    | rows | verdict
  ------+----------+----------+------+---------
      2 |        0 | FORMAL   |   16 | n/a - nothing addressed to it
      3 |        1 | FORMAL   |   32 | reconcile 32 enumerated against 1 outbound
      4 |        9 | FORMAL   |   44 | reconcile 44 enumerated against 9 outbound
      5 |       15 | FORMAL   |  131 | reconcile 131 enumerated against 15 outbound
      6 |        4 | FORMAL   |   28 | reconcile 28 enumerated against 4 outbound
      7 |       21 | FORMAL   |   88 | reconcile 88 enumerated against 21 outbound

TOTAL outbound handoff rows: 78
PHASES WITH ROWS ADDRESSED TO THEM AND NO ENUMERATION: 0

=== outbound rows, per target, for hand reconciliation ===
  -> Phase 3:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 3** | What of the inherited base was not carried over, whether the loss lasted
  -> Phase 4:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 4** | Whose ordinary day (spine L468): the general population is the born-here
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 4** | The research capacity of spec L195, at the step that reads V10 (`01_Inhe
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 4** | The shut half's closed population and the seasonal weight of winter skil
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 4** | S3-39 turned inward [PA-5]: the flow, travelers and crews as a possible 
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 4** | The day's physical structure for both bodies: outdoors and the heated do
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 4** | Whose ordinary day hears the season underfoot: the squeak half equals th
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 4** | For robots, a storm registered through the walls in heated rest (P3-16 →
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 4** | Questions only: calm days carry sound across frozen bays (P3-15, inferen
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 4** | REQ-32: admit split spec lines by part at the step that first uses them;
  -> Phase 5:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 5** | Who the visitor is (spine L468): the flow (travelers, convoys, ship crew
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 5** | The closing as the year's decision point for anyone at Casey by sea; att
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 5** | The instrument's later doors: electors (II.2.5), later-exiled robots (II
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 5** | First impressions of those who arrive, by sea, by road [PA-5] and for th
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 5** | The internal map that changes with the season (P3-35 →2, (c)): water div
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 5** | The decision point's danger sign: calm from the sea while cold builds on
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 5** | Signs of summer that are not access: the sea opens at the island coasts 
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 5** | The working city's ground-bound buildings and their dug-out doors, scope
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 5** | REQ-32, as for Phase 4 | sweep row 31 · P3C sweep row 20 |
       [04_Phase_04_Ordinary_Life.md]  | **Phase 5** | The held robot's and the flow's nightly heat: who gives it and on what t
       [04_Phase_04_Ordinary_Life.md]  | **Phase 5** | The internal map: whether the city's parts are joined over ice in the sh
       [04_Phase_04_Ordinary_Life.md]  | **Phase 5** | The bright-weeks rhythm: the stop at the door, the firm night hours, owe
       [04_Phase_04_Ordinary_Life.md]  | **Phase 5** | Road news as part of the resident's ordinary day [PA-5] (P4-20); the ice
       [04_Phase_04_Ordinary_Life.md]  | **Phase 5** | Care staff arriving and leaving in windows; the outbound resident who ca
       [04_Phase_04_Ordinary_Life.md]  | **Phase 5** | REQ-32: split spec lines still not admitted by part (sweep row 13) | swe
  -> Phase 6:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 6** | Necessity Before Meaning: what moral, if any, was hung on the founding w
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 6** | A warning for Phases 6 to 9: the native layer must not be written as wea
       [04_Phase_04_Ordinary_Life.md]  | **Phase 6** | Candidate sites only, nothing created (RF-7): the blizzard day as unsche
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 6** | Necessity before meaning at the edge, candidate sites only, nothing crea
  -> Phase 7:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 7** | The founding administration (II.4) and local councils (I.4): who held it
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 7** | The records' keepers: who keeps and reads them, on what terms, and wheth
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 7** | Heat and arrival: whether any rule decides who is given heated rest to w
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 7** | Who decided what of the inherited base was kept (`04_Phase_02` L486; P3-
       [04_Phase_04_Ordinary_Life.md]  | **Phase 7** | Who keeps heat, water and clearing through the shared night and on storm
       [04_Phase_04_Ordinary_Life.md]  | **Phase 7** | Who provides heated places away from home, in storms and for travelers, 
       [04_Phase_04_Ordinary_Life.md]  | **Phase 7** | Whether the hold is household-, city- or parent-run; who cannot lay in; 
       [04_Phase_04_Ordinary_Life.md]  | **Phase 7** | How a care trainee's departure and return are arranged, and how care pos
       [04_Phase_04_Ordinary_Life.md]  | **Phase 7** | Who makes the morning weather call and what closes; how schooling meets 
       [04_Phase_04_Ordinary_Life.md]  | **Phase 7** | What the free tier's 491,945 workers do (Casey's sector shares, at Step 
       [04_Phase_04_Ordinary_Life.md]  | **Phase 7** | Whether anyone protects the robot majority's leisure in the bright weeks
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 7** | Who makes the go/no-go at the decision point, under the network's local 
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 7** | Who keeps the nodes and heated waiting rooms, and on what terms a rider,
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 7** | Who lays in and who counts (membership as provisioning, conditional on t
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 7** | Who keeps the spur city's unshipped bulk goods at Casey through the shut
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 7** | Whether road traffic in the shut half draws on the sea-laid store; who d
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 7** | The internal crossings of the bays by season: who opens one, if any; nev
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 7** | Ordering the dependencies Casey cannot make: care posts across the shut 
       [04_Phase_06_Meaning.md]  | **Phase 7** | Who keeps the warm night: who provides the warm room at the day's end to
       [04_Phase_06_Meaning.md]  | **Phase 7** | Who records, if anyone: the held, the nights a robot rested cold, the de
       [04_Phase_06_Meaning.md]  | **Phase 7** | The keepers of heat as the people the promise rests on, conditional on P
  -> Phase 8:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 8** | Languages outside the supporting tier (`01_Inherited` L295; S1-14): hous
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 8** | What Casey builds with: no admitted material (P3-8); the country rock as
       [04_Phase_04_Ordinary_Life.md]  | **Phase 8** | The street shaped by wind and drift: warm stops, door-to-door routes, in
       [04_Phase_04_Ordinary_Life.md]  | **Phase 8** | Dry interiors and any remedy | P4-44 · P4A-HF-5, P4B-HF-11 |
       [04_Phase_04_Ordinary_Life.md]  | **Phase 8** | What residents make and use for the day's frame: outdoor clothing for bo
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 8** | What the nodes, the heated waiting rooms and the junction's vehicle-serv
       [04_Phase_07_Order.md]  | **Phase 8** | What is built for the order: warm stopping places, heated nodes and publ
       [04_Phase_07_Order.md]  | **Phase 8** | What Casey makes: the free tier's goods and the non-thematic export, if 
  -> Phase 9:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 9** | Which populations exist (spine L468): exile-era robots, sent and a persi
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 9** | The robot body at Casey: hearing direction (P3-16, under DQ-14); the che
       [04_Phase_04_Ordinary_Life.md]  | **Phase 9** | Whether a recharging robot perceives, and whether storm vibration touche
       [04_Phase_04_Ordinary_Life.md]  | **Phase 9** | The robot body in the cold: permanent capacity loss as individual histor
       [04_Phase_04_Ordinary_Life.md]  | **Phase 9** | Built for a need, free to leave; build weighting and build needs once se
       [04_Phase_04_Ordinary_Life.md]  | **Phase 9** | Populations: the human half outside the modeled workforce; the child and
       [04_Phase_04_Ordinary_Life.md]  | **Phase 9** | In the bright weeks, households with no held schedule: their humans drif
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 9** | The robot traveler and the held robot: nightly heat away from home as a 
       [04_Phase_06_Meaning.md]  | **Phase 9** | Memory by cohort: exile-era and founding-era robots as the city's only l
       [04_Phase_06_Meaning.md]  | **Phase 9** | The damaged, not the dead: robots whose capacity was reduced by broken n
       [04_Phase_06_Meaning.md]  | **Phase 9** | The meaning distribution as populations by position relative to the heat
       [04_Phase_06_Meaning.md]  | **Phase 9** | Whether robots feel cold (DQ-14; PA-11), on which the mild-week leg turn
       [04_Phase_07_Order.md]  | **Phase 9** | Populations by position in the order: the keepers of heat and clearing (
       [04_Phase_07_Order.md]  | **Phase 9** | The candidate dispositions, never a faction (RF-7): night-makers, teache
       [04_Phase_07_Order.md]  | **Phase 9** | Robot turnover by will, not age: what a labor order means for a body tha
       [04_Phase_07_Order.md]  | **Phase 9** | Who attends a death in the shut half and who carries word of a lost pass
  -> Phase 10:
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 10** | Naming places from what they look like: scoured crests, lee drifts, whi
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 10** | Names for the junction's legs, the turn inland, the harbor, the waiting
       [04_Phase_06_Meaning.md]  | **Phase 10** | Names of places for the warm room, the waiting room and the node, only 
       [04_Phase_07_Order.md]  | **Phase 10** | Names of places and roles the order produces (the warm stopping place, 
```

## Phase discipline check — `Tools/phase_discipline_check.py` (last change 2026-10-21), raw output, whole (38 lines; `.t8_04_Phase_7_phase_discipline_raw.txt`)

```
pass audited : Casey

=== T3 - POSITION-COVERAGE LEDGER ===
  phases in header: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Child              filled=2  blank=7   blank at: P3, P5, P6, P7, P8, P9, P10
  The Lover (position)   filled=3  blank=6   blank at: P3, P5, P7, P8, P9, P10
  The Parent             filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Ruler              filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Elder              filled=3  blank=6   blank at: P3, P5, P7, P8, P9, P10
  The Mentor             filled=1  blank=8   blank at: P3, P4, P5, P6, P7, P8, P9, P10
  The Passer-Through     filled=5  blank=4   blank at: P7, P8, P9, P10
  The Neighbor           filled=1  blank=8   blank at: P2, P3, P4, P6, P7, P8, P9, P10
  ⭐ The Lover FACULTY    filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10

  NOTE: a blank cell is a WARNING BEFORE Step 8, not a defect. Do not
  fill a blank by writing new phase content toward it - that is the
  contamination 00f Rule 3 forbids (see the recipe's hard bound on T3).

=== T4 - PER-PHASE SHED MARKER ===
  [04_Phase_02_Composition_and_Arrival.md]  T4 present: the 42 origin stocks as a sorting line: which nations are present, any row or share beyond
  [04_Phase_03_Surface_and_Texture.md]  T4 present: the 42 origin stocks and every composition share beyond the two bodies' halves, the founde
  [04_Phase_04_Ordinary_Life.md]  T4 present: the 42 origin stocks beyond the bare fact that none is the default; the founding, the arri
  [04_Phase_05_Relation_and_Geometry.md]  T4 present: the 42 origin stocks, every composition share beyond the two bodies and no majority, the f
  [04_Phase_06_Meaning.md]  T4 present: the 42 origin stocks beyond the fact that none is the default; the founder, the founding s
  [04_Phase_07_Order.md]  T4 present: the 42 origin stocks and every composition share beyond the two bodies and the fact that n

  6/6 phase files carry a T4 marker.
  >> If EVERY phase's answer was literally 'nothing', T4 is falsified
     per its own stated condition (the question would be decorative).
     This tool cannot see the marker's CONTENT well enough to judge
     that - read the 6 lines above by hand.

=== T5 - EARLY LOVER-FACULTY SMOKE TEST ===
  EARLY (Phase 6) verdict: Alive, yes: Phases 2 to 6 show a city of two bodies whose one unwritten obligation is a warm night for whoever is inside, strangers held by the ice included, kept in every month and broken only where nobody can see; whether anyone could love it, rather than rely on it, is not yet answerable, because no admitted line writes what any resident cherishes or feels for Casey, and its culture material opens only at Step 5.
  LATE marker absent (08_Review_Panel.md missing or has no 'T5 - LATE LOVER FACULTY:' line yet)

  T5 not fully applied this pass (one or both markers absent).
```

*The T3 rows above were printed before the ledger's P7 column was marked; the ledger was updated right after (see Notes).*

## Notes

**Handoff audit, reconciled by hand.** Inbound: the tool sees 21 rows addressed `**Phase 7**`; the phase file's sweep enumerates 88 rows (those, the contract's G3 row and REQ-11, the every-phase items and the items the readers found). Outbound: the file's HANDED FORWARD table holds 15 rows; rows addressed to Steps are outside the tool's form.

**Position-coverage ledger (T3).** The P7 column of `00.2_Position_Coverage_Ledger.md` was copied by the orchestrator from the phase file's `## T3 · Position coverage` (L570-584): The Ruler, The Elder, The Mentor and The Passer-Through covered; the other five blank, each with its reason there.

**Developer questions** DQ-23, DQ-24 and DQ-25 filed as DEC-533, DEC-534 and DEC-535 in `Research_Logs/DECISIONS_NEEDED_FROM_DEVELOPER.md` (the Casey section, above `## Answered`). No new provisional assumption.

**Web calls:** 38 in Round 1 and 9 in Round 3 (47), every one logged verbatim in the research log's Session 5 and checked against the readers' own tables (47 of 47). Session web total after the merge: see the progress file.

**Readers' staging folders:** B and C each hold only their output and their Round 3 reply; A holds those and its own read-only notes file (checked with `ls`).

