# Relung Panen ocean-side research (2026-10-29)

**Brief:** `Relung_Panen_Ocean_Research_BRIEF_2026-10-29.md` (this folder). Real physical environment and real precedents only for the sea off the Shackleton Ice Shelf / Bunger Hills coast (about 95-105E, 64-66S). No design, no recommendation; the developer decides.

**Already known (not repeated):** the four port files `Relung_Panen_Port_Research_2026-10-25_A` to `_D` (this folder).

**Labels:** SOURCED = read at the source page (WebFetch) during this session. UNVERIFIED = seen only in a search snippet, or recalled, or inferred; not confirmed at the source.

## PROGRESS

- [x] 1 Sea state and swell (completed in the resumed session, 2026-10-29)
- [x] 2 Tides and water level (completed in the resumed session, 2026-10-29)
- [ ] 3 Currents and water properties (handled in the items3-8 file)
- [ ] 4 Sea ice for floating or moored structures (handled in the items3-8 file)
- [ ] 5 Icebergs and calving hazards (handled in the items3-8 file)
- [ ] 6 Wind and atmosphere over the water (handled in the items3-8 file)
- [ ] 7 Ship access from Hobart and Fremantle (handled in the items3-8 file)
- [ ] 8 Real precedents for a floating or moored gateway (handled in the items3-8 file)
- [x] FINAL (this file's FINAL covers items 1 and 2 only)

**Scope change (coordinator, 2026-10-29, during the resumed session):** items 3 to 8 moved to a second agent writing `Relung_Panen_Ocean_Research_2026-10-29_items3-8.md` (this folder). This file finishes items 1 and 2 and writes a FINAL for those two only.

Started 2026-10-29 12:31 PDT. Stopped 2026-10-29 about 12:43 PDT at the coordinator's request (session closing). **No item is complete; nothing is ticked.** Partial material for items 1 and 2 is below, then the STOP note.

**RESUMED 2026-10-29 12:48 PDT** by a fresh agent from the STOP NOTE at the end of this file. New material is added under each item, marked "(resumed session)". The earlier STOP NOTE is kept as written. **Resumed session finished 2026-10-29 about 13:53 PDT:** items 1, 2 and this file's FINAL complete; no search was refused.

**Pointer for the items3-8 file (not used here beyond items 1 and 2):** the *Denman Marine Voyage (NUY2025-V03) Voyage Report* (RSV *Nuyina*, March-April 2025; PDF at `data.imas.utas.edu.au/attachments/4dad6eca-e62d-4f3f-af5b-ddbd52ccb539/DMV_Voyage_Report_final.pdf`, 236 pages) worked this exact sector and also covers currents and water masses (CTD casts along the Shackleton front), the Shackleton Polynya (mooring M1 at 66°01.77'S 95°13.66'E; water depth 647 m in the report's deployment table and 629 m in its instrument table), icebergs (mooring height limited by *"icebergs that can reach drafts of up to 300 m"*), sea-ice conditions, katabatic air observed from the ship, and ship operations in ice.

---

## 1. Sea state and swell (complete as far as the sources allow; first session's partial notes, then the resumed session)

**What was found**

- **SOURCED** (Fraser, Day, Wang, Bennetts, Liu, O'Farrell, Coleman, Voermans, Xu, Zhu, Auger, Massom, Wongpan, Craw, Brouwer, Toyota, Heil and Horvat, "Revealing the Antarctic marginal ice zone with a decade-long wave-in-ice climatology", *Nature Communications*, published 20 May 2026; read through WebFetch, first 100,000 of 144,617 characters only). Data: SARAL/AltiKa altimeter, March 2013 to December 2024; ICESat-2 for validation (October 2018 to December 2023); WAVEWATCH III hindcast and CICE6-WIM output (2010 to 2019).
  - The wave climate has "strong seasonality, with peak annual wave heights in late austral winter/early spring, and minima in summer", with "maximum wave height at ~50°S, decreasing poleward."
  - "Significant wave heights adjacent to the ice edge are typically very large (>4 m) from 30° to 90°E during late winter/early spring," and "generally large (>3.5 m) from the prime meridian, eastwards across East Antarctica and the Ross Sea to the Bellingshausen Sea (~65°W)." The 95-105°E sector falls in the second, ">3.5 m" description (my reading of the longitude ranges; the paper gives no figure for 95-105°E specifically).
  - The wave-affected marginal ice zone (MIZ) "covers around 16% of the sea-ice zone"; its circumpolar mean width reaches "a minimum of ~35 km in late February" and "a broad peak of around 180 km from mid-July to early October." "Waves can travel hundreds of km into the MIZ."
  - A search-result summary (not confirmed on the page) attributed to this work: "In February to March … low mean significant wave heights of <2 m at high latitudes and near the Antarctic coast." UNVERIFIED.
- **SOURCED** (Grieger et al. 2018, *Tellus A*, "Subantarctic cyclones identified by 14 tracking methods", ERA-Interim 1979-2008; read through WebFetch): the tracking methods agree best on local cyclone maxima "off the coast of Dronning Maud Land at 30°E, near Wilkes Land at 120°E", which "are more pronounced for winter". The paper gives densities only as maps, not numbers for 95-105°E. No cyclone count for this sector was found.
- **UNVERIFIED** (search-result summary of Ward et al. 2023, *JGR Atmospheres*, not opened): "higher-latitude eastern Antarctic sectors are host to the highest cyclone density."
- From the earlier port file A (not repeated here): the only swell item for this coast is the 2025 *Nuyina* anecdote ("huge swells").

**Dataset identified and tested, but not yet extracted:** the CAWCR Wave Hindcast (WAVEWATCH III v4.18b, forced by NCEP CFSR/CFSv2 winds and sea ice; global 0.4° grid; hourly; January 1979 to September 2026; 573 monthly files) is open on the CSIRO THREDDS server at `https://data-cbr.csiro.au/thredds/dodsC/catch_all/CMAR_CAWCR-Wave_archive/CAWCR_Wave_Hindcast_aggregate/gridded/ww3.glob_24m.YYYYMM.nc` (OPeNDAP; tested and working). Checked so far:
  - Variables include `hs` (significant wave height, scale 0.002), `ice` (sea-ice fraction, scale 0.001), `t02`, `fp`, `dir`, `uwnd`/`vwnd` (wind, scale 0.1), `dpt` (depth, scale 0.5). Grid: latitude index i = (lat + 78)/0.4; longitude 0-359.6°E, index = lon/0.4 (100.0°E = 250).
  - The model's southernmost wet cells near 100°E are at 65.6°S (index 31). Near 96-104°E, cells from 65.6°S to about 64.4°S carry status 7 in `MAPSTA` (February 2015 file), and in February 2015 all fields, including `ice`, are missing there at most time steps, while cells at 65.6°S 100.0°E and at 62.4-62.8°S had values (ice 0.34-0.75).
  - The global attributes give the switch `IC0`. **SOURCED** (Rogers et al. 2018, NRL Memorandum Report NRL/MR/7320--18-9786, section 3.1.1, PDF read): under IC0 a cell above an upper ice-concentration threshold is "deactivated (treated as land)", and between user-chosen thresholds (the report's example is "25% to 75%") waves are partly blocked, with no frequency dependence. **UNVERIFIED:** the CAWCR run's own thresholds. The largest valid `ice` value seen in the sample was 0.749, which is consistent with a 0.75 upper threshold, but this was not confirmed in documentation. The CAWCR technical report (CTR_070) page now shows only a site-closure notice (died at the source).
  - **Meaning for interpretation (method note, not a result):** in this hindcast a missing `hs` at a sea cell means the cell was ice-blocked, not calm. Hs statistics from it describe open-water hours only and must be reported together with the fraction of hours blocked.
  - **The bulk download failed and produced no data.** A bug in the script (`fetch_cawcr.sh`: the `grep -o '[0-9]*$'` that reads the time-dimension length returns empty because the match ends in `]`) logged `NODDS` for every month. The job was stopped. Nothing was derived from it.

### Item 1, resumed session (2026-10-29, from 12:48 PDT)

**Fraser et al. 2026, rest of the paper and two confirmations (SOURCED, WebFetch of the nature.com page).**
- The previously UNVERIFIED summer sentence is now confirmed on the page: *"In February to March and at the time of minimum annual sea-ice extent, low mean significant wave heights of <2 m at high latitudes and near the Antarctic coast result in the lowest MIZ widths in austral summertime."* The next sentences: *"Additionally, thick summer sea ice enhances wave attenuation, despite often low concentration. From April, the ice edge rapidly advances northward into higher wave-height regions, with wave intensification until September promoting deeper wave penetration."*
- The paper names *"a ~15° longitudinal zone centered at ~130°E"* (spelling Americanized) with *"a relatively narrow MIZ"* (outside 95-105°E; no MIZ width is given for 95-105°E).
- Characters 100,000 to 144,617 are only the reference list, acknowledgements and data statements. Data: AltiKa wave-affected MIZ width, IMAS Data Portal, doi:10.25959/J17B-CT76; processing code, Zenodo doi:10.5281/zenodo.19479024; ICESat-2 wave attenuation data, AADC doi:10.26179/q9pe-w283. Nothing in that part concerns this sector.

**CAWCR hindcast documentation (SOURCED, researchdata.edu.au record 1401722, "CAWCR Wave Hindcast - Aggregated Collection").**
- WAVEWATCH III **v4.08 for 1979 to May 2013 and v4.18 from June 2013**; CFSR winds (0.3°, hourly) for 1979-2010 and CFSv2 winds (0.2°, hourly) from 2011; sea ice from *"Hourly sea ice concentrations from the CFSR and CFSv2 data sets"* used to define the ice edge; global grid 0.4°; spectra 29 frequencies (0.038-0.5 Hz) by 24 directions.
- *"January 1979 is a "model spin-up" month and data from this month should not be used for research purposes."* (January 1979 is therefore excluded below.)
- **The ice threshold under IC0 is not stated** on the record. Variable names change with the version: before June 2013 the files use `U10`, `V10`, `CI`; from about mid-2013 `uwnd`, `vwnd`, `ice` (checked on the DDS of 201305 = old names and 201309 = new names). The `ice` metadata of a 2020 file lists the switches `... IC0 ...` (confirmed in the file's DAS).
- **The CAWCR Technical Report 070 (Durrant et al. 2013) is still NOT reached.** The cawcr.gov.au page points to the National Library's TROVE web archive; the archived copy at `webarchive.nla.gov.au` answers with an "Anubis" bot-check page (died at the source; not bypassed).

**In-situ wave measurements nearest to this sector.**
- **SOURCED** (Kohout, Williams, Dean and Meylan 2014, "Storm-induced sea-ice breakup and the implications for ice extent", *Nature* 509, 604-607, doi:10.1038/nature13262; nature.com page read). Wave sensors on floes during SIPEX-2, September to October 2012; the paper averages sea-ice concentration *"between 120° E and 129° E"*, so the measurements lie **east of 95-105°E, not in it**. Storm of 23 September 2012: Hs about 6, 5.5 and 4.2 m at sensors 39, 51 and 90 km inside the ice edge; calm conditions (27 September): about 2, 1.3 and 0.1 m at 0, 14 and 150 km. *"We observed the wave height decay to be almost linear for large waves"* (Hs > 3 m).
- **SOURCED: ship observations inside this sector, March to April 2025.** *Denman Marine Voyage (NUY2025-V03) Voyage Report* (RSV *Nuyina*, IMAS/AAD, PDF `data.imas.utas.edu.au/attachments/4dad6eca-e62d-4f3f-af5b-ddbd52ccb539/DMV_Voyage_Report_final.pdf`, downloaded and read; section 2 "Weather conditions during DMV" by Bruce Payne). The voyage worked the Bruce Rise and central Denman area from 9 March to 2 April and the "West Shackleton" area from 2 to 21 April 2025. Verbatim weather log, by date:
  - 4-6 March (transit, south of Hobart): *"large swell with wave heights up to 6.5 m and winds up to 45 knots"*; 7-8 March *"wave heights up to 6 m"*; crossed 60°S about 10:00 on 8 March.
  - 9 March: *"A large deep low ... bringing winds up to 45 knots and wave heights of up to 6.5 m."*
  - **10 March: *"The large low brought heavy sea conditions, snow showers and strong winds on Monday 10 March with winds over 50 knots and waves over 10 m ... Conditions prevented operational activities apart from Hydroacoustics."*** Position: the report's CTD table puts cast 3 at 63.00°S 104.00°E on 8 March and cast 4 at 63.28°S 97.31°E on 12 March, so the ship was in about 63°S, 97-104°E on 10 March (my inference from the cast table; the report does not give the position on the 10th).
  - 21-22 March: *"Winds of 40 knots and 4 m swells."*
  - 4-6 April: *"a deep low came in from the west bringing wind gusts over 45 knots and 40 knots"*, temperatures below -15 °C; 11-12 April *"below -25 °C ... with sea ice forming"*; 13 April gusts *"up to 60 knots"*; 17-18 April gusts *"up to 60 knots on the 17th and 80 knots on the 18th"*.
  - 28 April (return transit): *"large swell (6-7 m)"*.
  - Summary section: four operational days in the Denman area and six in the West Shackleton area were *"impacted by adverse weather"*; CTD work continued through the moon pool *"in conditions impacted by sea-ice and with winds gusting above 50 knots"*. Another chapter of the report records a camera tow *"porpoising with 4 m swell"*.
  - Caution: these are bridge or forecaster descriptions in a voyage report, not instrument-processed wave statistics; one season only (2025, which the voyage itself describes as having "low sea-ice conditions").
- **NOT FOUND:** any moored wave buoy, wave-radar series, or published in-situ wave climatology for 95-105°E.

**Cyclones and extremes.**
- **NOT FOUND:** a numerical cyclone frequency for 95-105°E. Ward et al. 2023 was not located by a targeted search (died at the query). A Russian-language query for storm frequency at Mirny and the Davis Sea also died at the query.
- The "October 2022 Southern Ocean cyclone" (Wikipedia, read) peaked at 69°S **98°W** (Bellingshausen Sea), **not** 98°E: not relevant to this sector (dead end at the source).
- The extreme-value and storm-count work is done from the CAWCR extraction below.

**CAWCR hindcast extraction: results (DERIVED from the SOURCED dataset).** Data: CAWCR Wave Hindcast, gridded global 0.4° files `ww3.glob_24m.YYYYMM.nc` on the CSIRO THREDDS server, read through OPeNDAP ASCII requests; every third hourly step (3-hourly); February 1979 to September 2026 (572 months, 139,272 steps per cell; January 1979 dropped as the documented spin-up month; no month failed). Cells: 65.6°S to 60.0°S every 0.4° at 100.0°E and 101.6°E. 65.6°S is the southernmost sea cell the model has at these longitudes; its center lies about 15-20 km north of the western open-sea front (port file A puts the front corner at 65.77°S 100.29°E). Scale factors from the file attributes (hs 0.002 m; ice 0.001; t02 0.01 s; fp 0.001 Hz; wind 0.1 m/s). Peak period Tp = 1/fp. Events: a run of steps above a threshold, with a new event counted after at least 24 h below it. Extremes: the annual maximum of the 3-hourly Hs for 1980-2025, fitted with a GEV and with a Gumbel distribution (scipy). Scripts in the session scratchpad (`parse_cawcr.py`, `stats_cawcr.py`). In every file, a missing wave value always coincided with a missing ice value, period value and wind value (checked across all steps: 100% agreement), so a missing step is a cell switched off by the ice rule, not a calm.

**Table 1-A. Share of 3-hourly steps with the cell ice-blocked (no wave value), %**

| Cell | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 65.6°S 100.0°E | 6 | 3 | 1 | 1 | 7 | 10 | 13 | 12 | 11 | 6 | 3 | 5 |
| 65.2°S 100.0°E | 57 | 45 | 34 | 45 | 63 | 74 | 77 | 76 | 74 | 71 | 54 | 49 |
| 64.8°S 100.0°E | 61 | 41 | 31 | 62 | 91 | 98 | 99 | 99 | 99 | 97 | 77 | 66 |
| 64.0°S 100.0°E | 28 | 8 | 5 | 31 | 82 | 98 | 100 | 100 | 100 | 99 | 92 | 71 |
| 63.2°S 100.0°E | 0 | 0 | 0 | 5 | 34 | 65 | 89 | 95 | 99 | 97 | 74 | 20 |
| 62.0°S 100.0°E | 0 | 0 | 0 | 0 | 0 | 5 | 32 | 54 | 59 | 43 | 5 | 0 |
| 60.0°S 100.0°E | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 16 | 5 | 0 | 0 |
| 65.6°S 101.6°E | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 64.8°S 101.6°E | 41 | 18 | 10 | 37 | 75 | 91 | 96 | 98 | 98 | 95 | 70 | 56 |

**Table 1-B. Open-water significant wave height, mean / 90th percentile, m (only steps with a wave value)**

| Cell | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 65.6°S 100.0°E | 0.4 / 1.0 | 0.5 / 1.3 | 0.7 / 1.6 | 0.6 / 1.4 | 0.5 / 1.2 | 0.6 / 1.6 | 0.5 / 1.5 | 0.5 / 1.4 | 0.5 / 1.3 | 0.4 / 1.1 | 0.4 / 1.0 | 0.3 / 0.9 |
| 65.2°S 100.0°E | 1.1 / 2.3 | 1.5 / 2.8 | 1.8 / 3.4 | 1.2 / 2.8 | 0.9 / 2.1 | 1.0 / 2.5 | 1.0 / 2.5 | 0.9 / 2.3 | 0.9 / 2.0 | 0.7 / 1.9 | 0.7 / 1.7 | 0.6 / 1.6 |
| 64.8°S 100.0°E | 1.5 / 2.9 | 1.9 / 3.5 | 2.3 / 4.0 | 1.8 / 3.6 | 0.9 / 1.8 | 1.1 / 2.5 | 1.2 / 2.3 | 1.5 / 3.2 | 0.8 / 1.4 | 0.6 / 1.2 | 0.6 / 1.3 | 0.7 / 1.7 |
| 64.0°S 100.0°E | 1.8 / 3.3 | 2.5 / 4.0 | 2.9 / 4.7 | 2.5 / 4.5 | 2.0 / 4.1 | 1.4 / 2.7 | — | — | — | 0.7 / 1.2 | 0.5 / 1.1 | 1.1 / 2.5 |
| 63.2°S 100.0°E | 2.4 / 3.8 | 2.9 / 4.3 | 3.4 / 5.0 | 3.1 / 5.0 | 2.3 / 4.4 | 1.8 / 3.6 | 1.6 / 3.1 | 1.2 / 2.4 | 1.1 / 1.9 | 2.2 / 4.2 | 1.0 / 1.9 | 1.7 / 3.2 |
| 62.0°S 100.0°E | 2.9 / 4.2 | 3.3 / 4.7 | 3.7 / 5.3 | 3.8 / 5.5 | 3.5 / 5.2 | 2.9 / 4.9 | 2.3 / 4.2 | 1.6 / 3.4 | 1.3 / 2.8 | 1.2 / 2.6 | 2.0 / 3.6 | 2.7 / 4.1 |
| 60.0°S 100.0°E | 3.2 / 4.6 | 3.6 / 5.1 | 4.1 / 5.8 | 4.3 / 6.1 | 4.2 / 6.0 | 4.0 / 5.9 | 3.8 / 5.7 | 3.1 / 5.4 | 2.7 / 5.0 | 2.7 / 4.6 | 3.3 / 4.9 | 3.2 / 4.6 |
| 65.6°S 101.6°E | 0.6 / 1.5 | 0.8 / 1.7 | 1.0 / 2.2 | 0.8 / 2.1 | 0.8 / 2.1 | 0.9 / 2.5 | 0.9 / 2.4 | 0.8 / 2.3 | 0.8 / 2.1 | 0.6 / 1.8 | 0.6 / 1.7 | 0.5 / 1.4 |
| 64.8°S 101.6°E | 1.4 / 2.7 | 1.9 / 3.4 | 2.3 / 4.0 | 1.5 / 3.4 | 1.1 / 2.4 | 1.2 / 2.7 | 1.1 / 2.4 | 1.3 / 2.8 | 1.1 / 2.4 | 0.6 / 1.3 | 0.6 / 1.4 | 0.8 / 1.8 |

**Table 1-C. Share of ALL 3-hourly steps (blocked steps counted as no waves) with Hs above 2 m / above 4 m, %**

| Cell | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 65.6°S 100.0°E | 1 / 0 | 2 / 0 | 5 / 0 | 4 / 0 | 3 / 0 | 5 / 0 | 4 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | 1 / 0 | 1 / 0 |
| 65.2°S 100.0°E | 6 / 1 | 13 / 2 | 23 / 4 | 10 / 2 | 4 / 0 | 4 / 0 | 3 / 0 | 3 / 0 | 3 / 0 | 2 / 0 | 3 / 0 | 3 / 0 |
| 64.8°S 100.0°E | 9 / 2 | 22 / 3 | 36 / 7 | 13 / 3 | 1 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | 1 / 0 | 3 / 0 |
| 64.0°S 100.0°E | 26 / 4 | 58 / 9 | 73 / 17 | 38 / 10 | 7 / 2 | 1 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | 4 / 1 |
| 63.2°S 100.0°E | 61 / 8 | 80 / 14 | 91 / 25 | 75 / 21 | 32 / 9 | 12 / 3 | 3 / 0 | 1 / 0 | 0 / 0 | 1 / 0 | 2 / 0 | 26 / 3 |
| 62.0°S 100.0°E | 83 / 13 | 92 / 21 | 98 / 35 | 96 / 36 | 89 / 30 | 69 / 21 | 35 / 8 | 14 / 3 | 8 / 1 | 11 / 2 | 45 / 6 | 75 / 12 |
| 60.0°S 100.0°E | 92 / 19 | 97 / 30 | 99 / 46 | 99 / 51 | 98 / 51 | 97 / 44 | 92 / 38 | 66 / 26 | 52 / 18 | 61 / 17 | 88 / 25 | 91 / 19 |
| 65.6°S 101.6°E | 4 / 0 | 7 / 0 | 12 / 1 | 12 / 1 | 12 / 1 | 16 / 2 | 15 / 2 | 13 / 1 | 11 / 1 | 8 / 0 | 7 / 0 | 4 / 0 |
| 64.8°S 101.6°E | 13 / 2 | 33 / 5 | 46 / 9 | 18 / 4 | 4 / 0 | 2 / 0 | 1 / 0 | 1 / 0 | 0 / 0 | 0 / 0 | 1 / 0 | 3 / 0 |

**Table 1-D. Wave period in open water, mean T02 / mean peak period Tp, s**

| Cell | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 65.6°S 100.0°E | 3.0 / 5.9 | 3.8 / 7.4 | 4.1 / 7.9 | 3.0 / 5.5 | 2.5 / 3.9 | 2.5 / 3.6 | 2.5 / 3.6 | 2.4 / 3.5 | 2.4 / 3.5 | 2.3 / 3.4 | 2.3 / 3.4 | 2.4 / 4.1 |
| 65.2°S 100.0°E | 4.4 / 7.9 | 5.5 / 9.2 | 5.6 / 9.6 | 4.1 / 7.1 | 3.0 / 4.8 | 3.1 / 4.5 | 3.1 / 4.5 | 3.0 / 4.4 | 2.9 / 4.2 | 2.8 / 4.1 | 2.7 / 4.0 | 3.0 / 4.9 |
| 64.8°S 100.0°E | 5.2 / 9.0 | 6.1 / 10.1 | 6.2 / 10.4 | 5.4 / 9.4 | 3.6 / 6.3 | 3.1 / 4.4 | 3.4 / 5.1 | 3.6 / 5.1 | 3.0 / 4.2 | 2.6 / 3.7 | 2.6 / 3.8 | 3.3 / 5.5 |
| 64.0°S 100.0°E | 6.0 / 10.0 | 6.8 / 10.8 | 6.9 / 11.1 | 6.5 / 10.8 | 5.9 / 10.3 | 4.4 / 8.4 | — | — | — | 2.9 / 4.9 | 2.6 / 4.0 | 4.5 / 7.6 |
| 63.2°S 100.0°E | 6.8 / 10.9 | 7.1 / 11.3 | 7.2 / 11.5 | 7.0 / 11.3 | 6.4 / 10.9 | 5.8 / 10.3 | 5.3 / 9.7 | 4.9 / 8.8 | 4.2 / 8.5 | 5.9 / 9.7 | 5.0 / 8.6 | 6.0 / 10.0 |
| 62.0°S 100.0°E | 7.0 / 11.3 | 7.3 / 11.5 | 7.5 / 11.8 | 7.4 / 11.7 | 7.2 / 11.6 | 6.7 / 11.0 | 6.1 / 10.3 | 5.0 / 8.7 | 4.5 / 7.9 | 4.4 / 7.8 | 5.9 / 10.0 | 6.8 / 11.0 |
| 60.0°S 100.0°E | 7.2 / 11.5 | 7.4 / 11.7 | 7.6 / 12.0 | 7.7 / 12.0 | 7.7 / 12.2 | 7.5 / 11.9 | 7.3 / 11.7 | 6.7 / 11.1 | 6.2 / 10.5 | 6.2 / 10.4 | 7.0 / 11.1 | 7.1 / 11.3 |
| 65.6°S 101.6°E | 3.3 / 5.9 | 4.3 / 7.6 | 4.7 / 8.2 | 3.4 / 5.8 | 2.8 / 4.2 | 2.9 / 4.2 | 2.8 / 4.2 | 2.8 / 4.2 | 2.7 / 4.0 | 2.6 / 3.9 | 2.6 / 3.9 | 2.7 / 4.4 |
| 64.8°S 101.6°E | 5.2 / 9.1 | 6.1 / 10.0 | 6.0 / 10.0 | 4.8 / 8.4 | 3.5 / 5.7 | 3.3 / 4.9 | 3.1 / 4.5 | 3.4 / 4.9 | 3.2 / 4.5 | 2.7 / 3.8 | 2.6 / 3.9 | 3.6 / 6.2 |

**Table 1-E. Model 10-m wind speed (CFSR/CFSv2 forcing, at steps with a wave value), mean / share of steps above 20 m/s (%)**

| Cell | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 65.6°S 100.0°E | 5.6 / 1 | 5.7 / 1 | 6.6 / 2 | 7.0 / 3 | 7.3 / 3 | 8.0 / 5 | 7.8 / 4 | 7.5 / 4 | 7.4 / 3 | 6.9 / 2 | 6.5 / 2 | 5.8 / 1 |
| 65.2°S 100.0°E | 6.8 / 0 | 7.2 / 1 | 8.4 / 2 | 8.6 / 2 | 8.7 / 2 | 9.9 / 2 | 9.4 / 2 | 9.1 / 1 | 8.8 / 1 | 8.1 / 1 | 7.3 / 1 | 6.7 / 1 |
| 64.8°S 100.0°E | 7.2 / 0 | 7.4 / 1 | 8.7 / 2 | 9.0 / 2 | 8.9 / 0 | 11.7 / 0 | 10.5 / 0 | 12.9 / 0 | 9.2 / 0 | 7.3 / 0 | 6.9 / 0 | 6.8 / 0 |
| 64.0°S 100.0°E | 6.9 / 0 | 7.3 / 0 | 8.5 / 1 | 8.7 / 1 | 8.8 / 0 | 10.6 / 0 | — | — | — | 7.8 / 0 | 6.4 / 0 | 6.6 / 0 |
| 63.2°S 100.0°E | 7.1 / 0 | 7.6 / 0 | 8.8 / 1 | 8.8 / 2 | 8.3 / 1 | 8.9 / 1 | 9.1 / 0 | 8.8 / 0 | 9.3 / 0 | 8.9 / 0 | 6.6 / 0 | 6.7 / 0 |
| 62.0°S 100.0°E | 7.6 / 0 | 8.0 / 0 | 9.0 / 1 | 9.4 / 1 | 9.5 / 1 | 9.4 / 1 | 8.8 / 1 | 8.6 / 0 | 8.5 / 0 | 8.0 / 0 | 7.6 / 0 | 7.8 / 0 |
| 60.0°S 100.0°E | 8.0 / 0 | 8.8 / 1 | 9.9 / 1 | 10.1 / 1 | 10.2 / 2 | 10.2 / 2 | 10.2 / 2 | 9.8 / 1 | 9.5 / 1 | 9.2 / 1 | 9.2 / 0 | 8.3 / 0 |
| 65.6°S 101.6°E | 6.3 / 1 | 6.4 / 2 | 7.1 / 3 | 7.6 / 4 | 8.2 / 6 | 9.1 / 10 | 8.9 / 9 | 8.7 / 9 | 8.3 / 7 | 7.6 / 4 | 7.3 / 3 | 6.5 / 1 |
| 64.8°S 101.6°E | 7.2 / 1 | 7.7 / 1 | 9.0 / 3 | 9.0 / 3 | 9.6 / 2 | 11.2 / 1 | 10.5 / 0 | 12.4 / 0 | 11.0 / 0 | 7.6 / 0 | 7.2 / 0 | 6.9 / 0 |

**Table 1-F. Storms and extremes per cell (open-water steps only; 1979-2026)**

| Cell | Steps blocked | Open-water Hs: mean / 99th pct | Largest Hs (date) | Events per year with Hs > 5 m / > 8 m / > 10 m | Median annual maximum | 100-year Hs: GEV / Gumbel |
|---|---|---|---|---|---|---|
| 65.6°S 100.0°E | 6.5% | 0.50 / 2.65 m | 5.22 m (5 Jun 2010) | 0.02 / 0 / 0 | 3.83 m | 5.2 / 6.8 m |
| 65.2°S 100.0°E | 60.2% | 1.08 / 4.71 m | 11.00 m (30 Mar 1980) | 1.76 / 0.13 / 0.02 | 5.12 m | 11.1 / 12.1 m |
| 64.8°S 100.0°E | 77.1% | 1.61 / 5.86 m | 11.80 m (30 Mar 1980) | 2.60 / 0.15 / 0.02 | 5.76 m | 11.1 / 15.7 m |
| 64.0°S 100.0°E | 68.1% | 2.28 / 6.43 m | 10.92 m (30 Mar 1980) | 6.06 / 0.50 / 0.08 | 7.23 m | 10.8 / 17.7 m |
| 63.2°S 100.0°E | 48.4% | 2.52 / 6.60 m | 10.69 m (27 Apr 1990) | 11.98 / 1.13 / 0.10 | 8.20 m | 10.7 / 13.7 m |
| 62.0°S 100.0°E | 16.7% | 2.81 / 6.90 m | 13.98 m (3 May 1993) | 24.88 / 2.62 / 0.36 | 9.31 m | 14.3 / 14.1 m |
| 60.0°S 100.0°E | 2.4% | 3.53 / 7.89 m | 14.69 m (27 Sep 1995) | 43.66 / 7.13 / 1.74 | 11.09 m | 14.7 / 16.5 m |
| 65.6°S 101.6°E | 0.0% | 0.76 / 3.92 m | 7.63 m (4 Mar 1985) | 1.83 / 0 / 0 | 5.22 m | 7.7 / 9.2 m |
| 64.8°S 101.6°E | 65.7% | 1.55 / 5.64 m | 11.43 m (30 Mar 1980) | 3.19 / 0.19 / 0.02 | 6.17 m | 11.0 / 14.1 m |

Months in which the Hs > 5 m events fell (counts over 47.7 years): at 64.0°S 100°E, 26 in January, 57 in February, 122 in March, 62 in April, 16 in May, 6 in December, none June to November; at 62.0°S, every month, peaking in April (229) and March (206); at 60.0°S, every month, peaking in May (259) and April (255).

**What the hindcast says, in plain terms (DERIVED; with the cautions below):**
- **Season.** Near the front, waves are a late-summer and autumn matter. North of about 64°S the sea is open and wave-exposed mainly from December to May; from June to November the cells at 64.0-64.8°S are ice-blocked almost all the time (Table 1-A), which agrees in timing with the satellite ice table below. The roughest open-water months there are March and April (Table 1-B, 1-C), when the ice edge is far south and autumn storms have started.
- **Gradient.** Wave height falls steeply toward the coast: mean open-water Hs about 3.5 m at 60°S, 2.8 m at 62°S, 2.3 m at 64°S, 1.1 m at 65.2°S, 0.5 m at 65.6°S. Storms above 5 m: about 44 a year at 60°S, 25 at 62°S, 6 at 64°S, under 2 at 65.2°S.
- **Period.** In open water at 62-64°S in summer and autumn, the mean peak period is about 10-12 s (mean T02 about 6-7.5 s), which is long-period swell from the open Southern Ocean; at the coastal cells it falls to 4-8 s.
- **Extremes.** The largest values in the record are 13-15 m at 60-62°S; 10.7-11.8 m at 63.2-65.2°S (three of those cells share one storm, 30 March 1980). The 100-year estimates depend heavily on the fitted distribution (GEV and Gumbel differ by up to 7 m at the blocked cells); they are reported only as a spread.
- **Cross-check with the 2025 voyage.** For 9-11 March 2025 the hindcast's daily maximum Hs at 100°E is 5.4-7.2 m at 63.2°S, 7.4 m at 64.0°S, 8.9 m at 64.8°S and 8.2 m at 60.0°S; the voyage log reports "waves over 10 m" on 10 March. A voyage log's "wave height" is not defined as Hs, and the ship's position that day is known only to within about 63°S 97-104°E, so the two are not directly comparable; they are not in conflict.

**Cautions (each one SOURCED or checked here):**
1. **The ice rule.** The model switches off a cell above an ice threshold (IC0; Rogers et al. 2018) and the CAWCR threshold is still UNVERIFIED (the technical report could not be reached). In all 139,272 steps the largest `ice` value stored is 0.750, consistent with, but not proof of, an upper threshold of 0.75. Everything in Tables 1-B to 1-F describes open-water hours only.
2. **The coastal cells disagree with the satellite ice.** At 65.6°S 100°E the hindcast's own ice value has a median of 0.49 (10th-90th percentile 0.33-0.69) and the cell is switched off in only 6.5% of steps (0% at 65.6°S 101.6°E, where the stored ice values are similar: monthly means 0.24-0.44), while the satellite record (table below) gives monthly means of 0.62-0.85 at the nearest satellite cell to 100°E and 0.51-0.82 near 101.5°E. The hindcast therefore treats the water next to the front as partly ice-covered but open, with waves damped, much more often than the satellite record supports. **The 65.6°S rows should not be read as the sea state at the front.** The reason (forcing-ice resolution near the coast, or something else) was not established.
3. **The record is not uniform in time.** The share of blocked steps changes between periods: at 65.2°S 100°E it is 27% in 1979-1990, 57% in 1991-2002, 79% in 2003-2013 and 79% in 2014-2026; at 64.0°S, 60%, 69%, 72% and 72%; at 65.6°S, 0%, 0%, 5% and 19%. The model version and forcing change in 2011/2013 (above), and the sea ice itself changed over the period; the two cannot be separated with what was found. Mean open-water Hs before 2013 and after 2014: 0.55 against 0.35 m at 65.6°S; 1.09 against 1.10 m at 65.2°S; 2.36 against 2.05 m at 64.0°S; 3.54 against 3.54 m at 60.0°S. The three largest near-coast storms (11.0-11.8 m, 30 March 1980) fall in the early period, when the near-coast cells were open more often.
4. **Resolution.** A 0.4° (about 44 km by 18 km here) global grid cannot represent the bays and iceberg fields along the front; nothing here describes conditions in the lee of the ice shelf, in the Shackleton Polynya, or among grounded icebergs.
5. **Wind.** The 10-m winds in Table 1-E are the reanalysis forcing at about 0.2-0.3°; they are given only at steps the wave model kept, so ice-covered hours are missing. They are not station observations.

**Ice-covered versus ice-free water by month (DERIVED from satellite data; the data are SOURCED).** Source: *Sea Ice Concentration, NOAA/NSIDC Climate Data Record V6, Southern Hemisphere, 25 km, Science Quality, Monthly* (dataset `nsidcG02202v6shmday`, variable `cdr_seaice_conc_monthly`, served by NOAA CoastWatch ERDDAP `coastwatch.pfeg.noaa.gov/erddap`; grid positions from `nsidcCDRice_sh_grid`). Months used: January 1979 to December 2025 (47 years; 564 months per cell). For each target, the nearest 25-km cell (its center and its distance from the target are given). The table gives the mean concentration for each calendar month, then the share of years in which that month's mean concentration was below 0.15 (the usual "ice-free" cut), then the share of years at or above 0.75.

| Cell (center) | | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 65.64°S 99.95°E (about 15 km north of the western open-sea front; 5 km from 65.6°S 100°E) | mean | 0.80 | 0.67 | 0.62 | 0.72 | 0.83 | 0.85 | 0.83 | 0.83 | 0.80 | 0.81 | 0.74 | 0.77 |
| | % years < 0.15 | 6 | 17 | 21 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 2 |
| | % years ≥ 0.75 | 74 | 62 | 53 | 53 | 85 | 96 | 85 | 85 | 72 | 70 | 51 | 68 |
| 65.21°S 99.77°E | mean | 0.80 | 0.72 | 0.70 | 0.85 | 0.94 | 0.95 | 0.94 | 0.93 | 0.93 | 0.91 | 0.84 | 0.79 |
| | % < 0.15 | 2 | 13 | 13 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| 64.73°S 100.10°E | mean | 0.71 | 0.58 | 0.57 | 0.84 | 0.95 | 0.96 | 0.97 | 0.97 | 0.97 | 0.96 | 0.89 | 0.77 |
| | % < 0.15 | 13 | 26 | 19 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| 64.08°S 99.83°E | mean | 0.55 | 0.25 | 0.20 | 0.62 | 0.92 | 0.96 | 0.97 | 0.97 | 0.97 | 0.97 | 0.94 | 0.82 |
| | % < 0.15 | 17 | 49 | 51 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| 63.18°S 99.98°E | mean | 0.06 | 0.01 | 0.01 | 0.18 | 0.64 | 0.86 | 0.93 | 0.95 | 0.96 | 0.95 | 0.88 | 0.50 |
| | % < 0.15 | 77 | 98 | 96 | 60 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 11 |
| 62.07°S 100.04°E | mean | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.22 | 0.56 | 0.72 | 0.77 | 0.68 | 0.31 | 0.01 |
| | % < 0.15 | 98 | 100 | 100 | 100 | 81 | 45 | 9 | 2 | 2 | 4 | 23 | 94 |
| 60.07°S 100.21°E | mean | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.04 | 0.28 | 0.36 | 0.25 | 0.03 | 0.00 |
| | % < 0.15 | 98 | 100 | 100 | 100 | 100 | 98 | 89 | 36 | 30 | 38 | 91 | 98 |
| 65.52°S 101.52°E (off the eastern front) | mean | 0.80 | 0.60 | 0.51 | 0.69 | 0.76 | 0.79 | 0.82 | 0.82 | 0.81 | 0.82 | 0.79 | 0.82 |
| | % < 0.15 | 4 | 17 | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| 65.90°S 95.15°E (Shackleton Polynya area, near the DMV mooring M1 at 66.03°S 95.23°E) | mean | 0.06 | 0.00 | 0.19 | 0.43 | 0.47 | 0.45 | 0.51 | 0.51 | 0.51 | 0.47 | 0.16 | 0.09 |
| | % < 0.15 | 79 | 100 | 30 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 49 | 77 |

What the table says, in plain terms: **within about 50 km of the front at 100°E, a calendar month is ice-free on average in only about 2 to 26% of years, and only from December to March;** from April or May to November the monthly mean there is never below 0.15. The ice-free belt in late summer reaches south to about 64°S in about half of years (February and March). At 62°S the sea is ice-free from December to April almost every year, and at 60°S ice appears mainly from August to October. The cell next to the polynya mooring is open in summer in most years and holds about 0.45-0.51 mean concentration through winter. **Cautions:** these are monthly means, so a month with a mean below 0.15 can still hold ice on some days and a month above it can have open days; passive-microwave cells next to a coast or ice-shelf front are subject to "land spillover", which these products correct for (NSIDC's page for the near-real-time sister product G10016 v3, read: *"Uses the NASA Team 2 land spillover correction instead of the original NASA Team correction"*); how well that correction works at these particular cells was not checked; the cell nearest the front corner itself (target 65.55°S 100.3°E → center 65.60°S 100.47°E) is masked (no data) in all months, which means the dataset treats it as land or ice shelf.

## 2. Tides and water level (complete as far as the sources allow; first session's partial notes, then the resumed session)

- **SOURCED** (Antarctic Tide Gauge database, Howard, King and Padman 2020, doi:10.15784/601358; read on the ESR browse page `https://www.esr.org/?p=1452`, raw page text downloaded). **No gauge lies between about 78°E and 110°E**; the stations nearest the Shackleton front are Davis and Casey. Amplitudes in cm (Greenwich phases in degrees in brackets), each from a 365-day bottom-pressure record with a 3,600 s sample interval:

| Station | Position | Q1 | O1 | P1 | K1 | N2 | M2 | S2 | K2 |
|---|---|---|---|---|---|---|---|---|---|
| Casey (20120-) | 66.283°S 110.533°E | 6.4 (224.2) | 26.5 (233.7) | 8.6 (242.4) | 26.6 (243.7) | 7.3 (120.5) | 29.3 (142.9) | 16.9 (200.1) | 4.7 (199.4) |
| Davis (20100-) | 68.45°S 77.967°E | 7.2 (260.7) | 28.8 (269.0) | 8.8 (276.0) | 27.8 (277.0) | 5.7 (168.2) | 20.1 (208.5) | 17.7 (307.1) | 5.1 (308.8) |
| Mawson (20080-) | 67.6°S 62.867°E | 6.0 | 25.4 | 7.7 | 23.4 | 2.3 | 3.1 | 11.4 | 3.3 |

- **DERIVED** (arithmetic on the Casey row only; not a prediction): the eight Casey amplitudes sum to 126.3 cm. That gives a theoretical ceiling of about 2.5 m on the peak-to-trough tidal range there if every constituent peaked together. The real maximum is lower, and no prediction was run. Casey is about 440 km east of the Shackleton front, so **this is not a figure for the front.**
- The diurnal (O1, K1) and semidiurnal (M2, S2) amplitudes are of similar size at Casey and Davis, which means a mixed tide (my reading of the table; no source states it for this coast).
- **NOT FOUND (so far):** a tidal range or model value at the Shackleton front itself, tidal currents, and tide cracks offshore. CATS2008 and the AntTG text file are behind a captcha download form at USAP-DC (died at the source). A commercial tide-prediction site (nashaplaneta.net, "186 cm" at Davis on one day) turned up in a search and was **not used**.

### Item 2, resumed session (2026-10-29)

**Tide type (SOURCED classification; DERIVED values).** The form factor F = (K1 + O1)/(M2 + S2) classes tides as semidiurnal (0-0.25), *"Mixed, mainly semidiurnal"* (0.25-1.5), *"Mixed, mainly diurnal"* (1.5-3) and diurnal (> 3) (Bosboom and Stive, *Coastal Dynamics*, Table 4.1, LibreTexts edition, read). From the AntTG amplitudes above: **Casey F = 1.15 (mixed, mainly semidiurnal); Davis F = 1.50 (on the boundary between the two mixed classes).**

**Harmonic prediction from the gauge constants (DERIVED; my own computation, not a published prediction).** Script `scripts/tidepred.py` (scratchpad): the eight AntTG constituents, Greenwich phases, astronomical arguments from mean lunar and solar longitudes, standard simplified nodal factors (f, u) for M2, N2, K1, O1, Q1 and K2; 10-minute steps for 2020-2038 (one full 18.6-year nodal cycle). Not validated against an official table (the Bureau of Meteorology prediction page for Casey, linked from the AAD Casey station page, returned HTTP 403: died at the source). Eight constituents only, so shallow-water and long-period terms are missing.

| | Casey (66.28°S 110.53°E) | Davis (68.45°S 77.97°E) |
|---|---|---|
| Largest high-to-low excursion, 2020-2038 | 2.06 m | 1.98 m |
| Daily range (calendar day): mean | 1.15 m | 1.08 m |
| Daily range: 10th / 90th / 99th percentile | 0.69 / 1.62 / 1.89 m | 0.61 / 1.52 / 1.80 m |
| Daily range: largest / smallest | 2.03 / 0.29 m | 1.96 / 0.10 m |
| Days with only one high and one low | about 11% | about 28% |
| Largest excursion in 2020 / 2025 / 2029 / 2034 | 1.97 / 2.05 / 1.94 / 1.85 m | 1.88 / 1.98 / 1.83 / 1.69 m |

The year-to-year swing follows the 18.6-year nodal cycle of the diurnal terms. **Neither station is at the Shackleton front** (Casey about 440 km east of it; Davis far to the west); these are the nearest measured tides, not a figure for the front.

**Why models are weaker here (SOURCED).** Hayakawa, Kim, Aoyama, Doi and Shibuya (National Institute of Polar Research), "Ocean tidal analysis with decade-scale tide gauge data in East Antarctica", JpGU 2010 abstract SGD001-P13 (PDF read): *"The model estimates around Antarctica, however, are less accurate than these for the global ocean since the altimeters have no coverage poleward of 66S."* They analyzed about 15 years at Syowa, Mawson, Davis and Casey and found *"periodic fluctuations for 6-8 years ... in some tidal constituents."* The same applies to EOT20 (SEANOE record, read): the empirical model covers 66°S to 66°N, and *"FES2014b"* fills the higher latitudes. The Shackleton front (about 65.5-66°S) sits at that edge.

**A tide-model value at the Shackleton front: EOT20 (data SOURCED; extraction and predictions DERIVED).** EOT20, DGFI-TUM global empirical ocean tide model (Hart-Davis, Piccioni and Dettmering; SEANOE doi:10.17882/79489, CC BY 4.0; file metadata: "product_version 1.0.0", 0.125° grid, amplitudes in cm, Greenwich phases). The `ocean_tides` NetCDF files were downloaded from the SEANOE archive (`seanoe.org/data/00683/79489/data/85762.zip`) and read at the nearest valid grid cell to each point (distance in brackets). Amplitude cm (phase °):

| Point (cell, distance) | Q1 | O1 | P1 | K1 | N2 | M2 | S2 | K2 | M4 |
|---|---|---|---|---|---|---|---|---|---|
| Casey gauge, check (66.25°S 110.50°E, 3.9 km) | 6.2 (229) | 25.9 (236) | 8.4 (245) | 26.5 (246) | 7.2 (122) | 28.8 (142) | 15.9 (201) | 4.2 (193) | 0.2 |
| Davis gauge, check (68.50°S 78.00°E, 5.7 km) | 6.5 (263) | 27.1 (272) | 8.6 (281) | 26.7 (280) | 5.6 (173) | 19.0 (213) | 16.6 (312) | 4.3 (315) | 0.3 |
| Western open-sea front (65.625°S 100.00°E, 1.7 km) | 6.4 (251) | 30.0 (235) | 16.2 (265) | 19.2 (249) | 7.3 (132) | 36.8 (166) | 15.8 (239) | 3.5 (349) | 4.3 |
| Eastern front (65.50°S 101.50°E, 2.4 km) | 6.9 (234) | 27.9 (230) | 22.8 (254) | 21.6 (273) | 7.7 (133) | 31.2 (159) | 19.4 (241) | 6.9 (300) | 2.8 |
| 65.25°S 100.00°E (5.5 km) | 6.9 (251) | 28.2 (239) | 13.8 (261) | 19.1 (250) | 7.0 (135) | 33.6 (167) | 13.2 (235) | 2.3 (308) | 2.2 |
| 64.00°S 100.00°E | 6.7 (239) | 26.1 (247) | 6.7 (262) | 25.9 (254) | 7.1 (141) | 26.9 (168) | 14.1 (230) | 4.6 (229) | 0.1 |
| Polynya, DMV mooring M1 (66.00°S 95.25°E, 3.4 km) | 6.5 (245) | 27.0 (249) | 7.2 (257) | 26.6 (254) | 7.2 (157) | 29.9 (182) | 18.1 (255) | 4.4 (248) | 1.1 |
| 62.00°S 100.00°E | 4.5 (237) | 20.4 (246) | 7.0 (250) | 19.4 (254) | 6.2 (144) | 24.5 (169) | 12.4 (228) | 3.3 (228) | 0.3 |

- **Check against the gauges:** at Casey the model agrees with the AntTG constants within 0.1-1.0 cm and 1-7° for all eight constituents; at Davis within 0.1-1.7 cm and 2-7°. Both gauges are south of 66°S, so these model values are from the FES2014b fill, not from EOT20's own altimetry solution (per the SEANOE note above).
- **Warning sign at the front cells (DERIVED check):** at the three cells within about 50 km of the front (65.25-65.64°S), P1 is 0.72-1.06 of K1 and the shallow-water M4 is 2-4 cm. At every gauge in the AntTG table above (Casey, Davis, Mawson), P1 is 0.32-0.33 of K1, and the model gives 0.26-0.36 at 64°S, 62°S and the polynya cell. Why this pair is fragile here (SOURCED: Andersen, Rose and Hart-Davis 2023, "Polar Ocean Tides—Revisited Using Cryosat-2", *Remote Sensing* 15(18):4479, doi:10.3390/rs15184479, PDF read): sampling *"causes the major diurnal constituent K1 to be aliased into the annual signal. In polar regions, another complication is due to the presence of sea ice, which frequently degrades satellite altimetry data."* Their Table 1 gives the alias period of both K1 and P1 as 365.24 days for Envisat and for Sentinel-3, so those missions cannot separate the two from each other or from the seasonal cycle. Linking that to the odd values at these particular cells is my inference. **The front-cell constants are therefore suspect, most of all P1, K1 and the larger M2 there.** No independent measurement at the front exists to settle it (none found).
- **Predicted ranges from these constants** (same script and method as the gauge predictions above; 2020-2038):

| Point | Largest excursion | Mean daily range | Daily range 90th / 99th percentile | F |
|---|---|---|---|---|
| Casey cell (model) | 1.98 m | 1.12 m | 1.56 / 1.82 m | 1.17 |
| Davis cell (model) | 1.86 m | 1.02 m | 1.44 / 1.70 m | 1.51 |
| Western front (suspect constants) | 2.43 m | 1.29 m | 1.87 / 2.19 m | 0.93 |
| Eastern front (suspect constants) | 2.46 m | 1.25 m | 1.83 / 2.18 m | 0.98 |
| 65.25°S 100°E (suspect constants) | 2.20 m | 1.18 m | 1.69 / 1.98 m | 1.01 |
| 64.0°S 100°E | 1.94 m | 1.08 m | 1.50 / 1.77 m | 1.27 |
| Polynya M1 cell | 2.12 m | 1.18 m | 1.66 / 1.95 m | 1.12 |
| 62.0°S 100°E | 1.61 m | 0.91 m | 1.27 / 1.48 m | 1.08 |

  The model reproduces the gauge-based Casey prediction within about 8 cm on the largest excursion (1.98 m model, 2.06 m gauge) and 3 cm on the mean daily range.

**A second, independent model: DTU23 (data SOURCED; extraction and predictions DERIVED).** *DTU23 Global Ocean Tide model (DTU23_OceanTide)*, DTU Space, data.dtu.dk / figshare article 23828874, doi:10.11583/DTU.23828874.v1. The record says (read through the figshare API): *"The newest version of the DTU global 1/6 degree ocean tide models derived from satellite altimetry ... The spatial resolution is 1/16 degree ... The model is mainly and update to the previous global ocean tide models (DTU16) in the polar regions."* Files: ASCII PERTH3-format grids (`*_DTU23.d.gz`, 2881 × 5761, amplitude cm and Greenwich phase), read at the nearest valid 1/16° cell:

| Point (cell, distance) | Q1 | O1 | P1 | K1 | N2 | M2 | S2 | K2 | M4 | P1/K1 |
|---|---|---|---|---|---|---|---|---|---|---|
| Casey gauge, check (66.31°S 110.56°E, 3.5 km) | 5.9 (231) | 25.3 (237) | 8.2 (244) | 26.4 (245) | 7.3 (120) | 29.2 (143) | 16.9 (203) | 4.4 (194) | 0.4 | 0.31 |
| Davis gauge, check (68.44°S 77.94°E, 1.8 km) | 6.9 (259) | 29.0 (269) | 8.7 (278) | 27.5 (276) | 5.9 (174) | 19.6 (208) | 17.3 (308) | 4.5 (312) | 0.1 | 0.32 |
| Western open-sea front (65.625°S 100.00°E, 1.7 km) | 6.3 (229) | 27.5 (239) | 8.8 (246) | 26.8 (246) | 8.8 (141) | 33.5 (168) | 19.9 (230) | 5.0 (225) | 0.2 | 0.33 |
| Eastern front (65.50°S 101.50°E, 2.4 km) | 5.9 (230) | 25.9 (238) | 8.3 (246) | 25.6 (245) | 8.3 (136) | 30.4 (161) | 17.9 (222) | 4.5 (216) | 0.3 | 0.32 |
| 65.19°S 100.00°E (1.4 km) | 6.1 (232) | 26.8 (242) | 8.5 (249) | 25.8 (249) | 8.1 (142) | 30.8 (169) | 18.0 (230) | 4.5 (225) | 0.2 | 0.33 |
| 64.00°S 100.00°E | 6.0 (238) | 25.9 (247) | 8.0 (253) | 24.9 (256) | 7.1 (144) | 27.2 (167) | 15.3 (231) | 3.8 (225) | 0.2 | 0.32 |
| Polynya, DMV mooring M1 (66.00°S 95.25°E, 3.4 km) | 6.5 (241) | 27.5 (250) | 8.6 (255) | 27.0 (257) | 7.2 (156) | 31.0 (183) | 17.7 (252) | 4.6 (249) | 0.1 | 0.32 |
| 62.00°S 100.00°E | 4.8 (236) | 20.0 (246) | 6.5 (250) | 20.4 (253) | 6.2 (143) | 23.9 (169) | 12.1 (227) | 3.1 (224) | 0.1 | 0.32 |

- **Check against the gauges:** Casey within 0.0-1.2 cm and 0-7° on all eight constituents; Davis within 0.1-0.6 cm and 0-6° (closer than EOT20 at Davis; about the same as EOT20 at Casey).
- **At the front cells DTU23 does not show EOT20's warning sign:** P1/K1 is 0.32-0.33, the same as at every gauge, and M4 is 0.2-0.3 cm. At the western front the two models agree within 0.1 cm on Q1, 1.5 cm on N2, 2.5-3.3 cm on O1 and M2 and 4.1 cm on S2, and disagree on P1 (8.8 against 16.2 cm) and K1 (26.8 against 19.2 cm).

| Point (DTU23) | Largest excursion 2020-2038 | Mean daily range | Daily range 90th / 99th percentile | Days with one high and one low | F |
|---|---|---|---|---|---|
| Casey cell (check; gauge-based value 2.06 m) | 1.99 m | 1.13 m | 1.57 / 1.83 m | 10% | 1.12 |
| Davis cell (check; gauge-based value 1.98 m) | 1.96 m | 1.07 m | 1.51 / 1.79 m | 29% | 1.53 |
| Western open-sea front | 2.28 m | 1.27 m | 1.80 / 2.10 m | 10% | 1.02 |
| Eastern front | 2.10 m | 1.18 m | 1.66 / 1.94 m | 10% | 1.07 |
| 65.19°S 100°E | 2.14 m | 1.19 m | 1.68 / 1.97 m | 11% | 1.08 |
| 64.0°S 100°E | 1.93 m | 1.08 m | 1.51 / 1.77 m | 12% | 1.20 |
| Polynya M1 cell | 2.15 m | 1.21 m | 1.69 / 1.98 m | 11% | 1.12 |
| 62.0°S 100°E | 1.59 m | 0.90 m | 1.26 / 1.47 m | 8% | 1.12 |

**Plain reading of item 2's model results:** both models put the sea next to the Shackleton front in the *"mixed, mainly semidiurnal"* class (F about 0.9-1.1), usually with two highs and two lows a day; on about one day in ten there is only one high and one low. The mean daily range is about 1.2-1.3 m, the 99th-percentile day about 1.9-2.2 m, and the largest astronomical excursion over a full 18.6-year nodal cycle about 2.1-2.3 m (DTU23; EOT20's suspect cells give up to about 2.4-2.5 m). The range grows from the open sea toward the front (DTU23: 1.59 m at 62°S to 2.28 m at the western front). **These are model values, not measurements; no tide record from the front itself exists in any source found.** Non-tidal effects (wind setup, air pressure, the 2004-type tsunami signal at Casey) come on top and were NOT FOUND as numbers for this coast.

**CATS2008 (SOURCED, ESR model summary page `esr.org/?p=1590`).** 4-km polar stereographic inverse model of the whole circum-Antarctic ocean including ice-shelf cavities; ten constituents (M2, S2, N2, K2, K1, O1, P1, Q1, Mf, Mm); assimilates TOPEX/Poseidon altimetry where sea ice is absent, about 50 tide records, and ICESat crossovers on the Ross and Filchner-Ronne shelves; gives currents in cm/s. No accuracy figures on the page. Download only through USAP-DC (captcha; died at the source, not retried).

**Tide cracks (SOURCED definition).** WMO Sea-Ice Nomenclature (WMO-No. 259, edition 1970-2017, vol. I, term 7.1.1.1; PDF from the Danish Meteorological Institute's ice service, read): *"Tide crack: Crack at the line of junction between an immovable ice foot or ice wall and fast ice, the latter subject to rise and fall of the tide."* **NOT FOUND:** any observation of tide cracks at the Shackleton front or in the fast ice east of it. The Zhongshan tidal-crack mapping paper (Prydz Bay, another coast) and an MDPI paper both returned HTTP 403 (died at the source); the US Antarctic Program sea-ice field-manual copy failed with a certificate error (died at the source).

**Non-tidal sea level (partly SOURCED).** AAD news item "Rising tide of interest in sea level rise", 3 June 2010 (read): about 15 years of bottom-mounted gauge records at Casey, Davis, Mawson and Macquarie Island; after the 26 December 2004 Sumatra earthquake *"tide gauges detected an increase in tide height of about 500mm at Mawson, 600mm at Casey and 200mm at Macquarie Island"*. **NOT FOUND:** the size of storm surges, the seasonal sea-level cycle or the atmospheric-pressure response at Casey or Davis. A 2019 USQ thesis on Casey sea level ("Measuring Changes in Sea Level Around Antarctica", seen in search results with a 4.2 mm/yr trend and "high uncertainty") could not be opened (SSL error on both https and http: died at the source), so its numbers stay UNVERIFIED.

**Tidal currents.** **NOT FOUND** for the Shackleton front or the Denman trough. Searches for tidal-current speeds there died at the query; the Padman et al. 2002 CATS paper (Cambridge) returned HTTP 403 (died at the source). The DMV voyage report (item 1 above) says that near the Denman Glacier at night *"strong local currents and numerous icebergs, combined with adverse winds, generated conditions not conducive to operations"*; it does not say whether those currents were tidal. Two open tide models that do give currents (CATS2008; TPXO) were not reachable without a captcha or a registration, and the two models used here (EOT20, DTU23) give heights only.

---

## FINAL (items 1 and 2 only; items 3 to 8 are in the items3-8 file)

Factual implications of what was found, for a large floating structure off the Shackleton Ice Shelf front (about 95-105°E) and for ships arriving there. No recommendation; the developer decides.

**Sea state (item 1).**
- **Supported by the sources:** the open Southern Ocean to the north is among the roughest water anywhere in the hindcast: at 60°S, 100°E the mean open-water Hs is about 3.5 m, Hs exceeds 5 m in about 44 separate storms a year, and the largest 3-hourly value since 1979 is 14.7 m. Waves weaken steeply southward, because the ice damps them (Fraser et al. 2026; Kohout et al. 2014) and because the ice covers the sea for much of the year. **Any ship coming from Hobart or Fremantle crosses that belt;** the 2025 *Nuyina* voyage log records 6-6.5 m waves on several days in transit and "waves over 10 m" on 10 March 2025 at about 63°S, 97-104°E.
- **Supported:** within about 50 km of the front at 100°E, the sea surface is ice-covered from May to October in every year of the 1979-2025 satellite record and in April and November in almost every year (long-term monthly means about 0.7-0.97 in those months), and is ice-free as a monthly mean only in December to March of a minority of years (2-26% of years, depending on cell and month). The ice-free summer belt reaches 64°S in about half of years in February and March.
- **Supported, with cautions:** where the sea is open near the front, the hindcast's roughest season is March and April; at 64°S, 100°E Hs exceeds 4 m in 9-17% of all February-April hours and 5-m storms come about 6 times a year, almost all from January to May; the record's largest values near the coast are about 11-12 m (one storm, 30 March 1980). Swell periods there are long (mean peak period about 10-11 s).
- **Not supported:** a reliable sea state for the cell next to the front itself (the hindcast's coastal cell carries less ice than the satellite record shows, so its 0.5 m mean is not trustworthy); any wave behavior inside the polynya, in the lee of the ice shelf or among icebergs (below the model's 0.4° resolution); a 100-year design wave (the estimates spread from about 11 to 18 m at 64-65°S depending on the fitted distribution, and the record is not uniform in time); a numerical cyclone frequency for this sector (NOT FOUND); any in-situ wave record in 95-105°E (NOT FOUND).

**Tides and water level (item 2).**
- **Supported (model values, cross-checked at two gauges):** next to the front the tide is mixed, mainly semidiurnal, normally two highs and two lows a day; mean daily range about 1.2-1.3 m; a 99th-percentile day about 1.9-2.2 m; largest astronomical rise-to-fall over an 18.6-year cycle about 2.1-2.3 m (DTU23), with EOT20 giving up to about 2.5 m from constants that fail an internal check. The nearest gauges (Casey, Davis) give 1.98-2.06 m for the same quantity. Any structure floating there would ride a daily vertical swing of about a meter, and about two meters at the extremes, before non-tidal effects.
- **Supported:** at least one tsunami reached this coast's gauges in the record: about 0.6 m at Casey after the December 2004 earthquake (AAD). Tide cracks form where fast ice meets ice fixed to the shore or an ice wall (WMO definition).
- **Not supported / NOT FOUND:** any measured tide at the front; tidal-current speeds at the front or in the Denman trough; storm-surge, seasonal sea-level and air-pressure effects as numbers for this coast; any observation of tide cracks on this stretch of coast; anything specific about how a floating structure here would respond to the water-level changes (precedents are in the items3-8 file).

---

## STOP NOTE (2026-10-29, about 12:43 PDT): session closed by the coordinator

> **Resolved (resumed session, 2026-10-29):** the items left below for items 1 and 2 were completed or are recorded as NOT FOUND/UNVERIFIED in the item sections above; items 3 to 8 moved to the items3-8 file. This note is kept as written for the record.

**Done:** none of items 1 to 8 or FINAL is complete, and none is ticked. A search budget limit was **not** hit; the stop was ordered so a fresh session can resume with a new quota.

**In the middle of:** item 1 (sea state), and item 2 (tides) had been started.

**Left in item 1:**
1. Fix the bug in `scratchpad/scripts/fetch_cawcr.sh` (read the time length with `grep -o 'time = [0-9]*'`, then take the digits).
2. Re-run the extraction for 197901-202609: 3-hourly; variables hs, ice, t02, fp, uwnd and vwnd; box latitude index 31-45 (65.6°S to 60.0°S), longitude index 250-254 step 4 (100.0°E and 101.6°E). Each month takes about 27 s; 6 in parallel take about 45 min.
3. Compute monthly Hs mean, P90 and maximum, and the share of hours ice-blocked per cell. Add peak period, storm counts (for example Hs above 5 m), and annual maxima for an extreme-value estimate.
4. Also: read the rest of Fraser et al. 2026 (offset 100000), confirm the IC0 thresholds in the CAWCR documentation (Durrant et al. 2013, CAWCR Technical Report 070; the cawcr.gov.au page is closed, so try the NLA web archive copy named on the closure page), and look for in-situ wave data in this sector.

**Left in item 2:**
- A tide-model value at the Shackleton front (CATS2008 or TPXO through pyTMD, or EOT20 from SEANOE, which is openly downloadable; numpy is present, netCDF4 is not installed).
- Tidal currents; tide cracks; and a harmonic prediction from the Casey constants to get the real spring and neap range.

**Not started:** items 3, 4, 5, 6, 7, 8 and FINAL.

**Sources already identified for unfinished items:**
- CAWCR hindcast THREDDS (above); Rogers et al. 2018 NRL report (downloaded); Fraser et al. 2026 *Nat. Commun.*; Grieger et al. 2018 *Tellus A*; Ward et al. 2023 *JGR Atmospheres* (not opened).
- AntTG database (ESR page); USAP-DC 601358 (captcha).
- Wikipedia "Davis Sea" and "Mawson Sea"; "October 2022 Southern Ocean cyclone" (Wikipedia; not opened).
- A ResearchGate paper on water masses of the Davis and Mawson seas from the 67th RAE (ResearchGate refused access to the earlier agents).
- SWIFT and SHARC wave-in-ice buoy studies (Weddell Sea, not this sector).

**Exact search strings already run (WebSearch):**
1. `significant wave height climatology East Antarctica coast sea ice ERA5 seasonal Southern Ocean waves` (extended). Found Fraser 2026. Hit.
2. `wave buoy deployed East Antarctica sea ice Nuyina OR "Aurora Australis" Spotter wave measurements 2019 2022 marginal ice zone`. Weddell Sea results only; nothing for this sector (died at the query).
3. `CAWCR wave hindcast THREDDS global 0.4 degree hs monthly data access OPeNDAP`. Hit (THREDDS address).
4. `extratropical cyclone frequency East Antarctic coast 90E-110E climatology cyclone density Davis Sea Mawson Sea` (extended). Grieger 2018; no numbers for the sector (died at the sources for a figure).
5. `WAVEWATCH III IC0 switch ice concentration cut-off FICE default 0.5 grid points treated as land manual`. Found the Rogers 2018 report. Hit.
6. `Antarctic Tide Gauge database harmonic constants King Padman ATG Casey Mirny Davis amplitude M2 K1 O1`. Hit (AntTG).
7. `море Дейвиса приливы неправильные суточные величина прилива Мирный м` (Russian). Only a commercial tide site; died at the query.
8. `"Shackleton Ice Shelf" OR "Denman Glacier" tide amplitude GNSS OR "tidal flexure" OR "tide model" cm diurnal`. Nothing for this site; died at the query.

**Pages opened:**
- nature.com s41467-026-73203-z (reached after two cookie redirects)
- tellusjournal.org 10.1080/16000870.2018.1454808
- www7320.nrlssc.navy.mil/pubs/2018/rogers-2018.pdf (WebFetch over the size limit; downloaded with curl and converted to text)
- usap-dc.org/view/dataset/601358
- esr.org/?p=1452
- cawcr.gov.au/technical-reports/CTR_070.pdf (closure notice only)
- CSIRO THREDDS catalog, DDS and DAS files

**Scratch files:** `scratchpad/ocean/` (test extraction `test.txt` for February 2015, `months.txt`, `dl/rogers2018.txt`, `dl/esr1452.txt`) and `scratchpad/scripts/fetch_cawcr.sh`. These are session-only.

---

## Resumed session log (2026-10-29, from 12:48 PDT)

**Fix applied:** the time length is now read with `grep -o 'time\[time = [0-9]*'` and then the digits; the variable names are detected per file (`U10`/`V10`/`CI` before mid-2013, `uwnd`/`vwnd`/`ice` after). Tested on 201502 and 197901, then run for all 573 months (two parallel workers, one forward and one in reverse order). Scratch scripts in the new session's scratchpad: `scripts/fetch_cawcr.sh`, `fetch_cawcr_b.sh`, `parse_cawcr.py`, `stats_cawcr.py`, `tidepred.py`, `eot20_pts.py`, `rzip.py` (reads one member out of a remote zip with HTTP range requests).

**Exact search strings run (WebSearch), with outcome:**
9. `CAWCR wave hindcast WAVEWATCH III sea ice concentration threshold "0.75" OR "0.25" ice blocking IC0 Durrant Hemer Trenham Greenslade`. Found the researchdata.edu.au records (model versions, spin-up note); the threshold itself not found (died at the sources).
10. `wave measurements East Antarctica 100°E sea ice waves-in-ice observations SIPEX OR PIPERS OR "Aurora Australis" stereo camera wave height Kohout`. Found SIPEX-2 / Kohout 2014 (120-129°E). The Kohout et al. 2015 DSR-II PDF at ifremer.fr returned 403 (died at the source).
11. `"Denman" OR "Shackleton Ice Shelf" Nuyina 2025 voyage waves swell sea state marine science "Denman Marine Voyage"`. Hit: the DMV voyage report PDF.
12. `обсерватория Мирный приливы колебания уровня моря величина прилива наблюдения` (Russian, new angle: the Mirny observatory). Nothing on Mirny tides (died at the query).
13. `tidal currents Shackleton Ice Shelf Denman Glacier tide model ocean cavity barotropic tides cm/s`. No values; the Padman et al. 2002 paper at Cambridge returned 403 twice (died at the source).
14. `Antarctic continental shelf break diurnal tidal currents amplified topographic waves East Antarctica tidal current speed map CATS Padman Erofeeva`. Found the ESR CATS2008 summary page; no current values for this sector (died at the query for values).
15. `Brancato 2020 Denman Glacier grounding line DInSAR tidal deflection Shackleton Ice Shelf tide amplitude`. Grounding-line results only; no tide amplitude (died at the query).
16. `"tide crack" fast ice Davis OR Casey OR Mirny station Antarctica hazard sea ice travel`. Only other coasts; the Zhongshan paper (figshare) and MDPI paper returned 403; the USAP field-manual copy failed on its certificate (died at the sources).
17. `WMO sea-ice nomenclature "tide crack" definition "line of junction" ice foot fast ice rise and fall of the tide`. Hit: WMO-No. 259 PDF (DMI).
18. `Casey Davis Mawson tide gauge sea level variability bottom pressure gauge Australian Antarctic Division seasonal cycle storm surge inverse barometer`. Found the AAD 2010 news item; the USQ thesis would not open (SSL error; died at the source).
19. `East Antarctic coastal sea level seasonal cycle amplitude cm tide gauge Casey Davis Mawson wind-driven Antarctic Slope Current sea level anomaly`. Found the Hayakawa et al. 2010 abstract; no seasonal-cycle numbers (died at the query).
20. `Bureau of Meteorology tide predictions Australian Antarctic Territory Casey Davis Mawson tide tables`. Found the AAD Casey page and its BoM link; the BoM page returned 403 (died at the source). A commercial site (tidesatlas.com) was not used.
21. `tidal form factor F = (K1+O1)/(M2+S2) classification 0.25 1.5 3.0 mixed mainly semidiurnal mainly diurnal`. Hit (LibreTexts *Coastal Dynamics*; the TU Delft copy gave an SSL error).
22. `Ward 2023 JGR Atmospheres Antarctic coastal cyclones climatology "cyclone density" East Antarctica sector seasonal`. The paper was not found (died at the query).
23. `повторяемость циклонов море Дейвиса Мирный штормовые ветры число дней с ветром более 15 м/с климат` (Russian). Nothing for this sector (died at the query).
24. `100-year return period significant wave height Southern Ocean altimeter global extreme value analysis Young Ribal Takbash Southern Ocean values`. Laloue et al. 2024 (read: maps only, no values in the text); Takbash and Young 2020 at MDPI returned 403. No number for this sector (died at the sources).
25. `EOT20 global ocean tide model SEANOE download ocean_tides netCDF Hart-Davis 2021`. Hit (SEANOE record and download).
26. `Shackleton Ice Shelf Denman trough mooring ADCP velocity tides "tidal" ocean observations Rintoul 2025 Science Advances circulation cavity`. No tidal-current data (died at the query).
27. `NSIDC sea ice concentration climate data record G02202 land spillover coastal contamination limitation user guide`. Found the G10016 v3 page (land-spillover correction).
28. `altimetry tide model sea ice gaps K1 P1 separation aliasing Antarctic coastal errors EOT20 FES2014 high latitude accuracy`. Hit (Andersen et al. 2023, DTU). A review "Advances and Accuracy Assessment of Ocean Tide Models in the Antarctic Ocean" (openpolar record) failed on its certificate (died at the source).
29. `DTU22 ocean tide model download netCDF data.dtu.dk polar Cryosat-2 tides`. No DTU22 tide-model download found (only raw CryoSat-2 residual files on ftp.space.dtu.dk); the DTU23 global tide model ("mainly an update ... in the polar regions") is downloadable from data.dtu.dk (figshare 23828874).

**Pages and files opened (resumed session):** nature.com s41467-026-73203-z (offset 100000, plus two targeted re-reads); researchdata.edu.au/cawcr-wave-hindcast-aggregated-collection/1401722; nature.com/articles/nature13262; the DMV voyage report PDF (IMAS); esr.org/?p=1590; WMO-No. 259 vol. I PDF (download.dmi.dk); antarctica.gov.au news 2010 "rising tide of interest"; antarctica.gov.au Mawson and Casey "climate, weather and tides" pages; jpgu.org SGD001-P13_e.pdf; LibreTexts *Coastal Dynamics* 4.4.1; Wikipedia "October 2022 Southern Ocean cyclone"; sp.copernicus.org Laloue et al. 2024; seanoe.org/data/00683/79489 and its zip; nsidc.org/data/g10016/versions/3; Andersen et al. 2023 PDF (orbit.dtu.dk); space.dtu.dk datasets page; ftp.space.dtu.dk OCEAN_TIDE Readme; figshare API record 23828874 and the DTU23 zip (455 MB, downloaded); the EOT20 `ocean_tides.zip` member (1.2 GB, read out of the SEANOE archive by HTTP range requests); NOAA CoastWatch ERDDAP (`nsidcG02202v6shmday`, `nsidcCDRice_sh_grid`). No slang was encountered, so no slang file was written. **Blocked:** webarchive.nla.gov.au (bot check), ifremer.fr (403), cambridge.org (403 x2), mdpi.com (403 x2), figshare.utas.edu.au (403), webarchive.library.unt.edu (certificate), sear.unisq.edu.au (SSL), bom.gov.au (403), coastal.citg.tudelft.nl (SSL), openpolar.no record (certificate).

