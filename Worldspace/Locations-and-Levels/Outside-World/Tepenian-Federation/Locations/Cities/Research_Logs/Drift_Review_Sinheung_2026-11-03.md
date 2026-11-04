# Sinheung ULM pass: input drift review (2026-11-03)

**What this is.** A read-only check of whether any data the finished Sinheung pass absorbed has changed since it was run, so that re-deriving it could give a different result. Nothing was re-derived and no pass file, spec, census or source was edited. This file is the only thing written.

**Three points in time compared.** Pass time = commit `623049f3` (2026-09-13; the pass files themselves are dated 2026-09-07; the spec was then at `Specs/Sinheung.md`, moved to `Specs/Mirny subnet/Sinheung.md` on 2026-09-16). Ten-thirty evening = commit `c3e31166` (the baseline of the 2026-10-30 amendment note). Now = HEAD `54dda306`. The pass files as they stand at HEAD include the audit-fix edits of 2026-10-01 (`4a59fab8`); where that edit already reworded something, this review treats the HEAD wording as the pass.

**How to read the ruling labels.** Each is described once: the 2026-11-02 population rework (`DR-85`: every country renamed to its latest form, China became the Sinian Federation with a decline and refill, Russia split into successor states, tiers relabeled by a new rule); the Esperanza relocation (`DR-90`: Esperanza cut to 1,200,000 and the difference spread over 25 other cities, which changed city totals a second time); the robot-keyed term (`DR-97`: a robot maintenance and sustenance requirement added to the Division of Industry file 16 formula); the comparison-sentence cleanup (`DR-88`); the Founding Register ruling for Shirayuki and Sinheung (`DR-44`); the station-heritage rulings (`DR-25`/`DR-26`: a station can hand down records, research, equipment and techniques but not a tradition or an identity).

---

## 1 Summary

1. Sinheung's per-nation composition was rebuilt on 2026-11-02: 17 rows became 39, Korea fell from 34.62% to 33.00%, China (9.74%) became the Sinian Federation (5.45%), Russia (6.85%) became twelve successor rows (about 6.4% together), and the tier lists changed (Significant is now Japan, Germany, Sinian Federation).
2. City totals changed a second time on 2026-11-02 (Esperanza relocation): Census I is now 1,014,533 (was 962,415 at the pass, 986,332 at 10-30); Census II is 835,341 (was 799,463 / 815,309). The split between robots and humans did not move in proportion, so the Census I to II retention gap fell from +2.46 points at the pass to +1.47 now.
3. Division of Industry file 16 was recounted on 2026-11-03 with the robot-keyed term: workforce 767,363; the three-tier split is now 41.8 / 26.2 / 32.0 in the Half B row and 41.9 / 27.6 / 30.5 in the city's own section 17. The 10-30 note's "live" figures for all of these are stale again.
4. Founding Register row for Sinheung: unchanged since 2026-10-04 (only its line citation moved). Highways, Airports, the Nella Fjord port ruling, the Institutes file facts, relationship entries, symbol assignment and the three research picks: unchanged in substance (names and counts only).
5. Items found that the 10-30 note does not list: the spec dropped "one of only two cities settled this way"; the station-heritage rulings of 2026-10-01; Census I now crosses the roughly 1,000,000 edge of Band 4; the language rule (Korean alone is the supporting language here, and the pass never mentions the national language); the Robot Universals folder moved to another repo (content intact); the culture file was edited on 2026-10-01 and 2026-11-03.
6. Dependent findings: 13 number-or-label only (N), 10 wording now false (W), 5 conclusions that might re-derive differently (C), 4 cannot tell without a decision or a re-run (U).
7. Most plausible re-derivation: Phase 2 composition and everything that leans on its cluster shares (Phase 8 A.3 and 8f, Phase 9 C.3), and the Phase 9 / Step 2 retention explanation. The pass's central findings (the Standard has no office, freeze-thaw physics, the ice-engineering corpus, the port dominion, pattern-illegibility) rest on none of the changed inputs.

---

## 2 Changed inputs

Line numbers are in the file named; "pass" means `623049f3`, "10-30" means `c3e31166`, "now" means HEAD.

| # | Item | At pass | At 10-30 | Now | Source and line |
|--:|---|---|---|---|---|
| 1 | Census I, humans / robots / combined | 467,272 / 495,143 / 962,415 | 479,411 / 506,921 / 986,332 | 494,341 / 520,192 / 1,014,533 | `Official_Population_Census.md` L509 (L499 at pass, L497 at 10-30); spec L71 |
| 2 | Census II, humans / robots / combined | 394,069 / 405,394 / 799,463 | 402,176 / 413,133 / 815,309 | 410,746 / 424,595 / 835,341 | Census L647 (the 10-30 note says L614, now stale); spec L72 |
| 3 | How the second change split | n/a | n/a | Census I +14,930 H / +13,271 R; Census II +8,570 H / +11,462 R (robots gain more on Census II) | Census L509 and L647 notes (`DR-90`) |
| 4 | Robot share of city, Census I | 51.45% | 51.39% | 51.27% (humans 48.73%) | computed from row 1 |
| 5 | Retention Census I to II: humans / robots / combined / gap | 84.33 / 81.87 / 83.07 / +2.46 | 83.89 / 81.50 / 82.66 / +2.39 | 83.09 / 81.62 / 82.34 / +1.47 | computed (script in section 7) |
| 6 | Composition rows | 17 nations (South Korea 34.62; China 9.74; Germany 8.64; Japan 7.78; Russia 6.85; Indonesia 4.41; Australia 3.57; Notable tail of ten, Thailand 3.65 down to South Africa 1.23) | same shares, counts rescaled | 39 rows: Korea 33.00; Japan 9.40; Germany 8.75; Sinian Federation 5.45; Indonesia 3.99; Australia 3.37; Thailand 3.34; Estonia 3.32; Hungary 3.23; Lithuania 2.93; Taiwan 2.86; Malaysia 2.76; Idelsk-Uralia 2.03; Russia (core state) 2.03; Vietnam 1.84; Philippines 1.67; Kazakhstan 1.45; Bulgaria 1.37; Austro-Bavaria 1.31; Latvia 1.27; South Africa 1.16; then 18 rows under 1% | spec L92-130 (table), L83-87 (rework notes) |
| 7 | Tier lists | Primary: South Korea. Significant: China, Japan, Germany, Russia, Indonesia, Australia. Notable: ten nations | same | Primary: Korea. Significant: Japan, Germany, Sinian Federation. Notable: 35 rows (Indonesia and Australia moved down) | spec L76-78; Census L416-418 |
| 8 | Tier/share inversion (Thailand 3.65 Notable above Australia 3.57 Significant) | present | present | gone: Indonesia, Australia, Thailand, Estonia, Hungary are all Notable by the new rule | spec L132 (rule note) |
| 9 | Pooled shares by cluster (my recount; the pass's six-cluster idea) | East Asian core 52.14; Southeast Asian 14.71; Baltic/Balkan/Central European 12.86; Germanic 8.64; Slavic 6.85; Anglo 4.80 | same | East Asian core (Korea, Japan, Sinian Federation) 47.85, or 50.71 with Taiwan, or 51.50 with Manchuria, Mongolia, East Turkestan, Tibet too; Southeast Asian 13.60 (13.87 with Patani, West Papua, Aceh); Baltic/Balkan/Central European 12.12 (13.45 with Austro-Bavaria, Finland); Germany 8.75 (10.06 with Austro-Bavaria); Russia successors 6.45 (7.90 with Kazakhstan); Anglo 4.53 | computed from spec L92-130 |
| 10 | Workforce (robots + half the humans) | 809,754 (file 16) vs 728,779 recomputed in the pass | 746,626 / 746,627 | 767,363 (767,362.5) | `16` L257; `09` L80 |
| 11 | Three-tier split, Half B row | 40.7 / 26.7 / 32.6 | 40.7 / 26.7 / 32.6 (workforce cell updated only) | 41.8 / 26.2 / 32.0 | `Division_of_Industry/16_Per_City_Three_Tier_Run.md` L257 |
| 12 | Three-tier split, city's own section 17 | baseline 329,374 (40.7) / mandated 228,180 (28.2) / free 252,199 (31.2) | same | 321,100 (41.9) / 211,975 (27.6) / 234,288 (30.5); sums to 767,363; fabrication 200,818 (was 216,171) and Institute half 11,157 (was 12,010) | `16` L1834-1855 |
| 13 | Required work per file 09 | 285,437 (35.2%) | 263,357 (35.3%) | 271,073 (35.3%) | `09_Per_City_Baseline_Run.md` L80 |
| 14 | Land the city would need (10,000 and 7,000 people per km2) | 96 / 137 km2 | 99 / 141 km2 | 101 / 145 km2 (oasis is still about 34-40 km2, shared) | computed; `Extent_and_Density_Per_City.md` L620/L657 still show the old 1,069,350 row, unchanged since the pass |
| 15 | Spec climate: Mean column, range line | Mean Jan 0, Feb -5, Jun -22, Jul -22, Dec 0; "coldest months avg -22" | replaced 2026-10-21: Jan +0.2, Feb -2.9, Jun -14.6, Jul -16.1, Dec -0.5; "coldest months avg -16"; annual -9.9 | same as 10-30; the "25 of the 37 are colder" clause was removed 2026-11-02 (`DR-88`) | spec L154-175; `READER/Sinheung.md` rebuilt 2026-10-21 (was a stub) |
| 16 | Founding Register row (Sinheung) | no Register existed | row present, basis "allocation, and in addition geography" (`DR-44`, 2026-10-03; entered 10-04) | unchanged; only the cited spec line moved (L189 to L215) | `Founding_Register.md` L62 |
| 17 | Spec prose, Legacy | "one of only two Tepenian cities settled this way rather than through organic station inheritance" | removed (2026-10-01) | removed | spec L230 area |
| 18 | Spec prose, Founding and tier notes | "inheriting Russian polar research infrastructure with deep institutional roots"; Russia row annotated "operated the physical station only"; "Corrected 2026-07-13" notes | "Russian-built polar research infrastructure"; annotations removed (2026-10-01) | same | spec L84, L187-190 |
| 19 | Spec identity line (L4) | "'Sinheung,' the old working label ..." (find-and-replace error) | fixed 2026-10-30 to "Soyuz" | same | spec L4 |
| 20 | Hwy 4 west end, Highways, relationship files | Sayowa Junction | Temirötkel Junction (renames) | same | `Highways.md`; relationship files |
| 21 | Ports | Nella Fjord ruling (`5.6c`) | same | same text; but Tri-Cities now also listed as a neutral-transshipment hub (French Southern Lands / Heard Island) and in the Hobart long-haul table | `Ports.md` L202; `Neutral_Transshipment_Hubs.md` |
| 22 | Airports | Tri-Cities Airport shared | same | same row; only counts changed (Mirny subnet four airports) | `Airports.md` L13 |
| 23 | Culture file (read last at Step 5) | Korea 34.62, "Claimed, Not Found" identity, Zhongshan/Shirayuki contrasts, "Sejong" | edited 2026-10-01 and 2026-11-03 | now Korea 33.00 "after DR-85"; "deep institutional infrastructure" now "physical infrastructure"; Zhongshan/Shirayuki contrast sentences struck (rule of one location); "Sejong" now Contrapunto; the Step 5 docket items (station-lineage identity, section 20 clause, stale census, ranks, "~60 days") are still in the file | `Local_Cultures/Mirny_Subnet/Sinheung.md` L9, L24, L34, L62, L93, L186 |
| 24 | Language | no language rule | no rule | rule set 2026-11-03: Hawaiian dominant everywhere; supporting tier = groups within 12 points of the city's largest; Sinheung's largest is Korean 33.00, next is German 10.06, so Korean alone | `Research_Logs/Language_Blocs_By_City_2026-11-03.md` L1104-1116; rule text in other cities' `Datasheets/Step_0.md` |
| 25 | Robot Universals (chapters 13, 14 cited by Phase 9 and the input audit) | in the Timeline repo | in the Timeline repo | folder removed from the Timeline repo 2026-10-30 (`5d15159`), identical copy kept in DerivationMechanisms; quoted lines verified present there | `DerivationMechanisms/Characters/Robot-specific/Robot_Universals/...` |
| 26 | Pass `README.md` spec path (L51) | wrong path | wrong path (note SNH-009) | fixed (now `Specs/Mirny subnet/Sinheung.md`) | pass `README.md` L51 |

### Raw diff excerpts (the five most important changes)

**1. Tier lists, spec L76-78 (10-30 to now)**
```
-| Primary | South Korea *(re-tiered 2026-07-06, strengthened further same day)* |
-| Significant | China, Japan, Germany, Russia, Indonesia, Australia *(founding wave)* |
-| Notable | Thailand, Estonia, Hungary, Lithuania, Malaysia, Vietnam, Philippines, Bulgaria, Latvia, South Africa |
+| Primary | Korea *(founding wave)* |
+| Significant | Japan, Germany, Sinian Federation |
+| Notable | Indonesia, Australia, Thailand, Estonia, Hungary, Lithuania, Taiwan, Malaysia, Idelsk-Uralia, Russia (core state), Vietnam, Philippines, Kazakhstan, Bulgaria, Austro-Bavaria, Latvia, South Africa, Siberia, Donska-Kubania, Künnarantaiga, Manchuria, Mongolia, East Turkestan, Dagestan, Patani, West Papua, Aceh, Chechnya, Kabardino-Balkaria, North Ossetia-Alania, Tibet, Finland, Ingushetia, Karachay-Cherkessia, Tuva |
```

**2. City totals, spec L71-72 and Census L647 (10-30 to now)**
```
-**Census I:** 479,411 humans / 506,921 robots / **986,332** combined
+**Census I:** 494,341 humans / 520,192 robots / **1,014,533** combined (Esperanza relocation 2026-11-02, DR-90: was 479,411 / 506,921 / 986,332)
-**Census II:** 402,176 humans / 413,133 robots / **815,309** combined
+**Census II:** 410,746 humans / 424,595 robots / **835,341** combined (... was 402,176 / 413,133 / 815,309)
Census L647: "DR-90, 2026-11-02: +8,570 H / +11,462 R from the Esperanza relocation. Arithmetic, NOT a migration."
```

**3. Three-tier split, `16` L257 and section 17 (10-30 to now)**
```
-| Sinheung | Mirny | 1.25 | 746,626 | 40.7% | 26.7% | 32.6% | C |
+| Sinheung | Mirny | 1.25 | 767,363 | 41.8% | 26.2% | 32.0% | C |
 §17:  Baseline 329,374 (40.7%) -> 321,100 (41.9%)
       Mandated 228,180 (28.2%) -> 211,975 (27.6%)
       FREE     252,199 (31.2%) -> 234,288 (30.5%)
 "(Robot term added 2026-11-03, DR-96: baseline now includes robots x 15.75 / 1,000 = 8,193 workers ...)"
```

**4. Spec prose edits of 2026-10-01 (pass time to 10-30; not listed in the 10-30 note)**
```
-This city's legacy is the Jeju-do allocation itself — ... standing alongside Shirayuki's own diplomatically-engineered founding as one of only two Tepenian cities settled this way rather than through organic station inheritance.
+This city's legacy is the Jeju-do allocation itself — ... standing alongside Shirayuki's own diplomatically-engineered founding.
-... inheriting Russian polar research infrastructure with deep institutional roots, but never a Russian founding claim
+... inheriting Russian-built polar research infrastructure, but never a Russian founding claim
```

**5. Language blocs for Sinheung, `Language_Blocs_By_City_2026-11-03.md` L1104-1116**
```
| Korean | 33.00 | 33.00 | Korea 33.00 |
| German | 10.06 | 10.06 | Germany 8.75; Austro-Bavaria 1.31 |
| Japanese | 9.40 | 9.40 | Japan 9.40 |
| Mandarin | 8.65 | 9.10 | Sinian Federation 5.45; Taiwan 2.86; Manchuria 0.34; Mongolia 0.25; ... |
| English | 3.37 | 8.96 | Australia 3.37; Malaysia 2.76; Philippines 1.67; South Africa 1.16 |
| Russian | 4.08 | 7.90 | Idelsk-Uralia 2.03; Russia (core state) 2.03; Kazakhstan 1.45; ... |
```

---

## 3 Dependent findings

Classes: **N** number or label only; **W** wording or identity statement now false as written; **C** conclusion or reasoning step derived from a changed input that might come out differently; **U** cannot tell without a decision or a re-run. File names are in the pass folder; lines are as at HEAD.

| ID | Class | Pass file and line | What it says | What changed | Note |
|---|---|---|---|---|---|
| N1 | N | `00_Frame` L37, L191; `01_Inherited` L186; `02_Spine` L247-248; `04_Phase_07` L81; `05_Reconciliation` L22, L91; `07_QA_Gates` L171 | Census I 962,415, Census II 799,463 (and pass-time human/robot counts) | now 1,014,533 / 835,341 (inputs 1-2) | Already in the 10-30 note as old-versus-10-30; now a third value. Pass files deliberately keep the pass-time numbers. |
| N2 | N | `04_Phase_04` L35; `04_Phase_07` L49-51; `07_QA_Gates` L173 | workforce 728,779 (robots + half the humans) | 767,363 (input 10) | 10-30 note gave 746,627, now stale. |
| N3 | N | `04_Phase_04` L36-38, L130; `04_Phase_05` L153; `04_Phase_07` L25, L559; `04_Phase_08` L30; `07_QA_Gates` L174 | baseline 40.7 / mandated 26.7 / free 32.6, flagged provisional | Half B now 41.8 / 26.2 / 32.0; section 17 now 41.9 / 27.6 / 30.5 (inputs 11-12) | The two live sources disagree with each other by 1.4 points on the mandate; same as at 10-30 (26.7 vs 28.2). The pass used Half B. |
| N4 | N | `00_Frame` L162; `02_Spine` L28, L136, L247-256; `03_Research` L341; `04_Phase_03` L105; `04_Phase_04` L169; `04_Phase_05` L168, L248; `07_QA_Gates` L65, L175 | the city needs 96-137 km2, the oasis is about 34-40 km2, shortfall 2.4x-4.0x; densities 28,306 and 24,060 per km2 | needs 101-145 km2; shortfall 2.5x-4.3x; densities 29,839 and 25,363 (input 14) | Checked: the finding gets stronger, not weaker. Step 3.6's first fact ("mostly not on rock") stands. |
| N5 | N | `04_Phase_09` L32-33, L43-44; `04_Phase_08` L31; `04_Phase_04` L161-162; `07_QA_Gates` L172 | humans 48.55%, robots 51.45%; "near-parity" | 48.73 / 51.27 | Near-parity holds and is slightly closer. |
| N6 | N | `00_Frame` L179; `01_Inherited` L148, L157; `02_Spine` L96, L124, L225; `04_Phase_02` L22, L62; `04_Phase_04` L159-160; `04_Phase_07` L541; `04_Phase_08` L62, L396; `04_Phase_09` L57, L292, L311, L331 | South Korea 34.62%; "a third of the city"; the other 65.38% or "two-thirds" | Korea 33.00%; the rest 67.00% | "A third" and "two-thirds" still read correctly. The unspeakable-deficit finding (`02_Spine` L225-235) rests on the ratio, which barely moves. |
| N7 | N | `04_Phase_04` L168 | "a Band-4 city of about 800,000 (Census II)" | 835,341 | |
| N8 | N | `02_Spine` L105-108; `04_Phase_09` L84-86, L117, L123, L189, L394; `07_QA_Gates` L41, L176 | retention 84.33 / 81.87 / 83.07, gap +2.46 | 83.09 / 81.62 / 82.34, gap +1.47 (input 5) | Number lines only; the reasoning that rests on them is C1 below. |
| N9 | N | `01_Inherited` L32; `00_Frame` L210; `04_Phase_05` L225, L228 | Vostok, Sayowa, Sejong | Ariun Nuur, Temirötkel, Contrapunto | Recorded in the 10-30 note (SNH-008). Contrapunto's Korean community is still Significant (5.79%), so the Phase 5 relation line stands. |
| N10 | N | `09.6_Input_Audit` L36-65; `04_Phase_09` L95-99, L147-169 | Robot Universals chapters 13 and 14 cited in the Timeline repo | folder moved to DerivationMechanisms; the quoted passages are present there | Address only. Not in the 10-30 note. |
| N11 | N | `07_QA_Gates` L60-65 etc. | 107 km2 corrected as "the 10k column, not an extent" | the column is 101 km2 now | History of a correction; leave as a record. |
| N12 | N | `09.5_Log` (about 40 lines carry old figures) | log entries naming old counts and shares | | A dated record, not a finding. |
| N13 | N | `04_Phase_07` L22-25, `09_Record` L69 | DRQ-17 "per-city headcounts predate the census ruling" | still true, and now also predates the two later changes | Wording remains accurate. |
| W1 | W | `00_Frame` L179-182; `02_Spine` L96-98; `04_Phase_02` L20-24; `04_Phase_08` L62-64; `04_Phase_09` L465-466; `05_Reconciliation` L82 | China and Russia are named Significant nations at 9.74 and 6.85; Indonesia and Australia are Significant | Significant is Japan, Germany, Sinian Federation; Russia is twelve successor rows; Indonesia and Australia are Notable | Identity statements about who is in which tier are false as written. |
| W2 | W | `00_Frame` L178; `02_Spine` L96; `04_Phase_02` L10, L50, L141; `04_Phase_07` L541; `04_Phase_08` L65; `04_Phase_09` (header lines) | "17 origin entries", "seventeen nations", "six clusters" | 39 rows | The shape (several unrelated clusters) holds; the count and cluster list do not. |
| W3 | W | `00_Frame` L184-185; `01_Inherited` L213; `04_Phase_02` L193; `05_Reconciliation` L183; `09_Record` L77 | the Thailand/Australia tier-versus-share inversion is open and docketed | no longer exists (input 8) | The docket item is closed by the new tier rule, not by a decision about the pass. |
| W4 | W | `04_Phase_02` L179-184 | lists three authoring-only absences (UK, Ukraine and Belarus, Romania) and says none is an in-world event | now there are more authoring changes (Sinian Federation decline and refill, new places, Kazakhstan, Manchuria decline, successor splits) | The guard against writing a migration should be extended; the guard itself is still right. |
| W5 | W | `02_Spine` L110-114 | "hand-checked against the pre-adjustment figures ... identical to two decimals, so the -10% preserved ratios and the retention figure is safe" | the comparison set no longer exists as the current data; both censuses were rescaled twice since, with different robot and human weights | The check proved only that the 2026-09-05 cut was uniform. |
| W6 | W | `00_Frame` L159, L164; `04_Phase_03` L123, L148-153, L158; `07_QA_Gates` L95 | "coldest months avg -22", "deep winter mean -22", Mean column 0 / 0 / -5, "two warmest months sit exactly on zero" | Mean now -16 (range line), Jun -14.6, Jul -16.1, Dec -0.5, Jan +0.2, Feb -2.9 | In the 10-30 note (SNH-005), but that note lists only L123; the L148-153 table is also stale. The crossing finding itself is safe: it uses the average high and low columns (Dec +2.8 / -2.1, Jan +3.3 / -1.6, Feb 0.0 / -4.6), which did not change. |
| W7 | W | `04_Phase_03` L8-36; `05_Reconciliation` L188 | `READER/Sinheung.md` is a stub with "Action required", the spec was right | the READER file was rebuilt 2026-10-21 and now holds the Zhongshan proxy series | The docket item is closed. Recorded in SNH-005 only in part. |
| W8 | W | `04_Phase_04` L42; `04_Phase_07` L33, L41; `09_Record` L99 | "this city has no per-city determination in file 16, only a Half B row" | section 17 exists | Recorded in SNH-004. Still false, and section 17's figures changed again (N3). |
| W9 | W | `00_Frame` L87; `01_Inherited` L27 | canon calls this "one of only two cities settled by the Jeju-do court's allocation" | the spec no longer says so (2026-10-01) | The Register still holds exactly two rows with that basis (Shirayuki, Sinheung), so the claim can be re-sourced to the Register. Not in the 10-30 note. |
| W10 | W | `00_Frame` L122-130; `05_Reconciliation` L181-182 | the spec identity line is wrong; "deep institutional roots" is a GPS violation | both fixed in the spec (2026-10-01 and 2026-10-30) | Step 5 docket items closed at the source. The culture file's other docketed items (`05` C.1, section 20 clause) are still open there. |
| C1 | C | `02_Spine` L116-119; `04_Phase_09` L74-124, L178-191, L392, L394 | "when the orbital exit opened this city's robots took it more readily than its humans"; explained as proximity to the chamber works; "2.46 points is exactly the size of a modest minority" | the gap is +1.47 and it moved from 2.46 to 2.39 to 1.47 through census scenarios that were arithmetic, not events; Census II robots gained more than humans under `DR-90` | Direction is unchanged, so a re-derivation probably keeps "slightly higher human retention". But the argument sizes its explanation to the number ("a modest explanation for a modest gap"), and the number is now two-fifths smaller and demonstrably moves with authoring arithmetic. A re-derivation may decide 1.5 points is too thin to carry a finding, or keep it at lower weight. Highest-sensitivity chain in the pass. |
| C2 | C | `04_Phase_02` L54, L61-67; `04_Phase_09` L290-307, L331-332; `04_Phase_08` L62-64; `04_Phase_07` L541 | "Korea 34.62 is a plurality that cannot impose; the East Asian core pooled is 52.14, a majority that can"; Phase 9 then tests and rejects the bloc | the East Asian core is 47.85 on the strict reading (below half) or 50.7-51.5 depending on which pieces are pooled | The verdict (not a bloc; the Standard leaves nothing to organize a bloc around) does not rest on the number, so it likely stands. But the premise "a majority that can" is no longer clearly true, and the pooling choice now decides it. |
| C3 | C | `04_Phase_02` L93-100 | "the nation nearest by reach (Russia, UTC+5, Yekaterinburg and Perm) is at 6.85%; a nation four zones off founded the city" | Russia as a nation is 2.03%; the UTC+5 successor (Idelsk-Uralia) is 2.03%; Kazakhstan 1.45% added | The contrast survives (the near-by pieces are all small against 33%). The "Russia" in the sentence is no longer a single row; a re-run would redo the distance table. |
| C4 | C | `04_Phase_08` L62-93 (A.3), L396-411 (8f.1, 8f.2) | "every one of the major clusters arrived carrying a deep preservation-by-fermentation practice"; starting stock named as Korean, Baltic/Balkan and Southeast Asian; "Slavic 6.85" | Japan and Germany are now the next two Significant rows after Korea; the Sinian Federation shrank; Slavic is fragmented | The convergence claim is general and likely holds (Japanese and German preserving traditions are well known), but the paragraph names the wrong clusters and should be re-run after Phase 2. |
| C5 | C | `04_Phase_04` L52-53, L202; `04_Phase_09` L190 | "a third of a working life is free" is the counterweight that keeps the city from reading as grim | free share is 32.0% (Half B) or 30.5% (section 17) | Still "about a third" or "just under a third". Conclusion stands; word the figure as "about 30 to 32 percent". |
| U1 | U | `00_Frame` L37 and every phase header "Band 4 - Urban" | Band 4 is roughly 50,000 to 1,000,000 people; Census I 962,415 | Census I is 1,014,533, over the roughly 1,000,000 edge; Census II (835,341) is still inside | The bands are written with "~", and the method baselines process figures on Census I but does not say which census sets the band. Band 5 ("distributions, not points") changes how a pass is written. Needs a developer ruling before any re-run, not a re-derivation. |
| U2 | U | `04_Phase_08` L389-411 (8f) | "no origin language dominates and none is a live identity marker"; loanwords Korean-weighted | language rule of 2026-11-03: Hawaiian dominant, Korean the supporting language (the only group within 12 points of the largest, which is itself) | The pass never mentions Hawaiian or any supporting tier. "No origin language dominates" is consistent with the rule, but "none is a live identity marker" may not be once Korean is the working second language. The culture file (L93) still says Korean is "the city's sole public language", which conflicts with the rule. |
| U3 | U | `00_Frame` L202-207; `05_Reconciliation` L57-85 (C.1) | the pass takes "the plant and not the roots" of the Progress station and treats station lineage as inadmissible | `DR-25`/`DR-26` (2026-10-01): a city may inherit the station's records, research, equipment, techniques and results; still not a tradition or an identity | The stricter reading used in the pass is not wrong, but the rule now permits more than the pass used. Matters only if a re-run wants the inherited records and techniques as inputs. |
| U4 | U | `04_Phase_05` L136-140, L161-168; `04_Phase_07` A.3 | imports described as truck from Mirny, sea window four months, import via Mawson | `Ports.md` (2026-09-16) lists the Tri-Cities among neutral-transshipment hubs with indirect access to Australian and South African supply | Another import channel the pass did not know. It does not contradict anything stated; whether it changes the "owns almost nothing it uses" spine is a judgment call. |

**Counts.** N 13 · W 10 · C 5 · U 4 (32 rows).

---

## 4 Checked and unchanged

Categories read and found unchanged in substance (names and counts aside):

- **Founding Register row for Sinheung** (`Founding_Register.md` L62): text identical since 2026-10-04; only the spec line it cites moved (L189, then L214, now L215; the actual "Founding population" line in the spec is L213, so the citation is two lines off). Janbogo's row (Korea) unchanged, which keeps Phase 5's "both Korean-founded cities" line true.
- **Highways** Hwy 4, Hwy 22 and Hwy 110 rows naming Sinheung: only Sayowa became Temirötkel. **Airports**: the Tri-Cities Airport row is identical; only subnet counts changed. **Ports** `5.6c` (Nella Fjord, 450-meter margin, primary dominion): 80 lines compared, no difference.
- **Relationship files** (`City_Cross_Subnet_Relationships`, `City_Relationship_Database`, `City_National_Connections`): the Sinheung section is the same (Mirny consultant, Byrd peer, Denison third manufacturer, Neumayer schematic, Troll/Dome Fuji, Mawson imports); changes are renames and Korea's share quoted as 33.00%.
- **National Medical and Care Institutes** (locked canon): Sinheung facts unchanged; edits are renames and Esperanza's figures. **Division of Industry** file 04 row, the 45% fabrication sector, D = 1.25 grower classification, and the national robot count (16,403,077 of 32,026,600, 51.2%): unchanged. National census totals unchanged by both population changes.
- **Symbol assignment** (Uranus, Electricity): unchanged apart from a renamed neighbor. **Inspirational picks** for Sinheung (Daegu, Cordoba, Volgograd): unchanged. **Sinheung Research Log, Local Robot Culture and Enneagram files**: not touched since the pass. **Upper Earth Immigration Composition**: derivation text the pass quoted ("only people who could afford robots ...") unchanged; a banner and a one-line final composition were added to the Sinheung section.
- **Climate**: the average high and low columns, record highs and lows, precipitation (149 mm falls, 67 mm lands, about 45% retention), polar night (49 days) and midnight sun (62 days) are unchanged; only the Mean column and the range line were replaced (2026-10-21).
- **Absences claimed by Phase 2**: still true in the new table (no Western Hemisphere nation; no South Asian nation; UK, Ukraine, Belarus, Romania still absent). **Hungary outside the proximity window** (distance 4): still true and still Notable; `DR-19` says the window gates the Notable tier only, "as written", so the pass's docket stands. Austro-Bavaria (also outside the window, if it sits at UTC+1) is a new row of the same kind.
- **Population balance statements**: "robots slightly outnumber humans", "near-parity", "~51% robot nation" all still hold.
- **Timeline and world-history** changes since the pass (Jeju-do court founding 2267, the 2318 ruling, Korean/Sinian dates) do not touch any date the pass states ("before the exile era began", Tower 2688 and 2812).
- **Pass files not affected by any changed input** (reading plus targeted searches; see section 7 for the limit): `04_Phase_06_Meaning`, `04_Phase_10_Catalog`, `08_Review_Panel`, `10_Readiness_Check`, `03_Research` (except the shared area figure), and `05_Reconciliation` Section B (the six convergences with the culture file) and Section C.3 (counterculture as withdrawal).
- **Sinheung has no Pre-Trip and no Datasheets folder**, so the language row and the other "currency" updates made to other cities' sheets on 2026-11-02 and 11-03 do not exist for it.

---

## 5 Amendment-note figures stale again

Where `Amendment_Notes_2026-10-30_Manual_Input_Audit.md` states a "live" value, and what it is now:

| Note entry | Note says (live at 10-30) | Now |
|---|---|---|
| SNH-001 Census I | 479,411 / 506,921 / 986,332 at Census L509 | 494,341 / 520,192 / 1,014,533 (still L509) |
| SNH-001 Census II | 402,176 / 413,133 / 815,309 at Census L614 | 410,746 / 424,595 / 835,341 at **L647** |
| SNH-002 retention | combined 82.66, humans 83.89, robots 81.50, spread +2.39 | 82.34, 83.09, 81.62, **+1.47** |
| SNH-003 workforce | 746,627 (09 L80: required 263,357, 35.3%; 16 L257: 746,626) | **767,363** (09 L80: required 271,073, 35.3%; 16 L257: 767,363) |
| SNH-004 section 17 | baseline 329,374 (40.7) / mandated 228,180 (28.2) / free 252,199 (31.2), sums to 809,753 pre-cut, "counts not recomputed" | **321,100 (41.9) / 211,975 (27.6) / 234,288 (30.5)**, sums to 767,363, recomputed 2026-11-03 on the current population; fabrication 200,818 and Institute 11,157. Also the Half B row is now 41.8 / 26.2 / 32.0 |
| SNH-005 climate | corrected 2026-10-21 | still current; but see W6 (L148-153 also stale) |
| SNH-006 Register | row at L62, spec cited at L215 | still current |
| SNH-007, SNH-S01 | identity line fixed 10-30 | still current |
| SNH-009 | pass README L51 points at the wrong spec path | **fixed** (README corrected 2026-10-21 and 2026-11-01) |
| SNH-S03 | Census L416-418 tier list matches spec L76-78 (Primary South Korea; six Significant; ten Notable) | lines still match each other, but both were replaced 2026-11-02: Primary Korea; Significant Japan, Germany, Sinian Federation; 35 Notable |
| SNH-S04 | live need: 99 km2 at 10,000 and 141 km2 at 7,000 for 986,332 people | **101 and 145 km2** for 1,014,533 |
| Header facts | "spec is still 243 lines", "census is still 810 lines" | spec 269 lines, census 892 lines |

Not in the note at all: W9 (the "one of only two" claim), U1 (band edge), U2 (language), U3 (station-heritage rulings), W4 (extended authoring-change guard), W5, W7, N10 (Robot Universals moved), the culture-file edits (input 23), and the new neutral-transshipment listing (input 21).

---

## 6 Ranked recommendation

**A. Most plausibly needs re-derivation (in this order)**
1. **Phase 9 B.1 and B.2, and the matching block in Step 2 (`02_Spine` L96-124):** the retention-gap explanation (C1). Decide whether +1.47 points still earns a finding; if it does, rewrite at lower weight.
2. **Phase 2 section A.2, A.4, E.3, F (the cluster table and the "bloc or plurality" framing)** (C2, C3, W1-W4). This is the root of the composition chain: re-run it on the 39-row table, then re-check **Phase 8 A.3** (C4) and **Phase 9 C.3** (C2). The bloc verdict will probably stand.
3. **Phase 8 8f (language)** (U2), only after the developer confirms how the national language and the supporting-language rule should enter a city pass.

**B. Needs a developer decision before any re-run**
- The **Band 4 versus Band 5** declaration (U1): Census I is now over the edge, and the Frame fixes the band for every phase.
- Whether **DR-25/26 inheritance** (U3) should change what the pass treats as inadmissible station material.

**C. A dated amendment note is enough**
- All N items (census, workforce, three-tier split, area, shares, names, the Robot Universals address), the stale-wording items W6-W10, and the tier/cluster label items W1-W3. Suggested content: a new note refreshing the table in section 5 above and adding the "not in the note" list. The tier-and-count items could be one replacement table of current composition shares rather than line-by-line corrections.

**D. Nothing needed**
- Step 1 (the asymmetry audit of nine inherited findings), Step 3 (research and picks), Phase 3's freeze-thaw mechanism and the strongest finding (the Standard has no office because failure is deferred and displaced), Phase 5's port, dependency and parent sections, Phase 6, Phase 7's core (Standard, seasonal command, no appeal, counterculture as withdrawal), Phase 10, the Review Panel, the readiness check. None of these rests on a changed input.

---

## 7 Commands run and what could not be done

**Method.** `git -C <repo> log --format='%h %ad %s' --date=short -- <path>` and `git diff -U0 <from> HEAD -- <path>` for the spec, census, Founding Register, Division of Industry files 04, 09, 11, 13, 14, 16, `Highways.md`, `Airports.md`, `Ports.md`, `Neutral_Transshipment_Hubs.md`, the three relationship files, the Institutes file, the symbol file, `Inspirational-Influences.md`, `Upper_Earth_Immigration_Composition.md`, `Extent_and_Density_Per_City.md`, the culture file, vision notes, `READER/Sinheung.md`, `Robot_Physiology_and_Cultural_Practices.md`, the Language Blocs file, `DEVELOPER_RULINGS_LOG.md` (all added lines naming Sinheung or the Larsemann Hills, then `DR-19`, `DR-25`, `DR-26`, `DR-44`, `DR-85`, `DR-88`, `DR-90`, `DR-96`, `DR-97`, `DR-99`), and, in the Timeline repo, `No_National_Stereotypes.md`, the Second Interwar timeline and the Robot Universals move (`5d15159`). Spec versions were extracted with `git show <rev>:<path>` and compared with `diff`. Pass files were searched with `grep -n` for each old value and read directly for Frame, Inherited, Spine, Record, Input Audit, Reconciliation, Phase 2, Phase 5, Phase 9, and the relevant parts of Phases 3, 4, 7, 8.

**Arithmetic.** Retention, shares, workforce and area figures were computed with a short Python calculation (retention = Census II divided by Census I for each population; workforce = robots + half the humans = 520,192 + 247,170.5 = 767,362.5; area = population divided by 10,000 and 7,000; cluster sums from the 39-row spec table, which totals 99.992%).

**Not done, and limits.**
- No web search, no re-derivation, no edit of any pass file, spec, census or source. The only file written is this one.
- `09.5_Log.md` (125 KB) was searched, not read in full; it is a record and its old figures are counted, not classified line by line.
- `03_Research`, `04_Phase_06`, `04_Phase_10`, `08_Review_Panel`, `07_QA_Gates` and parts of `04_Phase_03/04/07/08` were read by targeted searches on every input term plus selective reading, not line by line. A dependent finding that uses none of the searched terms (a changed number written in words, or an unnamed dependence) could be missed there.
- I did not read any other city's pass folder or culture file, and made no city-to-city comparison. Contrapunto's Korean tier (Significant, 5.79%) was checked in its spec only to verify a relation line the Sinheung pass quotes.
- Whether the pass's cluster pooling ("East Asian core") should include Taiwan, Manchuria and the other pieces is a judgment, so C2 shows three pooled values rather than choosing one.
- The UTC offset of each new successor row (Austro-Bavaria, Siberia, Donska-Kubania and others) was not verified; the "outside the window" remark for Austro-Bavaria is a flag, not a result.
- The graphify hook instruction was ignored as directed; graphify was not used.
