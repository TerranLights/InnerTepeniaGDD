# Relung Panen ocean-side research (2026-10-29)

**Brief:** `Relung_Panen_Ocean_Research_BRIEF_2026-10-29.md` (this folder). Real physical environment and real precedents only for the sea off the Shackleton Ice Shelf / Bunger Hills coast (about 95-105E, 64-66S). No design, no recommendation; the developer decides.

**Already known (not repeated):** the four port files `Relung_Panen_Port_Research_2026-10-25_A` to `_D` (this folder).

**Labels:** SOURCED = read at the source page (WebFetch) during this session. UNVERIFIED = seen only in a search snippet, or recalled, or inferred; not confirmed at the source.

## PROGRESS

- [ ] 1 Sea state and swell
- [ ] 2 Tides and water level
- [ ] 3 Currents and water properties
- [ ] 4 Sea ice for floating or moored structures
- [ ] 5 Icebergs and calving hazards
- [ ] 6 Wind and atmosphere over the water
- [ ] 7 Ship access from Hobart and Fremantle
- [ ] 8 Real precedents for a floating or moored gateway
- [ ] FINAL

Started 2026-10-29 12:31 PDT. Stopped 2026-10-29 about 12:43 PDT at the coordinator's request (session closing). **No item is complete; nothing is ticked.** Partial material for items 1 and 2 is below, then the STOP note.

---

## 1. Sea state and swell (PARTIAL, not complete)

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

## 2. Tides and water level (PARTIAL, not complete)

- **SOURCED** (Antarctic Tide Gauge database, Howard, King and Padman 2020, doi:10.15784/601358; read on the ESR browse page `https://www.esr.org/?p=1452`, raw page text downloaded). **No gauge lies between about 78°E and 110°E**; the stations nearest the Shackleton front are Davis and Casey. Amplitudes in cm (Greenwich phases in degrees in brackets), each from a 365-day bottom-pressure record with a 3,600 s sample interval:

| Station | Position | Q1 | O1 | P1 | K1 | N2 | M2 | S2 | K2 |
|---|---|---|---|---|---|---|---|---|---|
| Casey (20120-) | 66.283°S 110.533°E | 6.4 (224.2) | 26.5 (233.7) | 8.6 (242.4) | 26.6 (243.7) | 7.3 (120.5) | 29.3 (142.9) | 16.9 (200.1) | 4.7 (199.4) |
| Davis (20100-) | 68.45°S 77.967°E | 7.2 (260.7) | 28.8 (269.0) | 8.8 (276.0) | 27.8 (277.0) | 5.7 (168.2) | 20.1 (208.5) | 17.7 (307.1) | 5.1 (308.8) |
| Mawson (20080-) | 67.6°S 62.867°E | 6.0 | 25.4 | 7.7 | 23.4 | 2.3 | 3.1 | 11.4 | 3.3 |

- **DERIVED** (arithmetic on the Casey row only; not a prediction): the eight Casey amplitudes sum to 126.3 cm. That gives a theoretical ceiling of about 2.5 m on the peak-to-trough tidal range there if every constituent peaked together. The real maximum is lower, and no prediction was run. Casey is about 440 km east of the Shackleton front, so **this is not a figure for the front.**
- The diurnal (O1, K1) and semidiurnal (M2, S2) amplitudes are of similar size at Casey and Davis, which means a mixed tide (my reading of the table; no source states it for this coast).
- **NOT FOUND (so far):** a tidal range or model value at the Shackleton front itself, tidal currents, and tide cracks offshore. CATS2008 and the AntTG text file are behind a captcha download form at USAP-DC (died at the source). A commercial tide-prediction site (nashaplaneta.net, "186 cm" at Davis on one day) turned up in a search and was **not used**.

---

## STOP NOTE (2026-10-29, about 12:43 PDT): session closed by the coordinator

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

