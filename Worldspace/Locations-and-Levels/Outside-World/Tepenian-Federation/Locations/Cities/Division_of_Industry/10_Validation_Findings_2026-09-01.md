# Validation Findings — the national food balance and the proposed reserve program

> ## ⛔ **OUTCOME: THE PROPOSED NATIONAL FOOD RESERVE PROGRAM WAS WITHDRAWN, NOT ADOPTED.**
> **Three independent checkers, run on deliberately non-overlapping angles, none told the conclusion or which
> variant the author favored. All three returned adverse. They converged from different directions on the same
> judgment: the program answered a question the model could not actually pose.**
>
> **Recorded 2026-09-01.** `[CGRM 2026-09-01 · Path 2 · two-agent validation protocol, three-checker variant]`

**This file exists because the findings are more valuable than the proposal was.** Several of them invalidate
figures elsewhere in this folder. **Read this before citing any food figure from `04`, `05`, `09` or `README`.**

---

# What was proposed, and what it claimed

A national food reserve, funded by a uniform or weighted uplift on net-exporter cities.

| | Uniform (A) | Weighted (B) |
|---|--:|--:|
| Uplift | 17.5% ± 1–2pp on every exporter | 17.5% baseline, redistributed toward high-headroom cities |
| National surplus | ~7.3% | **9.03%** |
| Days accrued per year | ~27 | **33.0** |
| Years to a 120-day reserve | ~4.5 | **3.6** |
| Worst-hit city | Davis at ~7.2% | Juan Carlos 7.2%, **Davis down to 2.9%** |

**Variant B won on every headline measure.** That is the first thing the checkers attacked.

---

---

# ⭐⭐ FINDING 1 — THE HEADLINE NATIONAL BALANCE IS CIRCULAR. It demonstrates nothing.

**The single most important finding. It invalidates the result the whole proposal rested on.**

The pass reported a national food requirement of **822,291 producers** against a baseline supply that matched
it *"within 1%"* — and that agreement was cited, repeatedly and by the author, as evidence that the canon §15
sector percentages had been well-set.

**It is not evidence. It is one number written twice.**

```
1000 / 53          = 18.87   ("53 per 1,000" and "1 producer per 19 people" are the same rate)
15,623,523 / 19    = 822,291 (exactly the claimed national requirement)
```

**And the rate has no independent derivation anywhere in the corpus.** `08` §4.5 — the only research on the
food labor rate — delivers m²-based figures only *(1 FTE per 279 m² vertical; 6–8 per hectare greenhouse)* and
**explicitly refuses to pick a number**, calling the choice *"the largest determinable uncertainty in the
model."* The rate `53` then appears fully formed in `08` §5.1 with nothing behind it.

> ## **Its actual origin is `04` §4 — where it was computed by summing the seven provider cities' canon §15
> food sectors and dividing by population.**
>
> ```
> 306,780+210,093+65,816+87,546+42,638+93,889+28,463 = 835,225
> 835,225 / 15,623,523 = 0.05346  →  "1 food producer per ~19 people"
> ```
>
> **That is a SUPPLY figure. It was inverted into a DEMAND rate, inserted into the baseline formula, and the
> resulting demand was then compared back against the same §15 sheets and reported as a match.**

**`04` §4's own words — *"That closes"* — describe a rate being fitted, not a prediction being tested.** The
later run adds difficulty weighting and the distinctive-tier envelope, so it is not a literal algebraic
identity; **the closure is inherited, not earned.**

## The balance is below the model's own resolution

| Perturbation | Swing | vs. the +7,248 headline |
|---|--:|--:|
| Writing the rate as `1/19` instead of `53/1000` | 8,210 | **113%** |
| Marine discounts moved to (¼, ½) vs (½, ¾) | 172,769 | **2,384%** |
| Full-workforce vs. distinctive-tier convention | ~690,000 | **9,520%** |

> ### **A rounding choice between two ways of writing the same rate moves the national balance by more than
> the entire result.**

**⚠ And `README`'s claim that *"the rates — sourced against NFPA, WHO, UNESCO, FAO…"* is FALSE AS APPLIED TO
B1** — the one rate the entire food pass depends on. README's "known-and-stated uncertainties" names
Administration's ±1.7 points *(which changes no ranking)* and **omits B1 entirely.** It flags the uncertainty
that does not matter and omits the one that does.

---

# ⭐⭐ FINDING 2 — THE EXPORT DEFINITION DOUBLE-COUNTS, and two contradictory national balances are currently published in this folder

**Structurally larger than the circularity.**

The baseline formula contains `Humans × 53 · D / 1000`. **That term IS the city's own food workforce, inside
baseline.** README rules `baseline + distinctive = 100%` of the workforce — so **every city already staffs its
own food need by construction.**

The pass then computed `export = (distinctive-tier food sector) − (baseline food need)`, **booking the same
need a second time.**

- **Concordia**: 763,548 workers, 41.8% baseline *(which already contains 44,680 food workers)*. Its §15 names
  no food sector, so the model assigns it **−44,680** — workers simultaneously supplied and missing.
- Same for **Denison (−55,435), Shirayuki (−38,191), Lazar (−85,264), Halley (−94,042)**. In every case the
  deficit is *exactly* `humans × 0.053 × D`, **i.e. the city is credited with ZERO local food.**

**This flatly contradicts `04` §4's own recommended structure — *"Every city grows what it can locally"* — and
the `City_Logistics.md` Concordia precedent.**

## ⛔ The two published balances

```
README "First results":  Davis exports 269,442   (876,515 × 0.35 − 37,338)          ← full workforce
the per-city run:        Davis exports 157,774   (876,515 × 0.636 × 0.35 − 37,338)  ← distinctive tier
difference, ONE city:    111,668  =  15× the entire national headline surplus
```

**Nationally the convention choice moves supply from ~1,188,279 to ~1,871,000 — a net of +690,275 (+36.9%)
instead of +7,248.** **Two mutually inconsistent national food balances sit in the same folder and nothing
states which governs.** → **DRQ-09.**

---

# ⭐ FINDING 3 — A UNITS ERROR THAT MAY REMOVE THE CRISIS ENTIRELY

**Demand is difficulty-weighted (`×D`); supply is a raw headcount with no difficulty correction.** The model
asserts non-uniform productivity in one place and assumes uniform productivity in the other.

**It matters because exporters are systematically low-D and deficit cities systematically high-D.** A Davis
producer *(D=1.25)* feeds `1/(0.053×1.25) = 15.1` people; a Halley producer *(D=2.50)* feeds **7.5**.

```
sample exporters: 406,516 heads →  6,297,693 people fed    (15.49 people/head)
sample deficits : 352,995 heads →  3,868,038 people short  (10.96 people/head)

net in HEADS      :    +53,521
net in PEOPLE-FED : +2,429,655
```

**Scaled nationally: +13.8%, ≈50 days of reserve accruing per year, filling 120 days in ~2.4 years with no
uplift at all.**

> ## ⛔ **The "2.2 days / knife-edge" framing is an artifact of adding workers of unequal productivity. The
> 17.5% uplift was a fix for a problem that may not exist.**

*(The true figure sits between the two — imported food still pays a distribution penalty on arrival, since B1
is "production / processing / distribution" — but the model's version is at the wrong end and is unjustified.)*

---

# ⭐ FINDING 4 — THE MARINE DISCOUNTS ARE A FREE PARAMETER, AND THE SIGN FLIPS INSIDE A DEFENSIBLE RANGE

```
⅓-rule pool (undiscounted): 425,235   Cape Adare 177,732 · Princess Elisabeth 79,430 ·
                                      Troll 65,568 · Fort McMurdo 52,722 · Dumont d'Urville 49,782
⅔-rule pool (undiscounted): 265,841   Janbogo 124,985 · Belgrano 98,484 · Sanay 42,372
```

| Discounts | National net | % of production | Days/yr |
|---|--:|--:|--:|
| **¼ and ½** | **−72,495** | **−6.10%** | −22.3 |
| **⅓ and ⅔ (as built)** | +7,248 | +0.61% | +2.2 |
| **½ and ¾** | **+100,274** | **+8.44%** | +30.8 |
| 0 and ⅓ *(if marine sectors are mostly port work)* | −223,111 | −18.78% | −68.5 |

**Total swing across the plausible range: 172,769 producers = 14.5% of national production = 24× the headline
result.** Both factors are flagged unresolved in `04` §7 — *"Splitting those properly is per-city hand work."*

> **⚠ The two least-justified numbers in the model are the two the headline result is most sensitive to. Any
> balance landing near zero here should be read as "the parameters were set to land near zero."**

**⚠ And the still-open Cape Adare provider contradiction *(`04` §3 vs §4)* is the single largest item in the ⅓
pool at 177,732 undiscounted workers. The biggest unresolved provider question sits on the biggest sensitivity
lever.**

---

# ⭐⭐ FINDING 5 — THE MARINE INCREASES WERE DISTRIBUTED ALMOST EXACTLY BACKWARDS

**Ecological check, against CCAMLR primary sources. Verdict: *reckless*, and specifically correctable.**

## 5a. The 9.3% reference rate is obsolete, and was never the operating rate

| Parameter | Value |
|---|--:|
| Area 48 precautionary catch limit | 5.61 Mt |
| **Area 48 trigger level** | **620,000 t** *(11% of the PCL)* |
| Area 48 krill biomass *(2019 synoptic survey)* | 62.6 Mt |
| **Subarea 48.1 Grym-derived gamma, endorsed 2022** | **0.0338 — 3.4%, not 9.3%** |
| Ross Sea toothfish limit, entire region | **3,499 t/yr** |

> ## **The rate CCAMLR actually operates is 620,000 t against 62.6 Mt — about 1.0%. Not 9.3%, not 3.4%. One
> percent, held for 35 years in the richest krill ground on Earth.**

**The gap between the paper limit and the operating limit IS the margin of precaution, and it has never been
spent.** The trigger is explicitly *not* a yield estimate — it is an administrative brake based on historical
catches, adopted in 1991 to stop the whole limit being taken from a small area.

## 5b. ⭐ A polynya is an ACCESSIBLE feature, not a productive one — the core scientific error

**Primary production is genuinely high** *(Ross Sea polynya ~151 g C m⁻² yr⁻¹, among the highest in the
Southern Ocean)*. **It does not reach anything harvestable, for three documented reasons:**

1. **The bloom organism is inedible to the harvestable food chain.** Ross Sea blooms are dominated by
   *Phaeocystis antarctica*, *"not grazed by mesozooplankton, being grazed by microzooplankton at only low
   rates."* Its carbon exports rapidly to depth or routes through the microbial loop.
2. ***Euphausia superba* is largely absent.** South of ~74°S it is replaced by ice krill *E. crystallorophias*
   at **3.0 g per 1,000 m³** — roughly two orders of magnitude below the dense surface swarms that make
   commercial krill trawling economic at all.
3. **The three harvestable stocks are the worst possible candidates.** *E. crystallorophias* is a shelf endemic
   with **no biomass assessment and no catch limit anywhere in the world**, because nobody has ever proposed
   taking it at scale. *Pleuragramma antarctica* — Antarctic silverfish — is the shelf's keystone forage fish
   and **Terra Nova Bay is its nursery** *(larval concentrations averaging 14,764 individuals/m²)*.

> ## **High primary production + a food chain that doesn't transmit it + low-density endemic consumers =
> ACCESSIBILITY WITHOUT SURPLUS. The proposal confused the two.**

**A polynya is a *concentration* feature — ice-free, so ships can reach it, and predators aggregate for the
same reason. It is an "ice factory," not a nutrient pump feeding a large exportable stock.**

## 5c. The real-world siting is about as protected as water gets

- **Ross Sea region MPA** *(CM 91-05, in force 2017)* — 2.09 million km², the world's largest. The **General
  Protection Zone is 72% of it and is NO-TAKE.**
- **Terra Nova Bay and its polynya are named individually in the MPA Research and Monitoring Plan, assigned to
  the GPZ, carrying ALL FOUR impact codes at once** *(T1–T4)* — one of only a handful of features flagged on
  every axis.
- **ASPA 173** *(Cape Washington and Silverfish Bay)* protects the world's **second-largest emperor penguin
  colony, 25,000+ breeding pairs**, together with the silverfish nursery. **ASPA 161** covers a further
  29.4 km².

## 5d. Toothfish: the ramp is shorter than the detection time

von Bertalanffy **k ≈ 0.111**; **maturity ~13–16 years**; **longevity 39+ years**. The Ross Sea catch limit has
sat between **1,980 and 3,499 t for 28 consecutive years** to hold the stock at 65% B₀, against a target of
≥50% B₀ over a **35-year** projection.

> **A 4-year ramp is shorter than the time it takes to detect the damage.** The program would be declared a
> success roughly a decade before the recruitment failure surfaced — under a different administration.

## 5e. ⭐ The corrected distribution

| Location | Proposed | **Defensible** |
|---|--:|---|
| **Polynya cities** *(ice krill, silverfish, toothfish)* | +38% | **0%.** If a number is required: **+5% ceiling**, mid-water species only, outside the Oct–Feb breeding window, gated on a completed acoustic survey, hard cap **<1% of surveyed local standing stock** |
| **Scotia Sea krill** | +20% | **+20% on tonnage — but only with a BINDING SPATIAL RULE.** Cap any single management unit at ~25–30% of the sector total; exclude 30–50 km around breeding colonies in season |
| **Queen Maud Land / Weddell** | +25% | **+25%, and plausibly +50–100%.** Div. 58.4.2 carries a 450,000 t limit and is essentially unfished. ⚠ Real headroom, but **poorly surveyed** — the honest gate is "survey first" |
| **Davis greenhouse** | +36% | **No ecological ceiling.** Limited by energy, glass, CO₂, labor, logistics — engineering problems, all solvable with capital |

> ## **"The polynya cities' role in a national food reserve is not production — it is survey, monitoring and
> the enforcement of everyone else's limits. That is a job. It is just not the job the proposal gave them."**

---

# ⭐ FINDING 6 — THE COST IS DENOMINATED IN THE WRONG UNIT

**Both variants are priced in *labor percent*. Neither of the two things being bought is a labor problem.**

- **Krill is capital, not labor.** `04` §6.1, verbatim: *"krill fishing is capital-intensive, not
  labor-intensive. A fleet does not need a million people."* **Variant B's 38% uplifts are hulls, freezer
  capacity and fluoride-stripping processing lines** — paid by **Sinheung, Rothera, Fort McMurdo and Byrd,
  cities that appear nowhere in either variant's cost ledger.**
- **Davis is power-limited, not land-limited.** `04` §6.2: *"Ice-free does NOT mean arable… production is
  greenhouse and hydroponic regardless of geology."* Controlled-environment agriculture scales with **power and
  structure**. The nearest canon analogue is Vostok, diagnosed in `04` §5 as *"not 'too few farmers' but 'food
  here costs power the city does not have'"* — **labor-sufficient, energy-insufficient.**

**⚠ And this is a nation whose currency is denominated in guaranteed grid capacity.** A program here should be
costed in **watts**. Until it is, "Davis surrenders 7.2%" is not comparable to anything, including itself.

## Three further defects in the strain metric

1. **The denominator is not discretionary.** `09` §3.5's own qualification 2: the distinctive tier holds
   **mandated provider work** — Sinheung's fabrication, Sanay's docks. **Taking 10% of Sinheung's distinctive
   tier costs the NATION its chamber supply, not Sinheung its character. Strain prices the local cost and none
   of the national one.**
2. **Difficulty enters twice.** The numerator is difficulty-inflated *(`×D`)* and the denominator
   difficulty-deflated *(distinctive = 1 − baseline, and baseline rises with D)*. **Strain at high-D cities is
   squared relative to low-D cities and is not comparable across the table.**
3. **It is city-scoped, but the model's own Weddell fix is subnet-scoped** *(commuter labor from Halley and
   {{Abowasa}})*. **Strain computed per city cannot represent the mechanism that closes the gap.**

---

# ⭐⭐ FINDING 7 — THE DISTRIBUTIONAL RESULT INVERTS THE FRAMING, and nobody noticed

**`09` §3.5's headline finding: the freedom gradient runs OPPOSITE to the familiar one.** *"The Peninsula is
simultaneously the easiest place to live AND where the food comes from… Meanwhile the hardest-working cities in
the country have the least to show for it. That is a resentment engine, built into the geography, requiring no
villain."*

**Score the two variants against that, and they swap places:**

- **Variant B takes its increase overwhelmingly from the Peninsula and the krill grounds — the FREEST cities.
  It NARROWS the freedom gap.**
- **Variant A taxes everyone the same percentage — which, against an existing 28.9%–51.4% baseline spread,
  takes proportionally more from the cities that have least.**

> ## **On the project's own most important social finding, B is the PROGRESSIVE option and A is the REGRESSIVE
> one — and neither document said so, because "% of non-food economy" treats an hour at Rothera and an hour at
> Neumayer as identical, which is the exact fiction §3.5 exists to destroy.**

**⚠ With teeth:** Halley and Neumayer are not exporters, so they pay nothing — **but they eat.** A national
reserve means **the hardest-working cities consume a benefit the freest cities paid for.** That is the
resentment engine running **backwards for the first time in the setting's history.**

**And what is being spent is not budget.** `09` §3.5 and the `Robot_Physiology` ruling establish the residual
as **the material proof that leaving Upper Earth worked** — leisure that was *"contingent, personal, and
revocable"* there and is *"universal, owed to nobody"* here. `09` §3.5 also establishes that **provider work
counts as mandated**: *"A stevedore at Sanay is not there by preference; the Federation needs a port."* **A
national food program is a machine for manufacturing exactly that category** — and `Robot_Physiology` already
holds that overwork is *"a HAZARD WITH A MECHANISM,"* sitting close to the faulty-semantic-signal model of
robot illness. **A national uplift in mandated labor implies a national increase in semantic-care load, and
nobody costed it.**

---

# FINDING 8 — 120 DAYS IS THE WRONG TARGET, and this folder already contains the number that says so

**`08` §6.4, sourced:** Nunavut sealift runs late June–late October, with *"remote northern communities
sometimes only getting one delivery a year"* — and its own verdict: *"an interruption horizon of up to 365 days
at a real Arctic settlement, against the trial model's assumed 270 days for Vostok and 330 for Kunlun. The
assumptions were conservative, and the real world is harsher."*

**120 days is under half the assumed horizon for the cities that most need a reserve, and a third of the
empirical one.** For Vostok, Kunlun and Dome Fuji — which `04` §4 says must be *fully* supplied because they
structurally cannot grow — **a 120-day buffer expires mid-winter with no route open.** Simultaneously it is far
too much for Esperanza or Palmer City.

> **A single national number is a category error. The interruption horizon is a per-city physical property set
> by route seasonality and mode — and this model computes per-city physical properties for a living.**

## Two things never specified

- **⚠ What the reserve is MADE of.** Krill *"degrades enzymatically within hours of coming aboard"* and carries
  fluoride in the exoskeleton *(`04` §6.1)*. **A 120-day krill-meal store is not 120 days of food; it is 120
  days of protein with a micronutrient problem.** Stabilization at national scale is a processing industry and
  an energy load, and **it is not among the 22 industries and is nowhere costed.**
- **⚠ "Antarctic cold makes storage free" is doing enormous unexamined work.** Free *outside*. Anything buried
  sits in permafrost or on moving ice — **and Halley's own spec is "the city that moves."** **This project
  already ruled two Ross Ice Shelf sites out over a real 1987 calving event.** Fats oxidize and
  vitamins degrade even at −40 °C, so the reserve needs **perpetual rotation** — a standing forever cost that
  "built once and maintained" denies.

---

# FINDING 9 — WHAT THE PROPOSAL WAS ACTUALLY OPTIMIZING FOR

**Stated objective:** days of national reserve.
**Revealed objective, from the scoring:** *minimize measured disturbance to the largest producer, subject to
filling fastest.* **Both headline numbers were the objective function, and B wins on both by construction —
because the metric was chosen after the shape of the answer was known.**

**And fill time is the least important variable in the problem.** The reserve is a once-built permanent asset.
**3.6 vs 4.5 years is eleven months, once, ever.** *"Optimizing a multi-generational decision on an
eleven-month margin is how you end up concentrating a nation's food supply onto four fishing grounds."*

> ## **The right objective is not "maximize national days-in-store." It is "minimize P(any city runs out)" —
> and those point at different programs entirely.**

**⚠ A framing error worth naming:** a 0.6% surplus is a **flow**; "two days of reserve" is a **stock**. The
conversion implies the nation is two days from famine. **A nation at 100.6% of demand with zero stores is one
bad year from rationing** — serious, but a different problem with different answers.

---

# FINDING 10 — SMALLER ERRORS, ALL LIVE IN FILES MARKED RELIABLE

1. **⛔ `09` §2, {{Abowasa}} Required = 302,329 is WRONG. Correct value 303,329** — off by exactly 1,000, a
   digit error. `504,237×(53×1.54+85.6)/1000 + 1,034,241×(64×1.54+113.2)/1000 = 303,329.4`. **Corrected in
   place, same commit as this file.** No rank change.
2. **The quoted baseline supply "1,180,754" is a misquote of 1,181,031** — it came from multiplying by a
   rounded weighted D of 1.426 rather than the true 1.42629. **This is 3.8% of the surplus it was used to
   compute.**
3. **⛔ Zukelli does not reproduce under the stated rules.** `944,859×0.631×0.25 = 149,051` against a need of
   `627,584×0.053×1.25 = 41,577` gives **+107,474, not +37,917.** Reproducing the published figure requires a
   discount of **0.533** — neither ⅓ nor ⅔ nor 1. **There is an undocumented fourth factor on the supply side.**
4. **⛔ The stated reserve range is not derivable.** 17.5% on 458,881 = +80,304 → **7.37%**, and that only by
   inflating the numerator while freezing the denominator *(adding the workers to production gives 6.90%)*.
   **9.0% is unreachable from 17.5% — it requires a 21.7% uplift. The upper half of the published range has no
   derivation.**
5. **Two different numbers are both called "the requirement"** — 822,291 *(difficulty-free)* and 1,181,031
   *(difficulty-weighted)*, differing by 43.5%, **and the switch is unlabeled.**
6. **Distribution is double-booked or double-dropped.** B1 is "production / processing / **distribution**" and
   D1 Transport & logistics is 19 per 1,000 residents. **Either exporters' haulage labor is being counted as
   exportable production, or 53 is too high.** Unresolved anywhere.
7. **Neumayer's supply side is unsourced.** Its −35,383 implies a credited food sector of 45,937 = exactly 10%
   of its distinctive tier, with **no §15 entry found for it.**
8. **⚠ README's RELIABLE ruling was applied over the files' own hedges.** `09` still carries *"⛔ NOT
   DEPOSITED… Provisional"*; `08` §7.4 still says *"Still provisional"*; `08` §5 item 1 still says *"Until
   ruled, no canon percentage can validate any of this at any city."* **The status stamp did not reconcile
   them.**
9. **⚠ Wrong era for the game.** README records **Casey, Cape Adare, Zukelli and Denison destroyed and Belgrano
   ruined.** Three are food contributors in this ledger — **Zukelli +37,917, Belgrano +25,341, Cape Adare
   +9,824 = ~73,000 heads against a national net of +7,248. The balance is comfortably negative in the era the
   game actually occupies.**
10. **The stacked-vs-spread agriculture decision is still uncanonized** *(`08` §4.5)* **and is worth a factor of
    4+ on the entire food workforce.**

---

---

# ⭐ WHAT SURVIVED — and it is the real output of the pass

**All three checkers agreed on this independently. None of it depends on the disputed arithmetic.**

1. **⭐ THE COALITION FINDING.** Tepenia is fed by a **coalition** of farms and fisheries, not by Davis alone.
   **Davis alone gives an implausible 1-producer-per-51-people.** It follows from the *shape* of the canon §15
   sheets, not from the contested rate.
2. **⭐ THE WEDDELL SEA IS AN UNCLAIMED THIRD FOOD CENTER**, binding the 31% of the national population in the
   Halley subnet. This is new, and it holds.
3. **The population and workforce layer is solid.** Census sums reconcile exactly *(15,623,523 humans;
   32,026,600 residents)*; `robots + 0.5×humans` verifies on all 38 cities with zero mismatches; the `09` §5
   participation-vs-hours resolution is correct reasoning.
4. **The difficulty ladder is genuinely well-founded** — MCAA additive factors, the `1/(1−L)` conversion, the
   60% cap, and independent convergence with the Nunavut cost ladder, with the scope caveat honestly stated.
5. **The selective-application step *(`08` §7.1)* is the model's best idea** — a factor applied to everything
   cancels out of composition, so applying it only to physically-touched industries is what makes difficulty
   **differentiate** rather than merely scale.
6. **The strain metric's denominator choice is right** — `extra workers / non-food distinctive economy` is
   README §2's character budget, so strain reads as **"how much of a city's identity you must delete to eat."**
   **That framing is worth keeping even though the numbers around it were wrong.**

---

# ⭐⭐ THE TWO THINGS WORTH MORE THAN THE RESERVE WAS

## 1. The freedom margin is SPENDABLE — a genuinely new political object

*"The most valuable thing the proposal produced isn't a reserve. It's that scoring it forced someone to notice
the freedom margin is spendable. That is the first time anyone has proposed spending the thing the exile was
for. Whether or not a warehouse gets built, **'the year the Federation asked for hours back'** is better history
than 120 days of krill meal, and it is the piece of this that should reach the culture work."*

## 2. The real-world failure mode, which is better than a collapse story

**CM 51-07 spread the krill trigger across subareas** *(max 25% from 48.1, 45% from 48.2+48.3, 15% from 48.4)*.
**It expired at the end of the 2024 season after members failed to reach consensus for the fourth consecutive
year.** The full 620,000 t then became legally takeable from anywhere in Area 48 — **and the trigger was hit,
closing the fishery early, in 2025 and again in 2026, for the first time in the fishery's history.**

> ## **"The mechanism of failure is not a bad quota. It is a good quota that loses its spatial constraint to a
> political stalemate."**

**A fishery that spent three decades below its brake hit it twice the moment the spatial constraint came off.**

## And a third, for the setting's sense of scale

**Savoca et al. (Nature, 2021): pre-whaling Southern Ocean baleen whales consumed ~430 million tonnes of krill
annually — roughly TWICE the current standing biomass of the entire species.** Krill abundance a century ago
must have been ~5× today's; killing the whales broke the iron-cycling that fed the blooms. **The Southern Ocean
krill stock is not a stable natural baseline a nation can budget against. It is already the depleted remnant of
a system an earlier extractive industry farmed out** — *"drawing on an account someone else already overdrew."*

---

# What was queued as a result

- **DRQ-08** — the B1 food labor rate, which must be sourced **independently of `04` §4**.
- **DRQ-09** — whether §15 food sectors sit **inside or outside** the baseline tier. **One convention, fixed.**

**Until both are ruled, the honest statement is: *the national food balance is not determined to better than
±15%*, and the coalition structure should be reported without the 0.61%.**

---

# Method note — what the three-checker run cost and bought

**Three fresh agents, not forks. None was told the author's conclusion, which variant was favored, or that a
recommendation already existed.** Angles were assigned to be non-overlapping: **ecological feasibility**,
**arithmetic and methodology audit**, **adversarial systems critique.**

**All three returned adverse. Two independently identified the era problem; two independently identified the
labor-vs-capital unit error; the circularity was found by the audit after being flagged in its brief as
"the single most important question."**

> ## ⭐ **The self-audit that preceded them produced four objections, all real — and MISSED every one of the
> findings that actually killed the proposal.** **Self-audit found reasons to hesitate. Independent audit found
> reasons to stop.**

**⚠ The author had cited the "within 1%" agreement to the developer as evidence the canon percentages were
well-set. It was never evidence of anything.** *(Consistent with the standing finding that self-audit error in
this project has run in one direction — toward flattering the pass — on every occasion it has been measured.)*

**Related:** `Canon_Gap_Resolution_Method/05_Bulk_Mode_for_Repeated_Shape_Gaps.md` §B7a *(the protocol)* ·
`Canon_Gap_Resolution_Method/Developer_Ruling_Queue.md` DRQ-08, DRQ-09.
