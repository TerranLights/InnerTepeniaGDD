# Mirny · Amendment re-derivation · Piece ST13 (Phase 3, Surface and Texture) · T8 round record · 2026-11-05

**Companion to** `Amendment_Rederivation_ST13_Phase3_2026-11-05.md`. Raw tool output is pasted, not summarized; where a block is not the whole output it is headed as excerpted. Working files are in this folder as `.t8_amend_ST13_*`.

## Setup
- **Reading list (trimmed, `DR-74`):** `.t8_required_amend_ST13.txt` (scratchpad copy `amend_ST13/t8_required_amend_ST13.txt`, byte-identical by `cmp`), **35 entries, 7,315 admitted lines** (counted by this merge's scratch script: whole files by physical lines at merge time, spans by their ranges): the rules (the stereotypes law; the phase-spine spans; the general-population and shadow disciplines; the rulings log at 24 spans); the live sources at Mirny's rows only (the climate READER, the Mirny spec at 29 spans, both robot files, the Founding Register, the relationship database, the immigration composition file, the language blocs); the input contract's spans; the Frame, Inherited, the Spine, Research and Phase 2, whole; **the object, read whole: Phase 3 (entry 20) and its datasheet (entry 21)**; the amendment layer from before the repass (the Phase 6, 7, 2, 9 and 8 pieces, the Phase 8 dockets, the Idelsk-Uralia piece, the robot-term piece's first 30 lines, the amendment register, the reconciliation note's L1 to L120); the first 60 lines of the Phase 10 and Step 5 pieces; the answers note of 2026-11-04; and the first 90 lines of the Steps −1 to 3 piece (`ST12`).
- **The list's spec spans** (entry 4) are Phase 3's own receipt spans (`P3` L30) in the 230-line numbering, applied to the 252-line spec: an orchestrator's list error, found by all three readers (piece snag 1; AR-221).
- **Brief:** `.t8_amend_ST13_brief.md`, identical for A/B/C with `{X}` the reader letter; **sha256[:16] f546ab181f55adc5** (computed by this merge on the folder copy; the scratchpad copy is byte-identical by `cmp`). It carries eight orchestrator-verified results with sources, the developer's binding words, the stage order, eleven traps and six standing lines.
- **Readers:** three Opus agents, dispatched 06:55 on 2026-11-05 after the list and brief were frozen at 06:45 (file times; checkpoint L5): A `aae1fd60dd29bd6e1`, B `aab7046110b41eb46`, C `a42b49727af661164`. Outputs time-stamped 07:13 (A), 07:16 (B) and 07:18 (C) in the scratchpad; Round 1 recorded complete in the checkpoint's update (L14 to L15). **None refused any entry** (each reader's reading log and receipt). Graphify: not used by any reader; no reader saw a hook notice (A snag 12, B snag 12, C snag 1).

| Reader | Output lines | Bytes | PROOF blocks | Findings (Round 1 numbering) | Missed-findings list | Docket | Requests · questions · RFs |
|---|--:|--:|--:|---|---|---|---|
| A | 1,034 | 109,247 | 35 | AS13-1 to AS13-23 | by label (its L351 to L399) | DK13-1 to DK13-23 | AR-220 to AR-226 · AQ-220 to AQ-224 · RF-ST13-1 to RF-ST13-6 |
| B | 932 | 111,223 | 35 | AS13-1 to AS13-19 | M-1 to M-27 | DK13-1 to DK13-36 | AR-220 to AR-224 · AQ-220 to AQ-224 · RF-ST13-1 to RF-ST13-5 |
| C | 1,038 | 121,767 | 35 | AS13-1 to AS13-29 | by label (its L437 to L468) | DK13-1 to DK13-33 | AR-220 to AR-223 · AQ-220 to AQ-224 · RF-ST13-1 to RF-ST13-5 |

Line and byte counts by `wc` on the folder copies, byte-identical to the scratchpad copies (`cmp`); PROOF blocks counted by `grep -c '^### PROOF:'` (35 each). No reader proposed a DEC number.
- **Self-checks before handback (as each reader records):** A checked every whole file's line count with `wc -l` and the last byte (its L43); B re-copied three PROOF fields by hand after a check of the finished fields against the files caught them (its snag 15); C records no graphify use and no repository-wide search. No PROOF field was produced by a script; no reader created a helper file in the repo.
- **Ruling-log freeze (`M-302`):** not checked by this merge writer.

## Round 1 headline claims (union, before Round 3)
| Claim | A | B | C |
|---|---|---|---|
| The physics (P3-2's first and second orders, the door, the indoor default, the axis, §A) | stands | stands | stands |
| The door's social layer | written into P3-7's own addendum | a pointer to A8-5 | a pointer to A8-5 |
| "Cannot" at L175 | reads "has not yet been taught" (a reword) | the clause stands and now has its channel | the arrival "not yet taught" (in substance) |
| A social note on P3-2's physics lines (L168 to L173) | yes (its DK13-7) | a term note at L168 only | none |
| "Warning" for the physical onset (L168, L387, L417, L521) | marked (L168, L387, L417, L521) | marked (L168, L521) | not marked |
| L333, "the one role confirmed" | marked | stands | marked |
| The coinage at L342 | the ring's clearers | a no-label form | the ring's clearers |
| L216 (the visitor and the sky) | P | stands | W (minor) |
| L262 and L361 (the relay) | P | none, a pointer | W (an addition) |
| L68 (read order) | none | none | T |
| L456 (RF-9) | none | none | N |
| L441, L461, L475 (terrain) | L | P (L441, L461) | none |
| The extent lines' tag | C, L | C, P | C, L |
| Live spec L91 and L104 changed | not noted | noted | noted |
| The June and December notes changed | noted | noted | not noted |
| The L115 quotation slip | found | not found | found |
| Phase 3's own datasheet cites (L39, L41, L42, L78) | found | not found | found |
| L61 among the old-extent lines | in its section 3 | not listed | listed |
| The ring's form to research (`DR-55` Q-82) | not cited | not cited | cited |
| The equal-area radii | from 140.35 and 200.51 km² | from 140 and 201 km² | from 140.35 and 200.51 km² |
| Sensitivity of the re-key request | moderate | moderate | high |
| Numbering | AS13-1 to AS13-23 | AS13-1 to AS13-19 | AS13-1 to AS13-29 |

## Round 2 (`Tools/triple_read_verify.py`) · first run NOT UNANIMOUS on one field; reader C repaired it; re-run UNANIMOUS
**What happened (checkpoint L15, and the orchestrator's account to this merge, ORCH).** On the first run 34 of the 35 entries matched for all three readers, and on the 35th, `Founding_Register.md` at its admitted range `1-31,57,88`, readers A and B matched and reader C's **LMID** did not: the admitted set has 33 lines, so LMID is the line at position 17 of the set (L17), and C's claimed text is not that line (one line off). **This was a reader's copying error on one field, not a list defect.** Reader C repaired that single field (the orchestrator records the repair rule as `DR-117`, whose text is *ID not opened* for this merge) and the tool was re-run: **UNANIMOUS, 35 entries.** The first run is kept as `.t8_amend_ST13_round2_raw_FIRSTRUN.txt`. The two files differ on exactly two lines (`diff`, by this merge): line 82 (agent3's result on the Register) and line 180 (the verdict). Both raw outputs follow, verbatim.

### Round 2, first run: raw output (full; file `.t8_amend_ST13_round2_raw_FIRSTRUN.txt`)
```
required files: 35
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 82-272,472-531] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Climate Data/READER/Mirny.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Mirny.md  [range 1-3,5-8,10-58,60-83,85-98,100-135,137,139-140,142-143,145-157,159,161,163,165,167,169-182,184-188,193-195,197,199,201,203-205,207,209-211,213,215,217-221,224-226,229-230] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Cold_Physiology.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00.1_Step_MINUS-1_Input_Contract.md  [range 1-20,207-393] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00_Frame.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/01_Inherited.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/02_Spine.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/03_Research.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_02_Composition_and_Arrival.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 203-251,422-435,448-461,463-475,510-524,538-553,609-621,953-965,1075-1088,1092-1107,1111-1133,1137-1156,1211-1226,1404-1412,1427-1434,1438-1445,1460-1468,1472-1479,1523-1530,1550-1557,1570-1577,1655-1662,1664-1671,1707-1715] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Founding_Register.md  [range 1-31,57,88] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ⛔ LMID  MISMATCH  claimed='(`Post-War_Nations_Founder_Reference.md`) is a CST task (`DR'  actual='5. **Post-war framing comes later.** Rows name founders in p'

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Relationship_Database.md  [range 1-58,334-344] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Upper_Earth_Immigration_Composition.md  [range 1-3,21-35,619-627] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Language_Blocs_By_City_2026-11-03.md  [range 988-1026] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_03_Surface_and_Texture.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Phase_3.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P06_Meaning_2026-10-29.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P07_Order_2026-10-29.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P2c_Composition_2026-11-03.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P9_Populations_2026-11-04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P08_Making_2026-11-03.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Dockets_P08_Making_2026-11-04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_PIU_IdelskUralia_2026-11-04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_PRT_RobotTerm_2026-11-04.md  [range 1-30] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/DR-56_Amendment_Register_2026-10-13.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Notes_2026-11-03_Culture_File_and_Composition_Reconciliation.md  [range 1-120] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P10_Catalog_2026-11-04.md  [range 1-60] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_S5_Reconciliation_2026-11-04.md  [range 1-60] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Notes_2026-11-04_Answers_Carried_Forward.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md  [range 1-90] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
⛔ NOT UNANIMOUS - DO NOT WRITE. Log which agent/file failed and why.
```

### Round 2, second run: raw output (full; file `.t8_amend_ST13_round2_raw.txt`)
```
required files: 35
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 82-272,472-531] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Climate Data/READER/Mirny.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Mirny.md  [range 1-3,5-8,10-58,60-83,85-98,100-135,137,139-140,142-143,145-157,159,161,163,165,167,169-182,184-188,193-195,197,199,201,203-205,207,209-211,213,215,217-221,224-226,229-230] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Cold_Physiology.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00.1_Step_MINUS-1_Input_Contract.md  [range 1-20,207-393] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00_Frame.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/01_Inherited.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/02_Spine.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/03_Research.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_02_Composition_and_Arrival.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 203-251,422-435,448-461,463-475,510-524,538-553,609-621,953-965,1075-1088,1092-1107,1111-1133,1137-1156,1211-1226,1404-1412,1427-1434,1438-1445,1460-1468,1472-1479,1523-1530,1550-1557,1570-1577,1655-1662,1664-1671,1707-1715] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Founding_Register.md  [range 1-31,57,88] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Relationship_Database.md  [range 1-58,334-344] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Upper_Earth_Immigration_Composition.md  [range 1-3,21-35,619-627] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Language_Blocs_By_City_2026-11-03.md  [range 988-1026] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_03_Surface_and_Texture.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Phase_3.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P06_Meaning_2026-10-29.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P07_Order_2026-10-29.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P2c_Composition_2026-11-03.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P9_Populations_2026-11-04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P08_Making_2026-11-03.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Dockets_P08_Making_2026-11-04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_PIU_IdelskUralia_2026-11-04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_PRT_RobotTerm_2026-11-04.md  [range 1-30] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/DR-56_Amendment_Register_2026-10-13.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Notes_2026-11-03_Culture_File_and_Composition_Reconciliation.md  [range 1-120] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P10_Catalog_2026-11-04.md  [range 1-60] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_S5_Reconciliation_2026-11-04.md  [range 1-60] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Notes_2026-11-04_Answers_Carried_Forward.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md  [range 1-90] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

**Reading the two outputs.** First run: 35 entries; 104 of 105 agent-entry results show all fields matching; the one failure is agent3 (reader C), LMID, on the Founding Register; verdict NOT UNANIMOUS. Second run: 35 entries; 105 of 105 matching; verdict UNANIMOUS. **One field was repaired, by reader C, on one entry; no other field changed.**

## Round 3 (SendMessage to the same three agents) · 2026-11-05, replies 07:24 to 07:25 (scratchpad file times) · cross-check done
Each reader was sent shared points (K1 to K8), a request to map the other two readers' re-derivations onto the old items, to list every split that would change what a file says with the position it would hold, to check the single-finder finds against the pass lines, and to list any claim in the other two readers' work it would not accept. Replies: `.t8_amend_ST13_round3_reader{A,B,C}.md` (293, 191 and 171 lines; byte-identical to the scratchpad copies by `cmp`). **The text of K1 to K8 as sent is not in the folder;** the topics are read from the replies, which agree on them. Each reply adds its own ninth point (A also a tenth).

| Reader | Part 1 objections | Lines re-opened | Claims rejected in the others' work | Concessions (its Part 4) | Holds |
|---|---|---|---|---|---|
| A | none to K1 to K8; K9 concedes three live-source changes it missed | `P3` L68, L456; `DRL` L1102, L1219; spec L91; `CON` L261 to L271 (its L5 to L9) | C's T on L68; C's N on L456; none of B's | 11 (K9; L372, L73, L62; the Q-68 note; Q-82; the door as a pointer; the tags at L361, L262, L216; "cannot"; the L421 to L425 item; the L506 mark; B's datasheet find and C's splice; the requests folded) | the "warning" mark; L333; the L115 slip; the ring's clearers with B's form beside it; T none; no N on L456; its radii |
| B | K3: objects to C's T on L68 | `P3` L38 to L42, L68, L115, L333, L417, L464; spec L154, L205; `DRL` L1102; `P9` L125; `DS3` L5 to L6 (its L4) | C's T on L68 | 13 (L333, L417, L115, Phase 3's datasheet cites, L61, "cannot", the ring's clearers, A's L80 split, Q-82, C's trap-10 record, the optional rows and C's splice, AR-220 to high, its AS13-19 to the feeds) | the "warning" mark; L68 not T; the door as a pointer; the ring length; its own reserved finds; the masts note as a snag |
| C | K1: holds no note on the physics lines; K2: concedes the "warning" term it missed | `P3` L160 to L176, L198 to L206, L253 to L258, L330 to L348, L369 to L389, L414 to L425 (its L3) | A's L on L441, L461, L475 | 13 (L256; its L203 quotation; the term; the June and December notes; L80 narrowed; "cannot"; L335; L333 softened; W withdrawn at L216, L361, L262; L222 to L223; the no-link sentence; its Q-68 tag at L405 dropped; A's R-28 half, L471 and B's L48 accepted) | the physics with no note; the door as a pointer; L91; the trap-10 record; the indirect checks; the optional rows; its RF on capacity; the rejection of A's L tags |

### The shared points (K1 to K9)
| K | Topic (as read from the replies) | A | B | C |
|---|---|---|---|---|
| K1 | the physics stands: heat follows the wind, the door, the indoor default, the axis, §A | AGREE; concedes the door's pointer form and drops its separate reword of "cannot" | AGREE; accepts "cannot" as not yet taught and `DR-55` Q-82 for the entry and ring form | AGREE, with one docket split held: no note on the physics lines; the door a pointer |
| K2 | the wind lines | AGREE on the core set; keeps the "warning" term (A, B) and L333 (A, C) | AGREE; concedes L333 and L417 | AGREE; concedes the term it missed; narrows L335 and L333; withdraws W at L216, L361, L262 |
| K3 | composition and figures | AGREE; rejects C's T on L68; the rounding split immaterial | AGREE; concedes L61; objects to C's T on L68; adopts A's L80 split | AGREE; concedes its L255 and L203 quotation defects |
| K4 | NOT WIND rulings | AGREE; keeps C's Q-82; concedes the Q-68 note, L372, L73, L62; rejects C's N on L456 | AGREE; folds A's R-28 everyday half narrowly | AGREE; keeps Q-82 as a pointer; drops its Q-68 tag at L405, keeps a note on RF-9 |
| K5 | symbols, facts only | AGREE; no link from the axis to the Element | AGREE | AGREE; adds the no-link sentence |
| K6 | drifted anchors | AGREE; keeps the L115 slip (A, C), B's April-row precision and C's datasheet splice | AGREE; concedes the L115 slip and Phase 3's datasheet cites | AGREE |
| K7 | the spec span issue (the orchestrator's list error) | AGREE; none of the three read L99, L136, L138, L162, L164, L196, L198, L206; C's trap-10 record agreed | AGREE; adds C's trap-10 record to its snags | AGREE |
| K8 | the rulings outside the list | AGREE (`DR-117` to `DR-121`, `DR-78`: ID not opened; `DR-102`, `DR-107` to `DR-116` through entries 34 and 35) | AGREE | AGREE; agrees with A's Q-81 attribution note |
| K9 | (each reader's own) | the live-source changes A missed (spec L91, L104, L135): conceded | language: all three used `ANS` L10 over the Phase 9 piece's English alone | the live-source changes C missed (the June and December notes): conceded |
| K10 | (A only) | B's strongest-finding feed: keep as a feed line | (B moved it to its feeds) | — |

### The splits, and how they were settled
*Rule: the position two or three readers hold after Round 3's concessions; where they still differ, the most conservative reading (the one that changes less, claims less or keeps a record), the split named in the piece.*

| # | Point | Positions after Round 3 | Settlement (where in the piece) |
|--:|---|---|---|
| 1 | **The door's social layer** | B, C: a pointer to A8-5; A conceded | **a pointer** (AS13-19) |
| 2 | **A note on P3-2's physics lines** (A's DK13-7) | B: a term note only; C: none; A did not withdraw | **no mark on L168 to L173** (B, C; the reading that changes less) (AS13-13; DK13-13 empty) |
| 3 | **"Cannot" at L175** | all three: reads as not yet taught; A dropped its separate reword | **a reading note inside the scope addendum** (AS13-15) |
| 4 | **"Warning" for the physical onset** | A, B; C conceded | **a terminology mark; a decision proposed** (AS13-14) |
| 5 | **L333, "the one role confirmed"** | A, C; B conceded; C softened to a scope pointer | **a scope pointer, W, P, N** (AS13-23) |
| 6 | **The coinage's wording** | A, C: the ring's clearers; B adopted it and offers its no-label form beside it; A asked that both be offered | **the ring's clearers in the piece; both offered as a decision** (AS13-25) |
| 7 | **L216** | A, B: none; C withdrew W | **none; a pointer** (AS13-17) |
| 8 | **L262 and L361** | all three: none, a pointer | **as all three hold** (AS13-21) |
| 9 | **L68's T** | A, B: none; C did not hold it in Round 3 | **none** (section 1.1) |
| 10 | **L456's N** | A: rejected (`DRL` L1219 rules essential status, not exposure); B: no claim changes; C kept a note only | **not carried** (section 1.1); this merge read `DRL` L1219 |
| 11 | **L441, L461, L475's L** | C rejected (terrain, not a figure); B: P (single); A did not reply on it | **not carried;** this merge read `EXT` L611: the label still reads "coastal ice" (section 1.1; AS13-4) |
| 12 | **P on the extent lines** (L61, L255 to L256, L344 to L345) | B: C, L, P; C accepted both L and P; A: L, not P | **C, L, P** (B, C; A named) (AS13-4) |
| 13 | **P on P3-1's third order** (L142 to L144) | B; C accepted it; A folded it into W | **W, P** (B, C; A named) (AS13-11) |
| 14 | **N on M2** (L340 to L341) | C's tag; B's block tag; A's own AS13-10 label | **W, P, N** (AS13-24) |
| 15 | **I on snag 3** (L486) | A's; B and C both listed I in Round 3 | **A, I, L** (AS13-29) |
| 16 | **L425's W (B) and N (C)** | A: L425 makes no language claim; B, C: P | **P only** (AS13-28) |
| 17 | **The ring length's basis** | A, C: 140.35 and 200.51 km²; B: 140 and 201 km²; all: about 42 to 50 km | **A's and C's figures, B's named; immaterial** (AS13-4) |
| 18 | **Confidences** | the term (A moderate, B medium); M2 and dress (A high, B and C medium); the byproduct (A moderate, B high, C medium); the datasheet rows (A moderate, C low) | **the lower, unless a ruling is quoted verbatim** (B's rule) (section 5) |
| 19 | **AR-220's sensitivity** | A, B moved to C's high | **high** (AR-220) |
| 20 | **Numbering** | three colliding sets: A 23, B 19, C 29 | **33 merged findings in Phase 3's file order** (the merge brief), mapped in piece section 1.4 |

### Single-finder finds, checked against the pass lines in Round 3
| Find | Finder | Checked by | In the merge |
|---|---|---|---|
| L417, "the warm warning" | A | B, C added it | AS13-14 |
| L333's scope | A, C | B conceded | AS13-23 |
| The L115 quotation slip | A, C | B re-opened spec L154 and L205 and conceded | AS13-32 |
| Phase 3's own datasheet cites (L39, L41, L42, L78) | A, C | B re-opened L39 to L42 and conceded | AS13-32 |
| L61 among the old-extent lines | C (A's section 3) | B re-opened L61 and conceded | AS13-4 |
| Spec L91 now matches the READER | B, C | A re-opened spec L91 and conceded | AS13-22 |
| Spec L104's comparison clause gone | B, C | A conceded (`DRL` L1555) | AS13-22 |
| July's "Coldest month" unchanged | B, C | A conceded it as a record | AS13-22 |
| The June and December notes changed | A, B | C conceded | AS13-22 |
| L372 to the CST | B, C | A conceded | AS13-5 |
| L73 and L62 | C | A conceded | AS13-5 |
| `DR-55` Q-82 for the ring's and entry's form | C | A, B accepted (B re-opened `DRL` L1102) | AS13-7 |
| The `DR-59` Q-68 note on the harbor watch | B, C | A conceded (a note, no claim change) | AS13-23 |
| R-28's everyday half (L464) | A | B, C accepted it narrowly | AS13-5 |
| L471 (R-35) | A, B | C accepted | AS13-7 |
| L474 and L479 | C | A confirmed | AS13-7 |
| L48, the Register unopened | B | C accepted it as a record note | AS13-2 |
| S1 as an Act 1 seam, with AR-226 | C | B: keep as a pointer; A: S1 stands, the request kept low | AS13-20; AR-226 |
| L118 as a pointer | C | A, B folded it | AS13-8 |
| `DS3` L5's splice | C | A, B (low) | AS13-31 |
| Live L132 is the April row | B | A kept it | AS13-31 |
| The trap-10 placeholder line against `DR-111` | C | A, B agreed | AS13-7; piece snag 8 |
| "No living teacher" stays true of the station's work | A | B, C adopted it | AS13-9 |
| The L421 to L425 item | B, C | A conceded | AS13-28 |
| The L506 record mark | B, C | A conceded | AS13-30 |
| Q-81's attribution in the brief | A | C agreed | piece snag 10 |
| Optional datasheet data rows | A, C | B accepted (low) | AS13-31; decision 4 |
| The cold-file citation at L204 | A, C | B agreed | AS13-16 |
| What Phase 3 supplies to the strongest finding | B | A kept it as a feed line; B moved it to its feeds | AS13-33 |
| The terrain request (R-25, Q-39) | B, C | A conceded | AR-224 |
| Who clears the ring | B | A, C kept it low | AR-225 |
| Reserved singles: lead time (A RF-4); the newcomer's first storm in an outage (A RF-6); a knowledge seam, rime on the relay, newly online robots (B RF-1, RF-3, RF-5); a capacity reduction (C RF-4) | as named | kept reserved by the others (A's RF-6 folded as a pointer by A, kept by B) | RF-ST13-2, -10, -7, -3, -5, -4 |

### Claims not accepted (left out of the merge; each listed with what was done)
| Claim | Whose | Objected to by | Why | In the merge |
|---|---|---|---|---|
| T on L68 | C | A, B | the line states no tier or robot-term figure | none (section 1.1) |
| N on L456 (RF-9) | C | A (B: no claim changes) | `DRL` L1219 rules essential status, not exposure | not carried |
| L on L441, L461, L475 | A | C | the lines carry the terrain question, not a figure; `EXT` L611's label is unchanged | not carried |
| a social-layer note on P3-2's physics lines | A (DK13-7) | C (B a term note only) | the physics lines are unchanged; the social layer belongs to the third order | DK13-13 empty (AS13-13) |
| the door's social layer written into P3-7's addendum | A (AS13-8) | B, C (A conceded) | the layer is the accepted Phase 8 piece's A8-5 | a pointer (AS13-19) |
| a separate reword of "cannot" | A (AS13-6) | A withdrew it | the scope sentence carries the reading | a reading note (AS13-15) |
| the L175 clause "stands" without narrowing | B (AS13-3) | A, C (B conceded) | the protocol is public and learnable by anyone who wants to | not yet taught (AS13-15) |
| L333 "stands" | B (AS13-15 iii) | A, C (B conceded) | the harbor's call is one public call among others | a scope pointer (AS13-23) |
| L334 and L335 "state the retired premise" | C (AS13-4) | A, B (C conceded) | "without a named teacher" is literally true | must not be read as untaught (AS13-23) |
| W on L216, L361, L262 | C | A, B (C withdrew) | the lines are true as written | pointers (AS13-17, AS13-21) |
| "and a station is a small part of that" at L255 | C | (C found it itself in Round 3) | the clause is on L256 | L256 (AS13-4) |
| a L203 quotation across a line break | C | (C found it itself) | quotations come from one physical line | the on-line substring (AS13-12) |
| the R-13 clause anchored at L222 alone | C | (C conceded) | the clause runs across L222 to L223 | L222 to L223 (AS13-6) |
| L80's no-teacher clause scoped whole to the first generation | B, C | A (B, C adopted A's split) | the station's work stays untaught (`NNS` L21) | the split (AS13-9) |
| N on L425 for language | C | A | L425 makes no language claim | P only (AS13-28) |
| W on L425 | B | (single) | not confirmed in Round 3 | P only (AS13-28) |
| N on L405 | C | (C dropped it) | the harbor watch's status changes no claim there | none (section 1.1) |
| C's notice addendum restating "best placed" | C (AS13-1) | B (harmless) | adds to what supersedes the sentence | not carried (AS13-1) |

## Settled in the merge (beyond the splits)
- **Union applied:** A (the term at L417 and L521; the generators line's split; the L115 slip; Phase 3's datasheet cites; R-28's everyday half; L471; the radii from 140.35 and 200.51 km²; the delete-the-name test on the axis; RF-ST13-2, RF-ST13-10); B (L48; the spec's changed notes and lines; the both-bodies price of misreading; the visitor as a condition of a person; the April row; the Q-77 note on S2; the airlock line not used; the strongest-finding feed; AR-224, AR-225; RF-ST13-3, RF-ST13-5, RF-ST13-7; the confidence rule); C (L61, L62, L73; Q-82; the trap-10 record; the notice carrying every wind line; S1 as an Act 1 seam and AR-226; L474, L479; `DS3` L5; the no-label check of L335; M2 reserved and M1 standing; AR-221 as its own request; RF-ST13-4; the K7 indirect checks).
- **Who teaches is open** (`ANS` L15). The addenda say only that the wind is taught person to person. No reader named a teacher; none is named here.
- **The section 1 table:** positions extracted by this merge's scratch script at item grain (A's and B's tables; C's bullet list), with B's and C's rows assigned to A's finer rows inside A's blocks; Round 3 concessions and confirmations applied as named overrides (L35, L39 to L42, L45, L46, L48, L61, L62, L67, L68, L73, L77, L78, L80, L105, L115, L118, L142 to L144, L168, L216, L222 to L223, L234 to L238, L255 to L257, L262, L271 to L285, L333 to L335, L340 to L341, L344 to L345, L361, L372, L405, L417, L425, L441, L456, L461, L464, L471, L474, L475, L479, L486, L521, `DS3` L5). Single-reader A tags on spec citations are covered by the anchor rule (AS13-32) and not listed.
- **Numbering:** 33 merged findings in Phase 3's file order (the merge brief's order); one docket row per finding (the form of the Steps −1 to 3 piece), DK13-10 and DK13-13 empty; B's line-by-line rows and C's separate rows for the receipt's spans and old L69 and L82 folded into DK13-22 and DK13-32.
- **The four decisions proposed** come from: the end-of-file pointer, A's AS13-19 and AQ-223, B's AQ-222 and C's docket preface (reframed by `DR-101` and `DR-116` item 2, read in `ALR` L27 and L30); the coinage's wording, A's Round 3 conflict (2) and B's and C's AQ-221; the term, A's AQ-221 and B's AQ-220 (C joined); the datasheet rows, A's AR-224, C's AQ-223 and B's acceptance. No DEC number is assigned here.
- **Read by this merge beyond the readers' list, to settle points:** `EXT` L611 (the terrain label and the live extent); `ALR` (the amendment-layer rules); `ST12` L897 to L904 (its feeds to this unit); `DRL` L1099, L1100 to L1102, L1105, L1118, L1130, L1140 to L1152, L1219, L1222, L1431, L1432, L1442, L1555, L1660, L1669 (the rulings cited; all inside the readers' spans); the live spec lines quoted in the piece; the eight unread spec lines of snag 1 (an observation only; AR-221 stands).
- **Figures:** the old frame's figures appear only on the "As written" lines of section 2; the mixing check below runs at line level, at finding-block level and on the docket. Shares are weights, never head counts.
- **The coinage** appears in the piece only where it refers to the pass text "the ring has keepers" (L342): the quotation in AS13-25, the addendum's reading note and the decision's wording; no group is named by it and no replacement is coined. The two places where a draft used the plain word for the found record's custodian were reworded before the audit, so the word is not used in any other sense.

## Kept files (`M-132`)
The Round 1 outputs `.t8_amend_ST13_readerA.md`, `.t8_amend_ST13_readerB.md`, `.t8_amend_ST13_readerC.md` and the Round 3 replies `.t8_amend_ST13_round3_readerA.md`, `.t8_amend_ST13_round3_readerB.md`, `.t8_amend_ST13_round3_readerC.md` are kept in this folder as the round's working record, unedited, beside the Round 2 files (`.t8_amend_ST13_round2_raw.txt`, `.t8_amend_ST13_round2_raw_FIRSTRUN.txt`), the frozen brief `.t8_amend_ST13_brief.md`, the list `.t8_required_amend_ST13.txt` and the checkpoint `.t8_amend_ST13_CHECKPOINT.md`. The reader files, the replies, the brief and the list are byte-identical to the scratchpad copies in `amend_ST13/` (`cmp`, by this merge). None of these files is an input to any later step; this record and the piece are the merged result. No helper file was created in the repo by the readers or by this merge (scratch work stayed in the session's scratchpad, `st13_merge/`).

## Quotation audit (`Tools/quotation_audit.py <the Mirny pass folder> --files Amendment_Rederivation_ST13_Phase3_2026-11-05.md --own-pass`, run from the repo root) · 2026-11-05 about 07:46, run before this record existed
raw output, excerpted (1 line omitted: the positive control "HARD - case mismatch", whose test phrase names another location; it is one of the controls behind the instrument line below, which reads VALID; the whole output is in the session scratchpad at `st13_merge/qaudit_run1.txt`):
```
pass audited : Mirny
corpus mode  : default (own pass excluded)
corpus files : 6099   chars: 70,250,310
files audited: Amendment_Rederivation_ST13_Phase3_2026-11-05.md
own-pass mode: a quotation may also be found in this pass's OTHER files (never in its own file)

=== POSITIVE CONTROLS ===
  [easy                      ] FOUND     a terminus is nobody's midpoint
  [HARD - blockquote wrap    ] FOUND     A pass may not proceed to Step 5 with a NEVER CITED row
  [HARD - outside Worldspace ] FOUND     Paste raw QA scan output into the QA block. Never summa
  [HARD - long wrapped       ] FOUND     Different content is not differentiation; a different q

  INSTRUMENT VALID: YES
  NEGATIVE CONTROL (must be absent): PASS - absent

=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 56
NOT FOUND in corpus: 20
  of those, in TABLE CELLS : 0
  of those, in PROSE       : 20

  [Amendment_Rederivation_ST13_Phase3_2026-11-05.md:17]           (p3-2's first and second orders, as13-13), the door where wind, noise and cold stop together (p3-7, as13-19), the indoor default f
  [Amendment_Rederivation_ST13_Phase3_2026-11-05.md:19]           collides (as13-14; a and b, c conceded in round 3): phase 3 uses the word for the physical onset (l168, l387, l417, and the record
  [Amendment_Rederivation_ST13_Phase3_2026-11-05.md:210]           the june note (l134) and the december note (l140) now read with the corrected light model. unchanged residue: july's
  [Amendment_Rederivation_ST13_Phase3_2026-11-05.md:234]           ) l168, l387, l417 and the record l521 (the word
  [Amendment_Rederivation_ST13_Phase3_2026-11-05.md:234]           read as untaught) l340 to l341 (m2) l346 to l347 (unread) l385 to l389 (the byproduct's
  [Amendment_Rederivation_ST13_Phase3_2026-11-05.md:269]           ( drl l1151; drl l1141), provisional; planet
  [Amendment_Rederivation_ST13_Phase3_2026-11-05.md:292]           ( dr-111 , ans l16; p10 l17): rf-3's question and r-26's date and builder are held unstated by ruling, not merely unread, and r-35
  [Amendment_Rederivation_ST13_Phase3_2026-11-05.md:302]           stays true of the station's work : no institution crossed the gap (
  [Amendment_Rederivation_ST13_Phase3_2026-11-05.md:328]           (l169). the phrase is the spine's ( spn l41
  [Amendment_Rederivation_ST13_Phase3_2026-11-05.md:335]           are the ruled weather warnings that travel on the relay; the phase 8 piece lists
  [Amendment_Rederivation_ST13_Phase3_2026-11-05.md:342]           reads as not yet taught: the protocol is public and learnable by anyone who wants to ( drl l1140), so the condition narrows to
  [Amendment_Rederivation_ST13_Phase3_2026-11-05.md:342]           ( p07 l152) (a, c; b conceded in round 3). (ii) the blame pattern is the first generation's
  [Amendment_Rederivation_ST13_Phase3_2026-11-05.md:386]           con l293; the conflict with old l86, con l296) no longer describe them (a, b; c conceded in round 3). old l69 is live l91 and read
  [Amendment_Rederivation_ST13_Phase3_2026-11-05.md:386]           matching the reader, so its demotion ground (
  [Amendment_Rederivation_ST13_Phase3_2026-11-05.md:386]           con l261) is gone (b, c; a conceded). old l82 is live l104; its comparison clause is gone ( dr-88 , drl l1555), and every phrase p
  [Amendment_Rederivation_ST13_Phase3_2026-11-05.md:386]           ( spec l135) against august's lower mean (b, c; a conceded it as a record); the grazing residue at spec l122, l123 and l154, l122 
  [Amendment_Rederivation_ST13_Phase3_2026-11-05.md:404]           ( drl l1150), not canon. here it means the people who clear the ring's drift, a third use separate from the relay's upkeep crews a
  [Amendment_Rederivation_ST13_Phase3_2026-11-05.md:405]           the ring needs clearing, by people of either body; who clears it is not stated
  [Amendment_Rederivation_ST13_Phase3_2026-11-05.md:454]           to old l132, but live l154 (old l132) reads
  [Amendment_Rederivation_ST13_Phase3_2026-11-05.md:454]           old l183, excluded at step -1); a demoted row, nothing rests on it (a, c; b conceded). l202 cites rp l334 for

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```
**Triage by hand (each of the 20 misses read and classified):** 56 fragments tested, **20 not found** (0 in table cells, 20 in prose). **19 are connective prose** captured between two adjacent quotations on one line (the audit's own warning), or this piece's own wording on lines that also carry quotations: section 0 items 2 and 4 (L17, L19), section 2.1 (L210), section 3 (L234, twice), and the findings' text (L269, L292, L302, L328, L335, L342 twice, L386 four times, L404, L454 twice). **One is an exact quotation of reader B's Round 1 addendum** (L405: B's no-label form, `.t8_amend_ST13_readerB.md` L445); the audit's own-pass corpus reads the pass folder's `*.md` files and does not read dot-files, and the quotation was confirmed at its source line with `grep -nF` (merge checks below). **No misquotation was found by the audit.** This was the audit's only run on the piece. Before it, this merge's supplementary check (below) had flagged four strings: the four proposed wordings of piece section 7.4, which were this merge's own words in double quotation marks; they were set in italics without quotation marks, and two uses of the plain word for the found record's custodian were reworded (section "Settled in the merge"). **A supplementary check** of every double-quoted string in the piece of any length (a scratch script, `st13_merge/shortq.py`, normalizing dashes, quotes, markup, case and spaces, run with `python3 -I`) tested the piece's quoted strings against the Mirny folder's files **including the reader dot-files and the `Datasheets/` subfolder**, the rulings log, the runbook, the census, the extent file, the Founding Register, the relationship database, the Mirny spec, both robot files, the climate READER, the phase-spine file, the shadow discipline, the amendment-layer rules and the stereotypes law, **with this record excluded from the corpus**: **0 not found** (merge checks below). The audit was not re-run after this record was created. **Edits made to the piece after the audit (recorded, the recording law):** (1) a citation added on one line of AS13-16 (the cold file's lubricant line, `RCP` L82, which the draft had folded into L87 to L97); (2) the count of Phase 3 lines carrying old-frame figures, corrected on four lines (section 0 item 6, section 2.1's census list, section 3's C bullet, snag 11) after this merge searched Phase 3 for the old figures and found nine lines (L9, L61, L163, L203, L255, L256, L345, L371, L506) where the draft had repeated the readers' "at least seven". None adds a quotation or moves a line; the merge checks below were re-run after them with the same results.

## Merge checks
raw output (full; scripts in the session scratchpad `st13_merge/`, run with `python3 -I` on the final piece; the location-name scan's list is built from the spec file names, 37 names, and its positive control on a scratch text with three planted names found all three; names are not reproduced here):
```
$ python3 -I shortq.py ctl_piece.md   # positive control: two real quotations, one planted
  NOT FOUND L1: a planted control sentence for unit thirteen zq9 found nowhere
quoted strings tested: 3; files in corpus: 349; not found: 1
$ python3 -I shortq.py <the piece in the Mirny folder> <this record>   # the piece and this record are excluded from the corpus
quoted strings tested: 160; files in corpus: 348; not found: 0

$ grep -nF <the reader quotation the audit could not see> .t8_amend_ST13_readerB.md   # prints line:first 40 characters
445:- **(a) Old (L342):** "so **the ring

$ python3 -I checks.py city ctl_names.md   # positive control: three planted names
  hit L1 (name withheld, 5 chars)
  hit L1 (name withheld, 5 chars)
  hit L1 (name withheld, 8 chars)
== ctl_names.md: names scanned 37; hits 3
$ python3 -I checks.py city <piece>
== Amendment_Rederivation_ST13_Phase3_2026-11-05.md: names scanned 37; hits 0
$ python3 -I checks.py city <this record, before the check and sweep blocks were pasted>
== Amendment_Rederivation_ST13_Phase3_2026-11-05b_T8_Rounds.md: names scanned 37; hits 0
$ python3 -I checks.py city <the two Round 2 raw files>
== .t8_amend_ST13_round2_raw_FIRSTRUN.txt: names scanned 37; hits 0
== .t8_amend_ST13_round2_raw.txt: names scanned 37; hits 0

$ python3 -I checks.py ids <piece>   # reader Round 1 IDs (the mapping table's A, B, C columns and "its <ID>") excluded
AS13 cited  : 1 .. 33 (33 distinct)
AS13 headed : 1 .. 33 (33 distinct)
AS13 in mapping table (bold): 1 .. 33 (33 distinct)
cited but not headed: [] | cited but not in mapping: []
RF-ST13-: cited 1..10 (10 distinct); defined 1..10 (10 distinct); cited not defined: []
AR-2xx: cited 220..226 (7 distinct); defined 220..226 (7 distinct); cited not defined: []
AQ-2xx: cited 220..228 (9 distinct); defined 220..228 (9 distinct); cited not defined: []
DK13-: cited 1..33 (33 distinct); defined 1..33 (33 distinct); cited not defined: []
DEC-14x: cited 140..142 (3 distinct); defined - (0 distinct); cited not defined: [140, 141, 142]

$ python3 -I checks.py mix ctl_mix.md   # positive control: one mixed line, two mixed blocks
  line mix L2: old ['1,351,430'] live ['1,403,549']
line-level mixes: 1
  block mix ### AS13-99 · control: old ['1,351,430'] live ['1,403,549']
  block mix ### AS13-98 · control two: old ['665,901'] live ['692,971']
finding-block mixes: 2
docket rows carrying an old-frame figure: 0
$ python3 -I checks.py mix <piece>
line-level mixes: 0
finding-block mixes: 0
docket rows carrying an old-frame figure: 0

$ python3 -I checks.py keep <piece>
L403: ...- **Old.** "the ring has keepers" (L342)....
L406: ...- **Addendum (PROPOSED).** *2026-11-05: read the ring has keepers as the ring's clearers: the people of e...
L560: ...), this merge's own words:* ***Read Phase 3's 'the ring has keepers' as 'the ring's clearers', a role eithe...
occurrences of keeper/keepers: 3

$ wc -l <piece> <this record, before the check and sweep blocks were pasted>
599 Amendment_Rederivation_ST13_Phase3_2026-11-05.md
598 Amendment_Rederivation_ST13_Phase3_2026-11-05b_T8_Rounds.md
$ grep -c "^### AS13-" <piece>; grep -c "^| DK13-" <piece>
33
33
```
**Reading the checks:** the quotation check's control found its two real quotations (`P3` L236 and `DRL` L1219) and missed the planted one, as it should; the piece's quoted strings are all found with the piece and this record excluded from the corpus. B's no-label wording is at `.t8_amend_ST13_readerB.md` L445. No other location's name appears in the piece, in this record or in the two Round 2 raw outputs pasted above. Every AS13, RF-ST13, AR-22x, AQ-22x and DK13 number cited in the piece is defined, and every AS13 number is in the mapping table (piece section 1.4); the readers' own Round 1 IDs, which the mapping table cites, are excluded from that count by design; the three DEC-14x numbers are cited, not defined, because they are the Steps −1 to 3 piece's (DEC-140 to DEC-142), and no new DEC number is assigned. **No line, no finding block and no docket row carries both the old frame's and the live figures.** The coinage's three occurrences are listed by the keep check: the quoted pass text (L403), the addendum's reading note that names it (L406) and the decision's wording that quotes it (L560); no group is named by it. **Counts:** the piece has 33 findings (AS13-1 to AS13-33), 33 docket rows (31 marks, DK13-10 and DK13-13 empty), 7 requests (AR-220 to AR-226), 9 questions (AQ-220 to AQ-228), 10 reserved findings (RF-ST13-1 to RF-ST13-10) and 4 decisions proposed; **every reader item is mapped** (section 1.4 lists A's AS13-1 to AS13-23, B's AS13-1 to AS13-19 with its M-list, and C's AS13-1 to AS13-29; A's DK13-21, which had no AS item, maps to AS13-7); **every docket row is traced** to its finding by number (DK13-n to AS13-n).

## American English sweep
**Words checked** (the script's pattern, `st13_merge/ae_sweep.py`, the same as the Steps −1 to 3 piece's; named here by their American forms, so that listing them does not plant the British forms in this record): the -ize, -ized, -izes, -izing, -ization and -yze families written with an s (less an allow list of American words that end in -ise, such as premise, rise, otherwise, exercise and the forms of improvise); the British forms of color, behavior, center, centered, license, defense, offense, favor, honor, labor, neighbor and harbor with their forms; of organize, recognize, realize and finalize; of traveled, canceled, modeled and labeled with their -ing forms; of fulfill, enroll, gray, catalog, dialog, program, meter, liter and analog; and of toward, while, among, learned, spelled, dreamed, acknowledgment and aging. The script also counts the one British spelling the developer keeps without printing the word, so pasting this block does not change the count. Run with `python3 -I` on both files after every other section of this record was written; the final name scan is added at the end.

raw output, excerpted (14 lines omitted: the positive control's hit lines, which print the fourteen planted British spellings, so pasting them would put those spellings into this record; the control's summary lines are kept; the whole output of the control is reproducible from `st13_merge/ctl_ae.md`):
```
$ python3 -I ae_sweep.py ctl_ae.md   # positive control: fourteen planted British spellings, one planted kept spelling
== ctl_ae.md
British-spelling hits: 14
kept spelling (the one allowed British form): 1
$ python3 -I ae_sweep.py <piece> <this record>
== Amendment_Rederivation_ST13_Phase3_2026-11-05.md
British-spelling hits: 0
kept spelling (the one allowed British form): 1
== Amendment_Rederivation_ST13_Phase3_2026-11-05b_T8_Rounds.md
British-spelling hits: 0
kept spelling (the one allowed British form): 0
$ python3 -I checks.py city <piece>; python3 -I checks.py city <this record>   # a final name scan after the check block was pasted
== Amendment_Rederivation_ST13_Phase3_2026-11-05.md: names scanned 37; hits 0
== Amendment_Rederivation_ST13_Phase3_2026-11-05b_T8_Rounds.md: names scanned 37; hits 0
```
**Result:** no British spelling in either file; the one kept spelling occurs once, in the piece (section 5's confidence key); the record carries none. The control found all fifteen planted forms (fourteen hits and the kept one).
**Recorded (the recording law):** the block above was produced before this section was written. After it was written, a run on this record flagged 45 hits, all on one line: an earlier wording of the checked-words list above, which named the British forms themselves. The list was reworded to name the American forms, both files were swept again, and that run matched the block above exactly (`diff`, by this merge).
