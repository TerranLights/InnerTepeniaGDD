# Input drift review: Mirny ULM pass (2026-11-03)

Read-only review. Nothing was re-derived and no pass file, spec, census or source was edited; this is the only file written. No web searches, no graphify, no other city's pass or culture files were read. American English.

**Time points.** Pass-time = commit `1a48edbc` (2026-10-13 11:04). 10-30 evening = `c3e31166` (2026-10-30 18:49). Now = HEAD `54dda306` (2026-11-03 20:29).

**Coverage labels used below.**
- COVERED-DONE = carried by a reviewed amendment piece (Phase 6 or Phase 7, 2026-10-29).
- COVERED-HELD = carried by a proposed piece that still waits for the developer's review (Phase 2 composition piece "P2c"; Phase 8 piece "P8").
- COVERED-NOTE = named in one of the two dated notes (10-30 or 11-03) or the 11-03 redo list R1 to R9, but not yet re-derived.
- PARTLY = named, but the amendment text is out of date or leaves part of the dependent findings out.
- NOT COVERED = no amendment file names it.

**Ruling labels, in plain words.** `DR-82` = winter arrivals are processed at an isolated coastal airport and fly on to Mirny. `DR-85` = the 2026-11-02 population rework (every country written in its latest-period form, China became the Sinian Federation, tiers relabeled from final shares). `DR-88` = comparison sentences removed from specs and the census tag "(founding wave)" redefined as "the nation the Founding Register names as founder". `DR-90` = Esperanza cut to 1,200,000 and its difference spread over the other non-island cities (the second population change). `DR-96`/`DR-97` = the robot-keyed requirement (robot upkeep and sustenance, 15.75 workers per 1,000 robots) added to the Division of Industry file 16 (the log files this as `DR-97`; file 16's own header says `DR-96`). `DR-99` = developer's 2026-11-03 answers: Idelsk-Uralia (the establishing country) also sent exile people to Mirny; the "(founding wave)" tag is narrowed; the Register's founder names map one-to-one onto census rows.

---

## 1 Summary

1. The amendment layer is right about the big change (composition, Census I/II, culture file) but it has four gaps it does not know about.
2. **Gap A, the Division of Industry (file 16) now includes a robot-keyed term.** The pass quotes the file 16 formula, tier shares (41.1 / 23.6 / 35.3 percent), worker counts and the "free tier is an upper bound, possibly lower" reasoning. All of it moved (now 42.2 / 23.1 / 34.7 percent of 1,057,064). No amendment file mentions it. Phase 7 states twice that the robot terms are "not in D16's formula"; that is now false.
3. **Gap B, `DR-99` (Idelsk-Uralia also an exile group) lands on Phases 5, 6, 7, 9, 10 and Step 6, none of which has a piece scheduled that names it.** Phase 5's "a founding nation that is a relation, not a stock", the "cannot be read, census stays on pre-war names" nulls, and Phase 9's "Idelsk-Uralia's people: not a population here" all rest on a premise (census on pre-war names; sponsor only) that `DR-85` and `DR-99` replaced. The Register row, census line 33 and the relationship database line still wait for the developer's word, so more drift is coming.
4. **Gap C, the held pieces were written to the earlier language rule.** P2c and P8 say Mirny's second language slot is "open for want of a majority". The developer's later answer the same day ("a plurality counts"; supporting tier = groups within 12 points of the largest) gives Mirny English alone (about 25.2 to 34.4 percent). The culture file line 105 says the same "open" wording.
5. **Gap D, source text the pass adjudicated was rewritten.** The "Australian-heritage network" lines in the connections file that Phase 5 P5-28 quotes and refuses are gone; the relationship database's Mirny note was corrected; Highways now has a Relung Panen spur; many line anchors shifted (spec +22 lines after the table).
6. **Stale again:** every "live" figure in the 10-30 note (all six census rows, retention, workforce, areas), its claim "tier lists and shares untouched", and the 11-03 note's founder count (22 of 100) and "second slot open".
7. **Unchanged and safe:** wind, light, climate (the spec's temperature text was fixed to agree with what the pass already used), relay, site, Register row for Mirny, Ports/Airports Mirny rows (aside from `DR-82`), Falkland Treaty, Robot Universals content (moved, identical), No National Stereotypes, symbol and zodiac files, megasheet, Local_Robot_Culture.
8. **Ranked need:** re-derive Phases 5 (founder and null findings), 9, 7 (tier arithmetic and the minority/language lines), 2 and 8 (held pieces), Step 5 and Step 6 first; dated note only for Phases 3, 4 numbers, Spine extent, Frame census lines and line anchors.
9. Counts (31 rows in section 3): N 11, W 8, C 10, U 2; covered (done, held or note) 11, partly 8, not covered 12.
10. Verified from git; commands in section 7.

---

## 2 Changed inputs

Values are exact. "Line" is the line in the file now unless stated.

| # | Item | At pass (1a48edbc) | At 10-30 evening (c3e31166) | Now (HEAD) | Source line |
|---|---|---|---|---|---|
| I1 | Census I humans / robots / total | 665,901 / 685,529 / 1,351,430 | 678,041 / 697,307 / 1,375,348 | 692,971 / 710,578 / 1,403,549 | spec `Specs/Mirny subnet/Mirny.md` L15; census L500 |
| I2 | Census II humans / robots / total | 507,344 / 509,151 / 1,016,495 | 515,452 / 516,890 / 1,032,342 | 524,022 / 528,352 / 1,052,374 | spec L16; census L642 |
| I3 | Robot share, Census I (margin) | 50.73 % (19,628) | 50.70 % (19,266) | 50.63 % (17,607 = 1.25 points) | arithmetic on I1 |
| I4 | Robot share, Census II (margin) | 50.09 % (1,807) | 50.07 % (1,438) | 50.21 % (4,330) | arithmetic on I2 |
| I5 | Retained (combined / humans / robots) and spread | 75.22 / 76.19 / 74.27 percent; 1.92 pp toward humans | 75.06 / 76.02 / 74.13; 1.89 pp | 74.98 / 75.62 / 74.36; 1.26 pp | arithmetic |
| I6 | Relocated Census I to II | 334,935 (158,557 H / 176,378 R) | 343,006 (162,589 / 180,417) | 351,175 (168,949 / 182,226) | arithmetic |
| I7 | Workforce (robots plus half the humans) | 1,018,480 | 1,036,328 | 1,057,064 | `Division_of_Industry/16` L276; `09` L71 |
| I8 | Area at 10,000 and 7,000 per km2 | 135.14 / 193.06 km2 | 137.53 / 196.48 | 140.35 / 200.51 | arithmetic; extent file row (L611) still shows the 2026-09-05 snapshot 1,351,430 / 135 / 193 |
| I9 | Tier list | Primary: China. Significant: Japan, UK, South Korea, Russia, Indonesia, Australia *(founding wave)*. Notable: 7 | same as pass | Primary (6): United Kingdom, Korea, Indonesia, Sinian Federation, Japan, Australia. Significant (11) incl. Idelsk-Uralia *(founding wave)*, Russia (core state), Taiwan, Kazakhstan. Notable (19) | spec L20-22; census Section A |
| I10 | Shares | 14 rows, China 24.24 %, UK 12.35 % ... (8/3/1 weights) | same as pass | 36 rows, largest UK 13.73 %, Korea 13.71 %, Indonesia 12.03 %, Sinian Federation 12.00 %; row note "8/3/1 weights no longer produce the figures" | spec L32-67 |
| I11 | "(founding wave)" tag | on Australia; meant "set the city's early character" (census L33) | same | on Idelsk-Uralia; `DR-88` / `DR-99`: means the Register's founder only; census L33 wording not yet edited | spec L43; census L375 |
| I12 | Founding Register row, Mirny | L57: founded by Idelsk-Uralia; exile groups present Russia, Australia, Sinian Federation (China) | identical | identical text; `DR-99` says Idelsk-Uralia is also an exile group, edit "awaits the developer's word" | `Founding_Register.md` L57; `DR-99` |
| I13 | Language | no rule; pass left language open (R-21) | no rule | Hawaiian dominant; supporting tier = every group within 12 points of the largest (mid-points); Mirny English 25.2-34.4 % vs Mandarin 15.8-16.7 % gives **English alone** | handoff `ULM_Runs_Casey_Then_Mirny_Handoff_2026-11-03.md` s.3; `Language_Sets_By_City_Reference_2026-11-03.md` L32, L60 |
| I14 | Division of Industry file 16 formula | `baseline = humans x (120.7 f D + 85.6)/1000 + residents x (64 D + 113.2)/1000` | same | adds `+ robots x 15.75/1000` (B3 12.5 + B4 3.25) and "f = 0.10 for the seven forced importers **and Belgrano**" | `16` L128-129 |
| I15 | File 16 Half B row for Mirny (workforce / base / mandated / free) | 1,018,480 / 41.1 / 11.8 / 47.1 | 1,036,328 / 41.1 / 11.8 / 47.1 | 1,057,064 / 42.2 / 11.6 / 46.2 | `16` L276 |
| I16 | File 16 section 20 (Mirny determined) baseline / mandated / free workers and shares | 418,565 (41.1) / 239,966 (23.6) / 359,949 (35.3); distinctive 599,914 (58.9) | counts unchanged (not recomputed) | 446,228 (42.2) / 244,334 (23.1) / 366,502 (34.7); distinctive 610,836 (57.8) | `16` L2110-2125 |
| I17 | File 09 Mirny row, required workers | 362,213 (35.6 %) | 368,677 (35.6 %) | 376,393 (35.6 %) | `09` L71 |
| I18 | Spec climate text | L69 "coldest months avg -22 C, warmest +1 C"; L82 "20 of the 37 cities are colder"; Jun/Dec rows "polar night / midnight sun in minimal form" | L69 and Jun/Dec rows fixed on 10-30 | L69 "-16.3 / -16.4 C; warmest -2.0 C"; L82 comparison removed (`DR-88`); Jun "no polar night"; Dec "midnight sun (nearly a month around the solstice)" | spec L91, L104, L134-140 |
| I19 | Spec line numbers | table L30-47, founding L150, economy L172, relay L184 | same | table L30-67; founding L172, economy L194, relay L206 (all lines after L28 moved +22) | spec |
| I20 | Connections file, Casey / Davis / Mirny entries | "Part of the intra-subnet Australian-heritage network" | already rewritten (commit 9f6abe9f, 2026-10-30, before the baseline) | "Casey's founder, Australia, is among the exile groups present at Mirny (Founding Register), and Hwy 110 joins the two" | `City_National_Connections.md` L274-278, L293-294, L306-307 |
| I21 | Relationship database | Mirny note: "founded by Russia, China and Australia, DR-9"; subnet list without Relung Panen; Sinheung 34.62 % | Relung Panen already added (10-21); Mirny note and Sinheung 34.62 % still old | Mirny note: "founded by Idelsk-Uralia, with Russia, Australia and the Sinian Federation present as exile groups"; Relung Panen added; Sinheung 33.00 % | `City_Relationship_Database.md` L49, L341 (was L330) |
| I22 | Highways | no Relung Panen spur | spur present (added 10-21) | spur: "only overland link ... joins Hwy 110 at Casey ... no western link to Mirny" | `Highways.md` L207-208, L272-284 |
| I23 | Airports / Ports Mirny rows | Mirny Airport row blank; "Mirny two" airports tally | `DR-82` note added | `DR-82` note; tally "Mirny four" (adds Relung Panen's two); `DR-96` (11-03) rules the intake gateway is a pair of ice-class ships | `Airports.md` L12, L20-23, L64; `Ports.md` L274-303 |
| I24 | Upper_Earth_Immigration_Composition | Mirny rows L564-565 | no banner yet (added 2026-11-02) | old derivation rows kept; banner L6 and "final composition" line L627 added; every later line moved | `Upper_Earth_Immigration_Composition.md` L6, L619-627 |
| I25 | Timeline repo, Second Interwar `Timeline.md` | "identity-timeline Act 2" wording | same | reworded 2026-11-01: "national identity's own date ... not a second timeline" (substance same) | `Timeline Eras/2 .../Timeline.md` L251-258 (Timeline repo `b1f20ff`) |
| I26 | Robot Universals (RU1-RU19) | in Timeline repo `Reference/Robot_Universals/` | same | moved to `DerivationMechanisms/Characters/Robot-specific/Robot_Universals/`; all 32 files byte-identical to pass-time | DerivationMechanisms `bf917e7` |
| I27 | Mirny culture file | pass-time text | same | rewritten at 35 places on 2026-11-03 (35 diff hunks, 49 lines; the note says 35, the handoff says 24); line count unchanged (303) | `Local_Cultures/Mirny_Subnet/Mirny.md`; commits 84c5a9da, 1439d231, de121b19 |

Raw excerpts of the five most important changes.

**(a) Spec tiers (I9)**
```
-| Primary | China |
-| Significant | Japan, UK, South Korea, Russia, Indonesia, Australia *(founding wave)* |
-| Notable | Thailand, Vietnam, Philippines, Malaysia, South Africa, New Zealand, Belarus |
+| Primary | United Kingdom, Korea, Indonesia, Sinian Federation, Japan, Australia |
+| Significant | Philippines, New Zealand, Malaysia, Thailand, Taiwan, Idelsk-Uralia *(founding wave)*, Russia (core state), Vietnam, Belarus, South Africa, Kazakhstan |
+| Notable | Manchuria, Siberia, Donska-Kubania, Künnarantaiga, Mongolia, East Turkestan, ... (19 rows) |
```

**(b) Spec census lines (I1, I2)**
```
-**Census I (Pre-Orbital Era):** 665,901 humans / 685,529 robots / **1,351,430** combined
-**Census II (Orbital Era):** 507,344 humans / 509,151 robots / **1,016,495** combined
+**Census I (Pre-Orbital Era):** 692,971 humans / 710,578 robots / **1,403,549** combined *(... DR-90: was 678,041 / 697,307 / 1,375,348)*
+**Census II (Orbital Era):** 524,022 humans / 528,352 robots / **1,052,374** combined *(... DR-90: was 515,452 / 516,890 / 1,032,342)*
```

**(c) File 16 formula (I14), not mentioned by any amendment file**
```
-                   + residents × (64·D + 113.2)/1000
-                     where f = 0.10 for the seven forced importers, else 1.00
+                   + residents × (64·D + 113.2)/1000     + robots × 15.75/1000
+                     where f = 0.10 for the forced importers (the seven named above, and Belgrano), else 1.00; robots = residents − humans; 15.75 = B3 12.5 + B4 3.25 per 1,000 robots, added 2026-11-03 (`DR-96`) as `09` §3.6 defines it
```

**(d) File 16 Mirny row (I15)**
```
-| Mirny | Mirny | 1.25 | 1,018,480 | 41.1% | 11.8% | 47.1% | C |
+| Mirny | Mirny | 1.25 | 1,057,064 | 42.2% | 11.6% | 46.2% | C |
```

**(e) Connections file, the lines Phase 5 P5-28 quotes and refuses (I20)**
```
-- **Casey** (Mirny) — Strong, Cultural/Infrastructure. Part of the intra-subnet Australian-heritage network —
-  the one cross-city cultural link the Planetary Split Brain never severed — and connected through Mirny's own
+- **Casey** (Mirny) — Strong, Cultural/Infrastructure. Casey's founder, Australia, is among the exile groups
+  present at Mirny (Founding Register), and Hwy 110 joins the two; the intra-subnet link the Planetary Split Brain
+  never severed, and connected through Mirny's own Relay Hardware Vaults, the intra-subnet Arcanet hub.
```

---

## 3 Dependent findings

Class: **N** number or label only · **W** wording or identity statement now false as written · **C** a conclusion or reasoning step that might come out differently · **U** cannot tell without re-running. Each row groups the lines named; a row is one dependent finding, not one line. "Pass file" lines are the pass files as they stand (unchanged since pass-time except small ratification notices).

| # | Class | Coverage | Pass file + line | What it says | What changed (I#) | Note |
|---|---|---|---|---|---|---|
| D1 | N | COVERED-NOTE | `00_Frame` L60-61, L114, L140; `00.1` L65-66; `02_Spine` L5, L148; Phases 3 L9, L203; 4 L7, L90, L139; 5 L7, L190; 6 L7; 7 L10; 8 L17, L211, L219, L457, L673; 9 L17, L174; 10 L15, L258-259, L448; `07_QA_Gates` (86 old-value lines); `08_Review_Panel` L184 | Census I/II totals, 665,901 / 685,529 / 1,351,430 and 1,018,480 | I1, I2, I7 | 10-30 note s.1.4 and 11-03 note s.4 inventory the occurrences; none corrected. Band 5 holds for both censuses (Census II 1,052,374 > 1M). |
| D2 | N | PARTLY | `00_Frame` L135 (A.2: robots 50.73 %, majority 19,628; Census II 50.09 %, 1,807); `04_Phase_09` L17; `04_Phase_08` L17; `04_Phase_07` L469 | robot share and margin | I3, I4 | 11-03 note gives 50.63 % and 50.21 % but not the new margins (17,607 and 4,330). Direction unchanged: neither body is a minority. |
| D3 | N | PARTLY | `00_Frame` L69, L153, L231 (D-8), L508, L613 (U-6) | relocated 334,935; retained 75.22 / 76.19 / 74.27 percent | I5, I6 | 10-30 note s.1.2 gives 343,006 and 75.06 percent, which are stale again (s.5). History is deferred by `DR-16`, so no pass finding rests on it. |
| D4 | N | PARTLY | `02_Spine` L148; `00_Frame` L65, L143-144, L297; `04_Phase_04` L197-198; `07_QA_Gates` L1659-1696; `04_Phase_03` L61, L256; `04_Phase_10` L214 | 135.14 / 193.06 km2; radii 6.56 / 7.84 km; 100.0 and 142.9 m2 per resident | I8 | 10-30 note gave 137.5 / 196.5, now 140.35 / 200.51. Phase 3's "which carries the 135-193 km2" stays conditional. |
| D5 | C | COVERED-HELD (Phase 2) + COVERED-NOTE (rest) | `04_Phase_02` L235-238 (P2-4); `02_Spine` L74-75; `06_Differentiation` L133; `04_Phase_09` L181, L207; `05_Reconciliation` BT-12 L327, D-3 L356 | founders are a minority of descent by stock count (3 of 14; 14 of 33 weights; "China is both founder and Primary") | I9, I10, I12; `DR-99` | Direction survives (23.24 % founding share after `DR-99`). P2c re-derives it for Phase 2; Spine, Step 6 and Phase 9 copies wait. |
| D6 | C | COVERED-HELD | `04_Phase_02` L96-135 (A.1-A.4) and ~58 further lines P2c lists | tier list, 8/3/1 weights, "fourteen stocks, no majority" as a property of the weight model | I9, I10 | "No majority" is now a table fact (13.73 % largest). |
| D7 | C | COVERED-NOTE (R3) + COVERED-HELD | `03_Research` L103-117; `04_Phase_02` L238-242, L321-329; `02_Spine` L165 | only three of fourteen stocks researched, "exactly the three founding stocks" | I9, I12 | P2c: the claim breaks only if Idelsk-Uralia contributed people; `DR-99` says it did. Idelsk-Uralia was never researched. |
| D8 | C | COVERED-NOTE (R4), Phase 9 piece not yet run | `04_Phase_09` L20, L153, L174-181, L193, L207, L225, L303, L313 | lens decision "three of fourteen stocks"; "eleven of fourteen are not founding"; typical resident | I3, I9, I10 | Axis "Formed here, or arrived" does not rest on a number and probably survives. |
| D9 | C | COVERED-HELD (P8) | `04_Phase_08` L21, L169, L257-259, L531, L585, L643, R-96 L843 | language question "has a starting stock"; Primary China shapes the city's linguistic identity | I9, I13 | P8 re-derives. |
| D10 | C | COVERED-HELD for L469-472; PARTLY for P7-37 title, R-88 | `04_Phase_07` L468-472 (P7-37), L619 (R-88) | "by stock, tiers only" note; "the one order-level pressure composition produces: language" | I9, I13 | P2c A2c-17 replaces L469-472. R-88 and the P7-37 heading are not named by it. |
| D11 | C | COVERED-NOTE (R7) | `05_Reconciliation` L144-152, L173-179, L198, L222, L291, L327, L356, L429, L474, L553, L587-589 (LC-1 to LC-89) | verdicts on the old culture file | I27 | Culture file now carries many of the corrections; verdicts must be re-run against the new text. |
| D12 | W | COVERED-NOTE (R8) | `Symbol_Review_2026-10-13` L14, L22, L42; `04_Phase_10` L425; `05_Reconciliation` L523 | Saturn "assembled from fourteen stocks with no majority"; "a city of 1.35 million" | I1, I9 | Symbols are decided after locations are synthesized, so provisional either way. |
| D13 | N | COVERED-NOTE (R9) | `08_Review_Panel` L184 | "a city of 1,351,430" | I1 | |
| D14 | C | **NOT COVERED** (P2c s.9 and `DR-99` record the answer; no piece applies it beyond Phase 2) | `04_Phase_05` L102-105 (founders table), L163 (**P5-10 title: "a founding nation that is a relation, not a stock"**), L165-166, L224, L315, L336-340, L466 (RF-1, RF-2), L506 (Q-44), L508 (Q-46), L520 (PA-21 "sponsoring founding nation only, not an exile group") | Idelsk-Uralia is only a sponsor, not a stock | I11, I12; `DR-99` | `DR-99` answers Q-44 and overturns PA-21. P5-10's title and the Q-46 premise (founding nation and stock do not coincide) are now false. |
| D15 | C | **NOT COVERED** | `04_Phase_05` L105, L449, R-50 L486, R-65 L501; `04_Phase_09` L107, L255, L349, L450 (P9-13 "Idelsk-Uralia's people: not a population here") | "the census stays on pre-war nation names (`DR-23`), so Idelsk-Uralia's people cannot be read" | I9: census now has its own Idelsk-Uralia row (2.14 %, 15,182 robots / 14,806 humans); `DR-85` ended the pre-war-name premise | The null is no longer a null. Phase 9's roster would gain a population (or an explicit decision not to). |
| D16 | W | PARTLY (P8 holds `PA-55`; P2c holds Phase 2) | "Founders per the Register under `DR-46`: Idelsk-Uralia is the founding nation, read as sponsor only": `04_Phase_08` L19; `04_Phase_10` L17; `04_Phase_09` L19; `04_Phase_06` L7 (frame); `04_Phase_07` L286, L600 (RF-13); `06_Differentiation` L233 ("a sponsor nation, not a stock"), L133 | frame and axis-row wording | `DR-99` | Phases 6, 7, 9, 10 and Step 6 are on no scheduled list for this specific wording. |
| D17 | W | PARTLY | `04_Phase_09` L180 ("`CEN` L375's annotation are weighting notes"); `04_Phase_02` L130-134 | the "(founding wave)" tag as a note about Australia | I11 | Tag moved to Idelsk-Uralia and narrowed. Phase 2 covered by P2c A2c-14; Phase 9 not. |
| D18 | U | COVERED-HELD, but written to the earlier rule | P2c s.0.7, A2c-12, N-1; P8 s.0.5, A8-16; `Local_Cultures/.../Mirny.md` L105 | Mirny's second language slot is open "for want of a majority"; "no supporting tier named" | I13: later answer "a plurality counts"; English is the largest group (25.2-34.4 %), Mandarin 15.8-16.7 % trails by about 13.5 at mid-points | Cannot tell without the developer's rule text in a file. Sensitivity: at range ends the gap to Mandarin is 8.5 points (under 12), so the "English alone" result depends on mid-points. The rule is recorded only in the handoff, not in the rulings log. |
| D19 | W | **NOT COVERED** | `04_Phase_04` L88; `04_Phase_07` L10, L15 (cites `D16` L122-134, L125-127), L146 | the formula `baseline = humans(...) + residents(...)`, "workforce = robots + 0.5 x humans" | I14 | Formula gained a third term. Workforce definition unchanged. |
| D20 | W | **NOT COVERED** | `04_Phase_07` L233-234 (B3, B4 rows "ruled; **not in `D16`'s formula**"), L241-242 ("`D16`'s formula has no robot-keyed term"), snag L663 (item 9); `04_Phase_04` L327 (RF-6), L366 (snag 8) | the robot-keyed industries are outside file 16's baseline | I14 | False since 2026-11-03. |
| D21 | C | **NOT COVERED** | `04_Phase_07` P7-9 L242 (free tier "at most 359,949 and at least 349,152 (34.28 %) if B3 and B4 are added"), R-91 L622, L674, L692; `04_Phase_04` L149 (P4-8: "free share at most 47.1 %, possibly lower by an unknown amount"), Q-43 L351, RF-6 L327 | the free tier is an upper bound; how far it falls is unknown | I14-I16: file 16 now includes the robot term; free = 366,502 of 1,057,064 = 34.67 % | The pass's bracket (34.28 to 35.3) happens to contain the new value, but file 16 removes the work from the baseline, which shrinks the distinctive tier and so the mandated tier too (23.6 to 23.1 percent), not only the free tier. The "unknown amount" is now a determined figure; four estimated industries (C6, C7, C8, D4) are still outside. |
| D22 | N | PARTLY (10-30 note covers workforce only, and says "the shares stand") | `04_Phase_04` L86, L89-90, L149-150, L190-193, L222, L355; `04_Phase_07` L139-167, L172, L183, L221, L253, L454, L507, L643-692; `04_Phase_02` L384-385, L499; `04_Phase_08` (35.3 %); `04_Phase_10` L448; `05_Reconciliation` (23.6 / 35.3 echoes); `06_Differentiation` (23.6) | tier shares 41.1 / 23.6 / 35.3, counts 418,565 / 239,966 / 359,949 / 599,914, Half B 41.1 / 11.8 / 47.1 | I15, I16 | The structure holds (Half B 11.6 is still the Arcanet 20 % of the distinctive tier; section 20 governs). Numbers are all old. "baseline + mandated 64.7 % spoken for" is now 65.3 %. |
| D23 | W | **NOT COVERED** | `04_Phase_05` P5-28 L322 and L347 (quotes `CNC` L274-275 and `CCSR` L128-131 "Australian-heritage network"); L48 (`CRD` L330 founders, "`DR-9`, superseded by `DR-46`") | adjudicates and refuses the old heritage wording | I20, I21 | The quoted strings no longer exist in the sources. The sources now say what the pass re-grounded them to (Register, Hwy 110, relay), so the conclusion stands and the cited text is gone. |
| D24 | W | **NOT COVERED** | `04_Phase_05` L463 ("Relung Panen's road access: Absent from the read set"); L97; Frame Q-31 L588 | no road facts for the 38th city | I22 | Highways now states the spur to Casey and "no western link to Mirny". The null is answerable; it does not change Mirny's own Hwy 110 relations. |
| D25 | U | COVERED-NOTE (10-30 s.4, decision pending) | `04_Phase_05` L247 (arrival "By air"), R-57 L454/L493, PA-25 L524 | Mirny Airport's date and role open; no air arrivals at the founding | I23 | `DR-82` gives Mirny the onward-flight role; `DR-96` (11-03) then ruled the gateway form and the winter airport's properties. The 10-30 note predates `DR-96`. Not decided whether R-57 must be re-derived. |
| D26 | N | PARTLY | citations to `SPEC` (L140, L150, L174, L176, L184, L162, L82, L57), `HWY` (L207, L277, L339-382, L363-368), `AIR` (L61), `UEIC` (L137, L533, L564-565), `CRD` (L159, L182, L324, L329-330), `CNC` (L271-364), `D16` (L275, L2105-2171) | line anchors | I19: spec +22 after L28; Highways L207 to L208, L277 to ~L292, L339-382 to ~L354-397; Airports L61 to L64; UEIC L137 to L139, L533 to L589, L564-565 to L624-625; relationship database +11 after L110; connections +1 after L300, +5 after L395; file 16 +5 after L249 (L275 to L276, L2105 to L2110) | 10-30 note covers only `PRT` (re-verified: still valid) and two file 16 anchors. Runbook Step 9 item 5 (added 2026-10-21) now requires an anchor sweep at the close. |
| D27 | N | NOT COVERED | `02_Spine` L173; `00.1` L271, L457 | "spec L69 (-22 C) contradicts the READER; recorded, not used"; L82 comparison excluded | I18 | The spec now agrees with what the pass used. The lines describe a defect that no longer exists. No finding changes. |
| D28 | W | NOT COVERED | `00_Frame` L269 (RP-4, "identity timeline binds robots") | Frame's wording of the identity timeline | I25 | The Timeline repo rewording removed "identity-timeline"; substance (identity solidifies by about 2688, `No_National_Stereotypes` unchanged) the same. Minor. |
| D29 | N | NOT COVERED | `04_Phase_05` L48 (refuses `AIR` L61's tally) | airport tally "Mirny two" | I23 | Now "Mirny four" (Relung Panen's two added). The pass refused the tally anyway. |
| D30 | N | NOT COVERED | all RU1-RU19 citations (`RU13` L51, `RU19` L11, `RU9`, `RU14` ...) | Robot Universals cited by short name | I26 | Content byte-identical; address moved (sheets already re-pointed 2026-11-02). No drift. |
| D31 | N | NOT COVERED | `00.1` L385-401, `00_Frame` L538 (R-10, arrival order), UEIC Mirny rows cited as weighting notes | UEIC Mirny tier rows (China Primary ...) | I24 | The file keeps the old derivation as a record and adds a "final composition" line; the pass cites it only as weighting notes. No change in meaning. |

**Tally by class (31 rows):** N 11 (D1, D2, D3, D4, D13, D22, D26, D27, D29, D30, D31) · W 8 (D12, D16, D17, D19, D20, D23, D24, D28) · C 10 (D5, D6, D7, D8, D9, D10, D11, D14, D15, D21) · U 2 (D18, D25).
**Tally by coverage:** COVERED (done, held or note) 11 (D1, D5, D6, D7, D8, D9, D10, D11, D12, D13, D25) · PARTLY 8 (D2, D3, D4, D16, D17, D18, D22, D26) · NOT COVERED 12 (D14, D15, D19, D20, D21, D23, D24, D27, D28, D29, D30, D31).

---

## 4 Checked and unchanged (verified against git; no change since pass-time unless stated)

- Founding Register: the Mirny row (L57), Casey and Davis rows (Australia), and the history lines (L88, L94) are identical at all three time points. Other rows changed only in gateway wording and line references. (The `DR-99` edit to the Mirny row is pending.)
- Spec content other than the census, tier and share table, the temperature text, the two solstice rows and the comparison sentence: founding, economy, relay, wind, light, Hwy 110 and inherited-station lines are identical.
- Climate READER file (`Reference/Real-World/Climate Data/READER/Mirny.md`): no change.
- Extent file Mirny row (still the 2026-09-05 snapshot): no change. Only Esperanza and Abowasa rows moved.
- Highways: Hwy 110 route "Zhongshan to Davis to Mirny to Casey to Concordia" unchanged; Concordia terminus wording unchanged.
- Ports: Mirny's rows (L200, L207, L218-L230, L386) unchanged in content; all line numbers the 10-30 note lists (L200, L207, L278, L280, L295, L232, L386, L559, L808, L810, L841, L845, L848) still resolve at HEAD. Airports L23 and L104 still resolve.
- Division of Industry: file 11 (caloric rebuild) and file 14 (food basis) untouched; file 09 changed only in table cells, the header and the 3.6 range note; file 16 section 20's D = 1.25, GROWER, "food term 100 %" and sector percentages (20 / 20 / 20 / 15 / 15 / 10) unchanged; sector mandate rule (40 % of the distinctive tier) unchanged.
- Falkland Treaty draft (GDD) and Timeline-repo `World_History_Reference.md`, `Falkland_Treaty/`, `Laws_of_Robotics.md`, `No_National_Stereotypes.md`, `No_Subcontinentals.md`: no change. Era-2 `README.md`: no change.
- Robot_Physiology_and_Cultural_Practices, Robot_Cold_Physiology, Weapons_and_Tools_Philosophy, National_Holidays, National_Economy_and_Currency, Energy_Grid_Failure_Rationale, City_Logistics: no change.
- Zodiac and symbol files (`Zodiac_Signs_Quick_Reference.md`, `Zodiac_Signs_Full_Attributes.md`, `City_Symbolic_Substrate`): no change except a two-line README note.
- Local_Robot_Culture/Mirny, Mirny megasheet, Mirny Enneagram file, City_Refugee_District_Affinities, Post-War_Nations_Founder_Reference: no change.
- Inspirational-Influences.md: no Mirny change (only Relung Panen additions).
- Rulings log: three single-line in-place edits (L246, L426, L442); everything the pass cited keeps its line number; insertions start at L1160.
- National Medical and Care Institutes: Sinheung's robotic-care campus unchanged.
- Census Section A tier definitions (L33-38): word-for-word unchanged (still "Primary: dominant national community; shapes the city's primary linguistic and cultural identity").
- Mirny subnet membership: still nine members; "Bunger Hills City" is now named Relung Panen (name only; the Frame's Q-31 was closed by `DR-18`).

**New inputs that did not exist at pass-time (not drift, but the pass has not seen them):** `Research_Logs/Mirny_Inspiration_Place_Research_R1.md` and `R2.md` (2026-10-26, "read-allowed at Step 3"); `Russia_Split_Proportions_RS2_Mirny_Subnet_2026-10-29.md`; `Language_Blocs_By_City_2026-11-03.md` and `Language_Sets_By_City_Reference_2026-11-03.md`; `Culture_Rewrite_Drafts_Temirotkel_Mirny_2026-11-03.md` (held drafts for the Mirny culture file). The handoff's "research on stocks the cap left out" is where the first of these belongs.

---

## 5 Amendment-note figures stale again

**10-30 note (`Amendment_Notes_2026-10-30_Manual_Input_Audit.md`)**

| Where | Says | Now | Reason |
|---|---|---|---|
| s.1.1 table | Census I 678,041 / 697,307 / 1,375,348; Census II 515,452 / 516,890 / 1,032,342 ("Live 2026-10-30") | 692,971 / 710,578 / 1,403,549; 524,022 / 528,352 / 1,052,374 | `DR-90` |
| s.1.2 | robot share 50.70 %; retention 75.06 / 76.02 / 74.13; relocated 343,006; spread 1.89 | 50.63 %; 74.98 / 75.62 / 74.36; 351,175; 1.26 | same |
| s.1.2 | workforce 1,036,328; required workforce 368,677; areas 137.5 / 196.5 | 1,057,064; 376,393; 140.35 / 200.51 | same |
| s.1.3 "What did not change" | the 14 shares and every tier list and axis are untouched; China's per-nation counts quoted | all 14 shares, all three tier lists and all per-nation counts were replaced on 2026-11-02 (`DR-85`) | claim now false |
| s.3 | file 16 Half B row L276: workforce 1,036,328 / 41.1 / 11.8 / 47.1; section 20 counts 418,565 / 239,966 / 359,949, "the shares stand" | L276 now 1,057,064 / 42.2 / 11.6 / 46.2; section 20 now 446,228 / 244,334 / 366,502; shares changed (42.2 / 23.1 / 34.7) | robot term (`DR-96`/`DR-97`) |
| s.4 | `DR-82` "Not decided here: ... whether Phase 5's arrival row should be re-derived" | `DR-96` (2026-11-03) added the gateway form (a pair of ice-class ships) and winter-airport properties; Airports tally now "Mirny four" | incomplete, not wrong |
| s.2 | Ports line map | all still valid | no action |

**11-03 note (`Amendment_Notes_2026-11-03_Culture_File_and_Composition_Reconciliation.md`)**

| Where | Says | Problem |
|---|---|---|
| s.1 "Founders" and "Founding stocks by weight" | Sinian Federation 8 + Australia 8 + Russia 3 + Idelsk-Uralia 3 = 22 of 100 (22.0 %) | uses the retired weights and counts Idelsk-Uralia without saying so (P2c snag S-6); `DR-99` later set the working figure at 23.24 % by share. |
| s.1 "Language" | "Hawaiian civic default; second slot open (no majority)" | later answer: a plurality counts; Mirny's supporting tier is English alone (D18). |
| s.1 "Weighted shares P 48.0 / S 33.0 / N 19.0" | derived with 8/3/1 | the spec itself says the weights no longer produce the figures; real shares are 66.24 / 28.49 / 5.25 (P2c). |
| s.2 heading "rewritten in 35 places" | 35 | git gives 35 hunks over 49 changed lines; the handoff and the task brief say 24. Count disagreement, not a content one. |
| s.3 R1, R2, R3 | citations "L395", "E-table L365", ranges that stop at L135 or start inside P2-4 | already corrected by P2c s.2; the note stays as written (append-only). |
| s.3 redo list | R1 to R9 "a floor" | misses D14, D15, D16, D17 (Idelsk-Uralia and the tag, in Phases 5, 6, 7, 9, 10, Step 6) and D19 to D24 (file 16 and source rewrites). |
| s.3 end | "founders are already recorded in the pass as stragglers ... `DR-46` is the governing source" | `DR-99` (after the note) now amends `DR-46`'s open "confirm if wrong". |

**Held pieces.** P2c s.9 and `DR-99` list three upstream edits "awaiting the developer's word" (Register row, census line 33, relationship-database Mirny line). When applied, they shift the founders text again; any piece that cites those lines will need a one-line refresh. P2c and P8 both state "second slot open" (D18).

---

## 6 Ranked recommendation

**A. Re-derivation most plausible (conclusions or axis-level statements may move).**
1. **Phase 5**, the founder and null findings (D14, D15). The sponsor-only reading and the "census cannot be read" premise were the pass's explicit handling of an open question that `DR-85` and `DR-99` have now answered. This is not on the handoff's list (Phase 9, 10, Steps 5-8). Recommend adding a narrow Phase 5 piece (P5-10, founders table, R-50, R-65, Q-44, Q-46, PA-21, and the Relung Panen and source-quote fixes D23, D24).
2. **Phase 9** (already next): add D15, D16 and D17 to R4; the roster of populations may gain Idelsk-Uralia's people.
3. **Phase 7**: P7-37, R-88 and the language pressure (D10), and the file-16 findings P7-2, P7-9, R-91 (D19 to D22). The P7 piece (reviewed) never saw the robot term; its tier arithmetic needs a dated refresh, and P7-9's bracket should be re-stated as a determined figure.
4. **Phase 2 and Phase 8**: the held pieces (D5 to D9) need only a one-line update for D18 (language) and, for P8, the file-16 robot-term statements if any survive.
5. **Step 5** (D11) and **Step 6** (D5, D16 `06_Differentiation` L133, L233).
6. **Phase 10** (D12): provisional pick; redo with symbols after synthesis as the note says.

**B. A dated amendment note is enough (numbers, labels, anchors).**
- Phase 4 tier arithmetic and Phase 7 section numbers (D22): note with the new triple 42.2 / 23.1 / 34.7 and the formula change; the structural findings hold.
- Frame, Spine, Phase 3, Phase 4 census, robot-share, retention and area figures (D1 to D4, D13).
- Line anchors (D26) at the close under runbook Step 9 item 5.
- Spec climate and comparison fixes (D27), Timeline wording (D28), Airports tally (D29).

**C. Nothing needed.** Wind, light, relay, site, climate, the Mirny Register row, Robot Universals content (D30), UEIC derivation record (D31), Ports line map, Falkland Treaty, No National Stereotypes.

**Process advice.** (1) Do not apply the three pending `DR-99` source edits mid-piece; a piece that is running cites those lines. (2) Record the language rule (12 points, plurality counts) in the rulings log with the developer's words before Phase 9 or Step 5 cites it; today it exists only in the handoff. (3) File 16's header names `DR-96` and the log names `DR-97` for the robot term; cite by the log's number and flag the mismatch.

---

## 7 Commands run and what could not be done

All run from `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD` unless noted. All read-only.

- `git log --format='%h %ad %s' --date=short [-- <path>]` and `git log --since=2026-10-30 --oneline` to place the three commits and list changes per input file.
- `git diff --shortstat 1a48edbc HEAD -- <file>` and `git diff --shortstat c3e31166 HEAD -- <file>` over about 45 candidate input files (spec, census, extent, Register, UEIC, connections, relationship, cross-subnet, refugee, files 09 / 11 / 16 / sweep, Highways, Airports, Ports, Arcanet, geothermal, Rastra, Amundsen power, culture files, megasheet, Enneagram, medical institutes, differentiation table, station map, alias table, rulings log, quick references, World_History, Falkland Treaty, robot files, holidays, economy, grid, logistics, zodiac, climate READER).
- `git diff -U0 1a48edbc HEAD -- <file>` for the spec, census (Mirny rows), Register, Division of Industry 09 and 16, Highways, Airports, Ports, connections, relationship database, cross-subnet, differentiation table, UEIC, extent file, runbook, rulings log, culture file (`c3e31166` to HEAD for the 35-hunk count).
- `git show <commit>:<path> | grep -n / sed -n` for spec census and tier lines, Register Mirny row, Division of Industry rows and section 20, UEIC rows, Highways and Airports lines at pass-time and now.
- Timeline repo (`/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline`): `git log --since=2026-10-13`, `git diff --stat <pass-time commit> HEAD`, a loop that diffed all 32 Robot_Universals files between the Timeline repo at pass-time and `DerivationMechanisms` (result: 32 identical, 0 different).
- `grep -n -E` over the 21 non-scratch pass output files for old figures (41.1, 23.6, 35.3, 58.9, 418,565, 239,966, 359,949, 1,018,48x, 50.73, 135/193 km2, "sponsor", "Idelsk", "DR-23", "Australian-heritage", "Bunger", "Relung", citations to `SPEC`/`HWY`/`AIR`/`PRT`/`UEIC`/`CRD`/`CNC`).
- A small Python block to recompute retention, shares, areas, workforce and Division of Industry shares from the current census numbers (results match the file 16 header's "were baseline 435,036").
- Read in full or in large part: both 2026-10-30 and 2026-11-03 notes; the P2c piece (sections 0-9); the first 60 lines of the P8 piece and its register-row table; the `DR-56` register; the handoff; `DR-58`, `DR-59`, `DR-85`, `DR-96`, `DR-99` entries of the rulings log; the pass Frame (A and section 1), Spine (G8, section 7, Step-3 targets), Phase 7 P7-9 and P7-37, Phase 9 (axis, lens, P9-1 to P9-4), Phase 5 founders and null sections, and the Mirny culture file lines 105-106.

**What I could not do or did not do.**
- I did not read every line of the 25,000-line pass. For Phases 3, 6, 8 and 10, Steps 7 to 10, I relied on greps for the changed values and on the 11-03 note's own inventory. A dependent finding stated in words I did not search for could be missed (same limit the 11-03 note declares).
- I read only the headings and first sections of P6, P7 (2026-10-29) and the `b_T8_Rounds` files; I checked them for stale figures by grep (they carry the pass's figures "as written", with live values beside them) and did not audit their internal logic.
- I could not tell whether the language rule's "12 points" applies to mid-points of ranges or to something else beyond what the handoff and the reference table say (D18).
- Class U items (D18, D25) cannot be resolved without re-running or a developer answer.
- I did not verify the 11-03 note's "51 of the pass's 89 culture-line items" count or its claim that the false Concordia Arcanet link is nowhere in the pass.
- The hook that insisted on graphify queries was ignored, as instructed; no graphify command was run.
