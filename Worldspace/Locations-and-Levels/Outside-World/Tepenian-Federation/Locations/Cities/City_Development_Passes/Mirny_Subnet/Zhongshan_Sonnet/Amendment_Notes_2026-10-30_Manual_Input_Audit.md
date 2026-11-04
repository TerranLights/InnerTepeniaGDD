# Zhongshan (Sonnet trial): amendment notes (current as of 2026-11-03)

**What this is.** For each place where the Sonnet trial's text does not match the sources as they stand on 2026-11-03: the trial location, a neutral label for the topic, and the current fact with its source address. It covers only what the trial contains (Step -1 to Phase 3) and replaces the note filed 2026-10-30. Where a fact is the same as in the Opus folder's note, it is written out here in full and the trial files it applies to are named.
**No pass file is edited by this note.** The Pre-Trip alone carries dated notes, added 2026-10-30 (see "Pre-Trip notes").
**How entries are built.** Each current figure is read from the live file as of 2026-11-03 and each derived figure is recomputed by command. A trial location names where the text sits and what it is about, never what it says. Entry IDs are stable; other files cite them.
**Trial dates.** Run 2026-09-10 to 2026-09-11, committed 2026-09-13; Pre-Trip refreshed 2026-10-21; spec line citations remapped in part on 2026-11-02 (see ZSS-018). The trial holds the seven pass files `00.1_Step_MINUS-1_Input_Contract`, `00_Frame`, `01_Inherited`, `02_Spine`, `03_Research`, `04_Phase_02_Composition_and_Arrival`, `04_Phase_03_Surface_and_Texture`, plus the Pre-Trip and README. Most of these copy the Opus files' text.

**Source key.** `Cities/` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/`. `ULM/` = `Worldspace/Locations-and-Levels/Universal_Location_Methodology/`. `census` = `Cities/Official_Population_Census.md`. `spec` = `Cities/Specs/Mirny subnet/Zhongshan.md`. `09`, `16` = `Cities/Division_of_Industry/09_Per_City_Baseline_Run.md`, `16_Per_City_Three_Tier_Run.md`. `Extent` = `ULM/Extent_and_Density_Per_City.md`. `rulings log` = `ULM/DEVELOPER_RULINGS_LOG.md`. Plain meaning of the rulings cited: DR-21 confirmed Zhongshan's Chinese founding; DR-68 and DR-90 are the two population-adjustment steps (Santa Luce scenario 2026-10-28, Esperanza relocation 2026-11-02); DR-85 rebuilt every city's composition table (2026-11-02); DR-88 narrowed the "(founding wave)" tag; DR-89 and DR-96 set the language rule; DR-97 put the robot-keyed requirement into file 16.

---

## A. Population and the figures built on it

### ZSS-010 Headcounts

| Item | Current | Source address |
|---|---|---|
| Census I humans / robots / combined | 595,855 / 607,752 / **1,203,607** | `census` L502; `spec` L15 |
| Census II humans / robots / combined | 486,813 / 446,082 / **932,895** | `census` L643; `spec` L16 |

`census` L502 and L643 each carry two dated additions marked "Arithmetic, NOT a migration" (DR-68, 2026-10-28; DR-90, 2026-11-02). Sums check: 595,855 + 607,752 = 1,203,607; 486,813 + 446,082 = 932,895.
Trial locations (headcounts): `00_Frame` L32-33, L124, L150-152; `00.1_Step_MINUS-1_Input_Contract` L44, L218, L221, L242; `01_Inherited` L32; `04_Phase_02` L55-56.

### ZSS-011 Retention and mix between the censuses (recomputed)

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

Trial locations: `00_Frame` L150-155, L180; `01_Inherited` L92-94, L114; `02_Spine` L136-137, L168; `04_Phase_02` L55-57, L65, L306, L325.

### ZSS-012 Footprint and ice share

| Quantity | Current | Source address and computation |
|---|---|---|
| Zhongshan alone, area needed at 10,000 and 7,000 per km2 | **120.4 and 171.9 km2** (3.0 to 4.3 times the ~40 km2 oasis) | 1,203,607 / 10,000 and / 7,000; band at `Extent` L84; `census` L502 |
| Census I of the three Larsemann cities | 1,203,607 + 1,112,600 + 1,014,533 = **3,330,740** | `census` L502, L505, L509 |
| Footprint of the three together | **333.1 to 475.8 km2** | 3,330,740 / 10,000 and / 7,000 |
| Ice share of the three on a 40 km2 oasis | **88.0% to 91.6%** (rock 12.0% to 8.4%) | 40 / 333.1 and 40 / 475.8 |
| A third of the oasis (13.33 km2) against Zhongshan's footprint | rock **11.08% and 7.75%** | 13.33 / 120.4 and / 171.9 |

Trial locations: `00.1` L222-223; `00_Frame` L34, L168; `01_Inherited` L42; `02_Spine` L249-250, L274, L293; `04_Phase_03` L121. The trial quotes no three-city density figure.

### ZSS-014 Scope, and the Division-of-Industry figures the trial carries

The trial holds no Phase 4 to Phase 10 files and no workforce counts. It does carry file 16 section 18's three tier shares and the mandate: `02_Spine` L56-58 (the shares), L25, L39, L49, L52, L82, L164 (section 18 read and relied on) and `03_Research` L189.

| Quantity | Current | Source address |
|---|---|---|
| Baseline / mandated / free | 383,014 / 137,200 / 385,466 = **42.3% / 15.1% / 42.6%** of a workforce of 905,680 | `16` L1921-1923 |
| Difficulty and food term | D = 1.25, GROWER, food term 100% | `16` L1921 |
| Mandate | 137,200 workers, three quarters of the 35% technical sector, 26.25% of the distinctive tier (522,666; 57.7%) | `16` L1925, L1932 |
| Workforce | 905,680 = 607,752 + 595,855 / 2 (905,679.5) | `09` L72; `16` L275 |
| Developer's free-tier band | 38 to 48%; 42.6% lies inside it | `16` L1934-1938 |
| Robot-keyed term inside the baseline | 9,572 workers (607,752 x 15.75 / 1,000) | `16` L1926 |

## B. The composition table and the text about it

### ZSS-015 Composition table, tiers, labels

Current table: `spec` L20-22 (tiers) and L36-70 (35 rows, shares of the city; 99.986 in total by rounding). Counts recomputed from those rows:

| Item | Current |
|---|---|
| Tiers | Primary 1 row (Sinian Federation 35.83); Significant 3 rows (Korea 9.70, Japan 7.30, Germany 7.10; sum 24.10); Notable 31 rows (sum 40.056) |
| Germany | Germany 7.10 plus Austro-Bavaria 1.37 (Notable) = 8.47 |
| Russia | Twelve rows sum to 5.685: Idelsk-Uralia 1.79, Russia (core state) 1.79, Siberia 0.71, Donska-Kubania 0.68, Künnarantaiga 0.41, Dagestan 0.13, Chechnya 0.060, Kabardino-Balkaria 0.036, North Ossetia-Alania 0.027, Ingushetia 0.020, Karachay-Cherkessia 0.019, Tuva 0.013; Finland 0.021 is listed as a Russian successor in `census` L857 |
| Other splits | Thailand 3.09 + Patani 0.09 = 3.18; Indonesia 2.86 + West Papua 0.061 + Aceh 0.059 = 2.98; Romania 2.58 + Hungary 0.30 = 2.88 (`census` L862, L869-871) |
| Australia | Notable, 3.66 (`spec` L40) |
| Notable range | 3.66 down to 0.013; 23 of the 35 rows are under 2%, 15 under 1%, 10 under 0.1% |
| Leader | 35.83 against 64.17 for the rest; 35.83 / 9.70 = 3.69; the second row is 27.1% of the first |
| Not parties to the Jeju-do court | 32 rows (all but the Sinian Federation, Japan, Korea; `spec` L165); row sum 47.156, complement 100 - 35.83 - 9.70 - 7.30 = 47.17 |
| Labels | The first two groups are "Sinian Federation" and "Korea" (`spec` L20, L36-37; `census` L845, L850). DR-21 (`rulings log` L586): name the state as the Sinian Federation where the period calls for it; the people are Chinese (`rulings log` L577-585) |
| "(founding wave)" tag | on the Sinian Federation only (`spec` L20); it means a founder named in the Founding Register (`rulings log` L1555); Register row `Cities/Founding_Register.md` L60 |

Trial locations (counts and tier lists): `00.1` L91; `01_Inherited` L34, L73; `02_Spine` L138-139; `03_Research` L206; `04_Phase_02` L69-78, L106, L187, L217, L307. Trial locations (labels for the two largest groups): `00_Frame` L350; `00.1` L91; `01_Inherited` L34; `02_Spine` L136; `04_Phase_02` L73-74. `census` L400-408 (Section A, Zhongshan) carries the same tier lists as `spec` L20-22.

### ZSS-016 Spec text, the Jeju-do court and the Acts

- **Spec text.** The honorific sentence ends by stating that the city kept the name of its station (`spec` L92); the phrase "founding operator heritage" does not occur in the spec; the Settled paragraph rests on the Founding Register and DR-21 (`spec` L163); the Jeju-do court's confirmation of Zhongshan's Chinese claim is stated at `spec` L163 and L173; the Register row is `Cities/Founding_Register.md` L60 ("The Sinian Federation's (i.e. China's) immediate geographic and time-zone access to the site"; founders only from the Register, DR-19). Nothing in the trial depends on the replaced sentences (a search of the trial on 2026-11-03 finds none of the phrases "founding operator heritage", "cultural continuity" or "maritime heritage"). The trial quotes `spec` L165 at `01_Inherited` L66-68; see SD-2.
- **The Acts.** `04_Phase_02` L150-157 describes the Act 1 date range. Current: Act 1 runs "2564 -> somewhere in the 2600s (a hazy range)" and Act 2 "by the late 2600s / early 2700s, onward" (`/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md` L105-106); Zhongshan's exception rests on access, "The Jeju-do court later confirmed the claim" (same file L19). `00.1` L60 carries the current wording.

### ZSS-017 Language

| Fact | Source address |
|---|---|
| Developer, 2026-11-02: *"For all of the locations, the dominant language is always Hawaiian, which later becomes Tepenian. The next dominant language after that is whoever holds the majority."* | `rulings log` L1563 (DR-89) |
| Developer, 2026-11-03: *"Remember that the de-facto national language is Hawaiian, and later becomes Tepenian. But at the time of the signing of the Falkland Treaty, it's Hawaiian."* (said of Contrapunto, stated as the national language at the Treaty) | `rulings log` L1632 (DR-96) |
| Supporting tier = every language group within 12 percentage points of the largest group's mid-point, for every city | `Cities/Research_Logs/Language_Sets_By_City_Reference_2026-11-03.md` L75-77; `Cities/Research_Logs/ULM_Runs_Casey_Then_Mirny_Handoff_2026-11-03.md` L28 |
| Zhongshan's groups: Mandarin 35.83; Korean 9.70; German 8.47; Japanese 7.30; English 4.94 to 10.90; Russian 3.59 to 5.685 | `Cities/Research_Logs/Language_Blocs_By_City_2026-11-03.csv` L775-780 |
| Within 12 points of Mandarin (35.83 - 12 = 23.83): none. The supporting tier is Mandarin alone; no other group is within 5 or 10 points | computed; `Language_Sets_By_City_Reference_2026-11-03.md` L36 |
| `spec` carries no language field | `spec` (searched 2026-11-03) |

Trial locations (language): `00_Frame` L48, L327, L350 (the Federation fixes the language family; the Language Module); `03_Research` L208-209 (a research finding on station languages). The trial names no language for Zhongshan.

### ZSS-013 City names

`00.1_Step_MINUS-1_Input_Contract` L48 names the city now called **Relung Panen** (`Cities/City_Renames_Alias_Table_2026-10-03.md` L12). No other retired name occurs in the trial files (searched 2026-11-03 for Princess Elisabeth, Port Lockroy, Juan Carlos, Sejong, Sayowa, Vostok).

## C. Addresses that moved

### ZSS-018 Citations and source sizes

| Trial location | Topic | Current address |
|---|---|---|
| `00_Frame` L263, L363; `04_Phase_02` L29 | Zhongshan's census rows | Section A block `census` L400-408; Census I row L502; Census II row L643; held-ledger rows L754-755; Section D paragraph naming the city L816-817 |
| `00.1` L44 | census rows for the band check | `census` L502 and L643 |
| `04_Phase_02` L36, L86-90 | a one-sentence "only city" clause attributed to Section A | `census` Section A (L400-408) carries no such clause (searched 2026-11-03) |
| `00_Frame` L370; `02_Spine` L31; `00.1` L216 | Zhongshan's Extent rows | `Extent` L613 (city row) and L655 (scenario row); trio sum L593 |
| `04_Phase_02` L323, L324, L327 (short-form `Specs/` citations) | the Founding Elder and Composer placeholders | `spec` L192, L193 (block L192-195) |
| `04_Phase_02` L326 | the warmest-month temperature | `spec` L102 |
| `00_Frame` L261, L361; `02_Spine` L24; `04_Phase_02` L28 (read-in-full records) | current length of the spec (`wc -l`, 2026-11-03) | 213 |
| `04_Phase_02` L24 | current length of `No_National_Stereotypes.md` | 174 |
| `03_Research` L32, L57 | current length of `Cities/Research_Logs/Zhongshan_Research_Log.md` | 750 |

### ZSS-019 Pre-Trip addresses

The Pre-Trip (`00.0_Pre-Trip_Inspection.md`) names 111 distinct absolute addresses. 106 exist on disk. The five that do not are `Zhongshan_Sonnet/04_Phase_04_Ordinary_Life.md`, `04_Phase_08_Making.md`, `06_Differentiation.md`, `09.5_Log.md` and `09.6_Input_Audit.md`. Three independent counts (2026-11-03) agree.

## D. Pre-Trip notes (ZSS-001)

The Sonnet `00.0_Pre-Trip_Inspection.md` carries dated notes at the same lines as the Opus Pre-Trip; their figures are not repeated here, read the current values below.

| Pre-Trip location | Current fact |
|---|---|
| L168 (the §E headcount check) | Census I humans 595,855, robots 607,752 (`census` L502) |
| L260 (§J, `DRQ-11`) | the three cities' Census I sums to 3,330,740 (`census` L502, L505, L509): 333 to 476 km2, 88.0% to 91.6% on ice (ZSS-012) |
| L182 (§F research log) | `Cities/Research_Logs/Zhongshan_Research_Log.md` is 750 lines (`wc -l`) |
| L286 (§K row for `06_Differentiation.md`) | this folder holds neither `06_Differentiation.md` nor `09.6_Input_Audit.md`; `Zhongshan_Opus/06_Differentiation.md` is present and `Zhongshan_Opus/09.6_Input_Audit.md` is absent |
| L4 and L74 (runbook size and Step 10 range) | `ULM/00_RUNBOOK.md` is 3,179 lines; Step 10 runs L3057 to L3152 (next heading L3153) |
| L23-24 (alias note; Characters tree) | alias address in ZSS-013; the GDD `Worldspace/Characters/` tree names the city in 7 files (`grep -rli`, 2026-11-03) |

## E. Standing decisions

- **D-1 (developer, 2026-10-30, the walk-through of this city).** *"yup, all as recommended."* Rule in force: pass files are not edited; corrections go in a dated amendment note beside the trial; the Pre-Trip alone carries dated notes beside three lines. Recorded in `ULM/Manual_Input_Audit_2026-10-29/Walkthrough_Decisions.md` L236-249 and `FIX_LEDGER.md` rows ZSS-001 to ZSS-014.
- **D-2 (same answer; Opus ledger row ZSO-S01).** The `Extent` rows for Zhongshan stay as a dated record: `Extent` L613 (1,279,433 people; 128 and 183 km2), L655 (a -10% scenario row; 127,944 and 99,668) and L593 (three-city sum 3,527,096). `Extent` L631 states that its table is the dated record and the census is the live source. Current figures: 1,203,607 people need 120.4 to 171.9 km2 (ZSS-012). The trial cites these rows at `00_Frame` L370, `02_Spine` L31, `00.1` L216.
- **D-3 (same answer; Opus ledger row ZSO-S02).** For Zhongshan, `16` section 18 (L1917, "ZHONGSHAN - DETERMINED") is the determination: 383,014 / 137,200 / 385,466 on a workforce of 905,680 (ZSS-014). The Half B row (`16` L275, 42.3 / 11.6 / 46.1, source H) is a Half A estimate and does not govern. The trial's `02_Spine` L56-58 uses section 18.
- **D-4 (developer, 2026-10-30; Weekly To-Do L63-67).** The finished cities, Zhongshan included, are to be re-analyzed with the current methods; this note is the interim record.
- **D-5 (developer, 2026-10-29; `ULM/Manual_Input_Audit_2026-10-29/TRACKER.md` L5).** *"don't forget to check the cities we've already done, because things might possibly have changed since then."*
- None of D-1 to D-5 is in `rulings log` (searched 2026-11-03: no entry dated 2026-10-30; L1536's "all as recommended" concerns other items). `rulings log` L1354 (DR-68) names the Extent table among the items not refreshed.

## F. Source defects (two live sources disagree; neither chosen)

| ID | Statement and address | Against |
|---|---|---|
| SD-1 | `Extent` L613 gives Zhongshan 1,279,433 people (128 and 183 km2); L593 gives the three-city sum 3,527,096; `Extent` L577 gives 353 to 504 km2 and 89 to 92% on ice | `census` L502, L505, L509: 1,203,607 and the sum 3,330,740 (333 to 476 km2; 88.0% to 91.6%). `Extent` L631 calls its table the dated record |
| SD-2 | `spec` L165 (quoted in the trial at `01_Inherited` L66-68) calls Russia a Significant-tier nation at 5.72% | `spec` L21 (Significant: Korea, Japan, Germany) and L36-70 (Russia split into twelve rows, 5.685 in total) |
| SD-3 | `spec` L180 (Economy and Industry) names Prydz Bay maritime logistics and a cluster economy (the trial flags it at `02_Spine` L45) | `16` L1942-1957: the section 15 text says Prydz Bay fishing and "NOT a trade hub" |

## G. Conclusions that rest on current inputs and may change on re-derivation

No verdict is stated. Each row gives the input and its current value.

| ID | Trial location | Rests on | Current input |
|---|---|---|---|
| C-S1 | `04_Phase_02` L69-82 (the structure of "everyone else"); `02_Spine` L136-139 (strength, deficit, standing cost, grudging tolerance) | the shape of the roster | 35 rows; second row 9.70 is 27.1% of the leader; Notable rows 3.66 down to 0.013 (a band 3.647 points wide); six rows lie between 3.04 and 3.66 (`spec` L36-70) |
| C-S2 | `04_Phase_02` L59-65; `01_Inherited` L88-116; `02_Spine` L136-137 (where the inversion between the censuses originates) | Census I and II rows as in-world events | DR-90 added 14,930 H / 13,271 R to Census I (+2.57% / +2.23%) and 8,570 H / 11,462 R to Census II (+1.79% / +2.64%), marked "Arithmetic, NOT a migration" (`census` L502, L643); DR-68 added 12,139 H / 11,778 R and 8,108 H / 7,739 R |
| C-S3 | `04_Phase_02` L150-160 (Act 1 and the continuous-habitation branch) | the Act 1 date range | ZSS-016: "somewhere in the 2600s (a hazy range)" |
| C-S4 | `04_Phase_03` L121; `02_Spine` L249-293 (the rock and ice divide) | the rock share | ZSS-012: rock 8.4% to 12.0% of the three cities' footprint; 7.75% to 11.08% by the third-of-the-oasis method |
| C-S5 | `02_Spine` L56-58, L82, L164 (technical mandate; what leaves the city) | file 16 section 18 | ZSS-014: 42.3 / 15.1 / 42.6; mandate 137,200 |
| C-S6 | `00_Frame` L48, L327, L350 (language family; Language Module) | the language facts | ZSS-017: Hawaiian dominant, supporting tier Mandarin alone |
| U-S1 | `02_Spine` L82, L164 (function: people, not cargo) | relations with other cities | Relung Panen shares a joint agricultural research project with Davis, Ariun Nuur and Zhongshan: `rulings log` L1386 (DR-72) and L1421 (DR-75); no Zhongshan file mentions it |
| U-S2 | `03_Research` L36-58 (three inspiration picks) | the picks and later research on them | `Cities/Inspirational-Influences.md` L103-106 (Vilnius primary; Austin and Yekaterinburg secondary); `Cities/Research_Logs/Zhongshan_Inspiration_Place_Research_R1.md` (473 lines) and `_R2.md` (360 lines), 2026-10-26 |

## H. Open questions for the developer

1. **Language rule in this trial.** The trial names no language. The rule gives Hawaiian everywhere and Mandarin as Zhongshan's only supporting-tier language (ZSS-017). Should it enter as a dated note only?
2. **Which array is canonical, Opus or Sonnet.** `Zhongshan_Opus/09_Record.md` L68-71 and L139 list it as an open developer question; no ruling is in `rulings log` (searched 2026-11-03). Pending.
3. **Retention figures.** The census marks the two additions to Zhongshan as arithmetic and gives them different sizes by group in each census (C-S2). Should the retention rates in ZSS-011 be presented as findings about the city, or as arithmetic?
4. **Spec text (SD-2, SD-3).** Should `spec` L165 and L180 be corrected so they agree with the spec table and `16` section 18?
5. **Extent file (SD-1).** Leave the dated Extent figures as they are, as D-2 does for the Extent rows?
6. **Joint research project (U-S1).** Does it add a role to Zhongshan, or only to Relung Panen?

Decisions pending elsewhere that touch Zhongshan: the language rule's entry into finished passes (`Cities/Research_Logs/Drift_Review_SUMMARY_Finished_Passes_2026-11-03.md` L52); the choice of canonical array (item 2); the re-analysis of the finished cities and the creation of Zhongshan's datasheets (Weekly To-Do L63-67); whether to re-derive or only annotate (summary file L53).

---

*Entries filed 2026-10-30 at the developer's direction ("yup, all as recommended."); rewritten 2026-11-03 to record current facts only. Opus-folder facts that repeat here: ZSO-010 to ZSO-013, ZSO-015 to ZSO-018.*
