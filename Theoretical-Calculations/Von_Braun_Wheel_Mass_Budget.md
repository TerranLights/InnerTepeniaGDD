# Von Braun Wheel — Mass Budget & Population Calculations

Companion to `Orbital_Infrastructure_Mass_Budget.md`. Same living-condition and gravity
specifications as the O'Neill Cylinder calculation, re-derived for a wheel (torus)
geometry instead. Wheel-specific parameters chosen for this pass: single-deck ~15 m
rim tube, hub + spokes at a +15% mass overhead (midpoint of a requested 10–20% range).

All figures are back-of-envelope, order-of-magnitude estimates — plausibility bounds,
not locked canon.

---

## 0. What Changes Geometrically (and Why It Matters)

- **Cylinder:** the gravity radius *r* IS the habitat's cross-section. The entire
  wrapped inner hull surface is usable floor, and length is a free, independently
  scalable parameter.
- **Wheel:** the gravity radius *R* only sets rotation comfort. The actual habitat is
  a narrower rim tube attached to the hub via spokes. Ring circumference (2πR) is
  fixed the moment R is chosen — it is *not* a free parameter the way cylinder length
  was. Floor area = ring circumference × usable tube floor width, and is capped by
  tube size, not stretchable independently of R.
- **Net effect:** at equal radius, a slender-tube wheel has dramatically less
  habitable floor per tonne of shielding/structure than a cylinder, because most of
  the tube's hull skin (roof, sides, underside curvature) isn't usable flat floor, and
  the wheel's "extra dimension" (tube width) is small by design — it can't be
  stretched to hundreds of meters the way a cylinder's length can.

## 1. Real-World Debris Mass Budget

Unchanged from the companion doc: ~9,000–16,200+ tonnes total mass in Earth orbit,
using the ESA ~16,200-tonne figure as the working ceiling for constrained scenarios.

## 2. Wheel Geometry at the Cylinder's Comfort Radius (R = 100 m)

- Ring circumference: 2πR = **628 m** (same numeral as the cylinder's cross-sectional
  circumference — a coincidence of reusing the same R, not the same geometric role)
- Rim tube: 15 m diameter (per spec), usable flat single-deck floor width ≈ **10 m**
  (accounting for headroom, subfloor, and utilities within a round tube)
- Floor area: 628 m × 10 m ≈ **6,280 m²**
- Full tube hull / outer skin (torus surface area, 4π²R·r_tube): ≈ **29,600 m²**
- **Floor efficiency: ~21%** (floor area ÷ hull area) — compare to the cylinder's
  ~100% (its entire hull *is* floor)
- Practical meaning: for the same amount of shielded/structural hull, the wheel
  yields roughly **1/5 the usable floor** of the cylinder

## 3. Gravity & Rotation Comfort (Unchanged Physics)

Δg/g ≈ h/R depends only on radius-to-floor, not on hull shape, so every gravity
number from the cylinder doc transfers directly:

| Radius | Head-to-foot Δg (6'5" person) | Comfort |
|---|---|---|
| ~100 m | ~2% | acceptable / near-imperceptible |
| ~200 m | ~1% | very comfortable |
| ~400 m+ | <0.5% | truly imperceptible |

At R = 100 m, 1G: rotation ≈ 2–3 rpm — identical Coriolis comfort to the cylinder case.

## 4. Mass-Per-Floor-Area Penalty vs. the Cylinder

- Hull-per-floor-area penalty: **~4.7x** (1 ÷ 21% floor efficiency)
- Hub + spokes overhead (chosen: +15%): additional **×1.15**
- **Combined mass-per-person penalty vs. the cylinder: ~5.4x**

## 5. Population Ceiling Using the Full Debris Budget (~16,200 t, R = 100 m)

Applying the ~5.4x penalty to the cylinder's own mass-constrained population figures:

- **Comfortable population: ~35–150 humans** (cylinder equivalent: 200–800), plus a
  similar-or-larger number of robots, scaled down proportionally
- **Optimistic dense maximum: ~185–370+ humans** (cylinder equivalent: 1,000–2,000+)
- Floor area (6,280 m²) is *not* the binding constraint here — at 10 m²/person it
  could geometrically fit ~628 total inhabitants, but the shielding/structure mass
  budget runs out well before the floor does (the same relationship the cylinder had)

## 6. The 200 Humans + 200 Robots Baseline

- For the cylinder, this was "easily achievable" — 4,000 m² out of tens of thousands
  of m² available.
- For the wheel at R = 100 m: 4,000 m² fits inside the 6,280 m² floor ceiling
  geometrically, but 200 humans sits at the **top of the optimistic-dense mass range**
  (185–370+), not the comfortable range (35–150). What was trivial for the cylinder
  is a stretch case for the wheel.

## 7. Can a Wheel Reach the Cylinder's 5,000–10,000 Person Target?

Not at R = 100 m with a 15 m tube — nowhere close. Keeping the same ~100–200
m²/person spacious density the cylinder doc used for that target (~1–2 million m²
needed), there are two ways to get there:

- **Keep the tube slender (15 m), grow the radius:** ring circumference would need
  to reach ~100,000–200,000 m, meaning **R ≈ 16–32 km**. Gravity/Coriolis would
  actually be *smoother* at that scale (rotation drops to ~0.2 rpm), but this is an
  enormous structure — hull area balloons to ~4.7–9.4 million m², and total mass
  (shielding + structure + atmosphere + contents + hub/spokes) lands around
  **~10–25 million tonnes** — the same order of magnitude as the cylinder's own
  1–10 million ton estimate, just spread across a vastly larger-diameter ring
  instead of a longer tube.
- **Keep the radius near the cylinder's 250–500 m comfort range, fatten the tube
  instead:** required tube width balloons to roughly **320 m–1,270 m**. At that
  point it's no longer a "slender rim" — it's effectively a fat torus, closer to
  Stanford-Torus/Bishop-Ring territory than a classic Von Braun Wheel.

**Bottom line:** the slender single-deck Von Braun Wheel as specified is
architecturally a small-to-mid population design — tens to low hundreds of
comfortable inhabitants at human-scale radii. Reaching cylinder-scale populations
(thousands+) means either ballooning the ring out to tens of kilometers in radius,
or abandoning the "slender tube" concept for a much fatter torus — at which point it
stops behaving like the wheel that was asked for.

## Summary Comparison

| Metric (R = 100 m, 1G) | O'Neill Cylinder | Von Braun Wheel (15 m single-deck) |
|---|---|---|
| Floor area available | 60,000–190,000 m² | ~6,280 m² |
| Floor efficiency (floor ÷ hull) | ~100% | ~21% |
| Comfortable population (16,200 t budget) | 200–800 humans | ~35–150 humans |
| Optimistic dense maximum | 1,000–2,000+ humans | ~185–370+ humans |
| 200H + 200R baseline | Easily achievable | Stretch / optimistic-dense case |
| Mass to reach 5,000–10,000 humans | ~1–10 million tonnes | ~10–25 million tonnes (at R≈16–32 km), or requires a fat-torus redesign |

## Caveats

- All wheel-specific figures inherit the same "back-of-envelope, order-of-magnitude"
  caveat as the cylinder doc.
- Usable floor width (10 m out of a 15 m tube) is a rough assumption for headroom,
  subfloor, and utilities — could shift final numbers ±20–30% without changing the
  qualitative conclusion.
- Hub/spoke overhead (15%) is a placeholder within the requested 10–20% range; real
  designs vary with spoke count and design (elevator shafts vs. static trusses,
  docking hub size, etc.).
- This comparison assumes identical shielding/structure mass rates per m² for both
  designs — real torus-specific structural efficiencies (e.g. self-supporting
  curvature) aren't captured by this rough model.

## Relevance to Open Canon Work

Same as the companion doc: if Inner Tepenia canon ever specifies a Von Braun
Wheel-style station (as opposed to a cylinder) for an orbital location, treat these
numbers as the plausibility ceiling for population at that structure's stated
radius, unless canon separately establishes non-debris material sourcing (lunar/
asteroid mining, etc.).

---
Companion to: `Theoretical-Calculations/Orbital_Infrastructure_Mass_Budget.md`
