# Weekly To-Do — Current

**Started 2026-07-23.** A short working shortlist pulled from the much larger `TODO.md` backlog — items the
developer wants to actually work through over the next several days. Each entry below cross-references its
full write-up in `TODO.md` for context; this file is the queue, not a replacement for the fuller entries.
When an item here is finished, resolve it in `TODO.md`/`DONE.md` as usual and strike it here (or clear the
file and start a fresh one for the next stretch of work).

---

## High Priority

- [x] **DLC city Physical Infrastructure deep-dive — Methodology #1 AND Methodology #2 COMPLETE for all 34 non-Byrd cities**
  Completed 2026-07-30, directly following Byrd's own deep-dive (`Byrd_Physical_Infrastructure_Attributes.md`,
  80 attributes/57 Findings) — the source of `DLC_City_Under_Questline_Design_Method.md`'s own Input 9.
  Byrd got this treatment because it's a single-city DLC carrying full internal complexity alone; every other
  DLC city across all 5 subnets has now gone through the identical two-part process. **Methodology #1 (Base
  Attributes)** — first-principles derivation from each city's own governing facts, then a cross-city
  comparison round. **Methodology #2 (Cross-Referenced Extrapolation Findings)** — combining those attributes
  against each city's own existing lore for multi-order-effect Findings, same "Combining → 2nd/3rd/4th-order
  effect" format Byrd's own file uses, appended directly into each city's own Attributes file. Depth scaled
  per city rather than uniform in every subnet: each subnet's own hub/story-anchor city (or split of 2-3
  cities, confirmed per-subnet against `DLC_Overview.md`, asking the developer directly whenever that file
  left the central location ambiguous) got Mawson-level depth; every other city got proportionate, moderate
  treatment reflecting its own existing depth, never a token pass. **Final totals — every city now has a
  `[City]_Physical_Infrastructure_Attributes.md` file combining both methodologies:**
  - **Mawson subnet:** Dome Fuji 16 Findings, Mawson 13 (deepest), Sayowa 7
  - **Mirny subnet:** Mirny 11 (deepest), Kunlun 8, Vostok 8, Casey/Davis/Shirayuki/Sinheung/Zhongshan 7 each
  - **Halley subnet:** Neumayer 11, Sanay 10, Troll 9 (three deep-treatment cities), Halley/Abowasa/Belgrano/
    Lazar/Princess Elisabeth 8 each
  - **Janbogo subnet:** Janbogo 10, Fort McMurdo 10 (two deep-treatment cities), Cape Adare/Denison/Dumont
    d'Urville/Scott 8 each, Zukelli 9
  - **Palmer subnet:** Palmer City 16 (deepest, single clean hub per `DLC_Overview.md`), Esperanza/Juan
    Carlos/Port Lockroy/Rothera/Sejong/Signy 8 each, Marambio 7

  This entire high-priority item is now fully resolved — the natural next step, whenever picked up, is
  actually running `DLC_City_Under_Questline_Design_Method.md` against this material (Byrd is still the only
  city confirmed ready to run it with zero fallbacks, but all 34 other cities now have real Input 9-equivalent
  material of their own for the first time).

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

- [ ] **Per-district inter-city conflicts — measure, assess, derive, and synthesize** *(flagged 2026-07-31)*
  Using `District_Refugee_Diaspora_Composition.md`'s own weighted composition per district, work through what
  "cultural conflicts" would plausibly arise (a) **between different refugee-diaspora populations sharing the
  same district** (e.g. two source cities whose established values or social norms genuinely clash, not just
  differ) and (b) **between a district's refugee-diaspora population(s) and that district's own native/local
  population and established culture**. This is a distinct pass from the diaspora file's own "brought with
  them" transplant framing (which is about what each community contributes) and from the Deep Dive diaspora
  findings (which chase implications, not necessarily friction) — this pass is specifically about identifying
  and naming genuine points of tension. Natural companion to the item below, and further raw material for
  Under-Questline generation once both passes exist.

- [ ] **Per-district inter-city friendships — measure, assess, derive, and synthesize** *(flagged 2026-07-31)*
  The positive counterpart to the conflicts item directly above. Using `District_Refugee_Diaspora_Composition.md`'s
  own weighted composition per district, work through what "cultural crossovers" — genuine common ground,
  not just peaceful coexistence — would plausibly arise (a) **between different refugee-diaspora populations
  sharing the same district** (e.g. two source cities whose established values or social practices actually
  reinforce or complement each other) and (b) **between a district's refugee-diaspora population(s) and that
  district's own native/local population and established culture**. Same distinction as the conflicts item:
  this is about identifying and naming specific, genuine points of connection — ways people would actually
  find common ground — not a repeat of the diaspora file's own "brought with them" transplant framing or the
  Deep Dive findings. Further raw material for Under-Questline generation once both passes exist.

- [ ] **Per-district ordinary daily life — measure, assess, derive, and synthesize** *(flagged 2026-07-31)*
  Go through each of the 13 districts and work out what an ordinary resident's actual day-to-day life is
  like — daily routines, mundane concerns, personal struggles, and forms of personal escapism/downtime —
  distinct from whatever that district's own defining civic identity or institutional purpose is. Explicit
  example from the developer: Scorpio residents cannot plausibly spend every waking moment in a death ritual
  confessing their grief; people have lives outside of a district's headline function, and those ordinary
  lives are currently underexplored across the corpus. This is a third, distinct pass alongside the conflicts
  and friendships items directly above — not about inter-community dynamics at all, but about what any single
  resident's own life actually consists of day to day. Further raw material for Under-Questline generation
  (and general NPC/character writing) once all three passes exist.

- [ ] **District Main vs. Under-Questline candidates — generate more** ⭐ *(unblocked 2026-08-08 — see below)*
  Structure and both governing files (`District_Main_Questlines.md`, `District_Under_Questline_Design_Method.md`)
  are established; each district currently has only its *first* main-questline candidate. Main questlines:
  generate several candidates per district using the existing Internal-Conflict format, then narrow to
  exactly one. Under-Questlines: generate a floor of 5 (ideally 15-20) per district, anchored to a
  "significant starting point" (a named figure or a data-point at a significant location) — and, unlike main
  questlines, **keep all of them**, no narrowing. See `project_district_questline_production_workflow`
  memory for the full workflow. **Updated 2026-07-31 — new input material ready:** `District_Refugee_Diaspora_Composition.md`
  (weighted diaspora composition + specific named cultural transplants per district) and the matching
  2026-07-31 diaspora-informed extension of all 13 `Deep_Dives/[NN]_[District]_Deep_Dive.md` files (4-5 new
  findings each) give this generation pass real, specific, named hook material it didn't have before — see
  `TODO.md`'s own new entry for the full picture. **This item was deliberately held pending a thorough robot
  culture foundation, per the developer's own explicit sequencing decision — that foundation (the "Robot
  Universals" reference book, `TepenianUniverseTimeline/Reference/Robot_Universals/`) is now complete as of
  2026-08-08, so this is unblocked and ready to actually run.** Not yet run.

- [ ] **Doll Character Spec / Companion-Romance backstory depth — psychological depth and inner conflict**
  ⭐ *(unblocked 2026-08-08, same reason as above)*
  Also deliberately held pending the robot culture foundation — much of what the Character Spec and
  Companion/Romance Fill-In sheets ask about (kinship, build, personality formation) was unresolved for
  robots specifically until Robot Universals was finished. Now unblocked. Relevant material: the fill-in
  templates themselves (`Worldspace/Characters/Dolls/Character_Spec_Fill-In_Sheet_Template.md`,
  `Worldspace/Characters/Dolls/Companion_and_Romance_Questline_Fill-In_Sheet_Template.md`, and the composite
  `z-template/` folder), and TODO.md's own existing "Remaining named Doll characters — personality and
  backstory development" entry (Medium Priority — Character Development) listing the six companions still
  needing this pass: Kendra Heinrich, Meyzan Yocazhda, Michelle Stanton, Salagéa Aparast, Vosora Lashár
  Tanslock, and Calethina.

---

## 2026-08-01 Backlog Batch

Pulled from `TODO.md`'s "Large backlog batch — flagged 2026-08-01" entry — see there for the full write-up
per item. Everything from that batch is included here **except** "expand upon individual city history
specs," which stays in `TODO.md` only for now.

**Combat & systems mechanics**
- [ ] **Sneaking and line-of-sight** — stealth/detection mechanics not yet designed.
- [ ] **More weapons** — expand the current weapon roster.
- [ ] **Armor and clothing** — a system for this doesn't yet exist.
- [ ] **Faction outfitting** — what specific factions actually wear/carry, distinct from the general
  armor/clothing system above.
- [ ] **Real-world scientific basis for BG3 damage types** — what objects/items would cause the
  scientifically-supported equivalent of each BG3 damage type (and comparable relative amounts), and what
  kind of setting each would characteristically be found in. Ties into `Per_City_Weapons`/`Damage_Types.md`.

**Worldbuilding — civic life & economy**
- [ ] **The actual legal mechanisms of how Tepenia deals with criminals** — courts, arrest, enforcement
  procedure; more detailed than the existing 3-tier outcome framework (`project_tepenian_criminal_justice_system`
  memory).
- [ ] **What kinds of festivals exist, generally** — beyond what's already scattered per-city/per-district.
- [ ] **Are there any homeless people in Tepenia**, and if so, what does that look like.
- [ ] **Where do cities/districts actually get their water.**
- [ ] **What standard is Tepenian currency actually based on** — deliberately the first domino; the actual
  *name* (see the separate "National currency name and mechanics" entry above/below) is downstream of this,
  not decided in parallel. Also: don't use the word "scrip" in new writing — see that entry for why.
- [ ] **General standards of living, and the cost of things.**
- [ ] **What does it actually mean to be "rich" in Tepenia** — follows directly from the item above.
- [ ] **How is sewage and septic waste treated/handled.**
- [ ] **What other food-producing locations exist**, beyond what's already established (Davis's breadbasket
  role, etc.).
- [ ] **A general accounting of what currently exists across the project as flagged "side-content."**

**Documentation**
- [ ] **Go in and actually comment the code** — including pseudocode.

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

