# Climate trio: Sanay, Utstein, Cape Adare — findings (2026-10-28)

> **Status: APPLIED the same day (2026-10-28), after the developer's go-ahead and the Cape Adare proxy ruling (`DR-70`: Possession Island AWS).** Sections 1 to 3 are the findings; what was changed is listed in section 4. Written at the developer's request ("do some research and see what you're able to find; there's a file in the repo documenting climate information for nearly every location in Antarctica; start with that"). The repo source is `to-be-integrated/climate data CURL/` (the NOAA NCEI monthly summaries for about 70 Antarctic stations in `ncei/`, the station list `ncei/ay_stations.txt`, and the BAS READER pages in `reader_2026-10-21/`). **Every number below was computed from those files or from the one new download named in section 2.** Method follows the Aboa precedent (`Aboa_Karkas2004_Monthly_Temperature.md`): replace the **Mean** column with a measured one, and say where it came from.

## 1 · Sanay — SOLVED (measured, at the real station's own location)

**Source.** NOAA NCEI Global Summary of the Month, station `AYM00089004`, **"S.A.N.A.E. AWS"**, 71.70 °S, 2.80 °W, 817 m (the SANAE IV nunatak; SANAE IV is at 71°40′S 2°50′W, about 850 m), file `ncei/AYM00089004.csv`, 2001 to 2026, 230 monthly rows. Each month has 16 to 22 years of data. Mean = the average of the yearly monthly `TAVG`; Avg High / Avg Low = the average of the monthly `TMAX` / `TMIN` (mean daily maximum / minimum).

| Month | Spec Mean now | **Measured Mean** | years | **Avg High** | **Avg Low** |
|---|--:|--:|--:|--:|--:|
| Jan | −5.0 | **−6.7** | 16 | −3.4 | −10.1 |
| Feb | −11.0 | **−10.2** | 17 | −6.7 | −13.8 |
| Mar | −18.0 | **−14.3** | 19 | −10.8 | −17.9 |
| Apr | −25.0 | **−17.5** | 21 | −13.6 | −21.5 |
| May | −29.0 | **−19.4** | 18 | −15.5 | −23.4 |
| Jun | −30.0 | **−21.3** | 17 | −17.1 | −25.6 |
| Jul | −30.0 | **−23.2** | 22 | −18.9 | −27.5 |
| Aug | −28.0 | **−23.0** | 18 | −18.8 | −27.2 |
| Sep | −22.0 | **−21.7** | 19 | −17.7 | −25.8 |
| Oct | −14.0 | **−17.8** | 18 | −14.1 | −21.6 |
| Nov | −7.0 | **−11.7** | 20 | −8.2 | −15.3 |
| Dec | −5.0 | **−7.3** | 18 | −4.1 | −10.4 |

**Annual mean (average of the twelve monthly means): −16.2 °C.** The spec says "approximately −20 °C" (the stub's assumed figure), which is about 4 °C too cold; its winter months (−29 to −30) are 6 to 7 °C too cold. **The spec's Rec High and Rec Low columns already match this same station exactly** (for example Jan +3.9 / −19.8, Jul 0.0 / −46.2), so only the Mean, Avg High, Avg Low and the two summary lines change.

**Cross-check.** The published SANAE IV climate table (Wikipedia, citing the South African Weather Service) gives Jan −7.2 °C and Aug −24.2 °C; the measured values are −6.7 and −23.0, within about 1 °C. The spec's earlier "mean summer −8.3 / mean winter −21.8" are consistent with these monthly means (DJF about −8.1, JJA about −22.5).

## 2 · Utstein — SOLVED (the station's own AWS, hourly data)

**Source.** The spec already names it: IMAU **AWS16, Princess Elisabeth / Utsteinen**, 71.949 °S, 23.358 °E, hourly observations 2009-02-02 to 2020-07-03 (92,670), PANGAEA `10.1594/PANGAEA.974126` (Van Tiggelen et al. 2025). **Downloaded 2026-10-28 with `curl` from the shell** (so no browser save was needed): `https://doi.pangaea.de/10.1594/PANGAEA.974126?format=textfile` (17.8 MB; kept in the repo at `to-be-integrated/climate data CURL/pangaea/IMAU_AWS16_Princess_Elisabeth_PANGAEA.974126.tab`, with a README). Mean = the mean of all hourly `TTT [°C]` in a month, kept only for months with at least 75% of hours present, averaged across years (8 to 12 years per month). Avg High / Avg Low = the average of the daily maximum / minimum, from days with at least 20 hourly values.

| Month | Spec Mean now | **Measured Mean** | years | **Avg High** | **Avg Low** |
|---|--:|--:|--:|--:|--:|
| Jan | −5.0 | **−9.0** | 10 | −6.8 | −11.4 |
| Feb | −12.0 | **−12.4** | 12 | −9.9 | −14.9 |
| Mar | −19.0 | **−16.9** | 12 | −14.6 | −19.5 |
| Apr | −26.0 | **−19.9** | 12 | −17.8 | −22.4 |
| May | −29.0 | **−20.6** | 12 | −18.4 | −23.2 |
| Jun | −30.0 | **−22.3** | 11 | −20.0 | −24.9 |
| Jul | −30.0 | **−24.3** | 10 | −22.0 | −26.9 |
| Aug | −28.0 | **−24.4** | 10 | −21.9 | −27.1 |
| Sep | −22.0 | **−23.7** | 10 | −21.2 | −26.7 |
| Oct | −14.0 | **−19.2** | 9 | −16.6 | −22.4 |
| Nov | −7.0 | **−13.3** | 8 | −10.8 | −16.4 |
| Dec | −5.0 | **−9.3** | 9 | −7.0 | −12.0 |

**Annual mean: −18.0 °C**, which equals the spec's stated −18 °C, so the annual figure was right and the monthly shape was not: the spec's Jan is 4 °C too warm and its Jun to Aug (−30, −30, −28) are 6 to 8 °C too cold. **The spec's Rec High and Rec Low already come from this same AWS.**

**Cross-check.** Published for the station: mean annual −18 °C, February −12.3 °C, July −24.9 °C (Gorodetskaya et al., *Antarctic Science*, via the COMNAP Belgium station catalogue). Measured here: −18.0, −12.4 and −24.4.

## 3 · Cape Adare — CANDIDATES FOR YOUR PROXY RULING (no station at the cape)

The spec's record extremes already use two proxies (Possession Island for eleven months, Adare Hallett for July). Three real records exist near the cape:

| Candidate | Where | Record | What it is |
|---|---|---|---|
| **Possession Island AWS** | 71.88 °S, 171.20 °E, 30 m; about 75 km SE | 1993 to 2026, 23 to 34 years per month (BAS READER) | Automatic station on an island off the open outer coast, the closest and longest record |
| **Adare Hallett** (Hallett Station) | 72.29 °S, 170.31 °E, 5 m; about 113 km S | 1957 to 1973 surface station, 7 to 16 years per month (NOAA) | Inside Moubray Bay, sheltered, much colder winters |
| **Cape Ross AWS** | 76.72 °S, 162.97 °E | 1990 to 2026 (READER) | Too far south to be a sensible proxy; listed only to be ruled out |

| Month | Spec Mean now | Possession Is. | Adare Hallett | Cape Ross |
|---|--:|--:|--:|--:|
| Jan | −2.0 | 1.0 | −1.0 | −3.1 |
| Feb | −8.0 | −2.1 | −3.5 | −8.0 |
| Mar | −14.0 | −8.7 | −10.6 | −15.8 |
| Apr | −19.0 | −16.0 | −17.9 | −20.4 |
| May | −22.0 | −17.9 | −22.8 | −21.4 |
| Jun | −24.0 | −17.2 | −23.4 | −21.5 |
| Jul | −24.0 | −19.3 | −26.6 | −23.8 |
| Aug | −22.0 | −20.0 | −26.7 | −24.2 |
| Sep | −18.0 | −18.5 | −24.3 | −22.2 |
| Oct | −12.0 | −13.2 | −18.7 | −17.0 |
| Nov | −5.0 | −5.2 | −8.6 | −9.0 |
| Dec | −2.0 | 0.6 | −2.0 | −3.4 |
| **Annual mean** | about −12 | **−11.4** | **−15.5** | −15.8 |

**Reading it.** The spec's stated annual mean (about −12 °C) agrees with Possession Island (−11.4 °C), but its monthly shape does not: its winter is 4 to 5 °C colder than Possession Island (Jul −24 against −19.3) and its summer 3 °C colder (Jan −2 against 1.0). Hallett is the cold-winter case (−26.6 in July) because its bay freezes and shelters it from the open sea. **Cape Adare itself is an exposed spit on the open Southern Ocean side**, which is Possession Island's situation, not Hallett's.

**What I could not find.** A modern record for Cape Adare itself: the 1899 Southern Cross expedition (Bernacchi and Colbeck) made winter observations there, held in the Royal Society archive (catalogue MA/367), but no digitized monthly summary turned up. A historical year could be a later sanity check if you want one.

**My recommendation (your ruling).** Use **Possession Island** as the single proxy for the Mean column (nearest, longest, same open-coast exposure), keep Hallett as the stated cold-winter sensitivity case, and keep the spec's existing record extremes as they are. The alternative is a blend of the two, which I would not do without a reason.

## 4 · What applying these would touch (one city at a time, as for Aboa)

Per city: the spec's `Mean annual temperature`, `Temperature range`, the `Mean` / `Avg High` / `Avg Low` columns of the monthly table, the WIND vs COLD callout temperature, the mean summer / winter line (Sanay); the city's `READER/<City>.md` file (rebuilt as a dataset, like Aboa); the climate rows in its datasheets (`Step_1_and_2`) and the line references in its Pre-Trip and ledger; and, for Sanay and Utstein, nothing in the Rec High / Rec Low columns. Polar-night and midnight-sun days and precipitation are unaffected. **Applied 2026-10-28:** the three specs (Mean annual temperature, Temperature range, the Mean column for all three, measured Avg High and Avg Low for Sanay and Utstein, the climate-source and column-provenance lines, and the WIND vs COLD callouts for Sanay, Utstein and Cape Adare, with the cross-city ranks dropped); the three `READER/` files rebuilt; the `Step_1_and_2` climate rows of the three datasheet sets (and Cape Adare's `Phase_3` cross-reference). No spec line count changed. Cape Adare's Avg High and Avg Low remain the earlier derived figures, flagged.

## 5 · Search record (exact strings, per the research-log convention)

- Repo: `ncei/ay_stations.txt` read for stations near 70 to 74 °S at 10 °E to 45 °E, 160 °E to 175 °E and −10 °E to 5 °E; found `AYM00089004`, `AYM00089879`, `AYW00087701`; **no station near 23 °E** in the NOAA list (Utstein has none; its own AWS is in the IMAU data).
- Download: `curl -sS -m 90 -L "https://doi.pangaea.de/10.1594/PANGAEA.974126?format=textfile"` (worked first time).
- Web: `Utsteinen Princess Elisabeth station mean annual air temperature Sør Rondane Gorodetskaya meteorological conditions monthly`; `SANAE IV Vesleskarvet mean annual air temperature climate monthly mean temperature South African Weather Service`; `Cape Adare Southern Cross expedition 1899 meteorological observations mean temperature winter Colbeck Bernacchi` (dead end for a monthly table: archive catalogue entries only).
