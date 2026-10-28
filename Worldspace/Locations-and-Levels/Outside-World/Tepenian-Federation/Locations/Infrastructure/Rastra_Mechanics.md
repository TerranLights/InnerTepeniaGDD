# The Rastra: mechanics and status

> **Created 2026-10-28** at the developer's direction ("there should be a file specifically on Rastra mechanics. If not, we need to make one"). A search of every repo that day found **no file on the Rastra's mechanics and no numeric spec for it anywhere**; `City_Logistics.md` L266 lists "full Rastra fleet details" as an open question. This file is the home for them.
>
> **How to read it.** Section 1 is ruled. Section 2 is what canon already says, with citations, nothing added. Section 3 is real-world reference only (not canon). Section 4 is what is **not yet ruled**, with options offered as questions, **never as canon**. Only Section 1 and Section 2 may be cited as Tepenian fact.

---

## 1 · Ruled

| Item | Ruling | Source |
|---|---|---|
| **Later-era cruise speed** | **About 45 km/h** ("advanced tracked or hybrid"): the official base of reference for a mature Rastra, once Tepenians had learned to build them. | `DR-63` (2026-10-28), Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md |

Working assumptions that are **not** rulings: 20 driving hours a day with relief drivers sleeping aboard, and a 10 to 15% allowance for stops. See `Population_Scenario_Santa_Luce_Redistribution_2026-10-28.md` section 6 for the travel times these give.

---

## 2 · What canon already says (qualitative only)

**What it is.** "Massive, enclosed, heated cabins on tracked chassis," descended from real Soviet-era Kharkovchanka vehicles; "slow, reliable, able to operate in conditions that disable lighter vehicles." (`Worldspace/City_Logistics.md` L127.) Concordia's spec calls it "the nationwide heavy tracked vehicle lineage descended from real Soviet-era Kharkovchanka designs, adapted for the Antarctic plateau" and the primary mode of surface travel between Concordia and outside points (`Specs/Janbogo subnet/Concordia.md` L80). Surface travel on the plateau is "dangerous and slow, primarily via Rastra convoy" (`City_Logistics.md` L139).

**Where it came from (the lineage).**
1. **Belgrano** built a rough first-generation tracked hauler, colloquially **"la Arrastradora"** ("the Hauler"), "a genuine local advance on the basic Soviet-derived Kharkovchanka design," from technical archives its engineers had preserved, never tested for a long crossing (`Specs/Byrd subnet/Byrd.md` L219).
2. A small Belgrano crew drove it north to **Neumayer**, whose founding-era scientists reverse-engineered it and **redesigned it to survive the distance**; the rebuilt vehicle, not the prototype, made the crossing to Byrd and back and became the template for what spread nationally (`Byrd.md` L219; `Local_Cultures/Halley_Subnet/Neumayer.md` L36). Every Rastra since descends from that redesign.
3. **The name.** "las Arrastradoras" in the plural, worn down by non-Spanish-speaking cities into "**Rastra**"; "Arrastradoras" stays the term of record in Belgrano (`Byrd.md` L219).
4. **The crew.** The crossing to Byrd used an all-robot crew, deliberately, because the unmapped territory was judged too risky for humans (`Byrd.md`; `Local_Cultures/Byrd_Subnet/Byrd.md` L36, L163).
5. **Later use in orbit.** Neumayer's file says Rastras were built "on the ground or, later, refitted for orbit" (`Neumayer.md` L36). The word was later reused for small space vehicles (tugs, shuttles, maintenance craft); see the project notes on the Belgrano and Byrd expedition.

**Role in the world.**
- **The established convoy vehicle used everywhere**; "the single most common vehicle in the country" (`Weapon_Item_Catalog.md` L257; Halley DLC candidate 01). Its kit: tire iron, jumper cables, windshield ice-scraper (`Weapon_Item_Catalog.md` L257 to L260).
- **Convoy escort**: the autocannon is "convoy-escort-mounted, protecting a Rastra convoy rather than a person" (`Weapon_Item_Catalog.md` L74; `Weapons_and_Tools_Philosophy.md` L33).
- **Concordia**: Rastra shuttles carry heavy inter-district and between-junction surface travel (`City_Logistics.md` L28, L127).
- **Sagittarius (the Frostlands)**: communally-owned Rastras "treated as critical infrastructure rather than convenience," with a buddy-system culture (nobody works outdoors alone) (`Concordia_Mega_Init.md` L44; `District_Vision_Notes/Sagittarius.md` L17).
- **Highways** are maintained in part by the Neon Nomads, highway clans who live on the roads (`City_Logistics.md` L139).

**Who builds and maintains them.**
- **Belgrano**: the Rastra Garages (specialist mechanic workshops "for anything with an engine"), the Spare-Parts Fabrication Yards, Garage Nights, and Expedition Day. About 20% of its workforce is mechanical maintenance, including Rastras (`Local_Cultures/Halley_Subnet/Belgrano.md` L138, L159; `City_Megasheets/Halley_Subnet/Belgrano/`).
- **Byrd** plausibly still builds them (TODO, long-haul cities note).
- **Supply chain**: Rastra spare parts, made in Belgrano's fabrication economy, pass through the same freight network as Cradle chamber freight and are exposed when Troll's control is contested (Halley DLC candidate 01).
- **Depots and homes**: Rastra depots anchor explorer-guild districts and player-home types near supply routes (`Player_Homes.md` L669 to L671).
- **Michelle Stanton** built the Arcanet in a Rastra with a small team of robots and dedicated humans (TODO; separate, later event from the Byrd crossing).

---

## 3 · Real-world reference (not canon)

Research done 2026-10-28; see the sources at the end. Use these to **ground** later rulings, not to state facts about Tepenia.

| Vehicle | Type | Speed | Range / load | Note |
|---|---|---|---|---|
| Kharkovchanka (Soviet, 1957 on) | Tracked, enclosed | 30 km/h cruise, 56 km/h max | About 1,500 km on its fuel; tows up to 60 t; 35 t, 995 hp V-12 diesel; eight beds, galley, toilet | The named ancestor |
| Common tracked polar vehicles today | Tracked | About 15 km/h | Higher fuel burn | |
| Ivan the Terra Bus (Foremost, 1991) | Wheeled, three-axle bus | About 40 km/h top | 56 passengers, 300 hp | Passenger comparison |
| Arctic Trucks AT44 | Modified wheeled trucks | About 21 km/h average over a 2,308 km run to the Pole in 4.5 days | | Includes stops and weather |
| South Pole Traverse | Tractor and sled trains | About 64 km/day outbound (about 25 days for 1,600 km), faster on the return | | A freight benchmark |
| China's Snow Leopard 6x6 (2026) | Wheeled | 28 km/h soft snow, 42 km/h hard snow, 65 km/h cruise on solid ice | About 700 km per tank; 10,000 km of tests without a failure | Shows a faster, shorter-range design |

**Reading across them:** better manufacturing mostly buys range, reliability and comfort; sustained speed gains are modest for a heavy tracked passenger hauler. About 45 km/h is plausible with modern drivetrains and composites on a maintained highway; much beyond 50 to 60 km/h points to wheeled or hybrid running gear and a prepared surface. Fast designs tend to give up range.

---

## 4 · Not yet ruled (questions, with options offered, none of them canon)

1. **Early-era speed** (the first Arrastradoras and first-generation Rastras). Slower than 45 km/h; the Kharkovchanka's 30 km/h is only a stand-in.
2. **Range and fuel.** Options: a Kharkovchanka-like ~1,500 km; or longer. Every Hwy 22/175/183 route from Amundsen Station other than Byrd exceeds 1,500 km, so this decides how many fuel or charging stops the highways need.
3. **Power source.** Diesel, electric, hybrid? Ties to the national energy scarcity and to how fuel is made or imported.
4. **Capacity.** Passengers, cargo tonnage, towing; a passenger Rastra versus a freight Rastra (the Kharkovchanka lineage carries both).
5. **Crew and driving.** How many drivers, relief shifts, sleeping berths; robot versus human drivers (the founding crew was all-robot).
6. **Cabin and survival.** Heating, redundancy, shelter if disabled, emergency beacons, the buddy system.
7. **Terrain handling.** Crevasse avoidance, whiteout navigation, sastrugi, wind (Belgrano's winds exceed 200 km/h); GPS or other guidance; how Neon Nomads maintain highways.
8. **Convoy rules.** Minimum convoy size, spacing, escorts (the autocannon implies armed escort in some eras), radio relays.
9. **Maintenance cycle.** Intervals, field repair, spare-parts depots along the highways.
10. **Variants.** Passenger shuttle, freight hauler, command or expedition model, the Concordia inter-district shuttle, and the orbital "Rastra" (tugs, shuttles, maintenance craft): shared lineage or just a shared name?
11. **Numbers per route.** Fuel stops, rest stops and refuel points on Hwy 22, 175 and 183 (see the scenario file section 6).
12. **Cost and ownership.** Communally owned in the Frostlands; who owns convoy and freight Rastras elsewhere.

---

## 5 · Related files

- Highways: `Locations/Infrastructure/Highways.md` (routes, junctions, maintenance, hitchhiking rules).
- Ruling: `Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md`, `DR-63`.
- Travel-time worked example: `Universal_Location_Methodology/Population_Scenario_Santa_Luce_Redistribution_2026-10-28.md`, section 6.
- Open item this resolves in part: `Worldspace/City_Logistics.md` L266 ("full Rastra fleet details"). **That line was not edited.**

## 6 · Sources for Section 3

[Kharkovchanka (Wikipedia)](https://en.wikipedia.org/wiki/Kharkovchanka) · [Arctic Juggernauts (Australian Antarctic Division)](https://www.antarctica.gov.au/news/stations/davis/2024/26-january/) · [Snow coach / Terra Bus (Wikipedia)](https://en.wikipedia.org/wiki/Snow_coach) · [Ivan the Terra Bus retired (Supercar Blondie)](https://supercarblondie.com/united-states-antarctic-program-ivan-the-terra-bus-retired) · [Arctic Trucks, South Pole drives (South Pole Station)](https://southpolestation.com/news/ventures3.html) · [Arctic Trucks, previous expeditions](https://arctictrucks.com/previous-expeditions/) · [South Pole Traverse (Wikipedia)](https://en.wikipedia.org/wiki/South_Pole_Traverse) · [China's Snow Leopard, 10,000 km (CGTN)](https://news.cgtn.com/news/2026-02-11/China-s-self-developed-Antarctic-vehicle-travels-over-10-000-km-1KFLdbhjtjq/p.html)
