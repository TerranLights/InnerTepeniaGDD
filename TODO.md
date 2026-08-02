# Inner Tepenia — To-Do List

A running reference of outstanding design work, organized by urgency. Update as items are completed or reprioritized.

---

## Large backlog batch — flagged 2026-08-01, multiple distinct topics, none started

A batch of items the developer wants logged for future work. Grouped below by topic; nothing in this section has been researched or designed yet.

**Combat & systems mechanics**
- Sneaking and line-of-sight — stealth/detection mechanics not yet designed.
- More weapons — expand the current weapon roster.
- Armor and clothing — an armor/clothing system doesn't yet exist.
- Faction outfitting — what specific factions actually wear/carry, distinct from the general armor/clothing system above.
- Convert BG3 cantrips into "quickhacks," and BG3 spells and feats into perks and traits — a direct conversion-mapping exercise from Baldur's Gate 3's own ability lists into Inner Tepenia's own equivalent systems. **Progress, 2026-08-02:** the conversion methodology is now written (`Game-Mechanics/Perks/BG3_Conversion_Basis_of_Translation.md`), and a full first-pass triage of all 309 BG3 feat/spell/cantrip entries against that methodology is done — see `Reference/bg3-triage-01-feats-cantrips.md` through `bg3-triage-05-special-npc-item.md`. **Next step, not yet done:** review those 5 triage files and organize the ~309 triaged entries into their actual destination docs — level-up perks into `Regular_Perks_-_Level-Up.md`, quickhacks into a proper quickhack reference (doesn't fully exist yet, see `Hacking_and_Traceability_System.md`), earned perks into their respective category files per `Perk_Framework.md`, and items/weapons into whatever the armor/weapon system entry above resolves to. This is where exact numbers, final names, and destination filing (the framework doc's own Section 7 steps 5-7) actually happen — the triage pass deliberately stopped short of that.
- Convert Cyberpunk 2077's skill-based bonuses into "challenge perks," and also into ordinary level-up perks where that fits better — source material is CP2077's own skill trees (all five tabs, per [cyberpunk.fandom.com/wiki/Cyberpunk_2077_Skills](https://cyberpunk.fandom.com/wiki/Cyberpunk_2077_Skills)) and rank-up bonuses ([vg247.com's own skill progression writeup](https://www.vg247.com/cyberpunk-2077-skill-progression-and-rank-up-bonuses) — same underlying content as the wiki page, per the developer). Per direct developer instruction: this is explicitly a mixed sort, not a 1:1 conversion — some entries become challenge perks, some become ordinary level-up perks instead, and some won't translate at all given Inner Tepenia's Fallout-descended system rather than CP2077's own (e.g. CP2077's "+1 perk point" bonuses don't map cleanly, since Inner Tepenia only awards a perk point every two levels). Treat the CP2077 material as a rich basis to mine from, not a checklist to convert wholesale.
- What sorts of objects/items would cause the scientifically-supported, real-world-basis equivalent of BG3's damage types (and comparable relative amounts), and what kind of setting each would characteristically be found in — ties into the existing `Per_City_Weapons`/`Damage_Types.md` taxonomy work.

**Worldbuilding — civic life & economy**
- The actual legal mechanisms of how Tepenia deals with criminals — courts, arrest, enforcement procedure. Distinct from and more detailed than the existing 3-tier outcome framework already established (see `project_tepenian_criminal_justice_system` memory) — that covers where someone ends up, not how they get there.
- What kinds of festivals exist, generally — beyond whatever's already scattered across individual city/district Community Infrastructure files.
- Are there any homeless people in Tepenia, and if so, what does that actually look like.
- Where do cities/districts actually get their water.
- What standard is Tepenian currency actually based on (note: `project_national_currency_history` memory already covers the history of the currency fracturing into a regional/subnet system plus a cross-subnet trade standard — check whether this question is already partly answered there before starting from scratch. **Per direct developer instruction, 2026-08-01: this is deliberately the first domino, not a parallel task** — the actual name (see the "National currency name and mechanics" entry below) should be derived *from* whatever the money is actually based on, not chosen alongside it or before it. **Also note:** the term "scrip," used throughout the existing currency file, was never the developer's own choice and needs replacing — see `Worldspace/National_Economy_and_Currency.md`'s own top-of-file flag. Don't introduce or reuse that word in new writing.)
- General standards of living, and the cost of things.
- Following directly from the above — what does it actually mean to be "rich" in Tepenia.
- How is sewage and septic waste treated/handled.
- What other food-producing locations exist, beyond what's already established (Davis's breadbasket role, etc.).
- A general accounting of what currently exists across the project as flagged "side-content."

**City history expansion**
- Expand upon individual city history specs now that far better, clearer per-city information exists (Physical Infrastructure Attributes, Cross-Referenced Extrapolation Findings, diaspora composition data). Explicit developer example: a human resident of Byrd utterly snapping and losing his mind from being psychologically trapped underground for too long.

**Documentation**
- Go in and actually comment the code — including pseudocode.

---

## District Under-Questlines — new diaspora-composition input ready, generation not yet started — flagged 2026-07-31

Two new files now exist that substantially enrich the raw material `District_Under_Questline_Design_Method.md` draws on for each of Concordia's 13 districts: `Worldspace/Locations-and-Levels/Concordia-City/Districts/District_Refugee_Diaspora_Composition.md` (population-weighted breakdown of which outer Tepenian cities' refugee-diaspora populations live in each district, plus specific named Addition-location and Social Cohesion Mechanism transplants per contributing city, all summing to exactly 100% per district) and the 2026-07-31 diaspora-informed extension of all 13 `Deep_Dives/[NN]_[District]_Deep_Dive.md` files (4-5 new cross-referenced findings per district, each citing a specific diaspora fact and chasing it to a genuinely new implication — several of real quality, e.g. the Hub's Princess Elisabeth finding proposes an actual working answer to the long-standing "no Bridge Memorial ceremony has ever survived council review" problem).

**Not yet actioned:** nobody has run `District_Under_Questline_Design_Method.md` against this new material yet. This directly feeds the existing "District Main vs. Under-Questline candidates — generate more" item in `Weekly_To-Do_-_Current.md`/below — the diaspora file's own named communities, specific friction/fit dynamics, and the newly-added Deep Dive findings (particularly the ones explicitly flagged as "fertile Under-Questline material" in-line) are exactly the kind of concrete, named hook material the Under-Questline method needs and previously didn't have at this level of specificity. Natural next step whenever this gets picked back up.

---

## Remaining Municipal Holidays gaps — flagged 2026-07-31, deliberately deferred, not urgent

A full-corpus scan (all 35 cities' `Local_Cultures` sheets) found that cuisine, social contract, and religion are fully developed everywhere except Vostok (now resolved — see `Local_Cultures/Mirny_Subnet/Vostok.md`). Municipal Holidays is the one category with real remaining gaps: **Belgrano** (`Local_Cultures/Halley_Subnet/Belgrano.md` Section 26) is completely blank, *"(TBD — not yet established.)"* — the closest analog to what Vostok had. **Kunlun** and **Casey** have partial gaps (individual heritage-community observances unaddressed; open question whether a transit/function-organized city even has many observances at all). **Mirny (city)** and **Esperanza** have trivial "additional observances: TBD" stubs sitting on top of an already-established primary holiday. Per direct developer instruction (2026-07-31), this isn't urgent — pick it up whenever convenient.

---

## Byrd — deep-dive, Main Questline pool, and DLC City Under-Questline method complete 2026-07-30

Byrd's own dedicated deep-dive is done: `Byrd_Physical_Infrastructure_Attributes.md` (80 numbered physical/civic attributes, incl. "The Long Window" — a subglacial bioluminescent lake, cross-referenced into Vostok's own material too — plus 57 Cross-Referenced Extrapolation Findings), `Byrd_Community_Infrastructure.md`, both concatenated into `Byrd/README.md`. Closes out the entire nationwide Community Infrastructure & Social Life push (35/35 subnet cities, plus Concordia's 13 districts done earlier).

**27 DLC 2 Main Questline candidates on file** (`Storyline/DLC-Questlines/Byrd/`, #02–28) — none chosen/canon yet, that's the developer's own call whenever ready. The original Chamber Crisis candidate is preserved, not discarded, in `Storyline/DLC-Questlines/Byrd/recycling-bin/` as future unmarked Cradle side-content (ruled out per the standing `feedback_cradle_unmarked_lore` law, not for construction quality).

**New: `DLC_City_Under_Questline_Design_Method.md`** (`Storyline/DLC-Questlines/`) — the DLC-city-level adaptation of `District_Under_Questline_Design_Method.md`, written 2026-07-30. Byrd is the only DLC city where every Step 1 input currently has real material behind it (its own Main Questline pool covers input 6; its own Physical Infrastructure Attributes/Findings file covers input 9) — the natural first test case before trusting the method's own fallbacks against the other 5 DLCs, which don't have either yet at the same depth.

**Byrd Highway/Isolation Contradiction** (its own separate entry below, unchanged — "flag, don't fix" remains the developer's explicit direction) is directly load-bearing for the Isolation Crisis anchor specifically; Main Questline candidates built on it (#03, #18) were written to hold up under either resolution, not pick a side pre-emptively.

---

## Lazar's expansion-district name — flagged 2026-07-30, deliberately deferred

`Specs/Lazar.md` explicitly states the real "Maitri" station name "does not carry forward into Tepenia in any form" (No-Subcontinentals canon — no Indian/South Asian population ever settled there), but `Lazar_Mega_Init.md` and `Local_Cultures/Halley_Subnet/Lazar.md` both then repeatedly call the district "the former Maitri expansion" anyway — a real, unresolved inconsistency. Per direct developer instruction (2026-07-30), `Lazar_Community_Infrastructure.md` and its README now use a purely descriptive placeholder, **"the Overflow District,"** instead. An actual coined name still needs picking at some point — same category of open item as the Mirny and Marambio renames.

---

## Neumayer's "Precision Institute" — flagged 2026-07-30, open to alternate names

Renamed from "the Alfred Wegener Institute" (the real institute's own name, a GPS-only violation) during the Community Infrastructure pass. The developer likes "The Precision Institute" as a working name, but wants to leave room to consider additional options before treating it as final — see `Neumayer_Community_Infrastructure.md`.

---

## Majyao's teahouse (Janbogo) — flagged 2026-07-30 for an official, proper name

Currently known only as "Majyao's Original Teahouse" — the name of its former keeper (Majyao Bisyugota, now relocated to Concordia), not an actual name of its own. Tepenia's single most historically significant landmark in Janbogo (per `Janbogo_Community_Infrastructure.md`); worth a real name before it's used as an actual questline location.

---

## "The Endurance Span" (Signy) — flagged 2026-07-30 for possible future renaming

The named bridge holding Signy's two islands together (`Signy_Full_Extrapolation.md` Section III). Per direct developer instruction, Tepenia's own founders would probably have called it something else — see `Signy_Community_Infrastructure.md`. Same category as the Rothera geographic-name flag above.

---

## Sejong Community Infrastructure — flagged 2026-07-30 for future expansion

`Sejong_Community_Infrastructure.md`'s Social Cohesion Mechanisms list has only one entry — per direct developer instruction, a city this densely populated and multinational (a dozen absorbed national communities on one small island) would plausibly support far more. Revisit and expand.

---

## "Han Ji-woo" (Sejong) — flagged 2026-07-30 for future renaming

The founding-era figure credited with negotiating Sejong's original boundary-zone agreements (`Sejong_Full_Extrapolation.md` Section VI). Per direct developer instruction, the name isn't one they chose — see `Sejong_Community_Infrastructure.md`. Also noted there: `Sejong_Full_Extrapolation.md`'s proposed "Hangul Day" holiday was rejected outright by the developer ("that wouldn't happen") and should not be reused, though the source file itself hasn't been edited to remove it.

---

## Geographic-feature naming timeline — flagged 2026-07-30, a project-wide future pass needed

**The pattern, per direct developer instruction:** real-world geographic feature names (bays, mountains, hill ranges, straits) are plausibly accurate for the *earlier* portion of the Second Interwar Period — the exile generations would genuinely have kept using names like "Holme Bay" or "Marguerite Bay," inherited from documentation found inside the existing stations, simply because that's what the place was already called and there was no reason yet to change it. But over the following centuries, as Tepenian civic identity solidified and detached from its real-world origins, these names would very likely have been replaced with something the culture actually developed itself — the given example: the Larsemann Hills (Zhongshan/Sinheung/Shirayuki's shared terrain) eventually renamed to something Chinese, Korean, Japanese, or some fusion of the three, reflecting the Tri-Cities' own actual population rather than the real 2010s-era Antarctic place-name.

**This needs its own dedicated future pass** — going through every city's own geographic landmarks project-wide and identifying which real-world names would plausibly have persisted only into the earlier Second Interwar Period before being replaced, then coining the actual later-era replacement names. Already flagged as individual placeholders, pending this pass: Rothera's "Bonner Airstrip" and "Marguerite Bay Harbor," Signy's "Endurance Span," Mawson's "Holme Bay Harbor" and "Prince Charles Mountains," Sayowa's "Lützow-Holm Bay Harbor," and (implicitly) the Larsemann Hills shared by Zhongshan/Sinheung/Shirayuki. **Also applies to specific place-name labels tied to the Tepenian Saints framework** — e.g. Mawson's "St. Douglas's Landing": the *place-name* is real-world-derived and subject to this same eventual renaming, even though the underlying Saint veneration itself (part of the separate, legitimate, developer-confirmed Saints framework) is unaffected. Likely many more instances of both kinds exist across the corpus that haven't been individually flagged yet.

---

## Palmer City Community Infrastructure — flagged 2026-07-30 for future expansion

Per direct developer instruction: Palmer City is one of Tepenia's most culturally dense cities (43-nation composition, a full entertainment economy, its own defining founding myth) and its `Palmer_City_Community_Infrastructure.md` pass should get noticeably more Additions and social cohesion mechanisms than the standard-length first pass it received — come back and expand it, don't treat it as finished. Also flagged in the same file: **"The Petrograd Room"** needs a real name (not developer-chosen, likely would be called something else); and **where the relocated Antarctica flag now hangs in Concordia** is an open decision between (A) a museum-type building in whichever district fits best, or (B) a high-status official building in the Libra district specifically — not yet decided.

---

## "Elisa Faranda" (Zukelli) — flagged 2026-07-30 for future renaming

Zukelli's single most prominent named civic figure (proprietor of the city's most famous restaurant-and-performance-space, per `Zukelli_Full_Extrapolation.md` Section VII) — notably, the source file doesn't even tag her as a placeholder the way it does the adjacent "Councilman Renzo Adorni" entry. Per direct developer instruction, the name isn't one they chose and should be reconsidered before she's used in actual questline content — see `Zukelli_Community_Infrastructure.md`.

---

## Summer/winter dual-mode crossings — flagged 2026-07-30, logistics not yet worked out

Three established crossings share the same unresolved mechanic: sea ice passable in winter, boat/icebreaker crossing in summer, with no worked-out logistics for the actual switchover or the shoulder-season gap between the two modes. **Fort McMurdo:** the McMurdo Sound sea ice road, connecting to the Dry Valleys extraction operation. **Dumont d'Urville:** the Channel Crossing, the ~5km route between Petrel Island and the continental coast. **Sayowa:** the seasonal ice road connecting East Ongul Island to the mainland. Worth resolving once as a shared mechanic rather than separately per city — see `Fort_McMurdo_Community_Infrastructure.md`, `Dumont_dUrville_Community_Infrastructure.md`, and `Sayowa_Community_Infrastructure.md`.

---

## Tepenia's airports — flagged 2026-07-30 for proper official naming, all but one

Of the 8 confirmed airports (`Locations/Infrastructure/Airports.md`), 7 are currently named simply after their city (Zukelli/Janbogo Airport, Mirny Airport, The Tri-Cities Airport, Troll Airport, Rothera Airport, Marambio Airport, Machu Picchu Airport) — only **Mountain Pass Airport** already has a genuine, distinct proper name, and that one stays exactly as is. Per direct developer instruction: real-world major airports split both ways — some keep the city name (Los Angeles International Airport), some get their own distinct title unrelated to the city name (JFK for New York, McCarran/Harry Reid for Las Vegas). At some point in the future, go through all 7 city-named airports and decide, one at a time, which keep the plain city-name format and which get an actual distinct name instead.

---

## The Continuity and Stability Act — requirements confirmed 2026-07-29, actual document not yet drafted

Structural format and full "must be true" / "cannot be true" stipulations are locked in `Worldspace/Locations-and-Levels/Concordia-City/Districts/Continuity_and_Stability_Act_Requirements.md`. **Still open before drafting:** whether Capricorn and Leo count as confirmed provisions of the Act (loosely gestured at in earlier files but never actually confirmed in either district's own writeup — a real, flagged inconsistency) or are explicitly left out, same as Scorpio's own looser, derivative connection. Once that's resolved: draft the actual Articles (how many, what each broadly authorizes), and place each district's own partial citation of the Act somewhere in-world (Pisces' Triage Directive already has a home in Libra's Treaty Archive Vaults; the others don't yet).

**Also flagged 2026-07-29 — eventually create additional Under-Questlines using the Act as a reference,** once it's drafted: a genuine cross-district "connect the dots" investigation thread (plausibly a Gemini data archaeologist, per that district's own established role) piecing together Aries', Libra's, Cancer's, and Pisces' separate partial citations to reveal the Act's existence. `District_Under_Questline_Design_Method.md`'s own input 9 already flags this as a strong cross-district seed — this note just tracks it as a concrete future to-do once the Act itself actually has Articles to cite.

---

## National currency name and mechanics — flagged 2026-07-29, deliberately deferred

"Scrip" (`Worldspace/National_Economy_and_Currency.md`) was never the developer's own term and needs renaming — but it appears across 100+ files (course-of-events entries, code architecture docs, city lore), so this isn't a quick swap. **Sequencing clarified 2026-08-01, per direct developer instruction:** the actual name is downstream of, not decided alongside, a separate prior question — see the new "What standard is Tepenian currency actually based on" item in the 2026-08-01 backlog batch above. Resolve what the money is actually backed by first; the name should fall out of that once it's settled, not be picked in parallel. Don't rename piecemeal — revisit as its own dedicated pass once the standard is resolved.

---

## Companion Forbidden Traits — in progress, paused 2026-07-28

The "forbidden trait" romance-gate mechanic (`Game-Mechanics/Core-Mechanics/Companion_System.md`'s "Forbidden
Traits" section; full process in `Game-Mechanics/Core-Mechanics/Forbidden_Trait_Design_Method.md`) has been
assigned to 11 of the game's romanceable characters so far. Deliberately paused, not blocked — pick back up
whenever.

**Done (11):** Favi della Torre, Naizelle d'Edjordoś, Villena Hiresvett, Ji-Eun Kim, Michelle Stanton, Trisha
Miller (full romance design also created from scratch for her), Seica Cenilaithe, IT-068 [Flora], Vosora
Lashár Tanslock, Ayako Hayashi — plus Majyao Bisyugota (Demagogue confirmed; a new trait, "Broad Strokes,"
still pending finalization before her list can be closed out).

**Still remaining — stat thresholds already exist, just need this pass (3):** IT-021 [Fenny], FW-25 [Pink
Lucy], Lyuba Baranova.

**Blocked on stat design first (2):** TCY-25 "Rui" and Salagéa Aparast — MACHINE stat thresholds themselves
still TBD.

**Genuinely open question — may not apply at all (2):** Kendra Heinrich and Calethina — both have unique,
stat-free conduct-based romance gates; whether "forbidden traits" makes sense for either hasn't been decided.

**Side effects worth remembering when resuming:** two traits escalated mid-pass after becoming
disproportionately wide-reaching dealbreakers — **Cut Losses** (5 companions) and **Narrative Ghost** (8
companions) — see their own `Character-Creation/Traits.md` entries for the escalated mechanics. Two new
traits were designed and flagged for future review rather than finalized: **"Broad Strokes"** (bonus still
undecided) and **"One-Way Exchange"** (bonus finalized, but carries an unresolved content-tagging production
dependency). **Demagogue**'s own production dependency (sufficient crowd/group-address content) now applies
across multiple companions, not just Trisha — worth prioritizing if that content gap hasn't been addressed by
the time this pass resumes.

---

## In-Universe Mascot Icon ("not-Vault-Boy") — flagged 2026-07-28, deliberately deferred

The developer wants an in-universe Tepenian equivalent of Fallout's Vault Boy — a small recurring
"character-figure" icon used across relevant UI images (perk cards, trait cards, weapon icons, etc.), the
same way Vault Boy illustrates SPECIAL stats, perks, and items throughout the Fallout games. **Explicitly not
urgent** — the developer's own words: "something that needs to be addressed at some point in the future, not
now, not today, just sometime someday." Nothing designed yet: no name, no visual concept, no confirmation of
which UI elements would actually use it. Revisit once character-creation/UI art direction work is underway.

---

## Marambio's Post-Culture Identity Rename — flagged 2026-07-21, deliberately deferred

"Standing on Warmer Ground" only meant anything because of the fossil premise struck the same day (see
the "Marambio Fossil/Paleontology Strike" entry in `DONE.md`) — nothing else currently established about Marambio supports it (the city is
colder than its neighbors, not warmer). Three options drafted, none chosen: "Never Just One Thing"
(reuses Course of Events chain #10's title, about the airfield/shipyard diversification strategy),
"Built for Motion, Not for Staying" (new phrase, names the transience theme already running through the
whole culture sheet), "Whoever Runs It Now" (reuses chain #3's title, about founding discipline
outliving its founders). Full writeup with rationale for each:
`Cities/City_Megasheets/Palmer_Subnet/Marambio/Marambio_Identity_Rename_Options.md`. Whichever is chosen,
the name needs updating in `Local_Cultures/Palmer_Subnet/Marambio.md` (Section 5),
`Full_City_Integrity_Check.md`, `TODO.md`'s own historical entries, and `City_Vision_Notes/Marambio.md`.

## Megacorp Post-Falkland-Treaty Fate — flagged 2026-07-20, deliberately deferred

New question, occurred to the developer while developing Imelda Sánchez: what happened to the
pre-war robot-fabrication megacorps once the Falkland Treaty (2564) declared sentient-robot presence
illegal in Upper Earth? Their entire business model would've been existentially threatened overnight.

**What's established:** `TepenianUniverseTimeline/Megacorps/README.md` (in the sibling Timeline repo)
names two megacorps so far — HyperHedral (based in the People's Democratic Republic of Cascadia) and
Industrias Abramentes (based in the Republic of Sonora) — plus a third slot still marked `[TBD]`. Both
entries are one-line stubs with no post-Treaty fate defined. The Falkland Treaty draft itself
(`TepenianUniverseTimeline/Reference/Falkland_Treaty/Falkland_Treaty_Draft_v1.md`) never mentions
corporations at all — it's silent on this question, genuinely open territory. Imelda Sánchez's own
still-unresolved corruption backstory (exposing corruption between the Mexican government and
"Upper Earth megacorporations," per her `README.md`) is the one existing thread this could hook into.

**Candidate directions discussed, none chosen:** (a) dissolved/seized by treaty enforcement or
nationalization; (b) pivoted to adjacent non-sentient-robotics industries and survived legitimately;
(c) went underground, continuing illegal sentient-robot work as smuggling/black-market operations
(this one has the strongest hook into Imelda's expose). Likely not a single monolithic answer —
different megacorps (with different national homes) plausibly diverge, rather than all sharing one fate.

**Status: flag, don't fix — developer's own reserved decision.** Not resolved now; reserved for a
dedicated future session.

---

## Mawson DLC — City Depth Gap, flagged 2026-07-14, needed before Mawson DLC quest design begins

Mawson subnet has only 3 cities, and two of them can't carry real weight for the DLC main questline:
**Dome Fuji is completely, totally, and entirely optional** — it shouldn't factor into the DLC main
questline at all. **Sayowa is usable, but its significance outside shipping/supply-chain logistics is
thin** — it can be used, but may be difficult to lean on for much. That leaves **Mawson itself** to carry
a disproportionate share of the DLC's weight, which the city as currently developed isn't built to do
alone.

**What needs to happen, before Mawson DLC quest-design work starts (not now):** either (A) establish
real depth and complexity in the city of Mawson itself, well beyond its current development level, or
(B) invent smaller scattered settlements in the currently-open geographic area of that region, or
(C) both. Until one or both of these happen, running `DLC_Main_Questline_Design_Method.md` against the
Mawson subnet would be working from a genuinely thin evidentiary base compared to every other subnet.

**Resolution direction confirmed 2026-07-20: (C), both — plus a third lever.** Scattered smaller
settlements are now a confirmed general worldbuilding practice (realistic given real geography between and
beyond named cities), and for Mawson specifically they're treated as essentially required, not optional.
On top of that, Mawson is now assigned the highest companion-count tier in the game — **6-10 recruitable
companions** — under the new "Multiple Native Companions Per DLC" policy (see
`Game-Mechanics/Core-Mechanics/Companion_System.md`), explicitly as compensating depth for being the
thinnest, least narratively-developed subnet. This gives Mawson three separate levers to close the gap
(city depth, invented settlements, heavy companion presence) rather than relying on any one alone. Still
not started — this is confirmed direction, not executed content.

**A related planning note, same day:** Dome Fuji (and quite possibly Sayowa) will still end up carrying
an enormous amount of side-content — being excluded from the DLC *main* questline doesn't mean either
city goes underdeveloped. The thing to plan for deliberately is that this content stays **optional
side-content**, not folded into the main questline's own critical path. When Mawson DLC design actually
starts, this needs its own explicit pass: what Dome Fuji's (and possibly Sayowa's) optional content
consists of, and concrete guardrails ensuring none of it becomes load-bearing for the main questline —
consistent with this project's existing precedent for optional, unmarked content (see the Cradle's own
binding constraint, above) and the standing Companion-Mediated Access / Cross-DLC Bypass laws for how
optional content is normally scoped elsewhere in the project.

**Status: flag, don't fix — hold until Mawson DLC's turn comes up in the subnet quest-design rotation.**

---

## Population Tier-Ordering Anomaly — flagged 2026-07-13, deliberately deferred

A recurring data-quality pattern surfaced repeatedly across the country-wide culture re-check: in a city's own per-nation population breakdown, a Notable-tier nation's share sometimes exceeds a Significant-tier nation's share — the tiers no longer match the actual percentage ordering. **13 confirmed instances now**, spanning 10 nations across 12 cities plus Concordia: Port Lockroy (Chile), Abowasa (Germany), Troll (Germany), Lazar (France), Princess Elisabeth (UK), Sayowa (Japan), Mawson (Germany), Belgrano (UK), Halley (Germany), Dumont d'Urville (South Korea), Juan Carlos (Germany), Sinheung (Australia), and Concordia (Thailand, outside the 35-city count). Full detail, per-instance percentages, and the discovery history: `project_tier_ordering_anomaly_master_list` memory.

**Near-certainly a systematic artifact of the 2026-07-05 de-stacked randomized redistribution method** (tier assignment following the pre-de-stack ranking rather than the final de-stacked percentages), not isolated per-city errors — the recurrence across 5+ nations and both small and large magnitude instances argues against coincidence.

**Status: flag, don't fix — developer's own reserved decision.** Not resolved now; reserved for a dedicated future session once the developer decides how to approach it (spot-fix each instance individually, or re-run the de-stacking method for affected cities).

---

## Byrd Highway/Isolation Contradiction — flagged 2026-07-14, deliberately deferred

A genuine, significant internal contradiction in Byrd's own established lore, surfaced during the country-wide culture re-check and confirmed still unresolved during Investigation Loop Round 2. The header of `Specs/Byrd.md` (and `City_Relationship_Database.md`) confirms Byrd has real, functioning highway access — Hwy 1 west to the Peninsula via Rothera, Hwy 22 east toward Amundsen Station/Zhongshan — treated as established freight infrastructure. But the Geographic Basis, Current Status, and Open Questions sections of the same Specs file (plus matching passages in `Local_Cultures/Byrd_Subnet/Byrd.md`) still say things like "No overland road connects it to the highway system in any established way" — directly contradicting the header and undercutting the "sealed off since the aircraft broke down" premise DLC 2 is partly built on.

This isn't a fresh discovery — `Byrd_Cross_Reference_Synthesis.md` (2026-07-09) already names the tension directly ("Byrd's isolation was never actually total, even though its own established character insists otherwise"), and `Byrd_Mega_Init.md`'s "What's Actually Open" already flags "whether any overland highway connection was ever confirmed for *people*, as distinct from the freight-only Hwy 1/Hwy 22 network." It has simply never been reconciled in the primary Specs/Local_Cultures files.

**Status: flag, don't fix — developer's own explicit direction.** Reserved for a dedicated future session. See `project_byrd_bug_check` memory for the full discovery writeup.

---

## Companion character-file integrity sweep — flagged 2026-07-13, ready to start (city re-check now resolved, see DONE.md)

Not yet started; expected to begin 2026-07-15 or later, per developer's own timeline. During the country-wide culture re-check (now resolved, see the "Country-wide culture re-check" entry in `DONE.md`), the same bug — a city's composition claim, once fixed in that city's own files, surviving uncaught in a companion doll's own character file — was independently found twice in one day: Davis's "Priya Devendra" placeholder name (No Subcontinentals canon violation, in `Davis_Full_Extrapolation.md`) and Casey's stale "leads T2" claim (surviving in `Ayako Hayashi/README.md`'s own origin-city candidacy reasoning). Companion files reference cities constantly (origin cities, candidacy comparisons, refugee/diaspora ties) and are consistently the last place checked, if checked at all. Now that the city-by-city sweep is fully done, go through every companion's character folder and files individually, checking for dangling stale references to city composition, founding-nation claims, or any other fact that's since been corrected on the city's own side but never propagated to the companion's file. The topic-independent investigation-loop process built for the city sweep (`Cities/Founding_Nation_Bug_Investigation_Methodology.md` Section 4A, `testing/QA_template.md`) is the natural process to adapt for this sweep.

---

## Early Access vs. Launch Content Split — flagged 2026-07-10, released as reference

The developer's own plan: release Inner Tepenia in Early Access first, partly to raise funds for hiring professional 3D animators, voice actors, and bands/musicians, then follow with a full "Launch" release (not Early Access) — with all 7 DLCs waiting until after that full launch. Worked through a full answer to "what content is feasible to hold back for Launch specifically," now written up at `Dev-Road-Map/Early_Access_vs_Launch_Content_Split.md`. Headline recommendation: lead marketing with the three things the funding is directly for (full voice acting, final 3D animation polish, original music/bands) as the most emotionally legible pitch to an Early Access audience, with full companion roster completion, full localization, and final balance passes as secondary, well-precedented Launch-exclusive items. Not a blocking decision — this is a released reference document, consult it whenever release-strategy planning resumes.

**Resolved same day: romance stays in Early Access, but with a reduced roster.** Reconsidered and reversed an initial lean toward deferring all romance content to Launch — companion romance is too central to the game's own draw and to its own creative north star (love between robots and humans) to hide from the Early Access audience entirely. Instead, Early Access will include a small subset of recruitable companions (roughly 3-4) with their full romance arcs, at whatever polish level the rest of Early Access ships at; the remaining companions and their romance content are what's actually deferred to Launch.

**Revised 2026-07-10: Michelle Stanton confirmed for Early Access in Flora's place; Flora deferred to Launch.** Resolves the Flora/Michelle personality-overlap flag below without designing a new companion — the two aren't both in Early Access at the same time, so the near-identical personality/job overlap no longer matters for the Early Access subset. Flora's own recruitment scene is structurally tied to the Thermal Distribution Junction 12 diagnostic (the likely opening task, "The Heating Grid Failure"); in Early Access, the repair crew the player finds there is led by a **non-recruitable human NPC** instead, and Flora's version of that scene (plus her recruitment) becomes Launch content. Michelle needs no equivalent substitution — she's already the single most guaranteed-to-meet character in the base roster per the revised main quest beat structure (`Main_Quest_Revised_Beat_Structure_TENTATIVE.md`, Beat 4: she's structurally necessary to diagnose the grid crisis's own data-corruption layer).

**Flora/Michelle personality overlap — RESOLVED 2026-07-10 for Early Access purposes.** IT-068 (Flora) and Michelle Stanton read as basically the same personality type with basically the same job (both landing in similar Enneagram/thinking-competency territory, both craft-and-repair-coded). Rather than expanding the roster or reworking either character, the two are simply staggered — Michelle in Early Access, Flora at Launch. The underlying overlap between the two characters themselves is unchanged and could still matter once both are in the same released game at Launch, but it's no longer an Early Access scheduling problem.

**Favi della Torre confirmed for Early Access, 2026-07-10.** Taurus (Beat 2), distinctively Type 6 with a sniper/field-operative archetype — no personality overlap with Michelle or any other confirmed slot.

**Vosora Lashár Tanslock deferred to Launch, 2026-07-10.** She's co-located with Michelle in Gemini/Beat 4, running the recovery-side half of the same Great Corruption investigation Michelle runs from the slow-verification side. Rather than two Gemini companions both being present in Early Access, Vosora's own recruitment and questline become Launch content. **Substitution for Early Access:** a discoverable data-stash of her own investigation notes, placed somewhere in Gemini, continues the Great Corruption breadcrumb trail without Vosora herself appearing as a live NPC — same pattern as Flora's Junction-12 substitution above.

**Lyuba Baranova confirmed for the final Early Access slot, 2026-07-10; Seica Cenilaithe deferred to Launch.** Both Seica and Lyuba are 8w7 Sexual, so this was never a variety question between the two of them directly. The deciding factor: TCY-25 "Rui" (9w1 Self-Pres) was confirmed recruitable the same day and also lives in Scorpio — Seica's district. Deferring Seica to Launch alongside Rui keeps Scorpio's companion representation as a genuine Launch-era personality pairing (8w7 + 9w1) rather than splitting it across Early Access and Launch. Lyuba, in Aries, has no district overlap with anyone else confirmed or pending, making her the cleaner Early Access pick. Full Early Access companion roster as of 2026-07-10: **Michelle Stanton (Gemini), Favi della Torre (Taurus), Lyuba Baranova (Aries)** — Flora, Vosora, and Seica all deferred to Launch. See `Dev-Road-Map/Early_Access_vs_Launch_Content_Split.md`'s "Tentative Early Access Companions" section.

**TCY-25 "Rui" confirmed recruitable/romanceable, 2026-07-10.** 9w1 Self-Pres, Scorpio (Beat 3) — previously "Companion Potential: Undecided." Real name, backstory, MACHINE stat baseline, questline, and home design all still TBD; see the TBN-characters entry further down this file.

---

## New Cross-City Faction Patterns — flagged 2026-07-09, hold for later

Surfaced during a pass across `City_Origin_Factions_Second_Interwar.md` and `City_Origin_Factions_PostWar_Refugee.md`, prompted by how much richer the city-level picture has gotten since those docs were last updated (2026-07-04) — specifically the Halley subnet, Mawson subnet, and Byrd Megasheet cross-reference work done 2026-07-09. Both ideas below are genuinely new patterns those two documents don't yet cover; explicitly not developed further now, just captured so they aren't lost.

1. **"The Cradle-Keepers" (working name) — Neumayer, Byrd, Sinheung.** Three cities across three different subnets, each holding one piece of the single most nationally load-bearing system in Tepenia (the robot-creation/Cradle infrastructure), none of them getting real credit for it. Neumayer designs the current chamber schematic uncredited (the same pattern as the Amundsen Tower); Byrd and Sinheung manufacture it, both modest-political-profile cities most of Tepenia barely thinks about. Strong material: shared, mostly unspoken solidarity or resentment among people who know their city is quietly indispensable to the whole country's population growth while everyone else's attention goes elsewhere.

2. **"The Long Haul" (working name) — Belgrano, Byrd, Sayowa, Lazar, Troll.** Five cities whose civic economies are all, independently, built around keeping the actual overland freight network running (established for Sayowa and Byrd specifically on 2026-07-09; already on record for Troll/Lazar/Belgrano). The Rastra vehicle lineage (Belgrano invented it to find Byrd; Byrd plausibly still builds it today) gives this a genuine physical throughline, not just a thematic one — a working-class, road-and-dispatch professional identity distinct from Fort McMurdo's more centralized, prestige-adjacent logistics dominance.

**Also flagged:** once weekly model allotment has replenished, do a genuinely thorough sweep of all the new city-level material (all 35 city Megasheets, Amundsen Station) specifically hunting for more cross-city faction patterns like the two above — this session's pass was necessarily quick/surface-level given the day's allotment constraints, and a fuller pass will likely surface more.

---

## Concordia District Origins — Full Consistency Cross-Reference (flagged 2026-07-09, targeted for Sunday)

A large, multi-document audit task, explicitly deferred rather than started on a short-allotment day. **The question:** now that the project has accumulated an enormous amount of downstream world history since Concordia's own district-origin material was first written (the Second Interwar Period timeline, every city's full Megasheet treatment, faction spec sheets, the district canon reference itself), does each district's own "how it became the way it is" origin story still actually make sense? Or has later-established lore quietly undercut, contradicted, or made implausible any district's founding/development narrative?

**What needs to happen, when picked up:**
1. Read across the general historical docs (`World_History_Reference.md`, the First/Second Interwar Period timelines, `District_Canon_Timeline_Fix`-era dates).
2. Read across the completed city Megasheets (all 35 cities + Amundsen Station) for anything that bears on Concordia's own founding population, refugee waves, or district character.
3. Read across the various faction spec sheets (`Worldspace/Factions/`) for anything that bears on how a specific district's identity or history is explained.
4. Read Concordia's own district-origin docs (`District_Canon_Reference.md`, `Historical_Pressures.md`, and each district's own material) and check whether their own explanations for "how this district became this way" still hold up against everything above.
5. **Do not fix anything found — just document it.** For each district whose origin story no longer makes sense, or is in tension with something established elsewhere, write a clear note: what the district's own doc claims, what other now-established fact it conflicts with or is undercut by, and why the tension actually matters. Bring the list back for a joint decision on what to do about each one.

This is distinct from the earlier `project_concordia_consistency_audit` pass (2026-07-09, same day but done separately) — that pass caught factual/reference bugs (highway directions, stale status labels, a location's district placement). This task is narrower and deeper: whether each district's own *historical narrative*, not just its factual details, still coheres against the full weight of everything else the project now knows.

---

## The Cradle Manufacturing Network — Established 2026-07-07

**Confirmed and currently active — two manufacturing sites:**
1. **Sinheung** — original site, established 2026-07-06.
2. **Byrd** — "mechanized fabrication," housed in a specifically reinforced section of its own enormous underground plant complex (Notable Locations entry: "the chamber works"). The ceiling fortification this requires lines up with the city's own already-established "ongoing battle against accumulation" architecture, and mirrors Rothera's underground-vault protective logic — except stronger, since Byrd's underground isn't a secondary bunker, it's the city's actual founding core.

**Confirmed but historical, no longer operating — two sites:**
3. **Mountain Pass** — a joint Vostok-Kunlun venture, a small industrial outpost (not a city) at Mountain Pass Airport, the standalone waypoint on Hwy 37 between the two cities. Originally the resolution to a real problem: Fort McMurdo was confirmed as a third active site, then reverted the same day, because Mount Erebus's active-volcano status (continuously active since 1972, a persistent lava lake) raises a genuine double hazard for precision synthesis equipment — lava/ashfall risk *plus* ongoing seismic vibration. The role moved to Mountain Pass instead — geologically stable, no volcanic activity nearby, and a concrete physical expression of the already-established "two loneliest outposts" relationship between Vostok and Kunlun. **But then a second retcon, same day:** the outpost was too remote to support its own dedicated power infrastructure and ran instead on residual overflow from Amundsen Tower's continent-wide regulated grid (`Energy_Grid_Failure_Rationale.md` #11). The Tower's destruction during the Long Night War ended that supply, and the outpost's manufacturing capability, permanently — the facility itself is still standing, simply dark rather than destroyed. Chambers built there before the war still function wherever they shipped to; no new ones have been made there since. **A quiet, non-quest-related discoverable detail:** the specific chamber in Calethina's own lab in Concordia — the one that built the player character — was itself manufactured at this outpost, findable only by a sufficiently diligent, curious player, never surfaced through any quest. **Still open: the developer wants to eventually give this outpost a proper name** — currently only referred to by the airport waypoint's own name.
4. **Denison** — a legitimate Cradle producer during its living Second Interwar Period, lost when the city was later destroyed. Same category as Mountain Pass now (historical, not current).

**"The Cradle"** names the overall nationwide system (manufacturing sites, production industry, shipping network together), not the individual apparatus — still needs its own separate term, and the name itself remains provisional.

**Scott's one genuine industry** (beyond its established residential/political character) is also now confirmed: collecting Mount Erebus's volcanic fallout and delivering it to a trucking facility across McMurdo Sound, forwarded onward down the coastal highway into the Janbogo subnet — this is what originally prompted moving the manufacturing role off Fort McMurdo rather than trying to mitigate the volcanic hazard in place.

**Written into:** `Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md`, `Specs/Byrd.md` + `Local_Cultures/Byrd_Subnet/Byrd.md`, `Specs/Vostok.md`, `Specs/Kunlun.md`, `Specs/Scott.md` + `Local_Cultures/Janbogo_Subnet/Scott.md`, `Specs/Denison.md`, `Locations/Infrastructure/Airports.md`, `Locations/Infrastructure/Highways.md`, `City_Relationship_Database.md`, and `Sinheung_Full_Extrapolation.md` Section III (README regenerated).

**A related note on Concordia, surfaced during this thread:** Calethina's own personal activation lab ("your starting build chamber," per an older district-layout draft) is a real, pre-existing piece of canon — but it's a singular, personal facility tied to her specifically, not evidence of an industrial Cradle site. Its actual map location was pinned down to Cancer district's outer edge, right at the corner where Cancer, Taurus, and Capricorn meet (confirmed against the developer's own district map) — adjacent to Capricorn, Concordia's own industrial district, which is a natural candidate if a genuine industrial-scale facility is ever placed in Concordia, distinct from Calethina's own lab. Concordia's Cradle role (Cancer vs. Central Hub, originally proposed) remains genuinely undecided, deliberately deferred until Concordia's own development begins.

**Future task flagged 2026-07-10 — a full, elaborated nationwide Cradle network model.** Surfaced during the Mirny Subnet Ultra-Megasheet, which traced this network's own thread directly into the player character's own origin (Vostok/Kunlun's Mountain Pass venture → the specific chamber in Calethina's lab). Developer explicitly confirmed enthusiasm for a dedicated future pass extrapolating, elaborating, and fleshing out the network's full nationwide shape — framed as "a huge benefit to the game's lore and player discovery." Not started; reserved for a dedicated future session, in the same vein as the Orbital Composition task below. Likely scope: a proper name for Mountain Pass (still outstanding), resolving Zhongshan's/Sanay's/Belgrano's own still-open manufacturer candidacy, and possibly a dedicated `Cradle_Network.md` reference file consolidating the network's full shape rather than leaving it scattered across each subnet's own City Megasheets and Ultra-Megasheets.

**Binding constraint on all of the above, established 2026-07-10:** none of this may ever become an actual quest, marked or unmarked-but-tracked, in any DLC or the main game — no journal entry, no map marker, no XP, regardless of how elaborate this future pass makes the network's own lore. See `Design_Principles.md` Section IV ("Unmarked Discovery Content — The Cradle Precedent") for the full rule. The Cradle stays pure, optional, undirected background lore — a reward for player diligence and curiosity, not a game feature.

---

## Belgrano's Wartime Status — Still Genuinely Open

**Rothera and Belgrano remain proposed but not confirmed** as Cradle manufacturers — Rothera was only ever proposed alongside the original four, never separately confirmed; Belgrano is blocked on the items below. **Zhongshan remains a strong candidate**, not yet confirmed either way.

1. **A genuine status drift was found on Belgrano specifically.** `Specs/Belgrano.md`, `Local_Cultures/Halley_Subnet/Belgrano.md`, and `Official_Population_Census.md` all agree, with explicit correction dates, on **"Ruins (DLC 5)" — survived the Long Night War intact, then declined into ruin over subsequent decades; still inhabited.** But `Station_to_City_Map.md` and `Overview.md` both still say "Damaged; partially operational" — stale, never updated to match. **Do not fix these stale files yet** — the underlying status itself is under active reconsideration, not just the tracking tables.

2. **The post-war decline mechanism is well-supported:** Belgrano's own established Halley subnet supply route (one of two coastal ports receiving South African freighter shipments, redundant with Sanay — "whichever passage is open") means a disruption to just Belgrano's own leg, without any need for total wartime destruction, plausibly explains the slow, decades-long decline already in the Boneyard Times lore (`Worldspace/Factions/City_Origin_Factions_PostWar_Refugee.md`). Sanay's alternate seaborne route could plausibly have kept some raw material reaching Belgrano throughout, meaning a Cradle facility there never went fully dark — declined hard alongside everything else but kept limited, precarious production going. This piece is solid and can likely be written in as-is once the rest resolves.

3. **The actual open question: Belgrano's *wartime* survival has no established geographic reason, unlike its neighbors.** Sanay's bedrock foundation and Lazar's sheer scale both have explicit, stated physical reasons for surviving as "damaged, not destroyed." Belgrano — a coastal city with a confirmed, named-significant runway, the kind of target real militaries prioritize — has no equivalent justification for surviving the initial war intact when Zukelli and Denison, similarly identifiable targets, were fully destroyed. A full for/against breakdown across five lenses (air-weaponry realism, geography/environment, in-world construction facts, supply-line options, local culture) was worked through for all four possible states (Ruins / Destroyed / Damaged-yet-functional / Survived) — Ruins remains the best-supported overall, but the wartime-survival gap specifically is the one piece nobody has closed yet.

4. **Halley was examined for comparison and got a stronger answer than expected** — resolved, not paused, safe to write in whenever convenient. Its own worst-fit geography (floating Brunt Ice Shelf, the least stable foundation type, anchoring a high-value highway/comms corridor) is resolved by its own already-established "designed for relocation" trait — real militaries would most plausibly hit it with precision-guided munitions at the Hwy 59 corridor specifically, and/or trigger or accelerate ice-shelf calving (a real, documented risk of the actual Brunt Ice Shelf — the real Halley VI station was relocated in 2016–17 for exactly this reason). Halley's mobility design is what would let survivors relocate away from a cracking, calving section before full loss, explaining "damaged, not destroyed" despite carrying the subnet's most vulnerable foundation and highest strategic value.

**Status: do not write Belgrano's Cradle role, status fix, or decline mechanism into any file until the wartime-survival question above is revisited.**

---

## Mirny Rename — flagged 2026-07-08, deliberately deferred

Mirny's actual national composition (China Primary; Russia only Significant tier) bears no real resemblance to the real Russian station and ship (Bellingshausen's *Mirny*) the name and founding story are built around — unlike Sinheung's already-flagged Korean rename, this isn't a demographic-tiering bug to fix, just a name that no longer fits the population it describes. Flagged for an eventual rename; not resolved now. Whenever this gets picked up, note that `Local_Cultures/Mirny_Subnet/Mirny.md`'s entire cultural identity ("The City on the Line," Section 2 Founding Story, Section 5 Post-Culture Identity) is currently built around the Russian-name-vs-Chinese-majority founding tension specifically — a rename would need to either preserve that tension under a new name or replace it with a different defining identity entirely, not just swap the label.

**Confirmed 2026-07-10, during the Mirny Subnet Ultra-Megasheet:** the rename is scoped to the *city* only — the developer explicitly confirmed the six-city regional "Mirny subnet" keeps its own name regardless of what the city itself is eventually renamed to, a deliberate decoupling (the same way a real Antarctic regional name can outlive whichever specific station or claim it was originally drawn from). No replacement city name chosen yet.

---

## Quest Marker Design — flagged 2026-07-07, deliberately deferred

A tangent that came out of the Zukelli discoverability work, explicitly not resolved now: whether Inner Tepenia should have quest markers at all, and if so, what form. Four options discussed, not decided between:
1. **Full pinpoint markers (Bethesda-style)** — zero friction, but flattens exploration and cuts against the discovery-rewards-attention philosophy already built into World Perks and the Zukelli mechanic.
2. **Approximate/regional markers (New Vegas-style)** — the natural default given the project's own binding Fallout Precedence Law; marks a general area, still requires reading quest text to close the gap.
3. **No markers at all (Elden Ring-style)** — strong thematic fit, but risky at this game's continent-spanning scale without careful design.
4. **Diegetic markers** — an in-fiction justification (robot PC's own sensor/Arcanet overlay vs. a human PC relying on mundane notes) tying marker presence to the world itself rather than a pure UI toggle.

A tentative split-by-content-tier instinct was floated (NV-style approximate markers for main-quest critical path; no markers for optional/hidden content, consistent with the Zukelli precedent) but this is not settled — flagged for a real design pass later, not now.

**Important camera-paradigm correction surfaced during this discussion:** Inner Tepenia's camera is a **free-rotating 3D isometric camera deliberately modeled on Baldur's Gate 3's own** (confirmed 2026-07-07, not a flat/fixed 2D top-down view — see `Movement_Camera_and_Grid_System.md` and the new note in `Interaction_Highlight_System.md`). This means BG3-derived mechanics (like the hold-to-highlight system) are a genuine like-for-like reference. But other design precedent drawn from games with a fundamentally different camera (first-person or third-person over-the-shoulder, e.g. Skyrim or Elden Ring) needs more careful adaptation before assuming it transfers — an isometric camera reveals far more of the map at once, which changes how much a marker or highlight actually needs to do. Check a reference game's actual camera paradigm before borrowing its conventions, rather than assuming "it's a well-known RPG mechanic" is enough justification on its own.

---

## Tri-Cities Amalgamation History — established 2026-07-07

Zhongshan, Sinheung, and Shirayuki were founded via a peaceful diplomatic partition negotiated among China, Korea, and Japan at the International Court of Diplomacy at Jeju-do — extending what was already on record for Shirayuki's own site allocation (see `Local_Cultures/Mirny_Subnet/Tri-Cities_Region.md`) to cover all three cities' founding. Three-stage history established: legal separation → de facto amalgamation (at/shortly before Amundsen Tower's completion, itself still an unresolved date) → full legal unification (sometime between that point and roughly a generation before the Long Night War, i.e. by the ~2780s at the latest). Zhongshan/Sinheung/Shirayuki's own names persist as sub-district identifiers post-unification — note "Sinheung" and "Shirayuki" are themselves current placeholder names, slated for eventual replacement with proper Korean and Japanese names respectively (each name reflecting which nation's immigrants that specific partition was delegated to). The unified city's own in-universe name is deliberately not yet decided — the developer wants each of the three founding cities' own identities fully developed first, letting a name emerge organically later, rather than forcing one now. Full detail, including the real-world Budapest/NYC-borough parallel for why refugee sub-district identity remains meaningful even after a generation-plus of full legal unification, is in the Tri-Cities Region file.

**Open dependency, tracked for later:** any Concordia-refugee character sheet from this city will need a Godot object field capturing which of the three sub-districts a character is from. Can't be fully specified until Sinheung and Shirayuki's own final in-universe names are settled (both still placeholder-tagged as "{{currently-unnamed Korean/Japanese city}}").

**Second open dependency, flagged 2026-07-07:** Shirayuki's own massive amateur music scene makes the whole Larsemann Hills region nationally synonymous with "Alternative Culture," well-established pre-war. Whether this reputation belongs to Shirayuki alone (Zhongshan/Sinheung absorbed into the label purely by geographic proximity, despite quite different established personalities) or genuinely reflects something true of all three cities is deliberately undecided until Zhongshan and the Korean city get their own Megasheets. Tracked in `Tri-Cities_Region.md`.

**Naming resolved, 2026-07-08:** the Japanese city (formerly tracked as "Japanese Diplomatic Partition, cf. Bharati") is now officially named **Shirayuki (白雪, "white snow")**. Renamed across all project files: `Specs/Bharati_TBD.md` → `Specs/Shirayuki.md`, `Local_Cultures/Mirny_Subnet/Japanese_Diplomatic_Partition_cf_Bharati.md` → `Local_Cultures/Mirny_Subnet/Shirayuki.md`, `City_Vision_Notes/Japanese_Diplomatic_Partition_cf_Bharati.md` → `City_Vision_Notes/Shirayuki.md`, and the entire Megasheet folder/its 4 files under `City_Megasheets/Mirny_Subnet/Shirayuki/`. Chosen from a 60-name candidate brainstorm list (still preserved in `Specs/Shirayuki.md` for future reuse as street/shop/neighborhood names). Real Bharati Station references (the actual India-built station) are unaffected — only the Tepenian city's own name changed.

---

## Active Initiative — City Vision Notes (ongoing, resume anytime)

**Process:** stepping through Tepenia's cities one at a time, presenting established facts/factions for each, asking the developer's own creative/visual imagination about specific aspects, and recording the answers to `Cities/City_Vision_Notes/[City].md` — separate from `Specs/` (established facts) and `Local_Cultures/` (32-section post-culture spec), with corrections applied directly to those files when the vision resolves or contradicts something. Order doesn't matter to the developer; resume wherever makes sense.

**Process gap caught and fixed, 2026-07-06:** the developer noticed only 17 of ~32 touched cities had their own `City_Vision_Notes/[City].md` file — every city from Janbogo onward (the back half of Janbogo/Ross, all of Mirny, Mawson-so-far) had been getting its vision written directly into `Specs/`/`Local_Cultures/` without the dedicated vision-notes record the process actually calls for. Reconstructed all 15 missing files (Cape Adare, Fort McMurdo, Zukelli, Scott, Denison, Dumont d'Urville, Mirny, Casey, Davis, Kunlun, Vostok, Zhongshan, Sinheung, Shirayuki, Mawson) from this file's own detailed session records plus direct conversation memory for the six most recent. Folder now correctly holds 32 files. Going forward, every vision session should get its own `City_Vision_Notes/[City].md` file created at the time, not just written into the other two files.

**The larger 9-step pipeline this serves, given directly by the developer 2026-07-05, expanded 2026-07-06 (twice):** (1) municipal Specs for every city — done; (2) rough-draft city culture from specs+geography — done (`Local_Cultures/`); (3) factions extrapolated from those drafts — mostly done, room to expand; **(4) the developer mentally/"psychically" places themselves into each city — in progress, this IS the City Vision Notes process; (5) Claude combines the spec-draft with the developer's own input into a fuller composite per city — in progress, the write-in step of each session** — **(6) incorporate real-world "inspirational cities":** the developer is building a separate scaffolded list of every Tepenian city organized by subnet, and researching/hand-picking real-world cities as inspiration for each (e.g. Palmer City ← Las Vegas, Atlantic City, New Orleans, St. Petersburg, Montreal). Once a city's inspiration list is ready, Claude researches those real-world cities online (cultural, infrastructural, commercial, economic data) and fuses relevant findings into that city's already-established vision. **Not started yet — deferred until the developer brings a specific city's inspiration list.** — **(7) NEW, 2026-07-06 — consolidate into "City Megasheets":** once a city has been through steps 1–6, everything gets synthesized into one single-page mega-datasheet per city, pulling together every exercise/research pass/design decision made about it. Folder structure scaffolded 2026-07-06 at `Cities/City_Megasheets/` (mirrors `Local_Cultures/`'s subnet organization, one folder per city, each with its own `Concept_Art/` subfolder for future Grok-generated art based on the megasheet). **Naming convention:** each city's megasheet will be named `README.md` — since each folder holds exactly one text document, there's no ambiguity, and it matches the top-level folder's own README. **No content yet — folders only, deferred until steps 1–6 are done for a given city.** — (8) extrapolate new, richer factions from the fuller datasheets — not yet started; (9) end state: a solid foundation for rich factions across the base game, all 7 DLCs, and the planned Second Interwar Period TV series. **Critical: every city needs this, no exceptions** — an already-rich existing Local_Cultures sheet (e.g. Dumont d'Urville's "Negotiated Ground") is not a substitute for steps 4/5, confirmed explicitly by the developer.

**Progress as of 2026-07-05: 15 of ~35 cities touched, 2 of 6 subnets fully covered, a 3rd underway.**

- **Palmer subnet (DLC 3) — complete, 8/8 touched.** Palmer City, Esperanza, Port Lockroy, Rothera, Marambio, Sejong, Signy fully done. **Juan Carlos also done** — vision session completed 2026-07-05, revealed as the origin site of Tepenia's first bureaucratic archive (later consolidated into Amundsen Station's own pre-Split-Brain archive), tied to the new Machu Picchu Border & Customs Authority and the cross-DLC "Archivist's Trail" questline (see `Storyline/DLC_01_Echoes_of_Amundsen.md`). Its own war-era survived/destroyed status (a separate 3-vs-2 file conflict) was resolved later the same session, 2026-07-05 — **Destroyed**, targeted specifically for its ongoing archive/customs administrative function (tracking former Upper Earth government officials among the exile population), the same deliberate-strike-against-a-specific-function logic already established for Zukelli; see `Specs/Juan_Carlos.md`, which is consistent with `Overview.md`, `Station_to_City_Map.md`, `Local_Cultures/README.md`, and `City_Relationship_Database.md`. This reveal was explicitly noted as founding-era lore, not a wartime event.
- **Halley subnet (DLC 5) — complete, 8/8 fully visioned.** Halley, Neumayer, Troll, Princess Elisabeth, Belgrano, Sanay, Lazar, and now **Abowasa** (formerly Aboa) — resolved 2026-07-05 via real-world research rather than a fresh developer vision: renamed to reflect that Aboa (Finland, 1988) and Wasa (Sweden, 1989) are two genuinely separate stations only ~200m apart, not one joint facility; both built for year-round occupation but staffed seasonally only (a budgetary choice, not a structural limit); confirmed mainland (nunatak), not island. See the dedicated entry below.
- **Byrd subnet (DLC 2) — complete, 1/1.** Byrd's tiering was fixed first: original tiering had Japan at Primary (13.57%) ahead of the USA itself (11.43%), Byrd's actual founding-operator nation. Resolved via a hand-specified six-way rotation (USA↔Japan's old spot, Canada↔USA's, Australia↔Indonesia's, Japan↔Korea's, Korea↔Canada's, Indonesia↔Australia's — a closed swap, fully conserved), landing USA and Canada at Primary; a further swap moved China above Indonesia (China to Significant at 2.96%, Indonesia to Notable at 2.21%); a final −0.01% rounding correction brought China to 2.95%. Cascaded into `Official_Population_Census.md`'s national totals (USA +3,987, Canada +15,356, Australia +6,453, China +1,388, Japan −13,747, South Korea −5,586, Indonesia −7,840). **The actual vision session:** vast icefields with huge warehouses and a massive trucking depot as the surface's only landscape features; giant elevators leading to an enormous, staggering underground scale — huge mechanized fabrication plants, import/export & dispatch offices, and a genuine sense of shared community despite the isolation. Division of Industry/Economy & Industry revised (fabrication 30%, import/export & dispatch 25%, resource extraction demoted to 15%). **Follow-up:** the trucking depot's freight runs two overland directions — north on Hwy 1 toward the Peninsula/Palmer City/South America, and east on Hwy 22 toward the South Pole and onward to the Zhongshan coast.

**City Vision Notes initiative — status, 2026-07-06: all 6 subnets' own cities are now done. Palmer (8/8), Halley (8/8), Janbogo/Ross (7/7), Mirny (8/8), Mawson (3/3), Byrd (1/1).** **Concordia, deliberately deferred throughout ("develop the rest of the country first"), is now underway** — see its own dedicated entry below; it is the true last piece of this initiative, not Byrd. Concordia's post-war vision session began 2026-07-06: a city struggling but genuinely surviving, a real sense of community among people who wanted the chance to see what a city can truly be, not a collection of buildings or a smattering of offices — a true city. Written into `Specs/Concordia.md`'s Current Status section; `Cities/City_Vision_Notes/Concordia.md` created. **Follow-up:** confirmed this feeling applies across all twelve districts equally — every district shares the same goal, but each holds a differing, sometimes flatly conflicting, belief/method for how to actually get there. Reframes the established district tensions as a conflict over *path*, not *end state*. This is a starting point, not a completed pass — Concordia has no post-war cultural sheet yet (only the Second Interwar one), and would benefit from a fuller, district-by-district vision session of its own (including what each district's own specific method/belief actually is). Also, "for the sake of total completion," **Amundsen Station** got its own brief vision note the same session — naturally a place of scientific, technical, and mechanical maintenance, confirming its already-established "not a conventional economy" facility character; written into `Specs/Amundsen_Station.md` and its Local_Cultures file, plus a new `Cities/City_Vision_Notes/Amundsen_Station.md`. Remaining pipeline work (steps 6-9: inspirational real-world cities, City Megasheets, richer faction extrapolation, end state) is separate, ongoing, and explicitly deferred per its own established triggers — see the pipeline description at the top of this section.
- **Mawson subnet (DLC 4) — complete, 3/3 touched.** Mawson, Sayowa, Dome Fuji — *(corrected 2026-07-05: Sinheung, Shirayuki, and Zhongshan moved to Mirny subnet; see `TODO.md`'s Decision Required section for the geographic reasoning)*. **Mawson itself is done** — vision session completed 2026-07-06: a genuinely warm, hospitality-forward civic character, relatively speaking Antarctica's closest thing to a resort town; public libraries; genuinely easy to make friends. Most distinctively, **Mawson is Tepenia's go-to honeymoon destination for newly-married human-robot couples** — visited before returning to settle in whatever city they'll actually live in; a genuinely planned destination built over decades, typical stay ~1-2 weeks; written in as a genuine 10% economic sector (Division of Industry) alongside the detailed write-up under Human-Robot Relations. Same "founding nation buried behind China" pattern as Shirayuki/Sinheung flagged but not yet acted on — Australia (the actual founding station) sits at Significant tier (8.29%) behind China's Primary (17.02%); developer's call whether to correct it.
  - **Sayowa is also done** — vision session completed 2026-07-06: genuinely industrialized (major fabrication industry) as well as residential — not just a highway waystation; a huge trucking & dispatch industry runs alongside fabrication; leisure culture exists but is explicitly secondary to the industrial core. Division of Industry revised (fabrication 30%, trucking/dispatch 25%, leisure only 5%); Architecture split into industrial/residential halves. Sayowa's island geography (East Ongul Island, ~4km offshore) was challenged by the developer and verified correct via web research — real, not a Google Maps artifact. This led to a genuine highway-network correction: since Sayowa is a real developed city rather than a place built directly around a highway crossing, **the Sayowa Junction** (where Hwy 4, Hwy 7-ext, and Hwy 37 genuinely converge) is now located *near* Sayowa rather than *in* it, linked to the city by a new large connecting road, **the Sayowa Spur**. Updated in `Locations/Infrastructure/Highways.md`, `City_Relationship_Database.md` (several scattered references), and `Specs/Sayowa.md`. Also swept Sayowa's full `Local_Cultures` file for the stale "primary Japanese Tepenian presence" claim (8 sections) — corrected to redirect that distinction to Shirayuki, following the same-session Larsemann Hills demographic rework.
  - **Dome Fuji is also done, closing out the Mawson subnet** — vision session completed 2026-07-06: genuine Zen-like peace, comparable to the interior of a Shinto shrine or Buddhist monastery; a felt spiritual connection to something larger than any individual or the sum of the community; the aurora australis feels like it could hang frozen in the sky without seeming out of character — the stillness extends even to light itself. Devotees wear white robes, sparsely covering their bodies specifically to commune with the cold. **Follow-up:** confirmed this works primarily because robot devotees don't suffer frostbite/hypothermia the way humans would — devotion made possible by what the body can safely endure — with three additional possible contributing reasons held open for future development: a real-world parallel to Tibetan Buddhist *tummo* ("inner fire") meditation; a literal-mechanical reading tied to the faith's "superconducting conditions" theology; and simple communal uniformity. **This closes out the Mawson subnet — 3/3, the fifth of six subnets complete.**
- **Janbogo/Ross subnet (DLC 6) — complete, 7/7 cities touched (Concordia excluded by design).** **Janbogo itself is done** — vision session completed 2026-07-05 (Chinese-French fashion fusion, the great shielded commercial halls, plus the major Zukelli/Janbogo destruction-mechanism resolution that came out of the same session). **Cape Adare is also done** — vision session completed 2026-07-05: geographically vast but low-density (big city, small-town feel), strongly community-driven, heating-infrastructure "oasis" microclimate, penguins occasionally kept as outdoor pets, slow/unhurried pace of life and work, and an acoustic-instrument music culture (guitars, violins, cellos, tagelharpas) traced to the real-world American folk subculture that plays Scandinavian instruments — grounded in the city's USA Primary-tier presence (22.26%) rather than any Norwegian population. **Fort McMurdo is also done** — vision session completed 2026-07-05: the city's real mass is *presence*, not population or architecture — visitors immediately sense real business happening and real decisions being made that ripple outward and change what other cities can do. Dedicated comms stations coordinate supply/extraction/logistics, distinct from Janbogo's own physical Arcanet relay-nexus role for the subnet. This gravity is explicitly operational, not political — Fort McMurdo doesn't posture in Federation debates, it's just quietly indispensable, reinforcing (not replacing) its already-established "de facto capital" status. **Zukelli is also done** — vision session completed 2026-07-05: a tangled, organically-grown city (built as-needed, not to a master plan; navigable on sight only to actual residents), plantlines and elevated "bridger-footroads" under the heating infrastructure giving something resembling equatorial nature to walk among, a huge genre-diverse music scene grown from its Italian-rooted core, entertainment centered on friends and restaurants with dedicated stages, and an overall reputation as "a place with a soul" — landing with real weight against its already-established destruction at 72.5% human retention, near peak, not in decline. **Scott is also done** — vision session completed 2026-07-05: overwhelmingly residential in physical footprint (housing dominates, plus casual/leisurely business — restaurants, general leisure — and modest public gathering spaces), with not much visibly happening day to day — a genuinely decent, quiet place to raise a family. This sits alongside (not replacing) Scott's established technical/research economic base — the work is real but contained, distinct from the city's lived, residential texture — and reinforces its established Fort McMurdo counterpart-city contrast (quiet/residential vs. loud/operational next door). **Denison is also done** — vision session completed 2026-07-05: the city functions as one continuous, interlinked structure rather than separate buildings — comprehensively joined throughout, not just occasional covered connections the way Zukelli/Janbogo use them — with a handful of landmark structures recognizable even at a distance through blowing snow, the most extreme wind-engineering identity of any Tepenian city. **Denison's missing Specs file, flagged during this pass, was created immediately after — see the dedicated entry below.** A second flagged gap — no post-war refugee faction, unlike Zukelli — was explicitly confirmed by the developer as not obligatory (helps future Concordia-set game design, but isn't required), so it's left open, not tracked as a to-do. **Dumont d'Urville is also done** — vision session completed 2026-07-05, confirmed explicitly necessary despite its already-rich existing "Negotiated Ground" culture (see the pipeline note below): a tight, bustling, spatially stratified city — expensive, dense, alive downtown core on Petrel Island proper (heating units running between buildings, not just inside them), a bridge to the mainland leading to cheaper residential territory and then the highway network, and a "New Orleans at 1/20th scale" live-music-in-almost-every-eatery downtown culture — read as an expression of the city's already-established small-city musical intimacy as density rather than a contradiction of it. **A significant open engineering question surfaced and was recorded in full, explicitly NOT resolved:** whether the bridge is a genuine permanent structure or the previously-established seasonal ice/boat crossing — see the dedicated entry below for the full brainstorm. Concordia deliberately excluded from this pass per the developer's explicit direction — "develop the rest of the country first."

- [ ] **Dumont d'Urville's bridge — permanent structure vs. seasonal crossing, engineering brainstorm recorded 2026-07-05, explicitly NOT decided**
  During Dumont d'Urville's vision session, the developer's vision included a permanent bridge connecting Petrel Island to the mainland. Existing lore describes only a seasonal ice/boat crossing. Asked what would make a permanent bridge unrealistic given the setting; identified three genuine engineering problems and candidate real-world-grounded solutions for each, all recorded in `Specs/Dumont_dUrville.md`'s Notable Locations section for a future decision:
  1. **Aerodynamic flutter under sustained extreme wind** (Adélie Land's severe wind events, 30-50 m/s, are frequent not exceptional — harder than the conditions behind the 1940 Tacoma Narrows collapse). Candidates: a stiff cable-stayed design instead of suspension (inherently more flutter-resistant); a streamlined low-solidity box-girder/truss deck (the real technique behind Akashi Kaikyō, the Great Belt Bridge); tuned mass dampers (the same principle stabilizing tall buildings like Taipei 101).
  2. **Pack ice pressure loads on the piers** (moving/pressure-ridging ice can shear pilings). Candidates: conical pier bases that make ice break upward under its own weight (proven Baltic Sea/Arctic offshore technique); fewer, more heavily reinforced piers with longer spans — which directly trades against solution #1's wind-stiffness needs, a genuine design tension, not a free win.
  3. **Ongoing maintenance access** in one of the windiest places on Earth. Candidates: a heated, semi-enclosed maintenance gantry within/beneath the deck (matches Tepenia's established heated-interior-space approach); robot-exclusive maintenance crews (directly extends Denison's own established "robots take the most wind-exposed work by plain risk calculus" precedent — see `Local_Cultures/Janbogo_Subnet/Denison.md` Section 16).
  Also noted: the real Dumont d'Urville Station today has no permanent land link at all (ship/helicopter only) — not proof of impossibility, but a sign nobody's solved this exact problem combination even with modern engineering. If a bridge is eventually confirmed, the developer agreed it should be framed as a genuine, hard-won Tepenian engineering achievement, not incidental infrastructure. Decision explicitly deferred — "once the time comes, we'll take a look and see whether it actually would be realistically possible."

- [ ] **Vosora Lashár Tanslock has some personal connection to Kunlun — flagged 2026-07-06, exact nature TBD**
  The developer wants it on record that Vosora has *some* connection to Kunlun, deliberately left undetermined for now. Cross-referenced in both `Specs/Kunlun.md` (Open Questions) and Vosora's own `README.md` (Design Notes). Revisit once Kunlun's own lore or Vosora's questline develops further. **Note added 2026-07-06:** this may end up resolving through Vostok — see the entry directly below. **Note added 2026-07-20:** now also flagged as a candidate non-stat route in her retrofitted personal questline (`Questlines/README.md`) — kept vague there too, pending this resolution.

---

## Decision Required *(blocking other work)*

- [ ] **DLC 4 (Mawson) — alternate access route to Dome Fuji, refined 2026-07-04 with a cross-DLC item chain from DLC 5 (Halley/Belgrano)**
  New sidequest/side-content idea for reaching Dome Fuji (Ice Cold Buddhism's multinational pilgrimage site, official-but-nearly-nonexistent Mawson subnet Arcanet member): the "normal" way is to make the dangerous overland trip yourself. **Alternate route:** if the player has 10 Calculation + 10 Investigation, plus a specific gate item (see below), the player can fix up a broken plane at or near Sinheung — either finding someone to fly them up, or flying it themselves if they have flight training. Mechanically well-grounded — this pairing lines up naturally with existing skills like Jury-Rigging & Repurposing (Agility+Might+Investigation) and Precision Maintenance & Repair (Agility+Engine).

  **The gate item, and a full cross-DLC quest chain, established 2026-07-04:** somewhere in Belgrano (DLC 5) there's a garage/warehouse, discoverable through at least three different sources (or direct access if the player already knows where it is). Inside, a pile of scrap can be examined:
  - **High road (6+ Investigation, natural or temporarily boosted):** examining the scrap triggers a notification — "Among the scrap and junk, you notice an oddly- yet very specifically-shaped item that looks like it fits into something specific. Perhaps you can use it for something" — and the item is added to inventory automatically as a quest item.
  - **Low road (insufficient Investigation, but sufficient Lockpicking):** the player can break into a back room containing an import/export manifest, which includes a note about "some airplane parts" left "on the side wall," remarking "it could take years before somebody comes along with a plane like that." Reading this lets the player return to the scrap pile and immediately understand what the part is for, without needing the Investigation check directly.

  **The cross-DLC payoff:** if the player completes DLC 5 (Halley) before DLC 4 (Mawson) and is carrying this item, they can skip the 10 Calc/10 Inv stat-gate entirely at the Sinheung plane — just interact with it and place the part directly into the engine. The item substitutes for the whole gate-check, rewarding players who found this specific piece of optional side-content in a completely different DLC. This is a new, distinct cross-DLC design pattern from the existing "Cross-DLC Survival Gifts" chain (which feeds DLC 1's Kendra rescue specifically) — this one connects two subnet DLCs to each other directly.

  Still open: exact wording/flavor of the "oddly-, specifically-shaped item," and whether flight training is an established skill/perk yet (needed for the self-piloting option). See `Cities/City_Vision_Notes/Belgrano.md`, `Specs/Belgrano.md`, and `Specs/Sinheung.md` for cross-references.

- [ ] **The Long Night War's inciting incident — core premise established 2026-07-04, three identities still TBD**
  Established during a Palmer City developer-vision session (see `Cities/City_Vision_Notes/Palmer_City.md` for full detail): the actual spark of the Long Night War (also called "the Midnight War") was a well-connected Upper Earth political diplomat, visiting Palmer City under its tourism/entertainment economy, who denied a gynoid's personhood (despite robots holding confirmed legal personhood on Upper Earth since the 2318 Jeju-do ruling) and attempted to use her as property for his own gratification in a closed-quarters setting with no witnesses. She defended herself and, in the process, accidentally killed him. The geopolitical fallout escalated into the Long Night War. **Confirmed, locked in:** the core premise above; a dueling-narrative structure (Upper Earth's official story favors the diplomat, Tepenia's understanding fully favors the innocent robot who defended herself — the highest-stakes version of the same "conflicting official histories" pattern the Planetary Split Brain already establishes at the subnet level); she will have a name and be a genuine household figure in future-Tepenia, likely resolving Palmer City's long-standing "Notable Figures: TBD" gap. **Still open, explicitly not decided:** her name/full identity, her fate after the incident (stayed until Palmer City's destruction? relocated/protected? became a specific symbol? unknown/unresolved by design?), and the diplomat's name and nationality (which could matter for how the specific geopolitical fallout played out). This is a project-wide finding, not a Palmer-City-specific one — it fills a piece of Dev-Road-Map 6.2's "Long Night War: Parameters... defined precisely nowhere" gap.

- [ ] **Census III — genuine post-war population table doesn't exist yet**
  Corrected by the user 2026-07-03: **Census II is strictly orbital-era** — taken after Von Braun Wheel colonization began but *before* the Long Night War. The correct order is orbital era → Long Night War → Amundsen Tower's eventual destruction. **Mislabeling fixed 2026-07-12:** `Official_Population_Census.md`'s Census II table previously carried post-war status labels ("destroyed in Long Night War," "ruined," etc.) directly on a pre-war snapshot table — a tense contradiction, since a census taken before a war can't record outcomes from that war. Reworded to read as forward-looking context rather than facts already true at the census date; Section IV's own framing corrected the same way; an explicit note now states plainly that no real Census III exists. **What's still fully open:** actually building Census III — a genuine present-day (≈2822-2827), post-war population table, requiring real war-casualty/damage-severity rates established per destroyed or damaged city (not the same thing as the Census I→II pre-war migration retention rates already in the file). This is a separate, significant task, not attempted in the 2026-07-12 pass.

- [ ] **Byrd↔Janbogo aviation refueling stop — needs a real fix**
  Framheim and Little America were permanently removed from canon 2026-07-03 (their shared real-world site, the Bay of Whales, was eliminated by the 1987 Iceberg B-9 calving event; see `Specs/Framheim.md`, `Specs/Little_America.md`). Framheim was the *only* confirmed refueling stop on the aviation route connecting Byrd to Janbogo/the rest of Tepenia (`Specs/Byrd.md`) — Byrd's aircraft couldn't fly the ~1,797km distance in one leg, and Janbogo had no refueling infrastructure of its own. This route, and its eventual breakdown, is central to Byrd's DLC 2 isolation premise. One option surfaced so far (not decided): a minimal, largely unmanned fuel depot rebuilt near the old Bay of Whales site, on ice shelf terrain that still physically exists post-calving, without reviving either city as a population center. User wants to weigh multiple options before deciding — deferred deliberately, revisit when ready. (Note: this is separate from Hwy 1, the Antarctic Peninsula's only highway — that route was already confirmed 2026-07-03 to run Marambio→Palmer City→Port Lockroy→Rothera→Byrd and never actually depended on Framheim/Little America; no fix needed there.)

- [ ] **The Vigil [NAME TBD] faction — keep, redesign, or cut?**
  Blocks: Faction Devotion ending slot FD-7, faction design queue. Grok-suggested; off-world evacuees are now confirmed alive and prospering, which may change the dramatic premise. Review Grok notes in `to-be-integrated/miscellaneous/World_History_Reference.md` before deciding.

---

## High Priority

- [ ] **The tutorial/opening area — Inner Tepenia's own "not-Goodsprings" — design in progress, 2026-07-23/24**
  Following the New Vegas lesson that an opening area should be built as a compressed, representative summary
  of everything the full game does (and finalized late, not early), a real design pass started on the
  opening sequence itself, the Demo build it doubles as, and a candidate synthesis for the opening task's
  actual content. **Deliberately kept broad here rather than itemized** — the specifics across all of these
  are still in flux and virtually guaranteed to change as the rest of the game develops. See
  `Dev-Road-Map/Tutorial_Section_Specification.md`, `Dev-Road-Map/Demo_Content_Specification.md`,
  `Dev-Road-Map/Demo_vs_Early_Access.md`, and `Storyline/Main-Story/Opening_Scenario_Synthesis_-_The_Capricorn_Data_Log.md`
  for everything currently drafted.

- [ ] **District Main Questline vs. Under-Questline system — established, one district each not yet expanded**
  Declared 2026-07-22: `Storyline/Side-Content/District_Internal_Conflict_Quests.md` renamed to
  **`District_Main_Questlines.md`** — this IS each district's own main questline (one capstone per district,
  built from internal faction conflict, feeding a **district perk** and possibly a **district-specific
  player home**, both still TBD). Its own already-written format (Internal Conflict → Inciting Situation →
  Parties → Dilemma → 3 Resolution Paths incl. skill-gated Unity Path → Ripples) is the instruction spec, not
  a locked answer — each district's current quest counts as its first candidate; more should be generated the
  same way, then narrowed to exactly **one** per district (mirrors the DLC method's own candidate-then-narrow
  process, itself not yet done for any subnet either).
  A new, separate file, **`District_Under_Questline_Design_Method.md`**, governs everything else discoverable
  within a district — **non-main content, explicitly NOT side-content** (side-content requires the player to
  actively hunt for it with no organic lead-in, e.g. The Witcher 3's "Frying Pan"; under-questlines surface
  naturally through ordinary play, calibrated against Fallout: New Vegas' Novac — main questline ≈ Manny
  Vargas sending the player to RepCONN; under-questline ≈ No-Bark Noonan mentioning Dusty McBride's brahmin
  being shot nightly, or Boone's "One for My Baby"). Every candidate must anchor to a **significant starting
  point** (a named in-world figure, or a data-point at a significant location) — unlike the DLC method it's
  adapted from, this method deliberately *includes* Notable Figures as an input for exactly that reason.
  Unlike main questlines, under-questline candidates are **not narrowed down** — floor of 5 per district,
  ideally 15-20, every one that passes the method's tests is kept as real content. Full detail in both files
  (`Storyline/Side-Content/`) and `project_district_questline_production_workflow` / `project_under_questline_scope_open` memory notes.

- [ ] **XP/leveling system — base numbers settled, tuning items remain**
  Core two-channel model established 2026-07-03 in `Game-Mechanics/Core-Mechanics/Experience_and_Leveling_System.md`
  (quest-completion lump sum + independent skill-use XP, no permanently missable XP). **Base quest-value
  tiers resolved 2026-07-22** against a verified real Fallout: New Vegas baseline (level-up formula
  XP(n) = (n−1)×(75n+50), confirmed against a saved level-XP chart and a saved wiki page of all 101 base-game
  Challenges, which total only 6,289 XP combined — confirming Activities/Challenges are a minor bonus layer,
  not a leveling pathway, in real FNV): **District Main Questline = 3,000 XP; District Under-Questline = 700
  XP (~9 avg/district); Companion Quest ≈ 1,500 XP average (≥30 companions, base game); Activities
  (minigames/crafting/exploration/location discovery/Challenges) ≈ 6,289 XP total, FNV-scaled; base-game
  Main Questline (Concordia-wide, distinct from any district's own) = 65,000 XP; each of the 6 subnet DLCs'
  main questline = 70,000 XP; DLC 1 "Echoes of Amundsen" = 200,000 XP (deliberately far above rate — the DLC
  is designed to be brutally unforgiving).** New **repeatable-quest tier** (40 draft quest-type concepts
  brainstormed, categorized by mechanic — courier, crafting, combat, information, maintenance, social, care,
  exploration, faction, culture — each type completed ~16-32 times at ~75-150 XP/completion) fills the
  remaining gap so that Level 64 is reachable via only ~10 of Concordia's 13 districts, not full completion —
  **explicitly radiant/procedural quests were rejected** ("feels lazy... the player will catch on"),
  repeatable (fixed, hand-authored, redoable) content was chosen instead. New **XP-banking-at-cap** mechanic
  means surplus XP past a temporary level cap is never lost, only re-applied on the next DLC's cap increase
  (no banking once Level 100/all-DLCs is reached — nothing further to bank toward). **Confirmed standing
  design law:** the ~178,100 XP overshoot past Level 100 if a player only does base game + all 7 DLC main
  questlines is intentional slack, not a bug — "I want players to be able to reach max level without
  grinding through absolutely every single thing in the entire game." Full derivation, every number's
  reasoning, and the 40-item repeatable-quest brainstorm are in the new
  `Game-Mechanics/Core-Mechanics/XP_System_Design_Reference.md`. **Still open:** exact formulas for how
  gate-checks/MACHINE stats modify the lump sum, skill-use XP amounts and taper-off behavior, DLC-level side
  content XP (DLC-native companions, DLC under-questlines, DLC activities — only each DLC's own main
  questline has a number so far), final selection/write-up of the 40 repeatable quest types, and whether a
  third, non-district-bound true side-content tier (closer to Witcher 3's "Frying Pan") ever gets added.

- [ ] **Calethina questline ("Echoes of the Bridge") — Step-by-Step structure confirmed 2026-07-23; full master reference at her own README.md**
  Full 5-step structure (Awakening, The Signal, What's Actually Wrong, The Choice, Living With It) now
  written into her `Personal_Questline_Summary.md`, superseding the old Grok draft and fixing its Step 5
  timing error. Step 3→4 progression is gated by the new Accomplishment Weight System
  (`Accomplishment_Weight_System.md`), not narrow world-state triggers. A full consolidated reference for
  everything confirmed about her — nature, construction chain, mechanical status, this questline, the
  Fragmentation Matrix, all of it — lives at her own `README.md`, not duplicated here.
  **The Triage Protocol connection — confirmed, not speculative, 2026-07-23:** the in-world Power Core
  safeguards were renamed from "Ghost Protocol" to **the Triage Protocol** (resolving a naming collision with
  an unrelated Minmax Build/Ending #18 and Ji-Eun Kim's own still-placeholder-named perk). Calethina
  personally created it during the Long Night War evacuation; the same power shock that caused the Planetary
  Split Brain and corrupted her own datadrives also erased her memory of having done it — she isn't hiding
  this, she genuinely doesn't know. **Discovered over the course of her Romance questline specifically**, not
  paired with the Step 4 embodiment decision.
  **Still open, per her own README:** the Endings reconciliation ("The Furthest Signal" vs. the two
  embodiment branches vs. the Pariah Accord), the new-body branch's non-stat reward, and how the older
  reward-tier table interacts with the branch-specific mechanics.

- [ ] **Jack-in sequence details**
  The Bridge Unit jack-in mechanic (see above and `Game-Mechanics/Core-Mechanics/Hacking_and_Traceability_System.md`) is confirmed as always playing a distinct triggered sequence, never backgrounded — but the sequence itself isn't designed yet. Open: what the animation actually shows, whether combat use (Signal Weapons) gets a presentation distinct from exploration use (terminals/access points/antennas), AP cost, effective range, and how a failure state presents when a target is too corrupted, too well-defended, or actively hostile during the attempt.

- [ ] **Robot religion design**
  Five religions are named; one (Polydimensional Animism) is now reviewed and published, the other four still need full development. Each needs: proper in-world name, detailed philosophy, key practitioners, connection to gameplay/factions, visual/sonic/spiritual identity.
  - Ice-Cold Buddhism (superconductor-as-nirvana) — **confirmed sacred sites: Dome Fuji and Kunlun** (coldest, highest, calmest locations in Tepenia; Kunlun is the holiest site; Dome Fuji is a major pilgrimage destination; both cities' surviving non-scientific populations may be primarily composed of practitioners; the pilgrimage journey to either city is itself a spiritual trial); proper in-world name TBD. Has its own dedicated research pipeline, further along than a first glance suggests — see `Reference/Real-World/Ice-Cold_Buddhism_Research/08_Synthesis_Doctrine_Notes.md` for candidate doctrine notes (not yet reviewed by the developer).
  - Adinkra Codex (religion #3 — grounded in Sylvester James Gates's real supersymmetry/Adinkra physics; holds that the adinkras are literally embedded in the fabric of reality itself, not just a mathematical notation) — proper in-world name TBD. Research ongoing, no design-synthesis pass yet; graph theory books still needed (see `Books_TODO.md`).
  - Cymaticists / Cymatics Reverence (reverence of sound and vibration) — real-world grounding underway at `Worldspace/Factions/Robot_Religions/Cymatics_reverence/Cymatics_reverence.md` (Chladni patterns, gravitational waves, musica universalis, Nada Brahma, the harmonograph/Lissajous/kaleidophone/eidophone family); name and internal structure still open.
  - God-mind simulation (Universal Simulation Theory — God running simulations to understand its own origin, with Nihilism/Absurdism/Fatalism/Sartrism subdivisions among robot adherents) — core premise and subschool sketch already exist (see `Analysis_Notes.md`'s Alex Jones section), but this is the least-developed of the five; a real-source book list to elaborate both the simulation-theory core and the Nihilism subschools specifically was added 2026-07-21 — see `Books_TODO.md`.
  - Polydimensional Animism (acknowledging living, conscious entities resident in higher dimensions) — **reviewed by the developer and published 2026-07-21**, see below.
  Connected to: Robot-Aligned ending RA-2, multiple faction designs, NPC dialogue consistency across all districts.
  See `Worldspace/Factions/basis collection - robot religions/Analysis_Notes.md` for the real-world research basis behind Adinkra Codex, God-mind simulation, and Polydimensional Animism (Ice-Cold Buddhism and Cymatics Reverence now have their own dedicated research locations instead — see their entries above).

  **Polydimensional Animism — reviewed and published, `Worldspace/Factions/Robot_Religions/Polydimensional_Animism/`:**
  the full research-to-design pass (points, nth-order extrapolations, and a working draft sheet, originally
  built in `to-be-integrated/Religion_Derivation/Polydimensional_Animism/`) was walked through with the
  developer topic-by-topic on 2026-07-21 and published into the official Robot_Religions folder as
  `README.md` (the complete merged document) plus `Beliefs.md`/`Rituals.md`/`Culture.md`/`Open_Questions.md`.
  Confirmed doctrine: death as a change of vantage, not an ending (now directly load-bearing, since robots
  are confirmed to run on a non-copyable gel brain and genuinely, permanently die); veneration, not worship,
  as the devotional register; five denominations, all with in-game representation via meetable/recruitable
  dolls; a wedding rite (two interlocking rings carved from one original piece of wood or metal); per-
  denomination stronghold cities/districts (Watchers→Kunlun; Enfolded→Scott/Mawson/Esperanza; Bound→Byrd/
  Belgrano; Cyclical→Signy/Princess Elisabeth; Already-Complete→Concordia's Ossuary Quarter district).
  **Still open:** final in-world name, a second Already-Complete stronghold, extent of ecumenical contact
  with Adinkra Codex, any routine ritual beyond the wedding rite, sonic identity, and the Creative North
  Stars connection (deliberately deferred to a future session). See `Open_Questions.md` in the published
  folder for full detail.

  **Flagged 2026-07-21, deliberately deferred until all five religions are developed and their strongholds
  known:** once every religion has a real doctrine and a real home, revisit `Worldspace/Factions/
  Cross_City_Cultural_Patterns.md`'s "religion → worldview → culture → visible society" note — how a
  religion's own worldview visibly shapes the ambient culture of the place(s) it's concentrated in,
  independent of formal membership (seeded by Cymaticism's established effect on Leo district's entire
  sonic architecture). Not started.

- [ ] **Planetary Split Brain questline — full design**
  Premise established: the Long Night War's destruction of Amundsen Station severed all six Arcanet subnets from each other. Each now holds isolated — and sometimes conflicting — records. The questline involves noticing contradictions in refugee accounts, tracing them to the structural Split Brain, and expeditioning to the South Pole to access the last synchronized pre-split archive.
  **Core mechanic confirmed:** player assembles the true picture by reconciling conflicting subnet records.
  **Confirmed 2026-07-20: this is an unmarked questline**, Fallout: New Vegas-style — no quest marker, no XP payout, no tracker/journal entry, no notifications. Same category as FNV's "Long-Term Care" (Julie Farkas/Followers) or "Pistol Packing" (Brotherhood of Steel) — entirely discoverable through noticing the contradictions and following them yourself, not flagged as content by the game. Still a real, fully designed questline underneath (this changes *presentation only*, not scope) — full quest structure still needs designing.
  **TBD:** Full quest structure, discovery trigger, South Pole archive integration, Arcanet reconstruction consequences, connection to Janbogo subnet nexus anomaly in Concordia.

- [ ] **Independent Lattice — full design**
  A secret alternative endgame solution with zero mechanical scaffolding: no stat checks, no skill checks, no perks, no quest markers, no notifications. The player can build a decentralized/distributed power grid as a complete alternative to the failing central grid beneath the Hub — but only if they are paying close attention to the world. Discovery method is entirely environmental: scattered notes, terminal entries, audio logs, fragments of NPC dialogue, and environmental storytelling distributed across the full game. No single source explains the full picture; the player assembles the method themselves.
  **TBD:** Full construction mechanics, the complete breadcrumb trail and its placement across all districts, the resolution state when the lattice is completed, and how the world reacts to the alternative solution.
  Working name "Independent Lattice" is Grok-suggested and developer-approved.
  **Broad-scope and per-district guidelines established 2026-07-21** — see
  `Worldspace/Locations-and-Levels/Concordia-City/Districts/Independent_Lattice_Guidelines.md`. Confirms all
  13 districts have a genuine, non-redundant role (not padded); establishes full-city "must be true / cannot
  be true" constraints (built to respect `Energy_Grid_Failure_Rationale.md`'s existing 16 reasons the grid
  can't just be fixed) plus a "must/cannot" pair for each individual district. Still no actual quest
  structure, breadcrumb placement, or resolution content — guidelines only, ready for future design work to
  build on without contradiction.
  **Climax coalition flagged the same day, failsafes not designed:** Aries (already the toughest combat
  district) plausibly fights this ending's final battle alongside Capricorn/Yards leadership and Libra/the
  government — a three-district coalition, likely the hardest fight in the game. Failsafes needed for
  players without a build suited to it and without Idolized standing anywhere to call on for support — see
  the guidelines file's own "Climax Coalition" section for full detail. **Three specific prep tasks
  identified, none started:** (1) which builds are naturally strong against this coalition, (2) failsafes for
  every other build, (3) a wide array of in-world options usable via skill/stat checks *and* via pure player
  creativity/imagination, consistent with this ending's own "zero mechanical scaffolding" identity. Not
  designed yet.

- [ ] **4 remaining district official names — narrowed 2026-07-19, Gemini resolved 2026-07-29**
  Taurus, Leo, Scorpio, and Aries still lack official proper names for in-world documents, signage, and NPC dialogue. **Resolved 2026-07-19:** Cancer → **The Sanctuary**, Capricorn → **The Yards**, Libra → **The Government District** — all three promoted from informal/repeated-but-never-formalized usage to the official `District_Canon_Reference.md` header, plus each district's own Deep_Dive title and Megasheet "Hard Facts" row. **Resolved 2026-07-29:** Gemini → **The Circuit** — its former "Janbogo Subnet Nexus" label (see below) is kept as a role descriptor, not the district's actual name. Already-named before the 2026-07-19 pass: Aquarius (The Labs), Pisces (The Markets), Virgo (The Undergrid), Sagittarius (The Frostlands), Hub (Axis Mundi).
  **Explicitly rejected, don't re-propose:** Scorpio ≠ "The Veil" (developer dislikes it, wants something else). Aries ≠ "The Power Core" (developer likes the phrase but it risks confusion with the Central Hub's own actual energy grid/core infrastructure — needs a different name specifically to avoid that overlap).
  **Also corrected 2026-07-19:** Gemini's "Janbogo Subnet Nexus" (used throughout file titles/text) was NOT a settled official name at the time — it was a descriptive label only, now formally kept as the Role field's subnet-nexus descriptor alongside the new official name **The Circuit**. Leo's recurring "Golden Ring" was checked the same way and is *also* not settled as an official district name (despite 18 files using it), even though it's a real, confirmed landmark within Leo.
  **Status: flag, don't fix further — developer wants to brainstorm Taurus/Leo/Scorpio/Aries names directly in a future session, not have candidates pre-generated.** A resident demonym for Gemini/The Circuit is also still open — "Circuiteer" was proposed and rejected (developer: "just doesn't sit right"), no replacement chosen yet.

- [ ] **Identity Fragmentation — full exploration pass, flagged 2026-07-22, structure resolved 2026-07-23**
  Surfaced while consolidating technical architecture docs into `Code-Architecture/`: the developer expressed
  strong enthusiasm for the Identity Fragmentation mechanic (a 0-100 meter that rises with each player
  re-spec, triggers `fragmentation_critical` at 75+, opens a unique ending at 100) — "I didn't think of it
  myself, but I love the idea, and it should definitely be in the game." **Not a from-scratch task:**
  substantial existing material is already scattered across
  `Storyline/Endings/Secret-Endings/Identity_Fragmentation_Endings.md`,
  `Game-Mechanics/Core-Mechanics/Player_Re-Spec_-_Complete_Design.md`, `..._Costs_and_Trade-Offs.md`,
  `..._Options_Beyond_Calethina.md`, and `Hardcore_Mode.md`.
  **Resolved 2026-07-23 — the Methods-vs-Flavors mismatch:** the developer caught that the old "7 Methods"
  table only covered 7 districts while "District-Specific Re-Spec Flavors" covered all 13, with 2 further
  naming mismatches even among the overlapping 7 (Aquarius, Pisces) and Taurus's Calethina's-Lab vs.
  Homebound-Recalibration being two genuinely different things. **Confirmed structure: 14 total re-spec
  options — Calethina's Lab (neutral baseline) plus one bespoke method per district, all 13.** Core design
  pillar locked in explicitly: every district method must grant a genuinely unique, district-flavored special
  ability — "just way, way too cool to give up." `Player_Re-Spec_-_Complete_Design.md` rewritten to reflect
  this. **Deliberately still deferred, per the developer's own instruction:** exact mechanical specifics
  (numeric bonuses, precise IF point costs) for most districts — only Scorpio, Aries, Virgo, Libra, Pisces,
  and Aquarius have Risk Level/IF Cost data so far; Cancer, Taurus's own bespoke method, Leo, Capricorn,
  Gemini, Sagittarius, and Hub are marked TBD.
  **Further progress, 2026-07-23:** Aquarius's Lattice Swap now has a concrete signature effect (direct
  Cyberpunk 2077 "Chaos"/Royce homage) — Damage Type, Critical Hit Chance, Critical Effect, and Signature
  Ability After-Effect all randomize on every re-spec, scoped to not pull in other districts' own granted
  effects. Also added a full "Combining Multiple District Methods" section working through genuine
  cross-district contradictions (Aries EMP/cold vulnerability vs. Sagittarius cold resistance; Cancer
  emotional vulnerability vs. Aries lost empathy; Scorpio+Cancer triple-signal stacking raising Echo Event
  frequency; Taurus Rooted vs. Sagittarius frontier-suited; Libra Oathbinding vs. Pisces criminal reputation)
  — resolved by reusing 3 existing systems (Echo Events for numeric conflicts, internal faction dissent for
  reputation conflicts, the two-track Fame/Infamy model for simultaneous Fame+Infamy climbs) rather than
  inventing new resolution machinery per pair.
  **Still needed beyond this:** further
  development of mechanics, implications, implementation, and in-world lore per the developer's own request.
  See `project_identity_fragmentation_review_flagged` memory.

- [ ] **"Fragmentation Matrix" — core system designed and written to file 2026-07-23; per-character Long
  Vigil questlines are the next task**
  Full two-axis Bond/Grief system built at `Game-Mechanics/Core-Mechanics/Fragmentation_Matrix.md`,
  structurally parallel to the Reputation Matrix but genuinely independent (not "Loyal"/"Disloyal," which
  read as one spectrum — resolved into Bond/Grief as two separately-accumulating tracks that never cancel).
  Covers companions (Grief seeded from History Points/questline/romance progress × a per-character
  Personality Grief-Multiplier, calibrated against Ayako/Seica/Kendra as worked examples) and districts
  (Grief seeded from pre-re-spec Fame/Infamy history × an institutional multiplier, cross-checked against
  all 13 districts' existing Rebuilt Marker reactions). Full 16-cell tier grid named. The extreme state,
  **The Long Vigil** (Grief R3 + Bond R3), got its own citywide secret-ending category
  (`Storyline/Endings/Secret-Endings/Long_Vigil_Endings.md`, LV-1 through LV-4, structured like Wild Child)
  and a companion-questline design-rule pattern (`Companion_System.md`). Ayako Hayashi flagged as the first
  confirmed Long-Vigil-companion-pathline candidate (her own README).
  **Next:** brainstorm per-character Long Vigil companion questlines, starting with Ayako. Still open:
  exact numeric thresholds, remaining companions'/districts' multiplier values, whether Grief can ever be
  narratively reduced. See `project_fragmentation_matrix_flagged` memory.

- [ ] **District documentation template** — create `Worldspace/Locations-and-Levels/Concordia-City/Districts/_TEMPLATE.md`
  Must include a **Demonym** field: the word for "a person from [District]" (e.g., Sagittarius → Frostlander). Used in NPC dialogue, terminal entries, audio logs, and any in-world text referring to a district's residents as a group. Each district needs its own demonym established before NPC dialogue writing begins.

---

## Medium Priority — Character Development

- [ ] **Sexuality rule update — apply when the first human companion is designed**
  Rule updated 2026-07-03: robots and human women are bisexual, human men are heterosexual (previously all humans were heterosexual). Romanceable human male companions will gate on an additional gender check on top of the standard MACHINE stat check (see `Companion_System.md`, `Universal_Rules.md`). **Correction (2026-07-03):** all currently-existing recruitable companions are robots — Favi della Torre included (her established backstory describes her boyfriend as "a human," distinguishing him from her). No existing companion romance design needs auditing or updating right now; this rule only becomes relevant once a human companion is actually designed and added to the roster.

- [ ] **Ayako Hayashi — character development queue**
  Confirmed: recruitable companion; romanceable; 4w5 Self-Pres; Red Spiral medic; Japan origin; art/fashion → medicine trajectory; Schopenhauer as personal philosophy. Home designed (Leo district atelier). Romance design complete (Investigation ≥ 7, Humanity ≥ 7 [raised from ≥6, 2026-07-20], Calculation ≥ 6; full 6-beat Gate 3 sequence). **Resolved 2026-07-20:** pre-Concordia origin city — **Shirayuki** (see `Specs/Shirayuki.md` Open Questions and her own README); MACHINE stat baseline — Might 2 / Agility 7 / Calculation 6 / Humanity 9 / Investigation 9 / Nerve 7 / Engine 7; Red Spiral seniority direction — esteemed/senior member, structurally comparable to Arcade Gannon, confirmed NOT the leader (exact title still TBD); personal questline — broad-scope guiding direction charted (working title "The Unfinished Garment," see `Questlines/Personal_Questline_Summary.md`); speech pattern broad direction charted. **Personal questline retrofitted 2026-07-20 to the Personal Questline Design Rule:** categorical block is Red Spiral's own conflict-of-interest protocol barring Ayako from investigating a current case that echoes her own loss; 5 stat approaches plus 7 non-stat world-state routes now charted. Still outstanding:
  - Full personality/voice (Phase 3) — broad direction charted, exact lines/quirks not yet written
  - Full personal questline design (deliberately deferred until Concordia/Cancer district is developed)
  - Red Spiral exact rank/title (seniority direction confirmed; exact title deliberately held off until Tepenia's in-world naming/title conventions are better established generally)
  - Companion perks / notable traits
  - Japan lore (develop alongside Upper Earth/Japan world design)

- [ ] **Personal questlines — broad-scope guiding-idea charting pass, flagged 2026-07-20**
  Surfaced while working Ayako Hayashi's development queue: **none of the 13 confirmed main-game recruitable companions have any personal-questline content written** — every `Questlines/Personal_Questline_Summary.md` file checked so far is the untouched blank template. Full step-by-step quest design is correctly held off until Concordia is developed enough for beats to land on real places (same discipline as Calethina's own questline deferral) — but the developer's direction, confirmed 2026-07-20, is that enough is now known about the characters (Enneagram types, established wounds/hooks, the extensive romance-beat writing already done in `Companion_System.md`) to chart **broad-scope guiding ideas** — themes, emotional core, rough shape — for each companion now, without full detail. **In progress: Ayako, Flora (working title "Old Reliable"), Favi (existing "The Long Watch" draft consolidated and reworked), Villena (existing "The Last Stage" draft consolidated and reworked), Naizelle (existing "The Recovery" draft consolidated and reworked), Seica (existing "The One I Couldn't Stop" draft consolidated and reworked), Ji-Eun (Option A of the existing "The Shape of a Key" draft retrofitted, marked TENTATIVE pending the open threat-identity question), Vosora (existing "What the Silence Says" draft's investigative mechanism retrofitted — her four already-designed endings and dual-outcome perk structure untouched), Michelle (existing "What the Corruption Took" draft retrofitted the same way), and Pink Lucy (existing "Is This Real or Is This the Act?" draft retrofitted with a new present-tense inciting hook, 2026-07-20 — see below) charted.** Still not done for the other 3+ companions (Fenny, Lyuba, Rui, plus DLC companions) — working through them one at a time.

**Design principle surfaced 2026-07-20 while retrofitting Vosora:** the binding "no escort quest structure" constraint established for Ji-Eun Kim (cost/vulnerability must fall on the player, never on the companion as an NPC to be kept alive) generalizes beyond her — Vosora's own recruiting hooks originally leaned on "protect her during the vulnerable step," which got restructured the same way; Michelle's had the identical pattern and got the same fix. Worth checking future companions' existing drafts for the same pattern before retrofitting them.

- [ ] **Companion roster recruitability — final precise pass, 2026-07-20**
  While surveying the Dolls folder for the personal-questline pass, the developer gave a definitive, final-word update on recruitability status, corrected against `Companion_System.md`'s "Roster source of truth" section (which previously listed only 3 exceptions):
  - **Confirmed non-recruitable, permanently:** Trisha Miller, Majyao Bisyugota — unchanged.
  - **Structurally distinct special case:** Calethina — unchanged.
  - **Genuinely undecided (NEW — 3 characters), may end up recruitable or may follow the Majyao pattern (full companion + romance questline, location-anchored, never joins the party):** **FR-03 "Maria"** (developer's instinct: may operate a leisure/billiards establishment), **SE-031 "Akina"** (the Long Night War's actual inciting-incident gynoid — developer explicitly flagged her story as extremely delicate, requiring utmost care; developer is separately taking time to develop her personality before deciding anything else about her, including this), **TCY-20 "Miranda"** (developer's instinct: may operate an actual in-game bar as its bartender — consistent with her already-established "Hub bartender" role). **Miranda's file previously had a stale hardcoded "Companion Potential: No — NPC," corrected to "Undecided."**
  - **Everyone else, confirmed recruitable** — including **XT-21 "Angelina,"** whose own file previously said "Undecided" and has now been corrected to "Yes."
  - All affected files updated: `Companion_System.md`, and the individual READMEs for Maria, Akina, Miranda, and Angelina.

  **Major roster expansion, same day, 2026-07-20 — developer set up new character folders directly.** 20 new blank placeholder folders added to `recruitable/` (Felia Percelle [FW-70], Heather Wendell, Imelda Sánchez, Inés Ochoa, Laura Wahlström, Lieselotte "Lotte" Koster, Małgorzata "Gosia" Iskierka, Marisol Ruvalcaba, Pixi Fairiefeather, Seline Finley, Shuchar Vaszyong, and TBN [SE-157 Lita], [SE-164 Kemeny], [SHD-02 Starley], [STP-06 Hao], [STP-09 Keqing Qin], [STP-10 Mira], [TCY-02 Polly], [WM-06 darling freckled redhead], [XT-30 Luna]) and 16 new blank placeholder folders added to `unsure and_or special cases/` (Ísabel Camila Bóndar, Itzel Hernandez, Leticia Flores, Meifa Podeshén, Nóra Kerekes, Rosalva Mejía, and TBN [FFD-22 Tiancheng], [FFD-51 Duqing], [FFD-53 Leeson], [FFD-54 Yelan], [SE-150 Winola], [SE-154 Annika], [XT-41 Genri], [ZL-11 Olivia], [ZL-18 Miko], [ZL-41 Irene]). **All 36 are empty scaffolding only (README.md + Personal_Background/Questlines/Reference_Images subfolders, matching `z-template`) — no backstory, personality, Enneagram, or MACHINE stats written for any of them yet.** Developer's own framing: "I don't know what sorts of character backstories, situations, etc, they have, but I'm certain that I want them in the game." New roster total: **44 recruitable + 2 non-recruitable + 1 special case (Calethina) + 19 undecided = 66 real character folders.** `Companion_System.md`'s "Roster source of truth" section updated to match. These 36 are not yet in the personal-questline pass queue — that continues with the previously-identified companions (Fenny, Lyuba, Rui, DLC companions) until the developer indicates otherwise.

**Major correction surfaced 2026-07-20 while retrofitting Vosora and Michelle: the non-malice rule applies to invented antagonists, not just district-level history.** An initial draft gave both companions a vague "hostile organization" pressuring them — the developer caught that this doesn't hold up: a Tepenian actor doing this from malice breaks the rule that's governed every other piece of worldbuilding this session, and a genuinely hostile Upper Earth cell capable of running sustained surveillance on two targets would have escalated well past "undisclosed pressure" by now. This also surfaced a direct conflict with an already-locked rule: `Cross_District_Non_Malice_Audit.md` had already locked Gemini's Great Corruption to resolve toward accident, never deliberate sabotage — but Vosora's and Michelle's pre-existing questline drafts (written before this session) were built around confirming it as deliberate. **Resolved:** the Corruption was a genuine accident (founding-crisis storage triage put certain record types on infrastructure that later failed, clustering in a way that looks like sabotage but wasn't). The pressure on both companions is **Libra itself — specifically different officials, each independently and sincerely convinced suppression is the right call**, motivated by a real mix of (a) genuine fear that proving old structural inequities would destabilize a fragile peace, and (b) self-interested fear that proving Libra's own negligence would damage public trust in their fitness to govern. Neither companion's questline auto-completes the other's, since they're pressured by different officials. Both companions' full files (README, Questlines/README, Personal_Questline_Summary, and this file) have been corrected to match — see their entries below. **General lesson: check any newly-invented antagonist (not just existing district history) against the non-malice rule and against already-locked canon before writing it into a questline.**

**Correction to the Wild Child pattern, 2026-07-20:** the first several Wild Child routes designed in this pass (Villena/Libra, Ayako/Cancer, Flora/Libra) leaned too heavily on one flavor — an institution can't file the player, so records surface as a side effect of individualized handling. Flagged by the developer as needing genuine variety, citing Fallout: New Vegas's own Wild Child/NCR mechanic in Arcade Gannon's companion quest (Wild Child status lets the player talk Moreno into fighting alongside the NCR now, with betrayal left open later — a persuasion/leverage mechanic, not a records mechanic). `Companion_System.md` now lists multiple established flavors (bureaucratic, gossip/rumor, confessional, persuasion/leverage) and instructs designing each new one from what that specific faction/district would actually do with an unresolvable contradiction, not defaulting to the bureaucratic shape. Ji-Eun's own Wild Child/Aquarius route uses the new persuasion/leverage flavor. Not retrofitted onto the four earlier ones yet — flagged as available for a later pass if wanted, not done unprompted.

**New recommended pattern added 2026-07-20 to `Companion_System.md`'s Personal Questline Design Rule:** aim for at least one non-stat route usable via **Wild Child** status (Idolized + Vilified simultaneously) with a relevant faction/district — reuses the existing mechanic from `Wild_Child_Endings.md` where institutions can't categorize a Wild Child player and are forced into individualized handling, which can surface information as a side effect. First applied to Villena via a Libra route; **retrofitted the same day into Ayako (Wild Child/Cancer, since Red Spiral is headquartered there) and Flora (a second, distinct Libra route alongside her existing faction-antagonism one)** — both now at 8 non-stat routes total. Not required for every companion, same status as the faction-antagonism pattern.

**New binding rule surfaced 2026-07-20 while reworking Favi's questline, now in `Companion_System.md`'s "Personal Questline Design Rule":** every companion personal questline (not the romance questline) must hinge on something the player is able to do that the companion herself cannot — real player agency, not the player watching her faction/skills solve it off-screen. The exclusion must be **categorical** (something she's structurally barred from — wrong architecture, no access, barred by history — not just a stat she happens to score lower on; otherwise the rule collapses into "the player met a threshold she could in principle have met too"). Once that categorical block is established, the step needs (a) a minimum of 5 distinct, non-build-gated stat-based approaches spread across different MACHINE stats, deterministic pass/fail per the existing Fallout: New Vegas-style system (no dice rolls), and (b) non-stat, world-state-based approaches (faction reputation, knowledge/items from unrelated content, relevant allies) — **target 7–12, absolute floor of 3** — every one of which has to actually make sense within the established world, never invented purely to hit the count. **Recommended (not required) pattern within (b):** where a companion has an established negative/wary relationship with a specific faction or district, one non-stat route should ideally be the player's own positive reputation there (Fallout: New Vegas tiers, Accepted or better) opening a door she couldn't open herself — applied to Favi via Eyes of Gold's mutual distrust with Libra. The non-stat routes exist specifically so a player can never be structurally unable to complete the questline (and therefore reach the romance gate) purely because their build missed all 5 stat-based routes. **Retrofit complete, 2026-07-20:** Ayako and Flora were both brought up to the full rule the same day it was established — see their entries below.

- [ ] **"History Points" — now designed as the Accomplishment Weight System, 2026-07-23; per-companion rollout still gradual**
  Full mechanism now built at `Game-Mechanics/Core-Mechanics/Accomplishment_Weight_System.md`: a weighted
  accumulation of general accomplishments (district main/under-questline completion, location discovery,
  plus bespoke per-companion character-specific events and a companion-specific bonus for personally-
  meaningful districts) gates personal-questline progression — solving a real pacing problem where narrow
  world-state triggers either get skipped by speedrunners or create huge real-hours gaps for completionists.
  Calethina is the first full worked example (Gemini/Aquarius as her meaningful districts, six confirmed
  character-specific sites). **Still open, per the developer's own original framing:** exact point values
  per tier; which other companions get a full character-specific list, decided gradually, "who it makes the
  most sense for" rather than all at once.

- [ ] **IT-068 [Flora] — full development queue**
  First recruitable companion; well-scaffolded but incomplete. Established: 6w5 Thinking type; Capricorn industrial maintenance background; Frontline Utility Tank / Field Engineer combat role; recruitment scene at Thermal Distribution Junction 12 (mid-to-late Act 1); personality voice and approval system defined. **Personal questline broad-scope direction charted 2026-07-19** (working title "Old Reliable" — institutional distrust traced to a non-malicious broken promise during a past crisis; see her `Questlines/Personal_Questline_Summary.md`). **Retrofitted 2026-07-20 to the Personal Questline Design Rule:** categorical block is her own public/vocal history with city governance barring her from a fair hearing; 5 stat approaches plus 7 non-stat world-state routes now charted, including a Libra route using the faction-antagonism pattern. Outstanding:
  - Permanent name (replace [Flora] placeholder)
  - Visual design and reference images
  - Full personal questline design (broad-scope direction now charted; full step-by-step deferred until Capricorn/crisis-response locations exist)
  - MACHINE stat tuning (full mechanical balance pass)
  - Romance questline thresholds (Phase 3)
  - Repair crew member names and characterization
  - Subvariant (Self-Pres vs. Social vs. Sexual) — TBD
  - District-specific approval modifier details beyond what's in README

- [ ] **Remaining named Doll characters — personality and backstory development**
  Six named characters have backstory scaffolding but undeveloped personalities, voices, and questlines:
  - **Kendra Heinrich** — 8w7:Sc; DLC 1 protagonist (South Pole); "goddess of war"; held off Upper Earth forces at Amundsen Tower while innocents evacuated; stranded; personality TBD
  - **Meyzan Yocazhda** — 3w2:Pr; job/setting TBD (Leo vs. Capricorn); almost entirely blank
  - **Michelle Stanton** — 5w6:Sc; built the Arcanet in a Rastra with a small team of robots and dedicated humans; now in Janbogo doing data archaeology and Great Corruption investigation; personality TBD. **Personal questline ("What the Corruption Took") reworked 2026-07-20:** the Great Corruption is a genuine accident (Libra's own founding-era negligence), not sabotage; the pressure on her comes from a sympathetic, genuinely convinced Libra official (shared antagonist structure with Vosora — different officials, non-overlapping questlines). Her own slow-verification identity is the categorical block. 5 stat approaches plus 9 non-stat world-state approaches (including Aries and Virgo routes and a Wild Child/Long Frequency route) sketched in `Questlines/README.md`. MACHINE stats/personality/traits still fully placeholder — separate task.
  - **Salagéa Aparast** — 1w2:Sc; Belgrano native; boat-dwelling datashard archivist; preserved civilizational knowledge during Long Night War; personality TBD; **placement RESOLVED — DLC 5 (Atlantic Coastal Region), not a Concordia district** (corrected 2026-07-03; this line previously said "district pending," stale from before the Decision Required item was resolved)
  - **Vosora Lashár Tanslock** — 5w6:Sc; nomadic data/logistics expert; organized Amundsen Tower construction logistics; stranded in Concordia by circumstance; transmitting data to space-dwelling Tepenians; personality TBD
  - **Calethina** — personality, backstory, and core identity entirely blank beyond questline structure

- [ ] **TBN characters — 12 remaining**
  All need: real name, district confirmation, full personality sketch, MACHINE stat baseline, role (companion vs. NPC), questline or story hook. **TBN [SE-031 Akina] remains completely untouched (still the raw blank template) and isn't counted in this list yet — pick up whenever her development starts.**
  - **TBN [HKD-172] — development started 2026-07-20, previously the untouched blank template.** Confirmed: recruitable, **Mawson DLC**; origin city Mawson; hospitality-industry background (grounded in `Specs/Mawson.md`'s own established honeymoon-tourism economy). 4 role candidates printed to file, none chosen yet (Honeymoon Field Guide; the Course-of-Events "Character A" hospitality-vs-hub-logistics advocate role, reusing existing unnamed lore from `Mawson_07_The_Hub_That_Chose_Kindness.md`/`Mawson_10_What_The_Guests_Never_See.md`; General Visitor Liaison/Administrator; or a Field-Guide-to-Advocate combination) — see her own README's "Role Possibilities" section. Present-day location/reason for leaving Mawson (if any) deliberately left open, not defaulting to war-displacement.
  - TBN [FR-03 billiards Maria] — everything TBD
  - TBN [FW-25 Pink Lucy] — 7w6:Sc; Leo entertainer; questline written but personality TBD. **Personal questline retrofitted 2026-07-20:** new present-tense inciting hook (a Warm-Circuit-served outer district's real hardship being made worse by morale programming); her own professional-positivity role is the categorical block (a new "perceptual" flavor, distinct from prior companions). 5 stat approaches plus 8 non-stat world-state approaches (including a Wild Child route using a new "authenticity recognition" flavor) sketched in `Questlines/README.md`.
  - TBN [IT-021 white shirt Fenny] — 6w5:Pr; Taurus; questline written but personality TBD
  - TBN [TCY-06 red-dress Palmer City Elva] — established Star War house; personality TBD
  - TBN [TCY-20 unimpressed bartender Miranda] — The Quiet Shift; personality TBD
  - TBN [TCY-25 smoldering darkness Rui] — 9w1:Sp; Scorpio; **confirmed recruitable/romanceable 2026-07-10**; still needs real name, backstory, MACHINE stat baseline, questline, home design
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
  - **Favi della Torre:** boyfriend's name (Italian human, Eyes of Gold member); Italian scientist's name; Taurus security network official name ("The Steady Watch" is a placeholder); nature of Favi–scientist relationship (confirmed NOT romantic; paternal/daughter vs. something more complex — must be decided before datashard event dialogue is written; see `Questlines/Companion_Event_The_Scientist_Entry.md`). **Personal questline reworked 2026-07-20:** the scientist's-fate revelation is no longer required to go through the DLC-5 datashard event (that's now optional bonus flavor only) — canonical mechanism is Eyes of Gold identifying the lead and telling Favi directly (freely, as one of their own loyal members — no separate player-side gate needed for that part) plus the player, as Bridge Unit, retrieving the record from a corrupted Arcanet fragment (categorical block: Favi cannot do this regardless of her own stats — wrong architecture), with 5 non-build-gated stat approaches (Investigation/Calculation/Nerve/Humanity/Engine) plus 8 non-stat world-state approaches (Gemini, Calethina, Aquarius, Pisces, Virgo, Libra, a retired archivist NPC, a legacy item — an earlier "Eyes of Gold reputation route" was removed, since it didn't hold up: Favi's own standing already secures anything that faction could offer) sketched in `Questlines/README.md`. Exact skill-check design still TBD.
  - **Ji-Eun Kim:** identity of the person she built the concealment for; design the "undelivered letter" gate conditions and the lore it reveals (see Ji-Eun Kim README — Design Notes). **Personal questline (Option A) retrofitted TENTATIVE 2026-07-20:** her concealment protocol is the categorical block on investigating the threat hunting her herself; 5 stat approaches plus 9 non-stat world-state approaches (including a faction-antagonism route reusing Option B's own documented Aquarius-antagonistic district list, and a persuasion-flavored Wild Child/Aquarius route) sketched in `Questlines/README.md`. **Still genuinely open and flagged as needing real design attention: who is hunting her, why, what they stand to gain, and whether it's justifiable within the game's non-malice tone** — everything else in the retrofit is written not to depend on the answer.
  - **Seica Cenilaithe:** husband's name; occupation in Scorpio; Archive of Final Confessions engagement level. **Personal questline reworked 2026-07-20:** inciting hook reuses her existing "direction for the hatred" recruiting-hook idea; her own established cinematic beat (instant lethal response to a detected lie) is the categorical block, since her reputation makes patient/undercover investigation structurally impossible for her. 5 stat approaches plus 8 non-stat world-state approaches (including a Wild Child/Scorpio route, via the Archive of Final Confessions) sketched in `Questlines/README.md`.
  - **Villena Hiresvett:** venue names (2–3 regular residencies); Star War affiliation (Elva's established house vs. Lillian's legacy house). **Personal questline reworked 2026-07-20:** inciting hook is a Palmer City bandmate/creative partner she was separated from during the Amundsen Tower evacuation, believed to have made the last transport off-world (not to another ground city); her lack of any faction/institutional affiliation categorically bars her from investigating it herself. 5 stat approaches plus 8 non-stat world-state approaches (including a route via Vosora Lashár Tanslock's off-world comms work, and a Wild Child/Libra route) sketched in `Questlines/README.md`.
  - **Majyao Bisyugota:** teahouse name; ~~verify Enneagram against lead sheet~~ — confirmed 4w5 Self-Pres
  - **Naizelle d'Edjordoś:** pre-war home city (destroyed in Long Night War; depends on pre-war geography work); recruiting hook. **Personal questline reworked 2026-07-20:** inciting hook is an old recording from her pre-war Metal/Industrial scene days, still circulating informally; her "Low-Profile Movement" trait categorically bars her from personally chasing it without endangering her compound. 5 stat approaches plus 8 non-stat world-state approaches (including a Wild Child/Pisces route) sketched in `Questlines/README.md`.
  - **Meyzan Yocazhda:** job/setting decision (Leo vs. Capricorn)
  - **Trisha Miller:** Activation Date still TBD

- [ ] **Upper Earth Defector characters — placement reconciled 2026-07-24, exemplar NPCs still needed**
  The framework itself already existed (`Worldspace/Characters/Upper-Earth_Defectors/` — 3 subdivisions,
  Remorseful/Pragmatics/Infiltrators; this TODO entry's "no substantive content" was stale). **Placement now
  reconciled against current district canon** (previously stuck on the retired "Neutral 13th District"
  naming): Sagittarius (main settlement), Virgo (atonement labor — now ties directly into
  `Tepenian_Criminal_Justice_System.md`'s Tier 2 mechanic), Cancer (refugee aid, sharpened by the Overcrowding
  Decision), Aries (extremely restricted, Black Silence-driven paranoia), Pisces (Pragmatics/Infiltrators),
  Gemini (Infiltrator misinformation, via the Twin Channels duality), plus two new additions the original
  draft never had — Scorpio (Remorseful defectors at the same trauma clinics as war victims) and Libra
  (legal/parole governance layer, not a residence). **Still needed:** actual named exemplar NPC characters
  (motivation, what they lost, what they carry) — at least 2-3, per the original ask. **Also noticed in
  passing, not yet fixed:** `Storyline/Side-Content/Defectors_Major_Questline.md` appears to be an accidental
  duplicate of `Defectors_Early_Tie_Ins.md`'s content under the wrong filename, not actual major-questline
  content — worth a look. **New recruitable companion seeded 2026-07-24:** the single highest-esteemed
  proven-wartime-loyalty defector permitted in Cancer is now a real character — see
  `Worldspace/Characters/Humans/recruitable/Unnamed_Cancer_Defector/README.md` (name and all personal details
  still TBD; modeled on the Boone/Great Khans dynamic from Fallout: New Vegas). First recruitable human
  companion filed outside `Dolls/` — established a new `Humans/recruitable/` sibling folder structure.

---

## Medium Priority — World and Story

- [ ] **A genuinely still-derelict, present-day-discoverable pre-exile site — needed, not designed, flagged 2026-07-25**
  Surfaced while reviewing the new "Reclaimer's Hands" trait (`Character-Creation/Traits.md`) and "Derelict's
  Eye" perk (`Perks/World_and_Discovery_Perks.md`): both are currently decorative, not functional, because
  every pre-exile reclamation the recent GPS-purposes-only sweep fixed (Marambio's runway, Abowasa's labs,
  Casey's weather station) is historical backstory already resolved centuries before the game's present day
  — there's nothing left for the player to actually find and restore themselves. The developer's own
  framing: it's not enough to have pre-exile infrastructure exist in lore; there needs to be enough of it
  that's properly meaningful to the world and relevant to actual main- or side-content, or the trait/perk are
  just "logical decoration." **The model to build toward: Byrd** — never part of the 2564 founding wave,
  abandoned and buried, only found and reclaimed much later by Belgrano's own explorers. Need at least one
  (ideally several) new site(s) built on that same shape: unclaimed at founding, still derelict, discoverable
  by the player in actual quest content. Not designed yet.

- [ ] **Tepenian criminal justice — first-pass design written 2026-07-24, several open questions remain**
  Surfaced while discussing player-instigated violence (`Player-Instigated_Violence_-_Understandable_Reasons.md`);
  full design now at `Districts/Tepenian_Criminal_Justice_System.md`. **Three-tier severity model confirmed by
  the developer:** Tier 1 (petty/culturally-offensive crimes) → formal exile from the offender's home district
  → self-relocation to Pisces or Sagittarius (explains the previously-unconnected "exiles from stricter
  districts" line already sitting in both districts' own Inhabitants sections). Tier 2 (serious crimes) →
  heavily-supervised, closely-surveilled dangerous labor conscription in Virgo or Aries specifically, under
  native supervisors, doing work even native workers there would consider extremely dangerous. **Tier 3
  (truly abhorrent, utterly unfathomable crimes)** → forcibly "volunteered" as an Aquarius test subject,
  fitting the district's already-established ethical grey zone around consent/experimentation. Also covers:
  the robot-personhood complication (Scorpio's rebirth tech can't be used on a convicted robot without
  consent, given legal personhood since the 2318 Jeju-do ruling — framed as a live in-world controversy, not
  a clean answer) and why no clean codified penal code exists at all (Libra's own Suspended Compact/permanent-
  emergency-powers logic). **Still open, to be addressed progressively:** exactly where the Tier 2/Tier 3 line
  falls, whether society itself feels tension about Tier 3's abandonment of consent given the same system's
  care about robot personhood elsewhere, whether Tier 1's offense list should map directly onto
  `District_Hostile_Actions.md`, the actual tone of Virgo/Aries conscript-labor tension, and whether any of
  this becomes actual playable content.

- [ ] **Neo-Races and Neo-Cultures — Phase 2 synthesis (flagged 2026-07-17, ready to start)**
  Phase 1c (Cultural Iceberg Per-Nation Entries — 12-item Surface Culture + 17-item Deep Culture findings, per Primary/Significant nation) is now complete for all 35 Tepenian cities across all 6 subnets (Halley, Palmer, Mirny, Janbogo, Mawson, Byrd), see `Neo-Races-and-Cultures/_Method/Progress_Tracker.md` for the full per-city status record. **Not yet done:** Phase 2 — actually naming and crystallizing each city's own synthesized neo-culture/neo-race from that completed research. Every city's own "Synthesis Notes" section currently holds only a working first-pass draft, explicitly flagged throughout as not yet developer-confirmed. Also still open, deliberately deferred alongside Phase 2: the reserved Notable-tier passes for Palmer City (43 nations total) and Byrd (41 nations total), where only Primary+Significant tier was catalogued during Phase 1c; and any further cross-subnet or Federation-wide synthesis once all 35 cities' Phase 2 work is complete.

- [ ] **Hitchhiking as a valid travel mechanic on specific highways — established 2026-07-05**
  Hitchhiking is a genuinely normal, valid way to get around Tepenia — not a last resort — on a specific subset of highways: Hwy 7 (Belgrano Highway), Hwy 4 (Mawson-Sinheung Highway), Hwy 110 (Coastal Cut Highway), Hwy 2 (Dumont Coast Highway), and a short segment of Hwy 1 specifically between Marambio and Rothera. Written into `City_Relationship_Database.md`'s Highway Quick Reference section. **Still open:** the in-world reasoning for why these specific routes support it (traffic density, freight-truck culture, a cultural norm specific to those subnets, something else), and whether/how this becomes an actual gameplay travel mechanic (a fast-travel alternative, a random-encounter system, a skill check, or purely flavor/lore).

- [ ] **DLC exploration idea: frozen dead along the routes to Amundsen Tower**
  Developer note (2026-07-03), not yet designed: during the Long Night War, as bombs fell across the subnets, both human and robot bodies would plausibly be found frozen in the ice along the routes various subnet populations took while trying to reach Amundsen Tower to evacuate — people who didn't make it in time. Ties directly to the throughput finding in `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`: the Tower's own passenger capacity was never the evacuation bottleneck (it had ~455x headroom over normal operating capacity) — the real bottleneck and tragedy was the desperate journey *to* the Tower itself, across a warzone, in Antarctic conditions, with no guarantee of arriving in time. Relevant to DLC 1 (Kendra Heinrich, South Pole — she held the Tower "while innocents evacuated") and potentially every other regional subnet DLC (2–7), each of which would have had its own population making that same journey. Environmental storytelling material: frozen bodies, personal effects, journals/logs found en route — consistent with the game's existing environmental-storytelling patterns (Independent Lattice, Planetary Split Brain). **Zone fit (2026-07-03):** maps directly onto the "Debris Apron" zone (~2-4km out from the tower's base) in `Kendra Heinrich/DLC_South_Pole_Level_Design.md` — the terrain evacuees would have been crossing on final approach.

- [ ] **Long Night War — historical parameters**
  Needed: combatants (which Upper Earth nations, which Tepenian forces), approximate duration, major engagements, how it ended. The Amundsen Tower destruction is the most iconic event but the broader war context is undefined. Blocks character backstory depth and level design parameters.

- [ ] **Population redistribution to Concordia, Vostok, Kunlun, Dome Fuji (planned 2026-07-03, sequenced after Mawson and Byrd subnet work)**
  Two-stage plan, explicit order:
  1. **Concordia:** redistribute population numbers from higher-populated cities (explicitly *not* Lazar, to preserve its established megacity status) to establish Concordia's own population figures, currently unset (Concordia is one of the cities pending immigration composition analysis, per `Official_Population_Census.md`'s notes).
  2. **Vostok, Kunlun, Dome Fuji:** once Concordia is done, redistribute population from *all* populated cities, weighted by each city's specific scientific/research/engineering industry percentage share (not a flat population-based share) — fitting given all three are elite high-altitude/deep-ice research outposts (real Vostok's ice-core science, Kunlun/Dome A, Dome Fuji's own ice-core program) that would plausibly draw specifically from Tepenia's research-oriented population rather than a generic cross-section.
  Do not start this until Mawson and Byrd subnet cultural sheets are done — explicit sequencing from the user.

- [ ] **Amundsen Tower destruction — specifics**
  Exact construction dates (start and completion); weapon type used to destroy it. Directly affects DLC 1 (Kendra Heinrich) environment design.
  **Scale of the "giant mountain of scrap" now worked (2026-07-03):** full level design proposal — site condition, a proposed answer to "what defeated her" (the tower's collapse itself, not an enemy), ongoing DLC hazards, and physics-derived zone layout (central mountain ~27-109m tall, debris apron 2-4km out, clear ground beyond, surviving underground shaft) — written up in `Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/Kendra Heinrich/DLC_South_Pole_Level_Design.md`. Proposed, not locked. Still open: destruction weapon type, whether it should inform the site's specific hazard types.
  **Census finding to develop** *(figures updated 2026-07-04 — see below)*: By the time the Long Night War began, approximately **11.36 million Tepenians** (~35.5% of the entire pre-war population) were already living or working in low-earth orbit. The Amundsen Tower evacuations during the war were not people fleeing into a void — they were fleeing UP to an already-established, fully functional orbital civilization. This reframes the Tower's destruction: it was not just an act of mass murder against evacuees, it was the deliberate severing of a lifeline between two halves of a single civilization. Develop the narrative, mechanical, and faction implications of this — particularly for the orbital remnant's post-war relationship with Antarctic Tepenia, and for the Vigil faction concept (FD-7).

- [ ] **Orbital population — human/robot ratio and cultural implications**
  **Census finding** *(updated 2026-07-04 — the Orbital Population figures this was based on were stale and have been recalculated, see `TODO.md`'s Census II fix entry above)*: The pre-war orbital population (~11.36M combined) is **50.6% human / 49.4% robot** — barely human-heavy, much closer to parity than the previous (stale) 52/48 figure suggested, and closer still to Antarctic Tepenia's near-exact 1:1 surface ratio. **Structural reason superseded — needs a new explanation, though the tilt to explain is now smaller.** The previous rationale ("Von Braun Wheels were designed for human habitation first") no longer holds under the revised three-stage build order established below (staging station → Cylinders → Wheels+Cylinders combo), since Cylinders — not Wheels — became the primary long-term mixed-residence structure. A new explanation for the (now slighter) human-heavy tilt is needed: candidates include social/political migration patterns (human allies choosing to flee to the pre-existing orbital colony rather than go through Antarctic exile) rather than a structural/habitat-design cause. **Open — resolve before finalizing.** Develop implications once resolved:
  - Does orbital culture have a meaningfully different social texture than surface Tepenia, shaped by a slight human majority? Does this produce different politics, different faction dynamics, different relationship norms between humans and robots?
  - Is the ratio shift noticeable to the characters, or is 50.6/49.4 close enough to parity that no one treats it as a distinction? (This question is even more pointed now than under the old 52/48 figure.)
  - Does the Vigil faction (FD-7, pending redesign) or any other off-world faction reflect this demographic tilt?
  - How does the orbital population's human-heavy lean interact with post-war contact — do orbital Tepenians and surface Tepenians experience each other as culturally alien?

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

- [ ] **Perks — remaining ~84 to reach 160** *(elevated from Long-Term; updated 2026-07-04)*
  Current: 76/160 (48%), up from 61 after a batch of 15 perks ported/adapted from Fallout: New Vegas (see `project_fallout_trait_perk_adaptation` memory and `Regular_Perks_-_Level-Up.md`). Target: 160 total. Recommended distribution: ~107 non-combat / ~53 combat. Current split: ~49 non-combat / ~27 combat — prioritize non-combat to maintain ratio. Perks are core to character build identity; more than half still missing means build variety cannot be fully tested.

- [ ] **Might/Nerve design pass** *(elevated from Long-Term)*
  Both stats are marked TENTATIVE in the game mechanics files. The other five MACHINE stats are solid. Complete before balance testing can begin.

- [ ] **Tepenian Saints — create dedicated culture document**
  Confirmed canon: pre-War of Upper Earth (pre-2083) figures significant in the exploration and development of Antarctica are venerated as "Saints" in Tepenian civic culture. Known Saints so far: St. Robert (Robert Falcon Scott — city of Scott); St. Ernest (Shackleton); St. Roald (Amundsen — Amundsen Station); St. Douglas (Mawson — city of Mawson); St. Richard (Byrd — city of Byrd). Honorific uses first name. Tepenian interpretation: explorers who died or sacrificed for Antarctica unknowingly prepared the home that exiles would later need — the debt is real and is honored. Key tradition: Hut Point remembrance on Tepenian Independence Day (June 21) in Scott and Fort McMurdo — candles, flowers, personal tokens. Create a document in `Worldspace/Tepenian_Culture/` (or equivalent) covering the full Saints framework, known Saints roster, civic observances, and how the framework varies by city.

- [ ] **"The Courier" — unseen legendary figure, flagged 2026-07-16**
  Confirmed concept, not yet developed: a character named **"The Courier"** who never actually appears on-screen anywhere — not in-game, not in the TV show (*Southern Lights*) — existing only as lore mentions and passing conversation among other characters. Two purposes at once: (1) an in-world, low-key explanation for how small items (letters, personal packages, odd trinkets) get transported around Tepenia's perimeter outside the normal freight networks, and (2) a deliberate "tip-of-the-hat" homage to *Fallout: New Vegas*, whose player character is likewise called "the Courier" — consistent with this project's established Fallout Precedence Law (New Vegas as the primary Fallout reference point; see `feedback_fallout_precedence_law` memory) and its existing direct FNV trait/perk adaptations. Strong natural tie-in: Port Lockroy's own confirmed postal-corridor destiny ("Rothera moves the materials; Port Lockroy moves the words," per `City_Vision_Notes/Port_Lockroy.md`) — The Courier could plausibly be spoken of specifically in connection with Port Lockroy's postal network, or as a figure who predates and outlasts it. Not yet placed in any specific city, timeline period, or document — open design work for whenever this gets picked up.

- [ ] **National Holidays — Category 4 (Celestial/Faction-Specific) needs its own dedicated investigation, flagged 2026-07-16**
  `Worldspace/National_Holidays.md` scaffolds four holiday categories; the fourth — celestial/faction-specific holidays, tied to particular robot religious factions rather than being nationally universal — is the least resolved and needs real dedicated design work of its own, not just a quick fill-in. Two real precedents already exist in established lore (Dome Fuji's "Deepest Cold" — Ice-Cold Buddhism's solstice-adjacent observance; Mirny's "Two Days a Year" — a secular Antarctic Circle solstice-grazing tradition), but the brainstorm file's own proposal (a day when a specific star/nebula/galaxy feature touches the South Pole or Antarctic Circle) is not yet written and raises open questions that deserve their own pass: **which faction(s) would actually recognize such a holiday** (the simulation-theory religion? the still-unnamed Sylvester James Gates-grounded religion? some Kunlun-Observatory-centered faction distinct from either?), **what the specific astronomical event actually is** (a named star, a visible nebula, a Milky Way feature — "galaxy" as currently written is likely imprecise and needs a real astronomical anchor), whether it's tied to one city (Kunlun, given its status as Tepenia's primary sacred site) or observed differently by multiple factions, and how (if at all) it interacts with the existing Deepest Cold/Two Days a Year precedents. See `Worldspace/Factions/basis collection - robot religions/Analysis_Notes.md` for the religion research this should draw on.

- [ ] **Pre-war Tepenian city culture — at least 5 cities**
  Destroyed cities appear in multiple character backstories but have no cultural identity beyond names. Each needs a brief cultural sketch — architecture, character, what was lost — to give character grief its texture. Palmer City is done. Minimum needed: Fort McMurdo, Janbogo, Belgrano, Neumayer, Mirny.

- [ ] **City composite post-cultures — full pass across all cities**
  For every city, use its nation-of-origin tier composition (`Upper_Earth_Immigration_Composition.md`) to sketch a few candidate "composite new post-cultures" that could plausibly emerge from the specific mix of nationalities/ethnic backgrounds coexisting there — not just a list of source cultures, but what a blended, generations-deep Tepenian culture unique to that city might actually look like (language, food, custom, aesthetic). See also existing "Pre-war Tepenian city culture" item above and the memory note on this project (`project_city_post_cultures`).
  **Progress (2026-07-03): THE CITY POST-CULTURES PROJECT IS COMPLETE — all 6 subnets, 32 cities, done at full 32-section depth.** Final city: **Byrd** (`Cities/Local_Cultures/Byrd_Subnet/Byrd.md`, "Built From Below, Then Left Alone") — founded underground before it ever stood on the surface, discovered via a three-settlement expedition effort (Belgrano built the original "Arrastradoras"/"Rastra" tracked vehicles) on the strength of old maps alone. Its long-standing "composition TBD" blocker was resolved by deriving real tiers directly from the exact population blend it received earlier the same day (Primary USA/Japan and Significant South Korea/Canada/Indonesia/Australia inherited from Framheim/Little America; a broad 36-nation Notable tier, 34 of which came specifically from Palmer City's own over-cap trim, not Framheim/Little America — making Byrd the second-most nationally diverse Tepenian city, a direct echo of Palmer City's own earlier 43-nation expansion). Juan Carlos's post-war status was, at this point in the session, the only deliberately-unresolved item anywhere in the whole project — resolved later the same day to Destroyed; see the correction below and `Specs/Juan_Carlos.md`. Byrd subnet is now down to a single city (Framheim and Little America removed from canon earlier the same day) — its own long-standing aviation-route problem is still flagged separately in "Decision Required," above. **Mawson subnet is fully complete — 4 of 4 cities.** Final city: the Japanese city (cf. Bharati at the time; named Shirayuki 2026-07-08) — `Cities/Local_Cultures/Mawson_Subnet/Shirayuki.md`, "A Place Decided For You, Made Into a Place You'd Choose." Leans into the mild, delicate Larsemann Hills climate (per the general Sinheung-shared climate profile) as support for a genuine research/education/science/art/music/fashion civic identity — explicitly framed as a place that can support a wide variety of incoming personalities and life paths, both human and robot, rather than one dominant civic type, per the user's direct request. Also logged as an unresolved candidate consideration for Ayako Hayashi's pre-Concordia origin city (not decided). **Halley, Janbogo, Mirny, Palmer, and Mawson subnets are ALL now fully complete at the cultural-sheet level** (Juan Carlos's post-war status alone remained genuinely TBD within Palmer at this point in the session — resolved later the same day to Destroyed; see the correction further below and `Specs/Juan_Carlos.md`). **Next: Byrd subnet** — 0 done, Byrd itself blocked on missing census data; Framheim and Little America not yet checked for data availability. **Shirayuki's founding-population gap is now resolved**, the second and last such India-exclusion case in Tepenia (after Maitri/Lazar): founding population is **Japanese**, allocated via a pre-exile diplomatic decision of the International Court of Diplomacy at Jeju-do — explicitly an **Upper Earth institution, not a Tepenian one** (corrected after an initial draft miscalled it). Reasoning: Korea already held multiple footholds (Janbogo, Sejong) and China was already ubiquitous, including immediately adjacent at Zhongshan — so the Jeju-do court balanced the allocation to Japan instead, before the exile era ever began. Working title "Bharati" (later "Shirayuki," named 2026-07-08) pending the actual Japanese name at the time. **This also surfaced a real internal-consistency bug the user caught:** Sinheung and Zhongshan sit at effectively identical real-world coordinates (a few hundred meters apart) — yet Sinheung was filed as "Destroyed" while Zhongshan was "Damaged." Differing outcomes for co-located cities made no physical sense. **Resolved: all three Larsemann Hills cluster cities (Sinheung, Zhongshan, and the Japanese city) are now consistently "damaged, yet functional."** This required reversing Sinheung's earlier "Destroyed" resolution and updating its already-written cultural sheet (header, Section 30, Section 32, Open Questions), the census's "combined losses" total (revised down from ~3,762,000 to ~2,874,000, removing Sinheung's ~888,000), and all four tracking files (README, City_Relationship_Database, Overview, Station_to_City_Map) for both Sinheung and Shirayuki — City_Relationship_Database's "Geographic Rules" summary note was also substantially stale and got a full rewrite. Also flagged Shirayuki as a new candidate origin city consideration in the Ayako Hayashi discussion, though not decided. **Now working through Mawson subnet** (Mawson, Sinheung, and Sayowa done — `Cities/Local_Cultures/Mawson_Subnet/Sayowa.md`, "The Point Where Three Roads Meet": the primary Japanese Tepenian city (Shōwa-era name, JARE heritage), one of the smallest Mawson subnet cities by population but the single most geographically significant junction point in Tepenia — Hwy 37 to Vostok/Kunlun/Concordia, Hwy 7-ext to Princess Elisabeth/Lazar in the Halley subnet, the closest inter-subnet proximity in the Federation. **Data-quality fix:** resolved a 3-vs-1 status conflict (Specs file alone said "Survived," `City_Relationship_Database.md`/`Overview.md`/`Station_to_City_Map.md` all said "Damaged") in favor of damaged-but-functional, fitting a critical junction significant enough to be targeted but too structurally important to fully destroy — echoes Troll Airfield's contested-infrastructure stakes in the Halley subnet, logged as a possible DLC 4/5 connection. Also fixed a stray "Princess Elizabeth" spelling (should be "Elisabeth") found in the same file. 1 Mawson subnet city remains: Shirayuki). Sinheung done — `Cities/Local_Cultures/Mawson_Subnet/Sinheung.md`, "Chosen Ambition, Not Inherited Memory": destroyed Russian/Australian dual-founding city in the Larsemann Hills, the closest Mawson subnet parallel to Sejong's dense multinational King George Island cluster (shared with Zhongshan and the yet-to-be-resolved Shirayuki); named after the Sinheung spacecraft rather than any inherited station name, a deliberate act of ambition-over-nostalgia self-definition; combined with Zukelli, one of the two largest single population losses of the Long Night War (~2,190,000 combined). No status conflict — all sources already agreed on Destroyed. 2 Mawson subnet cities remain: Shirayuki, Sayowa). Mawson done — `Cities/Local_Cultures/Mawson_Subnet/Mawson.md`, "The Name That Outlasted the Founders": the Mawson subnet hub, longest continuously-occupied Tepenian city site (Australian Antarctic Division since 1954), named for St. Douglas (Sir Douglas Mawson) — but demographically China-Primary, breaking the USA-Primary pattern nearly every other Tepenian subnet follows, reflecting its genuine Indian-Ocean-facing (not Atlantic/South American-facing) immigration current; Australia retains a strong founding-wave Significant-tier position, similar to Rothera's UK/Sejong's South Korea/Juan Carlos's Spain. No status conflict — all sources already agreed on damaged/partially operational. 3 Mawson subnet cities remain: Sinheung, Shirayuki, Sayowa). **Palmer subnet cultural sheets are fully complete — 8 of 8 cities.** Juan Carlos's full sheet (`Cities/Local_Cultures/Palmer_Subnet/Juan_Carlos.md`, "Room to Be Itself") was written with its post-Long-Night-War status deliberately left TBD, per the project's standard present-tense living-culture methodology — the sheet describes the city as it was while active, independent of the still-unresolved survived/damaged/destroyed question. Hook: Spain retained an unusually strong Significant-tier position (like Rothera's UK); the defining civic institution is the tertulia (hosted, argument-driven gathering — already established Concordia diaspora lore in Leo/Taurus/Pisces districts, now traced back to its actual pre-war origin here). **Only remaining Palmer subnet open item: Juan Carlos's post-war status resolution** — genuinely deferred, not blocked, see `Specs/Juan_Carlos.md` for the full case-for-each-side (resolved later the same session — see below). **Palmer subnet: 7 of 8 cities done, only Juan Carlos remains (deliberately deferred as TBD, not blocked — see below, resolved later the same session).** **Signy upgraded same day from "damaged" to fully survived, untouched by direct war damage** — too remote for Upper Earth's forces to have bothered striking it at all. But the war still reached it indirectly: cut subnet supply lines left Signy's robot population with no local siligel source (humans sustain themselves fine on the Scotia Sea's marine resources instead) — flagged as a strong candidate DLC 3 questline (the untouched city that still needs the player's help). Updated across `Specs/Signy.md`, `City_Relationship_Database.md`, `Overview.md`, `Station_to_City_Map.md`, `Local_Cultures/README.md`, and the cultural sheet itself. Esperanza, Palmer City, Rothera, Marambio, Port Lockroy, Sejong, and Signy done — `Cities/Local_Cultures/Palmer_Subnet/Signy.md`, "Knowing You Are Alone, and Building Anyway": Tepenia's most isolated city (South Orkney Islands, no road/highway, weakest Arcanet link in the Federation), the only Palmer subnet city with a South African rather than Argentine/Chilean founding wave, and the strongest Tepenian claim on St. Ernest (Shackleton) veneration given the Endurance expedition's historic route passing ~300km away. Survived via yet another distinct mechanism from its subnet neighbors: not decentralization (Rothera), not misidentification (Port Lockroy), just genuine remoteness — too far away and too marginal to be worth targeting. No status conflict here — all four tracking sources already agreed. **Renamed "Juan Carlos I" → "Juan Carlos" as the city name across 8 files** (README, Official_Population_Census, Upper_Earth_Immigration_Composition, City_Origin_Factions, City_Refugee_District_Affinities, Localization_Language_List, and this session's own Marambio.md/Sejong.md), keeping "Juan Carlos I Station" untouched as the accurate real-world station name; `City_Relationship_Database.md` and `Overview.md`/`Station_to_City_Map.md` were already consistent. **Juan Carlos's survival status deliberately filed as TBD** rather than resolved — a genuine 3-vs-2 conflict where the terrain argument could plausibly go either way (limited usable footprint on Livingston Island vs. genuine island scale and rugged protective terrain); full case for each side logged in `Specs/Juan_Carlos.md` for whenever it's revisited. **Resolved later the same session, 2026-07-05: Destroyed** — Upper Earth specifically targeted Juan Carlos for its ongoing archive/customs administrative function, the same deliberate-strike-against-a-specific-function logic already established for Zukelli; `Overview.md`, `Station_to_City_Map.md`, `Local_Cultures/README.md`, and `City_Relationship_Database.md` all confirm. Sejong done — `Cities/Local_Cultures/Palmer_Subnet/Sejong.md`, "Knowing What You Are By What Surrounds You": the Korean settlement on King George Island, the most internationally concentrated location in Tepenia's founding period (~12 national communities on one ~80km island); co-Primary China/USA with an unusually strong South Korea Significant-tier retention; the other half of Tepenia's split Korean exile story alongside Janbogo. **Data-quality fix:** `Local_Cultures/README.md` said "Surviving," contradicting Specs/City_Relationship_Database/Overview/Station_to_City_Map (all four already said Destroyed) — corrected. 2 Palmer subnet cities remain: Juan Carlos I, Signy). Port Lockroy done — `Cities/Local_Cultures/Palmer_Subnet/Port_Lockroy.md`, "A City That Remembers Being Something Else": unique military→memorial→community founding progression (1944 Operation Tabarin wartime intelligence post → pre-exile heritage museum → living exile city), survived not through resilience but through strategic irrelevance plus plausible misidentification with adjacent Palmer City's strike zone. 3 Palmer subnet cities remain: Sejong, Juan Carlos I, Signy). Marambio done — `Cities/Local_Cultures/Palmer_Subnet/Marambio.md`, "Standing on Warmer Ground": Argentine Air Force aviation hub, dual airfield-and-shipyard identity. *(This entry originally also cited Seymour Island's Eocene-era fossil record as part of the city's identity — struck 2026-07-21 per the developer's own correction that the island's real-world fossil beds are a geological fact, not a driver of Marambio's culture; the same correction was actually made once already, 2026-07-16, in `Neo-Races-and-Cultures/_Method/Palmer_Subnet_Phase1c_Summary.md`, but didn't carry through to the later Megasheet pipeline until now.)* **Status resolution went the opposite direction from Rothera's:** initially found a 4-vs-1 conflict favoring "damaged," but checking Marambio's actual terrain (small, flat island, single concentrated airfield asset, no room to decentralize or build underground like Rothera's large mountainous Adelaide Island) argued for full destruction instead — the Specs file's lone "Destroyed" was correct, and the other four sources (`City_Relationship_Database.md`, `Overview.md`, `Station_to_City_Map.md`, `Local_Cultures/README.md`) were the stale ones, corrected to match. **Bonus catch:** `Overview.md` and `Station_to_City_Map.md` also both had stale "Damaged" entries for Esperanza (already long-established as destroyed) — fixed those too. 4 Palmer subnet cities remain for full write-ups: Sejong, Juan Carlos I, Port Lockroy, Signy. **Port Lockroy's status conflict is now resolved** (Damaged; partially operational, via strategic irrelevance — a heritage/museum city with no military/industrial value, plausibly conflated with adjacent Palmer City's strike zone given direct highway proximity — the same "not worth targeting" logic that saved Abowasa; its own Specs file was already correct, the other four tracking files were stale and have been fixed), ready for its full cultural sheet whenever its turn comes. Rothera done — `Cities/Local_Cultures/Palmer_Subnet/Rothera.md`, "Built to Last, By Never Being in One Place": established as the Palmer subnet's industrial center (raw materials into finished infrastructure components used across the whole subnet, including Palmer City) specifically because the user wanted a realistic manufacturing site among the remaining Palmer cities. **Status resolved as damaged-but-functional despite Rothera having a *smaller* population than both destroyed neighbors** (Palmer City, Sejong) — survival explained not by size but by two compounding physical factors established this session: (1) a genuinely decentralized industrial footprint spread across Adelaide Island's much-larger-than-usual landmass (~120km, mountainous), impossible to erase in one strike; (2) large-scale underground "vault" sections enabled by that same abundance of space, significantly bigger than genre-typical small vaults, giving surface damage a second layer to not necessarily reach. **Data-quality fix:** resolved a pre-existing 3-vs-2 status conflict (Specs/README said Destroyed; City_Relationship_Database/Overview/Station_to_City_Map said Damaged) in favor of damaged-but-functional. Palmer City done — `Cities/Local_Cultures/Palmer_Subnet/Palmer_City.md`, "The Place Everyone Passed Through": Tepenia's first-settled city and cultural capital, founded on a robot-partnership/ideology basis rather than any national identity, now also the only Tepenian city with all 43 master-list nations present following this session's deliberate population expansion. **Data-quality fix:** `Local_Cultures/README.md` still said "Surviving" for Palmer City, contradicting its Specs file, `City_Relationship_Database.md`, `Overview.md`, and `Station_to_City_Map.md` (all four already said Destroyed, consistent with its established "first settled, first destroyed" identity) — corrected. 5 Palmer subnet cities remain: Marambio, Sejong, Juan Carlos I, Port Lockroy, Signy — also worth double-checking Port Lockroy's own status, since a quick check found `Specs/Port_Lockroy.md` saying "Damaged" while `Local_Cultures/README.md` says "Destroyed," not yet reconciled). **Halley subnet is fully complete (8 of 8 cities).** Final city: **Lazar** (`Cities/Local_Cultures/Halley_Subnet/Lazar.md`, "Grown Together") — formerly the "Maitri_TBD" placeholder; resolved this session with a genuinely novel founding structure: two separate settlements (Russian-run Novolazarevskaya, continuously operated since 1961 in the real world, and the non-Indian-repopulated Maitri site) that coalesced into one city, originally named Novolazarevskaya and later phonetically shortened to "Lazar" as USA/Germany/France/Brazil immigration overtook the Russian founding population. Status finalized as damaged-but-functional: near-coastal position + genuine "megacity" scale meant it was badly bombed but too large to be destroyed outright. **This rename touched ~12 files repo-wide** — full detail in the `project_city_post_cultures` memory note. **Also caught in this pass:** stale status entries in `Overview.md` and `Station_to_City_Map.md` still had Abowasa/Sanay marked "Destroyed" and Princess Elisabeth marked "Damaged" (both superseded earlier the same session) — corrected throughout. Halley subnet done: Belgrano, Halley, Neumayer, Troll, Abowasa, Sanay, Princess Elisabeth (destroyed — ruins with straggling survivors, candidate questline: restoring its ruined zero-emissions power systems), Lazar. **Next: pick the next subnet** — remaining are Palmer (Esperanza done, 7 remain), Mawson (0 done), Byrd (0 done, Byrd itself blocked on missing census data). Prior progress — — Zhongshan, Janbogo, Belgrano (ruins/DLC5, ties to Salagéa Aparast), Esperanza (destroyed, present-tense per confirmed methodology), Denison (no prior Specs file existed, built from real Cape Denison/Mawson expedition history), Casey, Mirny (the subnet hub), Davis (`Cities/Local_Cultures/Mirny_Subnet/Davis.md`), and Fort McMurdo (`Cities/Local_Cultures/Janbogo_Subnet/Fort_McMurdo.md` — industrial capital hook, co-Primary China/USA founding tension, meritocracy-vs-founding-class fault line), Dumont d'Urville (`Cities/Local_Cultures/Janbogo_Subnet/Dumont_dUrville.md` — "Negotiated Ground": the only Tepenian city sharing its space with a massive penguin colony, extreme wind treated as ongoing negotiation rather than pride/mythology like Denison or stoic endurance like Mirny; French founding nation stayed civic default despite falling to Significant tier, unlike Fort McMurdo's exact-parity resolution), Cape Adare (`Cities/Local_Cultures/Janbogo_Subnet/Cape_Adare.md` — "Precedence": a genuinely new founding-tension shape, no single founding nation at all, civic identity built entirely around the 1899 Borchgrevink hut/St. Carsten rather than any national heritage; hosts one of the largest Adélie penguin rookeries in the world, 250,000+ pairs), Zukelli (`Cities/Local_Cultures/Janbogo_Subnet/Zukelli.md` — "The City You Can See From the Window": near-mirror of Janbogo's own composition and founding-tension shape (Italy instead of Korea as founding-operator nation), but destroyed near its demographic peak rather than settling into a stable living culture; the only destroyed Tepenian city visible in daily sightline of a surviving one, ~8km across the same Terra Nova Bay polynya from Janbogo), and Scott (`Cities/Local_Cultures/Janbogo_Subnet/Scott.md` — "Whose Name It Bears": the most extreme founding-tension gap yet, New Zealand reduced all the way to Notable tier by Census II yet the culture (St. Robert veneration, precision-over-scale ethos) shows no sign of noticing; small/intimate/stable counterpart to Fort McMurdo's large/industrial/transient, three km apart on the same peninsula and sharing the Hut Point remembrance tradition). **Janbogo subnet is now fully complete** (Concordia deliberately excluded, still blocked on missing composition data — 7 of 8 doable cities done). **Mirny subnet is now fully complete** (Vostok/Kunlun deliberately deferred to future design per the user, not just blocked on data). **Now working through Janbogo subnet** — Janbogo and Denison were already done; Fort McMurdo, Dumont d'Urville, Cape Adare, Zukelli, and Scott make 7 of 8 (Concordia still blocked on missing composition data) — subnet complete. Next subnet not yet chosen. **Data-quality fix (2026-07-03):** Fort McMurdo's own Specs file claimed it was Tepenia's largest city by population, contradicting the census (which caps it ~24th of ~30, explicitly marked "island cap" due to Ross Island's size) — corrected throughout `Specs/Fort_McMurdo.md` to "largest by industrial/physical footprint, not population." **Data-quality fix (2026-07-03):** Davis's own Specs file said "Mawson subnet," conflicting with the census and tracking table (both say Mirny) — corrected throughout `Specs/Davis.md`. **Data-quality fix (2026-07-03):** Dumont d'Urville's own Specs file said "Destroyed" and framed Pink Lucy as its "most prominent survivor," conflicting with the census destroyed-cities list, `City_Relationship_Database.md`, and the Local_Cultures tracking table (all three say damaged/surviving) — corrected throughout `Specs/Dumont_dUrville.md`; Pink Lucy's own files already framed her departure as a pre-war relocation, not an escape from a destroyed city, so no fix was needed there. **Approach confirmed with the user: work through remaining cities by subnet.** Byrd/Concordia also still blocked on missing composition data. Remaining subnets/cities listed in the `project_city_post_cultures` memory note — next up per this approach would be picking the next subnet. **Established 2026-07-03, relevant to future subnet work:** Tepenia's coastal shipping supply lines now have real-world-grounded national partners for every named region, all worth building into the relevant cities' Economy & Industry sections when their cultural spec sheets get written: **Halley subnet** (Halley, Neumayer, Belgrano) ← South Africa (raw materials from Africa); **Ross region** (Byrd subnet + Ross Sea side of Janbogo subnet: Framheim, Little America, Fort McMurdo, Scott, Cape Adare, Zukelli, Janbogo) ← New Zealand; **Dumont d'Urville Sea + Mirny/Mawson subnet coast** (Dumont d'Urville, Denison, Casey, Mawson, Sayowa, Zhongshan, Davis, Mirny, Sinheung, Shirayuki) ← Australia (staged via Hobart/Fremantle). Full detail in `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md` and `City_Relationship_Database.md`'s per-city Notes fields. `Local_Cultures/Mawson_Subnet/` folder also created (empty, awaiting cities).

- [ ] **Open design question: why does Upper Earth trade with Tepenia at all?**
  Flagged 2026-07-03, explicitly deferred — not to be solved now. Tepenia's entire coastal shipping network (South Africa/Halley subnet, New Zealand/Ross region, Australia/Dumont d'Urville Sea + Mirny/Mawson subnet coast) assumes Upper Earth retailers and materials-dealers are willing to sell to and transact with Tepenians (both human and robot) at commercial scale. This is in tension with the anti-robot sentiment that drove the Falkland Treaty exile in the first place — Upper Earth is "supposed to" hate them. Needs a characteristically believable in-world justification (or set of justifications, possibly varying by nation/era) for why this trade relationship exists and persists. See `project_upper_earth_trade_justification` memory note.

  **Confirmed methodology (2026-07-03):** every city gets a present-tense, living-culture write-up regardless of its current in-game-era status — a destroyed city like Esperanza is still described as active and populated here; destruction belongs in its `Specs/` file, not this one. Also corrected a stale status-tracking bug: `Local_Cultures/README.md` had Esperanza and Rothera marked "Surviving" when both cities' own Specs files say "Destroyed" — fixed.

- [ ] **Amundsen Tower — determine actual dimensions**
  **Mechanism established (2026-07-02):** Amundsen Tower is a **space fountain**, not a classic tension-cable elevator — a South Pole location makes the classic design physically impossible (no equatorial rotation to provide tension). Full design writeup: `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`. Ties directly into Hana Jinn's mass-driver research and the already-established "Amundsen Resonance Effect" (`Energy_Grid_Failure_Rationale.md` #11 — the Tower "drew massive planetary-scale energy," consistent with a pellet-stream accelerator's continuous power needs) and explains why the Kendra Heinrich DLC's underground tunnels plausibly run through the base rather than around it.

  **Numbers worked (2026-07-02):** height 150 km; guide tube ~225,000 tonnes; pellet stream ~270 tonnes/s at 4 km/s (top velocity ~3.62 km/s); power draw ~324 GW net (~2.16 TW gross); base accelerator track ~1.63 km; foundation load ~3.2 million tonnes-force over a ~63m-diameter core footprint at 10 MPa bedrock bearing capacity; foundation depth resolved by real-world South Pole ice thickness (~2,700m to bedrock). Construction-rate and collapse-locality sanity checks both pass. Full derivation and stated assumptions in `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`.

  **Full logistics worked (2026-07-02):** 300 bearing stations at 500m spacing (~30,000t total); 5 waystations (Base, ~15km, ~50km, ~100km/Kármán line, 150km terminus); base facility layout (accelerator + power generation + pellet return loop unified in the ~2.7km foundation shaft, ~1-2km² surface complex). **Throughput finding (revised 2026-07-04 for the Long Night War's precise 2812 date and the recalculated orbital population):** moving the full 11.36M orbital population via the Tower over the ~178-year window between completion and the Long Night War only requires ~7.28 people/hour average — the tower's existing 150km design comfortably supports this without needing to be sized any larger. All detail in `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`.

  **Still open:** exact construction start date and destruction weapon/method, detailed cargo/freight throughput, waystation naming, wartime evacuation surge peak throughput.

- [ ] **Orbital infrastructure — logistics, mathematics, and dimensions**
  **Build-order canon established (2026-07-02), sharpened 2026-07-04 with the design rationale for each stage:** Orbital infrastructure was built in three stages:
  1. **Robot-only staging station(s)** — small, light, low-tech. Occupied exclusively by robots, since a robot-only setting needs no oxygen or breathable atmosphere at all, no food production, and no sanitation — only energy harvesting (solar-collected, for recharging) and shielding from cosmic and solar radiation. This was the first structure(s) in orbit, and per the timeline constraint below, construction must have started **before the Falkland Treaty (June 21, 2564)**.
  2. **O'Neill Cylinders** — the first orbital infrastructure actually occupied by humans, alongside robots. Slow-moving, but huge and floor-space-efficient, making them the natural "inter-step" for humans to join the existing robot presence in space — the efficiency/floor-space advantage is exactly why Cylinders became the primary long-term residence structure, not the mobile Wheels that came after. Mass/population math for this stage lives in `Theoretical-Calculations/Orbital_Infrastructure_Mass_Budget.md` (a debris-built cylinder at ~100m radius tops out around 200–800 comfortable / 1,000–2,000+ optimistic-dense humans; efficiency holds at larger radii too — see `Design_Efficiency_Comparison.md`).
  3. **Combination of Wheels + Cylinders** — Von Braun Wheels are light and easy to move, trading away floor-space for mobility, purpose-built to transport robots and humans together over much farther distances specifically **to build subsequent space-based infrastructure** — a construction/expansion logistics role, not a competing permanent-residence option. Cylinders remained the structure for true long-term residence with full or near-full accommodations. Wheel-specific mass/population math lives in `Theoretical-Calculations/Von_Braun_Wheel_Mass_Budget.md` (~5.4x less material-efficient per resident than a Cylinder at any radius — consistent with Wheels being reserved for a specialized mobile/expansion-crew role rather than the primary residence type).

  **Note on the human/robot ratio question (flagged 2026-07-04):** this clarified build order doesn't actually resolve why the orbital population ended up slightly human-heavy (50.6%/49.4%, see "Orbital population" item above) — if anything, robots' head start in the robot-only Stage 1 would predict a robot-heavy population absent some other factor, since both humans and robots share Cylinders as the primary long-term residence once Stage 2 begins. The human-heavy tilt still needs its own separate explanation (social/political migration patterns remain the leading candidate) — this is a distinct question from the infrastructure build order, not something the build order itself answers.

  **Timeline anchors established (2026-07-02), via Hana Jinn and Mallory Dufay:** Since Amundsen Tower wasn't completed until ~65–75 years after the Falkland Treaty (~2630–2640), and Tepenians could only reach orbit via the Tower, the first orbital structures (stage 1) must have been built by robots who already had space access **before** the Falkland Treaty — enabled by 246 years of robot legal personhood on Upper Earth, starting April 27, 2318 (Jeju-do ruling). Two character-grounded anchors now pin this down:
  - **Hana Jinn** (`Worldspace/Characters/Dolls/Past_History_-_Known_to_Tepenians/Hana Jinn/`) — theoretical research only. Requested by name to A.R.U.Ta.G. shortly after the Jeju-do ruling (early-to-mid 2300s) to research metamaterials for mass drivers capable of launching reusable rockets into LEO. No construction — groundwork only.
  - **Mallory Dufay** (`Worldspace/Characters/Dolls/Past_History_-_Known_to_Tepenians/Mallory Dufay/`) — structural/safety inspector from The CSA (Texas; see `Reference-Images/Maps/North America with tentative labels.jpg`), who oversaw the **actual first launches and construction** of orbital infrastructure. Placed closer to the **mid-2300s** — meaning the research-to-construction gap after Hana's work was apparently modest (years to a couple decades, not centuries).
  - This places the true start of tangible orbital infrastructure (stage 1, robot-only staging station) at **roughly the mid-2300s** — over 200 years before the Falkland Treaty (2564), giving ~200+ years of pre-Treaty growth on top of the ~248 post-Treaty years now established (the Long Night War's precise 2812 date, up from the ~130–140 years assumed when this note was first written), before reaching ~11.36M by the Long Night War. Still TBD: exact decade for Mallory (an estimate closer to a specific decade within "mid-2300s" would sharpen this further), the funding/institutional mechanism behind Hana's and Mallory's work, and how stage 1 → 2 (Cylinders) → 3 (Wheels+Cylinders) timing maps across those ~200+ years.

  Needed: population capacity math consistent with the ~11.36M pre-war orbital population (50.6% human / 49.4% robot — see "Orbital population" item above, now flagged for a new explanation), habitat ring/cylinder dimensions and rotation rates for gravity simulation (baseline math done — see Theoretical-Calculations files above), number and growth timeline of each structure type, and how Amundsen Tower's throughput capacity ties into both the original build-out and the wartime evacuation surge.

- [ ] **Orbital population — national/ethnic composition map** *(high-token task; reserve a fresh session)*
  Derive the national/ethnic composition of the LEO orbital population (~10.10M combined, corrected 2026-07-05 — see the Census II Antarctic Surface total fix above; previously stated as ~11.36M) from the per-city census data. Method: for each city, weight its orbital migrant count by that city's national tier breakdown; sum across all cities with established compositions (now including Concordia's own fully-resolved composition). Produces a "nationality/ethnic composition map" for the full range of LEO orbital infrastructure (primarily Cylinders, plus Wheels and the original staging stations) as of the Long Night War period. Useful for orbital DLC content, off-world character backgrounds, and understanding the cultural texture of the population that survived up there.

- [ ] **Orbital infrastructure content — new shared folder, feeds three separate projects** *(flagged 2026-07-05, not yet started)*
  The developer is establishing `Worldspace/Locations-and-Levels/Outside-World/Orbital-Infrastructure/` to hold lore about what orbital infrastructure actually exists and what's happening up there — station types beyond the already-established Cylinders/Wheels/staging-stations, capacities, character-level detail. This single folder is meant to be the shared source of truth for three separate projects: (1) a planned **novel series** spanning post-Mars-colonization through the Jupiter frontier toward eventual Saturn exploration, whose founding population is explicitly the 12 million Tepenians who left during the later Second Interwar Period plus Long Night War escapees; (2) a planned **TV series** spanning the entire Second Interwar Period (arrival on Antarctic shores through the Concordia refugee migration); (3) eventual in-game lore sources for Inner Tepenia itself (audio logs, text entries, NPC dialogue about people currently in orbit or friends who escaped there). The developer plans two new separate GitHub repos (novel, TV) that will both pull from this same folder rather than duplicating content. See `project_tepenia_multimedia_expansion` memory. Directly connects to the "Orbital population — national/ethnic composition map" task above. A scaffolding `README.md` was written into the folder 2026-07-05 (purpose, cross-references to existing lore, open questions) — no content development yet.
  **Two design notes flagged 2026-07-05, for future exploration (not yet decided):**
  1. **Amundsen Tower's additional purposes beyond passenger transport — all 5 candidates approved 2026-07-05, written into `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`'s new "Additional Proposed Functions" section.** The developer noted the Tower's total capacity is so far beyond what's needed to move even 12 million people over 4-6 months that pure passenger shuttling alone makes it look oversized. All five candidates were liked and are approved for future extrapolation/design (none designed in detail yet): bulk raw-material export to orbit (feeding orbital manufacturing — connects directly to note 2 below), return cargo from orbit to the surface, a physical Arcanet relay anchor point, permanent scientific/atmospheric research outposts at the existing waystations (rather than just transit stops), and added strategic-value justification for why Upper Earth targeted it deliberately.
  2. **"Spaceborne" vs. "Earthborne" robots.** Given robot-manufacturing apparatus is virtually guaranteed to exist somewhere in orbital infrastructure, and given raw materials could eventually be harvested directly in space (asteroid/lunar material) rather than shuttled up from Earth/Antarctica, there's an inevitable future point where a subset of the robot population is fabricated entirely from space-sourced material — genuinely "spaceborne," never touched Earth, as distinct from "earthborne" robots built from surface-sourced components. Flagged as a rich, not-yet-developed identity/culture question, especially relevant to the novel series' "first fully spaceborne generation" framing and to the project's broader robot-consciousness themes (see `user_creative_principles` memory). Nothing decided yet — just noted for future design work.

- [ ] **Second Interwar Period timeline scaffolded — 2026-07-05, structure done, most content still TBD**
  New file: `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Timeline.md`, mirroring `Upper-Earth/Timeline.md`'s (the First Interwar Period's) exact composite Save the Cat/Bell/Truby/Campbell beat-sheet layout — same four sources, same methodology, all beat definitions reused verbatim rather than re-derived (see [[project_interwar_timeline]] for the full definitions). Covers the 248-year span from the Falkland Treaty (June 21, 2564) to the Long Night War (2812, exact day still TBD — this file provisionally uses June 21, 2812 for clean percentage math). Two concrete event placements made this session:
  - **Midpoint (50%, tentatively June 21, 2688) = Amundsen Tower's completion**, as a Snyder "False Victory." **Open tension, not yet resolved:** this contradicts the Tower's already-established completion date elsewhere in the GDD (~2629-2639 — cited in `Concordia_Second_Interwar_Cultural_Sheet.md`, this file's own Infrastructure Sequence entry above, and critically the entire "~178-year operating window" throughput math in `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`). Per the developer: this is deliberately tentative ("somewhere around" the Midpoint, not literally 50%), with a conclusive date to be settled once more background is developed — do not treat either date as settled canon until reconciled.
  - **Break into Three (~80%, ~2762) = the Long Night War's inciting incident** (the Upper Earth diplomat's death in Palmer City — see [[project_long_night_war_inciting_incident]]), per the developer's explicit direction. This creates a ~50-year Finale span between the inciting incident and the war's actual 2812 outbreak — flagged as worth confirming is intentional (a slow escalation) rather than assumed correct as-is.
  Two already-canon district events (Merit Board Audit ~2761, The Flood ~2771) land naturally within this structure at ~79.2% (tail of Dark Night of the Soul) and ~83.3% (early Finale) respectively, without needing to move either date.
  **The developer flagged, same session, wanting to revisit the Merit Board Audit's content — explicitly deferred until all cities are developed first.** Potentially significant changes, not yet specified. Don't build further content on its current framing until that discussion happens. **Echoed again 2026-07-10** during a minigame brainstorm ("I'm not even sure if I'll keep that") — a Merit Tribunal minigame concept built on it was dropped as a result. The Audit still appears as a planted, unresolved thread in `Main_Quest_Revised_Beat_Structure_TENTATIVE.md` (Beat 1 and the conflict-accumulation example), left as-is per the developer's own call — don't build further content assuming it survives until this is actually revisited.
  **Follow-up, same session — reinforced the Tower-capacity finding with real numbers.** The developer pointed out that Midpoint-to-Break-into-Three is ~74 years and Break-into-Three-to-END is ~50 years, for a combined ~120-year Tower operational lifetime (completion to destruction). Verified: at the Tower's own already-established design capacity (~194 people/hour), that's ~204 million people over 120 years — enough to move Tepenia's entire population (~32M) ~6.4x over, using the realistic design figure, not even the theoretical max (~90,000/hour, ~2,958x over). Written into `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`'s "Additional Proposed Functions" section — this raises developing the Tower's non-passenger functions (see the 5 candidates already logged above) from a nice-to-have to a real priority, since passenger transport alone would leave the overwhelming majority of the Tower's actual operating lifetime doing essentially nothing.

- [ ] **Five further Amundsen Tower layers, flagged 2026-07-05 for detailed future development — nothing written into lore files yet, brainstormed directions only:**
  1. **Who controlled the Tower.** If it regulated the whole continent's grid and gated bulk material export/import, whoever operated it controlled Tepenia's energy security and orbital economy outright — a single national authority, a contested point between factions, or a source of civic pride *and* civic anxiety (too much power concentrated in one place)? Not yet decided.
  2. **Did Upper Earth know what they were destroying?** Was the wartime strike aimed at the space elevator (stopping evacuation), with the grid catastrophe as unintended collateral — or did Upper Earth's intelligence understand the Tower was the grid's regulating flywheel, making the strike a deliberately calculated civilization-scale cascade-failure attack, not just "we destroyed their space elevator"? Bears directly on how coldly calculating vs. incidentally catastrophic Upper Earth's war conduct reads.
  3. **Why has nothing replaced the Tower's regulation function in 10-15 years?** Genuine lost technology/resources, or is the "psychological/cultural inertia" already in `Energy_Grid_Failure_Rationale.md` #14 (some residents treat grid instability as a badge of survivor identity, resisting "unnatural" full stability) actually the real blocker?
  4. **Partial salvage, uneven relief.** Could surviving Tower debris (bearing stations, superconducting magnets — ~93% of the wreckage reached the ground intact) have been salvaged into smaller local/regional stabilizers, explaining why grid instability isn't uniform across every city/district?
  5. **What Tepenia lost materially, not just electrically.** If the Tower was the primary bulk import/export channel with orbit, its loss may be the concrete, in-universe reason specific goods/materials/manufacturing capabilities that used to come from orbital production simply don't exist in Tepenia anymore — a worldbuilding constraint for "why can't they just build X."
  See `project_amundsen_tower_reframe` memory for full context these build on.

- [ ] **Second Interwar Period's Break into Two (~2614) — combined direction confirmed, three candidate shapes kept open, none chosen yet — 2026-07-05**
  Asked for possibilities for the era's "Doorway of No Return #1" (Break into Two). The developer liked combining two ingredients: a crisis proving isolated cities can't survive alone (forcing federation as necessity) and a generational handoff (founders giving way to Tepenians born in exile with no memory of Upper Earth) — well-grounded in existing lore, since human lifespans aren't meaningfully extended here, meaning most human founders would be elderly/dead by 2614 (50 years post-Treaty) while robots from the founding era are still fully active, spanning both generations. Three candidate shapes written into `Tepenian-Federation/Timeline.md`'s Break into Two section, explicitly kept open (not mutually exclusive, not yet chosen between):
  - **Shape A** — the crisis discredits founders' isolationist caution outright; exile-born humans organize cross-city aid without permission and it works, creating political will for real federation.
  - **Shape B** — a leadership handoff (founders' council going robot-only as humans age out) collides with the crisis mid-transition; the new generation is thrown into improvising federation under pressure, not choosing it calmly.
  - **Shape C** — robots (not humans) are the ones who push for federation, using their long institutional memory to recognize isolationism has outlived its usefulness, with exile-born humans as the ones willing to act on it.
  Explicitly may add more shapes later; decision on which to use (or how to combine further) deferred until more background/context is developed.

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

- [ ] **The Triage Protocol (renamed from "Ghost Protocol" 2026-07-23) — design as gameplay mechanic**
  Named and documented in `Worldspace/Energy_Grid_Failure_Rationale.md` (reason #9). Emergency AI protocols embedded into the Power Core during the Long Night War to prevent total collapse; now deeply entangled with core systems. Removing or overriding them risks triggering a built-in scorched-earth shutdown that could permanently disable large grid sections. Renamed to resolve a naming collision with an unrelated Minmax Build/Ending #18 and Ji-Eun Kim's own still-placeholder-named companion perk.
  **Calethina connection — confirmed, not speculative:** Calethina personally embedded these protocols during the evacuation; the same power shock that caused the Planetary Split Brain and corrupted her own datadrives also erased her memory of having done it. Discovered over the course of her Romance questline specifically. See her own `README.md` and Calethina questline entry for the full design note.
  **TBD:** how this functions as an in-game obstacle or quest mechanic; connection to the main story climax; whether the player can interface with it directly.
  **TBD:** How this functions as an in-game obstacle or quest mechanic; connection to the main story climax; whether the player can interface with it directly.

- [ ] **Amundsen Resonance Effect — design as gameplay mechanic**
  Named and documented in `Worldspace/Energy_Grid_Failure_Rationale.md` (reason #11). Harmonic instabilities from the destroyed Amundsen Tower cause resonance feedback during large-scale grid repairs, producing synchronized blackouts across multiple districts simultaneously — worse than the problem being fixed.
  **TBD:** How this manifests in gameplay; whether it connects to the Planetary Split Brain questline or the Amundsen Tower level environment; potential role in the climax.

---

## Long-Term / Low Urgency

- [ ] **City personality-deepening pass, using Subnet Ultra-Megasheets as the guide — flagged 2026-07-20, wait until the full book-TOC cataloging pass is finished**
  Not "list what real-world research we already have" — the opposite motion. Once
  `STEM_Biology_Cataloging_Checklist.md` and `Book_TOC_Master_Reference.md` are fully complete (every
  folder in the big 2026-07 book stash cataloged), go through every subnet and every city within it and
  deliberately think about what *additional* topics/subject matters would be characteristically fitting to
  add to that specific city — genuinely new material that expands the city's "personality," not a
  re-statement of existing content. The 5 Subnet Ultra-Megasheets (`project_subnet_ultra_megasheets_complete`
  memory) are the intended guide for this: read a city's established identity/tone there, then identify
  what real-world topic areas would deepen it in an in-character, internally-consistent way, and go find or
  flag books on those specific topics. This is a generative/creative pass, not a cataloging one — do not
  start it early or fold it into the current TOC-cataloging work.

- [ ] **Cross-nation/cross-subnet city relationship check — flagged 2026-07-17, STARTED 2026-07-20**
  Deliverable: `Worldspace/.../Cities/City_Cross_Subnet_Relationships.md`. First-pass map complete —
  traced the highway network (`Highways.md`) and airport network (`Airports.md`) for every subnet-boundary
  crossing, cataloged already-established cross-subnet connections as a set for the first time (Belgrano↔
  Byrd, Kunlun↔Dome Fuji, Sinheung↔Byrd, the Troll/Sinheung/Dome Fuji aviation triangle, Davis↔Mawson),
  surfaced a real unwritten historical connection (Davis's own namesake personally rescued Mawson's), and
  cross-referenced founding-nation composition to find 3 genuine anomalies (Byrd's population reads
  Janbogo-Pacific despite its only physical link running through Palmer; Vostok+Byrd share a unique
  USA+Japan Primary pairing found nowhere else; Fort McMurdo's Euro-leaning Significant tier breaks its
  own subnet's pattern, plausibly explained by its status as the historical capital). **20 of 35 cities
  now have an identified cross-subnet connection; 15 remain (Palmer subnet worst-covered by far — see the
  file's own Part 5).** Turning any of these threads into actual dramatized content is the explicit
  next step, not yet done.

- [ ] **Throwing weapons — full system, flagged 2026-07-04; universal retrieval principle written 2026-07-23**
  New combat category. **Core focus, clarified by the developer:** thrown blade weapons specifically — throwing knives, tomahawks, and similar bladed forms — not a generic "any weapon can be thrown" system. Envisioned as an "aggregated hybrid" of Baldur's Gate 3 (Strength-based throwing, a real build path) and Cyberpunk 2077 (dedicated throwing knives as their own distinct equipment/build category), but scoped to blades rather than BG3's broader "throw anything" approach. **Explicitly excluded:** BG3's alchemist's fire and similar consumable thrown items — a Fantasy-genre mechanic that doesn't fit Inner Tepenia's Sci-Fi setting. The developer is open to a separate grenade system as the Sci-Fi equivalent of that consumable-throwable niche, but that's a distinct, secondary idea, not the main thrust of this entry. This would also resolve an open gap surfaced during the 2026-07-04 Fallout trait/perk comparison pass — FNV's "Loose Cannon" trait and "Heave, Ho!"-style perks are built around a generic "thrown weapons" category Inner Tepenia doesn't have yet; those would attach to this blade-focused system once it exists. See `project_fallout_trait_perk_adaptation` memory.

  **Cross-project standing law confirmed 2026-07-23, written up in full at `Game-Mechanics/Combat/Throwing_Weapons.md`:** the fundamental retrieval principle is identical across Inner Tepenia AND all 3 planned Outer Tepenia trilogy titles, despite the very different engines (Inner Tepenia's top-down turn-based isometric vs. Outer Tepenia's 1st-/3rd-person real-time 3D open-world) — **a thrown blade stays exactly where it lands (ground, stuck in a surface, or in an enemy) until the player retrieves it**, never auto-returning to inventory. Only the implementation differs per game: Inner Tepenia gates the throw itself by range/stat-modifier checks before the action is even legal (every throw necessarily lands somewhere on the bounded tactical grid); Outer Tepenia's open world needs a separate "range of reach" concept (beyond it, a thrown weapon is lost for good) plus a confirmed exception for "iconic" unique weapons, which auto-return to inventory after a cooldown (illustrative example: 15 seconds) **only if the throw missed** — an iconic weapon that actually connects behaves like any ordinary thrown blade and must be manually retrieved. Full detail, including the still-open numeric questions, in the new file — not duplicated here.

  **Stat mapping — four dimensions to eventually work out (not urgent, future design & development):**
  1. Throwing distance/range — proposed: Might.
  2. Throwing accuracy — proposed: some combination of Agility and Calculation; exact formula/weighting not yet decided.
  3. Critical hit chance — not yet decided.
  4. Critical hit damage — not yet decided.

- [ ] **Piloting skill — reserved for the Outer Tepenia trilogy, explicitly not usable in Inner Tepenia, flagged 2026-07-26**
  Raised during the Agility-skill balancing pass on `Skills.md`'s restructure (see
  `Game-Mechanics/Character-Creation/Skills_Review_-_Verb_vs_Noun_Audit.md`) as a strong Agility-skill
  candidate — operating Rastras and other ground vehicles across the highway network. **Explicitly rejected
  for Inner Tepenia specifically**: as a turn-based, isometric game, there's no in-context moment where the
  player actually drives a vehicle, so the skill has nothing to attach to here. Held onto instead for the
  real-time, open-world Outer Tepenia trilogy, where vehicle operation is a genuine mechanical context. When
  design work reaches that series, ground it in what Inner Tepenia already established: the highway network
  (`Highways.md`), Rastra/Kharkovchanka vehicle culture, and the existing hitchhiking rules
  (`project_hitchhiking_highways` memory) — plus the still-separately-flagged "Antarctican motorcycles"
  vehicle-class idea (`project_antarctican_motorcycles_flagged` memory), which a Piloting skill would likely
  interact with directly.

- [ ] **Three FNV-ported perk candidates deferred — all depend on a system Inner Tepenia doesn't have yet, flagged 2026-07-26**
  Surfaced while cross-checking `Regular_Perks_-_Level-Up.md` against a complete real FNV perk list
  (`to-be-integrated/Fallout_New_Vegas_-_perks_full-list.txt`; full sorting in `Game-Mechanics/Perks/
  FNV_Perk_Cross_Reference_Audit.md`). **Long Haul** (real effect: "being over-encumbered no longer prevents
  you from using fast travel") and **Explorer** (real effect: reveals all fast-travel locations on the map —
  corrected 2026-07-26 from an earlier mischaracterization as quest-marker-related; it has nothing to do with
  quests) both require a fast-travel system, which Inner Tepenia does not currently have. **Adamantium
  Skeleton** (real effect: "damage taken by limbs reduced by 50%") requires a limb-specific damage system,
  which doesn't exist anywhere in the current docs either. None of the three were added — not a rejection of
  the perks themselves, just genuinely blocked on missing prerequisite systems. Revisit once (or if)
  fast travel and limb-specific damage get designed.

  **Update, 2026-07-28 — limb-specific damage system now developer-confirmed wanted, and two more traits
  join the pending-prerequisite list.** The developer explicitly confirmed limb-crippling should exist "just
  like in Fallout," independent of Adamantium Skeleton specifically — this is no longer a neutral "maybe
  someday" item, just still genuinely undesigned. The new FNV-ported trait **Small Frame**
  (`Character-Creation/Traits.md`) also depends on it. Two more newly-ported traits add two more pending
  systems to this same list: **Early Bird** needs a day/night cycle (same blocker as Night Person/Solar
  Powered above), and **Logan's Loophole** needs a robot-equivalent addiction/chems system (same blocker
  already flagged for Chemist/Chem Resistant/Implant GRX). **Four Eyes** adds a genuinely new, previously
  unflagged prerequisite: some kind of equippable/removable optical or sensory augmentation slot — a robot
  equivalent of "wearing glasses." See `Traits.md`'s own updated Fallout-Adapted Traits section for all four.

- [ ] **Demagogue trait needs sufficient crowd/group-address content, flagged 2026-07-28**
  Surfaced while assigning Trisha Miller's forbidden traits (`Core-Mechanics/Forbidden_Trait_Design_Method.md`).
  The new **Demagogue** trait (`Character-Creation/Traits.md`, Base traits) grants +20% Speech/Narrative
  effectiveness specifically when addressing groups or public gatherings — but it's not yet confirmed the
  game actually contains enough interactions where the player addresses a crowd (as opposed to one-on-one
  dialogue) for that bonus to be meaningfully usable. Not a rejection of the trait — Trisha's own forbidden
  trait assignment stands regardless — just a real content dependency to revisit once dialogue/quest design
  reaches this question.

- [ ] **SOC archetype Moderate-tier elaboration — deliberately deferred, flagged 2026-07-26**
  Surfaced while developing `Game-Mechanics/Perks/SOC_Cross_Reference_Perk_Concepts.md`'s Concept 1
  (district-flavored archetype variants) and Concept 4 (Portable Expertise), both of which were scoped to
  Strong-tier district matches only, per `Reference/Real-World/jobs_professions_and_fields/
  SOC_Cross_Category_District_Matching.md`. The Moderate-tier matches (tagged there as future Sidequest
  material) are real and cataloged, but deliberately not developed further yet — the developer's own
  sequencing call: the main skeleton of the city (main questlines, established district structure) needs to
  exist first, then side- and mini-detail work fills in afterward. Revisit this once that skeleton is in
  place, working the same archetype-by-archetype, one-at-a-time process already used for the Strong tier.

- [ ] **DLC-scoped FNV perk candidates — assigned to specific DLCs rather than the base 160, flagged 2026-07-26**
  Also surfaced during the FNV perk cross-reference audit (`Game-Mechanics/Perks/FNV_Perk_Cross_Reference_Audit.md`).
  **Hunter, Entomologist, Animal Friend, Tribal Wisdom** (wildlife/mutated-creature bonuses) are confirmed
  **Mirny DLC (DLC 7)** content, tied to Davis's near-idyllic, breadbasket-adjacent setting — the closest thing
  to huntable wildlife Antarctica plausibly offers. **Shotgun Surgeon, The Professional, And Stay Back**
  (traditional-firearm-specific bonuses) are confirmed **Halley DLC** content, since traditional firearms
  only exist in coastal cities with real cause for concern over an Upper Earth invasion — locked to Halley
  over Palmer after a lore check (Palmer is an established tourism/diplomatic gateway, not a militarized
  culture, and was itself the target of Upper Earth's wartime strikes; Halley's Belgrano has genuine ongoing
  military civic character plus the subnet's broader working-class/industrial identity). **A base-game
  equivalent for the latter three is still needed**: the developer confirmed "items-turned-weapons"
  counterparts are possible — proposed direction is three new perks built on the
  existing Improvised Weaponry perk (DT-penetration, sneak-attack-crit, and knockback versions), not yet
  drafted.

- [ ] **A Tepenian counterpart to Karma/Sanity — genuinely open, no shape decided yet**
  Flagged 2026-07-04: the developer wants some kind of in-universe system in the spirit of Fallout's Karma or Fallout DUST's Sanity — a persistent, personal player-character standing or psychological state, distinct from faction reputation (which already exists) — but is explicit that it definitely won't be Karma and probably won't be Sanity either. No shape, mechanic, or name decided; this is a "the idea appeals, the implementation doesn't exist yet" flag, not a design brief. Possible existing anchor points worth considering whenever this gets picked up (not decided, just noted): the Humanity and Nerve MACHINE stats, and the game's central robot-consciousness theme, all already touch adjacent territory.

- [ ] **Charging pods — sporadic world rest-spots, flagged 2026-07-04**
  New environmental feature, not yet designed: scattered, free-to-use rest/recharge spots placed around the world, akin to Fallout: New Vegas's mattresses (as opposed to owned player homes) — presumably robot-facing (a charging-pod equivalent of "resting"), offering some kind of temporary benefit and/or save opportunity without requiring ownership of a bed or home.

- [ ] **Amundsen Tower power supply — spec sheet (flagged 2026-07-03, held for later)**
  `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Infrastructure/Amundsen_Power_Supply.md` exists as an empty placeholder — meant to detail how Amundsen Tower actually gets its power: where it comes from, how it's generated, distribution, etc. Explicitly deferred; pick up later.

- [ ] **DLC 5 (Halley subnet) — working central-conflict anchor: Troll Airfield control**
  Established 2026-07-03: control over Troll Airfield (the only intercontinental-capable runway in the Halley subnet, functional post-war but contested) is the current working candidate for DLC 5's central conflict/"MacGuffin." Explicitly tentative — full details (who's contesting it, to what ends, the specific conditions of each subnet city and faction) wait for actual DLC design & development, and it's possible that further development of the subnet/storyline surfaces something else as the true centerpiece, with the airfield becoming an important side-piece rather than the main objective. Still, a solid working anchor rather than a blank slate. See `Storyline/DLC_Overview.md` (DLC 5 entry), `Cities/Specs/Troll.md`, and `Cities/Local_Cultures/Halley_Subnet/Troll.md`.

- [ ] **Halley DLC 5 — a permanent-loss path where the city falls into the sea**
  Flagged by the user 2026-07-03, explicitly for when actual DLC 5 design & development begins — not now. Among the multiple possible DLC 5 player-choice resolutions, one option should trigger an out-of-game chain reaction (a 2nd/3rd-order consequence, not shown directly) whose end state is that nobody is left to maintain Halley's ongoing relocation program. Without active management, the Brunt Ice Shelf's natural calving process takes over, and the city eventually falls into the sea and is gone permanently — no one left to build or maintain it. See `Specs/Halley.md` Open Questions and `Cities/Local_Cultures/Halley_Subnet/Halley.md` ("Built to Move") for the established premise this plays off of: Halley only survives through continuous active relocation choices, so letting that choice lapse is the natural worst-case path.

- [ ] **Byrd DLC — three candidate central-conflict anchors, none chosen yet**
  Flagged 2026-07-08. Byrd is the sole city in its own subnet, so its DLC needs a central conflict that doesn't depend on inter-city subnet politics the way most other DLCs do. Three options discussed, all kept as live candidates — a fourth ("Whose City Is It," an internal political-legitimacy crisis riffing on Byrd's extreme national diversity) was explicitly rejected by the developer and should not be revisited:
  1. **The Chamber Crisis** — Byrd is one of only two currently-active Cradle sites manufacturing fabrication-synthesis chambers (see `Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md` and the resolved Cradle network memory). A threat to that capacity (sabotage, structural failure in "the chamber works," an outside faction trying to seize control) would give a single-city DLC genuine nationwide stakes.
  2. **What's Actually Down There** — Byrd was "built from below, then left alone," discovered via an expedition using old maps whose origin was never explained (see `Local_Cultures/Byrd_Subnet/Byrd.md`). A DLC could explore whether Byrd's full underground scale has ever actually been explored, and what built the structure the city now sits on top of.
  3. **The Isolation Crisis** — Byrd's long-standing unresolved aviation-route problem (no confirmed Byrd–Janbogo refuel stop, flagged elsewhere in this file) and its role as a genuine two-way freight hub (Hwy 1 to Palmer City, Hwy 22 to the South Pole) could anchor a supply-crisis plot testing Byrd's established "genuine sense of shared community despite isolation."
  Also flagged the same day: **Maggie Aarden** (`Characters/Dolls/Still-Present_-_In-Game/recruitable/Maggie Aarden/`) is, as of 2026-07-09, a **confirmed** recruitable companion for this DLC, settled permanently in Byrd post-exile — option 1 (Chamber Crisis) is the developer's own lean, specifically because it's the only one of the three that gives Maggie's established industrial/welding skill set a direct mechanical reason to matter to the main plot, not just an emotional one.

  **Design requirement, flagged 2026-07-08: Byrd itself needs unusual internal complexity.** Every other DLC spreads its story, conflicts, and factions across 4–8 cities with genuinely differing interests, letting any single city stay comparatively simple. The Byrd DLC has exactly one city carrying the entire DLC alone, with no second or third city to distribute complexity onto or play off against. For the player to have a genuinely rich experience here, Byrd itself — its districts, factions, competing interests, and internal social structure — needs to be developed with a level of depth closer to what other DLCs achieve *collectively* across their whole city roster, not what any one of their individual cities gets on its own. Bear this in mind specifically once actual design & development begins on this DLC, whichever central-conflict candidate above ends up chosen.

  **More fundamental than the DLC design itself, clarified 2026-07-08: this is first and foremost a requirement on the *city*, not just the DLC built on top of it.** The DLC's quests, factions, and story design can only be as rich as the underlying place actually is — so `Cities/Specs/Byrd.md` and `Cities/Local_Cultures/Byrd_Subnet/Byrd.md` themselves need to be developed with unusually deep foundational complexity (districts, social structure, internal diversity, physical layout of its underground scale) well before any DLC-specific quest or story design begins, since every other city in the project could stay comparatively simpler precisely because it had 3-7 subnet neighbors to share the load with. Byrd doesn't have that luxury — the city has to do the work alone that other subnets spread across their whole roster.

  **Addressed 2026-07-09:** Byrd's full Megasheet (`Cities/City_Megasheets/Byrd_Subnet/Byrd/`) proposes a concrete five-guild faction structure (Fabricators' Guild, Dispatch Office, Foundation Keepers, Prospectors' Circle, Grounded Wings) mapped directly onto Byrd's own established economic sectors, plus a project-wide Cross-Reference Synthesis pass identifying exactly how Byrd connects to the rest of Tepenia: the Cradle chamber-manufacturing network (Neumayer designs, Byrd and Sinheung build), the Rastra vehicle lineage running from Belgrano's founding-era invention through to Byrd's own present-day freight fleet and the DLC 1 Rastra, the Hwy 1 corridor tying Byrd to the Palmer subnet (Rothera as manufacturing peer, Esperanza as food supplier), and the Hwy 22 corridor's fragile passage through the Amundsen Station ruins, which the whole eastern half of Tepenia's supply chain depends on staying passable.

  **Companion allocation confirmed 2026-07-20:** under the new "Multiple Native Companions Per DLC" policy (`Companion_System.md`), Byrd is assigned the **3-5 companion tier** — real compensating depth, but deliberately less than Mawson's 6-10, since Byrd already carries more established narrative density (this whole entry) than Mawson does. **Explicitly, Byrd gets no invented smaller settlements** — unlike Mawson, where scattered settlements are treated as essentially required, Byrd's isolation is the point, not a gap to patch, so its depth comes entirely from the internal city-complexity work already described above plus companion variety.

- [ ] **Companion-Mediated Access — apply to Vosora, Kendra, and all other companions**
  Flagged by the user 2026-07-03, explicitly deferred to much later priority. The "Companion-Mediated Access" design law (`Game-Mechanics/Perks/Perk_Framework.md`) — each companion questline branch grants the companion access to a new place/faction/group, unlocking branch-exclusive activities and lore for the player — cannot be meaningfully applied to specific companions (Vosora's four branches, Kendra's three, or any other companion) until Concordia's in-world setting is built out further: its factions, its locations, and how access to them would reasonably play out in the game. Hold off until that foundational world-building work is further along. Cross-reference `feedback_companion_mediated_access` memory.

- [ ] **Re-number the DLCs by release order — after meta-personalities/histories/main questlines are set**
  Flagged by the user 2026-07-03, downstream of the subnet meta-personalities task above (and of each DLC's main questline/central problem being worked out — see `Storyline/DLC_Overview.md`). Currently DLC numbers 2-7 are essentially placeholder/subnet-order assignments (Byrd=2, Palmer=3, Mawson=4, Halley=5, Janbogo=6, Mirny=7), not a deliberate release sequence. We already know DLC 1 (South Pole, Kendra Heinrich) releases *last* regardless of its number (see `project_level_cap_dlc_progression` memory) — but the release order of the other six relative to each other is still undecided. Once each subnet's tone/story is actually known (from the meta-personality work and each DLC's main questline design), revisit and re-number DLCs 2-7 to match whatever release order makes the best narrative/pacing sense, rather than leaving the current arbitrary subnet-based numbering in place.

- [ ] **The issue of treaties — scope TBD**
  Flagged by the user 2026-07-03 as something they want to tackle at some point; explicitly deferred, not started. Exact scope not yet defined — could mean the Falkland Treaty's specific terms/text, other historical Upper Earth-Tepenia agreements, ongoing diplomatic/legal relations between Tepenia and Upper Earth nations, or something else. Likely connects to the already-flagged `project_upper_earth_trade_justification` open question (why Upper Earth trades with Tepenia at all) but scope needs clarifying with the user before starting.

- [ ] **Localization — target language list and scope**
  Draft tiered language list established 2026-07-03 at `Dev-Road-Map/Localization_Language_List.md`, weighing Steam market ROI against thematic ties to Tepenia's own founding nations (e.g., Korean's tie to Janbogo is the single strongest thematic case in the game). **Open:** realistic launch scope for a solo dev (full Tier 1 text localization vs. a smaller subset vs. English-only at launch), voice acting scope if any, community/fan translation policy, priority order within Tier 1 if not all languages happen simultaneously.

- [ ] **Per-city improvised weapons survey, then Concordia convergence pass** *(blocker cleared 2026-07-11 — city post-cultures project is complete; Phase 1 per-city derivation itself is simply not started yet)*
  Developer note (2026-07-03): once the per-city composite post-culture pass (`Cities/Local_Cultures/`) is complete for all cities, do a per-city, per-culture, per-setting survey to develop in-game weapons. **Core design principle:** these are generally not "weapons" in the traditional sense — they're survival/utility items specific to each city's harsh Antarctic environment and culture (tools built for cold-weather survival, resource extraction, industry, or daily life) that are repurposed as weapons in-game, which is exactly how and why they'd actually get used that way. Traditional weapons still have a place too, since Tepenians generally maintain some defensive preparedness against a possible Upper Earth invasion — but the improvised/cultural item is the primary design lens, not the exception. Depends on each city's finished cultural spec sheet (industry, crafts, cuisine, and material culture sections in particular) for what items would plausibly exist there.

  **Update 2026-07-11:** the 13-category weapon taxonomy (7 conventional, 3 energy-adjacent, 3 Tepenia-original) is now locked and cross-referenced into `Game-Mechanics/Combat/Damage_Types.md`, and a cross-media philosophy datasheet exists at `Worldspace/Weapons_and_Tools_Philosophy.md` for the Southern Lights TV series. The actual Phase 1 per-city item derivation described below has not started. See `project_per_city_weapons` memory for full progress.

  **Second phase (2026-07-03):** once every city's full unique set exists, find the commonalities across all of them and derive an adjusted, converged set of "improvised weapons" specific to Concordia — since Concordia's population is a multi-subnet refugee melting pot (see `World_History_Reference.md`, "Refugee geography in Concordia"), not a single origin culture, its weapon set should read as a blended common denominator across contributing regions, not any one city's pure set. **Player-facing sequencing this implies:** the player encounters this converged Concordia set first (main game), then discovers each city's fuller unique/regional variants over the course of the corresponding DLCs. See `project_per_city_weapons` memory for progress tracking.

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

- [ ] **Amundsen Time Code (ATC) — geographic rationale finalized 2026-07-23, implementation still open**
  Tepenia's equivalent of UTC — logically derived from the geographical stretch of Eastern Standard Time
  (EST / UTC−5), in exactly the same relationship UTC itself has to the geographical stretch of GMT (a
  logical timekeeping construct anchored to, but conceptually distinct from, an actual geographic zone).
  **Finalized rationale, three reasons:**
  1. **EST is the single longest-spanning time zone that physically exists**, geographically. Its
     farthest-north land is the farthest-north land in the world, with the sole exception of the very tip
     of Greenland — and even setting Greenland aside entirely, EST remains a substantially long time zone
     in its own right, even though it doesn't reach all the way to the southern tip of South America.
  2. **EST contains New York City** — one of the largest human settlements in all of human history, and one
     of the most ethnically and linguistically diverse.
  3. **EST is adjacent to the Antarctic Peninsula** — not encompassing it directly, but the next time zone
     over, the closest real-world time zone to Tepenia's own first-settled ground (Palmer City, where
     robots and their human allies first set foot in 2564).
  Named after Amundsen Station, the neutral inter-subnet relay at the South Pole — the most geographically
  "centerless" location in Tepenia, and thus the natural symbolic anchor for a pan-Tepenian timekeeping
  standard, exactly the same relationship the South Pole (as opposed to any single subnet capital) already
  has to the rest of the Federation.
  **Still open, not part of this rationale pass:** in-game display (clocks, the Arcanet, NPC dialogue),
  whether the war/Planetary Split Brain disrupted timekeeping consistency across subnets, and how ATC
  relates to polar night/midnight sun (no sunrise/sunset to anchor local time perception).
  To develop: how ATC is displayed in-game (clocks, the Arcanet, NPC dialogue); whether the Long Night War disrupted timekeeping consistency across subnets; whether the Planetary Split Brain created divergent local time conventions in isolated subnets; how ATC relates to the polar night / midnight sun (no sunrise/sunset to anchor local time perception).

- [ ] **Robot biology and culture — expand foundational document**
  New file created: `Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md`. Established canon: robots don't breathe but have internal thermal/sensory systems; siligel (food), coolant (drink), robot coffee (specialty coolant), and smoking (robot-specific vapor products interacting with internal systems) are all confirmed. Open questions remaining: siligel full composition, robot coffee exact formulation, smoking prevalence across Concordia's population, in-game smoking behavior beyond Naizelle and Zhuldyz.

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
  - DLC 1: South Pole — **Kendra Heinrich** (character established; level design proposal drafted 2026-07-03, see her `DLC_South_Pole_Level_Design.md`; combat/quest design still TBD)
  - DLC 2: West Antarctica / Byrd — character and storyline TBD
  - DLC 3: Antarctic Peninsula (Palmer City ruins) — character and storyline TBD
  - DLC 4: Mawson Region (Indian Ocean coast) — character and storyline TBD
  - DLC 5: Atlantic Coastal Region (Halley, Belgrano, Queen Maud Land) — **Salagéa Aparast** (confirmed canon); storyline TBD
  - DLC 6: Janbogo Region (Ross Sea) — character and storyline TBD
  - DLC 7: Mirny Region (East Antarctic coast and interior) — **confirmed as its own DLC slot**; central character and storyline TBD; known assets: Mirny city (Antarctic Circle threshold, Hwy 110 physical link to Concordia — *corrected 2026-07-04, this was previously described as a surviving Arcanet link, which was wrong: Mirny and Concordia are different subnets, and the Planetary Split Brain severed that connection like every other inter-subnet one; see `Specs/Mirny.md`*), Casey (destroyed, blocks Pink Lucy Route B), Vostok (robot geneticist confirmed — reduced-mutation genetics breakthrough, Lake Vostok connection), Kunlun (Ice Cold Buddhism holy site, observatory implementation required as story beat); note: Dome Fuji is Halley subnet (DLC 5), not Mirny subnet

- [ ] **Byrd / Framheim / Little America founding — lore development**
  Confirmed canon for the founding chain:
  1. Old maps preserved at former Palmer Station, former Rothera Station, and former Belgrano Station II documented Byrd Station's location
  2. A founding expedition using rudimentary early-era Kharkovchankas (primitive by later Tepenian standards; the vehicles existed in basic form from Soviet Antarctic programs) followed the maps to Marie Byrd Land
  3. Found no surface structure — Byrd Station was entirely buried by 2564 (abandoned ~2005, buried for centuries)
  4. Set up a surface camp, probed, found the tunnels; the settlement grew downward first (underground town) before expanding outward through lateral tunneling and then upward above ground
  5. Underground archives at Byrd contained records of Framheim and Little America
  6. A later expedition from Byrd used those records to calculate the recalculated Ross Ice Shelf position and rebuild Framheim / Little America from scratch, designed for ice movement
  To develop: who led each expedition; the specific maps found at Palmer/Rothera/Belgrano II and what they contained; how the early-era Kharkovchanka compares to the mature vehicle (relevant to the broader Rastra technology development arc); the architectural design of rebuilt Framheim (precedents, engineering approach).

- [ ] **Michelle Stanton — Rastra as DLC trigger and character thread**
  Michelle is one of the very few Concordia residents capable of physically leaving the city. Her Rastra gives her continental travel capacity that almost no one else in Concordia possesses. She stays anyway — a choice that has never been fully explained in-world. Two design directions to develop:
  1. **Character revelation:** Why does someone who can leave choose not to? The answer to this question is a core piece of her personal questline — the choice to stay is as meaningful as the reason for it.
  2. **DLC trigger:** She is a natural vehicle for getting the player out of Concordia for at least one DLC. Her Rastra and continental expertise could be the practical means of departure; her reasons for finally leaving (or lending the vehicle) could tie directly into the DLC's stakes.
  See Michelle Stanton README — Design Notes.

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

Resolved items have been moved to [`DONE.md`](DONE.md) (split out 2026-07-12 to keep this file focused on outstanding work). New completions should be appended there, not left inline here.
