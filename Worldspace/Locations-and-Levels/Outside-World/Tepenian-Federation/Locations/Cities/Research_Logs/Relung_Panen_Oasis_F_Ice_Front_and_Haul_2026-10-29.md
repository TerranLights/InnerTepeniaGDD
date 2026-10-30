# Relung Panen oasis, Unit F: the ice-front landing and the shelf haul (real-world research, 2026-10-29)

**Brief:** `Relung_Panen_Oasis_Airports_and_Haul_Research_BRIEF_2026-10-29.md`, Unit F. **Real world only. No design of any fictional landing or haul. No recommendation.** Every claim is marked SOURCED, UNVERIFIED, DERIVED or NOT FOUND.

## PROGRESS
- [x] 1 The Shackleton Ice Shelf front near the Bunger Hills (freeboard, low or ramped places, Scott Glacier and Mill Island corner, front position over time, shelf surface front-to-oasis, ground or ship surveys)
- [x] 2 Overland traverses on ice-shelf margins and crevassed ground
- [x] 3 Satellite and survey data along the corridor (crevasse map, ITS_LIVE, REMA, accumulation and melt; DERIVED)
- [x] 4 Ice-front landing gaps left by port file D
- [x] 5 Ship-to-oasis by helicopter as the real fallback (sorties, payload, hours; DERIVED sortie count)
- [x] FINAL

STARTED 2026-10-29.

**Spelling:** quoted source text is put into American spelling (meters, liters, tons, sled), as in port file D; search strings in the logs are left exactly as typed. Tons in quotes are metric tons.

**Labels.** **SOURCED** = read in the cited page, PDF or dataset documentation. **UNVERIFIED** = seen only in a search-result summary, a page that could not be opened, or a source with a known weakness. **DERIVED** = computed in this session from a named public dataset or from SOURCED numbers; method and inputs are given. **NOT FOUND** = looked for; the search log says where.

**Not repeated here (already in the files the brief lists):** the shelf's size, thickness, 1962-2022 advance, C-39, the Scott calving since 2020, the sea-ice and open-water statistics off the front, the ETOPO surface heights, the 1912 Western Base cliff heights (port file A); the Casey/Mirny/Davis distances, Denman crossing history and the long inland traverses with their fuel figures (port file C); every recorded access to the oasis, the 1979 and 2022 helicopter legs and the 2019 Russian airfield survey (port file B); the ~20 ice-front unloading precedents, McMurdo ice pier, Gold's formula (port file D); sea state, tides, fast-ice thickness elsewhere, icebergs (ocean files); ship helicopter types and limits (intake file D).

**Data notes for the DERIVED work in sections 1 and 3 (method in full in section 3.1).** Surface heights come from **REMA v2.0 32 m mosaic** (Polar Geospatial Center; tiles 25_56, 25_57, 26_56, 26_57; built from WorldView stereo strips dated 2011-09-24 to 2020-02-17), converted from WGS84 ellipsoidal height to **EGM2008 orthometric height** (geoid offset N = −2.1 to −3.4 m here, from PROJ's EGM2008 grid). Ice speed and the floating-ice mask come from **ITS_LIVE v2 120 m static mosaic** (NASA MEaSUREs; climatology 2014-2022, time intercept 1 Jan 2018). Fractures come from the **Surawy-Stepney and Hogg (2023) June 2021 composite fracture map**, 100 m (Zenodo 10.5281/zenodo.8296992; score D from 0 = no fracture to 1 = fracture). Coastline, front and grounding lines come from the **SCAR ADD high-resolution coastline polylines** (BAS ArcGIS service, version current in October 2026). **The REMA mosaic is a composite of different dates; it is not a snapshot.** Heights over water near 0 m are a check on the datum, not proof of a sea surface: mean dynamic topography around Antarctica puts the real sea surface roughly 1-2 m below the geoid (general fact, UNVERIFIED for this coast).

---

## 1. The Shackleton Ice Shelf front near the Bunger Hills

### 1.1 Freeboard (cliff height) along the front: what REMA shows (DERIVED)

**Method.** For every point at 2 km spacing along each ADD "ice shelf and front" line inside 99.8-102.3°E, 65.55-66.4°S, a 16 km line was drawn toward the nearest oasis rock coastline, centered on the ADD front point. Walking from the sea side, the first REMA pixel above 8 m whose following 1 km also has a median above 8 m was taken as the REMA cliff. Heights are medians of five 32 m pixels at 250 m, 500 m, 1 km and 2 km inside that step. "Sea side" is the median of the 1 km before the step. The date is REMA's `maxdate` at the 250 m sample (the newest strip used there). Script: `scripts/front.py` in the session scratchpad.

| Front sector (ADD line, its date) | Sample points | REMA cliff vs ADD line | Sea-side surface | Height 250 m inside | 1 km inside | 2 km inside | REMA date at the cliff |
|---|---|---|---|---|---|---|---|
| **Scott Glacier / Mill Island corner, western open-sea front** (ADD feature 29096, Sentinel-1 2 May 2022), 100.27-100.33°E, 65.72-65.77°S | 7 | **3.8-6.8 km landward of the 2022 line** | −0.2 to +0.1 m (water or thin sea ice) | **17-24 m** | **22-29 m** | 24-29 m | 2018-10-03 to 2020-02-17 |
| Same line, 100.17-100.21°E, 65.75°S (west of the corner) | 2 | 5.5-6.6 km landward | ≈0.1 m | **≈51 m** | ≈51 m | ≈51-53 m | 2019-08-29 |
| Same line, 100.33-100.34°E, 65.68-65.69°S (rising onto Mill Island) | 2 | 5.9-7.8 km landward | ≈0 m | ≈44 m | ≈67 m | ≈78-79 m | 2019-08-29 |
| North of Mill Island (feature 29109, Sentinel-1 6 Jun 2016), 100.26-100.27°E, 65.57-65.60°S (only the south end lies in the sampled box) | 3 | −0.03 to +0.22 km (matches) | ≈−0.1 m | **19-20 m** | 33-37 m | 48-60 m (Mill Island dome) | 2019-08-29 |
| **Eastern front** (feature 29111, Sentinel-1 6 Jun 2016), 101.27-101.70°E, 65.55-65.66°S | 14 | −7.6 to +1.6 km (13 of 14 within 0.2-1.6 km seaward) | ≈0 m in 7 points; **5-6 m in 7 points** | **6-13 m** (one point 25 m) | mostly 10-17 m | mostly 11-20 m | 2017-08-28 to 2019-08-26 |
| Eastern front, 101.79-101.85°E, 65.76-65.78°S | 2 | 1.2-5.9 km seaward | ≈0.1 m | 27-41 m | 6-16 m | 5-6 m | 2019-03-12 |
| Eastern front, 102.22-102.29°E, 65.83-65.85°S | 3 | 0-2 km seaward | ≈0 m | 8-19 m | 6-17 m | 4-20 m | 2017-08-28, 2019-08-29 |
| Eastern front, 101.88-102.20°E, 101.81°E and 101.73-101.77°E | 16 | **no step above 8 m found within 8 km of the ADD line** | — | — | — | — | — |
| Inner fronts facing the oasis's own enclosed marine water (ADD Landsat-7 lines of 6 Feb 2000, 66.0-66.3°S) | 12 | — | ≈1.1-1.2 m (sea-ice level) | **8-14 m** (one point 25 m) | 7-13 m | 9-16 m | 2018-05-15 to 2019-02-09 |

**What this shows (DERIVED, with the caveats below):**
- **At the western corner nearest the oasis, the shelf surface stands about 17-29 m above the geoid within the first kilometer.** That brackets the 27-34 m ETOPO figure in port file A from below and agrees with it at 1-2 km in. It also falls inside the 18-30 m that Mawson's party saw at 95°E in 1912 (port file A).
- **REMA's cliff at the corner sits 3.8-6.8 km behind the ADD May 2022 line.** REMA's strips there are dated October 2018 to February 2020. Scott Glacier's front moved at 2-4 m/day (0.7-1.5 km/yr) in 2020-22 (port file A, Thompson et al. 2023), so 2.2-3.6 years of advance gives about 1.6-5.3 km (DERIVED). The offset is therefore consistent with the front advancing between the REMA strip dates and the 2022 line, and **the cliff position at any one place shifts by kilometers in a few years**.
- **The eastern "front" is low or absent.** Where REMA finds a step at all, the surface 250 m inside is 6-13 m. In 16 of 35 eastern sample points there was no surface above 8 m within 8 km of the ADD line. Section 3.3 shows why: much of what the ADD maps as ice shelf on the eastern side reads at sea-ice level.
- **Where the shelf meets the oasis's own enclosed marine water, its edge stands about 8-14 m above a surface at about 1 m** (that surface is the oasis's fast ice).

**Caveats.** REMA is a stereo-photogrammetric surface model that mixes strips of different dates; cliff faces themselves are poorly resolved at 32 m, so the step location carries about ±100 m of uncertainty, and a vertical face cannot be distinguished from a steep slope. The 8 m threshold misses any cliff lower than 8 m. Firn, snowdrifts and sastrugi are included in the surface. **No published measured freeboard (from a ship, a survey or a field team) at this front was found: NOT FOUND** (searched; see the log). The laser-altimeter check below is this session's own derivation.

### 1.1b Freeboard measured by the ICESat-2 laser altimeter, 2023-2025 (DERIVED)

**Method.** ICESat-2 ATL06-style land-ice heights were computed on demand by the public **SlideRule Earth** service (`slideruleearth.io`, client `sliderule` 5.8.0, `icesat2.atl06p`, land-ice surface type, confidence 4, 40 m segments every 20 m) over 100.05-100.55°E, 65.62-65.86°S for 1 Jan 2023 to 31 Dec 2025 (143,562 segments, 27 months with data). Heights converted to EGM2008. A front crossing = five consecutive segments below 3 m next to five above 10 m with no gap over 200 m. Script: `scripts/is2.py`, `scripts/is2_an.py`. 35 crossings were found on two repeat ground tracks (RGT 476 and 682).

| Date (track) | Position of the step | Water or sea-ice surface beside the cliff | Ice surface 0-250 m in | 250-500 m in | Step (ice minus water side) |
|---|---|---|---|---|---|
| 5 May 2023, 3 Aug 2023, 29 Jan 2025 (RGT 682, beam 50/60) | ≈65.765°S 100.308-100.309°E (≈0.9 km from the ADD 2022 corner point) | −1.1 to 0.0 m | **28.2-29.4 m** | 29.6-30.4 m | **≈29-30 m** |
| 3 Aug 2023 to 1 Feb 2024 (RGT 682, beams 30/40) | 65.732-65.738°S 100.226-100.229°E | −1.0 to −0.8 m | **31.2-33.0 m** | 34.8-37.0 m | ≈32-34 m |
| 19 Jan 2024 to 15 Oct 2025 (RGT 476) | 65.742-65.754°S 100.091-100.095°E | −1.4 to −0.5 m | 27.3-31.9 m | 26.4-36.7 m | ≈28-33 m |
| 18 Apr 2024 to 15 Oct 2025 (RGT 476, beams 10-40) | **65.772-65.790°S** 100.156-100.235°E | −1.1 to +0.1 m | **23.3-35.7 m** | 28.6-33.8 m | ≈24-36 m |
| 3 Aug 2023 (RGT 682, beam 20) | 65.743°S 100.156°E | −0.8 m | 36.8 m | 37.6 m | ≈38 m |

**What this shows (DERIVED):**
- **In 2023-2025 the ice cliff at the western corner stood about 23-37 m above the surface beside it, most often 28-33 m.** The water or sea-ice surface next to the cliff reads −1.4 to +0.1 m on EGM2008, which matches the expected 1-2 m mean dynamic topography below the geoid, so the step heights are the best available measure of freeboard above the local sea surface.
- **The front near 100.16-100.24°E sat at 65.772-65.790°S from April 2024 to October 2025**, i.e. up to 2 km south of the ADD May 2022 corner latitude (65.770°S). That is consistent with the March 2024 break-off reported by PS141 (section 1.3).
- These agree with REMA (section 1.1) within a few meters.
- **Caveats:** ATL06-style fits over a cliff smooth the face over 40 m; the cliff top can be a few meters higher than the 0-250 m median. Two ground tracks sample only a few kilometers of front. Heights include firn and snow.

### 1.2 Low or ramped places on the front

- **NOT FOUND:** any source describing a ramp, snow slope or low point in the front near the Bunger Hills that a vehicle could use. Port file A noted ETOPO's 2-4 m surface on the eastern side; REMA (section 3.3) indicates that much of that surface is sea-ice level, not a low shelf edge.
- **SOURCED (Nutt 1948, *Arctic* 1(2):88, PDF read):** USS *Edisto* "penetrated the pack to a low area of shelf ice some forty miles distant from the 'Oasis'", and "a small air operating base was set up on the shelf ice". The text gives no height and no position beyond "skirted to the eastward". **This is the only eyewitness description of a low section found.**
- **DERIVED:** on the eastern sector, seven of the fourteen sample points with a step at 101.27-101.70°E have a sea-side surface of 5-6 m and a shelf 250 m inside of 8-13 m, i.e. a step of only about 3-7 m, at 101.38-101.70°E, 65.58-65.66°S (REMA dates August 2017 to August 2019). Whether the 5-6 m surface is old fast ice, a snow-covered ice foot or a drift is not resolvable from REMA alone.
- **SOURCED (AARI, *Rossiyskie Polyarnye Issledovaniya* 3(37), 2019, p. 17, read in Russian):** "Наибольшей ширины припай в море Моусона достигает в районе ледниковых бухт Миловзорова и Малыгинцев (более 100 км)" (fast ice in the Mawson Sea reaches its greatest width, more than 100 km, near the glacier bays of Milovzorov and Malygintsev). Multiyear fast ice "возвышается над однолетним на 1,5–2 метра" (stands 1.5-2 m above first-year ice), noted at 113-116°E. "Only one of the polynyas in this sea appears with 60% probability (Malygintsev Bay); the others are seen almost constantly in the navigation period."

### 1.3 The Scott Glacier and Mill Island corner

- Already known (port file A): Scott front advanced ≈0.75 km/yr in 2015-2019, sped up from 2 to 4 m/day in 2020-22, calved small pieces from 2020 on the Mill Island side and lost a >25 km section (C-39) in April 2022.
- **SOURCED (AWI, PS141 expedition report, *Berichte zur Polar- und Meeresforschung* 793, 2025, ch. 3, PDF read):** cores PS141_71 and PS141_72 were taken in March 2024 where "advantage was taken from a break in the Shackleton Ice Shelf in Glacier Ice Stream that eventually led to a break-up of an iceberg in the first half of March 2024 and allowed access to this area." The summary chapter adds that on 22 March 2024 "an area was bathymetrically surveyed at sea where a large piece of the shelf ice had broken off a few days prior." Station positions (PANGAEA event list PS141, read): PS141_71 at 65.714°S 100.153°E (540 m water), PS141_72 at 65.778°S 100.217°E (538 m), 21 March 2024.
  - **DERIVED:** PS141_72 lies 3.6 km west of, and slightly south of, the ADD May 2022 corner point (65.770°S 100.293°E); it is 55.4 km from Edgeworth David and 60.3 km from Dobrowolski. So in March 2024 a research ship worked in open water at least as close to the oasis as the 2022 corner, after a calving "a few days prior".
- **DERIVED (ITS_LIVE v2, climatology 2014-2022):** speed at the ADD 2022 corner point is ≈340 m/yr, falling to ≈200 m/yr 2-4 km inside and below 100 m/yr by 8 km inside on the line toward Edgeworth David (section 3.2, transect T1).
- **DERIVED (REMA):** just west of the corner (100.17-100.21°E) the surface is ≈51 m, roughly twice the corner's 22-29 m, consistent with thicker glacier-tongue ice; Mill Island's dome rises to ≈115 m on the transects (section 3.2, T7).

### 1.4 Position and change of the front over time (beyond port file A)

- **SOURCED / DERIVED:** the March 2024 calving above. No size or name for the March 2024 piece was found in the US National Ice Center sense (it may be below the NIC's 10 nmi naming size): **NOT FOUND**.
- **DERIVED (REMA vs ADD, section 1.1):** at the corner the REMA front (2018-2020 strips) lies 3.8-6.8 km landward of the 2022 line; north of Mill Island the 2019 REMA front and the 2016 ADD line agree to within 0.2 km.
- **Not repeated:** 1962-2022 advance of 18 km and Scott's history (port file A).

### 1.5 The shelf surface between the front and the oasis

Full numbers are in section 3; the short form (DERIVED from REMA, ITS_LIVE, the June 2021 fracture map and ADD lines, along seven straight sample lines that are **sampling lines, not routes**):

- **Western side (from the Scott/Mill corner or the PS141 ship position toward Edgeworth David, Dobrowolski or Thomas Island; 48-66 km):** 41-48 km of the line is floating shelf at ≥3 m; the surface falls smoothly from 26-34 m near the front to 6-15 m near the oasis; on the floating part, 95% of 1 km windows have less than 0.5-1.8% relief (max 1.3-2.5%); 4-17% of 100 m samples have a fracture score above 0.5; speed drops from 126-340 m/yr at the front to 10-50 m/yr over most of the line. Two lines cross an ice-covered island or ice rise classed "land" in the ADD (≈65.84-65.87°S, 100.43-100.48°E; surface 39-51 m; speed 1-5 m/yr) with three ADD grounding-line crossings. Near the oasis the lines meet 1-11 km of sea-ice-level surface (the oasis's enclosed marine water) and then rock.
- **Eastern side (from the 2016 eastern front toward Dobrowolski or Thomas Island; 54-73 km):** **51 of 54-73 km reads below 3 m**, i.e. sea-ice level, on the two lines from 101.81°E. From 101.55°E, the first 15 km is shelf at 12-22 m, then 25 km at 3-7 m, then 15 km at sea-ice level. Fracture bands (D > 0.5) cluster 27-38 km in from the eastern front, where speeds rise to 46-66 m/yr.

### 1.6 Ground or ship surveys of the front-to-oasis route

- **1948, USS *Edisto* (SOURCED, Nutt 1948):** ship at "a low area of shelf ice some forty miles distant", "a small air operating base was set up on the shelf ice", helicopters carried the party ashore. Port file B adds two Weasels set up "a small relay camp and gasoline cache" between ships and shore camp (south-pole.com, SOURCED there). **SOURCED (Gore et al. 2025, *Antarctic Science* 37:1-4, open-access PDF read via Zenodo 15816838):** surveyors Merritt and Krause "were dropped at Bunger Hills via helicopter (probably from USS Edisto) on 12 January 1948 and were retrieved on the morning of 15 January 1948"; their survey point is probably the rock cairn found on Thomas Island at 66.10597°S 100.90063°E, ≈114 m. **No record of the Weasel route, distance or surface was found: NOT FOUND** (USNI *Proceedings* Dec 1948, 403 in port file B; the Windmill Navy report was not located).
- **2017-2019, *Akademik Fedorov* (SOURCED, AARI RPR 3(37) 2019, p. 17):** RAE geology moved to the Bunger Hills in the 63rd RAE (2017/18), which "требует пребывания судна в акватории моря Моусона (конкретно — в районе бухт Малыгинцев или Миловзорова)" (requires the ship to stay in the Mawson Sea, specifically near Malygintsev or Milovzorov bays). An oceanographic section was run 12-16 January 2018 and two in 2019 (along 100°E on 27-28 January; along ≈65°25′S on 2-3 February). These are **sea** surveys; **no ground or over-ice survey of the shelf between the bays and the oasis is reported.** The 2016/17 plan to work from those bays "at a minimum distance of 90-110 km" and the actual use of Aurora Bay, 250 km away, are in port file C (Lunev et al. 2017).
- **2021-22, *Akademik Fedorov*:** fully covered in port files B and D (Malygintsev Bay, 69 km; 2 km channel at 65°40.3′S 100°11.6′E; helicopter delivery). Nothing new was found on any surface survey of the shelf.
- **New, 2024, RV *Polarstern* PS141 (SOURCED, AWI BzPM 793, read):** on 19 February 2024 "Polarstern reached the Antarctic ice shelf edge northwest of the first target in the main research area: the Bunger Oasis"; a land team of eight was flown to Thomas Island; on the night of 19-20 February "bathymetric surveys were carried out in the bay off the Bunger Oasis, where numerous glacial troughs were mapped"; a hydroacoustic profile was collected "along the edge of the shelf ice" in mid-March; the ship worked at the Scott Glacier break on 21 March. These are **sea-floor** surveys in front of the shelf. **The report gives no measurements of the shelf surface, cliff height or crevassing.**
- **DERIVED (positions from the PANGAEA PS141 event list):** the ship stood at 65.711°S 100.330°E on 19 and 29 February 2024 (CTD and radiosonde stations), which is 52.0 km from the Thomas Island camp, 61.4 km from Edgeworth David and 65.7 km from Dobrowolski.
- **Air surveys (already known):** helicopters crossed "tall cliffs and deep crevasses of the Shackleton Ice Shelf" in 2022 (port file B). The 2008 Russian helicopter reconnaissance and the 2019 GPR airfield survey were inside the oasis (port file B, intake file B).
- **NOT FOUND:** any vehicle traverse, GPR line, probe line or published route survey across the shelf between any ice front and the Bunger Hills, in English, Russian, Polish or German sources searched.

### 1.7 Item 1 search log

| # | Tool | Exact string or URL | Result | Died at |
|---|---|---|---|---|
| 1 | WebSearch (extended) | `Operation Windmill 1948 Edisto Bunger Hills weasel shelf ice relay camp crevasses shore party` | Gore et al. 2025 (Cambridge 403, but open copy on Zenodo); Wikipedia; south-pole.com; Grokipedia (not used, weak) | Hit (Zenodo copy) |
| 2 | curl | zenodo.org/records/15816838/files/source.pdf | Gore et al. 2025 read in full (4 pp.) | Hit |
| 3 | WebSearch (extended) | `"Академик Федоров" оазис Бангера 2017 шельфовый ледник Шеклтона барьер вертолет выгрузка` | glonass-iac 2015 (already in file B); AARI RPR 37 | Partial (nothing on 2017 itself) |
| 4 | curl | data.aari.ru/publicat/rpr/sources/37/RPR-37p.pdf | Read in Russian: fast ice >100 km wide at Malygintsev/Milovzorov bays; 60% polynya; 2018-19 sections | Hit |
| 5 | WebSearch (extended) | `Polarstern PS141 expedition report Bunger Hills helicopter Shackleton Ice Shelf 2024 Berichte zur Polar- und Meeresforschung` | AWI EPIC 60017 (BzPM 793, 2025) and PS140 (BzPM 790) | Hit |
| 6 | curl | epic.awi.de/id/eprint/60017/9/BzPM_793_2025.pdf; epic.awi.de/id/eprint/59815/9/BzPM_790_2024.pdf | PS141 read (summary, weather, ch. 3, 5, 6); PS140 downloaded, only the PS141-camp note used | Hit |
| 7 | curl | pangaea.de/expeditions/events/PS141 | Event list parsed (ship positions 19 Feb, 29 Feb, 21 Mar 2024) | Hit |
| 8 | WebSearch (standard) | `Gore Gibson Leishman 2020 "Human occupation, impacts and environmental management of Bunger Hills" pdf` | Abstract records only; no open copy | Sources (paywall) |
| 9 | curl | pubs.aina.ucalgary.ca/arctic/Arctic1-2-88.pdf | Nutt 1948 re-read for the "low area of shelf ice" and "air operating base" wording | Hit |
| 10 | WebSearch (standard) | `Shackleton Ice Shelf freeboard ICESat-2 ice front height meters Scott Glacier Mill Island calving front elevation` | No published freeboard; only sea-ice freeboard products | Query (no publication) → computed instead |
| 11 | curl | openaltimetry.earthdatacloud.nasa.gov `/data/icesat2/getTracks?...` | HTTP 404 (API changed) | Source |
| 12 | WebSearch (standard) | `OpenAltimetry API icesat2 atl06 endpoint parameters trackId date bounding box "openaltimetry.earthdatacloud.nasa.gov/data/api/icesat2"` | Client docs only; API noted as changed since 2023 | Query → switched to SlideRule |
| 13 | Data | SlideRule Earth `atl06p`, western corner box 2023-2025 | 143,562 segments; 35 front crossings | Hit |
| 14 | Data | PGC REMA v2.0 32 m tiles via `pgc-opendata-dems` S3 (VRT read failed through `/vsis3`, so the four tiles were downloaded over HTTPS) | Read | Hit (after one failed method) |
| 15 | Data | BAS ArcGIS `High_resolution_vector_polylines_of_the_Antarctic_coastline/FeatureServer/1` (235 lines in box) and `..._polygons_.../FeatureServer/1` (point queries) | Read | Hit |

**Self-corrections (item 1):** the first count of eastern sample points (15 of 40 with no step; 8 of 15 with a 5-6 m sea side) was wrong; recounted from the script output as 16 of 35 and 7 of 14 and corrected before ticking. The AARI-reported ship position of 20 January 2022 (65°45′S 100°47′E, from port file B) falls on shelf ice in REMA (≈24 m surface), so it is either rounded or a position inside a front indentation; it was not used to infer anything about the front.


---

## 2. Overland traverses on ice-shelf margins and crevassed ground

Port file C already holds the long-haul figures (South Pole Traverse 1,658 km and 0.24 L per delivered t·km from CRREL TR-16-4; Concordia 6 L/km and 40-50 t per Challenger; Casey-Dome C North 643 t; Zhongshan-Kunlun; Progress-Vostok; Mirny-Vostok; Wilkes-Vostok 1962; the Mirny crevasse zone ≤12 km). Port file D holds the berth-to-station hauls (Atka 15-20 km; Halley 15 km or 60 km from N9; Princess Elisabeth ≈200 km, 10-12 km/h; Troll 235 km; Kohnen 757 km) and Halley's 9.5 t sea-ice limit. **Not repeated.** Below is what this pass added.

### 2.1 The McMurdo Shear Zone crossing on the South Pole Traverse: the best-documented crossing of a crevassed ice-shelf margin

**SOURCED (P. Thur, Traverse Operations Manager, Antarctic Support Contract, "Traversing in the Antarctic", Polar Technology Conference, 5 April 2012, PDF read at sundowner.colorado.edu):**
- The route (1,030 mi) is "27- McMurdo Ice Shelf · 621- Ross Ice Shelf · 88- Leverett Glacier · 296- Polar Plateau" (miles).
- "CRREL and John Wright's team spent the summer of '02 – '03 remediating the 3.5 mile trail across the Shear Zone (same trail in-use today, ~40 crevasses)." "CRREL assists on initial GPR survey assessment each year." "**Blasting and filling of 2 to 3 crevasses each year is required prior to crossing.**"
- Ice motion under the trail: "McMurdo Ice Shelf side moves ~2.3'/day (1.45 mi downstream in 9 yrs)"; "Ross Ice Shelf (RIS) side moves ~3.75'/day (2.37 mi downstream)"; "Trail length has increased by 0.31 mi"; "Eventual requirement to move back upstream".
  - **DERIVED:** 3.5 mi = 5.6 km; 2.3 ft/day ≈ 256 m/yr and 3.75 ft/day ≈ 417 m/yr; 1.45 mi ≈ 2.3 km and 2.37 mi ≈ 3.8 km; +0.31 mi ≈ 0.5 km.
- Speeds: "Traverse w/GPR travels at 7 mph maximum"; "Heavily loaded traverse w/o GPR travels ~8 – 10 mph"; "10 mph is maximum even for lighter Northbound traverses to minimize wear-and-tear on sleds, equipment, and personnel." **DERIVED:** 11.3 km/h with GPR; 12.9-16.1 km/h without.
- Fleet per traverse: "4 Caterpillar and 4 Case agricultural tractors, 1 snow-grooming type vehicle used for crevasse detection using GPR, and 2 generators". Fuel "~28 gallons per mile" for the whole train (**DERIVED ≈66 L/km**); Case "3.46 gpm heavily loaded / 2.26 gpm lightly loaded", "~25,000 to ~29,000 lbs drawbar pull"; Caterpillar "2.95 gpm heavily loaded / 1.94 gpm lightly loaded"; "Pisten Bully 100- ~1 gpm"; "Prinoth BR350- ~1 gpm". **DERIVED:** Case 8.1 / 5.3 L/km, Caterpillar 6.9 / 4.6 L/km, PistenBully 100 or Prinoth BR350 ≈2.4 L/km.
- Season "Oct. 25 to Feb. 10 … ~110 days"; planned round trip "~58 days (30 days Southbound, 7 days turn-around, 21 days Northbound)"; 2012-13 actuals 57 and 55 days.
- Crew per traverse: 10 (first) or 8 (second), including "1 x Mountaineer" on the first.
- Containers and tanks: the program moved from "Steel fuel tanks → plastic sleds and flexible transport bladders" and from "Steel skis under buildings → platforms with an air-cushion ride". Problems: "High molecular weight polyethylene (HMW) sleds- experienced breakages of plastic sheets in the field during each traverse"; "Fuel bladder reliability"; off-the-shelf pontoons "seams failed after 100 miles"; a custom pontoon system then ran "1,600+ miles … no failures".
- Other route sections: "Leverett Glacier … Gradual climb with no major crevassed areas"; "Some areas require shuttling of loads (~10% grade headwall and regions of scouring/reduced traction)"; "RIS swamp- several hundred miles of soft snow that can cause immobilizations (6" – 12" ruts)"; "Dornick region- … sastrugi … extremely rough on equipment".
- Season results (table on p. 17; DERIVED conversions):

| Season | Delivered (fuel + cargo) | Traverse fuel burned | Delivered per unit burned (as stated) | DERIVED L burned per delivered t·km (one-way 1,658 km) |
|---|---|---|---|---|
| 2005-06 | 218,465 lb ≈ 99 t | 27,273 gal ≈ 103 kL | 1.14 | 0.63 |
| 2007-08 | 56,343 lb ≈ 26 t | 39,033 gal ≈ 148 kL | 0.21 | 3.49 |
| 2008-09 | 933,745 lb ≈ 424 t | 72,212 gal ≈ 273 kL | 1.85 | 0.39 |
| 2009-10 | 701,750 lb ≈ 318 t | 62,271 gal ≈ 236 kL | 1.61 | 0.45 |
| 2010-11 | 667,240 lb ≈ 303 t | 60,881 gal ≈ 230 kL | 1.57 | 0.46 |
| 2011-12 SPoT 1 | 412,786 lb ≈ 187 t | 69,629 gal ≈ 264 kL | 0.85 | 0.85 |
| 2011-12 SPoT 2 | 643,231 lb ≈ 292 t | 38,761 gal ≈ 147 kL | 2.37 | 0.30 |

  The burned fuel is the season's round-trip consumption, so the DERIVED column is "all fuel burned ÷ (metric tons delivered × one-way distance)". It is higher than port file C's 0.24 L/t·km, which counts only tractor fuel at steady state.

**SOURCED (Marsh et al. 2021, *Cold Regions Sci. Tech.* 187:103284, PDF read):** the McMurdo Shear Zone "forms part of the South Pole Traverse Route and where crevasse bridges are opened with explosives"; snow bridges there are "several meters to over 10 m" thick; "an approximately 6 m thick snow bridge covering a crevasse 8 m wide" was imaged; GPR "is used as a standard procedure by the US, UK and NZ Antarctic programs (among others) for identifying upcoming hazards during snowmobile and heavy vehicle traverses", but "requires constant monitoring".

**UNVERIFIED (search-result summaries; sources not opened or refused):**
- Delaney and Arcone, *IEEE Trans. Geosci. Remote Sens.*, Dec 2005, "Crevasse detection with GPR across the Ross Ice Shelf": 400 MHz antenna on a 6.5 m boom pushed ahead of a tracked vehicle at 4.8-11.3 km/h; "thirty-two crevasses" along the 4.8 km crossing; mitigation by hot-water drilling, dynamite demolition of snow bridges and backfilling.
- A Dartmouth-linked account: the operator has "about two seconds to stop the tractor".
- Zamora et al. (Chile and Antarctica): radar on a 7 m rod ahead of a tractor convoy at ≈2 m/s; reaction ≈5 s or ≈10 m; detection depth to 15 m.
- Kaluzienski et al. 2019 (*J. Glaciol.*, Cloudflare block): the SPoT crossing has advected ≈4 km (west edge) and ≈6 km (east edge) since 2002; USAP's remediation rule is a snow-bridge-to-width ratio below 1.
- An Antarctic Sun article: removing a snow bridge with dynamite and refilling takes "about 4 to 8 hours" (page not reachable: DNS failure).

**Failures on this crossing (SOURCED, southpolestation.com "The Demise of Linda", quoting the *Antarctic Journal*):** on 21 November 1990 an LGP D-8 bulldozer, "a 41,000-kilogram (90,000-pound) bulldozer", fell "15 meters (50 feet) down into the crevasse" in the Shear Zone ≈27 mi (44 km) from McMurdo, "Traveling over an area used previously by D-8s"; "its blade halted its descent"; the two drivers were hoisted out after more than three hours with minor frostbite; about two weeks went into retrieving the dynamite it towed; the vehicle was never recovered. The crevasse was hidden by a snow bridge with no visible surface relief.

**SOURCED (NASA Earth Observatory, "Out of the Crevasse Field", 30 Aug 2005):** during the 2004-05 SPoT proof-of-concept, a crevasse field stalled the train near the base of the Transantarctic Mountains in December 2004; satellite-derived waypoints were sent to the team; heavy vehicles "mount GPR on long front booms and move slowly enough to stop"; at night radar surveyed "a 200-foot-diameter circle around camp"; a crevasse "Mongo" had a snow bridge "thick enough to support a person" but not "a heavy vehicle"; CRREL's Blaisdell: "you cannot assume that if the satellite doesn't see a crevasse, there won't be one." **SOURCED (Wikipedia, "South Pole Traverse"):** in December 2010 a train "got bogged down in a massive snow storm", needing several days to dig out.

### 2.2 Grounding ("hinge") zones and ice-shelf margins: failures on record

- **SOURCED (Z-fids, Halley Bay 1972 page):** an International Harvester tractor ("Paul") "had fallen into a crevasse in the hinge zone in 1969, while part of a tractor-based field trip to the mountains"; it was abandoned, and in October 1972 four men winched it out by hand because "It was too dangerous to take another big tractor to the site". It ran again after a new battery.
- **SOURCED (Z-fids, Halley Bay 1965 page):** on 12 October 1965 three men died in a crevasse accident at 74°22′S 13°14′W on a trip toward the Vestfjella; the page gives no vehicle type or ice setting.
- **SOURCED (AAD magazine issue 6, 2004, "AMISOR trilogy"):** on the Amery Ice Shelf, snow-trac vehicles "were driven onto the ice shelf further north via Mechanics Bay", and "occasional slotting of vehicles had occurred" on over-snow trips through the area.
- **UNVERIFIED (search-result summary of an NCPOR expedition-updates page whose current version no longer carries it):** on 26 December 2016 an Indian MADICE convoy's "snowmobiles, containers and living modules" got stuck in a melt-water channel on the ice shelf returning to Maitri, recovered by 3 January 2017.
- **Already in other files:** Mirny 1956 tractor through sea ice, one death (port file D); Wilkes 1962 crevasse and mechanical delays (port file C); Maitri 2012 barrier calving with cargo (port file D).

### 2.3 Moving large loads across an ice shelf (beyond port file D)

- **SOURCED (AAD magazine issue 11, 2006, "Station on skis"):** Halley VI's "completed modules will weigh around 80 tons"; "each module is supported by jackable steel legs on skis"; "the completed station … will later be towed inland using bulldozers"; it was to stand "16km further inland" than Halley V.
- **SOURCED (ENR, 12 May 2014, "Global project of the year: Halley VI"):** "each load could not exceed six tons—plus 3.5 tons for the sled" across sea ice "usually 1 m thick"; skis "3.9-m-long, 1.1-m-wide … double as spreader foundations"; designers aimed to reduce friction "when moving the 60-ton to 200-ton modules"; on-site build window "10- to 12-week" a year.
- **UNVERIFIED (search summaries of BAS and British Council pages; the BAS page returned empty to both tools):** in 2016-17 the eight modules were moved 23 km upstream of the reactivated chasm over about 13 weeks, each decoupled and towed by tractor.
- **SOURCED (PTC 2012, above):** flexible fuel bladders on HMW plastic sleds replaced steel tanks on the SPoT; air-cushion pontoon platforms for cargo were field-proven over 1,600+ miles in 2011-12.

### 2.4 Oasis stations supplied across an ice shelf: the nearest real precedents

- **Schirmacher Oasis (Novolazarevskaya, Maitri).** **SOURCED (en.wikipedia, "Schirmacher Oasis"):** "The oasis is located between the edge of the Antarctic Ice Sheet and the Novolazarevskaya Nivl Ice Shelf"; Dakshin Gangotri "was set up on the shelf ice, about 90 km from the Schirmacher Oasis" (1983-1989); the oasis has epishelf lakes with tidal effects. **SOURCED (ru.wikipedia, "Новолазаревская"):** the station is "примерно в 80 км от берега моря Лазарева" (about 80 km from the Lazarev Sea coast); a snow-ice runway 12 km south (1979, Il-76). **SOURCED (port file D):** cargo goes to a "barrier base" and is hauled by sled-tractor traverses; the Indian Barrier is "about 100 km north" of Maitri. **NOT FOUND:** the haul's distance as driven, vehicle count, time, or tonnage per season (searched in English and Russian; polarpost.ru forum returned HTTP 503; NCPOR reports not found in public form).
- **Princess Elisabeth.** **UNVERIFIED (search-result text of International Polar Foundation pages, not opened; consistent with port file D's ≈200 km):** the building load was carried "over almost 200 km, using three 'Prinoth' tractors and eight sleds … 18 traverses and over 700 hours"; one return trip needed a roadside repair because "fibrous debris had partially blocked its fuel lines". (Grounded inland ice, not an oasis behind a shelf.)

### 2.5 What these precedents show (facts only)

- Every heavy over-ice route found runs **in summer only** (SPoT 25 Oct-10 Feb; port file C for the others).
- Crevassed margins are crossed on a **fixed, surveyed trail that is re-surveyed every season** with GPR, with a few crevasses **blasted open and back-filled each year** before the heavy train crosses (SPoT: 2-3 a year on a 5.6 km trail with ≈40 crevasses).
- The trail itself **moves with the ice** (2.3-3.8 km in 9 years at the SPoT crossing) and lengthens, and must eventually be relocated.
- Lead vehicles with GPR hold **≤11 km/h**; heavy trains run 13-16 km/h on surveyed trail (SPoT).
- Fuel for a heavy train is **≈66 L/km for the whole 9-vehicle train** (SPoT), or **0.3-0.9 L per delivered t·km** counting all fuel over a season (SPoT 2005-2012, excluding the 2007-08 trial year).
- Known failures: heavy vehicles through snow bridges in a shear zone (1990) and a hinge zone (1969); deaths in crevasses (1965); sled and bladder breakages; storms burying trains for days; a convoy stuck in a meltwater channel on an ice shelf (2016, UNVERIFIED).

### 2.6 Item 2 search log

| # | Tool | Exact string or URL | Result | Died at |
|---|---|---|---|---|
| 1 | WebSearch (extended) | `McMurdo shear zone crevasse remediation South Pole Traverse ground penetrating radar filled crevasses bulldozer snow bridge CRREL` | Kaluzienski 2019, Marsh 2021, ADS abstracts | Partial |
| 2 | WebFetch / curl | cambridge.org Kaluzienski et al. 2019 (article page and Unpaywall PDF link) | 403 / Cloudflare "Just a moment" | Source (not worked around) |
| 3 | curl | sciencedirect.com S0165232X18302301 (Ray et al.) | Page shell only, no text | Source |
| 4 | WebSearch (extended) | `Antarctic Sun shear zone crossing traverse crevasses filled blasted "shear zone" route 2.5 miles wide crevasse detection radar PistenBully boom` | Antarctic Sun pages listed | Query hit; sources below |
| 5 | WebFetch | antarcticsun.usap.gov/science/contenthandler.cfm?id=4084 and /science/4454/ | `getaddrinfo ENOTFOUND` | Source (DNS) |
| 6 | WebFetch | web.archive.org copy of the same | Tool refused this host | Source (not worked around) |
| 7 | WebFetch | nzgeo.com/stories/the-long-haul/ | 403 | Source |
| 8 | WebFetch | en.wikipedia.org/wiki/South_Pole_Traverse | Read | Hit |
| 9 | WebSearch (extended) | `Halley VI relocation 2016-2017 modules towed across Brunt Ice Shelf tractors tonnes per module speed crevasse Chasm` | BAS, LiveScience, AECOM | Partial |
| 10 | WebFetch / curl | bas.ac.uk relocation-success page; livescience.com 57440 | Empty / headline only | Source |
| 11 | WebSearch (standard) | `Halley VI relocation module weight tonnes towed bulldozers skis 2017 "km" "tonnes" British Antarctic Survey move details` | AAD 2006, ENR 2014 | Hit |
| 12 | WebFetch | antarctica.gov.au magazine issue 11 "Station on skis"; enr.com 7401 | Read | Hit |
| 13 | WebSearch (standard) | `tractor fell into crevasse ice shelf Antarctica traverse killed Halley Bay 1965 Muskeg history` | Z-fids pages | Hit |
| 14 | WebFetch | zfids.org.uk/1972/ihrec.htm; zfids.org.uk/1965/cross.htm | Read | Hit |
| 15 | WebSearch (standard) | `Kohnen traverse fuel consumption PistenBully per km liters sledge load tonnes Neumayer AWI traverse` | Only generic PistenBully sheets | Query |
| 16 | WebSearch (extended) | `Новолазаревская ледовый барьер выгрузка санно-гусеничный поход расстояние км от барьера до станции шельфовый ледник Лазарева` | ru.wikipedia, polarpost forum, AARI RPR-6 | Partial |
| 17 | WebFetch / curl | polarpost.ru viewtopic t=1969; data.aari.ru RPR-6_site.pdf | 503; RPR-6 has no barrier distance | Source |
| 18 | WebFetch | ru.wikipedia Новолазаревская; en.wikipedia Schirmacher_Oasis | Read | Hit |
| 19 | WebSearch (extended) | `Maitri station convoy "India Bay" OR "Indian Barrier" ice shelf Schirmacher oasis km hours PistenBully sledges cargo transport expedition report` | GitHub demos (not used), Wikipedia | Query |
| 20 | WebSearch (standard) | `"India Bay" Maitri convoy shelf ice km tractors "Indian Expedition to Antarctica" logistics unloading ice shelf cargo tonnes report pdf` | NCPOR news 147, seanews 2026, MADICE snippet | Partial |
| 21 | WebFetch | ncaor.gov.in expedition updates (certificate error); ncpor.res.in same page (read; MADICE item absent); seanews.ru 15 Jan 2026 (read) | — | Partial |
| 22 | WebSearch (standard) | `Princess Elisabeth station traverse Prinoth tractors fuel consumption liters per kilometer sledges Lehmann tonnes per tractor coast Breid Bay crevasses route` | IPF pages (search text) | Partial (no fuel figure) |
| 23 | WebSearch (standard) | `Amery Ice Shelf overland traverse tractors Davis OR Zhongshan crevasse grounding zone 1960s ANARE Amery traverse vehicles` | AAD 2004 magazine; xnatmap reports | Partial |
| 24 | WebFetch | antarctica.gov.au magazine issue 6 "AMISOR trilogy" (read); xnatmap.org 1962-63 report (DNS failure) | — | Partial |
| 25 | WebSearch (standard) | `crevasse detection ground penetrating radar mounted boom ahead of tractor 400 MHz traverse speed km/h snow bridge "crevasse" Antarctic traverse lead vehicle` | Delaney-Arcone, Zamora (snippets) | Sources not opened |
| 26 | WebSearch (standard) | `Delaney Arcone "Crevasse detection with GPR across the Ross Ice Shelf" 400 MHz 6.5-m boom thirty-two crevasses 4.8 km` | Record pages; ISC page SSL error; core.ac.uk PDF returned HTML | Source |
| 27 | WebSearch (standard) | `southpolestation.com South Pole traverse shear zone crevasses filled tractors sleds fuel bladders Case Quadtrac Challenger "shear zone"` | PTC 2012 Thur PDF | Hit |
| 28 | curl | sundowner.colorado.edu/seefeldt/ptc-2005_2016/2012_pdf/PTC_2012_Thur.pdf | Read in full (22 pp.) | Hit |
| 29 | WebSearch (standard) | `Antarctic traverse vehicle fell into crevasse ice shelf accident PistenBully OR tractor 2010s 2020s rescued driver grounding zone` | "Linda" 1990; NASA EO 2005; older cases | Hit |
| 30 | WebFetch | southpolestation.com/trivia/90s/linda.html; science.nasa.gov out-of-the-crevasse-field | Read | Hit |


---

## 3. Satellite and survey data along the corridor (DERIVED unless marked)

**No route is chosen here.** The straight lines below are sampling lines between real points (ice-front points, ship positions on record, and the two stations and the 1948/2024 camp island). They show what lies between the front and the oasis; they are not proposed paths.

### 3.1 Datasets, versions and method

| Dataset | Version and source | What was used | Resolution and date |
|---|---|---|---|
| REMA (Reference Elevation Model of Antarctica) | v2.0 32 m mosaic, Polar Geospatial Center, `pgc-opendata-dems.s3.us-west-2.amazonaws.com/rema/mosaics/v2.0/32m/` tiles 25_56, 25_57, 26_56, 26_57 (`dem`, `maxdate`, `mindate`) | Surface height; per-pixel newest and oldest strip date | 32 m; strips 2011-09-24 to 2020-02-17 (tile 25_57 STAC: 60 WorldView strip pairs) |
| Geoid | EGM2008 via PROJ network grid (`EPSG:4979` → `EPSG:4326+3855`) | Ellipsoid to orthometric: N = −2.1 m at 100.29°E 65.77°S, −2.4 m at 100.6°E 66.0°S, −2.8 m at 100.75°E 66.27°S, −3.4 m at 101.8°E 65.78°S | — |
| ITS_LIVE | v2 static 120 m mosaic, RGI19A (Antarctica), NASA MEaSUREs/JPL, `its-live-data.s3.amazonaws.com/velocity_mosaic/v2/static/cog/` (`v`, `vx`, `vy`, `v_error`, `count`, `floatingice`, `landice`) | Speed and the floating-ice mask | 120 m; "climatological [2014-2022] v … time-intercept of January 1, 2018" (file metadata, SOURCED) |
| Fracture map | Surawy-Stepney and Hogg 2023, Zenodo 10.5281/zenodo.8296992, `202106_fracture_map.tiff` (the one composite month published); paper *The Cryosphere* 17:4421 (PDF read) | Fracture score D, 0-1 | 100 m; June 2021 composite of Sentinel-1 IW images |
| ICESat-2 | ATL06-style heights computed by SlideRule Earth (`icesat2.atl06p`), 2019-2025 east box, 2023-2025 west box | Heights, cliff steps, seasonal surface class | 40 m segments, 20 m spacing |
| Coastline, front, grounding line | SCAR ADD high-resolution polylines and polygons (BAS ArcGIS FeatureServer) | Front lines with their source scene and date; grounding-line and rock-coast crossings | Lines dated 2000 (Landsat 7), 2016 and 2022 (Sentinel-1) |

**Sampling.** Each line was sampled every ≈100 m on the WGS84 ellipsoid (pyproj `Geod.npts`). At each point: REMA height (nearest 32 m pixel) converted to EGM2008; ITS_LIVE speed and floating mask (nearest 120 m pixel); fracture score (nearest 100 m pixel). "1-km relief" = (max − min height within a sliding 1 km window) ÷ 1 km, as a percent; the floating-shelf figures use only windows that are entirely on the ITS_LIVE floating mask and ≥3 m; it is a crude roughness and slope measure, not a gradient along a path. Grounding-line and rock-coast crossings are counted against the ADD lines. Scripts: `scripts/load.py`, `scripts/transects.py`, `scripts/region.py` in the session scratchpad (session-only).

### 3.2 What lies along the sampling lines

| Line | Length | Sea-ice-level surface (<3 m) | Floating shelf ≥3 m | Grounded or other ≥3 m | Grounding-line crossings (ADD) | Speed median / 90th pct / max (m/yr) | Samples with fracture D > 0.5 | 1-km relief on the floating shelf ≥3 m: 95th percentile / max | Highest 1-km relief anywhere |
|---|---|---|---|---|---|---|---|---|---|
| **T1** W corner (65.770°S 100.293°E, ADD 2022) → Edgeworth David | 55.3 km | 7.4 km | **47.5 km** | 0.5 km | 0 | 47 / 126 / 340 | 7% | 0.52% / 1.70% | 2.1% |
| **T2** W corner → Thomas Island (66.105°S 100.94°E) | 47.6 km | 11.2 km | 26.9 km | 9.5 km (ice rise or island classed "land") | 3 | 9 / 55 / 340 | 4% | 1.80% / 2.50% | 4.5% |
| **T3** PS141 ship position 19 Feb 2024 (65.711°S 100.330°E) → Dobrowolski | 65.6 km | 8.9 km | 41.8 km | 15.0 km | 3 | 17 / 80 / 135 | 17% | 0.80% / 1.30% | 11.2% (oasis hills) |
| **T4** E front (65.780°S 101.809°E, ADD 2016) → Dobrowolski | 73.2 km | **50.9 km** | 7.2 km | 15.2 km | 4 | 6 / 60 / 68 | 23% | 1.01% / 1.25% (only 42 windows) | 8.4% |
| **T5** E front (same point) → Thomas Island | 53.6 km | **50.6 km** | 0.4 km | 2.7 km | 2 | 10 / 37 / 61 | 17% | — (no 1 km window of floating shelf ≥3 m) | 5.1% |
| **T6** E front at 101.55°E 65.61°S → Dobrowolski | 82.6 km | 31.3 km | 40.3 km | 11.1 km | 1 | 17 / 71 / 78 | 8% | 0.43% / 1.02% | 7.6% |
| **T7** reported *Akademik Fedorov* position 20 Jan 2022 (65.75°S 100.783°E) → Dobrowolski | 58.5 km | 19.2 km | 18.3 km | 21.1 km (crosses south end of Mill Island, up to ≈115 m) | 3 | 7 / 76 / 84 | 12% | 1.53% / 2.07% | 6.8% |

**Height profile along T1 (every 2 km; EGM2008 m / speed m/yr):** 0 km 28.7/340 · 2 km 32.2/221 · 4 km 31.1/195 · 6 km 32.5/110 · 8 km 29.7/87 · 10 km 30.6/60 · 14 km 26.9/53 · 18 km 23.2/47 · 22 km 19.2/24 · 26 km 13.7/30 · 30 km 9.3/33 · 34 km 6.0/41 · 36-40 km 1.1-1.2/23-47 (sea-ice level) · 42 km 13.9 · 46 km 21.9/81 · 50 km 12.8/68 · 52 km 8.3 · 54 km 1.6 (oasis shore). **The floating shelf on this line falls about 25 m over 34 km (≈0.07% average grade).** Fracture bands (D > 0.5, ≥300 m long) at 0-0.3, 5.4-5.7, 7.4-7.8, 42.2-42.8 and 52.7-53.1 km.

**Height profile along T4 (every 2 km):** 0-24 km 0.1-2.7 m (sea-ice level; speed 3-24 m/yr, which is near the noise level of the product) · 26-28 km 6.3-6.5 m · 30 km 0.5 · 32-34 km 8.5-8.8 m (speed 58-66 m/yr) · 36 km 0.7 · 38-40 km 33-43 m (grounded) · 42-58 km mostly 0.8-2.3 m (oasis embayment fast ice) with islands · 60-72 km islands and bays to Dobrowolski. Fracture bands cluster at 26.9-37.0 km (seven bands).

**Reading the table (DERIVED):**
- **West of Mill Island's southern end, the ground between front and oasis is mostly continuous floating shelf with a smooth, gently falling surface and few mapped fractures.** On T1 the shelf is unbroken for ≈34 km before the first sea-ice-level gap; on T1, 95% of 1 km windows on the floating shelf have under 0.52% relief (max 1.70%); T2's higher figures (95th percentile 1.80%) come from the stretch beside the ice rise.
- **The fastest ice is at the front.** Speeds of 126-340 m/yr in the first few kilometers (Scott Glacier) drop below 100 m/yr within ≈8 km and to 10-50 m/yr over most of the western lines. A fixed point on the shelf near the oasis moves tens of meters a year; near the corner it moves hundreds.
- **Grounded features interrupt some lines.** T2 and T3 cross an ice-covered feature classed "land" by the ADD at ≈65.84-65.87°S, 100.43-100.48°E (surface 39-51 m, speed 1-5 m/yr), with ADD grounding lines on either side. Grounding zones are where ice flexes with the tide (general glaciology; the Halley Bay 1969 tractor loss "in the hinge zone" in section 2 is one real case).
- **The eastern lines are mostly at sea-ice level** (section 3.3).
- **Near the oasis every line meets sea-ice-level surfaces (the oasis's enclosed marine water, ≈1 m) and then rock with 1-km relief of 2-11%.**

### 3.3 The eastern "ice shelf": what the surface data show (DERIVED; resolves part of port file A's open question)

Port file A asked whether part of the ADD's eastern "ice shelf" (≈101.2-102.5°E, 65.8-66.0°S) is multiyear fast ice. Two independent surface datasets were checked.

**REMA (2011-2020 strips).** Within 101.2-102.5°E, 65.55-66.0°S, of the area inside the ITS_LIVE floating-ice mask (96,705 samples at 128 m spacing):
| Height above EGM2008 | Share of the floating-mask area |
|---|---|
| < 2 m | 21% |
| < 4 m | 37% (≈583 km²) |
| < 8 m | 61% |
| < 15 m | 73% |
- In those <4 m pixels the oldest contributing strip dates from **2011-09-24 to 2016-10-01** and the newest from **2012-11-06 to 2020-02-17**; the newest strips are mostly August 2019 and **February-March 2019 (late summer)**. **So the surface read at sea-ice level in strips years apart, including late summer.**
- For contrast within the same corridor, in the western sector (99.9-100.6°E, 65.7-66.1°S) only 2% of the floating-mask area is below 4 m.

**ICESat-2 (SlideRule ATL06-style, 2019-2025), 101.3-102.2°E, 65.65-65.95°S, samples inside the ITS_LIVE floating mask (579,955 segments):**
| Year | Water-like (< −0.3 m) | Sea-ice-like (−0.3 to 3 m) | 3-8 m | ≥ 8 m |
|---|---|---|---|---|
| 2019 | 2.8% | 26.3% | 40.4% | 30.4% |
| 2020 | 1.9% | 26.6% | 40.4% | 31.1% |
| 2021 | 7.7% | 29.3% | 35.4% | 27.6% |
| 2022 | 2.5% | 27.0% | 37.8% | 32.7% |
| 2023 | 2.2% | 31.1% | 36.3% | 30.5% |
| 2024 | 4.7% | 33.6% | 38.4% | 23.3% |
| 2025 | 5.3% | 28.9% | 37.0% | 28.8% |
| **January-March, all years** | **2.4%** | 28.4% | 39.5% | 29.6% |
- Of 613 one-km cells sampled in four or more years, **183 have a median below 3 m and a 90th percentile below 4 m** (≈183 km²).
- Of 546 cells with January-March samples in three or more years, **116 were sea-ice-like (−0.3 to 3 m) in every one of those summers.**

**What this supports (DERIVED):** a large part of the ADD's eastern "ice shelf" near the Bunger Hills is **an ice surface 0-3 m above the geoid that is still present in summer, year after year (2011-2025)**, with almost no open water inside it even in January-March. That fits **multiyear landfast sea ice** (the AARI text above records >100 km-wide fast ice at the Malygintsev and Milovzorov glacier bays and multiyear fast ice standing 1.5-2 m above first-year ice elsewhere on this coast) **or very thin floating ice**; the two cannot be told apart from surface height alone. A further ≈35-40% of the area stands at 3-8 m. **It does not fit a 180-250 m-thick ice shelf**, which would stand ≈20-35 m high (port file A). **NOT FOUND:** any ice-thickness or radar measurement that settles which it is.

### 3.4 Fractures and crevasses (DERIVED from the June 2021 fracture map; SOURCED limits)

- **SOURCED (Surawy-Stepney et al. 2023):** type-A features are "large, multiple pixels in width" (rifts, shelf surface crevasses, basal-crevasse depressions); type-B are "fine, bright lines … pixel scale in width", mainly grounded crevasses and "to a far lesser extent, narrow ice shelf surface crevasses bridged by snow". "Approximately 85 % of type-B crevassing appears on grounded ice." The paper's Fig. 4e covers the "Shackleton Ice Shelf and Denman Glacier" and notes "severe crevassing in shear margins" on the Shackleton Ice Shelf.
- **SOURCED limits:** false type-B detections occur "in regions of steep topography, such as the ice rises and mountains"; specificity "is also low in regions where there is a large amount of surface meltwater". **The June 2021 composite is a winter map, so summer melt does not affect it, but the oasis hills and ice rises are where false positives are expected.** Crevasses are mapped where they are "linear on scales that are large compared to the resolution of the data" (100 m in the published file), so narrow bridged crevasses can be missed.
- **SOURCED (Marsh et al. 2021, *Cold Regions Sci. Tech.* 187:103284, NORA PDF read):** satellite radar crevasse detection "will … fail in regions of Antarctica where temperatures regularly exceed 0 °C, particularly when images are acquired in mid-late summer"; "additional ground observations from other areas would be needed before this technique could be relied on by itself for safety applications"; McMurdo Shear Zone snow bridges range from "several meters to over 10 m".
- **DERIVED, along the lines (D > 0.5):** T1 7% of samples, five short bands; T2 4%; T3 17% (most in the last 25 km, among the oasis islands and the outlet ice there); T4 23% and T5 17% (bands clustered 27-38 km from the eastern front, where ITS_LIVE speed rises to 46-66 m/yr); T6 8%; T7 12%.
- **DERIVED, the first 10 km inside the western corner:** fracture bands at 0-0.3 km (the front edge itself, D ≈ 0.97), 5.4-5.7 km and 7.4-7.8 km on T1; at 0.6-1.1, 2.0-2.4 and 5.7-5.9 km on T3. **Elsewhere on the western floating shelf, D stays mostly at 0.02-0.06.**
- **Not done:** a month-by-month fracture time series (the authors share it on request only). **NOT FOUND** in public form.

### 3.5 Ice velocity (DERIVED, ITS_LIVE v2, 2014-2022 climatology)

| Place | Speed (m/yr) |
|---|---|
| ADD 2022 western corner point | ≈340 |
| 2-4 km inside the corner (T1) | ≈195-220 |
| 8 km inside (T1) | ≈87 |
| 10-34 km inside (T1) | ≈24-60 |
| ice rise/island at 65.84-65.87°S (T2) | ≈1-5 |
| eastern sea-ice-level area (T4 0-24 km) | ≈3-24 (near the product's noise level over fast ice) |
| fractured belt 27-37 km in from the eastern front (T4) | ≈46-66 |
| Apfel Glacier (port file A, SOURCED, Thompson et al. 2023) | ≈150-220 |

The ITS_LIVE `v_error` layer was extracted but not used to filter the table; values under ≈10 m/yr should be read as "slow or noisy", not as measured motion.

### 3.6 Accumulation and melt

- **SOURCED (Inoue et al. 2017, *Climate of the Past* 13:437, abstract page read):** a 120 m ice core drilled on **Mill Island (65°30′S, 100°40′E)** in 2009/10 gives mean accumulation of **"1.35 m (ice-equivalent) per year"** for 1913-2009. **UNVERIFIED (search summary of the thesis):** annual range 0.79 m (1969) to 2.04 m (1934). The paper says accumulation there is influenced by local orography, so it is an ice-dome value, not a shelf value.
- **SOURCED (Arthur et al. 2020, *The Cryosphere* 14:4103, PDF read):**
  - Supraglacial lakes on the Shackleton Ice Shelf "cluster around the ice shelf grounding zone, near exposed blue-ice areas and the Bunger Hills nunataks, whereas they are almost entirely absent towards the ice shelf calving front, where surface melt rates are highest".
  - "Lakes form in particularly high densities on Scott, Apfel and Remenchus glaciers", reaching 0.27 km² per km². "No lakes form on the heavily crevassed tongue of Denman Glacier."
  - In a typical season there are "hundreds (∼100–1000)" of lakes, mean area 0.02 km², mean depth 0.96 m; at most 50.7 km² in total. The largest feature was "an area of coalesced lakes covering up to 11.96 km² which formed in January 2020 on Scott Glacier", next to elongate lakes in a "∼10 m deep longitudinal depression".
  - Lakes start "in late November", peak "in early to late January", and decline "until late February".
  - Lakes upstream of Apfel Glacier recur in the same places (seven lakes present in 62% of scenes); the highest recorded lake was at 527 m a.s.l., 12.8 km inland of the grounding line.
  - Katabatic winds "reach 19 m s−1 in summer"; blue ice (albedo ≈0.5) and dark rock raise melt locally "within 10 km"; RACMO 2.3p1 puts firn air content "as low as ≤1 m on parts of the ice shelf"; accumulation rises "towards the ice shelf calving front".
  - The outer shelf melts >200 mm w.e./yr (Trusel et al., cited there; also in port file A).
- **DERIVED, connecting to the corridor:** the lake belt (grounding zone, blue ice, oasis margin) lies on the **oasis end** of every sampling line, not at the front. The near-front shelf gets more snow and holds meltwater in firn.
- **NOT FOUND:** a measured or modeled accumulation rate on the shelf between the front and the oasis (RACMO2 regional tables were not reached; the RACMO2.4p1 paper, *The Cryosphere* 19:4061, 2025, was identified but its regional values were not extracted).

### 3.7 What the data show, in one place (DERIVED; no route chosen)

1. **Western side (Scott/Mill corner toward the oasis):** a measured 24-36 m ice cliff at the front (ICESat-2, 2023-2025); behind it, 34-48 km of continuous floating shelf with a smooth surface falling from ≈30 m to ≈6-15 m, low fracture scores away from the front's first ≈8 km, and speeds that fall from ≈340 to ≈50 m/yr within ≈10 km. The front edge itself moves kilometers in a few years and broke in 2022 and 2024.
2. **Eastern side:** a low or missing cliff (6-13 m where there is one) and, behind it, a mostly sea-ice-level surface that persisted 2011-2025 including summers, with a fractured belt ≈27-38 km in.
3. **Near the oasis on both sides:** the oasis's enclosed marine water (≈1 m surface, fast ice), islands, ice rises, a surface-lake belt in summer, and rock with 2-11% relief per kilometer.
4. **What the satellite data cannot show:** bridged crevasses narrower than about 100 m, ice thickness, the strength of any snow bridge, and conditions after the dates listed.

### 3.8 Item 3 search log

| # | Tool | Exact string or URL | Result | Died at |
|---|---|---|---|---|
| 1 | WebSearch (standard) | `Surawy-Stepney 2023 Antarctic fracture crevasse map Sentinel-1 deep learning dataset download zenodo` | Paper and Zenodo DOI found in the paper's data statement | Hit |
| 2 | curl / Zenodo API | `tc.copernicus.org/articles/17/4421/2023/tc-17-4421-2023.pdf`; `zenodo.org/api/records/8296992` | Paper read; one month (June 2021) published; read by HTTP range requests (the 1 GB file is strip-organized) | Hit |
| 3 | curl | S3 listings of `pgc-opendata-dems` and `its-live-data` | First guessed URLs 404 (`.../100m/rema_mosaic_100m_v2.0_filled_cop30_dem.tif`, `.../ANT_G0120_0000_v.tif`); correct keys found by listing | Query (wrong guesses) → Hit |
| 4 | curl | `tc.copernicus.org/articles/14/4103/2020/tc-14-4103-2020.pdf` | Arthur et al. 2020 read | Hit |
| 5 | WebSearch (standard) | `Shackleton Ice Shelf surface mass balance accumulation rate kg m-2 yr RACMO snowfall Bunger Hills region` | No site value; RACMO2.4p1 paper identified | Query |
| 6 | WebSearch (standard) | `Mill Island ice core accumulation rate East Antarctica Vallelonga 2017 snow accumulation m ice equivalent` | Inoue et al. 2017 | Hit |
| 7 | WebFetch | `cp.copernicus.org/articles/13/437/2017/` | Abstract read (1.35 m IE/yr) | Hit |
| 8 | curl | `nora.nerc.ac.uk/id/eprint/527817/1/1-s2.0-S0165232X21000653-main.pdf` | Marsh et al. 2021 read | Hit |
| 9 | Data | SlideRule `atl06p` east box 2019-2025 | 793,192 segments; 579,955 on the floating mask | Hit |

**Self-correction (item 3):** the first draft of the table in 3.2 carried estimated "highest 1-km relief on the floating shelf" values (≤0.2-1.0%) read off the 2 km printout; they were recomputed over every sliding 1 km window entirely on floating shelf ≥3 m (95th percentile 0.43-1.80%, max 1.02-2.50%) and replaced before ticking.

---

## 4. Ice-front landing: the gaps port file D left

Port file D's NOT FOUND list (items 1, 2, 4, 6, 8) and thin spots: Atka tonnage and change over time; engineering of ship berthing against floating cliffs (cliff stability under crane loads, mooring loads, swell); Novolazarevskaya barrier distance and tonnage; a modern measured Shackleton freeboard (now done in section 1.1b). Below is only what is new.

### 4.1 How high a front can be for crane unloading

- **SOURCED (NSF Office of Polar Programs Advisory Committee, *Report of the Subcommittee on U.S. Antarctic Program Resupply*, August 2005, PDF read, pp. 49-52):** "In general, a site where the ice shelf surface is not much higher than approximately the same as the height of the ship's deck (about 2-7 meters) above the sea is required for cargo unloading, so that the ship's crane(s) can lift cargo to the top of the ice shelf." "South Africa has used a high ice shelf with an access ramp carved into it … but persons involved report occasional problems, such as vehicles and/or cargo sliding down the ramp." "The 7-meter maximum ice shelf height does not directly apply to fuel offloads, which could reach the tops of significantly higher ice shelves via hoses and pumps." "No suitable ice shelf sites for cargo offload/onload were found in the southwestern Ross Sea."
- **Conflict with port file D:** ships have craned containers onto shelf edges of **12 m** (Atka 2017), "up to 15 meters" (Atka, Royal Arctic Line 2021) and **17 m** (Breid Bay, "just the right height for the deck cranes"). The NSF 2-7 m figure is a planning rule from 2005; the real berths in use are higher. Both are recorded; neither is resolved.
- **UNVERIFIED (search-result text of a 2017-18 Swedish MAGIC-DML expedition blog; page certificate error):** at the South African offload site "the ice shelf surface is about 40m above the ship's deck, so everything has to be lifted up by crane."
- **SOURCED (HartRAO, "2007/08 Summer Relief Expedition", read):** "Upon reaching the ice shelf, the first task was to bulldoze a ramp for offloading cargo"; the voyage took 26 days to reach Antarctica.
- **UNVERIFIED (search-result text of a South African expedition blog, not opened):** "our ramp has been declared unsafe due to the deteriorating ice conditions" in warmer weather and rougher seas.
- **DERIVED (connecting to section 1):** the measured cliff at the Shackleton western corner in 2023-2025 was ≈24-36 m (ICESat-2), above every working cargo berth found (10-17 m) and well above the NSF 2-7 m rule. The eastern front is 6-13 m where a step exists, but sits in front of a sea-ice-level surface (section 3.3). No ramp, low point or berth-height assessment exists for this front: NOT FOUND.

### 4.2 Cliff and staging-area stability: failures added

- **SOURCED (ABC News, 23 May 2026, read; consistent search summaries of Newser, RSOE-EDIS and others):** at **Neumayer III (Atka Bay)**, a blizzard of 130 km/h between 13 and 20 January [2026] calved "a roughly 500 m by 300 m iceberg" from the ice shelf carrying **seven containers** staged "a few hundred meters from the icy coastline" for a waste pickup: one with 9,500 L of Arctic diesel, four with non-hazardous waste, one with a generator and fuel, one shelter. Helicopters recovered "almost one ton" (three diesel drums, gas cylinders, batteries); salvage stopped on 25 January "because of the risk to human life"; the berg was last seen by satellite on 22 February and is presumed broken up. **New rule: containers to be stored "at least 5,000 meters distance to the ice shelf edge."** **UNVERIFIED (Newswav summary):** AWI committed to more thorough glaciological surveys along the station-to-ice-port route. **The AWI primary statement was not found** (searched; AWI press archive page "Neumayer und umzu" listed but not read).
- **Already in port file D:** Maitri, April 2012 (2 km × 1 km of the "Indian Barrier" with tank containers and fuel lost); Atka 2005 (berth rejected because of a long crack); Breid Bay (swell ripped out mooring pins, ship heaving 3-4 m).
- **SOURCED (AARI, *Rossiyskie Polyarnye Issledovaniya* no. 20, 2015, read in Russian):** at Novolazarevskaya in the 60th RAE (2014/15), "штормовая погода сменялась периодами затишья, используя которые швартовку провели успешно" (stormy weather alternated with calm spells, which were used to moor successfully); "погрузка на судно баржи «задержавшейся» на барьере станции с сезона 54-й РАЭ (2009 г.)" required extra effort, i.e. a barge had been left on the station's barrier since 2009. At Progress the same season, the plan assumed the worst case of multiyear fast ice persisting at the usual unloading place, where unloading over fast ice "сопряжено с определенным риском, всегда возникающим при транспортировке грузов по морскому льду" (carries the risk always present when moving cargo over sea ice).
- **NOT FOUND:** any published engineering limit for crane or vehicle loads near a floating ice-cliff edge, any rule for setback of cranes or vehicles from the edge (other than AWI's new 5 km container-storage rule), and any CRREL or peer-reviewed study of mooring loads against a floating ice front. Searched in English, German and Russian (log below).

### 4.3 Tide and swell at an ice front

- **Already known (ocean file, items 1-2):** modeled tide next to the front ≈1.2-1.3 m mean daily range, ≈2.1-2.5 m largest astronomical; swell periods ≈10-11 s; 5 m storms about 6 times a year near 64°S. Breid Bay pins ripped out by swell (port file D).
- **UNVERIFIED (search-result text of AGU 2015 abstract C11C-0777):** a coupled seismic-GPS instrument on an Antarctic ice shelf recorded tide-induced vertical motion "with a maximum of about 1.5 m over 5 hours" (near the grounding line, not the front). **UNVERIFIED (search text of Bromirski and co-workers):** swell-driven strain near the Ross Ice Shelf front of "tens to hundreds of nanostrain"; front vertical displacement amplitudes correlate with ocean gravity-wave amplitude.
- **General physics, not site-sourced:** a floating ice shelf rises and falls with the tide almost as a body away from its grounding zone, as a moored ship does; the relative motion at a berth comes mainly from swell, surge and wind, which the ice damps for most of the year (ocean file).
- **NOT FOUND:** any measurement of ship-to-cliff relative motion, or a swell limit for working a ship against an ice front.

### 4.4 Time and tonnage actually unloaded (additions)

| Site | Time | Tonnage or volume | Source | Mark |
|---|---|---|---|---|
| Neumayer III (Atka), planning rule | "takes 6 to 24 hours depending on ice conditions" to reach the berth; "at least 72 hours at the shelf ice edge", "may also take considerably longer"; 13 days Walvis Bay to Neumayer | — | AWI Spaces, "Provisioning of stations on land" (read) | SOURCED |
| Neumayer III, one undated call (2016/17 series) | — | 270,000 L Arctic diesel + 60,000 L aviation fuel pumped across the shelf edge; 24 containers | Wissenschaftsjahr 2016*17 podcast page (read) | SOURCED (matches port file D's 320,000 L, 24 containers in Jan 2017) |
| Neumayer III, 2021/22 | — | a crane of "næsten 40 tons" (almost 40 t) landed; edge "op mod 15 meter" (up to 15 m) | maritimedanmark.dk, 1 Jan 2022 (read) | SOURCED |
| Novolazarevskaya | — | "более 522 тонн грузов, в том числе: 430 тонн дизельного топлива, 56 тонн авиационного керосина" (over 522 t incl. 430 t diesel, 56 t jet fuel) — the page does not tie it to a station or year | search-result text of a korabel.ru page | UNVERIFIED |
| Novolazarevskaya, 71st RAE | arrival reported 10 March 2026, "идет разгрузка судна" | not stated | portnews.ru 388877 (read) | SOURCED (no numbers) |
| Maitri (Indian Barrier) | ship "about 6.5 miles" off in 2026, helicopters, "for about a week" | not stated | seanews.ru, 15 Jan 2026 (read) | SOURCED |
- **NOT FOUND:** a multi-year Atka or Novolazarevskaya tonnage series (AWI EPIC and AARI summaries searched; raexp.ru station pages refused with a certificate mismatch and were not worked around).

### 4.5 Item 4 search log

| # | Tool | Exact string or URL | Result | Died at |
|---|---|---|---|---|
| 1 | WebSearch (extended) | `швартовка к ледяному барьеру выгрузка на барьер ледовые якоря трещины обрушение барьера судно Академик Федоров Новолазаревская правила безопасности` | korabel.ru, portnews, AARI RPR-20 | Partial (no rules) |
| 2 | curl | mgmtmo.ru/edumat/polar/RPR-20.pdf | Read (2014/15 Novolazarevskaya and Progress passages) | Hit |
| 3 | WebSearch (extended) | `Polarstern Atka Bucht Schelfeiskante Entladung Neumayer Container Tonnen Kraftstoff Kubikmeter Wochenbericht Eisanker festmachen Kante Riss` | Helmholtz blogs, Wissenschaftsjahr, Zarges, perlentaucher | Partial |
| 4 | WebFetch | blogs.helmholtz.de/atkaxpress/2018/02/... | 403 | Source |
| 5 | WebFetch | wissenschaftsjahr.de … polarforscher-an-der-neumayer-iii-station.html | Read | Hit |
| 6 | WebSearch (extended) | `ship moored alongside ice shelf edge ice anchors deadman mooring lines crane unloading cliff collapse Antarctic resupply ice front berth safety distance from edge` | No engineering source; found the 2026 Neumayer container loss | Query (for engineering); hit (failure) |
| 7 | WebFetch | abc.net.au/news/2026-05-23/… | Read | Hit |
| 8 | WebSearch (standard) | `Neumayer III containers iceberg calved Atka Bay January 2026 AWI seven containers diesel ice shelf edge` | Secondary reports only; AWI release not found | Partial |
| 9 | WebFetch | spaces.awi.de/x/_AQOEQ; maritimedanmark.dk/malik-arctica-losser-i-antarktis | Read | Hit |
| 10 | WebSearch (extended) | `Новолазаревская выгрузка на барьер тонн груза топлива 69-я OR 70-я OR 71-я РАЭ "Академик Федоров" OR "Академик Трёшников" береговая база барьер` | korabel, portnews, raexp | Partial |
| 11 | WebFetch | raexp.ru/info-st091112-nov091112.html | Certificate mismatch; not worked around | Source |
| 12 | WebFetch | portnews.ru/news/388877/ | Read (no numbers) | Partial |
| 13 | WebSearch (extended) | `ice shelf edge collapsed during unloading ship moored Antarctic relief calving cargo lost tractor ice cliff "ice edge" collapse resupply` | NSF 2005 resupply report | Hit |
| 14 | curl | nsf-gov-resources.nsf.gov/attachments/114452/public/oac_resupply_report_081205.pdf | Read (pp. 49-52) | Hit |
| 15 | WebSearch (standard) | `ocean swell flexure ice shelf front vertical displacement measured seismometer GPS centimeters Ross Ice Shelf front tidal vertical motion ice shelf edge meters` | Abstract snippets only | Sources not opened |
| 16 | WebSearch (standard) | `SANAE ice shelf ramp cut into ice shelf edge offloading Agulhas vehicles sliding ramp construction bulldozer Penguin Bukta "ramp"` | HartRAO page, MAGIC blog, AWI report | Partial |
| 17 | WebFetch | polarforskningsportalen.se MAGIC blog (certificate error); geodesy.hartrao.ac.za 2007/08 page (read) | — | Partial |

---

## 5. Ship-to-oasis by helicopter: the real fallback

Already known and not repeated: every recorded ship-plus-helicopter access to the oasis 1948-2022 with distances (port file B); ship helicopter types, the *Polarstern* flight rules (VFR only, 600 ft and 3 km minima, no night flying, −30/−45 °C limits, 80 nmi limit) and sortie rates at other stations (intake file D).

### 5.1 Sorties, payloads and hours on record for this oasis (new in this pass)

| Year, ship | Ship position / distance | What was flown | Sorties and time | Source | Mark |
|---|---|---|---|---|---|
| 2012, Ka-32 from Mirny (station, not ship) | Mirny → oasis, ≈347 km (port file C) | a permafrost team; instruments | "Летели довольно долго - часа полтора, если я не ошибаюсь" (we flew quite a long time, about an hour and a half, if I'm not mistaken); ≈3 h on site | LiveJournal "dorofeich", 21 Feb 2012 (participant's blog, read) | SOURCED (personal account; time approximate) |
| 2016/17, *Akademik Fedorov* (62nd RAE) | planned 90-110 km from Malygintsev/Milovzorov bays; actually Aurora Bay, **250 km** | geology support | "в силу технических причин вертолет не мог длительно находиться на полевой базе Оазис" (for technical reasons the helicopter could not stay at the Oasis field base for long) | Lunev, Vorobyov, Kiselev, *RPI* 30, 2017, p. 31 (read in Russian) | SOURCED (no counts) |
| 2017/18, *Akademik Fedorov* (63rd RAE) | "on the south of Malygintsev Bay at the minimum distance (about 65 km)" from 29 January | helicopter support of seasonal work | not stated | search-result text; the year is not stated in the snippet; PMGE page refused (TLS error) | UNVERIFIED |
| 2021/22, *Akademik Fedorov* (67th RAE) | 69 km (port file B) | Polish team flown in 8 Jan 2022 "after several days of waiting for good weather"; "The following day, the helicopter brought us two containers full of cargo" | 2 container lifts on 9 Jan; extraction 12-13 Feb of 19 people + 5 containers (port file B) | UiO *Titan* blog, entry dated 23 Jan 2022 (read) | SOURCED |
| **2024, RV *Polarstern* PS141 (new)** | 65.711°S 100.330°E: **52 km** to the Thomas Island camp (DERIVED) | 19 Feb: "Equipment and the team of eight persons were brought to this location by helicopter during 19 February"; "a small window of good flying conditions" (English summary; the German summary says the same) | **29 Feb: "Flight operations were able to begin at 15:30, and five flights were completed by dusk; so that all the people (and most of the equipment) were back on board"**; the rest of the equipment came out on 21-22 March, the earlier attempt having been prevented by weather | AWI BzPM 793 (2025), summary, weather and ch. 6.1 (read); positions from PANGAEA | SOURCED (positions DERIVED) |
| 2024, PS141 at Gaussberg (comparable case on the same voyage) | ship 58-64 km from Gaussberg on 24-25 Feb; 46-47 km on 16-17 Mar (DERIVED from PANGAEA) | camp for five people; "The weight of the entire equipment (without persons) was 3.8 tons" | "Two helicopter flights were already performed on 24 February … The remaining scientific and camp equipment as well as all five participants were flown on 25 February"; return "mainly on 16 March 2024 with two additional helicopter flights accomplished on 17 March" | AWI BzPM 793, ch. 6.2 (read) | SOURCED |
| 2024, PS141 helicopters | — | two BK117 (Northern HeliCopter crews listed) | for comparison only: the seal-tagging work used "38 hours 58 minutes corresponding with 13 flights" including rotor-off time on floes; "By late March, heavy snow on top of ice floes made some helicopter landings impossible" | AWI BzPM 793, ch. 5 (read) | SOURCED |

**Weather on the PS141 Bunger days (SOURCED, BzPM 793, weather chapter):** 19 Feb: "A very small-scale low reduced the flying conditions, but all transport flights … were nevertheless able to be carried out, before the snow began to fall and the visibility was significantly reduced." The camp's work was delayed by "winds of up to 11 Bft" until 23 Feb and ended early because of a low "forecasted to reach winds of up to 12 Bft". On 3 March the coast had "average wind speeds of up to 12 Bft"; on 21-22 March a low gave "9 to 10 Bft at the stations north of Mill Island"; on 20 March "temporary very dense fog".

### 5.2 Aircraft figures used below

| Aircraft | Load per sortie | Speed | Source | Mark |
|---|---|---|---|---|
| BK117 (Australian program, Antarctic configuration) | "maximum underslung load capacity of 1.2 tons"; "up to six passengers"; range "300 nautical miles or 555 kilometers" | — | AAD "Helicopters" page (intake file D) | SOURCED |
| H145 / EC145 C-2 (the BK117 family) | "1,600 kg … dual cargo hook load (single hook)"; up to 10 pax | cruise "241 km/h"; range "650 km" | Wikipedia "Eurocopter EC145", Specifications (H145) (read) | SOURCED (encyclopedia; whether the AAD aircraft is this model is not stated) |
| Ka-32 | "4,000 kg (8,818 lb) payload (Ka-32)" | 205 km/h cruise is given for the Ka-27, not stated for the Ka-32 | Wikipedia "Kamov Ka-27" (read) | SOURCED / UNVERIFIED for the speed |
| Ka-32S (ship-based, RAE) | "lifting capacity of up to 6 t" | — | AARI *RPR* 1(1) 2010 (intake file D) | SOURCED |
| Ka-32A11BC | external sling "up to 5 tons"; internal payload 3,700 kg / 13 pax; cruise 245 km/h; range 650 km | — | search-result text of Russian Helicopters pages (rhc.ru refused: certificate error) | UNVERIFIED |
| CH-101 (*Shirase*) | "about 3,000 kg internal loading capacity" | — | trafficnews.jp 2026 (intake file D) | SOURCED |

### 5.3 DERIVED: sorties and flight hours for stated tonnages

**Inputs stated.** Tonnages 10, 100, 1,000 and 10,000 t (round numbers chosen only to show scale; 100 t is close to the 1978/79 Polish expedition's ≈100 t in port file B, and 1,000 t to a Syowa season in port file D). Load per sortie = the rated figure in 5.2, **an upper bound**: real loads at 50-90 km with fuel, wind and cold are lower (the Macquarie Island tally in intake file D averaged ≈0.45 t per helicopter sling lift, UNVERIFIED). Distances 52 km (PS141 2024), 69 km (2022) and 90 km (2015). Speeds: 241 km/h (H145 cruise) and 205 km/h (Ka-27 cruise); sling loads are normally flown slower, so real hours are higher. Ground time per sortie 10 minutes (an assumption, not sourced). Daily rates from the record: one take-off and landing an hour per helicopter (*L'Astrolabe*, 2017, port file D) × 2 helicopters × 10 flying hours = 20 sorties a day; and 23 flights in a day (*Aurora Australis* at Syowa, 2009, intake file D).

**Sorties = tonnage ÷ load per sortie (rounded up):**

| Aircraft (load per sortie) | 10 t | 100 t | 1,000 t | 10,000 t |
|---|---|---|---|---|
| BK117 (1.2 t) | 9 | 84 | 834 | 8,334 |
| CH-101 (3 t) | 4 | 34 | 334 | 3,334 |
| Ka-32 (4 t) | 3 | 25 | 250 | 2,500 |
| Ka-32S (6 t) | 2 | 17 | 167 | 1,667 |

**Round-trip flying time per sortie (2 × distance ÷ cruise, no ground time):** BK117 0.43 h (52 km), 0.57 h (69 km), 0.75 h (90 km); Ka-32 0.51, 0.67, 0.88 h.

**Flight hours at 69 km with 10 minutes ground time per sortie:** BK117 100 t ≈ 62 h, 1,000 t ≈ 617 h; Ka-32 (4 t) 100 t ≈ 21 h, 1,000 t ≈ 210 h; Ka-32S (6 t) 100 t ≈ 14 h, 1,000 t ≈ 140 h.

**Flying days at the recorded daily rates (20 or 23 sorties a day):**

| Aircraft | 100 t | 1,000 t |
|---|---|---|
| BK117 | 3.7-4.2 days | 36-42 days |
| CH-101 | 1.5-1.7 days | 14.5-16.7 days |
| Ka-32 (4 t) | 1.1-1.2 days | 10.9-12.5 days |
| Ka-32S (6 t) | 0.7-0.8 days | 7.3-8.3 days |

**These are flying days, not calendar days.** The record above shows days lost to weather on almost every visit (2022: "several days of waiting"; PS141: flights only in "a small window", a day lost on 29 Feb until 15:30, equipment left behind for three weeks). **A count of flyable days per season on this coast: NOT FOUND** (also not found by intake file D).

### 5.4 Fuel for helicopter work (facts on record only)

- **Already in port file B:** the Australian 2023/24 camp needed 300 drums pre-positioned "and more needed" after switching to twin-engine helicopters; C-17 airdrops of 40 drums (>8,000 L).
- **NOT FOUND:** fuel burn per hour for the BK117 or Ka-32 from a primary source (manufacturer pages refused or not reached). No DERIVED fuel figure is given for that reason.

### 5.5 Item 5 search log

| # | Tool | Exact string or URL | Result | Died at |
|---|---|---|---|---|
| 1 | WebSearch (standard) | `Лунев Воробьев Киселев оазис Бангера 62-я РАЭ полевая база вертолет залив Авроры 250 км Российские полярные исследования 2017` | AARI RPI 30 (2017) | Hit |
| 2 | curl | data.aari.ru/publicat/rpr/sources/30/RPI-30-2017-04-31-33.pdf | Read (250 km; helicopter could not stay) | Hit (no counts) |
| 3 | WebSearch (extended) | `оазис Бангера январь 2018 63-я РАЭ "Академик Федоров" вертолет Ка-32 доставка груза на полевую базу рейсов тонн бухта Малыгинцев` | PMGE 63rd RAE page; "≈65 km" snippet; dorofeich blog | Partial |
| 4 | WebFetch | pmge.ru index.php?id=697 | TLS internal error; not worked around | Source |
| 5 | WebFetch | dorofeich.livejournal.com/48401.html | Read | Hit |
| 6 | WebSearch (standard) | `titan.uio.no 2022 journey Antarctica Bunger Hills Akademik Fedorov helicopter containers flights Polish expedition Dobrowolski` | UiO blog entries | Hit |
| 7 | WebFetch | titan.uio.no/blogg/forskerbloggen/2022/what-happened-between-antarctica.html | Read | Hit |
| 8 | WebFetch | en.wikipedia.org/wiki/Kamov_Ka-27; en.wikipedia.org/wiki/Eurocopter_EC145 (two reads, offset 100000) | Read | Hit |
| 9 | WebSearch (standard) | `Ka-32A11BC specifications external sling load 5000 kg cargo cabin 3700 kg cruise speed 230 km/h range Russian Helicopters` | Search text only | Partial |
| 10 | WebFetch | rhc.ru/en/catalog/ka-32a11bc/ | Certificate error; not worked around | Source |
| 11 | curl | AWI BzPM 793 and PANGAEA PS141 events (already downloaded for item 1) | Bunger and Gaussberg flight passages; ship positions | Hit |

---

## FINAL: what the data and precedents support, and do not support, about landing at the front and hauling to the oasis

**No recommendation. Facts and derivations only; the developer decides.**

### What they support

1. **The front nearest the oasis is a high, moving cliff.** At the Scott Glacier / Mill Island corner, 52-61 km from the oasis stations, the ice cliff measured by ICESat-2 in 2023-2025 stood ≈24-36 m (most often 28-33 m) above the water beside it (section 1.1b); REMA gives 17-29 m within the first kilometer from 2018-2020 strips (1.1). The front there moved kilometers between 2018 and 2022, calved in April 2022 (C-39) and again in March 2024 (PS141, 1.3), and the ice at the corner moves ≈340 m/yr (3.5).
2. **That height is above every working cargo berth found.** Real ice-front berths run 10-17 m (port file D), and the NSF 2005 planning rule for crane offload is 2-7 m; fuel can be pumped up higher faces (4.1). Where a high shelf was used with a carved ramp (South Africa), vehicles and cargo slid on it (4.1).
3. **Behind the western corner the shelf is a smooth, continuous, slowly flowing surface.** On the sampling lines, 34-48 km of floating shelf falls gently (≈0.07% average on T1) with few mapped fractures except in the first ≈8 km and near the oasis (3.2, 3.4); speeds drop to 10-60 m/yr over most of it (3.5). An ice rise and grounding lines interrupt lines that run toward the north of the oasis (3.2).
4. **The eastern side is different.** The front there is low (6-13 m) or absent, and much of the ADD's "ice shelf" behind it is an ice surface 0-3 m above the geoid that has persisted, including summers, from 2011 to 2025 (REMA and ICESat-2, 3.3), consistent with multiyear fast ice or very thin floating ice; a fractured belt lies ≈27-38 km in (3.4).
5. **Near the oasis every approach meets the oasis's enclosed fast-ice bays, islands, a summer belt of surface lakes on the grounding zone (late November to February), blue ice and rock** (3.2, 3.6).
6. **Heavy over-ice hauling across crevassed ice-shelf margins is a real, repeated practice, with a known method and known costs.** The South Pole Traverse crosses a 5.6 km shear-zone trail with ≈40 crevasses, re-surveyed by GPR every season, with 2-3 crevasses blasted and back-filled each year; the trail moves 2.3-3.8 km in 9 years; GPR-led trains hold ≤11 km/h; the whole train burns ≈66 L/km; seasons run 25 October-10 February (2.1).
7. **Failures happen at exactly these features:** a 41 t bulldozer through a snow bridge in a shear zone (1990), a tractor lost in a hinge-zone crevasse (1969), three deaths in a crevasse (1965), staged cargo lost when shelf edges calved (Maitri 2012; Atka January 2026, after which AWI set a 5 km setback for container storage), a barge stranded on a barrier for six seasons (Novolazarevskaya 2009-2015) (2.1, 2.2, 4.2).
8. **Helicopters from a ship at the front have reached the oasis in 1948, 1986, 2015, 2017-2022 and 2024**, over 52-90 km legs, but in small numbers of sorties with repeated weather waits; the largest single lifts on record are containers and a few metric tons of camp gear (5.1). At rated loads, 100 t needs ≈17-84 sorties and 1,000 t ≈167-834 sorties depending on the helicopter (5.3, DERIVED, upper-bound loads).

### What they do not support (no evidence either way)

- Any statement about the stability of the Shackleton cliff under cranes, vehicles or stored cargo: no measurement or engineering study exists for this front, or for any floating ice front (4.2).
- A ramp or low place on the western front: none is recorded (1.2).
- The thickness and strength of the eastern sea-ice-level surface (3.3).
- Snow-bridge thickness or crevasse widths along any line here: satellite maps miss bridged crevasses narrower than ≈100 m and are not reliable alone for safety (3.4).
- The real number of flyable helicopter days per season on this coast (5.3), helicopter fuel burn (5.4), and how much of a rated sling load is achievable over 50-90 km in the cold.
- Any year-round haul: every heavy route found runs in summer only (2.5).

### NOT FOUND (collected)

Published measured freeboard at this front (computed instead from ICESat-2); a ground, GPR or vehicle survey of the shelf between any front and the oasis; the 1948 Weasel route; the March 2024 calved piece's size and name; a measured or modeled accumulation rate on the shelf corridor; fracture-map time series; a CRREL or peer-reviewed study of ship berthing against floating ice cliffs (cliff stability, mooring loads, swell); ship-to-cliff relative motion; the Novolazarevskaya barrier-to-station distance as driven, and its tonnage per season; an Atka multi-year tonnage series; the AWI primary statement on the January 2026 container loss; Kaluzienski et al. 2019 and Delaney-Arcone 2005 full texts (blocked); a flyable-day count for ship helicopters on this coast; helicopter fuel burn from a primary source.

### Pages that failed and were not worked around

cambridge.org (Cloudflare 403); sciencedirect.com (shell only); antarcticsun.usap.gov (DNS failure); web.archive.org (tool refused); nzgeo.com (403); blogs.helmholtz.de (403); bas.ac.uk relocation page and livescience.com (empty); polarpost.ru (503); raexp.ru (certificate mismatch); ncaor.gov.in (certificate mismatch; ncpor.res.in read instead, a separate official host); pmge.ru (TLS error); rhc.ru (certificate error); polarforskningsportalen.se (certificate error); core.ac.uk and search.isc.ac (HTML or SSL error); xnatmap.org (DNS failure); openaltimetry API (404; replaced by SlideRule, a different public service).

**No slang was found, so no slang file was written. No search was refused by the search tool, so no STOP note was needed.**

Finished 2026-10-29. Scratch data and scripts: the session scratchpad `unitF/` (`scripts/`, `dl/`), session-only.
