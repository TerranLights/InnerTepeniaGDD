# READER recomputed normals vs the specs' `Mean` column — 2026-10-21

Produced by `Tools/climate_reader_check.py` (read-only). Source: the BAS Met READER tables (`legacy.bas.ac.uk/met/READER/`), downloaded 2026-10-21; raw pages archived in `to-be-integrated/climate data CURL/reader_2026-10-21/`.

**Method.** Surface stations: mean of the yearly monthly values over 1991–2020. Automatic weather stations (AWS), whose records are short: every full year 1991–2025. A month needs ≥ 10 years or it is left blank. **The method is proven by the control set below: cities whose specs really were taken from READER match to ≤ 0.1 °C.**

## 1 · The control set — specs known to be READER-sourced (method proof)
| City | READER station | months | difference from the spec |
|---|---|--:|---|
| Zukelli | surface `Mario_Zucchelli` | 12 | max 0.1 · mean 0.0 (worst Jun: spec -20.1 vs -20.0) |
| Rothera | surface `Rothera` | 12 | max 0.0 · mean 0.0 (worst Mar: spec -0.9 vs -0.9) |
| Marambio | surface `Marambio` | 12 | max 0.1 · mean 0.0 (worst Sep: spec -10.6 vs -10.7) |
| Esperanza | surface `Esperanza` | 12 | max 0.1 · mean 0.0 (worst Jul: spec -10.9 vs -10.8) |
| Neumayer | surface `Neumayer` | 12 | max 0.0 · mean 0.0 (worst Apr: spec -18.1 vs -18.1) |
| Belgrano | surface `Belgrano_II` | 12 | max 0.2 · mean 0.0 (worst Apr: spec -16.3 vs -16.5) |
| Casey | surface `Casey` | 12 | max 0.0 · mean 0.0 (worst Jun: spec -14.4 vs -14.4) |
| Davis | surface `Davis` | 12 | max 0.0 · mean 0.0 (worst Aug: spec -17.1 vs -17.1) |
| Mirny | surface `Mirny` | 12 | max 0.1 · mean 0.0 (worst Mar: spec -10.5 vs -10.4) |
| Zhongshan | surface `Zhongshan` | 12 | max 0.0 · mean 0.0 (worst Jul: spec -16.1 vs -16.1) |
| Shirayuki | surface `Zhongshan` | 12 | max 0.0 · mean 0.0 (worst Jul: spec -16.1 vs -16.1) |
| Ariun Nuur | surface `Vostok` | 12 | max 0.1 · mean 0.0 (worst Dec: spec -31.3 vs -31.4) |
| Mawson | surface `Mawson` | 12 | max 0.0 · mean 0.0 (worst Jun: spec -16.3 vs -16.3) |
| Dumont d'Urville | surface `Dumont_Durville` | 12 | max 0.1 · mean 0.0 (worst Apr: spec -13.5 vs -13.4) |
| Scott | surface `Scott_Base` | 12 | max 0.0 · mean 0.0 (worst May: spec -26.2 vs -26.2) |
| Fort McMurdo | surface `McMurdo` | 12 | max 0.9 · mean 0.2 (worst May: spec -21.5 vs -22.4) |

## 2 · The cities that had a stub READER file, and the others tested
| City | READER station | months | difference from the spec `Mean` |
|---|---|--:|---|
| Halley | surface `Halley` | 12 | max 0.0 · mean 0.0 (worst Jun: spec -27.5 vs -27.5) |
| Lazar | surface `Novolazarevskaya` | 12 | max 0.1 · mean 0.0 (worst Aug: spec -17.2 vs -17.2) |
| Janbogo | surface `Mario_Zucchelli` | 12 | max 0.1 · mean 0.0 (worst Sep: spec -19.8 vs -19.8) |
| Janbogo (cross-check) | aws `Terra_Nova_Bay` | 12 | max 1.2 · mean 0.2 (worst Sep: spec -19.8 vs -18.6) |
| Troll | aws `Troll` | 12 | max 0.1 · mean 0.0 (worst Jul: spec -25.2 vs -25.2) |
| Kunlun | aws `Dome_A` | 12 | max 0.0 · mean 0.0 (worst Jul: spec -63.7 vs -63.7) |
| Dome Fuji | aws `Dome_F` | 12 | max 0.0 · mean 0.0 (worst Oct: spec -52.6 vs -52.6) |
| Cape Adare (candidate proxy) | aws `Possession_Island` | 12 | max 6.8 · mean 3.3 (worst Jun: spec -24 vs -17.2) |
| Cape Adare (candidate proxy) | aws `Cape_Ross` | 12 | max 5.0 · mean 2.0 (worst Oct: spec -12 vs -17.0) |
| Sinheung (a finished city) | surface `Zhongshan` | 12 | max 0.0 · mean 0.0 (worst Jul: spec -16.1 vs -16.1) |

### Month-by-month

#### Halley — READER surface `Halley` (record, 40 yrs on file 1987–2026; normal over 1991–2020)

| | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **READER normal** | -4.7 | -10.4 | -17.4 | -23.3 | -25.5 | -27.5 | -29.0 | -29.1 | -26.8 | -20.2 | -11.0 | -5.3 |
| years in the normal | 30 | 30 | 29 | 30 | 30 | 30 | 30 | 30 | 30 | 30 | 30 | 30 |
| **Spec `Mean`** | -4.7 | -10.4 | -17.4 | -23.3 | -25.5 | -27.5 | -29 | -29.1 | -26.8 | -20.2 | -11 | -5.3 |
| difference | +0.0 | +0.0 | -0.0 | +0.0 | -0.0 | +0.0 | +0.0 | +0.0 | -0.0 | +0.0 | +0.0 | -0.0 |

#### Lazar — READER surface `Novolazarevskaya` (record, 66 yrs on file 1961–2026; normal over 1991–2020)

| | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **READER normal** | -0.4 | -3.2 | -7.9 | -11.8 | -13.5 | -14.5 | -17.0 | -17.2 | -16.5 | -12.0 | -5.6 | -1.0 |
| years in the normal | 30 | 30 | 30 | 30 | 30 | 30 | 30 | 30 | 30 | 30 | 30 | 30 |
| **Spec `Mean`** | -0.4 | -3.2 | -7.9 | -11.8 | -13.5 | -14.5 | -17 | -17.2 | -16.5 | -12 | -5.6 | -1 |
| difference | +0.0 | +0.0 | -0.0 | -0.0 | -0.0 | +0.0 | +0.0 | +0.1 | -0.0 | +0.0 | +0.0 | +0.0 |

#### Janbogo — READER surface `Mario_Zucchelli` (record, 40 yrs on file 1987–2026; normal over 1991–2020)

| | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **READER normal** | -1.2 | -6.4 | -14.1 | -19.0 | -20.0 | -20.0 | -21.8 | -21.4 | -19.8 | -15.0 | -7.3 | -1.5 |
| years in the normal | 28 | 30 | 30 | 29 | 28 | 28 | 27 | 28 | 28 | 29 | 29 | 28 |
| **Spec `Mean`** | -1.2 | -6.4 | -14.1 | -19 | -20 | -20 | -21.8 | -21.4 | -19.8 | -15 | -7.3 | -1.5 |
| difference | +0.0 | -0.0 | +0.0 | +0.0 | -0.0 | -0.0 | +0.0 | +0.0 | -0.1 | +0.0 | +0.0 | -0.0 |

#### Janbogo (cross-check) — READER aws `Terra_Nova_Bay` (record, 40 yrs on file 1987–2026; normal over 1991–2025)

| | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **READER normal** | -1.2 | -6.2 | -14.1 | -19.1 | -20.1 | -19.9 | -21.4 | -21.0 | -18.6 | -14.8 | -7.3 | -1.5 |
| years in the normal | 35 | 35 | 35 | 34 | 31 | 31 | 31 | 31 | 31 | 33 | 35 | 35 |
| **Spec `Mean`** | -1.2 | -6.4 | -14.1 | -19 | -20 | -20 | -21.8 | -21.4 | -19.8 | -15 | -7.3 | -1.5 |
| difference | -0.0 | -0.2 | -0.0 | +0.1 | +0.1 | -0.1 | -0.4 | -0.4 | -1.2 | -0.2 | -0.0 | -0.0 |

#### Troll — READER aws `Troll` (record, 26 yrs on file 2001–2026; normal over 1991–2025)

| | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **READER normal** | -6.7 | -10.3 | -14.2 | -19.8 | -21.1 | -22.8 | -25.2 | -25.3 | -24.0 | -18.5 | -11.4 | -6.9 |
| years in the normal | 14 | 14 | 13 | 13 | 13 | 13 | 14 | 14 | 13 | 14 | 14 | 14 |
| **Spec `Mean`** | -6.7 | -10.3 | -14.2 | -19.8 | -21.1 | -22.8 | -25.2 | -25.3 | -24 | -18.5 | -11.4 | -6.9 |
| difference | +0.0 | -0.0 | +0.0 | -0.0 | +0.0 | +0.0 | +0.1 | +0.0 | -0.0 | -0.0 | +0.0 | -0.0 |

#### Kunlun — READER aws `Dome_A` (record, 22 yrs on file 2005–2026; normal over 1991–2025)

| | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **READER normal** | -34.9 | -44.0 | -55.2 | -61.4 | -62.4 | -63.4 | -63.7 | -64.2 | -62.9 | -55.4 | -44.3 | -35.7 |
| years in the normal | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 |
| **Spec `Mean`** | -34.9 | -44 | -55.2 | -61.4 | -62.4 | -63.4 | -63.7 | -64.2 | -62.9 | -55.4 | -44.3 | -35.7 |
| difference | +0.0 | -0.0 | +0.0 | +0.0 | -0.0 | -0.0 | -0.0 | -0.0 | -0.0 | +0.0 | -0.0 | +0.0 |

#### Dome Fuji — READER aws `Dome_F` (record, 30 yrs on file 1997–2026; normal over 1991–2025)

| | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **READER normal** | -29.6 | -41.5 | -55.2 | -62.9 | -64.0 | -65.1 | -66.0 | -64.2 | -62.7 | -52.6 | -39.3 | -29.7 |
| years in the normal | 14 | 13 | 15 | 15 | 16 | 16 | 14 | 11 | 12 | 17 | 12 | 12 |
| **Spec `Mean`** | -29.6 | -41.5 | -55.2 | -62.9 | -64 | -65.1 | -66 | -64.2 | -62.7 | -52.6 | -39.3 | -29.7 |
| difference | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | -0.0 | +0.0 | -0.0 | -0.0 | +0.0 | -0.0 | +0.0 |

#### Cape Adare (candidate proxy) — READER aws `Possession_Island` (record, 34 yrs on file 1993–2026; normal over 1991–2025)

| | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **READER normal** | 1.0 | -2.1 | -8.7 | -16.0 | -17.9 | -17.2 | -19.3 | -20.0 | -18.5 | -13.2 | -5.2 | 0.6 |
| years in the normal | 33 | 33 | 33 | 33 | 33 | 31 | 23 | 27 | 33 | 33 | 33 | 32 |
| **Spec `Mean`** | -2 | -8 | -14 | -19 | -22 | -24 | -24 | -22 | -18 | -12 | -5 | -2 |
| difference | -3.0 | -5.9 | -5.3 | -3.0 | -4.1 | -6.8 | -4.7 | -2.0 | +0.5 | +1.2 | +0.2 | -2.6 |

#### Cape Adare (candidate proxy) — READER aws `Cape_Ross` (record, 37 yrs on file 1990–2026; normal over 1991–2025)

| | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **READER normal** | -3.1 | -8.0 | -15.8 | -20.4 | -21.4 | -21.5 | -23.8 | -24.2 | -22.2 | -17.0 | -9.0 | -3.4 |
| years in the normal | 35 | 35 | 35 | 35 | 35 | 35 | 35 | 35 | 35 | 35 | 35 | 35 |
| **Spec `Mean`** | -2 | -8 | -14 | -19 | -22 | -24 | -24 | -22 | -18 | -12 | -5 | -2 |
| difference | +1.1 | -0.0 | +1.8 | +1.4 | -0.6 | -2.5 | -0.2 | +2.2 | +4.2 | +5.0 | +4.0 | +1.4 |

#### Sinheung (a finished city) — READER surface `Zhongshan` (record, 38 yrs on file 1989–2026; normal over 1991–2020)

| | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **READER normal** | 0.2 | -2.9 | -8.3 | -13.1 | -15.2 | -14.6 | -16.1 | -16.1 | -15.4 | -12.0 | -4.8 | -0.5 |
| years in the normal | 30 | 30 | 30 | 30 | 30 | 30 | 30 | 30 | 30 | 30 | 30 | 30 |
| **Spec `Mean`** | 0.2 | -2.9 | -8.3 | -13.1 | -15.2 | -14.6 | -16.1 | -16.1 | -15.4 | -12 | -4.8 | -0.5 |
| difference | -0.0 | -0.0 | +0.0 | +0.0 | -0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | -0.0 |

## 3 · Specs whose own `Mean` falls outside the same row's low–high range (impossible)
| Spec | months | which |
|---|--:|---|
| Sanay | 6 | Apr, May, Jun, Jul, Oct, Nov |
| Troll | 2 | May, Jun |
| Dome_Fuji | 12 | Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec |
| Kunlun | 12 | Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec |
| Rothera | 4 | Mar, Apr, May, Jun |
