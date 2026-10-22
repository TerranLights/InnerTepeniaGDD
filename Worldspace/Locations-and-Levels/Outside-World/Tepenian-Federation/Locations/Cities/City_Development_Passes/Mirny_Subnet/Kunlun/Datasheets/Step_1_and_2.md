# Kunlun — Datasheet · Step 1, Step 2 & Phase 1 (Constraint & Capability) — MERGED

> ⚠ **DRAFT — Tier C.** Merged per the Field Guide's consolidated 19-file shape: Step 1, Step 2, and Phase 1
> all draw on the identical physical/climate/capability facts. **Feeds `01_Inherited.md` (Step 1) and
> `02_Spine.md` (Step 2) when Kunlun's own pass actually runs.**
> ⛔ **Excluded sections — see `Step_-1.md`.** Nothing below cites them.

| Category | Value | Citation |
|---|---|---|
| `Access type:` | `ON` — not yet tested for meaning in contract | `Specs/Kunlun.md` L23 |
| Climate — type | East Antarctic Plateau polar desert, the most extreme version | `Specs/Kunlun.md` L88 |
| Climate — annual mean temperature | **≈ −54 °C** *(corrected 2026-10-21 from the Dome A record; the earlier −58 °C did not match the station)* | `Specs/Kunlun.md` L89 |
| Climate — temperature range | Coldest months (Jul/Aug) avg −64 °C · warmest month (Dec/Jan) avg −35 °C | `Specs/Kunlun.md` L90 |
| Climate — record extremes | High **−31.2 °C** (Jan) · Low **−77.0 °C** (Jun) — NOAA NCEI GHCN-Daily, station AYM00089577 (Dome A, ~7 km), daily observations 1996–2026 | `Specs/Kunlun.md` L91 |
| Climate — winds | Among the calmest recorded — Dome A is a wind minimum due to the dome-summit position. Average **3–5 m/s**. *"The defining hazard here is cold and altitude, not wind"* | `Specs/Kunlun.md` L92 |
| Climate — annual precipitation | ≈ 15–20 mm water equivalent | `Specs/Kunlun.md` L93 |
| Climate — precipitation regime | **PLATEAU** — *"snow is a deposit, not weather."* Falls ≈ 20 mm/yr · Lands ≈ 18 mm/yr (**≈ 90% retention**) · Lost to sublimation/wind transport ≈ 2 mm/yr | `Specs/Kunlun.md` L97–100 |
| Climate — wind-vs-cold finding, quoted (own-value portion only) | *"COLD, overwhelmingly"* *(the clause comparing this city with the others is not carried)* *"… it sits above the katabatic regime rather than in it… Retention is ~90%: what falls, stays. There is no whiteout-under-clear-sky here — when visibility closes, something is actually falling. The hazard is temperature and altitude. Air movement is close to irrelevant."* | `Specs/Kunlun.md` L103 — an already-published finding in the source, quoted as such |
| Climate — polar night / midnight sun | Polar night: ≈ Apr 18 → Aug 26 (**≈ 131 days**) · Midnight sun: ≈ Oct 17 → Feb 26 (**≈ 133 days**) | `Specs/Kunlun.md` L106–107 |
| Climate — monthly table | Full 12-month table (Rec High/Avg High/Mean/Avg Low/Rec Low/Precip/Precip Prob/Daylight) present in source — transcribe verbatim when needed; not reproduced here to avoid redundant duplication of a 12-row table | `Specs/Kunlun.md` L114–126 |
| Climate — column provenance, quoted | *"Avg Temp: measured; column replaced 2026-10-21. BAS Met READER AWS record `Dome_A`, mean of every full year 1991–2025 … a record-period mean, not a 30-year WMO normal … Avg High / Avg Low rows: derived and, as labeled, inverted (the \"high\" is colder than the \"low\"); not corrected here."* | `Specs/Kunlun.md` L134 |
| Climate READER folder, direct check | **Rebuilt 2026-10-21 as a dataset (it had been an 8-line stub).** BAS Met READER AWS record `Dome_A`; every full year 1991–2025 (automatic weather station; shorter record, a record-period mean); 21–21 years per month. Monthly mean (°C): Jan −34.9 · Feb −44.0 · Mar −55.2 · Apr −61.4 · May −62.4 · Jun −63.4 · Jul −63.7 · Aug −64.2 · Sep −62.9 · Oct −55.4 · Nov −44.3 · Dec −35.7 · annual −53.9 | `READER/Kunlun.md` L1–18 |
| Real-world airstrip fact | *"Kunlun Skiway \| East Antarctica (Dome A) \| China \| Ice"* | `Reference/Real-World/Stations/Antarctic_Stations_With_Airstrips.md` L31 |
| Notable weather phenomena, quoted | *"Altitude at or beyond human limits… Exceptional atmospheric stability"* *(a third heading, a superlative, is not carried)* | `Specs/Kunlun.md` L139–142 |
| Human physiological limit, stated directly | *"Chronic mountain sickness at this altitude is not a manageable condition — it is the permanent baseline."* Effective physiological altitude approaching 5,000 m despite 4,093 m geometric elevation, "due to polar atmospheric compression" | `Specs/Kunlun.md` L80 |
| `16_Per_City_Three_Tier_Run.md` §22 — Kunlun's own determination row | D (difficulty): **2.70**. Baseline 28.6% (35,306 workers) · Mandated 26.8% (33,054 workers) · **FREE 44.6%** (55,089 workers). Distinctive tier 71.4% (88,143 workers) | `16_Per_City_Three_Tier_Run.md` §22, L2251–2256 |
| `16` §22 — mechanism note, quoted (own-value portion only) | *"With zero humans, the entire human-keyed term… is multiplied by zero. Difficulty only scales costs there is nobody to spend on. The free tier is 71.4% of distinctive because robots do not eat."* | `16_Per_City_Three_Tier_Run.md` §22 |
| `09_Per_City_Baseline_Run.md` §2 row | Mirny subnet · D 2.70 · Humans 0 · Residents 123,449 · Required workforce 35,306 · Workforce 123,449 · **28.6%** | `09_Per_City_Baseline_Run.md` L89 |
| `11_Caloric_Rebuild_and_Livestock_Tier.md` — Kunlun's own row | D 2.70 · OLD 28.6% · **NEW 28.6% — unchanged.** Mechanism, quoted (own-value portion): *"Robots do not eat."* | `11_Caloric_Rebuild_and_Livestock_Tier.md` |
| `Energy_Grid_Failure_Rationale.md` | Checked, **zero hits for Kunlun** by name | Re-verified this turn |
| Founding — what the source states, verbatim structure | Post-Falkland Treaty, on Kunlun Station infrastructure — established by CHINARE in 2009 (an infrastructure fact, `DR-24`) | `Specs/Kunlun.md` L156–158 (CHINARE as builder: L78) |
| Founding population | **Ariun Nuur's founding stock (Künnarantaiga and Mongolia), plus the Sinian Federation (China)**, ruled in the Founding Register (`DR-34`, `DR-35`); a robot-only city, so *founding nation* means the robots' learned national origin (`DR-11`). Spec L168 now opens with that statement (rewritten 2026-10-13); the earlier "Chinese (CHINARE) exiles founded the city" no longer stands as a station-operator claim (`DR-19`). *(Refreshed 2026-10-21 against the corrected spec and the Founding Register.)* "The name was kept" is a naming fact only | `Specs/Kunlun.md` L168–170; `Founding_Register.md` |
| Composition tiers (kept here too for spine-building convenience; full detail at `Phase_2.md`) | Primary: USA, China, Russia · Significant: Canada, Japan, UK, Intermarium/Intermaria, Italy, South Korea, Germany, France · Notable: New Zealand, Argentina, Sweden, Australia, Chile, Norway, Spain, South Africa, Netherlands | `Specs/Kunlun.md` L38–40; cross-verified `Official_Population_Census.md` — exact match |

**Not mechanical / not included here:** the Gate 9 asymmetry audit, the inheritance classification
(`Determined`/`Inflected`/`Originated`/`Aggregated`), the shape reading (BALANCED/COST-DOMINANT/etc.),
generator selection, the spine sentence itself, any wording rule about the remaining population, the entire
three-generator four-quadrant capability profile — none of this exists until Kunlun's own Steps 1–2 actually
run.
