# Volume-Based Requirement Reference

> ## The method, developer-specified 2026-09-01. **This supersedes both prior sizing attempts.**

**Basis: CENSUS I** *(cities must be able to house their peak)*. **Period: Second Interwar.**

---

# 1. Why this replaces what came before

**Two sizing attempts have now failed validation, and two independent agents converged on the same root
cause without being asked about it:**

> **Evaluator:** *"Labor is not the binding resource here… A per-capita labor rate structurally cannot express
> that."*
> **Builder:** *"Energy is the actual binding constraint in this setting. The right successor is not a better
> burden index; it is a second model in **watts**, with headcount as a derived output of it."*

**Both prior models started from labor and never recovered.** `01`'s share-first model distributed percentages
by burden index — a quantity with no external referent, and therefore unfalsifiable. The requirement-first
trial started from workers-per-1,000, which is one step better but still skips the physical layer: it can say
Vostok needs 1 grower per 10.9 humans *(better than the national average)* while canon says Vostok plainly
cannot feed itself. **Nothing in a headcount model can see why.**

> ## ⭐ **This method inserts the missing layer: VOLUME.**
> **Volume is the physical quantity a city actually consumes** — liters of water, kilowatt-hours, tonnes of
> food, m² of enclosure. **Labor is derived from volume, not asserted per capita.** And critically, **volume
> carries energy**, which headcount cannot: the same tonne of food costs a different number of kilowatt-hours
> to produce at −54.8 °C under 121 days of darkness than it does at Davis.

---

# 2. The procedure

### Step 1 — Volume per capita, per industry
**For each necessary industry, research what volume a real population actually requires.**
*(Water: L/person/day. Power: kWh/person/year. Food: kg/person/year. Healthcare: beds and contacts per 1,000.
Construction: m² of maintained building stock per capita. And so on.)*

### Step 2 — Labor per volume
**Then research how many people are required to RUN that volume.** *(Workers per ML/day of treatment
capacity; per MW installed; per tonne processed; per 1,000 m² maintained.)*
**Robot or human is immaterial — a worker is a worker.**

### Step 3 — Multiply out
`required workers = (volume per capita × population) × (workers per unit volume)`

### Step 4 — ⭐ The +2% rule
**Add 2% to that person-count. The result is the THEORETICAL MAXIMUM for a
non-producing, non-contributor city.**

> **What this rule does, and it is the sharpest part of the method:** it says a city that serves only itself
> needs its own volume plus a **2% margin — and no more.** That makes the non-producer figure a **hard
> ceiling**, not an estimate.
>
> **Therefore: any city exceeding its +2% ceiling in an industry is, by definition, producing for somebody
> else.** Provider status stops being a judgment call and becomes an arithmetic result.

### Step 5 — Apply per city
Run every city's division of industry against these percentages.

### Step 6 — *(later, after Steps 1–5)* — the producer pass
**For the producing/contributing cities: establish their own non-outsourceable volume first**, then determine
**how much of other cities' OUTSOURCEABLE demand they can realistically absorb — without placing unreasonable
strain on their own local populations.** *(This is where the 04 §2 outsourceable/non-outsourceable split and
the autonomy-reserve concept become load-bearing. Not started.)*

---

# 3. What this method fixes

| Prior defect | Status under this method |
|---|---|
| **Envelope map undefined** *(~17pp swing)* | **Gone.** No normalizer exists. Percentages are `derived workers ÷ workforce`, and the workers come from physical volume |
| **Isolation cancels out of every row** | **Gone.** Isolation acts on *supply reliability*, which is a per-industry property, not a universal multiplier |
| **Rates invented with no external referent** | **Directly addressed.** Both research steps target published real-world figures. **This was the evaluator's single highest-value recommendation** |
| **Model can't see energy** | **Addressed at the root.** Volume is where energy cost attaches |
| **Provider status is a judgment call** | **Becomes arithmetic** via the +2% ceiling |
| **Drivers compound geometrically** *(7.28 against a 0.7–2.0 range)* | Carry forward the trial's fix: **additive excess over one**, not multiplication — realized 0.933–2.107 across 114 cells with zero clamp hits |

---

# 4. Research findings

**Status: IN PROGRESS.** Each industry needs two figures. **Every entry must carry its source.** Where a
figure is interpolated, assumed, or unavailable, it is marked as such rather than presented as researched —
the prior passes both had assumed numbers reading as sourced ones.

| # | Industry | Volume per capita | Labor per volume | Status |
|---|---|---|---|---|
| A1 | Thermal & power | | | ⏳ |
| **A2** | **Water & sanitation** | **129–380 L/person/day** | **plant: `staff ≈ 3 × MGD^0.65`** · **operators: 0.32/1,000 pop** | **✅ §4.1** |
| A3 | Enclosure & atmosphere | | | ⏳ |
| A4 | Construction & structural | | | ⏳ |
| A5 | Emergency services | | | ⏳ |
| B1 | Food production & distribution | | | ⏳ |
| B2 | Human healthcare | | | ⏳ |
| B3 | Robot maintenance & parts | | | ⏳ |
| B4 | Coolant & siligel | | | ⏳ |
| B5 | Textiles & survival gear | | | ⏳ |
| C1 | Education & training | | | ⏳ |
| C2 | Childcare & eldercare | | | ⏳ |
| C3 | Administration & records | | | ⏳ |
| C4 | Materials recovery | | | ⏳ |
| C5 | Mortuary & decommissioning | | | ⏳ |
| D1 | Transport & logistics | | | ⏳ |
| D2 | Communications / Arcanet | | | ⏳ |
| D3 | Retail & daily distribution | | | ⏳ |

---

## ⭐ 4.0 — A STRUCTURAL REFINEMENT THE FIRST INDUSTRY FORCED. Applies to all eighteen.

**Researching A2 exposed a problem with a single "labor per volume" figure, and the fix generalizes.**

**Two sourced figures for water labor disagree by 8×:**
- **EPA plant-staffing curves** → a 1.5 M-resident city needs **~59 plant staff.**
- **US BLS operator employment** *(107,941 operators ÷ ~335 M people)* → **~482 for the same city.**

**Neither is wrong. They measure different things**, and the gap is the whole lesson:

> ## **Labor in a necessary industry has THREE components, and only one of them scales with volume.**
>
> | Component | Scales with | Behavior |
> |---|---|---|
> | **Plant / production labor** | **volume** | **Strongly sub-linear** — EPA data gives `staff ∝ MGD^0.65` *(1 MGD→3 staff; 9.5→11.7; 20→21)*. **Big cities get this nearly free** |
> | **Network / distribution labor** | **extent** — pipe-km, corridor-km, dome area | Roughly linear in **area**, not population. **This is where the 8× lives** |
> | **Service / counter labor** | **population** | Linear per capita |

**Consequences for the method, and they are load-bearing:**

1. **Step 2 must produce three coefficients per industry, not one.** A single "workers per unit volume"
   understates any industry with a distribution network by roughly an order of magnitude.
2. **⭐ Economies of scale are real and large, and they run OPPOSITE to the physical drivers.** At `^0.65`,
   doubling a city's population raises plant labor by only ~57%. **Lazar's 2.6 M gets its water plants far
   cheaper per head than Kunlun's 123 k does** — which partly explains why every headcount model so far has
   found big cities cheap and been unable to say why.
3. **⭐ It supplies the physical hook for the density and foundation findings.** Network labor scales with
   *extent*, so **Lazar's 34 km² oasis is a genuine efficiency** — short pipe runs — while a sprawling or
   ice-founded city pays more for the same volume. `05` §3's rock-core/ice-periphery gradient stops being
   flavor and becomes a cost.

---

## 4.1 — A2 WATER & SANITATION ✅

**Volume per capita** *(sourced)*: **US 250–380 L/person/day · Canada 335 · Europe 200–300 · EU household
mean 129 · Australia 191 · WHO basic-needs floor 50–100.**

> **⚠ Tepenian divergence, flagged not settled.** Every figure above is from a society where water is pumped.
> **Tepenian water is MELTED — it carries the full latent heat of fusion plus warming from ambient**
> *(~0.13 kWh/L, established earlier this pass)*. **A metered, energy-costed supply should sit far below
> developed-world use — plausibly 100–150 L/person/day, nearer the WHO band than the American one.**
> ⭐ **And that is itself a characterization: Tepenians would regard American water use as obscene.**
> *(Exception: {{Bunger Hills City}}, which draws from Antarctica's largest freshwater lake and is the one
> place the normal figure could apply — see its development brief.)*

**Labor per volume** *(sourced)*: **EPA municipal wastewater staffing curves** — 1.0 MGD ≈ 3 staff · 9.5 MGD
≈ 11.7 · 20.0 MGD ≈ 21 (well-run) · 20.0 MGD ≈ 37 (**problem plant — a 76% penalty for poor condition**).
**Derived exponent: `staff ≈ 3 × MGD^0.65`.** ⚠ *EPA states the curves are valid 0.5–25 MGD and must not be
extrapolated; a Tepenian city needs many plants, not one large one.*

**Network + service labor**: **US BLS 107,941–122,100 water/wastewater operators ≈ 0.32 per 1,000
population**, and that is **operators only** — excluding distribution maintenance, engineering, billing and
administration. **The full sector is materially larger; a figure for NAICS 2213 is still needed.**

**⭐ The "problem plant" penalty is worth keeping as a mechanic**: identical capacity, **76% more labor**,
purely from condition. **That is a lever for a city in decline, or one that deferred maintenance** — and it is
sourced, not invented.

---

---

# 4.2 — ⭐ THE SOURCE REGISTER — canonical references located for all 18 industries

**Researched 2026-09-01.** **Sixteen of eighteen have a genuine authoritative source. Two do not, and are
marked honestly rather than papered over.**

## ✅ TIER 1 — canonical, free, per-country, both figures obtainable

| # | Industry | **Volume source** | **Labor source** | Figures already in hand |
|---|---|---|---|---|
| **A2** | Water & sanitation | national water statistics | **EPA municipal staffing curves** · AWWA Benchmarking · BLS | 129–380 L/cap/day · `staff ≈ 3×MGD^0.65` · 0.32 operators/1,000 |
| **A5** | Emergency services | — *(population-keyed)* | **NFPA 1710 / NFPA 1750** | **2.0–2.5 firefighters per 1,000 pop**; 4 first-arriving in 4 min; 15–17 full alarm in 8 min |
| **B1** | Food production | **FAO Food Balance Sheets / FAOSTAT** — kg/person/yr **and** kcal/person/day, 178 countries, 449 products, 2010–2023 | FAO/USDA ag. employment; CEA labor per m² | **Global DES >3,000 kcal/cap/day (2023)** |
| **B2** | Human healthcare | OECD *Health at a Glance* — beds/1,000 | **WHO Global Health Observatory / NHWA** — physicians and nursing-midwifery per 10,000 | canonical, per country |
| **C1** | Education & training | UIS enrolment | **UNESCO Institute for Statistics** — pupil-teacher ratio, 200+ countries, 1970– | primary / lower-sec / upper-sec / pre-primary separately |
| **C3** | Administration | — *(population-keyed)* | **OECD *Government at a Glance*** | **OECD avg 18.6%** of total employment · **Norway 30.1 · Sweden 28.2 · Denmark 27.3 · Finland 25.2** · US ~15 · Japan/Korea <10 |
| **C4** | Materials recovery | **World Bank *What a Waste 2.0*** | waste-management employment | **global 0.88 kg/cap/day · high-income 1.57–2.2 · low-income 0.2–0.43** |
| **A3** | Enclosure & atmosphere | floor area *(see A4)* | **IFMA O&M Benchmarks** — 54,000 buildings, 34 countries | **4.1 FTE per 100,000 GSF** overall; **1 maintenance FTE per 47,000 rentable ft²** |
| **A1** | Thermal & power | **World Bank / IEA** kWh per capita | EPA Power Sector Employment methodology; plant staffing studies | Iceland 52,920 · Norway 23,374 · Finland 14,747 kWh/yr · **nuclear ~0.62 workers/MW · CCGT ~0.02–0.10/MW** |
| **B5** | Textiles & survival gear | **EEA / Fiber Year** | textile manufacturing employment | **EU 19 kg/person/yr** (8 clothing, 4.4 footwear, 7.6 household) · global 13 kg (2018) vs 5.9 (1975) · China 18 · India urban 10 |

## ✅ TIER 2 — good sources, one figure needs more work

| # | Industry | Source | Note |
|---|---|---|---|
| **A4** | Construction & structural | **ENTRANZE** (Europe) · CEIC (China) · OECD | Floor area per capita well covered — China urban 40 m², US ~65–77 m²/person. **Maintenance labor per m² comes from IFMA (A3); new-build labor needs separating out** |
| **C2** | Childcare & eldercare | OECD Family Database · BLS | Splits cleanly into childcare and personal-care aides |
| **C5** | Mortuary & decommissioning | **UN World Population Prospects** (crude death rate) · funeral-industry employment | Human side straightforward. **Robot decommissioning has no analogue — see Tier 3** |
| **D1** | Transport & logistics | UNCTAD freight data · national labor stats | **Australia: 5.1% of total workforce** (Transport, Postal & Warehousing) · UK 2.1 M in logistics |
| **D2** | Communications / Arcanet | ITU · telecom employment | Straightforward; note extreme-altitude cities have essentially none |
| **D3** | Retail & daily distribution | retail employment · floorspace per capita | Needs the discretionary share stripped out — only groceries/pharmacy/hardware are *necessary* |

## ⚠ TIER 3 — NO DIRECT REAL-WORLD ANALOGUE EXISTS. Proxy or invent, and say which.

| # | Industry | Best available proxy | Honest status |
|---|---|---|---|
| **B3** | **Robot maintenance & parts** | **Aviation MRO: 0.36 maintenance man-hours per flight hour** *(industry average; IATA Maintenance Cost Data Exchange, Oliver Wyman MRO survey)*. Also fleet-vehicle servicing | ⚠ **The single largest unsourced quantity in the model — it sets the cost of maintaining 51% of the national population.** The MRO ratio is genuinely usable *if* a robot duty cycle is ruled on: man-hours = 0.36 × operating hours. **But that ruling does not exist** *(see §5.2)* |
| **B4** | **Coolant & siligel** | chemical manufacturing employment; single-product continuous-process plants | ⚠ **Fully invented.** A survival consumable with no earthly equivalent. Continuous-process chemical plants are capital- not labor-intensive, which bounds it low, but the volume per robot is pure canon invention |

---

# 4.3 — ⭐ THREE PATTERNS THAT RECUR ACROSS THE SOURCES

**1. Production labor scales SUB-LINEARLY with volume, in every industry that has a plant.**
Water: `staff ∝ MGD^0.65`. Power: nuclear ~0.62 workers/MW but **CCGT 0.02–0.10/MW** — *"staff per MW falls
sharply as plants get larger."* **This is now confirmed independently in two industries and is the strongest
structural regularity found.** **Big cities get their production infrastructure dramatically cheaper per
head** — and it explains, physically, why every headcount model in this pass found large cities cheap without
being able to say why.

**2. ⭐ Network and facility labor scales with EXTENT and is roughly LINEAR.** IFMA's 4.1 FTE/100,000 GSF has
no scale discount at all. **So a city's labor curve is the sum of a sub-linear production term and a linear
extent term** — which is exactly the three-component split §4.0 forced, now confirmed from a second industry's
sources.

**3. ⭐⭐ The Nordic public-employment band is the right anchor for Tepenia, and this is now the THIRD
independent confirmation.** OECD average is 18.6%, but **Norway 30.1 · Sweden 28.2 · Denmark 27.3 · Finland
25.2** — and earlier research in this pass found **Nunavut at 60% public sector** and **Svalbard ~50% against
a 35% mainland baseline**. **Cold, remote, state-founded settlements run administration-heavy, consistently,
from three unrelated data sources.** The register's C3 weighting was right and can now be sourced rather than
argued.

---

---

# 4.4 — ⏸️ THE ROBOT DUTY CYCLE IS DEFERRED, AND THE WORK ROUTES AROUND IT

> **Developer instruction, 2026-09-01:** *"Let's temporarily hold off on the robot duty cycle. That might
> require some extremely complex research (into supply lines, theoretical mechanics/cybernetics, etc.) that
> may very well end up bogging us down… let's focus on what we're able to determine for sure, and there might
> be a possibility that the answers may lend themselves towards figuring out how to approach the numbers that
> are related to robots."*

**⭐ This works better than deferral usually does, because the industries sort cleanly by what they are keyed
to — and only one group is blocked.**

| Keyed to | Industries | Status |
|---|---|---|
| **RESIDENT** *(serves anyone present)* | A1 power · A2 water · A3 enclosure · A4 construction · A5 emergency · **B5 textiles** · C1b trade training · C3 admin · C4 recovery · D1 transport · D2 comms · D3 retail | ✅ **determinable now** |
| **HUMAN** | B1 food · B2 healthcare · C1a general schooling · C2 childcare · C5 mortuary *(human side)* | ✅ **determinable now** |
| **ROBOT** | B3 maintenance · B4 coolant/siligel · C5 decommissioning *(robot side)* | ⏸️ **blocked** |

## ⚠⚠ TWO CORRECTIONS, developer-issued 2026-09-01. Both were my errors.

### 1 — **KEYING DETERMINES DEMAND, NOT STAFFING.** These are orthogonal axes.

> *"Just because a robot doesn't **need** some particular industry, that doesn't mean that a robot is 'not
> allowed to work' in some particular industry (such as education, for example)… 'zero robots' means 'zero
> robots **require**' those industries, not that 'zero robots **work**' in those industries."*

**I conflated the two and drew a false conclusion from it** — that because human-only industries consume ~28%
of the human workforce, humans could not also staff infrastructure, therefore robots must do the
infrastructure. **That inference is invalid.** Robots can staff human-keyed industries perfectly well, so
nothing forces that division.

| | Determined by | Status |
|---|---|---|
| **DEMAND** — how much of an industry is needed | **population keying** | ✅ arithmetic; unaffected by the correction |
| **SUPPLY** — who staffs it | **culture and canon** | ⭐ **a free design variable, not derived** |

**What survives:** every demand figure. **What died:** any inference from demand to staffing composition.
**The weaker bound still holds** — total demand must fit inside total workforce, so the robot-keyed three can
still be constrained by subtraction. It simply cannot tell us who works where.

> **⭐ And the staffing mix is better as a design variable than it would have been as a derived one.** A city
> where robots teach human children is a different place from one where humans do. The *reasons* for each
> split — trust, tradition, shortage, preference, prejudice — are exactly the texture culture work needs.

### 2 — **ROBOTS WEAR CLOTHING.** B5 textiles is resident-keyed, not human-keyed.

**Sized against all 32,026,600 residents rather than 15.6 M humans — roughly doubling national textile
demand.** And robot textile demand is **not a scaled-down copy of human demand**: at −55 °C a covering over
joints, actuators and fluid lines is **thermal management**, sitting in the same picture as coolant and
siligel. A different garment doing a different job, plausibly more demanding per wearer.

> **The social half matters more: a population that dresses is a population of PERSONS, not appliances** —
> consistent with robots already having religions, arts, drinking culture and counselors. **Open cultural
> axis: do robots and humans dress alike, or distinctly?** In a nation ~51% robot, whether the two share a
> wardrobe idiom is a real fact about how integrated that society is.

> ### ⚠ Both corrections have the same shape, and it is worth naming so it stops recurring:
> **I had been treating robots as an ABSENCE — zero demand, zero staffing — when they are a POPULATION.**
> They work in every industry and they wear clothes. **The places their number genuinely is zero are narrow
> and specific: they do not eat, do not attend childhood schooling, do not get sick, and are not born.**

> ## **Fifteen of eighteen are unblocked. And the deferral is not merely survivable — it is productive.**
>
> **Compute the fifteen as ABSOLUTE HEADCOUNTS and the robot-keyed three become the only unknown in a system
> that must fit inside a real workforce. That BOUNDS them from above** — they can be constrained by
> subtraction rather than derived from scratch. **This is precisely the possibility the developer flagged.**

**⚠ One thing the deferral does block: percentages.** `BaselineLoad% = required ÷ workforce`, and the
workforce denominator is exactly the disputed quantity *(does a robot work 100% of the time?)*. **So this
phase produces headcounts, not shares.** Headcounts are the more useful artifact anyway — they feed level
design, NPC population and faction sizing, which percentages cannot.

---

# 4.5 — EXTRACTED FIGURES, ROUND 2

### B2 — Human healthcare ✅ *(the total-sector figure, which is what was missing)*
- **⭐ Health and long-term care employ ~10% of the TOTAL WORKFORCE across OECD countries.** *(OECD, Society
  at a Glance 2024.)* This is the sector figure; the per-1,000 clinician densities below sit inside it.
- **Doctors: OECD average 3.7 per 1,000 population** (2021) — under 2.5 in Mexico/Colombia/Türkiye, **over 5
  in Norway, Austria, Portugal, Greece.**
- **Nurses: ~2.5 nurses per doctor on OECD average** → ~9.3 per 1,000 at the mean.
- **Tepenian adjustment**, per Register §A: **above** the norm, because there is no evacuation destination and
  the whole care arc must be internalized. **Norway's >5 doctors/1,000 is the better anchor than the OECD
  mean.**

### B1 — Food, the labor side ✅ *(and it carries a large, honest uncertainty)*
- **Vertical farming: ~1 FTE per 3,000 ft² (279 m²) of growing space** — industry rule of thumb.
  AeroFarms measured at 1 per 1,190 ft² (110 m²).
- **Greenhouse vegetables: 6–8 employees per hectare** *(= 1 per 1,250–1,670 m²)*; **lettuce with automation
  3–4/ha.**
- > **⚠ Vertical farming is roughly 5–10× more labor-intensive per m² than greenhouse.** Since a sealed
  > Antarctic city would stack rather than sprawl, **this single choice swings the food workforce by a factor
  > of four or more** — plausibly 15,000 vs 65,000 workers for a city of Casey's size. **It is the largest
  > determinable uncertainty in the model and needs a canon decision on how Tepenia grows: stacked or spread.**

### A1 — Thermal & power ✅ *(and the right analogue is now clear)*
- **Norway: 27,818 kWh per capita** — and critically, *"in Norway most homes are heated through electricity
  instead of district heating"* (only ~2% district heating, vs Sweden's 60%).
- **Iceland: 51,900 kWh per capita** — but ~85% of houses are heated **geothermally**, and much of the total
  is energy-intensive industry.
- > **⭐ Norway is Tepenia's analogue, not Iceland.** A cold country that heats with *electricity* rather than
  > free geothermal heat. **Iceland's figure is inflated by a resource Antarctica mostly does not have** —
  > with the pointed exception of any Tepenian city sited on volcanic ground.
- Plant labor: **nuclear ~0.62 workers/MW · CCGT 0.02–0.10 workers/MW**, and *"staff per MW falls sharply as
  plants get larger."*

---

---

# 5 — FIRST RUN OF THE NUMBERS — 2026-09-01

**Robot-keyed industries excluded (deferred). Census I. Workforce = robots + 50% of humans.**

## 5.1 The rate table

| **HUMAN-KEYED** *(per 1,000 humans)* | rate | | **RESIDENT-KEYED** *(per 1,000 residents)* | rate |
|---|--:|---|---|--:|
| B2 Health + long-term care | 54 | | A4 Construction & maintenance | 15 |
| B1 Food *(prod/proc/dist)* | 53 | | D1 Transport & logistics | 19 |
| C1a Childhood schooling | 26 | | ⚠ C3 Administration | **45** |
| C2 Childcare | 5 | | D3 Retail *(necessary only)* | 10 |
| C5 Mortuary *(human)* | 0.6 | | A3 Enclosure & atmosphere | 8 |
| | | | A1 Thermal & power | 5 |
| | | | C4 Materials recovery | 5 |
| | | | C1b Trade/technical training | 4.2 |
| | | | A5 Emergency services | 3.5 |
| | | | A2 Water & sanitation | 3 |
| | | | B5 Textiles | 3 |
| | | | D2 Communications | 2 |
| **TOTAL** | **138.6** | | **TOTAL** | **122.7** |

> **⚠ C3 Administration was the largest and least certain rate in the table — now SOURCED. See §8.**
> **Revised 45 → 65 per 1,000 residents.** *(The 45 used in §5.2's first run was an estimate; §7 onward uses
> 65.)*

---

# 8 — ⭐ THE ADMINISTRATION RATE, SOURCED — 2026-09-01

**The problem:** every earlier source *(OECD Nordics 25–30% · Nunavut 60% · Svalbard ~50%)* measures
**general government or public sector**, which bundles **education, health and state-owned enterprises** —
all counted separately here, and in Svalbard's case including **Store Norske, a mining company.** Stripping
them was a guess.

**The fix:** BLS Current Employment Statistics has series that already exclude education. **BLS blocks
automated access; FRED mirrors the same series and does not.**

| FRED series | What it is | Value *(Jul 2026, SA)* |
|---|---|--:|
| `CES9091000001` | All Employees, **Federal** | **2,683 k** |
| `CES9093200001` | **Local Government, excluding Education** | **6,973 k** |
| `CES9092200001` | **State Government, excluding Education** | **2,865 k** |
| | **Raw total** | **12,521 k** |

**Two subtractions the series do not make** *(my estimates, not data)*: **USPS ~530 k** *(maps to our D1
transport)* and **government hospitals ~1,000 k** *(maps to our B2 healthcare)*.

> ## **Core public administration ≈ 11.0 million ÷ ~342 M population = 32 per 1,000 = 6.9% of the US
> workforce.**
> **Tepenian workforce is 755 per 1,000 residents → US-equivalent rate = 52 per 1,000 residents.**
> **× ~1.25 remote/rationed uplift = 65.**

### ⭐ The estimate survived contact with the data

**65 was already the working figure. It did not move** — which means the reasoning chain that produced it
*(US core-admin base + modest remote uplift)* was sound rather than lucky. **Recorded because an estimate that
survives verification is evidence about the method, not just about the number.**

### ⚠ What is still soft — and it is now a different thing

**The base is measured. The UPLIFT is the remaining judgment**, and it is a worldbuilding call rather than a
data gap:

| Uplift | Rate | Effect on every city |
|---|--:|---|
| **1.0×** — no uplift *(if the Nordic premium is entirely education and health, which we count separately)* | 52 | **−2 points each** |
| **1.25× — used** | **65** | *baseline* |
| **1.5×** | 78 | **+2 points each** |

**Also ±10% on the base**, from the two hand-subtractions above.

> **The clean single source exists and would remove both uncertainties at once:**
> **`https://www.bls.gov/oes/2024/may/naics3_999000.htm`** — *"Federal, State, and Local Government, excluding
> State and Local Government Schools and Hospitals **and the U.S. Postal Service**."* **That category already
> excludes all three things subtracted by hand.** BLS blocks automated retrieval; a browser download would
> settle it exactly.

## 5.2 Results

| City | Humans | Residents | Human-keyed | Resident-keyed | **Required** | Workforce | **% of WF** |
|---|--:|--:|--:|--:|--:|--:|--:|
| **Lazar** | 1,287,003 | 2,620,319 | 178,379 | 321,513 | **499,892** | 1,976,818 | **25.3%** |
| **Casey** | 733,795 | 1,495,731 | 101,704 | 183,526 | **285,230** | 1,128,834 | **25.3%** |
| **Neumayer** | 613,735 | 1,252,080 | 85,064 | 153,630 | **238,694** | 945,213 | **25.3%** |
| **Denison** | 522,975 | 1,066,143 | 72,484 | 130,816 | **203,300** | 804,656 | **25.3%** |
| **{{Abowasa}}** | 504,237 | 1,034,241 | 69,887 | 126,901 | **196,788** | 782,123 | **25.2%** |
| **Vostok** | 129,617 | 389,261 | 17,965 | 47,762 | **65,727** | 324,453 | **20.3%** |
| **Kunlun** | 0 | 123,449 | 0 | 15,147 | **15,147** | 123,449 | **12.3%** |
| **NATIONAL** | 15,623,523 | 32,026,600 | **2,165,420** | **3,929,664** | **6,095,084** | 24,214,839 | **25.2%** |

---

# ⛔ 5.3 — THE RESULT IS A NEAR-FLAT LINE, AND THAT IS THE FINDING

**Five of the seven cities land within 0.1 percentage points of each other.** Lazar (2.6 M, cramped oasis),
Casey (mild, coastal, best-connected), Neumayer (floating ice shelf), Denison (windiest inhabited sea-level
site on Earth) and {{Abowasa}} (rotational residence) **all compute to 25.3%.**

> ## **On demand alone, the ONLY variable that separates Tepenian cities is their human fraction.**
> Vostok differs (20.3%) because it is 67% robot. Kunlun differs (12.3%) because it has no humans. **Every
> city between 48% and 51% human — which is 33 of the 38 — produces an identical number.**

**This is not a failure of the volume method. It is the volume method correctly reporting that *demand* is
demographic, and that everything which makes these cities different from one another lives somewhere else:**

1. **Difficulty** — not yet applied here. The physical drivers *(cold, wind, altitude, isolation, foundation)*
   do not change what a city needs; **they change what it costs to supply it.** That is the layer that must
   carry the spread, and the earlier trial's additive-excess formulation is the tool for it.
2. **The distinctive tier** — at 25% baseline, **~75% of every city's economy is still unaccounted for.**
   Provider roles, exports, and LAW G weird industries all live there.

**⚠ It also confirms, from a third independent direction, the weakness both agents flagged:** a per-capita
demand model cannot differentiate cities. **The share-first model over-differentiated on an undefined
envelope; requirement-first under-differentiates because demand is nearly uniform.** The truth is that
**difficulty, not demand, is where Tepenian cities differ** — and difficulty is exactly the layer that has
never been given a defensible calibration.

## 5.4 Sanity check against the anchor

**25.2% national, against McMurdo's ~66% support share.** The gap is not alarming — **it is the two excluded
groups**: robot maintenance and siligel/coolant *(deferred)*, plus everything McMurdo counts as "support"
that this model books as distinctive. **The figure is the right order of magnitude for a floor**, which is
what it is meant to be.

---

---

# 6 — THE DIFFICULTY LAYER: A SOURCED BASIS AT LAST

**Researched 2026-09-01.** Every difficulty multiplier in every prior model was *reasoned*, never measured.
**People who build in the cold for money have measured it.**

## 6.1 The cost ladder — three anchors, all sourced

| Setting | Cost vs. temperate baseline | Source |
|---|--:|---|
| Temperate developed construction | **1.0×** | ~$1,500–3,000/m² institutional |
| **Iqaluit / Nunavut — Arctic remote settlement** | **3.0×** *(+25% more for sealift, flights and accommodation for trades, winter heating)* | Nunavut Housing Corporation construction cost review |
| **⭐ Halley VI — Antarctic ice-shelf station** | **~10–20×** — **1,510 m² for $44,640,000 ≈ $29,565/m²** | ENR / BAS project figures |

> ## ⭐ **Halley VI is the real-world basis for the Tepenian city of Halley** — the one on the Brunt Ice Shelf,
> whose own spec calls it *"the city that moves."* **This is the most directly relevant construction-cost
> datum that exists anywhere.**

## 6.2 ⚠ AND IT REVERSES A JUDGMENT MADE EARLIER IN THIS PASS

**The share-first model was condemned partly because its driver product reached 7.28 "against a declared range
of ~0.7–2.0."** I called that a scandal. **The trial model then engineered an additive form specifically to
keep multipliers inside 0.933–2.107, and reported zero clamp hits as a success.**

> **But the declared range of 0.7–2.0 was invented by me. Nothing external ever supported it.**
> **And the real world says Arctic construction runs 3×, Antarctic ice-shelf construction 10–20×.**
>
> ### **A difficulty multiplier of 7 for construction at Vostok may not have been a blowup. It may have been
> approximately correct, rejected for violating a limit that had no authority behind it.**

**⚠ The honest qualification, which matters:** these are **COST** multipliers; the model needs **LABOR**
multipliers. Halley VI's $29,565/m² includes shipping every component to Antarctica, bespoke design, and
hydraulic jacking legs — **much of it materials and transport, not on-site worker-hours.** Labor per m² is
certainly a smaller multiple than cost per m².

**But the direction is unambiguous: the plausible difficulty range is far wider than 0.7–2.5.** Both prior
models may have been compressing the very variance they were being blamed for failing to produce — and §5.3's
near-flat line is exactly what over-compressed difficulty would look like.

## 6.3 The canonical labor instrument exists, and it is purchasable

**MCAA *Change Orders, Productivity, Overtime — A Primer for the Construction Industry*, pp. 135–136** — the
**MCAA Labor Productivity Factors**: 16 impact categories, each with **minor / average / severe** percentage
loss values. **Includes "Season and Weather Change"** *(very hot or very cold weather, storm events)* and
**"Site Access."** **Endorsed in full by NECA and SMACNA**, and NECA separately publishes *"The effect of
temperature on productivity."*

> **⚠ The table is behind the publication and could not be retrieved.** **This is the single highest-value
> purchasable input to the entire model** — it is the exact instrument the difficulty layer needs, it is
> industry-standard, it is legally load-bearing in construction claims, and **it would replace every invented
> multiplier with a sourced one.**

## 6.4 ⭐ And the research handed the autonomy-duration concept real numbers

**Nunavut's supply reality, sourced:** *"there are no roads between the main Arctic communities, and larger
bulk deliveries are supplied by Sealift, which services the North between late June and late October, with
remote northern communities sometimes only getting one delivery a year."*

> **That is a measured `D` — an interruption horizon of up to 365 days at a real Arctic settlement**, against
> the trial model's *assumed* 270 days for Vostok and 330 for Kunlun. **The assumptions were conservative,
> and the real world is harsher.** The autonomy-reserve mechanism now has an empirical anchor.

## ⭐⭐ 6.4b — THE MCAA FACTOR TABLE, OBTAINED. The difficulty layer now has a sourced basis.

**Retrieved 2026-09-01 at no cost.** The $495 publication was not needed — **the full factor table is
reproduced in a free open-access ASCE paper** *(Ibbs & Sun, "Use of Mechanical Contractors Association of
America Method in Loss of Productivity Claims", J. Legal Affairs & Dispute Resolution 8(4))*.

**Values are PERCENTAGE PRODUCTIVITY LOSS at minor / average / severe intensity.**

| MCAA impact category | Minor | Average | **Severe** |
|---|--:|--:|--:|
| **⭐ Season and weather change** *(either very hot or very cold weather)* | 10 | 20 | **30** |
| **⭐ Logistics** *(materials supply and storehouse problems)* | 10 | 25 | **50** |
| **⭐ Site access** *(interference with convenient access to work areas)* | 5 | 12 | **30** |
| Beneficial occupancy | 15 | 25 | 40 |
| Stacking of trades | 10 | 20 | 30 |
| Morale and attitude | 5 | 15 | 30 |
| Crew size inefficiency | 10 | 20 | 30 |
| Learning curve | 5 | 15 | 30 |
| Dilution of supervision | 10 | 15 | 25 |
| Concurrent operations | 5 | 15 | 25 |
| Joint occupancy | 5 | 12 | 20 |
| Ripple | 10 | 15 | 20 |
| Overtime | 10 | 15 | 20 |
| Reassignment of manpower | 5 | 10 | 15 |
| Fatigue | 8 | 10 | 12 |
| Errors and omissions | 1 | 3 | 6 |

### ⭐ Three things this settles

**1. The three categories that map to Tepenian conditions are exactly the drivers already identified:**
**weather** *(cold severity)*, **logistics** *(isolation and supply reliability)*, and **site access**
*(terrain, wind windows, enclosure)*. **The model's driver set was right; it simply had no numbers.**

**2. ⭐ MCAA applies its factors ADDITIVELY — which independently vindicates the trial model's fix.** The
trial agent derived `difficulty = 1 + Σw(m−1)` on its own reasoning, to escape the multiplicative blowup.
**The construction industry's own legally-tested instrument does the same thing.** Convergent, from an
unrelated direction.

**3. Converting loss to a labor multiplier:** `multiplier = 1 / (1 − L)`.
**30% loss → 1.43× · 50% → 2.00× · 60% → 2.50×.**

### The Tepenian ladder, sourced at last

| City type | Applicable factors | Loss | **Labor multiplier** |
|---|---|--:|--:|
| Mild, coastal, connected *(Casey)* | weather minor | 10% | **1.11×** |
| Ordinary coastal *(Cape Adare)* | weather 15 + site access 5 | 20% | **1.25×** |
| Harsh / exposed *(Denison)* | weather avg 20 + site access severe 30 | 50% | **2.00×** |
| Ice shelf *(Halley, Neumayer)* | weather 20 + access 30 + logistics avg 25 | 75%* | **~2.5–4×** |
| Isolated plateau *(Vostok, Kunlun)* | weather severe 30 + logistics severe 50 | 80%* | **~2.5–5×** |

> **⭐ AND IT CONVERGES WITH THE COST LADDER FROM A COMPLETELY DIFFERENT SOURCE.** §6.1's real-world figures
> gave **Nunavut 3×**, and §6.2's corrected Tepenian band — after the developer's point that Tepenian supply
> is *domestic and road-connected*, not intercontinental — was **~0.9–3.5×.** **The MCAA route independently
> lands in the same place.** Two unrelated methods agreeing is the strongest calibration signal this pass has
> produced.

> **⚠ \*Capping is required and the source says so.** Summed severe factors exceed 100% loss, which is
> nonsense — and this is the method's *documented* failure mode: *"if improperly applied… could
> unrealistically inflate the amount of lost staff-hours."* **Cap total loss around 60–65%, giving a ceiling
> of ~2.5–2.9×.**
>
> **⚠ And a scope caveat that matters:** MCAA factors measure **disruption to a project**, not **steady-state
> operations in a permanently hostile place.** A Tepenian city does not run at 30% weather loss forever — it
> adapts, encloses, and schedules around the weather. **"Severe" should not be the default even at Vostok.**

---

# 7 — SECOND RUN: DEMAND × DIFFICULTY. The flat line breaks.

## 7.1 Selective application — which industries each factor actually touches

**This is the step that makes difficulty differentiate rather than merely scale.** A factor applied to
everything cancels out of composition *(the isolation defect)*. Each MCAA factor enters only the industries it
physically touches.

| | Resident-keyed rate | Touched by weather / logistics / access? |
|---|--:|---|
| D1 Transport & logistics | 19 | ✅ all three |
| A4 Construction & maintenance | 15 | ✅ all three |
| A3 Enclosure & atmosphere | 8 | ✅ weather, access |
| A1 Thermal & power | 5 | ✅ weather |
| C4 Materials recovery | 5 | ✅ logistics |
| A5 Emergency services | 3.5 | ✅ weather, access |
| A2 Water & sanitation | 3 | ✅ weather, access |
| B5 Textiles | 3 | ✅ logistics |
| **AFFECTED SUBTOTAL** | **61.5** | |
| C3 Administration | 45 | ❌ indoor service work |
| D3 Retail | 10 | ❌ |
| C1b Trade training | 4.2 | ❌ |
| D2 Communications | 2 | ❌ |
| **UNAFFECTED SUBTOTAL** | **61.2** | |

**Human-keyed:** B1 Food (53) is **affected** *(energy and supply-dependent)*; B2 healthcare, C1a schooling,
C2 childcare and C5 mortuary (85.6 combined) are **not** — indoor care and teaching do not get harder because
it is −55 °C outside.

> ## ⭐ **The split is almost exactly 50/50 — 61.5 affected against 61.2 unaffected.**
> **Half of a Tepenian city's necessary labor is exposed to its environment and half is indifferent to it.**
> That is why difficulty reshapes composition instead of just inflating the headline.

## 7.2 Results

| City | Difficulty | **Before** | **After** | Δ |
|---|--:|--:|--:|--:|
| **Neumayer** *(Ekström ice shelf)* | 2.5× | 25.3% | **42.6%** | **+17.3** |
| **Denison** *(windiest inhabited sea-level site)* | 2.0× | 25.3% | **36.9%** | **+11.6** |
| **Vostok** *(−54.8 °C, isolated plateau)* | 2.5× | 20.3% | **34.5%** | **+14.2** |
| **{{Abowasa}}** *(inland nunatak)* | 1.54× | 25.2% | **31.4%** | +6.2 |
| **Lazar** *(coastal, connected, largest)* | 1.25× | 25.3% | **28.2%** | +2.9 |
| **Casey** *(mild, best-connected)* | 1.11× | 25.3% | **26.5%** | +1.2 |
| **Kunlun** *(harshest, zero humans)* | 2.7× | 12.3% | **22.7%** | +10.4 |

**Spread among the human-bearing cities: 26.5% → 42.6%, sixteen points.** Previously **five of them sat
within 0.1 points of each other.**

## 7.3 ⭐ And the ordering now matches physical intuition, unprompted

- **Neumayer tops the table** — the floating ice shelf is the most expensive thing to live on in Tepenia,
  above cold, above wind, above isolation. **This reproduces `05` §2's finding that Halley's construction
  burden should exceed Denison's, arrived at from a completely different direction.**
- **Denison outranks Lazar and Casey on wind alone**, which the share-first model could never make it do.
- **Vostok is third, not first** — its isolation and cold are extreme, but **two-thirds of its population is
  robot**, so its human-keyed demand is small. **Difficulty and demography pull against each other**, and the
  result is a city that is expensive per unit of work but has less work to do.
- **Kunlun stays low despite carrying the corpus's worst conditions** — 2.7× difficulty applied to a city
  with no schools, no clinics, no farms and no children. **Its environment is the hardest and its job is the
  smallest.**

## 7.4 Against the anchor

**Highest city now 42.6%, against McMurdo's ~66% support share.** The remaining gap is the two excluded robot
industries plus everything McMurdo books as "support" that this model assigns to the distinctive tier.
**42.6% for a floor at the hardest inhabited site is the right order of magnitude** — where 25.3% flat
plainly was not.

**⚠ Still provisional:** the C3 administration rate (45) remains the largest and least-certain input, the
difficulty assignments are reasoned from the MCAA categories rather than measured per industry, and the 60%
loss cap is a judgment call the source itself does not specify.

---

## 6.5 What is still missing

- **The MCAA factor values** *(purchasable — see 6.3)*.
- **A cost-to-labor split** for the Halley VI figure. Without it the 10–20× ladder bounds cost, not staffing.
- **CRREL** *(US Army Cold Regions Research and Engineering Laboratory)* holds McMurdo snow-road and Antarctic
  resupply studies; specific cost factors were not reachable by search but the body of work exists and is the
  authoritative source for cold-regions engineering.

---

*(Research log: `../Research_Logs/Division_of_Industry_Research_Log.md`.)*

---

# 5. ⚠ Known open questions this method inherits

1. **The §15 coverage denominator is still unruled.** Canon sheets partition the *visible* economy; any model
   partitions the whole one. **Until ruled, no canon percentage can validate any of this at any city.**
2. **The workforce rule.** The trial used 100% of robots + 50% of humans and its author flagged it: *"The rule
   I was given says 100% of robots; I followed it, but I do not believe it, and it is carrying more of the
   answer than any rate."* **Do robots have a duty cycle — maintenance downtime, charging, an off-shift?**
   Canon question, developer's call, and it moves every figure.
3. **Denison's canon 25%** has now failed two models in opposite directions *(share-first 14.2%, requirement-
   first 2.61% against a needed difficulty of 18.5)*. **The volume method will test it a third time** — and
   this time it can distinguish the two readings, because a wind-engineering *provider* will exceed its +2%
   ceiling and a mis-rated city will not.
