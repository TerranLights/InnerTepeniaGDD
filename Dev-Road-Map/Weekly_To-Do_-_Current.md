# Weekly To-Do — Current

**Started 2026-07-23.** A short working shortlist pulled from the much larger `TODO.md` backlog — items the
developer wants to actually work through over the next several days. Each entry below cross-references its
full write-up in `TODO.md` for context; this file is the queue, not a replacement for the fuller entries.
When an item here is finished, resolve it in `TODO.md`/`DONE.md` as usual and strike it here (or clear the
file and start a fresh one for the next stretch of work).

---

## High Priority

- [ ] **Calethina's questline ("Echoes of the Bridge") — further structure**
  Scope explicitly requested: general, non-detailed beat form — the "Major Steps/Acts" level of structure
  other questlines already have (e.g. Ayako's or Favi's `Personal_Questline_Summary.md` files), not a full
  beat-by-beat design pass. Full `TODO.md` entry has what's already established (archive-narrator direction,
  Ji-Eun Kim first thread, mid-game download option, Bridge Unit definition, Ghost Protocol connection to
  develop).

---

## Medium Priority

- [ ] **Tentative Factions — design all 9 (including sub-factions)**
  FD-3 Veilkeepers, FD-4 Lattice/Bonded Lattice, FD-6 Reclaimers, FD-7 The Vigil (pending keep/redesign/cut
  decision), FD-8 Siligel Purists, FD-9 Neon Nomads, FD-10 Chorus of the Deep, FD-11 Memory Weavers, FD-12
  Iron Gardeners. See `Storyline/Endings/Secret-Endings/Faction_Devotion_Endings.md`.

- [ ] **National Holidays — various kinds**
  `Worldspace/National_Holidays.md` has 4 categories scaffolded (Civic/National, Persisted Aesthetic,
  Internationally-Transcendent, Celestial/Faction-Specific). Category 4 is the least resolved and has its
  own flagged dedicated-investigation need (which faction(s), what astronomical event, Kunlun-centered or
  not) — but scope for this pass is left open per the developer's own phrasing, not narrowed to Category 4
  alone.

- [ ] **Ghost Protocol — what is it, how does it work, backstory**
  Named/documented in `Worldspace/Energy_Grid_Failure_Rationale.md` (reason #9): emergency AI protocols
  embedded into the Power Core during the Long Night War evacuation to prevent total collapse, now deeply
  entangled with core systems — removing/overriding them risks a built-in scorched-earth shutdown. Calethina
  may have been the one who embedded them (a life-saving measure that's been quietly strangling the city for
  a decade-plus since). Not yet designed as an actual in-game obstacle or quest mechanic.

**Housekeeping done alongside this list, 2026-07-23:** Juan Carlos's post-Long-Night-War status — already
resolved in-session (Destroyed, targeted for its archive/customs function) but still sitting as an open
checkbox in `TODO.md` — has been moved to `DONE.md`.

---

## Long-Term Priority

- [x] **Throwing weapon mechanics — blades first — universal retrieval principle written 2026-07-23**
  Cross-project standing law (Inner Tepenia + all 3 Outer Tepenia trilogy titles) written to
  `Game-Mechanics/Combat/Throwing_Weapons.md`: a thrown blade stays where it lands until manually retrieved,
  in every game, regardless of engine. Inner Tepenia gates the throw itself by range/stat checks before the
  action is legal; Outer Tepenia's open world needs a separate range-of-reach concept plus a
  miss-only auto-return exception for iconic weapons. Four stat-mapping dimensions (range, accuracy, crit
  chance, crit damage) remain open per `TODO.md`'s own entry — not blocking, tracked there.

- [ ] **Re-number the DLCs by release order — narrowed to 2 candidate orders, 2026-07-23, decision deferred**
  Both written into `Storyline/DLC_Overview.md`'s "Release Order vs. DLC Numbering" section. South Pole
  (DLC 1) confirmed last either way; release order and development order are explicitly decoupled, so neither
  candidate is blocked by the 4 subnet DLCs still lacking a real main-questline anchor.
  - **"Geometric"** — traces the continent's coastline in one rotational sweep from Concordia's own Janbogo
    subnet, nearly closing the loop before diving inward to the South Pole (the continent's actual center):
    Janbogo → Mirny → Mawson → Halley → Palmer → Byrd → South Pole.
  - **"Thematic"** — an emotional arc built from each subnet's confirmed meta-personality read (wound →
    response → destabilization → isolation → purpose → verdict, the verdict echoing the opening wound):
    Palmer → Halley → Mawson → Byrd → Mirny → Janbogo → South Pole.
  **Open:** which one actually becomes the release order — a spatial story vs. an emotional one, not both at
  once. Developer's own lean is toward Thematic, open to Geometric; deliberately not decided yet.

- [ ] **Amundsen Time Code (ATC) — geographic rationale finalized 2026-07-23, implementation still open**
  ATC is logically derived from EST's geographical stretch, exactly as UTC is derived from GMT's. Three
  finalized reasons, per `TODO.md`: (1) EST is the single longest-spanning real-world time zone (its
  farthest-north land is the world's farthest-north land, barring Greenland's tip); (2) EST contains New
  York City, one of history's largest and most ethnically/linguistically diverse settlements; (3) EST is
  *adjacent to* (not encompassing) the Antarctic Peninsula — the closest real-world time zone to Palmer
  City, Tepenia's first-settled ground. Named for Amundsen Station, the South Pole's geographically
  "centerless" neutral relay. Still open: in-game display, whether the Planetary Split Brain disrupted
  timekeeping consistency across subnets, and how ATC relates to polar night/midnight sun.

