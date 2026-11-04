# Shirayuki: amendment notes (current as of 2026-11-03)

**What this is.** A record of where Shirayuki's pass text does not match the sources as they stand on 2026-11-03, and what the sources say. It is the only amendment record for this pass. **This note edits no pass file, and no pass file has been edited.**
**How entries are built.** Pass location (file and line, with a neutral description of the topic), then the current fact, then its source address (file and line, or exact heading). Every current figure is read from the source line named; every derived figure is recomputed by command (2026-11-03).
**Entry numbers** (`SRY-001` to `SRY-008`, `SRY-S01` to `SRY-S03`) are cited by other files and are kept; new entries continue the numbering. Pass line numbers are as the files stand today.
**The pass** ran 2026-09-06 to 2026-09-13, with later edits to 2026-10-01, and is complete (`10_Readiness_Check.md` L321–322). Paths below: `CITIES` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/`; `ULM` = `Worldspace/Locations-and-Levels/Universal_Location_Methodology/`.

---

## A. Standing decisions (present tense)

**D-1. The developer's answer to the walk-through of 2026-10-30 is *"yup, all as recommended."*** (`ULM/Manual_Input_Audit_2026-10-29/Walkthrough_Decisions.md` L199–L201.) Standing consequence: no pass file is edited; each mismatch between the pass and the sources is recorded in this note; the pass stays the record of what it worked from. Recorded in `Walkthrough_Decisions.md` L199–L211 and `FIX_LEDGER.md` L1491–L1493. Not in `ULM/DEVELOPER_RULINGS_LOG.md`.

**D-2. A fresh analysis of the finished cities, and Pre-Trip and datasheet files for Shirayuki, are planned and not started.** Same message, 2026-10-30 (`Walkthrough_Decisions.md` L211): create the Pre-Trip and datasheet files for the cities that have none (Shirayuki is one); re-analyze Shirayuki, Sinheung and Zhongshan with the current methods. `Dev-Road-Map/Weekly_To-Do_-_Current.md` L65 and L67 carry both as open items. The pass folder holds no Pre-Trip or datasheet file. This note is the interim record. The Walkthrough paraphrases this decision; the developer's exact words are not in the repo.

**`SRY-S01`. The census tier list for Shirayuki equals the spec's.** `CITIES/Official_Population_Census.md` L424–L428 (Primary Japan; Significant Australia, Korea; Notable 35 rows, Sinian Federation first, Tibet last) is line for line the same as `CITIES/Specs/Mirny subnet/Shirayuki.md` L44–L48 (checked by `diff` of census L426–428 against spec L46–48: no difference). The census file is 892 lines (`wc -l`). Standing rule: the census tier list is kept equal to the spec's. The prose at census L422 is a separate item (`SRY-S04`).

**`SRY-S02`. Left in place.** `ULM/Extent_and_Density_Per_City.md` L616 (Shirayuki row) and L656 (Shirayuki scenario row) stay as dated records: L631 labels the table a record of the 2026-09-05 populations, and L656 sits in a dated scenario. Live: Census I 1,112,600 (`CITIES/Official_Population_Census.md` L505) needs 111.3 km² at 10,000 per km² and 158.9 km² at 7,000 per km² (`SRY-003`).

**`SRY-S03`. Left in place.** `CITIES/Division_of_Industry/16_Per_City_Three_Tier_Run.md` is not edited by this note. Its Shirayuki section (L1754–L1769) is covered by `SRY-006` and `SRY-011`.

---

## B. Founding

### SRY-005. The Founding Register states geography as an added founding factor (`DR-44`); founders come only from the Register (`DR-19`)

**Pass places that state the founding basis as the allocation alone** (each read in context): `00_Frame.md` L65 (epistemic-horizon lines) and L266 (founding row of the frame's table); `01_Inherited.md` L197–L204 (section `A1`); `02_Spine.md` L87; `04_Phase_02_Composition_and_Arrival.md` L42 (Primary-tier row) and L107; `04_Phase_05_Relation_and_Geometry.md` L47; `04_Phase_07_Order.md` L106 (legitimacy row); `04_Phase_10_Catalog.md` L158 ("Traces to" line); `04z_Post-Ruling_Enrichment_Review.md` L17; `07_QA_Gates.md` L156; `09.5_Log.md` L64, L206, L475, L707 (dated record). A search of the 22 numbered pass files and `README.md` for "zone gap", `DR-44`, "Founding Register" and `Founding_Register` returns no hit, so the pass cites neither the Register row nor the geography factor.

**Current fact.** `CITIES/Founding_Register.md` **L61** (header at L36), quoted exactly:

```
| Shirayuki | Mirny | +5 | ✅ | Japan, by the Jeju-do court's diplomatic allocation | The Jeju-do court's diplomatic allocation, **and, in addition, geography**: zone gap 3 to the Prydz Bay coast (the edge of the rule). Developer: geography is an *additional* factor, not a replacement. | `Specs/Mirny subnet/Shirayuki.md` L203; `DR-44` | — |
```

Spec L203 reads "Japanese exiles, arriving via the Jeju-do court's diplomatic allocation." The Register's change log (L90) records the ruling: "Shirayuki and Sinheung (the Jeju-do allocation, plus geography)".

**Standing decision (`DR-44`, 2026-10-03; ruling of the remaining founding rows).** Developer, verbatim (`ULM/DEVELOPER_RULINGS_LOG.md` L919): *"for Shirayuki and Sinheung … I would change that to geography being an additional factor, on top of the agreement at the Court of Jeju-Do"*. The ruling's table row (L930): "Japan and Korea stay, **by the Jeju-do court's diplomatic allocation, with geography (zone gap 3 to the Prydz Bay coast) as an ADDITIONAL factor** on top of it. Not a rewrite of the basis. Closes `FQ-13c`". Recorded in the rulings log.

**Standing rule (`DR-19`, 2026-09-30; founders stand on geography and access, never on the real station).** Register L8–L10: "Founders are decided here and nowhere else. No spec, culture sheet, megasheet, catalog, census tag, robot-culture sheet, datasheet or ULM pass may originate or restate a founding claim that this file doesn't hold. They **point to this file**." Register L11–L13: "A founding nation stands on geography and access, never on the real station." Rulings log L552: founding nations are "Legitimate on **geography and access**". Register L14 (rule 3, developer 2026-10-01): state each founding on the city's own geography and access. Recorded in the rulings log (`DR-19` L538).

### SRY-009. The station-heritage question about the national-connections file is closed

**Pass places that treat it as open or the tie as unusable:** `00_Frame.md` L148; `04_Phase_02_Composition_and_Arrival.md` L283; `04_Phase_05_Relation_and_Geometry.md` L89–L92 and L258; `05_Reconciliation.md` L254, L341 (row 8) and L346; `07_QA_Gates.md` L32 and L126; `09_Record.md` L35 and L99; `10_Readiness_Check.md` L132–L133; `README.md` L66; `09.5_Log.md` L707 (dated record).

**Current fact.** The question (`DRQ-14`: could a rated tie built on the real station's heritage stand in `City_National_Connections.md`) carries ✅ and "ANSWERED 2026-10-01" in its heading at `Worldspace/Canon_Gap_Resolution_Method/Developer_Ruling_Queue.md` **L696**. The closing text (L698–L702) says: answered by `DR-19`; the offending line is gone from `City_National_Connections.md`; the Shirayuki tie to the Mawson-subnet junction city (the name in that text is the one now ruled Temirötkel) is re-grounded on Highway 4; the corpus sweep is done; closed by the developer 2026-10-01. The live tie is `CITIES/City_National_Connections.md` L393–L394 (Shirayuki entry, L388): "Temirötkel (Mawson) — Medium, Infrastructure. Hwy 4 runs from the Temirötkel Junction to Shirayuki, the same Spur/Junction link that reaches Sinheung alongside it." Governing text: Register L8–L13 and rulings log `DR-19` (L538, L552). The other four queue questions the pass lists beside it (`DRQ-10` to `DRQ-13`) carry the open mark at queue L551, L579, L614, L656.

---

## C. Population figures and derived numbers

### SRY-001. Census totals (the population changes ruled 2026-10-28, `DR-68`, and 2026-11-02, `DR-90`: Esperanza cut to 1,200,000 and the difference spread over the other cities)

| | Census I | Census II |
|---|---|---|
| Humans | 545,891 | 319,190 |
| Robots | 566,709 | 372,181 |
| Combined | **1,112,600** | **691,371** |

Sources: `CITIES/Official_Population_Census.md` **L505** (Census I) and **L653** (Census II); `Specs/Mirny subnet/Shirayuki.md` L41 and L42 carry the same totals. The row notes record the two rulings (L505: `DR-68` +12,139 H / +11,778 R, then `DR-90` +14,930 H / +13,271 R; L653: `DR-68` +8,108 H / +7,739 R, then `DR-90` +8,570 H / +11,462 R).

**Pass places that carry the Census I and II totals or their components** (found by pattern search, read in context): `00_Frame.md` L29–L30, L45, L157–L159; `01_Inherited.md` L80, L86–L89, L111, L174, L229, L243; `03_Research.md` L314; `04_Phase_02_Composition_and_Arrival.md` L75, L94; `04_Phase_09_Populations.md` L24–L25; `05_Reconciliation.md` L174–L175, L333 (the table and docket row that give a "current" census column); `07_QA_Gates.md` L167–L168, L173–L175 (pasted raw scan output, a record of the 2026-09-06 run); `09.6_Input_Audit.md` L35; `09.5_Log.md` L571, L647, L925 (dated record).

### SRY-002. Derived figures (recomputed by command from the rows above)

| Derived figure | Current value |
|---|---|
| Retention, combined (691,371 ÷ 1,112,600) | **62.14%** |
| Retention, humans (319,190 ÷ 545,891) | **58.47%** |
| Retention, robots (372,181 ÷ 566,709) | **65.67%** |
| People not here (1,112,600 − 691,371) | **421,229** (humans 226,701; robots 194,528) |
| Humans gone / robots gone | **41.53%** / **34.33%** |
| Gap, robots minus humans | **+7.20 percentage points** |
| Robot share, Census I then II | **50.94%** then **53.83%** (+2.90 points) |

**Pass places:** retention and departure figures at `00_Frame.md` L311; `01_Inherited.md` L86–L89, L92, L103–L104, L111–L112, L119–L121, L228, L236, L349–L351, L370, L384, L408; `02_Spine.md` L125, L133; `03_Research.md` L163, L234, L250; `04_Phase_02_Composition_and_Arrival.md` L94, L244, L273; `04_Phase_05_Relation_and_Geometry.md` L234, L246–L247; `04_Phase_07_Order.md` L128; `04_Phase_09_Populations.md` L24–L25, L108, L202; `04_Phase_10_Catalog.md` L288; `04z_Post-Ruling_Enrichment_Review.md` L62, L251; `07_QA_Gates.md` L175; `09.5_Log.md` L65, L91, L354, L486, L563, L566, L570, L594, L625, L647, L715, L799, L827, L925 (dated record). Robot-share figures at `01_Inherited.md` L91, L113; `02_Spine.md` L82, L125; `03_Research.md` L163, L394; `04_Phase_02_Composition_and_Arrival.md` L75–L76, L205, L340; `04_Phase_07_Order.md` L55; `04_Phase_08_Making.md` L162; `04_Phase_09_Populations.md` L24; `05_Reconciliation.md` L177.

**Wording false as written.** `01_Inherited.md` L95–L99 states that the whole retention layer is immune to the census rebalancing; `05_Reconciliation.md` L177–L178 states that the ratios are unchanged and every ratio is invariant. Current fact: the two censuses carry different human and robot increments in the current rows (census L505 and L653, notes quoted in `SRY-001`), so retention and robot share take the values in the table above.

### SRY-003. Band, footprint, rock and ice shares, workforce

| Pass statement (topic) | Current value | Address |
|---|---|---|
| Distance of Census I from the one-million band line | **11.26% above** (112,600 people); Census II is **30.86% below** (308,629) | census L505, L653; computed |
| Required footprint at 10,000 and 7,000 per km² | **111.3 to 158.9 km²** (1,112,600 ÷ 10,000 = 111.26; ÷ 7,000 = 158.94) | computed |
| Cluster Census I (three Larsemann Hills cities) and Shirayuki's share | 3,330,740; Shirayuki **33.40%** | census L502, L505, L509; computed |
| Shirayuki's apportioned rock (~40 km² oasis, `ULM/Extent_and_Density_Per_City.md` §10) | **13.36 km²** (40 × 0.3340) | computed |
| Share of the footprint on rock / on ice | rock **8.4% to 12.0%**; ice **88.0% to 91.6%** (13.36 ÷ 158.94 = 8.41%; 13.36 ÷ 111.26 = 12.01%) | computed |
| Cluster density on the oasis | 3,330,740 ÷ 40 = **83,269 per km²** (the pass's ratio to its real-world comparable rests on a comparable figure the pass does not give; not recomputed) | computed |
| Workforce | **839,655** (352,970 + 97,337 + 389,348) | `16` L277; L1758–L1760 |
| Share of workforce in the pass's "25%", "20%" and "45%" tests, applied to the whole workforce | 25% = **209,914**; 20% = **167,931**; 45% = **377,845** | computed from 839,655 |
| The same percentages as file 16 applies them (to the distinctive tier of 486,685) | 25% = **121,671**; education 20% = **97,337** | `16` L1762, L1769 |

**Pass places.** Band: `00_Frame.md` L28–L33, L156–L160; `09.5_Log.md` L42. Footprint, rock and ice (and the oasis density): `00_Frame.md` L36, L40, L305, L366; `01_Inherited.md` L251, L351, L384; `02_Spine.md` L47–L49, L236–L261, L280; `03_Research.md` L48, L124, L234; `04_Phase_02_Composition_and_Arrival.md` L296; `04_Phase_03_Surface_and_Texture.md` L82–L83, L207; `04_Phase_04_Ordinary_Life.md` L48, L61; `04_Phase_06_Meaning.md` L58, L77; `04_Phase_07_Order.md` L61, L113; `04_Phase_08_Making.md` L252; `04_Phase_09_Populations.md` L288; `04_Phase_10_Catalog.md` L76, L224; `04z_Post-Ruling_Enrichment_Review.md` L72, L106, L109; `05_Reconciliation.md` L299; `07_QA_Gates.md` L166–L187 (pasted scan output); `09_Record.md` L98, L110; `10_Readiness_Check.md` L255; `09.5_Log.md` L22, L103, L147, L383, L408, L593, L923 (dated record). Workforce: `02_Spine.md` L60–L64, L79, L194; `03_Research.md` L368; `04_Phase_02_Composition_and_Arrival.md` L153; `04_Phase_04_Ordinary_Life.md` L44, L166; `04_Phase_07_Order.md` L32, L38–L40, L158; `04_Phase_10_Catalog.md` L223; `07_QA_Gates.md` L96; `09.5_Log.md` L408, L598, L754, L931 (dated record).

**Basis difference.** `04_Phase_07_Order.md` L38–L40 apply the arts and education percentages to the whole workforce; file 16 applies its sector percentages to the distinctive tier (`16` L1762, L1769). Both bases are in the sources as written.

### SRY-006. File 16's Shirayuki counts agree with its Half B row

`16` L1756–L1760: baseline 352,970 (42.0%), mandated 97,337 (11.6%), free 389,348 (46.4%); they sum to 839,655, equal to the Half B row at L277. L1762: distinctive tier 486,685 (58.0%); L1762–L1763 state the counts are recomputed on the current population with shares held, and name the added robot term (`SRY-011`). Pass places that quote the §16 counts: see the workforce list in `SRY-003` (`02_Spine.md` L60–L66, L79; `03_Research.md` L368; `04_Phase_04_Ordinary_Life.md` L44, L166).

### SRY-010. Composition: tier lists, shares and the number of origins (the population ruling of 2026-11-02, `DR-85`: every country in its latest-period form, the Sinian Federation reduced, tiers set from the final shares)

**Pass places.** Tier lists and counts: `04_Phase_02_Composition_and_Arrival.md` L40–L44, L184; `02_Spine.md` L123–L124, L132; `00_Frame.md` L311 (also the count of further nations). Japan's share and the remainder: `00_Frame.md` L311; `01_Inherited.md` L262–L282 (section `A4`), L376; `02_Spine.md` L123; `04_Phase_02_Composition_and_Arrival.md` L42, L53; `04_Phase_08_Making.md` L206, L318; `10_Readiness_Check.md` L78; `09.5_Log.md` L120, L475, L570, L596 (dated record). Statement that the largest foreign-origin group descends from the nation the founding refused: `01_Inherited.md` L217–L219; `02_Spine.md` L135.

**Current fact** (`Specs/Mirny subnet/Shirayuki.md`, tier list L44–L48, table L62–L99, rebuild note L54):

| Item | Value | Spec line |
|---|---|---|
| Rows in the table | 38 (1 Primary, 2 Significant, 35 Notable); shares sum to 99.989% | L62–L99 (computed) |
| Primary | Japan **34.20%**; the rest of the city, 100 − 34.20 = **65.80%** | L62 |
| Significant | Australia **9.65%**, Korea **9.10%** (0.55 points apart) | L63, L64 |
| Next rows | Sinian Federation **4.49%** (Notable; fourth-largest origin; 25,445 + 24,509 at Census I, 16,711 + 14,331 = 31,042 people at Census II), Germany 3.90%, Russia (core state) 3.53% | L65–L67 |
| The Sinian Federation's four detached pieces and Taiwan | Manchuria 0.26%, Mongolia 0.21%, East Turkestan 0.13%, Tibet 0.018% (sum 0.618%); Taiwan 2.86% as a separate row | table rows (computed) |
| Smallest Notable row | 0.018% | L99 |

`Upper_Earth_Immigration_Composition.md` L569 gives the same final composition (Primary Japan; Significant Australia, Korea; 35 Notable). Statements true to the sources and not in conflict: `04_Phase_02_Composition_and_Arrival.md` L42 names Japan as the Primary-tier founding population.

### SRY-011. Division of Industry shares and the robot-keyed term (`DR-97`, 2026-11-03: robot maintenance and robot sustenance added to file 16's formula)

**Current fact.** `16` L277 (Half B): Shirayuki workforce 839,655; baseline **42.0%**, mandated **11.6%**, free **46.4%**. `16` L1762: distinctive tier **58.0%**. `16` L1763: the baseline now includes robots × 15.75 ÷ 1,000 = 8,926 workers (566,709 × 0.01575 = 8,926.0, by command), as `09_Per_City_Baseline_Run.md` section 3.6 defines it. Ruling: `ULM/DEVELOPER_RULINGS_LOG.md` L1638–L1643 (`DR-97`) with the developer's confirmation *"that's right, robot maintenance and robot sustenance are both right"*. File 09 L78: required 297,848 of 839,655 = **35.5%**. File 09 L216: the two files agree on the robot term and differ on the food requirement (53 in file 09 section 2, 120.7 in file 16), "so the two baselines are not the same quantity".

| Pass place (topic) | Current fact |
|---|---|
| `04_Phase_04_Ordinary_Life.md` L43–L44; `02_Spine.md` L60, L316–L318 (statements that the percentages are ratios that do not move) | The shares take the values above (`16` L277). |
| `02_Spine.md` L82 (statement that the robot-keyed correction is pending) | The robot term is part of file 16's formula (`16` L1763; log L1638–L1643). |
| `02_Spine.md` L74–L75 (two baselines in the source) | File 09 L78 gives 35.5%; file 16 L277 gives 42.0%; the difference is explained at file 09 L216. |
| `02_Spine.md` L81 (difference between the baseline and a US comparable of about 29%) | 42.0 − 29 = **+13.0 points** (US comparable: `09` L146). |
| `04_Phase_10_Catalog.md` L134 (Capricorn compulsory-tier share) | **42.0%** (`16` L277). |

**Pass places that carry the share set** (baseline, mandated, free, distinctive): `00_Frame.md` L306; `02_Spine.md` L62–L66, L74–L75, L79–L82, L156–L157, L194, L260, L264, L278, L282; `03_Research.md` L368; `04_Phase_02_Composition_and_Arrival.md` L153; `04_Phase_04_Ordinary_Life.md` L43, L62, L166; `04_Phase_07_Order.md` L32; `04_Phase_08_Making.md` L181; `04_Phase_10_Catalog.md` L134; `08_Review_Panel.md` L57, L205; `09.5_Log.md` L91, L308, L588, L593, L598, L647 (dated record).

---

## D. Language

### SRY-012. The language rule of 2026-11-02 and 2026-11-03

**Pass places.** `04_Phase_08_Making.md` L198–L215 (section F; L206 derives the dominant local vernacular from Japan's Primary share), L404–L411 (`F.STOCK`); `04_Phase_09_Populations.md` L96 (the language row).

**Current fact.**
- `DR-89` (2026-11-02), developer, verbatim (`ULM/DEVELOPER_RULINGS_LOG.md` L1559 ff.): *"For all of the locations, the dominant language is always Hawaiian, which later becomes Tepenian. The next dominant language after that is whoever holds the majority."*
- `DR-85` (2026-11-02), developer, verbatim (log L1527): the Tepenian language is, *"down at its foundational level core, a Pidgin between English and Japanese"*.
- Supporting tier (2026-11-03, `CITIES/Research_Logs/Language_Sets_By_City_Reference_2026-11-03.md` L77): cutoff 12 percentage points from the largest group's mid-point, for every city. Shirayuki: largest group Japanese 34.2; no group within 5 or 10 points (L34); the 12-point table (L63–L73) lists no change for Shirayuki. The nearest groups are English 12.45 to 14.02 and Russian 6.09 to 15.30 (`Language_Blocs_By_City_2026-11-03.csv` L710, L709). The set for Shirayuki is Japanese alone.
- `Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md` L426 still reads that robot vernacular tracks the dominant local culture and the community who had her built.
- Status: "Not yet written into any culture file (window)" (Reference L80); the culture files named for the next window are listed at `CITIES/Research_Logs/ULM_Runs_Casey_Then_Mirny_Handoff_2026-11-03.md` L31 (the rule itself at L26–L28) and do not include Shirayuki.

---

## E. Names, citations and files

### SRY-004. Names in force

Four places named in the pass carry names that have since been ruled; the names in force are in `CITIES/City_Renames_Alias_Table_2026-10-03.md`. Pass places by role:

| Role of the place named | Pass places | Current name (alias table line; ruling) |
|---|---|---|
| The 38th city (named as a braced placeholder) | `00_Frame.md` L46, L325; `01_Inherited.md` L79; `04_Phase_02_Composition_and_Arrival.md` L240; `05_Reconciliation.md` L178; `07_QA_Gates.md` L237–L243, L249 (scan records) | **Relung Panen** (L12; `DR-39`) |
| The Mawson-subnet city on Highway 4 | `04_Phase_05_Relation_and_Geometry.md` L141 (a quoted route); `07_QA_Gates.md` L227 (scan pattern); `09.5_Log.md` L574, L710; `10_Readiness_Check.md` L78, L237 | **Temirötkel** (L10; `DR-37`); the junction is the Temirötkel Junction (L14) |
| The Halley-subnet city of the demographic tie | `04_Phase_05_Relation_and_Geometry.md` L86, L262; `09.5_Log.md` L720 | **Utstein** (L11; `DR-38`) |
| The plateau city of the kinship tie (each place names the city, not the district) | `04_Phase_05_Relation_and_Geometry.md` L82; `04_Phase_07_Order.md` L360–L361; `09.5_Log.md` L348; `09.6_Input_Audit.md` L60 | **Ariun Nuur** (L105; `DR-42`); the central scientific district inside it keeps the name Vostok (L107) |

Bharati is the name of the real station, a coordinate (Register L11–L13; spec L23). Names the alias table says it does not change are real stations and features (L15).

### SRY-007. Citations in `04_Phase_05` L82–L87

`04_Phase_05_Relation_and_Geometry.md` L82–L84 attribute to `Airports.md` the kinship tie to the plateau city and a quoted phrase about the neighbor that pushed for the Mountain Pass outpost; `09.5_Log.md` L348 attributes the tie to `Airports.md`. Current fact: `Infrastructure/Airports.md` **L18** (Mountain Pass row) contains "Zhongshan's tie runs to Kunlun, Shirayuki's to Ariun Nuur, and Sinheung's to BOTH", states the outpost began as an act pushed for by the Sinheung Institute of Cybernetics and Robotic Care, and contains the phrase "It had both reasons to push". The pass's parenthetical wording "the tier structures share an origin profile" (L82) is the pass's paraphrase; L18 says "The kinship is in the census". The same sentence about the three ties is in `CITIES/National_Medical_and_Care_Institutes.md` L109, with the Mountain Pass account at L97–L100 and a census table beside it (L102–L107). The place names differ from the pass's wording (`SRY-004`). L86–L87 describe the Utstein tie as unexplained in its source: `CITIES/City_National_Connections.md` L391–L392 (Shirayuki entry) gives "Both share genuine Japanese-heritage demographic presence", and L140–L142 (Utstein entry) gives its own reason.

### SRY-008. Runbook line numbers in the record

`10_Readiness_Check.md` L78 and L237 cite `00_RUNBOOK.md` "L2126–2131" and "L2129" for a restatement of two cities' demographic figures. Current runbook (`ULM/00_RUNBOOK.md`): L2128 is the heading of C.9c, L2130 the developer's quotation of 2026-09-06 about incorporating a nation's culture only after composition is established, L2140–L2146 the worked instance for Shirayuki and Sinheung (founders "per the Founding Register"). The runbook states no demographic percentage for any city (a search for 36.27, 34.20, 17.39 and 2.71 returns no hit). Read the two citations as pointers to the runbook's text at the time of the pass, not as live line numbers.

### SRY-013. Culture-file proposals in the pass docket

`05_Reconciliation.md` L170–L178 (table of the census figures in the culture file) and L326–L346 (docket rows 1–9, "proposed, not applied") rest on `CITIES/Local_Cultures/Mirny_Subnet/Shirayuki.md`. That file is the developer's file and is not edited by passes. Current sources for the docket's topics:

| Docket topic | Culture-file line | Current source |
|---|---|---|
| Census totals (row 1; L172–L175) | L9 | census L505, L653: 1,112,600 and 691,371 (`SRY-001`) |
| Polar night and midnight sun (row 2) | L48 | spec L157–L158: polar night about 49 days (May 29 to July 16), midnight sun about 62 days (November 22 to January 22) |
| Oasis shared with how many cities (row 6) | L42, L263 | `Extent_and_Density_Per_City.md` §10 and queue L579–L581: one ~40 km² patch shared by Shirayuki, Sinheung and Zhongshan; spec L221 also says "shared with Sinheung" |
| Real station's name in the landmark list (row 8) | L34, L100, L262 name the Bharati Station as infrastructure | Register L11–L13: the real station is a fact about infrastructure only; spec L23: the name does not carry forward into Tepenia |

### SRY-014. The pass README's state table

`README.md` L42–L46 describe Phase 9, `04z`, Phase 10, files `05` to `10` and the other two methods as not re-run, never written or not started. Current fact: the pass folder holds `04_Phase_09_Populations.md`, `04z_Post-Ruling_Enrichment_Review.md`, `04_Phase_10_Catalog.md` and files `05` to `10` (`ls`), and `10_Readiness_Check.md` L321–L322 reads "ULM COMPLETE FOR SHIRAYUKI. Steps −1 through 10. 22 files". `README.md` L80 describes the culture file as still unopened; `05_Reconciliation.md` L326 onward reconciles against it.

---

## F. Source defects (the sources disagree with themselves; no choice is made here)

### SRY-S04. Japan's share and the census total, stated differently inside the sources

| Source address | States | Its table or row |
|---|---|---|
| `Specs/Mirny subnet/Shirayuki.md` L35 (prose) | Japan **34.71%** | the table at L62 says **34.20%** |
| `Specs/Mirny subnet/Shirayuki.md` L321 (prose) | Japan **34.71%** | L62: **34.20%** |
| `Official_Population_Census.md` L422 (prose) | Japan **36.27%** | `Specs/Mirny subnet/Shirayuki.md` L62: **34.20%** |
| `Division_of_Industry/16_Per_City_Three_Tier_Run.md` L3180 | Japan **36.27%** | flagged by the banner at `16` L3580 (current share 34.20%) |
| `Local_Cultures/Mirny_Subnet/Shirayuki.md` L9 | Census I 1,178,313 and Census II 728,324 | census L505 and L653: 1,112,600 and 691,371 |

Other sources that quote shares from before the ruling of 2026-11-02 are listed in `CITIES/Sinian_Federation_Split_Scratch_2026-11-01/14_Downstream_Mentions.md` (`DR-94`, "Not decided" row).

### SRY-S05. Ruling label of the robot term

`16` L1 and L1763 and `09` L216 cite `DR-96` for the robot-keyed term (`09` L1 cites `DR-96` and `DR-97`). The rulings log records the term in `DR-97` (`ULM/DEVELOPER_RULINGS_LOG.md` L1638–L1643); `DR-96` (L1628) is a different ruling.

---

## G. Conclusions that rest on current inputs and may change on re-derivation

No verdict is stated. Each row gives the pass location, the input it rests on, and that input's current value.

| ID | Pass location | Input it rests on | Current value of the input |
|---|---|---|---|
| `SRY-C01` | `04_Phase_02_Composition_and_Arrival.md` L58–L71 (section A.2: the shape of the Significant tier and whether a second pole exists); `02_Spine.md` L123–L124, L132 (strength entry); `00_Frame.md` L311 | The Significant tier's members and shares; the number of origins | Significant: Australia 9.65, Korea 9.10; next row Sinian Federation 4.49; 38 origins (`SRY-010`). The 12 rows naming Russia (core state) or a Russian region sum to 9.07% (spec table, computed); `Language_Blocs_By_City_2026-11-03.csv` L709 gives a Russian language group of 6.09 to 15.30. |
| `SRY-C02` | `00_Frame.md` L28–L33 and the Reading A/B/C table (section 2), L156–L186 (the band choice, written at Band 4 and flagged `DRQ-10`) | Census I's distance from the one-million line | 11.26% above (112,600); Census II 30.86% below (`SRY-003`). `DRQ-10` is open (queue L551). |
| `SRY-C03` | `04_Phase_08_Making.md` L198–L215, L404–L411; `04_Phase_09_Populations.md` L96 (language reasoning; the register of keptness as a local speech marker) | The language rule; the Tepenian language's origin | `SRY-012`. |
| `SRY-U01` | `04_Phase_05_Relation_and_Geometry.md` L137–L152, L168–L198, L204–L209 (the supply line unloaded at a neighbor; the four-month window; the berthing queue) | The Ports file's Tri-Cities port section; the gateway rulings | `Infrastructure/Ports.md` L579 (section 5.6c) and the gateway distance table row L202 ("4,877 to 4,884 km ... Long haul, seasonal, shared"); Hobart is the primary gateway and three mainland Australian terminals carry bulk freight (`DR-49`, log L995). |
| `SRY-U02` | `04_Phase_06_Meaning.md` L166–L181 (death and ossuaries); `00_Frame.md` L326 (mortuary question) | The ossuary rulings | `Robot_Physiology_and_Cultural_Practices.md` L75–L103: a Tepenian ossuary holds robots' metal bones and the bones of the humans who loved them (ruled 2026-09-07); metal bone persists, calcium bone reduces. The mortuary question is deferred corpus-wide (pass `00_Frame.md` L326). |
| `SRY-U03` | `04_Phase_07_Order.md` L360–L361 (the plateau city's Japanese-Primary tier, used for a kinship tie) | Japan's tier at the plateau city | `National_Medical_and_Care_Institutes.md` L104–L107 table: Ariun Nuur is Primary in the Japanese column. The Shirayuki–Utstein tie text: `SRY-007`. |
| `SRY-U04` | `04_Phase_08_Making.md` L318–L410 (origin-stock addendum: the stock is Japanese; no term is coined) | Japan's tier and share; the language rule | Japan Primary 34.20% (spec L62); Register names Japan (L61); `SRY-012`. |

---

## H. Open questions for the developer

1. **Band.** Census I is now 11.3% above the one-million line and Census II 30.9% below it. Which band does a city get when its two censuses fall on different sides? (`DRQ-10`, queue L551, open.)
2. **The oasis rock.** One patch of about 40 km² of ice-free rock is shared by three cities; Shirayuki's apportioned part is 13.36 km². Who allocated it, or did nobody? (`DRQ-11`, queue L579, open.)
3. **Which sources may ground a finding.** The list of source folders treated as ratified has two entries; the picks list and the symbol files fall outside it. (`DRQ-12`, queue L614, open.)
4. **Rock-founded or on ice.** File 16 classes the ground as rock-founded (`16` L1758) while the extent arithmetic puts 88.0% to 91.6% of the footprint on ice. Is the difficulty coefficient set from the site or from the footprint? (`DRQ-13`, queue L656, open.)
5. **Grouping of the Russian-named rows** (`SRY-C01`): counted as one origin or as separate rows. The spec table gives twelve rows summing to 9.07%; the language-group file gives 6.09 to 15.30.
6. **Source defects** (`SRY-S04`, `SRY-S05`): the spec prose, the census prose at L422, file 16 L3180, the culture file's census line, and the ruling label. These sources are not edited by this note.

**Decisions pending elsewhere that touch Shirayuki.**
- How the language rule enters a finished pass: the rule is set (`SRY-012`) and is written first into the culture files named in the handoff; no instruction covers finished passes.
- Pre-Trip and datasheet files for Shirayuki, and the fresh analysis of the finished cities: open items (`D-2`).
- The culture-file proposals of the pass docket (`SRY-013`) stay unapplied until the developer takes up the culture file.

---

## I. Sources checked with no mismatch found

- Founding Register row: `Founding_Register.md` L61 (`SRY-005`).
- Tri-Cities airport with Shirayuki as a host: `Infrastructure/Airports.md` L13; pass `04_Phase_05_Relation_and_Geometry.md` L130.
- Shirayuki about 8 km from the Tri-Cities port on a different landform: `Infrastructure/Ports.md` L611; pass `04_Phase_05_Relation_and_Geometry.md` L26, L29.
- Symbol assignment Uranus / Air: `CITIES/City_Symbolic_Substrate/City_Symbol_Assignments.md` L117; pass `04_Phase_10_Catalog.md` L204.
- Polar night and midnight sun: spec L157–L158, L188.
