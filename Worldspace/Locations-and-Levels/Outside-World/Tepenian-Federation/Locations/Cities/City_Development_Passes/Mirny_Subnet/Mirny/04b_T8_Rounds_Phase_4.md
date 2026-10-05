# Mirny — Step 4 · Phase 4 · T8 round record

**Pass:** Mirny · ULM · Step 4, Phase 4 (Ordinary Life) · 2026-10-03; Round 1 dispatched 12:07; Round 2 at 13:02; Round 3 blocked at 13:13; slot C retried 13:15; closed 14:21; clock checks 12:05, 13:02, 13:13, 14:10, 14:21 (all in window; the merge was written after 13:59, finishing a started piece).
**Written file:** `04_Phase_04_Ordinary_Life.md`. **Required-reading list:** `.t8_required_04_Phase4.txt` (22 entries, ≈ 4,250 admitted lines).
**Reader files:** `.t8_Phase4_reader{A,B,C,C2}.md` (575 / 627 / 732 / 609 lines) · `.t8_Phase4_round3_reader{A,B,C,C2}.md`, `…_readerA_on_C2.md`, `…_readerB_on_C2.md`. Not canon, not an input; archived with the pass (`DR-27`).

## Round 0 — the required-reading list
From the Phase 4 `MUST OPEN` block (`03_The_Phase_Spine.md` L538–556) plus the pre-trip carve-outs. **Order is binding:** `Robot_Physiology_and_Cultural_Practices.md` before `Robot_Cold_Physiology.md` (`M-151`). **The Division of Industry files were admitted at ranges only:** file 16 at the four re-derivation warnings and formula (L109–134), the legend (L241–248) and Mirny's own row (L275); file 09 at §3.5's national principle (L124–141); file 13 at §12 (L637–694); files 10 and 11 in full (file 10 is required reading before citing any food figure). **Not admitted:** every other row of file 16; the `09` §2 per-city table (superseded); the cross-city comparison lines of `09` §3.5 (L142–185); `13` §§14–15 (cross-city classification). **Not files:** concept art (empty), the megasheet (withheld), `City_Logistics.md` (`M-152`). The brief carried the Division of Industry **citation gate** (citable: Mirny's own row; not citable: export headcounts, "feeds N", the withdrawn rate 53, the superseded `09` row, any Rank) and the named failure modes of the phase.

## Round 1 — dispatch
Three `general-purpose` agents, one brief (`T8_PHASE4_PROMPT`), differing only in letter and output file. Tool uses: A 91; B 84; C 70. **C's first attempt is superseded** (see Round 3); its slot was re-run as **C2** (83 tool uses) on the same brief.

## Round 2 — `triple_read_verify.py`, raw output (non-matching and header lines pasted; the 66 passing `all fields match ground truth` lines are counted, not repeated)
**Run 1 (13:02, readers A, B, C; file at that time 536 lines):**
```
required files: 22
agents: agent1, agent2, agent3
=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 82-272,534-611] ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Cold_Physiology.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/16_Per_City_Three_Tier_Run.md  [range 109-134,241-248,275] ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/09_Per_City_Baseline_Run.md  [range 124-141] ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/11_Caloric_Rebuild_and_Livestock_Tier.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/10_Validation_Findings_2026-09-01.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/13_National_Balance_Under_the_Ruling.md  [range 637-694] ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/National_Medical_and_Care_Institutes.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/National_Economy_and_Currency.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00b_General_Population_Discipline.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00d_Shadow_Proportion_Discipline.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00.1_Step_MINUS-1_Input_Contract.md  [range 1-20,207-393] ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Mirny.md  [range 1-3,5-8,10-58,60-83,85-98,100-135,137,139-140,142-143,145-157,159,161,163,165,167,169-182,184-188,193-195,197,199,201,203-205,207,209-211,213,215,217-221,224-226,229-230] ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00_Frame.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/01_Inherited.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/02_Spine.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/03_Research.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_02_Composition_and_Arrival.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_03_Surface_and_Texture.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Phase_4.md ===
=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```
Result: 66 / 66 field checks match. **UNANIMOUS - CLEARED TO WRITE.**

**Run 2 (14:10, readers A, B, C2) — after the input-file edit described in Snag 1 of the phase file:**
```
required files: 22
agents: agent1, agent2, agent3
=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 82-272,534-611] ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Cold_Physiology.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/16_Per_City_Three_Tier_Run.md  [range 109-134,241-248,275] ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/09_Per_City_Baseline_Run.md  [range 124-141] ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/11_Caloric_Rebuild_and_Livestock_Tier.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/10_Validation_Findings_2026-09-01.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/13_National_Balance_Under_the_Ruling.md  [range 637-694] ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/National_Medical_and_Care_Institutes.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/National_Economy_and_Currency.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00b_General_Population_Discipline.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00d_Shadow_Proportion_Discipline.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00.1_Step_MINUS-1_Input_Contract.md  [range 1-20,207-393] ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Mirny.md  [range 1-3,5-8,10-58,60-83,85-98,100-135,137,139-140,142-143,145-157,159,161,163,165,167,169-182,184-188,193-195,197,199,201,203-205,207,209-211,213,215,217-221,224-226,229-230] ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00_Frame.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/01_Inherited.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/02_Spine.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/03_Research.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_02_Composition_and_Arrival.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_03_Surface_and_Texture.md ===
  agent1   ⛔ LINES MISMATCH  claimed='536'  actual='539'
  agent2   ⛔ LINES MISMATCH  claimed='536'  actual='539'
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Phase_4.md ===
=== VERDICT ===
⛔ NOT UNANIMOUS - DO NOT WRITE. Log which agent/file failed and why.
```
Exit status 1: **NOT UNANIMOUS** — A's and B's file-21 PROOF claimed 536 lines; the file was 539 lines after my correction of two wordings (A and B had read the earlier state). Every other field matched. **Not a read failure: a process error of mine.** Repair: A and B re-read the file in full and re-issued only the file-21 PROOF block (each also reported what differed between the two states).

**Run 3 (14:21, readers A, B, C2, after the repair):**
```
required files: 22
agents: agent1, agent2, agent3
=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 82-272,534-611] ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Cold_Physiology.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/16_Per_City_Three_Tier_Run.md  [range 109-134,241-248,275] ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/09_Per_City_Baseline_Run.md  [range 124-141] ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/11_Caloric_Rebuild_and_Livestock_Tier.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/10_Validation_Findings_2026-09-01.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/13_National_Balance_Under_the_Ruling.md  [range 637-694] ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/National_Medical_and_Care_Institutes.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/National_Economy_and_Currency.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00b_General_Population_Discipline.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00d_Shadow_Proportion_Discipline.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00.1_Step_MINUS-1_Input_Contract.md  [range 1-20,207-393] ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Mirny.md  [range 1-3,5-8,10-58,60-83,85-98,100-135,137,139-140,142-143,145-157,159,161,163,165,167,169-182,184-188,193-195,197,199,201,203-205,207,209-211,213,215,217-221,224-226,229-230] ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00_Frame.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/01_Inherited.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/02_Spine.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/03_Research.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_02_Composition_and_Arrival.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_03_Surface_and_Texture.md ===
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Phase_4.md ===
=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```
Result: **66 / 66 field checks match. UNANIMOUS - CLEARED TO WRITE.**

## Round 3 — peer cross-check (same agents via `SendMessage`; each pointed at the other readers' files)
The prompt carried the four questions with sub-checks (non-verbatim quotations; EXCLUDED spec spans incl. L82 chars 423–500 and the five drifted lines; invented practice, amenity, time budget or robot behavior; other-city figures; currency; the food gate; a universal resident) plus the fifth section (disposition differences) with eleven required points.

**First pass (readers A, B, C):**
| Reader | vs | Verdict | One-sentence reason |
|---|---|---|---|
| A | B | CONSISTENT | quotations, arithmetic and receipts check out; over-reaches labelled [D] and low weight |
| A | C | **INCONSISTENT** | C read the same files and its quotations check out, but it contradicts the cold file by calling indoor recharge "required", writes a speed and commute minutes with no admitted transport mode, and builds smoking, kinship and near-miss practices no admitted line supports |
| B | A | CONSISTENT | — |
| B | C | CONSISTENT | — |
| C | A | CONSISTENT | — |
| C | B | CONSISTENT | — |

**Gate: BLOCKED** (not 6 / 6). Per `N.2` the write did not happen; per the recipe's retry rule the failing slot was re-dispatched.

**Retry (readers A, B, C2):**
| Reader | vs | Verdict | One-sentence reason |
|---|---|---|---|
| A | B | CONSISTENT (first pass stands) | — |
| B | A | CONSISTENT (first pass stands) | — |
| A | C2 | **CONSISTENT** | no walking speed, no "required", no invented practice, no time budget; one over-reach noted: the axis word "gated" and "the site closes the door" against `P3` B.0 |
| B | C2 | **CONSISTENT** | same checks; findings only C2 made are mostly confirmable; "bias toward staying in" and "below 47.1 %" as fact are not |
| C2 | A | **CONSISTENT** | — |
| C2 | B | **CONSISTENT** | — |

**6 / 6 CONSISTENT (A↔B, A↔C2, B↔C2) → gate met.**

### What Round 3 caught (the gate adding signal)
The first pass caught the failing reader: a **5 km/h** walking speed and minute commute times against a brief that said to write no mode; "required" recharge against a three-option cold table; three invented practices (a smoking plume, kinship by wind, near-miss retelling); a time budget. The retry pass caught a smaller set in C2 (the axis word "gated"; "no part of the city is a refuge"; a derived bias toward staying in) and **real defects in already-written files:** `P3` L140's **"29 lit weeks"** (reader B, a unit slip that three phases of readers had passed), `P3`'s **residual unsoftened recharge phrases** after my first repair (C2), `DS4` L21's **"governing mechanic" label** (the `M-151` trap, C2), and `DS4`'s header calling the row's percentages "of the DISTINCTIVE tier" against its own 100.0 sum (C).

### Dispositions on the eleven points (merge)
| Point | Disposition | Written as |
|---|---|---|
| (i) the 11.8 % | a share of the workforce *as the row states it* (sums to 100.0); `DS4`'s contrary header docketed; 11.8 / 23.6 stays parked | used as printed; R-24; Snag 5 |
| (ii) the free tier | **not** "what residents do instead"; it can contain the quarry and the hub; people-or-life reading is the developer's | P4-8; Q-43 |
| (iii) headline sentence | all three inside admitted spans; no difference of substance | §A |
| (iv) axis | "The stop and the crossings"; "gated" struck | The axis |
| (v) escapism | national canon only; Mirny's placement and human leisure REQUESTED; the empty middle named | P4-10 |
| (vi) populations | the same five plus the mixed household; constraints only | §C |
| (vii) scale arithmetic | identical across readers; no mode, speed or commute time; C2's D = 1.00 counterfactual and sunset arithmetic accepted as derivations | §D |
| (viii) recharge | **prudent default, not a requirement**; corrects `P3`'s wording | P4-1, P4-5; PA-20 |
| (ix) backward strains | five real, one reconciled | Backward check |
| (x) robot feeding | not in the admitted lines; free share an upper bound, possibly lower | P4-6, P4-8; R-42 |
| (xi) care figures | national rates × Mirny's census, indicative only | P4-6 |

## Merge (per the amended `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` §N.2, `M-246`)
Contradictions → most conservative; no contradiction → union with credit (provenance table in the phase file). The merge is of the **cleared set A, B, C2**; C's first attempt contributes only items that A or B confirmed in Round 3. **Quotation re-check by script:** 107 quoted strings checked against the 22 sources plus the pass's files; the two strings in `RP` that wrap across blockquote lines were re-checked with the markers stripped and match; the remaining unmatched strings are, by inspection, the alternate axis names, scare-quoted struck claims and the alternates list.

## Snags in this round (the recording law)
- **Input files must be frozen for a round.** I edited `P3` while C2 was reading; the verifier caught it (Run 2). See Snag 1 of the phase file.
- **A Round 3 INCONSISTENT is a real outcome, not a formality:** the first slot-C attempt would have put an invented walking speed and three invented practices into the written phase.
- The hook notice to run graphify appeared on essentially every orchestrator call; none reached readers B and C's sessions in this phase (A reported none either); nothing was run.
