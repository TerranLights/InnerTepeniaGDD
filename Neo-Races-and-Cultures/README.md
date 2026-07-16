# Neo-Races and Neo-Cultures — Project Scaffold

**Status:** scaffolding only, established 2026-07-16. This is a genuinely enormous, multi-phase
research and synthesis project — not something to be completed in any single session. This folder
exists so the work has a real home to be filled into gradually, over time, rather than being
re-derived from scratch each time it's picked back up.

---

## What this project actually is

For each Tepenian city (and eventually the orbital infrastructure population that appears later in
the *Cryptograph Helix* novel timeline), the goal is to eventually synthesize a genuine **neo-race** —
a new, localized people with its own real, internally coherent culture, analogous to how real-world
history has repeatedly produced genuinely new peoples out of a specific ethnic/national starting
population settling into a specific new place for generations: Taiwanese, Singaporean, Québécois,
Afrikaner. Not a variant flavor of an existing nationality — a real, new "third thing," culturally
distinct from any of the origin populations that fed into it.

**Worked example, given directly by the developer:** a "Zhongshanese" people, culturally distinct from
mainland Chinese culture, arising from Zhongshan's own multi-generational Chinese-founded population
settling into its own specific Tepenian conditions — the same shape as how "Taiwanese" is a real,
distinct people and culture today, not simply "Chinese people who live somewhere else."

---

## The three phases

### Phase 1 — Cataloging (the phase this scaffold is built for)
For each city, for each nationality/ethnicity present in meaningful proportion:
1. **Population data** — nationality and percentage proportions. Mostly already-established data;
   see `Official_Population_Census.md` and each city's own `Specs/[City].md` for the authoritative
   figures. This phase is about pulling that data into this project's own per-city working files, not
   re-deriving it.
2. **Geography and geology** — each city's own physical surroundings and geological composition.
   Also mostly already-established; see each city's own `Specs/[City].md` Geographic Basis section.
3. **Real-world parallels** — actual, real-world instances of people of comparable
   race/ethnicity/nationality living in geographically/geologically comparable conditions elsewhere in
   the real world (obviously much less cold and much less windy than Antarctica — the comparison is
   about terrain and geology, not climate). This is the genuinely new research this project requires.
4. **Cultural Iceberg sorting** — using Edward T. Hall's 1976 Cultural Iceberg model (see
   `_Method/Cultural_Iceberg_Method.md`) to sort what's found about each real-world parallel community
   into surface-culture and deep-culture findings, rather than stopping at surface-level detail (food,
   festivals, flags) the way most comparative-culture work does by default.

### Phase 2 — Synthesis (later, once Phase 1 has real material to draw from)
Using the cataloged real-world comparanda, actually synthesize each city's own neo-race and
neo-culture — a new people with its own values, social structures, communication norms, and yes,
eventually its own slang (see the separate, already-scoped slang-synthesis project, reserved for
similar reasons).

### Phase 3 — Orbital extension (later still)
Once the surface-city neo-races are established, extend the same method to the orbital infrastructure
population that carries the *Cryptograph Helix* timeline forward — see `Orbital_Cryptograph_Helix_Era/`,
currently an empty reserved folder.

---

## Folder structure

- `_Method/` — the Cultural Iceberg framework itself, the per-city cataloging template, and the
  progress tracker.
- `[Subnet]/[City]/` — one folder per city (mirroring the existing `City_Megasheets/` subnet
  structure), currently empty, ready to be filled in per the template as each city's cataloging work
  actually happens.
- `Concordia/` — reserved; Concordia's own population is drawn from every other city rather than
  having its own separate founding-nation composition, so its own treatment here may need to work
  differently from the other city folders once this is picked up.
- `Amundsen_Station/` — reserved.
- `Orbital_Cryptograph_Helix_Era/` — reserved for Phase 3.

## Status

Nothing has been filled in yet. See `_Method/Progress_Tracker.md` for the full 35-city + Concordia +
Amundsen Station checklist, currently all unstarted.
