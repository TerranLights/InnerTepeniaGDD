# Inner Tepenia — To-Do List

A running reference of outstanding design work, organized by urgency. Update as items are completed or reprioritized.

---

## Decision Required *(blocking other work)*

These require a developer call before downstream work can proceed. None can be resolved through research or writing alone.

- [x] **Ji-Eun Kim — main game vs. DLC — RESOLVED**
  Ji-Eun is alive, in Concordia, in the Aquarius district. Main game companion. Her concealment (nanotech self-modification) explains why Calethina cannot detect her. Calethina's degradation compounds the blindspot.

- [ ] **The Vigil [NAME TBD] faction — keep, redesign, or cut?**
  Blocks: Faction Devotion ending slot FD-7, faction design queue. Grok-suggested; off-world evacuees are now confirmed alive and prospering, which may change the dramatic premise. Review Grok notes in `to-be-integrated/miscellaneous/World_History_Reference.md` before deciding.

- [x] **Salagéa Aparast — main game vs. DLC placement — RESOLVED**
  DLC 5 (Atlantic Coastal Region) confirmed canon. She remains an active boat-dwelling datashard courier in the Belgrano/Atlantic coast region. Her full character concept is preserved. Cancer/No-One-Left-Behind Registry content in Concordia will need a different character or restructuring when that district is developed.

---

## High Priority

- [ ] **Issue F — Calethina's passive link to the player**
  What is the passive link between Calethina and the player called, and how does it feel mechanically? Affects questline structure and the player's relationship to her throughout the game. *Deferred alongside the full questline design.*

- [ ] **Calethina questline ("Echoes of the Bridge") — full design**
  *Deliberately deferred* until the surrounding world is better codified. Resume when the world feels stable enough for plot beats to land on real, established elements.

  **Established so far:**
  - Direction: archive-narrator. Calethina narrates ruins and abandoned infrastructure, generating quest hooks from her knowledge of the pre-Long Night War world.
  - First thread: Ji-Eun Kim (her ruined facility, her possible survival).
  - Structure: each location = physical ruin + Calethina's narration + a thread (person, object, question).
  - **Download option:** Approximately halfway through the main quest, the player can download Calethina onto their wrist device (the "not-Pipboy"). She's a single non-redundant instance — if her server is destroyed she is gone permanently. The download protects her but exposes her to everything the player encounters in the second half. Protection and risk simultaneously; a genuine choice.
  - **Grok notes:** The original 5-step questline and "personality download to Bridge Unit" climax were written before the archive-narrator direction was established. Review and reconcile (or discard) before writing the questline. See `Worldspace/Characters/Dolls/Still-Present_-_In-Game/Calethina/Personal_Questline_Summary.md`.
  - **Ghost Protocol connection (to develop):** Calethina may have been the one who embedded the Ghost Protocol safeguards into the Power Core during the Long Night War evacuation — a desperate emergency measure that saved lives at the time and has been quietly strangling the city for the one to two decades since the war ended. Her archive gaps may be guilt-adjacent rather than random degradation. She knows what she did; she doesn't lie, but she doesn't volunteer it. The player's path to this truth, and how the confrontation lands, is a core questline beat to design. See also: Ghost Protocol entry in Medium Priority — World and Story.

- [ ] **Robot religion design**
  Five religions are named but none are fully developed. Each needs: proper in-world name, detailed philosophy, key practitioners, connection to gameplay/factions, visual/sonic/spiritual identity.
  - Ice-Cold Buddhism (superconductor-as-nirvana) — **confirmed sacred sites: Dome Fuji and Kunlun** (coldest, highest, calmest locations in Tepenia; Kunlun is the holiest site; Dome Fuji is a major pilgrimage destination; both cities' surviving non-scientific populations may be primarily composed of practitioners; the pilgrimage journey to either city is itself a spiritual trial); proper in-world name TBD
  - Adinkra Codex (Universal Simulation Theory, with Sartre/Camus/Nietzsche subdivisions)
  - Cymaticists (reverence of sound and vibration)
  - God-mind simulation (God running simulations to understand its own origin)
  - Polydimensional Animism (acknowledging living entities in higher dimensions)
  Connected to: Robot-Aligned ending RA-2, multiple faction designs, NPC dialogue consistency across all districts.

- [ ] **Robot Religion Insight — naming conflict**
  A naming conflict was flagged in an earlier session and deferred. Resolve before robot religious content is finalized.

- [ ] **Planetary Split Brain questline — full design**
  Premise established: the Long Night War's destruction of Amundsen Station severed all six Arcanet subnets from each other. Each now holds isolated — and sometimes conflicting — records. The questline involves noticing contradictions in refugee accounts, tracing them to the structural Split Brain, and expeditioning to the South Pole to access the last synchronized pre-split archive.
  **Core mechanic confirmed:** player assembles the true picture by reconciling conflicting subnet records.
  **TBD:** Full quest structure, discovery trigger, South Pole archive integration, Arcanet reconstruction consequences, connection to Janbogo subnet nexus anomaly in Concordia.

- [ ] **Independent Lattice — full design**
  A secret alternative endgame solution with zero mechanical scaffolding: no stat checks, no skill checks, no perks, no quest markers, no notifications. The player can build a decentralized/distributed power grid as a complete alternative to the failing central grid beneath the Hub — but only if they are paying close attention to the world. Discovery method is entirely environmental: scattered notes, terminal entries, audio logs, fragments of NPC dialogue, and environmental storytelling distributed across the full game. No single source explains the full picture; the player assembles the method themselves.
  **TBD:** Full construction mechanics, the complete breadcrumb trail and its placement across all districts, the resolution state when the lattice is completed, and how the world reacts to the alternative solution.
  Working name "Independent Lattice" is Grok-suggested and developer-approved.

- [ ] **7 remaining district official names**
  Cancer, Taurus, Leo, Scorpio, Aries, Capricorn, and Libra use zodiac names but lack official proper names for in-world documents, signage, and NPC dialogue. The five already named: Aquarius (The Labs), Pisces (The Markets), Virgo (The Undergrid), Gemini (Janbogo), Sagittarius (The Frostlands).

- [ ] **District documentation template** — create `Worldspace/Locations-and-Levels/Concordia-City/Districts/_TEMPLATE.md`
  Must include a **Demonym** field: the word for "a person from [District]" (e.g., Sagittarius → Frostlander). Used in NPC dialogue, terminal entries, audio logs, and any in-world text referring to a district's residents as a group. Each district needs its own demonym established before NPC dialogue writing begins.

- [x] **District informal name system — resolved**
  All Grok-suggested informal names (Forgeward, Hearthward, Havenward, The Threshold, The Veil Market, Frostward Reaches, Ascendant Research Quarter, Thermal Spire, Coastal Cut, Mountain Cut, Resonance Crown, Bonded Habitation Rings, Governance Spire, Ossuary Quarter) replaced with zodiac + user-given names across all repo files.

---

## Medium Priority — Character Development

- [ ] **Ayako Hayashi — character development queue**
  Confirmed: recruitable companion; romanceable; 4w5 Self-Pres; Red Spiral medic; Japan origin; art/fashion → medicine trajectory; Schopenhauer as personal philosophy. Home designed (Leo district atelier). Romance design complete (Investigation ≥ 7, Humanity ≥ 6, Calculation ≥ 6; full 6-beat Gate 3 sequence). Outstanding:
  - Personality and voice (Phase 3)
  - MACHINE stat baseline
  - Full personal questline design
  - Red Spiral role/rank (confirmed NOT the leader)
  - Companion perks / notable traits
  - Japan lore (develop alongside Upper Earth/Japan world design)

- [ ] **IT-068 [Flora] — full development queue**
  First recruitable companion; well-scaffolded but incomplete. Established: 6w5 Thinking type; Capricorn industrial maintenance background; Frontline Utility Tank / Field Engineer combat role; recruitment scene at Thermal Distribution Junction 12 (mid-to-late Act 1); personality voice and approval system defined. Outstanding:
  - Permanent name (replace [Flora] placeholder)
  - Visual design and reference images
  - Full personal questline design
  - MACHINE stat tuning (full mechanical balance pass)
  - Romance questline thresholds (Phase 3)
  - Repair crew member names and characterization
  - Subvariant (Self-Pres vs. Social vs. Sexual) — TBD
  - District-specific approval modifier details beyond what's in README

- [ ] **Remaining named Doll characters — personality and backstory development**
  Six named characters have backstory scaffolding but undeveloped personalities, voices, and questlines:
  - **Kendra Heinrich** — 8w7:Sc; DLC 1 protagonist (South Pole); "goddess of war"; held off Upper Earth forces at Amundsen Tower while innocents evacuated; stranded; personality TBD
  - **Meyzan Yocazhda** — 3w2:Pr; job/setting TBD (Leo vs. Capricorn); almost entirely blank
  - **Michelle Stanton** — 5w6:Sc; built the Arcanet in a Kharkovchanka with a small team of robots and dedicated humans; now in Janbogo doing data archaeology and Great Corruption investigation; personality TBD
  - **Salagéa Aparast** — 1w2:Sc; Belgrano native; boat-dwelling datashard archivist; preserved civilizational knowledge during Long Night War; personality TBD; district pending (see Decision Required)
  - **Vosora Lashár Tanslock** — 5w6:Sc; nomadic data/logistics expert; organized Amundsen Tower construction logistics; stranded in Concordia by circumstance; transmitting data to space-dwelling Tepenians; personality TBD
  - **Calethina** — personality, backstory, and core identity entirely blank beyond questline structure

- [ ] **TBN characters — 11 remaining**
  All need: real name, district confirmation, full personality sketch, MACHINE stat baseline, role (companion vs. NPC), questline or story hook.
  - TBN [FR-03 billiards Maria] — everything TBD
  - TBN [FW-25 Pink Lucy] — 7w6:Sc; Leo entertainer; questline written but personality TBD
  - TBN [IT-021 white shirt Fenny] — 6w5:Pr; Taurus; questline written but personality TBD
  - TBN [TCY-06 red-dress Palmer City Elva] — established Star War house; personality TBD
  - TBN [TCY-20 unimpressed bartender Miranda] — The Quiet Shift; personality TBD
  - TBN [TCY-25 smoldering darkness Rui] — Scorpio-adjacent; personality TBD
  - TBN [TCY-42 ravishing extravagant Lillian] — legacy Star War house; personality TBD
  - TBN [TCY-45 heavenly summertime Momo] — everything TBD
  - TBN [XT-03 thicc Chinese Mei-Li] — 6w7:Sc; The Found/Assembled; personality TBD
  - TBN [XT-17 unorthodox science teacher Charlene] — 5w4; Aquarius; personality TBD
  - TBN [XT-21 cool citygirl Angelina] — 7w8; Hub; personality TBD

- [ ] **Doll Enneagram gaps — review pass**
  Four characters have no Enneagram type assigned; two have types but no subvariant. Do not design companion perks, attraction profiles, or romance gates for these characters until types are confirmed.
  - **Missing type entirely:** Maria (FR-03), Momo (TCY-45), Eirwyn Cardoss (Off-World template has no Enneagram field), Calethina (no standard README)
  - **Missing subvariant:** Charlene (XT-17) — 5w4, subvariant TBD; Angelina (XT-21) — 7w8, subvariant TBD
  - **Broader pass:** Full subvariant review across all doll characters with confirmed types — confirm existing subvariant assignments are correct before Phase 3 personality work begins

- [ ] **Red Spiral — leader identity TBD**
  Ayako Hayashi is confirmed NOT the leader of the Red Spiral. The actual leader's identity, background, and faction role within the Red Spiral hierarchy are undecided. Resolve before writing Red Spiral faction content or designing Ayako's questline in depth.

- [ ] **Character-level open questions (named Dolls)**
  Smaller items resolvable during character development sessions:
  - **Favi della Torre:** boyfriend's name (Italian human, Eyes of Gold member); Italian scientist's name; Taurus security network official name ("The Steady Watch" is a placeholder); nature of Favi–scientist relationship (confirmed NOT romantic; paternal/daughter vs. something more complex — must be decided before datashard event dialogue is written; see `Questlines/Companion_Event_The_Scientist_Entry.md`)
  - **Ji-Eun Kim:** identity of the person she built the concealment for; design the "undelivered letter" gate conditions and the lore it reveals (see Ji-Eun Kim README — Design Notes)
  - **Seica Cenilaithe:** husband's name; occupation in Scorpio; Archive of Final Confessions engagement level
  - **Villena Hiresvett:** venue names (2–3 regular residencies); Star War affiliation (Elva's established house vs. Lillian's legacy house)
  - **Majyao Bisyugota:** teahouse name; ~~verify Enneagram against lead sheet~~ — confirmed 4w5 Self-Pres
  - **Naizelle d'Edjordoś:** pre-war home city (destroyed in Long Night War; depends on pre-war geography work); recruiting hook
  - **Meyzan Yocazhda:** job/setting decision (Leo vs. Capricorn)
  - **Trisha Miller:** Activation Date still TBD

- [ ] **Upper Earth Defector characters — archetype framework**
  A folder exists but no substantive content. Upper Earth defectors are a significant player-facing archetype — humans or robots who crossed to help Tepenia. Needed: motivation framework, what they lost, what they carry. Create at least 2–3 exemplar NPC characters.

---

## Medium Priority — World and Story

- [ ] **Long Night War — historical parameters**
  Needed: combatants (which Upper Earth nations, which Tepenian forces), approximate duration, major engagements, how it ended. The Amundsen Tower destruction is the most iconic event but the broader war context is undefined. Blocks character backstory depth and level design parameters.

- [ ] **Zukelli vs. Janbogo — why one survived and the other didn't**
  Zukelli and Janbogo are ~10km apart on Terra Nova Bay, sharing the same polynya and coastal infrastructure. Zukelli was destroyed in the Long Night War; Janbogo survived. The reason for this asymmetry needs to be established — it is the most emotionally loaded open question in the Janbogo subnet's history and will directly shape the survivor-neighbor relationship in DLC content. Possible angles: strategic targeting (Zukelli had something the attackers wanted destroyed), defensive asymmetry (Janbogo had military infrastructure or faction protection Zukelli lacked), geography (Zukelli's island/coastal position made it more vulnerable), timing (Zukelli fell early and Janbogo's survival was partly because the war ended or the front shifted), or something else entirely. May connect to Long Night War historical parameters above.
  **Census finding to develop:** In the Orbital Era census (immediately before the Long Night War), Zukelli had one of the highest population retention rates of any city — 72.5% of its humans and 77.7% of its robots had not left for orbit, leaving it near its absolute peak population when it was destroyed. Zukelli did not die half-empty. This should shape how Janbogo NPCs remember it: survivor guilt is not "we watched a fading city die" but "we watched a full, living, thriving city burn." The grief has no softening qualifier. Develop this as a characterization note for Janbogo NPC writing and DLC 6 emotional tone.

- [ ] **Amundsen Tower destruction — specifics**
  Exact construction dates (start and completion); weapon type used to destroy it; scale of the resulting "giant mountain of scrap" at the South Pole as a level environment. Directly affects DLC 1 (Kendra Heinrich) environment design.
  **Census finding to develop:** By the time the Long Night War began, approximately **9.2 million Tepenians** (~30% of the entire pre-war population) were already living or working in low-earth orbit. The Amundsen Tower evacuations during the war were not people fleeing into a void — they were fleeing UP to an already-established, fully functional orbital civilization. This reframes the Tower's destruction: it was not just an act of mass murder against evacuees, it was the deliberate severing of a lifeline between two halves of a single civilization. Develop the narrative, mechanical, and faction implications of this — particularly for the orbital remnant's post-war relationship with Antarctic Tepenia, and for the Vigil faction concept (FD-7).

- [ ] **Orbital population — human/robot ratio and cultural implications**
  **Census finding:** The pre-war orbital population (~9.2M combined) was **52% human / 48% robot** — slightly human-heavy compared to Antarctic Tepenia's near-exact 1:1 surface ratio. The structural reason: Von Braun Wheels were designed for human habitation first; the robot-only staging station was long since absorbed by the time of the war, but the underlying design philosophy of orbital infrastructure remained human-primary. Develop implications:
  - Does orbital culture have a meaningfully different social texture than surface Tepenia, shaped by a slight human majority? Does this produce different politics, different faction dynamics, different relationship norms between humans and robots?
  - Is the ratio shift noticeable to the characters, or is 52/48 close enough to parity that no one treats it as a distinction?
  - Does the Vigil faction (FD-7, pending redesign) or any other off-world faction reflect this demographic tilt?
  - How does the orbital population's human-heavy lean interact with post-war contact — do orbital Tepenians and surface Tepenians experience each other as culturally alien?

- [ ] **Janbogo subnet nexus inside Concordia — narrative integration**
  The Janbogo subnet's physical nexus hardware sits inside Concordia's Gemini district, even though Concordia is a Mirny ("Australian") subnet city. Narrative potential: three non-exclusive explanations are possible — political deal (Janbogo refugees maintained hardware as integration condition), geographic legacy (routed through Concordia before Split Brain, never relocated), diaspora identity (cultural anchor for the enclave). Connects naturally to Planetary Split Brain questline and Gemini district identity. Decide which explanation (or combination) is canon.

- [ ] **Tentative factions — design all 9**
  Nine Faction Devotion endings are tagged [TENTATIVE] because the faction concepts they were written against are undesigned. All endings must be revised once faction designs are finalized. Factions needing full design:
  - FD-3: Veilkeepers
  - FD-4: Lattice / Bonded Lattice
  - FD-6: Reclaimers
  - FD-7: The Vigil [NAME TBD] *(pending keep/redesign/cut decision — see Decision Required)*
  - FD-8: Siligel Purists
  - FD-9: Neon Nomads
  - FD-10: Chorus of the Deep
  - FD-11: Memory Weavers
  - FD-12: Iron Gardeners
  See `Storyline/Endings/Secret-Endings/Faction_Devotion_Endings.md`.

- [ ] **Perks — first 50 remaining** *(elevated from Long-Term)*
  Current: 61/160 (38%). Target: 160 total. Recommended distribution: ~107 non-combat / ~53 combat. Current split: ~41 non-combat / ~20 combat — prioritize non-combat to maintain ratio. Perks are core to character build identity; 62% missing means build variety cannot be fully tested.

- [ ] **Might/Nerve design pass** *(elevated from Long-Term)*
  Both stats are marked TENTATIVE in the game mechanics files. The other five MACHINE stats are solid. Complete before balance testing can begin.

- [ ] **Tepenian Saints — create dedicated culture document**
  Confirmed canon: pre-War of Upper Earth (pre-2083) figures significant in the exploration and development of Antarctica are venerated as "Saints" in Tepenian civic culture. Known Saints so far: St. Robert (Robert Falcon Scott — city of Scott); St. Ernest (Shackleton); St. Roald (Amundsen — Amundsen Station); St. Douglas (Mawson — city of Mawson); St. Richard (Byrd — city of Byrd). Honorific uses first name. Tepenian interpretation: explorers who died or sacrificed for Antarctica unknowingly prepared the home that exiles would later need — the debt is real and is honored. Key tradition: Hut Point remembrance on Tepenian Independence Day (June 21) in Scott and Fort McMurdo — candles, flowers, personal tokens. Create a document in `Worldspace/Tepenian_Culture/` (or equivalent) covering the full Saints framework, known Saints roster, civic observances, and how the framework varies by city.

- [ ] **Pre-war Tepenian city culture — at least 5 cities**
  Destroyed cities appear in multiple character backstories but have no cultural identity beyond names. Each needs a brief cultural sketch — architecture, character, what was lost — to give character grief its texture. Palmer City is done. Minimum needed: Fort McMurdo, Janbogo, Belgrano, Neumayer, Mirny.

- [ ] **Midwestland — add to Maps/**
  Referenced in Trisha Miller's and Michelle Stanton's backstories as their Upper Earth origin. No map document exists for it.

- [ ] **Neural Overclock system — integration and balance pass**
  New file: `Game-Mechanics/Core-Mechanics/Neural_Overclock.md`. Three modes fully drafted (Framejack / Berserk / Overclock), stat scaling defined, drawback philosophy established. Outstanding:
  - Balance pass against AP economy (cross-ref `Action_Points_Base-Level_System.md`)
  - New perks per mode added to `Game-Mechanics/Character-Creation/Perks.md`
  - Enemy counterplay design (AI behavior during cooldown windows; cyberware-disrupting enemy units)
  - District vendor content (Aquarius experimental tiers; Capricorn industrial-grade; Pisces black market)
  - Narrative consequence tracking (companion reactions, ending flags, cyberpsychosis pathway)
  - Verify integration with Minmax build master chart

- [ ] **Damage Types system — integration pass**
  New file: `Game-Mechanics/Combat/Damage_Types.md`. Full 17-type system drafted; anti-robot / anti-human / shared specializations defined; district availability mapped. Outstanding:
  - Integration with existing DT/DR layered armor system
  - Perk interactions per damage type (which perks unlock resistance, bonus damage, or type-conversion)
  - Enemy unit damage type profiles (which enemy types use which damage)
  - Confirm Gravitic/Inertial as implemented or cut (marked "possible rather than confirmed")
  - Power-grid reactivity: ensure Aries destabilization → Lightning/EMP/Plasma hazard increase is mechanically implemented

- [ ] **Character_Connection_Map.md — reconciliation pass**
  File: `Worldspace/Characters/Character_Connection_Map.md`. Documents established narrative connections and a deferred issues table. Several items in the deferred table are now resolved (Ji-Eun main game decision, etc.). Needs a pass to:
  - Update or close resolved items in the deferred table
  - Ensure all new connections established since the file was written are added (Flora→Capricorn; Michelle→DLC 1 trigger; Kendra→Reclaimed Record; etc.)

- [ ] **Character_Concept_Bank.md — review for canon adoption**
  File: `Worldspace/Characters/Character_Concept_Bank.md`. Contains reassigned archetypes, faction seeds, and questlines that didn't fit their original characters but are too good to discard. Review each for adoption into the GDD:
  - **The Undergrid Cartographer + The Oldest Maps** (faction + questline) — Virgo; strong concept, no character attached yet
  - **The Frontier Route-Keeper + The Open Routes** (faction + questline) — Sagittarius; strong concept, no character attached yet
  - **The Aries Shift Crew Veteran** — knows the real Black Silence history; potential major NPC
  - **The Scorpio Archive Artist / Living Archive Community** — Goth Witness archetype; Scorpio faction in tension with clinical rebirth infrastructure
  - **Faction seeds** (Crossroads Claim, Fringe Curriculum, The Found/Assembled, The Warm Circuit, The Steady Watch, The House Network, No-One-Left-Behind Registry, The Long Frequency) — most already referenced in character files; confirm canon status and add to Factions folder where appropriate

- [ ] **Ghost Protocol safeguards — design as gameplay mechanic**
  Named and documented in `Worldspace/Energy_Grid_Failure_Rationale.md` (reason #9). Emergency AI protocols embedded into the Power Core during the Long Night War to prevent total collapse; now deeply entangled with core systems. Removing or overriding them risks triggering a built-in scorched-earth shutdown that could permanently disable large grid sections.
  **Calethina connection (to develop):** Calethina may have been the one who embedded these protocols during the evacuation — a life-saving emergency measure that has been quietly strangling the city for the one to two decades since the war ended. See Calethina questline entry for the full design note.
  **TBD:** How this functions as an in-game obstacle or quest mechanic; connection to the main story climax; whether the player can interface with it directly.

- [ ] **Amundsen Resonance Effect — design as gameplay mechanic**
  Named and documented in `Worldspace/Energy_Grid_Failure_Rationale.md` (reason #11). Harmonic instabilities from the destroyed Amundsen Tower cause resonance feedback during large-scale grid repairs, producing synchronized blackouts across multiple districts simultaneously — worse than the problem being fixed.
  **TBD:** How this manifests in gameplay; whether it connects to the Planetary Split Brain questline or the Amundsen Tower level environment; potential role in the climax.

---

## Long-Term / Low Urgency

- [ ] **to-be-integrated/ queue — review and extract**
  A large batch of raw files committed but not yet reviewed. Group them into two tiers:

  **Specific content files — likely to contain extractable canon:**
  - `Concordia Radio.txt` — new content area; no radio station design exists in canon yet beyond Trisha Miller's "The Signal"
  - `Defectors_Major_Questline.txt` — may supplement or conflict with `Storyline/Side-Content/Defectors_Major_Questline.md`; cross-reference before integrating
  - `balancing Minmax builds with Cyberjank functionalities.txt` — mechanics content; cross-ref against existing Minmax master chart
  - `district by Enneagram group series.txt` — district personality framework; compare against canon district profiles
  - `district conflicts - initial preliminary suggestions - 001.txt` — inter-district conflict seeds
  - `ending task possibilities - Act 3 and Climax.txt` — story structure seeds for Act 3; review for extractable beats
  - `starting task possibilities - Act 1 - leaving Calethina's lab.txt` — Act 1 structure seeds; compare against established Act 1 design
  - `per-district general problems.txt` — district-level problem seeds; may supplement District_Canon_Reference
  - `per-district history-factors and quest-triggers.txt` — district quest hooks; compare against Side-Content files
  - `skill list preliminary suggestions - possible basis for perks.txt` — perk/skill ideas; review during perk design pass
  - `first major recruitable companion.txt` — likely source material for Flora; verify absorbed or extract remainder
  - `current to-do.txt` — old TODO list; compare against current TODO.md for anything missing

  **Grok brainstorming files — treat with caution (banned names likely present):**
  - `Grok help - district conflicts and per-location quest-hooks.rtf`
  - `Grok help - district setup and per-location breakdown.rtf`
  - `Grok help - initial concept setup and pre-development.rtf`
  - `Grok help - main-story concept setup and pre-development - early brainstorming.rtf`
  - `Grok help - unorganized data 1.rtf`
  - `Grok help - unorganized data 2.rtf`
  Extract only specific ideas not already in canon; discard banned names and scaffolding. Do not treat any Grok file as authoritative.

  **Likely already absorbed — verify before discarding:**
  - `Damage Types - Baldurs Gate 3 equivalents.txt`, `Damage Types - Districts of Discovery.txt`, `Damage Types - Robots vs Humans vs Equal.txt` — precursor research to `Damage_Types.md`; confirm absorbed
  - `possible reasons - why not just fix the failing energy grid.txt` — precursor to `Energy_Grid_Failure_Rationale.md`; confirm absorbed
  - `city layout - district layout - preliminary suggestions.txt` — early concept; confirm absorbed into district docs
  - `district pairings - districts and their natural allies.txt`, `preliminary faction suggestions.txt` — compare against `District_Natural_Allies.md` and Factions folder

- [ ] **Amundsen Time Code (ATC) — design and integrate**
  Tepenia's equivalent of UTC. Based on North America's Eastern Standard Time (EST / UTC−5). Rationale:
  1. EST is home to New York City — one of the largest and most culturally, politically, and economically significant human settlements in history
  2. EST is the single geographically longest-spanning time zone on the world map
  3. EST de-facto encompasses the Antarctic Peninsula, home to Palmer City — the first Tepenian city, where robots (and their human allies) first set foot in 2564
  Named after Amundsen Station, the neutral inter-subnet relay at the South Pole — the most geographically "centerless" location in Tepenia, and thus the natural symbolic anchor for a pan-Tepenian timekeeping standard.
  To develop: how ATC is displayed in-game (clocks, the Arcanet, NPC dialogue); whether the Long Night War disrupted timekeeping consistency across subnets; whether the Planetary Split Brain created divergent local time conventions in isolated subnets; how ATC relates to the polar night / midnight sun (no sunrise/sunset to anchor local time perception).

- [ ] **"the Arcanet" / "the Solarnet" — terminology cleanup pass**
  Many older GDD files use bare "Arcanet" or "Solarnet" as standalone nouns without the definite article. Confirmed rule: always "the Arcanet" / "the Solarnet" when used as head nouns (equivalent to "the internet"); no article needed when used as modifiers ("Arcanet subnet", "Arcanet cables"). Files most likely to need correction: city layout docs, City_Logistics.md, Historical_Pressures.md, Player_Homes.md, to-be-integrated/ files.

- [ ] **Robot biology and culture — expand foundational document**
  New file created: `Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md`. Established canon: robots don't breathe but have internal thermal/sensory systems; siligel (food), coolant (drink), robot coffee (specialty coolant), and smoking (robot-specific vapor products interacting with internal systems) are all confirmed. Open questions remaining: siligel full composition, robot coffee exact formulation, smoking prevalence across Concordia's population, in-game smoking behavior beyond Naizelle and Zhuldyz.


- [ ] **Falkland Treaty — write the actual text**
  Research into real historical treaty formatting is complete. The document itself has not been drafted. Intended as a full in-world artifact, findable in the Treaty Archive Vaults in Libra's (TBN) governance spire.

- [ ] **World History — remaining TBDs**
  - Named evacuees in Concordia: who, which residents knew them, how
  - Unified Korea: reunification date, political system, role in War of Upper Earth
  - Gyeong-ja Yun: what happened after the 2318 ruling; specific in-game references
  - What "the evacuation" in the Falkland Treaty's suppressed information refers to
  - Sinian Federation: basically everything (deliberately deferred — see below)

- [ ] **Sinian Federation — full development**
  Deliberately underdeveloped until the developer has a clear picture of what the country is actually like. No stories set there until then. Exists as a named geopolitical reference only.

- [ ] **Narrative Weaver perk**
  Marked TENTATIVE. Revisit when perk design pass happens.

- [ ] **DLC structure — individual development**
  Seven DLCs planned (one per subnet + South Pole). See `Storyline/DLC_Overview.md` for full breakdown.
  **Confirmed scope standard:** main questline ~4–6 hours; optional side-content ~10–20 hours; total potential ~14–26 hours per DLC.
  - DLC 1: South Pole — **Kendra Heinrich** (character established; everything else TBD)
  - DLC 2: West Antarctica / Byrd — character and storyline TBD
  - DLC 3: Antarctic Peninsula (Palmer City ruins) — character and storyline TBD
  - DLC 4: Mawson Region (Indian Ocean coast) — character and storyline TBD
  - DLC 5: Atlantic Coastal Region (Halley, Belgrano, Queen Maud Land) — **Salagéa Aparast** (confirmed canon); storyline TBD
  - DLC 6: Janbogo Region (Ross Sea) — character and storyline TBD
  - DLC 7: Mirny Region (East Antarctic coast and interior) — **confirmed as its own DLC slot**; central character and storyline TBD; known assets: Mirny city (Antarctic Circle threshold, intra-subnet Arcanet link to Concordia), Casey (destroyed, blocks Pink Lucy Route B), Vostok (robot geneticist confirmed — reduced-mutation genetics breakthrough, Lake Vostok connection), Kunlun (Ice Cold Buddhism holy site, observatory implementation required as story beat); note: Dome Fuji is Halley subnet (DLC 5), not Mirny subnet

- [ ] **Byrd / Framheim / Little America founding — lore development**
  Confirmed canon for the founding chain:
  1. Old maps preserved at former Palmer Station, former Rothera Station, and former Belgrano Station II documented Byrd Station's location
  2. A founding expedition using rudimentary early-era Kharkovchankas (primitive by later Tepenian standards; the vehicles existed in basic form from Soviet Antarctic programs) followed the maps to Marie Byrd Land
  3. Found no surface structure — Byrd Station was entirely buried by 2564 (abandoned ~2005, buried for centuries)
  4. Set up a surface camp, probed, found the tunnels; the settlement grew downward first (underground town) before expanding outward through lateral tunneling and then upward above ground
  5. Underground archives at Byrd contained records of Framheim and Little America
  6. A later expedition from Byrd used those records to calculate the recalculated Ross Ice Shelf position and rebuild Framheim / Little America from scratch, designed for ice movement
  To develop: who led each expedition; the specific maps found at Palmer/Rothera/Belgrano II and what they contained; how the early-era Kharkovchanka compares to the mature vehicle (relevant to the broader Kharkovchanka technology development arc); the architectural design of rebuilt Framheim (precedents, engineering approach).

- [ ] **Michelle Stanton — Kharkovchanka as DLC trigger and character thread**
  Michelle is one of the very few Concordia residents capable of physically leaving the city. Her Kharkovchanka gives her continental travel capacity that almost no one else in Concordia possesses. She stays anyway — a choice that has never been fully explained in-world. Two design directions to develop:
  1. **Character revelation:** Why does someone who can leave choose not to? The answer to this question is a core piece of her personal questline — the choice to stay is as meaningful as the reason for it.
  2. **DLC trigger:** She is a natural vehicle for getting the player out of Concordia for at least one DLC. Her Kharkovchanka and continental expertise could be the practical means of departure; her reasons for finally leaving (or lending the vehicle) could tie directly into the DLC's stakes.
  See Michelle Stanton README — Design Notes.

- [ ] **Casey — city lore development (blocking Pink Lucy's migration route)**
  No lore exists for the city of Casey. Pink Lucy's pre-war migration route is either via Janbogo (Highway 183 → Concordia) or via Casey (Highway 2 / Dumont Coast Highway → Highway 110 → Concordia). Route B cannot be confirmed until Casey has at least a basic cultural and geographic identity. Develop Casey before finalizing her backstory.

- [ ] **Fort McMurdo and other Tepenian city lore**
  Palmer City is complete (`Worldspace/.../Cities/Palmer_City.md`). Full station-to-city map is complete. Fort McMurdo, Janbogo, Neumayer, Belgrano, Mirny, and others have no lore documents at Palmer City depth yet.

- [ ] **City logistics — remaining open questions**
  - Exact Concordia population figures (human and robot separately)
  - Currency and economic system
  - Cancer (TBN) district name resolution (formerly "Coastal Cut" — origin of "coastal" descriptor is still an open lore question for flavor, not blocking)
  - Subglacial water access (TBD whether it exists)
  - Nuclear vs. geothermal power specifics

- [ ] **Remaining perks — second and third batches**
  After the first 50 are completed (see Medium Priority), the remaining ~49 to reach 160 total.

---

## Completed

- [x] Enneagram_Dynamics.md — created in Worldspace/; global integration/disintegration ruleset transcribed from source; per-character application distributed to all 17 confirmed-type character READMEs under "Behavior under stress" field
- [x] Enneagram_Character_Index.md — created in Worldspace/Characters/; standalone per-character table with integration/disintegration directions for all confirmed-type characters; grows as new types are confirmed
- [x] Ayako Hayashi — core personality written: very shy in social contexts; brightens on fashion (primary) and art (secondary); shyness disappears entirely in medical contexts due to inner wound (was present and unable to save her human when he had his accident); Arcade Gannon comparison clarified as structural-only (not personality template)
- [x] Romance gate ordering rule — codified in Companion_System.md: Gate 1 (companion quest) always precedes Gate 2 (MACHINE stat check), which precedes Gate 3 (romance beat sequence)
- [x] Design_Principles.md — created in Worldspace/; five-opportunity minimum rule for romance beats established and documented with full per-character opportunity arrays for all 13 designed romances
- [x] Pink Lucy (FW-25) — romance design complete: Humanity ≥ 7 / Engine ≥ 6 / Nerve ≥ 5; full 5-beat Gate 3 sequence documented in Companion_System.md
- [x] Majyao Bisyugota — romance design complete: Humanity ≥ 7 / Investigation ≥ 6 / Calculation ≥ 6; full 5-beat Gate 3 sequence documented; Blood River Tea optional beat flagged for expansion
- [x] Ayako Hayashi — confirmed recruitable companion; romance design complete (Investigation ≥ 7 / Humanity ≥ 6 / Calculation ≥ 6; 6-beat Gate 3 sequence); Leo home designed (atelier-centered; full design in README); confirmed NOT Red Spiral leader
- [x] Ji-Eun Kim — confirmed alive; Aquarius district confirmed canon; main game companion confirmed; concealment motivations and gameplay mechanic seeds documented
- [x] Calethina's lab location — canonically Hub jurisdiction at Capricorn/Cancer border (updated in questline file)
- [x] Vosora Lashár Tanslock — Gemini/Janbogo district confirmed canon
- [x] Ji-Eun Kim — Aquarius/The Labs district confirmed canon
- [x] Favi della Torre — full backstory, personality, combat profile (sniper rifle primary; Might 3), and questline ("The Long Watch") complete
- [x] Trisha Miller — radio station name ("The Signal") and first Tepenian city (Belgrano) confirmed
- [x] Naizelle d'Edjordoś — district (Pisces), backstory, personality, and questline rewrite complete
- [x] Villena Hiresvett — district (Leo), backstory, personality, and questline rewrite complete
- [x] Majyao Bisyugota — district (Taurus), backstory (teahouse + Blood River Tea + Janbogo origin), and questline rewrite complete
- [x] Seica Cenilaithe — district (Scorpio), backstory, personality, and questline rewrite complete
- [x] Trisha Miller — district (Taurus), backstory, and personality rewrite complete
- [x] Michelle Stanton — backstory scaffolding complete (the Arcanet builder; Kharkovchanka; Janbogo data archaeology)
- [x] Kendra Heinrich — backstory scaffolding complete (South Pole; held Amundsen Tower; DLC 1 protagonist)
- [x] Salagéa Aparast — backstory scaffolding complete (Belgrano; boat; datashard courier; Long Night War archival mission)
- [x] Vosora Lashár Tanslock — backstory scaffolding complete (nomadic logistics; Amundsen Tower construction; transmitting to space)
- [x] All 13 district canon profiles written (District_Canon_Reference.md)
- [x] 12 named Doll Questlines/README.md files written
- [x] Character Concept Bank created (reassigned archetypes + faction seeds preserved)
- [x] All 6 failsafe ending categories designed and written (Near-Pariah, Wild Child, Faction Devotion, Calethina Devotion, Identity Fragmentation, Robot-Aligned)
- [x] FD-1 Eyes of Gold ending revision complete
- [x] Hidden Paths full treatment (4 paths, 9 resolutions)
- [x] Eyes of Gold full faction profile
- [x] Ji-Eun Kim character file
- [x] Concordia city logistics document
- [x] World History Reference document (with confirmed/TBD separation)
- [x] Character Connection Map
- [x] Tepenian city geography established (station-to-city mapping, ~40 stations)
- [x] "Upper Earth" correctly defined (geographic, not cosmological)
- [x] War of Upper Earth and Long Night War confirmed as separate conflicts
- [x] Robot personhood timeline established (2318–2564, Gyeong-ja Yun case)
- [x] Jeju-do International Court of Diplomacy documented
- [x] Sinian Federation named and flagged for future development
- [x] Off-world evacuees confirmed alive and prospering (orbit, Mars moons, toward Venus)
- [x] Red Nebula logo files renamed to Red Spiral
- [x] Livestock updated: yaks, alpacas, sheep, reindeer as primary herded protein; Cancer (TBN) + Frostlands placement; cattle as limited luxury
- [x] Palmer City lore document written
- [x] Full station-to-city mapping tabulated (all ~40 stations on the map)
- [x] Tepenian Federation flag decided (wide circuit)
- [x] Federal/government flag variants — three-tier hierarchy established (wide circuit / diamond+circuit background / tesseract seal)
