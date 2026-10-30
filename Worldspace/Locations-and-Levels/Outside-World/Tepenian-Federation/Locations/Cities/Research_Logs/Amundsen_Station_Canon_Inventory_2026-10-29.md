# Amundsen Station: canon inventory (Unit A1, evening wave 2026-10-29)

**Brief:** `Research_Logs/Evening_Wave_Briefs_Amundsen_and_Ethnic_Origin_2026-10-29.md`, Unit A1. Files-only inventory; no web research. **No design, no ruling, no recommendation.** Every fact cites file and line. Contradictions are stated flatly with both citations and are **not** adjudicated. The `City_Megasheets/` folder (and the `Super_Ultra_Megasheet/` folder built on top of it) were **listed, not opened**.

## PROGRESS
- [x] 1 Every GDD file that names the city
- [x] 2 What canon states about the city
- [x] 3 Contradictions and stale statements
- [x] 4 What the developer has said about expanding it
- [x] 5 Raw tool output (audit_city_inputs.py, verify_city_sheets.py)
- [x] 6 Rulings needed before a Division of Industry determination or a ULM pass
- [x] FINAL One-page index

**Path shorthands used below** (all relative to the GDD repo root):
- `CIT/` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/`
- `LOC/` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/`
- `ULM/` = `Worldspace/Locations-and-Levels/Universal_Location_Methodology/`
- `SPEC` = `CIT/Specs/Amundsen-Scott subnet/Amundsen_Station.md` (231 lines)
- `CEN` = `CIT/Official_Population_Census.md`
- `DRL` = `ULM/DEVELOPER_RULINGS_LOG.md`
- `PASS/` = `CIT/City_Development_Passes/Amundsen_Station/Amundsen_Station/`

**Method log (§9.5 recording law).**
- Name search, run 2026-10-29: `grep -rIlE 'Amundsen Station|Amundsen-Scott|Amundsen_Station|South Pole Station|Amundsen Scott'` over `Worldspace/` and `Reference/` (with `--exclude-dir=graphify-out`), plus each top-level file. **Result: 295 files under `Worldspace/` + `Reference/`, 2 at the top level (`TODO.md`, `DONE.md`).** Of the 295, 33 are in `City_Megasheets/` and 6 in `Super_Ultra_Megasheet/` (listed only, §1.N).
- The same search over the folders outside the brief's three roots (for item 4 and for completeness, §1.O): `Archive/` 29 · `Background-Lore/` 19 · `Storyline/` 8 · `Dev-Road-Map/` 3 · `to-be-integrated/` 5 · `Neo-Races-and-Cultures/` 2 · `Theoretical-Calculations/` 1 · `Game-Mechanics/` 1 · `General-Overview-Notes/` 1 · `testing/` 1.
- **Not searched for:** the bare word "Amundsen" (it returns every Amundsen Tower line in the repo, a different subject), and "South Pole" alone (returns the geographic pole in real-world research files). Lines about the Tower are cited below only where they state something about the station.
- **Snag:** the Pre-Trip sheet's and datasheets' line citations into `Airports.md`, `Ports.md` and `Inspirational-Influences.md` have drifted (see §3, C-27); every line number in **this** file was re-read on 2026-10-29.
- **Snag:** `LOC/Infrastructure/Amundsen_Power_Supply.md` is **0 bytes** (confirmed with `wc -c`). It is cited as a power source by other files; nothing in it can be cited.
- **Not graphify:** this inventory used direct reads and `grep` only (the brief names files-only work; no cold-run rule applies, but no graph query was needed to locate files that a name search returns exhaustively).

---

## 1 · Every GDD file that names the city

Kinds used: **spec · census · DoI** (Division of Industry) **· relationships · culture · enneagram · symbol · vision · concept art · infrastructure · status · sheets** (ULM datasheets / Pre-Trip / ledger) **· method · reference · research · character · map data · tool**. Hits = lines matching the name search.

### 1.A · The city's own files

| Path | Kind | What it holds |
|---|---|---|
| `SPEC` | spec | The city's spec: header fields (L3–L8), Census I/II and the 12-nation per-nation table (L12–L44), geographic basis and full climate block with the 2026-09-04 climate ruling (L48–L144), founding (L148–L152), character and culture (L156–L164), economy (L168–L172), notable locations and figures (L176–L187), Concordia connection (L191–L197), destruction and Calethina lore (L201–L209), legacy (L213–L217), 8 open questions (L221–L230) |
| `CIT/City_Development_Passes/Amundsen_Station/README.md` | sheets (README) | Outer folder README, opened 2026-09-05; the file plan for a ULM/CST/RWBEM run; source table (spec path given as `../../Specs/Amundsen_Station.md`, L36) |
| `PASS/README.md` | sheets (README) | Inner folder README, created 2026-10-21; same file plan plus the Datasheets row (L36) and the corrected spec path (L37) |
| `PASS/00.0_Pre-Trip_Inspection.md` | sheets (Pre-Trip) | 568-line address book generated 2026-10-21 by `Tools/build_pretrip.py`: alias set (§A), warm run mode (§B), per-step and per-phase read lists with `T8` wiring (§C, §D), carve-outs, withheld/read-last list, open items (§I) |
| `PASS/00.2_Position_Coverage_Ledger.md` | sheets (ledger) | Empty T3 ledger, 9 positions × Phases 2–10; L20: "all cells blank — Amundsen Station's ULM pass has not yet begun" |
| `PASS/Datasheets/Step_-1.md` | sheets | Bibliographic facts and spec fields; Census I/II lines (L19–L20); excluded later-era lines by number only (L12, L17–L18) |
| `PASS/Datasheets/Step_0.md` | sheets | Census I/II rows, computed retention (combined 71.33%, human 81.45%, robot 69.35%, L10), the Second Interwar frame and Act structure (L11–L13) |
| `PASS/Datasheets/Step_1_and_2.md` | sheets | Climate fields (L9–L29), `16` Half B row (L30), Founding Register row (L32), spec `Settled:` and `Founding population:` (L33–L34), composition tiers (L35) |
| `PASS/Datasheets/Step_3.md` | sheets | Research log does not exist (L8); `Inspirational-Influences.md` entry pointer (L9–L11) |
| `PASS/Datasheets/Step_5.md` | sheets | Deliberate stub: the culture files are read last (L3–L15) |
| `PASS/Datasheets/Step_6.md` | sheets | The 10-section differentiation-table inventory (Tier U) |
| `PASS/Datasheets/Step_7.md` | sheets | 17-gate index (Tier U) |
| `PASS/Datasheets/Step_8.md` | sheets | Review Panel index (Tier U) |
| `PASS/Datasheets/Step_9.md` | sheets | Record-step index (Tier U) |
| `PASS/Datasheets/Step_10.md` | sheets | `06_Worked_Example_Provenance.md` has zero hits (L7) |
| `PASS/Datasheets/Phase_2.md` | sheets | Spec and census tier tables compared "Identical" (L8–L10); Falkland Treaty clauses; Founding Register row (L23) |
| `PASS/Datasheets/Phase_3.md` | sheets | Concept-art folder empty (L8); megasheet file exists, withheld (L9); spec sections by range (L11–L13) |
| `PASS/Datasheets/Phase_4.md` | sheets | `09` §2 row and `16` Half B row (L10, L12); `11` and Medical Institutes have no row (L11, L13) |
| `PASS/Datasheets/Phase_5.md` | sheets | Lines naming the city in Highways, Airports, Ports, City_Relationship_Database, City_National_Connections (L10–L31) |
| `PASS/Datasheets/Phase_6.md` | sheets | Religions folder 0 hits; National_Holidays L41 St. Roald (L9) |
| `PASS/Datasheets/Phase_7.md` | sheets | `16` row and other `16` line numbers (L14–L15); DoI Sweep lines (L16–L20); Theoretical-Calculations pointers (L21) |
| `PASS/Datasheets/Phase_8.md` | sheets | Spec has 0 hits for cuisine, dress, music, craft (L9) |
| `PASS/Datasheets/Phase_9.md` | sheets | Robot share of Census I computed 83.65% (L13) |
| `PASS/Datasheets/Phase_10.md` | sheets | Characters canon: 2 universe-repo files name the city (L8–L11) |
| `CIT/Local_Cultures/Amundsen_Station/Amundsen_Station.md` | culture | 32-section cultural sheet (written 2026-07-04) with an opening "never a city" caveat (L5); §15 Division of Industry 60/30/10 (L144–L152) ⚠ read-last for any ULM pass |
| `CIT/Local_Robot_Culture/Amundsen_Station/Amundsen_Station.md` | culture (robot) | Run #35 of the Local Robot Culture Methodology, 2026-08-11 (L3), "Provisional — findings are proposals" (L22–L23); states tours of "six months to two years" (L14) ⚠ read-last |
| `CIT/City_Enneagram_Personalities/Amundsen_Station/Amundsen_Station.md` | enneagram | Head / Compliant / Competency profile (L5–L15) ⚠ read-last |
| `CIT/City_Vision_Notes/Amundsen_Station.md` | vision | 2026-07-06 session: "scientific, technical, and mechanical maintenance" (L19) ⛔ not a ULM input (`DR-10`) |
| `CIT/City_Concept-Art/Amundsen_Station/` (`.gitkeep` only) | concept art | Empty folder |
| `CIT/Local_Cultures/Amundsen_Station/.gitkeep` | — | Placeholder |
| `LOC/Infrastructure/Amundsen_Power_Supply.md` | infrastructure | **Empty (0 bytes)**; created in commit `46eb7b7b` (2026-07-03) |
| `Reference/Real-World/Climate Data/READER/Amundsen_Station.md` | reference (climate) | 17-line BAS READER file: annual mean −49.1 °C, monthly means 1991–2020 (L8–L14) |
| `Reference/Real-World/Inspiration_Place_Research/inputs/Amundsen_Station_Amundsen_Scott_Station_reference_only.md` | research input | The seven tiered inspiration picks copied from `Inspirational-Influences.md` (L6–L12) |
| `Reference/Real-World/Inspiration_Place_Research/candidates/Amundsen_Station.md` | research (draft) | 176-line draft of 104 candidate picks from knowledge, 2026-10-27; carries the developer's expansion direction (L7, facet F13 at L27) |
| `CIT/Research_Logs/Amundsen_Station_Canon_Inventory_2026-10-29.md` | research | This file |
| `CIT/Research_Logs/Amundsen_Station_Real_World_Research_2026-10-29.md` | research | Unit A2's output (sibling unit; not read by this unit beyond its title line) |
| `CIT/Research_Logs/Evening_Wave_Briefs_Amundsen_and_Ethnic_Origin_2026-10-29.md` | status | The brief for this unit |
| `Neo-Races-and-Cultures/Amundsen_Station/` (`.gitkeep` only) | — | Empty folder (outside the brief's roots; listed for completeness) |

### 1.B · Census, composition, founding

| Path | Kind | What it holds |
|---|---|---|
| `CEN` | census | Section A entry L456–L468 (tier table, "not a residential city" note L468); Census I row L519; maritime fleet row L520; Census I subnet total L540; Census II row L637; space workforce L638 and maritime fleet L639; Census II subnet totals L658–L660 |
| `CIT/Upper_Earth_Immigration_Composition.md` | census (method) | The Amundsen composition derivation L646–L656; the 0.2% / 1% reduction that set its population L1153–L1159; pre-reduction rows L768, L805, L870, L901; post-reduction rows L1005, L1020, L1023; Census II rows L1253, L1268 |
| `CIT/Founding_Register.md` | registry | The city's row L75 (no founding nation); ruling log L90 |
| `CIT/Founding_Register_TimeZone_Audit_and_Proposals_2026-10-03.md` | method | Pole sits on every longitude, so the solar-zone test does not apply (L20); "not nation-based … technical crews" (L46, L223) |
| `ULM/Population_Scenario_Santa_Luce_Redistribution_2026-10-28.md` | status (scenario, adopted) | Amundsen Station keeps 6,857 / 4,891 (L11, L45); its redistribution share becomes the space workforce and maritime fleet (L49–L56); hostel model (L79–L94, L126–L157); overland travel times from the station (L112–L124); overflow model (L159–L183) |
| `CIT/City_Refugee_District_Affinities.md` | relationships | Amundsen Station excluded as "a fixed, specialized station complement, not a source of ordinary civilian refugee flow" (L7) |

### 1.C · Division of Industry

| Path | Kind | What it holds |
|---|---|---|
| `CIT/Division_of_Industry/04_Providers_and_National_Balance.md` | DoI | Provider row: 6,857, ARCANET · TOWER, relay 60% + Tower 30%, "not a city; special case" (L79) |
| `CIT/Division_of_Industry/09_Per_City_Baseline_Run.md` | DoI | §2 row: D 2.50, humans 1,121, residents 6,857, required 2,118, workforce 6,297, 33.6% (L88) |
| `CIT/Division_of_Industry/13_National_Balance_Under_the_Ruling.md` | DoI | Geology row: 1,121 humans, 162, "polar plateau" (L73); ice-sheet forced importer (L864, L921) |
| `CIT/Division_of_Industry/15_Open_Items_and_Three_Resolutions.md` | DoI | "cover their obligations comfortably — … relay + Tower ops" (L333); food term at 10% for forced importers incl. Amundsen Station (L508) |
| `CIT/Division_of_Industry/16_Per_City_Three_Tier_Run.md` | DoI | Half B row (L249) and subnet row (L307); special-case range note (L336); archive ABCC candidate (L1238); **§35 "AMUNDSEN STATION — DETERMINED"** (L3445–L3546); review-register items 10 and 24 (L3564, L3578) |
| `CIT/Division_of_Industry/17_National_Balance_Refresh_2026-10-28.md` | DoI | Listed among the forced importers (L7, L11) |
| `CIT/Division_of_Industry_Sweep_2026-08-31.md` | DoI (audit) | Scope includes Amundsen Station (L10); "Arcanet 60% / Tower ops 30%" with the "no economy" caveat (L77–L78); 6/6 missing marks (L143, L187) |

### 1.D · Infrastructure

| Path | Kind | What it holds |
|---|---|---|
| `LOC/Infrastructure/Highways.md` | infrastructure | Hwy 22 route through the South Pole (L141, L146); Hwy 59 and Hwy 175 ramps with Hwy 22 (L62, L64, L185–L193, L214–L221, L297); Mountain Pass Airport accessible to Amundsen Station (L163) |
| `LOC/Infrastructure/Airports.md` | infrastructure | Mountain Pass Airport "reasonably accessible to … Amundsen Station" (L18); Amundsen Station in the no-airport list (L50) and in the "real-world airstrip, none in Tepenia" list (L54) |
| `LOC/Infrastructure/Ports.md` | infrastructure | "inland" (L182); "connect only by highway from a coastal port" (L205); deep interior / plateau (L482); LANDLOCKED (L740) |
| `LOC/Infrastructure/Rastra_Mechanics.md` | infrastructure | "Every Hwy 22/175/183 route from Amundsen Station other than Byrd exceeds 1,500 km" (L66); real South Pole traverse benchmarks (L55–L56) |
| `LOC/Infrastructure/Geothermal_Heating.md` | infrastructure | Names `Amundsen_Power_Supply.md` as the file covering "the regulated continent-wide grid that Amundsen Tower ran" (L3, L90, L189) |

### 1.E · Relationships, reference compiles, registries

| Path | Kind | What it holds |
|---|---|---|
| `CIT/City_Relationship_Database.md` | relationships | Hwy 22 table row (L25); relay note (L57); the city's own entry L78–L85; Byrd's corridor note and proposed debris bypass (L135); Split Brain section (L504, L512, L516, L525); resolved highway question (L541) |
| `CIT/City_National_Connections.md` | relationships | Post-Tower connection lists; Amundsen Station named under Halley (L43), Neumayer (L51), Sanay (L129), Pergamino (L253), Kunlun (L325), another Mirny-subnet city (L356), Fort McMurdo (L426), Cape Adare (L453); open item on Hwy 59 (L586). Header L5 dates the frame to "after the Tower's completion" ⚠ its own header says it draws on withheld material |
| `CIT/City_Master_Reference/Mawson_Byrd_Amundsen_Reference.md` | reference compile | Amundsen Station section L228–L284 (2026-09-02 compile): file list, canon facts, DoI status, draft-tier notes, infrastructure cross-references |
| `CIT/City_Master_Reference/README.md`, `…/Halley_Subnet_Reference.md`, `…/Janbogo_Subnet_Reference.md`, `…/Palmer_Subnet_Reference.md`, `…/Split_Extracts/Halley_Subnet_Reference_EXTRACT.md`, `…/Split_Extracts/Janbogo_Subnet_Reference_EXTRACT.md` | reference compile | Incidental mentions (Hwy 59 to the Pole; Airports L18; the Pergamino archive) |
| `LOC/Per-Subnet_Overview_Reference_Data.md` | reference | South Pole row: 1 member, 6,857, 83.65% robot (L11); "Unification/Scientific" label and founders line (L34); members row (L120) |
| `LOC/Per-Subnet_Guides/South_Pole.md` | reference (shell) | Empty regional-personality guide, created 2026-10-05; DLC 1; label "Unification/Scientific" (L7–L12) |
| `CIT/Overview.md` | reference | Station row: "Amundsen-Scott South Pole Station · USA · Inter-subnet relay · Destroyed" (L158); Split Brain note (L177) |
| `CIT/Station_to_City_Map.md` | reference | Station row (L108); destroyed list (L135) |
| `CIT/National_Capital_Candidates.md` | reference | Excluded: "destroyed … never a residential city" (L47) |
| `CIT/Inspirational-Influences.md` | reference | Heading "Amundsen Station · Amundsen-Scott Station [reference-only]" (L310), alias note (L312–L318), seven tiered picks |
| `CIT/City_Symbolic_Substrate/City_Symbol_Assignments.md` | symbol | Amundsen Station: Planet **Neptune**, Element **⏸️** (L145–L152); usage count (L306); "scale pair" note with Sanay (L331) |
| `Worldspace/National_Holidays.md` | culture (national) | "St. Roald — Roald Amundsen (Amundsen Station)" (L41) |
| `CIT/Local_Cultures/README.md` | status | Section heading (L109); status Destroyed, corrected 2026-07-03 (L114); "edge case" note (L123) |
| `CIT/Full_City_Integrity_Check.md`, `CIT/Investigation_Loop_Round2_Tracker.md`, `CIT/Founding_Nation_Bug_Investigation_Methodology.md` | status | 2026-07-14 re-checks; Amundsen Station checked "for completeness" (Full_City_Integrity_Check L106) |
| `CIT/Station_Heritage_Removal_Tracker.md` | status | Item I-7 flags "L346 Amundsen-Scott history" in the research-topics file (L262) |
| `CIT/City_Concept-Art/README.md` | concept art (README) | "a dedicated `Amundsen_Station/` folder … (a single city, no subnet)" (L3, L7) |
| `CIT/City_Development_Passes/README.md` | sheets (index) | Folder count (L37); "its own top-level folder" (L46) |
| `CIT/City_Development_Passes/follow-up_questions.md` | status | Amundsen Station among founding rows "canon but not re-ruled since `DR-19`" (L287) |

### 1.F · ULM method and status files

| Path | Kind | What it holds |
|---|---|---|
| `DRL` | status (rulings) | Planet note (L120–L133); `DR-17` seven subnets (L526–L532); `DR-44` founding row (L929); `DR-58` "The official census governs its population" (L1167); `DR-63` to `DR-69` (L1276–L1355) |
| `ULM/MASTER_Process_Tracker.md` | status | November scope excludes Amundsen Station "(the developer will expand it first)" (L367); same, dated 2026-10-21 (L437) |
| `ULM/City_Input_Gaps_2026-10-27.md` | status | Developer reminder (L4, L10); "research, design & development, and determination … Amundsen-Scott" (L11); audit false positive (L29); status row (L82) |
| `ULM/Extent_and_Density_Per_City.md` | method | Table row: 6,857, 1 km² at 10k/km², 1 at 7k, "South Pole" (L629); Port Lockroy smaller (L136); 0% rock (L578) |
| `ULM/Extent_and_Area_APPROACH.md` | method | Ice drift ~10 m/yr (L143) |
| `ULM/ULM_Input_Available_Audit.md` | status | Symbol pair "Neptune + Magnetism" (L86); picks correction (L90); "relay outpost, not a residential city" (L306) |
| `ULM/02_Generators_Capability_and_Symbols.md` | method | Symbol note (L707) |
| `ULM/ULM_Run_Progress.md` (L425), `ULM/CST_Progress.md` (L231), `ULM/RWBEM_Progress.md` (L200) | status | Empty progress rows |
| `ULM/Datasheet_and_PreTrip_Tracker.md` | status | Amundsen Station tracker rows (L30 onward) |
| `ULM/Location_Data-Input_To-Do.md` | status | Listed as MISSING in one input list (L185) |
| `ULM/ULM_Input_Required_Reference.md`, `ULM/RealWorld_Basis_Input_Availability.md`, `ULM/Datasheet_Citations_To_Reread_2026-10-21.md`, `ULM/00_RUNBOOK.md` (L2062), `ULM/Disciplines/Real-World_Basis_Extrapolation_Method.md` (L406), `Worldspace/Locations-and-Levels/Real-World_Basis_Extrapolation_Method.md` (L335) | method | Path conventions ("read by name") and input tables |
| `ULM/Pre-Contamination_Reviews/Shirayuki_Pre-Contamination_Review.md` | method | Lists the universe-repo `Amundsen_Station_Archive_and_Trucking_Network.md` as a read surface (L445, L496, L524, L726) |
| `ULM/Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` | method | Climate-tool sign inversion at the Pole (L5510–L5513); a "left alone" note (L167) |
| `ULM/Tools/audit_city_inputs.py`, `build_pretrip.py`, `build_datasheets.py`, `check_must_open_coverage.py`, `map_books_to_topics.py` | tool | Config entries naming the city key |

### 1.G · Reference/ folder (other than §1.A)

| Path | Kind | What it holds |
|---|---|---|
| `Reference/Real-World/Climate Data/Precipitation_Falls_vs_Lands.md` | reference (climate) | Gauge 2.1 mm vs ~70–80 mm accumulation (L12, L104); spec field still holds the gauge figure (L238, L244) |
| `Reference/Real-World/Climate Data/Climate_Data_Corpus_Audit_2026-09-04.md` | reference (climate) | Pole light-cycle sign inversion (L41) |
| `Reference/Real-World/City_and_District_Research_Topics.md` | research topics | "Part 2 — 35 Cities + Amundsen-Scott Station" (L158); Amundsen-Scott topics (L346–L353) |
| `Reference/Real-World/Book_to_City_Map.md` · `Book_to_Topic_Scores_2026-10-21.json` | research topics | Topic-to-book mapping for the same topics (L184 onward) |
| `Reference/Real-World/Stations/Antarctic_Stations_With_Airstrips.md` | reference (real) | Real Jack F. Paulus Skiway row (L29) |
| `Reference/Real-World/Volcanism_and_Geothermal/00_City_Coordinates_From_Specs.md` | reference | −90.000, 0.000 (L7) |
| `Reference/Real-World/Inspiration_Place_Research/_TRACKER.md` (L47), `_SESSION_RESUME_2026-10-29.md` (L63, L70), `candidates/_DEVELOPER_ADDITIONS.md` (L5–L6, Timbuktu libraries), `candidates/_DRAFTING_TRACKER.md` (L44), `candidates/_REVIEW_PROGRESS.md` (L157–L159) | research tracker | Inspiration-research status for this city (7 picks; 104 candidates; "nothing started" for research and determination) |

### 1.H · Characters (in `Worldspace/`)

| Path | What it holds |
|---|---|
| `Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/Kendra Heinrich/DLC_South_Pole_Level_Design.md` | DLC 1 site design: underground shaft and tunnels (L28–L39), zones (L107–L110), "the underbelly of Amundsen Station" (L164), archive end-slide (L191) |
| `…/Kendra Heinrich/README.md` | Enemy note "Unique to the South Pole / Amundsen Station ruins" (L98) |
| `…/Calethina/README.md` (L51, L58), `Personal_Background/Founding_Construction_Chain_Play-by-Play.md` (6 hits from L79), `Founding_Construction_Chain_UNMARKED.md` (L18), `Player_Chamber_Origin_Chain_DRAFT.md` (L28), `Personal_Questline_Summary.md` (L156), `Questlines/Substrate_Transfer_and_Embodiment_Design.md` (L119) | Calethina's forward-shipping through "Amundsen-Scott Station" |
| `Worldspace/Characters/Dolls/Methodology/00d_Quick_Capture_Seed_-_Ready-Made_Partial_Seeds_[rewritable].txt` | Same chain, one line (L105) |

### 1.I · Other cities' files that name it in passing (mechanical list)

Each row: path · kind · hits · **first hit, mechanically extracted** (not a reading of the file's purpose). Generated 2026-10-29 from the name search; 162 rows.

| Path | Kind | Hits | First hit |
|---|---|--:|---|
| `Reference/Images/Maps/working-stash/CHANGES.md` | map data | 1 | L41: Cities: 38 (Palmer 8, Halley 8, Mawson 3, Mirny 9 incl. the placeholder-named Bunger Hills City, Janbogo 8, By |
| `Reference/Images/Maps/working-stash/data/cities.csv` | map data | 1 | L39: amundsen_station,Amundsen Station,Amundsen-Scott,-90.0,0.0,0,,Amundsen-Scott subnet/Amundsen_Station.md,Destro |
| `Reference/Images/Maps/working-stash/out/01_Tepenia_Cities.svg` | map data | 1 | L103949: <text style="font-size: 12.5px; font-family: 'Lato'; text-anchor: start; fill: #232b33" x="1081.430156" y="332 |
| `Reference/Images/Maps/working-stash/out/05_Tepenia_Arcanet_Subnets.svg` | map data | 1 | L115584: <text style="font-size: 12.5px; font-family: 'Lato'; text-anchor: start; fill: #232b33" x="1122.215312" y="291 |
| `Reference/Images/Maps/working-stash/scripts/tepenia_common.py` | tool script | 7 | L40: 'Janbogo': '#CC7A22', 'Byrd': '#8E9A10', 'Amundsen-Scott': '#3A3A3A'} |
| `Reference/Real-World/Book_to_City_Map.md` | reference/registry | 3 | L184: [Amundsen-Scott Station] Antarctic Treaty neutrality as a governance model — the treaty's own provisions, no |
| `Reference/Real-World/Book_to_Topic_Scores_2026-10-21.json` | reference/registry | 1 | L1: {"topics": [{"scope": "NATIONAL N1", "line": 54, "text": "WASTE TREATMENT", "war": false, "words": ["treatment |
| `Reference/Real-World/City_and_District_Research_Topics.md` | reference/registry | 3 | L158: Part 2 — 35 Cities + Amundsen-Scott Station |
| `Reference/Real-World/Climate Data/Climate_Data_Corpus_Audit_2026-09-04.md` | climate reference | 4 | L41: 1. The pole special-case had its sign inverted — it reported January at Amundsen Station as 0 hours of |
| `Reference/Real-World/Inspiration_Place_Research/_SESSION_RESUME_2026-10-29.md` | inspiration research tracker | 2 | L63: Relung Panen's founding "how and why", the port ruling, the cold-chain share; Amundsen Station research and de |
| `Reference/Real-World/Inspiration_Place_Research/_TRACKER.md` | inspiration research tracker | 1 | L47: Amundsen_Station_Amundsen_Scott_Station_reference_only  Amundsen Station · Amundsen-Scott Station [reference- |
| `Reference/Real-World/Inspiration_Place_Research/candidates/_DRAFTING_TRACKER.md` | inspiration research tracker | 1 | L44: 38  Amundsen_Station  Amundsen Station  Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Loca |
| `Reference/Real-World/Inspiration_Place_Research/candidates/_REVIEW_PROGRESS.md` | inspiration research tracker | 3 | L157: Amundsen Station  1 to 34 (batch 1, 2026-10-27)  none given for Byrd batch 3 (user said next city) |
| `Reference/Real-World/Stations/Antarctic_Stations_With_Airstrips.md` | reference/registry | 1 | L29: Jack F. Paulus Skiway  Amundsen–Scott South Pole Station  United States  Snow |
| `Reference/Real-World/Volcanism_and_Geothermal/00_City_Coordinates_From_Specs.md` | reference/registry | 1 | L7: Amundsen Station  Amundsen-Scott  90°00'S (Geographic South Pole)  -90.000, 0.000 |
| `Worldspace/Characters/Dolls/Methodology/00d_Quick_Capture_Seed_-_Ready-Made_Partial_Seeds_[rewritable].txt` | character file | 1 | L105: rerouted via Fort McMurdo, forwarded via Amundsen-Scott Station) |
| `Worldspace/Characters/Dolls/Still-Present_-_In-Game/unsure and_or special cases/Calethina/Personal_Background/Founding_Construction_Chain_Play-by-Play.md` | character file | 6 | L79: was never meant to go anywhere near Amundsen-Scott Station or Concordia at all — it was heading back to |
| `Worldspace/Characters/Dolls/Still-Present_-_In-Game/unsure and_or special cases/Calethina/Personal_Background/Founding_Construction_Chain_UNMARKED.md` | character file | 2 | L18: Forward-shipped via  Amundsen-Scott Station  — |
| `Worldspace/Characters/Dolls/Still-Present_-_In-Game/unsure and_or special cases/Calethina/Personal_Background/Player_Chamber_Origin_Chain_DRAFT.md` | character file | 1 | L28: 8  Forward-shipped via  Amundsen-Scott Station  — (South Pole) |
| `Worldspace/Characters/Dolls/Still-Present_-_In-Game/unsure and_or special cases/Calethina/Personal_Questline_Summary.md` | character file | 1 | L156: content, cross-DLC portability plus the Wave 2 character-specific sites (Byrd, Fort McMurdo, Amundsen-Scott |
| `Worldspace/Characters/Dolls/Still-Present_-_In-Game/unsure and_or special cases/Calethina/Questlines/Substrate_Transfer_and_Embodiment_Design.md` | character file | 2 | L119: Mawson (request) → Neumayer/Halley subnet (spec & schematic design) → Kunlun/Mirny subnet (engineering & p |
| `Worldspace/Locations-and-Levels/Concordia-City/Concordia_Second_Interwar_Cultural_Sheet.md` | reference/registry | 1 | L212: Amundsen Station: the whole Federation's attention, during the Tower's construction years, would have turned t |
| `CIT/City_Development_Passes/Byrd_Subnet/Byrd/Datasheets/Phase_10.md` | datasheet (other city) | 1 | L18: ↳ Dolls/Calethina/Personal_Background/Formative_History.md  Her construction and shipping origin is delibera |
| `CIT/City_Development_Passes/Byrd_Subnet/Byrd/Datasheets/Phase_5.md` | datasheet (other city) | 2 | L15: ↳ README.md  5. Super-Ultra-Megasheet (Worldspace/Locations-and-Levels/Super_Ultra_Megasheet/) — the whole |
| `CIT/City_Development_Passes/Byrd_Subnet/Byrd/Datasheets/Step_-1.md` | datasheet (other city) | 1 | L15: Highway access  Corrected 2026-07-06 — Byrd is a major two-highway junction, missed by this file despite bei |
| `CIT/City_Development_Passes/Byrd_Subnet/Byrd/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Byrd_Subnet/Byrd.md ⚠ Amundsen Station and Concordia do NOT follow th |
| `CIT/City_Development_Passes/Halley_Subnet/Belgrano/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Halley_Subnet/Belgrano.md ⚠ Amundsen Station and Concordia do NOT fol |
| `CIT/City_Development_Passes/Halley_Subnet/Halley/Datasheets/Step_-1.md` | datasheet (other city) | 1 | L15: Highway access  Revised 2026-10-03 (developer ruling): Halley is not a main-line stop on Hwy 7. The highway pa |
| `CIT/City_Development_Passes/Halley_Subnet/Halley/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Halley_Subnet/Halley.md ⚠ Amundsen Station and Concordia do NOT follo |
| `CIT/City_Development_Passes/Halley_Subnet/Lazar/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Halley_Subnet/Lazar.md ⚠ Amundsen Station and Concordia do NOT follow |
| `CIT/City_Development_Passes/Halley_Subnet/Neumayer/Datasheets/Phase_10.md` | datasheet (other city) | 1 | L12: ↳ Dolls/Calethina/Personal_Background/Formative_History.md  Her construction and shipping origin is delibera |
| `CIT/City_Development_Passes/Halley_Subnet/Neumayer/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Halley_Subnet/Neumayer.md ⚠ Amundsen Station and Concordia do NOT fol |
| `CIT/City_Development_Passes/Halley_Subnet/Sanay/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Halley_Subnet/Sanay.md ⚠ Amundsen Station and Concordia do NOT follow |
| `CIT/City_Development_Passes/Halley_Subnet/Santa_Luce/README.md` | pass README (other city) | 1 | L39: Local culture  ../../../Local_Cultures/Halley_Subnet/Abowasa.md ⚠ Amundsen Station and Concordia do NOT foll |
| `CIT/City_Development_Passes/Halley_Subnet/Troll/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Halley_Subnet/Troll.md ⚠ Amundsen Station and Concordia do NOT follow |
| `CIT/City_Development_Passes/Halley_Subnet/Utstein/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Halley_Subnet/Princess_Elisabeth.md ⚠ Amundsen Station and Concordia |
| `CIT/City_Development_Passes/Janbogo_Subnet/Cape_Adare/Datasheets/Step_5.md` | datasheet (other city) | 1 | L13: input-not-output and notes the standard-pattern caveat does not apply to Amundsen Station or Concordia — Cap |
| `CIT/City_Development_Passes/Janbogo_Subnet/Cape_Adare/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Janbogo_Subnet/Cape_Adare.md ⚠ Amundsen Station and Concordia do NOT |
| `CIT/City_Development_Passes/Janbogo_Subnet/Denison/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Janbogo_Subnet/Denison.md ⚠ Amundsen Station and Concordia do NOT fol |
| `CIT/City_Development_Passes/Janbogo_Subnet/Dumont_dUrville/Datasheets/Step_5.md` | datasheet (other city) | 1 | L13: notes the standard-pattern caveat does not apply to Amundsen Station or Concordia — Dumont d'Urville follows |
| `CIT/City_Development_Passes/Janbogo_Subnet/Dumont_dUrville/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Janbogo_Subnet/Dumont_dUrville.md ⚠ Amundsen Station and Concordia do |
| `CIT/City_Development_Passes/Janbogo_Subnet/Fort_McMurdo/Datasheets/Phase_10.md` | datasheet (other city) | 1 | L13: ↳ Dolls/Calethina/Personal_Background/Formative_History.md  Her construction and shipping origin is delibera |
| `CIT/City_Development_Passes/Janbogo_Subnet/Fort_McMurdo/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Janbogo_Subnet/Fort_McMurdo.md ⚠ Amundsen Station and Concordia do NO |
| `CIT/City_Development_Passes/Janbogo_Subnet/Janbogo/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Janbogo_Subnet/Janbogo.md ⚠ Amundsen Station and Concordia do NOT fol |
| `CIT/City_Development_Passes/Janbogo_Subnet/Scott/00.0_Pre-Trip_Inspection.md` | pre-trip sheet (other city) | 1 | L33: ⚠ Ambiguous name  Scott is also a person's name and part of Amundsen-Scott; the search excludes those forms, |
| `CIT/City_Development_Passes/Janbogo_Subnet/Scott/Datasheets/Phase_10.md` | datasheet (other city) | 1 | L4: ⚠ Ambiguous name: Scott is also a person's name and part of Amundsen-Scott; the search excludes those forms, |
| `CIT/City_Development_Passes/Janbogo_Subnet/Scott/Datasheets/Phase_2.md` | datasheet (other city) | 1 | L4: ⚠ Ambiguous name: Scott is also a person's name and part of Amundsen-Scott; the search excludes those forms, |
| `CIT/City_Development_Passes/Janbogo_Subnet/Scott/Datasheets/Phase_3.md` | datasheet (other city) | 1 | L4: ⚠ Ambiguous name: Scott is also a person's name and part of Amundsen-Scott; the search excludes those forms, |
| `CIT/City_Development_Passes/Janbogo_Subnet/Scott/Datasheets/Phase_4.md` | datasheet (other city) | 1 | L6: ⚠ Ambiguous name: Scott is also a person's name and part of Amundsen-Scott; the search excludes those forms, |
| `CIT/City_Development_Passes/Janbogo_Subnet/Scott/Datasheets/Phase_5.md` | datasheet (other city) | 1 | L6: ⚠ Ambiguous name: Scott is also a person's name and part of Amundsen-Scott; the search excludes those forms, |
| `CIT/City_Development_Passes/Janbogo_Subnet/Scott/Datasheets/Phase_6.md` | datasheet (other city) | 1 | L4: ⚠ Ambiguous name: Scott is also a person's name and part of Amundsen-Scott; the search excludes those forms, |
| `CIT/City_Development_Passes/Janbogo_Subnet/Scott/Datasheets/Phase_7.md` | datasheet (other city) | 1 | L10: ⚠ Ambiguous name: Scott is also a person's name and part of Amundsen-Scott; the search excludes those forms, |
| `CIT/City_Development_Passes/Janbogo_Subnet/Scott/Datasheets/Phase_8.md` | datasheet (other city) | 1 | L4: ⚠ Ambiguous name: Scott is also a person's name and part of Amundsen-Scott; the search excludes those forms, |
| `CIT/City_Development_Passes/Janbogo_Subnet/Scott/Datasheets/Phase_9.md` | datasheet (other city) | 1 | L4: ⚠ Ambiguous name: Scott is also a person's name and part of Amundsen-Scott; the search excludes those forms, |
| `CIT/City_Development_Passes/Janbogo_Subnet/Scott/Datasheets/Step_-1.md` | datasheet (other city) | 1 | L4: ⚠ Ambiguous name: Scott is also a person's name and part of Amundsen-Scott; the search excludes those forms, |
| `CIT/City_Development_Passes/Janbogo_Subnet/Scott/Datasheets/Step_0.md` | datasheet (other city) | 1 | L4: ⚠ Ambiguous name: Scott is also a person's name and part of Amundsen-Scott; the search excludes those forms, |
| `CIT/City_Development_Passes/Janbogo_Subnet/Scott/Datasheets/Step_1_and_2.md` | datasheet (other city) | 1 | L4: ⚠ Ambiguous name: Scott is also a person's name and part of Amundsen-Scott; the search excludes those forms, |
| `CIT/City_Development_Passes/Janbogo_Subnet/Scott/Datasheets/Step_3.md` | datasheet (other city) | 1 | L4: ⚠ Ambiguous name: Scott is also a person's name and part of Amundsen-Scott; the search excludes those forms, |
| `CIT/City_Development_Passes/Janbogo_Subnet/Scott/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Janbogo_Subnet/Scott.md ⚠ Amundsen Station and Concordia do NOT follo |
| `CIT/City_Development_Passes/Janbogo_Subnet/Zukelli/Datasheets/Step_5.md` | datasheet (other city) | 1 | L13: input-not-output and notes the standard-pattern caveat does not apply to Amundsen Station or Concordia — Zuk |
| `CIT/City_Development_Passes/Janbogo_Subnet/Zukelli/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Janbogo_Subnet/Zukelli.md ⚠ Amundsen Station and Concordia do NOT fol |
| `CIT/City_Development_Passes/Mawson_Subnet/Dome_Fuji/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Mawson_Subnet/Dome_Fuji.md ⚠ Amundsen Station and Concordia do NOT fo |
| `CIT/City_Development_Passes/Mawson_Subnet/Mawson/Datasheets/Phase_10.md` | datasheet (other city) | 1 | L14: ↳ Dolls/Calethina/Personal_Background/Formative_History.md  Her construction and shipping origin is delibera |
| `CIT/City_Development_Passes/Mawson_Subnet/Mawson/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Mawson_Subnet/Mawson.md ⚠ Amundsen Station and Concordia do NOT follo |
| `CIT/City_Development_Passes/Mawson_Subnet/Temirotkel/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Mawson_Subnet/Sayowa.md ⚠ Amundsen Station and Concordia do NOT follo |
| `CIT/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Mirny_Subnet/Vostok.md ⚠ Amundsen Station and Concordia do NOT follow |
| `CIT/City_Development_Passes/Mirny_Subnet/Casey/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Mirny_Subnet/Casey.md ⚠ Amundsen Station and Concordia do NOT follow |
| `CIT/City_Development_Passes/Mirny_Subnet/Davis/00.1a_RULING_Vision_Notes_and_Specs_L135-181.md` | ULM pass file (other city) | 2 | L23: 37 files exist in Locations/Cities/City_Vision_Notes/ — one per city plus Amundsen_Station.md. |
| `CIT/City_Development_Passes/Mirny_Subnet/Kunlun/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Mirny_Subnet/Kunlun.md ⚠ Amundsen Station and Concordia do NOT follow |
| `CIT/City_Development_Passes/Mirny_Subnet/Mirny/.t8_Phase10_readerA.md` | T8 reader/probe scratch (Mirny pass) | 1 | L8: 4 DEVELOPER_RULINGS_LOG.md — read 20-147, 170-254, 384-419, 422-554, 623-665, 678-690, 725-757, 953-1031 — |
| `CIT/City_Development_Passes/Mirny_Subnet/Mirny/.t8_Phase10_readerC.md` | T8 reader/probe scratch (Mirny pass) | 1 | L8: 4 DEVELOPER_RULINGS_LOG.md — read L20-147, 170-254, 384-419, 422-554, 623-665, 678-690, 725-757, 953-1031 (1 |
| `CIT/City_Development_Passes/Mirny_Subnet/Mirny/.t8_Phase5_readerA.md` | T8 reader/probe scratch (Mirny pass) | 4 | L62: Spans refused inside admitted files: every Status: line and post-war span (CRD L14, L326, L57's second half fr |
| `CIT/City_Development_Passes/Mirny_Subnet/Mirny/.t8_Phase5_readerB.md` | T8 reader/probe scratch (Mirny pass) | 5 | L31: 13  CRD  1–58, 157–159, 180–182, 323–331, 510–523  87  Hwy 110 row; official subnet names = hub name |
| `CIT/City_Development_Passes/Mirny_Subnet/Mirny/00_Frame.md` | ULM pass file (other city) | 2 | L26: Q-30  Seven — "counting Amundsen-Scott Station as separate, even though it's technically a nexus" (DR-17)  C |
| `CIT/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_05_Relation_and_Geometry.md` | ULM pass file (other city) | 2 | L97: The parent, as the frame gives it: the Mirny subnet, UNWRITTEN — nine members at Census I, all routed throug |
| `CIT/City_Development_Passes/Mirny_Subnet/Mirny/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Mirny_Subnet/Mirny.md ⚠ Amundsen Station and Concordia do NOT follow |
| `CIT/City_Development_Passes/Mirny_Subnet/Mirny/_safeguard_probe/partials/Phase10_readerA_partial_before_assembly.md` | T8 reader/probe scratch (Mirny pass) | 1 | L8: 4 DEVELOPER_RULINGS_LOG.md — read 20-147, 170-254, 384-419, 422-554, 623-665, 678-690, 725-757, 953-1031 — |
| `CIT/City_Development_Passes/Mirny_Subnet/Mirny/_safeguard_probe/partials/Phase10_readerC_partial_before_assembly.md` | T8 reader/probe scratch (Mirny pass) | 1 | L8: 4 DEVELOPER_RULINGS_LOG.md — read L20-147, 170-254, 384-419, 422-554, 623-665, 678-690, 725-757, 953-1031 (1 |
| `CIT/City_Development_Passes/Mirny_Subnet/Mirny/_safeguard_probe/staging/P10_A_run1_a7b367_staging.md` | T8 reader/probe scratch (Mirny pass) | 1 | L20: 4 DEVELOPER_RULINGS_LOG.md — read 20-147, 170-254, 384-419, 422-554, 623-665, 678-690, 725-757, 953-1031 — |
| `CIT/City_Development_Passes/Mirny_Subnet/Mirny/_safeguard_probe/staging/P10_B_run1_a0acf6_staging.md` | T8 reader/probe scratch (Mirny pass) | 1 | L16: 4 DEVELOPER_RULINGS_LOG.md — read 20-147,170-254,384-419,422-554,623-665,678-690,725-757,953-1031 (550 admit |
| `CIT/City_Development_Passes/Mirny_Subnet/Relung_Panen/README.md` | pass README (other city) | 1 | L40: Local culture  ../../../Local_Cultures/Mirny_Subnet/Relung_Panen.md (does not exist yet) ⚠ Amundsen Station |
| `CIT/City_Development_Passes/Mirny_Subnet/Sinheung/README.md` | pass README (other city) | 1 | L52: Local culture  /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locati |
| `CIT/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/04_Phase_05_Relation_and_Geometry.md` | ULM pass file (other city) | 2 | L56: ✅ Not built on  Nothing below rests on it. Three of this city's six listed connections (Juan Carlos, Port Lo |
| `CIT/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/04_Phase_07_Order.md` | ULM pass file (other city) | 2 | L413: Hwy 22 — Transcontinental Highway. Byrd (Amundsen Sea) → South Pole (Amundsen Station) → junction |
| `CIT/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/README.md` | pass README (other city) | 1 | L37: Local culture  ../../../Local_Cultures/Mirny_Subnet/Zhongshan.md ⚠ Amundsen Station and Concordia do NOT fol |
| `CIT/City_Development_Passes/Mirny_Subnet/Zhongshan_Sonnet/README.md` | pass README (other city) | 1 | L37: Local culture  ../../../Local_Cultures/Mirny_Subnet/Zhongshan.md ⚠ Amundsen Station and Concordia do NOT fol |
| `CIT/City_Development_Passes/Palmer_Subnet/Contrapunto/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Palmer_Subnet/Sejong.md ⚠ Amundsen Station and Concordia do NOT follo |
| `CIT/City_Development_Passes/Palmer_Subnet/Esperanza/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Palmer_Subnet/Esperanza.md ⚠ Amundsen Station and Concordia do NOT fo |
| `CIT/City_Development_Passes/Palmer_Subnet/Marambio/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Palmer_Subnet/Marambio.md ⚠ Amundsen Station and Concordia do NOT fol |
| `CIT/City_Development_Passes/Palmer_Subnet/Palmer_City/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Palmer_Subnet/Palmer_City.md ⚠ Amundsen Station and Concordia do NOT |
| `CIT/City_Development_Passes/Palmer_Subnet/Pergamino/Datasheets/Step_-1.md` | datasheet (other city) | 1 | L17: Significance  Tepenian city on Livingston Island, South Shetland Islands; renamed Pergamino 2026-10-03 (DR-41) |
| `CIT/City_Development_Passes/Palmer_Subnet/Pergamino/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Palmer_Subnet/Juan_Carlos.md ⚠ Amundsen Station and Concordia do NOT |
| `CIT/City_Development_Passes/Palmer_Subnet/Puerto_Abrigo/Datasheets/Phase_10.md` | datasheet (other city) | 1 | L13: ↳ Dolls/Calethina/Personal_Background/Formative_History.md  Her construction and shipping origin is delibera |
| `CIT/City_Development_Passes/Palmer_Subnet/Puerto_Abrigo/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Palmer_Subnet/Port_Lockroy.md ⚠ Amundsen Station and Concordia do NOT |
| `CIT/City_Development_Passes/Palmer_Subnet/Rothera/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Palmer_Subnet/Rothera.md ⚠ Amundsen Station and Concordia do NOT foll |
| `CIT/City_Development_Passes/Palmer_Subnet/Signy/README.md` | pass README (other city) | 1 | L38: Local culture  ../../../Local_Cultures/Palmer_Subnet/Signy.md ⚠ Amundsen Station and Concordia do NOT follow |
| `CIT/City_Development_Passes/README.md` | pass README (other city) | 2 | L37: Amundsen_Station  1 |
| `CIT/City_Development_Passes/follow-up_questions.md` | ULM pass file (other city) | 1 | L287: 12 ruled · 2 ruled in part (Signy, Halley) · 6 canon but not re-ruled since DR-19 (Palmer City, Shirayuki, S |
| `CIT/City_Enneagram_Personalities/Distinguishing_Overlapping_Profiles.md` | reference/registry | 3 | L3: The three-axis Enneagram framework only has 27 possible combinations, and Tepenia has 36 profiled locations (3 |
| `CIT/City_Enneagram_Personalities/README.md` | reference/registry | 1 | L46: Amundsen Station: Amundsen_Station/ (not one of the 35 cities, included for completeness) |
| `CIT/City_Master_Reference/Halley_Subnet_Reference.md` | reference compile | 2 | L20: Highway spine: Hwy 7 runs the Queen Maud Land coast (Belgrano ↔ Sanay ↔ Santa Luce ↔ Troll ↔ Lazar), c |
| `CIT/City_Master_Reference/Janbogo_Subnet_Reference.md` | reference compile | 2 | L116: Airports.md L18 — named in the Mountain Pass Airport entry: "reasonably accessible to Kunlun, Dome Fuji, Amu |
| `CIT/City_Master_Reference/Palmer_Subnet_Reference.md` | reference compile | 1 | L221: ⭐ National role — Tepenia's first bureaucratic archive (established 2026-07-05): the original home of Fede |
| `CIT/City_Master_Reference/README.md` | reference compile | 3 | L67: ⭐⭐ Climate Data/Precipitation_Falls_vs_Lands.md  THE precipitation reference. Four distinct quantities — |
| `CIT/City_Master_Reference/Split_Extracts/Halley_Subnet_Reference_EXTRACT.md` | reference compile | 2 | L34: Highway spine: Hwy 7 runs the Queen Maud Land coast (Belgrano ↔ Sanay ↔ Santa Luce ↔ Troll ↔ Lazar), c |
| `CIT/City_Master_Reference/Split_Extracts/Janbogo_Subnet_Reference_EXTRACT.md` | reference compile | 2 | L147: Airports.md L18 — named in the Mountain Pass Airport entry: "reasonably accessible to Kunlun, Dome Fuji, Amu |
| `CIT/City_Vision_Notes/Byrd.md` | vision notes (other city) | 1 | L23: Follow-up asked: given Byrd's isolation (grounded aviation, no direct Hwy 37 connection), where does the massi |
| `CIT/City_Vision_Notes/Halley.md` | vision notes (other city) | 1 | L23: This meaningfully raises Halley's actual vulnerability, not lowers it. With no sea access of its own, Halley h |
| `CIT/Founding_Nation_Bug_Investigation_Methodology.md` | reference/registry | 2 | L644: item is drawn from. Amundsen Station (outside the 35-city count) was also re-checked, once, per |
| `CIT/Full_City_Integrity_Check.md` | reference/registry | 4 | L9: Amundsen Station as a formal convergence loop. No longer blocking. This tracker remains as the |
| `CIT/Investigation_Loop_Round2_Tracker.md` | reference/registry | 1 | L37: Halley (8) → Mirny (8) → Palmer (8) → Janbogo (7) → Mawson (3) → Byrd (1). Amundsen Station sits |
| `CIT/Local_Cultures/Byrd_Subnet/Byrd.md` | culture (other city) | 1 | L221: Vision session, 2026-07-06 — the trucking depot's actual routing, confirmed: overland freight runs in two di |
| `CIT/Local_Cultures/Halley_Subnet/Halley.md` | culture (other city) | 1 | L201: Amundsen Station: Connected via Hwy 59, which also carries the Arcanet cable — the single most strategically |
| `CIT/Local_Cultures/Halley_Subnet/Neumayer.md` | culture (other city) | 1 | L203: Amundsen Station (destroyed): No direct highway connection, but the deepest thematic tie in the subnet — Neu |
| `CIT/Local_Cultures/Janbogo_Subnet/Cape_Adare.md` | culture (other city) | 1 | L36: The city inherited St. Carsten — Carsten Borchgrevink himself — as its founding Saint, and his significanc |
| `CIT/Local_Cultures/Mirny_Subnet/Ariun_Nuur.md` | culture (other city) | 1 | L44: The coldest sustained environment of any Tepenian city — mean annual temperature −54.8°C, with the outrig |
| `CIT/Local_Cultures/Palmer_Subnet/Pergamino.md` | culture (other city) | 2 | L193: Developer vision, established 2026-07-05 — a quiet city with an outsized, largely invisible national respons |
| `CIT/Local_Robot_Culture/Halley_Subnet/Halley.md` | robot culture | 2 | L84: point at all (its own Arcanet signal routed through Amundsen Station pre-Split-Brain, now severed). |
| `CIT/Local_Robot_Culture/Halley_Subnet/Neumayer.md` | robot culture | 3 | L36: itself), §23 (Relationships — Halley, Amundsen Station, Vosora Lashár Tanslock; notably, no Sanay entry at |
| `CIT/Local_Robot_Culture/Halley_Subnet/Troll.md` | robot culture | 1 | L398: Halley) include no Neumayer entry, and Neumayer's own confirmed list (Amundsen Station, Sinheung, Byrd, |
| `CIT/Local_Robot_Culture/Palmer_Subnet/Pergamino.md` | robot culture | 3 | L95: City_National_Connections.md confirms a Strong Historical tie to Amundsen Station (not yet run — the direct |
| `CIT/Local_Robot_Culture/Palmer_Subnet/Signy.md` | robot culture | 1 | L359: own. This closes out the Palmer Subnet — 8 of 8 cities now Draft. Amundsen Station remains the sole |
| `CIT/Local_Robot_Culture_Methodology/00_DRAFT_Input_Categories_and_Approach.md` | robot culture | 2 | L311: Palmer_Subnet/, Byrd_Subnet/, Amundsen_Station/ — all created, currently empty). Each city gets its own |
| `CIT/Local_Robot_Culture_Methodology/02_City_Tracking_Checklist.md` | robot culture | 11 | L4: actual contents 2026-08-10 (not reconstructed from memory). 35 cities + Amundsen Station = 36 entries total. |
| `CIT/Local_Robot_Culture_Methodology/03_Standout_Findings_Digest.md` | robot culture | 15 | L290: Five subnets remain untouched (Byrd, Mawson, Halley, Janbogo, Palmer) plus Amundsen Station. See |
| `CIT/Research_Logs/Climate_Data_Research_Log.md` | research log | 8 | L160: at Amundsen Station as 0 hours of daylight — it is continuous sun), then a refraction omission. |
| `CIT/Research_Logs/Davis_Research_Log.md` | research log | 2 | L775: Wikipedia Amundsen–Scott South Pole Station  ⭐ isolated mid-February to late October; several flights/week |
| `CIT/Research_Logs/Relung_Panen_Intake_A_Winter_Aviation_2026-10-29.md` | research log | 2 | L46: 14-22 Jun 2016  South Pole (from Rothera)  2 × Twin Otter, Kenn Borek  Calgary 14 June → Rothera 20 June, f |
| `CIT/Research_Logs/Relung_Panen_Soil_Research_2026-10-25_F_Growing_Without_Soil_Precedents.md` | research log | 3 | L38: South Pole Food Growth Chamber (SPFGC), Amundsen-Scott, 2006  indoor room, ~22.7 m² cultivation, HPS lamps, N |
| `CIT/Specs/Byrd subnet/Byrd.md` | spec (other city) | 3 | L53: Highway access: Corrected 2026-07-06 — Byrd is a major two-highway junction, missed by this file despite bei |
| `CIT/Specs/Halley subnet/Halley.md` | spec (other city) | 4 | L7: Highway access: Revised 2026-10-03 (developer ruling): Halley is not a main-line stop on Hwy 7. The highway pa |
| `CIT/Specs/Janbogo subnet/Fort_McMurdo.md` | spec (other city) | 1 | L223: Unmarked background lore, 2026-07-16. It was at Fort McMurdo, still the historical seat of government at the e |
| `CIT/Specs/Mirny subnet/Kunlun.md` | spec (other city) | 1 | L142: Driest location in Tepenia: even less precipitation than Ariun Nuur or Amundsen Station; the air is essentiall |
| `CIT/Specs/Mirny subnet/Mirny.md` | spec (other city) | 1 | L55: The Antarctic Circle is the latitude below which the sun does not rise on the winter solstice and does not set |
| `CIT/Specs/Palmer subnet/Puerto_Abrigo.md` | spec (other city) | 1 | L54: ⚠ Puerto Abrigo is now the smallest settlement in Tepenia, below Amundsen Station's 6,857. |
| `CIT/Station_Heritage_Removal_Tracker.md` | reference/registry | 1 | L262: I-7  HIGH  Research topics shopping list: L304 DdU "Real Dumont d'Urville station history — French Antarctic |
| `LOC/Towns/Data/Real_Station_Inventory_Crossmatched.csv` | towns data | 18 | L15: amundsen,Amundsen,none found,-86.300000,-160.916667,wp_camps,"wp_camps=-86.300000,-160.916667",0.0,no,unknown, |
| `LOC/Towns/Data/Real_Station_Inventory_Method_and_Log.md` | towns data | 2 | L329: AYM00089799  NICO  -89.000  89.667  2935  Amundsen-Scott South Pole  110 |
| `LOC/Towns/Data/Real_Station_Inventory_Raw.csv` | towns data | 2 | L16: amundsen-scott-south-pole,Amundsen-Scott South Pole,Amundsen–Scott South Pole Station  Amundsen–Scott Sout |
| `LOC/Towns/Data/scripts/06_load_and_merge.py` | tool script | 1 | L48: 'Juan Carlos I', 'Wasa', 'Vernadsky', 'Halley VI', 'Rothera', 'Signy', 'Amundsen-Scott South Pole', 'McMurdo', |
| `LOC/Towns/Research_Logs/Radio_Physics_Followup3_Byrd_Legs_2026-10-04.md` | research log | 1 | L304: Search this session: "South Pole Station HF radio communications McMurdo HF reliability polar cap blackout win |
| `LOC/Towns/Towns_Data_Pass_Findings_and_Handoff_2026-10-04.md` | towns data | 2 | L54: By subnet (nearest city's subnet, NEAR_CITY plus CANDIDATE): Palmer 99 · Janbogo 80 · Mirny 50 · Halley 38 |
| `Worldspace/Locations-and-Levels/Real-World_Basis_Extrapolation_Method.md` | reference/registry | 1 | L335: ⚠ Amundsen Station and Concordia do not follow the <Subnet>/ pattern — read those two by name, never by |
| `ULM/00_RUNBOOK.md` | ULM method/status file | 1 | L2062: ⭐⭐ Climate Data/Precipitation_Falls_vs_Lands.md  The precipitation reference — four quantities, not one. |
| `ULM/02_Generators_Capability_and_Symbols.md` | ULM method/status file | 1 | L707: (Abowasa has no assignment) and for Amundsen Station, and it has never been written down. |
| `ULM/CST_Progress.md` | ULM method/status file | 1 | L231: Amundsen Station  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · |
| `ULM/Datasheet_Citations_To_Reread_2026-10-21.md` | ULM method/status file | 2 | L60: Vostok/Datasheets/Phase_5.md  Ports.md  L318  L459  Deep interior / plateau: Concordia · Ariun Nuur · Dome F |
| `ULM/Datasheet_and_PreTrip_Tracker.md` | ULM method/status file | 4 | L30: Amundsen Station |
| `ULM/Disciplines/Real-World_Basis_Extrapolation_Method.md` | ULM method/status file | 1 | L406: ⚠ Amundsen Station and Concordia do not follow the <Subnet>/ pattern — read those two by name, never by |
| `ULM/Extent_and_Area_APPROACH.md` | ULM method/status file | 1 | L143: Ice flow velocity  ⭐ a city on moving ice DEFORMS over 250 years. Amundsen Station drifts ~10 m/yr with the |
| `ULM/Location_Data-Input_To-Do.md` | ULM method/status file | 1 | L185: MISSING (33): Abowasa, Amundsen Station, Belgrano, Byrd, Cape Adare, Casey, Concordia, Davis, Denison, |
| `ULM/Pre-Contamination_Reviews/Shirayuki_Pre-Contamination_Review.md` | ULM method/status file | 4 | L445: «UNIV»/…/Amundsen_Station_Archive_and_Trucking_Network.md  114  45  69  65  94.2% |
| `ULM/RWBEM_Progress.md` | ULM method/status file | 1 | L200: Amundsen Station  7  ·  ·  ·  ·  ·  ·  ⛔ |
| `ULM/RealWorld_Basis_Input_Availability.md` | ULM method/status file | 1 | L46: Infrastructure, both outside the withheld tree. ⚠ With the standing warning that Amundsen Station and |
| `ULM/Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` | ULM method/status file | 5 | L167: Correctly left alone, and worth recording so a later sweep does not "fix" them: Amundsen Station's genuine |
| `ULM/Tools/audit_city_inputs.py` | tool script | 1 | L37: OUT_OF_SCOPE = {"Concordia", "Relung_Panen", "Amundsen_Station", "Shirayuki", "Sinheung", "Zhongshan_Opus", "Z |
| `ULM/Tools/build_datasheets.py` | tool script | 1 | L68: for extra in ("Concordia", "Shirayuki", "Sinheung", "Zhongshan", "Relung Panen", "Amundsen Station", "Palmer", |
| `ULM/Tools/build_pretrip.py` | tool script | 9 | L68: "Amundsen_Station": C("Amundsen_Station", "Amundsen Station", extra=["Amundsen-Scott"], reader="Amundsen_Stati |
| `ULM/Tools/check_must_open_coverage.py` | tool script | 1 | L36: OUT_OF_SCOPE = {"Concordia", "Relung_Panen", "Amundsen_Station", "Shirayuki", "Sinheung", "Zhongshan_Opus", "Z |
| `ULM/Tools/map_books_to_topics.py` | tool script | 2 | L14: 1. Parses Part 0 (national topics, the N# rows), and Part 2 (the 35 cities + Amundsen-Scott Station): each |
| `ULM/ULM_Input_Required_Reference.md` | ULM method/status file | 6 | L116: T0-1  Existence & designation — that it exists, and something to call it, even provisionally  05 §2.1  /hom |
| `ULM/ULM_Run_Progress.md` | ULM method/status file | 1 | L425: Amundsen Station  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · |

### 1.J · Map working stash

`Reference/Images/Maps/working-stash/`: `CHANGES.md` (L41) · `PROGRESS TRACKER - Read This First.md` (L22, flags the highway discrepancy, §3 C-2) · `data/cities.csv` (L39: `amundsen_station,Amundsen Station,Amundsen-Scott,-90.0,0.0,…,Destro…`) · `out/01_Tepenia_Cities.svg` · `out/05_Tepenia_Arcanet_Subnets.svg` · `scripts/tepenia_common.py` (7 hits; subnet color key `'Amundsen-Scott'`, L40) · and **18 archived SVGs**: `archive/{2026-10-03_1552, 2026-10-03_1556, 2026-10-03_1626, 2026-10-03_1723, 2026-10-03_1845, 2026-10-04_1018, 2026-10-04_1024, 2026-10-04_1029, 2026-10-04_1032}/{01_Tepenia_Cities.svg, 05_Tepenia_Arcanet_Subnets.svg}` (one label hit each).

### 1.K · Top level

| Path | Kind | What it holds |
|---|---|---|
| `TODO.md` | status | Thirteen cities missing six DoI marks (L233); Tower dimensions, throughput, timeline (L1385–L1432); Saints roster (L1365); Amundsen Time Code (L1676–L1697); power-supply placeholder (L1601–L1602); Mountain Pass "like Amundsen-Scott … rather thin" (L1750) |
| `DONE.md` | status | Integrity sweep closed incl. Amundsen Station (L252); Local_Cultures README status fixed (L398); Tower reframe and Split Brain (L446–L456); Juan Carlos archive origin (L465–L479); Kendra (L142) |

### 1.L · Universe repo pointer (outside the GDD)

`/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Amundsen_Station_Archive_and_Trucking_Network.md` exists (20,044 bytes). Cited by `…/Calethina/README.md` L58 as `Reference/Amundsen_Station_Archive_and_Trucking_Network.md`. **Not read** (separate repo, outside the brief).

### 1.N · WITHHELD: listed only, not opened

**`CIT/City_Megasheets/`** (33 files name the city; none opened):
- `Amundsen_Station/`: `Amundsen_Station_Community_Infrastructure.md` · `Amundsen_Station_Cross_Reference_Synthesis.md` · `Amundsen_Station_Full_Extrapolation.md` · `Amundsen_Station_Mega_Init.md` · `Amundsen_Station_Physical_Infrastructure_Attributes.md` · `README.md` · `Questline_Asset_Concept_Art/.gitkeep` (folder listing by `find`)
- `Byrd_Subnet/Byrd/`: `Byrd_Cross_Reference_Synthesis.md` · `Byrd_DLC_Reverse_Inferred_Guidelines.md` · `Byrd_Mega_Init.md` · `Byrd_Physical_Infrastructure_Attributes.md` · `README.md`
- `Halley_Subnet/Halley/`: `Halley_Full_Extrapolation.md` · `Halley_Mega_Init.md` · `Halley_Physical_Infrastructure_Attributes.md` · `README.md`
- `Halley_Subnet/Neumayer/`: `Neumayer_Cross_Reference_Synthesis.md` · `README.md`
- `Mawson_Subnet/Dome_Fuji/`: `Dome_Fuji_Cross_Reference_Synthesis.md` · `README.md`
- `Palmer_Subnet/Esperanza/README.md` · `Palmer_Subnet/Juan_Carlos/`: `Juan_Carlos_Cross_Reference_Synthesis.md` · `Juan_Carlos_Full_Extrapolation.md` · `Juan_Carlos_Mega_Init.md` · `Juan_Carlos_Physical_Infrastructure_Attributes.md` · `README.md`
- `Palmer_Subnet/Palmer_Subnet_Ultra_Megasheet/`: `Palmer_Cross_City_Throughways.md` · `Palmer_Subnet_Full_Extrapolation.md` · `Palmer_Subnet_Mega_Init.md` · `README.md`
- `Palmer_Subnet/Sejong/`: `README.md` · `Sejong_Cross_Reference_Synthesis.md` · `Sejong_Mega_Init.md`
- `Megasheet_Progress_Checklist.md`

**`Worldspace/Locations-and-Levels/Super_Ultra_Megasheet/`** (built on the megasheets, its README L4–L8; treated as withheld by caution, not opened beyond its first 8 lines): `README.md` · `Super_Cross_Regional_Patterns.md` · `Super_Cross_Regional_Throughways.md` · `Super_Ultra_Megasheet_Cross_Reference_Synthesis.md` · `Super_Ultra_Megasheet_Full_Extrapolation.md` · `Super_Ultra_Megasheet_Mega_Init.md`.

### 1.O · Outside the brief's three roots (listed for completeness)

- **`Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`** (1,155 lines): the Tower is anchored "at the South Pole (Amundsen Station)" (L221); At a Glance (L166–L212); base facility layout, power generation, tunnels, 1–2 km² surface complex (L921–L949); Hwy 22 through the station before Tower construction (L1055–L1060); still open (L1124–L1143).
- **`Storyline/`**: `DLC_01_Echoes_of_Amundsen.md` · `DLC_01_South_Pole_Side_Content_Suggestions.md` · `DLC_01_Enemy_Design_Options.md` · `DLC_Overview.md` · `DLC_PSB_Framework.md` · `DLC-Questlines/Subnet_Symbolic_Associations.md` · `DLC-Questlines/Mirny/DLC_7_Mirny_Main_Questline_Candidate_02.md` · `DLC-Questlines/Byrd/DLC_2_Byrd_Main_Questline_Candidate_03.md`.
- **`Dev-Road-Map/`**: `November_To-Do.md` · `Location_and_Culture_Build_Tracker.md` (L131) · `Weekly_To-Do_-_Current.md`.
- **`Background-Lore/`** ⛔ **NOT CANON, never an input** (19 files, not read): `Cities/README.md` · `Cities/City_History_Enhancement_Opportunities_Tracker.md` · `Cities/Historical_Vignettes_Review_Tracker.md` · `Cities/Historical_Vignettes_Progress_Tracker.md` · `Cities/City_History_Consistency_and_Enhancement_Tracker.md` · `Cities/Amundsen_Station_Enhancement_Opportunities.md` · `Cities/Amundsen_Station/Amundsen_Station_Historical_Vignettes_and_Informational_Sheets.md` · and 12 other cities' vignette/course-of-events files.
- `Neo-Races-and-Cultures/README.md` · `Neo-Races-and-Cultures/_Method/Progress_Tracker.md` · `Game-Mechanics/Core-Mechanics/Accomplishment_Weight_System.md` · `General-Overview-Notes/aspects_of_consideration.md` · `testing/QA_template.md` · `to-be-integrated/` (5 files incl. a saved climate web page and gear notes) · `Archive/` (29 files; not listed individually).

---

## 2 · What canon states about the city

Each fact: value · file:line. "As stated"; no reconciliation.

### 2.1 Identity and location
- **Name and basis:** "Amundsen Station"; *"Based on: Amundsen-Scott South Pole Station (USA), Geographic South Pole (90°00'S)"* · `SPEC` L1, L3.
- **Coordinates:** 90°00'S · `SPEC` L3; −90.000, 0.000 · `Reference/Real-World/Volcanism_and_Geothermal/00_City_Coordinates_From_Specs.md` L7.
- **Elevation and ice:** ~2,835 m on ice ~2,850 m thick; station drifts ~10 m/yr; marker periodically repositioned · `SPEC` L50.
- **Name split:** "In Tepenia, the station carries only Amundsen's name. Scott has his city. Amundsen has the Pole." · `SPEC` L52.
- **Access type:** ON · `SPEC` L6.
- **Status (later era, not a Second Interwar input):** Destroyed (Long Night War); DLC 1 setting · `SPEC` L4.
- **Solar UTC:** "—" · `CIT/Founding_Register.md` L75; "there is no solar time zone at the pole" · `CIT/Upper_Earth_Immigration_Composition.md` L1157.
- **Folder name of the spec:** `Specs/Amundsen-Scott subnet/` (path itself).

### 2.2 Population: Census I and II, and how it was set
- **Census I:** 1,121 humans / 5,736 robots / 6,857 (~84% robot; revised 2026-07-04) · `CEN` L519; `SPEC` L14.
- **Census II:** 913 humans / 3,978 robots / 4,891 (~81% robot; skeleton crew) · `CEN` L637; `SPEC` L15.
- **Retention (computed in the datasheet):** combined 71.33%, human 81.45%, robot 69.35% · `PASS/Datasheets/Step_0.md` L10.
- **Census I timing:** "before construction of Amundsen Tower and the onset of orbital colonization" · `CEN` L476. **Census II:** "immediately before the Long Night War, after decades of orbital migration via Amundsen Tower" · `CEN` L596.
- **How it was set:** the composite formula "applied naively, would put significant population at Amundsen" (pre-reduction 904,000 humans + 904,000 robots = 1,808,000, rank 9 · `CIT/Upper_Earth_Immigration_Composition.md` L768); humans reduced to **0.2%** and robots to **1%** of the computed figure, giving ~1,126 / ~5,763 / ~6,889 · same file L1157–L1159; "No overflow routed here" · L1023; then "two final randomization passes" · L1165; listed 1,126 / 6,889 · L1005.
- **Developer rulings on population:** "The official census governs its population" · `DRL` L1167 (`DR-58`); "Population: the official census governs … not 'low four digits'" (2026-10-18) · `Storyline/DLC_01_South_Pole_Side_Content_Suggestions.md` L20.
- **ULM works at full Census I** · `DRL` L522 (`DR-16`).
- **Smallest-settlement note:** Port Lockroy / Puerto Abrigo "now the smallest settlement in Tepenia, below Amundsen Station's 6,857" · `ULM/Extent_and_Density_Per_City.md` L136; `CIT/Specs/Palmer subnet/Puerto_Abrigo.md` L54.
- **Census note:** "a research and relay outpost, not a residential city. Human population is a skeleton crew embedded in a robot-majority operational facility" · `CEN` L468.

### 2.3 Role
- **Relay, not a subnet member:** "Inter-subnet relay — not a member of any subnet; served as the neutral switching point connecting all six subnets" · `SPEC` L5; same · `CIT/City_Relationship_Database.md` L57, L82; `LOC/Per-Subnet_Overview_Reference_Data.md` L11.
- **Seven subnets ruling:** *"let's say seven (counting Amundsen-Scott Station as separate, even though it's technically a nexus, and not a subnet)"* · `DRL` L528–L529 (`DR-17`).
- **Why central:** equidistant from all six subnet regions; "belonged to no subnet because it was too central to belong to any one" · `SPEC` L54.
- **Settled:** "Post-Falkland Treaty, as a neutral inter-subnet infrastructure installation rather than a conventional exile city … operated by a rotating technical staff maintaining the Arcanet relay hardware and the Amundsen Tower" · `SPEC` L150.
- **Mediation:** disputes "sometimes brought to Amundsen Station for mediation — not because it had formal authority" · `SPEC` L160.
- **Economy:** "Not applicable in the conventional sense … All supplies came in from elsewhere; nothing was produced for export" · `SPEC` L170; vision 2026-07-06: "scientific, technical, and mechanical maintenance" · `SPEC` L172; `CIT/City_Vision_Notes/Amundsen_Station.md` L19.
- **Archive:** "pre-Split-Brain Arcanet archive … the only place where all six subnets' histories can be compared and reconciled" · `SPEC` L180. Origin: Pergamino's archive "gradually superseded … hauled further and deeper into Antarctica … That 'bigger, better' archive is Amundsen Station's own" · `CIT/Specs/Palmer subnet/Pergamino.md` L166; timing open · same file L206; `CIT/Division_of_Industry/16_Per_City_Three_Tier_Run.md` L1136, L3564.
- **Tower base:** "site of the Amundsen Tower (space elevator)" · `SPEC` L8; "the Tower's ground base sits on the station site" · `SPEC` L66–L68; "anchored at the South Pole (Amundsen Station)" · `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md` L221.
- **Timekeeping:** the Amundsen Time Code is "Named after Amundsen Station, the neutral inter-subnet relay at the South Pole" · `TODO.md` L1690 (implementation open, L1694–L1697).

### 2.4 Amundsen Tower relation
- **Mechanism:** a space fountain, not a tension elevator; a polar elevator "is a physical non-starter" · `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md` L221–L224.
- **Numbers:** 150 km; 225,000 t guide tube; ~324 GW net (~2.16 TW gross); foundation ~2,700 m to bedrock · same file L168–L178.
- **Primary purpose:** continent-scale energy storage/regulation and bulk material mass-driving; passengers a side-application · same file L3–L15, L75 onward.
- **Base facility:** accelerator, power generation (nuclear/fusion plus possible geothermal taps), pellet return loop and maintenance tunnels in the ~2.7 km shaft; surface complex ~1–2 km² · same file L921–L949.
- **Completion:** ~2688 · `PASS/Datasheets/Step_0.md` L13; construction proper "plausibly in the final ~12-17 years before completion" · Tower file L1055–L1060, L1127.
- **Sequence:** Hwy 22 "running directly through the South Pole/Amundsen Station itself" was built before Tower construction · Tower file L1057–L1059.
- **Destruction and Split Brain:** the Tower's destruction caused the Planetary Split Brain · `SPEC` L203; debris "localized scrap mountain" · `SPEC` L178; `16` L3506.

### 2.5 Power supply file
- `LOC/Infrastructure/Amundsen_Power_Supply.md`: **0 bytes**.
- Described elsewhere as covering "the regulated continent-wide grid that Amundsen Tower ran" · `LOC/Infrastructure/Geothermal_Heating.md` L90; "Sibling to `Amundsen_Power_Supply.md` (the national grid)" · same file L3.
- "exists as an empty placeholder — meant to detail how Amundsen Tower actually gets its power … Explicitly deferred" · `TODO.md` L1601–L1602.
- Every non-geothermal city's heat "is a national service, delivered, and interruptible" · `Geothermal_Heating.md` L98 (table under L90).
- The city's own `Energy_Grid_Failure_Rationale.md` lookup: zero hits for the city name · `PASS/Datasheets/Step_1_and_2.md` L31.

### 2.6 Hostel, space workforce and maritime fleet (`DR-63` to `DR-69`)
- **`DR-63`:** later-era Rastra cruises ~45 km/h; derived travel times from Amundsen Station: Byrd ~1,277 km ~1.4 days; Janbogo/Zukelli ~1,960 km ~2.2 days; Concordia ~3,306 km ~3.7 days (road lengths estimated, not canon) · `DRL` L1276–L1284.
- **`DR-64`:** national custom of welcoming space workers on leave; most go to Byrd, Concordia, Janbogo or Zukelli, "the nearest by road from Amundsen Station"; **"Amundsen Station's role: It keeps hostel- or barracks-style infrastructure, not homes, only for the share of workers on leave who have no friends or family to go to. That keeps the station's scientists, engineers, cooks, chefs and other staff a solid majority of its population at any time."** · `DRL` L1293–L1295. Not written into any culture file · L1297.
- **`DR-65`:** working share staying at the hostel is 20%; ~287 beds Census I (~330 with surge), ~198 Census II (~228) · `DRL` L1303–L1305.
- **`DR-66`:** Byrd's share held near the others; overflow to other cities · `DRL` L1313–L1316.
- **`DR-67`:** Santa Luce scenario; "Amundsen Station's share goes to two new categories, the space workforce (11,492 Census I / 7,923 Census II) and the maritime fleet (11,490 / 7,922)" · `DRL` L1326; correction note · L1331.
- **`DR-68`:** scenario adopted; 50-50 nominal split · `DRL` L1339–L1340.
- **`DR-69`:** "Census I (before Amundsen Tower and orbital colonization): Amundsen Station's share … (22,982) is the maritime fleet alone; there is no space workforce in Census I. Census II: … space workforce (7,923) and maritime fleet (7,922)" · `DRL` L1351. Census rows · `CEN` L520, L638–L639.
- **Station's own population unchanged by the scenario:** 6,857 / 4,891 · `ULM/Population_Scenario_Santa_Luce_Redistribution_2026-10-28.md` L11, L45.

### 2.7 Division of Industry rows
- **§15 (culture sheet):** Arcanet relay operations / infrastructure maintenance 60%; Amundsen Tower operations 30%; Other / life support 10% · `CIT/Local_Cultures/Amundsen_Station/Amundsen_Station.md` L146–L148; caveat "assumes a civic economy" · L150.
- **`04`:** 6,857 · ARCANET · TOWER · relay 60% + Tower 30% · "not a city; special case" · `04` L79.
- **`09` §2:** D 2.50 · humans 1,121 · residents 6,857 · required 2,118 · workforce 6,297 · 33.6% · `09` L88.
- **`13`:** forced importer, ice sheet ("polar plateau") · `13` L73, L864, L921.
- **`16` Half B:** Subnet "Amundsen" · D 2.50 · workforce 6,296 · base 31.8% · mandated 61.4% · free 6.8% · src C · `16` L249.
- **`16` §35 "DETERMINED":** baseline 2,003 (31.8%), mandated 3,864 (61.4%), free 429 (6.8%); distinctive tier 4,293 (68.2%); relay 2,576 (60% of distinctive), Tower ops 1,288 (30%); free tier = "Other / LIFE SUPPORT" · `16` L3456–L3481. Food term at 10% (ice-sheet forced importer) · `16` L114, L3458.
- **Archive:** "Holds the consolidated federal archive; §15 has no line for it — ABCC candidate" · `16` L1238.
- **DLC hazard item parked by the developer 2026-09-02** ("that's a problem for the future") · `16` L3578.

### 2.8 Founding Register row
- `| Amundsen Station | Amundsen | — | ✅ | Multi-subnet technical crews on rotation; no founding nation (neutral by design) | Neutral inter-subnet infrastructure; the station's neutrality was built into its staffing. | Specs/… L152; DR-44 | — |` · `CIT/Founding_Register.md` L75.
- `DR-44`: "Amundsen Station: rotating multi-subnet technical crews" (not nation-based) · `DRL` L929.
- Spec: "Multi-subnet technical crews, with no dominant national or cultural community" · `SPEC` L152.

### 2.9 Composition
- **Tiers:** Primary China, USA · Significant Japan, Germany, UK, South Korea, Canada, Australia · Notable Argentina, Norway *(Amundsen heritage — Saint Roald)*, New Zealand, Chile *(unique Union Glacier route advantage)* · `SPEC` L19–L21; `CEN` L464–L466 (Chile annotation adds "closest overland approach from any inhabited continent").
- **Per-nation table:** USA 22.80% · China 19.31% · UK 10.57% · Germany 10.09% · Japan 9.59% · Canada 6.20% · South Korea 5.70% · Australia 5.22% · Argentina 3.59% · New Zealand 3.59% · Norway 1.67% · Chile 1.67% · `SPEC` L31–L42; within-tier values randomized, no finding may rest on them · `DRL` L463–L476 (`DR-12`).
- **Derivation:** corridors "McMurdo chain (Christchurch → McMurdo → Pole by air) and Union Glacier direct (Punta Arenas → Union Glacier → Pole by air)"; tier drivers · `CIT/Upper_Earth_Immigration_Composition.md` L648–L656.
- **What the table describes (culture sheet's own reading):** "which nations' Antarctic programs contributed rotating technical staff" · `CIT/Local_Cultures/Amundsen_Station/Amundsen_Station.md` L30.

### 2.10 Relationships
- **Concordia:** structural and historical; its destruction is why Concordia cannot communicate with Byrd, Halley, Mawson, Mirny or Palmer · `SPEC` L193.
- **Highways:** Hwy 22 passes directly through · `LOC/Infrastructure/Highways.md` L141, L146; Hwy 175 and Hwy 59 end at ramps with Hwy 22 · `Highways.md` L62, L64 (see C-2).
- **Direct highway neighbors:** Hwy 22 (Byrd west / Zhongshan tri-junction east), Hwy 175 (toward the Hwy 183 junction / Ross Sea region), Hwy 59 (toward Halley) · `CIT/City_Relationship_Database.md` L84.
- **Debris bypass (proposed 2026-07-09):** a maintained bypass through or around the debris field on Byrd's freight route · `City_Relationship_Database.md` L85, L135.
- **Post-Tower connections** (all "medium" or "strong"): Halley (Hwy 59 Arcanet Line), Neumayer (designed the Tower), Sanay (Halley subnet nexus), Pergamino (archive), Kunlun (observatory tracked Tower infrastructure), Fort McMurdo (capital status followed the Tower), Cape Adare (documentation method) · `CIT/City_National_Connections.md` L43, L51–L53, L129, L253–L254, L325–L326, L356, L426, L453.
- **Excluded:** from refugee-affinity mapping · `CIT/City_Refugee_District_Affinities.md` L7; from capital candidates · `CIT/National_Capital_Candidates.md` L47.
- **Saints:** St. Roald (Amundsen Station) · `Worldspace/National_Holidays.md` L41.
- **Airports:** no airport · `LOC/Infrastructure/Airports.md` L50, L54; Mountain Pass Airport "reasonably accessible … Amundsen Station (via the nearby Hwy 22 dual-junction)" · `Airports.md` L18.
- **Ports:** landlocked; reached only by highway from a coastal port · `LOC/Infrastructure/Ports.md` L205, L740.

### 2.11 Climate (ruling: Amundsen-Scott is the official reference, 2026-09-04 · `SPEC` L61–L78)
- Mean annual −49.1 °C · `SPEC` L81; READER L8.
- Coldest July/August avg −60 °C; warmest Dec/Jan avg −28 °C · `SPEC` L82.
- Records: high −12.3 °C (December); low −82.8 °C (June) · `SPEC` L83.
- Precipitation: gauge 2.1 mm · `SPEC` L86; falls ~70 mm, lands ~75 mm (~90% retention) · `SPEC` L93–L94; stake-farm accumulation ~70–80 mm · `Reference/Real-World/Climate Data/Precipitation_Falls_vs_Lands.md` L104.
- Wind 5–7 m/s average · `SPEC` L85; "COLD, overwhelmingly … Air movement is close to irrelevant" · `SPEC` L98.
- Polar night ~Mar 24 → Sep 21 (~182 days); midnight sun ~Sep 22 → Mar 23 (~183 days) · `SPEC` L101–L102.
- Monthly table · `SPEC` L108–L121.

### 2.12 Extent and ground
- Extent table: 6,857 · 1 km² at 10k/km² · 1 km² at 7k/km² · Site "South Pole" · `ULM/Extent_and_Density_Per_City.md` L629.
- 0% rock (cheap ice) · same file L578.
- Tower surface complex ~1–2 km² · Tower file L943–L948.

### 2.13 Symbol, culture-sheet and other attributes (conclusion-tier; listed, not inputs)
- Planet Neptune; element paused · `CIT/City_Symbolic_Substrate/City_Symbol_Assignments.md` L152.
- Enneagram: Head / Compliant / Competency · `CIT/City_Enneagram_Personalities/Amundsen_Station/Amundsen_Station.md` L5–L15.
- Regional label "Unification/Scientific" · `LOC/Per-Subnet_Guides/South_Pole.md` L8.
- Tours "of six months to two years" · `CIT/Local_Robot_Culture/Amundsen_Station/Amundsen_Station.md` L14 (provisional sheet, L22–L23).

### 2.14 DLC 1 (later era; recorded because the expansion is for this DLC)
- Seven DLCs, one for "the South Pole inter-subnet relay (Amundsen Station)" · `Storyline/DLC_Overview.md` L3.
- "definitely a full town during the Second Interwar Period" (developer, 2026-10-18) · `Storyline/DLC_01_South_Pole_Side_Content_Suggestions.md` L21.
- Underground shaft/tunnel network and zones · `Kendra Heinrich/DLC_South_Pole_Level_Design.md` L28–L39, L107–L110.
- Kendra locked inside "the actual Amundsen-Scott South Pole Station — the pre-war scien…" · `Storyline/DLC_01_Echoes_of_Amundsen.md` L172, L290.

---

## 3 · Contradictions and stale statements (stated flatly; not adjudicated)

| # | Subject | One side | Other side |
|---|---|---|---|
| **C-1** | Subnet membership | "not a member of any subnet" · `SPEC` L5; `City_Relationship_Database.md` L82; "Subnet: None" · `Local_Cultures/…/Amundsen_Station.md` L9; Robot culture L28 | Subnet column "Amundsen" · `CEN` L519, L637; `Founding_Register.md` L75; `09` L88; `16` L249; `Extent_and_Density_Per_City.md` L629. `DR-17` counts it as a seventh "subnet" while calling it "technically a nexus, and not a subnet" · `DRL` L528–L529. The spec folder is named `Specs/Amundsen-Scott subnet/` |
| **C-2** | Which highways reach it | "a genuine three-highway node … Hwy 175 … terminates here … Hwy 59 … also terminates here" · `SPEC` L7; `City_Relationship_Database.md` L83; `Mawson_Byrd_Amundsen_Reference.md` L252 | Hwy 59 and Hwy 175 end at ramps with Hwy 22; Hwy 59 "Does not reach the South Pole" · `Highways.md` L62, L64, L191–L193, L214–L220; "ONE highway reaches Amundsen Station. Two others feed into it, and neither touches the station" · `Mawson_Byrd_Amundsen_Reference.md` L274–L281 (same file as L252); `16` L3529–L3538. The map tracker flags it · `Reference/Images/Maps/working-stash/PROGRESS TRACKER - Read This First.md` L22 |
| **C-3** | Direction from the Pole | Hwy 175 "south toward the Hwy 183 junction / Ross Sea region" · `City_Relationship_Database.md` L84 | "Everything from the South Pole is north" · `SPEC` L50 |
| **C-4** | Precipitation | "~20–25mm annual precipitation" · `Local_Cultures/…/Amundsen_Station.md` L44 | 2.1 mm gauge; ~70 mm falls; ~75 mm lands · `SPEC` L86, L93–L94; ~70–80 mm · `Precipitation_Falls_vs_Lands.md` L104 |
| **C-5** | Driest site | "the driest site in Tepenia" · `Local_Cultures/…` L44; Robot culture L67 | Kunlun: "even less precipitation than Ariun Nuur or Amundsen Station" · `CIT/Specs/Mirny subnet/Kunlun.md` L142 |
| **C-6** | Scott's Saint name | "St. Richard (Scott …)" · `Local_Cultures/…` L170; `Mawson_Byrd_Amundsen_Reference.md` L253; `16` L3540 | "St. Robert — Robert Falcon Scott"; "St. Richard — Richard Byrd" · `Worldspace/National_Holidays.md` L39, L43; `TODO.md` L1365 |
| **C-7** | "Highest robot proportion of any population center" | `Local_Cultures/…` L11; Robot culture L12–L13; `Mawson_Byrd_Amundsen_Reference.md` L232; `16` L3465–L3466 | Kunlun and Dome Fuji have zero humans · `16` L116 ("Kunlun and Dome Fuji have ZERO humans"); scenario L47 |
| **C-8** | Census I figures | 1,121 / 5,736 / 6,857 · `CEN` L519 | ~1,126 / ~5,763 / ~6,889 · `Upper_Earth_Immigration_Composition.md` L1159; 1,126 / 6,889 · same file L1005 |
| **C-9** | Tower staff in the Census I era | Census I is "before construction of Amundsen Tower" · `CEN` L476; `DRL` L1351; the ULM works at full Census I · `DRL` L522 | The DoI mandate assigns 30% of the distinctive tier (1,288 workers) to Tower operations on the Census I workforce · `16` L3456–L3474; the station was settled post-Treaty to maintain "the Arcanet relay hardware and the Amundsen Tower" · `SPEC` L150 |
| **C-10** | When the relay began | Settled post-Treaty as the relay · `SPEC` L150, L54; Arcanet "gradually connected subnet by subnet" before Tower construction · Tower file L1057 | "once the Amundsen Tower's completion connected all six subnets through a single relay for the first time" · `City_National_Connections.md` L5 |
| **C-11** | Founding wave | "no founding nation (neutral by design)" · `Founding_Register.md` L75; "no 'founding wave'" · `Local_Cultures/…` L30 | "Australia via McMurdo chain sets the founding wave character alongside NZ" · `Upper_Earth_Immigration_Composition.md` L652 |
| **C-12** | Namesake as a composition driver | Norway "*(Amundsen heritage — Saint Roald)*" · `SPEC` L21; `CEN` L466; `Local_Cultures/…` L28; "Norway's Amundsen heritage (Saint Roald) gives it cultural significance" · `Upper_Earth_Immigration_Composition.md` L654, L656 | "namesakes are never a basis for data" · `DRL` L743–L752 (`DR-32`); "never derived from its namesake" · `DRL` L684 (`DR-28` D2) |
| **C-13** | Air corridors | Composition corridors arrive at the Pole "by air" · `Upper_Earth_Immigration_Composition.md` L648 | Amundsen Station has no airport in Tepenia; access by highway only · `Airports.md` L50–L56 |
| **C-14** | Other cities' founders inside this sheet | "the USA founded Byrd" · `Local_Cultures/…` L30 | Byrd founded by a joint team of first-wave Tepenians, not an Upper-Earth country · `DRL` L924 (`DR-44` row), `Founding_Register_TimeZone_Audit…` L223. Same line calls eight nations "the same six-nation core" · `Local_Cultures/…` L30 |
| **C-15** | Symbol entry exists? | Neptune, element ⏸️ · `City_Symbol_Assignments.md` L145–L152; "Neptune + (was Electromagnetism)" · `DRL` L133; "Neptune + Magnetism" · `ULM/ULM_Input_Available_Audit.md` L86 | "No entry found — not in `City_Symbol_Assignments.md`" · `Mawson_Byrd_Amundsen_Reference.md` L243; "No Symbolic Substrate entry exists … absent from `City_Symbol_Assignments.md`" · `16` L3544–L3545; robot culture: "Genuinely absent from `city-symbol-pairs.md`" · Robot culture L135. The element itself differs between the three files on the left |
| **C-16** | Concordia's lost subnets | Byrd, Halley, Mawson, Mirny, Palmer · `SPEC` L193 | Byrd, Halley, Mawson, Palmer (Mirny absent) · `Local_Cultures/…` L207 |
| **C-17** | Division of Industry status | "AMUNDSEN STATION — DETERMINED *(closes the roster)*" · `16` L3451 | "both still need their Division of Industry established" · `ULM/City_Input_Gaps_2026-10-27.md` L11; "Amundsen Station research and its Division of Industry are still to be done" · scenario L104; "(not started)" · `Reference/Real-World/Inspiration_Place_Research/_SESSION_RESUME_2026-10-29.md` L70 |
| **C-18** | Workforce | 6,297 · `09` L88 | 6,296 · `16` L249 (the formula `robots + 0.5 × humans`, `16` L27 and L125, gives 6,296.5) |
| **C-19** | Hostel figures in Census I | ~287 beds Census I · `DRL` L1305 (`DR-65`); scenario §7 L141 and §8 L166 | "there is no space workforce in Census I" · `DRL` L1351 (`DR-69`); `CEN` L520; scenario header: "the Census I columns of those sections are superseded" · scenario L3 (`DR-65` itself carries no such note) |
| **C-20** | Was the census edited? | "No census row, spec, Division of Industry row or megasheet was changed"; "It waits for the census rework" · scenario L3–L4 | "Applied 2026-10-28: `Official_Population_Census.md`: 26 Census I rows and 22 Census II rows changed …" · `DRL` L1352–L1355; rows present · `CEN` L520, L638–L639 |
| **C-21** | Ruling number on the census rows | Rows say "`DR-68`, Option A" · `CEN` L520, L638 | Option A is recorded as `DR-69` · `DRL` L1346–L1351 |
| **C-22** | What kind of place, and who lives there | "skeleton crew" · `SPEC` L15; `CEN` L468, L637; "never primarily a population center … a facility" · `SPEC` L150; "People came from their cities, did their work, and went home" · `SPEC` L158; "runs primarily on automated systems" · `Upper_Earth_Immigration_Composition.md` L1159 | "definitely a full town during the Second Interwar Period" · `Storyline/DLC_01_South_Pole_Side_Content_Suggestions.md` L21 (that file flags the reconciliation as open, L73); "scientists, engineers, cooks, chefs and other staff a solid majority of its population at any time" · `DRL` L1295; developer direction "a much larger population" · `candidates/Amundsen_Station.md` L7 |
| **C-23** | Ice thickness | ~2,850 m · `SPEC` L50; `16` L3458; `Mawson_Byrd_Amundsen_Reference.md` L259 | ~2,700 m to bedrock · Tower file L176, L921–L923; `TODO.md` L1388 |
| **C-24** | Power file | Covers "the regulated continent-wide grid that Amundsen Tower ran" · `Geothermal_Heating.md` L90 | The file is 0 bytes; "empty placeholder … held for later" · `TODO.md` L1601–L1602 |
| **C-25** | Tower completion and build length | ~2688 (resolved 2026-08-05) · `TODO.md` L1420; Tower file L1060, L1127 | "~2630–2640" · `TODO.md` L1402; "65–75 year build window" · Tower file L63, L193, L583 (superseded per L1063); the universe repo "still states the older ~2630-2640 completion date" · Tower file L1128–L1131; "one-third of the way through … construction began" · `Upper_Earth_Immigration_Composition.md` L1205 |
| **C-26** | Tower type wording | Space fountain; a polar tension elevator is "a physical non-starter" · Tower file L221–L224 | "the space elevator anchored at the geographic South Pole, exploiting the rotational axis as the optimal anchor point for a permanent surface-to-orbit tether" · `Upper_Earth_Immigration_Composition.md` L1205 |
| **C-27** | Orbital population | 10,104,964 · `CEN` L673; 10.10M · Tower file L179 | ~11.36M · `TODO.md` L1336, L1390; ~9.2 million · `Upper_Earth_Immigration_Composition.md` L1279 |
| **C-28** | Megasheet folder size | "(**5** files)" · `PASS/00.0_Pre-Trip_Inspection.md` (§F row, L401 of the file); "inside a folder of 7 files" · `PASS/Datasheets/Phase_3.md` L9; "4 files, **no README.md**" · `Mawson_Byrd_Amundsen_Reference.md` L244 | On disk (listing only): 6 `.md` files including `README.md`, plus `Questline_Asset_Concept_Art/.gitkeep` |
| **C-29** | Datasheets built? | "Datasheets not yet built for this city (November item N-5)" and "(**not yet built** …)" · `PASS/00.0_Pre-Trip_Inspection.md` L54 and §I row | 19 datasheet files exist (audit: "DATASHEETS: 19 files ok", §5) |
| **C-30** | Line drift in sheet citations | Datasheet/Pre-Trip cite `Airports.md` L47, L51; `Ports.md` L459, L717; `Inspirational-Influences.md` L279–L283 · `PASS/Datasheets/Phase_5.md` L14–L19; `Step_3.md` L9–L11 | Those lines are now `Airports.md` L50, L54; `Ports.md` L482, L740; `Inspirational-Influences.md` L310–L314 (re-read 2026-10-29). The Pre-Trip's own verifier still reports "66 claims, 0 fail" (§5) |
| **C-31** | Verifier failures | "fail **two** verifier checks" · `ULM/City_Input_Gaps_2026-10-27.md` L82 | Today's run: **3 FAIL** (D2, D3, D6) · §5 |
| **C-32** | Outer README | "No subnet layer … one level shallower" and spec path `../../Specs/Amundsen_Station.md` · `CIT/City_Development_Passes/Amundsen_Station/README.md` L3, L36 | The pass lives one level deeper at `Amundsen_Station/Amundsen_Station/`; the spec is at `Specs/Amundsen-Scott subnet/Amundsen_Station.md` (inner README L37) |
| **C-33** | Concept-art folder | "a dedicated `Amundsen_Station/` folder … (a single city, no subnet)" · `CIT/City_Concept-Art/README.md` L3, L7; Phase_3 datasheet checks `City_Concept-Art/Amundsen_Station/Amundsen_Station` · `Phase_3.md` L8 | "needs a nested concept-art folder of its own … Not created yet" · `Dev-Road-Map/November_To-Do.md` L103; on disk only `City_Concept-Art/Amundsen_Station/.gitkeep` |
| **C-34** | Neo-race catalog | "needs no neo-race catalog" · `Dev-Road-Map/November_To-Do.md` L103 | Folder `Neo-Races-and-Cultures/Amundsen_Station/` exists (`.gitkeep` only); the Pre-Trip lists a catalog path as "(file does not exist)" |
| **C-35** | Calethina citation path | `Reference/Amundsen_Station_Archive_and_Trucking_Network.md` · `…/Calethina/README.md` L58 | Not in the GDD's `Reference/`; the file is in the universe repo's `Reference/` (§1.L) |
| **C-36** | Archive's DoI line | "Holds the consolidated federal archive; §15 has no line for it — ABCC candidate" · `16` L1238 | §15 lists relay 60 / Tower 30 / life support 10, no archive · `Local_Cultures/…` L146–L148; spec economy names relay and Tower only · `SPEC` L170 |
| **C-37** | Spec open question already answered | Highway question listed as open · `SPEC` L227 | Self-marked "resolved 2026-07-06 … never swept afterward" · same line |
| **C-38** | Saints' venue | "Disputes … brought to Amundsen Station" (spec) fine; Spec L230 asks whether a St. Roald observance exists | Culture sheet names "St. Roald's Day *(placeholder name)*" as a holiday · `Local_Cultures/…` L225 |

---

## 4 · What the developer has said about expanding it

Searched `Dev-Road-Map/`, the status files (`MASTER_Process_Tracker.md`, `City_Input_Gaps_2026-10-27.md`, `ULM_Run_Progress.md`, `_SESSION_RESUME_2026-10-29.md`), `DRL`, `Worldspace/` and (because the expansion is for the DLC) `Storyline/`, for "Amundsen" near *expand, expansion, larger, intricate, DLC, bigger, complex*. Exact search: `grep -rn -i "intricate|much larger population|expand it|be expanded|its expansion|expansion of amundsen|expanding amundsen"` and `grep -rn -i "amundsen" Dev-Road-Map … | grep -i "expan|larger|intricate|DLC|bigger|complex|expand|grow|scale"`.

**Statements found, in date order:**

1. **2026-09-07** (as an aside, about Mountain Pass): *"…it's rather something more along the lines of something like Amundsen-Scott Station, so it's extremely likely that the data will probably end up being rather thin."* · `TODO.md` L1745–L1756.
2. **2026-10-18** (DLC idea): two pathways to the station, overland and below the ice; *"The population of the South Pole (Amundsen-Scott Station) would be in the low four digits, perhaps a couple of thousand … A couple of thousand people is a town … an underground network of tunnels, stations, actual living infrastructure"* (paraphrase recorded as the developer's structure) · `Storyline/DLC_01_South_Pole_Side_Content_Suggestions.md` L11–L17.
3. **2026-10-18** (answers): *"Population: the official census governs … (Census I 6,857; Census II 4,891) … not 'low four digits.' The earlier phrase was a rough guess"*; *"definitely a full town during the Second Interwar Period … What it is like after the Long Night War is still to be determined"*; one general underground network plus deeper chambers; dangers held off "until it is known what the place is actually like" · same file L20–L24. Open items · L72–L75.
4. **2026-10-18 to 10-21** (`DR-58`): *"Amundsen Station: The official census governs its population."* · `DRL` L1167.
5. **2026-10-21** (November setup): *"Amundsen-Scott Station needs a nested concept-art folder of its own (it will appear in the game, so it will need concept art eventually), even though it needs no neo-race catalog."* · `Dev-Road-Map/November_To-Do.md` L103. Excluded from November: *"Amundsen Station (to be expanded first)"* · same file L66 (D-6), L153.
6. **2026-10-21** (tracker): *"Amundsen Station is not in the November run — the developer wants to expand it first"* · `ULM/MASTER_Process_Tracker.md` L437; scope line *"(the developer will expand it first)"* · L367.
7. **2026-10-26** (picks): *"the Timbuktu manuscript libraries in Mali could additionally also supply inspiration material to Amundsen-Scott Station"* · `Reference/Real-World/Inspiration_Place_Research/candidates/_DEVELOPER_ADDITIONS.md` L5–L6.
8. **2026-10-27** (drafting direction): *"the city is to be expanded into a much larger population and a far more complex, intricate and engaging location for a downloadable-content setting"* · `Reference/Real-World/Inspiration_Place_Research/candidates/Amundsen_Station.md` L7; facet F13 "Much larger population; layered and buried structure; hidden spaces; rich civic, leisure and cultural life" · L27. (Recorded as "Developer direction for this draft"; the file does not quote the developer verbatim.)
9. **2026-10-27/28**: *"Amundsen Station (waits for its expansion; fails the sheet verifier by design)"* · `ULM/City_Input_Gaps_2026-10-27.md` L10, L82; developer, 2026-10-28: *"make sure to remind me about Relung Panen, Amundsen Station and the Mirny leftovers"* · L4; *"research, design & development, and determination for Relung Panen and Amundsen-Scott (Amundsen Station, the city: confirmed by the developer, 2026-10-28). Among other things, both still need their Division of Industry established."* · L11.
10. **2026-10-28** (`DR-64`): the station's "scientists, engineers, cooks, chefs and other staff" are "a solid majority of its population at any time"; hostel, not homes, for space workers on leave · `DRL` L1295.
11. **2026-10-29**: the brief for this unit: "much larger population, a far more complex and intricate location for its DLC" · `Research_Logs/Evening_Wave_Briefs_Amundsen_and_Ethnic_Origin_2026-10-29.md` L16; "Amundsen Station research and determination (nothing started)" · `_SESSION_RESUME_2026-10-29.md` L63, L70.

**Not found:** any ruling that sets a new population figure; any statement of what "expansion" changes in the census, in `16` §35, or in the spec; any statement that reverses `DR-58` ("the official census governs"). Searched `DRL` in full for "Amundsen" (15 hit lines, §1.F): no expansion ruling.

---

## 5 · Raw tool output (pasted, not summarized)

### 5a · `python3 Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/audit_city_inputs.py --city Amundsen_Station --out <scratchpad>/audit_amundsen.md` (run 2026-10-29; exit 0)

Terminal:
```
wrote /tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/a4f4478c-4c10-4425-b67b-16739b0736bb/scratchpad/audit_amundsen.md
Amundsen Station       tests 40  GAP 1  note 3 
      GAP  T1-G7 Inspirational-Influences entry with tiered picks — no entry found under the city's name
```

The city's block from the report file:
```
## Amundsen Station  (Amundsen_Station)

| Test | Result | Detail |
|---|---|---|
| T0-1 spec exists | ok | 231 lines |
| T0-2 Geographic Basis + `Based on:` | ok | Based on: Amundsen-Scott South Pole Station (USA), Geographic South Pole (90°00' |
| T0-3 census entry | ok | entry L462 |
| T0-3 census rows (Census I / II) | ok | Census I rows 1 · Census II rows 1 |
| T0-4 `Arcanet Subnet:` | ok | Inter-subnet relay — not a member of any subnet; served as t |
| T1-G2 spec monthly table | ok |  |
| T1-G2 spec Precipitation-regime block | ok |  |
| T1-G2 climate READER file | ok | 17 lines |
| T1-G3 `Significance:` | ok |  |
| T1-G3 Economy & Industry section | ok | 726 chars |
| T1-G3 own row in Division_of_Industry/16 (membership, not mention) | ok | row L249 |
| T1-G4 Founding Register row ruled | ok | row L75, status ✅ |
| T1-G4 spec `Founding population:` | ok |  |
| T1-G4 spec `Settled:` | ok |  |
| T1-G5 `Access type:` token | ok | ON |
| T1-G5 named in Highways.md | ok | 3 lines |
| T1-G5 named in Airports.md | ok | 3 lines |
| T1-G5 named in Ports.md | ok | 4 lines |
| T1-G6 named in universe history / Second Interwar era files | ok | 8 hit lines |
| T1-G7 Inspirational-Influences entry with tiered picks | **GAP** | no entry found under the city's name |
| T1-G8 composition tier table (census entry) | ok |  |
| T1-G8 Upper_Earth_Immigration_Composition names the city | ok | 9 lines |
| T2-1 Local_Cultures file (read LAST, existence only) | ok |  |
| T2-1 Megasheet folder (WITHHELD, existence only) | ok |  |
| T2-5 Local_Robot_Culture file | ok |  |
| T2-5 Enneagram personality file | ok |  |
| T2-6 named in City_Relationship_Database.md | ok | 11 lines |
| T2-6 named in City_Cross_Subnet_Relationships.md | note | no mention |
| T2-6 named in City_National_Connections.md | ok | 10 lines |
| T2-7 concept art holds real images | note | empty or missing folder (optional input) |
| T2-8 extent / area (own row or coastline ruling) | ok | rows 1 / other lines 1 |
| Neo-race catalog exists | note |  |
| PRE-TRIP sheet exists | ok | 568 lines |
| PRE-TRIP verification: no missing inputs | ok | MISSING-INPUT=0 |
| PRE-TRIP verification: line claims all OK | ok | 66 claims, 0 fail |
| Position-Coverage ledger exists | ok |  |
| DATASHEETS: 19 files | ok | 19 files |
| DATASHEETS: none a stub | ok |  |
| DATASHEETS: DRAFT marking on every file | ok |  |
| README has the Datasheets row | ok |  |
```

*(Note, not part of the output: the T1-G7 GAP is the false positive already recorded at `ULM/City_Input_Gaps_2026-10-27.md` L29 and L82; the entry exists at `CIT/Inspirational-Influences.md` L310 under the double-name heading.)*

### 5b · `python3 Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/verify_city_sheets.py Amundsen_Station` (run 2026-10-29; exit 1)

```
== Amundsen Station: 20 checks, 3 FAIL, 1 NOTE
  PASS D1 19 manifest files                             all present
  FAIL D2 spine MUST OPEN covered                       not covered: P1 Stations; P5 Locations; P7 01_Burden_Scoring_Model.md; P7 jobs_professions_and_fields
  FAIL D3 coverage line on phase sheets                 missing on: Step_0.md, Step_1_and_2.md, Phase_2.md, Phase_3.md, Phase_4.md, Phase_5.md, Phase_6.md, Phase_7.md, Phase_8.md, Phase_9.md, Phase_10.md
  PASS D4 Step_5 deliberate stub                        stub statement present
  PASS D5 Step_6 section inventory                      ten sections incl. Phase 10
  FAIL D6 DoI reliability gate cited (Phases 1, 4, 7)   not cited in: Step_1_and_2.md
  NOTE D7 later-era words                               1 line(s) to READ: Step_7.md L13
  PASS D8 inference markers (read, never strip)         none
  PASS D9 DRAFT marking                                 all marked
  PASS D10 shared sheets cited exist                    all exist
  PASS D11 README Datasheets row                        
  PASS D12 Step_-1 spec ranges and Step_0 census rows   line-range citations present; census named
  PASS P1 sections A-N                                  ABCDEFGHIJKLMN
  PASS P2 step/phase blocks                             steps 12, governing 11, T8 11 (want 12, 11, 11)
  PASS P3 spine addresses in section D                  all present
  PASS P4 datasheet files pointed to                    all 19
  PASS P5 aliases in section A                          all 2 names present
  PASS P6 verification block                            0 missing inputs; 66 claims, 0 failed
  PASS P7 placeholders / carried names                  none
  PASS P8 ledger exists                                 
```

---

## 6 · Rulings the developer must make before a Division of Industry determination or a ULM pass can be written

**Questions only. No proposed answers.**

### 6.1 What "expansion" means
1. What does "expand it first" change: the population figure, the physical extent, the city's type (facility or town), its role, or all of these?
2. Is the expansion a change to Second Interwar canon (the ULM's frame), to the post-war DLC site, or both?
3. Which existing files is the expansion allowed to change: the spec, the census, `16` §35, the culture sheets, the datasheets, the Pre-Trip sheet?
4. Does the ULM pass run after the expansion is written, or is the expansion itself done through the ULM?
5. Does `16` §35 ("DETERMINED", `16` L3451) stand, or is the Division of Industry determined again after the expansion (C-17)?

### 6.2 Population
6. Does `DR-58` ("The official census governs its population", `DRL` L1167) still stand, given the direction to a "much larger population" (`candidates/Amundsen_Station.md` L7)?
7. If the figure changes: what is the new Census I figure, and what is the new Census II figure?
8. If the figure changes: where do the added people come from in the national totals (other cities' rows, the non-city groups, or an increase in the national total)?
9. Does the 0.2% human / 1% robot reduction (`Upper_Earth_Immigration_Composition.md` L1159) still describe how the figure was set?
10. Which Census I figure is canon: 1,121 / 5,736 / 6,857 (`CEN` L519) or 1,126 / 5,763 / 6,889 (`Upper_Earth_Immigration_Composition.md` L1005, L1159) (C-8)?
11. Are the station's people residents, rotating staff, or both, and in what proportion ("skeleton crew", "full town", "solid majority … scientists, engineers, cooks, chefs") (C-22)?
12. How long is a rotation, if there are rotations (the only stated length is a provisional sheet's "six months to two years", Robot culture L14)?
13. Do the space workforce and the maritime fleet have any residence, office or administrative tie to the station beyond the hostel?
14. In Census I, with no space workforce (`DR-69`), does the station hold any hostel at all, and do `DR-65`'s Census I bed figures stand (C-19)?

### 6.3 Composition
15. Does the current tier table stand, and does it describe rotating staff, residents, or both?
16. How is composition derived for a site on every longitude, where the solar-zone window does not apply (`Founding_Register_TimeZone_Audit…` L20)?
17. Does Norway's "*(Amundsen heritage — Saint Roald)*" annotation stay under `DR-32` (namesakes never a basis for data) (C-12)?
18. Does Chile's "Union Glacier route" stand as an access reason when the station has no airport and the corridors were written "by air" (C-13)?
19. Is the robot share (~84% Census I, ~81% Census II) kept for an expanded population?

### 6.4 Role
20. Is the station a member of a subnet, a seventh "subnet" (`DR-17`), or neither, and which label do the census, register and DoI files carry (C-1)?
21. Did the station work as the inter-subnet relay from settlement (post-Treaty) or only from the Tower's completion (C-10)?
22. Did Tower-operations staff exist in the Census I era, given Census I is "before construction of Amundsen Tower" (C-9)?
23. Is the national archive a mandated sector of the station (no §15 line today; ABCC candidate, `16` L1238), and from when (archive relocation timing, `Pergamino.md` L206)?
24. Is the mediation role a formal institution or an informal practice, and does it employ anyone?
25. What scientific work, if any, is done at the station beyond relay and Tower maintenance ("scientific, technical, and mechanical maintenance")?
26. Which highways reach the station itself: one (Hwy 22) or three (C-2)?

### 6.5 Difficulty factors
27. Does D = 2.50 stand for the station (`09` L88, `16` L249), including after any expansion?
28. Which ice thickness is canon: ~2,850 m or ~2,700 m (C-23)?
29. Does the station's building on moving ice (~10 m/yr) and under ~75 mm/yr of lasting snow enter the difficulty figure?
30. What is the station's extent: 1 km² (`Extent_and_Density_Per_City.md` L629), the Tower's 1–2 km² surface complex, or a new figure; and how much of it is underground?
31. Are the underground network and the deeper chambers (`DLC_01_South_Pole_Side_Content_Suggestions.md` L23) Second Interwar canon or post-war DLC design only?

### 6.6 Food role
32. Is the station a forced importer with the food term at 10% (`16` L114, L3458), and does that hold for any expanded population?
33. Does the station grow any food of its own (no file states one; a greenhouse bay appears only in a withheld megasheet, cited by `Storyline/DLC_01_Echoes_of_Amundsen.md` L132)?
34. By which route and from which cities does the station's food arrive (Hwy 22 only; no airport; no port)?

### 6.7 Power
35. What powers the station before ~2688, before the Tower existed (the power file is empty)?
36. What powers the station after ~2688: the Tower's own generation, the national grid it regulated, or both?
37. Is `Amundsen_Power_Supply.md` to be written before the ULM pass, and what is its scope: the station, the Tower, or the national grid (C-24)?

### 6.8 Other open items that touch the pass
38. Which Tower completion and build-length figures govern (~2688 vs ~2630–2640; 12–17 years vs 65–75 years) (C-25)?
39. Which orbital population figure governs (10,104,964 vs ~11.36M vs ~9.2M) (C-27)?
40. What is the station's element (paused vs Electromagnetism vs Magnetism), and does its symbol entry count as existing (C-15)?
41. Should the outer README, concept-art folder and neo-race folder be corrected or left (C-32 to C-34)?
42. Should the three verifier FAILs (D2, D3, D6) be fixed before the pass, given the Gaps file calls them "by design" for a city awaiting expansion?
43. Is the "Location registries" Phase 0 row resolved for this city (Pre-Trip §D row, unresolved)?
44. Should the Founding Register be added to the Phase 2 read list for this city (Pre-Trip §I row, raised 2026-10-21)?

---

## FINAL · One-page index

| Item | Where | Key result |
|---|---|---|
| **1 Files** | §1.A–§1.O | 295 files under `Worldspace/` + `Reference/` and 2 top-level files name the city. Core set: `SPEC`, `PASS/` (README, Pre-Trip, ledger, 19 datasheets), the culture/robot/enneagram/vision sheets, `CEN`, `Founding_Register.md` L75, DoI `04`/`09`/`13`/`15`/`16`/`17`, infrastructure files, `City_Relationship_Database.md`, `City_National_Connections.md`, `Upper_Earth_Immigration_Composition.md`, the scenario file and `DRL`. **`Amundsen_Power_Supply.md` is empty.** 33 megasheet and 6 Super-Ultra-Megasheet files listed, not opened |
| **2 Canon** | §2.1–§2.14 | 90°S, ~2,835 m; Census I 1,121 H / 5,736 R / 6,857; Census II 913 / 3,978 / 4,891, set by a 0.2% / 1% reduction of a computed 1,808,000; inter-subnet relay, no subnet, no founding nation; Tower base; DoI relay 60 / Tower 30 / life support 10, `16` §35 "DETERMINED" (mandated 61.4%, free 6.8%); hostel 20% working share (`DR-65`); space workforce Census II only (`DR-69`); no airport, landlocked, Hwy 22 |
| **3 Contradictions** | §3, C-1 to C-38 | Largest: subnet label (C-1); one vs three highways (C-2); Tower staff in the pre-Tower Census I (C-9); relay start date (C-10); namesake-based composition note vs `DR-32` (C-12); symbol entry exists vs "no entry" (C-15); DoI "determined" vs "still to be done" (C-17); Census I hostel beds vs "no space workforce in Census I" (C-19); scenario "census not edited" vs `DR-69` "applied" (C-20); "skeleton crew / facility" vs "full town" and "much larger population" (C-22) |
| **4 Expansion** | §4 | 11 dated statements, 2026-09-07 to 2026-10-29. "Full town during the Second Interwar Period" (10-18); "official census governs" (10-18, `DR-58`); "to be expanded first" (10-21); "much larger population … far more complex, intricate" (10-27 draft direction). **No ruling sets a new figure or defines "expansion"** |
| **5 Tools** | §5 | Audit: 40 tests, 1 GAP (the known picks false positive), 3 notes. Verifier: 20 checks, **3 FAIL** (D2 must-open coverage, D3 coverage lines, D6 DoI reliability gate), 1 NOTE |
| **6 Questions** | §6.1–§6.8 | 44 questions: what expansion means (5), population (9), composition (5), role (7), difficulty (5), food (3), power (3), other (7) |

**Left open by this unit:** nothing in the brief. Not done, by the brief's limits: the megasheets, the Super-Ultra-Megasheet, `Background-Lore/` (not canon) and `Archive/` were not read; the universe-repo archive file was not read.
