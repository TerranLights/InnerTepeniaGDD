# Mirny · Amendment re-derivation · Piece ST7b (the Step 7 QA re-run on the applied text) · T8 round record · 2026-11-09

**Companion to** `Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md`. Raw tool output is pasted, not summarized; where a block is not the whole output it is headed as excerpted. Working files are in this folder as `.t8_amend_ST7b_*`, `.t8_amend_ST7bD_*`, `.t8_required_amend_ST7b.txt` and `.t8_required_amend_ST7bD.txt`. No other location is named in this record.

## Setup
- **The run and its hours.** The developer approved the corrections on 2026-11-08 and had them applied in three batches the same day, then ordered the Step 7 QA re-run, the fresh Review Panel and the Step 10 re-run, each written to file before the next starts (`DRL` L1877 items 1 and 4). When the orchestrator said those three would start the next morning, the developer answered "do those three items now" (`DRL` L1876); that instruction "overrides the derivation-hours rule (05:00-14:59) for this run only" (`DRL` L1877 item 5). **The run therefore started late:** the list was frozen at 14:21 and the brief at 14:22, the readers were dispatched at 14:22 (the checkpoint's second line), and every later stage (C's output at 15:03, the gap read, Round 3, this merge) ran after 14:59 under that override. No reader's output depends on the clock (brief result (8)).
- **Reading list (trimmed, `DR-74`):** `.t8_required_amend_ST7b.txt` (byte-identical to the scratchpad copy `amend_ST7b/t8_required_amend_ST7b.txt` by `cmp`), **58 entries, 17,492 admitted lines** (counted by this merge's scratch script: whole files by their physical lines at merge time, spans by their ranges). The rules (the stereotypes law; the phase-spine and generators spans; the two disciplines; the rulings log at 26 spans); the live sources at Mirny's rows only (the climate READER, both robot files, the spec at 29 spans, 219 lines, the Founding Register, the relationship database, the immigration composition file, the language blocs); **the object, read whole:** Step 7 (entry 15), the Step 7 piece (16), the sixteen pass files (17 to 32), the seven datasheets (33 to 39) and the culture file (40); the amendment layer (entries 41 to 58).
- **Gap list:** `.t8_required_amend_ST7bD.txt` (byte-identical to the scratchpad copy by `cmp`), **25 entries, 5,865 admitted lines:** the stereotypes law, the phase-spine spans, the spec, rulings-log, Register, relationship-database, immigration and language-bloc spans, Step 5 and Step 6 whole, the Phase 6, 7, 2 composition, 9 and 8 pieces and the Idelsk-Uralia piece whole, the amendment register whole, the 2026-11-03 note's L1 to L120, the Phase 10 and Step 5 pieces' L1 to L60, Step 7's L1 to L205, the Frame's three spans, the Phase 8 dockets, the robot-term piece's L1 to L30 and the answers note.
- **Briefs:** `.t8_amend_ST7b_brief.md`, identical for A, B and C with `{X}` the reader letter, **sha256[:16] ca4a7e5fa03a9d73** (computed by this merge on the folder copy; the scratchpad copy is byte-identical by `cmp`); it carries eight orchestrator-verified results with sources, the developer's binding words, the stage order, twelve traps and six standing lines. D's brief `.t8_amend_ST7bD_brief.md`, **sha256[:16] 598b845e14169c9d** (byte-identical to the scratchpad copy).
- **Readers:** three Opus agents for Round 1, A `a44bc2ecdd12d1fa6`, B `a04eeb98eba941505`, C `aa11f19221b79217c` (checkpoint, 14:22 line); outputs time-stamped 14:54 (A), 15:00 (B) and 15:03 (C) in the scratchpad. **Gap reader D** `abcf372d62ff41d45`, dispatched after Round 2 (checkpoint, 15:05 line), output 15:26; D saw none of A's, B's or C's output, and they saw none of D's. **None refused any entry** (each reading log). Graphify: not used by any reader.

| Reader | Output lines | Bytes | PROOF blocks | Findings (Round 1 numbering) | Docket | Requests · questions · RFs |
|---|--:|--:|--:|---|---|---|
| A | 1,560 | 197,063 | 58 | AS7b-1 to AS7b-34 | D7b-1 to D7b-8 | AR-280 to AR-283 · AQ-280 to AQ-283 · RF-ST7b-1 to RF-ST7b-3 |
| B | 1,485 | 196,752 | 58 | AS7b-1 to AS7b-19 | DK7b-1 to DK7b-9 | AR-280 to AR-284 · AQ-280 to AQ-285 · RF-ST7b-1 to RF-ST7b-4 |
| C | 1,707 | 211,036 | 58 | AS7b-1 to AS7b-14 | D7b-1 to D7b-6 | AR-280 to AR-284 · AQ-280 to AQ-285 · RF-ST7b-1 to RF-ST7b-4 |
| D | 698 | 82,531 | 25 | AS7bD-1 to AS7bD-16 | (proposed texts inside the findings) | AR-290 to AR-293 · AQ-290 to AQ-294 |

Line and byte counts by `wc` on the folder copies, each byte-identical to its scratchpad copy (`cmp`); PROOF blocks counted by `grep -c '^### PROOF:'`. No reader proposed a DEC number.
- **Self-checks before handback (as each reader records):** A compared its hand-copied PROOF fields with the files by a read-only script, repaired four LMID fields by hand (`DR-117` item 2) and re-ran the check; its quotation self-check matched 93 table rows and 22 quotations (A snags 10, 12). B displayed the positional lines with `sed -n` and copied them by hand (B L58). C compared its fields by a read-only script and re-cut four by hand (C snag 8). D repaired one field (the Register's LMID) by hand, and matched 68 tagged quotations to their lines (D snag 9). No PROOF field was produced by a script; no reader created a helper file in the repo.
- **Ruling-log freeze (`M-302`):** not checked by this merge writer. `DR-123` (`DRL` L1871 to L1879) was added after the readers' spans were set; it lies past every reader's span (piece snag 7).

## Round 1 headline claims (union, before Round 3)
| Claim | A | B | C | D |
|---|---|---|---|---|
| The ten pointers present, append-only | found | found | found, with line counts | Step 5's |
| `APB` L3 "NOT APPLIED" | found | found | found | — (not on D's list) |
| `ANS` L12 (the held Planet) / L20 / L29 | — | L12, L20 | L12 | L12, L20, L29 |
| The finish-run pieces' "held Planet" heads | — | — | found | — |
| `P2` L3's relay sentence without a docket | possibly | absence count 0 | whole read: none | — |
| `S6` L3's relay sentence without a docket | possibly | piece not on list | ID not opened | not on D's list (with Step 7's L3) |
| Q-123 answered by `DRL` L686 | found | (cited `DR-28` through the Frame) | "the October flag (Q-123) stands" | — |
| Q-20 "held" lines | four (with `P9` L82) | three | four | — |
| `DS12` L36 against `SPEC` L174 | found | found | found | — (not on D's list) |
| Anchor drift | measured, 555 hits | five by hand | spot | Step 5 map; `NOTE` L100 |
| Spec anchors in the old numbering | 109 lines, Phases 3 to Step 5 | 107 cites, six files | the early pointer silent | Step 7's spec L152 and L229 blank |
| Gate 2 | PASS, one moderate flag (re-derived) | PASS; F-10 dispositioned in the layer | PASS; the flag re-derived, verifiable | the Step 5 piece carries it |
| Gate 4's weakest cell | the duty clause and the organization | the duty clause | the core alone and the duty clause | — |
| Gate F | PASS; the Act statements agree | PASS, with flags | PASS, one flag: "(Act 1)" against `FRM` L167 | — |
| Gate I | ratio not counted | direction counted | ratio uncounted | — |
| `S6` L27, the Element open | found | not found | not found | — |
| `P2` L283 | not found | found | not found | — |
| `CUL` L107, L152, L261 unmarked | L107 noted | found | not found | — |
| `CUL` L77, L178; `CUL` L8 | not found | found | not found | — |
| `P4` L246, a third sense of "warning" | not found | not found | found | — |
| The Phase 3 pointer and `DR-122` item 6 | not found | "the pointer applies it" | the pointer lacks it | — |
| Station-builder scan | run | not run | run | — |
| Gate G runnable | (in its not-re-run lines) | found | (in its not-re-run lines) | — |
| The register, the older pieces, Step 6's rows | — | — | — | AS7bD-2, -3, -6 to -10, -14 to -16 |
| The count of pointer files (ten against eleven) | — | — | — | AS7bD-12 |
| Numbering | AS7b-1 to AS7b-34 | AS7b-1 to AS7b-19 | AS7b-1 to AS7b-14 | AS7bD-1 to AS7bD-16 |

## READ-COVERAGE (which reader read which entry in full)
**Key:** **W** read whole, or the whole admitted span · **S** scanned only (every line searched by script, the hits and named lines read in context) · **P** part (the lines stated) · **—** not read beyond the PROOF lines · blank: not on that reader's list. Sources: each reader's reading log and canon receipt (A L5 to L54, L60 to L99; B L5 to L58, L67 to L126 and snag 1; C L6 to L45, L1208 to L1231 and snag 1; D L5 to L33).

| # | Entry | A | B | C | D | Read whole by |
|--:|---|:-:|:-:|:-:|:-:|---|
| 1 | the stereotypes law | W | W | W | W | A, B, C, D |
| 2 | the phase-spine spans | W | W | W | W | A, B, C, D |
| 3 | the generators spans | W | W | W | | A, B, C |
| 4 to 8 | the climate READER, both robot files, the two disciplines | W | W | W | | A, B, C |
| 9 | the spec (29 spans) | W | W | W | W | A, B, C, D |
| 10 | the rulings log (26 spans) | W | W | W | W | A, B, C, D |
| 11 to 14 | the Register, the relationship database, the immigration file, the language blocs (spans) | W | W | W | W | A, B, C, D |
| 15 | Step 7 | P (L1 to L205 and the re-run raw blocks; L1521 to L1713 not opened) | P (L1 to L205 and the re-run raw blocks) | P (L1 to L1629, L1715 to L2027) | W (its span L1 to L205) | the report: A, B, C, D; the re-run raw blocks: A, B, C |
| 16 | the Step 7 piece | W | W | W | | A, B, C |
| 17 to 21 | the input contract, Frame, Inherited, Spine, Research | W | W | W | P (the Frame's three spans) | A, B, C |
| 22 | Phase 2 | W | W | W | | A, B, C |
| 23 to 30 | Phases 3 to 10 | S | W | W | | B, C |
| 31 | Step 5 | S | P (L1 to L130, L780 to L842; the rest scanned) | W | W | C, D |
| 32 | Step 6 | S | S | W | W | C, D |
| 33 to 40 | the seven datasheets; the culture file | W | W | W | | A, B, C |
| 41, 42 | the Phase 6 and Phase 7 pieces | S | S | W | W | C, D |
| 43 | the Phase 2 composition piece | S | S | W | W | C, D |
| 44, 45 | the Phase 9 and Phase 8 pieces | S | S | W | W | C, D |
| 46 | the Phase 8 dockets | W | W | W | W | A, B, C, D |
| 47 | the Idelsk-Uralia piece | S | S | W | W | C, D |
| 48 | the robot-term piece (L1 to L30) | W | S | W | W | A, C, D |
| 49 | the amendment register | W | S | W | W | A, C, D |
| 50 | the 2026-11-03 note (L1 to L120) | W | — | W | W | A, C, D |
| 51, 52 | the Phase 10 and Step 5 pieces (L1 to L60) | W | S | W | W | A, C, D |
| 53 | the answers note | W | W | W | W | A, B, C, D |
| 54 | the Steps −1 to 3 piece (two spans) | W | W | W | | A, B, C |
| 55 to 57 | the Phase 3, Phases 4 and 5 and symbols pieces (spans) | W | — | W | | A, C |
| 58 | `APB` (L1 to L60) | W | W | W | | A, B, C |

**How the gap was closed.** After Round 1, eight entries had been read whole by C alone: Step 5 (31), Step 6 (32) and the six older pieces (41 to 45, 47). The orchestrator wrote a 25-entry list around them and dispatched gap reader D (checkpoint, 15:05 line), who read all eight whole, plus the sources, the register, the 2026-11-03 note's span, the Phase 10 and Step 5 pieces' heads, Step 7's report and the Frame's spans, without seeing A's, B's or C's output. **After D every entry on the list was read whole by at least two readers.** D's findings that A, B and C also reached are independent confirmations; D's finds that no other reader had were checked by this merge at their lines (the piece credits each "(D)" and says "confirmed at the lines"). Gaps that remain, by design: Step 7's raw blocks for the gates not re-run (opened by no reader in full); the Step 5 piece past L60 and the Step 6 piece (on no list; this merge looked at the Step 6 rows its findings name).

## Round 2 (`Tools/triple_read_verify.py`) · UNANIMOUS on the first run, both lists
**What happened (checkpoint, 15:05 and 15:28 lines).** The tool was run once on A's, B's and C's outputs against the frozen 58-entry list: **58 entries, 174 of 174 agent-entry results match ("all fields match ground truth"), verdict UNANIMOUS - CLEARED TO WRITE.** No field was repaired at Round 2 and there is no first-run file. **D's 25 entries were checked as one reader: D's single output file was passed to the three-slot tool in all three agent slots**, so its **75 of 75** is one reader's PROOF blocks checked three times against the files, a mechanical check, not three independent readers (D's own pre-handback repair of one field is recorded above). Both raw outputs follow, verbatim.

### Round 2: raw output, the 58-entry list (full; file `.t8_amend_ST7b_round2_raw.txt`)
```
required files: 58
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 82-272,1098-1184] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/02_Generators_Capability_and_Symbols.md  [range 125-175,637-806] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Climate Data/READER/Mirny.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Mirny.md  [range 1-3,5-8,10-80,82-105,107-120,122-157,159,161-162,164-165,167-179,181,183,185,187,189,191-204,206-210,215-217,219,221,223,225-227,229,231-233,235,237,239-243,246-248,251-252] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 20-147,170-254,384-419,422-554,575-587,609-665,678-690,725-757,953-1031,1075-1088,1092-1107,1111-1133,1135-1160,1211-1226,1404-1412,1427-1434,1438-1445,1460-1468,1472-1479,1523-1530,1550-1557,1570-1577,1655-1662,1664-1671,1707-1715,1728-1870] ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/07_QA_Gates.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST7_QAGates_2026-11-04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00.1_Step_MINUS-1_Input_Contract.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_03_Surface_and_Texture.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_04_Ordinary_Life.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_05_Relation_and_Geometry.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_06_Meaning.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_07_Order.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_08_Making.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_09_Populations.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_10_Catalog.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/05_Reconciliation.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/06_Differentiation.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Step_-1.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Step_0.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Step_1_and_2.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Step_3.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Phase_3.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Phase_4.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Phase_5.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Local_Cultures/Mirny_Subnet/Mirny.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md  [range 1-30,895-918] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST13_Phase3_2026-11-05.md  [range 1-30,510-529] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md  [range 1-30,790-801] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_ST16_Symbols_2026-11-05.md  [range 1-60] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Application_Batch_1_Pointers_2026-11-08.md  [range 1-60] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

### Round 2: raw output, the gap reader's 25-entry list, one reader in three slots (full; file `.t8_amend_ST7bD_round2_raw.txt`)
```
required files: 25
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 82-272,1098-1184] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Mirny.md  [range 1-3,5-8,10-80,82-105,107-120,122-157,159,161-162,164-165,167-179,181,183,185,187,189,191-204,206-210,215-217,219,221,223,225-227,229,231-233,235,237,239-243,246-248,251-252] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 20-147,170-254,384-419,422-554,575-587,609-665,678-690,725-757,953-1031,1075-1088,1092-1107,1111-1133,1135-1160,1211-1226,1404-1412,1427-1434,1438-1445,1460-1468,1472-1479,1523-1530,1550-1557,1570-1577,1655-1662,1664-1671,1707-1715,1728-1870] ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/05_Reconciliation.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/06_Differentiation.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_PIU_IdelskUralia_2026-11-04.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/07_QA_Gates.md  [range 1-205] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00_Frame.md  [range 130-175,219-236,463-466] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Dockets_P08_Making_2026-11-04.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_PRT_RobotTerm_2026-11-04.md  [range 1-30] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Notes_2026-11-04_Answers_Carried_Forward.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

**Reading the output:** 58 entries, 174 of 174 agent-entry results matching, verdict UNANIMOUS; 25 entries, 75 of 75 slot results matching for the one gap reader, verdict UNANIMOUS. **No field was repaired at Round 2; no reader re-ran.**


## Round 3 (SendMessage to readers A, B and C) · 2026-11-08, replies 15:09 to 15:11 (scratchpad file times) · cross-check done
Each reader read the other two readers' sections from "What changed" to the snags, skipped their PROOF blocks, re-opened lines on its own list to settle disagreements, and wrote four parts: the shared points K1 to K8, each AGREE or OBJECT with the settling line; a mapping of the colliding AS7b numbers with keep, drop or fold for single finds; the docket, requests and questions unified; and its concessions and holds. Replies: `.t8_amend_ST7b_round3_reader{A,B,C}.md` (136, 212 and 358 lines; byte-identical to the scratchpad copies by `cmp`). **D was not part of Round 3** (D ran after Round 2 and alone); D's finds are weighed in this merge as independent confirmations or as single finds checked at their lines.

| Reader | Objections (its Part 1) | Lines re-opened (as each reply lists them) | Concessions | Holds |
|---|---|---|---|---|
| A | to B: the "signif" and "curat" rows over-match "Significant" and "accurate"; to C: the `FRM` L527 one-line quotation spans L526 to L527 | `P2` L283; `FRM` L526, L527; `S6` L27; the culture file L3, L25, L31, L34; `P5` L3, L145, L149, L514; `P2` L99, L101, L272 | Gate 2's wording; `S6` L27 downgraded to a record note; the Act 1 point to C's flag; its spec-anchor count folded; B's `ANS` L12, L20, `P2` L283, the culture-file lines, `CUL` L8 note and Gate G; C's core, Phase 3 pointer and `P4` L246 | the drift table; Q-123 closes; `P2` L3 at high confidence; no new station-builder violation |
| B | to C: "the October flag (Q-123) stands" (wording); C's prose at C L1051 names another location | `DRL` L686, L1130, L1868; `S6` L27; `FRM` L167, L526, L527; `P9` L82; `P3` L342; `P4` L246; `P2` L283; the culture file L107, L152, L243, L261 | the Phase 3 pointer claim; ruling C closes; A's and C's station-builder result; `P9` L82; `S6` L27; its Gate I arithmetic; the warnings classed originated; Gate 2's joint wording; its `CUL` L8 note dropped; its DK7b-9 replaced; A's drift table | `P2` L283; four culture-file lines (L243 added); the Act 1 flag, with C; its bracketed raw blocks |
| C | to B: the three-line Q-20 list (omits `P9` L82); the placement of B's DK7b-9 on Step 7's gate-result lines | `DRL` L678 to L690; `P2` L283; the culture file L77, L107, L152, L178, L261 and its held lines; `ANS` L16, L20; `S6` L27 | Q-123 closes; its Gate F flag becomes a note under AR-14 (its AQ-284 withdrawn); A's `S6` L27, `P10` L137 and drift table; B's `ANS` L20, `P2` L283, the culture-file lines L107, L152, L261, L77, L178 and L8, and Gate G; its own prose name at C L1051 | four Q-20 lines; Step 7's lines unmarked; `P4` L246's third sense; the core alone fails the swap; `DS12` L36 the only new contradiction |

### The shared points (K1 to K8)
| K | Topic | A | B | C |
|---|---|---|---|---|
| K1 | the new result per gate | AGREE on every verdict | AGREE; Gate 2 joint wording conceded; Gate I arithmetic withdrawn | AGREE; its Gate F flag becomes a note |
| K2 | the stale lines | AGREE; adopts `ANS` L12, L20; `S6` L27 downgraded | AGREE; adds `P9` L82 and the culture file's L243; concedes the Phase 3 pointer | AGREE; adopts the single finds it missed |
| K3 | the scans | AGREE; OBJECT to B's two rows (instrument) and C's L527 quotation | AGREE; accepts A's and C's station-builder scan | AGREE; counts differ by pattern |
| K4 | the anchor drift | AGREE (its measured table) | AGREE; A's table replaces its five | AGREE; A's table the better record |
| K5 | the errata | AGREE on E1′ to E16; the new ones unioned | AGREE; union | AGREE; union, none rejected |
| K6 | the symbols | AGREE | AGREE; `S6` L27 accepted | AGREE; adds `P06` L244 from its whole read |
| K7 | the reading limits | AGREE; its limits named | AGREE; its limits named; D covers the rest | AGREE; it read all 58 |
| K8 | other-location lines | AGREE none used; formats differ | AGREE; OBJECT (narrow) to C L1051 | AGREE; C L1051 conceded |

### The splits, and how they were settled
*Rule: the position two or three readers hold after Round 3's concessions; where they still differ, the most conservative reading (the one that changes less, claims less or keeps a record), the split named in the piece.*

| # | Point | Positions after Round 3 | Settlement (where in the piece) |
|--:|---|---|---|
| 1 | **Gate 2's label** | A: "flag (re-derived)"; B, C: "dispositioned in the layer"; A adopted the joint wording | **PASS; F-10 re-derived in the layer; the bodies keep the old scope as records** (AS7b-14) |
| 2 | **The "(Act 1)" tag against `FRM` L167** | A: a flag (conceded its Round 1 "agree"); B: a flag; C: a note under AR-14 | **a flag, riding with AR-14; C's form named** (AS7b-34; decision 7) |
| 3 | **Q-20's "held" lines** | A, C: four; B: three, conceded `P9` L82 | **four lines** (AS7b-4) |
| 4 | **Q-123** | A: closes; B: closes; C: "stands", conceded | **closes on `DRL` L686** (AS7b-4) |
| 5 | **`S6` L27, "the Element is open"** | A: a record note, low; B: moderate; C: keep | **a stale record, kept; this merge found the Step 6 piece's mark text itself stale** (AS7b-36) |
| 6 | **Gate I's ratio** | B's direction arithmetic withdrawn by B | **not counted; C's sentence adopted by all three** (AS7b-38) |
| 7 | **The warnings on the relay, classed** | B: inflected, conceded; C: originated; A: not classed apart | **originated, as part of the knowledge** (AS7b-38) |
| 8 | **The culture file's light lines** | B: four lines (L243 added in Round 3); A, C: agree for three | **no mark: Batch 3 left them unmarked on purpose** (`AB3` L635; this merge) (AS7b-23) |
| 9 | **`CUL` L8** | B dropped it; A, C keep it as a note | **a note** (AS7b-33) |
| 10 | **Marks on Step 7's gate-result lines** | B proposed (its DK7b-9); A, C: append after L2027 only; B conceded | **append only** (DK7b-17) |
| 11 | **The spec numbering** | A 109 lines; B 107 cites in six files; C the early pointer | **one finding, eleven files; Phase 2 carries none** (B's GC-b and A's GCb-5 print 0) (AS7b-30) |
| 12 | **Other-location lines in raw blocks** | A: unedited; B: bracketed; C: kept, listed in a snag | **omit the line, say so in the block's heading; no bracket edits inside pasted lines** (piece §3, common method; snag 4) |
| 13 | **Gate 4's weakest cells** | A: the duty and the organization; B: the duty; C: the core alone and the duty | **union: the core alone, the duty clause and the organization each fail alone** (AS7b-26) |
| 14 | **Numbering** | four colliding sets (A 34, B 19, C 14, D 16) | **39 merged findings in gate order** (piece §5) |
| 15 | **The unified requests and questions** | B's and C's Round 3 lists number them differently | **this merge's AR-280 to AR-287 and AQ-280 to AQ-294**, mapped in piece §5 |

### Single finds, checked
| Find | Finder | Checked by | In the merge |
|---|---|---|---|
| Q-123 answered by `DRL` L686 | A | B, C (Round 3) | AS7b-4 |
| `P9` L82 "held" | A, C | B conceded | AS7b-4 |
| `S6` L27, the Element open | A | B, C (Round 3) | AS7b-36 |
| The drift table (555 hits) | A | B, C, D | AS7b-8 |
| `ANS` L12 and L20 | B (C for L12) | C, D | AS7b-2 |
| `ANS` L29 | D | this merge at the line | AS7b-2 |
| The finish-run pieces' heads | C | A (Round 3, K6); this merge | AS7b-2 |
| `P2` L283 | B | C (whole read of `P2c`), A | AS7b-19 |
| `CUL` L107, L152, L261 | B | A, C | AS7b-23 (no mark) |
| `CUL` L243 | B (Round 3) | this merge at the line | AS7b-23 (no mark) |
| `CUL` L77, L178 | B | A, C | AS7b-23 |
| `CUL` L8 | B | A, C | AS7b-33 |
| `P4` L246's third sense | C | A, B | AS7b-22 |
| The Phase 3 pointer lacks `DR-122` item 6 | C | A, B | AS7b-27 |
| "(Act 1)" against `FRM` L167 | C | A, B | AS7b-34 |
| The core alone fails the swap | C | A, B | AS7b-26 |
| `P10` L137 settled by "of unstated making" | A | B, C | AS7b-21 |
| Gate G runnable | B | A, C | AS7b-39 |
| The status lines are records | B | A, C (the tracker on no list) | AS7b-5 |
| `P06` L244 | C (Round 3) | D | AS7b-36 |
| The answers note stale on three facts (AS7bD-1) | D | B, C (L12, L20); this merge (L29) | AS7b-2 |
| Six Step 6 contradictions (AS7bD-2) | D | this merge: the Step 6 piece's D6-10, D6-12, D6-18, D6-23, D6-38 | AS7b-17 (dispositioned) |
| Step 6's row cells (AS7bD-3) | D | this merge: D6-25, D6-26, D6-32, D6-49 | AS7b-25 (dispositioned) |
| Step 5's map; `NOTE` L100 (AS7bD-4) | D | A's drift; this merge at `S5` L714 to L719 | AS7b-8 |
| Step 7's spec anchors (AS7bD-5) | D | B's tag; this merge | AS7b-30 |
| The register stale (AS7bD-6) | D | this merge at the four lines | AS7b-9 |
| The Phase 6 piece's joined form (AS7bD-7) | D | this merge at `P06` L237, `DRL` L1787 | AS7b-24 |
| The older pieces' symbol timing (AS7bD-8) | D | C (`P06` L244); this merge | AS7b-37 |
| English-only and second-slot lines (AS7bD-9) | D | A, B, C on the rule; this merge at the lines | AS7b-18 |
| Accepted pieces still "awaiting" (AS7bD-10) | D | this merge at `P08` L3, L535, `P2c` L256 | AS7b-10 |
| `REG` L57's sources; `SPEC` L174's note (AS7bD-11) | D | this merge | AS7b-28 |
| Step 6 without a pointer; ten against eleven (AS7bD-12) | D | A, B, C (no pointer); `APB` L9, L42 and `DRL` L1876 (the count) | AS7b-11; AS7b-1 |
| Steps 6 and 7's L3 (AS7bD-13) | D | A, B, C; the Step 6 piece's D6-1; `ST7` D7-1 | AS7b-3 |
| LC-39 untagged (AS7bD-14) | D | this merge at `S5` L175, `S5p` L43 | AS7b-17 |
| The Frame's figures (AS7bD-15) | D | this merge (`FRM` L134, L153, L655) | AS7b-32 |
| The mandated share in `DRL` L1130 (AS7bD-16) | D | this merge: the Step 6 piece's D6-55 | AS7b-31 |

### Claims not accepted (left out of the merge; each listed with what was done)
| Claim | Whose | Objected to by | Why (the evidence line) | In the merge |
|---|---|---|---|---|
| held marks for `CUL` L107, L152, L243, L261 (its DK7b-6) | B | this merge | Batch 3 left them unmarked on purpose: "No physics error on these lines" (`AB3` L635), approved with the batch (`DRL` L1876) | not carried (AS7b-23; AQ-294 answered) |
| marks on Step 7's gate-result lines (its DK7b-9) | B | C, A | records are never reworded; the batch method appends at the end (`APB` L23) | withdrawn by B; DK7b-17 |
| the three-line Q-20 list | B | C, A | it omits `P9` L82 ("Mirny is a Settlement (Q-20 held)") | four lines (AS7b-4) |
| Gate I's direction arithmetic | B | B itself | without October's counts it is an assertion | withdrawn (AS7b-38) |
| the Phase 3 pointer applies `DR-122` item 6 | B | C | `P3` L543 cites `DR-122` for "warning" only | conceded (AS7b-27) |
| Q-123 "stands" | C | A, B | `DRL` L686 answers it | closes (AS7b-4) |
| the one-line quotation of `FRM` L527 | C | A | the sentence spans L526 and L527 | quoted as two fragments (AS7b-34) |
| prose naming another location (C L1051) | C | B | the one-location law | not reproduced; "(post-war; another location: not used)" |
| the counts of the "signif" and "curat" rows | B | A | they also match "Significant" and "accurate" | no conclusion rests on them (AS7b-12) |
| "the two agree" on the Act 1 tag | A | B, C | `FRM` L526's bound | conceded to C's flag (AS7b-34) |
| Step 6's L3 possibly undocketed | A, B, C, D | this merge | the Step 6 piece's D6-1 (`ST6` L409) | dispositioned (AS7b-3) |
| six Step 6 contradictions undispositioned | D | this merge | the Step 6 piece's D6-10, D6-12, D6-18, D6-23, D6-38 (`ST6` L418 to L446) | dispositioned (AS7b-17) |
| `S6` L266's tier half undocketed | D | this merge | D6-55 (`ST6` L463) | dispositioned (AS7b-31) |
| the eleventh pointer file unidentifiable | D | this merge | `APB` L9, L42; `DRL` L1876; the symbol review's L61 | answered (AS7b-1; AR-284) |

## Settled in the merge (beyond the splits)
- **Union applied:** A (the pointer check; the drift table; Q-123; `S6` L27; `P10` L137; the body-only coverage matrix; the station-builder scan; the census tally); B (the disposition look-ups; `ANS` L12 and L20; the status-lines null; `P2` L283; `CUL` L77, L178 and the L8 note; Gate G; the spec counts at or after old L46); C (the pointer texts and line counts; the ID sets; the Phase 3 pointer's missing item 6; `P4` L246; the Act 1 flag; the core alone; the early pointer's silence; the Gate I classes and the ratio sentence); D (the register; the Phase 6, Phase 8 and composition pieces' lines; the older pieces' symbol timing and language lines; LC-39; `NOTE` L100 and Step 5's map; the Frame's live arithmetic; the Register's sources cell and the spec's note; the count of pointer files).
- **One copy per scan:** the piece pastes 23 raw blocks (A 9, B 2, C 5, D 7), each complete or excerpted with the count of omitted lines and the reason; the other readers' agreement is stated under each. Nine pasted lines were omitted because they print another location's name (piece snag 4); no line inside a pasted block was edited.
- **Who teaches, who goes out, the warning's form and the organization's name stay open** (`ANS` L15, L26; `DRL` L1431); no reader named any, and none is named here.
- **Figures:** the old frame's figures appear only inside quoted or pasted lines; the mixing check below runs on the piece's prose (pasted blocks excluded, being records), on each finding block and on the docket. Shares are weights, never head counts.
- **The coinage** appears in the piece only inside pasted raw blocks (the pass's own lines); the piece's prose names it as "the coinage" and never uses the word.
- **No other location is named** in the piece or in this record (the name scans below); the Round 2 raw files carry none.
- **No DEC number is assigned**; eleven decisions are proposed with recommended wordings (piece §9), for the orchestrator to number from DEC-220.

## Read by this merge beyond the readers' lists (recorded; used only where the piece says so)
- **The Step 6 piece** (`Amendment_Rederivation_ST6_Differentiation_2026-11-04.md`, 593 lines, PROPOSED), by search and at these lines: L1 to L6 (status), L23, L38 to L54 (the head tags and the register's omissions), L64, L77, L105, L115 to L123, L280 to L297 (the corrected row), L334, L376 to L377, L405 to L463 (the dockets D6-1 to D6-55), L472 to L480 (its feeds to Steps 7 and 8). It settled Step 6's L3 (D6-1), L27 (D6-40), L93, L96, L129, L155, L156, L159, L325 (D6-10 to D6-38), L198, L210, L222, L233, L243 (D6-25 to D6-49) and L266 (D6-55); it has no Q-20 row. Its feed to Step 7's Gate 3 (L476) was not run here (piece AR-282).
- **The Batch 2 and Batch 3 files:** `AB2` L1 to L4 and L272 (where `DS12` L36's clause came from); `AB3` L1 to L6, L635 and L637 (the culture-file lines left unmarked; the language line kept as a docket row).
- **The rulings log L1863 to L1879** (`DR-122` and `DR-123`); L1733, L1742, L1760, L1778, L1787, L1805 at single lines to confirm the readers' citations.
- **The symbol review's last two lines** (L60, L61) and its line count (61); **the decisions file's DEC-203 heading** (L403); **`ALR`** L1 to L55.
- **Lines the readers cited, re-read to settle or confirm:** `DS12` L36; `SPEC` L174, L251 and L252 (the Mirny clauses only); `APB` L1 to L60; `ANS` L3, L12, L20, L29, L38, L43, L49; `S6` L3, L27, L265, L266, L380; `P9` L18, L82; `P10` L16, L137, L631; `DRL` L686, L1116, L1130, L1150, L1431, L1432, L1769; `FRM` L134, L153, L167, L526, L527; `P2` L282 to L284; `P4` L235, L238, L246, L404; `P5` L589; `P3` L342; `S5` L175, L357, L714, L715, L718, L719, L842; `REG56` L7, L96, L101, L163; `P06` L237, L244, L263; `P07` L54, L58, L85, L254, L349; `P9p` L108, L189, L206, L231, L244; `P08` L3, L106, L271, L436, L535; `P2c` L256; `REG` L57; `S5p` L37, L43; `PRTP` L9; `P10p` L57; `DK8` L26; `NOTE` L4, L20, L97, L100; `ST7` L173, L316, L428 to L507; `ST12` L8, L24; `ST13` L3, `ST14` L3, `ST16` L3; the culture file L1, L8, L53, L77, L105, L107, L152, L178, L235, L243, L249, L261, L303; `DS0` L26; `DSP4` L38 to L40; `DSP5` L57; `DSm1` L16. **Lines that name another location were read only to confirm their place and are quoted nowhere** (`SPEC` L15, L16, L251; `DRL` L1769's comparison; the culture file's L235).

## Kept files (`M-132`)
The Round 1 outputs `.t8_amend_ST7b_readerA.md`, `.t8_amend_ST7b_readerB.md`, `.t8_amend_ST7b_readerC.md`, the gap reader's `.t8_amend_ST7bD_readerD.md` and the Round 3 replies `.t8_amend_ST7b_round3_readerA.md`, `.t8_amend_ST7b_round3_readerB.md`, `.t8_amend_ST7b_round3_readerC.md` are kept in this folder as the round's working record, unedited, beside the Round 2 files (`.t8_amend_ST7b_round2_raw.txt`, `.t8_amend_ST7bD_round2_raw.txt`), the frozen briefs (`.t8_amend_ST7b_brief.md`, `.t8_amend_ST7bD_brief.md`), the lists (`.t8_required_amend_ST7b.txt`, `.t8_required_amend_ST7bD.txt`) and the checkpoint `.t8_amend_ST7b_CHECKPOINT.md`. The reader files, the replies, the briefs and the lists are byte-identical to their scratchpad copies in `amend_ST7b/` and `amend_ST7bD/` (`cmp`, by this merge). None of these files is an input to a later step; this record and the piece are the merged result. No helper file was created in the repo by the readers or by this merge (scratch work stayed in the session's scratchpad, `st7b_merge/`).


## Quotation audit (`Tools/quotation_audit.py <the Mirny pass folder> --files Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md --own-pass`, run from the repo root) · 2026-11-08 about 15:57, run before this record existed
*The merge brief's command omits the tool's required first argument, the pass folder; it was run with the folder given, as the Phase 4 and 5 and symbols records ran it.*
raw output, excerpted (1 line omitted: the positive control "HARD - case mismatch", whose test phrase names another location; it is one of the five controls behind the instrument line below, which reads VALID; the whole output is in the session scratchpad at `st7b_merge/qaudit_run1.txt`):
```
pass audited : Mirny
corpus mode  : default (own pass excluded)
corpus files : 6099   chars: 70,270,378
files audited: Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md
own-pass mode: a quotation may also be found in this pass's OTHER files (never in its own file)

=== POSITIVE CONTROLS ===
  [easy                      ] FOUND     a terminus is nobody's midpoint
  [HARD - blockquote wrap    ] FOUND     A pass may not proceed to Step 5 with a NEVER CITED row
  [HARD - outside Worldspace ] FOUND     Paste raw QA scan output into the QA block. Never summa
  [HARD - long wrapped       ] FOUND     Different content is not differentiation; a different q

  INSTRUMENT VALID: YES
  NEGATIVE CONTROL (must be absent): PASS - absent

=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 128
NOT FOUND in corpus: 46
  of those, in TABLE CELLS : 5
  of those, in PROSE       : 41

  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:4]           the scans ran on 2026-11-08, after 14:00, by the developer's explicit instruction
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:22]           hawaiian and the supporting tier occur in no pass body; they stand in ds0 , dsp4 , dsp5 and the culture file (as7b-12, as7b-14). t
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:72]  [CELL]  founders per reg l57; live census per the census row l500 and spec l20 to l22
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:417]           while the ten pointers it prepared are present (a, b, c). batches 2 and 3 already carry a dated line at their head
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:418]           ( drl l1868) (b, c, d). ans l20: the spec's founding lines
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:418]           against spec l174, l251, l252 as they now read (b, d). ans l29: the pointer lines
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:419]           (c; a in round 3, k6). mirny is still not complete, on other grounds ( drl l1877 item 4; drl l1878
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:430]           wording stands at p9 l18 and p10 l16 (
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:449]           against dr-99 ( drl l1660); l163's one-line finding carries the relay duty and the warnings' route inside the finding, against
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:453]           ( p08 l535) stands under a head that reads
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:453]           ( p08 l3); the axis wording it accepted is recorded in the register ( reg56 l90), and d found no line of the piece that states it.
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:613]           hawaiian and the supporting tier and the same coinage counts; b's
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:620]           zero lines in every file (a); c's two word-bounded hits ( p4 l157, p8 l221) quote the robot physiology file's coolant analogy: fal
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:620]           otherwise occurs only as sea or open water (a). emissions: a's two hits (
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:620]           p10 l394) and c's eight ( con l202, the word
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:700]           ) at p6 l139 and l331: records, dispositioned by a6-1 ( p06 l79, l95) and as7-25 (f-10 re-derive); p7 l391: a record, dispositione
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:700]           ): a false hit for the social contract; p8 l701 and p10 l252 scope a crossing item to crossers (
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:702]           at p7 l126, l128, l269, l279, l646, l668 and s5 l90: records, dispositioned by the phase 7 piece ( p07 l54, l58, l85: whoever is m
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:702]           the highway rule stays a highway rule); p5 l264 scopes the highway rule on its own line; p5 l205 is read through the phase 4 and 5
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1084]           ): records, dispositioned by the pointers (the five early files, p3 , p4 , p5 ), the composition piece, dk8 d8-4 and d8-5, the pha
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1084]           note l4). the six datasheet hits are marked records (
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1085]           docket or answer context; p2c l93, l112, l118, l138 and l183 (
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1085]           ) are superseded by that piece's own 9 answer ( p2c l256) and are read with it; p08 l180 (the three researched forms
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1089]           57 lines (16 carry a mark on the same line)
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1089]           24 (3), the october gate 3 phrases 16 (1). each file is covered by its notice and, for ten files, its pointer; phases 6 to 10 and 
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1089]           p06 , p07 , dk8 , the phase 9 piece's a9-23, dr-57
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1095]           ) is settled by dr-111 : the supporting tier is english and russian, set as a mirny special case ( drl l1769); applied at ds0 l26 
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1097]           ) and l452, the register's l96 (as7b-9) and the 2026-11-03 note's l20 (its live column
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1109]           ( p10 l137, october l135): the ring, the core and the relay hardware are
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1123]           they are needed inside the finding. dr-113 built the core around the knowledge the first generation made
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1142]           ( drl l1220) and still have no arbiter: passes (a, c). phase 8's axis
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1158]           ( drl l1868). the phase 3 pointer ( p3 l543) carries dr-122 's answer on
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1289]           ( reg l57; drl l1661); spec l174's own note still reads
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1457]           at the end of l526 (the sentence spans two lines: a's round 3 objection to a one-line quotation of it). act 1 is a hazy range (
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1463]           october l169, 4) and l337, by a9-21 (a, c); the relay-making absolutes ( p9 l174, l369, l380; p10 l137, l141, l239, l246, l271, l4
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1464]           lines, about the split brain, not people (a, c); cul l53's
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1471]           a piece record of 2026-10-29 (c in round 3; d). this merge's look: the step 6 piece marks s6 l27 as a record (d6-40, st6 l448), bu
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1497]           nothing here suggests the ratio crosses the 3 : 1 flag, and only a count can show it
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1542]  [CELL]  ). the exact wording is still to be drafted for the developer (dec-020) the core is now ruled; st7 's
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1547]  [CELL]  is superseded, and the culture file's l105 still says so as a docket row held on purpose
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1555]  [CELL]  ); holidays and religion come after it; symbols are decided within mirny's own ulm , which supersedes e16's
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1561]  [CELL]  keeps two uses in the pass text, the wind's own first sign and the weather warning on the relay, context deciding; phase 4 l246 us
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1741]           in the pointers read as the founding era while the frame holds the act open recommendation: keep the act open as the frame ruled; 
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1761]           rows over-match; d's scan 4 removed only the exact string
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1781]           tag against the frame's open act (as7b-34). options: a) the first generation is act 1 by definition b) keep the act open as the fr
  [Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md:1781]           as the founding era, under ar-14. recommended wording: keep the founders' act open as the frame ruled, and read the pointers'

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```
**Triage by hand (each of the 46 misses read and classified):** 128 fragments tested, **46 not found** (5 in table cells, 41 in prose). **45 are connective prose** captured between two adjacent quotations on one line (the audit's own warning; the merge's mechanical check below confirms, for each of them, that the missed text lies between two quoted strings and inside none): the status block (L4); section 0 (L22); section 2's first row (L72, a cell); AS7b-2 (L417, L418 twice, L419); AS7b-4 (L430); AS7b-9 (L449); AS7b-10 (L453 twice); the Gate 1 agreement line (L613); AS7b-13 (L620 three times); AS7b-14 (L700 twice, L702 twice); AS7b-16 (L1084 twice, L1085 twice); AS7b-17 (L1089 three times); AS7b-18 (L1095, L1097); AS7b-21 (L1109); AS7b-24 (L1123); AS7b-26 (L1142); AS7b-27 (L1158); AS7b-28 (L1289); AS7b-34 (L1457); AS7b-35 (L1463, L1464); AS7b-36 (L1471); the errata E3′, E8′, E16′ and E22 (L1542, L1547, L1555, L1561, cells); AQ-285 (L1741); snag 9 (L1761); decision 7 (L1781 twice). **One is an exact quotation of a reader's wording** (L1497: reader C's sentence on the Gate I ratio, `.t8_amend_ST7b_readerC.md` L1080, adopted by all three in Round 3); the audit's corpus does not read dot-files; confirmed below with `grep -nF`. **No misquotation was found by the audit.** This was the audit's only run on the piece. Before it, this merge's supplementary check had flagged three strings in a draft, all corrected before the piece was written to the folder: a list of reader labels set in quotation marks (re-set without them), a finding heading that put a paraphrase in quotation marks (re-worded without them) and a proposed mark text set in quotation marks inside a decision (re-set as plain text). **The supplementary check** (`st7b_merge/shortq7b.py`, run with `python3 -I`) tests every double-quoted string of any length in the piece's prose, ellipsis-split, normalizing dashes, quotes, markup, case and spaces, against the Mirny folder's files including the reader dot-files and the `Datasheets/` subfolder, the rulings log, the runbook, `ALR`, the phase-spine and generators files, both disciplines, the Founding Register, the Mirny spec, the relationship database, the culture file, the immigration file, both robot files, the climate READER and the stereotypes law, **with this record and the piece itself excluded**: **0 not found**; a second run without the reader dot-files leaves nine strings, each a reader's own wording quoted as that reader's (merge checks below). The audit was not re-run after this record was created.


## Merge checks
raw output (full; scripts in the session scratchpad `st7b_merge/`, run with `python3 -I` on the final piece; the name scan's list is built from the spec file names plus the names in the session's location list, 53 names, and its control on a scratch line with three planted names found all three; names are not reproduced here):
```
$ python3 -I shortq7b.py ctl_piece.md   # positive control: two real quotations, one planted
  NOT FOUND L2: a planted control sentence for unit ST7b zq7 found nowhere
prose quoted strings tested: 3; files in corpus: 386; not found: 1
$ python3 -I shortq7b.py <the piece in the Mirny folder>   # the piece excluded from its own corpus; this record not in the corpus
prose quoted strings tested: 299; files in corpus: 385; not found: 0
$ python3 -I shortq7b.py <the piece> --nodot   # the same, without the reader dot-files
  NOT FOUND L10: Step 7 Ln
  NOT FOUND L94: any line naming Q-20
  NOT FOUND L301: five early-step pointer lines identical: True
  NOT FOUND L301: P4 and P5 pointer lines identical: True
  NOT FOUND L708: one moderate flag (re-derived)
  NOT FOUND L708: dispositioned in the layer
  NOT FOUND L1140: alone it transfers
  NOT FOUND L1497: Nothing here suggests the ratio crosses the ~3 : 1 flag, and **only a count can show it**
  NOT FOUND L1756: (post-war; another location: not used)
prose quoted strings tested: 299; files in corpus: 125; not found: 9
$ grep -nF <each string the second run could not see> <the reader file it quotes>   # prints line:first 48 characters
58:**Reader A, T8 Round 1, piece ST7b. Status of
280:== G0b-3 Q-20 wording, October pattern (any 
385:five early-step pointer lines identical: Tru
386:P4 and P5 pointer lines identical: True
627:- **New result: PASS, one moderate flag (re-
539:**New result: PASS; the October flag (F-10) 
721:- **The strongest finding** (`DR-113`; `ANS`
1080:**The ratio.** **Not counted here, and not 
213:  - **The merge should write that clause as 
$ python3 -I shortq7b.py <this record, before the check and sweep blocks were pasted>   # its own quotations
prose quoted strings tested: 41; files in corpus: 386; not found: 0
$ python3 -I triage.py <the piece> qaudit_run1.txt   # each audit miss: between two quotations, or inside one?
  inside a quotation: L1497
audit misses: 45 between two quotations (connective prose); 1 inside a quotation

$ python3 -I checks7b.py city ctl_names.md   # positive control: three planted names
  hit L1 (name withheld, 4 chars)
== ctl_names.md: names scanned 53; hits 3
$ python3 -I checks7b.py city <piece>
== Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md: names scanned 53; hits 0
$ python3 -I checks7b.py city <this record, before the check and sweep blocks were pasted>
== Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09b_T8_Rounds.md: names scanned 53; hits 0
$ python3 -I checks7b.py city <each Round 2 raw file>
== .t8_amend_ST7b_round2_raw.txt: names scanned 53; hits 0
== .t8_amend_ST7bD_round2_raw.txt: names scanned 53; hits 0

$ python3 -I checks7b.py ids <piece>   # the readers' own IDs ("A AS7b-n", "its AQ-n", D's AS7bD-n) excluded
AS7b cited  : 1 .. 39 (39 distinct)
AS7b headed : 1 .. 39 (39 distinct)
AS7b in mapping table (bold): 1 .. 39 (39 distinct)
cited but not headed: [] | headed but not in mapping: []
DK7b-: cited 1..17 (17 distinct); defined 1..17 (17 distinct); cited not defined: []; defined not cited elsewhere: []
AR-28x: cited 280..287 (8 distinct); defined 280..287 (8 distinct); cited not defined: []; defined not cited elsewhere: []
AQ-28x/29x: cited 280..294 (15 distinct); defined 280..294 (15 distinct); cited not defined: []; defined not cited elsewhere: []
RF-ST7b-: cited 1..8 (8 distinct); defined 1..8 (8 distinct); cited not defined: []; defined not cited elsewhere: []
DEC-: cited 14..203 (11 distinct); defined - (0 distinct); cited not defined: [14, 16, 20, 42, 140, 141, 142, 160, 161, 180, 203]; defined not cited elsewhere: []
$ python3 -I checks7b.py map <piece>   # every reader item mapped; every docket row traced
A: R1 findings 1..34; mapped 34; missing []
B: R1 findings 1..19; mapped 19; missing []
C: R1 findings 1..14; mapped 14; missing []
D: R1 findings 1..16; mapped 16; missing []
A docket rows 1..8 mapped 8; missing []
B docket rows 1..9 mapped 9; missing []
C docket rows 1..6 mapped 6; missing []
A AR mapped [280, 281, 282, 283]; missing []
B AR mapped [280, 281, 282, 283, 284]; missing []
C AR mapped [280, 281, 282, 283, 284]; missing []
D AR mapped [290, 291, 292, 293]; missing []
A AQ mapped [280, 281, 282, 283]; missing []
B AQ mapped [280, 281, 282, 283, 284, 285]; missing []
C AQ mapped [280, 281, 282, 283, 284, 285]; missing []
D AQ mapped [290, 291, 292, 293, 294]; missing []
A RF mapped [1, 2, 3]; missing []
B RF mapped [1, 2, 3, 4]; missing []
C RF mapped [1, 2, 3, 4]; missing []
docket rows 17; rows without a traced finding: []

$ python3 -I checks7b.py mix ctl_mix.md   # positive control: one mixed line, two mixed blocks, one docket row
  line mix L4: old ['1,351,430'] live ['1,403,549']
prose line-level mixes: 1
  block mix ### AS7b-99 · control: old ['1,351,430'] live ['1,403,549']
  block mix ### AS7b-98 · control two: old ['1,351,430', '665,901'] live ['692,971']
finding-block mixes (prose only): 2
docket rows carrying an old-frame figure: 1
$ python3 -I checks7b.py mix <piece>   # prose only: the pasted raw blocks are records and are excluded
prose line-level mixes: 0
finding-block mixes (prose only): 0
docket rows carrying an old-frame figure: 0
  old-frame figure in prose at L1084: ['\\bfourteen\\b']
$ python3 -I checks7b.py keep <piece>
occurrences of keeper/keepers: 61 in all; 0 in prose outside pasted raw blocks

$ wc -l <piece> <this record, before the check and sweep blocks were pasted>
  1790 Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md
   724 Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09b_T8_Rounds.md
  2514 total
$ grep -c "^### AS7b-" <piece>; grep -c "^| DK7b-" <piece>; grep -c "^```" <piece>
39
17
46
$ python3 -I build.py . /dev/null   # the paste log re-printed (output to /dev/null; the piece is not rewritten): each block, the lines omitted, the lines written
A L243-L376 omitted 2 fence False -> 132 lines
A L379-L403 omitted 0 fence False -> 25 lines
C L341-L382 omitted 0 fence False -> 42 lines
C L410-L459 omitted 0 fence False -> 50 lines
B L414-L425 omitted 0 fence True -> 14 lines
C L537-L551 omitted 0 fence False -> 15 lines
D L206-L224 omitted 0 fence False -> 19 lines
A L419-L460 omitted 0 fence False -> 42 lines
A L463-L543 omitted 0 fence False -> 81 lines
C L599-L615 omitted 0 fence False -> 17 lines
A L555-L621 omitted 0 fence False -> 67 lines
A L633-L691 omitted 0 fence False -> 59 lines
A L694-L750 omitted 0 fence False -> 57 lines
C L747-L815 omitted 0 fence False -> 69 lines
D L229-L297 omitted 0 fence False -> 69 lines
D L312-L356 omitted 0 fence False -> 45 lines
D L357-L368 omitted 0 fence False -> 12 lines
D L373-L405 omitted 0 fence False -> 33 lines
A L780-L854 omitted 2 fence False -> 73 lines
B L767-L774 omitted 0 fence True -> 10 lines
D L410-L436 omitted 0 fence False -> 27 lines
A L867-L984 omitted 5 fence False -> 113 lines
D L441-L457 omitted 0 fence False -> 17 lines
lines written: 1790
$ cmp piece_draft.md <piece> && echo identical   # the piece in the folder is the built draft
identical
```
**Reading the checks.** *Quotations:* the check's control found its two real quotations (`DRL` L1868 and L686) and missed the planted one, as it should; the piece's 299 quoted prose strings are all found with the piece excluded from the corpus. Without the reader dot-files nine strings remain, each a reader's own wording quoted as that reader's, and `grep -nF` finds each at its line: A's label (A L58) and its Q-20 pattern (A L280); C's identity-check output (C L385, L386); A's and B's Gate 2 wordings (A L627, B L539); B's Gate 4 sentence (B L721); C's ratio sentence (C L1080); C's Round 3 replacement clause (`.t8_amend_ST7b_round3_readerC.md` L213). This record's own 41 quoted strings are all found. The mechanical triage puts 45 of the audit's 46 misses between two quotations and one inside a quotation (C L1080's sentence). *Names:* no other location's name in the piece, in this record before these blocks were pasted, or in either Round 2 raw file. *IDs:* AS7b-1 to AS7b-39 are each headed once, cited and in the mapping table; DK7b-1 to DK7b-17, AR-280 to AR-287, AQ-280 to AQ-294 and RF-ST7b-1 to RF-ST7b-8 are each defined and cited; the eleven DEC numbers are cited, not defined, because they belong to the decisions file and earlier pieces (DEC-014, DEC-016, DEC-020, DEC-042, DEC-140 to DEC-142, DEC-160, DEC-161, DEC-180, DEC-203), and **no new DEC number is assigned**. *Mapping:* every reader item is mapped (A's 34, B's 19, C's 14 and D's 16 findings; A's 8, B's 9 and C's 6 docket rows; every request, question and reserved finding of A, B, C and D), and every docket row names the finding it serves. *Figures:* no prose line, no finding block and no docket row carries both the old frame's and the live figures; the one old-frame word in the prose (L1084, "fourteen stocks") names a retired pattern in quotation marks, with no live figure on the line. *The coinage:* 61 occurrences, all inside pasted raw blocks (the pass's own lines); none in the piece's prose. **Counts:** the piece has 1,790 lines, 39 findings (AS7b-1 to AS7b-39), 17 docket rows (DK7b-1 to DK7b-17), 8 requests (AR-280 to AR-287; AR-284 and AR-287 answered), 15 questions (AQ-280 to AQ-294; AQ-294 answered), 8 reserved findings (RF-ST7b-1 to RF-ST7b-8), 27 errata (E1′ to E16 as they now read, E17 to E27 new), 11 decisions proposed and 23 pasted raw blocks (46 fence lines, paired), 9 pasted lines omitted for naming another location.
**Edits to the piece after the audit:** none. The piece was not changed after the audit run; its line count is the audited one (1,790), and the folder copy is byte-identical to the built draft (`cmp`, the last check above).


## American English sweep
**Words checked** (the script's pattern, `st7b_merge/ae_sweep7b.py`, the same as the symbols piece's; named here by their American forms, so that listing them does not plant the British forms in this record): the -ize, -ized, -izes, -izing, -ization and -yze families written with an s (less an allow list of American words that end in -ise, such as premise, rise, otherwise, exercise and the forms of improvise and revise); the British forms of color, behavior, center, centered, license, defense, offense, favor, honor, labor, neighbor and harbor with their forms; of organize, recognize, realize and finalize; of traveled, canceled, modeled and labeled with their -ing forms; of fulfill, enroll, gray, catalog, dialog, program, meter, liter and analog; and of toward, while, among, learned, spelled, dreamed, acknowledgment and aging. The script also counts the one British spelling the developer keeps, without printing the word, so pasting this block does not change the count. Run with `python3 -I` on both files after every other section of this record was written; a final name scan and a final quotation check of this record are added at the end.

raw output, excerpted (14 lines omitted: the positive control's hit lines, which print the fourteen planted British spellings, so pasting them would put those spellings into this record; the control's summary lines are kept; the control is reproducible from `st7b_merge/ctl_ae.md`):
```
$ python3 -I ae_sweep7b.py ctl_ae.md   # positive control: fourteen planted British spellings, one planted kept spelling
== ctl_ae.md
British-spelling hits: 14
kept spelling (the one allowed British form): 1
$ python3 -I ae_sweep7b.py <piece> <this record, before this block was pasted>
== Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md
British-spelling hits: 0
kept spelling (the one allowed British form): 1
== Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09b_T8_Rounds.md
British-spelling hits: 0
kept spelling (the one allowed British form): 0
$ python3 -I checks7b.py city <piece>; python3 -I checks7b.py city <this record>   # a final name scan after the check block was pasted
== Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md: names scanned 53; hits 0
== Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09b_T8_Rounds.md: names scanned 53; hits 0
$ python3 -I shortq7b.py <this record, before this block was pasted>   # its quotations, after the check block was pasted
prose quoted strings tested: 42; files in corpus: 386; not found: 0
```
**Result:** no British spelling in either file; the one kept spelling occurs once, in the piece (section 6's confidence key); this record carries none. The control found all fifteen planted forms (fourteen hits and the kept one). No other location's name is in either file, and every quotation in this record is found at its source.
