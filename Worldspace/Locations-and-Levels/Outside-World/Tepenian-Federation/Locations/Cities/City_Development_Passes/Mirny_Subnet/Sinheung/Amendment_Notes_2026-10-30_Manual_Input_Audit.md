# Sinheung: amendment notes (current as of 2026-11-03)

**What this is.** A record of where Sinheung's ULM pass text does not match the sources as they stand on 2026-11-03, and what those sources say. It states only the present; the pass stays the dated record of what it worked from.
**No pass file is edited by this note, and none is.** Pass passages are pointed at by file, line and a neutral topic description, found by searching the pass files for each topic (not by reading every line), so an unlisted passage may exist; `09.5_Log.md` is a dated record, searched but not listed line by line.
**How entries are built.** Pass location, then the current fact, then its source address (file and line). Derived figures are recomputed by command on 2026-11-03. Entry IDs keep their numbers because other files cite them; new entries are `SNH-010` onward.
**The pass.** Run and closed in September 2026 (files dated 2026-09-07, committed 2026-09-13); the last edit to a pass file (the audit fixes) is 2026-10-01. The folder has no Pre-Trip and no datasheets.
**Live files read:** Spec 269 lines, Census 892 lines. Where two live sources disagree, both values and both addresses are given and nothing is chosen.

**Source key** (all under `Worldspace/Locations-and-Levels/` unless stated). Cities folder = `Outside-World/Tepenian-Federation/Locations/Cities/`. **Spec** = Cities `Specs/Mirny subnet/Sinheung.md`. **Census** = Cities `Official_Population_Census.md`. **Register** = Cities `Founding_Register.md`. **`16`** / **`09`** = Cities `Division_of_Industry/16_Per_City_Three_Tier_Run.md` / `09_Per_City_Baseline_Run.md`. **Rulings log** = `Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md`. **Extent** = `Universal_Location_Methodology/Extent_and_Density_Per_City.md`. **Ledger** = `Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/FIX_LEDGER.md`. **Walk-through** = same folder, `Walkthrough_Decisions.md`.
**Rulings named below:** `DR-19` (a founding nation stands on geography and access, never on the real station) · `DR-25`/`DR-26` (a station hands down records, research, equipment and techniques, not a tradition; 2026-10-01) · `DR-44` (the remaining founding rows ruled, 2026-10-03) · `DR-68` (the Santa Luce population scenario, 2026-10-28) · `DR-85` (the 2026-11-02 population ruling: every country in its latest form, the Sinian Federation's share reduced and refilled, tiers relabeled) · `DR-90` (Esperanza cut to 1,200,000 and the difference spread over other cities, 2026-11-02) · `DR-97` (the robot maintenance and sustenance term added to file `16`, 2026-11-03).

---

## 1. Standing decisions (rules in force for this pass)

Developer, at the walk-through of Sinheung's audit, 2026-10-30: *"yup, all as recommended."* (`Walk-through` L216-218; the same answer is entered in the Ledger at L1501-1517.) It is the authority for `SNH-010` and `SNH-S01` to `SNH-S04` below. **None of these is in the Rulings log** (searched for "all as recommended", "SNH-" and "Manual_Input_Audit": the Rulings log has no Sinheung entry for them); they are recorded in the Walk-through, the Ledger and this note.

### SNH-010. This pass is never edited; findings are filed beside it
Rule for this city (Ledger L1496): the pass files are never edited; each finding is filed as an amendment note beside the pass; the pass is a dated record. The Rulings log states the same for finished passes at L1520. No Pre-Trip or datasheet set exists for this city (`Walk-through` L218). Planned, not started: create the Pre-Trip and datasheets (`Dev-Road-Map/Weekly_To-Do_-_Current.md` L65) and re-analyze the finished cities with the current methods, with the amendment notes as the interim record (same file L67; `Walk-through` L211).

### SNH-S01. The spec's identity line names "Soyuz"
`Spec` L4 names "Soyuz" as the working label tied to the physical station's Russian namesake, states that the city's founders did not choose it, and gives the city's name as Sinheung (신흥, 新興), official since 2026-07-14 (also L215). The pass proposes this correction at `00_Frame.md` L122-130 and `05_Reconciliation.md` L181-182; the Spec carries it. Applied 2026-10-30 (`Walk-through` L227; Ledger L1514).

### SNH-S02. The spec's climate source line names the Zhongshan READER series
`Spec` L154: the monthly Mean column is the BAS READER "Zhongshan" surface series, 1991-2020; Progress Station (AARI, Russia) is the site's real-world basis. L200 gives the column provenance. Applied 2026-10-30 (`Walk-through` L228; Ledger L1515). Figures: `SNH-005`.

### SNH-S03. The census tier list for Sinheung matches the spec's
`Census` L416-418 and `Spec` L76-78 are identical (checked by `diff`): Primary: Korea. Significant: Japan, Germany, Sinian Federation. Notable: 35 rows, Indonesia first, Tuva last. Applied 2026-10-30 (`Walk-through` L230; Ledger L1516). The composition behind the lists: `SNH-012`.

### SNH-S04. The Extent snapshot rows are left as dated records
`Extent` L620 (the 25-city snapshot table dated 2026-09-05) and L657 (the minus-10-percent discharge scenario) are left as they stand; developer decision at the walk-through (Ledger L1517 "LEFT 2026-10-30 (developer)"; `Walk-through` L231). `Extent` L631 states the table is the dated record and the census is the live source. Live need for Sinheung: `SNH-011`.

---

## 2. Population and workforce

### SNH-001. Census totals and the human/robot split
**Pass locations (totals and counts):** Census I and II combined: `00_Frame.md` L37, L191; `05_Reconciliation.md` L22, L91. Census I combined: `01_Inherited.md` L186; `04_Phase_07_Order.md` L81; `07_QA_Gates.md` L171; the density division at `02_Spine.md` L247-248. Human and robot counts: `04_Phase_04_Ordinary_Life.md` L35; `04_Phase_07_Order.md` L50; `04_Phase_08_Making.md` L31; `04_Phase_09_Populations.md` L32-33; `05_Reconciliation.md` L91; `07_QA_Gates.md` L171. Human/robot share lines: `04_Phase_09_Populations.md` L32-33, L43; `07_QA_Gates.md` L172.

| | Humans | Robots | Combined | Source |
|---|--:|--:|--:|---|
| Census I | 494,341 | 520,192 | **1,014,533** | `Census` L509; `Spec` L71 |
| Census II | 410,746 | 424,595 | **835,341** | `Census` L647; `Spec` L72 |

Census I shares (computed): robots 51.27%, humans 48.73%. Both rows carry the −10% ruling of 2026-09-05, the `DR-68` scenario and the `DR-90` relocation, and the census labels the last two "Arithmetic, NOT a migration" (L509, L647); `Spec` L71-72 labels the whole as "An authoring adjustment, NOT an event".

### SNH-002. Retention, Census II as a share of Census I
**Pass locations:** `02_Spine.md` L105-108; `04_Phase_09_Populations.md` L84-86, L115, L117, L123, L188-189, L394; `07_QA_Gates.md` L41, L176. The reasoning built on them: `SNH-C1`.

| | Census II ÷ Census I | Result |
|---|---|--:|
| Humans | 410,746 ÷ 494,341 | **83.09%** |
| Robots | 424,595 ÷ 520,192 | **81.62%** |
| Combined | 835,341 ÷ 1,014,533 | **82.34%** |
| Humans minus robots | | **+1.47 points** |

**The ratio-preservation check.** `02_Spine.md` L110-114 describes a check that the 2026-09-05 percentage cut preserved the human/robot ratios. The census rows now also carry two later additions: Census I +14,930 humans and +13,271 robots (`Census` L509; ratio 1.125 against the city's humans-to-robots ratio of 0.950) and Census II +8,570 and +11,462 (`Census` L647; ratio 0.748 against 0.967). Ratios computed by command.

### SNH-003. Workforce and required work
**Pass locations:** `04_Phase_04_Ordinary_Life.md` L25, L35; `04_Phase_07_Order.md` L49-51; `07_QA_Gates.md` L173; `09.5_Log.md` (several entries). The statements that per-city headcounts in the Division of Industry folder predate the census ruling: `09_Record.md` L69; `04_Phase_07_Order.md` L22-25.

Workforce (robots plus half the humans): 520,192 + 247,170.5 = **767,362.5**, printed **767,363** at `16` L257 and `09` L80 (both agree). Required work **271,073**, 35.3% of the workforce (`09` L80; 271,073 ÷ 767,363 = 35.33%); `16` L30 states that `09` is superseded as a result and kept as an input. `16` L1 states that Half B's workforce, base, mandated and free cells carry the refresh of 2026-10-28 (`DR-68`) and that the robot term is part of Half B and of all 35 city sections from 2026-11-03.

### SNH-004. The three-tier split: two live places disagree (source defect)
**Pass locations using the split:** `04_Phase_04_Ordinary_Life.md` L36-38, L47-48, L52, L130, L237; `04_Phase_05_Relation_and_Geometry.md` L153; `04_Phase_07_Order.md` L25, L27, L559; `04_Phase_08_Making.md` L30; `07_QA_Gates.md` L174. **Pass statements that the city has no per-city determination in `16`:** `04_Phase_04_Ordinary_Life.md` L42; `04_Phase_07_Order.md` L33, L41; `09_Record.md` L99.

`16` holds a determination for this city: **section 17, "SINHEUNG — DETERMINED", L1834** (the heading's spelling with E is why a search for "Sinheung" misses it; its mandate follows ruling C of 2026-09-02, L1846).

| Source | Workforce | Baseline | Mandated | Free |
|---|--:|--:|--:|--:|
| Half B row, `16` L257 | 767,363 | 41.8% | 26.2% | 32.0% |
| Section 17, `16` L1838-1840 | 767,363 (321,100 + 211,975 + 234,288) | 321,100, printed 41.9% | 211,975, printed 27.6% | 234,288, printed 30.5% |

**The two do not agree on any of the three tiers, and no source says which one the pass should use.** Computed from section 17's own counts: 41.845% / 27.624% / 30.532%, so its printed baseline (41.9%, L1838) and distinctive share (58.1%, L1842) differ from its counts at one decimal (41.8% and 58.2%). Arithmetic observation, no choice made: Half B's 26.2% equals fabrication alone (200,818 ÷ 767,363 = 26.17%), while section 17's 27.6% is fabrication plus the Institute's half of Education/other (200,818 + 11,157 = 211,975, `16` L1850-1852).
**Further defects inside section 17:** its table gives fabrication 200,818 and the Institute half 11,157 (L1850-1851), while the sentence at L1856 gives 216,171 for the fabrication sector and the sentence at L1894 gives 12,010 for the Institute; `16` L1 states that the narrative sentences that quote other figures are left as they stand. `16` L1 and L1844 cite `DR-96` for the robot term; the Rulings log records the robot-keyed requirement as `DR-97` (L1638), and `DR-96` (L1628) is a different ruling.

### SNH-011. Land the city would need, and the oasis area
**Pass locations:** `00_Frame.md` L38, L158, L162; `02_Spine.md` L27-28, L136, L247-256; `03_Research.md` L341; `04_Phase_03_Surface_and_Texture.md` L105; `04_Phase_04_Ordinary_Life.md` L169; `04_Phase_05_Relation_and_Geometry.md` L168, L248; `07_QA_Gates.md` L65, L175.
Census I 1,014,533 needs **101.45 km²** at 10,000 people per km² and **144.93 km²** at 7,000 (computed; 101 and 145 rounded). Live sources give the Larsemann Hills' ice-free area as about **40 km²**, shared by three cities (`Extent` L594, L613; `Census` L754; `Division_of_Industry/12_Terraforming_and_the_Outdoor_Tier.md` L258). On 40 km² the density is 25,363 people per km² (1,014,533 ÷ 40, computed). I found no live source giving 34 km² for the Larsemann Hills; the pass's range has 34 as its low end (`02_Spine.md` L247-252), so its source is not confirmed.

---

## 3. Composition and tier labels

### SNH-012. The composition table and the tiers
**Pass locations (nations and tier membership):** `00_Frame.md` L178-182; `02_Spine.md` L96-98; `04_Phase_02_Composition_and_Arrival.md` L10, L22-24, L54-67, L136-142, L156; `04_Phase_08_Making.md` L62-65; `04_Phase_09_Populations.md` L466; `05_Reconciliation.md` L82; `04_Phase_07_Order.md` L541. **Count of origin entries:** `00_Frame.md` L178; `02_Spine.md` L96, L123; `04_Phase_02_Composition_and_Arrival.md` L10, L136, L142, L156; `04_Phase_07_Order.md` L541. **The founding nation's share:** `01_Inherited.md` L148, L158; `02_Spine.md` L96, L124; `04_Phase_02_Composition_and_Arrival.md` L22, L62; `04_Phase_04_Ordinary_Life.md` L159; `04_Phase_08_Making.md` L62, L396; `04_Phase_09_Populations.md` L57, L292, L311, L331; `04_Phase_07_Order.md` L541. **Docketed tier-versus-share item:** `00_Frame.md` L180, L184-185; `01_Inherited.md` L213; `02_Spine.md` L97-98; `04_Phase_02_Composition_and_Arrival.md` L23-24, L193; `05_Reconciliation.md` L183; `09_Record.md` L77.

Current (`Spec` L92-130, rule at L132):
- **39 rows**, shares summing to 99.992% (computed). Tiers: Primary 1 row, Significant 3 rows, Notable 35 rows.
- **Primary: Korea 33.00%** (L92). The row is Korea as a whole, South and North Korea together (`Census` L878). So the share of the rest of the city is 67.00%.
- **Significant:** Japan 9.40% (L93), Germany 8.75% (L94), Sinian Federation 5.45% (L95); the Sinian Federation row includes Hong Kong and Macau (`Census` L877).
- **Notable:** Indonesia 3.99% (L96), Australia 3.37%, Thailand 3.34%, Estonia 3.32%, Hungary 3.23%, Lithuania 2.93%, Taiwan 2.86%, Malaysia 2.76%, Idelsk-Uralia 2.03%, Russia (core state) 2.03%, Vietnam 1.84%, Philippines 1.67%, Kazakhstan 1.45%, Bulgaria 1.37%, Austro-Bavaria 1.31%, Latvia 1.27%, South Africa 1.16% (L97-112), then 18 rows below 1% (L113-130).
- The tier rule (`Spec` L132): Primary and Significant end at the largest ratio gaps among rows at 4.5% or more; no row at 4.5% or more is Notable. The lowest Significant row (5.45%) is above the highest Notable row (3.99%), so the table has no tier-versus-share inversion.
- `Census` Section E (L857) lists thirteen names under Russia, and all thirteen are rows here: Idelsk-Uralia (L104), Russia (core state) (L105), Siberia (L113), Donska-Kubania (L114), Künnarantaiga (L115), Dagestan (L119), Chechnya (L123), Kabardino-Balkaria (L124), North Ossetia-Alania (L125), Finland (L127), Ingushetia (L128), Karachay-Cherkessia (L129), Tuva (L130). Together 6.47% (computed); Kazakhstan is a separate row at 1.45% (L108; `Census` L881), and the two together make 7.92%.
- **Authoring changes recorded in the spec** (`Spec` L84): successor states and renamed countries, the Sinian Federation's decline and refill, places added by time-zone window, and Kazakhstan (`DR-93`) and Manchuria (`DR-94`) adjustments, all stated as authoring, not events. The pass's guard against writing a migration (`04_Phase_02_Composition_and_Arrival.md` L179-184, three authoring absences listed) covers three adjustments; `Spec` L84 lists more.
- Absences stated by the pass as in-world: `04_Phase_02_Composition_and_Arrival.md` L165-178 (E.1, E.2). `Spec` L92-130 has no row for any Western Hemisphere nation, South Asian nation, the United Kingdom, Ukraine, Belarus or Romania (checked by reading the 39 rows).

---

## 4. Climate

### SNH-005. Mean column, range line and the READER file
**Pass locations:** `00_Frame.md` L164 (the temperature-range line); `04_Phase_03_Surface_and_Texture.md` L123 (the deep-winter row), L148-153 (the monthly table's Mean column), L158 (the sentence about the two warmest months); `07_QA_Gates.md` L95 (a quoted range line). The pass treats `READER/Sinheung.md` as incomplete at `04_Phase_03_Surface_and_Texture.md` L8-36 and `05_Reconciliation.md` L188.

Current (`Spec` L181-192, L154-160, `Reference/Real-World/Climate Data/READER/Sinheung.md` L3-15), °C, 1991-2020:

| Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | Annual |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| +0.2 | −2.9 | −8.3 | −13.1 | −15.2 | −14.6 | −16.1 | −16.1 | −15.4 | −12.0 | −4.8 | −0.5 | −9.9 |

The annual value is the mean of the twelve (computed, −9.9); the READER file L8 gives −9.9, `Spec` L157 gives "approximately −10°C" and L175 "-10.0 °C". The range line (`Spec` L160) reads "coldest months avg −16°C; warmest month avg 0°C". The READER file (17 lines) names Zhongshan as the proxy station (L3-5). The daily-crossing columns (`Spec` L181, L182, L192): Dec average high +2.8, low −2.1; Jan +3.3, −1.6; Feb 0, −4.6.

---

## 5. Founding

### SNH-006. The Founding Register row and the rules behind it
**Pass locations stating or citing the founding:** `00_Frame.md` L87, L197, L200, L226; `01_Inherited.md` L27; `02_Spine.md` L57; `03_Research.md` L342; `04_Phase_02_Composition_and_Arrival.md` L94; `04_Phase_03_Surface_and_Texture.md` L104; `04_Phase_05_Relation_and_Geometry.md` L90, L227, L278; `04_Phase_07_Order.md` L236; `04_Phase_09_Populations.md` L317-320 (quotation of the developer's `§C.9c` ruling); `04_Phase_10_Catalog.md` L116; `05_Reconciliation.md` L74; `09.6_Input_Audit.md` L150-152 (the same quotation); `09.5_Log.md` L71, L352, L383, L401. Passages that cite the Register: `04_Phase_05_Relation_and_Geometry.md` L227, L278; `09.5_Log.md` L401.

**The live row** (`Register` L62; columns at L36), quoted exactly: *Sinheung | Mirny | +5 | ✅ | Korea, by the Jeju-do court's diplomatic allocation | The Jeju-do court's diplomatic allocation, **and, in addition, geography**: zone gap 3 to the Prydz Bay coast (the edge of the rule). Developer: geography is an *additional* factor, not a replacement. | `Specs/Mirny subnet/Sinheung.md` L215; `DR-44` | —*. The Register's change log (L90) records the same ruling.
**The standing rule, `DR-44`** (Rulings log L919, verbatim, 2026-10-03): *"for Shirayuki and Sinheung … I would change that to geography being an additional factor, on top of the agreement at the Court of Jeju-Do"*; the ruling row (L930) reads "Japan and Korea stay, by the Jeju-do court's diplomatic allocation, with geography (zone gap 3 to the Prydz Bay coast) as an ADDITIONAL factor on top of it. Not a rewrite of the basis." Recorded in the Rulings log.
**The standing rules, `DR-19`** (2026-09-30; Rulings log L538, L552): a founding nation is legitimate on geography and access; a real station's operator is a GPS coordinate only and never a reason. `Register` L8-10: founders are decided in the Register and nowhere else, and no ULM pass may originate or restate a founding claim the Register does not hold; they point to it. `Register` L11-13: a founding nation stands on geography and access, never on the real station. `Register` L14: state each founding on the city's own geography and access, never by comparison to another city (developer, 2026-10-01).
**Source defect (small):** the Register's source cell cites `Spec` L215; the spec's "Founding population" line is L213 (L215 is the paragraph about the name "Soyuz").

### SNH-013. The claim that the allocation covers "only two" cities
**Pass locations:** `00_Frame.md` L87; `01_Inherited.md` L27, L29, L207; `02_Spine.md` L41, L209.
Neither `Spec` nor the culture file contains that claim (searched for "only two"). The Register rows whose Basis names the Jeju-do court's allocation are two: Shirayuki (L61) and Sinheung (L62). `Spec` L150 states that the sites of three Larsemann Hills cities come from the same Jeju-do arrangement, naming Zhongshan with this city and Shirayuki; `Register` L60 gives Zhongshan's basis as geography (`DR-21`). The spec and the Register do not agree on how many sites the allocation covers.

### SNH-007. The spec's identity line
**Pass locations:** `00_Frame.md` L122-130; `05_Reconciliation.md` L181-182 (the proposed correction of the spec's identity line). Current fact and source: `SNH-S01` (`Spec` L4). Nothing in the pass depends on this beyond the proposal, which the spec carries.

### SNH-014. The spec's wording about the station's infrastructure
**Pass locations:** `00_Frame.md` L202-207 (the pass flags one phrase of the spec's Founding paragraph); `05_Reconciliation.md` L57-85 (C.1, the proposed corrections concerning the culture file's identity and one clause).
Current: `Spec` L211 states that Korean exiles settled the site "inheriting Russian-built polar research infrastructure, but never a Russian founding claim", and that Russia is not a party to the Jeju-do court; `Spec` L3 calls the station's builder "physical infrastructure only, a GPS fact". The rulings that govern what a city may inherit from a station: `SNH-U3`.

---

## 6. Names, paths and addresses

### SNH-008. City names in the pass
**Pass locations:** `00_Frame.md` L210; `04_Phase_05_Relation_and_Geometry.md` L225, L228; `01_Inherited.md` L32; `09.5_Log.md` L395, L401. At these addresses the pass uses names that `Cities/City_Renames_Alias_Table_2026-10-03.md` maps to the current names: **Temirötkel** (L10), **Utstein** (L11), **Contrapunto** (L104), **Ariun Nuur** (L105; the central scientific district inside Ariun Nuur keeps the name "Vostok", L107, and the real station and lake keep their own names). `Spec` L8 gives the Hwy 4 route as Temirötkel → Mawson → Sinheung → Shirayuki.

### SNH-009. The spec path
`README.md` L51 gives `Specs/Mirny subnet/Sinheung.md`, and every absolute path in the README resolves (checked by command). Six pass lines cite the shorter path `Specs/Sinheung.md`, which does not exist: `00_Frame.md` L24, L122, L278; `01_Inherited.md` L222; `04_Phase_03_Surface_and_Texture.md` L216; `04_Phase_06_Meaning.md` L244. The spec is at `Cities/Specs/Mirny subnet/Sinheung.md`.

### SNH-015. Where the Robot Universals chapters are
**Pass locations:** `09.6_Input_Audit.md` L32, L43, L64-65, L86; `04_Phase_09_Populations.md` L95, L98, L147; `05_Reconciliation.md` L95; `07_QA_Gates.md` L191. The pass cites the folder in the Timeline repo; that folder is not in the Timeline repo's `Reference/` (only `Robot_Universals_Summary.md` is). The chapters are at `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Characters/Robot-specific/Robot_Universals/3_-_Part_III_Robot_Cultural_Universals/`: chapter 13 (`13_City-Locality_as_the_Seat_of_Identity/README.md`, the sentence on "same city, same struggles" at L35) and chapter 14 (`14_Generational_Identity_-_Gen-Mark_as_Real_but_Non-Hierarchical/README.md`, the sentence on fabrication chambers at L29). Both quoted passages are present there.

### SNH-016. The culture file the pass read last
`Cities/Local_Cultures/Mirny_Subnet/Sinheung.md` (282 lines) is an input, not a pass file. At these addresses it carries the topics the pass docketed at Step 5: a census line with city-size ranks (L9) and a rank clause (L109), which do not match `Census` L509 and L647; sentences naming other cities (L44, L109, L196); identity and founding-tension wording that refers to the station (L12, L60-66, L101); and a tier-membership list (L186) that does not match `SNH-012`. L90 gives Korea 33.00% and calls Korean "the city's sole public language", and L135 calls Korean "the dominant public language"; see `SNH-U2`.

---

## 7. Conclusions that rest on current inputs and may change on re-derivation

No verdict is stated. Each row gives the pass location, the input it rests on and that input's current value.

| ID | Pass location | Topic | Input | Current value and address |
|---|---|---|---|---|
| SNH-C1 | `02_Spine.md` L116-119; `04_Phase_09_Populations.md` B.1 L74-124, B.2 L178-191, L392, L394 | The explanation offered for the difference between robot and human retention | Census I and II rows | Humans 83.09%, robots 81.62%, difference +1.47 points (`SNH-002`); the census labels later additions "Arithmetic, NOT a migration" (`Census` L509, L647) |
| SNH-C2 | `04_Phase_02_Composition_and_Arrival.md` A.2 L47-72 (pooled-cluster table L54-67); `04_Phase_09_Populations.md` C.3 L290-337; `04_Phase_08_Making.md` L62-64; `04_Phase_07_Order.md` L541 | Whether the largest origin cluster is a plurality or a majority, and the bloc question | Pooled share of the East Asian cluster | Korea 33.00 (`Spec` L92); Korea, Japan, Sinian Federation 47.85 (L92, L93, L95); with Taiwan 50.71 (L102); with Manchuria 0.34, Mongolia 0.25, East Turkestan 0.17, Tibet 0.025 (L116-118, L126) 51.50. The sources do not say which pieces form the cluster. |
| SNH-C3 | `04_Phase_02_Composition_and_Arrival.md` A.4 L91-103 | The nation nearest by reach against the founding nation | Shares of the nearest-zone nations | Russia (core state) 2.03% (`Spec` L105); Idelsk-Uralia 2.03% (L104); Kazakhstan 1.45% (L108); the thirteen Russia rows together 6.47% (`SNH-012`); Korea 33.00% (L92). The spec table has no UTC column. |
| SNH-C4 | `04_Phase_08_Making.md` A.3 L60-99 and 8f F.1-F.2 L389-414 | Which origin clusters carry preservation practices; the starting stock named | Cluster composition | Significant rows Japan 9.40, Germany 8.75, Sinian Federation 5.45 (`Spec` L93-95); Notable rows as in `SNH-012` |
| SNH-C5 | `04_Phase_04_Ordinary_Life.md` L52-53, L94, L202; `04_Phase_08_Making.md` L30; `04_Phase_09_Populations.md` L190 | The figure given for unclaimed working life | Free share of the workforce | 32.0% (`16` L257) and 30.5% (`16` L1840); the two disagree (`SNH-004`) |
| SNH-U1 | `00_Frame.md` L37, L88, L98; the line-3 header of `04_Phase_02`, `_03`, `_04`, `_05`, `_06`, `_08`, `_09` and `_10`; `04_Phase_02_Composition_and_Arrival.md` L47; `04_Phase_04_Ordinary_Life.md` L168; `09_Record.md` L11 | The population band the pass declares | Census totals against the band edge | Census I 1,014,533, Census II 835,341 (`SNH-001`); band edge: question 1 below |
| SNH-U2 | `04_Phase_08_Making.md` 8f L389-414 | Whether an origin language dominates or marks identity; the pass does not mention the national language | The language rule | `SNH-U2a` below |
| SNH-U3 | `00_Frame.md` L202-207; `05_Reconciliation.md` L57-85 | Station lineage treated as inadmissible; "the plant and not the roots" (`00_Frame.md` L207) | Rulings on inheriting from a station | `DR-25` (Rulings log L634): records, logs, journals, manifests, maps and infrastructure can be inherited, a tradition cannot. `DR-26` (L654), verbatim, 2026-10-01: *"it's perfectly possible for newcomers to inherit the research, equipment, techniques, results, etc. That doesn't need to get thrown away"*; not inheritable: a tradition, and the station's operator or nation as a reason for the city's founders, identity, culture or ties. |
| SNH-U4 | `04_Phase_05_Relation_and_Geometry.md` L136-140, L161-168, L225 | Where the city's imports come from | Port and transshipment listings | `Locations/Infrastructure/Ports.md` L130 and `Locations/Infrastructure/Neutral_Transshipment_Hubs.md` L60 list the Tri-Cities among the beneficiaries of the French Southern Lands and Heard Island transshipment, with indirect access to Australian and South African supply (developer ruling 2026-09-16); the Nella Fjord port row is `Ports.md` §5.6c. |

**SNH-U2a. The language rule** (set 2026-11-03; `Research_Logs/ULM_Runs_Casey_Then_Mirny_Handoff_2026-11-03.md` L25-30, `Language_Sets_By_City_Reference_2026-11-03.md` L75-79): Hawaiian (later Tepenian) is the dominant language everywhere; a city's supporting-tier languages are every language group within 12 percentage points of its largest group (mid-points; nations sharing a language summed); the cutoff is 12 points for every city. For Sinheung the largest group is Korean 33.00%, then German 10.06%, Japanese 9.40%, Mandarin 8.65-9.10% (`Language_Blocs_By_City_2026-11-03.md` L1110-1113), so the set at 12 points is **Korean alone** (the reference table shows none within 5 or 10 points, L35). The rule is "not yet written into most culture files" (Handoff L25).

---

## 8. Open questions for the developer

1. **Which census sets the population band?** Band 4 is about 50,000 to 1,000,000 people and Band 5 about 1,000,000 to 50,000,000 (`Universal_Location_Methodology/01_Frame_Typology_and_Inheritance.md` L180-181; the 4-to-5 threshold, "above roughly a million", L216-218). Sinheung's Census I total (1,014,533) is above that edge and its Census II total (835,341) is below it. The runbook's Census I convention (`00_RUNBOOK.md` L1724-1729) covers process-derived figures; I found no rule there naming which census sets the band. The pass declares Band 4 (`SNH-U1`).
2. **Do the station-heritage rulings of 2026-10-01 change what the pass treats as inadmissible?** The pass keeps the physical plant and leaves out the station's lineage (`SNH-U3`). `DR-26` now lets a city inherit the station's research, equipment, techniques and results (and `DR-25` its records). Should a re-derivation use those as inputs?
3. **Which three-tier split is the figure for Sinheung,** Half B's 41.8 / 26.2 / 32.0 or section 17's 41.9 / 27.6 / 30.5 (`SNH-004`)? Should the narrative sentences inside section 17 be brought into line with its table?
4. **Which nations form the East Asian cluster** when its share is pooled (`SNH-C2`)?
5. **Which figure is the Larsemann Hills' ice-free area:** about 40 km² (`SNH-011`)?

## 9. Decisions pending elsewhere that touch Sinheung

- **The language rule's entry into a finished pass.** The rule (`SNH-U2a`) is "not yet written into most culture files" (Handoff L25-30). Whether and how it enters a finished pass such as this one is not decided; the culture file's wording on Korean is at L90 and L135 (`SNH-016`).
- **Re-analysis of the finished cities and the missing Pre-Trip and datasheets:** to-do, not started (`Dev-Road-Map/Weekly_To-Do_-_Current.md` L65, L67; `SNH-010`).

---

*Filed 2026-10-30 at the developer's direction (*"yup, all as recommended."*); current as of 2026-11-03. Record of the sweep: `Manual_Input_Audit_2026-10-29/Sweep_Reports/Finished_Cities_Sweep.md`. Drift review that located the open items: `Cities/Research_Logs/Drift_Review_Sinheung_2026-11-03.md`.*
