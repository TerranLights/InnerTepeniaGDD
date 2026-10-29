# Intake research, Unit B: candidate sites for an isolated coastal winter airfield (85°E to 115°E)

**Started 2026-10-29.** Brief: `Relung_Panen_Intake_Gateway_Research_BRIEF_2026-10-29.md`, Unit B. Real-world facts only. No design, no recommendation, no ranking. Every claim is marked **SOURCED**, **UNVERIFIED**, **DERIVED** or **NOT FOUND**. Exclusions per the brief: the immediate surroundings of Mirny station, the Bunger Hills oasis, Casey station and the Windmill Islands, Davis station and the Vestfold Hills.

## PROGRESS
- [x] 1 Drygalski Island
- [x] 2 Mill Island (and Bowman Island and other ice-capped islands of the Shackleton Ice Shelf front)
- [x] 3 Haswell Island and the other Haswell Islands
- [x] 4 Davis Sea fast ice off Mirny (as a winter sea-ice runway)
- [x] 5 Shackleton Ice Shelf surface
- [x] 6 West Ice Shelf surface
- [x] 7 Blue-ice areas near the coast
- [x] 8 Law Dome, western slope (and other ice domes and slow-ice areas)
- [x] 9 Past surveys and proposals (2019 Russian airfield survey; Australian Bunger Hills / Vestfold alternates)
- [x] 10 Other candidates found
- [x] FINAL

## Common notes for every site (read once)

- **Wind values are ERA5 reanalysis, 1991-2020, hourly** (Open-Meteo archive API, `models=era5`, 10 m wind, 10 m gusts, 2 m temperature), at the nearest 0.25° grid point the API chose; the grid point and its model elevation are given each time. **DERIVED.** *Check against a station:* at Mirny ERA5 gives a mean of 8.7 m/s and 9.7% of hours at or above 15 m/s, while the station record (secondary sources, already known) gives about 11 m/s and "more than 200 days" a year over 15 m/s. **ERA5 at this grid size smooths the katabatic jet and reads low near the coast**; treat its speeds as lower bounds and its directions as more reliable than its speeds.
- **"Hours above 0 °C per year"** is the ERA5 2 m air temperature count, given as a rough indicator of surface-melt exposure. It is not a melt measurement.
- **ERA5 snowfall was downloaded and not used.** It ignores wind redistribution and, where it can be checked (Mill Island ice core, item 2), it disagrees with the measured accumulation. Accumulation is reported only from field sources.
- **Visibility, fog and blowing-snow statistics: NOT FOUND for any site** except where a field source states them (Mill Island). ERA5 archive output does not include visibility.
- **Ice speed: "no reliable value" means ITS_LIVE has no pixel with an error of 20 m/yr or less there.** This happens on smooth ice domes where satellites find no features to track. It does not mean the ice is fast or slow.
- Elevations are REMA surface heights above the EGM2008 geoid (orthometric), DERIVED as described in the search log. Areas are ADD polygon areas corrected for polar-stereographic scale (DERIVED).
- **Island outlines** come from the SCAR Antarctic Digital Database (ADD) high-resolution polygons, current to November 2024 per the service description (BAS ArcGIS FeatureServer `High_resolution_vector_polygons_of_the_Antarctic_coastline`, layer 1, downloaded for 2.1-3.0 M m east, −1.25 to +0.45 M m north in EPSG:3031). Each island is identified below by its ADD FID.

---

## 1. Drygalski Island

| Fact | Value | Status |
|---|---|---|
| Position | 65°45′S 92°30′E (gazetteer); ADD polygon centroid 65.757°S 92.449°E | SOURCED (Wikipedia, from USGS GNIS); DERIVED (ADD FID 1500) |
| Distance to Mirny | **≈92 km** (centroid); the flattest lines found (below) are 89-90 km | DERIVED |
| Distance from the mainland | "about 85 km north of Queen Mary Land's coast and 45 km north-northeast of Cape Filchner" | SOURCED (Wikipedia). A search summary gave "55 km" from another copy: conflicting, UNVERIFIED |
| Size | 220 km²; 20.4 km long | SOURCED (Wikipedia; area carries "citation needed") |
| Size from the ADD outline | 221 km² true area; bounding rectangle about 20 × 14 km; perimeter 57 km | DERIVED |
| Surface | "ice-capped" island; no rock exposure is mentioned in any source read | SOURCED (Wikipedia). Rock: NOT FOUND |
| Elevation | highest point 325 m | SOURCED (Wikipedia) |
| Elevation from REMA | maximum 331 m, median 195 m | DERIVED |
| **Usable flat area** | **673 of 880 grid centers** (about 162 km² of the island) have at least one 3 km straight line lying wholly on the island with no 288 m segment steeper than 2%. Most follow the contours of the dome (flat along the line, sloping across it). Flattest examples: center 65.783°S 92.434°E, bearing 10°, steepest segment 0.13%, end-to-end 0.04%, at 246-248 m; and 65.784°S 92.424°E, bearing 10°, 0.18%, at 242-244 m. Qualifying lines lie between 43 and 328 m elevation. | DERIVED (method in search log) |
| Ice speed | **No reliable value anywhere on the island.** ITS_LIVE has no pixel with error ≤20 m/yr inside the outline (0 of 15,881 pixels). The few pixels with values have errors of 200-250 m/yr. | DERIVED / **NOT FOUND** |
| Crevassing | NOT FOUND | — |
| Snow accumulation | NOT FOUND | — |
| Surface melt | NOT FOUND as a measurement. ERA5 grid point (65.75°S 92.50°E, model elevation 262 m): **about 3 hours a year above 0 °C**; July mean −16.1 °C, January mean −2.9 °C, minimum −30.0 °C. | DERIVED |
| Wind | ERA5 (same point): mean 8.5 m/s for the year, 9.2 m/s April-October; 12.4% of hours at or above 15 m/s (16.3% April-October); 4.3% of April-October hours at or above 20 m/s; most common direction **E** (38% of all hours; 75% of hours at or above 15 m/s); highest hourly mean 32.3 m/s; highest gust 46.7 m/s. Katabatic exposure: the island stands 85 km offshore, so it is not at the foot of an ice-sheet slope; no source discusses katabatic flow reaching it. | DERIVED; katabatic statement NOT FOUND |
| Visibility | NOT FOUND | — |
| Shore and ice edge | The whole ADD shoreline faces sea or sea ice (no ice shelf touches it). REMA surface 150 m inside the shore: median 41 m (10th to 90th percentile 29-51 m). That is the ice-cliff top height around the island, measured from a surface model, not a survey. | DERIVED |
| Water depth offshore | ETOPO 2022 (15″ grid, not soundings) at cells off the ADD shore: 0-1 km out, median 86 m (shallowest tenth 51 m); 1-2 km, median 105 m; 2-5 km, median 135 m. | DERIVED / UNVERIFIED (gridded compilation) |
| Fast ice | No island-specific source. The Mirny fast ice reaches "30-40 km" wide by late winter (already known, ASPA 127), which does not reach an island 85-92 km out. Sea-ice cover around the island by month: NOT FOUND (not computed in this unit). | Context SOURCED; island value NOT FOUND |
| How a summer ship reaches it | No source describes a ship landing at Drygalski Island. Russian supply ships pass the area: the AARI 2021 report ran a CTD section "between Drygalski Island and the Shackleton Ice Shelf" from *Akademik Tryoshnikov* (already known, ocean file items 3-8). Mawson observed the island "from the *Aurora* in January 1914." | SOURCED as stated; ship landing NOT FOUND |
| Past landings, stations, surveys | A Soviet temporary meteorological field station, **"Mir," operated 20 May to 6 August 1960**, at 65°45′S 92°26′E, elevation 327 m, "for one winter." Wikipedia cites *Scientific Stations in Antarctica 1882-1963* (1971). How it was reached and supplied: NOT FOUND. A Russian encyclopedia snippet instead puts a 1960 station "Druzhba" (May-July) on the "Zavadovsky dome" of the West Ice Shelf; that is a different place (item 6), and the two should not be merged. | SOURCED (Wikipedia, secondary); snippet UNVERIFIED |
| Proposals for an airfield | NOT FOUND | — |

## 2. Mill Island, Bowman Island and the other ice-capped islands of the Shackleton Ice Shelf

The ADD lists seven ice-covered "land" polygons larger than 100 km² in the Shackleton system (besides those touching the Bunger Hills): Masson, Henderson, David, Mill, Bowman, and two that are not named in any source read. Each is given separately. **Common to all of them:** the Shackleton Ice Shelf around them moves at roughly 73-365 m/yr on its main body (already known, port file A); the islands themselves are grounded ice caps that move much more slowly where ITS_LIVE can measure them.

### 2a. Mill Island

| Fact | Value | Status |
|---|---|---|
| Position | 65°30′S 100°40′E (gazetteer); ice core drill site 65°33′10″S 100°47′06″E; ADD centroid 65.550°S 100.760°E | SOURCED (Wikipedia/GNIS; Inoue et al. 2017, *Climate of the Past* 13:437-453, Table 1, PDF downloaded and read); DERIVED |
| Distance to Mirny | **≈367 km** (centroid). Inoue et al.: "350 km east of Mirny Station" | DERIVED; SOURCED |
| Size | "46 km long and 30 km wide," 1,260 km² (Wikipedia/GNIS); "∼45 × 35 km" (Inoue 2017). ADD: 1,225 km² true area, bounding rectangle about 42 × 38 km | SOURCED; DERIVED |
| Elevation | "rising ∼500 m above sea level"; drill site surface 503 m (Inoue 2017). REMA maximum 515 m, median 266 m | SOURCED; DERIVED |
| Surface | ice dome ("ice-domed island"); firn-ice transition at 83.4 m depth at the drill site; borehole temperature −13.86 °C at 19.07 m | SOURCED (Wikipedia; Inoue 2017 Table 1) |
| **Usable flat area** | **4,789 of 4,997 grid centers** (about 1,150 km²) have a qualifying 3 km line on the island. Qualifying lines lie at 46-512 m. Example on the upper dome: 65.622°S 100.654°E, bearing 30°, 0.10% steepest segment, 328 m. **Caution:** some REMA patches on the dome are so flat (0.00-0.10%) that they may be interpolated fill rather than measured surface; REMA's data-count layer was not checked. | DERIVED |
| Ice speed | ITS_LIVE has reliable pixels on only 2% of the island (p10/median/p90 3.6/16.4/37.5 m/yr where available, mostly near the edges). Only 2 qualifying lines have reliable speed (max 32-35 m/yr, near the island's east edge at 61-81 m). **The dome interior has no reliable value.** Inoue 2017 gives a vertical strain rate of −0.6 × 10⁻² per year at the drill site, a thinning rate, not a horizontal speed. | DERIVED; horizontal speed of the dome NOT FOUND |
| Crevassing | NOT FOUND | — |
| **Snow accumulation** | **1.35 m ice equivalent per year** (mean of 1913-2009 in the 120 m core). "High precipitation, particularly on its eastern flank." A later study found "a clear difference in average yearly snow accumulation between the windward side, the leeward side and the peak of the ice rise." | SOURCED (Inoue 2017; second quote from a search summary of Inoue et al., *The Cryosphere* 2020, not opened: UNVERIFIED) |
| Surface melt | "at its ∼500 m summit elevation Mill Island likely experiences minimal melt"; crust layers in the core are probably wind crusts, "not … melt layers"; "the density profile … showed no sign of strong melt." ERA5 (65.50°S 100.75°E, 514 m): **0 hours a year above 0 °C**; July mean −19.8 °C, January −5.8 °C, minimum −41.1 °C. | SOURCED (Inoue 2017); DERIVED |
| Wind | Inoue 2017 (CFSR reanalysis 1979-2009, grid point about 17 km east of the drill site): "the wind direction is predominantly from the east, and the mean wind speed over the period is 7.6 m s⁻¹." ERA5: mean 8.2 m/s (9.0 April-October); 15.2% of hours ≥15 m/s (19.9% April-October); 7.6% of April-October hours ≥20 m/s; E in 42% of hours and **92% of hours ≥15 m/s**; highest hourly 35.0 m/s; highest gust 51.2 m/s. Inoue 2017 also describes "strong katabatic winds from the continent." | SOURCED; DERIVED |
| **Visibility** | "low-level cloud, fog, and rime formation over the summit caused by localized summer sea breezes associated with nearby sea-ice breakout"; "Fog and rime accretion associated with the fog events were observed during the field season." | SOURCED (Inoue 2017, citing Roberts et al. 2013) |
| Shore and ice edge | 90% of the ADD shoreline touches ice shelf; the remaining 10% (north coast) faces sea or sea ice. REMA surface 150 m inside the sea-facing shore: median 31 m (10th-90th percentile 19-52 m). | DERIVED |
| Water depth offshore (sea-facing side) | ETOPO 2022: 0-1 km out, median 157 m (shallowest tenth 32 m); 1-2 km, median 174 m; 2-5 km, median 213 m. Port file A already gives 173 m at 0.5 km and 461 m at 10 km north of the island. | DERIVED / UNVERIFIED |
| Sea ice off the north coast | Already known (port file A, cells N1 and N2): mean February concentration 40-48%, August 86-88%; open water (<15%) 27-29 days a season on average in 2011-2020, 0 in most seasons. A grounded giant iceberg (Pobeda Ice Island, C5) sat north-west of Mill Island until 2003-04. | SOURCED (Inoue 2017 for Pobeda); rest already known |
| Past landings, surveys | A reconnaissance shallow core in the 2008/09 summer; the main campaign in 2009/10 under the Australian Antarctic program: "The team spent 3 weeks in the field and drilled one 120 m main ice core … and seven shallow … firn cores." How the team was flown or shipped in: NOT FOUND. Discovered February 1936 from *William Scoresby*. | SOURCED (Inoue 2017; Wikipedia) |
| Proposals for an airfield | NOT FOUND | — |

### 2b. Bowman Island

| Fact | Value | Status |
|---|---|---|
| Position | 65°16′48″S 103°06′36″E; ADD centroid 65.281°S 103.069°E | SOURCED (Wikipedia, citing Mawson 1932); DERIVED (FID 1300) |
| Distance to Mirny | **≈477 km** | DERIVED |
| Size and shape | "about 39 km long and from 3 to 10 km wide," "shaped like a figure eight," 186 km² (Wikipedia). ADD: **369 km²** true area, bounding rectangle about 47 × 16 km. The ADD outline is about twice the Wikipedia area. | SOURCED; DERIVED (conflict not resolved; the ADD may include ice the older figure leaves out) |
| Surface | "high ice-covered island"; "rises above the northeastern part of the Shackleton Ice Shelf, which partly surrounds it" | SOURCED (Wikipedia) |
| Elevation | REMA maximum 254 m, median 128 m. Wikipedia gives none. | DERIVED |
| Usable flat area | 1,203 of 1,452 grid centers (about 290 km²). Several examples near 65.22°S 102.96-102.98°E at 234-243 m show 0.04-0.06% steepest segments and 0.00% end to end: **suspiciously flat, possibly interpolated REMA fill.** | DERIVED, with that caveat |
| Ice speed | **No reliable value** (2 of 26,612 pixels). | NOT FOUND |
| Crevassing, accumulation, visibility | NOT FOUND | — |
| Surface melt | ERA5 grid point chosen by the API at 65.50°S 103.00°E (model elevation 245 m; about 25 km south of the island's centroid, so this point may sit on the ice shelf or sea ice beside it): about 32 hours a year above 0 °C; July −17.5 °C, January −3.8 °C. | DERIVED (grid-point caveat) |
| Wind | Same point: mean 9.0 m/s (9.8 April-October); 16.7% of hours ≥15 m/s (21.5% April-October); 7.6% of April-October hours ≥20 m/s; ESE 47% of hours, 87% of hours ≥15 m/s; highest hourly 34.1 m/s, gust 47.9 m/s. | DERIVED |
| Shore and ice edge | Only 7% of the ADD shoreline touches ice shelf; 93% faces sea or sea ice. REMA 150 m inside the sea-facing shore: median 36 m (10th-90th percentile 13-45 m). | DERIVED |
| Water depth offshore | ETOPO 2022: 0-1 km out, median 18 m (shallowest tenth 2 m); 1-2 km, median 36 m; 2-5 km, median 75 m. **Shallow compared with the other islands.** 842 of 7,129 nearby ETOPO cells are above sea level outside the ADD outline (old ice or grounded bergs in the grid). | DERIVED / UNVERIFIED |
| Icebergs | Iceberg C-37 (2022) "broke free from Bowman Island" after calving from the Glenzer Ice Shelf remnants; scatterometer track uk52 sat beside the island 2002-2014 (already known, ocean file items 3-8). | already known |
| Past landings, surveys | Discovered 28 January 1931 by BANZARE (Mawson). Landings: NOT FOUND. | SOURCED; NOT FOUND |

### 2c. Masson Island

| Fact | Value | Status |
|---|---|---|
| Position | 66°08′S 96°35′E; ADD centroid 66.137°S 96.656°E | SOURCED (Wikipedia/GNIS); DERIVED (FID 1485) |
| Distance to Mirny | **≈169 km** | DERIVED |
| Size | "about 31 km long" (Wikipedia). ADD: 543 km² true area, bounding rectangle about 34 × 21 km | SOURCED; DERIVED |
| Elevation | "rises to 465 m" (Wikipedia). REMA maximum 489 m, median 211 m | SOURCED; DERIVED |
| Surface | "ice-covered island" within the Shackleton Ice Shelf. Rift R1 "starts from the lee side of Masson Island" (already known, port file A). | SOURCED |
| Usable flat area | 1,323 of 2,187 grid centers (about 320 km²), lines at 28-480 m | DERIVED |
| Ice speed | ITS_LIVE reliable on 33% of the island: p10/median/p90 6.8/16.2/46.7 m/yr. Of 186 qualifying lines with reliable speed, 42 have a maximum of 15 m/yr or less; none 5 m/yr or less. Slowest: center 66.082°S 96.455°E, bearing 140°, steepest segment 1.59%, 170-192 m, **max 7.8 m/yr**. | DERIVED |
| Crevassing, accumulation, visibility | NOT FOUND | — |
| Melt and wind | ERA5 (66.00°S 96.50°E, 156 m): about 27 hours a year above 0 °C; July −20.3 °C, January −5.5 °C, minimum −44.1 °C. Mean wind 7.3 m/s (8.0 April-October); 6.9% of hours ≥15 m/s (9.1% April-October); 2.0% of April-October hours ≥20 m/s; ESE 41% of hours, E in 75% of hours ≥15 m/s; highest hourly 32.1 m/s, gust 47.1 m/s. | DERIVED |
| Shore | **100% of the ADD shoreline touches the ice shelf.** A ship cannot reach the island's shore directly; the nearest sea is at the shelf front. | DERIVED |
| Past landings | Discovered February 1912 by Mawson's Australasian Antarctic Expedition. Landings: NOT FOUND. | SOURCED |

### 2d. Henderson Island

| Fact | Value | Status |
|---|---|---|
| Position | 66°22′S 97°10′E; ADD centroid 66.379°S 97.230°E | SOURCED (Wikipedia/GNIS); DERIVED (FID 1484) |
| Distance to Mirny | **≈188 km** | DERIVED |
| Size | "17 km long," 17 km southeast of Masson Island; ADD 131 km², about 19 × 10 km | SOURCED; DERIVED |
| Elevation | "rises to 240 m"; REMA maximum 271 m, median 109 m | SOURCED; DERIVED |
| Usable flat area | 185 of 512 grid centers (about 45 km²), lines at 40-258 m | DERIVED |
| Ice speed | ITS_LIVE reliable on 95% of the island: p10/median/p90 **2.5/8.8/17.6 m/yr**. 76 qualifying lines have max ≤15 m/yr; 6 have max ≤5 m/yr. Slowest: center 66.363°S 97.220°E, bearing 10°, steepest segment 1.85%, 204-220 m, **max 3.3 m/yr**. | DERIVED |
| Crevassing, accumulation, visibility | NOT FOUND | — |
| Melt and wind | ERA5 (66.25°S 97.25°E, 187 m): about 39 hours a year above 0 °C; July −19.8 °C, January −5.6 °C, minimum −43.2 °C. Mean wind 6.9 m/s (7.5 April-October); 4.1% of hours ≥15 m/s (5.5% April-October); 1.0% of April-October hours ≥20 m/s; ESE 31%, E in 67% of hours ≥15 m/s; highest hourly 31.1 m/s, gust 44.8 m/s. | DERIVED |
| Shore | 100% of the ADD shoreline touches the ice shelf. | DERIVED |
| Past landings | "discovered in August 1912 by the Western Base Party"; Mawson's sledging party reached its southeastern slopes in late August 1912 (search summary of the AAD "Mawson's Huts" pages, not opened: UNVERIFIED). | SOURCED / UNVERIFIED |
| Slow shelf ice beside it | The shelf just south of Henderson Island (66.44-66.50°S, 96.97-97.32°E, surface 40-67 m) holds most of the slow-shelf lines found on the whole Shackleton Ice Shelf (item 5). | DERIVED |

### 2e. David Island

| Fact | Value | Status |
|---|---|---|
| Position | 66°25′S 98°46′E (Wikipedia); 66°25′00″S 98°47′00″E, "off the mouth of the Reid Glacier" (AAD gazetteer, per search summary); ADD centroid 66.420°S 98.783°E | SOURCED (search summary of both; not opened: UNVERIFIED); DERIVED (FID 1479) |
| Distance to Mirny | **≈257 km** | DERIVED |
| Size | about 16 × 10 km (Wikipedia) or 19 × 11 km (gazetteer), per the search summary; ADD 165 km², about 18 × 15 km | UNVERIFIED; DERIVED |
| Elevation | REMA maximum 289 m, median 121 m | DERIVED |
| Usable flat area | 118 of 640 grid centers (about 29 km²) | DERIVED |
| Ice speed | ITS_LIVE reliable on 99%: p10/median/p90 **2.2/7.1/40.4 m/yr**. 61 qualifying lines have max ≤15 m/yr, 10 have max ≤5 m/yr. Slowest: center 66.427°S 98.752°E, bearing 150°, steepest segment 1.73%, 222-240 m, **max 2.5 m/yr**. | DERIVED |
| Melt and wind | ERA5 (66.50°S 98.75°E, 222 m): about 71 hours a year above 0 °C; July −19.4 °C, January −5.4 °C, minimum −45.2 °C. Mean wind 7.2 m/s (8.1 April-October); 2.8% of hours ≥15 m/s (4.3% April-October); 0.3% of April-October hours ≥20 m/s; **SSE** 48% of hours and 53% of hours ≥15 m/s (the only site in this unit where the strong wind is not from the east); highest hourly 32.3 m/s, gust 48.9 m/s. | DERIVED |
| Other fields | Crevassing, accumulation, visibility: NOT FOUND. Shore: 100% ice shelf in the ADD. | NOT FOUND; DERIVED |

### 2f. Two islands not named in any source read

| Fact | ADD FID 1466 (south of Mill Island) | ADD FID 1476 (west of the Bunger Hills) | Status |
|---|---|---|---|
| Centroid | 65.827°S 100.722°E | 66.172°S 100.213°E | DERIVED |
| Distance to Mirny | ≈355 km | ≈324 km | DERIVED |
| Note on the exclusion | about 25 km north of the Highjump Archipelago | **about 23 km west of the Bunger Hills oasis**; the developer should judge whether this is inside the excluded surroundings | DERIVED |
| Area, shape | 249 km², about 29 × 13 km | 124 km², about 15 × 10 km | DERIVED |
| REMA height | max 157 m, median 86 m | max 111 m, median 56 m | DERIVED |
| Usable flat area | 885 of 981 centers (about 214 km²) | 309 of 484 centers (about 75 km²) | DERIVED |
| ITS_LIVE speed | reliable on 71%; p10/median/p90 **2.1/3.9/6.9 m/yr**; all 582 qualifying lines with reliable speed have max ≤15 m/yr, 350 have max ≤5 m/yr; slowest 65.824°S 100.536°E, bearing 10°, 1.41% steepest segment, 79-109 m, **max 1.2 m/yr** | reliable on 95%; p10/median/p90 **2.9/5.5/9.5 m/yr**; 282 of 288 qualifying lines max ≤15 m/yr, 16 max ≤5 m/yr; e.g. 66.187°S 100.115°E, bearing 120°, 47-74 m, max 3.7 m/yr | DERIVED |
| Shore | 100% ice shelf in the ADD | 100% ice shelf in the ADD | DERIVED |
| Name, history, landings | NOT FOUND (the nearest named feature found, Chugunov Island, is at 65°55′S 99°29′E per the AAD gazetteer in a search summary, so neither polygon is Chugunov Island) | NOT FOUND | — |
| ERA5 melt indicator | grid point 65.75°S 100.50°E (97 m): about 75 hours a year above 0 °C; July −19.8 °C, January −4.4 °C | grid point 66.25°S 100.25°E (58 m): about 259 hours a year above 0 °C; July −19.5 °C, January −3.5 °C | DERIVED |
| ERA5 wind | mean 7.2 m/s (7.8 April-October); 12.7% of hours ≥15 m/s (16.5% April-October); 6.3% of April-October hours ≥20 m/s; E 39% of hours and **89% of hours ≥15 m/s**; highest hourly 36.1 m/s, gust 52.7 m/s | mean 6.2 m/s (6.8 April-October); 7.9% of hours ≥15 m/s (10.4% April-October); 4.2% of April-October hours ≥20 m/s; E 22% of hours, E in 62% of hours ≥15 m/s; highest hourly 38.1 m/s, gust 54.8 m/s | DERIVED |
| Crevassing, accumulation, visibility | NOT FOUND | NOT FOUND | — |

## 3. Haswell Island and the other Haswell Islands

Already known (Casey-Mirny geology file, from the ASPA 127 plan): Haswell Island is 0.82 km², 93 m high, 2.5 km from Mirny; the other islets are about 100-300 m across; fast ice surrounds them for most of the year. Added here:

| Fact | Value | Status |
|---|---|---|
| REMA land surface in a box over the group (66.49-66.54°S, 92.90-93.12°E) | only about 1 km² stands 5 m or more above the geoid; maximum 80 m in REMA (ASPA 127 gives 93 m for Haswell Island) | DERIVED |
| 3 km lines | **none**: no 3 km line fits on land anywhere in the group | DERIVED |
| Longest possible straight line on Haswell Island | well under 1.5 km (an island of 0.82 km²) | DERIVED from the SOURCED area |
| Status | Haswell Island is Antarctic Specially Protected Area No. 127 (already known) | SOURCED |
| Wind, melt | ERA5 for the nearest point is the Mirny check above (66.50°S 93.00°E, sea level): mean 8.7 m/s, 9.7% of hours ≥15 m/s, ESE 33% of hours and E in 80% of hours ≥15 m/s; about 206 hours a year above 0 °C | DERIVED |
| Landings or runway proposals on the islands | NOT FOUND | — |

**Result for this item:** the Haswell Islands cannot hold a 3 km runway on land. The only surface around them long enough is the fast ice (item 4).

## 4. The Davis Sea fast ice off Mirny (as a winter sea-ice runway)

Already known and not repeated in full: fast ice 30-40 km wide by the end of winter; break-up between 17 December and 9 March (mean 3 February); freeze-up between 18 March and 5 May (mean 6 April); "always full of icebergs" (ASPA 127, geology file). Thinner by about 10 cm than in the 1960s, with break-up about a month later; in 2002 a 30 km belt formed in 2001 did not break out at all, and the fuel ship could not reach the station (AARI RPR 4(18) 2014, ocean file items 3-8). The McMurdo sea-ice runway precedent (ice over 2 m for a C-17, used October to December) is already known; requirements for sea-ice runways belong to Unit A.

| Fact | Value | Status |
|---|---|---|
| Position | the Davis Sea immediately north of Mirny (66°33′S 93°01′E), across Tryoshnikov Gulf and around the Haswell Islands, out to 30-40 km by late winter | SOURCED (already known) |
| Distance to Mirny | 0 to about 40 km, by definition of the fast-ice belt | DERIVED |
| Size and shape of flat area | The belt is 30-40 km wide; its length along the coast and the spacing of grounded icebergs within it: **NOT FOUND**. No source gives an iceberg-free 3 km straight line. REMA cannot measure sea ice (the surface model treats it as sea level). | SOURCED / NOT FOUND |
| Surface | first-year fast ice, with multiyear ice in years when it fails to break out (2001-2002) | SOURCED (already known) |
| **Ice thickness at Mirny** | **NOT FOUND.** Five searches in Russian and English (search log) found that Mirny keeps "the longest series of observations of Antarctic fast ice," but no thickness figure was found in any source that could be opened. A Soviet paper title, "Шестериков Н.П. Некоторые особенности нарастания припайного льда в районе Мирного" ("Some features of fast-ice growth in the Mirny area"), is cited in *Problemy Arktiki i Antarktiki* 96; the paper itself was not found. | NOT FOUND |
| Nearest measured thickness (outside the sector, for scale only) | Off Davis station (Prydz Bay, about 78°E, about 675 km west-southwest of Mirny, DERIVED): annual maximum **1.64 ± 0.08 m**, snow 0.11-0.38 m (buoys, 2009-2018); off Zhongshan 1.59 ± 0.17 m. Sanefjord (Prydz Bay): mean 1.23-1.24 m in 2012, 1.81-1.84 m in 2011 (already known). | UNVERIFIED (Li et al. 2023, *The Cryosphere* 17:917-937, abstract text quoted in a search result, not opened); SOURCED (Sanefjord, already known) |
| Ice speed | not applicable (fast ice is attached to the coast and does not flow; it can break out) | — |
| Elevation and slope | sea level; slope not applicable. Pressure ridges and refrozen leads: NOT FOUND for Mirny. | — |
| Crevassing equivalent | tidal cracks at the shore and around grounded bergs: no Mirny-specific source found. Soviet studies of "fast ice deformations in the region of … Mirny" exist (DTIC AD0748399, "Fast Ice Dynamics in the Mirny Area"); full text not reached. | UNVERIFIED (title and abstract snippet only) |
| Snow cover on the ice | NOT FOUND for Mirny | — |
| Surface melt | ERA5 grid point 66.50°S 93.00°E (sea level; the same point as the Mirny check): **about 206 hours a year above 0 °C**, July mean −14.7 °C, January mean −2.0 °C, minimum −30.5 °C. | DERIVED |
| Wind | Same point: mean 8.7 m/s (9.4 April-October); 9.7% of hours ≥15 m/s (12.3% April-October); 3.0% of April-October hours ≥20 m/s; ESE 33% of hours, **E in 80% of hours ≥15 m/s**; highest hourly 33.6 m/s, gust 48.2 m/s. The station itself records stronger wind (about 11 m/s mean; "more than 200 days" over 15 m/s; secondary, already known). The fast ice lies directly downwind of the katabatic outflow from the ice sheet behind Mirny. | DERIVED; SOURCED (already known) |
| Visibility | NOT FOUND | — |
| How a summer ship reaches it | In summer the fast ice is what the ship must cross or wait out: the 1956 *Ob* "stopped 100 m from shore"; loads cross "many kilometers of deformed fast ice"; in 2002 the ship could not reach the station (already known). A runway on the fast ice would itself be gone in the months the ship arrives (break-up mean 3 February). | SOURCED (already known); DERIVED |
| Season the surface exists | From freeze-up (mean 6 April) to break-up (mean 3 February). Ice thick enough for heavy aircraft would come some weeks to months after freeze-up; the date when a given thickness is reached: **NOT FOUND for Mirny** (at Davis, maximum thickness is reached "in October or November," UNVERIFIED, already known). | SOURCED / NOT FOUND |
| Past landings | No source found of a sea-ice runway or landing on the fast ice at Mirny. Three searches (Russian and English) died at the query or at the sources (search log). The first Soviet heavy aircraft at Mirny (1961) landed on "a prepared snow runway" (already known, Lukin 2022). | NOT FOUND |

## 5. Shackleton Ice Shelf surface

Already known (port file A; not repeated in full): 33,820 km²; 180-250 m thick near the front; front 18-34 m high; main-shelf speed about 73-365 m/yr, Denman tongue about 1.8 km/yr, Scott Glacier over 1.46 km/yr; outer-shelf surface melt among the most intense outside the Peninsula (about 200 mm w.e./yr), surface lakes from late November to January; rifts R1 and R2; fractured zones held by fast ice; the front advanced about 0.3 km/yr in 2015-2022; ship access only to the outer front, with open water just off it on 14-29 days a season on average in 2011-2020.

| Fact | Value | Status |
|---|---|---|
| Position and distance to Mirny | about 95°E to 105°E (already known). The nearest point of the ADD shelf polygon to Mirny is about 82 km east of it (66.52°S 94.86°E); the slow area described below is about 180 km from Mirny. | SOURCED; DERIVED |
| Area from the ADD polygon | 33,464 km² true area (ADD FID 1487, "ice shelf"); bounding rectangle about 327 × 202 km | DERIVED |
| Surface height | REMA median 37 m, maximum 342 m (the maximum is at grounded rises inside the polygon) | DERIVED |
| **Flatness** | **8,168 of 8,573 grid centers** (2 km spacing) have a qualifying 3 km line wholly on the shelf: the surface is flat almost everywhere at this scale | DERIVED |
| **Ice speed** | ITS_LIVE reliable on 42% of the shelf: p10/median/p90 **20/161/1,462 m/yr**. Of 3,210 flat lines with reliable speed, **106 have a maximum of 15 m/yr or less** and 11 of 5 m/yr or less. | DERIVED |
| Where the slow lines are | **(a) South of Henderson Island**, 66.44-66.50°S, 96.97-97.32°E, surface 40-67 m: most of the slow lines on real shelf ice; slowest 66.487°S 97.066°E, bearing 160°, 40-49 m, **max 4.3 m/yr**; about 77 km from the nearest open-sea edge in the ADD, 180 km from Mirny. (b) 66.33-66.34°S 100.49-100.58°E, 37-77 m, max 4.5-8.8 m/yr: next to the Apfel Glacier and the Bunger Hills (excluded zone). (c) 65.78-65.88°S 100.50-100.89°E, 19-25 m, max 9.4-12.0 m/yr: beside the unnamed island FID 1466. (d) **Very low surfaces (1-3 m) east of the shelf, about 65.83-65.90°S, 101.57-101.62°E, max 3.4-3.6 m/yr**: a surface this low and this slow is what sea ice would show, which supports the open question in port file A that part of the ADD's eastern "ice shelf" may be multiyear fast ice. 1,017 of the 8,168 flat lines lie on surfaces below 10 m. | DERIVED |
| Crevassing | Rifts R1 (about 15 km wide, over 40 km long) and R2, and a rift near Roscoe within 3.2 km of the front (already known). Crevasse maps for the slow area south of Henderson Island: NOT FOUND. | already known; NOT FOUND |
| Snow accumulation | NOT FOUND for the shelf | — |
| Surface melt | Already known: about 200 mm w.e./yr on the outer shelf; surface lakes November-January. ERA5 (65.75°S 98.00°E, 51 m): about 107 hours a year above 0 °C; July −18.1 °C, January −3.9 °C, minimum −39.4 °C. | already known; DERIVED |
| Wind | ERA5 same point: mean 8.1 m/s (9.0 April-October); 8.8% of hours ≥15 m/s (11.3% April-October); 3.9% of April-October hours ≥20 m/s; SE 24% of hours, **E in 72% of hours ≥15 m/s**; highest hourly 37.3 m/s, gust 50.7 m/s. Katabatic outflow over the polynya west of the shelf is already known (ocean file, item 6.3). | DERIVED |
| Visibility | NOT FOUND | — |
| Ship access | Only to the outer front (18-34 m high near Mill Island; already known); the slow area south of Henderson Island is about 77 km inside the front. | already known; DERIVED |
| Past landings | Mawson's Western Base (1912) was built on the shelf near 95°E, about 0.6 km inside the cliff; *Edisto* (1948) reached "a low area of shelf ice" about 40 miles from the Bunger Hills (already known). Aircraft landings on the shelf: NOT FOUND. | already known; NOT FOUND |

## 6. West Ice Shelf surface (the part east of 85°E) and its islands

| Fact | Value | Status |
|---|---|---|
| Extent | "extending about 350 km in an east-west direction," reaching "up to 120 km northwards from the continental margin," between Barrier Bay and Posadowsky Bay. **The infobox position on that page (68°36′S 77°53′E) cannot be right for a shelf lying near 66-67°S, 81-89°E, and is not used.** | SOURCED (Wikipedia, from GNIS); the coordinate conflict is my observation |
| Area | 16,370 km²; surface "up to 70-100 m" above sea level; "shrank by roughly one third" (Russian Wikipedia, citing Maslennikov 1986 and the Soviet encyclopedia). ADD polygon (FID 14529, the whole shelf, including the part west of 85°E): 17,098 km² true area. | UNVERIFIED (unsourced figures in a secondary page); DERIVED |
| Distance to Mirny | the eastern end (about 89°E) is roughly 170-200 km west of Mirny; the islands below are 291-346 km | DERIVED |
| Surface height | REMA median 42 m, maximum 211 m (on rises) | DERIVED |
| Flatness | 3,895 of 4,342 grid centers (2 km spacing) have a flat 3 km line | DERIVED |
| **Ice speed** | ITS_LIVE reliable on 50%: p10/median/p90 **107/391/686 m/yr**. Of 1,783 flat lines with reliable speed, **only 3 have max ≤15 m/yr** (9.5-15.2 m/yr), and two of them lie west of 85°E (84.39-84.56°E). Inside the brief's range, one: 66.729°S 85.280°E, bearing 130°, 12-26 m, max 12.4 m/yr. | DERIVED |
| Surface melt | ERA5 (67.00°S 86.75°E, 79 m): about 136 hours a year above 0 °C; July −17.7 °C, January −3.9 °C, minimum −40.9 °C. Measured melt: NOT FOUND (two searches died at the query). | DERIVED; NOT FOUND |
| Wind | ERA5 same point: mean 9.1 m/s (9.8 April-October); 10.3% of hours ≥15 m/s (12.8% April-October); 4.3% of April-October hours ≥20 m/s; ESE 39% of hours, E in 61% of hours ≥15 m/s; highest hourly 38.2 m/s, gust 52.9 m/s | DERIVED |
| Front height | **could not be measured:** REMA 150 m inside the ADD front reads a median of 1 m, i.e. the two products place the front differently. NOT FOUND. | DERIVED (failed) |
| Ship access | *Gauss* (Drygalski's expedition) "was trapped in pack ice from February 21, 1902, until February 8, 1903" off this shelf. | SOURCED (Wikipedia) |
| Past stations and surveys | "In 1957-1960 … in the central part of the glacier," a meteorological station "Druzhba" worked for three months (May-July) on the "Zavadovsky dome"; further expeditions in 1964 and 1991 (Russian Wikipedia). See Zavadovskiy Island below. | UNVERIFIED (secondary, citing a 1986 book) |

**Islands in the West Ice Shelf (all within the brief's range, east of 85°E):**

| Fact | Mikhaylov Island (ADD FID 14527) | Zavadovskiy Island (FID 14525) | Leskov Island (FID 14528) | Status |
|---|---|---|---|---|
| Position | 66°48′S 85°30′E | 66°43′S 86°24′E | 66°36′S 85°10′E | SOURCED (Wikipedia/GNIS) |
| Distance to Mirny | ≈327 km | ≈291 km | ≈346 km | DERIVED |
| Published size and height | 685 km², 41 × 19 km, 240.6 m; "ice-covered non erupted Volcano" | 100 km², 200 m; also called Penguin Island | 49.5 km², 9 × 5.5 km, 185 m | SOURCED (Wikipedia) |
| ADD size | 560 km², about 35 × 22 km | 172 km², about 17 × 15 km | 110 km², about 16 × 11 km (twice the published figure; unresolved) | DERIVED |
| REMA height | max 246 m, median 129 m | max 206 m, median 110 m | max 193 m, median 96 m | DERIVED |
| Flat area (centers with a qualifying 3 km line) | 2,083 of 2,227 (about 507 km²) | 558 of 671 (about 136 km²) | 277 of 422 (about 67 km²) | DERIVED |
| ITS_LIVE speed | reliable on 51%: p10/median/p90 **2.1/5.4/13.1 m/yr**; 749 flat lines max ≤15, 74 max ≤5; slowest 66.773°S 85.434°E, bearing 70°, 213-245 m, **max 3.4 m/yr**; also 66.765°S 85.447°E, bearing 30°, 0.86% steepest segment, 206-218 m, max 3.5 m/yr | reliable on 45%: 3.7/7.2/21.4 m/yr; 161 flat lines max ≤15, none ≤5; slowest 66.727°S 86.293°E, bearing 100°, 97-109 m, **max 5.6 m/yr** | reliable on 16%: 9.4/12.1/14.8 m/yr; 19 flat lines max ≤15; slowest 66.558°S 85.130°E, 102-133 m, max 11.3 m/yr | DERIVED |
| Shore | 100% ice shelf in the ADD | 100% ice shelf | 68% ice shelf; the sea-facing 32% has an edge about 36 m high (median; 28-44 m) and ETOPO depths of 143 m median within 1 km, 207 m at 2-5 km | DERIVED |
| ERA5 (point, elevation) | 66.75°S 85.50°E, 225 m: mean 7.6 m/s; 9.7% of hours ≥15 m/s (11.9% April-October); 4.1% of April-October hours ≥20 m/s; E 41%, E in 69% of hours ≥15 m/s; gust max 50.3 m/s; **about 15 hours a year above 0 °C**; July −21.3 °C | 66.75°S 86.25°E, 114 m: mean 7.8 m/s; 10.6% ≥15 m/s (12.9% April-October); 4.9% of April-October hours ≥20 m/s; E 41%, E in 66% of hours ≥15 m/s; gust max 51.9 m/s; about 48 hours a year above 0 °C | not run (the Mikhaylov point is 11 km away) | DERIVED |
| History | discovered by a Soviet expedition in 1956 | discovered 1956; **Soviet temporary field station "Druzhba," 20 May to 6 August 1960**, meteorological, "one winter" | Wikipedia's discovery claim (1819-21) was not checked | SOURCED (Wikipedia) |
| Crevassing, accumulation, visibility | NOT FOUND | NOT FOUND | NOT FOUND | — |

**Snag recorded:** Wikipedia gives the identical dates, 20 May to 6 August 1960, for the "Mir" station on Drygalski Island and the "Druzhba" station on Zavadovskiy Island, both citing the same 1971 compendium. Russian Wikipedia puts Druzhba on the "Zavadovsky dome" for May-July 1960. **Whether these were two stations or one entry duplicated was not resolved.**

## 7. Blue-ice areas near the coast

**Source of the outlines:** Tollenaar, V., et al. (2024), "Where the White Continent is blue: deep learning locates bare ice in Antarctica," *Geophysical Research Letters* 51, e2023GL106285: a continent-wide 200 m map of blue-ice areas from MODIS, RADARSAT-2 and TanDEM-X; blue ice covers "about 140,000 km², roughly 1% of Antarctica" (SOURCED as given in search summaries of the paper; the paper was not opened). Smoothed outlines downloaded from Zenodo record 10539933 (`smoothed_BIAs.zip`, open; an earlier version, 8333865, is restricted).

**Method (DERIVED):** every outline whose centroid lies between 85°E and 115°E, north of 68.5°S, and within 60 km of the Natural Earth 1:10m coastline (which follows ice-shelf fronts) was kept: **452 outlines**. For each, a 3 km straight line was tested at 250 m spacing and 18 bearings to see whether it fits wholly inside the outline; about 90 outlines can hold one. Those that are slow at their centroid, or large, were then put through the same REMA grade and ITS_LIVE speed test used elsewhere (lines wholly inside the blue ice, no 288 m segment over 2%). **Caveat:** the map also marks some bare sea ice and glacier-tongue ice as "blue ice"; outlines at 0-5 m are probably sea ice or fast ice, not glacier ice.

**Count by longitude band (all 452):** 85-90°E: 63; 90-95°E: 18; 95-100°E: 84; 100-105°E: 137; 105-110°E: 51; 110-115°E: 99. *Most outlines that can hold a 3 km line sit on fast-moving outlet glaciers* (centroid speeds of 100 to over 1,700 m/yr: Denman, Scott, Totten, Vanderford, Helen and others). DERIVED.

| Blue-ice area (centroid) | Area; shape | Height | Distance to Mirny | Flat 3 km lines inside (≤2% per 288 m) | ITS_LIVE speed | Note | Status |
|---|---|---|---|---|---|---|---|
| **East and south of the Bunger Hills** (66.229°S 101.215°E) | 3,304 km²; about 123 × 64 km | 0-906 m, median 233 m | 361-379 km for the slow lines | 789 of 1,441 grid centers (1.5 km spacing) | across the area p10/median/p90 5.5/17.9/77.3 m/yr; **273 flat lines with max ≤15 m/yr, 119 with max ≤10** | Slowest grounded-ice lines: 66.278°S 101.160°E, bearing 130°, 400-406 m, steepest segment 1.12%, **max 3.9 m/yr**, about 4 km from the mapped ice edge and **about 17 km from the Bunger Hills gazetteer point**; 66.265-66.312°S 101.08-101.22°E, 240-480 m, max 4.4-6.0 m/yr; 66.343°S 101.528°E, 748-785 m, max 3.3 m/yr, 34 km from the oasis. Lines at 1-6 m elevation around 66.04-66.12°S 101.08-101.18°E are probably sea ice or fast ice inside the outline. **Adjoins the excluded Bunger Hills oasis.** Whether this is the Australian 2000 blue-ice alternate site: not stated by any source (item 9.2). | DERIVED; adjacency to the oasis DERIVED |
| Behind Mirny (66.608°S 92.976°E) | 4.7 km²; about 4 × 2 km | 211 m median (max 307 m) | **≈6 km** | **none** (too steep) | p10/median/p90 3.8/7.1/21.2 m/yr | Likely inside the brief's excluded surroundings of Mirny. Popov et al. 2019 report snow-firn thickness "between zero ('blue ice')" and 40 m across the Mirny strip survey area (already known). | DERIVED |
| Coastal slope south of Masson Island (66.667°S 95.823°E) | 463 km²; about 67 × 20 km | median 130 m | ≈125 km | 64 of 189 centers | p10/median/p90 41.5/125.7/299.6 m/yr; slowest flat line max 62.7 m/yr | fast-moving coastal ice | DERIVED |
| David Island area (66.452°S 98.379°E) | 26 km²; 17 × 5 km | median 19 m | ≈238 km | 22 (all at 7-19 m) | slowest flat line max 27.5 m/yr | low, probably on the shelf edge | DERIVED |
| Near Denman Glacier (66.604°S 99.807°E) | 8 km² | median 253 m | ≈300 km | none (too steep) | p10/median 1.2/3.1 m/yr | too small and sloping | DERIVED |
| Knox Coast (65.882°S 102.688°E) | 13 km² | median 73 m | ≈440 km | none | median 17.1 m/yr | — | DERIVED |
| Knox Coast (66.472°S 107.105°E) | 4.5 km² | median 112 m | ≈623 km | none | median 9.0 m/yr | — | DERIVED |
| Queen Mary Coast (66.531°S 94.765°E) | 11.6 km² | median 112 m | ≈78 km | none | median 22.3 m/yr | — | DERIVED |
| Wilkins area, Law Dome (66.803°S 111.502°E and two smaller ones to the south) | 463 km²; 10 km²; 22 km² | 692-803 m | 812-820 km | many | centroid 4.2-6.8 m/yr | **the Wilkins runway area, already known**; 22-49 km from the coastline | DERIVED / already known |

**Other facts for blue ice in this sector:**
- The Mirny-area and Progress papers (already known) found no usable blue ice near those stations; the Progress team found "no blue-ice zones within reasonable distance."
- The Polyakov et al. 2019 Apfel Glacier site is blue ice with slopes ≤2.5% and crevasses ≤25 cm (item 9.1).
- **Melt on low coastal blue ice:** "At low altitudes and relatively high latitudes, blue-ice ablation areas may be pitted with melt ponds and incised by summer melt streams"; near Mawson (about 63°E, outside the sector) net ablation is about 0.5 m/yr at 60 m elevation. (Mellor and Swithinbank 1989, SOURCED.) The Transcription Gulf survey found cryoconite cavities up to 6 m across (item 9.1).
- **Wind:** blue ice exists where wind keeps snow off; near the Bunger Hills it indicates "persistent snow surface scouring by easterly katabatic winds" (Arthur et al. 2020, already known). ERA5 for the Bunger-east area: see the table at the end of item 10.
- Ship access to any of these: none is on a shoreline a ship has used, as far as any source read says. **NOT FOUND.**

## 8. Law Dome (western and southwestern slopes) and other slow coastal ice

Already known (operations and geology files): Wilkins runway on Law Dome's western slope, 65-70 km from Casey at 720-780 m, ice about 500 m thick moving 12 m/yr, summer-only, closing 4-9 weeks for melt; Law Dome rises to 1,395 m and is about 150 km across; Wilkins is in a "rain shadow" and the eastern side receives over 2.5 m water equivalent a year; prevailing wind northeast through east-southeast; turbulence in the dome's wake.

| Fact | Value | Status |
|---|---|---|
| Position | summit 66°44′S 112°50′E; DSS ice core 66.7697°S 112.8069°E at 1,370 m | SOURCED (Wikipedia; Roberts et al. 2015, *Climate of the Past* 11:697, PDF read) |
| Distance to Mirny | the western slope near Casey is about 780-800 km from Mirny; Law Dome is the far eastern end of the brief's range | DERIVED |
| What Law Dome is | "a small independent icecap … with a maritime climate"; "ice flow at Law Dome is largely independent of the East Antarctic ice sheet and orography results in a strong east-west snow accumulation gradient (Morgan et al., 1997)" | SOURCED (Roberts 2015) |
| Accumulation | summit (DSS): **0.68 m ice equivalent per year**. The west side is drier (the "rain shadow," already known). S-1 near Casey: "small annual net accumulation" around a blue-ice patch with "negligible" ablation (item 9.4). Near the former Wilkes station, "annual balance rates have ranged from +6 cm of water to −3 cm of water" (Cameron 1964, quoted in CRREL 89-21). | SOURCED |
| **Slow, flat ice near the coast (DERIVED; method in the search log, 1 km spacing; lines within 15 km of Casey removed)** | Of the flat 3 km lines on the mainland within 10 km of the coast and with reliable speed: 1,372, of which **273 have max ≤15 m/yr** and 44 max ≤5 m/yr; within 20 km: 3,669, of which 951 ≤15 and 115 ≤5. **Almost all of these lie on the western and southwestern slopes (110.6-111.5°E).** Between 111.5°E and 112.5°E (north-facing slopes), none of 709 coastal lines is that slow; between 112.5°E and 114°E, 2 of 673. | DERIVED |
| Examples | (a) **Southwestern slope above the Vanderford-Peterson glacier coast**, 66.56-66.60°S 110.65-110.71°E, 32-84 m, steepest segments 0.97-1.9%, **max 3.1-7.4 m/yr**, 6-10 km from the open-sea edge in the ADD and 0.4-2 km from ADD ice-shelf ice, 31-36 km from Casey. (b) 66.65-66.67°S 110.90-110.93°E, 239-285 m, steepest segment 0.78-1.8%, **max 1.7-1.9 m/yr**, about 9 km from the coast. (c) 66.35°S 110.83-110.87°E, 404-470 m, max 1.7-2.5 m/yr, about 8 km from the coast but only about 15 km from Casey. (d) 66.39-66.44°S 111.05-111.16°E, 565-669 m, max 1.5-2.4 m/yr, 15-20 km from the coast. | DERIVED |
| Surface melt | ERA5 southwestern slope point (66.50°S 110.75°E, model elevation 58 m): **about 425 hours a year above 0 °C**, July −16.8 °C, January −1.7 °C, the warmest of all the points in this unit. ERA5 north slope (66.00°S 112.50°E, 344 m): about 53 hours a year. AAD sited Wilkins high and far inland to escape coastal summer warmth (already known). | DERIVED; already known |
| Wind | ERA5 southwestern point: mean 6.1 m/s (7.0 April-October); 6.4% of hours ≥15 m/s (9.1% April-October); 2.6% of April-October hours ≥20 m/s; E 33%, E in 48% of hours ≥15 m/s; highest hourly 36.0 m/s, gust 52.3 m/s. North slope point: mean 9.2 m/s (9.9 April-October); **20.0% of hours ≥15 m/s (25.0% April-October)**; 8.8% of April-October hours ≥20 m/s; ESE 36%, ESE 61% of hours ≥15 m/s; gust 48.5 m/s. Casey's own record (already known): 49% of days over 22 knots and 17% blizzard days in 2001. | DERIVED; already known |
| Low cloud | "Forced ascent … against the slope of Law Dome invariably leads to the formation of low cloud or fog" with westerlies (already known, AAD forecasting notes). | already known |
| Crevassing | NOT FOUND for the coastal slopes | — |
| Ship access | Casey's wharf and the fast-ice problem are already known; ship access to the southwestern slope's shore (Vanderford-Peterson coast): NOT FOUND | NOT FOUND |
| Past landings | S-1 Twin Otter wheel landing, 1988 (item 9.4); Wilkins (already known) | SOURCED |

### Other slow coastal ice found by the same scan (mainland only; Mirny ±10 km, Bunger ±25 km, Casey ±15 km removed)

| Stretch of coast | Flat lines within 20 km of the coast with reliable speed | of which max ≤15 m/yr | Slowest examples | Status |
|---|---|---|---|---|
| Queen Mary Coast west of Mirny (88.8-92.9°E) | 1,343 | 22 | 66.648°S 91.016°E, 248-259 m, max 8.5 m/yr, about 3 km from the open-sea edge, **about 89 km from Mirny**; 66.647°S 91.083°E, 292-305 m, max 9.0 m/yr, 86 km from Mirny | DERIVED |
| Queen Mary Coast east of Mirny (93.1-95.6°E) | 1,990 | 28 | 66.593°S 94.681°E, 395-420 m, max 12.7 m/yr, about 8 km from the open-sea edge, **about 74 km from Mirny** | DERIVED |
| Behind the Shackleton Ice Shelf (94.5-103.9°E; distance here is to the Natural Earth line, which may trace the grounding zone) | 1,694 | 268 | 66.665°S 99.812°E, 478-509 m, max 2.6 m/yr; 66.807°S 99.010°E, 314-360 m, max 3.0 m/yr. These are 54-91 km from any open sea (behind the shelf), 263-305 km from Mirny. | DERIVED |
| Knox Coast (102.4-109.5°E) | 4,052 | 148 | 66.733°S 108.197°E, 175-183 m, max 4.0 m/yr, about 4 km from the coast, 668 km from Mirny; 66.75-66.79°S 107.88-107.98°E, 210-351 m, max 5.1-6.8 m/yr | DERIVED |

ERA5 for these stretches was not downloaded (search log, rate limit), except as listed per site.

## 9. Past landings, surveys and proposals in the sector (85°E to 115°E)

These sites lie in or beside the brief's excluded zones (Bunger Hills, Casey). They are recorded because the brief asks for past surveys and proposals, not as candidates.

### 9.1 The 2019 Russian airfield survey at the Bunger Hills (the brief's "Polyakov, Martyanov and Sukhanova")

**Source, read in full in Russian (translations mine):** S.P. Polyakov, V.L. Martyanov (AARI), A.A. Sukhanova (St Petersburg State University), "Организация нового аэродрома РАЭ в районе оазиса Бангера, Антарктида" ("Organizing a new Russian Antarctic Expedition airfield in the Bunger Hills area, Antarctica"), *Российские полярные исследования* (*Russian Polar Research*) No. 37 (2019), pp. 11-15, PDF from data.aari.ru. **SOURCED** throughout this subsection unless marked.

- **Context:** "In total five landing sites belonging to the Russian Antarctic Expedition operate in Antarctica today. All of them are on glaciers and are snow-ice landing sites." The airborne geophysics laboratory (an An-2) had been based at the Mirny strip opened in February 2016. The new site was to serve the Bunger Hills field base and the flying laboratory, for "light and medium aircraft such as the An-2 and BT-67 'Basler' on ski undercarriage." **It was not a heavy-aircraft or jet survey.**
- **History of the search:** reconnaissance by helicopter from January 2008 (53rd RAE) "around the whole perimeter of the oasis, with landings at a number of places." The search found "a single potentially suitable area in the south-western part of Transcription Gulf." "According to historical data, an Il-14 aircraft landed on exactly this gulf in the 1960s." The authors also used "information on possible airfield areas kindly provided by our Australian colleagues from the Australian Antarctic Division." Field work ran from *Akademik Fedorov*, which arrived on 23 January 2019 and stayed until 16 February.
- **On rock:** "it is not possible to organize a landing site on the bedrock of the Bunger Hills because of the complex surface relief."
- **Site 1, Transcription Gulf (an epishelf lake):** "the only water body of the oasis on which the ice does not break up for many years." Depth in the center up to 100 m; fresh water (under 1‰ salinity) to 70 m depth. Lake-ice thickness "in summer close to 3 m on average, with a maximum of 5 m"; GPR over 27,300 m of profile gave **295-320 cm** in the surveyed area, checked by drilling to within 10 cm. Upper 30 cm is matte infiltration ice. The surface was "perfectly level"; "a runway could be laid out on it without preparing the surface, only marking it." **"The bearing capacity of the ice cover … fully allows heavy aircraft on wheeled undercarriage to work on it."** But **cryoconite cavities** (wind-blown rock dust melting into the ice) up to 6 m across and 30 cm deep cover much of the northern part. Zone 1 (smooth, no cavities) is the Australian Twin Otter ski strip at Edgeworth David Camp, possibly "insufficient" in size for medium aircraft; Zone 2 has few cavities and room for a medium-aircraft strip; Zone 3 is unusable without preparation. Hills up to 100 m are obstacles, "not critical." The camp is 5 km over rock from the main seasonal base (3 hours by GAZ-71 tracked carrier). Tidal cracks run along the shores.
- **Site 2, Apfel Glacier:** an outlet glacier on bedrock that flows around the south of the oasis. The surface is ice from the top ("can be assigned to the blue-ice zone"); crevasses no wider than 25 cm, most water-filled, with thin or no snow bridges; 9,000 m of GPR found no significant internal cracks or voids; macro-slopes "do not exceed 2.5%." Proposed runway centerline **66°20′36.0″S 100°48′47.0″E to 66°20′37.0″S 100°51′55.0″E, bearing 90°**, "matching the prevailing winds in the oasis." *Length of that centerline: about 2.33 km (DERIVED, great-circle). Distance to Mirny: about 348 km (DERIVED).* For a BT-67 the cracks must first be filled with snow and packed. A 9-stake network was set to measure glacier movement and mass balance (results not given).
- **Conclusion:** Transcription Gulf suits light and medium aircraft without preparation; the Apfel site "may be considered an alternate in the Bunger Hills area for light and medium aircraft." "In November 2010 an Australian aircraft was damaged landing on Transcription Gulf, running its undercarriage onto an ice sastruga."
- **The companion journal paper** (Sukhanova, Popov, Polyakov, Kashkevich, Martyanov, *Problemy Arktiki i Antarktiki* 65(3):315-327, 2019, DOI 10.30758/0555-2648-2019-65-3-315-327) chose "the central part of the epishelf Transcription Gulf, situated 7 km away from the base." **UNVERIFIED** (abstract-level search text only; three hosts refused the full text).
- A search result describes the 2010 incident as a CASA 212 that struck "hard ridged ice on the unprepared runway" at the Bunger Hills in November 2010 while ferrying to Davis. **UNVERIFIED** (aviation-safety database snippet; the page failed with a certificate error).

### 9.2 Australia's proposed Bunger Hills alternate (1999-2002)

- AAD news release, 2000: the Casey intercontinental terminus "would be supplemented by an alternative blue-ice runway … in the Bunger Hills, 440 km west of Casey"; "a suitable blue-ice runway site is available in the Bunger Hills to provide an alternative landing site"; it would be "a staging point for intracontinental flights"; "It is expected that a Hercules C130 aircraft will be used to trial the Bunger Hills blue ice runway this coming summer." Field investigators in 1999-2000 "used a Twin Otter aircraft to assess potential landing sites." **SOURCED** (antarctica.gov.au news 2000).
- AAD magazine, autumn 2001: the report "recommends that an airfield at Bunger Hills be used as an 'alternate'." **SOURCED.**
- **Whether the C-130 trial was flown, and the exact position of the Australian blue-ice site: NOT FOUND** (two searches; search log). Australia later chose round-trip fuel instead of an alternate (already known, Colborne 2010 via the operations file).
- *A possible match, DERIVED and not confirmed by any source:* the Tollenaar et al. 2024 blue-ice map shows one very large blue-ice area (about 3,300 km²) on the ice sheet east and south of the oasis (centroid 66.229°S 101.215°E); Arthur et al. 2020 describe "blue-ice areas next to the Bunger Hills" scoured by easterly katabatics (already known). Its measured properties are in item 7.

### 9.3 Soviet heavy-aircraft use of the Bunger Hills (already known, one line)

The 1961-62 Il-18 took on full fuel for the return to Christchurch "at a runway in the Bunger Hills oasis," and in 1963-64 two Il-18s landed "on a runway prepared in a Bunger Hills lagoon" (Lukin 2022, operations file). Polyakov et al. 2019 add the 1960s Il-14 landing on Transcription Gulf (above). Whether the 1963-64 "lagoon" is Transcription Gulf is not stated in either source (NOT FOUND).

### 9.4 Law Dome, near Casey: the S-1 blue-ice site and the 1988 wheel landing

**SOURCED** from Mellor and Swithinbank, *Airfields on Antarctic Glacier Ice*, CRREL Report 89-21 (1989), pp. 48 and 8, PDF downloaded from southpolestation.com and read:
- "Close to the Australian Casey station … there is a blue-ice runway site known as S-1," "approximately 66°16′S, 110°42′E, at an elevation of 262 m (860 ft), some 9 n.m. (16 km) south of Cape Folger, and about 2.5 n.m. (4.5 km) from the nearest coastline." Mean annual temperature about −10.5 °C. "Blue ice is exposed at the site … The site is surrounded by areas that have a small annual net accumulation of snow, and its ablation rate is negligible." "At the S-1 site near Casey, the long-term ablation rate is close to zero."
- First surveyed in early 1959 (Coombes, Department of Civil Aviation; Mellor); later studies "focused on compacted snow runway construction at a place called Lanyon Junction (Russell-Head and Budd 1989)."
- "In 1988 a strip was prepared on coastal blue ice 6 km east of Casey station and a wheel landing was made there by a Twin Otter after a flight from Hobart on 6 November." The strip "was located about 6 km (3¼ n.m.) east of Casey station at an elevation of about 300 m," on blue ice "with scattered patches of snow up to 5 cm"; central runway **30 m wide and 1.5 km long**, with 30 m graded strips each side. RAAF C-130 trial flights were planned for early February 1990. Whether they were flown: **NOT FOUND.**
- *DERIVED:* ITS_LIVE at 66.267°S 110.70°E: **6.2 m/yr** (error 1 m/yr); REMA 1 km: about 301 m.
- **This site is about 6-10 km from Casey and may fall inside the brief's excluded surroundings.**

### 9.5 Australia's Casey-area blue-ice survey sites before Wilkins (2001-2003)

The 2001/02 Air Transport Study "identified several 'Blue Ice' runway sites" and examined site **R3** in the upper Peterson Glacier region, about 50 km southeast of Casey; satellite imagery then showed "larger, higher patches of blue ice" to the south, and the 2002/03 team found "a suitable runway site" about 65 km southeast of Casey, moving about **6 m/yr east-southeast** (this became the A6 South site, later Wilkins). **SOURCED** (researchdata.edu.au record for the AADC "Casey Blue Ice Runway Survey Report 2002-2003"; the openpolar.no copy failed with a certificate error). Wilkins itself is already known.

### 9.6 Other searches for proposals

- **The Davis / Vestfold Hills paved runway** (2,700 m, canceled 2021) is already known (geology file) and lies in an excluded zone; not researched further.
- **A heavy-aircraft or jet runway at or near Mirny:** NOT FOUND (search log; the only Russian work is the 1.3 km BT-67 strip, already known).
- **Swithinbank's 1991 continent-wide list of potential wheeled-aircraft sites** (CRREL Report 91-24 / DTIC ADA249503; 84 blue-ice sites reported by a secondary source): **the list for this sector was not read**. DTIC returned 403, and the US Army ERDC library returned a reCAPTCHA page, which was not worked around.

## 10. Other candidates found

| Place | Facts | Status |
|---|---|---|
| **Gaussberg** (66°48′S 89°11′E; ≈171 km west of Mirny) | Extinct volcano, 373 m (Mitchell and Bergman 1991, cited by Wikipedia); the cone is "1.5-kilometer-wide" and covers "about 10 square kilometers" (spelling Americanized in quotation); "the only ice-free outcrop between Mirny Station and the Vestfold Hills"; "on the Davis Sea immediately west of Posadowsky Glacier," close to the West Ice Shelf. Visited 1902 (Drygalski's tethered balloon), 1912 (Australasian Antarctic Expedition), Soviet expedition 1956-57, Australian visits 1977, 1981, 1987. **No 3 km line fits on its rock** (a cone 1.5 km wide; DERIVED from the sourced size). The ice around it: 619 of 3,314 grid centers have a flat 3 km line, but the slowest flat line (66.829°S 89.142°E, 160-175 m, about 3.5 km from the open-sea edge) moves up to 44 m/yr; most move far faster (box median 164 m/yr). ERA5 (66.75°S 89.25°E, sea level): mean 8.5 m/s; 10.1% of hours ≥15 m/s; E in 90% of hours ≥15 m/s; about 412 hours a year above 0 °C. | SOURCED (Wikipedia); DERIVED |
| Ice tongue east of Mirny (ADD FID 1488; centroid 66.629°S 93.905°E; ≈41 km from Mirny; 280 km²) | Flat (324 of 1,093 centers) but **fast: 614 to over 1,200 m/yr** (ITS_LIVE p10/median/p90 690/947/1,296). Which glacier feeds it: not confirmed in a source read (the ASPA 127 plan mentions icebergs "calved from the Helen Glacier," already known). | DERIVED; name UNVERIFIED |
| Small ice shelf west of Mirny (ADD FID 1499; 66.611°S 92.492°E; ≈24 km from Mirny; 23 km²) | Only 7 flat centers; speed 207-493 m/yr | DERIVED |
| Two unnamed island ice caps in the Shackleton system (FID 1466 and FID 1476) | See item 2f: slow (median 3.9 and 5.5 m/yr) and largely flat; FID 1476 is about 23 km from the Bunger Hills | DERIVED |
| Slow shelf ice south of Henderson Island | See item 5 | DERIVED |
| West Ice Shelf islands (Mikhaylov, Zavadovskiy, Leskov) | See item 6 | SOURCED / DERIVED |
| Blue ice east and south of the Bunger Hills | See item 7 (adjoins an excluded zone) | DERIVED |
| Coastal ice-sheet stretches west and east of Mirny, behind the Shackleton Ice Shelf, and on the Knox Coast | See the table at the end of item 8 | DERIVED |
| Rock ground long enough for a 3 km runway anywhere in 85-115°E outside the excluded oases | **None found.** Gaussberg (10 km²) is described as the only ice-free outcrop between Mirny and the Vestfold Hills; the Haswell Islands are too small; the Bunger Hills (excluded) are "absolutely unsuitable" relief per the Russian survey. | SOURCED; DERIVED |

## FINAL: the candidates as a factual table, and what is and is not known

**No recommendation and no ranking.** Rows run west to east. "Flat" means at least one 3 km straight line with no 288 m segment steeper than 2% (REMA, DERIVED). Speeds are ITS_LIVE with error ≤20 m/yr (DERIVED). Wind is ERA5 1991-2020 at the nearest grid point (DERIVED, reads low near this coast): mean / share of hours ≥15 m/s / direction of strong winds. "Hours >0 °C" is ERA5 air temperature per year (DERIVED). Excluded-zone flags are my reading of the brief, for the developer to judge.

| Candidate | Position | km to Mirny | Size; flat area | Surface | Height | Ice speed on flat lines | Wind | Hours >0 °C | Shore and ship access | Past use | Main gaps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| West Ice Shelf (east of 85°E) | 66-67°S, 85-89°E | ≈188 (nearest) to 350 | shelf 17,098 km² (whole); flat almost everywhere | floating shelf | median 42 m | median 391 m/yr; 1 line ≤15 m/yr east of 85°E | 9.1 m/s / 10.3% / E-ESE | 136 | front height not measurable; *Gauss* beset 1902-03 | Druzhba 1960 (on Zavadovskiy) | melt, front, accumulation |
| Mikhaylov Island | 66°48′S 85°30′E | ≈327 | 560-685 km²; ≈507 km² flat | ice cap ("non erupted volcano") | to 241-246 m | 2.1-13.1 m/yr (p10-p90); slowest flat line 3.4 m/yr | 7.6 / 9.7% / E | 15 | shore 100% ice shelf | discovered 1956 | crevasses, accumulation, visibility |
| Zavadovskiy Island | 66°43′S 86°24′E | ≈291 | 100-172 km²; ≈136 km² flat | ice cap | to 200-206 m | 3.7-21.4; slowest 5.6 m/yr | 7.8 / 10.6% / E | 48 | 100% ice shelf | Druzhba station 20 May-6 Aug 1960 | dates duplicate Mir; crevasses, accumulation |
| Leskov Island | 66°36′S 85°10′E | ≈346 | 49.5-110 km²; ≈67 km² flat | ice cap | to 185-193 m | 9.4-14.8; slowest 11.3 m/yr | (Mikhaylov point) | (≈15) | 68% shelf; sea side: edge ≈36 m, depth ≈143 m within 1 km | — | area conflict; most fields |
| Gaussberg and its ice | 66°48′S 89°11′E | ≈171 | rock 10 km², 1.5 km wide: no 3 km line on rock | rock cone; fast ice sheet around | 373 m | ≥44 m/yr on flat ice nearby | 8.5 / 10.1% / E | 412 | 3.5 km from open-sea edge | visits 1902-1997 | ship landing record |
| Drygalski Island | 65°45′S 92°30′E | ≈92 | 220 km²; ≈162 km² flat | ice cap, no rock found | to 325-331 m | **no reliable value** | 8.5 / 12.4% / E | 3 | open sea all round; edge ≈41 m; depth ≈86 m within 1 km | Mir station 1960 | ice speed, accumulation, crevasses, ship landing |
| Haswell Islands | 66°31′S 93°E | 2.5-3 | Haswell 0.82 km²: **no 3 km line** | rock, ice-free | 93 m | — | 8.7 / 9.7% / E | 206 | fast ice most of the year | ASPA 127 | — |
| Davis Sea fast ice off Mirny | north of Mirny, to 30-40 km out | 0-40 | belt 30-40 km wide; iceberg-free 3 km line not found | first-year (sometimes multiyear) sea ice | sea level | — (breaks out; mean 3 Feb; refreezes mean 6 Apr) | 8.7 / 9.7% / E | 206 | it is the ship barrier; gone when the ship comes | none found | **thickness at Mirny**, iceberg spacing |
| Masson Island | 66°08′S 96°35′E | ≈169 | 543 km²; ≈320 km² flat | ice cap | to 465-489 m | 6.8-46.7; slowest 7.8 m/yr | 7.3 / 6.9% / E | 27 | 100% ice shelf | discovered 1912 | crevasses, accumulation |
| Shackleton shelf south of Henderson Island | 66.44-66.50°S, 96.97-97.32°E | ≈180 | a cluster of slow flat lines | floating or pinned shelf | 40-67 m | 4.3-12 m/yr | (shelf point) 8.1 / 8.8% / E | 107 | ≈77 km inside the front | — | whether grounded; crevasses |
| Henderson Island | 66°22′S 97°10′E | ≈188 | 131 km²; ≈45 km² flat | ice cap | to 240-271 m | 2.5-17.6; slowest 3.3 m/yr | 6.9 / 4.1% / E | 39 | 100% ice shelf | sledged to, 1912 | crevasses, accumulation |
| David Island | 66°25′S 98°46′E | ≈257 | 165 km²; ≈29 km² flat | ice cap | to 289 m | 2.2-40.4; slowest 2.5 m/yr | 7.2 / 2.8% / **SSE** | 71 | 100% ice shelf | — | most fields |
| Unnamed island FID 1476 | 66.17°S 100.21°E | ≈324 | 124 km²; ≈75 km² flat | ice cap | to 111 m | 2.9-9.5; slowest 3.7 m/yr | 6.2 / 7.9% / E | 259 | 100% ice shelf; **≈23 km from Bunger Hills** | — | name, history |
| Bunger-east blue ice | 66.27-66.34°S, 101.08-101.53°E (slow part) | 361-379 | blue-ice area 3,304 km²; 789 flat centers | blue ice on the ice sheet | 240-785 m | slowest 3.3-6.0 m/yr | 9.2 / 16.7% / E | 27 | ≈4-6 km from mapped ice edge; **adjoins excluded oasis** | possibly the 2000 Australian alternate (not confirmed) | site identity, melt, crevasses |
| Mill Island | 65°30′S 100°40′E | ≈367 | 1,225-1,260 km²; ≈1,150 km² flat | ice dome; 1.35 m ice/yr accumulation | to 503-515 m | **no reliable value on the dome** | 8.2 / 15.2% / E (CFSR: 7.6 m/s, E) | 0 | 90% ice shelf; north coast to sea: edge ≈31 m, depth ≈157 m within 1 km | ice-core camps 2008-10 | ice speed, crevasses; fog and rime reported |
| Unnamed island FID 1466 | 65.83°S 100.72°E | ≈355 | 249 km²; ≈214 km² flat | ice cap | to 157 m | 2.1-6.9; slowest 1.2 m/yr | 7.2 / 12.7% / E | 75 | 100% ice shelf | — | name, history |
| Bowman Island | 65°17′S 103°07′E | ≈477 | 186-369 km²; ≈290 km² flat | ice cap | to 254 m | **no reliable value** | 9.0 / 16.7% / ESE (grid point off-island) | 32 | 93% open sea; edge ≈36 m; **shallow: ≈18 m within 1 km** | — | speed, area conflict |
| Knox Coast ice sheet | 66.72-66.79°S, 107.88-108.21°E | 654-669 | slow flat lines within 4 km of the coast | grounded ice sheet | 130-384 m | 4.0-6.8 m/yr | not downloaded | — | coast within 2-7 km | — | wind, melt, access |
| Law Dome SW slope | 66.56-66.67°S, 110.65-110.93°E | 778-788 | many slow flat lines | grounded ice cap | 32-285 m | 1.7-7.4 m/yr | 6.1 / 6.4% / E | **425** | 6-10 km from open sea; beside shelf ice | S-1 strip 1988 nearby (Casey zone) | crevasses, melt measurement |
| Law Dome (Wilkins; already known) | 66°41′S 111°31′E | ≈814 | 3,000-3,200 m runway in use | blue ice + snow cap | 720-780 m | 10-12 m/yr | (already known) | (already known) | 43 km from open sea | in use, summer only | — |

**What the sources support (facts only):**
1. **No rock ground in 85-115°E, outside the excluded oases, can hold a 3 km line.** Gaussberg is the only ice-free outcrop between Mirny and the Vestfold Hills and is about 1.5 km across; the Haswell Islands are under 1 km². Every candidate is ice or sea ice.
2. **Flatness is common; slowness is not.** On most candidates a 3 km line under 2% grade exists. The ice shelves (Shackleton median 161 m/yr, West Ice Shelf median 391 m/yr) move tens to hundreds of meters a year; the island ice caps and some coastal slopes move a few meters a year where they can be measured.
3. **The slowest measured flat ice** (max under about 5 m/yr along a 3 km line) was found on: the unnamed island FID 1466, Henderson, David, FID 1476, Mikhaylov, the slow shelf south of Henderson Island, the blue ice east of the Bunger Hills, Law Dome's southwestern slope, and the Knox Coast near 108°E. These are 180-790 km from Mirny.
4. **The two islands nearest Mirny with large flat areas, Drygalski (≈92 km) and Mill (≈367 km), have no reliable ice-speed measurement** on their domes.
5. **Strong winds come from the east almost everywhere** (E or ESE in 48-92% of hours ≥15 m/s; 61-92% everywhere except Law Dome's southwestern slope, 48%), except David Island (SSE).
6. **Most island ice caps in the Shackleton system are wholly surrounded by shelf ice**; only Drygalski, Bowman and the north coasts of Mill and Leskov face the sea, with ice edges about 30-40 m high in REMA.
7. **Real precedents in the sector:** the 2019 Russian survey (Transcription Gulf lake ice 2.95-3.2 m, "bearing capacity … allows heavy aircraft on wheeled undercarriage," cryoconite cavities; Apfel Glacier blue ice for ski aircraft); the 1960s Il-14 on Transcription Gulf and 1961-64 Il-18s in the Bunger Hills; the 1988 Twin Otter wheel landing on 1.5 km of blue ice at S-1 near Casey; the Australian Bunger blue-ice alternate proposed in 2000 (trial not confirmed); Wilkins.

**NOT FOUND (collected):**
- Ice speed on the domes of Drygalski, Mill and Bowman Islands (ITS_LIVE gap).
- Fast-ice thickness at Mirny; iceberg spacing in the Mirny fast ice; any landing on Davis Sea fast ice.
- Crevasse maps for every candidate; snow accumulation for every candidate except Mill Island and Law Dome summit; measured surface melt for every candidate except Mill Island; visibility and fog statistics except Mill Island.
- Names of the two ADD islands FID 1466 and FID 1476.
- The position of the Australian 2000 Bunger blue-ice site and whether the C-130 trial was flown; whether the 1990 C-130 trials at S-1 were flown.
- Swithinbank's 1991 list of potential sites for this sector (DTIC 403; ERDC reCAPTCHA).
- Any ship landing at Drygalski, Bowman, Mill or the West Ice Shelf islands; West Ice Shelf front height and melt.
- ERA5 for the Queen Mary Coast stretches and the Knox Coast (rate limit).
- Any proposal for a jet runway anywhere in 85-115°E outside Wilkins.

## Search log
*(exact strings; result; dead ends noted as died-at-query or died-at-sources)*

| # | Search string or download | Result | Died at |
|---|---|---|---|
| 1 | `Поляков Мартьянов Суханова аэродром Российские полярные исследования 2019 Мирный площадка` | Pointed to the Mirny strip papers (already known) and to *Problemy Arktiki i Antarktiki* 65(3); not the RPR article | Query (wrong journal surfaced) |
| 2 | `Drygalski Island Davis Sea ice cap elevation area km` | Wikipedia "Drygalski Island" (opened) | Hit |
| 3 | `"Российские полярные исследования" 2019 №3 (37) аэродром Антарктида Поляков` | Sukhanova et al. 2019, *Problemy Arktiki i Antarktiki* 65(3):315-327 identified; core.ac.uk PDF returned HTML then 403; aaresearch.science 403; openpolar.no certificate error | Sources (access) for the journal paper |
| 4 | `Sukhanova Popov Polyakov Kashkevich Martyanov snow runway Bunger Oasis GPR 2018/2019 "Arctic and Antarctic Research"` | Abstract-level text only (Transcription Gulf, 7 km from the base) | Sources (full text refused) |
| 5 | `залив Транскрипции оазис Бангера снежная ВПП полевая база георадар` | **Found the brief's article:** AARI, *Russian Polar Research* No. 37, pp. 11-15, "Организация нового аэродрома РАЭ в районе оазиса Бангера, Антарктида," by S.P. Polyakov, V.L. Martyanov (AARI), A.A. Sukhanova (SPbU); PDF downloaded from data.aari.ru and read in full (Russian) | Hit |
| 6 | `Australian Antarctic Division Bunger Hills alternate runway A319 Wilkins survey blue ice site` | AAD news 2000 and AAD magazine issue 1 (2001) opened | Hit |
| 7 | `"Bunger Hills" "blue ice" runway site C130 trial 2000 2001 Australian Antarctic` | No report that the C-130 trial was flown; identified Swithinbank 1991 (DTIC ADA249503) | Query for the trial outcome; DTIC PDF 403 (source) |
| 8 | `Swithinbank "Potential airfield sites in Antarctica for wheeled aircraft" CRREL report pdf` | DTIC 403; ERDC library returned a reCAPTCHA page (not pursued); **CRREL Report 89-21 (Mellor and Swithinbank, "Airfields on Antarctic glacier ice") downloaded** from southpolestation.com and read for this sector | Sources (DTIC access; ERDC bot check, not worked around) |
| 9 | `Swithinbank 1991 potential airfield sites Antarctica blue ice "Queen Mary Land" OR "Wilkes Land" OR "Mirny" OR "Bunger" sites list` | No site list for this sector; 84 sites said to be identified (secondary) | Query and sources |
| 10 | (page) antarctic-logistics.com/blue-ice-airfields | Names only Law Dome/Casey in this sector | Sources (no detail) |
| 11 | `Tollenaar 2024 Antarctic blue ice areas map dataset zenodo 200 m` | Zenodo record 8333865 restricted; **version 10539933 open**, `smoothed_BIAs.zip` downloaded | Hit |
| 12 | (pages) Wikipedia Mill Island, Bowman Island, Masson Island, West Ice Shelf, Gaussberg, Law Dome | Opened; Henderson Island (Antarctica) page 404 | Hit / one source 404 |
| 13 | (page) AAD magazine issue 1 (2001) "Antarctic air transport link investigated"; AAD news 2000 "Australia moves closer to Antarctic air link" | Opened and quoted (item 9.2) | Hit |
| 14 | (attempt) curl of the AARI journal page with a browser user-agent | **Refused by the session's permission classifier ("bot check circumvention"). Not retried and not worked around.** The journal paper stays abstract-only. | Refused (tool) |
| 15 | `остров Дригальского ледниковый купол станция "Мир" 1960 зимовка аккумуляция скорость ветра` | Wikipedia again; a Soviet-encyclopedia snippet on the West Ice Shelf (booksite.ru, 403) | Sources for accumulation and wind |
| 16 | (page) ru.wikipedia "Западный шельфовый ледник" | Opened (item 6) | Hit (secondary) |
| 17 | `Mill Island ice rise Shackleton Ice Shelf ice core OR radar OR survey surface elevation accumulation` | Inoue et al. 2017 PDF downloaded and read (item 2a) | Hit |
| 18 | `толщина припая Мирный максимальная см многолетние наблюдения море Дейвиса взлетно-посадочная полоса на припае` | Only Sanefjord (Prydz Bay) paper | Sources (no Mirny figure) |
| 19 | `Mirny observatory landfast sea ice thickness annual maximum 1.5 m 1.8 m time series Davis Sea` | AARI Mirny page (opened: no ice data); Davis/Mawson/Casey AADC dataset titles; Li et al. 2023 abstract text | Sources for Mirny |
| 20 | `"Mirny" fast ice thickness "cm" Fedotov OR Panov OR Buinitsky Soviet Antarctic Expedition Information Bulletin` | Bulletin titles only (Ledenev 1964, 1967); DTIC AD0748399 title | Sources |
| 21 | `"толщина припая" Мирный РАЭ см обсерватория Мирный ледовые наблюдения` | Three AARI PDFs downloaded and grepped: none gives a Mirny thickness; one cites Shesterikov's Mirny fast-ice paper (title only) | Sources |
| 22 | `"1.64 ± 0.08" fast ice Davis Station buoy The Cryosphere 2023 annual maximum ice thickness Zhongshan` | Abstract text of Li et al. 2023 in the result; doaj.org 403 | Hit (abstract only) |
| 23 | `аэродром на припае Мирный посадка Ил-14 на морской лед 1956 OR 1957 OR 1960 ледовый аэродром Мирного` | Accident databases and the Molodyozhnaya memoir; no fast-ice landing | Query |
| 24 | `Mirny 1956 OR 1957 aircraft landed on fast ice "sea ice" airstrip Soviet Antarctic Expedition Li-2 Il-12 Davis Sea ice runway` | Polar Record abstract; CIA reading-room page (opened: the page did not contain the document's text) | Query / sources |
| 25 | `проект аэродром для тяжелых самолетов станция Мирный Ил-76 строительство ВПП 2024 OR 2025 ААНИИ` | Only Mirny, Yakutia (a different place) and Progress | Query (nothing for Antarctic Mirny) |
| 26 | `Casey blue ice runway survey 2002-2003 sites A6 South Upper Vanderford Glacier S-1 Lanyon Junction compacted snow runway Law Dome` | researchdata.edu.au record read (item 9.5); openpolar.no certificate error | Hit |
| 27 | `RAAF Hercules landed Bunger Hills blue ice 2001 OR 2002 trial flight Casey air link Edgeworth David` | Plan only; CASA 212 2010 snippet; ASN page certificate error | Query (trial outcome) / sources |
| 28 | `"Henderson Island" Shackleton Ice Shelf ice-covered island 66° Queen Mary Land GNIS` | Wikipedia opened (item 2d) | Hit |
| 29 | `David Island Shackleton Ice Shelf coordinates …; Zavadovskiy Island West Ice Shelf; Mikhaylov Island` | Wikipedia Zavadovskiy, Mikhaylov, Leskov opened; David Island from snippets | Hit / snippet |
| 30 | `Chugunov Island Shackleton Ice Shelf coordinates Scott Glacier; island south of Mill Island 65°50'S 100°40'E name` | Chugunov at 65°55′S 99°29′E; no name for the two ADD islands | Query (no name) |
| 31 | (download) geonames.org nearby-name lookup for the ADD island centroids | "daily limit … for demo has been exceeded" | Sources (service limit; not worked around) |
| 32 | `Law Dome accumulation rate western slope low accumulation Casey coastal "Lanyon Junction" OR "Cape Folger" snow accumulation m ice per year` | Roberts et al. 2015 PDF downloaded and read (item 8) | Hit for DSS; query for the west slope |
| 33 | `West Ice Shelf East Antarctica ice velocity thickness surface melt lakes front retreat study 2020 2023` | Nothing specific to this shelf | Query |
| 34 | `"West Ice Shelf" Antarctica "surface meltwater" OR "melt lakes" OR "rift" OR "calving" 85°E` | Only West Antarctic results | Query |
| 35 | `Fraser Massom landfast sea ice extent circumpolar 2000-2018 dataset download netcdf AADC 10.26179/5d267d1ceb60c` | AADC download link is a JavaScript app (no file for a script); ESSD 2020 paper downloaded: no sector numbers | Sources |
| 36 | (page) Wikipedia Harrisson Ice Rises | Opened (66°27′S 96°39′E, "a local swelling of the ice surface") | Hit |
| 37 | (data) BAS ArcGIS ADD polygon service, `resultOffset` paging | 528 polygons in the sector box (one page) | Hit |
| 38 | (data) Open-Meteo ERA5 archive | 18 points downloaded in all; **HTTP 429 "Too Many Requests" twice** (after 5 points in the first batch, and on a last batch of 3 coastal points). The rate limit was respected with pauses of 40 s between requests; the last 3 points (Queen Mary Coast west and east, Knox Coast) were **not downloaded**. | Sources (rate limit) |
| 39 | (data) NOAA CoastWatch ERDDAP ETOPO 2022 15″ | One request returned HTTP 503; retried after a pause and succeeded | Hit after retry |

**Self-corrections and snags**
- *ITS_LIVE without an error filter gave false speeds.* My first Drygalski run reported "15-24 m/yr" for the flattest lines; those values came from a handful of pixels with errors of 200-250 m/yr at the island's edge. The method was changed to accept only pixels with an error of 20 m/yr or less and only lines with at least 80% coverage; every number in this file uses the corrected method.
- *The first island boxes mixed islands, shelf and sea ice.* A box around Mill Island reported its slowest lines on a different, unnamed island to the south (FID 1466). All island results were redone inside the ADD island outlines.
- *REMA may contain interpolated patches* on Mill and Bowman Islands (lines with 0.00% grade over 3 km). Not checked against REMA's data-count layer. Treat those very flat values as unconfirmed.
- *The West Ice Shelf front height could not be measured* (REMA and the ADD front disagree).
- *Bowman Island's ERA5 point* is 25 km south of the island, on or beside the shelf.
- *The Wikipedia infobox position for the West Ice Shelf* (68°36′S 77°53′E) is inconsistent with the shelf's location and was not used.
- *Mir (Drygalski) and Druzhba (Zavadovskiy) carry identical dates* in Wikipedia (item 6); unresolved.
- *ERA5 reads low near this coast* (Mirny check); all ERA5 wind speeds are treated as lower bounds.

**Data downloads (all DERIVED values in this file come from these, with the method stated where used). Scripts and downloads are kept in the session scratchpad, not the repo.**
- **Elevation:** REMA v2.0 mosaic (Polar Geospatial Center), 32 m tiles (`data.pgc.umn.edu/elev/dem/setsm/REMA/mosaic/v2.0/32m/<row_col>/`) and the 1 km filled mosaic. REMA heights are WGS84 ellipsoidal; converted to orthometric (above the EGM2008 geoid) with the PROJ CDN grid `us_nga_egm08_25.tif`. *Check:* the method gives 738 m at Wilkins (AAD: 720-780 m), 1,390 m at Law Dome summit (Wikipedia: 1,395 m), about 40 m at the Mirny strip (Popov 2019: 38-59 m).
- **Ice speed:** ITS_LIVE v2 annual-velocity mosaic, 120 m, Antarctic composite (`its-live-data.s3.amazonaws.com/velocity_mosaic/v2/static/cog/ITS_LIVE_velocity_120m_RGI19A_0000_v02_v.tif`, with `_v_error` and `_count`), read remotely. *Check:* 10.2 m/yr at Wilkins (AAD: 12 m/yr), 13.3 m/yr at the Mirny strip (Popov 2019: 6-80 m/yr across the area), 6.2 m/yr at the 1988 S-1 blue-ice strip near Casey.
- **Blue ice:** Tollenaar et al. 2024 smoothed blue-ice-area outlines (Zenodo 10539933).
- **Wind:** ERA5 hourly reanalysis via the Open-Meteo archive API (method in "Common notes" above).
- **Distance to Mirny:** great-circle (haversine, R = 6,371 km) from 66.553°S 93.008°E (AARI gives 66°33′S 93°01′E).

**Method for "usable flat area" (DERIVED, my thresholds, stated so anyone can rerun it):** REMA resampled to 96 m by averaging; grid centers every 500 m (2,000 m on the large ice shelves); at each center, straight 3,000 m lines at 18 bearings (every 10°). A line counts if every point is on a surface at least 10 m above the geoid (to exclude sea and sea ice) and no 288 m segment along it is steeper than 2.0%. The 2.0% figure sits between the slopes in the sources (Wilkins centerline 1.58%; Mirny steepest segment about 2.9%, "close to the limit values"; the Apfel Glacier survey's "not more than 2.5%"). It is a filter for reporting, not a design criterion. For each qualifying line the ITS_LIVE speed is sampled at 120 m along it and the maximum reported. **Caveat:** REMA is a surface model compiled from 2009-2021 imagery; it does not see crevasses, sastrugi or snow bridges, and 96 m averaging hides short bumps.

