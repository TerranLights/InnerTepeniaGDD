# Amundsen Station: canon constraints for the formative town design (2026-11-21)

**Status: a reading digest. No design, no ruling, no recommendation.** It tells the people designing the town (its infrastructure, its people, their things, and the two settings, one above the surface and one below) what canon already fixes, what is only written down, and where the files disagree. Nothing here changes any other file.

**How to read the marks.**
- **FIXED**: canon, or ruled by the developer. The ruling is named.
- **SOFT**: written in a canon-tree file but never ruled: proposals, drafts, "plausibly", "suggested", working figures, provisional sheets, megasheet extrapolations.
- **CONFLICT**: two sources disagree. Both are quoted. Not settled here.

**Short names used for files** (paths under the GDD root, `<G>` = `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD`, `<C>` = `<G>/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities`):
- **SPEC** = `<C>/Specs/Amundsen-Scott subnet/Amundsen_Station.md` (301 lines, read 2026-11-21)
- **INV** = `<C>/Research_Logs/Amundsen_Station_Canon_Inventory_2026-10-29.md` (its own line numbers into the spec are from the older 231-line spec; facts from files this digest did not open are cited through INV)
- **FRAME** = `<C>/Research_Logs/Amundsen_Station_Developer_Framing_2026-10-29.md`
- **COMP** = `<C>/Research_Logs/Amundsen_Station_Spec_Composite_Applied_2026-11-03.md`
- **PACK** = `<C>/Research_Logs/Amundsen_Station_Review_Pack_2026-11-03.md`
- **POWER** = `<G>/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Infrastructure/Amundsen_Power_Supply.md`
- **TOWER** = `<G>/Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`
- **MS-PHYS** = `<C>/City_Megasheets/Amundsen_Station/Amundsen_Station_Physical_Infrastructure_Attributes.md`
- **MS-COMM** = `<C>/City_Megasheets/Amundsen_Station/Amundsen_Station_Community_Infrastructure.md`
- **DLC1** = `<G>/Storyline/DLC_01_Echoes_of_Amundsen.md`
- **SIDE** = `<G>/Storyline/DLC_01_South_Pole_Side_Content_Suggestions.md` (opened for lines 1 to 30 and 68 to 75 only; holds the developer's 2026-10-18 answers)
- **KLD** = `<G>/Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/Kendra Heinrich/DLC_South_Pole_Level_Design.md` (opened for lines 1 to 60, 95 to 125, 155 to 200 only)
- **VISION** = `<C>/City_Vision_Notes/Amundsen_Station.md`
- **CULT** = `<C>/Local_Cultures/Amundsen_Station/Amundsen_Station.md`
- **RCULT** = `<C>/Local_Robot_Culture/Amundsen_Station/Amundsen_Station.md`
- **PRETRIP** = `<C>/City_Development_Passes/Amundsen_Station/Amundsen_Station/00.0_Pre-Trip_Inspection.md`
- **READER** = `<G>/Reference/Real-World/Climate Data/READER/Amundsen_Station.md`
- **MREF** = `<C>/City_Master_Reference/Mawson_Byrd_Amundsen_Reference.md` (Amundsen section, L228 to L284, plus its legend L5 to L14)
- **DRL** = `<G>/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md`
- **FREG** = `<C>/Founding_Register.md`

**Three standing warnings about the sources themselves.**
- **The two megasheets are SOFT throughout.** MS-PHYS calls itself "Not locked canon" (MS-PHYS L10 to L11). The master reference ranks megasheet extrapolation as draft, and says every vignette-style narrative is not canon (MREF L11). The pass sheet lists the megasheet folder as withheld from every city pass (PRETRIP L406). The developer has said the megasheets "will be rebuilt and the originals archived" (`DR-58`, DRL L1164). Several megasheet and robot-culture items rest partly on non-canon vignette material (RCULT L110 to L113); those vignette sources are not inputs and are not summarized here.
- **The culture and robot-culture sheets predate the town decision.** Both open with "never a city" caveats (CULT L5; RCULT L8 to L14), the robot sheet is "Provisional — findings are proposals" (RCULT L22 to L24), and both are read-last material, never inputs to a pass (PRETRIP L44 to L47, L407). Their "facility, not a city" statements are superseded by the ruled town wording (see section 6).
- **The vision note is not an input at any step** (`DR-10`, DRL L437; PRETRIP L409). Its one fact is already folded into the spec (SPEC L243).

---

## 1 · The site as physical ground

1.1 **FIXED.** Location: the Geographic South Pole, 90°00'S; the station is the official climate reference (SPEC L3; developer ruling 2026-09-04, SPEC L132 to L149: "the Tower's ground base sits on the station site"; the Magnetic South Pole is not here and any pass that moves the file toward it is "wrong by ruling", SPEC L141 to L145).

1.2 **FIXED.** Elevation about 2,835 m on the East Antarctic Plateau (SPEC L121).

1.3 **CONFLICT.** Ice thickness. SPEC L121: "on ice approximately 2,700–2,850 meters thick (sources differ)". TOWER L176 and L566 to L568: foundation depth "~2,700m … before hitting bedrock". MREF L259: "~2,850 m of plateau ice". INV L533 records the same split. No ruling picks one.

1.4 **FIXED.** The ice moves: "the station built on the ice drifts roughly ten meters per year, requiring periodic repositioning of the ceremonial pole marker" (SPEC L121; also SPEC L147). A city on moving ice "DEFORMS over 250 years" (`Extent_and_Area_APPROACH.md` L143, via INV L331).

1.5 **FIXED.** Cities may be built on ice: "All cities can be built on rock or on ice; ice cover is not a restricting factor. What matters is the area's physical and geological makeup" (`DR-61`, DRL L1254). The station's site has 0% rock (`Extent_and_Density_Per_City.md` L578, via INV L490).

1.6 **FIXED.** Snow that lands stays: falls about 70 mm a year water equivalent; "Lands (accumulates and stays): ~70–80 mm/yr … no wind removes it"; about 0 lost to sublimation and wind (SPEC L163 to L166); "Retention is ~100%: what falls, stays" (SPEC L169). The gauge figure of 2.1 mm is the caught total, not what falls (SPEC L155, L157, L162). Canon states water equivalent only; no snow depth or burial rate in meters is written anywhere read.

1.7 **SOFT.** Burial consequence: "Ground that rises. About 75 mm a year of snow lands and stays; things built on top are buried unless raised (derived by the candidates file; conditional on the developer accepting it)" (PACK L159).

1.8 **FIXED.** Temperature: mean annual −49.1 °C; coldest months July and August about −60 °C; warmest December and January about −28 °C; record high −12.3 °C (December), record low −82.8 °C (June) (SPEC L152 to L154; monthly table SPEC L179 to L192; READER L8, L14).

1.9 **FIXED.** The defining hazard is cold and altitude, not wind: "COLD, overwhelmingly … it sits above the katabatic regime … There is no whiteout-under-clear-sky here … Air movement is close to irrelevant" (SPEC L168 to L169). Average wind 5 to 7 m/s; storms "occur but are less frequent" (SPEC L156).

1.10 **FIXED.** Light: polar night about March 24 to September 21 (about 182 days); midnight sun about September 22 to March 23 (about 183 days) (SPEC L172 to L175). Twilight lasts about seven weeks after sunset (to about May 12) and before sunrise (from about August 2); full astronomical darkness only about May 13 to August 1 (SPEC L202). The sun returns as a 360° sunrise (SPEC L203). Diamond dust and ice halos are common (SPEC L204).

1.11 **FIXED.** Isolation: "the most difficult location in Tepenia to reach; there are no nearby cities, no coastal access, no external reference points" (SPEC L205). Landlocked; reached only by highway from a coastal port (`Ports.md` L205, L740, via INV L477). Concordia is about 1,660 km away in a straight line (DLC1 L20; TOWER L58, L199).

1.12 **FIXED.** Every direction from the Pole is north (SPEC L121, L211).

1.13 **FIXED.** The Tower's foundation reaches bedrock through the full ice sheet: "Foundation depth ~2,700m" (TOWER L176); "Any stable foundation … must bore down through that full ice depth to anchor in solid rock" (TOWER L566 to L571). (Canon working design of 2026-07-02; no DR number.)

1.14 **SOFT.** Tower base footprint: structural core about 63 m across (about 3,160 m²) (TOWER L175, L563); construction shaft assumed about 100 m across, about 21.2 million m³ of ice removed (TOWER L751 to L756); "Surface complex … plausibly on the order of 1–2 km²" (TOWER L942 to L948). The extent table gives the whole station 1 km² (`Extent_and_Density_Per_City.md` L629, via INV L489). See CONFLICT 11.6.

1.15 **SOFT.** Excavated ice: proposed partly melted for water during construction and operation, the rest "piled into engineered ice ridges/mounds around the base facility … artificial ice ridges ringing the facility" (TOWER L760 to L769; summary L28 to L32).

1.16 **FIXED (era: Tower years).** The Tower base sits on the station site (SPEC L136 to L139); the Tower is "anchored at the South Pole (Amundsen Station)" (TOWER L221).

1.17 **CONFLICT.** Where the relay physically sits is not stated. SPEC L274: the inter-subnet cable "ran through or alongside the tower system". The relay predates the Tower in some files and only begins with it in another (see CONFLICT 11.10). No file gives the relay's depth, building or distance from the Tower base.

1.18 **SOFT.** Depth figures inside the Tower shaft: the 1.63 km accelerator track sits at "the bottom of the shaft (deepest, anchored in bedrock)" and launches "straight up through the remaining ice/shaft distance" (TOWER L925 to L928). On TOWER's own figures (2.7 km shaft, 1.63 km track) that places the track roughly in the lowest 1.6 km, below about 1.1 km depth (this digest's arithmetic; not written in any file).

1.19 **FIXED (era: after the Long Night War).** The ruin: a "scrap mountain" of collapsed structure around the base (SPEC L249, L276). Debris spreads about 2 to 10 km, typically 3 to 4 km; a tall central pile with a thinner apron 2 to 4 km out (TOWER L906 to L919); pile height 27 to 109 m depending on spread (TOWER L864 to L868). (The figures are SOFT estimates; the scrap mountain itself is canon.)

1.20 **FIXED (era: after the war).** Crevasses fractured by the Tower's impact around the scrap mountain (DLC1 L86 to L90); live residual-charge zones at severed accelerator and bearing wreckage (DLC1 L76, L83).

---

## 2 · What canon already places ABOVE the surface

2.1 **FIXED.** Highway 22 (the Transcontinental Highway) "passes directly through" the station (SPEC L7, corrected 2026-07-06 and 2026-10-31; `Highways.md` L141, L146 via INV L470). It was built before Tower construction proper began (TOWER L1056 to L1060).

2.2 **FIXED.** The Tower's guide tube rises from the base (150 km tall) and its passenger and cargo cars run on a separate vertical maglev track beside it (TOWER L170, L474 to L488). A Base Terminal at 0 km: "Main terminal; surface transport connections; accelerator/power complex" (TOWER L630). (Mechanism and height canon; the waystation list is a "Proposed layout", TOWER L625 to L636, so the terminal's name and layout are SOFT.)

2.3 **FIXED (era: after the war).** The actual Amundsen-Scott South Pole Station building stands and is locked from inside by Kendra Heinrich: "the pre-war scientific facility, the real-world building that exists at the South Pole today" (DLC1 L172, L290). It has a main entrance (DLC1 L200), an external intercom (DLC1 L218), a damaged section with a breach point (DLC1 L192), ventilation intakes "buried in the snow at several points around the building" (DLC1 L196), and, on the far side from the main entrance, "a pre-war maintenance hatch for the station's geothermal power infrastructure" reached across open ice (DLC1 L194). See CONFLICT 11.1.

2.4 **SOFT.** Tower surface complex: "worker/robot support facilities, cargo processing terminals, administrative buildings, surface transport connections toward the rest of Tepenia" (TOWER L942 to L946).

2.5 **SOFT.** Ice ridges ringing the base as windbreaks (TOWER L765 to L769). See CONFLICT 11.7.

2.6 **SOFT.** An Observation Dome oriented to the sky (MS-COMM L37 to L41). It is the only megasheet space whose purpose requires a view of the sky; no layer is stated.

2.7 **FIXED.** The Geographic South Pole marker, periodically repositioned because the ice drifts; its present form and survival are open (SPEC L250, L300).

2.8 **FIXED (era: after the war).** Kendra's exterior kill zone: automated weapons at the approaches, still running 10 to 15 years later (DLC1 L112, L172 to L174).

2.9 **SOFT (era: after the war).** A hub camp proposed on "Clear Ground … beyond ~4–10 km" from the ruin (KLD L110).

---

## 3 · What canon already places BELOW the surface

3.1 **FIXED.** An underground utility tunnel network "carved into the ice, built during the pre-war era"; one entrance is "buried under accumulated debris near the outer ruins" behind a frozen-shut hatch (DLC1 L188). It was carved "directly into moving ice" (DLC1 L120). It should hold lore content from the war (DLC1 L190).

3.2 **SOFT (developer, 2026-10-18).** "There can be one general underground network below the ice, leading toward the station, and a further, deeper series of underground chambers, which is where the player eventually finds Kendra Heinrich" (SIDE L23). The developer's idea: "two pathways to the station: one overland, one below the ice", with "an underground network of tunnels, stations, actual living infrastructure" (SIDE L11, L13), and "an entirely different set of lethal, deadly dangers" above and below (SIDE L15). SIDE's own status is "collection of suggestions, not canon" (SIDE L3); what the dangers are is held off "until it is known what the place is actually like" (SIDE L24).

3.3 **SOFT (developer framing, 2026-10-29, "NOT a ruling").** The town has "infrastructure both above and below the surface" (FRAME L3, L5). Not decided: "which layers hold housing, work and public life" (FRAME L11). Additive only; replaces nothing (FRAME L14).

3.4 **FIXED.** The Tower's foundation shaft reaches bedrock about 2.7 km down (see 1.13).

3.5 **SOFT.** What the shaft holds: the vertical linear accelerator at the bottom; power generation "above/alongside the accelerator"; pellet storage and the return loop; "Maintenance and access tunnels threading through all of the above" (TOWER L923 to L940; also L521 to L525). POWER L28 repeats the generation siting and calls it "a design inference, not a ruling".

3.6 **SOFT (era: after the war).** The shaft "very plausibly survived", sealed off and "damaged near the power plant vault", with surface access crushed or buried; "two very different environments stacked on each other" (KLD L28 to L39, L110). KLD's status: "proposed working direction, not locked canon" (KLD L3 to L8).

3.7 **SOFT.** The underground tunnel network is MS-PHYS's "confirmed DLC 1 lore-content site" (MS-PHYS L107 to L113).

3.8 **FIXED.** Things that are buried by the site's own processes: the ventilation intakes (DLC1 L196) and the tunnel entrance (DLC1 L188) (see 2.3, 3.1).

---

## 4 · Things canon mentions without saying above or below

4.1 **FIXED.** The inter-subnet relay hardware (SPEC L5, L8, L221; "the Arcanet relay hardware"). No layer stated. MS-PHYS adds a separate relay monitoring and control room (MS-PHYS L58 to L65, SOFT).

4.2 **FIXED.** The pre-Split-Brain archive: "deep within the ruins, accessible but not easily" (SPEC L251); it "survived in a protected location within the ruins" (SPEC L276). "Deep" is not defined as underground. Its origin: Pergamino's archive was hauled "further and deeper into Antarctica" (`Specs/Palmer subnet/Pergamino.md` L166, via INV L417), a geographic, not a depth, statement. Datadrives arrived by truck (DLC1 L261).

4.3 **SOFT.** Archive vault, a separate record-intake and synchronization room, and a guardian system (MS-PHYS L98 to L105, L129 to L132; DLC1 L237 to L239 commits only to "the archive should not be trivially accessible").

4.4 **SOFT.** Living quarters, a central mess (the Commons Hall), a mediation room, a message room, a greenhouse bay, an exercise bay, a crew handoff record, small training offices (MS-PHYS L80 to L94; MS-COMM L27 to L62). No layer stated for any.

4.5 **SOFT.** A bulk export terminal with cranes and "magnetically-levitated rail systems for moving material up the Tower", and a separate passenger terminal (MS-PHYS L71 to L76; DLC1 L126). Location relative to the surface not stated.

4.6 **FIXED.** The hostel or barracks for space workers on leave (`DR-64`, DRL L1295). No layer stated.

4.7 **FIXED.** The station's "geothermal power infrastructure" has a surface maintenance hatch (DLC1 L194); where the plant itself sits is not stated. See CONFLICT 11.8.

4.8 **FIXED.** The town's supporting community "(kitchens, utilities, medicine, teaching, offices, recreation)" (SPEC L221). No layer stated.

---

## 5 · Infrastructure systems

### Power
5.1 **FIXED.** The Tower's primary purposes are continent-scale energy regulation and bulk material mass-driving; passengers are a side use (TOWER L5 to L17, L75 to L162; POWER L11).
5.2 **FIXED.** The Tower draws about 324 GW net, continuously, and must never lose power: "Stop the power and it FALLS" (TOWER L173, L423 to L429; POWER L17). Its fall caused a continent-wide load-rejection overload (POWER L13; TOWER L103 to L117).
5.3 **SOFT.** Generation at the base is "plausibly an advanced nuclear/fusion reactor array … supplemented by geothermal taps into Antarctic subglacial volcanic activity" (TOWER L929 to L934); POWER L28: "a design inference, not a ruling".
5.4 **FIXED.** The national grid came "fully online" at the Tower's completion (about 2688) (POWER L12). A historical robot-fabrication site at Mountain Pass ran on overflow from the Tower's grid and ended when it fell (RCULT L347 to L355, citing the robot physiology file; SOFT as written in RCULT).
5.5 **FIXED (national, provisional).** A robot's charge draws on the electric supply, and warming a cold cell to charge it also draws on it; no rate written (`DR-140` item 4, DRL L2034; `DR-138` item 8, DRL L2014, "PROVISIONAL pending research").
5.6 **SOFT.** Before the Tower: no file says what powered the station. POWER says canon establishes no plant outside Concordia and the Tower complex (POWER L33), and lists the station among places with no neighbor within 500 km (POWER L61). For Relung Panen only, the developer ruled "a continental grid before the Tower, its regulation later" (`DR-140` item 8, DRL L2034); whether that applies here is not ruled.
5.7 **CONFLICT.** Nuclear power. POWER L40 to L41: the treaty draft bans nuclear explosives and radioactive waste disposal but not reactors, while the treaty scaffold's gloss says Tepenia runs "on the Amundsen Tower's grid-regulation model instead of nuclear power … a treaty-mandated one". "Unresolved." If reactors are allowed, spent fuel must leave the territory (POWER L43).

### Heat
5.8 **FIXED.** "Tepenia is a cold country that heats with electricity" except the volcanic exceptions (POWER L19). Every non-geothermal city's heat "is a national service, delivered, and interruptible" (`Geothermal_Heating.md` L98, via INV L434).
5.9 **FIXED (national).** Processing siligel is exothermic, "so warmth costs siligel" (`DR-137` item 5, DRL L2003).
5.10 **SOFT.** Antarctic cold reduces the cooling load on the Tower's superconducting systems (TOWER L346 to L350).

### Water and waste
5.11 **SOFT.** Water: the excavated shaft ice was proposed as a water windfall during construction and operation (TOWER L760 to L764). No other water source is written.
5.12 **FIXED (national, treaty draft standing).** Radioactive waste may not be disposed of in Tepenia (POWER L40). No other waste canon exists for the station.

### Food
5.13 **FIXED.** "All supplies came in from elsewhere; nothing was produced for export" (SPEC L241). The station is an ice-sheet forced food importer with the food term at 10% (Division of Industry `16` L114, L3458, via INV L453; `13` L73, via INV L451).
5.14 **FIXED (national).** Siligel is synthesized from mined minerals, processed only in some cities, then shipped on (`DR-137` item 5, DRL L2003). Siligel is robot food, "not lubricant, not blood, not a structural fluid" (DLC1 L38).
5.15 **SOFT.** A small greenhouse bay for crew wellbeing, not calories (MS-COMM L42 to L45). Whether the station grows any food is an open question (INV L710).

### Communications
5.16 **FIXED.** The station is the inter-subnet relay, the neutral switching point for all six subnets (SPEC L5, L125). Highway 59 "doubles as the Arcanet cable corridor to the Pole relay" (MREF L283; also `Local_Cultures/Halley_Subnet/Halley.md` L201, via INV L294).
5.17 **SOFT.** The Tower as "a physical Arcanet relay anchor" toward orbit (TOWER L1107 to L1109, a tertiary function "none designed in detail yet").
5.18 **SOFT.** The Amundsen Time Code is named after the station (`TODO.md` L1690, via INV L419; implementation open).
5.19 **SOFT.** A message room and a weekly message day for personal mail home (MS-COMM L49 to L51, L106 to L109).

### Transport
5.20 **FIXED.** One highway reaches the station: Highway 22. Highways 175 and 59 end at ramps with Highway 22, Highway 175's ramp nearer the Pole (SPEC L7, L298; MREF L274 to L282).
5.21 **FIXED.** No airport at the station (`Airports.md` L50, L54, via INV L476). Mountain Pass Airport is "reasonably accessible" via the Highway 22 junction (`Airports.md` L18, via INV L476).
5.22 **FIXED.** Later-era Rastras cruise at about 45 km/h (`DR-63`, DRL L1281). Derived travel times from the station (road lengths estimated, "not canon"): Byrd about 1.4 days, Janbogo or Zukelli about 2.2 days, Concordia about 3.7 days (DRL L1284).
5.23 **FIXED (era: Tower years).** Passengers ride 30-person maglev cars, about 6 minutes one way, design capacity about 194 people an hour (TOWER L683 to L694). Cargo goes both up and down; only the Tower carries people or brings anything down (TOWER L315 to L336).
5.24 **SOFT.** A maintained bypass through or around the debris field on Byrd's freight route (proposed 2026-07-09; `City_Relationship_Database.md` L85, L135, via INV L472).
5.25 **FIXED.** Tower materials came overland from ports by tracked convoy, before and while Highway 22 existed (TOWER L1029 to L1069).

### Medical, fire, security
5.26 **FIXED.** "Medicine" is named among the town's supporting services (SPEC L221). The national medical institutes file has no line naming the station (PRETRIP L297). Nothing else is written.
5.27 **FIXED.** No fire service, fire rule or fire hazard is written for the station in any file read. (Empty in canon.)
5.28 **FIXED (era: after the war).** "Station security systems gone rogue" exist as a minor enemy element (DLC1 L160), so the station had security systems.

### Fabrication chambers
5.29 **CONFLICT.** `DR-55` (DRL L1099) and `DR-89` (DRL L1563): "Every city in the entire country has an entire series of fabrication chambers (since there are robots from every city) and the one and only exception to this is Dome Fuji". RCULT L208 to L211: "No confirmed manufacturing chamber … existed at Amundsen Station itself". Whether the ruling's "every city" covers this station is not ruled.

---

## 6 · The people

6.1 **FIXED.** Census I: 1,121 humans, 5,736 robots, 6,857 combined (about 84% robot). Census II: 913 humans, 3,978 robots, 4,891 (about 81% robot) (SPEC L14 to L15). "The official census governs its population" (`DR-58`, DRL L1167; developer, SIDE L20). The population does not change (`DR-98` item 6, DRL L1651).

6.2 **FIXED.** Build to Census I: "Everything is assumed with Census I, because that's the maximum size per city that each city needs to accommodate" (`DR-4`, DRL L211 to L218).

6.3 **FIXED.** A town, not a skeleton crew: the spec now reads "a small town of rotating staff drawn from all of Tepenia" (SPEC L15) and "it grew into a small town: the staff who keep the network hub and the Tower base running live there for months to years, and a supporting community (kitchens, utilities, medicine, teaching, offices, recreation) grew around them. The population is small beside the station's strategic importance, and most of it is robot" (SPEC L221). Ruled: developer's town decision of 2026-10-31 (PACK L7) and `DR-98` item 5 (DRL L1651). "Definitely a full town during the Second Interwar Period" (developer, SIDE L21).

6.4 **FIXED.** Composition: "a composite of all of Tepenia, since there are people living & working there for periodic stays coming from all over the country" (`DR-98`, DRL L1650 to L1651). All 83 nations printed; Primary: Korea, Sinian Federation, Japan, Australia, CSA, United Kingdom; Significant: Indonesia, Germany, Brazil, France, Appalachia, Cascadia, New England; Notable: the other 70 (SPEC L19 to L21, L29 to L113; COMP L3). Robots use the humans' proportions (`DR-98` item 3). The old Norway and Chile notes are retired (COMP L15).

6.5 **SOFT.** What a robot's national origin means at the station is unsettled: robots each come online in a city's fabrication chambers, and "The robot-side translation of a national origin needs his input" (PACK L271).

6.6 **FIXED.** No founding nation: "Multi-subnet technical crews on rotation; no founding nation (neutral by design)" (FREG L75; `DR-44`, DRL L929; SPEC L223).

6.7 **FIXED.** Rotation: people "came from across Tepenia on rotation, served their term, and returned to their home cities" (SPEC L223); terms of "months to years" (SPEC L229).

6.8 **SOFT.** Term lengths: "six months to two years" (RCULT L14); "six months up to one or two years" (MS-COMM L10 to L11). Neither is ruled.

6.9 **FIXED.** Jobs named in ruled text: "scientists, engineers, cooks, chefs and other staff", who stay "a solid majority of its population at any time" (`DR-64`, DRL L1295); kitchens, utilities, medicine, teaching, offices, recreation (SPEC L221); the day's work is "scientific, technical, and mechanical maintenance" of the relay and Tower (SPEC L243; VISION L19).

6.10 **CONFLICT.** The Division of Industry split. Relay operations and maintenance 60%, Tower operations 30%, life support 10% (CULT L146 to L148; `04` L79 via INV L449). `16` §35 is headed "DETERMINED" (mandated 61.4%: relay 2,576 workers, Tower 1,288; free 429) (`16` L3451 to L3481, via INV L453), while other files say the station's Division of Industry is "still to be done" (INV L527). The archive has no line in the split (`16` L1238, via INV L454).

6.11 **SOFT.** Other roles written only in SOFT files: archive record intake and reconciliation, mediation hosts, incoming-crew orientation, survival refreshers (MS-PHYS L101 to L105; MS-COMM L53 to L62).

6.12 **FIXED.** The hostel: the station "keeps hostel- or barracks-style infrastructure, not homes, only for the share of workers on leave who have no friends or family to go to" (`DR-64`, DRL L1295). Working share 20%: about 287 beds in Census I (about 330 with surge), about 198 in Census II (about 228 with surge), about 4% of residents (`DR-65`, DRL L1304 to L1305; "a working number, not a final figure"). Guests stay counted in the space workforce, not the station (DRL L1294).

6.13 **FIXED.** The space workforce exists only in Census II (7,923, shift labor in orbit after the Tower's completion); the maritime fleet is the station's Census I share (`DR-69`, DRL L1350 to L1351). See CONFLICT 11.12.

6.14 **FIXED.** Neutrality is structural: "It belonged to no subnet because it was too central to belong to any one" (SPEC L125). Counted as a seventh "subnet" only "for the sake of completion … technically a nexus, and not a subnet" (`DR-17`, DRL L528 to L529).

6.15 **FIXED.** Mediation without authority: disputes "were sometimes brought to Amundsen Station for mediation — not because it had formal authority over inter-subnet matters, but because its neutrality was respected" (SPEC L231).

6.16 **FIXED.** Who is in charge: no file names a governing body, office or head. And no pass may write it yet: "no pass writes a city's government form or its justice, law or law enforcement until the DCI is fully complete … Until then a pass writes only where decisions fall and who is present" (`DR-137` item 11, DRL L2003). Factions also wait until the whole national process is done (`DR-58`, DRL L1166).

6.17 **FIXED.** Language: Hawaiian (later Tepenian) is dominant everywhere (`DR-89`, DRL L1563; `DR-100`, DRL L1669). The station's supporting tier is left open (`DR-98`, DRL L1652).

6.18 **FIXED (developer decisions, no DR number).** "Morale and belonging matter as much as survival", and the station and Byrd "must feel like two different DLCs" (PACK L7). Facet: "We need to keep them from climbing the walls" (PACK L161).

6.19 **FIXED.** Kendra Heinrich, a robot, is the station's one known present occupant (era: after the war) (SPEC L258, L278).

---

## 7 · Things people have

7.1 **FIXED.** Nothing is produced locally for export; all supplies come in (SPEC L241). No shop, market or store is named in any file read.
7.2 **FIXED.** No currency backing, unit, rate or name may be written (`DR-3`, PRETRIP L395).
7.3 **FIXED.** Robots eat siligel (DLC1 L36 to L38); siligel arrives processed from elsewhere (`DR-137` item 5).
7.4 **FIXED.** Rastras, the overland vehicles (SPEC L215, L252; `DR-63`).
7.5 **SOFT.** The Wall of Home: departing crew leave "a personal object, photo, or marker representing their own home city", never formally curated (MS-COMM L31 to L36; MS-PHYS L320 to L345). Its founding story in RCULT L160 to L161 rests on vignette material (not canon).
7.6 **SOFT.** Personal projects from a weekly craft and hobby block, "small, personal physical objects still findable in the ruins" (MS-COMM L102 to L105).
7.7 **SOFT.** Recreation and shared spaces: the Commons Hall, Observation Dome, Greenhouse Bay, Exercise Bay, Message Room (MS-COMM L27 to L51); a weekly rest day and shared meals (MS-COMM L74 to L101).
7.8 **SOFT.** "Purely functional, extreme-cold technical gear"; music "whatever individual rotating staff brought with them" (CULT L113, L119). Both written under the superseded "facility" framing. Dishes, music, dress, games and slang wait for the cultural synthesis in every city (`DR-140` item 2, DRL L2034, FIXED as a sequencing rule).
7.9 **SOFT.** Passenger-terminal personal items: "a farewell note, a ticket stub, a piece of luggage" (MS-PHYS L253 to L256).
7.10 **FIXED.** "Recreation" is named among the town's services (SPEC L221).

---

## 8 · Era: which period a fact belongs to

8.1 **FIXED.** First Interwar Period: 2083 to 2564 (DRL L1510). The real Amundsen-Scott station exists; Tepenians may inherit its physical infrastructure (`DR-24`, DRL L631), records, logs, journals, manifests and maps (`DR-25`, DRL L645), and research, equipment and techniques (`DR-26`, DRL L661), but never a tradition (`DR-25`, DRL L646). The real operator is a coordinate only, never a reason for founders, identity or culture (`DR-19`, DRL L551 to L552). Namesakes are "never a basis for data" (`DR-32`, DRL L752).
8.2 **SOFT.** "Established post-Falkland Treaty on the mature Amundsen-Scott South Pole Station infrastructure" (CULT L36).
8.3 **FIXED.** Founded after the Falkland Treaty (2564) as a facility (SPEC L221). Act 1 is "2564 → somewhere in the 2600s, a hazy range" (`DR-31`, DRL L737). No founding date is knowable yet; histories come after the ULM (`DR-16`, DRL L522 to L523).
8.4 **FIXED.** Census I is "before construction of Amundsen Tower and the onset of orbital colonization" (census, via INV L403); the governing census figure "dates to before ~2688 (±~20)" (`DR-143` item 3, DRL L2063).
8.5 **FIXED.** Highway 22 is built through the station before Tower construction proper; construction proper runs roughly 2671 to 2676 until completion about 2688, roughly the Second Interwar Period's midpoint, ±20 years (TOWER L1053 to L1065, L1126 to L1128; developer-confirmed 2026-08-05, TOWER L645 to L649).
8.6 **FIXED.** Census II is "immediately before the Long Night War, after decades of orbital migration via Amundsen Tower" (census, via INV L403).
8.7 **FIXED.** The Long Night War is 2812 (TOWER L643). The Tower falls; the station is destroyed; the Planetary Split Brain follows (SPEC L274).
8.8 **FIXED.** The game is set about 10 to 15 years after the war (DLC1 L170); grid instability runs into about 2822 to 2827 (POWER L14). What the town is like after the war "is still to be determined" (SIDE L21).
8.9 **FIXED.** Default scope for the town design: "definitely a full town during the Second Interwar Period" (SIDE L21). In pass work the spec's Status field and post-war sections are not inputs (PRETRIP L413). The megasheets describe the station "as it was while active" (MS-COMM L12 to L13; CULT L5).
8.10 **FIXED.** The Tower's working life is about 120 to 124 years (TOWER L1084 to L1095).

---

## 9 · Parked for later (religion, holidays, festivals)

`DR-140` item 2 (DRL L2034): faith and holidays wait for the stage after the cultural synthesis, in every city. Citations only:
- St. Roald, venerated as a Saint (SPEC L233; `Worldspace/National_Holidays.md` L41, via INV L475).
- Whether there is a Tepenian Independence Day tradition at the station (SPEC L301).
- "St. Roald's Day (placeholder name)" (CULT L225); the religion section (CULT L168 to L171).
- A St. Roald observance site (MS-PHYS L137 to L142; Finding G, MS-PHYS L282 to L296).
- Midwinter Observance and Equinox Sunrise Gathering (MS-COMM L113 to L119).
- The robot-culture religion section (RCULT L221 to L235).

---

## 10 · Open questions the canon leaves for the developer

1. Which ice thickness governs: about 2,700 m or about 2,850 m (1.3)?
2. How deep does snow bury what is built, in meters a year, and does the town accept the "ground that rises" condition (1.6, 1.7)?
3. The Tower's foundation is fixed in bedrock while the ice around it moves about 10 m a year (1.4, 1.13). No file says how the shaft, tunnels or surface buildings deal with that movement.
4. Where is the relay hardware: above, below, inside the Tower base, or apart from it (1.17, 4.1)?
5. What powered and heated the station before the Tower (5.6)? Is there geothermal plant at the station (CONFLICT 11.8)?
6. Are reactors allowed in Tepenia (5.7)?
7. Where does the station's water come from outside the construction years (5.11)? Waste?
8. Does the station grow any food (5.15)?
9. Does the station have fabrication chambers (5.29)?
10. Which layer holds housing, work and public life (FRAME L11)? Where does the hostel sit?
11. Do families or children live there? "Teaching" is a named service (SPEC L221); MS-PHYS L80 to L81 says quarters were "explicitly not designed around family life".
12. How long is a term, and how are rotations staggered (6.7, 6.8)?
13. What does a robot's national origin mean at the station (6.5)?
14. Is the archive a staffed sector, and since when (6.10; INV L696)?
15. Is mediation a formal institution with staff, or an informal practice (6.15; INV L697)?
16. What scientific work, if any, beyond relay and Tower upkeep (INV L698)?
17. Census I is before the Tower; what do the Census I town's people do instead of Tower operations (CONFLICT 11.11)?
18. Does the Census I town have a hostel at all (CONFLICT 11.12)?
19. What is the town's extent: 1 km² or 1 to 2 km², and how much of it is underground (1.14; INV L705)?
20. Is the underground network and its deeper chambers Second Interwar canon or post-war DLC design only (INV L706; SIDE L23)?
21. Where is Kendra: inside the station building, or in the deeper chambers (CONFLICT 11.1)?
22. What are the dangers above and below (SIDE L24)?
23. The station's supporting-tier language (6.17).
24. Which Tower terminal, waystation and surface-complex layout is adopted (2.2, 2.4)?

---

## 11 · Every CONFLICT found

11.1 **CONFLICT. Does the station building survive, and where is Kendra?** DLC1 L172: she "retreated inside the actual Amundsen-Scott South Pole Station — the pre-war scientific facility, the real-world building that exists at the South Pole today — and locked it from inside". SPEC L276: "The station facility itself was destroyed, but not everything within it was obliterated". KLD L23 to L27: "The original surface facility is gone, not ruined-but-standing … there is a mountain where the base used to be". SIDE L23: Kendra is found in "a further, deeper series of underground chambers"; KLD L109 to L110: "likely where Kendra is trapped, near a buried underground access point … Underground … where Kendra is actually found". SIDE L73 flags this for reconciliation.

11.2 **CONFLICT. What defeated Kendra.** DLC1 L156: "Primary framework: Option D (environment + attrition + enemies that prevent recovery)", confirmed. KLD L48 to L49: "she wasn't defeated by an enemy. She was defeated by the collapse itself" (proposed).

11.3 **CONFLICT. Ice thickness.** See 1.3.

11.4 **CONFLICT. Precipitation.** CULT L44: "~20–25mm annual precipitation". SPEC L157, L163 to L166: gauge 2.1 mm; falls about 70 mm; lands about 70 to 80 mm. Also within SPEC: "Falls … ~70 mm/yr" against "Lands … ~70–80 mm/yr" with "falls ≈ lands" (SPEC L164 to L165).

11.5 **CONFLICT. Driest and coldest.** CULT L44: "the driest site in Tepenia"; `Specs/Mirny subnet/Kunlun.md` L142: "even less precipitation than Ariun Nuur or Amundsen Station" (via INV L515). SPEC L213: "The most extreme cold of any location in Tepenia" and CULT L44 "The most extreme climate of any location"; Ariun Nuur's culture sheet: "The coldest sustained environment of any Tepenian city — mean annual temperature −54.8°C" (via INV L297), against the station's −49.1 °C (SPEC L152).

11.6 **CONFLICT. Extent.** The extent table: 1 km² (via INV L489). TOWER L946: the Tower's surface complex alone "plausibly on the order of 1–2 km²".

11.7 **CONFLICT. Wind.** TOWER L766 to L767: ice ridges "double as windbreaks against Antarctic katabatic winds". SPEC L169: the site "sits above the katabatic regime … Air movement is close to irrelevant". (DLC1 L66 to L71's periodic blizzards are a gameplay system; SPEC L169 says visibility closes only when something is actually falling.)

11.8 **CONFLICT. Geothermal at the station.** DLC1 L194: "a pre-war maintenance hatch for the station's geothermal power infrastructure". POWER L16: "The six geothermal cities were the only cities whose heat did not depend on the grid" (the station is not one of the six; POWER L29 to L31). TOWER L933 to L934 proposes "geothermal taps into Antarctic subglacial volcanic activity" (SOFT).

11.9 **CONFLICT. Nuclear power.** See 5.7.

11.10 **CONFLICT. When the relay began.** SPEC L221: founded post-Treaty "maintaining the Arcanet relay hardware and, later, the Amundsen Tower"; TOWER L1057: the Arcanet "gradually connected subnet by subnet" before the Tower. `City_National_Connections.md` L5: "once the Amundsen Tower's completion connected all six subnets through a single relay for the first time" (via INV L520).

11.11 **CONFLICT. Tower staff in the Census I era.** Census I is "before construction of Amundsen Tower" (via INV L403; `DR-69`, DRL L1351) and the town is built to Census I (`DR-4`). The Division of Industry gives 30% of the distinctive tier (1,288 workers) to Tower operations on the Census I workforce (`16` L3456 to L3474, via INV L519).

11.12 **CONFLICT. Hostel beds in Census I.** `DR-65` (DRL L1305): "about 287 hostel beds in Census I". `DR-69` (DRL L1351): "there is no space workforce in Census I".

11.13 **CONFLICT. Division of Industry status.** See 6.10.

11.14 **CONFLICT. "Facility" versus town.** CULT L5: "Amundsen Station was never a city"; CULT L242: "there was no 'resident' category"; MS-PHYS L80 to L81: "Living quarters sized for a rotating technical crew, not a permanent population"; MS-PHYS L146 to L148: "the same 'facility, not a city' discipline"; MREF L248: "Never a settlement". Ruled since: SPEC L15, L221, L229 town wording (`DR-98` item 5). The ruling governs; the older sheets have not been updated.

11.15 **CONFLICT. Composition.** CULT L26 to L28: Primary China, USA; Significant Japan, Germany, UK, South Korea, Canada, Australia; Notable Argentina, Norway, New Zealand, Chile. MS-COMM L15 to L18: the tier table "describes Antarctic-program national origin". Ruled since: the national composite (`DR-98`; SPEC L19 to L21). The ruling governs.

11.16 **CONFLICT. Highways (now settled in the spec).** MREF L252: "Three confirmed highways converge here … Hwy 175 (terminates), Hwy 59 (terminates)". MREF L274 and SPEC L7: one highway reaches the station; the other two end at ramps with Highway 22. The spec governs.

11.17 **CONFLICT. Tower type and build time.** SPEC L8: "site of the Amundsen Tower (space elevator)". TOWER L221 to L224: a polar space elevator "is a physical non-starter"; it is a space fountain. TOWER L63, L193: "~65-75 year total build"; TOWER L1060: construction proper "in the final ~12-17 years before completion". The universe repository "still states the older ~2630-2640 completion date" (TOWER L1128 to L1131).

11.18 **CONFLICT. Debris mass.** DLC1 L54: "millions of tons of debris from a near-orbit impact". TOWER L846: about 228,875 t reaches the ground; TOWER L773 to L774: the material "was never in orbit". (TOWER L550 puts the base facility itself at about 3 million t, which TOWER does not count as debris.)

11.19 **CONFLICT. Highest robot share.** CULT L11, MREF L232: "the highest robot proportion of any Tepenian population center". `16` L116: "Kunlun and Dome Fuji have ZERO humans" (via INV L517).

11.20 **CONFLICT. Fabrication chambers.** See 5.29.

---

## What I read

In full: SPEC (301 lines); INV (740 lines); FRAME; COMP; POWER (81 lines); TOWER (1,155 lines); MS-PHYS (355 lines); MS-COMM (150 lines); DLC1 (299 lines; one row about a later-stage topic skipped by instruction); VISION; CULT (274 lines); RCULT (407 lines); PRETRIP (573 lines; one row about a later-stage topic skipped by instruction); READER. In part: PACK sections 2.0, 3, 4 and 5 (L141 to L161, L255 to L400) plus its header (L1 to L7); MREF legend and Amundsen section (L1 to L19, L228 to L289); FREG rows L75 and L90; DRL rulings `DR-3` (via PRETRIP), `DR-4`, `DR-10`, `DR-16`, `DR-17`, `DR-19`, `DR-24` to `DR-27`, `DR-31`, `DR-32`, `DR-44` (Amundsen row), `DR-55`, `DR-58` and its open list, `DR-61`, `DR-63` to `DR-69`, `DR-89`, `DR-98`, `DR-100`, `DR-131`, `DR-137`, `DR-138`, `DR-140`, `DR-141`, `DR-143`, `DR-144`, `DR-145`, located by searching DRL's headings and text for the station, the Tower, the relay, Highway 22, the hostel, ice, eras and fabrication; SIDE L1 to L30, L68 to L75; KLD L1 to L60, L95 to L125, L155 to L200. Not opened: anything under `Background-Lore/`, any Byrd file, `graphify-out/`, the other megasheet files, the census, `Highways.md`, `Airports.md`, `Ports.md` and the Division of Industry files (their facts are cited through INV). No web research; no other file edited.
