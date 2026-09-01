# Burden Model — Test Log

**Accumulating log of validation runs against the burden scoring model (`01_Burden_Scoring_Model.md`).**
**Append-only. One section per test. Nothing here is deposited into any city's own files.**

**Basis: CENSUS I throughout** (developer ruling, 2026-09-01 — see `06_Census_Basis_Correction.md`).
**Period: Second Interwar.**

---

# Comparison table — all runs to date

| # | City | Test purpose | BaselineLoad | Verdict |
|---|---|---|--:|---|
| 1–5 | Vostok · Kunlun · Cape Adare · Casey · {{Abowasa}} | pilot; extremes + necessity function | 71 / 75 / 44 / 40 / 53 | ✅ **PASS** — 35-pt spread, Kunlun structurally distinct |
| **6** | **Denison** | **the fat middle + a known-value check** | **49%** | ⚠ **SPLIT — envelope passes, composition FAILS** |

---

# TEST 6 — DENISON — 2026-09-01

## Why this city

**Two things were being tested at once:**

1. **The fat middle.** The pilot validated both extremes and nothing between — Casey, chosen as the
   "deliberately ordinary" city, landed at the *floor*. **This is the first genuine mid-pack test.**
2. **⭐ A known-value check.** Denison's §15 already carries **`Structural/wind engineering: ~25%`**. **The
   model's output can be compared against an existing canon number it was not told about.** *(Declared in
   advance: if the instrument cannot reproduce that sector from its drivers, the instrument is wrong.)*

## Inputs — all already-canon

**Census I: 522,975 humans / 543,168 robots = 1,066,143.** Robot share **50.9%.**
**Workforce = 543,168 robots + 261,488 humans (50%) = 804,656.**

| Driver | Value | Source |
|---|---|---|
| **Wind** | **~80 km/h average (22.2 m/s); gusts recorded well over 300 km/h** | *"among the most severe wind regimes at any permanently inhabited sea-level site on Earth"* |
| Cold | ~−11 °C — **mild** | *"defined overwhelmingly by katabatic wind severity rather than temperature extremity"* |
| Altitude | sea level | Cape Denison, Commonwealth Bay |
| Coastal | coastal | 67°00'S, 142°40'E |
| Polar night | ~none (67°S, barely inside the Circle) | |
| Isolation | on **Hwy 183**, between the Cape Adare road and Dumont d'Urville | reasonably connected |

## The wind driver had to be re-scaled before the run — recorded as an instrument change

**The pilot's wind scale ran 1.0 (calm) → 1.6 (katabatic), with Casey topping out at 1.45 for 7–10 m/s.**
**Denison is 22.2 m/s — 2.6× Casey's speed.** The old scale had no room for it.

> **⚠ And wind LOAD is not linear in wind speed. Force ∝ v².** Denison against Casey is **2.6× the speed but
> ~6.8× the pressure.** **A linear wind driver structurally cannot represent this**, which is a defect in the
> pilot's model that this test exposed.

**Re-scaled to `wind = 4.0` for Denison** — a dampened v²-based figure, since maintenance cost scales
sub-linearly with design load rather than tracking pressure directly. **Recorded as an instrument change made
during a test, not silently absorbed.**

## Result

**Burden index** = isolation 1.1 × mean(cold 1.04, alt 1.0, **wind 4.0**, coastal 0.7, p-night 1.02,
enclosure 1.3) = 1.1 × 1.51 = **1.661** → **BaselineLoad 53.6%**

| Industry | Denison |
|---|--:|
| A1 Thermal & power | 7.7 |
| A2 Water & sanitation | 4.4 |
| A3 Enclosure & atmosphere | 5.9 |
| **A4 Construction & structural maintenance** | **14.2** |
| B1 Food production | 1.8 |
| B2 Human healthcare | 1.7 |
| B3 Robot maintenance + coolant | 5.5 |
| C1 Education & training | 1.7 |
| C3 Administration & records | 5.1 |
| C4 Materials recovery | 2.5 |
| D1 Transport & logistics | 3.2 |
| **BASELINE CIVIC LOAD** | **53.6%** |

---

# ⚠ VERDICT — SPLIT. One test passes, one fails.

## ✅ PASS — the fat-middle test

**Denison lands at 53.6%, between Cape Adare (44%) and {{Abowasa}} (53%), well inside the envelope and nowhere
near either extreme. The instrument does not break in the middle.** **The pilot's largest recorded weakness is
now closed.**

## ❌ FAIL — the known-value test

> ## **Model: A4 = 14.2%. Canon: `Structural/wind engineering: ~25%`. Off by a factor of ~1.8.**
>
> **At the pilot's original linear wind scale it was worse — 10.8%, off by 2.3×.**

**The instrument cannot reach 25% from its drivers.** To do so, wind would need a multiplier around **8**,
which is not defensible as a maintenance-cost figure at any wind speed.

## Two candidate causes — and I believe both contribute

**1. The wind driver was genuinely too weak, and still may be.** The pilot's 1.0–1.6 linear scale could not
represent a 6.8× pressure differential. **This is a real defect the test found, and the re-scale to 4.0 is a
partial fix, not a proven one.**

**2. ⭐ Canon's 25% is probably not a pure baseline sector.** *"Structural/wind engineering"* likely bundles
**two different things**: maintaining Denison's own structures *(baseline — which the model computes at
~14%)*, and **wind-engineering expertise as an exportable specialization** *(distinctive — the remaining
~11%)*. **Every Antarctic city fights wind; the city that fights it hardest would become the national
authority on it** — the "extremity → laboratory" pattern applied to an ordinary industry rather than a strange
one.

> ### ⚠⚠ SELF-AUDIT WARNING, recorded deliberately.
> **I predicted this test would fail, it failed, and I then produced an explanation for why the failure is
> acceptable.** **That is precisely the self-flattering direction this project has measured its own audit
> error running in, on every occasion it has been measured.** Cause 2 is a *hypothesis*, not a finding. **It
> should not be adopted until it is tested against a city where the same industry has no plausible export
> story** — and if no such test can be devised, it should be treated as unproven rather than accepted by
> default.

---

# What this test changes

1. **⚠ `01_Burden_Scoring_Model.md` §5's wind driver must be rewritten as non-linear.** The 1.0–1.6 linear
   scale is a confirmed defect. **Not yet applied to the model file** — it would invalidate the pilot's five
   published figures, and those should be re-run together rather than piecemeal.
2. **⭐ Denison is a candidate for PROMOTION to provider** — wind/structural engineering — which would move it
   out of `05`'s remaining-15 list. **Contingent on cause 2 being tested, not assumed.**
3. **The pilot's Casey wind value (1.45) is now suspect**, since it anchored a scale that has been shown
   inadequate at the top end.

# Open

- **Re-run the five pilot cities on the non-linear wind driver** before any countrywide pass.
- **Devise a discriminating test for cause 2** — a city with a high baseline-industry share and no export
  story. *(Candidate: Halley's construction share, once the foundation-stability driver exists — a city that
  moves has enormous baseline construction and nothing obvious to sell.)*

---

# TEST 7 — TWO-AGENT VALIDATION — 2026-09-01

**First use of the two-agent protocol** (`Canon_Gap_Resolution_Method/05_Bulk_Mode…` §B7a). Two fresh agents,
neither a fork, neither told the author's expectations or prior results. **Agent A** independently re-derived
the model across six cities. **Agent B** adversarially adjudicated the Test 6 gap.

## ⛔ RESULT: the model FAILED far more broadly than Test 6 suggested, and Test 6 itself was invalid.

### A. Test 6's "known-value check" was an invalid instrument — Agent B

**Canon §15 sheets partition the *visible* economy; the model partitions the *whole* economy.** Denison's
sheet names no thermal, water, food, healthcare, robot maintenance, admin or transport — **the 2026-08-31
sweep already recorded utilities absent from 36 of 36 cities** — and `TODO.md` had already stated the
consequence: ***"percentages must be rebalanced, not inflated… adding sectors means taking share from existing
ones."***

**Rescaled: model A4 14.2 ÷ visible economy 62.2 = 22.8%, against canon's ~25%. Residual 2–5 points on a
tilde figure. The "factor of 1.8" measured nothing.**

> **⚠ There are now TWO undefined terms in §15, not one.** `01` §5.1 already flagged *in-city vs. resident
> labor* — which diverges at one city. **This second one — the coverage denominator — diverges at all
> thirty-six.** **Until it is defined by ruling, no canon §15 percentage can confirm or falsify this model at
> any city.**

### B. ❌ The export hypothesis is REJECTED ON EVIDENCE, not merely untested — Agent B

**Searched for the economic basis and found none.** The only export text sits in **§25, which the template
defines as *cultural*** *("goods, ideas, art, people")*. Vignette evidence is **hobby-scale correspondence**,
and **Denison is often the recipient** — it sent a wind question to Mirny's Windwright Guildhall and credited
*"the successful expansion directly to the outside consultation."* **A city that imports second opinions on
its own defining problem is not running an export consultancy.** Construction is in this project's own
**non-outsourceable** column. At 11 points that would be ~88,500 workers — ~2,500 permanent consultants per
client city.

**Also: the 25% was never derived.** It entered in a seven-city batch commit; the **25/20/20/15 shape recurs
verbatim** at Halley, Princess Elisabeth and Zukelli; and **Dumont d'Urville, same wind regime, files identical
wind work under a generic 25% "Technical/scientific" slot.** *The number tracks the template, not the weather.*

**Disposition: cause 2 marked REJECTED. Denison's promotion to provider does NOT proceed** — it rested
entirely on this.

### C. The independent re-derivation — Agent A

**Wind driver, independently constructed:** `B = 1 + k·[(v/v₀)^1.3 − 1]`, anchored to the spec's *own*
endpoints (1.0 at 4 m/s; 1.6 at an ordinary 12 m/s katabatic city) and **unbounded above.** Denison → **2.567**.
**Unprompted convergence check: it returns 1.097 for Vostok against the spec's hand-figure of "~1.1."**

| City | Author's pilot | **Agent A** | Δ |
|---|--:|--:|--:|
| Vostok | 71% | **69.7%** | −1.3 |
| Kunlun | 75% | **68.5%** | **−6.5** |
| Cape Adare | 44% | **48.0%** | +4.0 |
| Casey | 40% | **43.4%** | +3.4 |
| {{Abowasa}} | 53% | **71.3%** | **+18.3** |
| Denison | — | **55.2%** | — |

- **⭐ Kunlun no longer tops the table.** It loses on *necessity* — B2 → 0, B1 → 0.10 strips ~22 weighted
  units, more than its driver advantage recovers. **The extreme end of the envelope is unreachable by the very
  cities nominated for it.**
- **⭐ Denison's canon identity DID emerge unprompted.** It is **the only city in the set where A1 Thermal is
  not the largest line** — A4 + A3 = **23.8%**, nearly 4× thermal. *"The model reproduced a canon fact it was
  not given."* Under the old linear clamp it would have been 17.2% and merely visible. **The wind revision is
  vindicated even though the numeric test was void.**

## ⛔ D. Seven structural defects in the model, found by Agent A

1. **⭐ THE ENVELOPE MAP IS NOT DEFINED AT ALL.** `01` §2 says "envelope-mapped sum of Raw" and never
   specifies the function. **Same formula, same drivers, same data: ~17 pp of headline swing** (Vostok 84.7%
   vs 69.7%) purely from the undefined choice. **Every figure this pass has published is contingent on a
   function the spec never wrote.**
2. **⭐ ISOLATION CANNOT DO WHAT `01` §5 CLAIMS.** Because it multiplies *every* industry equally, **it
   factors out of `Raw/ΣRaw` entirely.** **It moves the headline and cannot touch a single row.** The driver
   the model names as its primary differentiator **is structurally incapable of shaping any city's §15.** Wind,
   Cold and Coastal do all the real work.
3. **Multiplied drivers compound geometrically with nothing resisting it.** A1 at Vostok = 1.90 × 2.00 × 1.50
   × 1.28 = **7.28**, against a declared B range of "~0.7 → 2.0+." **The spine is multiplicative; the
   calibration language is additive; the two were never reconciled.**
4. **Building stock age is a driver that does nothing** — no multiplier, cannot enter a multiplicative
   formula. It belongs in the differentiation table, not the driver table.
5. **No economic-role driver.** Casey is the origin of Hwy 2 and a Hwy 110 waypoint, yet **being coastal
   *reduces* its transport line to 0.75.** The model treats logistics purely as import cost, never as
   throughput.
6. **⭐ Healthcare's §A inversion never reached the arithmetic.** The register argues at length that Tepenian
   healthcare must run *above* norms — then **B2's weight stayed at 10 while C3's was explicitly revised to 14
   on research grounds.** *"The same research pass corrected one weight and not the other."*
7. **The falsification test is weaker than it looks.** The ≥25 pp spread clears at 27.9 — **but only because
   {{Abowasa}}'s externalization adds 15.9 pp**, and that parameter is the least specified number in the
   model. **The spread test is near-guaranteed to pass for any monotone map: it measures the map's slope, not
   the instrument's validity.** *(The Kunlun row-set condition is the genuinely informative half, and it
   passes on its own merits.)*

## E. `01` §5's central claim is false

> *"Every driver below is already canon for every city… **Zero new research is needed** to compute all 36
> baselines."*

**False for two of six pilot cities on the wind driver alone.** Cape Adare and {{Abowasa}} state no wind
speed; Denison states **no mean annual temperature and no polar-night count.** **"If two of six pilot cities
have gaps, the 36-city run should expect roughly a dozen."**

**And `00_Necessary_Industries_Register.md` §4 contradicts itself on Kunlun's B3** — the table says N ≈ 1.0,
the prose two lines below says robot maintenance "expands into the space." **Both cannot hold**; at N = 1.0
Kunlun's row set is merely smaller, which the same box calls the failure mode.

---

# ⛔ STANDING CONCLUSION

**The burden model is NOT ready for a countrywide pass.** Defects 1, 2 and 6 are structural, not calibration.
**No figure from `03_Pilot_Run` should be treated as current**, and nothing may be deposited into any city
file until the envelope map is defined, isolation's role is reconciled with what it can actually do, and the
§15 coverage denominator is ruled on.

## ⭐ Protocol note — first use, and it worked

**The two-agent protocol found, in one run, more real defects than the author's own testing had found across
the entire pass** — including a rejected hypothesis the author had proposed and a claim about isolation the
author had written into the spec and repeated. **Both catches were inconvenient for the author.** *(One run is
not validation; recorded as the first data point against the bar in memory.)*
