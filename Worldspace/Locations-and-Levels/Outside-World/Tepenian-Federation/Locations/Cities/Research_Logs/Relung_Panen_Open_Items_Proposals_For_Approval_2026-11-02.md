# Relung Panen: proposals for the open items (2026-11-02)

**Status: PROPOSALS ONLY. Nothing here is ruled or applied.** Written at the developer's request after the Relung Panen research (the files in this folder named `Relung_Panen_Port_Research_*`, `_Ocean_Research_*`, `_Intake_*`, `_Oasis_E_*`, `_Oasis_F_*`, `_Soil_Research_*`). I read the final sections of those files and the rulings that bind this city (the two-airport ruling and the Australian-side intake ruling of 2026-10-29), not every line of the 5,700 lines of logs. Every fact below is from those final sections; where I am inferring, it says so. **Nothing is ruled until you say so, and the research gives no recommendation of its own.**

**What your earlier rulings fix (so these proposals do not reopen them):** Relung Panen has two airports inside the Bunger Hills, one passenger (domestic) and one cargo (international, freight only). The Australian-side intake is a seasonal sea gateway that goes out to meet arrivals in summer, and in winter an isolated, air-only coastal airport with customs and immigration, with onward flights to Mirny; the summer supply ship stocks that airport for the winter. A fixed floating city was not adopted. Relung Panen inherits nothing from its seven source rows. Founders are Indonesia and Malaysia, jointly.

**How to answer:** for each proposal, "approve", "approve with changes", "choose option B", or "not yet".

---

## Proposal 1 · Where the two airports sit inside the Bunger Hills

**Proposed.**
- **Cargo airport (international freight): Transcription Gulf, on its lake ice.**
- **Passenger airport (domestic): the Apfel Glacier blue-ice strip.**

**Why.**
- Transcription Gulf has about 18.5 km² of level ice. The longest straight line is 7.7 km, along 060°/240°.
- Its ice measured 2.95 to 3.2 m thick by ground radar in 2019, and the lake does not break up.
- It has carried heavy aircraft before: two wheeled Il-18 airliners landed on a prepared strip there in December 1963, plus an Il-14 and ski Twin Otters.
- Freighters (a 767-300F, A330-200F or 777F) can reach the oasis one way from Hobart or Perth with their payload, if fuel is waiting at the oasis. None can make the round trip at full payload, so the cargo airport needs a fuel store.
- The Apfel Glacier strip is 2.34 km long on its surveyed line, on grounded blue ice, and has been surveyed for ski aircraft (An-2, BT-67). Twin Otter and Basler aircraft have the range for the hops to Mirny (347 km) and Casey (439 km).

**Known gaps (from the research).**
- Cryoconite pits up to 6 m long and 0.3 m deep in two of the gulf's three zones, and tidal cracks at its shores. The length free of pits is not known.
- Summer: a belt of surface lakes forms on the grounding zone from late November to February, and the Apfel strip has water-filled cracks and "water-logged areas" in summer. *My inference, not in the research:* both runways work best in winter and spring, which suits the plot (air carries freight when ships cannot come).
- Apfel's ice thickness and melt rate were not measured.

**Alternatives.** (B) Put both airports on the gulf ice (simplest, but one surface for both jobs). (C) Use Lake Figurnoye for the passenger airport (flat, a 5.5 km² stretch, but "mostly ice-free" in summer, winter thickness unknown, and a Li-2 broke through an oasis lake in 1966; the research does not name which lake).

**Would change if approved:** `Infrastructure/Airports.md` (siting notes on the two rows), the two airport maps (marker positions are illustrative), the spec's Highway/Airport wording, and the Pre-Trip's research addendum.

---

## Proposal 2 · The winter intake airport

**Proposed: Drygalski Island** (about 92 km north of Mirny), as the winter intake airport, used for the summer sea gateway's supply landing too.

**Why it fits your four conditions.**
- *Coastal and isolated:* an ice-capped island with open sea all round, no ground route to any city.
- *Reachable by the summer ship:* it faces open sea (ice edge about 41 m high in the elevation data, water about 86 m deep within 1 km of the edge), so the supply ship can stock it for winter.
- *Onward flight to Mirny:* only about 92 km, well inside Twin Otter or Basler range.
- *Room for a runway:* about 220 km² of ice cap, about 162 km² of it flat.
- It had a Soviet station (Mir) in 1960. That is real history only; under the station-builder rule it is not an input.

**Known gaps (the research could not find these).**
- Ice speed on the dome has no reliable measurement, nor does snow accumulation or crevassing.
- No ship landing at the island is recorded, and the 41 m edge makes a conventional landing doubtful.
- **No winter landing at any station on this coast was found.** The nearest precedent is McMurdo's August flights, which lose one to four days to weather in every season on record. So the intake should be designed as weather-gated, with expected delay days, and with a standing crew to groom the snow (clearing an unmaintained winter's drift is tens of thousands of cubic meters).
- Deep darkness is not the problem here (at this latitude there are about six hours of civil twilight at midwinter); cold is, but the airframe limits found are fuel (about −45 °C) and hydraulics, and both are managed in practice.

**Alternatives.** (B) **Mill Island:** 1,225–1,260 km², about 1,150 km² flat, north coast faces the sea, but 367 km from Mirny, fog and rime are reported and its ice speed is also unmeasured. (C) **Keep the site unnamed** and rule only its properties (isolated, island, ice cap, within Twin Otter range of Mirny), leaving the exact island for the cold run to settle.

**Would change if approved:** the Winter Intake Airport row in `Airports.md` and the marker on both maps (the position is currently a placeholder on the coast between Davis and Mirny), `Ports.md` §3e, and Mirny's amendment note (an amendment note, never an edit of the finished pass).

---

## Proposal 3 · The summer sea gateway (the form it takes)

**Proposed: a pair of ice-class ships.** One acts as the reception ship (immigration and customs processing, quarantine, holding rooms) and meets the arriving ship at the ice edge. The second is the working ship (stores and fuel for the winter airport, helicopters). People go ashore by helicopter, or by gangway onto fast ice where it is safe.

**Why.**
- Processing at sea is a working practice today: Australia and Hong Kong put immigration officers aboard at the last foreign port, with a processing space supplied by the ship. Ellis Island is the historical model: most people passed in 3 to 5 hours and a minority were held.
- Polar passenger-ship rules (IMO) suggest "pairing" ships so each can rescue the other, and plan for a five-day wait for rescue.
- Ships have stood 50 to 100 km off the Bunger Hills and flown in, repeatedly (1948, 1986, 2015, 2017–2022, 2024).
- Ship-to-fast-ice transfer by gangway is routine; the failure mode is the ice moving (at Davis in 2023, the ice behind the ship drifted off on day three).
- **Biosecurity:** isolated places layer their checks upstream (pre-departure isolation and testing at the gateway was the COVID-era norm in every Antarctic program). The sea gateway is where that check sits.

**Limits to keep in the design.**
- Helicopters carry few people: six seats on a BK117, five on some rules (so a rescue stays possible in one flight), and a published rule keeps them within 80 nautical miles of the ship, daylight only. A good evening was five flights of up to 12 people.
- The Antarctic season is October to April; a typical tour departure carries about 139 people. So immigration numbers per ship are small, or the ships work in waves.
- The sea between Australia and the ice is among the roughest anywhere (storm waves over 5 m about 44 separate storms a year at 60°S, 100°E; the 2025 *Nuyina* voyage logged waves over 10 m at 63°S). Ships cross that before they reach the gateway.

**Alternatives.** (B) A single ship (cheaper, but no mutual rescue and one point of failure). (C) A fixed station at the ice edge (the research found no year-round moored precedent in drifting pack, which is why the fixed floating city was dropped).

**Would change if approved:** `Ports.md` §3e (the gateway's form), the cold-chain wording, and the spec's maritime access paragraph.

---

## Proposal 4 · The port question

**Proposed.** **No conventional port is built at Relung Panen.** The food and bulk goods leave and arrive by the road spur to Casey and through Casey's port, which is already how your rulings route everything by land. The "port" at Relung is the seasonal gateway of proposal 3 (people and special cargo only). The subglacial route stays as lore, not as a working port.

**Why.**
- The ice cliff in front of the oasis is 24 to 36 m high (ICESat-2, 2023–2025) and moves kilometers; every working ice-front berth found is 10 to 17 m. Where a high shelf was used with a carved ramp (South Africa), vehicles and cargo slid on it.
- Cargo staged near shelf edges has been lost when the edge calved (Maitri 2012; Atka January 2026, after which the German institute set a 5 km setback).
- Heavy hauling over the shelf is a summer-only, GPR-led, slow operation (about 11 km/h, October to February). At helicopter loads, 100 tons needs about 17 to 84 sorties and 1,000 tons about 167 to 834.
- The eastern front is low (6 to 13 m) or absent, but behind it is an ice surface that may be thin or multiyear fast ice, and nothing about its strength was found.
- The research found only that water exists under the shelf (a float drifted there). **Nothing shows a ship could pass.**

**Alternatives.** (B) Keep the subglacial approach as a proposed fifth port tier for a later study. (C) Build an ice-front berth on the eastern low front (needs ice-strength data the research does not have).

**Would change if approved:** `Ports.md` (the Relung Panen entries), the spec's maritime access paragraph, and the cold-chain wording.

---

## Proposal 5 · The founding remainder (route, soil, first wave, relation to Casey and Davis)

**Proposed order of events (a sequence, not numbers):**
1. **Arrival by air, onto the gulf.** The real history supports it: ski and wheeled aircraft landed in the oasis in 1956 (An-2 on Lake Figurnoye), the 1960s (Il-14 on the gulf) and 1961–64 (Il-18s in the Bunger Hills).
2. **The road spur to Casey comes later**, once the oasis can export; Casey becomes the door and the junction, and the single road makes everything pass through it.
3. **Soil is made on site** from imported organic matter and local rock, with the growing done in stacked hydroponics from the start. The soil research gives the precedents (compost on sand at SEKEM in Egypt, Negev runoff fields, the made-ground idea); the city's soil route is "made ground", not a natural soil.
4. **Davis is the science partner** (the joint agricultural research project already ruled), **Casey is the physical door.** That keeps each tie to one job.
5. **First-wave size:** I would not propose a figure. The research has none, and any number would be invented. I propose ruling the *shape* (a small founding party, grown over decades) and leaving the numbers to the culture run.

**Would change if approved:** the spec's founding paragraph and the Development Brief's open-question list, and the founding line in `ULM_Input_Status.md`.

---

## Proposal 6 · Power

**Proposed: a grid line along the same road spur from Casey, with local generation as a backup only.**

**Why, and how sure I am: not very.** This is the least-researched item.
- Canon has a regulated continent-wide grid, but the file that would describe it (`Infrastructure/Amundsen_Power_Supply.md`) is **empty**. Canon also says Tepenia is a cold country that heats with electricity (the Norway analogy), so a city of one million needs a large supply.
- At the oasis: no geothermal, no measured wind resource, a mean wind of 4.6 m/s at one station and 6.8 m/s at another (with 122 days a year over 15 m/s and a 56 m/s peak), midwinter sun for 2.5 hours, and continuous daylight for about 23 days. So solar and wind cannot carry the winter load.
- **Design payoff:** Relung's food then depends on one road and one power line, both through Casey. That matches the existing text that everything reaching or leaving the city by land passes through Casey, and it makes Casey's survival matter to the whole country's food.

**Alternatives.** (B) A local reactor (nuclear is mentioned for Concordia's core but is not canon for any city; the staffing reference gives about 0.62 workers per megawatt). (C) Rule only that power is "unresolved by design" until the national grid file exists.

**Recommended next step:** a short research pass on stacked-hydroponics power demand per person, so the demand is a number and not a guess.

**Would change if approved:** the spec's Economy & Industry line ("no geothermal, no measured wind resource, off-grid"), the input status, and `Amundsen_Power_Supply.md` (which is empty and would need its own task).

---

## Proposal 7 · The cold-chain share

**Proposed: 4% of the distinctive tier = 16,886 workers** (each point is about 4,221), which would raise the mandated total from 38% to 42% of the distinctive tier (21.3% to about 23.5% of the workforce) and lower the free tier from 34.7% to about 32.5% of the workforce.

**Why.** It carries the freezing and chilled storage and the cargo-airport and road-to-Casey handling for a city whose product is perishable. It sits beside the other three roles (4%, 3%, 6%). **It is a judgment call: no sourced staffing ratio was found for it, as for the seed and phosphorus shares.** It should follow proposals 1 to 4, since the airport and road decide what has to be chilled and moved.

**Alternatives.** (B) 3%. (C) 6%, if the road and a long cold-chain are treated as national infrastructure like phosphorus recovery.

**Would change if approved:** the determination file (`18`), `16` Half B and `09` for this city, and its Phase 4 and Phase 7 datasheets (all re-run as I did today for the population change).

---

## Proposal 8 · The 71 further inspiration candidates (for tomorrow's window)

**Proposed:** tomorrow from 05:00, propose tiers for the 71 from the 24 inspiration research files, in the same way the first 28 were done (seven research-based tier changes proposed, two Primary kept). This is creative work, so it falls in the 05:00–14:59 window and I am not starting it tonight.

---

## What I would do first if you approve

1. Proposals 1 to 4 together (they interlock), then 7.
2. Then 5, then power (6) after the short power research.
3. Each applied change goes into the rulings log, the airport/port files, the maps' notes and the Relung Panen sheets, with a diff shown to you before anything outside the Relung folder is edited.
