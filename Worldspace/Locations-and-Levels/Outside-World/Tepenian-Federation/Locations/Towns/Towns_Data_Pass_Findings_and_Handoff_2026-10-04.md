# Towns: Data Pass Findings and Handoff (written 2026-10-04, for the next session)

**Why this file exists.** The developer will close this session and open a new one **so the web-search budget is replenished** (the 500-search cap ran out during this session; set `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` in `~/.claude/settings.json` before starting; it took effect mid-session last time). **Everything found so far is below, plus what still needs real web research.** *Read this file first when resuming work on towns, the gateway research, or the Hobart/port questions.*

## ⛔ Governing rules for the towns work (all developer rulings, 2026-10-03; `DR-52`)

- **The idea (`DR-52`):** after the 38 cities, every real Antarctic station on a **stable** location that is **not already a declared city** becomes a lightly developed Tepenian **town**. Purposes: a fuller country; DLC places between cities; the *Southern Lights* show feels fuller; **a natural path from the coast to Ariun Nuur, Kunlun and Dome Fuji (Hwy 37)**, ending at Dome Fuji (which will get another name) even as side-content.
- **"Steady" means:** *"ice that's not moving at a speed to the point where the city itself needs to be moved. Ideally having bedrock at some distance below the ice."* Bare-rock sites qualify automatically.
- **Scope for the data pass:** *"Just collect every usable station location, and we'll figure out the rest as we go."* Nothing is excluded yet; everything is tagged.
- **Hours:** *"Establishing each town's personality, character, etc, that's something to do during the productive hours. Collecting data that's relevant to those towns can be done any time."* **Data any hour; town CHARACTER only 05:00 to 14:59.**
- **Census:** *"we'll figure that out later."* Census II's total is fixed and hands-off until the 38 cities finish the ULM (`DR-23`); where town populations come from is **deferred on purpose.**
- **The station-history law is NOT in tension** (developer, same day): what a station was dedicated to enters a town as **inherited research, equipment and records** (`DR-24`, `DR-25`, `DR-26`; precedents Belgrano, Neumayer, Kunlun, Ariun Nuur). Wording: *"took up the station's research, equipment and records"*, **never** "the research heritage continues". The operating nation is **never** a reason for a town's identity, culture or ties; real names may be kept as naming facts only (`DR-28` D2).
- **Nothing in this pass names a town or characterizes one.**

---

## 1. What exists (all under `Locations/Towns/Data/`)

| File | What it is |
|---|---|
| `Real_Station_Inventory_Raw.csv` | **524 rows**, one per real Antarctic station-like location (merged from 1,225 source records). 36 columns: id, names, lat/lon (with the source of each), elevation, type, status, years, capacity, `operator_context_only`, `purpose_as_stated`, `surface`, `stability_flag`, sources, notes |
| `Real_Station_Inventory_Crossmatched.csv` | The raw CSV **plus** `nearest_city`, `nearest_city_km`, `city_match_class` (script 09) and `nearest_highway`, `highway_km` (script 10) |
| `Real_Station_Inventory_Method_and_Log.md` | The collecting agent's full method and log: sources, counts, de-duplication rules, **all 51 manual merge decisions**, the 59 coordinate disagreements, name conflicts, sign and typo anomalies, 14 status disagreements, 38 opening-year disagreements, what was dropped, what is incomplete, the column dictionary, how to reproduce |
| `scripts/` | The pipeline: `00_fetch_raw.sh`, `01_`…`08_` (fetch, parse, merge, build, diagnostics), `inv_lib.py`, `merge_overrides.json`, `manual_notes.json`, plus **`09_crossmatch_cities.py`** and **`10_highway_proximity.py`** (written 2026-10-04 to cross-match against the 38 cities and the highway network). A leftover `scripts/__pycache__/` is safe to delete (the project's delete hook blocked it) |

**Reproducing:** run `00_fetch_raw.sh`, then the numbered scripts in order, then 09 and 10. Wikidata moves slightly day to day (the Filchner Station coordinate moved overnight).

**Sources that worked (all by `curl`, no web search):** COMNAP `Facilities_Nov2024.csv` (114 rows) and the 2017 COMNAP station-catalog PDF (76 stations); Wikidata SPARQL (352 items); the Wikipedia API (the station list, field camps, airports, Historic Sites lists, and a category-tree cross-check); the SCAR Composite Gazetteer through its `placenames.aq` API (the old AADC URL returns a 301 to an empty JavaScript page); the local NOAA GHCN-Daily list (`to-be-integrated/climate data CURL/ghcnd-stations [NOAA].txt`) as a cross-check only. **Not used:** WebSearch (budget gone), WebFetch, Wayback, the COMNAP Firebase app.

---

## 2. Headline numbers

**524 locations** (south of 60°S plus the South Shetlands and South Orkneys; **11 more** lie north of 60°S and are listed in the log only: Macquarie, the sub-Antarctic stations, Peggotty Bluff, Corbeta Uruguay in the South Sandwich Islands).

| Cut | Counts |
|---|---|
| **By type** | station 161 · hut-refuge 140 · field camp 86 · airfield 79 · automatic weather station 42 · other 16 |
| **By status** | summer-only 154 · closed 140 · unknown 135 · year-round 43 · abandoned 28 · historic 24 · planned 0 |
| **Stability flag** (sources' own statements only) | **unknown 356** · rock 81 · **needs a velocity test 62** (ice shelf, glacier, sea ice, or a source says it moved) · ice-sheet interior 25 |
| **Surface stated at all** | only **164 of 524** (only the 2017 COMNAP PDF states it systematically) |

### Cross-match against the 38 cities (script 09; thresholds are reading aids only: ≤25 km, 25 to 100 km, >100 km)

| Class | Rows | Meaning |
|---|---|---|
| **AT_CITY** (≤25 km of a declared city) | **191** | part of that city's site (35 are year-round stations); every city has one, **including Zhongshan** (see caveat below) |
| **NEAR_CITY** (25 to 100 km) | **132** | neighbors of a city, not the city |
| **CANDIDATE** (>100 km from every city) | **196** | the open land: 46 stations · 53 field camps · 37 huts/refuges · 31 automatic weather stations · 21 airfields · 8 other |
| NO_COORDS | 5 | no coordinate in any source |

**A first-filter reading (not a decision):** among the 328 NEAR_CITY and CANDIDATE rows, **205 are stations, field camps or huts not flagged as on moving ice** (80 huts · 69 stations · 56 field camps); **of those 69 stations, 8 are year-round, 16 summer-only, 30 closed, 7 abandoned, 7 unknown, 1 historic.** *Remember that "not flagged" mostly means unknown (see section 3).*

**By subnet** (nearest city's subnet, NEAR_CITY plus CANDIDATE): Palmer 99 · Janbogo 80 · Mirny 50 · Halley 38 · Byrd 24 · Mawson 22 · Amundsen-Scott 15.

**The eight YEAR-ROUND stations that are not at a city** *(prime early candidates; nearest city and distance)*: **Arturo Prat** (Pergamino, 41 km) · **GARS, the German receiving station** (Esperanza, 47 km) · **O'Higgins** (Esperanza, 47 km) · **Orcadas** (Signy, 47 km) · **Petrel** (Esperanza, 38 km) · **QinLing** (Zukelli, 30 km) · **San Martín** (Rothera, 76 km) · **Vernadsky** (Palmer City, 54 km). *(Operators are context only.)*

---

## 3. What the data shows (and does not)

1. **The Peninsula and the coast are crowded; the interior is nearly empty.** Palmer (99) and Janbogo (80) lead the candidate counts. **Real inland stations along the Dome Fuji path are very few**, so the real data will **not** fill the path to Dome Fuji by itself.
2. **The Hwy 37 corridor (Dome Fuji → Kunlun → Ariun Nuur → Concordia)** has, within 150 km of the traced line, only: **Little Dome C** (10 km, summer field camp, ice-sheet interior), **Criosfera 2** (18 km, summer, a "other"), the **EAGLE** automatic weather station (23 km), and **Mizuho** (94 km, closed, ice-sheet interior). Farther out (200 to 450 km): **Plateau Station** (215 km, closed, ice sheet), **Sovetskaya** (251 km, abandoned), **Komsomolskaya** (450 km, abandoned). **So the Dome Fuji path needs either closed historical stations, automatic-station sites, or invented towns.** This is a **developer decision**, not a research one.
3. **Other highways, 150 km or less, non-weather locations (candidate and near-city):** Hwy 1 has **82** (the Peninsula); Hwy 7 has 14; Hwy 22 has 11 (including the closed **Pole of Inaccessibility** station at 17 km); Hwy 110 has 9; Hwy 4 has 8; Hwy 7-ext has 6; Hwy 183 has 5; Hwy 37 has 3; Hwy 2 has 3; Hwys 59 and 175 have none. *(The highway lines are traced from the developer's sketch and are good to about ±20 km.)*
4. **Stability is the big unknown.** **356 of 524 are `unknown`** and only **62** are flagged for a velocity test; the developer's criterion (ice not moving fast enough to force relocation, bedrock below) **cannot be applied to most rows yet.** The collecting agent deliberately did **not** compute ice velocity or bedrock depth.
5. **Data cautions found:**
   - **WAIS Divide shows an elevation of 5,895 m**, which looks wrong (by my recollection the ice-divide site is under 2,000 m; **verify**); treat as a probable source error and check it in the next session.
   - **Zhongshan Skiway:** COMNAP gives latitude **+69.62 (north)**; the pipeline **flipped it to south** and flagged it (the only coordinate it altered). Every other source value is kept in `coords_by_source`.
   - **59 rows have a source coordinate more than 2 km from the one used** (several look like sign or digit typos, e.g., Criosfera 2, Mid Point, Strom Camp, and 2017-PDF longitudes for Elichiribehety and Gabriel de Castilla); all are listed in the log.
   - **The Tri-Cities** (Zhongshan, Sinheung, Shirayuki) **share almost one coordinate**, so the "nearest city" for rows in the Larsemann Hills is whichever of the three the arithmetic picks. The class (AT_CITY) is right; the city name is not meaningful there.
   - **Weather stations are incomplete:** **38 of the 102 NOAA Antarctic stations have no row within 5 km**; the log lists them.
   - **Capacity** exists only for stations; huts, camps and airfields have none. **Hut and refuge networks** beyond Wikipedia's lists are probably under-counted. **Status** is unknown for 135 rows (mostly airfields and Wikidata-only rows).

---

## 4. WHAT NEEDS WEB RESEARCH IN THE NEW SESSION (with the replenished budget)

**Set the cap high first** (`CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`, e.g. `"1000"`); the three gateway agents and the two Hobart agents together burned all 500 in this session.

### A. Towns: the stability test (the main job)
1. **Ice velocity at each CANDIDATE and NEAR_CITY site** (328 rows; start with the 205-row first filter and the 62 flagged rows). Sources to try: NASA **MEaSUREs Antarctic Ice Velocity** (needs an Earthdata login), **ITS_LIVE** (public S3), Mouginot/Rignot velocity mosaics, the BAS/AAD station pages. Record velocity in m/yr; classify against the developer's rule (relocation-forcing speed; Halley's 400 to 700 m/yr is the counter-example).
2. **Ice thickness and bedrock depth** at each site: **BedMachine Antarctica** (NSIDC, login), Bedmap2/3 (BAS, public). Record ice thickness and bed elevation; mark rock-at-surface sites.
3. **Fill the unknowns:** surface (360 rows), status (135 rows), years, capacity; verify the 59 coordinate disagreements and the 14 status disagreements against primary sources (COMNAP's Antarctic Facilities Information online data, national program pages).
4. **The 38 missing NOAA weather stations** and the **under-counted refuge/hut networks** (Wikipedia-only so far); decide which of these are even "stations".
5. **The Hwy 37 / Dome Fuji path:** every real or historical facility (including closed Soviet, US and Japanese inland stations and traverse depots) within, say, 400 km of the Dome Fuji–Kunlun–Ariun Nuur–Concordia line, with its stability data.

### B. Gateway and port research still thin (from the Hobart/Ushuaia work; logs in `Cities/Research_Logs/`)
6. **Hobart as an island port:** storm and sea-level exposure of the Derwent estuary; naval, Border Force and fisheries-patrol presence; ship repair and drydock capability in Tasmania; **Bell Bay hydrogen and ammonia**; which port ships tin and zinc concentrate; Hobart cargo by commodity; whether sealed Antarctic-bound cargo is exempt from Tasmanian import conditions; the Port Master Plan 2027 content (`Hobart_Island_Port_Research_A_…` and `_B_…`, `Hobart_Island_Port_Applications_Combined_2026-10-03.md`).
7. **The three mainland Australian freighter terminals** (Bunbury for Perth; Outer Harbor for Adelaide; Jan Juc, Torquay or Flinders for Melbourne, outside Port Phillip Bay): **real feasibility of each site** (water depth, shelter, Southern Ocean swell on the Surf Coast, rail and road links, land use) and whether **Sydney, Brisbane or other east-coast sites** need a terminal. *(Established 2026-09-26 in the CurrentNovelDocs repo; recorded in `Ports.md` §3c and memory `project_australian_freighter_terminals`.)*
8. **Where Australia's iron ore comes from** relative to the three terminals (the Pilbara is far northwest of all three); Savage River (Tasmania) pellets via Port Latta as a nearer source.
9. **The remaining gaps in the gateway re-run logs** (`…A2_`, `…B2_`, `…C2_`): Commonwealth Bay access after 2018; site-specific sea-ice climatology for the Shackleton/Bunger coast; Indonesian official statements on Treaty accession; Sumatran populations from BPS; published sea-distance-table figures from Hobart to Dumont d'Urville and Commonwealth Bay; Japan's gateway ports (Fremantle for the *Shirase*, Hobart for the *Umitaka Maru*).

### C. Not research: decisions waiting for the developer
10. **Basis wording for the nine gateway rows** (options A to E in `Founding_Basis_Wording_Options_2026-10-03.md`; none chosen).
11. **`FQ-20`:** Australia's share of the founders (five cities now: Mirny as an exile group, Casey, Davis, Denison, Zukelli). Optional.
12. **`DR-51` deferred on purpose:** three international airports, not one; early on only Marambio Airport; sort it out once the country is better determined.
13. **`DR-50` open items:** where Hobart arrivals are processed in later eras; which ports receive people; robots; whether the role continues in the Second Interwar Period.
14. **`FQ-22`:** Mirny's live ULM pass and `DR-46` (Idelsk-Uralia as the founding nation) need an in-window read of the pass's founders usage.
15. **Held rename files:** run `Universal_Location_Methodology/Tools/rename_sweep_held_files.py` (both batches) **after the Mirny pass finishes** (`MASTER_Process_Tracker.md`, `📍 RESUME HERE`).
16. **Town questions still open:** scale and names; ports, airstrips and highway stops; which cities each town hangs off; whether closed historical stations qualify; whether to keep real names; and where the town populations come from (the census).

---

## 5. Where everything from this session is (so nothing has to be rediscovered)

- **Rulings log:** `Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md`, `DR-33` to `DR-52` (founders `DR-33`/`34`/`35`/`44`/`45`/`46`; renames `DR-36` to `DR-43`; primary ports `DR-48`; freighter terminals `DR-49`; people ports of transfer `DR-50`; three airports `DR-51`; **towns `DR-52`**).
- **Follow-up questions:** `Cities/City_Development_Passes/follow-up_questions.md` (`FQ-13` to `FQ-25`).
- **Founding Register:** `Cities/Founding_Register.md` (all 38 rows ✅; Halley's "central role" and Temirötkel's first establisher stay partial).
- **Renames:** `Cities/City_Renames_Alias_Table_2026-10-03.md` (batches 1 and 2); the six held files wait for the Mirny pass.
- **Maps:** `Reference/Images/Maps/working-stash/` (five maps, current; names updated; `CHANGES.md`).
- **Ports:** `Locations/Infrastructure/Ports.md` §3b (primary ports), §3c (where each connects; the three mainland terminals; Fremantle), §3d (people ports of transfer; the three-airports deferral). Companion files in `Cities/`: `Gateway_Ports_Peninsula_and_Scotia_Sea_2026-10-03.md`, `Gateway_Ports_Adelie_and_Queen_Mary_Land_2026-10-03.md`, `Founding_Basis_Wording_Options_2026-10-03.md`, `Hobart_Island_Port_Applications_Combined_2026-10-03.md`.
- **Research logs:** `Cities/Research_Logs/` (gateway first pass `A_`,`B_`,`C_`; re-run `A2_`,`B2_`,`C2_`; Hobart `A_`,`B_`).
- **Memory:** `project_tepenian_towns_idea`, `project_australian_freighter_terminals`, `project_city_rename_batch2`, `project_founding_rulings_2026_09_30`, `reference_deferred_and_flagged` (the three-airports entry).
- **Nothing is committed**; `graphify update` has not been run (the graph still indexes old names).

## 6. How to resume (suggested first moves)

1. Raise the search cap, start the session, and read **this file**.
2. **Towns first (data, any hour):** run the velocity and bedrock lookups for the **205-row first filter** (section 4A), starting with the **62 flagged rows** and the **8 year-round non-city stations**; write results as new columns in `Real_Station_Inventory_Crossmatched.csv` (via a new numbered script) and log every source and dead end.
3. **Then the thin gateway items** (4B) as budget allows.
4. **Do not design any town's character outside 05:00 to 14:59.**

---

## 7. UPDATE (2026-10-04, later the same night): scope narrowed, Batch 1 started

- **Developer scope ruling (2026-10-04):** huts/refuges and field camps are **out** (not likely to survive 500+ years to be found after the Falkland Treaty); automatic weather stations are **at most comms beacons** (skeleton crews under 100); airfields are usable only as an undetermined subset; **in scope: the 87 NEAR_CITY/CANDIDATE `station` rows plus the 11 `other` rows.** This supersedes the 205-row first filter as the work list.
- **Priority Batch 1 (32 stations):** 25 active (8 year-round, 17 summer-only) + 7 recently closed and plausibly revivable (4 "temporarily closed" per COMNAP 2024: Brown, Carvajal, Kohnen, Melchior; 3 closed since 2000: Sarie Marais, Soyuz, Arturo Parodi). Reference file: `Towns_Priority_Batch_1_Reference_2026-10-04.md` (one block per station, "From the inventory" + "To fill in"). Left out on purpose: Drescher Ice Camp and Filchner Station (ice shelves).
- **Maps 06 to 11** (stations, Peninsula and South Shetlands close-ups, the 36 weather stations, all 68 sites, Casey/Law Dome close-up): `Reference/Images/Maps/working-stash/out/`; data `data/town_candidates.csv`; documented in that folder's README, CHANGES and PROGRESS TRACKER.
- **A1 (year-round) research DONE for all 8 stations**: logs in `Research_Logs/Batch1_A1_*`. Headline: Prat, GARS, O'Higgins, Orcadas, San Martín, Vernadsky and **QinLing** (best documented: full Final CEE; year-round since the 2025 winter, 18 wintering in 2026) **qualify** (rock); **Petrel unclear** (moraine on ice-rich permafrost, bedrock 31 to 94 m down, glacier retreating, no forced relocation). **#2, #3 and #22 are one site** (Rada Covadonga is an anchorage name). Inventory corrections: "Sandefjord Bay Station" is an unoccupied 1945 hut 73 km from Orcadas; Rada Covadonga is "Seasonal", not year-round; no 2008 fire at San Martín. **WAIS Divide Camp's 5,895 m elevation is 5,895 FEET entered as meters (about 1,797 m; drill site 1,766 m; ice 3,465 m thick; core site moves about 3 m/yr)**: the inventory CSV was NOT edited; correct it in a new script if wanted.
- **Still open from A1:** glacier velocities at every site (none found for Petrel's Rosamaría, Prat's Fuerza Aérea, Orcadas' Laurie Island glaciers); ATS Art. VII inspection reports (database 404/login); Petrel's Final CEE (ATCM46 IP133); Orcadas ground ice under the buildings; Woozle Hill collapse date at Vernadsky.
- **Next:** A2 summer-only (17), B1 temp-closed (4), B2 closed since 2000 (3); then the 11 "other" rows and the airfield subset. Several A2 rows share sites with A1 (Rada Covadonga/GARS/O'Higgins; Decepcion/Gabriel de Castilla; Prat/Maldonado/Risopatrón), so research them together where possible.
- Nothing is committed. `graphify update` has not been run.

## 8. UPDATE: Batch 1 research round 2 (A2 summer-only, B1, B2), filled 2026-10-04

**All 32 reference blocks are now filled** (Halley VI, Jinnah and Kohnen last: Halley VI fails, Jinnah is unverified and likely defunct, Kohnen passes the speed test but has no surface rock). A verdict summary table sits near the top of the reference file. Logs: `Research_Logs/Batch1_A2_*`, `Batch1_A2_B1_*`, `Batch1_A2_B2_*`. Seven of these logs are the agents' reports copied verbatim from their transcripts; the A1 logs were re-typed and condensed.

**Tier changes the evidence supports (all developer decisions, nothing changed yet):**
- **#22 Rada Covadonga:** an anchorage name, fold into O'Higgins (#3); #2, #3, #22 are one site.
- **#30 Arturo Parodi: drop.** The inventory point is the dismantled (2013) Patriot Hills base; Union Glacier (the live Chilean station, a different place) is on ice moving about 20 m/yr. Both fail.
- **#26 Brown and #29 Melchior are not closed** (COMNAP's "Temporarily Closed" is an off-season flag; both open every Argentine summer) and **#27 Carvajal is the only real closure** (ice runway failed; reopening announced for Jan 2026, unconfirmed). **#31 Sarie Marais** (decommissioned 2001/02 and recycled) **and #32 Soyuz** (closed 1989, derelict by 2010) are not "recently closed, revivable".
- **#9 Decepcion and #11 Gabriel de Castilla** are one site and sit on volcanic ash in an active caldera (leaning fail for a settlement); Gabriel de Castilla also has accelerating erosion (up to 2.5 m/yr).
- **#25 "Shirreff Base"** is really the Chilean Dr. Guillermo Mann camp at Cape Shirreff (inside ASPA 149, with the US Holt Watters camp 50 m away); relabel it. **#19 "Mountain Evening"** is Belarus's Mount Vechernyaya station.

**Inventory corrections to carry into a new script (the CSV was NOT edited):** "Belgrano II Skiway" row is a copy-paste coordinate error (the real one is at 77.87°S 34.63°W); "Sandefjord Bay Station" is an unoccupied 1945 hut; Gabriel de Castilla is not at Pendulum Cove; Druzhnaya IV is on Landing Bluff (Sandefjord Bay), not the Prince Charles Mountains; Soyuz closed 1989 not 2007; WAIS Divide 5,895 is feet; Parodi elevation 983 m is unsourced (855 to 880 m).

**METHOD FINDING: ice velocity can be computed directly.** The last agent pulled ITS_LIVE v2 datacubes (S3: `its-live-data/datacubes/v2-updated-october2024`) and used the per-pixel temporal median of vx and vy separately, then the magnitude (a median of scalar speed is biased upward by noise: about 19 m/yr at known rock vs 0 to 2 with the vector-median). Caveat: ITS_LIVE cannot separate rock from ice, so 0 to 3 m/yr means "stationary or rock". REMA v2.0 32 m mosaic (PGC S3) gives surface elevation. Bedmap3 returned 503 and BedMachine needs a login. **Next: run this at every Batch 1 site** (a new numbered script in `Towns/Data/scripts/`), which closes the "glacier velocity not found" gap for most of the 32.

**Still open overall:** glacier velocities at most sites (see above); ATS Art. VII inspection reports and the ATS APA database (JavaScript app; its backend API `https://www.ats.aq/devphbackend/api/apa/search` worked for one agent); Petrel's Final CEE (ATCM46 IP133); the 2018 QinLing draft CEE; Matienzo operations 2019 to 2024; whether Carvajal reopened; whether Mount Vechernyaya has begun wintering.

**Developer ruling (2026-10-04, after the Halley VI research):** Halley VI is already a city (the developer first typed "Halley IV" and corrected it to "Halley VI"). **#13 Halley VI is therefore redundant as a town candidate and is dropped from Batch 1**; the research stays in the reference file and log. It also fits the project: the city Halley is a spur off Hwy 7 because the shelf moves (about 1,400 m/yr per the research).

**Developer correction (2026-10-04):** cities and towns can be built on ice; rock is never required and rock-outcrop area is NOT a size test (my earlier suggestion to measure it is withdrawn). The `DR-52` test is ice SPEED only ("ideally bedrock below"), **and no speed threshold has been set** (Halley's 450 to 1,400 m/yr and Union Glacier's about 20 m/yr are unruled). Every "FAILS" in the verdict table means "moves fast", not "disqualified"; Kohnen (0.76 m/yr, grounded plateau, no rock) is a strong candidate on this reading, like Kunlun and Dome Fuji. Memory: `feedback_cities_can_be_built_on_ice`.

**Developer idea (2026-10-04): sites #18/#19 (Molodezhnaya + Mountain Evening / Mt Vechernyaya) could be a city unto itself** (Enderby Land, 296 to 308 km from Temirötkel, Hwy 4 about 62 to 67 km; the largest ice-free oasis of the sites of interest: 8.3 by 2.7 km, 40+ lakes). **Open question: who settles/establishes it.** Constraints already ruled: founders come only from `Cities/Founding_Register.md` and stand on geography and access (`DR-19`); a station's operator is never a reason for identity or founders; the city corpus is fixed at 38 and Census II is hands-off until the ULM finishes (`DR-23`), so adding a city is a developer decision about the corpus. Sites of interest are #24 Russkaya, #16 Leningradskaya and #18/#19 (map `12_Towns_Sites_of_Interest`).

## 9. Comms-posts idea and open research (2026-10-04)
Developer idea (not a ruling): the 36 weather-station comms posts cluster in the Asian-meridian stretch of the Eastern Hemisphere, so the people who renovate them would be mostly Australians, then Sinians and Kazakhs, giving the national long-distance comms network an Australian protocol and comms culture; **and in long-distance communications the pattern that dominates one area becomes the standard everywhere.** **Research to do (noted 2026-10-04): real Australian radio practice.** Full note, scope and guardrails: `Open_Research_Topics.md` (same folder). Not added to the Weekly To-Do (that file is the 37-locations queue; the towns work is parallel and has this handoff).

## 10. ⚠ WHAT THE 1,000-SEARCH SESSION CAP CUT OFF (2026-10-04; for the next session with a fresh quota)
> **STATUS UPDATE (2026-10-04, later): items 1 to 5 and most of the "thin spots" below were RE-RUN the same day by six agents; results are in section 12 and in `Research_Logs/`. Wording below is kept as the record of what was asked; claims later found wrong are marked ⚠ CORRECTED.**

**Context:** the `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` cap of 1000 was exhausted partway through the comms-research round. The cap is shared by every agent in a session, so the last agents to run were the most starved. All eight reports are saved in `Research_Logs/` (summaries in `Open_Research_Topics.md`); each log has a dead-ends list. **Gaps below are the topics that were not searched, or died at the query, because of the cap.** LAW 0-R applies: re-run them FULLY, from more than one angle.

**First, re-run (these were cut off outright):**
1. **Southern Ocean weather and observing cooperation, joint Australia-Chile research programs, SOOS/Argo/WMO** (`Why_Australia_Links_South_America_*`: never searched). Also more on Australian merinos in Patagonia (one unverified claim that the first 1926 Merinos died of cold; **⚠ CORRECTED: dead, Merinos were in Patagonia from the 1860s; Australian influence begins 1950s-60s**).
2. **Antarctic sea-ice forecast producers** (who makes the operational ice charts for the southern ring), **WMO regional-association mapping for Antarctica**, **Montevideo's logistics role** (`Southern_Hemisphere_Ring_*`).
3. **Drake transit-time variability, AIS studies and delay statistics for ships; dynamic-positioning fuel use and small-vessel hotel load** (`Drake_Crossings_*` last query refused; `Weddell_Floating_Relay_*` queries 58 and 59 never ran).
4. **The Weddell floating relay's unanswered items:** HF-range (3 to 30 MHz) conductivity of sea ice (the antenna numbers assume values); surface-mooring survival numbers for the Southern Ocean (SOFS, OOI 55 S); Polarstern fuel capacity in m3; fog frequency; relative flow beneath a drifting floe; any real floating HF relay or polar-sea current-turbine precedent.
5. **Perth to Cape Town HF:** any documented two-way contact (the agent found none) and the first Australia-South Africa and Australia-South America amateur or commercial HF contacts; SEACOM and other Australia-Africa cable facts; whether Google's Umoja cable is in service (timeline conflicts: early 2026 vs 2027; **⚠ CORRECTED: not in service, TeleGeography lists it as planned 2028; "early 2026" has no source**).

**Then, thin spots worth a second pass:**
- **Macquarie Island:** the station's present HF transmitter powers, antenna types, frequency plan beyond 3023 kHz, receive-site noise level, and any failure rate for a lightly staffed Macquarie antenna (`Radio_Physics_Followup5_Macquarie_*`). **Also: whether Macquarie exists in canon is a developer ruling, not research.**
- **Drake:** Antarctic Pilot (NP9) sailing distances (paywalled), Marambio's current runway length (1,208 m vs a 1,600 m second runway; **⚠ RESOLVED: both exist, 1,208 m main and a 1,600 m second test-flown July 2015; which is operational now stays unresolved**), Punta Arenas/Ushuaia port-closure rules, the Antarctica21 flight-delay figures (unverified), the Charcot expedition crossing times.
- **Sea state:** in-situ wave buoys in the Drake (none found), icebergs in the Drake (no quantitative data), seasickness prevalence and roll-angle statistics, the Cape Horn "10,000 sailors" origin. The sea-conditions agent stopped with background work still running, so that report may be interim.
- **Australia-South Africa:** a formal AAD-SANAP agreement (none found at program level; **⚠ but a direct Australia-South Africa rescue arrangement was signed 23 Sep 1998**), a Western Australia gold rush to Witwatersrand link (**not confirmed**), modern wine/wool/sheep flows, Southern Hemisphere storm-track propagation Cape to Australia.
- **Antarctic SAR boundaries by longitude** for Chile, Argentina, South Africa and New Zealand (agent had only snippets).

**Not research (still waiting on the developer):** keep Macquarie as a possible node; add Amundsen Station and Hobart/Perth/DDU as nodes; the tier changes (#22 into #3, drop #30, move #31/#32, relabel #25, map 06 legend and #13/#30 dropped); the DR-52 ice-speed threshold; the Temirötkel Junction Hwy 4 start (first about 57 km not on land); whether to run the ITS_LIVE velocity script on all 32 sites. Nothing from this session is committed and `graphify update` has not been run.

## 11. TO DO (developer request, 2026-10-04): research Australian / South American trade (and the Australia-South Africa trade side) properly
> **STATUS: DONE 2026-10-04 (six agents; synthesis `Research_Logs/Why_Australia_Links_SouthAmerica_SouthAfrica_Reconciliation_2026-10-04.md`; results in section 12). The "Grok's claims" below were checked: the $20bn and $35bn figures are CONFIRMED as regional totals, "concentrated in mining" is NOT supported, "gateway" is institutional only. Text below is the original request; ⚠ CORRECTED marks the lines found wrong.**

**Why:** the developer asked Grok the same question we put to the three agents and passed on its answer. Grok's answer leans on trade and investment as a reason for Australia to want links to South America, while our agents found trade the WEAKEST structural reason (Australia-Chile about A$1.4bn in 2016; Australia-South Africa about US$2.3bn in 2024; mining services and cross-ownership real but small; lithium and copper make Australia and Chile competitors as much as partners). **The two disagree on scale, so this needs a real research pass, not a pick of one answer.** Grok's text was unsourced, so everything below is a LEAD to verify, not a fact.

**Grok's claims to check (all unverified):**
- Two-way goods and services trade with Latin America "on the order of $20 billion a year", grown substantially in recent years. *(Our agents: Chile about A$1.4bn, Argentina about A$1.1bn, Brazil about US$1.7bn per country, which could sum to a few billion for the big three; whether $20bn includes Mexico, Colombia and services, and which year, is unknown.)*
- More than 300 Australian companies operating in Latin America, investment "often cited above $35 billion", concentrated in mining (BHP, Rio Tinto and mining-services firms in Chile, Peru, Brazil, Argentina).
- FTAs with Chile (2009) and Peru (2020); CPTPP membership shared with Chile, Peru and Mexico. *(Already confirmed by the South America agent.)*
- Chilean copper and Latin American lithium sit in the same critical-minerals supply chains Australia cares about. *(Our agents found this is competition plus cross-ownership, e.g. SQM holding 50% of Wesfarmers' Mt Holland.)*
- South Africa a smaller market but a resources peer and a gateway to southern Africa.
- Latency today: Johannesburg-Sydney about 400 ms, South America about 300 ms or more; Umoja expected about 2027 at roughly 110 to 150 ms to eastern South Africa; Humboldt service about 2028, around 14,800 km, with a separate branch toward Panama. *(The Humboldt and Umoja basics agree with our reports; the latency figures are unsourced, and the Umoja timeline conflicts: early 2026 vs 2027.)* **⚠ CORRECTED 2026-10-04: latency figures CONFIRMED by RIPE Atlas measurement (Sydney-Johannesburg 430-474 ms; Sydney-Santiago 265-312 ms); Umoja NOT in service, planned 2028, about 100 ms Perth-Johannesburg (agent estimate); TeleGeography lists NO cable named "Humboldt", so check Google's own announcement before relying on the name.**
- The value of the new cables is REDUNDANCY (a southern Indian Ocean path and a trans-Pacific path to Chile that avoid Singapore/Indonesia/North Pacific chokepoints) as much as speed. *(Matches our agents' "chokepoint diversity" reason.)*
- Antarctic Treaty cooperation, Southern Ocean carbon observations poorly measured in winter, thin Southern Ocean search-and-rescue, and proposed cables from Chile (and possibly New Zealand or Australia) toward Antarctic stations. *(Matches our agents.)*

**What to research (full, from several angles, LAW 0-R; fictional-setting use only, GPS/geography logic, no national-heritage claims about who settles anything):**
1. **Real Australia-South America trade by country and by commodity**, with the year and the definition (goods vs services, two-way vs exports): Chile, Argentina, Brazil, Peru, Uruguay, Colombia, Mexico. Reconcile the "$20bn" with the per-country figures found so far; note which numbers are Australian Government (DFAT/ABS) and which are secondary.
2. **Australian investment and companies in Latin America**: the real count and stock, by sector; mining-services (METS) exports; the BHP Escondida supplier network (about 80 Australian firms) and about 60 METS firms exporting to Chile. **⚠ CORRECTED: the 80 is a 2014 export-finance loan tied to one expansion and the 60 is a 2020 trade-press line; the pages originally cited contain neither. Regional stock is A$35.5bn, about 53% portfolio and 22% reported FDI.**
3. **What flows and what routes it takes**: lithium, copper, iron, gold, wheat, wool, wine, counter-seasonal fruit; Pacific shipping routes (Valparaiso-Sydney), ports, transit days; what a settled Antarctica would add (the Casey-Pole-Peninsula corridor, a Ross Sea hub).
4. **Durability test** (the project's method, `Fact vs. Driver`): which of these are structural and would plausibly persist for centuries (geography, the Pacific route, southern-hemisphere seasons, mining know-how) and which are contingent commodity or political cycles. Rank them as the earlier agents did.
5. **Do the same for Australia-South Africa trade**: coal, gold, platinum, alumina, wheat, mining capital (ASX firms the largest investors in South African mining; **⚠ CORRECTED: not supported; South African investment in Australia A$10.1bn vs Australian A$5.5bn, 2024**), Africa Down Under (Perth) and the Mining Indaba (Cape Town); how much it is goods vs capital vs services.
6. **Then the question that matters for this project:** does trade give Australia a reason to want a communications link (latency, redundancy, mining-operations traffic, corporate and financial traffic), and does it change the earlier ranking in `Open_Research_Topics.md` and the log `Southern_Hemisphere_Ring_Australia_SouthAmerica_SouthAfrica_2026-10-04.md`? State the answer as evidence, not as a preference for either source.

**Already in hand to build on (do not repeat):** `Research_Logs/Why_Australia_Links_South_America_2026-10-04.md` section 2 (trade and resources), `Research_Logs/Why_Australia_Links_South_Africa_2026-10-04.md` section 3, and `Research_Logs/Southern_Hemisphere_Ring_*` section 4. The new pass should go deeper than those, with primary sources (DFAT country briefs and fact sheets, ABS trade data, Austrade, USGS, company filings), several of which timed out or were blocked last time.

## 12. UPDATE (2026-10-04, same evening): the Australia / South America / South Africa question re-run and reconciled
**Done:** six agents re-ran sections 10 and 11. Logs in `Research_Logs/`: `Trade_A_…`, `Trade_B_…`, `Trade_C_…`, `Comms_Demand_Latency_Redundancy_Cables_…`, `Southern_Ocean_Cooperation_Rerun_…`, `HF_Contacts_and_Drake_Gaps_Rerun_…`. **Synthesis: `Research_Logs/Why_Australia_Links_SouthAmerica_SouthAfrica_Reconciliation_2026-10-04.md`** (claim-by-claim table, revised ranking, corrections, open items). **Summary is in `Open_Research_Topics.md` §5, "SECOND PASS".** Nothing is committed; `graphify update` not run.
- **Headline:** Australia has real reasons to link with both, but **not mainly goods trade**, and the evidence found is about economic DEMAND, not physical CAPABILITY. South America: A$19.4bn regional trade (about 1.7% of Australian trade; South America alone A$10-11bn), A$35.5bn investment (mostly portfolio, not mining), Pacific geometry, institutions, cable redundancy, **0 business-hours overlap**. South Africa: 1998 rescue arrangement and shared rescue edge, upstream weather (about 3 days Cape to Perth), the SKA data flow (the only quantified bilateral flow), flat A$5bn trade, capital flowing mostly TOWARD Australia. **No source shows trade, mining or finance creating a need for a dedicated link.**
- **Corrections carried over (2026-10-04):** inline in `Open_Research_Topics.md` §5 and in sections 10 and 11 above; one-line banners at the top of the first-pass logs (`Why_Australia_Links_South_America_`, `Why_Australia_Links_South_Africa_`, `Southern_Hemisphere_Ring_`). The first-pass log BODIES were not edited (verbatim agent reports).
- **Still open (research):** check Google's own announcement for the "Humboldt" cable name (TeleGeography has none); why Chile's Australian-investment stock jumped A$1.8bn to A$7.3bn in 2025; 2022-23 Australia-South Africa totals; a company list behind "300 companies"; first dated Australia-South Africa/South America two-way radio contact (none found); Macquarie transmitter powers and HF plan; NP9 sailing distances (paywalled); exact Australian and South African rescue-region coordinates; the single-sourced 2026 items (Perth cable faults 8 Aug and 4 Sep, Alcoa-South32 deal Jul 2026, Jun 2026 minister's speech text).
- **Still open (developer):** which reasons the fiction uses for each partner (best-evidenced sets are in the reconciliation §6); Macquarie's canon status; plus everything already in section 10's "Not research" list.
- **Tool note for the next session:** Noonsite and `www.directemar.cl` block WebFetch but open with `curl` and a browser User-Agent; DFAT's live site and some ABS pages time out from this environment (agents used Wayback copies and the ABS API).
