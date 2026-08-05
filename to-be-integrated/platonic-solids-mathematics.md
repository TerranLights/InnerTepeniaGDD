# The Five Platonic Solids — Mathematical and Geometric Properties

**What this is:** a reference layer for the flagged "original Platonic Solid symbol system" project (`TODO.md`), alongside the existing `platonic-solids-chemistry.md` reference. That file covers coordination geometry; this one covers the solids' own mathematical structure — both properties particular to each individual solid, and properties that only emerge from how the five relate to each other (duality, symmetry groups, space-filling, stellations). The relational layer is likely the more useful one for an orbital-nesting design, since Kepler's own *Mysterium Cosmographicum* was fundamentally about relationships between solids, not standalone per-solid traits.

---

## Per-Solid Properties

### Tetrahedron (4 faces, 4 vertices, 6 edges)
- The only Platonic solid that is **self-dual** — its dual polyhedron is itself. Every other solid pairs with a different one.
- Smallest dihedral angle of the five (~70.53°) — the "sharpest," least sphere-like shape.
- Simplest possible closed 3D shape — the minimum number of faces (4) any polyhedron can have at all.
- Vertex coordinates are rational/simple — no irrational constants needed to construct it exactly.
- Has zero stellations — nothing new emerges from extending its faces.

### Cube (6 faces, 8 vertices, 12 edges)
- The **only** Platonic solid that can tile 3D space by itself (fills space with no gaps, no partner shape needed) — none of the other four can do this alone.
- Dihedral angle is exactly 90° — the only one of the five with a "clean," rational angle.
- Dual of the octahedron.
- Rational coordinates, like the tetrahedron.
- Zero stellations, like the tetrahedron.

### Octahedron (8 faces, 6 vertices, 12 edges)
- Dual of the cube.
- Dihedral angle ~109.47° — notably identical to the tetrahedral bond angle in chemistry (sp³ hybridization), a real coincidence connecting two different solids' chemistry associations (see `platonic-solids-chemistry.md`'s Tetrahedron and Octahedron entries).
- Has exactly **one** stellation: the *stella octangula*, a compound of two interpenetrating tetrahedra — the octahedron sits at the intersection when two tetrahedra overlap.
- Paired with the tetrahedron, the two can jointly tile space (the tetrahedral-octahedral honeycomb) even though neither can do it alone — a genuinely relational property, not something either shape has by itself.
- Rational coordinates.

### Dodecahedron (12 faces, 20 vertices, 30 edges)
- Dual of the icosahedron.
- Its geometry is intrinsically built from the **golden ratio (φ)** — its vertex coordinates cannot be constructed without it. A real structural break from the tetrahedron/cube/octahedron trio above, which need no irrational constants at all.
- **Cannot tile space**, alone or with a partner — 5-fold symmetry is mathematically forbidden from periodic tiling (the crystallographic restriction theorem). Structurally an "outsider" among 3D space-filling shapes.
- Has 3 stellations.
- Plato's own *Timaeus* set the dodecahedron apart from the other four — the other four were mapped to earth/water/air/fire, while the dodecahedron alone was reserved for "the cosmos as a whole," a categorically different role from the start.

### Icosahedron (20 faces, 12 vertices, 30 edges)
- Dual of the dodecahedron.
- Also built from the golden ratio, like the dodecahedron.
- The **most sphere-like** of the five — for a given surface area, it encloses more volume than any other Platonic solid (the closest approximation to a sphere among the five). Ranked by that "efficiency": icosahedron > dodecahedron > octahedron > cube > tetrahedron.
- Has a strikingly large number of stellations: **59**, versus 0-3 for every other solid — a genuinely singular outlier.
- Same "cannot tile space" restriction as the dodecahedron.
- Real-world icosahedral quasicrystals exhibit true 5-fold symmetry that never repeats periodically — "impossible" long-range order without translational repetition (the same real-world basis `platonic-solids-chemistry.md`'s Icosahedron entry draws on for viral capsids/fullerenes).

---

## Relational / Structural Properties Across the Set

- **Duality pairs**: Cube↔Octahedron, Dodecahedron↔Icosahedron, Tetrahedron↔itself. A natural 2-2-1 grouping rather than five independent shapes.
- **The rational/golden-ratio split**: {Tetrahedron, Cube, Octahedron} need no irrational constants to construct; {Dodecahedron, Icosahedron} are inseparable from φ. Arguably the sharpest dividing line in the whole set — a "3 discrete/rational" vs. "2 continuous/irrational" structure.
- **Symmetry group sizes**: Tetrahedron's rotational symmetry group has order 12; Cube/Octahedron share order 24; Dodecahedron/Icosahedron share order 60. The duality pairs literally share identical symmetry groups — geometrically, a dual pair *is* one underlying symmetry wearing two different faces.
- **Space-filling hierarchy**: Cube alone → Tetrahedron+Octahedron jointly → Dodecahedron/Icosahedron never. A three-tier ordering by "ability to fill space," which could map cleanly onto an orbital-nesting logic (solid, joint, and structurally excluded).
- **Stellation counts**: 0, 0, 1, 3, 59 — an escalating, wildly non-linear sequence that's interesting as a progression on its own.

---

## Not Yet Used Here

Not folded into either list above, but worth keeping in reserve: Euler's formula (V − E + F = 2, holds for all five identically, so it's not a differentiator); Schläfli symbols ({3,3}, {4,3}, {3,4}, {5,3}, {3,5} — a compact notation for the same face/vertex data already covered); vertex configurations (3.3.3, 4.4.4, 3.3.3.3, 5.5.5, 3.3.3.3.3); insphere/circumsphere ratio as a separate "compactness" measure distinct from the sphericity ranking above; and Descartes' theorem on angular defect (total angular defect across all vertices of any convex polyhedron always sums to 720°) — the underlying reason only five Platonic solids can exist at all.
