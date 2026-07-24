# Weekly To-Do — Current

**Started 2026-07-23.** A short working shortlist pulled from the much larger `TODO.md` backlog — items the
developer wants to actually work through over the next several days. Each entry below cross-references its
full write-up in `TODO.md` for context; this file is the queue, not a replacement for the fuller entries.
When an item here is finished, resolve it in `TODO.md`/`DONE.md` as usual and strike it here (or clear the
file and start a fresh one for the next stretch of work).

---

## High Priority

- [ ] **District Main vs. Under-Questline candidates — generate more**
  Structure and both governing files (`District_Main_Questlines.md`, `District_Under_Questline_Design_Method.md`)
  are established; each district currently has only its *first* main-questline candidate. Main questlines:
  generate several candidates per district using the existing Internal-Conflict format, then narrow to
  exactly one. Under-Questlines: generate a floor of 5 (ideally 15-20) per district, anchored to a
  "significant starting point" (a named figure or a data-point at a significant location) — and, unlike main
  questlines, **keep all of them**, no narrowing. See `project_district_questline_production_workflow`
  memory for the full workflow.

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

- [ ] **Doll Enneagram gaps — review pass**
  Four characters missing a type entirely: Maria (FR-03), Momo (TCY-45), Eirwyn Cardoss (Off-World template
  has no Enneagram field), and **Calethina** — flagged in the original TODO entry as "no standard README,"
  which is now stale (she has a full master `README.md` as of this session) but she still has no formally
  assigned Enneagram type, so worth confirming whether that's still a real gap or already implicitly
  answered by everything now written about her. Two missing a subvariant: Charlene (XT-17, 5w4) and Angelina
  (XT-21, 7w8). Broader pass: confirm existing subvariant assignments are correct across all typed dolls
  before Phase 3 personality work begins. Don't design companion perks, attraction profiles, or romance
  gates for the type-missing characters until this is resolved.

**Housekeeping done alongside this list, 2026-07-23:** Juan Carlos's post-Long-Night-War status — already
resolved in-session (Destroyed, targeted for its archive/customs function) but still sitting as an open
checkbox in `TODO.md` — has been moved to `DONE.md`.

---

## Long-Term Priority

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

