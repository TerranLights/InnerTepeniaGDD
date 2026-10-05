<!-- Verbatim agent report, 2026-10-04 (NSIDC, ERA5 via Open-Meteo, AWI moorings, NEC-2, VOACAP, P.533). Model output: spot-check before relying on it. The agent ran out of web-search budget before its last two queries (list in the log). -->

# Weddell Sea floating-relay evidence report (research only, no project files edited)

**Bottom line.** No Weddell Sea region offers waters calm enough for an ordinary ship to float for weeks, and none is both calm and safe from ice. The water is calm only inside the consolidated pack, where ice damps swell, and there the ice itself drifts, ridges and crushes ships. In open water the sea is not calm. The sheltered ice-shelf-front strip is the one exception. It is open for a short summer window, and ships have needed icebreaker help to reach it.

The ship classes that have survived months in the Weddell or Arctic pack are ice-class icebreakers frozen in (Polarstern) or purpose-built ships (Fram). Endurance, a wooden ice-strengthened ship, was crushed. Surface moorings are not used in the Weddell ice zone. Fixed moorings keep their top instrument at about 150 m depth. "Hydroelectric" power is not physically sensible on a platform that drifts with the water or ice. Wind plus battery plus diesel is the only workable power mix.

A floating relay buys little radio performance. Against the direct hop, the limiting-leg median best-band SNR changes by about -2 to +6 dB (ITU-R P.533) or -1.5 to +12 dB (VOACAP). The direct hop is already 24/24 h at 1 kW or at +6 dBi.

**Conventions.** Access date for every source is 2026-10-04. "(calc)" is my own calculation and "(inf)" is my inference. "UNVERIFIED" means the fact was seen only in a search-result summary. Source numbers [S#] are in the table at the end. All scratch data live under `/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/e4d51707-727a-4f11-a99d-7863a3fbdd42/scratchpad/` (hereafter SP).

---

## 1. Weddell Sea physical environment

### 1.1 Data products I actually pulled
- **NSIDC Sea Ice Index v4 [S1, S2].** I downloaded the regional monthly workbook and all monthly 25-km concentration GeoTIFFs for 1979-2025. I sampled concentration at 12 points (SP/w/nsidc/conc_out.txt).
  - Reading check (calc): my sector sum gives 0.99 M km² for Feb 2025 against the workbook's 1.03. Sep 2025 gives 7.02 against 6.70, because my 60W-20E box differs from the NSIDC region mask.
  - The GeoTIFF scaling (0-1000 = tenths of percent; 2530/2540 flags) is my inference. The NSIDC landing page does not state it [S3].
- **ERA5 waves and wind.** I pulled ERA5-Ocean waves and ERA5 atmosphere hourly for 2013-2022 at 10 points through the Open-Meteo API [S4, S5]. The cell size is 0.5° (about 50 km). I do not have a Copernicus CDS account, so this is ERA5 data via a third-party API.
  - ECMWF's wave model (ecWAM) simulates waves only up to 30% sea-ice cover and sets them to 0 beyond that [S6]. This is the operational model description. I infer ERA5 inherits it, because the nulls in my series behave that way.
  - "Waves-valid %" below is therefore a proxy for hours with sea-ice cover of 30% or less.
- **ETOPO1 depths** via NOAA ERDDAP [S7]. They are uncertain on the Weddell shelf (see the E1 note in 1.7).
- **AWI current-meter moorings** from PANGAEA [S12] and the AWI sea-ice upward-looking-sonar array [S9].

### 1.2 Region-by-season table
SIC is the NSIDC monthly mean concentration (1979-2025), averaged over the season's months. Waves-valid % is the share of ERA5 hours with waves not ice-masked. Hs is the significant wave height when valid, shown as mean/P99. Wind is the 10-m speed, mean/P99, for DJF then JJA. T2m is the 2-m temperature for DJF then JJA. Seasons: DJF = Dec-Feb, MAM = Mar-May, JJA = Jun-Aug, SON = Sep-Nov. The source file is SP/w/era5/season_table.txt.

| Point | SIC % DJF/MAM/JJA/SON | Waves-valid % DJF/MAM/JJA/SON | Hs m, DJF; MAM | Wind m/s, DJF; JJA | T2m °C, DJF; JJA |
|---|---|---|---|---|---|
| N1 (-60,-45) Scotia Sea edge | 1/2/35/18 | 99/95/37/69 | 2.4/5.0; 2.9/5.7 | 8.4/16.1; 8.9/17.9 | +0.8; -4.8 |
| N2 (-62,-35) N Weddell | 18/19/80/73 | 68/70/1/2 | 2.2/4.5; 2.8/5.7 | 7.6/15.5; 8.4/17.8 | -0.6; -10.9 |
| A (-66,-45) | 46/58/91/84 | 34/26/0/0 | 1.6/3.9; 1.8/4.2 | 6.5/14.6; 7.5/16.8 | -1.2; -15.0 |
| D (-68,-30) E Weddell | 30/49/93/89 | 63/42/0/0 | 1.6/4.1; 2.2/5.0 | 6.3/15.0; 7.3/16.1 | -1.3; -18.6 |
| W2 (-65,-52) off Peninsula | 64/77/92/84 | 16/6/0/1 | 1.8/4.3; 1.9/4.0 | 6.1/14.4; 7.3/18.0 | -0.9; -13.6 |
| B (-70,-45) mid-Weddell | 85/89/97/94 | 3/1/0/0 | rare hours only | 5.8/13.9; 6.6/15.7 | -1.9; -20.4 |
| C (-72,-40) S Weddell | 84/89/97/95 | 4/0.2/0/0 | rare hours only | 5.5/13.7; 6.5/15.3 | -2.2; -21.9 |
| W1 (-74,-50) SW pack | 92/96/96/95 | 0/0/0/0 | none | 5.2/12.7; 6.2/15.2 | -3.2; -23.6 |
| R1 (-75,-60) Ronne front | 55/64/66/64* | 0 | none | 5.5/14.0; 6.9/18.4 | -6.3; -27.5 |
| H1 (-75,-27) Brunt coast | 20/69/83/72 | 60/3/0/5 | 0.6/2.5; 0.8/3.5 | 5.5/14.8; 6.8/18.2 | -2.8; -20.6 |

\*R1's 25-km pixel is probably contaminated by the shelf or coast, so its concentration is understated.

Maximum hourly values (SP/w/era5/stats.txt):
- Hs reached 9.3 m at D in March and 10.8 m at N2 in March.
- Wind reached 17-30 m/s at all points, and 30.1 m/s at R1 in September.

### 1.3 Sea ice
- **Extent.** NSIDC Weddell sector extent in M km², 1979-2025 [S1] (calc from workbook; the spurious "1978" row, which holds Nov/Dec values, is excluded):

| Month | Mean | Min (year) | Max (year) |
|---|---|---|---|
| Jan | 1.89 | 0.84 (1988) | 3.11 (2015) |
| Feb | 1.29 | 0.85 (1999) | 2.16 (2014) |
| Mar | 1.55 | 0.99 (1981) | 2.35 (2015) |
| Apr | 2.40 | 1.72 (2023) | 3.36 (2015) |
| May | 3.63 | 2.59 (2023) | 4.79 (1988) |
| Jun | 4.90 | 3.69 (2023) | 6.05 (1988) |
| Jul | 5.86 | 4.82 (2023) | 6.79 (1988) |
| Aug | 6.44 | 5.54 (2023) | 7.37 (1980) |
| Sep | 6.65 | 6.03 (2023) | 7.68 (1980) |
| Oct | 6.37 | 5.52 (2023) | 7.43 (1980) |
| Nov | 5.73 | 4.64 (1988) | 6.49 (1980) |
| Dec | 4.08 | 3.16 (2016) | 5.13 (2011) |

- **Perennial ice.** The Weddell holds about 10⁶ km² of perennial ice, about 40% of Antarctic summer sea-ice area. It lies in the northwest Weddell along the Peninsula, because of the semi-enclosed basin and the clockwise gyre [S8]. W1 is 90-98% covered in every month.
- **Thickness.**
  - The thickest ice is in the dynamic boundary regions of the gyre [S9].
  - The AWI sonar draft at the Peninsula tip fell by more than 1 m between 1996-97 and 2006-07 [S9].
  - Ship-based observations recorded ice thicker than 3.0 m [S8].
  - UNVERIFIED search snippet: mean thickness 2.6-5.4 m in the northwest Weddell, increasing from the Antarctic Sound toward Larsen B.
  - The ISW floe was 1.5 x 2 km and 1-2 m thick on average [S14].
- **Ice drift.**
  - ISW drifted 11 Feb to 9 Jun 1992 at 6.2 km/day, about 670 km, from 71°48'S 51°43'W to 65.63°S 52.41°W [S13].
  - Endurance's chord, beset to abandoned (calc from [S15]), was 1,053 km in 281 days, or 3.75 km/day.
  - UNVERIFIED search snippets: Kottmeier and Sellmann (1996) find geostrophic currents of about 6 cm/s along the western and northwestern shelf breaks, and daily ice-drift rates up to 0.9 m/s in the central-western pack.
  - Drift-time estimates (calc, chord distances, at 3.75-6.2 km/day):

| Leg | Chord | Time |
|---|---|---|
| Endurance start (-76.6,-31.5) to the Peninsula tip | 1,730 km | 280-460 days |
| ISW end to the Peninsula tip | 316 km | 51-84 days |

  - Endurance herself: beset 19 Jan 1915; crushed and abandoned 27 Oct 1915; sank 21 Nov 1915. The floes then carried the crew north until the boats were launched on 9 April 1916 [S15].
- **Marginal ice zone (MIZ).** UNVERIFIED (Wahlgren, Thomson, Biddle, Swart): 2019 SWIFT buoys, open water to more than 200 km into the ice.
  - Swell attenuation coefficient alpha was 4e-6 to 7e-5 per m in spring, and about five-fold larger in winter.
  - The e-folding distance 1/alpha is therefore (calc) 250 to 14 km in spring, and about 50 to 3 km in winter.
  - ECMWF acknowledges ice-wave interaction is not in the older model approach [S6].
- **Fast ice and the ice front.** A largely immobile ice mélange between the Filchner-Ronne front and a grounded iceberg shapes polynyas [S43].

### 1.4 Open-water reach, by month (calc)
This is the southernmost latitude reached by a contiguous open path (concentration under 15% in at least 50% of years). It is from SP/w/nsidc/open_water.txt.

| Month | 60W | 45W | 35W | 25W | 15W | 0 |
|---|---|---|---|---|---|---|
| Dec | 63.8S | 62.0S | none | none | none | none |
| Jan | 63.8S | 64.0S | 67.2S | 70.2S | 70.5S | 69.0S |
| Feb | 63.8S | 67.2S | 71.0S | 73.5S | 71.8S | 69.2S |
| Mar | 63.8S | 66.0S | 68.8S | 71.0S | 71.0S | 69.2S |

- The share of the 5.35 M km² sector (60W-20E, 60-80S) that is open in at least 50% of years is 4.21 M km² in Feb, 3.81 in Mar, 3.59 in Jan, and 0.60 in Dec.
- "Open" here includes the ordinary ocean north of 65S. It is not all pack interior.
- Probability of ice at each candidate point (SP/w/nsidc/conc_out.txt):

| Point | Month | P(conc ≥15%) |
|---|---|---|
| A (-66,-45) | Jan | 83% |
| A | Feb | 36% |
| A | Mar | 45% |
| A | Apr | 94% |
| D (-68,-30) | Jan | 41% |
| D | Feb | 11% |
| D | Mar | 28% |
| D | Apr | 79% |
| B (-70,-45) | Feb | 91% |
| C (-72,-40) | Feb | 98% |
| W1 (-74,-50) | Feb | 98% |

### 1.5 Waves, storms, katabatic winds, polynyas, icing, darkness
- **Waves.** Open water is not calm. The numbers are in 1.2 and in the wave-energy table in section 3.
  - The only sheltered open-water cell is H1 in front of the Brunt ice shelf. ERA5 gives DJF Hs of 0.6 m mean and 2.5 m P99, with a 3-4 s period (fetch-limited wind sea). It is ice-free 60% of DJF hours.
  - H1's 0.5° ERA5 cell is coarse (inf).
- **Cyclones and low-level jets.** I have only UNVERIFIED leads.
  - 286 mesoscale vortices were counted in 346 summer days (1989-90) in the coastal eastern Weddell, about 0.83 per day.
  - Katabatic low-level jets are typically 10-20 m/s.
  - My ERA5 10-m wind P99 is 12.7-19.6 m/s at the ice points.
- **Polynyas.**
  - Maud Rise polynya: about 9,500 km² in mid-September 2017, growing to about 80,000 km² by late October [S42]. It was caused by cyclonic winds plus Weddell Gyre flow over the rise. The 1970s Weddell polynya was seen on satellite imagery.
  - Polarstern penetrated nearly to the Dronning Maud Land coast in the 1986 winter project and failed to find the polynya [S22]. So the polynya is not a reliable open-water site.
  - Coastal polynyas cover about 2% of the southern Weddell shelf area but produce 17% of its sea ice [S43]. The largest are at the Ronne and Brunt ice shelves.
  - 70% of the ice made on the southern shelf is exported [S43].
- **Icing.** Ship icing in the Southern Ocean is real, about 13 mm/h in extreme events. This is UNVERIFIED (search summary of a ship-icing source).
- **Fog.** Not found.
- **Darkness (calc, solar geometry).** Polar-night days per year: 0 at 64S, 27 at 68S, 55 at 70S, 75 at 72S, 104 at 76S. Midnight-sun days: 28 at 66.5S and 67 at 70S.

### 1.6 Icebergs
- A-68 calved July 2017 from Larsen C at nearly 5,800 km², with a mean thickness of 235 m. It was tracked to the Scotia Sea and South Georgia and disintegrated by January 2021 [S44].
- A-74 (Feb 2021, about 1,270 km²) and A-81 (23 Jan 2023, about 1,550 km² and about 150 m thick) calved from Brunt [S45]. A-83 calved 20 May 2024 at 380 km² [S46].
- A-23A calved in 1986 at about 4,000 km² from Filchner-Ronne. It stayed grounded until 2020, drifted from late 2023, and reached South Georgia in May 2025. It was about 1,000 km² by 20 Dec 2025 [S47].
- AWI keeps its top sonar at about 150 m depth specifically "to avoid... damage by passing icebergs" [S9]. Berg drafts are therefore the design constraint on moorings.
- UNVERIFIED: 415 icebergs from 3.4 to 3,612 km² were tracked in the eastern Weddell "iceberg alley".

### 1.7 Currents, tides, depth
- **Gyre.** Total gyre transport is 29.5 Sv, about 90% in the boundary currents, with an interior anticyclonic cell under 4 Sv [S11].
  - Altimetry and GLORYS give time-mean surface speeds of 4-6 cm/s for the Antarctic Slope Front, Weddell Front and Inner Weddell Current [S10].
  - Synoptic measurements are higher: 20 cm/s (ASF) and 10 cm/s (WF) [S10, citing Thompson and Heywood 2008].
  - Full-depth transport is 40 ± 0.6 Sv in autumn and 33.8 ± 3.0 Sv in summer [S10].
- **Moored current meters** (S12, PANGAEA, CC-BY-3.0; speeds are my statistics, SP/w/pangaea_currents.txt):

| Mooring | Depth | Mean | P95 | Max | Residual |
|---|---|---|---|---|---|
| AWI211 (-70.49,-13.12), 1989-90 | 247 m | 9.2 cm/s | 17.1 | 28.7 | 8.4 |
| AWI211 | 2,066 m | 2.6 | 6.0 | 10.5 | 2.2 |
| FR-2 (-75.04,-33.56), 1995-97 | 191 m | 9.7 | 19.1 | 43.2 | 3.0 |
| FR-2 | 554 m | 7.6 | 15.8 | 55.6 | 1.1 |
| FR-3 (-77.00,-49.02), 1995-97 | 203 m | 12.7 | 25.3 | 43.2 | 2.0 |

  The shelf records are tidal and oscillating, with small residuals.
- **Tides.** Filchner-Ronne tides exceed 3 m peak-to-peak and give peak currents up to about 1 m/s under the ice shelf. These are UNVERIFIED search snippets. The Rosier and Gudmundsson paper [S52] handles tidal current drag, but I did not extract numbers. Open-shelf maxima at the moorings are 0.43-0.56 m/s.
- **Depth** (ETOPO1 via ERDDAP [S7]; shelf values uncertain):

| Point | Depth |
|---|---|
| A (-66,-45) | 4,277 m |
| B (-70,-45) | 3,746 m |
| C (-72,-40) | 3,343 m |
| D (-68,-30) | 4,626 m |
| N1 (-60,-45) | 5,298 m |
| G1 (-71.8,-51.7) | 1,551 m |
| G2 (-65.8,-52.4) | 2,356 m |
| Maud Rise (-65,3) | 2,023 m |
| E1 (-76.6,-31.5) | 321 m |

  - ETOPO1 gives 321 m at E1, but Shackleton sounded 312 fathoms (about 570 m, calc) there [S15]. Treat shelf values as rough.
  - The Endurance wreck lies at 3,008 m (UNVERIFIED).

---

## 2. Precedents for long-duration platforms

| Platform | Duration and where | Power, crew, comms | Outcome and failure modes | Source |
|---|---|---|---|---|
| **Endurance** (wooden barquentine, 1915) | beset 19 Jan 1915, abandoned 27 Oct, sank 21 Nov | no powered comms; wireless rigged "in the hope of hearing" signals | crushed by pressure; stern post and rudder torn; crew survived on floes to 9 Apr 1916 | [S15] |
| **Fram** (1893-96, Arctic) | in ice about 3 years | 13 men | survived; hull shape let ice lift the ship; stores moved onto the ice in Jan 1895 | [S18] |
| **Maud** (1922-25, Arctic) | locked in ice more than 2 years | not found | rounded hull "extremely solid" | [S19] |
| **NP-1** (1937-38, Arctic floe) | 274 days, 4 men, camp dismantled 19 Feb 1938 | radioman Krenkel (UNVERIFIED) | 2,100 km drift (JOR abstract); 2,850 km (search snippet, flagged) | [S20] |
| **T-3 Fletcher's Ice Island** | 1952-1979, abandoned 1974, melted near Greenland 1983 | more than 40 people at peak; huts, runway | thickness fell 132 ft (1954) to 99 ft (1964) | [S21] |
| **Ice Station Weddell 1992** | 11 Feb-9 Jun 1992; 6.2 km/day | 32 people (17 US, 15 Russian); temperatures to -36 °C | recovered by N.B. Palmer near 65.8°S; floe 1.5 x 2 km | [S13, S14] |
| **MOSAiC / Polarstern** | 389 days; about 357 days drifting; floe 2.5 x 3.5 km at start, then "floe 2.0" (400 x 500 m) | 15 t diesel/day drifting, 54 t/day under way; about 7,137 t total (plan); 105 crew + 337 scientists; 7 ships | about €200k/day; Kapitan Dranitsyn reached the ship 13 Dec and 28 Feb after fuel strain (UNVERIFIED) | [S16, S17] |
| **Polarstern, Winter Weddell Sea Project 1986** | 27 Jun-14 Dec 1986 in two cruises | 137 scientists | reached nearly to the Dronning Maud Land coast; did not find the Weddell polynya | [S22] |
| **AWI Weddell moorings (HAFOS)** | about a dozen hydrographic moorings over 30 years; instruments designed for up to 3-year deployments | sonar tops at about 150 m depth | success rate 86% (1990-95); failure rate about one third (1996-2008) from flooded instruments or lost moorings | [S9, S24] |
| **Polar Argo floats** | 1,026 deployed south of 60S, 216 active (June 2020) | autonomous | early Weddell survival about 40% from antenna ice damage; ice-sensing floats about 80% (UNVERIFIED) | [S23] |
| **Saildrone SD1020** | 19 Jan-3 Aug 2019, 196 days, 22,000 km | wind-driven; solar | survived 15 m waves, 130 km/h wind; iceberg collision 5 Apr damaged sensors; two companions returned early | [S25] |
| **MetOcean Spotter buoys** | 5 deployed Feb 2018; more than 6,500 km in a year | solar | all 5 survived; hibernate in extended darkness | [S26] |
| **Wave Glider (Drake Passage)** | four-month mission | solar | the "solar charging limits to Oct-Feb" statement is UNVERIFIED | [S27, S28] |
| **OOI Southern Ocean Array** | 54.08S 89.67W, 4,800 m; Feb 2015-Jan 2020 | surface mooring plus gliders | removed 15 Jan 2020 | [S29] |
| **OOI Irminger Sea surface buoy** | lost 12 Oct 2017 | n/a | not found by aerial search 26 Oct; cause unknown | [S30] |
| **NOAA Papa PA002 surface buoy** | deployed June 2008 | n/a | went adrift 11 Nov 2008 on a line break at the bridle; subsurface data lost | [S31] |
| **Halley VI resupply** | a window of "two to three weeks" in late December | n/a | by mid-January "last remnants have normally melted" (Wayback copy of the Ingenia article) | [S40] |
| **Neumayer III resupply 2007-08** | arrived 16 Dec 2007; reached ice edge 16 Jan 2008 | n/a | blocked by several metres of ice; Polarstern needed days of icebreaking | [S41] |

Notes:
- Ordinary ships do not survive in the pack. Of the pack-wintering ships above, the ones that lasted were Polarstern, which is purpose-built, and Fram. Wooden Endurance was crushed.
- OWS Mike/Polarfront (Station M, 66N 2E, 1948-2009) is UNVERIFIED and I found no crew-rotation data.
- A floating HF relay precedent in Antarctica was not found. See the search log.

---

## 3. Power: what water-driven generation can and cannot do

### 3.1 Hydrokinetic (calc)
P = 0.5 ρ v³ A Cp, with ρ = 1027 kg/m³ (assumed) and Cp = 0.35 (assumed). The Betz limit is 0.593.

| v (m/s) | Flux (W/m²) | 1 m² (W) | 5 m² (W) | 20 m² (W) | 20 m² at Betz (W) |
|---|---|---|---|---|---|
| 0.05 | 0.064 | 0.02 | 0.11 | 0.45 | 0.76 |
| 0.10 | 0.514 | 0.18 | 0.90 | 3.59 | 6.09 |
| 0.20 | 4.11 | 1.44 | 7.19 | 28.8 | 48.7 |
| 0.50 | 64.2 | 22.5 | 112 | 449 | 761 |
| 1.0 | 513 | 180 | 899 | 3,595 | 6,090 |

- To get 50 W continuous you need (calc) about 278 m² at 0.1 m/s, about 35 m² at 0.2 m/s, and about 2.2 m² at 0.5 m/s.
- A platform that drifts with the water or ice sees no relative flow. That is the physics. The only relative flow is shear (a drogue or deep turbine below an ice floe). I found no published value for it (inf: 0.05 m/s or less).
- **Measured Weddell currents** (S12, hourly moorings):
  - The time-mean kinetic flux <0.5ρv³> is 0.7-2.1 W/m² at about 200-250 m depth. The highest is 2.06 W/m² at FR-3, 203 m.
  - The speed never reached 0.5 m/s at the shelf instruments. Maxima are 0.43-0.56 m/s.
  - Mean output for a 5 m² rotor (calc, Cp 0.35, no cut-in) is 1.3-3.6 W, and for 20 m² it is 5-14 W.
  - Deep-water flux is 0.03-0.3 W/m² (AWI211, 900-2,300 m).
- **Real current turbines.** IHI Kairyu is rated about 100 kW at 1.5 m/s with about 11 m rotors, in the Kuroshio at 30-50 m depth [S32]. My check (calc) is 0.5 x 1027 x 1.5³ x 190 m² x 0.3 ≈ 99 kW, consistent. ORPC RivGen produced more than 8 MWh in its first 10 months and survived frazil ice in the Kvichak River, but the rating and capacity factor are not stated in the source [S33]. I found no polar-sea current-turbine demonstration. See the search log.

### 3.2 Wind (calc, ERA5 10 m, 2013-2022)
Turbine: A = 2 m² swept, Cp = 0.30, cut-in 3 m/s, rated at 12 m/s (about 695 W at ρ = 1.34), cut-out 25 m/s. Mean electrical watts, with no icing derate (SP/w/era5/wind_power.txt):

| Point | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | Annual |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A (-66,-45) | 131 | 197 | 241 | 251 | 244 | 230 | 232 | 249 | 285 | 201 | 222 | 179 | 222 |
| B (-70,-45) | 102 | 152 | 168 | 200 | 179 | 182 | 178 | 183 | 220 | 168 | 190 | 142 | 172 |
| C (-72,-40) | 81 | 146 | 173 | 177 | 162 | 177 | 190 | 152 | 208 | 149 | 176 | 120 | 159 |
| D (-68,-30) | 131 | 194 | 266 | 253 | 232 | 213 | 231 | 216 | 265 | 210 | 217 | 145 | 214 |
| N1 (-60,-45) | 243 | 327 | 355 | 372 | 344 | 306 | 329 | 334 | 401 | 335 | 345 | 289 | 331 |
| W1 (-74,-50) | 80 | 127 | 116 | 162 | 170 | 161 | 168 | 153 | 184 | 133 | 135 | 99 | 140 |

- Longest run of 10-m wind under 5 m/s over 10 years (calc): 6.2 days at A, 7.3 at B, 8.5 at C, 5.9 at D, 10.7 at W1.
- Wind is the only continuous resource. It needs storage for 6-11 days (battery) plus a generator.

### 3.3 Solar (ERA5 shortwave, 2019-2021; SP/w/era5/solar_wind.txt)
Mean daily horizontal insolation in kWh/m²/day:

| Point | Dec | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A (-66,-45) | 6.65 | 5.59 | 3.71 | 1.84 | 0.75 | 0.16 | 0.01 | 0.08 | 0.61 | 1.97 | 4.16 | 5.94 |
| B (-70,-45) | 7.34 | 6.02 | 3.60 | 1.89 | 0.57 | 0.04 | 0.00 | 0.00 | 0.35 | 1.61 | 3.82 | 6.22 |
| C (-72,-40) | 7.45 | 6.30 | 3.34 | 1.76 | 0.44 | 0.01 | 0.00 | 0.00 | 0.23 | 1.42 | 3.67 | 6.21 |
| D (-68,-30) | 6.44 | 5.67 | 3.38 | 1.60 | 0.51 | 0.07 | 0.00 | 0.03 | 0.50 | 1.77 | 3.92 | 5.60 |

- Cloud cover is 74-95%. At B, C and D there is essentially no sun for roughly May to July. This is ERA5 modeled radiation, not measured.
- A 1 m² panel at 20% (assumed) yields about 1.3 kWh/day in Dec-Jan, about 0.37 kWh/day in March, and about zero in winter.

### 3.4 Waves (calc)
P = ρg²Hs²Te/(64π), about 0.49 Hs² Te kW per metre of crest, with ERA5 wave period taken as Te (assumption). Ice-masked hours count as 0. Mean kW/m by season (SP/w/era5/wave_power.txt):

| Point | DJF | MAM | JJA | SON | Annual |
|---|---|---|---|---|---|
| N1 (-60,-45) | 27.6 | 37.3 | 17.5 | 29.8 | 28.0 |
| N2 (-62,-35) | 14.7 | 24.7 | 0.2 | 0.7 | 10.1 |
| A (-66,-45) | 3.5 | 3.6 | 0 | 0 | 1.76 |
| D (-68,-30) | 6.9 | 9.5 | 0 | 0 | 4.09 |
| B (-70,-45) | 0.11 | 0.02 | 0 | 0 | 0.03 |
| H1 (-75,-27) | 0.83 | 0.07 | 0 | 0.22 | 0.28 |

The energy is where the platform gets destroyed, and essentially none exists in the pack where it is calm.

### 3.5 Diesel, batteries, transmitter loads (calc)
Assumptions: diesel 36 MJ/L, genset efficiency 25%, battery 80% usable, LiFePO4 100 Wh/kg, lead-acid 25 Wh/kg.

| Mean load | Diesel | 14-day no-sun battery |
|---|---|---|
| 10 W | 0.10 L/day, 35 L/yr | 4.2 kWh; Li 42 kg; PbA 168 kg |
| 50 W | 0.48 L/day, 175 L/yr | 21 kWh; Li 210 kg; PbA 840 kg |
| 100 W | 0.96 L/day, 350 L/yr | 42 kWh; Li 420 kg; PbA 1,680 kg |
| 250 W | 2.4 L/day, 876 L/yr | 105 kWh; Li 1,050 kg; PbA 4,200 kg |

A 1 kW transmitter at 45% efficiency (assumed) draws 2.2 kW DC peak. Mean DC power including 15 W for receiver and controller:

| Duty | Mean DC |
|---|---|
| 1% | 37 W |
| 5% | 126 W |
| 10% | 237 W |
| 25% | 571 W |

Cold derating of batteries is not quantified here (inf).

### 3.6 Anchoring, drift, ships
- **Anchoring.** Deep moorings are routine: ocean observatories moor in about 4,800 m [S29]. The AWI array keeps the top instrument at about 150 m to avoid icebergs [S9]. Candidate depths are 3,300-4,600 m. No surface-expressing mooring in the Weddell ice zone was found (inf from [S9, S24]).
- **Gyre drift.** See 1.3: 3.75-6.2 km/day.
- **Ship fuel.**
  - MOSAiC Polarstern burned 15 t/day drifting and 54 t/day under way (planning figures) [S17].
  - RRS Sir David Attenborough: 19,000 nm at 13 kn, endurance up to 60 days, 660 m³ fuel (calc 19,000 / 13 kn / 24 = 61 days; consistent), Polar Class 4, icebreaking 3 kn in 1 m ice [S35].
  - I found no DP fuel figure and no small-vessel hotel-load figure (search budget exhausted; see the search log).
- **Nuclear.** RITM-200: 175 MWt, 60 MW at the propellers, refuel once every seven years, 40-year life [S34]. This is a technology note only. Treaty Article V prohibits nuclear explosions and radioactive-waste disposal in Antarctica; it does not mention reactor ships [S36].

---

## 4. Radio physics of a floating relay

### 4.1 Antenna over seawater versus ice (calc)
NEC-2 (PyNEC 2.3.4), a quarter-wave monopole with radials, Sommerfeld ground. Gain in dBi includes ground loss (SP/ant/mono_results.txt, mono_rock.txt).

| Ground | f (MHz) | Radials | Gain at 5° | at 10° | at 20° |
|---|---|---|---|---|---|
| Sea water (ε80, 5 S/m) | 3.5 | 16 | +4.6 | +4.7 | +4.2 |
| Sea water | 7.1 | 16 | +4.4 | +4.6 | +4.1 |
| Sea water | 14.2 | 16 | +4.1 | +4.4 | +4.0 |
| Ice sheet (ε3.2, 1e-5 S/m) | 7.1 | 16 | -9.6 | -5.1 | -1.9 |
| Ice sheet (3e-4 S/m) | 7.1 | 16 | -9.9 | -5.4 | -2.2 |
| Ice sheet (3e-4 S/m) | 7.1 | none | -13.5 | -8.9 | -5.8 |
| Rock (ε13, 0.002 S/m) | 7.1 | 16 | -7.3 | -3.4 | -1.0 |
| Average ground (ε15, 0.005 S/m) | 7.1 | 16 | -6.3 | -2.6 | -0.4 |

- The sea-water monopole is about 14 dB better than a monopole on an ice sheet at 5° elevation, and about 12 dB better than rock.
- Against a directional array at +6 dBi on the ice or rock site, the sea monopole has no advantage. The earlier modeling used 0 and +6 dBi.

**Thin ice over sea (calc, unvalidated).** Plane-wave far-field factor 20 log₁₀(|1+Rv|/2) relative to perfect ground (SP/ant/slab.txt):

| Surface | Frequency | Factor at 5° | at 10° | at 20° |
|---|---|---|---|---|
| Sea water | 7.1 MHz | -0.6 | -0.3 | -0.2 |
| 2 m ice (ε3.2, 1e-5) over sea | 3.5 MHz | -4.2 | -1.6 | -0.6 |
| 2 m ice over sea | 7.1 MHz | -9.0 | -4.6 | -1.9 |
| 2 m ice over sea | 14.2 MHz | -16.7 | -11.2 | -6.6 |
| 3 m sea ice (ε4.5, 0.05 S/m, ASSUMED) over sea | 3.5 MHz | -4.0 | -2.2 | -1.1 |
| 3 m sea ice (ε4.5, 0.05 S/m, ASSUMED) over sea | 7.1 MHz | -5.4 | -3.0 | -1.6 |
| 3 m sea ice (ε4.5, 0.05 S/m, ASSUMED) over sea | 14.2 MHz | -7.2 | -4.1 | -2.2 |

A few metres of ice over seawater does not behave like seawater at 7-14 MHz. The thin-dielectric-layer mechanism is confirmed qualitatively by [S49]. I found no HF-range conductivity for sea ice (see the search log), so the sea-ice constants are assumptions.

### 4.2 Ground-wave range (NTIA LFMF/GRWAVE, lf_test; calc)
Distance in km to reach +10 dBµV/m, with a vertical monopole.

| f | Power | Sea water | Sea ice (0.01 S/m, ASSUMED) | Ice sheet (3e-4) |
|---|---|---|---|---|
| 2.5 MHz | 100 W | 819 | 150 | 47 |
| 3.5 MHz | 100 W | 736 | 112 | 40 |
| 3.5 MHz | 1 kW | 891 | 164 | 67 |
| 7.1 MHz | 100 W | 545 | 57 | 31 |
| 7.1 MHz | 1 kW | 656 | 90 | 51 |

This reproduces your established 735 km for 3.5 MHz at 100 W over sea. A patent claims MF guided-wave coupling over sea ice at about 500 kHz with a seawater-grounded wire [S50]. That is a claim, not a measured result.

### 4.3 Geometry and geomagnetic latitude
AACGM-v2 at 110 km altitude, epoch 2026-10-01 (aacgmv2 2.7.1), and a centered-dipole value for a pole at 80.8 degrees, 287.2 E (equivalent to the south geomagnetic pole 80.8 S, 107.2 E). Distances are WGS84 geodesic in km (calc).

| Candidate | AACGM lat | Dipole lat | to PEN | to BEL | to HAL | to NEU | to SL |
|---|---|---|---|---|---|---|---|
| FA (-66,-45) | -53.9 | -57.6 | 753 | 1,367 | 1,253 | 1,572 | 1,437 |
| FB (-70,-45) | -57.1 | -61.6 | 940 | 932 | 864 | 1,361 | 1,152 |
| FC (-72,-40) | -59.1 | -63.8 | 1,220 | 673 | 576 | 1,130 | 891 |
| FD (-68,-30) | -57.0 | -60.6 | 1,429 | 1,111 | 854 | 901 | 831 |
| E1 (-76.6,-31.5) Endurance beset | -63.4 | -68.8 | 1,736 | 161 | 174 | 973 | 656 |
| G1 (-71.8,-51.7) ISW start | -58.2 | -63.0 | 940 | 834 | 884 | 1,531 | 1,276 |
| G2 (-65.8,-52.4) ISW end | -53.1 | -57.0 | 424 | 1,467 | 1,425 | 1,858 | 1,687 |
| Targets | PEN -51.0 | BEL -64.2 | HAL -62.9 | NEU -61.2 | SL -62.2 | | |

- Direct hop from the Peninsula centroid (-64.0,-60.3): BEL 1,774 km, HAL 1,785, SL 2,089, NEU 2,275.
- The sites span AACGM -51 to -64 and sit near the equatorward edge of the quiet auroral oval at the high end (inf). VOACAP and P.533 do not model storms or polar-cap absorption well, so their results are best-case for those events.

### 4.4 Results
Run in the scratchpad VOACAP (voacapl) and ITURHFProp (P.533) set-up. VOACAP columns were read with the extra leading MUF-column offset. The parser was validated against the earlier fixed legs: 5 test keys matched exactly, and P.533 hours match within a coordinate rounding of 1 h.

- All combinations are in `SP/fl/*.json`.
- Summaries: `SP/fl_summary.txt` (all 39 legs, all conditions), `SP/fl_table.txt`, `SP/fl_chain.txt`, `SP/fl_snr.txt`, `SP/fl_bands.txt`.
- Conditions run: Jan and Jul; SSN 5, 60, 160; 100 W, 10 W, 1 kW; 0 and +6 dBi; quiet-rural and rural noise; voice and digital.

Hours per 24 h usable on any band, "VOACAP/P533". Column order is [Jan SSN5, Jan SSN160, Jul SSN5, Jul SSN160]. Digital means VOACAP 15 dB-Hz required and P.533 -20 dB required.

| Leg | d km | 100 W 0 dBi voice | 1 kW 0 dBi voice | 100 W 0 dBi digital |
|---|---|---|---|---|
| Direct PEN-BEL | 1,774 | 8/24 7/24 24/17 24/15 | 24/24 all | 24/24 all |
| Direct PEN-HAL | 1,785 | 8/24 7/24 24/13 24/16 | 24/24 24/24... (see note) | 24/24 all |
| Direct PEN-SL | 2,089 | 4/24 5/23 24/11 19/8 | 24/24, one 23 | 24/24 all |
| Direct PEN-NEU | 2,275 | 0/24 2/23 19/9 14/6 | 21/24 21/24 24/22 24/24 | 24/24 all |
| FA to PEN | 753 | 24/24 24/24 24/23 24/21 | 24/24 all | 24/24 all |
| FA to BEL | 1,367 | 24/24 12/24 24/20 24/19 | 24/24 all | 24/24 all |
| FB to PEN | 940 | 24/24 22/24 24/21 24/19 | 24/24 all | 24/24 all |
| FB to BEL | 932 | 24/24 15/24 18/8 24/15 | 24/24 24/24 24/19 24/24 | 24/24 all |
| FB to HAL | 864 | 24/24 20/24 18/10 23/15 | 24/24 24/24 24/22 24/24 | 24/24 all |
| FC to PEN | 1,220 | 24/24 24/24 24/21 24/12 | 24/24 all | 24/24 all |
| FC to BEL | 673 | 24/24 24/24 18/12 24/17 | 24/24 24/24 18/19 24/24 | 24/24 24/24 18/24 24/24 |
| FC to HAL | 576 | 24/24 24/24 18/8 24/21 | 24/24 24/24 18/18 24/24 | 24/24 24/24 18/24 24/24 |
| FD to PEN | 1,429 | 23/24 12/24 24/16 24/5 | 24/24 all | 24/24 all |
| FD to BEL | 1,111 | 21/24 6/24 15/7 19/11 | 24/24 all | 24/24 all |
| G1 to PEN | 940 | 24/24 22/24 24/21 24/19 | 24/24 all | 24/24 all |
| G1 to BEL | 834 | 24/24 22/24 17/8 24/16 | 24/24 24/24 20/20 24/24 | 24/24 24/24 20/24 24/24 |
| G2 to PEN | 424 | 24/24 all | 24/24 all | 24/24 all |
| G2 to BEL | 1,467 | 20/24 9/24 24/16 24/20 | 24/24 24/24 24/22 24/24 | 24/24 all |
| E1 to PEN | 1,736 | 2/24 0/24 17/1 21/0 | 24/24 24/24 24/23 24/24 | 24/24 all |
| E1 to BEL | 161 | 24/24 24/24 8/6 24/21 | 24/24 24/24 8/12 24/24 | 24/24 24/24 8/24 24/24 |

Note for direct PEN-HAL at 1 kW 0 dBi voice: the four columns are 24/24, 23/24, 24/23, 24/24.

- **Remaining legs** (FA/FB/FC/FD/G1/G2/E1 to HAL, NEU, SL) are in `SP/fl_summary.txt`. SSN 60 is also there.
- **Strong links.** At 100 W with +6 dBi, or at 1 kW with 0 dBi, almost every leg is 24/24 by both models. That includes the direct hop. Exceptions:
  - Direct PEN-NEU is 21/24 in January.
  - Legs under about 700 km in July at SSN 5 give VOACAP 18 h/24 (FC to BEL, FC to HAL, G1 to BEL, E1 to BEL), even at 1 kW +6 dBi.
- **Model disagreement on the hard case** (100 W, 0 dBi, voice, quiet rural): for the direct PEN-BEL hop in January at SSN 5, VOACAP says 8 h and P.533 says 24 h. In July at SSN 5, VOACAP says 24 h and P.533 says 17 h.
- **Weak-signal digital** closes essentially all legs 24/24 by both models, including the direct hop at 100 W 0 dBi. Exceptions are the July SSN 5 short legs above.
- **Bands for the hard case** (100 W, 0 dBi, voice, SSN 60, at least 6 h/24; `SP/fl_bands.txt`):
  - Direct PEN-BEL in January: P.533 gives 3.5-14.2 MHz (VOACAP none). In July: VOACAP gives 2.5, 3.5, 5 and 7.1 MHz; P.533 gives 2.5, 3.5 and 5 MHz.
  - FB to PEN in January: 2.5-7.1 MHz (VOACAP) and 2.5-10.1 MHz (P.533). In July the bands collapse to 2.5-3.5 MHz.
- **Chain availability** (both legs usable in the same hour; `SP/fl_chain.txt`):
  - January, 100 W 0 dBi voice, SSN 5, PEN-BEL: direct is 8/24. Via FA, FB or FC it is 24/24 (VOACAP).
  - July, PEN-BEL: direct is 24/17. The relays degrade it: FB 18/7, FC 18/10, FD 15/6 at SSN 5.
- **Limiting-leg median best-band SNR gain over the direct hop** (SSN 60, 1 kW 0 dBi; relay minus direct; VOACAP/P.533, dB; excludes E1, where the relay is within 200 km of the target):

| Route | Jan | Jul |
|---|---|---|
| PEN-BEL | -- | -- |
| via FA | +3.0/+2.1 | +3.0/+2.5 |
| via FB | +9.5/+1.5 | +2.0/-0.1 |
| via FC | +5.5/+2.5 | +1.5/-0.1 |
| via FD | +3.0/+0.3 | -1.5/-2.1 |
| via G1 | +12.0/+2.2 | +2.0/+0.1 |
| via G2 | +2.5/+1.5 | +3.0/+1.9 |

  Across all four target routes (PEN to BEL, HAL, SL, NEU), P.533 gives -2.1 to +5.9 dB and VOACAP gives -1.5 to +12 dB. This matches your island-relay finding of only a few dB per leg. Beyond what the models say about Peninsula-to-Belgrano and the others, the relay's value is operational redundancy, not link budget (inf).

---

## 5. Feasibility, legal, logistical answer

**(a) Is there any sea area, in any season, where an ordinary ship can float for weeks to months?**
- The interior pack is wave-free for practical purposes. ERA5 waves are 0% valid in 3 of 4 seasons at W1, and the MIZ attenuates swell. But the pack is not calm ice: drift of 3.75-6.2 km/day, ridging, and pressure. The best-known ordinary-ship failure is Endurance.
- Open summer water north of about 65S is not calm. Mean Hs is 1.4-2.2 m, P99 is 4-5.7 m, and maxima are 9-11 m. It reverts to ice from April: P(≥15%) at A is 94% in April, and at D it is 79%.
- The one sheltered open-water strip is the coast in front of Brunt. ERA5 Hs there is 0.6 m (DJF mean). The window is short: late December, two to three weeks, and ships there have needed icebreaking [S40, S41].
- No region is calm and safe for an ordinary ship for months.

**(b) What class of platform survives where?**
- **Ice-class icebreaker frozen into drifting pack:** proven. MOSAiC Polarstern lasted 389 days (357 drifting) at 15 t/day, with six support ships. In the Weddell the precedent is ISW, a floe camp of 4 months.
- **Moored deep-sea buoy:** subsurface moorings work (AWI HAFOS), but with the top instrument at about 150 m and a failure rate of about one third. No surface mooring is used in the ice zone. In seasonally open northern water, surface moorings exist (OOI at 54S) but also fail (Irminger and Papa).
- **Autonomous surface vessel:** survives only in open water in summer (Saildrone 196 days). It cannot operate in the pack.
- **Grounded tabular berg or ice-shelf front:** has precedent (T-3 for 22+ years, A-23A grounded for decades) but is not a sea platform, and A-23A is now gone.

**(c) Endurance and resupply realism.**
- MOSAiC cost about €200k/day and needed six support ships.
- Winter Weddell resupply has no precedent. Even summer resupply to the coast needs an icebreaker.
- A 100 W average load needs 350 L/yr of diesel, or 42 kWh (420 kg Li) for a 14-day storm. These figures are small compared with the ship needed to carry them.

**(d) Best candidate regions and seasons.**
- A drifting platform in the western pack (G1 to G2, the ISW track) in about February to June: ice-class ship, 3.75-6.2 km/day.
- A site on the ice-shelf or coast side near Halley in late December to January.
- Radio-wise, FB (-70,-45) is geometrically the most balanced (940 km and 932 km to PEN and BEL), but it is 94-100% ice-covered in all seasons, so only an ice-based platform could sit there.
- In the Jan SSN 5 case, FA, FB and FC all lift the hard-case chain from 8 to 24 h. That benefit disappears with +6 dBi, 1 kW, or a digital mode.

**(e) What is simply impractical.**
- Hydrokinetic or "ice-drift" turbines: about 0 W at drift-relative flow, and 1-14 W at the strongest Weddell flows I could measure.
- Wave-energy converters in the pack, where there are no waves.
- Winter solar: essentially no sun May-July at B, C and D.
- Surface moorings in the ice zone: the AWI array deliberately has none.
- An ordinary ship wintering, or an unprotected ship anywhere in the pack.

**Legal and treaty paragraph.** The Antarctic Treaty applies south of 60S including ice shelves, but does not affect high-seas rights (Article VI) [S36]. Parties must give advance notice of expeditions by their ships and nationals (Article VII.5) [S36]. The Madrid Protocol makes environmental protection a fundamental consideration (Article 3), requires prior environmental impact assessment for activities (Article 8, Annex I), and has an Annex IV on marine pollution [S37]. CCAMLR applies south of 60S and to the area up to the Antarctic Convergence [S38]. The IMO Polar Code (in force 1 Jan 2017) applies under SOLAS and MARPOL to ships in polar waters, with Categories A, B and C [S39]. Article V prohibits nuclear explosions and radioactive-waste disposal in Antarctica [S36]. Radio licensing and ITU rules for a mobile floating station were not researched.

---

## Contradictions between sources

1. **Endurance beset longitude.** Shackleton's narrative gives 76°34'S 31°30'W for 19 Jan 1915. His appendix gives 37°30'W for the same position. His narrative gives the abandonment date as Wednesday 27 Oct, and his appendix gives 26 Oct. I used the narrative [S15].
2. **Weddell polynya years.** NASA and the search snippets give 1974-76. The Polar Record WWSP 1986 abstract says "1976-78" [S22, S42].
3. **NP-1 drift.** JOR abstract: 2,100 km in 274 days. A search snippet (which cites a Wikipedia lead): 2,850 km [S20].
4. **ISW drift.** LDEO page: 6.2 km/day, about 670 km. My chord gives 689 km and 5.8 km/day [S13, calc].
5. **Direct PEN-BEL distance.** Your 1,766 km is spherical (R = 6371) with Peninsula at (-64.01,-60.26). Mine is 1,774 km on the WGS84 ellipsoid with (-64.0,-60.3). The spherical value with (-64.0,-60.3) is 1,768 km.
6. **VOACAP versus P.533.** They differ most on the hard case (100 W, 0 dBi, voice). The VOACAP "SNR" field is in dB-Hz and P.533's is in dB over 3 kHz, so they are not directly comparable.
7. **NASA Maud Rise coordinates.** The fetch returned "-66.96, 37.88E". Maud Rise is near 65S, 3E (my ETOPO check gave 2,023 m at (-65,3)). I treat the fetched coordinate as mis-extracted.
8. **Gyre speeds.** Time-mean 4-6 cm/s [S10], synoptic 10-20 cm/s [S10], mooring means 9-13 cm/s at 200 m (tidal) [S12]. These are different quantities, not a conflict.
9. **Sector extents.** My GeoTIFF sector sum (Sep 2025: 7.02) differs from the workbook (6.70) because the boxes differ. The workbook has a spurious "1978" row.

---

## Search log

**WebSearch strings run (in order), all returning only the summaries noted:**
1. Weddell Sea perennial sea ice western Weddell thickest multi-year ice ice thickness drilling
2. Weddell Sea significant wave height ERA5 climatology sea ice marginal ice zone wave attenuation
3. Ice Station Weddell 1992 drift track duration Russian American ice camp
4. Weddell Gyre current speed mooring Antarctic Slope Current Weddell Sea volume transport velocities
5. Endurance Shackleton drift track 1915 Weddell Sea pack ice drifted 1,186 miles crushed 27 October 1915 position
6. MOSAiC expedition Polarstern drift 2019-2020 fuel consumption power resupply icebreakers Akademik Fedorov Kapitan Dranitsyn logistics
7. Weddell Sea polynya 1974-1976 Maud Rise polynya reappeared 2016 2017 size area km2 open-ocean polynya
8. A-23A iceberg Weddell Sea grounded 2024 2025 drift track Southern Ocean disintegrating A23a
9. Kottmeier Sellmann 1996 atmospheric and oceanic forcing of Weddell Sea ice motion drifting buoys ice velocity cm/s
10. Weddell Sea ice drift buoy trajectories Antarctic Weddell Gyre ice velocity mean drift speed km/day western Weddell Sea ice export
11. Filchner-Ronne ice shelf front tides tidal currents amplitude m/s Padman tide model Ronne Filchner
12. AWI Weddell Sea moorings Perennial Acoustic Observatory PALAOA Weddell Sea mooring array upward looking sonar ice draft
13. MOSAiC Polarstern drift 389 days fuel tonnes bunkering Akademik Tryoshnikov how much fuel Polarstern consumed generators power
14. Saildrone Southern Ocean circumnavigation 2019 Antarctica 196 days 22,000 km Meinig results wind-driven solar-powered Southern Ocean Hs
15. Weddell Sea surface wave buoys SWIFT 2019 Polarstern marginal ice zone swell attenuation waves Weddell Sea observations significant wave height
16. Southern Ocean Flux Station SOFS mooring 46.7S survival deployments Southern Ocean surface mooring OOI Southern Ocean Array 54.5S failure recovered
17. Argo floats Southern Ocean sea ice detection ice-avoidance algorithm under-ice profiling Weddell Sea floats lifetime Wong Riser 2011 RAFOS
18. ice-tethered profiler Southern Ocean Weddell Sea ice buoy deployed 2019 AWI sea ice drifting buoy survival lifetime months Iridium
19. hydrokinetic turbine ice-covered river Alaska ORPC RivGen Kvichak River Igiugig capacity factor ice frazil
20. ocean current turbine Kuroshio Florida Current capacity factor demonstration KCAT Kyushu University Black Rock turbine power measured kW
21. OOI Global Southern Ocean Array 55S mooring surface mooring problems Irminger Sea Station Papa buoy broke free recovered wire rope failure
22. ocean weather ship Polarfront Station M on station endurance crew rotation weeks 66N 2E weather ship 1948 2009 history
23. Rosatom nuclear icebreaker Arktika refueling interval years fuel RITM-200 reactor core life Sevmorput refueling
24. Antarctic Treaty Article VI high seas freedom Madrid Protocol Annex I environmental impact assessment Annex IV marine pollution vessels CCAMLR convention area 60 degrees south Polar Code
25. A-68 iceberg Larsen C calved July 2017 area 5,800 km2 thickness 190 m drift Weddell Sea South Georgia grounded British Antarctic Survey
26. A-74 A-81 A-83 iceberg Brunt Ice Shelf calving Halley 2021 2023 2025 area km2 chasm
27. iceberg alley Weddell Sea iceberg drift tracks Weddell gyre iceberg draft grounding Weddell shelf bathymetry shoals
28. Weddell Sea cyclone frequency per year mesoscale cyclones Weddell Sea polar lows katabatic winds Ronne ice shelf barrier wind jet speed
29. electrical conductivity of sea ice bulk conductivity S/m brine volume HF radio wave propagation over sea ice ground wave
30. Ice Station Weddell 1992 communications HF radio satellite Inmarsat ice camp logistics power generators fuel Gordon Lukin
31. RV Polarstern technical data fuel capacity cubic meters endurance days range power installed engines MW icebreaking 1.5 m ice
32. RRS Sir David Attenborough specification endurance 60 days range 19,000 nautical miles fuel capacity dynamic positioning
33. sea ice dielectric properties 1-100 MHz conductivity mS/m first-year ice multi-year ice relative permittivity brine volume measured Sihvola Hoekstra
34. Antarctic ice sheet snow ice relative permittivity 3.15 conductivity 1e-5 S/m radio wave HF 10 MHz ice thickness radar loss
35. moored buoy HF radio repeater floating relay antenna ocean buoy HF transmitter long range communications deep sea mooring prototype
36. T-3 Fletcher's Ice Island drifting ice island station 1952 1974 radio communications power station occupied years Arctic Ocean ARLIS II
37. Soviet North Pole drifting stations NP-1 Papanin 274 days ice floe radio operator Krenkel shortwave radio communication drift 2,500 km
38. Fram expedition 1893-1896 drift Arctic Nansen Fram frozen in 35 months Maud expedition Amundsen 1922-1925 drift distance
39. Weddell Sea 2019 SWIFT buoys wave attenuation swell attenuation coefficient Polarstern PS117 Antarctic marginal ice zone direct observations wave-sea ice interactions authors
40. ship trapped in Weddell Sea ice beset rescue icebreaker Weddell Sea heavy pack ice Magdalena Oldendorff Endurance22 Agulhas II difficulty
41. Weddell Sea coastal polynya Ronne polynya Filchner polynya area ice production katabatic winds Brunt Riiser-Larsen polynya size km2 Nihashi Ohshima Tamura
42. Weddell Sea sea ice extent record low 2023 2024 2025 Weddell Sea minimum February open water NSIDC ice-free
43. Halley VI resupply Weddell Sea ship season January February ice conditions SA Agulhas II Sir David Attenborough Brunt Ice Shelf ice edge ship unloading
44. Neumayer Station III supply Atka Bay ice shelf edge ship Polarstern season December January sea ice conditions ship unloading ice edge
45. superstructure icing sea spray icing ship Antarctic Southern Ocean icing rate Polar Code icing risk Weddell Sea fog frequency
46. ERA5 wave model sea ice treatment ice concentration threshold 30% wave height not computed ice-covered grid points ECMWF documentation
47. Open-Meteo Marine Weather API ERA5-Ocean documentation resolution 0.5 degree wave_height historical 1940 data source ECMWF
48. Weddell Gyre interior mean flow cm/s Fahrbach moorings current meters Greenwich meridian eastern limb velocity Schröder Fahrbach 1999 structure transport eastern Weddell Gyre
49. Antarctic Slope Current Weddell Sea speed m/s Antarctic Slope Front velocity measurements mooring Filchner Trough overflow current speeds 0.5 m/s
50. Wave Glider Southern Ocean mission days endurance sea ice avoidance uncrewed surface vehicle Antarctic Weddell Sea autonomous surface vessel sea ice limitation
51. Southern Ocean surface drifters lifetime wave heights strong winds buoys survive Southern Ocean surface mooring Antarctic Circumpolar Current mooring depth 4000 m Drake Passage cDrake
52. Polarstern Winter Weddell Sea Project 1986 Winter Weddell Gyre Study 1989 ship drifted in pack ice stations ice drift days Fahrbach ANT V/2 ANT VII/4 ice station drift
53. Polarstern drifted frozen in Weddell Sea ice floe drift ship beset winter 1992 ANT-X/4 Winter Weddell Gyre Study 1992 Polarstern ice drift station
54. ice floe drifting station HF radio link antenna sea ice conductivity vertical antenna on sea ice performance versus ship measured HF propagation from Arctic ice camp
55. Evaluation of HF Radio Communications in the Arctic ice camp icedrill.org NVIS HF radio over ice sheet ground conductivity antenna
56. Padman Siegfried Fricker 2018 Ocean tide influences on the Antarctic and Greenland ice sheets Reviews of Geophysics tidal currents Weddell Sea Ronne ice front speeds
57. Weddell Sea mesoscale cyclone frequency Antarctic cyclones Weddell Sea sector number per year Southern Hemisphere cyclone climatology ERA5 Weddell Sea high cyclone density Bellingshausen
58. dynamic positioning fuel consumption tonnes per day research vessel holding station thrusters DP mode fuel burn ice-class vessel station-keeping
59. small vessel autonomous long endurance Antarctic expedition ship fuel consumption per day 50 m ice-strengthened vessel diesel liters per day hotel load at anchor

**Dead ends.**
- **Died at the sources (blocked or empty), not the query:**
  - AWI epic / epic2-clone pages and openpolar.no returned Anubis bot-challenge pages; I did not attempt to bypass them. This blocked the Kottmeier and Sellmann abstract, the "sea ice thickness distribution NW Weddell" record, and the DTIC HF-telemetry study (ADA026552, ADD016206).
  - 403 or certificate errors: Wiley (Kottmeier), DOAJ, ESS Open Archive (Wahlgren), apps.dtic.mil (ADA180819), apl.uw.edu.
  - AWI sustainable-ship-operation page returned 404; the AWI Polarstern symbol page 404; BAS SDA page returned empty; Carrasco and Bromwich (2003) PDF had a connection failure.
- **Died at the query, with no answer found in the results returned:**
  - HF-range (3-30 MHz) electrical conductivity of sea ice. The only numbers found were for 10-95 kHz [S51] or in an MF-focused paper that gives no values [S49]. The sea-ice constants in 4.1 and 4.2 are assumptions.
  - A real floating HF relay in Antarctica: only patents and prototypes appeared.
  - A polar-sea ocean-current turbine: only ice-covered rivers (RivGen) and the Kuroshio (IHI).
  - Weddell fog frequency; cyclone counts beyond UNVERIFIED snippets; relative flow beneath a drifting floe; OWS Mike crew rotation; SOFS and OOI 55S surface-mooring survival numbers; Polarstern fuel capacity in m³.
- **Died at the search budget:** the WebSearch limit (1000 per session) was exhausted before queries 58 and 59 ran. DP fuel use and small-vessel hotel load remain unmet gaps.
- **Verified a different way after a search-only claim:** the Halley window (via a Wayback copy of the Ingenia article), SDA specs (Baird Maritime fetch), and the OOI, Papa, MetOcean and Saildrone items (fetches).
- **Verified, then resolved by curl instead of WebFetch:** the ARS 2025 PDF (binary through WebFetch, readable via pdftotext), Shackleton "South" (Gutenberg), and the MOSAiC factsheets.

---

## Source table (all accessed 2026-10-04)

| # | Source | URL |
|---|---|---|
| S1 | NSIDC Sea Ice Index v4.0, S regional monthly workbook | https://noaadata.apps.nsidc.org/NOAA/G02135/seaice_analysis/S_Sea_Ice_Index_Regional_Monthly_Data_G02135_v4.0.xlsx |
| S2 | NSIDC SII v4 monthly GeoTIFF concentration | https://noaadata.apps.nsidc.org/NOAA/G02135/south/monthly/geotiff/ |
| S3 | NSIDC Sea Ice Index v4 landing page | https://nsidc.org/data/g02135/versions/4 |
| S4 | Open-Meteo Marine API docs (ERA5-Ocean, 0.5°) | https://open-meteo.com/en/docs/marine-weather-api |
| S5 | Open-Meteo Historical archive API (ERA5) | https://archive-api.open-meteo.com/v1/archive |
| S6 | ECMWF Newsletter 185 (ecWAM 30% sea-ice rule) | https://www.ecmwf.int/node/29517 |
| S7 | NOAA ERDDAP etopo180 (ETOPO1) | https://coastwatch.pfeg.noaa.gov/erddap/griddap/etopo180.html |
| S8 | Shi et al. 2021, The Cryosphere 15, 31 | https://par.nsf.gov/servlets/purl/10267591 |
| S9 | Behrendt et al. 2013, ESSD 5, 209 | https://essd.copernicus.org/articles/5/209/2013/essd-5-209-2013.pdf |
| S10 | Frontiers Mar. Sci. 2025, 10.3389/fmars.2025.1540777 | https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2025.1540777/pdf |
| S11 | Fahrbach et al. 1994, Ann. Geophys. 12, 840 | https://angeo.copernicus.org/articles/12/840/1994/ |
| S12 | PANGAEA moorings 792971, 792887, 792888 (Fahrbach and Rohardt) | https://doi.pangaea.de/10.1594/PANGAEA.792971 |
| S13 | LDEO Ice Station Weddell project page | https://ocp.ldeo.columbia.edu/res/div/ocp/projects/ISW/proj_ISW_files/proj_desc.html |
| S14 | LDEO-94-2 ISW-1 CTD report | https://www.archive.org/download/icestationweddel00unse/icestationweddel00unse.pdf |
| S15 | Shackleton, South (Project Gutenberg) | https://www.gutenberg.org/cache/epub/5199/pg5199.txt |
| S16 | MOSAiC expedition in numbers (AWI) | https://mosaic-expedition.org/wp-content/uploads/2021/02/mosaic_factsheet_expedition-in-numbers_engl.pdf |
| S17 | MOSAiC sustainability factsheet (fuel) | https://www.mosaic-expedition.org/wp-content/uploads/2019/09/mosaic-factsheet-facts-on-sustainability.pdf |
| S18 | Fram Museum, first Fram expedition | https://frammuseum.no/polar-history/expeditions/the-first-fram-expedition-1893-1896/ |
| S19 | Maud expedition history | https://www.maudreturnshome.no/maud/expedition-history/ |
| S20 | NP-1 drift abstract (JOR) | https://jor.ocean.ru/index.php/jor/article/view/425 |
| S21 | ADN, Fletcher's Ice Island | https://www.adn.com/alaska-life/2023/01/15/fletchers-ice-island-the-air-forces-arctic-research-facility-that-melted-away |
| S22 | Polar Record, Winter Weddell Sea Project 1986 | https://www.cambridge.org/core/journals/polar-record/article/antarctic-marine-research-in-winter-the-winter-weddell-sea-project-1986/E2E08B53E912ECC5AF2207A7D5209586 |
| S23 | Polar Argo | https://argo.ucsd.edu/?p=2320 |
| S24 | HAFOS chapter, PS129 cruise report | https://www.vliz.be/imisdocs/publications/397006.pdf |
| S25 | NOAA PMEL, Saildrone Antarctic circumnavigation | https://www.pmel.noaa.gov/news-and-media/highlights/saildrone-first-circumnavigate-antarctica-search-carbon-dioxide |
| S26 | MetOcean Spotter buoys, Drake Passage | https://www.metocean.co.nz/news/2019/2/15/drifting-wave-buoys-pass-the-drake-passage |
| S27 | TOS Oceanography, Wave Glider Southern Ocean | https://tos.org/oceanography/article/sustained-measurements-of-southern-ocean-air-sea-coupling-from-a-wave-glide |
| S28 | UW news, Wave Glider | https://www.washington.edu/news/?p=64512 |
| S29 | OOI Global Southern Ocean Array | https://oceanobservatories.org/?p=30346 |
| S30 | OOI Irminger buoy flyover update | https://oceanobservatories.org/2017/11/update-irminger-sea-surface-mooring-flyover-conducted/ |
| S31 | NOAA PMEL OCS Papa PA002 report | https://pmel.noaa.gov/ocs/sites/default/files/atoms/files/OCS_DAPR_PA002_FINAL.pdf |
| S32 | IHI ocean current turbine (Tethys) | https://tethys.pnnl.gov/project-sites/ihi-ocean-current-turbine |
| S33 | RenewableEnergyWorld, RivGen | https://www.renewableenergyworld.com/wind-power/offshore/rivgen-power-system-achieves-10-months-of-operation-orpc-reports/ |
| S34 | WNN, RITM-200 | https://www.world-nuclear-news.org/Articles/Russia-speeds-up-manufacture-of-icebreaker-reactor |
| S35 | Baird Maritime, RRS Sir David Attenborough | https://www.bairdmaritime.com/work-boat-world/icebreaking/vessel-review-sir-david-attenborough-british-antarctic-surveys-large-capacity-research-and-supply-ship |
| S36 | Antarctic Treaty, UN Treaty Series vol. 402 | https://treaties.un.org/doc/Publication/UNTS/Volume%20402/volume-402-I-5778-English.pdf |
| S37 | Protocol on Environmental Protection | https://jus.uio.no/english/services/library/treaties/06/6-08/antarctic-environmental-protocol.html |
| S38 | CCAMLR Convention text | https://www.ccamlr.org/en/organisation/camlr-convention-text |
| S39 | IMO Polar Code | https://www.imo.org/en/ourwork/safety/pages/polar-code.aspx |
| S40 | Ingenia, Halley VI (Wayback copy) | https://web.archive.org/web/2023/https://ingenia.org.uk/articles/built-to-last-the-construction-of-halley-vi/ |
| S41 | AWI press release 16 Jan 2008, Neumayer III | https://awi.de/en/about-us/service/press/single-view/polarstern-hat-das-eis-gebrochen-anlegestelle-frei-fuer-die-entladung-der-neuen-antarktisstation-neumayer-iii.html |
| S42 | NASA Earth Observatory, Maud Rise polynya | https://science.nasa.gov/earth/earth-observatory/deciphering-the-maud-rise-polynya-145069/ |
| S43 | Stulic et al. 2023, Ocean Sci. 19, 1791 | https://os.copernicus.org/articles/19/1791/2023/os-19-1791-2023.pdf |
| S44 | NASA EO, A-68 | https://science.nasa.gov/earth/earth-observatory/tracking-the-demise-of-a-giant-antarctic-iceberg-149872/ |
| S45 | ESA, Brunt iceberg A-81 (also notes A-74) | https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Giant_iceberg_breaks_away_from_Antarctic_ice_shelf |
| S46 | ESA, A-83 | https://www.esa.int/ESA_Multimedia/Images/2024/05/Iceberg_A-83_breaks_free |
| S47 | ESA, A-23A | https://www.esa.int/ESA_Multimedia/Images/2026/01/Earth_from_Space_The_fate_of_a_giant |
| S48 | ESA, the A-68 story | https://www.esa.int/Applications/Observing_the_Earth/The_A-68_story |
| S49 | Hehenkamp et al. 2025, Adv. Radio Sci. 22, 77 | https://ars.copernicus.org/articles/22/77/2025/ars-22-77-2025.pdf |
| S50 | US patent 6,218,994 (claims only) | https://patents.google.com/patent/US6218994B1 |
| S51 | O'Sadnick et al. 2016, The Cryosphere 10, 2923 (10-95 kHz) | https://tc.copernicus.org/articles/10/2923/2016/tc-10-2923-2016.pdf |
| S52 | Rosier and Gudmundsson 2020, The Cryosphere 14, 17 | https://tc.copernicus.org/articles/14/17/2020/tc-14-17-2020.pdf |

**Tools and software.**
- VOACAP (voacapl)
- ITURHFProp (ITU-R P.533, from the ITU-R-HF repository in SP)
- NTIA LFMF/GRWAVE (`lf_test`)
- PyNEC 2.3.4 (NEC-2)
- aacgmv2 2.7.1
- pyproj, rasterio

**UNVERIFIED search-snippet-only items, not independently opened:**
- Kottmeier and Sellmann 1996 values
- Wahlgren et al. MIZ attenuation
- AWI ice-sensing float survival (80%)
- Weddell iceberg-alley counts
- Mesoscale cyclone counts
- Filchner-Ronne tidal current peaks (1 m/s)
- Wave Glider "Oct-Feb" statement
- OWS Mike/Polarfront history
- Endurance22 wreck depth
- Ship-icing rate
- NP-1 2,850 km

Wikipedia appeared only as search leads (Polarfront, T-3, NP-1, Arktika). I did not use it for any stated fact.