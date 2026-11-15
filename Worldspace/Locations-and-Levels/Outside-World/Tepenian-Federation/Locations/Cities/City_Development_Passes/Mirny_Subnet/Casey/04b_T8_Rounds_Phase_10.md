# Round record — Casey · Step 4, Phase 10 (Catalog)

**Output:** `04_Phase_10_Catalog.md` (647 lines) and Session 6 of `Cities/Research_Logs/Casey_Research_Log.md` (appended, 148 lines; the log now 1,357 lines). Casey's warm ULM run under `STARTUP_Mirny_Review_then_Casey_ULM_2026-11-11.md` Part B item 3: three readers, Round 2, Round 3, one fresh merge writer (`M-246`), the quotation audit run before this record existed, the American English sweep, the handoff audit and the phase discipline check. Every tool output below is pasted whole. PROPOSED; nothing declared complete.

## Round 0 — the reading list and the frozen briefs

Briefs `.t8_04_Phase_10_brief_A.md`, `_B.md`, `_C.md` (192 lines each; written new for Casey from the runbook, the spine and the earlier briefs on disk; standing lines 1–6, 10, 11 verbatim; A and B differ only in the slot, checked by `diff`; brief C's §1 read before dispatch; the symbol entries and their note added only after Phase 9 was written, `DR-8`). Merge brief `.t8_04_Phase_10_merge_brief.md`. List decisions: Casey's log CL-40. The list, `.t8_required_04_Phase_10.txt` (38 entries):

```
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md :: 82-272,1101-1188
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md :: 378-426,1760-1830,1966-2041,2076,2320-2361,2645-2758
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Characters/Enneagram_Character_Index.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Zodiac_Signs_Full_Attributes.md :: 1-5,11-264
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Corpus_Reference_Sheets/Zodiac_Signs_Quick_Reference.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/01_Aries.md :: 8-10,12-13,46-49
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/02_Taurus.md :: 8-9,28-29
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/03_Gemini.md :: 6-8,10-12,59-69
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/04_Cancer.md :: 6,8,41
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/05_Leo.md :: 6-8,40-41
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/06_Virgo.md :: 9-13,15-16,18,67-69,71,75-76
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/07_Libra.md :: 6,32-33
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/08_Scorpio.md :: 6-8,47-51,54
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/09_Sagittarius.md :: 6-10,39-42
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/10_Capricorn.md :: 10-15,66-68,70-71
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/11_Aquarius.md :: 6-11,61-68
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/12_Pisces.md :: 10-11,13-15,63-64,66,68,71-76
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Casey.md :: 1-3,5-83,85,87-93,95-107,110,112-121,125-152,154-155,157-159,166-170,172,174-180,182,184,186,188-200,202,204-207,212-214,243-244,248-249
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Casey_Inspiration_Place_Research_R1.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Casey_Inspiration_Place_Research_R2.md
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
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_07_Order.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_08_Making.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_09_Populations.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/Datasheets/Phase_10.md :: 1-2,6-11,14-15,17-20
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md :: 203-215,386-421,1707-1715,1989-1996
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Symbolic_Substrate/Planetary_Symbols.md :: 1-104,106-108,110-203
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Symbolic_Substrate/Robot_Elementals.md
```

## Round 1 — three readers, each in a private staging folder

Dispatched 2026-11-15 11:38, three Opus readers, one message: A `ad999b82ba28da168`, B `aedb7fa2f91c04a3d`, C `a43066bb276a94424`; staging `scratchpad/casey/phase10/reader<X>/`. Outputs copied into Casey's folder after Round 2 (standing line 9).

| Reader | Output | Lines | Findings | Handed forward | Developer questions | Web calls |
|---|---|--:|--:|--:|--:|--:|
| A | `.t8_04_Phase_10_readerA.md` | 683 | 38 | 6 | 4 | 10 (6 searches, 4 fetches) |
| B | `.t8_04_Phase_10_readerB.md` | 644 | 36 | 5 | 3 | 10 (6 searches, 4 fetches) |
| C | `.t8_04_Phase_10_readerC.md` | 646 | 31 | 4 | 4 | 9 (5 searches, 4 fetches) |

*The counts are as each reader reported them in its reply; the line counts are `wc -l` on the copied files.*

## Round 2 — `Tools/triple_read_verify.py` (last change 2026-11-03), raw output, whole (195 lines; `.t8_04_Phase_10_round2_raw.txt`)

```
required files: 38
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 82-272,1101-1188] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 378-426,1760-1830,1966-2041,2076,2320-2361,2645-2758] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Characters/Enneagram_Character_Index.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Zodiac_Signs_Full_Attributes.md  [range 1-5,11-264] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Corpus_Reference_Sheets/Zodiac_Signs_Quick_Reference.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/01_Aries.md  [range 8-10,12-13,46-49] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/02_Taurus.md  [range 8-9,28-29] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/03_Gemini.md  [range 6-8,10-12,59-69] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/04_Cancer.md  [range 6,8,41] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/05_Leo.md  [range 6-8,40-41] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/06_Virgo.md  [range 9-13,15-16,18,67-69,71,75-76] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/07_Libra.md  [range 6,32-33] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/08_Scorpio.md  [range 6-8,47-51,54] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/09_Sagittarius.md  [range 6-10,39-42] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/10_Capricorn.md  [range 10-15,66-68,70-71] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/11_Aquarius.md  [range 6-11,61-68] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/12_Pisces.md  [range 10-11,13-15,63-64,66,68,71-76] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Casey.md  [range 1-3,5-83,85,87-93,95-107,110,112-121,125-152,154-155,157-159,166-170,172,174-180,182,184,186,188-200,202,204-207,212-214,243-244,248-249] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Casey_Inspiration_Place_Research_R1.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Casey_Inspiration_Place_Research_R2.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_07_Order.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_08_Making.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/04_Phase_09_Populations.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/Datasheets/Phase_10.md  [range 1-2,6-11,14-15,17-20] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 203-215,386-421,1707-1715,1989-1996] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Symbolic_Substrate/Planetary_Symbols.md  [range 1-104,106-108,110-203] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Symbolic_Substrate/Robot_Elementals.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

## Round 3 — each reader continued by `SendMessage` with the other two outputs

Messages built from `scratchpad/casey/tools/phase10_round3_template.txt` (sections 1–4 per reader; 5 dispositions; 6 figures recomputed; 7 T3 marks; 8 the `T4 - SHED:` line; 9 web calls, up to 10 each). Sent 2026-11-15 12:14. Replies saved the moment each arrived (standing line 9):

| Reader | Reply | Lines | Verdict lines, as written in the reply (cut at the reason) | Web calls |
|---|---|--:|---|--:|
| A | `.t8_04_Phase_10_round3_readerA.md` | 211 | VERDICT: CONSISTENT · VERDICT: CONSISTENT | 3 |
| B | `.t8_04_Phase_10_round3_readerB.md` | 125 | VERDICT: CONSISTENT  · VERDICT: CONSISTENT  | 2 |
| C | `.t8_04_Phase_10_round3_readerC.md` | 302 | VERDICT: CONSISTENT · VERDICT: CONSISTENT | 0 |

**Verdicts: all six CONSISTENT.** Each reply carries sections 5 to 9 and one `T4 - SHED:` line (checked with `grep -c`).

## The merge — one fresh writer (`M-246`)

Dispatched 2026-11-15 12:24 after Round 3: `a1bfcd1feca7f8087` (Opus). Returned `04_Phase_10_Catalog.md` (647 lines; P10-1 to P10-49; 46 inbound sweep rows; 9 HANDED FORWARD rows plus 4 items carried outside the pass; DQ-29 to DQ-34; no new request, reserved finding or provisional assumption; the `T4 - SHED:` line at L540) and Session 6 of the research log (34 call rows; OT-85 to OT-92). `git diff --numstat` on the log against the last commit: `835 0` (Sessions 2 to 6, insertions only).

## Research-log strings against the readers' own tables — `scratchpad/casey/tools/check_session6_strings.py` (written this morning), raw output, whole (2 lines; `.t8_04_Phase_10_log_strings_raw.txt`)

```
rows 34 · verbatim found 34 · missing 0
per reader/round: A-R1 10 A-R3 3 B-R1 10 B-R3 2 C-R1 9
```

## Normalized quotation pre-check (standing line 13) — `scratchpad/casey/tools/quote_precheck.py` (written this morning), raw output, whole (1 lines; `.t8_04_Phase_10_quote_precheck_raw.txt`)

```
quoted strings (2+ words): 32 · found 32 · not found 0
```

## Quotation audit — `Tools/quotation_audit.py` (last change 2026-11-02), `--files 04_Phase_10_Catalog.md --own-pass`, raw output, whole (29 lines; `.t8_04_Phase_10_quotation_audit_raw.txt`)

```
pass audited : Casey
corpus mode  : default (own pass excluded)
corpus files : 7119   chars: 115,167,823
files audited: 04_Phase_10_Catalog.md
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
fragments tested (single-line, ellipsis-split, >=7 words): 15
NOT FOUND in corpus: 3
  of those, in TABLE CELLS : 0
  of those, in PROSE       : 3

  [04_Phase_10_Catalog.md:353]           ( 04 phase 06 l311; s2-25). whoever is not on the last ship stays seven months; the last days are spent counting the store; the ha
  [04_Phase_10_Catalog.md:430]           (elementals l118) as contradicting a city made from the hold; c records a fit, its duration
  [04_Phase_10_Catalog.md:514]           (frame l252). phase 7 separately writes, as an expression of its mandate trade (soc 43-5000)

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```

**Triage of the misses** (orchestrator; table `.t8_04_Phase_10_quotation_triage.md`): 3 misses: 3 CONNECTIVE, 0 WRAP, 0 DOT, 0 SELF, **0 MISQUOTE**. The audit does not read dot-files, so quotations of the readers' outputs and replies are checked by no tool except the pre-check above.

## American English sweep — a pattern of British forms (`scratchpad/casey/tools/ame_pattern.txt`), over the phase file and the log's Session 6, raw output, whole (22 lines; `.t8_04_Phase_10_ame_sweep_raw.txt`)

```
== 04_Phase_10_Catalog.md
93:raised
95:raised
130:raised
130:Raised
160:rises
180:raised
180:raised
291:raised
292:Raised
294:raised
294:raised
353:judgement
508:raised
509:raised
513:Raised
558:raised
== Casey_Research_Log.md (Session 6, from L1210)
1238:raised
1311:raised
1341:Raised
1349:raised
```

**Hits:** "judgement" once (L353, inside a quotation of `04_Phase_07` L371; the one British form the project keeps); the rest are false positives of the `-ise` pattern (raised, rises). 0 British forms.

## Handoff audit — `Tools/handoff_audit.py` (last change 2026-10-21), raw output, whole (118 lines; `.t8_04_Phase_10_handoff_audit_raw.txt`)

```
pass audited : Casey
phase files  : 9

=== CONTROLS (edit these per pass; they are what makes a zero trustworthy) ===
  PHASES WITH A FORMAL SWEEP BLOCK (found in this pass): 2, 3, 4, 5, 6, 7, 8, 9, 10
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
      8 |        8 | FORMAL   |   23 | reconcile 23 enumerated against 8 outbound
      9 |       21 | FORMAL   |   50 | reconcile 50 enumerated against 21 outbound
     10 |        6 | FORMAL   |    4 | reconcile 4 enumerated against 6 outbound

TOTAL outbound handoff rows: 85
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
       [04_Phase_08_Making.md]  | **Phase 9** | The robot body in Casey's cold, as making meets it: whether robot skin a
       [04_Phase_08_Making.md]  | **Phase 9** | The robot speaker: exile-era robots as long-lived carriers of languages 
       [04_Phase_08_Making.md]  | **Phase 9** | The robot half as tended bodies through the shut half: robot-care worker
       [04_Phase_08_Making.md]  | **Phase 9** | The music listener: the direction of the robots' wider hearing (DQ-14; R
       [04_Phase_08_Making.md]  | **Phase 9** | The coat's two stakes as a population fact: robots whose outdoor work is
  -> Phase 10:
       [04_Phase_03_Surface_and_Texture.md]  | **Phase 10** | Naming places from what they look like: scoured crests, lee drifts, whi
       [04_Phase_05_Relation_and_Geometry.md]  | **Phase 10** | Names for the junction's legs, the turn inland, the harbor, the waiting
       [04_Phase_06_Meaning.md]  | **Phase 10** | Names of places for the warm room, the waiting room and the node, only 
       [04_Phase_07_Order.md]  | **Phase 10** | Names of places and roles the order produces (the warm stopping place, 
       [04_Phase_08_Making.md]  | **Phase 10** | Names for made things and places (the door, the store, the stopping pla
       [04_Phase_09_Populations.md]  | **Phase 10** | Character work from these populations, as roles only, never names (RF-2
```

## Phase discipline check — `Tools/phase_discipline_check.py` (last change 2026-10-21), raw output, whole (41 lines; `.t8_04_Phase_10_phase_discipline_raw.txt`)

```
pass audited : Casey

=== T3 - POSITION-COVERAGE LEDGER ===
  phases in header: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Child              filled=3  blank=6   blank at: P3, P5, P6, P7, P8, P10
  The Lover (position)   filled=4  blank=5   blank at: P3, P5, P7, P8, P10
  The Parent             filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Ruler              filled=1  blank=8   blank at: P2, P3, P4, P5, P6, P8, P9, P10
  The Elder              filled=6  blank=3   blank at: P3, P5, P10
  The Mentor             filled=3  blank=6   blank at: P3, P4, P5, P6, P8, P10
  The Passer-Through     filled=8  blank=1   blank at: P10
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
  [04_Phase_08_Making.md]  T4 present: the content of the 42 origin stocks and every composition share beyond the two bodies and 
  [04_Phase_09_Populations.md]  T4 present: the content of the 42 origin stocks and every composition share beyond the two bodies, the
  [04_Phase_10_Catalog.md]  T4 present: the open half as a life of its own, the five navigable months of ships, the harbor's seaso

  9/9 phase files carry a T4 marker.
  >> If EVERY phase's answer was literally 'nothing', T4 is falsified
     per its own stated condition (the question would be decorative).
     This tool cannot see the marker's CONTENT well enough to judge
     that - read the 9 lines above by hand.

=== T5 - EARLY LOVER-FACULTY SMOKE TEST ===
  EARLY (Phase 6) verdict: Alive, yes: Phases 2 to 6 show a city of two bodies whose one unwritten obligation is a warm night for whoever is inside, strangers held by the ice included, kept in every month and broken only where nobody can see; whether anyone could love it, rather than rely on it, is not yet answerable, because no admitted line writes what any resident cherishes or feels for Casey, and its culture material opens only at Step 5.
  LATE marker absent (08_Review_Panel.md missing or has no 'T5 - LATE LOVER FACULTY:' line yet)

  T5 not fully applied this pass (one or both markers absent).
```

*The T3 rows above were printed before the ledger's P10 column was marked; the ledger was updated right after (see Notes).*

## Notes

**Handoff audit, reconciled by hand.** Inbound: the tool sees 6 rows addressed `**Phase 10**` and counts 4 rows in the sweep block by its own pattern; the phase file's sweep enumerates 46 rows, and all six addressed rows are in it (its rows 1, 3, 4, 6, 7 and 9; checked with `grep` over the block). Outbound: the file's HANDED FORWARD table holds 9 rows, all to Steps (5, 7, 8, 10), outside the tool's form, plus 4 items carried outside the pass.

**Position-coverage ledger (T3).** The P10 column of `00.2_Position_Coverage_Ledger.md` was copied by the orchestrator from the phase file's `## T3 · Position coverage` (L524-538), with one deliberate difference: **The Parent is left blank in the ledger although the file marks it "Covered, thinly"**, because the mark rests on one reader's own output and the same cell says no parent's standpoint is written (L532); the conservative reading under the merge rule is blank (CL-41). Marked: The Child, The Lover *(position)* (thinly), The Ruler, The Elder, The Mentor, The Passer-Through, The Neighbor (relation only); the Lover FACULTY blank.

**The symbol determination** went to the developer as DQ-29 (DEC-539): Mars, the incumbent, was reserved by no reader after reading Phases 2 to 9, so it is not confirmed; all three reserved the Asteroid Belt and chose Air. The assignments file was read by the orchestrator only, after Phase 9 was written; its `Why` column was never given to a reader.

**Developer questions** DQ-29 to DQ-34 filed as DEC-539 to DEC-544 in `Research_Logs/DECISIONS_NEEDED_FROM_DEVELOPER.md` (the Casey section, above `## Answered`). No new provisional assumption.

**Web calls:** 29 in Round 1 and 5 in Round 3 (34), every one logged verbatim in the research log's Session 6 and checked against the readers' own tables (34 of 34). Session web total after the merge: WebSearch: 119 | WebFetch: 111 | TOTAL: 230 (`Tools/web_quota_count.py`; it counts one call more than the readers' 34 over the 195 before this phase, unexplained; it also names one transcript, the Phase 9 merge writer's, as mentioning a quota or rate-limit error, which that writer, making no web calls, cannot have hit; recorded, not chased).

**Readers' staging folders and one snag:** B and C hold their output, their Round 3 reply and a notes file; A holds those and three body-part drafts of its own output. **Reader A wrote a read-only PROOF checker at `scratchpad/casey/phase10/checkA/verify.py`, outside its staging folder; the hook blocked its deletion; it stays in place (the scratchpad, never the repo), and the orchestrator does not work around the hook.**

