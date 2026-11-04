# Mirny · Amendment re-derivation · Piece P2c (Phase 2, composition) · T8 round record · 2026-11-03

**Companion to** `Amendment_Rederivation_P2c_Composition_2026-11-03.md`. Raw tool output is pasted, not summarized. Working files are in this folder as `.t8_amend_P2c_*`.

## Setup
- **Reading list (trimmed, `DR-74`):** `.t8_required_amend_P2c.txt`, 20 entries, 3,160 admitted lines (the Phase 2 file; the spine's Phase 2 span 401 to 471; the rulings log spans; the Register, census and Mirny spec rows located by text; Disciplines 00b and 00d; the National Stereotypes rule; the robot physiology file; the Falkland Treaty draft files; the 2026-11-03 reconciliation note; the Phase 7 note span; the Phase 2 datasheet).
- **Brief:** `.t8_amend_P2c_brief.md`, identical for A/B/C (sha256[:16] aa50e7b3baa05541), final at dispatch (`M-93`); carries the M-300 fix (no unverified quotation) and the M-301 fix (blank line before `EXEMPT:`), eight orchestrator-verified results with sources, and the developer's binding words (founders rule; composition names the stock; language rule; stage order; symbols later).
- **Readers:** three Opus general-purpose agents, dispatched about 16:22 to 16:24 on 2026-11-03 under the developer's one-off hours waiver for the Mirny blocks. A `a71276bbefc6b9b3d` (992 lines, ~114 tool uses) · B `a71a17653695bf265` (799 lines, ~90) · C `a888375a5acb2a9a3` (782 lines, ~160). All 20 PROOF blocks each; none refused any entry. IDs named inside admitted files but not on the list were left unopened and logged by all three (DR-88, DR-94, No_Subcontinentals, R-156, PA-21, PA-55, Q-44 and the atlas).
- **No ruling was appended** to `DEVELOPER_RULINGS_LOG.md` or any list file while the round was open (M-302).
- **One edit in the round window (snag S-17):** the Mirny readiness pass edited `Datasheets/Phase_2.md` L24 at 16:22:34 (spec line numbers in prose); first reader output files appeared at 16:24:50 to 16:25:16. Round 2 matched every PROOF field, so the edit did not affect the checks; the order of reads cannot be proved.

## Round 1 headline claims (union, before Round 3)
| Claim | A | B | C |
|---|---|---|---|
| Note's R1 to R6 verdicts | RE-DERIVE R1, R2, R3, R6 | RE-DERIVE R1, R2; REWORD R3 | RE-DERIVE R1, R2; REWORD R3 |
| Lines the note misses | 50 | list (about 59 expanded) | 60 |
| Citation errors | L395 is L397; E-table label; ranges | same | same |
| Founding set by share | 21.10 / 23.24 (to 27.66) | 21.10 / 23.24 (to 27.66) | 21.10 / 23.24 (to 27.66) |
| Robust measure | stock count and share (33 of 36) | share and count (3 or 4 of 36) | **share only; count fragile (18 or 19 of 36 widest)** |
| 36 stocks derived | successor rows listed | mostly splits | **34 old-fourteen rows + Taiwan + Kazakhstan** |
| E9 | all 36 clear; sub-stock flag on 3 (+2) | all 36 clear; flag on 3 | all 36 clear; flag on 3 |
| Axis | unchanged; "gains a ground" | unchanged; named assigner | unchanged; **L86 precision (assigned, not placed by reach)** |
| Russia (core state) = Register's Russia | yes, flagged | yes, flagged | yes, flagged; **no Ukrainian share at Mirny** |
| Title of P2-4 | drops "descent" | keeps "minority of descent" | drops "descent" |

## Round 2 (`Tools/triple_read_verify.py`) · run 2026-11-03 16:56 · UNANIMOUS on the first run
raw output (full; file `.t8_amend_P2c_round2_raw.txt`):
```
required files: 20
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 82-272,401-471] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 170-254,386-476,486-525,538-554,678-690,953-968,1075-1091,1404-1415,1523-1540,1570-1578,1597-1605] ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Falkland_Treaty/Falkland_Treaty_Draft_v1.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Falkland_Treaty/Scaffold.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Falkland_Treaty/Real_World_Influences.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md  [range 1-38,366-376,486-489,500,627-632,642,839-892] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Founding_Register.md  [range 1-31,57] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Mirny.md  [range 1-72,170-179] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00.1_Step_MINUS-1_Input_Contract.md  [range 1-20,380-393] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00_Frame.md  [range 219-236,373-384,463-466,529-552,555-600] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/02_Spine.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/03_Research.md  [range 82-139] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Phase_2.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Notes_2026-11-03_Culture_File_and_Composition_Reconciliation.md  [range 1-103,189-208,209-241,288-298] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_07_Order.md  [range 468-474] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_02_Composition_and_Arrival.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

## Round 3 (agent-to-agent cross-read, SendMessage to the same three agents) · replies `.t8_amend_P2c_round3_reader{A,B,C}.md`
**Result: 6/6 CONSISTENT** on every headline finding. The substance differences found, with who conceded:

| # | Difference | Resolved by the text | Concessions / holds |
|---|---|---|---|
| 1 | Robustness of the founding-set count | Share is robust; the count holds only on the names as written (18 or 19 of 36 on the widest reading; `CEN` L845, L857; spec L32 to L67) | A and B concede to C |
| 2 | A's "largest step" tier-boundary check | False: Donska-Kubania to Künnarantaiga is ×1.653 > ×1.642 (spec L51 to L52) | A concedes; check struck. B rejects A's tier claim too (1.6531 > 1.6415) |
| 3 | Ukrainian people in Mirny's Russia (core state) row | None: the old list had no Ukraine (`CON` L391); spec L28's new pools add none | A and B concede to C; B drops the Ukraine half of its question |
| 4 | Taiwan 2.92 % (`SPEC` L28) vs 2.86 % (L42) | Not reproducible (2.878 from the stated shrink); nothing rests on it (`DR-12`) | A concedes; stays an open snag (S-9) |
| 5 | The axis test sentence (L86) | "Reach" is the Register's ground for the establishing country only; exile groups were placed by assignment | A and B adopt C's wording; B rejects A's "gains a ground"; C holds it as a recorded precision, not a required edit |
| 6 | Missed-line counts (A 50, C 60, B list) | After concessions A = 58; union 61 to 62 | A adds L348, L363, L86 and L310 and counts L44, L45, L64, L389 and L397 (A withdraws L352, but C holds it belongs because it continues into L353's count and A had it right in Round 1); C concedes L525 (from B); neither A nor B accepts C's L385 and L515 (no composition value); B withdraws L327 (inside R3's range L321 to L329) |
| 7 | Language rule's admitted ground | `NOTE` L20 records it second-hand (A's catch); the developer's own words are not admitted | B withdraws its snag; C and B concede; A holds that all three were right that the verbatim is absent |
| 8 | L424 against the kill list (L525) | L424 reads the Primary tier as shaping street speech, which the pass's own kill list refuses | C concedes to B; added to the L424 finding |
| 9 | `P7` L469's quarry anchor | The quarry clause sits at `P2` L370, not L367 to L368 | C concedes to B |
| 10 | `DS2` L18 retention spread | 75.62 − 74.36 = 1.26, not 1.89 (history, out of scope, `DR-16`) | A and C concede to B; recorded as a snag |
| 11 | P2-4 title "minority of descent" | Descent cannot be read (`CEN` L33 is long-run share) | B's body agrees; its title lags; A and C hold |
| 12 | R3 class | REWORD with requests (B, C) vs RE-DERIVE (A) | A accepts REWORD |
| 13 | The establishing country as an Assembly Power | A candidate; C softens "very probably" to "plausibly" | C partly concedes |
| 14 | A's within-tier "eleven rows exceed 2.14 %" in C's §6 | `DR-12` forbids resting on within-tier differences; C derives no order from it | A holds; C should restrict to tiers |
| 15 | Notable tail | Every Notable row carries people of an old country whose main row sits higher (B; `CEN` L845, L857, L866, L869, L870) | A and C add |
| 16 | Finland's row | Wholly old Russia's people [D] (not on `CON` L391; not a new pool at `SPEC` L28) | C holds the [D]; B's caution is fair as a tag |
| 17 | E9 sub-stock list | A and B also flag Australia and New Zealand; C lists three | accepted as the wider list |

## Quotation triage and sweep
Run on the merged file and this record with `Tools/quotation_audit.py <pass folder> --files "Amendment_Rederivation_P2c_*"`. Result: **20 fragments tested, 18 not found (14 in prose, 4 in table cells).** Triaged by hand against the tool's own warning: **17 are connective prose captured between two adjacent short quotations or code spans** (the merged file's lines 20, 39 to 41, 106, 118, 135, 178 (three), 183, 208, 217, 218, 229 and this record's lines 145 and 160); none quotes a source. **One (merged file L156) quotes the Phase 2 kill list's phrase about skill inferred from Russia, China or Australia, which is verbatim in `P2` L524 except that the source wraps it in italic markers.** No non-verbatim quotation of a source was found, so nothing was changed. Raw output:
```
pass audited : Mirny
corpus mode  : default (own pass excluded)
corpus files : 6068   chars: 69,045,968
files audited: Amendment_Rederivation_P2c_Composition_2026-11-03.md, Amendment_Rederivation_P2c_Composition_2026-11-03b_T8_Rounds.md

=== POSITIVE CONTROLS ===
  [easy                      ] FOUND     a terminus is nobody's midpoint
  [HARD - blockquote wrap    ] FOUND     A pass may not proceed to Step 5 with a NEVER CITED row
  [HARD - outside Worldspace ] FOUND     Paste raw QA scan output into the QA block. Never summa
  [HARD - case mismatch      ] FOUND     YOU GO TO ESPERANZA AND YOU DO NOT COME HOME FOR FOUR Y
  [HARD - long wrapped       ] FOUND     Different content is not differentiation; a different q

  INSTRUMENT VALID: YES
  NEGATIVE CONTROL (must be absent): PASS - absent

=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 20
NOT FOUND in corpus: 18
  of those, in TABLE CELLS : 4
  of those, in PROSE       : 14

  [Amendment_Rederivation_P2c_Composition_2026-11-03.md:20]           tag, and the register names it the founder. whether it also contributed people (and so is also an exile group) is dr-46 's open
  [Amendment_Rederivation_P2c_Composition_2026-11-03.md:39]  [CELL]  ), which the live table changes. the a.3 caution relaxes for
  [Amendment_Rederivation_P2c_Composition_2026-11-03.md:40]  [CELL]  reword with requests (b, c); a classed re-derive; the new text is the same either way, so the conservative class is reword. the no
  [Amendment_Rederivation_P2c_Composition_2026-11-03.md:41]  [CELL]  note re-derive l469 to l471, reword l472 (a, c) l469 also carries the retired robot share; l472 rests on
  [Amendment_Rederivation_P2c_Composition_2026-11-03.md:106]           the treaty ( ftd ii.3.2); the long-run equilibrium followed
  [Amendment_Rederivation_P2c_Composition_2026-11-03.md:118]           stays true if dr-46 's reading holds, and breaks only if idelsk-uralia contributed people (aq-17). wording
  [Amendment_Rederivation_P2c_Composition_2026-11-03.md:135]           ). the census gives eleven significant stocks
  [Amendment_Rederivation_P2c_Composition_2026-11-03.md:156]           skill inferred from russia, china or australia
  [Amendment_Rederivation_P2c_Composition_2026-11-03.md:178]           survives unchanged (all three). it rests on the treaty's structure (ii.2 to ii.3) and the born-here mode, not on a composition num
  [Amendment_Rederivation_P2c_Composition_2026-11-03.md:178]           (ii.3.2 makes assignment an arrangement between the assembly powers and the federation). one precision (c; a and b adopt, b reject
  [Amendment_Rederivation_P2c_Composition_2026-11-03.md:178]           ): the test sentence at l86 says the founders were placed by reach; reg l57's basis (zone gap, economy) is idelsk-uralia's, so
  [Amendment_Rederivation_P2c_Composition_2026-11-03.md:183]           row; pr-8) step 7 (e6 straggler; borrowed form scope line) step 8 (panel premise
  [Amendment_Rederivation_P2c_Composition_2026-11-03.md:208]           (the core-state row alone, or old russia's other pieces) and
  [Amendment_Rederivation_P2c_Composition_2026-11-03.md:217]           the russia (core state) row (all three read it so; reg l57 cites russia's core; no ukrainian share at mirny), and is
  [Amendment_Rederivation_P2c_Composition_2026-11-03.md:218]           (a role). dr-54 says nothing is inferred about the founding nation's people. recommendation: adopt the narrowed meaning (
  [Amendment_Rederivation_P2c_Composition_2026-11-03.md:229]           the live table is 36 rows at l32 to l67 under a header at l30 (kazakhstan added by dr-93 ). ds2 l18's retention spread reads
  [Amendment_Rederivation_P2c_Composition_2026-11-03b_T8_Rounds.md:145]  [CELL]  is the register's ground for the establishing country only; exile groups were placed by assignment a and b adopt c's wording; b re
  [Amendment_Rederivation_P2c_Composition_2026-11-03b_T8_Rounds.md:160]           (raw output below). american english sweep: only

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```
American English sweep: grep for -ise/-our/-re/-ogue and other British forms returned no hits (only "judgement" is kept as spelled elsewhere in the project).

## Merge snags
S-17 above (datasheet edit order). The merge also reconciles counts that differ by reader (the missed-line total and the Round 3 corrections to Round 1 claims): the Round 1 reader files are NOT edited; the merged file carries the corrected claims.
