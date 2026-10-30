# Relung Panen oasis research, Unit E: the oasis airports (real world only), 2026-10-29

**Brief:** `Relung_Panen_Oasis_Airports_and_Haul_Research_BRIEF_2026-10-29.md`, Unit E. Real surfaces, real aircraft, real range, real season. **No design of any fictional airport, no recommendation.** Every claim is marked SOURCED, UNVERIFIED, DERIVED or NOT FOUND.

## PROGRESS
STARTED 2026-10-29
- [x] 1 Every candidate runway surface in or at the Bunger Hills oasis, with every measured dimension; past runways
- [x] 2 What each surface can carry (bearing capacity rules, heavy-aircraft precedents on ice, runway length on ice)
- [x] 3 Range and safe return (Hobart, Fremantle, Casey, Mirny to the oasis and back, with reserves)
- [x] 4 Season and weather at the oasis (melt, wind, crosswind, blowing snow, cloud, visibility, light)
- [x] 5 Freight-airport operations on ice (fuel, ground equipment, staffing, payload, turnaround, border presence)
- [x] 6 Two airfields at one Antarctic site
- [x] FINAL
COMPLETED 2026-10-29. No search was refused (no STOP note). No slang was met. Pages that failed are logged as DEAD-SOURCE and were not worked around.

## Common notes (read once)

- **Already known, not repeated** (see the brief's file list): the 2019 Russian survey's main findings (Transcription Gulf ice 2.95-3.20 m, "perfectly level," cryoconite cavities, the three zones, tidal cracks, rock "impossible"; Apfel Glacier blue ice, crevasses ≤25 cm, slopes ≤2.5%, centerline about 2.33 km at 90°); the 1961-62 and 1963-64 Il-18 landings as told in the operations file; the Australian 2000 alternate proposal; the 2010 CASA 212 hard landing; the Bunger-east blue-ice area (intake file B, item 7); the Oasis station 1956-58 climate table and the White Smoke Lake AWS (soil file E). This file adds what those files did not have, and cites them where it leans on them.
- **Data used for DERIVED values in this file (all downloaded 2026-10-29; scripts and files kept in the session scratchpad, not the repo):**
  - **Elevation:** REMA v2.0 mosaic, 32 m tiles `26_56` and `25_56` (Polar Geospatial Center, `data.pgc.umn.edu/elev/dem/setsm/REMA/mosaic/v2.0/32m/`), WGS84 ellipsoid heights converted to heights above the EGM2008 geoid with the PROJ grid `us_nga_egm08_25.tif` (geoid about −2.8 m here). REMA is built from 2009-2021 imagery; it does not see cracks, sastrugi or cryoconite pits, and it records a surface, not an ice type.
  - **Ice speed:** ITS_LIVE v2 annual-velocity mosaic, 120 m, Antarctic composite (`ITS_LIVE_velocity_120m_RGI19A_0000_v02_v.tif`, with `_v_error` and `_count`), read remotely with rasterio. **Noise floor check (DERIVED): the mosaic gives 5.3 m/yr at Edgeworth David Base, which stands on rock, and 5.9-6.1 m/yr on lake ice; values of about 5 m/yr or less here cannot be told apart from zero.**
  - **Distances:** WGS84 geodesics (pyproj `Geod`). Positions: Russian AWS "Oazis" 66°16.465′S 100°44.773′E (soil file E, SOURCED), Edgeworth David Base 66.25°S 100.6036°E (soil file E), Hobart airport, Perth airport, Casey, Wilkins and Mirny as in the operations file's search log entry 61.
- **Geography check (DERIVED):** in the oasis area, true north on the EPSG:3031 grid points toward +x; every bearing in this file is a true bearing.

## 1. Every candidate runway surface in or at the oasis, with every measured dimension; past runways

### 1a. Transcription Gulf (Transkriptsii Gulf), the epishelf lake

**What the 2019 survey adds beyond the already-known summary** (Polyakov, Mart'yanov and Sukhanova, *Rossiyskie polyarnye issledovaniya* No. 3 (37), 2019, pp. 11-15, PDF re-read in full from data.aari.ru for this file; translations mine). **SOURCED** unless marked.
- **The 2008 search result in full:** the single candidate area was "in the south-western part of Transcription Gulf, where there is the possibility of a field camp (two freshwater lakes, a flat area) and of laying out a snow-ice aerodrome with two runways in the directions west-east and north-south." The paper names the camp problem as "tidal cracks along the shores and hilly relief."
- **Why the gulf keeps its ice:** "the ice regime of the gulf is influenced by the considerable length of shore adjoining the glacier, because of which Transcription Gulf does not break up." It is "the only water body of the oasis on which the ice has not opened for many years." Under the fresh layer (to 70 m, <1‰) the salinity reaches **25‰** near the bottom (the soil file's Klokov figures, 11-19‰ at 93-104 m, differ; both are recorded).
- **The ice column:** upper 30 cm is "atmospheric ice of infiltration origin" (snow that melts in summer, refreezes and cements); below it the ice is "transparent, monolithic, with a small number of small bubble inclusions." **"Signs of spring decay in the ice cover are not observed."** Two 120 mm cores were "practically identical"; Kovacs auger checks agreed with GPR "to within 10 cm."
- **Cryoconite:** cavities to 6 m across and 30 cm deep, from rock dust "brought by wind from the surface of the oasis"; "the main outflow of cryoconite comes from a valley formed between two hills," carried by "the prevailing easterly winds in the oasis."
- **The three zones (Fig. 4 of the paper):** Zone 1, "smooth and even ice cover with a complete absence of cavities," used by the Australian expedition for its ski Twin Otter at Edgeworth David Camp, recommended for light aircraft, "its dimensions may be insufficient for medium-haul aircraft"; Zone 2, "a small number of cavities, but its size allows a runway for medium-haul aircraft to be chosen without difficulty, without prior preparation"; Zone 3, "a large number of cavities ... unsuitable without prior surface preparation." Hills to 100 m are air obstacles, "not critical."
- **No zone dimension is stated in the text.** The only dimensions are those drawn in Fig. 4.

**Zone dimensions measured from the paper's Fig. 4 (DERIVED, my measurement).** Method: the figure was extracted from the PDF (776 × 479 px); the printed scale bar (0-2,000 m, four 500 m blocks) spans 269 px, giving 7.43 m per pixel; each zone was isolated by its legend color, closed over its stipple, and measured as a connected region. **Uncertainty: the figure's own longitude labels (100°36′ and 100°39′, 346 px apart) imply 6.5 m per pixel against the 7.43 m/px of the scale bar, a 15% disagreement I could not resolve; treat every figure below as ±15% at best.** Zone 2 and Zone 3 run off the western edge of the figure, so their lengths are minimums.

| Zone | Area | Long axis | Across | Orientation of long axis | Note |
|---|---|---|---|---|---|
| 1 (no cavities; the Australian ski strip) | about 0.5 km² | about 1.5 km | about 0.35 km (median), 0.54 km (widest) | roughly ENE-WSW (about 33° off the figure's x axis) | lies off the Edgeworth David shore |
| 2 (few cavities) | about 1.3 km² (in frame) | **at least 3.3 km** (cut by the frame) | about 0.44 km (median), 0.82 km (widest) | roughly west-east | a band between Zone 3 and the south shore |
| 3 (many cavities) | about 2.3 km² (in frame) | at least 3.2 km (cut by the frame) | about 0.78 km (median), 1.09 km (widest) | roughly west-east | the northern band, downwind of the cryoconite valley |

**The whole gulf's level ice surface from REMA (DERIVED).** Method: on the 32 m REMA grid, surfaces below 4 m above the geoid were labeled as connected regions; the region that holds Edgeworth David's shore is centered at 66.247°S 100.560°E. For it, the longest straight line wholly inside the region was found at every 5° of true bearing (6,000 sample points).
- **Area 18.5 km²; surface 1.68 m above the geoid (median; interquartile 1.64-1.71 m; standard deviation 0.39 m).** The level is consistent with floating ice a meter or two above the sea surface, as an epishelf lake tied to the ocean would show; REMA does not say which part is lake ice and which is something else.
- **Longest straight lines inside it:** **7.7 km at 060°/240°** (66.2631°S 100.4789°E to 66.2290°S 100.6251°E), 7.7 km at 070°/250°, 7.6 km at 065°/245°, 7.4 km at 075°/255°, 6.3 km at 080°/260°, 5.8 km at 090°/270°; across the other bearings 2.8-5.3 km (north-south: 4.7 km).
- **These lines cross all three zones.** No source gives the cryoconite-free length along any of them. *The usable length on cavity-free ice, as distinct from the length of level ice, is NOT FOUND.*
- **A second gulf-level surface:** a flat region of 13.9 km² at the same height (1.67 m) is the gulf with its rougher edges removed (DERIVED from a 96 m local-relief test, under 0.5 m of relief).
- *A check on the name:* the companion paper (Sukhanova et al. 2019, *Problemy Arktiki i Antarktiki* 65(3)) placed its runway site "in the central part of the epishelf Transcription Gulf ... 7 km from the base" (UNVERIFIED, abstract-level, as in intake file B). My DERIVED distance from the middle of the gulf's longest chord to the Russian Oazis AWS is 9.3 km.

**Ice speed on the gulf (DERIVED):** ITS_LIVE 6.1 m/yr at 66.23°S 100.58°E and 5.3 m/yr at Edgeworth David Base (rock) — both at the noise floor. At 66.225°S 100.55°E it gives 51 m/yr, probably the Edisto Glacier side of the gulf; where the floating gulf ice meets moving glacier ice was not mapped.

**Does the ice persist year to year?**
- "Transkriptsii is perennially ice-covered, about 4 m thick" (Filcek & Zieliński 1990, already known, soil file E). "Does not break up" (Polyakov 2019, SOURCED). The 1963 Il-18 strip and the 1960s Il-14 landing, the Australian ski use since the 1980s and the 2019 survey all used this ice (below). **SOURCED pieces.**
- Why: "The Bunger Hills Oasis seems to be in a marginal climatic region for the persistence of thick lake ice"; "contact with glacier ice" controls whether a lake stays ice-covered year-round, through the glacier acting as a heat sink, its high albedo, or both (Doran, Wharton, Lyons, Des Marais and Andersen, "Climatology and implications for perennial lake ice occurrence at Bunger Hills Oasis, East Antarctica," *Antarctic Science* 8(3), 1996, abstract on repository.lsu.edu; full text not reached). **SOURCED (abstract).**
- **A recorded summer surface on the gulf:** the 2019 survey (late January to mid-February) found the surface "ideally level" with cryoconite pits; the infiltration layer forms from snow that "begins to melt in the summer season." Whether open water or slush ever forms on the gulf surface in a warm summer: **NOT FOUND.**
- A year-by-year satellite record of the gulf's ice: **NOT FOUND** (not searched in imagery; no paper found).

### 1b. The Apfel Glacier blue-ice strip

**Already known:** blue ice from the surface, crevasses ≤25 cm wide (most water-filled, thin or no snow bridges), no voids in 9,000 m of GPR at 270 and 900 MHz, slopes "do not exceed 2.5%" (Garmin GPSmap64st), centerline 66°20′36.0″S 100°48′47.0″E to 66°20′37.0″S 100°51′55.0″E at 90°, ski aircraft only (An-2 without preparation; BT-67 after filling cracks with packed snow), a 9-stake network (no results published). **One addition from the paper (SOURCED):** two kinds of surface irregularity were mapped, "cracks and water-logged areas" (обводненные участки); Fig. 6 shows a "water-logged area" on the strip in late January-February 2019.

**Measured along the surveyed centerline (DERIVED, REMA 32 m and ITS_LIVE, 74 points at 32 m):**
- **Length 2,339 m (WGS84 geodesic), forward azimuth 090.8° true.**
- Height above the geoid **140 m at the west end, 160 m at the east end**; overall grade 0.85% rising eastward; steepest 288 m segment **2.1%**, steepest ~96 m segment 2.3%, median 0.7%. This agrees with the survey's "≤2.5%."
- **Ice speed 3.4-13.2 m/yr along the line (error 2-3 m/yr)**, slower toward the east end; much of it is at or near the 5 m/yr noise floor.
- **Beyond the surveyed ends, on the same line (DERIVED):** westward the surface drops from 140 m to about 109 m within 1.5 km (250 m segments of 2.5-2.8%) and the ice speeds up to 29-47 m/yr; eastward it rises from 160 m to 174 m between 2.5 and 3.0 km (about 3.8% per 250 m) and to 191 m by 3.5 km (4.6%). **On this alignment the level, slow part is about the surveyed 2.3-2.5 km;** other alignments on the glacier were not tested.
- **Distance (DERIVED):** middle of the strip to the Russian Oazis AWS 8.8 km; to Edgeworth David Base 14.9 km.
- **Melt on it:** the survey's "water-logged areas" and water-filled cracks (SOURCED). A measured ablation rate for the strip: NOT FOUND (the stake results were not published in any source found).

### 1c. Other lakes and flat ice in or beside the oasis (DERIVED from REMA unless marked)

A 96 m local-relief test (under 0.5 m of relief in a 3 × 3 window) on the 32 m grid found these large flat surfaces in a box of about 66.14-66.40°S, 100.40-100.97°E:

| Surface | Area (flat part) | Height above geoid | Longest straight line inside | What it is (status) |
|---|---|---|---|---|
| **Northern marine bays** (centroid 66.198°S 100.844°E) | 88.8 km² | 1.34 m (IQR 1.30-1.42) | **14.3 km at 035°/215°**; 13.4 km at 040°; 13.2 km at 070°; 13.1 km at 145° | The oasis's "marine bays" (470 km² in the 1950s survey, soil file E). **Ice type, thickness and whether it breaks out each summer: NOT FOUND** (one search, died at the sources). The soil file records that Rybiy Khvost Bay "thaws in summer"; whether these northern bays do is not known. |
| **Transcription Gulf** | 13.9-18.5 km² | 1.67-1.68 m | 7.7 km at 060° | 1a above |
| **Lake Figurnoye (Algae Lake)**, its flattest stretch (centroid about 66.30°S 100.78°E) | 5.5 km² of a lake of 14.3 km² (SOURCED area, soil file E) | 13.3 m (AARI gives 11.6 m; the 1.7 m difference is not explained) | **about 4.3-4.4 km at 085°-105°** | Fresh lake; "in summer the lake is mostly ice-free" (AARI, already known); large lakes freeze from late February/early March "within about 10 days" (Filcek & Zieliński 1990, already known). **Winter ice thickness on Figurnoye: NOT FOUND.** A Soviet An-2 landed on it on 6 August 1956 (port file B). |
| Edisto Glacier tongue west and north of the gulf (centroid 66.209°S 100.482°E) | 86.5 km² flat at 96 m scale | 12-33 m (median 22 m) | not run | Glacier ice; its speed and crevassing were not examined here |
| A flat ice surface at 64-80 m, 66.36°S 100.49°E | 16.6 km² | median 68 m | not run | Probably on Edisto or Apfel Glacier ice south-west of the oasis; not identified in any source |
| White Smoke Lake (beside Apfel Glacier) | not isolated by the test | — | — | Epishelf lake with perennial ice **1.8-2.8 m**, "fresh and cold" (already known, soil file E) |
| Other flat lakes at 13.2-13.6 m (66.28-66.30°S 100.93-100.95°E; 66.300°S 100.726°E) | 0.7-1.1 km² each | 13.3-13.6 m | — | Probably the eastern arms of Figurnoye and its chain |

### 1d. The blue-ice area adjacent to the oasis (intake file B's figures, not re-derived)
A blue-ice area of 3,304 km² (about 123 × 64 km, centroid 66.229°S 101.215°E, 0-906 m) lies east and south of the oasis (Tollenaar et al. 2024 map). On it, 273 flat 3 km lines have a maximum speed ≤15 m/yr; the slowest grounded lines are at 66.278°S 101.160°E (400-406 m, steepest segment 1.12%, max 3.9 m/yr) and 66.265-66.312°S 101.08-101.22°E (240-480 m). ERA5 there: mean 9.2 m/s, 16.7% of hours ≥15 m/s, strong winds from the east, about 27 hours a year above 0 °C. **(All intake file B, DERIVED there.)** *New here (DERIVED):* the slowest line's position is 18.6 km from the Russian Oazis AWS and 16.1 km from the middle of the Apfel strip. Crevassing and measured melt on this blue ice: NOT FOUND (as in intake file B).

### 1e. Past runways and landings at the oasis

| Date | What | Surface | Status |
|---|---|---|---|
| 1956 (6 Aug) | An-2 landed on Lake Figurnoye; returned without siting the station | lake ice | already known (port file B) |
| 1956-66 | "Li-2 aircraft in the Bunger Oasis could land only on ice-covered lakes" (caption, Polish expedition page) | lake ice | **SOURCED**, dobrowolski.igf.edu.pl/wyprawy/1965-1966/ (Polish) |
| 1959 | Li-2 to "Scott Glacier," then Mi-4 for the last 20 km | glacier | already known |
| **Dec 1961-Jan 1962** | Il-18V (wheels) and An-12 (converted to skis at Mirny): "Full fueling of the aircraft for the return to Christchurch was done at the runway in the Bunger oasis"; both left on 24 January 1962 | not stated by Lukin | **SOURCED**, Lukin 2022 (re-read in full). A second account: "For their return, the runway of Mirny was in poor condition because the ice was beginning to thaw," so "both aircraft flew first with little fuel to Bunger Hills where they were fully fueled," leaving 24 January 1962; it also says both "arrived at Bunger Hills" on Christmas Day, 1961 (**SOURCED**, aeroflotarchives.com "Polar aviation"; conflicts with Lukin's first landing at Mirny on 26 December; not resolved). |
| **3 Dec 1963** | **Two Il-18Vs, CCCP-75743 and CCCP-75845,** carrying an 80-person air expedition, "landed on a runway prepared in advance by members of the 8th SAE **in one of the lagoons of Transcription Gulf** of the Bunger oasis, and then flew on to Mirny"; on 3 January 1964 both left "without a landing in the Bunger oasis" | gulf ice, prepared | **SOURCED**, Lukin 2022, p. 15 (translation mine). **This resolves the open question in intake file B (9.3) and the operations file: the 1963 "lagoon runway" was in Transcription Gulf.** Which lagoon, and the strip's length: NOT FOUND. |
| 1960s | Il-14 landed on Transcription Gulf | gulf ice | already known (Polyakov 2019) |
| **summer 1966** | A Soviet Li-2 carrying a Polish party "was to land on one of the frozen lakes. Unfortunately during landing the skis sank under the ice"; "nobody was hurt"; "the aircraft sank after some time"; "after a few days another aircraft took everyone to Mirny station" | lake ice (lake not named) | **SOURCED**, dobrowolski.igf.edu.pl/wyprawy/1965-1966/ (Polish; translation mine). *Port file B dates it January 1966; this page says summer 1966; both fit the 1965-66 season.* |
| 1979 | Polish Il-14 landing on the "Shackleton Glacier" (ice shelf), coordinates not found | shelf | already known |
| from the Edgeworth David years (base built 1986, port file B) | Australian Twin Otter ski landings in Zone 1, off Edgeworth David; the start year of this use is not stated | gulf ice | SOURCED (Polyakov 2019) |
| 1999-2000 | AAD Twin Otter assessed landing sites; *Aurora Australis* itinerary (14 Mar 2000) included a "helicopter inspection of Apfel Glacier AWS and runway site" | — | already known (port file B) |
| 2000/01 | C-130 trial of a Bunger blue-ice runway "expected" | blue ice | **whether flown: NOT FOUND** (two more searches this session, died at the sources; search log) |
| 15 Nov 2010 | CASA 212-400 VH-VHB hard landing (sastrugi); "subsequently deemed unserviceable"; "The effort to recover this aircraft was enormous and saw additional engineers flown in from Australia"; it "was eventually retrieved to Casey skiway"; a Twin Otter was chartered from Canada to make up the shortfall | gulf ice (Polyakov 2019 says "on Transcription Gulf") | **SOURCED**, *Australian Antarctic Magazine* 20 (2011), "A challenging Antarctic season"; the Aviation Safety Network record failed with a certificate error (not worked around) |
| 2019 | Russian survey (above) | gulf and Apfel | SOURCED |
| current | AAD lists Bunger Hills as a landing site, "unprepared ice," a fuel depot of up to 40 drums | gulf ice | already known (port file B) |

**What the record says about Soviet heavy-aircraft use (SOURCED, Lukin 2022):** after the 1961-64 flights "it became obvious that ensuring safe landings and take-offs of heavy wheeled aircraft on runways prepared at coastal Antarctic stations is very difficult. Serious preparatory work is needed to build runways of compacted snow." The Soviet program moved its heavy-aircraft gateway elsewhere (already known).

**Il-18 weights (for scale):** the Il-18**D**: maximum take-off 64,000 kg, empty 35,000 kg, maximum landing 52,600 kg, take-off run 1,350 m (**SOURCED at Wikipedia**, specifications for the Il-18D). **The Il-18V's figures: NOT FOUND** (cyclowiki 403; airvectors 404). The Il-18D is a later, heavier variant, so these are an upper bound for the 1963 aircraft (DERIVED reading).

### 1f. What item 1 adds up to (facts only)
- **Surfaces measured:** Transcription Gulf (level floating ice about 1.7 m above the geoid, 18.5 km², straight lines up to 7.7 km on ENE-WSW bearings, but three cryoconite zones of which the clean ones measure roughly 1.5 × 0.35-0.5 km and ≥3.3 × 0.4-0.8 km on the 2019 figure); the Apfel strip (2.34 km at 091°, 140-160 m, ≤2.1% per 288 m, 3-13 m/yr, steeper and faster beyond both ends on that line); the northern marine bays (89 km² flat, 14 km lines, ice type unknown); Lake Figurnoye (about 4.4 km lines on its flattest stretch, ice-free in summer); the blue ice east and south (intake file B). (DERIVED from sourced and downloaded data.)
- **Past use:** wheeled Il-18Vs landed on a prepared strip in a Transcription Gulf lagoon in December 1963; a Bunger runway refueled the Il-18 and An-12 in January 1962; ski aircraft have used the gulf since the 1960s; one Li-2 broke through lake ice and sank (1966); one CASA 212 was damaged on sastrugi (2010). (SOURCED.)
- **Not found:** zone dimensions stated in text; the cavity-free length on the gulf; the gulf's summer surface condition year by year; ice type and persistence in the northern bays; winter ice thickness on Figurnoye; Apfel ablation; the 2000/01 C-130 trial; the Il-18V's weights; the 1963 strip's exact place and length.

## 2. What each surface can carry

### 2a. Floating ice (lake, epishelf and sea ice): the engineering rules in use

- **Gold's formula.** "P = Ah²," where P is the allowable load, h the ice thickness and A "an empirical parameter with pressure units"; Gold built it from "breakthroughs that had occurred, including data on ice thickness and weight, of the vehicles and horses that caused the ice to fail"; it is "a curve-fitting exercise," to be used "in combination with experience and good judgment." Gold's 1971 chart shows three lines, labeled A = 3.5, 18 and "70" kg/cm² (the last as printed; it may be 7.0 with the decimal lost in the extraction, not resolved). One guideline (CRREL 2006) prescribes A = 10 kg/cm², "a relatively high value ... it is not known why"; guidelines disagree mainly on how much weaker white (snow or flooded) ice is than clear ice, some taking it as 50% weaker. **SOURCED** — P.D. Barrette (National Research Council Canada), "A review of guidelines on ice roads in Canada: determination of bearing capacity," Transportation Association of Canada conference, 2015 (PDF read).
- **Time on the ice.** "Gold's formula is not meant to be used for loads that remain at one location for a certain time period – the limit is often quoted as being two hours ... with time, the stresses induce non-elastic deformation in the form of micro-cracks ... and, ultimately, breakthrough, even with good quality ice cover and a load that is less than that indicated by Gold's formula." When a load must stay, guidelines monitor the freeboard by drilling and remove the load when water reaches the surface. **SOURCED**, Barrette 2015.
- **A working government rule set (Northwest Territories, Canada):** P (kg) = A h² (cm), with **A = 4 for "Routine"** operations and construction, **A = 6 for "Enhanced"** operations (more frequent ice measurement and controls), and above that "detailed stress analysis conducted by a Professional Engineer ... not using Gold's equation approach"; "temporary loads" are in one place "no more than two hours"; "stationary or long term loads" (over six hours) need "a greater ice thickness," and their bearing capacity "is beyond the scope of this document"; "wet cracks" (through the whole thickness) "reduce the capability of the ice sheet," and good practice is to "divert traffic or temporarily suspend the loading" until they are flooded and refrozen. **SOURCED** — Government of the Northwest Territories, Department of Transportation, *Guidelines for Safe Ice Construction* (February 2015), pp. 2, 23-26, appendices A-C (PDF read, from reviewboard.ca).
- **The US military rule for ski Hercules on floating ice:** "55 inches of ice is the thickness required" (about 1.40 m), from CRREL's "decades of research and fieldwork," applied to both sea and fresh ice and "in place for several decades for LC-130s." In spring 2025 an LC-130 ("61-ton") landed on **Parsons Lake** (NWT, about 68°N) on ice averaging **39.5 in (about 1.0 m)**, after a CRREL engineer weighed "the size of the plane, its load, unfrozen water depth, how long the plane is going to sit on the ice ... at what speed it will land, taxi, and takeoff," and whether it is an emergency or "a regular operation." On fresh ice: "Does the ice have cracks? What direction do they run in?" — depth, width, and whether cracks are wet or dry matter; sea-ice strength "really is just dependent on ice thickness." **SOURCED** — DVIDS, "ERDC and the 109th Airlift Wing team up for aviation first," 24 June 2025 (read); UAF Geophysical Institute news, 4 June 2026 (the 55 in figure). *The 109th Airlift Wing's own page returned 403.*
- **A modeled heavy jet on floating ice:** a Russian theoretical study of an **Il-76TD (weight 1.48 MN, about 151 t)** taking off and landing on a floating elastic ice plate found the stresses highest at takeoff and concluded take-off and landing "will be safe at ice thickness more than 1 m," **if** the critical stress for first cracking is taken as 2.35 MPa. **SOURCED** — A.V. Pogorelova, V.M. Kozin, A.A. Matyushina, *Prikladnaya mekhanika i tekhnicheskaya fizika* 56(5), 2015, pp. 214-221, doi 10.15372/PMTF20150520 (PDF read). *It is a model with an assumed failure stress, not a field rule.*

### 2b. What the rules give for the measured oasis ice (DERIVED, my arithmetic; not an engineering assessment)

Gold's formula with the Northwest Territories A values (P in kg, h in cm), for the thicknesses measured in the sources:

| Ice | h (cm) | A = 4 ("Routine") | A = 6 ("Enhanced") | Source of h |
|---|---|---|---|---|
| Transcription Gulf, thinnest GPR value 2019 | 295 | **348 t** | 522 t | Polyakov 2019 |
| Transcription Gulf, thickest GPR value 2019 | 320 | 410 t | 614 t | same |
| Same, with the 30 cm infiltration ice counted at half strength (one guideline practice) | 280 | 314 t | 470 t | DERIVED from the above |
| Transcription Gulf, summer mean "close to 3 m"; maximum 5 m | 300; 500 | 360 t; 1,000 t | 540 t; 1,500 t | Polyakov 2019 |
| White Smoke Lake (perennial) | 180-280 | 130-314 t | 194-470 t | soil file E |

*For scale only (SOURCED weights, set beside the DERIVED loads, not a finding that any of them may land):* C-130J maximum take-off 74.4 t (Wikipedia, "C-130J Super Hercules"); Il-18D 64 t; Il-76TD-90VD 195 t (Volga-Dnepr technical specification page); A330-200/-300 up to 242 t (Wikipedia, "Airbus A330"); C-17A 265 t (Wikipedia, "Boeing C-17 Globemaster III"); 767-300ER 187 t (Wikipedia, "Boeing 767").

**Limits on reading this table (each SOURCED in 2a):** Gold's formula is for loads in place under about two hours; a parked, loading or refueling aircraft is a stationary load that the guidelines put outside the formula; wet cracks (the gulf has "tidal cracks along the shores," Polyakov 2019) reduce capacity and stop traffic until refrozen; cryoconite cavities to 30 cm deep (Polyakov 2019) reduce the effective thickness locally by an amount no source states. **Whether the gulf's ice is fresh throughout:** the upper water layer is fresh (<1‰) to 70 m (SOURCED); the ice is "transparent, monolithic" below 30 cm (SOURCED); so the fresh-ice rules, not sea-ice rules, are the ones that match (DERIVED reading).

**What the survey itself concluded:** "the bearing capacity of the ice cover of the surveyed area fully allows heavy aircraft on wheeled undercarriage to work on it." **SOURCED** (Polyakov 2019). No aircraft type or weight is attached to that sentence.

### 2c. Glacier and blue ice

- "Unlike the cold, dry snow that covers most of Antarctica, blue ice has sufficient bearing capacity to support heavy wheel loads without rutting, even at the highest imaginable inflation pressures for aircraft tires. There is virtually no limit to the total load that can be supported." Blue ice "is solid glacier ice, typically hundreds of meters thick and resting on solid rock (on an ice shelf it may be afloat). By contrast, typical sea ice is a thin (< 3 m)" plate. "The typical cuspate surface of cold, windblown ice provides excellent friction for tires, to the extent that rubber can be burned off the tire if the wheel locks at high speed. By contrast, snow-free sea ice has a slick surface when temperatures approach the melting point." **SOURCED** — Mellor and Swithinbank, *Airfields on Antarctic Glacier Ice*, CRREL Report 89-21 (1989), pp. 3-4 (scan read, southpolestation.com).
- On buildings at blue-ice fields: "There is no lack of bearing strength, but structures need to be separated from the ice to prevent heat transfer"; set directly on ice they cause "differential ablation, either causing melting in summer or becoming elevated on glacier tables." **SOURCED**, same, p. 65.
- **What limits a blue-ice strip is its surface, not its strength:** roughness, crevasses and melt (Mellor and Swithinbank, pp. 60-62 on roughness and planing); at the Apfel site, cracks to 25 cm that must be filled for a BT-67 (Polyakov 2019); Wilkins' and Novo's melt closures (already known). Novo's ice is harder than 1.2 MPa "even at temperatures close to the phase-transition temperature" (already known). **SOURCED pieces.**
- **The Apfel strip as measured (item 1b) is grounded glacier ice moving 3-13 m/yr;** its thickness was not measured (the 2019 drilling was for stakes only). **NOT FOUND.**

### 2d. Heavy-aircraft precedents on lake, sea and glacier ice

| Aircraft | Where | Surface | Detail | Status |
|---|---|---|---|---|
| **Il-18V (two, wheels)** | **Transcription Gulf lagoon, 3 Dec 1963** | prepared gulf ice | carrying an 80-person expedition (item 1e) | SOURCED, Lukin 2022 |
| Il-18V and An-12 | "runway in the Bunger oasis," Jan 1962 | not stated | full fuel for Christchurch | SOURCED, Lukin 2022 |
| **C-5B Galaxy** | McMurdo, 4 Oct 1989 | sea-ice runway (DVIDS timeline: "Ross Sea ice runway") | "72 people and about 168,000 pounds [76 t] of freight, including two fully assembled helicopters," wheels | SOURCED, Air & Space Forces Magazine "This day in airpower"; DVIDS timeline via search text |
| C-5, C-141, C-17, C-130, P-3; Boeing 757 trial 2009/10 | McMurdo annual sea-ice runway, Oct-early Dec | sea ice | "The ice for the runway would be over 2 meters ... thick to land an aircraft like the C-17" | SOURCED at Wikipedia ("Ice Runway," citing a NASA Earth Observatory blog 2011, and an NSF 1993 page for the season); a blog gives "70 inches" minimum for a C-17 (UNVERIFIED) |
| A319 | Mario Zucchelli, 2018 | groomed sea ice about 2 m | already known | — |
| **CC-130J Hercules (wheels)** | Squaw Lake, near Schefferville, Quebec, 28 Feb 2013 | lake ice, flooded and built up | landed at "112,000 pounds [50.8 metric tons]"; strip "approximately 1,524 meters long, 49 meters wide and 106 centimeters thick"; the crew said "6,000-plus feet [1,829 meters] of runway ... had been prepared" (the two lengths conflict); about 40 engineers, "two weeks to clear the site" and "over three weeks to water the runway with pumps," temperatures to −40 °C; certified with GPR checks for "air or water pockets"; "the stable surface of an ice runway is similar to concrete" | SOURCED — CMEA/RCAF, "Ice landing: Still capable after 30 years" (2013 article, PDF read) |
| Hercules | CESAR, Arctic Ocean pack, March 1983 | sea ice, "leveled ... with explosives and flooded" | 1.6 km "ice-paved runway," 17 days to build | SOURCED, same article |
| LC-130 (skis) | Parsons Lake, NWT, 2025 | lake ice 39.5 in | below the 55 in rule, after engineering review | SOURCED (2a) |
| Il-76TD-90VD, 757, 787-9, A340, C-17, A319 | Novo, Union Glacier, Troll, Wolf's Fang, Wilkins | blue ice | already known (operations file 5d) | — |
| Li-2 (skis) | an oasis lake, 1966 | lake ice | broke through and sank (item 1e) | SOURCED |

### 2e. Runway length and braking on ice

- **Braking on blue ice as one operator reports it:** "The landing and stopping are not a problem – braking action is only slightly worse than landing on a wet runway – our biggest challenge is lateral control and handling the aircraft on the ground, especially in strong winds, when there is risk of the whole aircraft trying to 'weathercock'"; "The team on the ground measures the friction coefficient every 500 meters along the runway before we land and reports to us by radio – if it is okay we land, and if not we turn around"; the pilots look for "a runway friction coefficient of around 0.20 or better." Skytraders restricts the A319's center of gravity on ice "to keep a better distribution of weight on all three landing gear to optimize the bearing strength of the ice and also assist us to make a 180 degree turn on the blue-ice runway in winds of up to about 50 knots." **SOURCED** — Garry Studd (Skytraders), Airbus *FAST* 42 (July 2008), pp. 28-29 (PDF read from skytraders.com.au).
- **How regulators factor landing distance on contaminated runways (the planning rule, written for paved runways):** the US Runway Condition Assessment Matrix puts "Ice" at **runway condition code 1, braking "Poor"**; "Wet Ice," "Slush on top of Ice," "Water on top of Compacted Snow" and "Dry Snow or Wet Snow on top of Ice" at **code 0, "Less than Poor / Nil"**; compacted snow at −15 °C and colder at code 4. **SOURCED** — Transport Canada, Civil Aviation Safety Alert 2018-08 (RCAM table, read). FAA landing distance factors, multipliers on the unfactored AFM dry landing distance (with a 15% safety margin): **turbojet with reverse thrust: 1.67 (dry), 2.2 (code 5), 2.3 (4), 2.5 (3), 2.9 (2), 3.4 (code 1, "Poor")**; turbojet without reverse: 1.67 to 5.1; turboprop: 1.67 to 2.9. **SOURCED** — FAA Order 8900.1 Vol. 4 Ch. 3 Sec. 1, Table 4-11 (CHG 470, 13 Nov 2017; PDF read).
  - *Reading (DERIVED):* on these factors a jet needs about **2.0 times** (3.4 / 1.67) the runway on paved ice that it needs dry. The *FAST* 42 operator account puts Wilkins' cold, tilled blue ice closer to "wet" (code 5, factor 2.2) than to "ice." No source ties the RCAM codes to Antarctic blue ice.
- **Runway lengths in real heavy and jet use on ice (SOURCED, already known unless marked):** Wilkins 3,200 × 30 m (A319, C-17); Union Glacier 3,000 × 50 m (757, Il-76); Troll 3,000 m (787, 767, A340); Novo 3,000 × 60 m (Il-76); Phoenix 3,353 m compacted snow (C-17); McMurdo sea-ice runways 10,000 ft (3,048 m) (Wikipedia, "Ice Runway," DAFIF data); Mario Zucchelli 10,000 × 250 ft; Squaw Lake 1,524-1,829 m (C-130J at 50.8 t); Mirny 1.3-1.5 km (BT-67, skis); the Apfel survey line 2.34 km (ski aircraft only, per its authors).
- *First A319 trial landing at Wilkins (2007):* "the plane pulled up within 1,000 meters despite the lack of friction" (AFP text quoted on a forum; **UNVERIFIED**).
- **Published take-off and landing figures for a Hercules (paved, sea level, ISA):** C-130J take-off 1,780 m over a 15 m obstacle at 74.4 t (ground roll 940 m maximum effort); landing 910 m over 15 m at 61 t (ground roll 500 m maximum effort). **SOURCED at Wikipedia.** Il-76TD in the Russian ice model: take-off run 1,680 m, landing run 880 m at 151 t (inputs to Pogorelova et al. 2015, SOURCED as inputs).
- **Fuel cost at an ice field:** transporting fuel to Wilkins "would make it very costly – perhaps as much as $25 a gallon" (Studd 2008, SOURCED).

### 2f. What item 2 adds up to (facts only)
- The engineering rules found for floating ice (Gold's formula, the NWT A = 4/6, CRREL's 55 in for an LC-130, a 1 m modeled minimum for an Il-76TD) all put the measured 2.95-3.2 m of Transcription Gulf ice well above the moving-load thresholds of every heavy aircraft listed; the same rules exclude stationary loads, wet cracks and degraded ice from that arithmetic, and the gulf has tidal cracks and cryoconite cavities. (SOURCED rules; DERIVED application.)
- Blue ice has "virtually no limit" in bearing; its limits are surface, crevasses and melt. (SOURCED.)
- Jets on ice have used 3.0-3.35 km of runway in every Antarctic case found; regulators' factors for "ice" double a jet's dry landing distance; the one operator account puts cold blue ice near "wet." (SOURCED; DERIVED ratio.)
- **NOT FOUND:** Assur's 1956 SIPRE tables of required ice thickness per aircraft (ERDC library behind a browser check; DTIC 403); the McMurdo sea-ice runway design criteria (DTIC 403, already known); any wheeled jet landing on lake ice; any Il-76 landing on floating ice; the bearing capacity at the gulf's tidal cracks.

## 3. Range and safe return

### 3a. Distances (DERIVED, WGS84 geodesics from the Russian Oazis AWS position; air routes are longer)

| From the oasis to | km | nm | Note |
|---|---|---|---|
| Hobart airport | 3,840 | 2,073 | the brief's 3,818 km is within 0.6% |
| Perth airport | 3,952 | 2,134 | Fremantle (city) 3,936 km; Fremantle has no airport (operations file) |
| Learmonth (Exmouth, WA) | 4,986 | 2,692 | for scale |
| Darwin | 6,392 | 3,452 | |
| Denpasar (Bali) | 6,481 | 3,499 | |
| Jakarta (Soekarno-Hatta) | 6,692 | 3,613 | |
| Singapore (Changi) | 7,509 | 4,054 | |
| Kuala Lumpur | 7,657 | 4,135 | |
| Wilkins | 482 | 260 | |
| Casey | 439 | 237 | |
| Mirny | 347 | 187 | |

*The Southeast Asia rows are added because the brief's background (DR-81) names Southeast Asia; item 3 itself asks only for Hobart, Fremantle, Casey and Mirny.*

### 3b. The fuel rule (already known; restated as the input to 3c)
Australian Part 121 (larger airplanes): a destination is **isolated** when no qualifying alternate is within the fuel equal to 2 hours' cruise above it; then the flight carries **fuel to fly 2 hours at normal cruise above the destination, including final reserve**, and must not continue past a computed **critical point** unless the forecast supports a landing (operations file 2a, SOURCED). The real Antarctic operators carry **round-trip fuel** instead of relying on fuel at the destination: Skytraders "wanted an aircraft without a point-of-no-return" and carries four extra center tanks so "if the weather is not good enough for a landing, we can always turn around and fly back to Australia" (*FAST* 42, SOURCED). The USAP manual: "Currently there are no adverse weather landing sites available for wheeled aircraft in Antarctica" (already known).

### 3c. What each real aircraft type offers (published range at a stated payload) against the oasis (DERIVED arithmetic)

**Method and assumptions (DERIVED, mine):** "two-hour fuel" is converted to distance at an assumed cruise of 850 km/h for jets (1,700 km), 750 km/h for the Il-76TD-90VD (its published cruise; 1,500 km) and 640 km/h for the C-130J (1,280 km). **Case A, no fuel taken at the oasis:** still-air need = 2 × distance + two-hour fuel. **Case B, refueling at the oasis:** need = 1 × distance + two-hour fuel (the outbound flight must still be able to reach the oasis and hold or turn back from its critical point; Case B ignores the return-from-critical-point fuel, so it understates the real need). Published ranges already assume the maker's standard reserves (not stated on the pages read), headwinds are ignored, and no contingency fuel is added. **This is arithmetic on published figures, not a flight plan.**

Needs: **Hobart** Case A 9,380 km, Case B 5,540 km; **Perth** Case A 9,604 km, Case B 5,652 km (jet figures; Il-76: A 9,180 / 9,404, B 5,340 / 5,452; C-130J: A 8,960 / 9,184, B 5,120 / 5,232).

| Type (freight) | Published range at payload | Case A Hobart / Perth | Case B Hobart / Perth | Source of the published figure |
|---|---|---|---|---|
| Boeing 777F | 9,200 km at 103.7 t (maximum structural payload) | short by 180 / 404 km at full payload | met | SOURCED at Wikipedia ("Boeing 777") |
| Airbus A330-200F | 7,400 km at 65 t; 5,900 km at 70 t | not met at these payloads | met at 65 t and at 70 t | SOURCED at Wikipedia ("Airbus A330") |
| Boeing 767-300F | 6,025 km at 52.7 t | not met | met (485 / 373 km spare) | SOURCED at Wikipedia ("Boeing 767") |
| Il-76TD-90VD | 4,000 km at maximum load (50 t); table "RANGE 4 500 km" (payload not stated) | not met | not met at 50 t | SOURCED, Volga-Dnepr technical specification page |
| Boeing C-17A | about 2,400 nm (4,445 km) with 160,000 lb (72.6 t); 6,230 nm (11,540 km) unloaded | not met at 72.6 t | not met at 72.6 t | SOURCED at Wikipedia ("C-17") |
| C-130J | 3,300 km with 15.4 t | not met | not met (one-way 3,840 km exceeds it) | SOURCED at Wikipedia ("C-130J") |
| Boeing 737-800BCF | 1,995 nm (3,695 km) at 23.95 t | not met | not met | **UNVERIFIED** (search-result text of a Boeing brochure; the brochure URL now redirects) |

| Type (passenger) | Published range | Case A Hobart / Perth | Case B | Source |
|---|---|---|---|---|
| A319-115LR (the AAD aircraft, about 38 passengers) | "over 5,000 nautical miles" (over 9,260 km) | about equal to the need (9,380 / 9,604) | met | operations file, SOURCED (AAD) |
| A319neo / A320neo / 737-8 | 6,850 / 6,300 / 6,480 km | not met | met (A319neo, 737-8); A320neo met for Hobart and Perth | operations file |
| A321XLR | 8,700 km | not met | met | operations file |
| A330-900 / 787-8 / 787-9 | 13,600 / 14,820 / 15,370 km | met | met | operations file |

**Reading (DERIVED):** on published figures, the only freighters whose stated payload-range covers a no-refuel round trip from Hobart or Perth plus two hours are none at their headline payloads (the 777F comes within 2-4%); with fuel available at the oasis, the 777F, A330-200F and 767-300F cover the one-way leg plus two hours at their stated payloads, and the Il-76TD-90VD, C-17A at 72.6 t, C-130J and 737-800BCF do not. Lighter payloads raise every range; **payload-range charts were not opened, so the payload each type could carry on Case A is NOT FOUND.**

**Real precedents for the round trip (SOURCED, already known unless marked):** the RAAF C-17 flies Hobart-Wilkins (3,422 km) and "air-to-air refueling is typically not required"; the A319LR flies Hobart-Wilkins-Hobart; a 787 flew Cape Town-Troll (about 4,330 km) and back "without the need for refueling," carrying 45 passengers and 12 t in 2023; the A319 flew Hobart-Mario Zucchelli (about 3,650 km) and back in about 11 hours.

**The 1960s precedent at this oasis (SOURCED, Lukin 2022):** the Il-18V and An-12 took **full fuel** at the Bunger Hills runway for the leg to Christchurch in January 1962 — i.e., fuel was available at the oasis and the return leg began there.

### 3d. Short legs: Casey, Wilkins and Mirny to the oasis
- **Distances:** Mirny 347 km; Casey 439 km; Wilkins 482 km (DERIVED).
- **Published ranges:** Basler BT-67 950 nm (1,759 km) standard, 2,140 nm with long-range fuel, 195 kt on skis; Twin Otter 775 nm (1,435 km), 160 kt on skis (already known, intake file A).
- **Arithmetic (DERIVED, applying the two-hour rule text only for scale; Part 121 is the larger-airplane rule and the rule set that applies to these types was not checked):** Twin Otter, round trip plus 2 hours at 160 kt (593 km): Mirny 1,287 km, Casey 1,471 km, against 1,435 km published; Basler, round trip plus 2 hours at 195 kt (722 km): Mirny 1,416 km, Casey 1,600 km, Wilkins 1,686 km, against 1,759 km published.
- **Reported:** Casey to the Bunger Hills by Twin Otter, "nearly 2 hours" for "close to 450 km"; a 1999 Twin Otter Bunger→Casey turned back to Bunger because of cloud at Casey (already known, UNVERIFIED and SOURCED respectively).
- **A jet between Wilkins and the oasis:** 482 km is a short leg for any listed jet; no jet has landed at the oasis (none found). **NOT FOUND:** any operator's or regulator's analysis of a Wilkins-oasis pair.

## 4. Season and weather at the oasis

**Three records are used, each on its own terms (none is a runway record):** (1) the Soviet Oasis station, Oct 1956-late 1958, monthly tables (already known, soil file E); (2) **new here:** the Russian AWS "Oazis" (WMO 89601, Vaisala MAWS410, 42 m, on rock in the oasis), its SYNOP reports 2014-2026 from the Ogimet archive, six-hourly, **5,375 usable wind reports** (2014, 2017-2020, 2022-2026; 2015, 2016 and 2021 are all "NIL"), winds in m/s ("measured") in 93% of messages and knots in 7% (converted); the AWS reports **no visibility and no cloud** ("46///"); (3) **new here:** ERA5 hourly reanalysis 1991-2020 at the grid point 66.25°S 100.75°E (model elevation 54 m) via the Open-Meteo archive API. *ERA5 check (DERIVED):* its annual mean is −12.4 °C and January −2.1 °C against the station's −9.0 °C and +1.8 °C; its calms (<1 m/s) are 2.2% of hours against the station's 39% of observations. **ERA5 is colder and windier-in-light-air than the oasis's own records; treat its temperatures as those of a cell that mixes rock, lake and ice sheet, and its light-wind statistics as unreliable here.**

### 4a. Summer melt and the temperature thresholds
- **The thresholds in use elsewhere (already known):** Wilkins needs the runway at or below −7 °C (Carpentier 2010) or below −5 °C (AFP 2012); glacial-runway friction concern begins warmer than −5 °C, and "at least 0.25" is present below −10 °C (CRREL 98-1); Novo closes in January for slush and small lakes on the runway.
- **Station monthly mean air temperatures (1956-58):** Nov −3.5, Dec +1.7, Jan +1.8, Feb −2.2, Mar −6.0, Oct −11.2 °C; ground surface means above 0 °C from November to February (already known). *DERIVED:* every month from November through March has a mean air temperature warmer than −7 °C at the station, and November through February warmer than −5 °C.
- **ERA5, share of hours at or below −7 °C (and −5 °C), 1991-2020 (DERIVED):** Oct 91% (97%); **Nov 49% (66%); Dec 17% (30%); Jan 10% (20%); Feb 34% (49%)**; Mar 74% (87%); Apr-Sep 87-93% (94-98%). Hours above 0 °C: Jan 30%, Dec 19%, Feb 11%, Nov 2%.
- **ERA5, December-January by hour (DERIVED):** coldest at 17-20 UTC (local solar time about 23:00-03:00; the oasis is at 100.75°E, about UTC+6:43), mean −5.1 to −5.4 °C with **30-33% of those hours at or below −7 °C**; warmest at 06-09 UTC (local solar about 13:00-16:00), mean −0.3 °C with **0%** at or below −7 °C. November and February: 56-60% of hours at or below −7 °C at 15-21 UTC, 19-27% at 03-09 UTC.
- **On the oasis surfaces themselves (SOURCED, item 1):** Transcription Gulf shows no "signs of spring decay," but its top 30 cm forms from snow that melts in summer and refreezes, and cryoconite cavities are melt features; the Apfel strip had water-filled cracks and "water-logged areas" in late January-February 2019; Lake Figurnoye is "mostly ice-free" in summer; White Smoke Lake's AWS recorded 71 thawing degree-days in 1992-93 against about 108 estimated from the station's means (soil file E).
- *Reading (DERIVED):* on both the station means and ERA5, December and January at the oasis are warmer than the −5/−7 °C thresholds used at Wilkins for most hours of the day; the night hours are the cold part of the day in every summer month.
- A measured runway-surface (ice-surface) temperature record at the oasis: **NOT FOUND.**

### 4b. Wind: speed, direction and crosswind exposure

**Speed:**

| Record | Mean | ≥15 m/s | Maximum | Calm |
|---|---|---|---|---|
| Station 1956-58 | 6.8 m/s | 122 days a year (33%) | 56 m/s (April) | 39% of observations |
| AWS 89601, 2014-2026 (DERIVED from SYNOP) | 5.3 m/s | **11.6% of reports** (≥20 m/s: 4.9%) | 31 m/s (six-hourly reports, not gusts) | 7% |
| ERA5 1991-2020 (DERIVED) | 7.3 m/s | 11.3% of hours (≥20 m/s: 4.4% of hours; Jun-Aug 8.3-9.4%) | 39.8 m/s hourly; gust 55.9 m/s | 2.2% |

AWS monthly share of reports ≥15 m/s (DERIVED): Jan 3.9%, Feb 4.3%, Mar 10%, Apr 9.7%, May 13%, Jun 15%, **Jul 22%**, Aug 16%, Sep 13%, Oct 14%, Nov 5.6%, Dec 0% (December has only 180 reports). ERA5 monthly ≥15 m/s: Dec 4.3%, Jan 4.0%, Feb 5.1%, Jun 19.7%, Jul 18.6%.

**Direction:**
- Station (SOURCED, soil file E): maximum winds "from the east, all in the ENE-ESE octant"; strong winds (>10 m/s) today **118 ± 21 °T** (Gore & Leishman 2020); the oasis lies under the slope-wind zone but the main katabatic flow "miss[es] the elevated oasis or pass[es] above."
- Apfel survey (SOURCED): the 090° strip "matches the prevailing winds in the oasis."
- **AWS 89601 (DERIVED, my decoding):** all winds: E 30%, SW 12%, SSW 9%, S 7%, ENE 7%, ESE 6%; **winds ≥15 m/s (622 reports): E 32%, SW 22%, SSW 20%, ENE 10%, ESE 5%, S 5%.** *The AWS shows a second strong-wind direction, from the south-southwest to southwest, that neither the 1956-58 summary nor the Gore & Leishman figure describes. Whether this is a real local flow (for example off the ice sheet and Apfel Glacier to the south), sheltering of the site, or a sensor-orientation error was not resolved; no published analysis of this AWS's winds was found.*
- **ERA5 (DERIVED):** all winds E 34%, ESE 27%, SE 16%, ENE 13%; winds ≥15 m/s: **E 81%**, ENE 13%, ESE 5%. ERA5 has no south-westerly mode.

**Crosswind exposure on the bearings of the measured surfaces (DERIVED; a crosswind component is speed × sin(angle off the line); calm counted as zero; not a runway design).** Bearings: 060° and 070° (the longest lines on Transcription Gulf, item 1a); 090° (the Apfel strip and the gulf's 5.8 km W-E line); 115° and 120° (close to the Gore & Leishman strong-wind direction).

| Line | AWS 89601: share of reports with crosswind >10 kt / >20 kt / >25 kt | AWS, Nov-Feb only: >10 / >20 kt | ERA5: share of hours >10 kt / >20 kt / >25 kt | ERA5, Nov-Feb: >10 / >20 kt |
|---|---|---|---|---|
| 060°/240° | 16% / 5% / 2% | 9% / 1% | 27% / 4% / 1% | 14% / 1% |
| 070°/250° | 17% / 5% / 2% | 11% / 2% | 15% / 1% / 0% | 6% / 0% |
| 090°/270° | 17% / 7% / 5% | 14% / 4% | 3% / 0% / 0% | 1% / 0% |
| 115°/295° | 22% / 11% / 8% | 19% / 7% | 21% / 4% / 1% | 19% / 2% |
| 120°/300° | 23% / 12% / 8% | 21% / 7% | 24% / 6% / 2% | 22% / 4% |

- *Reading (DERIVED):* the two records agree that strong winds come from the east, and they disagree about the rest: in ERA5 a 090° line is almost never crossed by more than 10 kt, while at the AWS the south-westerly strong winds cross every one of these bearings. **The crosswind exposure of any line at the oasis therefore depends on which record is right, and no source resolves it.** For scale: Skytraders' own criterion at Wilkins (2008) was "less than 5 knots of cross-wind"; the Twin Otter's demonstrated crosswind is 20 kt (not limiting); a secondary summary gives "about 5-10 kts" as a typical crosswind limit on ice (UNVERIFIED, search-result text of a flight-simulation guide).

### 4c. Blowing snow, cloud and visibility
- **Station 1956-58 (SOURCED, soil file E):** blizzard on **53 days a year** (Jul and Sep 10 each, Aug 8, May 6, Jan 0, Dec 1, Nov 2, Feb 2); total cloud **7.0 tenths** on average (6.0-8.2 by month); **39 clear days a year** (2-5 a month); **fog on 4 days in two years**, all in July 1958; "the permanent snow cover does not form even in winter," and "a few windy days ... were enough to blow out nearly the whole snow" (1989).
- **ERA5 low cloud ≥50% (DERIVED):** 15-16% of hours in Nov-Jan, 19-22% in Feb-Oct. *Model cloud, not observed ceilings.*
- **The AWS reports no visibility or cloud** (SYNOP "46///"). A visibility, ceiling or whiteout statistic for the oasis: **NOT FOUND.**
- **Flight-delay record (already known, port file B):** Dec 2023 "multiple flight delays due to high winds and blizzards" to Bunger; 28 Dec 1999 a Twin Otter returned to Bunger because of cloud at Casey; Jan 2022 non-flying weather canceled Russian air-landed work.

### 4d. Sun and twilight at 66.27°S (DERIVED, NOAA declination approximation, ±10-20 min; 2026)

| Mid-month | Noon sun height | Sun above horizon | Civil light (sun above −6°) | Nautical light (above −12°) |
|---|---|---|---|---|
| 15 Jan | 45° | 21.0 h | 24 h | 24 h |
| 15 Feb | 37° | 16.5 h | 19.0 h | 24 h |
| 15 Mar | 26° | 13.0 h | 14.8 h | 17.1 h |
| 15 Apr | 14° | 9.3 h | 11.1 h | 13.1 h |
| 15 May | 5° | 5.7 h | 8.0 h | 10.3 h |
| **21 Jun** | **0.3°** | **2.5 h** | **6.0 h** | **8.7 h** |
| 15 Jul | 2° | 4.0 h | 6.8 h | 9.3 h |
| 15 Aug | 9° | 7.6 h | 9.6 h | 11.6 h |
| 15 Sep | 20° | 11.3 h | 13.0 h | 15.0 h |
| 15 Oct | 32° | 14.9 h | 16.8 h | 19.8 h |
| 15 Nov | 42° | 19.0 h | 24 h | 24 h |
| 15 Dec | 47° | 24 h | 24 h | 24 h |

- The sun does not set on **about 23 days** around the December solstice; civil light lasts all night on **about 79 days** (mid-November to late January); **there is no day on which the sun fails to rise.** Check: the station's published day lengths (Jan 20 h 56 min, Jun 2 h 32 min, Dec 24 h; soil file E) agree with these to within about 5 minutes.
- *Reading (DERIVED):* the coldest hours of the summer day (4a) fall in the low-sun hours around local midnight, when the sun is low but, from mid-November to late January, it is never darker than civil twilight.

### 4e. What item 4 adds up to (facts only)
- December and January are warmer than the Wilkins thresholds for most hours on every record; the night hours are colder. (SOURCED thresholds; DERIVED shares.)
- Strong winds (≥15 m/s) blow in roughly 11-12% of the time on both the AWS and ERA5, peaking in winter (July 22% at the AWS) and lowest in December-February (about 4%). (DERIVED.)
- Strong winds come from the east on every record; the AWS adds a south-south-westerly strong-wind mode that ERA5 and the published summaries lack, and the crosswind exposure of any line depends on which is right. (DERIVED; unresolved.)
- Blizzards on about 53 days a year, cloud cover 7/10, fog rare (1956-58). (SOURCED.)
- **NOT FOUND:** visibility and ceiling statistics; ice-surface temperatures; the Australian Bunger Hills AWS data (BoM station 300061, WMO 89817: SYNOP "NIL" in the January 2024 sample; the AAD tafoni dataset with the 1986 Edgeworth David and 2000 Apfel Glacier AWS winds is behind a JavaScript download page).

## 5. Freight-airport operations on ice

**Already known, not repeated:** Wilkins' facility list and "up to eight expeditioners" in season, its four-person spring start-up taking about two months, the snow-groomer tilling before each wheeled flight, the 88 t proof roller, the snow blowers airdropped in 2018; the A319's 2 hours on the ground; USAF engines left running about an hour on the ground in winter; Pegasus's recommended staff (two full-time, storm help, a half-time mechanic, a supervisor) and its graders, drags, planes and 45 t roller; Novo's runway prepared by the Russian expedition with a pneumatic-wheeled roller; Phoenix's 73 t weight cart; the Il-76's 226 Novo flights in 2001-2022 (intake file A; operations file).

### 5a. Payload actually carried per flight (as found)

| Aircraft and route | Payload | Status |
|---|---|---|
| RAAF C-17A, Hobart-Wilkins, first proof-of-concept flight, Nov 2015 | **12,340 kg** unloaded, "including a brand new Hägglunds" over-snow vehicle; 3,450 km "in just over five hours"; round trip from Hobart | **SOURCED** — AAD news 2015, "Flying high on C-17A proof of concept success in Antarctica"; Contact magazine (Hägglunds driven off) |
| Same series, five flights | "more than 109 metric tons" in total; the RAAF commander: "to get in on the ice at Wilkins all the way from Hobart we carry about 20 metric tons of equipment and people" | **UNVERIFIED** (search-result text; australianaviation.com.au 403; Defense minister's release "socket hang up") |
| Il-76TD-90VD, Cape Town-Novo, first DROMLAN season (2015-16), 12 return flights | 125 t of general cargo delivered, 64 t carried back, 34 t onward inland: "over 190 metric tons" | **SOURCED** — Volga-Dnepr press release 3669. *DERIVED:* about **10.4 t south per flight** on a combined cargo-and-passenger service. Since 2015: "around 1,700 metric tons" (aviacionline, SOURCED as reported) |
| Il-76TD-90VD, 2020/21 | five flights; "more than 200 tons of general cargo" | search-result text of Volga-Dnepr/payloadasia, **UNVERIFIED** |
| ALE Il-76TD, Punta Arenas-Union Glacier | 17,500 kg | already known |
| Norse 787-9, Cape Town-Troll, 2023 | 45 passengers and 12 t | already known |
| USAF C-5B, Christchurch-McMurdo, 4 Oct 1989 | about 168,000 lb (76 t) and 72 people | SOURCED (item 2d) |
| USAF C-17, Christchurch-McMurdo, 2007-08 season | "58 C-17 missions," "5,651 passengers and more than 5.6 million pounds of cargo" (*DERIVED:* about 44 t a mission if all one-way southbound; the release's counting basis is not known) | **UNVERIFIED** (search-result text of a US Air Force release; af.mil 403; globalsecurity 402) |

### 5b. Fuel at polar ice airfields
- **Wilkins (Skytraders, 2008):** the A319 carries four extra center tanks so that it needs no fuel at Wilkins: no point of no return, "no risk of contamination from a fuel spill," and "transporting fuel to the Wilkins runway would make it very costly – perhaps as much as $25 a gallon." **SOURCED**, *FAST* 42.
- **Australian aviation fuel delivery to stations:** "Each season, a new shipment of fuel is delivered to stations, primarily Casey and Davis ... usually in the range of 600–800 drums, each drum holding 205 liters"; aviation fuel is Jet A-1. *DERIVED:* 123,000-164,000 liters a season. **SOURCED** — AAD "This week at Casey, 7 February 2014." Wilkins' own storage capacity: **NOT FOUND** (AAD page lists "fuel storage" without volumes).
- **Troll:** "Ground handling, including supply of Jet A-1 fuel, is provided by the crew at Troll"; fuel kept in drums and large tanks on absorbent mats, with spill-response equipment and plans. **SOURCED at Wikipedia** ("Troll Airfield").
- **Novo:** the Russian expedition "prepares and maintains the runway" and delivers "aviation fuel to the airfield"; ALCI provides radio communications, weather monitoring, food and accommodation. **SOURCED**, Volga-Dnepr press release 3669. In 2015 an Il-76TD-90VD airdropped 208 barrels of fuel onto a remote Antarctic airfield (search-result text, **UNVERIFIED**).
- **Union Glacier:** the Il-76 "arrives with enough fuel for the return trip and for diversions, because bringing fuel to the glacier is impractical" (search-result paraphrase of a 2013 visitor account; the page failed with an expired certificate; **UNVERIFIED**); ALE moves fuel depots for its inland flights by tractor train (forum, **UNVERIFIED**).
- **Mellor and Swithinbank (1989):** at blue-ice fields, "cargo handling, fuel transfer and runway maintenance" take place on the ice, "strict discipline should be enforced," and "any spills should be cleaned up without delay"; facilities are best placed on rock or moraine, on gravel pads "perhaps as little as 0.3 m" thick. **SOURCED**, CRREL 89-21, p. 65.
- **The 1962 precedent at this oasis:** full fuel for two aircraft was taken on at the Bunger runway (Lukin 2022, SOURCED). How the fuel got there: NOT FOUND.

### 5c. Ground equipment and staff (new items only)
- **Troll:** for construction the Norwegian Polar Institute bought "a snow groomer and a tracked vehicle with a snow blower, flatbed and ice cutter"; the station crew provide ground handling, fuel, fire and rescue, communications and overnight stays for stranded personnel. **SOURCED at Wikipedia.** Staff numbers: NOT FOUND.
- **Squaw Lake (lake-ice strip, 2013):** about 40 engineers in six-hour shifts; two weeks clearing, over three weeks flooding; certification by an Air Division engineer with GPR "adhesion tests" and checks for "air or water pockets"; "landing zone controllers" and firefighters at the landing. **SOURCED** (item 2d source).
- **Union Glacier:** a seasonal staff count of about 70 appears only on an AI-generated page (**UNVERIFIED**, not used).
- **McMurdo:** the US Navy Cargo Handling Battalion One provides "port services" at McMurdo (SOURCED, copy of a 2007 US Air Force release on mt-milcom.blogspot.com). Air-cargo loader types and offload times on the ice: **NOT FOUND** (af.mil and pacaf.af.mil 403).
- **Turnaround on the ice:** A319 about 2 hours (already known); C-17 time on the ground at Wilkins: NOT FOUND.

### 5d. Customs, quarantine and border presence at remote freight-only airfields
- **At the Antarctic end (Australia):** the Australian Antarctic Territory is outside Australia's migration zone, so every traveler has an international movement recorded at Hobart (already known). Cargo "shipped or flown to and from the Antarctic or sub-Antarctic Stations is processed through biosecurity screening" by the AAD's Supply Chain Operations section in Hobart — external inspection of cargo surfaces; internal inspection of transport units, consolidation and packing; external inspection and fogging of containers and break-bulk cargo — with pest control at the AAD Kingston warehouse and the Cargo and Biosecurity Center. **SOURCED** — AAD "Biosecurity" (cargo) page. Returning cargo must "comply with Australian regulations upon entry, including the Customs Act 1901 and the Biosecurity Act 2015" and be "cleared by the relevant regulatory bodies" before release (**UNVERIFIED**: search-result text; not on the two AAD pages opened). **No border or customs presence at Wilkins itself is described in any source found;** the checks happen at the Australian gateway.
- **The legal mechanism for an aircraft to arrive at a place that is not a designated airport (Australia):** "The master of a ship or the pilot of any aircraft shall not bring his or her ship or aircraft to a place other than a port or airport unless from stress of weather or other reasonable cause" (s 58(1)); this "does not apply if the master or pilot has the permission of a Collector" (s 58(1A)); a Collector "may, by notice in writing ... give the person permission, subject to such conditions (if any) as are specified in the notice, to bring the ship or aircraft to, or to remain at, that place" (s 58(2)), and conditions may cover "matters occurring while the ship or aircraft is at the place" (s 58(5)). **SOURCED** — *Customs Act 1901* (Cth), compilation of 10 March 2016, s 58 (legislation.gov.au, read). *Later amendments (2015 and after) to customs control at such places were seen only in search text and not checked.*
- **How a border agency serves a low-volume airport (Canada):** "All international travelers must be processed by a CBSA officer," so officers must travel to such airports, which strains "both agency resources and travelers"; on 12 May 2020 the CBSA was "redirecting air traffic from low-volume airports of entry to busier locations." **SOURCED** — Public Safety Canada, parliamentary briefing, 31 Aug 2020 (read). On-request CBSA service at Saguenay for international flights of up to 30 occupants, 48 hours' notice; international aircraft for Terrace, B.C., "must first stop in at another Canadian airport to clear customs" (search-result text, **UNVERIFIED**).
- **A precedent for a freight-only, ice-runway airfield with its own customs or quarantine post: NOT FOUND** (two searches; search log).

### 5e. What item 5 adds up to (facts only)
- Payload actually delivered per flight to Antarctic ice runways in the record runs from about 10 t (Il-76 on mixed service, DERIVED) and 12 t (C-17 to Wilkins, 2015; 787 to Troll, 2023) to about 17.5 t (Il-76 to Union Glacier) and, once, 76 t (C-5B to McMurdo sea ice, 1989). (SOURCED/DERIVED.)
- The operators that fly long legs to ice runways carry return fuel; fuel at the ice field is costly ($25 a gallon quoted at Wilkins, 2008) and is supplied by ship and drums where it exists (Casey/Davis drums; Troll; Novo by the Russian expedition). (SOURCED.)
- Border and biosecurity checks for Antarctic freight happen at the home gateway, not at the ice airfield; Australian law has a written mechanism (s 58) for permitting arrival at a place that is not a designated airport, with conditions. (SOURCED.)
- **NOT FOUND:** Wilkins fuel storage capacity; staff numbers at Troll, Novo or Union Glacier from a primary source; C-17 offload times; a freight-only remote airfield with its own customs post.

## 6. Two airfields at one Antarctic site

| Site | Airfields (real) | What each was for | Status |
|---|---|---|---|
| **McMurdo (US)** | (1) the **annual sea-ice runway** ("Ice Runway"), Oct to early Dec, wheels (C-5, C-141, C-17, C-130, P-3); (2) **Williams Field**, skiway on the Ross Ice Shelf, for ski aircraft (LC-130, Basler, Twin Otter), main skiway 25/07 and a "crosswind skiway" 33/15, each 220 × 10,000 ft; (3) **Pegasus**, glacial ice under a snow cap, wheels, 1993-2016, year-round until 2012, the field "for the months when the sea-ice airstrip was no longer operable (early December through September)"; (4) **Phoenix**, compacted snow, wheels, from 2016-17, replacing Pegasus and the sea-ice runway; plus (5) a surveyed "Whiteout Landing Area" on the shelf for ski-only landings in bad weather | wheels in spring (sea ice), wheels in summer and winter (Pegasus, then Phoenix), skis all season (Williams), whiteout ski fallback | SOURCED — Wikipedia "Ice Runway"; USAP Air Operations Manual 2026; CRREL TR-19-4 (already known, intake file A, items 4a and 5a) |
| **Casey (Australia)** | (1) **Wilkins**, blue ice, 70 km from Casey, wheels (A319, C-17), summer only; (2) **Casey ski landing area** near the station ("Casey (inland of SLA) — alternate for Casey SLA or Wilkins," in the AAD's indicative landing-site list); (3) the 1988 S-1 blue-ice strip 6 km east of Casey (one Twin Otter wheel landing) | intercontinental wheels at Wilkins; intracontinental skis at the station; an "alternate" listed for the ski area and Wilkins (aircraft class not stated) | already known (operations file 2b; intake file B 9.4) |
| **Novolazarevskaya / Schirmacher oasis (Russia)** | the blue-ice runway 7 km from the oasis (Il-76, wheels); the station's own ski operations | intercontinental wheels; intracontinental skis | already known (intake file A 4c) |
| **Mario Zucchelli (Italy)** | (1) the seasonal **sea-ice runway** in Gerlache Inlet, prepared from mid-October, with **two strips**: 03/21, 3,090 m, for wheeled C-130s, and 06/24, 1,640 m, for Twin Otters and Basler BT-67s; "in the latest years it was closed earlier than before because the sea ice break up"; (2) **Enigma Lake Skiway**, lake ice about 3 km south of the station, 725 m, Twin Otter and Basler, "prepared by removing the snow accumulated in the winter by the Station staff"; (3) **Boulder Clay**, gravel on moraine over glacier ice, 60 m wide, "the first 1,700 meters out of the 2,200 envisaged," first C-130J landing in late 2022 (Wikipedia: 22 Nov 2022; ENEA release dated 7 Dec 2022), built because of "the emergency caused by thinning sea ice"; ENEA: the sea ice is usable "for only about a month at the start of the austral summer," and in 2022 operations were diverted to McMurdo | heavy wheels on sea ice in spring, light ski/wheel aircraft on a separate sea-ice strip and on lake ice, and a gravel strip as the alternative when sea ice fails | **SOURCED** — ENEA press release, 7 Dec 2022 (read); Wikipedia "Zucchelli Station" (read); USAP AOM 2026 (already known) |
| **Mirny (Russia), historical** | 1956: ski and wheel versions of Il-12, Li-2, An-2 plus Mi-4s; 1961-64 Il-18 on prepared snow at Mirny, with the **Bunger Hills runway** used for full fuel (1962) and as first landing (1963) | the Bunger strip served as the refueling and arrival field for the Mirny operation | SOURCED (Lukin 2022; intake file A) |
| **Bunger Hills itself** | Transcription Gulf (lake ice; Il-14, Il-18, Australian Twin Otter, CASA 212) and the Apfel blue-ice strip surveyed in 2019 as an "alternate in the Bunger oasis area for light and medium aircraft" | the 2019 Russian proposal names the Apfel site as the oasis's alternate to the gulf | SOURCED (Polyakov 2019) |

- **The cost side of several fields at McMurdo:** the US program has run "as many as three airfields, the Sea Ice Runway, Williams Field, and Pegasus Runway"; separate airfields meant separate fire-fighting crews and equipment; a design study proposed "a single skiway for ski-equipped aircraft and a single runway for wheeled aircraft" in their place (*Design and Implementation of a Consolidated Airfield at McMurdo*, DTIC ADA609591, and *McMurdo Consolidated Airfields Study: Phase I*, ADA576164). **UNVERIFIED** — search-result text only; the Antarctic Sun page failed on DNS, the openpolar record on a certificate error, and DTIC is 403 (already known).
- **What two fields at one site were for, in the record (SOURCED pieces; DERIVED summary):** a **season split** (McMurdo sea ice for spring, Pegasus/Phoenix for summer and winter; Mario Zucchelli sea ice then gravel); a **gear or size split** (wheels on glacier ice or sea ice, skis at a station skiway: McMurdo Williams, Casey, Novo; at Mario Zucchelli a 3,090 m sea-ice strip for C-130s beside a 1,640 m strip and a 725 m lake-ice skiway for Twin Otters and Baslers); a **weather fallback** (McMurdo's whiteout landing area; the Apfel site as the Bunger Hills alternate; the Casey inland "alternate"); and a **replacement** sequence as one surface failed (sea ice → Pegasus → Phoenix; sea ice → Boulder Clay).
- **NOT FOUND:** any Antarctic site where two wheeled jet runways operated at once for separate traffic (passenger and freight); any document describing a separate freight-only field at an Antarctic site.

## FINAL: what the surfaces can and cannot carry, what can reach the oasis and return, and what was not found

**No recommendation and no ranking.** Each cell says what it rests on. "Gold A = 4" is the Northwest Territories "Routine" rule for moving loads (P kg = 4 h² cm), applied by me.

### The surfaces

| Surface | Measured size | Surface and slope | Thickness / ice | What the sources say it carried or can carry | What limits it (as found) | Status |
|---|---|---|---|---|---|---|
| **Transcription Gulf** (epishelf lake) | 18.5 km² level ice at about 1.7 m above the geoid; longest straight lines **7.7 km at 060°/240°**, 5.8 km at 090°; clean Zone 1 about 1.5 × 0.35-0.5 km, Zone 2 at least 3.3 × 0.4-0.8 km (from the 2019 figure, ±15%) | "perfectly level"; cryoconite pits to 6 m × 0.3 m in Zones 2-3; tidal cracks at the shores; does not break up | **2.95-3.20 m** GPR (2019); "close to 3 m," max 5 m; about 4 m (1990); fresh, monolithic below 30 cm | **Carried two wheeled Il-18Vs on a prepared lagoon strip (Dec 1963)**, an Il-14 (1960s), ski Twin Otters, a CASA 212 (damaged on sastrugi, 2010); survey: bearing "fully allows heavy aircraft on wheeled undercarriage"; Gold A = 4 → about **350-410 t** moving load | stationary loads, wet (tidal) cracks and pitted ice are outside the moving-load rules; length of cavity-free ice not stated; summer surface condition not recorded year to year | SOURCED / DERIVED |
| **Apfel Glacier strip** (blue ice) | **2.34 km** at 091° (surveyed line); grade limits it to about 2.3-2.5 km on that line | 140-160 m; ≤2.1% per 288 m; cracks ≤25 cm, water-filled; "water-logged areas" in summer | grounded glacier ice; thickness not measured; 3-13 m/yr | surveyed for **ski** An-2 and BT-67 only (BT-67 after crack filling); blue ice: "virtually no limit to the total load" (Mellor & Swithinbank) | length on this alignment; summer water; crack filling | SOURCED / DERIVED |
| **Blue ice east and south of the oasis** | 3,304 km² area; 273 flat 3 km lines ≤15 m/yr | 240-785 m on the slow lines | ice sheet | possibly the 2000 Australian alternate (not confirmed); no landing found | crevassing, melt, identity: not found | intake file B; DERIVED |
| **Northern marine bays** | 88.8 km² flat at 1.3 m; lines to **14.3 km** | flat | ice type and thickness **unknown** | nothing found | whether it is perennial, fast or seasonal ice: not found | DERIVED; NOT FOUND |
| **Lake Figurnoye** | flattest stretch 5.5 km²; lines about 4.3-4.4 km | 13.3 m (REMA) | seasonal; "mostly ice-free" in summer; winter thickness unknown | An-2 landing, Aug 1956; one Li-2 broke through an oasis lake in 1966 (lake not named) | summer open water; unknown winter thickness | SOURCED / DERIVED |
| **White Smoke Lake** | not measured | — | perennial, 1.8-2.8 m | nothing found | size | soil file E |
| **Rock** | — | relief to 100-165 m | — | "not possible ... because of the complex surface relief" | — | SOURCED |

### Real aircraft against the oasis (published figures; DERIVED arithmetic: Case A = round trip + 2 hours' cruise; Case B = one way + 2 hours' cruise, fuel taken at the oasis)

| Aircraft | Payload at stated range | Hobart (3,840 km) A / B | Perth (3,952 km) A / B | Real ice-runway use (as found) |
|---|---|---|---|---|
| A319-115LR (AAD) | about 38 passengers + light cargo | ≈ / ✓ | ≈ / ✓ | Wilkins, Mario Zucchelli sea ice |
| A319neo, A320neo, 737-8 | typical passengers | ✗ / ✓ | ✗ / ✓ | — |
| A321XLR | typical passengers | ✗ / ✓ | ✗ / ✓ | — |
| A330-900, 787-8/-9 | typical passengers | ✓ / ✓ | ✓ / ✓ | 787-9 at Troll (45 passengers + 12 t) |
| 777F | 103.7 t | ✗ (2% short) / ✓ | ✗ (4% short) / ✓ | none found |
| A330-200F | 65 t; 70 t | ✗ / ✓ | ✗ / ✓ | none found |
| 767-300F | 52.7 t | ✗ / ✓ | ✗ / ✓ | 767 at Troll (Wikipedia list) |
| Il-76TD-90VD | 50 t at 4,000 km | ✗ / ✗ | ✗ / ✗ | Novo (about 10 t south per flight on mixed service); Union Glacier 17.5 t |
| C-17A | 72.6 t at 4,445 km | ✗ / ✗ at that payload | ✗ / ✗ | Wilkins round trip from Hobart with 12.3 t (2015); "about 20 metric tons" (UNVERIFIED) |
| C-130J | 15.4 t at 3,300 km | ✗ / ✗ | ✗ / ✗ | Squaw Lake lake ice at 50.8 t; Boulder Clay gravel |
| 737-800BCF | 23.95 t at 3,695 km (UNVERIFIED) | ✗ / ✗ | ✗ / ✗ | — |
| Twin Otter / Basler | 19 / 18+ passengers | Mirny and Casey legs (347 / 439 km) inside published range with 2 hours (Twin Otter from Casey marginal) | | the aircraft the Australian program has used at the oasis (Twin Otter on the gulf; CASA 212 in 2010) |

✓ = published range at that payload exceeds the need; ✗ = it does not; ≈ = about equal. *Published ranges assume the maker's standard reserves and no wind; payload-range charts were not opened.*

### The season (facts only)
- Dec-Jan: station monthly means +1.7/+1.8 °C; ERA5 has 10-17% of hours at or below −7 °C, nearly all at night (local midnight ±3 h). Nov and Feb: about half. Mar-Oct: 74-93%. (SOURCED / DERIVED.)
- Strong winds ≥15 m/s about 11-12% of the time, peaking in winter (AWS July 22%), lowest Dec-Feb (about 4%); from the east on every record, with a south-south-westerly strong-wind mode on the AWS only. (DERIVED.)
- Blizzards on about 53 days a year; cloud 7/10; fog rare (1956-58). (SOURCED.)
- Sun up 2.5 h at midwinter, never fails to rise; continuous daylight about 23 days, all-night civil light about 79 days. (DERIVED.)

### What was NOT FOUND (collected)
1. The cryoconite-free length on Transcription Gulf; zone dimensions in text (only the 2019 figure); the gulf's year-by-year summer surface; Gibson & Andersen 2002 Table I (403).
2. Ice type, thickness and persistence of the northern marine bays; Figurnoye's winter ice thickness.
3. Apfel Glacier ablation and ice thickness at the strip (stake results unpublished).
4. Whether the 2000/01 Australian C-130 trial of a Bunger blue-ice runway was flown, and that site's position.
5. Which lagoon of Transcription Gulf held the 1963 Il-18 strip, and its length; the Il-18V's weights; how fuel reached the 1962 runway.
6. Assur's 1956 SIPRE tables of ice thickness per aircraft (ERDC browser check; DTIC 403); the McMurdo sea-ice runway criteria (DTIC 403).
7. Any wheeled jet landing on lake ice; any Il-76 on floating ice.
8. Payload-range charts for any type (so the payload each could carry on a no-refuel round trip).
9. Visibility, ceiling and whiteout statistics for the oasis; ice-surface temperatures; the Australian Bunger Hills AWS record (BoM 300061 "NIL"; AAD dataset behind JavaScript); an explanation of the AWS's south-westerly strong winds.
10. Wilkins' fuel storage capacity; staff numbers at Troll, Novo and Union Glacier from a primary source; C-17 offload times.
11. A freight-only remote airfield with its own customs or quarantine post; a real Antarctic site with two simultaneous wheeled jet runways for separate passenger and freight traffic.

## Search log
(Exact strings; result; dead ends say whether they died at the query or at the sources.)

### Item 1
1. `Организация нового аэродрома РАЭ в районе оазиса Бангера Российские полярные исследования 37 2019 pdf` (standard) — found the RPR 37 PDF (data.aari.ru) and a core.ac.uk link for the companion paper. RPR 37 PDF downloaded with curl and re-read in full (text and Fig. 4).
2. (download) core.ac.uk `download/487571642.pdf` with curl — returned an HTML page, not the PDF. **DEAD-SOURCE.** *Self-correction (recording law): this curl carried a generic browser user-agent string; intake file B records that a user-agent curl to the AARI journal was refused by the session's permission classifier. This one was not refused, but I did not repeat it and did not try any other route to that paper.*
3. (data) Fig. 4 extracted with `pdfimages`; scale bar and zones measured with a Python script (method in 1a).
4. (data) ITS_LIVE v2 120 m mosaic sampled along the Apfel centerline and at gulf, rock and lake points (rasterio, `/vsicurl/`).
5. (data) REMA v2.0 32 m tiles `26_56`, `25_56` and the EGM2008 grid downloaded; tile `36_53` downloaded first by mistake while working out the tile grid (the grid is 100 km tiles, `row = floor((y+3,000,000)/100,000)+1`, `col` the same in x); not used.
6. `Transkriptsii Gulf Bunger Hills epishelf lake area km2 ice thickness perennial` (standard) — Doran et al. 1996 and Gibson & Andersen 2002 records. Doran 1996 abstract read (repository.lsu.edu/geo_pubs/692; "not available here" for the PDF). Gibson & Andersen 2002 on cambridge.org: **403, DEAD-SOURCE** (Table I with each lake's area and ice thickness not read).
7. `Ил-18 1963 посадка оазис Бангера лагуна ледовый аэродром Антарктида` (standard) — Lukin 2022 (RPR 48) re-downloaded and read: **found "in one of the lagoons of Transcription Gulf."** RPR 40 (Andreev 2020 botany) downloaded; nothing on airfields.
8. `Soviet Il-18 Bunger Hills ice runway 1962 refuel Christchurch lake ice landing` (standard) — aeroflotarchives.com "Polar aviation" read.
9. Wikipedia "Ilyushin Il-18" read (Il-18D specifications).
10. `Ил-18В максимальная взлетная масса кг посадочная масса характеристики` (standard) — cyclowiki: **403, DEAD-SOURCE**; airvectors.net/avil18.html: **404, DEAD-SOURCE**. Il-18V weights NOT FOUND.
11. `Li-2 1966 Bunger Hills lake ice broke through sank Dobrowolski station aircraft` (standard) — Dobrowolski English history and home pages read: no aircraft account (**DEAD at those pages**).
12. `"Bunger" 1966 samolot Li-2 lód zatonął stacja Dobrowolskiego` (standard) — **DEAD-QUERY.**
13. `Ли-2 провалился под лед озеро оазис Бангера 1966 самолет затонул` (standard) — **DEAD-QUERY.** Then the page cited by port file B, dobrowolski.igf.edu.pl/wyprawy/1965-1966/, was opened directly and read (the account is there).
14. `"Bunger Hills" blue ice runway Hercules trial 2001 Australian Antarctic Division air link` (standard) — only the 2000 plan; **trial outcome DEAD at the sources.**
15. `Australian Antarctic air transport study 2001 Hercules flight Casey Bunger Hills blue ice landing not flown postponed` (standard) — *Australian Antarctic Magazine* 20 (2011) read (CASA 212 recovery). Aviation Safety Network wikibase/321215: **certificate error, DEAD-SOURCE** (not worked around). Trial outcome still **NOT FOUND**.
16. `Bunger Hills marine inlets multiyear fast ice perennial Highjump Archipelago sea ice thickness breakout` (standard) — **DEAD at the sources** (general fast-ice papers only).

### Item 2
17. `Gold's formula ice bearing capacity P = A h^2 aircraft ice runway thickness guideline` (standard) — Barrette 2015 (tac-atc.ca): first curl got an HTML page; the same URL with redirects followed (`-L`, no other change) gave the PDF; read.
18. `ice airstrip lake Hercules L-382 required ice thickness Lac de Gras Diavik ice runway Boeing 737` (standard) — CMEA "Ice landing" PDF read; UAF news found. Diavik is a gravel runway (Wikipedia via search text), so not a lake-ice case. ERDC library "Airfields on floating ice sheets for routine and emergency operations": **browser-verification page, DEAD-SOURCE** (not worked around).
19. `"Airfields on floating ice sheets for routine and emergency operations" CRREL special report ice thickness aircraft gross weight` (standard) — identified as Assur 1956, SIPRE Report 36; DTIC ADA224867 and ADA200444: **403, DEAD-SOURCE.** Assur's aircraft thickness tables NOT FOUND.
20. Transportation Overview (Poland) 2018 "Airfield pavements on the lake ice sheets" downloaded and skimmed: light-aircraft, Polish lakes (30-80 cm); not used.
21. `Mellor Swithinbank "Airfields on Antarctic glacier ice" CRREL 89-21 pdf` (standard) — scan downloaded from southpolestation.com; bearing, friction and facilities passages read (OCR rough; quotations checked against the page layout).
22. UAF news, "Frozen Arctic lakes becoming less capable of supporting cargo aircraft" (4 June 2026), read. 109th Airlift Wing article: **403, DEAD-SOURCE**; DVIDS printable 501394 read instead (same event).
23. `McMurdo sea ice runway C-17 minimum ice thickness inches wheeled aircraft requirement` (standard) — Wikipedia "Ice Runway" read; the 70 in blog figure left UNVERIFIED; DTIC ADA453025 already known refused.
24. `C-5 Galaxy first landing Antarctica McMurdo sea ice runway 1989 cargo tons ice thickness` (standard) — Air & Space Forces "This day in airpower" entry read.
25. `Airbus FAST 42 A319 Antarctica Wilkins blue ice runway friction landing distance` (standard) — no new primary; then the *FAST* 42 PDF (URL from the operations file) downloaded and the blue-ice article read in full.
26. `runway condition code ice RWYCC 1 poor braking landing distance factor compared to dry EASA AMC 25.1591 table` (standard) — **DEAD-QUERY** for the EASA table.
27. `Transport Canada AC 700-057 landing distance factors table runway condition code` (standard) — FAA Order 8900.1 Table 4-11 PDF and Transport Canada CASA 2018-08 PDF downloaded and read.
28. `ледовый аэродром на озере толщина льда Ил-76 Ан-12 посадка требуемая толщина льда норматив` (standard) — Pogorelova, Kozin, Matyushina 2015 (sibran.ru) PDF read. A Soviet norm "ВСН 37-76" for Antarctic snow-ice airfields was named in a search result (AARI RPR 57); not opened (it concerns snow-ice runways, not floating ice).
29. `Alberta "Best Practice for Building and Working Safely on Ice Covers" wet cracks reduce load 50% A value table` (standard) — Alberta PDFs not opened; the NWT DOT *Guidelines for Safe Ice Construction* (2015) PDF found in the results, downloaded and read instead.
30. Aircraft data pages read: Wikipedia "Airbus A330," "Boeing 767," "Boeing 777," "Ilyushin Il-76" (specifications section not reached in the 100,000 characters read), "Boeing C-17 Globemaster III," "Lockheed Martin C-130J Super Hercules."

### Item 3
31. `Volga-Dnepr Il-76TD-90VD maximum payload 50 metric tons range km specifications fleet` (standard) — Volga-Dnepr technical specification page read.
32. `Boeing 737-800BCF converted freighter payload range nautical miles official; A321P2F payload 28 metric tons range EFW` (standard) — Boeing brochure PDF: **HTTP 301 to an HTML page, DEAD-SOURCE**; figures left UNVERIFIED. A321P2F range: **NOT FOUND** (trade press only).
33. (data) Distances computed with pyproj `Geod` (WGS84) from the Oazis AWS; airport coordinates: Hobart, Perth, Casey, Wilkins, Mirny as in the operations file; Jakarta, Singapore, Denpasar, Darwin, Learmonth, Kuala Lumpur from my own knowledge of the airport reference points (**UNVERIFIED** to about ±2 km, which does not change any figure at the precision given).

### Item 4
34. (data) Open-Meteo archive API, ERA5, hourly 1991-2020 at −66.27, 100.75 (returned grid point 66.25°S 100.75°E, 54 m): temperature, 10 m wind, gusts, low cloud. One request, no rate limit hit.
35. `AMRC automatic weather station "Bunger Hills" AWS data wind 2020` (standard) — no AMRC record for the oasis; BoM station 300061 (WMO 89817) found; AAD tafoni dataset found. AAD download `data.aad.gov.au/eds/5092/download`: **JavaScript app page, DEAD-SOURCE** (not worked around).
36. (data) Ogimet SYNOP archive (`ogimet.com/cgi-bin/getsynop`), WMO 89601, one request per year 2014-2026 with 15 s pauses; WMO 89817 tested for January 2024: all "NIL." *Self-correction (recording law): my first decoding read the temperature group as a wind group in four messages that have no wind group, giving a false 65 m/s maximum; the parser was fixed to accept only wind groups beginning "/" and all wind figures in 4b come from the corrected run.* The SYNOP temperature groups carry an unexpected sign digit ("12000," "12032") in summer messages and were **not used**.
37. `Bunger Hills oasis wind direction southwest foehn katabatic Edgeworth David AWS Apfel Glacier wind rose` (standard) — **DEAD-QUERY** for any analysis of the south-westerly mode.
38. (data) Sun and twilight computed with the NOAA fractional-year declination formula (script in scratchpad); checked against the station's published day lengths.

### Item 5
39. `Wilkins aerodrome fuel storage capacity liters fuel farm IEE aviation operations 2020-2025 ground equipment snow groomer` (standard) — AAD "This week at Casey, 7 February 2014" read (drums). Wilkins storage volume **NOT FOUND (died at the sources).**
40. Wikipedia "Troll Airfield" read.
41. `ALCI Novo runway ground handling staff fuel storage Il-76 cargo offloading turnaround hours DROMLAN` (standard) — aviacionline and Volga-Dnepr press release 3669 read. Turnaround and handling at Novo: **NOT FOUND.**
42. `Union Glacier camp staff number fuel cache drums ground handling Il-76 unloading runway grooming ALE logistics season` (standard) — fourmilab.ch 2013 account: **expired certificate, DEAD-SOURCE**; Wikipedia "Union Glacier Blue-Ice Runway" read (nothing on staff or fuel).
43. `Operation Deep Freeze season C-17 missions passengers pounds of cargo moved Christchurch McMurdo season totals` (standard) — globalsecurity copy: **402**; pacaf.af.mil: **403**; mt-milcom.blogspot.com copy of the 2007 release read. Season totals left UNVERIFIED.
44. `C-17 Wilkins aerodrome cargo unloading metric tons per flight ground crew forklift Hagglunds Casey RAAF season` (standard) — AAD 2015, greghunt.com.au and Contact magazine read; australianaviation.com.au **403**; minister.defense.gov.au and defense.gov.au **socket hang up**.
45. `Customs Act 1901 section 58 permission international aircraft land non-proclaimed airport remote mine site Australian Border Force officers attend` (standard) — austlii **403**; the 2016 compilation on legislation.gov.au downloaded and s 58 extracted.
46. `Australian Antarctic Division cargo biosecurity inspection Hobart departing Antarctic cargo pre-departure checks returning cargo Department of Agriculture` (standard) — AAD cargo "Biosecurity" page and "Supply Chain and Cargo Operations" page read; the returning-cargo sentence was not on either (UNVERIFIED).
47. `remote mine airport international cargo flight customs officers flown in on demand clearance Canada CBSA northern mine airport direct international charter` (standard) — Public Safety Canada briefing read. A freight-only remote airfield with its own customs post: **DEAD at the sources.**

### Item 6
48. `Boulder Clay runway Mario Zucchelli station gravel runway first landing 2022 sea ice runway alternative ENEA PNRA` (standard) — ENEA release (7 Dec 2022) and Wikipedia "Zucchelli Station" read. *Snag recorded: Wikipedia gives the first C-130J landing as 22 November 2022; the ENEA release is dated 7 December 2022 and gives no flight date; the geology file's "7 Dec 2022" landing date may be the release date.*
49. `Antarctic station two airfields wheeled runway and skiway Progress Zenit runway Vostok Novo Neumayer second landing site purpose` (standard) — McMurdo consolidation reports found as search text only; Antarctic Sun **DNS failure** (two hostnames tried); openpolar **certificate error**. Russian and German stations' second fields: **DEAD-QUERY.**

