# Davis ULM pass: input drift review (2026-11-03)

**What this is.** A read-only check of whether any input the finished Davis pass (run 2026-09-14 to 2026-09-16, completed in commit `d2dd2136`, last Record edit `4a59fab8` on 2026-10-01) absorbed has changed since, so that the pass results might come out differently if re-derived. **Nothing was re-derived. No pass file, spec, census or source was edited.** This file is the only thing written. No web searches. No other city's pass or culture files were read, and no Davis-to-other-city comparison is made (a city is named only where a source says it about Davis, as a relation).

**Three points in time used.** Pass = commit `d2dd2136` (2026-09-16). 10-30 = commit `c3e31166` (2026-10-30 evening, the baseline of the manual input audit and of `Amendment_Notes_2026-10-30_Manual_Input_Audit.md`). Now = `HEAD` (`54dda306`, 2026-11-03).

**Rulings cited, in plain words.** `DR-4`: Census I (the larger, pre-orbital count) governs the city's size and band. `DR-7`: pre-war records at a site are admissible. `DR-19`: a city's founders stand on geography and access, never on the real station that stood there. `DR-24/25/26`: a station's infrastructure, records, research, equipment and techniques may be inherited; its operator and its traditions may not. `DR-68`: the Santa Luce population scenario (2026-10-28) raised every city's totals. `DR-85`: the 2026-11-02 population rework (every country in its latest-period form, split by headcount, Sinian Federation share reduced, tiers relabeled). `DR-88`: comparison sentences in specs neutralized, and the "(founding wave)" tag means "named as a founder in the Founding Register" (2026-11-02). `DR-90`: Esperanza cut to 1,200,000 and the difference spread over 26 other cities (2026-11-02). `DR-93`: Kazakhstan added to the nation pool. `DR-94`: Manchuria's share reduced like the Sinian Federation's. `DR-97`: the robot-keyed term (robot maintenance 12.5 and robot sustenance 3.25 workers per 1,000 robots) added to the Division of Industry three-tier model in file 16 (2026-11-03; the file's own text calls it `DR-96`). `DR-99`: the tag "(founding wave)" is narrowed to mean the establishing country named in the Register, "not people who arrived in a wave" (2026-11-03).

---

## 1. Summary

1. The pass's inputs have drifted in two waves. Between the pass and 10-30 the census totals rose (`DR-68`) and the Register, symbol and relationship files were re-grounded; the 10-30 note recorded that. Between 10-30 and now the **composition of the city was rebuilt**: 21 origins (China the only Primary, 19.04%) became **45 rows** (Primary: Japan 10.42%, Sinian Federation 9.72%, United Kingdom 9.36%, Germany 8.54%, Korea 8.35%; Significant: Indonesia and Australia, each 5.74%; 38 Notable, 21 of them under 1%). The totals moved again (`DR-90`: 1,210,432 and 817,475). File 16 was recounted with a new robot term.
2. The 10-30 note's "live" figures are stale again, and its statement that "none of the shares changed" is no longer true (section 5).
3. **Numbers only (N): 11 items.** The retention and robot-share findings keep their direction (humans still retain more than robots; the city still goes from robot-majority, now 51.20%, to human-majority), but the retention spread fell from 19.74 to 18.25 points, more than the 10-30 note's estimate, because the Esperanza share was added to Census I and Census II unequally.
4. **Wording false as written (W): 7 items.** Chiefly "21 origins", "the only Primary is China", "plurality-Chinese", "largest at 19.04%, one person in five", "the tiers are a production weight", and mixed old/new spec line numbers across the pass files.
5. **Conclusions that might re-derive differently (C): 7 items.** The most consequential: Phase 2's headline H-2 and its flagged layer call H6 (what "(founding wave)" means); Phase 2's scale check that killed the small-origin finding ("not one of the 21 lacks numbers", now false for the smallest rows, 152 people at Tuva); Phase 2's "origins are where robots were" argument; the seal on comparing nations' figures (its stated ground was the old de-stacking randomization); Phase 5's "heritage relations structurally excluded, no independent route" (the national-connection entries now rest on the Register and Hwy 110); and Phase 8/9's "what any community speaks is not written" (a language rule now exists).
6. **Cannot tell without re-running (U): 5 items** (export headcount hole, what the law now lets cross the founding gap, a character draft sited in Davis, the Step -1 contract's composition ranges, stale culture files at Step 5).
7. Not drift but found along the way: the 10-30 note's "Phase 5's air claim is wrong because the source changed" is mis-framed: `Airports.md` already listed Davis among the no-air-access cities at pass time; the pass misread it.
8. Unchanged and safe: climate and extent, the Ports row for Davis, Highways, Arcanet, symbol assignment (still blank), the designated inspiration places, the medical-institutes line about Davis, the Davis culture robot file, the era timeline (still no Davis hits), the Falkland Treaty folder.
9. Ranking (section 6): re-derive Phase 2 first, then Phase 5's relations, Phase 8 section E and Phase 9 language lines, and the Spine's G8 entry; dated amendment note for the numbers in Phases 4, 7, 8, 9, 10 and Steps 0/1/2/7/8; nothing needed for Phases 3 and 6 or Step 5's findings.

---

## 2. Changed inputs

Line numbers are as of the named point in time unless stated. "Pass" = `d2dd2136`.

| # | Item | At pass | At 10-30 (`c3e31166`) | Now (`HEAD`) | Source and line |
|--:|---|---|---|---|---|
| 1 | Census I, Davis (humans / robots / total) | 563,599 / 594,715 / **1,158,314** | 575,738 / 606,493 / **1,182,231** (`DR-68`: +12,139 H, +11,778 R) | 590,668 / 619,764 / **1,210,432** (`DR-90`: +14,930 H, +13,271 R) | `Official_Population_Census.md` row 13: L496 / L494 / **L506**; spec `Specs/Mirny subnet/Davis.md` L15 |
| 2 | Census II, Davis | 437,423 / 344,173 / **781,596** | 445,531 / 351,912 / **797,443** (+8,108 H, +7,739 R) | 454,101 / 363,374 / **817,475** (`DR-90`: +8,570 H, +11,462 R) | Census row 14: L613 / L617 / **L650**; spec L16 |
| 3 | Band | Census I 1,158,314 = Band 5; Census II = Band 4 | same | 1,210,432 = Band 5; 817,475 is still under 1,000,000 (Band 4 straddle holds) | `00_Frame.md` L65 |
| 4 | Number of origin rows and tiers in the spec / census Section A | 21 rows: Primary 1 (China), Significant 7 (Japan, Germany, UK, South Korea, Russia, Indonesia, Australia "(founding wave)"), Notable 13 | same as pass (shares rescaled, not changed) | **45 rows**: Primary 5 (Japan, Sinian Federation, United Kingdom, Germany, Korea), Significant 2 (Indonesia, Australia "(founding wave)"), Notable **38** | spec tier lines L18-22 and per-nation table (pass L30-52; now L30-76); census Section A Davis entry L392-396 |
| 5 | Largest origin and its share | China **19.04%** (113,234 R + 107,309 H = 220,543 at Census I) | China 19.04% | **Japan 10.42%** (126,123 at Census I); Sinian Federation (China's row) 9.72% (117,596), second | spec per-nation table, rows 1-2 |
| 6 | Australia, the "(founding wave)" origin | 4.93% (about 57,105 at Census I), listed as 7th of 21 | 4.93% | **5.74%** (69,475 at Census I), tied with Indonesia at 5.74% | spec per-nation table |
| 7 | Small rows | smallest row 0.94% (Latvia) | same | 21 rows under 1%, 17 under 0.5%, **10 under 0.1%**; smallest Tuva 0.013% (152 people at Census I), Karachay-Cherkessia 212, Ingushetia 230, Finland 240 | spec per-nation table |
| 8 | How the per-nation figures are produced | "de-stacked 2026-07-05" by a randomization; tiers from weights 8 / 3 / 1; Russia annotation "added 2026-09-05" | same | "Rebalanced 2026-11-02, `DR-85`": successor states split by headcount, the Sinian Federation's share multiplied by 0.5719 and the freed points redistributed, Kazakhstan added at 1.45% (`DR-93`), Manchuria multiplied by 0.5855 (`DR-94`); tier labels from the final shares by "largest ratio gaps" (no longer produced by weights); per-nation shares still identical across the two censuses | spec L26 and the note under the table |
| 9 | Upper_Earth_Immigration_Composition Davis section | pool table (China sole T1; seven T2; 13 T3) | unchanged | table unchanged; one line added: "Final composition after the 2026-11-02 rework (`DR-85`): Primary Japan, Sinian Federation, United Kingdom, Germany, Korea; ..." | `Upper_Earth_Immigration_Composition.md` `### Davis`, pass L537-543; the added line follows the table |
| 10 | Founding Register row for Davis | **file did not exist** (created 2026-10-01, `ede29386`) | Australia, basis "extremely close... comparatively easy access", `DR-19`, status ruled | unchanged (the Register file itself changed 13 lines since 10-30, none in Davis's row) | `Founding_Register.md` L59 |
| 11 | Meaning of the census tag "(founding wave)" | undated annotation read by the pass as an in-world arrival datum | same | `DR-88` (2026-11-02): "a nation named as a founder in the Founding Register, and nothing else"; `DR-99` (2026-11-03): "the establishing country named in the Register, not people who arrived in a wave" | `DEVELOPER_RULINGS_LOG.md` L1550-1558 (`DR-88`), L1655+ (`DR-99`) |
| 12 | `09_Per_City_Baseline_Run.md` Davis row (humans / residents / required workforce / workforce / share) | 563,599 / 1,158,314 / 309,368 / 876,515 / 35.3% | 575,738 / 1,182,231 / 315,832 / 894,362 / 35.3% | 590,668 / 1,210,432 / **323,548 / 915,098 / 35.4%** | `09` L79 (header L52), same line at all three points |
| 13 | `16` Half B row (workforce / base / mandated / free) | 876,514 / 40.7% / 20.7% / 38.5% | 894,362 / 40.8% / 20.7% / 38.5% | **915,098 / 41.9% / 20.3% / 37.8%** | `16` L261 / L262 / **L262** |
| 14 | `16` section 19 (Davis's own determination, Option B) | baseline 357,063 (40.7%); mandated 246,740 (**28.2%**); free 272,712 (**31.1%**); distinctive tier 519,452 (59.3%); agriculture 181,808; technical half 64,932 | not recomputed (file's note said so) | baseline **383,295 (41.9%)**; mandated **252,606 (27.6%)**; free **279,197 (30.5%)**; distinctive tier **531,803 (58.1%)**; agriculture **186,131**; technical half 66,475; robot term adds 9,761 baseline workers | `16` L2006-2020 (heading L2006); the developer's Option B ruling text "Mandate 28.2% / free 31.1%" still stands at L2073-2076 |
| 15 | `16` Register-item-11 prose | "Davis alone: 306,780 producers... 1 per 51... 181,808... 124,972 workers apart" | same | **unchanged prose** (still 181,808 and 124,972) although the section 19 table now says 186,131: the live file carries two agriculture figures | `16` L2091-2094 |
| 16 | New national food files naming Davis | none (files 17, 18, 19 did not exist) | files 17 and 18 (convention B): Davis 50.8% of national export supply without Relung Panen, 39.6% with it (`17` L67, L82; `18` L48) | file 19 (2026-11-02, rerun 11-03): Davis **44.2%** of export supply (convention B); "Davis feeds about 1,309,000 people beyond itself"; the Davis/Esperanza denominator question "unchanged" | `19_National_Balance_Refresh_2026-11-02.md` L34, L44, L50, L81; `18_...` L31, L49 |
| 17 | Language rule (set 2026-11-03) | no language statement in any Davis input | none | Hawaiian (later Tepenian) dominant everywhere; supporting tier = every group within 12 points of the largest. Davis: largest group English 17.0-25.8%; Mandarin 13.3-14.1, Japanese 10.4, German 9.9 (Korean 8.3, Russian 4.5-11.6) | `Research_Logs/Language_Sets_By_City_Reference_2026-11-03.md` L30, L58, L71; `Language_Blocs_By_City_2026-11-03.md` `### Davis` (L916 onward) |
| 18 | Spec prose edits (excluding table rows) | line 8 "Australian Antarctic Division heritage"; the wind-versus-cold callout "(24 of the 37 are colder)... the mildest-conditions site on the East Antarctic coast"; line 143 "genuine research heritage" | line 8 and line 143 edited 2026-10-01 (`67d091af`) | callout rewritten 2026-11-02 (`DR-88`: "Davis has the mildest conditions on the East Antarctic coast it sits on", rank removed). **Everything else from pass L58-236 is byte-identical at L82-260** | spec L8, L112 (was L88), L167 (was L143) |
| 19 | Spec length and line numbers | 236 lines | 236 | **260 lines**; every line after the composition table moved **+24** (L127 is now L151, L143 is L167, L60 is L84, Notable Locations L207 is L231) | spec; checked by comparing L58-236 to L82-260 |
| 20 | `No_National_Stereotypes.md` (the binding anti-stereotype law, read in full at Phase 2) | 172 lines; says "founding nation"; records/journals/manuals may cross the gap; Acts "2564 -> early 2600s" | 172 lines | 174 lines (`ae54b47`, 2026-10-01): says "station-builder nation"; "Who founded each city is a separate question, answered only by the Founding Register"; "Records, research, results, equipment and techniques can cross the gap; personhood cannot" (`DR-25`, `DR-26`); Act 1 is "somewhere in the 2600s (a hazy range)" | universe repo `Reference/No_National_Stereotypes.md` (diff `ae54b47^..HEAD`) |
| 21 | Era timeline wording on Acts | "identity-timeline Act 2" | same | 2026-11-01 (`b1f20ff`): "identity has no Act, only a date on this timeline"; Act 2 now called "national identity's own date" | universe repo `Timeline Eras/2 The Second Interwar Period/Timeline.md` L251-258 |
| 22 | Division of Industry `README.md` | no banner | no banner | new top banner: founders only from the Register; a station's operator is never the cause of a sector; traditions are never inherited from a station | `Division_of_Industry/README.md` L3-7 |
| 23 | Davis lines in `Highways.md` | L197 Hwy 110 route | L197/L199 | unchanged text (L199); file grew 366 -> 397 lines only through other cities' material | `Infrastructure/Highways.md` |
| 24 | Davis in `Airports.md` | in the "no air access" list (L47, L52) | L50, L55 (+ Winter Intake Airport row L23 mentioning Davis as the placement of an unruled marker) | unchanged since 10-30 | `Airports.md` L3, L23, L50, L55 |
| 25 | Davis row in `Ports.md` | principal Indian-Ocean import port, tier CONSTRUCTED, `Neutral_Transshipment_Hubs` | row byte-identical; new distance tables from Hobart/Fremantle/Bunbury (Davis 4,814 / 4,712 / 4,576 km) | row byte-identical to the pass (diffed); the neutral-transshipment row names a renamed city (Sayowa -> Temirotkel) | `Ports.md` L130, L201, L224-232, L559, L736, L795 |
| 26 | Relationship entries naming Davis | `City_National_Connections` Davis section L296-308: three heritage ties (Mawson via namesake and "Australian-heritage network", Casey, Mirny) rest on the withheld megasheet | re-grounded 2026-10-30 (`DV-S02`) | unchanged since 10-30: Mawson "Australia is among the founders of both (`DR-19`; Founding Register)", Casey "both founded by Australia, on the same highway, Hwy 110", Mirny "Australia among the exile groups (Founding Register); Hwy 110, plus Relay Vaults link"; the three scientific prospects unchanged. `City_Cross_Subnet_Relationships` L123-128 still cites `Davis_Full_Extrapolation.md` (withheld) for the "symbolic-only, severed" nature of the Davis-Mawson tie | `City_National_Connections.md` L303-315; `City_Cross_Subnet_Relationships.md` L121-132; `City_Relationship_Database.md` L186-187 (Mirny's "Australian" row got Ariun Nuur and Relung Panen, a rename and an addition) |
| 27 | Symbol assignment | Earth / Earth until blanked on 2026-09-16 | BLANK, L112 | unchanged (0 commits since 10-30) | `City_Symbol_Assignments.md` L112, L335-341 |
| 28 | `Local_Cultures/Mirny_Subnet/Davis.md` | pass-time text | two wording edits 2026-10-01 (founders re-grounded) | unchanged since 10-30; still says "sole-China-Primary" (L28), "Mandarin (Primary tier)" (L104), "thirteen nations" (L107, L199) | file L24-28, L104-107, L199 |
| 29 | `Local_Robot_Culture/Mirny_Subnet/Davis.md` | pass-time text | unchanged | unchanged | file |
| 30 | `Extent_and_Density_Per_City.md` Davis rows | 1,158,314 on 410 km2 = 2,825/km2 | same | **same, not updated** (still 1,158,314 and 2,825) | L617, L636 |
| 31 | Universe-repo canon the pass opened | `Falkland_Treaty/` (3 files), `Timeline.md` (562 lines, 0 Davis hits), `World_History_Reference.md` (346 lines, 1 Davis hit) | - | Treaty folder unchanged since 2026-08-07; `Timeline.md` 825 lines, still 0 Davis hits; `World_History_Reference.md` 351 lines, still 1 Davis hit | universe repo |
| 32 | Davis inspiration picks | Tyumen [PRIMARY], San Luis Potosi [SECONDARY], Guatape [SECONDARY] | same (header note added 2026-09-22, inside the pass window) | identical to 10-30 (diffed) | `Inspirational-Influences.md` `##### Davis` (L81-91) |

### Raw diff excerpts (the five most important changes)

**(a) Spec composition: tier lines and first rows** (`git diff d2dd2136 HEAD -- Specs/Mirny subnet/Davis.md`):

```
-| Primary | China |
-| Significant | Japan, Germany, UK, South Korea, Russia *(added 2026-09-05 ...)*, Indonesia, Australia *(founding wave)* |
-| Notable | Thailand, Ukraine, Vietnam, Philippines, Malaysia, Romania, South Africa, New Zealand, Belarus, Bulgaria, Lithuania, Latvia, Estonia |
+| Primary | Japan, Sinian Federation, United Kingdom, Germany, Korea |
+| Significant | Indonesia, Australia *(founding wave)* |
+| Notable | Thailand, Vietnam, Philippines, Malaysia, Taiwan, Russia (core state), South Africa, Romania, Ukraine, New Zealand, Idelsk-Uralia, Belarus, Kazakhstan, Bulgaria, Austro-Bavaria, ... Tuva |   (38 names)
-| Primary | China | 19.04% | 113,234 | 107,309 | 65,530 | 83,285 |
+| Primary | Japan | 10.42% | 64,576 | 61,547 | 37,862 | 47,318 |
+| Primary | Sinian Federation | 9.72% | 60,212 | 57,384 | 35,301 | 44,117 |
...
+| Notable | Tuva | 0.013% | 78 | 74 | 45 | 57 |
```

**(b) Census rows** (`Official_Population_Census.md`):

```
pass  L496: | 13 | Davis | Mirny | 563,599 | 594,715 | **1,158,314** | *(revised 2026-07-04)* |
10-30 L494: | 13 | Davis | Mirny | 575,738 | 606,493 | **1,182,231** | ... Scenario DR-68 ... |
now   L506: | 13 | Davis | Mirny | 590,668 | 619,764 | **1,210,432** | ... DR-90, 2026-11-02: +14,930 H / +13,271 R from the Esperanza relocation. Arithmetic, NOT a migration. |
now   L650: | 14 | Davis | Mirny | 454,101 | 363,374 | **817,475** | ... DR-90: +8,570 H / +11,462 R ... |
```

**(c) Division of Industry rows** (`16` L261/262 and `09` L79):

```
16 Half B  pass : | Davis | Mirny | 1.25 | 876,514 | 40.7% | 20.7% | 38.5% | C |
16 Half B  now  : | Davis | Mirny | 1.25 | 915,098 | 41.9% | 20.3% | 37.8% | C |
09 L79     pass : | 26 | Davis | Mirny | 1.25 | 563,599 | 1,158,314 | 309,368 | 876,515 | 35.3% |
09 L79     now  : | 26 | Davis | Mirny | 1.25 | 590,668 | 1,210,432 | 323,548 | 915,098 | 35.4% |
16 s.19    pass : Mandated 246,740 28.2% | FREE 272,712 31.1% | Distinctive tier 519,452 (59.3%) | agriculture 181,808
16 s.19    now  : Baseline 383,295 41.9% | Mandated 252,606 27.6% | FREE 279,197 30.5% | Distinctive tier 531,803 (58.1%) | agriculture 186,131
```

**(d) The tag ruling** (`DEVELOPER_RULINGS_LOG.md`):

```
DR-88 (2026-11-02): "(founding wave)" now means a nation named as a founder in the Founding Register, and nothing else.
DR-99 (2026-11-03): (2) The census tag "(founding wave)" means the establishing country named in the Register, not people who arrived in a wave.
Founding_Register.md L59:  | Davis | Mirny | +5 | ✅ | Australia | "extremely close... comparatively easy access" | DR-19 | - |
```

**(e) The anti-stereotype law the pass read at Phase 2** (`No_National_Stereotypes.md`, `ae54b47`, 2026-10-01):

```
+**Who founded each city is a separate question, answered only by the Founding Register** (...). A city's founders stand on geography and access ... never on the station (`DR-19`).
-**Preserved records, not personhood, can still cross the gap.** ... journals, logs, and orientation manuals left behind are artifacts ...
+**Records, research, results, equipment and techniques can cross the gap; personhood cannot.** ... (`DR-25`, `DR-26`)
```

---

## 3. Dependent findings

Class key: **N** = number or label only; the value must be updated, the finding stands. **W** = wording or identity statement now false as written; the finding probably stands. **C** = a conclusion or reasoning step was derived from the changed input and might come out differently on re-derivation. **U** = cannot tell without re-running. Line numbers are in the pass files as they stand now (the pass files were not edited by this review).

### 3.1 Class N (numbers and labels): 11 items

| # | Pass file and line | What it says | What changed | Note |
|--:|---|---|---|---|
| N-1 | `00_Frame.md` L65, L89-90, L136; `00.1_Step_MINUS-1_Input_Contract.md` L64-71, L168-171; `03_Research.md` L164; pass `README.md` L49 | Census I 1,158,314 and Census II 781,596; "robots 594,715 -> 344,173 (-250,542); humans 563,599 -> 437,423 (-126,176)"; Band 5 | Totals now 1,210,432 / 817,475; robots 619,764 -> 363,374 (-256,390); humans 590,668 -> 454,101 (-136,567); departures 392,957 | Band 5 and the status "LIVING" are unaffected. The Frame's warning at L136 ("anything scaled off 1,158,314") now names the wrong figure. |
| N-2 | `00_Frame.md` L236, L342-349; `02_Spine.md` L112-113, L369-371, L389-394; `04_Phase_02` L283-292, L1217-1218, L1241-1262; `04_Phase_09` L59-60, L67 | Retention 67.48% combined, 77.61% humans, 57.87% robots, spread 19.74 pp; robots 51.34% -> 44.03% of the city; humans 22.39% departed, robots 42.13%; "robot departure rate nearly twice the human rate" | Now 67.54% / 76.88% / 58.63%, spread **18.25 pp**; robots 51.20% -> 44.45%; humans departing 23.12%, robots 41.37% (ratio 1.79, was 1.88) | The direction of every statement holds (humans retain more; robot-majority at Census I, human-majority at Census II; "more than one in five humans departed"). The Frame's "strongest finding available at Step 0" (L342) keeps its shape. |
| N-3 | `02_Spine.md` L318-331; pass `README.md` L75 | 1,158,314 / 410 km2 = 2,825.16 per km2, "reproduces the source's own stated density exactly" | 1,210,432 / 410 = **2,952.27**; the source (`Extent_and_Density_Per_City.md` L617, L636) itself still says 1,158,314 and 2,825, so the "reproduces the source" check now fails by 4.5% for a reason that is the source's staleness | Band stays UNDETERMINED; no finding rests on the density. |
| N-4 | `07_QA.md` L319-330 (Gate 11 raw block) | density at 200 / 400 / 420 / 512 km2: 5,792 / 2,896 / 2,758 / 2,262 per km2 (Census I); worst case "between London and New York" | Recomputed: 6,052 / 3,026 / 2,882 / 2,364 (Census I); 4,087 / 2,044 / 1,946 / 1,597 (Census II). The gate's verdict (PASS at all four area figures; worst case still below New York's ~11,000) is unchanged | The pasted block should be re-pasted if the gate is rerun. |
| N-5 | `04_Phase_04` L28, L265-267; `04_Phase_07` L32, L87; `04_Phase_08` L146; `04_Phase_10` L475, L564; `07_QA.md` L133, L138; `05_Reconciliation.md` L13 (tier-1 source "16's determinations") | Workforce 876,515; required workforce 309,368; "35.3% of the workforce required for survival"; "876,515 people are not six roles" | Workforce **915,098**; required **323,548**; share **35.4%** | The general-population arguments (a sector is not the city) do not depend on the count. |
| N-6 | `04_Phase_04` L27, L201, L269-270, L284, L418; `04_Phase_07` L99-100; `04_Phase_08` L224; `08_Review_Panel.md` L164, L308; `10_Readiness_Check.md` L104; `05_Reconciliation.md` L102; `00.1` L351-353 | Mandate 28.2%, free 31.1% (Option B); Half B row 40.7% / 20.7% / 38.5% | Section 19 table now **27.6% mandate, 30.5% free**, baseline 41.9%, distinctive tier 58.1%; Half B row 41.9% / 20.3% / 37.8% | The developer's ruling text still reads "28.2 / 31.1" (`16` L2073-2076), so a re-run must choose between the ruling's labels and the recounted table. Option B itself (35% agriculture plus half of technical/scientific = 47.5% of the distinctive tier) is unchanged. The Impotent Lover remark ("the free tier is 31.1% and what fills it is unwritten") still reads the same with 30.5%. |
| N-7 | `04_Phase_07` L91, L110, L120, L389, L407; `04_Phase_04` L285 | Agriculture sector = 181,808 workers, "settled" | `16` section 19 table: **186,131**. The same file's Register-item-11 prose (L2091-2094) still says 181,808 and "124,972 workers apart" | Two live values in the source; the pass's "settled at 181,808" is now stale by 2.4%. The whole-workforce figure 306,780 (file 04) is also older. |
| N-8 | `04_Phase_07` L116-123 (own-need and export table: 37,338 / 85,031 / 0 and 144,470 / 96,777 / 181,808) | The three live values of the own-need term and the resulting export numbers | All three depend on population and workforce, so all move | The structure (a two-fold spread on one term) is unchanged. See U-1 for the new national files. |
| N-9 | `04_Phase_09` L16-17, L59-60, L67, L174; `04_Phase_08` L18, L106-107; `04_Phase_09` L102, L198; `04_Phase_04` L244 | Census I split 563,599 H / 594,715 R, "51.3 / 48.7 is not dominance"; "a majority-robot city" | 590,668 H / 619,764 R, **51.2 / 48.8**; Census II 454,101 H / 363,374 R | Still majority-robot, with a thinner margin. "Not dominance" and the lens decision stand. |
| N-10 | `04_Phase_02` L948-949 | "the model's own product for the largest origin share is about 220,543 at Census I; the founding-wave community about 57,105" | Largest row (Japan) 126,123; Australia 69,475 | Numbers only here; the reasoning built on them is C-2. |
| N-11 | `01_Inherited.md` L70; `02_Spine.md` L108, L250; `04_Phase_02` L226, L306, L585, L631 | "the founders are 4.93%" (fire #3, deficit D5, "no precedence politics can form") | **5.74%** (tied with Indonesia) | "Too small to host and no later wave, so no precedence politics" still holds at 5.74% against five Primary rows of 8.35-10.42%. The tag's meaning is C-1. |

### 3.2 Class W (wording or identity statement false as written): 7 items

| # | Pass file and line | What it says | What changed | Note |
|--:|---|---|---|---|
| W-1 | `04_Phase_02` L26, L67, L349, L357, L485, L960-976, L1014, L1071, L1397, L1482, L1492; `02_Spine.md` L37, L107; `01_Inherited.md` L50; `04_Phase_06` L207; `04_Phase_07` L379; `04_Phase_08` L240; `04_Phase_09` L77, L96; `Cross_City_Culture_Differentiation_Table.md` L145 | "21 origins", "twenty-one communities", "twenty of twenty-one origins", "Notable tier counted as 14 -> 13; 21 total stands" | **45 rows** (5 / 2 / 38) | The phrase is carried into the Step 6 differentiation table cell (L145) as well. |
| W-2 | `04_Phase_02` L26 (table "1 / 7 / 13"), L297-309; `02_Spine.md` L107 ("largest at 19.04%... 13 nations at Notable"); `01_Inherited.md` L70 ("the Primary tier is another [community] at 19.04%") | "Primary: China (sole)"; "Davis has no majority origin. Its largest is a minority in its own city, at roughly one person in five" | Primary is five rows; the largest is Japan at 10.42% (roughly one person in ten); the China row is now the Sinian Federation at 9.72% | "No majority origin" stands more strongly. "One person in five" and "a sole-occupant tier's own share" (L324-326) are false. |
| W-3 | `04_Phase_02` L227, L236, L240 | "Davis is a founding-wave-Australian, plurality-Chinese Tepenian city" | The plurality is Japan (10.42%); the Sinian Federation is second (9.72%) and 0.7 points behind the top | The structure of H-2 is C-1. |
| W-4 | `02_Spine.md` L129-132; `01_Inherited.md` L78 (load-bearing fire #11); `04_Phase_02` L317 | "The tiers are a production weight, not a social fact" (the tier shares came from 8 / 3 / 1 share weights) | Tiers are now labels derived from final shares ("largest ratio gaps"); the weights "no longer produce the figures" (spec note under the table) | The guard (do not read tiers as rank or caste) is still prudent; its stated ground is out of date. |
| W-5 | `00_Frame.md` L99; `04_Phase_02` L852-888 ("once per Act"), L859 ("the 21 origins are live national identities - X who live in Antarctica"); `04_Phase_09` L76 | Acts used as identity phases; Act 1 "hazy range" | Universe repo 2026-11-01 (`b1f20ff`): "identity has no Act, only a date on this timeline"; Act 2 renamed "national identity's own date". Substance (hazy Act 1 into the 2600s, identity solid by the Tower, about 2688) is unchanged | Terminology to reconcile; findings stand. The Phase 2 text also treats the successor-state rows as "live national identities". |
| W-6 | Every pass file that cites the spec by line (`00.1` x ~25, `00_Frame` x ~12, `01_Inherited` x ~20, `02_Spine`, `04_Phase_02`, `04_Phase_05`, `00.1a`); census lines "392-398, 496, 613" (`04_Phase_02` L26; `00.1` L65) | L127, L143, L60, L117, L120, L129, L131 and the like = the spec as of 2026-09-16 | The spec after its composition table moved **+24 lines** (L127 is now L151, L143 is L167). On 2026-11-02 an automatic remap changed only six places (`00.1` L286, L303, L341; `00.1a` L1, L58, L60, L75, L85, L124, L146, L251; `00_Frame` L183) and left the rest, so the pass now cites **both numberings** (for example `01_Inherited` still L127 x12, `00_Frame` has one L151 and three L127). Census Section A is still L392-396; the Census I and II rows are now L506 and L650 | Mechanical, but a reader following a citation lands on the wrong line in most files. |
| W-7 | `04_Phase_05` L23, L203, L345; `Amendment_Notes` DV-002 | "Davis holds a confirmed airport marker"; arrival type 3 "by air" | **Not drift.** `Airports.md` listed Davis among the no-air-access cities at pass time (pass L47, L52); the pass misread it. The 10-30 note frames it as a later change | Finding "four arrival types" becomes three; road, sea and the treaty-right type stand. |

### 3.3 Class C (conclusions that might come out differently): 7 items

| # | Pass file and line | What it says | What changed | Note: which step and why |
|--:|---|---|---|---|
| C-1 | `04_Phase_02` H-2 (L224-258), A.2 closing (L324-331), A.3 (L334-345), B.4 (L583-636), hole `H6` (L1400), third doubt (L1598); `02_Spine` D5 (L250); `01_Inherited` fire #3 (L70); `Cross_City_Culture_Differentiation_Table.md` L62 | "Davis is a founding-wave-Australian, plurality-X city; founding stock and plurality stock are two different communities"; the tag is "the only route datum... the only thing that says when"; layer call (tag = in-world content, because undated) is "the most load-bearing interpretive call in the file"; "if ruled authoring, H-2 loses its first term and this phase must be re-run" | `DR-88` and `DR-99`: the tag means "the establishing country named in the Register, not people who arrived in a wave". The Register (absent at pass) names Australia as sole founder on geography and access | The ruling resolves `H6` in a third way (neither an arrival datum nor a pure authoring note). H-2's core contrast (the founding country is not the plurality) very probably survives (Australia 5.74% against Japan 10.42%), but its mechanism language ("founding wave", "arrived all at once and never followed", "founding population") has to be rewritten, and the claim that the tag says anything about route or timing is gone. The Phase 2 axis row in the Step 6 table ("native within two generations; no arrival mode operating since") rests on the treaty reading and the born-here inference, not the tag, and is not affected. |
| C-2 | `04_Phase_02` C.2 (L939-950), C.3 (L953-976), C.5 (L1012-1021), killed finding O-1 (L1448), `P.2` item 1 (L1482) | Killed finding: "origin culture survives only in one-person forms" was FALSE because "not one of the 21 lacks numbers for a liturgy, a street, a kitchen or a conversation"; so "21 substantial communities... a rich internal layer, twenty-one-fold, fully staffed, carried at full scale" over a thin procedural civic layer | 45 rows; **10 rows are under 0.1%** (152 to about 1,200 people at Census I; Tuva 152, Karachay-Cherkessia 212, Ingushetia 230, Finland 240, North Ossetia-Alania 309, Kabardino-Balkaria 405, Tibet 572) and 17 are under 0.5% | The scale check is a per-row test and would fail for the smallest rows, so the killed finding is partly alive for them and "fully staffed" is false for them. The two-layer conclusion and its lapse mechanism (C.4) very probably stand for the large and middle rows; restating them needs a size qualifier. Several of the new rows are regional or successor-state labels, not countries (Manchuria, Tibet, Chechnya, Dagestan, Aceh, West Papua, Patani, Donska-Kubania, Idelsk-Uralia), which also changes what "an origin practice" means. |
| C-3 | `04_Phase_02` E.1 (L1060-1081) | "Davis's 21 origins are not a sample of humanity. They are a sample of where robots were"; the composition is "a fossil record of the pre-exile global distribution of robot manufacture"; derived from the Assembly's membership note ("no robot populations of their own" are the exclusions) | `DR-85` added rows for places never counted before (Taiwan, Hong Kong, Macau, Mongolia, North Korea, Kazakhstan, Austria and others; pools estimated from the three nearest nations on income and inequality) and split countries into successor and regional rows | The inference runs through the treaty's membership list. Whether every new row is a "robot-holding" origin by that test must be re-checked row by row; membership-not-rank (the fourth order refusal) is unaffected. |
| C-4 | `01_Inherited` L87-88, L274; `04_Phase_02` L50 (n/a row), L318-320 (limit 2), L324; `02_Spine` L116-118 | "No two nations' figures may be compared, at any precision, in either direction: the within-tier ordering is an artifact of the de-stacking randomization"; the per-nation table is "present but SEALED" | The ordering is no longer the 2026-07-05 randomization: rows now follow headcount-based pool shares, with random multipliers only on the Sinian Federation (0.5719) and Manchuria (0.5855). Identical-across-censuses is kept (each row's Census II/I ratio is the same, checked for Japan and Sinian Federation: 0.675) | The part of the seal that rests on "identical by construction" (fire #2: which communities left is permanently unanswerable) survives. The part that rests on "ordering is a randomization artifact" no longer has its ground; a re-derivation might allow ordering statements within the city, or keep the seal on other grounds. |
| C-5 | `04_Phase_05` L35-36, L303-306, hole `H31` (L330), L346, L383-386 | The three heritage relations (Davis-Mawson; Casey; Mirny) are "structurally excluded... no admissible independent route exists; searching harder will not surface one"; "Davis's relational content is largely unwritten" | Since 2026-10-01/10-30 the national-connection entries rest on the Founding Register and Hwy 110: Mawson "Australia is among the founders of both", Casey "both founded by Australia, on the same highway", Mirny "Australia among the exile groups; Hwy 110; Relay Vaults link". The cross-subnet file still cites the withheld megasheet for the severed, symbolic-only character of the Davis-Mawson tie (L123-128) | A re-run would likely admit the Casey and Mirny ties and the Mawson founding-country link, and not the megasheet-sourced "severance" claim. `H31` is answered, 5a's "what does not flow: any heritage relation" and the "largely unwritten" headline need revision. This was done at the sources on 2026-10-30 (`DV-S02`) but the note recorded only the re-grounding, not that the pass's exclusion rationale is overtaken. |
| C-6 | `04_Phase_08` E.1 (L238-245), hole `H48`; `04_Phase_09` L92 (Language row) | "What any given community speaks is NOT written, and DR-4 defers the distribution"; "Davis's dominant local layer is thin and procedural"; the robot Language Module "tracks the dominant local culture AND the community who had her built" | Language rule set 2026-11-03: Hawaiian (later Tepenian) dominant everywhere; Davis's supporting tier is English (largest group 17.0-25.8%), Mandarin (13.3-14.1), Japanese (10.4), German (9.9) | `H48` is partly answerable now. The E.2 conclusion ("what marks someone as from Davis is how they make a claim, not how they pronounce it") was derived from Phases 6 and 7 and very probably stands, but it was reached with the language question open; a re-run should state it against the national language and the four supporting groups. |
| C-7 | `02_Spine.md` L107, L116-118; `04_Phase_02` A.4 (L347-363), B.2 chain (L461-476) | "21 origins, largest at 19.04% therefore nothing load-bearing can be tacit; everything must be explicit"; "a tacit norm is one a majority carries... with no majority, a tacit norm has no carrier"; "explicit and inert" | 45 origins, largest 10.42%, no row above 10.5% | The argument is a-fortiori stronger with the new table. Expected to survive. Listed because it is a reasoning step derived directly from the changed input. |

### 3.4 Class U (cannot tell without re-running): 5 items

| # | Pass file and line | What it says | What changed | Note |
|--:|---|---|---|---|
| U-1 | `04_Phase_07` A.2 (L102-123), A.2b (L125-138), `H39` (L407); `05_Reconciliation` L102-110 | The export headcount cannot be written because the own-need term has three live values; the "feeds a third of Tepenia" headline "is not a fact this pass may assert" | New post-pass files 17, 18, 19: under convention B Davis is 44.2% of national export supply and "feeds about 1,309,000 people beyond itself"; the Davis/Esperanza denominator question is declared "unchanged" (file 19 L50) | The pass's refusal still reads correct (no resolution of the denominator), but there are now two documented magnitudes and a national role statement; whether `H39` narrows is a re-run decision. |
| U-2 | `02_Spine` G4 profile (L90-101), L158-182 (the `G2` x `G4` conflict); `04_Phase_02` B.6 (L708-743, "Davis inherited a library and not a soul"), L38-41 | The inheritance that crossed the gap is the documentary record (journals, logs, manuals); everything else "requires occupation" | `ae54b47` + `DR-24/25/26`: "records, research, results, equipment and techniques can cross the gap; personhood cannot"; a tradition cannot cross; skills may be "rediscovered from the station's records, research and equipment" | The thesis (no living institution; the rebuilt competence is Davis's own) still follows. Whether G4's strength column and the "stationary subject" argument should list equipment and techniques as inherited is open. |
| U-3 | `04_Phase_10` F.3 (L499-503, "Character canon returns nothing for Davis"); `Local_Cultures` L7c | No figures sited in Davis | **Not drift, a pass-time gap:** the game repo's own `Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/TBN [STP-06 thicc Chinese Hao]/` (README created 2026-07-20, last edited 2026-10-01) lists "Davis, Tepenian Federation" as her present-day primary location and reasons from "Davis's own China-Primary founding tier" and "Davis's 20.51%" (old figures) | The pass searched the universe repo's characters and the Enneagram index, not this folder. A character draft placed at Davis would not contradict the "no notable figure in the spec" finding but would change "zero, verified". |
| U-4 | `00.1_Step_MINUS-1_Input_Contract.md` section 4 (admitted ranges `1-3,5-8,10-87,...`, strikes L21, L27, L37, L54, L28), `00.1a` | The contract classifies spec composition lines L13-57 (a 21-row table with a de-stacking note at L28 and a share-weighting note at L54) | The composition block is a different block (45 rows, new notes, the Russia parenthetical removed) | The classification cannot be reused; a re-run starts Step -1 over for the composition region. |
| U-5 | `05_Reconciliation` (whole file; tier 3 = `Local_Cultures` and `Local_Robot_Culture`) | The check files were compared on polar night, counterculture, credit kinship, glitch-coolant absence, GPS narrowing, the port ruling | `Local_Cultures/Davis.md` still carries the pre-rework composition ("sole-China-Primary", "Mandarin (Primary tier)", "thirteen nations") and the 66-67 day polar night that `H61` already flagged; neither file was edited | None of Step 5's compared findings touches composition, so its findings are not affected. A re-run would meet a check file that contradicts the new table. |

**Totals: N 11, W 7, C 7, U 5 (30 items).** Note that W-7 and U-3 are not drift (they are pass-time faults found while tracing), counted for completeness.

### 3.5 Checked and not affected (findings that do not depend on any change)

- **Phase 3** (surface and texture): rests on the Climate READER file for Davis (0 commits since the pass) and the unchanged spec climate block; the one spec sentence changed in that area (the wind-versus-cold callout) is not quoted or used anywhere in the pass (searched for "24 of the 37", "mildest", "East Antarctic coast": no pass hit).
- **Phase 6** (meaning): only L207 ("twenty-one-fold", W-1). The record-proposition, "truth is not singular", and the mortuary reservation (`A-1`) do not touch any changed input.
- **Phase 7 Sections B, C, D** (governance, knowledge, private life): the registrarial finding, credit kinship, the unattached, the counterculture result and the sanction pricing do not depend on composition or counts; the only changed input they cite is the 28.2 / 31.1 / 181,808 set (N-6, N-7).
- **Step 5 findings** (U-5), **Step 6** (apart from the "21-fold" cell, W-1), **Step 8** (Review Panel: apart from the 31.1% mention, N-6), **Step 9/9.5/10** (record keeping; nothing numeric except as listed).
- **The port ruling** (2026-09-16) and the Davis row of `Ports.md`: byte-identical to the pass.
- **`G6` null (no in-frame defining event):** the era `Timeline.md` grew from 562 to 825 lines and still names Davis zero times; `World_History_Reference.md` still has its one match. The null's status is unchanged.
- **The Falkland Treaty readings** (Articles II.2, II.3, I.4, IV, V.2, VI.1): the treaty folder has had no commit since 2026-08-07.

---

## 4. Checked and unchanged

| Category | Result |
|---|---|
| Climate (READER file for Davis), the spec climate table and ice-free area statements (~400 km2) | `READER/Davis.md`: 0 commits since pass. Spec body from the Geographic section to the end is byte-identical at +24 lines except the wind-versus-cold sentence and line 143's wording |
| Extent (410 km2) | Unchanged, but `Extent_and_Density_Per_City.md` still shows the pre-rework population (row 2 above, item 30) |
| `Precipitation_Falls_vs_Lands.md` Davis line; `Antarctic_Stations_With_Airstrips.md` Davis lines | 0 commits, same Davis line counts |
| Highways (Hwy 110 Zhongshan -> Davis -> Mirny -> Casey -> Concordia) | Davis text unchanged since the pass |
| Airports (Davis in the no-air-access list; Winter Intake Airport placed "between Davis and Mirny") | Davis lines unchanged since 10-30; the list text already said Davis had no airport at pass time |
| Ports (Davis principal import port, CONSTRUCTED, neutral transshipment) | Davis row byte-identical; new Hobart / Fremantle / Bunbury distance tables are additive; the transshipment row's Sayowa -> Temirotkel is a rename |
| `Arcanet.md` | 0 Davis hits at all three points |
| `Geothermal_Heating.md` | 0 Davis hits at all three points (Phase 5's heat finding stands) |
| `National_Medical_and_Care_Institutes.md` Davis sentence ("Davis can be supplemented by fishing fleets") | Byte-identical at L23-25; the file's other edits are renames and an Esperanza figure |
| Symbol assignment (`City_Symbol_Assignments.md`) | BLANK at L112; 0 commits since 10-30 |
| Zodiac substrate and `Zodiac_Signs_Full_Attributes.md` | Only a 2026-10-04 city-rename sweep touched them |
| `Inspirational-Influences.md` Davis picks | Identical to 10-30 and to the pass (Tyumen, San Luis Potosi, Guatape); the 11-03 edits concerned other places |
| `Local_Robot_Culture/Mirny_Subnet/Davis.md` | 0 commits since the pass |
| `Local_Cultures/Mirny_Subnet/Davis.md` | Two wording edits on 2026-10-01 (operator wording), none since; composition text is stale (item 28) |
| Division of Industry file 11 (caloric rebuild) Davis line; files 04, 08, 10, 13, 14 Davis line counts | 0 commits (file 11) or same Davis line counts; the only text change in file 04 for Davis is a rename (Vostok -> Ariun Nuur) |
| `City_Relationship_Database.md` Davis entry (L186-187) | Unchanged since 10-30 (the earlier shift was the 2026-10-21 edit the note recorded) |
| `National_Economy_and_Currency.md`, `National_Holidays.md`, `Energy_Grid_Failure_Rationale.md`, `Weapons_and_Tools_Philosophy.md`, `City_Logistics.md`, the two Robot physiology files | 0 Davis hits at all three points; `Robot_Physiology_and_Cultural_Practices.md` has 1 commit since the pass (no Davis line) |
| The Falkland Treaty folder (Treaty, Scaffold, Real_World_Influences) | No commit since 2026-08-07 |
| Davis in the Enneagram character index | 0 hits at pass and now |
| Davis's Band (5 at Census I) and status (LIVING) | Both hold at the new totals |
| Ruling `DR-4` (Census I governs) | Unchanged |
| Methodology files the pass followed (runbook, `01`-`04`, Disciplines) | Not assessed in depth. Several commits since the pass (runbook 9, `03_The_Phase_Spine` 6); the 2026-10-01 station-heritage audit fixes were already applied to the pass on 2026-10-01 (`4a59fab8`). A method-change review is a separate task |

---

## 5. Amendment-note figures that are stale again

`Amendment_Notes_2026-10-30_Manual_Input_Audit.md` records "live" figures as of 2026-10-30. Against the current sources:

| Note entry and line | Note says | Now | Cause |
|---|---|---|---|
| DV-001 table, L19 | Census I 575,738 + 606,493 = **1,182,231** | 590,668 + 619,764 = **1,210,432** | `DR-90` Esperanza relocation |
| DV-001, L20 | Census II **797,443** (445,531 + 351,912) | **817,475** (454,101 + 363,374) | `DR-90` |
| DV-001, L21-25 | retention combined 67.45%, humans 77.38%, robots 58.02%, spread 19.36 pp, robots 51.30% of Census I | **67.54%, 76.88%, 58.63%, 18.25 pp, 51.20%** (Census II robots 44.45%) | `DR-90` added to the two censuses by unequal ratios (Census II +8,570 H / +11,462 R against Census I +14,930 H / +13,271 R) |
| DV-001, L26 | density 2,883.49 per km2 | **2,952.27** | totals |
| DV-001, L27 | humans departed 130,207 = 22.62% | **136,567 = 23.12%** | totals |
| DV-001, L28 | people gone 384,788 | **392,957** | totals |
| DV-001, L29 | `09` row 315,832 / 894,362 / 35.3% | **323,548 / 915,098 / 35.4%** | totals |
| DV-001, L30 | `16` Half B 894,362 / 40.8% | **915,098 / 41.9%** (MAND 20.3%, FREE 37.8%) | totals and the robot term (`DR-97`) |
| DV-001, L13 | "per-nation shares are unchanged (for example China stays at 19.04%, the figure `02_Spine.md` records as the largest)" and L40 "None of the shares changed" | **False now.** 45 rows; the China row is the Sinian Federation at 9.72%, second; the largest is Japan at 10.42%; Australia 5.74% (was 4.93%) | `DR-85`, `DR-93`, `DR-94` |
| DV-001, L40 | ratio findings "move by 0.03 to 0.4 percentage points" | retention spread moved 1.49 points from the pass (19.74 -> 18.25); human retention 0.73 points, robot 0.76 points | `DR-90` |
| DV-006, L96-97 | Half B 894,362 / 40.8%; section 19 baseline 357,063 (40.7%), mandated 246,740 (28.2%), free 272,712 (31.1%), summing to 876,515; "the file's first line states the per-city determinations were not recomputed" | Half B **915,098 / 41.9% / 20.3% / 37.8%**; section 19 now **383,295 (41.9%) / 252,606 (27.6%) / 279,197 (30.5%)**, distinctive tier 531,803; the section 19 table **was recomputed** (2026-11-03, with the robot term) while the developer's ruling text at L2073-2076 still reads 28.2 / 31.1 | `DR-90`, `DR-97` |
| DV-006, L100 | "section 19's worker counts predate DR-68 and are re-run when baselines are re-run" | Done: re-run 2026-11-03 | `DR-97` |
| DV-007, L108 | file 18 L48 gives Davis 39.6% of export supply | file 18 now quotes **44.3%** (L49), and file 19 (rerun) **44.2%** (L81) | `DR-90`, `DR-91`, `DR-97` |
| DV-005, L85-89 | spec is **236 lines**; contract classifies L1-181; unclassified L182-236 | spec is **260 lines**; the composition block (L13-76) is new text; everything after the table is +24 (so the pass-time L182-236 is now L206-260) | `DR-85` table growth |
| DV-004, L72, L79 | spec L129 ("shares Australian founding-wave heritage"), Developer-vision paragraph L143 | now L153 and L167; Significance line L8 unchanged | +24 shift |
| DV-002, L46-52 | "Davis has no air access" framed as a change since the pass ("the source says otherwise") | Correct that Davis has no air access, but `Airports.md` said so at pass time (pass L47, L52); this is a pass-time misreading (W-7), not drift | - |
| DV-008 table, L118-125 | Davis line positions in Highways, Ports, Airports, Relationship and Connections files | Still correct at HEAD (checked: Highways L199; Ports L559, L736, L130, L201, L224, L795; Airports L3, L23, L50, L55, L57; Relationship L186-187; Connections L303-315) | none |
| DV-001, L33-39 ("where the pass rests on the old figures") | list of files with the old counts | still a correct list for the numbers, and incomplete for composition (it does not list the 19.04% / 4.93% / 21-origins sites, which the note correctly left out at that date) | `DR-85` |

---

## 6. Ranked recommendation

**A. Most plausibly needs re-derivation (partial, targeted):**
1. **Phase 2 (composition and arrival), first.** The 4.93% / 19.04% / 21-origin / Chinese-plurality statements (W-1 to W-3, N-10, N-11), H-2 and `H6` (C-1), the scale check and the two-layer structure (C-2), the origins-equal-robot-world argument (C-3) and the comparison seal (C-4) all rest on the old table. The Phase 2 file itself says "when the deferral lifts, come back to Phase 2 first"; the table has been replaced, so the same first-place logic applies. Plausible changes: H-2 is rewritten around the Register founder (not a wave); the "21-fold" structure becomes a 45-row structure with ten tiny rows; the seal on ordering may lift or be re-grounded.
2. **Step -1 and Step 1 for the composition region only** (U-4; Step 1 fire #3, #11 and the 2-D guard) since Phase 2 depends on their classification of the table.
3. **Phase 5 relations** (C-5): the heritage ties are no longer structurally excluded; this changes 5a and `H31` and the "largely unwritten" headline. Reassess 5d too (the by-air type is wrong anyway, W-7).
4. **Spine Item 2 G8 and D5 entries** (C-7, N-11) and the **spine clause "did not choose its remaining population"** are expected to stand; they need the new values rather than a new argument.

**B. A dated amendment note is enough (numbers or wording; finding stands):**
5. Phases 4, 7, 8, 9, 10 and Steps 0, 1, 2, 7, 8, 9, 10: the N items (population, retention, workforce, tier shares, agriculture, density, Gate 11) and W-1/W-2/W-4/W-5. A replacement for the 10-30 note should carry the table in section 5 and the corrected statement that shares did change.
6. Phase 8 section E and Phase 9 language line (C-6): one added paragraph stating the language rule and the four supporting groups; E.2 is expected to stand.
7. Citation hygiene (W-6): either finish the line remap across all pass files or add a one-line conversion note (+24 after the composition table) at the top of the pass README.
8. The Phase 5 airport statement (W-7) as an erratum, since it was never a change in the source.

**C. Needs nothing:** Phase 3 and Phase 6; Phase 7 sections B-D; Step 5's findings (U-5, with the caveat that the check files are stale); Step 6's table row except the "21-fold" phrase; the port ruling; the `G6` null; the Treaty-derived axis of Phase 2 (arrival by class sentence and allocation, rotation clock absent, accompaniment, "a placement, not a refuge"), which does not depend on the composition table.

**Three decisions to put to the developer before any rewrite:** (1) whether the 28.2% / 31.1% ruling labels or the recounted 27.6% / 30.5% table governs for Davis; (2) whether the comparison seal on nations' figures is kept on a new ground or lifted now that the table is headcount-based; (3) whether the small and regional successor rows (under 0.5%) are treated as "origin communities" in Phase 2's sense or as a tail.

---

## 7. Commands run and what could not be done

**Method.** Read in full: pass `README.md`, `Amendment_Notes_2026-10-30_...`, `00_Frame`, `01_Inherited`, `02_Spine`, `04_Phase_02` (all 1,602 lines), `04_Phase_05`, `04_Phase_09`, `05_Reconciliation`, `09_Record`, `10_Readiness_Check`, as-run and rebuilt Pre-Trip (sections C, D, O). Read in part: `04_Phase_04` (L20-40, L190-210, L255-300), `04_Phase_07` (L20-440), `04_Phase_08` (L228-270), `07_QA` (L300-345), `00.1` (grep of composition lines), and grep-located lines in Phases 3, 6, 10, `06_Differentiate`, `08_Review_Panel`, `09.5_Log`. Not read line by line: `03_Research`, `04_Phase_03`, `04_Phase_06`, `04_Phase_10`, `06_Differentiate`, `07_QA` (beyond Gate 11), `08_Review_Panel`, `09.5_Log`; their numeric and composition content was located by pattern search (section 3.5 states what that supports). `graphify` was not used.

**Representative commands** (all read-only; repo root `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD`):
- `git log --format='%h %ad %s' --date=short -- <Davis pass folder>` and `-- <spec>`; `git diff --stat d2dd2136 HEAD -- <Davis pass folder>`; `git diff d2dd2136 HEAD -- "Specs/Mirny subnet/Davis.md"`; `git diff -U0 4a59fab8 HEAD -- 00_Frame.md 00.1... 00.1a...`.
- `git show <d2dd2136|c3e31166|HEAD>:<path> | grep -n Davis` for the census, `Upper_Earth_Immigration_Composition`, `Founding_Register`, `09`, `16`, Highways, Airports, Ports, Arcanet, the three relationship files, `Extent_and_Density_Per_City`, `Inspirational-Influences`, `National_Medical_and_Care_Institutes`, Division of Industry files `README`, `04`, `08`, `10`, `11`, `13`, `14`, `15`, `17`, `18`, `19`.
- `git diff -U0 c3e31166 HEAD -- Infrastructure/Airports.md Ports.md Highways.md`; `git diff -U0 d2dd2136 HEAD -- <three relationship files> | grep -i davis`.
- For commit-by-commit spec edits: `git show <67d091af|5ee58d0e|e2dcc22d|5af08926|7ca14681|26dca3e5|4a94737a> -U0 -- <spec>`.
- Universe repo (`/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline`): `git log`/`git diff ae54b47^ HEAD -- Reference/No_National_Stereotypes.md`; `git show b1f20ff -U0`; line counts of `No_National_Stereotypes.md` and the era `Timeline.md` at four commits.
- Arithmetic (python3 -I): retention, shares, departures, density, workforce, Gate 11 table, and the 45-row table counts (rows by tier, rows under 1% / 0.5% / 0.1%, sum 100.0). Scratch copies of the pass-time and current spec were made under the session scratchpad only.
- `grep` (pattern search over the pass files, with line numbers) for every changed figure and phrase listed in section 3.

**Limits and things not done.**
- The pass files were not re-read line by line outside the files listed above; an occurrence worded differently from the searched patterns may exist (the same limit the 10-30 note states).
- Commit dates in the universe repo are not monotonic (`git rev-list --before` returned a 2026-08-24 commit for "2026-09-16"), so the pass-time version of `No_National_Stereotypes.md` was identified from the pass's own record (172 lines, matching the 172-line version at `56b4266`) and diffs were taken from `ae54b47^`.
- The methodology files (runbook, `01`-`04`, Disciplines, Run Modes) changed since the pass; their effect on the pass was not assessed.
- The Davis datasheets, Pre-Trip and ledger were not reviewed as inputs (they are derived support files, rebuilt 2026-11-03); the Pre-Trip's section O was used only as a pointer list and every entry in it was re-verified from git.
- Davis's row in `Cross_City_Culture_Differentiation_Table.md` was checked only for composition phrases, in Davis's own cells (no other city's cell was read).
- `Factions/City_Origin_Factions_Second_Interwar.md` and `Cross_City_Cultural_Patterns.md` name Davis; the pass refused the first as comparative and did not open them; they were not opened here.
- No web search, no edit to any pass file, spec, census or source.
