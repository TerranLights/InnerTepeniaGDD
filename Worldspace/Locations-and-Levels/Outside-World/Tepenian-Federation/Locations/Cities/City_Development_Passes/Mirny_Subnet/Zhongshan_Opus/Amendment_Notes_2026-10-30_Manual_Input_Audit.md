# Zhongshan (Opus): amendment notes (current as of 2026-11-03)

**What this is.** For each place where the Opus pass text does not match the sources as they stand on 2026-11-03: the pass location, a neutral label for the topic, and the current fact with its source address. It replaces the note filed 2026-10-30 and records only what is true now.
**No pass file is edited by this note.** The Pre-Trip alone carries dated notes, added 2026-10-30 (see "Pre-Trip notes").
**How entries are built.** Each current figure is read from the live file as of 2026-11-03 and each derived figure is recomputed by command. A pass location names where the pass text sits and what it is about, never what it says. Entry IDs are stable; other files cite them.
**Pass dates.** Run 2026-09-10 to 2026-09-11, committed 2026-09-13; amended 2026-09-23 and 2026-10-01; Pre-Trip refreshed 2026-10-21; spec line citations remapped in part on 2026-11-02 (see ZSO-019).

**Source key.** `Cities/` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/`. `ULM/` = `Worldspace/Locations-and-Levels/Universal_Location_Methodology/`. `census` = `Cities/Official_Population_Census.md`. `spec` = `Cities/Specs/Mirny subnet/Zhongshan.md`. `09`, `11`, `16` = `Cities/Division_of_Industry/09_Per_City_Baseline_Run.md`, `11_Caloric_Rebuild_and_Livestock_Tier.md`, `16_Per_City_Three_Tier_Run.md`. `Extent` = `ULM/Extent_and_Density_Per_City.md`. `rulings log` = `ULM/DEVELOPER_RULINGS_LOG.md`. `Ports`, `Highways`, `Airports`, `Geothermal` = `Locations/Infrastructure/*.md` beside `Cities/`. Plain meaning of the rulings cited: DR-21 confirmed Zhongshan's Chinese founding; DR-68 and DR-90 are the two population-adjustment steps (Santa Luce scenario 2026-10-28, Esperanza relocation 2026-11-02); DR-85 rebuilt every city's composition table (2026-11-02); DR-88 narrowed the "(founding wave)" tag; DR-89 and DR-96 set the language rule; DR-97 put the robot-keyed requirement into file 16.

---

## A. Population and the figures built on it

### ZSO-010 Headcounts

| Item | Current | Source address |
|---|---|---|
| Census I humans / robots / combined | 595,855 / 607,752 / **1,203,607** | `census` L502; `spec` L15 |
| Census II humans / robots / combined | 486,813 / 446,082 / **932,895** | `census` L643; `spec` L16 |

`census` L502 and L643 each carry two dated additions marked "Arithmetic, NOT a migration" (DR-68, 2026-10-28; DR-90, 2026-11-02). Sums check: 595,855 + 607,752 = 1,203,607; 486,813 + 446,082 = 932,895.
Pass locations (headcounts): `00_Frame` L32-33, L124, L150-152, L180; `00.1_Step_MINUS-1_Input_Contract` L44, L218, L221, L242; `01_Inherited` L32; `04_Phase_02` L55-56; `04_Phase_04` L303, L315; `04_Phase_07` L151-152; `04_Phase_08` L349; `04_Phase_09` L101-102, L127-128; `05_Reconciliation` L282, L417; `07_QA_Gates` L51. City size in words: `04_Phase_06` L136 (Census II is 932,895).

### ZSO-011 Retention and mix between the censuses (recomputed)

| Quantity | Current | Computation |
|---|---|---|
| Combined retention | **77.51%** | 932,895 / 1,203,607 |
| Human retention | **81.70%** | 486,813 / 595,855 |
| Robot retention | **73.40%** | 446,082 / 607,752 |
| Spread, humans minus robots | **+8.30 pp** | 81.70 - 73.40 (8.301 unrounded) |
| Not in Census II | **270,712** (22.49% of Census I) | 1,203,607 - 932,895 |
| Robot / human share, Census I | 50.49% / 49.51% (robots ahead by 11,897) | 607,752 / 1,203,607 |
| Robot / human share, Census II | 47.82% / 52.18% (humans ahead by 40,731) | 446,082 / 932,895 |
| National surface retention, humans / robots / gap | 67.12% / 69.71% / -2.59 pp | `census` L554 (15,623,523 H; 16,403,077 R) and L694 (10,486,701 H; 11,434,935 R) |

Pass locations: `00_Frame` L150-155, L180; `01_Inherited` L92-94, L114; `02_Spine` L136-137, L168; `04.9_Step_4_Close-Out_Check` L85-86; `04_Phase_02` L55-57, L65, L309, L328; `04_Phase_04` L143; `04_Phase_05` L136; `04_Phase_06` L155, L205; `04_Phase_08` L368, L819, L964; `04_Phase_09` L127-129, L251, L383-384, L442; `04_Phase_10` L305; `06_Differentiation` L121. Shared output: `Cities/Cross_City_Culture_Differentiation_Table.md` L103 (Zhongshan's cell on those who left through the orbital exit).

### ZSO-012 Workforce, requirement and the three tiers

| Quantity | Current | Source address and computation |
|---|---|---|
| Workforce (all robots plus half the humans) | **905,680** | 607,752 + 595,855 / 2 = 905,679.5; `09` L72; `16` L275 |
| Requirement and share of workforce | 323,017; **35.7%** | `09` L72 (323,017 / 905,680 = 35.67%). `09` L1 says its Required and % WF columns use the food rate that `11` replaces; `11` L292 sets the rate at 120.7 per 1,000 humans |
| Baseline / mandated / free | **383,014 / 137,200 / 385,466** = 42.3% / 15.1% / 42.6% | `16` L1917-1923 (sum 905,680; unrounded 42.29 / 15.15 / 42.56) |
| Distinctive tier | 522,666 (57.7%); mandated is 26.25% of it | `16` L1925, L1932 |
| Robot term inside the baseline | 9,572 workers | 607,752 x 15.75 / 1,000; `16` L1926 |
| Sector sizes (35 / 25 / 15 / 15 / 7 / 3% of the distinctive tier) | technical 182,933 (137,200 mandated, 45,733 free); industrial 130,667; marine 78,400; commercial 78,400; education 36,587; other 15,680 | computed from the sector shares at `16` L1925-1926 |
| Baseline from the pass's own Phase 4 formula, live inputs | 140,905 (human term) + 232,537 (resident term) = 373,442; plus the robot term 9,572 = **383,014**; baseline 42.29%, freedom margin 57.71% | `09` L50 formula with B1 = 120.7 (`11` L292), D = 1.25, 1,203,607 residents. The 383,014 equals `16` L1921 |
| Half B row | workforce 905,680; 42.3 / 11.6 / 46.1; source H (a Half A estimate, "needs ruling") | `16` L275; legend `16` L244-245 |
| Developer's free-tier band | 38 to 48%; 42.6% lies inside it | `16` L1934-1938 (quoted there with the developer's 2026-09-02 words) |

Pass locations: `02_Spine` L56-58; `04_Phase_04` L34, L51, L247, L308-316, L320, L367; `04_Phase_07` L152-189, L203, L216, L270-271, L287, L313, L342, L638, L737, L744, L786; `04_Phase_08` L302, L460, L529, L584, L629-632; `04_Phase_09` L232; `04_Phase_10` L193; `08_Review_Panel` L238-240, L421, L576. Shared output: `Cities/Cross_City_Culture_Differentiation_Table.md` L113 (the cell on the mandated export). `04_Phase_07` L163-179 compares two derivations of the baseline and describes the robot term as booked elsewhere; `16` now books it inside the baseline (L1926).

### ZSO-013 Footprint, ice share and the three-city density

| Quantity | Current | Source address and computation |
|---|---|---|
| Zhongshan alone, area needed at 10,000 and 7,000 per km2 | **120.4 and 171.9 km2** (3.0 to 4.3 times the ~40 km2 oasis) | 1,203,607 / 10,000 and / 7,000; band at `Extent` L84; `census` L502 |
| Census I of the three Larsemann cities | 1,203,607 + 1,112,600 + 1,014,533 = **3,330,740** | `census` L502, L505, L509 |
| Footprint of the three together | **333.1 to 475.8 km2** | 3,330,740 / 10,000 and / 7,000 |
| Ice share of the three on a 40 km2 oasis | **88.0% to 91.6%** (rock 12.0% to 8.4%) | 40 / 333.1 and 40 / 475.8 |
| Gate 11's own check (one third of the oasis, 13.33 km2, against Zhongshan's footprint) | rock **11.08% and 7.75%** | 13.33 / 120.4 and / 171.9; method at `07_QA_Gates` L59-63 |
| Density of the three on the 40 km2 oasis | **83,269 per km2** | 3,330,740 / 40 = 83,268.5 |

Pass locations (footprint, ice and rock share): `00.1` L222-223; `00_Frame` L34, L168; `01_Inherited` L42; `02_Spine` L249-250, L274, L293; `04_Phase_03` L121; `04_Phase_06` L74; `04_Phase_07` L210, L231, L371, L473, L514, L890; `04_Phase_09` L188, L332, L439, L454; `05_Reconciliation` L228, L236, L416; `07_QA_Gates` L52-68; `08_Review_Panel` L349. Pass locations (three-city density per km2): `04_Phase_07` L93, L379-380, L811; `04_Phase_08` L417, L946; `04_Phase_09` L443; `07_QA_Gates` L56, L74, L92; `09.5_Log` L120. `07_QA_Gates` L72-95 rebuilds the argument that the density figure carried; the other locations still quote the density figure.

## B. The composition table and the text about it

### ZSO-016 Composition table, tiers, labels

Current table: `spec` L20-22 (tiers) and L36-70 (35 rows, shares of the city; 99.986 in total by rounding). Counts recomputed from those rows:

| Item | Current |
|---|---|
| Tiers | Primary 1 row (Sinian Federation 35.83); Significant 3 rows (Korea 9.70, Japan 7.30, Germany 7.10; sum 24.10); Notable 31 rows (sum 40.056) |
| Germany | Germany 7.10 plus Austro-Bavaria 1.37 (Notable) = 8.47 |
| Russia | Twelve rows sum to 5.685: Idelsk-Uralia 1.79, Russia (core state) 1.79, Siberia 0.71, Donska-Kubania 0.68, Künnarantaiga 0.41, Dagestan 0.13, Chechnya 0.060, Kabardino-Balkaria 0.036, North Ossetia-Alania 0.027, Ingushetia 0.020, Karachay-Cherkessia 0.019, Tuva 0.013; Finland 0.021 is listed as a Russian successor in `census` L857 |
| Other splits | Thailand 3.09 + Patani 0.09 = 3.18; Indonesia 2.86 + West Papua 0.061 + Aceh 0.059 = 2.98; Romania 2.58 + Hungary 0.30 = 2.88 (`census` L862, L869-871) |
| Australia | Notable, 3.66 (`spec` L40) |
| Notable range | 3.66 down to 0.013; 23 of the 35 rows are under 2%, 15 under 1%, 10 under 0.1% |
| Cumulative | three rows reach half (52.83); eleven rows reach 80% (82.83; ten rows give 79.97) |
| Leader | 35.83 against 64.17 for the rest; 35.83 / 9.70 = 3.69 |
| Pooled groups | East Asian (Sinian Federation + Korea + Japan) 52.83; Southeast Asian: Vietnam 3.56 + Thailand 3.09 + Malaysia 3.04 + Indonesia 2.86 + Philippines 1.72 = 14.27, or 14.48 with Patani, West Papua and Aceh; Baltic (Estonia 3.55 + Lithuania 3.14 + Latvia 1.58) 8.27 |
| Not parties to the Jeju-do court | 32 rows (all but the Sinian Federation, Japan, Korea; `spec` L165); row sum 47.156, complement 100 - 35.83 - 9.70 - 7.30 = 47.17 |
| Labels | The first two groups are "Sinian Federation" and "Korea" (`spec` L20, L36-37; `census` L845, L850). DR-21 (`rulings log` L586): name the state as the Sinian Federation where the period calls for it; the people are Chinese (`rulings log` L577-585) |
| "(founding wave)" tag | on the Sinian Federation only (`spec` L20); it means a founder named in the Founding Register (`rulings log` L1555); Register row `Cities/Founding_Register.md` L60 |

Pass locations (counts and tier lists): `00.1` L91; `01_Inherited` L34, L73; `02_Spine` L138-139; `03_Research` L206; `04_Phase_02` L69-78, L106, L190, L220, L310; `04_Phase_08` L138-143, L163-176, L238, L269, L431, L850-855, L884, L947, L951; `07_QA_Gates` L351. Pass locations (pooled groups): `04_Phase_08` L140-141, L190-192, L218, L226-227; `04_Phase_09` L113; `05_Reconciliation` L94, L110, L323, L419; `09.5_Log` L136, L139, L258. Pass locations (labels for the two largest groups): `00_Frame` L350; `00.1` L91; `01_Inherited` L34; `02_Spine` L136; `04_Phase_02` L73-74; `04_Phase_08` L138-139, L190; `04_Phase_10` L333. `census` L400-408 (Section A, Zhongshan) carries the same tier lists as `spec` L20-22.

### ZSO-015 Spec text the pass could lean on

Current: the honorific sentence ends by stating that the city kept the name of its station (`spec` L92); the phrase "founding operator heritage" does not occur in the spec; the Settled paragraph rests on the Founding Register and DR-21 (`spec` L163); the Jeju-do court's confirmation of Zhongshan's Chinese claim is stated at `spec` L163 and L173; the Register row is `Cities/Founding_Register.md` L60 ("The Sinian Federation's (i.e. China's) immediate geographic and time-zone access to the site"; founders only from the Register, DR-19). Nothing in the pass depends on the replaced sentences (a search of both pass folders on 2026-11-03 finds no pass file carrying the phrases "founding operator heritage", "cultural continuity" or "maritime heritage").

### ZSO-017 The Acts

`04_Phase_02` L153-160 describes the Act 1 date range. Current: Act 1 runs "2564 -> somewhere in the 2600s (a hazy range)" and Act 2 "by the late 2600s / early 2700s, onward" (`/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md` L105-106); Zhongshan's exception rests on access, "The Jeju-do court later confirmed the claim" (same file L19). `00.1` L60 carries the current wording.

### ZSO-018 Language

| Fact | Source address |
|---|---|
| Developer, 2026-11-02: *"For all of the locations, the dominant language is always Hawaiian, which later becomes Tepenian. The next dominant language after that is whoever holds the majority."* | `rulings log` L1563 (DR-89) |
| Developer, 2026-11-03: *"Remember that the de-facto national language is Hawaiian, and later becomes Tepenian. But at the time of the signing of the Falkland Treaty, it's Hawaiian."* (said of Contrapunto, stated as the national language at the Treaty) | `rulings log` L1632 (DR-96) |
| Supporting tier = every language group within 12 percentage points of the largest group's mid-point, for every city | `Cities/Research_Logs/Language_Sets_By_City_Reference_2026-11-03.md` L75-77; `Cities/Research_Logs/ULM_Runs_Casey_Then_Mirny_Handoff_2026-11-03.md` L28 |
| Zhongshan's groups: Mandarin 35.83; Korean 9.70; German 8.47; Japanese 7.30; English 4.94 to 10.90; Russian 3.59 to 5.685 | `Cities/Research_Logs/Language_Blocs_By_City_2026-11-03.csv` L775-780 |
| Within 12 points of Mandarin (35.83 - 12 = 23.83): none. The supporting tier is Mandarin alone; no other group is within 5 or 10 points | computed; `Language_Sets_By_City_Reference_2026-11-03.md` L36 |
| `spec` carries no language field | `spec` (searched 2026-11-03) |

Pass locations (language and speech): `00_Frame` L48, L327, L350 (the Federation fixes the language family; the Language Module); `04_Phase_05` L155; `04_Phase_08` L806-856 (§8.8). The pass names no language.

### ZSO-014 City names

| Pass location | Current name | Alias table address |
|---|---|---|
| `00.1` L48 | Relung Panen | `Cities/City_Renames_Alias_Table_2026-10-03.md` L12 |
| `04_Phase_06` L129 | Utstein | same file L11 |
| `04_Phase_05` L56 | Puerto Abrigo, Pergamino | same file L102-103 |
| `10_Readiness_Check` L40, L81, L100; `04_Phase_08` L205, L207 (where the city is meant) | Ariun Nuur; the district inside it, the real station and the lake keep "Vostok" | same file L105, L107 |
| `04_Phase_10` L82 | Contrapunto | same file L104 |

## C. Addresses that moved

### ZSO-019 Citations and source sizes

| Pass location | Topic | Current address |
|---|---|---|
| `00_Frame` L263, L363; `04_Phase_02` L29 | Zhongshan's census rows | Section A block `census` L400-408; Census I row L502; Census II row L643; held-ledger rows L754-755; Section D paragraph naming the city L816-817 |
| `00.1` L44 | census rows for the band check | `census` L502 and L643 |
| `04_Phase_02` L36, L86-90 | a one-sentence "only city" clause attributed to Section A | `census` Section A (L400-408) carries no such clause (searched 2026-11-03) |
| `00_Frame` L370; `02_Spine` L31; `00.1` L216 | Zhongshan's Extent rows | `Extent` L613 (city row) and L655 (scenario row); trio sum L593 |
| `04_Phase_02` L326, L327, L330; `04_Phase_06` L340-341; `04_Phase_07` L250, L744; `04_Phase_08` L59, L529, L917; `05_Reconciliation` L421; `07_QA_Gates` L128-129 (short-form `Specs/` citations) | the Founding Elder, Composer and Master Craftsman placeholders | `spec` L192, L193, L194 (fourth figure L195) |
| `04_Phase_02` L329 | the warmest-month temperature | `spec` L102 |
| `04_Phase_05` L324; `04_Phase_08` L1052; `04_Phase_10` L385; `05_Reconciliation` L423 (short-form) | the Economy and Industry line | `spec` L180 |
| `04_Phase_05` L192; `04_Phase_07` L48, L411 | the Hwy 4 / 22 / 110 tri-junction and the Hwy 22 and 110 routes | `Highways` L49-72 (row L60, L63, text L69), Hwy 22 block L139-153, Hwy 110 block L197-211, junction row L292 |
| `04_Phase_05` L323; `04_Phase_07` L916; `04_Phase_08` L1052; `04_Phase_10` L385; `05_Reconciliation` L423; `09.5_Log` L237 | the Highways flag about the Ports file and the hitchhiking list | `Highways` L349 (flag); hitchhiking section L354-397 |
| `04_Phase_05` L89, L331 | Zhongshan's entry in the relationship database | `Cities/City_Relationship_Database.md` L488-495 (freighter sentence L495) |
| `00_Frame` L261, L361; `02_Spine` L24; `04_Phase_02` L24, L28; `04_Phase_04` L30; `04_Phase_05` L28-33; `03_Research` L32, L57 (read-in-full records) | current lengths (`wc -l`, 2026-11-03) | spec 213; `No_National_Stereotypes.md` 174; `09` 272; Highways 397; Ports 881; Airports 123; Geothermal 217; Cross-Subnet file 241; relationship database 543; research log 750 |

### ZSO-020 Pre-Trip addresses

The Pre-Trip (`00.0_Pre-Trip_Inspection.md`) names 111 distinct absolute addresses. 110 exist on disk. The one that does not is `Zhongshan_Opus/09.6_Input_Audit.md`. Three independent counts (2026-11-03) agree.

## D. Pre-Trip notes (ZSO-001 to ZSO-006)

Dated notes sit beside three lines of `00.0_Pre-Trip_Inspection.md`; their figures are not repeated here, read the current values below. The Pre-Trip's raw block is a dated record.

| ID | Pre-Trip location | Current fact |
|---|---|---|
| ZSO-001 | L168 (the §E headcount check) | Census I humans 595,855, robots 607,752 (`census` L502) |
| ZSO-002 | L260 (§J, `DRQ-11`) | the three cities' Census I sums to 3,330,740 (`census` L502, L505, L509): 333 to 476 km2, 88.0% to 91.6% on ice (ZSO-013) |
| ZSO-003 | L182 (§F research log) | `Cities/Research_Logs/Zhongshan_Research_Log.md` is 750 lines (`wc -l`) |
| ZSO-004 | L286 (§K row for `06_Differentiation.md`) | `Zhongshan_Opus/06_Differentiation.md` is present; `09.6_Input_Audit.md` is absent |
| ZSO-005 | L4 and L74 (runbook size and Step 10 range) | `ULM/00_RUNBOOK.md` is 3,179 lines; Step 10 runs L3057 to L3152 (next heading L3153) |
| ZSO-006 | L23-24 (alias note; Characters tree) | alias addresses in ZSO-014; the GDD `Worldspace/Characters/` tree names the city in 7 files (`grep -rli`, 2026-11-03) |

## E. Standing decisions

- **D-1 (developer, 2026-10-30, the walk-through of this city).** *"yup, all as recommended."* Rule in force: pass files are not edited; corrections go in a dated amendment note beside the pass; the Pre-Trip alone carries dated notes beside three lines. Recorded in `ULM/Manual_Input_Audit_2026-10-29/Walkthrough_Decisions.md` L236-249 and `FIX_LEDGER.md` rows ZSO-001 to ZSO-S02.
- **ZSO-S01 = D-2 (same answer).** The `Extent` rows for Zhongshan stay as a dated record: `Extent` L613 (1,279,433 people; 128 and 183 km2), L655 (a -10% scenario row; 127,944 and 99,668) and L593 (three-city sum 3,527,096). `Extent` L631 states that its table is the dated record and the census is the live source. Current figures: 1,203,607 people need 120.4 to 171.9 km2 (ZSO-013).
- **ZSO-S02 = D-3 (same answer).** For Zhongshan, `16` section 18 (L1917, "ZHONGSHAN - DETERMINED") is the determination: 383,014 / 137,200 / 385,466 on a workforce of 905,680 (ZSO-012). The Half B row (`16` L275, source H) is a Half A estimate and does not govern.
- **D-4 (developer, 2026-10-30; Weekly To-Do L63-67).** The finished cities, Zhongshan included, are to be re-analyzed with the current methods; this note is the interim record.
- **D-5 (developer, 2026-10-29; `ULM/Manual_Input_Audit_2026-10-29/TRACKER.md` L5).** *"don't forget to check the cities we've already done, because things might possibly have changed since then."*
- None of D-1 to D-5 is in `rulings log` (searched 2026-11-03: no entry dated 2026-10-30; L1536's "all as recommended" concerns other items). `rulings log` L1354 (DR-68) names the Extent table among the items not refreshed.

## F. Source defects (two live sources disagree; neither chosen)

| ID | Statement and address | Against |
|---|---|---|
| SD-1 | `Extent` L613 gives Zhongshan 1,279,433 people (128 and 183 km2); L593 and `Cities/Division_of_Industry/05_Remaining_Cities_Assessment.md` L158, L193 give the three-city sum 3,527,096 (about 88,000 per km2 at L158); `Extent` L577 gives 353 to 504 km2 and 89 to 92% on ice | `census` L502, L505, L509: 1,203,607 and the sum 3,330,740 (83,269 per km2; 333 to 476 km2; 88.0% to 91.6%). `Extent` L631 calls its table the dated record |
| SD-2 | `spec` L165 calls Russia a Significant-tier nation at 5.72% | `spec` L21 (Significant: Korea, Japan, Germany) and L36-70 (Russia split into twelve rows, 5.685 in total) |
| SD-3 | `Cities/Local_Cultures/Mirny_Subnet/Zhongshan.md` L22-24 gives China as Primary, five Significant nations and twelve Notable | `spec` L20-22; the same culture file's L38 share list matches the spec |
| SD-4 | The same culture file, L110, calls Mandarin the city's sole public language | `rulings log` L1563: Hawaiian is dominant in all locations (ZSO-018) |
| SD-6 | `spec` L180 (Economy and Industry) names Prydz Bay maritime logistics and a cluster economy | `16` L1942-1957: the section 15 text says Prydz Bay fishing and "NOT a trade hub" |

## G. Conclusions that rest on current inputs and may change on re-derivation

No verdict is stated. Each row gives the input and its current value.

| ID | Pass location | Rests on | Current input |
|---|---|---|---|
| C1 | `04_Phase_08` L163-178 (shoulder and tail reading), reused at L321-329, L388-390, L849-850; L165 (rows that reach half and 80%) | the shape of the roster | ZSO-016: 3 Significant rows (24.10), 31 Notable rows from 3.66 to 0.013; three rows reach half, eleven reach 80% (`spec` L36-70) |
| C2 | `04_Phase_08` L271-285 (rows too small to show) | rows under the integration floor | 23 rows under 2%, 15 under 1%, 10 under 0.1% (`spec` L36-70) |
| C3 | `04_Phase_08` L232-250, L882-884, L947 (does any origin assume a polar climate) | the regions the roster spans | rows now in the table include Siberia 0.71, Künnarantaiga 0.41, Finland 0.021, Tuva 0.013 and six Caucasus rows summing 0.292 (`spec` L56, L58, L67, L70, L60, L63, L65-66, L68-69; `census` L857) |
| C4 | `04_Phase_08` L880-890 (closing axis), L1041; `07_QA_Gates` L341-351 (Gate 4); `06_Differentiation` L121; `04.9` L155; `04_Phase_10` L374 | the plurality, the gap to second place and the tail shape | 35.83; 3.69 times the second row; tail as in C1 (`spec` L36-70) |
| C5 | `04_Phase_08` L806-856 (§8.8); `00_Frame` L48, L327, L350; `04_Phase_05` L155 | the language facts | ZSO-018: Hawaiian dominant, supporting tier Mandarin alone; `spec` has no language field |
| C6 | `04_Phase_02` L59-65; `04_Phase_09` L132-139, L396-398, L442; `04_Phase_05` L136-141; `01_Inherited` L88-116 (where the inversion between the censuses originates) | Census I and II rows as in-world events | DR-90 added 14,930 H / 13,271 R to Census I (+2.57% / +2.23%) and 8,570 H / 11,462 R to Census II (+1.79% / +2.64%), marked "Arithmetic, NOT a migration" (`census` L502, L643); DR-68 added 12,139 H / 11,778 R and 8,108 H / 7,739 R |
| C7 | `04_Phase_07` L160-179 (two derivations agree on the baseline) | which figures `16` contains | ZSO-012: the `16` baseline 383,014 equals Phase 4's formula without the robot term (373,442) plus the robot term (9,572) |
| U1 | `04_Phase_05` L89; `04_Phase_07` L255-280, L638 (what the city supplies; the technical mandate) | relations with other cities | Relung Panen shares a joint agricultural research project with Davis, Ariun Nuur and Zhongshan (seed breeding, phosphorus and soil recovery): `rulings log` L1386 (DR-72) and L1421 (DR-75); no Zhongshan file mentions it |
| U2 | `04_Phase_08` L180-229 (pooling check: three candidate groups) | which groups could pool | a Russian-successor group of 5.685 (12 rows) and a German pair of 8.47 are also in the table (ZSO-016); Russian 3.59 to 5.685 and Tatar and Bashkir 0 to 1.79 in `Language_Blocs_By_City_2026-11-03.csv` L780, L790 |
| U3 | `04_Phase_05` L323-333; `04_Phase_07` L421-425 (imports and the Ports file) | the gateways in `Ports` | `Ports` L129 (Australia: Dumont d'Urville, Mirny, Mawson); L130 (neutral transshipment: Davis principal; Temirötkel, the Tri-Cities, Mawson); L202 and L229-230 (Hobart to the Nella Fjord port 4,877 km; Fremantle 4,817 km); `City_Relationship_Database.md` L495 |
| U4 | `04_Phase_05` L31, L250 (count of cities without geothermal heat) | the Geothermal file | `Geothermal` L38-39 and the open flag at L203-217 (Concordia has deep-drilled geothermal generation; options A to C not applied; the count 31 is 32 on the 38-city list, L205) |
| U5 | `03_Research` L36-58 (three inspiration picks) | the picks and later research on them | `Cities/Inspirational-Influences.md` L103-106 (Vilnius primary; Austin and Yekaterinburg secondary); `Cities/Research_Logs/Zhongshan_Inspiration_Place_Research_R1.md` (473 lines) and `_R2.md` (360 lines), 2026-10-26 |

## H. Open questions for the developer

1. **Language rule in this pass.** The pass names no language. The rule gives Hawaiian everywhere and Mandarin as Zhongshan's only supporting-tier language (ZSO-018). Should this enter as a dated note only, or should §8.8 be re-derived? The culture file (SD-4) calls Mandarin the sole public language.
2. **Which array is canonical, Opus or Sonnet.** `09_Record.md` L68-71 and L139 list it as an open developer question; no ruling is in `rulings log` (searched 2026-11-03). Pending.
3. **Re-derive or annotate.** The inputs of C1 to C4 (roster shape) and C5 (language) have moved most; C6 and C7 are short re-reads. Which of C1 to U5 should be re-run?
4. **Retention figures.** The census marks the two additions to Zhongshan as arithmetic and gives them different sizes by group in each census (C6). Should the retention rates in ZSO-011 be presented as findings about the city, or as arithmetic?
5. **Joint research project (U1).** Does it add a role to Zhongshan, or only to Relung Panen?
6. **Spec and culture-file text (SD-2, SD-3, SD-4, SD-6).** Should these lines be corrected so they agree with the spec table, the language rule and `16` section 18?
7. **Extent file and file 05 (SD-1).** Leave the dated Extent and `05` figures as they are, as D-2 does for the Extent rows?

Decisions pending elsewhere that touch Zhongshan: the language rule's entry into finished passes (`Cities/Research_Logs/Drift_Review_SUMMARY_Finished_Passes_2026-11-03.md` L52); the choice of canonical array (item 2); the re-analysis of the finished cities and the creation of Zhongshan's datasheets (Weekly To-Do L63-67); whether to re-derive or only annotate (summary file L53).

---

*Entries filed 2026-10-30 at the developer's direction ("yup, all as recommended."); rewritten 2026-11-03 to record current facts only.*
