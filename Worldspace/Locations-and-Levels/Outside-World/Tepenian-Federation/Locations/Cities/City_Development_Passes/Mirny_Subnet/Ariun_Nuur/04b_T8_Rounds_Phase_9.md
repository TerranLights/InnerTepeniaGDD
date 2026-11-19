# Ariun Nuur — ULM Phase 9 (populations) — T8 round record

**Unit:** Phase 9. **Written:** `04_Phase_09_Populations.md` (594 lines; PROPOSED, not declared complete). **Run mode:** WARM (`DR-6`).
**Date:** 2026-11-19; brief frozen and readers dispatched 12:19, Round 1 back by 12:40, Round 3 by 12:46, merge
returned 13:00, record 13:01.
**List:** `.t8_required_04_Phase9.txt` (22 entries). The runbook's Step 4 (cut), the spine's Phase 9, the universe's laws of robotics, the robot universals' chapters 13 and 14 (a line naming another location cut), the doll representation categories, the robot physiology file (whole; governing; its other-location lines national canon only), the spec, the earlier twelve outputs, the Phase 9 datasheet and `DR-143`. **Brief:** `.t8_brief_04_Phase9.md` (200
lines; built from the phase template; sha256[:16] 74efb027f36152b0). Reader outputs archived as `.t8_Phase9_reader{A,B,C}.md`; Round 3
replies as `.t8_Phase9_round3_reader{A,B,C}.md`. Three Opus readers; one fresh Opus merge writer (`M-246`).

## Round 1 — receipts (as returned)

| Reader | Lines | Axis | Findings | Asymmetry rows | Handed forward | Positions | RF · SH · REQ · Q | Handoff places | Manifest |
|---|--:|---|--:|--:|--:|--:|---|--:|---|
| A | 547 | ordered by arrival, billed by body | 24 | 14 | 4 | 1 | 4 · 1 · 3 · 5 | 89 | 22 of 22 |
| B | 622 | kind sets the bill; arrival order sets the place | 28 | 17 | 4 | 3 | 7 · 1 · 4 · 9 | 94 | 22 of 22 |
| C | 624 | kind sets the price; arrival sets the place | 36 | 14 | 4 | 3 | 9 · 2 · 5 · 8 | 102 | 22 of 22 |

## Round 2 — `Tools/triple_read_verify.py` (last commit `8777bb5f` 2026-11-03; clean), run 1, raw output whole

```
required files: 22
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2662-2694,2696-2698,2700-2729,2731-2759] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 1026-1100] ===
  agent1   ✅ all fields match ground truth
  agent2   ⛔ LLAST MISMATCH  claimed='---'  actual=''
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Laws_of_Robotics.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Characters/Robot-specific/Robot_Universals/3_-_Part_III_Robot_Cultural_Universals/13_City-Locality_as_the_Seat_of_Identity/README.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Characters/Robot-specific/Robot_Universals/3_-_Part_III_Robot_Cultural_Universals/14_Generational_Identity_-_Gen-Mark_as_Real_but_Non-Hierarchical/README.md  [range 1-11,13-29,31-67] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Doll_Representation_Categories.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/03_Research.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_02_Composition_and_Arrival.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_03_Surface_and_Texture.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_04_Ordinary_Life.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_05_Relation_and_Geometry.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_06_Meaning.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_07_Order.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_08_Making.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/Datasheets/Phase_9.md ===
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

**What failed, confirmed at source:** reader B's LLAST for the spine (range 1026–1100) gave L1099 (`---`) for L1100, which is blank. B's first version kept as `.t8_Phase9_readerB_prerepair.md`; B corrected that field only (diff: L460).

**Run 2, raw output whole:**

```
required files: 22
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2662-2694,2696-2698,2700-2729,2731-2759] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 1026-1100] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Laws_of_Robotics.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Characters/Robot-specific/Robot_Universals/3_-_Part_III_Robot_Cultural_Universals/13_City-Locality_as_the_Seat_of_Identity/README.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Characters/Robot-specific/Robot_Universals/3_-_Part_III_Robot_Cultural_Universals/14_Generational_Identity_-_Gen-Mark_as_Real_but_Non-Hierarchical/README.md  [range 1-11,13-29,31-67] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Doll_Representation_Categories.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/03_Research.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_02_Composition_and_Arrival.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_03_Surface_and_Texture.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_04_Ordinary_Life.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_05_Relation_and_Geometry.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_06_Meaning.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_07_Order.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_08_Making.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/Datasheets/Phase_9.md ===
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

**Fixes after Round 3:** readers B and C found that reader A's PROOF block for the laws of robotics carries a national demonym on a positional line with no EXEMPT line (standing line 5), and that A's reading log reproduced the demonym. A added the EXEMPT line and masked the demonym in its log (diff: L7, one added line; no PROOF field changed). A's version before the fixes is kept in the scratchpad only, not in the pass folder, because its log carries the unmasked demonym.

**Run 3, raw output whole — UNANIMOUS:**

```
required files: 22
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2662-2694,2696-2698,2700-2729,2731-2759] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 1026-1100] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Laws_of_Robotics.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Characters/Robot-specific/Robot_Universals/3_-_Part_III_Robot_Cultural_Universals/13_City-Locality_as_the_Seat_of_Identity/README.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Characters/Robot-specific/Robot_Universals/3_-_Part_III_Robot_Cultural_Universals/14_Generational_Identity_-_Gen-Mark_as_Real_but_Non-Hierarchical/README.md  [range 1-11,13-29,31-67] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Doll_Representation_Categories.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/03_Research.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_02_Composition_and_Arrival.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_03_Surface_and_Texture.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_04_Ordinary_Life.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_05_Relation_and_Geometry.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_06_Meaning.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_07_Order.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_08_Making.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/Datasheets/Phase_9.md ===
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

**All six CONSISTENT.** Reader A again read only part of each other output first (its context), stated its scope, and finished on request; its addendum, saved with its reply, keeps both verdicts. One demonym quoted in A's reply is masked in the saved copy (noted in its header). Settled for the merge: robot smell is written nationally in the physiology file (L448; B withdrew); neither body is self-sufficient outdoors and no preference for robot rescuers is written; no ranking of which body pays more at the stop; the human no-return exclusion is national context; no comparison with an unnamed elsewhere; the Lover (position) and the Parent are not marked here (contested, asked). The (c) points became Q-184 to Q-203. Filed as `DEC-865` to `DEC-884`.

## Procedural events (the recording law)

1. **Round 2, run 1** failed on one field (reader B), repaired; **run 2** UNANIMOUS (66/66). After Round 3, reader A's two rule fixes changed its file, so Round 2 was re-run: **run 3** UNANIMOUS (66/66). The exact-field check found the run-1 defect too and nothing after (`.t8_Phase9_exact_fields.txt`, run before the repair).
2. **Reader A's partial Round 3 read** (second unit running): A read B to L460 and C to L440, stated it, and finished on request. A method note for after the run: Round 3 on long outputs can run out of a reader's context.
3. **An orchestrator slip, corrected:** A's pre-fix version was copied into the pass folder for the archive, then found to carry the unmasked demonym in its log. A delete was refused by the project's hook (it blocks `rm`); the copy was moved back to the scratchpad instead. No other file touched.
4. **The merge writer** re-read Phase 2 L150–209 to settle what Phase 2 FIND-P2-19 charges each body (split 4) and created no other file.

## Quotation checks, before this record existed

**Pre-check (T8 line 13), per quotation, normalized.** First run, raw:

```
quoted strings checked: 0 not found: 0
04_Phase_09_Populations.md British-form hits: []
other-location name scan (names: line numbers): {}
tower-name count: 0
```

**Triage:** no quotation-marked strings in the file.

**`Tools/quotation_audit.py`** (last commit `5a63e074` 2026-11-02; clean), `--phase 9 --own-pass`. Whole output saved beside this record
as `.t8_Phase9_quotation_audit.txt`; result block, raw:

```
=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 0
NOT FOUND in corpus: 0
  of those, in TABLE CELLS : 0
  of those, in PROSE       : 0


⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```

**Triage:** no fragment tested. **Confirmed defects: 0.**

## Phase-close instruments (raw output whole)

**`Tools/handoff_audit.py`** (T1):

```
pass audited : Ariun_Nuur
phase files  : 8

=== CONTROLS (edit these per pass; they are what makes a zero trustworthy) ===
  PHASES WITH A FORMAL SWEEP BLOCK (found in this pass): 2, 3, 4, 5, 6, 7, 8, 9
  PHASES WITH NO TRACE OF A SWEEP (found in this pass)  : none
  SELF-TEST (fixed positive and negative strings)       : passed
  INSTRUMENT VALID: YES - the detector separates a formal block from no block on the built-in controls

  phase | outbound | sweep    | rows | verdict
  ------+----------+----------+------+---------
      2 |        0 | FORMAL   |    0 | n/a - nothing addressed to it
      3 |        1 | FORMAL   |    0 | *** BLOCK EMPTY ***
      4 |        2 | FORMAL   |    0 | *** BLOCK EMPTY ***
      5 |        3 | FORMAL   |  166 | reconcile 166 enumerated against 3 outbound
      6 |        2 | FORMAL   |   33 | reconcile 33 enumerated against 2 outbound
      7 |        3 | FORMAL   |   86 | reconcile 86 enumerated against 3 outbound
      8 |        2 | FORMAL   |   49 | reconcile 49 enumerated against 2 outbound
      9 |        7 | FORMAL   |  111 | reconcile 111 enumerated against 7 outbound

TOTAL outbound handoff rows: 28
PHASES WITH ROWS ADDRESSED TO THEM AND NO ENUMERATION: 2

=== outbound rows, per target, for hand reconciliation ===
  -> Phase 3:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 3** | the founding wave's specialization, its criterion and its losing side (R
  -> Phase 4:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 4** | whose ordinary day: the arrival layers (founding-wave descendants, later
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 4** | the street register as the general answer, for whose ordinary day (FIND-
  -> Phase 5:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 5** | who the visitor is: Hwy 37 as the only written route of arrival, departu
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 5** | first impressions as the city's arrival texture (FIND-P3-34 to FIND-P3-4
       [04_Phase_04_Ordinary_Life.md]  | **Phase 5** | the supply window and the forecast, and Hwy 37's seasons (FIND-P4-16; re
  -> Phase 6:
       [04_Phase_04_Ordinary_Life.md]  | **Phase 6** | the keepers' off-rhythm day (FIND-P4-8, FIND-P4-42); whoever keeps her o
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 6** | the outsider senses that are conditions (FIND-P5-34): the newcomer not y
  -> Phase 7:
       [04_Phase_04_Ordinary_Life.md]  | **Phase 7** | any rule protecting rest where the work never stops, limiting outdoor st
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 7** | any rule of travel on Hwy 37 in a seasonal closure, if it holds (FIND-P5
       [04_Phase_06_Meaning.md]  | **Phase 7** | any rule, priority or prohibition the contract or the failure would need
  -> Phase 8:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 8** | composition established: the origin stocks as admissible, composition-gr
       [04_Phase_07_Order.md]  | **Phase 8** | the people the place's demand does not fit, as persons, never groups (FI
  -> Phase 9:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 9** | which populations exist: 25 rows, both bodies at their own counts, the h
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 9** | the sensory split by body: breath, thin air and smell for humans; capaci
       [04_Phase_04_Ordinary_Life.md]  | **Phase 9** | the two bodies' days (FIND-P4-44); the human night at about 3,900 m by m
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 9** | the arrival types by body and route, and their unsized layers, the resea
       [04_Phase_06_Meaning.md]  | **Phase 9** | who the contract's two layers reach and who they do not (FIND-P6-8, FIND
       [04_Phase_07_Order.md]  | **Phase 9** | who is present by function and body: the night's keepers and how many (h
       [04_Phase_08_Making.md]  | **Phase 9** | food by body: siligel and charge from the supply and the shipment for th
  -> Phase 10:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 10** | the district's honor of the city's own scientists (FIND-P2-37); the fou
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 10** | the named structures and their texture: the shaft as an interior kept f
       [04_Phase_04_Ordinary_Life.md]  | **Phase 10** | the charge night and the clock as the day's frame, and the warm stop as
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 10** | the road's name (the Mountain Cut Throughway), the waypoint, its outpos
       [04_Phase_06_Meaning.md]  | **Phase 10** | the district's honor, the city's own half as the ground (FIND-P6-3; swe
       [04_Phase_07_Order.md]  | **Phase 10** | the decisions that fall on unnamed parties, as candidate places or name
       [04_Phase_08_Making.md]  | **Phase 10** | the named things of making, as candidates only, PROPOSED: the inherited
       [04_Phase_09_Populations.md]  | **Phase 10** | the demonym slot, still open (RF-13), no population named; any naming o
```

**`Tools/phase_discipline_check.py`** (T3, T4, T5), run before the ledger was updated:

```
pass audited : Ariun_Nuur

=== T3 - POSITION-COVERAGE LEDGER ===
  phases in header: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Child              filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Lover (position)   filled=1  blank=8   blank at: P3, P4, P5, P6, P7, P8, P9, P10
  The Parent             filled=1  blank=8   blank at: P3, P4, P5, P6, P7, P8, P9, P10
  The Ruler              filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Elder              filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Mentor             filled=6  blank=3   blank at: P3, P9, P10
  The Passer-Through     filled=3  blank=6   blank at: P4, P6, P7, P8, P9, P10
  The Neighbor           filled=1  blank=8   blank at: P2, P3, P4, P6, P7, P8, P9, P10
  ⭐ The Lover FACULTY    filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10

  NOTE: a blank cell is a WARNING BEFORE Step 8, not a defect. Do not
  fill a blank by writing new phase content toward it - that is the
  contamination 00f Rule 3 forbids (see the recipe's hard bound on T3).

=== T4 - PER-PHASE SHED MARKER ===
  [04_Phase_02_Composition_and_Arrival.md]  T4 present: the origin stocks' own cultures, the per-row decimals and headcounts below the tier, the l
  [04_Phase_03_Surface_and_Texture.md]  T4 present: the composition's rows, tiers, stocks and decimals, the language blocs, the census arithme
  [04_Phase_04_Ordinary_Life.md]  T4 present: the composition's rows, tiers, decimals and origin shares, the founders' share beyond its 
  [04_Phase_05_Relation_and_Geometry.md]  T4 present: the composition's rows, tiers and decimals, the language blocs, the census-kinship reasoni
  [04_Phase_06_Meaning.md]  T4 present: the climate cells beyond the cold that punishes stopping, the industry figures and the Man
  [04_Phase_07_Order.md]  T4 present: the composition's rows, tiers, decimals and per-row headcounts beyond the two bodies, the 
  [04_Phase_08_Making.md]  T4 present: the industry tiers beyond the food term, the baseline, the robot term and the Other 10%, t
  [04_Phase_09_Populations.md]  T4 present: the per-row decimals and headcounts below the two bodies, beyond the largest row and the f

  8/8 phase files carry a T4 marker.
  >> If EVERY phase's answer was literally 'nothing', T4 is falsified
     per its own stated condition (the question would be decorative).
     This tool cannot see the marker's CONTENT well enough to judge
     that - read the 8 lines above by hand.

=== T5 - EARLY LOVER-FACULTY SMOKE TEST ===
  EARLY (Phase 6) verdict: alive, yes; lovable, not yet shown. It is alive in a hard way: everyone who comes is kept and taught by the one before, told where it is safe to stop, and what you know outlives you only if you give it away. Someone could be loyal to it and grateful to it before the files give anyone a reason to love it: no child, no elder, no grave and no pleasure in a stopped hour is written yet, the one beauty given is the air's glitter in the light season (Phase 3 FIND-P3-37), and what people do with the warmth waits for the CST. (Split 10: reader C's wider verdict, lovable for its seriousness and its debt, is not written.)
  LATE marker absent (08_Review_Panel.md missing or has no 'T5 - LATE LOVER FACULTY:' line yet)

  T5 not fully applied this pass (one or both markers absent).
```

**Ledger:** P9 marked for the Mentor; the Lover (position) and the Parent left unmarked (contested; Q-189).

## American English sweep and the one-location check

From the pre-check script's last lines, raw, above: no British form; the name scan's hits, if any, are the parent subnet and the pass
folder's path; the tower's name 0. **No other location named.**

## Tokens (from the task notifications; full rows in `Universal_Location_Methodology/TOKEN_LOG_Ariun_Nuur.md`)

| Agent | Round 1 | Round 3 (delta) | Last figure |
|---|--:|--:|--:|
| reader A | 800,371 | 108,860 (first part 87,946 · addendum and fixes 20,914) | 909,231 |
| reader B | 838,844 | 99,225; repair 229 | 938,298 |
| reader C | 833,851 | 96,558 | 930,409 |
| merge writer | — | — | 294,890 |
| **Unit total (sum of last figures)** | | | **3,072,828** |

Web calls: readers 0; `Tools/web_quota_count.py`: TOTAL 284 (unchanged).
**The record grows after this check** (T8 line 8): no DOUBLE-CHECK script was run on this record.
