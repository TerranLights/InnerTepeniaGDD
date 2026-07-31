# Weekly To-Do — Current

**Started 2026-07-23.** A short working shortlist pulled from the much larger `TODO.md` backlog — items the
developer wants to actually work through over the next several days. Each entry below cross-references its
full write-up in `TODO.md` for context; this file is the queue, not a replacement for the fuller entries.
When an item here is finished, resolve it in `TODO.md`/`DONE.md` as usual and strike it here (or clear the
file and start a fresh one for the next stretch of work).

---

## High Priority

- [ ] **DLC city Physical Infrastructure deep-dive — Methodology #1 (Base Attributes) COMPLETE for all 34 non-Byrd cities; Methodology #2 now unblocked**
  Started 2026-07-30, directly following Byrd's own deep-dive (`Byrd_Physical_Infrastructure_Attributes.md`,
  80 attributes/57 Findings) — the source of `DLC_City_Under_Questline_Design_Method.md`'s own Input 9.
  Byrd got this treatment because it's a single-city DLC carrying full internal complexity alone; the other
  34 DLC cities across 5 subnets never went through either half of it. Two distinct methodologies, run in
  sequence per Byrd's own precedent: **Methodology #1 (Base Attributes)** — first-principles derivation from
  each city's own governing facts (geography, climate, population, economy) until it hits diminishing
  returns, then a cross-city-comparison round (checking every other city's own Community Infrastructure file
  for infrastructure types that genuinely apply). **Methodology #2 (Cross-Referenced Extrapolation
  Findings)** — combining those attributes against each city's own existing established lore for genuine
  multi-order-effect Findings, same "Combining → 2nd/3rd/4th-order effect" format Byrd's own file uses.
  **Methodology #1 finished 2026-07-30: Mawson subnet (Dome Fuji, Mawson, Sayowa), Mirny subnet (Mirny,
  Casey, Davis, Kunlun, Shirayuki, Sinheung, Vostok, Zhongshan), Halley subnet (Halley, Abowasa, Belgrano,
  Lazar, Neumayer, Princess Elisabeth, Sanay, Troll), Janbogo subnet (Janbogo, Cape Adare, Denison,
  Dumont d'Urville, Fort McMurdo, Scott, Zukelli), Palmer subnet (Palmer City, Esperanza, Juan Carlos,
  Marambio, Port Lockroy, Rothera, Sejong, Signy) — all 34 of 34 non-Byrd cities done.** **Methodology #2
  started 2026-07-30, run per-subnet like Methodology #1, depth scaled per city rather than uniform —
  a multi-city subnet spreads its depth across cities, unlike Byrd's own single-city 57-Finding scale.
  Mawson subnet COMPLETE: Dome Fuji +6 Findings (16 total, kept light — optional/non-main-questline
  despite real existing depth), Mawson +10 Findings (13 total, deepest of the three per direct developer
  instruction — needs to carry disproportionate weight since Sayowa is thin and Dome Fuji is optional),
  Sayowa +4 Findings (7 total, lightest — least existing content of the three).** Mirny, Halley, Janbogo,
  and Palmer subnets remain for Methodology #2.

- [ ] **The Long Night War's inciting incident — three identities still TBD**
  Core premise established 2026-07-04 (a diplomat assaulted a gynoid, killed in self-defense — she's Akina);
  the three specific identities involved are not yet chosen. See `TODO.md`'s "Decision Required" section.

- [ ] **Capricorn's core injustice — mechanism not yet chosen**
  Expanded 2026-07-20 from a rename question into a mechanism question; 4 contenders shortlisted, none
  chosen. See `Districts/Deep_Dives/06b_Capricorn_Alternative_Conditions.md` and `TODO.md`'s "Decision
  Required" section.

- [ ] **Byrd↔Janbogo aviation refueling stop — needs a real fix**
  See `TODO.md`'s "Decision Required" section for the underlying problem.

- [ ] **Cross-district non-malice audit — 5 of 9 items remain**
  4 of 9 already resolved; the remaining 5 all have candidate alternatives already written up. See
  `Cross_District_Non_Malice_Audit.md` and `TODO.md`'s "Decision Required" section.

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

- [ ] **Companion Forbidden Traits pass — 3 companions remain, 1 in-progress**
  IT-021 [Fenny], FW-25 [Pink Lucy], and Lyuba Baranova all have existing romance stat gates and just need
  this pass done. Majyao Bisyugota is in-progress — Demagogue confirmed, but a new trait ("Broad Strokes,"
  `Character-Creation/Traits.md`) still needs its bonus finalized before her list can close out. See
  `Core-Mechanics/Forbidden_Trait_Design_Method.md` for the full process and `TODO.md`'s own tracking entry.

- [ ] **Implant procedure cost** — the reputation-gate requirement is set (`Permanent_MACHINE_Stat_Increases.md`);
  just needs an actual credit amount decided.

- [ ] **Block Stance's exact numbers** — AP cost and DT/DR bonus size (`Combat/Block_Stance.md`). Resolving
  this also unlocks finalizing Unstoppable Force's own effect.

- [ ] **Cold/storm gradient numbers for `World_Map_Boundaries.md`** — the Engine-gated mechanism is chosen;
  just needs actual figures.

- [ ] **Starting skill-point formula** — FNV's real formula is verified (2 + 2×stat + 0.5×Luck); just needs a
  decision on what (if anything) replaces the Luck term for Inner Tepenia.

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

