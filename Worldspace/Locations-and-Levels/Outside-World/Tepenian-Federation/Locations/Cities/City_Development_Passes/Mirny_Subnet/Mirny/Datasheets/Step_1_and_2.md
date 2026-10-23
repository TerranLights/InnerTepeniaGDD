# Mirny — Datasheet · Step 1, Step 2 & Phase 1 (Constraint & Capability) — MERGED

> ⚠ **DRAFT — Tier C.** Merged 2026-09-15: Step 1, Step 2, and Phase 1 all draw on the identical physical/
> climate/capability facts — kept as three files they were near-total duplicates. **Feeds `01_Inherited.md`
> (Step 1) and `02_Spine.md` (Step 2) when Mirny's own pass actually runs.** Mirny's Specs file is unusually
> detailed (230 lines) — this table extracts only what belongs to the physical/environmental capability
> profile. Economy, founding narrative, and notable-figures content living in the same Specs file belongs to
> later phases and is NOT pulled in here.

> ⛔⛔ **DoI CITATION GATE — binds every Division-of-Industry figure below.** `Corpus_Reference_Sheets/Division_of_Industry_Reliability_Quick_Reference.md`: workforce, difficulty, baseline load, distinctive tier and a city's own sector sizes are citable; an export headcount is not; nor is any "feeds N people" claim.

> 📂 **MUST-OPEN coverage — Field Guide Rule 1 (spine, Phase 1), checked 2026-10-23:** **6 of 6** addresses are named in this sheet (6 directly, 0 through a shared Tier U sheet it cites).

| Category | Value | Citation |
|---|---|---|
| Universe repo `Worldspace/Locations/` — directory enumerated | 4 `.md` files read; **1 name the city** | `…/Worldspace/Locations/` (enumerated 2026-10-23) |
| ↳ README.md | *[source line is a multi-city list; not copied, line number recorded only]* | `…/Worldspace/Locations/README.md` L20 |
| `Access type:` | `ON` — not yet tested for meaning in contract | `Specs/Mirny.md` L6 |
| Climate — annual mean temperature | **−11.2 °C** (1991–2020 WMO standard normal, 30 years; full record 1956–2026) | `Specs/Mirny.md` L68; cross-verified against `Climate Data/READER/Mirny.md` — exact match, both sources |
| Climate — monthly means (°C) | Jan −2.0 · Feb −5.2 · Mar −10.5 · Apr −13.9 · May −15.8 · Jun −15.4 · Jul −16.3 · Aug −16.4 · Sep −15.9 · Oct −13.4 · Nov −6.8 · Dec −2.7 | `Climate Data/READER/Mirny.md` L14; cross-verified against `Specs/Mirny.md`'s own monthly table — exact match |
| `Antarctic_Stations_With_Airstrips.md` — lines naming the city | Checked by name (`Mirny`): **zero hits** in a 100-line file | `Antarctic_Stations_With_Airstrips.md` |
| `COMNAP_Antarctic_Station_Catalogue.pdf` — pages naming the city (86 pages read) | pages 8, 65 *(page numbers only: the catalogue's index and entry pages are not separated here)* | `COMNAP_Antarctic_Station_Catalogue.pdf` |
| Climate — record extremes | High **+8.7 °C** (Dec) · Low **−36.5 °C** (Aug) — NOAA NCEI GHCN-Daily, station AYM00089592, daily observations 1973–2026 | `Specs/Mirny.md` L70 |
| Climate — winds | Katabatic, from south/southeast off the East Antarctic plateau; average **10–14 m/s**; sustained storms exceeding **40 m/s (144 km/h)** recorded; wind is stated as the dominant environmental feature | `Specs/Mirny.md` L71 |
| Climate — precipitation | Falls: **527.1 mm/yr** · Lands: **~200 mm/yr (~38% retention)** · Lost to sublimation/wind transport: **~327 mm/yr** — regime named "KATABATIC MARGIN: snow flux, not snowfall" | `Specs/Mirny.md` L72, L76–79 |
| Climate — polar night / midnight sun | Polar night: **NONE** (corrected 2026-09-04) · Midnight sun: **~29 days**, approx. Dec 8 → Jan 5 — asymmetric because refraction + solar semidiameter (~0.833°) separate the two boundaries by ~0.8°, and Mirny (66°33′S) sits between them | `Specs/Mirny.md` L85–99 |
| Climate — existing canon finding, quoted verbatim | *"WIND, decisively — the cold is NOT what defines this city."* *(the sentence ranking this city's temperature against the other cities is not carried)* *"Retention ~38% — residents dig out from what arrived from upwind, not from what fell on them."* | `Specs/Mirny.md` L82 — an already-published finding in the source, quoted as such |
| Geographic mechanism — the Antarctic Circle line | Mirny sits at 66°33′S, within arcseconds of the Antarctic Circle (66°33′26″S) — described in-source as "not a coincidence... the defining geographic fact of the city" | `Specs/Mirny.md` L53–55 |
| `16_Per_City_Three_Tier_Run.md` Half B — Mirny's own row | Subnet: Mirny · D (difficulty): 1.25 · Workforce: **1,018,480** · base%: 41.1% · MAND%: 11.8% · **FREE%: 47.1%** · src: `C` | `16_Per_City_Three_Tier_Run.md` L275 |
| `Energy_Grid_Failure_Rationale.md` | Checked, **zero hits for Mirny** by name | Re-verified this turn |
| Inherited infrastructure and records (`DR-24`, `DR-25`) | Settled post-Falkland Treaty, onto the substantial, functional station that remained (Soviet-era infrastructure, operating from 1956 — an infrastructure fact only). No institutional knowledge survived; preserved journals, logs and orientation manuals gave the exiles a documentary starting point | `Specs/Mirny.md` L150 (the operator succession, chars 35–361, is GPS-excluded by the Step −1 contract) |
| Founding population | Founded by Idelsk-Uralia, with exile groups from Russia, China (the Sinian Federation) and Australia (`DR-9`, `DR-46`, `DR-54`). Spec L152 was rewritten 2026-10-13 to match; the old *"Primarily Russian exiles…"* no longer stands. (Refreshed 2026-10-21 against the corrected spec and the Founding Register.) | `Founding_Register.md` (`DR-9`) |
| Reassignment note already in the source — dated, in-world content | *"Reassigned 2026-07-16… Mirny is also the near-exclusive top-tier industrial/quarrying hub feeding raw materials to the Tri-Cities — specifically to Sinheung, where they're fabricated into robot-synthesis chambers."* | `Specs/Mirny.md` L176 |
| Composition tiers (kept here too for spine-building convenience; full detail at `Phase_2.md`) | Primary: China · Significant: Japan, UK, South Korea, Russia, Indonesia, Australia (founding wave) · Notable: Thailand, Vietnam, Philippines, Malaysia, South Africa, New Zealand, Belarus | `Specs/Mirny.md` L18–22; cross-verified against `Official_Population_Census.md` L370–375, exact match |

**Not mechanical / not included here:** the Gate 9 asymmetry audit, the inheritance classification
(`Determined`/`Inflected`/`Originated`/`Aggregated`), the shape reading (BALANCED/COST-DOMINANT/etc.),
generator selection, the spine sentence itself, any wording rule about the remaining population, the entire
three-generator four-quadrant capability profile — none of this exists until Mirny's own Steps 1–2 actually
run.
