# Byrd: the spec's monthly climate table checked against measured data (2026-11-01)

**What this is.** The single-city check queued at the Byrd walk-through (2026-10-31, item 1; Weekly To-Do, Byrd entry (a)): check the spec's monthly table (`Specs/Byrd subnet/Byrd.md` L208–L183) against a data file. The spec gives its source as the "historical Byrd Station record, 1957–1969" and marks the Mean column "not checked against a data file". Run outside the 05:00–14:59 window as a data check (correcting figures against their stated source; no claim about the place or its people is derived).

**Nothing was edited.** The spec, the census and Byrd's `Phase_3.md` sheet are unchanged. Replacing the columns is a decision for the developer (options at the end).

**Claim marks:** SOURCED (URL and figure) · DERIVED (method shown) · NOT FOUND.

## Sources

1. **NOAA NCEI Global Summary of the Month, station `AYW00068201` "BYRD STN" (WMO 89125), 80.0167° S, 119.5333° W, 1,543.2 m.** SOURCED: https://www.ncei.noaa.gov/data/global-summary-of-the-month/access/AYW00068201.csv (downloaded 2026-11-01; 204 months, 1957-01 to 1995-02; the station identity is from NCEI's station list, https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt). Fields used: `TAVG`, `TMAX`, `TMIN` (monthly means of daily mean, maximum and minimum), `EMXT`, `EMNT` (highest and lowest daily value in the month), `PRCP` (monthly total), `DP01` (days with at least 0.01 inch, 0.254 mm). Values are in °C and mm; the round figures (for example −3.3, −8.9) are whole °F readings converted. The other Byrd identifier in NCEI's list, `AYM00089324` "BYRD STATION" (the automatic weather station), has no monthly file (HTTP 404).
2. **Bromwich et al. reconstructed Byrd record, original version (1957–2012).** SOURCED: https://amrdcdata.ssec.wisc.edu/dataset/178af4ae-27c7-408e-a56a-d8acc3b44cf2/resource/58f7b4fe-ae75-4c4c-a480-c13e18021bec/download/byrd_temp_recon_monthly_original.txt (downloaded 2026-11-01; 56 years). Its dataset note says the 1957–1979 part was **revised in September 2013** from Byrd Station observations found later at NCDC; this file is the unrevised original.
3. **The revised, ongoing series (1957 to present)** is listed at https://amrdcdata.ssec.wisc.edu/dataset/reconstructed-byrd-temperature-record-1957-present (updated 2026-06-22), but its data sit at https://polarmet.osu.edu/datasets/Byrd_recon/, which **failed certificate verification** both by direct download and by the web fetch tool ("unable to verify the first certificate"). NOT FOUND tonight; not worked around (certificate checking was not switched off). The dataset's zip holds only a metadata file.

**Cross-check of the site research.** The original file reproduces the 1958–2010 and 1981–2010 monthly means in `Byrd_S1_Site_Ice_Ground_and_Climate_2026-11-01.md` exactly, so S1's table (read through the web fetch tool, which can slip) is confirmed.

**Method (DERIVED).** Monthly means are the plain average of the available years for each calendar month; records are the single highest `EMXT` and lowest `EMNT` per calendar month over the whole file; the yearly precipitation is the sum of the twelve monthly means. Precipitation chance = mean `DP01` days ÷ days in the month. Scripts and downloads are in the session scratchpad (not kept in the repo).

## Results

### Mean, high and low (the station's own 1957–1969 record, the period the spec names)

The station (NCEI) and the reconstruction agree within 0.4 °C in every month, so the two independent sources confirm each other.

| Month | Spec Mean | Station TAVG 1957–1969 (NCEI) | Reconstruction 1957–1969 (original) | Spec − station |
|---|--:|--:|--:|--:|
| Jan | −12.0 | −15.2 (n 12) | −15.2 | +3.2 |
| Feb | −20.0 | −20.1 (n 13) | −20.0 | +0.1 |
| Mar | −29.0 | −28.0 (n 12) | −27.7 | −1.0 |
| Apr | −35.0 | −30.1 (n 13) | −30.0 | −4.9 |
| May | −38.0 | −32.9 (n 13) | −32.8 | −5.1 |
| Jun | −39.0 | −34.5 (n 13) | −34.5 | −4.5 |
| Jul | −40.0 | −36.1 (n 12) | −35.7 | −3.9 |
| Aug | −39.0 | −36.7 (n 13) | −36.8 | −2.3 |
| Sep | −34.0 | −36.7 (n 13) | −36.6 | +2.7 |
| Oct | −25.0 | −31.0 (n 13) | −30.9 | +6.0 |
| Nov | −16.0 | −21.6 (n 13) | −21.6 | +5.6 |
| Dec | −12.0 | −14.9 (n 13) | −14.8 | +2.9 |
| **Annual** | −28.2 | −28.2 | −28.1 | −0.1 |

| Month | Spec Avg High | Station TMAX 1957–1969 | Spec Avg Low | Station TMIN 1957–1969 | Spec day–night spread | Station spread |
|---|--:|--:|--:|--:|--:|--:|
| Jan | −5.0 | −12.1 | −19.0 | −18.4 | 14.0 | 6.4 |
| Feb | −12.0 | −16.2 | −28.0 | −23.9 | 16.0 | 7.7 |
| Mar | −21.0 | −23.6 | −37.0 | −32.4 | 16.0 | 8.8 |
| Apr | −26.0 | −25.2 | −44.0 | −35.0 | 18.0 | 9.8 |
| May | −29.0 | −27.9 | −47.0 | −38.0 | 18.0 | 10.2 |
| Jun | −29.0 | −29.5 | −49.0 | −39.6 | 20.0 | 10.1 |
| Jul | −29.0 | −31.1 | −51.0 | −41.1 | 22.0 | 10.0 |
| Aug | −29.0 | −31.7 | −49.0 | −41.7 | 20.0 | 10.0 |
| Sep | −25.0 | −31.8 | −43.0 | −41.5 | 18.0 | 9.7 |
| Oct | −17.0 | −26.1 | −33.0 | −35.9 | 16.0 | 9.8 |
| Nov | −9.0 | −17.7 | −23.0 | −25.4 | 14.0 | 7.7 |
| Dec | −5.0 | −11.8 | −19.0 | −18.0 | 14.0 | 6.2 |

### Monthly records (whole file, 1957–1988)

| Month | Spec Rec High | NCEI highest monthly max (year) | Match | Spec Rec Low | NCEI lowest monthly min (year) | Match |
|---|--:|--:|:-:|--:|--:|:-:|
| Jan | 5.0 | 5.0 (1988) | yes | −28.9 | −28.9 (1963) | yes |
| Feb | −3.3 | −3.3 (1961) | yes | −40.0 | −40.0 (1969) | yes |
| Mar | −8.9 | −8.9 (1964) | yes | −51.1 | −53.3 (1960) | **no** |
| Apr | −8.3 | −7.2 (1959) | **no** | −56.7 | −56.7 (1963) | yes |
| May | −8.3 | −6.7 (1957) | **no** | −61.7 | −61.7 (1965) | yes |
| Jun | −10.6 | −10.6 (1965) | yes | −61.1 | −61.1 (1969) | yes |
| Jul | −12.2 | −12.2 (1966) | yes | −60.6 | −63.3 (1958) | **no** |
| Aug | −13.9 | −13.3 (1957) | **no** | −62.2 | −62.2 (1958) | yes |
| Sep | −10.0 | −10.0 (1966) | yes | −62.2 | −62.2 (1962) | yes |
| Oct | −12.8 | −11.1 (1960) | **no** | −58.3 | −58.3 (1961) | yes |
| Nov | −6.1 | −4.4 (1957) | **no** | −43.3 | −43.3 (1986) | yes |
| Dec | 1.1 | 1.1 (1987) | yes | −34.4 | −34.4 (1972) | yes |

Record highs matching: 7 of 12. Record lows matching: 10 of 12.

### Precipitation

| Month | Spec Precip (mm) | Station PRCP mean 1957–1988 (mm, n months) | Station days with precipitation (DP01, mean) |
|---|--:|--:|--:|
| Jan | 6 | 5.4 (n 22) | 5.2 |
| Feb | 4 | 4.8 (n 13) | 4.3 |
| Mar | 2 | 3.0 (n 12) | 2.8 |
| Apr | 1 | 3.4 (n 13) | 3.1 |
| May | 5 | 6.2 (n 13) | 4.5 |
| Jun | 3 | 5.8 (n 13) | 3.4 |
| Jul | 2 | 7.4 (n 12) | 3.1 |
| Aug | 1 | 7.0 (n 13) | 2.8 |
| Sep | 0 | 3.3 (n 13) | 1.7 |
| Oct | 1 | 7.1 (n 13) | 2.8 |
| Nov | 2 | 1.9 (n 21) | 1.5 |
| Dec | 3 | 2.4 (n 24) | 2.6 |
| **Year (sum of monthly means)** | 30 | 57.8 | 37.9 |

*Notes on the tables.* Means, highs and lows use the manned-station years 1957–1969 only. The records and the precipitation use every month in the file (1957–1988 for those fields); the summer months (November to January) have more years because later operations ran in summer only. Precipitation chance, DERIVED from `DP01`: Jan 17% · Feb 15% · Mar 9% · Apr 10% · May 15% · Jun 11% · Jul 10% · Aug 9% · Sep 6% · Oct 9% · Nov 5% · Dec 8%, against the spec's ~8% · ~5% · ~2% · ~1% · ~4% · ~4% · ~2% · ~1% · ~0% · ~0% · ~2% · ~4%.

## What the check shows

1. **Mean column: the annual figure is right, the months are not.** Spec −28.2 °C a year; station −28.2 °C. But March to August run 1.0–5.1 °C too cold and September to January 2.7–6.0 °C too warm. The measured year is flatter: the coldest months are August and September (−36.7 °C), not July at −40.
2. **Avg High and Avg Low: wrong, and wrongly labeled.** The spec calls them "derived" because "the station publishes … no mean daily max/min"; NCEI holds both, measured. The spec's day–night spread (14–22 °C) is about twice the measured spread (6.2–10.2 °C). Its lows are 4.6–9.9 °C too cold from March to August.
3. **Record highs 7 of 12 match, record lows 10 of 12.** Every mismatch is a spec value *less extreme* than the station's record, and all seven of the station's records that the spec misses were set in 1957–1960 (three spec record highs equal the station's second-highest reading). This fits a source that missed the earliest years.
4. **Precipitation: the column does not match the station either.** Spec 30 mm a year; station gauge about 58 mm (1957–1988), with a different monthly shape (the spec has 0–2 mm in July to October; the gauge has 3.3–7.4 mm). The spec labels the column "measured". This adds a third figure to the precipitation question already flagged in the Byrd research tracker (section 0.8, item 1): spec 30 mm, station gauge about 58 mm, glaciological accumulation 67–156 mm water equivalent (S1). Gauges are known to under-catch blowing snow; that explanation is not checked here.
5. **Not checked:** the Daylight column (computed from latitude; S1 confirmed the polar-night and midnight-sun counts) and the Notes column.

## Options for the developer (nothing applied)

- **A.** Replace the Mean, Avg High, Avg Low, Rec High and Rec Low columns with the station's measured values above (the source and period the spec already names), relabel the High/Low provenance as measured, and write the same values into `Phase_3.md`.
- **B.** Use a later period for the means (the reconstruction's 1981–2010 means are in S1; the observed 2013–2025 automatic-station means are in S1 too). No high, low or record columns exist for those periods in this check.
- **C.** Keep the spec's table and label it as not matching the measured record.
- **Precipitation** goes with the precipitation decision (tracker 0.8, item 1), not with A–C.
