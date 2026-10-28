# PANGAEA downloads (raw data kept for reuse)

| File | What it is | Source | Fetched |
|---|---|---|---|
| `IMAU_AWS16_Princess_Elisabeth_PANGAEA.974126.tab` | Hourly automatic weather station data, **Princess Elisabeth station (Utsteinen)**, 71.949 °S 23.358 °E, 2009-02-02 to 2020-07-03 (92,670 hourly rows; air temperature, humidity, wind, pressure, radiation). 17.8 MB, tab-separated, with a PANGAEA header block ending in `*/`. | Van Tiggelen, Smeets, Tijm-Reijmer, Kuipers Munneke, van den Broeke, van Lipzig, Mangold (2025), IMAU Antarctic automatic weather station data (AWS16), PANGAEA, https://doi.org/10.1594/PANGAEA.974126, CC-BY | 2026-10-28, `curl -sS -m 90 -L "https://doi.pangaea.de/10.1594/PANGAEA.974126?format=textfile"` |

Used for: Utstein's measured monthly means and daily highs and lows (`Reference/Real-World/Climate Data/Climate_Trio_Findings_2026-10-28.md`). Other IMAU AWS datasets (for example AWS05 at Aboa, `10.1594/PANGAEA.974113`) can be fetched the same way by changing the DOI.
