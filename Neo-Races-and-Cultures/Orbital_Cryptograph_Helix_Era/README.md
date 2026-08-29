# Orbital Neo-Cultures — Phase 3

**Reserved folder, not yet started.** This is Phase 3 of the Neo-Races and Neo-Cultures project (see
`../README.md`): extending the neo-culture method to the orbital-infrastructure population that carries the
*Cryptograph Helix* timeline forward.

Phase 1c (Cultural Iceberg per-nation entries) is complete for all 35 surface cities. Phase 2 — actually naming
and crystallising each city's neo-culture — is still open. Whether Phase 3 must wait on Phase 2 or can run in
parallel is an open question worth deciding early, since the orbital population's origins trace back to those
same surface cities.

---

## ⚠ The constraint to read before starting

**Orbital settings do not need to be based on real, pre-existing orbital infrastructure — and cannot be.**

The surface cities each have a real-world referent to research at the concrete level: an actual Antarctic
station with a real operating history, real climate data, a real founding nation, real architecture. That is
what `Real-World_Basis_Extrapolation_Method.md` is built on.

**Orbital settlements have no equivalent, and there is no point pretending otherwise.** The only real-world
referent is the **ISS** — a single station, crewed by roughly seven people at a time, on rotations of months,
never multi-generational, with no children ever born aboard, no economy, no elders, no funerals, no politics
beyond mission scheduling. It is not a society. It is a workplace with a crew roster.

**No multi-generational orbital population has ever existed.** So there is nothing to mine, and the absence is
not a gap in our research — it is a fact about the world.

### What replaces the real-world basis

The developer's own framing (2026-08-24). The derivation needs three things:

1. **Who lives there** — the population itself.
2. **What sort of culture — more precisely, and more in-universe-consistently, what sort of "neo-culture"** —
   they have.
3. **How such a people would live, operate, function, and build their lives in what is effectively a closed
   environment**, with only minimal physical commuting, travel, and transportation between separate orbital
   infrastructure locations.

From those three, derive, extrapolate, and synthesise the **localized orbital neo-cultures** — plural and
mutually distinct, not one undifferentiated "orbital culture."

**The closed-environment constraint set is itself the generative input.** It does the job real-world comparanda
do for a surface city: a population, plus a specific set of conditions, run forward over generations, produces
a distinct people. That is the logic this whole project already runs on. Only the source of the conditions
changes.

**The minimal-travel constraint is a generative asset, not a hardship to describe.** It is precisely what would
cause separate orbital locations' neo-cultures to diverge from one another, which is what makes them *plural*.

---

## The trap specific to this setting

**Do not reach for generic "isolated closed environment" texture.** Tepenia's entire premise is already
Antarctic isolation — a hostile outside, engineered warmth, enclosure, scarcity, interdependence. If the
orbital neo-cultures are built from the same palette, they will read as Tepenia in a different box, and the
whole point of Phase 3 is lost.

The orbital case has to differ from the Tepenian surface case **specifically**, and the differences are real:

- **Tepenia has an outside.** It is lethal, but it exists — ground, weather, sky, horizon, a direction called
  "out there." Orbital settlements have no outside in that sense at all.
- **Tepenia has roads.** Highways connect its cities; hitchhiking is an established, ordinary way to travel
  between them. Movement between orbital locations is not a road trip — it is scheduled, expensive, physically
  demanding, and constrained by orbital mechanics rather than by weather or distance.
- **Gravity is a variable, not a constant.** Established canon already turns on this: a character fled to the
  low-earth orbital society specifically because lower gravity eased the physical pain of an illness (see the
  TCY-45 seed in `Worldspace/Characters/Dolls/Methodology/00e_Quick_Capture_Seed_Batch_Input_[rewritable].txt`).
  So at least part of the orbital population is there for **medical** reasons, which is a founding pressure no
  surface city has.
- **Orbital society is a knowledge recipient.** Also established canon: STP-06's entire life's work is
  developing more material-efficient farming and harvesting methods and **transmitting the schematics upward**,
  so that space-dwelling Tepenians can better provide for themselves (see her `README.md`). That implies an
  orbital population dependent on surface expertise, and a surface population that knows it. That relationship
  is a culture-shaping pressure in both directions.

---

## Method files that carry over unchanged

These are derivation engines, not real-world-research tools, so the absence of an orbital analog does not
affect them:

- `../_Method/Cultural_Iceberg_Method.md` — Hall's surface/deep-culture sorting. A sorting framework; it works
  regardless of where the raw material came from.
- `../_Method/Human_Universals_Culture_Framework.md` — Brown's universals as a believability floor and a
  question-generator.
- `Outside-World/.../Local_Robot_Culture_Methodology/` — the robot counterpart: what culture a robot population
  would naturally arrive at given its environment and pressures. Directly applicable, and arguably *more*
  important here than on the surface, given the orbital population's likely composition.

## The bar to meet

Per `../README.md`: a genuine new people — *"a real, new 'third thing,' culturally distinct from any of the
origin populations that fed into it,"* the way Taiwanese, Singaporean, Québécois, and Afrikaner are real
distinct peoples rather than variant flavors of a parent nationality. The developer's surface worked example is
a *"Zhongshanese"* people. Orbital neo-cultures meet the same bar.

## Hard dependency

**Input 1 — "who lives there" — is not yet answered.** Orbital population composition is its own unstarted,
deliberately-reserved high-token task (`project_orbital_composition` in project memory). The methodology can be
built without it; an actual orbital neo-culture pass cannot run without it.
