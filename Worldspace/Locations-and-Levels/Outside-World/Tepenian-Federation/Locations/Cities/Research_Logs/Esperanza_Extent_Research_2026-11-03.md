# Esperanza: ice speed, footprint and the Ulu Peninsula (research log, 2026-11-03, evening)

**Task (developer, 2026-11-03; handoff section 6):** real-world research on Esperanza's extent: (1) ice speed near Hope Bay and Tabarin, read directly from a velocity dataset; (2) the footprint; (3) whether the Ulu Peninsula has any role. Done in the evening (research is allowed after 15:00). **No existing file was edited by this research, and nothing here is a ruling.** Population stays 1,200,000 (Census I) and 753,159 (Census II) per `DR-90`. The rule that governs the use of the ice: *cities may stand on ice; only ice speed matters; no speed threshold has been set* (developer, 2026-10-04). So no threshold is applied below; the tables show what each threshold would give.

## 1 · Results in plain language
1. **Ice speed was found, which the 2026-11-01 research could not do.** The velocity dataset was read directly (ITS_LIVE annual-composite mosaic, 120 m cells, built from satellite feature tracking, period 2014–2022). **The ice around Esperanza moves slowly.** Within 10 km of the base the median speed of grounded ice is **16.5 m/yr**; within 20 km **16.7 m/yr**; over the Tabarin ice **13–14 m/yr**; at the head of Hope Bay (the Depot Glacier zone) **9.9 m/yr**. 94% of the Tabarin ice moves under 50 m/yr. For scale, 16 m/yr is 1.6 km per century. The fast ice (100 m/yr and more, up to several hundred) is in glacier outlets, about 12% of the ice within 10 km of the base and 2% of the Tabarin ice.
2. **Read this with the error in view.** The mosaic's own stated error for these cells is **23–41 m/yr, larger than the median speed**. Speed can only be positive, so noise pushes the slow-ice figures up. The honest reading is *"slow: tens of metres a year at most, probably less"*, not "16.5 m/yr exactly". A newer processing (version 2.1, 2014–2024) agrees: medians within 0.3 m/yr, per-cell median difference 1.7 m/yr. The long-term trend 2014–2022 is about zero (median −0.2 to −0.3 m/yr per year, inside the noise) and the seasonal swing is about 14–17 m/yr (same size as the speed).
3. **Footprint.** 1,200,000 people at 7,000–10,000 per km² need **120–171 km²** (Census II: 75–108 km²). The real Esperanza Base occupies about 0.37 ha. Hope Bay's own ice-free ground is about 4 km² (2026-11-01 log), 2–3% of the need. The grounded ice within 10 km of the base is 151 km²; within 20 km, 589 km²; over the Tabarin region (my definition, section 3), **428 km²**. How much of it passes a test depends on the speed ceiling the developer chooses (table in section 4): with speed under 20 m/yr and slope under 6°, **162 km² on Tabarin** (about the upper end of the need); with speed under 50 m/yr and slope under 6°, **258 km²** (1.5–2.2 times the need). Within 10 km of the base alone, only 46 km² passes the first test, so the city cannot be a compact core on Hope Bay; it has to run south over the Tabarin ice.
4. **Thickness (extra, beyond the speed rule).** The Tabarin ice is thin: median **107 m**, none thicker than about 250 m, 16% under 50 m. Near the base: median 115 m. This is Bedmap3 at 500 m; its uncertainty layer was not read.
5. **The Ulu Peninsula is a second site, not a bridgehead.** It has about 250 km² of ice-free ground (more than the whole need on paper) but it is across Prince Gustav Channel: from the ice data, the **narrowest gap between the two grounded-ice masks is 9.4 km at 63.93°S 58.27°W** (the channel is 8–24 km wide per the sources), and that crossing is far south; **from Esperanza Base the nearest James Ross Island ice is 73.9 km away**. No facts here decide whether it has a role; the decision is the developer's.

## 2 · Method and sources (what was actually read)
**Direct data (read by program, in a private environment in the scratchpad; scripts saved beside this file in `Esperanza_Extent_Scripts_2026-11-03/`):**
- **ITS_LIVE velocity mosaic, version 2, static, region RGI19A (Antarctica), 120 m, polar stereographic (EPSG:3031):** cloud-optimized GeoTIFFs `…RGI19A_0000_v02_{v, v_error, count, landice, floatingice, v_amp, dv_dt}.tif` at `its-live-data.s3.amazonaws.com/velocity_mosaic/v2/static/cog/`, read as a 120 km × 120 km window centered on 63.50°S 57.0°W by HTTP range requests. The mask `landice` marks grounded ice (value 1); `floatingice` is empty in this window (no ice shelf). The `dv_dt` layer's own tag says it is the trend 2014–2022. **Also** the version 2.1 static `v` layer (2014–2024) as a version check.
- **REMA (Reference Elevation Model of Antarctica) version 2.0, 32 m tiles**, public AWS bucket `pgc-opendata-dems`, read as a 60 km window averaged to 60 m; slope computed from it (smoothed by the averaging).
- **Bedmap3 `bm3_thickness.tif`** (British Antarctic Survey, CC-BY, 500 m, 361 MB; downloaded into its own folder, read in isolated mode).
- The **Hope Bay Esperanza Base point** (63°23.9′S 56°59.8′W) is from my own recall of the base position, **not** from the pages fetched (those gave 63°23′S 56°59′W for the bay, 1′ precision). The 1′ difference is about 1.6 km and does not change the 10 km and 20 km results materially.

**Web (all standard searches unless noted; exact strings are in section 6):** Wikipedia pages for Tabarin Peninsula, Hope Bay, Duse Bay and Ulu Peninsula (coordinates, shape, bounds); search summaries for Ulu Peninsula (channel width, 250 km² ice-free), Bedmap3 (files), REMA (bucket), Esperanza Base (size and population), South Pole Station and Halley VI (what a station on moving ice experiences), Depot Glacier accumulation (1956–60).

## 3 · Geography as found (sources partly disagree; the data settled it)
- **Esperanza Base** is at the head of Hope Bay on the north coast of the Trinity Peninsula tip; Mount Taylor (about 1,000 m), Mount Flora (520 m) and Blade Ridge stand west of the bay. **Tabarin Peninsula** (centre 63°32′S 57°00′W; 28 km × 9.3–22.2 km; average height about 250 m) is bounded by Hope Bay on the north, Duse Bay (63.53°S 57.25°W, which opens west onto Prince Gustav Channel) on the south and west, and Antarctic Sound on the east; an isthmus about 12 km wide joins it to the mainland.
- **A conflict in the sources:** the 2026-11-01 log, one search result and one page say Tabarin "lies south of the trough between Hope Bay and Duse Bay"; the Wikipedia Tabarin page says Hope Bay is at its north end. The velocity and terrain data show continuous grounded ice starting immediately south of the head of Hope Bay and running south to about 63.65°S along 57°W. **I used the data.** My working region, "Tabarin region", is the box 63.41–63.66°S, 57.17–56.55°W (a hand-defined box, not an official boundary; its grounded ice totals 428 km²).
- **Maps** (median grounded-ice speed and elevation, the 120 km window) are reproduced by `map2.py`; the fast cells (100–400 m/yr) are glacier outlets on the west side of the window and on the east coast, not the broad ice cap.

## 4 · Tables
**Speed of the grounded ice (m/yr) by zone** (ITS_LIVE v2, 120 m; "stated error" is the dataset's own):
| Zone | Grounded ice | Median | 25th–75th | <10 | <20 | <50 | ≥100 | Stated error (median) |
|---|--:|--:|---|--:|--:|--:|--:|--:|
| within 10 km of Esperanza | 151 km² | 16.5 | 5.3–41.9 | 35% | 57% | 78% | 12% | 35 |
| within 20 km | 589 km² | 16.7 | 6.7–33.7 | 34% | 57% | 84% | 6% | 39 |
| head of Hope Bay (Depot Glacier zone, 63.40–63.46°S) | 61 km² | 9.9 | 2.4–19.2 | 50% | 77% | 99% | 0% | 41 |
| Tabarin ice, central (63.46–63.60°S) | 225 km² | 14.3 | 5.9–26.0 | 38% | 64% | 95% | 1% | 23 |
| Tabarin box used first (63.40–63.66°S, 57.30–56.70°W) | 447 km² | 13.3 | 5.2–24.7 | 41% | 66% | 94% | 2% | 23 |

**Area (km²) of Tabarin-region grounded ice (428 km² in all) by speed and surface slope** (REMA, 60 m):
| Speed \ slope | <3° | 3–6° | 6–10° | ≥10° | total |
|---|--:|--:|--:|--:|--:|
| <10 m/yr | 28.1 | 49.4 | 41.8 | 60.7 | 180.0 |
| 10–20 | 42.2 | 42.8 | 18.2 | 11.5 | 114.7 |
| 20–50 | 46.5 | 49.4 | 13.8 | 4.3 | 113.9 |
| ≥50 | 9.7 | 5.9 | 2.9 | 0.9 | 19.5 |
Cumulative: speed <20 and slope <6°: **162.5 km²**; speed <20 and slope <10°: 222.5; speed <50 and slope <6°: **258.3**; speed <50 and slope <10°: 332.1; any speed, slope <6°: 273.9. Elevation of the Tabarin ice: median 265 m (10th–90th 62–435). The same tables for the zones within 10 km and 20 km of the base are in the script output (within 10 km: speed <20 and slope <6°: 45.8 km²; speed <50 and slope <6°: 71.2 km²; within 20 km: 210.5 and 350.8).

**Ice thickness (Bedmap3, 500 m):** Tabarin region: median 107 m, 90th percentile 183 m, maximum 247 m; 0–50 m 63 km² (16%), 50–100 m 113 km² (28%), 100–200 m 208 km² (52%), 200–400 m 15 km² (4%). Within 10 km of the base: median 115 m, 15% under 50 m. Of the Tabarin ice that is both slow (<20 m/yr) and gentle (<6°): 154 km², median thickness 114 m, 15 km² under 50 m.

**Real stations on moving ice, for scale (search summaries, not verified at the sources):** Amundsen–Scott South Pole Station drifts with the ice at about 10 m/yr (9.98 ± 0.01 m/yr in one measurement); Halley VI sits on an ice shelf moving about 400–500 m/yr and was relocated 15 km (or 14 miles; the sources disagree) in 2016–2017 because of a crack. The Tabarin ice at 13–17 m/yr is the same order as the South Pole's.

**Esperanza Base today (Wikipedia and a Spanish-language source via search, which disagree on the population):** urban area 0.3744 ha; 43 buildings; 10 families and 2 teachers (56 winter inhabitants; other sources say 55, 60 or 80); school with 12 children (2026); civilian families since 18 February 1978. Climate: about 726 mm/yr precipitation (mixed 1961–1990 and 1991–2020 data) and about 178 snowy days. Depot Glacier accumulation 1956–1960: 47.2, 57.0, 65.0 and 48.4 cm water equivalent per year; the glacier was judged near equilibrium (Koerner, via search summary). A Landsat study 1988–2015 reported the north tip of Trinity Peninsula losing about 40 km² of ice cover (about 2.7% of the study area) (search summary, not checked against the paper).

## 5 · Limits and things I did not do
- **Speed is a noisy, 8-year average of the surface** (2014–2022), not the base of the ice, and not a forecast. Years before 2014 exist in the annual mosaics (1984–2013) but were not read; they would show whether speed has changed.
- **No dataset check outside ITS_LIVE.** The MEaSUREs velocity maps (NSIDC, need a login) and the ESA/ENVEO Sentinel-1 maps were not read; the literature searches found no published speed for Hope Bay, Mott Snowfield, Depot or Mondor glaciers (see dead ends). The version 2.1 comparison is a processing-version check, not an independent measurement.
- **Not examined:** crevassing and ice-front hazards (Depot Glacier ends in a high ice cliff at the bay's head), the bedrock under the ice (Bedmap3 bed; thin ice means rock close to the surface in places), wind and drifting snow, Bedmap3's uncertainty layer, the sea route and port, and the sea-ice. The slope figures use a smoothed 60 m surface.
- **The landice mask** comes with the ITS_LIVE product; its original source was not traced.
- **Ulu ice-free area (about 250 km²)** is from Jennings et al. 2021 as reported in the 2026-11-01 log and in this session's search summary; I did not open the paper. Hope Bay's 4 km² of ice-free ground is from the 2026-11-01 log (Poeiras et al. 2026), also not re-opened.
- The earlier, approximate Tabarin box and the refined region overlap but differ in area (447 and 428 km²); the tables say which was used.

## 6 · Search log (exact strings; 13 web searches and 7 page fetches; every one logged)
Web searches (WebSearch, mode standard):
1. `Hope Bay Trinity Peninsula Antarctic ice velocity glacier flow speed` → no velocity for Hope Bay; 1958–60 Koerner movement studies (Depot, Victory, Russell East); a west-coast Sentinel-1 study not applicable. **Dead end at the sources.**
2. `Mott Snowfield Trinity Peninsula ice thickness radar velocity` → location only. **Dead end at the sources.**
3. `Tabarin Peninsula Depot Glacier Mondor Glacier Duse Bay glacier velocity retreat` → retreat only (one blog: Mondor terminus 400 m, 1988–2017). **Dead end for speed, at the sources.**
4. `ITS_LIVE Antarctic Peninsula annual velocity mosaic Trinity Peninsula` → product documentation only; led to the bucket that was then read directly.
5. `Bedmap3 ice thickness Antarctic Peninsula Trinity Peninsula download GeoTIFF` → dataset paper and record; led to the BAS record.
6. `Seehaus Wuite Antarctic Peninsula ice velocity Prince Gustav Channel Trinity Peninsula east coast glaciers speed Sentinel-1 TerraSAR-X` → general Peninsula work; nothing for the east coast of Trinity Peninsula. **Dead end at the sources.**
7. `Ulu Peninsula James Ross Island ice-free area Prince Gustav Channel distance Tabarin Peninsula Hope Bay` → channel 8–24 km wide; about 250 km² ice-free; no distance given.
8. `REMA Reference Elevation Model of Antarctica 100 m mosaic cloud optimized GeoTIFF AWS open data bucket` → bucket `pgc-opendata-dems`; the 100 m file did not exist at the path guessed (the bucket holds 2 m, 10 m and 32 m); 32 m tiles read instead.
9. `Esperanza Base Hope Bay Argentina families school buildings area hectares permanent settlement Fortín Sargento Cabral` → 0.3744 ha; 43 buildings; families; school; population figures conflict.
10. `Amundsen-Scott South Pole Station ice flow meters per year station moves with the ice` → about 10 m/yr.
11. `Halley VI research station Brunt Ice Shelf ice flow metres per year relocation skis` → 400–500 m/yr; relocated in 2016–17.
12. `Hope Bay Antarctic Peninsula Buenos Aires Kenney Flora glacier fronts 1988 2008 2017 retreat area` → front mapping paper (Costa et al. 2019); no distances in the summary.
13. `Trinity Peninsula ice cap accumulation snowfall rate Hope Bay Esperanza snow depth annual precipitation` → station precipitation; 1956–60 Depot Glacier accumulation.

Page fetches (WebFetch): `en.wikipedia.org/wiki/Tabarin_Peninsula` (read); `…/Hope_Bay,_Antarctica` (read); `…/Depot_Glacier` (**disambiguation page only: dead end**); `…/Ulu_Peninsula` (coordinates 63°56′S 58°5′W; no width); `…/Duse_Bay` (63.533°S 57.250°W; opens onto the channel); `doi.org/10.5285/2d0e4791-8e20-46a3-80e4-f5f6716025d2` (redirect) then `data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01615` (file list).
Direct HTTP/data (no search count): listing of the ITS_LIVE bucket and its v2 and v2.1 mosaic catalogs; the seven COG layers and the v2.1 layer; the PGC REMA bucket and 32 m tile index; the BAS Bedmap3 thickness file.
**Where each dead end died:** searches 1, 2, 3, 6 died at the sources (no published speeds exist in what the search returned), which is why the dataset was read directly.

## 7 · What the developer may want to decide (none made here)
1. **Whether to set a speed ceiling.** The data say about half of the ice within 20 km of the base is under 20 m/yr and 84% is under 50 m/yr.
2. **How to declare the extent.** The need (120–171 km²) fits the Tabarin region at a ceiling of 20–50 m/yr with gentle slope, but not within 10 km of the base. Held for this declaration: the extent row and the Esperanza figures noted in the 2026-11-01 log (education lines and Marambio L58 were already edited under `DR-90`).
3. **Whether the Ulu Peninsula plays a role,** now that it is known to be 74 km from the base, across a channel 8–24 km wide, with a narrowest gap far to the south.
4. **Whether to read more:** pre-2014 speeds, the bed and uncertainty layers, crevasse and ice-front hazards.
