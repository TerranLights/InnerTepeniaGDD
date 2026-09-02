# Division of Industry — Research Log

**Convention: append only, never overwrite.** See this folder's `README.md`.

**⚠ Subsystem scope, not a city scope.** This log covers cross-city economic research for the necessary-
industries bulk pass (`../Division_of_Industry/`). Per `Canon_Gap_Resolution_Method/00_RUNBOOK.md` Step 1, a
subsystem is a valid scope.

---

## Session 1 — 2026-09-01, Bulk Mode instrument build (B3 calibration)

**Context:** Building the burden scoring model (`../Division_of_Industry/01_Burden_Scoring_Model.md`) for the
36-city × ~18-industry necessary-sector gap identified by `../Division_of_Industry_Sweep_2026-08-31.md` §4.4.

**Researching against:** the one number the two-tier §15 structure cannot be built without — **what fraction of
a remote cold settlement's labor goes to simply existing.** Without a real anchor the baseline percentages
would be confident and meaningless.

**Search strings, verbatim:**
1. `McMurdo Station ratio support staff to scientists percentage personnel breakdown`
2. `Longyearbyen Svalbard employment by sector statistics percentage`
3. `Norilsk employment by sector percentage workforce industry composition city`
4. `Iqaluit Nunavut employment by industry sector percentage labour force`
5. (WebFetch) `https://www.ssb.no/en/virksomheter-foretak-og-regnskap/virksomheter-og-foretak/artikler/svalbard-population-economy-and-living-conditions` — prompt: all employment-by-industry percentages, and differences from mainland Norway.
6. (WebFetch) `https://www.canada.ca/en/immigration-refugees-citizenship/campaigns/immigration-matters/local-economies/iqaluit.html` — **FAILED, HTTP 403 Forbidden.** Not retried this session. **Open thread:** Nunavut Bureau of Statistics or Statistics Canada would give per-sector Iqaluit figures directly; the territorial-level number was used instead.

### Findings used

| Anchor | Figure | Applied to |
|---|---|---|
| **McMurdo Station**, Jan 2011 | 995 total personnel; 550 Raytheon support + 106 NANA kitchen/janitorial ≈ **656 support (~66%) / ~34% mission** | **The envelope's calibration point.** Closest physical analog in existence |
| **Nunavut** | **60% public sector**, 35% private, 5% self-employed; public sector is the largest employer, concentrated in Iqaluit | Administration's base weight (14) |
| **Svalbard / Longyearbyen** | **~50% private** vs. 65% on mainland Norway → public sector far larger than mainland | Independent confirmation of the above, in a civilian town rather than a station |
| **Svalbard health care** | **<2%** of workforce vs. mainland Norway's 4% | ⚠ **INVERTED for Tepenia** — see below |
| **Svalbard mining** | 19.5% (2008) → **3.2% (2022)**, ~330 jobs lost | Precedent: a remote settlement's defining industry can collapse without the settlement dying — relevant to post-Tower cities |

### ⭐ The finding that changed the design

**Remote cold settlements run *low* healthcare, not high** — because they screen who may arrive and evacuate
anyone who becomes a long-term burden. The low number is a policy expressed as an economy.

**Tepenia has no evacuation destination. The valve is closed.** So Tepenian cities must internalize the entire
care burden their real-world analogs export. **The mechanism transferred; the magnitude reversed.** Written up
in `../Division_of_Industry/00_Necessary_Industries_Register.md` §A as a worked example of
`Real_World_Basis_Extrapolation_Method` — a striking real fact is *not* automatically a city fact.

### Self-correction recorded

**Earlier the same session, before this research, I had reasoned that healthcare should be a large sector
everywhere and treated the sweep's 29/36 as its headline finding.** The research says the sweep's
**administration** gap (33/36) is probably the corpus's larger real error, and that healthcare's magnitude
needed the inversion argument above rather than an assumption. **Recorded per the standing rule that killed
findings and self-corrections get logged, not just successes.**

---

## Session 2 — 2026-09-01, feasibility check: harvesting water from the air

**Context:** Developer question — beyond melting ground ice, could a Tepenian city "farm" water by capturing
frozen water vapor from the air, rather than relying on rain (impossible) or snowfall (precipitation-
dependent)?

**Search strings, verbatim:**
1. `Antarctica absolute humidity water vapor content air grams per cubic meter polar desert driest`
2. `rime ice accretion hoarfrost buildup Antarctic station structures maintenance removal problem`

### Findings

- **Antarctic plateau air is close to saturated over the ice surface**, but absolute humidity is very low
  because of the extreme cold. **⚠ The saturation is the blocker, not the dryness** — every atmospheric water
  generator works by chilling air below its dew/frost point, and this air is already there.
- **Hoarfrost** = water vapor depositing *directly* as ice onto a surface below the frost point (no liquid
  phase). **Rime** = supercooled liquid droplets freezing on impact — **requires fog or low cloud, therefore
  coastal only.** The two are distinct and were being conflated in the original question.
- **Ice accretion on structures is an established real-world maintenance liability**, increasing structural
  load and maintenance costs at polar facilities.

### Derived figures *(computed here from Clausius-Clapeyron; not sourced — flagged as own work)*

| Condition | Absolute humidity | Ratio |
|---|---|---|
| Temperate, 20 °C | ~8.6 g/m³ | — |
| Antarctic coastal, −15 °C | **~1.4 g/m³** | ~6× drier |
| Plateau, −55 °C (Vostok) | **~0.02 g/m³** | **~430× drier** |

At 100 L/person/day, coastal air requires processing **~70,000 m³ of air per person per day at 100%
extraction**; plateau air roughly 10⁵× worse. **Ruled out as a municipal supply at every Tepenian city.**

### ⭐ Verdict and disposition

**Not Tier A. Reclassified as a LAW G weird-industry candidate**, and a strong one — the *passive* form is
free: radiative cooling drives surfaces below the frost point without refrigeration, and **these cities are
already paying crews to scrape accreted ice off their own structures.** Byproduct→product and liability→asset
simultaneously (`05_Bulk_Mode` LAW G moves 1 and 2).

**Geographic irony worth preserving:** it works best where it is least needed (coastal, ~70× the moisture, plus
abundant sea ice) and fails hardest where water costs most (the plateau). **An interior city doing it anyway is
doing it for a non-economic reason** — which is the interesting version.

**Third-order thread, unchased:** ice-melt water in an energy-rationed, administration-heavy economy is
allocated and registered; **frost landing on a private roof is not.** Suggests unmetered "sky water" as an
informal/parallel economy and an unsettled ownership question. **Belongs in
`Worldspace/Parallel_Economies_Survey.md`; not yet added there.**

**Also unchased:** `diamond dust` is already listed as a precipitation form in `Specs/_TEMPLATE.md` — the canon
hook exists and has not been used by any city.

---

## Session 3 — 2026-09-01, feasibility check: shipping beverages to Vostok

**Context:** Developer question — could drinks with high water content (alcoholic or not: juice, kombucha,
mate) be made outside Vostok and shipped in?

**Search strings, verbatim:**
1. `ethanol water mixture freezing point by ABV percentage table 40% 60% 70% proof`
2. (WebFetch) `https://www.engineeringtoolbox.com/ethanol-water-d_989.html` — **FAILED, HTTP 403.**
3. (WebFetch) `https://www.katmarsoftware.com/alcodens-ethanol-freezing-point.htm` — partial: confirmed the
   40% figure and the curve's endpoints, **but the page carries no intermediate table.** Not resolved.

### Findings

- **40% ABV freezes at −23.3 °C** *(sourced, confirmed).* Curve runs from 0 °C (pure water) to **−115 °C at
  ~95% ABV** *(sourced).*
- **⚠ The 60–70% ABV figures are INTERPOLATED BY ME between those two anchors, not sourced.** Both fetches for
  the intermediate table failed. **Flagged so a later pass does not mistake them for researched values** — the
  route-survival threshold of "roughly 60–70% ABV at −55 °C ambient" needs a real phase-diagram source before
  it becomes canon.

### Reasoning (own work, not sourced)

- **Melting local ice ≈ 0.13 kWh/L** (334 kJ/kg latent heat + ~113 kJ/kg warming ice from −55 °C). Hauling
  1 kg 1,300 km onto a 3,488 m plateau costs far more. **Shipping water as water is never rational** — Vostok
  sits on the largest freshwater reserve on Earth. **Water is not the scarce thing; melting energy is.**
- Therefore imported drink is never hydration. **The water is a tax paid to move the payload** (flavor,
  alcohol, live culture, provenance). Rational import form is concentrated → **dilution becomes the local act,
  and reconstitution the local craft.**

### ⭐ The result worth keeping

> **Alcohol content on the Hwy 37 plateau route is a shipping specification, not a recreational preference.**
> Only ~60%+ ABV survives an unheated haul at −55 °C. **Everything weaker needs a heated container** — energy
> cost, on the most expensive route, in an energy-backed economy.
>
> **So weakness is the luxury. Orange juice costs more than whiskey at Vostok.** Beer is an extravagance;
> kombucha is near-unobtainable as a liquid, though a live SCOBY ships fine and brews locally, making the
> culture itself a valuable and closely-held import.

**Generalizes to:** *anything with low water activity reaches the plateau — dry, sugary, salty, or alcoholic.*
Honey, syrups, freeze-dried goods, and **dry leaf — so mate, tea and coffee ship perfectly.** ⭐ **Gives
Janbogo's established teahouse economy a natural export line onto the plateau.**

**Two secondary threads, unchased:**
1. **Freeze distillation is free at Vostok** — the environment jack-freezes at no energy cost, where everywhere
   else it needs refrigeration. **Concentrates congeners and fusel oils along with ethanol → a cheap, strong
   local spirit with a reputation for punishing hangovers.** Physically grounded; not yet assigned.
2. **Alcohol is a diuretic** — the drinks that survive the trip actively dehydrate. **Nothing imported is ever
   hydration.** Interacts with the Session 2 sky-water thread: metered meltwater for living, unmetered frost at
   the margins, imported liquid purely as pleasure and status. Connects to `glitch-coolant`'s existing
   potency axis.

---

## Session 4 — 2026-09-01, the volume-based method: source register for all 18 industries

**Context:** developer specified a new method — research **volume per capita** per industry, then **labor per
volume**, then +2% as the ceiling for a non-producing city. Full method:
`../Division_of_Industry/08_Volume_Based_Requirement_Reference.md`.

**Search strings, verbatim:**
1. `water treatment plant staffing employees per million gallons per day capacity benchmark`
2. `municipal water consumption liters per person per day average developed country residential`
3. (WebFetch) `https://neiwpcc.org/.../NEIWPCC-Northeast-Staffing-Guide.pdf` — **image-based PDF, text
   extraction FAILED.** File retained in `Reference/Real-World/Industry_Staffing_and_Productivity/`.
4. `AWWA benchmarking "staffing levels per 1000 population served" water utility employees median` — **AWWA
   figures paywalled.**
5. `BLS number of water and wastewater treatment plant operators employed United States total employment`
6. (WebFetch) `https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=9100W7EU.TXT` — ✅ **EPA staffing curves obtained.**
7. `NFPA 1710 firefighters per 1000 population staffing standard fire department benchmark`
8. `WHO Global Health Workforce Statistics physicians nurses per 10000 population database`
9. `UNESCO Institute for Statistics pupil-teacher ratio primary secondary database`
10. `World Bank "What a Waste" municipal solid waste generation kg per capita per day global`
11. `IFMA facility management staffing benchmark maintenance employees per 100,000 square feet`
12. `OECD Government at a Glance public sector employment percentage of total employment by country`
13. `residential floor area per capita square meters by country building stock statistics`
14. `FAO food balance sheets kcal per capita per day kg food supply per person per year`
15. `electricity consumption kWh per capita by country IEA plus power plant staffing employees per MW`
16. `aircraft maintenance man-hours per flight hour MRO ratio fleet technicians per aircraft benchmark`
17. `apparel textile consumption kg per capita per year clothing purchased average`
18. `freight tonne-km per capita domestic transport employment percentage workforce logistics sector`
19. `total health and social care employment percentage of workforce OECD countries doctors nurses per 1000`
20. `controlled environment agriculture vertical farm labor workers per hectare greenhouse employment per m2`
21. `Iceland Norway district heating electricity consumption per capita kWh residential heating cold climate`

**⭐ Structural finding forced by the first industry:** labor has **three components** — plant *(scales with
volume, sub-linearly: `staff ∝ MGD^0.65`)*, network *(scales with extent, linear)*, service *(scales with
population)*. **A single "workers per unit volume" figure understates any networked industry ~8×.**

**⚠ Failures and gaps recorded:** AWWA and RSMeans paywalled · NEIWPCC PDF unreadable · **B3 robot
maintenance and B4 coolant/siligel have NO real-world analogue** *(best proxy: aviation MRO at 0.36
man-hours per flight hour)*.

---

## Session 5 — 2026-09-01, the difficulty layer

**Context:** demand alone produced a near-flat line — five cities within 0.1 points. **Difficulty was the
layer with no external calibration; every prior multiplier had been reasoned, never measured.**

**Search strings, verbatim:**
1. `cold weather construction labor productivity loss percentage by temperature estimating factor NECA MCAA`
2. `Nunavut Arctic construction cost multiplier compared to southern Canada per square meter remote premium`
3. `MCAA productivity factor table severe weather percentage minor average severe 16 categories values`
4. `CRREL cold regions construction cost factor Antarctic McMurdo logistics cost per pound delivered`
5. `construction productivity loss percentage below freezing temperature study bricklaying concrete winter`
6. `Antarctic research station construction cost per square meter Halley VI Princess Elisabeth budget`
7. (WebFetch ×3) engineeringtoolbox / adroitprojectconsultants / wsscwater — **403 or table absent.**
8. ⭐ (WebFetch → **local `pdftotext`**) `ibbsconsulting.com/.../Use-of-MCAA-Method-in-Loss-of-Productivity-
   Claims.pdf` — **✅ THE FULL MCAA FACTOR TABLE, free.** The $495 publication was not needed.

**Key figures obtained:** MCAA **weather 10/20/30 · logistics 10/25/50 · site access 5/12/30** *(percentage
loss, applied additively)* · **Iqaluit construction 3× southern Canada** · **Halley VI $29,565/m² ≈ 10–20×
temperate** · Nunavut sealift June–October, **some communities one delivery per year.**

> **⚠ Self-correction recorded twice in this session.** (a) I called the old model's 7.28 driver product a
> "scandal" against a 0.7–2.0 range **that I had invented**; the real-world ladder suggested it might be
> defensible. (b) **Then the developer pointed out Halley VI's cost is mostly intercontinental shipping**,
> which Tepenia does not pay — its supply is domestic, road-connected, 350–1,300 km. **That pulled the band
> back to ~0.9–3.5× and made my reversal an over-correction.** Both are logged rather than silently amended.

---

## Session 6 — 2026-09-01, SOC cross-check *(no web research — local PDF)*

**Source:** `to-be-integrated/BLS_-_Standard_Occupational_Classification_Manual_2018.pdf`, supplied by the
developer. Extracted the 23 major occupational groups via `pdftotext` and cross-checked both directions
against the necessary-industries register.

**⭐ Forward check → 4 industries added + 1 expanded** *(legal, community/social, finance, computing;
emergency expanded to include policing)*. **Register 18 → 22.**

**⭐⭐ Reverse check → the SOC cannot classify 4 Tepenian roles**, and all four are robot-personhood roles:
robot maintenance *(falls between machine repair and healthcare — categories that never overlap on Earth)*,
robot semantic care, Cradle chamber operation *(production, but of people)*, robot decommissioning/ossuary.
**Recorded in the register as a diagnostic of where the setting's actual novelty sits.**

**Also searched, unresolved:** `NAICS 92 public administration employment United States total BLS` and
`COFOG "general public services" government employment share by function` — **the clean category exists**
(BLS OEWS Sector 99, government excluding schools/hospitals/USPS) **but BLS blocks automated fetching.**
**The administration rate remains estimated at 65/1,000; the OEWS spreadsheet is a manual download away.**

---

## Open threads, carried forward

1. Per-sector Iqaluit figures (blocked by the 403; Nunavut Bureau of Statistics is the route).
2. Norilsk city-wide sector composition — **only Nornickel corporate figures were reachable** (67% of the
   regional workforce is Nornickel-employed); the city-level split would need Russian statistical sources.
   **The closest real analog to a large permafrost industrial city remains uncalibrated.**
3. Fog-harvesting yield data (Atacama `camanchaca` nets) for a defensible L/m²/day figure at coastal sites.
4. Real Antarctic station water-production energy budgets, to size A2 against A1 properly.
5. **⚠ Ethanol-water phase diagram, intermediate values (50–80% ABV).** Two sources 403'd or lacked the table.
   **The "~60–70% ABV survives −55 °C" threshold is currently interpolated, not sourced**, and is load-bearing
   for the Vostok beverage-import conclusion in Session 3. **Resolve before that becomes canon.**
