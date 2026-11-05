# Mirny · Amendment re-derivation · Piece ST6 (Step 6, Differentiation) · T8 round record · 2026-11-04

**Companion to** `Amendment_Rederivation_ST6_Differentiation_2026-11-04.md`. Raw tool output is pasted, not summarized; the one excerpt is labeled. Working files are in this folder as `.t8_amend_ST6_*`.

## Setup
- **Reading list (trimmed, `DR-74`):** `.t8_required_amend_ST6.txt` (scratchpad copy `amend_ST6/t8_required_amend_ST6.txt`), **25 entries, about 4,346 admitted lines** (ranges summed and whole files counted by a read-only script on the list): the rules (entry 1, the stereotypes law; 2, the runbook's spans; 3, `04` Part III; 4, the Tier U quick reference; 5, the rulings log at 24 spans); the live sources at Mirny's rows only (6 to 11: the census, the Founding Register, the Mirny spec, the relationship database, the immigration composition file, the language blocs); 12, the Step 6 datasheet; **13, `06_Differentiation.md` read whole (380 lines)**; 14, Step 5's spans; 15, the Frame's spans; 16 to 25, the amendment layer (the Phase 6, 7, 2, 9 and 8 pieces, the Phase 8 dockets, the Idelsk-Uralia piece, the robot-term piece's first 30 lines, the amendment register, the reconciliation note's lines 1 to 120). The shared differentiation table and every other location's row were on no list. **The Phase 10 piece (U5) and the Step 5 piece (U6) were not inputs** (concurrent).
- **Brief:** `.t8_amend_ST6_brief.md`, identical for A/B/C with `{X}` the reader letter; **sha256[:16] 797c8db9ce543708** (computed by this merge on the folder copy and on the scratchpad copy: both match); final at dispatch (`M-93`). It carries ten orchestrator-verified results with sources (its standing line 4 says "eight"), the developer's binding words, the stage order and twelve traps.
- **Readers:** three Opus agents dispatched 09:55 on 2026-11-04, inside the 05:00 to 14:59 window (checkpoint; the progress file's U7 row). None refused any entry. Graphify: readers A and B record disregarding the hook under `DR-6`; reader C records "any graphify hook disregarded per the brief (DR-6)".

| Reader | Agent ID | Output lines | Bytes | PROOF blocks | Findings (Round 1 numbering) | Docket rows | Requests · questions · RFs |
|---|---|--:|--:|--:|---|---|---|
| A | `a2a25af571a1319aa` | 941 | 130,933 | 25 | AS6-1 to AS6-12 | D6-1 to D6-42 | AR-100 to AR-105 · AQ-90 to AQ-97 · RF-ST6-1 to RF-ST6-3 |
| B | `ab26541080658383b` | 977 | 138,297 | 25 | AS6-1 to AS6-11 | DS6-1 to DS6-36 | AR-100 to AR-106 · AQ-90 to AQ-97 · RF-ST6-1 to RF-ST6-6 |
| C | `a7f68d64617c0701e` | 1,077 | 151,284 | 25 | AS6-1 to AS6-20 | D6-1 to D6-26 | AR-100 to AR-107 · AQ-90 to AQ-96 · RF-ST6-1 to RF-ST6-10 |

Line and byte counts by `wc` on the folder copies; PROOF blocks counted by `grep -c '^### PROOF:'` (25 each). The folder copies of the three Round 1 outputs and the three Round 3 replies are byte-identical to the scratchpad copies (`cmp`). Tool-use counts are not recorded in the checkpoint and are not given here.
- **Self-checks before handback (as each reader records):** A ran `wc -l` and last-byte checks on every whole file and blank-line checks on the positional lines ("no content generated"). B's snag S-15: a read-only comparison found four of its own hand-copied PROOF slips, each fixed by hand, and three own-wording strings inside quotation marks, unquoted. C's snag 16: two draft quotations failed its own check and four own-wording strings were unquoted; a read-only inline check then matched all 25 PROOF blocks and all checked quotations.
- **Ruling-log freeze (`M-302`):** not checked by this merge writer.

## Round 1 headline claims (union, before Round 3)
| Claim | A | B | C |
|---|---|---|---|
| Register L138's direction ("later losses are communal") overstates | yes | yes | yes |
| Register L139, L140, L141 are RE-DERIVE, not REWORD | yes | yes | yes |
| Governance and Dress are RE-DERIVE (the register has REWORD) | yes | yes | yes |
| "six of nine lines": the six named cells sit on three lines | yes | yes | yes |
| Destination lines that change | §4 to §7, plus §1 bookkeeping | §1, §4, §5, §6, §7, §9 | §1 (Pass), §4, §5, §6, §7, §9 |
| NS-11 | REWORD | REWORD | REWORD |
| L133 RE-DERIVE, PROVISIONAL on AIU-14 | yes | yes | yes |
| The datasheet's ten sections and Phase-axis column | shown as candidates | proposed, marked "new" | CAND |
| §2 handoffs | re-dispositioned | not re-run | records marked; H-8 to H-13 added |
| §3.1 3rd finding | in the body; the loss changes kind | in the body; the lesson "written" | reserved; the lesson "kept" |
| S6-RF-4 | CLOSE as to its ground | re-derived narrow, reserved | RE-DERIVE narrower, reserved |
| S6-RF-9 | CLOSE | falls | RE-DERIVE (a first-generation witness) |
| L301 | RE-DERIVE | record only | RE-DERIVE |
| PR-5 | RE-DERIVE | "changed" | REWORD |
| PR-10, Q-117 | RE-DERIVE; Q-117 CLOSE as to Step 6 | resolved | CLOSE both |
| §5 Meaning cell | of learning and response | of going, not of blame | on what was learned once and who responds |
| §6 Governance cell | who goes; no one may send them | compelling the response; obedience unassigned | the response, not the reading; a warning curated and issued |
| §5 Observance cell | axis, plus a CST clause | occasions of knowing; no day for a failure | occasions of knowing, not of failing |
| §9 Category cell | crossed by teaching and exposure | crossed by being taught | crossed by being taught here |
| New no-sibling rows | none | NS-12 | NS-12, NS-13 |
| Numbering | AS6-1 to AS6-12 | AS6-1 to AS6-11 | AS6-1 to AS6-20 |

## Round 2 (`Tools/triple_read_verify.py`) · run 2026-11-04 (raw file time 10:28) · UNANIMOUS (75 of 75 field sets)
raw output (full; file `.t8_amend_ST6_round2_raw.txt`):
```
required files: 25
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 309-372,378-426,430-540,2886-2920] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/04_QA_Gates_and_Differentiation.md  [range 420-525] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Corpus_Reference_Sheets/Differentiation_Instrument_Quick_Reference.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 203-251,422-435,448-461,463-475,510-524,538-553,609-621,953-965,1075-1088,1092-1107,1111-1133,1137-1156,1211-1226,1404-1412,1427-1434,1438-1445,1460-1468,1472-1479,1523-1530,1550-1557,1570-1577,1655-1662,1664-1671,1707-1715] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md  [range 1-38,370-378,500,642,839-892] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Founding_Register.md  [range 1-31,57,88] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Mirny.md  [range 1-3,13-72,92-94,103-109,118-150,152-154,160-165,171-173,195-199,205-207] ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Step_6.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/06_Differentiation.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/05_Reconciliation.md  [range 1-8,80-109,712-722] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00_Frame.md  [range 130-175,219-236,463-466] ===
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

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

## Round 3 (SendMessage to the same three agents) · 2026-11-04 about 10:45 · cross-check done
Each reader was sent seven points the three appeared to share (K1 to K7), a request to map the other two readers' findings onto the old Step 6 IDs and list every category, central-claim or cell split, a request to check the single-finder finds against the pass lines, a numbering proposal, and a request to list any claim in the other two re-derivations it would not accept. Replies are saved as `.t8_amend_ST6_round3_reader{A,B,C}.md`. **The text of K1 to K7 as sent is not in the folder; the topics below are read from the replies.**

| Reader | Part 1 OBJECTs | Part 2 splits listed | Single-finder finds checked | Part 3 claims not accepted | Coverage |
|---|---|---|---|---|---|
| A | 2 (K2, wording; K6) | 27 (concedes on 9: splits 4 in part, 10 in part, 11, 13, 15, 19, 20, 22, 24) | 14 (13 CONFIRM; 1 confirmed in substance with an OBJECT to a separate row); offers 3 of its own | 9 | read B L366 to L767 and C L347 to L870 |
| B | 1 (K2, wording) | 29 (12 concessions: splits 2, 3, 7, 11, 12, 15, 17, 18, 22, 28, 29, and its §2 miss) | 13 (11 CONFIRM, 1 OBJECT, 1 its own kept) | 4 | read A L325 to L729 and C L347 to L871 |
| C | 1 (K2, wording) | 22 (S1 to S22; explicit concessions on S2, S4, S6, S16, S17, S20; holds another reader's form on S5, S7, S9, S10, S12, S15) | 17 rows (14 CONFIRM, one of them flagged; 2 OBJECT; 1 its own offered) | 5 | read A at L325 to L731 and B at L366 to L767, by part |

### The shared points
| K | Topic (as read from the replies) | A | B | C |
|---|---|---|---|---|
| K1 | the six named §5 cells and the tense row: tense row, S6-RF-2, Meaning, Transmission, Counterculture RE-DERIVE; Governance and Dress RE-DERIVE against the register's REWORD | AGREE | AGREE (adds Observance REWORD) | AGREE |
| K2 | the register's count (six cells on three lines) and the cells it misses; as sent it named "Language cells (sections 4 and 7)" | **OBJECT (wording):** §4 has no Language cell; the misses are the §4 Axis, §7 Language, §1 Deficit address and the §9 cells | **OBJECT (wording):** the same; six lines change through a different list | **OBJECT (wording):** §4's missed cell is the Ordinary Life axis; six lines by a different list (A counts four plus §1's bookkeeping) |
| K3 | the datasheet's ten sections and Phase-axis column: an under-fill; the three Phase-axis cells from rulings and the accepted Phase 8 line; §10 pending | AGREE | AGREE (the structure rests on the datasheet alone) | AGREE |
| K4 | NS-11 REWORD; "risk lowered" not shown | AGREE | AGREE | AGREE |
| K5 | L133 RE-DERIVE, PROVISIONAL on AIU-14; "descent" dropped | AGREE | AGREE | AGREE |
| K6 | PR-5, L301, PR-10 and Q-117 | **OBJECT:** PR-5 REWORD (concedes to C); L301 split (report a record, conclusion RE-DERIVE); PR-10 and Q-117 CLOSE as to Step 6 (concedes) | AGREE: PR-5 RE-DERIVE; L301's conclusion RE-DERIVE (concedes its record-only mark); PR-10, Q-117 CLOSE | AGREE: PR-5 RE-DERIVE (concedes); L301 RE-DERIVE for its conclusion; PR-10, Q-117 CLOSE |
| K7 | the four substitutes re-run peer-free; §3.5 re-derived | AGREE (the properties differ in emphasis only) | AGREE | AGREE |

### The splits, and how they were settled in the merge (the position two or three hold after concessions; else the most conservative reading; split named in the piece)
| # | Point | Positions (Round 1 → Round 3) | Settlement |
|--:|---|---|---|
| 1 | §1 Deficit address (L180) | A, C drop the carriers; B adds "blamed by the first generation, taught after"; R3: B conceded | **A/C**: the spine's grade only; REWORD |
| 2 | §4 Axis (L198) | three wordings; R3: A holds A's with C's "one's own call" and "the warnings dark in the outage"; B holds C's; C holds B's | **no two readers hold the same text: the most conservative composition**: B's wording (held by C), keeping the object's own word "decided" for the person's call (A's and B's point): *crossings decided on a taught cue and a warning the storm can silence*; RE-DERIVE, weak; the silencing clause conditional (AR-24) |
| 3 | §5 Meaning (L204) | A "of learning and response"; B "of going, not of blame"; C "on what was learned once and who responds"; R3: A holds A's plus "uncompelled"; B holds C's (optionally with A's call clause); C holds A and C merged | **C's merged form** (B and C hold C-based forms; every element A holds is in it): *A Social Contract of learning once and responding — taught to all, danger told, the call at the door one's own; whoever is most able goes, uncompelled*; A's head ("of learning and response", to avoid echoing the Phase-axis cell) named |
| 4 | §5 Observance (L205) | A axis only (R3: concedes its CST clause to the check column); B, C hold C's "occasions of knowing, not of failing" in the cell | **majority B/C, but A's Part 3 does not accept the clause in the cell** (claims not accepted are excluded): the cell holds the axis only, *Dated by the light, or called on the day [CAND]*; the Phase 6 piece's [D] reading goes to the check column, with the empty-slot note and the stage order. **Not settled cleanly by the rule** (the two rules pull apart; AQ-101) |
| 5 | Beside the Meaning cell (L208) | A RE-DERIVE (mechanism); B, C REWORD, pending | **REWORD** (B, C), pending the Step 5 piece; the mechanism in ruled facts only (B's text) |
| 6 | §6 Governance (L213) | A "who goes; no one may send them"; B "compelling the response … obedience to a warning is unassigned"; C "the response, not the reading; a warning is curated and issued"; R3: A holds A's (obedience to the source column; "issued" implies an issuer); B holds C's; C holds B's | **no two readers hold the same text: the most conservative composition**: B's head and first clause (held by C), A's "may" not carried (B, C object), the obedience clause moved to the source column (A's point, the object's own class rule at L173), C's "issued" not carried (A): *Compelling the response — who goes is each person's own judgment of who is most able*; RE-DERIVE (AQ-101; DEC-042) |
| 7 | §6 Transmission (L214) | second clause: A, B "only the moment at the door is witnessed"; C "no examiner is admitted"; R3: C conceded | **A/C head, C's ruled body, A/B's second clause**: *Made here, taught to all — the skill the site demands passes person to person from its own first generation; only the moment at the door is witnessed*; "no examiner" to the source column |
| 8 | §6 Counterculture (L215) | A "a second path"; B "for what the relay carries"; C "for what the one path carries"; R3: A holds B's | **B's** (A, B) |
| 9 | §7 Language (L222) | A, B the tense axis; C "The taught terms, not the tongue or an accent"; R3: C conceded B's wording | **B's wording** (all three); C's A8-8 point to the source column |
| 10 | §7 Dress (L221), not raised in Round 3 | A, B "taught and warned"; C "informed and warned" | **"informed and warned"**: the accepted Phase 8 piece's own word (`AREG` L104), the conservative reading; named |
| 11 | §9 Category (L234) | A "teaching and exposure"; B, C "being taught" (neither answered A in Round 3) | **majority B/C, but A's Part 3 does not accept dropping exposure** (excluded): *crossed by teaching and exposure* (`PP9` L144), the conservative reading. **Not settled cleanly by the rule** (AQ-101) |
| 12 | Row 5's founding cell (L71): the civic language at the founding | A adds it (second-hand source); B, C later frame only; R3: A conceded; C held A's, flagged | **crossed concessions**: two hold "later frame only" (A, B): not carried |
| 13 | §3.4 L134's status | A "no longer unresolved by design"; B, C "unresolved by design"; R3: A conceded | **unresolved by design**; lived, no longer as a booking; the collision reserved (RF-ST6-7) |
| 14 | §3.4 3rd finding (L139) | A place and tense key the response; B the duty's timing; C where the storm meets the channel; R3: A holds B's; B holds A's; C holds A's | **A's** (B, C); B's and C's keys named as alternatives for the developer |
| 15 | §3.4 2nd finding | A in the body [D, soft]; B the ruled axis's halves, reserved; C the collision, reserved; R3: B holds C | **reserved** (RF-ST6-7 the collision; RF-ST6-4 the axis halves) |
| 16 | §3.4 L126's status | B "resolved in part by Mirny's own making"; A, C holds; R3: B conceded | **holds as the founding conflict**; found and made reserved (RF-ST6-6) |
| 17 | §3.1 3rd finding: placement | A, B in the body; C reserved; R3: B holds A | **in the body** (A, B); its tense-column use reserved (S6-RF-2) |
| 18 | §3.1 3rd finding: wording | A the loss changes kind; B the lesson "written"; C the lesson "kept"; R3: B conceded C's | **C's wording** (B, C; A's the same claim) |
| 19 | S6-RF-3 (L95, L324) | A the one scale at which a person answers; B no longer the only scale; C a loss and now a response; R3: B conceded C; A holds A/C; C proposes one neutral line | **C's neutral line** (A/C): *the city is the one scale at which a loss lands on a nameable person, and the duty now puts a nameable person where the relay fails*; reserved |
| 20 | S6-RF-4 (L325) | A CLOSE as to its ground; B narrow, reserved; C narrower, reserved; R3: A conceded RE-DERIVE narrow; B and C conceded CLOSE | **crossed concessions**: two hold CLOSE (B, C): **CLOSE**, with a pointer to A7-18 (the record kept by the pointer) |
| 21 | S6-RF-6 (L327) | A REWORD; B half falls; C RE-DERIVE; R3: B holds C; C conceded REWORD | **REWORD** (A, C) |
| 22 | S6-RF-7 (L80, L328) | A "older than the duty"; B the duty binds from the relay's onset; C overlap open; R3: C holds B's | **B's form** (B, C); A's not carried (Part 3, C) |
| 23 | S6-RF-9, Q-121 (L330, L356) | A CLOSE; B falls; C RE-DERIVE to a witness candidate; R3: C withdrew; A would keep the witness as Q-121's reworded half | **CLOSE** (all); A's Q-121 proposal not carried (B, C) |
| 24 | S6-RF-5 (L326) | all CLOSE | **CLOSE**: *for the first generation a limit; after it, neither — the instruments exist* (A's Round 3 wording) |
| 25 | §3.5 property (S6-RF-1) | A, B, C differ in emphasis; R3: B holds A's wording plus C's guilt clause and concedes the relay off the "not handed on" list | **A's wording plus C's guilt clause** (B, C hold the guilt clause; A does not object) |
| 26 | NS-2, NS-5, NS-6 | A, C REWORD; B KEEP; R3: B conceded | **REWORD** |
| 27 | NS-10 | A, C RE-DERIVE; B at risk, pending; R3: B holds A/C | **RE-DERIVE**, pending the Step 5 piece |
| 28 | New no-sibling rows | B NS-12; C NS-12 and NS-13 | **one NS-12** (B's with C's folded in); C's NS-13 dropped (all three; C withdrew) |
| 29 | Phase-axis cells' category | A, C CAND; B "new"; R3: B conceded | **CAND** |
| 30 | §10 cell | A CAND held; B flagged, not filled; C CAND; R3: B conceded | **CAND, held** (pending the Phase 10 piece) |
| 31 | §6 Governance swap verdict | A, C keep, weak; B keep; R3: B conceded | **keep, weak** |
| 32 | §2 handoffs H-2, H-3, H-5 | A re-dispositioned; B not re-run; C records plus H-8 to H-13; R3: A, B conceded | **C's form** |
| 33 | PR-5 (L263) | A RE-DERIVE; B "changed"; C REWORD; R3: A conceded REWORD; C conceded RE-DERIVE; B RE-DERIVE | **crossed concessions**: two hold RE-DERIVE (B, C): **RE-DERIVE**; A's REWORD named |
| 34 | L301 | A, C RE-DERIVE; B record only; R3: all split the line | **the report a record (marked); the conclusion RE-DERIVE** |
| 35 | PR-10, Q-117 | A RE-DERIVE (Q-117 CLOSE); B resolved; C CLOSE; R3: A conceded | **CLOSE as to Step 6** |
| 36 | PR-12 to PR-15 | A PR-12 shared axis, PR-13 the L3 notice; B PR-12 shared axis, PR-13 national root; C PR-12 same-commit, PR-13 under-fill; R3: three orderings | **PR-12 the ruled shared axis (all); PR-13 the under-fill and PR-15 the national root (A, B keep both as items; C folds the under-fill); PR-14 the stale own row and the same-commit request (A's and C's order)**; A's L3 item to the docket (all) |
| 37 | The two readings meeting at the relay | B in the body; C reserved; R3: B conceded | **reserved** (RF-ST6-8) |
| 38 | The tense row's Act headers | B ties the knowledge system to Act 2; C reads the first generation as Act 1, the brief's reading (AR-14); R3: B conceded | **C's reading** |
| 39 | Q-120 | A, B KEEP; C REWORD | **KEEP** (A, B) |
| 40 | R-145 | A REWORD; B waits; C KEEP; R3: A conceded | **KEEP**, content pending |
| 41 | Destination lines that change | A four plus §1; B, C six; R3: A conceded | **six** (§1 bookkeeping, §4, §5, §6, §7, §9); the coincidence with the register's number recorded |
| 42 | Finding numbering | A proposed C's 20-item set; B proposed an 18-item set; C proposed A's 12-item set | **one 19-item set in Step 6's own order** (§2 to §9, propagation before the swap test as in the object, live numbers before the §9 re-sort), close to B's granularity |
| 43 | Reserved-finding numbering | A: re-derived old findings keep S6-RF-n, RF-ST6-n only for findings with no old ID; B, C numbered re-derived ones as new RF-ST6-n | **A's principle** (keeps the record; the earlier pieces' practice): RF-ST6-1 to RF-ST6-9 as A proposed |
| 44 | Request numbering | AR-100 the table (all); AR-101 Phase 4 and AR-102 the spine (A, C); B swapped them; the pending §10 and Meaning-pair items requests (A, B) or not (C) | **AR-100 to AR-107 in C's order; AR-108, AR-109 the pending items (A, B)**; AR-16, AR-24 keep their IDs (all) |
| 45 | Question numbering | AQ-90 to AQ-94 (all); AQ-95 the Observance column (B, C); later items in three orders | **AQ-95 (B, C); AQ-96 to AQ-100 in B's order; AQ-101 A's Governance-wording question widened**; B's Round 1 L59 and L27 questions are docket rows (B in Round 3; C) |
| 46 | Docket numbering | A D6-1 to D6-42; B DS6-n; C D6-1 to D6-26 | **A's numbers kept** (A, C), additions from D6-43 |
| 47 | L380's "census tier weights" mark | C mark; A included it in its proposed D6-48; B OBJECT (the T4 line is a true record) | **D6-48 kept as a row proposing no mark** (the conservative form: changes nothing, keeps the record of the split) |

### Single-finder finds, checked against the pass lines in Round 3
| Find | Finder | Checked by | In the merge |
|---|---|---|---|
| L295 says "column" for a city table that holds rows | C | A, B CONFIRM (low) | D6-45 |
| PA-81's trigger names a Phase 9 Q-66 that `DR-55` lists under Phase 7 | C | A, B CONFIRM | AS6-19; snag 16 |
| The datasheet keeps a sentence the quick reference removed as unsourced (`DS6` L10, L34 to L35; `QR` L95) | B, C (two finders) | A CONFIRM | snag 12; AQ-100 |
| The brief's "and its dockets" against `DR-105`'s three held results | B | A, C CONFIRM | snag 11 |
| NS-12: the first generation taught everyone after | B | A, C CONFIRM | AS6-12 |
| NS-13: the duty without compulsion as its own row | C | A CONFIRM in substance, OBJECT to a separate row; B: drop; C withdrew | not carried (NS-3) |
| The double reading's lived form is the ruled axis | B | A, C CONFIRM as reserved | RF-ST6-4 |
| Substitute 3 now sorts Mirny's own two states | B | A CONFIRM (two finders) | RF-ST6-5 |
| Found governs the machine, made governs the weather | B | A CONFIRM as reserved | RF-ST6-6 |
| NS-10 inverted | C | A CONFIRM (two finders); B holds A/C | RF-ST6-9 |
| The two readings also meet at the relay | C | A CONFIRM as reserved; B conceded | RF-ST6-8 |
| Whether the Language column may carry the supporting-tier result | C | A, B CONFIRM | AR-107 |
| Whether the corrected row reaches the table in the same commit as the acceptance | C | A, B CONFIRM as a request only | AR-105; PR-14 |
| H-8 to H-13 from the amendment layer | C | B CONFIRM (its own miss); A routes the same feeds | AS6-1 |
| In Act 2 the founding robot is where Meaning, Order and Populations meet | A | B, C CONFIRM as reserved | RF-ST6-3 |
| The Phase 8 axis wording has no admitted developer line, only `AREG` L90 | A | B CONFIRM (its S-8) | AR-104 |
| The feed lines drifted +4 (`05` L718 to L720); the runbook span is 2886 to 2920 | A | B, C CONFIRM | AS6-1; snag 6 |
| L171's 21 holds only without §1's Pass and with §4 as its Axis alone | A | C CONFIRM | D6-42; snag 5 |
| The other reading's tier share as written against live, kept apart | A | B, C CONFIRM | AS6-18 |
| §8: Mirny's own warnings on the relay are internal, not a relation | A | C CONFIRM | AS6-13 §8 |
| PR-5's new rests-on class: the relay's technology | A | C CONFIRM | AS6-15 |
| Row 5: the civic language at the founding | A | C CONFIRM, flagged; A conceded | not carried (split 12) |
| Reading B is no longer silent while the signal holds | B | C CONFIRM | AS6-10 |
| The quick reference's two pre-ruling phrasings still stand | B (also A's and C's snags) | C CONFIRM | AQ-100 |
| The duty's national root, as a note for the terminal check | B | C CONFIRM | PR-15 |
| The L3 notice is stale (A's PR-13) | A | B, C CONFIRM the fact; a docket row, not propagation | D6-1 |
| L380's tier-weights mark | C | A included it; B OBJECT | D6-48, no mark (split 47) |
| B's §1 Deficit clause | B | C OBJECT; A (Part 3) | not carried |
| B's S6-RF-2 "written" | B | C OBJECT; B conceded | not carried |

### Claims not accepted (excluded from the merge)
| Claim | Whose | Objected to by | Why | In the merge |
|---|---|---|---|---|
| K2 as sent: the register misses "Language cells (sections 4 and 7)" | the K2 summary (A's Round 1 file names the §4 Axis and §7 Language cells separately, its L321) | A, B, C | §4 has no Language cell; its missed cell is the Ordinary Life axis | §4 Axis (L198) named (section 2.1) |
| §5 Meaning: "of going, not of blame" | B | A, C (B conceded) | asserts an absence the files leave open (AR-15); drops "danger told" | dropped |
| §1 Deficit address: "blamed by the first generation, taught after" | B | A, C (B conceded) | re-grades the spine's deficit from outside the list; a second axis in the cell | dropped (AR-102) |
| §9 Category: "crossed by being taught" (exposure dropped) | B, C | A | the opposite overstatement against `PP9` L144 | "teaching and exposure" kept |
| §6 Governance: obedience to a warning inside the UNADMINISTRABLE cell; "issued" | B, C (obedience); C ("issued") | A | obedience is UNASSIGNED (`PP7` L201, N5) and the object's class rule (L173) puts it in the source column; "issued" implies an issuer the rulings leave unknown | obedience to the source column; "issued" dropped |
| §7 Language: "The taught terms, not the tongue or an accent" | C | A (C conceded) | asserts as the marker what A8-8 states only conditionally | to the source column |
| §6 Transmission: "no examiner is admitted" in the cell | C | A (C conceded) | a reading of absence inside a cell | to the source column |
| §5 Observance: "occasions of knowing, not of failing" in the cell | C (held by B) | A | carries a [D] reading of two unadopted candidates into the cell | to the check column (split 4) |
| PR-12's span "`DR-56` to `DR-100`" | C | A | the span includes rulings on no list (`DR-78`, `DR-97`) | the rulings named one by one (PR-14) |
| L301 marked as a record only (DS6-28) | B | A (B conceded) | its conclusion is a finding | L301 split |
| §6 Governance: "no one may send them" | A | B, C | turns "nobody is officially required" into a prohibition; non-compelling coordination is open (AR-22) | dropped |
| "restoration by capability, not position" | C | B | the ruling as clarified is capability and position for the hazard, not nearness (`PP6` L20) | corrected (AS6-5, AS6-9) |
| the city's duty for others "to restore the relay and to tell danger", one duty of the same structure | C | B | telling danger is what people learned to do, not a ruled guilt-bearing duty (AR-27) | dropped |
| at the harbor the duty "attaches to a role ruled essential" | C | B | `DR-59` Q-68 rules a tier fact, not a `DR-56` duty | dropped |
| S6-RF-7: "whatever account of a loss the first generation used is older than the duty" | A | C | asserts an order of onsets the files do not date (R-148; PR-9) | B's form |
| §3.1: the lesson "written" into the made knowledge | B | C (B conceded) | the protocol's form is unruled (AR-1, AR-7) | "kept" |
| S6-RF-3: "no longer the only scale at which a loss lands on a nameable person" | B | C (B conceded) | counts guilt for an omission as a loss landing | C's neutral line |

Count: 16 distinct claims (18 objections: "no one may send them" by B and C; "of going, not of blame" by A and C), plus the K2 wording.

## Settled in the merge (beyond the splits)
- **Union applied:** A (the docket base D6-1 to D6-42; the line drift; AR-104; RF-ST6-1 to RF-ST6-3; PR-5's new rests-on class; the §8 internal-not-relation note; the tier-reading note; the §3.5 wording; the S6-RF-5 wording; the reserved-finding numbering principle); B (the X mark; NS-12; RF-ST6-4 to RF-ST6-6; PR-15; the acceptance snag; the Tier U sheets' lag; the §4 base wording; the Governance head; the Counterculture and Language wordings; reading B no longer silent; S6-RF-7's form; the not-yet-taught in the outage); C (H-8 to H-13; the dated dispositions as records; the Meaning cell's merged form; the Transmission body; the word "informed"; L295's "column"; PA-81's trigger; the same-commit request; AR-107; PR-13 and PR-14; RF-ST6-7 to RF-ST6-9; the 23.24 CALC; the 12 + 4 + 7 tally; S6-RF-3's neutral line; S6-RF-2's wording; the Act reading).
- **The concurrent pieces.** The Phase 10 and Step 5 pieces were in the folder (PROPOSED) when this merge began. They were read as form models (header, section 0, their tables, feeds and decision sections) and, for content, only at section 0 and their Step 6 feed rows; the piece's cross-reference note (end of its section 4) records what they propose. Nothing in the piece was changed by them. The Step 7 and Step 8 pieces are concurrent: pending.
- **Figures:** all three readers agree on the live set (1,403,549; robots 50.63 %; 36 stocks; largest 13.73 %; founding share 23.24 %; the PROPOSED tiers 42.2 / 23.1 / 34.7 % of workforce units; English on mid-points). The old figures appear in the piece only on "Old" lines (AS6-18).
- **Shares are weights, never head counts or hours** (`DR-12`). The pass's coinage for the relay's people is never used as a name.
- **Decisions** numbered from DEC-040 (three: DEC-040 to DEC-042).

## Kept files (`M-132`)
The Round 1 outputs `.t8_amend_ST6_readerA.md`, `.t8_amend_ST6_readerB.md`, `.t8_amend_ST6_readerC.md` and the Round 3 replies `.t8_amend_ST6_round3_readerA.md`, `.t8_amend_ST6_round3_readerB.md`, `.t8_amend_ST6_round3_readerC.md` are kept in this folder as the round's working record, unedited, beside `.t8_amend_ST6_round2_raw.txt`, the frozen brief `.t8_amend_ST6_brief.md`, the list `.t8_required_amend_ST6.txt` and the checkpoint `.t8_amend_ST6_CHECKPOINT.md`. They are not inputs to any later step; this record and the piece are the merged result. No helper file was created in the repo by the readers or by this merge (scratch work stayed in the session scratchpad, `amend_ST6_merge/`).

## Quotation audit (`Tools/quotation_audit.py`, `--files Amendment_Rederivation_ST6_Differentiation_2026-11-04.md --own-pass`) · 2026-11-04 · run before this record existed
raw output, excerpted (1 line omitted: the positive control "HARD - case mismatch", whose test phrase names another location; it reported FOUND, and the instrument line below reads VALID; file `amend_ST6_merge/qaudit_final.txt` in the session scratchpad holds the whole output):
```
pass audited : Mirny
corpus mode  : default (own pass excluded)
corpus files : 6089   chars: 69,785,185
files audited: Amendment_Rederivation_ST6_Differentiation_2026-11-04.md
own-pass mode: a quotation may also be found in this pass's OTHER files (never in its own file)

=== POSITIVE CONTROLS ===
  [easy                      ] FOUND     a terminus is nobody's midpoint
  [HARD - blockquote wrap    ] FOUND     A pass may not proceed to Step 5 with a NEVER CITED row
  [HARD - outside Worldspace ] FOUND     Paste raw QA scan output into the QA block. Never summa
  [HARD - long wrapped       ] FOUND     Different content is not differentiation; a different q

  INSTRUMENT VALID: YES
  NEGATIVE CONTROL (must be absent): PASS - absent

=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 80
NOT FOUND in corpus: 29
  of those, in TABLE CELLS : 2
  of those, in PROSE       : 27

  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:98]           all three readers objected: section 4 has no language cell ; its missed cell is the ordinary life axis (l198). reader a's own roun
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:115]           ) l68, l69, l71, l72 (the crisis and later cells; the in-place amendment of row 2 stopped at the later column, c) l76 (no move on 
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:115]           ) (as6-2) l80 (s6-rf-7, as6-4) l86 (the relay row: a debt, not the general social contract; the coinage
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:115]           ) (as6-5) l93, l94 (as6-6) l96, l97 (s6-rf-4, s6-rf-6; as6-6) l103 to l108, l112, l114 (as6-7) l126 (p8-12
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:116]           ) l160 (ns-8's speech slot) l222, l246, l291, l316 (the tongue
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:116]           ) against pp8 l305 l265 (pr-7: 7 language's act statement changes) l317 (r-96's stock count, at as6-19) l220's source (p8-6 re-der
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:116]           both changed) l187's check rests on p2 's test, which the accepted phase 2 piece refines (reach grounds the establishing country o
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:117]           ) l266 (pr-8), l363 (pa-79), l375 (snag 7, a record): founders now in three forms ( dr-9 , dr-46 , dr-99 ); pa-79's overturn condi
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:117]           ) has fired ( piu l245, aq-42) l293 (the register row changed 2026-11-03, freg l57) l112 (
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:118]           so the conflict may be live; still no arbiter, pp7 l363) l88 ( dr-59 q-68: the harbor watch is
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:118]           tier unplaced; dr-56 q-67 adopted: the call public and binding on ships and offload by practice, drl l1130) l186 and l365 (pa-81) 
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:120]           is unchanged; the row's character changed (the property
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:123]           (all three; d6-2) l171's calc (21 excludes 1's pass; snag 5) l295's
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:129]           ); not going, for whoever is at the foremost position, is a cause of
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:149]           (l76); the loss of unwritten judgment recurs at each death; the restorer's loss is
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:151]           ( frm l169) while founding robots are still active (d6-2 corrects l59's
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:178]           whatever account of a loss the first generation used is older than the duty
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:189]           falls. what the city still meets alone and without naming it is each person's own crossing, now informed. not carried (b's objecti
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:189]           as one duty of the same structure (telling danger is what people learned to do, not a ruled guilt-bearing duty; whether the duty r
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:191]           no longer the only scale at which a loss lands on a nameable person
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:280]  [CELL]  (l198); its second clause was the retired premise. new: taught ( dr-56 ) and warned on the relay ( dr-76 ); the silencing clause i
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:292]  [CELL]  is the accepted piece's own word (a and b wrote
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:395]           as6-15, as6-17). the step 5 piece re-derives the strongest finding as a whole and splits leg 4 three ways: the public wind call is
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:397]           the 4 cell's silencing clause is conditional in the same sense (ar-24). its step 6 feed tags the composition cell's
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:398]           ): a public weather report/relay system exists by ruling. consistent with s6-rf-4 close as to its ground, s6-rf-5 close, comparabl
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:573]           the phase 2 piece drops the word ( pp2 l38); the idelsk-uralia piece's aq-46 recommends the phase 2 form. no
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:584]           a did not accept it in the cell) and the 9 category cell (b and c wrote
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:588]           any name for the organization or the protocol; the pass's coinage as any group's name; a form for the warnings; a word for soon st
  [Amendment_Rederivation_ST6_Differentiation_2026-11-04.md:588]           for the duty; guilt as a sanction; a rite of restoration or a day for the first generation

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```
**Triage by hand (each of the 29 misses read and classified):** 80 fragments tested, **29 not found** (2 in table cells, 27 in prose). **27 are connective prose**, this piece's own wording captured between two adjacent quotations (the audit's own warning): L98, L115 (three), L116 (three), L117 (two), L118 (two), L120, L123, L129, L149, L151, L189 (two), L280, L292, L395, L397, L398, L573, L584, L588 (two); none of them is a quotation. At L189 the audit's quote pairing ran offset, so the line's actual quotations were checked by hand: "only to oneself" is in `06_Differentiation.md` L93; "to restore the relay and to tell danger" and "attaches to a role ruled essential" are exact text of `.t8_amend_ST6_readerC.md` L528 (`grep -nF`). **Two are quotations of a reader's Round 1 output, not of the corpus:** L178 ("whatever account of a loss the first generation used is older than the duty", exact text of `.t8_amend_ST6_readerA.md` L447) and L191 ("no longer the only scale at which a loss lands on a nameable person", exact text of `.t8_amend_ST6_readerB.md` L480), both checked with `grep -nF`; the audit corpus excludes the dot-files. **No misquotation remains.** Before this final run, four inexact quotations were found and fixed in the piece: the first run (31 not found) flagged two (L170, a paraphrase of B inside quotation marks, unquoted; L545, a self-quotation of the merged Governance cell not in its exact form, set in italics); reading the piece's reader quotations by hand found a third (L189, a near-quote of C, cut to C's exact words); a read-only check of every double-quoted span against its cited sources, reader files included (script `amend_ST6_merge/qcheck.py`), found a fourth (L170, A's reading of the defining loss inside quotation marks, unquoted). The span check then reported: `quoted spans checked: 230; not found in the cited sources: 0`.

## Merge checks (script `amend_ST6_merge/checks.py`, run with `python3 -I` on the piece)
raw output (full):
```
== Amendment_Rederivation_ST6_Differentiation_2026-11-04.md 593 lines
lines with "keeper" (any case): 1
  L129: ...is outside the sanction check (`DR-80`); **(e)** "Keepers" is the pass author's coinag...
other-location name hits: 0 []
lines carrying both an old and a live figure: []
AS6-(\d+)      [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
RF-ST6-(\d+)   [1, 2, 3, 4, 5, 6, 7, 8, 9]
S6-RF-(\d+)    [1, 2, 3, 4, 5, 6, 7, 8, 9]
\bAR-(\d+)     [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 16, 19, 21, 22, 23, 24, 27, 28, 29, 39, 47, 63, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
\bAQ-(\d+)     [3, 42, 46, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101]
\bD6-(\d+)     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]
DEC-0(\d+)     [5, 8, 9, 10, 11, 12, 13, 16, 20, 40, 41, 42]
\bPR-(\d+)     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
\bH-(\d+)      [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
\bNS-(\d+)     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
```
Read: the one line with the coinage is the corrected premise (e), which states it is the pass author's coinage and not a name; no other location's name appears; no line carries both an old and a live figure. The ID lists hold the merged sets (AS6-1 to AS6-19; RF-ST6-1 to RF-ST6-9; AR-100 to AR-109; AQ-90 to AQ-101; D6-1 to D6-56; PR-12 to PR-15; H-8 to H-13; NS-12; DEC-040 to DEC-042) plus carried IDs of earlier pieces and readers' Round 1 IDs cited in mapping rows (AS6-20 is reader C's Round 1 ID in the mapping table; NS-13 is C's dropped row).

Same check on this record (other-location names and old/live mixing only; script `amend_ST6_merge/names_only.py`):
```
== Amendment_Rederivation_ST6_Differentiation_2026-11-04b_T8_Rounds.md (415 lines)
other-location name hits: 0 []
lines carrying both an old and a live figure: []
```

## American English sweep
raw output (full; script `amend_ST6_merge/ae_sweep.py` in the session scratchpad, run with `python3 -I` on both files; its positive control on a scratch text with ten planted British spellings and one kept spelling found all ten and the one; the kept-spelling count in this record comes only from the two output lines below):
```
== Amendment_Rederivation_ST6_Differentiation_2026-11-04.md (593 lines)
British-spelling hits: 0
'judgement' (kept spelling): 0
== Amendment_Rederivation_ST6_Differentiation_2026-11-04b_T8_Rounds.md (415 lines)
British-spelling hits: 0
'judgement' (kept spelling): 2
```

