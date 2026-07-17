# Neo-Races and Neo-Cultures — Progress Tracker

**PROCESS REQUIREMENT, added 2026-07-16 during Marambio's correction pass — read before starting any
new city's Phase 1c work:** check that city's own `City_Megasheets/[Subnet]/[City]/` files
(Mega_Init, Full_Extrapolation, Cross_Reference_Synthesis), `City_Enneagram_Personalities/[Subnet]/
[City].md`, and `City_Vision_Notes/[City].md` (if it exists) *before* drafting Per-Nation Entries — not
just `Specs/[City].md`.

**DEEP CULTURE QUALITY BAR, added 2026-07-16 per developer feedback on Casey's first draft:** every
Deep Culture entry needs genuine multi-field substance (Communication styles, Notions of, Concepts of,
Attitudes toward, Approaches to — using whichever subset genuinely applies) rather than one thin
"Concepts of: [X], converging with the dominant register" line. A spot-check found this exact thinness
problem already present in at least Rothera (France's entry, and likely others across the Palmer
subnet) — **not yet retroactively audited for this specific issue**, flagged as a known quality gap
separate from the (already-resolved) research-completeness gap above.

**DEPTH STANDARD FINALIZED, 2026-07-16, per direct developer instruction: "establish this level of
depth as standard, and then we're gonna double-check the cities we've gone over."** Every nation entry
must individually address all 12 Surface Culture items and all 17 Deep Culture sub-items across the
five Deep Culture headers (Communication styles and rules — 5 items; Notions of — 3; Concepts of — 3;
Attitudes toward — 4; Approaches to — 2) — not condensed into one summary line per header, and not
silently dropped when genuinely unmatched ("no strongly distinct local variant surfaced" still gets its
own line). This is now written directly into `City_Catalog_Template.md` itself, not just this tracker.
**Davis (Mirny subnet, second city, redone under this bar after Casey exposed the gap) is the current
reference example** for full-depth treatment — Casey itself was drafted just before this exact standard
was finalized and should be checked against it too.

**FULL RE-AUDIT NOW REQUIRED, superseding the narrower "Deep Culture thinness" flag above:** every city
completed before Davis — all 8 Halley subnet cities, all 8 Palmer subnet cities, and Casey — needs to be
checked against the full 12+17-item depth standard, not just spot-checked for thinness. Recommended
approach: work through subnet by subnet in the same order already established (Halley, then Palmer,
then Casey), checking each nation entry against the full template checklist and expanding any condensed
or dropped items.

**FULL RE-AUDIT QUEUE COMPLETE, 2026-07-16.** All 17 cities flagged above have now been gap-filled to
the full 12+17-item depth standard — every Surface Culture item and every Deep Culture sub-item
individually addressed for every Primary/Significant-tier nation in every city: all 8 Halley subnet
cities (Sanay, Abowasa, Belgrano, Halley, Lazar, Neumayer, Princess Elisabeth, Troll), all 8 Palmer
subnet cities (Esperanza, Juan Carlos, Marambio, Palmer City, Port Lockroy, Rothera, Sejong, Signy), and
Casey (Mirny subnet). Each city committed individually with its own gap-fill commit. Casey required a
distinct approach from the other 16 — it already had substantial paragraph-level Deep Culture content
per header (drafted after the "Concepts of fields close to empty" correction but before the full
12+17-item standard existed), so that pass converted existing paragraphs into itemized sub-bullets
rather than writing from near-scratch. **No further backlog remains from the depth-standard
finalization — new cities going forward should be drafted at full depth from the start, per the
template's own DEPTH REQUIREMENT note.**

**RETROACTIVE-AUDIT GAP FULLY RESOLVED, 2026-07-16.** All 10 cities completed before the process
requirement existed (Sanay, Abowasa, Belgrano, Halley, Lazar, Neumayer, Princess Elisabeth, Troll,
Esperanza, Juan Carlos) have now been checked against their own Vision Notes/Megasheet research and
corrected where needed. Genuinely significant finds, not just minor polish: **Neumayer secretly
designed and engineered Amundsen Tower itself**, unrecognized at the Tower's own ruins today (the
single biggest find of the whole audit); **Troll's freight network directly supplied Dome Fuji**, a
concrete cross-subnet tie previously missing; **Halley's relocation mechanism was factually wrong**
("periodic towing" corrected to continuous digging-track propulsion); **Lazar's real internal fault
line is old-core-vs-new-expansion**, not the founder-vs-majority pattern used everywhere else;
**Esperanza's official identity is "The Guarded City"** (robots built to protect humans) with mining as
a missed second economic pillar; **Juan Carlos's tertulia** (already exported into Concordia's Leo/
Taurus/Pisces districts) was missing entirely, along with its "Room to Be Itself" counterpoint-to-Sejong
identity; Sanay, Abowasa, and Troll all share a "Competence Without Commentary" faction, each with a
distinct angle, not previously connected. Every affected commit is tagged "retroactively audited" in
its own city's line below and in git history. No further retroactive-audit work is outstanding for
these 10 cities; the same process requirement now applies going forward to all remaining cities so this
gap doesn't recur.

**Status, updated 2026-07-16:** all 35 cities now have their City Snapshot, their Real-World Parallel
Locations (Phase 1b, terrain/geography-based), their City-Type Parallels (Phase 1b-ii,
functional/civic-identity-based — port cities, aviation hubs, research towns, famous leisure
landmarks, etc., independent of geology), AND a Population Weighting Reference table (every nation at
every tier — not just Primary/Significant — with its exact population share %, pulled directly from
each city's own `Specs/[City].md` Per-Nation Breakdown table) sections filled in. For the two
real-world-match dimensions, matches have been identified for every Primary/Significant-tier nation in
each city (or honestly flagged as weak/no match/no distinctive type where none exists), subnet by
subnet. The Population Weighting Reference exists specifically so that future Phase 1c cultural
findings can be weighted by actual population share rather than treated as if every listed nation
contributed equally to a city's culture. Each city's own functional/civic type classification is also
consolidated in `City_Types_Reference.md` so it doesn't need to be re-derived later. **Phase 1c
(Per-Nation Cultural Iceberg / Surface+Deep Culture findings) is now underway.** Sanay was the first
city complete (2026-07-16), run as a deliberate test of the full method before scaling up; see
`Phase1c_Test_Run_Sanay.md` for the process notes. **The entire Halley Subnet is now Phase 1c
complete** (all 8 cities, 2026-07-16) — see `Halley_Subnet_Phase1c_Summary.md` for the full cross-city
synthesis roundup, kept deliberately separate from any single city's own Catalog file. Four recurring
findings are now validated across a full
subnet and should be treated as settled methodology for the remaining cities rather than re-derived
per city: (1) founding nations regularly drift to Notable tier while surviving only as civic mythology;
(2) population share and match-strength/narrative-weight regularly decouple; (3) Brazil's City-Type
matches are weak specifically at small purpose-built single-mission settlements and strong at large
organic multi-purpose cities — a predictable rule, not random weakness; (4) multiple populations often
converge on one civic value via genuinely different real-world routes, which is worth calling out
explicitly rather than treated as redundant. **The entire Palmer Subnet is now also Phase 1c complete**
(all 8 cities, 2026-07-16) — see `Palmer_Subnet_Phase1c_Summary.md` for its own cross-city roundup,
which adds three more findings: (5) a city's own existing Megasheet/Enneagram/Vision-Notes research
must be checked before drafting, now a standing process requirement after Marambio and Sejong both
needed correction passes; (6) a second "large population, no strong anchor" category exists (Italy,
Spain/Mexico) distinct from Brazil's settlement-type rule, not yet explained; (7) numeric population
dominance doesn't determine a city's civic register on its own — Signy's 33.33% USA population still
produces a quiet, Withdrawn-profile culture because the city's own personality core points that
direction regardless. The remaining 19 cities' Per-Nation Entries are unstarted; this is still the
genuinely expensive phase. Mirrors the checklist convention already established for
`Cities/Full_City_Integrity_Check.md`.

Legend: `[ ]` not started · `[~]` City Snapshot done only · `[b]` City Snapshot + Real-World Parallel Locations (Phase 1b) + City-Type Parallels (Phase 1b-ii) + Population Weighting Reference done, Cultural Iceberg findings (Phase 1c) not started · `[x]` Phase 1 fully complete, ready for Phase 2 synthesis

---

## Halley Subnet
- [x] Abowasa *(city-type resolved 2026-07-16: a scaled-down twin-settlement residential/commuter community for workers commuting to Sanay/Troll, echoing Budapest/Twin Cities/Kansas City at a much smaller scale; PHASE 1C COMPLETE 2026-07-16 — second city finished, Germany/Wanne-Eickel disproportionately strongest narrative match despite being smallest population share; RETROACTIVELY AUDITED 2026-07-16 — folded in Abowasa's own angle on the shared "Competence Without Commentary" faction ("competence is intimacy management") and the real Aboa/Wasa seasonal-staffing founding detail, fourth city in the retroactive-audit gap resolved)*
- [x] Belgrano *(also has a secondary garage/warehouse/industrial culture alongside its primary aeronautics/port identity — developer note added 2026-07-16; PHASE 1C COMPLETE 2026-07-16 — third city finished, Tepenia's clearest "maker city" synthesis so far; CORRECTED 2026-07-16 during Marambio's own pass: Brazil is NOT weak here after all — Belgrano is an Atlantic-coast receiving point for the established South America shipping corridor, missed in the original single-city City-Type search; RETROACTIVELY AUDITED against Vision Notes 2026-07-16 — folded in the Rastra vehicle lineage, the confirmed "Garage Rock" genre name, official identity "The Airbase That Never Stood Down," robot-specific culture, and Argentina's founding-drift echo — first city in the retroactive-audit gap resolved)*
- [x] Halley *(no true real-world non-polar analog for its moving-ice-shelf terrain — flagged, substitute category used instead; PHASE 1C COMPLETE 2026-07-16 — fourth city finished; unique dual-impermanence identity, moving ground plus pure-waypoint civic role, gives USA/Canada outsized cultural influence despite not being the largest populations; RETROACTIVELY AUDITED 2026-07-16 — corrected "periodic towing" to the actual continuous digging-track propulsion mechanism, folded in "The Methodologists" faction philosophy and official identity "Built to Move," second city in the retroactive-audit gap resolved)*
- [x] Lazar *(PHASE 1C COMPLETE 2026-07-16 — fifth city finished; Tepenia's clearest "big city" synthesis, all six populations well-textured since the megacity City-Type is broad; Brazil's strong showing here disproves an over-generalized "Brazil matches weakly" reading from Belgrano/Halley; surfaced a real "largest city, not the capital" civic tension; RETROACTIVELY AUDITED 2026-07-16 — major structural correction: Lazar's real fault line is old-core-vs-new-expansion ("Grown Together" faction), not founder-vs-majority like other cities; also flagged the city's actual economic engine as a genuine unresolved open thread, not something the national-flavor entries resolve; fifth city in the retroactive-audit gap resolved)*
- [x] Neumayer *(shares Halley's moving-ice-shelf terrain and its "no true analog" flag; PHASE 1C COMPLETE 2026-07-16 — sixth city finished; Tepenia's clearest research-institute city, multiple national prestige-hierarchies coexisting; Germany confirmed as founding-operator-plus-dual-anchored-plus-substantial-population, a genuinely foundational rather than just-present population; Brazil's "weak at small purpose-built towns, strong at large organic cities" pattern now confirmed across 3 cities; RETROACTIVELY AUDITED 2026-07-16 — major missed detail folded in: Neumayer secretly designed/engineered Amundsen Tower itself, unrecognized at the ruins today; also added confirmed Electronic/Metal/Digital-Industrial music genres and the "Measured, Not Debated" identity core; sixth city in the retroactive-audit gap resolved)*
- [x] Princess Elisabeth *(PHASE 1C COMPLETE 2026-07-16 — seventh city finished; both co-Primary populations, Japan and USA, are double-anchored and converge on "extreme wind as mastery/frontier, not just hardship"; working name "Elisabethan" flagged as a probably-unwanted real-world homophone, needs a different placeholder; RETROACTIVELY AUDITED 2026-07-16 — folded in official identity "Leaving No Mark, Meeting in the Middle" and the shared "Crossroads People" faction (unresolved cultural belonging, distinct from but coexisting with the research convergence), wind/solar infrastructure detail, and a genuine unresolved underground-mystery narrative hook; seventh city in the retroactive-audit gap resolved)*
- [x] Sanay *(the project's own first worked example for the City-Type Parallels category — a major shipping/logistics port city; now also the FIRST CITY WITH PHASE 1C COMPLETE, 2026-07-16 — Per-Nation Entries for Germany/Brazil/UK done, plus a draft Phase 2 "Sanayan" synthesis; see `Phase1c_Test_Run_Sanay.md`; RETROACTIVELY AUDITED 2026-07-16 — folded in "Competence Without Commentary" faction philosophy and the human-robot labor dynamic first established here (later generalized project-wide), third city in the retroactive-audit gap resolved)*
- [x] Troll *(PHASE 1C COMPLETE 2026-07-16 — eighth and final Halley subnet city; three-way freight-logistics-precision convergence, USA/UK/Germany; HALLEY SUBNET FULLY PHASE 1C COMPLETE — see `Halley_Subnet_Phase1c_Summary.md`; RETROACTIVELY AUDITED 2026-07-16 — major cross-subnet detail folded in: Troll's freight network directly supplied Dome Fuji, a concrete tie to that city's pilgrimage identity; also added the "competence is leverage" angle on the shared faction, the "no neutral path" airfield-control civic tension, and the above-average-spending-power/higher-quality-glitch-coolant economic nuance; eighth and LAST city in the original 10-city retroactive-audit gap resolved — ALL 8 HALLEY SUBNET CITIES NOW AUDITED, plus Sanay (done as part of this batch); only Esperanza and Juan Carlos remain from the original 10-city gap list)*

## Janbogo Subnet
- [b] Cape Adare
- [b] Denison
- [b] Dumont d'Urville *(city-type resolved 2026-07-16: a wildlife-tourism/nature-reserve gateway city, echoing Kaikōura/Simon's Town/Punta Tombo, with a "Quebec City-like" cultured small-town core)*
- [b] Fort McMurdo
- [b] Janbogo
- [b] Scott
- [b] Zukelli

## Mawson Subnet
- [b] Dome Fuji *(fundamentally, foundationally a religious/pilgrimage city — established by and for the Ice-Cold Buddhists; NOT a co-equal dual type with its ice-core research economy, which is a genuine but distant second — reinforced by the developer 2026-07-16)*
- [b] Mawson
- [b] Sayowa

## Mirny Subnet
- [x] Casey *(the project's own second worked example for the City-Type Parallels category — nationally famous for "Splinters," its huge live-music bar; PHASE 1C COMPLETE 2026-07-16 — first Mirny subnet city; real founding tension is destination-vs-waypoint (not entertainment-district generically), USA triple-anchored via Flagstaff/Memphis/Reno; DEEP CULTURE QUALITY BAR RAISED this city — full multi-field Deep Culture entries required per developer feedback, see quality-bar note in header)*
- [b] Davis *(city-type resolved 2026-07-16: a combined ecological/limnological research hub AND Tepenia's foremost sheltered-agriculture/greenhouse city — the "breadbasket of Tepenia," growing from Davis's status as the largest ice-free oasis in the country)*
- [b] Kunlun *(100% robot population — Phase 1b treated the nation list as heritage-tracking rather than a literal resident population; same caveat carries into Phase 1c)*
- [b] Mirny
- [b] Shirayuki
- [b] Sinheung
- [b] Vostok *(no true real-world non-polar analog for its extreme-cold/extreme-isolation terrain — flagged, same category as Halley)*
- [b] Zhongshan *(the developer's own worked example for the whole project — "Zhongshanese" — good candidate for the first full Phase 1c pass)*

## Palmer Subnet
- [x] Esperanza *(PHASE 1C COMPLETE 2026-07-16 — first Palmer subnet city; a "family/genesis city" identity tied to its real founding history; Argentina, despite being the smallest population, holds the strongest combined real-world match plus a literal historical tie to the city's own founding event, found anywhere in the project so far; RETROACTIVELY AUDITED 2026-07-16 — official identity is actually "The Guarded City" (robots built to protect humans, demographic drift read as compact-honored not eroded); added mining as a missed second economic pillar and the rotational-mining-shift/robot-caregiver family structure, the origin point for several now-project-wide facts (artificial womb tech, male-skewed immigration, robot memory-carriers); ninth city in the retroactive-audit gap resolved, one remains: Juan Carlos)*
- [x] Juan Carlos *(PHASE 1C COMPLETE 2026-07-16 — second Palmer subnet city; fishing-port-plus-archive city; Spain's namesake claim on "Juan Carlos I" is a second, distinct-mechanism instance of symbolic-vs-population-share weight; Italy flagged as a genuinely new "weak on both axes, doesn't fit the Brazil rule" case worth watching; RETROACTIVELY AUDITED 2026-07-16 — major missed detail: official identity is "Room to Be Itself," the deliberate counterpoint to Sejong's own contrast-defined identity ("Coherence vs. Contrast" faction), with the tertulia (already exported into Concordia's Leo/Taurus/Pisces districts) as its single most concrete expression; TENTH AND FINAL CITY IN THE ORIGINAL RETROACTIVE-AUDIT GAP — ALL 10 CITIES NOW RESOLVED)*
- [x] Marambio *(PHASE 1C COMPLETE 2026-07-16 — third Palmer subnet city; two cultural pillars, aviation (USA/Germany/UK) and South America shipping-corridor maritime trade (Brazil, via the already-established `City_Vision_Notes/Marambio.md` canon — also corrected Belgrano's own Brazil entry). CORRECTED same day: Eocene fossil beds are geology, not a driver of population culture — Canada's fossil-culture framing walked back to honestly weak. Spain/Mexico remain honestly weak on all dimensions (not South American nations, so the shipping corridor doesn't anchor them); Italy (Juan Carlos) and Spain/Mexico (here) are now three instances of "large population, no strong anchor," still unexplained)*
- [x] Palmer City *(flagged: 43-nation roster — largest single-city undertaking in the project; PHASE 1C COMPLETE 2026-07-16 at the same Primary+Significant scope used project-wide (Notable tier deferred for every city, not a special case here) — fourth Palmer subnet city, first pass properly checked against Enneagram/Vision-Notes/Megasheet research per the new process requirement; all populations converge on one shared value (identity/felt-experience) rather than splitting function-vs-warmth; Canada/Montreal confirmed as the standout precedent)*
- [x] Port Lockroy *(PHASE 1C COMPLETE 2026-07-16 — fifth Palmer subnet city, checked against Enneagram/Vision-Notes/Megasheet research first; first city with an explicitly temporal rather than national founding tension — living memory vs. heritage spectacle; UK and France both hold outsized authenticity via different mechanisms (literal WWII history vs. structural architecture echo); Germany/Brazil/Mexico all genuinely weak with no missed corridor found on re-check)*
- [x] Rothera *(PHASE 1C COMPLETE 2026-07-16 — sixth Palmer subnet city; clearest seven-way convergence found so far, all populations land on industrial craft competence as civic pride with no meaningful counter-register; Brazil and Mexico both confirm the settlement-type-dependent rule with strong matches here after weaker showings elsewhere; source of Tepenia's own project-wide glitch-coolant "working-class" canon)*
- [x] Sejong *(PHASE 1C COMPLETE 2026-07-16 — seventh Palmer subnet city; checking Enneagram/Vision-Notes/Megasheet research surfaced a major correction — the original "8 of 9 nations weak" reading was searching for the wrong kind of match; real precedent is a shared "boundary zones" structural pattern (Izmir/Smyrna, Keelung) where all nine populations hold a genuine negotiated quarter; South Korea's namesake claim mirrors Spain's at Juan Carlos)*
- [x] Signy *(PHASE 1C COMPLETE 2026-07-16 — eighth and final Palmer subnet city; highest Primary-tier population concentration found anywhere in the project (USA 33.33%) yet the quietest civic register of any city cataloged, matching its Thinking/Withdrawn/Competency Enneagram core over its numeric dominance; fishing confirmed as dominant economy over marine-biology research; PALMER SUBNET FULLY PHASE 1C COMPLETE — see `Palmer_Subnet_Phase1c_Summary.md`)*

## Byrd Subnet
- [b] Byrd *(flagged: 35+ nations — comparable in scale to Palmer City; Phase 1b covered Primary+Significant only)*

## Other
- [ ] Concordia *(needs its own approach — population drawn from every other city, not a single founding-nation composition)*
- [ ] Amundsen Station *(low priority — small, largely robot population; revisit once the 35 cities are underway)*

## Reserved for Phase 3
- [ ] Orbital / *Cryptograph Helix* era population — not started, not scoped in detail yet
