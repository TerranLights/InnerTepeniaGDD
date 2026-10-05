# Towns: Priority Batch 1 Reference (32 stations)

**Created 2026-10-04.** The first research batch for the towns work (`DR-52`): **the 25 currently active stations plus the 7 recently closed stations that could plausibly be revived** among the 87 `station` rows that sit outside the 38 cities. Scope follows the developer's 2026-10-04 ruling: huts/refuges and field camps are out; automatic weather stations are at most comms beacons; airfields are a separate, later subset.

**How to use this file.** The block **"From the inventory"** under each station is copied from `Data/Real_Station_Inventory_Crossmatched.csv` and must not be hand-edited (fix the CSV or its scripts instead). The block **"To fill in"** is empty on purpose: write verified findings there, with a source and date on every line, and log dead ends too. **Nothing here names or characterizes a town** (town character is 05:00 to 14:59 only). The operating nation is context only and never a reason for a town's identity (`DR-28` D2).

**Stability test (`DR-52`):** *"ice that's not moving at a speed to the point where the city itself needs to be moved. Ideally having bedrock at some distance below the ice."* Bare-rock sites qualify automatically.

## Batch overview

| Tier | Meaning | Rows |
|---|---|---|
| A1 | Active, year-round | 8 |
| A2 | Active, summer-only | 17 |
| B1 | Temporarily closed per COMNAP 2024 | 4 |
| B2 | Closed since 2000, plausibly revivable | 3 |
| | **Total** | **32** |

**Left out of the batch on purpose:** Drescher Ice Camp (closed 2016, ice shelf) and Filchner Station (abandoned 1999, ice shelf); both fail the stability test on the data we have. Revisit only if the velocity lookup says otherwise. **Not yet in any batch:** the 8 stations of unknown status, the 38 closed/abandoned stations older than 2000, and the 1 historic row.

## Verdict summary (all 32 blocks filled 2026-10-04)

**⚠ READ "FAILS" AS "MOVES FAST", NOT "DISQUALIFIED" (developer, 2026-10-04: cities can be built on ice; the test is ice SPEED, bedrock below is only "ideal", and no speed threshold has been set).** **Ground stability against the `DR-52` test ("ice not moving fast enough to force relocation; ideally bedrock below"), as the research agents found it. Confidence and sources are in each block; "qualifies" does not mean "should be a town".** Counts: 20 qualify on the ground, 1 passes the speed test but has no surface rock (Kohnen), 7 unclear or split, 3 fail, 1 is not a separate station.

| # | Station | Ground verdict | Operating status | Main caveat |
|---|---|---|---|---|
| 1 | Arturo Prat | qualifies (caveats) | year-round | glacier adjacent; no ground survey |
| 2 | GARS | qualifies | year-round | one site with #3 and #22 |
| 3 | O'Higgins | qualifies | year-round | one site with #2 and #22; HSM 37 |
| 4 | Orcadas | qualifies | year-round | bedrock under buildings unconfirmed |
| 5 | Petrel | unclear | year-round since 2022 | moraine on ice-rich permafrost; bedrock 31 to 94 m |
| 6 | QinLing | qualifies | year-round since 2025 | best documented; katabatic wind |
| 7 | San Martín | qualifies | year-round | sea-ice-dependent access |
| 8 | Vernadsky | qualifies | year-round | piles in volcanic rock |
| 9 | Decepcion | unclear, leaning fail | summer-only | active caldera; one site with #11 |
| 10 | Druzhnaya IV | qualifies | mothballed (likely) | Landing Bluff; AWS only since about 2015 |
| 11 | Gabriel de Castilla | unclear, leaning fail | summer-only | volcano + erosion up to 2.5 m/yr |
| 12 | González Videla | qualifies | summer-only | HSM 56; tourist stop |
| 13 | Halley VI | FAILS | summer-only since 2017 | **already a city (developer, 2026-10-04): dropped from the batch**; floating shelf about 1,400 m/yr |
| 14 | Jinnah | FAILS (published point) | likely defunct | not in any register; no use since 1993 |
| 15 | Mendel | qualifies | summer-only | sand terrace over permafrost |
| 16 | Leningradskaya | qualifies | mothballed since 1991 | last visit Jan 2020 |
| 17 | Matienzo | unclear (split) | lapsed (last 2018) | base on rock; ski-way on thinning shelf |
| 18 | Molodezhnaya | qualifies | seasonal field base | decaying legacy; flood hazard |
| 19 | Mountain Evening (Mt Vechernyaya) | qualifies | summer-only | Belarus; wintering planned, unconfirmed |
| 20 | Maldonado | qualifies (caveats) | summer-only | glacier proximity disputed |
| 21 | Primavera | qualifies | summer-only (reactivated) | ASPA 134 next door |
| 22 | Rada Covadonga | not a separate station | (O'Higgins anchorage) | fold into #3 |
| 23 | Risopatrón | qualifies | summer-only | 5 to 6 people; ASPA 112 adjacent |
| 24 | Russkaya | qualifies | mothballed since 1990 | active revival effort, unbuilt |
| 25 | Cape Shirreff (Guillermo Mann) | qualifies | summer-only | relabel; ASPA 149 |
| 26 | Brown | qualifies | summer-only (not closed) | heavy tourism |
| 27 | Carvajal | split: pad qualifies, runway fails | closed; reopening unconfirmed | only genuine closure |
| 28 | Kohnen | passes speed; no surface rock | mothballed | opens every 2 to 3 years |
| 29 | Melchior | unclear | summer-only (not closed) | rock vs ice-capped island conflict |
| 30 | Arturo Parodi | FAILS | dismantled 2013 | identity trap (Patriot Hills); drop |
| 31 | Sarie Marais | unclear | decommissioned 2001/02 | recycled; drop from B2 |
| 32 | Soyuz | qualifies on ground | abandoned 1989 | derelict by 2010; drop from B2 |

**Tier changes the evidence supports (developer decisions; nothing changed):** fold #22 into #3 (and #2, #3, #22 are one site); drop #30 (and do not substitute Union Glacier); move #31 and #32 out of B2; #26 and #29 are not really closed; #9 and #11 are one site. Ice speeds computed by the agents from ITS_LIVE cannot tell rock from slow ice (0 to 3 m/yr = stationary or rock).

## Rows that may be one physical site

Pairs within 10 km of each other in this batch. The inventory keeps them as separate rows; decide in the research pass whether each pair or group is one site.

| Row A | Row B | Distance |
|---|---|---|
| German Antarctic Receiving Station (GARS) | O'Higgins Base | 0.1 km |
| O'Higgins Base | Rada Covadonga | 0.1 km |
| German Antarctic Receiving Station (GARS) | Rada Covadonga | 0.1 km |
| Decepcion | Gabriel de Castilla Station | 1.3 km |
| Arturo Prat Antarctic Naval Base | Pedro Vicente Maldonado | 5.1 km |
| Gabriel Gonzalez Videla | Brown | 8.0 km |
| Pedro Vicente Maldonado | Risopatron | 8.1 km |

**Other duplicates to watch (outside this batch):** Belgrano II Skiway sits on Matienzo's coordinates; Marble Point Heliport is within about 4 km of the Marble Point depot (an "other" row).

## Index

**A1: Active, year-round**

1. Arturo Prat Antarctic Naval Base (Pergamino, 42 km)
2. German Antarctic Receiving Station (GARS) (Esperanza, 47 km)
3. O'Higgins Base (Esperanza, 46 km)
4. Orcadas (Signy, 47 km)
5. Petrel (Esperanza, 38 km)
6. QinLing (Zukelli, 30 km)
7. San Martin (Rothera, 76 km)
8. Vernadsky (Palmer City, 54 km)

**A2: Active, summer-only**

9. Decepcion (Pergamino, 40 km)
10. Druzhnaya IV (Shirayuki, 104 km)
11. Gabriel de Castilla Station (Pergamino, 39 km)
12. Gabriel Gonzalez Videla (Puerto Abrigo, 30 km)
13. Halley VI (Halley, 30 km)
14. Jinnah Antarctic Station (Utstein, 193 km)
15. Johann Gregor Mendel Czech Antarctic Station (Esperanza, 63 km)
16. Leningradskaya (Cape Adare, 450 km)
17. Matienzo (Puerto Abrigo, 162 km)
18. Molodezhnaya (Temirötkel, 296 km)
19. Mountain Evening (Temirötkel, 308 km)
20. Pedro Vicente Maldonado (Pergamino, 40 km)
21. Primavera (Puerto Abrigo, 142 km)
22. Rada Covadonga (Esperanza, 46 km)
23. Risopatron (Pergamino, 46 km)
24. Russkaya (Byrd, 713 km)
25. Shirreff Base (Pergamino, 28 km)

**B1: Temporarily closed per COMNAP 2024**

26. Brown (Puerto Abrigo, 30 km)
27. Carvajal (Rothera, 40 km)
28. Kohnen (Troll, 341 km)
29. Melchior (Puerto Abrigo, 60 km)

**B2: Closed since 2000, plausibly revivable**

30. Arturo Parodi Station (Byrd, 713 km)
31. Sarie Marais (Sanay, 40 km)
32. Soyuz (Shirayuki, 310 km)


---

## Tier A1: Active, year-round

### 1. Arturo Prat Antarctic Naval Base  `arturo-prat-antarctic-naval-base`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | Captain Arturo Prat Base / Arturo Prat / Prat / Capitan Arturo Prat / Arturo Prat Station / Base Naval Antártica Arturo Prat / Arturo-Prat-Station / Base Capitão Arturo Prat / base navale Capitán-Arturo-Prat / Base Naval Capitán Arturo Prat / Base navale capitano Arturo Prat / Captain Arturo Prat Basis / Captain Arturo Prat基地 / Arturo Prat-Station |
| Coordinates (lat, lon) | -62.478717, -59.663603  *(source: comnap24)* |
| Largest source disagreement | 2.6 km |
| Elevation (m) | 3  *(source: comnap24)* |
| Type / detail | station / comnap24:Station / comnap17:Station / wikidata:Antarctic research station / scar:Station / scar:Station |
| Status | year-round  *(COMNAP 2024: Year-Round, Open)* |
| Status across sources | comnap24: COMNAP 2024: Year-Round, Open // comnap17: COMNAP 2017: operational period "Year-round" // wp_list: Wikipedia list: permanent active |
| Years opened / closed | 1947 / n/a (active) |
| Capacity (winter / summer / peak) | 8 / 20 / 30 |
| Operator (context only) | Chile - Chilean Navy ; Instituto Antártico Chileno |
| Purpose as stated | science disciplines: Environmental sciences, Geology, Glaciology, Meteorology, Other Biological sciences |
| Surface | bare rock |
| Stability flag (sources only) | rock |
| Location text | Greenwich Island |
| Nearest city | Pergamino, 41.5 km (NEAR_CITY) |
| Nearest highway | hwy1, 158 km  *(lines good to about ±20 km)* |
| Inventory notes | COMNAP 2017 DMS: 62°28’43’’S 59°39’48’’W // COMNAP 2024 DDM: 62° 28.723' S 59° 39.8162' W // COMNAP region: Antarctic Peninsula // COMNAP 2017 permafrost: Discontinuous |
| Sources | COMNAP Facilities CSV (Nov 2024) ; COMNAP Station Catalog (Aug 2017) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) ; SCAR Composite Gazetteer (placenames.aq) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -62.4787, -59.6636 confirmed (COMNAP exact; Chilean Met Service -62.47889, -59.66389; SCAR UK -62.4804, -59.6659; all within about 200 m). Outlier: Spanish Wikipedia 59°37'49"W is about 1.7 km east, probably the Puerto Soberanía anchorage. Elevation 3 to 5 m (a US gazetteer "33 m" conflicts with everything else) | COMNAP rec. 28; DMC 950014; SCAR gazetteer; 2026-10-04 |
| Surface verified (rock / ice / other) | **Ice-free ground, low shingle-covered Guesalaga Peninsula** (US gazetteer); POLARIN "built on ice-free ground", discontinuous permafrost. Surrounding bedrock andesite/diorite/breccias/tuffs (ASPA 144 plan, 1987). Not measured: no bore or survey found | SCAR gazetteer; POLARIN Station/110; ATS Att145; 2026-10-04 |
| Ice velocity (m/yr) | Not found. Fuerza Aérea Glacier fringes the coast from the station's anchorage southward (centroid about 1.5 to 2 km S); no velocity or terminus distance measured. Greenwich Island glaciers are all retreating (0.32 km2/yr 1956 to 2023, faster after 2014); no source names glaciers advancing toward the station | SCAR gazetteer (CHL entry); scielo Anais da Acad. Bras. Ciências; 2026-10-04 |
| Ice thickness (m) | Not found | dead end |
| Bed elevation (m) | Not found | dead end |
| Depth to bedrock below surface (m) | Not found (no bore, geophysics or soil survey located). Shallow ground implied by wells that freeze in winter (1993 inspection) | 1993 Art. VII report |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **QUALIFIES with caveats.** About 85% confidence it is not on ice; about 60% that bedrock lies shallow. Same cove since 1947; no relocation, burial or erosion report; slope/glacier hazards are field-travel risks | Log; 2026-10-04 |
| Status verified (year-round / summer / closed / abandoned) | Year-round, open (COMNAP; 11 sailors deployed Nov 2024). **Closed 23 Feb 2004, reopened 12 Mar 2008** (the interim period was reported as summer-only by some sources) | COMNAP rec. 28; Aimone 2008; seawaves 2025 |
| Year opened / year closed, verified | Opened 6 Feb 1947 as "Soberanía" (6 men, one 14 by 3.4 m prefab), renamed Arturo Prat 1948; main building 1947 plus additions 1984; closed 2004; reopened 2008; handed to the Magallanes regional government 1 Mar 2006 (Wikipedia, lead only) | Revista de Marina 1972, 2008; 1993 report |
| Capacity: winter / summer (persons) | Sources disagree: winter 8 to 11 (1993 report: normal 9, comfortable maximum 15), summer 20 to 35; COMNAP peak 32; INACH lab 8 to 11 beds | COMNAP; 1993 report; POLARIN; UOH annex |
| Buildings and infrastructure: state, power, water | 1,500 m2 under roof (POLARIN), 150 m2 labs; 1993: main building, emergency building, four sheds; two wells (20,000 L, brackish when frozen); three 40 kW diesels (about 80 t fuel/yr), 8 x 20,000 L tanks, no berms (1993); AWS installed 24 Jan 2023; tide gauge since 1983 (non-operational from 2004, status after 2008 unconfirmed). Not found: current power system, whether the planned pier was built | 1993 report; POLARIN; DMC page |
| Landing/harbor/airstrip access | **No airstrip.** Three helipads (up to Sea King size), small jetty for craft up to about 10 m, inflatables; ships anchor in Iquique Cove / Puerto Soberanía, ice-free in summer. Medevac and mail via Eduardo Frei (47.6 km, King George Island aerodrome) | 1993 report; Chile gazetteer |
| Reachability from nearest city and highway (route, season) | Chilean Navy ship from Punta Arenas via the Drake Passage, resupply once a year (about 10 ship visits listed by POLARIN); ship season roughly Jan to Mar and Oct to Dec; hospital about 1,000 km away. Nearest city Pergamino 41.5 km; Hwy 1 158 km (±20 km) | 1993 report; POLARIN |
| Other facilities within 25 km | Pedro Vicente Maldonado (Ecuador, #20) 5.1 km, seasonal, peak 34; Risopatrón (Chile, #23) 11.3 km, seasonal, peak 6, next to ASPA 112; Cámara (Argentina, Half Moon Island) 18.3 km, seasonal, peak 22. Beyond: Juan Carlos I 42 km, St Kliment Ohridski 40 km, Fildes cluster 46 to 51 km. HSM 32, 33, 34, 35 on the site itself | COMNAP rec. 38, 33, 6; HSM list |

**Notes / dead ends / open questions:**

**Verdict: qualifies with caveats (the batch's weakest stability evidence: official pages carry almost no ground data).** Stated purpose: sovereignty (originally), maritime traffic control and safety of navigation, meteorology/glaciology reports, ionosphere, INACH science. Hazards on record: 1948 blizzard death; base commander's fall (1960 or 1961, sources conflict; 150 m fall "verifying glaciological conditions of Bahía Chile"); electrical fire problems (pre-1993); about 10,000 L diesel spill 1979. No storm-surge/sea-level damage found (dead end). Climate: annual mean about -2.3 °C (POLARIN), July -6.7, Feb +1.6, record 13.0/-30.0 °C, about 709 mm. ASPA 144 (Chile Bay, two benthic sites) is offshore only; the current plan was not retrieved. ONE contradiction the log flags: The Clinic (2013) puts Prat on King George Island, wrong. Full log: `Research_Logs/Batch1_A1_ArturoPrat_SanMartin_2026-10-04.md`.

### 2. German Antarctic Receiving Station (GARS)  `german-antarctic-receiving-station-gars`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | German Antarctic Receiving Station / GARS / GARS O'Higgins / Estación Alemana de Recepción Antártica / GARS-O’Higgins / German Antartic Receiving Station |
| Coordinates (lat, lon) | -63.321092, -57.900940  *(source: comnap24)* |
| Largest source disagreement | 0.0 km |
| Elevation (m) | 17  *(source: comnap24)* |
| Type / detail | station / comnap24:Station / wikidata:Antarctic research station |
| Status | year-round  *(COMNAP 2024: Year-Round, Open)* |
| Status across sources | comnap24: COMNAP 2024: Year-Round, Open // wp_list: Wikipedia list: permanent active |
| Years opened / closed | 1991 / n/a (active) |
| Capacity (winter / summer / peak) | unknown / unknown / 10 |
| Operator (context only) | Germany - German Aerospace Center ; Alfred Wegener Institute for Polar and Marine Research ; Federal Agency for Cartography and Geodesy |
| Purpose as stated | German Antarctic Receiving Station or GARS O'Higgins is a German polar research station in Antarctica |
| Surface | unknown |
| Stability flag (sources only) | unknown |
| Location text | Cape Legoupil |
| Nearest city | Esperanza, 46.6 km (NEAR_CITY) |
| Nearest highway | hwy1, 31 km  *(lines good to about ±20 km)* |
| Inventory notes | COMNAP 2024 DDM: 63° 19.2655' S 57° 54.0564' W // COMNAP region: Antarctic Peninsula |
| Sources | COMNAP Facilities CSV (Nov 2024) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -63.3211, -57.9009 confirmed (COMNAP 2024 exact; operator DLR 63°19'14.88"S 57°54'03.05"W, about 33 m off); elevation 17 m (DLR 17.56 m) | [S1][S4] 2026-10-04 |
| Surface verified (rock / ice / other) | **Rock.** Isabel Riquelme islet / Schmidt Peninsula, about 150 by 200 m; GNSS pillar OHI3 "bolted on bedrock" (weathered low-metamorphic slates) | [S4][S13] 2026-10-04 |
| Ice velocity (m/yr) | n/a, site is not on ice. Nearest ice is the continental-glacier runway 3 km SE (not measured; no report of it threatening the site) | [S6] 2026-10-04 |
| Ice thickness (m) | n/a | n/a |
| Bed elevation (m) | n/a (rock at surface) | [S13] |
| Depth to bedrock below surface (m) | 0 (pillar anchored 0.5 m into bedrock). Ground uplift about 5 mm/yr (elastic rebound after the Prince Gustav Channel ice-shelf collapse) | [S13][S11][S12] 2026-10-04 |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **QUALIFIES (high confidence).** No report of burial, relocation or ice threat; storms damage antenna mounts (2012, 2013) | [S13][S14] 2026-10-04 |
| Status verified (year-round / summer / closed / abandoned) | Year-round, open. Staffed continuously since early/June 2010; before that campaign mode, mothballed in winter | [S1][S7][S9] 2026-10-04 |
| Year opened / year closed, verified | Opened 1991 (first ERS-1 data Sept 1991; Chilean Monuments Council: 10 Jan 1991). Not closed | [S1][S8][S15] |
| Capacity: winter / summer (persons) | COMNAP peak 10; permanent team 4 (2 engineers + 2 Chilean staff) rotating every 2 to 3 months | [S1][S5] 2026-10-04 |
| Buildings and infrastructure: state, power, water | 35 twenty-foot containers (15 research/living, 20 utility); own diesel generators; desalination; sewage biotreatment; 24 m3 double-walled fuel tanks (2014); 2/1 Mbit/s satellite link; 9 m L/S/X antenna; GNSS OHI2 + OHI3; tide gauges; met mast; EUR 2.5 M upgrade 2016; waste goes to the Chilean base | [S5][S7][S9][S14] 2026-10-04 |
| Landing/harbor/airstrip access | No pier of its own. Twin Otter (skis) lands on the glacier runway 3 km SE, year-round; Hercules to King George Island; helicopter backup; ships in summer (ice permitting). Suspension bridge links islet to mainland; connects at low tide | [S4][S6] 2026-10-04 |
| Reachability from nearest city and highway (route, season) | Punta Arenas then King George Island then Twin Otter; delays up to 4 weeks normal. Nearest city Esperanza 47 km; Hwy 1 158 km (±20 km) | [S6][S9] 2026-10-04 |
| Other facilities within 25 km | O'Higgins Base 0.06 km (year-round); Rada Covadonga record 0.14 km (see #22); next COMNAP facility Esperanza about 46 km; no refuge huts found within 25 km | [S1] 2026-10-04 |

**Notes / dead ends / open questions:**

**Verdict: rock-qualifies, high.** Stated purpose: satellite data reception (ERS, TerraSAR-X, TanDEM-X), VLBI and tectonic monitoring; over a third of TanDEM-X elevation-model data came from here. Wind gusts to 180 km/h (storms to 250). Penguins breed around the antenna. Shares its islet with O'Higgins (#3): treat #2, #3 and #22 as ONE site when it comes to town placement. Uplift figures from Bouin and Vigny / Dietrich are via search summary only (unverified). Open: Final CEE not relevant here; AWI 1997 Polarforschung paper unreachable. Full log: `Research_Logs/Batch1_A1_GARS_OHiggins_Petrel_2026-10-04.md`.

### 3. O'Higgins Base  `o-higgins-base`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | Base General Bernardo O'Higgins Riquelme / General Bernardo O'Higgins / O'Higgins / O'Higgins Station / General Bernardo O'Higgins Riquelme / General O'Higgins Station / Bernardo O'Higgins Station / Base General Bernardo O'Higgins / Basis General Bernardo O'Higgins Riquelme / Base generale Bernardo O'Higgins / Bernardo O'Higgins / Bernardo-O’Higgins-Station / Puerto Covadonga / Base Bernardo O'Higgins |
| Coordinates (lat, lon) | -63.320951, -57.899781  *(source: comnap24)* |
| Largest source disagreement | 0.5 km |
| Elevation (m) | 12  *(source: comnap24)* |
| Type / detail | station / comnap24:Station / comnap17:Station / wikidata:Antarctic research station / scar:Station / scar:Station |
| Status | year-round  *(COMNAP 2024: Year-Round, Open)* |
| Status across sources | comnap24: COMNAP 2024: Year-Round, Open // comnap17: COMNAP 2017: operational period "Year-round" // wp_list: Wikipedia list: permanent active |
| Years opened / closed | 1948 / n/a (active) |
| Capacity (winter / summer / peak) | 21 / 44 / 60 |
| Operator (context only) | Chile - Chilean Army ; Instituto Antártico Chileno |
| Purpose as stated | science disciplines: Geology, Glaciology, Marine biology, Meteorology |
| Surface | bare rock |
| Stability flag (sources only) | rock |
| Location text | Cape Legoupil |
| Nearest city | Esperanza, 46.5 km (NEAR_CITY) |
| Nearest highway | hwy1, 31 km  *(lines good to about ±20 km)* |
| Inventory notes | COMNAP 2017 DMS: 63°19’15’’S 57°53’59’’W // COMNAP 2024 DDM: 63° 19.2571' S 57° 53.9869' W // COMNAP 2017 permafrost: Discontinuous |
| Sources | COMNAP Facilities CSV (Nov 2024) ; COMNAP Station Catalog (Aug 2017) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) ; SCAR Composite Gazetteer (placenames.aq) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -63.3210, -57.8998 confirmed (COMNAP; Chilean Met Directorate -63.32083, -57.89944, 21 m off). Elevation 10 to 13 m (sources disagree) | [S1][S21] 2026-10-04 |
| Surface verified (rock / ice / other) | **Rock / ice-free ground** (same islet as GARS; Trinity Peninsula Group slates). COMNAP lists glacier, crevasses and moraines in the facility area (nearby, not under it) | [S3][S13] 2026-10-04 |
| Ice velocity (m/yr) | n/a, not on ice; no measurement found | n/a |
| Ice thickness (m) | n/a | n/a |
| Bed elevation (m) | n/a (rock at surface) | n/a |
| Depth to bedrock below surface (m) | At/near surface (inferred from the GARS pillar on the same islet; no base-specific borehole data found) | [S13] |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **QUALIFIES (moderate-high).** Continuous presence since 1948 with no closures and no relocation in 78 years; no site-specific report of ice, erosion or landslide threat found | [S15][S42] 2026-10-04 |
| Status verified (year-round / summer / closed / abandoned) | Year-round, open | [S1] 2026-10-04 |
| Year opened / year closed, verified | Inaugurated 18 Feb 1948; rebuilt about 2003 (over 2,000 m2); never closed. HSM 37 covers the original base, bust, plaque and grotto | [S15][S17][S38] 2026-10-04 |
| Capacity: winter / summer (persons) | Sources disagree: COMNAP 2017 winter 21+3 / summer 44+8, 60 beds, 3,000 m2; INACH 21 / 50; COMNAP 2024 peak 70 | [S3][S16][S1] 2026-10-04 |
| Buildings and infrastructure: state, power, water | 2003 rebuild: gym, 40 t demountable pier, power plant (fossil + renewable), sewage and desalination plants, labs (40 m2 dry lab), accommodation, met station, conference room for 80, helipad, crane, loaders, snowmobiles, Zodiac; HF/VHF, phone, internet | [S3][S16][S17] 2026-10-04 |
| Landing/harbor/airstrip access | COMNAP: ship landing facilities "None" yet a demountable pier is reported; 800 m runway listed but DLR says Twin Otters land on a glacier runway 3 km SE; Wikipedia says "on sea ice" (primary source DLR preferred) | [S3][S6][S17] 2026-10-04 |
| Reachability from nearest city and highway (route, season) | Air: Hercules flights (about 30/yr) then Twin Otter; sea: about 6 ship visits/yr (Dec to Apr, Oct to Nov); 1,380 km from Punta Arenas. Esperanza 47 km; Hwy 1 158 km (±20 km) | [S3] 2026-10-04 |
| Other facilities within 25 km | GARS 0.06 km; Rada Covadonga record 0.08 km; nothing else; Duroch Islands about 1 nmi off; View Point refuge (Boonen Rivera) 36 km (outside 25) | [S1][S36] 2026-10-04 |

**Notes / dead ends / open questions:**

**Verdict: rock-qualifies, moderate-high.** The only Chilean station with uninterrupted presence since its opening. Climate (DMC normals via Wikipedia table): annual mean -3.5 °C, July -7.9 °C, precipitation 558 mm; COMNAP's catalogue gives -9.8 °C and 621 mm (contradiction unresolved; DMC is the more traceable). Field hazard: crevasse death of three soldiers near View Point in 2005 (Wikipedia, citation-needed). HSM 37 sits on the site itself, so land use is restricted. Open: peninsula vs islet naming (USGS says Schmidt Peninsula tied to Cape Legoupil by a low isthmus; Chilean and DLR sources say Isabel Riquelme islet). Full log: `Research_Logs/Batch1_A1_GARS_OHiggins_Petrel_2026-10-04.md`.

### 4. Orcadas  `orcadas`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | Orcadas Station / Orcadas Antartic Base / Base Orcadas / Estacion Orcadas / Orcadas-Station / base antarctique Orcadas / Distaccamento navale Orcadas / Orcadas Base / Orcadas /Arg./ |
| Coordinates (lat, lon) | -60.737592, -44.737387  *(source: comnap24)* |
| Largest source disagreement | 1.8 km |
| Elevation (m) | 8  *(source: comnap24)* |
| Type / detail | station / comnap24:Station / comnap17:Station / wikidata:Antarctic research station / scar:Station / scar:Station |
| Status | year-round  *(COMNAP 2024: Year-Round, Open)* |
| Status across sources | comnap24: COMNAP 2024: Year-Round, Open // comnap17: COMNAP 2017: operational period "Year-round" // wp_list: Wikipedia list: permanent active |
| Years opened / closed | 1904 / n/a (active) |
| Capacity (winter / summer / peak) | 15 / 35 / 65 |
| Operator (context only) | Argentina - Instituto Antartico Argentino, Argentine Navy |
| Purpose as stated | science disciplines: Geodesy, Geophysics, Terrestrial biology |
| Surface | bare rock |
| Stability flag (sources only) | rock |
| Location text | Laurie Island, South Orkney Islands |
| Nearest city | Signy, 47.0 km (NEAR_CITY) |
| Nearest highway | hwy1, 703 km  *(lines good to about ±20 km)* |
| Inventory notes | Also in wikidata (not a separate row): "Casa Moneta" [building; heritage] at -60.7403,-44.7425 // Also in wikidata (not a separate row): "Orcadas Magnetic Observatory" [magnetic observatory] at -60.7370,-44.7400 // COMNAP 2017 DMS: 60°44’25.6’’S 44°44’24.3’’W // COMNAP 2024 DDM: 60° 44.2555' S 44° 44.2432' W // COMNAP 2017 permafrost: Continuous |
| Sources | COMNAP Facilities CSV (Nov 2024) ; COMNAP Station Catalog (Aug 2017) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) ; SCAR Composite Gazetteer (placenames.aq) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -60.7376, -44.7374 confirmed (COMNAP 2024 exact; Wikipedia 50 m off; COMNAP 2017 catalogue about 350 m off). Elevation 8 m (COMNAP) vs 4 m (Wikipedia text) vs 12 m (blog). On the Ibarguren Isthmus between Scotia Bay and Uruguay Cove | COMNAP; Cancillería; 2026-10-04 |
| Surface verified (rock / ice / other) | **Ice-free ground, low isthmus 4 to 8 m a.s.l., 170 m from the shore** (COMNAP: "Ice-free ground", features: beaches, coast, **moraine**; permafrost "Continuous"). Island bedrock is Greywacke-Shale Formation. **Bedrock directly under the buildings NOT confirmed**: the moraine note suggests unconsolidated glacial deposits | COMNAP 2017 catalogue p.21; Wikipedia Laurie Island (lead only) |
| Ice velocity (m/yr) | Not found. Laurie Island glaciers exist behind the station; no distance to the nearest glacier and no advance report found (died at the sources) | dead end |
| Ice thickness (m) | n/a (not on ice) | n/a |
| Bed elevation (m) | Not found | dead end |
| Depth to bedrock below surface (m) | Not found; no borehole or CALM data for Laurie Island | dead end |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **QUALIFIES, moderate-to-high, with a stated gap.** 122 years on the same spot (Omond House 1903, stone, still standing; Casa Moneta 1905; HSM 42); no relocation, burial or ice threat on record. Unverified: a 1903 storm put waves within about 2 m of Omond House (AIDCA via search summary) | COMNAP; HSM 42; 2026-10-04 |
| Status verified (year-round / summer / closed / abandoned) | Year-round, open | COMNAP 2024 |
| Year opened / year closed, verified | Founded 1 Apr 1903 (Scottish National Antarctic Expedition, Bruce); handed to Argentina by decree 3073 (2 Jan 1904), formal transfer 22 Feb 1904; Casa Moneta 1905; radiotelegraph 1927; Navy 1951/52; new LABORC lab about 2023. COMNAP says 1904. Never closed | Cancillería; COMNAP |
| Capacity: winter / summer (persons) | COMNAP 2017: summer 35, winter 15+2, 52 beds, max 65 (COMNAP 2024 peak 65); winter crew 2022/23: 24; Jan 2024 handover 10 out / 10 in; main house 25 | COMNAP; argentina.gob.ar 2023; La Capital 2024 |
| Buildings and infrastructure: state, power, water | 11 buildings, 2,101 m2 under roof, 4,800 m2 total; main house with chapel, gym, library; Omond House + Casa Moneta museum; outbuildings separated for fire protection; labs 76 m2 + new LABORC; 26 m2 clinic. Power: fossil, 220 V (about 4 diesels, 280 kW, about 192,000 L/yr per secondary mirrors). Water: about 1.08 million L/yr from melted snow/ice (secondary). E-mail, internet, satellite phone, VHF; lighthouse on the comms tower | COMNAP 2017; Wikipedia lead; Hispanopedia (secondary) |
| Landing/harbor/airstrip access | **No airstrip, no pier** ("Ship landing facilities: None"); helipad yes. Zodiacs to a beach and a snow staircase; icebreaker Irízar with Sea King helicopters. On 15 Dec 2025 the icebreaker could not dock and drifted in Scotia Bay; a Sea King made 23 flights in about 2 h to land 21 crew, fuel and scientists | COMNAP; argentina.gob.ar 2025 |
| Reachability from nearest city and highway (route, season) | Ushuaia about 1,502 km; about 25 ship visits/yr (Jan to Mar, Nov to Dec); reliefs in Dec to Jan; no access by ship in winter (SHN report 1 Oct 2026: Scotia Bay 10/10 first-year fast ice); sea ice freezes out 7+ km. Nearest city Signy 46.8 km (sea only) | COMNAP; SHN; La Capital 2024 |
| Other facilities within 25 km | **Cape Geddes Station C (British FIDS, 1946 to Mar 1947), about 10.5 km NW, closed**; a small hut survives (weak source). **Sandefjord Bay is NOT within 25 km**: it is on Coronation Island's west coast, about 73 km from Orcadas (about 27 km from Signy); the 1945 hut there was never occupied and had collapsed by 1955 | COMNAP; Wikipedia (lead only); 2026-10-04 |

**Notes / dead ends / open questions:**

**Verdict: qualifies (moderate-to-high).** Correction to the inventory: the row "Sandefjord Bay Station" (unknown status, 26 km from Signy) is the Coronation Island site of an unoccupied 1945 hut, not a station; the real nearby facility is Station C at Cape Geddes (naming unresolved: the BAS page title reads "Sandefjord Bay Station C"). Purpose: the longest continuous Antarctic meteorological record (since 1903; Zazulie 2010: significant warming since 1950, none 1903 to 1950); glaciology, seismology, sea-ice work since 1985, geodesy, biology. Climate: annual mean -4.9 °C (Cancillería) vs -3.6 °C (COMNAP); precipitation 398, 486 or 1,180 mm (three sources); mean wind 24 km/h, gusts above 150 km/h; snow about 227 days, fog about 110. IBAs at Ferguslie Peninsula/Cape Geddes (about 12,000 chinstrap pairs); HSM 42 on site constrains land use. Open: ground ice/bedrock under the buildings, distance to nearest glacier (Hrbáček 2023 review not opened), Zazulie full text (site-move history), ATS HSM/ASPA entries. Full log: `Research_Logs/Batch1_A1_Orcadas_Vernadsky_2026-10-04.md`.

### 5. Petrel  `petrel`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | Petrel Base / Base Antártica Petrel / Petrel Antartic Base / Base Petrel / Petrel-Station / Baza Petrel / Stazione Petrel |
| Coordinates (lat, lon) | -63.478303, -56.230993  *(source: comnap24)* |
| Largest source disagreement | 2.9 km |
| Elevation (m) | 18  *(source: comnap24)* |
| Type / detail | station / comnap24:Station / comnap17:Station / wikidata:Antarctic research station |
| Status | year-round  *(COMNAP 2024: Year-Round, Open)* |
| Status across sources | comnap24: COMNAP 2024: Year-Round, Open // comnap17: COMNAP 2017: operational period "October–March" // wp_list: Wikipedia list: permanent active // wp_list: Wikipedia list: summer-only active |
| Years opened / closed | 1952 / n/a (active) |
| Capacity (winter / summer / peak) | 25 / 23 / 25 |
| Operator (context only) | Argentina - Argentine Army, Argentine Navy ; Argentina - Instituto Antartico Argentino ; Argentine Antarctic Institute |
| Purpose as stated | science disciplines: Geology |
| Surface | bare rock |
| Stability flag (sources only) | rock |
| Location text | Dundee Island |
| Nearest city | Esperanza, 38.4 km (NEAR_CITY) |
| Nearest highway | hwy1, 35 km  *(lines good to about ±20 km)* |
| Inventory notes | COMNAP 2017 DMS: 63°28’41.9’’S 56°13’51.6’’W // COMNAP 2024 DDM: 63° 28.6982' S 56° 13.8596' W // Wikipedia list has 2 rows merged here: Petrel (permanent_active 1967-); Petrel (summer_only_active 1967-) // COMNAP 2017 permafrost: Sporadic |
| Sources | COMNAP Facilities CSV (Nov 2024) ; COMNAP Station Catalog (Aug 2017) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -63.4783, -56.2310 confirmed (COMNAP 2024 and 2017 catalogue; Wikipedia about 118 m off). The Draft CEE's "63°28'S 56°17'W" is about 2.9 km west and treated as a typo. Elevation 18 m | [S1][S3][S23] 2026-10-04 |
| Surface verified (rock / ice / other) | **NOT bedrock.** Cape Welchness plain (2.5 km2, the island's only ice-free area) at the foot of the Rosamaría glacier; buildings on a bottom-moraine terrace of **ice-rich permafrost** (active layer 1.4 to 2.5 m); lateral moraines have buried ice cores. COMNAP says "ice-free ground", the CEE's geotechnics are more specific | [S23] 2026-10-04 |
| Ice velocity (m/yr) | Not found. The Rosamaría glacier "is in clear retreat" (CEE); press puts its edge about 200 m from the base. No velocity or retreat rate found (died at the sources) | [S23][S25] 2026-10-04 |
| Ice thickness (m) | Glacier about 35 m average height (visitor press, not a measurement); no thickness data found | [S28] |
| Bed elevation (m) | Not given as elevation; see depth below | n/a |
| Depth to bedrock below surface (m) | Geophysics: Pleistocene bottom moraine 17.9 to 42.7 m (mean 32.4 m); Lower Cretaceous mudstone/sandstone ("intensely fractured") about 66.8 m mean (30.8 to 93.8 m); Triassic Trinity Peninsula Group below. Cretaceous crops out about 15 m a.s.l. in the ESE ravine | [S23] 2026-10-04 |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **UNCLEAR (mixed), moderate.** Passes "ice not forcing relocation" (retreating glacier; reopened 2021 on the same terrace). Fails "bedrock close below". The CEE blames existing building deficiencies on ground movement and designs the new base on piles 2 m or more into permafrost, raised 3 to 4 m. Permafrost thaw and subsidence are called "central to Petrel Base" | [S23] 2026-10-04 |
| Status verified (year-round / summer / closed / abandoned) | Year-round again since reopening 9 Dec 2021 (one source 15 Nov 2021); wintering since 2022; 22 wintering July 2026. COMNAP 2017 listed it seasonal. Summer-only 1978 to 2017/18 (fire evacuation 1974; closed after 2017/18 on budget cuts) | [S25][S26][S29][S3] 2026-10-04 |
| Year opened / year closed, verified | Naval refuge 1950/51 (other sources Jan 1952, Dec 1952); permanent detachment inaugurated 22 Feb 1967; fire 1974; summer-only Feb 1978 (AAD says 1976); closed 2017/18; reopened Dec 2021; works planned to the 2028/29 summer | [S23][S3][S30] 2026-10-04 |
| Capacity: winter / summer (persons) | Now 22 wintering (Jul 2026; all male) / 30 (Dec 2024). COMNAP: 25 beds, peak 45. Design in the CEE: 60 permanent + 80 transit = 140 (press: 60 winter, 120 summer) | [S26][S28][S1][S23] 2026-10-04 |
| Buildings and infrastructure: state, power, water | Hangar about 1,150 m2 (recovered), warehouses, main house 275 m2, 12-person emergency house; planned six-module building about 2,400 m2 (labs, clinic, quarters). Two 160 kVA generators; solar 192 panels (goal 576); 3 x 25,000 L tanks + 31,000 L anti-spill. Water from a summer lagoon and an artificial lagoon, winter sea-ice melter (about 25 people); RO and sewage plants planned | [S23][S25][S26][S28] 2026-10-04 |
| Landing/harbor/airstrip access | Runway built up to Hercules class (length sources disagree: 850 m in 1967, then 1,000, about 1,400, 1,600 or 1,300 m); first landing 1 Jun 2024 (Saab 340, summary only). **No pier**; a 200 m pier is planned after bathymetry; icebergs and brash ice are a risk; Petrel Cove is the best local anchorage but ice-closed much of the year. Helipad on site | [S23][S25][S26][S28] 2026-10-04 |
| Reachability from nearest city and highway (route, season) | Ships (icebreaker Irízar, supply ship Puerto Argentino) mostly Dec to Feb; Twin Otters regularly, Hercules by runway; about 1,100 to 1,300 km from Ushuaia; Marambio about 80 to 87 km. Nearest city Esperanza 38 km; nearest Hwy 1 far (see inventory) | [S23][S26][S28] 2026-10-04 |
| Other facilities within 25 km | None among COMNAP facilities (Esperanza 39 km, Elichiribehety about 39 km). Paulet Island about 25 km SE: HSM 41 (1903 hut, grave, cairn) and a large Adélie colony. ASPA 148 (Mount Flora) about 40 km | [S1][S46] 2026-10-04 |

**Notes / dead ends / open questions:**

**Verdict: unclear, moderate.** The only station of the three with real settlement-planner caveats: moraine on ice-rich permafrost, buildings in poor state from ground movement, no pier, strong wind as the main operational obstacle (design maximum 149 km/h, 300 km/h gusts; recorded extremes 157 to 176 km/h). Climate (1967-76 Petrel record): annual mean -6.8 °C, extremes 12.1 and -31.5 °C; COMNAP 2017 gives -7.1 °C, 200 mm precipitation, mean wind 8 km/h (far lower than the CEE's 18 to 30 km/h means; the CEE is measured and more specific). Winter daylight about 4 h. Stated purpose: logistics hub and entry point for Argentine Peninsula operations; seismology, geology, a weather station. Open: the ATS-hosted Draft CEE and the Final CEE (IP133 at ATCM46) were not opened; glacier velocity unknown. Full log: `Research_Logs/Batch1_A1_GARS_OHiggins_Petrel_2026-10-04.md`.

### 6. QinLing  `qinling`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | Qinling Station / Qinling-Station / Base Qinling |
| Coordinates (lat, lon) | -74.934071, 163.713006  *(source: comnap24)* |
| Largest source disagreement | 0.1 km |
| Elevation (m) | unknown  *(source: unknown)* |
| Type / detail | station / comnap24:Station / wikidata:Antarctic research station |
| Status | year-round  *(COMNAP 2024: Year-Round, Open)* |
| Status across sources | comnap24: COMNAP 2024: Year-Round, Open // wp_list: Wikipedia list: permanent active |
| Years opened / closed | 2024 / n/a (active) |
| Capacity (winter / summer / peak) | 30 / 80 / 80 |
| Operator (context only) | China - Polar Research Institute of China |
| Purpose as stated | Qinling Station (Chinese: 秦岭站; pinyin: Qínlǐng zhàn) is an Antarctic research station operated by the Polar Research Institute of China |
| Surface | unknown |
| Stability flag (sources only) | unknown |
| Location text | Inexpressible Island, Terra Nova Bay |
| Nearest city | Zukelli, 30.3 km (NEAR_CITY) |
| Nearest highway | spur_zukelli, 30 km  *(lines good to about ±20 km)* |
| Inventory notes | COMNAP 2024 DDM: 74° 56.0443' S 163° 42.7804' E |
| Sources | COMNAP Facilities CSV (Nov 2024) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -74.9341, 163.7130 confirmed (COMNAP record 245, within about 10 m; ASPA 178 plan 74°56'04"S 163°42'52"E). The CEEs give a nominal 74°55'S 163°42'E, about 2 km north, because the 2018 revised draft moved the site 2 km south away from the Adélie colony. Elevation: COMNAP blank; CEE "standard terrain elevation" about 6 to 30 m (eastern step about 10 m) | COMNAP; ASPA 178 plan; Final CEE p.129, 182 |
| Surface verified (rock / ice / other) | **Rock.** Rock and gravel coastal terrace in a small embayment on the SE coast; surface is moraine with exposed bedrock; "mostly gravel, block stone and slightly weathered monzonitic granite" within the 10.1 m survey depth | Final CEE p.179, 188; Australian inspection 2020 p.22 to 23 |
| Ice velocity (m/yr) | Station is **not on ice**. Neighbors (not the site): Priestley Glacier up to about 180 m/yr, Reeves up to about 320 m/yr; the floating Nansen Ice Shelf (about 1,800 km2, calved massively Apr 2016) is pinned by Inexpressible Island. Distance from the station to the shelf edge not stated anywhere | Dow et al. 2024, The Cryosphere 18:1105; Final CEE p.177 |
| Ice thickness (m) | n/a at the site (rock) | n/a |
| Bed elevation (m) | Not given separately; bedrock exposed or shallow | Final CEE p.130, 186 |
| Depth to bedrock below surface (m) | Exposed or shallow: 12 holes (93 m) + 4 pits (7.1 m), hole depths 4.0 to 10.1 m, bedrock found in 7 holes under the main-building area; the 2014 survey failed to drill through the granite (thickness unknown). Bearing capacity granite 6,000 to 13,000 kPa, boulder soil 500 kPa | Final CEE p.50, 130, 131, 188 |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **QUALIFIES (high).** CEE §4.2.3: "no adverse geological effects ... no active faults ... The proposed site is a stable site." Cautions: seasonal frost heave/thaw settlement 0.6 to 0.8 m (design under 1.5 m), raised-beach terrace 6 to 30 m, corrosive seawater, **katabatic wind is the real hazard** (not ice) | Final CEE p.188, 189 |
| Status verified (year-round / summer / closed / abandoned) | **Year-round as of the 2026 winter** (COMNAP: Year-Round, Open). First confirmed winter-over 2025 (43 people; 32 construction staff also cited, not reconciled); 2026 winter 18 people. **No 2024 winter found.** Operational research began 9 Apr 2026 | COMNAP; Tide News 2025; Xinhua 21 Feb and 9 Apr 2026 |
| Year opened / year closed, verified | Draft CEE Jan 2014; revised draft Jan 2018 (site moved 2 km south); foundation ceremony 7 Feb 2018; temporary containers 2017/18 to 2019/20; Final CEE Oct 2021; ASPA 178 designated 2021; main construction 16 Dec 2023 (about 52 to 60 days); declared built 7 Feb 2024; COMNAP year 2024. Design life at least 25 years, intended to be dismantled and the site restored | ATS EIA 1565, 2292; ATCM XLI/XLIII; China Daily HK 2024 |
| Capacity: winter / summer (persons) | Design 30 winter / 80 summer (science to support 1:2 winter, 1:1 summer); COMNAP "peak population" 120 (probably includes construction crews, unverified); actual 21 (Jan 2020 inspection), 51 summer team 2024/25, 69 summer / 18 winter 2026 | Final CEE p.6, 60; COMNAP; Xinhua |
| Buildings and infrastructure: state, power, water | Built area 5,244 m2 ("Southern Cross" radial layout, 45% modular); elevated central building about 11.8 m. Power as built (Chinese reports): wind + solar 230 kW (about 60% of capacity) with hydrogen fuel cell and electrolyzer; renewables replaced diesel from 1 Mar 2025; the Final CEE design added 3 x 300 kW diesel, a micro-gas turbine, 300 kWh storage. Water: seawater reverse osmosis only (no meltwater), design 7,200 L/day. Fuel: 12 tanks x 88 m3 (about 2.5-year reserve). Satellite ground station planned | Final CEE p.76 to 121; China Energy News 2025; CSIS 2024 |
| Landing/harbor/airstrip access | **Rock-fill wharf** on the north shore of "South Bay" (about 36.7 by 12 m, 1,930 m3 stone) berthing a tug and a barge; **helipad yes** (concrete pad in 2024 imagery), 2-helicopter hangar. **No airstrip on the island** (none in the Final CEE; an unsourced Indian think-tank claim of a runway is contradicted); fixed-wing would use Italy's Boulder Clay gravel runway via a surveyed 38.6 km overland route | Final CEE p.49, 134 to 139; ENEA 2022 |
| Reachability from nearest city and highway (route, season) | Icebreakers Xuelong / Xuelong 2 from Shanghai via New Zealand; ship window about mid-Dec to late Feb; barges and helicopters ashore; isolated in winter. Nearest city Zukelli 29 km (helicopter or sea); Hwy per inventory | Final CEE p.68, 69; Draft CEE 2014 |
| Other facilities within 25 km | **No COMNAP facility within 25 km.** Next: Enigma Lake camp 25.6 km (seasonal), Mario Zucchelli 29.0 km, Gondwana 36.4 km, Jang Bogo 37.4 km (year-round). Outside COMNAP: Boulder Clay runway about 22.8 km; HSM 14 Inexpressible Island Ice Cave about 3.8 km (the ice cave is destroyed by ablation; plaque remains); ASPA 178 about 3 km (Adélie colony 29,899 pairs in 2019); HSM 68 Hells Gate Moraine depot about 8.3 km; ASPA 161 about 22 to 24 km | COMNAP; ASPA 178 plan; ATCM XLIII |

**Notes / dead ends / open questions:**

**Verdict: qualifies, high.** The best-documented station in the batch (326-page Final CEE read in full). Stated purpose: Ross Sea climate/cryosphere/ocean observatory, ice-shelf-ocean interaction, ecosystem monitoring, space physics paired with Zhongshan; marine lab to be open to neighboring stations. Climate: mean annual -18.5 °C (Manuela AWS), mean wind 12 m/s (ASPA plan says 14.2), max 43.5 to 45 m/s; 298 strong katabatic events in about 10 years, mostly winter; gales over 100 days a year; a force-12 hurricane Jan 2024 (Chinese news summary, unverified). ASPA 178 rules: no vehicles inside, helicopter landing prohibited without permit, overflight below 2,000 ft prohibited. Tourism: about 100 visitors/yr (up to 480 in 2005/06). Not to be confused with China's separate draft CEE (Mar 2025) for a seasonal station at Cox Point, Marie Byrd Land. Open: the 2018 revised draft CEE (ATS URLs failed; may mention an "ice runway", unresolved), the US inspection report (ATCM XLIII), SCAR gazetteer entry, distance to the Nansen shelf edge, any 2024 winter-over. Full log: `Research_Logs/Batch1_A1_QinLing_and_WAIS_Divide_2026-10-04.md`.

### 7. San Martin  `san-martin`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | San Martín Base / San Martin abandoned Station / San Martín Station / San Martin Antartic Base / Base Antártica San Martín / Base San Martín / Base dell'esercito generale San Martín / base antarctique San-Martín / San Martín basis / General-San-Martin-Station / base antarctique Saint-Martin / San Martín /Arg./ |
| Coordinates (lat, lon) | -68.130300, -67.102931  *(source: comnap24)* |
| Largest source disagreement | 2.0 km |
| Elevation (m) | 5  *(source: comnap24)* |
| Type / detail | station / comnap24:Station / comnap17:Station / wikidata:Antarctic research station; human settlement / scar:Station / scar:Station |
| Status | year-round  *(COMNAP 2024: Year-Round, Open)* |
| Status across sources | comnap24: COMNAP 2024: Year-Round, Open // comnap17: COMNAP 2017: operational period "Year-round" // wp_list: Wikipedia list: permanent active // wp_hsm: Historic Site/Monument no. 26 |
| Years opened / closed | 1951 / n/a (active) |
| Capacity (winter / summer / peak) | 19 / 15 / 21 |
| Operator (context only) | Argentina - Instituto Antartico Argentino ; Argentine Antarctic Institute |
| Purpose as stated | science disciplines: Geodesy, Geology, Geomorphology, Geophysics and Seismology, Glaciology |
| Surface | bare rock |
| Stability flag (sources only) | rock |
| Location text | Barry Island |
| Nearest city | Rothera, 75.7 km (NEAR_CITY) |
| Nearest highway | hwy1, 3 km  *(lines good to about ±20 km)* |
| Inventory notes | COMNAP 2017 DMS: 68°07’47’’S 67°06’10’’W // COMNAP 2024 DDM: 68° 7.818' S 67° 6.1759' W // COMNAP 2017 permafrost: None |
| Sources | COMNAP Facilities CSV (Nov 2024) ; COMNAP Station Catalog (Aug 2017) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) ; Wikipedia: Historic Sites and Monuments in Antarctica ; SCAR Composite Gazetteer (placenames.aq) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -68.1303, -67.1029 confirmed (COMNAP exact; aidca and Wikipedia within about 100 m). Army page "67°08'W" is about 1 km west (rounded or wrong). Elevation 4 to 5 m | COMNAP rec. 16; 2026-10-04 |
| Surface verified (rock / ice / other) | **Rock-cored island (qualified).** Barry Island, "in the center of" the Debenham Islands, "islands and rocks" in Marguerite Bay; BGLE hut stood here in 1936 to 37 and the Argentine base is on the same site; wooden buildings on about 0.2 km2 with concrete fuel hardstand. **No geology of Barry Island itself found**; regional exposures are plutonic and volcanic | SCAR gazetteer; 1993 report; 2026-10-04 |
| Ice velocity (m/yr) | Not found. Mainland glaciers (Northeast, McClary, Uspallata) lie a few km east; calved ice accumulated at the base shoreline in Apr 2023; no velocity data located | elciudadanoweb 2023; dead end |
| Ice thickness (m) | Not found. Sea ice (not glacier ice) is the local factor: freezes June to November, average 1.2 m, "notoriously unstable" in embayments | Army page; summary only |
| Bed elevation (m) | Not found | dead end |
| Depth to bedrock below surface (m) | Not found | dead end |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **QUALIFIES (qualified).** About 75% it is rock or rock-cored, not ice; no ice flow through the site reported; Stonington Island 7.3 km SE was once joined to the mainland by an ice ramp, now separated by glacier retreat. Low confidence on rock type and bedrock depth | Log; 2026-10-04 |
| Status verified (year-round / summer / closed / abandoned) | Year-round, open (continuous wintering of 19 to 23: 20 in Mar 2025, 19 incoming Mar 2026). Closed 28 Feb 1960 to 1973/75/76 (sources disagree), reopened | COMNAP; argentina.gob.ar 2025; gacetamarinera 2026 (summary) |
| Year opened / year closed, verified | Founded 21 Mar 1951 (Col. Hernán Pujato; first continental Argentine base); **fires 30 Jun 1952 (destroyed the main house, power plant and radio station), 1958, 1959**; evacuated 28 Feb 1960; reopened 1973 (SCAR UK), 1975 (1993 report) or 21 Mar 1976 (Army); main accommodation 1982. **No 2008 fire found** (see notes) | Log; Cancillería; 1993 report |
| Capacity: winter / summer (persons) | Peak 21 (COMNAP); 1993 maximum 20, all personnel winter over (no summer-only), one-year tour; recent reliefs 19 to 23. Typical winter-over about 20 | COMNAP; 1993 report |
| Buildings and infrastructure: state, power, water | 1993: seven timber/metal-clad buildings; water by melting snow/ice plus a reverse-osmosis plant (1,400 L/day); three 25 kW Deutz diesels, 45 to 50,000 L/yr (2023: about 130,000 L/yr), 10,000 L bladder tanks on a concrete pad (steel tanks then planned); surgery and doctor; trucks, Muskeg, snowmobiles; LASAN lab (geomagnetism, ionosphere, phytoplankton, geodesy, glaciology, botany). New labs planned 2023 to 24; completion not confirmed | 1993 report; elciudadanoweb; Army page |
| Landing/harbor/airstrip access | No jetty (beach landing, three inflatables); helicopter pad (about 70 movements/yr 1993). Twin Otter uses Uspallata Glacier about 11 km east (blog/Wikipedia only) and winter sea ice can serve as a runway | 1993 report; blog; unverified primary |
| Reachability from nearest city and highway (route, season) | Marguerite Bay is "closed by ice most of the year"; annual resupply by the icebreaker Almirante Irízar in Feb to Mar (3 days from the Drake), then Sea King helicopters and boats; weather delays common; 1952 to 53 relief blocked by sea ice (air drop). Nearest city Rothera 75.7 km (air or sea); Hwy 1 nearest per inventory | Cancillería; 2023 to 2026 relief reports |
| Other facilities within 25 km | Stonington Island 7.3 km SE: East Base (HSM 55) and Base E (HSM 64), both closed, plus a 1956 Chilean refuge; Ona refuge 4.5 km, active; 17 de Agosto refuge active; other refuge positions unverified. Beyond 25: Turkish camp (Horseshoe) 33.9 km seasonal; Rothera 75.7; Carvajal 86 | SCAR gazetteer; Wikipedia lead; IBA 2015 |

**Notes / dead ends / open questions:**

**Verdict: qualifies (qualified).** The 2008 "fire/damage" in the brief is **not supported by any source** after 8+ searches; documented fires are 1952, 1958, 1959. Likely origin of the association (agent's inference, unsourced): the Almirante Irízar burned 10 Apr 2007 and was out of service until 2017, disrupting resupply of all Argentine bases in 2007/08 and 2008/09. Sea-ice dependence of access is the main practical risk (one icebreaker per year). Climate: annual mean -3 to -6 °C (tutiempo; Spanish Wikipedia -5.1 °C), precipitation 500 to 676 mm, wind over 200 km/h cited repeatedly; the English "winter average -37 °C" conflicts. No ASPA/ASMA at the station. Stated purpose: science (geomagnetism, ionosphere, VLF), strategic control of the central Peninsula. Open: Barry Island geology; glacier velocities; current ATS inspection reports (only the 1993 UK/Italy/Korea joint report was read). Full log: `Research_Logs/Batch1_A1_ArturoPrat_SanMartin_2026-10-04.md`.

### 8. Vernadsky  `vernadsky`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | Vernadsky Research station / Faraday-Station / Faraday / Vernadsky Station / Faraday Station / Base F / Argentine Islands / Akademik Vernadsky Station / Estação Akademik Vernadsky / Wiernadski / base antarctique Akademik-Vernadsky / Base Vernadski / Wernadski-Station / Vernadskij |
| Coordinates (lat, lon) | -65.245743, -64.257481  *(source: comnap24)* |
| Largest source disagreement | 0.6 km |
| Elevation (m) | 7  *(source: comnap24)* |
| Type / detail | station / comnap24:Station / comnap17:Station / wikidata:Antarctic research station / wikidata:Antarctic research station / wp_list:Permanent / scar:Station |
| Status | year-round  *(COMNAP 2024: Year-Round, Open)* |
| Status across sources | comnap24: COMNAP 2024: Year-Round, Open // comnap17: COMNAP 2017: operational period "Year-round" // wp_list: Wikipedia list: permanent active |
| Years opened / closed | 1996 / n/a (active) |
| Capacity (winter / summer / peak) | 5 / 10 / 24 |
| Operator (context only) | Ukraine - National Antarctic Scientific Center of Ukraine ; United Kingdom - British Antarctic Survey |
| Purpose as stated | science disciplines: Climatology, Geology, Geophysics, GIS, Marine biology, Medicine, Microbiology, Oceanography, Terrestrial biology |
| Surface | bare rock |
| Stability flag (sources only) | rock |
| Location text | Galindez Island |
| Nearest city | Palmer City, 54.2 km (NEAR_CITY) |
| Nearest highway | hwy1, 27 km  *(lines good to about ±20 km)* |
| Inventory notes | Also in wikidata (not a separate row): "Argentine Island Magnetic Observatory" [magnetic observatory] at -65.2500,-64.2667 // Also in wikidata (not a separate row): "St. Volodymyr Chapel" [church building] at -65.2457,-64.2575 // COMNAP 2017 DMS: 65°14’44.7’’S 64°15’26.9’’W // COMNAP 2024 DDM: 65° 14.7446' S 64° 15.4489' W // Wikipedia inactive-list row at the same site: "Faraday" (Closed, became Vernadsky, est 1947, closed 1996) // Wikipedia list has 2 rows merged here: Vernadsky (permanent_active 1994-); Faraday (Closed, became Vernadsky 1947-1996) // COMNAP region: Antarctic Peninsula // COMNAP 2017 permafrost: Continuous |
| Sources | COMNAP Facilities CSV (Nov 2024) ; COMNAP Station Catalog (Aug 2017) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) ; SCAR Composite Gazetteer (placenames.aq) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -65.2457, -64.2575 confirmed (COMNAP 2024; Wikipedia 17 m off; the 2017 Ukrainian sheet's "65°14'74.5''" is a formatting error that matches 65°14.745' in decimal minutes). Elevation 7 m. NW tip of Galindez Island (Marina Point) | COMNAP; Ukraine 2017 sheet; 2026-10-04 |
| Surface verified (rock / ice / other) | **Rock, high confidence.** COMNAP "Ice-free ground"; 2021 works drilled over 100 holes in volcanic rock for grounding and piles; buildings on rock foundations. Regional bedrock: Antarctic Peninsula Volcanic Group andesite/pyroclastics, Paleocene plutons (Galindez lithology not confirmed in a fetched primary source) | COMNAP; NASC Ukraine 2021; GJI paper |
| Ice velocity (m/yr) | **Station not on ice.** Relict ice cap about 400 m square south of a 50 m rock peak (Woozle Hill); Thomas (1963): movement "negligible except in the ice adjacent to the southern ice cliffs"; fringe 60 to 80 m inland moved about 0.65 to 1.08 m/yr (stakes 5 to 108 cm over measured periods), ice cap in equilibrium 1960 to 62. Station-to-cliff distance not measured | Thomas 1963 BAS Bull. 2:27 to 43 (OCR); 2026-10-04 |
| Ice thickness (m) | Ice cap up to about 35 m (35.3 m, Galindez); ice caps cover about 50% of the Argentine Islands' land | Antarctic Science 2019; Ukrainian Antarctic Journal |
| Bed elevation (m) | Not found (rock at the station) | n/a |
| Depth to bedrock below surface (m) | At/near surface (piles drilled into volcanic rock). Permafrost "Continuous" (COMNAP); no Galindez borehole study opened | NASC Ukraine 2021 |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **QUALIFIES (high).** Not threatened by ice motion. Hazards: a 20 m by 5 m piece of the Woozle Hill glacier edge collapsed near the station (date not established; snippet only); snow load (2.2 m in Aug 2022, drifts to 5 m; 3 m event Dec 2021); a 1946 sea surge (possible tsunami) swept away the Winter Island hut | NASC; babel.ua 2022; Wordie House guide |
| Status verified (year-round / summer / closed / abandoned) | Year-round, open. Winter teams 12 to 14 (13 in 2025/26, 14 in 2026/27 per summaries); rotation each March (31st expedition arrived 3 Mar 2026) | COMNAP; NASC 2026 |
| Year opened / year closed, verified | Site history: BGLE hut (Winter Island) 1935/36; Wordie House 1947 (Winter Island); moved to Galindez May 1954 (Base F, "Coronation House"); Faraday 1977; Ukraine took over by notes of 20 Jul 1995, flag change 6 Feb 1996 (symbolic price £1). COMNAP year 1996. Major rebuilds 1979/80, 2021 to 2025 (cracked 50-year-old concrete at the fuel store, rotted timber) | NASC history; Wikipedia lead; NASC 2025 |
| Capacity: winter / summer (persons) | Max 24, 24 beds; summer 10 staff + 20 scientists; winter 5 + 7; typical wintering team 12 to 14 | COMNAP 2017 Ukraine sheet; NASC |
| Buildings and infrastructure: state, power, water | 1,150 m2 under roof, 385 m2 logistics, 180 m2 labs; 12 structures (main building, two non-magnetic modules, upper-air hall, workshops, VLF hut, emergency base, chapel); three 100 kVA Volvo-Penta diesels (one runs) + 10 kW emergency; seawater reverse-osmosis plant; fuel store rebuilt 2025; 1-bed hospital with X-ray; pier; boats; crane (second planned); solar/wind-powered camera at Woozle Hill | COMNAP; NASC 2021, 2025 |
| Landing/harbor/airstrip access | Pier, but the ship Noosfera cannot reach it (seabed): cargo (about 50 t) and people move by motorboat. **No airstrip, no helipad, 0 flights** | NASC 2026; COMNAP |
| Reachability from nearest city and highway (route, season) | Punta Arenas about 3.5 days by Noosfera; about 40 ship visits/yr, mostly tourist (Dec to Mar; 2,000 to 5,000 visitors a season); winter small-boat travel limited by sea ice (Aug 2024 ice out to 100 km; 2025 no stable ice formed); three Faraday men died in Aug 1982 when a storm broke the sea ice on a Petermann crossing. Nearest city Palmer City 53.3 km (Yelcho, Chile, 51.9 km) | NASC; texty.org.ua 2024; Antarctic Monument Trust |
| Other facilities within 25 km | Wordie House (UK, HSM 62, Winter Island) about 0.4 km, emergency refuge; Rasmussen Hut about 8 to 9 km (emergency refuge); Groussac Refuge (Argentina, Petermann Island) about 9.6 km, seasonal; ASPA 108 (Green Island) 8 to 9 km. No "Kyiv" refuge found. No other station within 25 km | NASC; UKAHT; ASPA 108 plan |

**Notes / dead ends / open questions:**

**Verdict: qualifies, high.** Stated purpose: meteorology, ionosphere, geomagnetism, ozone (Dobson since the 1985 Farman et al. discovery work), seismology, glaciology, biology; Faraday/Vernadsky temperature trend about +0.56 °C/decade (1951 to 2004; Turner 2005, secondary summaries only). Climate: annual mean about -3.3 to -3.8 °C (COMNAP's sign is missing), July about -7 to -8.7 °C, 530 mm, mean wind 15 km/h, max 144 km/h. Heritage: HSM 62 Wordie House (visitor cap 10 to 12 inside). Also a heavy tourist stop (the "Faraday Bar", Wordie House). Open: Woozle Hill collapse date; Galindez borehole data (Savenets 2020 not opened); Thomas/2019 radar papers for station-to-ice-edge distance. Full log: `Research_Logs/Batch1_A1_Orcadas_Vernadsky_2026-10-04.md`.


---

## Tier A2: Active, summer-only

### 9. Decepcion  `decepcion`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | Decepción Base / Deception / Base Antártica Decepción / Decepcion Antartic Base / Deception Base / Base Decepción / Decepción-Station / Stazione Decepción |
| Coordinates (lat, lon) | -62.976760, -60.700695  *(source: comnap24)* |
| Largest source disagreement | 0.2 km |
| Elevation (m) | 7  *(source: comnap24)* |
| Type / detail | station / comnap24:Station / comnap17:Station / wikidata:Antarctic research station |
| Status | summer-only  *(COMNAP 2024: Seasonal, Open)* |
| Status across sources | comnap24: COMNAP 2024: Seasonal, Open // comnap17: COMNAP 2017: operational period "October–March" // wp_list: Wikipedia list: summer-only active |
| Years opened / closed | 1948 / n/a (active) |
| Capacity (winter / summer / peak) | unknown / 18 / 36 |
| Operator (context only) | Argentina - Instituto Antartico Argentino ; Argentine Antarctic Institute |
| Purpose as stated | science disciplines: Geology, Geomorphology, Volcanology |
| Surface | bare rock |
| Stability flag (sources only) | rock |
| Location text | Deception Island |
| Nearest city | Pergamino, 39.8 km (NEAR_CITY) |
| Nearest highway | hwy1, 136 km  *(lines good to about ±20 km)* |
| Inventory notes | COMNAP 2017 DMS: 62°58’36.3’’S 60°42’02.5’’W // COMNAP 2024 DDM: 62° 58.6056' S 60° 42.0417' W // COMNAP 2017 permafrost: Discontinuous |
| Sources | COMNAP Facilities CSV (Nov 2024) ; COMNAP Station Catalog (Aug 2017) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -62.9768, -60.7007 confirmed (COMNAP; COMNAP 2017 same in DMS; ASMA 4 text 62°58'20"S 60°41'40"W, 0.6 km off; Wikipedia 0.22 km off). Elevation 7 m (COMNAP only). Fumarole Bay (Argentine "Bahía Primero de Mayo"), SW shore of Port Foster | COMNAP; ASMA 4 plan; SCAR gazetteer |
| Surface verified (rock / ice / other) | **Pyroclastic ground, not bedrock:** ash, scoria and lapilli beach and plain material (COMNAP: "Ice-free ground", discontinuous permafrost, features "volcanic caldera, terrestrial geothermal"). About 57% of the island is permanent (often ash-covered) glacier, but the stations are on the SW shore outside the glaciated zones | COMNAP 2017 p.14; ASMA 4 (2005, 2019 plans); Spanish Army posters |
| Ice velocity (m/yr) | No source reports ice moving toward or through the station; no velocity data found | dead end |
| Ice thickness (m) | n/a | n/a |
| Bed elevation (m) | n/a | n/a |
| Depth to bedrock below surface (m) | Not found. Shoreline erosion on Port Foster cliffs 0.3 to 2 m/yr outside eruption-affected areas; the SW coast "from the beach in front of Decepcion to Punta Colatinas" is receding | Torrecillas 2024 Remote Sensing 16:512; Spanish Army poster |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **UNCLEAR, leaning fail for a permanent settlement.** The ice test passes; the ground is volcanic ash in a restless caldera with eruptions in 1967 and 1969 that destroyed neighboring stations: Deception is an active basaltic volcano, a "restless caldera with a significant volcanic risk" (ASMA 4). Eruptions: about 1906 to 10; 4 Dec 1967 (Argentine station evacuated days before; Chilean Aguirre Cerda destroyed); 21 Feb 1969 (Chilean and British bases destroyed; thin ash on Decepcion, unharmed); unrest 1991/92 (up to 900 earthquakes, a probable small intrusion in Fumarole Bay), 1999, and 2014/15 (yellow alert 17 Feb 2015; Gabriel de Castilla closed 24 Feb 2015). 2019 plan: NE horizontal motion about 2 cm/yr, subsidence about 6 mm/yr; Caliente Hill 80 to 100 °C at 10 to 40 cm depth. Alert GREEN throughout 2023/24 and on 1 Mar 2026 (last reading; stations closed in winter). Escape from the caldera takes 2 to 4+ hours on foot. Areas 7 to 10 km from the eruption centre "could be relatively safe" | ASMA 4 plans [V]; ATCM46 IP179; Antarctic J. US 1969 |
| Status verified (year-round / summer / closed / abandoned) | Seasonal (Oct to Mar per COMNAP); **summer-only since December 1967**; nobody winters (the 2017 catalogue and Wikipedia list 3 winter persons: conflicts with the 2025/26 closure record). 2023/24: 19 Jan to 23 Mar; 2025/26: closed 26 Feb 2026 | COMNAP 2017; ATCM46 IP179; Spanish Army diary 2026 |
| Year opened / year closed, verified | Opened 25 Jan 1948 as a naval detachment ("operational since 1947" in one paper); seismograph and ionospheric station 1951; volcanological observatory 1993; no rebuild found | COMNAP 2017; Abella 2025 |
| Capacity: winter / summer (persons) | 0 winter / 30 beds, max 36, summer staff 18, 1,030 m2 under roof; COMNAP peak 36 (Argentine primary documents not found) | COMNAP 2017 |
| Buildings and infrastructure: state, power, water | Own generator (fossil fuel, 220 V, 24 h); fresh water from a small lake west of Crater Lake inside the Facilities Zone, shared with Gabriel de Castilla; secondary fuel containment; sat phone + VHF; workshops; 2 Zodiacs; helipad: COMNAP "No" but the ASMA 4 plan says helicopters land at "the helipad at Decepcion Station" | COMNAP 2017; ASMA 4 (2019) |
| Landing/harbor/airstrip access | No airstrip, no pier ("ship landing facilities: None"); entry to Port Foster through Neptune's Bellows (about 500 m wide, shallow, Ravn Rock mid-channel); icebreaker Irízar with Sea King helicopters | COMNAP 2017; ASMA 4 |
| Reachability from nearest city and highway (route, season) | Ship (6 visits/yr) and helicopter; nearest city Pergamino 40 km. Juan Carlos I (Livingston) 38 km | COMNAP; computed |
| Other facilities within 25 km | Gabriel de Castilla 1.26 km (same Facilities Zone); Whalers Bay about 7 km (Hektor whaling station 1912 to 1931 and British Base B 1944 to 1969, both destroyed by the 1969 lahar; HSM 71); Pendulum Cove about 6.9 km (Chilean Aguirre Cerda, 1955 to 1967/69, HSM 76; derelict hut 1 km SW) | ASMA 4 plans; SCAR |

**Notes / dead ends / open questions:**

**Verdict: the island is the problem, not the ice.** ASMA 4 (98.5 km2; Facilities Zone = both stations, the beach and the freshwater lake; neighboring ASPA 140 sites B, C, D and ASPA 145): an EIA is required for new permanent buildings; no vehicles or camping for non-scientific visitors; fuel-spill risk in the enclosed caldera is under discussion. Tourism about 45,000 passenger landings in 2023/24, mostly at Whalers Bay and Telefon Bay. Stated purpose: geology and volcanology, meteorology from the start, long-term seismic and biological datasets. Climate: mean annual -3 °C, mean wind 22.3 km/h SW, 407 mm. Monitoring: Spain's IGN (7 seismic, 6 GNSS stations, thermometry, camera) and Argentina's SEGEMAR/OAVV (3 seismic, 2 GNSS since March 2023); two SEGEMAR stations lost solar panels to a late-Dec 2023 storm. **Inventory fix: Gabriel de Castilla is NOT at Pendulum Cove** (that is the Chilean ruin 6 km away). Open: current alert after 1 Mar 2026, bedrock depth, Argentine EIA. Full log: `Research_Logs/Batch1_A2_Decepcion_GdC_Shirreff_Maldonado_Risopatron_2026-10-04.md`.

### 10. Druzhnaya IV  `druzhnaya-iv`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | Druzhnaya-4 / Druzhnaya 4 Station / Base Družnaja 4 / Drużnaja 4 / Base Druznaya 4 / Stazione Druzhnaya 4 / Base Druzhnaya 4 |
| Coordinates (lat, lon) | -69.747827, 73.709214  *(source: comnap24)* |
| Largest source disagreement | 1.7 km |
| Elevation (m) | 20  *(source: comnap24)* |
| Type / detail | station / comnap24:Station / comnap17:Station / wikidata:Antarctic research station / wp_list:Summer / scar:Station |
| Status | summer-only  *(COMNAP 2024: Seasonal, Open)* |
| Status across sources | comnap24: COMNAP 2024: Seasonal, Open // comnap17: COMNAP 2017: operational period "October–March" |
| Years opened / closed | unknown / n/a (active) |
| Capacity (winter / summer / peak) | unknown / 50 / 50 |
| Operator (context only) | Russia - Russian Antarctic Expedition ; Arctic and Antarctic Research Institute |
| Purpose as stated | science disciplines: Environmental sciences, Geodesy, Geology, Geophysics |
| Surface | bare rock |
| Stability flag (sources only) | rock |
| Location text | Princess Elizabeth Land |
| Nearest city | Shirayuki, 103.5 km (CANDIDATE) |
| Nearest highway | hwy22, 69 km  *(lines good to about ±20 km)* |
| Inventory notes | COMNAP 2017 DMS: 69°44’00’’S 73°43’00’’E // COMNAP 2024 DDM: 69° 44.8696' S 73° 42.5528' E // Wikipedia inactive-list row at the same site: "Druzhnaya IV" (Closed, est 1987, closed 2013) // COMNAP 2017 permafrost: Continuous |
| Sources | COMNAP Facilities CSV (Nov 2024) ; COMNAP Station Catalog (Aug 2017) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) ; SCAR Composite Gazetteer (placenames.aq) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -69.7478, 73.7092 confirmed (COMNAP; SCAR gazetteer Landing Bluff 69°44'32.1"S 73°42'36.9"E, 0.6 km off, summit 119 m). AARI's "72°42'E" and the 2010 Australian "59°44'S" are typos. **On Landing Bluff, a rock nunatak at Sandefjord Bay on the NE edge of the Amery Ice Shelf; NOT in the Prince Charles Mountains and NOT at Beaver Lake.** Elevation 20 m | COMNAP; SCAR (AADC); AARI Wayback 2016 |
| Surface verified (rock / ice / other) | **Rock mass** (AARI "nunatak Lending"): steep eastern slope and small outcrops to the SW; COMNAP "ice-free ground", features ice shelf, nunatak, rock; the shore has "difficult dissected glacial relief" with an ice barrier no higher than 6 m | AARI; COMNAP 2017 |
| Ice velocity (m/yr) | **ITS_LIVE (agent's computation): about 2 m/yr at the station pixel, a rock patch about 1 km across at 1 to 3 m/yr;** median 13.6 m/yr within 2 km; surrounding glacier ice 10 to 57 m/yr; Amery shelf margin about 40 to 50 m/yr to the east | Log (S15) |
| Ice thickness (m) | Not found | dead end |
| Bed elevation (m) | Not found | dead end |
| Depth to bedrock below surface (m) | At the surface (nunatak); not measured | Log |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **QUALIFIES (moderate-high).** Hazards: landfast ice 160 to 180 cm usually breaking out late Jan to early Feb; clear weather only about 10 to 12 days a month | AARI |
| Status verified (year-round / summer / closed / abandoned) | **Probably mothballed with an automatic weather station.** COMNAP "Seasonal, Open" and AARI 70th/71st RAE announcements list it as a seasonal base; 15 Jan 2025 "unscheduled technical maintenance of the automatic weather station Druzhnaya-4"; **no source confirms anyone occupying the base after about 2015** | COMNAP; AARI 2025 |
| Year opened / year closed, verified | Opened 1 Jan 1987; five summers 1987 to 91; conserved 24 Mar 1991; reopened 6 Feb 1994; geological/geophysical work from the 48th RAE (2003) through the 60th; Russian Wikipedia (secondary): conserved 13 Mar 2013, again 14 Apr 2014, deconserved 8 Jan 2015, conserved from 1 Mar 2015 | AARI Wayback 2016; ru.wikipedia (lead) |
| Capacity: winter / summer (persons) | 0 winter / 50 beds (COMNAP 2017; no showers or laundry; 78 kW diesel; 120 t oil tank); 2010: 16 small wooden structures, 8 present plus 12 at outlying camps | COMNAP; Aus. 2010 (ATCM34 IP39) |
| Buildings and infrastructure: state, power, water | Temporary panel and wooden huts (generator, kitchen/mess, communications), diesel with 200 L drums (empty drums were being dug out of a gully in 2010; "400 drums pressed" unverified), untreated sewage to sea, automatic met and geodetic stations; sat phone + VHF | Aus. 2010; COMNAP 2017 |
| Landing/harbor/airstrip access | COMNAP: 0 airstrips, no helipad; 1980s aerogeophysics (Il-14, An-2) used "ice airfields of Soyuz, Druzhnaya-4 and Progress"; 2010: ship and helicopter via Sandefjord Bay or Progress II (about 100 km) | COMNAP 2017; PMGRE |
| Reachability from nearest city and highway (route, season) | Ship (2 visits/yr) and helicopter; nearest city Shirayuki about 104 km; Progress 112 km | COMNAP; computed |
| Other facilities within 25 km | None found. Nearest: Bharati 104 km, Law Base 112 km, Zhongshan 112 km, Progress 112 km; Soyuz 208 km; Larsemann Hills ASMA 6 about 100 km | COMNAP; computed |

**Notes / dead ends / open questions:**

**Verdict: qualifies on rock; small, temporary, relocatable huts; effectively mothballed.** Revival realism: already deconserved twice (1994, 2015); huts are seasonal; no runway or helipad. Stated purpose: logistics hub for geological and geophysical work in Mac. Robertson and Princess Elizabeth Lands, the Prince Charles Mountains and Ingrid Christensen Coast oases. Inspected by Australia 13 Jan 2010 (judged appropriate to its scale). Inventory note: the "Druzhnaya III" rows are different places (one near Cape Norvegia, 71°06'S 10°49'W, closed 1991). Full log: `Research_Logs/Batch1_A2_B2_Molodezhnaya_MtVechernyaya_DruzhnayaIV_Soyuz_SarieMarais_2026-10-04.md`.

### 11. Gabriel de Castilla Station  `gabriel-de-castilla-station`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | Gabriel de Castilla / Gabriel de Castilla Spanish Antarctic Station / Estação Antártica Espanhola Gabriel de Castilla / base antarctique Gabriel de Castilla / Base Antártica Gabriel de Castilla / Base antartica spagnola dell'esercito Gabriel de Castilla / Gabriel-de-Castilla-Station / Base antarctique Gabriel de Castille / Base Antártica Española del Ejército de Tierra Gabriel de Castilla / Stazione de Castilla / Stazione spagnola Gabriel de Castilla / Base Gabriel de Castilla / Gabriel de Castilla, Refugio |
| Coordinates (lat, lon) | -62.977197, -60.675745  *(source: comnap24)* |
| Largest source disagreement | 33.7 km |
| Elevation (m) | 15  *(source: comnap24)* |
| Type / detail | station / comnap24:Station / comnap17:Station / wikidata:Antarctic research station / scar:Station / scar:Station |
| Status | summer-only  *(COMNAP 2024: Seasonal, Open)* |
| Status across sources | comnap24: COMNAP 2024: Seasonal, Open // comnap17: COMNAP 2017: operational period "November–March" // wp_list: Wikipedia list: summer-only active |
| Years opened / closed | 1990 / n/a (active) |
| Capacity (winter / summer / peak) | unknown / 13 / 36 |
| Operator (context only) | Spain - Spanish National Research Council ; Comite Polar Español |
| Purpose as stated | science disciplines: Atmospheric chemistry and physics, Climate change, Ecology, Environmental sciences, Geodesy, Geology, Geomorphology, Geophysics, GIS, Glaciology, Human biology, Human impact, Limnology, Mapping, [...] |
| Surface | bare rock |
| Stability flag (sources only) | rock |
| Location text | Deception Island |
| Nearest city | Pergamino, 39.3 km (NEAR_CITY) |
| Nearest highway | hwy1, 136 km  *(lines good to about ±20 km)* |
| Inventory notes | COMNAP 2017 DMS: 62°58’40’’S 60°00’30’’W // COMNAP 2024 DDM: 62° 58.6318' S 60° 40.5447' W // COMNAP region: Antarctic Peninsula // COMNAP 2017 permafrost: Discontinuous // SOURCE ANOMALY: COMNAP 2017 catalogue gives longitude 60 00 30 W; COMNAP 2024, Wikidata, Wikipedia and SCAR give about -60.68 (Deception Island). The 2017 value is about 34 km off (probable typo in the 2017 PDF). |
| Sources | COMNAP Facilities CSV (Nov 2024) ; COMNAP Station Catalog (Aug 2017) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) ; SCAR Composite Gazetteer (placenames.aq) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -62.9772, -60.6757 confirmed (COMNAP; ASMA plan 62°58'40"S 60°40'30"W, 75 m off; the 2017 Spanish catalogue prints 60°00'30"W, a typo for 60°40'30"). Elevation 15 m. **Not at Pendulum Cove** (6 km away); about 1.26 km SE of Decepcion at Fumarole Bay | COMNAP; ASMA 4; Spain 2017 catalogue |
| Surface verified (rock / ice / other) | **Volcanic material on a plain at the foot of a slope**, lapilli-sized beach material; COMNAP "Ice-free ground", discontinuous permafrost (resistivity profiles: discontinuous near the sea, more uniform on the slope, less than 1 m depth). A possible hillside landslide has a mapped head scarp, activity unknown | COMNAP; UPM/INTA/Spanish Army posters (2018) |
| Ice velocity (m/yr) | No source reports ice threatening the site | dead end |
| Ice thickness (m) | n/a | n/a |
| Bed elevation (m) | n/a | n/a |
| Depth to bedrock below surface (m) | Not found. **Documented accelerating coastal erosion:** the 2.5 to 3.5 m cliff in front of the base is receding, "especially after storms" (wave action, permafrost loss, runoff); 164-transect analysis of 2001 to 2013 imagery; UPM 2024: acceleration since 2010 with rates up to 2.5 m/yr (images 1956 to 2023); a retaining wall has been built; inland slow periglacial creep and mudflows "can reach parts of the Base causing serious deterioration" | Paredes et al. 2018; Santalices and Paredes 2024 |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **UNCLEAR, leaning fail for a permanent site** (same volcanic hazard as Decepcion, plus the erosion): the station was itself closed 24 Feb 2015 during unrest | ASMA 4 (2019) |
| Status verified (year-round / summer / closed / abandoned) | Seasonal, normally Nov to Mar; nobody winters. 2023/24: 1 Jan to 24 Mar; 2025/26: opened 29 Dec 2025, closed 20 Mar 2026 (a few days early for bad weather) | Spanish Army diary 2026; ATCM46 IP179 |
| Year opened / year closed, verified | Built late 1989, inaugurated 1990 (refuge first); formally a station 1998; Spain took over volcanic monitoring Sept 2020 | Spain 2017 catalogue; Abella 2025 |
| Capacity: winter / summer (persons) | 0 winter / 36 beds (792 m2, labs 142 m2); EU-POLARIN says 28; observed 20 (13 military + 7 scientists) at the opening and 33 on 27 Feb and 1 Mar 2026 | Spain 2017 catalogue; Spanish Army diary |
| Buildings and infrastructure: state, power, water | Living module (kitchen, bakery), seven 4-bed rooms, scientist module with 2 offices and 2 labs, containers (boats, wet lab, infirmary, freezer, workshop, stores, incinerator, three igloos); fossil fuel + renewables 220 V; water from the "Zapatilla" lake; 15 m2 medical room; Starlink, VHF, sat phone; five boats, ATVs, two telehandlers; wet-dock landing | Spain 2017 catalogue; Spanish Army diary |
| Landing/harbor/airstrip access | Wet-dock; no airstrip; research ship BIO Hespérides (Ushuaia, Livingston, Deception) and helicopter | Spain 2017 catalogue; Spanish Army diary |
| Reachability from nearest city and highway (route, season) | Hespérides via Neptune's Bellows into Port Foster; nearest city Pergamino 39 km | Spanish Army diary; inventory |
| Other facilities within 25 km | Decepcion 1.26 km; Whalers Bay about 5.8 km; Pendulum Cove about 6 km; Juan Carlos I about 38 km | ASMA 4; computed |

**Notes / dead ends / open questions:**

**Verdict: unclear, leaning fail for a permanent settlement.** Stated purpose: logistic support to scientific research and Army research (transmissions, environment, health, equipment); Spanish science on Deception (volcanology, seismology, biology, permafrost, pollution). Climate: wind max 130 km/h, mean 24 km/h, mean annual -0.7 °C; the catalogue's "23.2 mm" annual precipitation is almost certainly an error (about 500 mm island-wide). Same ASMA 4 Facilities Zone and restrictions as Decepcion. An active-layer study at Crater Lake reports thaw depth falling from about 36 cm (2006) to 23 cm (2014) (summary only). Full log: `Research_Logs/Batch1_A2_Decepcion_GdC_Shirreff_Maldonado_Risopatron_2026-10-04.md`.

### 12. Gabriel Gonzalez Videla  `gabriel-gonzalez-videla`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | González Videla Antarctic Base / González Videla / Shelter ‘Gabriel Gonzalez Videla' / Base Antártica Presidente Gabriel González Videla / Gonzalez Videla Station / Base Presidente Gabriel González Videla / González-Videla-Antarktis-Station / Base Gabriel González Videla / Gabriel-Gonzalez-Videla-Station / Base González Videla |
| Coordinates (lat, lon) | -64.823862, -62.857499  *(source: comnap24)* |
| Largest source disagreement | 0.9 km |
| Elevation (m) | 6  *(source: comnap24)* |
| Type / detail | station / comnap24:Station / comnap17:Station / wikidata:Antarctic research station |
| Status | summer-only  *(COMNAP 2024: Seasonal, Open)* |
| Status across sources | comnap24: COMNAP 2024: Seasonal, Open // comnap17: COMNAP 2017: operational period "December–April" // wp_list: Wikipedia list: summer-only active // wp_hsm: Historic Site/Monument no. 30 |
| Years opened / closed | 1951 / n/a (active) |
| Capacity (winter / summer / peak) | unknown / 11 / 15 |
| Operator (context only) | Chile - Chilean Air Force ; Instituto Antártico Chileno |
| Purpose as stated | science disciplines: Environmental science, Geology, Glaciology, Marine biology |
| Surface | bare rock |
| Stability flag (sources only) | rock |
| Location text | Waterboat Point, Graham Land |
| Nearest city | Puerto Abrigo, 29.6 km (NEAR_CITY) |
| Nearest highway | hwy1, 15 km  *(lines good to about ±20 km)* |
| Inventory notes | COMNAP 2017 DMS: 64°49’25’’S 62°51’26’’W // COMNAP 2024 DDM: 64° 49.4317' S 62° 51.4499' W // COMNAP 2017 permafrost: Discontinuous |
| Sources | COMNAP Facilities CSV (Nov 2024) ; COMNAP Station Catalog (Aug 2017) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) ; Wikipedia: Historic Sites and Monuments in Antarctica |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -64.8239, -62.8575 confirmed (COMNAP 2024; COMNAP 2017 about 31 m off; SCAR Waterboat Point -64.8167, -62.85; all within about 1 km). Elevation 6 m. Waterboat Point on a small rocky island joined to the mainland by a 50 m tidal causeway | COMNAP; SCAR gazetteer; 2012 inspection [V] |
| Surface verified (rock / ice / other) | **Rock, low-lying island (6 m).** "A small rocky island a few acres in extent", 7 buildings mostly on higher ground; COMNAP "Ice-free ground" (glacier, crevasses and permanent snowpatches nearby but not under the station). Regional bedrock: Cretaceous volcanics and Andean plutons over Trinity Peninsula Group | 2012 inspection ATCM36 att108 [V]; Birkenmajer [F] |
| Ice velocity (m/yr) | Not measured. Staff photograph the Torre Glacier annually to monitor retreat; no velocity reported | 2012 inspection [V] |
| Ice thickness (m) | n/a | n/a |
| Bed elevation (m) | n/a (rock) | n/a |
| Depth to bedrock below surface (m) | At/near surface (rocky island); not measured | 2012 inspection |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **QUALIFIES (medium-high).** No report of relocation, burial or damage by ice, erosion, landslide or fire. Hazards: early-season snow burial (helipad snow-covered 11 Dec 2012; 2023 crew dug out entrances), a tiny tidal island at 6 m, swell from calving in Paradise Harbour | 2012 inspection; Meteored 2023 [F] |
| Status verified (year-round / summer / closed / abandoned) | **Open, summer-only (Dec to Mar)** every year; COMNAP 2024 "Open". Wikipedia's "inactive" is stale. Run jointly by the Chilean Air Force (base commander) and Navy (maritime-traffic monitoring, pollution response) | COMNAP; 2012 inspection [V] |
| Year opened / year closed, verified | Established Jan 1951 (SCAR; Wikipedia 12 Mar 1951); occupied 1951 to 58; seasonal only since 1964; reopened early 1980s (COMNAP 2017) | SCAR; COMNAP 2017 |
| Capacity: winter / summer (persons) | 0 winter / 15 beds (peak 15: 11 staff + 4 scientists); 2012: 13 present, maximum 20; 2023/24: 14 (9 FACh + 5 Navy) | COMNAP; 2012 inspection; Meteored |
| Buildings and infrastructure: state, power, water | 7 buildings (main accommodation with lookout tower, generator building, fuel store, boat shed used as oil-spill store, former lab now a museum/shop), 595 m2 under roof; 2 x 75 kVA + 2 x 16 kVA generators (COMNAP lists renewables, the 2012 inspection found none); ship-supplied RO water (tanks 25, 7, 5 t); 3-tank biological sewage plant; VHF/HF/AIS/Iridium, 256 kb internet. Gaps in 2012: no fire or smoke detection, no defibrillator, small clinic with a nurse | 2012 inspection [V]; COMNAP 2017 |
| Landing/harbor/airstrip access | Station jetty for landings; helipad (snow-covered in Dec); no land vehicles; 2 Mark V zodiacs; no airstrip | 2012 inspection; Oceanites |
| Reachability from nearest city and highway (route, season) | Chilean Navy ships from Punta Arenas (30 ship visits/yr per COMNAP 2017, mostly tourist); helicopters from Eduardo Frei (casualty-evacuation hub). Nearest: Brown 8.0 km, Yelcho 34.8 km, Palmer 56.9 km. Nearest city Puerto Abrigo about 30 km | COMNAP 2017; computed |
| Other facilities within 25 km | Almirante Brown (#26) 8.0 km; Refugio Conscripto Ortiz (Argentine Navy, 1956, at Punta Beatriz near Brown); **HSM 56 (Waterboat Point hut remains; Rec. XVI-11, Chile/UK) and HSM 30 (1950 shelter, Rec. VII-9) at the station**. No other COMNAP facility within 25 km | ATS HSM list [V] |

**Notes / dead ends / open questions:**

**Verdict: qualifies. Not closed: nothing to revive.** The brief's "HSM 54" is wrong: Waterboat Point is **HSM 56** (HSM 54 is the Byrd bust at McMurdo). Operating each summer with 13 to 15 people and about 2,000 visitors a season (groups of 40 or fewer; museum and shop open). 2012 inspectors noted a "shift in focus away from science towards tourism and historic interest". Stated purpose: maritime-traffic and pollution-response base subsidiary to Fildes Maritime Station; basic met station, penguin counts, Torre Glacier photos. Climate: mean annual -6.7 °C, July -12, Feb -1.9; 915 mm; max wind 70 km/h. In the middle of a large gentoo colony. No ASPA, ASMA or visitor-site guideline for the site. Open: the fach.mil.cl pages (403); no Torre Glacier velocity. Full log: `Research_Logs/Batch1_A2_B1_Videla_Brown_Melchior_Carvajal_2026-10-04.md`.

### 13. Halley VI  `halley-vi`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | Halley Research Station / Halley / Halley Station / Halley Skiway / Halley base / Estação Halley / Halley-Station / base antarctique Halley / Base Halley / Stazione Halley / Estação de Pesquisa Halley / Halleyova výzkumná stanice / Halley Bay |
| Coordinates (lat, lon) | -75.571111, -25.473889  *(source: comnap24)* |
| Largest source disagreement | 1.0 km |
| Elevation (m) | 37  *(source: comnap24)* |
| Type / detail | station / comnap24:Station / comnap17:Station / wikidata:Antarctic research station |
| Status | summer-only  *(COMNAP 2024: Seasonal, Open)* |
| Status across sources | comnap24: COMNAP 2024: Seasonal, Open // comnap17: COMNAP 2017: operational period "Year-round" // wp_list: Wikipedia list: permanent active |
| Years opened / closed | 1956 / n/a (active) |
| Capacity (winter / summer / peak) | 13 / 52 / 52 |
| Operator (context only) | United Kingdom - British Antarctic Survey |
| Purpose as stated | science disciplines: Atmospheric chemistry and physics, Climate change, Environmental sciences, Geophysics, Upper atmospheric science |
| Surface | ice shelf |
| Stability flag (sources only) | ice_shelf_or_glacier_or_sea_ice (needs velocity test) |
| Location text | Brunt Ice Shelf |
| Nearest city | Halley, 30.3 km (NEAR_CITY) |
| Nearest highway | spur_halley, 29 km  *(lines good to about ±20 km)* |
| Inventory notes | COMNAP 2017 DMS: 75°34’24.56’’S 25°28’1.05’’W // COMNAP 2024 DDM: 75° 34.2667' S 25° 28.4333' W // COMNAP 2017 permafrost: None |
| Sources | COMNAP Facilities CSV (Nov 2024) ; COMNAP Station Catalog (Aug 2017) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | COMNAP -75.5711, -25.4739 (elevation 37 m); BAS (capture 2 Oct 2026) -75.56821, -25.50852; COMNAP 2017 75°34'24.56"S 25°28'1.05"W: the three points differ 0.3 to 1.3 km, consistent with a station drifting west at about 1.4 km/yr, so any published point is dated and nominal. The pre-2017 site Halley VI was at 75°36'S 26°12'W (about 20.6 km west; BAS says 23 km) | COMNAP; BAS; Hodgson et al. 2019 (The Cryosphere 13:545) |
| Surface verified (rock / ice / other) | **Floating Brunt Ice Shelf.** Bedmap3: floating-shelf mask in every cell of a 6 km box, ice about 120 to 125 m thick (BAS 130 to 150 m), seabed -507 m, so **about 400 m of seawater below**; nearest grounded ice 24.6 km, nearest rock over 250 km | Bedmap3 (Pritchard 2025; own point sampling); BAS |
| Ice velocity (m/yr) | **ITS_LIVE fixed-point annual: 487 (2013), 572 (2017), 661 (2019), 802 (2021), 855 (2022), 1,001 (2023), 1,417 (2024), 1,400 (2025).** GPS at the station about 450 m/yr in 2013 rising to about 900 by Jan 2023, then **1,500 m/yr in Aug 2023** after the A-81 calving ("almost double the maximum of the previous 60 years"); BAS says it has stabilised since 2024. BAS web pages still print stale values (700 and 400 m/yr) | Marsh, Luckman and Hodgson 2024 (The Cryosphere 18:705); BAS 21 May 2024; ITS_LIVE |
| Ice thickness (m) | About 120 to 150 m (sources differ: Bedmap3 120 to 125, BAS 130 and 150) | Bedmap3; BAS |
| Bed elevation (m) | Seabed about -507 m (Brunt Basin 400 to 800 m deep) | Bedmap3; Hodgson 2019 |
| Depth to bedrock below surface (m) | n/a: no bedrock; roughly 400 m of seawater under the ice | Bedmap3 |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **FAILS (high).** Floating shelf, about 1,400 m/yr; it already forced one relocation (2016/17: eight modules towed 23 km upstream of Chasm 1); three large calvings since 2021 (A-74 Feb 2021; A-81 22 Jan 2023 about 1,500 km2; A-83 20 May 2024 380 km2); the station is about 20 km behind a new, rifted ice front; the shelf may re-ground on three grounded icebergs | BAS 2017, 2023, 2024; Marsh 2024 |
| Status verified (year-round / summer / closed / abandoned) | **Summer-only since 2017** (BAS decided on 16 Jan 2017 not to winter because Halloween Crack made winter evacuation unpredictable; "for the foreseeable future"); runs autonomously through winter on a microturbine (up to 30 kW; a second installed 2023/24); summer season about late Nov to early Feb; the last overwintering was probably 2016 (inferred). **No plan to relocate again, replace or return to wintering found** ("Halley VII" returned nothing) | BAS 2017; BAS facility page; Z-fids newsletters |
| Year opened / year closed, verified | Occupied from 6, 15 or 16 Jan 1956 (sources differ); generations I (1956 to 67), II (1967 to 73), III (1973 to 83), IV (1983 to 91), V (about 1990/91 to 2011/12), VI (built 2007 to 12; officially opened 5 Feb 2013); relocation 2016/17 (13 weeks; success declared 2 Feb 2017); instruments moved 2017/18 | BAS long read 2026; SCAR gazetteer |
| Capacity: winter / summer (persons) | 0 winter / up to 52 summer (BAS "approximately 40 staff"; 2023/24 plan 40; COMNAP 2017: 52 beds, 13 winter design); open-up team 5 to 8 | BAS; COMNAP 2017; Z-fids |
| Buildings and infrastructure: state, power, water | Eight modules on hydraulic legs and skis (one red central, seven blue) plus the Drewry summer building, garage/workshop, cabooses, Clean Air Sector lab; 2,000 m2 under roof; modules raised twice in 2023/24 and "around twice as much snow as at the end of last winter" in Oct 2025 (another double raise planned); 500 m3 fuel bunkered and 250 t waste removed in 2023/24; food for 3 years; one snow skiway 1,100 by 50 m; water source not found | COMNAP 2017; Z-fids 54 to 58 |
| Landing/harbor/airstrip access | Snow skiway; ship relief only on the shelf (2023/24: MV Malik Arctica, "the first ship in 6 years"; second planned 2025/26); relief sites 15 to 20 km from the station with 12 to 25 m shelf edge; no coordinates found for "Creek 3/Creek 4" | Z-fids 54, 55, 58 |
| Reachability from nearest city and highway (route, season) | Air (Cape Town to Wolf's Fang to Halley, summer; 20 flight visits/yr) and ship relief; winter access "extremely difficult". **The project's city Halley is about 30 km away.** Nearest real facilities: Coats field station 262 km, Belgrano II 346 km | COMNAP 2017; Z-fids |
| Other facilities within 25 km | None of any nation; the abandoned pre-2017 Halley VI site about 20 km west; Halley I to IV positions 31 to 34 km (gone or buried); a GPS network (7 sensors) and ApRES radar on the shelf; Windy Bay emperor colony about 20 km | SCAR gazetteer; BAS |

**Notes / dead ends / open questions:**

**Verdict: fails on every count.** Nothing to revive: it is open every summer; the question was a return to winter operations, which BAS has not committed to. Evidence against: velocity about three times the 2013 level, three large calvings since 2021, a new rifted ice front 20 km away. Evidence for continued summer use: ship relief resumed 2023/24, a second microturbine, and the NERC RIFT-TIP project (to 1 Mar 2027). Stated purpose: atmospheric science, space weather, ozone (the hole was found here in 1985), glaciology; WMO GAW station since 2013. Climate: winter below -20 °C, extremes about -55 °C, 105 days of darkness; mean annual -20 °C (COMNAP); snow accumulation 0.9 to 1.2 m/yr. A 2014 power failure at -55 °C (Wikipedia, unverified). The Halley Bay emperor colony largely failed to breed 2016 to 2018 (summary only). Open: ATS protected-area check (JavaScript app). Full log: `Research_Logs/Batch1_A2_Halley_Jinnah_Kohnen_2026-10-04.md`.

### 14. Jinnah Antarctic Station  `jinnah-antarctic-station`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | Jinnah / JAS / Base Antártica Jinnah / Estação Antártica Jinnah / Jinnah Antarctic基地 |
| Coordinates (lat, lon) | -70.400000, 25.750000  *(source: wikidata:Q627249)* |
| Largest source disagreement | 0.0 km |
| Elevation (m) | unknown  *(source: unknown)* |
| Type / detail | station / wikidata:Antarctic research station |
| Status | summer-only  *(Wikipedia list: summer-only active)* |
| Status across sources | wp_list: Wikipedia list: summer-only active |
| Years opened / closed | 1991 / n/a (active) |
| Capacity (winter / summer / peak) | unknown / unknown / unknown |
| Operator (context only) | Pakistan - Pakistan Antarctic Programme |
| Purpose as stated | The Jinnah Antarctic Station is an Antarctic research station operated by the Pakistan Antarctic Programme |
| Surface | unknown |
| Stability flag (sources only) | unknown |
| Location text | Sør Rondane Mountains, Queen Maud Land |
| Nearest city | Utstein, 192.6 km (CANDIDATE) |
| Nearest highway | hwy7ext, 116 km  *(lines good to about ±20 km)* |
| Inventory notes | none |
| Sources | Wikidata ; Wikipedia: Research stations in Antarctica (list) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | **Unverified; the published coordinates cannot be reconciled.** Wikipedia/Wikidata 70.4°S 25.75°E (0.1° precision; Wikidata cites Wikipedia); the 1991 Pakistani Ministry text says "7024 S and 25 E ... Princess Ragnhild Coast" (about 28 km west). **Not in COMNAP (Nov 2024 or 2017), not in the SCAR gazetteer, no ATS information exchange; Pakistan is not a COMNAP member and acceded to the Treaty on 1 Mar 2012** | COMNAP; SCAR (zero hits); ATS Parties page; Pakistani Ministry text (blog copies) |
| Surface verified (rock / ice / other) | **Floating ice shelf at both candidate positions.** Bedmap3: 70.4°S 25.75°E floating, 408 m thick, seabed -391 m; 70°24'S 25°E floating, 264 m, seabed -334 m; nearest grounded ice 10 to 14 km, nearest rock 118 km. (The Iqbal weather observatory at 71.46°S 25.29°E is on rock.) "Sør Rondane Mountains" in the wording is loose: the mountains begin 170 to 190 km south | Bedmap3 (own point sampling) |
| Ice velocity (m/yr) | **ITS_LIVE annual at 70.4°S 25.75°E: 246 to 260 m/yr (2013 to 2025)**; 1 km west 265 to 305; Jinnah II point about 106; the Belgian Roi Baudouin site (1957 to 68, built on this shelf) about 66. A structure left on the surface in 1991 would have moved about 8 to 9 km seaward and been buried (the agent's arithmetic) | ITS_LIVE (own point sampling) |
| Ice thickness (m) | 264 to 408 m (the two candidate points) | Bedmap3 |
| Bed elevation (m) | Seabed -334 to -391 m | Bedmap3 |
| Depth to bedrock below surface (m) | n/a (floating shelf) | Bedmap3 |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **FAILS at the only coordinates ever published** (moderate to high on the ice classification: two independent datasets agree and both longitudes give the same result; the coordinate uncertainty is about ±11 km plus a 28 km longitude disagreement). Very low confidence on what exists today | Log |
| Status verified (year-round / summer / closed / abandoned) | **Most likely defunct or lost; no source says so directly.** Landing 15 Jan 1991; "commissioned" 25 Jan 1991 (Pakistan Maritime Museum says 18 Jan); Jinnah II 5 Jan 1992 and the Iqbal weather observatory 18 Jan 1991 (ISSRA; Wikipedia says 1992 to 93). **No independent expedition since 1993** (NIO Director General, Gulf News 25 Oct 2020: lack of funds); SCAR national reports 2007 to 10 say only "no expedition"; ISSRA Aug 2024: operations halted, stations "no longer maintained". Wikipedia's "Active" and its 2005 PAF airstrip, 2001 Badr-B link and 2010 expansion are unsourced and contradicted | Gulf News 2020; SCAR reports; ISSRA 2024 |
| Year opened / year closed, verified | First expedition left Karachi 12 Dec 1990 on the chartered Swedish MV Columbialand (about 40 people from NIO, Navy and Army; reconnaissance of nearly 1,000 miles of coast); station commissioned Jan 1991; last expedition 1993 | Pakistani Ministry text; Pakistan Maritime Museum |
| Capacity: winter / summer (persons) | 1991 station: three prefab laboratory huts, three prefab igloos "for accommodation of 9 persons", four tents, plus an unmanned weather station. Nothing later | Pakistani Ministry text (blog copies) |
| Buildings and infrastructure: state, power, water | Not found for the 1991 station (power, water, fuel, communications, runway) | dead end |
| Landing/harbor/airstrip access | 1991: by sea on MV Columbialand (ISSRA also credits PAF aircraft and PNS Tariq/Behr Paima). Now: no Pakistani logistics; NIO says joining other nations' expeditions is more feasible | ISSRA; Gulf News |
| Reachability from nearest city and highway (route, season) | n/a. Nearest city Utstein about 193 km; Roi Baudouin (Belgian, 1957 to 68) about 54 km | computed |
| Other facilities within 25 km | None known. From the Wikipedia point: Roi Baudouin site about 54 km, Jinnah II 53 km, Iqbal Observatory 119 km, Asuka 139 km, Princess Elisabeth 193 km; the 70°24'S 25°E variant is about 26 km from the Roi Baudouin site | computed |

**Notes / dead ends / open questions:**

**Verdict: not a revivable station. Recommend dropping #14 from Batch 1** (developer decision): nothing in any primary register, no evidence of use after 1993, the published position is on a moving floating shelf, and a revival "would have to be a new station at a new site, not the 1991 one". Stated purpose: multidisciplinary research and a "permanent base" aspiration; scientific presence and SCAR membership. Contradictions: region given as Sør Rondane, Princess Ragnhild Coast or (ISSRA) Schirmacher Oasis (which is at about 11.7°E, inconsistent with every coordinate); treaty accession 2011 vs 2012. Full log: `Research_Logs/Batch1_A2_Halley_Jinnah_Kohnen_2026-10-04.md`.

### 15. Johann Gregor Mendel Czech Antarctic Station  `johann-gregor-mendel-czech-antarctic-station`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | J.G. Mendel Czech Antarctic Station / Mendel / Johann Gregor Mendel / Ceska vedecka stanice Johanna Gregora Mendela / Mendel Polar Station / Stazione polare Mendel / Estación polar Mendel / Estação Polar Mendel / Mendel-Polarstation / Polární stanice Johann Gregor Mendel / Stanice J.G.M. / Mendelova polární stanice |
| Coordinates (lat, lon) | -63.800625, -57.882592  *(source: comnap24)* |
| Largest source disagreement | 0.0 km |
| Elevation (m) | 10  *(source: comnap24)* |
| Type / detail | station / comnap24:Station / comnap17:Station / wikidata:Antarctic research station |
| Status | summer-only  *(COMNAP 2024: Seasonal, Open)* |
| Status across sources | comnap24: COMNAP 2024: Seasonal, Open // comnap17: COMNAP 2017: operational period "December–March" // wp_list: Wikipedia list: summer-only active |
| Years opened / closed | 2006 / n/a (active) |
| Capacity (winter / summer / peak) | unknown / 4 / 20 |
| Operator (context only) | Czech Republic - Masaryk University |
| Purpose as stated | science disciplines: Atmospheric chemistry and physics, Botany, Climate change, Climatology, Ecology, Geocryology, Geodesy, Geology, Geomorphology, GIS, Glaciology, Human biology, Hydrology, Isotopic chemistry, [...] |
| Surface | bare rock |
| Stability flag (sources only) | rock |
| Location text | James Ross Island |
| Nearest city | Esperanza, 62.9 km (NEAR_CITY) |
| Nearest highway | hwy1, 14 km  *(lines good to about ±20 km)* |
| Inventory notes | COMNAP 2017 DMS: 63°48’02.3’’S 57°52’57.3’’W // COMNAP 2024 DDM: 63° 48.0375' S 57° 52.9555' W // COMNAP 2017 permafrost: Continuous |
| Sources | COMNAP Facilities CSV (Nov 2024) ; COMNAP Station Catalog (Aug 2017) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -63.8006, -57.8826 confirmed (COMNAP exact; GTN-P borehole 80 m off; 2017 inspection report about 0.4 km off; the COMNAP 2017 catalogue's "57°52'95.6''" is an impossible-seconds typo). Elevation 9 to 10 m, 100 m from the shore | COMNAP; GTN-P; Prošek 2013 |
| Surface verified (rock / ice / other) | **Raised marine terrace of compacted fine sandy sediment over continuous permafrost** (not bare rock): "firm, well drained and level" (2005 inspectors); foundation is a grate of oak railway sleepers in shallow grooves, not piles. Adjacent bedrock: weakly lithified Cretaceous muddy sandstone (Whisky Bay Formation) | Prošek 2013; ATCM28 att270; Hrbáček 2019 |
| Ice velocity (m/yr) | Not on or near moving ice. Nearest ice cap Davies Dome about 12.3 km away, retreating, on a different coast; four monitored glaciers within 15 km move about 2 to 3 m/yr (secondary source). Ulu Peninsula is over 300 km2 of deglaciated ground (deglaciation began about 12.9 ka) | Hrbáček 2019; amerisurv (secondary) |
| Ice thickness (m) | n/a at the site | n/a |
| Bed elevation (m) | Not found | dead end |
| Depth to bedrock below surface (m) | **Not found.** Permafrost continuous, active layer 0.5 to 1.0 m (about 55 to 60 cm at the terrace in late January, summary only); mean annual air -6.9 °C (2011 to 2017), ground -5.5 °C at 5 cm | COMNAP 2017 Czech sheet; Hrbáček 2019 |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **QUALIFIES (moderate-high).** Not on moving ice; 2017 inspection found the buildings "in very good condition" after 10 years; no relocation, damage, flooding or erosion found. Weak point: sand over permafrost rather than bedrock; periglacial processes limit geodetic point stability on Ulu Peninsula (a local reference point was stable) | ATCM40 att043; Stachoň 2014 (summary) |
| Status verified (year-round / summer / closed / abandoned) | Seasonal, open (January to mid-March per the program; December to March per COMNAP). **No wintering ever.** Summer expeditions every year since 2006; the 20th ran January to March 2026 (26 people) | COMNAP; carp.sci.muni.cz; Masaryk Univ. 2026 |
| Year opened / year closed, verified | Built in two seasons 2004/05 and 2005/06 (construction ended 4 Mar 2006); inaugurated 27 Feb 2007 (Wikipedia 22 Feb); COMNAP year 2006. No rebuild, move or closure | Masaryk brochure; ATCM40 att043 |
| Capacity: winter / summer (persons) | 0 winter / 20 beds (peak 20: 4 staff + 16 scientists); the 2017 inspection was told the maximum is 29 (17 present); 2005 design target was 15 | COMNAP; ATCM40 att043 |
| Buildings and infrastructure: state, power, water | Main building 26.5 x 11.5 m (sandwich panels), 2 labs (33 m2), 9 or 10 converted 20-ft containers on a 400 m2 footprint. Power: eight 1.5 kW wind turbines + solar + diesel (renewables about 75% of consumption per the inspection), Ni-Cd battery bank. Water from a nearby snowmelt stream (may freeze late Feb to early Mar), about 30 L/person/day. Fuel 25 drums diesel + 5 petrol (2017). Marine incinerator; effluent pumped to sea untreated. 9 m2 medical room; Iridium, HF/VHF, Inmarsat | Prošek 2013; ATCM40 att043 |
| Landing/harbor/airstrip access | **No airstrip, no pier.** Cargo over the beach by landing craft and Zodiac up a 15 to 20 degree, 150 m unloading slope; helipad: COMNAP says yes, the inspection says only a natural gravel area | ATCM40 att043 |
| Reachability from nearest city and highway (route, season) | Annual resupply by a Chilean Navy ship from Punta Arenas (early in the season); personnel by Hercules to King George Island then a Chilean ship, or helicopters from Marambio (2 scheduled movements/season, 79 to 80 km); Prince Gustav Channel can stay ice-choked (Jan 2026: team waited about 2 weeks). Marambio 78.5 km; Esperanza 62.7 km; O'Higgins 53 km | ATCM40 att043; UPJŠ Jan 2026 |
| Other facilities within 25 km | Refugio San Carlos (Argentine Army hut, 1959) about 7.6 km, current status unknown; Czech AWS/ground-temperature sites on Johnson Mesa and Berry Hill (not stations); Argentine refuges on Vega Island announced 2023, completion unverified. No station within 25 km; no ASPA, ASMA or HSM within about 50 km (nearest HSM 37 at 53.8 km) | SCAR gazetteer; ATS APA database |

**Notes / dead ends / open questions:**

**Verdict: qualifies, moderate-high.** The least ice-threatened site in the batch for an inland Peninsula-side location, and the only one built as a modern, mostly renewable-powered station (still a seasonal summer base). Stated purpose: ice-free terrestrial ecosystems and geosystems, long-term climatology, glaciology, permafrost, geology, biology (a substantial peer-reviewed literature exists). Climate: mean annual air -6.8 to -6.9 °C, Feb -0.1, July -14.1; precipitation 200 to 500 mm snow; COMNAP's "mean wind 6 km/h" looks implausibly low. Hazards: the unloading slope; medical evacuation depends on Marambio ("delicate" per inspectors). The station's CEE (ATCM XXVII IP 3) text was not found. Inventory note: COMNAP 2017 sheet and the 2005 inspection give wrong coordinates ("62°22'S 58°31'W"). Full log: `Research_Logs/Batch1_A2_Mendel_Primavera_Matienzo_2026-10-04.md`.

### 16. Leningradskaya  `leningradskaya`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | Leningradskaya Station / Estação Leningradskaya / Base Leningradskaya / Leningradskaja / Stazione Leningradskaya |
| Coordinates (lat, lon) | -69.501496, 159.391148  *(source: comnap24)* |
| Largest source disagreement | 0.4 km |
| Elevation (m) | 300  *(source: comnap24)* |
| Type / detail | station / comnap24:Station / comnap17:Station / wikidata:Antarctic research station / wp_list:Summer / scar:Station |
| Status | summer-only  *(COMNAP 2024: Seasonal, Open)* |
| Status across sources | comnap24: COMNAP 2024: Seasonal, Open // comnap17: COMNAP 2017: operational period "October–March" |
| Years opened / closed | 1971 / n/a (active) |
| Capacity (winter / summer / peak) | unknown / 10 / 10 |
| Operator (context only) | Russia - Russian Antarctic Expedition ; Arctic and Antarctic Research Institute |
| Purpose as stated | science disciplines: Environmental sciences, Geodesy |
| Surface | bare rock |
| Stability flag (sources only) | rock |
| Location text | Oates Coast, Victoria Land |
| Nearest city | Cape Adare, 449.6 km (CANDIDATE) |
| Nearest highway | hwy183, 178 km  *(lines good to about ±20 km)* |
| Inventory notes | COMNAP 2017 DMS: 69°30’00’’S 159°23’00’’E // COMNAP 2024 DDM: 69° 30.0898' S 159° 23.4689' E // Wikipedia inactive-list row at the same site: "Leningradskaya" (Closed, est 1971, closed 2008) // COMNAP 2017 permafrost: Continuous |
| Sources | COMNAP Facilities CSV (Nov 2024) ; COMNAP Station Catalog (Aug 2017) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) ; SCAR Composite Gazetteer (placenames.aq) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -69.5015, 159.3911 confirmed (COMNAP; AARI 69°29'45"S 159°22'48"E; all within about 1 km); elevation 300 m (station-area nunatak 294.5 m, summit 330.5 m). The "Cape Belousov" lead name is wrong: AARI places it on the Leningradskiy nunatak (Halladay group) by Tomilin Glacier, coast 2.7 to 3 km away | COMNAP; AARI geographical review (Wayback 2015) |
| Surface verified (rock / ice / other) | **Rock.** Western part of a bedrock nunatak (granite and biotite gneiss ridge, about 1 km by 100 to 150 m, standing 100 to 230 m above the surrounding glacier); COMNAP "Ice-free ground". Usable ground is tiny: station territory 200 to 250 m by at most 50 m; about two-thirds of the nunatak is snow-covered | AARI; COMNAP 2017 |
| Ice velocity (m/yr) | Not found for the surrounding glaciers (Tomilin outlet glacier ends in a 15 to 20 m barrier; 150 to 180 m cliff to the north). ITS_LIVE/MEaSUREs not queried (a gap, not a negative result) | AARI; dead end |
| Ice thickness (m) | n/a (nunatak) | n/a |
| Bed elevation (m) | n/a (rock at surface) | n/a |
| Depth to bedrock below surface (m) | 0 (a nunatak is exposed bedrock by definition) | AARI; COMNAP |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **QUALIFIES (high)** on ground; very small site, persistent storms, buildings damaged by moisture and ice | Log |
| Status verified (year-round / summer / closed / abandoned) | **Mothballed since 31 Mar 1991; carried as a "seasonal field base."** De-conserved for one summer (2007/08, buildings iced to the ceiling, only two rooms enterable, doors forced). Last documented visit Jan 2020 (65th RAE). **No visit after 2020 found.** COMNAP "Open / Seasonal / peak 10" is nominal; AARI releases 2022 to 2025 list it only in boilerplate | Rosgidromet 2020; AARI 2022 to 2025 |
| Year opened / year closed, verified | Site chosen Jan 1970 (15th SAE), built during the 16th SAE, opened 25 Feb 1971; mothballed 31 Mar 1991; 2007/08 de-conservation (automatic met and geodetic stations installed) | Rosgidromet; Aust. Antarctic Magazine 14 (2008) |
| Capacity: winter / summer (persons) | 0 winter / 10 beds (peak 10); 800 m2 under roof; "base facilities currently mothballed" | COMNAP 2017 |
| Buildings and infrastructure: state, power, water | Original: 148 m2 service-living building, diesel plant, two magnetic pavilions, insulated warehouse, met site, geodetic point. Diesel (220 V). Helipad listed; satellite phone only; automatic met/geodetic stations operating | Rosgidromet; COMNAP 2017 |
| Landing/harbor/airstrip access | **No pier, no airstrip** (AARI mentions only a possible ski-plane strip, never built); cargo by Mi-8 helicopter from the ship; fast ice often blocks approach all summer | AARI; COMNAP |
| Reachability from nearest city and highway (route, season) | Ship only (ice-class), January to March, 1 ship visit/yr; Ob drifted in 1973 and Mikhail Somov in 1977. Nearest city Cape Adare 450 km; no current air route found | COMNAP; AARI |
| Other facilities within 25 km | None documented (not found in COMNAP, AARI or Wikipedia leads: absence at the sources, not proof of absence); no ASPA found nearby (ATS database not queried) | dead end |

**Notes / dead ends / open questions:**

**Verdict: qualifies on rock, but effectively abandoned.** **Revival realism (evidence only):** mothballed 1991; one summer de-conservation in 2007/08; the AARI 2025 plans list year-round conversion only for Russkaya, not Leningradskaya; no plan, funding or schedule found; the site is a 1 km nunatak. Stated purpose: meteorology, actinometry, aerology, geomagnetism, ionosphere, geodesy, sea ice. Climate: mean annual -14.2 °C (-40.0 min, +5.1 max), mean wind 8.4 m/s, max gust 78 m/s, precipitation 59.6 mm, polar night 53 days. Inventory note: "reopened around 2008" claims in Wikipedia summaries are overstated. Full log: `Research_Logs/Batch1_A2_Leningradskaya_Russkaya_Parodi_2026-10-04.md`.

### 17. Matienzo  `matienzo`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | Base Aérea Teniente Benjamín Matienzo / Matienzo Antartic Base / Base Antártica Matienzo / Base Matienzo |
| Coordinates (lat, lon) | -64.975865, -60.070948  *(source: comnap24)* |
| Largest source disagreement | 0.7 km |
| Elevation (m) | 32  *(source: comnap24)* |
| Type / detail | station / comnap24:Station / comnap17:Station / wikidata:Antarctic research station |
| Status | summer-only  *(COMNAP 2024: Seasonal, Open)* |
| Status across sources | comnap24: COMNAP 2024: Seasonal, Open // comnap17: COMNAP 2017: operational period "October–March" // wp_list: Wikipedia list: summer-only active |
| Years opened / closed | 1961 / n/a (active) |
| Capacity (winter / summer / peak) | unknown / 10 / 12 |
| Operator (context only) | Argentina - Instituto Antartico Argentino ; Argentine Antarctic Institute |
| Purpose as stated | science disciplines: Atmospheric chemistry and physics, Atmospheric sciences, Climate change, Climatology, Environmental sciences, Geodesy, Geology, Geophysics, Glaciology, Mapping, Marine biology, Oceanography, [...] |
| Surface | bare rock |
| Stability flag (sources only) | rock |
| Location text | Graham Land |
| Nearest city | Puerto Abrigo, 161.9 km (CANDIDATE) |
| Nearest highway | hwy1, 69 km  *(lines good to about ±20 km)* |
| Inventory notes | COMNAP 2017 DMS: 64°58’55.2’’S 60°04’25.7’’W // COMNAP 2024 DDM: 64° 58.5519' S 60° 4.2569' W // COMNAP 2017 permafrost: Discontinuous |
| Sources | COMNAP Facilities CSV (Nov 2024) ; COMNAP Station Catalog (Aug 2017) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -64.9759, -60.0709 confirmed (COMNAP; Wikipedia -64.97566, -60.07150; COMNAP 2017 about 0.7 km off; Argentine pages scatter within about 1 km; one DNA page "62°59'S 60°43'W" is wrong). Elevation 32 m. **The "Belgrano II Skiway" inventory row at the same point is a copy-paste coordinate error** (see notes) | COMNAP; Wikipedia; SCAR gazetteer |
| Surface verified (rock / ice / other) | **Base on rock; access on ice.** Larsen Nunatak (Seal Nunataks), volcanic basalt/andesite outcrop; the base occupies a discontinuous 300 m strip at its eastern end ("ice-free ground"; glaciers and snowdrifts around). Nunatak height disputed (300 m, over 200 m, 140 m) | COMNAP 2017; Fundación Marambio; SCAR UK gazetteer |
| Ice velocity (m/yr) | The nunatak sits in the remnant Seal Nunataks Ice Shelf (about 743 km2, between the collapsed Larsen A (1995) and B (2002)): flow about 25 m/yr or less (pinned by nunataks), **thinning 1.9 to 2.7 m/yr (mean 2.32)**; the authors conclude it "will not persist for many more years" (data 2001 to 2013). Status after 2016: not found | Shuman et al. 2016, Ann. Glaciol. 57(73):94 to 104 |
| Ice thickness (m) | Not found | dead end |
| Bed elevation (m) | n/a (rock outcrop) | n/a |
| Depth to bedrock below surface (m) | At/near surface at the base; permafrost "discontinuous" | COMNAP 2017 |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **UNCLEAR (split).** Base footprint on volcanic rock passes; the skiway and approach are on glacier or ice-shelf-remnant ice, access is by air only (Marambio 183 km), the remnant shelf is thinning and may lose contact with nunataks. No reported damage or burial of the nunatak | Log; Shuman 2016 |
| Status verified (year-round / summer / closed / abandoned) | Summer-only on paper (COMNAP "Seasonal, Open"). **Last confirmed operation: summer 2017/18 (15 Jan to 23 Feb 2018, 10 people). Did NOT operate in 2025/26** (Gaceta Marinera, 27 Mar 2026; absent from the campaign opening list). 2019 to 2024: not found. A 2026 opposition draft resolution says Matienzo and Melchior have not been operated "for years" (political text, unverified) | Fundación Marambio 2018; Gaceta Marinera 2026; HCDN 2026 |
| Year opened / year closed, verified | Inaugurated 15 Mar 1961 (joint Army/Air Force, on the old San Antonio refuge; 240 t hauled from Esperanza by tracked vehicles); Air Force only from 1964/65/66; deactivated as a permanent base 1971/72 or 1972/73; Wikipedia adds reopening 1974 and a second closure 1985 (secondary) | Fundación Marambio; Air Force history |
| Capacity: winter / summer (persons) | 0 winter / 12 beds (peak 12: 10 staff + 2 scientists); 10 to 15 temporary residents | COMNAP; argentina.gob.ar |
| Buildings and infrastructure: state, power, water | About 1,000 m2 under roof; glaciology lab 700 m2; accommodation, stores, power building, fuel platform, heliport; fossil fuel 380 V; two snow-cats, no boats; sat phone + VHF; museum restored 2018; 2018 work: generator maintenance, 12 V lighting, first photovoltaic tests, radio LU1ZAB. Water source and system: **not found** | COMNAP 2017; Fundación Marambio 2018 |
| Landing/harbor/airstrip access | **No pier** ("Ship landing facilities: None"); helipad yes. Ski-equipped Twin Otter lands on the adjacent glacier (1,500 m ski sector 1,500 m to 2 km from the base; OurAirports puts SAWZ 1.8 km WSW at 23 m); in 2018 the crew carried cargo by hand over a 1,200 m traverse. Wikipedia lists the surface as "Sea Ice", primary sources say glacier | COMNAP 2017; Fundación Marambio 2018; OurAirports |
| Reachability from nearest city and highway (route, season) | By air only in practice: Twin Otter (Air Force "Águila" squadron) and Bell 212 / Mi-171E helicopters from Marambio 183 km; flying weather only. Nearest facility Primavera 100.5 km; Esperanza 230 km | COMNAP; argentina.gob.ar |
| Other facilities within 25 km | None. Nearest COMNAP facility Primavera 100.5 km; nearest ATS protected area ASPA 134 at 100.7 km | ATS APA database |

**Notes / dead ends / open questions:**

**Verdict: unclear (split): base on rock, access on ice, operations lapsed.** **Inventory correction: the "Belgrano II Skiway" row (SAYB) is NOT at Matienzo.** Wikipedia's airports list gives SAYB and Matienzo's SAWZ identical coordinates; the Belgrano II row's own location text reads "Bertrab Nunatak", near 77.88°S 34.63°W, over 1,600 km away, and airport databases put SAYB at 77°52'27"S 34°37'34"W. The Matienzo airstrip is SAWZ. Stated purpose: meteorology and aurora, aerial surveys, geology, geodesy, oceanography, the "Larsen project" on barrier retreat. Climate: mean annual -5 °C (COMNAP) vs -11.6 °C (1960s record), extremes 13.1/-44.4 °C: unresolved. Contradictions: Argentina says the base was "embedded in Larsen A, which disintegrated in 1995" vs Shuman's remnant-shelf description (the latter is more specific). Open: operations record 2019 to 2024; Seal Nunataks ice shelf after 2016; water/fuel details; no Art. VII inspection found. Full log: `Research_Logs/Batch1_A2_Mendel_Primavera_Matienzo_2026-10-04.md`.

### 18. Molodezhnaya  `molodezhnaya`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | Molodyozhnaya Station / Molodyozhnaya / Molodëzhnaja, nauchnaja stancija / Molodezhnaya Station / Molodjoschnaja-Station / Base Molodiózhnaya / Mołodiożnaja / Stazione Molodežnaja / Base Molodyozhnaya / Base Molodezhnaya / Molodëzhnaja, nauchnaja stancija /SSSR/ |
| Coordinates (lat, lon) | -67.665443, 45.842038  *(source: comnap24)* |
| Largest source disagreement | 12.5 km |
| Elevation (m) | 40  *(source: comnap24)* |
| Type / detail | station / comnap24:Station / comnap17:Station / wikidata:Antarctic research station / scar:Station / scar:Station / scar:Station |
| Status | summer-only  *(COMNAP 2024: Seasonal, Open)* |
| Status across sources | comnap24: COMNAP 2024: Seasonal, Open // comnap17: COMNAP 2017: operational period "December–March" // wp_list: Wikipedia list: summer-only active |
| Years opened / closed | 1963 / n/a (active) |
| Capacity (winter / summer / peak) | unknown / 15 / 15 |
| Operator (context only) | Russia - Russian Antarctic Expedition ; Arctic and Antarctic Research Institute |
| Purpose as stated | science disciplines: Environmental sciences, Geodesy, Pollution |
| Surface | bare rock |
| Stability flag (sources only) | rock |
| Location text | Thala Hills, East Antarctica |
| Nearest city | Temirötkel, 296.5 km (CANDIDATE) |
| Nearest highway | hwy4, 62 km  *(lines good to about ±20 km)* |
| Inventory notes | COMNAP 2017 DMS: 67°40’00’’S 45°51’00’’E // COMNAP 2024 DDM: 67° 39.9266' S 45° 50.5223' E // COMNAP 2017 permafrost: Continuous |
| Sources | COMNAP Facilities CSV (Nov 2024) ; COMNAP Station Catalog (Aug 2017) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) ; SCAR Composite Gazetteer (placenames.aq) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -67.6654, 45.8420 confirmed (COMNAP; SCAR AUS entry 0.4 km off). Elevation 40 m (TASS 42 m). **Warning: the SCAR USA entry "Molodezhnaya Station" (46.1344°E, from COMNAP 2006) is the old Vechernyaya airfield, 12.6 km east.** In the Thala Hills, 500 to 600 m from the coast | COMNAP; SCAR gazetteer |
| Surface verified (rock / ice / other) | **Rock:** parallel ice-free rocky ridges (up to 1 km long, about 150 m wide) in the Molodezhny Oasis (8.3 by 2.7 km, max 110 m); crystalline basement (pegmatites, migmatites); more than 40 lakes up to 36 m deep; COMNAP "ice-free ground", permafrost continuous. Parts of the station area are snow or ice covered | COMNAP 2017; Belarus CEE 2013; Mining Univ. 2025 |
| Ice velocity (m/yr) | **ITS_LIVE v2 (agent's own vector-median computation): 1.4 m/yr at the station pixel; median 2.2, max 7 m/yr within 500 m; up to 65 m/yr within 3 km** where inland ice enters the window. Literature: ice-sheet edge about 100 m/yr (Kotlyakov 2000); Hayes outlet glacier 900 to 1,400 m/yr but on the Vechernyaya side, not the station | Log (S15); Belarus CEE |
| Ice thickness (m) | Not found (Bedmap3 returned 503; BedMachine needs a login). CEE: ice sheet 10 to 20 m thick at the coast, about 500 m at 10 km inland | dead end; Belarus CEE |
| Bed elevation (m) | Not found | dead end |
| Depth to bedrock below surface (m) | At/near surface (oasis rock); not measured | Log |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **QUALIFIES on ground (high); moderate on site hazard.** Documented flood hazards: a lake-dam outburst ruptured a large fuel tank (2020 inspection); melt pools at footings; buildings destroyed by wind, fire or flooding; **17 Jan 2025 two RAE staff were evacuated to Gora Vechernyaya "due to the threat of flood inundation"** | ATCM43 att061 (Aus. 2020); AARI 2025 |
| Status verified (year-round / summer / closed / abandoned) | **Seasonal field base** (since 2006; Dec to Mar); winter population 0. Closure accounts conflict: "temporarily closed in 1990" (Australia 2020) vs mothballed 1999 during the 44th RAE (Rosgidromet). RAE 70 (2024/25) and RAE 71 (from Nov 2025) list it as seasonal; a Mining University team worked at the "decommissioned" station in the 70th RAE | Aus. 2020; Rosgidromet; AARI |
| Year opened / year closed, verified | Opened Feb 1962, officially 14 Jan 1963; the Soviet Union's main Enderby Land station; "small Molodezhnaya" consolidation begun 1998; Akademik Fedorov called 27 Apr 2022 for helicopter work | COMNAP 2017; Rosgidromet |
| Capacity: winter / summer (persons) | 0 winter / 15 beds (summer staff 15; 7,000 m2 under roof); 2020 inspection saw 7 (leader, 3 drivers, 2 mechanics, cook); Mar 2013: 15 plus 3 Belarusians | COMNAP; Aus. 2020; TASS |
| Buildings and infrastructure: state, power, water | About 60 buildings, mostly unused and in poor repair; 15 tanks of over 1 million L each (about 12 near the old skiway; residual sludge unassessed); rocket-launch complex, antennas, a derelict Il-14; about 6 buildings in seasonal use; powerhouse with 3 generator sets (good); water from a melt lake above the station; fuel flown in by helicopter in a bulk bag to an elevated tank without secondary containment; extensive fuel contamination seen in 2020 | ATCM43 att061 |
| Landing/harbor/airstrip access | No ship landing facilities; a skiway on the plateau about 7 km away serves DROMLAN ski aircraft; the original heavy compacted-snow runway (1979 to 81; 2,540 by 42 m; Il-76TD) was about 10 to 12 km east near Mount Vechernyaya, last prepared Nov 1992 (sources conflict on length, year and location) | ATCM25 WP15; COMNAP 2017 |
| Reachability from nearest city and highway (route, season) | Ship plus helicopter; the nearest COMNAP facility is S17 Camp (Japan) at 281 km; nearest city Temirötkel about 296 km | COMNAP; computed |
| Other facilities within 25 km | Mount Vechernyaya (Belarus, #19) about 13 km; the old Vechernyaya airfield camp; nothing else | Log |

**Notes / dead ends / open questions:**

**Verdict: qualifies on rock but is a decaying legacy station; the clean-up burden is the issue.** 2020 inspectors (Australia): a clean-up would be "a very substantial challenge" and "a priority", needing a "much greater level of resourcing". Climate: mean annual -11 °C, precipitation 270 mm, mean wind 38 km/h SE, 190 snowstorm days a year, min about -42 °C. Stated purpose now: stabilize or dismantle buildings, clean up, support intracontinental aviation. No ASPA/ASMA/HSM found (ATS database not queryable: unverified). Full log: `Research_Logs/Batch1_A2_B2_Molodezhnaya_MtVechernyaya_DruzhnayaIV_Soyuz_SarieMarais_2026-10-04.md`.

### 19. Mountain Evening  `mountain-evening`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | Vechernyaya Base / Vechernyaya / Mountain Evening (Vechernyaya) / Mountain Vechernyaya / Base Vechernyaya |
| Coordinates (lat, lon) | -67.658333, 46.153333  *(source: comnap24)* |
| Largest source disagreement | 42.3 km |
| Elevation (m) | 95  *(source: comnap24)* |
| Type / detail | station / comnap24:Station / comnap17:Station / wikidata:Antarctic research station / wikidata:Antarctic research station |
| Status | summer-only  *(COMNAP 2024: Seasonal, Open)* |
| Status across sources | comnap24: COMNAP 2024: Seasonal, Open // comnap17: COMNAP 2017: operational period "December–March" // wp_list: Wikipedia list: summer-only active |
| Years opened / closed | 2006 / n/a (active) |
| Capacity (winter / summer / peak) | unknown / 7 / 7 |
| Operator (context only) | Republic of Belarus ; Belarus - National Academy of Sciences of Belarus |
| Purpose as stated | science disciplines: Atmospheric chemistry and physics, Climatology, Ecology, Environmental sciences, Geology, Geophysics, GIS, Isotopic chemistry, Limnology, Marine biology, Microbiology, Ozone study, [...] |
| Surface | bare rock |
| Stability flag (sources only) | rock |
| Location text | Mount Vechernyaya, Thala Hills |
| Nearest city | Temirötkel, 308.1 km (CANDIDATE) |
| Nearest highway | hwy4, 64 km  *(lines good to about ±20 km)* |
| Inventory notes | COMNAP 2017 DMS: 67°39’35’’S 46°09’18’’E // COMNAP 2024 DDM: 67° 39.5' S 46° 9.2' E // COMNAP region: East Antarctica // COMNAP 2017 permafrost: Continuous |
| Sources | COMNAP Facilities CSV (Nov 2024) ; COMNAP Station Catalog (Aug 2017) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -67.6583, 46.1533 confirmed (COMNAP; Belarus catalogue 67°39'35"S 46°09'18"E, 0.2 km off). Elevation 95 m (Mount Vechernyaya itself 272 m). **This is Belarus's Mount Vechernyaya (Gora Vechernyaya) station**, not Chinese or Japanese. Distance to Molodezhnaya 13 km by coordinates (prose sources say 18 to 28 km) | COMNAP; Belarus catalogue 2017; CEE 2013 |
| Surface verified (rock / ice / other) | **Rock.** A flat mountain terrace 350 m by 50 to 80 m east of the mountain, on enderbite and charnockite gneisses; modules stand on adjustable legs "with small base plates bolted to bedrock"; soils only 20 cm over solid rock; about 70% of the wider territory is glacier-covered | Belarus CEE 2013; Aus. 2020 |
| Ice velocity (m/yr) | **ITS_LIVE (agent's computation): 0 m/yr at the station pixel; median 1, max 3 m/yr within 500 m;** the Hayes outlet glacier starts 2 to 3 km east at about 100 to 220 m/yr (CEE quotes 900 to 1,400 m/yr near Lazurnaya Bay, a different place); crevasses within 20 to 30 km of the coast | Log (S15); CEE |
| Ice thickness (m) | n/a at the site | n/a |
| Bed elevation (m) | n/a (rock) | n/a |
| Depth to bedrock below surface (m) | At the surface (modules bolted to bedrock) | Aus. 2020 |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **QUALIFIES (high).** Hazards: summer winds 12 to 18 m/s, gusts to 53 m/s (COMNAP max 194 km/h), 190 snowstorm days a year, lake-level instability | CEE 2013 |
| Status verified (year-round / summer / closed / abandoned) | **Seasonal (Dec to Mar).** Wintering was planned "from February 2021" but Belta (2024) still calls it seasonal; the 15th Belarusian expedition (Oct 2022, 12 people) was a "seasonal expedition"; **no confirmation that wintering has begun** | Aus. 2020; Belta 2024 |
| Year opened / year closed, verified | Belarusian camp inside the Russian field base since 2006; station modules: first 3-section module Dec 2015 to Jan 2016; second 8-section module 2020/21; five-section dining complex commissioned for experimental use 20 Jan 2025; inspected by Australia 27 Jan 2020 (compliant) | Belarus catalogue; AARI Jan 2025 |
| Capacity: winter / summer (persons) | 7 beds (COMNAP 2017), 8 (2020), maximum 12 (COMNAP peak 12); Belarus Republican Centre (31 Dec 2023): 16 new structures, 9 renovated, supports up to 15; planned 3 to 4 winter scientists | COMNAP; belpolus.by |
| Buildings and infrastructure: state, power, water | Container modules on legs; diesel gensets (2 x 100 kVA, 60 kVA, 20 kVA, 6 kVA backup) plus solar; fuel 13 m3 stationary + 3 insulated tank-containers; heated water and drain line about 100 m; water from nearby lakes; BGAN/FLEET/Iridium/VSAT, HF/VHF; helipad on cleared rock; vehicles (snowmobiles, Apache crawler, BOBR amphibious); renovated Soviet buildings; hydroponics. An older Soviet field base 500 m away (13 buildings at its peak, 7 left in 2013) | Aus. 2020; belpolus.by |
| Landing/harbor/airstrip access | Ship plus helicopter (Russian RAE on contract); overland route to Molodezhnaya and its skiway; 4 flight visits and 2 ship visits a year (COMNAP 2017) | Aus. 2020; COMNAP |
| Reachability from nearest city and highway (route, season) | As Molodezhnaya; nearest city Temirötkel about 308 km | COMNAP; inventory |
| Other facilities within 25 km | Molodezhnaya about 13 km; the old Russian Vechernyaya field base and aerodrome about 500 m | Log |

**Notes / dead ends / open questions:**

**Verdict: qualifies, high.** The most active and best-kept station in this region of the batch (not Russian, though it uses Russian logistics). Stated purpose: atmospheric aerosol, ozone and UV (AERONET), hydrometeorology, biology, geophysics; a political aim of Consultative Party status. CEE found no ASPA, ASMA, HSM or SSSI at the site. Nearest emergency facility 1,400 km. Open: whether wintering has begun. Full log: `Research_Logs/Batch1_A2_B2_Molodezhnaya_MtVechernyaya_DruzhnayaIV_Soyuz_SarieMarais_2026-10-04.md`.

### 20. Pedro Vicente Maldonado  `pedro-vicente-maldonado`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | Maldonado Base / Maldonado / Maldonado Station / Pedro Vicente Maldonado Station / Base Maldonado / base Pedro Vicente Maldonado / stazione Pedro Vicente Maldonado / Base antarctique Refugio Ecuador / Stazione scientifica Pedro Vincente Maldonado / Stazione Maldonado |
| Coordinates (lat, lon) | -62.449329, -59.740969  *(source: comnap24)* |
| Largest source disagreement | 0.1 km |
| Elevation (m) | 10  *(source: comnap24)* |
| Type / detail | station / comnap24:Station / comnap17:Station / wikidata:Antarctic research station / scar:Station |
| Status | summer-only  *(COMNAP 2024: Seasonal, Open)* |
| Status across sources | comnap24: COMNAP 2024: Seasonal, Open // comnap17: COMNAP 2017: operational period "October–March" // wp_list: Wikipedia list: summer-only active |
| Years opened / closed | 1990 / n/a (active) |
| Capacity (winter / summer / peak) | unknown / 22 / 34 |
| Operator (context only) | Ecuador - Instituto Antártico Ecuatoriano ; Instituto Antartico Ecuatoriano |
| Purpose as stated | science disciplines: Climatology, Climate change, Environmental sciences, Geodesy, Geology, Geophysics, Glaciology, Geomorphology, Mapping, Marine biology, Microbiology, Oceanography, Pollution, Sedimentology, Soil [...] |
| Surface | bare rock |
| Stability flag (sources only) | rock |
| Location text | Greenwich Island |
| Nearest city | Pergamino, 39.8 km (NEAR_CITY) |
| Nearest highway | hwy1, 162 km  *(lines good to about ±20 km)* |
| Inventory notes | COMNAP 2017 DMS: 62°26’57.6’’S 59°44’27.5’’W // COMNAP 2024 DDM: 62° 26.9598' S 59° 44.4581' W // COMNAP region: Antarctic Peninsula // COMNAP 2017 permafrost: Continuous |
| Sources | COMNAP Facilities CSV (Nov 2024) ; COMNAP Station Catalog (Aug 2017) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) ; SCAR Composite Gazetteer (placenames.aq) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -62.4493, -59.7410 confirmed (COMNAP; SCAR -62.4492, -59.7422; the 2017 catalogue prints an invalid "62°26'96.0''"). Elevation 10 m. Punta Fort Williams (Spark Point in one paper), north coast of Greenwich Island, Guayaquil Bay; a different "Fort William" exists on Robert Island 8.7 km away | COMNAP; SCAR; Santana and Dumont 2006 |
| Surface verified (rock / ice / other) | **Rock with caveats:** the station stands on the "Maldonado Platform", a sedimentary platform of wide pebble beach ridges at 10 to 11 m (eight raised ridges to 13.5 m) with volcanic bedrock (Late Cretaceous to Paleocene andesites and basalts) outcropping between ridges; a depression where snow and water remain all summer; the Culebra River (about 2 to 3 m3/s) crosses the platform. A 2018 undergraduate ESPOL thesis (lower authority) puts the point at about 80% sediment / 20% ice | Santana and Dumont 2006/2007 (USGS OF-2007-1047); Choez Mero 2018 |
| Ice velocity (m/yr) | Not found. The 2018 thesis says a 2014 photo shows a glacier "a few metres from the station" and warns its advance/retreat could erode the base (recommends annual DGPS or relocation); the INAE director said in 2009 that nearby glaciers retreated 150 to 200 m in ten years and the base, "surrounded by snow and ice" in 2006, was on rock by 2009. Quito Glacier (marine-terminating) is 2 to 3 km west; Greenwich glacier area fell 14.4% 1957 to 2023 | Choez Mero 2018; El Universo 2009; Anais Acad. Bras. Ciências 2024 |
| Ice thickness (m) | Not found | dead end |
| Bed elevation (m) | Not found | dead end |
| Depth to bedrock below surface (m) | Bedrock outcrops between beach ridges; depth under the ridges not found. COMNAP: permafrost "continuous" | COMNAP 2017 |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **QUALIFIES with caveats (medium).** Landslide/avalanche hazard "minimal" (flat ground); thesis rates seismic and flood hazard low, volcanic ash fall high (the thesis misstates Deception's distance as 150 km; about 76 km computed) | Choez Mero 2018 |
| Status verified (year-round / summer / closed / abandoned) | Seasonal (Oct to Mar); the XXIX Ecuadorian expedition used it in 2025/26. Ecuador's own text says it "will become a year-round facility within five years" (undated; has not materialized) | COMNAP 2017; El Comercio Oct 2026; SCAR |
| Year opened / year closed, verified | Inaugurated 2 Mar 1990 (COMNAP/Wikipedia), March 1989 (INAE director 2009) or 1991 ("35 years" in 2026): unresolved; capacity raised from 22 to 32 in 2012 | COMNAP; El Universo; El Comercio |
| Capacity: winter / summer (persons) | 0 winter / 34 beds (22 staff + 10 scientists; design 22, 32 since 2012); 908 m2 under roof, 200 m2 labs, 22 m2 medical; 2009 expedition: 13 scientists, 8 Jan to 22 Feb | Ecuador 2017 catalogue; El Universo |
| Buildings and infrastructure: state, power, water | Fossil fuel + renewable (CSV), 220 V; 3 rubber boats, 2 snowmobiles; workshops (electrical, mechanical, wood, ICT, gas, welding); helipad yes; Spanish-donated solar lighthouse nearby; wastewater sludge trials; email, sat phone, VHF. Water supply and fuel storage: **not found** | Ecuador 2017 catalogue; IHO HCA-18 report |
| Landing/harbor/airstrip access | No pier or wharf, no airstrip; ship visits Jan to Mar and Oct to Dec | Ecuador 2017 catalogue |
| Reachability from nearest city and highway (route, season) | Staff fly LATAM to Punta Arenas; beyond that only indirect press accounts (Chilean C-130 to King George Island, then boat about 50 miles: unverified). Nearest city Pergamino about 45 km | El Comercio 2026 |
| Other facilities within 25 km | Arturo Prat 5.1 km (year-round); Risopatrón 8.1 km (seasonal); Cámara (Half Moon Island) 18.5 km (seasonal); nearest ASPA 112 about 8 km (ASPA 144 revoked by Measure 9 (2023)) | COMNAP; ATS Measures 2023 |

**Notes / dead ends / open questions:**

**Verdict: qualifies with caveats; the least documented on ground stability.** Stated purpose: environmental studies, Ecuador-Antarctica interaction, climate change, technology for Antarctica; glaciological parameters monitored seasonally since 2010; mass balance estimated on the Quito Glacier. Climate: mean February 1 °C, 600 mm, mean wind 22.3 km/h, max 160.6 km/h dominant E. Open: ice velocity, station-specific bedrock, water/fuel details. Full log: `Research_Logs/Batch1_A2_Decepcion_GdC_Shirreff_Maldonado_Risopatron_2026-10-04.md`.

### 21. Primavera  `primavera`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | Base Primavera / Base Antártica Primavera / Primavera Antartic Base / Base antartica dell'esercito argentino Primavera / Stazione Primavera |
| Coordinates (lat, lon) | -64.155854, -60.954256  *(source: comnap24)* |
| Largest source disagreement | 0.5 km |
| Elevation (m) | 50  *(source: comnap24)* |
| Type / detail | station / comnap24:Station / comnap17:Station / wikidata:Antarctic research station |
| Status | summer-only  *(COMNAP 2024: Seasonal, Open)* |
| Status across sources | comnap24: COMNAP 2024: Seasonal, Open // comnap17: COMNAP 2017: operational period "November–March" // wp_list: Wikipedia list: summer-only active |
| Years opened / closed | 1977 / n/a (active) |
| Capacity (winter / summer / peak) | unknown / 12 / 18 |
| Operator (context only) | Argentina - Instituto Antartico Argentino ; Argentine Antarctic Institute |
| Purpose as stated | science disciplines: Climate change, Ecology, Environmental sciences, Marine biology |
| Surface | bare rock |
| Stability flag (sources only) | rock |
| Location text | Graham Land |
| Nearest city | Puerto Abrigo, 141.7 km (CANDIDATE) |
| Nearest highway | hwy1, 30 km  *(lines good to about ±20 km)* |
| Inventory notes | COMNAP 2017 DMS: 64°9’35.1’’S 60°57’25.5’’W // COMNAP 2024 DDM: 64° 9.3512' S 60° 57.2554' W // COMNAP 2017 permafrost: None |
| Sources | COMNAP Facilities CSV (Nov 2024) ; COMNAP Station Catalog (Aug 2017) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -64.1559, -60.9543 confirmed (COMNAP; all sources within about 0.5 km); elevation 50 m in every source. COMNAP's "Dundee Coast" is an error (Danco Coast). Jetty 64°9'19.53"S 60°57'11.69"W (IAATO) | COMNAP; IAATO manual; ASPA 134 plan |
| Surface verified (rock / ice / other) | **Rock.** Rocky promontory on the south side of Cierva Cove, a steep granitic massif ("large granite massif"; "ice-free ground"). The "granite" label comes from program text, not a geological survey; no lithology source found | Fundación Marambio; COMNAP 2017; IAATO |
| Ice velocity (m/yr) | Not measured. Two large tidewater glaciers (Breguet and Gregory) end at the head of Cierva Cove about 4 to 5 km east; the station sits on the western promontory away from the calving fronts; the cove entrance is exposed to large westerly swell | IAATO manual; Wikipedia IBA (secondary) |
| Ice thickness (m) | n/a | n/a |
| Bed elevation (m) | n/a (rock) | n/a |
| Depth to bedrock below surface (m) | At/near surface (promontory). Permafrost field blank in COMNAP; a 2018 master's dissertation (TTOP model, Cierva Point, 9 sites 2012 to 2018) reports permafrost tables at 0.4 to 5 m (summary only, unverified) | COMNAP 2017 |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **QUALIFIES (high).** Same spot since the Capitán Cobbett naval refuge (23 Jan 1954); no relocation, damage or burial found. The ASPA plan calls the coastal rock wall's scree "unstable" in places (protected area, not the footprint) | Fundación Marambio; ASPA 134 plan |
| Status verified (year-round / summer / closed / abandoned) | Seasonal (Nov to Mar per COMNAP; Dec to Mar per Argentine pages). **Reactivated 2024/25 and 2025/26** (Irízar campaign). Permanent 1977 to 1982, summer-only since; no wintering since 1982 | COMNAP; argentina.gob.ar 2025; Pescare 2025 |
| Year opened / year closed, verified | Naval refuge Capitán Cobbett 23 Jan 1954; base inaugurated 3 Mar 1977 (other pages 8 Mar 1977); "deactivated by a SCAR resolution" in 1982 (one source, unverified elsewhere) | COMNAP; Fundación Marambio |
| Capacity: winter / summer (persons) | 0 winter / 18 beds (peak 18: 12 staff + 6 scientists); usual complement 6 + 4 foreign scientists + 8 Army | COMNAP; Fundación Marambio |
| Buildings and infrastructure: state, power, water | Eight interconnected buildings with walkways to protect vegetation (ASPA plan; Wikipedia counts 11); main house, dining room, power plant, lab, carpentry shop, infirmary, vehicle park, stores, cold chamber, radio. Fossil fuel, 220 V. Sat phone + VHF. Water source and fuel storage: **not found** | ASPA 134 plan; COMNAP 2017 |
| Landing/harbor/airstrip access | Jetty plus a beach access that the ASPA excludes; Wikipedia lists a concrete "Primavera Heliport" at -64.1566, -60.9534; landing without DNA permission not allowed (IAATO marine-only site). No airstrip | IAATO; Wikipedia airports list |
| Reachability from nearest city and highway (route, season) | Sea only: icebreaker Almirante Irízar and landing craft; 5 ship visits/yr (Dec to Mar). Nearest facilities: Matienzo 100.5 km, Melchior 99.5 km, Almirante Brown 123 km, González Videla 117.6 km | COMNAP 2017; argentina.gob.ar 2025 |
| Other facilities within 25 km | None. ASPA 134 (Cierva Point and offshore islands) 3.3 km (the station and its beach access are excluded); Bombay Island (Mikkelsen Harbour) Argentine refuge 29.6 km (outside 25) | ATS APA database |

**Notes / dead ends / open questions:**

**Verdict: qualifies, high.** Heavily regulated surroundings: ASPA 134 (SSSI 15 in 1985, ASPA 2002, current plan Measure 5 (2013); permit entry only; ten breeding bird species; extensive moss turf with about 80 cm peat; invasive Poa pratensis present). Stated purpose: logistics for the base and refuges, SAR, science (limnology, birds, mosses, lichens, Cierva Point wetlands). Climate: max 13 °C, min -20 °C, NW winds averaging 45 km/h (Fundación Marambio); no long-term mean found. Hazard: calving ice and swell in the bay. Open: water/fuel/power details, lithology, permafrost data. The gazetteer also lists a "Primavera, cabo" at -64.3, -61.07 (about 15 km off): not this station. Full log: `Research_Logs/Batch1_A2_Mendel_Primavera_Matienzo_2026-10-04.md`.

### 22. Rada Covadonga  `rada-covadonga`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | none found |
| Coordinates (lat, lon) | -63.320658, -57.898224  *(source: comnap24)* |
| Largest source disagreement | 0.0 km |
| Elevation (m) | unknown  *(source: unknown)* |
| Type / detail | station / comnap24:Station / wikidata:Antarctic research station |
| Status | summer-only  *(COMNAP 2024: Seasonal, Open)* |
| Status across sources | comnap24: COMNAP 2024: Seasonal, Open |
| Years opened / closed | unknown / n/a (active) |
| Capacity (winter / summer / peak) | unknown / unknown / unknown |
| Operator (context only) | Instituto Antártico Chileno |
| Purpose as stated | unknown (Wikidata class only: Antarctic research station) |
| Surface | unknown |
| Stability flag (sources only) | unknown |
| Location text | Antarctic Peninsula |
| Nearest city | Esperanza, 46.5 km (NEAR_CITY) |
| Nearest highway | hwy1, 31 km  *(lines good to about ±20 km)* |
| Inventory notes | COMNAP 2024 DDM: 63° 19.2395' S 57° 53.8934' W // COMNAP region: Antarctic Peninsula |
| Sources | COMNAP Facilities CSV (Nov 2024) ; Wikidata |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -63.3207, -57.8982 (COMNAP record 104; about 84 m from O'Higgins, 144 m from GARS) | [S1] 2026-10-04 |
| Surface verified (rock / ice / other) | See #3 (same islet) | [S3] |
| Ice velocity (m/yr) |  |  |
| Ice thickness (m) |  |  |
| Bed elevation (m) |  |  |
| Depth to bedrock below surface (m) |  |  |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | See #3 and #2. **Not a separate station** | [S16] 2026-10-04 |
| Status verified (year-round / summer / closed / abandoned) | COMNAP: "Seasonal", open, with almost every field empty (last modified 19 Mar 2021). Not year-round | [S1] 2026-10-04 |
| Year opened / year closed, verified |  |  |
| Capacity: winter / summer (persons) |  |  |
| Buildings and infrastructure: state, power, water |  |  |
| Landing/harbor/airstrip access |  |  |
| Reachability from nearest city and highway (route, season) |  |  |
| Other facilities within 25 km | O'Higgins 0.08 km; GARS 0.14 km | [S1] |

**Notes / dead ends / open questions:**

**Judgment: a NAME, not a station (moderate-high).** "Rada" means roadstead/anchorage. Chile's science-support document gives the O'Higgins base's location itself as "Rada Covadonga, Cabo Legoupil"; the 1948 relief ships anchored in the "Covadonga anchorage"; "Puerto Covadonga" is the civil name and the official capital of the Antártica commune. For planning, **drop #22 as a separate row and fold it into O'Higgins (#3)**; COMNAP's record may mean the landing or anchorage point. This also means the batch is really 31 rows, and #2, #3, #22 are one site. Decision on removing the row left to the developer (the numbering is shared with the maps). Full log: `Research_Logs/Batch1_A1_GARS_OHiggins_Petrel_2026-10-04.md`.

### 23. Risopatron  `risopatron`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | Risopatrón Base / Luis Risopatrón / Base Luis Risopatrón |
| Coordinates (lat, lon) | -62.378533, -59.700724  *(source: comnap24)* |
| Largest source disagreement | 1.1 km |
| Elevation (m) | 15  *(source: comnap24)* |
| Type / detail | station / comnap24:Station / comnap17:Station / wikidata:shelter |
| Status | summer-only  *(COMNAP 2024: Seasonal, Open)* |
| Status across sources | comnap24: COMNAP 2024: Seasonal, Open // comnap17: COMNAP 2017: operational period "October–March" // wp_list: Wikipedia list: summer-only active |
| Years opened / closed | 1949 / n/a (active) |
| Capacity (winter / summer / peak) | unknown / 2 / 6 |
| Operator (context only) | Chile - Instituto Antártico Chileno |
| Purpose as stated | science disciplines: Environmental sciences, Geology, Glaciology, Meteorology, Terrestrial biology |
| Surface | bare rock |
| Stability flag (sources only) | rock |
| Location text | Robert Island |
| Nearest city | Pergamino, 46.2 km (NEAR_CITY) |
| Nearest highway | hwy1, 168 km  *(lines good to about ±20 km)* |
| Inventory notes | COMNAP 2017 DMS: 62°22’17’’S 59°42’53’’W // COMNAP 2024 DDM: 62° 22.712' S 59° 42.0434' W // COMNAP region: Antarctic Peninsula // COMNAP 2017 permafrost: None |
| Sources | COMNAP Facilities CSV (Nov 2024) ; COMNAP Station Catalog (Aug 2017) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -62.3785, -59.7007 confirmed (COMNAP; Wikipedia 0.01 km off; the COMNAP 2017 catalogue is 1.07 km off; INACH 2009 2.9 km off; the ASPA 112 plan's 62°24'S 59°30'W is a peninsula centre). Elevation 15 m (COMNAP) vs 40 m (ASPA 112 plan): unresolved. On the isthmus joining Coppermine Peninsula to Robert Island, between Carlota Cove and Coppermine Cove; no SCAR record for the station | COMNAP; ASPA 112 plan [V] |
| Surface verified (rock / ice / other) | **Rock (solid), medium-high.** ASPA 112 plan: the station "stands 40 m above sea level, on solid rock surface, 150 m from the coastal line", about 100 m west of the protected area; Late Cretaceous basaltic lavas, a perched strandflat; the isthmus is a 10 m terrace of marine gravel. COMNAP: permafrost "None", "Ice-free ground" | ASPA 112 plan (Measure 4, 2012) [V]; COMNAP 2017 |
| Ice velocity (m/yr) | Not found. Higher ground on the peninsula is permanently ice-covered; the Robert Island ice cap lost 17.35% of its area 1957 to 2023; nothing reports ice moving toward the site | ASPA 112 plan; Anais Acad. Bras. Ciências 2024 |
| Ice thickness (m) | n/a | n/a |
| Bed elevation (m) | n/a | n/a |
| Depth to bedrock below surface (m) | At/near surface ("solid rock") | ASPA 112 plan |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **QUALIFIES (medium-high on ground; low on current building state).** No damage, relocation or erosion report; INACH 2009 called the module "in deteriorated condition" | ASPA 112 plan; INACH 2009 |
| Status verified (year-round / summer / closed / abandoned) | Seasonal (Oct to Mar); COMNAP Seasonal, Open; 2025/26 dates not found; Wikipedia says "recently remodeled" (summary only) | COMNAP 2017 |
| Year opened / year closed, verified | Naval refuge "Refugio Naval Coppermine" 20 Mar 1949; small base 1954; renamed Base Luis Risopatrón 24 Sep 1991 | COMNAP 2017; Wikipedia (lead) |
| Capacity: winter / summer (persons) | 0 winter / 5 (ASPA 112 plan, INACH 2009) or 6 (COMNAP beds and peak) | ASPA 112 plan; INACH 2009; COMNAP |
| Buildings and infrastructure: state, power, water | 5 modules for accommodation, labs and storage (ASPA plan) or one habitation module plus a lounge/dining container (INACH 2009); 60 m2 under roof, 15 m2 microbiology lab, 25 m2 logistics; power fossil fuel 220 V for 10 h/day; Zodiacs, no land vehicles; sat phone + VHF. Water and fuel storage: **not found** | COMNAP 2017 p.36; ASPA 112 plan |
| Landing/harbor/airstrip access | No ship landing facilities; sea landing at the beaches in front of the station only (Carlota or Coppermine Cove); helicopter only in emergencies, landing east of the isthmus outside the ASPA | ASPA 112 plan |
| Reachability from nearest city and highway (route, season) | Sea only; nearest city Pergamino about 46 km; hospital about 1,000 km | COMNAP 2017; inventory |
| Other facilities within 25 km | Maldonado 8.1 km; Arturo Prat 11.3 km; Nelson Island ASPA 133 about 30 km NW | computed from COMNAP |

**Notes / dead ends / open questions:**

**Verdict: qualifies; tiny (5 to 6 people).** Contiguous to ASPA 112 (Coppermine Peninsula; SPA 16 in 1970; plan revised 2012; a later revision may exist, not checked): a large moss carpet (about 1.5 ha) and giant-petrel colonies; no vehicles, permit access, sea access only at the beaches in front of the station. Stated purpose: geology, geophysics, glaciology, lakes, terrestrial biology. Climate: mean annual -2.3 °C, Feb 1.6, July -6.7, 511 mm, mean wind 42 km/h, max 92.6 km/h NW. Full log: `Research_Logs/Batch1_A2_Decepcion_GdC_Shirreff_Maldonado_Risopatron_2026-10-04.md`.

### 24. Russkaya  `russkaya`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | Russkaya Station / Estação Russkaya / Base Rússkaya / Russkaja / Stazione Russkaya |
| Coordinates (lat, lon) | -74.765726, -136.800072  *(source: comnap24)* |
| Largest source disagreement | 4.3 km |
| Elevation (m) | 126  *(source: comnap24)* |
| Type / detail | station / comnap24:Station / comnap17:Station / wikidata:Antarctic research station / wp_list:Summer |
| Status | summer-only  *(COMNAP 2024: Seasonal, Open)* |
| Status across sources | comnap24: COMNAP 2024: Seasonal, Open // comnap17: COMNAP 2017: operational period "October–March" |
| Years opened / closed | 1980 / n/a (active) |
| Capacity (winter / summer / peak) | unknown / 10 / 10 |
| Operator (context only) | Russia - Russian Antarctic Expedition ; Arctic and Antarctic Research Institute |
| Purpose as stated | science disciplines: FACILITIES INFRASTRUCTURE Area under roof (m2) 800 Area scientific laboratories (m2) 0 Type of scientific laboratories: None Conference room (capacity) Logistic area (m2) Number of beds 10 [...] |
| Surface | bare rock |
| Stability flag (sources only) | rock |
| Location text | Marie Byrd Land |
| Nearest city | Byrd, 712.9 km (CANDIDATE) |
| Nearest highway | hwy1, 595 km  *(lines good to about ±20 km)* |
| Inventory notes | COMNAP 2017 DMS: 74°45’00’’S 136°40’00’’W // COMNAP 2024 DDM: 74° 45.9436' S 136° 48.0043' W // Wikipedia inactive-list row at the same site: "Russkaya" (Closed, est 1980, closed 1990) // COMNAP 2017 permafrost: Continuous |
| Sources | COMNAP Facilities CSV (Nov 2024) ; COMNAP Station Catalog (Aug 2017) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -74.7657, -136.8001 (COMNAP 2024); spread under 4 km across sources (COMNAP 2017 rounded 74°45'S 136°40'W; AARI 74°46'S 136°50 to 52'W). Cape Burks. Elevation 124 to 134 m (126 COMNAP) | COMNAP; AARI Wayback 2015 |
| Surface verified (rock / ice / other) | **Rock.** AARI: "built on an outcrop of bedrock of biotite-hornblende gneiss forming a nunatak," about 4 km (NNE-SSW) by 1 km, central terraces, a levelled plateau with up to 26 m relief; colluvium and weathered debris, **frozen ground from about 20 cm**; four lakes up to 2 m deep freeze to the bottom. Mountain tops nearly snow-free; small glaciers between hills; coast is a snow-ice barrier 2 to 40 m high | AARI; COMNAP 2017 |
| Ice velocity (m/yr) | Not found (Hull Glacier velocity: died at the sources); not needed for a bedrock site. AARI notes some shrinking of glaciation near Cape Burks tied to wind erosion | dead end |
| Ice thickness (m) | n/a | n/a |
| Bed elevation (m) | n/a (rock) | n/a |
| Depth to bedrock below surface (m) | 0 at the nunatak; permafrost from about 20 cm | AARI |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **QUALIFIES (high).** Weak points: extreme wind (264 days/yr over 15 m/s, 136 over 30 m/s), a coastal barrier with avalanche risk for ships, permafrost (not a movement issue) | AARI |
| Status verified (year-round / summer / closed / abandoned) | **Mothballed (12 Mar 1990); seasonal field base.** Visits during conservation: Feb 2008 (53rd RAE), 2010, 2014, maybe 2016 (sources conflict). **Year-round reactivation announced for 2021 did not happen**; as of Mar 2025 AARI was still at technical studies (sites identified for a new winter complex, science pavilions and a landing area for long-range aircraft); AARI lists it as seasonal in Nov 2025; reason for the delay not found | AARI Mar 2025, Nov 2025; RGO 2020 |
| Year opened / year closed, verified | Attempts abandoned 1973 and 1979 after storms; station opened 9 Mar 1980 (25th SAE; 132 t cargo, 87 t fuel by helicopter); two aluminum-panel buildings 1984/85; conserved 12 Mar 1990 after cargo was lost from Mikhail Somov in a storm and budget problems | AARI; Rosgidromet |
| Capacity: winter / summer (persons) | 0 winter / 10 beds (peak 10), 800 m2, majority of facilities mothballed; planned winter staff 10 to 13 (RGO 2020); no capacity for the new complex found | COMNAP 2017; RGO |
| Buildings and infrastructure: state, power, water | Wooden panel buildings + two aluminum-panel buildings; diesel 220 V; 2006 to 08 inspection: diesel hall buried in snow, windows blown out, rooms full of ice; later mold in two main buildings and a collapsed medical-building roof; solar/wind automatic stations (2008). Planned: GLONASS ground station (Roscosmos; about 300 million rubles reported 2019, unverified). Satellite phone only; no helipad, no airstrip, no ship landing facilities | AARI; RGO; COMNAP |
| Landing/harbor/airstrip access | None built. Ship window only Feb to Mar (about 3 weeks a year); Mi-8 helicopters from the ship (Akademik Treshnikov in Feb 2022); a landing area for long-range aircraft is at the planning stage | AARI 2025 |
| Reachability from nearest city and highway (route, season) | Ship only; nearest city Byrd about 713 km; no air access today | AARI; inventory |
| Other facilities within 25 km | None: AARI calls Russkaya the only station on a coastal stretch of more than 1,500 km | AARI |

**Notes / dead ends / open questions:**

**Verdict: qualifies on rock; the only one of the three Russian-program stations with a documented, active revival effort (still unfunded as a build).** Stated purpose: fill the data gap left by Little America and Byrd; planned GLONASS/Roscosmos tracking, space weather, geophysics, hydrology; 67th RAE found 18 unstudied lakes (up to 8,500 m2; freshwater above 85 m). Climate: mean annual -12.4 °C (-46.4 min, +7.4 max), mean wind 12.9 m/s, max gust 77 m/s, 16 days of continuous 50 to 60 m/s storm during the 25th SAE; polar night 5 May to 9 Aug. Adélie colonies of 120 to 140 birds. Contradictions: COMNAP 2017 precipitation 1,977 mm looks like a data error; coast named Ruppert (Wikipedia) vs Hobbs (AARI, COMNAP). Open: why 2021 slipped; ATS EIA/inspection records; ice velocity. Full log: `Research_Logs/Batch1_A2_Leningradskaya_Russkaya_Parodi_2026-10-04.md`.

### 25. Shirreff Base  `shirreff-base`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | Shirreff / Base Shirreff / Base Cabo Shirreff |
| Coordinates (lat, lon) | -62.470400, -60.770800  *(source: wikidata:Q7498973)* |
| Largest source disagreement | 0.1 km |
| Elevation (m) | unknown  *(source: unknown)* |
| Type / detail | station / wikidata:Antarctic research station |
| Status | summer-only  *(Wikipedia list: summer-only active)* |
| Status across sources | wp_list: Wikipedia list: summer-only active |
| Years opened / closed | 1996 / n/a (active) |
| Capacity (winter / summer / peak) | unknown / 6 / unknown |
| Operator (context only) | United States - National Oceanic and Atmospheric Administration |
| Purpose as stated | Shirreff Base (original name Cape Shirreff Field Station) is a seasonal field station in the Southern Ocean operated by the U.S. National Oceanic and Atmospheric Administration (NOAA) and opened in 1996. It is [...] |
| Surface | unknown |
| Stability flag (sources only) | unknown |
| Location text | Cape Shirreff |
| Nearest city | Pergamino, 28.2 km (NEAR_CITY) |
| Nearest highway | hwy1, 187 km  *(lines good to about ±20 km)* |
| Inventory notes | none |
| Sources | Wikidata ; Wikipedia: Research stations in Antarctica (list) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | **The inventory row is the Chilean "Dr. Guillermo Mann" camp at Cape Shirreff, Livingston Island** (COMNAP -62.47015, -60.77118, a "Refuge", seasonal, est. 1991; 34 m from the inventory value). "Shirreff Base" is the Wikipedia name of the adjacent US NOAA camp (renamed Holt Watters Field Camp in 2023), about 50 m away; both lie inside ASPA 149 at the base of Condor Hill, 62°28.25'S 60°46.28'W. Elevation 15 m. The COMNAP 2017 catalogue's coordinates are the cape, 2.3 km off; the SCAR gazetteer has a wrong longitude (-58.47) | COMNAP; ASPA 149 plan [V] |
| Surface verified (rock / ice / other) | **Rock:** porphyritic basaltic lavas and minor breccias about 450 m thick (Late Cretaceous, K-Ar 90.2 ± 5.6 Ma); an ice-free peninsula of about 3.1 km2, mostly a raised marine platform at 46 to 53 m with lower platforms at 7 to 9 m and 12 to 15 m; the camp is on the east coast at 15 m; "the bedrock is largely covered by weathered rock and glacial deposits"; soils fine, porous ash and scoria | ASPA 149 plan, Measure 7 (2016) and Measure 12 (2023) |
| Ice velocity (m/yr) | Not found. The Livingston ice-cap margin lies south of the peninsula, retreating (cover 832 km2 in 1957 to 679 km2 in 2020, about 2.4 km2/yr); roughly 1 to 1.5 km from the camp (the agent's inference from the plan) | Anais Acad. Bras. Ciências 2024; log |
| Ice thickness (m) | n/a | n/a |
| Bed elevation (m) | n/a | n/a |
| Depth to bedrock below surface (m) | Shallow under weathered rock and glacial deposits; not measured | ASPA 149 plan |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **QUALIFIES (medium-high).** No landslide, erosion or flood problem reported; the US camp was rebuilt (2023/24) because 26 years of weather meant scientists spent up to 30% of their time on repairs (deterioration, not ground failure); 2023/24 winter damage: none to essential infrastructure; 4 to 14 ft of snow drifts | NOAA situation reports 2023/24, 2024/25 |
| Status verified (year-round / summer / closed / abandoned) | Seasonal, summer-only; buildings stay in place year-round. COMNAP: Seasonal, Open (Wikipedia says "Closed": conflict). 2023/24: all three camps (Cape Shirreff, Holt Watters, Chilean) inspected and opened, the Chilean camp used as extra housing and storage; US season 2024/25 began 11 Nov 2024. **Whether the Chilean camp itself is currently staffed is unresolved** | NOAA reports; COMNAP |
| Year opened / year closed, verified | Chilean studies from 1965 (intensive from 1982); fibreglass igloo 1990/91; camp opened Nov 1991; US camp 1996/97, rebuilt as the 2,000 ft2 Holt Watters Field Camp (three buildings plus a bird blind), completed 2023/24 | COMNAP 2017 p.30; NOAA |
| Capacity: winter / summer (persons) | Chilean camp: 6 to 8 (COMNAP peak 6; INACH 2009 maximum 6); US camp 7 (2024/25), 8 staff + a 13-person construction crew in 2023/24 | COMNAP; INACH 2009; NOAA |
| Buildings and infrastructure: state, power, water | Chilean: house, igloo, lab module, store, outhouse, quad; HF/VHF + sat phone; wind-generator tower "defunct" in the 2023 plan. US: berthing, galley, pinniped and seabird labs, emergency shelter/bird blind, comms tower, ATV shed; solar, propane heating, water collection; Weatherhaven tent; helicopter landing sites A and B; no fuel or food storage in the area except for essential purposes | ASPA 149 plan; NOAA |
| Landing/harbor/airstrip access | **No pier:** 178 full Zodiac loads were landed from the M/V Betanzos in 2023/24; two anchorages then small boats to Módulo Beach; helicopters discouraged 1 Nov to 31 Mar; vehicles only on the coastal strip; sea states 1 to 4 m | ASPA 149 plan; NOAA |
| Reachability from nearest city and highway (route, season) | US: M/V Betanzos from Punta Arenas (about 15 Nov); Chile: INACH. Nearest city Pergamino 28 km | NOAA; inventory |
| Other facilities within 25 km | None in COMNAP; Spanish Byers Field Camp about 27 km (two huts, summer), Juan Carlos I 29 km; ASPA 126 Byers Peninsula 20 km SW | computed |

**Notes / dead ends / open questions:**

**Verdict: qualifies (medium-high) but is a protected research site, not a settlement site.** ASPA 149 (originally SPA 11, 1966; HSM 59 San Telmo cairn inside): permit required; main facilities limited to within 200 m of the existing camps; helicopter route and landing limits; the camp must not interfere with the largest Antarctic fur seal colony in the Peninsula region (CEMP site no. 2). Stated purpose: fur seal and penguin monitoring (CCAMLR), Chilean fur seals, archaeology, weather, geology, glaciology. Climate (summers 2005/06 to 2009/10): mean 1.84 °C, max 19.9, min -8.1; mean wind 5.4 m/s; winter mean -6.7 °C; gusts to 62 mph (2024/25). **Inventory fix: relabel #25 as Cape Shirreff / Dr. Guillermo Mann (Chile) with the adjacent US Holt Watters camp.** Full log: `Research_Logs/Batch1_A2_Decepcion_GdC_Shirreff_Maldonado_Risopatron_2026-10-04.md`.


---

## Tier B1: Temporarily closed per COMNAP 2024

### 26. Brown  `brown`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | Almirante Brown Antarctic Base / Brown Antartic Base / Base Antártica Brown / Brown Base / Base Antártica Almirante Brown / base antarctique Almirante-Brown / Antarctische basis Almirante Brown / Base ammiraglio Brown / Almirante Brown / Estacion científica almirante brown / Almirante Brown Antarctische Basis / Stazione almirante Brown / Base almirante Brown / Base Brown |
| Coordinates (lat, lon) | -64.895370, -62.870452  *(source: comnap24)* |
| Largest source disagreement | 0.0 km |
| Elevation (m) | 22  *(source: comnap24)* |
| Type / detail | station / comnap24:Station / comnap17:Station / wikidata:Antarctic research station |
| Status | closed  *(COMNAP 2024: Temporarily Closed (seasonality Seasonal))* |
| Status across sources | comnap24: COMNAP 2024: Temporarily Closed (seasonality Seasonal) // comnap17: COMNAP 2017: operational period "October–March" // wp_list: Wikipedia list: summer-only active |
| Years opened / closed | 1951 / n/a (temporarily closed per COMNAP 2024) |
| Capacity (winter / summer / peak) | unknown / 8 / 12 |
| Operator (context only) | Argentina - Instituto Antártico Argentino ; Argentine Antarctic Institute |
| Purpose as stated | science disciplines: Meteorology, Oceanography |
| Surface | bare rock |
| Stability flag (sources only) | rock |
| Location text | Paradise Harbor |
| Nearest city | Puerto Abrigo, 30.2 km (NEAR_CITY) |
| Nearest highway | hwy1, 8 km  *(lines good to about ±20 km)* |
| Inventory notes | COMNAP 2017 DMS: 64°53’43.3’’S 62°52’13.6’’W // COMNAP 2024 DDM: 64° 53.7222' S 62° 52.2271' W // COMNAP 2017 permafrost: Discontinuous |
| Sources | COMNAP Facilities CSV (Nov 2024) ; COMNAP Station Catalog (Aug 2017) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -64.8954, -62.8705 confirmed (COMNAP 2024; COMNAP 2017 about 1 m off). Elevation 22 m. On Coughtrey Peninsula / Sanavirón Peninsula (Proa Head), a hook-shaped point at the north side of the entrance to Skontorp Cove | COMNAP; SCAR gazetteer |
| Surface verified (rock / ice / other) | **Rock** (qualified): steep sea-cliffs at least 100 m high on one side and the sheer face of a tidewater glacier on the east side; gentoo nests "on the bedrock below the ruins of the main derelict station building"; Marambio.aq: "a rocky massif with a hill of nearly 70 m"; COMNAP "Ice-free ground", discontinuous permafrost. Limited space ashore, linked by a narrow beach | Oceanites/EPA 2011 [V]; COMNAP 2017; marambio.aq [F] |
| Ice velocity (m/yr) | Not found (an adjacent tidewater glacier; calving swell is a known harbor hazard) | dead end |
| Ice thickness (m) | n/a | n/a |
| Bed elevation (m) | n/a (rock) | n/a |
| Depth to bedrock below surface (m) | At/near surface | Oceanites |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **QUALIFIES (medium-high).** Damage history is fire, not ice: July 1951 fire (rebuilt Jan 1952) and **12 Apr 1984 fire** (set by the station doctor who did not want to winter, per Wikipedia/Spanish accounts, unverified) destroyed the main house. No relocation, burial or landslide found | Fundación Marambio; Minuto Fueguino [F] |
| Status verified (year-round / summer / closed / abandoned) | **Not closed: staffed every Argentine summer.** The COMNAP "Temporarily Closed" flag is an off-season snapshot (the same CSV also lists Cámara and Primavera as "Open", though Cámara had been closed two years). 2022/23: 53 days, 11 people; 2025/26: early Jan to about 15 to 16 Mar, 11 people. Officially "temporary" since 1984 | argentina.gob.ar Mar 2026 [V]; Pampa Azul 2023 [F] |
| Year opened / year closed, verified | Naval Detachment Almirante Brown 6 Apr 1951; fire Jul 1951, rebuilt Jan 1952; Ortiz refuge 29 Jan 1956; closed Dec 1959; to the Argentine Antarctic Institute 29 Nov 1964; reopened 17 Feb 1965 as a permanent science station; 1984 fire; sporadic from 1988/89; 1995/96 two modular units; 1999/2000 new main house for 8; 2010/11 dock and AWS | COMNAP 2017; SCAR; marambio.aq [F] |
| Capacity: winter / summer (persons) | 0 winter / peak 12 (8 staff + 4 scientists), 178 m2 under roof (COMNAP lists "0 beds" [sic]); real crews 11 | COMNAP; argentina.gob.ar 2026 |
| Buildings and infrastructure: state, power, water | Main house (1999/2000), residence and lab modules, power plant, Ortiz refuge, jetty; 220 V fossil fuel; sat phone + VHF; 2 zodiacs; no medical staff (a 2010 casualty had to be treated by the GGV nurse); AWS since 2010/11; no helipad or airstrip. Fuel tanks "2 x 30,000 L" is Wikipedia-only | COMNAP 2017; 2012 inspection [V] |
| Landing/harbor/airstrip access | Sea only: icebreaker Irízar with Beach Group and EDPV landing craft; jetty; about 100 ship visits/yr (mostly tourist) | COMNAP 2017; argentina.gob.ar |
| Reachability from nearest city and highway (route, season) | By sea only; in practice González Videla (8 km) is the nearest help; Frei evacuation. Yelcho 33.7 km, Palmer 57.5 km. Nearest city Puerto Abrigo about 30 km | COMNAP; computed |
| Other facilities within 25 km | González Videla 8.0 km; Ortiz refuge 200 m; no other COMNAP facility within 25 km; HSM 30 and 56 are at GGV | ATS HSM list |

**Notes / dead ends / open questions:**

**Verdict: qualifies. Not closed: nothing to revive; year-round use is not planned** (it has been "temporary" since 1984; COMNAP 2017 mentions only renovation; the Wikipedia "complete renovation for year-round use" is unverified). Tourism: IAATO landings at "Brown Station" were 90 (2019/20), 40, 61, 65, 57 (2024/25); the only possible shore landing is at the station itself. Stated purpose: Paradise Bay coastal-environment research; 2026: mammals, birds, fish, IWC SORP cetaceans. Climate: mean annual -2.4 °C, July -6.9, mean wind 22 km/h W. **Correction:** a search summary's "17-person crew in 2024/25" is Primavera, not Brown. Full log: `Research_Logs/Batch1_A2_B1_Videla_Brown_Melchior_Carvajal_2026-10-04.md`.

### 27. Carvajal  `carvajal`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | Adelaide Island Station / Teniente Luis Carvajal Villaroel Antarctic Base / Station T / Adelaide Island (Base T) / Lieutenant Luis Carvajal Villarroel (SCTJ) / Base T / Base Carvajal / Base tenente Luis Carvajal Villaroel / Teniente Luis Carvajal Villaroel / Stazione Carvajal / Adelaide Island (Base T) /Brit./ |
| Coordinates (lat, lon) | -67.761322, -68.914815  *(source: comnap24)* |
| Largest source disagreement | 1.0 km |
| Elevation (m) | 92  *(source: comnap24)* |
| Type / detail | station / comnap24:Station / comnap17:Station / wikidata:Antarctic research station / wikidata:Antarctic research station / wp_list:Permanent / scar:unspecified |
| Status | closed  *(COMNAP 2024: Temporarily Closed (seasonality Seasonal))* |
| Status across sources | comnap24: COMNAP 2024: Temporarily Closed (seasonality Seasonal) // comnap17: COMNAP 2017: operational period "October–March" // wp_list: Wikipedia list: summer-only active // wp_list: Wikipedia list (inactive): "Closed, became Carvajal", closed 1977 // wikidata: Wikidata dissolved/closed 1977 |
| Years opened / closed | 1985 / n/a (temporarily closed per COMNAP 2024) |
| Capacity (winter / summer / peak) | unknown / 12 / 46 |
| Operator (context only) | Chile - Instituto Antártico Chileno ; United Kingdom - British Antarctic Survey |
| Purpose as stated | science disciplines: Atmospheric sciences, Environmental science, Geology, Geomorphology, Geophysics, Glaciology, Marine biology, Paleoecology, Pollution, Terrestrial biology |
| Surface | bare rock |
| Stability flag (sources only) | rock |
| Location text | Adelaide Island |
| Nearest city | Rothera, 40.1 km (NEAR_CITY) |
| Nearest highway | spur_rothera, 40 km  *(lines good to about ±20 km)* |
| Inventory notes | COMNAP 2017 DMS: 67°45’37.7’’S 68°54’53.4’’W // COMNAP 2024 DDM: 67° 45.6793' S 68° 54.8889' W // Wikipedia inactive-list row at the same site: "Station T" (Closed, became Carvajal, est 1961, closed 1977) // Wikipedia list has 2 rows merged here: Carvajal (summer_only_active 1984-); Station T (Closed, became Carvajal 1961-1977) // COMNAP 2017 permafrost: Discontinuous |
| Sources | COMNAP Facilities CSV (Nov 2024) ; COMNAP Station Catalog (Aug 2017) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) ; SCAR Composite Gazetteer (placenames.aq) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -67.7613, -68.9148 confirmed (COMNAP 2024; COMNAP 2017 94 m off; INACH 67°45'40.8"S 68°54'53.3"W; SCAR "Adelaide" -67.7667, -68.9167). **It is on the south tip of Adelaide Island (BAS Base T / Adelaide), not Leonie Island** (no gazetteer entry for any Leonie Island location); official name Teniente Luis Carvajal Villarroel. Elevation 4 m (COMNAP 2017, Wikipedia) vs 92 m (COMNAP 2024): unresolved | COMNAP; INACH [F]; SCAR [V] |
| Surface verified (rock / ice / other) | **Station pad: ice-free ground on a rock bluff** (Rivera et al. 2005: one of the ice-free areas on the southern edge, "much more stable" there; slope steepens at the contact with the rock outcrop near the station; adjacent Avian Island 1.2 km away is Late Cretaceous volcaniclastic sandstone). **Ice runway: on a local ice divide of the Fuchs Ice Piedmont** and unusable | Rivera 2005, Ann. Glaciol. 41:57 to 62 [F]; ASPA 117 plan [V] |
| Ice velocity (m/yr) | Near the runway "smaller than the errors"; maximum 9 ± 0.5 cm/day (about 33 m/yr) at both margins of the divide; glacier front grounded or nearly so; 1976 to 2001 area loss averaged 1.1 km2/yr; summer melt arrives earlier each year and crevasses open earlier | Rivera 2005 [F] |
| Ice thickness (m) | Not found (ice-runway area spans sea level to 325 m) | Rivera 2005 |
| Bed elevation (m) | Not found | dead end |
| Depth to bedrock below surface (m) | Station on a rock bluff (shallow); not measured | Rivera 2005; blog (low reliability) |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **Split: station pad QUALIFIES (medium), skiway FAILS.** The closure was the runway: a 2002 Valdivia scientific-center study found cracks in the landing zone; BAS left in 1977 because of the skiway, not the buildings. No report of the station itself moved, buried or threatened | Rivera 2005; La Tercera [F] |
| Status verified (year-round / summer / closed / abandoned) | **Real closure.** Chile ran it in summers on Twin Otter ski aircraft; stopped on the unusable ice runway (dates disputed: 2004 per glaciologia.cl; 2014 per La Tercera and Radio Polar; the 2014/15 season per FACh). **Reopening announced** (Feb 2025 inspection said full-capacity reopening possible; recovery team Dec 2025; activation scheduled Jan 2026). **No source confirms the Jan 2026 activation happened.** No wintering | FACh via Meganoticias/CNN Chile Nov 2025 [F]; Pauta Sep 2026 (silent) |
| Year opened / year closed, verified | BAS Base T / Adelaide 3 Feb 1961 to 1 Mar 1977 (chosen over Rothera Point for a better skiway); transferred to Chile 14 Aug 1984; Chilean station established Jan 1985 (SCAR; ASPA plan says summer-only since 1982); two INACH labs built 2017 (materials by icebreaker Viel in one operation) | SCAR [V]; INACH 2017 [F] |
| Capacity: winter / summer (persons) | COMNAP: 46 beds (12 staff + 34 scientists), 770 m2; ASPA 117 plan: "up to 10 personnel"; FACh 2025: 12 people (10 uniformed + 2 civilians); press: about 200 m2 facility. Winter 0 | COMNAP; ASPA 117 [V]; FACh [F] |
| Buildings and infrastructure: state, power, water | BAS-era huts (Stephenson, Rymill, Hampton Houses, 1967 plastic block; Wikipedia); a 2012 blog describes leaking roofs and doors that no longer close (low reliability); INACH dry and wet labs (2017) and a sensor-network station; fossil fuel + renewables listed; loader, quad, skidoos, zodiacs; helipad yes; no ship landing facilities | COMNAP 2017; INACH [F] |
| Landing/harbor/airstrip access | No pier ("Ship landing facilities: None"): cargo by boat and landing craft in swell-exposed conditions; ski runway unusable; helipad | COMNAP 2017; INACH 2017 |
| Reachability from nearest city and highway (route, season) | Ship (icebreaker Viel and others; 2 visits/yr) or helicopter; Punta Arenas 1,698 km (COMNAP) or 2,002 km. Rothera 39.6 km, Dirck Gerritsz Lab 39.7 km, Turkish camp 70.9 km, San Martín 86.1 km. **Nearest city is Rothera (39.6 km), a city in the project** | COMNAP; computed |
| Other facilities within 25 km | Avian Island (ASPA 117) 1.2 to 1.6 km, with two abandoned refuges (Chilean Comodoro Guesalaga 1962/63; Argentine "Paso de los Andes" 1957) and a 1998 beacon. No other COMNAP facility within 25 km. No HSM found; no tourist traffic found | ASPA 117 plan [V] |

**Notes / dead ends / open questions:**

**Verdict: the only genuine closure in the group. Station pad qualifies; the access (ice runway) fails.** Revival realism (evidence only): a 12-person FACh reconditioning of about 200 m2 is announced with no plan for the ice runway; a US$80 million, 3,400 m2 INACH base (68 summer / 25 winter, 7 labs) was announced for 2026 in 2023, has slipped (INACH Jun 2025: should become a joint "Base Científica Conjunta" for all four Chilean operators, funding to be sought); a Sep 2026 article says Carvajal and Yelcho replacements follow the Escudero rebuild, construction 2028/29 to 2033. ASPA 117 (Avian Island, Measure 2 (2018)): permit only, no aircraft landings, about 35,000 Adélie pairs; a copy of the plan must be kept at Carvajal. Climate: mean annual -9.8 °C, July -17.8, 621 mm, max wind 174 km/h NE. **Corrections:** Leonie Island is not the location; Carvajal is not "Prof. Julio Escudero" (a different Chilean station on King George Island). Full log: `Research_Logs/Batch1_A2_B1_Videla_Brown_Melchior_Carvajal_2026-10-04.md`.

### 28. Kohnen  `kohnen`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | Kohnen Station / Estação Kohnen / Kohnen-Station / base antarctique Kohnen / Estación Kohnen / Stazione Kohnen / Kohnen Base / Base Kohnen |
| Coordinates (lat, lon) | -75.001909, 0.066336  *(source: comnap24)* |
| Largest source disagreement | 0.2 km |
| Elevation (m) | 2892  *(source: comnap24)* |
| Type / detail | station / comnap24:Station / comnap17:Station / wikidata:Antarctic research station / scar:Station |
| Status | closed  *(COMNAP 2024: Temporarily Closed (seasonality Seasonal))* |
| Status across sources | comnap24: COMNAP 2024: Temporarily Closed (seasonality Seasonal) // comnap17: COMNAP 2017: operational period "October–March" // wp_list: Wikipedia list: summer-only active |
| Years opened / closed | 2000 / n/a (temporarily closed per COMNAP 2024) |
| Capacity (winter / summer / peak) | unknown / 4 / 28 |
| Operator (context only) | Germany - Alfred Wegener Institute ; Alfred Wegener Institute for Polar and Marine Research |
| Purpose as stated | science disciplines: Atmospheric chemistry and physics, Climate change, Climatology, Geodesy, Geophysics, Glaciology |
| Surface | ice sheet |
| Stability flag (sources only) | ice_sheet_interior |
| Location text | Queen Maud Land |
| Nearest city | Troll, 340.9 km (CANDIDATE) |
| Nearest highway | hwy7, 341 km  *(lines good to about ±20 km)* |
| Inventory notes | COMNAP 2017 DMS: 75°00’06’’S 00°04’04’’E // COMNAP 2024 DDM: 75° 0.1145' S 0° 3.9802' E // COMNAP region: Dronning Maud Land // COMNAP 2017 permafrost: None |
| Sources | COMNAP Facilities CSV (Nov 2024) ; COMNAP Station Catalog (Aug 2017) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) ; SCAR Composite Gazetteer (placenames.aq) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -75.0019, 0.0663 (COMNAP); AWI paper 75°00'06"S 0°04'04"E (borehole 75°00'09"S 0°04'06"E, 2,892 m WGS84, 10 Jan 2001); ATS EIA 75°00'00"S 0°04'00"E. Elevation 2,892 m | COMNAP; Oerter et al. 2009 (Polarforschung 78) |
| Surface verified (rock / ice / other) | **Ice: the East Antarctic plateau; no surface rock** (nearest rock about 181 km away). Bedmap3: grounded ice 2,760 m thick, surface 2,879 m, bed +119 m; AWI: 2,782 ± 10 m of ice and snow | Bedmap3; Oerter 2009; COMNAP 2017 |
| Ice velocity (m/yr) | **GPS: 0.756 m/yr toward 273.4° at the drill site** (Wesche et al. 2007; the mean of 12 survey points is 0.74 m/yr); the site is "in the immediate vicinity of a transient and forking ice divide". ITS_LIVE gives 2.5 to 3.3 m/yr for 2022 to 2025 but cannot resolve speeds this low, so treat 2 to 3 m/yr as an upper bound | Oerter 2009; Wesche 2007 (abstract via summary); ITS_LIVE |
| Ice thickness (m) | 2,760 to 2,782 m | Bedmap3; Oerter 2009 |
| Bed elevation (m) | About +110 to +119 m above sea level | Bedmap3; the agent's subtraction |
| Depth to bedrock below surface (m) | About 2,760 to 2,780 m (the EPICA core reached 2,774.15 m on 16 Jan 2006) | Oerter 2009 |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **PASSES the speed test (high confidence on speed; moderate-high on thickness): bedrock is 2.8 km down but there is no surface rock.** Real issue is snow, not flow: accumulation about 64 kg/m2/yr (about 0.16 to 0.18 m/yr, 1.6 to 1.8 m per decade); the platform on 16 pillars must be raised about every second year (last raised 2021/22; in 2023/24 raising was not possible for lack of a hydraulic cylinder) | Oerter 2009; AWI BzPM 767, 796 |
| Status verified (year-round / summer / closed / abandoned) | **Mothballed summer camp, opened only every two to three years.** COMNAP "Seasonal, Temporarily Closed". AWI reports: open 2018/19; closed 2019/20 and 2020/21; open 2021/22 (traverse about 3 Dec 2021, closed 24 Jan 2022); "not opened" 2022/23; open 2023/24 (6-person team from 19 Dec; "left winterised" 20 Jan 2024; trench cleared and closed); "not opened" 2024/25; 2025/26 not found. **No AWI document states a reason for the closure.** AWI keeps renewing its annual permit and lists Kohnen in the 2028/29 call for proposals; one 2025/26 permit is mislabeled "wintering" | AWI BzPM 733 to 807; ATS EIA 2010 to 2836; AWI proposals page |
| Year opened / year closed, verified | Built over 1999/2000 and 2000/2001; put into operation 11 Jan 2001 (COMNAP: year 2000); EPICA drilling four summers from 2001/02, ending 16 Jan 2006; CoFi (Coldest Firn) project since 2012/13 | Oerter 2009; AWI |
| Capacity: winter / summer (persons) | 0 winter / COMNAP: 8 beds, peak 28 (4 staff + 2 scientists in summer), 160 m2; AWI "up to 20 researchers"; designed for 20 permanent plus 5 to 7 short-term during drilling | COMNAP 2017; Oerter 2009; AWI |
| Buildings and infrastructure: state, power, water | Eleven 20-ft ISO containers on a steel platform on 16 pillars (about 32 by 8 m; some from the dug-out Filchner Station); drill/science trench 66 m long, 4.8 m wide, 6 m deep; diesel (engine replaced 2021/22; generator repaired 2023/24); snow melter fed from the roof; water system replaced with copper pipes 2023/24; email, sat phone, VHF; an AWI automatic weather station since 2021/22 | Oerter 2009; AWI BzPM 767, 796 |
| Landing/harbor/airstrip access | Snow runway (1,200 m per Oerter; 2,000 by 20 m per COMNAP: unresolved) | Oerter 2009; COMNAP |
| Reachability from nearest city and highway (route, season) | Traverse from Neumayer III: 750 to 760 km, about 10 to 11 days, up to six PistenBully vehicles (about 400 L fuel per tonne per 1,000 km); or Basler BT-67 / Dornier 228 / Polar 5/6; DROMLAN serves it. About four technicians are needed to open the station. Great-circle: Neumayer III 554 km, Troll 341 km, SANAE IV 381 km, Halley VI 719 km. Nearest city Dome Fuji about 340 km | Oerter 2009; AWI |
| Other facilities within 25 km | None. Within a few km: AWS9 (Utrecht, 1997 to 2008) and a replacement AWS, snow-height gauges, boreholes B32 to B52, the airstrip. Nearest other nation's facility about 330 km (Svea, temporarily closed 332 km) | Oerter 2009 |

**Notes / dead ends / open questions:**

**Verdict: passes the speed test; it is a mothballed summer camp, not a candidate for a year-round post** on the evidence (opens every two to three years; needs a 10-day diesel traverse and about four technicians; trench emptied and closed in 2023/24). Stated purpose: logistics base for the EPICA deep core (EDML), refueling for plateau flights, CoFi since 2012/13. Climate: mean annual -42.2 °C (COMNAP; -44.6 °C at 10 m in 1997/98), winter to -70 °C, summer never warmer than -17 °C, midnight sun 31 Oct to 12 Feb; altitude 2,892 m (higher medical incidents noted in BzPM 758). No plan to restart deep drilling; the successor project is at Little Dome C near Concordia (summary only). Open: the 2025/26 AWI report; why closed; seasons 2016/17 to 2017/18. Full log: `Research_Logs/Batch1_A2_Halley_Jinnah_Kohnen_2026-10-04.md`.

### 29. Melchior  `melchior`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | Base Melchior / Melchior Antartic Base / Base Antártica Melchior / Melchior-Station / Destacamento Naval Melchior / Stazione Melchior |
| Coordinates (lat, lon) | -64.325705, -62.976329  *(source: comnap24)* |
| Largest source disagreement | 0.9 km |
| Elevation (m) | 4  *(source: comnap24)* |
| Type / detail | station / comnap24:Station / comnap17:Station / wikidata:Antarctic research station |
| Status | closed  *(COMNAP 2024: Temporarily Closed (seasonality Seasonal))* |
| Status across sources | comnap24: COMNAP 2024: Temporarily Closed (seasonality Seasonal) // comnap17: COMNAP 2017: operational period "October–March" // wp_list: Wikipedia list: summer-only active |
| Years opened / closed | 1947 / n/a (temporarily closed per COMNAP 2024) |
| Capacity (winter / summer / peak) | unknown / 12 / 15 |
| Operator (context only) | Argentina - Instituto Antartico Argentino ; Argentine Antarctic Institute |
| Purpose as stated | science disciplines: Terrestrial biology |
| Surface | rock and ice |
| Stability flag (sources only) | ice_shelf_or_glacier_or_sea_ice (needs velocity test) |
| Location text | Melchior Islands |
| Nearest city | Puerto Abrigo, 59.7 km (NEAR_CITY) |
| Nearest highway | spur_puerto_abrigo, 60 km  *(lines good to about ±20 km)* |
| Inventory notes | COMNAP 2017 DMS: 64°19’54.2’’S 62°58’58.0’’W // COMNAP 2024 DDM: 64° 19.5423' S 62° 58.5797' W // COMNAP 2017 permafrost: Continuous |
| Sources | COMNAP Facilities CSV (Nov 2024) ; COMNAP Station Catalog (Aug 2017) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | Good to about 1 km only: COMNAP 2024 -64.3257, -62.9763 vs COMNAP 2017 -64.3317, -62.9828 (about 740 m apart); SCAR puts it on Gamma Island (Isla Observatorio), NE end, south of Gallows Point (-64.3333, -62.9833); use the SCAR description. Elevation 4 m (COMNAP) vs 8 m (Argentine sources) | COMNAP; SCAR gazetteer [V] |
| Surface verified (rock / ice / other) | **UNCLEAR (conflict).** For rock: Argentine sources "rocky terrain", the 1947 build needed blasting; COMNAP features "Bird colonies, Coast, Rock". For ice: COMNAP 2017 "built on Ice-sheet, Moraine", permafrost continuous; Oceanites "many low, ice-covered islands"; Spanish Wikipedia (Pierrou 1970) says the island is 2 km long, 140 m high, "completely covered by a thick layer of ice" with ice-cliff coasts | COMNAP 2017 [V]; marambio.aq; Pierrou (secondary) |
| Ice velocity (m/yr) | Not found | dead end |
| Ice thickness (m) | Not found | dead end |
| Bed elevation (m) | Not found | dead end |
| Depth to bedrock below surface (m) | Not found (regional Anvers-Melchior block: volcanics plus granite/diorite/tonalite, summary only) | dead end |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **UNCLEAR (low confidence).** The 1947 prefab base has stood about 80 years with no reported relocation or ice damage (mild evidence), but it sits at sea level beside an ice-capped island and the surface-type question must be settled first | Log |
| Status verified (year-round / summer / closed / abandoned) | **Not closed: opened each Argentine summer.** The COMNAP "Temporarily Closed" flag is an off-season snapshot. 2017/18: 54 days, 11 people; 2022/23: 22 days, 7 people; 2024/25 hydrographic and buoy work; 2025/26 opened with Hydrography staff installing AIS equipment. (An opposition draft resolution in 2026 says Matienzo and Melchior were not operated "for years": political, unverified) | Casa Rosada 2018; Pampa Azul 2023 [F]; argentina.gob.ar 2026 |
| Year opened / year closed, verified | Established 31 Mar 1947 (SCAR: 31 Jan 1947), built in 47 days; main Antarctic weather-forecast source in 1952; astronomical station 1955; IGY tide gauge 1957/58; closed as a permanent base 30 Nov 1961; reopened 1968/69 for hydrographic and marine biology work; seasonal since | Fundación Marambio [F]; SCAR |
| Capacity: winter / summer (persons) | 0 winter / 15 beds (peak 15: 12 staff); 336 m2 under roof; "maximum 36" in Asociación Polar conflicts; real crews 7 to 11 | COMNAP; Asociación Polar [F] |
| Buildings and infrastructure: state, power, water | Lab, lounge, kitchen, food store, workshop; 5 structures (2018); 6 m2 infirmary with a paramedic; pier/jetty; 2 zodiacs; 220 V fossil fuel; sat phone + VHF; waste, hazardous-waste and fuel-spill capability listed; no helipad, no airstrip. Lambda Island lighthouse (1942, still lit) nearby | COMNAP 2017 [V]; IPIEC |
| Landing/harbor/airstrip access | Sea only: icebreaker Irízar, aviso ARA Puerto Argentino or ARA Canal Beagle; 5 ship visits/yr (Dec to Feb) | COMNAP; argentina.gob.ar |
| Reachability from nearest city and highway (route, season) | By sea only. Nearest: GGV 55.7 km, Brown 63.5 km, Yelcho 67.7 km, Palmer 71.6 km. Nearest city Puerto Abrigo about 60 km | computed from COMNAP |
| Other facilities within 25 km | None in COMNAP; HSM 29 (Primero de Mayo lighthouse, Lambda Island, 1942) in the same island group | ATS HSM list [V] |

**Notes / dead ends / open questions:**

**Verdict: unclear; already operated every summer, so "revival" is moot.** The decision that matters is the surface type (rock vs ice-covered island). Stated purpose: terrestrial biology (botany) per COMNAP, historically hydrographic surveys; 2025/26 AIS installation. Climate: mean annual -2.9 °C (COMNAP) or -3.6 °C, July -9.5, max wind 222 km/h NW, 1,308.7 mm precipitation, snow-free only in January. Protected areas: none beyond HSM 29; "dangerous, difficult or impossible to access; appropriately visited only by zodiac cruising" (Oceanites). A tourist report calling it "abandoned many years ago" reflects an off-season visit. Open: Pierrou source, a station-level geology paper, ice-cap velocity. Full log: `Research_Logs/Batch1_A2_B1_Videla_Brown_Melchior_Carvajal_2026-10-04.md`.


---

## Tier B2: Closed since 2000, plausibly revivable

### 30. Arturo Parodi Station  `arturo-parodi-station`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | Arturo Parodi / Teniente Arturo Parodi Alister Base / Base Teniente Arturo Parodi Alister / Teniente Arturo Parodi / Base antarctique Teniente Arturo Parodi Alister / Base Arturo Parodi |
| Coordinates (lat, lon) | -80.305556, -81.344167  *(source: wikidata:Q19754242)* |
| Largest source disagreement | 1.6 km |
| Elevation (m) | 983  *(source: wikidata)* |
| Type / detail | station / wikidata:Antarctic research station / wp_list:Summer / scar:Station |
| Status | closed  *(Wikipedia list (inactive): "Dismantled", closed 2014)* |
| Status across sources | wp_list: Wikipedia list (inactive): "Dismantled", closed 2014 |
| Years opened / closed | 1999 / 2014 |
| Capacity (winter / summer / peak) | unknown / unknown / unknown |
| Operator (context only) | Chile - Instituto Antártico Chileno |
| Purpose as stated | Teniente Arturo Parodi Alister Base was a Chilean Antarctic research base located in the claimed Chilean Antarctic Territory |
| Surface | unknown |
| Stability flag (sources only) | unknown |
| Location text | Ellsworth Land |
| Nearest city | Byrd, 713.0 km (CANDIDATE) |
| Nearest highway | hwy22, 339 km  *(lines good to about ±20 km)* |
| Inventory notes | none |
| Sources | Wikidata ; Wikipedia: Research stations in Antarctica (list) ; SCAR Composite Gazetteer (placenames.aq) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | **The inventory point (-80.3056, -81.3442) is the old Chilean Parodi / INACH Huneeus base at Patriot Hills, NOT Union Glacier.** Position sources: Wikipedia 80°18'15"S 81°23'13"W; Spanish Wikipedia 80°18'S 81°22'W; architects 80°19'S 81°18'W (855 m); Wikidata three variants. **Elevation 855 to 880 m; the 983 m in the inventory is unsourced.** Union Glacier (EPCCGU) is a different place about 67 km straight-line (95 km by traverse), with positions varying up to about 7 km E-W across sources | Wikidata Q19754242; ARQZE; COMNAP Nov 2024 |
| Surface verified (rock / ice / other) | **Ice.** Old Parodi: snowfield 800 m north of the Patriot Hills blue-ice area, about 2 m of hardened snow on blue ice; ice several hundred metres thick (radar about 400 m at the BIA centre, about 600 m at 2.5 km, 700 m per architects). Union Glacier: mean ice thickness 1,450 m (max 1,540 m near the camp), bed down to -858 m | Rivera et al. 2014 (The Cryosphere 8:1445); Casassa 2004; ARQZE |
| Ice velocity (m/yr) | Patriot Hills area: about 5 m/yr (stake P9, 1995), 13 m/yr at Horseshoe Valley margins up to 25 m/yr at the centre, about 20 m/yr at the valley centre; BIA near equilibrium. **Union Glacier: 20.5 m/yr at the camp (stake B11), 20.9 to 22.9 m/yr nearby, runway BIA mean 20 m/yr (11 to 24)**; 33 to 35 m/yr upstream | Rivera 2014; Rivera 2010; Casassa 2004 |
| Ice thickness (m) | Union Glacier 1,450 to 1,540 m; old Parodi about 400 to 700 m | Rivera 2014; Casassa 2004 |
| Bed elevation (m) | Union Glacier minimum -858 m (a -190 m pinning point lies upglacier of the grounding line) | Rivera 2014 |
| Depth to bedrock below surface (m) | Hundreds to over 1,400 m (see thickness); Patriot Hills itself is an exposed rock massif, but the station sat about 1 km from it, on snow over ice | Casassa 2004; ARQZE |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **FAILS (medium-high).** Union Glacier moves about 200 m per decade toward the Ronne Ice Shelf; the Chilean program itself treats the station as non-permanent (skis, domes dug out each season; the old station was deliberately dismantled and moved) | Rivera 2014; Diálogo Sur 2025 |
| Status verified (year-round / summer / closed / abandoned) | **Parodi: dismantled in the 2013 season** (32 men and 1 woman, 21 days, 120+ t of ice and snow shoveled out, left 8 Dec 2013). Its tunnel and domes were reused at Union Glacier. **EPCCGU (Chilean joint station, Union Glacier): seasonal, "fully operational" in 2025/26** (about Nov to Jan); no source shows anyone wintering (a "12 to 15 winter staff" claim is unverified) | El Pinguino 2013; Infogate 2026 |
| Year opened / year closed, verified | Chilean campaigns at Patriot Hills from 1995 (INACH); Parodi opened 1996 (ALE) or 7 Dec 1999 (Spanish Wikipedia); dismantled 2013; EPCCGU inaugurated 4 Jan 2014 (Piñera); ALE moved to Union Glacier 2007/08, runway certified Dec 2008, main operations from Nov 2010 | Casassa 2004; ALE; INACH |
| Capacity: winter / summer (persons) | Old Parodi: 24 initial (six 4-person modules), 25 per Wikipedia, design maximum 100. EPCCGU: INACH lists 8 researchers (about one-month campaign); a 2012 inspection said up to 50 scientists; modernization Dec 2025 (five Sustérmica modules), a 60-researcher design is unverified. ALE camp: up to 70 guests (Wikipedia says 160) | ARQZE; INACH; ALE |
| Buildings and infrastructure: state, power, water | Old Parodi: 50 m tunnel plus six Igloo Cabin modules. EPCCGU: salvaged tunnel re-erected in a crevasse-free zone; 2025 five modules on skis (about 80 cm above the surface), generator + photovoltaic; the settlement is mostly tents and two domes dug out each season; kitchen, infirmary, dormitories planned in three phases. Union Glacier blue-ice runway 3,000 m by 50 m (SCGC), 60-seat B757 capable | USM; Diálogo Sur 2025; ALE |
| Landing/harbor/airstrip access | Blue-ice runway only (air; Punta Arenas flights about 4.25 h, about weekly Nov to Jan); Patriot Hills kept as a backup runway | ALE |
| Reachability from nearest city and highway (route, season) | Air only; Patriot Hills to Union Glacier 95 km by traverse (Wikipedia 70, USM 150: unresolved). Nearest city Byrd about 713 km | El Pinguino; ALE |
| Other facilities within 25 km | Union Glacier: ALE camp and runway within about 10 km of each other; Patriot Hills: the old ALE camp about 1 km (now backup). Nothing else documented | Rivera 2014 |

**Notes / dead ends / open questions:**

**Verdict: remove from the batch as a "recently closed, revivable" station.** **Identity trap:** the inventory row is the dismantled Patriot Hills base; the live Chilean station is Union Glacier (EPCCGU), a different place; both are on moving ice and fail the project test (about 20 m/yr on 1.4 to 1.5 km of ice). **Revival realism (evidence only):** the old site was deliberately dismantled in 2013 and moved, so there is nothing at Patriot Hills except a backup blue-ice runway; EPCCGU is being upgraded but remains a summer tent-and-dome settlement dug out each season; no wintering plan confirmed. **Developer decision:** drop #30 (and do not substitute Union Glacier). Stated purpose: runway logistics, glaciology, meteorology, microbiology, support for Chilean and international science (Air Force Twin Otters supported Vinson and Schanz work in 2025/26). Climate: annual mean about -20 °C; katabatic gust 150 km/h recorded 29 Dec 1999; hazards: crevasses at the runway and Gifford Peaks passage, burial by drifting snow. Open: ATS APA database not queried; the Chilean Air Force primary page was blocked. Full log: `Research_Logs/Batch1_A2_Leningradskaya_Russkaya_Parodi_2026-10-04.md`.

### 31. Sarie Marais  `sarie-marais`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | none found |
| Coordinates (lat, lon) | -72.030850, -2.807350  *(source: wikidata:Q15219717)* |
| Largest source disagreement | 2.3 km |
| Elevation (m) | 1089  *(source: wikidata)* |
| Type / detail | station / wikidata:research station / wp_list:Summer |
| Status | closed  *(Wikipedia list (inactive): "Closed, decommissioned", closed 2001)* |
| Status across sources | wp_list: Wikipedia list (inactive): "Closed, decommissioned", closed 2001 // wikidata: Wikidata dissolved/closed 1999 |
| Years opened / closed | 1982 / 2001 |
| Capacity (winter / summer / peak) | unknown / unknown / unknown |
| Operator (context only) | South Africa - South African National Antarctic Programme |
| Purpose as stated | research station in Antarctica |
| Surface | unknown |
| Stability flag (sources only) | unknown |
| Location text | Ahlmann Ridge |
| Nearest city | Sanay, 40.5 km (NEAR_CITY) |
| Nearest highway | hwy7, 39 km  *(lines good to about ±20 km)* |
| Inventory notes | none |
| Sources | Wikidata ; Wikipedia: Research stations in Antarctica (list) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -72.0309, -2.8074 (inventory); not in COMNAP 2024 or SCAR as "Sarie Marais". World Antarctic Postal 72°02'00"S 02°48'00"W (0.5 km off; low authority); Wikipedia 72°01'35"S 2°48'18"W. **At Grunehogna (Ahlmannryggen), NOT near "Fuchs Dome"** (the Shackleton Range, about 1,142 km away). Elevation 1,047 m (WAP) vs about 1,213 m (agent's REMA lookup; 1 km box 1,025 to 1,300 m) | WAP; Wikipedia (lead); SCAR; REMA (own computation) |
| Surface verified (rock / ice / other) | **Unclear, leaning rock/nunatak.** Grunehogna Peaks are exposed Mesoproterozoic Ritscherflya Supergroup sediments (about 2,000 m with sills) over the Archaean Grunehogna craton (summary only); the base was also called "Grunehogna Mountain Base"; ITS_LIVE cannot tell rock from slow ice | SCAR; WAP; summaries (unverified) |
| Ice velocity (m/yr) | **ITS_LIVE (agent's computation): 6.4 m/yr at the inventory pixel; median 5.0 m/yr within 2 km;** the whole 6 km box is under 12 m/yr (96% under 10 m/yr); nearest pixel at 3 m/yr or less is 620 m away (the Wikipedia coordinate gives 430 m and 27 m for 5 m/yr). Ice thickness, accumulation and burial rate: not found | Log (S15) |
| Ice thickness (m) | Not found | dead end |
| Bed elevation (m) | Not found | dead end |
| Depth to bedrock below surface (m) | Not found | dead end |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **UNCLEAR.** Slow ice (under 12 m/yr) rather than a proven rock site; stability is not the concern: there is nothing left to assess | Log |
| Status verified (year-round / summer / closed / abandoned) | **Decommissioned 2001/02 and recycled** (Cooper 2006: structures at decommissioned Dronning Maud Land bases not buried by ice were recycled, Sarie Marais named as an earlier example); absent from COMNAP 2024. Radio operation documented 14 Jan 1992 | Cooper 2006; WAP |
| Year opened / year closed, verified | Erected 1982/83 for geology, geophysics and surveying; decommissioned 2001/02 (Wikipedia citing Cooper 1991 and the ATS 2003/04 exchange, neither opened); in 1971 a prefabricated hut was put up at Grunehogna when a team could not reach Borga Base (unverified) | Wikipedia (lead); Cooper 2006 |
| Capacity: winter / summer (persons) | Not found | dead end |
| Buildings and infrastructure: state, power, water | Not found beyond "summer base used in support of geological parties"; current condition unknown | WAP |
| Landing/harbor/airstrip access | Overland from SANAE III (200 km, unverified); today DROMLAN flights land at Troll airfield, 184 km away | Cooper 2006; COMNAP |
| Reachability from nearest city and highway (route, season) | SANAE IV (Vesleskarvet) 40 km; Troll 184 km; nearest city Sanay about 41 km | computed |
| Other facilities within 25 km | None found; SANAE IV 40 km; Troll 184 km; a COMNAP-listed "SANAP Summer Station" (est. 2010) 248 km away, identity unverified | COMNAP; computed |

**Notes / dead ends / open questions:**

**Verdict: not a revivable station. Decommissioned and recycled by policy; recommend moving #31 out of tier B2** (developer decision). Cooper suggested Robertskollen as ASPA-worthy; no protected area found at Grunehogna. The WAP "250 km inland from SANAE" conflicts with the geometry (40 km to SANAE IV). Open: Cooper 1991 and the ATS 2003/04 exchange not opened; current condition unknown. Full log: `Research_Logs/Batch1_A2_B2_Molodezhnaya_MtVechernyaya_DruzhnayaIV_Soyuz_SarieMarais_2026-10-04.md`.

### 32. Soyuz  `soyuz`

**From the inventory** *(do not hand-edit)*

| Field | Value |
|---|---|
| Alternate names | Soyuz Station / Sojuz / Base Soyuz |
| Coordinates (lat, lon) | -70.576577, 68.794937  *(source: comnap24)* |
| Largest source disagreement | 0.1 km |
| Elevation (m) | 336  *(source: comnap24)* |
| Type / detail | station / comnap24:Station / wikidata:Antarctic research station / wp_list:Permanent |
| Status | closed  *(COMNAP 2024: Temporarily Closed (seasonality Seasonal))* |
| Status across sources | comnap24: COMNAP 2024: Temporarily Closed (seasonality Seasonal) // wp_list: Wikipedia list (inactive): "Closed", closed 2007 |
| Years opened / closed | 1982 / 2007 |
| Capacity (winter / summer / peak) | unknown / unknown / 30 |
| Operator (context only) | Russia ; Soviet Union - Soviet Antarctic Expedition ; Arctic and Antarctic Research Institute |
| Purpose as stated | Soyuz Station is a Russian (formerly Soviet) Antarctic research station, located on the shores of Beaver Lake, 260 km off Prydz Bay on the Lars Christensen Coast of the Mac Robertson Land in East Antarctica. |
| Surface | unknown |
| Stability flag (sources only) | unknown |
| Location text | Prince Charles Mountains |
| Nearest city | Shirayuki, 309.8 km (CANDIDATE) |
| Nearest highway | hwy22, 180 km  *(lines good to about ±20 km)* |
| Inventory notes | COMNAP 2024 DDM: 70° 34.5946' S 68° 47.6962' E // Wikipedia inactive-list row at the same site: "Soyuz" (Closed, est 1982, closed 2007) // COMNAP region: East Antarctica |
| Sources | COMNAP Facilities CSV (Nov 2024) ; Wikidata ; Wikipedia: Research stations in Antarctica (list) |

**To fill in** *(verified findings only; source and date on every line)*

| Field | Value | Source / date |
|---|---|---|
| Coordinate verified (lat, lon) | -70.5766, 68.7949 (COMNAP); AARI/Australia 70°35'S 68°47'E (1-minute precision, about ±1 km). "Exposed low rock ridge of Jetty Peninsula on the eastern shore of Beaver Lake". **Elevation conflict: 336 m (AARI, COMNAP) vs about 35 m at the inventory pixel in the agent's REMA lookup**; 336 m would match a ridge position, not the inventory point | COMNAP; AARI Wayback 2016; Aus. 2010; REMA (own computation) |
| Surface verified (rock / ice / other) | **Rock** (Jetty Oasis; shield rock with alkaline-ultramafic dykes and pipes; moraine; next to Stagnant Glacier; Beaver Lake is a smooth-ice lake 11.3 by 8 km): "exposed low rock ridge"; geology from a search summary (unverified) | Aus. 2010; AARI; SCAR (AADC) |
| Ice velocity (m/yr) | **ITS_LIVE (agent's computation): 2.2 m/yr at the station pixel; median 1.0, max 3.2 m/yr within 500 m; median 3.6 m/yr within 3 km; about 65% of the 12 km window at 5 m/yr or less;** fast ice about 70 m/yr only on the NW edge | Log (S15) |
| Ice thickness (m) | Not found | dead end |
| Bed elevation (m) | Not found | dead end |
| Depth to bedrock below surface (m) | Surface rock ridge; not measured | Log |
| Stability verdict vs. `DR-52` (qualifies / fails / unclear) | **QUALIFIES on ground (moderate; the position is uncertain).** The problem is the state of the buildings, not the ground | Log |
| Status verified (year-round / summer / closed / abandoned) | **Abandoned (not recently closed).** AARI: opened 3 Dec 1982 (28th SAE), **closed 28 Feb 1989**; the inventory's "closed 2007" is not supported (secondary sources only say reconditioning plans from 2006/07 were "not carried out"); 18 Jan 2010 inspection: unoccupied, "no evidence of use in recent years"; no source found on any use after 2010. COMNAP 2024 still says "Temporarily Closed" | AARI Wayback 2016; Aus. 2010 |
| Year opened / year closed, verified | Opened 3 Dec 1982; closed 28 Feb 1989; absent from the 2017 COMNAP Russia catalogue | AARI; COMNAP 2017 |
| Capacity: winter / summer (persons) | Main staff 33 in 1987 (ru.wikipedia, unverified); COMNAP peak 30 | COMNAP |
| Buildings and infrastructure: state, power, water | 2010: about 12 plywood huts in a line along the ridge with weather damage, snow and ice inside, delaminating plywood, collapsed elements, broken windows; unsecured empty drums, open waste containers, localized fuel spills, obsolete equipment; inspectors called it "a high environmental risk" to the peninsula and Beaver Lake with waste "not recoverable" and "a substantial loss of utility as a seasonal station" | Aus. 2010 (ATCM34 IP39) |
| Landing/harbor/airstrip access | Soviet era ice airfield (aerogeophysics Il-14 and An-2 based at Soyuz, Druzhnaya-4 and Progress); Beaver Lake used by ANARE Beaver aircraft from 1957; no runway dimensions or surface found | PMGRE; SCAR (AADC) |
| Reachability from nearest city and highway (route, season) | Supplied from Druzhnaya IV in the Soviet era; nearest city Mawson 316 km, Shirayuki 310 km | AARI; inventory |
| Other facilities within 25 km | Australia's Beaver Lake field site (70°47'S 68°17'E, est. 1995) about 30 km (outside 25 km); nothing else; nearest COMNAP facility Druzhnaya IV 208 km | SCAR; computed |

**Notes / dead ends / open questions:**

**Verdict: not a "recently closed" station: closed 1989, derelict by 2010. Revival realism (evidence only): the 2010 inspectors recommended securing or removing the structures and remediating the site; Russian planning documents stress Russkaya, not Soyuz. Recommend moving #32 out of tier B2** (developer decision). Stated purpose: summer geological and geophysical work in the Prince Charles Mountains, aviation weather. Climate (AARI): January mean -3.1 °C, extremes +3.5 / -23 °C, winds 5 to 9 m/s (gusts to 30). Full log: `Research_Logs/Batch1_A2_B2_Molodezhnaya_MtVechernyaya_DruzhnayaIV_Soyuz_SarieMarais_2026-10-04.md`.
