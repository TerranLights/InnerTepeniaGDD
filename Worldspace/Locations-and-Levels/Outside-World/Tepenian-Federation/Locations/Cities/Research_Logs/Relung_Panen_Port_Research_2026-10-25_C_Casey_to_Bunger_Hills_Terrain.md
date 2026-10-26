# Research Log C: Casey to Bunger Hills, Distance and Terrain (Real-World Only)

- **Date of research:** 2026-10-25
- **Scope:** Real-world physical and logistical facts only. Nothing in this file describes the fictional setting.
- **Slice:** Distance and terrain between Casey Station (Windmill Islands, Budd Coast) and the Bunger Hills oasis (Knox Coast, Wilkes Land); terrain of the oasis; Denman Glacier crossing; precedent traverses; heavy-vehicle traverse figures.
- **Status labels:**
  - **SOURCED**: read at the source (page or PDF text), with the citation given.
  - **COMPUTED**: arithmetic shown, from SOURCED inputs. Scripts are in the session scratchpad (`calc/dist.py`), not in the repo.
  - **UNVERIFIED**: seen only in a search-engine summary or snippet, or in a secondary or popular source, and **not** read at a primary source. Do not build on these without checking them.
  - **NOT FOUND**: looked for and not found. The search log (section 4) says where.
- **Units:** km, m, m/yr (m a⁻¹), °C, t (metric tonnes), L. US units are kept where the source uses them, with conversions marked COMPUTED.

---

## 1. Findings summary

### 1.1 The headline facts

1. **The straight-line distance from Casey to the Bunger Hills is about 437–446 km**, depending on which Bunger Hills point is used (COMPUTED). This matches the Australian Antarctic Division's (AAD's) own figures of "about 440 km" and "about 450 km" (SOURCED), and its flight distance of "240 nautical miles" (444.5 km) to Edgeworth David base (SOURCED).
2. **The straight line does not stay on land.** Casey sits inside Vincennes Bay, a bay of about 9,000 km² that is 150 km east–west. Heading west, the line crosses the bay and passes about 33 km north of Cape Nutt, its western headland. A route on grounded ice has to swing south round the head of the bay, past the Vanderford Glacier. Measured through gazetteer points at the bay head, the shortest such dog-leg is about **468 km** (COMPUTED). That is a lower bound, not a surveyed route.
3. **The Denman Glacier is not on the Casey route.** It lies south-west of the oasis (gazetteer point 66.75°S, 99.5°E), and the Scott Glacier lies to the west. Both bar the route **west** toward Mirny and Davis, not the route east to Casey (SOURCED positions). The glaciers on the Casey side are the Vincennes Bay outlets (Vanderford, Adams, Anzac, Bond East and West, Underwood). Bond West reaches 3,339 m/yr at its terminus and has crevasse patterns "more typically observed across fast-moving Greenlandic glaciers" (SOURCED).
4. **No overland traverse between Casey and the Bunger Hills, or along the Knox Coast, was found in any language searched.** Access to the oasis has been by aircraft, helicopter, and ship-plus-helicopter since 1947 (SOURCED). The 1912 Western Base sledging party turned back on the Denman Glacier because each crevasse took "at least two hours to negotiate" (SOURCED).
5. **The oasis is about 952 km² in total, of which only 395 km² is land.** Marine bays take 470 km², lakes 36 km² and snow 51 km² (Simonov 1971, as cited 1990; SOURCED). The southern block of bare bedrock is 263 km² with a maximum altitude of 165 m (SOURCED).

### 1.2 Key-figures table

| # | Figure | Value | Unit | Source | Source date | Status |
|---|---|---|---|---|---|---|
| 1 | Casey coordinates | 66.282514°S, 110.526613°E | deg | Wikipedia "Casey Station" (AAD coordinates) | accessed 2026-10-25 | SOURCED |
| 2 | Bunger Hills center | 66.283°S, 100.783°E (66°17′S 100°47′E) | deg | Wikipedia "Bunger Hills" | accessed 2026-10-25 | SOURCED |
| 3 | Casey → Bunger Hills center, geodesic | 437.1 | km | Vincenty, WGS84, from rows 1–2 | 2026-10-25 | COMPUTED |
| 4 | Casey → Oazis/Dobrowolski station (66°16′29″S 100°44′49″E) | 438.7 | km | Vincenty, WGS84 | 2026-10-25 | COMPUTED |
| 5 | Casey → Edgeworth David (66°15′S 100°36′E) | 445.6 | km | Vincenty, WGS84 | 2026-10-25 | COMPUTED |
| 6 | AAD stated Casey → Edgeworth David | "approximately 440 km"; "about 450 km"; "240 nautical miles" (= 444.5 km) | km / nmi | AAD Field sites page; AAD news 2023, 2024; This Week at Casey 22 Dec 2023 | 2023–2024 | SOURCED (nmi→km COMPUTED) |
| 7 | Casey → Vanderford pt → Underwood pt → Oazis (around the bay head) | 467.8 | km | Vincenty, gazetteer points | 2026-10-25 | COMPUTED (lower bound, not a route) |
| 8 | Bunger Hills (Oazis) → Mirny | 346.8 | km | Vincenty; Mirny 66.553122°S 93.009724°E | 2026-10-25 | COMPUTED |
| 9 | Stated Oazis → Mirny | 350 (en.wiki), 360 (ru.wiki), 370 | km | Wikipedia; ru.wikipedia; Russian popular sources | various | SOURCED (3 different values) |
| 10 | Bunger Hills (Oazis) → Davis | 1,003.0 | km | Vincenty; Davis 68.576667°S 77.9675°E | 2026-10-25 | COMPUTED |
| 11 | Edgeworth David → Shackleton Ice Shelf | "85 km inland from the Shackleton Ice Shelf" | km | AAD Field sites page | accessed 2026-10-25 | SOURCED |
| 12 | Ship at Shackleton Ice Shelf barrier (Malygintsev / Milovzorov bays) → oasis | 90–110 | km | Lunev, Vorobyov & Kiselev, *Russian Polar Research* 4/2017 | 2017 | SOURCED |
| 13 | Oazis → Cape Elliott (eastern end of Shackleton Ice Shelf) | 94.7 | km | Vincenty; Cape Elliott 65°52′S 102°35′E | 2026-10-25 | COMPUTED |
| 14 | Vincennes Bay size | 120 km N–S × 150 km E–W, about 9,000 km²; entrance 105 km wide | km, km² | Wikipedia "Vincennes Bay" | accessed 2026-10-25 | SOURCED |
| 15 | Bond West Glacier velocity | 241 (inland) to 3,339 (terminus) | m/yr | Picton et al., *The Cryosphere* 17, 3593 (2023) | 2023 | SOURCED |
| 16 | Vanderford grounding-line retreat 1996–2020 | 18.6 km total (about 0.8 km/yr) | km | Picton et al. 2023 | 2023 | SOURCED |
| 17 | Oasis total area (ice-free incl. bays) | 952 (land 395; marine bays 470; lakes 36; snow 51) | km² | Filcek & Zieliński, *Polish Polar Research* 11 (1990), citing Simonov 1971 | 1990 | SOURCED |
| 18 | Southern bare-bedrock block | 263 km², max altitude 165 m | km², m | Klokov et al., *Polish Polar Research* 11 (1990) | 1990 | SOURCED |
| 19 | Prevailing heights, southern (mainland) part | 50–80 m a.s.l. | m | Andreev, *Russian Polar Research* 2/2020 | 2020 | SOURCED |
| 20 | Lake Figurnoye (Algae Lake) | 25 km long; 16 km² surface; to 137 m deep | km, km², m | 1990 (Simonov 1971); ru.wikipedia | 1990 | SOURCED (length conflicts with GNIS 17 km) |
| 21 | Mean annual air temperature | −11.2 (White Smoke Lake AWS, Jan 1992–Jul 1993); −9.1 (Rusin 1961) | °C | Doran et al., *Antarctic Science* 8 (1996); Klokov et al. 1990 | 1996; 1990 | SOURCED |
| 22 | Summer thawing degree-days | 71 °C-days; winter freezing 3,987 °C-days | °C-days | Doran et al. 1996 | 1996 | SOURCED |
| 23 | Permafrost table depth | 82–106 | cm | Alekseev & Abakumov, *Czech Polar Reports* 10(1) (2020) | 2020 | SOURCED |
| 24 | Max wind gust, Feb–Apr 1989 | 43 m/s (24 Feb 1989); strongest winds from the east | m/s | Filcek & Zieliński 1990 | 1990 | SOURCED |
| 25 | Denman Glacier | 11–16 km wide, 110 km long; bed to 3,500 m below sea level | km, m | Wikipedia "Denman Glacier"; AAD "Nudging a sleeping giant" | accessed 2026-10-25 | SOURCED |
| 26 | Denman tongue speed (2015–2022) | about 5 m/day (about 1,825 m/yr) | m/d | Thompson et al., *The Cryosphere* 17, 157 (2023) | 2023 | SOURCED (m/yr COMPUTED) |
| 27 | Casey → Dome C North traverse (2025) | 1,168 km; 643 t gross (493 t gear); 15–18 days expected | km, t, d | AAD "Long haul for science begins" | 2025 | SOURCED |
| 28 | Implied daily distance, row 27 | 65–78 | km/day | 1,168 / 18 and 1,168 / 15 | 2026-10-25 | COMPUTED |
| 29 | Concordia traverse (Challenger towing) | 6 L/km; tow 40–50 t at 7–18 km/h | L/km, t, km/h | G. Dargaud, Antarctic Traverse page | page updated 2025-10-27 | SOURCED |
| 30 | South Pole Traverse, fuel per delivered tonne-km | about 0.24 | L/(t·km) | from CRREL TR-16-4 (2016): 6,000 gal burned per tractor round trip, 18,000 gal delivered, 1,030 mi one way | 2016 | COMPUTED |

---

## 2. Findings by question

### Q1. Distances

**Method (COMPUTED):** WGS84 ellipsoid geodesic by Vincenty's inverse formula, cross-checked with a haversine on a 6,371.0088 km sphere. The two agree within about 0.4%. Coordinates come from Wikipedia and the AAD gazetteer as cited. A Python script is in the session scratchpad.

| From → To | Vincenty (km) | Haversine (km) | Initial azimuth |
|---|---|---|---|
| Casey → Bunger Hills center (66.283°S 100.783°E) | 437.1 | 435.3 | 265.5° |
| Casey → brief's point (66°15′S 100°45′E) | 438.8 | 437.1 | 266.0° |
| Casey → Oazis/Dobrowolski (66°16′29″S 100°44′49″E) | 438.7 | 437.0 | 265.6° |
| Casey → Edgeworth David (66°15′S 100°36′E) | 445.6 | 443.8 | 265.9° |
| Oazis → Mirny (66.553122°S 93.009724°E) | 346.8 | 345.4 | 261.3° |
| Bunger center → Mirny | 348.2 | 346.9 | 261.5° |
| Oazis → Davis (68.576667°S 77.9675°E) | 1,003.0 | 999.0 | 244.9° |
| Mirny → Davis | 677.4 | 674.8 | 243.7° |
| Oazis → Highjump Archipelago gazetteer point (66.0255°S 100.7356°E) | 27.8 | 27.7 | 358.9° |
| Oazis → Cape Elliott (65.867°S 102.583°E; eastern end of the Shackleton Ice Shelf) | 94.7 | | |
| Oazis → Shackleton Ice Shelf KBA center point (64.9888°S 96.1561°E) | 255.4 | 254.5 | 302.0° |
| Casey → Law Dome Summit South (DSS, 66°46′S 112°48′E) | 114.6 | 114.2 | 119.1° |
| Casey → Cape Nutt (66.633°S 108.2°E) | 110.9 | | |

**Stated distances to compare (SOURCED):**
- AAD Field sites page: Edgeworth David is "approximately 440 km west of Casey research station and 85 km inland from the Shackleton Ice Shelf."
- AAD news 2023 and 2024: "450 kilometers west of Casey" and "about 440km."
- This Week at Casey, 22 Dec 2023: helicopters "transit 240 nautical miles west of Casey Station" to Edgeworth David, and Basler flights take "240 nautical miles, or 1.5 hour flight." 240 nmi is 444.5 km (COMPUTED). This agrees with the computed 445.6 km to within 0.3%.
- The 2024 French inspection of Casey (ATCM 46 attachment): "Bunger Hills, 440 km from the Casey station."
- Mawson's Huts site: Casey is "about 450 kilometers" further east of the AAE Western Base area.
- Oazis to Mirny: "350 km to the west" (en.wikipedia, Bunger Hills); "360 км к востоку от Мирного" (ru.wikipedia, Dobrowolski station); "370 километров от Мирного" (Russian popular histories). The computed value is 347 km. The stated figures are probably rounded or describe flight tracks; the sources do not say which.

**Where the straight line runs (COMPUTED, plus SOURCED geography):**
- On a sphere, the great circle from Casey to the oasis bows slightly poleward. It stays between 66.28°S and 66.36°S along its whole length; the most southerly point, 66.355°S, is at about 105.6°E, 219 km from Casey.
- Casey lies inside Vincennes Bay. The bay's entrance runs from Cape Folger (66.133°S, 110.733°E; Wikipedia) to Cape Nutt (66.633°S, 108.2°E; Wikipedia/GNIS). At Casey's longitude the entrance line is at about 66.17°S, north of Casey (COMPUTED by linear interpolation). Heading west, the line crosses the bay. At 108.2°E it is at 66.336°S, about 33 km north of Cape Nutt, so it is over the sea there (COMPUTED).
- The bay head is far south of the line. The Vanderford Glacier gazetteer point is at 66.583°S, 110.433°E, about 34 km south of Casey; the Underwood Glacier point is at 66.656°S, 107.945°E (AAD gazetteer). A route on grounded ice must go round the head of the bay.
- Where the line makes landfall on the Knox Coast between 108°E and 104°E is **NOT DETERMINED**: no coastline dataset (ADD/MEaSUREs) could be opened in this session. At 103.55°E the line is at 66.34°S, about 34 km south of the Conger Glacier gazetteer point (66.033°S 103.55°E), which drains north into the eastern Shackleton Ice Shelf. That suggests the western part of the line is over grounded ice, but this is **not verified**.

**Plausible overland distances (COMPUTED lower bounds):**
- Casey → Vanderford Glacier point → Underwood Glacier point → Oazis: 33.8 + 110.5 + 323.5 = **467.8 km**.
- Casey → Vanderford point → Cape Nutt → Oazis: 33.8 + 99.1 + 334.6 = **467.5 km**.
- These pass through points on or near glacier termini and fast ice. Any route kept inland of the grounding lines and crevasse fields would be longer. No sourced figure was found for how much longer (**NOT FOUND**).
- **Mirny and Davis routes:** both must cross the Denman and Scott glaciers immediately west of the oasis (see Q5). Beyond those, the Mirny and Davis routes were not researched in this slice.

**Bunger Hills to the Shackleton Ice Shelf front:**
- SOURCED: "85 km inland from the Shackleton Ice Shelf" (AAD).
- SOURCED: the Russian 2016 (62nd RAE) plan was to unload from the ship in Malygintsev and Milovzorov bays north of the oasis, "на минимальном расстоянии в 90–110 км" (at a minimum distance of 90–110 km). The ship was in fact sent to Aurora Bay instead, "на расстоянии 250 км от полевой базы Оазис" (250 km from the Oasis field base) (Lunev et al. 2017).
- SOURCED: in 2020 the Russian party was landed "к ледяному барьеру шельфового ледника Шеклтона в заливе Малыгинцев" (at the ice barrier of the Shackleton Ice Shelf in Malygintsev Bay) from RV *Akademik Tryoshnikov*, then flown into the oasis by helicopter (Andreev 2020).
- SOURCED: the Shackleton Ice Shelf runs along about 384 km of coast from 95°E to 105°E. It projects about 145 km seaward in the west and 64 km in the east, and covers 33,820 km² (Wikipedia). The KBA factsheet gives about 350 km along-shore, 180 km and 80 km projections. AAD gives 34,000 km².

### Q2. Terrain on the line between Casey and the Bunger Hills

**Casey end, Windmill Islands and Law Dome (SOURCED):**
- Casey is on the Bailey Peninsula, Windmill Islands. The islands occupy "a rectangle roughly 15×30 km and contain about 75 km² of exposed rock" (AAD gazetteer, as returned in search; the Windmill Islands gazetteer page was not opened, so treat as UNVERIFIED).
- Law Dome is an independent ice dome east and south-east of Casey: summit 1,395 m (Wikipedia), "bounded by the Totten Glacier to the east and the Vanderford Glacier to the west."
- The DSS ice-core site is at 66°46′11″S 112°48′25″E, 4.7 km SSW of the summit, with accumulation of 0.69 m/yr ice equivalent (ESSD 14, 3313, 2022).
- Law Dome is **not on the Casey–Bunger line**. The line runs west, away from it. The Totten Glacier (67.0°S, 116.33°E; Wikipedia) is east of Law Dome and also **not on the line**.
- Wilkins Aerodrome is "on a plateau at approximately 750 meters above sea level and 67 kilometers southeast of Casey." The site "moves approximately 12 meters per year." The glacial-ice runway cannot be used in December and January "due to surface deformation of the runway at ground temperatures above −5°C" (French Article VII inspection report, ATCM 46, Feb 2024 inspection; SOURCED, PDF text read).
- The Casey–Law Dome traverse route was used in the 1970s and 1980s, and "old reports indicating the route is crevasse-free" (AAD magazine, issue 38, June 2020; SOURCED).

**Vincennes Bay outlet glaciers, the first obstacles west of Casey (SOURCED, Picton et al., *The Cryosphere* 17, 3593–3616, 2023):**
- Vincennes Bay is "situated on the Wilkes Land coast between 104 and 111° E" and is "drained by several marine-terminating outlet glaciers: Vanderford, Adams, Anzac, Bond and Underwood."
- Vanderford: "ice-surface velocity at box IN accelerating from 201 ± 39 to 264 ± 6 m yr−1 between 2000 and 2013." Its grounding line retreated 18.6 km between 1996 and 2020 (about 0.8 km/yr). The paper also reports "an undiscovered canyon at the front of Vanderford Glacier, estimated to be more than 55 kilometers in length, reaching a maximum depth of 2200 m."
- Anzac: "128 ± 1 m yr−1 inland … to a maximum of 331 ± 1 m yr−1."
- Bond East: grounding-line box 508 ± 42 m/yr (2006), 430 ± 66 m/yr (2009), 496 m/yr (2021).
- Bond West: "the fastest-flowing outlet glacier, accelerating rapidly from 241 ± 4 m yr−1 inland … to a maximum velocity of 3339 ± 2 m yr−1." Average 1,463 m/yr (2002–2021). It shows "a crevasse pattern more typically observed across fast-moving Greenlandic glaciers."
- Adams and Underwood: no single velocity values were extracted from the text read.
- Gazetteer: Vanderford is "about 9 km wide, flowing north-west in the south-east side of Vincennes Bay," at 66.583°S, 110.433°E, altitude 55 m. Underwood is at 66.656°S, 107.945°E, "between Snyder Rocks and Cape Nutt." Bond Glacier is at about 109.0°E (Wikipedia). All AAD gazetteer or Wikipedia; SOURCED.
- Wikipedia "Vincennes Bay": "much of Vincennes Bay lies deeper than 1000 m below sea level," with an "over-deepened glacial trough" up to 2,100 m deep locally. The bay is "marked by several large, steep glaciers near its head." The Knox Coast forms its western boundary, where (per search summary) "the East Antarctic ice sheet terminates in continuous ice cliffs" (UNVERIFIED, search summary only).

**Vincennes Bay sea ice (SOURCED):**
- The Vincennes Bay Polynya is a recurring coastal polynya. Strong winds "generate energetic waves capable of breaking surrounding sea ice from the inside-outward." Satellite records 2003–2022 show extreme wave-breakup events with reductions in sea-ice concentration lasting "at least one week" (Voermans et al., *Nature Communications*, 2026; abstract read at NORA).
- Fast ice near Casey with instrument buoys on it "broke out" on several occasions (UNVERIFIED, search summary of the same paper).

**Knox Coast, Vincennes Bay to the Bunger Hills (SOURCED unless marked):**
- The Knox Coast runs from Cape Hordern (100.52°E) to the Hatch Islands (109.28°E) (AAD gazetteer, read).
- The Glenzer Glacier (65.967°S, 103.25°E) and Conger Glacier (66.033°S, 103.55°E) drain "northward from Knox Coast into the eastern part of the Shackleton Ice Shelf" (Wikipedia/GNIS).
- On 25 March 2022 it was reported that the Conger Ice Shelf had collapsed about ten days earlier (Wikipedia "Conger Glacier"; UNVERIFIED at a primary source here).
- Cape Elliott (65.867°S, 102.583°E) is "an ice-covered cape marking the northern extremity of the Knox Coast … fronts on Shackleton Ice Shelf" (Wikipedia, via search summary).
- Bowman Island (65.28°S, 103.11°E; 186 km², about 39 km long) lies above the north-eastern Shackleton Ice Shelf (Wikipedia, via search summary).
- **Surface type along the Knox Coast** (blue ice, firn, sastrugi): **NOT FOUND** for this coast specifically. General facts: blue ice covers about 1% of the ice sheet, and "nearly 50% is located within 20 km of the grounding line." That figure comes from a search summary of a recent blue-ice mapping paper and is UNVERIFIED; it is not region-specific.
- **Elevations along a plausible route: NOT FOUND.** REMA and BedMachine profiles could not be queried (see search log). Sourced anchor points: Casey at sea level; Wilkins at about 750 m, 67 km SE; Law Dome summit 1,395 m (off-route); southern Bunger Hills bedrock up to 165 m. The Bunger Hills SPOT5 DEM box (100–101.85°E, 65.82–66.52°S) spans 5–410 m, and that box includes surrounding ice (AADC metadata). The ice sheet bounds the oasis on the south-east with "steep slopes" (en/ru Wikipedia).
- **Crevasse maps:** a pan-Antarctic Sentinel-1 deep-learning fracture map exists (Surawy-Stepney et al., *The Cryosphere* 17, 4421, 2023). It gives monthly maps at 50 m resolution, 2015–2022, including grounded ice, and its Fig. 4(e) covers the "Shackleton Ice Shelf and Denman Glacier." It reports "Approximately 85 % of type-B crevassing appears on grounded ice." No route-specific crevasse statistics for the Knox Coast were extracted (**NOT FOUND**).
- One AAD and editorial-adjacent summary reads: Bunger Hills' "location surrounded by the ice sheet, heavily crevassed glaciers and Shackleton Ice Shelf has ensured that sea- and land-based approaches are difficult and rarely attempted." This is attributed to Gore & Berg's 2020 *Antarctic Science* editorial (DOI 10.1017/S0954102020000115), but it was seen **only in a search-engine summary**; the publisher page returned 403. **UNVERIFIED wording.**

**Glaciers that bound the oasis itself (SOURCED):**
- Apfel Glacier (66.417°S, 100.583°E): "about 5 nautical miles (10 km) wide and 20 nautical miles (40 km) long, flowing west-northwest along the south flank of the Bunger Hills and terminating in Edisto Ice Tongue" (AAD gazetteer / Wikipedia).
- Edisto Ice Tongue lies "along the northwest margin of Bunger Hills" and "occupies the southwestern portion of Edisto Channel" (Wikipedia "Scott Glacier (East Antarctica)").
- Scott Glacier (66.5°S, 100.33°E): "7 nmi (13 km) wide and 20 nmi (37 km) long," flowing NNW "between Denman Glacier and Mill Island" (Wikipedia/GNIS).
- Shackleton system glaciers: "Denman, Scott, Northcliff, Roscoe and Apfel." There is "no clear margin between Scott Glacier and Apfel Glacier offshore of the Taylor Islands" (Thompson et al. 2023). Note that Roscoe (66.5°S, 95.33°E) and Northcliffe are far west of the oasis and not relevant to the Casey side.
- The 1990 Polish report names the bounding outflow glaciers as "Adisto, Apfel and Ramenhus" (Filcek & Zieliński 1990). "Adisto" is the Polish transliteration used in that report; it appears to correspond to Edisto. This equivalence is inferred, not sourced, so mark it UNVERIFIED.
- Highjump Archipelago: "rocky islands and rocks about 95 km long and 9 to 28 km wide, extending in a north-east direction off the Bunger Hills" (AAD gazetteer).
- "There's the Edisto Glacier to the west, the continental ice sheet to the south and east, and an ice shelf to the north." The marine area "opens up in summer, but it is surrounded by ice" (AAD, "Marine mystery in the Bunger Hills," 2024).

### Q3. Real overland traverses in the region

**Casey–Bunger Hills or along the Knox Coast: NOT FOUND.** No Soviet, Russian, Australian, US or Chinese overland traverse between Casey/Wilkes and the Bunger Hills, or between Mirny and the Bunger Hills, was found (see search log). Every documented access is by air or by sea plus air:
- **1947:** US Navy Operation Highjump. A PBM Mariner flying boat under Lt Cdr David E. Bunger landed on an unfrozen lake/inlet in February 1947 (Wikipedia; AAD gazetteer). SOURCED.
- **1956:** the Soviet reconnaissance group arrived by aircraft on 23 January 1956, with a temporary base about 20 km from the oasis. Six people under E. S. Korotkevich arrived by Li-2 aircraft on 19 September 1956, and Oasis station opened on 15 October 1956 (Russian popular histories; UNVERIFIED at a primary source).
- **Oasis/Dobrowolski supply (ru.wikipedia, SOURCED at that level):** "В летом переброска грузов производилась самолётами из Мирного на ледяной аэродром в 15 км от станции, откуда грузы доставлялись на станцию вертолётами." (In summer, cargo was flown from Mirny to an ice airfield 15 km from the station, then brought in by helicopter.) "В зимний период посадки тяжёлых и лёгких самолётов совершались непосредственно возле станции на лёд озера Фигурного." (In winter, heavy and light aircraft landed directly by the station on the ice of Lake Figurnoye.)
- **1979:** the Polish reactivation ended in evacuation to Mirny after a sudden change in the weather. The date is 17 March per en.wikipedia and 21 February per ru.wikipedia. **Conflict; unresolved.**
- **1988/89:** Polish biologists traveled with the 34th Soviet Antarctic Expedition on RV *Akademik Fedorov* via Mirny and arrived 4 Feb 1989. They worked 65 days, to 10 Apr 1989 (Filcek & Zieliński 1990). SOURCED.
- **2016 (62nd RAE):** support came from Aurora Bay, 250 km from the field base, instead of the planned 90–110 km, and this "негативно сказалось на выполнении плана исследований" (hurt the research plan). The helicopter could not stay at the base for long (Lunev et al. 2017). SOURCED.
- **2019/20 (65th RAE):** party landed by ship at the Shackleton barrier and flown in by helicopter (Andreev 2020). SOURCED.
- **2022–2025, Denman Terrestrial Campaign (AAD):**
  - Building supplies were "air-dropped" (search summary) and personnel "were flown to the site."
  - The camp was "constructed over 55 days by a small team" of five.
  - About 39 t of equipment went by C-17 to Wilkins, then by "snow vehicles and track trailers 70 kilometers to Casey," then by Basler for 240 nmi.
  - "300 drums" of fuel were pre-positioned. Up to about 40 people were at camp in the first season.
  - Satellite camps were reached by helicopter: the RAID drill site was "about 90 kilometers from the main Edgeworth David campsite."
  - All SOURCED from AAD news 2023–2024, except the air-drop wording.

**Precedent traverses from Wilkes/Casey (SOURCED unless marked):**
- **Wilkes Station → S-2 (1957):** S-2 was on Law Dome, "80km inland" ("A year at Wilkes," AAD magazine 13, 2007). The surveyed trail was "unbroken by crevasses," and S-2 was at 1,166 m elevation (search summary of a *Journal of Glaciology* IGY paper; publisher page 403; **UNVERIFIED**).
- **Wilkes 1958 traverse:** "a 600 km traverse to the south and west of the Windmill Islands … with two 'Weasels' and one 'Sno-cat' from September to November," with a return "via the Vanderford Glacier" (search summary of the same J. Glaciol. paper; **UNVERIFIED**).
- An AAD reminiscence gives a "three-month, 400 mile (640km) return trip inland, towards the Russian base at Vostok," with a sno-cat and two weasels at half-mile spacing. On it: "we broke through and looked down all we could see was the blue expanse of a huge crevasse underneath us, and we had three vehicles sitting on top." Elsewhere: "Ice thickness at one location measured only 15cm" ("A year at Wilkes"; SOURCED). The direction and route relative to the Knox Coast are not stated.
- **Wilkes → Vostok (1962, ANARE):**
  - "3000 kilometer, four-month" round trip with two 1943 M29 Weasels and two 1950 D4 tractors, six men.
  - Departed 17 Sep 1962, reached Vostok 18 Nov 1962; Wilkes to Vostok was "900 miles."
  - "During the first month they lost 24 days of travel."
  - Mechanical failures: a sheared oil-pump pin at 505 miles (two-day repair), and a blown pre-combustion chamber at 477 miles on the return with no spare.
  - Navigation: "bamboo guide posts left at two and a half mile intervals" (Wikipedia). The first 300 miles followed "markers placed every mile," and the surface had "sastrugi … up to five feet high" (AAD "Steak and onions").
  - **Fuel figures conflict.** Wikipedia and AAD "Ice Nomads" give "Weasels achieved two miles to the gallon and the tractors one mile per gallon." AAD "Steak and onions" gives tractors "one and a half miles to the gallon," weasels "two and a half." The gallon type is not stated.
- **Casey → Law Dome summit area (modern):**
  - "120 km inland," "about 1400 meters above sea level," "eight hours each way" with two Hägglunds and a tractor towing fuel, equipment and an accommodation van; nine people; 22–23 Sep 2021 (AAD 2021). Implied average 120 km / 8 h = 15 km/h (COMPUTED).
  - Casey→Law Dome Summit 118 km and Casey→S2 84 km (search summary of an AAD route list; UNVERIFIED).
- **Casey → Little Dome C / Dome C North (modern AAD heavy traverse):**
  - 2020 plan: five bespoke Caterpillar Challenger tractors (modified by William Adams), three groomers with GPR, 28 sleds; each tractor tows "80 tonnes," for "320 and 400 tonnes per traverse," at "90 kilometers per day"; route rises to 1,500 m at Law Dome, then descends toward the Totten Glacier, then climbs past 3,200 m. "It's very unlikely we'll encounter crevasses" (AAD magazine 38, 2020).
  - 2022/23: departed 23 Dec 2022; at 846 km by 4 Jan 2023 at 2,983 m; sastrugi "up to two meters high"; 2,321 km logged by 15 Feb 2023 (AAD; AAPP).
  - 2023/24: 40 t of materials (2024 inspection report).
  - 2025: "1168 kilometers to the drilling site, at Dome C North"; "six tractors and 20 sleds," "two snow groomers at the front"; "493 tonnes of gear" including 140 t of fuel (174,600 L); "643 tonnes (including tractors)"; departed 1 Nov 2025, "15–18 days." The route "passes Law Dome, goes through the Elcheikh Saddle." Implied 65–78 km/day (COMPUTED).
- **Mirny crevasse zone (SOURCED, Russian Geographical Society essay):** "Зона трещин в районе станции Мирный невелика – не более двенадцати километров" (the crevasse zone near Mirny is small, no more than twelve kilometers). The route is reconnoitered before every traverse and marked with poles every two kilometers.

**Soviet 1956–1959 interior traverses from Mirny** (Pionerskaya, Komsomolskaya, Vostok, Sovetskaya) are documented, but **none to the Oasis** was found.

### Q4. The oasis itself

**Extent and area:**
- Bounds: 65°58′–66°20′S, 100°20′–101°28′E (Filcek & Zieliński 1990, citing Wiśniewski 1981); en.wikipedia gives 100°20′–101°28′E, and ru.wikipedia gives 100°28′–101°20′E. Center 66°10′S 101°00′E per Klokov et al. 1990. SOURCED (bounds differ slightly between sources).
- Total about 952 km², split as land 395, marine bays 470, lakes 36 and snow 51 km² (Simonov 1971, cited by Filcek & Zieliński 1990). AARI paleopolar page: "общей площадью около 950 км2." Andreev 2020: about 950 km² of which about 450 km² land; about 50 km long and 20 km wide. Wikipedia: ice-free 450 km², "according to some sources even 750 or 942 km²," the larger values including marine areas. SOURCED.
- Southern block: "The largest area of the icefree bedrock (263 km²) is located in the southern part of the oasis and borders on the Adisto Glacier in the west, on Apfel Glacier in the south and on the continental ice slope in the east" (Klokov et al. 1990). The Wikipedia figure of about 300 km² for the southern part is less precise. SOURCED.

**Relief:**
- Southern part: "rather low with a maximum altitude of 165 m above sea level, the relief is not much pronounced. Ranges of smoothed hills and several shallow valleys are extending from east to west and to north-west" (Klokov et al. 1990). AARI paleopolar: "мелкосопочник высотой до 165 м" (low hills up to 165 m). SOURCED.
- Andreev 2020: southern mainland part "холмистым, с преобладающими высотами около 50–80 м" (hilly, prevailing heights about 50–80 m), "рассечена многочисленными узкими и глубокими долинами с крутыми или даже отвесными бортами" (cut by many narrow, deep valleys with steep or even sheer sides); hilltops covered with loose moraine. SOURCED.
- Moraine "занимают три четверти площади оазиса" (moraine deposits occupy three quarters of the oasis area); ten genetic types of Quaternary deposits were identified (Lunev et al. 2017). SOURCED.
- Kakapon Bay, the largest inlet, is "more than 400 km²" in area (Klokov et al. 1990). SOURCED.
- Biogeography dataset elevation range is 0–200 m (AADC metadata). SOURCED.

**Lakes and drainage (SOURCED):**
- "Hundreds of large and small lakes … total area of the lakes is about 36 km² covering 6–7% of the oasis bedrock" (Klokov et al. 1990). The other 1990 report says lakes cover 9% of the land surface. The two percentages differ.
- Lake Figurnoye (Algae Lake): "crosses all the teritory of the oasis along the length of 25 km, and its surface area is 16 squ.km" (Filcek & Zieliński 1990, citing Simonov 1971); depth to 137 m (ru/en Wikipedia). GNIS/Wikipedia "Algae Lake" gives "9 nautical miles (17 km)" long and 0.4–1.9 km wide. **Length conflict (25 vs 17 km); unresolved.** The search-summary claim that it is "the largest freshwater lake in all of Antarctica" is UNVERIFIED and not used.
- Algae River (Gibson, Gore & Kaup, *Polar Record* 38(205), 2002, abstract via search): "The 25-km-long Algae River is the third longest known in Antarctica after Onyx River … and Druzhby River." It "receives meltwater from the Antarctic ice sheet, Apfel Glacier, and ephemeral and permanent snow banks." Water flows through epiglacial lakes to Algae Lake, "which in turn has an outlet to Transkriptsii Gulf, a largely fresh-water, tidal epishelf lake connected to the ocean under the Edisto Ice Tongue and Shackleton Ice Shelf." Status: abstract via search summary; publisher page 403; **UNVERIFIED at source**.
- Transkripcii Bay: "never melting ice cover has a thickness of about 4 m and its upper water layer is of fresh water," and it is tidal (Filcek & Zieliński 1990). Water is two-layered: upper fresh water (0.3–1.0‰) over salt water (19‰), with H₂S at the bottom (Klokov et al. 1990).
- Epishelf lakes "deep (maximum depths from 68 to 122 m), cold (maximum recorded temperatures less than 1.2°C)" (search summary of Gibson & Andersen 2002; UNVERIFIED). White Smoke Lake has perennial ice 1.8–2.8 m thick (search summary; UNVERIFIED).
- Salinity: Salt Lake reached 78‰ (Filcek & Zieliński 1990, from E. Kaup). Saline lakes range 3.4–79.0‰ (Crossref abstract snippet of a 1993 *Antarctic Science* paper; UNVERIFIED).
- "Almost all small and a greater part of larger lakes are without any outflow. … There are only few permanent water streams" (Filcek & Zieliński 1990).
- Andreev 2020: "Летом здесь текут многочисленные ручьи и даже подобия рек, питающихся тающими снежниками или стекающими с ледника в виде многометровых водопадов" (in summer many streams and even river-like flows run here, fed by melting snowbanks or falling from the glacier as waterfalls many meters high).
- Freeze-up, 1989: small water bodies froze by the turn of the 2nd–3rd decade of February; large lakes began freezing at the end of February and early March and finished within ten days (Filcek & Zieliński 1990).
- "Only a few" lakes keep an ice cover all year. The "extent of glacier ice contact becomes the controlling factor" (Doran et al. 1996).

**Climate (SOURCED):**
- Doran et al. 1996 (AWS on White Smoke Lake, Jan 1992–Jul 1993): mean air temperature −11.2 °C; mean wind 4.6 m/s; solar flux 115 W/m²; summer degree-days above freezing 71 °C-days; winter freezing degree-days 3,987 °C-days. They describe the oasis as "in a marginal climatic region for the persistence of thick lake ice."
- Klokov et al. 1990 (citing Rusin 1961): "Mean annual air temperature is −9,1°C. The ground temperatures are above freezing point during four months." Lowest relative humidity 12%, potential evaporation "450—600 mm per year," annual net radiation positive at 35–40 kcal/cm².
- AARI paleopolar: monthly mean air temperatures up to +1.6 °C in summer and down to −20.6 °C in winter; potential evaporation 400–600 mm/yr against about 200 mm of annual precipitation.
- Filcek & Zieliński 1990, Feb–Apr 1989:
  - Max +7.9 °C (10 Feb 1989); min −31.9 °C (26 Mar 1989).
  - Only two days with a minimum above 0 °C; on 35 days wind did not exceed 10 m/s; on 12 days it was above 20 m/s.
  - "Strongest winds blew from the East." Max 43 m/s (24 Feb 1989).
  - Snow cover peaked at 40 cm (19 Mar 1989) and was then largely blown away within a few windy days.
- Andreev 2020: in the anomalously warm summer of 2019/20, daytime January temperatures were usually 7–8 °C, sometimes 10 and "даже 13 градусов" (even 13 degrees). It rained twice in January, called "небывалое явление" (an unheard-of event). Dark rock and soil "могут нагреваться солнцем до 30 и более градусов" (can be heated by the sun to 30 degrees or more). Because of high summer temperatures and periodic winter storms, the oasis is snow-free nearly all year.
- Wind direction: strong winds (>10 m/s) "dominantly blow from 118 ± 21 degrees true," and tafoni orientations are 101 ± 18°T over 686 measurements at 28 sites (Gore and co-authors, *Antarctic Science* 32(2), 2020, abstract via search summary; the AADC dataset record was read and confirms AWS data from Edgeworth David 1986 and Apfel Glacier 2000). The numbers are UNVERIFIED at the publisher.
- DTC 2024: base camp average "−10, −15° Celsius"; Mt Strathcona "blows 40 knots, it's −20° Celsius"; "very challenging" weather in the final three weeks (AAD 2024).

**Soils, permafrost and vegetation (SOURCED unless marked):**
- Permafrost table depth is 82–106 cm in the Bunger Hills (Alekseev & Abakumov 2020, abstract read). Andreev 2020: "грунт местами оттаивает до глубины 140–160 см" (the ground in places thaws to 140–160 cm).
- Soils: "predominantly coarse structure and low organic carbon content, with alkaline to almost neutral pH" (Polar Science 2024, Larsemann and Bunger Hills; search summary; UNVERIFIED). "Very limited ornithogenic transfer … due to the absence of penguin rookeries and very rare nesting of flying birds." Total carbon is 0.70–2.43% (search summary of Abakumov et al.; UNVERIFIED). "A high content of available forms of phosphorus and potassium in ornithogenic and non-ornithogenic soils was found" (Nizamutdinov, Andreev & Abakumov, EJSS 2021, abstract page read).
- Salts: "The distribution of halite and thenardite acts as a major control on the geomorphology, sediment geochemistry and biogeography" (Crossref abstract snippet, *Antarctic Science* 2020; UNVERIFIED).
- Vegetation: "Mosses and lichens were most abundant around the ice margins where fresh snow and ice meltwater are abundant." In the salty, wind-abraded center they are "reduced in abundance and diversity" (Leishman, Gibson & Gore 2020, abstract via search; UNVERIFIED at publisher). Where lichens occur in favorable conditions "they may cover 75% of the surface area of the rocks," but are absent over large stretches (Filcek & Zieliński 1990). Andreev 2020 counts 64 lichen species, "второй по богатству в континентальной Антарктиде" (second richest in continental Antarctica, after Schirmacher), and found in sheltered moist places "неожиданно развитый и сомкнутый растительный покров из лишайников и мхов" (an unexpectedly developed, closed cover of lichens and mosses).
- Birds: snow petrel about 2,000 pairs; Wilson's storm petrel and south polar skua nest. Weddell seals use Rybij Chvost Bay (Filcek & Zieliński 1990).
- History: the oasis was ice-free at the Last Glacial Maximum per one study (*Geology* 2001), but glaciated during the last glaciation per another (*Antarctic Science* 1992). Holocene deglaciation is dated from about 10 ka. **These conflict in the literature.** The ice-sheet margins have been "approximately their present size" for at least 5–6 ka (ASAC 275 abstract via search; UNVERIFIED).

**Agriculture or large-scale construction:**
- **No source was found that assesses the Bunger Hills for agriculture or for large-scale construction (NOT FOUND).**
- The nearest sourced facts:
  - Low organic carbon, coarse soils, salt-controlled biogeography, an active layer under about 1 m, and four months of above-freezing ground temperature (all above).
  - General, not Bunger-specific: Antarctic soil "was of too poor quality for most crops beyond mustard and cress, and it typically lost its fertility after a year or two" (The Conversation, 2022, via search summary; UNVERIFIED). This refers to historical station soil gardening, not to this oasis.
- Construction precedent in the oasis (SOURCED):
  - Soviet/Polish Oasis station: two connected Shaposhnikov houses on stone foundations plus a third PDSh-4 house; met site at 29 m (ru.wikipedia).
  - Oasis-2: "only 300 m from the Polish station" (Filcek & Zieliński 1990).
  - Edgeworth David: summer refuge for "up to 8" (Wikipedia). The DTC camp added four "melon" huts, ten tent platforms and a kitchen-tent foundation for up to 40 people (AAD 2023).
  - Fuel and contaminant persistence: a synthetic oil spilled at a Bunger Hills helipad showed "no degradation evidence" ten years on (Crossref abstract snippet, *Antarctic Science* 1999; UNVERIFIED).

### Q5. The Denman Glacier crossing

- **Position (SOURCED):** Denman Glacier gazetteer point 66.75°S, 99.5°E, "east of David Island" (Wikipedia). The oasis center is about 77 km NE of that point (COMPUTED). Scott Glacier (66.5°S, 100.33°E) is about 31 km SW of Oazis (COMPUTED). Both lie between the oasis and Mirny/Davis. **Neither is on the Casey side.**
- **Dimensions:** 11–16 km wide, 110 km long; bed 3,500 m below sea level (Wikipedia; AAD). Ice front "35 km wide" (Miles et al., *The Cryosphere* 15, 663, 2021). The Landsat-visible ice stream extends "250 km from south of Mount Strathcona (67.5°S, 99.2°E) through to the northern boundary of Shackleton Ice Shelf (65.3°S, 99°E)" (N. Young, *Annals of Glaciology*, 1989, abstract via search; UNVERIFIED at publisher).
- **Speed:** the tongue is about 5 m/day (2015–2022) (Thompson et al. 2023). Speed near the grounding line rose 17 ± 4% between 1972–74 and 2016–17 (Miles et al. 2021). The "previously observed increase in the ice flow speed of the Denman Glacier has not continued beyond 2008" (Thompson et al. 2023, via search summary). Grounding-line speeds "approach 1.4 km/yr" (search summary; UNVERIFIED).
- **Grounding line:** retreated 5.4 ± 0.3 km between 1996 and 2017–18 (Brancato et al. 2020, *GRL*; JPL news, 25 Mar 2020). "Denman's eastern flank is protected … by a roughly 6-mile-wide (10-kilometer-wide) ridge under the ice sheet"; the western flank "sits over a deep, steep trough" (JPL). SOURCED.
- **Shear margins and crevassing (SOURCED):**
  - "The surface of the Denman Glacier tongue is heavily fractured with a combination of crevasses, flow lines and channel-like features." There is "a new area of intense crevassing along the northern glacier margin," and "new areas of crevassing are also evident in the grounding zone" (search-summary wording of the Shackleton-system papers; the Thompson et al. 2023 text read confirms rifting and shear-margin damage, so treat these specific phrases as UNVERIFIED wording).
  - "In 1974, the ice tongue was intensely shearing against Chugunov Island, as indicated by the heavily damaged shear margins"; rifts R1–R7 on the tongue (Miles et al. 2021).
  - Shear margins migrated laterally by about 5 km east and west over time (search summary; UNVERIFIED).
- **1912 crossing attempt (SOURCED, Mawson, *The Home of the Blizzard*, ch. 21, Western Base, AAD online text):**
  - The Denman Glacier, "moving much more rapidly than the Shackleton Shelf, tore through the latter and, in doing so, shattered both its own sides and also a considerable area of the larger ice sheet."
  - It sweeps "down for forty miles from over three thousand feet," and is "twelve miles in breadth."
  - "An enormous chasm over one thousand feet wide and from three hundred feet to four hundred feet deep." Crevasses ran "up to two hundred feet in width."
  - Progress fell to "one thousand and fifty yards" on 26 November and "a miserable four miles" on 17 November 1912.
  - The party turned back because crossing "would be by lowering the gear piecemeal into chasms fifty to one hundred feet deep, and hauling it up on the other side; each crevasse taking at least two hours to negotiate."
  - Wikipedia: they "couldn't reach [Cape Hordern] due to crevassing on Denman and Scott Glaciers."
- **Modern on-glacier work (SOURCED):** DTC field camps on and near the Denman were reached by helicopter. Teams "carefully probed for crevasses before commencing measurements" (search summary of an EGU blog; UNVERIFIED wording). The RAID drill went "over 203 meters through the glacier" at a site about 90 km from base (AAD).
- **Crevasse-detection methods tested in East Antarctica (abstract via search; UNVERIFIED at publisher):** on the Totten Glacier, 80 MHz helicopter GPR detected crevasses "up to a depth of 70 m, with snow bridge thickness of >30 m." TerraSAR-X detected "100% of crevasses with snow bridges of up to 4m thick and … 95% … up to 10 m thick" (*Cold Regions Science and Technology* 178, 2020).
- **Engineering assessment of a vehicle crossing of the Denman: NOT FOUND.** No route survey or trafficability study was found in English, Russian or Chinese.

### Q6. Heavy-vehicle routes in East Antarctica, and comparable figures

**All of these routes run in summer only:** the SPoT season, Concordia "2-3 times a summer," Progress–Vostok December–February, and Casey traverses Nov–Feb. **No year-round heavy overland route in Antarctica was found (NOT FOUND).**

| Route | Length | Duration / speed | Load | Fuel | Source | Status |
|---|---|---|---|---|---|---|
| McMurdo–South Pole (SPoT) | 1,030 mi one way (1,658 km); "has grown from 1,028 to 1,030 miles" | about 25 days out, about 10 back; bladder train steady state 7.8–8.1 mph (12.6–13.0 km/h) in a test | 24,000 gal fuel outbound per tractor (168,000 lb payload; gross 181,000 lb) | "approximately 6000 gal. each tractor consumes per round trip"; delivers 18,000 gal per tractor | Lever et al., ERDC/CRREL TR-16-4 (Feb 2016) PDF text; Wikipedia | SOURCED |
| SPoT derived | 1,658 km × 2 | | 18,000 gal delivered ≈ 126,000 lb ≈ 57.2 t (7.0 lb/gal from Table 2) | 22,712 L per tractor round trip → about 6.85 L/km averaged over the round trip; about 0.24 L per delivered t·km (one-way basis) | from the row above | COMPUTED |
| SPoT fleet | | | 2008–11: "average annual payload of 768,000 lb" (348 t) by 8 tractors, offsetting about 30 LC-130 flights a year; net benefit $2.0M/yr | | CRREL TR-16-4 | SOURCED |
| SPoT other ratios | | | | "0.56 lb fuel per lb fuel delivered"; "1.25 lb fuel per lb cargo" | search summaries of CRREL documents | UNVERIFIED |
| Cap Prud'homme–Concordia (IPEV/PNRA) | about 1,100 km | 12–15 days on the first trip; 100–120 km/day; 14 h/day driving; Challengers 7–18 km/h loaded, 30 km/h empty | Challenger 320 hp, 15 t, tows 40–50 t; about 400 t net per year | "about 6 l/km (about 0.4 mpg) while towing" | G. Dargaud (page updated 2025-10-27); ESA Concordia blog 2018 | SOURCED |
| Concordia derived | | | 40–50 t towed | 6 / 50 to 6 / 40 = 0.12–0.15 L per towed t·km | from the row above | COMPUTED |
| Concordia crevasses | a crevasse area about 200 km inland "is now avoided by driving around it" | | | | Dargaud; ESA | SOURCED |
| Casey–Dome C North (AAD, 2025) | 1,168 km, sea level to 3,233 m | 15–18 days planned; 65–78 km/day (COMPUTED); 2020 plan 90 km/day | 643 t gross; 493 t gear; 80 t per tractor (2020 plan) | 140 t (174,600 L) fuel carried; consumption not stated | AAD 2020, 2025 | SOURCED / COMPUTED |
| Zhongshan–Kunlun (CHINARE) | "1260多公里" (1,260+ km); also given as about 1,231 km and 1,300 km | 33rd CHINARE: "16天" (16 days); 32nd: 15 days for 1,200+ km | PistenBully 300 "30–35 t" and Challenger MT865B "50–60 t" carrying load; Kunlun construction "12辆雪地车运送600多吨物资" (12 vehicles, 600+ t) | **NOT FOUND** | CMA news 2017-01-01 (read); other values via search summaries | SOURCED (16 days, 1,260 km) / UNVERIFIED (rest) |
| Progress–Vostok (RAE) | 1,460 km ("1460 км от береговой станции Прогресс") | supply depots at 550 and 1,100 km; 2008 trial with 2 PistenBully Polar 300 in 10 days | 6,800 t unloaded at Progress for the new Vostok complex | **NOT FOUND** | Roshydromet news 30 Dec 2021 (read); 2008 trial via search summary | SOURCED / UNVERIFIED |
| Mirny–Vostok (historic Soviet) | about 1,400–1,500 km | "more than a month"; 12–15 km/h train speed | AT-T: about 20 t, 5 t in cab, tows up to 40 t; Kharkovchanka 35 t, over 500 hp, tows up to 60 t; first convoy 5 AT-T with 125 t | **NOT FOUND** | Roshydromet "200 years" page (read: weights, loads); speeds and durations via popular sources | SOURCED (vehicle specs) / UNVERIFIED (speeds) |
| Wilkes–Vostok (1962) | 3,000 km round trip | 4 months; 24 travel days lost in month 1 | 2 Weasels, 2 D4 | 1–2.5 mpg (conflicting) | AAD; Wikipedia | SOURCED (conflict noted) |

---

## 3. NOT FOUND and open threads

1. **Any overland traverse Casey/Wilkes ↔ Bunger Hills, Mirny ↔ Bunger Hills, or along the Knox Coast.** Searched in English and Russian; Chinese is not relevant to this coast. Died at the sources: the queries returned results, and none describes such a traverse. The 1958 Wilkes "600 km traverse to the south and west of the Windmill Islands" (UNVERIFIED) is the closest lead. **Open thread:** read Cameron, "Glaciological Studies at Wilkes Station," *Antarctic Research Series* 2 (1964/1971, AGU), and the *Journal of Glaciology* IGY Wilkes paper, for its route and whether it reached the Knox Coast.
2. **Surface elevation profile and slope along a Casey–Bunger route.** REMA was not queryable: the ArcGIS ImageServer host would not resolve from WebFetch, and Bash has no network. **Open thread:** sample REMA or BedMachine v3 along the computed great circle and the dog-leg.
3. **Coastline crossing points of the straight line** between 104°E and 110°E. Needs ADD or MEaSUREs coastline and grounding line data.
4. **Ice velocity (MEaSUREs) along the route inland of the Vincennes Bay glaciers,** and how far inland each glacier must be crossed to find slow ice. Not extracted.
5. **Crevasse-zone extents along the Knox Coast** from the Surawy-Stepney et al. 2023 fracture maps. The dataset exists but was not opened.
6. **Surface type (blue ice / firn / sastrugi) on the Knox Coast.** Not found specifically.
7. **Engineering or trafficability assessment of crossing the Denman or Scott glaciers.** Not found.
8. **Agriculture or large-scale-construction assessments for the Bunger Hills.** Not found.
9. **Zhongshan–Kunlun and Progress–Vostok fuel per km or per tonne-km.** Not found.
10. **Conflicts left unresolved:**
    - Algae/Figurnoye Lake length: 25 km vs 17 km.
    - 1979 evacuation date: 17 Mar vs 21 Feb.
    - Oazis–Mirny distance: 350, 360 or 370 km stated vs 347 km computed.
    - 1962 traverse fuel economy figures.
    - Lake share of the land surface: 6–7% vs 9%.
    - Whether the oasis was ice-free at the LGM: *Geology* 2001 vs *Antarctic Science* 1992.
11. **Publisher pages blocked (HTTP 403)** for every Cambridge *Antarctic Science*, *Polar Record* and *Journal of Glaciology* item, so the 2020 Bunger Hills special issue was seen only as abstracts or snippets. **Open thread:** obtain the full texts of the 2020 special issue, Gore & Berg (eds.), *Antarctic Science* 32(2): salt/weathering, biogeography, human occupation, tafoni, postglacial water bodies, and the 60-years-of-geology review.
12. **Florinsky & Zharnova (2025), "Geomorphometry of the Bunger Hills," *Advances in Polar Science* 36(2): 95–112** (REMA-based slope and catchment maps). The PDF is 53 MB and exceeded the fetch limit. **Open thread:** download locally for slope statistics.

---

## 4. Search log

Format: query or URL → result → where it died (Q = at the query, no relevant results; S = at the sources, results found but not usable or blocked; OK = useful).

**Distances and coordinates**
1. `Casey station coordinates latitude longitude Australian Antarctic Division` → Wikipedia, GLOSS, USGS → OK (66.282514°S 110.526613°E).
2. `Mirny Station coordinates 66°33′S 93°00′E` → Wikipedia → OK.
3. `Davis station coordinates 68°34′36″S 77°58′03″E` → Wikipedia → OK.
4. `Shackleton Ice Shelf location coordinates extent ice front latitude` → Wikipedia, KBA → OK (both fetched).
5. `Edgeworth David base Bunger Hills access helicopter from Casey distance km` → AAD field sites, news → OK.
6. `"Bunger Hills" "Casey" 400 km OR 450 km OR 440 km` → irrelevant motor-racing pages → died Q.
7. `Law Dome Summit South DSS ice core coordinates 66°46'S 112°48'E elevation` → ESSD 2022 → OK.
8. `Cape Nutt Antarctica coordinates Knox Coast Vincennes Bay western entrance` → Wikipedia → OK.
9. `Cape Elliott Knox Coast Shackleton Ice Shelf eastern end coordinates` → Wikipedia, KBA → OK.
10. Fetch `wikimili.com/en/Cape_Folger` → 404 → died S. Fetch `en.wikipedia.org/wiki/Cape_Folger` → OK.
11. Fetch `data.aad.gov.au/aadc/gaz/search_names_action.cfm?feature_name=Elliott…` → HTTP 500 → died S.
12. Python geodesics (Vincenty WGS84 and haversine) → OK. The first run failed on a variable-shadowing bug (loop variable `b` overwrote the ellipsoid semi-minor axis); fixed and rerun. Logged as a self-correction.

**Terrain, glaciers, ice**
13. `Denman Glacier ice velocity shear margin crevasses Bunger Hills` (extended) → TC 2023, TC 2021, Annals → OK.
14. Fetch TC 17/157/2023 (Thompson et al.), twice: once general, once term-specific → OK.
15. `Apfel Glacier Bunger Hills Edisto Inlet Highjump Archipelago gazetteer` → AAD gazetteer, Wikipedia → OK.
16. Fetch Wikipedia Scott Glacier (East Antarctica), Apfel Glacier, Roscoe Glacier, Denman Glacier, Glenzer Glacier, Vincennes Bay, Totten Glacier, Law Dome → OK.
17. `Knox Coast Wilkes Land glaciers Underwood Glacier Adams Glacier Bond Glacier Vanderford Glacier longitude` (extended) → TC 2023 Vanderford, gazetteer → OK.
18. Fetch TC 17/3593/2023, twice (the summary's "similar velocity range" claim was suspect, so re-queried for verbatim values) → OK. Self-correction: discarded the first summary's "similar range" statements.
19. Fetch Durham e-thesis PDF (Picton) → exceeded 10 MB → died S.
20. `Knox Coast definition Cape Hordern Hatch Islands longitude` → gazetteer → OK.
21. `glacier "Knox Coast" flowing into Shackleton Ice Shelf OR Vincennes Bay gazetteer narrative` → Glenzer, Vincennes Bay → OK.
22. `"Knox Coast" island OR peninsula OR bay "106°" OR "105°" OR "104°" E …` → only the Knox Coast record → died Q (no coastal features at 104–106°E surfaced).
23. `Conger Glacier Knox Coast coordinates Shackleton Ice Shelf Bowman Island` → Wikipedia (via summary) → OK, partially UNVERIFIED.
24. `Knox Coast ice sheet surface elevation profile inland Bunger Hills to Vincennes Bay ice divide Law Dome saddle` (extended) → *Nature Geoscience* 2025 (PMC) → fetched; no route profile → died S.
25. REMA: `curl` to `di-pgc.img.arcgis.com/.../REMA_Mosaic/ImageServer` → 404. `REMA mosaic ImageServer arcgis rest services …` → elevation2.arcgis.com. `curl` → no network in Bash (HTTP 000). WebFetch identify → ENOTFOUND → died S.
26. `crevasse map Antarctica deep learning Sentinel-1 East Antarctica Wilkes Land …` (extended) → TC 17/4421/2023 → fetched; no region statistics → partial.
27. `"Glaciological setting of the Queen Mary and Knox coasts" The Cryosphere final paper` → the preprint is the same work as TC 17/157. Preprint PDF over 10 MB → died S (final version read instead).
28. `Casey station traverse route "crevasse" Law Dome A028 S2 Wilkes skiway inland route hazards` (extended) → AAD magazine 38 → OK.
29. `Vincennes Bay polynya fast ice Casey sea ice season breakout winter open water` → Voermans et al. 2026 → NORA abstract read → OK.
30. `Shackleton Ice Shelf polynya fast ice Bunger Hills Davis Sea Mill Island Knox Coast polynya landfast ice extent` → general only → died S.
31. `blue ice areas East Antarctica map Wilkes Land Knox Coast Bunger Hills blue ice extent Hui Winther` → general continental figures only → died S for region.
32. `"Form, structure and stability of the margin of the Antarctic ice sheet, Vestfold Hills and Bunger Hills" abstract` → ASAC 275 summary only → partial (UNVERIFIED).
33. `Denman Glacier grounding zone velocity "m/yr" … Brancato 2020 …` (extended) → TC preprint, JPL → JPL fetched → OK.
34. `"Surface velocities of Denman Glacier, Antarctica, derived from Landsat imagery" abstract …` → abstract via summary → UNVERIFIED.
35. `Denman Glacier shear margin width crevassed zone kilometers surface velocity MEaSUREs "km wide" …` → JPL eastern-flank ridge; no margin widths → partial.
36. `egusphere-2026-4768` PDF → Austrian Alps crevasse inventory, irrelevant → dead end (died S).

**Traverses**
37. `Wilkes Station Vostok traverse 1962 Australian tractor Sno-Cat distance days` (extended) → AAD Ice Nomads, Wikipedia, Steak & onions → all fetched → OK.
38. `overland traverse Mirny to Bunger Hills Oasis tractor` (extended) → nothing specific → died S.
39. `Casey station traverse Law Dome summit tractor distance km crevasses` (extended) → AAD 2021, inland traverse page, 2025 → all fetched → OK.
40. Fetch AAD "Long haul for science begins" (2025), AAPP 2023, "Australia's modern inland traverse" → OK.
41. `Wilkes Station 1957 1958 IGY traverse inland S-2 tractor route crevasses Vanderford` (extended) → J. Glaciol. IGY paper; Cambridge 403 → died S (UNVERIFIED summary only).
42. `"Wilkes Station" 1958 traverse "600 km" Weasels Sno-cat …` → "A year at Wilkes" fetched → OK. NZ Antarctic Society 1958 PDF over 10 MB → died S.
43. `Australasian Antarctic Expedition Western Base Wild eastern sledging journey Denman Glacier crevasses 1912` (extended) → Gutenberg full text (fetch read only the front matter; 908k characters) → switched to the AAD chapter 21 text → OK. Wikipedia "Western Base party" had no journey detail → died S. Mawson's Huts "Floating fortresses" had no journey detail → died S.
44. `"Bunger Hills" traverse overland vehicle OR tractor OR quad OR skidoo Casey OR Mirny route sea ice` (extended) → AAD logistics pages → OK (air access only).
45. `overland journey Mirny to Wilkes Station OR "Bunger Hills" sledge tractor 1957 1958 1959 coastal traverse Knox Coast` (extended) → nothing → died S. Fetch Wikipedia "3rd Soviet Antarctic Expedition" → no Oasis transport detail → died S.
46. Russian: `станция Оазис 1956 оазис Бангера санно-гусеничный поход Мирный` (extended) → ru.wikipedia, popular histories → OK (air supply only).
47. Russian: `поход в оазис Бангера на тракторах из Мирного 1956 Коротков OR Короткевич "оазис Бангера" вездеход` (extended) → popular histories (air arrival) → no traverse → died S.
48. Russian: `ледник Денмана трещины переход поход Мирный оазис Бангера тягач` (extended) → children's-encyclopedia retelling of AAE → no modern crossing → died S.
49. Russian: `санно-гусеничный поход Прогресс Восток 2020 тонн топлива км дней тягачи PistenBully расход топлива` (extended) → Roshydromet pages fetched → OK (no fuel rate).
50. Russian: `санно-гусеничный поход Мирный Восток 1400 км суток скорость км/ч расход топлива тягач Харьковчанка зона трещин у Мирного` (extended) → RGO essay fetched (Mirny crevasse zone ≤12 km) → OK. `antarctic.su` book page → TLS certificate expired → died S. `ekaykin.livejournal.com/120310.html` → socket closed → died S.
51. Chinese: `中山站 昆仑站 内陆冰盖 车队 1300公里 天 吨 雪地车 燃油` (extended) → CAS and CMA news → CAS URL 404 (died S); CMA 2017 fetched → OK (16 days, 1,260 km).
52. Chinese: `昆仑站队 雪地车 油耗 每公里 升 中山站 出发 冰裂隙区 内陆出发基地 天抵达` (extended) → no fuel rates → died S. chinanews 2012 fetch → garbled summary, not used → died S.
53. `Zhongshan Kunlun traverse PistenBully 300 Polar tonnes fuel per km days 1300 km …` (extended) → load figures via summary (UNVERIFIED). sciencepoles.org TLS mismatch → died S. BAS tractor-train page returned empty → died S. zh.wikipedia Kunlun → no traverse data → died S.

**Heavy-vehicle figures**
54. Fetch Wikipedia "South Pole Traverse" → OK.
55. `South Pole Traverse fuel efficiency gallons fuel delivered per gallon consumed tractor CRREL Lever` (extended) → CRREL TR-16-4 PDF saved and pdftotext extracted → OK. DTIC ADA602402 (economic analysis) → 403 → died S.
56. `Concordia traverse raid Cap Prud'homme Dome C 1100 km tonnes fuel days Challenger tractors IPEV logistics` (extended) → Dargaud page and ESA blog fetched, the Dargaud page twice for verbatim context → OK.

**The oasis**
57. `Bunger Hills oasis area km2 ice-free lakes geography` (extended) → Wikipedia → OK.
58. Fetch Wikipedia "Bunger Hills" and "Algae Lake" → OK.
59. `Bunger Hills geomorphology deglaciation lakes epishelf Lake Figurnoye depth area Gore Colhoun` (extended) → paper titles only → partial.
60. Fetch Cambridge "Salt, sediments…" (article page and the aop PDF), "hidden oasis" (article and core-reader), Polar Record Algae River → all 403 → died S. ADS abstract → 405 → died S. Semantic Scholar API → 429 → died S.
61. Crossref API `works?query=Bunger+Hills&rows=40` → bibliography of 40 items → OK (used as an index).
62. `"Climatology and implications for perennial lake ice occurrence at Bunger Hills Oasis" abstract …` (extended) → LSU repository abstract read → OK.
63. `"Algae River" Bunger Hills drainage system 25 km Polar Record 2002 abstract` → abstract via summary → UNVERIFIED.
64. Russian: `оазис Бангера площадь км2 озера климат температура лето` (extended) → AARI paleopolar page and ru.wikipedia fetched → OK. booksite.ru (Great Soviet Encyclopedia) → 403 → died S.
65. Russian: `Бангера оазис Большая советская энциклопедия высота холмов м озёра площадь` → AARI RPR PDFs → both saved and extracted with pdftotext → OK (Andreev 2020; Lunev et al. 2017).
66. `Bunger Hills highest point elevation meters hills relief …` (extended) → AADC SPOT5 DEM metadata (5–410 m box) → OK, with the caveat that the box includes ice.
67. `"Bunger Hills" gazetteer data.aad.gov.au display_name narrative "moderately low"` → feature pages only → died Q for the oasis narrative.
68. `"Tafoni show postglacial and modern wind azimuths" …` → abstract numbers via summary; AADC/RDA record read → partial.
69. `Abakumov Bunger Hills soils permafrost active layer …` (extended) → EJSS page read; ResearchGate 403 → died S.
70. `"Permafrost table depth in soils of Eastern Antarctica oases" Bunger Hills cm abstract` → Czech Polar Reports abstract read → OK.
71. `"Spatial distribution of birds and terrestrial plants in Bunger Hills" abstract …` → abstract via summary; AADC record read → partial.
72. `Antarctica agriculture greenhouse feasibility ice-free oasis soil "Bunger Hills" OR "Antarctic oasis" crops construction` (extended) → only general station-greenhouse items → died S for Bunger-specific.
73. `Figurnoye Lake Bunger Hills area km2 depth …` → Polish Polar Research 1990 PDFs (journals.pan.pl). The `ochroma.man.poznan.pl` mirror had a TLS mismatch, so it was refetched via journals.pan.pl. Both PDFs extracted with pdftotext → OK (Filcek & Zieliński 1990; Klokov et al. 1990).
74. Polish Polar Research 1981 PDF (likely Wiśniewski) → over 10 MB → died S.
75. `Florinsky Zharnova "Geomorphometry of the Bunger Hills" …` → arcticportal record read; PDF 53 MB → died S. arXiv 2508.10462 is a different region (Sôya Coast) → dead end.
76. `"heavily crevassed glaciers" "Bunger Hills" "rarely attempted"` → attributed to the Gore & Berg core-reader page, which returned 403 → UNVERIFIED.
77. Fetch AAD DTC pages: "Happy campers" 2023, "Bunger Hills camp set up" 2024, "Nudging a sleeping giant," "Marine mystery" 2024, "This Week at Casey 22 Dec 2023," DTC wrap-up 2024 → all OK.
78. `Denman Terrestrial Campaign field camp on Denman Glacier crevasse ground penetrating radar …` (extended) → AAD and EGU blog via summary; ScienceDirect CRST 2020 → 403 → abstract via a second search → UNVERIFIED.
79. French Article VII inspection report of Casey (ATCM 46 att104) → PDF saved and extracted → OK (Wilkins, Bunger logistics).
