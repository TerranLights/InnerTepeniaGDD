# Vostok — Datasheet · Step 1, Step 2 & Phase 1 (Constraint & Capability) — MERGED

> ⚠ **DRAFT — Tier C.** Merged per the Field Guide's consolidated 19-file shape. **Feeds `01_Inherited.md`
> (Step 1) and `02_Spine.md` (Step 2) when Vostok's own pass actually runs.**
> ⛔ **Excluded sections — see `Step_-1.md`.** Nothing below cites them.

| Category | Value | Citation |
|---|---|---|
| `Access type:` | `ON` | `Specs/Vostok.md` L6 |
| Climate — type | East Antarctic Plateau polar desert, the most extreme version; the coldest mean annual temperature of any Tepenian city | `Specs/Vostok.md` L59 |
| Climate — annual mean temperature | **≈ −54.8°C** | `Specs/Vostok.md` L60; cross-verified `Reference/Real-World/Climate Data/READER/Vostok.md` — exact match, full monthly table also matches |
| Climate — temperature range | Coldest months (Jul/Aug) avg −66°C · warmest month (Dec/Jan) avg −28°C | `Specs/Vostok.md` L61 |
| Climate — record extremes | High **−14.0°C** · Low **−89.2°C** — the lowest reliably measured natural surface temperature on Earth, Jul 21 1983 | `Specs/Vostok.md` L62 |
| Climate — data authority | AARI (Russia) / BAS READER, 1991–2020 WMO standard normal (30 years), full record 1958–2026, station: Vostok | `Specs/Vostok.md` L55; `Reference/Real-World/Climate Data/READER/Vostok.md` L1–7 |
| Climate — winds | Average **~5 m/s**, rising to **27 m/s** in the strongest events — light by Antarctic coastal standards. "#2 coldest of the 37," sits above the katabatic regime | `Specs/Vostok.md` L63, L74 |
| Climate — annual precipitation | ≈ 22 mm water equivalent | `Specs/Vostok.md` L64 |
| Climate — precipitation regime | **PLATEAU** — snow is a deposit, not weather. Falls ≈ 25 mm/yr · Lands ≈ 22 mm/yr (**≈ 90% retention**) · Lost to sublimation/wind transport ≈ 2 mm/yr | `Specs/Vostok.md` L68–71 |
| Climate — wind-vs-cold finding, quoted (own-value portion only) | *"COLD, overwhelmingly — and this city is one of the few where that is true. At −54.8°C it is the #2 coldest of the 37, but it sits above the katabatic regime rather than in it. Retention is ~90%: what falls, stays. There is no whiteout-under-clear-sky here — when visibility closes, something is actually falling. The hazard is temperature and altitude. Air movement is close to irrelevant."* | `Specs/Vostok.md` L74 |
| Climate — polar night / midnight sun | Polar night: ≈ Apr 24 → Aug 21 (**≈ 120 days**) · Midnight sun: ≈ Oct 22 → Feb 21 (**≈ 123 days**) | `Specs/Vostok.md` L77–78 |
| Climate — monthly table | Full 12-month table present in source, exactly cross-matched against the Climate READER folder's own independent table; transcribe verbatim when needed; not reproduced here to avoid redundant duplication of a 12-row table | `Specs/Vostok.md` L84–97; `Reference/Real-World/Climate Data/READER/Vostok.md` L12–14 |
| Climate — column provenance, quoted verbatim | *"Avg Temp: BAS READER WMO 1991–2020 normal. Temp Range: measured — mean daily minimum to mean daily maximum. Avg Precip: measured monthly normals. Precip Probability: measured — 26 measured snow-days/yr distributed across measured monthly precipitation. Avg Daylight: computed from this city's own latitude."* ⭐ **All three normally-derived columns here are MEASURED, not design-grade estimates** — a genuine difference from other extreme-plateau cities in this corpus whose equivalent columns are estimated | `Specs/Vostok.md` L102 |
| Notable weather phenomena, quoted (own-value portion only) | *"The record cold: −89.2°C is a number that has to be experienced to understand; at those temperatures, exhaled breath freezes before it disperses; exposed metal becomes brittle; lubricants fail... Katabatic calm: paradoxically, Vostok is much calmer in terms of wind than the coastal stations; the plateau interior lacks the slope-to-coast gradient that drives katabatic winds... Diamond dust: in the extreme cold and dry air, ice crystals are always present; the sky at Vostok has a permanent faint shimmer on clear days; solar halos and pillars are common"* | `Specs/Vostok.md` L107–109 |
| `16_Per_City_Three_Tier_Run.md` §23 — Vostok's own determination row | D (difficulty): **2.50**. Baseline 37.4% (121,353 workers) · Mandated 20.3% (66,007 workers) · **FREE 42.3%** (137,092 workers). Distinctive tier 62.6% (203,100 workers) | `16_Per_City_Three_Tier_Run.md` §23, L2344–2350 |
| `09_Per_City_Baseline_Run.md` §2 row | Mirny subnet · D 2.50 · Humans 129,617 · Residents 389,261 · Required workforce 134,615 · Workforce 324,453 · **41.5%** | `09_Per_City_Baseline_Run.md` L57 |
| `08_Volume_Based_Requirement_Reference.md` §5.2 row | Humans 129,617 · Residents 389,261 · Human-keyed 17,965 · Resident-keyed 47,762 · **Required 65,727** · Workforce 324,453 · **% of WF 20.3%** | `08_Volume_Based_Requirement_Reference.md` L505 |
| `09` §3.5 — THE FREEDOM GRADIENT | **Checked and confirmed excluded, per the Field Guide's own explicit instruction** — §3.5 is titled "THE FREEDOM MARGIN. A worldbuilding finding, not a calculation," and its table ranks all 38 cities against each other. This is an explicit cross-city comparison, never a per-city mechanical fact; not extracted | `09_Per_City_Baseline_Run.md` §3.5, L124 — opened and correctly excluded, not an unchecked hole |
| `National_Economy_and_Currency.md`, `Energy_Grid_Failure_Rationale.md` | Checked, **zero hits for Vostok** in either | Re-verified this turn |
| Founding — what the source states, verbatim structure | Post-Falkland Treaty; Vostok Station in continuous Soviet/Russian then rotating-national operation from 1957 (an infrastructure fact, `DR-24`). Preserved journals, logs, and orientation manuals survived and gave exiles a documentary starting point; no living scientific institution survived to teach them | `Specs/Vostok.md` L126 |
| Founding population | UNRULED in the Founding Register. ⛔ Spec L128 derives it ("Primarily Russian exiles") from the station's Soviet/Russian character — not an input (`DR-19`). "The name was kept" (L130) is a naming fact only | `Specs/Vostok.md` L128, L130; `Founding_Register.md` |
| Composition tiers (kept here too for spine-building convenience; full detail at `Phase_2.md`) | Primary: USA, Japan · Significant: South Korea, Canada, Indonesia, Australia · Notable: New Zealand, Chile | `Specs/Vostok.md` L18–22; cross-verified `Official_Population_Census.md` L510 |

**Not mechanical / not included here:** the Gate 9 asymmetry audit, the inheritance classification
(`Determined`/`Inflected`/`Originated`/`Aggregated`), the shape reading (BALANCED/COST-DOMINANT/etc.),
generator selection, the spine sentence itself, any wording rule about the remaining population, the entire
three-generator four-quadrant capability profile — none of this exists until Vostok's own Steps 1–2 actually
run.
