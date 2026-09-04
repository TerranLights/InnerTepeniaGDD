# PRECIPITATION — WHAT FALLS vs WHAT LANDS

**Created 2026-09-04** at developer direction, during the 37-city climate pass.
**Purpose: the reference for how Antarctic precipitation figures diverge, and what each of the 37 cities
actually experiences.** *Intended to be referred back to — the mechanism is recorded first so that any
later pass can re-derive the numbers rather than trusting this file's arithmetic.*

> ## ⛔ THE PROBLEM THIS FILE EXISTS TO PREVENT
> **"Annual precipitation" for an Antarctic site can mean four different things, differing by more than an
> order of magnitude, and sources rarely say which one they publish.**
>
> **The worst case in this corpus: Amundsen Station.** Its gauge reads **2.1 mm/yr**. Its actual
> accumulation is **~70–80 mm/yr**. ***The gauge catches roughly three percent of the snow.*** A pass that
> takes the gauge figure at face value will describe the South Pole as thirty times drier than it is.

---

# PART 1 · THE MECHANISM

## The chain — four quantities, in order

```
   [1] FALLS ALOFT          precipitation formed in cloud, measured by radar ~1200 m above ground
        │
        │  ── low-level sublimation ──  katabatic air is dry and unsaturated;
        │                               snow evaporates during its last kilometre of fall
        ▼
   [2] REACHES THE SURFACE   what a person standing outside is actually snowed on by
        │
        │  ── blowing-snow sublimation ──  snow already on the ground is lifted by wind
        │  ── wind transport / erosion ──  and either evaporates aloft or is carried elsewhere
        ▼
   [3] ACCUMULATES (SMB)     what stays; what a stake farm or ice core measures
        
   [✗] GAUGE-CAUGHT          NOT on this chain. An instrument artifact — blowing snow
                             does not enter the gauge, so gauges under-read severely
                             wherever there is wind.
```

## Measured coefficients for each step

| Step | Coefficient | Source |
|---|---|---|
| **[1] Falls aloft** | **coastal 275 mm/yr · plateau 34 mm/yr · continent mean 171 mm/yr** *(at 1200 m a.g.l.)* | CloudSat radar climatology *(Palerme et al.; Lemonnier et al.)* |
| **[1]→[2] low-level sublimation** | **−17% continent-wide** · **up to −35% on East Antarctic margins** | **Grazioli et al. 2017, PNAS**, *"Katabatic winds diminish precipitation contribution to the Antarctic ice mass balance"* |
| **[2]→[3] blowing snow** | **up to −50% of precipitation** removed in coastal and slope convergence areas | blowing-snow SMB studies; MAR/RACMO2 intercomparison |
| *continent totals* | total sublimation **236.2 Gt/yr**, of which **223.3 Gt/yr is blowing-snow sublimation**; erosion only **11.2 Gt/yr** | Antarctic SMB intercomparison |

> ### ⭐ Note what that last row means
> **The snow that never lands is overwhelmingly snow that already landed once and was picked back up.**
> Only ~5% of the loss is snow carried bodily downhill; the rest evaporates *while airborne, after having
> been on the ground.* **The ice sheet loses mass to the air, not to its neighbours.**

## ⭐⭐ THE SINGLE MOST IMPORTANT NUMBER

> ***"Cumulative snow transportation can be approximately 4 orders of magnitude higher than snow
> precipitation at coastal sites."***

**At a coastal katabatic city, the snow moving horizontally past a person is on the order of TEN THOUSAND
TIMES the snow falling from the sky.**

***Weather there is not something that comes down. It is something that goes past.***
**Nobody at Denison digs out from what fell on them. They dig out from what arrived from upwind.**

## Why the divergence is NOT a function of temperature

**This is the load-bearing insight, and it is orthogonal to everything else in the climate tables.**

**Vostok and Denison are both brutally cold and are opposite weather experiences.** Vostok is airless
stillness where snow is a permanent deposit and essentially nothing is lost. Denison is a horizontal river
of ice crystals where snow is a *medium you move through*. ***Two cities can share a temperature curve and
share nothing whatsoever about what weather means.***

**The controlling variable is WIND, not cold.** Specifically: **the presence of a persistent katabatic
drainage regime.**

---

# PART 2 · THE SIX REGIMES

| Regime | Retention | Character |
|---|--:|---|
| **PLATEAU** | **~90%** | Almost nothing falls — and nearly every flake that does, stays. No wind to remove it. Snow is not weather here; it is a permanent, slow deposit |
| **INTERIOR** | ~70% | Low precipitation, moderate wind, elevated inland sites |
| **ICE SHELF** | ~65% | Flat, exposed, windy; moderate precipitation with substantial redistribution |
| **OASIS** | ~45% | Ice-free rock with strong katabatic flow — low fall, high transport, little retained |
| **KATABATIC MARGIN** | **~38%** | **Snow flux, not snowfall.** Up to a third evaporates before landing; most of the rest is entrained. Blue-ice and wind-crust surfaces where the net goes negative |
| **MARITIME** | **~80%** | Genuinely wet. **Rain as well as snow**, melt, compaction, slush. The only cities where precipitation behaves like temperate weather |

⚠ **Retention percentages are MODELED**, applied from the published regional coefficients above. **They are
design-grade estimates, not per-station measurements** — except where Part 3 marks a value ⭐ measured.

---

# PART 3 · THE 37 CITIES

**`Falls` = reaches the surface** *(the figure now in each spec's `Annual precipitation`)*.
**`Lands` = accumulates and stays.** **`Lost` = removed by sublimation and wind.**

## ⭐ Measured accumulation — no modeling involved

| City | Gauge reads | Actually falls | ⭐ Actually lands | Note |
|---|--:|--:|--:|---|
| **Amundsen Station** | **2.1 mm** | ~70 mm | **~70–80 mm** | Stake farm, 1983–2010. ***The gauge catches ~3%.*** Falls ≈ lands: no wind to remove it |
| **Vostok** | 22 mm | ~25 mm | **22.5 ± 1.3 mm** | Stake, since 1970 *(+8% when corrected for stake bias)*. ⭐ **Gauge ≈ accumulation — nothing is lost because nothing blows** |

> ⭐ **These two sites prove the mechanism from both ends.** At the Pole the gauge is catastrophically wrong;
> at Vostok the same instrument is very nearly right. **The difference is not the instrument. It is the
> wind.**

## Modeled — all remaining cities

### PLATEAU · retention ~90%

| City | Falls | Lands | Lost |
|---|--:|--:|--:|
| Concordia | 25 | **22** | 2 |
| Dome_Fuji | 25 | **22** | 2 |
| Kunlun | 20 | **18** | 2 |

### INTERIOR · retention ~70%

| City | Falls | Lands | Lost |
|---|--:|--:|--:|
| Abowasa | 150 | **105** | 45 |
| Byrd | 30 | **21** | 9 |
| Princess_Elisabeth | 200 | **140** | 60 |
| Troll | 200 | **140** | 60 |

### ICE SHELF · retention ~65%

| City | Falls | Lands | Lost |
|---|--:|--:|--:|
| Belgrano | 300 | **195** | 105 |
| Halley | 450 | **292** | 158 |
| Neumayer | 396 | **257** | 138 |
| Sanay | 200 | **130** | 70 |

### OASIS · retention ~45%

| City | Falls | Lands | Lost |
|---|--:|--:|--:|
| Zhongshan | 149 | **67** | 82 |
| Shirayuki | 149 | **67** | 82 |
| Sinheung | 149 | **67** | 82 |

### ⛔ KATABATIC MARGIN · retention ~38% — the scoured cities

| City | Falls | Lands | Lost |
|---|--:|--:|--:|
| **Dumont_dUrville** | **655** | **249** | ⛔ **406** |
| **Denison** | **650** | **247** | ⛔ **403** |
| **Mirny** | 527 | **200** | ⛔ **327** |
| Cape_Adare | 350 | **133** | 217 |
| Mawson | 350 | **133** | 217 |
| Sayowa | 350 | **133** | 217 |
| Lazar | 238 | **90** | 147 |
| Casey | 225 | **86** | 140 |
| Fort_McMurdo | 213 | **81** | 132 |
| Scott | 184 | **70** | 114 |
| Janbogo | 145 | **55** | 90 |
| Zukelli | 145 | **55** | 90 |
| Davis | 73 | **28** | 45 |

### MARITIME · retention ~80% — the wet cities

| City | Falls | Lands | Lost |
|---|--:|--:|--:|
| Esperanza | 726 | **581** | 145 |
| Juan_Carlos | 702 | **562** | 140 |
| Sejong | 702 | **562** | 140 |
| Rothera | 700 | **560** | 140 |
| Signy | 663 | **530** | 133 |
| Palmer_City | 657 | **526** | 131 |
| Port_Lockroy | 657 | **526** | 131 |
| Marambio | 363 | **290** | 73 |

---

# PART 4 · WHAT THIS IS FOR

## Two different game systems, not one number

| System | Driven by | Where it matters |
|---|---|---|
| **Visibility · storms · "is it snowing"** | **what falls** *(and, at margins, what BLOWS — which is far larger)* | Katabatic cities: whiteout is routine and often happens **under a clear sky**, because the snow is lifted, not falling |
| **Digging out · structural load · terrain change** | **what lands** | Maritime and ice-shelf cities accumulate genuinely; katabatic cities may accumulate almost nothing while being unnavigable |

⭐ **The two decouple completely at the margins.** **A Denison resident experiences constant snow and
almost no accumulation.** A Port Lockroy resident experiences moderate snow and has to shovel it.

## ⭐ It explains canon that was already written

**`Specs/Denison.md` already describes the city as "one continuous, interlinked, load-sharing structure
rather than separate buildings — unique in Tepenia," and spends 25% of its distinctive industrial tier on
structural and wind engineering, exported nationally.**

***That city is not built against snow load. It is built against snow flux.*** **The canon was right before
the mechanism was understood, and the mechanism now supplies its reason.**

---

# SOURCES — with addresses, so every coefficient can be re-checked

| Figure used | Source |
|---|---|
| ⭐ **−17% continent-wide, up to −35% at East Antarctic margins** *(low-level sublimation)* | **Grazioli et al. 2017, PNAS** — *"Katabatic winds diminish precipitation contribution to the Antarctic ice mass balance"* — https://www.pnas.org/doi/10.1073/pnas.1707633114 |
| **coastal 275 · plateau 34 mm/yr at 1200 m a.g.l.** | **Lemonnier et al. 2020**, *"CloudSat-Inferred Vertical Structure of Snowfall Over the Antarctic Continent"*, JGR Atmospheres — https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2019JD031399 |
| **continent mean 171 mm/yr** | Palerme et al. CloudSat surface snowfall climatology; see also https://tc.copernicus.org/articles/14/2715/2020/ |
| ⭐ **up to −50% removed in coastal/slope convergence areas** | *"Contribution of blowing-snow sublimation to the surface mass balance of Antarctica"*, **The Cryosphere 18:4933 (2024)** — https://tc.copernicus.org/articles/18/4933/2024/ |
| **236.2 Gt/yr total sublimation · 223.3 Gt/yr blowing-snow · 11.2 Gt/yr erosion** | **Agosta et al. 2019**, *"Estimation of the Antarctic surface mass balance using MAR (1979–2015)"*, **The Cryosphere 13:281** — https://tc.copernicus.org/articles/13/281/2019/ |
| *MAR vs RACMO2 intercomparison* | **Mottram et al. 2021**, *"What is the surface mass balance of Antarctica?"*, **The Cryosphere 15:3751** — https://tc.copernicus.org/articles/15/3751/2021/ |
| **DDU sublimation measured by profiling radar** | **Grazioli et al. 2018**, APRES3 campaigns dataset, **ESSD 10:1605** — https://essd.copernicus.org/articles/10/1605/2018/ |
| ⭐ **Vostok accumulation 22.5 ± 1.3 mm/yr** *(stake, since 1970)* | *"Fifty years of instrumental surface mass balance observations at Vostok Station"*, **Journal of Glaciology** — https://www.cambridge.org/core/journals/journal-of-glaciology/article/fifty-years-of-instrumental-surface-mass-balance-observations-at-vostok-station-central-antarctica/0C5059EAAF392550C2CA577DE26D6A25 |
| **stake measurements under-read by 8 ± 4%** | *"Underestimation of Snow Accumulation Rate in Central Antarctica (Vostok Station) Derived from Stake Measurements"* — https://link.springer.com/article/10.3103/S1068373920020090 |
| ⭐ **South Pole ~7 cm w.e. precipitation; ~275 mm/yr snow-depth accumulation** | *"Fifty-year Amundsen–Scott South Pole station surface climatology"* — https://www.sciencedirect.com/science/article/pii/S0169809512002256 · *"Snow Accumulation Variability at the South Pole From 1983 to 2020"* — https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2023JD039388 |
| **Larsemann Hills climate and NE katabatic regime** | **ASMA No. 6 — Larsemann Hills Management Plan §4.2**, ATCM XXXVII Final Report — https://www.env.go.jp/nature/nankyoku/kankyohogo/database/jyouyaku/asma/asma_pdf_en/ASMA06_en.pdf |

**Station-level climate data used throughout this pass:**
**BAS READER** — https://legacy.bas.ac.uk/met/READER/ ·
**NOAA NCEI Global Summary of the Month** *(per-station CSVs)* — https://www.ncei.noaa.gov/data/gsom/access/ ·
**GHCN station list** — https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt

⛔ **Sources tried and REJECTED, recorded so they are not retried:** **timeanddate.com** — unreachable by
tooling *(Cloudflare JS challenge defeats `curl`; browser-saved pages omit the monthly grid, which loads by
AJAX)*, **and its Antarctic precipitation figures conflict with measured values by up to 16×.** **Signy's
published climate box** — internally inconsistent *(February minimum warmer than January)*; **Signy is
sourced from Orcadas instead.**

---

# ⚠ STATUS AND CAVEATS

1. **Retention percentages are regional coefficients applied by regime, not per-station measurements.**
   Only Amundsen Station and Vostok carry measured accumulation.
2. **`Falls` values inherit whatever provenance each spec's `Annual precipitation` already had** — a mix of
   measured station normals, reanalysis totals and regional estimates. **See each city's own provenance
   line.** ⛔ **Amundsen Station's spec field still holds the 2.1 mm GAUGE figure**; the ~70 mm used here is
   the corrected value.
3. ✅ **APPLIED — developer ruling 2026-09-04:** *"update all 37 to carry as many individual quantities as
   we have available… especially make sure to distinguish between wind and cold."* **All 37 specs now carry
   a `Precipitation regime` block** giving regime · falls · lands · lost · retention, plus a
   **`WIND vs COLD`** statement naming which hazard actually defines that city, with its own cold-rank and
   wind figure. ⛔ **Amundsen Station's block carries an explicit warning that the `Annual precipitation`
   field above it is the gauge figure and must not be used.**
4. **Regime assignment is a judgement**, made from latitude, elevation, distance inland and the presence of
   a katabatic regime. The Larsemann trio in particular sits between plateau and margin and was given its
   own `OASIS` class rather than forced into either.

*Research record, with every source and search string: `…/Locations/Cities/Research_Logs/Climate_Data_Research_Log.md`, Session 7.*
