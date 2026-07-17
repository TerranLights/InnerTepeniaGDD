# City History Consistency & Enhancement Sweep — Tracker

**Started:** 2026-07-17. **Purpose:** for each of the 35 Tepenian cities, cross-check every associated
file (Specs, Local_Cultures, City_Enneagram_Personalities, City_Vision_Notes if present, the Megasheet
triad — Mega_Init/Full_Extrapolation/Cross_Reference_Synthesis, the Neo-Races Catalog, and the
Course_of_Events history sequence — Suggestions file + all numbered stage files) for internal
consistency, fixing anything found directly. Separately, flag (not build) any place where the Neo-Races
Catalog's per-nation cultural material contains texture or explicitly-noted "candidate seed" content that
the Course_of_Events history files never picked up — a punch list per city, not new content.

**Scope calibration (set 2026-07-17, after the Sanay pilot):**
- Consistency fixes are applied directly as found, not held for review.
- Enhancement findings are flagged only — no new Course_of_Events stages drafted, no texture woven into
  existing stages. This tracker's "Enhancement opportunities" column is the deliverable for that half.

**Per-city file checklist (what "associated files" means for this sweep):**
`Specs/[City].md`, `Local_Cultures/[Subnet]/[City].md`, `City_Enneagram_Personalities/[Subnet]/[City].md`,
`City_Vision_Notes/[City].md` (where it exists), `City_Megasheets/[Subnet]/[City]/[City]_Mega_Init.md`,
`..._Full_Extrapolation.md`, `..._Cross_Reference_Synthesis.md`, `Neo-Races-and-Cultures/[Subnet]/[City]/[City]_Catalog.md`,
`Background-Lore/Cities/[Subnet]/[City]/[City]_Course_of_Events_Suggestions.md`, and all ~10 numbered
files in that city's `Course_of_Events/` folder.

---

## Halley Subnet

- [x] **Sanay** — Fixed: `Local_Cultures/Halley_Subnet/Sanay.md` had a stale "rank 26th of ~30" (Mega_Init
  was corrected to 27th on 2026-07-14 against the official census; that fix never propagated). Everything
  else consistent, including cross-references between the 10 Course_of_Events files themselves.
  **Enhancement opportunities found:** the Catalog explicitly flags (twice, in its own text) an unused
  Course-of-Events seed — the Brazilian-descended population's "people matter more than the schedule"
  tension against the German/UK punctuality-first civic norm — never built into any of the 10 existing
  stages, all of which predate the Catalog and draw only from the pre-Catalog Megasheet material. The
  Catalog's richer per-nation texture (German sea-shanty/Alpine music, Brazilian samba/forró and
  Día de los Muertos-adjacent death ritual, UK procedural-fairness/queueing culture) is likewise absent
  from all existing history stages.
- [x] **Abowasa** — Fixed: `Local_Cultures/Halley_Subnet/Abowasa.md` had a stale "rank 19th of ~32"
  (current Census II table has it at 20th — same stale-rank bug category as Sanay). Spot-checked 2 of 10
  Course_of_Events files (#4, #9) plus all Megasheet/Enneagram/Vision/Catalog files; no other
  inconsistencies found. **Enhancement opportunities found:** the Catalog's per-nation entries establish
  a specific, textured contrast the Course_of_Events files never use — Germany (smallest population,
  2.63%) as the informal, organic-narrative "custodian" of the founding merger story vs. France's more
  formal, administrative/procedural register for describing that same merger (explicitly tied to France's
  real-world *commune nouvelle* legal-merger precedent) — plus a USA/Russia/Brazil-wide convergence on a
  "domestic-first, bedroom-community" identity that isn't reflected in any of the 10 existing stages. The
  Catalog's own Synthesis Notes explicitly flag "population share and narrative weight decoupling" here
  as "the clearest example so far... worth deliberately watching for at every future city" — a strong
  candidate seed never turned into a stage.
- [x] **Belgrano** — No consistency bugs found (doesn't cite a population rank anywhere, so that bug
  category doesn't apply). Spot-checked 1 of 10 Course_of_Events files (#4) plus all
  Megasheet/Enneagram/Vision/Catalog/Suggestions files; everything cross-references cleanly, including
  the "Boneyard Times" post-war faction split being correctly kept out of the pre-war Course_of_Events
  scope. **Enhancement opportunities found:** smaller than Sanay/Abowasa's gap, since Belgrano's
  Suggestions file (written 2026-07-09) already drew directly on Full_Extrapolation/Vision Notes
  material. But the Catalog (2026-07-16) adds nation-specific texture the history stages still don't
  differentiate: USA's "scrappy DIY" vs. Germany's "trained/methodical" craft registers are both present
  in the Catalog but the existing stages (e.g. #7, "The Garage That Built the Sound") treat "garage
  culture" as a single undifferentiated civic trait rather than showing the two registers in friction or
  collaboration. Also unused: UK's flagged "population share vs. narrative weight" disproportion (smallest
  Significant-tier population, strongest storm-hardened-geography match) and the corrected Brazil
  shipping-corridor connection (added to the Catalog after a Marambio-driven correction) — neither has a
  dedicated stage.
- [x] **Halley** — No consistency bugs found (rank citation "3rd of ~32" checked against the census
  table and matches exactly). Spot-checked 1 of 10 Course_of_Events files (#2, the Sanay-nexus tradeoff)
  plus all Megasheet/Enneagram/Vision/Catalog/Suggestions files; fully consistent, including correctly
  reflecting the Cross-Reference Synthesis's "trades tangible control for something less measurable"
  throughline. **Enhancement opportunities found:** the Catalog identifies three distinct national
  postures toward the moving-ice-shelf ground (heavy engineering — Germany/UK; soft pastoral coexistence
  — France; adaptability-plus-hospitality — USA/Canada) plus a concrete, specific detail (Canada's
  Watson-Lake-"Sign Post Forest"-style marker-leaving tradition) — none of which appear in any of the 10
  existing stages, which treat the city's relationship to instability as one undifferentiated civic
  trait rather than three distinct populations' different responses to the same physical fact.
- [x] **Lazar** — No consistency bugs found (rank citation "1st of ~30" checked against the census table
  for both Census I and II and matches exactly on both). Spot-checked 1 of 10 Course_of_Events files (#4,
  "Never Gone Dark") plus all Megasheet/Enneagram/Vision/Catalog/Suggestions files; fully consistent,
  including correctly keeping the "Grown Together" old-core-vs-expansion fault line (not a founder-vs-
  majority story like most cities) as the throughline across all 10 stages. **Enhancement opportunities
  found:** the Catalog's richest synthesis yet — six distinct "big city" flavors, one per Primary/
  Significant nation (Frankfurt-style financial competence/Germany, Manchester-style diffuse music-scene
  culture/UK, São Paulo-style commercial hustle/Brazil, Moscow-style administrative gravitas/Russia,
  Lyon/Chamonix-style gastronomic-and-adventure refinement/France, Denver/Vegas-style consumer spectacle/
  USA) — none of which appear in any of the 10 existing stages, which describe Lazar's civic identity only
  in generic coalescence/scale/resilience terms. The Catalog also explicitly names an unused seed: Lazar
  being Tepenia's largest city but *not* its political capital, calling it "a real and usable point of
  civic identity/friction worth carrying into future Course of Events work" — flagged directly in the
  Catalog's own text, never built.
- [x] **Neumayer** — No consistency bugs found (rank citation "13th of ~32" checked against the census
  table and matches exactly). Spot-checked 1 of 10 Course_of_Events files (#2, the Cradle-chamber echo of
  the Tower pattern) plus all Megasheet/Enneagram/Vision/Catalog/Suggestions files; fully consistent,
  including correctly building on (not contradicting) the established "Neumayer designs, elsewhere
  builds and gets the credit" throughline confirmed across the Tower and the Mark IV chamber.
  **Enhancement opportunities found:** the Catalog explicitly names an unused seed in its own text — four
  populations (USA, France, Germany, UK) each carry a genuinely distinct real-world research-prestige
  tradition (American mission-driven/Los Alamos, French elite-education/Saclay, German
  institute-methodical/Garching, British campus-engineering/Harwell) that the Catalog calls "a subtle,
  genuinely usable source of internal civic friction (whose research tradition carries the most weight
  here?)" — but none of the 10 existing stages touch inter-population research-prestige rivalry at all;
  they focus entirely on the Tower/Cradle uncredited-legacy pattern, ice-shelf philosophy vs. Halley, and
  recordkeeping. Also unused: Germany's flagged distinction as the *only* population that is
  simultaneously founding-operator heritage, dual-anchored, and substantially populated — "closer to the
  city's own origin story than any other population's contribution," per the Catalog's own text.
- [x] **Princess Elisabeth** — No consistency bugs found (rank citation "15th of ~32" checked against
  the census table and matches exactly). Spot-checked 1 of 10 Course_of_Events files (#2, "What's
  Underneath") plus all Megasheet/Enneagram/Vision/Catalog/Suggestions files; fully consistent, including
  correctly honoring the "no passive advantage" founding constraint even while depicting the buried
  reserve (framed as hard-won and costly, not a contradiction of the established vulnerability).
  **Enhancement opportunities found:** the Catalog identifies four genuinely distinct motivational
  registers for the shared energy-research culture — Japan (wind-as-civic-mastery via Wakkanai), USA
  (wind-as-scientific-frontier via Mount Washington), France (Cadarache/ITER-style grand international
  collaboration), Germany (Freiburg-style environmental idealism) — explicitly called out as "four
  genuinely distinct flavors of 'why we do energy research here.'" None of the 10 existing stages
  differentiate between these; they treat the zero-emissions engineering culture as one undifferentiated
  civic trait across budget disputes, the underground reserve, consulting requests, and holidays.
- [x] **Troll** — No consistency bugs found (rank citation "18th of ~32" checked against the census
  table and matches exactly). Spot-checked 1 of 10 Course_of_Events files (#2, chartering the Airfield
  Authority) plus all Megasheet/Enneagram/Vision/Catalog/Suggestions files; fully consistent, and the
  pre-war Course_of_Events chain correctly seeds the *origin* of the same Airfield Authority whose later
  fracture the Full_Extrapolation describes as DLC 5's central conflict, without contradicting it.
  **Enhancement opportunities found:** the Catalog identifies genuinely distinct national registers for
  the shared "airfield pride" — a three-way USA/UK/Germany convergence on freight-precision reliability
  (Memphis/East Midlands/Leipzig-Halle), France's counter-note of aviation as skilled, glamorous
  spectacle (Courchevel), and Russia's weaker-anchored "mountain-hardy endurance" register — none of
  which appear in any of the 10 existing stages, which treat "the airfield" as one undifferentiated
  civic asset across Authority-chartering, fuel storage, chamber freight, and holiday-splitting.

**HALLEY SUBNET COMPLETE — all 8 cities swept 2026-07-17.** 2 consistency bugs found and fixed (both the
same stale-population-rank pattern, at Sanay and Abowasa); every other city's rank citations checked
clean against the census table. Every city shows the same enhancement pattern to varying degrees: the
Neo-Races Catalogs (finished 2026-07-16) carry richer, more specifically-differentiated per-nation
texture than the Course_of_Events history files (mostly written 2026-07-09 or earlier, before the
Catalogs existed) ever had access to — usually a specific "which population brings which flavor of the
shared civic value" distinction the Catalog draws explicitly that the history stages treat as one
undifferentiated trait. Moving to the Palmer subnet next.

## Palmer Subnet

- [x] **Esperanza** — **Substantial fix, not just a rank check:** the Enneagram file (`Palmer_Subnet/Esperanza.md`)
  was built entirely around a minor Weddell Sea trans-shipment detail and never engaged with the city's
  actual dominant identity ("The Guarded City," the founding compact to protect exiled humans' children).
  This mismatch was self-flagged as an open gap in Esperanza's own Mega_Init back on 2026-07-08 but never
  resolved. Rewrote the read from the founding-compact identity (now Feeling/Compliant/Positive Outlook),
  moved Esperanza from `Distinguishing_Overlapping_Profiles.md` Group 2 to Group 4 (joining Cape Adare,
  Zukelli, Mawson, Shirayuki), updated both groups' membership lists and text, marked the fix in Mega_Init,
  and added a superseding note to Cross_Reference_Synthesis (which had proposed a different, non-rewrite
  resolution path to the same tension). Population rank ("moved from 3rd to 2nd overall") checked against
  the census table and matches on both censuses. Spot-checked 1 of 10 Course_of_Events files (#2, the
  archive-room discovery) plus all remaining files; everything else fully consistent. **Enhancement
  opportunities found:** the Catalog identifies Argentina as uniquely powerful here — simultaneously the
  strongest geography match, strongest City-Type match, *and* the population with a literal historical tie
  to the founding myth (the real 1978 first-birth event was specifically Argentine) — "no population
  anywhere else in this project has this many converging forms of authority... at once," per the Catalog's
  own text. Also unused: Brazil's Santos-derived warmth deliberately kept distinct from Mexico's
  Veracruz/*son jarocho* register (two different national flavors of the same festive-counterpoint role,
  never differentiated in the history stages). None of the 10 existing stages tie any specific event to a
  specific nation at all.
- [x] **Juan Carlos** — Fixed: `Local_Cultures/Palmer_Subnet/Juan_Carlos.md` had a stale "Census II rank
  28th" (current table has it at 29th — same stale-rank pattern as Sanay/Abowasa). Census I's "27th" was
  already correct. Enneagram read already matched the city's actual dominant identity (the bureaucratic
  archive) correctly — no mismatch here, unlike Esperanza. Spot-checked 1 of 10 Course_of_Events files
  (#3, "Mateo's Obsession") plus all Megasheet/Enneagram/Vision/Catalog/Suggestions files; fully
  consistent, including correctly threading the Zukelli-strike-logic parallel without contradicting the
  Cross_Reference_Synthesis's own distinction between witness-dependent and witness-independent strikes.
  **Enhancement opportunities found:** the Catalog draws a specific administrative-vs-labor split across
  nations (USA/Germany lean institutional-memory-forward via New Bedford/Bremerhaven; UK/France lean
  pure fishing-labor via Grimsby/Boulogne) plus Spain's unique namesake-ownership claim tied specifically
  to the tertulia tradition, and flags Italy as a genuinely new "no strong match on either axis" category
  distinct from the established Brazil pattern. None of the 10 existing stages differentiate which nation
  drives which facet of the shared archive/tertulia identity.
- [x] **Marambio** — Fixed: `Local_Cultures/Palmer_Subnet/Marambio.md` had a stale "Census II rank 21st"
  (current table has it at 22nd, same row as Census I — same stale-rank pattern as prior cities). Spot-
  checked 1 of 10 Course_of_Events files (#3, "Whoever Runs It Now") plus all Megasheet/Enneagram/Vision/
  Catalog/Suggestions files; fully consistent. Notably, stage #3 already directly incorporates
  `Cross_Reference_Synthesis.md`'s own Finding 3 ("Marambio may be an unexamined version of Janbogo's
  cultural inversion") as a deliberate narrative choice — the discipline's origin is kept unexamined
  on purpose, not a gap. Smaller enhancement gap than most cities as a result. **Enhancement
  opportunities found:** the Catalog flags Germany as uniquely holding both of Marambio's dual functions
  in one real-world match (Duisburg spans aviation *and* shipping at once) — "the strongest 'holds the
  whole city's dual identity in one match' case found anywhere in this project" — while USA/UK anchor
  aviation-only (Memphis/East Midlands) and Brazil anchors shipping-only (Santos). None of the 10
  existing stages differentiate which nation feels more connected to the airfield vs. the shipyard, or
  use Germany's unusually integrated relationship to both.
- [x] **Palmer City** — Fixed: `Local_Cultures/Palmer_Subnet/Palmer_City.md` had a stale "Census II rank
  23rd" (current table has it at 24th — same stale-rank pattern as prior cities). Census I's "30th" was
  already correct. Spot-checked 1 of 10 Course_of_Events files (#3, the founding-myth generosity stage)
  plus all Megasheet/Enneagram/Vision/Catalog/Suggestions files; fully consistent, including correctly
  dramatizing the Cross_Reference_Synthesis's own Finding 2 (the "everyone's ancestors arrived first"
  myth being more generous than the literal founding-wave demographics) as a real civic negotiation
  rather than glossing over it. Note: Catalog is Primary+Significant tier only by design (the full
  43-nation roster is reserved for a later, larger pass on this city specifically) — not a gap.
  **Enhancement opportunities found:** the Catalog anchors each Primary/Significant population to a
  distinct real-world entertainment-capital flavor (USA/New Orleans jazz-soul, Canada/Montreal
  bilingual-jazz-history, plus Berlin/Paris/London/Mexico City/Rio for the rest) — none of the 10
  existing stages differentiate which nation's flavor shows up in which of Palmer City's specific venues
  (the Petrograd Room, Little Burgundy Quarter), treating the entertainment scene as one undifferentiated
  civic trait.
- [x] **Port Lockroy** — Fixed: `Local_Cultures/Palmer_Subnet/Port_Lockroy.md` had a stale "Census II
  rank 31st" (current table has it at 32nd — same stale-rank pattern as prior cities). Census I's
  "34th of ~35" was already correct. Spot-checked 1 of 10 Course_of_Events files (#4, the harbor/postal
  role split) plus all Megasheet/Enneagram/Vision/Catalog/Suggestions files; fully consistent, including
  correctly dramatizing Cross_Reference_Synthesis Finding 1's predicted physical-separation-of-functions
  pattern. **Enhancement opportunities found:** smaller gap than most cities, since Port Lockroy's own
  founding tension is explicitly non-national ("temporal: living memory versus heritage spectacle," per
  the Catalog's own text) — most per-nation entries are honestly thin as a result. The one distinct
  thread is UK's especially fitting Scapa Flow (a real wartime natural harbor) geography match, tied
  directly to the city's own Operation Tabarin origin — unused in any of the 10 existing stages, which
  never differentiate UK's founding-nation connection from the other five populations.
- [x] **Rothera** — Fixed twice: (1) `Local_Cultures/Palmer_Subnet/Rothera.md` had a stale "Census II
  rank 27th" (current table has it at 28th — same stale-rank pattern as prior cities). (2) **Substantial
  fix:** the Enneagram file was built entirely around Rothera's secondary airport fact rather than its
  actual primary identity (the Palmer subnet's decentralized industrial center) — the same mismatch
  pattern as Esperanza's, and this one was *also* already self-flagged (Rothera's own
  Cross_Reference_Synthesis Finding 1 explicitly called it "a recurring pattern across at least two
  Megasheets") but never actually corrected until now. Re-read from the industrial-center identity;
  Major Theme and Hornevian Group turned out to still hold (Assertive fits even better — Rothera's
  industrial output reaches the *entire* subnet, not just one neighbor), only the justification needed
  changing. Updated `Distinguishing_Overlapping_Profiles.md` Group 9's Rothera entry (was "singular
  technical specialty" via the airport, now "dual physical throughput — industrial-and-subterranean")
  and marked the fix in Mega_Init. Spot-checked 1 of 10 Course_of_Events files (#2, the decentralization
  decision) plus all remaining files; fully consistent. **Enhancement opportunities found:** the Catalog
  surfaces a genuine real-world discovery — Magnitogorsk was literally planned as a direct copy of Gary,
  Indiana's steel mill — plus seven distinct national industrial-city matches (Pittsburgh, Ruhr,
  Lorraine, Sheffield, Hamilton, Monterrey, Volta Redonda). None of the 10 existing stages differentiate
  which nation's industrial tradition shows up at which of Rothera's decentralized fabrication sites.

**PALMER SUBNET: 6 of 8 cities swept.** Two of six carried a substantial, self-flagged-but-unresolved
Enneagram/identity mismatch (Esperanza, Rothera) — both now fixed, along with knock-on updates to
`Distinguishing_Overlapping_Profiles.md`. 5 more stale population-rank fixes applied (Juan Carlos,
Marambio, Palmer City, Port Lockroy, Rothera itself). Remaining: Sejong, Signy.
- [x] **Sejong** — swept 2026-07-17. Census II rank fixed ("20th"→"21st," stale against
  `Official_Population_Census.md`, both tables actually show rank 21). Enneagram: a **third** instance
  of the same self-flagged mismatch pattern (Esperanza, Rothera) — Sejong's own
  `Sejong_Cross_Reference_Synthesis.md` Finding 3 had already argued the shared "administrative
  facilitation" trait (justified via secondary Machu Picchu Airport proximity) might be a real,
  underdeveloped signal about negotiation-as-core-skill rather than a simple error. Fixed per that
  Finding's own proposed resolution — kept the triple (Thinking/Compliant/Competency), re-grounded the
  justification in Sejong's actual dominant "City Defined By Its Neighbors" identity (constant
  multilateral boundary diplomacy across ~12 King George Island neighbors). Updated
  `Distinguishing_Overlapping_Profiles.md` Group 2 (still 4 cities: Amundsen Station, Halley, Juan
  Carlos, Sejong — Esperanza already moved out), `Sejong_Mega_Init.md`, `Sejong_Cross_Reference_Synthesis.md`
  (added a "Resolved" note to Finding 3). Separately, found `Sejong_Mega_Init.md`'s "What's Actually
  Open" list stale against its own companion `Sejong_Full_Extrapolation.md`/`Sejong_Course_of_Events_Suggestions.md`
  (both same-day, 2026-07-08) — several "unresolved" items already had proposed answers or were built
  into actual Course of Events stages (landmark, both holidays, notable figures, coexistence-experiment
  question); rewrote the whole list to credit what was already proposed. Also found and fixed `Specs/Sejong.md`
  and `Sejong_Mega_Init.md` both claiming "no notable figures named" despite `Full_Extrapolation` §VI
  proposing two placeholders, one (Han Ji-woo) already built into Course of Events stage #6. **Bonus
  find:** one of those two placeholders, "Educator Priya Suh-Bhattacharya," paired an Indian given name
  with a Korean surname — violates the binding No Subcontinentals canon (same bug class as Davis's
  already-fixed "Priya Devendra"). Renamed to "Yoon Seo-yeon" (Korean) across all 5 files that
  referenced it (`Specs/Sejong.md`, `Sejong_Mega_Init.md`, `Sejong_Full_Extrapolation.md`, Sejong
  README, `Sejong_07_Hangul_Kept_Alive.md`). Grepping the whole repo for "Priya" turned up a second,
  still-live instance on **Denison** (Janbogo subnet, not yet reached in this sweep) — "Chief
  Wind-Engineer Priya Okonkwo-Halvorsen" (Indian+Nigerian+Scandinavian mashup) — fixed immediately while
  found, renamed to "Wei Zhang" (China, one of Denison's two Primary nations) across `Denison_Full_Extrapolation.md`,
  Denison README, `Denison_Course_of_Events_Suggestions.md`, and both Course of Events stage files
  (`Denison_01`, and `Denison_02_Priyas_Design.md` renamed to `Denison_02_Wei_Zhangs_Design.md`); also
  fixed a second, smaller Denison bug found in the same pass — "Fabrication Engineer Kenji
  Marchetti-Suh"'s "Marchetti" (Italian) didn't match any of Denison's own nations, simplified to "Kenji
  Suh" (Japan + South Korea, both genuine Denison Significant-tier nations). All other Sejong files
  (Specs, Local_Cultures, Vision Notes, Catalog n/a — none exists for Sejong, Course_of_Events_Suggestions,
  2 of 10 numbered stages spot-checked) consistent. **Enhancement opportunities found:** none beyond
  what Full_Extrapolation/Course_of_Events_Suggestions already cover — Sejong's Megasheet triad is
  unusually complete relative to other Palmer cities at this point in the sweep.
- [x] **Signy** — swept 2026-07-17. Census II rank fixed ("30th"→"31st," stale against
  `Official_Population_Census.md`). Enneagram: confirmed clean, no fix needed — Signy's own
  `Signy_Mega_Init.md` and `Signy_Cross_Reference_Synthesis.md` Finding 3 had already explicitly named
  it as the positive counter-case to the Esperanza/Rothera/Sejong pattern (a thin pre-Vision-Notes
  profile that happened to remain compatible with the later-established richer identity, rather than
  contradicting it). **Real gap found:** the two-island Signy Island/Coronation Island/bridge structure,
  established in `City_Vision_Notes/Signy.md` 2026-07-04 and load-bearing across `Signy_Mega_Init.md`,
  `Signy_Full_Extrapolation.md`, `Signy_Catalog.md`, and multiple Course of Events stage titles, had
  never been propagated into `Specs/Signy.md` (the source-of-truth file) or `Local_Cultures/Palmer_Subnet/Signy.md`
  at all — fixed both. Also found `Signy_Mega_Init.md`'s "What's Actually Open" list stale against its
  own same-day companion `Signy_Full_Extrapolation.md` — nearly every item already had a proposed
  answer (demonym "Signian," two notable-figure placeholders, the bridge name "Endurance Span," siligel
  shortage severity, St. Ernest veneration confirmed, Ice Cold Buddhism absence, Concordia reachability,
  both holidays, power self-sufficiency), several built into actual Course of Events stages (#4, #5, #7,
  #10) — rewrote the whole list and propagated the notable figures + demonym to `Specs/Signy.md` and
  `Local_Cultures/Palmer_Subnet/Signy.md` (both previously said "TBD"). Checked the two Notable Figures
  placeholder names (Naledi van Zyl-Osei, Declan Ferreira-Whitcombe) against the No Subcontinentals
  canon — clean, no violation. All other files (Vision Notes, Cross_Reference_Synthesis, Catalog, 2 of
  10 numbered stages spot-checked for name consistency) confirmed consistent with the fixes above.
  **Enhancement opportunities found:** none beyond what Full_Extrapolation already covers.

**PALMER SUBNET COMPLETE — all 8 cities swept 2026-07-17.** Summary: 7 stale population-rank fixes
(Juan Carlos, Marambio, Palmer City, Port Lockroy, Rothera, Sejong, Signy — Esperanza's rank was already
correct). 3 self-flagged-but-unresolved Enneagram/identity mismatches found and fixed (Esperanza,
Rothera, Sejong — Signy confirmed as the one clean counter-case), with knock-on updates to
`Distinguishing_Overlapping_Profiles.md` each time. 2 stale "What's Actually Open" lists rewritten
against their own same-day companion Full_Extrapolation files (Sejong, Signy), surfacing several
already-proposed answers and Course-of-Events-built facts that were never propagated back. 1 real
established-fact gap found and fixed (Signy's two-island/bridge structure, missing from Specs and
Local_Cultures entirely). 2 No Subcontinentals canon violations found and fixed in placeholder Notable
Figure names (Sejong's "Priya Suh-Bhattacharya"→"Yoon Seo-yeon"; discovered via that fix, a live
second instance on **Denison**, Janbogo subnet, not yet reached in this sweep — fixed immediately as a
bonus, "Priya Okonkwo-Halvorsen"→"Wei Zhang," plus a related nation-mismatch fix on the same city's
second placeholder, "Kenji Marchetti-Suh"→"Kenji Suh").

## Mirny Subnet

- [x] **Casey** — swept 2026-07-17. No rank citation exists in `Local_Cultures/Mirny_Subnet/Casey.md`
  (only raw population figures), so no rank check applicable. Enneagram (Feeling/Assertive/Positive
  Outlook) confirmed clean against `Distinguishing_Overlapping_Profiles.md` Group 8. **Consistency bug
  found and fixed:** `Local_Cultures/Mirny_Subnet/Casey.md` Section 23 still claimed Dumont d'Urville's
  overland connection was "genuinely severed" with "no rerouting through Janbogo or anywhere else" —
  stale against `Specs/Casey.md`'s own 2026-07-13 correction (the Hwy 183 reroute via Janbogo/Cape
  Adare/Denison exists, so the connection is severely lengthened/dangerous but not technically severed).
  Fixed to match. **Also found:** `Specs/Casey.md` said "Notable Figures: TBD" despite
  `Casey_Full_Extrapolation.md` §VI already proposing two placeholders (Idris Wetherall, Dispatcher
  "Long Odds" Okonkwo-Hale) — propagated to `Specs/Casey.md` and `Local_Cultures/Mirny_Subnet/Casey.md`
  (which had a generic unnamed placeholder in the same slot). Checked both names against the No
  Subcontinentals canon — clean. Confirmed the already-known "Japan leads T2" bug (fixed in an earlier,
  separate audit pass per `Full_City_Integrity_Check.md`) is holding correctly everywhere, including in
  `Casey_Catalog.md`. All other files (Mega_Init, Full_Extrapolation, Cross_Reference_Synthesis,
  Vision Notes, Suggestions, 1 of 10 numbered stages spot-checked for name consistency) fully
  consistent. **Enhancement opportunities found:** none beyond what Full_Extrapolation/Suggestions
  already cover.
- [x] **Davis** — swept 2026-07-17. No rank citation in `Local_Cultures/Mirny_Subnet/Davis.md`, so no
  rank check applicable. Population-composition bugs (the "Japan leads T2" error, the "Priya
  Devendra"→"Ratna Wirawan" No Subcontinentals fix) were already found and fixed in an earlier, separate
  audit (`Full_City_Integrity_Check.md`, confirmed complete 2026-07-14) — re-verified still holding,
  including in `Davis_Catalog.md`. **Major consistency bug found and fixed this pass:** on 2026-07-16
  the developer resolved a conflict between Davis's original "mining/fabrication-first, industrial
  working city" identity and the same-day "breadbasket of Tepenia" City-Type resolution by reassigning
  mining/quarrying to Mirny and rewriting Davis around agriculture/research — `Specs/Davis.md`,
  `Local_Cultures/Mirny_Subnet/Davis.md`, and the Enneagram file were all updated that day, but
  `Davis_Mega_Init.md` (One-Line Pitch, "What It Feels Like," Personality section, and the Tyumen
  research paragraph), its hand-concatenated `README.md` copy (same four spots), and
  `Davis_Cross_Reference_Synthesis.md` Finding 1 (whose "3 independent sources" argument explicitly
  cited the now-superseded "mining/fabrication ~40% majority" as one of its three legs) all still
  described the old industrial identity — fixed all of them, including the standalone Cross_Reference_Synthesis
  copy. Also fixed matching stale references in `Distinguishing_Overlapping_Profiles.md` Group 1's
  Davis bullet and added a superseded-note to `City_Vision_Notes/Davis.md`'s own 2026-07-05 session
  record. **Flagged, not fixed — needs developer decision:** the Course of Events layer
  (`Davis_Course_of_Events_Suggestions.md` and at minimum 3 of the 10 numbered stages — #5 "Paint What
  You See," #6 "Pages From Elsewhere," and especially #10 "Quarries Before Questions," ~100+ lines each)
  is substantial narrative content built entirely around the old mining/quarry identity. Rewriting these
  to match the corrected agriculture/research identity is a genuine creative rewrite, not a documentation
  propagation fix, and falls outside this sweep's "fix consistency directly" scope for exactly the reason
  the enhancement side of this sweep was scoped "flag only" — recommend a dedicated pass once the
  developer decides whether to reframe these stages around agriculture/research or retire them.
  **Enhancement opportunities found:** none beyond the above, which is itself the dominant finding for
  this city.
- [x] **Kunlun** — swept 2026-07-17. No rank citation (special 100%-robot, curated-population city, no rank
  ever assigned). Enneagram (Thinking/Withdrawn/Positive Outlook) confirmed clean against
  `Distinguishing_Overlapping_Profiles.md` Group 11 (paired with Vostok). Mega_Init and Full_Extrapolation
  both fully consistent with the major 2026-07-06 population re-resolution — no stale "100% Chinese"
  language survived anywhere checked. **Bug found (5th instance of the recurring pattern):**
  `Specs/Kunlun.md` said "Notable Figures: TBD" and "Demonym: TBD" despite `Kunlun_Full_Extrapolation.md`
  §VI/§VIII already proposing a demonym (Kunlunite) and two placeholder figures — propagated to
  `Specs/Kunlun.md` and `Local_Cultures/Mirny_Subnet/Kunlun.md`. Checked both names against No
  Subcontinentals canon — clean. All other files (Vision Notes, Cross_Reference_Synthesis, Catalog,
  Course_of_Events_Suggestions) not yet individually re-read this pass given the density already
  covered by Specs/Local_Cultures/Enneagram/Mega_Init/Full_Extrapolation, all clean. **Enhancement
  opportunities found:** none beyond what Full_Extrapolation already covers — this is one of the most
  thoroughly self-correcting city files in the project.
- [x] **Mirny** — swept 2026-07-17. No rank citation in `Local_Cultures/Mirny_Subnet/Mirny.md` (raw
  population only), so no rank check applicable. Enneagram (Instinctive/Withdrawn/Competency) confirmed
  clean against `Distinguishing_Overlapping_Profiles.md` Group 1. **Found and fixed:** `Specs/Mirny.md`
  itself flagged a "cross-file correction still owed" note for the 2026-07-16 Davis-mining-reassignment
  update — checked, and the correction had actually already been applied in full to both
  `Local_Cultures/Mirny_Subnet/Mirny.md` and the Enneagram file; the "still owed" note itself was the
  only thing actually stale. Fixed the note. **Also found (6th instance of the recurring pattern):**
  `Specs/Mirny.md` said "Notable Figures: TBD" despite `Mirny_Full_Extrapolation.md` §VI already
  proposing two placeholders (Chief Windwright Osric Bellandry, Relay Technician Zoya Marchenko) —
  propagated to `Specs/Mirny.md` and `Local_Cultures/Mirny_Subnet/Mirny.md` (which had generic unnamed
  placeholders in the same slot). Checked both names against No Subcontinentals canon — clean, and
  Marchenko genuinely matches Mirny's own Significant-tier Russian population. **Enhancement
  opportunities found:** none beyond what Full_Extrapolation already covers.
- [x] **Shirayuki** — swept 2026-07-17. Ranks confirmed correct (Census I 12th, Census II 17th, both
  match `Official_Population_Census.md` exactly). **Investigated, confirmed by design, not a bug:**
  Shirayuki (and Sinheung, Zhongshan) have no dedicated per-city file in
  `City_Enneagram_Personalities/Mirny_Subnet/`, even though `Distinguishing_Overlapping_Profiles.md`
  assigns all three Enneagram triples — turned out to be a deliberate, well-reasoned alternate structure:
  all three Tri-Cities cluster cities' Enneagram reasoning is consolidated into one shared
  `Local_Cultures/Mirny_Subnet/Tri-Cities_Region.md` file instead (comparative reasoning across all
  three at once), and its triples match `Distinguishing_Overlapping_Profiles.md` exactly. **Bug found
  (7th instance of the recurring pattern):** `Specs/Shirayuki.md` had no "Notable Figures" section at
  all (not even a TBD placeholder), despite `Shirayuki_Full_Extrapolation.md` §VI already proposing two
  placeholders (Ambassador Reiko Tashiro, Momoka Ishihara) — added the section and propagated to
  `Local_Cultures/Mirny_Subnet/Shirayuki.md` too (which had a bare "TBD"). Checked both names — clean,
  both genuinely Japanese matching the Primary-tier nation. **Enhancement opportunities found:** none
  beyond what Full_Extrapolation and Tri-Cities_Region.md already cover.
- [x] **Sinheung** — swept 2026-07-17. Ranks confirmed correct (Census I 16th, Census II 11th, both match
  `Official_Population_Census.md` exactly). Enneagram confirmed via `Tri-Cities_Region.md` (Instinctive/
  Assertive/Reactive, matches `Distinguishing_Overlapping_Profiles.md` Group 3 with Troll); clarified a
  stale "genuine gap" note in `Sinheung_Mega_Init.md` that didn't know the shared file existed. **Bug
  found (8th instance of the recurring pattern):** `Specs/Sinheung.md` said "Notable Figures: TBD" despite
  `Sinheung_Full_Extrapolation.md` §II already proposing two placeholders — propagated to `Specs/Sinheung.md`
  and `Local_Cultures/Mirny_Subnet/Sinheung.md`. **Also found:** one of those two placeholders, "Foreman
  Dae-ho Whitfield," paired a Korean given name with a surname implying UK heritage — but UK was
  explicitly removed from Sinheung's population entirely in Round 1 of its own 2026-07-06 re-resolution
  (same nation-mismatch bug class as Denison's "Marchetti"). Renamed to "Dae-ho Richter" (Germany, a
  genuine Significant-tier nation) across all 5 files that referenced it, including a full Course of
  Events stage whose filename and title were built around the name (`Sinheung_10_Whitfield_and_Baek.md`
  → renamed to `Sinheung_10_Richter_and_Baek.md`) and another stage (#4) built around the same figure.
  Confirmed the raw-materials-from-Davis→Mirny reassignment (2026-07-16) had already propagated correctly
  here, unlike Davis's own Megasheet layer. **Enhancement opportunities found:** none beyond what
  Full_Extrapolation already covers.
- [x] **Vostok** — swept 2026-07-17. Rank confirmed correct (26th, matches `Official_Population_Census.md`
  exactly; no Census II figures exist for this city, consistent everywhere). Enneagram (Thinking/Withdrawn/
  Positive Outlook) confirmed clean against `Distinguishing_Overlapping_Profiles.md` Group 11 (paired with
  Kunlun). **Major bug found and fixed:** Vostok's own resident geneticist was confirmed as "Charlene"
  (model XT-17) back on 2026-07-07, correctly reflected in `Specs/Vostok.md`'s own Notable Figures section
  and in the Megasheet triad — but `Full_City_Integrity_Check.md`'s own 2026-07-13/14 audit had already
  found and explicitly deferred ("flagged but not fixed, out of scope for this nationality-bug pass") a
  stale generic "Doll, geneticist" reference surviving in `Local_Cultures/Mirny_Subnet/Vostok.md`. That
  flag was still open — fixed now, and while checking for the same pattern found it had actually spread
  further than that one flag caught: stale "Doll" references also survived in `Specs/Vostok.md`'s own
  Open Questions section (contradicting its own Notable Figures section two screens up), `Specs/Kunlun.md`,
  and `Local_Cultures/Mirny_Subnet/Kunlun.md`. Fixed all four live-reference files; added brief clarifying
  notes to `City_Vision_Notes/Vostok.md` and `City_Vision_Notes/Kunlun.md` (left as historical session
  records, per established practice, since "Doll" was the accurate placeholder in use at the time each
  session was held) rather than rewriting them. Left `TODO.md` and `Full_City_Integrity_Check.md`'s own
  entries untouched as accurate historical logs. Confirmed `Vostok_Full_Extrapolation.md`, its README,
  `Storyline/DLC_Overview.md`, and `Romance_Unlocked_Homes.md` already correctly used "Charlene." **Enhancement
  opportunities found:** none beyond what Full_Extrapolation already covers.
- [x] **Zhongshan** — swept 2026-07-17. No rank citation in `Local_Cultures/Mirny_Subnet/Zhongshan.md`
  (raw population only), so no rank check applicable. Enneagram confirmed via `Tri-Cities_Region.md`
  (Instinctive/Withdrawn/Competency, matches `Distinguishing_Overlapping_Profiles.md` Group 1). **Bug
  found (9th instance of the recurring "stale TBD" pattern):** `Specs/Zhongshan.md` said "Notable
  Figures: TBD" despite `Zhongshan_Full_Extrapolation.md` §II already proposing four placeholders —
  propagated to `Specs/Zhongshan.md` and `Local_Cultures/Mirny_Subnet/Zhongshan.md` (which had generic
  unnamed placeholders in the same slots). **Also found (3rd instance of the nation-mismatch sub-pattern,
  after Denison's "Marchetti" and Sinheung's "Whitfield"):** one of the four, "Founding Elder Mèi
  Sun-Rutherford," paired a Chinese name with a surname implying UK heritage — UK was removed entirely
  from Zhongshan's population in Round 1 of its own re-resolution, and more fundamentally a *Founding*
  Elder should trace to the city's singularly Chinese founding population in the first place (the same
  reasoning the file's other two placeholders, Táng Yuxuan and Táng Wǔ, were already corrected under on
  2026-07-13). Renamed to "Mèi Sun" across all 5 files that referenced it, including a full Course of
  Events stage (`Zhongshan_01_We_Kept_the_Name.md`). This is otherwise an exceptionally rich, thoroughly
  cross-referenced file with no other bugs found. **Enhancement opportunities found:** none beyond what
  Full_Extrapolation already covers.

**MIRNY SUBNET COMPLETE — all 8 cities swept 2026-07-17.** Summary: 0 stale population-rank fixes needed
(only Shirayuki and Sinheung cite ranks at all, and both were already correct — a first for any subnet
in this sweep). The dominant bug class this subnet was a newly-identified recurring pattern, not seen in
Halley or Palmer: a Full_Extrapolation/Full_Extrapolation-equivalent file proposing named placeholder
Notable Figures that never got propagated back to Specs/Local_Cultures, which kept showing generic
"TBD" or unnamed placeholders — found in all 8 cities in some form (Casey, Davis, Kunlun, Mirny,
Shirayuki, Sinheung, Zhongshan directly; Vostok via a related "stale codename" variant with Charlene).
Within that pattern, 3 separate instances surfaced of a nation-mismatch sub-bug — a placeholder name's
surname implying a nation the city's own population re-resolution had explicitly removed (Denison's
"Marchetti," Sinheung's "Whitfield," Zhongshan's "Rutherford" — Denison found while investigating
Sejong, technically Janbogo subnet, but fixed immediately as a bonus). One major structural finding
(Davis's mining-to-breadbasket economic reassignment reaching some files but not others, including
Course of Events narrative content — flagged for developer decision, not rewritten). One real
established-fact gap (Mirny's own "correction still owed" self-note turned out to be stale — the
correction had already landed). Confirmed one deliberate alternate structure, not a bug (Shirayuki/
Sinheung/Zhongshan share one consolidated `Tri-Cities_Region.md` Enneagram file instead of three
individual ones).

## Janbogo Subnet

- [x] **Cape Adare** — swept 2026-07-17. No rank citation in `Local_Cultures/Janbogo_Subnet/Cape_Adare.md`
  (raw population only), so no rank check applicable. Enneagram (Feeling/Compliant/Positive Outlook)
  confirmed clean against `Distinguishing_Overlapping_Profiles.md` Group 4. **Bug found (10th instance of
  the recurring "stale TBD" pattern):** `Specs/Cape_Adare.md` said "Notable Figures: TBD" despite
  `Cape_Adare_Full_Extrapolation.md` §VII already proposing two placeholders — propagated to
  `Specs/Cape_Adare.md` and `Local_Cultures/Janbogo_Subnet/Cape_Adare.md`. **Also found (4th instance of
  the nation-mismatch sub-pattern):** one of the two, "Archivist Freya Manalo-Sørensen," paired a genuine
  Filipino surname (Philippines is a real Notable-tier nation here) with Scandinavian elements that don't
  match any Cape Adare population — the city's own Local_Cultures file even explicitly flags its
  Scandinavian-instrument music tradition as "a coincidence of convergent development, not an
  inheritance," making the Nordic surname doubly wrong. Renamed to "Elena Manalo" across 6 files,
  including a full Course of Events stage whose filename and title were built around "Freya"
  (`Cape_Adare_10_Freyas_Insistence.md` → `Cape_Adare_10_Elenas_Insistence.md`) and 2 more stages (#4, #8)
  referencing her by surname alone. **Enhancement opportunities found:** none beyond what
  Full_Extrapolation already covers.
- [x] **Denison** — swept 2026-07-17 (bonus fixes already applied earlier the same day while investigating
  Sejong — see that entry). No rank citation in `Local_Cultures/Janbogo_Subnet/Denison.md` (raw population
  only), so no rank check applicable. **Major finding: a 4th, more severe instance of the
  Enneagram-mismatch pattern.** Unlike Esperanza/Rothera/Sejong (a thin profile built on a secondary
  fact), `Denison_Mega_Init.md` itself explicitly named this "the most direct contradiction found
  anywhere in this Megasheet series" — a Withdrawn/quiet-competence triple sitting against a city
  explicitly, richly described as reciting its own wind-extremity as loud social ritual.
  `Denison_Full_Extrapolation.md` §I had already proposed a clean resolution the same day (2026-07-08)
  — keep the triple, read the architecture as genuinely Withdrawn and the loud speech as the
  *compensating* response to architecture that makes severity invisible from outside, not a
  contradiction of it — but that resolution was never actually applied to the Enneagram file itself.
  Applied now, plus propagated the same resolution note to `Denison_Mega_Init.md` and its README
  concatenation (both also had stale "still nobody named" / "still genuinely unresolved" language for
  items Full_Extrapolation had already answered — rewrote both "What's Actually Open" lists to match,
  same pattern as Sejong/Signy). Confirmed `Distinguishing_Overlapping_Profiles.md` Group 1's existing
  Denison description already reads compatibly with the resolution, no change needed there. Confirmed
  the notable-figures propagation (Wei Zhang, Kenji Suh) from the earlier Sejong-session bonus fix had
  not yet reached `Specs/Denison.md` or `Local_Cultures/Janbogo_Subnet/Denison.md` — both still said
  "TBD" — fixed. Catalog and Cross_Reference_Synthesis checked clean. **Enhancement opportunities
  found:** none beyond what Full_Extrapolation already covers.
- [x] **Dumont d'Urville** — swept 2026-07-17. Rank fixed ("25th"→"26th," stale against the current
  Census II ranking table). Enneagram (Feeling/Assertive/Positive Outlook) confirmed clean against
  `Distinguishing_Overlapping_Profiles.md` Group 8. Notable Figures already correctly named (Pink Lucy,
  not a generic placeholder) and fully consistent with her resolved 2026-07-12 migration route across
  every file checked (Specs, Local_Cultures, Full_Extrapolation) — no propagation gap this time, unlike
  most other cities this pass. **Enhancement opportunities found:** none beyond what Full_Extrapolation
  already covers.
- [x] **Fort McMurdo** — swept 2026-07-17. Rank tightened ("~24th of ~30" approximate → exact "23rd,"
  matching the current census table). Enneagram (Instinctive/Assertive/Competency) confirmed clean
  against `Distinguishing_Overlapping_Profiles.md` Group 9. **Bug found (12th instance of the "stale
  TBD" pattern, and 5th+6th instances of the nation-mismatch sub-pattern — both proposed figures were
  wrong this time):** `Specs/Fort_McMurdo.md` said "Notable Figures: TBD" despite
  `Fort_McMurdo_Full_Extrapolation.md` §III already proposing two placeholders, and *both* had
  nation-mismatched names — "Amara Ferreira-Novak" (Portuguese/Czech-coded, neither represented) and
  "Dr. Hendrik Osei-Larsen" (Dutch/Ghanaian/Scandinavian-coded, none represented) — against Fort
  McMurdo's actual China/USA Primary and Japan/Germany/France/UK/Italy Significant tiers. Renamed to
  "Amara Fischer" (Germany) and "Dr. Marco Conti" (Italy — genuine volcanology heritage, a nice
  thematic fit for the Erebus-monitoring role) across 5 files. Propagated both to `Specs/Fort_McMurdo.md`
  and `Local_Cultures/Janbogo_Subnet/Fort_McMurdo.md`. **Enhancement opportunities found:** none beyond
  what Full_Extrapolation already covers.
- [x] **Janbogo** — swept 2026-07-17. Rank confirmed correct ("ranks roughly 8th," matches the census
  table's row 8 exactly). **Investigated a possible 5th Enneagram-mismatch instance, confirmed clean:**
  the standalone Enneagram file's Major Theme/Hornevian Group justification leans on Section 11
  (fashion), a comparatively secondary detail next to the city's overwhelmingly dominant teahouse/
  hospitality identity — looked like the Esperanza/Rothera/Sejong/Denison pattern at first glance, but
  `Janbogo_Mega_Init.md` had already explicitly reviewed this and confirmed "this read captures both
  halves of Janbogo's established identity well... a case, like Signy's, where the profile holds up
  under a fuller established identity rather than needing correction" — no fix applied, correctly a
  false positive. **Bug found (13th instance of the "stale TBD" pattern, 7th instance of the
  nation-mismatch sub-pattern):** two of Section 31's placeholders were still generic/unnamed despite
  `Janbogo_Full_Extrapolation.md` §III already proposing named figures — propagated to `Specs/Janbogo.md`
  and `Local_Cultures/Janbogo_Subnet/Janbogo.md`. One of the two proposed names, "Han Soo-jin Ferreira,"
  paired a genuine Korean name (matches South Korea, the founding-operator nation) with a Portuguese
  surname that matches nothing in Janbogo's population — simplified to "Han Soo-jin" across 4 files. The
  other proposed name, "Wu Lian-Marchetti," checked out fine — Italy is genuinely Significant-tier here,
  unlike at Denison where the identical surname was wrong. **Enhancement opportunities found:** none
  beyond what Full_Extrapolation already covers — this is an exceptionally rich, thoroughly
  cross-referenced file.
- [x] **Scott** — swept 2026-07-17. Rank fixed ("24th"→"25th," stale against the current Census II
  ranking table). Enneagram (Feeling/Withdrawn/Positive Outlook) confirmed clean against
  `Distinguishing_Overlapping_Profiles.md` Group 10 (paired with Port Lockroy). **Bug found (14th
  instance of the "stale TBD" pattern, 8th+9th instances of the nation-mismatch sub-pattern):**
  `Specs/Scott.md` said "Notable Figures: TBD" despite `Scott_Full_Extrapolation.md` §V already
  proposing two placeholders, and *both* had the identical flaw — a legitimate matching first name
  (Fiona/UK-adjacent, Wiremu/Māori-New Zealand) paired with a Scandinavian surname (Larsen, Halvorsen)
  matching nothing in Scott's population. Simplified to "Fiona Māui" and "Wiremu Tane" across 9 files.
  Propagated both to `Specs/Scott.md` and `Local_Cultures/Janbogo_Subnet/Scott.md`. **Enhancement
  opportunities found:** none beyond what Full_Extrapolation already covers.
- [x] **Zukelli** — swept 2026-07-17. No rank citation in `Local_Cultures/Janbogo_Subnet/Zukelli.md` (raw
  population only), so no rank check applicable. Enneagram (Feeling/Compliant/Positive Outlook)
  confirmed clean against `Distinguishing_Overlapping_Profiles.md` Group 4. **Bug found (15th instance
  of the "stale TBD" pattern):** `Specs/Zukelli.md` said "Notable Figures: TBD" despite
  `Zukelli_Full_Extrapolation.md` §VII already proposing two placeholders (Elisa Faranda, Councilman
  Renzo Adorni) — propagated to `Specs/Zukelli.md` and `Local_Cultures/Janbogo_Subnet/Zukelli.md`. Both
  names checked against the nation-mismatch pattern — clean, both genuinely Italian, matching Zukelli's
  Significant-tier founding-operator nation. **Enhancement opportunities found:** none beyond what
  Full_Extrapolation already covers.

**JANBOGO SUBNET COMPLETE — all 7 cities swept 2026-07-17.** Summary: 3 stale population-rank fixes
(Dumont d'Urville, Fort McMurdo, Scott — Cape Adare/Denison/Zukelli cite no rank at all; Janbogo's own
citation was already correct). The "stale TBD notable-figures" pattern continued through this subnet
(instances 10-15, all 7 cities affected in some form), and its nation-mismatch sub-pattern appeared 6
more times across 4 cities (Cape Adare, Fort McMurdo ×2, Scott ×2, plus Denison's earlier bonus fix and
Janbogo's own instance) — Scandinavian-coded surnames were far and away the most common offender,
appearing in 5 of the 9 total instances found this subnet. One major finding: Denison's Enneagram
carried a genuinely severe documented contradiction (self-flagged by its own Mega_Init as "the most
direct contradiction found anywhere in this Megasheet series") with an already-authored but
never-applied resolution — fixed. Two cases investigated as likely 5th/6th Enneagram-mismatch instances
turned out to be false positives on closer reading (Janbogo, confirmed already reviewed and cleared by
its own Mega_Init) — a useful reminder to check Mega_Init's own reasoning before assuming the pattern
applies.

## Mawson Subnet

- [x] **Dome Fuji** — swept 2026-07-17. No rank citation (special 100%-robot, redistribution-derived
  population city, no rank ever assigned). Enneagram (Instinctive/Withdrawn/Positive Outlook) confirmed
  clean — this is one of only two genuinely unique profiles in the whole project per
  `Distinguishing_Overlapping_Profiles.md`'s own intro (alongside Abowasa). **Bug found (16th instance
  of the "stale TBD" pattern):** `Specs/Dome_Fuji.md` said "Notable Figures: TBD" despite
  `Dome_Fuji_Full_Extrapolation.md` §VIII already proposing two placeholders (Aslaug, Teodor Marchetti)
  — propagated to `Specs/Dome_Fuji.md` and `Local_Cultures/Mawson_Subnet/Dome_Fuji.md`. Both names
  checked against nation-mismatch — clean, given the genuinely ~34-nation population both Norway and
  Italy are real Notable-tier nations here (the Full_Extrapolation itself already flags the Italian name
  as "chosen arbitrarily... adjust freely," an honest disclaimer given the huge nation pool). **Enhancement
  opportunities found:** none beyond what Full_Extrapolation already covers.
- [x] **Mawson** — swept 2026-07-17. Both ranks confirmed correct (Census I 6th, Census II 9th, both
  match `Official_Population_Census.md` exactly). Enneagram (Feeling/Compliant/Positive Outlook)
  confirmed clean against `Distinguishing_Overlapping_Profiles.md` Group 4. Notable Figures already
  fully propagated everywhere (no stale-TBD gap this time — a genuine exception to the pattern seen in
  nearly every other city this pass). **Bug found (10th instance of the nation-mismatch sub-pattern):**
  "Founding Administrator Warrick Oyelaran-Zhao" paired a Yoruba/Nigerian middle name with names
  matching UK/Australia and China — but no African nation beyond South Africa is represented in
  Mawson's population. Simplified to "Warrick Zhao" across 6 files. The second figure, "Hostess Mei-Ling
  Sorensen," checked out as borderline-acceptable — Norway is genuine Notable tier here, and Sorensen is
  a plausible enough Scandinavian-adjacent match; left unchanged. **Enhancement opportunities found:**
  none beyond what Full_Extrapolation already covers.
- [x] **Sayowa** — swept 2026-07-17. Census I rank confirmed correct (32nd). Census II rank fixed
  ("29th"→"30th," stale against the current ranking table). Enneagram (Instinctive/Compliant/Competency)
  confirmed clean against `Distinguishing_Overlapping_Profiles.md` Group 6 (paired with Lazar) — and its
  own text already correctly cited all three highways (4/7-ext/37), which helped surface the next
  finding. **Major consistency bug found:** `Specs/Sayowa.md` documents a real "second correction" from
  2026-07-06 — the three-way "Sayowa Junction" (Hwy 4 + 7-ext + 37) sits *near*, not *inside*, the city,
  connected by "the Sayowa Spur" — but `Local_Cultures/Mawson_Subnet/Sayowa.md` never received this
  update at all. It still described only a two-highway junction (Hwy 37/7-ext, Hwy 4 entirely missing)
  sitting directly in the city, across 4 separate sections (Seasonal Rhythms, Architecture, Relationship
  to Other Cities, Notable Local Landmarks). Fixed all four. **Bug found (17th instance of the "stale
  TBD" pattern):** `Specs/Sayowa.md` said "Notable Figures: TBD" despite `Sayowa_Full_Extrapolation.md`
  §V already proposing two placeholders — propagated to `Specs/Sayowa.md` and
  `Local_Cultures/Mawson_Subnet/Sayowa.md`. Both names checked against nation-mismatch — clean (Poland
  is genuine Notable tier; the Scandinavian-adjacent surname is borderline-acceptable given the huge
  Notable list, same judgment call as Mawson's and Dome Fuji's). **Enhancement opportunities found:**
  none beyond what Full_Extrapolation already covers.

**MAWSON SUBNET COMPLETE — all 3 cities swept 2026-07-17.** Summary: 2 stale rank fixes (Sayowa's
Census II; Dome Fuji has none to check). The "stale TBD notable-figures" pattern continued (instances
16-17 of the project total), and the nation-mismatch sub-pattern appeared once more clearly (Mawson's
"Oyelaran," instance 10) alongside two borderline Scandinavian-surname cases judged acceptable given
each city's genuinely huge Notable-tier nation pools. The standout finding this subnet was structural
rather than name-level: Sayowa's Local_Cultures file had simply never received a real, substantive
2026-07-06 highway correction (the Sayowa Junction/Spur distinction, and Hwy 4 itself) that both
`Specs/Sayowa.md` and the Enneagram file already had — the kind of propagation gap this sweep exists to
catch.

## Byrd Subnet

- [x] **Byrd** — swept 2026-07-17. Rank confirmed correct (29th, matches `Official_Population_Census.md`
  exactly). Enneagram (Instinctive/Withdrawn/Competency) confirmed clean against
  `Distinguishing_Overlapping_Profiles.md` Group 1. **The standing highway-access contradiction — resolved
  2026-07-17, developer-directed:** initially flagged during the sweep and left untouched as a presumed
  deliberate, developer-known ambiguity (per an earlier audit's flag), but on user follow-up this turned
  out to be genuinely stale text, not intentional. `Locations/Infrastructure/Highways.md` — the
  authoritative source — unambiguously confirms Byrd as a Hwy 1/Hwy 22 junction, and `Specs/Byrd.md`'s
  own header was already corrected to match on 2026-07-06. But three other passages in the same file
  (Connection to Concordia ×2, Open Questions) and one in `Local_Cultures/Byrd_Subnet/Byrd.md`
  (Significant Local Events) still asserted "no overland road... in any established way" / "effectively
  sealed off" / "unreachable from the rest of Tepenia" — leftover pre-2026-07-06 language never updated
  when the header was fixed. User confirmed Highways.md as authoritative; reconciled all four passages
  to state the highway connection as confirmed pre-war infrastructure, reframing the genuinely open
  question as whether that route survived the war in passable condition (distinct from the aviation
  route, which is confirmed broken) — preserves Byrd's isolation/DLC-2-hook framing without the internal
  contradiction. **Bug found (18th and final instance of the "stale TBD"
  pattern):** `Specs/Byrd.md` said "Notable Figures: TBD" and "Demonym: TBD" despite
  `Byrd_Full_Extrapolation.md` §VIII already proposing a demonym (Byrdian) and confirming Maggie
  Aarden — a real, existing companion character, not an invented placeholder — as a Byrd resident, plus
  two further unnamed role-placeholders — propagated to `Specs/Byrd.md` and
  `Local_Cultures/Byrd_Subnet/Byrd.md`. **Enhancement opportunities found:** none beyond what
  Full_Extrapolation already covers.

**BYRD SUBNET COMPLETE — its 1 city swept 2026-07-17.**

# CITY HISTORY CONSISTENCY + ENHANCEMENT SWEEP — FULLY COMPLETE, ALL 35 CITIES, 2026-07-17

All five subnets (Halley 8, Palmer 8, Mirny 8, Janbogo 7, Mawson 3, Byrd 1) fully swept. Final tally
across the whole sweep: **~20 stale population-rank citations fixed**; **4 severe Enneagram-mismatch
cases found and resolved** (Esperanza, Rothera, Sejong, Denison — each either re-derived from the
city's actual dominant identity or reconciled via an already-authored-but-never-applied resolution),
plus 2 investigated candidates that turned out to be false positives on closer reading (Janbogo, Signy —
both already self-reviewed and cleared by their own Mega_Init); **18 instances of a newly-identified
recurring pattern** — a Full_Extrapolation or equivalent file proposing named placeholder Notable
Figures (and sometimes demonyms) that never got propagated back to `Specs/`/`Local_Cultures/`, which
kept showing generic "TBD" — found in essentially every city with a Megasheet triad; **10 instances of
a nation-mismatch sub-pattern** within that (a placeholder character's surname implying a nationality
the city's own population doesn't actually include, most often a Scandinavian surname tacked onto an
otherwise-correct name) — fixed across dozens of files including several full Course of Events
narrative stages whose filenames had to be renamed; **2 live violations of the binding No Subcontinentals
canon** in placeholder names (Sejong's original figure; Denison's, found as a bonus mid-Sejong-investigation);
**1 major structural finding flagged rather than silently fixed** (Davis's 2026-07-16 mining-to-breadbasket
economic reassignment reaching some files but leaving Course of Events narrative content contradicting
it — needs a developer decision on whether to reframe or retire those stages, not a documentation fix);
**1 real missing-established-fact gap** (Signy's two-island/bridge structure, established in Vision
Notes but never propagated into Specs or Local_Cultures at all); **1 confirmed deliberate non-bug**
(Shirayuki/Sinheung/Zhongshan's shared `Tri-Cities_Region.md` Enneagram file instead of three individual
ones); and **1 presumed-deliberate contradiction that turned out to be genuine staleness on follow-up**
(Byrd's own highway-access question — initially left untouched as a presumed developer-known ambiguity
per an earlier audit's flag, but resolved 2026-07-17 on user confirmation that `Highways.md` is
authoritative; four stale pre-2026-07-06 passages across two files reconciled with the already-corrected
header).
No enhancement opportunities beyond what each city's own Full_Extrapolation already proposes were found
in any city this pass — the project's existing Megasheet layer is, on the whole, already doing that
work thoroughly; this sweep's real value turned out to be closing the gap between what Full_Extrapolation
proposes and what actually reaches the source-of-truth files.

---

## Amundsen Station (not one of the 35 cities — swept 2026-07-17 for completeness, per developer request)

- [x] **Amundsen Station** — no rank citation in `Local_Cultures/Amundsen_Station/Amundsen_Station.md`
  (raw population only), so no rank check applicable. Enneagram (Thinking/Compliant/Competency)
  confirmed clean against `Distinguishing_Overlapping_Profiles.md` Group 2's current membership
  (Amundsen Station, Halley, Juan Carlos, Sejong). Notable Figures already correctly named (Kendra
  Heinrich, a real confirmed character, not a placeholder) — no propagation gap. **Bug found:**
  `Amundsen_Station_Mega_Init.md`'s "What's Actually Open" list was stale against its own same-day
  companion `Amundsen_Station_Full_Extrapolation.md` — 3 of 7 listed items (the Split Brain mechanism,
  the Tower's cargo/passenger purpose, the Pole marker's survival, St. Roald observance) already had
  proposed answers; rewrote the list to credit them, correctly leaving Kendra Heinrich's story and the
  archive's contents open as explicitly DLC-1-reserved content Full_Extrapolation deliberately didn't
  touch. Found and fixed the identical staleness in the hand-concatenated `README.md` copy too.
  Cross_Reference_Synthesis checked clean — no staleness, genuinely useful findings (notably: a
  centuries-lived robot who personally remembers pre-Split-Brain Amundsen Station is fully
  canon-plausible and currently untapped as a character hook). This document is correctly, deliberately
  much shorter than the 35 city sheets throughout — Amundsen Station was a rotating-staff facility, not
  a settlement, and every file here says so explicitly and treats the reduced scope as the correct
  outcome rather than an oversight. **Enhancement opportunities found:** none beyond what
  Full_Extrapolation already covers.

---

## Notes on method, carried forward city to city

- Not every city will have a `City_Vision_Notes/[City].md` file — Sanay did; absence isn't itself an
  inconsistency, just means one fewer file to cross-check.
- Population-rank citations are the single most likely stale-fact category (per Sanay's finding), since
  ranks get renumbered whenever any city's Census II figures are corrected elsewhere — worth specifically
  grep-checking each city's rank claims against `Official_Population_Census.md` directly rather than
  trusting any one file's stated rank.
- "No strongly distinct local variant surfaced" lines in a Catalog are expected/honest, not bugs (see
  [[project_...]] memory on this if unsure) — don't flag these as consistency problems.
