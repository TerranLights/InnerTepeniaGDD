# Design Efficiency Comparison — Cylinder vs. Wheel at Near-Zero Gravity Gradient

Question: given a "near-zero" perceived head-to-foot gravity difference (<0.5% for a
6'5" / 1.96m person, which requires R ≈ 400m per the gradient formula in the companion
docs), which orbital habitat shape houses the most residents per tonne of material?

## Key Finding: Efficiency Is Radius-Invariant

For both shapes, mass-per-resident turns out to be independent of R, given the model's
core assumption (inherited from the source Grok data) that radiation shielding — the
dominant mass driver in every estimate so far — scales with exposed surface area, not
with rotation rate or radius:

- **Cylinder:** mass/person = shielding rate × (m²/person density). R cancels out
  entirely — floor area and hull area are the *same* surface (2πR × length), so their
  ratio is always 1, regardless of R or length.
- **Wheel (15m slender tube):** mass/person = 2π × r_tube × shielding rate × hub
  overhead. R cancels out here too — hull area (4π²R·r_tube) and floor area
  (2πR × usable width) both scale linearly with R for a fixed tube cross-section, so
  their ratio is fixed purely by tube geometry (tube radius, usable floor width),
  never by R.

**Practical consequence: pushing the radius out to ~400m to make the gravity gradient
imperceptible costs neither design anything in efficiency.** It only means building a
physically bigger structure, not a less efficient one per resident. At 1.49 rpm
(R = 400m, down from ~2.99 rpm at R = 100m — also a more comfortable spin rate as a
free bonus), both the cylinder and the 15m-tube wheel retain exactly the tonnes-per-
person figures already computed at R = 100m.

## Verdict: O'Neill Cylinder Wins, at Any Radius

| | O'Neill Cylinder | Von Braun Wheel (15m tube) |
|---|---|---|
| Floor efficiency (floor ÷ hull) | ~100% | ~21% |
| Hub/spoke structural tax | none | +15% |
| Combined efficiency penalty vs. cylinder | — | ~5.4x worse |
| Population at 16,200t budget, R=100m *or* R≈400m | ~1,000–2,000+ (dense) | ~185–370+ (dense) |

The cylinder wins for two compounding reasons, both shape properties, neither
radius-dependent:

1. **Its entire hull is habitable floor** (people live wrapped around the whole inner
   surface), vs. the wheel's slender rim using only its outward-facing strip — the
   roof, sides, and curvature of a round tube are dead weight, shielded but unused.
2. **It needs no separate hub-and-spoke structure.** A cylinder docks at its
   (relatively simple) endcaps; a wheel's rim is structurally dependent on a hub and
   spokes it must build, and that overhead exists regardless of R.

Scaling a wheel out to a giant ring (the R ≈ 16–32km case explored for reaching
5,000–10,000 residents) does **not** close this gap. It reaches a bigger absolute
population by spending proportionally more total mass, at the *same* (worse)
per-resident rate. Size buys population; for this shape, it never buys efficiency.

**Bottom line: for maximum residents per tonne of material at a near-imperceptible
gravity gradient, the O'Neill Cylinder is the clear winner** — same ~5.4x efficiency
edge over the slender-rim Von Braun Wheel that held at R=100m, unchanged at R≈400m.

## Where a Torus Could Close the Gap (Not Modeled Here)

A "fat torus" that uses its *entire* tube cross-section as multi-deck, wrap-around
floor (Stanford-Torus/Bishop-Ring style, rather than a slender single-deck rim) could
approach — but never beat — the cylinder's efficiency, since at best it converges on
the same "hull = floor" relationship the cylinder already gets for free, while still
carrying the wheel's hub/spoke tax. A flatter, non-circular tube cross-section (e.g.
D-shaped: flat floor + curved outer shielded roof, flat internal walls needing little
shielding) could also narrow the gap, since it stops spending shielding mass on tube
surfaces that aren't usable floor. Neither variant has been modeled in these
calculations; either would need its own pass if pursued.

## Caveat

This model treats shielding — the dominant mass driver in the source data — as purely
a function of exposed surface area, which is physically accurate for radiation
shielding. It ignores that *structural* mass (resisting spin/hoop stress) does
increase somewhat with radius at fixed 1G, since hoop stress scales with R at constant
gravitational acceleration. Because shielding dominates the source estimates, this is
treated as a secondary correction rather than a dominant one — but it means very large
radii (e.g. the 16–32km giant-ring wheel) are mildly more structure-expensive than
this model accounts for.

---
Companion to: `Orbital_Infrastructure_Mass_Budget.md`, `Von_Braun_Wheel_Mass_Budget.md`
