# Tepenian City Relationship Database

**Purpose:** Consistency reference for written lore — journal entries, audio logs, terminal entries, transit logs, shipping manifests, NPC dialogue, etc. Cross-check any city-to-city reference against this file to catch geographic, logistical, or network errors before they enter the game.

**Sources:** Three reference maps —
- Antarctica station/national possession map
- Antarctica/Tepenia Highway Map (with highway routes drawn over)
- Arcanet Regional Subnets map

---

## 1. Highway Quick Reference

All highways are pre-Long Night War infrastructure. Post-war, coastal sections are partially or fully non-operational. Inland sections (particularly those connecting Concordia, Byrd, Vostok, and the South Pole ruins) may still be functional or partially maintained.

| Hwy # | Name | Nickname | Route Summary | Notes |
|---|---|---|---|---|
| **1** | Rothera Highway | "Palmer Highway" | Palmer City → Port Lockroy → Rothera → [West Antarctica] → Byrd → Framheim → Little America → Scott → Fort McMurdo | Western loop; only land route connecting the Antarctic Peninsula to the rest of Tepenia |
| **2** | Dumont Coast Highway | "DCH" | Casey → Dumont d'Urville → Cape Denison | Short coastal route along the Dumont d'Urville Sea |
| **4** | Mawson-Soyuz Highway | — | Mawson → Bharati → Soyuz | Short Indian Ocean coastal link |
| **7** | Belgrano Highway | "Atlantic Highway" | Belgrano → Halley → Aboa → Sanay → Troll → Lazar | Atlantic/Queen Maud Land coast spine; **does NOT pass through Neumayer** — Neumayer has a separate unnamed connector road |
| **7-ext** | Belgrano Highway Extension | — | Lazar → Princess Elisabeth → Sayowa; built **2611–2614** | Extends Hwy 7 eastward from its terminus at Lazar; only highway with confirmed in-world construction dates |
| **22** | Transcontinental Highway | — | Byrd (Amundsen Sea end) → **South Pole (Amundsen Station)** → [junction with Hwy 175] → [northern bend — junction with Hwy 59] → Zhongshan coast (multi-highway junction with Hwy 110) | Cross-continent spine from West Antarctica to East Antarctic coast; **corrected 2026-07-03 — confirmed against `Reference-Images/Maps/Antarctica_highway_map_by_topology.jpeg`: Hwy 22 DOES pass directly through the South Pole** (the purple route loops through the Amundsen-Scott Station pin). Still does not pass through Sayowa or Mawson. |
| **37** | Mountain Cut Throughway | — | Sayowa → Vostok → Kunlun → Concordia | East Antarctic **plateau** traverse — not through the Transantarctic Mountains; connects Indian Ocean coast to inland stations and Concordia |
| **59** | Atlantic Throughway | "Arcanet Line" | Halley (junction with Hwy 7) → [interior] → northern bend of Hwy 22 | **Connector highway, not a city-to-city road** — links Hwy 7 to Hwy 22; also carries the Arcanet cable along its full length; does NOT reach the South Pole or Concordia |
| **110** | Coastal Cut Highway | — | Zhongshan → Davis → Mirny → Casey → [inland spur to Concordia] | Main East Antarctic coastal route; Concordia spur exits from Casey end |
| **175** | Central Cut Throughway | — | South Pole (Amundsen Station) → [junction with Hwy 22] → junction with northern curve of Hwy 183 | Connects South Pole to the Janbogo subnet region; **shares its South Pole endpoint directly with Hwy 22** (both highways physically meet at Amundsen Station, not at a separate distant junction — corrected 2026-07-03); does NOT connect directly to Byrd |
| **183** | Janbogo Highway | — | Concordia (northern terminus) → [south, northern curve / junction with Hwy 175] → Scott → Fort McMurdo → Janbogo → Cape Adare → Zukelli | Connects Concordia to all Ross Sea coastal cities; Concordia is the inland terminus |
| **Neumayer connector** | *(unnamed)* | — | Nearest safe point on Hwy 7 (between Aboa and Sanay) → Neumayer | Small connector road; exact organization TBD |

**Route to Byrd from Concordia:** Hwy 183 (south) → junction with Hwy 175 → Hwy 175 → junction with Hwy 22 → Hwy 22 (Amundsen Sea direction) → Byrd. Multiple transfers; a very long journey.

---

## 2. Arcanet Regional Subnets

Six subnets, each named after its hub city. **Official names** are the hub city names — used in Arcanet documentation, government records, and signage. **Colloquial nicknames** in quotes are informal regional terms, not official designations.

| Subnet | Hub | Colloquial Nickname | Member Cities |
|---|---|---|---|
| **Palmer** | Palmer City | "American" | Palmer City, Rothera, Esperanza, Marambio, Sejong, Juan Carlos, Port Lockroy, Signy* |
| **Halley** | Halley | "Atlantic" | Halley, Belgrano, Neumayer, Sanay, Troll, Aboa, Lazar, Princess Elisabeth |
| **Mawson** | Mawson | *(none)* | Mawson, Sayowa, Soyuz, Bharati, Dome Fuji |
| **Mirny** | Mirny | "Australian" | Mirny, Vostok, Kunlun, Casey, Zhongshan, Davis |
| **Janbogo** | Janbogo | *(none)* | Janbogo, Fort McMurdo, Scott, Zukelli, Cape Adare, Dumont d'Urville, Cape Denison, Concordia |
| **Byrd** | Byrd | "Pacific" | Byrd, Framheim, Little America |

**Signy\*:** Shown with a dashed border on the Arcanet map — peripheral/weaker connectivity, due to being on an island (South Orkney Islands) off the main peninsula. Treat as intermittent or lower-bandwidth in lore.

**Colloquial nickname note:** "American," "Atlantic," "Australian," and "Pacific" are informal terms — not official. Characters from non-matching cities within these subnets (e.g., Rothera in the "American" subnet, Mirny in the "Australian" subnet) may find their subnet's nickname inaccurate or mildly irritating. Mawson and Janbogo have no established colloquial nicknames.

**Amundsen Station (South Pole):** **Confirmed: inter-subnet relay — neutral ground; not a member of any subnet.** The South Pole was the routing node through which all six subnets communicated with each other. When the Long Night War destroyed Amundsen Station, it severed all inter-subnet Arcanet connections simultaneously, causing the **Planetary Split Brain** — each subnet became permanently isolated, developing its own version of historical records, sometimes in direct conflict with other subnets. The last synchronized pre-split Arcanet archive is cached at the South Pole ruins — the only place in Tepenia where the full unified record can be recovered. See Split Brain rules in Section 4.

---

## 3. City Profiles

Organized alphabetically. Each profile contains the data needed to verify lore consistency.

---

### Aboa
- **Real station:** Aboa Station (Finland)
- **Region:** Queen Maud Land / King Haakon VII Sea (Atlantic coast)
- **Status:** Damaged; partially operational *(corrected 2026-07-03 from "Destroyed" — resolved as a middle ground between conflicting sources; see `Specs/Aboa.md`)*
- **Arcanet subnet:** Halley ("Atlantic")
- **Highways:** Hwy 7
- **Direct highway neighbors:** Halley (west), Sanay (east)
- **Notes:** Finnish-Swedish joint founding, the only dual-national founding in Tepenia; seasonal in real life — smaller settlement than year-round stations; Neumayer is nearby but off Hwy 7 (connector road)

---

### Amundsen Station *(South Pole)*
- **Real station:** Amundsen-Scott South Pole Station (USA)
- **Region:** South Pole — interior
- **Status:** Destroyed (Long Night War) — now a scrap mountain; most significant ruins in Tepenia
- **Arcanet subnet:** Inter-subnet relay — neutral ground; not a member of any subnet ✓
- **Highways:** Hwy 175 (one endpoint here); Hwy 22 may also pass through — confirm against map
- **Direct highway neighbors:** Hwy 175 south toward Hwy 183 junction / Ross Sea region
- **Notes:** Site of the Amundsen Tower (space elevator); destroyed by Upper Earth militaries; scrap confined to South Pole vicinity; last synchronized Arcanet archive is here; named after Roald Amundsen

---

### Belgrano
- **Real station:** Belgrano Station II (Argentina) ✓
- **Region:** Weddell Sea coast (Atlantic)
- **Status:** Damaged; partially operational
- **Arcanet subnet:** Halley ("Atlantic")
- **Highways:** Hwy 7 (western terminus)
- **Direct highway neighbors:** Halley (east, Hwy 7)
- **Notes:** Western terminus of Hwy 7; Hwy 59 originates at Halley, not Belgrano — Belgrano reaches Hwy 59 via Hwy 7 to Halley; Hwy 7 bears the "Belgrano" name; the Extension (2611–2614) extends east from Lazar, not from Belgrano. **Coastal port receiving South African summer freighter shipments** (raw materials from Africa) as part of the seasonal Halley subnet supply window — see `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`.

---

### [NAME TBD] *(location: Bharati Station)*
- **Real station:** Bharati Station (India)
- **Region:** Indian Ocean coast
- **Status:** Destroyed (Long Night War)
- **Arcanet subnet:** Mawson
- **Highways:** Hwy 4 — midpoint
- **Direct highway neighbors:** Mawson (west), Soyuz (east)
- **Notes:** India's second Antarctic station; between Mawson and Soyuz on the Hwy 4 coastal link. City name "Bharati" is a placeholder — location confirmed for future development; final name TBD. **Coastal port that received Australian freighter shipments** (raw materials, staged via Hobart/Fremantle) pre-destruction, as part of the Mawson subnet coastal supply line.

---

### Byrd
- **Real station:** Byrd Station (USA)
- **Region:** West Antarctica — inland
- **Status:** Survived — struggling (nature of struggle TBD)
- **Arcanet subnet:** Byrd ("Pacific") — **hub city**
- **Highways:** Hwy 1 (passes through), Hwy 22 (western/Amundsen Sea terminus)
- **Direct highway neighbors:** [Antarctic Peninsula via Hwy 1], [Ross Ice Shelf / Fort McMurdo via Hwy 1], [Hwy 22 junction with Hwy 175 going east]
- **Notes:** Only surviving city besides Concordia; ~1,530m altitude — lower than Concordia (3,233m); West Antarctic location; DLC centerpiece (storyline TBD); hub of the Byrd ("Pacific") Arcanet subnet; NOT directly connected to Hwy 175 — reach via Hwy 22. Inland, not a port itself — receives its share of New Zealand-sourced raw materials overland via Hwy 1 from the Ross Sea coastal ports (Fort McMurdo, Scott, Framheim, Little America).

---

### Cape Adare
- **Real station:** Cape Adare (historical expedition site)
- **Region:** Ross Sea coast
- **Status:** Destroyed (Long Night War)
- **Arcanet subnet:** Janbogo
- **Highways:** Hwy 183 — passes through
- **Direct highway neighbors:** Mario Zucchelli (west), Janbogo (south)
- **Notes:** Founded on earliest Antarctic expedition landing site; destroyed Long Night War. **Ross Sea coastal port receiving New Zealand freighter shipments** (raw materials) as part of the Ross region supply line — see `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`.

---

### Denison
- **Real station:** Cape Denison (historical — Mawson's 1912 base)
- **Region:** Dumont d'Urville Sea coast
- **Status:** Destroyed (Long Night War)
- **Arcanet subnet:** Janbogo ✓
- **Highways:** Hwy 2 (DCH) — eastern terminus
- **Direct highway neighbors:** Dumont d'Urville (west)
- **Notes:** Founded on Mawson's 1912 expedition base (Cape Denison); eastern end of Dumont Coast Highway; destroyed Long Night War; Census I population: 526,521 humans / 546,852 robots / 1,073,373 combined. **Dumont d'Urville Sea coastal port receiving Australian freighter shipments** (raw materials, staged via Hobart) — see `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`.

---

### Casey
- **Real station:** Casey Station (Australia)
- **Region:** East Antarctic coast / Dumont d'Urville Sea area
- **Status:** Destroyed (Long Night War)
- **Arcanet subnet:** Mirny ("Australian")
- **Highways:** Hwy 110 (Coastal Cut), Hwy 2 (DCH — western terminus)
- **Direct highway neighbors:** Mirny (west via Hwy 110), Concordia (inland spur via Hwy 110), Dumont d'Urville (east via Hwy 2)
- **Notes:** Junction city — where Hwy 110 and Hwy 2 meet; gateway between the Mirny subnet coast and the Dumont d'Urville Sea area. **Coastal port receiving Australian freighter shipments** (raw materials, staged via Hobart) — sits at the overlap of both the Mirny subnet and Dumont d'Urville Sea supply lines, both of which run through Australia.

---

### Concordia
- **Real station:** Concordia Station (France / Italy) ✓
- **Region:** East Antarctic plateau — inland (Dome C)
- **Altitude:** 3,233m
- **Status:** Survived — last major city; **primary game setting**
- **Arcanet subnet:** Janbogo
- **Highways:** Hwy 110 (NE exit → Casey coast), Hwy 37 (NW exit → Kunlun → Vostok → Sayowa), Hwy 183 (S exit — northern terminus → Ross Sea cities)
- **Direct highway neighbors:** Casey (Hwy 110 NE), Kunlun (Hwy 37 NW), [Hwy 183 south toward northern curve / Ross Sea]
- **Notes:** Three highway exits confirmed from city map; survived Long Night War due to inland position; French/Italian founding; Kharkovchanka tracked vehicles primary transport; full city logistics in `to-be-integrated/city-logistics/Concordia_City_Logistics.md`

---

### Davis
- **Real station:** Davis Station (Australia)
- **Region:** Indian Ocean coast / East Antarctica
- **Status:** Damaged; partially operational
- **Arcanet subnet:** Mirny ("Australian")
- **Highways:** Hwy 110 — midpoint
- **Direct highway neighbors:** Zhongshan (west), Mirny (east)
- **Notes:** Major Australian station; geographically between Zhongshan (Mirny subnet) and Mirny city. **Coastal port receiving Australian freighter shipments** (raw materials, staged via Hobart/Fremantle) as part of the Mirny/Mawson subnet coastal supply line — see `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`.

---

### Dome Fuji
- **Real station:** Dome Fuji / Valkyrie Dome (Japan)
- **Region:** East Antarctic plateau — inland (high altitude)
- **Altitude:** ~3,810m
- **Status:** Survived — too high altitude for viable large settlement
- **Arcanet subnet:** Mawson
- **Highways:** None — road-isolated ✓
- **Notes:** Japanese inland station; no highway connection confirmed; altitude too extreme for population growth; in Mawson subnet — connected via Arcanet cable, not road; access likely by Kharkovchanka or air

---

### Dumont d'Urville
- **Real station:** Dumont d'Urville Station (France)
- **Region:** Dumont d'Urville Sea coast
- **Status:** Damaged; partially operational
- **Arcanet subnet:** Janbogo
- **Highways:** Hwy 2 (DCH) — midpoint
- **Direct highway neighbors:** Casey (west), Cape Denison (east)
- **Notes:** Dumont d'Urville Sea named after this location/explorer; French station; major refugee source for Concordia (Dumont d'Urville Sea coast = primary refugee geography). **Primary Dumont d'Urville Sea port for Australian freighter shipments** (raw materials, staged via Hobart) — mirrors the real French IPEV logistics chain, which runs *L'Astrolabe* out of Hobart despite France being the founding/operating nation; see `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`.

---

### Esperanza
- **Real station:** Esperanza Base (Argentina) ✓
- **Region:** Antarctic Peninsula — northern tip
- **Status:** Damaged; partially operational
- **Arcanet subnet:** Palmer ("American")
- **Highways:** Hwy 1 — northern peninsula section
- **Direct highway neighbors:** Marambio (nearby), Sejong (nearby), Palmer City (south via Hwy 1)
- **Notes:** Oldest continuously occupied Antarctic station in real life; historic families; northern peninsula cluster alongside Marambio, Sejong, Juan Carlos

---

### Fort McMurdo
- **Real station:** McMurdo Station (USA) ✓
- **Region:** Ross Sea — Ross Island
- **Status:** Damaged; partially operational
- **Arcanet subnet:** Janbogo
- **Highways:** Hwy 1 (eastern terminus), Hwy 183
- **Direct highway neighbors:** Scott (adjacent, Hwy 183), Janbogo (north, Hwy 183), [West Antarctica / Byrd via Hwy 1]
- **Notes:** Largest Antarctic station in real life → largest pre-war Tepenian city; "Fort" = mining/resource-processing hub + deliberate reference to Fort MacMurray (Alberta, Canada); two-highway junction = major logistics hub; Scott directly adjacent; **does NOT connect to Hwy 37** — that route runs Sayowa→Vostok→Kunlun→Concordia on the East Antarctic plateau. **Ross Sea coastal port receiving New Zealand freighter shipments** (raw materials) — see `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`.

---

### Framheim
- **Real station:** Framheim Base (Norway — historical expedition)
- **Region:** Ross Ice Shelf
- **Status:** Historical site (pre-exile ruins)
- **Arcanet subnet:** Byrd ("Pacific")
- **Highways:** Hwy 1 — passes through ✓
- **Notes:** Roald Amundsen's 1911 South Pole expedition base; on Hwy 1 between Byrd and Scott/McMurdo. **Ross Sea coastal port receiving New Zealand freighter shipments** (raw materials) — see `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`.

---

### Halley
- **Real station:** Halley Stations I–VI (UK) ✓
- **Region:** Weddell Sea coast — Brunt Ice Shelf (Atlantic)
- **Status:** Damaged; partially operational
- **Arcanet subnet:** Halley ("Atlantic") — **hub city**
- **Highways:** Hwy 7 (hub/midpoint), Hwy 59 (originates here — junction with Hwy 7) ✓
- **Direct highway neighbors:** Belgrano (west, Hwy 7), Aboa (east, Hwy 7)
- **Notes:** Built on a **floating ice shelf** — the city literally moved over time; unique structural character no other Tepenian city shares; Hwy 59 (Arcanet cable line) originates at Halley and runs inland to Hwy 22's northern bend. **Hub port for South African summer freighter shipments** (raw materials from Africa) — as the subnet hub with the most developed port infrastructure, Halley is likely the primary receiving point for the seasonal Halley subnet supply window — see `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`.

---

### Janbogo
- **Real station:** Jang Bogo Station (Unified Korea) ✓
- **Region:** Ross Sea coast — Terra Nova Bay
- **Status:** Damaged; partially operational
- **Arcanet subnet:** Janbogo — **hub city**
- **Highways:** Hwy 183 — hub
- **Direct highway neighbors:** Cape Adare (north, Hwy 183), Scott / Fort McMurdo (south, Hwy 183)
- **Notes:** Primary active connection between Concordia and the outside world; supplies Concordia; major refugee source; Unified Korea founding; damaged but not fully destroyed = strategically critical. **Ross Sea hub port receiving New Zealand freighter shipments** (raw materials) — as the Janbogo subnet's hub with year-round ice-free access (Terra Nova Bay polynya), likely the primary receiving point for the Ross region supply line — see `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`.

---

### Juan Carlos
- **Real station:** Juan Carlos I Station (Spain) ✓
- **Region:** Antarctic Peninsula — Livingston Island
- **Status:** Destroyed (Long Night War)
- **Arcanet subnet:** Palmer ("American")
- **Highways:** Hwy 1 — northern peninsula section
- **Direct highway neighbors:** Peninsula cluster (Esperanza, Marambio, Sejong nearby)
- **Notes:** Spanish station, Livingston Island; northern peninsula cluster

---

### Kunlun
- **Real station:** Kunlun Station / Dome Argus (Sinian Federation — China)
- **Region:** East Antarctic plateau — inland (highest station)
- **Altitude:** 4,093m
- **Status:** Survived — too high altitude for viable large settlement
- **Arcanet subnet:** Mirny ("Australian")
- **Highways:** Hwy 37 ✓
- **Direct highway neighbors:** Vostok (one direction, Hwy 37), Concordia (other direction, Hwy 37)
- **Notes:** Highest station in Antarctica; Sinian Federation origin; altitude too extreme for population growth; in Mirny subnet despite Sinian Federation ownership — subnets were organized geographically, not nationally; on Hwy 37 between Vostok and Concordia

---

### Little America
- **Real station:** Little America Base (USA — historical expedition)
- **Region:** Ross Ice Shelf
- **Status:** Historical site (pre-exile ruins)
- **Arcanet subnet:** Byrd ("Pacific")
- **Highways:** Hwy 1 — passes through ✓
- **Notes:** Richard Byrd's expedition bases (1929–1958); adjacent to Framheim on the Ross Ice Shelf; on Hwy 1 between Byrd and Scott/McMurdo. **Ross Sea coastal port receiving New Zealand freighter shipments** (raw materials) — see `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`.

---

### Lazar *(location: Novolazarevskaya Station / Maitri Station site)*
- **Real stations:** Novolazarevskaya Station (Russia, continuously operated since 1961) and the adjacent Maitri Station site (India — unoccupied in Tepenia; see canon note in `Specs/Lazar.md`)
- **Region:** Queen Maud Land / King Haakon VII Sea (Atlantic coast)
- **Status:** Damaged; partially operational *(finalized 2026-07-03: near-coastal position + genuine megacity scale — badly bombed, not destroyed)*
- **Arcanet subnet:** Halley ("Atlantic")
- **Highways:** Hwy 7 (eastern terminus), Hwy 7-ext (origin point → Princess Elisabeth → Sayowa)
- **Direct highway neighbors:** Troll (west, Hwy 7), Princess Elisabeth (east, Hwy 7-ext)
- **Notes:** Eastern terminus of Hwy 7 proper; origin of the Belgrano Highway Extension (built 2611–2614). Name finalized 2026-07-03: founded as two settlements (Russian-run Novolazarevskaya and the non-Indian-repopulated Maitri site) that coalesced into one city, originally called Novolazarevskaya, later phonetically shortened to "Lazar" as USA/Germany/France/Brazil immigration overtook the Russian founding population. See `Specs/Lazar.md`.

---

### Marambio
- **Real station:** Marambio Base (Argentina) ✓
- **Region:** Antarctic Peninsula — northern tip
- **Status:** Damaged; partially operational
- **Arcanet subnet:** Palmer ("American")
- **Highways:** Hwy 1 — northern peninsula section
- **Direct highway neighbors:** Esperanza, Sejong, Juan Carlos (all nearby); Palmer City (south via Hwy 1)
- **Notes:** Has a runway in real life — likely a logistics/air transport hub in-game; Argentine station

---

### Zukelli
- **Real station:** Mario Zucchelli Station (Italy)
- **Region:** Ross Sea coast — Terra Nova Bay
- **Status:** Destroyed (Long Night War)
- **Arcanet subnet:** Janbogo
- **Highways:** Hwy 183 — southern terminus
- **Direct highway neighbors:** Cape Adare (east, Hwy 183)
- **Notes:** Italian station; confirmed Tepenian city name: Zukelli. Southern terminus of Hwy 183; Terra Nova Bay. **Ross Sea coastal port that received New Zealand freighter shipments** (raw materials) pre-destruction — see `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`.

---

### Mawson
- **Real station:** Mawson Station (Australia)
- **Region:** Indian Ocean coast
- **Status:** Damaged; partially operational
- **Arcanet subnet:** Mawson — **hub city**
- **Highways:** Hwy 4 (Mawson-Soyuz)
- **Direct highway neighbors:** Bharati (east, Hwy 4)
- **Notes:** Hub of the Mawson Arcanet subnet; Australian station; **Hwy 22 does not pass through Mawson** — Hwy 22 runs Byrd→Zhongshan coast, not through Mawson. **Hub port for Australian freighter shipments** (raw materials, staged via Hobart/Fremantle) — as the subnet hub, likely the primary receiving point for the Mawson subnet coastal supply line — see `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`.

---

### Mirny
- **Real station:** Mirny Station (Russia)
- **Region:** East Antarctic coast
- **Status:** Damaged; partially operational
- **Arcanet subnet:** Mirny ("Australian") — **hub city**
- **Highways:** Hwy 110 — midpoint
- **Direct highway neighbors:** Davis (west), Casey (east)
- **Notes:** Hub of the Mirny ("Australian") Arcanet subnet despite being Russian — subnets organized geographically, not nationally; primary refugee source for Concordia. **Hub port for Australian freighter shipments** (raw materials, staged via Hobart/Fremantle) — as the subnet hub, likely the primary receiving point for the Mirny/Mawson subnet coastal supply line, same real-world logistics pattern as Halley (subnet hub, different nationality) receiving South African shipments — see `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`.

---

### Neumayer
- **Real station:** Neumayer Station III (Germany) ✓
- **Region:** Queen Maud Land / King Haakon VII Sea (Atlantic coast)
- **Status:** Damaged; partially operational
- **Arcanet subnet:** Halley ("Atlantic")
- **Highways:** Unnamed connector road to nearest safe point on Hwy 7 (between Aboa and Sanay) ✓
- **Direct highway neighbors:** None via Hwy 7 directly — connected only via connector road
- **Notes:** **NOT on Hwy 7** — Hwy 7 passes directly from Aboa to Sanay; Neumayer is served by a small unnamed connector road branching off at the nearest geographically safe point; connector road organization TBD; this makes Neumayer slightly less accessible than other Hwy 7 cities. **Coastal port receiving South African summer freighter shipments** (raw materials from Africa) as part of the seasonal Halley subnet supply window — see `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`.

---

### Palmer City
- **Real station:** Palmer Station (USA) ✓
- **Region:** Antarctic Peninsula — Anvers Island (64°46'S, 64°03'W)
- **Status:** Destroyed (Long Night War) — first settled, first destroyed
- **Arcanet subnet:** Palmer ("American") — **hub city**
- **Highways:** Hwy 1 — western terminus / origin
- **Direct highway neighbors:** Port Lockroy (north, Hwy 1), Rothera (south, Hwy 1)
- **Notes:** First settled location in Tepenia (June 21, 2564); cultural and entertainment capital; 100 Miles Davis Blvd. is the first official address in Tepenia; most accessible from Upper Earth = first settled AND first heavily targeted; full lore in `Palmer_City.md`

---

### Port Lockroy
- **Real station:** Port Lockroy (UK) ✓
- **Region:** Antarctic Peninsula
- **Status:** Destroyed (Long Night War)
- **Arcanet subnet:** Palmer ("American")
- **Highways:** Hwy 1 — passes through
- **Direct highway neighbors:** Palmer City (north), Rothera (south)
- **Notes:** Founded on UK historical expedition base; on Hwy 1 between Palmer City and Rothera; destroyed Long Night War

---

### Princess Elisabeth
- **Real station:** Princess Elisabeth Station (Belgium)
- **Region:** East Queen Maud Land
- **Status:** Destroyed (Long Night War) *(finalized 2026-07-03 after two earlier revisions the same day — ruins with straggling survivors; see `Specs/Princess_Elisabeth.md`)*
- **Arcanet subnet:** Halley ("Atlantic")
- **Highways:** Hwy 7-ext (Belgrano Highway Extension) ✓
- **Direct highway neighbors:** Lazar (west, Hwy 7-ext), Sayowa (east, Hwy 7-ext)
- **Notes:** Belgian station; on the Belgrano Extension between Lazar and Sayowa; zero-emission design in real life, but the real station is actually famous for extreme wind exposure (gales to 300 km/h), surviving only via deliberate engineering, not natural shelter; at the eastern edge of the Halley subnet; destroyed in the Long Night War once that engineering failed — ruins with straggling survivors

---

### Rothera
- **Real station:** Rothera Station (UK) ✓
- **Region:** Antarctic Peninsula — Adelaide Island
- **Status:** Damaged; partially operational
- **Arcanet subnet:** Palmer ("American")
- **Highways:** Hwy 1 — the highway bears this name as primary designation
- **Direct highway neighbors:** Port Lockroy / Palmer City (north, Hwy 1), [West Antarctica toward Byrd, south via Hwy 1]
- **Notes:** Highway named "Rothera Highway" first, "Palmer Highway" as nickname — suggests Rothera was the more significant city at the time of naming, or naming ran south to north

---

### Sanay
- **Real station:** Sanae IV Station (South Africa)
- **Region:** Queen Maud Land / King Haakon VII Sea
- **Status:** Damaged; partially operational *(corrected 2026-07-03 from "Destroyed" — resolved as a middle ground; see `Specs/Sanay.md`)*
- **Arcanet subnet:** Halley ("Atlantic")
- **Highways:** Hwy 7
- **Direct highway neighbors:** Aboa (west, Hwy 7), Troll (east, Hwy 7)
- **Notes:** South African station; Queen Maud Land; Neumayer is nearby but on a connector road, not a direct Hwy 7 neighbor

---

### Scott
- **Real station:** Scott Base (New Zealand)
- **Region:** Ross Sea — Ross Island (adjacent to McMurdo)
- **Status:** Damaged; partially operational
- **Arcanet subnet:** Janbogo
- **Highways:** Hwy 183, Hwy 1 (eastern terminus)
- **Direct highway neighbors:** Fort McMurdo (adjacent), Janbogo (north, Hwy 183)
- **Notes:** Directly adjacent to Fort McMurdo on Ross Island; New Zealand station; junction of Hwy 1 and Hwy 183. **Ross Sea coastal port receiving New Zealand freighter shipments** (raw materials) — fittingly, given Scott's own real-world founding nation is New Zealand — see `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`.

---

### Sejong
- **Real station:** King Sejong Station (Unified Korea)
- **Region:** Antarctic Peninsula — King George Island
- **Status:** Destroyed (Long Night War)
- **Arcanet subnet:** Palmer ("American")
- **Highways:** Hwy 1 — northern peninsula section
- **Direct highway neighbors:** Peninsula cluster (Esperanza, Marambio, Juan Carlos nearby)
- **Notes:** Unified Korea's Antarctic presence alongside Janbogo; named after King Sejong the Great (Hangul alphabet creator); King George Island = slightly off the peninsula proper

---

### Signy
- **Real station:** Signy Station (UK) ✓
- **Region:** South Orkney Islands (Atlantic Ocean — north of Antarctic Peninsula)
- **Status:** Damaged; partially operational
- **Arcanet subnet:** Palmer ("American") — peripheral/dashed boundary
- **Highways:** None — maritime/air only ✓
- **Notes:** Northernmost Tepenian outpost; island location makes road connection impossible; Palmer subnet connection weak/intermittent (dashed border on Arcanet map); communications to/from Signy should reflect delays and dropouts in lore

---

### Soyuz
- **Real station:** Soyuz Station (Russia)
- **Region:** Indian Ocean coast
- **Status:** Destroyed (Long Night War)
- **Arcanet subnet:** Mawson
- **Highways:** Hwy 4 — eastern terminus
- **Direct highway neighbors:** Bharati (west, Hwy 4)
- **Notes:** Eastern terminus of Hwy 4; Russian station. **Coastal port that received Australian freighter shipments** (raw materials, staged via Hobart/Fremantle) pre-destruction, as part of the Mawson subnet coastal supply line.

---

### Sayowa
- **Real station:** Syowa Station (Japan)
- **Region:** Indian Ocean coast
- **Status:** Damaged; partially operational
- **Arcanet subnet:** Mawson
- **Highways:** Hwy 37 (western terminus → Vostok → Kunlun → Concordia), Hwy 7-ext (eastern terminus ← Princess Elisabeth ← Lazar) ✓
- **Direct highway neighbors:** Vostok (inland, Hwy 37), Princess Elisabeth (west, Hwy 7-ext)
- **Notes:** **Major junction city** — two highways converge here from very different directions; Hwy 37 goes inland to Concordia via the plateau; Hwy 7-ext connects westward to the full Atlantic coast highway system; Japanese station; significant Japanese presence in Tepenia alongside Sejong and Janbogo; **Hwy 22 does not pass through Sayowa**. **Coastal port receiving Australian freighter shipments** (raw materials, staged via Hobart/Fremantle) as part of the Mawson subnet coastal supply line — see `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`.

---

### Troll
- **Real station:** Troll Base (Norway)
- **Region:** Queen Maud Land
- **Status:** Damaged; partially operational
- **Arcanet subnet:** Halley ("Atlantic")
- **Highways:** Hwy 7
- **Direct highway neighbors:** Sanay (west, Hwy 7), Lazar (east, Hwy 7)
- **Notes:** Norwegian station; has a runway in real life; Queen Maud Land is Norwegian territorial claim

---

### Vostok
- **Real station:** Vostok Station (Russia)
- **Region:** East Antarctic plateau — inland
- **Altitude:** 3,488m
- **Status:** Survived — too isolated for self-support; small population or effectively abandoned
- **Arcanet subnet:** Mirny ("Australian")
- **Highways:** Hwy 37 ✓
- **Direct highway neighbors:** Sayowa (one direction, Hwy 37), Kunlun (other direction, Hwy 37)
- **Notes:** Russian inland station; sits above subglacial Lake Vostok — one of the largest lakes on Earth, buried under the ice; on Hwy 37 between Sayowa and Kunlun; **NOT on Hwy 59**

---

### Zhongshan
- **Real station:** Zhongshan Station (Sinian Federation — China)
- **Region:** Indian Ocean coast / East Antarctica
- **Status:** Damaged; partially operational
- **Arcanet subnet:** Mirny ("Australian")
- **Highways:** Hwy 110 (western terminus), Hwy 22 (eastern terminus — multi-highway junction here) ✓
- **Direct highway neighbors:** Davis (east, Hwy 110), [Hwy 22 → interior → Hwy 175 junction → Byrd]
- **Notes:** Named after Sun Yat-sen (courtesy name "Zhongshan") — well-respected historical figure; name retained under Sinian Federation ✓; major coastal junction where Hwy 22 and Hwy 110 meet. **Coastal port receiving Australian freighter shipments** (raw materials, staged via Hobart/Fremantle) as part of the Mirny subnet coastal supply line — see `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`.

---

## 4. Lore Consistency Rules

When writing any in-world text (journal entries, audio logs, terminal entries, transit/shipping logs, NPC dialogue), the following must hold.

### The Planetary Split Brain
The destruction of Amundsen Station severed all inter-subnet Arcanet connections permanently. Each of the six subnets has been informationally isolated since the Long Night War:
- **NPCs from different subnet backgrounds may have genuinely conflicting accounts of the same historical events** — neither is lying; they are each working from their subnet's isolated records
- **Written lore reflects the subnet of its author** — a Mawson-subnet refugee's account may directly contradict a Halley-subnet account
- **Concordia has only Janbogo subnet records** — the Janbogo account of history is the dominant narrative in Concordia by default, simply because it's the only one locally accessible
- **No city currently has access to another subnet's records** — the only place to reconcile the Split Brain is the South Pole ruins and the last synchronized pre-split archive cached there
- **The Split Brain is not a malfunction** — the subnets are functioning correctly within their isolation; this is a structural consequence of the relay going dark

### Geographic Rules
- **Concordia is the only fully functioning major city.** Byrd survives but is struggling. Most coastal cities were destroyed or severely damaged during the Long Night War — fully destroyed cities include Palmer City, Port Lockroy, Sejong, Juan Carlos, Sanay, Aboa, Soyuz, [NAME TBD — Bharati location], Casey, Denison, Cape Adare, Zukelli, and Amundsen Station. Princess Elisabeth is damaged but partially operational. Damaged but partially operational cities retain some surviving sections or populations. Dome Fuji and Kunlun survived but were never viable population centers.
- **Palmer City is on the Antarctic Peninsula** — as far from Concordia as any point in Antarctica. Palmer City refugees are rare in Concordia and traveled an exceptionally long way.
- **Janbogo is partially operational** — key link between Concordia and the outside world. Anything entering or leaving Concordia by ground passes through Janbogo.
- **Fort McMurdo and Scott are adjacent** on Ross Island — effectively twin cities, not distant settlements.
- **Amundsen Station (South Pole) is deep interior** — not coastal, not easily accessible, a major expedition destination.
- **Signy is an island** in the South Orkney Islands, north of the main continent. Travel to Signy is maritime only — no road connection exists.
- **Halley was on a floating ice shelf** — it moved. Characters from Halley would be aware their city literally drifted over time.
- **Sayowa is a major highway junction** — it's where Hwy 37 (inland plateau route to Concordia) meets Hwy 7-ext (Atlantic coast system). In lore, it was a significant transfer point between the two sides of the continent.

### Network Rules
- **Arcanet subnet official names** are the hub city names (Palmer, Halley, Mawson, Mirny, Janbogo, Byrd). Colloquial nicknames ("American," "Atlantic," etc.) are informal — use official names in any formal in-world documentation.
- **Hwy 59 carries both road traffic and Arcanet cable** — physical damage to Hwy 59 disrupts Arcanet connectivity across the Halley subnet's inland connection. These consequences are simultaneous.
- **Signy's Arcanet connection was weak/intermittent** — communications to/from Signy should reflect delays, dropouts, and lower bandwidth.
- **Amundsen Station was the inter-subnet relay** — any cross-subnet Arcanet communication in lore set before the Long Night War would have been routed through the South Pole.

### Highway Rules
- **Hwy 1 is the only land route connecting the Antarctic Peninsula to the rest of Tepenia** — travel from Palmer City to Concordia by ground: Palmer → Hwy 1 → Byrd → Hwy 22 → Hwy 175 junction → Hwy 175 → Hwy 183 → Concordia. Extremely long journey.
- **Hwy 7 does NOT pass through Neumayer** — Neumayer is on a small unnamed connector road. Transit logs and travel accounts should reflect that Neumayer required a detour off the main highway.
- **The Belgrano Highway Extension was built 2611–2614** — lore set before 2611 cannot reference it; lore set 2611–2614 could reference construction; lore set after 2614 treats it as existing infrastructure.
- **Hwy 37 is an East Antarctic plateau route** — Sayowa → Vostok → Kunlun → Concordia. It does NOT cross the Transantarctic Mountains and does NOT connect to Fort McMurdo or the Ross Sea cities.
- **Hwy 183 has Concordia as its northern terminus** — travel from Concordia to the Ross Sea cities (Fort McMurdo, Janbogo, etc.) uses Hwy 183 south. Shipping logs between Concordia and the Ross Sea reference Hwy 183.
- **Hwy 59 does NOT reach the South Pole or Concordia** — it is a connector between Hwy 7 and the northern bend of Hwy 22, carrying Arcanet cable. It is not a city-to-city road.

---

## 5. Open Questions (for future resolution)

- **Governmental capital of Tepenia** — which city served as the governmental center? (Palmer City was cultural, not governmental — TBD)
- **Neumayer connector road** — exact organization, name, and which precise point on Hwy 7 it branches from (between Aboa and Sanay, at nearest safe geographic point — details TBD)
- ~~**Hwy 22 at Amundsen Station** — does Hwy 22 pass through the South Pole, or does Hwy 175 connect to it at a point away from the South Pole? (confirm against map)~~ **RESOLVED 2026-07-03:** confirmed against `Reference-Images/Maps/Antarctica_highway_map_by_topology.jpeg` — Hwy 22 passes directly through the South Pole/Amundsen Station.
- ~~**Maitri rename** — city will be renamed in later documents; new name TBD~~ **RESOLVED 2026-07-03:** finalized as "Lazar" — see `Specs/Lazar.md` for the full two-settlement coalescence founding story.
- **Hwy 7 order between Belgrano and Aboa** — confirmed: Belgrano → Halley → Aboa; intermediate stops (if any) between Halley and Aboa not yet verified
